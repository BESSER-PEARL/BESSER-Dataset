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
account_statement__UseCase = Class(name="account_statement__UseCase")
add_new_beneficiary_UseCase = Class(name="add_new_beneficiary_UseCase")
modify_beneficiary_information_UseCase = Class(name="modify_beneficiary_information_UseCase")
print_beneficiary_information_UseCase = Class(name="print_beneficiary_information_UseCase")
delete_beneficiary__UseCase = Class(name="delete_beneficiary__UseCase")
print_beneficiaries_list_UseCase = Class(name="print_beneficiaries_list_UseCase")
Browse_based_care_type_UseCase = Class(name="Browse_based_care_type_UseCase")
Browse_based_name_UseCase = Class(name="Browse_based_name_UseCase")
Browse_based_Scientific_qualification_UseCase = Class(name="Browse_based_Scientific_qualification_UseCase")
Browse_based_Housing_kind_UseCase = Class(name="Browse_based_Housing_kind_UseCase")
Browse_based_age_UseCase = Class(name="Browse_based_age_UseCase")
Browse_based_number_of_children_UseCase = Class(name="Browse_based_number_of_children_UseCase")
add_new_volunteer_UseCase = Class(name="add_new_volunteer_UseCase")
add_honor_member_UseCase = Class(name="add_honor_member_UseCase")
display_all_UseCase = Class(name="display_all_UseCase")
Data_entry_employee__Actor = Class(name="Data_entry_employee__Actor")
Admin = Class(name="Admin")
Origination = Class(name="Origination")
Data_entry = Class(name="Data_entry")
Member = Class(name="Member")
Honor_member = Class(name="Honor_member")
Volunteer = Class(name="Volunteer")
Beneficiary = Class(name="Beneficiary")
Amount = Class(name="Amount")
Marriage_Demand = Class(name="Marriage_Demand")
Care = Class(name="Care")
Employee = Class(name="Employee")
Vacation = Class(name="Vacation")
Administrator__Actor = Class(name="Administrator__Actor")
display_organization_information_UseCase = Class(name="display_organization_information_UseCase")
change_his_password_UseCase = Class(name="change_his_password_UseCase")
change_the_organization_information__UseCase = Class(name="change_the_organization_information__UseCase")
add_new_data_entry_account_UseCase = Class(name="add_new_data_entry_account_UseCase")
delete_data_entry_account__UseCase = Class(name="delete_data_entry_account__UseCase")
display_data_entry_UseCase = Class(name="display_data_entry_UseCase")
display_employee_information_UseCase = Class(name="display_employee_information_UseCase")
add_employee_UseCase = Class(name="add_employee_UseCase")
modify_employee_data_UseCase = Class(name="modify_employee_data_UseCase")
delete_employee_UseCase = Class(name="delete_employee_UseCase")
manage_holiday_UseCase = Class(name="manage_holiday_UseCase")
print_employee_information_UseCase = Class(name="print_employee_information_UseCase")
Log_out_UseCase = Class(name="Log_out_UseCase")
Log_in__UseCase = Class(name="Log_in__UseCase")
change_his_password__UseCase = Class(name="change_his_password__UseCase")
display_beneficiaries_list_UseCase = Class(name="display_beneficiaries_list_UseCase")
display_volunteer_list_UseCase = Class(name="display_volunteer_list_UseCase")
modify_volunteer_data_UseCase = Class(name="modify_volunteer_data_UseCase")
delete_volunteer_UseCase = Class(name="delete_volunteer_UseCase")
print_volunteer_data_UseCase = Class(name="print_volunteer_data_UseCase")
display_honor_member_UseCase = Class(name="display_honor_member_UseCase")
print_honor_member_information__UseCase = Class(name="print_honor_member_information__UseCase")
modify_honor_member_information__UseCase = Class(name="modify_honor_member_information__UseCase")
delete_honor_member_UseCase = Class(name="delete_honor_member_UseCase")
_20Data_20entry_external = Class(name="_20Data_20entry_external")
The_20member_external = Class(name="The_20member_external")

