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
publication105_Researcher = Class(name="publication105::Researcher")
publication105_Write = Class(name="publication105::Write")
publication105_Review = Class(name="publication105::Review")
publication105_Paper = Class(name="publication105::Paper")
publication105_Skill = Class(name="publication105::Skill")
publication105_Position = Class(name="publication105::Position")
Named = Class(name="Named")
publication105_Paragraph = Class(name="publication105::Paragraph")
Counted = Class(name="Counted")
publication105_ReviewNote = Class(name="publication105::ReviewNote")
publication105_Collaboration = Class(name="publication105::Collaboration")
publication105_PublicationStructure = Class(name="publication105::PublicationStructure")
publication105_Named = Class(name="publication105::Named", is_abstract=True)
Labelled = Class(name="Labelled")
publication105_Labelled = Class(name="publication105::Labelled", is_abstract=True)
publication105_Counted = Class(name="publication105::Counted", is_abstract=True)

# publication105_Researcher class attributes and methods
publication105_Researcher_name: Property = Property(name="name", type=StringType)
publication105_Researcher_forName: Property = Property(name="forName", type=StringType)
publication105_Researcher.attributes={publication105_Researcher_name, publication105_Researcher_forName}

# publication105_Write class attributes and methods
publication105_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
publication105_Write.attributes={publication105_Write_timeSpent}

# publication105_Review class attributes and methods
publication105_Review_date: Property = Property(name="date", type=DateType)
publication105_Review.attributes={publication105_Review_date}

# publication105_Paper class attributes and methods

# publication105_Skill class attributes and methods
publication105_Skill_description: Property = Property(name="description", type=StringType)
publication105_Skill.attributes={publication105_Skill_description}

# publication105_Position class attributes and methods
publication105_Position_description: Property = Property(name="description", type=StringType)
publication105_Position.attributes={publication105_Position_description}

# Named class attributes and methods

# publication105_Paragraph class attributes and methods
publication105_Paragraph_content: Property = Property(name="content", type=StringType)
publication105_Paragraph.attributes={publication105_Paragraph_content}

# Counted class attributes and methods

# publication105_ReviewNote class attributes and methods
publication105_ReviewNote_content: Property = Property(name="content", type=StringType)
publication105_ReviewNote.attributes={publication105_ReviewNote_content}

# publication105_Collaboration class attributes and methods
publication105_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
publication105_Collaboration.attributes={publication105_Collaboration_ratio}

# publication105_PublicationStructure class attributes and methods

# publication105_Named class attributes and methods
publication105_Named_name: Property = Property(name="name", type=StringType)
publication105_Named.attributes={publication105_Named_name}

# Labelled class attributes and methods

# publication105_Labelled class attributes and methods
publication105_Labelled_lname: Property = Property(name="lname", type=StringType)
publication105_Labelled.attributes={publication105_Labelled_lname}

# publication105_Counted class attributes and methods
publication105_Counted_id: Property = Property(name="id", type=IntegerType)
publication105_Counted.attributes={publication105_Counted_id}

