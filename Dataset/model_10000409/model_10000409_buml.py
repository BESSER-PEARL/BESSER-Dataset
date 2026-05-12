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
Registered_Customer = Class(name="Registered_Customer")
__enumeration___UserState = Class(name="__enumeration___UserState")
New_Customer = Class(name="New_Customer")
Product = Class(name="Product")
Customer = Class(name="Customer")
__enumeration___OderStatus = Class(name="__enumeration___OderStatus")
Content = Class(name="Content")
Payment = Class(name="Payment")
Order = Class(name="Order")
Shopping_Cart = Class(name="Shopping_Cart")

# Registered_Customer class attributes and methods
Registered_Customer_Email: Property = Property(name="Email", type=StringType)
Registered_Customer_password: Property = Property(name="password", type=StringType)
Registered_Customer.attributes={Registered_Customer_Email, Registered_Customer_password}

# __enumeration___UserState class attributes and methods
__enumeration___UserState_new: Property = Property(name="new", type=StringType)
__enumeration___UserState_active: Property = Property(name="active", type=StringType)
__enumeration___UserState_blocked: Property = Property(name="blocked", type=StringType)
__enumeration___UserState_banned: Property = Property(name="banned", type=StringType)
__enumeration___UserState.attributes={__enumeration___UserState_new, __enumeration___UserState_blocked, __enumeration___UserState_banned, __enumeration___UserState_active}

# New_Customer class attributes and methods
New_Customer_Name: Property = Property(name="Name", type=StringType)
New_Customer_address: Property = Property(name="address", type=StringType)
New_Customer_phone: Property = Property(name="phone", type=StringType)
New_Customer_email: Property = Property(name="email", type=StringType)
New_Customer_password: Property = Property(name="password", type=StringType)
New_Customer.attributes={New_Customer_password, New_Customer_address, New_Customer_phone, New_Customer_email, New_Customer_Name}

# Product class attributes and methods
Product_id: Property = Property(name="id", type=StringType)
Product_name: Property = Property(name="name", type=StringType)
Product_supplier: Property = Property(name="supplier", type=StringType)
Product.attributes={Product_supplier, Product_id, Product_name}

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phone: Property = Property(name="phone", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer.attributes={Customer_name, Customer_email, Customer_phone, Customer_address}

# __enumeration___OderStatus class attributes and methods
__enumeration___OderStatus_new: Property = Property(name="new", type=StringType)
__enumeration___OderStatus_hold: Property = Property(name="hold", type=StringType)
__enumeration___OderStatus_shipped: Property = Property(name="shipped", type=StringType)
__enumeration___OderStatus_delivery: Property = Property(name="delivery", type=StringType)
__enumeration___OderStatus_closed: Property = Property(name="closed", type=StringType)
__enumeration___OderStatus_return: Property = Property(name="return", type=StringType)
__enumeration___OderStatus.attributes={__enumeration___OderStatus_hold, __enumeration___OderStatus_closed, __enumeration___OderStatus_new, __enumeration___OderStatus_return, __enumeration___OderStatus_shipped, __enumeration___OderStatus_delivery}

# Content class attributes and methods
Content_quantity: Property = Property(name="quantity", type=IntegerType)
Content_price: Property = Property(name="price", type=FloatType)
Content.attributes={Content_price, Content_quantity}

# Payment class attributes and methods
Payment_id: Property = Property(name="id", type=StringType)
Payment_paid: Property = Property(name="paid", type=DateType)
Payment_details: Property = Property(name="details", type=StringType)
Payment_total: Property = Property(name="total", type=FloatType)
Payment.attributes={Payment_details, Payment_paid, Payment_id, Payment_total}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=StringType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=DateType)
Order_ship_to: Property = Property(name="ship_to", type=StringType)
Order.attributes={Order_ship_to, Order_shipped, Order_ordered, Order_number}

# Shopping_Cart class attributes and methods
Shopping_Cart_id: Property = Property(name="id", type=StringType)
Shopping_Cart_number: Property = Property(name="number", type=StringType)
Shopping_Cart_total: Property = Property(name="total", type=FloatType)
Shopping_Cart.attributes={Shopping_Cart_id, Shopping_Cart_total, Shopping_Cart_number}

# Relationships
New_Customer_Customer: BinaryAssociation = BinaryAssociation(
    name="New_Customer_Customer",
    ends={
        Property(name="customer0", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="new_Customer1", type=New_Customer, multiplicity=Multiplicity(0, 1))
    }
)
Registered_Customer_Customer: BinaryAssociation = BinaryAssociation(
    name="Registered_Customer_Customer",
    ends={
        Property(name="customer2", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_Customer3", type=Registered_Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Product: BinaryAssociation = BinaryAssociation(
    name="Customer_Product",
    ends={
        Property(name="product4", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Content: BinaryAssociation = BinaryAssociation(
    name="Customer_Content",
    ends={
        Property(name="content6", type=Content, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Shopping_Cart_Order: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Order",
    ends={
        Property(name="order8", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="shopping_Cart9", type=Shopping_Cart, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order10", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Shopping_Cart_Payment: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Payment",
    ends={
        Property(name="payment12", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="shopping_Cart13", type=Shopping_Cart, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_33a6ffa4_e15c_4000_8f81_326d12de9860",
    types={Registered_Customer, __enumeration___UserState, New_Customer, Product, Customer, __enumeration___OderStatus, Content, Payment, Order, Shopping_Cart},
    associations={New_Customer_Customer, Registered_Customer_Customer, Customer_Product, Customer_Content, Shopping_Cart_Order, Customer_Order, Shopping_Cart_Payment},
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