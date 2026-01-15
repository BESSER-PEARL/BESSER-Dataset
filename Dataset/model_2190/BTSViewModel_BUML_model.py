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
MessageType: Enumeration = Enumeration(
    name="MessageType",
    literals={
            EnumerationLiteral(name="ERROR"),
			EnumerationLiteral(name="WARNING"),
			EnumerationLiteral(name="LOCKED"),
			EnumerationLiteral(name="NO_EDITING_RIGHTS"),
			EnumerationLiteral(name="FILTERED"),
			EnumerationLiteral(name="UPDATE"),
			EnumerationLiteral(name="INFORMATION")
    }
)

# Classes
btsviewmodel_TreeNodeWrapper = Class(name="btsviewmodel::TreeNodeWrapper")
btsviewmodel_DBCollectionStatusInformation = Class(name="btsviewmodel::DBCollectionStatusInformation")
btsviewmodel_StatusMessage = Class(name="btsviewmodel::StatusMessage")
btsviewmodel_BTSObjectTypeTreeNode = Class(name="btsviewmodel::BTSObjectTypeTreeNode")

# btsviewmodel_TreeNodeWrapper class attributes and methods
btsviewmodel_TreeNodeWrapper_object: Property = Property(name="object", type=StringType)
btsviewmodel_TreeNodeWrapper_propertyChangeSupport: Property = Property(name="propertyChangeSupport", type=StringType)
btsviewmodel_TreeNodeWrapper_childrenLoaded: Property = Property(name="childrenLoaded", type=BooleanType)
btsviewmodel_TreeNodeWrapper_label: Property = Property(name="label", type=StringType)
btsviewmodel_TreeNodeWrapper_parentObject: Property = Property(name="parentObject", type=StringType)
btsviewmodel_TreeNodeWrapper_m_addPropertyChangeListener: Method = Method(name="addPropertyChangeListener", parameters={Parameter(name='propertyChangeListener')})
btsviewmodel_TreeNodeWrapper_m_removePropertyChangeListener: Method = Method(name="removePropertyChangeListener", parameters={Parameter(name='propertyChangeListener')})
btsviewmodel_TreeNodeWrapper.attributes={btsviewmodel_TreeNodeWrapper_label, btsviewmodel_TreeNodeWrapper_object, btsviewmodel_TreeNodeWrapper_propertyChangeSupport, btsviewmodel_TreeNodeWrapper_childrenLoaded, btsviewmodel_TreeNodeWrapper_parentObject}
btsviewmodel_TreeNodeWrapper.methods={btsviewmodel_TreeNodeWrapper_m_removePropertyChangeListener, btsviewmodel_TreeNodeWrapper_m_addPropertyChangeListener}

# btsviewmodel_DBCollectionStatusInformation class attributes and methods
btsviewmodel_DBCollectionStatusInformation_dbCollectionName: Property = Property(name="dbCollectionName", type=StringType)
btsviewmodel_DBCollectionStatusInformation_dbDocCount: Property = Property(name="dbDocCount", type=StringType)
btsviewmodel_DBCollectionStatusInformation_syncStatusToRemote: Property = Property(name="syncStatusToRemote", type=StringType)
btsviewmodel_DBCollectionStatusInformation_syncStatusFromRemote: Property = Property(name="syncStatusFromRemote", type=StringType)
btsviewmodel_DBCollectionStatusInformation_indexDocCount: Property = Property(name="indexDocCount", type=StringType)
btsviewmodel_DBCollectionStatusInformation_indexStatus: Property = Property(name="indexStatus", type=StringType)
btsviewmodel_DBCollectionStatusInformation_dbDiskSize: Property = Property(name="dbDiskSize", type=StringType)
btsviewmodel_DBCollectionStatusInformation_dbDocDelCount: Property = Property(name="dbDocDelCount", type=StringType)
btsviewmodel_DBCollectionStatusInformation_dbPurgeSeq: Property = Property(name="dbPurgeSeq", type=StringType)
btsviewmodel_DBCollectionStatusInformation_dbUpdateSeq: Property = Property(name="dbUpdateSeq", type=StringType)
btsviewmodel_DBCollectionStatusInformation_indexUpdateSeq: Property = Property(name="indexUpdateSeq", type=StringType)
btsviewmodel_DBCollectionStatusInformation.attributes={btsviewmodel_DBCollectionStatusInformation_indexDocCount, btsviewmodel_DBCollectionStatusInformation_indexStatus, btsviewmodel_DBCollectionStatusInformation_dbDocCount, btsviewmodel_DBCollectionStatusInformation_dbUpdateSeq, btsviewmodel_DBCollectionStatusInformation_dbDocDelCount, btsviewmodel_DBCollectionStatusInformation_indexUpdateSeq, btsviewmodel_DBCollectionStatusInformation_dbCollectionName, btsviewmodel_DBCollectionStatusInformation_syncStatusFromRemote, btsviewmodel_DBCollectionStatusInformation_dbPurgeSeq, btsviewmodel_DBCollectionStatusInformation_syncStatusToRemote, btsviewmodel_DBCollectionStatusInformation_dbDiskSize}