# account_statement__UseCase class attributes and methods

# add_new_beneficiary_UseCase class attributes and methods

# modify_beneficiary_information_UseCase class attributes and methods

# print_beneficiary_information_UseCase class attributes and methods

# delete_beneficiary__UseCase class attributes and methods

# print_beneficiaries_list_UseCase class attributes and methods

# Browse_based_care_type_UseCase class attributes and methods

# Browse_based_name_UseCase class attributes and methods

# Browse_based_Scientific_qualification_UseCase class attributes and methods

# Browse_based_Housing_kind_UseCase class attributes and methods

# Browse_based_age_UseCase class attributes and methods

# Browse_based_number_of_children_UseCase class attributes and methods

# add_new_volunteer_UseCase class attributes and methods

# add_honor_member_UseCase class attributes and methods

# display_all_UseCase class attributes and methods

# Data_entry_employee__Actor class attributes and methods

# Admin class attributes and methods
Admin_ID: Property = Property(name="ID", type=IntegerType)
Admin_User_name: Property = Property(name="User_name", type=StringType)
Admin_Password: Property = Property(name="Password", type=IntegerType)
Admin.attributes={Admin_Password, Admin_User_name, Admin_ID}

# Origination class attributes and methods
Origination_Logo: Property = Property(name="Logo", type=StringType)
Origination_Full_name: Property = Property(name="Full_name", type=StringType)
Origination_Executive_manager: Property = Property(name="Executive_manager", type=StringType)
Origination_General_supervisor: Property = Property(name="General_supervisor", type=StringType)
Origination.attributes={Origination_General_supervisor, Origination_Full_name, Origination_Executive_manager, Origination_Logo}

# Data_entry class attributes and methods
Data_entry_attribute: Property = Property(name="attribute", type=StringType)
Data_entry_attribute2: Property = Property(name="attribute2", type=StringType)
Data_entry.attributes={Data_entry_attribute, Data_entry_attribute2}

# Member class attributes and methods
Member_F_name: Property = Property(name="F_name", type=StringType)
Member_L_name: Property = Property(name="L_name", type=StringType)
Member_Job: Property = Property(name="Job", type=StringType)
Member_Mobile_number: Property = Property(name="Mobile_number", type=IntegerType)
Member_Scientific_qualifications: Property = Property(name="Scientific_qualifications", type=StringType)
Member_Email_address: Property = Property(name="Email_address", type=StringType)
Member_Vacation_type: Property = Property(name="Vacation_type", type=StringType)
Member.attributes={Member_Scientific_qualifications, Member_Mobile_number, Member_Email_address, Member_Vacation_type, Member_L_name, Member_Job, Member_F_name}

# Honor_member class attributes and methods
Honor_member_Member_start_date: Property = Property(name="Member_start_date", type=StringType)
Honor_member_Amount_of_partnership: Property = Property(name="Amount_of_partnership", type=IntegerType)
Honor_member.attributes={Honor_member_Amount_of_partnership, Honor_member_Member_start_date}

# Volunteer class attributes and methods
Volunteer_Volunteer_ID: Property = Property(name="Volunteer_ID", type=IntegerType)
Volunteer_Age: Property = Property(name="Age", type=IntegerType)
Volunteer_Time_of_volunteering: Property = Property(name="Time_of_volunteering", type=StringType)
Volunteer_Preparing_event: Property = Property(name="Preparing_event", type=StringType)
Volunteer_Design_and_montag: Property = Property(name="Design_and_montag", type=StringType)
Volunteer_Public_relations: Property = Property(name="Public_relations", type=StringType)
Volunteer_Decor__and_aesthetic_touches: Property = Property(name="Decor__and_aesthetic_touches", type=StringType)
Volunteer_Organization: Property = Property(name="Organization", type=StringType)
Volunteer_Professional_status: Property = Property(name="Professional_status", type=StringType)
Volunteer.attributes={Volunteer_Volunteer_ID, Volunteer_Organization, Volunteer_Age, Volunteer_Preparing_event, Volunteer_Design_and_montag, Volunteer_Professional_status, Volunteer_Public_relations, Volunteer_Time_of_volunteering, Volunteer_Decor__and_aesthetic_touches}

