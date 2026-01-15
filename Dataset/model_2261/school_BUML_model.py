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
school_Course = Class(name="school::Course")
school_SchoolClass = Class(name="school::SchoolClass")
school_Year = Class(name="school::Year")
school_School = Class(name="school::School")
school_Teacher = Class(name="school::Teacher")
school_SpecialisationCourse = Class(name="school::SpecialisationCourse")
Course = Class(name="Course")
school_Student = Class(name="school::Student")

# school_Course class attributes and methods
school_Course_subject: Property = Property(name="subject", type=StringType)
school_Course_weight: Property = Property(name="weight", type=IntegerType)
school_Course.attributes={school_Course_subject, school_Course_weight}

# school_SchoolClass class attributes and methods
school_SchoolClass_code: Property = Property(name="code", type=StringType)
school_SchoolClass.attributes={school_SchoolClass_code}

# school_Year class attributes and methods
school_Year_startingDate: Property = Property(name="startingDate", type=IntegerType)
school_Year.attributes={school_Year_startingDate}

# school_School class attributes and methods
school_School_name: Property = Property(name="name", type=StringType)
school_School_address: Property = Property(name="address", type=StringType)
school_School.attributes={school_School_name, school_School_address}

# school_Teacher class attributes and methods
school_Teacher_name: Property = Property(name="name", type=StringType)
school_Teacher.attributes={school_Teacher_name}

# school_SpecialisationCourse class attributes and methods
school_SpecialisationCourse_specialisation: Property = Property(name="specialisation", type=StringType)
school_SpecialisationCourse.attributes={school_SpecialisationCourse_specialisation}

# Course class attributes and methods

# school_Student class attributes and methods
school_Student_name: Property = Property(name="name", type=StringType)
school_Student.attributes={school_Student_name}

# Relationships
teacher1: BinaryAssociation = BinaryAssociation(
    name="teacher1",
    ends={
        Property(name="Teacher", type=school_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses2", type=school_Teacher, multiplicity=Multiplicity(0, 1))
    }
)
schoolClass3: BinaryAssociation = BinaryAssociation(
    name="schoolClass3",
    ends={
        Property(name="SchoolClass", type=school_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses4", type=school_SchoolClass, multiplicity=Multiplicity(0, 1))
    }
)
years5: BinaryAssociation = BinaryAssociation(
    name="years5",
    ends={
        Property(name="Year", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school", type=school_Year, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teachers6: BinaryAssociation = BinaryAssociation(
    name="teachers6",
    ends={
        Property(name="Teacher8", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school7", type=school_Teacher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses9: BinaryAssociation = BinaryAssociation(
    name="courses9",
    ends={
        Property(name="Course", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school10", type=school_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
school0: BinaryAssociation = BinaryAssociation(
    name="school0",
    ends={
        Property(name="School", type=school_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=school_School, multiplicity=Multiplicity(0, 1))
    }
)
students13: BinaryAssociation = BinaryAssociation(
    name="students13",
    ends={
        Property(name="Student", type=school_SchoolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="schoolClass", type=school_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses14: BinaryAssociation = BinaryAssociation(
    name="courses14",
    ends={
        Property(name="Course16", type=school_SchoolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="schoolClass15", type=school_Course, multiplicity=Multiplicity(0, 9999))
    }
)
homeroomTeacher17: BinaryAssociation = BinaryAssociation(
    name="homeroomTeacher17",
    ends={
        Property(name="school_Teacher", type=school_SchoolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="school_SchoolClass", type=school_Teacher, multiplicity=Multiplicity(0, 1))
    }
)
schoolClass18: BinaryAssociation = BinaryAssociation(
    name="schoolClass18",
    ends={
        Property(name="SchoolClass19", type=school_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=school_SchoolClass, multiplicity=Multiplicity(0, 1))
    }
)
year11: BinaryAssociation = BinaryAssociation(
    name="year11",
    ends={
        Property(name="Year12", type=school_SchoolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="schoolClasses", type=school_Year, multiplicity=Multiplicity(0, 1))
    }
)
courses22: BinaryAssociation = BinaryAssociation(
    name="courses22",
    ends={
        Property(name="Course23", type=school_Teacher, multiplicity=Multiplicity(1, 1)),
        Property(name="teacher", type=school_Course, multiplicity=Multiplicity(0, 9999))
    }
)
homeroomedClass24: BinaryAssociation = BinaryAssociation(
    name="homeroomedClass24",
    ends={
        Property(name="school_SchoolClass26", type=school_Teacher, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Teacher25", type=school_SchoolClass, multiplicity=Multiplicity(0, 1))
    }
)
school27: BinaryAssociation = BinaryAssociation(
    name="school27",
    ends={
        Property(name="School28", type=school_Year, multiplicity=Multiplicity(1, 1)),
        Property(name="years", type=school_School, multiplicity=Multiplicity(0, 1))
    }
)
schoolClasses29: BinaryAssociation = BinaryAssociation(
    name="schoolClasses29",
    ends={
        Property(name="SchoolClass30", type=school_Year, multiplicity=Multiplicity(1, 1)),
        Property(name="year", type=school_SchoolClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
school20: BinaryAssociation = BinaryAssociation(
    name="school20",
    ends={
        Property(name="School21", type=school_Teacher, multiplicity=Multiplicity(1, 1)),
        Property(name="teachers", type=school_School, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_school_SpecialisationCourse_Course = Generalization(general=Course, specific=school_SpecialisationCourse)

# Domain Model
domain_model = DomainModel(
    name="school",
    types={school_Course, school_SchoolClass, school_Year, school_School, school_Teacher, school_SpecialisationCourse, Course, school_Student},
    associations={teacher1, schoolClass3, years5, teachers6, courses9, school0, students13, courses14, homeroomTeacher17, schoolClass18, year11, courses22, homeroomedClass24, school27, schoolClasses29, school20},
    generalizations={gen_school_SpecialisationCourse_Course},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)