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
VersionStatus: Enumeration = Enumeration(
    name="VersionStatus",
    literals={
            EnumerationLiteral(name="IN_PROGRESS"),
			EnumerationLiteral(name="COMPLETE")
    }
)

IssueStatus: Enumeration = Enumeration(
    name="IssueStatus",
    literals={
            EnumerationLiteral(name="OPEN"),
			EnumerationLiteral(name="CLOSED")
    }
)

IssueType: Enumeration = Enumeration(
    name="IssueType",
    literals={
            EnumerationLiteral(name="ENHANCEMENT"),
			EnumerationLiteral(name="BUG"),
			EnumerationLiteral(name="WONT_FIX"),
			EnumerationLiteral(name="HELP_REQUIRED"),
			EnumerationLiteral(name="DUPLICATE")
    }
)

# Classes
trackit_IssueTracker = Class(name="trackit::IssueTracker")
trackit_Team = Class(name="trackit::Team")
trackit_Product = Class(name="trackit::Product")
trackit_Issue = Class(name="trackit::Issue")
trackit_Member = Class(name="trackit::Member")
trackit_Identifiable = Class(name="trackit::Identifiable", is_abstract=True)
Identifiable = Class(name="Identifiable")
trackit_Comment = Class(name="trackit::Comment")
trackit_Version = Class(name="trackit::Version")

# trackit_IssueTracker class attributes and methods
trackit_IssueTracker_projectName: Property = Property(name="projectName", type=StringType)
trackit_IssueTracker.attributes={trackit_IssueTracker_projectName}

# trackit_Team class attributes and methods
trackit_Team_teamName: Property = Property(name="teamName", type=StringType)
trackit_Team.attributes={trackit_Team_teamName}

# trackit_Product class attributes and methods
trackit_Product_name: Property = Property(name="name", type=StringType)
trackit_Product.attributes={trackit_Product_name}

# trackit_Issue class attributes and methods
trackit_Issue_title: Property = Property(name="title", type=StringType)
trackit_Issue_description: Property = Property(name="description", type=StringType)
trackit_Issue_dateCreated: Property = Property(name="dateCreated", type=StringType)
trackit_Issue_status: Property = Property(name="status", type=StringType)
trackit_Issue_issueType: Property = Property(name="issueType", type=StringType)
trackit_Issue.attributes={trackit_Issue_dateCreated, trackit_Issue_issueType, trackit_Issue_title, trackit_Issue_status, trackit_Issue_description}

# trackit_Member class attributes and methods
trackit_Member_firstName: Property = Property(name="firstName", type=StringType)
trackit_Member_lastName: Property = Property(name="lastName", type=StringType)
trackit_Member_fullName: Property = Property(name="fullName", type=StringType)
trackit_Member.attributes={trackit_Member_lastName, trackit_Member_firstName, trackit_Member_fullName}

# trackit_Identifiable class attributes and methods
trackit_Identifiable_uuid: Property = Property(name="uuid", type=StringType)
trackit_Identifiable.attributes={trackit_Identifiable_uuid}

# Identifiable class attributes and methods

# trackit_Comment class attributes and methods
trackit_Comment_text: Property = Property(name="text", type=StringType)
trackit_Comment_dateCreated: Property = Property(name="dateCreated", type=StringType)
trackit_Comment.attributes={trackit_Comment_text, trackit_Comment_dateCreated}

# trackit_Version class attributes and methods
trackit_Version_name: Property = Property(name="name", type=StringType)
trackit_Version_status: Property = Property(name="status", type=StringType)
trackit_Version.attributes={trackit_Version_name, trackit_Version_status}

