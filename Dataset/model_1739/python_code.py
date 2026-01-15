from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_MappedLibrary:

    def __init__(self, books: str, model_MappedLibrary17: set["model_Book"] = None, model_MappedLibrary: "model_Location" = None, model_MappedLibrary14: set["model_Book"] = None):
        self.books = books
        self.model_MappedLibrary17 = model_MappedLibrary17 if model_MappedLibrary17 is not None else set()
        self.model_MappedLibrary = model_MappedLibrary
        self.model_MappedLibrary14 = model_MappedLibrary14 if model_MappedLibrary14 is not None else set()
        
    @property
    def books(self) -> str:
        return self.__books

    @books.setter
    def books(self, books: str):
        self.__books = books

    @property
    def model_MappedLibrary(self):
        return self.__model_MappedLibrary

    @model_MappedLibrary.setter
    def model_MappedLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MappedLibrary__model_MappedLibrary", None)
        self.__model_MappedLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Location12"):
                opp_val = getattr(old_value, "model_Location12", None)
                if opp_val == self:
                    setattr(old_value, "model_Location12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Location12"):
                opp_val = getattr(value, "model_Location12", None)
                setattr(value, "model_Location12", self)

    @property
    def model_MappedLibrary17(self):
        return self.__model_MappedLibrary17

    @model_MappedLibrary17.setter
    def model_MappedLibrary17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MappedLibrary__model_MappedLibrary17", None)
        self.__model_MappedLibrary17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Book18"):
                    opp_val = getattr(item, "model_Book18", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Book18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Book18"):
                    opp_val = getattr(item, "model_Book18", None)
                    
                    setattr(item, "model_Book18", self)
                    

    @property
    def model_MappedLibrary14(self):
        return self.__model_MappedLibrary14

    @model_MappedLibrary14.setter
    def model_MappedLibrary14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MappedLibrary__model_MappedLibrary14", None)
        self.__model_MappedLibrary14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Book15"):
                    opp_val = getattr(item, "model_Book15", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Book15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Book15"):
                    opp_val = getattr(item, "model_Book15", None)
                    
                    setattr(item, "model_Book15", self)
                    

class model_Location:

    def __init__(self, address: str, id: str, model_Location: "model_Library" = None, model_Location9: "model_Book" = None, model_Location12: "model_MappedLibrary" = None):
        self.address = address
        self.id = id
        self.model_Location = model_Location
        self.model_Location9 = model_Location9
        self.model_Location12 = model_Location12
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def model_Location(self):
        return self.__model_Location

    @model_Location.setter
    def model_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Location__model_Location", None)
        self.__model_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Library4"):
                opp_val = getattr(old_value, "model_Library4", None)
                if opp_val == self:
                    setattr(old_value, "model_Library4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library4"):
                opp_val = getattr(value, "model_Library4", None)
                setattr(value, "model_Library4", self)

    @property
    def model_Location12(self):
        return self.__model_Location12

    @model_Location12.setter
    def model_Location12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Location__model_Location12", None)
        self.__model_Location12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MappedLibrary"):
                opp_val = getattr(old_value, "model_MappedLibrary", None)
                if opp_val == self:
                    setattr(old_value, "model_MappedLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MappedLibrary"):
                opp_val = getattr(value, "model_MappedLibrary", None)
                setattr(value, "model_MappedLibrary", self)

    @property
    def model_Location9(self):
        return self.__model_Location9

    @model_Location9.setter
    def model_Location9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Location__model_Location9", None)
        self.__model_Location9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Book10"):
                opp_val = getattr(old_value, "model_Book10", None)
                if opp_val == self:
                    setattr(old_value, "model_Book10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Book10"):
                opp_val = getattr(value, "model_Book10", None)
                setattr(value, "model_Book10", self)

class model_Library:

    pass
class model_Book:

    def __init__(self, tags: str, data: str, title: str, Book: "model_Person" = None, model_Book: "model_Library" = None, books: set["model_Person"] = None, model_Book18: "model_MappedLibrary" = None, model_Book7: "model_Library" = None, model_Book10: "model_Location" = None, model_Book15: "model_MappedLibrary" = None):
        self.tags = tags
        self.data = data
        self.title = title
        self.Book = Book
        self.model_Book = model_Book
        self.books = books if books is not None else set()
        self.model_Book18 = model_Book18
        self.model_Book7 = model_Book7
        self.model_Book10 = model_Book10
        self.model_Book15 = model_Book15
        
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def tags(self) -> str:
        return self.__tags

    @tags.setter
    def tags(self, tags: str):
        self.__tags = tags

    @property
    def model_Book7(self):
        return self.__model_Book7

    @model_Book7.setter
    def model_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book7", None)
        self.__model_Book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Library6"):
                opp_val = getattr(old_value, "model_Library6", None)
                if opp_val == self:
                    setattr(old_value, "model_Library6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library6"):
                opp_val = getattr(value, "model_Library6", None)
                setattr(value, "model_Library6", self)

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
            if hasattr(old_value, "model_Library"):
                opp_val = getattr(old_value, "model_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library"):
                opp_val = getattr(value, "model_Library", None)
                if opp_val is None:
                    setattr(value, "model_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Book18(self):
        return self.__model_Book18

    @model_Book18.setter
    def model_Book18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book18", None)
        self.__model_Book18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MappedLibrary17"):
                opp_val = getattr(old_value, "model_MappedLibrary17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MappedLibrary17"):
                opp_val = getattr(value, "model_MappedLibrary17", None)
                if opp_val is None:
                    setattr(value, "model_MappedLibrary17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Book10(self):
        return self.__model_Book10

    @model_Book10.setter
    def model_Book10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book10", None)
        self.__model_Book10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Location9"):
                opp_val = getattr(old_value, "model_Location9", None)
                if opp_val == self:
                    setattr(old_value, "model_Location9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Location9"):
                opp_val = getattr(value, "model_Location9", None)
                setattr(value, "model_Location9", self)

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
            if hasattr(old_value, "authors"):
                opp_val = getattr(old_value, "authors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authors"):
                opp_val = getattr(value, "authors", None)
                if opp_val is None:
                    setattr(value, "authors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def model_Book15(self):
        return self.__model_Book15

    @model_Book15.setter
    def model_Book15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book15", None)
        self.__model_Book15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MappedLibrary14"):
                opp_val = getattr(old_value, "model_MappedLibrary14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MappedLibrary14"):
                opp_val = getattr(value, "model_MappedLibrary14", None)
                if opp_val is None:
                    setattr(value, "model_MappedLibrary14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Person:

    def __init__(self, name: str, authors: set["model_Book"] = None, Person: "model_Book" = None):
        self.name = name
        self.authors = authors if authors is not None else set()
        self.Person = Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__authors", None)
        self.__authors = value if value is not None else set()
        
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
                    
