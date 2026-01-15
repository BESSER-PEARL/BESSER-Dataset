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
research13_PublicationProcess = Class(name="research13::PublicationProcess")
Named = Class(name="Named")
research13_Paragraph = Class(name="research13::Paragraph")
research13_Phase = Class(name="research13::Phase")
research13_Progress = Class(name="research13::Progress")
research13_Write = Class(name="research13::Write")
research13_Researcher = Class(name="research13::Researcher")
research13_Review = Class(name="research13::Review")
research13_Paper = Class(name="research13::Paper")
research13_Skill = Class(name="research13::Skill")
research13_Position = Class(name="research13::Position")
research13_Collaboration = Class(name="research13::Collaboration")
Labelled = Class(name="Labelled")
research13_PaperKeyword = Class(name="research13::PaperKeyword")
Counted = Class(name="Counted")
research13_ReviewNote = Class(name="research13::ReviewNote")
research13_PublicationStructure = Class(name="research13::PublicationStructure")
research13_Named = Class(name="research13::Named", is_abstract=True)
research13_Counted = Class(name="research13::Counted", is_abstract=True)
research13_Labelled = Class(name="research13::Labelled", is_abstract=True)
research13_KnowledgeManager = Class(name="research13::KnowledgeManager")
research13_PublicationSystem = Class(name="research13::PublicationSystem")
research13_Keyword = Class(name="research13::Keyword")

# research13_PublicationProcess class attributes and methods
research13_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research13_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research13_PublicationProcess.attributes={research13_PublicationProcess_maxTime, research13_PublicationProcess_minTime}

# Named class attributes and methods

# research13_Paragraph class attributes and methods
research13_Paragraph_content: Property = Property(name="content", type=StringType)
research13_Paragraph.attributes={research13_Paragraph_content}

# research13_Phase class attributes and methods
research13_Phase_name: Property = Property(name="name", type=StringType)
research13_Phase.attributes={research13_Phase_name}

# research13_Progress class attributes and methods
research13_Progress_percent: Property = Property(name="percent", type=IntegerType)
research13_Progress.attributes={research13_Progress_percent}

# research13_Write class attributes and methods
research13_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research13_Write.attributes={research13_Write_timeSpent}

# research13_Researcher class attributes and methods
research13_Researcher_name: Property = Property(name="name", type=StringType)
research13_Researcher_forName: Property = Property(name="forName", type=StringType)
research13_Researcher.attributes={research13_Researcher_forName, research13_Researcher_name}

# research13_Review class attributes and methods
research13_Review_date: Property = Property(name="date", type=DateType)
research13_Review.attributes={research13_Review_date}

# research13_Paper class attributes and methods

# research13_Skill class attributes and methods
research13_Skill_description: Property = Property(name="description", type=StringType)
research13_Skill.attributes={research13_Skill_description}

# research13_Position class attributes and methods
research13_Position_description: Property = Property(name="description", type=StringType)
research13_Position.attributes={research13_Position_description}

# research13_Collaboration class attributes and methods
research13_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research13_Collaboration.attributes={research13_Collaboration_ratio}

# Labelled class attributes and methods

# research13_PaperKeyword class attributes and methods
research13_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research13_PaperKeyword.attributes={research13_PaperKeyword_weight}

# Counted class attributes and methods

# research13_ReviewNote class attributes and methods
research13_ReviewNote_content: Property = Property(name="content", type=StringType)
research13_ReviewNote.attributes={research13_ReviewNote_content}

# research13_PublicationStructure class attributes and methods

# research13_Named class attributes and methods
research13_Named_name: Property = Property(name="name", type=StringType)
research13_Named.attributes={research13_Named_name}

# research13_Counted class attributes and methods
research13_Counted_id: Property = Property(name="id", type=IntegerType)
research13_Counted.attributes={research13_Counted_id}

# research13_Labelled class attributes and methods
research13_Labelled_lname: Property = Property(name="lname", type=StringType)
research13_Labelled.attributes={research13_Labelled_lname}

# research13_KnowledgeManager class attributes and methods

# research13_PublicationSystem class attributes and methods

# research13_Keyword class attributes and methods
research13_Keyword_description: Property = Property(name="description", type=StringType)
research13_Keyword.attributes={research13_Keyword_description}

