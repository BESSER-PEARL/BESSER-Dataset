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
BIBTEXML_AuthoredEntry = Class(name="BIBTEXML_AuthoredEntry", is_abstract=True)
Author = Class(name="Author")
BIBTEXML_BookTitledEntry = Class(name="BIBTEXML_BookTitledEntry", is_abstract=True)
BIBTEXML_BibtexFile = Class(name="BIBTEXML_BibtexFile")
Entry = Class(name="Entry")
BIBTEXML_Author = Class(name="BIBTEXML_Author")
BIBTEXML_Entry = Class(name="BIBTEXML_Entry", is_abstract=True)
BIBTEXML_DatedEntry = Class(name="BIBTEXML_DatedEntry", is_abstract=True)
BIBTEXML_JournalEntry = Class(name="BIBTEXML_JournalEntry", is_abstract=True)
BIBTEXML_TitledEntry = Class(name="BIBTEXML_TitledEntry", is_abstract=True)
BIBTEXML_InstitutionEntry = Class(name="BIBTEXML_InstitutionEntry", is_abstract=True)
BIBTEXML_EditoredEntry = Class(name="BIBTEXML_EditoredEntry", is_abstract=True)
BIBTEXML_SchoolEntry = Class(name="BIBTEXML_SchoolEntry", is_abstract=True)
BIBTEXML_Article = Class(name="BIBTEXML_Article")
AuthoredEntry = Class(name="AuthoredEntry")
DatedEntry = Class(name="DatedEntry")
TitledEntry = Class(name="TitledEntry")
BIBTEXML_NotedEntry = Class(name="BIBTEXML_NotedEntry", is_abstract=True)
BIBTEXML_PublisheredEntry = Class(name="BIBTEXML_PublisheredEntry", is_abstract=True)
JournalEntry = Class(name="JournalEntry")
BIBTEXML_Book = Class(name="BIBTEXML_Book")
EditoredEntry = Class(name="EditoredEntry")
PublisheredEntry = Class(name="PublisheredEntry")
BIBTEXML_InBook = Class(name="BIBTEXML_InBook")
Book = Class(name="Book")
BIBTEXML_InCollection = Class(name="BIBTEXML_InCollection")
BookTitledEntry = Class(name="BookTitledEntry")
BIBTEXML_Booklet = Class(name="BIBTEXML_Booklet")
BIBTEXML_TechReport = Class(name="BIBTEXML_TechReport")
InstitutionEntry = Class(name="InstitutionEntry")
BIBTEXML_Manual = Class(name="BIBTEXML_Manual")
BIBTEXML_ThesisEntry = Class(name="BIBTEXML_ThesisEntry", is_abstract=True)
SchoolEntry = Class(name="SchoolEntry")
BIBTEXML_PhdThesis = Class(name="BIBTEXML_PhdThesis")
ThesisEntry = Class(name="ThesisEntry")
BIBTEXML_MastersThesis = Class(name="BIBTEXML_MastersThesis")
BIBTEXML_Proceedings = Class(name="BIBTEXML_Proceedings")
BIBTEXML_InProceedings = Class(name="BIBTEXML_InProceedings")
Proceedings = Class(name="Proceedings")
BIBTEXML_Conference = Class(name="BIBTEXML_Conference")
InProceedings = Class(name="InProceedings")
BIBTEXML_Unpublished = Class(name="BIBTEXML_Unpublished")
NotedEntry = Class(name="NotedEntry")
BIBTEXML_Misc = Class(name="BIBTEXML_Misc")

# BIBTEXML_AuthoredEntry class attributes and methods

# Author class attributes and methods

# BIBTEXML_BookTitledEntry class attributes and methods
BIBTEXML_BookTitledEntry_booktitle: Property = Property(name="booktitle", type=StringType)
BIBTEXML_BookTitledEntry.attributes={BIBTEXML_BookTitledEntry_booktitle}

# BIBTEXML_BibtexFile class attributes and methods

# Entry class attributes and methods

# BIBTEXML_Author class attributes and methods
BIBTEXML_Author_name: Property = Property(name="name", type=StringType)
BIBTEXML_Author.attributes={BIBTEXML_Author_name}

