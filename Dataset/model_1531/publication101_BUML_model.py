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
publication101_PublicationProcess = Class(name="publication101::PublicationProcess")
Named = Class(name="Named")
publication101_Phase = Class(name="publication101::Phase")
publication101_Researcher = Class(name="publication101::Researcher")
publication101_Paper = Class(name="publication101::Paper")
publication101_Skill = Class(name="publication101::Skill")
publication101_Position = Class(name="publication101::Position")
publication101_Collaboration = Class(name="publication101::Collaboration")
publication101_Paragraph = Class(name="publication101::Paragraph")
publication101_Progress = Class(name="publication101::Progress")
publication101_Write = Class(name="publication101::Write")
publication101_Review = Class(name="publication101::Review")
Counted = Class(name="Counted")
publication101_ReviewNote = Class(name="publication101::ReviewNote")
Labelled = Class(name="Labelled")
publication101_PaperKeyword = Class(name="publication101::PaperKeyword")
publication101_PublicationStructure = Class(name="publication101::PublicationStructure")
publication101_PublicationSystem = Class(name="publication101::PublicationSystem")
publication101_Named = Class(name="publication101::Named", is_abstract=True)
publication101_Counted = Class(name="publication101::Counted", is_abstract=True)
publication101_KnowledgeManager = Class(name="publication101::KnowledgeManager")
publication101_Keyword = Class(name="publication101::Keyword")
publication101_Labelled = Class(name="publication101::Labelled", is_abstract=True)

# publication101_PublicationProcess class attributes and methods
publication101_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
publication101_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
publication101_PublicationProcess.attributes={publication101_PublicationProcess_maxTime, publication101_PublicationProcess_minTime}

# Named class attributes and methods

# publication101_Phase class attributes and methods
publication101_Phase_name: Property = Property(name="name", type=StringType)
publication101_Phase.attributes={publication101_Phase_name}

# publication101_Researcher class attributes and methods
publication101_Researcher_name: Property = Property(name="name", type=StringType)
publication101_Researcher_forName: Property = Property(name="forName", type=StringType)
publication101_Researcher.attributes={publication101_Researcher_forName, publication101_Researcher_name}

# publication101_Paper class attributes and methods

# publication101_Skill class attributes and methods
publication101_Skill_description: Property = Property(name="description", type=StringType)
publication101_Skill.attributes={publication101_Skill_description}

# publication101_Position class attributes and methods
publication101_Position_description: Property = Property(name="description", type=StringType)
publication101_Position.attributes={publication101_Position_description}

# publication101_Collaboration class attributes and methods
publication101_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
publication101_Collaboration.attributes={publication101_Collaboration_ratio}

# publication101_Paragraph class attributes and methods
publication101_Paragraph_content: Property = Property(name="content", type=StringType)
publication101_Paragraph.attributes={publication101_Paragraph_content}

# publication101_Progress class attributes and methods
publication101_Progress_percent: Property = Property(name="percent", type=IntegerType)
publication101_Progress.attributes={publication101_Progress_percent}

# publication101_Write class attributes and methods
publication101_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
publication101_Write.attributes={publication101_Write_timeSpent}

# publication101_Review class attributes and methods
publication101_Review_date: Property = Property(name="date", type=DateType)
publication101_Review.attributes={publication101_Review_date}

# Counted class attributes and methods

# publication101_ReviewNote class attributes and methods
publication101_ReviewNote_content: Property = Property(name="content", type=StringType)
publication101_ReviewNote.attributes={publication101_ReviewNote_content}

# Labelled class attributes and methods

# publication101_PaperKeyword class attributes and methods
publication101_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
publication101_PaperKeyword.attributes={publication101_PaperKeyword_weight}

# publication101_PublicationStructure class attributes and methods

# publication101_PublicationSystem class attributes and methods

# publication101_Named class attributes and methods
publication101_Named_name: Property = Property(name="name", type=StringType)
publication101_Named.attributes={publication101_Named_name}

# publication101_Counted class attributes and methods
publication101_Counted_id: Property = Property(name="id", type=IntegerType)
publication101_Counted.attributes={publication101_Counted_id}

# publication101_KnowledgeManager class attributes and methods

# publication101_Keyword class attributes and methods
publication101_Keyword_description: Property = Property(name="description", type=StringType)
publication101_Keyword.attributes={publication101_Keyword_description}

