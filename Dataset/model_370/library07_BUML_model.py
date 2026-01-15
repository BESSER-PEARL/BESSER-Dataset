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
library_Employee = Class(name="library::Employee")
library_Shelf = Class(name="library::Shelf")
library_Library = Class(name="library::Library")
library_Author = Class(name="library::Author")

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book.attributes={library_Book_title}

# library_Employee class attributes and methods
library_Employee_name: Property = Property(name="name", type=StringType)
library_Employee.attributes={library_Employee_name}

# library_Shelf class attributes and methods
library_Shelf_name: Property = Property(name="name", type=StringType)
library_Shelf.attributes={library_Shelf_name}

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_Author class attributes and methods
library_Author_name: Property = Property(name="name", type=StringType)
library_Author.attributes={library_Author_name}

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
shelves2: BinaryAssociation = BinaryAssociation(
    name="shelves2",
    ends={
        Property(name="library_Shelf", type=library_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Employee", type=library_Shelf, multiplicity=Multiplicity(0, 9999))
    }
)
shelves3: BinaryAssociation = BinaryAssociation(
    name="shelves3",
    ends={
        Property(name="library_Shelf4", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Shelf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors5: BinaryAssociation = BinaryAssociation(
    name="authors5",
    ends={
        Property(name="library_Author", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library6", type=library_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees7: BinaryAssociation = BinaryAssociation(
    name="employees7",
    ends={
        Property(name="library_Employee9", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library8", type=library_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books10: BinaryAssociation = BinaryAssociation(
    name="books10",
    ends={
        Property(name="library_Book", type=library_Shelf, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Shelf11", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Book, library_Employee, library_Shelf, library_Library, library_Author},
    associations={books0, author1, shelves2, shelves3, authors5, employees7, books10},
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