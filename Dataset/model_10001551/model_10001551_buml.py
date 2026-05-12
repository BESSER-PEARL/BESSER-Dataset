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
View_items_UseCase = Class(name="View_items_UseCase")
Make_Purchase_UseCase = Class(name="Make_Purchase_UseCase")
Checkout_UseCase = Class(name="Checkout_UseCase")
Client_Register_UseCase = Class(name="Client_Register_UseCase")
Authentication_Actor = Class(name="Authentication_Actor")
Cash_on_Delivery_Actor = Class(name="Cash_on_Delivery_Actor")
Web_User = Class(name="Web_User")
Customer = Class(name="Customer")
Suppliers = Class(name="Suppliers")
Shopping_cart = Class(name="Shopping_cart")
Product = Class(name="Product")
Order = Class(name="Order")
Bill = Class(name="Bill")
Account = Class(name="Account")
Class_ = Class(name="Class")
Registered_Customer_Actor = Class(name="Registered_Customer_Actor")
New_customer_Actor = Class(name="New_customer_Actor")
Web_Customer_Actor = Class(name="Web_Customer_Actor")

# View_items_UseCase class attributes and methods

# Make_Purchase_UseCase class attributes and methods

# Checkout_UseCase class attributes and methods

# Client_Register_UseCase class attributes and methods

# Authentication_Actor class attributes and methods

# Cash_on_Delivery_Actor class attributes and methods

# Web_User class attributes and methods
Web_User_Username: Property = Property(name="Username", type=StringType)
Web_User_Password: Property = Property(name="Password", type=IntegerType)
Web_User.attributes={Web_User_Password, Web_User_Username}

# Customer class attributes and methods
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer_Contact: Property = Property(name="Contact", type=StringType)
Customer_Username: Property = Property(name="Username", type=StringType)
Customer_Password: Property = Property(name="Password", type=StringType)
Customer.attributes={Customer_Address, Customer_Username, Customer_Password, Customer_Name, Customer_Contact}

# Suppliers class attributes and methods
Suppliers_id: Property = Property(name="id", type=IntegerType)
Suppliers_Name: Property = Property(name="Name", type=StringType)
Suppliers.attributes={Suppliers_Name, Suppliers_id}

# Shopping_cart class attributes and methods
Shopping_cart_Cart_id: Property = Property(name="Cart_id", type=IntegerType)
Shopping_cart_Customer_id: Property = Property(name="Customer_id", type=Customer)
Shopping_cart_Product_Name: Property = Property(name="Product_Name", type=Product)
Shopping_cart_Quantity: Property = Property(name="Quantity", type=IntegerType)
Shopping_cart.attributes={Shopping_cart_Cart_id, Shopping_cart_Customer_id, Shopping_cart_Product_Name, Shopping_cart_Quantity}

# Product class attributes and methods
Product_id: Property = Property(name="id", type=IntegerType)
Product_Product_Name: Property = Property(name="Product_Name", type=StringType)
Product_Price: Property = Property(name="Price", type=IntegerType)
Product.attributes={Product_Price, Product_id, Product_Product_Name}

# Order class attributes and methods
Order_id: Property = Property(name="id", type=StringType)
Order_Total: Property = Property(name="Total", type=IntegerType)
Order.attributes={Order_id, Order_Total}

# Bill class attributes and methods
Bill_Customer_name: Property = Property(name="Customer_name", type=Customer)
Bill_Billing_address: Property = Property(name="Billing_address", type=Account)
Bill_Total_Price: Property = Property(name="Total_Price", type=Order)
Bill.attributes={Bill_Total_Price, Bill_Customer_name, Bill_Billing_address}

# Account class attributes and methods
Account_id: Property = Property(name="id", type=IntegerType)
Account_billing_address: Property = Property(name="billing_address", type=Customer)
Account.attributes={Account_billing_address, Account_id}

# Class class attributes and methods

# Registered_Customer_Actor class attributes and methods

# New_customer_Actor class attributes and methods

# Web_Customer_Actor class attributes and methods

