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
FacultyInfo = Class(name="FacultyInfo")
Department = Class(name="Department")
AcademicResult = Class(name="AcademicResult")
Student = Class(name="Student")
Course = Class(name="Course")
Administrator = Class(name="Administrator")

# Portal class attributes and methods

# FacultyInfo class attributes and methods
FacultyInfo_facultyID: Property = Property(name="facultyID", type=StringType)
FacultyInfo_facultyName: Property = Property(name="facultyName", type=StringType)
FacultyInfo_department: Property = Property(name="department", type=Department)
FacultyInfo.attributes={FacultyInfo_department, FacultyInfo_facultyName, FacultyInfo_facultyID}

# Department class attributes and methods
Department_name: Property = Property(name="name", type=StringType)
Department_course: Property = Property(name="course", type=Course)
Department.attributes={Department_name, Department_course}

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
FacultyInfo_Department: BinaryAssociation = BinaryAssociation(
    name="FacultyInfo_Department",
    ends={
        Property(name="department20", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="facultyInfo1", type=FacultyInfo, multiplicity=Multiplicity(0, 1))
    }
)
Department_Course: BinaryAssociation = BinaryAssociation(
    name="Department_Course",
    ends={
        Property(name="course2", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="department3", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Department_Student: BinaryAssociation = BinaryAssociation(
    name="Department_Student",
    ends={
        Property(name="student4", type=Student, multiplicity=Multiplicity(0, 1)),
        Property(name="department5", type=Department, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_qCT8EDdpEeiQp6eXyhUzBA",
    types={Portal, FacultyInfo, Department, AcademicResult, Student, Course, Administrator},
    associations={FacultyInfo_Department, Department_Course, Department_Student},
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