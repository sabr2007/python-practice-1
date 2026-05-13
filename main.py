from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser, CountryAnalyser, DataAnalyser


def main():
    # --- Setup ---
    fm = FileManager("students.csv")
    if not fm.check_file():
        print("Stopping program.")
        exit()
    fm.create_output_folder()

    dl = DataLoader("students.csv")
    dl.load()
    dl.preview()

    # --- Task 1 demo: base class shows it's a stub ---
    base = DataAnalyser(dl.students)
    print(base)
    base.analyse()

    # --- Polymorphism ---
    analysers = [
        GpaAnalyser(dl.students),
        CountryAnalyser(dl.students),
    ]

    print("-" * 30)
    print("Running all analysers:")
    print("-" * 30)

    for analyser in analysers:
        print(analyser)
        analyser.analyse()
        analyser.print_results()

    # --- Report (association) ---
    saver = ResultSaver(analysers[0].result, "output/result.json")
    report = Report(analysers[0], saver)
    report.generate()


if __name__ == "__main__":
    main()