# Beneficiary class attributes and methods
Beneficiary_Beneficiary__ID: Property = Property(name="Beneficiary__ID", type=IntegerType)
Beneficiary_F_name: Property = Property(name="F_name", type=StringType)
Beneficiary_L_name: Property = Property(name="L_name", type=StringType)
Beneficiary_Address: Property = Property(name="Address", type=StringType)
Beneficiary_District: Property = Property(name="District", type=StringType)
Beneficiary_Job: Property = Property(name="Job", type=StringType)
Beneficiary_House_number: Property = Property(name="House_number", type=IntegerType)
Beneficiary_Date_of_birth: Property = Property(name="Date_of_birth", type=StringType)
Beneficiary_Phone: Property = Property(name="Phone", type=IntegerType)
Beneficiary_Scientific_qualification: Property = Property(name="Scientific_qualification", type=StringType)
Beneficiary_Marital_status: Property = Property(name="Marital_status", type=StringType)
Beneficiary.attributes={Beneficiary_Address, Beneficiary_House_number, Beneficiary_Marital_status, Beneficiary_Date_of_birth, Beneficiary_Phone, Beneficiary_Scientific_qualification, Beneficiary_Job, Beneficiary_F_name, Beneficiary_L_name, Beneficiary_District, Beneficiary_Beneficiary__ID}

# Amount class attributes and methods
Amount_Amount: Property = Property(name="Amount", type=IntegerType)
Amount_Subvention_date: Property = Property(name="Subvention_date", type=StringType)
Amount_Month: Property = Property(name="Month", type=IntegerType)
Amount.attributes={Amount_Month, Amount_Amount, Amount_Subvention_date}

# Marriage_Demand class attributes and methods
Marriage_Demand_Nationality: Property = Property(name="Nationality", type=StringType)
Marriage_Demand_Nationality_of_the_mother: Property = Property(name="Nationality_of_the_mother", type=StringType)
Marriage_Demand_Tribe: Property = Property(name="Tribe", type=StringType)
Marriage_Demand_Legitimate_vision: Property = Property(name="Legitimate_vision", type=StringType)
Marriage_Demand_Salary: Property = Property(name="Salary", type=StringType)
Marriage_Demand_Marital_status_of_the_proposer: Property = Property(name="Marital_status_of_the_proposer", type=StringType)
Marriage_Demand_Educational_status: Property = Property(name="Educational_status", type=StringType)
Marriage_Demand_Other_district: Property = Property(name="Other_district", type=StringType)
Marriage_Demand_Accept_multi_marriage: Property = Property(name="Accept_multi_marriage", type=StringType)
Marriage_Demand_Relation_with_proposal: Property = Property(name="Relation_with_proposal", type=StringType)
Marriage_Demand.attributes={Marriage_Demand_Nationality_of_the_mother, Marriage_Demand_Other_district, Marriage_Demand_Marital_status_of_the_proposer, Marriage_Demand_Educational_status, Marriage_Demand_Tribe, Marriage_Demand_Legitimate_vision, Marriage_Demand_Accept_multi_marriage, Marriage_Demand_Relation_with_proposal, Marriage_Demand_Nationality, Marriage_Demand_Salary}

