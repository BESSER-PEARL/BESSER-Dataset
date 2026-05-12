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
Date: Enumeration = Enumeration(
    name="Date",
    literals={
            
    }
)

Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

VIDEO: Enumeration = Enumeration(
    name="VIDEO",
    literals={
            
    }
)

MediaType: Enumeration = Enumeration(
    name="MediaType",
    literals={
            
    }
)

ContentPagePublicityState: Enumeration = Enumeration(
    name="ContentPagePublicityState",
    literals={
            
    }
)

PublicityState: Enumeration = Enumeration(
    name="PublicityState",
    literals={
            
    }
)

# Classes
User = Class(name="User")
Profile = Class(name="Profile")
Group = Class(name="Group")
Message = Class(name="Message")
Friend = Class(name="Friend")
AbstractEntity = Class(name="AbstractEntity", is_abstract=True)
Settings = Class(name="Settings")
MediaPool = Class(name="MediaPool")
Media = Class(name="Media")
Image = Class(name="Image")
Video = Class(name="Video")
Tenant = Class(name="Tenant")
int2_Interface = Class(name="int2_Interface")
LogEntry = Class(name="LogEntry")
AdminUser = Class(name="AdminUser")
Profile2 = Class(name="Profile2")
ContentPage = Class(name="ContentPage")
Tag = Class(name="Tag")
Address = Class(name="Address")

# User class attributes and methods
User_userId: Property = Property(name="userId", type=StringType)
User_active: Property = Property(name="active", type=BooleanType)
User_password: Property = Property(name="password", type=StringType)
User.attributes={User_password, User_active, User_userId}

# Profile class attributes and methods
Profile_username: Property = Property(name="username", type=StringType)
Profile_name: Property = Property(name="name", type=StringType)
Profile_firstName: Property = Property(name="firstName", type=StringType)
Profile_email: Property = Property(name="email", type=StringType)
Profile.attributes={Profile_firstName, Profile_name, Profile_username, Profile_email}

# Group class attributes and methods

# Message class attributes and methods

# Friend class attributes and methods

# AbstractEntity class attributes and methods
AbstractEntity_id: Property = Property(name="id", type=StringType)
AbstractEntity_createdAt: Property = Property(name="createdAt", type=Date)
AbstractEntity_createdBy: Property = Property(name="createdBy", type=User)
AbstractEntity_modifiedAt: Property = Property(name="modifiedAt", type=DateType)
AbstractEntity_modifiedBy: Property = Property(name="modifiedBy", type=User)
AbstractEntity.attributes={AbstractEntity_id, AbstractEntity_modifiedBy, AbstractEntity_createdAt, AbstractEntity_modifiedAt, AbstractEntity_createdBy}

# Settings class attributes and methods
Settings_username: Property = Property(name="username", type=StringType)
Settings_name: Property = Property(name="name", type=StringType)
Settings_firstName: Property = Property(name="firstName", type=StringType)
Settings_email: Property = Property(name="email", type=StringType)
Settings_notificationChannels: Property = Property(name="notificationChannels", type=StringType)
Settings.attributes={Settings_username, Settings_notificationChannels, Settings_firstName, Settings_name, Settings_email}

# MediaPool class attributes and methods
MediaPool_assets: Property = Property(name="assets", type=StringType)
MediaPool_name: Property = Property(name="name", type=StringType)
MediaPool.attributes={MediaPool_name, MediaPool_assets}

# Media class attributes and methods
Media_mimetype: Property = Property(name="mimetype", type=StringType)
Media_name: Property = Property(name="name", type=StringType)
Media_link: Property = Property(name="link", type=StringType)
Media_description: Property = Property(name="description", type=StringType)
Media_active: Property = Property(name="active", type=BooleanType)
Media_filesize: Property = Property(name="filesize", type=IntegerType)
Media_mediaPool: Property = Property(name="mediaPool", type=MediaPool)
Media.attributes={Media_active, Media_mimetype, Media_link, Media_filesize, Media_mediaPool, Media_name, Media_description}

# Image class attributes and methods

# Video class attributes and methods

# Tenant class attributes and methods
Tenant_id: Property = Property(name="id", type=StringType)
Tenant_name: Property = Property(name="name", type=StringType)
Tenant.attributes={Tenant_name, Tenant_id}

# int2_Interface class attributes and methods

