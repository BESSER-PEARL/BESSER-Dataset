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
Account = Class(name="Account")
Payment = Class(name="Payment")
Order = Class(name="Order")
Product = Class(name="Product")
Cart = Class(name="Cart")
catalog = Class(name="catalog")
Payment_Verification = Class(name="Payment_Verification")
Web_Login = Class(name="Web_Login")

# Customer class attributes and methods
Customer_id_: Property = Property(name="id_", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phone: Property = Property(name="phone", type=IntegerType)
Customer_email: Property = Property(name="email", type=StringType)
Customer.attributes={Customer_id_, Customer_address, Customer_phone, Customer_email}

# Account class attributes and methods
Account_id: Property = Property(name="id", type=StringType)
Account_billing_address: Property = Property(name="billing_address", type=StringType)
Account_open: Property = Property(name="open", type=StringType)
Account.attributes={Account_id, Account_open, Account_billing_address}

# Payment class attributes and methods
Payment_txn_id: Property = Property(name="txn_id", type=StringType)
Payment_paid: Property = Property(name="paid", type=StringType)
Payment_total: Property = Property(name="total", type=StringType)
Payment_Details: Property = Property(name="Details", type=StringType)
Payment.attributes={Payment_total, Payment_paid, Payment_Details, Payment_txn_id}

# Order class attributes and methods
Order_items: Property = Property(name="items", type=StringType)
Order_ordered: Property = Property(name="ordered", type=StringType)
Order_shipped: Property = Property(name="shipped", type=StringType)
Order_address: Property = Property(name="address", type=StringType)
Order_status: Property = Property(name="status", type=StringType)
Order_t: Property = Property(name="t", type=StringType)
Order.attributes={Order_t, Order_address, Order_status, Order_ordered, Order_items, Order_shipped}

# Product class attributes and methods
Product_Category: Property = Property(name="Category", type=StringType)
Product_name: Property = Property(name="name", type=StringType)
Product_price: Property = Property(name="price", type=StringType)
Product_attribute: Property = Property(name="attribute", type=StringType)
Product.attributes={Product_price, Product_name, Product_Category, Product_attribute}

# Cart class attributes and methods
Cart_Id: Property = Property(name="Id", type=StringType)
Cart_items: Property = Property(name="items", type=IntegerType)
Cart.attributes={Cart_Id, Cart_items}

# catalog class attributes and methods
catalog_category: Property = Property(name="category", type=StringType)
catalog_name: Property = Property(name="name", type=StringType)
catalog.attributes={catalog_name, catalog_category}

# Payment_Verification class attributes and methods
Payment_Verification_txn_id: Property = Property(name="txn_id", type=StringType)
Payment_Verification_status: Property = Property(name="status", type=StringType)
Payment_Verification.attributes={Payment_Verification_status, Payment_Verification_txn_id}

# Web_Login class attributes and methods
Web_Login_login_id: Property = Property(name="login_id", type=StringType)
Web_Login_password: Property = Property(name="password", type=StringType)
Web_Login_verification: Property = Property(name="verification", type=Customer)
Web_Login.attributes={Web_Login_login_id, Web_Login_password, Web_Login_verification}

# Relationships
Web_Login_Customer: BinaryAssociation = BinaryAssociation(
    name="Web_Login_Customer",
    ends={
        Property(name="customer0", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="web_Login1", type=Web_Login, multiplicity=Multiplicity(0, 1))
    }
)
Web_Login_Cart: BinaryAssociation = BinaryAssociation(
    name="Web_Login_Cart",
    ends={
        Property(name="cart2", type=Cart, multiplicity=Multiplicity(0, 1)),
        Property(name="web_Login3", type=Web_Login, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
catalog_Product: BinaryAssociation = BinaryAssociation(
    name="catalog_Product",
    ends={
        Property(name="product6", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="catalog7", type=catalog, multiplicity=Multiplicity(0, 1))
    }
)
Product_Order: BinaryAssociation = BinaryAssociation(
    name="Product_Order",
    ends={
        Property(name="order8", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="product9", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Order_Payment: BinaryAssociation = BinaryAssociation(
    name="Order_Payment",
    ends={
        Property(name="payment10", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="order11", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Payment_Verification: BinaryAssociation = BinaryAssociation(
    name="Payment_Payment_Verification",
    ends={
        Property(name="payment_Verification12", type=Payment_Verification, multiplicity=Multiplicity(0, 1)),
        Property(name="payment13", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Account__Order: BinaryAssociation = BinaryAssociation(
    name="Account__Order",
    ends={
        Property(name="order14", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="account15", type=Account, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Verification_Account: BinaryAssociation = BinaryAssociation(
    name="Payment_Verification_Account",
    ends={
        Property(name="account16", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="payment_Verification17", type=Payment_Verification, multiplicity=Multiplicity(0, 1))
    }
)
Cart_Order: BinaryAssociation = BinaryAssociation(
    name="Cart_Order",
    ends={
        Property(name="order18", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="cart19", type=Cart, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Verification_Customer: BinaryAssociation = BinaryAssociation(
    name="Payment_Verification_Customer",
    ends={
        Property(name="customer20", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="payment_Verification21", type=Payment_Verification, multiplicity=Multiplicity(0, 1))
    }
)
Cart_Product: BinaryAssociation = BinaryAssociation(
    name="Cart_Product",
    ends={
        Property(name="product22", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="cart23", type=Cart, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_QA2iwKcFEeeEQN1ZyOr__g",
    types={Customer, Account, Payment, Order, Product, Cart, catalog, Payment_Verification, Web_Login},
    associations={Web_Login_Customer, Web_Login_Cart, Customer_Account, catalog_Product, Product_Order, Order_Payment, Payment_Payment_Verification, Account__Order, Payment_Verification_Account, Cart_Order, Payment_Verification_Customer, Cart_Product},
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