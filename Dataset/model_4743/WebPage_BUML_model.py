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
VisualRepresentation: Enumeration = Enumeration(
    name="VisualRepresentation",
    literals={
            EnumerationLiteral(name="BAR_CHART"),
			EnumerationLiteral(name="LINEAL_CHART"),
			EnumerationLiteral(name="PIE_CHART"),
			EnumerationLiteral(name="TEXTUAL")
    }
)

MySqlType: Enumeration = Enumeration(
    name="MySqlType",
    literals={
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="VARCHAR")
    }
)

CorrectAnwser: Enumeration = Enumeration(
    name="CorrectAnwser",
    literals={
            EnumerationLiteral(name="True"),
			EnumerationLiteral(name="False")
    }
)

# Classes
WebApp_Entity = Class(name="WebApp::Entity")
WebApp_Opened = Class(name="WebApp::Opened")
SimpleQuestion = Class(name="SimpleQuestion")
WebApp_PageS_Q = Class(name="WebApp::PageS::Q", is_abstract=True)
WebPage = Class(name="WebPage")
WebApp_Question = Class(name="WebApp::Question", is_abstract=True)
WebApp_Survey = Class(name="WebApp::Survey")
PageS_Q = Class(name="PageS::Q")
WebApp_WebApp = Class(name="WebApp::WebApp")
WebApp_WebPage = Class(name="WebApp::WebPage", is_abstract=True)
WebApp_DataBase = Class(name="WebApp::DataBase")
WebApp_QuestionBank = Class(name="WebApp::QuestionBank")
WebApp_Attribute = Class(name="WebApp::Attribute")
WebApp_Create = Class(name="WebApp::Create")
WebApp_Delete = Class(name="WebApp::Delete")
WebApp_CRUD = Class(name="WebApp::CRUD")
WebApp_Option = Class(name="WebApp::Option")
WebApp_Questionnary = Class(name="WebApp::Questionnary")
WebApp_ExternalSource = Class(name="WebApp::ExternalSource", is_abstract=True)
WebApp_ExternalLink = Class(name="WebApp::ExternalLink")
WebApp_Home = Class(name="WebApp::Home")
WebApp_Index = Class(name="WebApp::Index")
EntityWebPage = Class(name="EntityWebPage")
WebApp_Details = Class(name="WebApp::Details")
WebApp_SimpleQuestion = Class(name="WebApp::SimpleQuestion", is_abstract=True)
WebApp_EntityWebPage = Class(name="WebApp::EntityWebPage", is_abstract=True)
WebApp_TrueFalseForSurvey = Class(name="WebApp::TrueFalseForSurvey")
TrueFalse = Class(name="TrueFalse")
WebApp_GroupOfQuestions = Class(name="WebApp::GroupOfQuestions")
Question = Class(name="Question")
WebApp_Multiple = Class(name="WebApp::Multiple", is_abstract=True)
WebApp_TrueFalse = Class(name="WebApp::TrueFalse", is_abstract=True)
WebApp_MultipleForSurvey = Class(name="WebApp::MultipleForSurvey")
Multiple = Class(name="Multiple")
WebApp_TrueFalseForQuestionnary = Class(name="WebApp::TrueFalseForQuestionnary")
WebApp_MultipleForQuestionnary = Class(name="WebApp::MultipleForQuestionnary")
WebApp_Twitter = Class(name="WebApp::Twitter")
ExternalSource = Class(name="ExternalSource")
WebApp_RSSFeed = Class(name="WebApp::RSSFeed")

# WebApp_Entity class attributes and methods
WebApp_Entity_name: Property = Property(name="name", type=StringType)
WebApp_Entity.attributes={WebApp_Entity_name}

# WebApp_Opened class attributes and methods

# SimpleQuestion class attributes and methods

# WebApp_PageS_Q class attributes and methods

# WebPage class attributes and methods

# WebApp_Question class attributes and methods

# WebApp_Survey class attributes and methods

# PageS_Q class attributes and methods

