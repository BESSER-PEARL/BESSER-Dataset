from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ThesisEntry:

    pass
class BibTeX_MasterThesis(ThesisEntry):

    pass
class BibTeX_PhDThesis(ThesisEntry):

    pass
class Book:

    pass
class BibTeX_InBook(Book):

    def __init__(self, chapter: str):
        self.chapter = chapter
        
        pass
    @property
    def chapter(self):
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: str):
        self.__chapter = chapter


class BookTitledEntry:

    pass
class BibTeX_InCollection(Book, BookTitledEntry):

    pass
class Proceedings:

    pass
class TitledEntry:

    pass
class BibTeX_Manual(TitledEntry):

    pass
class DatedEntry:

    pass
class BibTeX_Booklet(DatedEntry):

    pass
class BibTeX_Proceedings(DatedEntry, TitledEntry):

    pass
class AuthoredEntry:

    pass
class BibTeX_Unpublished(AuthoredEntry, TitledEntry):

    def __init__(self, note: str):
        self.note = note
        
        pass
    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


class BibTeX_TechReport(DatedEntry, TitledEntry, AuthoredEntry):

    pass
class BibTeX_ThesisEntry(DatedEntry, TitledEntry, AuthoredEntry):

    def __init__(self, school: str):
        self.school = school
        
        pass
    @property
    def school(self):
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school


class BibTeX_InProceedings(Proceedings, BookTitledEntry, AuthoredEntry):

    pass
class BibTeX_Article(DatedEntry, TitledEntry, AuthoredEntry):

    def __init__(self, journal: str):
        self.journal = journal
        
        pass
    @property
    def journal(self):
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal


class BibTeX_Book(DatedEntry, TitledEntry, AuthoredEntry):

    def __init__(self, publisher: str):
        self.publisher = publisher
        
        pass
    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher


class Author:

    pass
class BibTeX_BibTeXEntry(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class BibTeX_Author:

    def __init__(self, author: str):
        self.author = author
        
        pass
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


class BibTeXEntry:

    pass
class BibTeX_BookTitledEntry(BibTeXEntry):

    def __init__(self, booktitle: str, BibTeXEntry: "BibTeX_BibTeXFile" = None):
        self.booktitle = booktitle
        
        pass
    @property
    def booktitle(self):
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle


class BibTeX_TitledEntry(BibTeXEntry):

    def __init__(self, title: str, BibTeXEntry: "BibTeX_BibTeXFile" = None):
        self.title = title
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


class BibTeX_Misc(BibTeXEntry):

    pass
class BibTeX_AuthoredEntry(BibTeXEntry):

    pass
class BibTeX_DatedEntry(BibTeXEntry):

    def __init__(self, year: str, BibTeXEntry: "BibTeX_BibTeXFile" = None):
        self.year = year
        
        pass
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


class BibTeX_BibTeXFile:

    pass