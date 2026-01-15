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
bibtex_Person = Class(name="bibtex::Person", is_abstract=True)
bibtex_Author = Class(name="bibtex::Author")
Person = Class(name="Person")
bibtex_Editor = Class(name="bibtex::Editor")
bibtex_StringValue = Class(name="bibtex::StringValue", is_abstract=True)
bibtex_YearValue = Class(name="bibtex::YearValue", is_abstract=True)
bibtex_IntValue = Class(name="bibtex::IntValue", is_abstract=True)
bibtex_Page = Class(name="bibtex::Page")
IntValue = Class(name="IntValue")
bibtex_Field = Class(name="bibtex::Field", is_abstract=True)
bibtex_AuthorField = Class(name="bibtex::AuthorField")
Field = Class(name="Field")
bibtex_EditorField = Class(name="bibtex::EditorField")
bibtex_TitleField = Class(name="bibtex::TitleField")
StringValue = Class(name="StringValue")
bibtex_BookTitleField = Class(name="bibtex::BookTitleField")
bibtex_NumberField = Class(name="bibtex::NumberField")
bibtex_YearField = Class(name="bibtex::YearField")
YearValue = Class(name="YearValue")
bibtex_BibtexKeyField = Class(name="bibtex::BibtexKeyField")
bibtex_JournalField = Class(name="bibtex::JournalField")
bibtex_VolumeField = Class(name="bibtex::VolumeField")
bibtex_PageField = Class(name="bibtex::PageField")
bibtex_SeriesField = Class(name="bibtex::SeriesField")
bibtex_AddressField = Class(name="bibtex::AddressField")
bibtex_MonthField = Class(name="bibtex::MonthField")
bibtex_OrganizationField = Class(name="bibtex::OrganizationField")
bibtex_NoteField = Class(name="bibtex::NoteField")
bibtex_PublisherField = Class(name="bibtex::PublisherField")
bibtex_PartField = Class(name="bibtex::PartField")
bibtex_EidField = Class(name="bibtex::EidField")
bibtex_UrlField = Class(name="bibtex::UrlField")
bibtex_Keyword = Class(name="bibtex::Keyword")
bibtex_KeywordField = Class(name="bibtex::KeywordField")
bibtex_AbstractField = Class(name="bibtex::AbstractField")
bibtex_ReviewField = Class(name="bibtex::ReviewField")
bibtex_Entry = Class(name="bibtex::Entry", is_abstract=True)
bibtex_InProceedingsEntry = Class(name="bibtex::InProceedingsEntry")
Entry = Class(name="Entry")
bibtex_ArticleEntry = Class(name="bibtex::ArticleEntry")
bibtex_Bibliography = Class(name="bibtex::Bibliography")

# bibtex_Person class attributes and methods
bibtex_Person_firstName: Property = Property(name="firstName", type=StringType)
bibtex_Person_secondName: Property = Property(name="secondName", type=StringType)
bibtex_Person_lastName: Property = Property(name="lastName", type=StringType)
bibtex_Person.attributes={bibtex_Person_secondName, bibtex_Person_firstName, bibtex_Person_lastName}

# bibtex_Author class attributes and methods

# Person class attributes and methods

# bibtex_Editor class attributes and methods

# bibtex_StringValue class attributes and methods
bibtex_StringValue_value: Property = Property(name="value", type=StringType)
bibtex_StringValue.attributes={bibtex_StringValue_value}

# bibtex_YearValue class attributes and methods
bibtex_YearValue_value: Property = Property(name="value", type=IntegerType)
bibtex_YearValue.attributes={bibtex_YearValue_value}

# bibtex_IntValue class attributes and methods
bibtex_IntValue_value: Property = Property(name="value", type=IntegerType)
bibtex_IntValue.attributes={bibtex_IntValue_value}

# bibtex_Page class attributes and methods

# IntValue class attributes and methods

# bibtex_Field class attributes and methods

# bibtex_AuthorField class attributes and methods

# Field class attributes and methods

# bibtex_EditorField class attributes and methods

# bibtex_TitleField class attributes and methods

# StringValue class attributes and methods

# bibtex_BookTitleField class attributes and methods

# bibtex_NumberField class attributes and methods

# bibtex_YearField class attributes and methods

