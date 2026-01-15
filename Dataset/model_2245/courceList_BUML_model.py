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
Semester: Enumeration = Enumeration(
    name="Semester",
    literals={
            EnumerationLiteral(name="autumn"),
			EnumerationLiteral(name="spring")
    }
)

WorkForm: Enumeration = Enumeration(
    name="WorkForm",
    literals={
            EnumerationLiteral(name="oral"),
			EnumerationLiteral(name="written"),
			EnumerationLiteral(name="home")
    }
)

EducationLevel: Enumeration = Enumeration(
    name="EducationLevel",
    literals={
            EnumerationLiteral(name="bachelor"),
			EnumerationLiteral(name="master"),
			EnumerationLiteral(name="phd"),
			EnumerationLiteral(name="oneYear")
    }
)

Campus: Enumeration = Enumeration(
    name="Campus",
    literals={
            EnumerationLiteral(name="Trondheim"),
			EnumerationLiteral(name="Gjøvik"),
			EnumerationLiteral(name="Web"),
			EnumerationLiteral(name="Ålesund")
    }
)

EvaluationType: Enumeration = Enumeration(
    name="EvaluationType",
    literals={
            EnumerationLiteral(name="grade"),
			EnumerationLiteral(name="approved")
    }
)

# Classes
courceList_Department = Class(name="courceList::Department")
courceList_StudyGeneralization = Class(name="courceList::StudyGeneralization")
courceList_Cource = Class(name="courceList::Cource")
courceList_Professor = Class(name="courceList::Professor")
courceList_CourceSpecification = Class(name="courceList::CourceSpecification")
courceList_Student = Class(name="courceList::Student")
courceList_StudyProgram = Class(name="courceList::StudyProgram")
courceList_Specialisation = Class(name="courceList::Specialisation")
courceList_Work = Class(name="courceList::Work")
courceList_Exam = Class(name="courceList::Exam")
courceList_EvaluationForm = Class(name="courceList::EvaluationForm")
courceList_StudyCourceRelation = Class(name="courceList::StudyCourceRelation")

# courceList_Department class attributes and methods
courceList_Department_name: Property = Property(name="name", type=StringType)
courceList_Department_abbreviation: Property = Property(name="abbreviation", type=StringType)
courceList_Department.attributes={courceList_Department_abbreviation, courceList_Department_name}

# courceList_StudyGeneralization class attributes and methods
courceList_StudyGeneralization_name: Property = Property(name="name", type=StringType)
courceList_StudyGeneralization_educationLevel: Property = Property(name="educationLevel", type=StringType)
courceList_StudyGeneralization_nrOfYears: Property = Property(name="nrOfYears", type=IntegerType)
courceList_StudyGeneralization_campus: Property = Property(name="campus", type=StringType)
courceList_StudyGeneralization_abbreviation: Property = Property(name="abbreviation", type=StringType)
courceList_StudyGeneralization.attributes={courceList_StudyGeneralization_campus, courceList_StudyGeneralization_educationLevel, courceList_StudyGeneralization_abbreviation, courceList_StudyGeneralization_nrOfYears, courceList_StudyGeneralization_name}

# courceList_Cource class attributes and methods
courceList_Cource_code: Property = Property(name="code", type=StringType)
courceList_Cource_name: Property = Property(name="name", type=StringType)
courceList_Cource_location: Property = Property(name="location", type=StringType)
courceList_Cource.attributes={courceList_Cource_code, courceList_Cource_location, courceList_Cource_name}

# courceList_Professor class attributes and methods
courceList_Professor_name: Property = Property(name="name", type=StringType)
courceList_Professor_title: Property = Property(name="title", type=StringType)
courceList_Professor.attributes={courceList_Professor_title, courceList_Professor_name}

# courceList_CourceSpecification class attributes and methods
courceList_CourceSpecification_specificationYear: Property = Property(name="specificationYear", type=IntegerType)
courceList_CourceSpecification_semester: Property = Property(name="semester", type=StringType)
courceList_CourceSpecification_language: Property = Property(name="language", type=StringType)
courceList_CourceSpecification_version: Property = Property(name="version", type=StringType)
courceList_CourceSpecification_credits: Property = Property(name="credits", type=FloatType)
courceList_CourceSpecification_name: Property = Property(name="name", type=StringType)
courceList_CourceSpecification.attributes={courceList_CourceSpecification_semester, courceList_CourceSpecification_credits, courceList_CourceSpecification_specificationYear, courceList_CourceSpecification_language, courceList_CourceSpecification_version, courceList_CourceSpecification_name}

