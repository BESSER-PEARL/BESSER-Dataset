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
tp6_Skill = Class(name="tp6::Skill")
tp6_Position = Class(name="tp6::Position")
tp6_Collaboration = Class(name="tp6::Collaboration")
tp6_Researcher = Class(name="tp6::Researcher")
tp6_Paper = Class(name="tp6::Paper")
tp6_PaperKeywords = Class(name="tp6::PaperKeywords")
tp6_PublicationStructure = Class(name="tp6::PublicationStructure")
tp6_Paragraph = Class(name="tp6::Paragraph")
tp6_Keyword = Class(name="tp6::Keyword")
tp6_KnowledgeManager = Class(name="tp6::KnowledgeManager")

# tp6_Skill class attributes and methods
tp6_Skill_description: Property = Property(name="description", type=StringType)
tp6_Skill.attributes={tp6_Skill_description}

# tp6_Position class attributes and methods
tp6_Position_name: Property = Property(name="name", type=StringType)
tp6_Position_description: Property = Property(name="description", type=StringType)
tp6_Position.attributes={tp6_Position_description, tp6_Position_name}

# tp6_Collaboration class attributes and methods
tp6_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
tp6_Collaboration.attributes={tp6_Collaboration_ratio}

# tp6_Researcher class attributes and methods
tp6_Researcher_name: Property = Property(name="name", type=StringType)
tp6_Researcher_forName: Property = Property(name="forName", type=StringType)
tp6_Researcher.attributes={tp6_Researcher_forName, tp6_Researcher_name}

# tp6_Paper class attributes and methods
tp6_Paper_name: Property = Property(name="name", type=StringType)
tp6_Paper.attributes={tp6_Paper_name}

# tp6_PaperKeywords class attributes and methods
tp6_PaperKeywords_weight: Property = Property(name="weight", type=IntegerType)
tp6_PaperKeywords.attributes={tp6_PaperKeywords_weight}

# tp6_PublicationStructure class attributes and methods

# tp6_Paragraph class attributes and methods
tp6_Paragraph_name: Property = Property(name="name", type=StringType)
tp6_Paragraph_id: Property = Property(name="id", type=IntegerType)
tp6_Paragraph_content: Property = Property(name="content", type=StringType)
tp6_Paragraph.attributes={tp6_Paragraph_name, tp6_Paragraph_content, tp6_Paragraph_id}

# tp6_Keyword class attributes and methods
tp6_Keyword_key: Property = Property(name="key", type=StringType)
tp6_Keyword_description: Property = Property(name="description", type=StringType)
tp6_Keyword.attributes={tp6_Keyword_key, tp6_Keyword_description}

# tp6_KnowledgeManager class attributes and methods
tp6_KnowledgeManager_name: Property = Property(name="name", type=StringType)
tp6_KnowledgeManager.attributes={tp6_KnowledgeManager_name}

# Relationships
res_papers0: BinaryAssociation = BinaryAssociation(
    name="res_papers0",
    ends={
        Property(name="Paper", type=tp6_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=tp6_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills1: BinaryAssociation = BinaryAssociation(
    name="skills1",
    ends={
        Property(name="tp6_Skill", type=tp6_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_Researcher", type=tp6_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position2: BinaryAssociation = BinaryAssociation(
    name="res_position2",
    ends={
        Property(name="tp6_Position", type=tp6_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_Researcher3", type=tp6_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations4: BinaryAssociation = BinaryAssociation(
    name="collaborations4",
    ends={
        Property(name="tp6_Collaboration", type=tp6_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_Researcher5", type=tp6_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keywords11: BinaryAssociation = BinaryAssociation(
    name="keywords11",
    ends={
        Property(name="tp6_PaperKeywords", type=tp6_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_Paper12", type=tp6_PaperKeywords, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs6: BinaryAssociation = BinaryAssociation(
    name="paragraphs6",
    ends={
        Property(name="tp6_Paragraph", type=tp6_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_Paper", type=tp6_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors7: BinaryAssociation = BinaryAssociation(
    name="authors7",
    ends={
        Property(name="Researcher", type=tp6_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=tp6_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
citedBy9: BinaryAssociation = BinaryAssociation(
    name="citedBy9",
    ends={
        Property(name="tp6_Paper10", type=tp6_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_Paper8", type=tp6_Paper, multiplicity=Multiplicity(0, 1))
    }
)
parent24: BinaryAssociation = BinaryAssociation(
    name="parent24",
    ends={
        Property(name="tp6_Position25", type=tp6_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_Position23", type=tp6_Position, multiplicity=Multiplicity(0, 1))
    }
)
col_paper26: BinaryAssociation = BinaryAssociation(
    name="col_paper26",
    ends={
        Property(name="tp6_Paper28", type=tp6_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_Collaboration27", type=tp6_Paper, multiplicity=Multiplicity(0, 1))
    }
)
researchers13: BinaryAssociation = BinaryAssociation(
    name="researchers13",
    ends={
        Property(name="tp6_Researcher14", type=tp6_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_PublicationStructure", type=tp6_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers15: BinaryAssociation = BinaryAssociation(
    name="papers15",
    ends={
        Property(name="tp6_Paper17", type=tp6_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_PublicationStructure16", type=tp6_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positions18: BinaryAssociation = BinaryAssociation(
    name="positions18",
    ends={
        Property(name="tp6_Position20", type=tp6_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_PublicationStructure19", type=tp6_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan21: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan21",
    ends={
        Property(name="tp6_KnowledgeManager", type=tp6_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_PublicationStructure22", type=tp6_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allKeywords34: BinaryAssociation = BinaryAssociation(
    name="allKeywords34",
    ends={
        Property(name="tp6_Keyword36", type=tp6_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_KnowledgeManager35", type=tp6_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kPapers29: BinaryAssociation = BinaryAssociation(
    name="kPapers29",
    ends={
        Property(name="tp6_Paper30", type=tp6_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_Keyword", type=tp6_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
keyword31: BinaryAssociation = BinaryAssociation(
    name="keyword31",
    ends={
        Property(name="tp6_Keyword33", type=tp6_PaperKeywords, multiplicity=Multiplicity(1, 1)),
        Property(name="tp6_PaperKeywords32", type=tp6_Keyword, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tp6",
    types={tp6_Skill, tp6_Position, tp6_Collaboration, tp6_Researcher, tp6_Paper, tp6_PaperKeywords, tp6_PublicationStructure, tp6_Paragraph, tp6_Keyword, tp6_KnowledgeManager},
    associations={res_papers0, skills1, res_position2, collaborations4, keywords11, paragraphs6, authors7, citedBy9, parent24, col_paper26, researchers13, papers15, positions18, knowledgeMan21, allKeywords34, kPapers29, keyword31},
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