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
doublemulti_A = Class(name="doublemulti::A")
doublemulti_B = Class(name="doublemulti::B")
doublemulti_C = Class(name="doublemulti::C")
A = Class(name="A")
B = Class(name="B")
doublemulti_D = Class(name="doublemulti::D")

# doublemulti_A class attributes and methods

# doublemulti_B class attributes and methods

# doublemulti_C class attributes and methods

# A class attributes and methods

# B class attributes and methods

# doublemulti_D class attributes and methods

# Generalizations
gen_doublemulti_C_A = Generalization(general=A, specific=doublemulti_C)
gen_doublemulti_C_B = Generalization(general=B, specific=doublemulti_C)
gen_doublemulti_D_B = Generalization(general=B, specific=doublemulti_D)
gen_doublemulti_D_A = Generalization(general=A, specific=doublemulti_D)

# Domain Model
domain_model = DomainModel(
    name="doublemulti",
    types={doublemulti_A, doublemulti_B, doublemulti_C, A, B, doublemulti_D},
    associations={},
    generalizations={gen_doublemulti_C_A, gen_doublemulti_C_B, gen_doublemulti_D_B, gen_doublemulti_D_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)