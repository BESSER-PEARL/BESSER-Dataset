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
hExample_3_RHS_X = Class(name="hExample::3::RHS::X")

# hExample_3_RHS_X class attributes and methods
hExample_3_RHS_X_att1: Property = Property(name="att1", type=StringType)
hExample_3_RHS_X_att2: Property = Property(name="att2", type=StringType)
hExample_3_RHS_X.attributes={hExample_3_RHS_X_att2, hExample_3_RHS_X_att1}

# Domain Model
domain_model = DomainModel(
    name="hExample_3_RHS",
    types={hExample_3_RHS_X},
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