'''
3. Library Manager - A Menu Driven Console Application

'''
import csv
from sys import exit
import re
import logging

# Variables to store the file names
BOOK_LIST = "BooksList"
MEMBER_LIST = "MembersList"
RENTAL_LIST = "BookRentals"

# Function to display the menu
def menu():
    print("----MENU-----")
    print("1. Add Books")
    print("2. Remove Books")
    print("3. Add Membership")
    print("4. Remove Membership")
    print("5. Rent Book")
    print("6. List Books")
    print("7. List Membership")
    print("8. Exit")

# Function to read the book details from file
def read_books():
    try:
        books = []
        with open(BOOK_LIST, newline="") as file:  # Reading from BooksList file
            reader = csv.reader(file)
            for row in reader:
                books.append(row)
        return books
    except FileNotFoundError as e:
        print("Could not find " + BOOK_LIST + " file.")
        logging.error("Could not find the file: ", BOOK_LIST)
        exit()
    except Exception as e:
        print(type(e), e)
        logging.error(type(e), e)
        exit()

# Function to read the member details from file
def read_members():
    try:
        members = []
        with open(MEMBER_LIST, newline="") as file:  # Reading from MembersList file
            reader = csv.reader(file)
            for row in reader:
                members.append(row)
        return members
    except FileNotFoundError as e:
        print("Could not find " + MEMBER_LIST + " file.")
        logging.error("Could not find the file: ", MEMBER_LIST)
        exit()
    except Exception as e:
        print(type(e), e)
        logging.error(type(e), e)
        exit()

# Function to write the book details to file
def write_books(books):
    try:
        with open(BOOK_LIST, "w", newline="") as file:  # Writing to BooksList file
            writer = csv.writer(file)
            writer.writerows(books)
    except Exception as e:
        print(type(e), e)
        logging.error(type(e), e)
        exit()

# Function to write the rental details to file
def write_rentals(rentals):
    try:
        with open(RENTAL_LIST, "w", newline="") as file:  # Writing to BookRentals file
            writer = csv.writer(file)
            writer.writerows(rentals)
    except Exception as e:
        print(type(e), e)
        logging.error(type(e), e)
        exit()

# Function to write the member details to file
def write_members(members):
    try:
        with open(MEMBER_LIST, "w", newline="") as file:   # Writing to MembersList file
            writer = csv.writer(file)
            writer.writerows(members)
    except Exception as e:
        print(type(e), e)
        logging.error(type(e), e)
        exit()