# WebApp_WebApp class attributes and methods
WebApp_WebApp_name: Property = Property(name="name", type=StringType)
WebApp_WebApp_User: Property = Property(name="User", type=StringType)
WebApp_WebApp_Password: Property = Property(name="Password", type=StringType)
WebApp_WebApp.attributes={WebApp_WebApp_User, WebApp_WebApp_Password, WebApp_WebApp_name}

# WebApp_WebPage class attributes and methods
WebApp_WebPage_name: Property = Property(name="name", type=StringType)
WebApp_WebPage.attributes={WebApp_WebPage_name}

# WebApp_DataBase class attributes and methods

# WebApp_QuestionBank class attributes and methods

# WebApp_Attribute class attributes and methods
WebApp_Attribute_name: Property = Property(name="name", type=StringType)
WebApp_Attribute_type: Property = Property(name="type", type=StringType)
WebApp_Attribute.attributes={WebApp_Attribute_name, WebApp_Attribute_type}

# WebApp_Create class attributes and methods

# WebApp_Delete class attributes and methods

# WebApp_CRUD class attributes and methods

# WebApp_Option class attributes and methods
WebApp_Option_text: Property = Property(name="text", type=StringType)
WebApp_Option_fraction: Property = Property(name="fraction", type=IntegerType)
WebApp_Option.attributes={WebApp_Option_fraction, WebApp_Option_text}

# WebApp_Questionnary class attributes and methods
WebApp_Questionnary_feedback: Property = Property(name="feedback", type=BooleanType)
WebApp_Questionnary.attributes={WebApp_Questionnary_feedback}

# WebApp_ExternalSource class attributes and methods

# WebApp_ExternalLink class attributes and methods
WebApp_ExternalLink_url: Property = Property(name="url", type=StringType)
WebApp_ExternalLink.attributes={WebApp_ExternalLink_url}

# WebApp_Home class attributes and methods

# WebApp_Index class attributes and methods

# EntityWebPage class attributes and methods

# WebApp_Details class attributes and methods

# WebApp_SimpleQuestion class attributes and methods
WebApp_SimpleQuestion_QuestionText: Property = Property(name="QuestionText", type=StringType)
WebApp_SimpleQuestion_visualRep: Property = Property(name="visualRep", type=StringType)
WebApp_SimpleQuestion.attributes={WebApp_SimpleQuestion_QuestionText, WebApp_SimpleQuestion_visualRep}

# WebApp_EntityWebPage class attributes and methods

# WebApp_TrueFalseForSurvey class attributes and methods

# TrueFalse class attributes and methods

# WebApp_GroupOfQuestions class attributes and methods
WebApp_GroupOfQuestions_name: Property = Property(name="name", type=StringType)
WebApp_GroupOfQuestions.attributes={WebApp_GroupOfQuestions_name}

# Question class attributes and methods

# WebApp_Multiple class attributes and methods

# WebApp_TrueFalse class attributes and methods

# WebApp_MultipleForSurvey class attributes and methods

# Multiple class attributes and methods

# WebApp_TrueFalseForQuestionnary class attributes and methods
WebApp_TrueFalseForQuestionnary_correct: Property = Property(name="correct", type=StringType)
WebApp_TrueFalseForQuestionnary.attributes={WebApp_TrueFalseForQuestionnary_correct}

# WebApp_MultipleForQuestionnary class attributes and methods

# WebApp_Twitter class attributes and methods
WebApp_Twitter_username: Property = Property(name="username", type=StringType)
WebApp_Twitter.attributes={WebApp_Twitter_username}

# ExternalSource class attributes and methods

# WebApp_RSSFeed class attributes and methods
WebApp_RSSFeed_url: Property = Property(name="url", type=StringType)
WebApp_RSSFeed_items_to_display: Property = Property(name="items_to_display", type=IntegerType)
WebApp_RSSFeed_show_date: Property = Property(name="show_date", type=StringType)
WebApp_RSSFeed_feedname: Property = Property(name="feedname", type=StringType)
WebApp_RSSFeed.attributes={WebApp_RSSFeed_url, WebApp_RSSFeed_items_to_display, WebApp_RSSFeed_feedname, WebApp_RSSFeed_show_date}

