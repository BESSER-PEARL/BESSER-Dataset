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
ShoppingCart = Class(name="ShoppingCart")
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
Payment_paidDate: Property = Property(name="paidDate", type=DateType)
Payment_total: Property = Property(name="total", type=FloatType)
Payment_details: Property = Property(name="details", type=StringType)
Payment.attributes={Payment_total, Payment_paidDate, Payment_details}

# ShoppingCart class attributes and methods
ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppingCart.attributes={ShoppingCart_creationDate}

# Account class attributes and methods
Account_billingAddress: Property = Property(name="billingAddress", type=StringType)
Account_open: Property = Property(name="open", type=DateType)
Account_closed: Property = Property(name="closed", type=DateType)
Account_isClosed: Property = Property(name="isClosed", type=BooleanType)
Account.attributes={Account_billingAddress, Account_closed, Account_isClosed, Account_open}

# WebUser class attributes and methods
WebUser_login: Property = Property(name="login", type=StringType)
WebUser_password: Property = Property(name="password", type=StringType)
WebUser_state: Property = Property(name="state", type=UserState)
WebUser.attributes={WebUser_login, WebUser_state, WebUser_password}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=OrderStatus)
Order.attributes={Order_number, Order_shipTo, Order_total, Order_shipped, Order_status, Order_ordered}

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
        Property(name="p0", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="acc1", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart2", type=ShoppingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser3", type=WebUser, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="customer4", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser5", type=WebUser, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account6", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items10", type=LineItem, multiplicity=Multiplicity(1, 1)),
        Property(name="sc11", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="lineItems12", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="product13", type=Product, multiplicity=Multiplicity(1, 1))
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
        Property(name="account17", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order18", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment19", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart8", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account9", type=Account, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0c9d4a6c_241f_4651_9982_e3702264adc9",
    types={Customer, Payment, ShoppingCart, Account, WebUser, Order, LineItem, Product, UserState, OrderStatus},
    associations={Account_Payment, WebUser_ShoppingCart, WebUser_Customer, Customer_Account, ShoppingCart_LineItem, Product_LineItem, Order_LineItem, Account_Order, Payment_Order, Account_ShoppingCart},
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