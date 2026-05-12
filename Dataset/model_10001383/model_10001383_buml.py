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

# Enumerations
Online_Shopping_Or: Enumeration = Enumeration(
    name="Online_Shopping_Or",
    literals={
            
    }
)

Integer: Enumeration = Enumeration(
    name="Integer",
    literals={
            
    }
)

# Classes
Customer_Actor = Class(name="Customer_Actor")
register_UseCase = Class(name="register_UseCase")
Login_UseCase = Class(name="Login_UseCase")
Authentication_UseCase = Class(name="Authentication_UseCase")
view_items_UseCase = Class(name="view_items_UseCase")
make_a_purchase_UseCase = Class(name="make_a_purchase_UseCase")
claim_some_points_UseCase = Class(name="claim_some_points_UseCase")
special_offers_UseCase = Class(name="special_offers_UseCase")
payment_UseCase = Class(name="payment_UseCase")
PayPal__Mastercard__etc__UseCase = Class(name="PayPal__Mastercard__etc__UseCase")
Choose_items_UseCase = Class(name="Choose_items_UseCase")
View_items_UseCase = Class(name="View_items_UseCase")
Search_for_items_UseCase = Class(name="Search_for_items_UseCase")
browse_catalogue_UseCase = Class(name="browse_catalogue_UseCase")
view_recommended_items_UseCase = Class(name="view_recommended_items_UseCase")
add_items_to_shopping_cart_UseCase = Class(name="add_items_to_shopping_cart_UseCase")
save_items_for_later_in_wish_list_UseCase = Class(name="save_items_for_later_in_wish_list_UseCase")
Checkout_UseCase = Class(name="Checkout_UseCase")
Checkout_UseCase1 = Class(name="Checkout_UseCase1")
Customer_authentication__UseCase = Class(name="Customer_authentication__UseCase")
Log_in__sign_in_page_UseCase = Class(name="Log_in__sign_in_page_UseCase")
user_authentication_cookie_UseCase = Class(name="user_authentication_cookie_UseCase")
Credit_payment_service_Actor = Class(name="Credit_payment_service_Actor")
Authentication_or_service_or_identity_provider_Actor = Class(name="Authentication_or_service_or_identity_provider_Actor")
Payment_UseCase = Class(name="Payment_UseCase")
Online_customer_Actor = Class(name="Online_customer_Actor")
credit_card__shop_card__PayPal_UseCase = Class(name="credit_card__shop_card__PayPal_UseCase")
bank__Actor = Class(name="bank__Actor")
Customer_Actor1 = Class(name="Customer_Actor1")
_unnamed = Class(name="_unnamed")
Online_Shopping_Card_payment = Class(name="Online_Shopping_Card_payment")
Online_Shopping_PayPal_payment = Class(name="Online_Shopping_PayPal_payment")
Online_Shopping_Item = Class(name="Online_Shopping_Item")
Online_Shopping_Checkout = Class(name="Online_Shopping_Checkout")
Online_Shopping_Basket = Class(name="Online_Shopping_Basket")
Online_Shopping_BasketItem = Class(name="Online_Shopping_BasketItem")
Online_Shopping_Order = Class(name="Online_Shopping_Order")
Online_Shopping_Orderstate = Class(name="Online_Shopping_Orderstate")
Online_Shopping_Special_offers = Class(name="Online_Shopping_Special_offers")
Online_Shopping_Customer_points = Class(name="Online_Shopping_Customer_points")
Online_Shopping_Customer = Class(name="Online_Shopping_Customer")
Online_Shopping_Orderitem = Class(name="Online_Shopping_Orderitem")

# Customer_Actor class attributes and methods

# register_UseCase class attributes and methods

# Login_UseCase class attributes and methods

# Authentication_UseCase class attributes and methods

# view_items_UseCase class attributes and methods

# make_a_purchase_UseCase class attributes and methods

# claim_some_points_UseCase class attributes and methods

# special_offers_UseCase class attributes and methods

# payment_UseCase class attributes and methods

# PayPal__Mastercard__etc__UseCase class attributes and methods

# Choose_items_UseCase class attributes and methods

# View_items_UseCase class attributes and methods

# Search_for_items_UseCase class attributes and methods

# browse_catalogue_UseCase class attributes and methods

