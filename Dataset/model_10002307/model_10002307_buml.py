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
Registered_User_Actor = Class(name="Registered_User_Actor")
Sign_In_UseCase = Class(name="Sign_In_UseCase")
View_Meal_Deal_UseCase = Class(name="View_Meal_Deal_UseCase")
View_Pizza_types_UseCase = Class(name="View_Pizza_types_UseCase")
Create_your_own_pizza_UseCase = Class(name="Create_your_own_pizza_UseCase")
Add_item_UseCase = Class(name="Add_item_UseCase")
View_side_orders_UseCase = Class(name="View_side_orders_UseCase")
Create_Account_UseCase = Class(name="Create_Account_UseCase")
Change_toppings_UseCase = Class(name="Change_toppings_UseCase")
Search_store_locations_UseCase = Class(name="Search_store_locations_UseCase")
Checkout_UseCase = Class(name="Checkout_UseCase")
Pay_online_UseCase = Class(name="Pay_online_UseCase")
Save_favourite_order_UseCase = Class(name="Save_favourite_order_UseCase")
Make_Payment_UseCase = Class(name="Make_Payment_UseCase")
Order_tracking_UseCase = Class(name="Order_tracking_UseCase")
Pizza_Chef_Actor = Class(name="Pizza_Chef_Actor")
Delivery_person_Actor = Class(name="Delivery_person_Actor")
Receive_order_UseCase = Class(name="Receive_order_UseCase")
Cook_Pizza_UseCase = Class(name="Cook_Pizza_UseCase")
Deliver_pizza_UseCase = Class(name="Deliver_pizza_UseCase")
Edit_menu_UseCase = Class(name="Edit_menu_UseCase")
Manage_accounts_UseCase = Class(name="Manage_accounts_UseCase")
Admin_Actor = Class(name="Admin_Actor")
Pre_order_UseCase = Class(name="Pre_order_UseCase")
Add_new_address_UseCase = Class(name="Add_new_address_UseCase")
PayAt_Delivery_UseCase = Class(name="PayAt_Delivery_UseCase")
Customer = Class(name="Customer")
Admin = Class(name="Admin")
Payment = Class(name="Payment")
Pay_cash_on_deliver = Class(name="Pay_cash_on_deliver")
Online_payment_methods = Class(name="Online_payment_methods")
Online_pizza_ordering = Class(name="Online_pizza_ordering")
Menu = Class(name="Menu")

# Registered_User_Actor class attributes and methods

# Sign_In_UseCase class attributes and methods

# View_Meal_Deal_UseCase class attributes and methods

# View_Pizza_types_UseCase class attributes and methods

# Create_your_own_pizza_UseCase class attributes and methods

# Add_item_UseCase class attributes and methods

# View_side_orders_UseCase class attributes and methods

# Create_Account_UseCase class attributes and methods

# Change_toppings_UseCase class attributes and methods

# Search_store_locations_UseCase class attributes and methods

# Checkout_UseCase class attributes and methods

# Pay_online_UseCase class attributes and methods

# Save_favourite_order_UseCase class attributes and methods

# Make_Payment_UseCase class attributes and methods

# Order_tracking_UseCase class attributes and methods

# Pizza_Chef_Actor class attributes and methods

# Delivery_person_Actor class attributes and methods

# Receive_order_UseCase class attributes and methods

# Cook_Pizza_UseCase class attributes and methods

# Deliver_pizza_UseCase class attributes and methods

# Edit_menu_UseCase class attributes and methods

# Manage_accounts_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# Pre_order_UseCase class attributes and methods

# Add_new_address_UseCase class attributes and methods

# PayAt_Delivery_UseCase class attributes and methods

# Customer class attributes and methods
Customer_Password: Property = Property(name="Password", type=StringType)
Customer_Name: Property = Property(name="Name", type=StringType)
Customer.attributes={Customer_Password, Customer_Name}

# Admin class attributes and methods

# Payment class attributes and methods

# Pay_cash_on_deliver class attributes and methods

# Online_payment_methods class attributes and methods

# Online_pizza_ordering class attributes and methods
Online_pizza_ordering_Price: Property = Property(name="Price", type=FloatType)
Online_pizza_ordering_pizza_type: Property = Property(name="pizza_type", type=StringType)
Online_pizza_ordering_Ingredients: Property = Property(name="Ingredients", type=StringType)
Online_pizza_ordering.attributes={Online_pizza_ordering_Ingredients, Online_pizza_ordering_Price, Online_pizza_ordering_pizza_type}

# Menu class attributes and methods
Menu_Quantity: Property = Property(name="Quantity", type=StringType)
Menu_toppings: Property = Property(name="toppings", type=StringType)
Menu.attributes={Menu_Quantity, Menu_toppings}

