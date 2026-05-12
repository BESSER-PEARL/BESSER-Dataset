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
research_team_Team = Class(name="research_team_Team")
research_team_ActivityReport = Class(name="research_team_ActivityReport")
research_team_Person = Class(name="research_team_Person")
research_team_OpenPosition = Class(name="research_team_OpenPosition")
research_team_Collaboration = Class(name="research_team_Collaboration")
research_team_Publication = Class(name="research_team_Publication")
research_team_Software = Class(name="research_team_Software")
research_team_Seminar = Class(name="research_team_Seminar")
research_team_Paper = Class(name="research_team_Paper")
research_team_Article = Class(name="research_team_Article")
Publication = Class(name="Publication")
research_team_MasterThesis = Class(name="research_team_MasterThesis")
research_team_Misc = Class(name="research_team_Misc")
research_team_PhDThesis = Class(name="research_team_PhDThesis")
research_team_InProceedings = Class(name="research_team_InProceedings")
research_team_Section = Class(name="research_team_Section")
research_team_CallForPaper = Class(name="research_team_CallForPaper")
research_team_Partner = Class(name="research_team_Partner")
research_team_TypeCollaboration = Class(name="research_team_TypeCollaboration")

# research_team_Team class attributes and methods
research_team_Team_name: Property = Property(name="name", type=StringType)
research_team_Team_meaning: Property = Property(name="meaning", type=StringType)
research_team_Team_status: Property = Property(name="status", type=StringType)
research_team_Team_urlPage: Property = Property(name="urlPage", type=StringType)
research_team_Team.attributes={research_team_Team_meaning, research_team_Team_name, research_team_Team_status, research_team_Team_urlPage}

# research_team_ActivityReport class attributes and methods

# research_team_Person class attributes and methods
research_team_Person_name: Property = Property(name="name", type=StringType)
research_team_Person_firstname: Property = Property(name="firstname", type=StringType)
research_team_Person_affiliation: Property = Property(name="affiliation", type=StringType)
research_team_Person_phone: Property = Property(name="phone", type=StringType)
research_team_Person_mail: Property = Property(name="mail", type=StringType)
research_team_Person.attributes={research_team_Person_phone, research_team_Person_firstname, research_team_Person_name, research_team_Person_mail, research_team_Person_affiliation}

# research_team_OpenPosition class attributes and methods
research_team_OpenPosition_status: Property = Property(name="status", type=StringType)
research_team_OpenPosition_mission: Property = Property(name="mission", type=StringType)
research_team_OpenPosition_duration: Property = Property(name="duration", type=StringType)
research_team_OpenPosition.attributes={research_team_OpenPosition_status, research_team_OpenPosition_mission, research_team_OpenPosition_duration}

# research_team_Collaboration class attributes and methods
research_team_Collaboration_website: Property = Property(name="website", type=StringType)
research_team_Collaboration_title: Property = Property(name="title", type=StringType)
research_team_Collaboration_status: Property = Property(name="status", type=StringType)
research_team_Collaboration_from_: Property = Property(name="from_", type=StringType)
research_team_Collaboration_until: Property = Property(name="until", type=StringType)
research_team_Collaboration.attributes={research_team_Collaboration_status, research_team_Collaboration_website, research_team_Collaboration_until, research_team_Collaboration_from_, research_team_Collaboration_title}

# research_team_Publication class attributes and methods
research_team_Publication_m_getBibtex: Method = Method(name="getBibtex", parameters={}, type=StringType)
research_team_Publication_m_getEndnote: Method = Method(name="getEndnote", parameters={}, type=StringType)
research_team_Publication.methods={research_team_Publication_m_getEndnote, research_team_Publication_m_getBibtex}

# research_team_Software class attributes and methods
research_team_Software_website: Property = Property(name="website", type=StringType)
research_team_Software_title: Property = Property(name="title", type=StringType)
research_team_Software_description: Property = Property(name="description", type=StringType)
research_team_Software.attributes={research_team_Software_description, research_team_Software_website, research_team_Software_title}