# publication101_Labelled class attributes and methods
publication101_Labelled_lname: Property = Property(name="lname", type=StringType)
publication101_Labelled.attributes={publication101_Labelled_lname}

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="publication101_Phase", type=publication101_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_PublicationProcess", type=publication101_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="publication101_Researcher3", type=publication101_Review, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="publication101_Review", type=publication101_Researcher, multiplicity=Multiplicity(1, 1))
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=publication101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=publication101_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="publication101_Skill", type=publication101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Researcher6", type=publication101_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="publication101_Position", type=publication101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Researcher8", type=publication101_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="publication101_Collaboration", type=publication101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Researcher10", type=publication101_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="publication101_Paragraph", type=publication101_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Paper", type=publication101_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="publication101_Write", type=publication101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Researcher", type=publication101_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="publication101_Paper18", type=publication101_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Paper16", type=publication101_Paper, multiplicity=Multiplicity(0, 1))
    }
)
reviews19: BinaryAssociation = BinaryAssociation(
    name="reviews19",
    ends={
        Property(name="publication101_ReviewNote", type=publication101_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Paragraph20", type=publication101_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=publication101_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=publication101_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=publication101_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=publication101_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="publication101_PaperKeyword", type=publication101_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Paper15", type=publication101_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph25: BinaryAssociation = BinaryAssociation(
    name="paragraph25",
    ends={
        Property(name="publication101_Paragraph27", type=publication101_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Write26", type=publication101_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote28: BinaryAssociation = BinaryAssociation(
    name="reviewNote28",
    ends={
        Property(name="publication101_ReviewNote30", type=publication101_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Review29", type=publication101_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
process21: BinaryAssociation = BinaryAssociation(
    name="process21",
    ends={
        Property(name="publication101_PublicationProcess22", type=publication101_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Progress", type=publication101_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper23: BinaryAssociation = BinaryAssociation(
    name="paper23",
    ends={
        Property(name="Paper24", type=publication101_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=publication101_Paper, multiplicity=Multiplicity(0, 1))
    }
)
knowledgeMan36: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan36",
    ends={
        Property(name="publication101_PublicationStructure37", type=publication101_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="publication101_KnowledgeManager", type=publication101_PublicationStructure, multiplicity=Multiplicity(1, 1))
    }
)
processView38: BinaryAssociation = BinaryAssociation(
    name="processView38",
    ends={
        Property(name="publication101_PublicationProcess39", type=publication101_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_PublicationSystem", type=publication101_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView40: BinaryAssociation = BinaryAssociation(
    name="structuralView40",
    ends={
        Property(name="publication101_PublicationStructure42", type=publication101_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_PublicationSystem41", type=publication101_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions43: BinaryAssociation = BinaryAssociation(
    name="positions43",
    ends={
        Property(name="publication101_Position45", type=publication101_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_PublicationSystem44", type=publication101_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
researchers31: BinaryAssociation = BinaryAssociation(
    name="researchers31",
    ends={
        Property(name="publication101_Researcher32", type=publication101_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_PublicationStructure", type=publication101_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers33: BinaryAssociation = BinaryAssociation(
    name="papers33",
    ends={
        Property(name="publication101_Paper35", type=publication101_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_PublicationStructure34", type=publication101_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent47: BinaryAssociation = BinaryAssociation(
    name="parent47",
    ends={
        Property(name="publication101_Position48", type=publication101_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Position46", type=publication101_Position, multiplicity=Multiplicity(0, 1))
    }
)
kpapers49: BinaryAssociation = BinaryAssociation(
    name="kpapers49",
    ends={
        Property(name="publication101_Paper50", type=publication101_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Keyword", type=publication101_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
keyword54: BinaryAssociation = BinaryAssociation(
    name="keyword54",
    ends={
        Property(name="publication101_Keyword56", type=publication101_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_PaperKeyword55", type=publication101_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
col_paper57: BinaryAssociation = BinaryAssociation(
    name="col_paper57",
    ends={
        Property(name="publication101_Paper59", type=publication101_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_Collaboration58", type=publication101_Paper, multiplicity=Multiplicity(0, 1))
    }
)
allkeywords51: BinaryAssociation = BinaryAssociation(
    name="allkeywords51",
    ends={
        Property(name="publication101_Keyword53", type=publication101_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="publication101_KnowledgeManager52", type=publication101_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_publication101_PublicationProcess_Named = Generalization(general=Named, specific=publication101_PublicationProcess)
gen_publication101_Paper_Named = Generalization(general=Named, specific=publication101_Paper)
gen_publication101_Paragraph_Counted = Generalization(general=Counted, specific=publication101_Paragraph)
gen_publication101_Paragraph_Named = Generalization(general=Named, specific=publication101_Paragraph)
gen_publication101_ReviewNote_Named = Generalization(general=Named, specific=publication101_ReviewNote)
gen_publication101_Progress_Labelled = Generalization(general=Labelled, specific=publication101_Progress)
gen_publication101_Write_Labelled = Generalization(general=Labelled, specific=publication101_Write)
gen_publication101_Review_Labelled = Generalization(general=Labelled, specific=publication101_Review)
gen_publication101_PublicationStructure_Named = Generalization(general=Named, specific=publication101_PublicationStructure)
gen_publication101_PublicationSystem_Named = Generalization(general=Named, specific=publication101_PublicationSystem)
gen_publication101_Position_Named = Generalization(general=Named, specific=publication101_Position)
gen_publication101_Keyword_Named = Generalization(general=Named, specific=publication101_Keyword)
gen_publication101_KnowledgeManager_Named = Generalization(general=Named, specific=publication101_KnowledgeManager)

# Domain Model
domain_model = DomainModel(
    name="publication101",
    types={publication101_PublicationProcess, Named, publication101_Phase, publication101_Researcher, publication101_Paper, publication101_Skill, publication101_Position, publication101_Collaboration, publication101_Paragraph, publication101_Progress, publication101_Write, publication101_Review, Counted, publication101_ReviewNote, Labelled, publication101_PaperKeyword, publication101_PublicationStructure, publication101_PublicationSystem, publication101_Named, publication101_Counted, publication101_KnowledgeManager, publication101_Keyword, publication101_Labelled},
    associations={phases0, reviews2, res_papers4, skills5, res_position7, collaborations9, paragraphs11, writes1, citedBy17, reviews19, progress12, authors13, keywords14, paragraph25, reviewNote28, process21, paper23, knowledgeMan36, processView38, structuralView40, positions43, researchers31, papers33, parent47, kpapers49, keyword54, col_paper57, allkeywords51},
    generalizations={gen_publication101_PublicationProcess_Named, gen_publication101_Paper_Named, gen_publication101_Paragraph_Counted, gen_publication101_Paragraph_Named, gen_publication101_ReviewNote_Named, gen_publication101_Progress_Labelled, gen_publication101_Write_Labelled, gen_publication101_Review_Labelled, gen_publication101_PublicationStructure_Named, gen_publication101_PublicationSystem_Named, gen_publication101_Position_Named, gen_publication101_Keyword_Named, gen_publication101_KnowledgeManager_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)