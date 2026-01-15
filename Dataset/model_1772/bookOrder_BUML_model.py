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
bookOrder_Universe = Class(name="bookOrder::Universe")
bookOrder_BookOrder = Class(name="bookOrder::BookOrder")
bookOrder_Book = Class(name="bookOrder::Book")

# bookOrder_Universe class attributes and methods

# bookOrder_BookOrder class attributes and methods
bookOrder_BookOrder_info: Property = Property(name="info", type=StringType)
bookOrder_BookOrder.attributes={bookOrder_BookOrder_info}

# bookOrder_Book class attributes and methods
bookOrder_Book_title: Property = Property(name="title", type=StringType)
bookOrder_Book.attributes={bookOrder_Book_title}

# Relationships
bookorder0: BinaryAssociation = BinaryAssociation(
    name="bookorder0",
    ends={
        Property(name="bookOrder_BookOrder", type=bookOrder_Universe, multiplicity=Multiplicity(1, 1)),
        Property(name="bookOrder_Universe", type=bookOrder_BookOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book1: BinaryAssociation = BinaryAssociation(
    name="book1",
    ends={
        Property(name="bookOrder_Book", type=bookOrder_BookOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="bookOrder_BookOrder2", type=bookOrder_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="bookOrder",
    types={bookOrder_Universe, bookOrder_BookOrder, bookOrder_Book},
    associations={bookorder0, book1},
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