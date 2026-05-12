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

# Enumerations
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

Status: Enumeration = Enumeration(
    name="Status",
    literals={
            
    }
)

Enumeration1: Enumeration = Enumeration(
    name="Enumeration1",
    literals={
            
    }
)

# Classes
Student_Actor = Class(name="Student_Actor")
TEACHER_Actor = Class(name="TEACHER_Actor")
CORPORATE_CLIENT_Actor = Class(name="CORPORATE_CLIENT_Actor")
Traning_Admin_Actor = Class(name="Traning_Admin_Actor")
Student_ID_UseCase = Class(name="Student_ID_UseCase")
Name_UseCase = Class(name="Name_UseCase")
Address_UseCase = Class(name="Address_UseCase")
Create_Course_UseCase = Class(name="Create_Course_UseCase")
Courses_Component = Class(name="Courses_Component")
Add_Course_UseCase = Class(name="Add_Course_UseCase")
Drop_Course_UseCase = Class(name="Drop_Course_UseCase")
CompleteCourse_UseCase = Class(name="CompleteCourse_UseCase")
Remove_Course_UseCase = Class(name="Remove_Course_UseCase")
Modify_Course_UseCase = Class(name="Modify_Course_UseCase")
Show_Course_UseCase = Class(name="Show_Course_UseCase")
LearningMaterial_UseCase = Class(name="LearningMaterial_UseCase")
Reports_UseCase = Class(name="Reports_UseCase")
Show_Grade_UseCase = Class(name="Show_Grade_UseCase")
Login_UseCase = Class(name="Login_UseCase")
Teacher_Actor = Class(name="Teacher_Actor")
Class_Course_List_UseCase = Class(name="Class_Course_List_UseCase")
Select_Course_List_UseCase = Class(name="Select_Course_List_UseCase")
Grade_Course_UseCase = Class(name="Grade_Course_UseCase")
User_Info_UseCase = Class(name="User_Info_UseCase")
Update_Registar_UseCase = Class(name="Update_Registar_UseCase")
UseCase_UseCase = Class(name="UseCase_UseCase")
Corporate_Client_Actor = Class(name="Corporate_Client_Actor")
Corporate_UseCase = Class(name="Corporate_UseCase")
class_Student_Registration = Class(name="class_Student_Registration")
class_Student_Registration_Student = Class(name="class_Student_Registration_Student")
class_Student_Registration_Teacher = Class(name="class_Student_Registration_Teacher")
class_Student_Registration_Corporate = Class(name="class_Student_Registration_Corporate")
class_Student_Registration_Admin = Class(name="class_Student_Registration_Admin")
_UseCase = Class(name="_UseCase")
Student = Class(name="Student")
Course = Class(name="Course")
corprateClient = Class(name="corprateClient")
Teacher = Class(name="Teacher")
Registrar = Class(name="Registrar")
ADMIN = Class(name="ADMIN")
registeredUser = Class(name="registeredUser")
Admin = Class(name="Admin")
courseList = Class(name="courseList")
Class_ = Class(name="Class")

# Student_Actor class attributes and methods

# TEACHER_Actor class attributes and methods

# CORPORATE_CLIENT_Actor class attributes and methods

# Traning_Admin_Actor class attributes and methods

# Student_ID_UseCase class attributes and methods

# Name_UseCase class attributes and methods

# Address_UseCase class attributes and methods

# Create_Course_UseCase class attributes and methods

# Courses_Component class attributes and methods

# Add_Course_UseCase class attributes and methods

# Drop_Course_UseCase class attributes and methods

# CompleteCourse_UseCase class attributes and methods

# Remove_Course_UseCase class attributes and methods

# Modify_Course_UseCase class attributes and methods

# Show_Course_UseCase class attributes and methods

# LearningMaterial_UseCase class attributes and methods

# Reports_UseCase class attributes and methods

# Show_Grade_UseCase class attributes and methods

# Login_UseCase class attributes and methods

