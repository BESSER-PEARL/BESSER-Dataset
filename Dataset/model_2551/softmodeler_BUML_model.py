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
ObjectState: Enumeration = Enumeration(
    name="ObjectState",
    literals={
            EnumerationLiteral(name="NEW"),
			EnumerationLiteral(name="PRODUCTION"),
			EnumerationLiteral(name="MODIFICATION"),
			EnumerationLiteral(name="DELETION")
    }
)

# Classes
model_Attachment = Class(name="model::Attachment")
BasicObject = Class(name="BasicObject")
model_ObjectRef = Class(name="model::ObjectRef")
model_BasicObject = Class(name="model::BasicObject", is_abstract=True)
model_TreeNode = Class(name="model::TreeNode")
model_TreeNodeChild = Class(name="model::TreeNodeChild")
model_BasicCode = Class(name="model::BasicCode", is_abstract=True)
model_Code = Class(name="model::Code")
BasicCode = Class(name="BasicCode")
model_Category = Class(name="model::Category")
model_CodeEntry = Class(name="model::CodeEntry")
model_BasicNotificationDefinition = Class(name="model::BasicNotificationDefinition", is_abstract=True)
model_NotificationParticipant = Class(name="model::NotificationParticipant")
model_NotificationDefinition = Class(name="model::NotificationDefinition")
BasicNotificationDefinition = Class(name="BasicNotificationDefinition")

# model_Attachment class attributes and methods
model_Attachment_key: Property = Property(name="key", type=StringType)
model_Attachment_objectId: Property = Property(name="objectId", type=StringType)
model_Attachment_data: Property = Property(name="data", type=StringType)
model_Attachment.attributes={model_Attachment_key, model_Attachment_objectId, model_Attachment_data}

# BasicObject class attributes and methods

# model_ObjectRef class attributes and methods
model_ObjectRef_nature: Property = Property(name="nature", type=StringType)
model_ObjectRef_id: Property = Property(name="id", type=StringType)
model_ObjectRef_domain: Property = Property(name="domain", type=IntegerType)
model_ObjectRef_state: Property = Property(name="state", type=StringType)
model_ObjectRef_labels: Property = Property(name="labels", type=StringType)
model_ObjectRef_appId: Property = Property(name="appId", type=StringType)
model_ObjectRef_type: Property = Property(name="type", type=StringType)
model_ObjectRef_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
model_ObjectRef_m_getWorkingId: Method = Method(name="getWorkingId", parameters={}, type=StringType)
model_ObjectRef_m_getDefaultLocale: Method = Method(name="getDefaultLocale", parameters={}, type=StringType)
model_ObjectRef_m_getDefaultLabel: Method = Method(name="getDefaultLabel", parameters={}, type=StringType)
model_ObjectRef.attributes={model_ObjectRef_domain, model_ObjectRef_appId, model_ObjectRef_state, model_ObjectRef_labels, model_ObjectRef_nature, model_ObjectRef_id, model_ObjectRef_type}
model_ObjectRef.methods={model_ObjectRef_m_toString, model_ObjectRef_m_getWorkingId, model_ObjectRef_m_getDefaultLocale, model_ObjectRef_m_getDefaultLabel}

# model_BasicObject class attributes and methods
model_BasicObject_domain: Property = Property(name="domain", type=IntegerType)
model_BasicObject_locale: Property = Property(name="locale", type=StringType)
model_BasicObject_id: Property = Property(name="id", type=StringType)
model_BasicObject_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
model_BasicObject.attributes={model_BasicObject_locale, model_BasicObject_domain, model_BasicObject_id}
model_BasicObject.methods={model_BasicObject_m_toString}

# model_TreeNode class attributes and methods
model_TreeNode_name: Property = Property(name="name", type=StringType)
model_TreeNode.attributes={model_TreeNode_name}

# model_TreeNodeChild class attributes and methods
model_TreeNodeChild_nodeId: Property = Property(name="nodeId", type=StringType)
model_TreeNodeChild.attributes={model_TreeNodeChild_nodeId}

