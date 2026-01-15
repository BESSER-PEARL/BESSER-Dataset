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
StudyProgramType: Enumeration = Enumeration(
    name="StudyProgramType",
    literals={
            EnumerationLiteral(name="MTDT"),
			EnumerationLiteral(name="MTMART")
    }
)

RoleType: Enumeration = Enumeration(
    name="RoleType",
    literals={
            EnumerationLiteral(name="Lecturer"),
			EnumerationLiteral(name="Student"),
			EnumerationLiteral(name="Supervisor")
    }
)

EvaluationType: Enumeration = Enumeration(
    name="EvaluationType",
    literals={
            EnumerationLiteral(name="Exam"),
			EnumerationLiteral(name="Project"),
			EnumerationLiteral(name="Assignment")
    }
)

CourseWorkType: Enumeration = Enumeration(
    name="CourseWorkType",
    literals={
            EnumerationLiteral(name="InDepth"),
			EnumerationLiteral(name="Lecture"),
			EnumerationLiteral(name="Exercise")
    }
)

# Classes
oving4_Root = Class(name="oving4::Root")
oving4_Department = Class(name="oving4::Department")
oving4_Person = Class(name="oving4::Person")
oving4_StudyProgram = Class(name="oving4::StudyProgram")
oving4_Project = Class(name="oving4::Project")
oving4_Course = Class(name="oving4::Course")
oving4_PersonRole = Class(name="oving4::PersonRole")
oving4_Evaluation = Class(name="oving4::Evaluation")
oving4_CourseInstance = Class(name="oving4::CourseInstance")
oving4_Precondition = Class(name="oving4::Precondition")
oving4_TimeTable = Class(name="oving4::TimeTable")
oving4_TimeTableElement = Class(name="oving4::TimeTableElement")
oving4_EvaluationElement = Class(name="oving4::EvaluationElement")
oving4_CourseWork = Class(name="oving4::CourseWork")
oving4_Exam = Class(name="oving4::Exam")
oving4_Assignment = Class(name="oving4::Assignment")

# oving4_Root class attributes and methods

# oving4_Department class attributes and methods
oving4_Department_name: Property = Property(name="name", type=StringType)
oving4_Department.attributes={oving4_Department_name}

# oving4_Person class attributes and methods
oving4_Person_first_name: Property = Property(name="first_name", type=StringType)
oving4_Person_last_name: Property = Property(name="last_name", type=StringType)
oving4_Person_name: Property = Property(name="name", type=StringType)
oving4_Person_studyCredits: Property = Property(name="studyCredits", type=FloatType)
oving4_Person_m_signUpForExam: Method = Method(name="signUpForExam", parameters={Parameter(name='course')}, type=BooleanType)
oving4_Person_m_cancelExam: Method = Method(name="cancelExam", parameters={Parameter(name='course')}, type=BooleanType)
oving4_Person_m_takeExam: Method = Method(name="takeExam", parameters={Parameter(name='course'), Parameter(name='percentageResult')}, type=BooleanType)
oving4_Person.attributes={oving4_Person_first_name, oving4_Person_last_name, oving4_Person_name, oving4_Person_studyCredits}
oving4_Person.methods={oving4_Person_m_takeExam, oving4_Person_m_cancelExam, oving4_Person_m_signUpForExam}

# oving4_StudyProgram class attributes and methods
oving4_StudyProgram_type: Property = Property(name="type", type=StringType)
oving4_StudyProgram.attributes={oving4_StudyProgram_type}

# oving4_Project class attributes and methods
oving4_Project_deadline: Property = Property(name="deadline", type=StringType)
oving4_Project.attributes={oving4_Project_deadline}

# oving4_Course class attributes and methods
oving4_Course_name: Property = Property(name="name", type=StringType)
oving4_Course_code: Property = Property(name="code", type=StringType)
oving4_Course_credits: Property = Property(name="credits", type=FloatType)
oving4_Course_content: Property = Property(name="content", type=StringType)
oving4_Course_examStartDate: Property = Property(name="examStartDate", type=StringType)
oving4_Course_examEndDate: Property = Property(name="examEndDate", type=StringType)
oving4_Course.attributes={oving4_Course_name, oving4_Course_content, oving4_Course_credits, oving4_Course_code, oving4_Course_examStartDate, oving4_Course_examEndDate}

# oving4_PersonRole class attributes and methods
oving4_PersonRole_type: Property = Property(name="type", type=StringType)
oving4_PersonRole.attributes={oving4_PersonRole_type}

# oving4_Evaluation class attributes and methods
oving4_Evaluation_creditsReceived: Property = Property(name="creditsReceived", type=FloatType)
oving4_Evaluation_description: Property = Property(name="description", type=StringType)
oving4_Evaluation_totalPercentageResult: Property = Property(name="totalPercentageResult", type=FloatType)
oving4_Evaluation_completed: Property = Property(name="completed", type=BooleanType)
oving4_Evaluation.attributes={oving4_Evaluation_totalPercentageResult, oving4_Evaluation_description, oving4_Evaluation_creditsReceived, oving4_Evaluation_completed}

