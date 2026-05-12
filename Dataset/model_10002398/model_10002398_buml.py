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
mypackage_Perosn = Class(name="mypackage_Perosn")
mypackage_Staff = Class(name="mypackage_Staff")
mypackage_Student = Class(name="mypackage_Student")
mypackage_studentAffairsEmp = Class(name="mypackage_studentAffairsEmp")
mypackage_Tutor = Class(name="mypackage_Tutor")
mypackage_Admin = Class(name="mypackage_Admin")
mypackage_Course = Class(name="mypackage_Course")
mypackage_Exam = Class(name="mypackage_Exam")
mypackage_FileManager = Class(name="mypackage_FileManager")

# mypackage_Perosn class attributes and methods
mypackage_Perosn_id: Property = Property(name="id", type=IntegerType)
mypackage_Perosn_UserName: Property = Property(name="UserName", type=StringType)
mypackage_Perosn_fName: Property = Property(name="fName", type=StringType)
mypackage_Perosn_lname: Property = Property(name="lname", type=StringType)
mypackage_Perosn_age: Property = Property(name="age", type=IntegerType)
mypackage_Perosn.attributes={mypackage_Perosn_UserName, mypackage_Perosn_lname, mypackage_Perosn_age, mypackage_Perosn_fName, mypackage_Perosn_id}

# mypackage_Staff class attributes and methods
mypackage_Staff_salary: Property = Property(name="salary", type=StringType)
mypackage_Staff.attributes={mypackage_Staff_salary}

# mypackage_Student class attributes and methods
mypackage_Student_level: Property = Property(name="level", type=IntegerType)
mypackage_Student_grade: Property = Property(name="grade", type=StringType)
mypackage_Student_studentFileName: Property = Property(name="studentFileName", type=StringType)
mypackage_Student.attributes={mypackage_Student_level, mypackage_Student_studentFileName, mypackage_Student_grade}

# mypackage_studentAffairsEmp class attributes and methods
mypackage_studentAffairsEmp_EmpFileName: Property = Property(name="EmpFileName", type=StringType)
mypackage_studentAffairsEmp.attributes={mypackage_studentAffairsEmp_EmpFileName}

# mypackage_Tutor class attributes and methods
mypackage_Tutor_TutorFileName: Property = Property(name="TutorFileName", type=StringType)
mypackage_Tutor_academicalHours: Property = Property(name="academicalHours", type=StringType)
mypackage_Tutor.attributes={mypackage_Tutor_academicalHours, mypackage_Tutor_TutorFileName}

# mypackage_Admin class attributes and methods

# mypackage_Course class attributes and methods
mypackage_Course_CreditHours: Property = Property(name="CreditHours", type=IntegerType)
mypackage_Course_CName: Property = Property(name="CName", type=StringType)
mypackage_Course_CourseFileName: Property = Property(name="CourseFileName", type=StringType)
mypackage_Course_CId: Property = Property(name="CId", type=StringType)
mypackage_Course.attributes={mypackage_Course_CId, mypackage_Course_CreditHours, mypackage_Course_CName, mypackage_Course_CourseFileName}

# mypackage_Exam class attributes and methods
mypackage_Exam_EName: Property = Property(name="EName", type=StringType)
mypackage_Exam_MaxGrade: Property = Property(name="MaxGrade", type=StringType)
mypackage_Exam_ExamsFileName: Property = Property(name="ExamsFileName", type=StringType)
mypackage_Exam_EId: Property = Property(name="EId", type=StringType)
mypackage_Exam.attributes={mypackage_Exam_MaxGrade, mypackage_Exam_EName, mypackage_Exam_EId, mypackage_Exam_ExamsFileName}

# mypackage_FileManager class attributes and methods

# Relationships
Course_Exam: BinaryAssociation = BinaryAssociation(
    name="Course_Exam",
    ends={
        Property(name="exam0", type=mypackage_Exam, multiplicity=Multiplicity(0, 1)),
        Property(name="course1", type=mypackage_Course, multiplicity=Multiplicity(0, 1))
    }
)
FileManager_Perosn: BinaryAssociation = BinaryAssociation(
    name="FileManager_Perosn",
    ends={
        Property(name="perosn2", type=mypackage_Perosn, multiplicity=Multiplicity(0, 1)),
        Property(name="fileManager3", type=mypackage_FileManager, multiplicity=Multiplicity(0, 1))
    }
)
FileManager_Course: BinaryAssociation = BinaryAssociation(
    name="FileManager_Course",
    ends={
        Property(name="course4", type=mypackage_Course, multiplicity=Multiplicity(0, 1)),
        Property(name="fileManager5", type=mypackage_FileManager, multiplicity=Multiplicity(0, 1))
    }
)
FileManager_Exam: BinaryAssociation = BinaryAssociation(
    name="FileManager_Exam",
    ends={
        Property(name="exam6", type=mypackage_Exam, multiplicity=Multiplicity(0, 1)),
        Property(name="fileManager7", type=mypackage_FileManager, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="af0f31ff_7f82_4c2f_993c_03d3d46a4887",
    types={mypackage_Perosn, mypackage_Staff, mypackage_Student, mypackage_studentAffairsEmp, mypackage_Tutor, mypackage_Admin, mypackage_Course, mypackage_Exam, mypackage_FileManager},
    associations={Course_Exam, FileManager_Perosn, FileManager_Course, FileManager_Exam},
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