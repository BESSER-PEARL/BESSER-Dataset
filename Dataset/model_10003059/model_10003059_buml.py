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
View_order_transation_UseCase = Class(name="View_order_transation_UseCase")
Update_status_of_orders_UseCase = Class(name="Update_status_of_orders_UseCase")
Operator_Actor = Class(name="Operator_Actor")
Login_Logout_UseCase = Class(name="Login_Logout_UseCase")
View_order_transation_UseCase1 = Class(name="View_order_transation_UseCase1")
Add_Edit_Delete_menus_UseCase = Class(name="Add_Edit_Delete_menus_UseCase")
Food = Class(name="Food")
Customer_Actor = Class(name="Customer_Actor")
Log_in_logout_UseCase = Class(name="Log_in_logout_UseCase")
order_food_UseCase = Class(name="order_food_UseCase")
Write_Review_UseCase = Class(name="Write_Review_UseCase")
See_order_Status_UseCase = Class(name="See_order_Status_UseCase")
View_open_bill_and_ordered_items_UseCase = Class(name="View_open_bill_and_ordered_items_UseCase")
View_Food_products_UseCase = Class(name="View_Food_products_UseCase")
Edit_personal_Information_UseCase = Class(name="Edit_personal_Information_UseCase")
Admin_Actor = Class(name="Admin_Actor")
Access_the_system_UseCase = Class(name="Access_the_system_UseCase")
Add_Edit_Delete_menus_menu_items__UseCase = Class(name="Add_Edit_Delete_menus_menu_items__UseCase")
Add_user_and_Assign_role_UseCase = Class(name="Add_user_and_Assign_role_UseCase")

# View_order_transation_UseCase class attributes and methods

# Update_status_of_orders_UseCase class attributes and methods

# Operator_Actor class attributes and methods

# Login_Logout_UseCase class attributes and methods

# View_order_transation_UseCase1 class attributes and methods

# Add_Edit_Delete_menus_UseCase class attributes and methods

# Food class attributes and methods
Food_id: Property = Property(name="id", type=IntegerType)
Food_name: Property = Property(name="name", type=StringType)
Food.attributes={Food_name, Food_id}

# Customer_Actor class attributes and methods

# Log_in_logout_UseCase class attributes and methods

# order_food_UseCase class attributes and methods

# Write_Review_UseCase class attributes and methods

# See_order_Status_UseCase class attributes and methods

# View_open_bill_and_ordered_items_UseCase class attributes and methods

# View_Food_products_UseCase class attributes and methods

# Edit_personal_Information_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# Access_the_system_UseCase class attributes and methods

# Add_Edit_Delete_menus_menu_items__UseCase class attributes and methods

# Add_user_and_Assign_role_UseCase class attributes and methods

# Relationships
Customer_Log_in_logout: BinaryAssociation = BinaryAssociation(
    name="Customer_Log_in_logout",
    ends={
        Property(name="log_in_logout0", type=Log_in_logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_View_Food_products: BinaryAssociation = BinaryAssociation(
    name="Customer_View_Food_products",
    ends={
        Property(name="view_Food_products2", type=View_Food_products_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_order_food: BinaryAssociation = BinaryAssociation(
    name="Customer_order_food",
    ends={
        Property(name="order_food4", type=order_food_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_View_open_bill_and_ordered_items: BinaryAssociation = BinaryAssociation(
    name="Customer_View_open_bill_and_ordered_items",
    ends={
        Property(name="view_open_bill_and_ordered_items6", type=View_open_bill_and_ordered_items_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Edit_personal_Information: BinaryAssociation = BinaryAssociation(
    name="Customer_Edit_personal_Information",
    ends={
        Property(name="edit_personal_Information8", type=Edit_personal_Information_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_See_order_Status: BinaryAssociation = BinaryAssociation(
    name="Customer_See_order_Status",
    ends={
        Property(name="see_order_Status10", type=See_order_Status_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Write_Review: BinaryAssociation = BinaryAssociation(
    name="Customer_Write_Review",
    ends={
        Property(name="write_Review12", type=Write_Review_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Access_the_system: BinaryAssociation = BinaryAssociation(
    name="Admin_Access_the_system",
    ends={
        Property(name="access_the_system14", type=Access_the_system_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin15", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Add_Edit_Delete_menus_menu_items_: BinaryAssociation = BinaryAssociation(
    name="Admin_Add_Edit_Delete_menus_menu_items_",
    ends={
        Property(name="add_Edit_Delete_menus_menu_items_16", type=Add_Edit_Delete_menus_menu_items__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin17", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Add_user_and_Assign_role: BinaryAssociation = BinaryAssociation(
    name="Admin_Add_user_and_Assign_role",
    ends={
        Property(name="add_user_and_Assign_role18", type=Add_user_and_Assign_role_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin19", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_View_order_transation: BinaryAssociation = BinaryAssociation(
    name="Admin_View_order_transation",
    ends={
        Property(name="view_order_transation20", type=View_order_transation_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin21", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Update_status_of_orders: BinaryAssociation = BinaryAssociation(
    name="Admin_Update_status_of_orders",
    ends={
        Property(name="update_status_of_orders22", type=Update_status_of_orders_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin23", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Operator_Login_Logout: BinaryAssociation = BinaryAssociation(
    name="Operator_Login_Logout",
    ends={
        Property(name="login_Logout24", type=Login_Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="operator25", type=Operator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Operator_View_order_transation: BinaryAssociation = BinaryAssociation(
    name="Operator_View_order_transation",
    ends={
        Property(name="view_order_transation26", type=View_order_transation_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="operator27", type=Operator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Operator_Add_Edit_Delete_menus: BinaryAssociation = BinaryAssociation(
    name="Operator_Add_Edit_Delete_menus",
    ends={
        Property(name="add_Edit_Delete_menus28", type=Add_Edit_Delete_menus_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="operator29", type=Operator_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f9ac04d4_299a_4096_81cb_2c42ca37da5e",
    types={View_order_transation_UseCase, Update_status_of_orders_UseCase, Operator_Actor, Login_Logout_UseCase, View_order_transation_UseCase1, Add_Edit_Delete_menus_UseCase, Food, Customer_Actor, Log_in_logout_UseCase, order_food_UseCase, Write_Review_UseCase, See_order_Status_UseCase, View_open_bill_and_ordered_items_UseCase, View_Food_products_UseCase, Edit_personal_Information_UseCase, Admin_Actor, Access_the_system_UseCase, Add_Edit_Delete_menus_menu_items__UseCase, Add_user_and_Assign_role_UseCase},
    associations={Customer_Log_in_logout, Customer_View_Food_products, Customer_order_food, Customer_View_open_bill_and_ordered_items, Customer_Edit_personal_Information, Customer_See_order_Status, Customer_Write_Review, Admin_Access_the_system, Admin_Add_Edit_Delete_menus_menu_items_, Admin_Add_user_and_Assign_role, Admin_View_order_transation, Admin_Update_status_of_orders, Operator_Login_Logout, Operator_View_order_transation, Operator_Add_Edit_Delete_menus},
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