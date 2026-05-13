class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        gpas = []
        high_performers = 0

        for student in self.students:
            try:
                gpa = float(student["GPA"])
            except ValueError:
                print(
                    f"Warning: could not convert value for student "
                    f"{student['student_id']} — skipping row."
                )
                continue

            gpas.append(gpa)
            if gpa > 3.5:
                high_performers += 1

        average_gpa = round(sum(gpas) / len(gpas), 2)
        max_gpa = max(gpas)
        min_gpa = min(gpas)

        high_gpa = list(filter(lambda s: float(s["GPA"]) > 3.8, self.students))
        gpa_values = list(map(lambda s: float(s["GPA"]), self.students))
        hard_workers = list(filter(lambda s: float(s["study_hours_per_day"]) > 4, self.students))

        print("-" * 30)
        print("Lambda / Map / Filter")
        print("-" * 30)
        print(f"GPA > 3.8 : {len(high_gpa)}")
        print(f"GPA values (first 5) : {gpa_values[:5]}")
        print(f"study_hours_per_day > 4 : {len(hard_workers)}")
        print("-" * 30)

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": average_gpa,
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,
            "high_performers": high_performers,
        }
        return self.result

    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"


class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        country_counts = {}
        for student in self.students:
            country = student["country"]
            country_counts[country] = country_counts.get(country, 0) + 1

        top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]

        self.result = {
            "analysis": "Country Analysis",
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3": top_3,
        }
        return self.result

    def print_results(self):
        print("=" * 30)
        print("COUNTRY ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"  