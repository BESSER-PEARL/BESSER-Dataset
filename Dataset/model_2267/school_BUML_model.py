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
SchoolElement: Enumeration = Enumeration(
    name="SchoolElement",
    literals={
            EnumerationLiteral(name="Student"),
			EnumerationLiteral(name="Teacher"),
			EnumerationLiteral(name="Faculty"),
			EnumerationLiteral(name="CourseOfStudy"),
			EnumerationLiteral(name="Course"),
			EnumerationLiteral(name="School")
    }
)

# Classes
school_School = Class(name="school::School")
school_Faculty = Class(name="school::Faculty")
school_CourseOfStudy = Class(name="school::CourseOfStudy")
school_Course = Class(name="school::Course")
school_Student = Class(name="school::Student")
school_Teacher = Class(name="school::Teacher")
school_CourseResult = Class(name="school::CourseResult")
school_Where = Class(name="school::Where")
school_BooleanExpr = Class(name="school::BooleanExpr")
school_SchoolDatabase = Class(name="school::SchoolDatabase")
school_Query = Class(name="school::Query")

# school_School class attributes and methods
school_School_name: Property = Property(name="name", type=StringType)
school_School.attributes={school_School_name}

# school_Faculty class attributes and methods
school_Faculty_name: Property = Property(name="name", type=StringType)
school_Faculty.attributes={school_Faculty_name}

# school_CourseOfStudy class attributes and methods
school_CourseOfStudy_name: Property = Property(name="name", type=StringType)
school_CourseOfStudy.attributes={school_CourseOfStudy_name}

# school_Course class attributes and methods
school_Course_name: Property = Property(name="name", type=StringType)
school_Course_courseNumber: Property = Property(name="courseNumber", type=StringType)
school_Course.attributes={school_Course_courseNumber, school_Course_name}

# school_Student class attributes and methods
school_Student_name: Property = Property(name="name", type=StringType)
school_Student_studentNumber: Property = Property(name="studentNumber", type=StringType)
school_Student.attributes={school_Student_name, school_Student_studentNumber}

# school_Teacher class attributes and methods
school_Teacher_name: Property = Property(name="name", type=StringType)
school_Teacher.attributes={school_Teacher_name}

# school_CourseResult class attributes and methods
school_CourseResult_grade: Property = Property(name="grade", type=StringType)
school_CourseResult.attributes={school_CourseResult_grade}

# school_Where class attributes and methods

# school_BooleanExpr class attributes and methods
school_BooleanExpr_lhs: Property = Property(name="lhs", type=StringType)
school_BooleanExpr_rhs: Property = Property(name="rhs", type=StringType)
school_BooleanExpr_operator: Property = Property(name="operator", type=StringType)
school_BooleanExpr.attributes={school_BooleanExpr_rhs, school_BooleanExpr_lhs, school_BooleanExpr_operator}

# school_SchoolDatabase class attributes and methods

# school_Query class attributes and methods
school_Query_type: Property = Property(name="type", type=StringType)
school_Query.attributes={school_Query_type}