# Relationships
writes0: BinaryAssociation = BinaryAssociation(
    name="writes0",
    ends={
        Property(name="publication105_Write", type=publication105_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Researcher", type=publication105_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews1: BinaryAssociation = BinaryAssociation(
    name="reviews1",
    ends={
        Property(name="publication105_Review", type=publication105_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Researcher2", type=publication105_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers3: BinaryAssociation = BinaryAssociation(
    name="res_papers3",
    ends={
        Property(name="Paper", type=publication105_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=publication105_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills4: BinaryAssociation = BinaryAssociation(
    name="skills4",
    ends={
        Property(name="publication105_Skill", type=publication105_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Researcher5", type=publication105_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs10: BinaryAssociation = BinaryAssociation(
    name="paragraphs10",
    ends={
        Property(name="publication105_Paragraph", type=publication105_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Paper", type=publication105_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors11: BinaryAssociation = BinaryAssociation(
    name="authors11",
    ends={
        Property(name="Researcher", type=publication105_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=publication105_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
citedBy13: BinaryAssociation = BinaryAssociation(
    name="citedBy13",
    ends={
        Property(name="publication105_Paper14", type=publication105_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Paper12", type=publication105_Paper, multiplicity=Multiplicity(0, 1))
    }
)
reviews15: BinaryAssociation = BinaryAssociation(
    name="reviews15",
    ends={
        Property(name="publication105_ReviewNote", type=publication105_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Paragraph16", type=publication105_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position6: BinaryAssociation = BinaryAssociation(
    name="res_position6",
    ends={
        Property(name="publication105_Position", type=publication105_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Researcher7", type=publication105_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations8: BinaryAssociation = BinaryAssociation(
    name="collaborations8",
    ends={
        Property(name="publication105_Collaboration", type=publication105_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Researcher9", type=publication105_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph17: BinaryAssociation = BinaryAssociation(
    name="paragraph17",
    ends={
        Property(name="publication105_Paragraph19", type=publication105_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Write18", type=publication105_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote20: BinaryAssociation = BinaryAssociation(
    name="reviewNote20",
    ends={
        Property(name="publication105_ReviewNote22", type=publication105_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Review21", type=publication105_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
researchers23: BinaryAssociation = BinaryAssociation(
    name="researchers23",
    ends={
        Property(name="publication105_Researcher24", type=publication105_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_PublicationStructure", type=publication105_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers25: BinaryAssociation = BinaryAssociation(
    name="papers25",
    ends={
        Property(name="publication105_Paper27", type=publication105_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_PublicationStructure26", type=publication105_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positions28: BinaryAssociation = BinaryAssociation(
    name="positions28",
    ends={
        Property(name="publication105_Position30", type=publication105_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_PublicationStructure29", type=publication105_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent32: BinaryAssociation = BinaryAssociation(
    name="parent32",
    ends={
        Property(name="publication105_Position33", type=publication105_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Position31", type=publication105_Position, multiplicity=Multiplicity(0, 1))
    }
)
col_paper34: BinaryAssociation = BinaryAssociation(
    name="col_paper34",
    ends={
        Property(name="publication105_Paper36", type=publication105_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="publication105_Collaboration35", type=publication105_Paper, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_publication105_Paper_Named = Generalization(general=Named, specific=publication105_Paper)
gen_publication105_Paragraph_Counted = Generalization(general=Counted, specific=publication105_Paragraph)
gen_publication105_Paragraph_Named = Generalization(general=Named, specific=publication105_Paragraph)
gen_publication105_ReviewNote_Named = Generalization(general=Named, specific=publication105_ReviewNote)
gen_publication105_Review_Labelled = Generalization(general=Labelled, specific=publication105_Review)
gen_publication105_PublicationStructure_Named = Generalization(general=Named, specific=publication105_PublicationStructure)
gen_publication105_Write_Labelled = Generalization(general=Labelled, specific=publication105_Write)
gen_publication105_Position_Named = Generalization(general=Named, specific=publication105_Position)

# Domain Model
domain_model = DomainModel(
    name="publication105",
    types={publication105_Researcher, publication105_Write, publication105_Review, publication105_Paper, publication105_Skill, publication105_Position, Named, publication105_Paragraph, Counted, publication105_ReviewNote, publication105_Collaboration, publication105_PublicationStructure, publication105_Named, Labelled, publication105_Labelled, publication105_Counted},
    associations={writes0, reviews1, res_papers3, skills4, paragraphs10, authors11, citedBy13, reviews15, res_position6, collaborations8, paragraph17, reviewNote20, researchers23, papers25, positions28, parent32, col_paper34},
    generalizations={gen_publication105_Paper_Named, gen_publication105_Paragraph_Counted, gen_publication105_Paragraph_Named, gen_publication105_ReviewNote_Named, gen_publication105_Review_Labelled, gen_publication105_PublicationStructure_Named, gen_publication105_Write_Labelled, gen_publication105_Position_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)