import saving, datetime,lending


def delete_book_taker(borrower_list,search_book,name):
    for taker in borrower_list:
        if taker["title"] == search_book and taker["name"]==name:
            borrower_list.remove(taker)
            lending.save_all_lending_books(borrower_list)
            print("Book taker name deleted Successfully")
            return borrower_list
    print("Not Found")


def return_books(book_list,borrower_list):
    title = input("Enter Title of returning book: ")
    for book in book_list:
        if book["title"] == title:
            book["quantity"] +=1
            book_last_updated_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            book["bookLastUpdatedAt"] = book_last_updated_at
            saving.save_all_books(book_list)

            name =input("Enter the book taker name ")
            borrower_list=delete_book_taker(borrower_list,title,name)
            lending.save_all_lending_books(borrower_list)

            print("Book Returned Successfully")
            return book_list
    else:
        print("Invalid ")
