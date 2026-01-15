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
bibtex_Author = Class(name="bibtex::Author")
bibtex_BibTeXFile = Class(name="bibtex::BibTeXFile")
bibtex_BibTeXEntry = Class(name="bibtex::BibTeXEntry", is_abstract=True)
bibtex_TechReport = Class(name="bibtex::TechReport")
bibtex_Unpublished = Class(name="bibtex::Unpublished")
bibtex_AuthoredEntry = Class(name="bibtex::AuthoredEntry", is_abstract=True)
BibTeXEntry = Class(name="BibTeXEntry")
bibtex_DatedEntry = Class(name="bibtex::DatedEntry", is_abstract=True)
bibtex_TitledEntry = Class(name="bibtex::TitledEntry", is_abstract=True)
bibtex_BookTitledEntry = Class(name="bibtex::BookTitledEntry", is_abstract=True)
bibtex_Article = Class(name="bibtex::Article")
AuthoredEntry = Class(name="AuthoredEntry")
DatedEntry = Class(name="DatedEntry")
TitledEntry = Class(name="TitledEntry")
bibtex_Misc = Class(name="bibtex::Misc")
bibtex_ThesisEntry = Class(name="bibtex::ThesisEntry", is_abstract=True)
bibtex_Manual = Class(name="bibtex::Manual")
bibtex_Proceedings = Class(name="bibtex::Proceedings")
bibtex_InProceedings = Class(name="bibtex::InProceedings")
Proceedings = Class(name="Proceedings")
BookTitledEntry = Class(name="BookTitledEntry")
bibtex_Booklet = Class(name="bibtex::Booklet")
bibtex_Book = Class(name="bibtex::Book")
bibtex_InCollection = Class(name="bibtex::InCollection")
Book = Class(name="Book")
bibtex_InBook = Class(name="bibtex::InBook")
bibtex_PhDThesis = Class(name="bibtex::PhDThesis")
ThesisEntry = Class(name="ThesisEntry")
bibtex_MasterThesis = Class(name="bibtex::MasterThesis")

# bibtex_Author class attributes and methods
bibtex_Author_author: Property = Property(name="author", type=StringType)
bibtex_Author.attributes={bibtex_Author_author}

# bibtex_BibTeXFile class attributes and methods

# bibtex_BibTeXEntry class attributes and methods
bibtex_BibTeXEntry_id: Property = Property(name="id", type=StringType)
bibtex_BibTeXEntry.attributes={bibtex_BibTeXEntry_id}

# bibtex_TechReport class attributes and methods

# bibtex_Unpublished class attributes and methods
bibtex_Unpublished_note: Property = Property(name="note", type=StringType)
bibtex_Unpublished.attributes={bibtex_Unpublished_note}

# bibtex_AuthoredEntry class attributes and methods

# BibTeXEntry class attributes and methods

# bibtex_DatedEntry class attributes and methods
bibtex_DatedEntry_year: Property = Property(name="year", type=IntegerType)
bibtex_DatedEntry.attributes={bibtex_DatedEntry_year}

# bibtex_TitledEntry class attributes and methods
bibtex_TitledEntry_title: Property = Property(name="title", type=StringType)
bibtex_TitledEntry.attributes={bibtex_TitledEntry_title}

# bibtex_BookTitledEntry class attributes and methods
bibtex_BookTitledEntry_booktitle: Property = Property(name="booktitle", type=StringType)
bibtex_BookTitledEntry.attributes={bibtex_BookTitledEntry_booktitle}

# bibtex_Article class attributes and methods
bibtex_Article_journal: Property = Property(name="journal", type=StringType)
bibtex_Article.attributes={bibtex_Article_journal}

# AuthoredEntry class attributes and methods

# DatedEntry class attributes and methods

# TitledEntry class attributes and methods

# bibtex_Misc class attributes and methods

# bibtex_ThesisEntry class attributes and methods
bibtex_ThesisEntry_school: Property = Property(name="school", type=StringType)
bibtex_ThesisEntry.attributes={bibtex_ThesisEntry_school}

# bibtex_Manual class attributes and methods

# bibtex_Proceedings class attributes and methods

# bibtex_InProceedings class attributes and methods

# Proceedings class attributes and methods

# BookTitledEntry class attributes and methods

# bibtex_Booklet class attributes and methods

# bibtex_Book class attributes and methods
bibtex_Book_publisher: Property = Property(name="publisher", type=StringType)
bibtex_Book.attributes={bibtex_Book_publisher}

# bibtex_InCollection class attributes and methods

# Book class attributes and methods

# bibtex_InBook class attributes and methods
bibtex_InBook_chapter: Property = Property(name="chapter", type=IntegerType)
bibtex_InBook.attributes={bibtex_InBook_chapter}

# bibtex_PhDThesis class attributes and methods

# ThesisEntry class attributes and methods

# bibtex_MasterThesis class attributes and methods

