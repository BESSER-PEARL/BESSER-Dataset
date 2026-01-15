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
library_Author = Class(name="library::Author")
library_Book = Class(name="library::Book")

# library_Author class attributes and methods
library_Author_first_name: Property = Property(name="first_name", type=StringType)
library_Author_surname: Property = Property(name="surname", type=StringType)
library_Author.attributes={library_Author_first_name, library_Author_surname}

# library_Book class attributes and methods
library_Book_name: Property = Property(name="name", type=StringType)
library_Book.attributes={library_Book_name}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Book", type=library_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
author1: BinaryAssociation = BinaryAssociation(
    name="author1",
    ends={
        Property(name="Author", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=library_Author, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Author, library_Book},
    associations={books0, author1},
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