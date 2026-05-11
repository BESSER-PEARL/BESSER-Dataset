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
c_C = Class(name="c_C")
A = Class(name="A")
c_A = Class(name="c_A")
c_B = Class(name="c_B")

# c_C class attributes and methods
c_C_c: Property = Property(name="c", type=IntegerType)
c_C_z: Property = Property(name="z", type=StringType)
c_C.attributes={c_C_c, c_C_z}

# A class attributes and methods

# c_A class attributes and methods
c_A_x: Property = Property(name="x", type=StringType)
c_A_a: Property = Property(name="a", type=StringType)
c_A_b: Property = Property(name="b", type=StringType)
c_A_m_foo: Method = Method(name="foo", parameters={Parameter(name='c_a', type=StringType), Parameter(name='c_b', type=StringType)})
c_A_m_bar: Method = Method(name="bar", parameters={}, type=StringType)
c_A.attributes={c_A_x, c_A_a, c_A_b}
c_A.methods={c_A_m_bar, c_A_m_foo}

# c_B class attributes and methods
c_B_c: Property = Property(name="c", type=FloatType)
c_B_y: Property = Property(name="y", type=BooleanType)
c_B.attributes={c_B_c, c_B_y}

# Relationships
cc1: BinaryAssociation = BinaryAssociation(
    name="cc1",
    ends={
        Property(name="C", type=c_B, multiplicity=Multiplicity(1, 1)),
        Property(name="cc", type=c_C, multiplicity=Multiplicity(1, 1))
    }
)
as_2: BinaryAssociation = BinaryAssociation(
    name="as_2",
    ends={
        Property(name="c_A4", type=c_B, multiplicity=Multiplicity(1, 1)),
        Property(name="c_B3", type=c_A, multiplicity=Multiplicity(0, 9999))
    }
)
b6: BinaryAssociation = BinaryAssociation(
    name="b6",
    ends={
        Property(name="c_B7", type=c_B, multiplicity=Multiplicity(1, 1)),
        Property(name="c_B5", type=c_B, multiplicity=Multiplicity(0, 1))
    }
)
cc8: BinaryAssociation = BinaryAssociation(
    name="cc8",
    ends={
        Property(name="B", type=c_C, multiplicity=Multiplicity(1, 1)),
        Property(name="cc9", type=c_B, multiplicity=Multiplicity(1, 1))
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="c_B", type=c_A, multiplicity=Multiplicity(1, 1)),
        Property(name="c_A", type=c_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_c_C_A = Generalization(general=A, specific=c_C)

# Domain Model
domain_model = DomainModel(
    name="c",
    types={c_C, A, c_A, c_B},
    associations={cc1, as_2, b6, cc8, bs0},
    generalizations={gen_c_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)