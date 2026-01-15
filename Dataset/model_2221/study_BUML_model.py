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
grades: Enumeration = Enumeration(
    name="grades",
    literals={
            EnumerationLiteral(name="B"),
			EnumerationLiteral(name="C"),
			EnumerationLiteral(name="D"),
			EnumerationLiteral(name="E"),
			EnumerationLiteral(name="F"),
			EnumerationLiteral(name="A")
    }
)

# Classes
study_Department = Class(name="study::Department")
study_Course = Class(name="study::Course")
study_Program = Class(name="study::Program")
study_Student = Class(name="study::Student")
study_Specialisation = Class(name="study::Specialisation")
study_Semester = Class(name="study::Semester")
study_StudyPlan = Class(name="study::StudyPlan")
study_courseAllocation = Class(name="study::courseAllocation")

# study_Department class attributes and methods
study_Department_name: Property = Property(name="name", type=StringType)
study_Department_code: Property = Property(name="code", type=StringType)
study_Department.attributes={study_Department_name, study_Department_code}

# study_Course class attributes and methods
study_Course_season: Property = Property(name="season", type=StringType)
study_Course_year: Property = Property(name="year", type=IntegerType)
study_Course_name: Property = Property(name="name", type=StringType)
study_Course_code: Property = Property(name="code", type=StringType)
study_Course_credits: Property = Property(name="credits", type=FloatType)
study_Course.attributes={study_Course_season, study_Course_credits, study_Course_year, study_Course_name, study_Course_code}

# study_Program class attributes and methods
study_Program_name: Property = Property(name="name", type=StringType)
study_Program_code: Property = Property(name="code", type=StringType)
study_Program_numYears: Property = Property(name="numYears", type=IntegerType)
study_Program.attributes={study_Program_name, study_Program_numYears, study_Program_code}

# study_Student class attributes and methods
study_Student_name: Property = Property(name="name", type=StringType)
study_Student.attributes={study_Student_name}

# study_Specialisation class attributes and methods
study_Specialisation_name: Property = Property(name="name", type=StringType)
study_Specialisation_requirement: Property = Property(name="requirement", type=StringType)
study_Specialisation.attributes={study_Specialisation_name, study_Specialisation_requirement}

# study_Semester class attributes and methods
study_Semester_season: Property = Property(name="season", type=StringType)
study_Semester_year: Property = Property(name="year", type=IntegerType)
study_Semester.attributes={study_Semester_year, study_Semester_season}

# study_StudyPlan class attributes and methods
study_StudyPlan_m_chooseCourse: Method = Method(name="chooseCourse", parameters={Parameter(name='course'), Parameter(name='studyplan')})
study_StudyPlan.methods={study_StudyPlan_m_chooseCourse}

# study_courseAllocation class attributes and methods
study_courseAllocation_grade: Property = Property(name="grade", type=StringType)
study_courseAllocation.attributes={study_courseAllocation_grade}

