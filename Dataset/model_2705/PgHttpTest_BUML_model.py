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
pghttptest_A = Class(name="pghttptest::A")
pghttptest_B = Class(name="pghttptest::B")
pghttptest_Root = Class(name="pghttptest::Root")
pghttptest_C = Class(name="pghttptest::C")
pghttptest_D = Class(name="pghttptest::D")
C = Class(name="C")
pghttptest_Priv = Class(name="pghttptest::Priv")

# pghttptest_A class attributes and methods
pghttptest_A_name: Property = Property(name="name", type=StringType)
pghttptest_A_value: Property = Property(name="value", type=IntegerType)
pghttptest_A.attributes={pghttptest_A_name, pghttptest_A_value}

# pghttptest_B class attributes and methods
pghttptest_B_priv1: Property = Property(name="priv1", type=IntegerType)
pghttptest_B_m_lastC: Method = Method(name="lastC", parameters={}, type=StringType)
pghttptest_B_m_priv2: Method = Method(name="priv2", parameters={}, type=StringType)
pghttptest_B.attributes={pghttptest_B_priv1}
pghttptest_B.methods={pghttptest_B_m_priv2, pghttptest_B_m_lastC}

# pghttptest_Root class attributes and methods

# pghttptest_C class attributes and methods
pghttptest_C_name: Property = Property(name="name", type=StringType)
pghttptest_C_m_rotName: Method = Method(name="rotName", parameters={Parameter(name='update'), Parameter(name='distance')}, type=StringType)
pghttptest_C.attributes={pghttptest_C_name}
pghttptest_C.methods={pghttptest_C_m_rotName}

# pghttptest_D class attributes and methods

# C class attributes and methods

# pghttptest_Priv class attributes and methods
pghttptest_Priv_name: Property = Property(name="name", type=StringType)
pghttptest_Priv.attributes={pghttptest_Priv_name}

# Relationships
as0: BinaryAssociation = BinaryAssociation(
    name="as0",
    ends={
        Property(name="pghttptest_A", type=pghttptest_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="pghttptest_Root", type=pghttptest_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="pghttptest_B", type=pghttptest_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="pghttptest_Root2", type=pghttptest_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cs3: BinaryAssociation = BinaryAssociation(
    name="cs3",
    ends={
        Property(name="pghttptest_C", type=pghttptest_B, multiplicity=Multiplicity(1, 1)),
        Property(name="pghttptest_B4", type=pghttptest_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pghttptest_D_C = Generalization(general=C, specific=pghttptest_D)

# Domain Model
domain_model = DomainModel(
    name="pghttptest",
    types={pghttptest_A, pghttptest_B, pghttptest_Root, pghttptest_C, pghttptest_D, C, pghttptest_Priv},
    associations={as0, b1, cs3},
    generalizations={gen_pghttptest_D_C},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)