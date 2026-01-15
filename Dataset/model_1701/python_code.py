from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_t_published:

    def __init__(self, tagName: str, text: str, library_t_published: "library_t_book" = None, library_t_published12: "library_t_book" = None):
        self.tagName = tagName
        self.text = text
        self.library_t_published = library_t_published
        self.library_t_published12 = library_t_published12
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def library_t_published12(self):
        return self.__library_t_published12

    @library_t_published12.setter
    def library_t_published12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_published__library_t_published12", None)
        self.__library_t_published12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_t_book13"):
                opp_val = getattr(old_value, "library_t_book13", None)
                if opp_val == self:
                    setattr(old_value, "library_t_book13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_t_book13"):
                opp_val = getattr(value, "library_t_book13", None)
                setattr(value, "library_t_book13", self)

    @property
    def library_t_published(self):
        return self.__library_t_published

    @library_t_published.setter
    def library_t_published(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_published__library_t_published", None)
        self.__library_t_published = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_t_book7"):
                opp_val = getattr(old_value, "library_t_book7", None)
                if opp_val == self:
                    setattr(old_value, "library_t_book7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_t_book7"):
                opp_val = getattr(value, "library_t_book7", None)
                setattr(value, "library_t_book7", self)

class library_t_author:

    def __init__(self, tagName: str, text: str, library_t_author: "library_t_book" = None, library_t_author9: "library_t_book" = None):
        self.tagName = tagName
        self.text = text
        self.library_t_author = library_t_author
        self.library_t_author9 = library_t_author9
        
    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def library_t_author9(self):
        return self.__library_t_author9

    @library_t_author9.setter
    def library_t_author9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_author__library_t_author9", None)
        self.__library_t_author9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_t_book10"):
                opp_val = getattr(old_value, "library_t_book10", None)
                if opp_val == self:
                    setattr(old_value, "library_t_book10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_t_book10"):
                opp_val = getattr(value, "library_t_book10", None)
                setattr(value, "library_t_book10", self)

    @property
    def library_t_author(self):
        return self.__library_t_author

    @library_t_author.setter
    def library_t_author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_author__library_t_author", None)
        self.__library_t_author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_t_book5"):
                opp_val = getattr(old_value, "library_t_book5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_t_book5"):
                opp_val = getattr(value, "library_t_book5", None)
                if opp_val is None:
                    setattr(value, "library_t_book5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_t_book:

    def __init__(self, text: str, pages: int, title: str, tagName: str, library_t_book: "library_t_library" = None, library_t_book2: "library_t_library" = None, library_t_book5: set["library_t_author"] = None, library_t_book7: "library_t_published" = None, library_t_book10: "library_t_author" = None, library_t_book13: "library_t_published" = None):
        self.text = text
        self.pages = pages
        self.title = title
        self.tagName = tagName
        self.library_t_book = library_t_book
        self.library_t_book2 = library_t_book2
        self.library_t_book5 = library_t_book5 if library_t_book5 is not None else set()
        self.library_t_book7 = library_t_book7
        self.library_t_book10 = library_t_book10
        self.library_t_book13 = library_t_book13
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

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
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def library_t_book2(self):
        return self.__library_t_book2

    @library_t_book2.setter
    def library_t_book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_book__library_t_book2", None)
        self.__library_t_book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_t_library3"):
                opp_val = getattr(old_value, "library_t_library3", None)
                if opp_val == self:
                    setattr(old_value, "library_t_library3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_t_library3"):
                opp_val = getattr(value, "library_t_library3", None)
                setattr(value, "library_t_library3", self)

    @property
    def library_t_book13(self):
        return self.__library_t_book13

    @library_t_book13.setter
    def library_t_book13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_book__library_t_book13", None)
        self.__library_t_book13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_t_published12"):
                opp_val = getattr(old_value, "library_t_published12", None)
                if opp_val == self:
                    setattr(old_value, "library_t_published12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_t_published12"):
                opp_val = getattr(value, "library_t_published12", None)
                setattr(value, "library_t_published12", self)

    @property
    def library_t_book(self):
        return self.__library_t_book

    @library_t_book.setter
    def library_t_book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_book__library_t_book", None)
        self.__library_t_book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_t_library"):
                opp_val = getattr(old_value, "library_t_library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_t_library"):
                opp_val = getattr(value, "library_t_library", None)
                if opp_val is None:
                    setattr(value, "library_t_library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_t_book10(self):
        return self.__library_t_book10

    @library_t_book10.setter
    def library_t_book10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_book__library_t_book10", None)
        self.__library_t_book10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_t_author9"):
                opp_val = getattr(old_value, "library_t_author9", None)
                if opp_val == self:
                    setattr(old_value, "library_t_author9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_t_author9"):
                opp_val = getattr(value, "library_t_author9", None)
                setattr(value, "library_t_author9", self)

    @property
    def library_t_book5(self):
        return self.__library_t_book5

    @library_t_book5.setter
    def library_t_book5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_book__library_t_book5", None)
        self.__library_t_book5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_t_author"):
                    opp_val = getattr(item, "library_t_author", None)
                    
                    if opp_val == self:
                        setattr(item, "library_t_author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_t_author"):
                    opp_val = getattr(item, "library_t_author", None)
                    
                    setattr(item, "library_t_author", self)
                    

    @property
    def library_t_book7(self):
        return self.__library_t_book7

    @library_t_book7.setter
    def library_t_book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_book__library_t_book7", None)
        self.__library_t_book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_t_published"):
                opp_val = getattr(old_value, "library_t_published", None)
                if opp_val == self:
                    setattr(old_value, "library_t_published", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_t_published"):
                opp_val = getattr(value, "library_t_published", None)
                setattr(value, "library_t_published", self)

class library_t_library:

    def __init__(self, tagName: str, text: str, library_t_library: set["library_t_book"] = None, library_t_library3: "library_t_book" = None):
        self.tagName = tagName
        self.text = text
        self.library_t_library = library_t_library if library_t_library is not None else set()
        self.library_t_library3 = library_t_library3
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def library_t_library3(self):
        return self.__library_t_library3

    @library_t_library3.setter
    def library_t_library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_library__library_t_library3", None)
        self.__library_t_library3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_t_book2"):
                opp_val = getattr(old_value, "library_t_book2", None)
                if opp_val == self:
                    setattr(old_value, "library_t_book2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_t_book2"):
                opp_val = getattr(value, "library_t_book2", None)
                setattr(value, "library_t_book2", self)

    @property
    def library_t_library(self):
        return self.__library_t_library

    @library_t_library.setter
    def library_t_library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_t_library__library_t_library", None)
        self.__library_t_library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_t_book"):
                    opp_val = getattr(item, "library_t_book", None)
                    
                    if opp_val == self:
                        setattr(item, "library_t_book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_t_book"):
                    opp_val = getattr(item, "library_t_book", None)
                    
                    setattr(item, "library_t_book", self)
                    
