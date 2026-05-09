from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class books_Title:

    def __init__(self, lan: str, text: str, books_Title: "books_Book" = None):
        self.lan = lan
        self.text = text
        self.books_Title = books_Title
        
        pass
    @property
    def lan(self):
        return self.__lan

    @lan.setter
    def lan(self, lan: str):
        self.__lan = lan


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def books_Title(self):
        return self.__books_Title

    @books_Title.setter
    def books_Title(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_books_Title__books_Title", None)
        self.__books_Title = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books_Book2"):
                opp_val = getattr(old_value, "books_Book2", None)
                if opp_val == self:
                    setattr(old_value, "books_Book2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books_Book2"):
                opp_val = getattr(value, "books_Book2", None)
                setattr(value, "books_Book2", self)

class books_Book:

    def __init__(self, author: str, price: float, year: str, books_Book: "books_Bookstore" = None, books_Book2: "books_Title" = None):
        self.author = author
        self.price = price
        self.year = year
        self.books_Book = books_Book
        self.books_Book2 = books_Book2
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def books_Book2(self):
        return self.__books_Book2

    @books_Book2.setter
    def books_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_books_Book__books_Book2", None)
        self.__books_Book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books_Title"):
                opp_val = getattr(old_value, "books_Title", None)
                if opp_val == self:
                    setattr(old_value, "books_Title", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books_Title"):
                opp_val = getattr(value, "books_Title", None)
                setattr(value, "books_Title", self)

    @property
    def books_Book(self):
        return self.__books_Book

    @books_Book.setter
    def books_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_books_Book__books_Book", None)
        self.__books_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books_Bookstore"):
                opp_val = getattr(old_value, "books_Bookstore", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books_Bookstore"):
                opp_val = getattr(value, "books_Bookstore", None)
                if opp_val is None:
                    setattr(value, "books_Bookstore", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class books_Bookstore:

    pass