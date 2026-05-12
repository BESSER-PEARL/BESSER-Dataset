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
User = Class(name="User")
Group = Class(name="Group")
User__ = Class(name="User__")
Post = Class(name="Post")
Page = Class(name="Page")
HashTags = Class(name="HashTags")
User2_Interface = Class(name="User2_Interface")
Users_User = Class(name="Users_User")
Users_Normal_User = Class(name="Users_Normal_User")
Users_Premium_User = Class(name="Users_Premium_User")
User_Interactions_Page = Class(name="User_Interactions_Page")
User_Interactions_Group = Class(name="User_Interactions_Group")
User_Interactions_Post = Class(name="User_Interactions_Post")
User_Interactions_HashTags = Class(name="User_Interactions_HashTags")
User_Interactions_Message = Class(name="User_Interactions_Message")
User_Interactions_Search = Class(name="User_Interactions_Search")
GUI_GUI = Class(name="GUI_GUI")
Back_End_API_PaymentMethod = Class(name="Back_End_API_PaymentMethod")
Back_End_API_PayPal = Class(name="Back_End_API_PayPal")
Back_End_API_CreditCard = Class(name="Back_End_API_CreditCard")
System_Controller_User_Controller = Class(name="System_Controller_User_Controller")
System_Controller_System_Controller = Class(name="System_Controller_System_Controller")
System_Control = Class(name="System_Control")
Normal_User = Class(name="Normal_User")
Premuim_User = Class(name="Premuim_User")
Post2 = Class(name="Post2")
Listeener = Class(name="Listeener")
List_User__Interface = Class(name="List_User__Interface")
User1 = Class(name="User1")
Normal_User1 = Class(name="Normal_User1")
Premium_User = Class(name="Premium_User")
User_Controller = Class(name="User_Controller")
System_Controller = Class(name="System_Controller")
Page1 = Class(name="Page1")
Message = Class(name="Message")
Search = Class(name="Search")
Group1 = Class(name="Group1")
Post1 = Class(name="Post1")
HashTags1 = Class(name="HashTags1")
PaymentMethod = Class(name="PaymentMethod")
PayPal = Class(name="PayPal")
CreditCard = Class(name="CreditCard")
GUI = Class(name="GUI")

