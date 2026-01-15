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
research2_Write = Class(name="research2::Write")
research2_Review = Class(name="research2::Review")
research2_PublicationProcess = Class(name="research2::PublicationProcess")
Named = Class(name="Named")
research2_Phase = Class(name="research2::Phase")
research2_Researcher = Class(name="research2::Researcher")
research2_Paragraph = Class(name="research2::Paragraph")
research2_Progress = Class(name="research2::Progress")
research2_Paper = Class(name="research2::Paper")
research2_Skill = Class(name="research2::Skill")
research2_Position = Class(name="research2::Position")
Labelled = Class(name="Labelled")
research2_Keyword = Class(name="research2::Keyword")
Counted = Class(name="Counted")
research2_ReviewNote = Class(name="research2::ReviewNote")
research2_PublicationStructure = Class(name="research2::PublicationStructure")
research2_Named = Class(name="research2::Named", is_abstract=True)
research2_KnowledgeManager = Class(name="research2::KnowledgeManager")
research2_PublicationSystem = Class(name="research2::PublicationSystem")
research2_Counted = Class(name="research2::Counted", is_abstract=True)
research2_Labelled = Class(name="research2::Labelled", is_abstract=True)

# research2_Write class attributes and methods
research2_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research2_Write.attributes={research2_Write_timeSpent}

# research2_Review class attributes and methods
research2_Review_date: Property = Property(name="date", type=DateType)
research2_Review.attributes={research2_Review_date}

# research2_PublicationProcess class attributes and methods
research2_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research2_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research2_PublicationProcess.attributes={research2_PublicationProcess_maxTime, research2_PublicationProcess_minTime}

# Named class attributes and methods

# research2_Phase class attributes and methods
research2_Phase_name: Property = Property(name="name", type=StringType)
research2_Phase.attributes={research2_Phase_name}

# research2_Researcher class attributes and methods
research2_Researcher_name: Property = Property(name="name", type=StringType)
research2_Researcher_forName: Property = Property(name="forName", type=StringType)
research2_Researcher.attributes={research2_Researcher_name, research2_Researcher_forName}

# research2_Paragraph class attributes and methods
research2_Paragraph_content: Property = Property(name="content", type=StringType)
research2_Paragraph.attributes={research2_Paragraph_content}

# research2_Progress class attributes and methods
research2_Progress_percent: Property = Property(name="percent", type=IntegerType)
research2_Progress.attributes={research2_Progress_percent}

# research2_Paper class attributes and methods

# research2_Skill class attributes and methods
research2_Skill_description: Property = Property(name="description", type=StringType)
research2_Skill.attributes={research2_Skill_description}

# research2_Position class attributes and methods
research2_Position_description: Property = Property(name="description", type=StringType)
research2_Position.attributes={research2_Position_description}

# Labelled class attributes and methods

# research2_Keyword class attributes and methods
research2_Keyword_description: Property = Property(name="description", type=StringType)
research2_Keyword.attributes={research2_Keyword_description}

# Counted class attributes and methods

# research2_ReviewNote class attributes and methods
research2_ReviewNote_content: Property = Property(name="content", type=StringType)
research2_ReviewNote.attributes={research2_ReviewNote_content}

# research2_PublicationStructure class attributes and methods

# research2_Named class attributes and methods
research2_Named_name: Property = Property(name="name", type=StringType)
research2_Named.attributes={research2_Named_name}

# research2_KnowledgeManager class attributes and methods

# research2_PublicationSystem class attributes and methods

# research2_Counted class attributes and methods
research2_Counted_id: Property = Property(name="id", type=IntegerType)
research2_Counted.attributes={research2_Counted_id}

# research2_Labelled class attributes and methods
research2_Labelled_lname: Property = Property(name="lname", type=StringType)
research2_Labelled.attributes={research2_Labelled_lname}