# Function to delete a book
def delete_book(books):
    list_books(books)
    print("Please note that deleting a book deletes the entire entry")
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:  # Value entered is not a number
            print("Invalid integer. Please try again.")
            logging.error("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(books):  # Value entered does not exist on list
            print("There is no book with that number. " +
                  "Please try again.")
            logging.error("Invalid book number")
        else:
            break
    book = books.pop(number - 1)
    write_books(books)
    print(book[0] + " was deleted.\n")
    list_books(books)

# Function to delete a member
def delete_member(members):
    list_members(members)
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:  # Value entered is not a number
            print("Invalid integer. Please try again.")
            logging.error("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(members):  # Value entered does not exist on list
            print("There is no member with that number. " +
                  "Please try again.")
            logging.error("Invalid member number")
        else:
            break
    member = members.pop(number - 1)
    write_members(members)
    print(member[0] + " was deleted.\n")
    list_members(members)

# Function to add a new book or increase number of copies of existing books
def add_book(books):
    isbn = input("ISBN: ")
    for item in books:
        if item[2] == isbn:  # Checking if the book already exits, if yes then increase the #copies
            copies = int(item[3])
            copies = copies + 1
            item[3] = copies
            write_books(books)
            print(item[0] + " already exists, so #copies was increased.\n")
            return True

    # If book does not exist then new book details are added
    name = input("Name: ")
    author = input("Author: ")
    book = []
    book.append(name)
    book.append(author)
    book.append(isbn)
    book.append("1")
    books.append(book)
    write_books(books)
    print(name + " was added.\n")
    return True

# Function that validates the phone number
def validatePhoneNumber(number):
    pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')  # Pattern for xxx-xxx-xxxx
    match = pattern.search(number)
    if match:
        return True
    return False

# Function that validates email by checking if it contains the symbol '@' and '.'
def validateEmail(email):
    valid = email.count("@") + email.count(".")
    if valid < 2:
        return False
    return True

# Function that adds new members
def add_member(members):
    name = input("Name: ")
    while name == "":  # Checking if name is empty
        print("Name cannot be empty! Please enter your name: ")
        name = input("Name: ")

    dob = input("DOB: ")
    while dob == "":  # Checking if dob is empty
        print("DOB cannot be empty! Please enter your DOB: ")
        dob = input("Name: ")

    phonenum = input("Contact Number (xxx)xxx-xxxx: ")
    while validatePhoneNumber(phonenum) == False:  # Checking if phone number is valid
        print("Please enter a valid Contact Number (xxx)xxx-xxxx")
        phonenum = input("Contact Number (xxx)xxx-xxxx: ")

    email = input("Email: ")
    while validateEmail(email) == False:  # Checking if email is valid
        print("Please enter a valid Email")
        email = input("Email: ")

    member = []
    member.append(name)
    member.append(dob)
    member.append(phonenum)
    member.append(email)
    members.append(member)
    write_members(members)
    print(name + " was added.\n")
    return True

# Function that lists all books
def list_books(books):
    print()
    print("*****************************BOOK DETAILS******************************")
    print('{:^5}{:^35}{:^15}{:^15}{:^5}'.format("#","NAME","AUTHOR","ISBN","COPIES"))  # Center aligned headings
    i = 1
    for book in books:
        print('{:^5}{:35} {:15} {:15}{:5}'.format(i,book[0],book[1],book[2],book[3]))  # Left aligned book details
        i = i + 1

# Function that lists all members
def list_members(members):
    print()
    print("**************************MEMBER DETAILS**************************")
    print('{:^5}{:^15}   {:^10} {:^15}{:^20}'.format("#","NAME","DOB","CONTACT_NO","EMAIL"))  # Center aligned headings
    i = 1
    for member in members:
        print('{:^5}{:15} {:10} {:15} {:20}'.format(i,member[0],member[1],member[2],member[3]))  # Left aligned member details
        i = i + 1

# Function to check if a member exists by email
def checkMembership(email, members):
    member = []
    for val in members:
        if val[3] == email:
            member = val
            return member
    return False

# Function to rent a book by entering user info and book info
def rent_book(books, members):
    print("Please enter your membership detail")
    email = input("Email: ")
    member = checkMembership(email, members)
    if member == False:
        print("Email not in list! Please register or try again!")
        return False

    print("Please choose the book you want to rent")
    list_books(books)
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            logging.error("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(books):
            print("There is no book with that number. " +
                  "Please try again.")
            logging.error("Book Number does not exists")
        else:
            break

    #  Decreasing the number of copies of the book chosen
    book = books[number - 1]
    copies = int(book[3])
    book[3] = copies - 1

    #  Creating a rental list to store the details of the book rented and user who rented it
    rentals = []
    rental = []
    rental.append(book[0])
    rental.append(book[3])
    rental.append(email)
    rentals.append(rental)
    write_rentals(rentals)  # Writing to the rental file

    write_books(books)  # Updating the book availability to file
    print(book[0] + " was rented.\n")
    list_members(books)

# Main function
def main():
    menu()
    books = read_books()
    members = read_members()

    while True:
        command = input("Command: ")
        if command == "1":
            add_book(books)
            print()
        elif command == "2":
            delete_book(books)
            print()
        elif command == "3":
            add_member(members)
            print()
        elif command == "4":
            delete_member(members)
            print()
        elif command == "5":
            rent_book(books, members)
            print()
        elif command == "6":
            list_books(books)
            print()
        elif command == "7":
            list_members(members)
            print()
        elif command == "8":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

# calling main function to execute first
if __name__ == "__main__":
    main()