# Relationships
entries0: BinaryAssociation = BinaryAssociation(
    name="entries0",
    ends={
        Property(name="bibtex_BibTeXEntry", type=bibtex_BibTeXFile, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_BibTeXFile", type=bibtex_BibTeXEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="bibtex_Author", type=bibtex_AuthoredEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_AuthoredEntry", type=bibtex_Author, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_bibtex_TechReport_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibtex_TechReport)
gen_bibtex_TechReport_DatedEntry = Generalization(general=DatedEntry, specific=bibtex_TechReport)
gen_bibtex_TechReport_TitledEntry = Generalization(general=TitledEntry, specific=bibtex_TechReport)
gen_bibtex_Unpublished_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibtex_Unpublished)
gen_bibtex_Unpublished_TitledEntry = Generalization(general=TitledEntry, specific=bibtex_Unpublished)
gen_bibtex_AuthoredEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=bibtex_AuthoredEntry)
gen_bibtex_DatedEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=bibtex_DatedEntry)
gen_bibtex_TitledEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=bibtex_TitledEntry)
gen_bibtex_BookTitledEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=bibtex_BookTitledEntry)
gen_bibtex_Article_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibtex_Article)
gen_bibtex_Article_DatedEntry = Generalization(general=DatedEntry, specific=bibtex_Article)
gen_bibtex_Article_TitledEntry = Generalization(general=TitledEntry, specific=bibtex_Article)
gen_bibtex_Misc_BibTeXEntry = Generalization(general=BibTeXEntry, specific=bibtex_Misc)
gen_bibtex_ThesisEntry_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibtex_ThesisEntry)
gen_bibtex_ThesisEntry_DatedEntry = Generalization(general=DatedEntry, specific=bibtex_ThesisEntry)
gen_bibtex_Manual_TitledEntry = Generalization(general=TitledEntry, specific=bibtex_Manual)
gen_bibtex_Proceedings_DatedEntry = Generalization(general=DatedEntry, specific=bibtex_Proceedings)
gen_bibtex_Proceedings_TitledEntry = Generalization(general=TitledEntry, specific=bibtex_Proceedings)
gen_bibtex_InProceedings_Proceedings = Generalization(general=Proceedings, specific=bibtex_InProceedings)
gen_bibtex_InProceedings_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibtex_InProceedings)
gen_bibtex_InProceedings_BookTitledEntry = Generalization(general=BookTitledEntry, specific=bibtex_InProceedings)
gen_bibtex_Booklet_DatedEntry = Generalization(general=DatedEntry, specific=bibtex_Booklet)
gen_bibtex_Book_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibtex_Book)
gen_bibtex_Book_DatedEntry = Generalization(general=DatedEntry, specific=bibtex_Book)
gen_bibtex_Book_TitledEntry = Generalization(general=TitledEntry, specific=bibtex_Book)
gen_bibtex_InCollection_Book = Generalization(general=Book, specific=bibtex_InCollection)
gen_bibtex_InCollection_BookTitledEntry = Generalization(general=BookTitledEntry, specific=bibtex_InCollection)
gen_bibtex_InBook_Book = Generalization(general=Book, specific=bibtex_InBook)
gen_bibtex_ThesisEntry_TitledEntry = Generalization(general=TitledEntry, specific=bibtex_ThesisEntry)
gen_bibtex_PhDThesis_ThesisEntry = Generalization(general=ThesisEntry, specific=bibtex_PhDThesis)
gen_bibtex_MasterThesis_ThesisEntry = Generalization(general=ThesisEntry, specific=bibtex_MasterThesis)

# Domain Model
domain_model = DomainModel(
    name="bibtex",
    types={bibtex_Author, bibtex_BibTeXFile, bibtex_BibTeXEntry, bibtex_TechReport, bibtex_Unpublished, bibtex_AuthoredEntry, BibTeXEntry, bibtex_DatedEntry, bibtex_TitledEntry, bibtex_BookTitledEntry, bibtex_Article, AuthoredEntry, DatedEntry, TitledEntry, bibtex_Misc, bibtex_ThesisEntry, bibtex_Manual, bibtex_Proceedings, bibtex_InProceedings, Proceedings, BookTitledEntry, bibtex_Booklet, bibtex_Book, bibtex_InCollection, Book, bibtex_InBook, bibtex_PhDThesis, ThesisEntry, bibtex_MasterThesis},
    associations={entries0, authors1},
    generalizations={gen_bibtex_TechReport_AuthoredEntry, gen_bibtex_TechReport_DatedEntry, gen_bibtex_TechReport_TitledEntry, gen_bibtex_Unpublished_AuthoredEntry, gen_bibtex_Unpublished_TitledEntry, gen_bibtex_AuthoredEntry_BibTeXEntry, gen_bibtex_DatedEntry_BibTeXEntry, gen_bibtex_TitledEntry_BibTeXEntry, gen_bibtex_BookTitledEntry_BibTeXEntry, gen_bibtex_Article_AuthoredEntry, gen_bibtex_Article_DatedEntry, gen_bibtex_Article_TitledEntry, gen_bibtex_Misc_BibTeXEntry, gen_bibtex_ThesisEntry_AuthoredEntry, gen_bibtex_ThesisEntry_DatedEntry, gen_bibtex_Manual_TitledEntry, gen_bibtex_Proceedings_DatedEntry, gen_bibtex_Proceedings_TitledEntry, gen_bibtex_InProceedings_Proceedings, gen_bibtex_InProceedings_AuthoredEntry, gen_bibtex_InProceedings_BookTitledEntry, gen_bibtex_Booklet_DatedEntry, gen_bibtex_Book_AuthoredEntry, gen_bibtex_Book_DatedEntry, gen_bibtex_Book_TitledEntry, gen_bibtex_InCollection_Book, gen_bibtex_InCollection_BookTitledEntry, gen_bibtex_InBook_Book, gen_bibtex_ThesisEntry_TitledEntry, gen_bibtex_PhDThesis_ThesisEntry, gen_bibtex_MasterThesis_ThesisEntry},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)