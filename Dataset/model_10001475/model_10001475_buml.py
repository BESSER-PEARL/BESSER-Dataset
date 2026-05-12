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
Customer_Actor = Class(name="Customer_Actor")
Login_UseCase = Class(name="Login_UseCase")
Register_UseCase = Class(name="Register_UseCase")
Authentication_UseCase = Class(name="Authentication_UseCase")
Points_and_Special_Offers_UseCase = Class(name="Points_and_Special_Offers_UseCase")
Checkout_UseCase = Class(name="Checkout_UseCase")
Payment_UseCase = Class(name="Payment_UseCase")
View_Items_UseCase = Class(name="View_Items_UseCase")
Move_items_into_basket_UseCase = Class(name="Move_items_into_basket_UseCase")
PayPal_Mastercard_etc_UseCase = Class(name="PayPal_Mastercard_etc_UseCase")
Search_for_items_UseCase = Class(name="Search_for_items_UseCase")
Browse_catalogue_UseCase = Class(name="Browse_catalogue_UseCase")
View_Items_UseCase1 = Class(name="View_Items_UseCase1")
View_recommended_items_UseCase = Class(name="View_recommended_items_UseCase")
Add_items_to_shopping_cart_UseCase = Class(name="Add_items_to_shopping_cart_UseCase")
Save_items_for_later_UseCase = Class(name="Save_items_for_later_UseCase")
UseCase_UseCase = Class(name="UseCase_UseCase")
Checkout_UseCase1 = Class(name="Checkout_UseCase1")
Customer_authentication_UseCase = Class(name="Customer_authentication_UseCase")
Credit_payment_service_Actor = Class(name="Credit_payment_service_Actor")
Customer_Actor1 = Class(name="Customer_Actor1")
User_authentication_cookie__UseCase = Class(name="User_authentication_cookie__UseCase")
Credit__shop_credit_card_or_PayPal_payments_UseCase = Class(name="Credit__shop_credit_card_or_PayPal_payments_UseCase")
Authentication_Service_or_identity_provider_Actor = Class(name="Authentication_Service_or_identity_provider_Actor")
Payment_UseCase1 = Class(name="Payment_UseCase1")
Bank_Actor = Class(name="Bank_Actor")
login_or_sign_in_page_UseCase = Class(name="login_or_sign_in_page_UseCase")
Customer_Actor2 = Class(name="Customer_Actor2")
Online_Shopping_Card_Payment = Class(name="Online_Shopping_Card_Payment")
Online_Shopping_Paypal_Payment = Class(name="Online_Shopping_Paypal_Payment")
Online_Shopping_Checkout = Class(name="Online_Shopping_Checkout")
Online_Shopping_Item = Class(name="Online_Shopping_Item")
Online_Shopping_Shopping_Cart = Class(name="Online_Shopping_Shopping_Cart")
Online_Shopping_Customer_Account = Class(name="Online_Shopping_Customer_Account")
Online_Shopping_Shopping_Cart_Item = Class(name="Online_Shopping_Shopping_Cart_Item")
Online_Shopping_Order_Item = Class(name="Online_Shopping_Order_Item")
Online_Shopping_Points___Special_Offers = Class(name="Online_Shopping_Points___Special_Offers")
Online_Shopping_Order = Class(name="Online_Shopping_Order")
str = Class(name="str")

# Customer_Actor class attributes and methods

# Login_UseCase class attributes and methods

# Register_UseCase class attributes and methods

# Authentication_UseCase class attributes and methods

# Points_and_Special_Offers_UseCase class attributes and methods

# Checkout_UseCase class attributes and methods

# Payment_UseCase class attributes and methods

# View_Items_UseCase class attributes and methods

# Move_items_into_basket_UseCase class attributes and methods

# PayPal_Mastercard_etc_UseCase class attributes and methods

# Search_for_items_UseCase class attributes and methods

# Browse_catalogue_UseCase class attributes and methods

# View_Items_UseCase1 class attributes and methods

# View_recommended_items_UseCase class attributes and methods

# Add_items_to_shopping_cart_UseCase class attributes and methods

# Save_items_for_later_UseCase class attributes and methods

# UseCase_UseCase class attributes and methods

# Checkout_UseCase1 class attributes and methods

# Customer_authentication_UseCase class attributes and methods

# Credit_payment_service_Actor class attributes and methods

# Customer_Actor1 class attributes and methods

# User_authentication_cookie__UseCase class attributes and methods

# Credit__shop_credit_card_or_PayPal_payments_UseCase class attributes and methods

# Authentication_Service_or_identity_provider_Actor class attributes and methods

# Payment_UseCase1 class attributes and methods

# Bank_Actor class attributes and methods

