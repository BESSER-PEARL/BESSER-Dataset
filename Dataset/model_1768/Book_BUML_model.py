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
Book_Books = Class(name="Book::Books")
Book_Book = Class(name="Book::Book")
Book_Chapter = Class(name="Book::Chapter")

# Book_Books class attributes and methods

# Book_Book class attributes and methods
Book_Book_title: Property = Property(name="title", type=StringType)
Book_Book.attributes={Book_Book_title}

# Book_Chapter class attributes and methods
Book_Chapter_title: Property = Property(name="title", type=StringType)
Book_Chapter_nbPages: Property = Property(name="nbPages", type=IntegerType)
Book_Chapter_author: Property = Property(name="author", type=StringType)
Book_Chapter.attributes={Book_Chapter_title, Book_Chapter_nbPages, Book_Chapter_author}

# Relationships
chapters1: BinaryAssociation = BinaryAssociation(
    name="chapters1",
    ends={
        Property(name="Book_Chapter", type=Book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Book2", type=Book_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book3: BinaryAssociation = BinaryAssociation(
    name="book3",
    ends={
        Property(name="Book_Book5", type=Book_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Chapter4", type=Book_Book, multiplicity=Multiplicity(1, 1))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Book_Book", type=Book_Books, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Books", type=Book_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Book",
    types={Book_Books, Book_Book, Book_Chapter},
    associations={chapters1, book3, books0},
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