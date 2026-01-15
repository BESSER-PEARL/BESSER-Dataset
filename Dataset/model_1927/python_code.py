from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ThesisEntry:

    pass
class BibTeX_PhDThesis(ThesisEntry):

    pass
class Book:

    pass
class BibTeX_InBook(Book):

    def __init__(self, chapter: int):
        self.chapter = chapter
        
    @property
    def chapter(self) -> int:
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: int):
        self.__chapter = chapter

class BookTitledEntry:

    pass
class BibTeX_InCollection(Book, BookTitledEntry):

    pass
class Proceedings:

    pass
class BibTeX_MasterThesis(ThesisEntry):

    pass
class TitledEntry:

    pass
class DatedEntry:

    pass
class BibTeX_Booklet(DatedEntry):

    pass
class BibTeX_Proceedings(TitledEntry, DatedEntry):

    pass
class AuthoredEntry:

    pass
class BibTeX_Unpublished(TitledEntry, AuthoredEntry):

    def __init__(self, note: str):
        self.note = note
        
    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

class BibTeX_ThesisEntry(TitledEntry, DatedEntry, AuthoredEntry):

    def __init__(self, school: str):
        self.school = school
        
    @property
    def school(self) -> str:
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school

class BibTeX_InProceedings(AuthoredEntry, Proceedings, BookTitledEntry):

    pass
class BibTeX_TechReport(AuthoredEntry, DatedEntry, TitledEntry):

    pass
class BibTeX_Book(AuthoredEntry, DatedEntry, TitledEntry):

    def __init__(self, publisher: str):
        self.publisher = publisher
        
    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

class BibTeX_Article(TitledEntry, DatedEntry, AuthoredEntry):

    def __init__(self, journal: str):
        self.journal = journal
        
    @property
    def journal(self) -> str:
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal

class BibTeX_Manual(TitledEntry):

    pass
class BibTeX_BibTeXEntry(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class BibTeX_Author:

    def __init__(self, author: str):
        self.author = author
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

class BibTeXEntry:

    pass
class BibTeX_DatedEntry(BibTeXEntry):

    def __init__(self, year: str, BibTeXEntry: "BibTeX_BibTeXFile"):
        self.year = year
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

class BibTeX_AuthoredEntry(BibTeXEntry):

    pass
class BibTeX_TitledEntry(BibTeXEntry):

    def __init__(self, title: str, BibTeXEntry: "BibTeX_BibTeXFile"):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class BibTeX_BookTitledEntry(BibTeXEntry):

    def __init__(self, booktitle: str, BibTeXEntry: "BibTeX_BibTeXFile"):
        self.booktitle = booktitle
        
    @property
    def booktitle(self) -> str:
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle

class BibTeX_Misc(BibTeXEntry):

    pass
class BibTeX_BibTeXFile:

    pass
class Author:

    pass