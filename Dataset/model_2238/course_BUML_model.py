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
TypeOfInstruction: Enumeration = Enumeration(
    name="TypeOfInstruction",
    literals={
            EnumerationLiteral(name="Lab"),
			EnumerationLiteral(name="Lecture")
    }
)

DayOfWeek: Enumeration = Enumeration(
    name="DayOfWeek",
    literals={
            EnumerationLiteral(name="Monday"),
			EnumerationLiteral(name="Tuesday"),
			EnumerationLiteral(name="Wednesday"),
			EnumerationLiteral(name="Thursday"),
			EnumerationLiteral(name="Friday")
    }
)

# Classes
course_StudyProgram = Class(name="course::StudyProgram")
course_CourseInstance = Class(name="course::CourseInstance")
course_University = Class(name="course::University")
course_Faculty = Class(name="course::Faculty")
course_Department = Class(name="course::Department")
course_Course = Class(name="course::Course")
course_Student = Class(name="course::Student")
course_CourseCoordinator = Class(name="course::CourseCoordinator")
course_Lecturer = Class(name="course::Lecturer")
course_TA = Class(name="course::TA")
course_Organisation = Class(name="course::Organisation")
course_Evaluation = Class(name="course::Evaluation")
course_CourseWork = Class(name="course::CourseWork")
course_Timetable = Class(name="course::Timetable")
course_Person = Class(name="course::Person")
Person = Class(name="Person")
course_TimetableEntry = Class(name="course::TimetableEntry")

# course_StudyProgram class attributes and methods
course_StudyProgram_code: Property = Property(name="code", type=StringType)
course_StudyProgram.attributes={course_StudyProgram_code}

# course_CourseInstance class attributes and methods

# course_University class attributes and methods
course_University_name: Property = Property(name="name", type=StringType)
course_University.attributes={course_University_name}

# course_Faculty class attributes and methods
course_Faculty_name: Property = Property(name="name", type=StringType)
course_Faculty_shortName: Property = Property(name="shortName", type=StringType)
course_Faculty.attributes={course_Faculty_shortName, course_Faculty_name}

# course_Department class attributes and methods
course_Department_name: Property = Property(name="name", type=StringType)
course_Department_shortName: Property = Property(name="shortName", type=StringType)
course_Department.attributes={course_Department_name, course_Department_shortName}

# course_Course class attributes and methods
course_Course_content: Property = Property(name="content", type=StringType)
course_Course_credits: Property = Property(name="credits", type=FloatType)
course_Course_code: Property = Property(name="code", type=StringType)
course_Course_name: Property = Property(name="name", type=StringType)
course_Course.attributes={course_Course_content, course_Course_name, course_Course_code, course_Course_credits}

# course_Student class attributes and methods

# course_CourseCoordinator class attributes and methods

# course_Lecturer class attributes and methods

# course_TA class attributes and methods

# course_Organisation class attributes and methods

# course_Evaluation class attributes and methods
course_Evaluation_project: Property = Property(name="project", type=IntegerType)
course_Evaluation_assigments: Property = Property(name="assigments", type=IntegerType)
course_Evaluation_exam: Property = Property(name="exam", type=IntegerType)
course_Evaluation.attributes={course_Evaluation_project, course_Evaluation_exam, course_Evaluation_assigments}

# course_CourseWork class attributes and methods
course_CourseWork_lectureHours: Property = Property(name="lectureHours", type=IntegerType)
course_CourseWork_labHours: Property = Property(name="labHours", type=IntegerType)
course_CourseWork.attributes={course_CourseWork_labHours, course_CourseWork_lectureHours}

# course_Timetable class attributes and methods

# course_Person class attributes and methods
course_Person_name: Property = Property(name="name", type=StringType)
course_Person.attributes={course_Person_name}

# Person class attributes and methods

# course_TimetableEntry class attributes and methods
course_TimetableEntry_day: Property = Property(name="day", type=StringType)
course_TimetableEntry_room: Property = Property(name="room", type=StringType)
course_TimetableEntry_time: Property = Property(name="time", type=StringType)
course_TimetableEntry_type: Property = Property(name="type", type=StringType)
course_TimetableEntry.attributes={course_TimetableEntry_time, course_TimetableEntry_type, course_TimetableEntry_day, course_TimetableEntry_room}

