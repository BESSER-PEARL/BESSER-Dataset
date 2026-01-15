from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ThesisEntry:

    pass
class bibtex_MasterThesis(ThesisEntry):

    pass
class bibtex_PhDThesis(ThesisEntry):

    pass
class Book:

    pass
class bibtex_InBook(Book):

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
class bibtex_InCollection(Book, BookTitledEntry):

    pass
class Proceedings:

    pass
class TitledEntry:

    pass
class bibtex_Manual(TitledEntry):

    pass
class DatedEntry:

    pass
class bibtex_Booklet(DatedEntry):

    pass
class bibtex_Proceedings(DatedEntry, TitledEntry):

    pass
class AuthoredEntry:

    pass
class bibtex_Book(TitledEntry, DatedEntry, AuthoredEntry):

    def __init__(self, publisher: str):
        self.publisher = publisher
        
    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

class bibtex_InProceedings(AuthoredEntry, BookTitledEntry, Proceedings):

    pass
class bibtex_ThesisEntry(TitledEntry, DatedEntry, AuthoredEntry):

    def __init__(self, school: str):
        self.school = school
        
    @property
    def school(self) -> str:
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school

class bibtex_Article(TitledEntry, DatedEntry, AuthoredEntry):

    def __init__(self, journal: str):
        self.journal = journal
        
    @property
    def journal(self) -> str:
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal

class BibTeXEntry:

    pass
class bibtex_BookTitledEntry(BibTeXEntry):

    def __init__(self, booktitle: str):
        self.booktitle = booktitle
        
    @property
    def booktitle(self) -> str:
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle

class bibtex_TitledEntry(BibTeXEntry):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class bibtex_DatedEntry(BibTeXEntry):

    def __init__(self, year: int):
        self.year = year
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

class bibtex_Misc(BibTeXEntry):

    pass
class bibtex_AuthoredEntry(BibTeXEntry):

    pass
class bibtex_Unpublished(TitledEntry, AuthoredEntry):

    def __init__(self, note: str):
        self.note = note
        
    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

class bibtex_TechReport(DatedEntry, AuthoredEntry, TitledEntry):

    pass
class bibtex_BibTeXEntry(ABC):

    def __init__(self, id: str, bibtex_BibTeXEntry: "bibtex_BibTeXFile" = None):
        self.id = id
        self.bibtex_BibTeXEntry = bibtex_BibTeXEntry
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bibtex_BibTeXEntry(self):
        return self.__bibtex_BibTeXEntry

    @bibtex_BibTeXEntry.setter
    def bibtex_BibTeXEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_BibTeXEntry__bibtex_BibTeXEntry", None)
        self.__bibtex_BibTeXEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_BibTeXFile"):
                opp_val = getattr(old_value, "bibtex_BibTeXFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_BibTeXFile"):
                opp_val = getattr(value, "bibtex_BibTeXFile", None)
                if opp_val is None:
                    setattr(value, "bibtex_BibTeXFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibtex_BibTeXFile:

    pass
class bibtex_Author:

    def __init__(self, author: str, bibtex_Author: "bibtex_AuthoredEntry" = None):
        self.author = author
        self.bibtex_Author = bibtex_Author
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def bibtex_Author(self):
        return self.__bibtex_Author

    @bibtex_Author.setter
    def bibtex_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author", None)
        self.__bibtex_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_AuthoredEntry"):
                opp_val = getattr(old_value, "bibtex_AuthoredEntry", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_AuthoredEntry"):
                opp_val = getattr(value, "bibtex_AuthoredEntry", None)
                if opp_val is None:
                    setattr(value, "bibtex_AuthoredEntry", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
