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
NO_Queue_mobile_application__App_User = Class(name="NO_Queue_mobile_application__App_User")
NO_Queue_mobile_application__Customer = Class(name="NO_Queue_mobile_application__Customer")
NO_Queue_mobile_application__Account = Class(name="NO_Queue_mobile_application__Account")
NO_Queue_mobile_application__Payment = Class(name="NO_Queue_mobile_application__Payment")
NO_Queue_mobile_application__Order = Class(name="NO_Queue_mobile_application__Order")
NO_Queue_mobile_application__Shopping_Cart = Class(name="NO_Queue_mobile_application__Shopping_Cart")
NO_Queue_mobile_application__Line_item = Class(name="NO_Queue_mobile_application__Line_item")
NO_Queue_mobile_application__Product = Class(name="NO_Queue_mobile_application__Product")
NO_Queue_mobile_application__NOQueue = Class(name="NO_Queue_mobile_application__NOQueue")

# NO_Queue_mobile_application__App_User class attributes and methods
NO_Queue_mobile_application__App_User_login_id: Property = Property(name="login_id", type=StringType)
NO_Queue_mobile_application__App_User_passwd: Property = Property(name="passwd", type=StringType)
NO_Queue_mobile_application__App_User.attributes={NO_Queue_mobile_application__App_User_passwd, NO_Queue_mobile_application__App_User_login_id}

# NO_Queue_mobile_application__Customer class attributes and methods
NO_Queue_mobile_application__Customer_ID: Property = Property(name="ID", type=StringType)
NO_Queue_mobile_application__Customer_Address: Property = Property(name="Address", type=StringType)
NO_Queue_mobile_application__Customer_Phone: Property = Property(name="Phone", type=StringType)
NO_Queue_mobile_application__Customer_Email: Property = Property(name="Email", type=StringType)
NO_Queue_mobile_application__Customer.attributes={NO_Queue_mobile_application__Customer_Address, NO_Queue_mobile_application__Customer_Email, NO_Queue_mobile_application__Customer_Phone, NO_Queue_mobile_application__Customer_ID}

# NO_Queue_mobile_application__Account class attributes and methods
NO_Queue_mobile_application__Account_ID: Property = Property(name="ID", type=StringType)
NO_Queue_mobile_application__Account_billing_address: Property = Property(name="billing_address", type=StringType)
NO_Queue_mobile_application__Account_is_closed: Property = Property(name="is_closed", type=BooleanType)
NO_Queue_mobile_application__Account_Open: Property = Property(name="Open", type=StringType)
NO_Queue_mobile_application__Account_Closed: Property = Property(name="Closed", type=StringType)
NO_Queue_mobile_application__Account.attributes={NO_Queue_mobile_application__Account_Open, NO_Queue_mobile_application__Account_is_closed, NO_Queue_mobile_application__Account_Closed, NO_Queue_mobile_application__Account_ID, NO_Queue_mobile_application__Account_billing_address}

# NO_Queue_mobile_application__Payment class attributes and methods
NO_Queue_mobile_application__Payment_ID: Property = Property(name="ID", type=StringType)
NO_Queue_mobile_application__Payment_Paid: Property = Property(name="Paid", type=StringType)
NO_Queue_mobile_application__Payment_Total: Property = Property(name="Total", type=StringType)
NO_Queue_mobile_application__Payment_Details: Property = Property(name="Details", type=StringType)
NO_Queue_mobile_application__Payment.attributes={NO_Queue_mobile_application__Payment_Paid, NO_Queue_mobile_application__Payment_Details, NO_Queue_mobile_application__Payment_Total, NO_Queue_mobile_application__Payment_ID}

# NO_Queue_mobile_application__Order class attributes and methods
NO_Queue_mobile_application__Order_Number: Property = Property(name="Number", type=StringType)
NO_Queue_mobile_application__Order_ordered: Property = Property(name="ordered", type=StringType)
NO_Queue_mobile_application__Order_shipped: Property = Property(name="shipped", type=StringType)
NO_Queue_mobile_application__Order_Ship_to: Property = Property(name="Ship_to", type=StringType)
NO_Queue_mobile_application__Order_status: Property = Property(name="status", type=StringType)
NO_Queue_mobile_application__Order_total: Property = Property(name="total", type=StringType)
NO_Queue_mobile_application__Order.attributes={NO_Queue_mobile_application__Order_total, NO_Queue_mobile_application__Order_ordered, NO_Queue_mobile_application__Order_Number, NO_Queue_mobile_application__Order_status, NO_Queue_mobile_application__Order_shipped, NO_Queue_mobile_application__Order_Ship_to}

