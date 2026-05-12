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
User_Account = Class(name="User_Account")
UserName = Class(name="UserName")
Premium_Members = Class(name="Premium_Members")
Regular_Members = Class(name="Regular_Members")
ShoppingCart = Class(name="ShoppingCart")
OrderProcess = Class(name="OrderProcess")
Product = Class(name="Product")
Promos = Class(name="Promos")
UserAddress = Class(name="UserAddress")
Vendor = Class(name="Vendor")

# User_Account class attributes and methods
User_Account_UserID: Property = Property(name="UserID", type=StringType)
User_Account_FullName: Property = Property(name="FullName", type=StringType)
User_Account_Email: Property = Property(name="Email", type=StringType)
User_Account_DateOfBirth: Property = Property(name="DateOfBirth", type=StringType)
User_Account_RegDate: Property = Property(name="RegDate", type=StringType)
User_Account_UserAddress: Property = Property(name="UserAddress", type=StringType)
User_Account.attributes={User_Account_DateOfBirth, User_Account_UserID, User_Account_RegDate, User_Account_UserAddress, User_Account_FullName, User_Account_Email}

# UserName class attributes and methods
UserName_FirstName: Property = Property(name="FirstName", type=StringType)
UserName_LastName: Property = Property(name="LastName", type=StringType)
UserName.attributes={UserName_FirstName, UserName_LastName}

# Premium_Members class attributes and methods
Premium_Members_MembershipStartDate: Property = Property(name="MembershipStartDate", type=StringType)
Premium_Members_MembershipEndDate: Property = Property(name="MembershipEndDate", type=StringType)
Premium_Members_PromoCode: Property = Property(name="PromoCode", type=StringType)
Premium_Members.attributes={Premium_Members_PromoCode, Premium_Members_MembershipEndDate, Premium_Members_MembershipStartDate}

# Regular_Members class attributes and methods
Regular_Members_TriedPremium: Property = Property(name="TriedPremium", type=IntegerType)
Regular_Members_TrialStartDate: Property = Property(name="TrialStartDate", type=StringType)
Regular_Members.attributes={Regular_Members_TriedPremium, Regular_Members_TrialStartDate}

# ShoppingCart class attributes and methods
ShoppingCart_ShoppingCartID: Property = Property(name="ShoppingCartID", type=IntegerType)
ShoppingCart_OrderID: Property = Property(name="OrderID", type=IntegerType)
ShoppingCart_UserID: Property = Property(name="UserID", type=StringType)
ShoppingCart_Total: Property = Property(name="Total", type=StringType)
ShoppingCart_ProductID: Property = Property(name="ProductID", type=IntegerType)
ShoppingCart_Quantity: Property = Property(name="Quantity", type=IntegerType)
ShoppingCart_Promo: Property = Property(name="Promo", type=Promos)
ShoppingCart.attributes={ShoppingCart_UserID, ShoppingCart_OrderID, ShoppingCart_Total, ShoppingCart_ShoppingCartID, ShoppingCart_Promo, ShoppingCart_Quantity, ShoppingCart_ProductID}

# OrderProcess class attributes and methods
OrderProcess_OrderID: Property = Property(name="OrderID", type=IntegerType)
OrderProcess_UserID: Property = Property(name="UserID", type=IntegerType)
OrderProcess_MemberShipPayment: Property = Property(name="MemberShipPayment", type=IntegerType)
OrderProcess_PromoCode: Property = Property(name="PromoCode", type=StringType)
OrderProcess_Total: Property = Property(name="Total", type=StringType)
OrderProcess_IsMember: Property = Property(name="IsMember", type=IntegerType)
OrderProcess_OrderPickUp: Property = Property(name="OrderPickUp", type=IntegerType)
OrderProcess.attributes={OrderProcess_MemberShipPayment, OrderProcess_OrderPickUp, OrderProcess_UserID, OrderProcess_IsMember, OrderProcess_PromoCode, OrderProcess_OrderID, OrderProcess_Total}

# Product class attributes and methods
Product_ProductID: Property = Property(name="ProductID", type=IntegerType)
Product_Description: Property = Property(name="Description", type=StringType)
Product_InventoryQuantity: Property = Property(name="InventoryQuantity", type=IntegerType)
Product_InventoryMinQuantity: Property = Property(name="InventoryMinQuantity", type=IntegerType)
Product_VendorID: Property = Property(name="VendorID", type=IntegerType)
Product.attributes={Product_ProductID, Product_Description, Product_InventoryMinQuantity, Product_InventoryQuantity, Product_VendorID}