# BIBTEXML_Entry class attributes and methods
BIBTEXML_Entry_abstract: Property = Property(name="abstract", type=StringType)
BIBTEXML_Entry_id: Property = Property(name="id", type=StringType)
BIBTEXML_Entry.attributes={BIBTEXML_Entry_abstract, BIBTEXML_Entry_id}

# BIBTEXML_DatedEntry class attributes and methods
BIBTEXML_DatedEntry_year: Property = Property(name="year", type=StringType)
BIBTEXML_DatedEntry_month: Property = Property(name="month", type=StringType)
BIBTEXML_DatedEntry.attributes={BIBTEXML_DatedEntry_month, BIBTEXML_DatedEntry_year}

# BIBTEXML_JournalEntry class attributes and methods
BIBTEXML_JournalEntry_journal: Property = Property(name="journal", type=StringType)
BIBTEXML_JournalEntry.attributes={BIBTEXML_JournalEntry_journal}

# BIBTEXML_TitledEntry class attributes and methods
BIBTEXML_TitledEntry_title: Property = Property(name="title", type=StringType)
BIBTEXML_TitledEntry.attributes={BIBTEXML_TitledEntry_title}

# BIBTEXML_InstitutionEntry class attributes and methods
BIBTEXML_InstitutionEntry_institution: Property = Property(name="institution", type=StringType)
BIBTEXML_InstitutionEntry.attributes={BIBTEXML_InstitutionEntry_institution}

# BIBTEXML_EditoredEntry class attributes and methods
BIBTEXML_EditoredEntry_editor: Property = Property(name="editor", type=StringType)
BIBTEXML_EditoredEntry.attributes={BIBTEXML_EditoredEntry_editor}

# BIBTEXML_SchoolEntry class attributes and methods
BIBTEXML_SchoolEntry_school: Property = Property(name="school", type=StringType)
BIBTEXML_SchoolEntry.attributes={BIBTEXML_SchoolEntry_school}

# BIBTEXML_Article class attributes and methods
BIBTEXML_Article_volume: Property = Property(name="volume", type=StringType)
BIBTEXML_Article_number: Property = Property(name="number", type=StringType)
BIBTEXML_Article_pages: Property = Property(name="pages", type=StringType)
BIBTEXML_Article_note: Property = Property(name="note", type=StringType)
BIBTEXML_Article.attributes={BIBTEXML_Article_number, BIBTEXML_Article_pages, BIBTEXML_Article_volume, BIBTEXML_Article_note}

# AuthoredEntry class attributes and methods

# DatedEntry class attributes and methods

# TitledEntry class attributes and methods

# BIBTEXML_NotedEntry class attributes and methods
BIBTEXML_NotedEntry_note: Property = Property(name="note", type=StringType)
BIBTEXML_NotedEntry.attributes={BIBTEXML_NotedEntry_note}

# BIBTEXML_PublisheredEntry class attributes and methods
BIBTEXML_PublisheredEntry_publisher: Property = Property(name="publisher", type=StringType)
BIBTEXML_PublisheredEntry.attributes={BIBTEXML_PublisheredEntry_publisher}

# JournalEntry class attributes and methods

# BIBTEXML_Book class attributes and methods
BIBTEXML_Book_volume: Property = Property(name="volume", type=StringType)
BIBTEXML_Book_number: Property = Property(name="number", type=StringType)
BIBTEXML_Book_series: Property = Property(name="series", type=StringType)
BIBTEXML_Book_address: Property = Property(name="address", type=StringType)
BIBTEXML_Book_edition: Property = Property(name="edition", type=StringType)
BIBTEXML_Book_note: Property = Property(name="note", type=StringType)
BIBTEXML_Book.attributes={BIBTEXML_Book_series, BIBTEXML_Book_number, BIBTEXML_Book_volume, BIBTEXML_Book_address, BIBTEXML_Book_note, BIBTEXML_Book_edition}

# EditoredEntry class attributes and methods

# PublisheredEntry class attributes and methods

