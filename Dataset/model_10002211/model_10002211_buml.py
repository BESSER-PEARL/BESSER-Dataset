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
Category = Class(name="Category")
OnlineShop = Class(name="OnlineShop")
Order = Class(name="Order")
Product = Class(name="Product")
User = Class(name="User")
Role = Class(name="Role")
BaseDateInformation = Class(name="BaseDateInformation")
FlashSale = Class(name="FlashSale")
Customer = Class(name="Customer")

# Category class attributes and methods
Category_CategoryID: Property = Property(name="CategoryID", type=IntegerType)
Category_CategoryName: Property = Property(name="CategoryName", type=StringType)
Category_Description: Property = Property(name="Description", type=StringType)
Category_isActive: Property = Property(name="isActive", type=BooleanType)
Category.attributes={Category_Description, Category_CategoryName, Category_isActive, Category_CategoryID}

# OnlineShop class attributes and methods
OnlineShop_OnlineShopID: Property = Property(name="OnlineShopID", type=IntegerType)
OnlineShop_OnlineShopName: Property = Property(name="OnlineShopName", type=StringType)
OnlineShop_ShopCategoryID: Property = Property(name="ShopCategoryID", type=IntegerType)
OnlineShop_isActive: Property = Property(name="isActive", type=BooleanType)
OnlineShop.attributes={OnlineShop_OnlineShopName, OnlineShop_isActive, OnlineShop_OnlineShopID, OnlineShop_ShopCategoryID}

# Order class attributes and methods
Order_OrderID: Property = Property(name="OrderID", type=IntegerType)
Order_ShopOnlineID: Property = Property(name="ShopOnlineID", type=IntegerType)
Order_OrderDate: Property = Property(name="OrderDate", type=StringType)
Order_Status: Property = Property(name="Status", type=BooleanType)
Order_TotalPrice: Property = Property(name="TotalPrice", type=StringType)
Order_TotalDiscount: Property = Property(name="TotalDiscount", type=StringType)
Order_OrderCustomerID: Property = Property(name="OrderCustomerID", type=IntegerType)
Order_ReceiveCustomerID: Property = Property(name="ReceiveCustomerID", type=IntegerType)
Order_UserID: Property = Property(name="UserID", type=IntegerType)
Order.attributes={Order_TotalDiscount, Order_TotalPrice, Order_UserID, Order_ShopOnlineID, Order_ReceiveCustomerID, Order_OrderID, Order_OrderDate, Order_Status, Order_OrderCustomerID}

# Product class attributes and methods
Product_ProductID: Property = Property(name="ProductID", type=IntegerType)
Product_ProductName: Property = Property(name="ProductName", type=StringType)
Product_OnlineShopID: Property = Property(name="OnlineShopID", type=IntegerType)
Product_CategoryID: Property = Property(name="CategoryID", type=IntegerType)
Product_Description: Property = Property(name="Description", type=StringType)
Product_Price: Property = Property(name="Price", type=StringType)
Product_Image: Property = Property(name="Image", type=StringType)
Product_isActive: Property = Property(name="isActive", type=BooleanType)
Product.attributes={Product_OnlineShopID, Product_Description, Product_Price, Product_isActive, Product_ProductName, Product_Image, Product_CategoryID, Product_ProductID}

# User class attributes and methods
User_UserID: Property = Property(name="UserID", type=StringType)
User_Username: Property = Property(name="Username", type=StringType)
User_RoleID: Property = Property(name="RoleID", type=IntegerType)
User_Password: Property = Property(name="Password", type=StringType)
User_RegisterDate: Property = Property(name="RegisterDate", type=StringType)
User_isActive: Property = Property(name="isActive", type=BooleanType)
User.attributes={User_UserID, User_Username, User_isActive, User_RoleID, User_Password, User_RegisterDate}

# Role class attributes and methods
Role_RoleID: Property = Property(name="RoleID", type=IntegerType)
Role_RoleName: Property = Property(name="RoleName", type=StringType)
Role_Description: Property = Property(name="Description", type=StringType)
Role_isActive: Property = Property(name="isActive", type=BooleanType)
Role.attributes={Role_isActive, Role_RoleName, Role_Description, Role_RoleID}

# BaseDateInformation class attributes and methods
BaseDateInformation_CreatedBy: Property = Property(name="CreatedBy", type=StringType)
BaseDateInformation_CreateDate: Property = Property(name="CreateDate", type=StringType)
BaseDateInformation_LastModifedBy: Property = Property(name="LastModifedBy", type=StringType)
BaseDateInformation_LastModifedDate: Property = Property(name="LastModifedDate", type=StringType)
BaseDateInformation.attributes={BaseDateInformation_LastModifedBy, BaseDateInformation_LastModifedDate, BaseDateInformation_CreateDate, BaseDateInformation_CreatedBy}

