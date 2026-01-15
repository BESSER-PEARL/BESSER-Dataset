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
TestEnum: Enumeration = Enumeration(
    name="TestEnum",
    literals={
            
    }
)

SubTestEnum: Enumeration = Enumeration(
    name="SubTestEnum",
    literals={
            
    }
)

# Classes
TestPackage_TestClass = Class(name="TestPackage::TestClass")
SuperClass = Class(name="SuperClass")
UberClass = Class(name="UberClass")
SubTestClass = Class(name="SubTestClass")
TestPackage_TestInterface = Class(name="TestPackage::TestInterface", is_abstract=True)
TestPackage_SuperClass = Class(name="TestPackage::SuperClass", is_abstract=True)
TestPackage_UberClass = Class(name="TestPackage::UberClass", is_abstract=True)
TestPackage_SubPackage_SubTestClass = Class(name="TestPackage::SubPackage::SubTestClass")
TestPackage_SubPackage_SubTestInterface = Class(name="TestPackage::SubPackage::SubTestInterface", is_abstract=True)

# TestPackage_TestClass class attributes and methods

# SuperClass class attributes and methods

# UberClass class attributes and methods

# SubTestClass class attributes and methods

# TestPackage_TestInterface class attributes and methods
TestPackage_TestInterface_testAttr: Property = Property(name="testAttr", type=StringType)
TestPackage_TestInterface.attributes={TestPackage_TestInterface_testAttr}

# TestPackage_SuperClass class attributes and methods

# TestPackage_UberClass class attributes and methods

# TestPackage_SubPackage_SubTestClass class attributes and methods

# TestPackage_SubPackage_SubTestInterface class attributes and methods

# Relationships
testRef0: BinaryAssociation = BinaryAssociation(
    name="testRef0",
    ends={
        Property(name="SubTestClass", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass", type=SubTestClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
testRef721: BinaryAssociation = BinaryAssociation(
    name="testRef721",
    ends={
        Property(name="TestPackage_TestInterface23", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass22", type=TestPackage_TestInterface, multiplicity=Multiplicity(0, 9999))
    }
)
testRef21: BinaryAssociation = BinaryAssociation(
    name="testRef21",
    ends={
        Property(name="TestPackage_TestInterface", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass2", type=TestPackage_TestInterface, multiplicity=Multiplicity(0, 1))
    }
)
testRef33: BinaryAssociation = BinaryAssociation(
    name="testRef33",
    ends={
        Property(name="TestPackage_TestInterface5", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass4", type=TestPackage_TestInterface, multiplicity=Multiplicity(1, 1))
    }
)
testRef46: BinaryAssociation = BinaryAssociation(
    name="testRef46",
    ends={
        Property(name="TestPackage_TestInterface8", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass7", type=TestPackage_TestInterface, multiplicity=Multiplicity(0, 9999))
    }
)
testRef59: BinaryAssociation = BinaryAssociation(
    name="testRef59",
    ends={
        Property(name="TestPackage_TestInterface11", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass10", type=TestPackage_TestInterface, multiplicity=Multiplicity(1, 5))
    }
)
testRef612: BinaryAssociation = BinaryAssociation(
    name="testRef612",
    ends={
        Property(name="TestPackage_TestInterface14", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass13", type=TestPackage_TestInterface, multiplicity=Multiplicity(1, 9999))
    }
)
testRefWithExp15: BinaryAssociation = BinaryAssociation(
    name="testRefWithExp15",
    ends={
        Property(name="TestPackage_TestInterface17", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass16", type=TestPackage_TestInterface, multiplicity=Multiplicity(0, 1))
    }
)
testRefWithKey18: BinaryAssociation = BinaryAssociation(
    name="testRefWithKey18",
    ends={
        Property(name="TestPackage_TestInterface20", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass19", type=TestPackage_TestInterface, multiplicity=Multiplicity(0, 1))
    }
)
testRef824: BinaryAssociation = BinaryAssociation(
    name="testRef824",
    ends={
        Property(name="TestPackage_TestInterface26", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass25", type=TestPackage_TestInterface, multiplicity=Multiplicity(1, 5))
    }
)
testRef927: BinaryAssociation = BinaryAssociation(
    name="testRef927",
    ends={
        Property(name="TestPackage_TestInterface29", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass28", type=TestPackage_TestInterface, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_TestPackage_TestClass_SuperClass = Generalization(general=SuperClass, specific=TestPackage_TestClass)
gen_TestPackage_TestClass_UberClass = Generalization(general=UberClass, specific=TestPackage_TestClass)
gen_TestPackage_TestInterface_SuperClass = Generalization(general=SuperClass, specific=TestPackage_TestInterface)

# Domain Model
domain_model = DomainModel(
    name="TestPackage",
    types={TestPackage_TestClass, SuperClass, UberClass, SubTestClass, TestPackage_TestInterface, TestPackage_SuperClass, TestPackage_UberClass, TestPackage_SubPackage_SubTestClass, TestPackage_SubPackage_SubTestInterface, TestEnum, SubTestEnum},
    associations={testRef0, testRef721, testRef21, testRef33, testRef46, testRef59, testRef612, testRefWithExp15, testRefWithKey18, testRef824, testRef927},
    generalizations={gen_TestPackage_TestClass_SuperClass, gen_TestPackage_TestClass_UberClass, gen_TestPackage_TestInterface_SuperClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)