# BIBTEXML_InBook class attributes and methods
BIBTEXML_InBook_chapter: Property = Property(name="chapter", type=StringType)
BIBTEXML_InBook_type: Property = Property(name="type", type=StringType)
BIBTEXML_InBook.attributes={BIBTEXML_InBook_chapter, BIBTEXML_InBook_type}

# Book class attributes and methods

# BIBTEXML_InCollection class attributes and methods
BIBTEXML_InCollection_chapter: Property = Property(name="chapter", type=StringType)
BIBTEXML_InCollection_type: Property = Property(name="type", type=StringType)
BIBTEXML_InCollection.attributes={BIBTEXML_InCollection_type, BIBTEXML_InCollection_chapter}

# BookTitledEntry class attributes and methods

# BIBTEXML_Booklet class attributes and methods
BIBTEXML_Booklet_note: Property = Property(name="note", type=StringType)
BIBTEXML_Booklet_howpublished: Property = Property(name="howpublished", type=StringType)
BIBTEXML_Booklet_address: Property = Property(name="address", type=StringType)
BIBTEXML_Booklet.attributes={BIBTEXML_Booklet_note, BIBTEXML_Booklet_howpublished, BIBTEXML_Booklet_address}

# BIBTEXML_TechReport class attributes and methods
BIBTEXML_TechReport_type: Property = Property(name="type", type=StringType)
BIBTEXML_TechReport_number: Property = Property(name="number", type=StringType)
BIBTEXML_TechReport_address: Property = Property(name="address", type=StringType)
BIBTEXML_TechReport_note: Property = Property(name="note", type=StringType)
BIBTEXML_TechReport.attributes={BIBTEXML_TechReport_address, BIBTEXML_TechReport_note, BIBTEXML_TechReport_number, BIBTEXML_TechReport_type}

# InstitutionEntry class attributes and methods

# BIBTEXML_Manual class attributes and methods
BIBTEXML_Manual_note: Property = Property(name="note", type=StringType)
BIBTEXML_Manual_organization: Property = Property(name="organization", type=StringType)
BIBTEXML_Manual_address: Property = Property(name="address", type=StringType)
BIBTEXML_Manual_edition: Property = Property(name="edition", type=StringType)
BIBTEXML_Manual.attributes={BIBTEXML_Manual_edition, BIBTEXML_Manual_note, BIBTEXML_Manual_address, BIBTEXML_Manual_organization}

# BIBTEXML_ThesisEntry class attributes and methods
BIBTEXML_ThesisEntry_type: Property = Property(name="type", type=StringType)
BIBTEXML_ThesisEntry_address: Property = Property(name="address", type=StringType)
BIBTEXML_ThesisEntry_note: Property = Property(name="note", type=StringType)
BIBTEXML_ThesisEntry.attributes={BIBTEXML_ThesisEntry_note, BIBTEXML_ThesisEntry_address, BIBTEXML_ThesisEntry_type}

# SchoolEntry class attributes and methods

# BIBTEXML_PhdThesis class attributes and methods

# ThesisEntry class attributes and methods

# BIBTEXML_MastersThesis class attributes and methods

# BIBTEXML_Proceedings class attributes and methods
BIBTEXML_Proceedings_editor: Property = Property(name="editor", type=StringType)
BIBTEXML_Proceedings_volume: Property = Property(name="volume", type=StringType)
BIBTEXML_Proceedings_number: Property = Property(name="number", type=StringType)
BIBTEXML_Proceedings_series: Property = Property(name="series", type=StringType)
BIBTEXML_Proceedings_address: Property = Property(name="address", type=StringType)
BIBTEXML_Proceedings_organization: Property = Property(name="organization", type=StringType)
BIBTEXML_Proceedings_publisher: Property = Property(name="publisher", type=StringType)
BIBTEXML_Proceedings_note: Property = Property(name="note", type=StringType)
BIBTEXML_Proceedings.attributes={BIBTEXML_Proceedings_volume, BIBTEXML_Proceedings_number, BIBTEXML_Proceedings_organization, BIBTEXML_Proceedings_series, BIBTEXML_Proceedings_address, BIBTEXML_Proceedings_publisher, BIBTEXML_Proceedings_editor, BIBTEXML_Proceedings_note}

