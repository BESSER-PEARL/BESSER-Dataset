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
Manage_Accounts_external = Class(name="Manage_Accounts_external")
Assign_Roles_external = Class(name="Assign_Roles_external")
Support_User_Actor = Class(name="Support_User_Actor")
Sales_User_Actor = Class(name="Sales_User_Actor")
Login_and_authentication_UseCase = Class(name="Login_and_authentication_UseCase")
Sales_Users_Creation_UseCase = Class(name="Sales_Users_Creation_UseCase")
Business_Users_Creation_UseCase = Class(name="Business_Users_Creation_UseCase")
Business_User_Actor = Class(name="Business_User_Actor")
Component_Component = Class(name="Component_Component")
Order_Management_System_Component = Class(name="Order_Management_System_Component")
T = Class(name="T")
T1 = Class(name="T1")
Sales_Users_Creation_UseCase1 = Class(name="Sales_Users_Creation_UseCase1")
Order_Approved_Rejected_external = Class(name="Order_Approved_Rejected_external")
Order_Created_external = Class(name="Order_Created_external")
Invoice_generation_external = Class(name="Invoice_generation_external")
Product_Invoice_generation_external = Class(name="Product_Invoice_generation_external")
Notifications_for_Order_Tracking_external = Class(name="Notifications_for_Order_Tracking_external")
Login_and_authentication_external = Class(name="Login_and_authentication_external")
Business_Users_Creation_external = Class(name="Business_Users_Creation_external")
Manage_Sales_Users_external = Class(name="Manage_Sales_Users_external")
Search_Products_to_Order_external = Class(name="Search_Products_to_Order_external")
Select_Products_external = Class(name="Select_Products_external")
Review_Order_external = Class(name="Review_Order_external")
Confirm_Order_external = Class(name="Confirm_Order_external")

# Manage_Accounts_external class attributes and methods

# Assign_Roles_external class attributes and methods

# Support_User_Actor class attributes and methods

# Sales_User_Actor class attributes and methods

# Login_and_authentication_UseCase class attributes and methods

# Sales_Users_Creation_UseCase class attributes and methods

# Business_Users_Creation_UseCase class attributes and methods

# Business_User_Actor class attributes and methods

# Component_Component class attributes and methods

# Order_Management_System_Component class attributes and methods

# T class attributes and methods

# T1 class attributes and methods

# Sales_Users_Creation_UseCase1 class attributes and methods

# Order_Approved_Rejected_external class attributes and methods

# Order_Created_external class attributes and methods

# Invoice_generation_external class attributes and methods

# Product_Invoice_generation_external class attributes and methods

# Notifications_for_Order_Tracking_external class attributes and methods

# Login_and_authentication_external class attributes and methods

# Business_Users_Creation_external class attributes and methods

# Manage_Sales_Users_external class attributes and methods

# Search_Products_to_Order_external class attributes and methods

# Select_Products_external class attributes and methods

# Review_Order_external class attributes and methods

# Confirm_Order_external class attributes and methods

