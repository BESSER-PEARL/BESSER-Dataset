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
MyActor_Actor = Class(name="MyActor_Actor")
Admin_Actor = Class(name="Admin_Actor")
Webuser_Actor = Class(name="Webuser_Actor")
AjoutProduit_UseCase = Class(name="AjoutProduit_UseCase")
Customer = Class(name="Customer")
Payment = Class(name="Payment")
ShoppingCart = Class(name="ShoppingCart")
Account = Class(name="Account")
WebUser = Class(name="WebUser")
Order = Class(name="Order")
LineItem = Class(name="LineItem")
Product = Class(name="Product")

# MyActor_Actor class attributes and methods

# Admin_Actor class attributes and methods

# Webuser_Actor class attributes and methods

# AjoutProduit_UseCase class attributes and methods

# Customer class attributes and methods
Customer_address: Property = Property(name="address", type=StringType)
Customer_phone: Property = Property(name="phone", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer.attributes={Customer_email, Customer_address, Customer_phone}

# Payment class attributes and methods
Payment_paidDate: Property = Property(name="paidDate", type=DateType)
Payment_total: Property = Property(name="total", type=FloatType)
Payment_details: Property = Property(name="details", type=StringType)
Payment.attributes={Payment_paidDate, Payment_total, Payment_details}

# ShoppingCart class attributes and methods
ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppingCart.attributes={ShoppingCart_creationDate}

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
WebUser.attributes={WebUser_state, WebUser_login, WebUser_password}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=OrderStatus)
Order.attributes={Order_status, Order_number, Order_shipped, Order_total, Order_ordered, Order_shipTo}

# LineItem class attributes and methods
LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
LineItem_price: Property = Property(name="price", type=FloatType)
LineItem.attributes={LineItem_price, LineItem_quantity}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_name, Product_description}

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="admin0", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="ajoutproduit1", type=AjoutProduit_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items2", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="sc3", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart4", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account5", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
LineItem_Product: BinaryAssociation = BinaryAssociation(
    name="LineItem_Product",
    ends={
        Property(name="product6", type=Product, multiplicity=Multiplicity(1, 1)),
        Property(name="item7", type=LineItem, multiplicity=Multiplicity(0, 9999))
    }
)
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart8", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser9", type=WebUser, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="customer10", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser11", type=WebUser, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="acc12", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer13", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items14", type=LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="order15", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order16", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="accnt17", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="payment18", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="account19", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order20", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment21", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f7cb9ede_73f5_4d19_babe_f5969f97e197",
    types={MyActor_Actor, Admin_Actor, Webuser_Actor, AjoutProduit_UseCase, Customer, Payment, ShoppingCart, Account, WebUser, Order, LineItem, Product, UserState, OrderStatus},
    associations={association2, ShoppingCart_LineItem, Account_ShoppingCart, LineItem_Product, WebUser_ShoppingCart, WebUser_Customer, Customer_Account, Order_LineItem, Account_Order, Account_Payment, Payment_Order},
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