# YearValue class attributes and methods

# bibtex_BibtexKeyField class attributes and methods

# bibtex_JournalField class attributes and methods

# bibtex_VolumeField class attributes and methods

# bibtex_PageField class attributes and methods

# bibtex_SeriesField class attributes and methods

# bibtex_AddressField class attributes and methods

# bibtex_MonthField class attributes and methods

# bibtex_OrganizationField class attributes and methods

# bibtex_NoteField class attributes and methods

# bibtex_PublisherField class attributes and methods

# bibtex_PartField class attributes and methods

# bibtex_EidField class attributes and methods

# bibtex_UrlField class attributes and methods

# bibtex_Keyword class attributes and methods

# bibtex_KeywordField class attributes and methods

# bibtex_AbstractField class attributes and methods

# bibtex_ReviewField class attributes and methods

# bibtex_Entry class attributes and methods
bibtex_Entry_m_getGeneralFields: Method = Method(name="getGeneralFields", parameters={}, type=Field)
bibtex_Entry_m_getFields: Method = Method(name="getFields", parameters={}, type=Field)
bibtex_Entry.methods={bibtex_Entry_m_getGeneralFields, bibtex_Entry_m_getFields}

# bibtex_InProceedingsEntry class attributes and methods
bibtex_InProceedingsEntry_m_getFields: Method = Method(name="getFields", parameters={}, type=Field)
bibtex_InProceedingsEntry.methods={bibtex_InProceedingsEntry_m_getFields}

# Entry class attributes and methods

# bibtex_ArticleEntry class attributes and methods
bibtex_ArticleEntry_m_getFields: Method = Method(name="getFields", parameters={}, type=Field)
bibtex_ArticleEntry.methods={bibtex_ArticleEntry_m_getFields}

# bibtex_Bibliography class attributes and methods