# oving4_CourseInstance class attributes and methods
oving4_CourseInstance_sumLectureHours: Property = Property(name="sumLectureHours", type=IntegerType)
oving4_CourseInstance_sumInDepthHours: Property = Property(name="sumInDepthHours", type=IntegerType)
oving4_CourseInstance_sumExerciseHours: Property = Property(name="sumExerciseHours", type=IntegerType)
oving4_CourseInstance.attributes={oving4_CourseInstance_sumExerciseHours, oving4_CourseInstance_sumInDepthHours, oving4_CourseInstance_sumLectureHours}

# oving4_Precondition class attributes and methods
oving4_Precondition_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
oving4_Precondition_creditReduction: Property = Property(name="creditReduction", type=FloatType)
oving4_Precondition.attributes={oving4_Precondition_creditReduction, oving4_Precondition_isMandatory}

# oving4_TimeTable class attributes and methods
oving4_TimeTable_isRestrictedToProgramsInParallell: Property = Property(name="isRestrictedToProgramsInParallell", type=BooleanType)
oving4_TimeTable.attributes={oving4_TimeTable_isRestrictedToProgramsInParallell}

# oving4_TimeTableElement class attributes and methods
oving4_TimeTableElement_date: Property = Property(name="date", type=StringType)
oving4_TimeTableElement_room: Property = Property(name="room", type=StringType)
oving4_TimeTableElement_durationInMinutes: Property = Property(name="durationInMinutes", type=IntegerType)
oving4_TimeTableElement.attributes={oving4_TimeTableElement_date, oving4_TimeTableElement_room, oving4_TimeTableElement_durationInMinutes}

# oving4_EvaluationElement class attributes and methods
oving4_EvaluationElement_percentageResult: Property = Property(name="percentageResult", type=FloatType)
oving4_EvaluationElement_weight: Property = Property(name="weight", type=FloatType)
oving4_EvaluationElement_type: Property = Property(name="type", type=StringType)
oving4_EvaluationElement_attended: Property = Property(name="attended", type=BooleanType)
oving4_EvaluationElement.attributes={oving4_EvaluationElement_attended, oving4_EvaluationElement_type, oving4_EvaluationElement_percentageResult, oving4_EvaluationElement_weight}

# oving4_CourseWork class attributes and methods
oving4_CourseWork_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
oving4_CourseWork_type: Property = Property(name="type", type=StringType)
oving4_CourseWork_name: Property = Property(name="name", type=StringType)
oving4_CourseWork.attributes={oving4_CourseWork_type, oving4_CourseWork_isMandatory, oving4_CourseWork_name}

# oving4_Exam class attributes and methods
oving4_Exam_endDate: Property = Property(name="endDate", type=StringType)
oving4_Exam_previousStartDate: Property = Property(name="previousStartDate", type=StringType)
oving4_Exam_previousEndDate: Property = Property(name="previousEndDate", type=StringType)
oving4_Exam_startDate: Property = Property(name="startDate", type=StringType)
oving4_Exam.attributes={oving4_Exam_endDate, oving4_Exam_startDate, oving4_Exam_previousEndDate, oving4_Exam_previousStartDate}

# oving4_Assignment class attributes and methods
oving4_Assignment_deadline: Property = Property(name="deadline", type=StringType)
oving4_Assignment.attributes={oving4_Assignment_deadline}

