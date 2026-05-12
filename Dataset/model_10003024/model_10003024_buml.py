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
Currency: Enumeration = Enumeration(
    name="Currency",
    literals={
            
    }
)

Package_ExpenseStatus: Enumeration = Enumeration(
    name="Package_ExpenseStatus",
    literals={
            
    }
)

Package_PaymentMethod: Enumeration = Enumeration(
    name="Package_PaymentMethod",
    literals={
            
    }
)

# Classes
My_Expenses_general_use_case_diagram_Component = Class(name="My_Expenses_general_use_case_diagram_Component")
Collaborator_Actor = Class(name="Collaborator_Actor")
Manager_Actor = Class(name="Manager_Actor")
Office_Manager_Actor = Class(name="Office_Manager_Actor")
Administrator_Actor = Class(name="Administrator_Actor")
Sales_agent_Actor = Class(name="Sales_agent_Actor")
Super_Administrator_Actor = Class(name="Super_Administrator_Actor")
Manage_Expenses_Component = Class(name="Manage_Expenses_Component")
Manage_attached_files_UseCase = Class(name="Manage_attached_files_UseCase")
Upload_a_file_UseCase = Class(name="Upload_a_file_UseCase")
Delete_an_attached_file_UseCase = Class(name="Delete_an_attached_file_UseCase")
Consult_an_attched_file_UseCase = Class(name="Consult_an_attched_file_UseCase")
Download_an_attached_file_UseCase = Class(name="Download_an_attached_file_UseCase")
Collaborator_Actor1 = Class(name="Collaborator_Actor1")
Consult_collaborators__Expenses_Component = Class(name="Consult_collaborators__Expenses_Component")
Sales_Agent_Actor = Class(name="Sales_Agent_Actor")
Authenticate_UseCase = Class(name="Authenticate_UseCase")
Office_Manager_Actor1 = Class(name="Office_Manager_Actor1")
Manager_Actor1 = Class(name="Manager_Actor1")
Review_collaborators__Expense_refunds_Component = Class(name="Review_collaborators__Expense_refunds_Component")
Manager_Actor2 = Class(name="Manager_Actor2")
Manager_Actor3 = Class(name="Manager_Actor3")
Manage_Expenses__settings_Component = Class(name="Manage_Expenses__settings_Component")
Package_Expense = Class(name="Package_Expense")
Package_Bill = Class(name="Package_Bill")
Package_Comment = Class(name="Package_Comment")
Package_Currency = Class(name="Package_Currency")
Package_ExpenseType = Class(name="Package_ExpenseType")
Consult_Expenses_external = Class(name="Consult_Expenses_external")
Search_Expenses_external = Class(name="Search_Expenses_external")
Filter_Expenses_external = Class(name="Filter_Expenses_external")
Validate_collaborators__Expense_refunds_external = Class(name="Validate_collaborators__Expense_refunds_external")
Refuse_collaborators__Expense_refunds_external = Class(name="Refuse_collaborators__Expense_refunds_external")
Manage_Expense_types_external = Class(name="Manage_Expense_types_external")
Manage_Expense_currency_external = Class(name="Manage_Expense_currency_external")
Manage_Expenses_external = Class(name="Manage_Expenses_external")
Consult_collaborators__Expenses_external = Class(name="Consult_collaborators__Expenses_external")
Review_collaborators__Expense_refunds_external = Class(name="Review_collaborators__Expense_refunds_external")
Refund_Expenses_external = Class(name="Refund_Expenses_external")
Manage_Expenses__settings_external = Class(name="Manage_Expenses__settings_external")
Verify_collaborators__Expenses_external = Class(name="Verify_collaborators__Expenses_external")
Create_an_Expense_external = Class(name="Create_an_Expense_external")
Update_an_Expense_external = Class(name="Update_an_Expense_external")
Send_an_Expenses_to_verification_external = Class(name="Send_an_Expenses_to_verification_external")
Delete_an_Expense_external = Class(name="Delete_an_Expense_external")

# My_Expenses_general_use_case_diagram_Component class attributes and methods

# Collaborator_Actor class attributes and methods

# Manager_Actor class attributes and methods

# Office_Manager_Actor class attributes and methods

# Administrator_Actor class attributes and methods

# Sales_agent_Actor class attributes and methods

# Super_Administrator_Actor class attributes and methods

# Manage_Expenses_Component class attributes and methods

# Manage_attached_files_UseCase class attributes and methods

# Upload_a_file_UseCase class attributes and methods

# Delete_an_attached_file_UseCase class attributes and methods

