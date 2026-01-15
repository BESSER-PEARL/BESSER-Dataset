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
library_Book = Class(name="library::Book")
library_Writer = Class(name="library::Writer")

# library_Library class attributes and methods

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book.attributes={library_Book_title}

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="library_Writer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library2", type=library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writers3: BinaryAssociation = BinaryAssociation(
    name="writers3",
    ends={
        Property(name="library_Writer5", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book4", type=library_Writer, multiplicity=Multiplicity(0, 9999))
    }
)
citations7: BinaryAssociation = BinaryAssociation(
    name="citations7",
    ends={
        Property(name="library_Book8", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book6", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Book, library_Writer},
    associations={books0, writers1, writers3, citations7},
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