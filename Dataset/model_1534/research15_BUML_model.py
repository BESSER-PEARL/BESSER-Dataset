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
research15_Phase = Class(name="research15::Phase")
research15_PublicationProcess = Class(name="research15::PublicationProcess")
Named = Class(name="Named")
research15_Skill = Class(name="research15::Skill")
research15_Position = Class(name="research15::Position")
research15_Researcher = Class(name="research15::Researcher")
research15_Write = Class(name="research15::Write")
research15_Review = Class(name="research15::Review")
research15_Paper = Class(name="research15::Paper")
Counted = Class(name="Counted")
research15_Collaboration = Class(name="research15::Collaboration")
research15_Paragraph = Class(name="research15::Paragraph")
research15_Progress = Class(name="research15::Progress")
research15_PaperKeyword = Class(name="research15::PaperKeyword")
research15_ReviewNote = Class(name="research15::ReviewNote")
Labelled = Class(name="Labelled")
research15_PublicationSystem = Class(name="research15::PublicationSystem")
research15_PublicationStructure = Class(name="research15::PublicationStructure")
research15_KnowledgeManager = Class(name="research15::KnowledgeManager")
research15_Named = Class(name="research15::Named", is_abstract=True)
research15_Counted = Class(name="research15::Counted", is_abstract=True)
research15_Labelled = Class(name="research15::Labelled", is_abstract=True)
research15_Keyword = Class(name="research15::Keyword")

# research15_Phase class attributes and methods
research15_Phase_name: Property = Property(name="name", type=StringType)
research15_Phase.attributes={research15_Phase_name}

# research15_PublicationProcess class attributes and methods
research15_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research15_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research15_PublicationProcess.attributes={research15_PublicationProcess_minTime, research15_PublicationProcess_maxTime}

# Named class attributes and methods

# research15_Skill class attributes and methods
research15_Skill_description: Property = Property(name="description", type=StringType)
research15_Skill.attributes={research15_Skill_description}

# research15_Position class attributes and methods
research15_Position_description: Property = Property(name="description", type=StringType)
research15_Position.attributes={research15_Position_description}

# research15_Researcher class attributes and methods
research15_Researcher_name: Property = Property(name="name", type=StringType)
research15_Researcher_forName: Property = Property(name="forName", type=StringType)
research15_Researcher.attributes={research15_Researcher_name, research15_Researcher_forName}

# research15_Write class attributes and methods
research15_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research15_Write.attributes={research15_Write_timeSpent}

# research15_Review class attributes and methods
research15_Review_date: Property = Property(name="date", type=DateType)
research15_Review.attributes={research15_Review_date}

# research15_Paper class attributes and methods

# Counted class attributes and methods

# research15_Collaboration class attributes and methods
research15_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research15_Collaboration.attributes={research15_Collaboration_ratio}

# research15_Paragraph class attributes and methods
research15_Paragraph_content: Property = Property(name="content", type=StringType)
research15_Paragraph.attributes={research15_Paragraph_content}

# research15_Progress class attributes and methods
research15_Progress_percent: Property = Property(name="percent", type=IntegerType)
research15_Progress.attributes={research15_Progress_percent}

# research15_PaperKeyword class attributes and methods
research15_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research15_PaperKeyword.attributes={research15_PaperKeyword_weight}

# research15_ReviewNote class attributes and methods
research15_ReviewNote_content: Property = Property(name="content", type=StringType)
research15_ReviewNote.attributes={research15_ReviewNote_content}

# Labelled class attributes and methods

# research15_PublicationSystem class attributes and methods

# research15_PublicationStructure class attributes and methods

# research15_KnowledgeManager class attributes and methods

# research15_Named class attributes and methods
research15_Named_name: Property = Property(name="name", type=StringType)
research15_Named.attributes={research15_Named_name}

# research15_Counted class attributes and methods
research15_Counted_id: Property = Property(name="id", type=IntegerType)
research15_Counted.attributes={research15_Counted_id}

# research15_Labelled class attributes and methods
research15_Labelled_lname: Property = Property(name="lname", type=StringType)
research15_Labelled.attributes={research15_Labelled_lname}

