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
IssueStatus: Enumeration = Enumeration(
    name="IssueStatus",
    literals={
            EnumerationLiteral(name="OPEN"),
			EnumerationLiteral(name="CLOSED"),
			EnumerationLiteral(name="ASSIGNED"),
			EnumerationLiteral(name="RESOLVED")
    }
)

VersionStatus: Enumeration = Enumeration(
    name="VersionStatus",
    literals={
            EnumerationLiteral(name="CLOSED"),
			EnumerationLiteral(name="OPEN"),
			EnumerationLiteral(name="INPROGRESS")
    }
)

IssuePriority: Enumeration = Enumeration(
    name="IssuePriority",
    literals={
            EnumerationLiteral(name="HIGHER"),
			EnumerationLiteral(name="HIGH"),
			EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="LOW"),
			EnumerationLiteral(name="LOWER")
    }
)

DependencyType: Enumeration = Enumeration(
    name="DependencyType",
    literals={
            EnumerationLiteral(name="START_START"),
			EnumerationLiteral(name="START_END"),
			EnumerationLiteral(name="END_START"),
			EnumerationLiteral(name="END_END")
    }
)

# Classes
itm_Project = Class(name="itm_Project")
itm_Tracker = Class(name="itm_Tracker")
itm_Role = Class(name="itm_Role")
itm_User = Class(name="itm_User")
itm_Version = Class(name="itm_Version")
itm_IssueCategory = Class(name="itm_IssueCategory")
itm_Member = Class(name="itm_Member")
itm_IssueTrackingDatabase = Class(name="itm_IssueTrackingDatabase")
itm_IssueDependency = Class(name="itm_IssueDependency")
itm_Issue = Class(name="itm_Issue")

# itm_Project class attributes and methods
itm_Project_name: Property = Property(name="name", type=StringType)
itm_Project_description: Property = Property(name="description", type=StringType)
itm_Project.attributes={itm_Project_description, itm_Project_name}

# itm_Tracker class attributes and methods
itm_Tracker_name: Property = Property(name="name", type=StringType)
itm_Tracker.attributes={itm_Tracker_name}

# itm_Role class attributes and methods
itm_Role_name: Property = Property(name="name", type=StringType)
itm_Role_permissions: Property = Property(name="permissions", type=StringType)
itm_Role.attributes={itm_Role_name, itm_Role_permissions}

# itm_User class attributes and methods
itm_User_login: Property = Property(name="login", type=StringType)
itm_User_language: Property = Property(name="language", type=StringType)
itm_User.attributes={itm_User_language, itm_User_login}

# itm_Version class attributes and methods
itm_Version_description: Property = Property(name="description", type=StringType)
itm_Version_name: Property = Property(name="name", type=StringType)
itm_Version_status: Property = Property(name="status", type=StringType)
itm_Version_completedDate: Property = Property(name="completedDate", type=DateType)
itm_Version.attributes={itm_Version_completedDate, itm_Version_status, itm_Version_name, itm_Version_description}

# itm_IssueCategory class attributes and methods
itm_IssueCategory_name: Property = Property(name="name", type=StringType)
itm_IssueCategory.attributes={itm_IssueCategory_name}

# itm_Member class attributes and methods

# itm_IssueTrackingDatabase class attributes and methods

# itm_IssueDependency class attributes and methods
itm_IssueDependency_type: Property = Property(name="type", type=StringType)
itm_IssueDependency.attributes={itm_IssueDependency_type}

# itm_Issue class attributes and methods
itm_Issue_status: Property = Property(name="status", type=StringType)
itm_Issue_priority: Property = Property(name="priority", type=StringType)
itm_Issue_dueDate: Property = Property(name="dueDate", type=DateType)
itm_Issue_completedDate: Property = Property(name="completedDate", type=DateType)
itm_Issue_name: Property = Property(name="name", type=StringType)
itm_Issue_description: Property = Property(name="description", type=StringType)
itm_Issue_doneRatio: Property = Property(name="doneRatio", type=FloatType)
itm_Issue_estimatedHours: Property = Property(name="estimatedHours", type=FloatType)
itm_Issue_elapsedHours: Property = Property(name="elapsedHours", type=FloatType)
itm_Issue.attributes={itm_Issue_status, itm_Issue_estimatedHours, itm_Issue_description, itm_Issue_dueDate, itm_Issue_completedDate, itm_Issue_name, itm_Issue_elapsedHours, itm_Issue_priority, itm_Issue_doneRatio}

