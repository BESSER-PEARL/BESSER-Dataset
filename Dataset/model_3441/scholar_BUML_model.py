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
scholar_Student = Class(name="scholar::Student")
scholar_Teacher = Class(name="scholar::Teacher")
scholar_Discipline = Class(name="scholar::Discipline")
Named = Class(name="Named")
scholar_Exam = Class(name="scholar::Exam")
scholar_Lecture = Class(name="scholar::Lecture")
scholar_ScholarManagement = Class(name="scholar::ScholarManagement")
scholar_Named = Class(name="scholar::Named", is_abstract=True)

# scholar_Student class attributes and methods
scholar_Student_forname: Property = Property(name="forname", type=StringType)
scholar_Student.attributes={scholar_Student_forname}

# scholar_Teacher class attributes and methods

# scholar_Discipline class attributes and methods

# Named class attributes and methods

# scholar_Exam class attributes and methods
scholar_Exam_score: Property = Property(name="score", type=FloatType)
scholar_Exam.attributes={scholar_Exam_score}

# scholar_Lecture class attributes and methods

# scholar_ScholarManagement class attributes and methods

# scholar_Named class attributes and methods
scholar_Named_name: Property = Property(name="name", type=StringType)
scholar_Named.attributes={scholar_Named_name}

# Relationships
lecture_teacher1: BinaryAssociation = BinaryAssociation(
    name="lecture_teacher1",
    ends={
        Property(name="scholar_Teacher", type=scholar_Lecture, multiplicity=Multiplicity(1, 1)),
        Property(name="scholar_Lecture", type=scholar_Teacher, multiplicity=Multiplicity(0, 1))
    }
)
discipline2: BinaryAssociation = BinaryAssociation(
    name="discipline2",
    ends={
        Property(name="scholar_Discipline", type=scholar_Lecture, multiplicity=Multiplicity(1, 1)),
        Property(name="scholar_Lecture3", type=scholar_Discipline, multiplicity=Multiplicity(0, 1))
    }
)
exams0: BinaryAssociation = BinaryAssociation(
    name="exams0",
    ends={
        Property(name="scholar_Exam", type=scholar_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="scholar_Student", type=scholar_Exam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lecture4: BinaryAssociation = BinaryAssociation(
    name="lecture4",
    ends={
        Property(name="scholar_Lecture6", type=scholar_Exam, multiplicity=Multiplicity(1, 1)),
        Property(name="scholar_Exam5", type=scholar_Lecture, multiplicity=Multiplicity(0, 1))
    }
)
students7: BinaryAssociation = BinaryAssociation(
    name="students7",
    ends={
        Property(name="scholar_Student8", type=scholar_ScholarManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="scholar_ScholarManagement", type=scholar_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
disciplines9: BinaryAssociation = BinaryAssociation(
    name="disciplines9",
    ends={
        Property(name="scholar_Discipline11", type=scholar_ScholarManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="scholar_ScholarManagement10", type=scholar_Discipline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lectures12: BinaryAssociation = BinaryAssociation(
    name="lectures12",
    ends={
        Property(name="scholar_Lecture14", type=scholar_ScholarManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="scholar_ScholarManagement13", type=scholar_Lecture, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teachers15: BinaryAssociation = BinaryAssociation(
    name="teachers15",
    ends={
        Property(name="scholar_Teacher17", type=scholar_ScholarManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="scholar_ScholarManagement16", type=scholar_Teacher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_scholar_Exam_Named = Generalization(general=Named, specific=scholar_Exam)
gen_scholar_Student_Named = Generalization(general=Named, specific=scholar_Student)
gen_scholar_Lecture_Named = Generalization(general=Named, specific=scholar_Lecture)
gen_scholar_Discipline_Named = Generalization(general=Named, specific=scholar_Discipline)
gen_scholar_Teacher_Named = Generalization(general=Named, specific=scholar_Teacher)

# Domain Model
domain_model = DomainModel(
    name="scholar",
    types={scholar_Student, scholar_Teacher, scholar_Discipline, Named, scholar_Exam, scholar_Lecture, scholar_ScholarManagement, scholar_Named},
    associations={lecture_teacher1, discipline2, exams0, lecture4, students7, disciplines9, lectures12, teachers15},
    generalizations={gen_scholar_Exam_Named, gen_scholar_Student_Named, gen_scholar_Lecture_Named, gen_scholar_Discipline_Named, gen_scholar_Teacher_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)