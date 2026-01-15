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
            EnumerationLiteral(name="Fall"),
			EnumerationLiteral(name="Spring")
    }
)

CourseType: Enumeration = Enumeration(
    name="CourseType",
    literals={
            EnumerationLiteral(name="Obligatory"),
			EnumerationLiteral(name="Elective")
    }
)

# Classes
studyprogram_University = Class(name="studyprogram::University")
studyprogram_Department = Class(name="studyprogram::Department")
studyprogram_Course = Class(name="studyprogram::Course")
studyprogram_Program = Class(name="studyprogram::Program")
studyprogram_StudyPlan = Class(name="studyprogram::StudyPlan")
studyprogram_ElectiveCourses = Class(name="studyprogram::ElectiveCourses")
studyprogram_ObligatoryCourses = Class(name="studyprogram::ObligatoryCourses")
studyprogram_Year = Class(name="studyprogram::Year")
studyprogram_Semester = Class(name="studyprogram::Semester")
studyprogram_SemesterCourse = Class(name="studyprogram::SemesterCourse")

# studyprogram_University class attributes and methods
studyprogram_University_name: Property = Property(name="name", type=StringType)
studyprogram_University.attributes={studyprogram_University_name}

# studyprogram_Department class attributes and methods
studyprogram_Department_name: Property = Property(name="name", type=StringType)
studyprogram_Department.attributes={studyprogram_Department_name}

# studyprogram_Course class attributes and methods
studyprogram_Course_semester: Property = Property(name="semester", type=StringType)
studyprogram_Course_name: Property = Property(name="name", type=StringType)
studyprogram_Course_credits: Property = Property(name="credits", type=StringType)
studyprogram_Course_code: Property = Property(name="code", type=StringType)
studyprogram_Course.attributes={studyprogram_Course_semester, studyprogram_Course_credits, studyprogram_Course_name, studyprogram_Course_code}

# studyprogram_Program class attributes and methods
studyprogram_Program_name: Property = Property(name="name", type=StringType)
studyprogram_Program.attributes={studyprogram_Program_name}

# studyprogram_StudyPlan class attributes and methods
studyprogram_StudyPlan_name: Property = Property(name="name", type=StringType)
studyprogram_StudyPlan.attributes={studyprogram_StudyPlan_name}

# studyprogram_ElectiveCourses class attributes and methods

# studyprogram_ObligatoryCourses class attributes and methods

# studyprogram_Year class attributes and methods
studyprogram_Year_value: Property = Property(name="value", type=IntegerType)
studyprogram_Year.attributes={studyprogram_Year_value}

# studyprogram_Semester class attributes and methods
studyprogram_Semester_type: Property = Property(name="type", type=StringType)
studyprogram_Semester.attributes={studyprogram_Semester_type}

# studyprogram_SemesterCourse class attributes and methods
studyprogram_SemesterCourse_type: Property = Property(name="type", type=StringType)
studyprogram_SemesterCourse_name: Property = Property(name="name", type=StringType)
studyprogram_SemesterCourse.attributes={studyprogram_SemesterCourse_type, studyprogram_SemesterCourse_name}