# research15_Keyword class attributes and methods
research15_Keyword_description: Property = Property(name="description", type=StringType)
research15_Keyword.attributes={research15_Keyword_description}

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research15_Phase", type=research15_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_PublicationProcess", type=research15_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research15_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research15_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research15_Skill", type=research15_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Researcher6", type=research15_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research15_Write", type=research15_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Researcher", type=research15_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research15_Review", type=research15_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Researcher3", type=research15_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research15_Paper16", type=research15_Paper, multiplicity=Multiplicity(0, 1)),
        Property(name="research15_Paper18", type=research15_Paper, multiplicity=Multiplicity(1, 1))
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research15_Position", type=research15_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Researcher8", type=research15_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research15_Collaboration", type=research15_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Researcher10", type=research15_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research15_Paragraph", type=research15_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Paper", type=research15_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research15_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research15_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research15_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research15_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research15_PaperKeyword", type=research15_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Paper15", type=research15_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph25: BinaryAssociation = BinaryAssociation(
    name="paragraph25",
    ends={
        Property(name="research15_Paragraph27", type=research15_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Write26", type=research15_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviews19: BinaryAssociation = BinaryAssociation(
    name="reviews19",
    ends={
        Property(name="research15_ReviewNote", type=research15_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Paragraph20", type=research15_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process21: BinaryAssociation = BinaryAssociation(
    name="process21",
    ends={
        Property(name="research15_PublicationProcess22", type=research15_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Progress", type=research15_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper23: BinaryAssociation = BinaryAssociation(
    name="paper23",
    ends={
        Property(name="Paper24", type=research15_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research15_Paper, multiplicity=Multiplicity(0, 1))
    }
)
processView38: BinaryAssociation = BinaryAssociation(
    name="processView38",
    ends={
        Property(name="research15_PublicationProcess39", type=research15_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_PublicationSystem", type=research15_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reviewNote28: BinaryAssociation = BinaryAssociation(
    name="reviewNote28",
    ends={
        Property(name="research15_ReviewNote30", type=research15_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Review29", type=research15_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
researchers31: BinaryAssociation = BinaryAssociation(
    name="researchers31",
    ends={
        Property(name="research15_Researcher32", type=research15_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_PublicationStructure", type=research15_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers33: BinaryAssociation = BinaryAssociation(
    name="papers33",
    ends={
        Property(name="research15_Paper35", type=research15_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_PublicationStructure34", type=research15_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan36: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan36",
    ends={
        Property(name="research15_KnowledgeManager", type=research15_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_PublicationStructure37", type=research15_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent47: BinaryAssociation = BinaryAssociation(
    name="parent47",
    ends={
        Property(name="research15_Position48", type=research15_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Position46", type=research15_Position, multiplicity=Multiplicity(0, 1))
    }
)
structuralView40: BinaryAssociation = BinaryAssociation(
    name="structuralView40",
    ends={
        Property(name="research15_PublicationStructure42", type=research15_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_PublicationSystem41", type=research15_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions43: BinaryAssociation = BinaryAssociation(
    name="positions43",
    ends={
        Property(name="research15_Position45", type=research15_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_PublicationSystem44", type=research15_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kpapers49: BinaryAssociation = BinaryAssociation(
    name="kpapers49",
    ends={
        Property(name="research15_Paper50", type=research15_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Keyword", type=research15_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
allkeywords51: BinaryAssociation = BinaryAssociation(
    name="allkeywords51",
    ends={
        Property(name="research15_Keyword53", type=research15_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_KnowledgeManager52", type=research15_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword54: BinaryAssociation = BinaryAssociation(
    name="keyword54",
    ends={
        Property(name="research15_Keyword56", type=research15_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_PaperKeyword55", type=research15_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
col_paper57: BinaryAssociation = BinaryAssociation(
    name="col_paper57",
    ends={
        Property(name="research15_Paper59", type=research15_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research15_Collaboration58", type=research15_Paper, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_research15_PublicationProcess_Named = Generalization(general=Named, specific=research15_PublicationProcess)
gen_research15_Paragraph_Counted = Generalization(general=Counted, specific=research15_Paragraph)
gen_research15_Paragraph_Named = Generalization(general=Named, specific=research15_Paragraph)
gen_research15_Paper_Named = Generalization(general=Named, specific=research15_Paper)
gen_research15_Write_Labelled = Generalization(general=Labelled, specific=research15_Write)
gen_research15_ReviewNote_Named = Generalization(general=Named, specific=research15_ReviewNote)
gen_research15_Progress_Labelled = Generalization(general=Labelled, specific=research15_Progress)
gen_research15_PublicationSystem_Named = Generalization(general=Named, specific=research15_PublicationSystem)
gen_research15_Review_Labelled = Generalization(general=Labelled, specific=research15_Review)
gen_research15_PublicationStructure_Named = Generalization(general=Named, specific=research15_PublicationStructure)
gen_research15_Position_Named = Generalization(general=Named, specific=research15_Position)
gen_research15_Keyword_Named = Generalization(general=Named, specific=research15_Keyword)
gen_research15_KnowledgeManager_Named = Generalization(general=Named, specific=research15_KnowledgeManager)

# Domain Model
domain_model = DomainModel(
    name="research15",
    types={research15_Phase, research15_PublicationProcess, Named, research15_Skill, research15_Position, research15_Researcher, research15_Write, research15_Review, research15_Paper, Counted, research15_Collaboration, research15_Paragraph, research15_Progress, research15_PaperKeyword, research15_ReviewNote, Labelled, research15_PublicationSystem, research15_PublicationStructure, research15_KnowledgeManager, research15_Named, research15_Counted, research15_Labelled, research15_Keyword},
    associations={phases0, res_papers4, skills5, writes1, reviews2, citedBy17, res_position7, collaborations9, paragraphs11, progress12, authors13, keywords14, paragraph25, reviews19, process21, paper23, processView38, reviewNote28, researchers31, papers33, knowledgeMan36, parent47, structuralView40, positions43, kpapers49, allkeywords51, keyword54, col_paper57},
    generalizations={gen_research15_PublicationProcess_Named, gen_research15_Paragraph_Counted, gen_research15_Paragraph_Named, gen_research15_Paper_Named, gen_research15_Write_Labelled, gen_research15_ReviewNote_Named, gen_research15_Progress_Labelled, gen_research15_PublicationSystem_Named, gen_research15_Review_Labelled, gen_research15_PublicationStructure_Named, gen_research15_Position_Named, gen_research15_Keyword_Named, gen_research15_KnowledgeManager_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)