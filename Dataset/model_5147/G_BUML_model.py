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
g_A = Class(name="g_A")
g_B = Class(name="g_B")
g_C = Class(name="g_C")
A = Class(name="A")
g_X = Class(name="g_X")
g_Y = Class(name="g_Y")

# g_A class attributes and methods
g_A_x: Property = Property(name="x", type=StringType)
g_A_m_bar: Method = Method(name="bar", parameters={}, type=StringType)
g_A.attributes={g_A_x}
g_A.methods={g_A_m_bar}

# g_B class attributes and methods
g_B_y: Property = Property(name="y", type=BooleanType)
g_B.attributes={g_B_y}

# g_C class attributes and methods
g_C_z: Property = Property(name="z", type=StringType)
g_C.attributes={g_C_z}

# A class attributes and methods

# g_X class attributes and methods
g_X_m_foo: Method = Method(name="foo", parameters={})
g_X.methods={g_X_m_foo}

# g_Y class attributes and methods
g_Y_a: Property = Property(name="a", type=StringType)
g_Y.attributes={g_Y_a}

# Relationships
as_0: BinaryAssociation = BinaryAssociation(
    name="as_0",
    ends={
        Property(name="g_A", type=g_B, multiplicity=Multiplicity(1, 1)),
        Property(name="g_B", type=g_A, multiplicity=Multiplicity(0, 9999))
    }
)
b2: BinaryAssociation = BinaryAssociation(
    name="b2",
    ends={
        Property(name="g_B3", type=g_B, multiplicity=Multiplicity(1, 1)),
        Property(name="g_B1", type=g_B, multiplicity=Multiplicity(0, 1))
    }
)
ys4: BinaryAssociation = BinaryAssociation(
    name="ys4",
    ends={
        Property(name="g_Y", type=g_X, multiplicity=Multiplicity(1, 1)),
        Property(name="g_X", type=g_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_g_C_A = Generalization(general=A, specific=g_C)

# Domain Model
domain_model = DomainModel(
    name="g",
    types={g_A, g_B, g_C, A, g_X, g_Y},
    associations={as_0, b2, ys4},
    generalizations={gen_g_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)