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
Online_Shopping_System_Web_User = Class(name="Online_Shopping_System_Web_User")
Online_Shopping_System_Customer = Class(name="Online_Shopping_System_Customer")
Online_Shopping_System_Account = Class(name="Online_Shopping_System_Account")
Online_Shopping_System_Payment = Class(name="Online_Shopping_System_Payment")
Online_Shopping_System_Order = Class(name="Online_Shopping_System_Order")
Online_Shopping_System_Shopping_Cart = Class(name="Online_Shopping_System_Shopping_Cart")
Online_Shopping_System_Line_item = Class(name="Online_Shopping_System_Line_item")
Online_Shopping_System_Product = Class(name="Online_Shopping_System_Product")

# Online_Shopping_System_Web_User class attributes and methods
Online_Shopping_System_Web_User_passwd: Property = Property(name="passwd", type=StringType)
Online_Shopping_System_Web_User_login_id: Property = Property(name="login_id", type=StringType)
Online_Shopping_System_Web_User.attributes={Online_Shopping_System_Web_User_login_id, Online_Shopping_System_Web_User_passwd}

# Online_Shopping_System_Customer class attributes and methods
Online_Shopping_System_Customer_ID: Property = Property(name="ID", type=StringType)
Online_Shopping_System_Customer_Address: Property = Property(name="Address", type=StringType)
Online_Shopping_System_Customer_Phone: Property = Property(name="Phone", type=StringType)
Online_Shopping_System_Customer_Email: Property = Property(name="Email", type=StringType)
Online_Shopping_System_Customer.attributes={Online_Shopping_System_Customer_Email, Online_Shopping_System_Customer_Address, Online_Shopping_System_Customer_ID, Online_Shopping_System_Customer_Phone}

# Online_Shopping_System_Account class attributes and methods
Online_Shopping_System_Account_ID: Property = Property(name="ID", type=StringType)
Online_Shopping_System_Account_billing_address: Property = Property(name="billing_address", type=StringType)
Online_Shopping_System_Account_is_closed: Property = Property(name="is_closed", type=BooleanType)
Online_Shopping_System_Account_Open: Property = Property(name="Open", type=StringType)
Online_Shopping_System_Account_Closed: Property = Property(name="Closed", type=StringType)
Online_Shopping_System_Account.attributes={Online_Shopping_System_Account_Closed, Online_Shopping_System_Account_billing_address, Online_Shopping_System_Account_is_closed, Online_Shopping_System_Account_ID, Online_Shopping_System_Account_Open}

# Online_Shopping_System_Payment class attributes and methods
Online_Shopping_System_Payment_ID: Property = Property(name="ID", type=StringType)
Online_Shopping_System_Payment_Paid: Property = Property(name="Paid", type=StringType)
Online_Shopping_System_Payment_Total: Property = Property(name="Total", type=StringType)
Online_Shopping_System_Payment_Details: Property = Property(name="Details", type=StringType)
Online_Shopping_System_Payment.attributes={Online_Shopping_System_Payment_Paid, Online_Shopping_System_Payment_ID, Online_Shopping_System_Payment_Total, Online_Shopping_System_Payment_Details}

# Online_Shopping_System_Order class attributes and methods
Online_Shopping_System_Order_Number: Property = Property(name="Number", type=StringType)
Online_Shopping_System_Order_ordered: Property = Property(name="ordered", type=StringType)
Online_Shopping_System_Order_shipped: Property = Property(name="shipped", type=StringType)
Online_Shopping_System_Order_Ship_to: Property = Property(name="Ship_to", type=StringType)
Online_Shopping_System_Order_status: Property = Property(name="status", type=StringType)
Online_Shopping_System_Order_total: Property = Property(name="total", type=StringType)
Online_Shopping_System_Order.attributes={Online_Shopping_System_Order_total, Online_Shopping_System_Order_Ship_to, Online_Shopping_System_Order_status, Online_Shopping_System_Order_ordered, Online_Shopping_System_Order_Number, Online_Shopping_System_Order_shipped}

