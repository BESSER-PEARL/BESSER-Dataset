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
R4EAnomalyState: Enumeration = Enumeration(
    name="R4EAnomalyState",
    literals={
            EnumerationLiteral(name="R4E_ANOMALY_STATE_CREATED"),
			EnumerationLiteral(name="R4E_ANOMALY_STATE_ASSIGNED"),
			EnumerationLiteral(name="R4E_ANOMALY_STATE_ACCEPTED"),
			EnumerationLiteral(name="R4E_ANOMALY_STATE_FIXED"),
			EnumerationLiteral(name="R4E_ANOMALY_STATE_DUPLICATED"),
			EnumerationLiteral(name="R4E_ANOMALY_STATE_REJECTED"),
			EnumerationLiteral(name="R4E_ANOMALY_STATE_DEFERRED"),
			EnumerationLiteral(name="R4E_ANOMALY_STATE_VERIFIED")
    }
)

R4EReviewPhase: Enumeration = Enumeration(
    name="R4EReviewPhase",
    literals={
            EnumerationLiteral(name="R4E_REVIEW_PHASE_REWORK"),
			EnumerationLiteral(name="R4E_REVIEW_PHASE_COMPLETED"),
			EnumerationLiteral(name="R4E_REVIEW_PHASE_STARTED"),
			EnumerationLiteral(name="R4E_REVIEW_PHASE_PREPARATION"),
			EnumerationLiteral(name="R4E_REVIEW_PHASE_DECISION")
    }
)

R4EUserRole: Enumeration = Enumeration(
    name="R4EUserRole",
    literals={
            EnumerationLiteral(name="R4E_ROLE_REVIEWER"),
			EnumerationLiteral(name="R4E_ROLE_LEAD"),
			EnumerationLiteral(name="R4E_ROLE_AUTHOR"),
			EnumerationLiteral(name="R4E_ROLE_ORGANIZER")
    }
)

R4EDecision: Enumeration = Enumeration(
    name="R4EDecision",
    literals={
            EnumerationLiteral(name="R4E_REVIEW_DECISION_NONE"),
			EnumerationLiteral(name="R4E_REVIEW_DECISION_ACCEPTED"),
			EnumerationLiteral(name="R4E_REVIEW_DECISION_ACCEPTED_FOLLOWUP"),
			EnumerationLiteral(name="R4E_REVIEW_DECISION_REJECTED")
    }
)

R4EReviewType: Enumeration = Enumeration(
    name="R4EReviewType",
    literals={
            EnumerationLiteral(name="R4E_REVIEW_TYPE_BASIC"),
			EnumerationLiteral(name="R4E_REVIEW_TYPE_INFORMAL"),
			EnumerationLiteral(name="R4E_REVIEW_TYPE_FORMAL")
    }
)

R4EContextType: Enumeration = Enumeration(
    name="R4EContextType",
    literals={
            EnumerationLiteral(name="R4E_UNDEFINED"),
			EnumerationLiteral(name="R4E_ADDED"),
			EnumerationLiteral(name="R4E_DELETED"),
			EnumerationLiteral(name="R4E_MODIFIED"),
			EnumerationLiteral(name="R4E_REPLACED")
    }
)

