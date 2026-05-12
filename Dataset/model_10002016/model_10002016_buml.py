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
Registration = Class(name="Registration")
Position = Class(name="Position")
Login = Class(name="Login")
Attendance = Class(name="Attendance")
Requirement = Class(name="Requirement")
Task = Class(name="Task")
New_Employee = Class(name="New_Employee")
Survey = Class(name="Survey")
Performance = Class(name="Performance")
Assessment = Class(name="Assessment")
Assessment__Self_Assessment = Class(name="Assessment__Self_Assessment")
Applicant = Class(name="Applicant")

# Admin class attributes and methods
Admin_name: Property = Property(name="name", type=StringType)
Admin_qualification: Property = Property(name="qualification", type=StringType)
Admin_address: Property = Property(name="address", type=StringType)
Admin.attributes={Admin_address, Admin_qualification, Admin_name}

# Registration class attributes and methods
Registration_Date: Property = Property(name="Date", type=StringType)
Registration_Name: Property = Property(name="Name", type=StringType)
Registration_Address: Property = Property(name="Address", type=StringType)
Registration_Phone: Property = Property(name="Phone", type=StringType)
Registration_Email: Property = Property(name="Email", type=StringType)
Registration_Applied_Position: Property = Property(name="Applied_Position", type=StringType)
Registration_Position_Type: Property = Property(name="Position_Type", type=StringType)
Registration_Skills___Requirement: Property = Property(name="Skills___Requirement", type=StringType)
Registration.attributes={Registration_Phone, Registration_Skills___Requirement, Registration_Address, Registration_Name, Registration_Date, Registration_Applied_Position, Registration_Position_Type, Registration_Email}

# Position class attributes and methods
Position_positionID: Property = Property(name="positionID", type=IntegerType)
Position_positionName: Property = Property(name="positionName", type=StringType)
Position_divisionName: Property = Property(name="divisionName", type=StringType)
Position_jobID: Property = Property(name="jobID", type=StringType)
Position.attributes={Position_positionName, Position_divisionName, Position_positionID, Position_jobID}

# Login class attributes and methods
Login_userid: Property = Property(name="userid", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_password, Login_userid}

# Attendance class attributes and methods
Attendance_Name: Property = Property(name="Name", type=StringType)
Attendance_Date___Time: Property = Property(name="Date___Time", type=StringType)
Attendance_Position: Property = Property(name="Position", type=StringType)
Attendance_Details: Property = Property(name="Details", type=StringType)
Attendance.attributes={Attendance_Position, Attendance_Details, Attendance_Date___Time, Attendance_Name}

# Requirement class attributes and methods
Requirement_ID_Card: Property = Property(name="ID_Card", type=StringType)
Requirement_Curriculum_Vitae: Property = Property(name="Curriculum_Vitae", type=StringType)
Requirement_Diploma: Property = Property(name="Diploma", type=StringType)
Requirement_Transcript: Property = Property(name="Transcript", type=StringType)
Requirement_Photo: Property = Property(name="Photo", type=StringType)
Requirement.attributes={Requirement_Curriculum_Vitae, Requirement_ID_Card, Requirement_Transcript, Requirement_Photo, Requirement_Diploma}

# Task class attributes and methods
Task_Task_Name: Property = Property(name="Task_Name", type=StringType)
Task_Task_Detail: Property = Property(name="Task_Detail", type=StringType)
Task_Name: Property = Property(name="Name", type=StringType)
Task_Deadline: Property = Property(name="Deadline", type=StringType)
Task.attributes={Task_Task_Name, Task_Deadline, Task_Name, Task_Task_Detail}

# New_Employee class attributes and methods
New_Employee_Name: Property = Property(name="Name", type=StringType)
New_Employee_Position: Property = Property(name="Position", type=StringType)
New_Employee_Division: Property = Property(name="Division", type=StringType)
New_Employee_Date_of_Birth: Property = Property(name="Date_of_Birth", type=StringType)
New_Employee_Place_of_Birth: Property = Property(name="Place_of_Birth", type=StringType)
New_Employee_Working_Since: Property = Property(name="Working_Since", type=StringType)
New_Employee.attributes={New_Employee_Place_of_Birth, New_Employee_Working_Since, New_Employee_Date_of_Birth, New_Employee_Division, New_Employee_Position, New_Employee_Name}

# Survey class attributes and methods
Survey_Name: Property = Property(name="Name", type=StringType)
Survey_Question: Property = Property(name="Question", type=StringType)
Survey_Score: Property = Property(name="Score", type=StringType)
Survey.attributes={Survey_Score, Survey_Question, Survey_Name}

# Performance class attributes and methods
Performance_Name: Property = Property(name="Name", type=StringType)
Performance_Punctuality: Property = Property(name="Punctuality", type=StringType)
Performance_Target: Property = Property(name="Target", type=StringType)
Performance_Coordination: Property = Property(name="Coordination", type=StringType)
Performance.attributes={Performance_Coordination, Performance_Name, Performance_Punctuality, Performance_Target}

# Assessment class attributes and methods
Assessment_Name: Property = Property(name="Name", type=StringType)
Assessment_Type_of_Assessment: Property = Property(name="Type_of_Assessment", type=StringType)
Assessment_Total_Score: Property = Property(name="Total_Score", type=StringType)
Assessment.attributes={Assessment_Name, Assessment_Total_Score, Assessment_Type_of_Assessment}

# Assessment__Self_Assessment class attributes and methods
Assessment__Self_Assessment_Name: Property = Property(name="Name", type=StringType)
Assessment__Self_Assessment_Question: Property = Property(name="Question", type=StringType)
Assessment__Self_Assessment_Score: Property = Property(name="Score", type=StringType)
Assessment__Self_Assessment.attributes={Assessment__Self_Assessment_Name, Assessment__Self_Assessment_Score, Assessment__Self_Assessment_Question}

