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
research101_Phase = Class(name="research101::Phase")
research101_Researcher = Class(name="research101::Researcher")
research101_PublicationProcess = Class(name="research101::PublicationProcess")
Named = Class(name="Named")
research101_Collaboration = Class(name="research101::Collaboration")
research101_Write = Class(name="research101::Write")
research101_Review = Class(name="research101::Review")
research101_Paper = Class(name="research101::Paper")
research101_Skill = Class(name="research101::Skill")
research101_Position = Class(name="research101::Position")
Counted = Class(name="Counted")
research101_ReviewNote = Class(name="research101::ReviewNote")
research101_Paragraph = Class(name="research101::Paragraph")
research101_Progress = Class(name="research101::Progress")
research101_PaperKeyword = Class(name="research101::PaperKeyword")
Labelled = Class(name="Labelled")
research101_PublicationStructure = Class(name="research101::PublicationStructure")
research101_Named = Class(name="research101::Named", is_abstract=True)
research101_Counted = Class(name="research101::Counted", is_abstract=True)
research101_KnowledgeManager = Class(name="research101::KnowledgeManager")
research101_PublicationSystem = Class(name="research101::PublicationSystem")
research101_Keyword = Class(name="research101::Keyword")
research101_Labelled = Class(name="research101::Labelled", is_abstract=True)

# research101_Phase class attributes and methods
research101_Phase_name: Property = Property(name="name", type=StringType)
research101_Phase.attributes={research101_Phase_name}

# research101_Researcher class attributes and methods
research101_Researcher_name: Property = Property(name="name", type=StringType)
research101_Researcher_forName: Property = Property(name="forName", type=StringType)
research101_Researcher.attributes={research101_Researcher_name, research101_Researcher_forName}

# research101_PublicationProcess class attributes and methods
research101_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research101_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research101_PublicationProcess.attributes={research101_PublicationProcess_maxTime, research101_PublicationProcess_minTime}

# Named class attributes and methods

# research101_Collaboration class attributes and methods
research101_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research101_Collaboration.attributes={research101_Collaboration_ratio}

# research101_Write class attributes and methods
research101_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research101_Write.attributes={research101_Write_timeSpent}

# research101_Review class attributes and methods
research101_Review_date: Property = Property(name="date", type=DateType)
research101_Review.attributes={research101_Review_date}

# research101_Paper class attributes and methods

# research101_Skill class attributes and methods
research101_Skill_description: Property = Property(name="description", type=StringType)
research101_Skill.attributes={research101_Skill_description}

# research101_Position class attributes and methods
research101_Position_description: Property = Property(name="description", type=StringType)
research101_Position.attributes={research101_Position_description}

# Counted class attributes and methods

# research101_ReviewNote class attributes and methods
research101_ReviewNote_content: Property = Property(name="content", type=StringType)
research101_ReviewNote.attributes={research101_ReviewNote_content}

# research101_Paragraph class attributes and methods
research101_Paragraph_content: Property = Property(name="content", type=StringType)
research101_Paragraph.attributes={research101_Paragraph_content}

# research101_Progress class attributes and methods
research101_Progress_percent: Property = Property(name="percent", type=IntegerType)
research101_Progress.attributes={research101_Progress_percent}

# research101_PaperKeyword class attributes and methods
research101_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research101_PaperKeyword.attributes={research101_PaperKeyword_weight}

# Labelled class attributes and methods

# research101_PublicationStructure class attributes and methods

# research101_Named class attributes and methods
research101_Named_name: Property = Property(name="name", type=StringType)
research101_Named.attributes={research101_Named_name}

# research101_Counted class attributes and methods
research101_Counted_id: Property = Property(name="id", type=IntegerType)
research101_Counted.attributes={research101_Counted_id}

# research101_KnowledgeManager class attributes and methods

# research101_PublicationSystem class attributes and methods

# research101_Keyword class attributes and methods
research101_Keyword_description: Property = Property(name="description", type=StringType)
research101_Keyword.attributes={research101_Keyword_description}

