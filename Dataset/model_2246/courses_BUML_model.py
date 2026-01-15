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
Day: Enumeration = Enumeration(
    name="Day",
    literals={
            EnumerationLiteral(name="Monday"),
			EnumerationLiteral(name="Tuesday"),
			EnumerationLiteral(name="Wednesday"),
			EnumerationLiteral(name="Thursday"),
			EnumerationLiteral(name="Friday")
    }
)

HourStart: Enumeration = Enumeration(
    name="HourStart",
    literals={
            EnumerationLiteral(name="h0815"),
			EnumerationLiteral(name="h0915"),
			EnumerationLiteral(name="h1015"),
			EnumerationLiteral(name="h1715"),
			EnumerationLiteral(name="h1815"),
			EnumerationLiteral(name="h1915"),
			EnumerationLiteral(name="h1115"),
			EnumerationLiteral(name="h1215"),
			EnumerationLiteral(name="h1315"),
			EnumerationLiteral(name="h1415"),
			EnumerationLiteral(name="h1515"),
			EnumerationLiteral(name="h1615")
    }
)

HourEnd: Enumeration = Enumeration(
    name="HourEnd",
    literals={
            EnumerationLiteral(name="h0800"),
			EnumerationLiteral(name="h0900"),
			EnumerationLiteral(name="h1000"),
			EnumerationLiteral(name="h1100"),
			EnumerationLiteral(name="h1200"),
			EnumerationLiteral(name="h1300"),
			EnumerationLiteral(name="h1400"),
			EnumerationLiteral(name="h1500"),
			EnumerationLiteral(name="h1600"),
			EnumerationLiteral(name="h1700"),
			EnumerationLiteral(name="h1800"),
			EnumerationLiteral(name="h1900"),
			EnumerationLiteral(name="h2000")
    }
)

Semester: Enumeration = Enumeration(
    name="Semester",
    literals={
            EnumerationLiteral(name="Spring2011"),
			EnumerationLiteral(name="Autumn2011"),
			EnumerationLiteral(name="Spring2012"),
			EnumerationLiteral(name="Autumn2012"),
			EnumerationLiteral(name="Spring2013"),
			EnumerationLiteral(name="Autumn2013"),
			EnumerationLiteral(name="Spring2014"),
			EnumerationLiteral(name="Autumn2014"),
			EnumerationLiteral(name="Spring2015"),
			EnumerationLiteral(name="Autumn2015"),
			EnumerationLiteral(name="Spring2016"),
			EnumerationLiteral(name="Autumn2016"),
			EnumerationLiteral(name="Spring2017"),
			EnumerationLiteral(name="Autumn2017"),
			EnumerationLiteral(name="Autumn2010"),
			EnumerationLiteral(name="Spring2018")
    }
)

TeachingLanguage: Enumeration = Enumeration(
    name="TeachingLanguage",
    literals={
            EnumerationLiteral(name="English"),
			EnumerationLiteral(name="Norwegian")
    }
)

Location: Enumeration = Enumeration(
    name="Location",
    literals={
            EnumerationLiteral(name="Trondheim")
    }
)

Department: Enumeration = Enumeration(
    name="Department",
    literals={
            EnumerationLiteral(name="DepartmentofComputerScience"),
			EnumerationLiteral(name="DepartmentofMathematicalSciences")
    }
)

# Classes
courses_University = Class(name="courses::University")
courses_Course = Class(name="courses::Course")
courses_Person = Class(name="courses::Person")
courses_Content = Class(name="courses::Content")
courses_ExaminationArrangement = Class(name="courses::ExaminationArrangement")
courses_Paragraph = Class(name="courses::Paragraph")
courses_StudyProgram = Class(name="courses::StudyProgram")
courses_CourseInstance = Class(name="courses::CourseInstance")
courses_ExaminationPanel = Class(name="courses::ExaminationPanel")
courses_ContactInfo = Class(name="courses::ContactInfo")
courses_Coursework = Class(name="courses::Coursework")
courses_Timetable = Class(name="courses::Timetable")
courses_EvaluationForm = Class(name="courses::EvaluationForm")
courses_CreditsReduction = Class(name="courses::CreditsReduction")
courses_CourseHour = Class(name="courses::CourseHour")

