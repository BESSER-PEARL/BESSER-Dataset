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
e_Y = Class(name="e_Y")
e_A = Class(name="e_A")
e_B = Class(name="e_B")
Y = Class(name="Y")
e_Z = Class(name="e_Z")
e_C = Class(name="e_C")
A = Class(name="A")
e_X = Class(name="e_X")

# e_Y class attributes and methods
e_Y_a: Property = Property(name="a", type=StringType)
e_Y.attributes={e_Y_a}

# e_A class attributes and methods
e_A_a: Property = Property(name="a", type=StringType)
e_A_b: Property = Property(name="b", type=StringType)
e_A_m_foo: Method = Method(name="foo", parameters={Parameter(name='e_b', type=StringType), Parameter(name='e_a', type=StringType)})
e_A.attributes={e_A_a, e_A_b}
e_A.methods={e_A_m_foo}

# e_B class attributes and methods
e_B_c: Property = Property(name="c", type=FloatType)
e_B.attributes={e_B_c}

# Y class attributes and methods

# e_Z class attributes and methods
e_Z_b: Property = Property(name="b", type=IntegerType)
e_Z.attributes={e_Z_b}

# e_C class attributes and methods
e_C_c: Property = Property(name="c", type=IntegerType)
e_C.attributes={e_C_c}

# A class attributes and methods

# e_X class attributes and methods
e_X_m_bar: Method = Method(name="bar", parameters={Parameter(name='e_aaa', type=StringType)})
e_X.methods={e_X_m_bar}

# Relationships
xxx0: BinaryAssociation = BinaryAssociation(
    name="xxx0",
    ends={
        Property(name="e_B", type=e_A, multiplicity=Multiplicity(1, 1)),
        Property(name="e_A", type=e_B, multiplicity=Multiplicity(0, 1))
    }
)
bs1: BinaryAssociation = BinaryAssociation(
    name="bs1",
    ends={
        Property(name="e_B3", type=e_A, multiplicity=Multiplicity(1, 1)),
        Property(name="e_A2", type=e_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
yyy4: BinaryAssociation = BinaryAssociation(
    name="yyy4",
    ends={
        Property(name="e_Z", type=e_B, multiplicity=Multiplicity(1, 1)),
        Property(name="e_B5", type=e_Z, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cc6: BinaryAssociation = BinaryAssociation(
    name="cc6",
    ends={
        Property(name="C", type=e_B, multiplicity=Multiplicity(1, 1)),
        Property(name="cc", type=e_C, multiplicity=Multiplicity(1, 1))
    }
)
cc7: BinaryAssociation = BinaryAssociation(
    name="cc7",
    ends={
        Property(name="B", type=e_C, multiplicity=Multiplicity(1, 1)),
        Property(name="cc8", type=e_B, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_e_B_Y = Generalization(general=Y, specific=e_B)
gen_e_C_A = Generalization(general=A, specific=e_C)
gen_e_X_A = Generalization(general=A, specific=e_X)

# Domain Model
domain_model = DomainModel(
    name="e",
    types={e_Y, e_A, e_B, Y, e_Z, e_C, A, e_X},
    associations={xxx0, bs1, yyy4, cc6, cc7},
    generalizations={gen_e_B_Y, gen_e_C_A, gen_e_X_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)