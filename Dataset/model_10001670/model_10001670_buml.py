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
Customer = Class(name="Customer")
Products = Class(name="Products")
Shopping_Cart = Class(name="Shopping_Cart")
Payment = Class(name="Payment")
Order = Class(name="Order")
Account = Class(name="Account")
Items = Class(name="Items")
Phone_Order = Class(name="Phone_Order")
Corporate_Order = Class(name="Corporate_Order")
Social_Login = Class(name="Social_Login")
Custom_Login = Class(name="Custom_Login")

# Customer class attributes and methods
Customer_Customer_ID: Property = Property(name="Customer_ID", type=StringType)
Customer_Name: Property = Property(name="Name", type=StringType)
Customer.attributes={Customer_Name, Customer_Customer_ID}

# Products class attributes and methods
Products_SKU_Code: Property = Property(name="SKU_Code", type=StringType)
Products_Product_Name: Property = Property(name="Product_Name", type=StringType)
Products.attributes={Products_SKU_Code, Products_Product_Name}

# Shopping_Cart class attributes and methods
Shopping_Cart_Date: Property = Property(name="Date", type=StringType)
Shopping_Cart.attributes={Shopping_Cart_Date}

# Payment class attributes and methods
Payment_Payment_ID: Property = Property(name="Payment_ID", type=StringType)
Payment_Date: Property = Property(name="Date", type=IntegerType)
Payment.attributes={Payment_Payment_ID, Payment_Date}

# Order class attributes and methods
Order_Order_ID: Property = Property(name="Order_ID", type=StringType)
Order_ReceipientName: Property = Property(name="ReceipientName", type=StringType)
Order_ReceipientAddress: Property = Property(name="ReceipientAddress", type=StringType)
Order_ReceipientContactNo: Property = Property(name="ReceipientContactNo", type=StringType)
Order_ReceipientEmail: Property = Property(name="ReceipientEmail", type=StringType)
Order_GiftMessage: Property = Property(name="GiftMessage", type=StringType)
Order.attributes={Order_ReceipientAddress, Order_GiftMessage, Order_ReceipientEmail, Order_ReceipientContactNo, Order_ReceipientName, Order_Order_ID}

# Account class attributes and methods
Account_Address: Property = Property(name="Address", type=StringType)
Account_ContactNo: Property = Property(name="ContactNo", type=StringType)
Account_Email: Property = Property(name="Email", type=StringType)
Account.attributes={Account_Email, Account_Address, Account_ContactNo}

# Items class attributes and methods
Items_SKUCode: Property = Property(name="SKUCode", type=StringType)
Items_Quantity: Property = Property(name="Quantity", type=StringType)
Items.attributes={Items_SKUCode, Items_Quantity}

# Phone_Order class attributes and methods
Phone_Order_Date: Property = Property(name="Date", type=StringType)
Phone_Order.attributes={Phone_Order_Date}

# Corporate_Order class attributes and methods
Corporate_Order_Date: Property = Property(name="Date", type=StringType)
Corporate_Order.attributes={Corporate_Order_Date}

# Social_Login class attributes and methods
Social_Login_email: Property = Property(name="email", type=StringType)
Social_Login_password: Property = Property(name="password", type=StringType)
Social_Login.attributes={Social_Login_email, Social_Login_password}

# Custom_Login class attributes and methods
Custom_Login_Login: Property = Property(name="Login", type=StringType)
Custom_Login_Password: Property = Property(name="Password", type=StringType)
Custom_Login.attributes={Custom_Login_Login, Custom_Login_Password}

# Relationships
Customer_Products: BinaryAssociation = BinaryAssociation(
    name="Customer_Products",
    ends={
        Property(name="Customer_Products_00", type=Products, multiplicity=Multiplicity(1, 9999)),
        Property(name="Customer_Products_11", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="Customer_Order_02", type=Order, multiplicity=Multiplicity(1, 9999)),
        Property(name="Customer_Order_13", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Shopping_Cart",
    ends={
        Property(name="Customer_Shopping_Cart_04", type=Shopping_Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="Customer_Shopping_Cart_15", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Payment",
    ends={
        Property(name="Customer_Payment_06", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="Customer_Payment_17", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Account_Customer: BinaryAssociation = BinaryAssociation(
    name="Account_Customer",
    ends={
        Property(name="customer8", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="account9", type=Account, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="Customer_Account_010", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="Customer_Account_111", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Payment__Order: BinaryAssociation = BinaryAssociation(
    name="Payment__Order",
    ends={
        Property(name="Payment__Order_012", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="Payment__Order_113", type=Payment, multiplicity=Multiplicity(1, 1))
    }
)
Shopping_Cart_Items: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Items",
    ends={
        Property(name="Shopping_Cart_Items_014", type=Items, multiplicity=Multiplicity(1, 9999)),
        Property(name="Shopping_Cart_Items_115", type=Shopping_Cart, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Account: BinaryAssociation = BinaryAssociation(
    name="Order_Account",
    ends={
        Property(name="account16", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="order17", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_Account2: BinaryAssociation = BinaryAssociation(
    name="Order_Account2",
    ends={
        Property(name="account18", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="order19", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="Account_Order_020", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="Account_Order_121", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Phone_Order_Items: BinaryAssociation = BinaryAssociation(
    name="Phone_Order_Items",
    ends={
        Property(name="Phone_Order_Items_022", type=Items, multiplicity=Multiplicity(1, 9999)),
        Property(name="Phone_Order_Items_123", type=Phone_Order, multiplicity=Multiplicity(0, 9999))
    }
)
Corporate_Order_Items: BinaryAssociation = BinaryAssociation(
    name="Corporate_Order_Items",
    ends={
        Property(name="Corporate_Order_Items_024", type=Items, multiplicity=Multiplicity(1, 9999)),
        Property(name="Corporate_Order_Items_125", type=Corporate_Order, multiplicity=Multiplicity(0, 9999))
    }
)
Phone_Order_Customer: BinaryAssociation = BinaryAssociation(
    name="Phone_Order_Customer",
    ends={
        Property(name="Phone_Order_Customer_026", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="Phone_Order_Customer_127", type=Phone_Order, multiplicity=Multiplicity(1, 1))
    }
)
Corporate_Order_Customer: BinaryAssociation = BinaryAssociation(
    name="Corporate_Order_Customer",
    ends={
        Property(name="Corporate_Order_Customer_028", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="Corporate_Order_Customer_129", type=Corporate_Order, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Nl19wDQxEeqqcaoAsxFIeg",
    types={Customer, Products, Shopping_Cart, Payment, Order, Account, Items, Phone_Order, Corporate_Order, Social_Login, Custom_Login},
    associations={Customer_Products, Customer_Order, Customer_Shopping_Cart, Customer_Payment, Account_Customer, Customer_Account, Payment__Order, Shopping_Cart_Items, Order_Account, Order_Account2, Account_Order, Phone_Order_Items, Corporate_Order_Items, Phone_Order_Customer, Corporate_Order_Customer},
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