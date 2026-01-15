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
listType: Enumeration = Enumeration(
    name="listType",
    literals={
            EnumerationLiteral(name="ArrayList"),
			EnumerationLiteral(name="List")
    }
)

# Classes
List_List = Class(name="List::List")
List_Element = Class(name="List::Element")
Test = Class(name="Test")
SubTestPackage_SubTest = Class(name="SubTestPackage::SubTest")
List_TestPackage_Test = Class(name="List::TestPackage::Test")
List_SubTestPackage_SubTest = Class(name="List::SubTestPackage::SubTest")
SubTestPackage_List_Element = Class(name="SubTestPackage::List::Element")
TestPackage_List_Element = Class(name="TestPackage::List::Element")

# List_List class attributes and methods
List_List_size: Property = Property(name="size", type=IntegerType)
List_List_type: Property = Property(name="type", type=StringType)
List_List.attributes={List_List_type, List_List_size}

# List_Element class attributes and methods
List_Element_name: Property = Property(name="name", type=StringType)
List_Element_value: Property = Property(name="value", type=IntegerType)
List_Element.attributes={List_Element_name, List_Element_value}

# Test class attributes and methods

# SubTestPackage_SubTest class attributes and methods

# List_TestPackage_Test class attributes and methods
List_TestPackage_Test_value: Property = Property(name="value", type=IntegerType)
List_TestPackage_Test.attributes={List_TestPackage_Test_value}

# List_SubTestPackage_SubTest class attributes and methods
List_SubTestPackage_SubTest_value: Property = Property(name="value", type=IntegerType)
List_SubTestPackage_SubTest.attributes={List_SubTestPackage_SubTest_value}

# SubTestPackage_List_Element class attributes and methods

# TestPackage_List_Element class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="List_Element", type=List_List, multiplicity=Multiplicity(1, 1)),
        Property(name="List_List", type=List_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstElement1: BinaryAssociation = BinaryAssociation(
    name="firstElement1",
    ends={
        Property(name="List_Element3", type=List_List, multiplicity=Multiplicity(1, 1)),
        Property(name="List_List2", type=List_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastElement4: BinaryAssociation = BinaryAssociation(
    name="lastElement4",
    ends={
        Property(name="List_Element6", type=List_List, multiplicity=Multiplicity(1, 1)),
        Property(name="List_List5", type=List_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
testPointer8: BinaryAssociation = BinaryAssociation(
    name="testPointer8",
    ends={
        Property(name="List_List9", type=List_List, multiplicity=Multiplicity(1, 1)),
        Property(name="List_List7", type=List_List, multiplicity=Multiplicity(0, 1))
    }
)
packagePointer10: BinaryAssociation = BinaryAssociation(
    name="packagePointer10",
    ends={
        Property(name="Test", type=List_List, multiplicity=Multiplicity(1, 1)),
        Property(name="List_List11", type=Test, multiplicity=Multiplicity(0, 1))
    }
)
subElements12: BinaryAssociation = BinaryAssociation(
    name="subElements12",
    ends={
        Property(name="List_List14", type=List_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="List_Element13", type=List_List, multiplicity=Multiplicity(0, 1))
    }
)
subTestPointer15: BinaryAssociation = BinaryAssociation(
    name="subTestPointer15",
    ends={
        Property(name="TestPackage", type=List_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="SubTestPackage", type=SubTestPackage_SubTest, multiplicity=Multiplicity(0, 1))
    }
)
elementPointer20: BinaryAssociation = BinaryAssociation(
    name="elementPointer20",
    ends={
        Property(name="Element", type=List_SubTestPackage_SubTest, multiplicity=Multiplicity(1, 1)),
        Property(name="subTestPointer", type=SubTestPackage_List_Element, multiplicity=Multiplicity(0, 1))
    }
)
elementPointer16: BinaryAssociation = BinaryAssociation(
    name="elementPointer16",
    ends={
        Property(name="TestPackage_List_Element", type=List_TestPackage_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="List_TestPackage_Test", type=TestPackage_List_Element, multiplicity=Multiplicity(0, 1))
    }
)
elementPointer217: BinaryAssociation = BinaryAssociation(
    name="elementPointer217",
    ends={
        Property(name="TestPackage_List_Element19", type=List_TestPackage_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="List_TestPackage_Test18", type=TestPackage_List_Element, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="List",
    types={List_List, List_Element, Test, SubTestPackage_SubTest, List_TestPackage_Test, List_SubTestPackage_SubTest, SubTestPackage_List_Element, TestPackage_List_Element, listType},
    associations={elements0, firstElement1, lastElement4, testPointer8, packagePointer10, subElements12, subTestPointer15, elementPointer20, elementPointer16, elementPointer217},
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