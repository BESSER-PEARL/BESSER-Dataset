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
TestPackage_SubPackage_SubTestInterface = Class(name="TestPackage::SubPackage::SubTestInterface", is_abstract=True)
TestPackage_TestClass = Class(name="TestPackage::TestClass")
SuperClass = Class(name="SuperClass")
UberClass = Class(name="UberClass")
TestPackage_TestInterface = Class(name="TestPackage::TestInterface", is_abstract=True)
TestPackage_SuperClass = Class(name="TestPackage::SuperClass", is_abstract=True)
TestPackage_UberClass = Class(name="TestPackage::UberClass", is_abstract=True)
TestPackage_SubPackage_SubTestClass = Class(name="TestPackage::SubPackage::SubTestClass")

# TestPackage_SubPackage_SubTestInterface class attributes and methods

# TestPackage_TestClass class attributes and methods

# SuperClass class attributes and methods

# UberClass class attributes and methods

# TestPackage_TestInterface class attributes and methods

# TestPackage_SuperClass class attributes and methods

# TestPackage_UberClass class attributes and methods

# TestPackage_SubPackage_SubTestClass class attributes and methods

# Generalizations
gen_TestPackage_TestClass_SuperClass = Generalization(general=SuperClass, specific=TestPackage_TestClass)
gen_TestPackage_TestClass_UberClass = Generalization(general=UberClass, specific=TestPackage_TestClass)
gen_TestPackage_TestInterface_SuperClass = Generalization(general=SuperClass, specific=TestPackage_TestInterface)

# Domain Model
domain_model = DomainModel(
    name="TestPackage",
    types={TestPackage_SubPackage_SubTestInterface, TestPackage_TestClass, SuperClass, UberClass, TestPackage_TestInterface, TestPackage_SuperClass, TestPackage_UberClass, TestPackage_SubPackage_SubTestClass, SubTestEnum, TestEnum},
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