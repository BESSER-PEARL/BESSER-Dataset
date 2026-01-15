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
model_DoorsFolder = Class(name="model::DoorsFolder")
DoorsTreeNode = Class(name="DoorsTreeNode")
model_DoorsModule = Class(name="model::DoorsModule")
model_DoorsObject = Class(name="model::DoorsObject")
model_DoorsLink = Class(name="model::DoorsLink")
model_DoorsTableRow = Class(name="model::DoorsTableRow")
DoorsObject = Class(name="DoorsObject")
model_AttributeMap = Class(name="model::AttributeMap")
model_DoorsTreeNode = Class(name="model::DoorsTreeNode", is_abstract=True)

# model_DoorsFolder class attributes and methods
model_DoorsFolder_project: Property = Property(name="project", type=BooleanType)
model_DoorsFolder.attributes={model_DoorsFolder_project}

# DoorsTreeNode class attributes and methods

# model_DoorsModule class attributes and methods
model_DoorsModule_m_getObjectAttributes: Method = Method(name="getObjectAttributes", parameters={}, type=StringType)
model_DoorsModule_m_setObjectAttributes: Method = Method(name="setObjectAttributes", parameters={Parameter(name='attrs')})
model_DoorsModule_m_getView: Method = Method(name="getView", parameters={}, type=StringType)
model_DoorsModule.methods={model_DoorsModule_m_getObjectAttributes, model_DoorsModule_m_setObjectAttributes, model_DoorsModule_m_getView}

# model_DoorsObject class attributes and methods
model_DoorsObject_objectIdentifier: Property = Property(name="objectIdentifier", type=StringType)
model_DoorsObject_objectNumber: Property = Property(name="objectNumber", type=StringType)
model_DoorsObject_objectHeading: Property = Property(name="objectHeading", type=StringType)
model_DoorsObject_text: Property = Property(name="text", type=StringType)
model_DoorsObject_absoluteNumber: Property = Property(name="absoluteNumber", type=IntegerType)
model_DoorsObject_objectText: Property = Property(name="objectText", type=StringType)
model_DoorsObject_objectShortText: Property = Property(name="objectShortText", type=StringType)
model_DoorsObject_m_isHeading: Method = Method(name="isHeading", parameters={}, type=BooleanType)
model_DoorsObject_m_getObjectLevel: Method = Method(name="getObjectLevel", parameters={}, type=IntegerType)
model_DoorsObject.attributes={model_DoorsObject_objectNumber, model_DoorsObject_objectShortText, model_DoorsObject_absoluteNumber, model_DoorsObject_objectHeading, model_DoorsObject_objectIdentifier, model_DoorsObject_objectText, model_DoorsObject_text}
model_DoorsObject.methods={model_DoorsObject_m_isHeading, model_DoorsObject_m_getObjectLevel}

# model_DoorsLink class attributes and methods
model_DoorsLink_targetModule: Property = Property(name="targetModule", type=StringType)
model_DoorsLink_targetObject: Property = Property(name="targetObject", type=StringType)
model_DoorsLink_m_getLinkStatus: Method = Method(name="getLinkStatus", parameters={}, type=StringType)
model_DoorsLink_m_resolve: Method = Method(name="resolve", parameters={}, type=DoorsObject)
model_DoorsLink_m_resolve: Method = Method(name="resolve", parameters={Parameter(name='sourceOverride')}, type=DoorsObject)
model_DoorsLink.attributes={model_DoorsLink_targetModule, model_DoorsLink_targetObject}
model_DoorsLink.methods={model_DoorsLink_m_resolve, model_DoorsLink_m_resolve, model_DoorsLink_m_getLinkStatus}

# model_DoorsTableRow class attributes and methods

# DoorsObject class attributes and methods

# model_AttributeMap class attributes and methods
model_AttributeMap_key: Property = Property(name="key", type=StringType)
model_AttributeMap_value: Property = Property(name="value", type=StringType)
model_AttributeMap.attributes={model_AttributeMap_value, model_AttributeMap_key}