# courses_University class attributes and methods
courses_University_name: Property = Property(name="name", type=StringType)
courses_University_m_StudentInscription: Method = Method(name="StudentInscription", parameters={Parameter(name='name')})
courses_University_m_StaffInscription: Method = Method(name="StaffInscription", parameters={Parameter(name='name')})
courses_University.attributes={courses_University_name}
courses_University.methods={courses_University_m_StaffInscription, courses_University_m_StudentInscription}

# courses_Course class attributes and methods
courses_Course_name: Property = Property(name="name", type=StringType)
courses_Course_credit: Property = Property(name="credit", type=FloatType)
courses_Course_code: Property = Property(name="code", type=StringType)
courses_Course.attributes={courses_Course_code, courses_Course_credit, courses_Course_name}

# courses_Person class attributes and methods
courses_Person_name: Property = Property(name="name", type=StringType)
courses_Person_Credits: Property = Property(name="Credits", type=FloatType)
courses_Person_m_SignUpExam: Method = Method(name="SignUpExam", parameters={Parameter(name='course')})
courses_Person_m_CancelExam: Method = Method(name="CancelExam", parameters={Parameter(name='course')})
courses_Person_m_PassingExam: Method = Method(name="PassingExam", parameters={Parameter(name='course')})
courses_Person.attributes={courses_Person_name, courses_Person_Credits}
courses_Person.methods={courses_Person_m_SignUpExam, courses_Person_m_CancelExam, courses_Person_m_PassingExam}

# courses_Content class attributes and methods

# courses_ExaminationArrangement class attributes and methods
courses_ExaminationArrangement_type: Property = Property(name="type", type=StringType)
courses_ExaminationArrangement_grade: Property = Property(name="grade", type=StringType)
courses_ExaminationArrangement.attributes={courses_ExaminationArrangement_type, courses_ExaminationArrangement_grade}

# courses_Paragraph class attributes and methods
courses_Paragraph_name: Property = Property(name="name", type=StringType)
courses_Paragraph_description: Property = Property(name="description", type=StringType)
courses_Paragraph.attributes={courses_Paragraph_name, courses_Paragraph_description}

# courses_StudyProgram class attributes and methods
courses_StudyProgram_code: Property = Property(name="code", type=StringType)
courses_StudyProgram.attributes={courses_StudyProgram_code}

# courses_CourseInstance class attributes and methods

# courses_ExaminationPanel class attributes and methods
courses_ExaminationPanel_date: Property = Property(name="date", type=StringType)
courses_ExaminationPanel_time: Property = Property(name="time", type=StringType)
courses_ExaminationPanel_room: Property = Property(name="room", type=StringType)
courses_ExaminationPanel.attributes={courses_ExaminationPanel_room, courses_ExaminationPanel_date, courses_ExaminationPanel_time}

# courses_ContactInfo class attributes and methods
courses_ContactInfo_department: Property = Property(name="department", type=StringType)
courses_ContactInfo_phone: Property = Property(name="phone", type=StringType)
courses_ContactInfo.attributes={courses_ContactInfo_phone, courses_ContactInfo_department}

# courses_Coursework class attributes and methods
courses_Coursework_termNumber: Property = Property(name="termNumber", type=IntegerType)
courses_Coursework_teachingSemester: Property = Property(name="teachingSemester", type=StringType)
courses_Coursework_numLectHour: Property = Property(name="numLectHour", type=IntegerType)
courses_Coursework_numLabHour: Property = Property(name="numLabHour", type=IntegerType)
courses_Coursework_numSpecHour: Property = Property(name="numSpecHour", type=IntegerType)
courses_Coursework_instructionLanguage: Property = Property(name="instructionLanguage", type=StringType)
courses_Coursework_location: Property = Property(name="location", type=StringType)
courses_Coursework.attributes={courses_Coursework_teachingSemester, courses_Coursework_termNumber, courses_Coursework_numLabHour, courses_Coursework_instructionLanguage, courses_Coursework_numSpecHour, courses_Coursework_numLectHour, courses_Coursework_location}

# courses_Timetable class attributes and methods

