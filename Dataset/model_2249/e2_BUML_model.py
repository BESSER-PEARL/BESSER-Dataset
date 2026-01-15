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
e2_Lecture = Class(name="e2::Lecture")
e2_Course = Class(name="e2::Course")
e2_LectureContent = Class(name="e2::LectureContent")
e2_Person = Class(name="e2::Person")
e2_AssignmentSubmission = Class(name="e2::AssignmentSubmission")
e2_Assingnment = Class(name="e2::Assingnment")
e2_Group = Class(name="e2::Group")
e2_University = Class(name="e2::University")

# e2_Lecture class attributes and methods
e2_Lecture_Date: Property = Property(name="Date", type=DateType)
e2_Lecture_Length: Property = Property(name="Length", type=IntegerType)
e2_Lecture.attributes={e2_Lecture_Date, e2_Lecture_Length}

# e2_Course class attributes and methods
e2_Course_ID: Property = Property(name="ID", type=StringType)
e2_Course_Name: Property = Property(name="Name", type=StringType)
e2_Course_Credit: Property = Property(name="Credit", type=FloatType)
e2_Course.attributes={e2_Course_Name, e2_Course_ID, e2_Course_Credit}

# e2_LectureContent class attributes and methods
e2_LectureContent_Material: Property = Property(name="Material", type=StringType)
e2_LectureContent_Type: Property = Property(name="Type", type=StringType)
e2_LectureContent.attributes={e2_LectureContent_Material, e2_LectureContent_Type}

# e2_Person class attributes and methods
e2_Person_Name: Property = Property(name="Name", type=StringType)
e2_Person.attributes={e2_Person_Name}

# e2_AssignmentSubmission class attributes and methods
e2_AssignmentSubmission_Comments: Property = Property(name="Comments", type=StringType)
e2_AssignmentSubmission_Assessment: Property = Property(name="Assessment", type=IntegerType)
e2_AssignmentSubmission.attributes={e2_AssignmentSubmission_Assessment, e2_AssignmentSubmission_Comments}

# e2_Assingnment class attributes and methods
e2_Assingnment_Title: Property = Property(name="Title", type=StringType)
e2_Assingnment_Content: Property = Property(name="Content", type=StringType)
e2_Assingnment_Type: Property = Property(name="Type", type=StringType)
e2_Assingnment_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
e2_Assingnment_Deadline: Property = Property(name="Deadline", type=DateType)
e2_Assingnment_StartDate: Property = Property(name="StartDate", type=DateType)
e2_Assingnment.attributes={e2_Assingnment_isMandatory, e2_Assingnment_Content, e2_Assingnment_Type, e2_Assingnment_Title, e2_Assingnment_Deadline, e2_Assingnment_StartDate}

# e2_Group class attributes and methods
e2_Group_Name: Property = Property(name="Name", type=StringType)
e2_Group.attributes={e2_Group_Name}

# e2_University class attributes and methods
e2_University_Name: Property = Property(name="Name", type=StringType)
e2_University.attributes={e2_University_Name}

# Relationships
Students2: BinaryAssociation = BinaryAssociation(
    name="Students2",
    ends={
        Property(name="e2_Person3", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course", type=e2_Person, multiplicity=Multiplicity(0, 9999))
    }
)
Content0: BinaryAssociation = BinaryAssociation(
    name="Content0",
    ends={
        Property(name="e2_LectureContent", type=e2_Lecture, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Lecture", type=e2_LectureContent, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Submitted1: BinaryAssociation = BinaryAssociation(
    name="Submitted1",
    ends={
        Property(name="e2_AssignmentSubmission", type=e2_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Person", type=e2_AssignmentSubmission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
GroupMember17: BinaryAssociation = BinaryAssociation(
    name="GroupMember17",
    ends={
        Property(name="e2_Group18", type=e2_Person, multiplicity=Multiplicity(2, 3)),
        Property(name="e2_Person19", type=e2_Group, multiplicity=Multiplicity(1, 1))
    }
)
Submitted20: BinaryAssociation = BinaryAssociation(
    name="Submitted20",
    ends={
        Property(name="e2_AssignmentSubmission22", type=e2_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Group21", type=e2_AssignmentSubmission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Lecturerer4: BinaryAssociation = BinaryAssociation(
    name="Lecturerer4",
    ends={
        Property(name="e2_Person6", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course5", type=e2_Person, multiplicity=Multiplicity(1, 9999))
    }
)
Assingments7: BinaryAssociation = BinaryAssociation(
    name="Assingments7",
    ends={
        Property(name="e2_Assingnment", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course8", type=e2_Assingnment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Lectures9: BinaryAssociation = BinaryAssociation(
    name="Lectures9",
    ends={
        Property(name="e2_Lecture11", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course10", type=e2_Lecture, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StudentGroups12: BinaryAssociation = BinaryAssociation(
    name="StudentGroups12",
    ends={
        Property(name="e2_Group", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course13", type=e2_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TeachingAssistant14: BinaryAssociation = BinaryAssociation(
    name="TeachingAssistant14",
    ends={
        Property(name="e2_Person16", type=e2_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_Course15", type=e2_Person, multiplicity=Multiplicity(0, 9999))
    }
)
assignment23: BinaryAssociation = BinaryAssociation(
    name="assignment23",
    ends={
        Property(name="e2_Assingnment25", type=e2_AssignmentSubmission, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_AssignmentSubmission24", type=e2_Assingnment, multiplicity=Multiplicity(1, 1))
    }
)
AssesedBy26: BinaryAssociation = BinaryAssociation(
    name="AssesedBy26",
    ends={
        Property(name="e2_Person28", type=e2_AssignmentSubmission, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_AssignmentSubmission27", type=e2_Person, multiplicity=Multiplicity(1, 1))
    }
)
Persons29: BinaryAssociation = BinaryAssociation(
    name="Persons29",
    ends={
        Property(name="e2_Person30", type=e2_University, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_University", type=e2_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Courses31: BinaryAssociation = BinaryAssociation(
    name="Courses31",
    ends={
        Property(name="e2_Course33", type=e2_University, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_University32", type=e2_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
LectureAssignment34: BinaryAssociation = BinaryAssociation(
    name="LectureAssignment34",
    ends={
        Property(name="e2_Assingnment36", type=e2_LectureContent, multiplicity=Multiplicity(1, 1)),
        Property(name="e2_LectureContent35", type=e2_Assingnment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="e2",
    types={e2_Lecture, e2_Course, e2_LectureContent, e2_Person, e2_AssignmentSubmission, e2_Assingnment, e2_Group, e2_University},
    associations={Students2, Content0, Submitted1, GroupMember17, Submitted20, Lecturerer4, Assingments7, Lectures9, StudentGroups12, TeachingAssistant14, assignment23, AssesedBy26, Persons29, Courses31, LectureAssignment34},
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