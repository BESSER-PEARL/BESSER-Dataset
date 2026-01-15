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
testaccessors_EAcc = Class(name="testaccessors::EAcc")

# testaccessors_EAcc class attributes and methods
testaccessors_EAcc_is: Property = Property(name="is", type=IntegerType)
testaccessors_EAcc_b: Property = Property(name="b", type=BooleanType)
testaccessors_EAcc_i: Property = Property(name="i", type=IntegerType)
testaccessors_EAcc_bs: Property = Property(name="bs", type=BooleanType)
testaccessors_EAcc.attributes={testaccessors_EAcc_b, testaccessors_EAcc_bs, testaccessors_EAcc_is, testaccessors_EAcc_i}

# Domain Model
domain_model = DomainModel(
    name="testaccessors",
    types={testaccessors_EAcc},
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