# Relationships
Registered_Customer_View_items: BinaryAssociation = BinaryAssociation(
    name="Registered_Customer_View_items",
    ends={
        Property(name="view_items0", type=View_items_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_Customer1", type=Registered_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_Customer_Make_Purchase: BinaryAssociation = BinaryAssociation(
    name="Registered_Customer_Make_Purchase",
    ends={
        Property(name="make_Purchase2", type=Make_Purchase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_Customer3", type=Registered_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
New_customer_View_items: BinaryAssociation = BinaryAssociation(
    name="New_customer_View_items",
    ends={
        Property(name="view_items4", type=View_items_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="new_customer5", type=New_customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
New_customer_Client_Register: BinaryAssociation = BinaryAssociation(
    name="New_customer_Client_Register",
    ends={
        Property(name="client_Register6", type=Client_Register_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="new_customer7", type=New_customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_Cash_on_Delivery: BinaryAssociation = BinaryAssociation(
    name="Checkout_Cash_on_Delivery",
    ends={
        Property(name="checkout15", type=Checkout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cash_on_Delivery14", type=Cash_on_Delivery_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Web_User_Customer: BinaryAssociation = BinaryAssociation(
    name="Web_User_Customer",
    ends={
        Property(name="customer16", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="web_User17", type=Web_User, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Bill: BinaryAssociation = BinaryAssociation(
    name="Customer_Bill",
    ends={
        Property(name="bill18", type=Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="customer19", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Suppliers_Product: BinaryAssociation = BinaryAssociation(
    name="Suppliers_Product",
    ends={
        Property(name="product20", type=Product, multiplicity=Multiplicity(1, 1)),
        Property(name="suppliers21", type=Suppliers, multiplicity=Multiplicity(0, 1))
    }
)
Product_Shopping_cart: BinaryAssociation = BinaryAssociation(
    name="Product_Shopping_cart",
    ends={
        Property(name="shopping_cart22", type=Shopping_cart, multiplicity=Multiplicity(1, 1)),
        Property(name="product23", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Account_Shopping_cart: BinaryAssociation = BinaryAssociation(
    name="Account_Shopping_cart",
    ends={
        Property(name="shopping_cart24", type=Shopping_cart, multiplicity=Multiplicity(1, 1)),
        Property(name="account25", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account26", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer27", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order28", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="account29", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Order_Bill: BinaryAssociation = BinaryAssociation(
    name="Order_Bill",
    ends={
        Property(name="bill30", type=Bill, multiplicity=Multiplicity(0, 1)),
        Property(name="order31", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Bill_Account: BinaryAssociation = BinaryAssociation(
    name="Bill_Account",
    ends={
        Property(name="account32", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="bill33", type=Bill, multiplicity=Multiplicity(0, 1))
    }
)
Authentication_View_items: BinaryAssociation = BinaryAssociation(
    name="Authentication_View_items",
    ends={
        Property(name="view_items8", type=View_items_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="authentication9", type=Authentication_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Authentication_Client_Register: BinaryAssociation = BinaryAssociation(
    name="Authentication_Client_Register",
    ends={
        Property(name="client_Register10", type=Client_Register_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="authentication11", type=Authentication_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Authentication_Checkout: BinaryAssociation = BinaryAssociation(
    name="Authentication_Checkout",
    ends={
        Property(name="checkout12", type=Checkout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="authentication13", type=Authentication_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_FIFx8MWFEeidHYrYeMfZow",
    types={View_items_UseCase, Make_Purchase_UseCase, Checkout_UseCase, Client_Register_UseCase, Authentication_Actor, Cash_on_Delivery_Actor, Web_User, Customer, Suppliers, Shopping_cart, Product, Order, Bill, Account, Class_, Registered_Customer_Actor, New_customer_Actor, Web_Customer_Actor},
    associations={Registered_Customer_View_items, Registered_Customer_Make_Purchase, New_customer_View_items, New_customer_Client_Register, Checkout_Cash_on_Delivery, Web_User_Customer, Customer_Bill, Suppliers_Product, Product_Shopping_cart, Account_Shopping_cart, Customer_Account, Account_Order, Order_Bill, Bill_Account, Authentication_View_items, Authentication_Client_Register, Authentication_Checkout},
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