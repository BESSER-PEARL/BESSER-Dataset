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
BIBTEX_LocatedElement = Class(name="BIBTEX_LocatedElement", is_abstract=True)
BIBTEX_Bibtex = Class(name="BIBTEX_Bibtex")
Entry = Class(name="Entry")
BIBTEX_Entry = Class(name="BIBTEX_Entry", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
BIBTEX_Field = Class(name="BIBTEX_Field", is_abstract=True)
Field = Class(name="Field")
BIBTEX_Article = Class(name="BIBTEX_Article")
BIBTEX_Book = Class(name="BIBTEX_Book")
BIBTEX_Inbook = Class(name="BIBTEX_Inbook")
BIBTEX_Booklet = Class(name="BIBTEX_Booklet")
BIBTEX_Inproceedings = Class(name="BIBTEX_Inproceedings")
BIBTEX_Proceedings = Class(name="BIBTEX_Proceedings")
BIBTEX_Incollection = Class(name="BIBTEX_Incollection")
BIBTEX_Techreport = Class(name="BIBTEX_Techreport")
BIBTEX_PhdThesis = Class(name="BIBTEX_PhdThesis")
BIBTEX_MastersThesis = Class(name="BIBTEX_MastersThesis")
BIBTEX_Manual = Class(name="BIBTEX_Manual")
BIBTEX_Misc = Class(name="BIBTEX_Misc")
BIBTEX_Number = Class(name="BIBTEX_Number")
BIBTEX_Authors = Class(name="BIBTEX_Authors")
BIBTEX_AuthorUrls = Class(name="BIBTEX_AuthorUrls")
BIBTEX_Title = Class(name="BIBTEX_Title")
BIBTEX_Journal = Class(name="BIBTEX_Journal")
BIBTEX_BookTitle = Class(name="BIBTEX_BookTitle")
BIBTEX_Institution = Class(name="BIBTEX_Institution")
BIBTEX_Organization = Class(name="BIBTEX_Organization")
BIBTEX_Type = Class(name="BIBTEX_Type")
BIBTEX_Day = Class(name="BIBTEX_Day")
BIBTEX_Chapter = Class(name="BIBTEX_Chapter")
BIBTEX_Volume = Class(name="BIBTEX_Volume")
BIBTEX_Series = Class(name="BIBTEX_Series")
BIBTEX_Pages = Class(name="BIBTEX_Pages")
BIBTEX_Publisher = Class(name="BIBTEX_Publisher")
BIBTEX_Howpublished = Class(name="BIBTEX_Howpublished")
BIBTEX_School = Class(name="BIBTEX_School")
BIBTEX_Editor = Class(name="BIBTEX_Editor")
BIBTEX_Edition = Class(name="BIBTEX_Edition")
BIBTEX_Address = Class(name="BIBTEX_Address")
BIBTEX_Year = Class(name="BIBTEX_Year")
BIBTEX_Month = Class(name="BIBTEX_Month")
BIBTEX_Note = Class(name="BIBTEX_Note")
BIBTEX_Text = Class(name="BIBTEX_Text")
BIBTEX_AbstractField = Class(name="BIBTEX_AbstractField")
BIBTEX_Isbn = Class(name="BIBTEX_Isbn")
BIBTEX_Issn = Class(name="BIBTEX_Issn")
BIBTEX_Url = Class(name="BIBTEX_Url")
BIBTEX_Doi = Class(name="BIBTEX_Doi")

# BIBTEX_LocatedElement class attributes and methods
BIBTEX_LocatedElement_location: Property = Property(name="location", type=StringType)
BIBTEX_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
BIBTEX_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
BIBTEX_LocatedElement.attributes={BIBTEX_LocatedElement_commentsBefore, BIBTEX_LocatedElement_commentsAfter, BIBTEX_LocatedElement_location}

# BIBTEX_Bibtex class attributes and methods

# Entry class attributes and methods

# BIBTEX_Entry class attributes and methods
BIBTEX_Entry_key: Property = Property(name="key", type=StringType)
BIBTEX_Entry.attributes={BIBTEX_Entry_key}

# LocatedElement class attributes and methods

# BIBTEX_Field class attributes and methods
BIBTEX_Field_value: Property = Property(name="value", type=StringType)
BIBTEX_Field.attributes={BIBTEX_Field_value}

# Field class attributes and methods

# BIBTEX_Article class attributes and methods

# BIBTEX_Book class attributes and methods

# BIBTEX_Inbook class attributes and methods

# BIBTEX_Booklet class attributes and methods

# BIBTEX_Inproceedings class attributes and methods

# BIBTEX_Proceedings class attributes and methods

# BIBTEX_Incollection class attributes and methods

# BIBTEX_Techreport class attributes and methods

# BIBTEX_PhdThesis class attributes and methods

# BIBTEX_MastersThesis class attributes and methods

# BIBTEX_Manual class attributes and methods

# BIBTEX_Misc class attributes and methods

# BIBTEX_Number class attributes and methods

# BIBTEX_Authors class attributes and methods

# BIBTEX_AuthorUrls class attributes and methods

# BIBTEX_Title class attributes and methods

# BIBTEX_Journal class attributes and methods

# BIBTEX_BookTitle class attributes and methods

# BIBTEX_Institution class attributes and methods

# BIBTEX_Organization class attributes and methods

# BIBTEX_Type class attributes and methods

# BIBTEX_Day class attributes and methods

# BIBTEX_Chapter class attributes and methods

# BIBTEX_Volume class attributes and methods

# BIBTEX_Series class attributes and methods

# BIBTEX_Pages class attributes and methods

# BIBTEX_Publisher class attributes and methods

# BIBTEX_Howpublished class attributes and methods

# BIBTEX_School class attributes and methods

# BIBTEX_Editor class attributes and methods

# BIBTEX_Edition class attributes and methods

# BIBTEX_Address class attributes and methods

# BIBTEX_Year class attributes and methods

# BIBTEX_Month class attributes and methods

# BIBTEX_Note class attributes and methods

# BIBTEX_Text class attributes and methods

# BIBTEX_AbstractField class attributes and methods

# BIBTEX_Isbn class attributes and methods

# BIBTEX_Issn class attributes and methods

# BIBTEX_Url class attributes and methods

# BIBTEX_Doi class attributes and methods

# Relationships
entries0: BinaryAssociation = BinaryAssociation(
    name="entries0",
    ends={
        Property(name="Entry", type=BIBTEX_Bibtex, multiplicity=Multiplicity(1, 1)),
        Property(name="BIBTEX_Bibtex", type=Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields1: BinaryAssociation = BinaryAssociation(
    name="fields1",
    ends={
        Property(name="Field", type=BIBTEX_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="BIBTEX_Entry", type=Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_BIBTEX_Entry_LocatedElement = Generalization(general=LocatedElement, specific=BIBTEX_Entry)
gen_BIBTEX_Article_Entry = Generalization(general=Entry, specific=BIBTEX_Article)
gen_BIBTEX_Book_Entry = Generalization(general=Entry, specific=BIBTEX_Book)
gen_BIBTEX_Inbook_Entry = Generalization(general=Entry, specific=BIBTEX_Inbook)
gen_BIBTEX_Booklet_Entry = Generalization(general=Entry, specific=BIBTEX_Booklet)
gen_BIBTEX_Inproceedings_Entry = Generalization(general=Entry, specific=BIBTEX_Inproceedings)
gen_BIBTEX_Proceedings_Entry = Generalization(general=Entry, specific=BIBTEX_Proceedings)
gen_BIBTEX_Incollection_Entry = Generalization(general=Entry, specific=BIBTEX_Incollection)
gen_BIBTEX_Techreport_Entry = Generalization(general=Entry, specific=BIBTEX_Techreport)
gen_BIBTEX_PhdThesis_Entry = Generalization(general=Entry, specific=BIBTEX_PhdThesis)
gen_BIBTEX_MastersThesis_Entry = Generalization(general=Entry, specific=BIBTEX_MastersThesis)
gen_BIBTEX_Manual_Entry = Generalization(general=Entry, specific=BIBTEX_Manual)
gen_BIBTEX_Misc_Entry = Generalization(general=Entry, specific=BIBTEX_Misc)
gen_BIBTEX_Number_Field = Generalization(general=Field, specific=BIBTEX_Number)
gen_BIBTEX_Authors_Field = Generalization(general=Field, specific=BIBTEX_Authors)
gen_BIBTEX_AuthorUrls_Field = Generalization(general=Field, specific=BIBTEX_AuthorUrls)
gen_BIBTEX_Title_Field = Generalization(general=Field, specific=BIBTEX_Title)
gen_BIBTEX_Journal_Field = Generalization(general=Field, specific=BIBTEX_Journal)
gen_BIBTEX_BookTitle_Field = Generalization(general=Field, specific=BIBTEX_BookTitle)
gen_BIBTEX_Institution_Field = Generalization(general=Field, specific=BIBTEX_Institution)
gen_BIBTEX_Organization_Field = Generalization(general=Field, specific=BIBTEX_Organization)
gen_BIBTEX_Type_Field = Generalization(general=Field, specific=BIBTEX_Type)
gen_BIBTEX_Day_Field = Generalization(general=Field, specific=BIBTEX_Day)
gen_BIBTEX_Chapter_Field = Generalization(general=Field, specific=BIBTEX_Chapter)
gen_BIBTEX_Volume_Field = Generalization(general=Field, specific=BIBTEX_Volume)
gen_BIBTEX_Series_Field = Generalization(general=Field, specific=BIBTEX_Series)
gen_BIBTEX_Pages_Field = Generalization(general=Field, specific=BIBTEX_Pages)
gen_BIBTEX_Publisher_Field = Generalization(general=Field, specific=BIBTEX_Publisher)
gen_BIBTEX_Howpublished_Field = Generalization(general=Field, specific=BIBTEX_Howpublished)
gen_BIBTEX_School_Field = Generalization(general=Field, specific=BIBTEX_School)
gen_BIBTEX_Editor_Field = Generalization(general=Field, specific=BIBTEX_Editor)
gen_BIBTEX_Edition_Field = Generalization(general=Field, specific=BIBTEX_Edition)
gen_BIBTEX_Address_Field = Generalization(general=Field, specific=BIBTEX_Address)
gen_BIBTEX_Year_Field = Generalization(general=Field, specific=BIBTEX_Year)
gen_BIBTEX_Month_Field = Generalization(general=Field, specific=BIBTEX_Month)
gen_BIBTEX_Note_Field = Generalization(general=Field, specific=BIBTEX_Note)
gen_BIBTEX_Text_Field = Generalization(general=Field, specific=BIBTEX_Text)
gen_BIBTEX_AbstractField_Field = Generalization(general=Field, specific=BIBTEX_AbstractField)
gen_BIBTEX_Isbn_Field = Generalization(general=Field, specific=BIBTEX_Isbn)
gen_BIBTEX_Issn_Field = Generalization(general=Field, specific=BIBTEX_Issn)
gen_BIBTEX_Url_Field = Generalization(general=Field, specific=BIBTEX_Url)
gen_BIBTEX_Doi_Field = Generalization(general=Field, specific=BIBTEX_Doi)

# Domain Model
domain_model = DomainModel(
    name="BIBTEX",
    types={BIBTEX_LocatedElement, BIBTEX_Bibtex, Entry, BIBTEX_Entry, LocatedElement, BIBTEX_Field, Field, BIBTEX_Article, BIBTEX_Book, BIBTEX_Inbook, BIBTEX_Booklet, BIBTEX_Inproceedings, BIBTEX_Proceedings, BIBTEX_Incollection, BIBTEX_Techreport, BIBTEX_PhdThesis, BIBTEX_MastersThesis, BIBTEX_Manual, BIBTEX_Misc, BIBTEX_Number, BIBTEX_Authors, BIBTEX_AuthorUrls, BIBTEX_Title, BIBTEX_Journal, BIBTEX_BookTitle, BIBTEX_Institution, BIBTEX_Organization, BIBTEX_Type, BIBTEX_Day, BIBTEX_Chapter, BIBTEX_Volume, BIBTEX_Series, BIBTEX_Pages, BIBTEX_Publisher, BIBTEX_Howpublished, BIBTEX_School, BIBTEX_Editor, BIBTEX_Edition, BIBTEX_Address, BIBTEX_Year, BIBTEX_Month, BIBTEX_Note, BIBTEX_Text, BIBTEX_AbstractField, BIBTEX_Isbn, BIBTEX_Issn, BIBTEX_Url, BIBTEX_Doi},
    associations={entries0, fields1},
    generalizations={gen_BIBTEX_Entry_LocatedElement, gen_BIBTEX_Article_Entry, gen_BIBTEX_Book_Entry, gen_BIBTEX_Inbook_Entry, gen_BIBTEX_Booklet_Entry, gen_BIBTEX_Inproceedings_Entry, gen_BIBTEX_Proceedings_Entry, gen_BIBTEX_Incollection_Entry, gen_BIBTEX_Techreport_Entry, gen_BIBTEX_PhdThesis_Entry, gen_BIBTEX_MastersThesis_Entry, gen_BIBTEX_Manual_Entry, gen_BIBTEX_Misc_Entry, gen_BIBTEX_Number_Field, gen_BIBTEX_Authors_Field, gen_BIBTEX_AuthorUrls_Field, gen_BIBTEX_Title_Field, gen_BIBTEX_Journal_Field, gen_BIBTEX_BookTitle_Field, gen_BIBTEX_Institution_Field, gen_BIBTEX_Organization_Field, gen_BIBTEX_Type_Field, gen_BIBTEX_Day_Field, gen_BIBTEX_Chapter_Field, gen_BIBTEX_Volume_Field, gen_BIBTEX_Series_Field, gen_BIBTEX_Pages_Field, gen_BIBTEX_Publisher_Field, gen_BIBTEX_Howpublished_Field, gen_BIBTEX_School_Field, gen_BIBTEX_Editor_Field, gen_BIBTEX_Edition_Field, gen_BIBTEX_Address_Field, gen_BIBTEX_Year_Field, gen_BIBTEX_Month_Field, gen_BIBTEX_Note_Field, gen_BIBTEX_Text_Field, gen_BIBTEX_AbstractField_Field, gen_BIBTEX_Isbn_Field, gen_BIBTEX_Issn_Field, gen_BIBTEX_Url_Field, gen_BIBTEX_Doi_Field},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)