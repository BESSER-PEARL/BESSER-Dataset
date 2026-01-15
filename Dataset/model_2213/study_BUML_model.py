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
GradeEnum: Enumeration = Enumeration(
    name="GradeEnum",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="A"),
			EnumerationLiteral(name="B"),
			EnumerationLiteral(name="C"),
			EnumerationLiteral(name="D"),
			EnumerationLiteral(name="E"),
			EnumerationLiteral(name="F")
    }
)

# Classes
study_Course = Class(name="study::Course")
study_Student = Class(name="study::Student")
study_Specialization = Class(name="study::Specialization")
study_University = Class(name="study::University")
study_StudyProgramme = Class(name="study::StudyProgramme")
study_Semester = Class(name="study::Semester")
study_ElectiveCourseList = Class(name="study::ElectiveCourseList")
study_IndividualStudyPlan = Class(name="study::IndividualStudyPlan")
study_CourseRelationship = Class(name="study::CourseRelationship")

# study_Course class attributes and methods
study_Course_code: Property = Property(name="code", type=StringType)
study_Course_name: Property = Property(name="name", type=StringType)
study_Course_credits: Property = Property(name="credits", type=FloatType)
study_Course_level: Property = Property(name="level", type=IntegerType)
study_Course.attributes={study_Course_code, study_Course_level, study_Course_credits, study_Course_name}

# study_Student class attributes and methods
study_Student_username: Property = Property(name="username", type=StringType)
study_Student_name: Property = Property(name="name", type=StringType)
study_Student.attributes={study_Student_name, study_Student_username}

# study_Specialization class attributes and methods
study_Specialization_numYears: Property = Property(name="numYears", type=IntegerType)
study_Specialization_name: Property = Property(name="name", type=StringType)
study_Specialization.attributes={study_Specialization_name, study_Specialization_numYears}

# study_University class attributes and methods
study_University_name: Property = Property(name="name", type=StringType)
study_University.attributes={study_University_name}

# study_StudyProgramme class attributes and methods
study_StudyProgramme_code: Property = Property(name="code", type=StringType)
study_StudyProgramme_name: Property = Property(name="name", type=StringType)
study_StudyProgramme_numYears: Property = Property(name="numYears", type=IntegerType)
study_StudyProgramme.attributes={study_StudyProgramme_name, study_StudyProgramme_code, study_StudyProgramme_numYears}

# study_Semester class attributes and methods
study_Semester_ordinal: Property = Property(name="ordinal", type=IntegerType)
study_Semester.attributes={study_Semester_ordinal}

# study_ElectiveCourseList class attributes and methods

# study_IndividualStudyPlan class attributes and methods

# study_CourseRelationship class attributes and methods
study_CourseRelationship_grade: Property = Property(name="grade", type=StringType)
study_CourseRelationship_numExamAttempts: Property = Property(name="numExamAttempts", type=IntegerType)
study_CourseRelationship.attributes={study_CourseRelationship_grade, study_CourseRelationship_numExamAttempts}

