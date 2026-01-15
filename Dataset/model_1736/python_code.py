from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Ent:

    pass
class bookstore_Magazine(Ent):

    def __init__(self, title: str, pages: int, version: str, bookstore_Magazine: "bookstore_Person" = None):
        self.title = title
        self.pages = pages
        self.version = version
        self.bookstore_Magazine = bookstore_Magazine
        
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def bookstore_Magazine(self):
        return self.__bookstore_Magazine

    @bookstore_Magazine.setter
    def bookstore_Magazine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Magazine__bookstore_Magazine", None)
        self.__bookstore_Magazine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Person9"):
                opp_val = getattr(old_value, "bookstore_Person9", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Person9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Person9"):
                opp_val = getattr(value, "bookstore_Person9", None)
                setattr(value, "bookstore_Person9", self)

class bookstore_Dvd(Ent):

    def __init__(self, title: str, bookstore_Dvd: set["bookstore_Person"] = None, bookstore_Dvd13: "bookstore_Book" = None, bookstore_Dvd16: "bookstore_Person" = None, bookstore_Dvd20: "bookstore_Dvd" = None, bookstore_Dvd18: "bookstore_Dvd" = None):
        self.title = title
        self.bookstore_Dvd = bookstore_Dvd if bookstore_Dvd is not None else set()
        self.bookstore_Dvd13 = bookstore_Dvd13
        self.bookstore_Dvd16 = bookstore_Dvd16
        self.bookstore_Dvd20 = bookstore_Dvd20
        self.bookstore_Dvd18 = bookstore_Dvd18
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def bookstore_Dvd(self):
        return self.__bookstore_Dvd

    @bookstore_Dvd.setter
    def bookstore_Dvd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Dvd__bookstore_Dvd", None)
        self.__bookstore_Dvd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookstore_Person11"):
                    opp_val = getattr(item, "bookstore_Person11", None)
                    
                    if opp_val == self:
                        setattr(item, "bookstore_Person11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookstore_Person11"):
                    opp_val = getattr(item, "bookstore_Person11", None)
                    
                    setattr(item, "bookstore_Person11", self)
                    

    @property
    def bookstore_Dvd16(self):
        return self.__bookstore_Dvd16

    @bookstore_Dvd16.setter
    def bookstore_Dvd16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Dvd__bookstore_Dvd16", None)
        self.__bookstore_Dvd16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Person17"):
                opp_val = getattr(old_value, "bookstore_Person17", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Person17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Person17"):
                opp_val = getattr(value, "bookstore_Person17", None)
                setattr(value, "bookstore_Person17", self)

    @property
    def bookstore_Dvd18(self):
        return self.__bookstore_Dvd18

    @bookstore_Dvd18.setter
    def bookstore_Dvd18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Dvd__bookstore_Dvd18", None)
        self.__bookstore_Dvd18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Dvd20"):
                opp_val = getattr(old_value, "bookstore_Dvd20", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Dvd20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Dvd20"):
                opp_val = getattr(value, "bookstore_Dvd20", None)
                setattr(value, "bookstore_Dvd20", self)

    @property
    def bookstore_Dvd20(self):
        return self.__bookstore_Dvd20

    @bookstore_Dvd20.setter
    def bookstore_Dvd20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Dvd__bookstore_Dvd20", None)
        self.__bookstore_Dvd20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Dvd18"):
                opp_val = getattr(old_value, "bookstore_Dvd18", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Dvd18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Dvd18"):
                opp_val = getattr(value, "bookstore_Dvd18", None)
                setattr(value, "bookstore_Dvd18", self)

    @property
    def bookstore_Dvd13(self):
        return self.__bookstore_Dvd13

    @bookstore_Dvd13.setter
    def bookstore_Dvd13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Dvd__bookstore_Dvd13", None)
        self.__bookstore_Dvd13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Book14"):
                opp_val = getattr(old_value, "bookstore_Book14", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Book14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Book14"):
                opp_val = getattr(value, "bookstore_Book14", None)
                setattr(value, "bookstore_Book14", self)

class bookstore_Book(Ent):

    def __init__(self, title: str, pages: int, bookstore_Book: "bookstore_Book" = None, bookstore_Book3: "bookstore_Book" = None, bookstore_Book6: "bookstore_Person" = None, bookstore_Book14: "bookstore_Dvd" = None):
        self.title = title
        self.pages = pages
        self.bookstore_Book = bookstore_Book
        self.bookstore_Book3 = bookstore_Book3
        self.bookstore_Book6 = bookstore_Book6
        self.bookstore_Book14 = bookstore_Book14
        
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def bookstore_Book(self):
        return self.__bookstore_Book

    @bookstore_Book.setter
    def bookstore_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Book__bookstore_Book", None)
        self.__bookstore_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Book3"):
                opp_val = getattr(old_value, "bookstore_Book3", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Book3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Book3"):
                opp_val = getattr(value, "bookstore_Book3", None)
                setattr(value, "bookstore_Book3", self)

    @property
    def bookstore_Book6(self):
        return self.__bookstore_Book6

    @bookstore_Book6.setter
    def bookstore_Book6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Book__bookstore_Book6", None)
        self.__bookstore_Book6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Person7"):
                opp_val = getattr(old_value, "bookstore_Person7", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Person7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Person7"):
                opp_val = getattr(value, "bookstore_Person7", None)
                setattr(value, "bookstore_Person7", self)

    @property
    def bookstore_Book3(self):
        return self.__bookstore_Book3

    @bookstore_Book3.setter
    def bookstore_Book3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Book__bookstore_Book3", None)
        self.__bookstore_Book3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Book"):
                opp_val = getattr(old_value, "bookstore_Book", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Book"):
                opp_val = getattr(value, "bookstore_Book", None)
                setattr(value, "bookstore_Book", self)

    @property
    def bookstore_Book14(self):
        return self.__bookstore_Book14

    @bookstore_Book14.setter
    def bookstore_Book14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Book__bookstore_Book14", None)
        self.__bookstore_Book14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Dvd13"):
                opp_val = getattr(old_value, "bookstore_Dvd13", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Dvd13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Dvd13"):
                opp_val = getattr(value, "bookstore_Dvd13", None)
                setattr(value, "bookstore_Dvd13", self)

class bookstore_Cd(Ent):

    def __init__(self, albumName: str, bandArtist: str, bookstore_Cd: set["bookstore_Person"] = None):
        self.albumName = albumName
        self.bandArtist = bandArtist
        self.bookstore_Cd = bookstore_Cd if bookstore_Cd is not None else set()
        
    @property
    def bandArtist(self) -> str:
        return self.__bandArtist

    @bandArtist.setter
    def bandArtist(self, bandArtist: str):
        self.__bandArtist = bandArtist

    @property
    def albumName(self) -> str:
        return self.__albumName

    @albumName.setter
    def albumName(self, albumName: str):
        self.__albumName = albumName

    @property
    def bookstore_Cd(self):
        return self.__bookstore_Cd

    @bookstore_Cd.setter
    def bookstore_Cd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Cd__bookstore_Cd", None)
        self.__bookstore_Cd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookstore_Person22"):
                    opp_val = getattr(item, "bookstore_Person22", None)
                    
                    if opp_val == self:
                        setattr(item, "bookstore_Person22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookstore_Person22"):
                    opp_val = getattr(item, "bookstore_Person22", None)
                    
                    setattr(item, "bookstore_Person22", self)
                    

class bookstore_Person(Ent):

    def __init__(self, voornaam: str, achternaam: str, bookstore_Person: "bookstore_Person" = None, bookstore_Person1: "bookstore_Person" = None, bookstore_Person7: "bookstore_Book" = None, bookstore_Person9: "bookstore_Magazine" = None, bookstore_Person11: "bookstore_Dvd" = None, bookstore_Person17: "bookstore_Dvd" = None, bookstore_Person22: "bookstore_Cd" = None):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.bookstore_Person = bookstore_Person
        self.bookstore_Person1 = bookstore_Person1
        self.bookstore_Person7 = bookstore_Person7
        self.bookstore_Person9 = bookstore_Person9
        self.bookstore_Person11 = bookstore_Person11
        self.bookstore_Person17 = bookstore_Person17
        self.bookstore_Person22 = bookstore_Person22
        
    @property
    def achternaam(self) -> str:
        return self.__achternaam

    @achternaam.setter
    def achternaam(self, achternaam: str):
        self.__achternaam = achternaam

    @property
    def voornaam(self) -> str:
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, voornaam: str):
        self.__voornaam = voornaam

    @property
    def bookstore_Person(self):
        return self.__bookstore_Person

    @bookstore_Person.setter
    def bookstore_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Person__bookstore_Person", None)
        self.__bookstore_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Person1"):
                opp_val = getattr(old_value, "bookstore_Person1", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Person1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Person1"):
                opp_val = getattr(value, "bookstore_Person1", None)
                setattr(value, "bookstore_Person1", self)

    @property
    def bookstore_Person7(self):
        return self.__bookstore_Person7

    @bookstore_Person7.setter
    def bookstore_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Person__bookstore_Person7", None)
        self.__bookstore_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Book6"):
                opp_val = getattr(old_value, "bookstore_Book6", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Book6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Book6"):
                opp_val = getattr(value, "bookstore_Book6", None)
                setattr(value, "bookstore_Book6", self)

    @property
    def bookstore_Person11(self):
        return self.__bookstore_Person11

    @bookstore_Person11.setter
    def bookstore_Person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Person__bookstore_Person11", None)
        self.__bookstore_Person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Dvd"):
                opp_val = getattr(old_value, "bookstore_Dvd", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Dvd"):
                opp_val = getattr(value, "bookstore_Dvd", None)
                if opp_val is None:
                    setattr(value, "bookstore_Dvd", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bookstore_Person22(self):
        return self.__bookstore_Person22

    @bookstore_Person22.setter
    def bookstore_Person22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Person__bookstore_Person22", None)
        self.__bookstore_Person22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Cd"):
                opp_val = getattr(old_value, "bookstore_Cd", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Cd"):
                opp_val = getattr(value, "bookstore_Cd", None)
                if opp_val is None:
                    setattr(value, "bookstore_Cd", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bookstore_Person1(self):
        return self.__bookstore_Person1

    @bookstore_Person1.setter
    def bookstore_Person1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Person__bookstore_Person1", None)
        self.__bookstore_Person1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Person"):
                opp_val = getattr(old_value, "bookstore_Person", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Person"):
                opp_val = getattr(value, "bookstore_Person", None)
                setattr(value, "bookstore_Person", self)

    @property
    def bookstore_Person17(self):
        return self.__bookstore_Person17

    @bookstore_Person17.setter
    def bookstore_Person17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Person__bookstore_Person17", None)
        self.__bookstore_Person17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Dvd16"):
                opp_val = getattr(old_value, "bookstore_Dvd16", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Dvd16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Dvd16"):
                opp_val = getattr(value, "bookstore_Dvd16", None)
                setattr(value, "bookstore_Dvd16", self)

    @property
    def bookstore_Person9(self):
        return self.__bookstore_Person9

    @bookstore_Person9.setter
    def bookstore_Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Person__bookstore_Person9", None)
        self.__bookstore_Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Magazine"):
                opp_val = getattr(old_value, "bookstore_Magazine", None)
                if opp_val == self:
                    setattr(old_value, "bookstore_Magazine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Magazine"):
                opp_val = getattr(value, "bookstore_Magazine", None)
                setattr(value, "bookstore_Magazine", self)

class bookstore_Ent:

    def __init__(self, name: str, bookstore_Ent: "bookstore_Model" = None):
        self.name = name
        self.bookstore_Ent = bookstore_Ent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bookstore_Ent(self):
        return self.__bookstore_Ent

    @bookstore_Ent.setter
    def bookstore_Ent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookstore_Ent__bookstore_Ent", None)
        self.__bookstore_Ent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookstore_Model"):
                opp_val = getattr(old_value, "bookstore_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookstore_Model"):
                opp_val = getattr(value, "bookstore_Model", None)
                if opp_val is None:
                    setattr(value, "bookstore_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bookstore_Model:

    pass