# Promos class attributes and methods
Promos_PromoCode: Property = Property(name="PromoCode", type=StringType)
Promos_Name: Property = Property(name="Name", type=StringType)
Promos_Discount: Property = Property(name="Discount", type=StringType)
Promos_StartDate: Property = Property(name="StartDate", type=StringType)
Promos_EndDate: Property = Property(name="EndDate", type=StringType)
Promos.attributes={Promos_Discount, Promos_EndDate, Promos_PromoCode, Promos_StartDate, Promos_Name}

# UserAddress class attributes and methods
UserAddress_City: Property = Property(name="City", type=StringType)
UserAddress_StreetNum: Property = Property(name="StreetNum", type=IntegerType)
UserAddress_StreetName: Property = Property(name="StreetName", type=StringType)
UserAddress_PostCode: Property = Property(name="PostCode", type=StringType)
UserAddress.attributes={UserAddress_StreetName, UserAddress_PostCode, UserAddress_StreetNum, UserAddress_City}

# Vendor class attributes and methods
Vendor_VendorID: Property = Property(name="VendorID", type=IntegerType)
Vendor_Name: Property = Property(name="Name", type=StringType)
Vendor_Address: Property = Property(name="Address", type=StringType)
Vendor_Contact_Number: Property = Property(name="Contact_Number", type=IntegerType)
Vendor_Email: Property = Property(name="Email", type=StringType)
Vendor.attributes={Vendor_VendorID, Vendor_Address, Vendor_Name, Vendor_Contact_Number, Vendor_Email}

# Relationships
Customer_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Customer_ShoppingCart",
    ends={
        Property(name="Customer_ShoppingCart_00", type=UserName, multiplicity=Multiplicity(0, 1)),
        Property(name="Customer_ShoppingCart_11", type=User_Account, multiplicity=Multiplicity(0, 1))
    }
)
ShoppingCart_Order: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Order",
    ends={
        Property(name="ShoppingCart_Order_02", type=OrderProcess, multiplicity=Multiplicity(0, 1)),
        Property(name="ShoppingCart_Order_13", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Order_Regular_Members: BinaryAssociation = BinaryAssociation(
    name="Order_Regular_Members",
    ends={
        Property(name="Order_Regular_Members_04", type=User_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="Order_Regular_Members_15", type=ShoppingCart, multiplicity=Multiplicity(1, 9999))
    }
)
User_Account_OrderProcess: BinaryAssociation = BinaryAssociation(
    name="User_Account_OrderProcess",
    ends={
        Property(name="orderProcess6", type=OrderProcess, multiplicity=Multiplicity(0, 9999)),
        Property(name="user_Account7", type=User_Account, multiplicity=Multiplicity(1, 1))
    }
)
Promos_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Promos_ShoppingCart",
    ends={
        Property(name="shoppingCart8", type=ShoppingCart, multiplicity=Multiplicity(0, 9999)),
        Property(name="promos9", type=Promos, multiplicity=Multiplicity(0, 1))
    }
)
User_Account_UserAddress: BinaryAssociation = BinaryAssociation(
    name="User_Account_UserAddress",
    ends={
        Property(name="userAddress10", type=UserAddress, multiplicity=Multiplicity(0, 1)),
        Property(name="user_Account11", type=User_Account, multiplicity=Multiplicity(0, 1))
    }
)
Premium_Members_Promos: BinaryAssociation = BinaryAssociation(
    name="Premium_Members_Promos",
    ends={
        Property(name="Premium_Members_Promos_012", type=Promos, multiplicity=Multiplicity(0, 1)),
        Property(name="Premium_Members_Promos_113", type=Premium_Members, multiplicity=Multiplicity(1, 1))
    }
)
Product_Vendor: BinaryAssociation = BinaryAssociation(
    name="Product_Vendor",
    ends={
        Property(name="Product_Vendor_014", type=Vendor, multiplicity=Multiplicity(1, 1)),
        Property(name="Product_Vendor_115", type=Product, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9fb1c050_67b9_46aa_81c9_cfeefe6f47e2",
    types={User_Account, UserName, Premium_Members, Regular_Members, ShoppingCart, OrderProcess, Product, Promos, UserAddress, Vendor},
    associations={Customer_ShoppingCart, ShoppingCart_Order, Order_Regular_Members, User_Account_OrderProcess, Promos_ShoppingCart, User_Account_UserAddress, Premium_Members_Promos, Product_Vendor},
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