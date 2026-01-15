from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MonthStringType(Enum):
    Jan = "Jan"
    Feb = "Feb"
    Mar = "Mar"
    Apr = "Apr"
    May = "May"
    Jun = "Jun"
    Jul = "Jul"
    Aug = "Aug"
    Sep = "Sep"
    Oct = "Oct"
    Nov = "Nov"
    Dec = "Dec"


############################################
# Definition of Classes
############################################

class bibtexml_FileType:

    pass
class bibtexml_EStringToStringMapEntry:

    pass
class bibtexml_DocumentRoot:

    def __init__(self, mixed: str, address: str, annote: str, author: str, booktitle: str, chapter: str, edition: str, editor: str, crossref: str, doi: str, institution: str, howpublished: str, key: str, journal: str, note: str, number: str, organization: str, pages: str, month: str, publisher: str, school: str, series: str, type: str, url: str, volume: str, title: str, year: str, bibtexml_DocumentRoot: set["bibtexml_EStringToStringMapEntry"] = None, bibtexml_DocumentRoot32: set["bibtexml_ArticleType"] = None, bibtexml_DocumentRoot29: set["bibtexml_EStringToStringMapEntry"] = None, bibtexml_DocumentRoot38: set["bibtexml_BookletType"] = None, bibtexml_DocumentRoot41: set["bibtexml_ConferenceType"] = None, bibtexml_DocumentRoot35: set["bibtexml_BookType"] = None, bibtexml_DocumentRoot44: set["bibtexml_BibTeXMLEntryType"] = None, bibtexml_DocumentRoot48: set["bibtexml_InbookType"] = None, bibtexml_DocumentRoot51: set["bibtexml_IncollectionType"] = None, bibtexml_DocumentRoot54: set["bibtexml_InproceedingsType"] = None, bibtexml_DocumentRoot46: set["bibtexml_FileType"] = None, bibtexml_DocumentRoot57: set["bibtexml_ManualType"] = None, bibtexml_DocumentRoot60: set["bibtexml_MastersthesisType"] = None, bibtexml_DocumentRoot63: set["bibtexml_MiscType"] = None, bibtexml_DocumentRoot66: set["bibtexml_PhdthesisType"] = None, bibtexml_DocumentRoot69: set["bibtexml_ProceedingsType"] = None, bibtexml_DocumentRoot75: set["bibtexml_UnpublishedType"] = None, bibtexml_DocumentRoot72: set["bibtexml_TechreportType"] = None):
        self.mixed = mixed
        self.address = address
        self.annote = annote
        self.author = author
        self.booktitle = booktitle
        self.chapter = chapter
        self.edition = edition
        self.editor = editor
        self.crossref = crossref
        self.doi = doi
        self.institution = institution
        self.howpublished = howpublished
        self.key = key
        self.journal = journal
        self.note = note
        self.number = number
        self.organization = organization
        self.pages = pages
        self.month = month
        self.publisher = publisher
        self.school = school
        self.series = series
        self.type = type
        self.url = url
        self.volume = volume
        self.title = title
        self.year = year
        self.bibtexml_DocumentRoot = bibtexml_DocumentRoot if bibtexml_DocumentRoot is not None else set()
        self.bibtexml_DocumentRoot32 = bibtexml_DocumentRoot32 if bibtexml_DocumentRoot32 is not None else set()
        self.bibtexml_DocumentRoot29 = bibtexml_DocumentRoot29 if bibtexml_DocumentRoot29 is not None else set()
        self.bibtexml_DocumentRoot38 = bibtexml_DocumentRoot38 if bibtexml_DocumentRoot38 is not None else set()
        self.bibtexml_DocumentRoot41 = bibtexml_DocumentRoot41 if bibtexml_DocumentRoot41 is not None else set()
        self.bibtexml_DocumentRoot35 = bibtexml_DocumentRoot35 if bibtexml_DocumentRoot35 is not None else set()
        self.bibtexml_DocumentRoot44 = bibtexml_DocumentRoot44 if bibtexml_DocumentRoot44 is not None else set()
        self.bibtexml_DocumentRoot48 = bibtexml_DocumentRoot48 if bibtexml_DocumentRoot48 is not None else set()
        self.bibtexml_DocumentRoot51 = bibtexml_DocumentRoot51 if bibtexml_DocumentRoot51 is not None else set()
        self.bibtexml_DocumentRoot54 = bibtexml_DocumentRoot54 if bibtexml_DocumentRoot54 is not None else set()
        self.bibtexml_DocumentRoot46 = bibtexml_DocumentRoot46 if bibtexml_DocumentRoot46 is not None else set()
        self.bibtexml_DocumentRoot57 = bibtexml_DocumentRoot57 if bibtexml_DocumentRoot57 is not None else set()
        self.bibtexml_DocumentRoot60 = bibtexml_DocumentRoot60 if bibtexml_DocumentRoot60 is not None else set()
        self.bibtexml_DocumentRoot63 = bibtexml_DocumentRoot63 if bibtexml_DocumentRoot63 is not None else set()
        self.bibtexml_DocumentRoot66 = bibtexml_DocumentRoot66 if bibtexml_DocumentRoot66 is not None else set()
        self.bibtexml_DocumentRoot69 = bibtexml_DocumentRoot69 if bibtexml_DocumentRoot69 is not None else set()
        self.bibtexml_DocumentRoot75 = bibtexml_DocumentRoot75 if bibtexml_DocumentRoot75 is not None else set()
        self.bibtexml_DocumentRoot72 = bibtexml_DocumentRoot72 if bibtexml_DocumentRoot72 is not None else set()
        
    @property
    def edition(self) -> str:
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition

    @property
    def school(self) -> str:
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school

    @property
    def journal(self) -> str:
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def howpublished(self) -> str:
        return self.__howpublished

    @howpublished.setter
    def howpublished(self, howpublished: str):
        self.__howpublished = howpublished

    @property
    def chapter(self) -> str:
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: str):
        self.__chapter = chapter

    @property
    def annote(self) -> str:
        return self.__annote

    @annote.setter
    def annote(self, annote: str):
        self.__annote = annote

    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def institution(self) -> str:
        return self.__institution

    @institution.setter
    def institution(self, institution: str):
        self.__institution = institution

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def booktitle(self) -> str:
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def editor(self) -> str:
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def series(self) -> str:
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series

    @property
    def bibtexml_DocumentRoot35(self):
        return self.__bibtexml_DocumentRoot35

    @bibtexml_DocumentRoot35.setter
    def bibtexml_DocumentRoot35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot35", None)
        self.__bibtexml_DocumentRoot35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_BookType36"):
                    opp_val = getattr(item, "bibtexml_BookType36", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_BookType36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_BookType36"):
                    opp_val = getattr(item, "bibtexml_BookType36", None)
                    
                    setattr(item, "bibtexml_BookType36", self)
                    

    @property
    def bibtexml_DocumentRoot51(self):
        return self.__bibtexml_DocumentRoot51

    @bibtexml_DocumentRoot51.setter
    def bibtexml_DocumentRoot51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot51", None)
        self.__bibtexml_DocumentRoot51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_IncollectionType52"):
                    opp_val = getattr(item, "bibtexml_IncollectionType52", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_IncollectionType52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_IncollectionType52"):
                    opp_val = getattr(item, "bibtexml_IncollectionType52", None)
                    
                    setattr(item, "bibtexml_IncollectionType52", self)
                    

    @property
    def bibtexml_DocumentRoot72(self):
        return self.__bibtexml_DocumentRoot72

    @bibtexml_DocumentRoot72.setter
    def bibtexml_DocumentRoot72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot72", None)
        self.__bibtexml_DocumentRoot72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_TechreportType73"):
                    opp_val = getattr(item, "bibtexml_TechreportType73", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_TechreportType73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_TechreportType73"):
                    opp_val = getattr(item, "bibtexml_TechreportType73", None)
                    
                    setattr(item, "bibtexml_TechreportType73", self)
                    

    @property
    def bibtexml_DocumentRoot29(self):
        return self.__bibtexml_DocumentRoot29

    @bibtexml_DocumentRoot29.setter
    def bibtexml_DocumentRoot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot29", None)
        self.__bibtexml_DocumentRoot29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_EStringToStringMapEntry30"):
                    opp_val = getattr(item, "bibtexml_EStringToStringMapEntry30", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_EStringToStringMapEntry30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_EStringToStringMapEntry30"):
                    opp_val = getattr(item, "bibtexml_EStringToStringMapEntry30", None)
                    
                    setattr(item, "bibtexml_EStringToStringMapEntry30", self)
                    

    @property
    def bibtexml_DocumentRoot41(self):
        return self.__bibtexml_DocumentRoot41

    @bibtexml_DocumentRoot41.setter
    def bibtexml_DocumentRoot41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot41", None)
        self.__bibtexml_DocumentRoot41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_ConferenceType42"):
                    opp_val = getattr(item, "bibtexml_ConferenceType42", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_ConferenceType42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_ConferenceType42"):
                    opp_val = getattr(item, "bibtexml_ConferenceType42", None)
                    
                    setattr(item, "bibtexml_ConferenceType42", self)
                    

    @property
    def bibtexml_DocumentRoot(self):
        return self.__bibtexml_DocumentRoot

    @bibtexml_DocumentRoot.setter
    def bibtexml_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot", None)
        self.__bibtexml_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_EStringToStringMapEntry"):
                    opp_val = getattr(item, "bibtexml_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_EStringToStringMapEntry"):
                    opp_val = getattr(item, "bibtexml_EStringToStringMapEntry", None)
                    
                    setattr(item, "bibtexml_EStringToStringMapEntry", self)
                    

    @property
    def bibtexml_DocumentRoot38(self):
        return self.__bibtexml_DocumentRoot38

    @bibtexml_DocumentRoot38.setter
    def bibtexml_DocumentRoot38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot38", None)
        self.__bibtexml_DocumentRoot38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_BookletType39"):
                    opp_val = getattr(item, "bibtexml_BookletType39", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_BookletType39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_BookletType39"):
                    opp_val = getattr(item, "bibtexml_BookletType39", None)
                    
                    setattr(item, "bibtexml_BookletType39", self)
                    

    @property
    def bibtexml_DocumentRoot54(self):
        return self.__bibtexml_DocumentRoot54

    @bibtexml_DocumentRoot54.setter
    def bibtexml_DocumentRoot54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot54", None)
        self.__bibtexml_DocumentRoot54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_InproceedingsType55"):
                    opp_val = getattr(item, "bibtexml_InproceedingsType55", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_InproceedingsType55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_InproceedingsType55"):
                    opp_val = getattr(item, "bibtexml_InproceedingsType55", None)
                    
                    setattr(item, "bibtexml_InproceedingsType55", self)
                    

    @property
    def bibtexml_DocumentRoot75(self):
        return self.__bibtexml_DocumentRoot75

    @bibtexml_DocumentRoot75.setter
    def bibtexml_DocumentRoot75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot75", None)
        self.__bibtexml_DocumentRoot75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_UnpublishedType76"):
                    opp_val = getattr(item, "bibtexml_UnpublishedType76", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_UnpublishedType76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_UnpublishedType76"):
                    opp_val = getattr(item, "bibtexml_UnpublishedType76", None)
                    
                    setattr(item, "bibtexml_UnpublishedType76", self)
                    

    @property
    def bibtexml_DocumentRoot63(self):
        return self.__bibtexml_DocumentRoot63

    @bibtexml_DocumentRoot63.setter
    def bibtexml_DocumentRoot63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot63", None)
        self.__bibtexml_DocumentRoot63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_MiscType64"):
                    opp_val = getattr(item, "bibtexml_MiscType64", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_MiscType64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_MiscType64"):
                    opp_val = getattr(item, "bibtexml_MiscType64", None)
                    
                    setattr(item, "bibtexml_MiscType64", self)
                    

    @property
    def bibtexml_DocumentRoot48(self):
        return self.__bibtexml_DocumentRoot48

    @bibtexml_DocumentRoot48.setter
    def bibtexml_DocumentRoot48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot48", None)
        self.__bibtexml_DocumentRoot48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_InbookType49"):
                    opp_val = getattr(item, "bibtexml_InbookType49", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_InbookType49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_InbookType49"):
                    opp_val = getattr(item, "bibtexml_InbookType49", None)
                    
                    setattr(item, "bibtexml_InbookType49", self)
                    

    @property
    def bibtexml_DocumentRoot69(self):
        return self.__bibtexml_DocumentRoot69

    @bibtexml_DocumentRoot69.setter
    def bibtexml_DocumentRoot69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot69", None)
        self.__bibtexml_DocumentRoot69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_ProceedingsType70"):
                    opp_val = getattr(item, "bibtexml_ProceedingsType70", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_ProceedingsType70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_ProceedingsType70"):
                    opp_val = getattr(item, "bibtexml_ProceedingsType70", None)
                    
                    setattr(item, "bibtexml_ProceedingsType70", self)
                    

    @property
    def bibtexml_DocumentRoot57(self):
        return self.__bibtexml_DocumentRoot57

    @bibtexml_DocumentRoot57.setter
    def bibtexml_DocumentRoot57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot57", None)
        self.__bibtexml_DocumentRoot57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_ManualType58"):
                    opp_val = getattr(item, "bibtexml_ManualType58", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_ManualType58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_ManualType58"):
                    opp_val = getattr(item, "bibtexml_ManualType58", None)
                    
                    setattr(item, "bibtexml_ManualType58", self)
                    

    @property
    def bibtexml_DocumentRoot46(self):
        return self.__bibtexml_DocumentRoot46

    @bibtexml_DocumentRoot46.setter
    def bibtexml_DocumentRoot46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot46", None)
        self.__bibtexml_DocumentRoot46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_FileType"):
                    opp_val = getattr(item, "bibtexml_FileType", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_FileType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_FileType"):
                    opp_val = getattr(item, "bibtexml_FileType", None)
                    
                    setattr(item, "bibtexml_FileType", self)
                    

    @property
    def bibtexml_DocumentRoot60(self):
        return self.__bibtexml_DocumentRoot60

    @bibtexml_DocumentRoot60.setter
    def bibtexml_DocumentRoot60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot60", None)
        self.__bibtexml_DocumentRoot60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_MastersthesisType61"):
                    opp_val = getattr(item, "bibtexml_MastersthesisType61", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_MastersthesisType61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_MastersthesisType61"):
                    opp_val = getattr(item, "bibtexml_MastersthesisType61", None)
                    
                    setattr(item, "bibtexml_MastersthesisType61", self)
                    

    @property
    def bibtexml_DocumentRoot44(self):
        return self.__bibtexml_DocumentRoot44

    @bibtexml_DocumentRoot44.setter
    def bibtexml_DocumentRoot44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot44", None)
        self.__bibtexml_DocumentRoot44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_BibTeXMLEntryType"):
                    opp_val = getattr(item, "bibtexml_BibTeXMLEntryType", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_BibTeXMLEntryType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_BibTeXMLEntryType"):
                    opp_val = getattr(item, "bibtexml_BibTeXMLEntryType", None)
                    
                    setattr(item, "bibtexml_BibTeXMLEntryType", self)
                    

    @property
    def bibtexml_DocumentRoot32(self):
        return self.__bibtexml_DocumentRoot32

    @bibtexml_DocumentRoot32.setter
    def bibtexml_DocumentRoot32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot32", None)
        self.__bibtexml_DocumentRoot32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_ArticleType33"):
                    opp_val = getattr(item, "bibtexml_ArticleType33", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_ArticleType33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_ArticleType33"):
                    opp_val = getattr(item, "bibtexml_ArticleType33", None)
                    
                    setattr(item, "bibtexml_ArticleType33", self)
                    

    @property
    def bibtexml_DocumentRoot66(self):
        return self.__bibtexml_DocumentRoot66

    @bibtexml_DocumentRoot66.setter
    def bibtexml_DocumentRoot66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_DocumentRoot__bibtexml_DocumentRoot66", None)
        self.__bibtexml_DocumentRoot66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bibtexml_PhdthesisType67"):
                    opp_val = getattr(item, "bibtexml_PhdthesisType67", None)
                    
                    if opp_val == self:
                        setattr(item, "bibtexml_PhdthesisType67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bibtexml_PhdthesisType67"):
                    opp_val = getattr(item, "bibtexml_PhdthesisType67", None)
                    
                    setattr(item, "bibtexml_PhdthesisType67", self)
                    

class BibTeXMLEntriesClass:

    pass
class bibtexml_BibTeXMLEntryType(BibTeXMLEntriesClass):

    def __init__(self, id: str, bibtexml_BibTeXMLEntryType: "bibtexml_DocumentRoot" = None, bibtexml_BibTeXMLEntryType79: "bibtexml_FileType" = None):
        self.id = id
        self.bibtexml_BibTeXMLEntryType = bibtexml_BibTeXMLEntryType
        self.bibtexml_BibTeXMLEntryType79 = bibtexml_BibTeXMLEntryType79
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bibtexml_BibTeXMLEntryType79(self):
        return self.__bibtexml_BibTeXMLEntryType79

    @bibtexml_BibTeXMLEntryType79.setter
    def bibtexml_BibTeXMLEntryType79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_BibTeXMLEntryType__bibtexml_BibTeXMLEntryType79", None)
        self.__bibtexml_BibTeXMLEntryType79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_FileType78"):
                opp_val = getattr(old_value, "bibtexml_FileType78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_FileType78"):
                opp_val = getattr(value, "bibtexml_FileType78", None)
                if opp_val is None:
                    setattr(value, "bibtexml_FileType78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bibtexml_BibTeXMLEntryType(self):
        return self.__bibtexml_BibTeXMLEntryType

    @bibtexml_BibTeXMLEntryType.setter
    def bibtexml_BibTeXMLEntryType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_BibTeXMLEntryType__bibtexml_BibTeXMLEntryType", None)
        self.__bibtexml_BibTeXMLEntryType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot44"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot44"):
                opp_val = getattr(value, "bibtexml_DocumentRoot44", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibtexml_MiscType:

    def __init__(self, author: str, title: str, howpublished: str, url: str, month: str, year: str, note: str, key: str, crossref: str, doi: str, bibtexml_MiscType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_MiscType64: "bibtexml_DocumentRoot" = None):
        self.author = author
        self.title = title
        self.howpublished = howpublished
        self.url = url
        self.month = month
        self.year = year
        self.note = note
        self.key = key
        self.crossref = crossref
        self.doi = doi
        self.bibtexml_MiscType = bibtexml_MiscType
        self.bibtexml_MiscType64 = bibtexml_MiscType64
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def howpublished(self) -> str:
        return self.__howpublished

    @howpublished.setter
    def howpublished(self, howpublished: str):
        self.__howpublished = howpublished

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def bibtexml_MiscType(self):
        return self.__bibtexml_MiscType

    @bibtexml_MiscType.setter
    def bibtexml_MiscType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_MiscType__bibtexml_MiscType", None)
        self.__bibtexml_MiscType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass26"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass26", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass26"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass26", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass26", self)

    @property
    def bibtexml_MiscType64(self):
        return self.__bibtexml_MiscType64

    @bibtexml_MiscType64.setter
    def bibtexml_MiscType64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_MiscType__bibtexml_MiscType64", None)
        self.__bibtexml_MiscType64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot63"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot63"):
                opp_val = getattr(value, "bibtexml_DocumentRoot63", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibtexml_UnpublishedType:

    def __init__(self, note: str, month: str, year: str, author: str, title: str, key: str, crossref: str, doi: str, url: str, bibtexml_UnpublishedType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_UnpublishedType76: "bibtexml_DocumentRoot" = None):
        self.note = note
        self.month = month
        self.year = year
        self.author = author
        self.title = title
        self.key = key
        self.crossref = crossref
        self.doi = doi
        self.url = url
        self.bibtexml_UnpublishedType = bibtexml_UnpublishedType
        self.bibtexml_UnpublishedType76 = bibtexml_UnpublishedType76
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def bibtexml_UnpublishedType76(self):
        return self.__bibtexml_UnpublishedType76

    @bibtexml_UnpublishedType76.setter
    def bibtexml_UnpublishedType76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_UnpublishedType__bibtexml_UnpublishedType76", None)
        self.__bibtexml_UnpublishedType76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot75"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot75"):
                opp_val = getattr(value, "bibtexml_DocumentRoot75", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bibtexml_UnpublishedType(self):
        return self.__bibtexml_UnpublishedType

    @bibtexml_UnpublishedType.setter
    def bibtexml_UnpublishedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_UnpublishedType__bibtexml_UnpublishedType", None)
        self.__bibtexml_UnpublishedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass24"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass24", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass24"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass24", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass24", self)

class bibtexml_InproceedingsType:

    def __init__(self, author: str, editor: str, title: str, booktitle: str, year: str, pages: str, volume: str, number: str, series: str, publisher: str, address: str, month: str, organization: str, doi: str, note: str, key: str, crossref: str, url: str, bibtexml_InproceedingsType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_InproceedingsType55: "bibtexml_DocumentRoot" = None):
        self.author = author
        self.editor = editor
        self.title = title
        self.booktitle = booktitle
        self.year = year
        self.pages = pages
        self.volume = volume
        self.number = number
        self.series = series
        self.publisher = publisher
        self.address = address
        self.month = month
        self.organization = organization
        self.doi = doi
        self.note = note
        self.key = key
        self.crossref = crossref
        self.url = url
        self.bibtexml_InproceedingsType = bibtexml_InproceedingsType
        self.bibtexml_InproceedingsType55 = bibtexml_InproceedingsType55
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def series(self) -> str:
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def booktitle(self) -> str:
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle

    @property
    def editor(self) -> str:
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor

    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def bibtexml_InproceedingsType(self):
        return self.__bibtexml_InproceedingsType

    @bibtexml_InproceedingsType.setter
    def bibtexml_InproceedingsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_InproceedingsType__bibtexml_InproceedingsType", None)
        self.__bibtexml_InproceedingsType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass20"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass20", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass20"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass20", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass20", self)

    @property
    def bibtexml_InproceedingsType55(self):
        return self.__bibtexml_InproceedingsType55

    @bibtexml_InproceedingsType55.setter
    def bibtexml_InproceedingsType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_InproceedingsType__bibtexml_InproceedingsType55", None)
        self.__bibtexml_InproceedingsType55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot54"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot54"):
                opp_val = getattr(value, "bibtexml_DocumentRoot54", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibtexml_ProceedingsType:

    def __init__(self, number: str, series: str, editor: str, title: str, year: str, volume: str, key: str, crossref: str, address: str, month: str, organization: str, publisher: str, note: str, doi: str, url: str, bibtexml_ProceedingsType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_ProceedingsType70: "bibtexml_DocumentRoot" = None):
        self.number = number
        self.series = series
        self.editor = editor
        self.title = title
        self.year = year
        self.volume = volume
        self.key = key
        self.crossref = crossref
        self.address = address
        self.month = month
        self.organization = organization
        self.publisher = publisher
        self.note = note
        self.doi = doi
        self.url = url
        self.bibtexml_ProceedingsType = bibtexml_ProceedingsType
        self.bibtexml_ProceedingsType70 = bibtexml_ProceedingsType70
        
    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def editor(self) -> str:
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor

    @property
    def series(self) -> str:
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def bibtexml_ProceedingsType70(self):
        return self.__bibtexml_ProceedingsType70

    @bibtexml_ProceedingsType70.setter
    def bibtexml_ProceedingsType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_ProceedingsType__bibtexml_ProceedingsType70", None)
        self.__bibtexml_ProceedingsType70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot69"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot69"):
                opp_val = getattr(value, "bibtexml_DocumentRoot69", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bibtexml_ProceedingsType(self):
        return self.__bibtexml_ProceedingsType

    @bibtexml_ProceedingsType.setter
    def bibtexml_ProceedingsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_ProceedingsType__bibtexml_ProceedingsType", None)
        self.__bibtexml_ProceedingsType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass18"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass18", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass18"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass18", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass18", self)

class bibtexml_IncollectionType:

    def __init__(self, title: str, author: str, editor: str, booktitle: str, publisher: str, year: str, type: str, volume: str, number: str, series: str, edition: str, chapter: str, pages: str, address: str, crossref: str, month: str, note: str, key: str, doi: str, url: str, bibtexml_IncollectionType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_IncollectionType52: "bibtexml_DocumentRoot" = None):
        self.title = title
        self.author = author
        self.editor = editor
        self.booktitle = booktitle
        self.publisher = publisher
        self.year = year
        self.type = type
        self.volume = volume
        self.number = number
        self.series = series
        self.edition = edition
        self.chapter = chapter
        self.pages = pages
        self.address = address
        self.crossref = crossref
        self.month = month
        self.note = note
        self.key = key
        self.doi = doi
        self.url = url
        self.bibtexml_IncollectionType = bibtexml_IncollectionType
        self.bibtexml_IncollectionType52 = bibtexml_IncollectionType52
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def booktitle(self) -> str:
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def edition(self) -> str:
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def chapter(self) -> str:
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: str):
        self.__chapter = chapter

    @property
    def editor(self) -> str:
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def series(self) -> str:
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series

    @property
    def bibtexml_IncollectionType(self):
        return self.__bibtexml_IncollectionType

    @bibtexml_IncollectionType.setter
    def bibtexml_IncollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_IncollectionType__bibtexml_IncollectionType", None)
        self.__bibtexml_IncollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass16"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass16", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass16"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass16", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass16", self)

    @property
    def bibtexml_IncollectionType52(self):
        return self.__bibtexml_IncollectionType52

    @bibtexml_IncollectionType52.setter
    def bibtexml_IncollectionType52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_IncollectionType__bibtexml_IncollectionType52", None)
        self.__bibtexml_IncollectionType52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot51"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot51"):
                opp_val = getattr(value, "bibtexml_DocumentRoot51", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibtexml_InbookType:

    def __init__(self, chapter: str, author: str, editor: str, title: str, number: str, pages: str, pages1: str, publisher: str, year: str, volume: str, month: str, series: str, type: str, address: str, edition: str, crossref: str, doi: str, note: str, key: str, url: str, bibtexml_InbookType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_InbookType49: "bibtexml_DocumentRoot" = None):
        self.chapter = chapter
        self.author = author
        self.editor = editor
        self.title = title
        self.number = number
        self.pages = pages
        self.pages1 = pages1
        self.publisher = publisher
        self.year = year
        self.volume = volume
        self.month = month
        self.series = series
        self.type = type
        self.address = address
        self.edition = edition
        self.crossref = crossref
        self.doi = doi
        self.note = note
        self.key = key
        self.url = url
        self.bibtexml_InbookType = bibtexml_InbookType
        self.bibtexml_InbookType49 = bibtexml_InbookType49
        
    @property
    def chapter(self) -> str:
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: str):
        self.__chapter = chapter

    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def editor(self) -> str:
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor

    @property
    def edition(self) -> str:
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def series(self) -> str:
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def pages1(self) -> str:
        return self.__pages1

    @pages1.setter
    def pages1(self, pages1: str):
        self.__pages1 = pages1

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def bibtexml_InbookType(self):
        return self.__bibtexml_InbookType

    @bibtexml_InbookType.setter
    def bibtexml_InbookType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_InbookType__bibtexml_InbookType", None)
        self.__bibtexml_InbookType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass14"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass14", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass14"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass14", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass14", self)

    @property
    def bibtexml_InbookType49(self):
        return self.__bibtexml_InbookType49

    @bibtexml_InbookType49.setter
    def bibtexml_InbookType49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_InbookType__bibtexml_InbookType49", None)
        self.__bibtexml_InbookType49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot48"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot48"):
                opp_val = getattr(value, "bibtexml_DocumentRoot48", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibtexml_ConferenceType:

    def __init__(self, author: str, title: str, year: str, editor: str, volume: str, number: str, series: str, booktitle: str, month: str, organization: str, publisher: str, note: str, pages: str, address: str, doi: str, url: str, key: str, crossref: str, bibtexml_ConferenceType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_ConferenceType42: "bibtexml_DocumentRoot" = None):
        self.author = author
        self.title = title
        self.year = year
        self.editor = editor
        self.volume = volume
        self.number = number
        self.series = series
        self.booktitle = booktitle
        self.month = month
        self.organization = organization
        self.publisher = publisher
        self.note = note
        self.pages = pages
        self.address = address
        self.doi = doi
        self.url = url
        self.key = key
        self.crossref = crossref
        self.bibtexml_ConferenceType = bibtexml_ConferenceType
        self.bibtexml_ConferenceType42 = bibtexml_ConferenceType42
        
    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def booktitle(self) -> str:
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle

    @property
    def series(self) -> str:
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series

    @property
    def editor(self) -> str:
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor

    @property
    def bibtexml_ConferenceType42(self):
        return self.__bibtexml_ConferenceType42

    @bibtexml_ConferenceType42.setter
    def bibtexml_ConferenceType42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_ConferenceType__bibtexml_ConferenceType42", None)
        self.__bibtexml_ConferenceType42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot41"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot41"):
                opp_val = getattr(value, "bibtexml_DocumentRoot41", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bibtexml_ConferenceType(self):
        return self.__bibtexml_ConferenceType

    @bibtexml_ConferenceType.setter
    def bibtexml_ConferenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_ConferenceType__bibtexml_ConferenceType", None)
        self.__bibtexml_ConferenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass22"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass22", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass22"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass22", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass22", self)

class bibtexml_MastersthesisType:

    def __init__(self, author: str, title: str, school: str, year: str, type: str, address: str, month: str, note: str, key: str, crossref: str, doi: str, url: str, bibtexml_MastersthesisType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_MastersthesisType61: "bibtexml_DocumentRoot" = None):
        self.author = author
        self.title = title
        self.school = school
        self.year = year
        self.type = type
        self.address = address
        self.month = month
        self.note = note
        self.key = key
        self.crossref = crossref
        self.doi = doi
        self.url = url
        self.bibtexml_MastersthesisType = bibtexml_MastersthesisType
        self.bibtexml_MastersthesisType61 = bibtexml_MastersthesisType61
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def school(self) -> str:
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def bibtexml_MastersthesisType61(self):
        return self.__bibtexml_MastersthesisType61

    @bibtexml_MastersthesisType61.setter
    def bibtexml_MastersthesisType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_MastersthesisType__bibtexml_MastersthesisType61", None)
        self.__bibtexml_MastersthesisType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot60"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot60"):
                opp_val = getattr(value, "bibtexml_DocumentRoot60", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bibtexml_MastersthesisType(self):
        return self.__bibtexml_MastersthesisType

    @bibtexml_MastersthesisType.setter
    def bibtexml_MastersthesisType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_MastersthesisType__bibtexml_MastersthesisType", None)
        self.__bibtexml_MastersthesisType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass10"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass10", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass10"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass10", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass10", self)

class bibtexml_TechreportType:

    def __init__(self, institution: str, year: str, type: str, author: str, title: str, key: str, crossref: str, doi: str, number: str, address: str, month: str, note: str, url: str, bibtexml_TechreportType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_TechreportType73: "bibtexml_DocumentRoot" = None):
        self.institution = institution
        self.year = year
        self.type = type
        self.author = author
        self.title = title
        self.key = key
        self.crossref = crossref
        self.doi = doi
        self.number = number
        self.address = address
        self.month = month
        self.note = note
        self.url = url
        self.bibtexml_TechreportType = bibtexml_TechreportType
        self.bibtexml_TechreportType73 = bibtexml_TechreportType73
        
    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def institution(self) -> str:
        return self.__institution

    @institution.setter
    def institution(self, institution: str):
        self.__institution = institution

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def bibtexml_TechreportType(self):
        return self.__bibtexml_TechreportType

    @bibtexml_TechreportType.setter
    def bibtexml_TechreportType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_TechreportType__bibtexml_TechreportType", None)
        self.__bibtexml_TechreportType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass8"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass8", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass8"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass8", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass8", self)

    @property
    def bibtexml_TechreportType73(self):
        return self.__bibtexml_TechreportType73

    @bibtexml_TechreportType73.setter
    def bibtexml_TechreportType73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_TechreportType__bibtexml_TechreportType73", None)
        self.__bibtexml_TechreportType73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot72"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot72"):
                opp_val = getattr(value, "bibtexml_DocumentRoot72", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibtexml_ManualType:

    def __init__(self, title: str, author: str, month: str, organization: str, address: str, edition: str, year: str, note: str, key: str, crossref: str, doi: str, url: str, bibtexml_ManualType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_ManualType58: "bibtexml_DocumentRoot" = None):
        self.title = title
        self.author = author
        self.month = month
        self.organization = organization
        self.address = address
        self.edition = edition
        self.year = year
        self.note = note
        self.key = key
        self.crossref = crossref
        self.doi = doi
        self.url = url
        self.bibtexml_ManualType = bibtexml_ManualType
        self.bibtexml_ManualType58 = bibtexml_ManualType58
        
    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def edition(self) -> str:
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def bibtexml_ManualType(self):
        return self.__bibtexml_ManualType

    @bibtexml_ManualType.setter
    def bibtexml_ManualType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_ManualType__bibtexml_ManualType", None)
        self.__bibtexml_ManualType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass6"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass6", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass6"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass6", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass6", self)

    @property
    def bibtexml_ManualType58(self):
        return self.__bibtexml_ManualType58

    @bibtexml_ManualType58.setter
    def bibtexml_ManualType58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_ManualType__bibtexml_ManualType58", None)
        self.__bibtexml_ManualType58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot57"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot57"):
                opp_val = getattr(value, "bibtexml_DocumentRoot57", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibtexml_BookletType:

    def __init__(self, author: str, title: str, key: str, howpublished: str, address: str, month: str, year: str, note: str, crossref: str, doi: str, url: str, bibtexml_BookletType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_BookletType39: "bibtexml_DocumentRoot" = None):
        self.author = author
        self.title = title
        self.key = key
        self.howpublished = howpublished
        self.address = address
        self.month = month
        self.year = year
        self.note = note
        self.crossref = crossref
        self.doi = doi
        self.url = url
        self.bibtexml_BookletType = bibtexml_BookletType
        self.bibtexml_BookletType39 = bibtexml_BookletType39
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def howpublished(self) -> str:
        return self.__howpublished

    @howpublished.setter
    def howpublished(self, howpublished: str):
        self.__howpublished = howpublished

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def bibtexml_BookletType(self):
        return self.__bibtexml_BookletType

    @bibtexml_BookletType.setter
    def bibtexml_BookletType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_BookletType__bibtexml_BookletType", None)
        self.__bibtexml_BookletType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass4"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass4", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass4"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass4", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass4", self)

    @property
    def bibtexml_BookletType39(self):
        return self.__bibtexml_BookletType39

    @bibtexml_BookletType39.setter
    def bibtexml_BookletType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_BookletType__bibtexml_BookletType39", None)
        self.__bibtexml_BookletType39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot38"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot38"):
                opp_val = getattr(value, "bibtexml_DocumentRoot38", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibtexml_BookType:

    def __init__(self, title: str, author: str, editor: str, address: str, publisher: str, year: str, volume: str, number: str, series: str, doi: str, url: str, edition: str, month: str, note: str, key: str, crossref: str, bibtexml_BookType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_BookType36: "bibtexml_DocumentRoot" = None):
        self.title = title
        self.author = author
        self.editor = editor
        self.address = address
        self.publisher = publisher
        self.year = year
        self.volume = volume
        self.number = number
        self.series = series
        self.doi = doi
        self.url = url
        self.edition = edition
        self.month = month
        self.note = note
        self.key = key
        self.crossref = crossref
        self.bibtexml_BookType = bibtexml_BookType
        self.bibtexml_BookType36 = bibtexml_BookType36
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def series(self) -> str:
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def edition(self) -> str:
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def editor(self) -> str:
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor

    @property
    def bibtexml_BookType36(self):
        return self.__bibtexml_BookType36

    @bibtexml_BookType36.setter
    def bibtexml_BookType36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_BookType__bibtexml_BookType36", None)
        self.__bibtexml_BookType36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot35"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot35"):
                opp_val = getattr(value, "bibtexml_DocumentRoot35", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bibtexml_BookType(self):
        return self.__bibtexml_BookType

    @bibtexml_BookType.setter
    def bibtexml_BookType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_BookType__bibtexml_BookType", None)
        self.__bibtexml_BookType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass2"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass2", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass2"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass2", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass2", self)

class bibtexml_PhdthesisType:

    def __init__(self, year: str, type: str, author: str, title: str, school: str, doi: str, url: str, address: str, month: str, note: str, key: str, crossref: str, bibtexml_PhdthesisType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_PhdthesisType67: "bibtexml_DocumentRoot" = None):
        self.year = year
        self.type = type
        self.author = author
        self.title = title
        self.school = school
        self.doi = doi
        self.url = url
        self.address = address
        self.month = month
        self.note = note
        self.key = key
        self.crossref = crossref
        self.bibtexml_PhdthesisType = bibtexml_PhdthesisType
        self.bibtexml_PhdthesisType67 = bibtexml_PhdthesisType67
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def school(self) -> str:
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def bibtexml_PhdthesisType(self):
        return self.__bibtexml_PhdthesisType

    @bibtexml_PhdthesisType.setter
    def bibtexml_PhdthesisType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_PhdthesisType__bibtexml_PhdthesisType", None)
        self.__bibtexml_PhdthesisType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass12"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass12", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass12"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass12", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass12", self)

    @property
    def bibtexml_PhdthesisType67(self):
        return self.__bibtexml_PhdthesisType67

    @bibtexml_PhdthesisType67.setter
    def bibtexml_PhdthesisType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_PhdthesisType__bibtexml_PhdthesisType67", None)
        self.__bibtexml_PhdthesisType67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot66"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot66"):
                opp_val = getattr(value, "bibtexml_DocumentRoot66", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bibtexml_BibTeXMLEntriesClass:

    pass
class bibtexml_ArticleType:

    def __init__(self, journal: str, author: str, title: str, note: str, year: str, volume: str, number: str, pages: str, month: str, key: str, crossref: str, doi: str, url: str, bibtexml_ArticleType: "bibtexml_BibTeXMLEntriesClass" = None, bibtexml_ArticleType33: "bibtexml_DocumentRoot" = None):
        self.journal = journal
        self.author = author
        self.title = title
        self.note = note
        self.year = year
        self.volume = volume
        self.number = number
        self.pages = pages
        self.month = month
        self.key = key
        self.crossref = crossref
        self.doi = doi
        self.url = url
        self.bibtexml_ArticleType = bibtexml_ArticleType
        self.bibtexml_ArticleType33 = bibtexml_ArticleType33
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def doi(self) -> str:
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi

    @property
    def journal(self) -> str:
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def crossref(self) -> str:
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref

    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def bibtexml_ArticleType33(self):
        return self.__bibtexml_ArticleType33

    @bibtexml_ArticleType33.setter
    def bibtexml_ArticleType33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_ArticleType__bibtexml_ArticleType33", None)
        self.__bibtexml_ArticleType33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_DocumentRoot32"):
                opp_val = getattr(old_value, "bibtexml_DocumentRoot32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_DocumentRoot32"):
                opp_val = getattr(value, "bibtexml_DocumentRoot32", None)
                if opp_val is None:
                    setattr(value, "bibtexml_DocumentRoot32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bibtexml_ArticleType(self):
        return self.__bibtexml_ArticleType

    @bibtexml_ArticleType.setter
    def bibtexml_ArticleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtexml_ArticleType__bibtexml_ArticleType", None)
        self.__bibtexml_ArticleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtexml_BibTeXMLEntriesClass"):
                opp_val = getattr(old_value, "bibtexml_BibTeXMLEntriesClass", None)
                if opp_val == self:
                    setattr(old_value, "bibtexml_BibTeXMLEntriesClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtexml_BibTeXMLEntriesClass"):
                opp_val = getattr(value, "bibtexml_BibTeXMLEntriesClass", None)
                setattr(value, "bibtexml_BibTeXMLEntriesClass", self)