# Classes
model_R4EAnomalyType = Class(name="model::R4EAnomalyType")
model_MapToAnomalyType = Class(name="model::MapToAnomalyType")
model_R4EReviewGroup = Class(name="model::R4EReviewGroup")
ReviewGroup = Class(name="ReviewGroup")
R4EReviewComponent = Class(name="R4EReviewComponent")
model_R4EReviewDecision = Class(name="model::R4EReviewDecision")
model_MapNameToReview = Class(name="model::MapNameToReview")
model_MapUserIDToUserReviews = Class(name="model::MapUserIDToUserReviews")
model_R4EReview = Class(name="model::R4EReview")
Review = Class(name="Review")
model_R4EUser = Class(name="model::R4EUser")
model_R4EAnomaly = Class(name="model::R4EAnomaly")
model_MapToUsers = Class(name="model::MapToUsers")
R4EComment = Class(name="R4EComment")
model_MapIDToComponent = Class(name="model::MapIDToComponent")
model_R4EMeetingData = Class(name="model::R4EMeetingData")
Topic = Class(name="Topic")
model_R4EDesignRule = Class(name="model::R4EDesignRule")
model_R4EFileVersion = Class(name="model::R4EFileVersion")
model_R4EFormalReview = Class(name="model::R4EFormalReview")
R4EReview = Class(name="R4EReview")
model_R4EParticipant = Class(name="model::R4EParticipant")
model_R4ETextPosition = Class(name="model::R4ETextPosition")
R4EPosition = Class(name="R4EPosition")
model_R4EReviewPhaseInfo = Class(name="model::R4EReviewPhaseInfo")
model_R4EComment = Class(name="model::R4EComment")
model_R4EItem = Class(name="model::R4EItem")
User = Class(name="User")
model_R4EID = Class(name="model::R4EID")
model_MapDateToDuration = Class(name="model::MapDateToDuration")
R4EIDComponent = Class(name="R4EIDComponent")
Item = Class(name="Item")
R4EUser = Class(name="R4EUser")
CommentType = Class(name="CommentType")
model_R4EFileContext = Class(name="model::R4EFileContext")
model_MapKeyToInfoAttributes = Class(name="model::MapKeyToInfoAttributes")
model_R4ETextContent = Class(name="model::R4ETextContent")
R4EContent = Class(name="R4EContent")
model_R4EDelta = Class(name="model::R4EDelta")
model_R4ETaskReference = Class(name="model::R4ETaskReference")
TaskReference = Class(name="TaskReference")
model_R4EReviewState = Class(name="model::R4EReviewState")
ReviewState = Class(name="ReviewState")
Comment = Class(name="Comment")
model_R4EReviewComponent = Class(name="model::R4EReviewComponent")
ReviewComponent = Class(name="ReviewComponent")
Location = Class(name="Location")
model_R4EPosition = Class(name="model::R4EPosition")
model_R4EContent = Class(name="model::R4EContent", is_abstract=True)
model_R4ECommentType = Class(name="model::R4ECommentType")
model_R4EAnomalyTextPosition = Class(name="model::R4EAnomalyTextPosition")
R4ETextPosition = Class(name="R4ETextPosition")
model_R4EUserReviews = Class(name="model::R4EUserReviews")
model_R4EIDComponent = Class(name="model::R4EIDComponent")

# model_R4EAnomalyType class attributes and methods
model_R4EAnomalyType_type: Property = Property(name="type", type=StringType)
model_R4EAnomalyType.attributes={model_R4EAnomalyType_type}

# model_MapToAnomalyType class attributes and methods
model_MapToAnomalyType_key: Property = Property(name="key", type=StringType)
model_MapToAnomalyType.attributes={model_MapToAnomalyType_key}

# model_R4EReviewGroup class attributes and methods
model_R4EReviewGroup_availableProjects: Property = Property(name="availableProjects", type=StringType)
model_R4EReviewGroup_availableComponents: Property = Property(name="availableComponents", type=StringType)
model_R4EReviewGroup_designRuleLocations: Property = Property(name="designRuleLocations", type=StringType)
model_R4EReviewGroup_name: Property = Property(name="name", type=StringType)
model_R4EReviewGroup_folder: Property = Property(name="folder", type=StringType)
model_R4EReviewGroup_defaultEntryCriteria: Property = Property(name="defaultEntryCriteria", type=StringType)
model_R4EReviewGroup.attributes={model_R4EReviewGroup_designRuleLocations, model_R4EReviewGroup_folder, model_R4EReviewGroup_name, model_R4EReviewGroup_defaultEntryCriteria, model_R4EReviewGroup_availableProjects, model_R4EReviewGroup_availableComponents}

# ReviewGroup class attributes and methods

# R4EReviewComponent class attributes and methods

# model_R4EReviewDecision class attributes and methods
model_R4EReviewDecision_spentTime: Property = Property(name="spentTime", type=IntegerType)
model_R4EReviewDecision_value: Property = Property(name="value", type=StringType)
model_R4EReviewDecision.attributes={model_R4EReviewDecision_spentTime, model_R4EReviewDecision_value}

# model_MapNameToReview class attributes and methods
model_MapNameToReview_key: Property = Property(name="key", type=StringType)
model_MapNameToReview.attributes={model_MapNameToReview_key}

# model_MapUserIDToUserReviews class attributes and methods
model_MapUserIDToUserReviews_key: Property = Property(name="key", type=StringType)
model_MapUserIDToUserReviews.attributes={model_MapUserIDToUserReviews_key}

# model_R4EReview class attributes and methods
model_R4EReview_referenceMaterial: Property = Property(name="referenceMaterial", type=StringType)
model_R4EReview_startDate: Property = Property(name="startDate", type=DateType)
model_R4EReview_name: Property = Property(name="name", type=StringType)
model_R4EReview_project: Property = Property(name="project", type=StringType)
model_R4EReview_components: Property = Property(name="components", type=StringType)
model_R4EReview_entryCriteria: Property = Property(name="entryCriteria", type=StringType)
model_R4EReview_extraNotes: Property = Property(name="extraNotes", type=StringType)
model_R4EReview_objectives: Property = Property(name="objectives", type=StringType)
model_R4EReview_endDate: Property = Property(name="endDate", type=DateType)
model_R4EReview_dueDate: Property = Property(name="dueDate", type=DateType)
model_R4EReview_type: Property = Property(name="type", type=StringType)
model_R4EReview_modifiedDate: Property = Property(name="modifiedDate", type=DateType)
model_R4EReview.attributes={model_R4EReview_modifiedDate, model_R4EReview_entryCriteria, model_R4EReview_project, model_R4EReview_name, model_R4EReview_type, model_R4EReview_endDate, model_R4EReview_objectives, model_R4EReview_components, model_R4EReview_referenceMaterial, model_R4EReview_extraNotes, model_R4EReview_startDate, model_R4EReview_dueDate}

