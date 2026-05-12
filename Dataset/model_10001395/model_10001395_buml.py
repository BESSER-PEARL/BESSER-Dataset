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
Course = Class(name="Course")
Exam = Class(name="Exam")
Email = Class(name="Email")
FileBinary = Class(name="FileBinary")
ILogin_Interface = Class(name="ILogin_Interface")
Finance = Class(name="Finance")
Insturctor = Class(name="Insturctor")
Person = Class(name="Person")
Student = Class(name="Student")

# Admin class attributes and methods
Admin_AdminFileName: Property = Property(name="AdminFileName", type=StringType)
Admin.attributes={Admin_AdminFileName}

# Course class attributes and methods
Course_Course_File_Name: Property = Property(name="Course_File_Name", type=StringType)
Course_Course_REG: Property = Property(name="Course_REG", type=StringType)
Course_Cprice: Property = Property(name="Cprice", type=StringType)
Course_CTutor: Property = Property(name="CTutor", type=StringType)
Course_Cid: Property = Property(name="Cid", type=StringType)
Course_Cname: Property = Property(name="Cname", type=StringType)
Course.attributes={Course_Course_REG, Course_Cname, Course_Cid, Course_Cprice, Course_CTutor, Course_Course_File_Name}

# Exam class attributes and methods
Exam_EID: Property = Property(name="EID", type=StringType)
Exam_EName: Property = Property(name="EName", type=StringType)
Exam_ETIME: Property = Property(name="ETIME", type=StringType)
Exam_Exam_File_Name: Property = Property(name="Exam_File_Name", type=StringType)
Exam_MaxGrade: Property = Property(name="MaxGrade", type=StringType)
Exam.attributes={Exam_EID, Exam_MaxGrade, Exam_EName, Exam_ETIME, Exam_Exam_File_Name}

# Email class attributes and methods
Email_Email: Property = Property(name="Email", type=StringType)
Email.attributes={Email_Email}

# FileBinary class attributes and methods

# ILogin_Interface class attributes and methods

# Finance class attributes and methods
Finance_Cname: Property = Property(name="Cname", type=StringType)
Finance_coast: Property = Property(name="coast", type=StringType)
Finance.attributes={Finance_Cname, Finance_coast}

# Insturctor class attributes and methods
Insturctor_INfilename: Property = Property(name="INfilename", type=StringType)
Insturctor.attributes={Insturctor_INfilename}

# Person class attributes and methods
Person_id: Property = Property(name="id", type=StringType)
Person_phNum: Property = Property(name="phNum", type=StringType)
Person_PersonFName: Property = Property(name="PersonFName", type=StringType)
Person.attributes={Person_phNum, Person_id, Person_PersonFName}

# Student class attributes and methods
Student_s_age: Property = Property(name="s_age", type=IntegerType)
Student_grade: Property = Property(name="grade", type=StringType)
Student_studentfname: Property = Property(name="studentfname", type=StringType)
Student.attributes={Student_studentfname, Student_s_age, Student_grade}

# Relationships
Exam_Course: BinaryAssociation = BinaryAssociation(
    name="Exam_Course",
    ends={
        Property(name="course0", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="exam1", type=Exam, multiplicity=Multiplicity(0, 1))
    }
)
Exam_FileBinary: BinaryAssociation = BinaryAssociation(
    name="Exam_FileBinary",
    ends={
        Property(name="fileBinary2", type=FileBinary, multiplicity=Multiplicity(0, 1)),
        Property(name="exam3", type=Exam, multiplicity=Multiplicity(0, 1))
    }
)
Course_FileBinary: BinaryAssociation = BinaryAssociation(
    name="Course_FileBinary",
    ends={
        Property(name="fileBinary4", type=FileBinary, multiplicity=Multiplicity(0, 1)),
        Property(name="course5", type=Course, multiplicity=Multiplicity(0, 1))
    }
)
Email_FileBinary: BinaryAssociation = BinaryAssociation(
    name="Email_FileBinary",
    ends={
        Property(name="fileBinary6", type=FileBinary, multiplicity=Multiplicity(0, 1)),
        Property(name="email7", type=Email, multiplicity=Multiplicity(0, 1))
    }
)
Insturctor_FileBinary: BinaryAssociation = BinaryAssociation(
    name="Insturctor_FileBinary",
    ends={
        Property(name="fileBinary8", type=FileBinary, multiplicity=Multiplicity(0, 1)),
        Property(name="insturctor9", type=Insturctor, multiplicity=Multiplicity(0, 1))
    }
)
Student_FileBinary: BinaryAssociation = BinaryAssociation(
    name="Student_FileBinary",
    ends={
        Property(name="fileBinary10", type=FileBinary, multiplicity=Multiplicity(0, 1)),
        Property(name="student11", type=Student, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4HfOQON7Eee1VcqWCkiVQg",
    types={Admin, Course, Exam, Email, FileBinary, ILogin_Interface, Finance, Insturctor, Person, Student},
    associations={Exam_Course, Exam_FileBinary, Course_FileBinary, Email_FileBinary, Insturctor_FileBinary, Student_FileBinary},
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