# Consult_an_attched_file_UseCase class attributes and methods

# Download_an_attached_file_UseCase class attributes and methods

# Collaborator_Actor1 class attributes and methods

# Consult_collaborators__Expenses_Component class attributes and methods

# Sales_Agent_Actor class attributes and methods

# Authenticate_UseCase class attributes and methods

# Office_Manager_Actor1 class attributes and methods

# Manager_Actor1 class attributes and methods

# Review_collaborators__Expense_refunds_Component class attributes and methods

# Manager_Actor2 class attributes and methods

# Manager_Actor3 class attributes and methods

# Manage_Expenses__settings_Component class attributes and methods

# Package_Expense class attributes and methods
Package_Expense_project_id: Property = Property(name="project_id", type=StringType)
Package_Expense_id: Property = Property(name="id", type=StringType)
Package_Expense_user_id: Property = Property(name="user_id", type=StringType)
Package_Expense_manager_id: Property = Property(name="manager_id", type=StringType)
Package_Expense_mission_id: Property = Property(name="mission_id", type=StringType)
Package_Expense.attributes={Package_Expense_manager_id, Package_Expense_user_id, Package_Expense_project_id, Package_Expense_id, Package_Expense_mission_id}

# Package_Bill class attributes and methods
Package_Bill_id: Property = Property(name="id", type=StringType)
Package_Bill_date: Property = Property(name="date", type=StringType)
Package_Bill_payment_method: Property = Property(name="payment_method", type=Package_PaymentMethod)
Package_Bill_attachment_id: Property = Property(name="attachment_id", type=StringType)
Package_Bill_sum: Property = Property(name="sum", type=StringType)
Package_Bill_status: Property = Property(name="status", type=Package_ExpenseStatus)
Package_Bill_distance: Property = Property(name="distance", type=StringType)
Package_Bill.attributes={Package_Bill_date, Package_Bill_payment_method, Package_Bill_sum, Package_Bill_status, Package_Bill_id, Package_Bill_attachment_id, Package_Bill_distance}

# Package_Comment class attributes and methods
Package_Comment_id: Property = Property(name="id", type=StringType)
Package_Comment_user_id: Property = Property(name="user_id", type=StringType)
Package_Comment_text: Property = Property(name="text", type=StringType)
Package_Comment.attributes={Package_Comment_text, Package_Comment_user_id, Package_Comment_id}

# Package_Currency class attributes and methods
Package_Currency_id: Property = Property(name="id", type=StringType)
Package_Currency_name: Property = Property(name="name", type=StringType)
Package_Currency_abr: Property = Property(name="abr", type=StringType)
Package_Currency.attributes={Package_Currency_abr, Package_Currency_name, Package_Currency_id}

# Package_ExpenseType class attributes and methods
Package_ExpenseType_id: Property = Property(name="id", type=StringType)
Package_ExpenseType_name: Property = Property(name="name", type=StringType)
Package_ExpenseType_price: Property = Property(name="price", type=StringType)
Package_ExpenseType.attributes={Package_ExpenseType_name, Package_ExpenseType_id, Package_ExpenseType_price}

# Consult_Expenses_external class attributes and methods

# Search_Expenses_external class attributes and methods

# Filter_Expenses_external class attributes and methods

# Validate_collaborators__Expense_refunds_external class attributes and methods

# Refuse_collaborators__Expense_refunds_external class attributes and methods

# Manage_Expense_types_external class attributes and methods

# Manage_Expense_currency_external class attributes and methods

# Manage_Expenses_external class attributes and methods

# Consult_collaborators__Expenses_external class attributes and methods

# Review_collaborators__Expense_refunds_external class attributes and methods

# Refund_Expenses_external class attributes and methods

# Manage_Expenses__settings_external class attributes and methods

# Verify_collaborators__Expenses_external class attributes and methods

# Create_an_Expense_external class attributes and methods

# Update_an_Expense_external class attributes and methods

# Send_an_Expenses_to_verification_external class attributes and methods

# Delete_an_Expense_external class attributes and methods

