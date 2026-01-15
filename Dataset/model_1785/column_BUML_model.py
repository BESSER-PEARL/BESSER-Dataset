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
column_Book = Class(name="column::Book")

# column_Book class attributes and methods
column_Book_title: Property = Property(name="title", type=StringType)
column_Book_pages: Property = Property(name="pages", type=StringType)
column_Book_weight: Property = Property(name="weight", type=StringType)
column_Book_author: Property = Property(name="author", type=StringType)
column_Book.attributes={column_Book_pages, column_Book_author, column_Book_weight, column_Book_title}

# Domain Model
domain_model = DomainModel(
    name="column",
    types={column_Book},
    associations={},
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