# Relationships
Sales_User_Manage_Accounts: BinaryAssociation = BinaryAssociation(
    name="Sales_User_Manage_Accounts",
    ends={
        Property(name="sales_User40", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_Accounts41", type=Manage_Accounts_external, multiplicity=Multiplicity(0, 1))
    }
)
Business_User_Manage_Accounts: BinaryAssociation = BinaryAssociation(
    name="Business_User_Manage_Accounts",
    ends={
        Property(name="business_User42", type=Business_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_Accounts43", type=Manage_Accounts_external, multiplicity=Multiplicity(0, 1))
    }
)
Support_User_Assign_Roles: BinaryAssociation = BinaryAssociation(
    name="Support_User_Assign_Roles",
    ends={
        Property(name="support_User44", type=Support_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="assign_Roles45", type=Assign_Roles_external, multiplicity=Multiplicity(0, 1))
    }
)
Sales_User_Assign_Roles: BinaryAssociation = BinaryAssociation(
    name="Sales_User_Assign_Roles",
    ends={
        Property(name="sales_User46", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="assign_Roles47", type=Assign_Roles_external, multiplicity=Multiplicity(0, 1))
    }
)
Support_User_Login_and_authentication: BinaryAssociation = BinaryAssociation(
    name="Support_User_Login_and_authentication",
    ends={
        Property(name="support_User0", type=Support_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login_and_authentication1", type=Login_and_authentication_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Sales_User_Login_and_authentication: BinaryAssociation = BinaryAssociation(
    name="Sales_User_Login_and_authentication",
    ends={
        Property(name="sales_User2", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login_and_authentication3", type=Login_and_authentication_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Business_User_Login_and_authentication: BinaryAssociation = BinaryAssociation(
    name="Business_User_Login_and_authentication",
    ends={
        Property(name="business_User4", type=Business_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login_and_authentication5", type=Login_and_authentication_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Business_User_Business_Users_Creation: BinaryAssociation = BinaryAssociation(
    name="Business_User_Business_Users_Creation",
    ends={
        Property(name="business_User6", type=Business_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="business_Users_Creation7", type=Business_Users_Creation_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Sales_User_Sales_Users_Creation: BinaryAssociation = BinaryAssociation(
    name="Sales_User_Sales_Users_Creation",
    ends={
        Property(name="sales_User8", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Users_Creation9", type=Sales_Users_Creation_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Support_User_Sales_Users_Creation: BinaryAssociation = BinaryAssociation(
    name="Support_User_Sales_Users_Creation",
    ends={
        Property(name="support_User10", type=Support_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Users_Creation11", type=Sales_Users_Creation_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Support_User_Business_Users_Creation: BinaryAssociation = BinaryAssociation(
    name="Support_User_Business_Users_Creation",
    ends={
        Property(name="support_User12", type=Support_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="business_Users_Creation13", type=Business_Users_Creation_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Order_Approved_Rejected_Business_User: BinaryAssociation = BinaryAssociation(
    name="Order_Approved_Rejected_Business_User",
    ends={
        Property(name="order_Approved_Rejected14", type=Order_Approved_Rejected_external, multiplicity=Multiplicity(0, 1)),
        Property(name="business_User15", type=Business_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Order_Created_Sales_User: BinaryAssociation = BinaryAssociation(
    name="Order_Created_Sales_User",
    ends={
        Property(name="order_Created16", type=Order_Created_external, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_User17", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Invoice_generation_Sales_User: BinaryAssociation = BinaryAssociation(
    name="Invoice_generation_Sales_User",
    ends={
        Property(name="invoice_generation18", type=Invoice_generation_external, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_User19", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Product_Invoice_generation_Sales_User: BinaryAssociation = BinaryAssociation(
    name="Product_Invoice_generation_Sales_User",
    ends={
        Property(name="product_Invoice_generation20", type=Product_Invoice_generation_external, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_User21", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Notification_for_Order_Tracking_Sales_User: BinaryAssociation = BinaryAssociation(
    name="Notification_for_Order_Tracking_Sales_User",
    ends={
        Property(name="notification_for_Order_Tracking22", type=Notifications_for_Order_Tracking_external, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_User23", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Notification_for_Order_Tracking_Business_User: BinaryAssociation = BinaryAssociation(
    name="Notification_for_Order_Tracking_Business_User",
    ends={
        Property(name="notification_for_Order_Tracking24", type=Notifications_for_Order_Tracking_external, multiplicity=Multiplicity(0, 1)),
        Property(name="business_User25", type=Business_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Notification_for_Order_Tracking_Support_User: BinaryAssociation = BinaryAssociation(
    name="Notification_for_Order_Tracking_Support_User",
    ends={
        Property(name="notification_for_Order_Tracking26", type=Notifications_for_Order_Tracking_external, multiplicity=Multiplicity(0, 1)),
        Property(name="support_User27", type=Support_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Support_User_Login_and_authentication2: BinaryAssociation = BinaryAssociation(
    name="Support_User_Login_and_authentication2",
    ends={
        Property(name="support_User28", type=Support_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login_and_authentication29", type=Login_and_authentication_external, multiplicity=Multiplicity(0, 1))
    }
)
Sales_User_Login_and_authentication2: BinaryAssociation = BinaryAssociation(
    name="Sales_User_Login_and_authentication2",
    ends={
        Property(name="sales_User30", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login_and_authentication31", type=Login_and_authentication_external, multiplicity=Multiplicity(0, 1))
    }
)
Business_User_Login_and_authentication2: BinaryAssociation = BinaryAssociation(
    name="Business_User_Login_and_authentication2",
    ends={
        Property(name="business_User32", type=Business_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login_and_authentication33", type=Login_and_authentication_external, multiplicity=Multiplicity(0, 1))
    }
)
Support_User_Sales_Users_Creation2: BinaryAssociation = BinaryAssociation(
    name="Support_User_Sales_Users_Creation2",
    ends={
        Property(name="support_User34", type=Support_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Users_Creation35", type=Sales_Users_Creation_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Sales_User_Sales_User: BinaryAssociation = BinaryAssociation(
    name="Sales_User_Sales_User",
    ends={
        Property(name="sales_User36", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_User37", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Support_User_Business_Users_Creation2: BinaryAssociation = BinaryAssociation(
    name="Support_User_Business_Users_Creation2",
    ends={
        Property(name="support_User38", type=Support_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="business_Users_Creation39", type=Business_Users_Creation_external, multiplicity=Multiplicity(0, 1))
    }
)
Business_User_Assign_Roles: BinaryAssociation = BinaryAssociation(
    name="Business_User_Assign_Roles",
    ends={
        Property(name="business_User48", type=Business_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="assign_Roles49", type=Assign_Roles_external, multiplicity=Multiplicity(0, 1))
    }
)
Business_User_Manage_Sales_Users: BinaryAssociation = BinaryAssociation(
    name="Business_User_Manage_Sales_Users",
    ends={
        Property(name="business_User50", type=Business_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_Sales_Users51", type=Manage_Sales_Users_external, multiplicity=Multiplicity(0, 1))
    }
)
Support_User_Manage_Accounts: BinaryAssociation = BinaryAssociation(
    name="Support_User_Manage_Accounts",
    ends={
        Property(name="support_User52", type=Support_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_Accounts53", type=Manage_Accounts_external, multiplicity=Multiplicity(0, 1))
    }
)
Support_User_Manage_Sales_Users: BinaryAssociation = BinaryAssociation(
    name="Support_User_Manage_Sales_Users",
    ends={
        Property(name="support_User54", type=Support_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_Sales_Users55", type=Manage_Sales_Users_external, multiplicity=Multiplicity(0, 1))
    }
)
Sales_User_Search_Products_to_Order: BinaryAssociation = BinaryAssociation(
    name="Sales_User_Search_Products_to_Order",
    ends={
        Property(name="sales_User56", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="search_Products_to_Order57", type=Search_Products_to_Order_external, multiplicity=Multiplicity(0, 1))
    }
)
Sales_User_Select_Products: BinaryAssociation = BinaryAssociation(
    name="Sales_User_Select_Products",
    ends={
        Property(name="sales_User58", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="select_Products59", type=Select_Products_external, multiplicity=Multiplicity(0, 1))
    }
)
Sales_User_Review_Order: BinaryAssociation = BinaryAssociation(
    name="Sales_User_Review_Order",
    ends={
        Property(name="sales_User60", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="review_Order61", type=Review_Order_external, multiplicity=Multiplicity(0, 1))
    }
)
Sales_User_Confirm_Order: BinaryAssociation = BinaryAssociation(
    name="Sales_User_Confirm_Order",
    ends={
        Property(name="sales_User62", type=Sales_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="confirm_Order63", type=Confirm_Order_external, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5WaHcImMEeq3N_Xh6gsEIQ",
    types={Manage_Accounts_external, Assign_Roles_external, Support_User_Actor, Sales_User_Actor, Login_and_authentication_UseCase, Sales_Users_Creation_UseCase, Business_Users_Creation_UseCase, Business_User_Actor, Component_Component, Order_Management_System_Component, T, T1, Sales_Users_Creation_UseCase1, Order_Approved_Rejected_external, Order_Created_external, Invoice_generation_external, Product_Invoice_generation_external, Notifications_for_Order_Tracking_external, Login_and_authentication_external, Business_Users_Creation_external, Manage_Sales_Users_external, Search_Products_to_Order_external, Select_Products_external, Review_Order_external, Confirm_Order_external},
    associations={Sales_User_Manage_Accounts, Business_User_Manage_Accounts, Support_User_Assign_Roles, Sales_User_Assign_Roles, Support_User_Login_and_authentication, Sales_User_Login_and_authentication, Business_User_Login_and_authentication, Business_User_Business_Users_Creation, Sales_User_Sales_Users_Creation, Support_User_Sales_Users_Creation, Support_User_Business_Users_Creation, Order_Approved_Rejected_Business_User, Order_Created_Sales_User, Invoice_generation_Sales_User, Product_Invoice_generation_Sales_User, Notification_for_Order_Tracking_Sales_User, Notification_for_Order_Tracking_Business_User, Notification_for_Order_Tracking_Support_User, Support_User_Login_and_authentication2, Sales_User_Login_and_authentication2, Business_User_Login_and_authentication2, Support_User_Sales_Users_Creation2, Sales_User_Sales_User, Support_User_Business_Users_Creation2, Business_User_Assign_Roles, Business_User_Manage_Sales_Users, Support_User_Manage_Accounts, Support_User_Manage_Sales_Users, Sales_User_Search_Products_to_Order, Sales_User_Select_Products, Sales_User_Review_Order, Sales_User_Confirm_Order},
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