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
testmultipleinheritanceedgeclasses_D = Class(name="testmultipleinheritanceedgeclasses::D")
testmultipleinheritanceedgeclasses_A = Class(name="testmultipleinheritanceedgeclasses::A")
C = Class(name="C")
testmultipleinheritanceedgeclasses_EdgeAB = Class(name="testmultipleinheritanceedgeclasses::EdgeAB")
EdgeCD = Class(name="EdgeCD")
testmultipleinheritanceedgeclasses_B = Class(name="testmultipleinheritanceedgeclasses::B")
D = Class(name="D")
testmultipleinheritanceedgeclasses_BetterEdgeAB = Class(name="testmultipleinheritanceedgeclasses::BetterEdgeAB")
EdgeAB = Class(name="EdgeAB")
testmultipleinheritanceedgeclasses_C = Class(name="testmultipleinheritanceedgeclasses::C")
testmultipleinheritanceedgeclasses_EdgeCD = Class(name="testmultipleinheritanceedgeclasses::EdgeCD")
testmultipleinheritanceedgeclasses_K = Class(name="testmultipleinheritanceedgeclasses::K")
testmultipleinheritanceedgeclasses_EdgeKL = Class(name="testmultipleinheritanceedgeclasses::EdgeKL")
testmultipleinheritanceedgeclasses_L = Class(name="testmultipleinheritanceedgeclasses::L")
testmultipleinheritanceedgeclasses_BetterEdgeKL = Class(name="testmultipleinheritanceedgeclasses::BetterEdgeKL")
EdgeKL = Class(name="EdgeKL")

# testmultipleinheritanceedgeclasses_D class attributes and methods

# testmultipleinheritanceedgeclasses_A class attributes and methods

# C class attributes and methods

# testmultipleinheritanceedgeclasses_EdgeAB class attributes and methods

# EdgeCD class attributes and methods

# testmultipleinheritanceedgeclasses_B class attributes and methods

# D class attributes and methods

# testmultipleinheritanceedgeclasses_BetterEdgeAB class attributes and methods

# EdgeAB class attributes and methods

# testmultipleinheritanceedgeclasses_C class attributes and methods

# testmultipleinheritanceedgeclasses_EdgeCD class attributes and methods

# testmultipleinheritanceedgeclasses_K class attributes and methods

# testmultipleinheritanceedgeclasses_EdgeKL class attributes and methods

# testmultipleinheritanceedgeclasses_L class attributes and methods

# testmultipleinheritanceedgeclasses_BetterEdgeKL class attributes and methods

# EdgeKL class attributes and methods

