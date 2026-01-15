from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class book_Book:

    def __init__(self, name: str, id: int, book_Book2: "book_EObject" = None, book_Book: "book_BookCollection" = None):
        self.name = name
        self.id = id
        self.book_Book2 = book_Book2
        self.book_Book = book_Book
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def book_Book(self):
        return self.__book_Book

    @book_Book.setter
    def book_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__book_Book", None)
        self.__book_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_BookCollection"):
                opp_val = getattr(old_value, "book_BookCollection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_BookCollection"):
                opp_val = getattr(value, "book_BookCollection", None)
                if opp_val is None:
                    setattr(value, "book_BookCollection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def book_Book2(self):
        return self.__book_Book2

    @book_Book2.setter
    def book_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__book_Book2", None)
        self.__book_Book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_EObject"):
                opp_val = getattr(old_value, "book_EObject", None)
                if opp_val == self:
                    setattr(old_value, "book_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_EObject"):
                opp_val = getattr(value, "book_EObject", None)
                setattr(value, "book_EObject", self)

class book_BookCollection:

    pass
class book_EObject:

    pass