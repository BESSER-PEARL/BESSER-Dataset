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
eiqlibrary_Library = Class(name="eiqlibrary::Library")
eiqlibrary_Writer = Class(name="eiqlibrary::Writer")
eiqlibrary_Book = Class(name="eiqlibrary::Book")

# eiqlibrary_Library class attributes and methods
eiqlibrary_Library_address: Property = Property(name="address", type=StringType)
eiqlibrary_Library_sumOfPages: Property = Property(name="sumOfPages", type=IntegerType)
eiqlibrary_Library_internalRequestCount: Property = Property(name="internalRequestCount", type=IntegerType)
eiqlibrary_Library_requestCount: Property = Property(name="requestCount", type=IntegerType)
eiqlibrary_Library.attributes={eiqlibrary_Library_internalRequestCount, eiqlibrary_Library_address, eiqlibrary_Library_requestCount, eiqlibrary_Library_sumOfPages}

# eiqlibrary_Writer class attributes and methods
eiqlibrary_Writer_name: Property = Property(name="name", type=StringType)
eiqlibrary_Writer.attributes={eiqlibrary_Writer_name}

# eiqlibrary_Book class attributes and methods
eiqlibrary_Book_title: Property = Property(name="title", type=StringType)
eiqlibrary_Book_pages: Property = Property(name="pages", type=IntegerType)
eiqlibrary_Book_category: Property = Property(name="category", type=StringType)
eiqlibrary_Book.attributes={eiqlibrary_Book_category, eiqlibrary_Book_title, eiqlibrary_Book_pages}

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="eiqlibrary_Writer", type=eiqlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eiqlibrary_Library", type=eiqlibrary_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scifiBooks11: BinaryAssociation = BinaryAssociation(
    name="scifiBooks11",
    ends={
        Property(name="eiqlibrary_Book13", type=eiqlibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="eiqlibrary_Writer12", type=eiqlibrary_Book, multiplicity=Multiplicity(0, 9999))
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="eiqlibrary_Book", type=eiqlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eiqlibrary_Library2", type=eiqlibrary_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
someBooks3: BinaryAssociation = BinaryAssociation(
    name="someBooks3",
    ends={
        Property(name="eiqlibrary_Book5", type=eiqlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eiqlibrary_Library4", type=eiqlibrary_Book, multiplicity=Multiplicity(0, 9999))
    }
)
authors6: BinaryAssociation = BinaryAssociation(
    name="authors6",
    ends={
        Property(name="Writer", type=eiqlibrary_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=eiqlibrary_Writer, multiplicity=Multiplicity(0, 9999))
    }
)
books7: BinaryAssociation = BinaryAssociation(
    name="books7",
    ends={
        Property(name="Book", type=eiqlibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=eiqlibrary_Book, multiplicity=Multiplicity(0, 9999))
    }
)
firstBook8: BinaryAssociation = BinaryAssociation(
    name="firstBook8",
    ends={
        Property(name="eiqlibrary_Book10", type=eiqlibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="eiqlibrary_Writer9", type=eiqlibrary_Book, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="eiqlibrary",
    types={eiqlibrary_Library, eiqlibrary_Writer, eiqlibrary_Book, BookCategory},
    associations={writers0, scifiBooks11, books1, someBooks3, authors6, books7, firstBook8},
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