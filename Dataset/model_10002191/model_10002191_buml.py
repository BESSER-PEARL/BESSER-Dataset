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
Payment = Class(name="Payment")
ShoppingCart = Class(name="ShoppingCart")
ShoppingCart1 = Class(name="ShoppingCart1")
Order = Class(name="Order")
LineItem = Class(name="LineItem")
Product = Class(name="Product")

# Payment class attributes and methods
Payment_paidDate: Property = Property(name="paidDate", type=DateType)
Payment_total: Property = Property(name="total", type=FloatType)
Payment_details: Property = Property(name="details", type=StringType)
Payment.attributes={Payment_total, Payment_details, Payment_paidDate}

# ShoppingCart class attributes and methods
ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppingCart.attributes={ShoppingCart_creationDate}

# ShoppingCart1 class attributes and methods
ShoppingCart1_itemCount: Property = Property(name="itemCount", type=IntegerType)
ShoppingCart1_totalPrice: Property = Property(name="totalPrice", type=IntegerType)
ShoppingCart1_closed: Property = Property(name="closed", type=DateType)
ShoppingCart1_isClosed: Property = Property(name="isClosed", type=BooleanType)
ShoppingCart1.attributes={ShoppingCart1_isClosed, ShoppingCart1_itemCount, ShoppingCart1_totalPrice, ShoppingCart1_closed}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=OrderStatus)
Order.attributes={Order_ordered, Order_shipped, Order_total, Order_number, Order_status, Order_shipTo}

# LineItem class attributes and methods
LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
LineItem_price: Property = Property(name="price", type=FloatType)
LineItem.attributes={LineItem_price, LineItem_quantity}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_name, Product_description}

# Relationships
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="p0", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="acc1", type=ShoppingCart1, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart2", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account3", type=ShoppingCart1, multiplicity=Multiplicity(1, 1))
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
        Property(name="account11", type=ShoppingCart1, multiplicity=Multiplicity(1, 1))
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
    name="_vPujQHDeEeqhRdvvYtDJdw",
    types={Payment, ShoppingCart, ShoppingCart1, Order, LineItem, Product, UserState, OrderStatus},
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