# Online_Shopping_System_Shopping_Cart class attributes and methods
Online_Shopping_System_Shopping_Cart_created: Property = Property(name="created", type=StringType)
Online_Shopping_System_Shopping_Cart.attributes={Online_Shopping_System_Shopping_Cart_created}

# Online_Shopping_System_Line_item class attributes and methods
Online_Shopping_System_Line_item_quantity: Property = Property(name="quantity", type=IntegerType)
Online_Shopping_System_Line_item_price: Property = Property(name="price", type=StringType)
Online_Shopping_System_Line_item.attributes={Online_Shopping_System_Line_item_quantity, Online_Shopping_System_Line_item_price}

# Online_Shopping_System_Product class attributes and methods
Online_Shopping_System_Product_ID: Property = Property(name="ID", type=StringType)
Online_Shopping_System_Product_Name: Property = Property(name="Name", type=StringType)
Online_Shopping_System_Product_Supplier: Property = Property(name="Supplier", type=StringType)
Online_Shopping_System_Product.attributes={Online_Shopping_System_Product_ID, Online_Shopping_System_Product_Name, Online_Shopping_System_Product_Supplier}

# Relationships
Web_User_Customer: BinaryAssociation = BinaryAssociation(
    name="Web_User_Customer",
    ends={
        Property(name="customer0", type=Online_Shopping_System_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="web_User1", type=Online_Shopping_System_Web_User, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account2", type=Online_Shopping_System_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer3", type=Online_Shopping_System_Customer, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Account: BinaryAssociation = BinaryAssociation(
    name="Payment_Account",
    ends={
        Property(name="account4", type=Online_Shopping_System_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="payment5", type=Online_Shopping_System_Payment, multiplicity=Multiplicity(1, 9999))
    }
)
Web_User_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Web_User_Shopping_Cart",
    ends={
        Property(name="shopping_Cart6", type=Online_Shopping_System_Shopping_Cart, multiplicity=Multiplicity(0, 1)),
        Property(name="web_User7", type=Online_Shopping_System_Web_User, multiplicity=Multiplicity(1, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order8", type=Online_Shopping_System_Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="account9", type=Online_Shopping_System_Account, multiplicity=Multiplicity(1, 1))
    }
)
Shopping_Cart_Line_item: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Line_item",
    ends={
        Property(name="ordered__unique10", type=Online_Shopping_System_Line_item, multiplicity=Multiplicity(0, 9999)),
        Property(name="shopping_Cart11", type=Online_Shopping_System_Shopping_Cart, multiplicity=Multiplicity(1, 1))
    }
)
Order_Line_item: BinaryAssociation = BinaryAssociation(
    name="Order_Line_item",
    ends={
        Property(name="line_item12", type=Online_Shopping_System_Line_item, multiplicity=Multiplicity(0, 9999)),
        Property(name="_order__unique_13", type=Online_Shopping_System_Order, multiplicity=Multiplicity(1, 1))
    }
)
Line_item_Product: BinaryAssociation = BinaryAssociation(
    name="Line_item_Product",
    ends={
        Property(name="product14", type=Online_Shopping_System_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="line_item15", type=Online_Shopping_System_Line_item, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6ebaa76d_d77e_4880_8aa6_96b6f56d9c5b",
    types={Online_Shopping_System_Web_User, Online_Shopping_System_Customer, Online_Shopping_System_Account, Online_Shopping_System_Payment, Online_Shopping_System_Order, Online_Shopping_System_Shopping_Cart, Online_Shopping_System_Line_item, Online_Shopping_System_Product},
    associations={Web_User_Customer, Customer_Account, Payment_Account, Web_User_Shopping_Cart, Account_Order, Shopping_Cart_Line_item, Order_Line_item, Line_item_Product},
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