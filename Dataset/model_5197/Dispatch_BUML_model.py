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
dispatchroot_A = Class(name="dispatchroot::A")
dispatchroot_B = Class(name="dispatchroot::B")
A = Class(name="A")
dispatchroot_C = Class(name="dispatchroot::C")

# dispatchroot_A class attributes and methods

# dispatchroot_B class attributes and methods

# A class attributes and methods

# dispatchroot_C class attributes and methods

# Generalizations
gen_dispatchroot_B_A = Generalization(general=A, specific=dispatchroot_B)

# Domain Model
domain_model = DomainModel(
    name="dispatchroot",
    types={dispatchroot_A, dispatchroot_B, A, dispatchroot_C},
    associations={},
    generalizations={gen_dispatchroot_B_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)