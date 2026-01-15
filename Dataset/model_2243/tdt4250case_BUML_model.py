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
tdt4250case_Studyprogram = Class(name="tdt4250case::Studyprogram")
tdt4250case_Course = Class(name="tdt4250case::Course")
tdt4250case_CreditReductionCourse = Class(name="tdt4250case::CreditReductionCourse")
tdt4250case_CourseInstance = Class(name="tdt4250case::CourseInstance")
tdt4250case_CourseWork = Class(name="tdt4250case::CourseWork")
tdt4250case_Person = Class(name="tdt4250case::Person")
tdt4250case_Examination = Class(name="tdt4250case::Examination")
tdt4250case_Timetable = Class(name="tdt4250case::Timetable")
tdt4250case_Department = Class(name="tdt4250case::Department")
tdt4250case_CourseRole = Class(name="tdt4250case::CourseRole")
tdt4250case_ExaminationActivity = Class(name="tdt4250case::ExaminationActivity")
tdt4250case_ScheduledActivity = Class(name="tdt4250case::ScheduledActivity")

# tdt4250case_Studyprogram class attributes and methods
tdt4250case_Studyprogram_code: Property = Property(name="code", type=StringType)
tdt4250case_Studyprogram.attributes={tdt4250case_Studyprogram_code}

# tdt4250case_Course class attributes and methods
tdt4250case_Course_code: Property = Property(name="code", type=StringType)
tdt4250case_Course_name: Property = Property(name="name", type=StringType)
tdt4250case_Course_content: Property = Property(name="content", type=StringType)
tdt4250case_Course_credits: Property = Property(name="credits", type=FloatType)
tdt4250case_Course.attributes={tdt4250case_Course_credits, tdt4250case_Course_content, tdt4250case_Course_code, tdt4250case_Course_name}

# tdt4250case_CreditReductionCourse class attributes and methods
tdt4250case_CreditReductionCourse_reduction: Property = Property(name="reduction", type=FloatType)
tdt4250case_CreditReductionCourse_from: Property = Property(name="from", type=DateType)
tdt4250case_CreditReductionCourse_to: Property = Property(name="to", type=DateType)
tdt4250case_CreditReductionCourse.attributes={tdt4250case_CreditReductionCourse_reduction, tdt4250case_CreditReductionCourse_from, tdt4250case_CreditReductionCourse_to}

# tdt4250case_CourseInstance class attributes and methods
tdt4250case_CourseInstance_semester: Property = Property(name="semester", type=StringType)
tdt4250case_CourseInstance.attributes={tdt4250case_CourseInstance_semester}

# tdt4250case_CourseWork class attributes and methods
tdt4250case_CourseWork_type: Property = Property(name="type", type=StringType)
tdt4250case_CourseWork_hours: Property = Property(name="hours", type=IntegerType)
tdt4250case_CourseWork.attributes={tdt4250case_CourseWork_type, tdt4250case_CourseWork_hours}

# tdt4250case_Person class attributes and methods
tdt4250case_Person_name: Property = Property(name="name", type=StringType)
tdt4250case_Person_username: Property = Property(name="username", type=StringType)
tdt4250case_Person.attributes={tdt4250case_Person_name, tdt4250case_Person_username}

# tdt4250case_Examination class attributes and methods

# tdt4250case_Timetable class attributes and methods

# tdt4250case_Department class attributes and methods
tdt4250case_Department_code: Property = Property(name="code", type=StringType)
tdt4250case_Department_name: Property = Property(name="name", type=StringType)
tdt4250case_Department.attributes={tdt4250case_Department_code, tdt4250case_Department_name}

# tdt4250case_CourseRole class attributes and methods
tdt4250case_CourseRole_name: Property = Property(name="name", type=StringType)
tdt4250case_CourseRole.attributes={tdt4250case_CourseRole_name}

# tdt4250case_ExaminationActivity class attributes and methods
tdt4250case_ExaminationActivity_evaluationForm: Property = Property(name="evaluationForm", type=StringType)
tdt4250case_ExaminationActivity_weighting: Property = Property(name="weighting", type=StringType)
tdt4250case_ExaminationActivity.attributes={tdt4250case_ExaminationActivity_weighting, tdt4250case_ExaminationActivity_evaluationForm}

# tdt4250case_ScheduledActivity class attributes and methods
tdt4250case_ScheduledActivity_room: Property = Property(name="room", type=StringType)
tdt4250case_ScheduledActivity_timeslot: Property = Property(name="timeslot", type=StringType)
tdt4250case_ScheduledActivity_activity: Property = Property(name="activity", type=StringType)
tdt4250case_ScheduledActivity.attributes={tdt4250case_ScheduledActivity_timeslot, tdt4250case_ScheduledActivity_room, tdt4250case_ScheduledActivity_activity}