# research_team_Seminar class attributes and methods
research_team_Seminar_title: Property = Property(name="title", type=StringType)
research_team_Seminar_abstract: Property = Property(name="abstract", type=StringType)
research_team_Seminar_place: Property = Property(name="place", type=StringType)
research_team_Seminar_dateFrom: Property = Property(name="dateFrom", type=StringType)
research_team_Seminar_dateUntil: Property = Property(name="dateUntil", type=StringType)
research_team_Seminar_url4slides: Property = Property(name="url4slides", type=StringType)
research_team_Seminar.attributes={research_team_Seminar_abstract, research_team_Seminar_dateFrom, research_team_Seminar_dateUntil, research_team_Seminar_place, research_team_Seminar_url4slides, research_team_Seminar_title}

# research_team_Paper class attributes and methods
research_team_Paper_title: Property = Property(name="title", type=StringType)
research_team_Paper_url4pdf: Property = Property(name="url4pdf", type=StringType)
research_team_Paper_state: Property = Property(name="state", type=StringType)
research_team_Paper.attributes={research_team_Paper_title, research_team_Paper_state, research_team_Paper_url4pdf}

# research_team_Article class attributes and methods

# Publication class attributes and methods

# research_team_MasterThesis class attributes and methods

# research_team_Misc class attributes and methods

# research_team_PhDThesis class attributes and methods

# research_team_InProceedings class attributes and methods

# research_team_Section class attributes and methods
research_team_Section_text: Property = Property(name="text", type=StringType)
research_team_Section.attributes={research_team_Section_text}

# research_team_CallForPaper class attributes and methods
research_team_CallForPaper_title: Property = Property(name="title", type=StringType)
research_team_CallForPaper_category: Property = Property(name="category", type=StringType)
research_team_CallForPaper_deadline: Property = Property(name="deadline", type=StringType)
research_team_CallForPaper_url: Property = Property(name="url", type=StringType)
research_team_CallForPaper.attributes={research_team_CallForPaper_deadline, research_team_CallForPaper_title, research_team_CallForPaper_category, research_team_CallForPaper_url}

# research_team_Partner class attributes and methods
research_team_Partner_name: Property = Property(name="name", type=StringType)
research_team_Partner_country: Property = Property(name="country", type=StringType)
research_team_Partner_category: Property = Property(name="category", type=StringType)
research_team_Partner.attributes={research_team_Partner_name, research_team_Partner_category, research_team_Partner_country}

# research_team_TypeCollaboration class attributes and methods
research_team_TypeCollaboration_name: Property = Property(name="name", type=StringType)
research_team_TypeCollaboration.attributes={research_team_TypeCollaboration_name}

