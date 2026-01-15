from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class BookStorePackage_Book:

    def __init__(self, name: str, isbn: int, BookStorePackage_Book: "BookStorePackage_BookStore" = None):
        self.name = name
        self.isbn = isbn
        self.BookStorePackage_Book = BookStorePackage_Book
        
    @property
    def isbn(self) -> int:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: int):
        self.__isbn = isbn

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BookStorePackage_Book(self):
        return self.__BookStorePackage_Book

    @BookStorePackage_Book.setter
    def BookStorePackage_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookStorePackage_Book__BookStorePackage_Book", None)
        self.__BookStorePackage_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BookStorePackage_BookStore"):
                opp_val = getattr(old_value, "BookStorePackage_BookStore", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BookStorePackage_BookStore"):
                opp_val = getattr(value, "BookStorePackage_BookStore", None)
                if opp_val is None:
                    setattr(value, "BookStorePackage_BookStore", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BookStorePackage_BookStore:

    def __init__(self, owner: str, location: str, BookStorePackage_BookStore: set["BookStorePackage_Book"] = None):
        self.owner = owner
        self.location = location
        self.BookStorePackage_BookStore = BookStorePackage_BookStore if BookStorePackage_BookStore is not None else set()
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def BookStorePackage_BookStore(self):
        return self.__BookStorePackage_BookStore

    @BookStorePackage_BookStore.setter
    def BookStorePackage_BookStore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookStorePackage_BookStore__BookStorePackage_BookStore", None)
        self.__BookStorePackage_BookStore = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BookStorePackage_Book"):
                    opp_val = getattr(item, "BookStorePackage_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "BookStorePackage_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BookStorePackage_Book"):
                    opp_val = getattr(item, "BookStorePackage_Book", None)
                    
                    setattr(item, "BookStorePackage_Book", self)
                    