# Relationships
studyprogram0: BinaryAssociation = BinaryAssociation(
    name="studyprogram0",
    ends={
        Property(name="Studyprogram", type=tdt4250case_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=tdt4250case_Studyprogram, multiplicity=Multiplicity(0, 9999))
    }
)
recommendedCourse4: BinaryAssociation = BinaryAssociation(
    name="recommendedCourse4",
    ends={
        Property(name="tdt4250case_Course5", type=tdt4250case_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_Course3", type=tdt4250case_Course, multiplicity=Multiplicity(0, 9999))
    }
)
requiredCourse2: BinaryAssociation = BinaryAssociation(
    name="requiredCourse2",
    ends={
        Property(name="tdt4250case_Course", type=tdt4250case_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_Course1", type=tdt4250case_Course, multiplicity=Multiplicity(0, 9999))
    }
)
creditReductionCourse6: BinaryAssociation = BinaryAssociation(
    name="creditReductionCourse6",
    ends={
        Property(name="tdt4250case_CreditReductionCourse", type=tdt4250case_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_Course7", type=tdt4250case_CreditReductionCourse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance8: BinaryAssociation = BinaryAssociation(
    name="instance8",
    ends={
        Property(name="CourseInstance", type=tdt4250case_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course9", type=tdt4250case_CourseInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseWork10: BinaryAssociation = BinaryAssociation(
    name="courseWork10",
    ends={
        Property(name="tdt4250case_CourseWork", type=tdt4250case_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_Course11", type=tdt4250case_CourseWork, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
course12: BinaryAssociation = BinaryAssociation(
    name="course12",
    ends={
        Property(name="tdt4250case_Course14", type=tdt4250case_CreditReductionCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_CreditReductionCourse13", type=tdt4250case_Course, multiplicity=Multiplicity(1, 1))
    }
)
course15: BinaryAssociation = BinaryAssociation(
    name="course15",
    ends={
        Property(name="Course", type=tdt4250case_Studyprogram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram", type=tdt4250case_Course, multiplicity=Multiplicity(0, 9999))
    }
)
role21: BinaryAssociation = BinaryAssociation(
    name="role21",
    ends={
        Property(name="tdt4250case_CourseRole", type=tdt4250case_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_CourseInstance22", type=tdt4250case_CourseRole, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
examination16: BinaryAssociation = BinaryAssociation(
    name="examination16",
    ends={
        Property(name="tdt4250case_Examination", type=tdt4250case_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_CourseInstance", type=tdt4250case_Examination, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
timetable17: BinaryAssociation = BinaryAssociation(
    name="timetable17",
    ends={
        Property(name="tdt4250case_Timetable", type=tdt4250case_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_CourseInstance18", type=tdt4250case_Timetable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
responsibleDepartment19: BinaryAssociation = BinaryAssociation(
    name="responsibleDepartment19",
    ends={
        Property(name="tdt4250case_Department", type=tdt4250case_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_CourseInstance20", type=tdt4250case_Department, multiplicity=Multiplicity(1, 1))
    }
)
courseCoordinator23: BinaryAssociation = BinaryAssociation(
    name="courseCoordinator23",
    ends={
        Property(name="tdt4250case_Person", type=tdt4250case_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_CourseInstance24", type=tdt4250case_Person, multiplicity=Multiplicity(1, 1))
    }
)
course25: BinaryAssociation = BinaryAssociation(
    name="course25",
    ends={
        Property(name="Course26", type=tdt4250case_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance", type=tdt4250case_Course, multiplicity=Multiplicity(1, 1))
    }
)
activity27: BinaryAssociation = BinaryAssociation(
    name="activity27",
    ends={
        Property(name="tdt4250case_ExaminationActivity", type=tdt4250case_Examination, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_Examination28", type=tdt4250case_ExaminationActivity, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reservedFor31: BinaryAssociation = BinaryAssociation(
    name="reservedFor31",
    ends={
        Property(name="tdt4250case_Studyprogram", type=tdt4250case_ScheduledActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_ScheduledActivity32", type=tdt4250case_Studyprogram, multiplicity=Multiplicity(1, 9999))
    }
)
scheduledActivity29: BinaryAssociation = BinaryAssociation(
    name="scheduledActivity29",
    ends={
        Property(name="tdt4250case_ScheduledActivity", type=tdt4250case_Timetable, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_Timetable30", type=tdt4250case_ScheduledActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role36: BinaryAssociation = BinaryAssociation(
    name="role36",
    ends={
        Property(name="CourseRole", type=tdt4250case_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="person", type=tdt4250case_CourseRole, multiplicity=Multiplicity(0, 9999))
    }
)
employee33: BinaryAssociation = BinaryAssociation(
    name="employee33",
    ends={
        Property(name="tdt4250case_Person35", type=tdt4250case_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250case_Department34", type=tdt4250case_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person37: BinaryAssociation = BinaryAssociation(
    name="person37",
    ends={
        Property(name="Person", type=tdt4250case_CourseRole, multiplicity=Multiplicity(1, 1)),
        Property(name="role", type=tdt4250case_Person, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tdt4250case",
    types={tdt4250case_Studyprogram, tdt4250case_Course, tdt4250case_CreditReductionCourse, tdt4250case_CourseInstance, tdt4250case_CourseWork, tdt4250case_Person, tdt4250case_Examination, tdt4250case_Timetable, tdt4250case_Department, tdt4250case_CourseRole, tdt4250case_ExaminationActivity, tdt4250case_ScheduledActivity},
    associations={studyprogram0, recommendedCourse4, requiredCourse2, creditReductionCourse6, instance8, courseWork10, course12, course15, role21, examination16, timetable17, responsibleDepartment19, courseCoordinator23, course25, activity27, reservedFor31, scheduledActivity29, role36, employee33, person37},
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