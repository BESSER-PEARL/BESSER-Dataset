####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
bibTeX_CiteKey = Class(name="bibTeX::CiteKey")
bibTeX_TitleField = Class(name="bibTeX::TitleField")
bibTeX_YearField = Class(name="bibTeX::YearField")
bibTeX_MonthField = Class(name="bibTeX::MonthField")
bibTeX_NoteField = Class(name="bibTeX::NoteField")
bibTeX_UnknownField = Class(name="bibTeX::UnknownField")
bibTeX_Model = Class(name="bibTeX::Model")
bibTeX_BibtexEntryTypes = Class(name="bibTeX::BibtexEntryTypes")
bibTeX_UnknownType = Class(name="bibTeX::UnknownType")
bibTeX_UnknownValue = Class(name="bibTeX::UnknownValue")
bibTeX_Authors = Class(name="bibTeX::Authors")
AuthorField = Class(name="AuthorField")
bibTeX_Fullname = Class(name="bibTeX::Fullname")
bibTeX_Article = Class(name="bibTeX::Article")
BibtexEntryTypes = Class(name="BibtexEntryTypes")
bibTeX_AuthorField = Class(name="bibTeX::AuthorField")
bibTeX_JournalField = Class(name="bibTeX::JournalField")
bibTeX_VolumeField = Class(name="bibTeX::VolumeField")
bibTeX_NumberField = Class(name="bibTeX::NumberField")
bibTeX_PagesField = Class(name="bibTeX::PagesField")
bibTeX_Book = Class(name="bibTeX::Book")
bibTeX_EObject = Class(name="bibTeX::EObject")
bibTeX_PublisherField = Class(name="bibTeX::PublisherField")
bibTeX_SeriesField = Class(name="bibTeX::SeriesField")
bibTeX_AddressField = Class(name="bibTeX::AddressField")
bibTeX_EditionField = Class(name="bibTeX::EditionField")
bibTeX_IsbnField = Class(name="bibTeX::IsbnField")
bibTeX_EditorField = Class(name="bibTeX::EditorField")

# bibTeX_CiteKey class attributes and methods
bibTeX_CiteKey_key: Property = Property(name="key", type=StringType)
bibTeX_CiteKey.attributes={bibTeX_CiteKey_key}

# bibTeX_TitleField class attributes and methods
bibTeX_TitleField_title: Property = Property(name="title", type=StringType)
bibTeX_TitleField.attributes={bibTeX_TitleField_title}

# bibTeX_YearField class attributes and methods
bibTeX_YearField_year: Property = Property(name="year", type=StringType)
bibTeX_YearField.attributes={bibTeX_YearField_year}

# bibTeX_MonthField class attributes and methods
bibTeX_MonthField_month: Property = Property(name="month", type=StringType)
bibTeX_MonthField.attributes={bibTeX_MonthField_month}

# bibTeX_NoteField class attributes and methods
bibTeX_NoteField_note: Property = Property(name="note", type=StringType)
bibTeX_NoteField.attributes={bibTeX_NoteField_note}

# bibTeX_UnknownField class attributes and methods

# bibTeX_Model class attributes and methods

# bibTeX_BibtexEntryTypes class attributes and methods

# bibTeX_UnknownType class attributes and methods
bibTeX_UnknownType_type: Property = Property(name="type", type=StringType)
bibTeX_UnknownType.attributes={bibTeX_UnknownType_type}

# bibTeX_UnknownValue class attributes and methods
bibTeX_UnknownValue_value: Property = Property(name="value", type=StringType)
bibTeX_UnknownValue.attributes={bibTeX_UnknownValue_value}

# bibTeX_Authors class attributes and methods

# AuthorField class attributes and methods

# bibTeX_Fullname class attributes and methods
bibTeX_Fullname_lastname: Property = Property(name="lastname", type=StringType)
bibTeX_Fullname_firstname: Property = Property(name="firstname", type=StringType)
bibTeX_Fullname.attributes={bibTeX_Fullname_firstname, bibTeX_Fullname_lastname}

# bibTeX_Article class attributes and methods

# BibtexEntryTypes class attributes and methods

# bibTeX_AuthorField class attributes and methods

