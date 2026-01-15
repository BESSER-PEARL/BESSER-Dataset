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
Y = Class(name="Y")
d_Z = Class(name="d::Z")
d_A = Class(name="d::A")
d_B = Class(name="d::B")
d_X = Class(name="d::X")
A = Class(name="A")
d_Y = Class(name="d::Y")

# Y class attributes and methods

# d_Z class attributes and methods
d_Z_b: Property = Property(name="b", type=IntegerType)
d_Z.attributes={d_Z_b}

# d_A class attributes and methods

# d_B class attributes and methods

# d_X class attributes and methods
d_X_m_baz: Method = Method(name="baz", parameters={Parameter(name='aaa')})
d_X.methods={d_X_m_baz}

# A class attributes and methods

# d_Y class attributes and methods
d_Y_a: Property = Property(name="a", type=StringType)
d_Y.attributes={d_Y_a}

# Relationships
yyy1: BinaryAssociation = BinaryAssociation(
    name="yyy1",
    ends={
        Property(name="d_Z", type=d_B, multiplicity=Multiplicity(1, 1)),
        Property(name="d_B2", type=d_Z, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
xxx0: BinaryAssociation = BinaryAssociation(
    name="xxx0",
    ends={
        Property(name="d_B", type=d_A, multiplicity=Multiplicity(1, 1)),
        Property(name="d_A", type=d_B, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_d_B_Y = Generalization(general=Y, specific=d_B)
gen_d_X_A = Generalization(general=A, specific=d_X)

# Domain Model
domain_model = DomainModel(
    name="d",
    types={Y, d_Z, d_A, d_B, d_X, A, d_Y},
    associations={yyy1, xxx0},
    generalizations={gen_d_B_Y, gen_d_X_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)