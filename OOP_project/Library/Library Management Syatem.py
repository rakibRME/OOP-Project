# Admin email admin and Admin password admin
import hashlib
issue_book = []
#book_review = []
date = {}
user_info = []
books_list = []

class Book:
    def __init__(self, book_id, title, author, edition, num_book):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.edition = edition
        self.num_book = num_book
        self.available = True

class Library:

    def __init__(self):
        self.books = {}

        self.add_book("1", "physics", "topon", "5th", 1)
        self.add_book("2", "chemistry", "hazari", "1st", 5)
        self.add_book("3", "math", "su", "3rd", 7)

    def check_book(self, book_id):
        if book_id in self.books:
            return "true"
        else:
            return "false"

    def give_title(self, book_id):
        if book_id in self.books:
            for i in range(len(books_list)):
                if books_list[i]['book_id'] == book_id:
                    return books_list[i]['title']
                # break
    def give_author(self, book_id):
        if book_id in self.books:
            for i in range(len(books_list)):
                if books_list[i]['book_id'] == book_id:
                    return books_list[i]['author']
                # break
    def give_edition(self, book_id):
        if book_id in self.books:
            for i in range(len(books_list)):
                if books_list[i]['book_id'] == book_id:
                    return books_list[i]['edition']
                # break
    def add_book(self, book_id, title, author, edition, num_book):

        # book = Book(book_id, title, author, edition, num_book)
        if book_id not in self.books:
            self.books[book_id] = {'book_id': book_id, 'title': title, 'author': author, 'edition': edition, 'count': num_book}
            books_list.append(self.books[book_id])
        else:
            self.books[book_id]['count'] += num_book

    def issue_book(self, book_id):

        if book_id in self.books and self.books[book_id]['count'] > 0:
            date.update({book_id: input("When will you pay back? (date/month/year) ")})
            self.books[book_id]['count'] -= 1
            print("Book issued successfully.")
            issue_book.append(book_id)
        elif book_id in self.books and self.books[book_id]['count'] == 0:
            print(f"This book is not available now. But I can provide you {date[book_id]}")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        if book_id in issue_book:
            issue_book.remove(book_id)
            del date[book_id]
            self.books[book_id]['count'] += 1
            #book_review.append(dict({book_id: input("Please give review about this book ")}))
            print("Book returned successfully.")

        else:
            print("This book is not issued!")

    def edit_book(self, book_id, new_title, new_author, new_edition, new_count):
        if book_id in self.books:
            self.books[book_id]['title'] = new_title
            self.books[book_id]['author'] = new_author
            self.books[book_id]['edition'] = new_edition
            self.books[book_id]['count'] = new_count
            print("Book details updated successfully.")

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            for i in range(len(books_list)):
                if books_list[i]['book_id'] == book_id:
                    del books_list[i]
                    break
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    def search_book(self, book_id):
        if book_id in self.books:
            book_info = self.books[book_id]
            print(f"Book ID: {book_id}")
            print(f"Title: {book_info['title']}")
            print(f"Author: {book_info['author']}")
            print(f"Edition: {book_info['edition']}")
            print(f"Available Copies: {book_info['count']}")
            #print(book_review)
        else:
            print("Book not found.")

    def show_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("\nBooks in the library:\n")
            # for book_id, book_info in self.books.items():
            #     print(f"Book ID: {book_id}")
            #     print(f"Title: {book_info['title']}")
            #     print(f"Author: {book_info['author']}")
            #     print(f"Edition: {book_info['edition']}")
            #     print(f"Available Copies: {book_info['count']}")
            #     print("\n")
            for i in books_list:
                print(i)
            print("\n")
    def new_account(self, email, name, reg_num, phn, set_password):
         self.email = email
         self.name = name
         self. reg_num = reg_num
         self.phn = phn
         self.set_password = set_password
         user_info.append({reg_num: {"email": email, 'name': name, "phn": phn, "set_password": set_password}})

