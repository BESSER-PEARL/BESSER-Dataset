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

# Classes
schoolIncqDerived_Course = Class(name="schoolIncqDerived::Course")
schoolIncqDerived_Teacher = Class(name="schoolIncqDerived::Teacher")
schoolIncqDerived_SchoolClass = Class(name="schoolIncqDerived::SchoolClass")
schoolIncqDerived_Year = Class(name="schoolIncqDerived::Year")
schoolIncqDerived_School = Class(name="schoolIncqDerived::School")
schoolIncqDerived_Student = Class(name="schoolIncqDerived::Student")
schoolIncqDerived_SpecialisationCourse = Class(name="schoolIncqDerived::SpecialisationCourse")
Course = Class(name="Course")

# schoolIncqDerived_Course class attributes and methods
schoolIncqDerived_Course_subject: Property = Property(name="subject", type=StringType)
schoolIncqDerived_Course_weight: Property = Property(name="weight", type=IntegerType)
schoolIncqDerived_Course.attributes={schoolIncqDerived_Course_subject, schoolIncqDerived_Course_weight}

# schoolIncqDerived_Teacher class attributes and methods
schoolIncqDerived_Teacher_name: Property = Property(name="name", type=StringType)
schoolIncqDerived_Teacher.attributes={schoolIncqDerived_Teacher_name}

# schoolIncqDerived_SchoolClass class attributes and methods
schoolIncqDerived_SchoolClass_code: Property = Property(name="code", type=StringType)
schoolIncqDerived_SchoolClass.attributes={schoolIncqDerived_SchoolClass_code}

# schoolIncqDerived_Year class attributes and methods
schoolIncqDerived_Year_startingDate: Property = Property(name="startingDate", type=IntegerType)
schoolIncqDerived_Year.attributes={schoolIncqDerived_Year_startingDate}

# schoolIncqDerived_School class attributes and methods
schoolIncqDerived_School_name: Property = Property(name="name", type=StringType)
schoolIncqDerived_School_address: Property = Property(name="address", type=StringType)
schoolIncqDerived_School_currentYear: Property = Property(name="currentYear", type=IntegerType)
schoolIncqDerived_School_numberOfTeachers: Property = Property(name="numberOfTeachers", type=IntegerType)
schoolIncqDerived_School.attributes={schoolIncqDerived_School_address, schoolIncqDerived_School_name, schoolIncqDerived_School_currentYear, schoolIncqDerived_School_numberOfTeachers}

# schoolIncqDerived_Student class attributes and methods
schoolIncqDerived_Student_name: Property = Property(name="name", type=StringType)
schoolIncqDerived_Student.attributes={schoolIncqDerived_Student_name}

# schoolIncqDerived_SpecialisationCourse class attributes and methods
schoolIncqDerived_SpecialisationCourse_specialisation: Property = Property(name="specialisation", type=StringType)
schoolIncqDerived_SpecialisationCourse.attributes={schoolIncqDerived_SpecialisationCourse_specialisation}

# Course class attributes and methods

