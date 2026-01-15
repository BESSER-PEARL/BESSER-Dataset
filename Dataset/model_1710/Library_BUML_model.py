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
library_Book = Class(name="library::Book")
library_Library = Class(name="library::Library")
library_Author = Class(name="library::Author")

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book.attributes={library_Book_title, library_Book_pages}

# library_Library class attributes and methods

# library_Author class attributes and methods
library_Author_name: Property = Property(name="name", type=StringType)
library_Author_surname: Property = Property(name="surname", type=StringType)
library_Author_birthdate: Property = Property(name="birthdate", type=DateType)
library_Author.attributes={library_Author_birthdate, library_Author_surname, library_Author_name}

# Relationships
authors0: BinaryAssociation = BinaryAssociation(
    name="authors0",
    ends={
        Property(name="library_Author", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book", type=library_Author, multiplicity=Multiplicity(0, 9999))
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="library_Book2", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors3: BinaryAssociation = BinaryAssociation(
    name="authors3",
    ends={
        Property(name="library_Author5", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library4", type=library_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Book, library_Library, library_Author},
    associations={authors0, books1, authors3},
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