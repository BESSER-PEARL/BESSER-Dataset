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
bibtex_Model = Class(name="bibtex_Model")
bibtex_BibType = Class(name="bibtex_BibType")
bibtex_CiteKey = Class(name="bibtex_CiteKey")
bibtex_Title = Class(name="bibtex_Title")
bibtex_Year = Class(name="bibtex_Year")
bibtex_Month = Class(name="bibtex_Month")
bibtex_Key = Class(name="bibtex_Key")
bibtex_Article = Class(name="bibtex_Article")
BibType = Class(name="BibType")
bibtex_Author = Class(name="bibtex_Author")
bibtex_Note = Class(name="bibtex_Note")
bibtex_Volume = Class(name="bibtex_Volume")
bibtex_Number = Class(name="bibtex_Number")
bibtex_Pages = Class(name="bibtex_Pages")
bibtex_Book = Class(name="bibtex_Book")
bibtex_Publisher = Class(name="bibtex_Publisher")
bibtex_Journal = Class(name="bibtex_Journal")
bibtex_Series = Class(name="bibtex_Series")
bibtex_Address = Class(name="bibtex_Address")
bibtex_Editor = Class(name="bibtex_Editor")
bibtex_Edition = Class(name="bibtex_Edition")
bibtex_Booklet = Class(name="bibtex_Booklet")
bibtex_Howpublished = Class(name="bibtex_Howpublished")
bibtex_Conference = Class(name="bibtex_Conference")
bibtex_Booktitle = Class(name="bibtex_Booktitle")
bibtex_Organization = Class(name="bibtex_Organization")
bibtex_Chapter = Class(name="bibtex_Chapter")
bibtex_Inbook = Class(name="bibtex_Inbook")
bibtex_Incollection = Class(name="bibtex_Incollection")
bibtex_Inproceedings = Class(name="bibtex_Inproceedings")
bibtex_Mastersthesis = Class(name="bibtex_Mastersthesis")
bibtex_Manual = Class(name="bibtex_Manual")
bibtex_School = Class(name="bibtex_School")
bibtex_Misc = Class(name="bibtex_Misc")
bibtex_Phdthesis = Class(name="bibtex_Phdthesis")
bibtex_Proceedings = Class(name="bibtex_Proceedings")
bibtex_Institution = Class(name="bibtex_Institution")
bibtex_Type = Class(name="bibtex_Type")
bibtex_Techreport = Class(name="bibtex_Techreport")
bibtex_Crossref = Class(name="bibtex_Crossref")
bibtex_Unpublished = Class(name="bibtex_Unpublished")

# bibtex_Model class attributes and methods

# bibtex_BibType class attributes and methods

# bibtex_CiteKey class attributes and methods
bibtex_CiteKey_citeKey: Property = Property(name="citeKey", type=StringType)
bibtex_CiteKey.attributes={bibtex_CiteKey_citeKey}

# bibtex_Title class attributes and methods
bibtex_Title_title: Property = Property(name="title", type=StringType)
bibtex_Title.attributes={bibtex_Title_title}

# bibtex_Year class attributes and methods
bibtex_Year_year: Property = Property(name="year", type=StringType)
bibtex_Year.attributes={bibtex_Year_year}

# bibtex_Month class attributes and methods
bibtex_Month_month: Property = Property(name="month", type=StringType)
bibtex_Month.attributes={bibtex_Month_month}

# bibtex_Key class attributes and methods
bibtex_Key_key: Property = Property(name="key", type=StringType)
bibtex_Key.attributes={bibtex_Key_key}

# bibtex_Article class attributes and methods

# BibType class attributes and methods

# bibtex_Author class attributes and methods
bibtex_Author_author: Property = Property(name="author", type=StringType)
bibtex_Author.attributes={bibtex_Author_author}

# bibtex_Note class attributes and methods
bibtex_Note_note: Property = Property(name="note", type=StringType)
bibtex_Note.attributes={bibtex_Note_note}

# bibtex_Volume class attributes and methods
bibtex_Volume_volume: Property = Property(name="volume", type=StringType)
bibtex_Volume.attributes={bibtex_Volume_volume}

# bibtex_Number class attributes and methods
bibtex_Number_number: Property = Property(name="number", type=StringType)
bibtex_Number.attributes={bibtex_Number_number}

