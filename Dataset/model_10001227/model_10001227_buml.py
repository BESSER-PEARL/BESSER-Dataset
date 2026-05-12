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
Log_In_UseCase = Class(name="Log_In_UseCase")
View_Pizza_types_UseCase = Class(name="View_Pizza_types_UseCase")
Create_your_own_pizza_UseCase = Class(name="Create_your_own_pizza_UseCase")
Add_item_UseCase = Class(name="Add_item_UseCase")
View_side_orders_UseCase = Class(name="View_side_orders_UseCase")
Change_toppings_UseCase = Class(name="Change_toppings_UseCase")
Order_tracking_UseCase = Class(name="Order_tracking_UseCase")
Edit____delete___view_menu_UseCase = Class(name="Edit____delete___view_menu_UseCase")
Manage_accounts_UseCase = Class(name="Manage_accounts_UseCase")
Admin_Actor = Class(name="Admin_Actor")
Visit_home_page_UseCase = Class(name="Visit_home_page_UseCase")
Customer = Class(name="Customer")
Admin = Class(name="Admin")
Payment = Class(name="Payment")
Pay_cash_on_deliver = Class(name="Pay_cash_on_deliver")
Online_payment_methods = Class(name="Online_payment_methods")
Online_pizza_ordering = Class(name="Online_pizza_ordering")
Menu = Class(name="Menu")
Registration_UseCase = Class(name="Registration_UseCase")
Add_to_cart_and_buy_UseCase = Class(name="Add_to_cart_and_buy_UseCase")
Make_payment_UseCase = Class(name="Make_payment_UseCase")
Pay_online_UseCase = Class(name="Pay_online_UseCase")
Pay_At_delivery_UseCase = Class(name="Pay_At_delivery_UseCase")
Write_feedback_UseCase = Class(name="Write_feedback_UseCase")
Change_password_UseCase = Class(name="Change_password_UseCase")
Update_order_UseCase = Class(name="Update_order_UseCase")
View_pizza_sales_UseCase = Class(name="View_pizza_sales_UseCase")
View_feedback_UseCase = Class(name="View_feedback_UseCase")
Add_pizza_UseCase = Class(name="Add_pizza_UseCase")
Customer_Actor = Class(name="Customer_Actor")

# Log_In_UseCase class attributes and methods

# View_Pizza_types_UseCase class attributes and methods

# Create_your_own_pizza_UseCase class attributes and methods

# Add_item_UseCase class attributes and methods

# View_side_orders_UseCase class attributes and methods

# Change_toppings_UseCase class attributes and methods

# Order_tracking_UseCase class attributes and methods

# Edit____delete___view_menu_UseCase class attributes and methods

# Manage_accounts_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# Visit_home_page_UseCase class attributes and methods

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
Online_pizza_ordering.attributes={Online_pizza_ordering_Price, Online_pizza_ordering_pizza_type, Online_pizza_ordering_Ingredients}

# Menu class attributes and methods
Menu_Quantity: Property = Property(name="Quantity", type=StringType)
Menu_toppings: Property = Property(name="toppings", type=StringType)
Menu.attributes={Menu_Quantity, Menu_toppings}

# Registration_UseCase class attributes and methods

# Add_to_cart_and_buy_UseCase class attributes and methods

# Make_payment_UseCase class attributes and methods

# Pay_online_UseCase class attributes and methods

# Pay_At_delivery_UseCase class attributes and methods

# Write_feedback_UseCase class attributes and methods

# Change_password_UseCase class attributes and methods

# Update_order_UseCase class attributes and methods

# View_pizza_sales_UseCase class attributes and methods

# View_feedback_UseCase class attributes and methods

# Add_pizza_UseCase class attributes and methods

# Customer_Actor class attributes and methods

