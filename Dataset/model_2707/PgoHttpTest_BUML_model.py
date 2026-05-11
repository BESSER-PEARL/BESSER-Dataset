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
pgohttpestest_C = Class(name="pgohttpestest_C")
pgohttpestest_D = Class(name="pgohttpestest_D")
C = Class(name="C")
pgohttpestest_Priv = Class(name="pgohttpestest_Priv")
pgohttpestest_Root = Class(name="pgohttpestest_Root")
pgohttpestest_A = Class(name="pgohttpestest_A")
pgohttpestest_B = Class(name="pgohttpestest_B")

# pgohttpestest_C class attributes and methods
pgohttpestest_C_name: Property = Property(name="name", type=StringType)
pgohttpestest_C_m_rotName: Method = Method(name="rotName", parameters={Parameter(name='pgohttpestest_distance', type=StringType), Parameter(name='pgohttpestest_update', type=StringType)}, type=StringType)
pgohttpestest_C.attributes={pgohttpestest_C_name}
pgohttpestest_C.methods={pgohttpestest_C_m_rotName}

# pgohttpestest_D class attributes and methods

# C class attributes and methods

# pgohttpestest_Priv class attributes and methods
pgohttpestest_Priv_name: Property = Property(name="name", type=StringType)
pgohttpestest_Priv.attributes={pgohttpestest_Priv_name}

# pgohttpestest_Root class attributes and methods

# pgohttpestest_A class attributes and methods
pgohttpestest_A_name: Property = Property(name="name", type=StringType)
pgohttpestest_A_value: Property = Property(name="value", type=IntegerType)
pgohttpestest_A.attributes={pgohttpestest_A_value, pgohttpestest_A_name}

# pgohttpestest_B class attributes and methods
pgohttpestest_B_priv1: Property = Property(name="priv1", type=IntegerType)
pgohttpestest_B_m_lastC: Method = Method(name="lastC", parameters={}, type=StringType)
pgohttpestest_B_m_priv2: Method = Method(name="priv2", parameters={}, type=StringType)
pgohttpestest_B.attributes={pgohttpestest_B_priv1}
pgohttpestest_B.methods={pgohttpestest_B_m_priv2, pgohttpestest_B_m_lastC}

# Relationships
cs3: BinaryAssociation = BinaryAssociation(
    name="cs3",
    ends={
        Property(name="pgohttpestest_C", type=pgohttpestest_B, multiplicity=Multiplicity(1, 1)),
        Property(name="pgohttpestest_B4", type=pgohttpestest_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
as_0: BinaryAssociation = BinaryAssociation(
    name="as_0",
    ends={
        Property(name="pgohttpestest_A", type=pgohttpestest_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="pgohttpestest_Root", type=pgohttpestest_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="pgohttpestest_B", type=pgohttpestest_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="pgohttpestest_Root2", type=pgohttpestest_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_pgohttpestest_D_C = Generalization(general=C, specific=pgohttpestest_D)

# Domain Model
domain_model = DomainModel(
    name="pgohttpestest",
    types={pgohttpestest_C, pgohttpestest_D, C, pgohttpestest_Priv, pgohttpestest_Root, pgohttpestest_A, pgohttpestest_B},
    associations={cs3, as_0, b1},
    generalizations={gen_pgohttpestest_D_C},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)