# courses_EvaluationForm class attributes and methods
courses_EvaluationForm_type: Property = Property(name="type", type=StringType)
courses_EvaluationForm_weighting: Property = Property(name="weighting", type=StringType)
courses_EvaluationForm_duration: Property = Property(name="duration", type=StringType)
courses_EvaluationForm_examAids: Property = Property(name="examAids", type=StringType)
courses_EvaluationForm.attributes={courses_EvaluationForm_weighting, courses_EvaluationForm_examAids, courses_EvaluationForm_duration, courses_EvaluationForm_type}

# courses_CreditsReduction class attributes and methods
courses_CreditsReduction_reduction: Property = Property(name="reduction", type=FloatType)
courses_CreditsReduction.attributes={courses_CreditsReduction_reduction}

# courses_CourseHour class attributes and methods
courses_CourseHour_day: Property = Property(name="day", type=StringType)
courses_CourseHour_startHour: Property = Property(name="startHour", type=StringType)
courses_CourseHour_endHour: Property = Property(name="endHour", type=StringType)
courses_CourseHour_type: Property = Property(name="type", type=StringType)
courses_CourseHour_room: Property = Property(name="room", type=StringType)
courses_CourseHour.attributes={courses_CourseHour_endHour, courses_CourseHour_room, courses_CourseHour_type, courses_CourseHour_day, courses_CourseHour_startHour}

