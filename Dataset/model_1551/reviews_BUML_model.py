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
RequirementStatus: Enumeration = Enumeration(
    name="RequirementStatus",
    literals={
            EnumerationLiteral(name="Unknown"),
			EnumerationLiteral(name="Satisfied"),
			EnumerationLiteral(name="Optional"),
			EnumerationLiteral(name="Closed"),
			EnumerationLiteral(name="NotSatisfied"),
			EnumerationLiteral(name="Rejected"),
			EnumerationLiteral(name="Error")
    }
)

ReviewStatus: Enumeration = Enumeration(
    name="ReviewStatus",
    literals={
            EnumerationLiteral(name="Abandoned"),
			EnumerationLiteral(name="Draft"),
			EnumerationLiteral(name="New"),
			EnumerationLiteral(name="Submitted"),
			EnumerationLiteral(name="Merged")
    }
)

# Classes
reviews_CommentContainer = Class(name="reviews::CommentContainer", is_abstract=True)
reviews_Change = Class(name="reviews::Change")
Dated = Class(name="Dated")
reviews_User = Class(name="reviews::User")
reviews_Review = Class(name="reviews::Review")
CommentContainer = Class(name="CommentContainer")
Change = Class(name="Change")
reviews_ReviewItemSet = Class(name="reviews::ReviewItemSet")
reviews_Repository = Class(name="reviews::Repository")
reviews_Comment = Class(name="reviews::Comment")
reviews_ReviewRequirementsMap = Class(name="reviews::ReviewRequirementsMap")
Indexed = Class(name="Indexed")
reviews_Location = Class(name="reviews::Location", is_abstract=True)
reviews_UserApprovalsMap = Class(name="reviews::UserApprovalsMap")
reviews_ReviewItem = Class(name="reviews::ReviewItem", is_abstract=True)
reviews_FileItem = Class(name="reviews::FileItem")
ReviewItem = Class(name="ReviewItem")
reviews_FileVersion = Class(name="reviews::FileVersion")
reviews_ApprovalType = Class(name="reviews::ApprovalType")
reviews_Commit = Class(name="reviews::Commit")
reviews_LineLocation = Class(name="reviews::LineLocation")
Location = Class(name="Location")
reviews_LineRange = Class(name="reviews::LineRange")
reviews_Indexed = Class(name="reviews::Indexed", is_abstract=True)
reviews_Dated = Class(name="reviews::Dated", is_abstract=True)
reviews_ReviewerEntry = Class(name="reviews::ReviewerEntry")
reviews_RequirementEntry = Class(name="reviews::RequirementEntry")
reviews_ApprovalValueMap = Class(name="reviews::ApprovalValueMap")

# reviews_CommentContainer class attributes and methods
reviews_CommentContainer_m_createComment: Method = Method(name="createComment", parameters={Parameter(name='commentText'), Parameter(name='initalLocation')}, type=StringType)
reviews_CommentContainer.methods={reviews_CommentContainer_m_createComment}

# reviews_Change class attributes and methods
reviews_Change_id: Property = Property(name="id", type=StringType)
reviews_Change_key: Property = Property(name="key", type=StringType)
reviews_Change_subject: Property = Property(name="subject", type=StringType)
reviews_Change_message: Property = Property(name="message", type=StringType)
reviews_Change_state: Property = Property(name="state", type=StringType)
reviews_Change.attributes={reviews_Change_subject, reviews_Change_state, reviews_Change_id, reviews_Change_message, reviews_Change_key}

# Dated class attributes and methods

# reviews_User class attributes and methods
reviews_User_id: Property = Property(name="id", type=StringType)
reviews_User_email: Property = Property(name="email", type=StringType)
reviews_User_displayName: Property = Property(name="displayName", type=StringType)
reviews_User.attributes={reviews_User_id, reviews_User_displayName, reviews_User_email}

# reviews_Review class attributes and methods

# CommentContainer class attributes and methods

# Change class attributes and methods

# reviews_ReviewItemSet class attributes and methods
reviews_ReviewItemSet_inNeedOfRetrieval: Property = Property(name="inNeedOfRetrieval", type=BooleanType)
reviews_ReviewItemSet_revision: Property = Property(name="revision", type=StringType)
reviews_ReviewItemSet.attributes={reviews_ReviewItemSet_revision, reviews_ReviewItemSet_inNeedOfRetrieval}

