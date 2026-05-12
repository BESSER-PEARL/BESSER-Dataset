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
Employee = Class(name="Employee")
Salary = Class(name="Salary")
Leave = Class(name="Leave")
Users = Class(name="Users")
Employee_Management_System_Component = Class(name="Employee_Management_System_Component")
Authentication_UseCase = Class(name="Authentication_UseCase")
Salary_Management_UseCase = Class(name="Salary_Management_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Employee_Actor = Class(name="Employee_Actor")
Admin = Class(name="Admin")
Users1 = Class(name="Users1")
Admin1 = Class(name="Admin1")
Employee1 = Class(name="Employee1")
Customer = Class(name="Customer")
Manager = Class(name="Manager")
Order = Class(name="Order")
Manager1 = Class(name="Manager1")
Customer1 = Class(name="Customer1")
Manager2 = Class(name="Manager2")
Login_external = Class(name="Login_external")
Logout_external = Class(name="Logout_external")

# Employee class attributes and methods
Employee_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Employee_Password: Property = Property(name="Password", type=StringType)
Employee_Emp_Name: Property = Property(name="Emp_Name", type=StringType)
Employee_Emp_ContactNo: Property = Property(name="Emp_ContactNo", type=StringType)
Employee_Emp_Email: Property = Property(name="Emp_Email", type=StringType)
Employee_Emp_Address: Property = Property(name="Emp_Address", type=StringType)
Employee_Emp_Department: Property = Property(name="Emp_Department", type=StringType)
Employee_Emp_Salary: Property = Property(name="Emp_Salary", type=FloatType)
Employee.attributes={Employee_Emp_Address, Employee_Emp_Email, Employee_Emp_Department, Employee_Emp_ContactNo, Employee_Emp_Salary, Employee_Password, Employee_Emp_Name, Employee_Emp_Id}

# Salary class attributes and methods
Salary_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Salary_Sly_Basic: Property = Property(name="Sly_Basic", type=FloatType)
Salary_Sly_Increment: Property = Property(name="Sly_Increment", type=FloatType)
Salary_Sly_Decrement: Property = Property(name="Sly_Decrement", type=FloatType)
Salary_Sly_Netgross: Property = Property(name="Sly_Netgross", type=FloatType)
Salary_OverTime: Property = Property(name="OverTime", type=StringType)
Salary.attributes={Salary_Sly_Increment, Salary_Sly_Netgross, Salary_Emp_Id, Salary_OverTime, Salary_Sly_Decrement, Salary_Sly_Basic}

# Leave class attributes and methods
Leave_leave_id: Property = Property(name="leave_id", type=IntegerType)
Leave_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Leave_Leave_Title: Property = Property(name="Leave_Title", type=StringType)
Leave_Leave_detail: Property = Property(name="Leave_detail", type=StringType)
Leave_Leave_EndDate: Property = Property(name="Leave_EndDate", type=DateType)
Leave_Leave_Status: Property = Property(name="Leave_Status", type=StringType)
Leave.attributes={Leave_Emp_Id, Leave_leave_id, Leave_Leave_EndDate, Leave_Leave_Status, Leave_Leave_Title, Leave_Leave_detail}

# Users class attributes and methods
Users_UserName: Property = Property(name="UserName", type=StringType)
Users_Password: Property = Property(name="Password", type=StringType)
Users.attributes={Users_Password, Users_UserName}

# Employee_Management_System_Component class attributes and methods

# Authentication_UseCase class attributes and methods

# Salary_Management_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Employee_Actor class attributes and methods

# Admin class attributes and methods
Admin_UserName: Property = Property(name="UserName", type=StringType)
Admin_Password: Property = Property(name="Password", type=StringType)
Admin.attributes={Admin_Password, Admin_UserName}

# Users1 class attributes and methods
Users1_id: Property = Property(name="id", type=StringType)
Users1_password: Property = Property(name="password", type=StringType)
Users1.attributes={Users1_password, Users1_id}

# Admin1 class attributes and methods
Admin1_UserName: Property = Property(name="UserName", type=StringType)
Admin1_password: Property = Property(name="password", type=StringType)
Admin1.attributes={Admin1_password, Admin1_UserName}

# Employee1 class attributes and methods
Employee1_UserName: Property = Property(name="UserName", type=StringType)
Employee1_password: Property = Property(name="password", type=StringType)
Employee1_name: Property = Property(name="name", type=StringType)
Employee1_contact_no: Property = Property(name="contact_no", type=IntegerType)
Employee1_Email: Property = Property(name="Email", type=StringType)
Employee1_attribute: Property = Property(name="attribute", type=StringType)
Employee1_Emp_Address: Property = Property(name="Emp_Address", type=StringType)
Employee1_Emp_Dep: Property = Property(name="Emp_Dep", type=StringType)
Employee1_Salary: Property = Property(name="Salary", type=IntegerType)
Employee1.attributes={Employee1_contact_no, Employee1_Emp_Address, Employee1_name, Employee1_password, Employee1_UserName, Employee1_attribute, Employee1_Salary, Employee1_Emp_Dep, Employee1_Email}

# Customer class attributes and methods
Customer_UserName: Property = Property(name="UserName", type=StringType)
Customer_password: Property = Property(name="password", type=StringType)
Customer.attributes={Customer_password, Customer_UserName}

# Manager class attributes and methods
Manager_UserName: Property = Property(name="UserName", type=StringType)
Manager_password: Property = Property(name="password", type=StringType)
Manager.attributes={Manager_UserName, Manager_password}

# Order class attributes and methods
Order_id: Property = Property(name="id", type=IntegerType)
Order_name: Property = Property(name="name", type=StringType)
Order.attributes={Order_id, Order_name}

# Manager1 class attributes and methods
Manager1_Manager_id: Property = Property(name="Manager_id", type=IntegerType)
Manager1_Password: Property = Property(name="Password", type=StringType)
Manager1_Name: Property = Property(name="Name", type=StringType)
Manager1.attributes={Manager1_Password, Manager1_Name, Manager1_Manager_id}

# Customer1 class attributes and methods
Customer1_Customer_Name: Property = Property(name="Customer_Name", type=StringType)
Customer1_S: Property = Property(name="S", type=StringType)
Customer1.attributes={Customer1_S, Customer1_Customer_Name}

# Manager2 class attributes and methods
Manager2_id: Property = Property(name="id", type=IntegerType)
Manager2_password: Property = Property(name="password", type=StringType)
Manager2_name: Property = Property(name="name", type=StringType)
Manager2.attributes={Manager2_name, Manager2_password, Manager2_id}

# Login_external class attributes and methods

# Logout_external class attributes and methods

# Relationships
Employee_Leave: BinaryAssociation = BinaryAssociation(
    name="Employee_Leave",
    ends={
        Property(name="leave0", type=Leave, multiplicity=Multiplicity(0, 1)),
        Property(name="employee1", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Salary: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary",
    ends={
        Property(name="salary2", type=Salary, multiplicity=Multiplicity(0, 1)),
        Property(name="employee3", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Login: BinaryAssociation = BinaryAssociation(
    name="Employee_Login",
    ends={
        Property(name="login4", type=Login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee5", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Logout: BinaryAssociation = BinaryAssociation(
    name="Employee_Logout",
    ends={
        Property(name="logout6", type=Logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee7", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order8", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer9", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Admin_Employee: BinaryAssociation = BinaryAssociation(
    name="Admin_Employee",
    ends={
        Property(name="employee10", type=Employee1, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin11", type=Admin1, multiplicity=Multiplicity(1, 1))
    }
)
Admin_Order: BinaryAssociation = BinaryAssociation(
    name="Admin_Order",
    ends={
        Property(name="order12", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="admin13", type=Admin1, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Manager: BinaryAssociation = BinaryAssociation(
    name="Employee_Manager",
    ends={
        Property(name="manager14", type=Manager2, multiplicity=Multiplicity(1, 1)),
        Property(name="employee15", type=Employee1, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3645ac35_2a16_4a7e_92d7_d5c4b59c6e90",
    types={Employee, Salary, Leave, Users, Employee_Management_System_Component, Authentication_UseCase, Salary_Management_UseCase, Administrator_Actor, Employee_Actor, Admin, Users1, Admin1, Employee1, Customer, Manager, Order, Manager1, Customer1, Manager2, Login_external, Logout_external},
    associations={Employee_Leave, Employee_Salary, Employee_Login, Employee_Logout, Customer_Order, Admin_Employee, Admin_Order, Employee_Manager},
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