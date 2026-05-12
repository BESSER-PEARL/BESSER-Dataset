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
Usuario = Class(name="Usuario")
Student = Class(name="Student")
Profesor = Class(name="Profesor")
Database = Class(name="Database")
Admin = Class(name="Admin")
Curso = Class(name="Curso")
Login = Class(name="Login")
Interface_Interface = Class(name="Interface_Interface")

# Usuario class attributes and methods
Usuario_First_Name: Property = Property(name="First_Name", type=StringType)
Usuario_Last_Name: Property = Property(name="Last_Name", type=StringType)
Usuario_ID_Number: Property = Property(name="ID_Number", type=IntegerType)
Usuario_Password: Property = Property(name="Password", type=StringType)
Usuario.attributes={Usuario_Last_Name, Usuario_Password, Usuario_First_Name, Usuario_ID_Number}

# Student class attributes and methods
Student_Year: Property = Property(name="Year", type=StringType)
Student.attributes={Student_Year}

# Profesor class attributes and methods
Profesor_Assigned_Courses: Property = Property(name="Assigned_Courses", type=StringType)
Profesor.attributes={Profesor_Assigned_Courses}

# Database class attributes and methods
Database_Materials: Property = Property(name="Materials", type=Database)
Database_Schedules: Property = Property(name="Schedules", type=Database)
Database_Grades: Property = Property(name="Grades", type=Database)
Database_Accounts: Property = Property(name="Accounts", type=Database)
Database.attributes={Database_Materials, Database_Schedules, Database_Grades, Database_Accounts}

# Admin class attributes and methods

# Curso class attributes and methods
Curso_CourseName: Property = Property(name="CourseName", type=StringType)
Curso_CourseNumber: Property = Property(name="CourseNumber", type=StringType)
Curso_Course_Teacher: Property = Property(name="Course_Teacher", type=Profesor)
Curso.attributes={Curso_Course_Teacher, Curso_CourseName, Curso_CourseNumber}

# Login class attributes and methods

# Interface_Interface class attributes and methods

# Relationships
Course_Student: BinaryAssociation = BinaryAssociation(
    name="Course_Student",
    ends={
        Property(name="takes_course0", type=Student, multiplicity=Multiplicity(1, 9999)),
        Property(name="course1", type=Curso, multiplicity=Multiplicity(1, 9999))
    }
)
User_Database: BinaryAssociation = BinaryAssociation(
    name="User_Database",
    ends={
        Property(name="has_user2", type=Database, multiplicity=Multiplicity(0, 1)),
        Property(name="User_Database_13", type=Usuario, multiplicity=Multiplicity(1, 1))
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
Teacher_Course: BinaryAssociation = BinaryAssociation(
    name="Teacher_Course",
    ends={
        Property(name="teacher11", type=Profesor, multiplicity=Multiplicity(0, 1)),
        Property(name="Teaches10", type=Curso, multiplicity=Multiplicity(1, 9999))
    }
)
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login12", type=Login, multiplicity=Multiplicity(1, 1)),
        Property(name="user13", type=Usuario, multiplicity=Multiplicity(0, 9999))
    }
)
Teacher_Database: BinaryAssociation = BinaryAssociation(
    name="Teacher_Database",
    ends={
        Property(name="upload_to_database14", type=Database, multiplicity=Multiplicity(1, 1)),
        Property(name="teacher15", type=Profesor, multiplicity=Multiplicity(0, 9999))
    }
)
Student_Database: BinaryAssociation = BinaryAssociation(
    name="Student_Database",
    ends={
        Property(name="database8", type=Database, multiplicity=Multiplicity(0, 1)),
        Property(name="Student_Database_19", type=Student, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3b084a68_1319_4b0e_8628_297d48eb06e5",
    types={Usuario, Student, Profesor, Database, Admin, Curso, Login, Interface_Interface},
    associations={Course_Student, User_Database, Login_Database, Database_Admin, Teacher_Course, User_Login, Teacher_Database, Student_Database},
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