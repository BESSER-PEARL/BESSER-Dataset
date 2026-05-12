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
UserState: Enumeration = Enumeration(
    name="UserState",
    literals={
            
    }
)

post_status: Enumeration = Enumeration(
    name="post_status",
    literals={
            
    }
)

# Classes
User = Class(name="User")
AddPost = Class(name="AddPost")
Account = Class(name="Account")
WebUser = Class(name="WebUser")
Post = Class(name="Post")
LineItem = Class(name="LineItem")
post = Class(name="post")

# User class attributes and methods
User_Id: Property = Property(name="Id", type=IntegerType)
User_Name: Property = Property(name="Name", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User.attributes={User_Name, User_Id, User_email}

# AddPost class attributes and methods
AddPost_creationDate: Property = Property(name="creationDate", type=DateType)
AddPost.attributes={AddPost_creationDate}

# Account class attributes and methods
Account_Name: Property = Property(name="Name", type=StringType)
Account_created: Property = Property(name="created", type=DateType)
Account_closed: Property = Property(name="closed", type=DateType)
Account_isClosed: Property = Property(name="isClosed", type=BooleanType)
Account.attributes={Account_created, Account_Name, Account_closed, Account_isClosed}

# WebUser class attributes and methods
WebUser_login: Property = Property(name="login", type=StringType)
WebUser_password: Property = Property(name="password", type=StringType)
WebUser_state: Property = Property(name="state", type=UserState)
WebUser.attributes={WebUser_login, WebUser_password, WebUser_state}

# Post class attributes and methods
Post_ID: Property = Property(name="ID", type=IntegerType)
Post_Created: Property = Property(name="Created", type=DateType)
Post_User: Property = Property(name="User", type=StringType)
Post_Category: Property = Property(name="Category", type=StringType)
Post_tags: Property = Property(name="tags", type=FloatType)
Post_status: Property = Property(name="status", type=post_status)
Post.attributes={Post_Created, Post_tags, Post_User, Post_ID, Post_status, Post_Category}

# LineItem class attributes and methods
LineItem_category: Property = Property(name="category", type=IntegerType)
LineItem_tags: Property = Property(name="tags", type=FloatType)
LineItem.attributes={LineItem_tags, LineItem_category}

# post class attributes and methods
post_ID: Property = Property(name="ID", type=IntegerType)
post_description: Property = Property(name="description", type=StringType)
post.attributes={post_ID, post_description}

# Relationships
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="additionals12", type=LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="order13", type=Post, multiplicity=Multiplicity(0, 1))
    }
)
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart0", type=AddPost, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser1", type=WebUser, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="customer2", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser3", type=WebUser, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart6", type=AddPost, multiplicity=Multiplicity(1, 1)),
        Property(name="account7", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items8", type=LineItem, multiplicity=Multiplicity(1, 1)),
        Property(name="sc9", type=AddPost, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="lineItems10", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="Post11", type=post, multiplicity=Multiplicity(1, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order14", type=Post, multiplicity=Multiplicity(0, 9999)),
        Property(name="account15", type=Account, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_283c71fd_f80f_4c20_b595_b6747fa192ba",
    types={User, AddPost, Account, WebUser, Post, LineItem, post, UserState, post_status},
    associations={Order_LineItem, WebUser_ShoppingCart, WebUser_Customer, Customer_Account, Account_ShoppingCart, ShoppingCart_LineItem, Product_LineItem, Account_Order},
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