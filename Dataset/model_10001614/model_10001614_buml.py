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
Customer1_Actor = Class(name="Customer1_Actor")
Warehouse_man_Actor = Class(name="Warehouse_man_Actor")
Warehouse_department_Actor = Class(name="Warehouse_department_Actor")
delivery_man_Actor = Class(name="delivery_man_Actor")
Supper_System_Start_Shopping_UseCase = Class(name="Supper_System_Start_Shopping_UseCase")
Supper_System_View_Product_UseCase = Class(name="Supper_System_View_Product_UseCase")
Supper_System_Add_product_UseCase = Class(name="Supper_System_Add_product_UseCase")
Supper_System_Search_product_UseCase = Class(name="Supper_System_Search_product_UseCase")
Supper_System_Update_order_list_UseCase = Class(name="Supper_System_Update_order_list_UseCase")
Supper_System_Create_order_list_UseCase = Class(name="Supper_System_Create_order_list_UseCase")
Supper_System_Checkout_UseCase = Class(name="Supper_System_Checkout_UseCase")
Supper_System_Verify_Customer_information_UseCase = Class(name="Supper_System_Verify_Customer_information_UseCase")
Supper_System_Confirm_payment_UseCase = Class(name="Supper_System_Confirm_payment_UseCase")
Supper_System_Update_unit_number_UseCase = Class(name="Supper_System_Update_unit_number_UseCase")
Supper_System_View_invoice_on_screen_UseCase = Class(name="Supper_System_View_invoice_on_screen_UseCase")
Supper_System_Print_invoice_UseCase = Class(name="Supper_System_Print_invoice_UseCase")
Supper_System_Save_invoice_UseCase = Class(name="Supper_System_Save_invoice_UseCase")
Supper_System_prepare_package_UseCase = Class(name="Supper_System_prepare_package_UseCase")
Supper_System_schedule_for_delivery_UseCase = Class(name="Supper_System_schedule_for_delivery_UseCase")
Supper_System_Email_reminder_UseCase = Class(name="Supper_System_Email_reminder_UseCase")
Supper_System_Collect_package_UseCase = Class(name="Supper_System_Collect_package_UseCase")
Supper_System_Sign_delivery_notice_UseCase = Class(name="Supper_System_Sign_delivery_notice_UseCase")
Supper_System_Return_defective_items_UseCase = Class(name="Supper_System_Return_defective_items_UseCase")
Supper_System_Return_items_UseCase = Class(name="Supper_System_Return_items_UseCase")
Supper_System_Pay_Shipping_Fees_UseCase = Class(name="Supper_System_Pay_Shipping_Fees_UseCase")
Supper_System_Create_account_UseCase = Class(name="Supper_System_Create_account_UseCase")
Supper_System_Login_UseCase = Class(name="Supper_System_Login_UseCase")
Supper_System_Check_item_availability_UseCase = Class(name="Supper_System_Check_item_availability_UseCase")
Supper_System_Deliver_Package_UseCase = Class(name="Supper_System_Deliver_Package_UseCase")
Supper_System_Receive_package_UseCase = Class(name="Supper_System_Receive_package_UseCase")
Credit_Card_company_Actor = Class(name="Credit_Card_company_Actor")
prepare_package_UseCase = Class(name="prepare_package_UseCase")
Customer1_Actor1 = Class(name="Customer1_Actor1")
Class_ = Class(name="Class")
djkd = Class(name="djkd")
fsdf = Class(name="fsdf")

# Customer1_Actor class attributes and methods

# Warehouse_man_Actor class attributes and methods

# Warehouse_department_Actor class attributes and methods

# delivery_man_Actor class attributes and methods

# Supper_System_Start_Shopping_UseCase class attributes and methods

# Supper_System_View_Product_UseCase class attributes and methods

# Supper_System_Add_product_UseCase class attributes and methods

# Supper_System_Search_product_UseCase class attributes and methods

# Supper_System_Update_order_list_UseCase class attributes and methods

# Supper_System_Create_order_list_UseCase class attributes and methods

# Supper_System_Checkout_UseCase class attributes and methods

# Supper_System_Verify_Customer_information_UseCase class attributes and methods

# Supper_System_Confirm_payment_UseCase class attributes and methods

# Supper_System_Update_unit_number_UseCase class attributes and methods

# Supper_System_View_invoice_on_screen_UseCase class attributes and methods

# Supper_System_Print_invoice_UseCase class attributes and methods

# Supper_System_Save_invoice_UseCase class attributes and methods

# Supper_System_prepare_package_UseCase class attributes and methods

# Supper_System_schedule_for_delivery_UseCase class attributes and methods

# Supper_System_Email_reminder_UseCase class attributes and methods

# Supper_System_Collect_package_UseCase class attributes and methods

# Supper_System_Sign_delivery_notice_UseCase class attributes and methods

# Supper_System_Return_defective_items_UseCase class attributes and methods

# Supper_System_Return_items_UseCase class attributes and methods

