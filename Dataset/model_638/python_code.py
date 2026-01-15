from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class libraryModel_ecore_NamedElement:

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class libraryModel_ecore_LibraryModel:

    def __init__(self, LibraryModel5: "libraryModel_ecore_Author" = None, LibraryModel: "libraryModel_ecore_Book" = None, library: set["libraryModel_ecore_Book"] = None, library8: set["libraryModel_ecore_Author"] = None):
        self.LibraryModel5 = LibraryModel5
        self.LibraryModel = LibraryModel
        self.library = library if library is not None else set()
        self.library8 = library8 if library8 is not None else set()
        
    @property
    def library8(self):
        return self.__library8

    @library8.setter
    def library8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_ecore_LibraryModel__library8", None)
        self.__library8 = value if value is not None else set()
        
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
    def LibraryModel5(self):
        return self.__LibraryModel5

    @LibraryModel5.setter
    def LibraryModel5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_ecore_LibraryModel__LibraryModel5", None)
        self.__LibraryModel5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authors"):
                opp_val = getattr(old_value, "authors", None)
                if opp_val == self:
                    setattr(old_value, "authors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authors"):
                opp_val = getattr(value, "authors", None)
                setattr(value, "authors", self)

    @property
    def LibraryModel(self):
        return self.__LibraryModel

    @LibraryModel.setter
    def LibraryModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_ecore_LibraryModel__LibraryModel", None)
        self.__LibraryModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book"):
                opp_val = getattr(old_value, "book", None)
                if opp_val == self:
                    setattr(old_value, "book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book"):
                opp_val = getattr(value, "book", None)
                setattr(value, "book", self)

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_ecore_LibraryModel__library", None)
        self.__library = value if value is not None else set()
        
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
                    

    def printLibrary(self):
        # TODO: Implement printLibrary method
        pass

class NamedElement:

    pass
class libraryModel_ecore_Author(NamedElement):

    pass
class libraryModel_ecore_Book(NamedElement):

    pass
class libraryModel_ecore_Picture(NamedElement):

    def __init__(self, pageNumber: str, Picture: "libraryModel_ecore_Book" = None, pictures: "libraryModel_ecore_Book" = None):
        self.pageNumber = pageNumber
        self.Picture = Picture
        self.pictures = pictures
        
    @property
    def pageNumber(self) -> str:
        return self.__pageNumber

    @pageNumber.setter
    def pageNumber(self, pageNumber: str):
        self.__pageNumber = pageNumber

    @property
    def pictures(self):
        return self.__pictures

    @pictures.setter
    def pictures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_ecore_Picture__pictures", None)
        self.__pictures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book10"):
                opp_val = getattr(old_value, "Book10", None)
                if opp_val == self:
                    setattr(old_value, "Book10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book10"):
                opp_val = getattr(value, "Book10", None)
                setattr(value, "Book10", self)

    @property
    def Picture(self):
        return self.__Picture

    @Picture.setter
    def Picture(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_ecore_Picture__Picture", None)
        self.__Picture = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book3"):
                opp_val = getattr(old_value, "book3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book3"):
                opp_val = getattr(value, "book3", None)
                if opp_val is None:
                    setattr(value, "book3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
