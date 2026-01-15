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
TestPackage_TestInterface = Class(name="TestPackage::TestInterface", is_abstract=True)
TestPackage_SuperClass = Class(name="TestPackage::SuperClass", is_abstract=True)
TestPackage_UberClass = Class(name="TestPackage::UberClass", is_abstract=True)
TestPackage_SubPackage_SubTestClass = Class(name="TestPackage::SubPackage::SubTestClass")
TestPackage_SubPackage_SubTestInterface = Class(name="TestPackage::SubPackage::SubTestInterface", is_abstract=True)

# TestPackage_TestClass class attributes and methods
TestPackage_TestClass_m_testOp4: Method = Method(name="testOp4", parameters={}, type=StringType)
TestPackage_TestClass_m_testOp5: Method = Method(name="testOp5", parameters={}, type=StringType)
TestPackage_TestClass_m_testVoidOp: Method = Method(name="testVoidOp", parameters={})
TestPackage_TestClass_m_testOp: Method = Method(name="testOp", parameters={Parameter(name='testParam2'), Parameter(name='testParam')}, type=StringType)
TestPackage_TestClass_m_testOp1: Method = Method(name="testOp1", parameters={}, type=StringType)
TestPackage_TestClass_m_testOp2: Method = Method(name="testOp2", parameters={}, type=StringType)
TestPackage_TestClass_m_testOp3: Method = Method(name="testOp3", parameters={}, type=StringType)
TestPackage_TestClass_m_testOp6: Method = Method(name="testOp6", parameters={}, type=StringType)
TestPackage_TestClass_m_testOp7: Method = Method(name="testOp7", parameters={}, type=StringType)
TestPackage_TestClass_m_testOp8: Method = Method(name="testOp8", parameters={}, type=StringType)
TestPackage_TestClass_m_testOp9: Method = Method(name="testOp9", parameters={Parameter(name='testParam2'), Parameter(name='testParam')}, type=StringType)
TestPackage_TestClass.methods={TestPackage_TestClass_m_testOp6, TestPackage_TestClass_m_testOp7, TestPackage_TestClass_m_testOp2, TestPackage_TestClass_m_testOp3, TestPackage_TestClass_m_testOp8, TestPackage_TestClass_m_testOp, TestPackage_TestClass_m_testOp1, TestPackage_TestClass_m_testOp4, TestPackage_TestClass_m_testOp5, TestPackage_TestClass_m_testVoidOp, TestPackage_TestClass_m_testOp9}

# SuperClass class attributes and methods

# UberClass class attributes and methods

# TestPackage_TestInterface class attributes and methods

# TestPackage_SuperClass class attributes and methods

# TestPackage_UberClass class attributes and methods

# TestPackage_SubPackage_SubTestClass class attributes and methods

# TestPackage_SubPackage_SubTestInterface class attributes and methods

# Generalizations
gen_TestPackage_TestClass_SuperClass = Generalization(general=SuperClass, specific=TestPackage_TestClass)
gen_TestPackage_TestClass_UberClass = Generalization(general=UberClass, specific=TestPackage_TestClass)
gen_TestPackage_TestInterface_SuperClass = Generalization(general=SuperClass, specific=TestPackage_TestInterface)

# Domain Model
domain_model = DomainModel(
    name="TestPackage",
    types={TestPackage_TestClass, SuperClass, UberClass, TestPackage_TestInterface, TestPackage_SuperClass, TestPackage_UberClass, TestPackage_SubPackage_SubTestClass, TestPackage_SubPackage_SubTestInterface, TestEnum, SubTestEnum},
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