# Care class attributes and methods
Care_Care_sort: Property = Property(name="Care_sort", type=StringType)
Care_Civil_Registry: Property = Property(name="Civil_Registry", type=StringType)
Care_Street: Property = Property(name="Street", type=StringType)
Care_Workplace: Property = Property(name="Workplace", type=StringType)
Care_Health_status: Property = Property(name="Health_status", type=StringType)
Care_Children_health_status: Property = Property(name="Children_health_status", type=StringType)
Care_Income_sources: Property = Property(name="Income_sources", type=StringType)
Care_Income_amount: Property = Property(name="Income_amount", type=StringType)
Care_Housing_description: Property = Property(name="Housing_description", type=StringType)
Care_Housing_kind: Property = Property(name="Housing_kind", type=StringType)
Care_Number_of_children: Property = Property(name="Number_of_children", type=StringType)
Care_Family_members__The_number: Property = Property(name="Family_members__The_number", type=IntegerType)
Care_Guardian: Property = Property(name="Guardian", type=StringType)
Care_Relation_of_the_guardian: Property = Property(name="Relation_of_the_guardian", type=StringType)
Care_Profession_of_the_guardian: Property = Property(name="Profession_of_the_guardian", type=StringType)
Care_Workplace_the_guardian: Property = Property(name="Workplace_the_guardian", type=StringType)
Care_Monthly_income: Property = Property(name="Monthly_income", type=IntegerType)
Care_Adopting_degree: Property = Property(name="Adopting_degree", type=StringType)
Care_Family_bonding: Property = Property(name="Family_bonding", type=StringType)
Care_Interaction_degree: Property = Property(name="Interaction_degree", type=StringType)
Care.attributes={Care_Family_bonding, Care_Children_health_status, Care_Income_sources, Care_Profession_of_the_guardian, Care_Adopting_degree, Care_Civil_Registry, Care_Relation_of_the_guardian, Care_Number_of_children, Care_Guardian, Care_Workplace_the_guardian, Care_Health_status, Care_Workplace, Care_Housing_kind, Care_Interaction_degree, Care_Street, Care_Income_amount, Care_Care_sort, Care_Housing_description, Care_Family_members__The_number, Care_Monthly_income}

# Employee class attributes and methods
Employee_ID: Property = Property(name="ID", type=IntegerType)
Employee_First_name: Property = Property(name="First_name", type=StringType)
Employee_Last_name: Property = Property(name="Last_name", type=StringType)
Employee_Email_address: Property = Property(name="Email_address", type=StringType)
Employee_Mobile_number: Property = Property(name="Mobile_number", type=IntegerType)
Employee_Remaining_days: Property = Property(name="Remaining_days", type=IntegerType)
Employee_Functional_number: Property = Property(name="Functional_number", type=IntegerType)
Employee.attributes={Employee_Mobile_number, Employee_First_name, Employee_Remaining_days, Employee_Functional_number, Employee_Last_name, Employee_ID, Employee_Email_address}

# Vacation class attributes and methods
Vacation_Employee_ID: Property = Property(name="Employee_ID", type=IntegerType)
Vacation_Beginning_date: Property = Property(name="Beginning_date", type=StringType)
Vacation_Expiry_date: Property = Property(name="Expiry_date", type=StringType)
Vacation.attributes={Vacation_Beginning_date, Vacation_Expiry_date, Vacation_Employee_ID}

# Administrator__Actor class attributes and methods

# display_organization_information_UseCase class attributes and methods

# change_his_password_UseCase class attributes and methods

# change_the_organization_information__UseCase class attributes and methods

# add_new_data_entry_account_UseCase class attributes and methods

# delete_data_entry_account__UseCase class attributes and methods

# display_data_entry_UseCase class attributes and methods

# display_employee_information_UseCase class attributes and methods

# add_employee_UseCase class attributes and methods

# modify_employee_data_UseCase class attributes and methods

# delete_employee_UseCase class attributes and methods

# manage_holiday_UseCase class attributes and methods

# print_employee_information_UseCase class attributes and methods

# Log_out_UseCase class attributes and methods

# Log_in__UseCase class attributes and methods

# change_his_password__UseCase class attributes and methods

