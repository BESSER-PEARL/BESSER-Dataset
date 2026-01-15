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
B_B = Class(name="B::B")

# B_B class attributes and methods
B_B_description1: Property = Property(name="description1", type=StringType)
B_B_description2: Property = Property(name="description2", type=StringType)
B_B_name: Property = Property(name="name", type=StringType)
B_B.attributes={B_B_description1, B_B_name, B_B_description2}

# Domain Model
domain_model = DomainModel(
    name="B",
    types={B_B},
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