# Teacher_Actor class attributes and methods

# Class_Course_List_UseCase class attributes and methods

# Select_Course_List_UseCase class attributes and methods

# Grade_Course_UseCase class attributes and methods

# User_Info_UseCase class attributes and methods

# Update_Registar_UseCase class attributes and methods

# UseCase_UseCase class attributes and methods

# Corporate_Client_Actor class attributes and methods

# Corporate_UseCase class attributes and methods

# class_Student_Registration class attributes and methods

# class_Student_Registration_Student class attributes and methods
class_Student_Registration_Student_attribute: Property = Property(name="attribute", type=StringType)
class_Student_Registration_Student_String: Property = Property(name="String", type=Name_UseCase)
class_Student_Registration_Student_String1: Property = Property(name="String1", type=Student_ID_UseCase)
class_Student_Registration_Student_String2: Property = Property(name="String2", type=Address_UseCase)
class_Student_Registration_Student_Integer: Property = Property(name="Integer", type=StringType)
class_Student_Registration_Student_Function: Property = Property(name="Function", type=Add_Course_UseCase)
class_Student_Registration_Student.attributes={class_Student_Registration_Student_String2, class_Student_Registration_Student_String, class_Student_Registration_Student_attribute, class_Student_Registration_Student_String1, class_Student_Registration_Student_Function, class_Student_Registration_Student_Integer}

# class_Student_Registration_Teacher class attributes and methods

# class_Student_Registration_Corporate class attributes and methods

# class_Student_Registration_Admin class attributes and methods

# _UseCase class attributes and methods

# Student class attributes and methods
Student_student_name: Property = Property(name="student_name", type=StringType)
Student_student_ID: Property = Property(name="student_ID", type=IntegerType)
Student_phone: Property = Property(name="phone", type=IntegerType)
Student_studentRate: Property = Property(name="studentRate", type=IntegerType)
Student.attributes={Student_student_name, Student_student_ID, Student_studentRate, Student_phone}

# Course class attributes and methods
Course_courseName: Property = Property(name="courseName", type=StringType)
Course_Description: Property = Property(name="Description", type=StringType)
Course_courseCode: Property = Property(name="courseCode", type=IntegerType)
Course_start_date: Property = Property(name="start_date", type=StringType)
Course_end_date: Property = Property(name="end_date", type=StringType)
Course.attributes={Course_end_date, Course_courseName, Course_courseCode, Course_start_date, Course_Description}

# corprateClient class attributes and methods
corprateClient_client_name: Property = Property(name="client_name", type=StringType)
corprateClient_client_ID: Property = Property(name="client_ID", type=IntegerType)
corprateClient_phone: Property = Property(name="phone", type=IntegerType)
corprateClient_companyRate: Property = Property(name="companyRate", type=IntegerType)
corprateClient.attributes={corprateClient_client_name, corprateClient_client_ID, corprateClient_companyRate, corprateClient_phone}

# Teacher class attributes and methods
Teacher_teacher_name: Property = Property(name="teacher_name", type=StringType)
Teacher_teacher_ID: Property = Property(name="teacher_ID", type=IntegerType)
Teacher_phone: Property = Property(name="phone", type=IntegerType)
Teacher_class_list: Property = Property(name="class_list", type=StringType)
Teacher.attributes={Teacher_teacher_ID, Teacher_phone, Teacher_teacher_name, Teacher_class_list}

# Registrar class attributes and methods
Registrar_Status: Property = Property(name="Status", type=Enumeration_)
Registrar_courseList: Property = Property(name="courseList", type=StringType)
Registrar__attr: Property = Property(name="_attr", type=StringType)
Registrar.attributes={Registrar_Status, Registrar__attr, Registrar_courseList}

# ADMIN class attributes and methods

# registeredUser class attributes and methods
registeredUser_Id: Property = Property(name="Id", type=IntegerType)
registeredUser_Status: Property = Property(name="Status", type=StringType)
registeredUser.attributes={registeredUser_Status, registeredUser_Id}

