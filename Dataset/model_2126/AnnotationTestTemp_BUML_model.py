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
SubTestClass = Class(name="SubTestClass")
TestPackage_SubPackage_SubTestClass = Class(name="TestPackage::SubPackage::SubTestClass")
TestPackage_SubPackage_SubTestInterface = Class(name="TestPackage::SubPackage::SubTestInterface", is_abstract=True)

# TestPackage_TestClass class attributes and methods
TestPackage_TestClass_testAttr: Property = Property(name="testAttr", type=BooleanType)
TestPackage_TestClass_m_testOp: Method = Method(name="testOp", parameters={})
TestPackage_TestClass.attributes={TestPackage_TestClass_testAttr}
TestPackage_TestClass.methods={TestPackage_TestClass_m_testOp}

# SubTestClass class attributes and methods

# TestPackage_SubPackage_SubTestClass class attributes and methods

# TestPackage_SubPackage_SubTestInterface class attributes and methods

# Relationships
testRef0: BinaryAssociation = BinaryAssociation(
    name="testRef0",
    ends={
        Property(name="SubTestClass", type=TestPackage_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestClass", type=SubTestClass, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="TestPackage",
    types={TestPackage_TestClass, SubTestClass, TestPackage_SubPackage_SubTestClass, TestPackage_SubPackage_SubTestInterface, TestEnum, SubTestEnum},
    associations={testRef0},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)