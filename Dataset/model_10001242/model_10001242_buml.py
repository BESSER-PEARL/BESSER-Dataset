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
Leave = Class(name="Leave")
Attendance = Class(name="Attendance")
Login = Class(name="Login")
Employee_Management_System_Component = Class(name="Employee_Management_System_Component")
Authentication_UseCase = Class(name="Authentication_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Employee_Actor = Class(name="Employee_Actor")
FingerprintReader = Class(name="FingerprintReader")
Admin = Class(name="Admin")
Login_external = Class(name="Login_external")
Logout_external = Class(name="Logout_external")

# Employee class attributes and methods
Employee_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
Employee_Emp_Name: Property = Property(name="Emp_Name", type=StringType)
Employee_Emp_ContactNo: Property = Property(name="Emp_ContactNo", type=StringType)
Employee_Emp_Email: Property = Property(name="Emp_Email", type=StringType)
Employee_Emp_NIC: Property = Property(name="Emp_NIC", type=StringType)
Employee_Emp_Address: Property = Property(name="Emp_Address", type=StringType)
Employee_Emp_DOB: Property = Property(name="Emp_DOB", type=DateType)
Employee_Emp_Department: Property = Property(name="Emp_Department", type=StringType)
Employee_Emp_Date_Of_Joint: Property = Property(name="Emp_Date_Of_Joint", type=DateType)
Employee_Emp_Position: Property = Property(name="Emp_Position", type=StringType)
Employee.attributes={Employee_Emp_Address, Employee_Emp_Date_Of_Joint, Employee_Emp_Email, Employee_Emp_DOB, Employee_Emp_NIC, Employee_Emp_Name, Employee_Emp_Position, Employee_Emp_ContactNo, Employee_Emp_Department, Employee_Emp_Id}

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
Leave.attributes={Leave_Leave_EndDate, Leave_Leave_Status, Leave_Leave_StartDate, Leave_Leave_detail, Leave_Leave_ApplyDate, Leave_leave_id, Leave_Leave_NoOfDays, Leave_Emp_Id, Leave_Leave_Title}

# Attendance class attributes and methods
Attendance_Attend_date: Property = Property(name="Attend_date", type=DateType)
Attendance_Emp_id: Property = Property(name="Emp_id", type=StringType)
Attendance_AttendTime: Property = Property(name="AttendTime", type=StringType)
Attendance_Leaving_Time: Property = Property(name="Leaving_Time", type=StringType)
Attendance.attributes={Attendance_Leaving_Time, Attendance_Attend_date, Attendance_Emp_id, Attendance_AttendTime}

# Login class attributes and methods
Login_UserName: Property = Property(name="UserName", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login_Password1: Property = Property(name="Password1", type=StringType)
Login.attributes={Login_Password, Login_UserName, Login_Password1}

# Employee_Management_System_Component class attributes and methods

# Authentication_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Employee_Actor class attributes and methods

# FingerprintReader class attributes and methods
FingerprintReader_X_cord: Property = Property(name="X_cord", type=FloatType)
FingerprintReader_Y__Cord: Property = Property(name="Y__Cord", type=FloatType)
FingerprintReader_Angle: Property = Property(name="Angle", type=FloatType)
FingerprintReader_MiniType: Property = Property(name="MiniType", type=FingerprintReader)
FingerprintReader_miniType: Property = Property(name="miniType", type=IntegerType)
FingerprintReader_Emp_Id: Property = Property(name="Emp_Id", type=IntegerType)
FingerprintReader.attributes={FingerprintReader_Y__Cord, FingerprintReader_MiniType, FingerprintReader_X_cord, FingerprintReader_Emp_Id, FingerprintReader_miniType, FingerprintReader_Angle}

# Admin class attributes and methods
Admin_UserName: Property = Property(name="UserName", type=StringType)
Admin_Password: Property = Property(name="Password", type=StringType)
Admin_UserType: Property = Property(name="UserType", type=StringType)
Admin.attributes={Admin_Password, Admin_UserName, Admin_UserType}

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
Employee_Attendance: BinaryAssociation = BinaryAssociation(
    name="Employee_Attendance",
    ends={
        Property(name="attendance2", type=Attendance, multiplicity=Multiplicity(0, 1)),
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
FingerprintReader_Attendance: BinaryAssociation = BinaryAssociation(
    name="FingerprintReader_Attendance",
    ends={
        Property(name="attendance8", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="fingerprintReader9", type=FingerprintReader, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Admin: BinaryAssociation = BinaryAssociation(
    name="Employee_Admin",
    ends={
        Property(name="admin10", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="employee11", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_97f3f312_6bac_4bb4_876f_62ad63066c25",
    types={Employee, Leave, Attendance, Login, Employee_Management_System_Component, Authentication_UseCase, Administrator_Actor, Employee_Actor, FingerprintReader, Admin, Login_external, Logout_external},
    associations={Employee_Leave, Employee_Attendance, Employee_Login, Employee_Logout, FingerprintReader_Attendance, Employee_Admin},
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