# Review class attributes and methods

# model_R4EUser class attributes and methods
model_R4EUser_groupPaths: Property = Property(name="groupPaths", type=StringType)
model_R4EUser_sequenceIDCounter: Property = Property(name="sequenceIDCounter", type=IntegerType)
model_R4EUser_reviewCreatedByMe: Property = Property(name="reviewCreatedByMe", type=BooleanType)
model_R4EUser_reviewCompleted: Property = Property(name="reviewCompleted", type=BooleanType)
model_R4EUser_reviewCompletedCode: Property = Property(name="reviewCompletedCode", type=IntegerType)
model_R4EUser.attributes={model_R4EUser_reviewCompleted, model_R4EUser_reviewCreatedByMe, model_R4EUser_groupPaths, model_R4EUser_reviewCompletedCode, model_R4EUser_sequenceIDCounter}

# model_R4EAnomaly class attributes and methods
model_R4EAnomaly_state: Property = Property(name="state", type=StringType)
model_R4EAnomaly_dueDate: Property = Property(name="dueDate", type=DateType)
model_R4EAnomaly_ruleID: Property = Property(name="ruleID", type=StringType)
model_R4EAnomaly_decidedByID: Property = Property(name="decidedByID", type=StringType)
model_R4EAnomaly_fixedByID: Property = Property(name="fixedByID", type=StringType)
model_R4EAnomaly_followUpByID: Property = Property(name="followUpByID", type=StringType)
model_R4EAnomaly_rank: Property = Property(name="rank", type=StringType)
model_R4EAnomaly_notAcceptedReason: Property = Property(name="notAcceptedReason", type=StringType)
model_R4EAnomaly_isImported: Property = Property(name="isImported", type=BooleanType)
model_R4EAnomaly.attributes={model_R4EAnomaly_fixedByID, model_R4EAnomaly_decidedByID, model_R4EAnomaly_dueDate, model_R4EAnomaly_state, model_R4EAnomaly_followUpByID, model_R4EAnomaly_isImported, model_R4EAnomaly_rank, model_R4EAnomaly_notAcceptedReason, model_R4EAnomaly_ruleID}

# model_MapToUsers class attributes and methods
model_MapToUsers_key: Property = Property(name="key", type=StringType)
model_MapToUsers.attributes={model_MapToUsers_key}

# R4EComment class attributes and methods

# model_MapIDToComponent class attributes and methods

# model_R4EMeetingData class attributes and methods
model_R4EMeetingData_id: Property = Property(name="id", type=StringType)
model_R4EMeetingData_subject: Property = Property(name="subject", type=StringType)
model_R4EMeetingData_location: Property = Property(name="location", type=StringType)
model_R4EMeetingData_startTime: Property = Property(name="startTime", type=StringType)
model_R4EMeetingData_duration: Property = Property(name="duration", type=IntegerType)
model_R4EMeetingData_sentCount: Property = Property(name="sentCount", type=IntegerType)
model_R4EMeetingData_sender: Property = Property(name="sender", type=StringType)
model_R4EMeetingData_receivers: Property = Property(name="receivers", type=StringType)
model_R4EMeetingData_body: Property = Property(name="body", type=StringType)
model_R4EMeetingData.attributes={model_R4EMeetingData_duration, model_R4EMeetingData_receivers, model_R4EMeetingData_body, model_R4EMeetingData_startTime, model_R4EMeetingData_sender, model_R4EMeetingData_sentCount, model_R4EMeetingData_location, model_R4EMeetingData_id, model_R4EMeetingData_subject}

# Topic class attributes and methods

# model_R4EDesignRule class attributes and methods

# model_R4EFileVersion class attributes and methods
model_R4EFileVersion_platformURI: Property = Property(name="platformURI", type=StringType)
model_R4EFileVersion_versionID: Property = Property(name="versionID", type=StringType)
model_R4EFileVersion_repositoryPath: Property = Property(name="repositoryPath", type=StringType)
model_R4EFileVersion_name: Property = Property(name="name", type=StringType)
model_R4EFileVersion_resource: Property = Property(name="resource", type=StringType)
model_R4EFileVersion_localVersionID: Property = Property(name="localVersionID", type=StringType)
model_R4EFileVersion_fileRevision: Property = Property(name="fileRevision", type=StringType)
model_R4EFileVersion.attributes={model_R4EFileVersion_repositoryPath, model_R4EFileVersion_platformURI, model_R4EFileVersion_localVersionID, model_R4EFileVersion_resource, model_R4EFileVersion_fileRevision, model_R4EFileVersion_name, model_R4EFileVersion_versionID}

