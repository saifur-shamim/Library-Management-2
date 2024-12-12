import saving


def delete_books(book_list):
    search_book = input("Enter Removing Book Title: ")
    for book in book_list:
        if book["title"] == search_book:
            book_list.remove(book)
            saving.save_all_books(book_list)
            print("Book Removed Successfully")
            return book_list

    print("Book Not Found")