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
bibTeX_BibTeXFile = Class(name="bibTeX_BibTeXFile")
bibTeX_BibTeXEntry = Class(name="bibTeX_BibTeXEntry", is_abstract=True)
bibTeX_Author = Class(name="bibTeX_Author")
bibTeX_AuthoredEntry = Class(name="bibTeX_AuthoredEntry", is_abstract=True)
BibTeXEntry = Class(name="BibTeXEntry")
bibTeX_Manual = Class(name="bibTeX_Manual")
bibTeX_Proceedings = Class(name="bibTeX_Proceedings")
bibTeX_InProceedings = Class(name="bibTeX_InProceedings")
Proceedings = Class(name="Proceedings")
BookTitledEntry = Class(name="BookTitledEntry")
bibTeX_Booklet = Class(name="bibTeX_Booklet")
bibTeX_Book = Class(name="bibTeX_Book")
bibTeX_DatedEntry = Class(name="bibTeX_DatedEntry", is_abstract=True)
bibTeX_TitledEntry = Class(name="bibTeX_TitledEntry", is_abstract=True)
bibTeX_BookTitledEntry = Class(name="bibTeX_BookTitledEntry", is_abstract=True)
bibTeX_Article = Class(name="bibTeX_Article")
AuthoredEntry = Class(name="AuthoredEntry")
DatedEntry = Class(name="DatedEntry")
TitledEntry = Class(name="TitledEntry")
bibTeX_TechReport = Class(name="bibTeX_TechReport")
bibTeX_Unpublished = Class(name="bibTeX_Unpublished")
bibTeX_InCollection = Class(name="bibTeX_InCollection")
Book = Class(name="Book")
bibTeX_InBook = Class(name="bibTeX_InBook")
bibTeX_Misc = Class(name="bibTeX_Misc")
bibTeX_ThesisEntry = Class(name="bibTeX_ThesisEntry", is_abstract=True)
bibTeX_PhDThesis = Class(name="bibTeX_PhDThesis")
ThesisEntry = Class(name="ThesisEntry")
bibTeX_MasterThesis = Class(name="bibTeX_MasterThesis")

# bibTeX_BibTeXFile class attributes and methods

# bibTeX_BibTeXEntry class attributes and methods
bibTeX_BibTeXEntry_theId: Property = Property(name="theId", type=StringType)
bibTeX_BibTeXEntry.attributes={bibTeX_BibTeXEntry_theId}

# bibTeX_Author class attributes and methods
bibTeX_Author_author: Property = Property(name="author", type=StringType)
bibTeX_Author.attributes={bibTeX_Author_author}

# bibTeX_AuthoredEntry class attributes and methods

# BibTeXEntry class attributes and methods

# bibTeX_Manual class attributes and methods

# bibTeX_Proceedings class attributes and methods

# bibTeX_InProceedings class attributes and methods

# Proceedings class attributes and methods

# BookTitledEntry class attributes and methods

# bibTeX_Booklet class attributes and methods

# bibTeX_Book class attributes and methods
bibTeX_Book_publisher: Property = Property(name="publisher", type=StringType)
bibTeX_Book.attributes={bibTeX_Book_publisher}

# bibTeX_DatedEntry class attributes and methods
bibTeX_DatedEntry_year: Property = Property(name="year", type=StringType)
bibTeX_DatedEntry.attributes={bibTeX_DatedEntry_year}

# bibTeX_TitledEntry class attributes and methods
bibTeX_TitledEntry_title: Property = Property(name="title", type=StringType)
bibTeX_TitledEntry.attributes={bibTeX_TitledEntry_title}

# bibTeX_BookTitledEntry class attributes and methods
bibTeX_BookTitledEntry_booktitle: Property = Property(name="booktitle", type=StringType)
bibTeX_BookTitledEntry.attributes={bibTeX_BookTitledEntry_booktitle}

# bibTeX_Article class attributes and methods
bibTeX_Article_journal: Property = Property(name="journal", type=StringType)
bibTeX_Article.attributes={bibTeX_Article_journal}

# AuthoredEntry class attributes and methods

# DatedEntry class attributes and methods

# TitledEntry class attributes and methods

# bibTeX_TechReport class attributes and methods

# bibTeX_Unpublished class attributes and methods
bibTeX_Unpublished_note: Property = Property(name="note", type=StringType)
bibTeX_Unpublished.attributes={bibTeX_Unpublished_note}

# bibTeX_InCollection class attributes and methods

# Book class attributes and methods

# bibTeX_InBook class attributes and methods
bibTeX_InBook_chapter: Property = Property(name="chapter", type=StringType)
bibTeX_InBook.attributes={bibTeX_InBook_chapter}

# bibTeX_Misc class attributes and methods

# bibTeX_ThesisEntry class attributes and methods
bibTeX_ThesisEntry_school: Property = Property(name="school", type=StringType)
bibTeX_ThesisEntry.attributes={bibTeX_ThesisEntry_school}

# bibTeX_PhDThesis class attributes and methods

# ThesisEntry class attributes and methods

# bibTeX_MasterThesis class attributes and methods