# bibTeX_JournalField class attributes and methods
bibTeX_JournalField_journal: Property = Property(name="journal", type=StringType)
bibTeX_JournalField.attributes={bibTeX_JournalField_journal}

# bibTeX_VolumeField class attributes and methods
bibTeX_VolumeField_volume: Property = Property(name="volume", type=StringType)
bibTeX_VolumeField.attributes={bibTeX_VolumeField_volume}

# bibTeX_NumberField class attributes and methods
bibTeX_NumberField_number: Property = Property(name="number", type=StringType)
bibTeX_NumberField.attributes={bibTeX_NumberField_number}

# bibTeX_PagesField class attributes and methods
bibTeX_PagesField_pages: Property = Property(name="pages", type=StringType)
bibTeX_PagesField.attributes={bibTeX_PagesField_pages}

# bibTeX_Book class attributes and methods

# bibTeX_EObject class attributes and methods

# bibTeX_PublisherField class attributes and methods
bibTeX_PublisherField_publisher: Property = Property(name="publisher", type=StringType)
bibTeX_PublisherField.attributes={bibTeX_PublisherField_publisher}

# bibTeX_SeriesField class attributes and methods
bibTeX_SeriesField_series: Property = Property(name="series", type=StringType)
bibTeX_SeriesField.attributes={bibTeX_SeriesField_series}

# bibTeX_AddressField class attributes and methods
bibTeX_AddressField_address: Property = Property(name="address", type=StringType)
bibTeX_AddressField.attributes={bibTeX_AddressField_address}

# bibTeX_EditionField class attributes and methods
bibTeX_EditionField_edition: Property = Property(name="edition", type=StringType)
bibTeX_EditionField.attributes={bibTeX_EditionField_edition}

# bibTeX_IsbnField class attributes and methods
bibTeX_IsbnField_isbn: Property = Property(name="isbn", type=StringType)
bibTeX_IsbnField.attributes={bibTeX_IsbnField_isbn}

# bibTeX_EditorField class attributes and methods
bibTeX_EditorField_editor: Property = Property(name="editor", type=StringType)
bibTeX_EditorField.attributes={bibTeX_EditorField_editor}

