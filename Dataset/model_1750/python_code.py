from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class libraryinteractionmodel_Client:

    def __init__(self, name: str, email: str, libraryinteractionmodel_Client: "libraryinteractionmodel_Client" = None, libraryinteractionmodel_Client17: "libraryinteractionmodel_Client" = None, libraryinteractionmodel_Client21: "libraryinteractionmodel_Clients" = None, libraryinteractionmodel_Client24: "libraryinteractionmodel_Reservation" = None):
        self.name = name
        self.email = email
        self.libraryinteractionmodel_Client = libraryinteractionmodel_Client
        self.libraryinteractionmodel_Client17 = libraryinteractionmodel_Client17
        self.libraryinteractionmodel_Client21 = libraryinteractionmodel_Client21
        self.libraryinteractionmodel_Client24 = libraryinteractionmodel_Client24
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libraryinteractionmodel_Client24(self):
        return self.__libraryinteractionmodel_Client24

    @libraryinteractionmodel_Client24.setter
    def libraryinteractionmodel_Client24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Client__libraryinteractionmodel_Client24", None)
        self.__libraryinteractionmodel_Client24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Reservation23"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Reservation23", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Reservation23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Reservation23"):
                opp_val = getattr(value, "libraryinteractionmodel_Reservation23", None)
                setattr(value, "libraryinteractionmodel_Reservation23", self)

    @property
    def libraryinteractionmodel_Client(self):
        return self.__libraryinteractionmodel_Client

    @libraryinteractionmodel_Client.setter
    def libraryinteractionmodel_Client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Client__libraryinteractionmodel_Client", None)
        self.__libraryinteractionmodel_Client = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Client17"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Client17", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Client17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Client17"):
                opp_val = getattr(value, "libraryinteractionmodel_Client17", None)
                setattr(value, "libraryinteractionmodel_Client17", self)

    @property
    def libraryinteractionmodel_Client17(self):
        return self.__libraryinteractionmodel_Client17

    @libraryinteractionmodel_Client17.setter
    def libraryinteractionmodel_Client17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Client__libraryinteractionmodel_Client17", None)
        self.__libraryinteractionmodel_Client17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Client"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Client", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Client", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Client"):
                opp_val = getattr(value, "libraryinteractionmodel_Client", None)
                setattr(value, "libraryinteractionmodel_Client", self)

    @property
    def libraryinteractionmodel_Client21(self):
        return self.__libraryinteractionmodel_Client21

    @libraryinteractionmodel_Client21.setter
    def libraryinteractionmodel_Client21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Client__libraryinteractionmodel_Client21", None)
        self.__libraryinteractionmodel_Client21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Clients20"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Clients20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Clients20"):
                opp_val = getattr(value, "libraryinteractionmodel_Clients20", None)
                if opp_val is None:
                    setattr(value, "libraryinteractionmodel_Clients20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class libraryinteractionmodel_Author:

    def __init__(self, fullBio: str, name: str, nationality: str, libraryinteractionmodel_Author: "libraryinteractionmodel_AuthorShort" = None, libraryinteractionmodel_Author29: set["libraryinteractionmodel_BookShort"] = None):
        self.fullBio = fullBio
        self.name = name
        self.nationality = nationality
        self.libraryinteractionmodel_Author = libraryinteractionmodel_Author
        self.libraryinteractionmodel_Author29 = libraryinteractionmodel_Author29 if libraryinteractionmodel_Author29 is not None else set()
        
    @property
    def nationality(self) -> str:
        return self.__nationality

    @nationality.setter
    def nationality(self, nationality: str):
        self.__nationality = nationality

    @property
    def fullBio(self) -> str:
        return self.__fullBio

    @fullBio.setter
    def fullBio(self, fullBio: str):
        self.__fullBio = fullBio

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libraryinteractionmodel_Author(self):
        return self.__libraryinteractionmodel_Author

    @libraryinteractionmodel_Author.setter
    def libraryinteractionmodel_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Author__libraryinteractionmodel_Author", None)
        self.__libraryinteractionmodel_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_AuthorShort16"):
                opp_val = getattr(old_value, "libraryinteractionmodel_AuthorShort16", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_AuthorShort16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_AuthorShort16"):
                opp_val = getattr(value, "libraryinteractionmodel_AuthorShort16", None)
                setattr(value, "libraryinteractionmodel_AuthorShort16", self)

    @property
    def libraryinteractionmodel_Author29(self):
        return self.__libraryinteractionmodel_Author29

    @libraryinteractionmodel_Author29.setter
    def libraryinteractionmodel_Author29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Author__libraryinteractionmodel_Author29", None)
        self.__libraryinteractionmodel_Author29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryinteractionmodel_BookShort30"):
                    opp_val = getattr(item, "libraryinteractionmodel_BookShort30", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryinteractionmodel_BookShort30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryinteractionmodel_BookShort30"):
                    opp_val = getattr(item, "libraryinteractionmodel_BookShort30", None)
                    
                    setattr(item, "libraryinteractionmodel_BookShort30", self)
                    

class libraryinteractionmodel_BookShort:

    def __init__(self, isbn: str, title: str, libraryinteractionmodel_BookShort: "libraryinteractionmodel_Books" = None, libraryinteractionmodel_BookShort30: "libraryinteractionmodel_Author" = None, libraryinteractionmodel_BookShort32: "libraryinteractionmodel_Book" = None):
        self.isbn = isbn
        self.title = title
        self.libraryinteractionmodel_BookShort = libraryinteractionmodel_BookShort
        self.libraryinteractionmodel_BookShort30 = libraryinteractionmodel_BookShort30
        self.libraryinteractionmodel_BookShort32 = libraryinteractionmodel_BookShort32
        
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
    def libraryinteractionmodel_BookShort(self):
        return self.__libraryinteractionmodel_BookShort

    @libraryinteractionmodel_BookShort.setter
    def libraryinteractionmodel_BookShort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_BookShort__libraryinteractionmodel_BookShort", None)
        self.__libraryinteractionmodel_BookShort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Books11"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Books11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Books11"):
                opp_val = getattr(value, "libraryinteractionmodel_Books11", None)
                if opp_val is None:
                    setattr(value, "libraryinteractionmodel_Books11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryinteractionmodel_BookShort30(self):
        return self.__libraryinteractionmodel_BookShort30

    @libraryinteractionmodel_BookShort30.setter
    def libraryinteractionmodel_BookShort30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_BookShort__libraryinteractionmodel_BookShort30", None)
        self.__libraryinteractionmodel_BookShort30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Author29"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Author29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Author29"):
                opp_val = getattr(value, "libraryinteractionmodel_Author29", None)
                if opp_val is None:
                    setattr(value, "libraryinteractionmodel_Author29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryinteractionmodel_BookShort32(self):
        return self.__libraryinteractionmodel_BookShort32

    @libraryinteractionmodel_BookShort32.setter
    def libraryinteractionmodel_BookShort32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_BookShort__libraryinteractionmodel_BookShort32", None)
        self.__libraryinteractionmodel_BookShort32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Book33"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Book33", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Book33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Book33"):
                opp_val = getattr(value, "libraryinteractionmodel_Book33", None)
                setattr(value, "libraryinteractionmodel_Book33", self)

class libraryinteractionmodel_Reservations:

    pass
class libraryinteractionmodel_Reservation:

    def __init__(self, to: date, from: date, libraryinteractionmodel_Reservation: "libraryinteractionmodel_Book" = None, libraryinteractionmodel_Reservation23: "libraryinteractionmodel_Client" = None, libraryinteractionmodel_Reservation26: "libraryinteractionmodel_Book" = None, libraryinteractionmodel_Reservation36: "libraryinteractionmodel_Reservations" = None):
        self.to = to
        self.from = from
        self.libraryinteractionmodel_Reservation = libraryinteractionmodel_Reservation
        self.libraryinteractionmodel_Reservation23 = libraryinteractionmodel_Reservation23
        self.libraryinteractionmodel_Reservation26 = libraryinteractionmodel_Reservation26
        self.libraryinteractionmodel_Reservation36 = libraryinteractionmodel_Reservation36
        
    @property
    def to(self) -> date:
        return self.__to

    @to.setter
    def to(self, to: date):
        self.__to = to

    @property
    def from(self) -> date:
        return self.__from

    @from.setter
    def from(self, from: date):
        self.__from = from

    @property
    def libraryinteractionmodel_Reservation23(self):
        return self.__libraryinteractionmodel_Reservation23

    @libraryinteractionmodel_Reservation23.setter
    def libraryinteractionmodel_Reservation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Reservation__libraryinteractionmodel_Reservation23", None)
        self.__libraryinteractionmodel_Reservation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Client24"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Client24", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Client24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Client24"):
                opp_val = getattr(value, "libraryinteractionmodel_Client24", None)
                setattr(value, "libraryinteractionmodel_Client24", self)

    @property
    def libraryinteractionmodel_Reservation(self):
        return self.__libraryinteractionmodel_Reservation

    @libraryinteractionmodel_Reservation.setter
    def libraryinteractionmodel_Reservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Reservation__libraryinteractionmodel_Reservation", None)
        self.__libraryinteractionmodel_Reservation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Book7"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Book7", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Book7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Book7"):
                opp_val = getattr(value, "libraryinteractionmodel_Book7", None)
                setattr(value, "libraryinteractionmodel_Book7", self)

    @property
    def libraryinteractionmodel_Reservation26(self):
        return self.__libraryinteractionmodel_Reservation26

    @libraryinteractionmodel_Reservation26.setter
    def libraryinteractionmodel_Reservation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Reservation__libraryinteractionmodel_Reservation26", None)
        self.__libraryinteractionmodel_Reservation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Book27"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Book27", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Book27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Book27"):
                opp_val = getattr(value, "libraryinteractionmodel_Book27", None)
                setattr(value, "libraryinteractionmodel_Book27", self)

    @property
    def libraryinteractionmodel_Reservation36(self):
        return self.__libraryinteractionmodel_Reservation36

    @libraryinteractionmodel_Reservation36.setter
    def libraryinteractionmodel_Reservation36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Reservation__libraryinteractionmodel_Reservation36", None)
        self.__libraryinteractionmodel_Reservation36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Reservations35"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Reservations35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Reservations35"):
                opp_val = getattr(value, "libraryinteractionmodel_Reservations35", None)
                if opp_val is None:
                    setattr(value, "libraryinteractionmodel_Reservations35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class libraryinteractionmodel_AuthorShort:

    def __init__(self, nationality: str, name: str, libraryinteractionmodel_AuthorShort: "libraryinteractionmodel_Book" = None, libraryinteractionmodel_AuthorShort14: "libraryinteractionmodel_Authors" = None, libraryinteractionmodel_AuthorShort16: "libraryinteractionmodel_Author" = None):
        self.nationality = nationality
        self.name = name
        self.libraryinteractionmodel_AuthorShort = libraryinteractionmodel_AuthorShort
        self.libraryinteractionmodel_AuthorShort14 = libraryinteractionmodel_AuthorShort14
        self.libraryinteractionmodel_AuthorShort16 = libraryinteractionmodel_AuthorShort16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nationality(self) -> str:
        return self.__nationality

    @nationality.setter
    def nationality(self, nationality: str):
        self.__nationality = nationality

    @property
    def libraryinteractionmodel_AuthorShort14(self):
        return self.__libraryinteractionmodel_AuthorShort14

    @libraryinteractionmodel_AuthorShort14.setter
    def libraryinteractionmodel_AuthorShort14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_AuthorShort__libraryinteractionmodel_AuthorShort14", None)
        self.__libraryinteractionmodel_AuthorShort14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Authors13"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Authors13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Authors13"):
                opp_val = getattr(value, "libraryinteractionmodel_Authors13", None)
                if opp_val is None:
                    setattr(value, "libraryinteractionmodel_Authors13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryinteractionmodel_AuthorShort16(self):
        return self.__libraryinteractionmodel_AuthorShort16

    @libraryinteractionmodel_AuthorShort16.setter
    def libraryinteractionmodel_AuthorShort16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_AuthorShort__libraryinteractionmodel_AuthorShort16", None)
        self.__libraryinteractionmodel_AuthorShort16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Author"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Author", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Author"):
                opp_val = getattr(value, "libraryinteractionmodel_Author", None)
                setattr(value, "libraryinteractionmodel_Author", self)

    @property
    def libraryinteractionmodel_AuthorShort(self):
        return self.__libraryinteractionmodel_AuthorShort

    @libraryinteractionmodel_AuthorShort.setter
    def libraryinteractionmodel_AuthorShort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_AuthorShort__libraryinteractionmodel_AuthorShort", None)
        self.__libraryinteractionmodel_AuthorShort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Book"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Book", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Book"):
                opp_val = getattr(value, "libraryinteractionmodel_Book", None)
                setattr(value, "libraryinteractionmodel_Book", self)

class libraryinteractionmodel_Clients:

    pass
class libraryinteractionmodel_Authors:

    pass
class libraryinteractionmodel_Books:

    pass
class libraryinteractionmodel_Library:

    pass
class libraryinteractionmodel_Book:

    def __init__(self, isbn: str, title: str, libraryinteractionmodel_Book: "libraryinteractionmodel_AuthorShort" = None, libraryinteractionmodel_Book7: "libraryinteractionmodel_Reservation" = None, libraryinteractionmodel_Book9: "libraryinteractionmodel_Reservations" = None, libraryinteractionmodel_Book27: "libraryinteractionmodel_Reservation" = None, libraryinteractionmodel_Book33: "libraryinteractionmodel_BookShort" = None):
        self.isbn = isbn
        self.title = title
        self.libraryinteractionmodel_Book = libraryinteractionmodel_Book
        self.libraryinteractionmodel_Book7 = libraryinteractionmodel_Book7
        self.libraryinteractionmodel_Book9 = libraryinteractionmodel_Book9
        self.libraryinteractionmodel_Book27 = libraryinteractionmodel_Book27
        self.libraryinteractionmodel_Book33 = libraryinteractionmodel_Book33
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def libraryinteractionmodel_Book7(self):
        return self.__libraryinteractionmodel_Book7

    @libraryinteractionmodel_Book7.setter
    def libraryinteractionmodel_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Book__libraryinteractionmodel_Book7", None)
        self.__libraryinteractionmodel_Book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Reservation"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Reservation", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Reservation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Reservation"):
                opp_val = getattr(value, "libraryinteractionmodel_Reservation", None)
                setattr(value, "libraryinteractionmodel_Reservation", self)

    @property
    def libraryinteractionmodel_Book9(self):
        return self.__libraryinteractionmodel_Book9

    @libraryinteractionmodel_Book9.setter
    def libraryinteractionmodel_Book9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Book__libraryinteractionmodel_Book9", None)
        self.__libraryinteractionmodel_Book9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Reservations"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Reservations", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Reservations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Reservations"):
                opp_val = getattr(value, "libraryinteractionmodel_Reservations", None)
                setattr(value, "libraryinteractionmodel_Reservations", self)

    @property
    def libraryinteractionmodel_Book33(self):
        return self.__libraryinteractionmodel_Book33

    @libraryinteractionmodel_Book33.setter
    def libraryinteractionmodel_Book33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Book__libraryinteractionmodel_Book33", None)
        self.__libraryinteractionmodel_Book33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_BookShort32"):
                opp_val = getattr(old_value, "libraryinteractionmodel_BookShort32", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_BookShort32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_BookShort32"):
                opp_val = getattr(value, "libraryinteractionmodel_BookShort32", None)
                setattr(value, "libraryinteractionmodel_BookShort32", self)

    @property
    def libraryinteractionmodel_Book27(self):
        return self.__libraryinteractionmodel_Book27

    @libraryinteractionmodel_Book27.setter
    def libraryinteractionmodel_Book27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Book__libraryinteractionmodel_Book27", None)
        self.__libraryinteractionmodel_Book27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_Reservation26"):
                opp_val = getattr(old_value, "libraryinteractionmodel_Reservation26", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_Reservation26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_Reservation26"):
                opp_val = getattr(value, "libraryinteractionmodel_Reservation26", None)
                setattr(value, "libraryinteractionmodel_Reservation26", self)

    @property
    def libraryinteractionmodel_Book(self):
        return self.__libraryinteractionmodel_Book

    @libraryinteractionmodel_Book.setter
    def libraryinteractionmodel_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryinteractionmodel_Book__libraryinteractionmodel_Book", None)
        self.__libraryinteractionmodel_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryinteractionmodel_AuthorShort"):
                opp_val = getattr(old_value, "libraryinteractionmodel_AuthorShort", None)
                if opp_val == self:
                    setattr(old_value, "libraryinteractionmodel_AuthorShort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryinteractionmodel_AuthorShort"):
                opp_val = getattr(value, "libraryinteractionmodel_AuthorShort", None)
                setattr(value, "libraryinteractionmodel_AuthorShort", self)
