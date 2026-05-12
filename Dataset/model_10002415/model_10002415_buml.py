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
String: Enumeration = Enumeration(
    name="String",
    literals={
            
    }
)

# Classes
User = Class(name="User")
Project = Class(name="Project")
Activity = Class(name="Activity")
Comment = Class(name="Comment")
Attachment = Class(name="Attachment")
Role = Class(name="Role")

# User class attributes and methods
User_UserID: Property = Property(name="UserID", type=IntegerType)
User_Username: Property = Property(name="Username", type=StringType)
User_Password: Property = Property(name="Password", type=StringType)
User_Firstname: Property = Property(name="Firstname", type=StringType)
User_Lastname: Property = Property(name="Lastname", type=StringType)
User_Dateofbirth: Property = Property(name="Dateofbirth", type=StringType)
User_Email: Property = Property(name="Email", type=StringType)
User_Phone: Property = Property(name="Phone", type=StringType)
User_DepartmentID: Property = Property(name="DepartmentID", type=IntegerType)
User_TitleID: Property = Property(name="TitleID", type=IntegerType)
User_Active: Property = Property(name="Active", type=BooleanType)
User_Settings: Property = Property(name="Settings", type=StringType)
User_Position: Property = Property(name="Position", type=StringType)
User_Hiredate: Property = Property(name="Hiredate", type=StringType)
User_About: Property = Property(name="About", type=StringType)
User_Facebook_link: Property = Property(name="Facebook_link", type=StringType)
User_Google_plus_link: Property = Property(name="Google_plus_link", type=StringType)
User_Linkedin_link: Property = Property(name="Linkedin_link", type=StringType)
User_Roles___: Property = Property(name="Roles___", type=StringType)
User.attributes={User_Google_plus_link, User_Dateofbirth, User_Username, User_Position, User_Settings, User_Email, User_Firstname, User_Active, User_Phone, User_Facebook_link, User_Lastname, User_Roles___, User_TitleID, User_Password, User_Hiredate, User_Linkedin_link, User_DepartmentID, User_UserID, User_About}

# Project class attributes and methods
Project_PorjectID: Property = Property(name="PorjectID", type=IntegerType)
Project_Title: Property = Property(name="Title", type=StringType)
Project_Created: Property = Property(name="Created", type=StringType)
Project_Deadline: Property = Property(name="Deadline", type=StringType)
Project_StatusID: Property = Property(name="StatusID", type=IntegerType)
Project_PriorityID: Property = Property(name="PriorityID", type=IntegerType)
Project_Author: Property = Property(name="Author", type=User)
Project_ProjectManager: Property = Property(name="ProjectManager", type=User)
Project_Assignee: Property = Property(name="Assignee", type=User)
Project_Description: Property = Property(name="Description", type=StringType)
Project_Team___: Property = Property(name="Team___", type=StringType)
Project_Subscriptions___: Property = Property(name="Subscriptions___", type=StringType)
Project_Comments___: Property = Property(name="Comments___", type=StringType)
Project_Attachments___: Property = Property(name="Attachments___", type=StringType)
Project_Activities___: Property = Property(name="Activities___", type=StringType)
Project.attributes={Project_PorjectID, Project_Title, Project_Comments___, Project_Description, Project_Activities___, Project_Author, Project_Created, Project_Attachments___, Project_ProjectManager, Project_Deadline, Project_Assignee, Project_PriorityID, Project_Subscriptions___, Project_StatusID, Project_Team___}

# Activity class attributes and methods
Activity_ActivityID: Property = Property(name="ActivityID", type=IntegerType)
Activity_User: Property = Property(name="User", type=User)
Activity_Project: Property = Property(name="Project", type=Project)
Activity_ActivityType: Property = Property(name="ActivityType", type=IntegerType)
Activity_ActivitySubType: Property = Property(name="ActivitySubType", type=IntegerType)
Activity_PrevValue: Property = Property(name="PrevValue", type=StringType)
Activity_NewValue: Property = Property(name="NewValue", type=StringType)
Activity_Seen: Property = Property(name="Seen", type=BooleanType)
Activity.attributes={Activity_ActivityType, Activity_User, Activity_Project, Activity_ActivitySubType, Activity_Seen, Activity_ActivityID, Activity_NewValue, Activity_PrevValue}