# Relationships
Collaborator_Delete_an_Expense_Report: BinaryAssociation = BinaryAssociation(
    name="Collaborator_Delete_an_Expense_Report",
    ends={
        Property(name="delete_an_Expense_Report18", type=Delete_an_Expense_external, multiplicity=Multiplicity(0, 1)),
        Property(name="collaborator19", type=Collaborator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Collaborator_View_an_Expense_Report: BinaryAssociation = BinaryAssociation(
    name="Collaborator_View_an_Expense_Report",
    ends={
        Property(name="view_an_Expense_Report20", type=Consult_Expenses_external, multiplicity=Multiplicity(0, 1)),
        Property(name="collaborator21", type=Collaborator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Sales_Agent_Search_Expenses: BinaryAssociation = BinaryAssociation(
    name="Sales_Agent_Search_Expenses",
    ends={
        Property(name="search_Expenses22", type=Search_Expenses_external, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Agent23", type=Sales_Agent_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Sales_Agent_Filter_Expenses: BinaryAssociation = BinaryAssociation(
    name="Sales_Agent_Filter_Expenses",
    ends={
        Property(name="filter_Expenses24", type=Filter_Expenses_external, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Agent25", type=Sales_Agent_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Validate_collaborators__Expense_refunds: BinaryAssociation = BinaryAssociation(
    name="Manager_Validate_collaborators__Expense_refunds",
    ends={
        Property(name="validate_collaborators__Expense_refunds26", type=Validate_collaborators__Expense_refunds_external, multiplicity=Multiplicity(0, 1)),
        Property(name="manager27", type=Manager_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Refuse_collaborators__Expense_refunds: BinaryAssociation = BinaryAssociation(
    name="Manager_Refuse_collaborators__Expense_refunds",
    ends={
        Property(name="refuse_collaborators__Expense_refunds28", type=Refuse_collaborators__Expense_refunds_external, multiplicity=Multiplicity(0, 1)),
        Property(name="manager29", type=Manager_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Validate_collaborators__Expense_refunds2: BinaryAssociation = BinaryAssociation(
    name="Manager_Validate_collaborators__Expense_refunds2",
    ends={
        Property(name="validate_collaborators__Expense_refunds30", type=Manage_Expense_types_external, multiplicity=Multiplicity(0, 1)),
        Property(name="manager31", type=Manager_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Collaborator_Manage_Expense_Report: BinaryAssociation = BinaryAssociation(
    name="Collaborator_Manage_Expense_Report",
    ends={
        Property(name="manage_Expense_Report0", type=Manage_Expenses_external, multiplicity=Multiplicity(0, 1)),
        Property(name="collaborator1", type=Collaborator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Sales_agent_Consult_collaborators__Expense_reports: BinaryAssociation = BinaryAssociation(
    name="Sales_agent_Consult_collaborators__Expense_reports",
    ends={
        Property(name="consult_collaborators__Expense_reports2", type=Consult_collaborators__Expenses_external, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_agent3", type=Sales_agent_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Review_collaborators__Expense_reports: BinaryAssociation = BinaryAssociation(
    name="Manager_Review_collaborators__Expense_reports",
    ends={
        Property(name="review_collaborators__Expense_reports4", type=Review_collaborators__Expense_refunds_external, multiplicity=Multiplicity(0, 1)),
        Property(name="manager5", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Office_Manager_Manage_refunds: BinaryAssociation = BinaryAssociation(
    name="Office_Manager_Manage_refunds",
    ends={
        Property(name="manage_refunds6", type=Refund_Expenses_external, multiplicity=Multiplicity(0, 1)),
        Property(name="office_Manager7", type=Office_Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Manage_Expense_report_settings: BinaryAssociation = BinaryAssociation(
    name="Administrator_Manage_Expense_report_settings",
    ends={
        Property(name="manage_Expense_report_settings8", type=Manage_Expenses__settings_external, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator9", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Office_Manager_Verify_collaborators__Expense_reports: BinaryAssociation = BinaryAssociation(
    name="Office_Manager_Verify_collaborators__Expense_reports",
    ends={
        Property(name="verify_collaborators__Expense_reports10", type=Verify_collaborators__Expenses_external, multiplicity=Multiplicity(0, 1)),
        Property(name="office_Manager11", type=Office_Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Collaborator_Create_an_Expense_Report: BinaryAssociation = BinaryAssociation(
    name="Collaborator_Create_an_Expense_Report",
    ends={
        Property(name="create_an_Expense_Report12", type=Create_an_Expense_external, multiplicity=Multiplicity(0, 1)),
        Property(name="collaborator13", type=Collaborator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Collaborator_Update_an_Expense_Report: BinaryAssociation = BinaryAssociation(
    name="Collaborator_Update_an_Expense_Report",
    ends={
        Property(name="update_an_Expense_Report14", type=Update_an_Expense_external, multiplicity=Multiplicity(0, 1)),
        Property(name="collaborator15", type=Collaborator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Collaborator_Send_an_Expense_Report_to_verification: BinaryAssociation = BinaryAssociation(
    name="Collaborator_Send_an_Expense_Report_to_verification",
    ends={
        Property(name="send_an_Expense_Report_to_verification16", type=Send_an_Expenses_to_verification_external, multiplicity=Multiplicity(0, 1)),
        Property(name="collaborator17", type=Collaborator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Refuse_collaborators__Expense_refunds2: BinaryAssociation = BinaryAssociation(
    name="Manager_Refuse_collaborators__Expense_refunds2",
    ends={
        Property(name="refuse_collaborators__Expense_refunds32", type=Manage_Expense_currency_external, multiplicity=Multiplicity(0, 1)),
        Property(name="manager33", type=Manager_Actor3, multiplicity=Multiplicity(0, 1))
    }
)
Collaborator_Manage_attached_files: BinaryAssociation = BinaryAssociation(
    name="Collaborator_Manage_attached_files",
    ends={
        Property(name="manage_attached_files34", type=Manage_attached_files_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="collaborator35", type=Collaborator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Expense_Comment: BinaryAssociation = BinaryAssociation(
    name="Expense_Comment",
    ends={
        Property(name="Expense_Comment_036", type=Package_Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="Expense_Comment_137", type=Package_Bill, multiplicity=Multiplicity(1, 1))
    }
)
Expense_Bill: BinaryAssociation = BinaryAssociation(
    name="Expense_Bill",
    ends={
        Property(name="Expense_Bill_038", type=Package_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="Expense_Bill_139", type=Package_Expense, multiplicity=Multiplicity(0, 1))
    }
)
Currency_Expense: BinaryAssociation = BinaryAssociation(
    name="Currency_Expense",
    ends={
        Property(name="Currency_Expense_040", type=Package_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="Currency_Expense_141", type=Package_Currency, multiplicity=Multiplicity(1, 1))
    }
)
ExpenseType_Bill: BinaryAssociation = BinaryAssociation(
    name="ExpenseType_Bill",
    ends={
        Property(name="ExpenseType_Bill_042", type=Package_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="ExpenseType_Bill_143", type=Package_ExpenseType, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f658a104_dd9d_494f_9332_e43921dfccfe",
    types={My_Expenses_general_use_case_diagram_Component, Collaborator_Actor, Manager_Actor, Office_Manager_Actor, Administrator_Actor, Sales_agent_Actor, Super_Administrator_Actor, Manage_Expenses_Component, Manage_attached_files_UseCase, Upload_a_file_UseCase, Delete_an_attached_file_UseCase, Consult_an_attched_file_UseCase, Download_an_attached_file_UseCase, Collaborator_Actor1, Consult_collaborators__Expenses_Component, Sales_Agent_Actor, Authenticate_UseCase, Office_Manager_Actor1, Manager_Actor1, Review_collaborators__Expense_refunds_Component, Manager_Actor2, Manager_Actor3, Manage_Expenses__settings_Component, Package_Expense, Package_Bill, Package_Comment, Package_Currency, Package_ExpenseType, Consult_Expenses_external, Search_Expenses_external, Filter_Expenses_external, Validate_collaborators__Expense_refunds_external, Refuse_collaborators__Expense_refunds_external, Manage_Expense_types_external, Manage_Expense_currency_external, Manage_Expenses_external, Consult_collaborators__Expenses_external, Review_collaborators__Expense_refunds_external, Refund_Expenses_external, Manage_Expenses__settings_external, Verify_collaborators__Expenses_external, Create_an_Expense_external, Update_an_Expense_external, Send_an_Expenses_to_verification_external, Delete_an_Expense_external, Currency, Package_ExpenseStatus, Package_PaymentMethod},
    associations={Collaborator_Delete_an_Expense_Report, Collaborator_View_an_Expense_Report, Sales_Agent_Search_Expenses, Sales_Agent_Filter_Expenses, Manager_Validate_collaborators__Expense_refunds, Manager_Refuse_collaborators__Expense_refunds, Manager_Validate_collaborators__Expense_refunds2, Collaborator_Manage_Expense_Report, Sales_agent_Consult_collaborators__Expense_reports, Manager_Review_collaborators__Expense_reports, Office_Manager_Manage_refunds, Administrator_Manage_Expense_report_settings, Office_Manager_Verify_collaborators__Expense_reports, Collaborator_Create_an_Expense_Report, Collaborator_Update_an_Expense_Report, Collaborator_Send_an_Expense_Report_to_verification, Manager_Refuse_collaborators__Expense_refunds2, Collaborator_Manage_attached_files, Expense_Comment, Expense_Bill, Currency_Expense, ExpenseType_Bill},
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