# model_BasicCode class attributes and methods
model_BasicCode_id: Property = Property(name="id", type=StringType)
model_BasicCode_sortHint: Property = Property(name="sortHint", type=IntegerType)
model_BasicCode_domain: Property = Property(name="domain", type=IntegerType)
model_BasicCode_active: Property = Property(name="active", type=BooleanType)
model_BasicCode_structure: Property = Property(name="structure", type=BooleanType)
model_BasicCode_names: Property = Property(name="names", type=StringType)
model_BasicCode_descriptions: Property = Property(name="descriptions", type=StringType)
model_BasicCode_m_getSegments: Method = Method(name="getSegments", parameters={}, type=StringType)
model_BasicCode_m_getLastSegment: Method = Method(name="getLastSegment", parameters={}, type=StringType)
model_BasicCode_m_getPureLastSegment: Method = Method(name="getPureLastSegment", parameters={}, type=StringType)
model_BasicCode_m_getFirstSegment: Method = Method(name="getFirstSegment", parameters={}, type=StringType)
model_BasicCode_m_setParentPath: Method = Method(name="setParentPath", parameters={Parameter(name='parent')})
model_BasicCode.attributes={model_BasicCode_names, model_BasicCode_structure, model_BasicCode_sortHint, model_BasicCode_id, model_BasicCode_domain, model_BasicCode_active, model_BasicCode_descriptions}
model_BasicCode.methods={model_BasicCode_m_getSegments, model_BasicCode_m_getLastSegment, model_BasicCode_m_getFirstSegment, model_BasicCode_m_setParentPath, model_BasicCode_m_getPureLastSegment}

# model_Code class attributes and methods

# BasicCode class attributes and methods

# model_Category class attributes and methods
model_Category_classifier: Property = Property(name="classifier", type=StringType)
model_Category_associatedClassifier: Property = Property(name="associatedClassifier", type=StringType)
model_Category.attributes={model_Category_classifier, model_Category_associatedClassifier}

# model_CodeEntry class attributes and methods
model_CodeEntry_id: Property = Property(name="id", type=StringType)
model_CodeEntry_key: Property = Property(name="key", type=StringType)
model_CodeEntry_value: Property = Property(name="value", type=StringType)
model_CodeEntry.attributes={model_CodeEntry_value, model_CodeEntry_id, model_CodeEntry_key}

# model_BasicNotificationDefinition class attributes and methods
model_BasicNotificationDefinition_notificationEventId: Property = Property(name="notificationEventId", type=StringType)
model_BasicNotificationDefinition_identifier: Property = Property(name="identifier", type=StringType)
model_BasicNotificationDefinition_active: Property = Property(name="active", type=BooleanType)
model_BasicNotificationDefinition_description: Property = Property(name="description", type=StringType)
model_BasicNotificationDefinition_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
model_BasicNotificationDefinition.attributes={model_BasicNotificationDefinition_notificationEventId, model_BasicNotificationDefinition_active, model_BasicNotificationDefinition_identifier, model_BasicNotificationDefinition_description}
model_BasicNotificationDefinition.methods={model_BasicNotificationDefinition_m_toString}

# model_NotificationParticipant class attributes and methods
model_NotificationParticipant_mailAddress: Property = Property(name="mailAddress", type=StringType)
model_NotificationParticipant_id: Property = Property(name="id", type=StringType)
model_NotificationParticipant_groupId: Property = Property(name="groupId", type=StringType)
model_NotificationParticipant.attributes={model_NotificationParticipant_groupId, model_NotificationParticipant_mailAddress, model_NotificationParticipant_id}

# model_NotificationDefinition class attributes and methods
model_NotificationDefinition_includeFilter: Property = Property(name="includeFilter", type=StringType)
model_NotificationDefinition_excludeFilter: Property = Property(name="excludeFilter", type=StringType)
model_NotificationDefinition_template: Property = Property(name="template", type=BooleanType)
model_NotificationDefinition_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
model_NotificationDefinition.attributes={model_NotificationDefinition_excludeFilter, model_NotificationDefinition_template, model_NotificationDefinition_includeFilter}
model_NotificationDefinition.methods={model_NotificationDefinition_m_toString}

# BasicNotificationDefinition class attributes and methods

