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
library_Library = Class(name="library::Library")

# library_Author class attributes and methods
library_Author_name: Property = Property(name="name", type=StringType)
library_Author_surname: Property = Property(name="surname", type=StringType)
library_Author.attributes={library_Author_name, library_Author_surname}

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book.attributes={library_Book_title}

# library_Library class attributes and methods

# Relationships
EReference00: BinaryAssociation = BinaryAssociation(
    name="EReference00",
    ends={
        Property(name="library_Author", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book", type=library_Author, multiplicity=Multiplicity(0, 1))
    }
)
author1: BinaryAssociation = BinaryAssociation(
    name="author1",
    ends={
        Property(name="library_Author3", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book2", type=library_Author, multiplicity=Multiplicity(0, 1))
    }
)
listAuthor4: BinaryAssociation = BinaryAssociation(
    name="listAuthor4",
    ends={
        Property(name="library_Author5", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listBook6: BinaryAssociation = BinaryAssociation(
    name="listBook6",
    ends={
        Property(name="library_Book8", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library7", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Author, library_Book, library_Library},
    associations={EReference00, author1, listAuthor4, listBook6},
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