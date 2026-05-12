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
StudentPortal = Class(name="StudentPortal")
Portal = Class(name="Portal")
AcademicRecords = Class(name="AcademicRecords")
FacultyInfo = Class(name="FacultyInfo")
Department = Class(name="Department")
Attendance = Class(name="Attendance")
AcademicResult = Class(name="AcademicResult")
Student = Class(name="Student")
Course = Class(name="Course")
Dues = Class(name="Dues")
Student_Actor = Class(name="Student_Actor")
Package_getResult_UseCase = Class(name="Package_getResult_UseCase")
Package_UseCase = Class(name="Package_UseCase")
Teacher_Actor = Class(name="Teacher_Actor")
Administrator_Actor = Class(name="Administrator_Actor")
Administrator = Class(name="Administrator")
UseCase_UseCase = Class(name="UseCase_UseCase")
UseCase2_UseCase = Class(name="UseCase2_UseCase")
ELibrary = Class(name="ELibrary")

# StudentPortal class attributes and methods

# Portal class attributes and methods

# AcademicRecords class attributes and methods
AcademicRecords_student: Property = Property(name="student", type=Student)
AcademicRecords_attendance: Property = Property(name="attendance", type=Attendance)
AcademicRecords_result: Property = Property(name="result", type=AcademicResult)
AcademicRecords_dues: Property = Property(name="dues", type=IntegerType)
AcademicRecords.attributes={AcademicRecords_attendance, AcademicRecords_dues, AcademicRecords_student, AcademicRecords_result}

# FacultyInfo class attributes and methods
FacultyInfo_facultyID: Property = Property(name="facultyID", type=StringType)
FacultyInfo_facultyName: Property = Property(name="facultyName", type=StringType)
FacultyInfo_department: Property = Property(name="department", type=Department)
FacultyInfo.attributes={FacultyInfo_facultyID, FacultyInfo_department, FacultyInfo_facultyName}

# Department class attributes and methods
Department_name: Property = Property(name="name", type=StringType)
Department_course: Property = Property(name="course", type=Course)
Department.attributes={Department_course, Department_name}

# Attendance class attributes and methods
Attendance_student: Property = Property(name="student", type=Student)
Attendance_course: Property = Property(name="course", type=Course)
Attendance.attributes={Attendance_course, Attendance_student}

# AcademicResult class attributes and methods
AcademicResult_semester: Property = Property(name="semester", type=IntegerType)
AcademicResult.attributes={AcademicResult_semester}

# Student class attributes and methods
Student_name: Property = Property(name="name", type=StringType)
Student_scholarNo: Property = Property(name="scholarNo", type=IntegerType)
Student_branch: Property = Property(name="branch", type=Department)
Student_semester: Property = Property(name="semester", type=IntegerType)
Student.attributes={Student_branch, Student_name, Student_scholarNo, Student_semester}

# Course class attributes and methods
Course_courseName: Property = Property(name="courseName", type=StringType)
Course_subjectCode: Property = Property(name="subjectCode", type=StringType)
Course.attributes={Course_courseName, Course_subjectCode}

# Dues class attributes and methods
Dues_student: Property = Property(name="student", type=Student)
Dues_amount: Property = Property(name="amount", type=IntegerType)
Dues.attributes={Dues_amount, Dues_student}

# Student_Actor class attributes and methods

# Package_getResult_UseCase class attributes and methods

# Package_UseCase class attributes and methods

# Teacher_Actor class attributes and methods

# Administrator_Actor class attributes and methods

# Administrator class attributes and methods
Administrator_name: Property = Property(name="name", type=StringType)
Administrator_administratorID: Property = Property(name="administratorID", type=IntegerType)
Administrator.attributes={Administrator_name, Administrator_administratorID}

# UseCase_UseCase class attributes and methods

# UseCase2_UseCase class attributes and methods

# ELibrary class attributes and methods

# Relationships
Portal_StudentPortal: BinaryAssociation = BinaryAssociation(
    name="Portal_StudentPortal",
    ends={
        Property(name="studentPortal0", type=StudentPortal, multiplicity=Multiplicity(0, 1)),
        Property(name="portal1", type=Portal, multiplicity=Multiplicity(0, 1))
    }
)
Portal_AcademicRecords: BinaryAssociation = BinaryAssociation(
    name="Portal_AcademicRecords",
    ends={
        Property(name="academicRecords2", type=AcademicRecords, multiplicity=Multiplicity(0, 1)),
        Property(name="portal3", type=Portal, multiplicity=Multiplicity(0, 1))
    }
)
Department_Course: BinaryAssociation = BinaryAssociation(
    name="Department_Course",
    ends={
        Property(name="course10", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="department11", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
FacultyInfo_Department: BinaryAssociation = BinaryAssociation(
    name="FacultyInfo_Department",
    ends={
        Property(name="department212", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="facultyInfo13", type=FacultyInfo, multiplicity=Multiplicity(0, 1))
    }
)
Student_getResult: BinaryAssociation = BinaryAssociation(
    name="Student_getResult",
    ends={
        Property(name="getResult14", type=Package_getResult_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student15", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
AcademicRecords_Administrator: BinaryAssociation = BinaryAssociation(
    name="AcademicRecords_Administrator",
    ends={
        Property(name="administrator16", type=Administrator, multiplicity=Multiplicity(0, 1)),
        Property(name="academicRecords17", type=AcademicRecords, multiplicity=Multiplicity(0, 1))
    }
)
Department_Student: BinaryAssociation = BinaryAssociation(
    name="Department_Student",
    ends={
        Property(name="student18", type=Student, multiplicity=Multiplicity(0, 1)),
        Property(name="department19", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
AcademicRecords_Student: BinaryAssociation = BinaryAssociation(
    name="AcademicRecords_Student",
    ends={
        Property(name="student220", type=Student, multiplicity=Multiplicity(0, 1)),
        Property(name="academicRecords21", type=AcademicRecords, multiplicity=Multiplicity(0, 1))
    }
)
Attendance_AcademicRecords: BinaryAssociation = BinaryAssociation(
    name="Attendance_AcademicRecords",
    ends={
        Property(name="academicRecords4", type=AcademicRecords, multiplicity=Multiplicity(0, 1)),
        Property(name="attendance5", type=Attendance, multiplicity=Multiplicity(0, 1))
    }
)
AcademicRecords_AcademicResult: BinaryAssociation = BinaryAssociation(
    name="AcademicRecords_AcademicResult",
    ends={
        Property(name="academicResult6", type=AcademicResult, multiplicity=Multiplicity(0, 1)),
        Property(name="academicRecords7", type=AcademicRecords, multiplicity=Multiplicity(0, 1))
    }
)
Dues_Portal: BinaryAssociation = BinaryAssociation(
    name="Dues_Portal",
    ends={
        Property(name="portal8", type=Portal, multiplicity=Multiplicity(0, 1)),
        Property(name="dues9", type=Dues, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_DIlkIAZuEeipbtix_oa2Dg",
    types={StudentPortal, Portal, AcademicRecords, FacultyInfo, Department, Attendance, AcademicResult, Student, Course, Dues, Student_Actor, Package_getResult_UseCase, Package_UseCase, Teacher_Actor, Administrator_Actor, Administrator, UseCase_UseCase, UseCase2_UseCase, ELibrary},
    associations={Portal_StudentPortal, Portal_AcademicRecords, Department_Course, FacultyInfo_Department, Student_getResult, AcademicRecords_Administrator, Department_Student, AcademicRecords_Student, Attendance_AcademicRecords, AcademicRecords_AcademicResult, Dues_Portal},
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