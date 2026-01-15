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
testscenario_H = Class(name="testscenario::H")
testscenario_G = Class(name="testscenario::G")
H = Class(name="H")
testscenario_F = Class(name="testscenario::F")
testscenario_E = Class(name="testscenario::E")
K = Class(name="K")
D = Class(name="D")
C = Class(name="C")
F = Class(name="F")
testscenario_M = Class(name="testscenario::M")
testscenario_L = Class(name="testscenario::L")
M = Class(name="M")
testscenario_K = Class(name="testscenario::K")
L = Class(name="L")
testscenario_I = Class(name="testscenario::I")
G = Class(name="G")
I = Class(name="I")
testscenario_D = Class(name="testscenario::D")
B = Class(name="B")
testscenario_C = Class(name="testscenario::C")
A = Class(name="A")
testscenario_B = Class(name="testscenario::B")
testscenario_A = Class(name="testscenario::A")

# testscenario_H class attributes and methods

# testscenario_G class attributes and methods

# H class attributes and methods

# testscenario_F class attributes and methods

# testscenario_E class attributes and methods

# K class attributes and methods

# D class attributes and methods

# C class attributes and methods

# F class attributes and methods

# testscenario_M class attributes and methods

# testscenario_L class attributes and methods

# M class attributes and methods

# testscenario_K class attributes and methods

# L class attributes and methods

# testscenario_I class attributes and methods

# G class attributes and methods

# I class attributes and methods

# testscenario_D class attributes and methods

# B class attributes and methods

# testscenario_C class attributes and methods

# A class attributes and methods

# testscenario_B class attributes and methods

# testscenario_A class attributes and methods

# Generalizations
gen_testscenario_G_H = Generalization(general=H, specific=testscenario_G)
gen_testscenario_E_K = Generalization(general=K, specific=testscenario_E)
gen_testscenario_E_D = Generalization(general=D, specific=testscenario_E)
gen_testscenario_E_C = Generalization(general=C, specific=testscenario_E)
gen_testscenario_L_M = Generalization(general=M, specific=testscenario_L)
gen_testscenario_K_L = Generalization(general=L, specific=testscenario_K)
gen_testscenario_E_F = Generalization(general=F, specific=testscenario_E)
gen_testscenario_E_G = Generalization(general=G, specific=testscenario_E)
gen_testscenario_E_I = Generalization(general=I, specific=testscenario_E)
gen_testscenario_D_B = Generalization(general=B, specific=testscenario_D)
gen_testscenario_C_A = Generalization(general=A, specific=testscenario_C)
gen_testscenario_B_A = Generalization(general=A, specific=testscenario_B)

# Domain Model
domain_model = DomainModel(
    name="testscenario",
    types={testscenario_H, testscenario_G, H, testscenario_F, testscenario_E, K, D, C, F, testscenario_M, testscenario_L, M, testscenario_K, L, testscenario_I, G, I, testscenario_D, B, testscenario_C, A, testscenario_B, testscenario_A},
    associations={},
    generalizations={gen_testscenario_G_H, gen_testscenario_E_K, gen_testscenario_E_D, gen_testscenario_E_C, gen_testscenario_L_M, gen_testscenario_K_L, gen_testscenario_E_F, gen_testscenario_E_G, gen_testscenario_E_I, gen_testscenario_D_B, gen_testscenario_C_A, gen_testscenario_B_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)