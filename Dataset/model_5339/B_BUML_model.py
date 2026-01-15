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
B_B2 = Class(name="B::B2")
B_B1 = Class(name="B::B1")

# B_B2 class attributes and methods
B_B2_name: Property = Property(name="name", type=StringType)
B_B2.attributes={B_B2_name}

# B_B1 class attributes and methods
B_B1_name: Property = Property(name="name", type=StringType)
B_B1.attributes={B_B1_name}

# Relationships
bssoc0: BinaryAssociation = BinaryAssociation(
    name="bssoc0",
    ends={
        Property(name="B_B2", type=B_B1, multiplicity=Multiplicity(1, 1)),
        Property(name="B_B1", type=B_B2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="B",
    types={B_B2, B_B1},
    associations={bssoc0},
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