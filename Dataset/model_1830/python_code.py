from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TrgSect1:

    pass
class TrgTitledElement:

    pass
class jointPackage_TrgArticle(TrgTitledElement):

    pass
class jointPackage_TrgTitledElement(ABC):

    def __init__(self, title: str):
        self.title = title
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


class TrgArticle:

    pass
class jointPackage_TrgBook:

    pass
class TrgBook:

    pass
class jointPackage_TrgDocBook:

    pass
class jointPackage_TrgPara:

    def __init__(self, content: str, paras: "TrgSection" = None):
        self.content = content
        self.paras = paras
        
        pass
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


    @property
    def paras(self):
        return self.__paras

    @paras.setter
    def paras(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_TrgPara__paras", None)
        self.__paras = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgSection"):
                opp_val = getattr(old_value, "TrgSection", None)
                if opp_val == self:
                    setattr(old_value, "TrgSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgSection"):
                opp_val = getattr(value, "TrgSection", None)
                setattr(value, "TrgSection", self)

class TrgSect2:

    pass
class TrgSection:

    pass
class jointPackage_TrgSect2(TrgSection):

    pass
class jointPackage_TrgSect1(TrgSection):

    pass
class TrgPara:

    pass
class jointPackage_TrgSection(TrgTitledElement):

    pass
class SrcBookTitledEntry:

    pass
class SrcProceedings:

    pass
class SrcAuthor:

    pass
class jointPackage_SrcBibTeXEntry(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class jointPackage_SrcAuthor:

    def __init__(self, author: str):
        self.author = author
        
        pass
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


class SrcThesisEntry:

    pass
class jointPackage_SrcMasterThesis(SrcThesisEntry):

    pass
class jointPackage_SrcPhDThesis(SrcThesisEntry):

    pass
class SrcBook:

    pass
class jointPackage_SrcInBook(SrcBook):

    def __init__(self, chapter: int):
        self.chapter = chapter
        
        pass
    @property
    def chapter(self):
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: int):
        self.__chapter = chapter


class jointPackage_SrcInCollection(SrcBookTitledEntry, SrcBook):

    pass
class SrcTitledEntry:

    pass
class jointPackage_SrcManual(SrcTitledEntry):

    pass
class SrcDatedEntry:

    pass
class jointPackage_SrcBooklet(SrcDatedEntry):

    pass
class jointPackage_SrcProceedings(SrcTitledEntry, SrcDatedEntry):

    pass
class SrcAuthoredEntry:

    pass
class jointPackage_SrcTechReport(SrcDatedEntry, SrcAuthoredEntry, SrcTitledEntry):

    pass
class jointPackage_SrcInProceedings(SrcAuthoredEntry, SrcBookTitledEntry, SrcProceedings):

    pass
class jointPackage_SrcUnpublished(SrcTitledEntry, SrcAuthoredEntry):

    def __init__(self, note: str):
        self.note = note
        
        pass
    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


class jointPackage_SrcThesisEntry(SrcTitledEntry, SrcDatedEntry, SrcAuthoredEntry):

    def __init__(self, school: str):
        self.school = school
        
        pass
    @property
    def school(self):
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school


class jointPackage_SrcBook(SrcTitledEntry, SrcAuthoredEntry, SrcDatedEntry):

    def __init__(self, publisher: str):
        self.publisher = publisher
        
        pass
    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher


class jointPackage_SrcArticle(SrcDatedEntry, SrcAuthoredEntry, SrcTitledEntry):

    def __init__(self, journal: str):
        self.journal = journal
        
        pass
    @property
    def journal(self):
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal


class SrcBibTeXEntry:

    pass
class jointPackage_SrcDatedEntry(SrcBibTeXEntry):

    def __init__(self, year: str, SrcBibTeXEntry: "jointPackage_SrcBibTeXFile" = None):
        self.year = year
        
        pass
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


class jointPackage_SrcBookTitledEntry(SrcBibTeXEntry):

    def __init__(self, booktitle: str, SrcBibTeXEntry: "jointPackage_SrcBibTeXFile" = None):
        self.booktitle = booktitle
        
        pass
    @property
    def booktitle(self):
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle


class jointPackage_SrcTitledEntry(SrcBibTeXEntry):

    def __init__(self, title: str, SrcBibTeXEntry: "jointPackage_SrcBibTeXFile" = None):
        self.title = title
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


class jointPackage_SrcAuthoredEntry(SrcBibTeXEntry):

    pass
class jointPackage_SrcMisc(SrcBibTeXEntry):

    pass
class jointPackage_SrcBibTeXFile:

    pass
class TrgDocBook:

    pass
class SrcMasterThesis:

    pass
class jointPackage_JointMM:

    pass