import json

with open('receipts.json') as json_data:
    print(json_data)
    print(json.load(json_data))

def add_receipt(receipts):
    pass

def search_receipt_by_name(receipts):
    keyword = input("Enter part of the receipt name: ")
    found_receipts = []
    for receipt in receipts:
        if keyword.lower() in receipt["title"].lower():
            found_receipts.append(receipt)
    if found_receipts:
        print("Matching books:")
        for receipt in found_receipts:
            print(receipt['receipt'], "-", receipt['ingredients'])
    else:
        print("No matching receipts found.")

try:
    with open('receipts.json') as f:
        receipts = json.load(f)
except FileNotFoundError:
    print("Library file not found. Starting with an empty library.")

while True:
    print("\nPavārgrāmata")
    print("1. search by name")
    print("2. add receipt")
    print("3. search receipt without ingredient")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_receipt_by_name(receipts)

    elif choice == "2":
        add_receipt(receipts)

    

    elif choice == "3":
        pass


    elif choice == "4":
        # save books to file
        with open('books.json', 'w') as f:
            json.dump(receipts, f, indent=4)
        print("Library saved. Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")