# NO_Queue_mobile_application__Shopping_Cart class attributes and methods
NO_Queue_mobile_application__Shopping_Cart_created: Property = Property(name="created", type=StringType)
NO_Queue_mobile_application__Shopping_Cart.attributes={NO_Queue_mobile_application__Shopping_Cart_created}

# NO_Queue_mobile_application__Line_item class attributes and methods
NO_Queue_mobile_application__Line_item_quantity: Property = Property(name="quantity", type=IntegerType)
NO_Queue_mobile_application__Line_item_price: Property = Property(name="price", type=StringType)
NO_Queue_mobile_application__Line_item.attributes={NO_Queue_mobile_application__Line_item_price, NO_Queue_mobile_application__Line_item_quantity}

# NO_Queue_mobile_application__Product class attributes and methods
NO_Queue_mobile_application__Product_ID: Property = Property(name="ID", type=StringType)
NO_Queue_mobile_application__Product_Name: Property = Property(name="Name", type=StringType)
NO_Queue_mobile_application__Product_Supplier: Property = Property(name="Supplier", type=StringType)
NO_Queue_mobile_application__Product.attributes={NO_Queue_mobile_application__Product_ID, NO_Queue_mobile_application__Product_Supplier, NO_Queue_mobile_application__Product_Name}

# NO_Queue_mobile_application__NOQueue class attributes and methods
NO_Queue_mobile_application__NOQueue_APP_Details: Property = Property(name="APP_Details", type=StringType)
NO_Queue_mobile_application__NOQueue.attributes={NO_Queue_mobile_application__NOQueue_APP_Details}

# Relationships
Web_User_Customer: BinaryAssociation = BinaryAssociation(
    name="Web_User_Customer",
    ends={
        Property(name="customer0", type=NO_Queue_mobile_application__Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="web_User1", type=NO_Queue_mobile_application__App_User, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account2", type=NO_Queue_mobile_application__Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer3", type=NO_Queue_mobile_application__Customer, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Account: BinaryAssociation = BinaryAssociation(
    name="Payment_Account",
    ends={
        Property(name="account4", type=NO_Queue_mobile_application__Account, multiplicity=Multiplicity(1, 1)),
        Property(name="payment5", type=NO_Queue_mobile_application__Payment, multiplicity=Multiplicity(1, 9999))
    }
)
Web_User_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Web_User_Shopping_Cart",
    ends={
        Property(name="shopping_Cart6", type=NO_Queue_mobile_application__Shopping_Cart, multiplicity=Multiplicity(0, 1)),
        Property(name="web_User7", type=NO_Queue_mobile_application__App_User, multiplicity=Multiplicity(1, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order8", type=NO_Queue_mobile_application__Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="account9", type=NO_Queue_mobile_application__Account, multiplicity=Multiplicity(1, 1))
    }
)
Shopping_Cart_Line_item: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Line_item",
    ends={
        Property(name="ordered__unique10", type=NO_Queue_mobile_application__Line_item, multiplicity=Multiplicity(0, 9999)),
        Property(name="shopping_Cart11", type=NO_Queue_mobile_application__Shopping_Cart, multiplicity=Multiplicity(1, 1))
    }
)
Order_Line_item: BinaryAssociation = BinaryAssociation(
    name="Order_Line_item",
    ends={
        Property(name="line_item12", type=NO_Queue_mobile_application__Line_item, multiplicity=Multiplicity(0, 9999)),
        Property(name="_order__unique_13", type=NO_Queue_mobile_application__Order, multiplicity=Multiplicity(1, 1))
    }
)
Line_item_Product: BinaryAssociation = BinaryAssociation(
    name="Line_item_Product",
    ends={
        Property(name="product14", type=NO_Queue_mobile_application__Product, multiplicity=Multiplicity(1, 1)),
        Property(name="line_item15", type=NO_Queue_mobile_application__Line_item, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a084aca1_4f29_432c_a981_b9c2055a2da3",
    types={NO_Queue_mobile_application__App_User, NO_Queue_mobile_application__Customer, NO_Queue_mobile_application__Account, NO_Queue_mobile_application__Payment, NO_Queue_mobile_application__Order, NO_Queue_mobile_application__Shopping_Cart, NO_Queue_mobile_application__Line_item, NO_Queue_mobile_application__Product, NO_Queue_mobile_application__NOQueue},
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