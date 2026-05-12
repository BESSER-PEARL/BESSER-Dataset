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
Student_Actor = Class(name="Student_Actor")
Faculty__Actor = Class(name="Faculty__Actor")
Admin_Actor = Class(name="Admin_Actor")
SignUp_UseCase = Class(name="SignUp_UseCase")
Login_UseCase = Class(name="Login_UseCase")
Upload_Materials_UseCase = Class(name="Upload_Materials_UseCase")
View___Modify_the_Uploaded_Materials_UseCase = Class(name="View___Modify_the_Uploaded_Materials_UseCase")
Manage_Student___Faculty_List_UseCase = Class(name="Manage_Student___Faculty_List_UseCase")
View_The_Uploaded_Materials_UseCase = Class(name="View_The_Uploaded_Materials_UseCase")
Post_Questions_UseCase = Class(name="Post_Questions_UseCase")
View_Questions_And_Post_Answers_UseCase = Class(name="View_Questions_And_Post_Answers_UseCase")
Logout_UseCase = Class(name="Logout_UseCase")
Student = Class(name="Student")
Faculty = Class(name="Faculty")
Admin = Class(name="Admin")

# Student_Actor class attributes and methods

# Faculty__Actor class attributes and methods

# Admin_Actor class attributes and methods

# SignUp_UseCase class attributes and methods

# Login_UseCase class attributes and methods

# Upload_Materials_UseCase class attributes and methods

# View___Modify_the_Uploaded_Materials_UseCase class attributes and methods

# Manage_Student___Faculty_List_UseCase class attributes and methods

# View_The_Uploaded_Materials_UseCase class attributes and methods

# Post_Questions_UseCase class attributes and methods

# View_Questions_And_Post_Answers_UseCase class attributes and methods

# Logout_UseCase class attributes and methods

# Student class attributes and methods
Student_name: Property = Property(name="name", type=StringType)
Student_mail_ID: Property = Property(name="mail_ID", type=StringType)
Student_reg_Num: Property = Property(name="reg_Num", type=StringType)
Student.attributes={Student_name, Student_mail_ID, Student_reg_Num}

# Faculty class attributes and methods
Faculty_name: Property = Property(name="name", type=StringType)
Faculty_mail_ID: Property = Property(name="mail_ID", type=StringType)
Faculty_emp_ID: Property = Property(name="emp_ID", type=StringType)
Faculty.attributes={Faculty_name, Faculty_emp_ID, Faculty_mail_ID}

# Admin class attributes and methods
Admin_name: Property = Property(name="name", type=StringType)
Admin_mail_ID: Property = Property(name="mail_ID", type=StringType)
Admin.attributes={Admin_mail_ID, Admin_name}

# Relationships
Student_View_The_Uploaded_Materials: BinaryAssociation = BinaryAssociation(
    name="Student_View_The_Uploaded_Materials",
    ends={
        Property(name="view_The_Uploaded_Materials16", type=View_The_Uploaded_Materials_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student17", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Post_Questions: BinaryAssociation = BinaryAssociation(
    name="Student_Post_Questions",
    ends={
        Property(name="post_Questions18", type=Post_Questions_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student19", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_View_Questions_And_Post_Answers: BinaryAssociation = BinaryAssociation(
    name="Teacher_View_Questions_And_Post_Answers",
    ends={
        Property(name="view_Questions_And_Post_Answers20", type=View_Questions_And_Post_Answers_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="teacher21", type=Faculty__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Logout: BinaryAssociation = BinaryAssociation(
    name="Student_Logout",
    ends={
        Property(name="logout22", type=Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student23", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_Logout: BinaryAssociation = BinaryAssociation(
    name="Teacher_Logout",
    ends={
        Property(name="logout24", type=Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="teacher25", type=Faculty__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Logout: BinaryAssociation = BinaryAssociation(
    name="Admin_Logout",
    ends={
        Property(name="logout26", type=Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin27", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_SignUp: BinaryAssociation = BinaryAssociation(
    name="Student_SignUp",
    ends={
        Property(name="signUp0", type=SignUp_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student1", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Login: BinaryAssociation = BinaryAssociation(
    name="Student_Login",
    ends={
        Property(name="login2", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student3", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Manage_Student___Faculty_List: BinaryAssociation = BinaryAssociation(
    name="Admin_Manage_Student___Faculty_List",
    ends={
        Property(name="manage_Student___Faculty_List4", type=Manage_Student___Faculty_List_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin5", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_SignUp: BinaryAssociation = BinaryAssociation(
    name="Teacher_SignUp",
    ends={
        Property(name="signUp6", type=SignUp_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="teacher7", type=Faculty__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_Login: BinaryAssociation = BinaryAssociation(
    name="Teacher_Login",
    ends={
        Property(name="login8", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="teacher9", type=Faculty__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_Upload_Materials: BinaryAssociation = BinaryAssociation(
    name="Teacher_Upload_Materials",
    ends={
        Property(name="upload_Materials10", type=Upload_Materials_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="teacher11", type=Faculty__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_View___Modify_the_Uploaded_Materials: BinaryAssociation = BinaryAssociation(
    name="Admin_View___Modify_the_Uploaded_Materials",
    ends={
        Property(name="view___Modify_the_Uploaded_Materials12", type=View___Modify_the_Uploaded_Materials_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin13", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_View___Modify_the_Uploaded_Materials: BinaryAssociation = BinaryAssociation(
    name="Teacher_View___Modify_the_Uploaded_Materials",
    ends={
        Property(name="view___Modify_the_Uploaded_Materials14", type=View___Modify_the_Uploaded_Materials_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="teacher15", type=Faculty__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Faculty: BinaryAssociation = BinaryAssociation(
    name="Student_Faculty",
    ends={
        Property(name="faculty28", type=Faculty, multiplicity=Multiplicity(0, 9999)),
        Property(name="student29", type=Student, multiplicity=Multiplicity(0, 9999))
    }
)
Student_Admin: BinaryAssociation = BinaryAssociation(
    name="Student_Admin",
    ends={
        Property(name="admin30", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="student31", type=Student, multiplicity=Multiplicity(0, 9999))
    }
)
Faculty_Admin: BinaryAssociation = BinaryAssociation(
    name="Faculty_Admin",
    ends={
        Property(name="admin32", type=Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="faculty33", type=Faculty, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="dc1d984c_4866_4536_8d87_92419d3dd646",
    types={Student_Actor, Faculty__Actor, Admin_Actor, SignUp_UseCase, Login_UseCase, Upload_Materials_UseCase, View___Modify_the_Uploaded_Materials_UseCase, Manage_Student___Faculty_List_UseCase, View_The_Uploaded_Materials_UseCase, Post_Questions_UseCase, View_Questions_And_Post_Answers_UseCase, Logout_UseCase, Student, Faculty, Admin},
    associations={Student_View_The_Uploaded_Materials, Student_Post_Questions, Teacher_View_Questions_And_Post_Answers, Student_Logout, Teacher_Logout, Admin_Logout, Student_SignUp, Student_Login, Admin_Manage_Student___Faculty_List, Teacher_SignUp, Teacher_Login, Teacher_Upload_Materials, Admin_View___Modify_the_Uploaded_Materials, Teacher_View___Modify_the_Uploaded_Materials, Student_Faculty, Student_Admin, Faculty_Admin},
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