# Supper_System_Pay_Shipping_Fees_UseCase class attributes and methods

# Supper_System_Create_account_UseCase class attributes and methods

# Supper_System_Login_UseCase class attributes and methods

# Supper_System_Check_item_availability_UseCase class attributes and methods

# Supper_System_Deliver_Package_UseCase class attributes and methods

# Supper_System_Receive_package_UseCase class attributes and methods

# Credit_Card_company_Actor class attributes and methods

# prepare_package_UseCase class attributes and methods

# Customer1_Actor1 class attributes and methods

# Class class attributes and methods

# djkd class attributes and methods

# fsdf class attributes and methods
fsdf_fdasf: Property = Property(name="fdasf", type=IntegerType)
fsdf.attributes={fsdf_fdasf}

# Relationships
Verify_Customer_information_Credit_Card_company: BinaryAssociation = BinaryAssociation(
    name="Verify_Customer_information_Credit_Card_company",
    ends={
        Property(name="credit_Card_company0", type=Credit_Card_company_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="verify_Customer_information1", type=Supper_System_Verify_Customer_information_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Create_order_list_Warehouse_department: BinaryAssociation = BinaryAssociation(
    name="Create_order_list_Warehouse_department",
    ends={
        Property(name="warehouse_department2", type=Warehouse_department_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="create_order_list3", type=Supper_System_Checkout_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Email_reminder_Customer1: BinaryAssociation = BinaryAssociation(
    name="Email_reminder_Customer1",
    ends={
        Property(name="customer14", type=Customer1_Actor1, multiplicity=Multiplicity(0, 1)),
        Property(name="email_reminder5", type=Supper_System_Email_reminder_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
schedule_for_delivery_delivery_man: BinaryAssociation = BinaryAssociation(
    name="schedule_for_delivery_delivery_man",
    ends={
        Property(name="delivery_man6", type=delivery_man_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="schedule_for_delivery7", type=Supper_System_Deliver_Package_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Sign_delivery_notice_delivery_man: BinaryAssociation = BinaryAssociation(
    name="Sign_delivery_notice_delivery_man",
    ends={
        Property(name="delivery_man8", type=delivery_man_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sign_delivery_notice9", type=Supper_System_Sign_delivery_notice_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Create_account_Customer1: BinaryAssociation = BinaryAssociation(
    name="Create_account_Customer1",
    ends={
        Property(name="customer110", type=Customer1_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="create_account11", type=Supper_System_Create_account_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Warehouse_man_prepare_package: BinaryAssociation = BinaryAssociation(
    name="Warehouse_man_prepare_package",
    ends={
        Property(name="prepare_package12", type=Supper_System_prepare_package_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="warehouse_man13", type=Warehouse_man_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer1_Create_account: BinaryAssociation = BinaryAssociation(
    name="Customer1_Create_account",
    ends={
        Property(name="create_account14", type=Supper_System_Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer115", type=Customer1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer1_Receive_package: BinaryAssociation = BinaryAssociation(
    name="Customer1_Receive_package",
    ends={
        Property(name="receive_package16", type=Supper_System_Receive_package_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer117", type=Customer1_Actor1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_JUFnIPTXEemTHo7LQdQL6Q",
    types={Customer1_Actor, Warehouse_man_Actor, Warehouse_department_Actor, delivery_man_Actor, Supper_System_Start_Shopping_UseCase, Supper_System_View_Product_UseCase, Supper_System_Add_product_UseCase, Supper_System_Search_product_UseCase, Supper_System_Update_order_list_UseCase, Supper_System_Create_order_list_UseCase, Supper_System_Checkout_UseCase, Supper_System_Verify_Customer_information_UseCase, Supper_System_Confirm_payment_UseCase, Supper_System_Update_unit_number_UseCase, Supper_System_View_invoice_on_screen_UseCase, Supper_System_Print_invoice_UseCase, Supper_System_Save_invoice_UseCase, Supper_System_prepare_package_UseCase, Supper_System_schedule_for_delivery_UseCase, Supper_System_Email_reminder_UseCase, Supper_System_Collect_package_UseCase, Supper_System_Sign_delivery_notice_UseCase, Supper_System_Return_defective_items_UseCase, Supper_System_Return_items_UseCase, Supper_System_Pay_Shipping_Fees_UseCase, Supper_System_Create_account_UseCase, Supper_System_Login_UseCase, Supper_System_Check_item_availability_UseCase, Supper_System_Deliver_Package_UseCase, Supper_System_Receive_package_UseCase, Credit_Card_company_Actor, prepare_package_UseCase, Customer1_Actor1, Class_, djkd, fsdf},
    associations={Verify_Customer_information_Credit_Card_company, Create_order_list_Warehouse_department, Email_reminder_Customer1, schedule_for_delivery_delivery_man, Sign_delivery_notice_delivery_man, Create_account_Customer1, Warehouse_man_prepare_package, Customer1_Create_account, Customer1_Receive_package},
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