# Relationships
childs0: BinaryAssociation = BinaryAssociation(
    name="childs0",
    ends={
        Property(name="TreeNodeChild", type=model_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=model_TreeNodeChild, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object1: BinaryAssociation = BinaryAssociation(
    name="object1",
    ends={
        Property(name="model_ObjectRef", type=model_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TreeNode", type=model_ObjectRef, multiplicity=Multiplicity(0, 1))
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="TreeNode", type=model_TreeNodeChild, multiplicity=Multiplicity(1, 1)),
        Property(name="childs", type=model_TreeNode, multiplicity=Multiplicity(0, 1))
    }
)
parent4: BinaryAssociation = BinaryAssociation(
    name="parent4",
    ends={
        Property(name="model_BasicCode", type=model_BasicCode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BasicCode3", type=model_BasicCode, multiplicity=Multiplicity(0, 1))
    }
)
entries5: BinaryAssociation = BinaryAssociation(
    name="entries5",
    ends={
        Property(name="model_CodeEntry", type=model_BasicCode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BasicCode6", type=model_CodeEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectRef7: BinaryAssociation = BinaryAssociation(
    name="objectRef7",
    ends={
        Property(name="model_ObjectRef8", type=model_NotificationParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="model_NotificationParticipant", type=model_ObjectRef, multiplicity=Multiplicity(0, 1))
    }
)
bccReceivers17: BinaryAssociation = BinaryAssociation(
    name="bccReceivers17",
    ends={
        Property(name="model_BasicNotificationDefinition18", type=model_NotificationParticipant, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="model_NotificationParticipant19", type=model_BasicNotificationDefinition, multiplicity=Multiplicity(1, 1))
    }
)
delivery20: BinaryAssociation = BinaryAssociation(
    name="delivery20",
    ends={
        Property(name="model_Code", type=model_BasicNotificationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BasicNotificationDefinition21", type=model_Code, multiplicity=Multiplicity(0, 1))
    }
)
sender9: BinaryAssociation = BinaryAssociation(
    name="sender9",
    ends={
        Property(name="model_NotificationParticipant10", type=model_BasicNotificationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BasicNotificationDefinition", type=model_NotificationParticipant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receivers11: BinaryAssociation = BinaryAssociation(
    name="receivers11",
    ends={
        Property(name="model_NotificationParticipant13", type=model_BasicNotificationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BasicNotificationDefinition12", type=model_NotificationParticipant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ccReceivers14: BinaryAssociation = BinaryAssociation(
    name="ccReceivers14",
    ends={
        Property(name="model_NotificationParticipant16", type=model_BasicNotificationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BasicNotificationDefinition15", type=model_NotificationParticipant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_Attachment_BasicObject = Generalization(general=BasicObject, specific=model_Attachment)
gen_model_TreeNode_BasicObject = Generalization(general=BasicObject, specific=model_TreeNode)
gen_model_Code_BasicCode = Generalization(general=BasicCode, specific=model_Code)
gen_model_Category_BasicCode = Generalization(general=BasicCode, specific=model_Category)
gen_model_BasicNotificationDefinition_BasicObject = Generalization(general=BasicObject, specific=model_BasicNotificationDefinition)
gen_model_NotificationDefinition_BasicNotificationDefinition = Generalization(general=BasicNotificationDefinition, specific=model_NotificationDefinition)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Attachment, BasicObject, model_ObjectRef, model_BasicObject, model_TreeNode, model_TreeNodeChild, model_BasicCode, model_Code, BasicCode, model_Category, model_CodeEntry, model_BasicNotificationDefinition, model_NotificationParticipant, model_NotificationDefinition, BasicNotificationDefinition, ObjectState},
    associations={childs0, object1, parent2, parent4, entries5, objectRef7, bccReceivers17, delivery20, sender9, receivers11, ccReceivers14},
    generalizations={gen_model_Attachment_BasicObject, gen_model_TreeNode_BasicObject, gen_model_Code_BasicCode, gen_model_Category_BasicCode, gen_model_BasicNotificationDefinition_BasicObject, gen_model_NotificationDefinition_BasicNotificationDefinition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)