# Relationships
course0: BinaryAssociation = BinaryAssociation(
    name="course0",
    ends={
        Property(name="courses_Course", type=courses_University, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_University", type=courses_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staff1: BinaryAssociation = BinaryAssociation(
    name="staff1",
    ends={
        Property(name="courses_Person", type=courses_University, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_University2", type=courses_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyProgram10: BinaryAssociation = BinaryAssociation(
    name="studyProgram10",
    ends={
        Property(name="StudyProgram", type=courses_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=courses_StudyProgram, multiplicity=Multiplicity(0, 9999))
    }
)
student11: BinaryAssociation = BinaryAssociation(
    name="student11",
    ends={
        Property(name="Person", type=courses_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=courses_Person, multiplicity=Multiplicity(0, 9999))
    }
)
examArrangement12: BinaryAssociation = BinaryAssociation(
    name="examArrangement12",
    ends={
        Property(name="courses_ExaminationArrangement", type=courses_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_Content", type=courses_ExaminationArrangement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paragraph13: BinaryAssociation = BinaryAssociation(
    name="paragraph13",
    ends={
        Property(name="courses_Paragraph", type=courses_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_Content14", type=courses_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyProgram3: BinaryAssociation = BinaryAssociation(
    name="studyProgram3",
    ends={
        Property(name="courses_StudyProgram", type=courses_University, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_University4", type=courses_StudyProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students5: BinaryAssociation = BinaryAssociation(
    name="students5",
    ends={
        Property(name="courses_Person7", type=courses_University, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_University6", type=courses_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listCourseInstance8: BinaryAssociation = BinaryAssociation(
    name="listCourseInstance8",
    ends={
        Property(name="courses_CourseInstance", type=courses_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_Course9", type=courses_CourseInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timetable22: BinaryAssociation = BinaryAssociation(
    name="timetable22",
    ends={
        Property(name="courses_Timetable", type=courses_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_CourseInstance23", type=courses_Timetable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
examination24: BinaryAssociation = BinaryAssociation(
    name="examination24",
    ends={
        Property(name="courses_ExaminationPanel", type=courses_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_CourseInstance25", type=courses_ExaminationPanel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
courseRequired26: BinaryAssociation = BinaryAssociation(
    name="courseRequired26",
    ends={
        Property(name="courses_Course28", type=courses_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_CourseInstance27", type=courses_Course, multiplicity=Multiplicity(0, 9999))
    }
)
courseRecommended29: BinaryAssociation = BinaryAssociation(
    name="courseRecommended29",
    ends={
        Property(name="courses_Course31", type=courses_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_CourseInstance30", type=courses_Course, multiplicity=Multiplicity(0, 9999))
    }
)
contactInfo15: BinaryAssociation = BinaryAssociation(
    name="contactInfo15",
    ends={
        Property(name="courses_ContactInfo", type=courses_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_CourseInstance16", type=courses_ContactInfo, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
courseContent17: BinaryAssociation = BinaryAssociation(
    name="courseContent17",
    ends={
        Property(name="courses_Content19", type=courses_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_CourseInstance18", type=courses_Content, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
coursework20: BinaryAssociation = BinaryAssociation(
    name="coursework20",
    ends={
        Property(name="courses_Coursework", type=courses_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_CourseInstance21", type=courses_Coursework, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
creditsReduction32: BinaryAssociation = BinaryAssociation(
    name="creditsReduction32",
    ends={
        Property(name="courses_CreditsReduction", type=courses_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_CourseInstance33", type=courses_CreditsReduction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
evaluationForms34: BinaryAssociation = BinaryAssociation(
    name="evaluationForms34",
    ends={
        Property(name="courses_ExaminationPanel36", type=courses_ExaminationArrangement, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_ExaminationArrangement35", type=courses_ExaminationPanel, multiplicity=Multiplicity(0, 9999))
    }
)
courseCoordinator37: BinaryAssociation = BinaryAssociation(
    name="courseCoordinator37",
    ends={
        Property(name="courses_Person39", type=courses_ContactInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_ContactInfo38", type=courses_Person, multiplicity=Multiplicity(0, 1))
    }
)
staff40: BinaryAssociation = BinaryAssociation(
    name="staff40",
    ends={
        Property(name="courses_Person42", type=courses_ContactInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_ContactInfo41", type=courses_Person, multiplicity=Multiplicity(0, 9999))
    }
)
listCourseHour43: BinaryAssociation = BinaryAssociation(
    name="listCourseHour43",
    ends={
        Property(name="courses_CourseHour", type=courses_Timetable, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_Timetable44", type=courses_CourseHour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plannedFor45: BinaryAssociation = BinaryAssociation(
    name="plannedFor45",
    ends={
        Property(name="courses_StudyProgram47", type=courses_CourseHour, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_CourseHour46", type=courses_StudyProgram, multiplicity=Multiplicity(0, 9999))
    }
)
evaluationForm48: BinaryAssociation = BinaryAssociation(
    name="evaluationForm48",
    ends={
        Property(name="courses_EvaluationForm", type=courses_ExaminationPanel, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_ExaminationPanel49", type=courses_EvaluationForm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course54: BinaryAssociation = BinaryAssociation(
    name="course54",
    ends={
        Property(name="Course55", type=courses_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=courses_Course, multiplicity=Multiplicity(0, 9999))
    }
)
studyProgram56: BinaryAssociation = BinaryAssociation(
    name="studyProgram56",
    ends={
        Property(name="StudyProgram58", type=courses_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="student57", type=courses_StudyProgram, multiplicity=Multiplicity(0, 1))
    }
)
courses50: BinaryAssociation = BinaryAssociation(
    name="courses50",
    ends={
        Property(name="Course", type=courses_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram", type=courses_Course, multiplicity=Multiplicity(0, 9999))
    }
)
student51: BinaryAssociation = BinaryAssociation(
    name="student51",
    ends={
        Property(name="Person53", type=courses_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram52", type=courses_Person, multiplicity=Multiplicity(0, 9999))
    }
)
course59: BinaryAssociation = BinaryAssociation(
    name="course59",
    ends={
        Property(name="courses_Course61", type=courses_CreditsReduction, multiplicity=Multiplicity(1, 1)),
        Property(name="courses_CreditsReduction60", type=courses_Course, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="courses",
    types={courses_University, courses_Course, courses_Person, courses_Content, courses_ExaminationArrangement, courses_Paragraph, courses_StudyProgram, courses_CourseInstance, courses_ExaminationPanel, courses_ContactInfo, courses_Coursework, courses_Timetable, courses_EvaluationForm, courses_CreditsReduction, courses_CourseHour, Day, HourStart, HourEnd, Semester, TeachingLanguage, Location, Department},
    associations={course0, staff1, studyProgram10, student11, examArrangement12, paragraph13, studyProgram3, students5, listCourseInstance8, timetable22, examination24, courseRequired26, courseRecommended29, contactInfo15, courseContent17, coursework20, creditsReduction32, evaluationForms34, courseCoordinator37, staff40, listCourseHour43, plannedFor45, evaluationForm48, course54, studyProgram56, courses50, student51, course59},
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