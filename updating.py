import saving
from datetime import datetime

def update_books(book_list):
    search_book = input("Enter Updating Book Title : ")
    for book in book_list:
        if book["title"] == search_book:
            title = input("Enter New Book Title: ")
            author = input("Enter Author Name: ")
            year = int(input("Enter Publishing Year : "))
            price = int(input("Enter Book Price: "))
            quantity = int(input("Enter Quantity Number: "))

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["bookLastUpdatedAt"] = book_last_updated_at

            saving.save_all_books(book_list)
            print("Book Updated Successfully")
            return book_list

    print("Book Not Found")