# Relationships
teams0: BinaryAssociation = BinaryAssociation(
    name="teams0",
    ends={
        Property(name="trackit_Team", type=trackit_IssueTracker, multiplicity=Multiplicity(1, 1)),
        Property(name="trackit_IssueTracker", type=trackit_Team, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
products1: BinaryAssociation = BinaryAssociation(
    name="products1",
    ends={
        Property(name="trackit_Product", type=trackit_IssueTracker, multiplicity=Multiplicity(1, 1)),
        Property(name="trackit_IssueTracker2", type=trackit_Product, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
issues3: BinaryAssociation = BinaryAssociation(
    name="issues3",
    ends={
        Property(name="trackit_Issue", type=trackit_IssueTracker, multiplicity=Multiplicity(1, 1)),
        Property(name="trackit_IssueTracker4", type=trackit_Issue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members5: BinaryAssociation = BinaryAssociation(
    name="members5",
    ends={
        Property(name="trackit_Member", type=trackit_IssueTracker, multiplicity=Multiplicity(1, 1)),
        Property(name="trackit_IssueTracker6", type=trackit_Member, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
comments8: BinaryAssociation = BinaryAssociation(
    name="comments8",
    ends={
        Property(name="Comment", type=trackit_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="author9", type=trackit_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
issuesAssigned10: BinaryAssociation = BinaryAssociation(
    name="issuesAssigned10",
    ends={
        Property(name="Issue11", type=trackit_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedTo", type=trackit_Issue, multiplicity=Multiplicity(0, 9999))
    }
)
members12: BinaryAssociation = BinaryAssociation(
    name="members12",
    ends={
        Property(name="trackit_Member14", type=trackit_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="trackit_Team13", type=trackit_Member, multiplicity=Multiplicity(1, 9999))
    }
)
issuesCreated7: BinaryAssociation = BinaryAssociation(
    name="issuesCreated7",
    ends={
        Property(name="Issue", type=trackit_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=trackit_Issue, multiplicity=Multiplicity(0, 9999))
    }
)
version15: BinaryAssociation = BinaryAssociation(
    name="version15",
    ends={
        Property(name="trackit_Version", type=trackit_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="trackit_Product16", type=trackit_Version, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
product17: BinaryAssociation = BinaryAssociation(
    name="product17",
    ends={
        Property(name="trackit_Product19", type=trackit_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="trackit_Version18", type=trackit_Product, multiplicity=Multiplicity(0, 1))
    }
)
issues20: BinaryAssociation = BinaryAssociation(
    name="issues20",
    ends={
        Property(name="Issue21", type=trackit_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="versionsAffected", type=trackit_Issue, multiplicity=Multiplicity(0, 9999))
    }
)
author22: BinaryAssociation = BinaryAssociation(
    name="author22",
    ends={
        Property(name="Member", type=trackit_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="issuesCreated", type=trackit_Member, multiplicity=Multiplicity(0, 1))
    }
)
blockers24: BinaryAssociation = BinaryAssociation(
    name="blockers24",
    ends={
        Property(name="Issue25", type=trackit_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="blocking", type=trackit_Issue, multiplicity=Multiplicity(0, 9999))
    }
)
assignedTo26: BinaryAssociation = BinaryAssociation(
    name="assignedTo26",
    ends={
        Property(name="Member27", type=trackit_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="issuesAssigned", type=trackit_Member, multiplicity=Multiplicity(0, 9999))
    }
)
comments28: BinaryAssociation = BinaryAssociation(
    name="comments28",
    ends={
        Property(name="Comment29", type=trackit_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="issue", type=trackit_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duplicateOf31: BinaryAssociation = BinaryAssociation(
    name="duplicateOf31",
    ends={
        Property(name="trackit_Issue32", type=trackit_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="trackit_Issue30", type=trackit_Issue, multiplicity=Multiplicity(0, 9999))
    }
)
dependencies34: BinaryAssociation = BinaryAssociation(
    name="dependencies34",
    ends={
        Property(name="trackit_Issue35", type=trackit_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="trackit_Issue33", type=trackit_Issue, multiplicity=Multiplicity(0, 9999))
    }
)
versionsAffected36: BinaryAssociation = BinaryAssociation(
    name="versionsAffected36",
    ends={
        Property(name="Version", type=trackit_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="issues", type=trackit_Version, multiplicity=Multiplicity(1, 9999))
    }
)
blocking38: BinaryAssociation = BinaryAssociation(
    name="blocking38",
    ends={
        Property(name="Issue39", type=trackit_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="blockers", type=trackit_Issue, multiplicity=Multiplicity(0, 9999))
    }
)
issue40: BinaryAssociation = BinaryAssociation(
    name="issue40",
    ends={
        Property(name="Issue41", type=trackit_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=trackit_Issue, multiplicity=Multiplicity(0, 1))
    }
)
author42: BinaryAssociation = BinaryAssociation(
    name="author42",
    ends={
        Property(name="Member44", type=trackit_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments43", type=trackit_Member, multiplicity=Multiplicity(0, 1))
    }
)
parent46: BinaryAssociation = BinaryAssociation(
    name="parent46",
    ends={
        Property(name="Comment47", type=trackit_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="replies", type=trackit_Comment, multiplicity=Multiplicity(0, 1))
    }
)
replies49: BinaryAssociation = BinaryAssociation(
    name="replies49",
    ends={
        Property(name="Comment50", type=trackit_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=trackit_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_trackit_Member_Identifiable = Generalization(general=Identifiable, specific=trackit_Member)
gen_trackit_Team_Identifiable = Generalization(general=Identifiable, specific=trackit_Team)
gen_trackit_Product_Identifiable = Generalization(general=Identifiable, specific=trackit_Product)
gen_trackit_Version_Identifiable = Generalization(general=Identifiable, specific=trackit_Version)
gen_trackit_Issue_Identifiable = Generalization(general=Identifiable, specific=trackit_Issue)
gen_trackit_Comment_Identifiable = Generalization(general=Identifiable, specific=trackit_Comment)

# Domain Model
domain_model = DomainModel(
    name="trackit",
    types={trackit_IssueTracker, trackit_Team, trackit_Product, trackit_Issue, trackit_Member, trackit_Identifiable, Identifiable, trackit_Comment, trackit_Version, VersionStatus, IssueStatus, IssueType},
    associations={teams0, products1, issues3, members5, comments8, issuesAssigned10, members12, issuesCreated7, version15, product17, issues20, author22, blockers24, assignedTo26, comments28, duplicateOf31, dependencies34, versionsAffected36, blocking38, issue40, author42, parent46, replies49},
    generalizations={gen_trackit_Member_Identifiable, gen_trackit_Team_Identifiable, gen_trackit_Product_Identifiable, gen_trackit_Version_Identifiable, gen_trackit_Issue_Identifiable, gen_trackit_Comment_Identifiable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)