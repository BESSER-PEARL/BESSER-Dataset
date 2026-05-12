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

OrderStatus: Enumeration = Enumeration(
    name="OrderStatus",
    literals={
            
    }
)

# Classes
Customer = Class(name="Customer")
Payment = Class(name="Payment")
ShoppinCart = Class(name="ShoppinCart")
Account = Class(name="Account")
WebUser = Class(name="WebUser")
Order = Class(name="Order")
LineItem = Class(name="LineItem")
Product = Class(name="Product")

# Customer class attributes and methods
Customer_address: Property = Property(name="address", type=StringType)
Customer_phone: Property = Property(name="phone", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer.attributes={Customer_address, Customer_email, Customer_phone}

# Payment class attributes and methods
Payment_total: Property = Property(name="total", type=FloatType)
Payment_details: Property = Property(name="details", type=StringType)
Payment_paidDate: Property = Property(name="paidDate", type=DateType)
Payment.attributes={Payment_details, Payment_total, Payment_paidDate}

# ShoppinCart class attributes and methods
ShoppinCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppinCart.attributes={ShoppinCart_creationDate}

# Account class attributes and methods
Account_billingAddress: Property = Property(name="billingAddress", type=StringType)
Account_open: Property = Property(name="open", type=DateType)
Account_closed: Property = Property(name="closed", type=DateType)
Account_isClosed: Property = Property(name="isClosed", type=BooleanType)
Account.attributes={Account_open, Account_isClosed, Account_billingAddress, Account_closed}

# WebUser class attributes and methods
WebUser_login: Property = Property(name="login", type=StringType)
WebUser_password: Property = Property(name="password", type=StringType)
WebUser_state: Property = Property(name="state", type=UserState)
WebUser.attributes={WebUser_password, WebUser_state, WebUser_login}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=OrderStatus)
Order.attributes={Order_shipTo, Order_shipped, Order_total, Order_number, Order_ordered, Order_status}

# LineItem class attributes and methods
LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
LineItem_price: Property = Property(name="price", type=FloatType)
LineItem.attributes={LineItem_quantity, LineItem_price}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_description, Product_name}

# Relationships
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="payment0", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="account1", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order2", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order3", type=Payment, multiplicity=Multiplicity(0, 9999))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order4", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="account5", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="customer6", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="webuser7", type=WebUser, multiplicity=Multiplicity(1, 1))
    }
)
ShoppinCart_WebUser: BinaryAssociation = BinaryAssociation(
    name="ShoppinCart_WebUser",
    ends={
        Property(name="webuser8", type=WebUser, multiplicity=Multiplicity(1, 1)),
        Property(name="shoppincart9", type=ShoppinCart, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="acc10", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer11", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="item12", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="product13", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items14", type=LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="lineitem15", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)
Account_ShoppinCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppinCart",
    ends={
        Property(name="cart16", type=ShoppinCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account17", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
ShoppinCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppinCart_LineItem",
    ends={
        Property(name="items18", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="sc19", type=ShoppinCart, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_XKDdUGVlEeqK2M3E1LfZ7Q",
    types={Customer, Payment, ShoppinCart, Account, WebUser, Order, LineItem, Product, UserState, OrderStatus},
    associations={Account_Payment, Payment_Order, Account_Order, WebUser_Customer, ShoppinCart_WebUser, Customer_Account, Product_LineItem, Order_LineItem, Account_ShoppinCart, ShoppinCart_LineItem},
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