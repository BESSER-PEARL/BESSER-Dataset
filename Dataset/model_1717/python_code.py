from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Library3_LibraryType:

    pass
class Library3_EStringToStringMapEntry:

    pass
class Library3_DocumentRoot:

    def __init__(self, mixed: str, Library3_DocumentRoot: set["Library3_EStringToStringMapEntry"] = None, Library3_DocumentRoot3: set["Library3_EStringToStringMapEntry"] = None, Library3_DocumentRoot6: set["Library3_LibraryType"] = None):
        self.mixed = mixed
        self.Library3_DocumentRoot = Library3_DocumentRoot if Library3_DocumentRoot is not None else set()
        self.Library3_DocumentRoot3 = Library3_DocumentRoot3 if Library3_DocumentRoot3 is not None else set()
        self.Library3_DocumentRoot6 = Library3_DocumentRoot6 if Library3_DocumentRoot6 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Library3_DocumentRoot3(self):
        return self.__Library3_DocumentRoot3

    @Library3_DocumentRoot3.setter
    def Library3_DocumentRoot3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library3_DocumentRoot__Library3_DocumentRoot3", None)
        self.__Library3_DocumentRoot3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library3_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "Library3_EStringToStringMapEntry4", None)
                    
                    if opp_val == self:
                        setattr(item, "Library3_EStringToStringMapEntry4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library3_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "Library3_EStringToStringMapEntry4", None)
                    
                    setattr(item, "Library3_EStringToStringMapEntry4", self)
                    

    @property
    def Library3_DocumentRoot(self):
        return self.__Library3_DocumentRoot

    @Library3_DocumentRoot.setter
    def Library3_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library3_DocumentRoot__Library3_DocumentRoot", None)
        self.__Library3_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library3_EStringToStringMapEntry"):
                    opp_val = getattr(item, "Library3_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "Library3_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library3_EStringToStringMapEntry"):
                    opp_val = getattr(item, "Library3_EStringToStringMapEntry", None)
                    
                    setattr(item, "Library3_EStringToStringMapEntry", self)
                    

    @property
    def Library3_DocumentRoot6(self):
        return self.__Library3_DocumentRoot6

    @Library3_DocumentRoot6.setter
    def Library3_DocumentRoot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library3_DocumentRoot__Library3_DocumentRoot6", None)
        self.__Library3_DocumentRoot6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library3_LibraryType"):
                    opp_val = getattr(item, "Library3_LibraryType", None)
                    
                    if opp_val == self:
                        setattr(item, "Library3_LibraryType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library3_LibraryType"):
                    opp_val = getattr(item, "Library3_LibraryType", None)
                    
                    setattr(item, "Library3_LibraryType", self)
                    

class Library3_CustomerType:

    def __init__(self, firstName: str, lastName: str, borrowedBookId: str, Library3_CustomerType: "Library3_LibraryType" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.borrowedBookId = borrowedBookId
        self.Library3_CustomerType = Library3_CustomerType
        
    @property
    def borrowedBookId(self) -> str:
        return self.__borrowedBookId

    @borrowedBookId.setter
    def borrowedBookId(self, borrowedBookId: str):
        self.__borrowedBookId = borrowedBookId

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def Library3_CustomerType(self):
        return self.__Library3_CustomerType

    @Library3_CustomerType.setter
    def Library3_CustomerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library3_CustomerType__Library3_CustomerType", None)
        self.__Library3_CustomerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library3_LibraryType11"):
                opp_val = getattr(old_value, "Library3_LibraryType11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library3_LibraryType11"):
                opp_val = getattr(value, "Library3_LibraryType11", None)
                if opp_val is None:
                    setattr(value, "Library3_LibraryType11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Library3_BookType:

    def __init__(self, name: str, title: str, author: str, pages: str, isbn: str, Library3_BookType: "Library3_BookInfoType" = None, Library3_BookType9: "Library3_LibraryType" = None):
        self.name = name
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.Library3_BookType = Library3_BookType
        self.Library3_BookType9 = Library3_BookType9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

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
    def Library3_BookType9(self):
        return self.__Library3_BookType9

    @Library3_BookType9.setter
    def Library3_BookType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library3_BookType__Library3_BookType9", None)
        self.__Library3_BookType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library3_LibraryType8"):
                opp_val = getattr(old_value, "Library3_LibraryType8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library3_LibraryType8"):
                opp_val = getattr(value, "Library3_LibraryType8", None)
                if opp_val is None:
                    setattr(value, "Library3_LibraryType8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Library3_BookType(self):
        return self.__Library3_BookType

    @Library3_BookType.setter
    def Library3_BookType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library3_BookType__Library3_BookType", None)
        self.__Library3_BookType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library3_BookInfoType"):
                opp_val = getattr(old_value, "Library3_BookInfoType", None)
                if opp_val == self:
                    setattr(old_value, "Library3_BookInfoType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library3_BookInfoType"):
                opp_val = getattr(value, "Library3_BookInfoType", None)
                setattr(value, "Library3_BookInfoType", self)

class Library3_BookInfoType:

    def __init__(self, any: str, Library3_BookInfoType: "Library3_BookType" = None):
        self.any = any
        self.Library3_BookInfoType = Library3_BookInfoType
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def Library3_BookInfoType(self):
        return self.__Library3_BookInfoType

    @Library3_BookInfoType.setter
    def Library3_BookInfoType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library3_BookInfoType__Library3_BookInfoType", None)
        self.__Library3_BookInfoType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library3_BookType"):
                opp_val = getattr(old_value, "Library3_BookType", None)
                if opp_val == self:
                    setattr(old_value, "Library3_BookType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library3_BookType"):
                opp_val = getattr(value, "Library3_BookType", None)
                setattr(value, "Library3_BookType", self)