# login_or_sign_in_page_UseCase class attributes and methods

# Customer_Actor2 class attributes and methods

# Online_Shopping_Card_Payment class attributes and methods
Online_Shopping_Card_Payment_Card_Holder_Name: Property = Property(name="Card_Holder_Name", type=StringType)
Online_Shopping_Card_Payment_Valid_Date: Property = Property(name="Valid_Date", type=StringType)
Online_Shopping_Card_Payment_Card_Number: Property = Property(name="Card_Number", type=IntegerType)
Online_Shopping_Card_Payment_CVS_Number: Property = Property(name="CVS_Number", type=IntegerType)
Online_Shopping_Card_Payment.attributes={Online_Shopping_Card_Payment_Card_Holder_Name, Online_Shopping_Card_Payment_Card_Number, Online_Shopping_Card_Payment_Valid_Date, Online_Shopping_Card_Payment_CVS_Number}

# Online_Shopping_Paypal_Payment class attributes and methods
Online_Shopping_Paypal_Payment_Username: Property = Property(name="Username", type=StringType)
Online_Shopping_Paypal_Payment_Password: Property = Property(name="Password", type=StringType)
Online_Shopping_Paypal_Payment.attributes={Online_Shopping_Paypal_Payment_Password, Online_Shopping_Paypal_Payment_Username}

# Online_Shopping_Checkout class attributes and methods
Online_Shopping_Checkout_Billing_Address: Property = Property(name="Billing_Address", type=StringType)
Online_Shopping_Checkout_Delivery_Address: Property = Property(name="Delivery_Address", type=StringType)
Online_Shopping_Checkout_Phone_Number: Property = Property(name="Phone_Number", type=IntegerType)
Online_Shopping_Checkout_Email_Address: Property = Property(name="Email_Address", type=StringType)
Online_Shopping_Checkout.attributes={Online_Shopping_Checkout_Phone_Number, Online_Shopping_Checkout_Email_Address, Online_Shopping_Checkout_Delivery_Address, Online_Shopping_Checkout_Billing_Address}

# Online_Shopping_Item class attributes and methods
Online_Shopping_Item_Name: Property = Property(name="Name", type=StringType)
Online_Shopping_Item_Product_ID: Property = Property(name="Product_ID", type=StringType)
Online_Shopping_Item_Description: Property = Property(name="Description", type=StringType)
Online_Shopping_Item_Price: Property = Property(name="Price", type=IntegerType)
Online_Shopping_Item.attributes={Online_Shopping_Item_Price, Online_Shopping_Item_Description, Online_Shopping_Item_Name, Online_Shopping_Item_Product_ID}

# Online_Shopping_Shopping_Cart class attributes and methods
Online_Shopping_Shopping_Cart_Is_Empty: Property = Property(name="Is_Empty", type=BooleanType)
Online_Shopping_Shopping_Cart_Contents: Property = Property(name="Contents", type=Online_Shopping_Shopping_Cart_Item)
Online_Shopping_Shopping_Cart.attributes={Online_Shopping_Shopping_Cart_Is_Empty, Online_Shopping_Shopping_Cart_Contents}

# Online_Shopping_Customer_Account class attributes and methods
Online_Shopping_Customer_Account_Username: Property = Property(name="Username", type=StringType)
Online_Shopping_Customer_Account_Password: Property = Property(name="Password", type=StringType)
Online_Shopping_Customer_Account.attributes={Online_Shopping_Customer_Account_Username, Online_Shopping_Customer_Account_Password}

# Online_Shopping_Shopping_Cart_Item class attributes and methods
Online_Shopping_Shopping_Cart_Item_Price: Property = Property(name="Price", type=IntegerType)
Online_Shopping_Shopping_Cart_Item_Quantity: Property = Property(name="Quantity", type=StringType)
Online_Shopping_Shopping_Cart_Item.attributes={Online_Shopping_Shopping_Cart_Item_Quantity, Online_Shopping_Shopping_Cart_Item_Price}

# Online_Shopping_Order_Item class attributes and methods
Online_Shopping_Order_Item_Product_ID: Property = Property(name="Product_ID", type=StringType)
Online_Shopping_Order_Item_Quantity: Property = Property(name="Quantity", type=IntegerType)
Online_Shopping_Order_Item_SubTotal: Property = Property(name="SubTotal", type=StringType)
Online_Shopping_Order_Item.attributes={Online_Shopping_Order_Item_Quantity, Online_Shopping_Order_Item_SubTotal, Online_Shopping_Order_Item_Product_ID}

# Online_Shopping_Points___Special_Offers class attributes and methods
Online_Shopping_Points___Special_Offers_Discount: Property = Property(name="Discount", type=IntegerType)
Online_Shopping_Points___Special_Offers.attributes={Online_Shopping_Points___Special_Offers_Discount}