# Relationships
projects0: BinaryAssociation = BinaryAssociation(
    name="projects0",
    ends={
        Property(name="itm_Project", type=itm_IssueTrackingDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_IssueTrackingDatabase", type=itm_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trackers1: BinaryAssociation = BinaryAssociation(
    name="trackers1",
    ends={
        Property(name="itm_Tracker", type=itm_IssueTrackingDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_IssueTrackingDatabase2", type=itm_Tracker, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
roles3: BinaryAssociation = BinaryAssociation(
    name="roles3",
    ends={
        Property(name="itm_Role", type=itm_IssueTrackingDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_IssueTrackingDatabase4", type=itm_Role, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
users5: BinaryAssociation = BinaryAssociation(
    name="users5",
    ends={
        Property(name="itm_User", type=itm_IssueTrackingDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_IssueTrackingDatabase6", type=itm_User, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
versions7: BinaryAssociation = BinaryAssociation(
    name="versions7",
    ends={
        Property(name="itm_Version", type=itm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Project8", type=itm_Version, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
issueCategories9: BinaryAssociation = BinaryAssociation(
    name="issueCategories9",
    ends={
        Property(name="itm_IssueCategory", type=itm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Project10", type=itm_IssueCategory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members11: BinaryAssociation = BinaryAssociation(
    name="members11",
    ends={
        Property(name="itm_Member", type=itm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Project12", type=itm_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tracker15: BinaryAssociation = BinaryAssociation(
    name="tracker15",
    ends={
        Property(name="itm_Tracker17", type=itm_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Issue16", type=itm_Tracker, multiplicity=Multiplicity(1, 1))
    }
)
dependencies18: BinaryAssociation = BinaryAssociation(
    name="dependencies18",
    ends={
        Property(name="itm_IssueDependency", type=itm_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Issue19", type=itm_IssueDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
category20: BinaryAssociation = BinaryAssociation(
    name="category20",
    ends={
        Property(name="itm_IssueCategory22", type=itm_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Issue21", type=itm_IssueCategory, multiplicity=Multiplicity(0, 1))
    }
)
owner23: BinaryAssociation = BinaryAssociation(
    name="owner23",
    ends={
        Property(name="itm_Member25", type=itm_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Issue24", type=itm_Member, multiplicity=Multiplicity(1, 1))
    }
)
responsible26: BinaryAssociation = BinaryAssociation(
    name="responsible26",
    ends={
        Property(name="itm_Member28", type=itm_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Issue27", type=itm_Member, multiplicity=Multiplicity(1, 1))
    }
)
issues13: BinaryAssociation = BinaryAssociation(
    name="issues13",
    ends={
        Property(name="itm_Issue", type=itm_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Version14", type=itm_Issue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user32: BinaryAssociation = BinaryAssociation(
    name="user32",
    ends={
        Property(name="itm_User34", type=itm_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Member33", type=itm_User, multiplicity=Multiplicity(1, 1))
    }
)
role35: BinaryAssociation = BinaryAssociation(
    name="role35",
    ends={
        Property(name="itm_Role37", type=itm_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_Member36", type=itm_Role, multiplicity=Multiplicity(1, 1))
    }
)
dependentTask29: BinaryAssociation = BinaryAssociation(
    name="dependentTask29",
    ends={
        Property(name="itm_Issue31", type=itm_IssueDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="itm_IssueDependency30", type=itm_Issue, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="itm",
    types={itm_Project, itm_Tracker, itm_Role, itm_User, itm_Version, itm_IssueCategory, itm_Member, itm_IssueTrackingDatabase, itm_IssueDependency, itm_Issue, IssueStatus, VersionStatus, IssuePriority, DependencyType},
    associations={projects0, trackers1, roles3, users5, versions7, issueCategories9, members11, tracker15, dependencies18, category20, owner23, responsible26, issues13, user32, role35, dependentTask29},
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