# Relationships
Registered_User_View_side_orders: BinaryAssociation = BinaryAssociation(
    name="Registered_User_View_side_orders",
    ends={
        Property(name="view_side_orders0", type=View_side_orders_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User1", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_View_Pizza_types: BinaryAssociation = BinaryAssociation(
    name="Registered_User_View_Pizza_types",
    ends={
        Property(name="view_Pizza_types2", type=View_Pizza_types_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User3", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Create_your_own_pizza: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Create_your_own_pizza",
    ends={
        Property(name="create_your_own_pizza4", type=Create_your_own_pizza_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User5", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Order_tracking: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Order_tracking",
    ends={
        Property(name="order_tracking6", type=Order_tracking_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="registered_User7", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Edit_menu_Admin: BinaryAssociation = BinaryAssociation(
    name="Edit_menu_Admin",
    ends={
        Property(name="admin8", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="edit_menu9", type=Edit____delete___view_menu_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Manage_accounts_Admin: BinaryAssociation = BinaryAssociation(
    name="Manage_accounts_Admin",
    ends={
        Property(name="admin10", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_accounts11", type=Manage_accounts_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Online_pizza_ordering: BinaryAssociation = BinaryAssociation(
    name="Customer_Online_pizza_ordering",
    ends={
        Property(name="Customer_Online_pizza_ordering_012", type=Online_pizza_ordering, multiplicity=Multiplicity(0, 1)),
        Property(name="Customer_Online_pizza_ordering_113", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
assoc__RwqMk5UFEeqqGZh46IEtXQ: BinaryAssociation = BinaryAssociation(
    name="assoc__RwqMk5UFEeqqGZh46IEtXQ",
    ends={
        Property(name="assoc_014", type=Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="assoc_115", type=Online_pizza_ordering, multiplicity=Multiplicity(1, 9999))
    }
)
assoc__RwqMpJUFEeqqGZh46IEtXQ: BinaryAssociation = BinaryAssociation(
    name="assoc__RwqMpJUFEeqqGZh46IEtXQ",
    ends={
        Property(name="assoc_016", type=Payment, multiplicity=Multiplicity(1, 9999)),
        Property(name="assoc_117", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
assoc__RwqMw5UFEeqqGZh46IEtXQ: BinaryAssociation = BinaryAssociation(
    name="assoc__RwqMw5UFEeqqGZh46IEtXQ",
    ends={
        Property(name="assoc_018", type=Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="assoc_119", type=Online_pizza_ordering, multiplicity=Multiplicity(1, 1))
    }
)
Registration_Customer: BinaryAssociation = BinaryAssociation(
    name="Registration_Customer",
    ends={
        Property(name="customer20", type=Customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registration21", type=Registration_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Sign_In_Customer: BinaryAssociation = BinaryAssociation(
    name="Sign_In_Customer",
    ends={
        Property(name="customer22", type=Customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sign_In23", type=Log_In_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Visit_home_page_Customer: BinaryAssociation = BinaryAssociation(
    name="Visit_home_page_Customer",
    ends={
        Property(name="customer24", type=Customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="visit_home_page25", type=Visit_home_page_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Add_to_cart_and_buy: BinaryAssociation = BinaryAssociation(
    name="Customer_Add_to_cart_and_buy",
    ends={
        Property(name="add_to_cart_and_buy26", type=Add_to_cart_and_buy_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer27", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Make_payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Make_payment",
    ends={
        Property(name="make_payment28", type=Make_payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer29", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Write_feedback: BinaryAssociation = BinaryAssociation(
    name="Customer_Write_feedback",
    ends={
        Property(name="write_feedback30", type=Write_feedback_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer31", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Change_password: BinaryAssociation = BinaryAssociation(
    name="Customer_Change_password",
    ends={
        Property(name="change_password32", type=Change_password_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer33", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Add_pizza_Admin: BinaryAssociation = BinaryAssociation(
    name="Add_pizza_Admin",
    ends={
        Property(name="admin34", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="add_pizza35", type=Add_pizza_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Update_order_Admin: BinaryAssociation = BinaryAssociation(
    name="Update_order_Admin",
    ends={
        Property(name="admin36", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="update_order37", type=Update_order_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
View_pizza_sales_Admin: BinaryAssociation = BinaryAssociation(
    name="View_pizza_sales_Admin",
    ends={
        Property(name="admin38", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_pizza_sales39", type=View_pizza_sales_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
View_feedback_Admin: BinaryAssociation = BinaryAssociation(
    name="View_feedback_Admin",
    ends={
        Property(name="admin40", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_feedback41", type=View_feedback_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_95d0e2ee_9657_43dc_be1a_beeff28fbe5f",
    types={Log_In_UseCase, View_Pizza_types_UseCase, Create_your_own_pizza_UseCase, Add_item_UseCase, View_side_orders_UseCase, Change_toppings_UseCase, Order_tracking_UseCase, Edit____delete___view_menu_UseCase, Manage_accounts_UseCase, Admin_Actor, Visit_home_page_UseCase, Customer, Admin, Payment, Pay_cash_on_deliver, Online_payment_methods, Online_pizza_ordering, Menu, Registration_UseCase, Add_to_cart_and_buy_UseCase, Make_payment_UseCase, Pay_online_UseCase, Pay_At_delivery_UseCase, Write_feedback_UseCase, Change_password_UseCase, Update_order_UseCase, View_pizza_sales_UseCase, View_feedback_UseCase, Add_pizza_UseCase, Customer_Actor},
    associations={Registered_User_View_side_orders, Registered_User_View_Pizza_types, Registered_User_Create_your_own_pizza, Registered_User_Order_tracking, Edit_menu_Admin, Manage_accounts_Admin, Customer_Online_pizza_ordering, assoc__RwqMk5UFEeqqGZh46IEtXQ, assoc__RwqMpJUFEeqqGZh46IEtXQ, assoc__RwqMw5UFEeqqGZh46IEtXQ, Registration_Customer, Sign_In_Customer, Visit_home_page_Customer, Customer_Add_to_cart_and_buy, Customer_Make_payment, Customer_Write_feedback, Customer_Change_password, Add_pizza_Admin, Update_order_Admin, View_pizza_sales_Admin, View_feedback_Admin},
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