# btsviewmodel_StatusMessage class attributes and methods
btsviewmodel_StatusMessage_message: Property = Property(name="message", type=StringType)
btsviewmodel_StatusMessage_creationTime: Property = Property(name="creationTime", type=DateType)
btsviewmodel_StatusMessage_userId: Property = Property(name="userId", type=StringType)
btsviewmodel_StatusMessage_messageType: Property = Property(name="messageType", type=StringType)
btsviewmodel_StatusMessage.attributes={btsviewmodel_StatusMessage_creationTime, btsviewmodel_StatusMessage_userId, btsviewmodel_StatusMessage_message, btsviewmodel_StatusMessage_messageType}

# btsviewmodel_BTSObjectTypeTreeNode class attributes and methods
btsviewmodel_BTSObjectTypeTreeNode_selected: Property = Property(name="selected", type=BooleanType)
btsviewmodel_BTSObjectTypeTreeNode_value: Property = Property(name="value", type=StringType)
btsviewmodel_BTSObjectTypeTreeNode.attributes={btsviewmodel_BTSObjectTypeTreeNode_selected, btsviewmodel_BTSObjectTypeTreeNode_value}

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="btsviewmodel_TreeNodeWrapper", type=btsviewmodel_TreeNodeWrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="btsviewmodel_TreeNodeWrapper0", type=btsviewmodel_TreeNodeWrapper, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="btsviewmodel_TreeNodeWrapper4", type=btsviewmodel_TreeNodeWrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="btsviewmodel_TreeNodeWrapper2", type=btsviewmodel_TreeNodeWrapper, multiplicity=Multiplicity(0, 9999))
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="btsviewmodel_StatusMessage", type=btsviewmodel_StatusMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="btsviewmodel_StatusMessage5", type=btsviewmodel_StatusMessage, multiplicity=Multiplicity(0, 9999))
    }
)
children8: BinaryAssociation = BinaryAssociation(
    name="children8",
    ends={
        Property(name="btsviewmodel_BTSObjectTypeTreeNode", type=btsviewmodel_BTSObjectTypeTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="btsviewmodel_BTSObjectTypeTreeNode7", type=btsviewmodel_BTSObjectTypeTreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedTypesPath10: BinaryAssociation = BinaryAssociation(
    name="referencedTypesPath10",
    ends={
        Property(name="btsviewmodel_BTSObjectTypeTreeNode11", type=btsviewmodel_BTSObjectTypeTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="btsviewmodel_BTSObjectTypeTreeNode9", type=btsviewmodel_BTSObjectTypeTreeNode, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="btsviewmodel",
    types={btsviewmodel_TreeNodeWrapper, btsviewmodel_DBCollectionStatusInformation, btsviewmodel_StatusMessage, btsviewmodel_BTSObjectTypeTreeNode, MessageType},
    associations={parent1, children3, children6, children8, referencedTypesPath10},
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