# Relationships
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research13_Paragraph", type=research13_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Paper", type=research13_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research13_Phase", type=research13_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_PublicationProcess", type=research13_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research13_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research13_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research13_Write", type=research13_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Researcher", type=research13_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research13_Review", type=research13_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Researcher3", type=research13_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research13_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research13_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research13_Skill", type=research13_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Researcher6", type=research13_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research13_Position", type=research13_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Researcher8", type=research13_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research13_Collaboration", type=research13_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Researcher10", type=research13_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research13_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research13_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research13_PaperKeyword", type=research13_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Paper15", type=research13_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research13_Paper18", type=research13_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Paper16", type=research13_Paper, multiplicity=Multiplicity(0, 1))
    }
)
reviews19: BinaryAssociation = BinaryAssociation(
    name="reviews19",
    ends={
        Property(name="research13_ReviewNote", type=research13_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Paragraph20", type=research13_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
researchers31: BinaryAssociation = BinaryAssociation(
    name="researchers31",
    ends={
        Property(name="research13_Researcher32", type=research13_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_PublicationStructure", type=research13_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process21: BinaryAssociation = BinaryAssociation(
    name="process21",
    ends={
        Property(name="research13_PublicationProcess22", type=research13_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Progress", type=research13_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper23: BinaryAssociation = BinaryAssociation(
    name="paper23",
    ends={
        Property(name="Paper24", type=research13_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research13_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph25: BinaryAssociation = BinaryAssociation(
    name="paragraph25",
    ends={
        Property(name="research13_Paragraph27", type=research13_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Write26", type=research13_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote28: BinaryAssociation = BinaryAssociation(
    name="reviewNote28",
    ends={
        Property(name="research13_ReviewNote30", type=research13_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Review29", type=research13_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
papers33: BinaryAssociation = BinaryAssociation(
    name="papers33",
    ends={
        Property(name="research13_Paper35", type=research13_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_PublicationStructure34", type=research13_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan36: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan36",
    ends={
        Property(name="research13_KnowledgeManager", type=research13_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_PublicationStructure37", type=research13_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processView38: BinaryAssociation = BinaryAssociation(
    name="processView38",
    ends={
        Property(name="research13_PublicationProcess39", type=research13_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_PublicationSystem", type=research13_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView40: BinaryAssociation = BinaryAssociation(
    name="structuralView40",
    ends={
        Property(name="research13_PublicationStructure42", type=research13_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_PublicationSystem41", type=research13_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions43: BinaryAssociation = BinaryAssociation(
    name="positions43",
    ends={
        Property(name="research13_Position45", type=research13_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_PublicationSystem44", type=research13_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kpapers49: BinaryAssociation = BinaryAssociation(
    name="kpapers49",
    ends={
        Property(name="research13_Paper50", type=research13_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Keyword", type=research13_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
allkeywords51: BinaryAssociation = BinaryAssociation(
    name="allkeywords51",
    ends={
        Property(name="research13_Keyword53", type=research13_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_KnowledgeManager52", type=research13_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent47: BinaryAssociation = BinaryAssociation(
    name="parent47",
    ends={
        Property(name="research13_Position48", type=research13_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Position46", type=research13_Position, multiplicity=Multiplicity(0, 1))
    }
)
keyword54: BinaryAssociation = BinaryAssociation(
    name="keyword54",
    ends={
        Property(name="research13_Keyword56", type=research13_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_PaperKeyword55", type=research13_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
col_paper57: BinaryAssociation = BinaryAssociation(
    name="col_paper57",
    ends={
        Property(name="research13_Paper59", type=research13_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research13_Collaboration58", type=research13_Paper, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_research13_PublicationProcess_Named = Generalization(general=Named, specific=research13_PublicationProcess)
gen_research13_Paper_Named = Generalization(general=Named, specific=research13_Paper)
gen_research13_ReviewNote_Named = Generalization(general=Named, specific=research13_ReviewNote)
gen_research13_Progress_Labelled = Generalization(general=Labelled, specific=research13_Progress)
gen_research13_Paragraph_Counted = Generalization(general=Counted, specific=research13_Paragraph)
gen_research13_Paragraph_Named = Generalization(general=Named, specific=research13_Paragraph)
gen_research13_PublicationStructure_Named = Generalization(general=Named, specific=research13_PublicationStructure)
gen_research13_Write_Labelled = Generalization(general=Labelled, specific=research13_Write)
gen_research13_Review_Labelled = Generalization(general=Labelled, specific=research13_Review)
gen_research13_PublicationSystem_Named = Generalization(general=Named, specific=research13_PublicationSystem)
gen_research13_KnowledgeManager_Named = Generalization(general=Named, specific=research13_KnowledgeManager)
gen_research13_Position_Named = Generalization(general=Named, specific=research13_Position)
gen_research13_Keyword_Named = Generalization(general=Named, specific=research13_Keyword)

# Domain Model
domain_model = DomainModel(
    name="research13",
    types={research13_PublicationProcess, Named, research13_Paragraph, research13_Phase, research13_Progress, research13_Write, research13_Researcher, research13_Review, research13_Paper, research13_Skill, research13_Position, research13_Collaboration, Labelled, research13_PaperKeyword, Counted, research13_ReviewNote, research13_PublicationStructure, research13_Named, research13_Counted, research13_Labelled, research13_KnowledgeManager, research13_PublicationSystem, research13_Keyword},
    associations={paragraphs11, phases0, progress12, writes1, reviews2, res_papers4, skills5, res_position7, collaborations9, authors13, keywords14, citedBy17, reviews19, researchers31, process21, paper23, paragraph25, reviewNote28, papers33, knowledgeMan36, processView38, structuralView40, positions43, kpapers49, allkeywords51, parent47, keyword54, col_paper57},
    generalizations={gen_research13_PublicationProcess_Named, gen_research13_Paper_Named, gen_research13_ReviewNote_Named, gen_research13_Progress_Labelled, gen_research13_Paragraph_Counted, gen_research13_Paragraph_Named, gen_research13_PublicationStructure_Named, gen_research13_Write_Labelled, gen_research13_Review_Labelled, gen_research13_PublicationSystem_Named, gen_research13_KnowledgeManager_Named, gen_research13_Position_Named, gen_research13_Keyword_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)