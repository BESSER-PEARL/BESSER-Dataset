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
tp5_Skill = Class(name="tp5::Skill")
tp5_Position = Class(name="tp5::Position")
tp5_Collaboration = Class(name="tp5::Collaboration")
tp5_Researcher = Class(name="tp5::Researcher")
tp5_Paper = Class(name="tp5::Paper")
tp5_Paragraph = Class(name="tp5::Paragraph")
tp5_PublicationStructure = Class(name="tp5::PublicationStructure")

# tp5_Skill class attributes and methods
tp5_Skill_description: Property = Property(name="description", type=StringType)
tp5_Skill.attributes={tp5_Skill_description}

# tp5_Position class attributes and methods
tp5_Position_name: Property = Property(name="name", type=StringType)
tp5_Position_description: Property = Property(name="description", type=StringType)
tp5_Position.attributes={tp5_Position_description, tp5_Position_name}

# tp5_Collaboration class attributes and methods
tp5_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
tp5_Collaboration.attributes={tp5_Collaboration_ratio}

# tp5_Researcher class attributes and methods
tp5_Researcher_name: Property = Property(name="name", type=StringType)
tp5_Researcher_forName: Property = Property(name="forName", type=StringType)
tp5_Researcher.attributes={tp5_Researcher_name, tp5_Researcher_forName}

# tp5_Paper class attributes and methods
tp5_Paper_name: Property = Property(name="name", type=StringType)
tp5_Paper.attributes={tp5_Paper_name}

# tp5_Paragraph class attributes and methods
tp5_Paragraph_name: Property = Property(name="name", type=StringType)
tp5_Paragraph_id: Property = Property(name="id", type=IntegerType)
tp5_Paragraph_content: Property = Property(name="content", type=StringType)
tp5_Paragraph.attributes={tp5_Paragraph_id, tp5_Paragraph_name, tp5_Paragraph_content}

# tp5_PublicationStructure class attributes and methods

# Relationships
skills1: BinaryAssociation = BinaryAssociation(
    name="skills1",
    ends={
        Property(name="tp5_Skill", type=tp5_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="tp5_Researcher", type=tp5_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position2: BinaryAssociation = BinaryAssociation(
    name="res_position2",
    ends={
        Property(name="tp5_Position", type=tp5_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="tp5_Researcher3", type=tp5_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations4: BinaryAssociation = BinaryAssociation(
    name="collaborations4",
    ends={
        Property(name="tp5_Collaboration", type=tp5_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="tp5_Researcher5", type=tp5_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers0: BinaryAssociation = BinaryAssociation(
    name="res_papers0",
    ends={
        Property(name="Paper", type=tp5_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=tp5_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
papers13: BinaryAssociation = BinaryAssociation(
    name="papers13",
    ends={
        Property(name="tp5_Paper15", type=tp5_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="tp5_PublicationStructure14", type=tp5_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positions16: BinaryAssociation = BinaryAssociation(
    name="positions16",
    ends={
        Property(name="tp5_Position18", type=tp5_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="tp5_PublicationStructure17", type=tp5_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs6: BinaryAssociation = BinaryAssociation(
    name="paragraphs6",
    ends={
        Property(name="tp5_Paragraph", type=tp5_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="tp5_Paper", type=tp5_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors7: BinaryAssociation = BinaryAssociation(
    name="authors7",
    ends={
        Property(name="Researcher", type=tp5_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=tp5_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
citedBy9: BinaryAssociation = BinaryAssociation(
    name="citedBy9",
    ends={
        Property(name="tp5_Paper10", type=tp5_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="tp5_Paper8", type=tp5_Paper, multiplicity=Multiplicity(0, 1))
    }
)
researchers11: BinaryAssociation = BinaryAssociation(
    name="researchers11",
    ends={
        Property(name="tp5_Researcher12", type=tp5_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="tp5_PublicationStructure", type=tp5_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent20: BinaryAssociation = BinaryAssociation(
    name="parent20",
    ends={
        Property(name="tp5_Position21", type=tp5_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="tp5_Position19", type=tp5_Position, multiplicity=Multiplicity(0, 1))
    }
)
col_paper22: BinaryAssociation = BinaryAssociation(
    name="col_paper22",
    ends={
        Property(name="tp5_Paper24", type=tp5_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="tp5_Collaboration23", type=tp5_Paper, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tp5",
    types={tp5_Skill, tp5_Position, tp5_Collaboration, tp5_Researcher, tp5_Paper, tp5_Paragraph, tp5_PublicationStructure},
    associations={skills1, res_position2, collaborations4, res_papers0, papers13, positions16, paragraphs6, authors7, citedBy9, researchers11, parent20, col_paper22},
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