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
RedisClient = Class(name="RedisClient")
Payment = Class(name="Payment")
ShoppingCart = Class(name="ShoppingCart")
Redis = Class(name="Redis")
RadixClient = Class(name="RadixClient")
Order = Class(name="Order")
LineItem = Class(name="LineItem")
Product = Class(name="Product")
LZUser2 = Class(name="LZUser2")

# RedisClient class attributes and methods
RedisClient_RadixClient: Property = Property(name="RadixClient", type=StringType)
RedisClient_log: Property = Property(name="log", type=StringType)
RedisClient_email: Property = Property(name="email", type=StringType)
RedisClient.attributes={RedisClient_RadixClient, RedisClient_email, RedisClient_log}

# Payment class attributes and methods
Payment_paidDate: Property = Property(name="paidDate", type=DateType)
Payment_total: Property = Property(name="total", type=FloatType)
Payment_details: Property = Property(name="details", type=StringType)
Payment.attributes={Payment_paidDate, Payment_total, Payment_details}

# ShoppingCart class attributes and methods
ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppingCart.attributes={ShoppingCart_creationDate}

# Redis class attributes and methods

# RadixClient class attributes and methods
RadixClient_populate: Property = Property(name="populate", type=StringType)
RadixClient_password: Property = Property(name="password", type=StringType)
RadixClient_state: Property = Property(name="state", type=UserState)
RadixClient.attributes={RadixClient_populate, RadixClient_password, RadixClient_state}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=OrderStatus)
Order.attributes={Order_shipped, Order_status, Order_total, Order_number, Order_shipTo, Order_ordered}

# LineItem class attributes and methods
LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
LineItem_price: Property = Property(name="price", type=FloatType)
LineItem.attributes={LineItem_quantity, LineItem_price}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_name, Product_description}

# LZUser2 class attributes and methods
LZUser2_populate: Property = Property(name="populate", type=StringType)
LZUser2_password: Property = Property(name="password", type=StringType)
LZUser2_state: Property = Property(name="state", type=UserState)
LZUser2.attributes={LZUser2_populate, LZUser2_password, LZUser2_state}

# Relationships
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart6", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account7", type=Redis, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items8", type=LineItem, multiplicity=Multiplicity(1, 1)),
        Property(name="sc9", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="lineItems10", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="product11", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items12", type=LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="order13", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order14", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="account15", type=Redis, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order16", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment17", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="p0", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="acc1", type=Redis, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart2", type=ShoppingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser3", type=RadixClient, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account4", type=Redis, multiplicity=Multiplicity(1, 1)),
        Property(name="customer5", type=RedisClient, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="__2Kg8Hf4EeqeQcxm9hmzHw",
    types={RedisClient, Payment, ShoppingCart, Redis, RadixClient, Order, LineItem, Product, LZUser2, UserState, OrderStatus},
    associations={Account_ShoppingCart, ShoppingCart_LineItem, Product_LineItem, Order_LineItem, Account_Order, Payment_Order, Account_Payment, WebUser_ShoppingCart, Customer_Account},
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