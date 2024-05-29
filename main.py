import json

def search_receipt_by_name(receipts):
    keyword = input("Enter part of the receipt name: ")
    found_receipts = []
    for receipt in receipts:
        if keyword.lower() in receipt["receipt"].lower():
            found_receipts.append(receipt)
    if found_receipts:
        print("Matching receipts:")
        for receipt in found_receipts:
            print(receipt['receipt'], ": ingredients:   ", receipt['ingredients'], "; instruction:   ", receipt['instruction'])
    else:
        print("No matching receipts found.")

def add_receipt(receipts):
    receipt = input("Enter receipt name: ")
    ingredients = input("Enter ingredients: ")
    instruction = input("Enter instruction: ")
    new_receipt = {
        "receipt": receipt,
        "ingredients": ingredients,
        "instruction": instruction
    }
    receipts.append(new_receipt)
    print("Receipt added successfully.")

def search_receipt_without_ingr(receipts):
    keyword = input("Enter ingredient you don't have: ")
    without_receipts = receipts.copy()

    for receipt in receipts:
        if keyword.lower() in receipt["ingredients"].lower():
            without_receipts.remove(receipt)
    print("Matching receipts:", without_receipts)  
try:
    with open('receipts.json', mode="r", encoding="utf-8") as f:
        receipts = json.load(f)
        # print(receipts[0]['instruction'])
except FileNotFoundError:
    print("Library file not found. Starting with an empty library.")

while True:
    print("\nPavārgrāmata")
    print("1. Search by name")
    print("2. Add receipt")
    print("3. Search receipt without ingredient")
    print("4. Save and exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_receipt_by_name(receipts)

    elif choice == "2":
        add_receipt(receipts)

    

    elif choice == "3":
        search_receipt_without_ingr(receipts)


    elif choice == "4":
        # save receipts to file
        with open('receipts.json', 'w') as f:
            json.dump(receipts, f, indent=4)
        print("Receipts saved. Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")