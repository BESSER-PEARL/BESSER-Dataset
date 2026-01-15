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
            EnumerationLiteral(name="Bachelor"),
			EnumerationLiteral(name="Master"),
			EnumerationLiteral(name="IntegrertMaster"),
			EnumerationLiteral(name="Årsstudie")
    }
)

Seasons: Enumeration = Enumeration(
    name="Seasons",
    literals={
            EnumerationLiteral(name="Fall"),
			EnumerationLiteral(name="Spring")
    }
)

Credits: Enumeration = Enumeration(
    name="Credits",
    literals={
            EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Full"),
			EnumerationLiteral(name="Minor"),
			EnumerationLiteral(name="Basic")
    }
)

# Classes
universityStudies_Course = Class(name="universityStudies::Course")
universityStudies_Programme = Class(name="universityStudies::Programme")
universityStudies_Semester = Class(name="universityStudies::Semester")
universityStudies_Department = Class(name="universityStudies::Department")
universityStudies_Specialization = Class(name="universityStudies::Specialization")
universityStudies_MandatoryCourseSlot = Class(name="universityStudies::MandatoryCourseSlot")
CourseSlot = Class(name="CourseSlot")
universityStudies_CourseSlot = Class(name="universityStudies::CourseSlot", is_abstract=True)
universityStudies_ElectiveCourseSlot = Class(name="universityStudies::ElectiveCourseSlot")

# universityStudies_Course class attributes and methods
universityStudies_Course_name: Property = Property(name="name", type=StringType)
universityStudies_Course_code: Property = Property(name="code", type=StringType)
universityStudies_Course_credits: Property = Property(name="credits", type=StringType)
universityStudies_Course_level: Property = Property(name="level", type=IntegerType)
universityStudies_Course.attributes={universityStudies_Course_level, universityStudies_Course_credits, universityStudies_Course_name, universityStudies_Course_code}

# universityStudies_Programme class attributes and methods
universityStudies_Programme_programmeType: Property = Property(name="programmeType", type=StringType)
universityStudies_Programme_numberOfSemesters: Property = Property(name="numberOfSemesters", type=IntegerType)
universityStudies_Programme_name: Property = Property(name="name", type=StringType)
universityStudies_Programme.attributes={universityStudies_Programme_programmeType, universityStudies_Programme_name, universityStudies_Programme_numberOfSemesters}

# universityStudies_Semester class attributes and methods
universityStudies_Semester_season: Property = Property(name="season", type=StringType)
universityStudies_Semester_semesterNumber: Property = Property(name="semesterNumber", type=IntegerType)
universityStudies_Semester_name: Property = Property(name="name", type=StringType)
universityStudies_Semester.attributes={universityStudies_Semester_season, universityStudies_Semester_semesterNumber, universityStudies_Semester_name}

# universityStudies_Department class attributes and methods

# universityStudies_Specialization class attributes and methods
universityStudies_Specialization_name: Property = Property(name="name", type=StringType)
universityStudies_Specialization.attributes={universityStudies_Specialization_name}

# universityStudies_MandatoryCourseSlot class attributes and methods

# CourseSlot class attributes and methods

# universityStudies_CourseSlot class attributes and methods

# universityStudies_ElectiveCourseSlot class attributes and methods

# Relationships
programmes0: BinaryAssociation = BinaryAssociation(
    name="programmes0",
    ends={
        Property(name="universityStudies_Programme", type=universityStudies_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="universityStudies_Course", type=universityStudies_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters3: BinaryAssociation = BinaryAssociation(
    name="semesters3",
    ends={
        Property(name="universityStudies_Semester", type=universityStudies_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="universityStudies_Programme4", type=universityStudies_Semester, multiplicity=Multiplicity(0, 10), is_composite=True)
    }
)
Department5: BinaryAssociation = BinaryAssociation(
    name="Department5",
    ends={
        Property(name="Department", type=universityStudies_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="Programmes", type=universityStudies_Department, multiplicity=Multiplicity(0, 1))
    }
)
furtherSpecializations7: BinaryAssociation = BinaryAssociation(
    name="furtherSpecializations7",
    ends={
        Property(name="universityStudies_Specialization8", type=universityStudies_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="universityStudies_Specialization6", type=universityStudies_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters9: BinaryAssociation = BinaryAssociation(
    name="semesters9",
    ends={
        Property(name="universityStudies_Semester11", type=universityStudies_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="universityStudies_Specialization10", type=universityStudies_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializations1: BinaryAssociation = BinaryAssociation(
    name="specializations1",
    ends={
        Property(name="universityStudies_Specialization", type=universityStudies_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="universityStudies_Programme2", type=universityStudies_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Courses14: BinaryAssociation = BinaryAssociation(
    name="Courses14",
    ends={
        Property(name="universityStudies_Course15", type=universityStudies_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="universityStudies_Department", type=universityStudies_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Programmes16: BinaryAssociation = BinaryAssociation(
    name="Programmes16",
    ends={
        Property(name="Programme", type=universityStudies_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="Department17", type=universityStudies_Programme, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
course18: BinaryAssociation = BinaryAssociation(
    name="course18",
    ends={
        Property(name="universityStudies_Course20", type=universityStudies_CourseSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="universityStudies_CourseSlot19", type=universityStudies_Course, multiplicity=Multiplicity(0, 1))
    }
)
courseSlots12: BinaryAssociation = BinaryAssociation(
    name="courseSlots12",
    ends={
        Property(name="universityStudies_CourseSlot", type=universityStudies_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="universityStudies_Semester13", type=universityStudies_CourseSlot, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
optionalCourses21: BinaryAssociation = BinaryAssociation(
    name="optionalCourses21",
    ends={
        Property(name="universityStudies_Course22", type=universityStudies_ElectiveCourseSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="universityStudies_ElectiveCourseSlot", type=universityStudies_Course, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_universityStudies_MandatoryCourseSlot_CourseSlot = Generalization(general=CourseSlot, specific=universityStudies_MandatoryCourseSlot)
gen_universityStudies_ElectiveCourseSlot_CourseSlot = Generalization(general=CourseSlot, specific=universityStudies_ElectiveCourseSlot)

# Domain Model
domain_model = DomainModel(
    name="universityStudies",
    types={universityStudies_Course, universityStudies_Programme, universityStudies_Semester, universityStudies_Department, universityStudies_Specialization, universityStudies_MandatoryCourseSlot, CourseSlot, universityStudies_CourseSlot, universityStudies_ElectiveCourseSlot, ProgrammeType, Seasons, Credits},
    associations={programmes0, semesters3, Department5, furtherSpecializations7, semesters9, specializations1, Courses14, Programmes16, course18, courseSlots12, optionalCourses21},
    generalizations={gen_universityStudies_MandatoryCourseSlot_CourseSlot, gen_universityStudies_ElectiveCourseSlot_CourseSlot},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)