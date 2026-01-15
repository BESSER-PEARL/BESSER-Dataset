from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Books_Author:

    def __init__(self, name: str, Author: "Books_Book" = None, Books_Author: "Books_System" = None, auths: set["Books_Book"] = None):
        self.name = name
        self.Author = Author
        self.Books_Author = Books_Author
        self.auths = auths if auths is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_Author__Author", None)
        self.__Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mybs"):
                opp_val = getattr(old_value, "mybs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mybs"):
                opp_val = getattr(value, "mybs", None)
                if opp_val is None:
                    setattr(value, "mybs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Books_Author(self):
        return self.__Books_Author

    @Books_Author.setter
    def Books_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_Author__Books_Author", None)
        self.__Books_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Books_System2"):
                opp_val = getattr(old_value, "Books_System2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Books_System2"):
                opp_val = getattr(value, "Books_System2", None)
                if opp_val is None:
                    setattr(value, "Books_System2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def auths(self):
        return self.__auths

    @auths.setter
    def auths(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_Author__auths", None)
        self.__auths = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book7"):
                    opp_val = getattr(item, "Book7", None)
                    
                    if opp_val == self:
                        setattr(item, "Book7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book7"):
                    opp_val = getattr(item, "Book7", None)
                    
                    setattr(item, "Book7", self)
                    

class Books_Book:

    def __init__(self, collecName: str, title: str, itsbook: set["Books_Chapter"] = None, mybs: set["Books_Author"] = None, Book: "Books_Chapter" = None, Books_Book: "Books_System" = None, Book7: "Books_Author" = None):
        self.collecName = collecName
        self.title = title
        self.itsbook = itsbook if itsbook is not None else set()
        self.mybs = mybs if mybs is not None else set()
        self.Book = Book
        self.Books_Book = Books_Book
        self.Book7 = Book7
        
    @property
    def collecName(self) -> str:
        return self.__collecName

    @collecName.setter
    def collecName(self, collecName: str):
        self.__collecName = collecName

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Book7(self):
        return self.__Book7

    @Book7.setter
    def Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_Book__Book7", None)
        self.__Book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auths"):
                opp_val = getattr(old_value, "auths", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auths"):
                opp_val = getattr(value, "auths", None)
                if opp_val is None:
                    setattr(value, "auths", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mybs(self):
        return self.__mybs

    @mybs.setter
    def mybs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_Book__mybs", None)
        self.__mybs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    if opp_val == self:
                        setattr(item, "Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    setattr(item, "Author", self)
                    

    @property
    def Books_Book(self):
        return self.__Books_Book

    @Books_Book.setter
    def Books_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_Book__Books_Book", None)
        self.__Books_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Books_System"):
                opp_val = getattr(old_value, "Books_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Books_System"):
                opp_val = getattr(value, "Books_System", None)
                if opp_val is None:
                    setattr(value, "Books_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chaps"):
                opp_val = getattr(old_value, "chaps", None)
                if opp_val == self:
                    setattr(old_value, "chaps", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chaps"):
                opp_val = getattr(value, "chaps", None)
                setattr(value, "chaps", self)

    @property
    def itsbook(self):
        return self.__itsbook

    @itsbook.setter
    def itsbook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_Book__itsbook", None)
        self.__itsbook = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Chapter"):
                    opp_val = getattr(item, "Chapter", None)
                    
                    if opp_val == self:
                        setattr(item, "Chapter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Chapter"):
                    opp_val = getattr(item, "Chapter", None)
                    
                    setattr(item, "Chapter", self)
                    

class Books_System:

    def __init__(self, name: str, Books_System: set["Books_Book"] = None, Books_System2: set["Books_Author"] = None):
        self.name = name
        self.Books_System = Books_System if Books_System is not None else set()
        self.Books_System2 = Books_System2 if Books_System2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Books_System2(self):
        return self.__Books_System2

    @Books_System2.setter
    def Books_System2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_System__Books_System2", None)
        self.__Books_System2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Books_Author"):
                    opp_val = getattr(item, "Books_Author", None)
                    
                    if opp_val == self:
                        setattr(item, "Books_Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Books_Author"):
                    opp_val = getattr(item, "Books_Author", None)
                    
                    setattr(item, "Books_Author", self)
                    

    @property
    def Books_System(self):
        return self.__Books_System

    @Books_System.setter
    def Books_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_System__Books_System", None)
        self.__Books_System = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Books_Book"):
                    opp_val = getattr(item, "Books_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Books_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Books_Book"):
                    opp_val = getattr(item, "Books_Book", None)
                    
                    setattr(item, "Books_Book", self)
                    

class Books_Chapter:

    def __init__(self, title: str, Chapter: "Books_Book" = None, chaps: "Books_Book" = None):
        self.title = title
        self.Chapter = Chapter
        self.chaps = chaps
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def chaps(self):
        return self.__chaps

    @chaps.setter
    def chaps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_Chapter__chaps", None)
        self.__chaps = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book"):
                opp_val = getattr(old_value, "Book", None)
                if opp_val == self:
                    setattr(old_value, "Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book"):
                opp_val = getattr(value, "Book", None)
                setattr(value, "Book", self)

    @property
    def Chapter(self):
        return self.__Chapter

    @Chapter.setter
    def Chapter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Books_Chapter__Chapter", None)
        self.__Chapter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itsbook"):
                opp_val = getattr(old_value, "itsbook", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itsbook"):
                opp_val = getattr(value, "itsbook", None)
                if opp_val is None:
                    setattr(value, "itsbook", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
