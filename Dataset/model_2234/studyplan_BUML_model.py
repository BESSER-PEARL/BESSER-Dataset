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
SemesterType: Enumeration = Enumeration(
    name="SemesterType",
    literals={
            EnumerationLiteral(name="SPRING"),
			EnumerationLiteral(name="FALL")
    }
)

CourseStatus: Enumeration = Enumeration(
    name="CourseStatus",
    literals={
            EnumerationLiteral(name="MANDATORY"),
			EnumerationLiteral(name="ELECTIVE")
    }
)

# Classes
studyplan_FieldOfStudy = Class(name="studyplan::FieldOfStudy")
studyplan_Course = Class(name="studyplan::Course")
studyplan_Semester = Class(name="studyplan::Semester")
studyplan_StudyPlan = Class(name="studyplan::StudyPlan")
studyplan_Specialization = Class(name="studyplan::Specialization")
studyplan_CourseGroup = Class(name="studyplan::CourseGroup")

# studyplan_FieldOfStudy class attributes and methods
studyplan_FieldOfStudy_fieldName: Property = Property(name="fieldName", type=StringType)
studyplan_FieldOfStudy.attributes={studyplan_FieldOfStudy_fieldName}

# studyplan_Course class attributes and methods
studyplan_Course_courseName: Property = Property(name="courseName", type=StringType)
studyplan_Course_courseCode: Property = Property(name="courseCode", type=IntegerType)
studyplan_Course_credit: Property = Property(name="credit", type=FloatType)
studyplan_Course_status: Property = Property(name="status", type=StringType)
studyplan_Course.attributes={studyplan_Course_status, studyplan_Course_courseCode, studyplan_Course_courseName, studyplan_Course_credit}

# studyplan_Semester class attributes and methods
studyplan_Semester_year: Property = Property(name="year", type=IntegerType)
studyplan_Semester_semesterType: Property = Property(name="semesterType", type=StringType)
studyplan_Semester.attributes={studyplan_Semester_semesterType, studyplan_Semester_year}

# studyplan_StudyPlan class attributes and methods
studyplan_StudyPlan_planName: Property = Property(name="planName", type=StringType)
studyplan_StudyPlan.attributes={studyplan_StudyPlan_planName}

# studyplan_Specialization class attributes and methods
studyplan_Specialization_specName: Property = Property(name="specName", type=StringType)
studyplan_Specialization.attributes={studyplan_Specialization_specName}

# studyplan_CourseGroup class attributes and methods
studyplan_CourseGroup_group: Property = Property(name="group", type=StringType)
studyplan_CourseGroup_courseStatus: Property = Property(name="courseStatus", type=StringType)
studyplan_CourseGroup.attributes={studyplan_CourseGroup_group, studyplan_CourseGroup_courseStatus}

# Relationships
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="studyplan_FieldOfStudy", type=studyplan_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_StudyPlan", type=studyplan_FieldOfStudy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
courses1: BinaryAssociation = BinaryAssociation(
    name="courses1",
    ends={
        Property(name="studyplan_Course", type=studyplan_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_StudyPlan2", type=studyplan_Course, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
semester3: BinaryAssociation = BinaryAssociation(
    name="semester3",
    ends={
        Property(name="studyplan_Semester", type=studyplan_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_StudyPlan4", type=studyplan_Semester, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
courses5: BinaryAssociation = BinaryAssociation(
    name="courses5",
    ends={
        Property(name="studyplan_Course7", type=studyplan_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_Semester6", type=studyplan_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters9: BinaryAssociation = BinaryAssociation(
    name="semesters9",
    ends={
        Property(name="studyplan_Semester10", type=studyplan_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_Specialization", type=studyplan_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specialization12: BinaryAssociation = BinaryAssociation(
    name="specialization12",
    ends={
        Property(name="studyplan_Specialization13", type=studyplan_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_Specialization11", type=studyplan_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseGroup14: BinaryAssociation = BinaryAssociation(
    name="courseGroup14",
    ends={
        Property(name="studyplan_CourseGroup", type=studyplan_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_Specialization15", type=studyplan_CourseGroup, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
courseGroup8: BinaryAssociation = BinaryAssociation(
    name="courseGroup8",
    ends={
        Property(name="CourseGroup", type=studyplan_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=studyplan_CourseGroup, multiplicity=Multiplicity(0, 1))
    }
)
course25: BinaryAssociation = BinaryAssociation(
    name="course25",
    ends={
        Property(name="courseGroup", type=studyplan_Course, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Course", type=studyplan_CourseGroup, multiplicity=Multiplicity(1, 1))
    }
)
specialization16: BinaryAssociation = BinaryAssociation(
    name="specialization16",
    ends={
        Property(name="studyplan_Specialization18", type=studyplan_FieldOfStudy, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_FieldOfStudy17", type=studyplan_Specialization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
semesters19: BinaryAssociation = BinaryAssociation(
    name="semesters19",
    ends={
        Property(name="studyplan_Semester21", type=studyplan_FieldOfStudy, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_FieldOfStudy20", type=studyplan_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester22: BinaryAssociation = BinaryAssociation(
    name="semester22",
    ends={
        Property(name="studyplan_Semester24", type=studyplan_CourseGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_CourseGroup23", type=studyplan_Semester, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="studyplan",
    types={studyplan_FieldOfStudy, studyplan_Course, studyplan_Semester, studyplan_StudyPlan, studyplan_Specialization, studyplan_CourseGroup, SemesterType, CourseStatus},
    associations={program0, courses1, semester3, courses5, semesters9, specialization12, courseGroup14, courseGroup8, course25, specialization16, semesters19, semester22},
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