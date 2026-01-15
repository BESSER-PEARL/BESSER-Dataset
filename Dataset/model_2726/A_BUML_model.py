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
a_A = Class(name="a::A")
a_B = Class(name="a::B")
a_C = Class(name="a::C")
A = Class(name="A")

# a_A class attributes and methods
a_A_a: Property = Property(name="a", type=StringType)
a_A_b: Property = Property(name="b", type=StringType)
a_A_m_foo: Method = Method(name="foo", parameters={Parameter(name='b'), Parameter(name='a')})
a_A.attributes={a_A_b, a_A_a}
a_A.methods={a_A_m_foo}

# a_B class attributes and methods
a_B_c: Property = Property(name="c", type=FloatType)
a_B.attributes={a_B_c}

# a_C class attributes and methods
a_C_c: Property = Property(name="c", type=IntegerType)
a_C.attributes={a_C_c}

# A class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="a_B", type=a_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a_A", type=a_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cc1: BinaryAssociation = BinaryAssociation(
    name="cc1",
    ends={
        Property(name="C", type=a_B, multiplicity=Multiplicity(1, 1)),
        Property(name="cc", type=a_C, multiplicity=Multiplicity(1, 1))
    }
)
cc2: BinaryAssociation = BinaryAssociation(
    name="cc2",
    ends={
        Property(name="B", type=a_C, multiplicity=Multiplicity(1, 1)),
        Property(name="cc3", type=a_B, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_a_C_A = Generalization(general=A, specific=a_C)

# Domain Model
domain_model = DomainModel(
    name="a",
    types={a_A, a_B, a_C, A},
    associations={bs0, cc1, cc2},
    generalizations={gen_a_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)