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
ABC_A = Class(name="ABC::A")
ABC_B = Class(name="ABC::B")
A = Class(name="A")
ABC_C = Class(name="ABC::C")
B = Class(name="B")

# ABC_A class attributes and methods
ABC_A_m_fa0: Method = Method(name="fa0", parameters={})
ABC_A_m_fa1: Method = Method(name="fa1", parameters={})
ABC_A.methods={ABC_A_m_fa1, ABC_A_m_fa0}

# ABC_B class attributes and methods
ABC_B_m_fb0: Method = Method(name="fb0", parameters={})
ABC_B.methods={ABC_B_m_fb0}

# A class attributes and methods

# ABC_C class attributes and methods
ABC_C_m_fa1: Method = Method(name="fa1", parameters={})
ABC_C_m_fc0: Method = Method(name="fc0", parameters={})
ABC_C.methods={ABC_C_m_fa1, ABC_C_m_fc0}

# B class attributes and methods

# Generalizations
gen_ABC_B_A = Generalization(general=A, specific=ABC_B)
gen_ABC_C_B = Generalization(general=B, specific=ABC_C)

# Domain Model
domain_model = DomainModel(
    name="ABC",
    types={ABC_A, ABC_B, A, ABC_C, B},
    associations={},
    generalizations={gen_ABC_B_A, gen_ABC_C_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)