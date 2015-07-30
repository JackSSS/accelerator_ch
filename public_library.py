#!/usr/bin/env python
"""
The library should be aware of a number of distinct shelves.
Each shelf should know what books it contains. Create methods to add
and remove a book from a self. The library should have a method to report
all books it contains. Note: this should *not* be a Django (or any other)
app - just a single file with three classes (plus commands at the bottom
showing it works) is all that is needed.
"""


class Library(object):
    def __init__(self):
        self.books = [["four", "six", "five"], ["seven", "eight", "9"],
                      ["10", "11", "12"]]
        self.lib = {"sun": self.books[0], "rain": self.books[1], "snow":
                    self.books[2]}

    def shelf_name(self):
        """List distinctive shelves."""
        for i in self.lib.iterkeys():
            print(i)

    def shelf_num(self):
        """List number of shelves"""
        print(u"This library contains " + str(len(self.lib)) + " shelves.")


class Shelf(Library):
    def __init__(self):
        super(Shelf, self).__init__()

    def shelf_books(self):
        """Report books on shelf"""
        for s, b in self.lib.iteritems():
            print s, b


class Book(Shelf):
    def __init__(self):
        super(Book, self).__init__()

    def report_books(self):
        """ Reports all books in Library."""
        for s, b in self.lib.iteritems():
            for book in b:
                print book

    def add_book(self):
        """Add book to shelf"""
        user_book = raw_input(u"Create a book name: ")
        shelf_choice = raw_input(u"Choose a shelf to place '" +
                                 user_book + "' (sun, rain, or snow): ")
        self.lib[shelf_choice].append(user_book)
        print(self.lib[shelf_choice])

    def remove_book(self):
        """Remove book from shelf"""
        for s, b in self.lib.iteritems():
            print s, b
        user_book = raw_input(u"Type a book name to remove: ")
        shelf_choice = raw_input(u"From which shelf is the book '" +
                                 user_book + "': sun, rain, or snow? ")
        self.lib[shelf_choice].remove(user_book)
        print(self.lib[shelf_choice])

if __name__ == '__main__':

    x = Book()
    # Reports all books in Library.
    x.report_books()
    # List distinctive shelves.
    x.shelf_name()
    # List number of shelves.
    x.shelf_num()
    # Report books on shelf
    x.shelf_books()
    # Add book to shelf
    x.add_book()
    # Remove book from shelf
    x.remove_book()
