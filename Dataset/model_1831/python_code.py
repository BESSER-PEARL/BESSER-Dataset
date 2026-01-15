from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TrgSect1:

    pass
class jointPackage_BibTeX2DocBook_TrgPara:

    def __init__(self, content: str, 011: "TrgSection" = None):
        self.content = content
        self.011 = 011
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def 011(self):
        return self.__011

    @011.setter
    def 011(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_BibTeX2DocBook_TrgPara__011", None)
        self.__011 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#12"):
                opp_val = getattr(old_value, "#12", None)
                if opp_val == self:
                    setattr(old_value, "#12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#12"):
                opp_val = getattr(value, "#12", None)
                setattr(value, "#12", self)

class TrgSect2:

    pass
class TrgSection:

    pass
class jointPackage_BibTeX2DocBook_TrgSect2(TrgSection):

    pass
class jointPackage_BibTeX2DocBook_TrgSect1(TrgSection):

    pass
class TrgPara:

    pass
class TrgTitledElement:

    pass
class jointPackage_BibTeX2DocBook_TrgSection(TrgTitledElement):

    pass
class jointPackage_BibTeX2DocBook_TrgArticle(TrgTitledElement):

    pass
class jointPackage_BibTeX2DocBook_TrgTitledElement(ABC):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class TrgArticle:

    pass
class jointPackage_BibTeX2DocBook_TrgBook:

    pass
class TrgBook:

    pass
class jointPackage_BibTeX2DocBook_TrgDocBook:

    pass
class SrcBookTitledEntry:

    pass
class SrcProceedings:

    pass
class SrcAuthor:

    pass
class jointPackage_BibTeX2DocBook_SrcBibTeXEntry(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class jointPackage_BibTeX2DocBook_SrcAuthor:

    def __init__(self, author: str):
        self.author = author
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

class SrcThesisEntry:

    pass
class jointPackage_BibTeX2DocBook_SrcMasterThesis(SrcThesisEntry):

    pass
class jointPackage_BibTeX2DocBook_SrcPhDThesis(SrcThesisEntry):

    pass
class SrcBook:

    pass
class jointPackage_BibTeX2DocBook_SrcInBook(SrcBook):

    def __init__(self, chapter: int):
        self.chapter = chapter
        
    @property
    def chapter(self) -> int:
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: int):
        self.__chapter = chapter

class jointPackage_BibTeX2DocBook_SrcInCollection(SrcBookTitledEntry, SrcBook):

    pass
class TrgDocBook:

    pass
class SrcTitledEntry:

    pass
class jointPackage_BibTeX2DocBook_SrcManual(SrcTitledEntry):

    pass
class SrcDatedEntry:

    pass
class jointPackage_BibTeX2DocBook_SrcBooklet(SrcDatedEntry):

    pass
class jointPackage_BibTeX2DocBook_SrcProceedings(SrcTitledEntry, SrcDatedEntry):

    pass
class SrcAuthoredEntry:

    pass
class jointPackage_BibTeX2DocBook_SrcInProceedings(SrcBookTitledEntry, SrcProceedings, SrcAuthoredEntry):

    pass
class jointPackage_BibTeX2DocBook_SrcTechReport(SrcTitledEntry, SrcDatedEntry, SrcAuthoredEntry):

    pass
class jointPackage_BibTeX2DocBook_SrcBook(SrcTitledEntry, SrcDatedEntry, SrcAuthoredEntry):

    def __init__(self, publisher: str):
        self.publisher = publisher
        
    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

class jointPackage_BibTeX2DocBook_SrcUnpublished(SrcTitledEntry, SrcAuthoredEntry):

    def __init__(self, note: str):
        self.note = note
        
    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

class jointPackage_BibTeX2DocBook_SrcThesisEntry(SrcTitledEntry, SrcDatedEntry, SrcAuthoredEntry):

    def __init__(self, school: str):
        self.school = school
        
    @property
    def school(self) -> str:
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school

class jointPackage_BibTeX2DocBook_SrcArticle(SrcTitledEntry, SrcDatedEntry, SrcAuthoredEntry):

    def __init__(self, journal: str):
        self.journal = journal
        
    @property
    def journal(self) -> str:
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal

class SrcBibTeXEntry:

    pass
class jointPackage_BibTeX2DocBook_SrcTitledEntry(SrcBibTeXEntry):

    def __init__(self, title: str, SrcBibTeXEntry: "jointPackage_BibTeX2DocBook_SrcBibTeXFile"):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class jointPackage_BibTeX2DocBook_SrcBookTitledEntry(SrcBibTeXEntry):

    def __init__(self, booktitle: str, SrcBibTeXEntry: "jointPackage_BibTeX2DocBook_SrcBibTeXFile"):
        self.booktitle = booktitle
        
    @property
    def booktitle(self) -> str:
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle

class jointPackage_BibTeX2DocBook_SrcMisc(SrcBibTeXEntry):

    pass
class jointPackage_BibTeX2DocBook_SrcAuthoredEntry(SrcBibTeXEntry):

    pass
class jointPackage_BibTeX2DocBook_SrcDatedEntry(SrcBibTeXEntry):

    def __init__(self, year: str, SrcBibTeXEntry: "jointPackage_BibTeX2DocBook_SrcBibTeXFile"):
        self.year = year
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

class jointPackage_BibTeX2DocBook_SrcBibTeXFile:

    pass
class SrcMasterThesis:

    pass
class jointPackage_BibTeX2DocBook_JointMM:

    pass