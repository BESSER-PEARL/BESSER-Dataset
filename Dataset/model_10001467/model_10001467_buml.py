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
Create_Account_UseCase = Class(name="Create_Account_UseCase")
Login_UseCase = Class(name="Login_UseCase")
View_Menu_UseCase = Class(name="View_Menu_UseCase")
Add_Items_to_Cart_UseCase = Class(name="Add_Items_to_Cart_UseCase")
Check_Out_UseCase = Class(name="Check_Out_UseCase")
Make_Payment_UseCase = Class(name="Make_Payment_UseCase")
Confirmation_e_mail_UseCase = Class(name="Confirmation_e_mail_UseCase")
Void_Order_UseCase = Class(name="Void_Order_UseCase")
Admin_Actor = Class(name="Admin_Actor")
Delivery_Person_Actor = Class(name="Delivery_Person_Actor")
Receive_Order_UseCase = Class(name="Receive_Order_UseCase")
Deliver_Order_UseCase = Class(name="Deliver_Order_UseCase")
Register__UseCase = Class(name="Register__UseCase")
System_Actor = Class(name="System_Actor")
Generate_report_UseCase = Class(name="Generate_report_UseCase")
Update_Menu_Info_UseCase = Class(name="Update_Menu_Info_UseCase")
Menu = Class(name="Menu")
Class_ = Class(name="Class")

# Customer_Actor class attributes and methods

# Create_Account_UseCase class attributes and methods

# Login_UseCase class attributes and methods

# View_Menu_UseCase class attributes and methods

# Add_Items_to_Cart_UseCase class attributes and methods

# Check_Out_UseCase class attributes and methods

# Make_Payment_UseCase class attributes and methods

# Confirmation_e_mail_UseCase class attributes and methods

# Void_Order_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# Delivery_Person_Actor class attributes and methods

# Receive_Order_UseCase class attributes and methods

# Deliver_Order_UseCase class attributes and methods

# Register__UseCase class attributes and methods

# System_Actor class attributes and methods

# Generate_report_UseCase class attributes and methods

# Update_Menu_Info_UseCase class attributes and methods

# Menu class attributes and methods
Menu_attribute: Property = Property(name="attribute", type=StringType)
Menu.attributes={Menu_attribute}

# Class class attributes and methods

