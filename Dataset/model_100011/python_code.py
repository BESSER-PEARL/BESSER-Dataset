from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class bibtex_Author:

    def __init__(self, name: str, surname: str, bibtex_Author: set["bibtex_AuthoredEntry"] = None):
        self.name = name
        self.surname = surname
        self.bibtex_Author = bibtex_Author if bibtex_Author is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname


    @property
    def bibtex_Author(self):
        return self.__bibtex_Author

    @bibtex_Author.setter
    def bibtex_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author", None)
        self.__bibtex_Author = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtex_AuthoredEntry"):
                    opp_val = getattr(item, "bibtex_AuthoredEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtex_AuthoredEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtex_AuthoredEntry"):
                    opp_val = getattr(item, "bibtex_AuthoredEntry", None)
                    
                    setattr(item, "bibtex_AuthoredEntry", self)
                    

class MonthEntry:

    pass
class DatedEntry:

    pass
class AuthoredEntry:

    pass
class Entries:

    pass
class bibtex_MonthEntry(Entries):

    def __init__(self, month: str):
        self.month = month
        
        pass
    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


class bibtex_AuthoredEntry(Entries):

    pass
class bibtex_DatedEntry(Entries):

    def __init__(self, year: int):
        self.year = year
        
        pass
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year


class bibtex_Book(DatedEntry, Entries, MonthEntry, AuthoredEntry):

    def __init__(self, publisher: str, volume: int, series: int, address: str, edition: int):
        self.publisher = publisher
        self.volume = volume
        self.series = series
        self.address = address
        self.edition = edition
        
        pass
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: int):
        self.__volume = volume


    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition: int):
        self.__edition = edition


    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: int):
        self.__series = series


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher


class bibtex_Bibtex:

    pass
class bibtex_Entries(ABC):

    pass
class bibtex_Article(DatedEntry, Entries, MonthEntry, AuthoredEntry):

    def __init__(self, journal: str, volume: int, number: int, pages: int, note: str):
        self.journal = journal
        self.volume = volume
        self.number = number
        self.pages = pages
        self.note = note
        
        pass
    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages


    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: int):
        self.__volume = volume


    @property
    def journal(self):
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