# courceList_Student class attributes and methods
courceList_Student_nr: Property = Property(name="nr", type=IntegerType)
courceList_Student.attributes={courceList_Student_nr}

# courceList_StudyProgram class attributes and methods
courceList_StudyProgram_year: Property = Property(name="year", type=IntegerType)
courceList_StudyProgram.attributes={courceList_StudyProgram_year}

# courceList_Specialisation class attributes and methods
courceList_Specialisation_name: Property = Property(name="name", type=StringType)
courceList_Specialisation_startSemester: Property = Property(name="startSemester", type=IntegerType)
courceList_Specialisation.attributes={courceList_Specialisation_name, courceList_Specialisation_startSemester}

# courceList_Work class attributes and methods
courceList_Work_weight: Property = Property(name="weight", type=IntegerType)
courceList_Work.attributes={courceList_Work_weight}

# courceList_Exam class attributes and methods
courceList_Exam_form: Property = Property(name="form", type=StringType)
courceList_Exam_lenght: Property = Property(name="lenght", type=IntegerType)
courceList_Exam_date: Property = Property(name="date", type=DateType)
courceList_Exam_weight: Property = Property(name="weight", type=IntegerType)
courceList_Exam.attributes={courceList_Exam_weight, courceList_Exam_date, courceList_Exam_form, courceList_Exam_lenght}

# courceList_EvaluationForm class attributes and methods
courceList_EvaluationForm_evaluationType: Property = Property(name="evaluationType", type=StringType)
courceList_EvaluationForm.attributes={courceList_EvaluationForm_evaluationType}

# courceList_StudyCourceRelation class attributes and methods
courceList_StudyCourceRelation_status: Property = Property(name="status", type=StringType)
courceList_StudyCourceRelation_year: Property = Property(name="year", type=IntegerType)
courceList_StudyCourceRelation.attributes={courceList_StudyCourceRelation_status, courceList_StudyCourceRelation_year}

