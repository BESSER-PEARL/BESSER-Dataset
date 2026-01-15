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
mytry_Author = Class(name="mytry::Author")
mytry_Library = Class(name="mytry::Library")
mytry_Book = Class(name="mytry::Book")

# mytry_Author class attributes and methods
mytry_Author_name: Property = Property(name="name", type=StringType)
mytry_Author.attributes={mytry_Author_name}

# mytry_Library class attributes and methods

# mytry_Book class attributes and methods
mytry_Book_title: Property = Property(name="title", type=StringType)
mytry_Book.attributes={mytry_Book_title}

# Relationships
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="mytry_Author", type=mytry_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mytry_Library2", type=mytry_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors3: BinaryAssociation = BinaryAssociation(
    name="authors3",
    ends={
        Property(name="Author", type=mytry_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=mytry_Author, multiplicity=Multiplicity(0, 9999))
    }
)
books4: BinaryAssociation = BinaryAssociation(
    name="books4",
    ends={
        Property(name="Book", type=mytry_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=mytry_Book, multiplicity=Multiplicity(0, 9999))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="mytry_Book", type=mytry_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mytry_Library", type=mytry_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="mytry",
    types={mytry_Author, mytry_Library, mytry_Book},
    associations={authors1, authors3, books4, books0},
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