# Relationships
programs3: BinaryAssociation = BinaryAssociation(
    name="programs3",
    ends={
        Property(name="department4", type=studyprogram_Program, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Program", type=studyprogram_Department, multiplicity=Multiplicity(1, 1))
    }
)
departments0: BinaryAssociation = BinaryAssociation(
    name="departments0",
    ends={
        Property(name="Department", type=studyprogram_University, multiplicity=Multiplicity(1, 1)),
        Property(name="school", type=studyprogram_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
school1: BinaryAssociation = BinaryAssociation(
    name="school1",
    ends={
        Property(name="University", type=studyprogram_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="departments", type=studyprogram_University, multiplicity=Multiplicity(0, 1))
    }
)
courses2: BinaryAssociation = BinaryAssociation(
    name="courses2",
    ends={
        Property(name="Course", type=studyprogram_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=studyprogram_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department5: BinaryAssociation = BinaryAssociation(
    name="department5",
    ends={
        Property(name="Department6", type=studyprogram_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="programs", type=studyprogram_Department, multiplicity=Multiplicity(0, 1))
    }
)
studyPlans7: BinaryAssociation = BinaryAssociation(
    name="studyPlans7",
    ends={
        Property(name="StudyPlan", type=studyprogram_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="program", type=studyprogram_StudyPlan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
electiveCourses8: BinaryAssociation = BinaryAssociation(
    name="electiveCourses8",
    ends={
        Property(name="ElectiveCourses", type=studyprogram_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="program9", type=studyprogram_ElectiveCourses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
obligatoryCourses10: BinaryAssociation = BinaryAssociation(
    name="obligatoryCourses10",
    ends={
        Property(name="ObligatoryCourses", type=studyprogram_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="program11", type=studyprogram_ObligatoryCourses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
years12: BinaryAssociation = BinaryAssociation(
    name="years12",
    ends={
        Property(name="Year", type=studyprogram_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan", type=studyprogram_Year, multiplicity=Multiplicity(0, 5), is_composite=True)
    }
)
program13: BinaryAssociation = BinaryAssociation(
    name="program13",
    ends={
        Property(name="Program14", type=studyprogram_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlans", type=studyprogram_Program, multiplicity=Multiplicity(0, 1))
    }
)
studyPlan16: BinaryAssociation = BinaryAssociation(
    name="studyPlan16",
    ends={
        Property(name="StudyPlan17", type=studyprogram_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="specialisations", type=studyprogram_StudyPlan, multiplicity=Multiplicity(0, 1))
    }
)
specialisations19: BinaryAssociation = BinaryAssociation(
    name="specialisations19",
    ends={
        Property(name="StudyPlan21", type=studyprogram_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan20", type=studyprogram_StudyPlan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters22: BinaryAssociation = BinaryAssociation(
    name="semesters22",
    ends={
        Property(name="Semester", type=studyprogram_Year, multiplicity=Multiplicity(1, 1)),
        Property(name="year", type=studyprogram_Semester, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
studyPlan23: BinaryAssociation = BinaryAssociation(
    name="studyPlan23",
    ends={
        Property(name="StudyPlan24", type=studyprogram_Year, multiplicity=Multiplicity(1, 1)),
        Property(name="years", type=studyprogram_StudyPlan, multiplicity=Multiplicity(0, 1))
    }
)
year25: BinaryAssociation = BinaryAssociation(
    name="year25",
    ends={
        Property(name="Year26", type=studyprogram_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semesters", type=studyprogram_Year, multiplicity=Multiplicity(0, 1))
    }
)
semesterCourses27: BinaryAssociation = BinaryAssociation(
    name="semesterCourses27",
    ends={
        Property(name="SemesterCourse", type=studyprogram_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=studyprogram_SemesterCourse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester28: BinaryAssociation = BinaryAssociation(
    name="semester28",
    ends={
        Property(name="Semester29", type=studyprogram_SemesterCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="semesterCourses", type=studyprogram_Semester, multiplicity=Multiplicity(0, 1))
    }
)
course30: BinaryAssociation = BinaryAssociation(
    name="course30",
    ends={
        Property(name="studyprogram_Course", type=studyprogram_SemesterCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_SemesterCourse", type=studyprogram_Course, multiplicity=Multiplicity(0, 1))
    }
)
department31: BinaryAssociation = BinaryAssociation(
    name="department31",
    ends={
        Property(name="Department32", type=studyprogram_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=studyprogram_Department, multiplicity=Multiplicity(0, 1))
    }
)
program33: BinaryAssociation = BinaryAssociation(
    name="program33",
    ends={
        Property(name="Program34", type=studyprogram_ElectiveCourses, multiplicity=Multiplicity(1, 1)),
        Property(name="electiveCourses", type=studyprogram_Program, multiplicity=Multiplicity(0, 1))
    }
)
courses35: BinaryAssociation = BinaryAssociation(
    name="courses35",
    ends={
        Property(name="studyprogram_Course36", type=studyprogram_ElectiveCourses, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_ElectiveCourses", type=studyprogram_Course, multiplicity=Multiplicity(0, 9999))
    }
)
program37: BinaryAssociation = BinaryAssociation(
    name="program37",
    ends={
        Property(name="Program38", type=studyprogram_ObligatoryCourses, multiplicity=Multiplicity(1, 1)),
        Property(name="obligatoryCourses", type=studyprogram_Program, multiplicity=Multiplicity(0, 1))
    }
)
courses39: BinaryAssociation = BinaryAssociation(
    name="courses39",
    ends={
        Property(name="studyprogram_Course40", type=studyprogram_ObligatoryCourses, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_ObligatoryCourses", type=studyprogram_Course, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="studyprogram",
    types={studyprogram_University, studyprogram_Department, studyprogram_Course, studyprogram_Program, studyprogram_StudyPlan, studyprogram_ElectiveCourses, studyprogram_ObligatoryCourses, studyprogram_Year, studyprogram_Semester, studyprogram_SemesterCourse, SemesterType, CourseType},
    associations={programs3, departments0, school1, courses2, department5, studyPlans7, electiveCourses8, obligatoryCourses10, years12, program13, studyPlan16, specialisations19, semesters22, studyPlan23, year25, semesterCourses27, semester28, course30, department31, program33, courses35, program37, courses39},
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