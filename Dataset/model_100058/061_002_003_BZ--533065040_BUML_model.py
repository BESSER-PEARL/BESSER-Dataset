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
BZ_BZRepo = Class(name="BZ_BZRepo")
BZ_BZProduct = Class(name="BZ_BZProduct")
BZ_BZComponent = Class(name="BZ_BZComponent")
BZ_BZIssue = Class(name="BZ_BZIssue")
BZ_BZComment = Class(name="BZ_BZComment")
BZ_BZEvent = Class(name="BZ_BZEvent")

# BZ_BZRepo class attributes and methods
BZ_BZRepo_repoURL: Property = Property(name="repoURL", type=StringType)
BZ_BZRepo.attributes={BZ_BZRepo_repoURL}

# BZ_BZProduct class attributes and methods
BZ_BZProduct_productId: Property = Property(name="productId", type=StringType)
BZ_BZProduct_productDescription: Property = Property(name="productDescription", type=StringType)
BZ_BZProduct_productURL: Property = Property(name="productURL", type=StringType)
BZ_BZProduct.attributes={BZ_BZProduct_productId, BZ_BZProduct_productURL, BZ_BZProduct_productDescription}

# BZ_BZComponent class attributes and methods
BZ_BZComponent_componentId: Property = Property(name="componentId", type=StringType)
BZ_BZComponent_componentURL: Property = Property(name="componentURL", type=StringType)
BZ_BZComponent_componentDescription: Property = Property(name="componentDescription", type=StringType)
BZ_BZComponent_defaultAssignee: Property = Property(name="defaultAssignee", type=StringType)
BZ_BZComponent.attributes={BZ_BZComponent_componentDescription, BZ_BZComponent_componentURL, BZ_BZComponent_componentId, BZ_BZComponent_defaultAssignee}

# BZ_BZIssue class attributes and methods
BZ_BZIssue_issueId: Property = Property(name="issueId", type=IntegerType)
BZ_BZIssue_issueTitle: Property = Property(name="issueTitle", type=StringType)
BZ_BZIssue_issueURL: Property = Property(name="issueURL", type=StringType)
BZ_BZIssue_status: Property = Property(name="status", type=StringType)
BZ_BZIssue_productName: Property = Property(name="productName", type=StringType)
BZ_BZIssue_componentName: Property = Property(name="componentName", type=StringType)
BZ_BZIssue_classification: Property = Property(name="classification", type=StringType)
BZ_BZIssue_version: Property = Property(name="version", type=StringType)
BZ_BZIssue_platform: Property = Property(name="platform", type=StringType)
BZ_BZIssue_importance: Property = Property(name="importance", type=StringType)
BZ_BZIssue_milestone: Property = Property(name="milestone", type=StringType)
BZ_BZIssue_assignedTo: Property = Property(name="assignedTo", type=StringType)
BZ_BZIssue_keywords: Property = Property(name="keywords", type=StringType)
BZ_BZIssue_referenceURL: Property = Property(name="referenceURL", type=StringType)
BZ_BZIssue_dependsOn: Property = Property(name="dependsOn", type=StringType)
BZ_BZIssue_blocks: Property = Property(name="blocks", type=StringType)
BZ_BZIssue_reportedBy: Property = Property(name="reportedBy", type=StringType)
BZ_BZIssue_reportedByUsername: Property = Property(name="reportedByUsername", type=StringType)
BZ_BZIssue_reportedOn: Property = Property(name="reportedOn", type=DateType)
BZ_BZIssue_lastModifiedOn: Property = Property(name="lastModifiedOn", type=DateType)
BZ_BZIssue_ccList: Property = Property(name="ccList", type=StringType)
BZ_BZIssue_seeAlso: Property = Property(name="seeAlso", type=StringType)
BZ_BZIssue_latestCommit: Property = Property(name="latestCommit", type=StringType)
BZ_BZIssue_versionFixedIn: Property = Property(name="versionFixedIn", type=StringType)
BZ_BZIssue.attributes={BZ_BZIssue_importance, BZ_BZIssue_assignedTo, BZ_BZIssue_blocks, BZ_BZIssue_productName, BZ_BZIssue_issueURL, BZ_BZIssue_componentName, BZ_BZIssue_issueTitle, BZ_BZIssue_versionFixedIn, BZ_BZIssue_platform, BZ_BZIssue_classification, BZ_BZIssue_reportedBy, BZ_BZIssue_issueId, BZ_BZIssue_seeAlso, BZ_BZIssue_reportedByUsername, BZ_BZIssue_version, BZ_BZIssue_ccList, BZ_BZIssue_keywords, BZ_BZIssue_latestCommit, BZ_BZIssue_lastModifiedOn, BZ_BZIssue_dependsOn, BZ_BZIssue_milestone, BZ_BZIssue_status, BZ_BZIssue_reportedOn, BZ_BZIssue_referenceURL}

# BZ_BZComment class attributes and methods
BZ_BZComment_issueId: Property = Property(name="issueId", type=IntegerType)
BZ_BZComment_commentId: Property = Property(name="commentId", type=StringType)
BZ_BZComment_commentAuthor: Property = Property(name="commentAuthor", type=StringType)
BZ_BZComment_commentTime: Property = Property(name="commentTime", type=DateType)
BZ_BZComment_commentHTML: Property = Property(name="commentHTML", type=StringType)
BZ_BZComment_commentText: Property = Property(name="commentText", type=StringType)
BZ_BZComment.attributes={BZ_BZComment_commentHTML, BZ_BZComment_commentTime, BZ_BZComment_commentId, BZ_BZComment_commentAuthor, BZ_BZComment_issueId, BZ_BZComment_commentText}

