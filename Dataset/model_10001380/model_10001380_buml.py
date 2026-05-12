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
Student__: Enumeration = Enumeration(
    name="Student__",
    literals={
            
    }
)

Teacher__: Enumeration = Enumeration(
    name="Teacher__",
    literals={
            
    }
)

StudyField__: Enumeration = Enumeration(
    name="StudyField__",
    literals={
            
    }
)

Subjects__: Enumeration = Enumeration(
    name="Subjects__",
    literals={
            
    }
)

# Classes
School = Class(name="School")
Student = Class(name="Student")
Teacher = Class(name="Teacher")
Exam = Class(name="Exam")
Headmaster = Class(name="Headmaster")
StudyField = Class(name="StudyField")
Subject = Class(name="Subject")

# School class attributes and methods
School_students: Property = Property(name="students", type=Student__)
School_studentsCount: Property = Property(name="studentsCount", type=IntegerType)
School_teachers: Property = Property(name="teachers", type=Teacher__)
School_teachersCount: Property = Property(name="teachersCount", type=IntegerType)
School_fields: Property = Property(name="fields", type=StudyField__)
School_fieldsCount: Property = Property(name="fieldsCount", type=IntegerType)
School_headmaster: Property = Property(name="headmaster", type=Headmaster)
School_name: Property = Property(name="name", type=IntegerType)
School.attributes={School_fieldsCount, School_students, School_headmaster, School_teachers, School_studentsCount, School_name, School_fields, School_teachersCount}

# Student class attributes and methods

# Teacher class attributes and methods

# Exam class attributes and methods
Exam_name: Property = Property(name="name", type=StringType)
Exam_id: Property = Property(name="id", type=StringType)
Exam_points: Property = Property(name="points", type=IntegerType)
Exam_subject: Property = Property(name="subject", type=Subject)
Exam_currentId: Property = Property(name="currentId", type=IntegerType)
Exam.attributes={Exam_subject, Exam_id, Exam_currentId, Exam_name, Exam_points}

# Headmaster class attributes and methods

# StudyField class attributes and methods
StudyField_name: Property = Property(name="name", type=StringType)
StudyField_id: Property = Property(name="id", type=IntegerType)
StudyField_subjects: Property = Property(name="subjects", type=Subjects__)
StudyField_subjectsCount: Property = Property(name="subjectsCount", type=IntegerType)
StudyField_currentId: Property = Property(name="currentId", type=IntegerType)
StudyField.attributes={StudyField_subjects, StudyField_name, StudyField_currentId, StudyField_subjectsCount, StudyField_id}

# Subject class attributes and methods
Subject_name: Property = Property(name="name", type=StringType)
Subject_id: Property = Property(name="id", type=IntegerType)
Subject_credits: Property = Property(name="credits", type=IntegerType)
Subject_currentId: Property = Property(name="currentId", type=IntegerType)
Subject.attributes={Subject_name, Subject_credits, Subject_id, Subject_currentId}

# Domain Model
domain_model = DomainModel(
    name="_3UpZwFMqEemuQ_TjUfVNTA",
    types={School, Student, Teacher, Exam, Headmaster, StudyField, Subject, Student__, Teacher__, StudyField__, Subjects__},
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