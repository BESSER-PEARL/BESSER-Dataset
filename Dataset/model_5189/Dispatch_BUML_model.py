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
dispatch_Container = Class(name="dispatch_Container")
dispatch_A = Class(name="dispatch_A")
dispatch_B = Class(name="dispatch_B")
A = Class(name="A")
dispatch_C = Class(name="dispatch_C")
dispatch_D = Class(name="dispatch_D")
B = Class(name="B")
dispatch_E = Class(name="dispatch_E")
dispatch_F = Class(name="dispatch_F")
C = Class(name="C")
dispatch_G = Class(name="dispatch_G")

# dispatch_Container class attributes and methods

# dispatch_A class attributes and methods

# dispatch_B class attributes and methods

# A class attributes and methods

# dispatch_C class attributes and methods

# dispatch_D class attributes and methods

# B class attributes and methods

# dispatch_E class attributes and methods

# dispatch_F class attributes and methods

# C class attributes and methods

# dispatch_G class attributes and methods

# Relationships
objs0: BinaryAssociation = BinaryAssociation(
    name="objs0",
    ends={
        Property(name="dispatch_A", type=dispatch_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="dispatch_Container", type=dispatch_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dispatch_B_A = Generalization(general=A, specific=dispatch_B)
gen_dispatch_C_A = Generalization(general=A, specific=dispatch_C)
gen_dispatch_D_B = Generalization(general=B, specific=dispatch_D)
gen_dispatch_E_B = Generalization(general=B, specific=dispatch_E)
gen_dispatch_F_C = Generalization(general=C, specific=dispatch_F)
gen_dispatch_G_C = Generalization(general=C, specific=dispatch_G)

# Domain Model
domain_model = DomainModel(
    name="dispatch",
    types={dispatch_Container, dispatch_A, dispatch_B, A, dispatch_C, dispatch_D, B, dispatch_E, dispatch_F, C, dispatch_G},
    associations={objs0},
    generalizations={gen_dispatch_B_A, gen_dispatch_C_A, gen_dispatch_D_B, gen_dispatch_E_B, gen_dispatch_F_C, gen_dispatch_G_C},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)