# BZ_BZEvent class attributes and methods
BZ_BZEvent_author: Property = Property(name="author", type=StringType)
BZ_BZEvent_date: Property = Property(name="date", type=DateType)
BZ_BZEvent_field: Property = Property(name="field", type=StringType)
BZ_BZEvent_oldValue: Property = Property(name="oldValue", type=StringType)
BZ_BZEvent_newValue: Property = Property(name="newValue", type=StringType)
BZ_BZEvent_issueId: Property = Property(name="issueId", type=IntegerType)
BZ_BZEvent.attributes={BZ_BZEvent_issueId, BZ_BZEvent_author, BZ_BZEvent_newValue, BZ_BZEvent_date, BZ_BZEvent_field, BZ_BZEvent_oldValue}

# Relationships
products0: BinaryAssociation = BinaryAssociation(
    name="products0",
    ends={
        Property(name="BZProduct", type=BZ_BZRepo, multiplicity=Multiplicity(1, 1)),
        Property(name="repo", type=BZ_BZProduct, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
issues11: BinaryAssociation = BinaryAssociation(
    name="issues11",
    ends={
        Property(name="BZIssue12", type=BZ_BZComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="component", type=BZ_BZIssue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
product13: BinaryAssociation = BinaryAssociation(
    name="product13",
    ends={
        Property(name="BZProduct14", type=BZ_BZComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components", type=BZ_BZProduct, multiplicity=Multiplicity(1, 1))
    }
)
repo15: BinaryAssociation = BinaryAssociation(
    name="repo15",
    ends={
        Property(name="BZRepo17", type=BZ_BZComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components16", type=BZ_BZRepo, multiplicity=Multiplicity(1, 1))
    }
)
components1: BinaryAssociation = BinaryAssociation(
    name="components1",
    ends={
        Property(name="BZComponent", type=BZ_BZRepo, multiplicity=Multiplicity(1, 1)),
        Property(name="repo2", type=BZ_BZComponent, multiplicity=Multiplicity(0, 9999))
    }
)
issues3: BinaryAssociation = BinaryAssociation(
    name="issues3",
    ends={
        Property(name="BZIssue", type=BZ_BZRepo, multiplicity=Multiplicity(1, 1)),
        Property(name="repo4", type=BZ_BZIssue, multiplicity=Multiplicity(0, 9999))
    }
)
repo5: BinaryAssociation = BinaryAssociation(
    name="repo5",
    ends={
        Property(name="BZRepo", type=BZ_BZProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="products", type=BZ_BZRepo, multiplicity=Multiplicity(1, 1))
    }
)
components6: BinaryAssociation = BinaryAssociation(
    name="components6",
    ends={
        Property(name="BZComponent7", type=BZ_BZProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="product", type=BZ_BZComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
issues8: BinaryAssociation = BinaryAssociation(
    name="issues8",
    ends={
        Property(name="BZIssue10", type=BZ_BZProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="product9", type=BZ_BZIssue, multiplicity=Multiplicity(0, 9999))
    }
)
product26: BinaryAssociation = BinaryAssociation(
    name="product26",
    ends={
        Property(name="BZProduct28", type=BZ_BZIssue, multiplicity=Multiplicity(1, 1)),
        Property(name="issues27", type=BZ_BZProduct, multiplicity=Multiplicity(1, 1))
    }
)
issue29: BinaryAssociation = BinaryAssociation(
    name="issue29",
    ends={
        Property(name="BZIssue30", type=BZ_BZComment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=BZ_BZIssue, multiplicity=Multiplicity(1, 1))
    }
)
issue31: BinaryAssociation = BinaryAssociation(
    name="issue31",
    ends={
        Property(name="BZIssue32", type=BZ_BZEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="events", type=BZ_BZIssue, multiplicity=Multiplicity(1, 1))
    }
)
repo18: BinaryAssociation = BinaryAssociation(
    name="repo18",
    ends={
        Property(name="BZRepo19", type=BZ_BZIssue, multiplicity=Multiplicity(1, 1)),
        Property(name="issues", type=BZ_BZRepo, multiplicity=Multiplicity(1, 1))
    }
)
comments20: BinaryAssociation = BinaryAssociation(
    name="comments20",
    ends={
        Property(name="BZComment", type=BZ_BZIssue, multiplicity=Multiplicity(1, 1)),
        Property(name="issue", type=BZ_BZComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events21: BinaryAssociation = BinaryAssociation(
    name="events21",
    ends={
        Property(name="BZEvent", type=BZ_BZIssue, multiplicity=Multiplicity(1, 1)),
        Property(name="issue22", type=BZ_BZEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
component23: BinaryAssociation = BinaryAssociation(
    name="component23",
    ends={
        Property(name="BZComponent25", type=BZ_BZIssue, multiplicity=Multiplicity(1, 1)),
        Property(name="issues24", type=BZ_BZComponent, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="BZ",
    types={BZ_BZRepo, BZ_BZProduct, BZ_BZComponent, BZ_BZIssue, BZ_BZComment, BZ_BZEvent},
    associations={products0, issues11, product13, repo15, components1, issues3, repo5, components6, issues8, product26, issue29, issue31, repo18, comments20, events21, component23},
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