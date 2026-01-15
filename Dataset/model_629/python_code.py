from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_Book:

    def __init__(self, title: str, pages: int, test_Book: "test_Library" = None, Book: "test_Writer" = None, books: "test_Writer" = None):
        self.title = title
        self.pages = pages
        self.test_Book = test_Book
        self.Book = Book
        self.books = books
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Book__books", None)
        self.__books = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Writer6"):
                opp_val = getattr(old_value, "Writer6", None)
                if opp_val == self:
                    setattr(old_value, "Writer6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Writer6"):
                opp_val = getattr(value, "Writer6", None)
                setattr(value, "Writer6", self)

    @property
    def test_Book(self):
        return self.__test_Book

    @test_Book.setter
    def test_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Book__test_Book", None)
        self.__test_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Library"):
                opp_val = getattr(old_value, "test_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Library"):
                opp_val = getattr(value, "test_Library", None)
                if opp_val is None:
                    setattr(value, "test_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writers"):
                opp_val = getattr(old_value, "writers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writers"):
                opp_val = getattr(value, "writers", None)
                if opp_val is None:
                    setattr(value, "writers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_Writer:

    def __init__(self, firstName: str, BirthDate: date, Pseudonym: bool, lastName: str, EMail: str, Writer: "test_Library" = None, writers: set["test_Book"] = None, writers4: "test_Library" = None, Writer6: "test_Book" = None):
        self.firstName = firstName
        self.BirthDate = BirthDate
        self.Pseudonym = Pseudonym
        self.lastName = lastName
        self.EMail = EMail
        self.Writer = Writer
        self.writers = writers if writers is not None else set()
        self.writers4 = writers4
        self.Writer6 = Writer6
        
    @property
    def Pseudonym(self) -> bool:
        return self.__Pseudonym

    @Pseudonym.setter
    def Pseudonym(self, Pseudonym: bool):
        self.__Pseudonym = Pseudonym

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def BirthDate(self) -> date:
        return self.__BirthDate

    @BirthDate.setter
    def BirthDate(self, BirthDate: date):
        self.__BirthDate = BirthDate

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def EMail(self) -> str:
        return self.__EMail

    @EMail.setter
    def EMail(self, EMail: str):
        self.__EMail = EMail

    @property
    def writers4(self):
        return self.__writers4

    @writers4.setter
    def writers4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Writer__writers4", None)
        self.__writers4 = value
        
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
    def writers(self):
        return self.__writers

    @writers.setter
    def writers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Writer__writers", None)
        self.__writers = value if value is not None else set()
        
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
    def Writer6(self):
        return self.__Writer6

    @Writer6.setter
    def Writer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Writer__Writer6", None)
        self.__Writer6 = value
        
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
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Writer__Writer", None)
        self.__Writer = value
        
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

    def validate(self, context: str, diagnostic: str) -> bool:
        # TODO: Implement validate method
        pass

class test_Library:

    def __init__(self, name: str, library: set["test_Writer"] = None, test_Library: set["test_Book"] = None, Library: "test_Writer" = None):
        self.name = name
        self.library = library if library is not None else set()
        self.test_Library = test_Library if test_Library is not None else set()
        self.Library = Library
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Library__library", None)
        self.__library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Writer"):
                    opp_val = getattr(item, "Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Writer"):
                    opp_val = getattr(item, "Writer", None)
                    
                    setattr(item, "Writer", self)
                    

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writers4"):
                opp_val = getattr(old_value, "writers4", None)
                if opp_val == self:
                    setattr(old_value, "writers4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writers4"):
                opp_val = getattr(value, "writers4", None)
                setattr(value, "writers4", self)

    @property
    def test_Library(self):
        return self.__test_Library

    @test_Library.setter
    def test_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Library__test_Library", None)
        self.__test_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_Book"):
                    opp_val = getattr(item, "test_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "test_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_Book"):
                    opp_val = getattr(item, "test_Book", None)
                    
                    setattr(item, "test_Book", self)
                    
