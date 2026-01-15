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
research_Researcher = Class(name="research::Researcher")
research_Write = Class(name="research::Write")
research_Review = Class(name="research::Review")
research_PublicationProcess = Class(name="research::PublicationProcess")
Named = Class(name="Named")
research_Phase = Class(name="research::Phase")
research_Paragraph = Class(name="research::Paragraph")
research_Progress = Class(name="research::Progress")
research_PaperKeyword = Class(name="research::PaperKeyword")
research_Paper = Class(name="research::Paper")
research_Skill = Class(name="research::Skill")
research_Position = Class(name="research::Position")
research_Collaboration = Class(name="research::Collaboration")
Labelled = Class(name="Labelled")
Counted = Class(name="Counted")
research_ReviewNote = Class(name="research::ReviewNote")
research_PublicationStructure = Class(name="research::PublicationStructure")
research_KnowledgeManager = Class(name="research::KnowledgeManager")
research_PublicationSystem = Class(name="research::PublicationSystem")
research_Named = Class(name="research::Named", is_abstract=True)
research_Labelled = Class(name="research::Labelled", is_abstract=True)
research_Counted = Class(name="research::Counted", is_abstract=True)
research_Keyword = Class(name="research::Keyword")

# research_Researcher class attributes and methods
research_Researcher_name: Property = Property(name="name", type=StringType)
research_Researcher_forName: Property = Property(name="forName", type=StringType)
research_Researcher.attributes={research_Researcher_forName, research_Researcher_name}

# research_Write class attributes and methods
research_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research_Write.attributes={research_Write_timeSpent}

# research_Review class attributes and methods
research_Review_date: Property = Property(name="date", type=DateType)
research_Review.attributes={research_Review_date}

# research_PublicationProcess class attributes and methods
research_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research_PublicationProcess.attributes={research_PublicationProcess_minTime, research_PublicationProcess_maxTime}

# Named class attributes and methods

# research_Phase class attributes and methods
research_Phase_name: Property = Property(name="name", type=StringType)
research_Phase.attributes={research_Phase_name}

# research_Paragraph class attributes and methods
research_Paragraph_content: Property = Property(name="content", type=StringType)
research_Paragraph.attributes={research_Paragraph_content}

# research_Progress class attributes and methods
research_Progress_percent: Property = Property(name="percent", type=IntegerType)
research_Progress.attributes={research_Progress_percent}

# research_PaperKeyword class attributes and methods
research_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research_PaperKeyword.attributes={research_PaperKeyword_weight}

# research_Paper class attributes and methods

# research_Skill class attributes and methods
research_Skill_description: Property = Property(name="description", type=StringType)
research_Skill.attributes={research_Skill_description}

# research_Position class attributes and methods
research_Position_description: Property = Property(name="description", type=StringType)
research_Position.attributes={research_Position_description}

# research_Collaboration class attributes and methods
research_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research_Collaboration.attributes={research_Collaboration_ratio}

# Labelled class attributes and methods

# Counted class attributes and methods

# research_ReviewNote class attributes and methods
research_ReviewNote_content: Property = Property(name="content", type=StringType)
research_ReviewNote.attributes={research_ReviewNote_content}

# research_PublicationStructure class attributes and methods

# research_KnowledgeManager class attributes and methods

# research_PublicationSystem class attributes and methods

# research_Named class attributes and methods
research_Named_name: Property = Property(name="name", type=StringType)
research_Named.attributes={research_Named_name}

# research_Labelled class attributes and methods
research_Labelled_lname: Property = Property(name="lname", type=StringType)
research_Labelled.attributes={research_Labelled_lname}

# research_Counted class attributes and methods
research_Counted_id: Property = Property(name="id", type=IntegerType)
research_Counted.attributes={research_Counted_id}

