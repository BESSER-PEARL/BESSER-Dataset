from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DictionaryLanguage_Entry:

    def __init__(self, content: str, level: str, DictionaryLanguage_Entry: "DictionaryLanguage_Dictionary" = None):
        self.content = content
        self.level = level
        self.DictionaryLanguage_Entry = DictionaryLanguage_Entry
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def DictionaryLanguage_Entry(self):
        return self.__DictionaryLanguage_Entry

    @DictionaryLanguage_Entry.setter
    def DictionaryLanguage_Entry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Entry__DictionaryLanguage_Entry", None)
        self.__DictionaryLanguage_Entry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DictionaryLanguage_Dictionary"):
                opp_val = getattr(old_value, "DictionaryLanguage_Dictionary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DictionaryLanguage_Dictionary"):
                opp_val = getattr(value, "DictionaryLanguage_Dictionary", None)
                if opp_val is None:
                    setattr(value, "DictionaryLanguage_Dictionary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DictionaryLanguage_Shelf:

    def __init__(self, description: str, Shelf: "DictionaryLanguage_Dictionary" = None, DictionaryLanguage_Shelf: "DictionaryLanguage_Library" = None, shelf: set["DictionaryLanguage_Dictionary"] = None):
        self.description = description
        self.Shelf = Shelf
        self.DictionaryLanguage_Shelf = DictionaryLanguage_Shelf
        self.shelf = shelf if shelf is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Shelf(self):
        return self.__Shelf

    @Shelf.setter
    def Shelf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Shelf__Shelf", None)
        self.__Shelf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dictionary"):
                opp_val = getattr(old_value, "dictionary", None)
                if opp_val == self:
                    setattr(old_value, "dictionary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dictionary"):
                opp_val = getattr(value, "dictionary", None)
                setattr(value, "dictionary", self)

    @property
    def shelf(self):
        return self.__shelf

    @shelf.setter
    def shelf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Shelf__shelf", None)
        self.__shelf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dictionary11"):
                    opp_val = getattr(item, "Dictionary11", None)
                    
                    if opp_val == self:
                        setattr(item, "Dictionary11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dictionary11"):
                    opp_val = getattr(item, "Dictionary11", None)
                    
                    setattr(item, "Dictionary11", self)
                    

    @property
    def DictionaryLanguage_Shelf(self):
        return self.__DictionaryLanguage_Shelf

    @DictionaryLanguage_Shelf.setter
    def DictionaryLanguage_Shelf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Shelf__DictionaryLanguage_Shelf", None)
        self.__DictionaryLanguage_Shelf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DictionaryLanguage_Library"):
                opp_val = getattr(old_value, "DictionaryLanguage_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DictionaryLanguage_Library"):
                opp_val = getattr(value, "DictionaryLanguage_Library", None)
                if opp_val is None:
                    setattr(value, "DictionaryLanguage_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DictionaryLanguage_Dictionary:

    def __init__(self, title: str, Dictionary: "DictionaryLanguage_Author" = None, Dictionary11: "DictionaryLanguage_Shelf" = None, dictionary: "DictionaryLanguage_Shelf" = None, dictionary5: "DictionaryLanguage_Author" = None, DictionaryLanguage_Dictionary: set["DictionaryLanguage_Entry"] = None):
        self.title = title
        self.Dictionary = Dictionary
        self.Dictionary11 = Dictionary11
        self.dictionary = dictionary
        self.dictionary5 = dictionary5
        self.DictionaryLanguage_Dictionary = DictionaryLanguage_Dictionary if DictionaryLanguage_Dictionary is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Dictionary11(self):
        return self.__Dictionary11

    @Dictionary11.setter
    def Dictionary11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Dictionary__Dictionary11", None)
        self.__Dictionary11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shelf"):
                opp_val = getattr(old_value, "shelf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shelf"):
                opp_val = getattr(value, "shelf", None)
                if opp_val is None:
                    setattr(value, "shelf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DictionaryLanguage_Dictionary(self):
        return self.__DictionaryLanguage_Dictionary

    @DictionaryLanguage_Dictionary.setter
    def DictionaryLanguage_Dictionary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Dictionary__DictionaryLanguage_Dictionary", None)
        self.__DictionaryLanguage_Dictionary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DictionaryLanguage_Entry"):
                    opp_val = getattr(item, "DictionaryLanguage_Entry", None)
                    
                    if opp_val == self:
                        setattr(item, "DictionaryLanguage_Entry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DictionaryLanguage_Entry"):
                    opp_val = getattr(item, "DictionaryLanguage_Entry", None)
                    
                    setattr(item, "DictionaryLanguage_Entry", self)
                    

    @property
    def Dictionary(self):
        return self.__Dictionary

    @Dictionary.setter
    def Dictionary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Dictionary__Dictionary", None)
        self.__Dictionary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author2"):
                opp_val = getattr(old_value, "author2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author2"):
                opp_val = getattr(value, "author2", None)
                if opp_val is None:
                    setattr(value, "author2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dictionary(self):
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Dictionary__dictionary", None)
        self.__dictionary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Shelf"):
                opp_val = getattr(old_value, "Shelf", None)
                if opp_val == self:
                    setattr(old_value, "Shelf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Shelf"):
                opp_val = getattr(value, "Shelf", None)
                setattr(value, "Shelf", self)

    @property
    def dictionary5(self):
        return self.__dictionary5

    @dictionary5.setter
    def dictionary5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Dictionary__dictionary5", None)
        self.__dictionary5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Author"):
                opp_val = getattr(old_value, "Author", None)
                if opp_val == self:
                    setattr(old_value, "Author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Author"):
                opp_val = getattr(value, "Author", None)
                setattr(value, "Author", self)

class DictionaryLanguage_Library:

    def __init__(self, name: str, Library: "DictionaryLanguage_Author" = None, DictionaryLanguage_Library: set["DictionaryLanguage_Shelf"] = None, library: set["DictionaryLanguage_Author"] = None):
        self.name = name
        self.Library = Library
        self.DictionaryLanguage_Library = DictionaryLanguage_Library if DictionaryLanguage_Library is not None else set()
        self.library = library if library is not None else set()
        
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
        old_value = getattr(self, f"_DictionaryLanguage_Library__library", None)
        self.__library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author9"):
                    opp_val = getattr(item, "Author9", None)
                    
                    if opp_val == self:
                        setattr(item, "Author9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author9"):
                    opp_val = getattr(item, "Author9", None)
                    
                    setattr(item, "Author9", self)
                    

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author"):
                opp_val = getattr(old_value, "author", None)
                if opp_val == self:
                    setattr(old_value, "author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author"):
                opp_val = getattr(value, "author", None)
                setattr(value, "author", self)

    @property
    def DictionaryLanguage_Library(self):
        return self.__DictionaryLanguage_Library

    @DictionaryLanguage_Library.setter
    def DictionaryLanguage_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Library__DictionaryLanguage_Library", None)
        self.__DictionaryLanguage_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DictionaryLanguage_Shelf"):
                    opp_val = getattr(item, "DictionaryLanguage_Shelf", None)
                    
                    if opp_val == self:
                        setattr(item, "DictionaryLanguage_Shelf", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DictionaryLanguage_Shelf"):
                    opp_val = getattr(item, "DictionaryLanguage_Shelf", None)
                    
                    setattr(item, "DictionaryLanguage_Shelf", self)
                    

class DictionaryLanguage_Author:

    def __init__(self, email: str, author: "DictionaryLanguage_Library" = None, author2: set["DictionaryLanguage_Dictionary"] = None, Author: "DictionaryLanguage_Dictionary" = None, Author9: "DictionaryLanguage_Library" = None):
        self.email = email
        self.author = author
        self.author2 = author2 if author2 is not None else set()
        self.Author = Author
        self.Author9 = Author9
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Author__Author", None)
        self.__Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dictionary5"):
                opp_val = getattr(old_value, "dictionary5", None)
                if opp_val == self:
                    setattr(old_value, "dictionary5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dictionary5"):
                opp_val = getattr(value, "dictionary5", None)
                setattr(value, "dictionary5", self)

    @property
    def Author9(self):
        return self.__Author9

    @Author9.setter
    def Author9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Author__Author9", None)
        self.__Author9 = value
        
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

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Author__author", None)
        self.__author = value
        
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
    def author2(self):
        return self.__author2

    @author2.setter
    def author2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DictionaryLanguage_Author__author2", None)
        self.__author2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dictionary"):
                    opp_val = getattr(item, "Dictionary", None)
                    
                    if opp_val == self:
                        setattr(item, "Dictionary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dictionary"):
                    opp_val = getattr(item, "Dictionary", None)
                    
                    setattr(item, "Dictionary", self)
                    