# FlashSale class attributes and methods
FlashSale_FlashSaleID: Property = Property(name="FlashSaleID", type=IntegerType)
FlashSale_FlashSaleName: Property = Property(name="FlashSaleName", type=StringType)
FlashSale_OnlineShopID: Property = Property(name="OnlineShopID", type=IntegerType)
FlashSale_DiscountPercent: Property = Property(name="DiscountPercent", type=IntegerType)
FlashSale_DiscountAmount: Property = Property(name="DiscountAmount", type=IntegerType)
FlashSale_Description: Property = Property(name="Description", type=StringType)
FlashSale.attributes={FlashSale_FlashSaleID, FlashSale_DiscountPercent, FlashSale_DiscountAmount, FlashSale_Description, FlashSale_OnlineShopID, FlashSale_FlashSaleName}

# Customer class attributes and methods
Customer_CustomerID: Property = Property(name="CustomerID", type=IntegerType)
Customer_CustomerName: Property = Property(name="CustomerName", type=StringType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer_Phone: Property = Property(name="Phone", type=StringType)
Customer_Email: Property = Property(name="Email", type=StringType)
Customer_Gender: Property = Property(name="Gender", type=IntegerType)
Customer.attributes={Customer_CustomerName, Customer_CustomerID, Customer_Gender, Customer_Phone, Customer_Address, Customer_Email}

# Relationships
Category_Product: BinaryAssociation = BinaryAssociation(
    name="Category_Product",
    ends={
        Property(name="product0", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="category1", type=Category, multiplicity=Multiplicity(1, 1))
    }
)
Product_OnlineShop: BinaryAssociation = BinaryAssociation(
    name="Product_OnlineShop",
    ends={
        Property(name="onlineShop8", type=OnlineShop, multiplicity=Multiplicity(0, 1)),
        Property(name="product9", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
BaseDateInformation_Product: BinaryAssociation = BinaryAssociation(
    name="BaseDateInformation_Product",
    ends={
        Property(name="product10", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="baseDateInformation11", type=BaseDateInformation, multiplicity=Multiplicity(0, 1))
    }
)
User_Role: BinaryAssociation = BinaryAssociation(
    name="User_Role",
    ends={
        Property(name="role12", type=Role, multiplicity=Multiplicity(0, 1)),
        Property(name="user13", type=User, multiplicity=Multiplicity(0, 1))
    }
)
OnlineShop_User: BinaryAssociation = BinaryAssociation(
    name="OnlineShop_User",
    ends={
        Property(name="user14", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="onlineShop15", type=OnlineShop, multiplicity=Multiplicity(0, 1))
    }
)
BaseDateInformation_FlashSale: BinaryAssociation = BinaryAssociation(
    name="BaseDateInformation_FlashSale",
    ends={
        Property(name="flashSale16", type=FlashSale, multiplicity=Multiplicity(0, 1)),
        Property(name="baseDateInformation17", type=BaseDateInformation, multiplicity=Multiplicity(0, 1))
    }
)
OnlineShop_FlashSale: BinaryAssociation = BinaryAssociation(
    name="OnlineShop_FlashSale",
    ends={
        Property(name="flashSale18", type=FlashSale, multiplicity=Multiplicity(0, 1)),
        Property(name="onlineShop19", type=OnlineShop, multiplicity=Multiplicity(0, 1))
    }
)
OnlineShop_Order: BinaryAssociation = BinaryAssociation(
    name="OnlineShop_Order",
    ends={
        Property(name="order20", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="onlineShop21", type=OnlineShop, multiplicity=Multiplicity(0, 1))
    }
)
BaseDateInformation_OnlineShop: BinaryAssociation = BinaryAssociation(
    name="BaseDateInformation_OnlineShop",
    ends={
        Property(name="onlineShop22", type=OnlineShop, multiplicity=Multiplicity(0, 1)),
        Property(name="baseDateInformation23", type=BaseDateInformation, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order2", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Category_OnlineShop: BinaryAssociation = BinaryAssociation(
    name="Category_OnlineShop",
    ends={
        Property(name="onlineShop4", type=OnlineShop, multiplicity=Multiplicity(0, 1)),
        Property(name="category5", type=Category, multiplicity=Multiplicity(0, 1))
    }
)
BaseDateInformation_Category: BinaryAssociation = BinaryAssociation(
    name="BaseDateInformation_Category",
    ends={
        Property(name="category6", type=Category, multiplicity=Multiplicity(0, 1)),
        Property(name="baseDateInformation7", type=BaseDateInformation, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_wrUNEJ_QEemWLqKkNNGPFg",
    types={Category, OnlineShop, Order, Product, User, Role, BaseDateInformation, FlashSale, Customer},
    associations={Category_Product, Product_OnlineShop, BaseDateInformation_Product, User_Role, OnlineShop_User, BaseDateInformation_FlashSale, OnlineShop_FlashSale, OnlineShop_Order, BaseDateInformation_OnlineShop, Customer_Order, Category_OnlineShop, BaseDateInformation_Category},
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