# view_recommended_items_UseCase class attributes and methods

# add_items_to_shopping_cart_UseCase class attributes and methods

# save_items_for_later_in_wish_list_UseCase class attributes and methods

# Checkout_UseCase class attributes and methods

# Checkout_UseCase1 class attributes and methods

# Customer_authentication__UseCase class attributes and methods

# Log_in__sign_in_page_UseCase class attributes and methods

# user_authentication_cookie_UseCase class attributes and methods

# Credit_payment_service_Actor class attributes and methods

# Authentication_or_service_or_identity_provider_Actor class attributes and methods

# Payment_UseCase class attributes and methods

# Online_customer_Actor class attributes and methods

# credit_card__shop_card__PayPal_UseCase class attributes and methods

# bank__Actor class attributes and methods

# Customer_Actor1 class attributes and methods

# _unnamed class attributes and methods

# Online_Shopping_Card_payment class attributes and methods
Online_Shopping_Card_payment_payment_type: Property = Property(name="payment_type", type=StringType)
Online_Shopping_Card_payment_Card_number: Property = Property(name="Card_number", type=IntegerType)
Online_Shopping_Card_payment_Cardholder_name: Property = Property(name="Cardholder_name", type=StringType)
Online_Shopping_Card_payment_Valid_date: Property = Property(name="Valid_date", type=IntegerType)
Online_Shopping_Card_payment_CVS_number: Property = Property(name="CVS_number", type=IntegerType)
Online_Shopping_Card_payment.attributes={Online_Shopping_Card_payment_Cardholder_name, Online_Shopping_Card_payment_CVS_number, Online_Shopping_Card_payment_payment_type, Online_Shopping_Card_payment_Valid_date, Online_Shopping_Card_payment_Card_number}

# Online_Shopping_PayPal_payment class attributes and methods
Online_Shopping_PayPal_payment_Username: Property = Property(name="Username", type=StringType)
Online_Shopping_PayPal_payment_attribute: Property = Property(name="attribute", type=StringType)
Online_Shopping_PayPal_payment_Password: Property = Property(name="Password", type=StringType)
Online_Shopping_PayPal_payment.attributes={Online_Shopping_PayPal_payment_attribute, Online_Shopping_PayPal_payment_Password, Online_Shopping_PayPal_payment_Username}

# Online_Shopping_Item class attributes and methods
Online_Shopping_Item_ProductID: Property = Property(name="ProductID", type=StringType)
Online_Shopping_Item_Name: Property = Property(name="Name", type=StringType)
Online_Shopping_Item_Description: Property = Property(name="Description", type=StringType)
Online_Shopping_Item_Price: Property = Property(name="Price", type=IntegerType)
Online_Shopping_Item.attributes={Online_Shopping_Item_Price, Online_Shopping_Item_Description, Online_Shopping_Item_Name, Online_Shopping_Item_ProductID}

# Online_Shopping_Checkout class attributes and methods
Online_Shopping_Checkout_Billing_address: Property = Property(name="Billing_address", type=StringType)
Online_Shopping_Checkout_Checkout_address: Property = Property(name="Checkout_address", type=StringType)
Online_Shopping_Checkout_Phone_number: Property = Property(name="Phone_number", type=IntegerType)
Online_Shopping_Checkout_Email_address: Property = Property(name="Email_address", type=StringType)
Online_Shopping_Checkout.attributes={Online_Shopping_Checkout_Phone_number, Online_Shopping_Checkout_Billing_address, Online_Shopping_Checkout_Email_address, Online_Shopping_Checkout_Checkout_address}

# Online_Shopping_Basket class attributes and methods
Online_Shopping_Basket_IsEmpty: Property = Property(name="IsEmpty", type=BooleanType)
Online_Shopping_Basket_attribute: Property = Property(name="attribute", type=StringType)
Online_Shopping_Basket_Contents: Property = Property(name="Contents", type=Online_Shopping_BasketItem)
Online_Shopping_Basket.attributes={Online_Shopping_Basket_IsEmpty, Online_Shopping_Basket_attribute, Online_Shopping_Basket_Contents}