# reviews_Repository class attributes and methods
reviews_Repository_taskRepository: Property = Property(name="taskRepository", type=StringType)
reviews_Repository_description: Property = Property(name="description", type=StringType)
reviews_Repository_taskRepositoryUrl: Property = Property(name="taskRepositoryUrl", type=StringType)
reviews_Repository_taskConnectorKind: Property = Property(name="taskConnectorKind", type=StringType)
reviews_Repository.attributes={reviews_Repository_description, reviews_Repository_taskRepositoryUrl, reviews_Repository_taskConnectorKind, reviews_Repository_taskRepository}

# reviews_Comment class attributes and methods
reviews_Comment_description: Property = Property(name="description", type=StringType)
reviews_Comment_id: Property = Property(name="id", type=StringType)
reviews_Comment_draft: Property = Property(name="draft", type=BooleanType)
reviews_Comment_mine: Property = Property(name="mine", type=BooleanType)
reviews_Comment_title: Property = Property(name="title", type=StringType)
reviews_Comment.attributes={reviews_Comment_title, reviews_Comment_description, reviews_Comment_mine, reviews_Comment_id, reviews_Comment_draft}

# reviews_ReviewRequirementsMap class attributes and methods

# Indexed class attributes and methods

# reviews_Location class attributes and methods

# reviews_UserApprovalsMap class attributes and methods

# reviews_ReviewItem class attributes and methods
reviews_ReviewItem_name: Property = Property(name="name", type=StringType)
reviews_ReviewItem_id: Property = Property(name="id", type=StringType)
reviews_ReviewItem_reference: Property = Property(name="reference", type=StringType)
reviews_ReviewItem.attributes={reviews_ReviewItem_name, reviews_ReviewItem_id, reviews_ReviewItem_reference}

# reviews_FileItem class attributes and methods

# ReviewItem class attributes and methods

# reviews_FileVersion class attributes and methods
reviews_FileVersion_path: Property = Property(name="path", type=StringType)
reviews_FileVersion_fileRevision: Property = Property(name="fileRevision", type=StringType)
reviews_FileVersion_binaryContent: Property = Property(name="binaryContent", type=StringType)
reviews_FileVersion_description: Property = Property(name="description", type=StringType)
reviews_FileVersion_content: Property = Property(name="content", type=StringType)
reviews_FileVersion.attributes={reviews_FileVersion_content, reviews_FileVersion_path, reviews_FileVersion_binaryContent, reviews_FileVersion_description, reviews_FileVersion_fileRevision}

# reviews_ApprovalType class attributes and methods
reviews_ApprovalType_key: Property = Property(name="key", type=StringType)
reviews_ApprovalType_name: Property = Property(name="name", type=StringType)
reviews_ApprovalType.attributes={reviews_ApprovalType_name, reviews_ApprovalType_key}

# reviews_Commit class attributes and methods
reviews_Commit_id: Property = Property(name="id", type=StringType)
reviews_Commit_subject: Property = Property(name="subject", type=StringType)
reviews_Commit.attributes={reviews_Commit_id, reviews_Commit_subject}

# reviews_LineLocation class attributes and methods
reviews_LineLocation_rangeMin: Property = Property(name="rangeMin", type=IntegerType)
reviews_LineLocation_rangeMax: Property = Property(name="rangeMax", type=IntegerType)
reviews_LineLocation.attributes={reviews_LineLocation_rangeMax, reviews_LineLocation_rangeMin}

# Location class attributes and methods

# reviews_LineRange class attributes and methods
reviews_LineRange_start: Property = Property(name="start", type=IntegerType)
reviews_LineRange_end: Property = Property(name="end", type=IntegerType)
reviews_LineRange.attributes={reviews_LineRange_start, reviews_LineRange_end}

# reviews_Indexed class attributes and methods
reviews_Indexed_index: Property = Property(name="index", type=StringType)
reviews_Indexed.attributes={reviews_Indexed_index}

