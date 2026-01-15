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
edatatypeColumn_Book = Class(name="edatatypeColumn::Book")

# edatatypeColumn_Book class attributes and methods
edatatypeColumn_Book_title: Property = Property(name="title", type=StringType)
edatatypeColumn_Book_pages: Property = Property(name="pages", type=StringType)
edatatypeColumn_Book_weight: Property = Property(name="weight", type=StringType)
edatatypeColumn_Book_author: Property = Property(name="author", type=StringType)
edatatypeColumn_Book.attributes={edatatypeColumn_Book_author, edatatypeColumn_Book_pages, edatatypeColumn_Book_title, edatatypeColumn_Book_weight}

# Domain Model
domain_model = DomainModel(
    name="edatatypeColumn",
    types={edatatypeColumn_Book},
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