# Applicant class attributes and methods
Applicant_First_Name: Property = Property(name="First_Name", type=StringType)
Applicant_Last_Name: Property = Property(name="Last_Name", type=StringType)
Applicant_Applied_Position: Property = Property(name="Applied_Position", type=StringType)
Applicant_Email: Property = Property(name="Email", type=StringType)
Applicant_Password: Property = Property(name="Password", type=StringType)
Applicant_Date_of_Birth: Property = Property(name="Date_of_Birth", type=StringType)
Applicant_Phone: Property = Property(name="Phone", type=StringType)
Applicant_Address: Property = Property(name="Address", type=StringType)
Applicant.attributes={Applicant_Date_of_Birth, Applicant_Applied_Position, Applicant_Password, Applicant_Address, Applicant_Email, Applicant_First_Name, Applicant_Phone, Applicant_Last_Name}

# Relationships
Admin_Login: BinaryAssociation = BinaryAssociation(
    name="Admin_Login",
    ends={
        Property(name="login0", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="admin1", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Applicant_Login: BinaryAssociation = BinaryAssociation(
    name="Applicant_Login",
    ends={
        Property(name="login2", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="applicant3", type=Applicant, multiplicity=Multiplicity(0, 1))
    }
)
Applicant_Registration: BinaryAssociation = BinaryAssociation(
    name="Applicant_Registration",
    ends={
        Property(name="registration4", type=Registration, multiplicity=Multiplicity(0, 1)),
        Property(name="applicant5", type=Applicant, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Registration: BinaryAssociation = BinaryAssociation(
    name="Admin_Registration",
    ends={
        Property(name="registration6", type=Registration, multiplicity=Multiplicity(0, 1)),
        Property(name="admin7", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Applicant_Position: BinaryAssociation = BinaryAssociation(
    name="Applicant_Position",
    ends={
        Property(name="position8", type=Position, multiplicity=Multiplicity(0, 1)),
        Property(name="applicant9", type=Applicant, multiplicity=Multiplicity(0, 1))
    }
)
Registration_New_Employee: BinaryAssociation = BinaryAssociation(
    name="Registration_New_Employee",
    ends={
        Property(name="new_Employee10", type=New_Employee, multiplicity=Multiplicity(0, 1)),
        Property(name="registration11", type=Registration, multiplicity=Multiplicity(0, 1))
    }
)
Applicant_New_Employee: BinaryAssociation = BinaryAssociation(
    name="Applicant_New_Employee",
    ends={
        Property(name="new_Employee12", type=New_Employee, multiplicity=Multiplicity(0, 1)),
        Property(name="applicant13", type=Applicant, multiplicity=Multiplicity(0, 1))
    }
)
Task_New_Employee: BinaryAssociation = BinaryAssociation(
    name="Task_New_Employee",
    ends={
        Property(name="new_Employee14", type=New_Employee, multiplicity=Multiplicity(0, 1)),
        Property(name="task15", type=Task, multiplicity=Multiplicity(0, 1))
    }
)
New_Employee_Attendance: BinaryAssociation = BinaryAssociation(
    name="New_Employee_Attendance",
    ends={
        Property(name="attendance16", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="new_Employee17", type=New_Employee, multiplicity=Multiplicity(0, 1))
    }
)
Requirement_Registration: BinaryAssociation = BinaryAssociation(
    name="Requirement_Registration",
    ends={
        Property(name="registration18", type=Registration, multiplicity=Multiplicity(0, 1)),
        Property(name="requirement19", type=Requirement, multiplicity=Multiplicity(0, 1))
    }
)
Attendance_Assessment: BinaryAssociation = BinaryAssociation(
    name="Attendance_Assessment",
    ends={
        Property(name="assessment20", type=Assessment, multiplicity=Multiplicity(0, 1)),
        Property(name="attendance21", type=Attendance, multiplicity=Multiplicity(0, 1))
    }
)
Assessment__Self_Assessment_Assessment: BinaryAssociation = BinaryAssociation(
    name="Assessment__Self_Assessment_Assessment",
    ends={
        Property(name="assessment22", type=Assessment, multiplicity=Multiplicity(0, 1)),
        Property(name="assessment__Self_Assessment23", type=Assessment__Self_Assessment, multiplicity=Multiplicity(0, 1))
    }
)
Survey_Assessment: BinaryAssociation = BinaryAssociation(
    name="Survey_Assessment",
    ends={
        Property(name="assessment24", type=Assessment, multiplicity=Multiplicity(0, 1)),
        Property(name="survey25", type=Survey, multiplicity=Multiplicity(0, 1))
    }
)
Performance_Assessment: BinaryAssociation = BinaryAssociation(
    name="Performance_Assessment",
    ends={
        Property(name="assessment26", type=Assessment, multiplicity=Multiplicity(0, 1)),
        Property(name="performance27", type=Performance, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_jjUpANd6EeeQi8PFukjNiw",
    types={Admin, Registration, Position, Login, Attendance, Requirement, Task, New_Employee, Survey, Performance, Assessment, Assessment__Self_Assessment, Applicant},
    associations={Admin_Login, Applicant_Login, Applicant_Registration, Admin_Registration, Applicant_Position, Registration_New_Employee, Applicant_New_Employee, Task_New_Employee, New_Employee_Attendance, Requirement_Registration, Attendance_Assessment, Assessment__Self_Assessment_Assessment, Survey_Assessment, Performance_Assessment},
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