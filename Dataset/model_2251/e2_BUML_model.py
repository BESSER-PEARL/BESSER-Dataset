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
e2_Course = Class(name="e2::Course")
e2_Lecture = Class(name="e2::Lecture")
e2_LectureContent = Class(name="e2::LectureContent")
e2_SubGoal = Class(name="e2::SubGoal")
e2_Person = Class(name="e2::Person")
e2_AssignmentSubmission = Class(name="e2::AssignmentSubmission")
e2_Assingnment = Class(name="e2::Assingnment")
e2_Group = Class(name="e2::Group")
e2_Goal = Class(name="e2::Goal")
e2_University = Class(name="e2::University")
e2_EClass0 = Class(name="e2::EClass0")

# e2_Course class attributes and methods
e2_Course_ID: Property = Property(name="ID", type=StringType)
e2_Course_Name: Property = Property(name="Name", type=StringType)
e2_Course_credit: Property = Property(name="credit", type=FloatType)
e2_Course.attributes={e2_Course_credit, e2_Course_ID, e2_Course_Name}

# e2_Lecture class attributes and methods
e2_Lecture_Date: Property = Property(name="Date", type=DateType)
e2_Lecture_length: Property = Property(name="length", type=IntegerType)
e2_Lecture.attributes={e2_Lecture_length, e2_Lecture_Date}

# e2_LectureContent class attributes and methods
e2_LectureContent_Type: Property = Property(name="Type", type=StringType)
e2_LectureContent_Material: Property = Property(name="Material", type=StringType)
e2_LectureContent.attributes={e2_LectureContent_Type, e2_LectureContent_Material}

# e2_SubGoal class attributes and methods
e2_SubGoal_GoalID: Property = Property(name="GoalID", type=StringType)
e2_SubGoal_GoalText: Property = Property(name="GoalText", type=StringType)
e2_SubGoal.attributes={e2_SubGoal_GoalID, e2_SubGoal_GoalText}

# e2_Person class attributes and methods
e2_Person_Name: Property = Property(name="Name", type=StringType)
e2_Person.attributes={e2_Person_Name}

# e2_AssignmentSubmission class attributes and methods
e2_AssignmentSubmission_Comments: Property = Property(name="Comments", type=StringType)
e2_AssignmentSubmission_assessment: Property = Property(name="assessment", type=IntegerType)
e2_AssignmentSubmission.attributes={e2_AssignmentSubmission_Comments, e2_AssignmentSubmission_assessment}

# e2_Assingnment class attributes and methods
e2_Assingnment_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
e2_Assingnment_Deadline: Property = Property(name="Deadline", type=DateType)
e2_Assingnment_StartDate: Property = Property(name="StartDate", type=DateType)
e2_Assingnment_Title: Property = Property(name="Title", type=StringType)
e2_Assingnment_Content: Property = Property(name="Content", type=StringType)
e2_Assingnment_Type: Property = Property(name="Type", type=StringType)
e2_Assingnment.attributes={e2_Assingnment_Deadline, e2_Assingnment_StartDate, e2_Assingnment_Type, e2_Assingnment_Content, e2_Assingnment_Title, e2_Assingnment_isMandatory}

# e2_Group class attributes and methods
e2_Group_Name: Property = Property(name="Name", type=StringType)
e2_Group.attributes={e2_Group_Name}

# e2_Goal class attributes and methods
e2_Goal_GoalID: Property = Property(name="GoalID", type=StringType)
e2_Goal_GoalText: Property = Property(name="GoalText", type=StringType)
e2_Goal.attributes={e2_Goal_GoalText, e2_Goal_GoalID}

# e2_University class attributes and methods
e2_University_Name: Property = Property(name="Name", type=StringType)
e2_University.attributes={e2_University_Name}

# e2_EClass0 class attributes and methods