# BIBTEXML_InProceedings class attributes and methods
BIBTEXML_InProceedings_pages: Property = Property(name="pages", type=StringType)
BIBTEXML_InProceedings.attributes={BIBTEXML_InProceedings_pages}

# Proceedings class attributes and methods

# BIBTEXML_Conference class attributes and methods

# InProceedings class attributes and methods

# BIBTEXML_Unpublished class attributes and methods

# NotedEntry class attributes and methods

# BIBTEXML_Misc class attributes and methods
BIBTEXML_Misc_title: Property = Property(name="title", type=StringType)
BIBTEXML_Misc_howpublished: Property = Property(name="howpublished", type=StringType)
BIBTEXML_Misc_month: Property = Property(name="month", type=StringType)
BIBTEXML_Misc_year: Property = Property(name="year", type=StringType)
BIBTEXML_Misc_note: Property = Property(name="note", type=StringType)
BIBTEXML_Misc.attributes={BIBTEXML_Misc_title, BIBTEXML_Misc_howpublished, BIBTEXML_Misc_year, BIBTEXML_Misc_month, BIBTEXML_Misc_note}

# Relationships
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="Author", type=BIBTEXML_AuthoredEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="BIBTEXML_AuthoredEntry", type=Author, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entries0: BinaryAssociation = BinaryAssociation(
    name="entries0",
    ends={
        Property(name="Entry", type=BIBTEXML_BibtexFile, multiplicity=Multiplicity(1, 1)),
        Property(name="BIBTEXML_BibtexFile", type=Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors2: BinaryAssociation = BinaryAssociation(
    name="authors2",
    ends={
        Property(name="Author3", type=BIBTEXML_Booklet, multiplicity=Multiplicity(1, 1)),
        Property(name="BIBTEXML_Booklet", type=Author, multiplicity=Multiplicity(0, 9999))
    }
)
authors4: BinaryAssociation = BinaryAssociation(
    name="authors4",
    ends={
        Property(name="Author5", type=BIBTEXML_Misc, multiplicity=Multiplicity(1, 1)),
        Property(name="BIBTEXML_Misc", type=Author, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_BIBTEXML_AuthoredEntry_Entry = Generalization(general=Entry, specific=BIBTEXML_AuthoredEntry)
gen_BIBTEXML_BookTitledEntry_Entry = Generalization(general=Entry, specific=BIBTEXML_BookTitledEntry)
gen_BIBTEXML_DatedEntry_Entry = Generalization(general=Entry, specific=BIBTEXML_DatedEntry)
gen_BIBTEXML_JournalEntry_Entry = Generalization(general=Entry, specific=BIBTEXML_JournalEntry)
gen_BIBTEXML_TitledEntry_Entry = Generalization(general=Entry, specific=BIBTEXML_TitledEntry)
gen_BIBTEXML_InstitutionEntry_Entry = Generalization(general=Entry, specific=BIBTEXML_InstitutionEntry)
gen_BIBTEXML_EditoredEntry_Entry = Generalization(general=Entry, specific=BIBTEXML_EditoredEntry)
gen_BIBTEXML_SchoolEntry_Entry = Generalization(general=Entry, specific=BIBTEXML_SchoolEntry)
gen_BIBTEXML_Article_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BIBTEXML_Article)
gen_BIBTEXML_Article_DatedEntry = Generalization(general=DatedEntry, specific=BIBTEXML_Article)
gen_BIBTEXML_Article_TitledEntry = Generalization(general=TitledEntry, specific=BIBTEXML_Article)
gen_BIBTEXML_NotedEntry_Entry = Generalization(general=Entry, specific=BIBTEXML_NotedEntry)
gen_BIBTEXML_PublisheredEntry_Entry = Generalization(general=Entry, specific=BIBTEXML_PublisheredEntry)
gen_BIBTEXML_Book_DatedEntry = Generalization(general=DatedEntry, specific=BIBTEXML_Book)
gen_BIBTEXML_Book_TitledEntry = Generalization(general=TitledEntry, specific=BIBTEXML_Book)
gen_BIBTEXML_Article_JournalEntry = Generalization(general=JournalEntry, specific=BIBTEXML_Article)
gen_BIBTEXML_Book_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BIBTEXML_Book)
gen_BIBTEXML_Book_EditoredEntry = Generalization(general=EditoredEntry, specific=BIBTEXML_Book)
gen_BIBTEXML_Book_PublisheredEntry = Generalization(general=PublisheredEntry, specific=BIBTEXML_Book)
gen_BIBTEXML_InBook_Book = Generalization(general=Book, specific=BIBTEXML_InBook)
gen_BIBTEXML_InCollection_Book = Generalization(general=Book, specific=BIBTEXML_InCollection)
gen_BIBTEXML_InCollection_BookTitledEntry = Generalization(general=BookTitledEntry, specific=BIBTEXML_InCollection)
gen_BIBTEXML_Booklet_DatedEntry = Generalization(general=DatedEntry, specific=BIBTEXML_Booklet)
gen_BIBTEXML_Booklet_TitledEntry = Generalization(general=TitledEntry, specific=BIBTEXML_Booklet)
gen_BIBTEXML_TechReport_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BIBTEXML_TechReport)
gen_BIBTEXML_TechReport_InstitutionEntry = Generalization(general=InstitutionEntry, specific=BIBTEXML_TechReport)
gen_BIBTEXML_TechReport_DatedEntry = Generalization(general=DatedEntry, specific=BIBTEXML_TechReport)
gen_BIBTEXML_TechReport_TitledEntry = Generalization(general=TitledEntry, specific=BIBTEXML_TechReport)
gen_BIBTEXML_Manual_TitledEntry = Generalization(general=TitledEntry, specific=BIBTEXML_Manual)
gen_BIBTEXML_Manual_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BIBTEXML_Manual)
gen_BIBTEXML_Manual_DatedEntry = Generalization(general=DatedEntry, specific=BIBTEXML_Manual)
gen_BIBTEXML_ThesisEntry_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BIBTEXML_ThesisEntry)
gen_BIBTEXML_ThesisEntry_DatedEntry = Generalization(general=DatedEntry, specific=BIBTEXML_ThesisEntry)
gen_BIBTEXML_ThesisEntry_TitledEntry = Generalization(general=TitledEntry, specific=BIBTEXML_ThesisEntry)
gen_BIBTEXML_ThesisEntry_SchoolEntry = Generalization(general=SchoolEntry, specific=BIBTEXML_ThesisEntry)
gen_BIBTEXML_PhdThesis_ThesisEntry = Generalization(general=ThesisEntry, specific=BIBTEXML_PhdThesis)
gen_BIBTEXML_MastersThesis_ThesisEntry = Generalization(general=ThesisEntry, specific=BIBTEXML_MastersThesis)
gen_BIBTEXML_Proceedings_DatedEntry = Generalization(general=DatedEntry, specific=BIBTEXML_Proceedings)
gen_BIBTEXML_Proceedings_TitledEntry = Generalization(general=TitledEntry, specific=BIBTEXML_Proceedings)
gen_BIBTEXML_Unpublished_DatedEntry = Generalization(general=DatedEntry, specific=BIBTEXML_Unpublished)
gen_BIBTEXML_InProceedings_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BIBTEXML_InProceedings)
gen_BIBTEXML_InProceedings_BookTitledEntry = Generalization(general=BookTitledEntry, specific=BIBTEXML_InProceedings)
gen_BIBTEXML_InProceedings_Proceedings = Generalization(general=Proceedings, specific=BIBTEXML_InProceedings)
gen_BIBTEXML_Conference_InProceedings = Generalization(general=InProceedings, specific=BIBTEXML_Conference)
gen_BIBTEXML_Unpublished_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BIBTEXML_Unpublished)
gen_BIBTEXML_Unpublished_TitledEntry = Generalization(general=TitledEntry, specific=BIBTEXML_Unpublished)
gen_BIBTEXML_Unpublished_NotedEntry = Generalization(general=NotedEntry, specific=BIBTEXML_Unpublished)
gen_BIBTEXML_Misc_Entry = Generalization(general=Entry, specific=BIBTEXML_Misc)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={BIBTEXML_AuthoredEntry, Author, BIBTEXML_BookTitledEntry, BIBTEXML_BibtexFile, Entry, BIBTEXML_Author, BIBTEXML_Entry, BIBTEXML_DatedEntry, BIBTEXML_JournalEntry, BIBTEXML_TitledEntry, BIBTEXML_InstitutionEntry, BIBTEXML_EditoredEntry, BIBTEXML_SchoolEntry, BIBTEXML_Article, AuthoredEntry, DatedEntry, TitledEntry, BIBTEXML_NotedEntry, BIBTEXML_PublisheredEntry, JournalEntry, BIBTEXML_Book, EditoredEntry, PublisheredEntry, BIBTEXML_InBook, Book, BIBTEXML_InCollection, BookTitledEntry, BIBTEXML_Booklet, BIBTEXML_TechReport, InstitutionEntry, BIBTEXML_Manual, BIBTEXML_ThesisEntry, SchoolEntry, BIBTEXML_PhdThesis, ThesisEntry, BIBTEXML_MastersThesis, BIBTEXML_Proceedings, BIBTEXML_InProceedings, Proceedings, BIBTEXML_Conference, InProceedings, BIBTEXML_Unpublished, NotedEntry, BIBTEXML_Misc},
    associations={authors1, entries0, authors2, authors4},
    generalizations={gen_BIBTEXML_AuthoredEntry_Entry, gen_BIBTEXML_BookTitledEntry_Entry, gen_BIBTEXML_DatedEntry_Entry, gen_BIBTEXML_JournalEntry_Entry, gen_BIBTEXML_TitledEntry_Entry, gen_BIBTEXML_InstitutionEntry_Entry, gen_BIBTEXML_EditoredEntry_Entry, gen_BIBTEXML_SchoolEntry_Entry, gen_BIBTEXML_Article_AuthoredEntry, gen_BIBTEXML_Article_DatedEntry, gen_BIBTEXML_Article_TitledEntry, gen_BIBTEXML_NotedEntry_Entry, gen_BIBTEXML_PublisheredEntry_Entry, gen_BIBTEXML_Book_DatedEntry, gen_BIBTEXML_Book_TitledEntry, gen_BIBTEXML_Article_JournalEntry, gen_BIBTEXML_Book_AuthoredEntry, gen_BIBTEXML_Book_EditoredEntry, gen_BIBTEXML_Book_PublisheredEntry, gen_BIBTEXML_InBook_Book, gen_BIBTEXML_InCollection_Book, gen_BIBTEXML_InCollection_BookTitledEntry, gen_BIBTEXML_Booklet_DatedEntry, gen_BIBTEXML_Booklet_TitledEntry, gen_BIBTEXML_TechReport_AuthoredEntry, gen_BIBTEXML_TechReport_InstitutionEntry, gen_BIBTEXML_TechReport_DatedEntry, gen_BIBTEXML_TechReport_TitledEntry, gen_BIBTEXML_Manual_TitledEntry, gen_BIBTEXML_Manual_AuthoredEntry, gen_BIBTEXML_Manual_DatedEntry, gen_BIBTEXML_ThesisEntry_AuthoredEntry, gen_BIBTEXML_ThesisEntry_DatedEntry, gen_BIBTEXML_ThesisEntry_TitledEntry, gen_BIBTEXML_ThesisEntry_SchoolEntry, gen_BIBTEXML_PhdThesis_ThesisEntry, gen_BIBTEXML_MastersThesis_ThesisEntry, gen_BIBTEXML_Proceedings_DatedEntry, gen_BIBTEXML_Proceedings_TitledEntry, gen_BIBTEXML_Unpublished_DatedEntry, gen_BIBTEXML_InProceedings_AuthoredEntry, gen_BIBTEXML_InProceedings_BookTitledEntry, gen_BIBTEXML_InProceedings_Proceedings, gen_BIBTEXML_Conference_InProceedings, gen_BIBTEXML_Unpublished_AuthoredEntry, gen_BIBTEXML_Unpublished_TitledEntry, gen_BIBTEXML_Unpublished_NotedEntry, gen_BIBTEXML_Misc_Entry},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)