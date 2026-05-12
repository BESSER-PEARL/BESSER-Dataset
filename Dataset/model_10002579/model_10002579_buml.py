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
staff_member = Class(name="staff_member")
Salary = Class(name="Salary")
Authenticate_staff = Class(name="Authenticate_staff")
Mission = Class(name="Mission")
Attendance = Class(name="Attendance")
Login = Class(name="Login")
Employee_Management_System_Component = Class(name="Employee_Management_System_Component")
Authentication_UseCase = Class(name="Authentication_UseCase")
Salary_Management_UseCase = Class(name="Salary_Management_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Employee_Actor = Class(name="Employee_Actor")

# Login_external class attributes and methods

# Logout_external class attributes and methods

# staff_member class attributes and methods
staff_member_staff_Salary: Property = Property(name="staff_Salary", type=FloatType)
staff_member_staff_Id: Property = Property(name="staff_Id", type=IntegerType)
staff_member_staff_Name: Property = Property(name="staff_Name", type=StringType)
staff_member_staff_ContactNo: Property = Property(name="staff_ContactNo", type=StringType)
staff_member_staff_Email: Property = Property(name="staff_Email", type=StringType)
staff_member_staff_NIC: Property = Property(name="staff_NIC", type=StringType)
staff_member_staff_Address: Property = Property(name="staff_Address", type=StringType)
staff_member_staff_DOB: Property = Property(name="staff_DOB", type=DateType)
staff_member_staff_Department: Property = Property(name="staff_Department", type=StringType)
staff_member_staff_Date_Of_Joint: Property = Property(name="staff_Date_Of_Joint", type=DateType)
staff_member_staff_Position: Property = Property(name="staff_Position", type=StringType)
staff_member.attributes={staff_member_staff_Email, staff_member_staff_Id, staff_member_staff_Date_Of_Joint, staff_member_staff_Position, staff_member_staff_Address, staff_member_staff_ContactNo, staff_member_staff_Salary, staff_member_staff_Name, staff_member_staff_DOB, staff_member_staff_NIC, staff_member_staff_Department}

# Salary class attributes and methods
Salary_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Salary_Sly_Basic: Property = Property(name="Sly_Basic", type=FloatType)
Salary_Sly_Increment: Property = Property(name="Sly_Increment", type=FloatType)
Salary_Sly_Decrement: Property = Property(name="Sly_Decrement", type=FloatType)
Salary_Sly_Netgross: Property = Property(name="Sly_Netgross", type=FloatType)
Salary_OverTime: Property = Property(name="OverTime", type=StringType)
Salary.attributes={Salary_Sly_Increment, Salary_Sly_Decrement, Salary_Emp_Id, Salary_Sly_Basic, Salary_Sly_Netgross, Salary_OverTime}

# Authenticate_staff class attributes and methods
Authenticate_staff_Password: Property = Property(name="Password", type=StringType)
Authenticate_staff_Authendication_Mood: Property = Property(name="Authendication_Mood", type=StringType)
Authenticate_staff_UserName: Property = Property(name="UserName", type=StringType)
Authenticate_staff.attributes={Authenticate_staff_UserName, Authenticate_staff_Password, Authenticate_staff_Authendication_Mood}

# Mission class attributes and methods
Mission_mission_id: Property = Property(name="mission_id", type=IntegerType)
Mission_staff_Id: Property = Property(name="staff_Id", type=IntegerType)
Mission_mission_Title: Property = Property(name="mission_Title", type=StringType)
Mission_mission_detail: Property = Property(name="mission_detail", type=StringType)
Mission_mission_StartDate: Property = Property(name="mission_StartDate", type=DateType)
Mission_mission_EndDate: Property = Property(name="mission_EndDate", type=DateType)
Mission_mission_NoOfDays: Property = Property(name="mission_NoOfDays", type=IntegerType)
Mission_mission_Status: Property = Property(name="mission_Status", type=StringType)
Mission.attributes={Mission_mission_StartDate, Mission_mission_EndDate, Mission_mission_Status, Mission_mission_Title, Mission_mission_NoOfDays, Mission_mission_detail, Mission_staff_Id, Mission_mission_id}

# Attendance class attributes and methods
Attendance_Attend_date: Property = Property(name="Attend_date", type=DateType)
Attendance_Emp_id: Property = Property(name="Emp_id", type=StringType)
Attendance_AttendTime: Property = Property(name="AttendTime", type=StringType)
Attendance_Leaving_Time: Property = Property(name="Leaving_Time", type=StringType)
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

# Relationships
Employee_Leave: BinaryAssociation = BinaryAssociation(
    name="Employee_Leave",
    ends={
        Property(name="staff0", type=Mission, multiplicity=Multiplicity(0, 1)),
        Property(name="staff1", type=staff_member, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Attendance: BinaryAssociation = BinaryAssociation(
    name="Employee_Attendance",
    ends={
        Property(name="attendance2", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="staff3", type=staff_member, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Salary: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary",
    ends={
        Property(name="salary4", type=Salary, multiplicity=Multiplicity(0, 1)),
        Property(name="staff5", type=staff_member, multiplicity=Multiplicity(0, 1))
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
    name="c2e65a76_4cd8_47ff_93e7_e8acff6bf917",
    types={Login_external, Logout_external, staff_member, Salary, Authenticate_staff, Mission, Attendance, Login, Employee_Management_System_Component, Authentication_UseCase, Salary_Management_UseCase, Administrator_Actor, Employee_Actor},
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