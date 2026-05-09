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
Book_Author = Class(name="Book_Author")
Book_Chapter = Class(name="Book_Chapter")
Book_Library = Class(name="Book_Library")
Book_Book = Class(name="Book_Book")

# Book_Author class attributes and methods
Book_Author_name: Property = Property(name="name", type=StringType)
Book_Author.attributes={Book_Author_name}

# Book_Chapter class attributes and methods
Book_Chapter_title: Property = Property(name="title", type=StringType)
Book_Chapter.attributes={Book_Chapter_title}

# Book_Library class attributes and methods

# Book_Book class attributes and methods
Book_Book_isbn: Property = Property(name="isbn", type=StringType)
Book_Book_title: Property = Property(name="title", type=StringType)
Book_Book_nbpages: Property = Property(name="nbpages", type=IntegerType)
Book_Book.attributes={Book_Book_nbpages, Book_Book_title, Book_Book_isbn}

# Relationships
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="Book_Author", type=Book_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Library2", type=Book_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors3: BinaryAssociation = BinaryAssociation(
    name="authors3",
    ends={
        Property(name="Book_Author5", type=Book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Book4", type=Book_Author, multiplicity=Multiplicity(0, 9999))
    }
)
sections6: BinaryAssociation = BinaryAssociation(
    name="sections6",
    ends={
        Property(name="Book_Chapter", type=Book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Book7", type=Book_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Book_Book", type=Book_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Library", type=Book_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Book",
    types={Book_Author, Book_Chapter, Book_Library, Book_Book},
    associations={authors1, authors3, sections6, books0},
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