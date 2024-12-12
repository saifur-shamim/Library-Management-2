import datetime, saving,json

def save_all_lending_books(borrower_list):
    with open("lending_list.json", "w") as fp:
        json.dump(borrower_list, fp, indent=4)

def lend_books(book_list,borrower_list):
    search_book = input("Enter Lending Book Title: ")
    for book in book_list:
        if book["title"] == search_book and book["quantity"]>0:
            book["quantity"] -=1
            book_last_updated_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            book["bookLastUpdatedAt"] = book_last_updated_at
            saving.save_all_books(book_list)
            name =input("Enter the book taker name ")
            phone = int(input("Enter the book taker phone no "))
            returndate = int(input("Enter days (how many days later will you return the book?) "))
            cdate = datetime.datetime.now()
            returndate = cdate + datetime.timedelta(days=returndate)
            returndate = str(returndate)
            cdate=str(cdate)

            book_taker = {
                "name": name,
                "phone": phone,
                "title": search_book,
                "takingdate": cdate,
                "returndate": returndate
            }
            borrower_list.append(book_taker)
            save_all_lending_books(borrower_list)
            print("Book lent Successfully")
            return book_list


    print(f"{search_book} is not available ")
    