import json

def view_book_taker(borrower_list):
    with open("lending_list.json","r") as fp:
        borrower_list_list =json.load(fp)

    if borrower_list !=[]:
        print("Book taker list: ")
        for taker in borrower_list:
            print(f"Name: {taker['name']} | Phone: {taker['phone']} | Title: {taker['title']} | Taking Date: {taker['takingdate']} | Return Date: {taker['returndate']}")
    else :
        print("Empty List ")