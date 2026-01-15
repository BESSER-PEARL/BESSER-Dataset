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
entity_Book = Class(name="entity::Book")
entity_Writer = Class(name="entity::Writer")

# entity_Book class attributes and methods
entity_Book_title: Property = Property(name="title", type=StringType)
entity_Book.attributes={entity_Book_title}

# entity_Writer class attributes and methods
entity_Writer_name: Property = Property(name="name", type=StringType)
entity_Writer.attributes={entity_Writer_name}

# Domain Model
domain_model = DomainModel(
    name="entity",
    types={entity_Book, entity_Writer},
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