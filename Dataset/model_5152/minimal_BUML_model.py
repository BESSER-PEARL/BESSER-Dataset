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

# Enumerations
MyEnum: Enumeration = Enumeration(
    name="MyEnum",
    literals={
            EnumerationLiteral(name="ABC"),
			EnumerationLiteral(name="DEF")
    }
)

# Classes
mytest_A = Class(name="mytest::A")
mytest_B = Class(name="mytest::B")
mytest_MyRoot = Class(name="mytest::MyRoot")
mytest_C = Class(name="mytest::C")
B = Class(name="B")

# mytest_A class attributes and methods
mytest_A_name: Property = Property(name="name", type=StringType)
mytest_A.attributes={mytest_A_name}

# mytest_B class attributes and methods
mytest_B_enumatt: Property = Property(name="enumatt", type=StringType)
mytest_B.attributes={mytest_B_enumatt}

# mytest_MyRoot class attributes and methods

# mytest_C class attributes and methods

# B class attributes and methods

# Relationships
aContainer0: BinaryAssociation = BinaryAssociation(
    name="aContainer0",
    ends={
        Property(name="mytest_A", type=mytest_MyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mytest_MyRoot", type=mytest_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bContainer1: BinaryAssociation = BinaryAssociation(
    name="bContainer1",
    ends={
        Property(name="mytest_B", type=mytest_MyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mytest_MyRoot2", type=mytest_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b_transient3: BinaryAssociation = BinaryAssociation(
    name="b_transient3",
    ends={
        Property(name="mytest_B5", type=mytest_MyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mytest_MyRoot4", type=mytest_B, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_mytest_C_B = Generalization(general=B, specific=mytest_C)

# Domain Model
domain_model = DomainModel(
    name="mytest",
    types={mytest_A, mytest_B, mytest_MyRoot, mytest_C, B, MyEnum},
    associations={aContainer0, bContainer1, b_transient3},
    generalizations={gen_mytest_C_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)