# Relationships
requiredPreCond4: BinaryAssociation = BinaryAssociation(
    name="requiredPreCond4",
    ends={
        Property(name="course_Course", type=course_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course_Course3", type=course_Course, multiplicity=Multiplicity(0, 9999))
    }
)
recommendedPreCond6: BinaryAssociation = BinaryAssociation(
    name="recommendedPreCond6",
    ends={
        Property(name="course_Course7", type=course_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course_Course5", type=course_Course, multiplicity=Multiplicity(0, 9999))
    }
)
studyPrograms8: BinaryAssociation = BinaryAssociation(
    name="studyPrograms8",
    ends={
        Property(name="course_StudyProgram", type=course_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course_Course9", type=course_StudyProgram, multiplicity=Multiplicity(0, 9999))
    }
)
courseInstances10: BinaryAssociation = BinaryAssociation(
    name="courseInstances10",
    ends={
        Property(name="CourseInstance", type=course_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=course_CourseInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
faculties0: BinaryAssociation = BinaryAssociation(
    name="faculties0",
    ends={
        Property(name="Faculty", type=course_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university", type=course_Faculty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
university1: BinaryAssociation = BinaryAssociation(
    name="university1",
    ends={
        Property(name="University", type=course_Faculty, multiplicity=Multiplicity(1, 1)),
        Property(name="faculties", type=course_University, multiplicity=Multiplicity(0, 1))
    }
)
departments2: BinaryAssociation = BinaryAssociation(
    name="departments2",
    ends={
        Property(name="Department", type=course_Faculty, multiplicity=Multiplicity(1, 1)),
        Property(name="faculty", type=course_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseInstance27: BinaryAssociation = BinaryAssociation(
    name="courseInstance27",
    ends={
        Property(name="CourseInstance28", type=course_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluation", type=course_CourseInstance, multiplicity=Multiplicity(0, 1))
    }
)
registeredStudents29: BinaryAssociation = BinaryAssociation(
    name="registeredStudents29",
    ends={
        Property(name="Student", type=course_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluation30", type=course_Student, multiplicity=Multiplicity(0, 9999))
    }
)
courseCoordinator31: BinaryAssociation = BinaryAssociation(
    name="courseCoordinator31",
    ends={
        Property(name="CourseCoordinator", type=course_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="organisation", type=course_CourseCoordinator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lecturer32: BinaryAssociation = BinaryAssociation(
    name="lecturer32",
    ends={
        Property(name="Lecturer", type=course_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="organisation33", type=course_Lecturer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
department11: BinaryAssociation = BinaryAssociation(
    name="department11",
    ends={
        Property(name="Department12", type=course_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=course_Department, multiplicity=Multiplicity(1, 1))
    }
)
ta34: BinaryAssociation = BinaryAssociation(
    name="ta34",
    ends={
        Property(name="TA", type=course_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="organisation35", type=course_TA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course13: BinaryAssociation = BinaryAssociation(
    name="course13",
    ends={
        Property(name="Course", type=course_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courseInstances", type=course_Course, multiplicity=Multiplicity(1, 1))
    }
)
organisation14: BinaryAssociation = BinaryAssociation(
    name="organisation14",
    ends={
        Property(name="Organisation", type=course_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courseInstance", type=course_Organisation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
evaluation15: BinaryAssociation = BinaryAssociation(
    name="evaluation15",
    ends={
        Property(name="Evaluation", type=course_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courseInstance16", type=course_Evaluation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
courseWork17: BinaryAssociation = BinaryAssociation(
    name="courseWork17",
    ends={
        Property(name="CourseWork", type=course_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courseInstance18", type=course_CourseWork, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
timeTable19: BinaryAssociation = BinaryAssociation(
    name="timeTable19",
    ends={
        Property(name="Timetable", type=course_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courseInstance20", type=course_Timetable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
courses21: BinaryAssociation = BinaryAssociation(
    name="courses21",
    ends={
        Property(name="Course22", type=course_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=course_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyPrograms23: BinaryAssociation = BinaryAssociation(
    name="studyPrograms23",
    ends={
        Property(name="course_StudyProgram24", type=course_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="course_Department", type=course_StudyProgram, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
faculty25: BinaryAssociation = BinaryAssociation(
    name="faculty25",
    ends={
        Property(name="Faculty26", type=course_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="departments", type=course_Faculty, multiplicity=Multiplicity(1, 1))
    }
)
studyProgram49: BinaryAssociation = BinaryAssociation(
    name="studyProgram49",
    ends={
        Property(name="StudyProgram", type=course_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=course_StudyProgram, multiplicity=Multiplicity(1, 1))
    }
)
evaluation50: BinaryAssociation = BinaryAssociation(
    name="evaluation50",
    ends={
        Property(name="Evaluation51", type=course_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="registeredStudents", type=course_Evaluation, multiplicity=Multiplicity(0, 9999))
    }
)
organisation52: BinaryAssociation = BinaryAssociation(
    name="organisation52",
    ends={
        Property(name="Organisation53", type=course_CourseCoordinator, multiplicity=Multiplicity(1, 1)),
        Property(name="courseCoordinator", type=course_Organisation, multiplicity=Multiplicity(1, 1))
    }
)
courseInstance36: BinaryAssociation = BinaryAssociation(
    name="courseInstance36",
    ends={
        Property(name="CourseInstance38", type=course_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="organisation37", type=course_CourseInstance, multiplicity=Multiplicity(0, 1))
    }
)
students39: BinaryAssociation = BinaryAssociation(
    name="students39",
    ends={
        Property(name="Student40", type=course_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram", type=course_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseInstance41: BinaryAssociation = BinaryAssociation(
    name="courseInstance41",
    ends={
        Property(name="CourseInstance42", type=course_CourseWork, multiplicity=Multiplicity(1, 1)),
        Property(name="courseWork", type=course_CourseInstance, multiplicity=Multiplicity(1, 1))
    }
)
courseInstance43: BinaryAssociation = BinaryAssociation(
    name="courseInstance43",
    ends={
        Property(name="CourseInstance44", type=course_Timetable, multiplicity=Multiplicity(1, 1)),
        Property(name="timeTable", type=course_CourseInstance, multiplicity=Multiplicity(1, 1))
    }
)
timetableEntry45: BinaryAssociation = BinaryAssociation(
    name="timetableEntry45",
    ends={
        Property(name="course_TimetableEntry", type=course_Timetable, multiplicity=Multiplicity(1, 1)),
        Property(name="course_Timetable", type=course_TimetableEntry, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
studyProgram46: BinaryAssociation = BinaryAssociation(
    name="studyProgram46",
    ends={
        Property(name="course_StudyProgram48", type=course_TimetableEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="course_TimetableEntry47", type=course_StudyProgram, multiplicity=Multiplicity(0, 9999))
    }
)
organisation54: BinaryAssociation = BinaryAssociation(
    name="organisation54",
    ends={
        Property(name="Organisation55", type=course_Lecturer, multiplicity=Multiplicity(1, 1)),
        Property(name="lecturer", type=course_Organisation, multiplicity=Multiplicity(1, 1))
    }
)
organisation56: BinaryAssociation = BinaryAssociation(
    name="organisation56",
    ends={
        Property(name="Organisation57", type=course_TA, multiplicity=Multiplicity(1, 1)),
        Property(name="ta", type=course_Organisation, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_course_Student_Person = Generalization(general=Person, specific=course_Student)
gen_course_CourseCoordinator_Person = Generalization(general=Person, specific=course_CourseCoordinator)
gen_course_Lecturer_Person = Generalization(general=Person, specific=course_Lecturer)
gen_course_TA_Person = Generalization(general=Person, specific=course_TA)

# Domain Model
domain_model = DomainModel(
    name="course",
    types={course_StudyProgram, course_CourseInstance, course_University, course_Faculty, course_Department, course_Course, course_Student, course_CourseCoordinator, course_Lecturer, course_TA, course_Organisation, course_Evaluation, course_CourseWork, course_Timetable, course_Person, Person, course_TimetableEntry, TypeOfInstruction, DayOfWeek},
    associations={requiredPreCond4, recommendedPreCond6, studyPrograms8, courseInstances10, faculties0, university1, departments2, courseInstance27, registeredStudents29, courseCoordinator31, lecturer32, department11, ta34, course13, organisation14, evaluation15, courseWork17, timeTable19, courses21, studyPrograms23, faculty25, studyProgram49, evaluation50, organisation52, courseInstance36, students39, courseInstance41, courseInstance43, timetableEntry45, studyProgram46, organisation54, organisation56},
    generalizations={gen_course_Student_Person, gen_course_CourseCoordinator_Person, gen_course_Lecturer_Person, gen_course_TA_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)