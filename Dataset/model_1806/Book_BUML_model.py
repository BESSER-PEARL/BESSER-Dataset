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
Book_Book = Class(name="Book::Book")
Chapter = Class(name="Chapter")
Book_Chapter = Class(name="Book::Chapter")
Book = Class(name="Book")

# Book_Book class attributes and methods
Book_Book_title: Property = Property(name="title", type=StringType)
Book_Book.attributes={Book_Book_title}

# Chapter class attributes and methods

# Book_Chapter class attributes and methods
Book_Chapter_title: Property = Property(name="title", type=StringType)
Book_Chapter_nbPages: Property = Property(name="nbPages", type=StringType)
Book_Chapter_author: Property = Property(name="author", type=StringType)
Book_Chapter.attributes={Book_Chapter_author, Book_Chapter_nbPages, Book_Chapter_title}

# Book class attributes and methods

# Relationships
chapters0: BinaryAssociation = BinaryAssociation(
    name="chapters0",
    ends={
        Property(name="#", type=Book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="1", type=Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book1: BinaryAssociation = BinaryAssociation(
    name="book1",
    ends={
        Property(name="#3", type=Book_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=Book, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Book",
    types={Book_Book, Chapter, Book_Chapter, Book},
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