# Relationships
ownsDepartment0: BinaryAssociation = BinaryAssociation(
    name="ownsDepartment0",
    ends={
        Property(name="oving4_Department", type=oving4_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_Root", type=oving4_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownsPerson1: BinaryAssociation = BinaryAssociation(
    name="ownsPerson1",
    ends={
        Property(name="oving4_Person", type=oving4_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_Root2", type=oving4_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownsStudyProgram3: BinaryAssociation = BinaryAssociation(
    name="ownsStudyProgram3",
    ends={
        Property(name="oving4_StudyProgram", type=oving4_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_Root4", type=oving4_StudyProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownsProject5: BinaryAssociation = BinaryAssociation(
    name="ownsProject5",
    ends={
        Property(name="oving4_Project", type=oving4_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_Root6", type=oving4_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownsCourse7: BinaryAssociation = BinaryAssociation(
    name="ownsCourse7",
    ends={
        Property(name="oving4_Course", type=oving4_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_Department8", type=oving4_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasEmployee9: BinaryAssociation = BinaryAssociation(
    name="hasEmployee9",
    ends={
        Property(name="PersonRole", type=oving4_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="employedByDepartment", type=oving4_PersonRole, multiplicity=Multiplicity(0, 9999))
    }
)
containsCourse10: BinaryAssociation = BinaryAssociation(
    name="containsCourse10",
    ends={
        Property(name="Course", type=oving4_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram", type=oving4_Course, multiplicity=Multiplicity(0, 9999))
    }
)
hasEmployee11: BinaryAssociation = BinaryAssociation(
    name="hasEmployee11",
    ends={
        Property(name="PersonRole12", type=oving4_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="employedOfStudyProgram", type=oving4_PersonRole, multiplicity=Multiplicity(0, 1))
    }
)
hasRole13: BinaryAssociation = BinaryAssociation(
    name="hasRole13",
    ends={
        Property(name="PersonRole14", type=oving4_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="person", type=oving4_PersonRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasEvaluation15: BinaryAssociation = BinaryAssociation(
    name="hasEvaluation15",
    ends={
        Property(name="Evaluation", type=oving4_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="personEvaluated", type=oving4_Evaluation, multiplicity=Multiplicity(0, 9999))
    }
)
courseInstance16: BinaryAssociation = BinaryAssociation(
    name="courseInstance16",
    ends={
        Property(name="CourseInstance", type=oving4_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedBy", type=oving4_CourseInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyprogram17: BinaryAssociation = BinaryAssociation(
    name="studyprogram17",
    ends={
        Property(name="StudyProgram", type=oving4_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="containsCourse", type=oving4_StudyProgram, multiplicity=Multiplicity(1, 1))
    }
)
hasPrecondition18: BinaryAssociation = BinaryAssociation(
    name="hasPrecondition18",
    ends={
        Property(name="oving4_Precondition", type=oving4_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_Course19", type=oving4_Precondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasTimeTable20: BinaryAssociation = BinaryAssociation(
    name="hasTimeTable20",
    ends={
        Property(name="TimeTable", type=oving4_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedByCourseInstance", type=oving4_TimeTable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hasMember24: BinaryAssociation = BinaryAssociation(
    name="hasMember24",
    ends={
        Property(name="PersonRole25", type=oving4_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="memberOfCourse", type=oving4_PersonRole, multiplicity=Multiplicity(0, 9999))
    }
)
containsEvaluation26: BinaryAssociation = BinaryAssociation(
    name="containsEvaluation26",
    ends={
        Property(name="Evaluation28", type=oving4_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courseInstance27", type=oving4_Evaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person29: BinaryAssociation = BinaryAssociation(
    name="person29",
    ends={
        Property(name="Person", type=oving4_PersonRole, multiplicity=Multiplicity(1, 1)),
        Property(name="hasRole", type=oving4_Person, multiplicity=Multiplicity(0, 1))
    }
)
employedOfStudyProgram30: BinaryAssociation = BinaryAssociation(
    name="employedOfStudyProgram30",
    ends={
        Property(name="StudyProgram31", type=oving4_PersonRole, multiplicity=Multiplicity(1, 1)),
        Property(name="hasEmployee", type=oving4_StudyProgram, multiplicity=Multiplicity(0, 1))
    }
)
memberOfCourse32: BinaryAssociation = BinaryAssociation(
    name="memberOfCourse32",
    ends={
        Property(name="CourseInstance33", type=oving4_PersonRole, multiplicity=Multiplicity(1, 1)),
        Property(name="hasMember", type=oving4_CourseInstance, multiplicity=Multiplicity(0, 9999))
    }
)
employedByDepartment34: BinaryAssociation = BinaryAssociation(
    name="employedByDepartment34",
    ends={
        Property(name="Department", type=oving4_PersonRole, multiplicity=Multiplicity(1, 1)),
        Property(name="hasEmployee35", type=oving4_Department, multiplicity=Multiplicity(1, 1))
    }
)
containsTimeTableElement36: BinaryAssociation = BinaryAssociation(
    name="containsTimeTableElement36",
    ends={
        Property(name="oving4_TimeTableElement", type=oving4_TimeTable, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_TimeTable", type=oving4_TimeTableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedByStudyProgram37: BinaryAssociation = BinaryAssociation(
    name="usedByStudyProgram37",
    ends={
        Property(name="oving4_StudyProgram39", type=oving4_TimeTable, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_TimeTable38", type=oving4_StudyProgram, multiplicity=Multiplicity(0, 1))
    }
)
ownedByCourseInstance40: BinaryAssociation = BinaryAssociation(
    name="ownedByCourseInstance40",
    ends={
        Property(name="CourseInstance41", type=oving4_TimeTable, multiplicity=Multiplicity(1, 1)),
        Property(name="hasTimeTable", type=oving4_CourseInstance, multiplicity=Multiplicity(1, 1))
    }
)
personEvaluated42: BinaryAssociation = BinaryAssociation(
    name="personEvaluated42",
    ends={
        Property(name="Person43", type=oving4_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="hasEvaluation", type=oving4_Person, multiplicity=Multiplicity(1, 1))
    }
)
containsElement44: BinaryAssociation = BinaryAssociation(
    name="containsElement44",
    ends={
        Property(name="oving4_EvaluationElement", type=oving4_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_Evaluation", type=oving4_EvaluationElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBy21: BinaryAssociation = BinaryAssociation(
    name="ownedBy21",
    ends={
        Property(name="Course22", type=oving4_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courseInstance", type=oving4_Course, multiplicity=Multiplicity(1, 1))
    }
)
containsCourseWork23: BinaryAssociation = BinaryAssociation(
    name="containsCourseWork23",
    ends={
        Property(name="oving4_CourseWork", type=oving4_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_CourseInstance", type=oving4_CourseWork, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseInstance45: BinaryAssociation = BinaryAssociation(
    name="courseInstance45",
    ends={
        Property(name="CourseInstance46", type=oving4_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="containsEvaluation", type=oving4_CourseInstance, multiplicity=Multiplicity(1, 1))
    }
)
preconditionCourse47: BinaryAssociation = BinaryAssociation(
    name="preconditionCourse47",
    ends={
        Property(name="oving4_Course49", type=oving4_Precondition, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_Precondition48", type=oving4_Course, multiplicity=Multiplicity(0, 1))
    }
)
usedByCourseWork50: BinaryAssociation = BinaryAssociation(
    name="usedByCourseWork50",
    ends={
        Property(name="oving4_CourseWork52", type=oving4_TimeTableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_TimeTableElement51", type=oving4_CourseWork, multiplicity=Multiplicity(1, 1))
    }
)
containsExam53: BinaryAssociation = BinaryAssociation(
    name="containsExam53",
    ends={
        Property(name="Exam", type=oving4_EvaluationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="belongsToEvaluationElement", type=oving4_Exam, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containsProject54: BinaryAssociation = BinaryAssociation(
    name="containsProject54",
    ends={
        Property(name="Project", type=oving4_EvaluationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="belongsToEvaluationel", type=oving4_Project, multiplicity=Multiplicity(1, 1))
    }
)
containsAssignment55: BinaryAssociation = BinaryAssociation(
    name="containsAssignment55",
    ends={
        Property(name="Assignment", type=oving4_EvaluationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="belongToEvEl", type=oving4_Assignment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
belongsToEvaluationElement56: BinaryAssociation = BinaryAssociation(
    name="belongsToEvaluationElement56",
    ends={
        Property(name="EvaluationElement", type=oving4_Exam, multiplicity=Multiplicity(1, 1)),
        Property(name="containsExam", type=oving4_EvaluationElement, multiplicity=Multiplicity(1, 1))
    }
)
belongsToEvaluationel57: BinaryAssociation = BinaryAssociation(
    name="belongsToEvaluationel57",
    ends={
        Property(name="EvaluationElement58", type=oving4_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="containsProject", type=oving4_EvaluationElement, multiplicity=Multiplicity(1, 1))
    }
)
hasMembers59: BinaryAssociation = BinaryAssociation(
    name="hasMembers59",
    ends={
        Property(name="oving4_PersonRole", type=oving4_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="oving4_Project60", type=oving4_PersonRole, multiplicity=Multiplicity(0, 9999))
    }
)
belongToEvEl61: BinaryAssociation = BinaryAssociation(
    name="belongToEvEl61",
    ends={
        Property(name="EvaluationElement62", type=oving4_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="containsAssignment", type=oving4_EvaluationElement, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="oving4",
    types={oving4_Root, oving4_Department, oving4_Person, oving4_StudyProgram, oving4_Project, oving4_Course, oving4_PersonRole, oving4_Evaluation, oving4_CourseInstance, oving4_Precondition, oving4_TimeTable, oving4_TimeTableElement, oving4_EvaluationElement, oving4_CourseWork, oving4_Exam, oving4_Assignment, StudyProgramType, RoleType, EvaluationType, CourseWorkType},
    associations={ownsDepartment0, ownsPerson1, ownsStudyProgram3, ownsProject5, ownsCourse7, hasEmployee9, containsCourse10, hasEmployee11, hasRole13, hasEvaluation15, courseInstance16, studyprogram17, hasPrecondition18, hasTimeTable20, hasMember24, containsEvaluation26, person29, employedOfStudyProgram30, memberOfCourse32, employedByDepartment34, containsTimeTableElement36, usedByStudyProgram37, ownedByCourseInstance40, personEvaluated42, containsElement44, ownedBy21, containsCourseWork23, courseInstance45, preconditionCourse47, usedByCourseWork50, containsExam53, containsProject54, containsAssignment55, belongsToEvaluationElement56, belongsToEvaluationel57, hasMembers59, belongToEvEl61},
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