# LogEntry class attributes and methods
LogEntry_objectType: Property = Property(name="objectType", type=StringType)
LogEntry_objectId: Property = Property(name="objectId", type=StringType)
LogEntry_time: Property = Property(name="time", type=StringType)
LogEntry__attr: Property = Property(name="_attr", type=StringType)
LogEntry.attributes={LogEntry_time, LogEntry__attr, LogEntry_objectType, LogEntry_objectId}

# AdminUser class attributes and methods
AdminUser_id: Property = Property(name="id", type=StringType)
AdminUser_active: Property = Property(name="active", type=BooleanType)
AdminUser_password: Property = Property(name="password", type=StringType)
AdminUser_roles: Property = Property(name="roles", type=StringType)
AdminUser_username: Property = Property(name="username", type=StringType)
AdminUser_email: Property = Property(name="email", type=StringType)
AdminUser_phone: Property = Property(name="phone", type=StringType)
AdminUser.attributes={AdminUser_phone, AdminUser_username, AdminUser_email, AdminUser_password, AdminUser_active, AdminUser_roles, AdminUser_id}

# Profile2 class attributes and methods
Profile2_username: Property = Property(name="username", type=StringType)
Profile2_name: Property = Property(name="name", type=StringType)
Profile2_firstName: Property = Property(name="firstName", type=StringType)
Profile2_email: Property = Property(name="email", type=StringType)
Profile2.attributes={Profile2_email, Profile2_name, Profile2_firstName, Profile2_username}

# ContentPage class attributes and methods
ContentPage_priority: Property = Property(name="priority", type=StringType)
ContentPage_priorityExpiryDate: Property = Property(name="priorityExpiryDate", type=Date)
ContentPage_title: Property = Property(name="title", type=StringType)
ContentPage_active: Property = Property(name="active", type=BooleanType)
ContentPage_content: Property = Property(name="content", type=StringType)
ContentPage_author: Property = Property(name="author", type=AdminUser)
ContentPage_externalSource: Property = Property(name="externalSource", type=StringType)
ContentPage_media: Property = Property(name="media", type=Media)
ContentPage_references: Property = Property(name="references", type=StringType)
ContentPage_address: Property = Property(name="address", type=Address)
ContentPage_date: Property = Property(name="date", type=Date)
ContentPage_headline: Property = Property(name="headline", type=StringType)
ContentPage_tags: Property = Property(name="tags", type=StringType)
ContentPage_state: Property = Property(name="state", type=StringType)
ContentPage_attribute: Property = Property(name="attribute", type=StringType)
ContentPage_publishingDate: Property = Property(name="publishingDate", type=Date)
ContentPage_expiryDate: Property = Property(name="expiryDate", type=Date)
ContentPage_content1: Property = Property(name="content1", type=StringType)
ContentPage.attributes={ContentPage_author, ContentPage_content, ContentPage_address, ContentPage_content1, ContentPage_publishingDate, ContentPage_references, ContentPage_active, ContentPage_attribute, ContentPage_expiryDate, ContentPage_priorityExpiryDate, ContentPage_media, ContentPage_date, ContentPage_tags, ContentPage_state, ContentPage_priority, ContentPage_externalSource, ContentPage_title, ContentPage_headline}

# Tag class attributes and methods
Tag_name: Property = Property(name="name", type=StringType)
Tag.attributes={Tag_name}

# Address class attributes and methods
Address_city: Property = Property(name="city", type=StringType)
Address_street: Property = Property(name="street", type=StringType)
Address_streetnumber: Property = Property(name="streetnumber", type=StringType)
Address_zipCode: Property = Property(name="zipCode", type=StringType)
Address_country: Property = Property(name="country", type=StringType)
Address.attributes={Address_city, Address_street, Address_streetnumber, Address_zipCode, Address_country}

