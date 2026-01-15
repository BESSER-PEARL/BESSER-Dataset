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
BOOKS_Chapter = Class(name="BOOKS::Chapter")
BOOKS_Book = Class(name="BOOKS::Book")

# BOOKS_Chapter class attributes and methods
BOOKS_Chapter_title: Property = Property(name="title", type=StringType)
BOOKS_Chapter_nbPages: Property = Property(name="nbPages", type=IntegerType)
BOOKS_Chapter.attributes={BOOKS_Chapter_title, BOOKS_Chapter_nbPages}

# BOOKS_Book class attributes and methods
BOOKS_Book_title: Property = Property(name="title", type=StringType)
BOOKS_Book.attributes={BOOKS_Book_title}

# Relationships
chapters0: BinaryAssociation = BinaryAssociation(
    name="chapters0",
    ends={
        Property(name="BOOKS_Chapter", type=BOOKS_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="BOOKS_Book", type=BOOKS_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="BOOKS",
    types={BOOKS_Chapter, BOOKS_Book},
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