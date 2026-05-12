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
user = Class(name="user")
administrator = Class(name="administrator")
Customer = Class(name="Customer")
Shopping_Cart = Class(name="Shopping_Cart")
Payment = Class(name="Payment")
Product = Class(name="Product")
Supplier = Class(name="Supplier")
Cancellation = Class(name="Cancellation")
web_customer_Actor = Class(name="web_customer_Actor")
Registered_customer__Actor = Class(name="Registered_customer__Actor")
New_Customer_Actor = Class(name="New_Customer_Actor")
Online_grocery_shopping_Component = Class(name="Online_grocery_shopping_Component")
Authentication_Actor = Class(name="Authentication_Actor")
Identity_Provider_Actor = Class(name="Identity_Provider_Actor")
View_Items_external = Class(name="View_Items_external")
Make_Purchase_external = Class(name="Make_Purchase_external")
Client_Register_external = Class(name="Client_Register_external")

# user class attributes and methods
user_userID: Property = Property(name="userID", type=StringType)
user_password: Property = Property(name="password", type=StringType)
user_loginStatus: Property = Property(name="loginStatus", type=StringType)
user.attributes={user_userID, user_password, user_loginStatus}

# administrator class attributes and methods
administrator_adminName: Property = Property(name="adminName", type=StringType)
administrator_email: Property = Property(name="email", type=StringType)
administrator.attributes={administrator_adminName, administrator_email}

# Customer class attributes and methods
Customer_address: Property = Property(name="address", type=StringType)
Customer_loginName: Property = Property(name="loginName", type=StringType)
Customer_mobileNo: Property = Property(name="mobileNo", type=IntegerType)
Customer.attributes={Customer_loginName, Customer_address, Customer_mobileNo}

# Shopping_Cart class attributes and methods
Shopping_Cart_cartId: Property = Property(name="cartId", type=StringType)
Shopping_Cart_quantity: Property = Property(name="quantity", type=IntegerType)
Shopping_Cart_dateAdded: Property = Property(name="dateAdded", type=StringType)
Shopping_Cart.attributes={Shopping_Cart_dateAdded, Shopping_Cart_cartId, Shopping_Cart_quantity}

# Payment class attributes and methods
Payment_customerId: Property = Property(name="customerId", type=StringType)
Payment_productID: Property = Property(name="productID", type=StringType)
Payment_amount: Property = Property(name="amount", type=IntegerType)
Payment.attributes={Payment_customerId, Payment_productID, Payment_amount}

# Product class attributes and methods
Product_quantity: Property = Property(name="quantity", type=IntegerType)
Product_name: Property = Property(name="name", type=StringType)
Product_price: Property = Property(name="price", type=IntegerType)
Product_productID: Property = Property(name="productID", type=StringType)
Product.attributes={Product_name, Product_productID, Product_price, Product_quantity}

# Supplier class attributes and methods
Supplier_suppName: Property = Property(name="suppName", type=StringType)
Supplier_suppID: Property = Property(name="suppID", type=StringType)
Supplier_address: Property = Property(name="address", type=StringType)
Supplier.attributes={Supplier_suppID, Supplier_suppName, Supplier_address}

# Cancellation class attributes and methods
Cancellation_customerID: Property = Property(name="customerID", type=StringType)
Cancellation_productID: Property = Property(name="productID", type=StringType)
Cancellation_amount: Property = Property(name="amount", type=StringType)
Cancellation.attributes={Cancellation_amount, Cancellation_productID, Cancellation_customerID}

# web_customer_Actor class attributes and methods

# Registered_customer__Actor class attributes and methods

# New_Customer_Actor class attributes and methods

# Online_grocery_shopping_Component class attributes and methods

# Authentication_Actor class attributes and methods

# Identity_Provider_Actor class attributes and methods

# View_Items_external class attributes and methods

# Make_Purchase_external class attributes and methods

# Client_Register_external class attributes and methods

# Relationships
user_user: BinaryAssociation = BinaryAssociation(
    name="user_user",
    ends={
        Property(name="user0", type=user, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=user, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Shopping_Cart",
    ends={
        Property(name="shopping_Cart2", type=Shopping_Cart, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer3", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Shopping_Cart_Product: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Product",
    ends={
        Property(name="product4", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="shopping_Cart5", type=Shopping_Cart, multiplicity=Multiplicity(1, 1))
    }
)
Shopping_Cart_Payment: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Payment",
    ends={
        Property(name="payment6", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="shopping_Cart7", type=Shopping_Cart, multiplicity=Multiplicity(1, 1))
    }
)
Product_Cancellation: BinaryAssociation = BinaryAssociation(
    name="Product_Cancellation",
    ends={
        Property(name="cancellation8", type=Cancellation, multiplicity=Multiplicity(1, 1)),
        Property(name="product9", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Product_Supplier: BinaryAssociation = BinaryAssociation(
    name="Product_Supplier",
    ends={
        Property(name="supplier10", type=Supplier, multiplicity=Multiplicity(0, 9999)),
        Property(name="product11", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Registered_customer__View_Items: BinaryAssociation = BinaryAssociation(
    name="Registered_customer__View_Items",
    ends={
        Property(name="view_Items12", type=View_Items_external, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_customer13", type=Registered_customer__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_customer__Make_Purchase: BinaryAssociation = BinaryAssociation(
    name="Registered_customer__Make_Purchase",
    ends={
        Property(name="make_Purchase14", type=Make_Purchase_external, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_customer15", type=Registered_customer__Actor, multiplicity=Multiplicity(0, 1))
    }
)
New_Customer_View_Items: BinaryAssociation = BinaryAssociation(
    name="New_Customer_View_Items",
    ends={
        Property(name="view_Items16", type=View_Items_external, multiplicity=Multiplicity(0, 1)),
        Property(name="new_Customer17", type=New_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
New_Customer_Client_Register: BinaryAssociation = BinaryAssociation(
    name="New_Customer_Client_Register",
    ends={
        Property(name="client_Register18", type=Client_Register_external, multiplicity=Multiplicity(0, 1)),
        Property(name="new_Customer19", type=New_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bc5da61c_fd95_4d0b_ba94_28ef5c3447f1",
    types={user, administrator, Customer, Shopping_Cart, Payment, Product, Supplier, Cancellation, web_customer_Actor, Registered_customer__Actor, New_Customer_Actor, Online_grocery_shopping_Component, Authentication_Actor, Identity_Provider_Actor, View_Items_external, Make_Purchase_external, Client_Register_external},
    associations={user_user, Customer_Shopping_Cart, Shopping_Cart_Product, Shopping_Cart_Payment, Product_Cancellation, Product_Supplier, Registered_customer__View_Items, Registered_customer__Make_Purchase, New_Customer_View_Items, New_Customer_Client_Register},
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