# Relationships
User_Myprofile: BinaryAssociation = BinaryAssociation(
    name="User_Myprofile",
    ends={
        Property(name="myprofile0", type=Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="user1", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="group2", type=Group, multiplicity=Multiplicity(0, 9999)),
        Property(name="user3", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message4", type=Message, multiplicity=Multiplicity(0, 9999)),
        Property(name="user5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Profile_User: BinaryAssociation = BinaryAssociation(
    name="Profile_User",
    ends={
        Property(name="user6", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="profile7", type=Profile, multiplicity=Multiplicity(1, 1))
    }
)
Settings_User: BinaryAssociation = BinaryAssociation(
    name="Settings_User",
    ends={
        Property(name="user8", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="settings9", type=Settings, multiplicity=Multiplicity(1, 1))
    }
)
MediaPool_Media: BinaryAssociation = BinaryAssociation(
    name="MediaPool_Media",
    ends={
        Property(name="media10", type=Media, multiplicity=Multiplicity(0, 1)),
        Property(name="mediaPool11", type=MediaPool, multiplicity=Multiplicity(1, 1))
    }
)
MediaPool_Media2: BinaryAssociation = BinaryAssociation(
    name="MediaPool_Media2",
    ends={
        Property(name="assets12", type=Media, multiplicity=Multiplicity(1, 9999)),
        Property(name="mediaPool13", type=MediaPool, multiplicity=Multiplicity(1, 1))
    }
)
AbstractEntity_Tenant: BinaryAssociation = BinaryAssociation(
    name="AbstractEntity_Tenant",
    ends={
        Property(name="tenant14", type=Tenant, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractEntity15", type=AbstractEntity, multiplicity=Multiplicity(1, 9999))
    }
)
MediaPool_MediaPool: BinaryAssociation = BinaryAssociation(
    name="MediaPool_MediaPool",
    ends={
        Property(name="parent16", type=MediaPool, multiplicity=Multiplicity(0, 1)),
        Property(name="mediaPool17", type=MediaPool, multiplicity=Multiplicity(0, 1))
    }
)
ContentPage_Tag: BinaryAssociation = BinaryAssociation(
    name="ContentPage_Tag",
    ends={
        Property(name="tag18", type=Tag, multiplicity=Multiplicity(0, 1)),
        Property(name="contentPage19", type=ContentPage, multiplicity=Multiplicity(0, 1))
    }
)
User_Settings: BinaryAssociation = BinaryAssociation(
    name="User_Settings",
    ends={
        Property(name="settings20", type=Settings, multiplicity=Multiplicity(1, 1)),
        Property(name="user21", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Profile: BinaryAssociation = BinaryAssociation(
    name="User_Profile",
    ends={
        Property(name="profile22", type=Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="user23", type=User, multiplicity=Multiplicity(1, 1))
    }
)
ContentPage_Tag2: BinaryAssociation = BinaryAssociation(
    name="ContentPage_Tag2",
    ends={
        Property(name="tag24", type=Tag, multiplicity=Multiplicity(1, 9999)),
        Property(name="contentPage25", type=ContentPage, multiplicity=Multiplicity(1, 9999))
    }
)
Tenant_AbstractEntity: BinaryAssociation = BinaryAssociation(
    name="Tenant_AbstractEntity",
    ends={
        Property(name="abstractEntity26", type=AbstractEntity, multiplicity=Multiplicity(0, 9999)),
        Property(name="tenant27", type=Tenant, multiplicity=Multiplicity(1, 1))
    }
)
ContentPage_Address: BinaryAssociation = BinaryAssociation(
    name="ContentPage_Address",
    ends={
        Property(name="address28", type=Address, multiplicity=Multiplicity(0, 1)),
        Property(name="contentPage29", type=ContentPage, multiplicity=Multiplicity(0, 1))
    }
)
ContentPage_AdminUser: BinaryAssociation = BinaryAssociation(
    name="ContentPage_AdminUser",
    ends={
        Property(name="author30", type=AdminUser, multiplicity=Multiplicity(0, 1)),
        Property(name="contentPage31", type=ContentPage, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b3487372_ba60_4705_9d75_e4829af3c5db",
    types={User, Profile, Group, Message, Friend, AbstractEntity, Settings, MediaPool, Media, Image, Video, Tenant, int2_Interface, LogEntry, AdminUser, Profile2, ContentPage, Tag, Address, Date, Enumeration_, VIDEO, MediaType, ContentPagePublicityState, PublicityState},
    associations={User_Myprofile, User_Group, User_Message, Profile_User, Settings_User, MediaPool_Media, MediaPool_Media2, AbstractEntity_Tenant, MediaPool_MediaPool, ContentPage_Tag, User_Settings, User_Profile, ContentPage_Tag2, Tenant_AbstractEntity, ContentPage_Address, ContentPage_AdminUser},
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