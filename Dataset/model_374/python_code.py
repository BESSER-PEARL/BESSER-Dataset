from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Writer:

    pass
class library_GuideBookWriter(Writer):

    def __init__(self, countries: str):
        self.countries = countries
        
    @property
    def countries(self) -> str:
        return self.__countries

    @countries.setter
    def countries(self, countries: str):
        self.__countries = countries

class library_Library:

    def __init__(self, name: str, library_Library: set["library_Book"] = None):
        self.name = name
        self.library_Library = library_Library if library_Library is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Library(self):
        return self.__library_Library

    @library_Library.setter
    def library_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library", None)
        self.__library_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book2"):
                    opp_val = getattr(item, "library_Book2", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book2"):
                    opp_val = getattr(item, "library_Book2", None)
                    
                    setattr(item, "library_Book2", self)
                    

class library_Writer:

    def __init__(self, name: str, library_Writer: "library_Book" = None):
        self.name = name
        self.library_Writer = library_Writer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Writer(self):
        return self.__library_Writer

    @library_Writer.setter
    def library_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer", None)
        self.__library_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book"):
                opp_val = getattr(old_value, "library_Book", None)
                if opp_val == self:
                    setattr(old_value, "library_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book"):
                opp_val = getattr(value, "library_Book", None)
                setattr(value, "library_Book", self)

class library_Book:

    def __init__(self, title: str, pages: str, library_Book: "library_Writer" = None, library_Book2: "library_Library" = None):
        self.title = title
        self.pages = pages
        self.library_Book = library_Book
        self.library_Book2 = library_Book2
        
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
    def library_Book2(self):
        return self.__library_Book2

    @library_Book2.setter
    def library_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book2", None)
        self.__library_Book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library"):
                opp_val = getattr(old_value, "library_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library"):
                opp_val = getattr(value, "library_Library", None)
                if opp_val is None:
                    setattr(value, "library_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Book(self):
        return self.__library_Book

    @library_Book.setter
    def library_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book", None)
        self.__library_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Writer"):
                opp_val = getattr(old_value, "library_Writer", None)
                if opp_val == self:
                    setattr(old_value, "library_Writer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Writer"):
                opp_val = getattr(value, "library_Writer", None)
                setattr(value, "library_Writer", self)

class library_SpecialistBookWriter(Writer):

    def __init__(self, subject: str):
        self.subject = subject
        
    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject
