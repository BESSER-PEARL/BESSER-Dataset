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
CourseWorkType: Enumeration = Enumeration(
    name="CourseWorkType",
    literals={
            EnumerationLiteral(name="Lecture"),
			EnumerationLiteral(name="Lab"),
			EnumerationLiteral(name="Exercise")
    }
)

EvaluationType: Enumeration = Enumeration(
    name="EvaluationType",
    literals={
            EnumerationLiteral(name="WrittenExam"),
			EnumerationLiteral(name="OralExam"),
			EnumerationLiteral(name="Assignments"),
			EnumerationLiteral(name="PracticalExam"),
			EnumerationLiteral(name="Participated")
    }
)

TermType: Enumeration = Enumeration(
    name="TermType",
    literals={
            EnumerationLiteral(name="Spring"),
			EnumerationLiteral(name="Summer"),
			EnumerationLiteral(name="Fall")
    }
)

personRoleType: Enumeration = Enumeration(
    name="personRoleType",
    literals={
            EnumerationLiteral(name="Lecture"),
			EnumerationLiteral(name="CourseCordinator")
    }
)

PrecondistionType: Enumeration = Enumeration(
    name="PrecondistionType",
    literals={
            EnumerationLiteral(name="Required"),
			EnumerationLiteral(name="Recommended")
    }
)

# Classes
coursePages_Person = Class(name="coursePages::Person")
coursePages_Employee = Class(name="coursePages::Employee")
coursePages_Department = Class(name="coursePages::Department")
coursePages_Student = Class(name="coursePages::Student")
Person = Class(name="Person")
coursePages_StudyPrograms = Class(name="coursePages::StudyPrograms")
coursePages_Course = Class(name="coursePages::Course")
coursePages_EvaluationObject = Class(name="coursePages::EvaluationObject")
coursePages_Evaluations = Class(name="coursePages::Evaluations")
coursePages_CourseInstance = Class(name="coursePages::CourseInstance")
coursePages_CourseWorker = Class(name="coursePages::CourseWorker")
coursePages_Precondition = Class(name="coursePages::Precondition")
coursePages_CourseWorkObject = Class(name="coursePages::CourseWorkObject")
coursePages_CourseWork = Class(name="coursePages::CourseWork")
coursePages_Reduction = Class(name="coursePages::Reduction")

# coursePages_Person class attributes and methods
coursePages_Person_firstName: Property = Property(name="firstName", type=StringType)
coursePages_Person_surName: Property = Property(name="surName", type=StringType)
coursePages_Person_phoneNummber: Property = Property(name="phoneNummber", type=StringType)
coursePages_Person_email: Property = Property(name="email", type=StringType)
coursePages_Person.attributes={coursePages_Person_phoneNummber, coursePages_Person_firstName, coursePages_Person_email, coursePages_Person_surName}

# coursePages_Employee class attributes and methods
coursePages_Employee_position: Property = Property(name="position", type=StringType)
coursePages_Employee.attributes={coursePages_Employee_position}

# coursePages_Department class attributes and methods
coursePages_Department_departmentName: Property = Property(name="departmentName", type=StringType)
coursePages_Department_phoneNummber: Property = Property(name="phoneNummber", type=StringType)
coursePages_Department_email: Property = Property(name="email", type=StringType)
coursePages_Department.attributes={coursePages_Department_email, coursePages_Department_departmentName, coursePages_Department_phoneNummber}

# coursePages_Student class attributes and methods
coursePages_Student_studentID: Property = Property(name="studentID", type=StringType)
coursePages_Student.attributes={coursePages_Student_studentID}

# Person class attributes and methods

# coursePages_StudyPrograms class attributes and methods
coursePages_StudyPrograms_studyProgramCode: Property = Property(name="studyProgramCode", type=StringType)
coursePages_StudyPrograms_studyProgramName: Property = Property(name="studyProgramName", type=StringType)
coursePages_StudyPrograms.attributes={coursePages_StudyPrograms_studyProgramCode, coursePages_StudyPrograms_studyProgramName}

# coursePages_Course class attributes and methods
coursePages_Course_courseCredits: Property = Property(name="courseCredits", type=FloatType)
coursePages_Course_courseContent: Property = Property(name="courseContent", type=StringType)
coursePages_Course_courseCode: Property = Property(name="courseCode", type=StringType)
coursePages_Course_courseName: Property = Property(name="courseName", type=StringType)
coursePages_Course.attributes={coursePages_Course_courseName, coursePages_Course_courseContent, coursePages_Course_courseCode, coursePages_Course_courseCredits}

# coursePages_EvaluationObject class attributes and methods
coursePages_EvaluationObject_evaluationsForm: Property = Property(name="evaluationsForm", type=StringType)
coursePages_EvaluationObject_term: Property = Property(name="term", type=StringType)
coursePages_EvaluationObject_credits: Property = Property(name="credits", type=IntegerType)
coursePages_EvaluationObject_date: Property = Property(name="date", type=DateType)
coursePages_EvaluationObject.attributes={coursePages_EvaluationObject_evaluationsForm, coursePages_EvaluationObject_term, coursePages_EvaluationObject_date, coursePages_EvaluationObject_credits}

# coursePages_Evaluations class attributes and methods

# coursePages_CourseInstance class attributes and methods
coursePages_CourseInstance_courseYear: Property = Property(name="courseYear", type=StringType)
coursePages_CourseInstance_term: Property = Property(name="term", type=StringType)
coursePages_CourseInstance.attributes={coursePages_CourseInstance_courseYear, coursePages_CourseInstance_term}

# coursePages_CourseWorker class attributes and methods
coursePages_CourseWorker_courseRole: Property = Property(name="courseRole", type=StringType)
coursePages_CourseWorker.attributes={coursePages_CourseWorker_courseRole}

# coursePages_Precondition class attributes and methods
coursePages_Precondition_preconditionStatus: Property = Property(name="preconditionStatus", type=StringType)
coursePages_Precondition.attributes={coursePages_Precondition_preconditionStatus}

# coursePages_CourseWorkObject class attributes and methods
coursePages_CourseWorkObject_courseWorkType: Property = Property(name="courseWorkType", type=StringType)
coursePages_CourseWorkObject_room: Property = Property(name="room", type=StringType)
coursePages_CourseWorkObject_day: Property = Property(name="day", type=StringType)
coursePages_CourseWorkObject_start: Property = Property(name="start", type=DateType)
coursePages_CourseWorkObject_end: Property = Property(name="end", type=DateType)
coursePages_CourseWorkObject.attributes={coursePages_CourseWorkObject_start, coursePages_CourseWorkObject_end, coursePages_CourseWorkObject_room, coursePages_CourseWorkObject_courseWorkType, coursePages_CourseWorkObject_day}

# coursePages_CourseWork class attributes and methods

# coursePages_Reduction class attributes and methods
coursePages_Reduction_creditReduction: Property = Property(name="creditReduction", type=FloatType)
coursePages_Reduction.attributes={coursePages_Reduction_creditReduction}

# Relationships
course1: BinaryAssociation = BinaryAssociation(
    name="course1",
    ends={
        Property(name="coursePages_Student", type=coursePages_Course, multiplicity=Multiplicity(0, 9999)),
        Property(name="coursePages_Course", type=coursePages_Student, multiplicity=Multiplicity(1, 1))
    }
)
department2: BinaryAssociation = BinaryAssociation(
    name="department2",
    ends={
        Property(name="Department", type=coursePages_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee", type=coursePages_Department, multiplicity=Multiplicity(1, 1))
    }
)
employee3: BinaryAssociation = BinaryAssociation(
    name="employee3",
    ends={
        Property(name="Employee", type=coursePages_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=coursePages_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
studyprograms0: BinaryAssociation = BinaryAssociation(
    name="studyprograms0",
    ends={
        Property(name="StudyPrograms", type=coursePages_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=coursePages_StudyPrograms, multiplicity=Multiplicity(1, 1))
    }
)
course12: BinaryAssociation = BinaryAssociation(
    name="course12",
    ends={
        Property(name="Course", type=coursePages_StudyPrograms, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms13", type=coursePages_Course, multiplicity=Multiplicity(0, 9999))
    }
)
evaluationobject14: BinaryAssociation = BinaryAssociation(
    name="evaluationobject14",
    ends={
        Property(name="coursePages_EvaluationObject", type=coursePages_Evaluations, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_Evaluations", type=coursePages_EvaluationObject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
studyprograms4: BinaryAssociation = BinaryAssociation(
    name="studyprograms4",
    ends={
        Property(name="StudyPrograms5", type=coursePages_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="belongsToDepartment", type=coursePages_StudyPrograms, multiplicity=Multiplicity(0, 9999))
    }
)
course6: BinaryAssociation = BinaryAssociation(
    name="course6",
    ends={
        Property(name="coursePages_Course7", type=coursePages_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_Department", type=coursePages_Course, multiplicity=Multiplicity(0, 9999))
    }
)
belongsToDepartment8: BinaryAssociation = BinaryAssociation(
    name="belongsToDepartment8",
    ends={
        Property(name="Department9", type=coursePages_StudyPrograms, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms", type=coursePages_Department, multiplicity=Multiplicity(1, 1))
    }
)
student10: BinaryAssociation = BinaryAssociation(
    name="student10",
    ends={
        Property(name="Student", type=coursePages_StudyPrograms, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms11", type=coursePages_Student, multiplicity=Multiplicity(0, 9999))
    }
)
courseinstance16: BinaryAssociation = BinaryAssociation(
    name="courseinstance16",
    ends={
        Property(name="coursePages_CourseInstance", type=coursePages_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_Course17", type=coursePages_CourseInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyprograms18: BinaryAssociation = BinaryAssociation(
    name="studyprograms18",
    ends={
        Property(name="StudyPrograms19", type=coursePages_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=coursePages_StudyPrograms, multiplicity=Multiplicity(0, 9999))
    }
)
courseworker20: BinaryAssociation = BinaryAssociation(
    name="courseworker20",
    ends={
        Property(name="coursePages_CourseWorker", type=coursePages_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_Course21", type=coursePages_CourseWorker, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precondition22: BinaryAssociation = BinaryAssociation(
    name="precondition22",
    ends={
        Property(name="coursePages_Precondition", type=coursePages_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_Course23", type=coursePages_Precondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseworkobject15: BinaryAssociation = BinaryAssociation(
    name="courseworkobject15",
    ends={
        Property(name="coursePages_CourseWorkObject", type=coursePages_CourseWork, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_CourseWork", type=coursePages_CourseWorkObject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
employee32: BinaryAssociation = BinaryAssociation(
    name="employee32",
    ends={
        Property(name="coursePages_Employee", type=coursePages_CourseWorker, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_CourseWorker33", type=coursePages_Employee, multiplicity=Multiplicity(0, 1))
    }
)
course34: BinaryAssociation = BinaryAssociation(
    name="course34",
    ends={
        Property(name="coursePages_Course36", type=coursePages_Precondition, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_Precondition35", type=coursePages_Course, multiplicity=Multiplicity(1, 1))
    }
)
course37: BinaryAssociation = BinaryAssociation(
    name="course37",
    ends={
        Property(name="coursePages_Course39", type=coursePages_Reduction, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_Reduction38", type=coursePages_Course, multiplicity=Multiplicity(1, 1))
    }
)
reduction24: BinaryAssociation = BinaryAssociation(
    name="reduction24",
    ends={
        Property(name="coursePages_Reduction", type=coursePages_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_Course25", type=coursePages_Reduction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coursework26: BinaryAssociation = BinaryAssociation(
    name="coursework26",
    ends={
        Property(name="coursePages_CourseWork28", type=coursePages_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_CourseInstance27", type=coursePages_CourseWork, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
evaluations29: BinaryAssociation = BinaryAssociation(
    name="evaluations29",
    ends={
        Property(name="coursePages_Evaluations31", type=coursePages_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="coursePages_CourseInstance30", type=coursePages_Evaluations, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_coursePages_Employee_Person = Generalization(general=Person, specific=coursePages_Employee)
gen_coursePages_Student_Person = Generalization(general=Person, specific=coursePages_Student)

# Domain Model
domain_model = DomainModel(
    name="coursePages",
    types={coursePages_Person, coursePages_Employee, coursePages_Department, coursePages_Student, Person, coursePages_StudyPrograms, coursePages_Course, coursePages_EvaluationObject, coursePages_Evaluations, coursePages_CourseInstance, coursePages_CourseWorker, coursePages_Precondition, coursePages_CourseWorkObject, coursePages_CourseWork, coursePages_Reduction, CourseWorkType, EvaluationType, TermType, personRoleType, PrecondistionType},
    associations={course1, department2, employee3, studyprograms0, course12, evaluationobject14, studyprograms4, course6, belongsToDepartment8, student10, courseinstance16, studyprograms18, courseworker20, precondition22, courseworkobject15, employee32, course34, course37, reduction24, coursework26, evaluations29},
    generalizations={gen_coursePages_Employee_Person, gen_coursePages_Student_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)