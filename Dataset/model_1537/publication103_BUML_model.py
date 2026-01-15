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
publication103_Write = Class(name="publication103::Write")
publication103_Review = Class(name="publication103::Review")
publication103_Paper = Class(name="publication103::Paper")
publication103_Skill = Class(name="publication103::Skill")
publication103_Position = Class(name="publication103::Position")
publication103_Collaboration = Class(name="publication103::Collaboration")
publication103_Researcher = Class(name="publication103::Researcher")
Counted = Class(name="Counted")
publication103_ReviewNote = Class(name="publication103::ReviewNote")
Labelled = Class(name="Labelled")
Named = Class(name="Named")
publication103_Paragraph = Class(name="publication103::Paragraph")
publication103_PublicationStructure = Class(name="publication103::PublicationStructure")
publication103_Named = Class(name="publication103::Named", is_abstract=True)
publication103_Counted = Class(name="publication103::Counted", is_abstract=True)
publication103_Labelled = Class(name="publication103::Labelled", is_abstract=True)

# publication103_Write class attributes and methods
publication103_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
publication103_Write.attributes={publication103_Write_timeSpent}

# publication103_Review class attributes and methods
publication103_Review_date: Property = Property(name="date", type=DateType)
publication103_Review.attributes={publication103_Review_date}

# publication103_Paper class attributes and methods

# publication103_Skill class attributes and methods
publication103_Skill_description: Property = Property(name="description", type=StringType)
publication103_Skill.attributes={publication103_Skill_description}

# publication103_Position class attributes and methods
publication103_Position_description: Property = Property(name="description", type=StringType)
publication103_Position.attributes={publication103_Position_description}

# publication103_Collaboration class attributes and methods
publication103_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
publication103_Collaboration.attributes={publication103_Collaboration_ratio}

# publication103_Researcher class attributes and methods
publication103_Researcher_name: Property = Property(name="name", type=StringType)
publication103_Researcher_forName: Property = Property(name="forName", type=StringType)
publication103_Researcher.attributes={publication103_Researcher_name, publication103_Researcher_forName}

# Counted class attributes and methods

# publication103_ReviewNote class attributes and methods
publication103_ReviewNote_content: Property = Property(name="content", type=StringType)
publication103_ReviewNote.attributes={publication103_ReviewNote_content}

# Labelled class attributes and methods

# Named class attributes and methods

# publication103_Paragraph class attributes and methods
publication103_Paragraph_content: Property = Property(name="content", type=StringType)
publication103_Paragraph.attributes={publication103_Paragraph_content}

# publication103_PublicationStructure class attributes and methods

# publication103_Named class attributes and methods
publication103_Named_name: Property = Property(name="name", type=StringType)
publication103_Named.attributes={publication103_Named_name}

# publication103_Counted class attributes and methods
publication103_Counted_id: Property = Property(name="id", type=IntegerType)
publication103_Counted.attributes={publication103_Counted_id}

# publication103_Labelled class attributes and methods
publication103_Labelled_lname: Property = Property(name="lname", type=StringType)
publication103_Labelled.attributes={publication103_Labelled_lname}

