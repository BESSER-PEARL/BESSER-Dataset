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
mytest_A = Class(name="mytest::A")
EModelElement = Class(name="EModelElement")
mytest_B = Class(name="mytest::B")
mytest_MyRoot = Class(name="mytest::MyRoot")

# mytest_A class attributes and methods
mytest_A_name: Property = Property(name="name", type=StringType)
mytest_A.attributes={mytest_A_name}

# EModelElement class attributes and methods

# mytest_B class attributes and methods

# mytest_MyRoot class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="B", type=mytest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a", type=mytest_B, multiplicity=Multiplicity(0, 1))
    }
)
a1: BinaryAssociation = BinaryAssociation(
    name="a1",
    ends={
        Property(name="A", type=mytest_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b", type=mytest_A, multiplicity=Multiplicity(0, 1))
    }
)
aContainer2: BinaryAssociation = BinaryAssociation(
    name="aContainer2",
    ends={
        Property(name="mytest_A", type=mytest_MyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mytest_MyRoot", type=mytest_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bContainer3: BinaryAssociation = BinaryAssociation(
    name="bContainer3",
    ends={
        Property(name="mytest_B", type=mytest_MyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mytest_MyRoot4", type=mytest_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mytest_A_EModelElement = Generalization(general=EModelElement, specific=mytest_A)

# Domain Model
domain_model = DomainModel(
    name="mytest",
    types={mytest_A, EModelElement, mytest_B, mytest_MyRoot},
    associations={b0, a1, aContainer2, bContainer3},
    generalizations={gen_mytest_A_EModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)