# research_Keyword class attributes and methods
research_Keyword_description: Property = Property(name="description", type=StringType)
research_Keyword.attributes={research_Keyword_description}

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research_PublicationProcess", type=research_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="research_Phase", type=research_PublicationProcess, multiplicity=Multiplicity(1, 1))
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research_Write", type=research_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Researcher", type=research_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research_Review", type=research_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Researcher3", type=research_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research_Paragraph", type=research_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Paper", type=research_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research_PaperKeyword", type=research_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Paper15", type=research_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research_Paper18", type=research_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Paper16", type=research_Paper, multiplicity=Multiplicity(0, 1))
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research_Skill", type=research_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Researcher6", type=research_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research_Position", type=research_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Researcher8", type=research_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research_Collaboration", type=research_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Researcher10", type=research_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process21: BinaryAssociation = BinaryAssociation(
    name="process21",
    ends={
        Property(name="research_PublicationProcess22", type=research_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Progress", type=research_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
reviews19: BinaryAssociation = BinaryAssociation(
    name="reviews19",
    ends={
        Property(name="research_ReviewNote", type=research_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Paragraph20", type=research_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph25: BinaryAssociation = BinaryAssociation(
    name="paragraph25",
    ends={
        Property(name="research_Paragraph27", type=research_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Write26", type=research_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
paper23: BinaryAssociation = BinaryAssociation(
    name="paper23",
    ends={
        Property(name="Paper24", type=research_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research_Paper, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote28: BinaryAssociation = BinaryAssociation(
    name="reviewNote28",
    ends={
        Property(name="research_ReviewNote30", type=research_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Review29", type=research_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
researchers31: BinaryAssociation = BinaryAssociation(
    name="researchers31",
    ends={
        Property(name="research_Researcher32", type=research_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research_PublicationStructure", type=research_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers33: BinaryAssociation = BinaryAssociation(
    name="papers33",
    ends={
        Property(name="research_Paper35", type=research_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research_PublicationStructure34", type=research_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processView38: BinaryAssociation = BinaryAssociation(
    name="processView38",
    ends={
        Property(name="research_PublicationProcess39", type=research_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research_PublicationSystem", type=research_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView40: BinaryAssociation = BinaryAssociation(
    name="structuralView40",
    ends={
        Property(name="research_PublicationStructure42", type=research_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research_PublicationSystem41", type=research_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
knowledgeMan36: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan36",
    ends={
        Property(name="research_KnowledgeManager", type=research_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research_PublicationStructure37", type=research_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions43: BinaryAssociation = BinaryAssociation(
    name="positions43",
    ends={
        Property(name="research_PublicationSystem44", type=research_Position, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="research_Position45", type=research_PublicationSystem, multiplicity=Multiplicity(1, 1))
    }
)
parent47: BinaryAssociation = BinaryAssociation(
    name="parent47",
    ends={
        Property(name="research_Position48", type=research_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Position46", type=research_Position, multiplicity=Multiplicity(0, 1))
    }
)
allkeywords51: BinaryAssociation = BinaryAssociation(
    name="allkeywords51",
    ends={
        Property(name="research_Keyword53", type=research_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research_KnowledgeManager52", type=research_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword54: BinaryAssociation = BinaryAssociation(
    name="keyword54",
    ends={
        Property(name="research_Keyword56", type=research_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research_PaperKeyword55", type=research_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
kpapers49: BinaryAssociation = BinaryAssociation(
    name="kpapers49",
    ends={
        Property(name="research_Paper50", type=research_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Keyword", type=research_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
col_paper57: BinaryAssociation = BinaryAssociation(
    name="col_paper57",
    ends={
        Property(name="research_Paper59", type=research_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research_Collaboration58", type=research_Paper, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_research_PublicationProcess_Named = Generalization(general=Named, specific=research_PublicationProcess)
gen_research_Paper_Named = Generalization(general=Named, specific=research_Paper)
gen_research_Progress_Labelled = Generalization(general=Labelled, specific=research_Progress)
gen_research_Paragraph_Counted = Generalization(general=Counted, specific=research_Paragraph)
gen_research_Paragraph_Named = Generalization(general=Named, specific=research_Paragraph)
gen_research_ReviewNote_Named = Generalization(general=Named, specific=research_ReviewNote)
gen_research_Review_Labelled = Generalization(general=Labelled, specific=research_Review)
gen_research_Write_Labelled = Generalization(general=Labelled, specific=research_Write)
gen_research_PublicationStructure_Named = Generalization(general=Named, specific=research_PublicationStructure)
gen_research_PublicationSystem_Named = Generalization(general=Named, specific=research_PublicationSystem)
gen_research_Position_Named = Generalization(general=Named, specific=research_Position)
gen_research_Keyword_Named = Generalization(general=Named, specific=research_Keyword)
gen_research_KnowledgeManager_Named = Generalization(general=Named, specific=research_KnowledgeManager)

# Domain Model
domain_model = DomainModel(
    name="research",
    types={research_Researcher, research_Write, research_Review, research_PublicationProcess, Named, research_Phase, research_Paragraph, research_Progress, research_PaperKeyword, research_Paper, research_Skill, research_Position, research_Collaboration, Labelled, Counted, research_ReviewNote, research_PublicationStructure, research_KnowledgeManager, research_PublicationSystem, research_Named, research_Labelled, research_Counted, research_Keyword},
    associations={phases0, writes1, reviews2, paragraphs11, progress12, authors13, keywords14, citedBy17, res_papers4, skills5, res_position7, collaborations9, process21, reviews19, paragraph25, paper23, reviewNote28, researchers31, papers33, processView38, structuralView40, knowledgeMan36, positions43, parent47, allkeywords51, keyword54, kpapers49, col_paper57},
    generalizations={gen_research_PublicationProcess_Named, gen_research_Paper_Named, gen_research_Progress_Labelled, gen_research_Paragraph_Counted, gen_research_Paragraph_Named, gen_research_ReviewNote_Named, gen_research_Review_Labelled, gen_research_Write_Labelled, gen_research_PublicationStructure_Named, gen_research_PublicationSystem_Named, gen_research_Position_Named, gen_research_Keyword_Named, gen_research_KnowledgeManager_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)