# bibtex_Pages class attributes and methods
bibtex_Pages_pages: Property = Property(name="pages", type=StringType)
bibtex_Pages.attributes={bibtex_Pages_pages}

# bibtex_Book class attributes and methods

# bibtex_Publisher class attributes and methods
bibtex_Publisher_publisher: Property = Property(name="publisher", type=StringType)
bibtex_Publisher.attributes={bibtex_Publisher_publisher}

# bibtex_Journal class attributes and methods
bibtex_Journal_journal: Property = Property(name="journal", type=StringType)
bibtex_Journal.attributes={bibtex_Journal_journal}

# bibtex_Series class attributes and methods
bibtex_Series_series: Property = Property(name="series", type=StringType)
bibtex_Series.attributes={bibtex_Series_series}

# bibtex_Address class attributes and methods
bibtex_Address_address: Property = Property(name="address", type=StringType)
bibtex_Address.attributes={bibtex_Address_address}

# bibtex_Editor class attributes and methods
bibtex_Editor_editor: Property = Property(name="editor", type=StringType)
bibtex_Editor.attributes={bibtex_Editor_editor}

# bibtex_Edition class attributes and methods
bibtex_Edition_edition: Property = Property(name="edition", type=StringType)
bibtex_Edition.attributes={bibtex_Edition_edition}

# bibtex_Booklet class attributes and methods

# bibtex_Howpublished class attributes and methods
bibtex_Howpublished_howpublished: Property = Property(name="howpublished", type=StringType)
bibtex_Howpublished.attributes={bibtex_Howpublished_howpublished}

# bibtex_Conference class attributes and methods

# bibtex_Booktitle class attributes and methods
bibtex_Booktitle_booktitle: Property = Property(name="booktitle", type=StringType)
bibtex_Booktitle.attributes={bibtex_Booktitle_booktitle}

# bibtex_Organization class attributes and methods
bibtex_Organization_organization: Property = Property(name="organization", type=StringType)
bibtex_Organization.attributes={bibtex_Organization_organization}

# bibtex_Chapter class attributes and methods
bibtex_Chapter_chapter: Property = Property(name="chapter", type=StringType)
bibtex_Chapter.attributes={bibtex_Chapter_chapter}

# bibtex_Inbook class attributes and methods
bibtex_Inbook_author: Property = Property(name="author", type=BooleanType)
bibtex_Inbook_editor: Property = Property(name="editor", type=BooleanType)
bibtex_Inbook.attributes={bibtex_Inbook_author, bibtex_Inbook_editor}

# bibtex_Incollection class attributes and methods

# bibtex_Inproceedings class attributes and methods

# bibtex_Mastersthesis class attributes and methods

# bibtex_Manual class attributes and methods

# bibtex_School class attributes and methods
bibtex_School_school: Property = Property(name="school", type=StringType)
bibtex_School.attributes={bibtex_School_school}

# bibtex_Misc class attributes and methods

# bibtex_Phdthesis class attributes and methods

# bibtex_Proceedings class attributes and methods

# bibtex_Institution class attributes and methods
bibtex_Institution_institution: Property = Property(name="institution", type=StringType)
bibtex_Institution.attributes={bibtex_Institution_institution}

# bibtex_Type class attributes and methods
bibtex_Type_type: Property = Property(name="type", type=StringType)
bibtex_Type.attributes={bibtex_Type_type}

# bibtex_Techreport class attributes and methods

# bibtex_Crossref class attributes and methods
bibtex_Crossref_crossref: Property = Property(name="crossref", type=StringType)
bibtex_Crossref.attributes={bibtex_Crossref_crossref}

# bibtex_Unpublished class attributes and methods

