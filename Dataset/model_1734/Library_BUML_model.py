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
library_Person = Class(name="library::Person")
library_Model = Class(name="library::Model")
library_Library = Class(name="library::Library")
library_Book = Class(name="library::Book")
library_Author = Class(name="library::Author")
Person = Class(name="Person")

# library_Person class attributes and methods

# library_Model class attributes and methods

# library_Library class attributes and methods

# library_Book class attributes and methods

# library_Author class attributes and methods

# Person class attributes and methods

# Relationships
borrows3: BinaryAssociation = BinaryAssociation(
    name="borrows3",
    ends={
        Property(name="library_Book4", type=library_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Person", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="Author", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="writtenBooks", type=library_Author, multiplicity=Multiplicity(1, 9999))
    }
)
writtenBooks2: BinaryAssociation = BinaryAssociation(
    name="writtenBooks2",
    ends={
        Property(name="Book", type=library_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
library5: BinaryAssociation = BinaryAssociation(
    name="library5",
    ends={
        Property(name="library_Library6", type=library_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Model", type=library_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persons7: BinaryAssociation = BinaryAssociation(
    name="persons7",
    ends={
        Property(name="library_Person9", type=library_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Model8", type=library_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_Author_Person = Generalization(general=Person, specific=library_Author)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Person, library_Model, library_Library, library_Book, library_Author, Person},
    associations={borrows3, books0, authors1, writtenBooks2, library5, persons7},
    generalizations={gen_library_Author_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)