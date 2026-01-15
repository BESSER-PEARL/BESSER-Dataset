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
factorydeclorder_C = Class(name="factorydeclorder::C")
B = Class(name="B")
A = Class(name="A")
factorydeclorder_A = Class(name="factorydeclorder::A")
D = Class(name="D")
factorydeclorder_B = Class(name="factorydeclorder::B")
factorydeclorder_D = Class(name="factorydeclorder::D")

# factorydeclorder_C class attributes and methods
factorydeclorder_C_fc: Property = Property(name="fc", type=BooleanType)
factorydeclorder_C.attributes={factorydeclorder_C_fc}

# B class attributes and methods

# A class attributes and methods

# factorydeclorder_A class attributes and methods
factorydeclorder_A_fa: Property = Property(name="fa", type=IntegerType)
factorydeclorder_A.attributes={factorydeclorder_A_fa}

# D class attributes and methods

# factorydeclorder_B class attributes and methods
factorydeclorder_B_fb: Property = Property(name="fb", type=StringType)
factorydeclorder_B.attributes={factorydeclorder_B_fb}

# factorydeclorder_D class attributes and methods

# Generalizations
gen_factorydeclorder_C_B = Generalization(general=B, specific=factorydeclorder_C)
gen_factorydeclorder_C_A = Generalization(general=A, specific=factorydeclorder_C)
gen_factorydeclorder_A_D = Generalization(general=D, specific=factorydeclorder_A)
gen_factorydeclorder_A_B = Generalization(general=B, specific=factorydeclorder_A)

# Domain Model
domain_model = DomainModel(
    name="factorydeclorder",
    types={factorydeclorder_C, B, A, factorydeclorder_A, D, factorydeclorder_B, factorydeclorder_D},
    associations={},
    generalizations={gen_factorydeclorder_C_B, gen_factorydeclorder_C_A, gen_factorydeclorder_A_D, gen_factorydeclorder_A_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)