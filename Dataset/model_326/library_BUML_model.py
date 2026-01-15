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
            EnumerationLiteral(name="Drama"),
			EnumerationLiteral(name="History"),
			EnumerationLiteral(name="Art"),
			EnumerationLiteral(name="SciFi")
    }
)

# Classes
library_Library = Class(name="library::Library")
library_Writer = Class(name="library::Writer")
library_Book = Class(name="library::Book")

# library_Library class attributes and methods
library_Library_address: Property = Property(name="address", type=StringType)
library_Library_sumOfPages: Property = Property(name="sumOfPages", type=IntegerType)
library_Library_internalRequestCount: Property = Property(name="internalRequestCount", type=IntegerType)
library_Library_requestCount: Property = Property(name="requestCount", type=IntegerType)
library_Library.attributes={library_Library_sumOfPages, library_Library_address, library_Library_requestCount, library_Library_internalRequestCount}

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book_category: Property = Property(name="category", type=StringType)
library_Book.attributes={library_Book_pages, library_Book_category, library_Book_title}

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="library_Writer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library2", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
someBooks3: BinaryAssociation = BinaryAssociation(
    name="someBooks3",
    ends={
        Property(name="library_Book5", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library4", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
authors6: BinaryAssociation = BinaryAssociation(
    name="authors6",
    ends={
        Property(name="Writer", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=library_Writer, multiplicity=Multiplicity(0, 9999))
    }
)
books7: BinaryAssociation = BinaryAssociation(
    name="books7",
    ends={
        Property(name="Book", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
firstBook8: BinaryAssociation = BinaryAssociation(
    name="firstBook8",
    ends={
        Property(name="library_Book10", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Writer9", type=library_Book, multiplicity=Multiplicity(0, 1))
    }
)
scifiBooks11: BinaryAssociation = BinaryAssociation(
    name="scifiBooks11",
    ends={
        Property(name="library_Book13", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Writer12", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Writer, library_Book, BookCategory},
    associations={writers0, books1, someBooks3, authors6, books7, firstBook8, scifiBooks11},
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