# Comment class attributes and methods
Comment_CommentID: Property = Property(name="CommentID", type=IntegerType)
Comment_User: Property = Property(name="User", type=User)
Comment_Project: Property = Property(name="Project", type=Project)
Comment_Created: Property = Property(name="Created", type=StringType)
Comment_Content: Property = Property(name="Content", type=StringType)
Comment.attributes={Comment_User, Comment_Content, Comment_Project, Comment_Created, Comment_CommentID}

# Attachment class attributes and methods
Attachment_AttachmentID: Property = Property(name="AttachmentID", type=IntegerType)
Attachment_User: Property = Property(name="User", type=User)
Attachment_Project: Property = Property(name="Project", type=Project)
Attachment_Created: Property = Property(name="Created", type=StringType)
Attachment_Size: Property = Property(name="Size", type=StringType)
Attachment_Extension: Property = Property(name="Extension", type=StringType)
Attachment_Path: Property = Property(name="Path", type=StringType)
Attachment_Name: Property = Property(name="Name", type=StringType)
Attachment.attributes={Attachment_Name, Attachment_Path, Attachment_Project, Attachment_Created, Attachment_User, Attachment_Size, Attachment_Extension, Attachment_AttachmentID}

# Role class attributes and methods
Role_RoleID: Property = Property(name="RoleID", type=IntegerType)
Role_Name: Property = Property(name="Name", type=String)
Role_Description: Property = Property(name="Description", type=StringType)
Role.attributes={Role_Description, Role_RoleID, Role_Name}

# Relationships
User_Project: BinaryAssociation = BinaryAssociation(
    name="User_Project",
    ends={
        Property(name="Author0", type=Project, multiplicity=Multiplicity(1, 1)),
        Property(name="User1", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Project2: BinaryAssociation = BinaryAssociation(
    name="User_Project2",
    ends={
        Property(name="ProjectMan_2", type=Project, multiplicity=Multiplicity(0, 9999)),
        Property(name="User3", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Project3: BinaryAssociation = BinaryAssociation(
    name="User_Project3",
    ends={
        Property(name="Assignee4", type=Project, multiplicity=Multiplicity(0, 9999)),
        Property(name="User5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Activity: BinaryAssociation = BinaryAssociation(
    name="User_Activity",
    ends={
        Property(name="Activity6", type=Activity, multiplicity=Multiplicity(0, 9999)),
        Property(name="User7", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Project_Activity: BinaryAssociation = BinaryAssociation(
    name="Project_Activity",
    ends={
        Property(name="Activity8", type=Activity, multiplicity=Multiplicity(0, 9999)),
        Property(name="Project9", type=Project, multiplicity=Multiplicity(1, 1))
    }
)
Project_Comment: BinaryAssociation = BinaryAssociation(
    name="Project_Comment",
    ends={
        Property(name="Comment10", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="Project11", type=Project, multiplicity=Multiplicity(1, 1))
    }
)
User_Comment: BinaryAssociation = BinaryAssociation(
    name="User_Comment",
    ends={
        Property(name="Comment12", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="User13", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Attachment: BinaryAssociation = BinaryAssociation(
    name="User_Attachment",
    ends={
        Property(name="Attachment14", type=Attachment, multiplicity=Multiplicity(0, 9999)),
        Property(name="User15", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Project_Attachment: BinaryAssociation = BinaryAssociation(
    name="Project_Attachment",
    ends={
        Property(name="Attachment16", type=Attachment, multiplicity=Multiplicity(0, 9999)),
        Property(name="Project17", type=Project, multiplicity=Multiplicity(1, 1))
    }
)
User_Role: BinaryAssociation = BinaryAssociation(
    name="User_Role",
    ends={
        Property(name="Role18", type=Role, multiplicity=Multiplicity(0, 9999)),
        Property(name="User19", type=User, multiplicity=Multiplicity(1, 9999))
    }
)
Project_User: BinaryAssociation = BinaryAssociation(
    name="Project_User",
    ends={
        Property(name="User20", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="Project21", type=Project, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b147a92a_1c28_4ab7_a667_c688ca646e4d",
    types={User, Project, Activity, Comment, Attachment, Role, String},
    associations={User_Project, User_Project2, User_Project3, User_Activity, Project_Activity, Project_Comment, User_Comment, User_Attachment, Project_Attachment, User_Role, Project_User},
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