# Relationships
faculty0: BinaryAssociation = BinaryAssociation(
    name="faculty0",
    ends={
        Property(name="school_Faculty", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School", type=school_Faculty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseofstudy1: BinaryAssociation = BinaryAssociation(
    name="courseofstudy1",
    ends={
        Property(name="school_CourseOfStudy", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School2", type=school_CourseOfStudy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course3: BinaryAssociation = BinaryAssociation(
    name="course3",
    ends={
        Property(name="school_Course", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School4", type=school_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
student5: BinaryAssociation = BinaryAssociation(
    name="student5",
    ends={
        Property(name="school_Student", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School6", type=school_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teacher7: BinaryAssociation = BinaryAssociation(
    name="teacher7",
    ends={
        Property(name="school_Teacher", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School8", type=school_Teacher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseofstudy9: BinaryAssociation = BinaryAssociation(
    name="courseofstudy9",
    ends={
        Property(name="CourseOfStudy", type=school_Faculty, multiplicity=Multiplicity(1, 1)),
        Property(name="faculty", type=school_CourseOfStudy, multiplicity=Multiplicity(0, 9999))
    }
)
course10: BinaryAssociation = BinaryAssociation(
    name="course10",
    ends={
        Property(name="school_Course12", type=school_CourseOfStudy, multiplicity=Multiplicity(1, 1)),
        Property(name="school_CourseOfStudy11", type=school_Course, multiplicity=Multiplicity(0, 9999))
    }
)
faculty13: BinaryAssociation = BinaryAssociation(
    name="faculty13",
    ends={
        Property(name="Faculty", type=school_CourseOfStudy, multiplicity=Multiplicity(1, 1)),
        Property(name="courseofstudy", type=school_Faculty, multiplicity=Multiplicity(1, 1))
    }
)
student14: BinaryAssociation = BinaryAssociation(
    name="student14",
    ends={
        Property(name="Student", type=school_CourseOfStudy, multiplicity=Multiplicity(1, 1)),
        Property(name="courseofstudy15", type=school_Student, multiplicity=Multiplicity(0, 9999))
    }
)
enrolledStudent16: BinaryAssociation = BinaryAssociation(
    name="enrolledStudent16",
    ends={
        Property(name="Student17", type=school_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="enrolledIn", type=school_Student, multiplicity=Multiplicity(0, 9999))
    }
)
taughtBy18: BinaryAssociation = BinaryAssociation(
    name="taughtBy18",
    ends={
        Property(name="Teacher", type=school_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="teaches", type=school_Teacher, multiplicity=Multiplicity(1, 1))
    }
)
courseresult19: BinaryAssociation = BinaryAssociation(
    name="courseresult19",
    ends={
        Property(name="CourseResult", type=school_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=school_CourseResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enrolledIn20: BinaryAssociation = BinaryAssociation(
    name="enrolledIn20",
    ends={
        Property(name="Course", type=school_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="enrolledStudent", type=school_Course, multiplicity=Multiplicity(0, 9999))
    }
)
courseofstudy21: BinaryAssociation = BinaryAssociation(
    name="courseofstudy21",
    ends={
        Property(name="CourseOfStudy22", type=school_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=school_CourseOfStudy, multiplicity=Multiplicity(1, 1))
    }
)
teaches23: BinaryAssociation = BinaryAssociation(
    name="teaches23",
    ends={
        Property(name="Course24", type=school_Teacher, multiplicity=Multiplicity(1, 1)),
        Property(name="taughtBy", type=school_Course, multiplicity=Multiplicity(0, 9999))
    }
)
student25: BinaryAssociation = BinaryAssociation(
    name="student25",
    ends={
        Property(name="school_Student26", type=school_CourseResult, multiplicity=Multiplicity(1, 1)),
        Property(name="school_CourseResult", type=school_Student, multiplicity=Multiplicity(1, 1))
    }
)
course27: BinaryAssociation = BinaryAssociation(
    name="course27",
    ends={
        Property(name="Course28", type=school_CourseResult, multiplicity=Multiplicity(1, 1)),
        Property(name="courseresult", type=school_Course, multiplicity=Multiplicity(1, 1))
    }
)
where31: BinaryAssociation = BinaryAssociation(
    name="where31",
    ends={
        Property(name="school_Where", type=school_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Query32", type=school_Where, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
booleanexpr33: BinaryAssociation = BinaryAssociation(
    name="booleanexpr33",
    ends={
        Property(name="school_BooleanExpr", type=school_Where, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Where34", type=school_BooleanExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
and36: BinaryAssociation = BinaryAssociation(
    name="and36",
    ends={
        Property(name="school_BooleanExpr37", type=school_BooleanExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="school_BooleanExpr35", type=school_BooleanExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
or39: BinaryAssociation = BinaryAssociation(
    name="or39",
    ends={
        Property(name="school_BooleanExpr40", type=school_BooleanExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="school_BooleanExpr38", type=school_BooleanExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
school41: BinaryAssociation = BinaryAssociation(
    name="school41",
    ends={
        Property(name="school_School42", type=school_SchoolDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="school_SchoolDatabase", type=school_School, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
student29: BinaryAssociation = BinaryAssociation(
    name="student29",
    ends={
        Property(name="school_Student30", type=school_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Query", type=school_Student, multiplicity=Multiplicity(0, 1))
    }
)
query43: BinaryAssociation = BinaryAssociation(
    name="query43",
    ends={
        Property(name="school_Query45", type=school_SchoolDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="school_SchoolDatabase44", type=school_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="school",
    types={school_School, school_Faculty, school_CourseOfStudy, school_Course, school_Student, school_Teacher, school_CourseResult, school_Where, school_BooleanExpr, school_SchoolDatabase, school_Query, SchoolElement},
    associations={faculty0, courseofstudy1, course3, student5, teacher7, courseofstudy9, course10, faculty13, student14, enrolledStudent16, taughtBy18, courseresult19, enrolledIn20, courseofstudy21, teaches23, student25, course27, where31, booleanexpr33, and36, or39, school41, student29, query43},
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