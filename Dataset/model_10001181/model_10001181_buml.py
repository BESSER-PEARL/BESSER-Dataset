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
Manager = Class(name="Manager")
Salary = Class(name="Salary")
Staff = Class(name="Staff")
Leave_Status = Class(name="Leave_Status")
Attendance = Class(name="Attendance")
Login = Class(name="Login")
Employee_Management_System_Component = Class(name="Employee_Management_System_Component")
Authentication_UseCase = Class(name="Authentication_UseCase")
Salary_Management_UseCase = Class(name="Salary_Management_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Employee_Actor = Class(name="Employee_Actor")
Administrator = Class(name="Administrator")
Driving_Staff = Class(name="Driving_Staff")
Tuning_Staff = Class(name="Tuning_Staff")
Login_external = Class(name="Login_external")
Logout_external = Class(name="Logout_external")

# Manager class attributes and methods
Manager_Mng_Id: Property = Property(name="Mng_Id", type=IntegerType)
Manager_Mng_Name: Property = Property(name="Mng_Name", type=StringType)
Manager_Mng_ContactNo: Property = Property(name="Mng_ContactNo", type=StringType)
Manager_Mng_Email: Property = Property(name="Mng_Email", type=StringType)
Manager_Emp_NIC: Property = Property(name="Emp_NIC", type=StringType)
Manager_Emp_Address: Property = Property(name="Emp_Address", type=StringType)
Manager_Emp_DOB: Property = Property(name="Emp_DOB", type=DateType)
Manager_Emp_Department: Property = Property(name="Emp_Department", type=StringType)
Manager_Emp_Date_Of_Joint: Property = Property(name="Emp_Date_Of_Joint", type=DateType)
Manager_Emp_Position: Property = Property(name="Emp_Position", type=StringType)
Manager_Mng_Salary: Property = Property(name="Mng_Salary", type=FloatType)
Manager.attributes={Manager_Emp_DOB, Manager_Mng_ContactNo, Manager_Emp_Date_Of_Joint, Manager_Mng_Email, Manager_Mng_Salary, Manager_Mng_Name, Manager_Emp_Department, Manager_Emp_Position, Manager_Emp_Address, Manager_Mng_Id, Manager_Emp_NIC}

# Salary class attributes and methods
Salary_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Salary_Sly_Basic: Property = Property(name="Sly_Basic", type=FloatType)
Salary_Sly_Increment: Property = Property(name="Sly_Increment", type=FloatType)
Salary_Sly_Decrement: Property = Property(name="Sly_Decrement", type=FloatType)
Salary_Sly_Netgross: Property = Property(name="Sly_Netgross", type=FloatType)
Salary_OverTime: Property = Property(name="OverTime", type=StringType)
Salary.attributes={Salary_Sly_Basic, Salary_OverTime, Salary_Emp_Id, Salary_Sly_Increment, Salary_Sly_Decrement, Salary_Sly_Netgross}

# Staff class attributes and methods
Staff_UserName: Property = Property(name="UserName", type=StringType)
Staff_Password: Property = Property(name="Password", type=StringType)
Staff_Authendication_Mood: Property = Property(name="Authendication_Mood", type=StringType)
Staff.attributes={Staff_Authendication_Mood, Staff_UserName, Staff_Password}

# Leave_Status class attributes and methods
Leave_Status_leave_id: Property = Property(name="leave_id", type=IntegerType)
Leave_Status_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Leave_Status_Leave_Title: Property = Property(name="Leave_Title", type=StringType)
Leave_Status_Leave_detail: Property = Property(name="Leave_detail", type=StringType)
Leave_Status_Leave_ApplyDate: Property = Property(name="Leave_ApplyDate", type=DateType)
Leave_Status_Leave_StartDate: Property = Property(name="Leave_StartDate", type=DateType)
Leave_Status_Leave_EndDate: Property = Property(name="Leave_EndDate", type=DateType)
Leave_Status_Leave_NoOfDays: Property = Property(name="Leave_NoOfDays", type=IntegerType)
Leave_Status_Leave_Status: Property = Property(name="Leave_Status", type=StringType)
Leave_Status.attributes={Leave_Status_Leave_detail, Leave_Status_Emp_Id, Leave_Status_Leave_Status, Leave_Status_Leave_NoOfDays, Leave_Status_Leave_Title, Leave_Status_Leave_StartDate, Leave_Status_leave_id, Leave_Status_Leave_ApplyDate, Leave_Status_Leave_EndDate}

# Attendance class attributes and methods
Attendance_Emp_id: Property = Property(name="Emp_id", type=StringType)
Attendance_AttendTime: Property = Property(name="AttendTime", type=StringType)
Attendance_Leaving_Time: Property = Property(name="Leaving_Time", type=StringType)
Attendance_Attend_date: Property = Property(name="Attend_date", type=DateType)
Attendance.attributes={Attendance_AttendTime, Attendance_Attend_date, Attendance_Emp_id, Attendance_Leaving_Time}

# Login class attributes and methods
Login_UserName: Property = Property(name="UserName", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login.attributes={Login_UserName, Login_Password}

# Employee_Management_System_Component class attributes and methods

# Authentication_UseCase class attributes and methods

# Salary_Management_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Employee_Actor class attributes and methods

# Administrator class attributes and methods
Administrator_Admin_Id: Property = Property(name="Admin_Id", type=IntegerType)
Administrator_Admin_Name: Property = Property(name="Admin_Name", type=StringType)
Administrator_Admin_ContactNo: Property = Property(name="Admin_ContactNo", type=StringType)
Administrator_Admin_Email: Property = Property(name="Admin_Email", type=StringType)
Administrator_Admin_NIC: Property = Property(name="Admin_NIC", type=StringType)
Administrator_Emp_DOB: Property = Property(name="Emp_DOB", type=DateType)
Administrator_Emp_Department: Property = Property(name="Emp_Department", type=StringType)
Administrator_Emp_Date_Of_Joint: Property = Property(name="Emp_Date_Of_Joint", type=DateType)
Administrator_Emp_Position: Property = Property(name="Emp_Position", type=StringType)
Administrator.attributes={Administrator_Admin_ContactNo, Administrator_Emp_Date_Of_Joint, Administrator_Admin_Name, Administrator_Emp_DOB, Administrator_Emp_Position, Administrator_Admin_Id, Administrator_Emp_Department, Administrator_Admin_NIC, Administrator_Admin_Email}

# Driving_Staff class attributes and methods
Driving_Staff_PilotName: Property = Property(name="PilotName", type=StringType)
Driving_Staff_Password: Property = Property(name="Password", type=StringType)
Driving_Staff_Authendication_Mood: Property = Property(name="Authendication_Mood", type=StringType)
Driving_Staff_Pilot_ContactNo: Property = Property(name="Pilot_ContactNo", type=StringType)
Driving_Staff.attributes={Driving_Staff_Password, Driving_Staff_Authendication_Mood, Driving_Staff_PilotName, Driving_Staff_Pilot_ContactNo}

# Tuning_Staff class attributes and methods
Tuning_Staff_UserName: Property = Property(name="UserName", type=StringType)
Tuning_Staff_Address: Property = Property(name="Address", type=StringType)
Tuning_Staff_Authendication_Mood: Property = Property(name="Authendication_Mood", type=StringType)
Tuning_Staff.attributes={Tuning_Staff_UserName, Tuning_Staff_Authendication_Mood, Tuning_Staff_Address}

# Login_external class attributes and methods

# Logout_external class attributes and methods

# Relationships
Employee_Leave: BinaryAssociation = BinaryAssociation(
    name="Employee_Leave",
    ends={
        Property(name="leave0", type=Leave_Status, multiplicity=Multiplicity(0, 1)),
        Property(name="employee1", type=Manager, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Attendance: BinaryAssociation = BinaryAssociation(
    name="Employee_Attendance",
    ends={
        Property(name="attendance2", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="employee3", type=Manager, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Salary: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary",
    ends={
        Property(name="salary4", type=Salary, multiplicity=Multiplicity(0, 1)),
        Property(name="employee5", type=Manager, multiplicity=Multiplicity(0, 1))
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
Staff_Leave_Status: BinaryAssociation = BinaryAssociation(
    name="Staff_Leave_Status",
    ends={
        Property(name="leave_Status10", type=Leave_Status, multiplicity=Multiplicity(0, 1)),
        Property(name="staff11", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Manager: BinaryAssociation = BinaryAssociation(
    name="Administrator_Manager",
    ends={
        Property(name="manager12", type=Manager, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator13", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
Login_Administrator: BinaryAssociation = BinaryAssociation(
    name="Login_Administrator",
    ends={
        Property(name="administrator14", type=Administrator, multiplicity=Multiplicity(0, 1)),
        Property(name="login15", type=Login, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Login: BinaryAssociation = BinaryAssociation(
    name="Administrator_Login",
    ends={
        Property(name="login16", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator17", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
Login_Manager: BinaryAssociation = BinaryAssociation(
    name="Login_Manager",
    ends={
        Property(name="manager18", type=Manager, multiplicity=Multiplicity(0, 1)),
        Property(name="login19", type=Login, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Driving_Staff: BinaryAssociation = BinaryAssociation(
    name="Staff_Driving_Staff",
    ends={
        Property(name="driving_Staff20", type=Driving_Staff, multiplicity=Multiplicity(0, 1)),
        Property(name="staff21", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Tuning_Staff: BinaryAssociation = BinaryAssociation(
    name="Staff_Tuning_Staff",
    ends={
        Property(name="tuning_Staff22", type=Tuning_Staff, multiplicity=Multiplicity(0, 1)),
        Property(name="staff23", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8ec6a73d_4af0_4adb_a226_7ff6054bce24",
    types={Manager, Salary, Staff, Leave_Status, Attendance, Login, Employee_Management_System_Component, Authentication_UseCase, Salary_Management_UseCase, Administrator_Actor, Employee_Actor, Administrator, Driving_Staff, Tuning_Staff, Login_external, Logout_external},
    associations={Employee_Leave, Employee_Attendance, Employee_Salary, Employee_Login, Employee_Logout, Staff_Leave_Status, Administrator_Manager, Login_Administrator, Administrator_Login, Login_Manager, Staff_Driving_Staff, Staff_Tuning_Staff},
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