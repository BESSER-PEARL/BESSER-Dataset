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
library_Library = Class(name="library::Library")
library_Writer = Class(name="library::Writer")
library_Book = Class(name="library::Book")

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_Writer class attributes and methods
library_Writer_firstName: Property = Property(name="firstName", type=StringType)
library_Writer_lastName: Property = Property(name="lastName", type=StringType)
library_Writer.attributes={library_Writer_firstName, library_Writer_lastName}

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book.attributes={library_Book_title, library_Book_pages}

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
books3: BinaryAssociation = BinaryAssociation(
    name="books3",
    ends={
        Property(name="library_Book5", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Writer4", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
writers6: BinaryAssociation = BinaryAssociation(
    name="writers6",
    ends={
        Property(name="library_Writer8", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book7", type=library_Writer, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Writer, library_Book},
    associations={writers0, books1, books3, writers6},
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