# Relationships
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research2_Write", type=research2_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Researcher", type=research2_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research2_Review", type=research2_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Researcher3", type=research2_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research2_Phase", type=research2_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_PublicationProcess", type=research2_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs9: BinaryAssociation = BinaryAssociation(
    name="paragraphs9",
    ends={
        Property(name="research2_Paragraph", type=research2_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Paper", type=research2_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress10: BinaryAssociation = BinaryAssociation(
    name="progress10",
    ends={
        Property(name="Progress", type=research2_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research2_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors11: BinaryAssociation = BinaryAssociation(
    name="authors11",
    ends={
        Property(name="Researcher", type=research2_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research2_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research2_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research2_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research2_Skill", type=research2_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Researcher6", type=research2_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research2_Position", type=research2_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Researcher8", type=research2_Position, multiplicity=Multiplicity(0, 1))
    }
)
keywords12: BinaryAssociation = BinaryAssociation(
    name="keywords12",
    ends={
        Property(name="Keyword", type=research2_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="kpapers", type=research2_Keyword, multiplicity=Multiplicity(0, 9999))
    }
)
citedBy14: BinaryAssociation = BinaryAssociation(
    name="citedBy14",
    ends={
        Property(name="research2_Paper15", type=research2_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Paper13", type=research2_Paper, multiplicity=Multiplicity(0, 1))
    }
)
reviews16: BinaryAssociation = BinaryAssociation(
    name="reviews16",
    ends={
        Property(name="research2_ReviewNote", type=research2_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Paragraph17", type=research2_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviewNote25: BinaryAssociation = BinaryAssociation(
    name="reviewNote25",
    ends={
        Property(name="research2_ReviewNote27", type=research2_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Review26", type=research2_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
process18: BinaryAssociation = BinaryAssociation(
    name="process18",
    ends={
        Property(name="research2_PublicationProcess19", type=research2_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Progress", type=research2_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper20: BinaryAssociation = BinaryAssociation(
    name="paper20",
    ends={
        Property(name="Paper21", type=research2_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research2_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph22: BinaryAssociation = BinaryAssociation(
    name="paragraph22",
    ends={
        Property(name="research2_Paragraph24", type=research2_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Write23", type=research2_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
processView35: BinaryAssociation = BinaryAssociation(
    name="processView35",
    ends={
        Property(name="research2_PublicationSystem", type=research2_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="research2_PublicationProcess36", type=research2_PublicationSystem, multiplicity=Multiplicity(1, 1))
    }
)
structuralView37: BinaryAssociation = BinaryAssociation(
    name="structuralView37",
    ends={
        Property(name="research2_PublicationStructure39", type=research2_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_PublicationSystem38", type=research2_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions40: BinaryAssociation = BinaryAssociation(
    name="positions40",
    ends={
        Property(name="research2_Position42", type=research2_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_PublicationSystem41", type=research2_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
researchers28: BinaryAssociation = BinaryAssociation(
    name="researchers28",
    ends={
        Property(name="research2_Researcher29", type=research2_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_PublicationStructure", type=research2_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers30: BinaryAssociation = BinaryAssociation(
    name="papers30",
    ends={
        Property(name="research2_Paper32", type=research2_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_PublicationStructure31", type=research2_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan33: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan33",
    ends={
        Property(name="research2_KnowledgeManager", type=research2_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_PublicationStructure34", type=research2_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent44: BinaryAssociation = BinaryAssociation(
    name="parent44",
    ends={
        Property(name="research2_Position45", type=research2_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_Position43", type=research2_Position, multiplicity=Multiplicity(0, 1))
    }
)
kpapers46: BinaryAssociation = BinaryAssociation(
    name="kpapers46",
    ends={
        Property(name="Paper47", type=research2_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="keywords", type=research2_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
allkeywords48: BinaryAssociation = BinaryAssociation(
    name="allkeywords48",
    ends={
        Property(name="research2_Keyword", type=research2_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research2_KnowledgeManager49", type=research2_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_research2_PublicationProcess_Named = Generalization(general=Named, specific=research2_PublicationProcess)
gen_research2_Paper_Named = Generalization(general=Named, specific=research2_Paper)
gen_research2_ReviewNote_Named = Generalization(general=Named, specific=research2_ReviewNote)
gen_research2_Progress_Labelled = Generalization(general=Labelled, specific=research2_Progress)
gen_research2_Paragraph_Counted = Generalization(general=Counted, specific=research2_Paragraph)
gen_research2_Paragraph_Named = Generalization(general=Named, specific=research2_Paragraph)
gen_research2_PublicationStructure_Named = Generalization(general=Named, specific=research2_PublicationStructure)
gen_research2_Write_Labelled = Generalization(general=Labelled, specific=research2_Write)
gen_research2_Review_Labelled = Generalization(general=Labelled, specific=research2_Review)
gen_research2_PublicationSystem_Named = Generalization(general=Named, specific=research2_PublicationSystem)
gen_research2_Position_Named = Generalization(general=Named, specific=research2_Position)
gen_research2_Keyword_Named = Generalization(general=Named, specific=research2_Keyword)
gen_research2_KnowledgeManager_Named = Generalization(general=Named, specific=research2_KnowledgeManager)

# Domain Model
domain_model = DomainModel(
    name="research2",
    types={research2_Write, research2_Review, research2_PublicationProcess, Named, research2_Phase, research2_Researcher, research2_Paragraph, research2_Progress, research2_Paper, research2_Skill, research2_Position, Labelled, research2_Keyword, Counted, research2_ReviewNote, research2_PublicationStructure, research2_Named, research2_KnowledgeManager, research2_PublicationSystem, research2_Counted, research2_Labelled},
    associations={writes1, reviews2, phases0, paragraphs9, progress10, authors11, res_papers4, skills5, res_position7, keywords12, citedBy14, reviews16, reviewNote25, process18, paper20, paragraph22, processView35, structuralView37, positions40, researchers28, papers30, knowledgeMan33, parent44, kpapers46, allkeywords48},
    generalizations={gen_research2_PublicationProcess_Named, gen_research2_Paper_Named, gen_research2_ReviewNote_Named, gen_research2_Progress_Labelled, gen_research2_Paragraph_Counted, gen_research2_Paragraph_Named, gen_research2_PublicationStructure_Named, gen_research2_Write_Labelled, gen_research2_Review_Labelled, gen_research2_PublicationSystem_Named, gen_research2_Position_Named, gen_research2_Keyword_Named, gen_research2_KnowledgeManager_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)