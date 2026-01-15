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
book_Book = Class(name="book::Book")
book_Chapter = Class(name="book::Chapter")

# book_Book class attributes and methods
book_Book_title: Property = Property(name="title", type=StringType)
book_Book.attributes={book_Book_title}

# book_Chapter class attributes and methods
book_Chapter_title: Property = Property(name="title", type=StringType)
book_Chapter_nbPages: Property = Property(name="nbPages", type=IntegerType)
book_Chapter_author: Property = Property(name="author", type=StringType)
book_Chapter.attributes={book_Chapter_title, book_Chapter_author, book_Chapter_nbPages}

# Relationships
chapters0: BinaryAssociation = BinaryAssociation(
    name="chapters0",
    ends={
        Property(name="Chapter", type=book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=book_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book1: BinaryAssociation = BinaryAssociation(
    name="book1",
    ends={
        Property(name="Book", type=book_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="chapters", type=book_Book, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="book",
    types={book_Book, book_Chapter},
    associations={chapters0, book1},
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