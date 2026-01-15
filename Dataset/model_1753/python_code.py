from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simpleany_LibraryType:

    pass
class simpleany_EStringToStringMapEntry:

    pass
class simpleany_BookType:

    def __init__(self, name: str, title: str, author: str, simpleany_BookType: "simpleany_Description" = None, simpleany_BookType12: "simpleany_LibraryType" = None):
        self.name = name
        self.title = title
        self.author = author
        self.simpleany_BookType = simpleany_BookType
        self.simpleany_BookType12 = simpleany_BookType12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def simpleany_BookType12(self):
        return self.__simpleany_BookType12

    @simpleany_BookType12.setter
    def simpleany_BookType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleany_BookType__simpleany_BookType12", None)
        self.__simpleany_BookType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleany_LibraryType11"):
                opp_val = getattr(old_value, "simpleany_LibraryType11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleany_LibraryType11"):
                opp_val = getattr(value, "simpleany_LibraryType11", None)
                if opp_val is None:
                    setattr(value, "simpleany_LibraryType11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleany_BookType(self):
        return self.__simpleany_BookType

    @simpleany_BookType.setter
    def simpleany_BookType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleany_BookType__simpleany_BookType", None)
        self.__simpleany_BookType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleany_Description"):
                opp_val = getattr(old_value, "simpleany_Description", None)
                if opp_val == self:
                    setattr(old_value, "simpleany_Description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleany_Description"):
                opp_val = getattr(value, "simpleany_Description", None)
                setattr(value, "simpleany_Description", self)

class simpleany_DocumentRoot:

    def __init__(self, mixed: str, simpleany_DocumentRoot: set["simpleany_EStringToStringMapEntry"] = None, simpleany_DocumentRoot6: set["simpleany_EStringToStringMapEntry"] = None, simpleany_DocumentRoot9: set["simpleany_LibraryType"] = None):
        self.mixed = mixed
        self.simpleany_DocumentRoot = simpleany_DocumentRoot if simpleany_DocumentRoot is not None else set()
        self.simpleany_DocumentRoot6 = simpleany_DocumentRoot6 if simpleany_DocumentRoot6 is not None else set()
        self.simpleany_DocumentRoot9 = simpleany_DocumentRoot9 if simpleany_DocumentRoot9 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def simpleany_DocumentRoot6(self):
        return self.__simpleany_DocumentRoot6

    @simpleany_DocumentRoot6.setter
    def simpleany_DocumentRoot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleany_DocumentRoot__simpleany_DocumentRoot6", None)
        self.__simpleany_DocumentRoot6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleany_EStringToStringMapEntry7"):
                    opp_val = getattr(item, "simpleany_EStringToStringMapEntry7", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleany_EStringToStringMapEntry7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleany_EStringToStringMapEntry7"):
                    opp_val = getattr(item, "simpleany_EStringToStringMapEntry7", None)
                    
                    setattr(item, "simpleany_EStringToStringMapEntry7", self)
                    

    @property
    def simpleany_DocumentRoot9(self):
        return self.__simpleany_DocumentRoot9

    @simpleany_DocumentRoot9.setter
    def simpleany_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleany_DocumentRoot__simpleany_DocumentRoot9", None)
        self.__simpleany_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleany_LibraryType"):
                    opp_val = getattr(item, "simpleany_LibraryType", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleany_LibraryType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleany_LibraryType"):
                    opp_val = getattr(item, "simpleany_LibraryType", None)
                    
                    setattr(item, "simpleany_LibraryType", self)
                    

    @property
    def simpleany_DocumentRoot(self):
        return self.__simpleany_DocumentRoot

    @simpleany_DocumentRoot.setter
    def simpleany_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleany_DocumentRoot__simpleany_DocumentRoot", None)
        self.__simpleany_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleany_EStringToStringMapEntry"):
                    opp_val = getattr(item, "simpleany_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleany_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleany_EStringToStringMapEntry"):
                    opp_val = getattr(item, "simpleany_EStringToStringMapEntry", None)
                    
                    setattr(item, "simpleany_EStringToStringMapEntry", self)
                    

class simpleany_Description:

    def __init__(self, mixed: str, keyword: str, simpleany_Description: "simpleany_BookType" = None, simpleany_Description3: "simpleany_Description" = None, simpleany_Description1: set["simpleany_Description"] = None):
        self.mixed = mixed
        self.keyword = keyword
        self.simpleany_Description = simpleany_Description
        self.simpleany_Description3 = simpleany_Description3
        self.simpleany_Description1 = simpleany_Description1 if simpleany_Description1 is not None else set()
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def simpleany_Description1(self):
        return self.__simpleany_Description1

    @simpleany_Description1.setter
    def simpleany_Description1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleany_Description__simpleany_Description1", None)
        self.__simpleany_Description1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleany_Description3"):
                    opp_val = getattr(item, "simpleany_Description3", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleany_Description3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleany_Description3"):
                    opp_val = getattr(item, "simpleany_Description3", None)
                    
                    setattr(item, "simpleany_Description3", self)
                    

    @property
    def simpleany_Description(self):
        return self.__simpleany_Description

    @simpleany_Description.setter
    def simpleany_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleany_Description__simpleany_Description", None)
        self.__simpleany_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleany_BookType"):
                opp_val = getattr(old_value, "simpleany_BookType", None)
                if opp_val == self:
                    setattr(old_value, "simpleany_BookType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleany_BookType"):
                opp_val = getattr(value, "simpleany_BookType", None)
                setattr(value, "simpleany_BookType", self)

    @property
    def simpleany_Description3(self):
        return self.__simpleany_Description3

    @simpleany_Description3.setter
    def simpleany_Description3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleany_Description__simpleany_Description3", None)
        self.__simpleany_Description3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleany_Description1"):
                opp_val = getattr(old_value, "simpleany_Description1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleany_Description1"):
                opp_val = getattr(value, "simpleany_Description1", None)
                if opp_val is None:
                    setattr(value, "simpleany_Description1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
