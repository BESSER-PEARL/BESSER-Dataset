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
BaseEntity = Class(name="BaseEntity")
User = Class(name="User")
Order = Class(name="Order")
Item = Class(name="Item")
Category = Class(name="Category")
CouponCode = Class(name="CouponCode")
FavoriteItem = Class(name="FavoriteItem")
OrderItem = Class(name="OrderItem")
SubCategory = Class(name="SubCategory")

# BaseEntity class attributes and methods
BaseEntity_Id: Property = Property(name="Id", type=StringType)
BaseEntity_Active: Property = Property(name="Active", type=BooleanType)
BaseEntity_CreatedBy: Property = Property(name="CreatedBy", type=StringType)
BaseEntity_CreatedDate: Property = Property(name="CreatedDate", type=StringType)
BaseEntity_UpdatedBy: Property = Property(name="UpdatedBy", type=StringType)
BaseEntity_UpdatedDate: Property = Property(name="UpdatedDate", type=StringType)
BaseEntity.attributes={BaseEntity_CreatedDate, BaseEntity_Id, BaseEntity_UpdatedBy, BaseEntity_UpdatedDate, BaseEntity_Active, BaseEntity_CreatedBy}

# User class attributes and methods
User_Login: Property = Property(name="Login", type=StringType)
User_Password: Property = Property(name="Password", type=StringType)
User_Email: Property = Property(name="Email", type=StringType)
User_FirstName: Property = Property(name="FirstName", type=StringType)
User_LastName: Property = Property(name="LastName", type=StringType)
User_Role: Property = Property(name="Role", type=IntegerType)
User_PhoneNumber: Property = Property(name="PhoneNumber", type=StringType)
User.attributes={User_Email, User_Role, User_PhoneNumber, User_Login, User_Password, User_LastName, User_FirstName}

# Order class attributes and methods
Order_Name: Property = Property(name="Name", type=StringType)
Order_PhoneNumber: Property = Property(name="PhoneNumber", type=StringType)
Order_Email: Property = Property(name="Email", type=StringType)
Order_Comment: Property = Property(name="Comment", type=StringType)
Order_Address: Property = Property(name="Address", type=StringType)
Order_TotalPrice: Property = Property(name="TotalPrice", type=StringType)
Order_Status: Property = Property(name="Status", type=IntegerType)
Order_CodeId: Property = Property(name="CodeId", type=StringType)
Order_UserId: Property = Property(name="UserId", type=StringType)
Order.attributes={Order_CodeId, Order_TotalPrice, Order_Name, Order_PhoneNumber, Order_Email, Order_Address, Order_Status, Order_UserId, Order_Comment}

# Item class attributes and methods
Item_Name: Property = Property(name="Name", type=StringType)
Item_Description: Property = Property(name="Description", type=StringType)
Item_Color: Property = Property(name="Color", type=StringType)
Item_Brand: Property = Property(name="Brand", type=StringType)
Item_Discount: Property = Property(name="Discount", type=StringType)
Item_Price: Property = Property(name="Price", type=StringType)
Item_PreviewImagePath: Property = Property(name="PreviewImagePath", type=StringType)
Item_MinPreviewImagePath: Property = Property(name="MinPreviewImagePath", type=StringType)
Item_ImagePath1: Property = Property(name="ImagePath1", type=StringType)
Item_ImagePath2: Property = Property(name="ImagePath2", type=StringType)
Item_ImagePath3: Property = Property(name="ImagePath3", type=StringType)
Item_Status: Property = Property(name="Status", type=IntegerType)
Item_Size: Property = Property(name="Size", type=StringType)
Item_Amount: Property = Property(name="Amount", type=IntegerType)
Item_Sex: Property = Property(name="Sex", type=IntegerType)
Item_CategoryId: Property = Property(name="CategoryId", type=StringType)
Item_SubCategoryId: Property = Property(name="SubCategoryId", type=StringType)
Item.attributes={Item_ImagePath3, Item_Status, Item_MinPreviewImagePath, Item_PreviewImagePath, Item_Sex, Item_Name, Item_Color, Item_Brand, Item_ImagePath1, Item_CategoryId, Item_SubCategoryId, Item_Amount, Item_Discount, Item_ImagePath2, Item_Price, Item_Description, Item_Size}

