from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################







class Change_Password_UseCase:

    pass


class Manage_Notifications_UseCase:

    pass


class Manage_Tracking_UseCase:

    pass


class Settings_UseCase:

    pass


class view_the_count_each_app_has_been_opened_UseCase:

    pass


class View_time_spent_on_each_app_UseCase:

    pass


class View_points_scored_UseCase:

    pass


class Categorize_apps_as_productive___Social_UseCase:

    pass


class Home_Page_UseCase:

    pass


class Sign_up_UseCase:

    pass


class Login_UseCase:

    pass


class User_Actor:

    pass





class Login:

    def __init__(self, username: str, _attr: str):
        self.username = username
        self._attr = _attr
        
        pass
    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username



class Book:

    def __init__(self, Author: str, title: str, publisherCity: str, yearPublished: int, publisher: str, Book_Library_04: "Library" = None):
        self.Author = Author
        self.title = title
        self.publisherCity = publisherCity
        self.yearPublished = yearPublished
        self.publisher = publisher
        self.Book_Library_04 = Book_Library_04
        
        pass
    @property
    def publisher(self):
        return self.__publisher
    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def publisherCity(self):
        return self.__publisherCity
    @publisherCity.setter
    def publisherCity(self, publisherCity: str):
        self.__publisherCity = publisherCity

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Author(self):
        return self.__Author
    @Author.setter
    def Author(self, Author: str):
        self.__Author = Author

    @property
    def yearPublished(self):
        return self.__yearPublished
    @yearPublished.setter
    def yearPublished(self, yearPublished: int):
        self.__yearPublished = yearPublished

    @property
    def Book_Library_04(self):
        return self.__Book_Library_04
    @Book_Library_04.setter
    def Book_Library_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book__Book_Library_04", None)
        self.__Book_Library_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book_Library_15"):
                opp_val = getattr(old_value, "Book_Library_15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Library_15"):
                opp_val = getattr(value, "Book_Library_15", None)
                if opp_val is None:
                    setattr(value, "Book_Library_15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Library:

    def __init__(self, count: int, file: str, changeSinceLastSave: bool, collection: str, Book_Library_15: set["Book"] = None, libraryGui2: "LibraryGui" = None):
        self.count = count
        self.file = file
        self.changeSinceLastSave = changeSinceLastSave
        self.collection = collection
        self.Book_Library_15 = Book_Library_15 if Book_Library_15 is not None else set()
        self.libraryGui2 = libraryGui2
        
        pass
    @property
    def collection(self):
        return self.__collection
    @collection.setter
    def collection(self, collection: str):
        self.__collection = collection

    @property
    def changeSinceLastSave(self):
        return self.__changeSinceLastSave
    @changeSinceLastSave.setter
    def changeSinceLastSave(self, changeSinceLastSave: bool):
        self.__changeSinceLastSave = changeSinceLastSave

    @property
    def file(self):
        return self.__file
    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def libraryGui2(self):
        return self.__libraryGui2
    @libraryGui2.setter
    def libraryGui2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library__libraryGui2", None)
        self.__libraryGui2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library3"):
                opp_val = getattr(old_value, "library3", None)
                if opp_val == self:
                    setattr(old_value, "library3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library3"):
                opp_val = getattr(value, "library3", None)
                setattr(value, "library3", self)

    @property
    def Book_Library_15(self):
        return self.__Book_Library_15
    @Book_Library_15.setter
    def Book_Library_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library__Book_Library_15", None)
        self.__Book_Library_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book_Library_04"):
                    opp_val = getattr(item, "Book_Library_04", None)
                    
                    if opp_val == self:
                        setattr(item, "Book_Library_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book_Library_04"):
                    opp_val = getattr(item, "Book_Library_04", None)
                    
                    setattr(item, "Book_Library_04", self)
                    



class LibraryGui:

    def __init__(self, library: Library, libraryController: LibraryController, LibraryGui_LibraryController_00: "LibraryController" = None, library3: "Library" = None):
        self.library = library
        self.libraryController = libraryController
        self.LibraryGui_LibraryController_00 = LibraryGui_LibraryController_00
        self.library3 = library3
        
        pass
    @property
    def libraryController(self):
        return self.__libraryController
    @libraryController.setter
    def libraryController(self, libraryController: LibraryController):
        self.__libraryController = libraryController

    @property
    def library(self):
        return self.__library
    @library.setter
    def library(self, library: Library):
        self.__library = library

    @property
    def library3(self):
        return self.__library3
    @library3.setter
    def library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LibraryGui__library3", None)
        self.__library3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryGui2"):
                opp_val = getattr(old_value, "libraryGui2", None)
                if opp_val == self:
                    setattr(old_value, "libraryGui2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryGui2"):
                opp_val = getattr(value, "libraryGui2", None)
                setattr(value, "libraryGui2", self)

    @property
    def LibraryGui_LibraryController_00(self):
        return self.__LibraryGui_LibraryController_00
    @LibraryGui_LibraryController_00.setter
    def LibraryGui_LibraryController_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LibraryGui__LibraryGui_LibraryController_00", None)
        self.__LibraryGui_LibraryController_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LibraryGui_LibraryController_11"):
                opp_val = getattr(old_value, "LibraryGui_LibraryController_11", None)
                if opp_val == self:
                    setattr(old_value, "LibraryGui_LibraryController_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LibraryGui_LibraryController_11"):
                opp_val = getattr(value, "LibraryGui_LibraryController_11", None)
                setattr(value, "LibraryGui_LibraryController_11", self)



class LibraryController:

    def __init__(self, libraryDataAcces: str, LibraryGui_LibraryController_11: "LibraryGui" = None):
        self.libraryDataAcces = libraryDataAcces
        self.LibraryGui_LibraryController_11 = LibraryGui_LibraryController_11
        
        pass
    @property
    def libraryDataAcces(self):
        return self.__libraryDataAcces
    @libraryDataAcces.setter
    def libraryDataAcces(self, libraryDataAcces: str):
        self.__libraryDataAcces = libraryDataAcces

    @property
    def LibraryGui_LibraryController_11(self):
        return self.__LibraryGui_LibraryController_11
    @LibraryGui_LibraryController_11.setter
    def LibraryGui_LibraryController_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LibraryController__LibraryGui_LibraryController_11", None)
        self.__LibraryGui_LibraryController_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LibraryGui_LibraryController_00"):
                opp_val = getattr(old_value, "LibraryGui_LibraryController_00", None)
                if opp_val == self:
                    setattr(old_value, "LibraryGui_LibraryController_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LibraryGui_LibraryController_00"):
                opp_val = getattr(value, "LibraryGui_LibraryController_00", None)
                setattr(value, "LibraryGui_LibraryController_00", self)