# model_R4EFormalReview class attributes and methods

# R4EReview class attributes and methods

# model_R4EParticipant class attributes and methods
model_R4EParticipant_isPartOfDecision: Property = Property(name="isPartOfDecision", type=BooleanType)
model_R4EParticipant_roles: Property = Property(name="roles", type=StringType)
model_R4EParticipant_focusArea: Property = Property(name="focusArea", type=StringType)
model_R4EParticipant.attributes={model_R4EParticipant_isPartOfDecision, model_R4EParticipant_focusArea, model_R4EParticipant_roles}

# model_R4ETextPosition class attributes and methods
model_R4ETextPosition_startPosition: Property = Property(name="startPosition", type=IntegerType)
model_R4ETextPosition_length: Property = Property(name="length", type=IntegerType)
model_R4ETextPosition_startLine: Property = Property(name="startLine", type=IntegerType)
model_R4ETextPosition_endLine: Property = Property(name="endLine", type=IntegerType)
model_R4ETextPosition.attributes={model_R4ETextPosition_startPosition, model_R4ETextPosition_endLine, model_R4ETextPosition_length, model_R4ETextPosition_startLine}

# R4EPosition class attributes and methods

# model_R4EReviewPhaseInfo class attributes and methods
model_R4EReviewPhaseInfo_startDate: Property = Property(name="startDate", type=DateType)
model_R4EReviewPhaseInfo_endDate: Property = Property(name="endDate", type=DateType)
model_R4EReviewPhaseInfo_type: Property = Property(name="type", type=StringType)
model_R4EReviewPhaseInfo_phaseOwnerID: Property = Property(name="phaseOwnerID", type=StringType)
model_R4EReviewPhaseInfo.attributes={model_R4EReviewPhaseInfo_phaseOwnerID, model_R4EReviewPhaseInfo_type, model_R4EReviewPhaseInfo_startDate, model_R4EReviewPhaseInfo_endDate}

# model_R4EComment class attributes and methods
model_R4EComment_createdOn: Property = Property(name="createdOn", type=DateType)
model_R4EComment.attributes={model_R4EComment_createdOn}

# model_R4EItem class attributes and methods
model_R4EItem_description: Property = Property(name="description", type=StringType)
model_R4EItem_addedById: Property = Property(name="addedById", type=StringType)
model_R4EItem_repositoryRef: Property = Property(name="repositoryRef", type=StringType)
model_R4EItem_ProjectURIs: Property = Property(name="ProjectURIs", type=StringType)
model_R4EItem_authorRep: Property = Property(name="authorRep", type=StringType)
model_R4EItem_submitted: Property = Property(name="submitted", type=DateType)
model_R4EItem.attributes={model_R4EItem_submitted, model_R4EItem_description, model_R4EItem_repositoryRef, model_R4EItem_authorRep, model_R4EItem_ProjectURIs, model_R4EItem_addedById}

# User class attributes and methods

# model_R4EID class attributes and methods
model_R4EID_sequenceID: Property = Property(name="sequenceID", type=IntegerType)
model_R4EID_userID: Property = Property(name="userID", type=StringType)
model_R4EID.attributes={model_R4EID_userID, model_R4EID_sequenceID}

# model_MapDateToDuration class attributes and methods
model_MapDateToDuration_key: Property = Property(name="key", type=DateType)
model_MapDateToDuration_value: Property = Property(name="value", type=StringType)
model_MapDateToDuration.attributes={model_MapDateToDuration_key, model_MapDateToDuration_value}

# R4EIDComponent class attributes and methods

# Item class attributes and methods

# R4EUser class attributes and methods

# CommentType class attributes and methods

# model_R4EFileContext class attributes and methods
model_R4EFileContext_type: Property = Property(name="type", type=StringType)
model_R4EFileContext.attributes={model_R4EFileContext_type}

# model_MapKeyToInfoAttributes class attributes and methods
model_MapKeyToInfoAttributes_key: Property = Property(name="key", type=StringType)
model_MapKeyToInfoAttributes_value: Property = Property(name="value", type=StringType)
model_MapKeyToInfoAttributes.attributes={model_MapKeyToInfoAttributes_key, model_MapKeyToInfoAttributes_value}