# User class attributes and methods
User_pages: Property = Property(name="pages", type=StringType)
User_name: Property = Property(name="name", type=StringType)
User_username: Property = Property(name="username", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_gender: Property = Property(name="gender", type=StringType)
User_groups: Property = Property(name="groups", type=StringType)
User.attributes={User_username, User_email, User_name, User_password, User_gender, User_groups, User_pages}

# Group class attributes and methods
Group_name: Property = Property(name="name", type=StringType)
Group_description: Property = Property(name="description", type=StringType)
Group_admins: Property = Property(name="admins", type=User__)
Group_members: Property = Property(name="members", type=User__)
Group_nMembers: Property = Property(name="nMembers", type=IntegerType)
Group_posts: Property = Property(name="posts", type=StringType)
Group.attributes={Group_admins, Group_description, Group_members, Group_nMembers, Group_name, Group_posts}

# User__ class attributes and methods

# Post class attributes and methods
Post_privateMode: Property = Property(name="privateMode", type=BooleanType)
Post_nLikes: Property = Property(name="nLikes", type=IntegerType)
Post_nComments: Property = Property(name="nComments", type=IntegerType)
Post_nShares: Property = Property(name="nShares", type=IntegerType)
Post_owner: Property = Property(name="owner", type=User)
Post.attributes={Post_nShares, Post_privateMode, Post_nComments, Post_nLikes, Post_owner}

# Page class attributes and methods
Page_name: Property = Property(name="name", type=StringType)
Page_admin: Property = Property(name="admin", type=User)
Page_fans: Property = Property(name="fans", type=User__)
Page_description: Property = Property(name="description", type=StringType)
Page_posts: Property = Property(name="posts", type=StringType)
Page_nFans: Property = Property(name="nFans", type=IntegerType)
Page.attributes={Page_fans, Page_name, Page_admin, Page_posts, Page_description, Page_nFans}

# HashTags class attributes and methods
HashTags_allHashTags: Property = Property(name="allHashTags", type=StringType)
HashTags.attributes={HashTags_allHashTags}

# User2_Interface class attributes and methods

# Users_User class attributes and methods
Users_User_UserID: Property = Property(name="UserID", type=IntegerType)
Users_User_Full_Name: Property = Property(name="Full_Name", type=StringType)
Users_User_username: Property = Property(name="username", type=StringType)
Users_User_email: Property = Property(name="email", type=StringType)
Users_User_Gender: Property = Property(name="Gender", type=StringType)
Users_User_password: Property = Property(name="password", type=StringType)
Users_User_Age: Property = Property(name="Age", type=IntegerType)
Users_User_pages: Property = Property(name="pages", type=StringType)
Users_User_groups: Property = Property(name="groups", type=StringType)
Users_User_Messages: Property = Property(name="Messages", type=StringType)
Users_User_Friends: Property = Property(name="Friends", type=List_User__Interface)
Users_User_FriendRequests: Property = Property(name="FriendRequests", type=StringType)
Users_User_Privacy: Property = Property(name="Privacy", type=StringType)
Users_User.attributes={Users_User_Friends, Users_User_Privacy, Users_User_FriendRequests, Users_User_groups, Users_User_username, Users_User_Full_Name, Users_User_email, Users_User_pages, Users_User_password, Users_User_Messages, Users_User_Gender, Users_User_Age, Users_User_UserID}

# Users_Normal_User class attributes and methods

# Users_Premium_User class attributes and methods

# User_Interactions_Page class attributes and methods
User_Interactions_Page_posts: Property = Property(name="posts", type=StringType)
User_Interactions_Page_nFans: Property = Property(name="nFans", type=IntegerType)
User_Interactions_Page_name: Property = Property(name="name", type=StringType)
User_Interactions_Page_admin: Property = Property(name="admin", type=User)
User_Interactions_Page_fans: Property = Property(name="fans", type=User__)
User_Interactions_Page_description: Property = Property(name="description", type=StringType)
User_Interactions_Page.attributes={User_Interactions_Page_name, User_Interactions_Page_admin, User_Interactions_Page_description, User_Interactions_Page_nFans, User_Interactions_Page_fans, User_Interactions_Page_posts}

# User_Interactions_Group class attributes and methods
User_Interactions_Group_name: Property = Property(name="name", type=StringType)
User_Interactions_Group_description: Property = Property(name="description", type=StringType)
User_Interactions_Group_admins: Property = Property(name="admins", type=User__)
User_Interactions_Group_members: Property = Property(name="members", type=User__)
User_Interactions_Group_nMembers: Property = Property(name="nMembers", type=IntegerType)
User_Interactions_Group_posts: Property = Property(name="posts", type=StringType)
User_Interactions_Group.attributes={User_Interactions_Group_members, User_Interactions_Group_nMembers, User_Interactions_Group_admins, User_Interactions_Group_description, User_Interactions_Group_name, User_Interactions_Group_posts}

# User_Interactions_Post class attributes and methods
User_Interactions_Post_privateMode: Property = Property(name="privateMode", type=BooleanType)
User_Interactions_Post_nLikes: Property = Property(name="nLikes", type=IntegerType)
User_Interactions_Post_nComments: Property = Property(name="nComments", type=IntegerType)
User_Interactions_Post_nShares: Property = Property(name="nShares", type=IntegerType)
User_Interactions_Post_owner: Property = Property(name="owner", type=User)
User_Interactions_Post.attributes={User_Interactions_Post_nShares, User_Interactions_Post_privateMode, User_Interactions_Post_owner, User_Interactions_Post_nComments, User_Interactions_Post_nLikes}

# User_Interactions_HashTags class attributes and methods
User_Interactions_HashTags_allHashTags: Property = Property(name="allHashTags", type=StringType)
User_Interactions_HashTags.attributes={User_Interactions_HashTags_allHashTags}

# User_Interactions_Message class attributes and methods
User_Interactions_Message_SenderID: Property = Property(name="SenderID", type=IntegerType)
User_Interactions_Message_ReceiverID: Property = Property(name="ReceiverID", type=IntegerType)
User_Interactions_Message_MessageContent: Property = Property(name="MessageContent", type=StringType)
User_Interactions_Message_Time: Property = Property(name="Time", type=IntegerType)
User_Interactions_Message_Seen: Property = Property(name="Seen", type=BooleanType)
User_Interactions_Message_Deliverd: Property = Property(name="Deliverd", type=BooleanType)
User_Interactions_Message.attributes={User_Interactions_Message_ReceiverID, User_Interactions_Message_SenderID, User_Interactions_Message_Time, User_Interactions_Message_MessageContent, User_Interactions_Message_Deliverd, User_Interactions_Message_Seen}

# User_Interactions_Search class attributes and methods

# GUI_GUI class attributes and methods

# Back_End_API_PaymentMethod class attributes and methods

# Back_End_API_PayPal class attributes and methods

# Back_End_API_CreditCard class attributes and methods

# System_Controller_User_Controller class attributes and methods

# System_Controller_System_Controller class attributes and methods
System_Controller_System_Controller_GiveResponse: Property = Property(name="GiveResponse", type=BooleanType)
System_Controller_System_Controller_Database_Connection: Property = Property(name="Database_Connection", type=BooleanType)
System_Controller_System_Controller.attributes={System_Controller_System_Controller_Database_Connection, System_Controller_System_Controller_GiveResponse}

# System_Control class attributes and methods

# Normal_User class attributes and methods

# Premuim_User class attributes and methods

# Post2 class attributes and methods

# Listeener class attributes and methods

# List_User__Interface class attributes and methods

# User1 class attributes and methods
User1_UserID: Property = Property(name="UserID", type=IntegerType)
User1_Full_Name: Property = Property(name="Full_Name", type=StringType)
User1_username: Property = Property(name="username", type=StringType)
User1_email: Property = Property(name="email", type=StringType)
User1_Gender: Property = Property(name="Gender", type=StringType)
User1_password: Property = Property(name="password", type=StringType)
User1_Age: Property = Property(name="Age", type=IntegerType)
User1_pages: Property = Property(name="pages", type=StringType)
User1_groups: Property = Property(name="groups", type=StringType)
User1_Messages: Property = Property(name="Messages", type=StringType)
User1_Friends: Property = Property(name="Friends", type=List_User__Interface)
User1_FriendRequests: Property = Property(name="FriendRequests", type=StringType)
User1_Privacy: Property = Property(name="Privacy", type=StringType)
User1.attributes={User1_Messages, User1_password, User1_Age, User1_Privacy, User1_groups, User1_UserID, User1_email, User1_username, User1_Gender, User1_pages, User1_Friends, User1_Full_Name, User1_FriendRequests}

# Normal_User1 class attributes and methods

# Premium_User class attributes and methods

# User_Controller class attributes and methods

# System_Controller class attributes and methods
System_Controller_GiveResponse: Property = Property(name="GiveResponse", type=BooleanType)
System_Controller_Database_Connection: Property = Property(name="Database_Connection", type=BooleanType)
System_Controller.attributes={System_Controller_Database_Connection, System_Controller_GiveResponse}

# Page1 class attributes and methods
Page1_name: Property = Property(name="name", type=StringType)
Page1_admin: Property = Property(name="admin", type=User)
Page1_fans: Property = Property(name="fans", type=User__)
Page1_description: Property = Property(name="description", type=StringType)
Page1_posts: Property = Property(name="posts", type=StringType)
Page1_nFans: Property = Property(name="nFans", type=IntegerType)
Page1.attributes={Page1_nFans, Page1_admin, Page1_posts, Page1_fans, Page1_description, Page1_name}

# Message class attributes and methods
Message_SenderID: Property = Property(name="SenderID", type=IntegerType)
Message_MessageContent: Property = Property(name="MessageContent", type=StringType)
Message_Time: Property = Property(name="Time", type=IntegerType)
Message_ReceiverID: Property = Property(name="ReceiverID", type=IntegerType)
Message_Seen: Property = Property(name="Seen", type=BooleanType)
Message_Deliverd: Property = Property(name="Deliverd", type=BooleanType)
Message.attributes={Message_MessageContent, Message_ReceiverID, Message_SenderID, Message_Time, Message_Seen, Message_Deliverd}

# Search class attributes and methods

# Group1 class attributes and methods
Group1_name: Property = Property(name="name", type=StringType)
Group1_description: Property = Property(name="description", type=StringType)
Group1_admins: Property = Property(name="admins", type=User__)
Group1_members: Property = Property(name="members", type=User__)
Group1_nMembers: Property = Property(name="nMembers", type=IntegerType)
Group1_posts: Property = Property(name="posts", type=StringType)
Group1.attributes={Group1_nMembers, Group1_members, Group1_description, Group1_admins, Group1_posts, Group1_name}

# Post1 class attributes and methods
Post1_CommentContainer: Property = Property(name="CommentContainer", type=StringType)
Post1_privateMode: Property = Property(name="privateMode", type=BooleanType)
Post1_nLikes: Property = Property(name="nLikes", type=IntegerType)
Post1_nComments: Property = Property(name="nComments", type=IntegerType)
Post1_nShares: Property = Property(name="nShares", type=IntegerType)
Post1_owner: Property = Property(name="owner", type=User)
Post1_LikeContainer_int_: Property = Property(name="LikeContainer_int_", type=StringType)
Post1.attributes={Post1_nShares, Post1_nComments, Post1_owner, Post1_privateMode, Post1_CommentContainer, Post1_LikeContainer_int_, Post1_nLikes}

# HashTags1 class attributes and methods
HashTags1_allHashTags: Property = Property(name="allHashTags", type=StringType)
HashTags1.attributes={HashTags1_allHashTags}

# PaymentMethod class attributes and methods

# PayPal class attributes and methods

# CreditCard class attributes and methods

# GUI class attributes and methods

# Relationships
User_Group2: BinaryAssociation = BinaryAssociation(
    name="User_Group2",
    ends={
        Property(name="group0", type=Group, multiplicity=Multiplicity(1, 1)),
        Property(name="user1", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
User_Page: BinaryAssociation = BinaryAssociation(
    name="User_Page",
    ends={
        Property(name="page2", type=Page, multiplicity=Multiplicity(1, 1)),
        Property(name="user3", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="post4", type=Post, multiplicity=Multiplicity(1, 1)),
        Property(name="user5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Post_Group: BinaryAssociation = BinaryAssociation(
    name="Post_Group",
    ends={
        Property(name="group6", type=Group, multiplicity=Multiplicity(0, 1)),
        Property(name="post7", type=Post, multiplicity=Multiplicity(0, 1))
    }
)
Post_HashTags: BinaryAssociation = BinaryAssociation(
    name="Post_HashTags",
    ends={
        Property(name="hashTags8", type=HashTags, multiplicity=Multiplicity(0, 1)),
        Property(name="post9", type=Post, multiplicity=Multiplicity(0, 1))
    }
)
Post_Page: BinaryAssociation = BinaryAssociation(
    name="Post_Page",
    ends={
        Property(name="page10", type=Page, multiplicity=Multiplicity(0, 1)),
        Property(name="post11", type=Post, multiplicity=Multiplicity(0, 1))
    }
)
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="group12", type=User_Interactions_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="user13", type=Users_User, multiplicity=Multiplicity(0, 9999))
    }
)
User_Post1: BinaryAssociation = BinaryAssociation(
    name="User_Post1",
    ends={
        Property(name="post14", type=User_Interactions_Post, multiplicity=Multiplicity(1, 9999)),
        Property(name="user15", type=Users_User, multiplicity=Multiplicity(1, 1))
    }
)
User_Page1: BinaryAssociation = BinaryAssociation(
    name="User_Page1",
    ends={
        Property(name="page16", type=User_Interactions_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="user17", type=Users_User, multiplicity=Multiplicity(0, 9999))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message18", type=User_Interactions_Message, multiplicity=Multiplicity(0, 1)),
        Property(name="user19", type=Users_User, multiplicity=Multiplicity(0, 1))
    }
)
Post_HashTags1: BinaryAssociation = BinaryAssociation(
    name="Post_HashTags1",
    ends={
        Property(name="hashTags20", type=User_Interactions_HashTags, multiplicity=Multiplicity(0, 1)),
        Property(name="post21", type=User_Interactions_Post, multiplicity=Multiplicity(0, 1))
    }
)
Group_Post: BinaryAssociation = BinaryAssociation(
    name="Group_Post",
    ends={
        Property(name="post22", type=User_Interactions_Post, multiplicity=Multiplicity(1, 1)),
        Property(name="group23", type=User_Interactions_Group, multiplicity=Multiplicity(1, 1))
    }
)
Page_Post: BinaryAssociation = BinaryAssociation(
    name="Page_Post",
    ends={
        Property(name="post24", type=User_Interactions_Post, multiplicity=Multiplicity(1, 1)),
        Property(name="page25", type=User_Interactions_Page, multiplicity=Multiplicity(1, 1))
    }
)
Search_User: BinaryAssociation = BinaryAssociation(
    name="Search_User",
    ends={
        Property(name="user26", type=Users_User, multiplicity=Multiplicity(0, 1)),
        Property(name="search27", type=User_Interactions_Search, multiplicity=Multiplicity(0, 1))
    }
)
PaymentMethod_Premium_User: BinaryAssociation = BinaryAssociation(
    name="PaymentMethod_Premium_User",
    ends={
        Property(name="premium_User28", type=Users_Premium_User, multiplicity=Multiplicity(0, 1)),
        Property(name="paymentMethod29", type=Back_End_API_PaymentMethod, multiplicity=Multiplicity(0, 1))
    }
)
User_Controller_User: BinaryAssociation = BinaryAssociation(
    name="User_Controller_User",
    ends={
        Property(name="user30", type=User1, multiplicity=Multiplicity(1, 1)),
        Property(name="user_Controller31", type=User_Controller, multiplicity=Multiplicity(1, 1))
    }
)
PaymentMethod_User: BinaryAssociation = BinaryAssociation(
    name="PaymentMethod_User",
    ends={
        Property(name="user32", type=User1, multiplicity=Multiplicity(1, 1)),
        Property(name="paymentMethod33", type=PaymentMethod, multiplicity=Multiplicity(1, 1))
    }
)
Post_System_Controller: BinaryAssociation = BinaryAssociation(
    name="Post_System_Controller",
    ends={
        Property(name="system_Controller34", type=System_Controller, multiplicity=Multiplicity(0, 1)),
        Property(name="post35", type=Post1, multiplicity=Multiplicity(0, 1))
    }
)
Group_System_Controller: BinaryAssociation = BinaryAssociation(
    name="Group_System_Controller",
    ends={
        Property(name="system_Controller36", type=System_Controller, multiplicity=Multiplicity(0, 1)),
        Property(name="group37", type=Group1, multiplicity=Multiplicity(0, 1))
    }
)
Search_System_Controller: BinaryAssociation = BinaryAssociation(
    name="Search_System_Controller",
    ends={
        Property(name="system_Controller38", type=System_Controller, multiplicity=Multiplicity(0, 1)),
        Property(name="search39", type=Search, multiplicity=Multiplicity(0, 1))
    }
)
Message_System_Controller: BinaryAssociation = BinaryAssociation(
    name="Message_System_Controller",
    ends={
        Property(name="system_Controller40", type=System_Controller, multiplicity=Multiplicity(0, 1)),
        Property(name="message41", type=Message, multiplicity=Multiplicity(0, 1))
    }
)
Page_System_Controller: BinaryAssociation = BinaryAssociation(
    name="Page_System_Controller",
    ends={
        Property(name="system_Controller42", type=System_Controller, multiplicity=Multiplicity(0, 1)),
        Property(name="page43", type=Page1, multiplicity=Multiplicity(0, 1))
    }
)
HashTags_Post: BinaryAssociation = BinaryAssociation(
    name="HashTags_Post",
    ends={
        Property(name="post44", type=Post1, multiplicity=Multiplicity(1, 1)),
        Property(name="hashTags45", type=HashTags1, multiplicity=Multiplicity(0, 9999))
    }
)
User_Controller_System_Controller: BinaryAssociation = BinaryAssociation(
    name="User_Controller_System_Controller",
    ends={
        Property(name="system_Controller46", type=System_Controller, multiplicity=Multiplicity(0, 1)),
        Property(name="user_Controller47", type=User_Controller, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_l4uH4BkLEeqDmNBP3mfLQg",
    types={User, Group, User__, Post, Page, HashTags, User2_Interface, Users_User, Users_Normal_User, Users_Premium_User, User_Interactions_Page, User_Interactions_Group, User_Interactions_Post, User_Interactions_HashTags, User_Interactions_Message, User_Interactions_Search, GUI_GUI, Back_End_API_PaymentMethod, Back_End_API_PayPal, Back_End_API_CreditCard, System_Controller_User_Controller, System_Controller_System_Controller, System_Control, Normal_User, Premuim_User, Post2, Listeener, List_User__Interface, User1, Normal_User1, Premium_User, User_Controller, System_Controller, Page1, Message, Search, Group1, Post1, HashTags1, PaymentMethod, PayPal, CreditCard, GUI},
    associations={User_Group2, User_Page, User_Post, Post_Group, Post_HashTags, Post_Page, User_Group, User_Post1, User_Page1, User_Message, Post_HashTags1, Group_Post, Page_Post, Search_User, PaymentMethod_Premium_User, User_Controller_User, PaymentMethod_User, Post_System_Controller, Group_System_Controller, Search_System_Controller, Message_System_Controller, Page_System_Controller, HashTags_Post, User_Controller_System_Controller},
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