# Relationships
zero: BinaryAssociation = BinaryAssociation(
    name="0",
    ends={
        Property(name="research_team_ActivityReport", type=research_team_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="research_team_Team", type=research_team_ActivityReport, multiplicity=Multiplicity(0, 9999))
    }
)
members1: BinaryAssociation = BinaryAssociation(
    name="members1",
    ends={
        Property(name="research_team_Person", type=research_team_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="research_team_Team2", type=research_team_Person, multiplicity=Multiplicity(1, 9999))
    }
)
teamMaster3: BinaryAssociation = BinaryAssociation(
    name="teamMaster3",
    ends={
        Property(name="research_team_Person5", type=research_team_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="research_team_Team4", type=research_team_Person, multiplicity=Multiplicity(1, 1))
    }
)
openPosition6: BinaryAssociation = BinaryAssociation(
    name="openPosition6",
    ends={
        Property(name="research_team_OpenPosition", type=research_team_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="research_team_Team7", type=research_team_OpenPosition, multiplicity=Multiplicity(0, 9999))
    }
)
involvedIn8: BinaryAssociation = BinaryAssociation(
    name="involvedIn8",
    ends={
        Property(name="research_team_Collaboration", type=research_team_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="research_team_Team9", type=research_team_Collaboration, multiplicity=Multiplicity(0, 9999))
    }
)
mainReferences10: BinaryAssociation = BinaryAssociation(
    name="mainReferences10",
    ends={
        Property(name="Publication", type=research_team_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="team", type=research_team_Publication, multiplicity=Multiplicity(0, 9999))
    }
)
soft11: BinaryAssociation = BinaryAssociation(
    name="soft11",
    ends={
        Property(name="Software", type=research_team_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="developers", type=research_team_Software, multiplicity=Multiplicity(0, 9999))
    }
)
seminars12: BinaryAssociation = BinaryAssociation(
    name="seminars12",
    ends={
        Property(name="Seminar", type=research_team_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="speakers", type=research_team_Seminar, multiplicity=Multiplicity(0, 1))
    }
)
paper13: BinaryAssociation = BinaryAssociation(
    name="paper13",
    ends={
        Property(name="Paper", type=research_team_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=research_team_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
participates14: BinaryAssociation = BinaryAssociation(
    name="participates14",
    ends={
        Property(name="research_team_Collaboration16", type=research_team_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="research_team_Person15", type=research_team_Collaboration, multiplicity=Multiplicity(0, 9999))
    }
)
team17: BinaryAssociation = BinaryAssociation(
    name="team17",
    ends={
        Property(name="Team", type=research_team_Publication, multiplicity=Multiplicity(1, 1)),
        Property(name="mainReferences", type=research_team_Team, multiplicity=Multiplicity(0, 1))
    }
)
publishedAs18: BinaryAssociation = BinaryAssociation(
    name="publishedAs18",
    ends={
        Property(name="research_team_Paper", type=research_team_Publication, multiplicity=Multiplicity(1, 1)),
        Property(name="research_team_Publication", type=research_team_Paper, multiplicity=Multiplicity(1, 1))
    }
)
speakers19: BinaryAssociation = BinaryAssociation(
    name="speakers19",
    ends={
        Property(name="Person", type=research_team_Seminar, multiplicity=Multiplicity(1, 1)),
        Property(name="seminars", type=research_team_Person, multiplicity=Multiplicity(1, 9999))
    }
)
context20: BinaryAssociation = BinaryAssociation(
    name="context20",
    ends={
        Property(name="Collaboration", type=research_team_OpenPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="openPositions", type=research_team_Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
twentyone: BinaryAssociation = BinaryAssociation(
    name="21",
    ends={
        Property(name="Publication22", type=research_team_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publishedAs", type=research_team_Publication, multiplicity=Multiplicity(0, 9999))
    }
)
author23: BinaryAssociation = BinaryAssociation(
    name="author23",
    ends={
        Property(name="Person24", type=research_team_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research_team_Person, multiplicity=Multiplicity(1, 9999))
    }
)
developers25: BinaryAssociation = BinaryAssociation(
    name="developers25",
    ends={
        Property(name="Person26", type=research_team_Software, multiplicity=Multiplicity(1, 1)),
        Property(name="soft", type=research_team_Person, multiplicity=Multiplicity(1, 9999))
    }
)
collaboration27: BinaryAssociation = BinaryAssociation(
    name="collaboration27",
    ends={
        Property(name="Collaboration28", type=research_team_Partner, multiplicity=Multiplicity(1, 1)),
        Property(name="partners", type=research_team_Collaboration, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_research_team_Article_Publication = Generalization(general=Publication, specific=research_team_Article)
gen_research_team_MasterThesis_Publication = Generalization(general=Publication, specific=research_team_MasterThesis)
gen_research_team_Misc_Publication = Generalization(general=Publication, specific=research_team_Misc)
gen_research_team_PhDThesis_Publication = Generalization(general=Publication, specific=research_team_PhDThesis)
gen_research_team_InProceedings_Publication = Generalization(general=Publication, specific=research_team_InProceedings)

# Domain Model
domain_model = DomainModel(
    name="research_team",
    types={research_team_Team, research_team_ActivityReport, research_team_Person, research_team_OpenPosition, research_team_Collaboration, research_team_Publication, research_team_Software, research_team_Seminar, research_team_Paper, research_team_Article, Publication, research_team_MasterThesis, research_team_Misc, research_team_PhDThesis, research_team_InProceedings, research_team_Section, research_team_CallForPaper, research_team_Partner, research_team_TypeCollaboration},
    associations={zero, members1, teamMaster3, openPosition6, involvedIn8, mainReferences10, soft11, seminars12, paper13, participates14, team17, publishedAs18, speakers19, context20, twentyone, author23, developers25, collaboration27},
    generalizations={gen_research_team_Article_Publication, gen_research_team_MasterThesis_Publication, gen_research_team_Misc_Publication, gen_research_team_PhDThesis_Publication, gen_research_team_InProceedings_Publication},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)