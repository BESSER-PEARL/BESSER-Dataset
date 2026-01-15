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
Author = Class(name="Author")
BibTeX_BibTeXFile = Class(name="BibTeX::BibTeXFile")
BibTeXEntry = Class(name="BibTeXEntry")
BibTeX_Author = Class(name="BibTeX::Author")
BibTeX_BibTeXEntry = Class(name="BibTeX::BibTeXEntry", is_abstract=True)
BibTeX_AuthoredEntry = Class(name="BibTeX::AuthoredEntry", is_abstract=True)
BibTeX_Manual = Class(name="BibTeX::Manual")
BibTeX_DatedEntry = Class(name="BibTeX::DatedEntry", is_abstract=True)
BibTeX_TitledEntry = Class(name="BibTeX::TitledEntry", is_abstract=True)
BibTeX_BookTitledEntry = Class(name="BibTeX::BookTitledEntry", is_abstract=True)
BibTeX_Article = Class(name="BibTeX::Article")
AuthoredEntry = Class(name="AuthoredEntry")
DatedEntry = Class(name="DatedEntry")
TitledEntry = Class(name="TitledEntry")
BibTeX_TechReport = Class(name="BibTeX::TechReport")
BibTeX_Unpublished = Class(name="BibTeX::Unpublished")
BibTeX_MasterThesis = Class(name="BibTeX::MasterThesis")
BibTeX_Proceedings = Class(name="BibTeX::Proceedings")
BibTeX_InProceedings = Class(name="BibTeX::InProceedings")
Proceedings = Class(name="Proceedings")
BookTitledEntry = Class(name="BookTitledEntry")
BibTeX_Booklet = Class(name="BibTeX::Booklet")
BibTeX_Book = Class(name="BibTeX::Book")
BibTeX_InCollection = Class(name="BibTeX::InCollection")
Book = Class(name="Book")
BibTeX_InBook = Class(name="BibTeX::InBook")
BibTeX_Misc = Class(name="BibTeX::Misc")
BibTeX_ThesisEntry = Class(name="BibTeX::ThesisEntry", is_abstract=True)
BibTeX_PhDThesis = Class(name="BibTeX::PhDThesis")
ThesisEntry = Class(name="ThesisEntry")

# Author class attributes and methods

# BibTeX_BibTeXFile class attributes and methods

# BibTeXEntry class attributes and methods

# BibTeX_Author class attributes and methods
BibTeX_Author_author: Property = Property(name="author", type=StringType)
BibTeX_Author.attributes={BibTeX_Author_author}

# BibTeX_BibTeXEntry class attributes and methods
BibTeX_BibTeXEntry_id: Property = Property(name="id", type=StringType)
BibTeX_BibTeXEntry.attributes={BibTeX_BibTeXEntry_id}

# BibTeX_AuthoredEntry class attributes and methods

# BibTeX_Manual class attributes and methods

# BibTeX_DatedEntry class attributes and methods
BibTeX_DatedEntry_year: Property = Property(name="year", type=StringType)
BibTeX_DatedEntry.attributes={BibTeX_DatedEntry_year}

# BibTeX_TitledEntry class attributes and methods
BibTeX_TitledEntry_title: Property = Property(name="title", type=StringType)
BibTeX_TitledEntry.attributes={BibTeX_TitledEntry_title}

# BibTeX_BookTitledEntry class attributes and methods
BibTeX_BookTitledEntry_booktitle: Property = Property(name="booktitle", type=StringType)
BibTeX_BookTitledEntry.attributes={BibTeX_BookTitledEntry_booktitle}

# BibTeX_Article class attributes and methods
BibTeX_Article_journal: Property = Property(name="journal", type=StringType)
BibTeX_Article.attributes={BibTeX_Article_journal}

# AuthoredEntry class attributes and methods

# DatedEntry class attributes and methods

# TitledEntry class attributes and methods

# BibTeX_TechReport class attributes and methods

