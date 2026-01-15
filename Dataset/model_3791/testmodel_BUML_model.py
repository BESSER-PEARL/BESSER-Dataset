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
test_TestElement = Class(name="test::TestElement")
EObject = Class(name="EObject")
test_TestElementToTestElementMap = Class(name="test::TestElementToTestElementMap")
test_StringToStringMap = Class(name="test::StringToStringMap")
test_TestElementToStringMap = Class(name="test::TestElementToStringMap")
test_StringToTestElementMap = Class(name="test::StringToTestElementMap")

# test_TestElement class attributes and methods
test_TestElement_name: Property = Property(name="name", type=StringType)
test_TestElement_strings: Property = Property(name="strings", type=StringType)
test_TestElement_description: Property = Property(name="description", type=StringType)
test_TestElement.attributes={test_TestElement_name, test_TestElement_description, test_TestElement_strings}

# EObject class attributes and methods

# test_TestElementToTestElementMap class attributes and methods

# test_StringToStringMap class attributes and methods
test_StringToStringMap_key: Property = Property(name="key", type=StringType)
test_StringToStringMap_value: Property = Property(name="value", type=StringType)
test_StringToStringMap.attributes={test_StringToStringMap_value, test_StringToStringMap_key}

# test_TestElementToStringMap class attributes and methods
test_TestElementToStringMap_value: Property = Property(name="value", type=StringType)
test_TestElementToStringMap.attributes={test_TestElementToStringMap_value}

# test_StringToTestElementMap class attributes and methods
test_StringToTestElementMap_key: Property = Property(name="key", type=StringType)
test_StringToTestElementMap.attributes={test_StringToTestElementMap_key}

# Relationships
references1: BinaryAssociation = BinaryAssociation(
    name="references1",
    ends={
        Property(name="test_TestElement", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement0", type=test_TestElement, multiplicity=Multiplicity(0, 9999))
    }
)
containedElements3: BinaryAssociation = BinaryAssociation(
    name="containedElements3",
    ends={
        Property(name="TestElement", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=test_TestElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference5: BinaryAssociation = BinaryAssociation(
    name="reference5",
    ends={
        Property(name="test_TestElement6", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement4", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
containedElement8: BinaryAssociation = BinaryAssociation(
    name="containedElement8",
    ends={
        Property(name="TestElement9", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="srefContainer", type=test_TestElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
otherReference11: BinaryAssociation = BinaryAssociation(
    name="otherReference11",
    ends={
        Property(name="test_TestElement12", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement10", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
container14: BinaryAssociation = BinaryAssociation(
    name="container14",
    ends={
        Property(name="TestElement15", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="containedElements", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
srefContainer17: BinaryAssociation = BinaryAssociation(
    name="srefContainer17",
    ends={
        Property(name="TestElement18", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="containedElement", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
elementMap19: BinaryAssociation = BinaryAssociation(
    name="elementMap19",
    ends={
        Property(name="test_TestElementToTestElementMap", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement20", type=test_TestElementToTestElementMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stringToStringMap21: BinaryAssociation = BinaryAssociation(
    name="stringToStringMap21",
    ends={
        Property(name="test_StringToStringMap", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement22", type=test_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementToStringMap23: BinaryAssociation = BinaryAssociation(
    name="elementToStringMap23",
    ends={
        Property(name="test_TestElementToStringMap", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement24", type=test_TestElementToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stringToElementMap25: BinaryAssociation = BinaryAssociation(
    name="stringToElementMap25",
    ends={
        Property(name="test_StringToTestElementMap", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement26", type=test_StringToTestElementMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonContained_NTo128: BinaryAssociation = BinaryAssociation(
    name="nonContained_NTo128",
    ends={
        Property(name="TestElement29", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="nonContained_1ToN", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
nonContained_1ToN31: BinaryAssociation = BinaryAssociation(
    name="nonContained_1ToN31",
    ends={
        Property(name="TestElement32", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="nonContained_NTo1", type=test_TestElement, multiplicity=Multiplicity(0, 9999))
    }
)
nonContained_NToM34: BinaryAssociation = BinaryAssociation(
    name="nonContained_NToM34",
    ends={
        Property(name="TestElement35", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="nonContained_MToN", type=test_TestElement, multiplicity=Multiplicity(0, 9999))
    }
)
nonContained_MToN37: BinaryAssociation = BinaryAssociation(
    name="nonContained_MToN37",
    ends={
        Property(name="TestElement38", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="nonContained_NToM", type=test_TestElement, multiplicity=Multiplicity(0, 9999))
    }
)
containedElements240: BinaryAssociation = BinaryAssociation(
    name="containedElements240",
    ends={
        Property(name="TestElement41", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="container2", type=test_TestElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container243: BinaryAssociation = BinaryAssociation(
    name="container243",
    ends={
        Property(name="TestElement44", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="containedElements2", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
containedElements_NoOpposite46: BinaryAssociation = BinaryAssociation(
    name="containedElements_NoOpposite46",
    ends={
        Property(name="test_TestElement47", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement45", type=test_TestElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key48: BinaryAssociation = BinaryAssociation(
    name="key48",
    ends={
        Property(name="test_TestElement50", type=test_TestElementToStringMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElementToStringMap49", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
value51: BinaryAssociation = BinaryAssociation(
    name="value51",
    ends={
        Property(name="test_TestElement53", type=test_TestElementToTestElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElementToTestElementMap52", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
key54: BinaryAssociation = BinaryAssociation(
    name="key54",
    ends={
        Property(name="test_TestElement56", type=test_TestElementToTestElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElementToTestElementMap55", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
value57: BinaryAssociation = BinaryAssociation(
    name="value57",
    ends={
        Property(name="test_TestElement59", type=test_StringToTestElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_StringToTestElementMap58", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_test_TestElement_EObject = Generalization(general=EObject, specific=test_TestElement)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_TestElement, EObject, test_TestElementToTestElementMap, test_StringToStringMap, test_TestElementToStringMap, test_StringToTestElementMap},
    associations={references1, containedElements3, reference5, containedElement8, otherReference11, container14, srefContainer17, elementMap19, stringToStringMap21, elementToStringMap23, stringToElementMap25, nonContained_NTo128, nonContained_1ToN31, nonContained_NToM34, nonContained_MToN37, containedElements240, container243, containedElements_NoOpposite46, key48, value51, key54, value57},
    generalizations={gen_test_TestElement_EObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)