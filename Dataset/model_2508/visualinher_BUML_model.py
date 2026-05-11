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
visualinher_S = Class(name="visualinher_S")
visualinher_A = Class(name="visualinher_A", is_abstract=True)
visualinher_R = Class(name="visualinher_R")
visualinher_B = Class(name="visualinher_B")
I = Class(name="I")
visualinher_E = Class(name="visualinher_E")
visualinher_D = Class(name="visualinher_D")
visualinher_I = Class(name="visualinher_I")
A = Class(name="A")
visualinher_C = Class(name="visualinher_C")
N = Class(name="N")
visualinher_N = Class(name="visualinher_N", is_abstract=True)

# visualinher_S class attributes and methods

# visualinher_A class attributes and methods

# visualinher_R class attributes and methods

# visualinher_B class attributes and methods

# I class attributes and methods

# visualinher_E class attributes and methods

# visualinher_D class attributes and methods

# visualinher_I class attributes and methods

# A class attributes and methods

# visualinher_C class attributes and methods

# N class attributes and methods

# visualinher_N class attributes and methods
visualinher_N_name: Property = Property(name="name", type=StringType)
visualinher_N.attributes={visualinher_N_name}

# Relationships
as_0: BinaryAssociation = BinaryAssociation(
    name="as_0",
    ends={
        Property(name="visualinher_A", type=visualinher_S, multiplicity=Multiplicity(1, 1)),
        Property(name="visualinher_S", type=visualinher_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rs1: BinaryAssociation = BinaryAssociation(
    name="rs1",
    ends={
        Property(name="visualinher_R", type=visualinher_S, multiplicity=Multiplicity(1, 1)),
        Property(name="visualinher_S2", type=visualinher_R, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
e3: BinaryAssociation = BinaryAssociation(
    name="e3",
    ends={
        Property(name="visualinher_E", type=visualinher_B, multiplicity=Multiplicity(1, 1)),
        Property(name="visualinher_B", type=visualinher_E, multiplicity=Multiplicity(0, 1))
    }
)
fromA8: BinaryAssociation = BinaryAssociation(
    name="fromA8",
    ends={
        Property(name="visualinher_A9", type=visualinher_D, multiplicity=Multiplicity(1, 1)),
        Property(name="visualinher_D", type=visualinher_A, multiplicity=Multiplicity(0, 1))
    }
)
toE10: BinaryAssociation = BinaryAssociation(
    name="toE10",
    ends={
        Property(name="visualinher_E12", type=visualinher_D, multiplicity=Multiplicity(1, 1)),
        Property(name="visualinher_D11", type=visualinher_E, multiplicity=Multiplicity(0, 1))
    }
)
c4: BinaryAssociation = BinaryAssociation(
    name="c4",
    ends={
        Property(name="visualinher_C", type=visualinher_I, multiplicity=Multiplicity(1, 1)),
        Property(name="visualinher_I", type=visualinher_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
r5: BinaryAssociation = BinaryAssociation(
    name="r5",
    ends={
        Property(name="visualinher_R7", type=visualinher_A, multiplicity=Multiplicity(1, 1)),
        Property(name="visualinher_A6", type=visualinher_R, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_visualinher_B_I = Generalization(general=I, specific=visualinher_B)
gen_visualinher_R_N = Generalization(general=N, specific=visualinher_R)
gen_visualinher_D_A = Generalization(general=A, specific=visualinher_D)
gen_visualinher_E_A = Generalization(general=A, specific=visualinher_E)
gen_visualinher_I_A = Generalization(general=A, specific=visualinher_I)
gen_visualinher_A_N = Generalization(general=N, specific=visualinher_A)

# Domain Model
domain_model = DomainModel(
    name="visualinher",
    types={visualinher_S, visualinher_A, visualinher_R, visualinher_B, I, visualinher_E, visualinher_D, visualinher_I, A, visualinher_C, N, visualinher_N},
    associations={as_0, rs1, e3, fromA8, toE10, c4, r5},
    generalizations={gen_visualinher_B_I, gen_visualinher_R_N, gen_visualinher_D_A, gen_visualinher_E_A, gen_visualinher_I_A, gen_visualinher_A_N},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)