# Relationships
bibEntry0: BinaryAssociation = BinaryAssociation(
    name="bibEntry0",
    ends={
        Property(name="bibtex_BibType", type=bibtex_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Model", type=bibtex_BibType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citeKey1: BinaryAssociation = BinaryAssociation(
    name="citeKey1",
    ends={
        Property(name="bibtex_CiteKey", type=bibtex_BibType, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_BibType2", type=bibtex_CiteKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title3: BinaryAssociation = BinaryAssociation(
    name="title3",
    ends={
        Property(name="bibtex_Title", type=bibtex_BibType, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_BibType4", type=bibtex_Title, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
year5: BinaryAssociation = BinaryAssociation(
    name="year5",
    ends={
        Property(name="bibtex_Year", type=bibtex_BibType, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_BibType6", type=bibtex_Year, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key11: BinaryAssociation = BinaryAssociation(
    name="key11",
    ends={
        Property(name="bibtex_Key", type=bibtex_BibType, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_BibType12", type=bibtex_Key, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author13: BinaryAssociation = BinaryAssociation(
    name="author13",
    ends={
        Property(name="bibtex_Author", type=bibtex_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Article", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
month7: BinaryAssociation = BinaryAssociation(
    name="month7",
    ends={
        Property(name="bibtex_Month", type=bibtex_BibType, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_BibType8", type=bibtex_Month, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
note9: BinaryAssociation = BinaryAssociation(
    name="note9",
    ends={
        Property(name="bibtex_Note", type=bibtex_BibType, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_BibType10", type=bibtex_Note, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
volume16: BinaryAssociation = BinaryAssociation(
    name="volume16",
    ends={
        Property(name="bibtex_Volume", type=bibtex_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Article17", type=bibtex_Volume, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number18: BinaryAssociation = BinaryAssociation(
    name="number18",
    ends={
        Property(name="bibtex_Number", type=bibtex_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Article19", type=bibtex_Number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pages20: BinaryAssociation = BinaryAssociation(
    name="pages20",
    ends={
        Property(name="bibtex_Pages", type=bibtex_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Article21", type=bibtex_Pages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publisher22: BinaryAssociation = BinaryAssociation(
    name="publisher22",
    ends={
        Property(name="bibtex_Publisher", type=bibtex_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Book", type=bibtex_Publisher, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
journal14: BinaryAssociation = BinaryAssociation(
    name="journal14",
    ends={
        Property(name="bibtex_Journal", type=bibtex_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Article15", type=bibtex_Journal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
editor26: BinaryAssociation = BinaryAssociation(
    name="editor26",
    ends={
        Property(name="bibtex_Book27", type=bibtex_Editor, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="bibtex_Editor", type=bibtex_Book, multiplicity=Multiplicity(1, 1))
    }
)
volume28: BinaryAssociation = BinaryAssociation(
    name="volume28",
    ends={
        Property(name="bibtex_Volume30", type=bibtex_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Book29", type=bibtex_Volume, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
series31: BinaryAssociation = BinaryAssociation(
    name="series31",
    ends={
        Property(name="bibtex_Series", type=bibtex_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Book32", type=bibtex_Series, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address33: BinaryAssociation = BinaryAssociation(
    name="address33",
    ends={
        Property(name="bibtex_Address", type=bibtex_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Book34", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author23: BinaryAssociation = BinaryAssociation(
    name="author23",
    ends={
        Property(name="bibtex_Author25", type=bibtex_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Book24", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edition35: BinaryAssociation = BinaryAssociation(
    name="edition35",
    ends={
        Property(name="bibtex_Edition", type=bibtex_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Book36", type=bibtex_Edition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author37: BinaryAssociation = BinaryAssociation(
    name="author37",
    ends={
        Property(name="bibtex_Author38", type=bibtex_Booklet, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Booklet", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
howpublished39: BinaryAssociation = BinaryAssociation(
    name="howpublished39",
    ends={
        Property(name="bibtex_Howpublished", type=bibtex_Booklet, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Booklet40", type=bibtex_Howpublished, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address41: BinaryAssociation = BinaryAssociation(
    name="address41",
    ends={
        Property(name="bibtex_Address43", type=bibtex_Booklet, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Booklet42", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
booktitle46: BinaryAssociation = BinaryAssociation(
    name="booktitle46",
    ends={
        Property(name="bibtex_Booktitle", type=bibtex_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Conference47", type=bibtex_Booktitle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address59: BinaryAssociation = BinaryAssociation(
    name="address59",
    ends={
        Property(name="bibtex_Address61", type=bibtex_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Conference60", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
editor48: BinaryAssociation = BinaryAssociation(
    name="editor48",
    ends={
        Property(name="bibtex_Editor50", type=bibtex_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Conference49", type=bibtex_Editor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pages51: BinaryAssociation = BinaryAssociation(
    name="pages51",
    ends={
        Property(name="bibtex_Pages53", type=bibtex_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Conference52", type=bibtex_Pages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization54: BinaryAssociation = BinaryAssociation(
    name="organization54",
    ends={
        Property(name="bibtex_Organization", type=bibtex_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Conference55", type=bibtex_Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publisher56: BinaryAssociation = BinaryAssociation(
    name="publisher56",
    ends={
        Property(name="bibtex_Publisher58", type=bibtex_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Conference57", type=bibtex_Publisher, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author44: BinaryAssociation = BinaryAssociation(
    name="author44",
    ends={
        Property(name="bibtex_Author45", type=bibtex_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Conference", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
chapter64: BinaryAssociation = BinaryAssociation(
    name="chapter64",
    ends={
        Property(name="bibtex_Chapter", type=bibtex_Inbook, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inbook65", type=bibtex_Chapter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publisher62: BinaryAssociation = BinaryAssociation(
    name="publisher62",
    ends={
        Property(name="bibtex_Publisher63", type=bibtex_Inbook, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inbook", type=bibtex_Publisher, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
series72: BinaryAssociation = BinaryAssociation(
    name="series72",
    ends={
        Property(name="bibtex_Series74", type=bibtex_Inbook, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inbook73", type=bibtex_Series, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pages66: BinaryAssociation = BinaryAssociation(
    name="pages66",
    ends={
        Property(name="bibtex_Pages68", type=bibtex_Inbook, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inbook67", type=bibtex_Pages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
volume69: BinaryAssociation = BinaryAssociation(
    name="volume69",
    ends={
        Property(name="bibtex_Volume71", type=bibtex_Inbook, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inbook70", type=bibtex_Volume, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author81: BinaryAssociation = BinaryAssociation(
    name="author81",
    ends={
        Property(name="bibtex_Author82", type=bibtex_Incollection, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Incollection", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
booktitle83: BinaryAssociation = BinaryAssociation(
    name="booktitle83",
    ends={
        Property(name="bibtex_Booktitle85", type=bibtex_Incollection, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Incollection84", type=bibtex_Booktitle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address75: BinaryAssociation = BinaryAssociation(
    name="address75",
    ends={
        Property(name="bibtex_Address77", type=bibtex_Inbook, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inbook76", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edition78: BinaryAssociation = BinaryAssociation(
    name="edition78",
    ends={
        Property(name="bibtex_Edition80", type=bibtex_Inbook, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inbook79", type=bibtex_Edition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publisher95: BinaryAssociation = BinaryAssociation(
    name="publisher95",
    ends={
        Property(name="bibtex_Publisher97", type=bibtex_Incollection, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Incollection96", type=bibtex_Publisher, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
editor86: BinaryAssociation = BinaryAssociation(
    name="editor86",
    ends={
        Property(name="bibtex_Editor88", type=bibtex_Incollection, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Incollection87", type=bibtex_Editor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address98: BinaryAssociation = BinaryAssociation(
    name="address98",
    ends={
        Property(name="bibtex_Address100", type=bibtex_Incollection, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Incollection99", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pages89: BinaryAssociation = BinaryAssociation(
    name="pages89",
    ends={
        Property(name="bibtex_Pages91", type=bibtex_Incollection, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Incollection90", type=bibtex_Pages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization92: BinaryAssociation = BinaryAssociation(
    name="organization92",
    ends={
        Property(name="bibtex_Organization94", type=bibtex_Incollection, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Incollection93", type=bibtex_Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
series109: BinaryAssociation = BinaryAssociation(
    name="series109",
    ends={
        Property(name="bibtex_Series111", type=bibtex_Inproceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inproceedings110", type=bibtex_Series, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author101: BinaryAssociation = BinaryAssociation(
    name="author101",
    ends={
        Property(name="bibtex_Author102", type=bibtex_Inproceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inproceedings", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
booktitle103: BinaryAssociation = BinaryAssociation(
    name="booktitle103",
    ends={
        Property(name="bibtex_Booktitle105", type=bibtex_Inproceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inproceedings104", type=bibtex_Booktitle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
editor106: BinaryAssociation = BinaryAssociation(
    name="editor106",
    ends={
        Property(name="bibtex_Editor108", type=bibtex_Inproceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inproceedings107", type=bibtex_Editor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pages112: BinaryAssociation = BinaryAssociation(
    name="pages112",
    ends={
        Property(name="bibtex_Pages114", type=bibtex_Inproceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inproceedings113", type=bibtex_Pages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization115: BinaryAssociation = BinaryAssociation(
    name="organization115",
    ends={
        Property(name="bibtex_Organization117", type=bibtex_Inproceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inproceedings116", type=bibtex_Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publisher118: BinaryAssociation = BinaryAssociation(
    name="publisher118",
    ends={
        Property(name="bibtex_Publisher120", type=bibtex_Inproceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inproceedings119", type=bibtex_Publisher, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address121: BinaryAssociation = BinaryAssociation(
    name="address121",
    ends={
        Property(name="bibtex_Address123", type=bibtex_Inproceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Inproceedings122", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author124: BinaryAssociation = BinaryAssociation(
    name="author124",
    ends={
        Property(name="bibtex_Author125", type=bibtex_Manual, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Manual", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization126: BinaryAssociation = BinaryAssociation(
    name="organization126",
    ends={
        Property(name="bibtex_Organization128", type=bibtex_Manual, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Manual127", type=bibtex_Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address129: BinaryAssociation = BinaryAssociation(
    name="address129",
    ends={
        Property(name="bibtex_Address131", type=bibtex_Manual, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Manual130", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edition132: BinaryAssociation = BinaryAssociation(
    name="edition132",
    ends={
        Property(name="bibtex_Edition134", type=bibtex_Manual, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Manual133", type=bibtex_Edition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author142: BinaryAssociation = BinaryAssociation(
    name="author142",
    ends={
        Property(name="bibtex_Author143", type=bibtex_Misc, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Misc", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author135: BinaryAssociation = BinaryAssociation(
    name="author135",
    ends={
        Property(name="bibtex_Author136", type=bibtex_Mastersthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Mastersthesis", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
school137: BinaryAssociation = BinaryAssociation(
    name="school137",
    ends={
        Property(name="bibtex_School", type=bibtex_Mastersthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Mastersthesis138", type=bibtex_School, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address139: BinaryAssociation = BinaryAssociation(
    name="address139",
    ends={
        Property(name="bibtex_Address141", type=bibtex_Mastersthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Mastersthesis140", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
school149: BinaryAssociation = BinaryAssociation(
    name="school149",
    ends={
        Property(name="bibtex_School151", type=bibtex_Phdthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Phdthesis150", type=bibtex_School, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
howpublished144: BinaryAssociation = BinaryAssociation(
    name="howpublished144",
    ends={
        Property(name="bibtex_Howpublished146", type=bibtex_Misc, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Misc145", type=bibtex_Howpublished, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author147: BinaryAssociation = BinaryAssociation(
    name="author147",
    ends={
        Property(name="bibtex_Author148", type=bibtex_Phdthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Phdthesis", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
editor155: BinaryAssociation = BinaryAssociation(
    name="editor155",
    ends={
        Property(name="bibtex_Editor156", type=bibtex_Proceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Proceedings", type=bibtex_Editor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publisher157: BinaryAssociation = BinaryAssociation(
    name="publisher157",
    ends={
        Property(name="bibtex_Publisher159", type=bibtex_Proceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Proceedings158", type=bibtex_Publisher, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization160: BinaryAssociation = BinaryAssociation(
    name="organization160",
    ends={
        Property(name="bibtex_Organization162", type=bibtex_Proceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Proceedings161", type=bibtex_Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address152: BinaryAssociation = BinaryAssociation(
    name="address152",
    ends={
        Property(name="bibtex_Address154", type=bibtex_Phdthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Phdthesis153", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
institution168: BinaryAssociation = BinaryAssociation(
    name="institution168",
    ends={
        Property(name="bibtex_Institution", type=bibtex_Techreport, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Techreport169", type=bibtex_Institution, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type170: BinaryAssociation = BinaryAssociation(
    name="type170",
    ends={
        Property(name="bibtex_Type", type=bibtex_Techreport, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Techreport171", type=bibtex_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number172: BinaryAssociation = BinaryAssociation(
    name="number172",
    ends={
        Property(name="bibtex_Number174", type=bibtex_Techreport, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Techreport173", type=bibtex_Number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address163: BinaryAssociation = BinaryAssociation(
    name="address163",
    ends={
        Property(name="bibtex_Address165", type=bibtex_Proceedings, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Proceedings164", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author166: BinaryAssociation = BinaryAssociation(
    name="author166",
    ends={
        Property(name="bibtex_Author167", type=bibtex_Techreport, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Techreport", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address175: BinaryAssociation = BinaryAssociation(
    name="address175",
    ends={
        Property(name="bibtex_Address177", type=bibtex_Techreport, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Techreport176", type=bibtex_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author178: BinaryAssociation = BinaryAssociation(
    name="author178",
    ends={
        Property(name="bibtex_Author179", type=bibtex_Unpublished, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Unpublished", type=bibtex_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_bibtex_Article_BibType = Generalization(general=BibType, specific=bibtex_Article)
gen_bibtex_Book_BibType = Generalization(general=BibType, specific=bibtex_Book)
gen_bibtex_Booklet_BibType = Generalization(general=BibType, specific=bibtex_Booklet)
gen_bibtex_Conference_BibType = Generalization(general=BibType, specific=bibtex_Conference)
gen_bibtex_Inbook_BibType = Generalization(general=BibType, specific=bibtex_Inbook)
gen_bibtex_Incollection_BibType = Generalization(general=BibType, specific=bibtex_Incollection)
gen_bibtex_Inproceedings_BibType = Generalization(general=BibType, specific=bibtex_Inproceedings)
gen_bibtex_Mastersthesis_BibType = Generalization(general=BibType, specific=bibtex_Mastersthesis)
gen_bibtex_Manual_BibType = Generalization(general=BibType, specific=bibtex_Manual)
gen_bibtex_Misc_BibType = Generalization(general=BibType, specific=bibtex_Misc)
gen_bibtex_Phdthesis_BibType = Generalization(general=BibType, specific=bibtex_Phdthesis)
gen_bibtex_Proceedings_BibType = Generalization(general=BibType, specific=bibtex_Proceedings)
gen_bibtex_Techreport_BibType = Generalization(general=BibType, specific=bibtex_Techreport)
gen_bibtex_Unpublished_BibType = Generalization(general=BibType, specific=bibtex_Unpublished)

# Domain Model
domain_model = DomainModel(
    name="bibtex",
    types={bibtex_Model, bibtex_BibType, bibtex_CiteKey, bibtex_Title, bibtex_Year, bibtex_Month, bibtex_Key, bibtex_Article, BibType, bibtex_Author, bibtex_Note, bibtex_Volume, bibtex_Number, bibtex_Pages, bibtex_Book, bibtex_Publisher, bibtex_Journal, bibtex_Series, bibtex_Address, bibtex_Editor, bibtex_Edition, bibtex_Booklet, bibtex_Howpublished, bibtex_Conference, bibtex_Booktitle, bibtex_Organization, bibtex_Chapter, bibtex_Inbook, bibtex_Incollection, bibtex_Inproceedings, bibtex_Mastersthesis, bibtex_Manual, bibtex_School, bibtex_Misc, bibtex_Phdthesis, bibtex_Proceedings, bibtex_Institution, bibtex_Type, bibtex_Techreport, bibtex_Crossref, bibtex_Unpublished},
    associations={bibEntry0, citeKey1, title3, year5, key11, author13, month7, note9, volume16, number18, pages20, publisher22, journal14, editor26, volume28, series31, address33, author23, edition35, author37, howpublished39, address41, booktitle46, address59, editor48, pages51, organization54, publisher56, author44, chapter64, publisher62, series72, pages66, volume69, author81, booktitle83, address75, edition78, publisher95, editor86, address98, pages89, organization92, series109, author101, booktitle103, editor106, pages112, organization115, publisher118, address121, author124, organization126, address129, edition132, author142, author135, school137, address139, school149, howpublished144, author147, editor155, publisher157, organization160, address152, institution168, type170, number172, address163, author166, address175, author178},
    generalizations={gen_bibtex_Article_BibType, gen_bibtex_Book_BibType, gen_bibtex_Booklet_BibType, gen_bibtex_Conference_BibType, gen_bibtex_Inbook_BibType, gen_bibtex_Incollection_BibType, gen_bibtex_Inproceedings_BibType, gen_bibtex_Mastersthesis_BibType, gen_bibtex_Manual_BibType, gen_bibtex_Misc_BibType, gen_bibtex_Phdthesis_BibType, gen_bibtex_Proceedings_BibType, gen_bibtex_Techreport_BibType, gen_bibtex_Unpublished_BibType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)