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
StudyProgramCode: Enumeration = Enumeration(
    name="StudyProgramCode",
    literals={
            EnumerationLiteral(name="MTDT"),
			EnumerationLiteral(name="BIT"),
			EnumerationLiteral(name="MIT"),
			EnumerationLiteral(name="MTIØT")
    }
)

CourseWorkType: Enumeration = Enumeration(
    name="CourseWorkType",
    literals={
            EnumerationLiteral(name="LABHOUR"),
			EnumerationLiteral(name="LECTURE")
    }
)

DeadlineEvaluation: Enumeration = Enumeration(
    name="DeadlineEvaluation",
    literals={
            EnumerationLiteral(name="ASSIGNMENT"),
			EnumerationLiteral(name="PROJECT")
    }
)

# Classes
course_desc_Course = Class(name="course::desc::Course")
course_desc_CoursePreconditions = Class(name="course::desc::CoursePreconditions")
course_desc_Timetable = Class(name="course::desc::Timetable")
course_desc_Lecturer = Class(name="course::desc::Lecturer")
course_desc_CourseCoordinator = Class(name="course::desc::CourseCoordinator")
course_desc_CourseInstance = Class(name="course::desc::CourseInstance")
course_desc_Evaluation = Class(name="course::desc::Evaluation", is_abstract=True)
course_desc_Department = Class(name="course::desc::Department")
course_desc_Exam = Class(name="course::desc::Exam")
Evaluation = Class(name="Evaluation")
course_desc_Student = Class(name="course::desc::Student")
course_desc_StudyProgram = Class(name="course::desc::StudyProgram")
course_desc_CourseWork = Class(name="course::desc::CourseWork")
PersonRole = Class(name="PersonRole")
course_desc_Person = Class(name="course::desc::Person")
course_desc_PersonRole = Class(name="course::desc::PersonRole", is_abstract=True)
course_desc_Univ = Class(name="course::desc::Univ")
course_desc_EvaluationWithDeadline = Class(name="course::desc::EvaluationWithDeadline")

# course_desc_Course class attributes and methods
course_desc_Course_Code: Property = Property(name="Code", type=StringType)
course_desc_Course_name: Property = Property(name="name", type=StringType)
course_desc_Course_Content: Property = Property(name="Content", type=StringType)
course_desc_Course_Credits: Property = Property(name="Credits", type=StringType)
course_desc_Course.attributes={course_desc_Course_Content, course_desc_Course_Code, course_desc_Course_Credits, course_desc_Course_name}

# course_desc_CoursePreconditions class attributes and methods
course_desc_CoursePreconditions_isRecommended: Property = Property(name="isRecommended", type=BooleanType)
course_desc_CoursePreconditions_isRequired: Property = Property(name="isRequired", type=BooleanType)
course_desc_CoursePreconditions_reductionPoints: Property = Property(name="reductionPoints", type=FloatType)
course_desc_CoursePreconditions.attributes={course_desc_CoursePreconditions_isRecommended, course_desc_CoursePreconditions_isRequired, course_desc_CoursePreconditions_reductionPoints}

# course_desc_Timetable class attributes and methods

# course_desc_Lecturer class attributes and methods

# course_desc_CourseCoordinator class attributes and methods

# course_desc_CourseInstance class attributes and methods
course_desc_CourseInstance_Year: Property = Property(name="Year", type=IntegerType)
course_desc_CourseInstance_LectureHours: Property = Property(name="LectureHours", type=FloatType)
course_desc_CourseInstance_LabHours: Property = Property(name="LabHours", type=FloatType)
course_desc_CourseInstance.attributes={course_desc_CourseInstance_LabHours, course_desc_CourseInstance_Year, course_desc_CourseInstance_LectureHours}

# course_desc_Evaluation class attributes and methods
course_desc_Evaluation_Percentage: Property = Property(name="Percentage", type=FloatType)
course_desc_Evaluation.attributes={course_desc_Evaluation_Percentage}

# course_desc_Department class attributes and methods
course_desc_Department_name: Property = Property(name="name", type=StringType)
course_desc_Department.attributes={course_desc_Department_name}