# display_beneficiaries_list_UseCase class attributes and methods

# display_volunteer_list_UseCase class attributes and methods

# modify_volunteer_data_UseCase class attributes and methods

# delete_volunteer_UseCase class attributes and methods

# print_volunteer_data_UseCase class attributes and methods

# display_honor_member_UseCase class attributes and methods

# print_honor_member_information__UseCase class attributes and methods

# modify_honor_member_information__UseCase class attributes and methods

# delete_honor_member_UseCase class attributes and methods

# _20Data_20entry_external class attributes and methods

# The_20member_external class attributes and methods

# Relationships
Administrator__display_data_entry: BinaryAssociation = BinaryAssociation(
    name="Administrator__display_data_entry",
    ends={
        Property(name="administrator11", type=Administrator__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="display_data_entry10", type=display_data_entry_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__display_employee_information: BinaryAssociation = BinaryAssociation(
    name="Administrator__display_employee_information",
    ends={
        Property(name="display_employee_information12", type=display_employee_information_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator13", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__modify_employee_data: BinaryAssociation = BinaryAssociation(
    name="Administrator__modify_employee_data",
    ends={
        Property(name="modify_employee_data14", type=modify_employee_data_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator15", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__delete_employee: BinaryAssociation = BinaryAssociation(
    name="Administrator__delete_employee",
    ends={
        Property(name="delete_employee16", type=delete_employee_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator17", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__change_his_password: BinaryAssociation = BinaryAssociation(
    name="Administrator__change_his_password",
    ends={
        Property(name="change_his_password0", type=change_his_password_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator1", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__display_organization_information: BinaryAssociation = BinaryAssociation(
    name="Administrator__display_organization_information",
    ends={
        Property(name="display_organization_information2", type=display_organization_information_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator3", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__change_the_organization_information: BinaryAssociation = BinaryAssociation(
    name="Administrator__change_the_organization_information",
    ends={
        Property(name="change_the_organization_information4", type=change_the_organization_information__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator5", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__add_new_data_entry_account: BinaryAssociation = BinaryAssociation(
    name="Administrator__add_new_data_entry_account",
    ends={
        Property(name="add_new_data_entry_account6", type=add_new_data_entry_account_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator7", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__delete_data_entry_account: BinaryAssociation = BinaryAssociation(
    name="Administrator__delete_data_entry_account",
    ends={
        Property(name="delete_data_entry_account8", type=delete_data_entry_account__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator9", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__manage_holiday: BinaryAssociation = BinaryAssociation(
    name="Administrator__manage_holiday",
    ends={
        Property(name="manage_holiday18", type=manage_holiday_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator19", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__print_employee_information: BinaryAssociation = BinaryAssociation(
    name="Administrator__print_employee_information",
    ends={
        Property(name="print_employee_information20", type=print_employee_information_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator21", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__Log_out: BinaryAssociation = BinaryAssociation(
    name="Administrator__Log_out",
    ends={
        Property(name="log_out22", type=Log_out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator23", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__Log_in: BinaryAssociation = BinaryAssociation(
    name="Administrator__Log_in",
    ends={
        Property(name="log_in24", type=Log_in__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator25", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Data_entry_employee__Log_in: BinaryAssociation = BinaryAssociation(
    name="Data_entry_employee__Log_in",
    ends={
        Property(name="log_in26", type=Log_in__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="data_entry_employee27", type=Data_entry_employee__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Data_entry_employee__Log_out: BinaryAssociation = BinaryAssociation(
    name="Data_entry_employee__Log_out",
    ends={
        Property(name="log_out28", type=Log_out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="data_entry_employee29", type=Data_entry_employee__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator__add_employee: BinaryAssociation = BinaryAssociation(
    name="Administrator__add_employee",
    ends={
        Property(name="add_employee30", type=add_employee_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator31", type=Administrator__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_The_origination: BinaryAssociation = BinaryAssociation(
    name="Admin_The_origination",
    ends={
        Property(name="Admin_The_origination_032", type=Origination, multiplicity=Multiplicity(1, 1)),
        Property(name="Admin_The_origination_133", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Data_entry__Beneficiary: BinaryAssociation = BinaryAssociation(
    name="Data_entry__Beneficiary",
    ends={
        Property(name="Beneficiary34", type=Beneficiary, multiplicity=Multiplicity(0, 1)),
        Property(name="Data_entry35", type=_20Data_20entry_external, multiplicity=Multiplicity(0, 1))
    }
)
The_amount_Care: BinaryAssociation = BinaryAssociation(
    name="The_amount_Care",
    ends={
        Property(name="care36", type=Care, multiplicity=Multiplicity(0, 1)),
        Property(name="the_amount37", type=Amount, multiplicity=Multiplicity(0, 1))
    }
)
Vacation_Employee: BinaryAssociation = BinaryAssociation(
    name="Vacation_Employee",
    ends={
        Property(name="employee38", type=Employee, multiplicity=Multiplicity(0, 1)),
        Property(name="vacation39", type=Vacation, multiplicity=Multiplicity(0, 1))
    }
)
The_member__Data_entry: BinaryAssociation = BinaryAssociation(
    name="The_member__Data_entry",
    ends={
        Property(name="Data_entry40", type=Data_entry, multiplicity=Multiplicity(0, 1)),
        Property(name="the_member41", type=The_20member_external, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Admin: BinaryAssociation = BinaryAssociation(
    name="Employee_Admin",
    ends={
        Property(name="admin42", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="employee43", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2D8DMN3KEeeAyLDAJ12_fg",
    types={account_statement__UseCase, add_new_beneficiary_UseCase, modify_beneficiary_information_UseCase, print_beneficiary_information_UseCase, delete_beneficiary__UseCase, print_beneficiaries_list_UseCase, Browse_based_care_type_UseCase, Browse_based_name_UseCase, Browse_based_Scientific_qualification_UseCase, Browse_based_Housing_kind_UseCase, Browse_based_age_UseCase, Browse_based_number_of_children_UseCase, add_new_volunteer_UseCase, add_honor_member_UseCase, display_all_UseCase, Data_entry_employee__Actor, Admin, Origination, Data_entry, Member, Honor_member, Volunteer, Beneficiary, Amount, Marriage_Demand, Care, Employee, Vacation, Administrator__Actor, display_organization_information_UseCase, change_his_password_UseCase, change_the_organization_information__UseCase, add_new_data_entry_account_UseCase, delete_data_entry_account__UseCase, display_data_entry_UseCase, display_employee_information_UseCase, add_employee_UseCase, modify_employee_data_UseCase, delete_employee_UseCase, manage_holiday_UseCase, print_employee_information_UseCase, Log_out_UseCase, Log_in__UseCase, change_his_password__UseCase, display_beneficiaries_list_UseCase, display_volunteer_list_UseCase, modify_volunteer_data_UseCase, delete_volunteer_UseCase, print_volunteer_data_UseCase, display_honor_member_UseCase, print_honor_member_information__UseCase, modify_honor_member_information__UseCase, delete_honor_member_UseCase, _20Data_20entry_external, The_20member_external},
    associations={Administrator__display_data_entry, Administrator__display_employee_information, Administrator__modify_employee_data, Administrator__delete_employee, Administrator__change_his_password, Administrator__display_organization_information, Administrator__change_the_organization_information, Administrator__add_new_data_entry_account, Administrator__delete_data_entry_account, Administrator__manage_holiday, Administrator__print_employee_information, Administrator__Log_out, Administrator__Log_in, Data_entry_employee__Log_in, Data_entry_employee__Log_out, Administrator__add_employee, Admin_The_origination, Data_entry__Beneficiary, The_amount_Care, Vacation_Employee, The_member__Data_entry, Employee_Admin},
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