# reviews_Dated class attributes and methods
reviews_Dated_creationDate: Property = Property(name="creationDate", type=DateType)
reviews_Dated_modificationDate: Property = Property(name="modificationDate", type=DateType)
reviews_Dated.attributes={reviews_Dated_creationDate, reviews_Dated_modificationDate}

# reviews_ReviewerEntry class attributes and methods

# reviews_RequirementEntry class attributes and methods
reviews_RequirementEntry_status: Property = Property(name="status", type=StringType)
reviews_RequirementEntry.attributes={reviews_RequirementEntry_status}

# reviews_ApprovalValueMap class attributes and methods
reviews_ApprovalValueMap_value: Property = Property(name="value", type=StringType)
reviews_ApprovalValueMap.attributes={reviews_ApprovalValueMap_value}

# Relationships
drafts5: BinaryAssociation = BinaryAssociation(
    name="drafts5",
    ends={
        Property(name="reviews_Comment7", type=reviews_CommentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_CommentContainer6", type=reviews_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner8: BinaryAssociation = BinaryAssociation(
    name="owner8",
    ends={
        Property(name="reviews_User", type=reviews_Change, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Change", type=reviews_User, multiplicity=Multiplicity(0, 1))
    }
)
sets9: BinaryAssociation = BinaryAssociation(
    name="sets9",
    ends={
        Property(name="ReviewItemSet", type=reviews_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="parentReview", type=reviews_ReviewItemSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository10: BinaryAssociation = BinaryAssociation(
    name="repository10",
    ends={
        Property(name="Repository", type=reviews_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews", type=reviews_Repository, multiplicity=Multiplicity(1, 1))
    }
)
allComments0: BinaryAssociation = BinaryAssociation(
    name="allComments0",
    ends={
        Property(name="reviews_Comment", type=reviews_CommentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_CommentContainer", type=reviews_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
comments1: BinaryAssociation = BinaryAssociation(
    name="comments1",
    ends={
        Property(name="Comment", type=reviews_CommentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="item", type=reviews_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviewerApprovals16: BinaryAssociation = BinaryAssociation(
    name="reviewerApprovals16",
    ends={
        Property(name="reviews_Review17", type=reviews_UserApprovalsMap, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="reviews_UserApprovalsMap", type=reviews_Review, multiplicity=Multiplicity(1, 1))
    }
)
allDrafts2: BinaryAssociation = BinaryAssociation(
    name="allDrafts2",
    ends={
        Property(name="reviews_Comment4", type=reviews_CommentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_CommentContainer3", type=reviews_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
requirements18: BinaryAssociation = BinaryAssociation(
    name="requirements18",
    ends={
        Property(name="reviews_ReviewRequirementsMap", type=reviews_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Review19", type=reviews_ReviewRequirementsMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author20: BinaryAssociation = BinaryAssociation(
    name="author20",
    ends={
        Property(name="reviews_User22", type=reviews_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Comment21", type=reviews_User, multiplicity=Multiplicity(1, 1))
    }
)
replies24: BinaryAssociation = BinaryAssociation(
    name="replies24",
    ends={
        Property(name="reviews_Comment25", type=reviews_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Comment23", type=reviews_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
locations26: BinaryAssociation = BinaryAssociation(
    name="locations26",
    ends={
        Property(name="reviews_Location", type=reviews_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Comment27", type=reviews_Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parents11: BinaryAssociation = BinaryAssociation(
    name="parents11",
    ends={
        Property(name="reviews_Change12", type=reviews_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Review", type=reviews_Change, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children13: BinaryAssociation = BinaryAssociation(
    name="children13",
    ends={
        Property(name="reviews_Change15", type=reviews_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Review14", type=reviews_Change, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addedBy32: BinaryAssociation = BinaryAssociation(
    name="addedBy32",
    ends={
        Property(name="reviews_User33", type=reviews_ReviewItem, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_ReviewItem", type=reviews_User, multiplicity=Multiplicity(1, 1))
    }
)
committedBy34: BinaryAssociation = BinaryAssociation(
    name="committedBy34",
    ends={
        Property(name="reviews_User36", type=reviews_ReviewItem, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_ReviewItem35", type=reviews_User, multiplicity=Multiplicity(1, 1))
    }
)
review37: BinaryAssociation = BinaryAssociation(
    name="review37",
    ends={
        Property(name="reviews_Review39", type=reviews_ReviewItem, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_ReviewItem38", type=reviews_Review, multiplicity=Multiplicity(1, 1))
    }
)
review28: BinaryAssociation = BinaryAssociation(
    name="review28",
    ends={
        Property(name="reviews_Review30", type=reviews_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Comment29", type=reviews_Review, multiplicity=Multiplicity(1, 1))
    }
)
item31: BinaryAssociation = BinaryAssociation(
    name="item31",
    ends={
        Property(name="CommentContainer", type=reviews_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=reviews_CommentContainer, multiplicity=Multiplicity(0, 1))
    }
)
account41: BinaryAssociation = BinaryAssociation(
    name="account41",
    ends={
        Property(name="reviews_User43", type=reviews_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Repository42", type=reviews_User, multiplicity=Multiplicity(1, 1))
    }
)
reviews44: BinaryAssociation = BinaryAssociation(
    name="reviews44",
    ends={
        Property(name="Review", type=reviews_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository", type=reviews_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users45: BinaryAssociation = BinaryAssociation(
    name="users45",
    ends={
        Property(name="reviews_User47", type=reviews_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Repository46", type=reviews_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base48: BinaryAssociation = BinaryAssociation(
    name="base48",
    ends={
        Property(name="reviews_FileVersion", type=reviews_FileItem, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_FileItem", type=reviews_FileVersion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target49: BinaryAssociation = BinaryAssociation(
    name="target49",
    ends={
        Property(name="reviews_FileVersion51", type=reviews_FileItem, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_FileItem50", type=reviews_FileVersion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set52: BinaryAssociation = BinaryAssociation(
    name="set52",
    ends={
        Property(name="ReviewItemSet53", type=reviews_FileItem, multiplicity=Multiplicity(1, 1)),
        Property(name="items", type=reviews_ReviewItemSet, multiplicity=Multiplicity(0, 1))
    }
)
approvalTypes40: BinaryAssociation = BinaryAssociation(
    name="approvalTypes40",
    ends={
        Property(name="reviews_ApprovalType", type=reviews_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_Repository", type=reviews_ApprovalType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentReview55: BinaryAssociation = BinaryAssociation(
    name="parentReview55",
    ends={
        Property(name="Review56", type=reviews_ReviewItemSet, multiplicity=Multiplicity(1, 1)),
        Property(name="sets", type=reviews_Review, multiplicity=Multiplicity(1, 1))
    }
)
parentCommits57: BinaryAssociation = BinaryAssociation(
    name="parentCommits57",
    ends={
        Property(name="reviews_Commit", type=reviews_ReviewItemSet, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_ReviewItemSet", type=reviews_Commit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ranges58: BinaryAssociation = BinaryAssociation(
    name="ranges58",
    ends={
        Property(name="reviews_LineRange", type=reviews_LineLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_LineLocation", type=reviews_LineRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items54: BinaryAssociation = BinaryAssociation(
    name="items54",
    ends={
        Property(name="FileItem", type=reviews_ReviewItemSet, multiplicity=Multiplicity(1, 1)),
        Property(name="set", type=reviews_FileItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key62: BinaryAssociation = BinaryAssociation(
    name="key62",
    ends={
        Property(name="reviews_User64", type=reviews_UserApprovalsMap, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_UserApprovalsMap63", type=reviews_User, multiplicity=Multiplicity(1, 1))
    }
)
file59: BinaryAssociation = BinaryAssociation(
    name="file59",
    ends={
        Property(name="reviews_FileItem61", type=reviews_FileVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_FileVersion60", type=reviews_FileItem, multiplicity=Multiplicity(0, 1))
    }
)
key69: BinaryAssociation = BinaryAssociation(
    name="key69",
    ends={
        Property(name="reviews_ApprovalType71", type=reviews_ApprovalValueMap, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_ApprovalValueMap70", type=reviews_ApprovalType, multiplicity=Multiplicity(1, 1))
    }
)
by72: BinaryAssociation = BinaryAssociation(
    name="by72",
    ends={
        Property(name="reviews_User73", type=reviews_RequirementEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_RequirementEntry", type=reviews_User, multiplicity=Multiplicity(0, 1))
    }
)
value65: BinaryAssociation = BinaryAssociation(
    name="value65",
    ends={
        Property(name="reviews_ReviewerEntry", type=reviews_UserApprovalsMap, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_UserApprovalsMap66", type=reviews_ReviewerEntry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
approvals67: BinaryAssociation = BinaryAssociation(
    name="approvals67",
    ends={
        Property(name="reviews_ApprovalValueMap", type=reviews_ReviewerEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_ReviewerEntry68", type=reviews_ApprovalValueMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key74: BinaryAssociation = BinaryAssociation(
    name="key74",
    ends={
        Property(name="reviews_ApprovalType76", type=reviews_ReviewRequirementsMap, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_ReviewRequirementsMap75", type=reviews_ApprovalType, multiplicity=Multiplicity(1, 1))
    }
)
value77: BinaryAssociation = BinaryAssociation(
    name="value77",
    ends={
        Property(name="reviews_RequirementEntry79", type=reviews_ReviewRequirementsMap, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews_ReviewRequirementsMap78", type=reviews_RequirementEntry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_reviews_Change_Dated = Generalization(general=Dated, specific=reviews_Change)
gen_reviews_Review_CommentContainer = Generalization(general=CommentContainer, specific=reviews_Review)
gen_reviews_Review_Change = Generalization(general=Change, specific=reviews_Review)
gen_reviews_Comment_Indexed = Generalization(general=Indexed, specific=reviews_Comment)
gen_reviews_Comment_Dated = Generalization(general=Dated, specific=reviews_Comment)
gen_reviews_ReviewItem_CommentContainer = Generalization(general=CommentContainer, specific=reviews_ReviewItem)
gen_reviews_Location_Indexed = Generalization(general=Indexed, specific=reviews_Location)
gen_reviews_FileItem_ReviewItem = Generalization(general=ReviewItem, specific=reviews_FileItem)
gen_reviews_ReviewItemSet_ReviewItem = Generalization(general=ReviewItem, specific=reviews_ReviewItemSet)
gen_reviews_ReviewItemSet_Dated = Generalization(general=Dated, specific=reviews_ReviewItemSet)
gen_reviews_LineLocation_Location = Generalization(general=Location, specific=reviews_LineLocation)
gen_reviews_FileVersion_ReviewItem = Generalization(general=ReviewItem, specific=reviews_FileVersion)

# Domain Model
domain_model = DomainModel(
    name="reviews",
    types={reviews_CommentContainer, reviews_Change, Dated, reviews_User, reviews_Review, CommentContainer, Change, reviews_ReviewItemSet, reviews_Repository, reviews_Comment, reviews_ReviewRequirementsMap, Indexed, reviews_Location, reviews_UserApprovalsMap, reviews_ReviewItem, reviews_FileItem, ReviewItem, reviews_FileVersion, reviews_ApprovalType, reviews_Commit, reviews_LineLocation, Location, reviews_LineRange, reviews_Indexed, reviews_Dated, reviews_ReviewerEntry, reviews_RequirementEntry, reviews_ApprovalValueMap, RequirementStatus, ReviewStatus},
    associations={drafts5, owner8, sets9, repository10, allComments0, comments1, reviewerApprovals16, allDrafts2, requirements18, author20, replies24, locations26, parents11, children13, addedBy32, committedBy34, review37, review28, item31, account41, reviews44, users45, base48, target49, set52, approvalTypes40, parentReview55, parentCommits57, ranges58, items54, key62, file59, key69, by72, value65, approvals67, key74, value77},
    generalizations={gen_reviews_Change_Dated, gen_reviews_Review_CommentContainer, gen_reviews_Review_Change, gen_reviews_Comment_Indexed, gen_reviews_Comment_Dated, gen_reviews_ReviewItem_CommentContainer, gen_reviews_Location_Indexed, gen_reviews_FileItem_ReviewItem, gen_reviews_ReviewItemSet_ReviewItem, gen_reviews_ReviewItemSet_Dated, gen_reviews_LineLocation_Location, gen_reviews_FileVersion_ReviewItem},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)