# Relationships
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="WebApp_Attribute", type=WebApp_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Entity", type=WebApp_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entityReference7: BinaryAssociation = BinaryAssociation(
    name="entityReference7",
    ends={
        Property(name="WebApp_Entity8", type=WebApp_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Entity6", type=WebApp_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
question9: BinaryAssociation = BinaryAssociation(
    name="question9",
    ends={
        Property(name="WebApp_Question", type=WebApp_PageS_Q, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_PageS_Q", type=WebApp_Question, multiplicity=Multiplicity(1, 9999))
    }
)
webpages0: BinaryAssociation = BinaryAssociation(
    name="webpages0",
    ends={
        Property(name="WebApp_WebPage", type=WebApp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_WebApp", type=WebApp_WebPage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
database1: BinaryAssociation = BinaryAssociation(
    name="database1",
    ends={
        Property(name="WebApp_DataBase", type=WebApp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_WebApp2", type=WebApp_DataBase, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
questionbank3: BinaryAssociation = BinaryAssociation(
    name="questionbank3",
    ends={
        Property(name="WebApp_QuestionBank", type=WebApp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_WebApp4", type=WebApp_QuestionBank, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
socialnetwork10: BinaryAssociation = BinaryAssociation(
    name="socialnetwork10",
    ends={
        Property(name="WebApp_ExternalSource", type=WebApp_WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_WebPage11", type=WebApp_ExternalSource, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
internallink13: BinaryAssociation = BinaryAssociation(
    name="internallink13",
    ends={
        Property(name="WebApp_WebPage14", type=WebApp_WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_WebPage12", type=WebApp_WebPage, multiplicity=Multiplicity(0, 9999))
    }
)
externallinks15: BinaryAssociation = BinaryAssociation(
    name="externallinks15",
    ends={
        Property(name="WebApp_ExternalLink", type=WebApp_WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_WebPage16", type=WebApp_ExternalLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity20: BinaryAssociation = BinaryAssociation(
    name="entity20",
    ends={
        Property(name="WebApp_Entity21", type=WebApp_EntityWebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_EntityWebPage", type=WebApp_Entity, multiplicity=Multiplicity(1, 1))
    }
)
entities22: BinaryAssociation = BinaryAssociation(
    name="entities22",
    ends={
        Property(name="WebApp_Entity24", type=WebApp_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_DataBase23", type=WebApp_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
quiestions25: BinaryAssociation = BinaryAssociation(
    name="quiestions25",
    ends={
        Property(name="WebApp_Question27", type=WebApp_QuestionBank, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_QuestionBank26", type=WebApp_Question, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
questions17: BinaryAssociation = BinaryAssociation(
    name="questions17",
    ends={
        Property(name="WebApp_Question18", type=WebApp_GroupOfQuestions, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_GroupOfQuestions", type=WebApp_Question, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
option19: BinaryAssociation = BinaryAssociation(
    name="option19",
    ends={
        Property(name="WebApp_Option", type=WebApp_Multiple, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Multiple", type=WebApp_Option, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
correctOption28: BinaryAssociation = BinaryAssociation(
    name="correctOption28",
    ends={
        Property(name="WebApp_Option29", type=WebApp_MultipleForQuestionnary, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_MultipleForQuestionnary", type=WebApp_Option, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_WebApp_Opened_SimpleQuestion = Generalization(general=SimpleQuestion, specific=WebApp_Opened)
gen_WebApp_PageS_Q_WebPage = Generalization(general=WebPage, specific=WebApp_PageS_Q)
gen_WebApp_Survey_PageS_Q = Generalization(general=PageS_Q, specific=WebApp_Survey)
gen_WebApp_Create_EntityWebPage = Generalization(general=EntityWebPage, specific=WebApp_Create)
gen_WebApp_Delete_EntityWebPage = Generalization(general=EntityWebPage, specific=WebApp_Delete)
gen_WebApp_CRUD_EntityWebPage = Generalization(general=EntityWebPage, specific=WebApp_CRUD)
gen_WebApp_Questionnary_PageS_Q = Generalization(general=PageS_Q, specific=WebApp_Questionnary)
gen_WebApp_Home_WebPage = Generalization(general=WebPage, specific=WebApp_Home)
gen_WebApp_Index_EntityWebPage = Generalization(general=EntityWebPage, specific=WebApp_Index)
gen_WebApp_Details_EntityWebPage = Generalization(general=EntityWebPage, specific=WebApp_Details)
gen_WebApp_SimpleQuestion_Question = Generalization(general=Question, specific=WebApp_SimpleQuestion)
gen_WebApp_EntityWebPage_WebPage = Generalization(general=WebPage, specific=WebApp_EntityWebPage)
gen_WebApp_TrueFalseForSurvey_TrueFalse = Generalization(general=TrueFalse, specific=WebApp_TrueFalseForSurvey)
gen_WebApp_GroupOfQuestions_Question = Generalization(general=Question, specific=WebApp_GroupOfQuestions)
gen_WebApp_Multiple_SimpleQuestion = Generalization(general=SimpleQuestion, specific=WebApp_Multiple)
gen_WebApp_TrueFalse_SimpleQuestion = Generalization(general=SimpleQuestion, specific=WebApp_TrueFalse)
gen_WebApp_MultipleForSurvey_Multiple = Generalization(general=Multiple, specific=WebApp_MultipleForSurvey)
gen_WebApp_TrueFalseForQuestionnary_TrueFalse = Generalization(general=TrueFalse, specific=WebApp_TrueFalseForQuestionnary)
gen_WebApp_MultipleForQuestionnary_Multiple = Generalization(general=Multiple, specific=WebApp_MultipleForQuestionnary)
gen_WebApp_Twitter_ExternalSource = Generalization(general=ExternalSource, specific=WebApp_Twitter)
gen_WebApp_RSSFeed_ExternalSource = Generalization(general=ExternalSource, specific=WebApp_RSSFeed)

# Domain Model
domain_model = DomainModel(
    name="WebApp",
    types={WebApp_Entity, WebApp_Opened, SimpleQuestion, WebApp_PageS_Q, WebPage, WebApp_Question, WebApp_Survey, PageS_Q, WebApp_WebApp, WebApp_WebPage, WebApp_DataBase, WebApp_QuestionBank, WebApp_Attribute, WebApp_Create, WebApp_Delete, WebApp_CRUD, WebApp_Option, WebApp_Questionnary, WebApp_ExternalSource, WebApp_ExternalLink, WebApp_Home, WebApp_Index, EntityWebPage, WebApp_Details, WebApp_SimpleQuestion, WebApp_EntityWebPage, WebApp_TrueFalseForSurvey, TrueFalse, WebApp_GroupOfQuestions, Question, WebApp_Multiple, WebApp_TrueFalse, WebApp_MultipleForSurvey, Multiple, WebApp_TrueFalseForQuestionnary, WebApp_MultipleForQuestionnary, WebApp_Twitter, ExternalSource, WebApp_RSSFeed, VisualRepresentation, MySqlType, CorrectAnwser},
    associations={attributes5, entityReference7, question9, webpages0, database1, questionbank3, socialnetwork10, internallink13, externallinks15, entity20, entities22, quiestions25, questions17, option19, correctOption28},
    generalizations={gen_WebApp_Opened_SimpleQuestion, gen_WebApp_PageS_Q_WebPage, gen_WebApp_Survey_PageS_Q, gen_WebApp_Create_EntityWebPage, gen_WebApp_Delete_EntityWebPage, gen_WebApp_CRUD_EntityWebPage, gen_WebApp_Questionnary_PageS_Q, gen_WebApp_Home_WebPage, gen_WebApp_Index_EntityWebPage, gen_WebApp_Details_EntityWebPage, gen_WebApp_SimpleQuestion_Question, gen_WebApp_EntityWebPage_WebPage, gen_WebApp_TrueFalseForSurvey_TrueFalse, gen_WebApp_GroupOfQuestions_Question, gen_WebApp_Multiple_SimpleQuestion, gen_WebApp_TrueFalse_SimpleQuestion, gen_WebApp_MultipleForSurvey_Multiple, gen_WebApp_TrueFalseForQuestionnary_TrueFalse, gen_WebApp_MultipleForQuestionnary_Multiple, gen_WebApp_Twitter_ExternalSource, gen_WebApp_RSSFeed_ExternalSource},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)