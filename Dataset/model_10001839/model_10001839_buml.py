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
Payment = Class(name="Payment")
ShoppingCart = Class(name="ShoppingCart")
Account = Class(name="Account")
Visitor = Class(name="Visitor")
Order = Class(name="Order")
LineItem = Class(name="LineItem")
Product = Class(name="Product")
MyActor_Actor = Class(name="MyActor_Actor")
Admin_Actor = Class(name="Admin_Actor")
Webuser_Actor = Class(name="Webuser_Actor")
AjoutProduit_UseCase = Class(name="AjoutProduit_UseCase")
Administrator = Class(name="Administrator")
Shop_Owner = Class(name="Shop_Owner")
Customer_Support = Class(name="Customer_Support")

# Customer class attributes and methods
Customer_IDCust: Property = Property(name="IDCust", type=IntegerType)
Customer_Last_name: Property = Property(name="Last_name", type=StringType)
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_Password: Property = Property(name="Password", type=StringType)
Customer_Email: Property = Property(name="Email", type=StringType)
Customer.attributes={Customer_IDCust, Customer_Name, Customer_Last_name, Customer_Password, Customer_Email}

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
Account.attributes={Account_isClosed, Account_closed, Account_billingAddress, Account_open}

# Visitor class attributes and methods

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=StringType)
Order.attributes={Order_number, Order_shipTo, Order_status, Order_ordered, Order_total, Order_shipped}

# LineItem class attributes and methods
LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
LineItem_price: Property = Property(name="price", type=FloatType)
LineItem.attributes={LineItem_price, LineItem_quantity}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_name, Product_description}

# MyActor_Actor class attributes and methods

# Admin_Actor class attributes and methods

# Webuser_Actor class attributes and methods

# AjoutProduit_UseCase class attributes and methods

# Administrator class attributes and methods
Administrator_IDAdm: Property = Property(name="IDAdm", type=IntegerType)
Administrator_Email: Property = Property(name="Email", type=StringType)
Administrator_Password: Property = Property(name="Password", type=StringType)
Administrator_Name: Property = Property(name="Name", type=StringType)
Administrator_Last_name: Property = Property(name="Last_name", type=StringType)
Administrator.attributes={Administrator_IDAdm, Administrator_Email, Administrator_Last_name, Administrator_Name, Administrator_Password}

# Shop_Owner class attributes and methods
Shop_Owner_Last_name: Property = Property(name="Last_name", type=StringType)
Shop_Owner_Name: Property = Property(name="Name", type=StringType)
Shop_Owner_Password: Property = Property(name="Password", type=StringType)
Shop_Owner_IDSowner: Property = Property(name="IDSowner", type=IntegerType)
Shop_Owner_Email: Property = Property(name="Email", type=StringType)
Shop_Owner.attributes={Shop_Owner_Password, Shop_Owner_Last_name, Shop_Owner_Email, Shop_Owner_IDSowner, Shop_Owner_Name}

# Customer_Support class attributes and methods
Customer_Support_Email: Property = Property(name="Email", type=StringType)
Customer_Support_Password: Property = Property(name="Password", type=StringType)
Customer_Support_ID: Property = Property(name="ID", type=IntegerType)
Customer_Support.attributes={Customer_Support_Password, Customer_Support_Email, Customer_Support_ID}

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="admin0", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="ajoutproduit1", type=AjoutProduit_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items2", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="shopping_cart3", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Visitor_Product: BinaryAssociation = BinaryAssociation(
    name="Visitor_Product",
    ends={
        Property(name="view_products30", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="visitor31", type=Visitor, multiplicity=Multiplicity(1, 1))
    }
)
Administrator_Customer: BinaryAssociation = BinaryAssociation(
    name="Administrator_Customer",
    ends={
        Property(name="Manage32", type=Customer, multiplicity=Multiplicity(1, 9999)),
        Property(name="Administrator_Customer_133", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Product: BinaryAssociation = BinaryAssociation(
    name="Administrator_Product",
    ends={
        Property(name="View_and_edit34", type=Product, multiplicity=Multiplicity(1, 9999)),
        Property(name="administrator35", type=Administrator, multiplicity=Multiplicity(1, 1))
    }
)
Vendors_Administrator: BinaryAssociation = BinaryAssociation(
    name="Vendors_Administrator",
    ends={
        Property(name="Vendors_Administrator_036", type=Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="give_permission37", type=Shop_Owner, multiplicity=Multiplicity(1, 9999))
    }
)
Vendors_Product: BinaryAssociation = BinaryAssociation(
    name="Vendors_Product",
    ends={
        Property(name="add_and_modify38", type=Product, multiplicity=Multiplicity(1, 9999)),
        Property(name="vendors39", type=Shop_Owner, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart4", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account5", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
LineItem_Product: BinaryAssociation = BinaryAssociation(
    name="LineItem_Product",
    ends={
        Property(name="product6", type=Product, multiplicity=Multiplicity(1, 1)),
        Property(name="item7", type=LineItem, multiplicity=Multiplicity(0, 9999))
    }
)
Account_ShoppingCart2: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart2",
    ends={
        Property(name="Giving_feedback40", type=ShoppingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="Account_ShoppingCart2_141", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart8", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser9", type=Visitor, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Support_Customer: BinaryAssociation = BinaryAssociation(
    name="Customer_Support_Customer",
    ends={
        Property(name="help42", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="Ask_question43", type=Customer_Support, multiplicity=Multiplicity(0, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="customer10", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser11", type=Visitor, multiplicity=Multiplicity(1, 1))
    }
)
Shop_Owner_Product: BinaryAssociation = BinaryAssociation(
    name="Shop_Owner_Product",
    ends={
        Property(name="Advertise44", type=Product, multiplicity=Multiplicity(1, 9999)),
        Property(name="Shop_Owner_Product_145", type=Shop_Owner, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="has12", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer13", type=Customer, multiplicity=Multiplicity(1, 1))
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
        Property(name="accnt17", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="payment18", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="account19", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order20", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment21", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Product_Account: BinaryAssociation = BinaryAssociation(
    name="Product_Account",
    ends={
        Property(name="account22", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="product23", type=Product, multiplicity=Multiplicity(1, 9999))
    }
)
Product_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Product_ShoppingCart",
    ends={
        Property(name="Add_to_cart24", type=ShoppingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="product25", type=Product, multiplicity=Multiplicity(1, 9999))
    }
)
ShoppingCart_Order: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Order",
    ends={
        Property(name="order26", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingCart27", type=ShoppingCart, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Account: BinaryAssociation = BinaryAssociation(
    name="Payment_Account",
    ends={
        Property(name="account28", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="payment29", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ZDS4AFK7Eeqesv9gci_YTQ",
    types={Customer, Payment, ShoppingCart, Account, Visitor, Order, LineItem, Product, MyActor_Actor, Admin_Actor, Webuser_Actor, AjoutProduit_UseCase, Administrator, Shop_Owner, Customer_Support},
    associations={association2, ShoppingCart_LineItem, Visitor_Product, Administrator_Customer, Administrator_Product, Vendors_Administrator, Vendors_Product, Account_ShoppingCart, LineItem_Product, Account_ShoppingCart2, WebUser_ShoppingCart, Customer_Support_Customer, WebUser_Customer, Shop_Owner_Product, Customer_Account, Order_LineItem, Account_Order, Account_Payment, Payment_Order, Product_Account, Product_ShoppingCart, ShoppingCart_Order, Payment_Account},
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