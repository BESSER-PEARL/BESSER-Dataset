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
Season: Enumeration = Enumeration(
    name="Season",
    literals={
            EnumerationLiteral(name="fall"),
			EnumerationLiteral(name="spring")
    }
)

CourseStatus: Enumeration = Enumeration(
    name="CourseStatus",
    literals={
            EnumerationLiteral(name="mandatory"),
			EnumerationLiteral(name="elective")
    }
)

Grade: Enumeration = Enumeration(
    name="Grade",
    literals={
            EnumerationLiteral(name="E"),
			EnumerationLiteral(name="F"),
			EnumerationLiteral(name="A"),
			EnumerationLiteral(name="B"),
			EnumerationLiteral(name="C"),
			EnumerationLiteral(name="D")
    }
)

# Classes
studyProgramStructure_Course = Class(name="studyProgramStructure::Course")
studyProgramStructure_Program = Class(name="studyProgramStructure::Program")
studyProgramStructure_Specialization = Class(name="studyProgramStructure::Specialization")
studyProgramStructure_Semester = Class(name="studyProgramStructure::Semester")
studyProgramStructure_CourseGroup = Class(name="studyProgramStructure::CourseGroup")
studyProgramStructure_University = Class(name="studyProgramStructure::University")
studyProgramStructure_CourseAllocation = Class(name="studyProgramStructure::CourseAllocation")
studyProgramStructure_Student = Class(name="studyProgramStructure::Student")
studyProgramStructure_StudyPlan = Class(name="studyProgramStructure::StudyPlan")

# studyProgramStructure_Course class attributes and methods
studyProgramStructure_Course_name: Property = Property(name="name", type=StringType)
studyProgramStructure_Course_code: Property = Property(name="code", type=StringType)
studyProgramStructure_Course_credits: Property = Property(name="credits", type=FloatType)
studyProgramStructure_Course_level: Property = Property(name="level", type=IntegerType)
studyProgramStructure_Course.attributes={studyProgramStructure_Course_code, studyProgramStructure_Course_credits, studyProgramStructure_Course_name, studyProgramStructure_Course_level}

# studyProgramStructure_Program class attributes and methods
studyProgramStructure_Program_numOfSemestersForBaseSpecialization: Property = Property(name="numOfSemestersForBaseSpecialization", type=IntegerType)
studyProgramStructure_Program_numOfYears: Property = Property(name="numOfYears", type=IntegerType)
studyProgramStructure_Program_name: Property = Property(name="name", type=StringType)
studyProgramStructure_Program_code: Property = Property(name="code", type=StringType)
studyProgramStructure_Program.attributes={studyProgramStructure_Program_code, studyProgramStructure_Program_numOfSemestersForBaseSpecialization, studyProgramStructure_Program_numOfYears, studyProgramStructure_Program_name}

# studyProgramStructure_Specialization class attributes and methods
studyProgramStructure_Specialization_name: Property = Property(name="name", type=StringType)
studyProgramStructure_Specialization_numOfSemesters: Property = Property(name="numOfSemesters", type=IntegerType)
studyProgramStructure_Specialization.attributes={studyProgramStructure_Specialization_name, studyProgramStructure_Specialization_numOfSemesters}

# studyProgramStructure_Semester class attributes and methods
studyProgramStructure_Semester_year: Property = Property(name="year", type=IntegerType)
studyProgramStructure_Semester_season: Property = Property(name="season", type=StringType)
studyProgramStructure_Semester.attributes={studyProgramStructure_Semester_season, studyProgramStructure_Semester_year}

# studyProgramStructure_CourseGroup class attributes and methods
studyProgramStructure_CourseGroup_name: Property = Property(name="name", type=StringType)
studyProgramStructure_CourseGroup_status: Property = Property(name="status", type=StringType)
studyProgramStructure_CourseGroup.attributes={studyProgramStructure_CourseGroup_status, studyProgramStructure_CourseGroup_name}

# studyProgramStructure_University class attributes and methods
studyProgramStructure_University_name: Property = Property(name="name", type=StringType)
studyProgramStructure_University.attributes={studyProgramStructure_University_name}

# studyProgramStructure_CourseAllocation class attributes and methods
studyProgramStructure_CourseAllocation_grade: Property = Property(name="grade", type=StringType)
studyProgramStructure_CourseAllocation.attributes={studyProgramStructure_CourseAllocation_grade}

# studyProgramStructure_Student class attributes and methods
studyProgramStructure_Student_name: Property = Property(name="name", type=StringType)
studyProgramStructure_Student.attributes={studyProgramStructure_Student_name}

# studyProgramStructure_StudyPlan class attributes and methods