# course_desc_Exam class attributes and methods
course_desc_Exam_date: Property = Property(name="date", type=DateType)
course_desc_Exam_place: Property = Property(name="place", type=StringType)
course_desc_Exam_duration: Property = Property(name="duration", type=FloatType)
course_desc_Exam.attributes={course_desc_Exam_date, course_desc_Exam_place, course_desc_Exam_duration}

# Evaluation class attributes and methods

# course_desc_Student class attributes and methods
course_desc_Student_totalStudyPoints: Property = Property(name="totalStudyPoints", type=FloatType)
course_desc_Student_m_signUpForExam: Method = Method(name="signUpForExam", parameters={Parameter(name='exam')}, type=BooleanType)
course_desc_Student_m_cancelExam: Method = Method(name="cancelExam", parameters={Parameter(name='exam')}, type=BooleanType)
course_desc_Student_m_takeExam: Method = Method(name="takeExam", parameters={Parameter(name='exam')}, type=BooleanType)
course_desc_Student.attributes={course_desc_Student_totalStudyPoints}
course_desc_Student.methods={course_desc_Student_m_takeExam, course_desc_Student_m_cancelExam, course_desc_Student_m_signUpForExam}

# course_desc_StudyProgram class attributes and methods
course_desc_StudyProgram_studyCode: Property = Property(name="studyCode", type=StringType)
course_desc_StudyProgram.attributes={course_desc_StudyProgram_studyCode}

# course_desc_CourseWork class attributes and methods
course_desc_CourseWork_Duration: Property = Property(name="Duration", type=IntegerType)
course_desc_CourseWork_Room: Property = Property(name="Room", type=StringType)
course_desc_CourseWork_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
course_desc_CourseWork_isRestricted: Property = Property(name="isRestricted", type=BooleanType)
course_desc_CourseWork_Type: Property = Property(name="Type", type=StringType)
course_desc_CourseWork.attributes={course_desc_CourseWork_Duration, course_desc_CourseWork_Type, course_desc_CourseWork_Room, course_desc_CourseWork_isMandatory, course_desc_CourseWork_isRestricted}

# PersonRole class attributes and methods

# course_desc_Person class attributes and methods
course_desc_Person_fullName: Property = Property(name="fullName", type=StringType)
course_desc_Person_lastName: Property = Property(name="lastName", type=StringType)
course_desc_Person_personNr: Property = Property(name="personNr", type=StringType)
course_desc_Person_name: Property = Property(name="name", type=StringType)
course_desc_Person.attributes={course_desc_Person_personNr, course_desc_Person_lastName, course_desc_Person_name, course_desc_Person_fullName}

# course_desc_PersonRole class attributes and methods

# course_desc_Univ class attributes and methods

# course_desc_EvaluationWithDeadline class attributes and methods
course_desc_EvaluationWithDeadline_deadlineEvaluation: Property = Property(name="deadlineEvaluation", type=StringType)
course_desc_EvaluationWithDeadline.attributes={course_desc_EvaluationWithDeadline_deadlineEvaluation}

