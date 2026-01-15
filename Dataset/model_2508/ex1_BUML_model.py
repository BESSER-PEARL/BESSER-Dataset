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
ex1_A = Class(name="ex1::A")
F = Class(name="F")
ex1_D = Class(name="ex1::D")
ex1_B = Class(name="ex1::B")
A = Class(name="A")
ex1_C = Class(name="ex1::C")
ex1_E = Class(name="ex1::E")
ex1_F = Class(name="ex1::F")
ex1_G = Class(name="ex1::G")

# ex1_A class attributes and methods
ex1_A_a1: Property = Property(name="a1", type=IntegerType)
ex1_A.attributes={ex1_A_a1}

# F class attributes and methods

# ex1_D class attributes and methods
ex1_D_dAttr: Property = Property(name="dAttr", type=BooleanType)
ex1_D.attributes={ex1_D_dAttr}

# ex1_B class attributes and methods

# A class attributes and methods

# ex1_C class attributes and methods

# ex1_E class attributes and methods

# ex1_F class attributes and methods

# ex1_G class attributes and methods

# Relationships
d0: BinaryAssociation = BinaryAssociation(
    name="d0",
    ends={
        Property(name="ex1_D", type=ex1_A, multiplicity=Multiplicity(1, 1)),
        Property(name="ex1_A", type=ex1_D, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
a2: BinaryAssociation = BinaryAssociation(
    name="a2",
    ends={
        Property(name="ex1_A3", type=ex1_A, multiplicity=Multiplicity(1, 1)),
        Property(name="ex1_A1", type=ex1_A, multiplicity=Multiplicity(0, 1))
    }
)
ce4: BinaryAssociation = BinaryAssociation(
    name="ce4",
    ends={
        Property(name="ex1_E", type=ex1_C, multiplicity=Multiplicity(1, 1)),
        Property(name="ex1_C", type=ex1_E, multiplicity=Multiplicity(0, 1))
    }
)
g5: BinaryAssociation = BinaryAssociation(
    name="g5",
    ends={
        Property(name="ex1_G", type=ex1_F, multiplicity=Multiplicity(1, 1)),
        Property(name="ex1_F", type=ex1_G, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
de6: BinaryAssociation = BinaryAssociation(
    name="de6",
    ends={
        Property(name="ex1_E8", type=ex1_D, multiplicity=Multiplicity(1, 1)),
        Property(name="ex1_D7", type=ex1_E, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ex1_A_F = Generalization(general=F, specific=ex1_A)
gen_ex1_B_A = Generalization(general=A, specific=ex1_B)
gen_ex1_C_A = Generalization(general=A, specific=ex1_C)

# Domain Model
domain_model = DomainModel(
    name="ex1",
    types={ex1_A, F, ex1_D, ex1_B, A, ex1_C, ex1_E, ex1_F, ex1_G},
    associations={d0, a2, ce4, g5, de6},
    generalizations={gen_ex1_A_F, gen_ex1_B_A, gen_ex1_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)