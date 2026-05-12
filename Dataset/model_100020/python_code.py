from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PublisheredEntry:

    pass
class EditoredEntry:

    pass
class JournalEntry:

    pass
class TitledEntry:

    pass
class BIBTEXML_Author:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class AuthoredEntry:

    pass
class Entry:

    pass
class BIBTEXML_BibtexFile:

    pass
class BIBTEXML_SchoolEntry(Entry):

    def __init__(self, school: str, Entry: "BIBTEXML_BibtexFile" = None):
        self.school = school
        
        pass
    @property
    def school(self):
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school


class BIBTEXML_PublisheredEntry(Entry):

    def __init__(self, publisher: str, Entry: "BIBTEXML_BibtexFile" = None):
        self.publisher = publisher
        
        pass
    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher


class BIBTEXML_NotedEntry(Entry):

    def __init__(self, note: str, Entry: "BIBTEXML_BibtexFile" = None):
        self.note = note
        
        pass
    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


class BIBTEXML_TitledEntry(Entry):

    def __init__(self, title: str, Entry: "BIBTEXML_BibtexFile" = None):
        self.title = title
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


class BIBTEXML_JournalEntry(Entry):

    def __init__(self, journal: str, Entry: "BIBTEXML_BibtexFile" = None):
        self.journal = journal
        
        pass
    @property
    def journal(self):
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal


class BIBTEXML_DatedEntry(Entry):

    def __init__(self, year: str, month: str, Entry: "BIBTEXML_BibtexFile" = None):
        self.year = year
        self.month = month
        
        pass
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


class BIBTEXML_EditoredEntry(Entry):

    def __init__(self, editor: str, Entry: "BIBTEXML_BibtexFile" = None):
        self.editor = editor
        
        pass
    @property
    def editor(self):
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor


class BIBTEXML_InstitutionEntry(Entry):

    def __init__(self, institution: str, Entry: "BIBTEXML_BibtexFile" = None):
        self.institution = institution
        
        pass
    @property
    def institution(self):
        return self.__institution

    @institution.setter
    def institution(self, institution: str):
        self.__institution = institution


class BIBTEXML_BookTitledEntry(Entry):

    def __init__(self, booktitle: str, Entry: "BIBTEXML_BibtexFile" = None):
        self.booktitle = booktitle
        
        pass
    @property
    def booktitle(self):
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle


class Author:

    pass
class BIBTEXML_AuthoredEntry(Entry):

    pass
class BIBTEXML_Entry(ABC):

    def __init__(self, id: str, abstract: str):
        self.id = id
        self.abstract = abstract
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


class InstitutionEntry:

    pass
class BIBTEXML_Misc(Entry):

    def __init__(self, note: str, title: str, howpublished: str, month: str, year: str, BIBTEXML_Misc: set["Author"] = None, Entry: "BIBTEXML_BibtexFile" = None):
        self.note = note
        self.title = title
        self.howpublished = howpublished
        self.month = month
        self.year = year
        self.BIBTEXML_Misc = BIBTEXML_Misc if BIBTEXML_Misc is not None else set()
        
        pass
    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def howpublished(self):
        return self.__howpublished

    @howpublished.setter
    def howpublished(self, howpublished: str):
        self.__howpublished = howpublished


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def BIBTEXML_Misc(self):
        return self.__BIBTEXML_Misc

    @BIBTEXML_Misc.setter
    def BIBTEXML_Misc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BIBTEXML_Misc__BIBTEXML_Misc", None)
        self.__BIBTEXML_Misc = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author5"):
                    opp_val = getattr(item, "Author5", None)
                    
                    if opp_val == self:
                        setattr(item, "Author5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author5"):
                    opp_val = getattr(item, "Author5", None)
                    
                    setattr(item, "Author5", self)
                    

class NotedEntry:

    pass
class InProceedings:

    pass
class BIBTEXML_Conference(InProceedings):

    pass
class Proceedings:

    pass
class ThesisEntry:

    pass
