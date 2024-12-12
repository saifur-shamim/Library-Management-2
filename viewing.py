import json

def view_all_books(book_list):
    with open("all_books.json", "r") as fp:
        book_list=json.load(fp)

    if book_list !=[]:
        for book in book_list:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['bookAddedAt']} | Book Last Updated At: {book['bookLastUpdatedAt']}")
    else :
        print("There is no book in the list ")