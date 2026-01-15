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
book_EObject = Class(name="book::EObject")
book_BookCollection = Class(name="book::BookCollection")
book_Book = Class(name="book::Book")

# book_EObject class attributes and methods

# book_BookCollection class attributes and methods

# book_Book class attributes and methods
book_Book_name: Property = Property(name="name", type=StringType)
book_Book_id: Property = Property(name="id", type=IntegerType)
book_Book.attributes={book_Book_name, book_Book_id}

# Relationships
producedFor1: BinaryAssociation = BinaryAssociation(
    name="producedFor1",
    ends={
        Property(name="book_EObject", type=book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book_Book2", type=book_EObject, multiplicity=Multiplicity(0, 1))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="book_Book", type=book_BookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="book_BookCollection", type=book_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="book",
    types={book_EObject, book_BookCollection, book_Book},
    associations={producedFor1, books0},
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