# Relationships
key1: BinaryAssociation = BinaryAssociation(
    name="key1",
    ends={
        Property(name="bibTeX_CiteKey", type=bibTeX_BibtexEntryTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_BibtexEntryTypes2", type=bibTeX_CiteKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title3: BinaryAssociation = BinaryAssociation(
    name="title3",
    ends={
        Property(name="bibTeX_TitleField", type=bibTeX_BibtexEntryTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_BibtexEntryTypes4", type=bibTeX_TitleField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
year5: BinaryAssociation = BinaryAssociation(
    name="year5",
    ends={
        Property(name="bibTeX_YearField", type=bibTeX_BibtexEntryTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_BibtexEntryTypes6", type=bibTeX_YearField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
month7: BinaryAssociation = BinaryAssociation(
    name="month7",
    ends={
        Property(name="bibTeX_MonthField", type=bibTeX_BibtexEntryTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_BibtexEntryTypes8", type=bibTeX_MonthField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
note9: BinaryAssociation = BinaryAssociation(
    name="note9",
    ends={
        Property(name="bibTeX_NoteField", type=bibTeX_BibtexEntryTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_BibtexEntryTypes10", type=bibTeX_NoteField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unknowns11: BinaryAssociation = BinaryAssociation(
    name="unknowns11",
    ends={
        Property(name="bibTeX_UnknownField", type=bibTeX_BibtexEntryTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_BibtexEntryTypes12", type=bibTeX_UnknownField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BibtexEntries0: BinaryAssociation = BinaryAssociation(
    name="BibtexEntries0",
    ends={
        Property(name="bibTeX_BibtexEntryTypes", type=bibTeX_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Model", type=bibTeX_BibtexEntryTypes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type36: BinaryAssociation = BinaryAssociation(
    name="type36",
    ends={
        Property(name="bibTeX_UnknownType", type=bibTeX_UnknownField, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_UnknownField37", type=bibTeX_UnknownType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value38: BinaryAssociation = BinaryAssociation(
    name="value38",
    ends={
        Property(name="bibTeX_UnknownValue", type=bibTeX_UnknownField, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_UnknownField39", type=bibTeX_UnknownValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author13: BinaryAssociation = BinaryAssociation(
    name="author13",
    ends={
        Property(name="bibTeX_AuthorField", type=bibTeX_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Article", type=bibTeX_AuthorField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
journal14: BinaryAssociation = BinaryAssociation(
    name="journal14",
    ends={
        Property(name="bibTeX_JournalField", type=bibTeX_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Article15", type=bibTeX_JournalField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
volume16: BinaryAssociation = BinaryAssociation(
    name="volume16",
    ends={
        Property(name="bibTeX_VolumeField", type=bibTeX_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Article17", type=bibTeX_VolumeField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number18: BinaryAssociation = BinaryAssociation(
    name="number18",
    ends={
        Property(name="bibTeX_NumberField", type=bibTeX_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Article19", type=bibTeX_NumberField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pages20: BinaryAssociation = BinaryAssociation(
    name="pages20",
    ends={
        Property(name="bibTeX_PagesField", type=bibTeX_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Article21", type=bibTeX_PagesField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author_editor22: BinaryAssociation = BinaryAssociation(
    name="author_editor22",
    ends={
        Property(name="bibTeX_EObject", type=bibTeX_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Book", type=bibTeX_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publisher23: BinaryAssociation = BinaryAssociation(
    name="publisher23",
    ends={
        Property(name="bibTeX_PublisherField", type=bibTeX_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Book24", type=bibTeX_PublisherField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
volume_number25: BinaryAssociation = BinaryAssociation(
    name="volume_number25",
    ends={
        Property(name="bibTeX_EObject27", type=bibTeX_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Book26", type=bibTeX_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
series28: BinaryAssociation = BinaryAssociation(
    name="series28",
    ends={
        Property(name="bibTeX_SeriesField", type=bibTeX_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Book29", type=bibTeX_SeriesField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address30: BinaryAssociation = BinaryAssociation(
    name="address30",
    ends={
        Property(name="bibTeX_AddressField", type=bibTeX_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Book31", type=bibTeX_AddressField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edition32: BinaryAssociation = BinaryAssociation(
    name="edition32",
    ends={
        Property(name="bibTeX_EditionField", type=bibTeX_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Book33", type=bibTeX_EditionField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isbn34: BinaryAssociation = BinaryAssociation(
    name="isbn34",
    ends={
        Property(name="bibTeX_IsbnField", type=bibTeX_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Book35", type=bibTeX_IsbnField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
names40: BinaryAssociation = BinaryAssociation(
    name="names40",
    ends={
        Property(name="bibTeX_Fullname", type=bibTeX_Authors, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_Authors", type=bibTeX_Fullname, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_bibTeX_Authors_AuthorField = Generalization(general=AuthorField, specific=bibTeX_Authors)
gen_bibTeX_Article_BibtexEntryTypes = Generalization(general=BibtexEntryTypes, specific=bibTeX_Article)
gen_bibTeX_Book_BibtexEntryTypes = Generalization(general=BibtexEntryTypes, specific=bibTeX_Book)

# Domain Model
domain_model = DomainModel(
    name="bibTeX",
    types={bibTeX_CiteKey, bibTeX_TitleField, bibTeX_YearField, bibTeX_MonthField, bibTeX_NoteField, bibTeX_UnknownField, bibTeX_Model, bibTeX_BibtexEntryTypes, bibTeX_UnknownType, bibTeX_UnknownValue, bibTeX_Authors, AuthorField, bibTeX_Fullname, bibTeX_Article, BibtexEntryTypes, bibTeX_AuthorField, bibTeX_JournalField, bibTeX_VolumeField, bibTeX_NumberField, bibTeX_PagesField, bibTeX_Book, bibTeX_EObject, bibTeX_PublisherField, bibTeX_SeriesField, bibTeX_AddressField, bibTeX_EditionField, bibTeX_IsbnField, bibTeX_EditorField},
    associations={key1, title3, year5, month7, note9, unknowns11, BibtexEntries0, type36, value38, author13, journal14, volume16, number18, pages20, author_editor22, publisher23, volume_number25, series28, address30, edition32, isbn34, names40},
    generalizations={gen_bibTeX_Authors_AuthorField, gen_bibTeX_Article_BibtexEntryTypes, gen_bibTeX_Book_BibtexEntryTypes},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)