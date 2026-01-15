from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_DataBase:

    pass
class model_Person:

    def __init__(self, name: str, ownedBy: set["model_BookShelf"] = None, model_Person: "model_Person" = None, model_Person3: set["model_Person"] = None, Person: "model_BookShelf" = None, model_Person8: "model_DataBase" = None):
        self.name = name
        self.ownedBy = ownedBy if ownedBy is not None else set()
        self.model_Person = model_Person
        self.model_Person3 = model_Person3 if model_Person3 is not None else set()
        self.Person = Person
        self.model_Person8 = model_Person8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ownedBy(self):
        return self.__ownedBy

    @ownedBy.setter
    def ownedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__ownedBy", None)
        self.__ownedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BookShelf2"):
                    opp_val = getattr(item, "BookShelf2", None)
                    
                    if opp_val == self:
                        setattr(item, "BookShelf2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BookShelf2"):
                    opp_val = getattr(item, "BookShelf2", None)
                    
                    setattr(item, "BookShelf2", self)
                    

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shelves"):
                opp_val = getattr(old_value, "shelves", None)
                if opp_val == self:
                    setattr(old_value, "shelves", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shelves"):
                opp_val = getattr(value, "shelves", None)
                setattr(value, "shelves", self)

    @property
    def model_Person3(self):
        return self.__model_Person3

    @model_Person3.setter
    def model_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__model_Person3", None)
        self.__model_Person3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Person"):
                    opp_val = getattr(item, "model_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Person"):
                    opp_val = getattr(item, "model_Person", None)
                    
                    setattr(item, "model_Person", self)
                    

    @property
    def model_Person(self):
        return self.__model_Person

    @model_Person.setter
    def model_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__model_Person", None)
        self.__model_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Person3"):
                opp_val = getattr(old_value, "model_Person3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Person3"):
                opp_val = getattr(value, "model_Person3", None)
                if opp_val is None:
                    setattr(value, "model_Person3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Person8(self):
        return self.__model_Person8

    @model_Person8.setter
    def model_Person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__model_Person8", None)
        self.__model_Person8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DataBase"):
                opp_val = getattr(old_value, "model_DataBase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DataBase"):
                opp_val = getattr(value, "model_DataBase", None)
                if opp_val is None:
                    setattr(value, "model_DataBase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_BookShelf:

    def __init__(self, name: str, BookShelf: "model_Book" = None, BookShelf2: "model_Person" = None, presentIn: set["model_Book"] = None, shelves: "model_Person" = None):
        self.name = name
        self.BookShelf = BookShelf
        self.BookShelf2 = BookShelf2
        self.presentIn = presentIn if presentIn is not None else set()
        self.shelves = shelves
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BookShelf(self):
        return self.__BookShelf

    @BookShelf.setter
    def BookShelf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookShelf__BookShelf", None)
        self.__BookShelf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books"):
                opp_val = getattr(old_value, "books", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books"):
                opp_val = getattr(value, "books", None)
                if opp_val is None:
                    setattr(value, "books", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BookShelf2(self):
        return self.__BookShelf2

    @BookShelf2.setter
    def BookShelf2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookShelf__BookShelf2", None)
        self.__BookShelf2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedBy"):
                opp_val = getattr(old_value, "ownedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedBy"):
                opp_val = getattr(value, "ownedBy", None)
                if opp_val is None:
                    setattr(value, "ownedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shelves(self):
        return self.__shelves

    @shelves.setter
    def shelves(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookShelf__shelves", None)
        self.__shelves = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person"):
                opp_val = getattr(old_value, "Person", None)
                if opp_val == self:
                    setattr(old_value, "Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person"):
                opp_val = getattr(value, "Person", None)
                setattr(value, "Person", self)

    @property
    def presentIn(self):
        return self.__presentIn

    @presentIn.setter
    def presentIn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookShelf__presentIn", None)
        self.__presentIn = value if value is not None else set()
        
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
                    

class model_Book:

    def __init__(self, name: str, author: str, avgRating: int, books: set["model_BookShelf"] = None, Book: "model_BookShelf" = None, model_Book: "model_DataBase" = None):
        self.name = name
        self.author = author
        self.avgRating = avgRating
        self.books = books if books is not None else set()
        self.Book = Book
        self.model_Book = model_Book
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def avgRating(self) -> int:
        return self.__avgRating

    @avgRating.setter
    def avgRating(self, avgRating: int):
        self.__avgRating = avgRating

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
        old_value = getattr(self, f"_model_Book__books", None)
        self.__books = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BookShelf"):
                    opp_val = getattr(item, "BookShelf", None)
                    
                    if opp_val == self:
                        setattr(item, "BookShelf", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BookShelf"):
                    opp_val = getattr(item, "BookShelf", None)
                    
                    setattr(item, "BookShelf", self)
                    

    @property
    def model_Book(self):
        return self.__model_Book

    @model_Book.setter
    def model_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book", None)
        self.__model_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DataBase10"):
                opp_val = getattr(old_value, "model_DataBase10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DataBase10"):
                opp_val = getattr(value, "model_DataBase10", None)
                if opp_val is None:
                    setattr(value, "model_DataBase10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentIn"):
                opp_val = getattr(old_value, "presentIn", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentIn"):
                opp_val = getattr(value, "presentIn", None)
                if opp_val is None:
                    setattr(value, "presentIn", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
