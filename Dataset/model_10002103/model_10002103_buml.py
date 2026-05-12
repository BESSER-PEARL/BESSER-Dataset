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
Admin = Class(name="Admin")
Employee = Class(name="Employee")
Leave = Class(name="Leave")
Haff_day = Class(name="Haff_day")
Full_day = Class(name="Full_day")
Attendance = Class(name="Attendance")
login = Class(name="login")
location = Class(name="location")

# Admin class attributes and methods
Admin_username: Property = Property(name="username", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin.attributes={Admin_username, Admin_password}

# Employee class attributes and methods
Employee_e_id: Property = Property(name="e_id", type=IntegerType)
Employee_name: Property = Property(name="name", type=StringType)
Employee_phone_no: Property = Property(name="phone_no", type=IntegerType)
Employee_email_id: Property = Property(name="email_id", type=StringType)
Employee_paasword: Property = Property(name="paasword", type=StringType)
Employee_address: Property = Property(name="address", type=StringType)
Employee_office_address: Property = Property(name="office_address", type=StringType)
Employee.attributes={Employee_email_id, Employee_phone_no, Employee_address, Employee_office_address, Employee_name, Employee_e_id, Employee_paasword}

# Leave class attributes and methods
Leave_l_id: Property = Property(name="l_id", type=IntegerType)
Leave_l_description: Property = Property(name="l_description", type=StringType)
Leave_l_type: Property = Property(name="l_type", type=StringType)
Leave_l_emp_id: Property = Property(name="l_emp_id", type=IntegerType)
Leave.attributes={Leave_l_description, Leave_l_emp_id, Leave_l_id, Leave_l_type}

# Haff_day class attributes and methods
Haff_day_start_date: Property = Property(name="start_date", type=IntegerType)
Haff_day.attributes={Haff_day_start_date}

# Full_day class attributes and methods
Full_day_start_date: Property = Property(name="start_date", type=IntegerType)
Full_day_end_date: Property = Property(name="end_date", type=IntegerType)
Full_day.attributes={Full_day_end_date, Full_day_start_date}

# Attendance class attributes and methods
Attendance_atten_id: Property = Property(name="atten_id", type=IntegerType)
Attendance_atten_emp_id: Property = Property(name="atten_emp_id", type=IntegerType)
Attendance_atten_type: Property = Property(name="atten_type", type=StringType)
Attendance_atten_time: Property = Property(name="atten_time", type=IntegerType)
Attendance_atten_date: Property = Property(name="atten_date", type=StringType)
Attendance.attributes={Attendance_atten_type, Attendance_atten_id, Attendance_atten_time, Attendance_atten_emp_id, Attendance_atten_date}

# login class attributes and methods
login_login_id: Property = Property(name="login_id", type=IntegerType)
login_loginUsername: Property = Property(name="loginUsername", type=StringType)
login_loginpassword: Property = Property(name="loginpassword", type=StringType)
login_loginStatus: Property = Property(name="loginStatus", type=StringType)
login.attributes={login_loginUsername, login_login_id, login_loginStatus, login_loginpassword}

# location class attributes and methods
location_Latitude: Property = Property(name="Latitude", type=IntegerType)
location_Longitude: Property = Property(name="Longitude", type=IntegerType)
location.attributes={location_Longitude, location_Latitude}

# Relationships
Employee_____Admin: BinaryAssociation = BinaryAssociation(
    name="Employee_____Admin",
    ends={
        Property(name="Admin0", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="employee1", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Leave: BinaryAssociation = BinaryAssociation(
    name="Admin_Leave",
    ends={
        Property(name="leave2", type=Leave, multiplicity=Multiplicity(0, 1)),
        Property(name="Admin3", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Employee_login: BinaryAssociation = BinaryAssociation(
    name="Employee_login",
    ends={
        Property(name="login218", type=login, multiplicity=Multiplicity(0, 1)),
        Property(name="employee19", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Admin_login: BinaryAssociation = BinaryAssociation(
    name="Admin_login",
    ends={
        Property(name="login20", type=login, multiplicity=Multiplicity(0, 1)),
        Property(name="Admin21", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Attendance: BinaryAssociation = BinaryAssociation(
    name="Employee_Attendance",
    ends={
        Property(name="attendance4", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="employee5", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Attendance_location: BinaryAssociation = BinaryAssociation(
    name="Attendance_location",
    ends={
        Property(name="location6", type=location, multiplicity=Multiplicity(0, 1)),
        Property(name="attendance7", type=Attendance, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Employee: BinaryAssociation = BinaryAssociation(
    name="Admin_Employee",
    ends={
        Property(name="employee8", type=Employee, multiplicity=Multiplicity(1, 9999)),
        Property(name="Admin9", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Leave_Employee: BinaryAssociation = BinaryAssociation(
    name="Leave_Employee",
    ends={
        Property(name="employee10", type=Employee, multiplicity=Multiplicity(1, 9999)),
        Property(name="leave11", type=Leave, multiplicity=Multiplicity(1, 9999))
    }
)
Admin_Attendance: BinaryAssociation = BinaryAssociation(
    name="Admin_Attendance",
    ends={
        Property(name="attendance12", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="Admin13", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Attendance1: BinaryAssociation = BinaryAssociation(
    name="Employee_Attendance1",
    ends={
        Property(name="attendance14", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="employee15", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
location_Attendance: BinaryAssociation = BinaryAssociation(
    name="location_Attendance",
    ends={
        Property(name="attendance16", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="location17", type=location, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_oUcb8Nf5EeeQi8PFukjNiw",
    types={Admin, Employee, Leave, Haff_day, Full_day, Attendance, login, location},
    associations={Employee_____Admin, Admin_Leave, Employee_login, Admin_login, Employee_Attendance, Attendance_location, Admin_Employee, Leave_Employee, Admin_Attendance, Employee_Attendance1, location_Attendance},
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