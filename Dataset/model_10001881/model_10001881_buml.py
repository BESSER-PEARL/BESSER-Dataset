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
Order_Compute_Price = Class(name="Order_Compute_Price")
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
Payment.attributes={Payment_details, Payment_paidDate, Payment_total}

# ShoppinCart class attributes and methods
ShoppinCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppinCart.attributes={ShoppinCart_creationDate}

# Account class attributes and methods
Account_billingAddress: Property = Property(name="billingAddress", type=StringType)
Account_open: Property = Property(name="open", type=DateType)
Account_closed: Property = Property(name="closed", type=DateType)
Account_isClosed: Property = Property(name="isClosed", type=BooleanType)
Account.attributes={Account_billingAddress, Account_open, Account_closed, Account_isClosed}

# Order_Compute_Price class attributes and methods
Order_Compute_Price_number: Property = Property(name="number", type=IntegerType)
Order_Compute_Price_ordered: Property = Property(name="ordered", type=DateType)
Order_Compute_Price_shipped: Property = Property(name="shipped", type=BooleanType)
Order_Compute_Price_shipTo: Property = Property(name="shipTo", type=StringType)
Order_Compute_Price_total: Property = Property(name="total", type=FloatType)
Order_Compute_Price_status: Property = Property(name="status", type=OrderStatus)
Order_Compute_Price.attributes={Order_Compute_Price_number, Order_Compute_Price_shipped, Order_Compute_Price_shipTo, Order_Compute_Price_total, Order_Compute_Price_status, Order_Compute_Price_ordered}

# LineItem class attributes and methods
LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
LineItem_price: Property = Property(name="price", type=FloatType)
LineItem.attributes={LineItem_quantity, LineItem_price}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_name, Product_description}

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
        Property(name="order2", type=Order_Compute_Price, multiplicity=Multiplicity(1, 1)),
        Property(name="order3", type=Payment, multiplicity=Multiplicity(0, 9999))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order4", type=Order_Compute_Price, multiplicity=Multiplicity(0, 9999)),
        Property(name="account5", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="acc6", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="item8", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="product9", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items10", type=LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="lineitem11", type=Order_Compute_Price, multiplicity=Multiplicity(0, 9999))
    }
)
Account_ShoppinCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppinCart",
    ends={
        Property(name="cart12", type=ShoppinCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account13", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
ShoppinCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppinCart_LineItem",
    ends={
        Property(name="items14", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="sc15", type=ShoppinCart, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_bAFQ8HEcEeqhRdvvYtDJdw",
    types={Customer, Payment, ShoppinCart, Account, Order_Compute_Price, LineItem, Product, UserState, OrderStatus},
    associations={Account_Payment, Payment_Order, Account_Order, Customer_Account, Product_LineItem, Order_LineItem, Account_ShoppinCart, ShoppinCart_LineItem},
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