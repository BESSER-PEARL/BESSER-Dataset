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
Student = Class(name="Student")
Faculty = Class(name="Faculty")
Login = Class(name="Login")
Monitor = Class(name="Monitor")
Attendance = Class(name="Attendance")
Database = Class(name="Database")

# Student class attributes and methods
Student_Username: Property = Property(name="Username", type=StringType)
Student_ID: Property = Property(name="ID", type=StringType)
Student_Password: Property = Property(name="Password", type=StringType)
Student_First_Name: Property = Property(name="First_Name", type=StringType)
Student_Last_Name: Property = Property(name="Last_Name", type=StringType)
Student.attributes={Student_ID, Student_Last_Name, Student_Username, Student_Password, Student_First_Name}

# Faculty class attributes and methods
Faculty_ID: Property = Property(name="ID", type=StringType)
Faculty_Username: Property = Property(name="Username", type=StringType)
Faculty_Password: Property = Property(name="Password", type=StringType)
Faculty.attributes={Faculty_Username, Faculty_ID, Faculty_Password}

# Login class attributes and methods
Login_Username: Property = Property(name="Username", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login_login: Property = Property(name="login", type=Faculty)
Login.attributes={Login_Password, Login_Username, Login_login}

# Monitor class attributes and methods
Monitor_Date: Property = Property(name="Date", type=DateType)
Monitor_Location: Property = Property(name="Location", type=StringType)
Monitor_Time: Property = Property(name="Time", type=IntegerType)
Monitor.attributes={Monitor_Time, Monitor_Location, Monitor_Date}

# Attendance class attributes and methods
Attendance_ID: Property = Property(name="ID", type=StringType)
Attendance_Date: Property = Property(name="Date", type=StringType)
Attendance.attributes={Attendance_ID, Attendance_Date}

# Database class attributes and methods
Database_Category: Property = Property(name="Category", type=StringType)
Database_Attendance: Property = Property(name="Attendance", type=StringType)
Database.attributes={Database_Category, Database_Attendance}

# Relationships
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login0", type=Attendance, multiplicity=Multiplicity(1, 1)),
        Property(name="user1", type=Student, multiplicity=Multiplicity(1, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message2", type=Monitor, multiplicity=Multiplicity(0, 9999)),
        Property(name="user3", type=Student, multiplicity=Multiplicity(1, 1))
    }
)
Faculty_Login: BinaryAssociation = BinaryAssociation(
    name="Faculty_Login",
    ends={
        Property(name="Faculty_Login_04", type=Login, multiplicity=Multiplicity(1, 1)),
        Property(name="Faculty_Login_15", type=Faculty, multiplicity=Multiplicity(0, 1))
    }
)
Faculty_Attendance: BinaryAssociation = BinaryAssociation(
    name="Faculty_Attendance",
    ends={
        Property(name="Faculty_Attendance_06", type=Attendance, multiplicity=Multiplicity(1, 1)),
        Property(name="Faculty_Attendance_17", type=Faculty, multiplicity=Multiplicity(1, 1))
    }
)
Attendance_Database: BinaryAssociation = BinaryAssociation(
    name="Attendance_Database",
    ends={
        Property(name="Attendance_Database_08", type=Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Attendance_Database_19", type=Attendance, multiplicity=Multiplicity(1, 1))
    }
)
Student_Login: BinaryAssociation = BinaryAssociation(
    name="Student_Login",
    ends={
        Property(name="Student_Login_010", type=Login, multiplicity=Multiplicity(1, 1)),
        Property(name="Student_Login_111", type=Student, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_595cd0f7_97b4_495f_b3f0_d86908b20321",
    types={Student, Faculty, Login, Monitor, Attendance, Database},
    associations={User_Login, User_Message, Faculty_Login, Faculty_Attendance, Attendance_Database, Student_Login},
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