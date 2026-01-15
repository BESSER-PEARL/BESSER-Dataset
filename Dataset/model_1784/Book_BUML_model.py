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
Book_Chapter = Class(name="Book::Chapter")
Book_Book = Class(name="Book::Book")

# Book_Chapter class attributes and methods
Book_Chapter_title: Property = Property(name="title", type=StringType)
Book_Chapter_nbPages: Property = Property(name="nbPages", type=IntegerType)
Book_Chapter.attributes={Book_Chapter_nbPages, Book_Chapter_title}

# Book_Book class attributes and methods
Book_Book_title: Property = Property(name="title", type=StringType)
Book_Book_authorName: Property = Property(name="authorName", type=StringType)
Book_Book.attributes={Book_Book_authorName, Book_Book_title}

# Relationships
chapters0: BinaryAssociation = BinaryAssociation(
    name="chapters0",
    ends={
        Property(name="Book_Chapter", type=Book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Book", type=Book_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Book",
    types={Book_Chapter, Book_Book},
    associations={chapters0},
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