# Relationships
hasPrecondition1: BinaryAssociation = BinaryAssociation(
    name="hasPrecondition1",
    ends={
        Property(name="course_desc_CoursePreconditions", type=course_desc_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_Course", type=course_desc_CoursePreconditions, multiplicity=Multiplicity(0, 9999))
    }
)
hasTimetable2: BinaryAssociation = BinaryAssociation(
    name="hasTimetable2",
    ends={
        Property(name="course_desc_Timetable", type=course_desc_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_CourseInstance", type=course_desc_Timetable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
isInstanceOf5: BinaryAssociation = BinaryAssociation(
    name="isInstanceOf5",
    ends={
        Property(name="Department", type=course_desc_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="responsible", type=course_desc_Department, multiplicity=Multiplicity(1, 1))
    }
)
hasLecturers6: BinaryAssociation = BinaryAssociation(
    name="hasLecturers6",
    ends={
        Property(name="course_desc_Lecturer", type=course_desc_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_CourseInstance7", type=course_desc_Lecturer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasCourseCoordinator8: BinaryAssociation = BinaryAssociation(
    name="hasCourseCoordinator8",
    ends={
        Property(name="course_desc_CourseCoordinator", type=course_desc_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_CourseInstance9", type=course_desc_CourseCoordinator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasInstance0: BinaryAssociation = BinaryAssociation(
    name="hasInstance0",
    ends={
        Property(name="CourseInstance", type=course_desc_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="instanceOfCourse", type=course_desc_CourseInstance, multiplicity=Multiplicity(0, 9999))
    }
)
instanceOfCourse3: BinaryAssociation = BinaryAssociation(
    name="instanceOfCourse3",
    ends={
        Property(name="Course", type=course_desc_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="hasInstance", type=course_desc_Course, multiplicity=Multiplicity(1, 1))
    }
)
hasEvaluations4: BinaryAssociation = BinaryAssociation(
    name="hasEvaluations4",
    ends={
        Property(name="Evaluation", type=course_desc_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="belongsTo", type=course_desc_Evaluation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
hasRegisteredStudents15: BinaryAssociation = BinaryAssociation(
    name="hasRegisteredStudents15",
    ends={
        Property(name="Student", type=course_desc_Exam, multiplicity=Multiplicity(1, 1)),
        Property(name="hasExams", type=course_desc_Student, multiplicity=Multiplicity(0, 9999))
    }
)
responsible10: BinaryAssociation = BinaryAssociation(
    name="responsible10",
    ends={
        Property(name="CourseInstance11", type=course_desc_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="isInstanceOf", type=course_desc_CourseInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manages12: BinaryAssociation = BinaryAssociation(
    name="manages12",
    ends={
        Property(name="StudyProgram", type=course_desc_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="belongs", type=course_desc_StudyProgram, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
belongsTo13: BinaryAssociation = BinaryAssociation(
    name="belongsTo13",
    ends={
        Property(name="CourseInstance14", type=course_desc_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="hasEvaluations", type=course_desc_CourseInstance, multiplicity=Multiplicity(0, 1))
    }
)
belongsTo20: BinaryAssociation = BinaryAssociation(
    name="belongsTo20",
    ends={
        Property(name="course_desc_Course22", type=course_desc_CoursePreconditions, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_CoursePreconditions21", type=course_desc_Course, multiplicity=Multiplicity(1, 1))
    }
)
hasCourseWork16: BinaryAssociation = BinaryAssociation(
    name="hasCourseWork16",
    ends={
        Property(name="course_desc_CourseWork", type=course_desc_Timetable, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_Timetable17", type=course_desc_CourseWork, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programs18: BinaryAssociation = BinaryAssociation(
    name="programs18",
    ends={
        Property(name="course_desc_StudyProgram", type=course_desc_Timetable, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_Timetable19", type=course_desc_StudyProgram, multiplicity=Multiplicity(0, 9999))
    }
)
belongs26: BinaryAssociation = BinaryAssociation(
    name="belongs26",
    ends={
        Property(name="Department27", type=course_desc_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="manages", type=course_desc_Department, multiplicity=Multiplicity(1, 1))
    }
)
offers23: BinaryAssociation = BinaryAssociation(
    name="offers23",
    ends={
        Property(name="course_desc_Course25", type=course_desc_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_StudyProgram24", type=course_desc_Course, multiplicity=Multiplicity(0, 9999))
    }
)
linkedTo29: BinaryAssociation = BinaryAssociation(
    name="linkedTo29",
    ends={
        Property(name="Person", type=course_desc_PersonRole, multiplicity=Multiplicity(1, 1)),
        Property(name="hasRole", type=course_desc_Person, multiplicity=Multiplicity(0, 1))
    }
)
hasRole28: BinaryAssociation = BinaryAssociation(
    name="hasRole28",
    ends={
        Property(name="PersonRole", type=course_desc_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="linkedTo", type=course_desc_PersonRole, multiplicity=Multiplicity(0, 9999))
    }
)
belongsTo35: BinaryAssociation = BinaryAssociation(
    name="belongsTo35",
    ends={
        Property(name="course_desc_CourseInstance37", type=course_desc_CourseCoordinator, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_CourseCoordinator36", type=course_desc_CourseInstance, multiplicity=Multiplicity(0, 1))
    }
)
hasDepartment38: BinaryAssociation = BinaryAssociation(
    name="hasDepartment38",
    ends={
        Property(name="course_desc_Department", type=course_desc_Univ, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_Univ", type=course_desc_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasCourses39: BinaryAssociation = BinaryAssociation(
    name="hasCourses39",
    ends={
        Property(name="course_desc_Course41", type=course_desc_Univ, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_Univ40", type=course_desc_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasExams30: BinaryAssociation = BinaryAssociation(
    name="hasExams30",
    ends={
        Property(name="Exam", type=course_desc_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="hasRegisteredStudents", type=course_desc_Exam, multiplicity=Multiplicity(0, 9999))
    }
)
finishedExams31: BinaryAssociation = BinaryAssociation(
    name="finishedExams31",
    ends={
        Property(name="course_desc_Exam", type=course_desc_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_Student", type=course_desc_Exam, multiplicity=Multiplicity(0, 9999))
    }
)
belongsTo32: BinaryAssociation = BinaryAssociation(
    name="belongsTo32",
    ends={
        Property(name="course_desc_CourseInstance34", type=course_desc_Lecturer, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_Lecturer33", type=course_desc_CourseInstance, multiplicity=Multiplicity(0, 1))
    }
)
hasPersons42: BinaryAssociation = BinaryAssociation(
    name="hasPersons42",
    ends={
        Property(name="course_desc_Person", type=course_desc_Univ, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_Univ43", type=course_desc_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasPrecond44: BinaryAssociation = BinaryAssociation(
    name="hasPrecond44",
    ends={
        Property(name="course_desc_CoursePreconditions46", type=course_desc_Univ, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_Univ45", type=course_desc_CoursePreconditions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasStudents47: BinaryAssociation = BinaryAssociation(
    name="hasStudents47",
    ends={
        Property(name="course_desc_Student49", type=course_desc_Univ, multiplicity=Multiplicity(1, 1)),
        Property(name="course_desc_Univ48", type=course_desc_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_course_desc_Exam_Evaluation = Generalization(general=Evaluation, specific=course_desc_Exam)
gen_course_desc_Student_PersonRole = Generalization(general=PersonRole, specific=course_desc_Student)
gen_course_desc_CourseCoordinator_PersonRole = Generalization(general=PersonRole, specific=course_desc_CourseCoordinator)
gen_course_desc_Lecturer_PersonRole = Generalization(general=PersonRole, specific=course_desc_Lecturer)
gen_course_desc_EvaluationWithDeadline_Evaluation = Generalization(general=Evaluation, specific=course_desc_EvaluationWithDeadline)

# Domain Model
domain_model = DomainModel(
    name="course_desc",
    types={course_desc_Course, course_desc_CoursePreconditions, course_desc_Timetable, course_desc_Lecturer, course_desc_CourseCoordinator, course_desc_CourseInstance, course_desc_Evaluation, course_desc_Department, course_desc_Exam, Evaluation, course_desc_Student, course_desc_StudyProgram, course_desc_CourseWork, PersonRole, course_desc_Person, course_desc_PersonRole, course_desc_Univ, course_desc_EvaluationWithDeadline, StudyProgramCode, CourseWorkType, DeadlineEvaluation},
    associations={hasPrecondition1, hasTimetable2, isInstanceOf5, hasLecturers6, hasCourseCoordinator8, hasInstance0, instanceOfCourse3, hasEvaluations4, hasRegisteredStudents15, responsible10, manages12, belongsTo13, belongsTo20, hasCourseWork16, programs18, belongs26, offers23, linkedTo29, hasRole28, belongsTo35, hasDepartment38, hasCourses39, hasExams30, finishedExams31, belongsTo32, hasPersons42, hasPrecond44, hasStudents47},
    generalizations={gen_course_desc_Exam_Evaluation, gen_course_desc_Student_PersonRole, gen_course_desc_CourseCoordinator_PersonRole, gen_course_desc_Lecturer_PersonRole, gen_course_desc_EvaluationWithDeadline_Evaluation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)