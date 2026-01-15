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
b_A = Class(name="b::A")
b_B = Class(name="b::B")
b_C = Class(name="b::C")
A = Class(name="A")

# b_A class attributes and methods
b_A_x: Property = Property(name="x", type=StringType)
b_A_m_bar: Method = Method(name="bar", parameters={}, type=StringType)
b_A.attributes={b_A_x}
b_A.methods={b_A_m_bar}

# b_B class attributes and methods
b_B_y: Property = Property(name="y", type=BooleanType)
b_B.attributes={b_B_y}

# b_C class attributes and methods
b_C_z: Property = Property(name="z", type=StringType)
b_C.attributes={b_C_z}

# A class attributes and methods

# Relationships
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="b_B", type=b_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b_B0", type=b_B, multiplicity=Multiplicity(0, 1))
    }
)
as2: BinaryAssociation = BinaryAssociation(
    name="as2",
    ends={
        Property(name="b_A", type=b_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b_B3", type=b_A, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_b_C_A = Generalization(general=A, specific=b_C)

# Domain Model
domain_model = DomainModel(
    name="b",
    types={b_A, b_B, b_C, A},
    associations={b1, as2},
    generalizations={gen_b_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)