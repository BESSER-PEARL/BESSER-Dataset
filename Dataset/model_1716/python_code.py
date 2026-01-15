from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library3_LibraryType:

    pass
class library3_DocumentRoot:

    def __init__(self, mixed: str, library3_DocumentRoot: set["library3_EStringToStringMapEntry"] = None, library3_DocumentRoot3: set["library3_EStringToStringMapEntry"] = None, library3_DocumentRoot6: set["library3_LibraryType"] = None):
        self.mixed = mixed
        self.library3_DocumentRoot = library3_DocumentRoot if library3_DocumentRoot is not None else set()
        self.library3_DocumentRoot3 = library3_DocumentRoot3 if library3_DocumentRoot3 is not None else set()
        self.library3_DocumentRoot6 = library3_DocumentRoot6 if library3_DocumentRoot6 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def library3_DocumentRoot(self):
        return self.__library3_DocumentRoot

    @library3_DocumentRoot.setter
    def library3_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3_DocumentRoot__library3_DocumentRoot", None)
        self.__library3_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library3_EStringToStringMapEntry"):
                    opp_val = getattr(item, "library3_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "library3_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library3_EStringToStringMapEntry"):
                    opp_val = getattr(item, "library3_EStringToStringMapEntry", None)
                    
                    setattr(item, "library3_EStringToStringMapEntry", self)
                    

    @property
    def library3_DocumentRoot6(self):
        return self.__library3_DocumentRoot6

    @library3_DocumentRoot6.setter
    def library3_DocumentRoot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3_DocumentRoot__library3_DocumentRoot6", None)
        self.__library3_DocumentRoot6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library3_LibraryType"):
                    opp_val = getattr(item, "library3_LibraryType", None)
                    
                    if opp_val == self:
                        setattr(item, "library3_LibraryType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library3_LibraryType"):
                    opp_val = getattr(item, "library3_LibraryType", None)
                    
                    setattr(item, "library3_LibraryType", self)
                    

    @property
    def library3_DocumentRoot3(self):
        return self.__library3_DocumentRoot3

    @library3_DocumentRoot3.setter
    def library3_DocumentRoot3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3_DocumentRoot__library3_DocumentRoot3", None)
        self.__library3_DocumentRoot3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library3_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "library3_EStringToStringMapEntry4", None)
                    
                    if opp_val == self:
                        setattr(item, "library3_EStringToStringMapEntry4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library3_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "library3_EStringToStringMapEntry4", None)
                    
                    setattr(item, "library3_EStringToStringMapEntry4", self)
                    

class library3_EStringToStringMapEntry:

    pass
class library3_CustomerType:

    def __init__(self, firstName: str, lastName: str, borrowedBookId: str, library3_CustomerType: "library3_LibraryType" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.borrowedBookId = borrowedBookId
        self.library3_CustomerType = library3_CustomerType
        
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
    def borrowedBookId(self) -> str:
        return self.__borrowedBookId

    @borrowedBookId.setter
    def borrowedBookId(self, borrowedBookId: str):
        self.__borrowedBookId = borrowedBookId

    @property
    def library3_CustomerType(self):
        return self.__library3_CustomerType

    @library3_CustomerType.setter
    def library3_CustomerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3_CustomerType__library3_CustomerType", None)
        self.__library3_CustomerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3_LibraryType11"):
                opp_val = getattr(old_value, "library3_LibraryType11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3_LibraryType11"):
                opp_val = getattr(value, "library3_LibraryType11", None)
                if opp_val is None:
                    setattr(value, "library3_LibraryType11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library3_BookInfoType:

    def __init__(self, any: str, library3_BookInfoType: "library3_BookType" = None):
        self.any = any
        self.library3_BookInfoType = library3_BookInfoType
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def library3_BookInfoType(self):
        return self.__library3_BookInfoType

    @library3_BookInfoType.setter
    def library3_BookInfoType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3_BookInfoType__library3_BookInfoType", None)
        self.__library3_BookInfoType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3_BookType"):
                opp_val = getattr(old_value, "library3_BookType", None)
                if opp_val == self:
                    setattr(old_value, "library3_BookType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3_BookType"):
                opp_val = getattr(value, "library3_BookType", None)
                setattr(value, "library3_BookType", self)

class library3_BookType:

    def __init__(self, name: str, isbn: str, title: str, author: str, pages: str, library3_BookType: "library3_BookInfoType" = None, library3_BookType9: "library3_LibraryType" = None):
        self.name = name
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages
        self.library3_BookType = library3_BookType
        self.library3_BookType9 = library3_BookType9
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def library3_BookType9(self):
        return self.__library3_BookType9

    @library3_BookType9.setter
    def library3_BookType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3_BookType__library3_BookType9", None)
        self.__library3_BookType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3_LibraryType8"):
                opp_val = getattr(old_value, "library3_LibraryType8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3_LibraryType8"):
                opp_val = getattr(value, "library3_LibraryType8", None)
                if opp_val is None:
                    setattr(value, "library3_LibraryType8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library3_BookType(self):
        return self.__library3_BookType

    @library3_BookType.setter
    def library3_BookType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library3_BookType__library3_BookType", None)
        self.__library3_BookType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3_BookInfoType"):
                opp_val = getattr(old_value, "library3_BookInfoType", None)
                if opp_val == self:
                    setattr(old_value, "library3_BookInfoType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3_BookInfoType"):
                opp_val = getattr(value, "library3_BookInfoType", None)
                setattr(value, "library3_BookInfoType", self)