# model_R4ETextContent class attributes and methods
model_R4ETextContent_content: Property = Property(name="content", type=StringType)
model_R4ETextContent.attributes={model_R4ETextContent_content}

# R4EContent class attributes and methods

# model_R4EDelta class attributes and methods

# model_R4ETaskReference class attributes and methods

# TaskReference class attributes and methods

# model_R4EReviewState class attributes and methods
model_R4EReviewState_state: Property = Property(name="state", type=StringType)
model_R4EReviewState.attributes={model_R4EReviewState_state}

# ReviewState class attributes and methods

# Comment class attributes and methods

# model_R4EReviewComponent class attributes and methods
model_R4EReviewComponent_assignedTo: Property = Property(name="assignedTo", type=StringType)
model_R4EReviewComponent.attributes={model_R4EReviewComponent_assignedTo}

# ReviewComponent class attributes and methods

# Location class attributes and methods

# model_R4EPosition class attributes and methods

# model_R4EContent class attributes and methods
model_R4EContent_info: Property = Property(name="info", type=StringType)
model_R4EContent.attributes={model_R4EContent_info}

# model_R4ECommentType class attributes and methods
model_R4ECommentType_type: Property = Property(name="type", type=StringType)
model_R4ECommentType.attributes={model_R4ECommentType_type}

# model_R4EAnomalyTextPosition class attributes and methods

# R4ETextPosition class attributes and methods

# model_R4EUserReviews class attributes and methods
model_R4EUserReviews_name: Property = Property(name="name", type=StringType)
model_R4EUserReviews_createdReviews: Property = Property(name="createdReviews", type=StringType)
model_R4EUserReviews.attributes={model_R4EUserReviews_createdReviews, model_R4EUserReviews_name}

# model_R4EIDComponent class attributes and methods

