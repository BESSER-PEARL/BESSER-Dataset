from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_BorrowedItem:

    def __init__(self, borrowDate: date, lastReturnDate: date, library_BorrowedItem: "library_Book" = None, BorrowedItem: "library_User" = None, borrowedItems: "library_User" = None):
        self.borrowDate = borrowDate
        self.lastReturnDate = lastReturnDate
        self.library_BorrowedItem = library_BorrowedItem
        self.BorrowedItem = BorrowedItem
        self.borrowedItems = borrowedItems
        
    @property
    def borrowDate(self) -> date:
        return self.__borrowDate

    @borrowDate.setter
    def borrowDate(self, borrowDate: date):
        self.__borrowDate = borrowDate

    @property
    def lastReturnDate(self) -> date:
        return self.__lastReturnDate

    @lastReturnDate.setter
    def lastReturnDate(self, lastReturnDate: date):
        self.__lastReturnDate = lastReturnDate

    @property
    def BorrowedItem(self):
        return self.__BorrowedItem

    @BorrowedItem.setter
    def BorrowedItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_BorrowedItem__BorrowedItem", None)
        self.__BorrowedItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user"):
                opp_val = getattr(old_value, "user", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user"):
                opp_val = getattr(value, "user", None)
                if opp_val is None:
                    setattr(value, "user", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def borrowedItems(self):
        return self.__borrowedItems

    @borrowedItems.setter
    def borrowedItems(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_BorrowedItem__borrowedItems", None)
        self.__borrowedItems = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User9"):
                opp_val = getattr(old_value, "User9", None)
                if opp_val == self:
                    setattr(old_value, "User9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User9"):
                opp_val = getattr(value, "User9", None)
                setattr(value, "User9", self)

    @property
    def library_BorrowedItem(self):
        return self.__library_BorrowedItem

    @library_BorrowedItem.setter
    def library_BorrowedItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_BorrowedItem__library_BorrowedItem", None)
        self.__library_BorrowedItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book"):
                opp_val = getattr(old_value, "library_Book", None)
                if opp_val == self:
                    setattr(old_value, "library_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book"):
                opp_val = getattr(value, "library_Book", None)
                setattr(value, "library_Book", self)

class library_User:

    def __init__(self, name: str, user: set["library_BorrowedItem"] = None, users: "library_Library" = None, User: "library_Library" = None, User9: "library_BorrowedItem" = None):
        self.name = name
        self.user = user if user is not None else set()
        self.users = users
        self.User = User
        self.User9 = User9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def User(self):
        return self.__User

    @User.setter
    def User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_User__User", None)
        self.__User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library2"):
                opp_val = getattr(old_value, "library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library2"):
                opp_val = getattr(value, "library2", None)
                if opp_val is None:
                    setattr(value, "library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def User9(self):
        return self.__User9

    @User9.setter
    def User9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_User__User9", None)
        self.__User9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "borrowedItems"):
                opp_val = getattr(old_value, "borrowedItems", None)
                if opp_val == self:
                    setattr(old_value, "borrowedItems", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "borrowedItems"):
                opp_val = getattr(value, "borrowedItems", None)
                setattr(value, "borrowedItems", self)

    @property
    def users(self):
        return self.__users

    @users.setter
    def users(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_User__users", None)
        self.__users = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library6"):
                opp_val = getattr(old_value, "Library6", None)
                if opp_val == self:
                    setattr(old_value, "Library6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library6"):
                opp_val = getattr(value, "Library6", None)
                setattr(value, "Library6", self)

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_User__user", None)
        self.__user = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BorrowedItem"):
                    opp_val = getattr(item, "BorrowedItem", None)
                    
                    if opp_val == self:
                        setattr(item, "BorrowedItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BorrowedItem"):
                    opp_val = getattr(item, "BorrowedItem", None)
                    
                    setattr(item, "BorrowedItem", self)
                    

class library_Book:

    def __init__(self, name: str, author: str, library_Book: "library_BorrowedItem" = None, Book: "library_Library" = None, books: "library_Library" = None):
        self.name = name
        self.author = author
        self.library_Book = library_Book
        self.Book = Book
        self.books = books
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__books", None)
        self.__books = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library"):
                opp_val = getattr(old_value, "Library", None)
                if opp_val == self:
                    setattr(old_value, "Library", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library"):
                opp_val = getattr(value, "Library", None)
                setattr(value, "Library", self)

    @property
    def library_Book(self):
        return self.__library_Book

    @library_Book.setter
    def library_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book", None)
        self.__library_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_BorrowedItem"):
                opp_val = getattr(old_value, "library_BorrowedItem", None)
                if opp_val == self:
                    setattr(old_value, "library_BorrowedItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_BorrowedItem"):
                opp_val = getattr(value, "library_BorrowedItem", None)
                setattr(value, "library_BorrowedItem", self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library"):
                opp_val = getattr(old_value, "library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library"):
                opp_val = getattr(value, "library", None)
                if opp_val is None:
                    setattr(value, "library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Library:

    def __init__(self, name: str, Library6: "library_User" = None, library: set["library_Book"] = None, library2: set["library_User"] = None, Library: "library_Book" = None):
        self.name = name
        self.Library6 = Library6
        self.library = library if library is not None else set()
        self.library2 = library2 if library2 is not None else set()
        self.Library = Library
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books"):
                opp_val = getattr(old_value, "books", None)
                if opp_val == self:
                    setattr(old_value, "books", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books"):
                opp_val = getattr(value, "books", None)
                setattr(value, "books", self)

    @property
    def Library6(self):
        return self.__Library6

    @Library6.setter
    def Library6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__Library6", None)
        self.__Library6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "users"):
                opp_val = getattr(old_value, "users", None)
                if opp_val == self:
                    setattr(old_value, "users", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "users"):
                opp_val = getattr(value, "users", None)
                setattr(value, "users", self)

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library", None)
        self.__library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    setattr(item, "Book", self)
                    

    @property
    def library2(self):
        return self.__library2

    @library2.setter
    def library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library2", None)
        self.__library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User"):
                    opp_val = getattr(item, "User", None)
                    
                    if opp_val == self:
                        setattr(item, "User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User"):
                    opp_val = getattr(item, "User", None)
                    
                    setattr(item, "User", self)
                    
