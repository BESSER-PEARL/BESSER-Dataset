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
Student = Class(name="Student")
Teacher = Class(name="Teacher")
Database = Class(name="Database")
Admin = Class(name="Admin")
Course = Class(name="Course")
Login = Class(name="Login")

# User class attributes and methods
User_First_Name: Property = Property(name="First_Name", type=StringType)
User_Last_Name: Property = Property(name="Last_Name", type=StringType)
User_ID_Number: Property = Property(name="ID_Number", type=IntegerType)
User_Password: Property = Property(name="Password", type=StringType)
User.attributes={User_First_Name, User_ID_Number, User_Last_Name, User_Password}

# Student class attributes and methods
Student_Year: Property = Property(name="Year", type=StringType)
Student.attributes={Student_Year}

# Teacher class attributes and methods
Teacher_Assigned_Courses: Property = Property(name="Assigned_Courses", type=StringType)
Teacher.attributes={Teacher_Assigned_Courses}

# Database class attributes and methods
Database_Materials: Property = Property(name="Materials", type=Database)
Database_Schedules: Property = Property(name="Schedules", type=Database)
Database_Grades: Property = Property(name="Grades", type=Database)
Database_Accounts: Property = Property(name="Accounts", type=Database)
Database.attributes={Database_Schedules, Database_Accounts, Database_Grades, Database_Materials}

# Admin class attributes and methods

# Course class attributes and methods
Course_CourseName: Property = Property(name="CourseName", type=StringType)
Course_CourseNumber: Property = Property(name="CourseNumber", type=StringType)
Course_Course_Teacher: Property = Property(name="Course_Teacher", type=Teacher)
Course.attributes={Course_Course_Teacher, Course_CourseNumber, Course_CourseName}

# Login class attributes and methods

# Relationships
Course_Student: BinaryAssociation = BinaryAssociation(
    name="Course_Student",
    ends={
        Property(name="takes_course0", type=Student, multiplicity=Multiplicity(1, 9999)),
        Property(name="course1", type=Course, multiplicity=Multiplicity(1, 9999))
    }
)
User_Database: BinaryAssociation = BinaryAssociation(
    name="User_Database",
    ends={
        Property(name="has_user2", type=Database, multiplicity=Multiplicity(0, 1)),
        Property(name="User_Database_13", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Login_Database: BinaryAssociation = BinaryAssociation(
    name="Login_Database",
    ends={
        Property(name="verify_account4", type=Database, multiplicity=Multiplicity(0, 1)),
        Property(name="login5", type=Login, multiplicity=Multiplicity(0, 1))
    }
)
Database_Admin: BinaryAssociation = BinaryAssociation(
    name="Database_Admin",
    ends={
        Property(name="admin6", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="Database_Admin_17", type=Database, multiplicity=Multiplicity(0, 1))
    }
)
Student_Database: BinaryAssociation = BinaryAssociation(
    name="Student_Database",
    ends={
        Property(name="database8", type=Database, multiplicity=Multiplicity(0, 1)),
        Property(name="Student_Database_19", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_Course: BinaryAssociation = BinaryAssociation(
    name="Teacher_Course",
    ends={
        Property(name="Teaches10", type=Course, multiplicity=Multiplicity(1, 9999)),
        Property(name="teacher11", type=Teacher, multiplicity=Multiplicity(0, 1))
    }
)
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login12", type=Login, multiplicity=Multiplicity(1, 1)),
        Property(name="user13", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
Teacher_Database: BinaryAssociation = BinaryAssociation(
    name="Teacher_Database",
    ends={
        Property(name="upload_to_database14", type=Database, multiplicity=Multiplicity(1, 1)),
        Property(name="teacher15", type=Teacher, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ca0c32db_c7cf_4046_8e41_6e2d120a4973",
    types={User, Student, Teacher, Database, Admin, Course, Login},
    associations={Course_Student, User_Database, Login_Database, Database_Admin, Student_Database, Teacher_Course, User_Login, Teacher_Database},
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