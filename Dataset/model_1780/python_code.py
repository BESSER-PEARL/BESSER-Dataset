from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class imports_RootElementType:

    def __init__(self, importURI: str, imports_RootElementType: "imports_DocumentRoot" = None, imports_RootElementType7: "imports_BookType" = None):
        self.importURI = importURI
        self.imports_RootElementType = imports_RootElementType
        self.imports_RootElementType7 = imports_RootElementType7
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def imports_RootElementType7(self):
        return self.__imports_RootElementType7

    @imports_RootElementType7.setter
    def imports_RootElementType7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imports_RootElementType__imports_RootElementType7", None)
        self.__imports_RootElementType7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imports_BookType"):
                opp_val = getattr(old_value, "imports_BookType", None)
                if opp_val == self:
                    setattr(old_value, "imports_BookType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imports_BookType"):
                opp_val = getattr(value, "imports_BookType", None)
                setattr(value, "imports_BookType", self)

    @property
    def imports_RootElementType(self):
        return self.__imports_RootElementType

    @imports_RootElementType.setter
    def imports_RootElementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imports_RootElementType__imports_RootElementType", None)
        self.__imports_RootElementType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imports_DocumentRoot5"):
                opp_val = getattr(old_value, "imports_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imports_DocumentRoot5"):
                opp_val = getattr(value, "imports_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "imports_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class imports_EStringToStringMapEntry:

    pass
class imports_DocumentRoot:

    def __init__(self, mixed: str, imports_DocumentRoot5: set["imports_RootElementType"] = None, imports_DocumentRoot: set["imports_EStringToStringMapEntry"] = None, imports_DocumentRoot2: set["imports_EStringToStringMapEntry"] = None):
        self.mixed = mixed
        self.imports_DocumentRoot5 = imports_DocumentRoot5 if imports_DocumentRoot5 is not None else set()
        self.imports_DocumentRoot = imports_DocumentRoot if imports_DocumentRoot is not None else set()
        self.imports_DocumentRoot2 = imports_DocumentRoot2 if imports_DocumentRoot2 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def imports_DocumentRoot(self):
        return self.__imports_DocumentRoot

    @imports_DocumentRoot.setter
    def imports_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imports_DocumentRoot__imports_DocumentRoot", None)
        self.__imports_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imports_EStringToStringMapEntry"):
                    opp_val = getattr(item, "imports_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "imports_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imports_EStringToStringMapEntry"):
                    opp_val = getattr(item, "imports_EStringToStringMapEntry", None)
                    
                    setattr(item, "imports_EStringToStringMapEntry", self)
                    

    @property
    def imports_DocumentRoot2(self):
        return self.__imports_DocumentRoot2

    @imports_DocumentRoot2.setter
    def imports_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imports_DocumentRoot__imports_DocumentRoot2", None)
        self.__imports_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imports_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "imports_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "imports_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imports_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "imports_EStringToStringMapEntry3", None)
                    
                    setattr(item, "imports_EStringToStringMapEntry3", self)
                    

    @property
    def imports_DocumentRoot5(self):
        return self.__imports_DocumentRoot5

    @imports_DocumentRoot5.setter
    def imports_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imports_DocumentRoot__imports_DocumentRoot5", None)
        self.__imports_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imports_RootElementType"):
                    opp_val = getattr(item, "imports_RootElementType", None)
                    
                    if opp_val == self:
                        setattr(item, "imports_RootElementType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imports_RootElementType"):
                    opp_val = getattr(item, "imports_RootElementType", None)
                    
                    setattr(item, "imports_RootElementType", self)
                    

class imports_BookType:

    def __init__(self, author: str, title: str, isbn: str, imports_BookType: "imports_RootElementType" = None):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.imports_BookType = imports_BookType
        
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
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def imports_BookType(self):
        return self.__imports_BookType

    @imports_BookType.setter
    def imports_BookType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imports_BookType__imports_BookType", None)
        self.__imports_BookType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imports_RootElementType7"):
                opp_val = getattr(old_value, "imports_RootElementType7", None)
                if opp_val == self:
                    setattr(old_value, "imports_RootElementType7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imports_RootElementType7"):
                opp_val = getattr(value, "imports_RootElementType7", None)
                setattr(value, "imports_RootElementType7", self)
