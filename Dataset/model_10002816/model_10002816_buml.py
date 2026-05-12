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
Recollector = Class(name="Recollector")
Payment = Class(name="Payment")
ShoppingCart = Class(name="ShoppingCart")
Account = Class(name="Account")
User_Account = Class(name="User_Account")
Order = Class(name="Order")
LineItem = Class(name="LineItem")
Product = Class(name="Product")

# Recollector class attributes and methods
Recollector_id: Property = Property(name="id", type=StringType)
Recollector_full_name: Property = Property(name="full_name", type=StringType)
Recollector_telephone: Property = Property(name="telephone", type=StringType)
Recollector_latitude: Property = Property(name="latitude", type=StringType)
Recollector_longitude: Property = Property(name="longitude", type=StringType)
Recollector.attributes={Recollector_id, Recollector_longitude, Recollector_latitude, Recollector_full_name, Recollector_telephone}

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
Account.attributes={Account_isClosed, Account_open, Account_closed, Account_billingAddress}

# User_Account class attributes and methods
User_Account_email: Property = Property(name="email", type=StringType)
User_Account_password: Property = Property(name="password", type=StringType)
User_Account_full_name: Property = Property(name="full_name", type=StringType)
User_Account_telephone: Property = Property(name="telephone", type=StringType)
User_Account.attributes={User_Account_email, User_Account_full_name, User_Account_password, User_Account_telephone}

# Order class attributes and methods
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=OrderStatus)
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order.attributes={Order_status, Order_number, Order_shipped, Order_total, Order_shipTo, Order_ordered}

# LineItem class attributes and methods
LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
LineItem_price: Property = Property(name="price", type=FloatType)
LineItem.attributes={LineItem_price, LineItem_quantity}

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
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart2", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account3", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items4", type=LineItem, multiplicity=Multiplicity(1, 1)),
        Property(name="sc5", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="lineItems6", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="product7", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items8", type=LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="order9", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order10", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="account11", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order12", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment13", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="de878011_6ee0_4bea_946d_a811dbcb9a64",
    types={Recollector, Payment, ShoppingCart, Account, User_Account, Order, LineItem, Product, UserState, OrderStatus},
    associations={Account_Payment, Account_ShoppingCart, ShoppingCart_LineItem, Product_LineItem, Order_LineItem, Account_Order, Payment_Order},
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