# Relationships
writes0: BinaryAssociation = BinaryAssociation(
    name="writes0",
    ends={
        Property(name="publication103_Write", type=publication103_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Researcher", type=publication103_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews1: BinaryAssociation = BinaryAssociation(
    name="reviews1",
    ends={
        Property(name="publication103_Review", type=publication103_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Researcher2", type=publication103_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers3: BinaryAssociation = BinaryAssociation(
    name="res_papers3",
    ends={
        Property(name="Paper", type=publication103_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=publication103_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills4: BinaryAssociation = BinaryAssociation(
    name="skills4",
    ends={
        Property(name="publication103_Skill", type=publication103_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Researcher5", type=publication103_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position6: BinaryAssociation = BinaryAssociation(
    name="res_position6",
    ends={
        Property(name="publication103_Position", type=publication103_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Researcher7", type=publication103_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations8: BinaryAssociation = BinaryAssociation(
    name="collaborations8",
    ends={
        Property(name="publication103_Collaboration", type=publication103_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Researcher9", type=publication103_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors11: BinaryAssociation = BinaryAssociation(
    name="authors11",
    ends={
        Property(name="Researcher", type=publication103_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=publication103_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
citedBy13: BinaryAssociation = BinaryAssociation(
    name="citedBy13",
    ends={
        Property(name="publication103_Paper14", type=publication103_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Paper12", type=publication103_Paper, multiplicity=Multiplicity(0, 1))
    }
)
reviews15: BinaryAssociation = BinaryAssociation(
    name="reviews15",
    ends={
        Property(name="publication103_ReviewNote", type=publication103_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Paragraph16", type=publication103_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs10: BinaryAssociation = BinaryAssociation(
    name="paragraphs10",
    ends={
        Property(name="publication103_Paragraph", type=publication103_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Paper", type=publication103_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviewNote20: BinaryAssociation = BinaryAssociation(
    name="reviewNote20",
    ends={
        Property(name="publication103_ReviewNote22", type=publication103_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Review21", type=publication103_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
researchers23: BinaryAssociation = BinaryAssociation(
    name="researchers23",
    ends={
        Property(name="publication103_Researcher24", type=publication103_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_PublicationStructure", type=publication103_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers25: BinaryAssociation = BinaryAssociation(
    name="papers25",
    ends={
        Property(name="publication103_Paper27", type=publication103_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_PublicationStructure26", type=publication103_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positions28: BinaryAssociation = BinaryAssociation(
    name="positions28",
    ends={
        Property(name="publication103_Position30", type=publication103_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_PublicationStructure29", type=publication103_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph17: BinaryAssociation = BinaryAssociation(
    name="paragraph17",
    ends={
        Property(name="publication103_Paragraph19", type=publication103_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Write18", type=publication103_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
parent32: BinaryAssociation = BinaryAssociation(
    name="parent32",
    ends={
        Property(name="publication103_Position33", type=publication103_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Position31", type=publication103_Position, multiplicity=Multiplicity(0, 1))
    }
)
col_paper34: BinaryAssociation = BinaryAssociation(
    name="col_paper34",
    ends={
        Property(name="publication103_Paper36", type=publication103_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="publication103_Collaboration35", type=publication103_Paper, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_publication103_Paragraph_Counted = Generalization(general=Counted, specific=publication103_Paragraph)
gen_publication103_Paragraph_Named = Generalization(general=Named, specific=publication103_Paragraph)
gen_publication103_ReviewNote_Named = Generalization(general=Named, specific=publication103_ReviewNote)
gen_publication103_Paper_Named = Generalization(general=Named, specific=publication103_Paper)
gen_publication103_PublicationStructure_Named = Generalization(general=Named, specific=publication103_PublicationStructure)
gen_publication103_Write_Labelled = Generalization(general=Labelled, specific=publication103_Write)
gen_publication103_Review_Labelled = Generalization(general=Labelled, specific=publication103_Review)
gen_publication103_Position_Named = Generalization(general=Named, specific=publication103_Position)

# Domain Model
domain_model = DomainModel(
    name="publication103",
    types={publication103_Write, publication103_Review, publication103_Paper, publication103_Skill, publication103_Position, publication103_Collaboration, publication103_Researcher, Counted, publication103_ReviewNote, Labelled, Named, publication103_Paragraph, publication103_PublicationStructure, publication103_Named, publication103_Counted, publication103_Labelled},
    associations={writes0, reviews1, res_papers3, skills4, res_position6, collaborations8, authors11, citedBy13, reviews15, paragraphs10, reviewNote20, researchers23, papers25, positions28, paragraph17, parent32, col_paper34},
    generalizations={gen_publication103_Paragraph_Counted, gen_publication103_Paragraph_Named, gen_publication103_ReviewNote_Named, gen_publication103_Paper_Named, gen_publication103_PublicationStructure_Named, gen_publication103_Write_Labelled, gen_publication103_Review_Labelled, gen_publication103_Position_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)