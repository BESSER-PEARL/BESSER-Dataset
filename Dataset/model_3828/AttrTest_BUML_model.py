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
SubTestEnum: Enumeration = Enumeration(
    name="SubTestEnum",
    literals={
            
    }
)

TestEnum: Enumeration = Enumeration(
    name="TestEnum",
    literals={
            
    }
)

# Classes
TestPackage_TestClass = Class(name="TestPackage::TestClass")
SuperClass = Class(name="SuperClass")
UberClass = Class(name="UberClass")
TestPackage_SuperClass = Class(name="TestPackage::SuperClass", is_abstract=True)
TestPackage_UberClass = Class(name="TestPackage::UberClass", is_abstract=True)
TestPackage_SubPackage_SubTestClass = Class(name="TestPackage::SubPackage::SubTestClass")
TestPackage_SubPackage_SubTestInterface = Class(name="TestPackage::SubPackage::SubTestInterface", is_abstract=True)
TestPackage_TestInterface = Class(name="TestPackage::TestInterface", is_abstract=True)

# TestPackage_TestClass class attributes and methods
TestPackage_TestClass_testRealAttr: Property = Property(name="testRealAttr", type=StringType)
TestPackage_TestClass_testBooleanAttr: Property = Property(name="testBooleanAttr", type=BooleanType)
TestPackage_TestClass_testIntAttr: Property = Property(name="testIntAttr", type=IntegerType)
TestPackage_TestClass_testAttr1: Property = Property(name="testAttr1", type=IntegerType)
TestPackage_TestClass_testAttr2: Property = Property(name="testAttr2", type=IntegerType)
TestPackage_TestClass_testAttr3: Property = Property(name="testAttr3", type=IntegerType)
TestPackage_TestClass_testAttr4: Property = Property(name="testAttr4", type=IntegerType)
TestPackage_TestClass_testAttr5: Property = Property(name="testAttr5", type=IntegerType)
TestPackage_TestClass_testUnlimitedNaturalAttr: Property = Property(name="testUnlimitedNaturalAttr", type=StringType)
TestPackage_TestClass_testAttr: Property = Property(name="testAttr", type=DateType)
TestPackage_TestClass_testStringAttr: Property = Property(name="testStringAttr", type=StringType)
TestPackage_TestClass_testAttr6: Property = Property(name="testAttr6", type=IntegerType)
TestPackage_TestClass_testAttr7: Property = Property(name="testAttr7", type=IntegerType)
TestPackage_TestClass_testAttr8: Property = Property(name="testAttr8", type=IntegerType)
TestPackage_TestClass.attributes={TestPackage_TestClass_testUnlimitedNaturalAttr, TestPackage_TestClass_testAttr5, TestPackage_TestClass_testAttr1, TestPackage_TestClass_testAttr2, TestPackage_TestClass_testIntAttr, TestPackage_TestClass_testStringAttr, TestPackage_TestClass_testBooleanAttr, TestPackage_TestClass_testRealAttr, TestPackage_TestClass_testAttr8, TestPackage_TestClass_testAttr3, TestPackage_TestClass_testAttr, TestPackage_TestClass_testAttr7, TestPackage_TestClass_testAttr4, TestPackage_TestClass_testAttr6}

# SuperClass class attributes and methods

# UberClass class attributes and methods

# TestPackage_SuperClass class attributes and methods

# TestPackage_UberClass class attributes and methods

# TestPackage_SubPackage_SubTestClass class attributes and methods
TestPackage_SubPackage_SubTestClass_testIntAttr: Property = Property(name="testIntAttr", type=IntegerType)
TestPackage_SubPackage_SubTestClass_testStringAttr: Property = Property(name="testStringAttr", type=StringType)
TestPackage_SubPackage_SubTestClass_testRealAttr: Property = Property(name="testRealAttr", type=StringType)
TestPackage_SubPackage_SubTestClass_testBooleanAttr: Property = Property(name="testBooleanAttr", type=BooleanType)
TestPackage_SubPackage_SubTestClass_testAttr: Property = Property(name="testAttr", type=DateType)
TestPackage_SubPackage_SubTestClass.attributes={TestPackage_SubPackage_SubTestClass_testRealAttr, TestPackage_SubPackage_SubTestClass_testIntAttr, TestPackage_SubPackage_SubTestClass_testAttr, TestPackage_SubPackage_SubTestClass_testStringAttr, TestPackage_SubPackage_SubTestClass_testBooleanAttr}

# TestPackage_SubPackage_SubTestInterface class attributes and methods

# TestPackage_TestInterface class attributes and methods

# Generalizations
gen_TestPackage_TestClass_SuperClass = Generalization(general=SuperClass, specific=TestPackage_TestClass)
gen_TestPackage_TestClass_UberClass = Generalization(general=UberClass, specific=TestPackage_TestClass)
gen_TestPackage_TestInterface_SuperClass = Generalization(general=SuperClass, specific=TestPackage_TestInterface)

# Domain Model
domain_model = DomainModel(
    name="TestPackage",
    types={TestPackage_TestClass, SuperClass, UberClass, TestPackage_SuperClass, TestPackage_UberClass, TestPackage_SubPackage_SubTestClass, TestPackage_SubPackage_SubTestInterface, TestPackage_TestInterface, SubTestEnum, TestEnum},
    associations={},
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