# Online_Shopping_BasketItem class attributes and methods
Online_Shopping_BasketItem_Quantity: Property = Property(name="Quantity", type=IntegerType)
Online_Shopping_BasketItem_ProductID: Property = Property(name="ProductID", type=StringType)
Online_Shopping_BasketItem.attributes={Online_Shopping_BasketItem_ProductID, Online_Shopping_BasketItem_Quantity}

# Online_Shopping_Order class attributes and methods
Online_Shopping_Order_Placed_Date: Property = Property(name="Placed_Date", type=IntegerType)
Online_Shopping_Order_State: Property = Property(name="State", type=StringType)
Online_Shopping_Order_Contents: Property = Property(name="Contents", type=Online_Shopping_Orderitem)
Online_Shopping_Order.attributes={Online_Shopping_Order_Placed_Date, Online_Shopping_Order_Contents, Online_Shopping_Order_State}

# Online_Shopping_Orderstate class attributes and methods
Online_Shopping_Orderstate_attribute: Property = Property(name="attribute", type=StringType)
Online_Shopping_Orderstate.attributes={Online_Shopping_Orderstate_attribute}

# Online_Shopping_Special_offers class attributes and methods
Online_Shopping_Special_offers_Price: Property = Property(name="Price", type=StringType)
Online_Shopping_Special_offers_Discount: Property = Property(name="Discount", type=IntegerType)
Online_Shopping_Special_offers.attributes={Online_Shopping_Special_offers_Price, Online_Shopping_Special_offers_Discount}

# Online_Shopping_Customer_points class attributes and methods
Online_Shopping_Customer_points_Balance: Property = Property(name="Balance", type=Integer)
Online_Shopping_Customer_points.attributes={Online_Shopping_Customer_points_Balance}

# Online_Shopping_Customer class attributes and methods
Online_Shopping_Customer_Username: Property = Property(name="Username", type=StringType)
Online_Shopping_Customer_Password: Property = Property(name="Password", type=StringType)
Online_Shopping_Customer_Address: Property = Property(name="Address", type=StringType)
Online_Shopping_Customer_Age: Property = Property(name="Age", type=IntegerType)
Online_Shopping_Customer.attributes={Online_Shopping_Customer_Address, Online_Shopping_Customer_Age, Online_Shopping_Customer_Password, Online_Shopping_Customer_Username}

# Online_Shopping_Orderitem class attributes and methods
Online_Shopping_Orderitem_Quantity: Property = Property(name="Quantity", type=IntegerType)
Online_Shopping_Orderitem_ProductID: Property = Property(name="ProductID", type=StringType)
Online_Shopping_Orderitem_Sub_Total: Property = Property(name="Sub_Total", type=StringType)
Online_Shopping_Orderitem.attributes={Online_Shopping_Orderitem_Quantity, Online_Shopping_Orderitem_Sub_Total, Online_Shopping_Orderitem_ProductID}

