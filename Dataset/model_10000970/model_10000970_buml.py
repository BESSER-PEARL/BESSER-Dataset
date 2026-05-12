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
Login_external = Class(name="Login_external")
Logout_external = Class(name="Logout_external")
Employee = Class(name="Employee")
Salary = Class(name="Salary")
Authenticate_staff = Class(name="Authenticate_staff")
Leave = Class(name="Leave")
Attendance = Class(name="Attendance")
Login = Class(name="Login")
Employee_Management_System_Component = Class(name="Employee_Management_System_Component")
Authentication_UseCase = Class(name="Authentication_UseCase")
Salary_Management_UseCase = Class(name="Salary_Management_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Employee_Actor = Class(name="Employee_Actor")

# Login_external class attributes and methods

# Logout_external class attributes and methods

# Employee class attributes and methods
Employee_Emp_Name: Property = Property(name="Emp_Name", type=StringType)
Employee_Emp_ContactNo: Property = Property(name="Emp_ContactNo", type=StringType)
Employee_Emp_Email: Property = Property(name="Emp_Email", type=StringType)
Employee_Emp_NIC: Property = Property(name="Emp_NIC", type=StringType)
Employee_Emp_Address: Property = Property(name="Emp_Address", type=StringType)
Employee_Emp_DOB: Property = Property(name="Emp_DOB", type=DateType)
Employee_Emp_Department: Property = Property(name="Emp_Department", type=StringType)
Employee_Emp_Date_Of_Joint: Property = Property(name="Emp_Date_Of_Joint", type=DateType)
Employee_Emp_Position: Property = Property(name="Emp_Position", type=StringType)
Employee_Emp_Salary: Property = Property(name="Emp_Salary", type=FloatType)
Employee_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Employee.attributes={Employee_Emp_Department, Employee_Emp_DOB, Employee_Emp_Date_Of_Joint, Employee_Emp_Position, Employee_Emp_NIC, Employee_Emp_Id, Employee_Emp_Address, Employee_Emp_Salary, Employee_Emp_Email, Employee_Emp_Name, Employee_Emp_ContactNo}

# Salary class attributes and methods
Salary_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Salary_Sly_Basic: Property = Property(name="Sly_Basic", type=FloatType)
Salary_Sly_Increment: Property = Property(name="Sly_Increment", type=FloatType)
Salary_Sly_Decrement: Property = Property(name="Sly_Decrement", type=FloatType)
Salary_Sly_Netgross: Property = Property(name="Sly_Netgross", type=FloatType)
Salary_OverTime: Property = Property(name="OverTime", type=StringType)
Salary.attributes={Salary_Sly_Increment, Salary_Emp_Id, Salary_Sly_Decrement, Salary_OverTime, Salary_Sly_Netgross, Salary_Sly_Basic}

# Authenticate_staff class attributes and methods
Authenticate_staff_UserName: Property = Property(name="UserName", type=StringType)
Authenticate_staff_Password: Property = Property(name="Password", type=StringType)
Authenticate_staff_Authendication_Mood: Property = Property(name="Authendication_Mood", type=StringType)
Authenticate_staff.attributes={Authenticate_staff_UserName, Authenticate_staff_Password, Authenticate_staff_Authendication_Mood}

# Leave class attributes and methods
Leave_leave_id: Property = Property(name="leave_id", type=IntegerType)
Leave_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Leave_Leave_Title: Property = Property(name="Leave_Title", type=StringType)
Leave_Leave_detail: Property = Property(name="Leave_detail", type=StringType)
Leave_Leave_ApplyDate: Property = Property(name="Leave_ApplyDate", type=DateType)
Leave_Leave_StartDate: Property = Property(name="Leave_StartDate", type=DateType)
Leave_Leave_EndDate: Property = Property(name="Leave_EndDate", type=DateType)
Leave_Leave_NoOfDays: Property = Property(name="Leave_NoOfDays", type=IntegerType)
Leave_Leave_Status: Property = Property(name="Leave_Status", type=StringType)
Leave.attributes={Leave_Leave_EndDate, Leave_Leave_Status, Leave_Leave_Title, Leave_Leave_ApplyDate, Leave_Leave_StartDate, Leave_Leave_NoOfDays, Leave_leave_id, Leave_Leave_detail, Leave_Emp_Id}

# Attendance class attributes and methods
Attendance_Attend_date: Property = Property(name="Attend_date", type=DateType)
Attendance_Emp_id: Property = Property(name="Emp_id", type=StringType)
Attendance_AttendTime: Property = Property(name="AttendTime", type=StringType)
Attendance_Leaving_Time: Property = Property(name="Leaving_Time", type=StringType)
Attendance.attributes={Attendance_AttendTime, Attendance_Emp_id, Attendance_Leaving_Time, Attendance_Attend_date}

# Login class attributes and methods
Login_UserName: Property = Property(name="UserName", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login.attributes={Login_UserName, Login_Password}

# Employee_Management_System_Component class attributes and methods

# Authentication_UseCase class attributes and methods

# Salary_Management_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Employee_Actor class attributes and methods

# Relationships
Employee_Leave: BinaryAssociation = BinaryAssociation(
    name="Employee_Leave",
    ends={
        Property(name="leave0", type=Leave, multiplicity=Multiplicity(0, 1)),
        Property(name="employee1", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Attendance: BinaryAssociation = BinaryAssociation(
    name="Employee_Attendance",
    ends={
        Property(name="attendance2", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="employee3", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Salary: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary",
    ends={
        Property(name="salary4", type=Salary, multiplicity=Multiplicity(0, 1)),
        Property(name="employee5", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Login: BinaryAssociation = BinaryAssociation(
    name="Employee_Login",
    ends={
        Property(name="login6", type=Login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee7", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Logout: BinaryAssociation = BinaryAssociation(
    name="Employee_Logout",
    ends={
        Property(name="logout8", type=Logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee9", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_762760db_56a7_4d41_aa82_211765e5196b",
    types={Login_external, Logout_external, Employee, Salary, Authenticate_staff, Leave, Attendance, Login, Employee_Management_System_Component, Authentication_UseCase, Salary_Management_UseCase, Administrator_Actor, Employee_Actor},
    associations={Employee_Leave, Employee_Attendance, Employee_Salary, Employee_Login, Employee_Logout},
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