# Online_Shopping_Order class attributes and methods
Online_Shopping_Order_Placed_Date: Property = Property(name="Placed_Date", type=StringType)
Online_Shopping_Order_Contents: Property = Property(name="Contents", type=Online_Shopping_Order_Item)
Online_Shopping_Order.attributes={Online_Shopping_Order_Placed_Date, Online_Shopping_Order_Contents}

# str class attributes and methods

# Relationships
Order_Order_Item: BinaryAssociation = BinaryAssociation(
    name="Order_Order_Item",
    ends={
        Property(name="Order47", type=Online_Shopping_Order, multiplicity=Multiplicity(0, 1)),
        Property(name="order_Item46", type=Online_Shopping_Order_Item, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Registered: BinaryAssociation = BinaryAssociation(
    name="Customer_Registered",
    ends={
        Property(name="registered0", type=Register_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login2", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Move_items_into_basket_View_Items: BinaryAssociation = BinaryAssociation(
    name="Move_items_into_basket_View_Items",
    ends={
        Property(name="view_Items4", type=View_Items_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="move_items_into_basket5", type=Move_items_into_basket_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Move_items_into_basket_Checkout: BinaryAssociation = BinaryAssociation(
    name="Move_items_into_basket_Checkout",
    ends={
        Property(name="checkout6", type=Checkout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="move_items_into_basket7", type=Move_items_into_basket_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Points_and_Special_Offers_Checkout: BinaryAssociation = BinaryAssociation(
    name="Points_and_Special_Offers_Checkout",
    ends={
        Property(name="checkout8", type=Checkout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="points_and_Special_Offers9", type=Points_and_Special_Offers_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_Payment: BinaryAssociation = BinaryAssociation(
    name="Checkout_Payment",
    ends={
        Property(name="payment10", type=Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout11", type=Checkout_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Credit_payment_service: BinaryAssociation = BinaryAssociation(
    name="Payment_Credit_payment_service",
    ends={
        Property(name="credit_payment_service12", type=Credit_payment_service_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="payment13", type=Payment_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
login_or_sign_in_page__Authentication_Service_or_identity_provider: BinaryAssociation = BinaryAssociation(
    name="login_or_sign_in_page__Authentication_Service_or_identity_provider",
    ends={
        Property(name="Authentication_Service_or_identity_provider14", type=Authentication_Service_or_identity_provider_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login_or_sign_in_page15", type=login_or_sign_in_page_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
User_authentication_cookie___Authentication_Service_or_identity_provider: BinaryAssociation = BinaryAssociation(
    name="User_authentication_cookie___Authentication_Service_or_identity_provider",
    ends={
        Property(name="Authentication_Service_or_identity_provider16", type=Authentication_Service_or_identity_provider_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="user_authentication_cookie17", type=User_authentication_cookie__UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Credit__shop_credit_card_or_PayPal_payments_Bank: BinaryAssociation = BinaryAssociation(
    name="Credit__shop_credit_card_or_PayPal_payments_Bank",
    ends={
        Property(name="bank18", type=Bank_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="credit__shop_credit_card_or_PayPal_payments19", type=Credit__shop_credit_card_or_PayPal_payments_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_authentication_Customer: BinaryAssociation = BinaryAssociation(
    name="Customer_authentication_Customer",
    ends={
        Property(name="customer20", type=Customer_Actor1, multiplicity=Multiplicity(0, 1)),
        Property(name="customer_authentication21", type=Customer_authentication_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Checkout: BinaryAssociation = BinaryAssociation(
    name="Customer_Checkout",
    ends={
        Property(name="checkout22", type=Checkout_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="customer23", type=Customer_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Save_items_for_later_Customer: BinaryAssociation = BinaryAssociation(
    name="Save_items_for_later_Customer",
    ends={
        Property(name="customer24", type=Customer_Actor2, multiplicity=Multiplicity(0, 1)),
        Property(name="save_items_for_later25", type=Save_items_for_later_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Add_items_to_shopping_cart_Customer: BinaryAssociation = BinaryAssociation(
    name="Add_items_to_shopping_cart_Customer",
    ends={
        Property(name="customer26", type=Customer_Actor2, multiplicity=Multiplicity(0, 1)),
        Property(name="add_items_to_shopping_cart27", type=Add_items_to_shopping_cart_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account_Points___Special_Offers: BinaryAssociation = BinaryAssociation(
    name="Customer_Account_Points___Special_Offers",
    ends={
        Property(name="points___Special_Offers28", type=Online_Shopping_Points___Special_Offers, multiplicity=Multiplicity(0, 1)),
        Property(name="customer_Account29", type=Online_Shopping_Customer_Account, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account_Item: BinaryAssociation = BinaryAssociation(
    name="Customer_Account_Item",
    ends={
        Property(name="item30", type=Online_Shopping_Item, multiplicity=Multiplicity(0, 1)),
        Property(name="customer_Account31", type=Online_Shopping_Customer_Account, multiplicity=Multiplicity(0, 1))
    }
)
Item_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Item_Shopping_Cart",
    ends={
        Property(name="shopping_Cart32", type=Online_Shopping_Shopping_Cart, multiplicity=Multiplicity(0, 1)),
        Property(name="item33", type=Online_Shopping_Item, multiplicity=Multiplicity(0, 1))
    }
)
Shopping_Cart_Shopping_Cart_Item: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Shopping_Cart_Item",
    ends={
        Property(name="shopping_Cart_Item34", type=Online_Shopping_Shopping_Cart_Item, multiplicity=Multiplicity(0, 1)),
        Property(name="shopping_Cart35", type=Online_Shopping_Shopping_Cart, multiplicity=Multiplicity(0, 1))
    }
)
Shopping_Cart_Checkout: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Checkout",
    ends={
        Property(name="checkout36", type=Online_Shopping_Checkout, multiplicity=Multiplicity(0, 1)),
        Property(name="shopping_Cart37", type=Online_Shopping_Shopping_Cart, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_Card_Payment: BinaryAssociation = BinaryAssociation(
    name="Checkout_Card_Payment",
    ends={
        Property(name="card_Payment38", type=Online_Shopping_Card_Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout39", type=Online_Shopping_Checkout, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_Paypal_Payment: BinaryAssociation = BinaryAssociation(
    name="Checkout_Paypal_Payment",
    ends={
        Property(name="paypal_Payment40", type=Online_Shopping_Paypal_Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout41", type=Online_Shopping_Checkout, multiplicity=Multiplicity(0, 1))
    }
)
Card_Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Card_Payment_Order",
    ends={
        Property(name="order42", type=Online_Shopping_Order, multiplicity=Multiplicity(0, 1)),
        Property(name="card_Payment43", type=Online_Shopping_Card_Payment, multiplicity=Multiplicity(0, 1))
    }
)
Paypal_Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Paypal_Payment_Order",
    ends={
        Property(name="order44", type=Online_Shopping_Order, multiplicity=Multiplicity(0, 1)),
        Property(name="paypal_Payment45", type=Online_Shopping_Paypal_Payment, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9TBCsHGUEemkSo3PkdMxbg",
    types={Customer_Actor, Login_UseCase, Register_UseCase, Authentication_UseCase, Points_and_Special_Offers_UseCase, Checkout_UseCase, Payment_UseCase, View_Items_UseCase, Move_items_into_basket_UseCase, PayPal_Mastercard_etc_UseCase, Search_for_items_UseCase, Browse_catalogue_UseCase, View_Items_UseCase1, View_recommended_items_UseCase, Add_items_to_shopping_cart_UseCase, Save_items_for_later_UseCase, UseCase_UseCase, Checkout_UseCase1, Customer_authentication_UseCase, Credit_payment_service_Actor, Customer_Actor1, User_authentication_cookie__UseCase, Credit__shop_credit_card_or_PayPal_payments_UseCase, Authentication_Service_or_identity_provider_Actor, Payment_UseCase1, Bank_Actor, login_or_sign_in_page_UseCase, Customer_Actor2, Online_Shopping_Card_Payment, Online_Shopping_Paypal_Payment, Online_Shopping_Checkout, Online_Shopping_Item, Online_Shopping_Shopping_Cart, Online_Shopping_Customer_Account, Online_Shopping_Shopping_Cart_Item, Online_Shopping_Order_Item, Online_Shopping_Points___Special_Offers, Online_Shopping_Order, str},
    associations={Order_Order_Item, Customer_Registered, Customer_Login, Move_items_into_basket_View_Items, Move_items_into_basket_Checkout, Points_and_Special_Offers_Checkout, Checkout_Payment, Payment_Credit_payment_service, login_or_sign_in_page__Authentication_Service_or_identity_provider, User_authentication_cookie___Authentication_Service_or_identity_provider, Credit__shop_credit_card_or_PayPal_payments_Bank, Customer_authentication_Customer, Customer_Checkout, Save_items_for_later_Customer, Add_items_to_shopping_cart_Customer, Customer_Account_Points___Special_Offers, Customer_Account_Item, Item_Shopping_Cart, Shopping_Cart_Shopping_Cart_Item, Shopping_Cart_Checkout, Checkout_Card_Payment, Checkout_Paypal_Payment, Card_Payment_Order, Paypal_Payment_Order},
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