# Relationships
view_items_Choose_items: BinaryAssociation = BinaryAssociation(
    name="view_items_Choose_items",
    ends={
        Property(name="choose_items8", type=Choose_items_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="view_items9", type=view_items_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Choose_items_make_a_purchase: BinaryAssociation = BinaryAssociation(
    name="Choose_items_make_a_purchase",
    ends={
        Property(name="make_a_purchase10", type=make_a_purchase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="choose_items11", type=Choose_items_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Choose_items_Checkout: BinaryAssociation = BinaryAssociation(
    name="Choose_items_Checkout",
    ends={
        Property(name="checkout12", type=Checkout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="choose_items13", type=Choose_items_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_make_a_purchase: BinaryAssociation = BinaryAssociation(
    name="Checkout_make_a_purchase",
    ends={
        Property(name="make_a_purchase14", type=make_a_purchase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout15", type=Checkout_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Credit_payment_service_payment: BinaryAssociation = BinaryAssociation(
    name="Credit_payment_service_payment",
    ends={
        Property(name="payment16", type=payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="credit_payment_service17", type=Credit_payment_service_Actor, multiplicity=Multiplicity(0, 1))
    }
)
bank__credit_card__shop_card__PayPal: BinaryAssociation = BinaryAssociation(
    name="bank__credit_card__shop_card__PayPal",
    ends={
        Property(name="credit_card__shop_card__PayPal18", type=credit_card__shop_card__PayPal_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="bank19", type=bank__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_Online_customer: BinaryAssociation = BinaryAssociation(
    name="Checkout_Online_customer",
    ends={
        Property(name="online_customer20", type=Online_customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout21", type=Checkout_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Online_customer_Customer_authentication: BinaryAssociation = BinaryAssociation(
    name="Online_customer_Customer_authentication",
    ends={
        Property(name="customer_authentication22", type=Customer_authentication__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="online_customer23", type=Online_customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
user_authentication_cookie_Authentication_or_service_or_identity_provider: BinaryAssociation = BinaryAssociation(
    name="user_authentication_cookie_Authentication_or_service_or_identity_provider",
    ends={
        Property(name="authentication_or_service_or_identity_provider24", type=Authentication_or_service_or_identity_provider_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="user_authentication_cookie25", type=user_authentication_cookie_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_register: BinaryAssociation = BinaryAssociation(
    name="Customer_register",
    ends={
        Property(name="register0", type=register_UseCase, multiplicity=Multiplicity(0, 1)),
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
Login_view_items: BinaryAssociation = BinaryAssociation(
    name="Login_view_items",
    ends={
        Property(name="view_items4", type=view_items_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="login5", type=Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
special_offers_Choose_items: BinaryAssociation = BinaryAssociation(
    name="special_offers_Choose_items",
    ends={
        Property(name="choose_items6", type=Choose_items_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="special_offers7", type=special_offers_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Log_in__sign_in_page_Authentication_or_service_or_identity_provider: BinaryAssociation = BinaryAssociation(
    name="Log_in__sign_in_page_Authentication_or_service_or_identity_provider",
    ends={
        Property(name="authentication_or_service_or_identity_provider26", type=Authentication_or_service_or_identity_provider_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="log_in__sign_in_page27", type=Log_in__sign_in_page_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_save_items_for_late_in_wish_list: BinaryAssociation = BinaryAssociation(
    name="Customer_save_items_for_late_in_wish_list",
    ends={
        Property(name="save_items_for_late_in_wish_list28", type=save_items_for_later_in_wish_list_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer29", type=Customer_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Customer_add_items_to_shopping_cart: BinaryAssociation = BinaryAssociation(
    name="Customer_add_items_to_shopping_cart",
    ends={
        Property(name="add_items_to_shopping_cart30", type=add_items_to_shopping_cart_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer31", type=Customer_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Special_offers: BinaryAssociation = BinaryAssociation(
    name="Customer_Special_offers",
    ends={
        Property(name="special_offers32", type=Online_Shopping_Special_offers, multiplicity=Multiplicity(0, 1)),
        Property(name="customer33", type=Online_Shopping_Customer, multiplicity=Multiplicity(0, 1))
    }
)
Special_offers_BasketItem: BinaryAssociation = BinaryAssociation(
    name="Special_offers_BasketItem",
    ends={
        Property(name="basketItem34", type=Online_Shopping_BasketItem, multiplicity=Multiplicity(0, 1)),
        Property(name="special_offers35", type=Online_Shopping_Special_offers, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Customer_points: BinaryAssociation = BinaryAssociation(
    name="Customer_Customer_points",
    ends={
        Property(name="customer_points36", type=Online_Shopping_Customer_points, multiplicity=Multiplicity(0, 1)),
        Property(name="customer37", type=Online_Shopping_Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Item: BinaryAssociation = BinaryAssociation(
    name="Customer_Item",
    ends={
        Property(name="item38", type=Online_Shopping_Item, multiplicity=Multiplicity(0, 1)),
        Property(name="customer39", type=Online_Shopping_Customer, multiplicity=Multiplicity(0, 1))
    }
)
Item_Basket: BinaryAssociation = BinaryAssociation(
    name="Item_Basket",
    ends={
        Property(name="basket40", type=Online_Shopping_Basket, multiplicity=Multiplicity(0, 1)),
        Property(name="item41", type=Online_Shopping_Item, multiplicity=Multiplicity(0, 1))
    }
)
Basket_BasketItem: BinaryAssociation = BinaryAssociation(
    name="Basket_BasketItem",
    ends={
        Property(name="basketItem42", type=Online_Shopping_BasketItem, multiplicity=Multiplicity(0, 1)),
        Property(name="basket43", type=Online_Shopping_Basket, multiplicity=Multiplicity(0, 1))
    }
)
Basket_Checkout: BinaryAssociation = BinaryAssociation(
    name="Basket_Checkout",
    ends={
        Property(name="checkout44", type=Online_Shopping_Checkout, multiplicity=Multiplicity(0, 1)),
        Property(name="basket45", type=Online_Shopping_Basket, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_PayPal_payment: BinaryAssociation = BinaryAssociation(
    name="Checkout_PayPal_payment",
    ends={
        Property(name="payPal_payment46", type=Online_Shopping_PayPal_payment, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout47", type=Online_Shopping_Checkout, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_Card_payment: BinaryAssociation = BinaryAssociation(
    name="Checkout_Card_payment",
    ends={
        Property(name="card_payment48", type=Online_Shopping_Card_payment, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout49", type=Online_Shopping_Checkout, multiplicity=Multiplicity(0, 1))
    }
)
Card_payment_Orderitem: BinaryAssociation = BinaryAssociation(
    name="Card_payment_Orderitem",
    ends={
        Property(name="orderitem50", type=Online_Shopping_Order, multiplicity=Multiplicity(0, 1)),
        Property(name="card_payment51", type=Online_Shopping_Card_payment, multiplicity=Multiplicity(0, 1))
    }
)
PayPal_payment_Orderitem: BinaryAssociation = BinaryAssociation(
    name="PayPal_payment_Orderitem",
    ends={
        Property(name="orderitem52", type=Online_Shopping_Order, multiplicity=Multiplicity(0, 1)),
        Property(name="payPal_payment53", type=Online_Shopping_PayPal_payment, multiplicity=Multiplicity(0, 1))
    }
)
Orderitem_Order: BinaryAssociation = BinaryAssociation(
    name="Orderitem_Order",
    ends={
        Property(name="order54", type=Online_Shopping_Order, multiplicity=Multiplicity(0, 1)),
        Property(name="orderitem55", type=Online_Shopping_Orderitem, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3i_aQHGTEemkSo3PkdMxbg",
    types={Customer_Actor, register_UseCase, Login_UseCase, Authentication_UseCase, view_items_UseCase, make_a_purchase_UseCase, claim_some_points_UseCase, special_offers_UseCase, payment_UseCase, PayPal__Mastercard__etc__UseCase, Choose_items_UseCase, View_items_UseCase, Search_for_items_UseCase, browse_catalogue_UseCase, view_recommended_items_UseCase, add_items_to_shopping_cart_UseCase, save_items_for_later_in_wish_list_UseCase, Checkout_UseCase, Checkout_UseCase1, Customer_authentication__UseCase, Log_in__sign_in_page_UseCase, user_authentication_cookie_UseCase, Credit_payment_service_Actor, Authentication_or_service_or_identity_provider_Actor, Payment_UseCase, Online_customer_Actor, credit_card__shop_card__PayPal_UseCase, bank__Actor, Customer_Actor1, _unnamed, Online_Shopping_Card_payment, Online_Shopping_PayPal_payment, Online_Shopping_Item, Online_Shopping_Checkout, Online_Shopping_Basket, Online_Shopping_BasketItem, Online_Shopping_Order, Online_Shopping_Orderstate, Online_Shopping_Special_offers, Online_Shopping_Customer_points, Online_Shopping_Customer, Online_Shopping_Orderitem, Online_Shopping_Or, Integer},
    associations={view_items_Choose_items, Choose_items_make_a_purchase, Choose_items_Checkout, Checkout_make_a_purchase, Credit_payment_service_payment, bank__credit_card__shop_card__PayPal, Checkout_Online_customer, Online_customer_Customer_authentication, user_authentication_cookie_Authentication_or_service_or_identity_provider, Customer_register, Customer_Login, Login_view_items, special_offers_Choose_items, Log_in__sign_in_page_Authentication_or_service_or_identity_provider, Customer_save_items_for_late_in_wish_list, Customer_add_items_to_shopping_cart, Customer_Special_offers, Special_offers_BasketItem, Customer_Customer_points, Customer_Item, Item_Basket, Basket_BasketItem, Basket_Checkout, Checkout_PayPal_payment, Checkout_Card_payment, Card_payment_Orderitem, PayPal_payment_Orderitem, Orderitem_Order},
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