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
User = Class(name="User")
Salary = Class(name="Salary")
Admin = Class(name="Admin")
L__Leave = Class(name="L__Leave")
Attendance = Class(name="Attendance")
Login = Class(name="Login")
T = Class(name="T")
Employee_Management_System_Component = Class(name="Employee_Management_System_Component")
Authentication_UseCase = Class(name="Authentication_UseCase")
Salary_Management_UseCase = Class(name="Salary_Management_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Employee_Actor = Class(name="Employee_Actor")
Employee = Class(name="Employee")
_10000 = Class(name="_10000")
_10_7_1992 = Class(name="_10_7_1992")
Logout_external = Class(name="Logout_external")
Login_external = Class(name="Login_external")

# User class attributes and methods
User_User_Id: Property = Property(name="User_Id", type=StringType)
User_User_Name: Property = Property(name="User_Name", type=StringType)
User_User_contact: Property = Property(name="User_contact", type=StringType)
User_User_Email: Property = Property(name="User_Email", type=StringType)
User_User_Address: Property = Property(name="User_Address", type=StringType)
User_User_DOB: Property = Property(name="User_DOB", type=StringType)
User.attributes={User_User_Address, User_User_DOB, User_User_Name, User_User_Id, User_User_contact, User_User_Email}

# Salary class attributes and methods
Salary_Emp_Id: Property = Property(name="Emp_Id", type=StringType)
Salary_Sly_Basic: Property = Property(name="Sly_Basic", type=StringType)
Salary_Sly_Increment: Property = Property(name="Sly_Increment", type=_10000)
Salary_Sly_Decrement: Property = Property(name="Sly_Decrement", type=StringType)
Salary_Sly_Netgross: Property = Property(name="Sly_Netgross", type=StringType)
Salary_OverTime: Property = Property(name="OverTime", type=StringType)
Salary.attributes={Salary_Emp_Id, Salary_Sly_Netgross, Salary_Sly_Increment, Salary_Sly_Basic, Salary_Sly_Decrement, Salary_OverTime}

# Admin class attributes and methods
Admin_UserName: Property = Property(name="UserName", type=StringType)
Admin_Password: Property = Property(name="Password", type=StringType)
Admin_attribute: Property = Property(name="attribute", type=StringType)
Admin.attributes={Admin_attribute, Admin_UserName, Admin_Password}

# L__Leave class attributes and methods
L__Leave_leave_id: Property = Property(name="leave_id", type=StringType)
L__Leave_Emp_Id: Property = Property(name="Emp_Id", type=StringType)
L__Leave_Leave_Title: Property = Property(name="Leave_Title", type=StringType)
L__Leave_Leave_detail: Property = Property(name="Leave_detail", type=StringType)
L__Leave_Leave_ApplyDate: Property = Property(name="Leave_ApplyDate", type=StringType)
L__Leave_Leave_StartDate: Property = Property(name="Leave_StartDate", type=StringType)
L__Leave_Leave_EndDate: Property = Property(name="Leave_EndDate", type=StringType)
L__Leave_Leave_NoOfDays: Property = Property(name="Leave_NoOfDays", type=StringType)
L__Leave_Leave_Status: Property = Property(name="Leave_Status", type=StringType)
L__Leave.attributes={L__Leave_Leave_Title, L__Leave_Leave_StartDate, L__Leave_Leave_NoOfDays, L__Leave_Leave_EndDate, L__Leave_Leave_ApplyDate, L__Leave_Emp_Id, L__Leave_Leave_detail, L__Leave_leave_id, L__Leave_Leave_Status}

# Attendance class attributes and methods
Attendance_Attend_date: Property = Property(name="Attend_date", type=StringType)
Attendance_Emp_id: Property = Property(name="Emp_id", type=StringType)
Attendance_AttendTime: Property = Property(name="AttendTime", type=StringType)
Attendance_Leaving_Time: Property = Property(name="Leaving_Time", type=StringType)
Attendance.attributes={Attendance_Emp_id, Attendance_AttendTime, Attendance_Leaving_Time, Attendance_Attend_date}

# Login class attributes and methods
Login_UserName: Property = Property(name="UserName", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login.attributes={Login_Password, Login_UserName}

# T class attributes and methods

# Employee_Management_System_Component class attributes and methods

# Authentication_UseCase class attributes and methods

# Salary_Management_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Employee_Actor class attributes and methods

# Employee class attributes and methods
Employee_Emp_Id: Property = Property(name="Emp_Id", type=StringType)
Employee_Emp_Name: Property = Property(name="Emp_Name", type=StringType)
Employee_Emp_ContactNo: Property = Property(name="Emp_ContactNo", type=StringType)
Employee_Emp_Email: Property = Property(name="Emp_Email", type=StringType)
Employee_Emp_NIC: Property = Property(name="Emp_NIC", type=StringType)
Employee_Emp_Address: Property = Property(name="Emp_Address", type=StringType)
Employee_Emp_DOB: Property = Property(name="Emp_DOB", type=_10_7_1992)
Employee_Emp_Department: Property = Property(name="Emp_Department", type=StringType)
Employee_Emp_Date_Of_Joint: Property = Property(name="Emp_Date_Of_Joint", type=StringType)
Employee_Emp_Position: Property = Property(name="Emp_Position", type=StringType)
Employee_Emp_Salary: Property = Property(name="Emp_Salary", type=StringType)
Employee.attributes={Employee_Emp_Address, Employee_Emp_Name, Employee_Emp_Date_Of_Joint, Employee_Emp_Position, Employee_Emp_Department, Employee_Emp_DOB, Employee_Emp_Salary, Employee_Emp_ContactNo, Employee_Emp_NIC, Employee_Emp_Email, Employee_Emp_Id}

# _10000 class attributes and methods

# _10_7_1992 class attributes and methods

# Logout_external class attributes and methods

# Login_external class attributes and methods

# Relationships
Employee_Logout: BinaryAssociation = BinaryAssociation(
    name="Employee_Logout",
    ends={
        Property(name="logout8", type=Logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee9", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Leave: BinaryAssociation = BinaryAssociation(
    name="Employee_Leave",
    ends={
        Property(name="Employee_Leave_00", type=L__Leave, multiplicity=Multiplicity(0, 1)),
        Property(name="Employee_Leave_11", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Attendance: BinaryAssociation = BinaryAssociation(
    name="Employee_Attendance",
    ends={
        Property(name="Employee_Attendance_02", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="Employee_Attendance_13", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Salary: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary",
    ends={
        Property(name="Employee_Salary_04", type=Salary, multiplicity=Multiplicity(0, 1)),
        Property(name="Employee_Salary_15", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Login: BinaryAssociation = BinaryAssociation(
    name="Employee_Login",
    ends={
        Property(name="login6", type=Login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee7", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_jjFEYM2XEem3EtTcbeVZ5Q",
    types={User, Salary, Admin, L__Leave, Attendance, Login, T, Employee_Management_System_Component, Authentication_UseCase, Salary_Management_UseCase, Administrator_Actor, Employee_Actor, Employee, _10000, _10_7_1992, Logout_external, Login_external},
    associations={Employee_Logout, Employee_Leave, Employee_Attendance, Employee_Salary, Employee_Login},
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