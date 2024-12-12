from saving import save_all_books
import random
from datetime import datetime


def add_books(book_list):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = int(input("Enter Publishing Year: "))
    price = int(input("Enter Book Price: "))

    while True:
        try:
            quantity = int(input("Enter Quantity Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    isbn = random.randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": bookAddedAt,
        "bookLastUpdatedAt": ""
    }

    book_list.append(book)
    save_all_books(book_list)

    print(f"{book['title']} Added Successfully ")

    return book_list
