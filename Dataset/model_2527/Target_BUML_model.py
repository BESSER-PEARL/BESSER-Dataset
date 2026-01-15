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
target_E = Class(name="target::E")
target_F = Class(name="target::F")
target_G = Class(name="target::G")
F = Class(name="F")
target_H = Class(name="target::H")

# target_E class attributes and methods

# target_F class attributes and methods

# target_G class attributes and methods

# F class attributes and methods

# target_H class attributes and methods

# Relationships
f0: BinaryAssociation = BinaryAssociation(
    name="f0",
    ends={
        Property(name="target_F", type=target_E, multiplicity=Multiplicity(1, 1)),
        Property(name="target_E", type=target_F, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_target_G_F = Generalization(general=F, specific=target_G)
gen_target_H_F = Generalization(general=F, specific=target_H)

# Domain Model
domain_model = DomainModel(
    name="target",
    types={target_E, target_F, target_G, F, target_H},
    associations={f0},
    generalizations={gen_target_G_F, gen_target_H_F},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)