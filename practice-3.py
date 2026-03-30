
store_info = ("FreshMart", "Astana, Respublika Ave 1", "+7 700 0000000")

print("=" * 30)
print(store_info[0])
print(store_info[1])
print(store_info[2])
print("=" * 30)

names = []
prices = []

while True:
    product_name = input("Enter product name (or 'done' to finish): ")
    if product_name == "done":
        break 
    price = float(input("Enter price: "))
    names.append(product_name)
    prices.append(price)
    

print("-" * 30)
print(f"Your cart ({len(names)} items):")
print("-" * 30)

for i in range (len(names)):
    print(f"{names[i]} - {prices[i]} KZT")

print("-" * 30)

weekly_products = set()

while True:
    product_names = input(("Enter product name (or 'done' to finish): "))
    if product_names == "done":
        break
    weekly_products.add(product_names)

unique_products = len(weekly_products)
print(f"Unique products: {unique_products}")
print(weekly_products)

print()

customer_name = input("Enter customer name: ")
subtotal = sum(prices)

discount = 0
discount_status = "No discount"

if subtotal >= 3000 and subtotal < 7000:
    discount = (subtotal * 5) / 100
    discount_status = "Standart discount"

elif subtotal >= 7000:
    discount = (subtotal * 15) / 100
    discount_status = "Premium discount"

total = subtotal - discount
receipt = {"customer": customer_name, "items": len(names), "subtotal": subtotal, "discount": discount, "total": total}

print("=" * 30)
print(f"RECEIPT - {store_info[0]}")
print("=" * 30)

print(f"Customer : {receipt.get("customer")}")
print(f"Items : {receipt.get("items")}")
print("-" * 30)

for i in range (len(names)):
    print(f"{names[i]} - {prices[i]} KZT")

print("-" * 30)

print(f"Subtotal : {receipt.get("subtotal")} KZT")
print(f"Discount : {receipt.get("discount")} KZT ({discount_status})")
print(f"Total : {receipt.get("total")} KZT")

print("=" * 30)