# Admin class attributes and methods
Admin_attribute: Property = Property(name="attribute", type=StringType)
Admin_Name: Property = Property(name="Name", type=StringType)
Admin_registrarList: Property = Property(name="registrarList", type=StringType)
Admin_courseList: Property = Property(name="courseList", type=StringType)
Admin_User_status: Property = Property(name="User_status", type=StringType)
Admin.attributes={Admin_registrarList, Admin_courseList, Admin_attribute, Admin_Name, Admin_User_status}

# courseList class attributes and methods
courseList_Class: Property = Property(name="Class", type=Add_Course_UseCase)
courseList_currentCourse: Property = Property(name="currentCourse", type=Course)
courseList.attributes={courseList_Class, courseList_currentCourse}

# Class class attributes and methods

# Relationships
STUDENT_REGISTER: BinaryAssociation = BinaryAssociation(
    name="STUDENT_REGISTER",
    ends={
        Property(name="rEGISTER0", type=Add_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="sTUDENT1", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
FIND_CLASS_STUDENT: BinaryAssociation = BinaryAssociation(
    name="FIND_CLASS_STUDENT",
    ends={
        Property(name="sTUDENT2", type=Student_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="fIND_CLASS3", type=CompleteCourse_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
CORPORATE_CLIENT_AddCourse: BinaryAssociation = BinaryAssociation(
    name="CORPORATE_CLIENT_AddCourse",
    ends={
        Property(name="addCourse4", type=Add_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cORPORATE_CLIENT5", type=CORPORATE_CLIENT_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CORPORATE_CLIENT_DropCourse: BinaryAssociation = BinaryAssociation(
    name="CORPORATE_CLIENT_DropCourse",
    ends={
        Property(name="dropCourse6", type=Drop_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cORPORATE_CLIENT7", type=CORPORATE_CLIENT_Actor, multiplicity=Multiplicity(0, 1))
    }
)
STUDENT_AddCourse: BinaryAssociation = BinaryAssociation(
    name="STUDENT_AddCourse",
    ends={
        Property(name="addCourse8", type=Add_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="sTUDENT9", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
STUDENT_DropCourse: BinaryAssociation = BinaryAssociation(
    name="STUDENT_DropCourse",
    ends={
        Property(name="dropCourse10", type=Drop_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="sTUDENT11", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
STUDENT_ShowCourse: BinaryAssociation = BinaryAssociation(
    name="STUDENT_ShowCourse",
    ends={
        Property(name="showCourse12", type=Show_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="sTUDENT13", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CORPORATE_CLIENT_ShowCourse: BinaryAssociation = BinaryAssociation(
    name="CORPORATE_CLIENT_ShowCourse",
    ends={
        Property(name="showCourse14", type=Show_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cORPORATE_CLIENT15", type=CORPORATE_CLIENT_Actor, multiplicity=Multiplicity(0, 1))
    }
)
TEACHER_ShowCourse: BinaryAssociation = BinaryAssociation(
    name="TEACHER_ShowCourse",
    ends={
        Property(name="showCourse16", type=Show_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tEACHER17", type=TEACHER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
TRAINING_ADMIN_ShowCourse: BinaryAssociation = BinaryAssociation(
    name="TRAINING_ADMIN_ShowCourse",
    ends={
        Property(name="showCourse18", type=Show_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tRAINING_ADMIN19", type=Traning_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
TRAINING_ADMIN_CreateCourse: BinaryAssociation = BinaryAssociation(
    name="TRAINING_ADMIN_CreateCourse",
    ends={
        Property(name="createCourse20", type=Create_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tRAINING_ADMIN21", type=Traning_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
TRAINING_ADMIN_RemoveCourse: BinaryAssociation = BinaryAssociation(
    name="TRAINING_ADMIN_RemoveCourse",
    ends={
        Property(name="removeCourse22", type=Remove_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tRAINING_ADMIN23", type=Traning_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
TRAINING_ADMIN_ModifyCourse: BinaryAssociation = BinaryAssociation(
    name="TRAINING_ADMIN_ModifyCourse",
    ends={
        Property(name="modifyCourse24", type=Modify_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tRAINING_ADMIN25", type=Traning_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Reports_TRAINING_ADMIN: BinaryAssociation = BinaryAssociation(
    name="Reports_TRAINING_ADMIN",
    ends={
        Property(name="tRAINING_ADMIN26", type=Traning_Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="reports27", type=Reports_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Traning_Admin_Login: BinaryAssociation = BinaryAssociation(
    name="Traning_Admin_Login",
    ends={
        Property(name="login28", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="traning_Admin29", type=Traning_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_Login: BinaryAssociation = BinaryAssociation(
    name="Teacher_Login",
    ends={
        Property(name="login30", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="teacher31", type=Teacher_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Login: BinaryAssociation = BinaryAssociation(
    name="Student_Login",
    ends={
        Property(name="login32", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student33", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Show_Grade: BinaryAssociation = BinaryAssociation(
    name="Student_Show_Grade",
    ends={
        Property(name="show_Grade34", type=Show_Grade_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student35", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_Show_Course: BinaryAssociation = BinaryAssociation(
    name="Teacher_Show_Course",
    ends={
        Property(name="show_Course36", type=Show_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="teacher37", type=Teacher_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Traning_Admin_Class_Course_List: BinaryAssociation = BinaryAssociation(
    name="Traning_Admin_Class_Course_List",
    ends={
        Property(name="class_Course_List38", type=Class_Course_List_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="traning_Admin39", type=Traning_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Select_Class_List_Teacher: BinaryAssociation = BinaryAssociation(
    name="Select_Class_List_Teacher",
    ends={
        Property(name="teacher40", type=Teacher_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="select_Class_List41", type=Select_Course_List_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Grade_Course_Teacher: BinaryAssociation = BinaryAssociation(
    name="Grade_Course_Teacher",
    ends={
        Property(name="teacher42", type=Teacher_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="grade_Course43", type=Grade_Course_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Traning_Admin_User_Info: BinaryAssociation = BinaryAssociation(
    name="Traning_Admin_User_Info",
    ends={
        Property(name="user_Info44", type=User_Info_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="traning_Admin45", type=Traning_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Update_Registar_Traning_Admin: BinaryAssociation = BinaryAssociation(
    name="Update_Registar_Traning_Admin",
    ends={
        Property(name="traning_Admin46", type=Traning_Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="update_Registar47", type=Update_Registar_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Corporate_Client_Login: BinaryAssociation = BinaryAssociation(
    name="Corporate_Client_Login",
    ends={
        Property(name="login48", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="corporate_Client49", type=Corporate_Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Add_Course_Corporate_Client: BinaryAssociation = BinaryAssociation(
    name="Add_Course_Corporate_Client",
    ends={
        Property(name="corporate_Client50", type=Corporate_Client_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="add_Course51", type=Add_Course_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Drop_Course_Corporate_Client: BinaryAssociation = BinaryAssociation(
    name="Drop_Course_Corporate_Client",
    ends={
        Property(name="corporate_Client52", type=Corporate_Client_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="drop_Course53", type=Drop_Course_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Corporate_Client_Show_Grade: BinaryAssociation = BinaryAssociation(
    name="Corporate_Client_Show_Grade",
    ends={
        Property(name="show_Grade54", type=Show_Grade_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="corporate_Client55", type=Corporate_Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Corporate_Client_Show_Course: BinaryAssociation = BinaryAssociation(
    name="Corporate_Client_Show_Course",
    ends={
        Property(name="show_Course56", type=Show_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="corporate_Client57", type=Corporate_Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_registeredUser: BinaryAssociation = BinaryAssociation(
    name="Admin_registeredUser",
    ends={
        Property(name="registeredUser58", type=registeredUser, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin59", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Admin_registeredUser2: BinaryAssociation = BinaryAssociation(
    name="Admin_registeredUser2",
    ends={
        Property(name="registeredUser60", type=registeredUser, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin61", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Student_addCourse: BinaryAssociation = BinaryAssociation(
    name="Student_addCourse",
    ends={
        Property(name="Course62", type=Course, multiplicity=Multiplicity(1, 1)),
        Property(name="student63", type=Student, multiplicity=Multiplicity(0, 9999))
    }
)
Course_Student: BinaryAssociation = BinaryAssociation(
    name="Course_Student",
    ends={
        Property(name="student64", type=Student, multiplicity=Multiplicity(0, 9999)),
        Property(name="course65", type=Course, multiplicity=Multiplicity(1, 1))
    }
)
Teacher_classSchedule: BinaryAssociation = BinaryAssociation(
    name="Teacher_classSchedule",
    ends={
        Property(name="classSchedule66", type=courseList, multiplicity=Multiplicity(0, 1)),
        Property(name="teacher67", type=Teacher, multiplicity=Multiplicity(1, 1))
    }
)
Course_corprateClient: BinaryAssociation = BinaryAssociation(
    name="Course_corprateClient",
    ends={
        Property(name="corprateClient68", type=corprateClient, multiplicity=Multiplicity(0, 9999)),
        Property(name="course69", type=Course, multiplicity=Multiplicity(1, 1))
    }
)
courseList_Course: BinaryAssociation = BinaryAssociation(
    name="courseList_Course",
    ends={
        Property(name="course70", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="courseList71", type=courseList, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_fwjc0JPiEemUc_r98N0eWg",
    types={Student_Actor, TEACHER_Actor, CORPORATE_CLIENT_Actor, Traning_Admin_Actor, Student_ID_UseCase, Name_UseCase, Address_UseCase, Create_Course_UseCase, Courses_Component, Add_Course_UseCase, Drop_Course_UseCase, CompleteCourse_UseCase, Remove_Course_UseCase, Modify_Course_UseCase, Show_Course_UseCase, LearningMaterial_UseCase, Reports_UseCase, Show_Grade_UseCase, Login_UseCase, Teacher_Actor, Class_Course_List_UseCase, Select_Course_List_UseCase, Grade_Course_UseCase, User_Info_UseCase, Update_Registar_UseCase, UseCase_UseCase, Corporate_Client_Actor, Corporate_UseCase, class_Student_Registration, class_Student_Registration_Student, class_Student_Registration_Teacher, class_Student_Registration_Corporate, class_Student_Registration_Admin, _UseCase, Student, Course, corprateClient, Teacher, Registrar, ADMIN, registeredUser, Admin, courseList, Class_, Enumeration_, Status, Enumeration1},
    associations={STUDENT_REGISTER, FIND_CLASS_STUDENT, CORPORATE_CLIENT_AddCourse, CORPORATE_CLIENT_DropCourse, STUDENT_AddCourse, STUDENT_DropCourse, STUDENT_ShowCourse, CORPORATE_CLIENT_ShowCourse, TEACHER_ShowCourse, TRAINING_ADMIN_ShowCourse, TRAINING_ADMIN_CreateCourse, TRAINING_ADMIN_RemoveCourse, TRAINING_ADMIN_ModifyCourse, Reports_TRAINING_ADMIN, Traning_Admin_Login, Teacher_Login, Student_Login, Student_Show_Grade, Teacher_Show_Course, Traning_Admin_Class_Course_List, Select_Class_List_Teacher, Grade_Course_Teacher, Traning_Admin_User_Info, Update_Registar_Traning_Admin, Corporate_Client_Login, Add_Course_Corporate_Client, Drop_Course_Corporate_Client, Corporate_Client_Show_Grade, Corporate_Client_Show_Course, Admin_registeredUser, Admin_registeredUser2, Student_addCourse, Course_Student, Teacher_classSchedule, Course_corprateClient, courseList_Course},
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