from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class a_Book:

    def __init__(self, title: str, author: str, published: str, a_Book: "a_Model" = None):
        self.title = title
        self.author = author
        self.published = published
        self.a_Book = a_Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def published(self) -> str:
        return self.__published

    @published.setter
    def published(self, published: str):
        self.__published = published

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def a_Book(self):
        return self.__a_Book

    @a_Book.setter
    def a_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_Book__a_Book", None)
        self.__a_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a_Model2"):
                opp_val = getattr(old_value, "a_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a_Model2"):
                opp_val = getattr(value, "a_Model2", None)
                if opp_val is None:
                    setattr(value, "a_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class a_A:

    def __init__(self, name: str, a_A: "a_Model" = None):
        self.name = name
        self.a_A = a_A
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def a_A(self):
        return self.__a_A

    @a_A.setter
    def a_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_A__a_A", None)
        self.__a_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a_Model"):
                opp_val = getattr(old_value, "a_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a_Model"):
                opp_val = getattr(value, "a_Model", None)
                if opp_val is None:
                    setattr(value, "a_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class a_Model:

    pass