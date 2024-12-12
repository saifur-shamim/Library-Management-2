import adding,viewing,updating,removing,lending,returning,viewing_borrower
import json, datetime

import viewing_borrower


def restore_all_books(book_list):
    with open("all_books.json", "r") as fp:
        book_list = json.load(fp)
    return book_list

def restore_all_book_taker_list(borrower_list):
    with open("lending_list.json", "r") as fp:
        borrower_list = json.load(fp)
    return borrower_list


book_list = []
borrower_list = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit ")
    print("1. Add Book" )
    print("2. View All Books ")
    print("3. Update Book ")
    print("4. Remove/Delete Book")
    print("5. Lend Book")
    print("6. Return Book ")
    print("7. View all book-taker list ")

    book_list = restore_all_books(book_list)
    borrower_list=restore_all_book_taker_list(borrower_list)
    option = input("Select Your Operation: ")

    if option == "0":
        print("Thanks for using Library Management System ")
        break
    elif option == "1":
        book_list = adding.add_books(book_list)
    elif option == "2":
        viewing.view_all_books(book_list)
    elif option == "3":
        updating.update_books(book_list)
    elif option == "4":
        book_list=removing.delete_books(book_list)
    elif option == "5":
        book_list=lending.lend_books(book_list,borrower_list)
    elif option == "6":
        book_list = returning.return_books(book_list, borrower_list)
    elif option =="7":
        viewing_borrower.view_book_taker(borrower_list)
    else:
        print("Choose a valid number")