# Relationships
courses1: BinaryAssociation = BinaryAssociation(
    name="courses1",
    ends={
        Property(name="Course", type=study_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university2", type=study_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students3: BinaryAssociation = BinaryAssociation(
    name="students3",
    ends={
        Property(name="Student", type=study_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university4", type=study_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
university5: BinaryAssociation = BinaryAssociation(
    name="university5",
    ends={
        Property(name="University", type=study_StudyProgramme, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgrammes", type=study_University, multiplicity=Multiplicity(1, 1))
    }
)
allSpecializations6: BinaryAssociation = BinaryAssociation(
    name="allSpecializations6",
    ends={
        Property(name="Specialization", type=study_StudyProgramme, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgramme", type=study_Specialization, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
baseSpecializations7: BinaryAssociation = BinaryAssociation(
    name="baseSpecializations7",
    ends={
        Property(name="study_Specialization", type=study_StudyProgramme, multiplicity=Multiplicity(1, 1)),
        Property(name="study_StudyProgramme", type=study_Specialization, multiplicity=Multiplicity(1, 9999))
    }
)
studyProgrammes0: BinaryAssociation = BinaryAssociation(
    name="studyProgrammes0",
    ends={
        Property(name="StudyProgramme", type=study_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university", type=study_StudyProgramme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters10: BinaryAssociation = BinaryAssociation(
    name="semesters10",
    ends={
        Property(name="Semester", type=study_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization", type=study_Semester, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
furtherSpecializations12: BinaryAssociation = BinaryAssociation(
    name="furtherSpecializations12",
    ends={
        Property(name="study_Specialization13", type=study_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Specialization11", type=study_Specialization, multiplicity=Multiplicity(0, 9999))
    }
)
specialization14: BinaryAssociation = BinaryAssociation(
    name="specialization14",
    ends={
        Property(name="Specialization15", type=study_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semesters", type=study_Specialization, multiplicity=Multiplicity(1, 1))
    }
)
mandatoryCourses16: BinaryAssociation = BinaryAssociation(
    name="mandatoryCourses16",
    ends={
        Property(name="study_Course", type=study_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Semester", type=study_Course, multiplicity=Multiplicity(0, 9999))
    }
)
electiveCourses17: BinaryAssociation = BinaryAssociation(
    name="electiveCourses17",
    ends={
        Property(name="ElectiveCourseList", type=study_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=study_ElectiveCourseList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
studyProgramme8: BinaryAssociation = BinaryAssociation(
    name="studyProgramme8",
    ends={
        Property(name="StudyProgramme9", type=study_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="allSpecializations", type=study_StudyProgramme, multiplicity=Multiplicity(1, 1))
    }
)
semester20: BinaryAssociation = BinaryAssociation(
    name="semester20",
    ends={
        Property(name="Semester21", type=study_ElectiveCourseList, multiplicity=Multiplicity(1, 1)),
        Property(name="electiveCourses", type=study_Semester, multiplicity=Multiplicity(1, 1))
    }
)
courses22: BinaryAssociation = BinaryAssociation(
    name="courses22",
    ends={
        Property(name="study_Course23", type=study_ElectiveCourseList, multiplicity=Multiplicity(1, 1)),
        Property(name="study_ElectiveCourseList", type=study_Course, multiplicity=Multiplicity(1, 9999))
    }
)
university24: BinaryAssociation = BinaryAssociation(
    name="university24",
    ends={
        Property(name="University25", type=study_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=study_University, multiplicity=Multiplicity(1, 1))
    }
)
studyPlan26: BinaryAssociation = BinaryAssociation(
    name="studyPlan26",
    ends={
        Property(name="IndividualStudyPlan", type=study_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=study_IndividualStudyPlan, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
student27: BinaryAssociation = BinaryAssociation(
    name="student27",
    ends={
        Property(name="Student28", type=study_IndividualStudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan", type=study_Student, multiplicity=Multiplicity(1, 1))
    }
)
university18: BinaryAssociation = BinaryAssociation(
    name="university18",
    ends={
        Property(name="University19", type=study_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=study_University, multiplicity=Multiplicity(1, 1))
    }
)
currentSemester29: BinaryAssociation = BinaryAssociation(
    name="currentSemester29",
    ends={
        Property(name="study_Semester30", type=study_IndividualStudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="study_IndividualStudyPlan", type=study_Semester, multiplicity=Multiplicity(1, 1))
    }
)
courses31: BinaryAssociation = BinaryAssociation(
    name="courses31",
    ends={
        Property(name="CourseRelationship", type=study_IndividualStudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan32", type=study_CourseRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyPlan33: BinaryAssociation = BinaryAssociation(
    name="studyPlan33",
    ends={
        Property(name="IndividualStudyPlan35", type=study_CourseRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="courses34", type=study_IndividualStudyPlan, multiplicity=Multiplicity(1, 1))
    }
)
course36: BinaryAssociation = BinaryAssociation(
    name="course36",
    ends={
        Property(name="study_Course37", type=study_CourseRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="study_CourseRelationship", type=study_Course, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="study",
    types={study_Course, study_Student, study_Specialization, study_University, study_StudyProgramme, study_Semester, study_ElectiveCourseList, study_IndividualStudyPlan, study_CourseRelationship, GradeEnum},
    associations={courses1, students3, university5, allSpecializations6, baseSpecializations7, studyProgrammes0, semesters10, furtherSpecializations12, specialization14, mandatoryCourses16, electiveCourses17, studyProgramme8, semester20, courses22, university24, studyPlan26, student27, university18, currentSemester29, courses31, studyPlan33, course36},
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