# Relationships
courses0: BinaryAssociation = BinaryAssociation(
    name="courses0",
    ends={
        Property(name="Course", type=study_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=study_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programs1: BinaryAssociation = BinaryAssociation(
    name="programs1",
    ends={
        Property(name="Program", type=study_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department2", type=study_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students3: BinaryAssociation = BinaryAssociation(
    name="students3",
    ends={
        Property(name="Student", type=study_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department4", type=study_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specialisations5: BinaryAssociation = BinaryAssociation(
    name="specialisations5",
    ends={
        Property(name="Specialisation", type=study_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department6", type=study_Specialisation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
semesters7: BinaryAssociation = BinaryAssociation(
    name="semesters7",
    ends={
        Property(name="Semester", type=study_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department8", type=study_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department9: BinaryAssociation = BinaryAssociation(
    name="department9",
    ends={
        Property(name="Department", type=study_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="programs", type=study_Department, multiplicity=Multiplicity(1, 1))
    }
)
specialisations10: BinaryAssociation = BinaryAssociation(
    name="specialisations10",
    ends={
        Property(name="Specialisation11", type=study_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="program", type=study_Specialisation, multiplicity=Multiplicity(1, 9999))
    }
)
department12: BinaryAssociation = BinaryAssociation(
    name="department12",
    ends={
        Property(name="Department13", type=study_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=study_Department, multiplicity=Multiplicity(1, 1))
    }
)
studyPlan14: BinaryAssociation = BinaryAssociation(
    name="studyPlan14",
    ends={
        Property(name="StudyPlan", type=study_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=study_StudyPlan, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
specialisations15: BinaryAssociation = BinaryAssociation(
    name="specialisations15",
    ends={
        Property(name="study_Specialisation", type=study_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Student", type=study_Specialisation, multiplicity=Multiplicity(0, 2))
    }
)
department16: BinaryAssociation = BinaryAssociation(
    name="department16",
    ends={
        Property(name="courses", type=study_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="Department17", type=study_Course, multiplicity=Multiplicity(1, 1))
    }
)
program18: BinaryAssociation = BinaryAssociation(
    name="program18",
    ends={
        Property(name="Program19", type=study_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="specialisations", type=study_Program, multiplicity=Multiplicity(1, 1))
    }
)
students20: BinaryAssociation = BinaryAssociation(
    name="students20",
    ends={
        Property(name="study_Student22", type=study_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Specialisation21", type=study_Student, multiplicity=Multiplicity(1, 1))
    }
)
semesters23: BinaryAssociation = BinaryAssociation(
    name="semesters23",
    ends={
        Property(name="Semester24", type=study_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="specialisation", type=study_Semester, multiplicity=Multiplicity(2, 9999))
    }
)
department25: BinaryAssociation = BinaryAssociation(
    name="department25",
    ends={
        Property(name="Department27", type=study_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="specialisations26", type=study_Department, multiplicity=Multiplicity(1, 1))
    }
)
department31: BinaryAssociation = BinaryAssociation(
    name="department31",
    ends={
        Property(name="Department33", type=study_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semesters32", type=study_Department, multiplicity=Multiplicity(0, 1))
    }
)
semester34: BinaryAssociation = BinaryAssociation(
    name="semester34",
    ends={
        Property(name="study_Semester35", type=study_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="study_StudyPlan", type=study_Semester, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
courses36: BinaryAssociation = BinaryAssociation(
    name="courses36",
    ends={
        Property(name="study_courseAllocation", type=study_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="study_StudyPlan37", type=study_courseAllocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
student38: BinaryAssociation = BinaryAssociation(
    name="student38",
    ends={
        Property(name="Student39", type=study_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan", type=study_Student, multiplicity=Multiplicity(1, 1))
    }
)
specialisation28: BinaryAssociation = BinaryAssociation(
    name="specialisation28",
    ends={
        Property(name="Specialisation29", type=study_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semesters", type=study_Specialisation, multiplicity=Multiplicity(1, 1))
    }
)
courses30: BinaryAssociation = BinaryAssociation(
    name="courses30",
    ends={
        Property(name="study_Course", type=study_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Semester", type=study_Course, multiplicity=Multiplicity(1, 9999))
    }
)
studyPlan40: BinaryAssociation = BinaryAssociation(
    name="studyPlan40",
    ends={
        Property(name="study_StudyPlan42", type=study_courseAllocation, multiplicity=Multiplicity(1, 1)),
        Property(name="study_courseAllocation41", type=study_StudyPlan, multiplicity=Multiplicity(0, 1))
    }
)
course43: BinaryAssociation = BinaryAssociation(
    name="course43",
    ends={
        Property(name="study_Course45", type=study_courseAllocation, multiplicity=Multiplicity(1, 1)),
        Property(name="study_courseAllocation44", type=study_Course, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="study",
    types={study_Department, study_Course, study_Program, study_Student, study_Specialisation, study_Semester, study_StudyPlan, study_courseAllocation, grades},
    associations={courses0, programs1, students3, specialisations5, semesters7, department9, specialisations10, department12, studyPlan14, specialisations15, department16, program18, students20, semesters23, department25, department31, semester34, courses36, student38, specialisation28, courses30, studyPlan40, course43},
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