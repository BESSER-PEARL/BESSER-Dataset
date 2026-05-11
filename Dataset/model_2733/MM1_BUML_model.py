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
testmerge_B = Class(name="testmerge_B")
testmerge_C = Class(name="testmerge_C")
testmerge_AA = Class(name="testmerge_AA")
A = Class(name="A")
testmerge_AAA = Class(name="testmerge_AAA")
AA = Class(name="AA")
testmerge_SuperA = Class(name="testmerge_SuperA")
testmerge_SubB = Class(name="testmerge_SubB")
B = Class(name="B")
testmerge_A = Class(name="testmerge_A")
SuperA = Class(name="SuperA")

# testmerge_B class attributes and methods
testmerge_B_anAttribute: Property = Property(name="anAttribute", type=StringType)
testmerge_B_m_getA: Method = Method(name="getA", parameters={Parameter(name='testmerge_paramB', type=StringType)}, type=StringType)
testmerge_B.attributes={testmerge_B_anAttribute}
testmerge_B.methods={testmerge_B_m_getA}

# testmerge_C class attributes and methods

# testmerge_AA class attributes and methods

# A class attributes and methods

# testmerge_AAA class attributes and methods

# AA class attributes and methods

# testmerge_SuperA class attributes and methods

# testmerge_SubB class attributes and methods

# B class attributes and methods

# testmerge_A class attributes and methods

# SuperA class attributes and methods

# Relationships
toB0: BinaryAssociation = BinaryAssociation(
    name="toB0",
    ends={
        Property(name="B", type=testmerge_A, multiplicity=Multiplicity(1, 1)),
        Property(name="toA", type=testmerge_B, multiplicity=Multiplicity(0, 1))
    }
)
toA1: BinaryAssociation = BinaryAssociation(
    name="toA1",
    ends={
        Property(name="A", type=testmerge_B, multiplicity=Multiplicity(1, 1)),
        Property(name="toB", type=testmerge_A, multiplicity=Multiplicity(0, 1))
    }
)
toC2: BinaryAssociation = BinaryAssociation(
    name="toC2",
    ends={
        Property(name="testmerge_C", type=testmerge_AAA, multiplicity=Multiplicity(1, 1)),
        Property(name="testmerge_AAA", type=testmerge_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_testmerge_AA_A = Generalization(general=A, specific=testmerge_AA)
gen_testmerge_AAA_AA = Generalization(general=AA, specific=testmerge_AAA)
gen_testmerge_SubB_B = Generalization(general=B, specific=testmerge_SubB)
gen_testmerge_A_SuperA = Generalization(general=SuperA, specific=testmerge_A)

# Domain Model
domain_model = DomainModel(
    name="testmerge",
    types={testmerge_B, testmerge_C, testmerge_AA, A, testmerge_AAA, AA, testmerge_SuperA, testmerge_SubB, B, testmerge_A, SuperA},
    associations={toB0, toA1, toC2},
    generalizations={gen_testmerge_AA_A, gen_testmerge_AAA_AA, gen_testmerge_SubB_B, gen_testmerge_A_SuperA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)