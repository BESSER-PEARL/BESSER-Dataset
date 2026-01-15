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
Library_Library = Class(name="Library::Library")
Library_Writer = Class(name="Library::Writer")
Library_Book = Class(name="Library::Book")

# Library_Library class attributes and methods
Library_Library_name: Property = Property(name="name", type=StringType)
Library_Library.attributes={Library_Library_name}

# Library_Writer class attributes and methods
Library_Writer_name: Property = Property(name="name", type=StringType)
Library_Writer.attributes={Library_Writer_name}

# Library_Book class attributes and methods
Library_Book_title: Property = Property(name="title", type=StringType)
Library_Book.attributes={Library_Book_title}

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="Library_Writer", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_Library", type=Library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="Library_Book", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_Library2", type=Library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author3: BinaryAssociation = BinaryAssociation(
    name="author3",
    ends={
        Property(name="Writer", type=Library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=Library_Writer, multiplicity=Multiplicity(0, 9999))
    }
)
books4: BinaryAssociation = BinaryAssociation(
    name="books4",
    ends={
        Property(name="Book", type=Library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=Library_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Library",
    types={Library_Library, Library_Writer, Library_Book},
    associations={writers0, books1, author3, books4},
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