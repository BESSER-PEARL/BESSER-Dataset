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
Admin_Actor = Class(name="Admin_Actor")
customer_Actor = Class(name="customer_Actor")
Login_UseCase = Class(name="Login_UseCase")
Payment_UseCase = Class(name="Payment_UseCase")
Order_Details_UseCase = Class(name="Order_Details_UseCase")
Password_UseCase = Class(name="Password_UseCase")
Registration_UseCase = Class(name="Registration_UseCase")
cart_UseCase = Class(name="cart_UseCase")
Shipping_UseCase = Class(name="Shipping_UseCase")
credit_card_UseCase = Class(name="credit_card_UseCase")
cheque_UseCase = Class(name="cheque_UseCase")
Order_Status = Class(name="Order_Status")
Customer = Class(name="Customer")
Order = Class(name="Order")
OrderDetails = Class(name="OrderDetails")
Payment = Class(name="Payment")
Credit_Card = Class(name="Credit_Card")
Cash = Class(name="Cash")

# Admin_Actor class attributes and methods

# customer_Actor class attributes and methods

# Login_UseCase class attributes and methods

# Payment_UseCase class attributes and methods

# Order_Details_UseCase class attributes and methods

# Password_UseCase class attributes and methods

# Registration_UseCase class attributes and methods

# cart_UseCase class attributes and methods

# Shipping_UseCase class attributes and methods

# credit_card_UseCase class attributes and methods

# cheque_UseCase class attributes and methods

# Order_Status class attributes and methods
Order_Status_Create: Property = Property(name="Create", type=IntegerType)
Order_Status_Deliveried: Property = Property(name="Deliveried", type=IntegerType)
Order_Status_Paid: Property = Property(name="Paid", type=IntegerType)
Order_Status.attributes={Order_Status_Create, Order_Status_Deliveried, Order_Status_Paid}

# Customer class attributes and methods
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer_Contact: Property = Property(name="Contact", type=StringType)
Customer.attributes={Customer_Contact, Customer_Address, Customer_Name}

# Order class attributes and methods
Order_Date: Property = Property(name="Date", type=StringType)
Order.attributes={Order_Date}

# OrderDetails class attributes and methods
OrderDetails_qty: Property = Property(name="qty", type=IntegerType)
OrderDetails.attributes={OrderDetails_qty}

# Payment class attributes and methods
Payment_Amount: Property = Property(name="Amount", type=StringType)
Payment.attributes={Payment_Amount}

# Credit_Card class attributes and methods
Credit_Card_number: Property = Property(name="number", type=IntegerType)
Credit_Card.attributes={Credit_Card_number}

# Cash class attributes and methods
Cash_cashTendered: Property = Property(name="cashTendered", type=IntegerType)
Cash.attributes={Cash_cashTendered}

# Relationships
Admin_Password: BinaryAssociation = BinaryAssociation(
    name="Admin_Password",
    ends={
        Property(name="password0", type=Password_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin1", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Login_customer: BinaryAssociation = BinaryAssociation(
    name="Login_customer",
    ends={
        Property(name="customer2", type=customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login3", type=Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Password_customer: BinaryAssociation = BinaryAssociation(
    name="Password_customer",
    ends={
        Property(name="customer4", type=customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="password5", type=Password_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Payment_customer: BinaryAssociation = BinaryAssociation(
    name="Payment_customer",
    ends={
        Property(name="customer6", type=customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="payment7", type=Payment_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
customer_Order_Details: BinaryAssociation = BinaryAssociation(
    name="customer_Order_Details",
    ends={
        Property(name="order_Details8", type=Order_Details_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_cart: BinaryAssociation = BinaryAssociation(
    name="customer_cart",
    ends={
        Property(name="cart10", type=cart_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registration_customer: BinaryAssociation = BinaryAssociation(
    name="Registration_customer",
    ends={
        Property(name="customer12", type=customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registration13", type=Registration_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
customer_Shipping: BinaryAssociation = BinaryAssociation(
    name="customer_Shipping",
    ends={
        Property(name="shipping14", type=Shipping_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer15", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order16", type=Order, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer17", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Order_Status_Order: BinaryAssociation = BinaryAssociation(
    name="Order_Status_Order",
    ends={
        Property(name="order18", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="order_Status19", type=Order_Status, multiplicity=Multiplicity(0, 1))
    }
)
Order_OrderDetails: BinaryAssociation = BinaryAssociation(
    name="Order_OrderDetails",
    ends={
        Property(name="orderDetails20", type=OrderDetails, multiplicity=Multiplicity(0, 1)),
        Property(name="order21", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order____Payment: BinaryAssociation = BinaryAssociation(
    name="Order____Payment",
    ends={
        Property(name="Payment22", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="order23", type=Order, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_tkudcNGSEemr0Oy2Fixrzg",
    types={Admin_Actor, customer_Actor, Login_UseCase, Payment_UseCase, Order_Details_UseCase, Password_UseCase, Registration_UseCase, cart_UseCase, Shipping_UseCase, credit_card_UseCase, cheque_UseCase, Order_Status, Customer, Order, OrderDetails, Payment, Credit_Card, Cash},
    associations={Admin_Password, Login_customer, Password_customer, Payment_customer, customer_Order_Details, customer_cart, Registration_customer, customer_Shipping, Customer_Order, Order_Status_Order, Order_OrderDetails, Order____Payment},
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