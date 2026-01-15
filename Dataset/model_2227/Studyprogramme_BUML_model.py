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
ProgrammeType: Enumeration = Enumeration(
    name="ProgrammeType",
    literals={
            EnumerationLiteral(name="Bachelors"),
			EnumerationLiteral(name="Masters"),
			EnumerationLiteral(name="IntegratedMaster")
    }
)

ProgrammeCode: Enumeration = Enumeration(
    name="ProgrammeCode",
    literals={
            EnumerationLiteral(name="MIDT"),
			EnumerationLiteral(name="BIT"),
			EnumerationLiteral(name="MIT"),
			EnumerationLiteral(name="MTIOT"),
			EnumerationLiteral(name="MTPROD"),
			EnumerationLiteral(name="MTDT")
    }
)

# Classes
studyprogramme_Programme = Class(name="studyprogramme::Programme")
SemesterContainer = Class(name="SemesterContainer")
studyprogramme_Course = Class(name="studyprogramme::Course")
studyprogramme_Specialization = Class(name="studyprogramme::Specialization")
studyprogramme_SemesterContainer = Class(name="studyprogramme::SemesterContainer")
studyprogramme_ElectiveCourseList = Class(name="studyprogramme::ElectiveCourseList")
studyprogramme_Semester = Class(name="studyprogramme::Semester")
studyprogramme_CourseSlot = Class(name="studyprogramme::CourseSlot")
studyprogramme_ElectiveCourseSlot = Class(name="studyprogramme::ElectiveCourseSlot")
studyprogramme_University = Class(name="studyprogramme::University")
CourseSlot = Class(name="CourseSlot")
studyprogramme_CompulsoryCourseSlot = Class(name="studyprogramme::CompulsoryCourseSlot")

# studyprogramme_Programme class attributes and methods
studyprogramme_Programme_name: Property = Property(name="name", type=StringType)
studyprogramme_Programme_programmeCode: Property = Property(name="programmeCode", type=StringType)
studyprogramme_Programme_numberOfYears: Property = Property(name="numberOfYears", type=IntegerType)
studyprogramme_Programme_programmeType: Property = Property(name="programmeType", type=StringType)
studyprogramme_Programme.attributes={studyprogramme_Programme_programmeType, studyprogramme_Programme_programmeCode, studyprogramme_Programme_name, studyprogramme_Programme_numberOfYears}

# SemesterContainer class attributes and methods

# studyprogramme_Course class attributes and methods
studyprogramme_Course_level: Property = Property(name="level", type=IntegerType)
studyprogramme_Course_displayedName: Property = Property(name="displayedName", type=StringType)
studyprogramme_Course_name: Property = Property(name="name", type=StringType)
studyprogramme_Course_courseCode: Property = Property(name="courseCode", type=StringType)
studyprogramme_Course_credits: Property = Property(name="credits", type=FloatType)
studyprogramme_Course.attributes={studyprogramme_Course_name, studyprogramme_Course_courseCode, studyprogramme_Course_level, studyprogramme_Course_displayedName, studyprogramme_Course_credits}

# studyprogramme_Specialization class attributes and methods
studyprogramme_Specialization_selectionSemester: Property = Property(name="selectionSemester", type=IntegerType)
studyprogramme_Specialization_name: Property = Property(name="name", type=StringType)
studyprogramme_Specialization.attributes={studyprogramme_Specialization_selectionSemester, studyprogramme_Specialization_name}

# studyprogramme_SemesterContainer class attributes and methods

# studyprogramme_ElectiveCourseList class attributes and methods
studyprogramme_ElectiveCourseList_name: Property = Property(name="name", type=StringType)
studyprogramme_ElectiveCourseList.attributes={studyprogramme_ElectiveCourseList_name}

# studyprogramme_Semester class attributes and methods
studyprogramme_Semester_semesterNumber: Property = Property(name="semesterNumber", type=IntegerType)
studyprogramme_Semester.attributes={studyprogramme_Semester_semesterNumber}

# studyprogramme_CourseSlot class attributes and methods

# studyprogramme_ElectiveCourseSlot class attributes and methods

# studyprogramme_University class attributes and methods
studyprogramme_University_name: Property = Property(name="name", type=StringType)
studyprogramme_University.attributes={studyprogramme_University_name}

# CourseSlot class attributes and methods

# studyprogramme_CompulsoryCourseSlot class attributes and methods

