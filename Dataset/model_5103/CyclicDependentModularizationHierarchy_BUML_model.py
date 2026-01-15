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
testPackage_SuperType = Class(name="testPackage::SuperType")
testPackage_AnotherType = Class(name="testPackage::AnotherType")
testPackage_SubType = Class(name="testPackage::SubType")
SuperType = Class(name="SuperType")
testPackage_AnotherType2 = Class(name="testPackage::AnotherType2")

# testPackage_SuperType class attributes and methods

# testPackage_AnotherType class attributes and methods

# testPackage_SubType class attributes and methods

# SuperType class attributes and methods

# testPackage_AnotherType2 class attributes and methods

# Relationships
TestReference0: BinaryAssociation = BinaryAssociation(
    name="TestReference0",
    ends={
        Property(name="testPackage_AnotherType", type=testPackage_SuperType, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_SuperType", type=testPackage_AnotherType, multiplicity=Multiplicity(0, 1))
    }
)
TestReference1: BinaryAssociation = BinaryAssociation(
    name="TestReference1",
    ends={
        Property(name="testPackage_AnotherType23", type=testPackage_AnotherType, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_AnotherType2", type=testPackage_AnotherType2, multiplicity=Multiplicity(0, 1))
    }
)
TestReference4: BinaryAssociation = BinaryAssociation(
    name="TestReference4",
    ends={
        Property(name="testPackage_SubType", type=testPackage_AnotherType2, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_AnotherType25", type=testPackage_SubType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_testPackage_SubType_SuperType = Generalization(general=SuperType, specific=testPackage_SubType)

# Domain Model
domain_model = DomainModel(
    name="testPackage",
    types={testPackage_SuperType, testPackage_AnotherType, testPackage_SubType, SuperType, testPackage_AnotherType2},
    associations={TestReference0, TestReference1, TestReference4},
    generalizations={gen_testPackage_SubType_SuperType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)