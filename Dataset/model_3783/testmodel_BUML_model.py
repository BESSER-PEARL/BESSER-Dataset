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
test_TestElementToStringMap = Class(name="test::TestElementToStringMap")
test_TestElementToTestElementMap = Class(name="test::TestElementToTestElementMap")
test_StringToStringMap = Class(name="test::StringToStringMap")
test_StringToTestElementMap = Class(name="test::StringToTestElementMap")
test_TypeWithFeatureMapContainment = Class(name="test::TypeWithFeatureMapContainment")
test_TestType = Class(name="test::TestType")
test_TypeWithFeatureMapNonContainment = Class(name="test::TypeWithFeatureMapNonContainment")
TestType = Class(name="TestType")

# test_TestElement class attributes and methods
test_TestElement_name: Property = Property(name="name", type=StringType)
test_TestElement_strings: Property = Property(name="strings", type=StringType)
test_TestElement_description: Property = Property(name="description", type=StringType)
test_TestElement_featureMapEntries: Property = Property(name="featureMapEntries", type=StringType)
test_TestElement.attributes={test_TestElement_description, test_TestElement_featureMapEntries, test_TestElement_strings, test_TestElement_name}

# EObject class attributes and methods

# test_TestElementToStringMap class attributes and methods
test_TestElementToStringMap_value: Property = Property(name="value", type=StringType)
test_TestElementToStringMap.attributes={test_TestElementToStringMap_value}

# test_TestElementToTestElementMap class attributes and methods

# test_StringToStringMap class attributes and methods
test_StringToStringMap_value: Property = Property(name="value", type=StringType)
test_StringToStringMap_key: Property = Property(name="key", type=StringType)
test_StringToStringMap.attributes={test_StringToStringMap_key, test_StringToStringMap_value}

# test_StringToTestElementMap class attributes and methods
test_StringToTestElementMap_key: Property = Property(name="key", type=StringType)
test_StringToTestElementMap.attributes={test_StringToTestElementMap_key}

# test_TypeWithFeatureMapContainment class attributes and methods
test_TypeWithFeatureMapContainment_mapContainment: Property = Property(name="mapContainment", type=StringType)
test_TypeWithFeatureMapContainment.attributes={test_TypeWithFeatureMapContainment_mapContainment}

# test_TestType class attributes and methods
test_TestType_name: Property = Property(name="name", type=StringType)
test_TestType.attributes={test_TestType_name}

# test_TypeWithFeatureMapNonContainment class attributes and methods
test_TypeWithFeatureMapNonContainment_map: Property = Property(name="map", type=StringType)
test_TypeWithFeatureMapNonContainment.attributes={test_TypeWithFeatureMapNonContainment_map}

# TestType class attributes and methods

# Relationships
references1: BinaryAssociation = BinaryAssociation(
    name="references1",
    ends={
        Property(name="test_TestElement0", type=test_TestElement, multiplicity=Multiplicity(0, 9999)),
        Property(name="test_TestElement", type=test_TestElement, multiplicity=Multiplicity(1, 1))
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
container14: BinaryAssociation = BinaryAssociation(
    name="container14",
    ends={
        Property(name="TestElement15", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="containedElements", type=test_TestElement, multiplicity=Multiplicity(0, 1))
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
otherReference11: BinaryAssociation = BinaryAssociation(
    name="otherReference11",
    ends={
        Property(name="test_TestElement12", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement10", type=test_TestElement, multiplicity=Multiplicity(0, 1))
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
featureMapReferences152: BinaryAssociation = BinaryAssociation(
    name="featureMapReferences152",
    ends={
        Property(name="test_TestElement53", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement51", type=test_TestElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedElement_NoOpposite49: BinaryAssociation = BinaryAssociation(
    name="containedElement_NoOpposite49",
    ends={
        Property(name="test_TestElement50", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement48", type=test_TestElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureMapReferences255: BinaryAssociation = BinaryAssociation(
    name="featureMapReferences255",
    ends={
        Property(name="test_TestElement54", type=test_TestElement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="test_TestElement56", type=test_TestElement, multiplicity=Multiplicity(1, 1))
    }
)
value60: BinaryAssociation = BinaryAssociation(
    name="value60",
    ends={
        Property(name="test_TestElement62", type=test_TestElementToTestElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElementToTestElementMap61", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
key63: BinaryAssociation = BinaryAssociation(
    name="key63",
    ends={
        Property(name="test_TestElement65", type=test_TestElementToTestElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElementToTestElementMap64", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
value66: BinaryAssociation = BinaryAssociation(
    name="value66",
    ends={
        Property(name="test_TestElement68", type=test_StringToTestElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_StringToTestElementMap67", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
key57: BinaryAssociation = BinaryAssociation(
    name="key57",
    ends={
        Property(name="test_TestElement59", type=test_TestElementToStringMap, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElementToStringMap58", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
secondKey70: BinaryAssociation = BinaryAssociation(
    name="secondKey70",
    ends={
        Property(name="test_TestType72", type=test_TypeWithFeatureMapNonContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TypeWithFeatureMapNonContainment71", type=test_TestType, multiplicity=Multiplicity(0, 9999))
    }
)
firstKeyContainment73: BinaryAssociation = BinaryAssociation(
    name="firstKeyContainment73",
    ends={
        Property(name="test_TestType74", type=test_TypeWithFeatureMapContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TypeWithFeatureMapContainment", type=test_TestType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstKey69: BinaryAssociation = BinaryAssociation(
    name="firstKey69",
    ends={
        Property(name="test_TestType", type=test_TypeWithFeatureMapNonContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TypeWithFeatureMapNonContainment", type=test_TestType, multiplicity=Multiplicity(0, 9999))
    }
)
secondKeyContainment75: BinaryAssociation = BinaryAssociation(
    name="secondKeyContainment75",
    ends={
        Property(name="test_TestType77", type=test_TypeWithFeatureMapContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TypeWithFeatureMapContainment76", type=test_TestType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test_TestElement_EObject = Generalization(general=EObject, specific=test_TestElement)
gen_test_TypeWithFeatureMapContainment_TestType = Generalization(general=TestType, specific=test_TypeWithFeatureMapContainment)
gen_test_TypeWithFeatureMapNonContainment_TestType = Generalization(general=TestType, specific=test_TypeWithFeatureMapNonContainment)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_TestElement, EObject, test_TestElementToStringMap, test_TestElementToTestElementMap, test_StringToStringMap, test_StringToTestElementMap, test_TypeWithFeatureMapContainment, test_TestType, test_TypeWithFeatureMapNonContainment, TestType},
    associations={references1, containedElements3, reference5, containedElement8, container14, stringToStringMap21, elementToStringMap23, otherReference11, srefContainer17, elementMap19, nonContained_1ToN31, nonContained_NToM34, stringToElementMap25, nonContained_NTo128, container243, containedElements_NoOpposite46, nonContained_MToN37, containedElements240, featureMapReferences152, containedElement_NoOpposite49, featureMapReferences255, value60, key63, value66, key57, secondKey70, firstKeyContainment73, firstKey69, secondKeyContainment75},
    generalizations={gen_test_TestElement_EObject, gen_test_TypeWithFeatureMapContainment_TestType, gen_test_TypeWithFeatureMapNonContainment_TestType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)