# Relationships
availableAnomalyTypes0: BinaryAssociation = BinaryAssociation(
    name="availableAnomalyTypes0",
    ends={
        Property(name="model_R4EAnomalyType", type=model_R4EReviewGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EReviewGroup", type=model_R4EAnomalyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision7: BinaryAssociation = BinaryAssociation(
    name="decision7",
    ends={
        Property(name="model_R4EReviewDecision", type=model_R4EReview, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EReview", type=model_R4EReviewDecision, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anomalyTypeKeyToReference1: BinaryAssociation = BinaryAssociation(
    name="anomalyTypeKeyToReference1",
    ends={
        Property(name="model_MapToAnomalyType", type=model_R4EReviewGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EReviewGroup2", type=model_MapToAnomalyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviewsMap3: BinaryAssociation = BinaryAssociation(
    name="reviewsMap3",
    ends={
        Property(name="model_MapNameToReview", type=model_R4EReviewGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EReviewGroup4", type=model_MapNameToReview, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userReviews5: BinaryAssociation = BinaryAssociation(
    name="userReviews5",
    ends={
        Property(name="model_MapUserIDToUserReviews", type=model_R4EReviewGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EReviewGroup6", type=model_MapUserIDToUserReviews, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createdBy12: BinaryAssociation = BinaryAssociation(
    name="createdBy12",
    ends={
        Property(name="model_R4EUser", type=model_R4EReview, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EReview13", type=model_R4EUser, multiplicity=Multiplicity(1, 1))
    }
)
anomalyTemplate8: BinaryAssociation = BinaryAssociation(
    name="anomalyTemplate8",
    ends={
        Property(name="model_R4EAnomaly", type=model_R4EReview, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EReview9", type=model_R4EAnomaly, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usersMap10: BinaryAssociation = BinaryAssociation(
    name="usersMap10",
    ends={
        Property(name="model_MapToUsers", type=model_R4EReview, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EReview11", type=model_MapToUsers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idsMap14: BinaryAssociation = BinaryAssociation(
    name="idsMap14",
    ends={
        Property(name="model_MapIDToComponent", type=model_R4EReview, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EReview15", type=model_MapIDToComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activeMeeting16: BinaryAssociation = BinaryAssociation(
    name="activeMeeting16",
    ends={
        Property(name="model_R4EMeetingData", type=model_R4EReview, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EReview17", type=model_R4EMeetingData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule18: BinaryAssociation = BinaryAssociation(
    name="rule18",
    ends={
        Property(name="model_R4EDesignRule", type=model_R4EAnomaly, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EAnomaly19", type=model_R4EDesignRule, multiplicity=Multiplicity(0, 1))
    }
)
fixedInVersion20: BinaryAssociation = BinaryAssociation(
    name="fixedInVersion20",
    ends={
        Property(name="model_R4EFileVersion", type=model_R4EAnomaly, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EAnomaly21", type=model_R4EFileVersion, multiplicity=Multiplicity(0, 1))
    }
)
phaseOwner22: BinaryAssociation = BinaryAssociation(
    name="phaseOwner22",
    ends={
        Property(name="model_R4EParticipant", type=model_R4EFormalReview, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EFormalReview", type=model_R4EParticipant, multiplicity=Multiplicity(1, 1))
    }
)
phases23: BinaryAssociation = BinaryAssociation(
    name="phases23",
    ends={
        Property(name="model_R4EReviewPhaseInfo", type=model_R4EFormalReview, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EFormalReview24", type=model_R4EReviewPhaseInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
current25: BinaryAssociation = BinaryAssociation(
    name="current25",
    ends={
        Property(name="model_R4EReviewPhaseInfo27", type=model_R4EFormalReview, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EFormalReview26", type=model_R4EReviewPhaseInfo, multiplicity=Multiplicity(0, 1))
    }
)
addedComments28: BinaryAssociation = BinaryAssociation(
    name="addedComments28",
    ends={
        Property(name="model_R4EComment", type=model_R4EUser, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EUser29", type=model_R4EComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviewedContent35: BinaryAssociation = BinaryAssociation(
    name="reviewedContent35",
    ends={
        Property(name="model_R4EID", type=model_R4EParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EParticipant36", type=model_R4EID, multiplicity=Multiplicity(0, 9999))
    }
)
timeLog37: BinaryAssociation = BinaryAssociation(
    name="timeLog37",
    ends={
        Property(name="model_MapDateToDuration", type=model_R4EParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EParticipant38", type=model_MapDateToDuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addedItems30: BinaryAssociation = BinaryAssociation(
    name="addedItems30",
    ends={
        Property(name="model_R4EItem", type=model_R4EUser, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EUser31", type=model_R4EItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviewInstance32: BinaryAssociation = BinaryAssociation(
    name="reviewInstance32",
    ends={
        Property(name="model_R4EReview34", type=model_R4EUser, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EUser33", type=model_R4EReview, multiplicity=Multiplicity(1, 1))
    }
)
fileContextList39: BinaryAssociation = BinaryAssociation(
    name="fileContextList39",
    ends={
        Property(name="model_R4EFileContext", type=model_R4EItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EItem40", type=model_R4EFileContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infoAtt41: BinaryAssociation = BinaryAssociation(
    name="infoAtt41",
    ends={
        Property(name="model_MapKeyToInfoAttributes", type=model_R4EItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EItem42", type=model_MapKeyToInfoAttributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deltas49: BinaryAssociation = BinaryAssociation(
    name="deltas49",
    ends={
        Property(name="model_R4EDelta", type=model_R4EFileContext, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EFileContext50", type=model_R4EDelta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base51: BinaryAssociation = BinaryAssociation(
    name="base51",
    ends={
        Property(name="model_R4EFileVersion53", type=model_R4EFileContext, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EFileContext52", type=model_R4EFileVersion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anomaly43: BinaryAssociation = BinaryAssociation(
    name="anomaly43",
    ends={
        Property(name="model_R4EAnomaly45", type=model_R4EComment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EComment44", type=model_R4EAnomaly, multiplicity=Multiplicity(1, 1))
    }
)
infoAtt46: BinaryAssociation = BinaryAssociation(
    name="infoAtt46",
    ends={
        Property(name="model_MapKeyToInfoAttributes48", type=model_R4EComment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EComment47", type=model_MapKeyToInfoAttributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value65: BinaryAssociation = BinaryAssociation(
    name="value65",
    ends={
        Property(name="model_R4EAnomalyType67", type=model_MapToAnomalyType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MapToAnomalyType66", type=model_R4EAnomalyType, multiplicity=Multiplicity(0, 1))
    }
)
location68: BinaryAssociation = BinaryAssociation(
    name="location68",
    ends={
        Property(name="model_R4EPosition", type=model_R4EContent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EContent69", type=model_R4EPosition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target54: BinaryAssociation = BinaryAssociation(
    name="target54",
    ends={
        Property(name="model_R4EFileVersion56", type=model_R4EFileContext, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EFileContext55", type=model_R4EFileVersion, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
infoAtt57: BinaryAssociation = BinaryAssociation(
    name="infoAtt57",
    ends={
        Property(name="model_MapKeyToInfoAttributes59", type=model_R4EFileContext, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EFileContext58", type=model_MapKeyToInfoAttributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base60: BinaryAssociation = BinaryAssociation(
    name="base60",
    ends={
        Property(name="model_R4EContent", type=model_R4EDelta, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EDelta61", type=model_R4EContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target62: BinaryAssociation = BinaryAssociation(
    name="target62",
    ends={
        Property(name="model_R4EContent64", type=model_R4EDelta, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EDelta63", type=model_R4EContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value73: BinaryAssociation = BinaryAssociation(
    name="value73",
    ends={
        Property(name="model_R4EReview75", type=model_MapNameToReview, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MapNameToReview74", type=model_R4EReview, multiplicity=Multiplicity(1, 1))
    }
)
value76: BinaryAssociation = BinaryAssociation(
    name="value76",
    ends={
        Property(name="model_R4EUser78", type=model_MapToUsers, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MapToUsers77", type=model_R4EUser, multiplicity=Multiplicity(1, 1))
    }
)
infoAtt70: BinaryAssociation = BinaryAssociation(
    name="infoAtt70",
    ends={
        Property(name="model_MapKeyToInfoAttributes72", type=model_R4EFileVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EFileVersion71", type=model_MapKeyToInfoAttributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value92: BinaryAssociation = BinaryAssociation(
    name="value92",
    ends={
        Property(name="model_R4EUserReviews94", type=model_MapUserIDToUserReviews, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MapUserIDToUserReviews93", type=model_R4EUserReviews, multiplicity=Multiplicity(1, 1))
    }
)
invitedToMap79: BinaryAssociation = BinaryAssociation(
    name="invitedToMap79",
    ends={
        Property(name="model_MapNameToReview80", type=model_R4EUserReviews, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EUserReviews", type=model_MapNameToReview, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group81: BinaryAssociation = BinaryAssociation(
    name="group81",
    ends={
        Property(name="model_R4EReviewGroup83", type=model_R4EUserReviews, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EUserReviews82", type=model_R4EReviewGroup, multiplicity=Multiplicity(0, 1))
    }
)
id84: BinaryAssociation = BinaryAssociation(
    name="id84",
    ends={
        Property(name="model_R4EID85", type=model_R4EIDComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EIDComponent", type=model_R4EID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key86: BinaryAssociation = BinaryAssociation(
    name="key86",
    ends={
        Property(name="model_R4EID88", type=model_MapIDToComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MapIDToComponent87", type=model_R4EID, multiplicity=Multiplicity(1, 1))
    }
)
value89: BinaryAssociation = BinaryAssociation(
    name="value89",
    ends={
        Property(name="model_R4EIDComponent91", type=model_MapIDToComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MapIDToComponent90", type=model_R4EIDComponent, multiplicity=Multiplicity(1, 1))
    }
)
file95: BinaryAssociation = BinaryAssociation(
    name="file95",
    ends={
        Property(name="model_R4EFileVersion96", type=model_R4EAnomalyTextPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_R4EAnomalyTextPosition", type=model_R4EFileVersion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_model_R4EReviewGroup_ReviewGroup = Generalization(general=ReviewGroup, specific=model_R4EReviewGroup)
gen_model_R4EReviewGroup_R4EReviewComponent = Generalization(general=R4EReviewComponent, specific=model_R4EReviewGroup)
gen_model_R4EReview_Review = Generalization(general=Review, specific=model_R4EReview)
gen_model_R4EReview_R4EReviewComponent = Generalization(general=R4EReviewComponent, specific=model_R4EReview)
gen_model_R4EAnomaly_R4EComment = Generalization(general=R4EComment, specific=model_R4EAnomaly)
gen_model_R4EAnomaly_Topic = Generalization(general=Topic, specific=model_R4EAnomaly)
gen_model_R4EAnomaly_R4EReviewComponent = Generalization(general=R4EReviewComponent, specific=model_R4EAnomaly)
gen_model_R4EFormalReview_R4EReview = Generalization(general=R4EReview, specific=model_R4EFormalReview)
gen_model_R4ETextPosition_R4EPosition = Generalization(general=R4EPosition, specific=model_R4ETextPosition)
gen_model_R4EUser_User = Generalization(general=User, specific=model_R4EUser)
gen_model_R4EUser_R4EReviewComponent = Generalization(general=R4EReviewComponent, specific=model_R4EUser)
gen_model_R4EItem_R4EIDComponent = Generalization(general=R4EIDComponent, specific=model_R4EItem)
gen_model_R4EParticipant_R4EUser = Generalization(general=R4EUser, specific=model_R4EParticipant)
gen_model_R4EAnomalyType_CommentType = Generalization(general=CommentType, specific=model_R4EAnomalyType)
gen_model_R4EItem_Item = Generalization(general=Item, specific=model_R4EItem)
gen_model_R4ETextContent_R4EContent = Generalization(general=R4EContent, specific=model_R4ETextContent)
gen_model_R4EFileContext_R4EIDComponent = Generalization(general=R4EIDComponent, specific=model_R4EFileContext)
gen_model_R4ETaskReference_TaskReference = Generalization(general=TaskReference, specific=model_R4ETaskReference)
gen_model_R4ETaskReference_R4EReviewComponent = Generalization(general=R4EReviewComponent, specific=model_R4ETaskReference)
gen_model_R4EReviewState_ReviewState = Generalization(general=ReviewState, specific=model_R4EReviewState)
gen_model_R4EComment_Comment = Generalization(general=Comment, specific=model_R4EComment)
gen_model_R4EComment_R4EReviewComponent = Generalization(general=R4EReviewComponent, specific=model_R4EComment)
gen_model_R4EComment_R4EIDComponent = Generalization(general=R4EIDComponent, specific=model_R4EComment)
gen_model_R4EReviewComponent_ReviewComponent = Generalization(general=ReviewComponent, specific=model_R4EReviewComponent)
gen_model_R4EContent_Location = Generalization(general=Location, specific=model_R4EContent)
gen_model_R4EDelta_R4EIDComponent = Generalization(general=R4EIDComponent, specific=model_R4EDelta)
gen_model_R4ECommentType_CommentType = Generalization(general=CommentType, specific=model_R4ECommentType)
gen_model_R4EAnomalyTextPosition_R4ETextPosition = Generalization(general=R4ETextPosition, specific=model_R4EAnomalyTextPosition)
gen_model_R4EIDComponent_R4EReviewComponent = Generalization(general=R4EReviewComponent, specific=model_R4EIDComponent)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_R4EAnomalyType, model_MapToAnomalyType, model_R4EReviewGroup, ReviewGroup, R4EReviewComponent, model_R4EReviewDecision, model_MapNameToReview, model_MapUserIDToUserReviews, model_R4EReview, Review, model_R4EUser, model_R4EAnomaly, model_MapToUsers, R4EComment, model_MapIDToComponent, model_R4EMeetingData, Topic, model_R4EDesignRule, model_R4EFileVersion, model_R4EFormalReview, R4EReview, model_R4EParticipant, model_R4ETextPosition, R4EPosition, model_R4EReviewPhaseInfo, model_R4EComment, model_R4EItem, User, model_R4EID, model_MapDateToDuration, R4EIDComponent, Item, R4EUser, CommentType, model_R4EFileContext, model_MapKeyToInfoAttributes, model_R4ETextContent, R4EContent, model_R4EDelta, model_R4ETaskReference, TaskReference, model_R4EReviewState, ReviewState, Comment, model_R4EReviewComponent, ReviewComponent, Location, model_R4EPosition, model_R4EContent, model_R4ECommentType, model_R4EAnomalyTextPosition, R4ETextPosition, model_R4EUserReviews, model_R4EIDComponent, R4EAnomalyState, R4EReviewPhase, R4EUserRole, R4EDecision, R4EReviewType, R4EContextType},
    associations={availableAnomalyTypes0, decision7, anomalyTypeKeyToReference1, reviewsMap3, userReviews5, createdBy12, anomalyTemplate8, usersMap10, idsMap14, activeMeeting16, rule18, fixedInVersion20, phaseOwner22, phases23, current25, addedComments28, reviewedContent35, timeLog37, addedItems30, reviewInstance32, fileContextList39, infoAtt41, deltas49, base51, anomaly43, infoAtt46, value65, location68, target54, infoAtt57, base60, target62, value73, value76, infoAtt70, value92, invitedToMap79, group81, id84, key86, value89, file95},
    generalizations={gen_model_R4EReviewGroup_ReviewGroup, gen_model_R4EReviewGroup_R4EReviewComponent, gen_model_R4EReview_Review, gen_model_R4EReview_R4EReviewComponent, gen_model_R4EAnomaly_R4EComment, gen_model_R4EAnomaly_Topic, gen_model_R4EAnomaly_R4EReviewComponent, gen_model_R4EFormalReview_R4EReview, gen_model_R4ETextPosition_R4EPosition, gen_model_R4EUser_User, gen_model_R4EUser_R4EReviewComponent, gen_model_R4EItem_R4EIDComponent, gen_model_R4EParticipant_R4EUser, gen_model_R4EAnomalyType_CommentType, gen_model_R4EItem_Item, gen_model_R4ETextContent_R4EContent, gen_model_R4EFileContext_R4EIDComponent, gen_model_R4ETaskReference_TaskReference, gen_model_R4ETaskReference_R4EReviewComponent, gen_model_R4EReviewState_ReviewState, gen_model_R4EComment_Comment, gen_model_R4EComment_R4EReviewComponent, gen_model_R4EComment_R4EIDComponent, gen_model_R4EReviewComponent_ReviewComponent, gen_model_R4EContent_Location, gen_model_R4EDelta_R4EIDComponent, gen_model_R4ECommentType_CommentType, gen_model_R4EAnomalyTextPosition_R4ETextPosition, gen_model_R4EIDComponent_R4EReviewComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)