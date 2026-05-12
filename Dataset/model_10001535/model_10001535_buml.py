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
Portal = Class(name="Portal")
AcademicRecords = Class(name="AcademicRecords")
FacultyInfo = Class(name="FacultyInfo")
Department = Class(name="Department")
AcademicResult = Class(name="AcademicResult")
Student = Class(name="Student")
Course = Class(name="Course")
Administrator = Class(name="Administrator")

# Portal class attributes and methods

# AcademicRecords class attributes and methods
AcademicRecords_student: Property = Property(name="student", type=Student)
AcademicRecords_attendance: Property = Property(name="attendance", type=StringType)
AcademicRecords_result: Property = Property(name="result", type=AcademicResult)
AcademicRecords_dues: Property = Property(name="dues", type=IntegerType)
AcademicRecords.attributes={AcademicRecords_result, AcademicRecords_dues, AcademicRecords_attendance, AcademicRecords_student}

# FacultyInfo class attributes and methods
FacultyInfo_facultyID: Property = Property(name="facultyID", type=StringType)
FacultyInfo_facultyName: Property = Property(name="facultyName", type=StringType)
FacultyInfo_department: Property = Property(name="department", type=Department)
FacultyInfo.attributes={FacultyInfo_facultyName, FacultyInfo_department, FacultyInfo_facultyID}

# Department class attributes and methods
Department_name: Property = Property(name="name", type=StringType)
Department_course: Property = Property(name="course", type=Course)
Department.attributes={Department_course, Department_name}

# AcademicResult class attributes and methods
AcademicResult_semester: Property = Property(name="semester", type=IntegerType)
AcademicResult.attributes={AcademicResult_semester}

# Student class attributes and methods
Student_name: Property = Property(name="name", type=StringType)
Student_scholarNo: Property = Property(name="scholarNo", type=IntegerType)
Student_branch: Property = Property(name="branch", type=Department)
Student_semester: Property = Property(name="semester", type=IntegerType)
Student.attributes={Student_semester, Student_branch, Student_name, Student_scholarNo}

# Course class attributes and methods
Course_courseName: Property = Property(name="courseName", type=StringType)
Course_subjectCode: Property = Property(name="subjectCode", type=StringType)
Course.attributes={Course_subjectCode, Course_courseName}

# Administrator class attributes and methods
Administrator_name: Property = Property(name="name", type=StringType)
Administrator_administratorID: Property = Property(name="administratorID", type=IntegerType)
Administrator.attributes={Administrator_name, Administrator_administratorID}

# Relationships
Portal_AcademicRecords: BinaryAssociation = BinaryAssociation(
    name="Portal_AcademicRecords",
    ends={
        Property(name="academicRecords0", type=AcademicRecords, multiplicity=Multiplicity(0, 1)),
        Property(name="portal1", type=Portal, multiplicity=Multiplicity(0, 1))
    }
)
AcademicRecords_Administrator: BinaryAssociation = BinaryAssociation(
    name="AcademicRecords_Administrator",
    ends={
        Property(name="administrator2", type=Administrator, multiplicity=Multiplicity(0, 1)),
        Property(name="academicRecords3", type=AcademicRecords, multiplicity=Multiplicity(0, 1))
    }
)
AcademicRecords_Student: BinaryAssociation = BinaryAssociation(
    name="AcademicRecords_Student",
    ends={
        Property(name="student24", type=Student, multiplicity=Multiplicity(0, 1)),
        Property(name="academicRecords5", type=AcademicRecords, multiplicity=Multiplicity(0, 1))
    }
)
AcademicRecords_AcademicResult: BinaryAssociation = BinaryAssociation(
    name="AcademicRecords_AcademicResult",
    ends={
        Property(name="academicResult6", type=AcademicResult, multiplicity=Multiplicity(0, 1)),
        Property(name="academicRecords7", type=AcademicRecords, multiplicity=Multiplicity(0, 1))
    }
)
FacultyInfo_Department: BinaryAssociation = BinaryAssociation(
    name="FacultyInfo_Department",
    ends={
        Property(name="department28", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="facultyInfo9", type=FacultyInfo, multiplicity=Multiplicity(0, 1))
    }
)
Department_Course: BinaryAssociation = BinaryAssociation(
    name="Department_Course",
    ends={
        Property(name="course10", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="department11", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Department_Student: BinaryAssociation = BinaryAssociation(
    name="Department_Student",
    ends={
        Property(name="student12", type=Student, multiplicity=Multiplicity(0, 1)),
        Property(name="department13", type=Department, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_EFLyoDdrEeiQp6eXyhUzBA",
    types={Portal, AcademicRecords, FacultyInfo, Department, AcademicResult, Student, Course, Administrator},
    associations={Portal_AcademicRecords, AcademicRecords_Administrator, AcademicRecords_Student, AcademicRecords_AcademicResult, FacultyInfo_Department, Department_Course, Department_Student},
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