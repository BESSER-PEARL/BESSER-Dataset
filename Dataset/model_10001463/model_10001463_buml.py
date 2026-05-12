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
Actor_Actor = Class(name="Actor_Actor")
_Component = Class(name="_Component")
Employee_Actor = Class(name="Employee_Actor")
Class_ = Class(name="Class")
Edit_profile_external = Class(name="Edit_profile_external")
Add_Employee_external = Class(name="Add_Employee_external")
login_external = Class(name="login_external")
logout_external = Class(name="logout_external")
View_list_of_all_employees_external = Class(name="View_list_of_all_employees_external")
Salary_reports_external = Class(name="Salary_reports_external")
Update_Employee_external = Class(name="Update_Employee_external")
manage_leave_requests_external = Class(name="manage_leave_requests_external")
change_password_external = Class(name="change_password_external")
Request_a_leave_external = Class(name="Request_a_leave_external")
update_leaves_external = Class(name="update_leaves_external")
Pay_Salary_external = Class(name="Pay_Salary_external")
update_salary_external = Class(name="update_salary_external")
delete_employee_external = Class(name="delete_employee_external")

# Actor_Actor class attributes and methods

# _Component class attributes and methods

# Employee_Actor class attributes and methods

# Class class attributes and methods

# Edit_profile_external class attributes and methods

# Add_Employee_external class attributes and methods

# login_external class attributes and methods

# logout_external class attributes and methods

# View_list_of_all_employees_external class attributes and methods

# Salary_reports_external class attributes and methods

# Update_Employee_external class attributes and methods

# manage_leave_requests_external class attributes and methods

# change_password_external class attributes and methods

# Request_a_leave_external class attributes and methods

# update_leaves_external class attributes and methods

# Pay_Salary_external class attributes and methods

# update_salary_external class attributes and methods

# delete_employee_external class attributes and methods

# Relationships
edit_profile_Actor: BinaryAssociation = BinaryAssociation(
    name="edit_profile_Actor",
    ends={
        Property(name="actor0", type=Actor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="edit_profile1", type=Edit_profile_external, multiplicity=Multiplicity(0, 1))
    }
)
Add_Employee_Actor: BinaryAssociation = BinaryAssociation(
    name="Add_Employee_Actor",
    ends={
        Property(name="actor2", type=Actor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="add_Employee3", type=Add_Employee_external, multiplicity=Multiplicity(0, 1))
    }
)
Actor_login: BinaryAssociation = BinaryAssociation(
    name="Actor_login",
    ends={
        Property(name="login4", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor5", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_logout: BinaryAssociation = BinaryAssociation(
    name="Actor_logout",
    ends={
        Property(name="logout6", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor7", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_View_list_of_all_employees: BinaryAssociation = BinaryAssociation(
    name="Actor_View_list_of_all_employees",
    ends={
        Property(name="view_list_of_all_employees8", type=View_list_of_all_employees_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor9", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor__Salary_reports: BinaryAssociation = BinaryAssociation(
    name="Actor__Salary_reports",
    ends={
        Property(name="Salary_reports10", type=Salary_reports_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor11", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Update_Employee: BinaryAssociation = BinaryAssociation(
    name="Actor_Update_Employee",
    ends={
        Property(name="update_Employee12", type=Update_Employee_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor13", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_manage_leave_requests: BinaryAssociation = BinaryAssociation(
    name="Actor_manage_leave_requests",
    ends={
        Property(name="manage_leave_requests14", type=manage_leave_requests_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor15", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_change_password: BinaryAssociation = BinaryAssociation(
    name="Actor_change_password",
    ends={
        Property(name="change_password16", type=change_password_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor17", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_edit_profile: BinaryAssociation = BinaryAssociation(
    name="Employee_edit_profile",
    ends={
        Property(name="edit_profile18", type=Edit_profile_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee19", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_login: BinaryAssociation = BinaryAssociation(
    name="Employee_login",
    ends={
        Property(name="login20", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee21", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_logout: BinaryAssociation = BinaryAssociation(
    name="Employee_logout",
    ends={
        Property(name="logout22", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee23", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee__Salary_reports: BinaryAssociation = BinaryAssociation(
    name="Employee__Salary_reports",
    ends={
        Property(name="Salary_reports24", type=Salary_reports_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee25", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_change_password: BinaryAssociation = BinaryAssociation(
    name="Employee_change_password",
    ends={
        Property(name="change_password26", type=change_password_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee27", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Request_a_leave: BinaryAssociation = BinaryAssociation(
    name="Employee_Request_a_leave",
    ends={
        Property(name="request_a_leave28", type=Request_a_leave_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee29", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_update_leaves: BinaryAssociation = BinaryAssociation(
    name="Actor_update_leaves",
    ends={
        Property(name="update_leaves30", type=update_leaves_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor31", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Pay_Salary: BinaryAssociation = BinaryAssociation(
    name="Actor_Pay_Salary",
    ends={
        Property(name="pay_Salary32", type=Pay_Salary_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor33", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_update_salary: BinaryAssociation = BinaryAssociation(
    name="Actor_update_salary",
    ends={
        Property(name="update_salary34", type=update_salary_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor35", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_delete_employee: BinaryAssociation = BinaryAssociation(
    name="Actor_delete_employee",
    ends={
        Property(name="delete_employee36", type=delete_employee_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor37", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8IgNAFc2EeqK2M3E1LfZ7Q",
    types={Actor_Actor, _Component, Employee_Actor, Class_, Edit_profile_external, Add_Employee_external, login_external, logout_external, View_list_of_all_employees_external, Salary_reports_external, Update_Employee_external, manage_leave_requests_external, change_password_external, Request_a_leave_external, update_leaves_external, Pay_Salary_external, update_salary_external, delete_employee_external},
    associations={edit_profile_Actor, Add_Employee_Actor, Actor_login, Actor_logout, Actor_View_list_of_all_employees, Actor__Salary_reports, Actor_Update_Employee, Actor_manage_leave_requests, Actor_change_password, Employee_edit_profile, Employee_login, Employee_logout, Employee__Salary_reports, Employee_change_password, Employee_Request_a_leave, Actor_update_leaves, Actor_Pay_Salary, Actor_update_salary, Actor_delete_employee},
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