# Category class attributes and methods
Category_Name: Property = Property(name="Name", type=StringType)
Category_RusName: Property = Property(name="RusName", type=StringType)
Category.attributes={Category_Name, Category_RusName}

# CouponCode class attributes and methods
CouponCode_ExpiryDate: Property = Property(name="ExpiryDate", type=StringType)
CouponCode_Code: Property = Property(name="Code", type=StringType)
CouponCode_Discount: Property = Property(name="Discount", type=IntegerType)
CouponCode_UserId: Property = Property(name="UserId", type=StringType)
CouponCode.attributes={CouponCode_UserId, CouponCode_Discount, CouponCode_Code, CouponCode_ExpiryDate}

# FavoriteItem class attributes and methods
FavoriteItem_UserId: Property = Property(name="UserId", type=StringType)
FavoriteItem_ItemId: Property = Property(name="ItemId", type=StringType)
FavoriteItem.attributes={FavoriteItem_UserId, FavoriteItem_ItemId}

# OrderItem class attributes and methods
OrderItem_Name: Property = Property(name="Name", type=StringType)
OrderItem_Price: Property = Property(name="Price", type=StringType)
OrderItem_Amount: Property = Property(name="Amount", type=IntegerType)
OrderItem_ItemId: Property = Property(name="ItemId", type=StringType)
OrderItem_OrderId: Property = Property(name="OrderId", type=StringType)
OrderItem.attributes={OrderItem_Price, OrderItem_ItemId, OrderItem_Amount, OrderItem_Name, OrderItem_OrderId}

# SubCategory class attributes and methods
SubCategory_Name: Property = Property(name="Name", type=StringType)
SubCategory_RusName: Property = Property(name="RusName", type=StringType)
SubCategory_CategoryId: Property = Property(name="CategoryId", type=StringType)
SubCategory.attributes={SubCategory_Name, SubCategory_RusName, SubCategory_CategoryId}

# Relationships
Item_FavoriteItem: BinaryAssociation = BinaryAssociation(
    name="Item_FavoriteItem",
    ends={
        Property(name="favoriteItem0", type=FavoriteItem, multiplicity=Multiplicity(0, 1)),
        Property(name="item1", type=Item, multiplicity=Multiplicity(0, 1))
    }
)
FavoriteItem_User: BinaryAssociation = BinaryAssociation(
    name="FavoriteItem_User",
    ends={
        Property(name="user2", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="favoriteItem3", type=FavoriteItem, multiplicity=Multiplicity(0, 1))
    }
)
Order_CouponCode: BinaryAssociation = BinaryAssociation(
    name="Order_CouponCode",
    ends={
        Property(name="couponCode4", type=CouponCode, multiplicity=Multiplicity(0, 1)),
        Property(name="order5", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
CouponCode_User: BinaryAssociation = BinaryAssociation(
    name="CouponCode_User",
    ends={
        Property(name="user6", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="couponCode7", type=CouponCode, multiplicity=Multiplicity(0, 1))
    }
)
OrderItem_Order: BinaryAssociation = BinaryAssociation(
    name="OrderItem_Order",
    ends={
        Property(name="order8", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="orderItem9", type=OrderItem, multiplicity=Multiplicity(0, 1))
    }
)
SubCategory_Category: BinaryAssociation = BinaryAssociation(
    name="SubCategory_Category",
    ends={
        Property(name="category10", type=Category, multiplicity=Multiplicity(0, 1)),
        Property(name="subCategory11", type=SubCategory, multiplicity=Multiplicity(0, 1))
    }
)
SubCategory_Item: BinaryAssociation = BinaryAssociation(
    name="SubCategory_Item",
    ends={
        Property(name="item12", type=Item, multiplicity=Multiplicity(0, 1)),
        Property(name="subCategory13", type=SubCategory, multiplicity=Multiplicity(0, 1))
    }
)
Category_Item: BinaryAssociation = BinaryAssociation(
    name="Category_Item",
    ends={
        Property(name="item14", type=Item, multiplicity=Multiplicity(0, 1)),
        Property(name="category15", type=Category, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_IyzjEA5pEemlr9XsZWPkQQ",
    types={BaseEntity, User, Order, Item, Category, CouponCode, FavoriteItem, OrderItem, SubCategory},
    associations={Item_FavoriteItem, FavoriteItem_User, Order_CouponCode, CouponCode_User, OrderItem_Order, SubCategory_Category, SubCategory_Item, Category_Item},
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