# Relationships
d6: BinaryAssociation = BinaryAssociation(
    name="d6",
    ends={
        Property(name="testmultipleinheritanceedgeclasses_D", type=testmultipleinheritanceedgeclasses_EdgeCD, multiplicity=Multiplicity(1, 1)),
        Property(name="testmultipleinheritanceedgeclasses_EdgeCD7", type=testmultipleinheritanceedgeclasses_D, multiplicity=Multiplicity(1, 1))
    }
)
edgeforA0: BinaryAssociation = BinaryAssociation(
    name="edgeforA0",
    ends={
        Property(name="EdgeAB", type=testmultipleinheritanceedgeclasses_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a", type=testmultipleinheritanceedgeclasses_EdgeAB, multiplicity=Multiplicity(0, 9999))
    }
)
a1: BinaryAssociation = BinaryAssociation(
    name="a1",
    ends={
        Property(name="A", type=testmultipleinheritanceedgeclasses_EdgeAB, multiplicity=Multiplicity(1, 1)),
        Property(name="edgeforA", type=testmultipleinheritanceedgeclasses_A, multiplicity=Multiplicity(1, 1))
    }
)
b2: BinaryAssociation = BinaryAssociation(
    name="b2",
    ends={
        Property(name="B", type=testmultipleinheritanceedgeclasses_EdgeAB, multiplicity=Multiplicity(1, 1)),
        Property(name="edgeforB", type=testmultipleinheritanceedgeclasses_B, multiplicity=Multiplicity(1, 1))
    }
)
edgeforB3: BinaryAssociation = BinaryAssociation(
    name="edgeforB3",
    ends={
        Property(name="EdgeAB4", type=testmultipleinheritanceedgeclasses_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b", type=testmultipleinheritanceedgeclasses_EdgeAB, multiplicity=Multiplicity(0, 9999))
    }
)
edgeforC5: BinaryAssociation = BinaryAssociation(
    name="edgeforC5",
    ends={
        Property(name="testmultipleinheritanceedgeclasses_EdgeCD", type=testmultipleinheritanceedgeclasses_C, multiplicity=Multiplicity(1, 1)),
        Property(name="testmultipleinheritanceedgeclasses_C", type=testmultipleinheritanceedgeclasses_EdgeCD, multiplicity=Multiplicity(0, 9999))
    }
)
edgeforK8: BinaryAssociation = BinaryAssociation(
    name="edgeforK8",
    ends={
        Property(name="testmultipleinheritanceedgeclasses_EdgeKL", type=testmultipleinheritanceedgeclasses_K, multiplicity=Multiplicity(1, 1)),
        Property(name="testmultipleinheritanceedgeclasses_K", type=testmultipleinheritanceedgeclasses_EdgeKL, multiplicity=Multiplicity(0, 9999))
    }
)
l9: BinaryAssociation = BinaryAssociation(
    name="l9",
    ends={
        Property(name="testmultipleinheritanceedgeclasses_L", type=testmultipleinheritanceedgeclasses_EdgeKL, multiplicity=Multiplicity(1, 1)),
        Property(name="testmultipleinheritanceedgeclasses_EdgeKL10", type=testmultipleinheritanceedgeclasses_L, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_testmultipleinheritanceedgeclasses_A_C = Generalization(general=C, specific=testmultipleinheritanceedgeclasses_A)
gen_testmultipleinheritanceedgeclasses_EdgeAB_EdgeCD = Generalization(general=EdgeCD, specific=testmultipleinheritanceedgeclasses_EdgeAB)
gen_testmultipleinheritanceedgeclasses_B_D = Generalization(general=D, specific=testmultipleinheritanceedgeclasses_B)
gen_testmultipleinheritanceedgeclasses_BetterEdgeAB_EdgeAB = Generalization(general=EdgeAB, specific=testmultipleinheritanceedgeclasses_BetterEdgeAB)
gen_testmultipleinheritanceedgeclasses_BetterEdgeKL_EdgeKL = Generalization(general=EdgeKL, specific=testmultipleinheritanceedgeclasses_BetterEdgeKL)

# Domain Model
domain_model = DomainModel(
    name="testmultipleinheritanceedgeclasses",
    types={testmultipleinheritanceedgeclasses_D, testmultipleinheritanceedgeclasses_A, C, testmultipleinheritanceedgeclasses_EdgeAB, EdgeCD, testmultipleinheritanceedgeclasses_B, D, testmultipleinheritanceedgeclasses_BetterEdgeAB, EdgeAB, testmultipleinheritanceedgeclasses_C, testmultipleinheritanceedgeclasses_EdgeCD, testmultipleinheritanceedgeclasses_K, testmultipleinheritanceedgeclasses_EdgeKL, testmultipleinheritanceedgeclasses_L, testmultipleinheritanceedgeclasses_BetterEdgeKL, EdgeKL},
    associations={d6, edgeforA0, a1, b2, edgeforB3, edgeforC5, edgeforK8, l9},
    generalizations={gen_testmultipleinheritanceedgeclasses_A_C, gen_testmultipleinheritanceedgeclasses_EdgeAB_EdgeCD, gen_testmultipleinheritanceedgeclasses_B_D, gen_testmultipleinheritanceedgeclasses_BetterEdgeAB_EdgeAB, gen_testmultipleinheritanceedgeclasses_BetterEdgeKL_EdgeKL},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)