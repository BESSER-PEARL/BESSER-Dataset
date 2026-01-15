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
ecore_A = Class(name="ecore::A")
EOperation = Class(name="EOperation")
ecore_B = Class(name="ecore::B")
ecore_C = Class(name="ecore::C")
B = Class(name="B")
Y = Class(name="Y")
ecore_EClass = Class(name="ecore::EClass")
C = Class(name="C")
ecore_EOperation = Class(name="ecore::EOperation")
ecore_X = Class(name="ecore::X")
A = Class(name="A")
ecore_Y = Class(name="ecore::Y")

# ecore_A class attributes and methods

# EOperation class attributes and methods

# ecore_B class attributes and methods

# ecore_C class attributes and methods

# B class attributes and methods

# Y class attributes and methods

# ecore_EClass class attributes and methods

# C class attributes and methods

# ecore_EOperation class attributes and methods

# ecore_X class attributes and methods

# A class attributes and methods

# ecore_Y class attributes and methods

# Generalizations
gen_ecore_A_EOperation = Generalization(general=EOperation, specific=ecore_A)
gen_ecore_C_B = Generalization(general=B, specific=ecore_C)
gen_ecore_C_Y = Generalization(general=Y, specific=ecore_C)
gen_ecore_EClass_C = Generalization(general=C, specific=ecore_EClass)
gen_ecore_X_A = Generalization(general=A, specific=ecore_X)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_A, EOperation, ecore_B, ecore_C, B, Y, ecore_EClass, C, ecore_EOperation, ecore_X, A, ecore_Y},
    associations={},
    generalizations={gen_ecore_A_EOperation, gen_ecore_C_B, gen_ecore_C_Y, gen_ecore_EClass_C, gen_ecore_X_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)