# Relationships
studyProgram0: BinaryAssociation = BinaryAssociation(
    name="studyProgram0",
    ends={
        Property(name="StudyGeneralization", type=courceList_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=courceList_StudyGeneralization, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
course1: BinaryAssociation = BinaryAssociation(
    name="course1",
    ends={
        Property(name="Cource", type=courceList_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department2", type=courceList_Cource, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
professor3: BinaryAssociation = BinaryAssociation(
    name="professor3",
    ends={
        Property(name="Professor", type=courceList_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department4", type=courceList_Professor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
corseSpecifications6: BinaryAssociation = BinaryAssociation(
    name="corseSpecifications6",
    ends={
        Property(name="CourceSpecification", type=courceList_Cource, multiplicity=Multiplicity(1, 1)),
        Property(name="cource", type=courceList_CourceSpecification, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
studyProgram7: BinaryAssociation = BinaryAssociation(
    name="studyProgram7",
    ends={
        Property(name="StudyProgram", type=courceList_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=courceList_StudyProgram, multiplicity=Multiplicity(1, 1))
    }
)
cource8: BinaryAssociation = BinaryAssociation(
    name="cource8",
    ends={
        Property(name="Specialisation", type=courceList_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram", type=courceList_Specialisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalization9: BinaryAssociation = BinaryAssociation(
    name="generalization9",
    ends={
        Property(name="StudyGeneralization11", type=courceList_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram10", type=courceList_StudyGeneralization, multiplicity=Multiplicity(0, 1))
    }
)
student12: BinaryAssociation = BinaryAssociation(
    name="student12",
    ends={
        Property(name="Student", type=courceList_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram13", type=courceList_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department5: BinaryAssociation = BinaryAssociation(
    name="department5",
    ends={
        Property(name="Department", type=courceList_Cource, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=courceList_Department, multiplicity=Multiplicity(0, 1))
    }
)
exam15: BinaryAssociation = BinaryAssociation(
    name="exam15",
    ends={
        Property(name="Exam", type=courceList_EvaluationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluationForm", type=courceList_Exam, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
work16: BinaryAssociation = BinaryAssociation(
    name="work16",
    ends={
        Property(name="Work", type=courceList_EvaluationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluationForm17", type=courceList_Work, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cource18: BinaryAssociation = BinaryAssociation(
    name="cource18",
    ends={
        Property(name="CourceSpecification20", type=courceList_EvaluationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluationForm19", type=courceList_CourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
evaluationForm14: BinaryAssociation = BinaryAssociation(
    name="evaluationForm14",
    ends={
        Property(name="EvaluationForm", type=courceList_Exam, multiplicity=Multiplicity(1, 1)),
        Property(name="exam", type=courceList_EvaluationForm, multiplicity=Multiplicity(0, 1))
    }
)
specialisation24: BinaryAssociation = BinaryAssociation(
    name="specialisation24",
    ends={
        Property(name="Specialisation26", type=courceList_StudyCourceRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="cource25", type=courceList_Specialisation, multiplicity=Multiplicity(0, 1))
    }
)
department27: BinaryAssociation = BinaryAssociation(
    name="department27",
    ends={
        Property(name="Department28", type=courceList_Professor, multiplicity=Multiplicity(1, 1)),
        Property(name="professor", type=courceList_Department, multiplicity=Multiplicity(0, 1))
    }
)
cource29: BinaryAssociation = BinaryAssociation(
    name="cource29",
    ends={
        Property(name="StudyCourceRelation", type=courceList_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="specialisation", type=courceList_StudyCourceRelation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
studyProgram30: BinaryAssociation = BinaryAssociation(
    name="studyProgram30",
    ends={
        Property(name="StudyProgram32", type=courceList_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="cource31", type=courceList_StudyProgram, multiplicity=Multiplicity(0, 1))
    }
)
evaluationForm21: BinaryAssociation = BinaryAssociation(
    name="evaluationForm21",
    ends={
        Property(name="EvaluationForm22", type=courceList_Work, multiplicity=Multiplicity(1, 1)),
        Property(name="work", type=courceList_EvaluationForm, multiplicity=Multiplicity(0, 1))
    }
)
cource23: BinaryAssociation = BinaryAssociation(
    name="cource23",
    ends={
        Property(name="courceList_CourceSpecification", type=courceList_StudyCourceRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="courceList_StudyCourceRelation", type=courceList_CourceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
cource39: BinaryAssociation = BinaryAssociation(
    name="cource39",
    ends={
        Property(name="Cource40", type=courceList_CourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="corseSpecifications", type=courceList_Cource, multiplicity=Multiplicity(1, 1))
    }
)
coordinator41: BinaryAssociation = BinaryAssociation(
    name="coordinator41",
    ends={
        Property(name="courceList_Professor", type=courceList_CourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="courceList_CourceSpecification42", type=courceList_Professor, multiplicity=Multiplicity(0, 1))
    }
)
evaluationForm43: BinaryAssociation = BinaryAssociation(
    name="evaluationForm43",
    ends={
        Property(name="EvaluationForm45", type=courceList_CourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="cource44", type=courceList_EvaluationForm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
furtherSpecialisation34: BinaryAssociation = BinaryAssociation(
    name="furtherSpecialisation34",
    ends={
        Property(name="Specialisation35", type=courceList_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="hostSpecialisation", type=courceList_Specialisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hostSpecialisation37: BinaryAssociation = BinaryAssociation(
    name="hostSpecialisation37",
    ends={
        Property(name="Specialisation38", type=courceList_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="furtherSpecialisation", type=courceList_Specialisation, multiplicity=Multiplicity(0, 1))
    }
)
studyProgram46: BinaryAssociation = BinaryAssociation(
    name="studyProgram46",
    ends={
        Property(name="StudyProgram47", type=courceList_StudyGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=courceList_StudyProgram, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
department48: BinaryAssociation = BinaryAssociation(
    name="department48",
    ends={
        Property(name="Department50", type=courceList_StudyGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram49", type=courceList_Department, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="courceList",
    types={courceList_Department, courceList_StudyGeneralization, courceList_Cource, courceList_Professor, courceList_CourceSpecification, courceList_Student, courceList_StudyProgram, courceList_Specialisation, courceList_Work, courceList_Exam, courceList_EvaluationForm, courceList_StudyCourceRelation, Semester, WorkForm, EducationLevel, Campus, EvaluationType},
    associations={studyProgram0, course1, professor3, corseSpecifications6, studyProgram7, cource8, generalization9, student12, department5, exam15, work16, cource18, evaluationForm14, specialisation24, department27, cource29, studyProgram30, evaluationForm21, cource23, cource39, coordinator41, evaluationForm43, furtherSpecialisation34, hostSpecialisation37, studyProgram46, department48},
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