# Relationships
programme1: BinaryAssociation = BinaryAssociation(
    name="programme1",
    ends={
        Property(name="Programme", type=studyprogramme_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specializations", type=studyprogramme_Programme, multiplicity=Multiplicity(0, 1))
    }
)
subSpecialisations3: BinaryAssociation = BinaryAssociation(
    name="subSpecialisations3",
    ends={
        Property(name="Specialization4", type=studyprogramme_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="parrentSpecialisation", type=studyprogramme_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializations0: BinaryAssociation = BinaryAssociation(
    name="specializations0",
    ends={
        Property(name="Specialization", type=studyprogramme_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programme", type=studyprogramme_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course9: BinaryAssociation = BinaryAssociation(
    name="course9",
    ends={
        Property(name="studyprogramme_Course", type=studyprogramme_CourseSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogramme_CourseSlot10", type=studyprogramme_Course, multiplicity=Multiplicity(1, 1))
    }
)
semesters11: BinaryAssociation = BinaryAssociation(
    name="semesters11",
    ends={
        Property(name="studyprogramme_Semester12", type=studyprogramme_SemesterContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogramme_SemesterContainer", type=studyprogramme_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parrentSpecialisation6: BinaryAssociation = BinaryAssociation(
    name="parrentSpecialisation6",
    ends={
        Property(name="Specialization7", type=studyprogramme_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="subSpecialisations", type=studyprogramme_Specialization, multiplicity=Multiplicity(0, 1))
    }
)
slots8: BinaryAssociation = BinaryAssociation(
    name="slots8",
    ends={
        Property(name="studyprogramme_CourseSlot", type=studyprogramme_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogramme_Semester", type=studyprogramme_CourseSlot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses17: BinaryAssociation = BinaryAssociation(
    name="courses17",
    ends={
        Property(name="studyprogramme_Course19", type=studyprogramme_University, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogramme_University18", type=studyprogramme_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Semesters20: BinaryAssociation = BinaryAssociation(
    name="Semesters20",
    ends={
        Property(name="studyprogramme_Semester22", type=studyprogramme_University, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogramme_University21", type=studyprogramme_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specialisations23: BinaryAssociation = BinaryAssociation(
    name="specialisations23",
    ends={
        Property(name="studyprogramme_Specialization", type=studyprogramme_University, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogramme_University24", type=studyprogramme_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableCourses13: BinaryAssociation = BinaryAssociation(
    name="availableCourses13",
    ends={
        Property(name="studyprogramme_Course14", type=studyprogramme_ElectiveCourseList, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogramme_ElectiveCourseList", type=studyprogramme_Course, multiplicity=Multiplicity(0, 9999))
    }
)
electiveCourseSlot15: BinaryAssociation = BinaryAssociation(
    name="electiveCourseSlot15",
    ends={
        Property(name="ElectiveCourseSlot", type=studyprogramme_ElectiveCourseList, multiplicity=Multiplicity(1, 1)),
        Property(name="electiveCourseList", type=studyprogramme_ElectiveCourseSlot, multiplicity=Multiplicity(0, 1))
    }
)
programmes16: BinaryAssociation = BinaryAssociation(
    name="programmes16",
    ends={
        Property(name="studyprogramme_Programme", type=studyprogramme_University, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogramme_University", type=studyprogramme_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
electiveCourseList25: BinaryAssociation = BinaryAssociation(
    name="electiveCourseList25",
    ends={
        Property(name="ElectiveCourseList", type=studyprogramme_ElectiveCourseSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="electiveCourseSlot", type=studyprogramme_ElectiveCourseList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignedCourse26: BinaryAssociation = BinaryAssociation(
    name="assignedCourse26",
    ends={
        Property(name="studyprogramme_Course27", type=studyprogramme_ElectiveCourseSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogramme_ElectiveCourseSlot", type=studyprogramme_Course, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_studyprogramme_Programme_SemesterContainer = Generalization(general=SemesterContainer, specific=studyprogramme_Programme)
gen_studyprogramme_Specialization_SemesterContainer = Generalization(general=SemesterContainer, specific=studyprogramme_Specialization)
gen_studyprogramme_ElectiveCourseSlot_CourseSlot = Generalization(general=CourseSlot, specific=studyprogramme_ElectiveCourseSlot)
gen_studyprogramme_CompulsoryCourseSlot_CourseSlot = Generalization(general=CourseSlot, specific=studyprogramme_CompulsoryCourseSlot)

# Domain Model
domain_model = DomainModel(
    name="studyprogramme",
    types={studyprogramme_Programme, SemesterContainer, studyprogramme_Course, studyprogramme_Specialization, studyprogramme_SemesterContainer, studyprogramme_ElectiveCourseList, studyprogramme_Semester, studyprogramme_CourseSlot, studyprogramme_ElectiveCourseSlot, studyprogramme_University, CourseSlot, studyprogramme_CompulsoryCourseSlot, ProgrammeType, ProgrammeCode},
    associations={programme1, subSpecialisations3, specializations0, course9, semesters11, parrentSpecialisation6, slots8, courses17, Semesters20, specialisations23, availableCourses13, electiveCourseSlot15, programmes16, electiveCourseList25, assignedCourse26},
    generalizations={gen_studyprogramme_Programme_SemesterContainer, gen_studyprogramme_Specialization_SemesterContainer, gen_studyprogramme_ElectiveCourseSlot_CourseSlot, gen_studyprogramme_CompulsoryCourseSlot_CourseSlot},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)