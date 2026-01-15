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
SemesterCode: Enumeration = Enumeration(
    name="SemesterCode",
    literals={
            EnumerationLiteral(name="Spring"),
			EnumerationLiteral(name="Autumn")
    }
)

# Classes
studies_University = Class(name="studies::University")
studies_Course = Class(name="studies::Course")
studies_StudyInstance = Class(name="studies::StudyInstance")
studies_Study = Class(name="studies::Study")
studies_CourseInstance = Class(name="studies::CourseInstance")
studies_StudyYear = Class(name="studies::StudyYear")
studies_Semester = Class(name="studies::Semester")
studies_StudyCourse = Class(name="studies::StudyCourse")

# studies_University class attributes and methods
studies_University_name: Property = Property(name="name", type=StringType)
studies_University.attributes={studies_University_name}

# studies_Course class attributes and methods
studies_Course_name: Property = Property(name="name", type=StringType)
studies_Course_code: Property = Property(name="code", type=StringType)
studies_Course_studyPoints: Property = Property(name="studyPoints", type=FloatType)
studies_Course.attributes={studies_Course_name, studies_Course_code, studies_Course_studyPoints}

# studies_StudyInstance class attributes and methods
studies_StudyInstance_year: Property = Property(name="year", type=IntegerType)
studies_StudyInstance.attributes={studies_StudyInstance_year}

# studies_Study class attributes and methods
studies_Study_name: Property = Property(name="name", type=StringType)
studies_Study_code: Property = Property(name="code", type=StringType)
studies_Study.attributes={studies_Study_code, studies_Study_name}

# studies_CourseInstance class attributes and methods
studies_CourseInstance_year: Property = Property(name="year", type=IntegerType)
studies_CourseInstance_semester: Property = Property(name="semester", type=StringType)
studies_CourseInstance_instanceName: Property = Property(name="instanceName", type=StringType)
studies_CourseInstance.attributes={studies_CourseInstance_instanceName, studies_CourseInstance_year, studies_CourseInstance_semester}

# studies_StudyYear class attributes and methods
studies_StudyYear_programName: Property = Property(name="programName", type=StringType)
studies_StudyYear.attributes={studies_StudyYear_programName}

# studies_Semester class attributes and methods
studies_Semester_studyYearSemester: Property = Property(name="studyYearSemester", type=StringType)
studies_Semester.attributes={studies_Semester_studyYearSemester}

# studies_StudyCourse class attributes and methods
studies_StudyCourse_mandatory: Property = Property(name="mandatory", type=BooleanType)
studies_StudyCourse.attributes={studies_StudyCourse_mandatory}

# Relationships
courses0: BinaryAssociation = BinaryAssociation(
    name="courses0",
    ends={
        Property(name="studies_Course", type=studies_University, multiplicity=Multiplicity(1, 1)),
        Property(name="studies_University", type=studies_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyInstances5: BinaryAssociation = BinaryAssociation(
    name="studyInstances5",
    ends={
        Property(name="StudyInstance", type=studies_Study, multiplicity=Multiplicity(1, 1)),
        Property(name="study", type=studies_StudyInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studies1: BinaryAssociation = BinaryAssociation(
    name="studies1",
    ends={
        Property(name="studies_Study", type=studies_University, multiplicity=Multiplicity(1, 1)),
        Property(name="studies_University2", type=studies_Study, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseInstances3: BinaryAssociation = BinaryAssociation(
    name="courseInstances3",
    ends={
        Property(name="CourseInstance", type=studies_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=studies_CourseInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course4: BinaryAssociation = BinaryAssociation(
    name="course4",
    ends={
        Property(name="Course", type=studies_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courseInstances", type=studies_Course, multiplicity=Multiplicity(1, 1))
    }
)
study6: BinaryAssociation = BinaryAssociation(
    name="study6",
    ends={
        Property(name="Study", type=studies_StudyInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="studyInstances", type=studies_Study, multiplicity=Multiplicity(1, 1))
    }
)
startYear7: BinaryAssociation = BinaryAssociation(
    name="startYear7",
    ends={
        Property(name="studies_StudyYear", type=studies_StudyInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="studies_StudyInstance", type=studies_StudyYear, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
springSemester11: BinaryAssociation = BinaryAssociation(
    name="springSemester11",
    ends={
        Property(name="studies_Semester", type=studies_StudyYear, multiplicity=Multiplicity(1, 1)),
        Property(name="studies_StudyYear12", type=studies_Semester, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nextYear9: BinaryAssociation = BinaryAssociation(
    name="nextYear9",
    ends={
        Property(name="studies_StudyYear10", type=studies_StudyYear, multiplicity=Multiplicity(1, 1)),
        Property(name="studies_StudyYear8", type=studies_StudyYear, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseInstance16: BinaryAssociation = BinaryAssociation(
    name="courseInstance16",
    ends={
        Property(name="studies_StudyCourse", type=studies_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="studies_CourseInstance", type=studies_StudyCourse, multiplicity=Multiplicity(1, 1))
    }
)
autumnSemester13: BinaryAssociation = BinaryAssociation(
    name="autumnSemester13",
    ends={
        Property(name="studies_Semester15", type=studies_StudyYear, multiplicity=Multiplicity(1, 1)),
        Property(name="studies_StudyYear14", type=studies_Semester, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
courses17: BinaryAssociation = BinaryAssociation(
    name="courses17",
    ends={
        Property(name="studies_CourseInstance19", type=studies_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="studies_Semester18", type=studies_CourseInstance, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="studies",
    types={studies_University, studies_Course, studies_StudyInstance, studies_Study, studies_CourseInstance, studies_StudyYear, studies_Semester, studies_StudyCourse, SemesterCode},
    associations={courses0, studyInstances5, studies1, courseInstances3, course4, study6, startYear7, springSemester11, nextYear9, courseInstance16, autumnSemester13, courses17},
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