# Relationships
Registered_User_Save_favourite_order: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Save_favourite_order",
    ends={
        Property(name="save_favourite_order0", type=Save_favourite_order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User1", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Search_store_locations: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Search_store_locations",
    ends={
        Property(name="search_store_locations2", type=Search_store_locations_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User3", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_View_side_orders: BinaryAssociation = BinaryAssociation(
    name="Registered_User_View_side_orders",
    ends={
        Property(name="view_side_orders4", type=View_side_orders_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User5", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_View_Pizza_types: BinaryAssociation = BinaryAssociation(
    name="Registered_User_View_Pizza_types",
    ends={
        Property(name="view_Pizza_types6", type=View_Pizza_types_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User7", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Select_Meal_Deal: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Select_Meal_Deal",
    ends={
        Property(name="select_Meal_Deal8", type=View_Meal_Deal_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User9", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Checkout: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Checkout",
    ends={
        Property(name="checkout10", type=Checkout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User11", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Create_your_own_pizza: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Create_your_own_pizza",
    ends={
        Property(name="create_your_own_pizza12", type=Create_your_own_pizza_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User13", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Order_tracking: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Order_tracking",
    ends={
        Property(name="order_tracking14", type=Order_tracking_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User15", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receive_order_Pizza_Chef: BinaryAssociation = BinaryAssociation(
    name="Receive_order_Pizza_Chef",
    ends={
        Property(name="pizza_Chef16", type=Pizza_Chef_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="receive_order17", type=Receive_order_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Delivery_person_Receive_order: BinaryAssociation = BinaryAssociation(
    name="Delivery_person_Receive_order",
    ends={
        Property(name="receive_order18", type=Receive_order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="delivery_person19", type=Delivery_person_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Edit_menu_Admin: BinaryAssociation = BinaryAssociation(
    name="Edit_menu_Admin",
    ends={
        Property(name="admin20", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="edit_menu21", type=Edit_menu_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Manage_accounts_Admin: BinaryAssociation = BinaryAssociation(
    name="Manage_accounts_Admin",
    ends={
        Property(name="admin22", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_accounts23", type=Manage_accounts_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Pre_order: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Pre_order",
    ends={
        Property(name="pre_order24", type=Pre_order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User25", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Create_Account: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Create_Account",
    ends={
        Property(name="create_Account26", type=Create_Account_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User27", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Sign_In: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Sign_In",
    ends={
        Property(name="sign_In28", type=Sign_In_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User29", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Online_pizza_ordering: BinaryAssociation = BinaryAssociation(
    name="Customer_Online_pizza_ordering",
    ends={
        Property(name="Customer_Online_pizza_ordering_030", type=Online_pizza_ordering, multiplicity=Multiplicity(0, 1)),
        Property(name="Customer_Online_pizza_ordering_131", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
assoc__R_J8U5UFEeqqGZh46IEtXQ: BinaryAssociation = BinaryAssociation(
    name="assoc__R_J8U5UFEeqqGZh46IEtXQ",
    ends={
        Property(name="assoc_032", type=Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="assoc_133", type=Online_pizza_ordering, multiplicity=Multiplicity(1, 9999))
    }
)
assoc__R_J8ZJUFEeqqGZh46IEtXQ: BinaryAssociation = BinaryAssociation(
    name="assoc__R_J8ZJUFEeqqGZh46IEtXQ",
    ends={
        Property(name="assoc_034", type=Payment, multiplicity=Multiplicity(1, 9999)),
        Property(name="assoc_135", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
assoc__R_J8g5UFEeqqGZh46IEtXQ: BinaryAssociation = BinaryAssociation(
    name="assoc__R_J8g5UFEeqqGZh46IEtXQ",
    ends={
        Property(name="assoc_036", type=Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="assoc_137", type=Online_pizza_ordering, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a5a9b442_0651_484f_81d7_64c493c16f39",
    types={Registered_User_Actor, Sign_In_UseCase, View_Meal_Deal_UseCase, View_Pizza_types_UseCase, Create_your_own_pizza_UseCase, Add_item_UseCase, View_side_orders_UseCase, Create_Account_UseCase, Change_toppings_UseCase, Search_store_locations_UseCase, Checkout_UseCase, Pay_online_UseCase, Save_favourite_order_UseCase, Make_Payment_UseCase, Order_tracking_UseCase, Pizza_Chef_Actor, Delivery_person_Actor, Receive_order_UseCase, Cook_Pizza_UseCase, Deliver_pizza_UseCase, Edit_menu_UseCase, Manage_accounts_UseCase, Admin_Actor, Pre_order_UseCase, Add_new_address_UseCase, PayAt_Delivery_UseCase, Customer, Admin, Payment, Pay_cash_on_deliver, Online_payment_methods, Online_pizza_ordering, Menu},
    associations={Registered_User_Save_favourite_order, Registered_User_Search_store_locations, Registered_User_View_side_orders, Registered_User_View_Pizza_types, Registered_User_Select_Meal_Deal, Registered_User_Checkout, Registered_User_Create_your_own_pizza, Registered_User_Order_tracking, Receive_order_Pizza_Chef, Delivery_person_Receive_order, Edit_menu_Admin, Manage_accounts_Admin, Registered_User_Pre_order, Registered_User_Create_Account, Registered_User_Sign_In, Customer_Online_pizza_ordering, assoc__R_J8U5UFEeqqGZh46IEtXQ, assoc__R_J8ZJUFEeqqGZh46IEtXQ, assoc__R_J8g5UFEeqqGZh46IEtXQ},
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