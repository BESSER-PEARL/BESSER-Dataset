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
ShoppingCartExample_ShoppingCart = Class(name="ShoppingCartExample_ShoppingCart")
ShoppingCartExample_Order = Class(name="ShoppingCartExample_Order")
ShoppingCartExample_LineItem = Class(name="ShoppingCartExample_LineItem")
ShoppingCartExample_Account = Class(name="ShoppingCartExample_Account")
ShoppingCartExample_Customer = Class(name="ShoppingCartExample_Customer")
Register_UseCase = Class(name="Register_UseCase")
Customer_Actor = Class(name="Customer_Actor")
Login_UseCase = Class(name="Login_UseCase")
View_Dashboard_UseCase = Class(name="View_Dashboard_UseCase")
View_Static_Content_UseCase = Class(name="View_Static_Content_UseCase")
Top_UP_via_card_voucher_UseCase = Class(name="Top_UP_via_card_voucher_UseCase")
Purchase_Credit_UseCase = Class(name="Purchase_Credit_UseCase")
Payment_express_Actor = Class(name="Payment_express_Actor")
Digitalk_Actor = Class(name="Digitalk_Actor")

# ShoppingCartExample_ShoppingCart class attributes and methods
ShoppingCartExample_ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppingCartExample_ShoppingCart.attributes={ShoppingCartExample_ShoppingCart_creationDate}

# ShoppingCartExample_Order class attributes and methods
ShoppingCartExample_Order_id: Property = Property(name="id", type=IntegerType)
ShoppingCartExample_Order.attributes={ShoppingCartExample_Order_id}

# ShoppingCartExample_LineItem class attributes and methods
ShoppingCartExample_LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
ShoppingCartExample_LineItem_price: Property = Property(name="price", type=IntegerType)
ShoppingCartExample_LineItem.attributes={ShoppingCartExample_LineItem_quantity, ShoppingCartExample_LineItem_price}

# ShoppingCartExample_Account class attributes and methods
ShoppingCartExample_Account_id: Property = Property(name="id", type=IntegerType)
ShoppingCartExample_Account.attributes={ShoppingCartExample_Account_id}

# ShoppingCartExample_Customer class attributes and methods

# Register_UseCase class attributes and methods

# Customer_Actor class attributes and methods

# Login_UseCase class attributes and methods

# View_Dashboard_UseCase class attributes and methods

# View_Static_Content_UseCase class attributes and methods

# Top_UP_via_card_voucher_UseCase class attributes and methods

# Purchase_Credit_UseCase class attributes and methods

# Payment_express_Actor class attributes and methods

# Digitalk_Actor class attributes and methods

# Relationships
Account_Customer: BinaryAssociation = BinaryAssociation(
    name="Account_Customer",
    ends={
        Property(name="customer6", type=ShoppingCartExample_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="account7", type=ShoppingCartExample_Account, multiplicity=Multiplicity(1, 1))
    }
)
Customer_CSR_Register: BinaryAssociation = BinaryAssociation(
    name="Customer_CSR_Register",
    ends={
        Property(name="register8", type=Register_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer_CSR9", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Payment_express_Purchase_Credit: BinaryAssociation = BinaryAssociation(
    name="Payment_express_Purchase_Credit",
    ends={
        Property(name="purchase_Credit10", type=Purchase_Credit_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="payment_express11", type=Payment_express_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Top_UP_via_card_voucher_Digitalk: BinaryAssociation = BinaryAssociation(
    name="Top_UP_via_card_voucher_Digitalk",
    ends={
        Property(name="digitalk12", type=Digitalk_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="top_UP_via_card_voucher13", type=Top_UP_via_card_voucher_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Purchase_Credit_Digitalk: BinaryAssociation = BinaryAssociation(
    name="Purchase_Credit_Digitalk",
    ends={
        Property(name="digitalk14", type=Digitalk_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="purchase_Credit15", type=Purchase_Credit_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_View_Static_Content: BinaryAssociation = BinaryAssociation(
    name="Customer_View_Static_Content",
    ends={
        Property(name="view_Static_Content16", type=View_Static_Content_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer17", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login18", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer19", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Top_UP_via_card_voucher: BinaryAssociation = BinaryAssociation(
    name="Customer_Top_UP_via_card_voucher",
    ends={
        Property(name="top_UP_via_card_voucher20", type=Top_UP_via_card_voucher_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer21", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_View_Dashboard: BinaryAssociation = BinaryAssociation(
    name="Customer_View_Dashboard",
    ends={
        Property(name="view_Dashboard22", type=View_Dashboard_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer23", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Purchase_Credit: BinaryAssociation = BinaryAssociation(
    name="Customer_Purchase_Credit",
    ends={
        Property(name="purchase_Credit24", type=Purchase_Credit_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer25", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
View_Dashboard_Digitalk: BinaryAssociation = BinaryAssociation(
    name="View_Dashboard_Digitalk",
    ends={
        Property(name="digitalk26", type=Digitalk_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_Dashboard27", type=View_Dashboard_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Register_Digitalk: BinaryAssociation = BinaryAssociation(
    name="Register_Digitalk",
    ends={
        Property(name="digitalk28", type=Digitalk_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="register29", type=Register_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Order_Line: BinaryAssociation = BinaryAssociation(
    name="Order_Line",
    ends={
        Property(name="items0", type=ShoppingCartExample_LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="order1", type=ShoppingCartExample_Order, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_Order: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Order",
    ends={
        Property(name="order2", type=ShoppingCartExample_Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="c3", type=ShoppingCartExample_ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart4", type=ShoppingCartExample_ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account5", type=ShoppingCartExample_Account, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_249054a1_d65a_4a88_9c67_c97eae5a3d55",
    types={ShoppingCartExample_ShoppingCart, ShoppingCartExample_Order, ShoppingCartExample_LineItem, ShoppingCartExample_Account, ShoppingCartExample_Customer, Register_UseCase, Customer_Actor, Login_UseCase, View_Dashboard_UseCase, View_Static_Content_UseCase, Top_UP_via_card_voucher_UseCase, Purchase_Credit_UseCase, Payment_express_Actor, Digitalk_Actor},
    associations={Account_Customer, Customer_CSR_Register, Payment_express_Purchase_Credit, Top_UP_via_card_voucher_Digitalk, Purchase_Credit_Digitalk, Customer_View_Static_Content, Customer_Login, Customer_Top_UP_via_card_voucher, Customer_View_Dashboard, Customer_Purchase_Credit, View_Dashboard_Digitalk, Register_Digitalk, Order_Line, ShoppingCart_Order, Account_ShoppingCart},
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