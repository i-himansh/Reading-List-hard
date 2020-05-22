def add_books():
    title = input("Title: ").strip().title()
    author = input("Author:  ").strip().title()
    year = input("Publishing year:  ").strip()

    book = f"{title},{author},{year},Not read\n"

    with open('books.csv' , 'a') as reading_list:
        reading_list.write(book)

def get_all_books():
    books = []
    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            title, author, year, read_status = book.strip().split(",")

            books.append({
                'title' : title,
                'author': author,
                'year' : year,
                'read': read_status
            })
    return books


def show_book(books):
    print()
    for book in books:
        print(f"{book['title']}, by {book['author']} ({book['year']}) - {book['read']}")
    print()

def find_books():
    matching_books = []
    reading_list = get_all_books()

    search_term = input("Enter the title name to search the book : ").strip().lower()
    for book in reading_list:
        if search_term in book['title'].lower():
            matching_books.append(book)

    return matching_books

def delete_books():
    books = get_all_books()
    matching_books = find_books()

    if matching_books :
        books.remove(matching_books[0])

        with open("books.csv" , "w") as reading_list:
            for book in books:
                reading_list.write(f"{book['title']},{book['author']},{book['year']},{book['read']}\n")
    else:
        print("Sorry, we didn't find any books matching that title.")


def mark_book_as_read():
    books = get_all_books()
    matching_books = find_books()

    if matching_books :
        index = books.index(matching_books[0])
        books[index]['read'] = 'Read'

        with open("books.csv" ,"w") as reading_list:
            for book in books :
                reading_list.write(f"{book['title']},{book['author']},{book['year']},{book['read']}\n")



    else:
        print("Not matching book found")


menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'd' to delete a book
- 'l' to list the books
- 'r' to mark a book as read
- 's' to search for a book
- 'q' to quit

What would you like to do? """

user_input = input(menu_prompt).strip().lower() #userinput in lower and strip so that it dont count spaces
while user_input != 'q':
    if user_input == 'a':
        add_books()
    elif user_input == 'd':
        delete_books()
    elif user_input == 'l':
        reading_list = get_all_books()
        if reading_list:
            show_book(reading_list)
        else:
            print("List is empty")
    elif user_input == 'r':
        mark_book_as_read()
    elif user_input == 's':
        matching_books = find_books()
        if matching_books:
            show_book(matching_books)
        else:
            print("No matching books found")
    else:
        print("Input is not valid, please enter again.")

    user_input = input(menu_prompt).strip().lower()
