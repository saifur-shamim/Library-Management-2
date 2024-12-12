
import json

def save_all_books(book_list):
    with open("all_books.json", "w") as fp:
        json.dump(book_list, fp, indent=4)