if __name__ == "__main__":
    library = Library()

    while True:
        print("1. Admin")
        print("2. User")
        choice = input("Enter your choice: ")
        if choice == '1':
            email = input("Enter Admin email: ")
            password = input("Enter Admin password: ")
            if(email == "admin" and password == "admin"):

                print("\nLibrary Management System:")

                while True:
                    print("1. Add Book")
                    print("2. Issue Book")
                    print("3. Return Book")
                    print("4. Edit Book")
                    print("5. Delete Book")
                    print("6. Search Book")
                    print("7. Show all Books")
                    print("8. See all members")
                    print("9. Logout")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        book_id = input("Enter Book ID: ")

                        # def generate_book_id(title, author, edition, num_book):
                        #     book_info = f"{title}{author}{edition}{num_book}"
                        #     hash_object = hashlib.md5(book_info.encode())
                        #     book_id = hash_object.hexdigest()[:4]
                        #     return book_id
                        # book_id = generate_book_id(title, author, edition, num_book)

                        if library.check_book(book_id) == "false":
                            title = input("Enter Title: ")
                            author = input("Enter Author: ")
                            edition = input("Enter Edition: ")
                            num_book = int(input("Enter number of books: "))
                            library.add_book(book_id, title, author, edition, num_book)
                            print("Book issued successfully.")
                        else:
                            num_book = int(input("Enter number of books: "))
                            library.add_book(book_id, library.give_title(book_id), library.give_author(book_id), library.give_edition(book_id), num_book)
                            print("Book issued successfully.")

                    elif choice == '2':
                        book_id = input("Enter Book ID to issue: ")
                        library.issue_book(book_id)

                    elif choice == '3':
                        book_id = input("Enter Book ID to return: ")
                        library.return_book(book_id)

                    elif choice == '4':
                        book_id = input("Enter Book ID to edit: ")
                        if library.check_book(book_id) == "false":
                            print("Book not found.")
                        else:
                            new_title = input("Enter New Title: ")
                            new_author = input("Enter New Author: ")
                            new_edition = input("Enter New Edition: ")
                            new_count = input("Enter New count: ")
                            library.edit_book(book_id, new_title, new_author, new_edition, new_count)

                    elif choice == '5':
                        book_id = input("Enter Book ID to delete: ")
                        library.delete_book(book_id)

                    elif choice == '6':
                        book_id = input("Enter Book ID to search: ")
                        library.search_book(book_id)

                    elif choice == '7':
                        library.show_books()

                    elif choice == '8':
                        if not user_info:
                            print("No member available")
                        else:
                            print("\nMembers:\n")
                            for i in user_info:
                                print(i)
                            print("\n")

                    elif choice == '9':
                        print("Logged out from the admin session.")
                        break

                    else:
                        print("Invalid choice. Please choose a valid option.")

            else:
                print("Wrong admin email or password!!")

        if choice == '2':
            reg_num = input("Enter User registration number: ")
            found_user = None
            key_exists = any(user_dict.get(reg_num) is not None for user_dict in user_info)
            if not key_exists:
            # if reg_num not in user_info:
                print("Welcome to RMEDU Library!!")
                name = input("Enter your name ")
                while True:
                    email = input("Enter your email ")
                    if "@rme.du.ac.bd" in email:
                        while True:
                            phn = input("Enter your phone number ")
                            if phn.isnumeric() == True and len(phn) > 10 and len(phn) < 14:
                                set_password = input("Set library password ")
                                print("Entry Successful!!")
                                library.new_account(email, name, reg_num, phn, set_password)
                                break
                            else:
                                print("Invalid phone number!!")
                        break
                    else:
                        print("Invalid email address!!")
            found_user = None
            for user_data in user_info:
                if reg_num in user_data:
                    found_user = user_data
                    break
            if found_user is not None:
                print("\nLibrary Management System:")
                user_password = input("Enter your password ")
                if user_password == found_user[reg_num]["set_password"]:
                    while True:
                        print("1. Issue Book")
                        print("2. Return Book")
                        print("3. Search Book")
                        print("4. Show all Books")
                        print("5. Logout")

                        choice = input("Enter your choice: ")

                        if choice == '1':
                            book_id = input("Enter Book ID to issue: ")
                            library.issue_book(book_id)

                        elif choice == '2':
                            book_id = input("Enter Book ID to return: ")
                            library.return_book(book_id)

                        elif choice == '3':
                            book_id = input("Enter Book ID to search: ")
                            library.search_book(book_id)

                        elif choice == '4':
                            library.show_books()

                        elif choice == '5':
                            print("Logged out from the user session.")
                            break
                    else:
                        print("Wrong user password!!")
                else:
                    print("Wrong user email or password!!")
        else:
            print("Wrong input")