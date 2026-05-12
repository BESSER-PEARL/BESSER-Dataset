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
Enum: Enumeration = Enumeration(
    name="Enum",
    literals={
            
    }
)

# Classes
User = Class(name="User")
Course = Class(name="Course")
Section = Class(name="Section")
Question = Class(name="Question", is_abstract=True)
TextQuestion = Class(name="TextQuestion")
ImageQuestion = Class(name="ImageQuestion")
SoundQuestion = Class(name="SoundQuestion")
Comment = Class(name="Comment")
Rating = Class(name="Rating")

# User class attributes and methods
User_nickname: Property = Property(name="nickname", type=StringType)
User_avatar: Property = Property(name="avatar", type=StringType)
User_level: Property = Property(name="level", type=IntegerType)
User_bio: Property = Property(name="bio", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User_links: Property = Property(name="links", type=StringType)
User.attributes={User_email, User_links, User_bio, User_avatar, User_nickname, User_level}

# Course class attributes and methods
Course_name: Property = Property(name="name", type=StringType)
Course_description: Property = Property(name="description", type=StringType)
Course_material: Property = Property(name="material", type=StringType)
Course.attributes={Course_description, Course_name, Course_material}

# Section class attributes and methods
Section_material: Property = Property(name="material", type=StringType)
Section.attributes={Section_material}

# Question class attributes and methods
Question_definition: Property = Property(name="definition", type=StringType)
Question_explanation: Property = Property(name="explanation", type=StringType)
Question.attributes={Question_definition, Question_explanation}

# TextQuestion class attributes and methods
TextQuestion_text: Property = Property(name="text", type=StringType)
TextQuestion_caseSensitive: Property = Property(name="caseSensitive", type=BooleanType)
TextQuestion.attributes={TextQuestion_caseSensitive, TextQuestion_text}

# ImageQuestion class attributes and methods
ImageQuestion_image: Property = Property(name="image", type=StringType)
ImageQuestion.attributes={ImageQuestion_image}

# SoundQuestion class attributes and methods
SoundQuestion_sound: Property = Property(name="sound", type=StringType)
SoundQuestion.attributes={SoundQuestion_sound}

# Comment class attributes and methods
Comment_subject: Property = Property(name="subject", type=StringType)
Comment_text: Property = Property(name="text", type=StringType)
Comment.attributes={Comment_text, Comment_subject}

# Rating class attributes and methods
Rating_value: Property = Property(name="value", type=IntegerType)
Rating_type: Property = Property(name="type", type=Enum)
Rating.attributes={Rating_type, Rating_value}

# Relationships
Section_Question: BinaryAssociation = BinaryAssociation(
    name="Section_Question",
    ends={
        Property(name="has_section0", type=Question, multiplicity=Multiplicity(0, 9999)),
        Property(name="has_question1", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
Section_Comment: BinaryAssociation = BinaryAssociation(
    name="Section_Comment",
    ends={
        Property(name="comments_section2", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="has_comments3", type=Section, multiplicity=Multiplicity(0, 1))
    }
)
Course_Section: BinaryAssociation = BinaryAssociation(
    name="Course_Section",
    ends={
        Property(name="has_course4", type=Section, multiplicity=Multiplicity(0, 9999)),
        Property(name="has_sections5", type=Course, multiplicity=Multiplicity(1, 1))
    }
)
Course_Comment: BinaryAssociation = BinaryAssociation(
    name="Course_Comment",
    ends={
        Property(name="comments_course6", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="has_comments7", type=Course, multiplicity=Multiplicity(0, 1))
    }
)
User_Comment: BinaryAssociation = BinaryAssociation(
    name="User_Comment",
    ends={
        Property(name="has_owner8", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="has_comments9", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Course: BinaryAssociation = BinaryAssociation(
    name="User_Course",
    ends={
        Property(name="has_users10", type=Course, multiplicity=Multiplicity(0, 9999)),
        Property(name="has_courses11", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
Rating_User: BinaryAssociation = BinaryAssociation(
    name="Rating_User",
    ends={
        Property(name="has_ratings12", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="has_owner13", type=Rating, multiplicity=Multiplicity(0, 9999))
    }
)
Rating_Course: BinaryAssociation = BinaryAssociation(
    name="Rating_Course",
    ends={
        Property(name="has_ratings14", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="rates_course15", type=Rating, multiplicity=Multiplicity(0, 9999))
    }
)
Rating_Comment: BinaryAssociation = BinaryAssociation(
    name="Rating_Comment",
    ends={
        Property(name="has_ratings16", type=Comment, multiplicity=Multiplicity(0, 1)),
        Property(name="rates_comment17", type=Rating, multiplicity=Multiplicity(0, 9999))
    }
)
Course_User: BinaryAssociation = BinaryAssociation(
    name="Course_User",
    ends={
        Property(name="owns18", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="has_owner19", type=Course, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_uQJeUBiEEeizPrac7I6KfQ",
    types={User, Course, Section, Question, TextQuestion, ImageQuestion, SoundQuestion, Comment, Rating, Enum},
    associations={Section_Question, Section_Comment, Course_Section, Course_Comment, User_Comment, User_Course, Rating_User, Rating_Course, Rating_Comment, Course_User},
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