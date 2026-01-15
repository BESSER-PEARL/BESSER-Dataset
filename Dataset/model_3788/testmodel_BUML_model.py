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
testmodel_TestElement = Class(name="testmodel::TestElement")
EObject = Class(name="EObject")
testmodel_StringToStringMap = Class(name="testmodel::StringToStringMap")
testmodel_TestElementToStringMap = Class(name="testmodel::TestElementToStringMap")
testmodel_StringToTestElementMap = Class(name="testmodel::StringToTestElementMap")
testmodel_TestElementContainer = Class(name="testmodel::TestElementContainer")
testmodel_TestElementToTestElementMap = Class(name="testmodel::TestElementToTestElementMap")

# testmodel_TestElement class attributes and methods
testmodel_TestElement_name: Property = Property(name="name", type=StringType)
testmodel_TestElement_strings: Property = Property(name="strings", type=StringType)
testmodel_TestElement_description: Property = Property(name="description", type=StringType)
testmodel_TestElement.attributes={testmodel_TestElement_strings, testmodel_TestElement_description, testmodel_TestElement_name}

# EObject class attributes and methods

# testmodel_StringToStringMap class attributes and methods
testmodel_StringToStringMap_key: Property = Property(name="key", type=StringType)
testmodel_StringToStringMap_value: Property = Property(name="value", type=StringType)
testmodel_StringToStringMap.attributes={testmodel_StringToStringMap_value, testmodel_StringToStringMap_key}

# testmodel_TestElementToStringMap class attributes and methods
testmodel_TestElementToStringMap_value: Property = Property(name="value", type=StringType)
testmodel_TestElementToStringMap.attributes={testmodel_TestElementToStringMap_value}

# testmodel_StringToTestElementMap class attributes and methods
testmodel_StringToTestElementMap_key: Property = Property(name="key", type=StringType)
testmodel_StringToTestElementMap.attributes={testmodel_StringToTestElementMap_key}

# testmodel_TestElementContainer class attributes and methods

# testmodel_TestElementToTestElementMap class attributes and methods

# Relationships
stringToStringMap20: BinaryAssociation = BinaryAssociation(
    name="stringToStringMap20",
    ends={
        Property(name="testmodel_StringToStringMap", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElement21", type=testmodel_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementToStringMap22: BinaryAssociation = BinaryAssociation(
    name="elementToStringMap22",
    ends={
        Property(name="testmodel_TestElementToStringMap", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElement23", type=testmodel_TestElementToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stringToElementMap24: BinaryAssociation = BinaryAssociation(
    name="stringToElementMap24",
    ends={
        Property(name="testmodel_StringToTestElementMap", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElement25", type=testmodel_StringToTestElementMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements26: BinaryAssociation = BinaryAssociation(
    name="elements26",
    ends={
        Property(name="TestElement", type=testmodel_TestElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=testmodel_TestElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key27: BinaryAssociation = BinaryAssociation(
    name="key27",
    ends={
        Property(name="testmodel_TestElement29", type=testmodel_TestElementToStringMap, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElementToStringMap28", type=testmodel_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
references1: BinaryAssociation = BinaryAssociation(
    name="references1",
    ends={
        Property(name="testmodel_TestElement", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElement0", type=testmodel_TestElement, multiplicity=Multiplicity(0, 9999))
    }
)
containedElements3: BinaryAssociation = BinaryAssociation(
    name="containedElements3",
    ends={
        Property(name="testmodel_TestElement4", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElement2", type=testmodel_TestElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference6: BinaryAssociation = BinaryAssociation(
    name="reference6",
    ends={
        Property(name="testmodel_TestElement7", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElement5", type=testmodel_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
containedElement9: BinaryAssociation = BinaryAssociation(
    name="containedElement9",
    ends={
        Property(name="testmodel_TestElement10", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElement8", type=testmodel_TestElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
otherReference12: BinaryAssociation = BinaryAssociation(
    name="otherReference12",
    ends={
        Property(name="testmodel_TestElement13", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElement11", type=testmodel_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
containedElements215: BinaryAssociation = BinaryAssociation(
    name="containedElements215",
    ends={
        Property(name="testmodel_TestElement16", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElement14", type=testmodel_TestElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container17: BinaryAssociation = BinaryAssociation(
    name="container17",
    ends={
        Property(name="TestElementContainer", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=testmodel_TestElementContainer, multiplicity=Multiplicity(0, 1))
    }
)
elementMap18: BinaryAssociation = BinaryAssociation(
    name="elementMap18",
    ends={
        Property(name="testmodel_TestElementToTestElementMap", type=testmodel_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElement19", type=testmodel_TestElementToTestElementMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value30: BinaryAssociation = BinaryAssociation(
    name="value30",
    ends={
        Property(name="testmodel_TestElement32", type=testmodel_TestElementToTestElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElementToTestElementMap31", type=testmodel_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
key33: BinaryAssociation = BinaryAssociation(
    name="key33",
    ends={
        Property(name="testmodel_TestElement35", type=testmodel_TestElementToTestElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TestElementToTestElementMap34", type=testmodel_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
value36: BinaryAssociation = BinaryAssociation(
    name="value36",
    ends={
        Property(name="testmodel_TestElement38", type=testmodel_StringToTestElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_StringToTestElementMap37", type=testmodel_TestElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_testmodel_TestElement_EObject = Generalization(general=EObject, specific=testmodel_TestElement)

# Domain Model
domain_model = DomainModel(
    name="testmodel",
    types={testmodel_TestElement, EObject, testmodel_StringToStringMap, testmodel_TestElementToStringMap, testmodel_StringToTestElementMap, testmodel_TestElementContainer, testmodel_TestElementToTestElementMap},
    associations={stringToStringMap20, elementToStringMap22, stringToElementMap24, elements26, key27, references1, containedElements3, reference6, containedElement9, otherReference12, containedElements215, container17, elementMap18, value30, key33, value36},
    generalizations={gen_testmodel_TestElement_EObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)