# Relationships
LearningGoals4: BinaryAssociation = BinaryAssociation(
    name="LearningGoals4",
    ends={
        Property(name="e2_SubGoal5", type=e2_Assingnment, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Assingnment", type=e2_SubGoal, multiplicity=Multiplicity(1, 9999))
    }
)
Students6: BinaryAssociation = BinaryAssociation(
    name="Students6",
    ends={
        Property(name="e2_Person7", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course", type=e2_Person, multiplicity=Multiplicity(0, 9999))
    }
)
Lecturerer8: BinaryAssociation = BinaryAssociation(
    name="Lecturerer8",
    ends={
        Property(name="e2_Person10", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course9", type=e2_Person, multiplicity=Multiplicity(1, 9999))
    }
)
Content0: BinaryAssociation = BinaryAssociation(
    name="Content0",
    ends={
        Property(name="e2_LectureContent", type=e2_Lecture, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Lecture", type=e2_LectureContent, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
LearningGoals1: BinaryAssociation = BinaryAssociation(
    name="LearningGoals1",
    ends={
        Property(name="e2_SubGoal", type=e2_Lecture, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Lecture2", type=e2_SubGoal, multiplicity=Multiplicity(1, 9999))
    }
)
Submitted3: BinaryAssociation = BinaryAssociation(
    name="Submitted3",
    ends={
        Property(name="e2_AssignmentSubmission", type=e2_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Person", type=e2_AssignmentSubmission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Assignment30: BinaryAssociation = BinaryAssociation(
    name="Assignment30",
    ends={
        Property(name="e2_AssignmentSubmission31", type=e2_Assingnment, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Assingnment32", type=e2_AssignmentSubmission, multiplicity=Multiplicity(1, 1))
    }
)
AssesedBy33: BinaryAssociation = BinaryAssociation(
    name="AssesedBy33",
    ends={
        Property(name="e2_Person35", type=e2_AssignmentSubmission, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_AssignmentSubmission34", type=e2_Person, multiplicity=Multiplicity(1, 1))
    }
)
Assingments11: BinaryAssociation = BinaryAssociation(
    name="Assingments11",
    ends={
        Property(name="e2_Assingnment13", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course12", type=e2_Assingnment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Lectures14: BinaryAssociation = BinaryAssociation(
    name="Lectures14",
    ends={
        Property(name="e2_Lecture16", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course15", type=e2_Lecture, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StudentGroups17: BinaryAssociation = BinaryAssociation(
    name="StudentGroups17",
    ends={
        Property(name="e2_Group", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course18", type=e2_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TeachingAssistant19: BinaryAssociation = BinaryAssociation(
    name="TeachingAssistant19",
    ends={
        Property(name="e2_Person21", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course20", type=e2_Person, multiplicity=Multiplicity(0, 9999))
    }
)
LearningGoals22: BinaryAssociation = BinaryAssociation(
    name="LearningGoals22",
    ends={
        Property(name="e2_Goal", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course23", type=e2_Goal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
GroupMember24: BinaryAssociation = BinaryAssociation(
    name="GroupMember24",
    ends={
        Property(name="e2_Person26", type=e2_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Group25", type=e2_Person, multiplicity=Multiplicity(2, 3))
    }
)
Submitted27: BinaryAssociation = BinaryAssociation(
    name="Submitted27",
    ends={
        Property(name="e2_AssignmentSubmission29", type=e2_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Group28", type=e2_AssignmentSubmission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Persons36: BinaryAssociation = BinaryAssociation(
    name="Persons36",
    ends={
        Property(name="e2_Person37", type=e2_University, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_University", type=e2_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Courses38: BinaryAssociation = BinaryAssociation(
    name="Courses38",
    ends={
        Property(name="e2_Course40", type=e2_University, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_University39", type=e2_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
LectureAssignment41: BinaryAssociation = BinaryAssociation(
    name="LectureAssignment41",
    ends={
        Property(name="e2_Assingnment43", type=e2_LectureContent, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_LectureContent42", type=e2_Assingnment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
SubGoals44: BinaryAssociation = BinaryAssociation(
    name="SubGoals44",
    ends={
        Property(name="e2_SubGoal46", type=e2_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Goal45", type=e2_SubGoal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="e2",
    types={e2_Course, e2_Lecture, e2_LectureContent, e2_SubGoal, e2_Person, e2_AssignmentSubmission, e2_Assingnment, e2_Group, e2_Goal, e2_University, e2_EClass0},
    associations={LearningGoals4, Students6, Lecturerer8, Content0, LearningGoals1, Submitted3, Assignment30, AssesedBy33, Assingments11, Lectures14, StudentGroups17, TeachingAssistant19, LearningGoals22, GroupMember24, Submitted27, Persons36, Courses38, LectureAssignment41, SubGoals44},
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