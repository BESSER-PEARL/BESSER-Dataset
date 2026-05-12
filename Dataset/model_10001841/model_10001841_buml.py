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
Administrator = Class(name="Administrator")
Teachers = Class(name="Teachers")
Students = Class(name="Students")
Department = Class(name="Department")
Course = Class(name="Course")
Team = Class(name="Team")
News_in_Dl = Class(name="News_in_Dl")
Training_materials_IITU = Class(name="Training_materials_IITU")
Schedule = Class(name="Schedule")
Library = Class(name="Library")
Questionnaire_survey = Class(name="Questionnaire_survey")
Moderator = Class(name="Moderator")
Dean = Class(name="Dean")
Other_employees = Class(name="Other_employees")

# Administrator class attributes and methods
Administrator_Name: Property = Property(name="Name", type=Administrator)
Administrator_Privilege: Property = Property(name="Privilege", type=StringType)
Administrator.attributes={Administrator_Privilege, Administrator_Name}

# Teachers class attributes and methods
Teachers_ID: Property = Property(name="ID", type=Teachers)
Teachers_Name: Property = Property(name="Name", type=StringType)
Teachers_Rank: Property = Property(name="Rank", type=Teachers)
Teachers_Department: Property = Property(name="Department", type=Department)
Teachers_Course: Property = Property(name="Course", type=Course)
Teachers_Info: Property = Property(name="Info", type=Teachers)
Teachers.attributes={Teachers_ID, Teachers_Rank, Teachers_Name, Teachers_Course, Teachers_Info, Teachers_Department}

# Students class attributes and methods
Students_ID: Property = Property(name="ID", type=Students)
Students_Name: Property = Property(name="Name", type=StringType)
Students_Course: Property = Property(name="Course", type=Course)
Students.attributes={Students_ID, Students_Course, Students_Name}

# Department class attributes and methods
Department_IS: Property = Property(name="IS", type=StringType)
Department_MCM: Property = Property(name="MCM", type=StringType)
Department_CSSE: Property = Property(name="CSSE", type=StringType)
Department_CS: Property = Property(name="CS", type=StringType)
Department_JUR: Property = Property(name="JUR", type=StringType)
Department_ITM: Property = Property(name="ITM", type=StringType)
Department.attributes={Department_IS, Department_JUR, Department_MCM, Department_ITM, Department_CS, Department_CSSE}

# Course class attributes and methods
Course__1_Course: Property = Property(name="_1_Course", type=Department)
Course__2_Course: Property = Property(name="_2_Course", type=Department)
Course__3_Course: Property = Property(name="_3_Course", type=Department)
Course__4_Course: Property = Property(name="_4_Course", type=Department)
Course.attributes={Course__4_Course, Course__3_Course, Course__2_Course, Course__1_Course}

# Team class attributes and methods
Team_Robotric_teams: Property = Property(name="Robotric_teams", type=Students)
Team_Footballs_teams: Property = Property(name="Footballs_teams", type=Students)
Team_Ministry: Property = Property(name="Ministry", type=StringType)
Team_President: Property = Property(name="President", type=StringType)
Team.attributes={Team_Ministry, Team_President, Team_Robotric_teams, Team_Footballs_teams}

# News_in_Dl class attributes and methods
News_in_Dl_Opens_news: Property = Property(name="Opens_news", type=Moderator)
News_in_Dl_Update_news: Property = Property(name="Update_news", type=Moderator)
News_in_Dl_Hyperlink: Property = Property(name="Hyperlink", type=StringType)
News_in_Dl.attributes={News_in_Dl_Update_news, News_in_Dl_Hyperlink, News_in_Dl_Opens_news}

# Training_materials_IITU class attributes and methods
Training_materials_IITU_Materials: Property = Property(name="Materials", type=StringType)
Training_materials_IITU.attributes={Training_materials_IITU_Materials}

# Schedule class attributes and methods
Schedule_Teacher: Property = Property(name="Teacher", type=Schedule)
Schedule_Course: Property = Property(name="Course", type=Schedule)
Schedule.attributes={Schedule_Teacher, Schedule_Course}

