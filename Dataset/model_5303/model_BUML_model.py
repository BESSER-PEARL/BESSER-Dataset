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
root_SuperA = Class(name="root::SuperA")
root_A = Class(name="root::A")
SuperA = Class(name="SuperA")
root_B = Class(name="root::B")
root_SubA = Class(name="root::SubA")
A = Class(name="A")

# root_SuperA class attributes and methods

# root_A class attributes and methods

# SuperA class attributes and methods

# root_B class attributes and methods

# root_SubA class attributes and methods

# A class attributes and methods

# Relationships
toB0: BinaryAssociation = BinaryAssociation(
    name="toB0",
    ends={
        Property(name="root_B", type=root_A, multiplicity=Multiplicity(1, 1)),
        Property(name="root_A", type=root_B, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_root_A_SuperA = Generalization(general=SuperA, specific=root_A)
gen_root_SubA_A = Generalization(general=A, specific=root_SubA)

# Domain Model
domain_model = DomainModel(
    name="root",
    types={root_SuperA, root_A, SuperA, root_B, root_SubA, A},
    associations={toB0},
    generalizations={gen_root_A_SuperA, gen_root_SubA_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)