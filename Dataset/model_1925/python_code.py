from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Book:

    pass
class bibTeX_InBook(Book):

    def __init__(self, chapter: str):
        self.chapter = chapter
        
    @property
    def chapter(self) -> str:
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: str):
        self.__chapter = chapter

class ThesisEntry:

    pass
class bibTeX_MasterThesis(ThesisEntry):

    pass
class bibTeX_PhDThesis(ThesisEntry):

    pass
class BookTitledEntry:

    pass
class bibTeX_InCollection(BookTitledEntry, Book):

    pass
class Proceedings:

    pass
class TitledEntry:

    pass
class DatedEntry:

    pass
class bibTeX_Booklet(DatedEntry):

    pass
class bibTeX_Proceedings(TitledEntry, DatedEntry):

    pass
class AuthoredEntry:

    pass
class bibTeX_InProceedings(AuthoredEntry, BookTitledEntry, Proceedings):

    pass
class bibTeX_Book(TitledEntry, AuthoredEntry, DatedEntry):

    def __init__(self, publisher: str):
        self.publisher = publisher
        
    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

class bibTeX_ThesisEntry(TitledEntry, AuthoredEntry, DatedEntry):

    def __init__(self, school: str):
        self.school = school
        
    @property
    def school(self) -> str:
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school

class bibTeX_Article(AuthoredEntry, TitledEntry, DatedEntry):

    def __init__(self, journal: str):
        self.journal = journal
        
    @property
    def journal(self) -> str:
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal

class bibTeX_Manual(TitledEntry):

    pass
class bibTeX_Unpublished(AuthoredEntry, TitledEntry):

    def __init__(self, note: str):
        self.note = note
        
    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

class bibTeX_TechReport(TitledEntry, AuthoredEntry, DatedEntry):

    pass
class bibTeX_Author:

    def __init__(self, author: str, bibTeX_Author: "bibTeX_AuthoredEntry" = None):
        self.author = author
        self.bibTeX_Author = bibTeX_Author
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def bibTeX_Author(self):
        return self.__bibTeX_Author

    @bibTeX_Author.setter
    def bibTeX_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_Author__bibTeX_Author", None)
        self.__bibTeX_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_AuthoredEntry"):
                opp_val = getattr(old_value, "bibTeX_AuthoredEntry", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_AuthoredEntry"):
                opp_val = getattr(value, "bibTeX_AuthoredEntry", None)
                if opp_val is None:
                    setattr(value, "bibTeX_AuthoredEntry", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BibTeXEntry:

    pass
class bibTeX_TitledEntry(BibTeXEntry):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class bibTeX_BookTitledEntry(BibTeXEntry):

    def __init__(self, booktitle: str):
        self.booktitle = booktitle
        
    @property
    def booktitle(self) -> str:
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle

class bibTeX_Misc(BibTeXEntry):

    pass
class bibTeX_DatedEntry(BibTeXEntry):

    def __init__(self, year: str):
        self.year = year
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

class bibTeX_AuthoredEntry(BibTeXEntry):

    pass
class bibTeX_BibTeXEntry(ABC):

    def __init__(self, theId: str, bibTeX_BibTeXEntry: "bibTeX_BibTeXFile" = None):
        self.theId = theId
        self.bibTeX_BibTeXEntry = bibTeX_BibTeXEntry
        
    @property
    def theId(self) -> str:
        return self.__theId

    @theId.setter
    def theId(self, theId: str):
        self.__theId = theId

    @property
    def bibTeX_BibTeXEntry(self):
        return self.__bibTeX_BibTeXEntry

    @bibTeX_BibTeXEntry.setter
    def bibTeX_BibTeXEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_BibTeXEntry__bibTeX_BibTeXEntry", None)
        self.__bibTeX_BibTeXEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_BibTeXFile"):
                opp_val = getattr(old_value, "bibTeX_BibTeXFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_BibTeXFile"):
                opp_val = getattr(value, "bibTeX_BibTeXFile", None)
                if opp_val is None:
                    setattr(value, "bibTeX_BibTeXFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibTeX_BibTeXFile:

    pass