# Library class attributes and methods
Library_Books: Property = Property(name="Books", type=Library)
Library_Materials: Property = Property(name="Materials", type=Library)
Library.attributes={Library_Materials, Library_Books}

# Questionnaire_survey class attributes and methods
Questionnaire_survey_Teachers: Property = Property(name="Teachers", type=StringType)
Questionnaire_survey_Students: Property = Property(name="Students", type=StringType)
Questionnaire_survey.attributes={Questionnaire_survey_Teachers, Questionnaire_survey_Students}

# Moderator class attributes and methods
Moderator_Name: Property = Property(name="Name", type=Moderator)
Moderator.attributes={Moderator_Name}

# Dean class attributes and methods
Dean_Employees: Property = Property(name="Employees", type=Dean)
Dean.attributes={Dean_Employees}

# Other_employees class attributes and methods
Other_employees_Name: Property = Property(name="Name", type=StringType)
Other_employees_Position: Property = Property(name="Position", type=StringType)
Other_employees.attributes={Other_employees_Position, Other_employees_Name}

# Relationships
Course_Department: BinaryAssociation = BinaryAssociation(
    name="Course_Department",
    ends={
        Property(name="department0", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="course1", type=Course, multiplicity=Multiplicity(0, 1))
    }
)
Dean_News_in_Dl: BinaryAssociation = BinaryAssociation(
    name="Dean_News_in_Dl",
    ends={
        Property(name="news_in_Dl2", type=News_in_Dl, multiplicity=Multiplicity(0, 1)),
        Property(name="dean3", type=Dean, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Dean: BinaryAssociation = BinaryAssociation(
    name="Administrator_Dean",
    ends={
        Property(name="dean4", type=Dean, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator5", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Course: BinaryAssociation = BinaryAssociation(
    name="Administrator_Course",
    ends={
        Property(name="course6", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator7", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Teachers: BinaryAssociation = BinaryAssociation(
    name="Administrator_Teachers",
    ends={
        Property(name="teachers8", type=Teachers, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator9", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Moderator: BinaryAssociation = BinaryAssociation(
    name="Administrator_Moderator",
    ends={
        Property(name="moderator10", type=Moderator, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator11", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
Department_Students: BinaryAssociation = BinaryAssociation(
    name="Department_Students",
    ends={
        Property(name="students12", type=Students, multiplicity=Multiplicity(0, 1)),
        Property(name="department13", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Team_Students: BinaryAssociation = BinaryAssociation(
    name="Team_Students",
    ends={
        Property(name="students14", type=Students, multiplicity=Multiplicity(0, 1)),
        Property(name="team15", type=Team, multiplicity=Multiplicity(0, 1))
    }
)
Teachers_Students: BinaryAssociation = BinaryAssociation(
    name="Teachers_Students",
    ends={
        Property(name="students16", type=Students, multiplicity=Multiplicity(0, 1)),
        Property(name="teachers17", type=Teachers, multiplicity=Multiplicity(0, 1))
    }
)
Teachers_Schedule: BinaryAssociation = BinaryAssociation(
    name="Teachers_Schedule",
    ends={
        Property(name="schedule18", type=Schedule, multiplicity=Multiplicity(0, 1)),
        Property(name="teachers19", type=Teachers, multiplicity=Multiplicity(0, 1))
    }
)
Teachers_Course: BinaryAssociation = BinaryAssociation(
    name="Teachers_Course",
    ends={
        Property(name="course20", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="teachers21", type=Teachers, multiplicity=Multiplicity(0, 1))
    }
)
Course_Students: BinaryAssociation = BinaryAssociation(
    name="Course_Students",
    ends={
        Property(name="students22", type=Students, multiplicity=Multiplicity(0, 1)),
        Property(name="course23", type=Course, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ZnStkL_oEeeEXb8Dudo6PQ",
    types={Administrator, Teachers, Students, Department, Course, Team, News_in_Dl, Training_materials_IITU, Schedule, Library, Questionnaire_survey, Moderator, Dean, Other_employees},
    associations={Course_Department, Dean_News_in_Dl, Administrator_Dean, Administrator_Course, Administrator_Teachers, Administrator_Moderator, Department_Students, Team_Students, Teachers_Students, Teachers_Schedule, Teachers_Course, Course_Students},
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