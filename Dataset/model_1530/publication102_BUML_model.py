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
publication102_Researcher = Class(name="publication102::Researcher")
publication102_Write = Class(name="publication102::Write")
publication102_Review = Class(name="publication102::Review")
publication102_Paper = Class(name="publication102::Paper")
publication102_Skill = Class(name="publication102::Skill")
publication102_Collaboration = Class(name="publication102::Collaboration")
Named = Class(name="Named")
publication102_Paragraph = Class(name="publication102::Paragraph")
publication102_PaperKeyword = Class(name="publication102::PaperKeyword")
Counted = Class(name="Counted")
publication102_Position = Class(name="publication102::Position")
Labelled = Class(name="Labelled")
publication102_PublicationStructure = Class(name="publication102::PublicationStructure")
publication102_ReviewNote = Class(name="publication102::ReviewNote")
publication102_KnowledgeManager = Class(name="publication102::KnowledgeManager")
publication102_Named = Class(name="publication102::Named", is_abstract=True)
publication102_Counted = Class(name="publication102::Counted", is_abstract=True)
publication102_Labelled = Class(name="publication102::Labelled", is_abstract=True)
publication102_Keyword = Class(name="publication102::Keyword")

# publication102_Researcher class attributes and methods
publication102_Researcher_name: Property = Property(name="name", type=StringType)
publication102_Researcher_forName: Property = Property(name="forName", type=StringType)
publication102_Researcher.attributes={publication102_Researcher_forName, publication102_Researcher_name}

# publication102_Write class attributes and methods
publication102_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
publication102_Write.attributes={publication102_Write_timeSpent}

# publication102_Review class attributes and methods
publication102_Review_date: Property = Property(name="date", type=DateType)
publication102_Review.attributes={publication102_Review_date}

# publication102_Paper class attributes and methods

# publication102_Skill class attributes and methods
publication102_Skill_description: Property = Property(name="description", type=StringType)
publication102_Skill.attributes={publication102_Skill_description}

# publication102_Collaboration class attributes and methods
publication102_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
publication102_Collaboration.attributes={publication102_Collaboration_ratio}

# Named class attributes and methods

# publication102_Paragraph class attributes and methods
publication102_Paragraph_content: Property = Property(name="content", type=StringType)
publication102_Paragraph.attributes={publication102_Paragraph_content}

# publication102_PaperKeyword class attributes and methods
publication102_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
publication102_PaperKeyword.attributes={publication102_PaperKeyword_weight}

# Counted class attributes and methods

# publication102_Position class attributes and methods
publication102_Position_description: Property = Property(name="description", type=StringType)
publication102_Position.attributes={publication102_Position_description}

# Labelled class attributes and methods

# publication102_PublicationStructure class attributes and methods

# publication102_ReviewNote class attributes and methods
publication102_ReviewNote_content: Property = Property(name="content", type=StringType)
publication102_ReviewNote.attributes={publication102_ReviewNote_content}

# publication102_KnowledgeManager class attributes and methods

# publication102_Named class attributes and methods
publication102_Named_name: Property = Property(name="name", type=StringType)
publication102_Named.attributes={publication102_Named_name}

# publication102_Counted class attributes and methods
publication102_Counted_id: Property = Property(name="id", type=IntegerType)
publication102_Counted.attributes={publication102_Counted_id}

# publication102_Labelled class attributes and methods
publication102_Labelled_lname: Property = Property(name="lname", type=StringType)
publication102_Labelled.attributes={publication102_Labelled_lname}

# publication102_Keyword class attributes and methods
publication102_Keyword_description: Property = Property(name="description", type=StringType)
publication102_Keyword.attributes={publication102_Keyword_description}