# Relationships
specializations0: BinaryAssociation = BinaryAssociation(
    name="specializations0",
    ends={
        Property(name="Specialization", type=studyProgramStructure_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="program", type=studyProgramStructure_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters1: BinaryAssociation = BinaryAssociation(
    name="semesters1",
    ends={
        Property(name="Semester", type=studyProgramStructure_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="program2", type=studyProgramStructure_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
furtherSpecializations4: BinaryAssociation = BinaryAssociation(
    name="furtherSpecializations4",
    ends={
        Property(name="Specialization5", type=studyProgramStructure_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="baseSpecialization", type=studyProgramStructure_Specialization, multiplicity=Multiplicity(0, 9999))
    }
)
baseSpecialization7: BinaryAssociation = BinaryAssociation(
    name="baseSpecialization7",
    ends={
        Property(name="Specialization8", type=studyProgramStructure_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="furtherSpecializations", type=studyProgramStructure_Specialization, multiplicity=Multiplicity(0, 1))
    }
)
semesters9: BinaryAssociation = BinaryAssociation(
    name="semesters9",
    ends={
        Property(name="Semester10", type=studyProgramStructure_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization", type=studyProgramStructure_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseGroups12: BinaryAssociation = BinaryAssociation(
    name="courseGroups12",
    ends={
        Property(name="CourseGroup", type=studyProgramStructure_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=studyProgramStructure_CourseGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program13: BinaryAssociation = BinaryAssociation(
    name="program13",
    ends={
        Property(name="Program14", type=studyProgramStructure_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semesters", type=studyProgramStructure_Program, multiplicity=Multiplicity(0, 1))
    }
)
program11: BinaryAssociation = BinaryAssociation(
    name="program11",
    ends={
        Property(name="Program", type=studyProgramStructure_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specializations", type=studyProgramStructure_Program, multiplicity=Multiplicity(1, 1))
    }
)
semester18: BinaryAssociation = BinaryAssociation(
    name="semester18",
    ends={
        Property(name="Semester19", type=studyProgramStructure_CourseGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="courseGroups", type=studyProgramStructure_Semester, multiplicity=Multiplicity(1, 1))
    }
)
courses20: BinaryAssociation = BinaryAssociation(
    name="courses20",
    ends={
        Property(name="studyProgramStructure_Course", type=studyProgramStructure_CourseGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramStructure_CourseGroup", type=studyProgramStructure_Course, multiplicity=Multiplicity(0, 9999))
    }
)
programs21: BinaryAssociation = BinaryAssociation(
    name="programs21",
    ends={
        Property(name="studyProgramStructure_Program", type=studyProgramStructure_University, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramStructure_University", type=studyProgramStructure_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses22: BinaryAssociation = BinaryAssociation(
    name="courses22",
    ends={
        Property(name="studyProgramStructure_Course24", type=studyProgramStructure_University, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramStructure_University23", type=studyProgramStructure_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specialization15: BinaryAssociation = BinaryAssociation(
    name="specialization15",
    ends={
        Property(name="Specialization17", type=studyProgramStructure_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semesters16", type=studyProgramStructure_Specialization, multiplicity=Multiplicity(0, 1))
    }
)
program28: BinaryAssociation = BinaryAssociation(
    name="program28",
    ends={
        Property(name="studyProgramStructure_Program30", type=studyProgramStructure_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramStructure_Student29", type=studyProgramStructure_Program, multiplicity=Multiplicity(0, 1))
    }
)
specializations31: BinaryAssociation = BinaryAssociation(
    name="specializations31",
    ends={
        Property(name="studyProgramStructure_Specialization", type=studyProgramStructure_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramStructure_Student32", type=studyProgramStructure_Specialization, multiplicity=Multiplicity(0, 9999))
    }
)
semesters33: BinaryAssociation = BinaryAssociation(
    name="semesters33",
    ends={
        Property(name="studyProgramStructure_Semester", type=studyProgramStructure_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramStructure_StudyPlan", type=studyProgramStructure_Semester, multiplicity=Multiplicity(0, 9999))
    }
)
courseAllocation34: BinaryAssociation = BinaryAssociation(
    name="courseAllocation34",
    ends={
        Property(name="studyProgramStructure_CourseAllocation", type=studyProgramStructure_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramStructure_StudyPlan35", type=studyProgramStructure_CourseAllocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
student36: BinaryAssociation = BinaryAssociation(
    name="student36",
    ends={
        Property(name="Student", type=studyProgramStructure_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan", type=studyProgramStructure_Student, multiplicity=Multiplicity(0, 1))
    }
)
course37: BinaryAssociation = BinaryAssociation(
    name="course37",
    ends={
        Property(name="studyProgramStructure_Course39", type=studyProgramStructure_CourseAllocation, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramStructure_CourseAllocation38", type=studyProgramStructure_Course, multiplicity=Multiplicity(0, 1))
    }
)
students25: BinaryAssociation = BinaryAssociation(
    name="students25",
    ends={
        Property(name="studyProgramStructure_Student", type=studyProgramStructure_University, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramStructure_University26", type=studyProgramStructure_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyPlan27: BinaryAssociation = BinaryAssociation(
    name="studyPlan27",
    ends={
        Property(name="StudyPlan", type=studyProgramStructure_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=studyProgramStructure_StudyPlan, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="studyProgramStructure",
    types={studyProgramStructure_Course, studyProgramStructure_Program, studyProgramStructure_Specialization, studyProgramStructure_Semester, studyProgramStructure_CourseGroup, studyProgramStructure_University, studyProgramStructure_CourseAllocation, studyProgramStructure_Student, studyProgramStructure_StudyPlan, Season, CourseStatus, Grade},
    associations={specializations0, semesters1, furtherSpecializations4, baseSpecialization7, semesters9, courseGroups12, program13, program11, semester18, courses20, programs21, courses22, specialization15, program28, specializations31, semesters33, courseAllocation34, student36, course37, students25, studyPlan27},
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