# BibTeX_Unpublished class attributes and methods
BibTeX_Unpublished_note: Property = Property(name="note", type=StringType)
BibTeX_Unpublished.attributes={BibTeX_Unpublished_note}

# BibTeX_MasterThesis class attributes and methods

# BibTeX_Proceedings class attributes and methods

# BibTeX_InProceedings class attributes and methods

# Proceedings class attributes and methods

# BookTitledEntry class attributes and methods

# BibTeX_Booklet class attributes and methods

# BibTeX_Book class attributes and methods
BibTeX_Book_publisher: Property = Property(name="publisher", type=StringType)
BibTeX_Book.attributes={BibTeX_Book_publisher}

# BibTeX_InCollection class attributes and methods

# Book class attributes and methods

# BibTeX_InBook class attributes and methods
BibTeX_InBook_chapter: Property = Property(name="chapter", type=IntegerType)
BibTeX_InBook.attributes={BibTeX_InBook_chapter}

# BibTeX_Misc class attributes and methods

# BibTeX_ThesisEntry class attributes and methods
BibTeX_ThesisEntry_school: Property = Property(name="school", type=StringType)
BibTeX_ThesisEntry.attributes={BibTeX_ThesisEntry_school}

# BibTeX_PhDThesis class attributes and methods

# ThesisEntry class attributes and methods

# Relationships
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="Author", type=BibTeX_AuthoredEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="BibTeX_AuthoredEntry", type=Author, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entries0: BinaryAssociation = BinaryAssociation(
    name="entries0",
    ends={
        Property(name="BibTeXEntry", type=BibTeX_BibTeXFile, multiplicity=Multiplicity(1, 1)),
        Property(name="BibTeX_BibTeXFile", type=BibTeXEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_BibTeX_AuthoredEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=BibTeX_AuthoredEntry)
gen_BibTeX_Manual_TitledEntry = Generalization(general=TitledEntry, specific=BibTeX_Manual)
gen_BibTeX_DatedEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=BibTeX_DatedEntry)
gen_BibTeX_TitledEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=BibTeX_TitledEntry)
gen_BibTeX_BookTitledEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=BibTeX_BookTitledEntry)
gen_BibTeX_Article_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BibTeX_Article)
gen_BibTeX_Article_DatedEntry = Generalization(general=DatedEntry, specific=BibTeX_Article)
gen_BibTeX_Article_TitledEntry = Generalization(general=TitledEntry, specific=BibTeX_Article)
gen_BibTeX_TechReport_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BibTeX_TechReport)
gen_BibTeX_TechReport_DatedEntry = Generalization(general=DatedEntry, specific=BibTeX_TechReport)
gen_BibTeX_TechReport_TitledEntry = Generalization(general=TitledEntry, specific=BibTeX_TechReport)
gen_BibTeX_Unpublished_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BibTeX_Unpublished)
gen_BibTeX_Unpublished_TitledEntry = Generalization(general=TitledEntry, specific=BibTeX_Unpublished)
gen_BibTeX_MasterThesis_ThesisEntry = Generalization(general=ThesisEntry, specific=BibTeX_MasterThesis)
gen_BibTeX_Proceedings_DatedEntry = Generalization(general=DatedEntry, specific=BibTeX_Proceedings)
gen_BibTeX_Proceedings_TitledEntry = Generalization(general=TitledEntry, specific=BibTeX_Proceedings)
gen_BibTeX_InProceedings_Proceedings = Generalization(general=Proceedings, specific=BibTeX_InProceedings)
gen_BibTeX_InProceedings_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BibTeX_InProceedings)
gen_BibTeX_InProceedings_BookTitledEntry = Generalization(general=BookTitledEntry, specific=BibTeX_InProceedings)
gen_BibTeX_Booklet_DatedEntry = Generalization(general=DatedEntry, specific=BibTeX_Booklet)
gen_BibTeX_Book_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BibTeX_Book)
gen_BibTeX_Book_DatedEntry = Generalization(general=DatedEntry, specific=BibTeX_Book)
gen_BibTeX_Book_TitledEntry = Generalization(general=TitledEntry, specific=BibTeX_Book)
gen_BibTeX_InCollection_Book = Generalization(general=Book, specific=BibTeX_InCollection)
gen_BibTeX_InCollection_BookTitledEntry = Generalization(general=BookTitledEntry, specific=BibTeX_InCollection)
gen_BibTeX_InBook_Book = Generalization(general=Book, specific=BibTeX_InBook)
gen_BibTeX_Misc_BibTeXEntry = Generalization(general=BibTeXEntry, specific=BibTeX_Misc)
gen_BibTeX_ThesisEntry_AuthoredEntry = Generalization(general=AuthoredEntry, specific=BibTeX_ThesisEntry)
gen_BibTeX_ThesisEntry_DatedEntry = Generalization(general=DatedEntry, specific=BibTeX_ThesisEntry)
gen_BibTeX_ThesisEntry_TitledEntry = Generalization(general=TitledEntry, specific=BibTeX_ThesisEntry)
gen_BibTeX_PhDThesis_ThesisEntry = Generalization(general=ThesisEntry, specific=BibTeX_PhDThesis)

