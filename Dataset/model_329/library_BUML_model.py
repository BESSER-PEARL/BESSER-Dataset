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

# Enumerations
BookCategory: Enumeration = Enumeration(
    name="BookCategory",
    literals={
            EnumerationLiteral(name="Mystery"),
			EnumerationLiteral(name="ScienceFiction"),
			EnumerationLiteral(name="Biography")
    }
)

# Classes
bz242995_Book = Class(name="bz242995::Book")
bz242995_Writer = Class(name="bz242995::Writer")
bz242995_Library = Class(name="bz242995::Library")
bz242995_OneTimeWonder = Class(name="bz242995::OneTimeWonder")
bz242995_Author = Class(name="bz242995::Author")

# bz242995_Book class attributes and methods
bz242995_Book_title: Property = Property(name="title", type=StringType)
bz242995_Book_pages: Property = Property(name="pages", type=IntegerType)
bz242995_Book_category: Property = Property(name="category", type=StringType)
bz242995_Book.attributes={bz242995_Book_title, bz242995_Book_pages, bz242995_Book_category}

# bz242995_Writer class attributes and methods
bz242995_Writer_name: Property = Property(name="name", type=StringType)
bz242995_Writer.attributes={bz242995_Writer_name}

# bz242995_Library class attributes and methods
bz242995_Library_name: Property = Property(name="name", type=StringType)
bz242995_Library.attributes={bz242995_Library_name}

# bz242995_OneTimeWonder class attributes and methods
bz242995_OneTimeWonder_id: Property = Property(name="id", type=StringType)
bz242995_OneTimeWonder_Name: Property = Property(name="Name", type=StringType)
bz242995_OneTimeWonder.attributes={bz242995_OneTimeWonder_Name, bz242995_OneTimeWonder_id}

# bz242995_Author class attributes and methods
bz242995_Author_Name: Property = Property(name="Name", type=StringType)
bz242995_Author_id: Property = Property(name="id", type=StringType)
bz242995_Author.attributes={bz242995_Author_Name, bz242995_Author_id}

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=bz242995_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=bz242995_Writer, multiplicity=Multiplicity(1, 1))
    }
)
theAuthor5: BinaryAssociation = BinaryAssociation(
    name="theAuthor5",
    ends={
        Property(name="Author", type=bz242995_OneTimeWonder, multiplicity=Multiplicity(1, 1)),
        Property(name="theBook", type=bz242995_Author, multiplicity=Multiplicity(1, 1))
    }
)
theBook6: BinaryAssociation = BinaryAssociation(
    name="theBook6",
    ends={
        Property(name="OneTimeWonder", type=bz242995_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="theAuthor", type=bz242995_OneTimeWonder, multiplicity=Multiplicity(1, 1))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="bz242995_Writer", type=bz242995_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="bz242995_Library", type=bz242995_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books2: BinaryAssociation = BinaryAssociation(
    name="books2",
    ends={
        Property(name="bz242995_Book", type=bz242995_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="bz242995_Library3", type=bz242995_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books4: BinaryAssociation = BinaryAssociation(
    name="books4",
    ends={
        Property(name="Book", type=bz242995_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=bz242995_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bz242995",
    types={bz242995_Book, bz242995_Writer, bz242995_Library, bz242995_OneTimeWonder, bz242995_Author, BookCategory},
    associations={author0, theAuthor5, theBook6, writers1, books2, books4},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)