# Relationships
authors0: BinaryAssociation = BinaryAssociation(
    name="authors0",
    ends={
        Property(name="bibtex_Author", type=bibtex_AuthorField, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_AuthorField", type=bibtex_Author, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
editors1: BinaryAssociation = BinaryAssociation(
    name="editors1",
    ends={
        Property(name="bibtex_Editor", type=bibtex_EditorField, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_EditorField", type=bibtex_Editor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fromPage2: BinaryAssociation = BinaryAssociation(
    name="fromPage2",
    ends={
        Property(name="bibtex_Page", type=bibtex_PageField, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_PageField", type=bibtex_Page, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
toPage3: BinaryAssociation = BinaryAssociation(
    name="toPage3",
    ends={
        Property(name="bibtex_Page5", type=bibtex_PageField, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_PageField4", type=bibtex_Page, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keywords6: BinaryAssociation = BinaryAssociation(
    name="keywords6",
    ends={
        Property(name="bibtex_Keyword", type=bibtex_KeywordField, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_KeywordField", type=bibtex_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bookTitle21: BinaryAssociation = BinaryAssociation(
    name="bookTitle21",
    ends={
        Property(name="bibtex_BookTitleField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry22", type=bibtex_BookTitleField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bibtexKey7: BinaryAssociation = BinaryAssociation(
    name="bibtexKey7",
    ends={
        Property(name="bibtex_BibtexKeyField", type=bibtex_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Entry", type=bibtex_BibtexKeyField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
abstract8: BinaryAssociation = BinaryAssociation(
    name="abstract8",
    ends={
        Property(name="bibtex_AbstractField", type=bibtex_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Entry9", type=bibtex_AbstractField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
url10: BinaryAssociation = BinaryAssociation(
    name="url10",
    ends={
        Property(name="bibtex_UrlField", type=bibtex_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Entry11", type=bibtex_UrlField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyword12: BinaryAssociation = BinaryAssociation(
    name="keyword12",
    ends={
        Property(name="bibtex_KeywordField14", type=bibtex_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Entry13", type=bibtex_KeywordField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
review15: BinaryAssociation = BinaryAssociation(
    name="review15",
    ends={
        Property(name="bibtex_ReviewField", type=bibtex_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Entry16", type=bibtex_ReviewField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author17: BinaryAssociation = BinaryAssociation(
    name="author17",
    ends={
        Property(name="bibtex_AuthorField18", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry", type=bibtex_AuthorField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
title19: BinaryAssociation = BinaryAssociation(
    name="title19",
    ends={
        Property(name="bibtex_TitleField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry20", type=bibtex_TitleField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
year23: BinaryAssociation = BinaryAssociation(
    name="year23",
    ends={
        Property(name="bibtex_YearField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry24", type=bibtex_YearField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
editor25: BinaryAssociation = BinaryAssociation(
    name="editor25",
    ends={
        Property(name="bibtex_EditorField27", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry26", type=bibtex_EditorField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pages28: BinaryAssociation = BinaryAssociation(
    name="pages28",
    ends={
        Property(name="bibtex_PageField30", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry29", type=bibtex_PageField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
volume31: BinaryAssociation = BinaryAssociation(
    name="volume31",
    ends={
        Property(name="bibtex_VolumeField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry32", type=bibtex_VolumeField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number33: BinaryAssociation = BinaryAssociation(
    name="number33",
    ends={
        Property(name="bibtex_NumberField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry34", type=bibtex_NumberField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
series35: BinaryAssociation = BinaryAssociation(
    name="series35",
    ends={
        Property(name="bibtex_SeriesField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry36", type=bibtex_SeriesField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address37: BinaryAssociation = BinaryAssociation(
    name="address37",
    ends={
        Property(name="bibtex_AddressField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry38", type=bibtex_AddressField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
month39: BinaryAssociation = BinaryAssociation(
    name="month39",
    ends={
        Property(name="bibtex_MonthField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry40", type=bibtex_MonthField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization41: BinaryAssociation = BinaryAssociation(
    name="organization41",
    ends={
        Property(name="bibtex_OrganizationField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry42", type=bibtex_OrganizationField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
volume60: BinaryAssociation = BinaryAssociation(
    name="volume60",
    ends={
        Property(name="bibtex_VolumeField62", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry61", type=bibtex_VolumeField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
note43: BinaryAssociation = BinaryAssociation(
    name="note43",
    ends={
        Property(name="bibtex_NoteField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry44", type=bibtex_NoteField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number63: BinaryAssociation = BinaryAssociation(
    name="number63",
    ends={
        Property(name="bibtex_NumberField65", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry64", type=bibtex_NumberField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publisher45: BinaryAssociation = BinaryAssociation(
    name="publisher45",
    ends={
        Property(name="bibtex_PublisherField", type=bibtex_InProceedingsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_InProceedingsEntry46", type=bibtex_PublisherField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
month66: BinaryAssociation = BinaryAssociation(
    name="month66",
    ends={
        Property(name="bibtex_MonthField68", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry67", type=bibtex_MonthField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
note69: BinaryAssociation = BinaryAssociation(
    name="note69",
    ends={
        Property(name="bibtex_NoteField71", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry70", type=bibtex_NoteField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part72: BinaryAssociation = BinaryAssociation(
    name="part72",
    ends={
        Property(name="bibtex_PartField", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry73", type=bibtex_PartField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author47: BinaryAssociation = BinaryAssociation(
    name="author47",
    ends={
        Property(name="bibtex_AuthorField48", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry", type=bibtex_AuthorField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
title49: BinaryAssociation = BinaryAssociation(
    name="title49",
    ends={
        Property(name="bibtex_TitleField51", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry50", type=bibtex_TitleField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
year52: BinaryAssociation = BinaryAssociation(
    name="year52",
    ends={
        Property(name="bibtex_YearField54", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry53", type=bibtex_YearField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
journal55: BinaryAssociation = BinaryAssociation(
    name="journal55",
    ends={
        Property(name="bibtex_JournalField", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry56", type=bibtex_JournalField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pages57: BinaryAssociation = BinaryAssociation(
    name="pages57",
    ends={
        Property(name="bibtex_PageField59", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry58", type=bibtex_PageField, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eid74: BinaryAssociation = BinaryAssociation(
    name="eid74",
    ends={
        Property(name="bibtex_EidField", type=bibtex_ArticleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_ArticleEntry75", type=bibtex_EidField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries76: BinaryAssociation = BinaryAssociation(
    name="entries76",
    ends={
        Property(name="bibtex_Entry77", type=bibtex_Bibliography, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Bibliography", type=bibtex_Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_bibtex_Author_Person = Generalization(general=Person, specific=bibtex_Author)
gen_bibtex_Editor_Person = Generalization(general=Person, specific=bibtex_Editor)
gen_bibtex_NumberField_Field = Generalization(general=Field, specific=bibtex_NumberField)
gen_bibtex_Page_IntValue = Generalization(general=IntValue, specific=bibtex_Page)
gen_bibtex_AuthorField_Field = Generalization(general=Field, specific=bibtex_AuthorField)
gen_bibtex_EditorField_Field = Generalization(general=Field, specific=bibtex_EditorField)
gen_bibtex_TitleField_Field = Generalization(general=Field, specific=bibtex_TitleField)
gen_bibtex_TitleField_StringValue = Generalization(general=StringValue, specific=bibtex_TitleField)
gen_bibtex_BookTitleField_Field = Generalization(general=Field, specific=bibtex_BookTitleField)
gen_bibtex_BookTitleField_StringValue = Generalization(general=StringValue, specific=bibtex_BookTitleField)
gen_bibtex_NumberField_IntValue = Generalization(general=IntValue, specific=bibtex_NumberField)
gen_bibtex_NoteField_StringValue = Generalization(general=StringValue, specific=bibtex_NoteField)
gen_bibtex_YearField_Field = Generalization(general=Field, specific=bibtex_YearField)
gen_bibtex_YearField_YearValue = Generalization(general=YearValue, specific=bibtex_YearField)
gen_bibtex_BibtexKeyField_Field = Generalization(general=Field, specific=bibtex_BibtexKeyField)
gen_bibtex_BibtexKeyField_StringValue = Generalization(general=StringValue, specific=bibtex_BibtexKeyField)
gen_bibtex_JournalField_Field = Generalization(general=Field, specific=bibtex_JournalField)
gen_bibtex_JournalField_StringValue = Generalization(general=StringValue, specific=bibtex_JournalField)
gen_bibtex_VolumeField_Field = Generalization(general=Field, specific=bibtex_VolumeField)
gen_bibtex_VolumeField_IntValue = Generalization(general=IntValue, specific=bibtex_VolumeField)
gen_bibtex_PageField_Field = Generalization(general=Field, specific=bibtex_PageField)
gen_bibtex_SeriesField_StringValue = Generalization(general=StringValue, specific=bibtex_SeriesField)
gen_bibtex_SeriesField_Field = Generalization(general=Field, specific=bibtex_SeriesField)
gen_bibtex_AddressField_Field = Generalization(general=Field, specific=bibtex_AddressField)
gen_bibtex_AddressField_StringValue = Generalization(general=StringValue, specific=bibtex_AddressField)
gen_bibtex_MonthField_Field = Generalization(general=Field, specific=bibtex_MonthField)
gen_bibtex_MonthField_StringValue = Generalization(general=StringValue, specific=bibtex_MonthField)
gen_bibtex_OrganizationField_Field = Generalization(general=Field, specific=bibtex_OrganizationField)
gen_bibtex_OrganizationField_StringValue = Generalization(general=StringValue, specific=bibtex_OrganizationField)
gen_bibtex_NoteField_Field = Generalization(general=Field, specific=bibtex_NoteField)
gen_bibtex_PublisherField_Field = Generalization(general=Field, specific=bibtex_PublisherField)
gen_bibtex_PublisherField_StringValue = Generalization(general=StringValue, specific=bibtex_PublisherField)
gen_bibtex_PartField_IntValue = Generalization(general=IntValue, specific=bibtex_PartField)
gen_bibtex_PartField_Field = Generalization(general=Field, specific=bibtex_PartField)
gen_bibtex_EidField_Field = Generalization(general=Field, specific=bibtex_EidField)
gen_bibtex_EidField_StringValue = Generalization(general=StringValue, specific=bibtex_EidField)
gen_bibtex_UrlField_StringValue = Generalization(general=StringValue, specific=bibtex_UrlField)
gen_bibtex_UrlField_Field = Generalization(general=Field, specific=bibtex_UrlField)
gen_bibtex_Keyword_StringValue = Generalization(general=StringValue, specific=bibtex_Keyword)
gen_bibtex_KeywordField_Field = Generalization(general=Field, specific=bibtex_KeywordField)
gen_bibtex_AbstractField_StringValue = Generalization(general=StringValue, specific=bibtex_AbstractField)
gen_bibtex_AbstractField_Field = Generalization(general=Field, specific=bibtex_AbstractField)
gen_bibtex_ReviewField_StringValue = Generalization(general=StringValue, specific=bibtex_ReviewField)
gen_bibtex_ReviewField_Field = Generalization(general=Field, specific=bibtex_ReviewField)
gen_bibtex_InProceedingsEntry_Entry = Generalization(general=Entry, specific=bibtex_InProceedingsEntry)
gen_bibtex_ArticleEntry_Entry = Generalization(general=Entry, specific=bibtex_ArticleEntry)

# Domain Model
domain_model = DomainModel(
    name="bibtex",
    types={bibtex_Person, bibtex_Author, Person, bibtex_Editor, bibtex_StringValue, bibtex_YearValue, bibtex_IntValue, bibtex_Page, IntValue, bibtex_Field, bibtex_AuthorField, Field, bibtex_EditorField, bibtex_TitleField, StringValue, bibtex_BookTitleField, bibtex_NumberField, bibtex_YearField, YearValue, bibtex_BibtexKeyField, bibtex_JournalField, bibtex_VolumeField, bibtex_PageField, bibtex_SeriesField, bibtex_AddressField, bibtex_MonthField, bibtex_OrganizationField, bibtex_NoteField, bibtex_PublisherField, bibtex_PartField, bibtex_EidField, bibtex_UrlField, bibtex_Keyword, bibtex_KeywordField, bibtex_AbstractField, bibtex_ReviewField, bibtex_Entry, bibtex_InProceedingsEntry, Entry, bibtex_ArticleEntry, bibtex_Bibliography},
    associations={authors0, editors1, fromPage2, toPage3, keywords6, bookTitle21, bibtexKey7, abstract8, url10, keyword12, review15, author17, title19, year23, editor25, pages28, volume31, number33, series35, address37, month39, organization41, volume60, note43, number63, publisher45, month66, note69, part72, author47, title49, year52, journal55, pages57, eid74, entries76},
    generalizations={gen_bibtex_Author_Person, gen_bibtex_Editor_Person, gen_bibtex_NumberField_Field, gen_bibtex_Page_IntValue, gen_bibtex_AuthorField_Field, gen_bibtex_EditorField_Field, gen_bibtex_TitleField_Field, gen_bibtex_TitleField_StringValue, gen_bibtex_BookTitleField_Field, gen_bibtex_BookTitleField_StringValue, gen_bibtex_NumberField_IntValue, gen_bibtex_NoteField_StringValue, gen_bibtex_YearField_Field, gen_bibtex_YearField_YearValue, gen_bibtex_BibtexKeyField_Field, gen_bibtex_BibtexKeyField_StringValue, gen_bibtex_JournalField_Field, gen_bibtex_JournalField_StringValue, gen_bibtex_VolumeField_Field, gen_bibtex_VolumeField_IntValue, gen_bibtex_PageField_Field, gen_bibtex_SeriesField_StringValue, gen_bibtex_SeriesField_Field, gen_bibtex_AddressField_Field, gen_bibtex_AddressField_StringValue, gen_bibtex_MonthField_Field, gen_bibtex_MonthField_StringValue, gen_bibtex_OrganizationField_Field, gen_bibtex_OrganizationField_StringValue, gen_bibtex_NoteField_Field, gen_bibtex_PublisherField_Field, gen_bibtex_PublisherField_StringValue, gen_bibtex_PartField_IntValue, gen_bibtex_PartField_Field, gen_bibtex_EidField_Field, gen_bibtex_EidField_StringValue, gen_bibtex_UrlField_StringValue, gen_bibtex_UrlField_Field, gen_bibtex_Keyword_StringValue, gen_bibtex_KeywordField_Field, gen_bibtex_AbstractField_StringValue, gen_bibtex_AbstractField_Field, gen_bibtex_ReviewField_StringValue, gen_bibtex_ReviewField_Field, gen_bibtex_InProceedingsEntry_Entry, gen_bibtex_ArticleEntry_Entry},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)