class BIBTEXML_MastersThesis(ThesisEntry):

    pass
class BIBTEXML_PhdThesis(ThesisEntry):

    pass
class SchoolEntry:

    pass
class DatedEntry:

    pass
class BIBTEXML_Booklet(DatedEntry, TitledEntry):

    def __init__(self, howpublished: str, address: str, note: str, BIBTEXML_Booklet: set["Author"] = None):
        self.howpublished = howpublished
        self.address = address
        self.note = note
        self.BIBTEXML_Booklet = BIBTEXML_Booklet if BIBTEXML_Booklet is not None else set()
        
        pass
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


    @property
    def howpublished(self):
        return self.__howpublished

    @howpublished.setter
    def howpublished(self, howpublished: str):
        self.__howpublished = howpublished


    @property
    def BIBTEXML_Booklet(self):
        return self.__BIBTEXML_Booklet

    @BIBTEXML_Booklet.setter
    def BIBTEXML_Booklet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BIBTEXML_Booklet__BIBTEXML_Booklet", None)
        self.__BIBTEXML_Booklet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author3"):
                    opp_val = getattr(item, "Author3", None)
                    
                    if opp_val == self:
                        setattr(item, "Author3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author3"):
                    opp_val = getattr(item, "Author3", None)
                    
                    setattr(item, "Author3", self)
                    

class BIBTEXML_Unpublished(DatedEntry, NotedEntry, TitledEntry, AuthoredEntry):

    pass
class BIBTEXML_ThesisEntry(DatedEntry, SchoolEntry, TitledEntry, AuthoredEntry):

    def __init__(self, type: str, address: str, note: str):
        self.type = type
        self.address = address
        self.note = note
        
        pass
    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class BIBTEXML_Manual(DatedEntry, TitledEntry, AuthoredEntry):

    def __init__(self, organization: str, address: str, edition: str, note: str):
        self.organization = organization
        self.address = address
        self.edition = edition
        self.note = note
        
        pass
    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition


class BIBTEXML_Proceedings(DatedEntry, TitledEntry):

    def __init__(self, editor: str, volume: str, number: str, series: str, address: str, organization: str, publisher: str, note: str):
        self.editor = editor
        self.volume = volume
        self.number = number
        self.series = series
        self.address = address
        self.organization = organization
        self.publisher = publisher
        self.note = note
        
        pass
    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def editor(self):
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


class BIBTEXML_TechReport(DatedEntry, InstitutionEntry, TitledEntry, AuthoredEntry):

    def __init__(self, type: str, number: str, address: str, note: str):
        self.type = type
        self.number = number
        self.address = address
        self.note = note
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


class BIBTEXML_Article(DatedEntry, JournalEntry, TitledEntry, AuthoredEntry):

    def __init__(self, volume: str, number: str, pages: str, note: str):
        self.volume = volume
        self.number = number
        self.pages = pages
        self.note = note
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


class BIBTEXML_Book(PublisheredEntry, EditoredEntry, TitledEntry, DatedEntry, AuthoredEntry):

    def __init__(self, volume: str, number: str, series: str, address: str, edition: str, note: str):
        self.volume = volume
        self.number = number
        self.series = series
        self.address = address
        self.edition = edition
        self.note = note
        
        pass
    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


class BookTitledEntry:

    pass
class BIBTEXML_InProceedings(BookTitledEntry, Proceedings, AuthoredEntry):

    def __init__(self, pages: str):
        self.pages = pages
        
        pass
    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


class Book:

    pass
class BIBTEXML_InCollection(BookTitledEntry, Book):

    def __init__(self, chapter: str, type: str):
        self.chapter = chapter
        self.type = type
        
        pass
    @property
    def chapter(self):
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: str):
        self.__chapter = chapter


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class BIBTEXML_InBook(Book):

    def __init__(self, chapter: str, type: str):
        self.chapter = chapter
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def chapter(self):
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: str):
        self.__chapter = chapter