# Relationships
teacher1: BinaryAssociation = BinaryAssociation(
    name="teacher1",
    ends={
        Property(name="Teacher", type=schoolIncqDerived_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses2", type=schoolIncqDerived_Teacher, multiplicity=Multiplicity(0, 1))
    }
)
schoolClass3: BinaryAssociation = BinaryAssociation(
    name="schoolClass3",
    ends={
        Property(name="SchoolClass", type=schoolIncqDerived_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses4", type=schoolIncqDerived_SchoolClass, multiplicity=Multiplicity(0, 1))
    }
)
years5: BinaryAssociation = BinaryAssociation(
    name="years5",
    ends={
        Property(name="Year", type=schoolIncqDerived_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school", type=schoolIncqDerived_Year, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teachers6: BinaryAssociation = BinaryAssociation(
    name="teachers6",
    ends={
        Property(name="Teacher8", type=schoolIncqDerived_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school7", type=schoolIncqDerived_Teacher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses9: BinaryAssociation = BinaryAssociation(
    name="courses9",
    ends={
        Property(name="Course", type=schoolIncqDerived_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school10", type=schoolIncqDerived_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
school0: BinaryAssociation = BinaryAssociation(
    name="school0",
    ends={
        Property(name="School", type=schoolIncqDerived_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=schoolIncqDerived_School, multiplicity=Multiplicity(0, 1))
    }
)
year14: BinaryAssociation = BinaryAssociation(
    name="year14",
    ends={
        Property(name="Year15", type=schoolIncqDerived_SchoolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="schoolClasses", type=schoolIncqDerived_Year, multiplicity=Multiplicity(0, 1))
    }
)
students16: BinaryAssociation = BinaryAssociation(
    name="students16",
    ends={
        Property(name="Student", type=schoolIncqDerived_SchoolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="schoolClass", type=schoolIncqDerived_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses17: BinaryAssociation = BinaryAssociation(
    name="courses17",
    ends={
        Property(name="Course19", type=schoolIncqDerived_SchoolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="schoolClass18", type=schoolIncqDerived_Course, multiplicity=Multiplicity(0, 9999))
    }
)
homeroomTeacher20: BinaryAssociation = BinaryAssociation(
    name="homeroomTeacher20",
    ends={
        Property(name="schoolIncqDerived_Teacher21", type=schoolIncqDerived_SchoolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="schoolIncqDerived_SchoolClass", type=schoolIncqDerived_Teacher, multiplicity=Multiplicity(0, 1))
    }
)
teachersWithMostCourses11: BinaryAssociation = BinaryAssociation(
    name="teachersWithMostCourses11",
    ends={
        Property(name="schoolIncqDerived_Teacher", type=schoolIncqDerived_School, multiplicity=Multiplicity(1, 1)),
        Property(name="schoolIncqDerived_School", type=schoolIncqDerived_Teacher, multiplicity=Multiplicity(0, 9999))
    }
)
lastYear12: BinaryAssociation = BinaryAssociation(
    name="lastYear12",
    ends={
        Property(name="schoolIncqDerived_Year", type=schoolIncqDerived_School, multiplicity=Multiplicity(1, 1)),
        Property(name="schoolIncqDerived_School13", type=schoolIncqDerived_Year, multiplicity=Multiplicity(0, 1))
    }
)
school24: BinaryAssociation = BinaryAssociation(
    name="school24",
    ends={
        Property(name="School25", type=schoolIncqDerived_Teacher, multiplicity=Multiplicity(1, 1)),
        Property(name="teachers", type=schoolIncqDerived_School, multiplicity=Multiplicity(0, 1))
    }
)
courses26: BinaryAssociation = BinaryAssociation(
    name="courses26",
    ends={
        Property(name="Course27", type=schoolIncqDerived_Teacher, multiplicity=Multiplicity(1, 1)),
        Property(name="teacher", type=schoolIncqDerived_Course, multiplicity=Multiplicity(0, 9999))
    }
)
homeroomedClass28: BinaryAssociation = BinaryAssociation(
    name="homeroomedClass28",
    ends={
        Property(name="schoolIncqDerived_SchoolClass30", type=schoolIncqDerived_Teacher, multiplicity=Multiplicity(1, 1)),
        Property(name="schoolIncqDerived_Teacher29", type=schoolIncqDerived_SchoolClass, multiplicity=Multiplicity(0, 1))
    }
)
school31: BinaryAssociation = BinaryAssociation(
    name="school31",
    ends={
        Property(name="School32", type=schoolIncqDerived_Year, multiplicity=Multiplicity(1, 1)),
        Property(name="years", type=schoolIncqDerived_School, multiplicity=Multiplicity(0, 1))
    }
)
schoolClasses33: BinaryAssociation = BinaryAssociation(
    name="schoolClasses33",
    ends={
        Property(name="SchoolClass34", type=schoolIncqDerived_Year, multiplicity=Multiplicity(1, 1)),
        Property(name="year", type=schoolIncqDerived_SchoolClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schoolClass22: BinaryAssociation = BinaryAssociation(
    name="schoolClass22",
    ends={
        Property(name="SchoolClass23", type=schoolIncqDerived_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=schoolIncqDerived_SchoolClass, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_schoolIncqDerived_SpecialisationCourse_Course = Generalization(general=Course, specific=schoolIncqDerived_SpecialisationCourse)

# Domain Model
domain_model = DomainModel(
    name="schoolIncqDerived",
    types={schoolIncqDerived_Course, schoolIncqDerived_Teacher, schoolIncqDerived_SchoolClass, schoolIncqDerived_Year, schoolIncqDerived_School, schoolIncqDerived_Student, schoolIncqDerived_SpecialisationCourse, Course},
    associations={teacher1, schoolClass3, years5, teachers6, courses9, school0, year14, students16, courses17, homeroomTeacher20, teachersWithMostCourses11, lastYear12, school24, courses26, homeroomedClass28, school31, schoolClasses33, schoolClass22},
    generalizations={gen_schoolIncqDerived_SpecialisationCourse_Course},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)