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
Exceptions = Class(name="Exceptions")
Finance = Class(name="Finance")
Insturctor = Class(name="Insturctor")

# Admin class attributes and methods
Admin_AdminFileName: Property = Property(name="AdminFileName", type=StringType)
Admin.attributes={Admin_AdminFileName}

# Course class attributes and methods
Course_CTutor: Property = Property(name="CTutor", type=StringType)
Course_Cid: Property = Property(name="Cid", type=StringType)
Course_Cname: Property = Property(name="Cname", type=StringType)
Course_Course_File_Name: Property = Property(name="Course_File_Name", type=StringType)
Course_Course_REG: Property = Property(name="Course_REG", type=StringType)
Course_Cprice: Property = Property(name="Cprice", type=StringType)
Course.attributes={Course_Cprice, Course_Cid, Course_Cname, Course_Course_File_Name, Course_CTutor, Course_Course_REG}

# Exam class attributes and methods
Exam_EID: Property = Property(name="EID", type=StringType)
Exam_EName: Property = Property(name="EName", type=StringType)
Exam_ETIME: Property = Property(name="ETIME", type=StringType)
Exam_Exam_File_Name: Property = Property(name="Exam_File_Name", type=StringType)
Exam_MaxGrade: Property = Property(name="MaxGrade", type=StringType)
Exam.attributes={Exam_EID, Exam_ETIME, Exam_Exam_File_Name, Exam_MaxGrade, Exam_EName}

# Email class attributes and methods
Email_Email: Property = Property(name="Email", type=StringType)
Email.attributes={Email_Email}

# FileBinary class attributes and methods

# ILogin_Interface class attributes and methods

# Exceptions class attributes and methods

# Finance class attributes and methods
Finance_Cname: Property = Property(name="Cname", type=StringType)
Finance_coast: Property = Property(name="coast", type=StringType)
Finance.attributes={Finance_coast, Finance_Cname}

# Insturctor class attributes and methods
Insturctor_INfilename: Property = Property(name="INfilename", type=StringType)
Insturctor.attributes={Insturctor_INfilename}

# Domain Model
domain_model = DomainModel(
    name="_68a36e34_602a_45aa_93c9_b4f3b59202fa",
    types={Admin, Course, Exam, Email, FileBinary, ILogin_Interface, Exceptions, Finance, Insturctor},
    associations={},
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