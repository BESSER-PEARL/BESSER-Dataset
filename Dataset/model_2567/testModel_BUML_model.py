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
TestPackage_AbstractTestClass = Class(name="TestPackage::AbstractTestClass", is_abstract=True)
TestPackage_TestClass1 = Class(name="TestPackage::TestClass1")
AbstractTestClass = Class(name="AbstractTestClass")
TestPackage_TestClass2 = Class(name="TestPackage::TestClass2")
TestPackage_TestIndex = Class(name="TestPackage::TestIndex")
TestPackage_TestIndexEntry = Class(name="TestPackage::TestIndexEntry")

# TestPackage_AbstractTestClass class attributes and methods
TestPackage_AbstractTestClass_name: Property = Property(name="name", type=StringType)
TestPackage_AbstractTestClass.attributes={TestPackage_AbstractTestClass_name}

# TestPackage_TestClass1 class attributes and methods
TestPackage_TestClass1_theAttributeToListen: Property = Property(name="theAttributeToListen", type=StringType)
TestPackage_TestClass1_m_testOperation: Method = Method(name="testOperation", parameters={Parameter(name='testParameter')}, type=StringType)
TestPackage_TestClass1.attributes={TestPackage_TestClass1_theAttributeToListen}
TestPackage_TestClass1.methods={TestPackage_TestClass1_m_testOperation}

# AbstractTestClass class attributes and methods

# TestPackage_TestClass2 class attributes and methods

# TestPackage_TestIndex class attributes and methods

# TestPackage_TestIndexEntry class attributes and methods

# Relationships
entries0: BinaryAssociation = BinaryAssociation(
    name="entries0",
    ends={
        Property(name="TestPackage_TestIndexEntry", type=TestPackage_TestIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestIndex", type=TestPackage_TestIndexEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedElement1: BinaryAssociation = BinaryAssociation(
    name="referencedElement1",
    ends={
        Property(name="TestPackage_AbstractTestClass", type=TestPackage_TestIndexEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="TestPackage_TestIndexEntry2", type=TestPackage_AbstractTestClass, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_TestPackage_TestClass1_AbstractTestClass = Generalization(general=AbstractTestClass, specific=TestPackage_TestClass1)
gen_TestPackage_TestClass2_AbstractTestClass = Generalization(general=AbstractTestClass, specific=TestPackage_TestClass2)

# Domain Model
domain_model = DomainModel(
    name="TestPackage",
    types={TestPackage_AbstractTestClass, TestPackage_TestClass1, AbstractTestClass, TestPackage_TestClass2, TestPackage_TestIndex, TestPackage_TestIndexEntry},
    associations={entries0, referencedElement1},
    generalizations={gen_TestPackage_TestClass1_AbstractTestClass, gen_TestPackage_TestClass2_AbstractTestClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)