# Relationships
writes0: BinaryAssociation = BinaryAssociation(
    name="writes0",
    ends={
        Property(name="publication102_Write", type=publication102_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Researcher", type=publication102_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews1: BinaryAssociation = BinaryAssociation(
    name="reviews1",
    ends={
        Property(name="publication102_Review", type=publication102_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Researcher2", type=publication102_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers3: BinaryAssociation = BinaryAssociation(
    name="res_papers3",
    ends={
        Property(name="Paper", type=publication102_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=publication102_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills4: BinaryAssociation = BinaryAssociation(
    name="skills4",
    ends={
        Property(name="publication102_Skill", type=publication102_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Researcher5", type=publication102_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaborations8: BinaryAssociation = BinaryAssociation(
    name="collaborations8",
    ends={
        Property(name="publication102_Collaboration", type=publication102_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Researcher9", type=publication102_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs10: BinaryAssociation = BinaryAssociation(
    name="paragraphs10",
    ends={
        Property(name="publication102_Paragraph", type=publication102_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Paper", type=publication102_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors11: BinaryAssociation = BinaryAssociation(
    name="authors11",
    ends={
        Property(name="Researcher", type=publication102_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=publication102_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords12: BinaryAssociation = BinaryAssociation(
    name="keywords12",
    ends={
        Property(name="publication102_PaperKeyword", type=publication102_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Paper13", type=publication102_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy15: BinaryAssociation = BinaryAssociation(
    name="citedBy15",
    ends={
        Property(name="publication102_Paper16", type=publication102_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Paper14", type=publication102_Paper, multiplicity=Multiplicity(0, 1))
    }
)
res_position6: BinaryAssociation = BinaryAssociation(
    name="res_position6",
    ends={
        Property(name="publication102_Position", type=publication102_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Researcher7", type=publication102_Position, multiplicity=Multiplicity(0, 1))
    }
)
reviews17: BinaryAssociation = BinaryAssociation(
    name="reviews17",
    ends={
        Property(name="publication102_ReviewNote", type=publication102_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Paragraph18", type=publication102_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph19: BinaryAssociation = BinaryAssociation(
    name="paragraph19",
    ends={
        Property(name="publication102_Paragraph21", type=publication102_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Write20", type=publication102_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote22: BinaryAssociation = BinaryAssociation(
    name="reviewNote22",
    ends={
        Property(name="publication102_ReviewNote24", type=publication102_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Review23", type=publication102_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
researchers25: BinaryAssociation = BinaryAssociation(
    name="researchers25",
    ends={
        Property(name="publication102_Researcher26", type=publication102_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_PublicationStructure", type=publication102_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers27: BinaryAssociation = BinaryAssociation(
    name="papers27",
    ends={
        Property(name="publication102_Paper29", type=publication102_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_PublicationStructure28", type=publication102_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan30: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan30",
    ends={
        Property(name="publication102_KnowledgeManager", type=publication102_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_PublicationStructure31", type=publication102_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions32: BinaryAssociation = BinaryAssociation(
    name="positions32",
    ends={
        Property(name="publication102_Position34", type=publication102_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_PublicationStructure33", type=publication102_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent36: BinaryAssociation = BinaryAssociation(
    name="parent36",
    ends={
        Property(name="publication102_Position37", type=publication102_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Position35", type=publication102_Position, multiplicity=Multiplicity(0, 1))
    }
)
kpapers38: BinaryAssociation = BinaryAssociation(
    name="kpapers38",
    ends={
        Property(name="publication102_Paper39", type=publication102_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Keyword", type=publication102_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
allkeywords40: BinaryAssociation = BinaryAssociation(
    name="allkeywords40",
    ends={
        Property(name="publication102_Keyword42", type=publication102_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_KnowledgeManager41", type=publication102_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword43: BinaryAssociation = BinaryAssociation(
    name="keyword43",
    ends={
        Property(name="publication102_Keyword45", type=publication102_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_PaperKeyword44", type=publication102_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
col_paper46: BinaryAssociation = BinaryAssociation(
    name="col_paper46",
    ends={
        Property(name="publication102_Paper48", type=publication102_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="publication102_Collaboration47", type=publication102_Paper, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_publication102_Paper_Named = Generalization(general=Named, specific=publication102_Paper)
gen_publication102_Paragraph_Counted = Generalization(general=Counted, specific=publication102_Paragraph)
gen_publication102_Paragraph_Named = Generalization(general=Named, specific=publication102_Paragraph)
gen_publication102_ReviewNote_Named = Generalization(general=Named, specific=publication102_ReviewNote)
gen_publication102_Write_Labelled = Generalization(general=Labelled, specific=publication102_Write)
gen_publication102_Review_Labelled = Generalization(general=Labelled, specific=publication102_Review)
gen_publication102_PublicationStructure_Named = Generalization(general=Named, specific=publication102_PublicationStructure)
gen_publication102_Position_Named = Generalization(general=Named, specific=publication102_Position)
gen_publication102_Keyword_Named = Generalization(general=Named, specific=publication102_Keyword)
gen_publication102_KnowledgeManager_Named = Generalization(general=Named, specific=publication102_KnowledgeManager)

# Domain Model
domain_model = DomainModel(
    name="publication102",
    types={publication102_Researcher, publication102_Write, publication102_Review, publication102_Paper, publication102_Skill, publication102_Collaboration, Named, publication102_Paragraph, publication102_PaperKeyword, Counted, publication102_Position, Labelled, publication102_PublicationStructure, publication102_ReviewNote, publication102_KnowledgeManager, publication102_Named, publication102_Counted, publication102_Labelled, publication102_Keyword},
    associations={writes0, reviews1, res_papers3, skills4, collaborations8, paragraphs10, authors11, keywords12, citedBy15, res_position6, reviews17, paragraph19, reviewNote22, researchers25, papers27, knowledgeMan30, positions32, parent36, kpapers38, allkeywords40, keyword43, col_paper46},
    generalizations={gen_publication102_Paper_Named, gen_publication102_Paragraph_Counted, gen_publication102_Paragraph_Named, gen_publication102_ReviewNote_Named, gen_publication102_Write_Labelled, gen_publication102_Review_Labelled, gen_publication102_PublicationStructure_Named, gen_publication102_Position_Named, gen_publication102_Keyword_Named, gen_publication102_KnowledgeManager_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)