# Relationships
Customer_Check_Out: BinaryAssociation = BinaryAssociation(
    name="Customer_Check_Out",
    ends={
        Property(name="customer9", type=Customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_Out8", type=Check_Out_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Make_Payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Make_Payment",
    ends={
        Property(name="make_Payment10", type=Make_Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Confirmation_e_mail: BinaryAssociation = BinaryAssociation(
    name="Customer_Confirmation_e_mail",
    ends={
        Property(name="confirmation_e_mail12", type=Confirmation_e_mail_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Cancel_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Cancel_Order",
    ends={
        Property(name="cancel_Order14", type=Void_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer15", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Create_Account_Admin: BinaryAssociation = BinaryAssociation(
    name="Create_Account_Admin",
    ends={
        Property(name="admin16", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="create_Account17", type=Create_Account_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Login_Admin: BinaryAssociation = BinaryAssociation(
    name="Login_Admin",
    ends={
        Property(name="admin18", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login19", type=Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
View_Menu_Admin: BinaryAssociation = BinaryAssociation(
    name="View_Menu_Admin",
    ends={
        Property(name="admin20", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_Menu21", type=View_Menu_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Add_Items_to_Cart_Admin: BinaryAssociation = BinaryAssociation(
    name="Add_Items_to_Cart_Admin",
    ends={
        Property(name="admin22", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="add_Items_to_Cart23", type=Add_Items_to_Cart_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Check_Out_Admin: BinaryAssociation = BinaryAssociation(
    name="Check_Out_Admin",
    ends={
        Property(name="admin24", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_Out25", type=Check_Out_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Make_Payment_Admin: BinaryAssociation = BinaryAssociation(
    name="Make_Payment_Admin",
    ends={
        Property(name="admin26", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="make_Payment27", type=Make_Payment_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Confirmation_e_mail_Admin: BinaryAssociation = BinaryAssociation(
    name="Confirmation_e_mail_Admin",
    ends={
        Property(name="admin28", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="confirmation_e_mail29", type=Confirmation_e_mail_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Cancel_Order_Admin: BinaryAssociation = BinaryAssociation(
    name="Cancel_Order_Admin",
    ends={
        Property(name="admin30", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="cancel_Order31", type=Void_Order_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Delivery_Person_Receive_Order: BinaryAssociation = BinaryAssociation(
    name="Delivery_Person_Receive_Order",
    ends={
        Property(name="receive_Order32", type=Receive_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="delivery_Person33", type=Delivery_Person_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Delivery_Person_Deliver_Order: BinaryAssociation = BinaryAssociation(
    name="Delivery_Person_Deliver_Order",
    ends={
        Property(name="deliver_Order34", type=Deliver_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="delivery_Person35", type=Delivery_Person_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Delivery_Person_Register: BinaryAssociation = BinaryAssociation(
    name="Delivery_Person_Register",
    ends={
        Property(name="register36", type=Register__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="delivery_Person37", type=Delivery_Person_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Register: BinaryAssociation = BinaryAssociation(
    name="Admin_Register",
    ends={
        Property(name="register38", type=Register__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin39", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Receive_Order: BinaryAssociation = BinaryAssociation(
    name="Admin_Receive_Order",
    ends={
        Property(name="receive_Order40", type=Receive_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin41", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Deliver_Order_Admin: BinaryAssociation = BinaryAssociation(
    name="Deliver_Order_Admin",
    ends={
        Property(name="admin42", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="deliver_Order43", type=Deliver_Order_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Generate_report: BinaryAssociation = BinaryAssociation(
    name="Admin_Generate_report",
    ends={
        Property(name="generate_report44", type=Generate_report_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin45", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Generate_report_System: BinaryAssociation = BinaryAssociation(
    name="Generate_report_System",
    ends={
        Property(name="system46", type=System_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="generate_report47", type=Generate_report_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Update_Menu_Info: BinaryAssociation = BinaryAssociation(
    name="Admin_Update_Menu_Info",
    ends={
        Property(name="update_Menu_Info48", type=Update_Menu_Info_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin49", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Update_Menu_Info_System: BinaryAssociation = BinaryAssociation(
    name="Update_Menu_Info_System",
    ends={
        Property(name="system50", type=System_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="update_Menu_Info51", type=Update_Menu_Info_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Create_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Create_Account",
    ends={
        Property(name="create_Account0", type=Create_Account_UseCase, multiplicity=Multiplicity(0, 1)),
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
Customer_View_Menu: BinaryAssociation = BinaryAssociation(
    name="Customer_View_Menu",
    ends={
        Property(name="view_Menu4", type=View_Menu_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Add_Items_to_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Add_Items_to_Cart",
    ends={
        Property(name="add_Items_to_Cart6", type=Add_Items_to_Cart_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8kQ1YNLaEeiczqJWtOPN4Q",
    types={Customer_Actor, Create_Account_UseCase, Login_UseCase, View_Menu_UseCase, Add_Items_to_Cart_UseCase, Check_Out_UseCase, Make_Payment_UseCase, Confirmation_e_mail_UseCase, Void_Order_UseCase, Admin_Actor, Delivery_Person_Actor, Receive_Order_UseCase, Deliver_Order_UseCase, Register__UseCase, System_Actor, Generate_report_UseCase, Update_Menu_Info_UseCase, Menu, Class_},
    associations={Customer_Check_Out, Customer_Make_Payment, Customer_Confirmation_e_mail, Customer_Cancel_Order, Create_Account_Admin, Login_Admin, View_Menu_Admin, Add_Items_to_Cart_Admin, Check_Out_Admin, Make_Payment_Admin, Confirmation_e_mail_Admin, Cancel_Order_Admin, Delivery_Person_Receive_Order, Delivery_Person_Deliver_Order, Delivery_Person_Register, Admin_Register, Admin_Receive_Order, Deliver_Order_Admin, Admin_Generate_report, Generate_report_System, Admin_Update_Menu_Info, Update_Menu_Info_System, Customer_Create_Account, Customer_Login, Customer_View_Menu, Customer_Add_Items_to_Cart},
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