# Relationships
entries0: BinaryAssociation = BinaryAssociation(
    name="entries0",
    ends={
        Property(name="bibTeX_BibTeXEntry", type=bibTeX_BibTeXFile, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_BibTeXFile", type=bibTeX_BibTeXEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="bibTeX_Author", type=bibTeX_AuthoredEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bibTeX_AuthoredEntry", type=bibTeX_Author, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_bibTeX_AuthoredEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=bibTeX_AuthoredEntry)
gen_bibTeX_Manual_TitledEntry = Generalization(general=TitledEntry, specific=bibTeX_Manual)
gen_bibTeX_Proceedings_DatedEntry = Generalization(general=DatedEntry, specific=bibTeX_Proceedings)
gen_bibTeX_Proceedings_TitledEntry = Generalization(general=TitledEntry, specific=bibTeX_Proceedings)
gen_bibTeX_InProceedings_Proceedings = Generalization(general=Proceedings, specific=bibTeX_InProceedings)
gen_bibTeX_InProceedings_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibTeX_InProceedings)
gen_bibTeX_InProceedings_BookTitledEntry = Generalization(general=BookTitledEntry, specific=bibTeX_InProceedings)
gen_bibTeX_Booklet_DatedEntry = Generalization(general=DatedEntry, specific=bibTeX_Booklet)
gen_bibTeX_Book_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibTeX_Book)
gen_bibTeX_Book_DatedEntry = Generalization(general=DatedEntry, specific=bibTeX_Book)
gen_bibTeX_Book_TitledEntry = Generalization(general=TitledEntry, specific=bibTeX_Book)
gen_bibTeX_DatedEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=bibTeX_DatedEntry)
gen_bibTeX_TitledEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=bibTeX_TitledEntry)
gen_bibTeX_BookTitledEntry_BibTeXEntry = Generalization(general=BibTeXEntry, specific=bibTeX_BookTitledEntry)
gen_bibTeX_Article_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibTeX_Article)
gen_bibTeX_Article_DatedEntry = Generalization(general=DatedEntry, specific=bibTeX_Article)
gen_bibTeX_Article_TitledEntry = Generalization(general=TitledEntry, specific=bibTeX_Article)
gen_bibTeX_TechReport_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibTeX_TechReport)
gen_bibTeX_TechReport_DatedEntry = Generalization(general=DatedEntry, specific=bibTeX_TechReport)
gen_bibTeX_TechReport_TitledEntry = Generalization(general=TitledEntry, specific=bibTeX_TechReport)
gen_bibTeX_Unpublished_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibTeX_Unpublished)
gen_bibTeX_Unpublished_TitledEntry = Generalization(general=TitledEntry, specific=bibTeX_Unpublished)
gen_bibTeX_InCollection_Book = Generalization(general=Book, specific=bibTeX_InCollection)
gen_bibTeX_InCollection_BookTitledEntry = Generalization(general=BookTitledEntry, specific=bibTeX_InCollection)
gen_bibTeX_InBook_Book = Generalization(general=Book, specific=bibTeX_InBook)
gen_bibTeX_Misc_BibTeXEntry = Generalization(general=BibTeXEntry, specific=bibTeX_Misc)
gen_bibTeX_ThesisEntry_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibTeX_ThesisEntry)
gen_bibTeX_ThesisEntry_DatedEntry = Generalization(general=DatedEntry, specific=bibTeX_ThesisEntry)
gen_bibTeX_ThesisEntry_TitledEntry = Generalization(general=TitledEntry, specific=bibTeX_ThesisEntry)
gen_bibTeX_PhDThesis_ThesisEntry = Generalization(general=ThesisEntry, specific=bibTeX_PhDThesis)
gen_bibTeX_MasterThesis_ThesisEntry = Generalization(general=ThesisEntry, specific=bibTeX_MasterThesis)

# Domain Model
domain_model = DomainModel(
    name="bibTeX",
    types={bibTeX_BibTeXFile, bibTeX_BibTeXEntry, bibTeX_Author, bibTeX_AuthoredEntry, BibTeXEntry, bibTeX_Manual, bibTeX_Proceedings, bibTeX_InProceedings, Proceedings, BookTitledEntry, bibTeX_Booklet, bibTeX_Book, bibTeX_DatedEntry, bibTeX_TitledEntry, bibTeX_BookTitledEntry, bibTeX_Article, AuthoredEntry, DatedEntry, TitledEntry, bibTeX_TechReport, bibTeX_Unpublished, bibTeX_InCollection, Book, bibTeX_InBook, bibTeX_Misc, bibTeX_ThesisEntry, bibTeX_PhDThesis, ThesisEntry, bibTeX_MasterThesis},
    associations={entries0, authors1},
    generalizations={gen_bibTeX_AuthoredEntry_BibTeXEntry, gen_bibTeX_Manual_TitledEntry, gen_bibTeX_Proceedings_DatedEntry, gen_bibTeX_Proceedings_TitledEntry, gen_bibTeX_InProceedings_Proceedings, gen_bibTeX_InProceedings_AuthoredEntry, gen_bibTeX_InProceedings_BookTitledEntry, gen_bibTeX_Booklet_DatedEntry, gen_bibTeX_Book_AuthoredEntry, gen_bibTeX_Book_DatedEntry, gen_bibTeX_Book_TitledEntry, gen_bibTeX_DatedEntry_BibTeXEntry, gen_bibTeX_TitledEntry_BibTeXEntry, gen_bibTeX_BookTitledEntry_BibTeXEntry, gen_bibTeX_Article_AuthoredEntry, gen_bibTeX_Article_DatedEntry, gen_bibTeX_Article_TitledEntry, gen_bibTeX_TechReport_AuthoredEntry, gen_bibTeX_TechReport_DatedEntry, gen_bibTeX_TechReport_TitledEntry, gen_bibTeX_Unpublished_AuthoredEntry, gen_bibTeX_Unpublished_TitledEntry, gen_bibTeX_InCollection_Book, gen_bibTeX_InCollection_BookTitledEntry, gen_bibTeX_InBook_Book, gen_bibTeX_Misc_BibTeXEntry, gen_bibTeX_ThesisEntry_AuthoredEntry, gen_bibTeX_ThesisEntry_DatedEntry, gen_bibTeX_ThesisEntry_TitledEntry, gen_bibTeX_PhDThesis_ThesisEntry, gen_bibTeX_MasterThesis_ThesisEntry},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)