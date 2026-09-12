from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return self.name


class Member(Person):
    def role(self):
        return "Member: " + self.name


class Librarian(Person):
    def role(self):
        return "Librarian: " + self.name


class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def __str__(self):
        return self.title


class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, book, member):
        if book.available:
            book.available = False
            self.loans.append(Loan(book, member))
            print(member.name, "borrowed", book.title)

    def show_people(self):
        people = self.members

        for person in people:
            print(person.role())


# Create objects
library = Library()

book1 = Book("Python Programming")
book2 = Book("Database Systems")

member1 = Member("Ahmad")
member2 = Member("Ali")

librarian = Librarian("Mr. Karim")

# Add to Library
library.add_book(book1)
library.add_book(book2)

library.add_member(member1)
library.add_member(member2)

# Borrow book
library.borrow_book(book1, member1)

# Polymorphism
people = [member1, librarian]

for person in people:
    print(person.role())

# Output
print("Book:", book1)
print("Loan:", book1.title, "->", member1.name)