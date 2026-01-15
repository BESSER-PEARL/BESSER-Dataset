from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library3Simplified_Library:

    pass
class library3Simplified_Customer:

    def __init__(self, firstName: str, lastName: str, borrowedBookSince: str, library3Simplified_Customer: "library3Simplified_Book" = None, library3Simplified_Customer7: "library3Simplified_Library" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.borrowedBookSince = borrowedBookSince
        self.library3Simplified_Customer = library3Simplified_Customer
        self.library3Simplified_Customer7 = library3Simplified_Customer7
        
    @property
    def borrowedBookSince(self) -> str:
        return self.__borrowedBookSince

    @borrowedBookSince.setter
    def borrowedBookSince(self, borrowedBookSince: str):
        self.__borrowedBookSince = borrowedBookSince

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def library3Simplified_Customer(self):
        return self.__library3Simplified_Customer

    @library3Simplified_Customer.setter
    def library3Simplified_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3Simplified_Customer__library3Simplified_Customer", None)
        self.__library3Simplified_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3Simplified_Book2"):
                opp_val = getattr(old_value, "library3Simplified_Book2", None)
                if opp_val == self:
                    setattr(old_value, "library3Simplified_Book2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3Simplified_Book2"):
                opp_val = getattr(value, "library3Simplified_Book2", None)
                setattr(value, "library3Simplified_Book2", self)

    @property
    def library3Simplified_Customer7(self):
        return self.__library3Simplified_Customer7

    @library3Simplified_Customer7.setter
    def library3Simplified_Customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3Simplified_Customer__library3Simplified_Customer7", None)
        self.__library3Simplified_Customer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3Simplified_Library6"):
                opp_val = getattr(old_value, "library3Simplified_Library6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3Simplified_Library6"):
                opp_val = getattr(value, "library3Simplified_Library6", None)
                if opp_val is None:
                    setattr(value, "library3Simplified_Library6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library3Simplified_Book:

    def __init__(self, pages: int, dimension: str, download: str, isbn: str, name: str, title: str, author: str, library3Simplified_Book: "library3Simplified_BookInfo" = None, library3Simplified_Book2: "library3Simplified_Customer" = None, library3Simplified_Book4: "library3Simplified_Library" = None):
        self.pages = pages
        self.dimension = dimension
        self.download = download
        self.isbn = isbn
        self.name = name
        self.title = title
        self.author = author
        self.library3Simplified_Book = library3Simplified_Book
        self.library3Simplified_Book2 = library3Simplified_Book2
        self.library3Simplified_Book4 = library3Simplified_Book4
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def download(self) -> str:
        return self.__download

    @download.setter
    def download(self, download: str):
        self.__download = download

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dimension(self) -> str:
        return self.__dimension

    @dimension.setter
    def dimension(self, dimension: str):
        self.__dimension = dimension

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def library3Simplified_Book(self):
        return self.__library3Simplified_Book

    @library3Simplified_Book.setter
    def library3Simplified_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3Simplified_Book__library3Simplified_Book", None)
        self.__library3Simplified_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3Simplified_BookInfo"):
                opp_val = getattr(old_value, "library3Simplified_BookInfo", None)
                if opp_val == self:
                    setattr(old_value, "library3Simplified_BookInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3Simplified_BookInfo"):
                opp_val = getattr(value, "library3Simplified_BookInfo", None)
                setattr(value, "library3Simplified_BookInfo", self)

    @property
    def library3Simplified_Book2(self):
        return self.__library3Simplified_Book2

    @library3Simplified_Book2.setter
    def library3Simplified_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3Simplified_Book__library3Simplified_Book2", None)
        self.__library3Simplified_Book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3Simplified_Customer"):
                opp_val = getattr(old_value, "library3Simplified_Customer", None)
                if opp_val == self:
                    setattr(old_value, "library3Simplified_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3Simplified_Customer"):
                opp_val = getattr(value, "library3Simplified_Customer", None)
                setattr(value, "library3Simplified_Customer", self)

    @property
    def library3Simplified_Book4(self):
        return self.__library3Simplified_Book4

    @library3Simplified_Book4.setter
    def library3Simplified_Book4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3Simplified_Book__library3Simplified_Book4", None)
        self.__library3Simplified_Book4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3Simplified_Library"):
                opp_val = getattr(old_value, "library3Simplified_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3Simplified_Library"):
                opp_val = getattr(value, "library3Simplified_Library", None)
                if opp_val is None:
                    setattr(value, "library3Simplified_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library3Simplified_BookInfo:

    pass