# Domain Model
domain_model = DomainModel(
    name="BibTeX",
    types={Author, BibTeX_BibTeXFile, BibTeXEntry, BibTeX_Author, BibTeX_BibTeXEntry, BibTeX_AuthoredEntry, BibTeX_Manual, BibTeX_DatedEntry, BibTeX_TitledEntry, BibTeX_BookTitledEntry, BibTeX_Article, AuthoredEntry, DatedEntry, TitledEntry, BibTeX_TechReport, BibTeX_Unpublished, BibTeX_MasterThesis, BibTeX_Proceedings, BibTeX_InProceedings, Proceedings, BookTitledEntry, BibTeX_Booklet, BibTeX_Book, BibTeX_InCollection, Book, BibTeX_InBook, BibTeX_Misc, BibTeX_ThesisEntry, BibTeX_PhDThesis, ThesisEntry},
    associations={authors1, entries0},
    generalizations={gen_BibTeX_AuthoredEntry_BibTeXEntry, gen_BibTeX_Manual_TitledEntry, gen_BibTeX_DatedEntry_BibTeXEntry, gen_BibTeX_TitledEntry_BibTeXEntry, gen_BibTeX_BookTitledEntry_BibTeXEntry, gen_BibTeX_Article_AuthoredEntry, gen_BibTeX_Article_DatedEntry, gen_BibTeX_Article_TitledEntry, gen_BibTeX_TechReport_AuthoredEntry, gen_BibTeX_TechReport_DatedEntry, gen_BibTeX_TechReport_TitledEntry, gen_BibTeX_Unpublished_AuthoredEntry, gen_BibTeX_Unpublished_TitledEntry, gen_BibTeX_MasterThesis_ThesisEntry, gen_BibTeX_Proceedings_DatedEntry, gen_BibTeX_Proceedings_TitledEntry, gen_BibTeX_InProceedings_Proceedings, gen_BibTeX_InProceedings_AuthoredEntry, gen_BibTeX_InProceedings_BookTitledEntry, gen_BibTeX_Booklet_DatedEntry, gen_BibTeX_Book_AuthoredEntry, gen_BibTeX_Book_DatedEntry, gen_BibTeX_Book_TitledEntry, gen_BibTeX_InCollection_Book, gen_BibTeX_InCollection_BookTitledEntry, gen_BibTeX_InBook_Book, gen_BibTeX_Misc_BibTeXEntry, gen_BibTeX_ThesisEntry_AuthoredEntry, gen_BibTeX_ThesisEntry_DatedEntry, gen_BibTeX_ThesisEntry_TitledEntry, gen_BibTeX_PhDThesis_ThesisEntry},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)