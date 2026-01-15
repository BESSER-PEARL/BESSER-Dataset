from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class bibTeX_EditorField:

    def __init__(self, editor: str):
        self.editor = editor
        
    @property
    def editor(self) -> str:
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor

class bibTeX_IsbnField:

    def __init__(self, isbn: str, bibTeX_IsbnField: "bibTeX_Book" = None):
        self.isbn = isbn
        self.bibTeX_IsbnField = bibTeX_IsbnField
        
    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def bibTeX_IsbnField(self):
        return self.__bibTeX_IsbnField

    @bibTeX_IsbnField.setter
    def bibTeX_IsbnField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_IsbnField__bibTeX_IsbnField", None)
        self.__bibTeX_IsbnField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_Book35"):
                opp_val = getattr(old_value, "bibTeX_Book35", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_Book35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_Book35"):
                opp_val = getattr(value, "bibTeX_Book35", None)
                setattr(value, "bibTeX_Book35", self)

class bibTeX_EditionField:

    def __init__(self, edition: str, bibTeX_EditionField: "bibTeX_Book" = None):
        self.edition = edition
        self.bibTeX_EditionField = bibTeX_EditionField
        
    @property
    def edition(self) -> str:
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition

    @property
    def bibTeX_EditionField(self):
        return self.__bibTeX_EditionField

    @bibTeX_EditionField.setter
    def bibTeX_EditionField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_EditionField__bibTeX_EditionField", None)
        self.__bibTeX_EditionField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_Book33"):
                opp_val = getattr(old_value, "bibTeX_Book33", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_Book33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_Book33"):
                opp_val = getattr(value, "bibTeX_Book33", None)
                setattr(value, "bibTeX_Book33", self)

class bibTeX_AddressField:

    def __init__(self, address: str, bibTeX_AddressField: "bibTeX_Book" = None):
        self.address = address
        self.bibTeX_AddressField = bibTeX_AddressField
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def bibTeX_AddressField(self):
        return self.__bibTeX_AddressField

    @bibTeX_AddressField.setter
    def bibTeX_AddressField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_AddressField__bibTeX_AddressField", None)
        self.__bibTeX_AddressField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_Book31"):
                opp_val = getattr(old_value, "bibTeX_Book31", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_Book31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_Book31"):
                opp_val = getattr(value, "bibTeX_Book31", None)
                setattr(value, "bibTeX_Book31", self)

class bibTeX_SeriesField:

    def __init__(self, series: str, bibTeX_SeriesField: "bibTeX_Book" = None):
        self.series = series
        self.bibTeX_SeriesField = bibTeX_SeriesField
        
    @property
    def series(self) -> str:
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series

    @property
    def bibTeX_SeriesField(self):
        return self.__bibTeX_SeriesField

    @bibTeX_SeriesField.setter
    def bibTeX_SeriesField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_SeriesField__bibTeX_SeriesField", None)
        self.__bibTeX_SeriesField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_Book29"):
                opp_val = getattr(old_value, "bibTeX_Book29", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_Book29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_Book29"):
                opp_val = getattr(value, "bibTeX_Book29", None)
                setattr(value, "bibTeX_Book29", self)

class bibTeX_PublisherField:

    def __init__(self, publisher: str, bibTeX_PublisherField: "bibTeX_Book" = None):
        self.publisher = publisher
        self.bibTeX_PublisherField = bibTeX_PublisherField
        
    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def bibTeX_PublisherField(self):
        return self.__bibTeX_PublisherField

    @bibTeX_PublisherField.setter
    def bibTeX_PublisherField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_PublisherField__bibTeX_PublisherField", None)
        self.__bibTeX_PublisherField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_Book24"):
                opp_val = getattr(old_value, "bibTeX_Book24", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_Book24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_Book24"):
                opp_val = getattr(value, "bibTeX_Book24", None)
                setattr(value, "bibTeX_Book24", self)

class bibTeX_EObject:

    pass
class bibTeX_PagesField:

    def __init__(self, pages: str, bibTeX_PagesField: "bibTeX_Article" = None):
        self.pages = pages
        self.bibTeX_PagesField = bibTeX_PagesField
        
    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def bibTeX_PagesField(self):
        return self.__bibTeX_PagesField

    @bibTeX_PagesField.setter
    def bibTeX_PagesField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_PagesField__bibTeX_PagesField", None)
        self.__bibTeX_PagesField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_Article21"):
                opp_val = getattr(old_value, "bibTeX_Article21", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_Article21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_Article21"):
                opp_val = getattr(value, "bibTeX_Article21", None)
                setattr(value, "bibTeX_Article21", self)

class bibTeX_NumberField:

    def __init__(self, number: str, bibTeX_NumberField: "bibTeX_Article" = None):
        self.number = number
        self.bibTeX_NumberField = bibTeX_NumberField
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def bibTeX_NumberField(self):
        return self.__bibTeX_NumberField

    @bibTeX_NumberField.setter
    def bibTeX_NumberField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_NumberField__bibTeX_NumberField", None)
        self.__bibTeX_NumberField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_Article19"):
                opp_val = getattr(old_value, "bibTeX_Article19", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_Article19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_Article19"):
                opp_val = getattr(value, "bibTeX_Article19", None)
                setattr(value, "bibTeX_Article19", self)

class bibTeX_VolumeField:

    def __init__(self, volume: str, bibTeX_VolumeField: "bibTeX_Article" = None):
        self.volume = volume
        self.bibTeX_VolumeField = bibTeX_VolumeField
        
    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def bibTeX_VolumeField(self):
        return self.__bibTeX_VolumeField

    @bibTeX_VolumeField.setter
    def bibTeX_VolumeField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_VolumeField__bibTeX_VolumeField", None)
        self.__bibTeX_VolumeField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_Article17"):
                opp_val = getattr(old_value, "bibTeX_Article17", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_Article17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_Article17"):
                opp_val = getattr(value, "bibTeX_Article17", None)
                setattr(value, "bibTeX_Article17", self)

class bibTeX_JournalField:

    def __init__(self, journal: str, bibTeX_JournalField: "bibTeX_Article" = None):
        self.journal = journal
        self.bibTeX_JournalField = bibTeX_JournalField
        
    @property
    def journal(self) -> str:
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal

    @property
    def bibTeX_JournalField(self):
        return self.__bibTeX_JournalField

    @bibTeX_JournalField.setter
    def bibTeX_JournalField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_JournalField__bibTeX_JournalField", None)
        self.__bibTeX_JournalField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_Article15"):
                opp_val = getattr(old_value, "bibTeX_Article15", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_Article15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_Article15"):
                opp_val = getattr(value, "bibTeX_Article15", None)
                setattr(value, "bibTeX_Article15", self)

class bibTeX_AuthorField:

    pass
class BibtexEntryTypes:

    pass
class bibTeX_Book(BibtexEntryTypes):

    pass
class bibTeX_Article(BibtexEntryTypes):

    pass
class bibTeX_Fullname:

    def __init__(self, lastname: str, firstname: str, bibTeX_Fullname: "bibTeX_Authors" = None):
        self.lastname = lastname
        self.firstname = firstname
        self.bibTeX_Fullname = bibTeX_Fullname
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def bibTeX_Fullname(self):
        return self.__bibTeX_Fullname

    @bibTeX_Fullname.setter
    def bibTeX_Fullname(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_Fullname__bibTeX_Fullname", None)
        self.__bibTeX_Fullname = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_Authors"):
                opp_val = getattr(old_value, "bibTeX_Authors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_Authors"):
                opp_val = getattr(value, "bibTeX_Authors", None)
                if opp_val is None:
                    setattr(value, "bibTeX_Authors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AuthorField:

    pass
class bibTeX_Authors(AuthorField):

    pass
class bibTeX_UnknownValue:

    def __init__(self, value: str, bibTeX_UnknownValue: "bibTeX_UnknownField" = None):
        self.value = value
        self.bibTeX_UnknownValue = bibTeX_UnknownValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def bibTeX_UnknownValue(self):
        return self.__bibTeX_UnknownValue

    @bibTeX_UnknownValue.setter
    def bibTeX_UnknownValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_UnknownValue__bibTeX_UnknownValue", None)
        self.__bibTeX_UnknownValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_UnknownField39"):
                opp_val = getattr(old_value, "bibTeX_UnknownField39", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_UnknownField39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_UnknownField39"):
                opp_val = getattr(value, "bibTeX_UnknownField39", None)
                setattr(value, "bibTeX_UnknownField39", self)

class bibTeX_UnknownType:

    def __init__(self, type: str, bibTeX_UnknownType: "bibTeX_UnknownField" = None):
        self.type = type
        self.bibTeX_UnknownType = bibTeX_UnknownType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def bibTeX_UnknownType(self):
        return self.__bibTeX_UnknownType

    @bibTeX_UnknownType.setter
    def bibTeX_UnknownType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_UnknownType__bibTeX_UnknownType", None)
        self.__bibTeX_UnknownType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_UnknownField37"):
                opp_val = getattr(old_value, "bibTeX_UnknownField37", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_UnknownField37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_UnknownField37"):
                opp_val = getattr(value, "bibTeX_UnknownField37", None)
                setattr(value, "bibTeX_UnknownField37", self)

class bibTeX_BibtexEntryTypes:

    pass
class bibTeX_Model:

    pass
class bibTeX_UnknownField:

    pass
class bibTeX_NoteField:

    def __init__(self, note: str, bibTeX_NoteField: "bibTeX_BibtexEntryTypes" = None):
        self.note = note
        self.bibTeX_NoteField = bibTeX_NoteField
        
    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def bibTeX_NoteField(self):
        return self.__bibTeX_NoteField

    @bibTeX_NoteField.setter
    def bibTeX_NoteField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_NoteField__bibTeX_NoteField", None)
        self.__bibTeX_NoteField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_BibtexEntryTypes10"):
                opp_val = getattr(old_value, "bibTeX_BibtexEntryTypes10", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_BibtexEntryTypes10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_BibtexEntryTypes10"):
                opp_val = getattr(value, "bibTeX_BibtexEntryTypes10", None)
                setattr(value, "bibTeX_BibtexEntryTypes10", self)

class bibTeX_MonthField:

    def __init__(self, month: str, bibTeX_MonthField: "bibTeX_BibtexEntryTypes" = None):
        self.month = month
        self.bibTeX_MonthField = bibTeX_MonthField
        
    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def bibTeX_MonthField(self):
        return self.__bibTeX_MonthField

    @bibTeX_MonthField.setter
    def bibTeX_MonthField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_MonthField__bibTeX_MonthField", None)
        self.__bibTeX_MonthField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_BibtexEntryTypes8"):
                opp_val = getattr(old_value, "bibTeX_BibtexEntryTypes8", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_BibtexEntryTypes8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_BibtexEntryTypes8"):
                opp_val = getattr(value, "bibTeX_BibtexEntryTypes8", None)
                setattr(value, "bibTeX_BibtexEntryTypes8", self)

class bibTeX_YearField:

    def __init__(self, year: str, bibTeX_YearField: "bibTeX_BibtexEntryTypes" = None):
        self.year = year
        self.bibTeX_YearField = bibTeX_YearField
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def bibTeX_YearField(self):
        return self.__bibTeX_YearField

    @bibTeX_YearField.setter
    def bibTeX_YearField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_YearField__bibTeX_YearField", None)
        self.__bibTeX_YearField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_BibtexEntryTypes6"):
                opp_val = getattr(old_value, "bibTeX_BibtexEntryTypes6", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_BibtexEntryTypes6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_BibtexEntryTypes6"):
                opp_val = getattr(value, "bibTeX_BibtexEntryTypes6", None)
                setattr(value, "bibTeX_BibtexEntryTypes6", self)

class bibTeX_TitleField:

    def __init__(self, title: str, bibTeX_TitleField: "bibTeX_BibtexEntryTypes" = None):
        self.title = title
        self.bibTeX_TitleField = bibTeX_TitleField
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def bibTeX_TitleField(self):
        return self.__bibTeX_TitleField

    @bibTeX_TitleField.setter
    def bibTeX_TitleField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_TitleField__bibTeX_TitleField", None)
        self.__bibTeX_TitleField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_BibtexEntryTypes4"):
                opp_val = getattr(old_value, "bibTeX_BibtexEntryTypes4", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_BibtexEntryTypes4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_BibtexEntryTypes4"):
                opp_val = getattr(value, "bibTeX_BibtexEntryTypes4", None)
                setattr(value, "bibTeX_BibtexEntryTypes4", self)

class bibTeX_CiteKey:

    def __init__(self, key: str, bibTeX_CiteKey: "bibTeX_BibtexEntryTypes" = None):
        self.key = key
        self.bibTeX_CiteKey = bibTeX_CiteKey
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def bibTeX_CiteKey(self):
        return self.__bibTeX_CiteKey

    @bibTeX_CiteKey.setter
    def bibTeX_CiteKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibTeX_CiteKey__bibTeX_CiteKey", None)
        self.__bibTeX_CiteKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibTeX_BibtexEntryTypes2"):
                opp_val = getattr(old_value, "bibTeX_BibtexEntryTypes2", None)
                if opp_val == self:
                    setattr(old_value, "bibTeX_BibtexEntryTypes2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibTeX_BibtexEntryTypes2"):
                opp_val = getattr(value, "bibTeX_BibtexEntryTypes2", None)
                setattr(value, "bibTeX_BibtexEntryTypes2", self)