# research101_Labelled class attributes and methods
research101_Labelled_lname: Property = Property(name="lname", type=StringType)
research101_Labelled.attributes={research101_Labelled_lname}

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research101_Phase", type=research101_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_PublicationProcess", type=research101_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research101_Position", type=research101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Researcher8", type=research101_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research101_Collaboration", type=research101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Researcher10", type=research101_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research101_Write", type=research101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Researcher", type=research101_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research101_Review", type=research101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Researcher3", type=research101_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research101_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research101_Skill", type=research101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Researcher6", type=research101_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research101_Paragraph", type=research101_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Paper", type=research101_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research101_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research101_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research101_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research101_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research101_PaperKeyword", type=research101_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Paper15", type=research101_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research101_Paper18", type=research101_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Paper16", type=research101_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paper23: BinaryAssociation = BinaryAssociation(
    name="paper23",
    ends={
        Property(name="progress", type=research101_Paper, multiplicity=Multiplicity(0, 1)),
        Property(name="Paper24", type=research101_Progress, multiplicity=Multiplicity(1, 1))
    }
)
reviews19: BinaryAssociation = BinaryAssociation(
    name="reviews19",
    ends={
        Property(name="research101_ReviewNote", type=research101_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Paragraph20", type=research101_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process21: BinaryAssociation = BinaryAssociation(
    name="process21",
    ends={
        Property(name="research101_PublicationProcess22", type=research101_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Progress", type=research101_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
researchers31: BinaryAssociation = BinaryAssociation(
    name="researchers31",
    ends={
        Property(name="research101_Researcher32", type=research101_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_PublicationStructure", type=research101_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph25: BinaryAssociation = BinaryAssociation(
    name="paragraph25",
    ends={
        Property(name="research101_Paragraph27", type=research101_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Write26", type=research101_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote28: BinaryAssociation = BinaryAssociation(
    name="reviewNote28",
    ends={
        Property(name="research101_ReviewNote30", type=research101_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Review29", type=research101_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
positions43: BinaryAssociation = BinaryAssociation(
    name="positions43",
    ends={
        Property(name="research101_PublicationSystem44", type=research101_Position, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="research101_Position45", type=research101_PublicationSystem, multiplicity=Multiplicity(1, 1))
    }
)
papers33: BinaryAssociation = BinaryAssociation(
    name="papers33",
    ends={
        Property(name="research101_Paper35", type=research101_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_PublicationStructure34", type=research101_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan36: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan36",
    ends={
        Property(name="research101_KnowledgeManager", type=research101_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_PublicationStructure37", type=research101_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processView38: BinaryAssociation = BinaryAssociation(
    name="processView38",
    ends={
        Property(name="research101_PublicationProcess39", type=research101_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_PublicationSystem", type=research101_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView40: BinaryAssociation = BinaryAssociation(
    name="structuralView40",
    ends={
        Property(name="research101_PublicationStructure42", type=research101_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_PublicationSystem41", type=research101_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
kpapers49: BinaryAssociation = BinaryAssociation(
    name="kpapers49",
    ends={
        Property(name="research101_Paper50", type=research101_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Keyword", type=research101_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
parent47: BinaryAssociation = BinaryAssociation(
    name="parent47",
    ends={
        Property(name="research101_Position48", type=research101_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Position46", type=research101_Position, multiplicity=Multiplicity(0, 1))
    }
)
keyword54: BinaryAssociation = BinaryAssociation(
    name="keyword54",
    ends={
        Property(name="research101_Keyword56", type=research101_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_PaperKeyword55", type=research101_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
allkeywords51: BinaryAssociation = BinaryAssociation(
    name="allkeywords51",
    ends={
        Property(name="research101_Keyword53", type=research101_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_KnowledgeManager52", type=research101_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col_paper57: BinaryAssociation = BinaryAssociation(
    name="col_paper57",
    ends={
        Property(name="research101_Paper59", type=research101_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research101_Collaboration58", type=research101_Paper, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_research101_PublicationProcess_Named = Generalization(general=Named, specific=research101_PublicationProcess)
gen_research101_Paper_Named = Generalization(general=Named, specific=research101_Paper)
gen_research101_Paragraph_Counted = Generalization(general=Counted, specific=research101_Paragraph)
gen_research101_Paragraph_Named = Generalization(general=Named, specific=research101_Paragraph)
gen_research101_Write_Labelled = Generalization(general=Labelled, specific=research101_Write)
gen_research101_ReviewNote_Named = Generalization(general=Named, specific=research101_ReviewNote)
gen_research101_Progress_Labelled = Generalization(general=Labelled, specific=research101_Progress)
gen_research101_Review_Labelled = Generalization(general=Labelled, specific=research101_Review)
gen_research101_PublicationStructure_Named = Generalization(general=Named, specific=research101_PublicationStructure)
gen_research101_PublicationSystem_Named = Generalization(general=Named, specific=research101_PublicationSystem)
gen_research101_Keyword_Named = Generalization(general=Named, specific=research101_Keyword)
gen_research101_Position_Named = Generalization(general=Named, specific=research101_Position)
gen_research101_KnowledgeManager_Named = Generalization(general=Named, specific=research101_KnowledgeManager)

# Domain Model
domain_model = DomainModel(
    name="research101",
    types={research101_Phase, research101_Researcher, research101_PublicationProcess, Named, research101_Collaboration, research101_Write, research101_Review, research101_Paper, research101_Skill, research101_Position, Counted, research101_ReviewNote, research101_Paragraph, research101_Progress, research101_PaperKeyword, Labelled, research101_PublicationStructure, research101_Named, research101_Counted, research101_KnowledgeManager, research101_PublicationSystem, research101_Keyword, research101_Labelled},
    associations={phases0, res_position7, collaborations9, writes1, reviews2, res_papers4, skills5, paragraphs11, progress12, authors13, keywords14, citedBy17, paper23, reviews19, process21, researchers31, paragraph25, reviewNote28, positions43, papers33, knowledgeMan36, processView38, structuralView40, kpapers49, parent47, keyword54, allkeywords51, col_paper57},
    generalizations={gen_research101_PublicationProcess_Named, gen_research101_Paper_Named, gen_research101_Paragraph_Counted, gen_research101_Paragraph_Named, gen_research101_Write_Labelled, gen_research101_ReviewNote_Named, gen_research101_Progress_Labelled, gen_research101_Review_Labelled, gen_research101_PublicationStructure_Named, gen_research101_PublicationSystem_Named, gen_research101_Keyword_Named, gen_research101_Position_Named, gen_research101_KnowledgeManager_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)