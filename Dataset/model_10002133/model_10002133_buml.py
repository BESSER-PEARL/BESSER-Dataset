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
ResourceType: Enumeration = Enumeration(
    name="ResourceType",
    literals={
            
    }
)

ApprovalType: Enumeration = Enumeration(
    name="ApprovalType",
    literals={
            
    }
)

CrudType: Enumeration = Enumeration(
    name="CrudType",
    literals={
            
    }
)

AllowType: Enumeration = Enumeration(
    name="AllowType",
    literals={
            
    }
)

ScopeType: Enumeration = Enumeration(
    name="ScopeType",
    literals={
            
    }
)

Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
Organization = Class(name="Organization")
User = Class(name="User")
Group = Class(name="Group")
Event = Class(name="Event")
Panel = Class(name="Panel")
Resource = Class(name="Resource")
Permission = Class(name="Permission")

# Organization class attributes and methods
Organization_Id: Property = Property(name="Id", type=IntegerType)
Organization_Name: Property = Property(name="Name", type=StringType)
Organization_Description: Property = Property(name="Description", type=StringType)
Organization_Url: Property = Property(name="Url", type=StringType)
Organization_Groups: Property = Property(name="Groups", type=Group)
Organization_Events: Property = Property(name="Events", type=Event)
Organization_Owners: Property = Property(name="Owners", type=User)
Organization.attributes={Organization_Description, Organization_Groups, Organization_Id, Organization_Name, Organization_Owners, Organization_Url, Organization_Events}

# User class attributes and methods
User_UserName: Property = Property(name="UserName", type=StringType)
User_UserHash: Property = Property(name="UserHash", type=IntegerType)
User_UserNameFull: Property = Property(name="UserNameFull", type=StringType)
User_EmailAddress: Property = Property(name="EmailAddress", type=StringType)
User_Password: Property = Property(name="Password", type=StringType)
User_Id: Property = Property(name="Id", type=IntegerType)
User_FirstName: Property = Property(name="FirstName", type=StringType)
User_LastName: Property = Property(name="LastName", type=StringType)
User.attributes={User_FirstName, User_Id, User_LastName, User_UserHash, User_UserNameFull, User_Password, User_UserName, User_EmailAddress}

# Group class attributes and methods
Group_Id: Property = Property(name="Id", type=IntegerType)
Group_Name: Property = Property(name="Name", type=StringType)
Group_Users: Property = Property(name="Users", type=User)
Group_Permissions: Property = Property(name="Permissions", type=Permission)
Group_Scope: Property = Property(name="Scope", type=ScopeType)
Group_ScopeId: Property = Property(name="ScopeId", type=IntegerType)
Group.attributes={Group_ScopeId, Group_Id, Group_Scope, Group_Users, Group_Name, Group_Permissions}

# Event class attributes and methods
Event_Id: Property = Property(name="Id", type=IntegerType)
Event_Name: Property = Property(name="Name", type=StringType)
Event_Description: Property = Property(name="Description", type=StringType)
Event_Date: Property = Property(name="Date", type=StringType)
Event_Panels: Property = Property(name="Panels", type=Panel)
Event_Resources: Property = Property(name="Resources", type=Resource)
Event_Groups: Property = Property(name="Groups", type=Group)
Event.attributes={Event_Date, Event_Panels, Event_Description, Event_Id, Event_Groups, Event_Resources, Event_Name}

# Panel class attributes and methods
Panel_Id: Property = Property(name="Id", type=IntegerType)
Panel_Name: Property = Property(name="Name", type=StringType)
Panel_Submitter: Property = Property(name="Submitter", type=User)
Panel_Description: Property = Property(name="Description", type=StringType)
Panel_Scheduled: Property = Property(name="Scheduled", type=StringType)
Panel_Length: Property = Property(name="Length", type=IntegerType)
Panel_PreBufferTime: Property = Property(name="PreBufferTime", type=IntegerType)
Panel_PostBufferTime: Property = Property(name="PostBufferTime", type=IntegerType)
Panel_Approval: Property = Property(name="Approval", type=ApprovalType)
Panel_Resources: Property = Property(name="Resources", type=Resource)
Panel_Private: Property = Property(name="Private", type=BooleanType)
Panel_Panelists: Property = Property(name="Panelists", type=User)
Panel.attributes={Panel_PostBufferTime, Panel_Name, Panel_Private, Panel_Length, Panel_PreBufferTime, Panel_Submitter, Panel_Resources, Panel_Description, Panel_Id, Panel_Panelists, Panel_Scheduled, Panel_Approval}

# Resource class attributes and methods
Resource_Id: Property = Property(name="Id", type=IntegerType)
Resource_Name: Property = Property(name="Name", type=StringType)
Resource_Description: Property = Property(name="Description", type=StringType)
Resource_NumberAvailable: Property = Property(name="NumberAvailable", type=IntegerType)
Resource_Type: Property = Property(name="Type", type=ResourceType)
Resource_Private: Property = Property(name="Private", type=BooleanType)
Resource.attributes={Resource_Id, Resource_Private, Resource_Description, Resource_Type, Resource_NumberAvailable, Resource_Name}

# Permission class attributes and methods
Permission_Id: Property = Property(name="Id", type=IntegerType)
Permission_Name: Property = Property(name="Name", type=StringType)
Permission_Crud: Property = Property(name="Crud", type=CrudType)
Permission_Allow: Property = Property(name="Allow", type=AllowType)
Permission_Scope: Property = Property(name="Scope", type=ScopeType)
Permission.attributes={Permission_Name, Permission_Id, Permission_Crud, Permission_Allow, Permission_Scope}

# Domain Model
domain_model = DomainModel(
    name="_qkkm4NGAEeib2vfQ4l86Yg",
    types={Organization, User, Group, Event, Panel, Resource, Permission, ResourceType, ApprovalType, CrudType, AllowType, ScopeType, Enumeration_},
    associations={},
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