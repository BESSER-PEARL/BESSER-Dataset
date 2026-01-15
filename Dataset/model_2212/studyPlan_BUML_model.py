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
SeasonEnum: Enumeration = Enumeration(
    name="SeasonEnum",
    literals={
            EnumerationLiteral(name="Vår"),
			EnumerationLiteral(name="Høst")
    }
)

# Classes
studyPlan_Student = Class(name="studyPlan::Student")
studyPlan_StudyProgramme = Class(name="studyPlan::StudyProgramme")
studyPlan_Course = Class(name="studyPlan::Course")
studyPlan_University = Class(name="studyPlan::University")
Semester = Class(name="Semester")
studyPlan_SemesterProgramme = Class(name="studyPlan::SemesterProgramme")
studyPlan_Specialization = Class(name="studyPlan::Specialization")
studyPlan_StudyPlan = Class(name="studyPlan::StudyPlan")
studyPlan_SemesterPlan = Class(name="studyPlan::SemesterPlan")
studyPlan_Semester = Class(name="studyPlan::Semester")

# studyPlan_Student class attributes and methods
studyPlan_Student_name: Property = Property(name="name", type=StringType)
studyPlan_Student_username: Property = Property(name="username", type=StringType)
studyPlan_Student.attributes={studyPlan_Student_username, studyPlan_Student_name}

# studyPlan_StudyProgramme class attributes and methods
studyPlan_StudyProgramme_codename: Property = Property(name="codename", type=StringType)
studyPlan_StudyProgramme_name: Property = Property(name="name", type=StringType)
studyPlan_StudyProgramme_lengthInYears: Property = Property(name="lengthInYears", type=IntegerType)
studyPlan_StudyProgramme.attributes={studyPlan_StudyProgramme_name, studyPlan_StudyProgramme_lengthInYears, studyPlan_StudyProgramme_codename}

# studyPlan_Course class attributes and methods
studyPlan_Course_credits: Property = Property(name="credits", type=FloatType)
studyPlan_Course_level: Property = Property(name="level", type=IntegerType)
studyPlan_Course_codename: Property = Property(name="codename", type=StringType)
studyPlan_Course_name: Property = Property(name="name", type=StringType)
studyPlan_Course.attributes={studyPlan_Course_level, studyPlan_Course_credits, studyPlan_Course_name, studyPlan_Course_codename}

# studyPlan_University class attributes and methods
studyPlan_University_name: Property = Property(name="name", type=StringType)
studyPlan_University.attributes={studyPlan_University_name}

# Semester class attributes and methods

# studyPlan_SemesterProgramme class attributes and methods

# studyPlan_Specialization class attributes and methods
studyPlan_Specialization_name: Property = Property(name="name", type=StringType)
studyPlan_Specialization_year: Property = Property(name="year", type=IntegerType)
studyPlan_Specialization.attributes={studyPlan_Specialization_name, studyPlan_Specialization_year}

# studyPlan_StudyPlan class attributes and methods

# studyPlan_SemesterPlan class attributes and methods

# studyPlan_Semester class attributes and methods
studyPlan_Semester_season: Property = Property(name="season", type=StringType)
studyPlan_Semester_codename: Property = Property(name="codename", type=StringType)
studyPlan_Semester_year: Property = Property(name="year", type=IntegerType)
studyPlan_Semester.attributes={studyPlan_Semester_season, studyPlan_Semester_codename, studyPlan_Semester_year}

