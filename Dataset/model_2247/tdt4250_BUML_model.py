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
StudyProgramName: Enumeration = Enumeration(
    name="StudyProgramName",
    literals={
            EnumerationLiteral(name="computer_science_5_years"),
			EnumerationLiteral(name="computer_science_2_years"),
			EnumerationLiteral(name="informatics")
    }
)

Semester: Enumeration = Enumeration(
    name="Semester",
    literals={
            EnumerationLiteral(name="spring"),
			EnumerationLiteral(name="autumn")
    }
)

# Classes
tdt4250_Specialisation = Class(name="tdt4250::Specialisation")
tdt4250_Course = Class(name="tdt4250::Course")
tdt4250_StudyProgram = Class(name="tdt4250::StudyProgram")
tdt4250_Student = Class(name="tdt4250::Student")
tdt4250_CourseGroup = Class(name="tdt4250::CourseGroup")

# tdt4250_Specialisation class attributes and methods
tdt4250_Specialisation_name: Property = Property(name="name", type=StringType)
tdt4250_Specialisation.attributes={tdt4250_Specialisation_name}

# tdt4250_Course class attributes and methods
tdt4250_Course_code: Property = Property(name="code", type=StringType)
tdt4250_Course_name: Property = Property(name="name", type=StringType)
tdt4250_Course_study_points: Property = Property(name="study_points", type=FloatType)
tdt4250_Course_level: Property = Property(name="level", type=StringType)
tdt4250_Course_semester: Property = Property(name="semester", type=StringType)
tdt4250_Course.attributes={tdt4250_Course_study_points, tdt4250_Course_semester, tdt4250_Course_name, tdt4250_Course_code, tdt4250_Course_level}

# tdt4250_StudyProgram class attributes and methods
tdt4250_StudyProgram_number_of_semesters: Property = Property(name="number_of_semesters", type=IntegerType)
tdt4250_StudyProgram_name: Property = Property(name="name", type=StringType)
tdt4250_StudyProgram.attributes={tdt4250_StudyProgram_name, tdt4250_StudyProgram_number_of_semesters}

# tdt4250_Student class attributes and methods
tdt4250_Student_studentID: Property = Property(name="studentID", type=IntegerType)
tdt4250_Student_current_semester: Property = Property(name="current_semester", type=IntegerType)
tdt4250_Student.attributes={tdt4250_Student_studentID, tdt4250_Student_current_semester}

# tdt4250_CourseGroup class attributes and methods

# Relationships
specialisations1: BinaryAssociation = BinaryAssociation(
    name="specialisations1",
    ends={
        Property(name="tdt4250_Specialisation", type=tdt4250_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_StudyProgram2", type=tdt4250_Specialisation, multiplicity=Multiplicity(0, 10), is_composite=True)
    }
)
obligatory_courses3: BinaryAssociation = BinaryAssociation(
    name="obligatory_courses3",
    ends={
        Property(name="tdt4250_Course", type=tdt4250_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_StudyProgram4", type=tdt4250_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students0: BinaryAssociation = BinaryAssociation(
    name="students0",
    ends={
        Property(name="tdt4250_Student", type=tdt4250_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_StudyProgram", type=tdt4250_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mandatory_courses8: BinaryAssociation = BinaryAssociation(
    name="mandatory_courses8",
    ends={
        Property(name="tdt4250_Course9", type=tdt4250_CourseGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_CourseGroup", type=tdt4250_Course, multiplicity=Multiplicity(0, 1))
    }
)
elective_courses10: BinaryAssociation = BinaryAssociation(
    name="elective_courses10",
    ends={
        Property(name="tdt4250_Course12", type=tdt4250_CourseGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_CourseGroup11", type=tdt4250_Course, multiplicity=Multiplicity(0, 1))
    }
)
specialisation13: BinaryAssociation = BinaryAssociation(
    name="specialisation13",
    ends={
        Property(name="tdt4250_Specialisation15", type=tdt4250_CourseGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_CourseGroup14", type=tdt4250_Specialisation, multiplicity=Multiplicity(0, 1))
    }
)
students16: BinaryAssociation = BinaryAssociation(
    name="students16",
    ends={
        Property(name="tdt4250_Student18", type=tdt4250_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Specialisation17", type=tdt4250_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
further_specialisation20: BinaryAssociation = BinaryAssociation(
    name="further_specialisation20",
    ends={
        Property(name="tdt4250_Specialisation21", type=tdt4250_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Specialisation19", type=tdt4250_Specialisation, multiplicity=Multiplicity(0, 1))
    }
)
courses5: BinaryAssociation = BinaryAssociation(
    name="courses5",
    ends={
        Property(name="tdt4250_Course7", type=tdt4250_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Student6", type=tdt4250_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course_group22: BinaryAssociation = BinaryAssociation(
    name="course_group22",
    ends={
        Property(name="tdt4250_CourseGroup24", type=tdt4250_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Specialisation23", type=tdt4250_CourseGroup, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tdt4250",
    types={tdt4250_Specialisation, tdt4250_Course, tdt4250_StudyProgram, tdt4250_Student, tdt4250_CourseGroup, StudyProgramName, Semester},
    associations={specialisations1, obligatory_courses3, students0, mandatory_courses8, elective_courses10, specialisation13, students16, further_specialisation20, courses5, course_group22},
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