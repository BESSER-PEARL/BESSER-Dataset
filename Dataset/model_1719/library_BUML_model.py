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
library_BookCopy = Class(name="library::BookCopy")
library_Book = Class(name="library::Book")

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_BookCopy class attributes and methods
library_BookCopy_copies: Property = Property(name="copies", type=IntegerType)
library_BookCopy.attributes={library_BookCopy_copies}

# library_Book class attributes and methods

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="library_BookCopy", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_BookCopy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book1: BinaryAssociation = BinaryAssociation(
    name="book1",
    ends={
        Property(name="library_Book", type=library_BookCopy, multiplicity=Multiplicity(1, 1)),
        Property(name="library_BookCopy2", type=library_Book, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_BookCopy, library_Book},
    associations={books0, book1},
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