# model_DoorsTreeNode class attributes and methods
model_DoorsTreeNode_name: Property = Property(name="name", type=StringType)
model_DoorsTreeNode_fullName: Property = Property(name="fullName", type=StringType)
model_DoorsTreeNode_fullNameSegments: Property = Property(name="fullNameSegments", type=StringType)
model_DoorsTreeNode_m_getChild: Method = Method(name="getChild", parameters={Parameter(name='name')}, type=DoorsTreeNode)
model_DoorsTreeNode_m_hasTag: Method = Method(name="hasTag", parameters={Parameter(name='tag')}, type=BooleanType)
model_DoorsTreeNode_m_hasTag: Method = Method(name="hasTag", parameters={Parameter(name='pattern')}, type=BooleanType)
model_DoorsTreeNode_m_getTags: Method = Method(name="getTags", parameters={}, type=StringType)
model_DoorsTreeNode_m_setTag: Method = Method(name="setTag", parameters={Parameter(name='tag')})
model_DoorsTreeNode_m_removeTag: Method = Method(name="removeTag", parameters={Parameter(name='tag')})
model_DoorsTreeNode_m_removeTag: Method = Method(name="removeTag", parameters={Parameter(name='pattern')})
model_DoorsTreeNode_m_canCopyFrom: Method = Method(name="canCopyFrom", parameters={Parameter(name='node')}, type=BooleanType)
model_DoorsTreeNode_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
model_DoorsTreeNode.attributes={model_DoorsTreeNode_fullNameSegments, model_DoorsTreeNode_name, model_DoorsTreeNode_fullName}
model_DoorsTreeNode.methods={model_DoorsTreeNode_m_removeTag, model_DoorsTreeNode_m_hasTag, model_DoorsTreeNode_m_hasTag, model_DoorsTreeNode_m_toString, model_DoorsTreeNode_m_getTags, model_DoorsTreeNode_m_getChild, model_DoorsTreeNode_m_setTag, model_DoorsTreeNode_m_canCopyFrom, model_DoorsTreeNode_m_removeTag}

# Relationships
outgoingLinks0: BinaryAssociation = BinaryAssociation(
    name="outgoingLinks0",
    ends={
        Property(name="DoorsLink", type=model_DoorsObject, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=model_DoorsLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent5: BinaryAssociation = BinaryAssociation(
    name="parent5",
    ends={
        Property(name="DoorsTreeNode6", type=model_DoorsTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=model_DoorsTreeNode, multiplicity=Multiplicity(0, 1))
    }
)
attributes7: BinaryAssociation = BinaryAssociation(
    name="attributes7",
    ends={
        Property(name="model_AttributeMap", type=model_DoorsTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DoorsTreeNode", type=model_AttributeMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="DoorsObject", type=model_DoorsLink, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingLinks", type=model_DoorsObject, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="DoorsTreeNode", type=model_DoorsTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=model_DoorsTreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_DoorsFolder_DoorsTreeNode = Generalization(general=DoorsTreeNode, specific=model_DoorsFolder)
gen_model_DoorsModule_DoorsTreeNode = Generalization(general=DoorsTreeNode, specific=model_DoorsModule)
gen_model_DoorsObject_DoorsTreeNode = Generalization(general=DoorsTreeNode, specific=model_DoorsObject)
gen_model_DoorsTableRow_DoorsObject = Generalization(general=DoorsObject, specific=model_DoorsTableRow)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_DoorsFolder, DoorsTreeNode, model_DoorsModule, model_DoorsObject, model_DoorsLink, model_DoorsTableRow, DoorsObject, model_AttributeMap, model_DoorsTreeNode},
    associations={outgoingLinks0, parent5, attributes7, source1, children3},
    generalizations={gen_model_DoorsFolder_DoorsTreeNode, gen_model_DoorsModule_DoorsTreeNode, gen_model_DoorsObject_DoorsTreeNode, gen_model_DoorsTableRow_DoorsObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)