# Relationships
university0: BinaryAssociation = BinaryAssociation(
    name="university0",
    ends={
        Property(name="courses", type=studyPlan_University, multiplicity=Multiplicity(1, 1)),
        Property(name="University", type=studyPlan_Course, multiplicity=Multiplicity(1, 1))
    }
)
students1: BinaryAssociation = BinaryAssociation(
    name="students1",
    ends={
        Property(name="Student", type=studyPlan_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university", type=studyPlan_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyProgrammes2: BinaryAssociation = BinaryAssociation(
    name="studyProgrammes2",
    ends={
        Property(name="StudyProgramme", type=studyPlan_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university3", type=studyPlan_StudyProgramme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses4: BinaryAssociation = BinaryAssociation(
    name="courses4",
    ends={
        Property(name="Course", type=studyPlan_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university5", type=studyPlan_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyPlan9: BinaryAssociation = BinaryAssociation(
    name="studyPlan9",
    ends={
        Property(name="StudyPlan", type=studyPlan_SemesterPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="semesterPlans", type=studyPlan_StudyPlan, multiplicity=Multiplicity(1, 1))
    }
)
selectedCourses10: BinaryAssociation = BinaryAssociation(
    name="selectedCourses10",
    ends={
        Property(name="studyPlan_Course", type=studyPlan_SemesterPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan_SemesterPlan", type=studyPlan_Course, multiplicity=Multiplicity(0, 9999))
    }
)
student6: BinaryAssociation = BinaryAssociation(
    name="student6",
    ends={
        Property(name="Student7", type=studyPlan_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan", type=studyPlan_Student, multiplicity=Multiplicity(1, 1))
    }
)
semesterPlans8: BinaryAssociation = BinaryAssociation(
    name="semesterPlans8",
    ends={
        Property(name="SemesterPlan", type=studyPlan_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan", type=studyPlan_SemesterPlan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyplan19: BinaryAssociation = BinaryAssociation(
    name="studyplan19",
    ends={
        Property(name="StudyPlan20", type=studyPlan_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=studyPlan_StudyPlan, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
university21: BinaryAssociation = BinaryAssociation(
    name="university21",
    ends={
        Property(name="University22", type=studyPlan_StudyProgramme, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgrammes", type=studyPlan_University, multiplicity=Multiplicity(1, 1))
    }
)
specialization11: BinaryAssociation = BinaryAssociation(
    name="specialization11",
    ends={
        Property(name="Specialization", type=studyPlan_SemesterProgramme, multiplicity=Multiplicity(1, 1)),
        Property(name="semesters", type=studyPlan_Specialization, multiplicity=Multiplicity(1, 1))
    }
)
mandatoryCourses12: BinaryAssociation = BinaryAssociation(
    name="mandatoryCourses12",
    ends={
        Property(name="studyPlan_Course13", type=studyPlan_SemesterProgramme, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan_SemesterProgramme", type=studyPlan_Course, multiplicity=Multiplicity(0, 9999))
    }
)
electiveCourses14: BinaryAssociation = BinaryAssociation(
    name="electiveCourses14",
    ends={
        Property(name="studyPlan_Course16", type=studyPlan_SemesterProgramme, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan_SemesterProgramme15", type=studyPlan_Course, multiplicity=Multiplicity(0, 9999))
    }
)
university17: BinaryAssociation = BinaryAssociation(
    name="university17",
    ends={
        Property(name="University18", type=studyPlan_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=studyPlan_University, multiplicity=Multiplicity(1, 1))
    }
)
studyProgramme25: BinaryAssociation = BinaryAssociation(
    name="studyProgramme25",
    ends={
        Property(name="StudyProgramme26", type=studyPlan_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specializations", type=studyPlan_StudyProgramme, multiplicity=Multiplicity(0, 1))
    }
)
specializations23: BinaryAssociation = BinaryAssociation(
    name="specializations23",
    ends={
        Property(name="Specialization24", type=studyPlan_StudyProgramme, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramme", type=studyPlan_Specialization, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
continuations28: BinaryAssociation = BinaryAssociation(
    name="continuations28",
    ends={
        Property(name="studyPlan_Specialization", type=studyPlan_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan_Specialization27", type=studyPlan_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters29: BinaryAssociation = BinaryAssociation(
    name="semesters29",
    ends={
        Property(name="SemesterProgramme", type=studyPlan_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization", type=studyPlan_SemesterProgramme, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_studyPlan_SemesterPlan_Semester = Generalization(general=Semester, specific=studyPlan_SemesterPlan)
gen_studyPlan_SemesterProgramme_Semester = Generalization(general=Semester, specific=studyPlan_SemesterProgramme)

# Domain Model
domain_model = DomainModel(
    name="studyPlan",
    types={studyPlan_Student, studyPlan_StudyProgramme, studyPlan_Course, studyPlan_University, Semester, studyPlan_SemesterProgramme, studyPlan_Specialization, studyPlan_StudyPlan, studyPlan_SemesterPlan, studyPlan_Semester, SeasonEnum},
    associations={university0, students1, studyProgrammes2, courses4, studyPlan9, selectedCourses10, student6, semesterPlans8, studyplan19, university21, specialization11, mandatoryCourses12, electiveCourses14, university17, studyProgramme25, specializations23, continuations28, semesters29},
    generalizations={gen_studyPlan_SemesterPlan_Semester, gen_studyPlan_SemesterProgramme_Semester},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)