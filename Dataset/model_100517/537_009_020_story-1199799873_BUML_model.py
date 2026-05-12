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
story_Catalog = Class(name="story_Catalog")
CatalogElement = Class(name="CatalogElement")
story_CatalogElement = Class(name="story_CatalogElement", is_abstract=True)
story_StoryBase = Class(name="story_StoryBase", is_abstract=True)
story_StoryContainer = Class(name="story_StoryContainer", is_abstract=True)
story_Protagonist = Class(name="story_Protagonist", is_abstract=True)
StoryContainer = Class(name="StoryContainer")
story_EClass = Class(name="story_EClass")
story_Role = Class(name="story_Role")
Protagonist = Class(name="Protagonist")
story_User = Class(name="story_User")
Actor = Class(name="Actor")
story_System = Class(name="story_System")
story_Persona = Class(name="story_Persona")
User = Class(name="User")
story_Actor = Class(name="story_Actor", is_abstract=True)
story_Epic = Class(name="story_Epic")
StoryBase = Class(name="StoryBase")
story_Theme = Class(name="story_Theme")
story_Story = Class(name="story_Story")
story_Scenario = Class(name="story_Scenario")
story_Goal = Class(name="story_Goal")
story_ConditionalProtagonist = Class(name="story_ConditionalProtagonist")
story_Parameter = Class(name="story_Parameter")

# story_Catalog class attributes and methods

# CatalogElement class attributes and methods

# story_CatalogElement class attributes and methods
story_CatalogElement_id: Property = Property(name="id", type=StringType)
story_CatalogElement_name: Property = Property(name="name", type=StringType)
story_CatalogElement_description: Property = Property(name="description", type=StringType)
story_CatalogElement.attributes={story_CatalogElement_description, story_CatalogElement_id, story_CatalogElement_name}

# story_StoryBase class attributes and methods

# story_StoryContainer class attributes and methods

# story_Protagonist class attributes and methods

# StoryContainer class attributes and methods

# story_EClass class attributes and methods

# story_Role class attributes and methods

# Protagonist class attributes and methods

# story_User class attributes and methods

# Actor class attributes and methods

# story_System class attributes and methods

# story_Persona class attributes and methods
story_Persona_picture: Property = Property(name="picture", type=StringType)
story_Persona.attributes={story_Persona_picture}

# User class attributes and methods

# story_Actor class attributes and methods

# story_Epic class attributes and methods

# StoryBase class attributes and methods

# story_Theme class attributes and methods

# story_Story class attributes and methods
story_Story_goal: Property = Property(name="goal", type=StringType)
story_Story_benefit: Property = Property(name="benefit", type=StringType)
story_Story_completed: Property = Property(name="completed", type=BooleanType)
story_Story.attributes={story_Story_benefit, story_Story_completed, story_Story_goal}

# story_Scenario class attributes and methods
story_Scenario_action: Property = Property(name="action", type=StringType)
story_Scenario_outcome: Property = Property(name="outcome", type=StringType)
story_Scenario_context: Property = Property(name="context", type=StringType)
story_Scenario.attributes={story_Scenario_action, story_Scenario_context, story_Scenario_outcome}

# story_Goal class attributes and methods
story_Goal_name: Property = Property(name="name", type=StringType)
story_Goal_details: Property = Property(name="details", type=StringType)
story_Goal.attributes={story_Goal_details, story_Goal_name}

# story_ConditionalProtagonist class attributes and methods
story_ConditionalProtagonist_condition: Property = Property(name="condition", type=StringType)
story_ConditionalProtagonist.attributes={story_ConditionalProtagonist_condition}

# story_Parameter class attributes and methods
story_Parameter_name: Property = Property(name="name", type=StringType)
story_Parameter_type: Property = Property(name="type", type=StringType)
story_Parameter_description: Property = Property(name="description", type=StringType)
story_Parameter.attributes={story_Parameter_description, story_Parameter_name, story_Parameter_type}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="story_CatalogElement", type=story_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Catalog", type=story_CatalogElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stories1: BinaryAssociation = BinaryAssociation(
    name="stories1",
    ends={
        Property(name="story_StoryBase", type=story_StoryContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="story_StoryContainer", type=story_StoryBase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkTo2: BinaryAssociation = BinaryAssociation(
    name="linkTo2",
    ends={
        Property(name="story_EClass", type=story_Protagonist, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Protagonist", type=story_EClass, multiplicity=Multiplicity(0, 1))
    }
)
subRoles4: BinaryAssociation = BinaryAssociation(
    name="subRoles4",
    ends={
        Property(name="story_Role", type=story_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Role3", type=story_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superRoles6: BinaryAssociation = BinaryAssociation(
    name="superRoles6",
    ends={
        Property(name="story_Role7", type=story_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Role5", type=story_Role, multiplicity=Multiplicity(0, 9999))
    }
)
subActors11: BinaryAssociation = BinaryAssociation(
    name="subActors11",
    ends={
        Property(name="story_Actor12", type=story_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Actor10", type=story_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superActors14: BinaryAssociation = BinaryAssociation(
    name="superActors14",
    ends={
        Property(name="story_Actor15", type=story_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Actor13", type=story_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
goals16: BinaryAssociation = BinaryAssociation(
    name="goals16",
    ends={
        Property(name="story_Persona", type=story_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="story_Goal", type=story_Persona, multiplicity=Multiplicity(1, 1))
    }
)
roles8: BinaryAssociation = BinaryAssociation(
    name="roles8",
    ends={
        Property(name="story_Role9", type=story_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Actor", type=story_Role, multiplicity=Multiplicity(0, 9999))
    }
)
children18: BinaryAssociation = BinaryAssociation(
    name="children18",
    ends={
        Property(name="story_Theme", type=story_Theme, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Theme17", type=story_Theme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenarios19: BinaryAssociation = BinaryAssociation(
    name="scenarios19",
    ends={
        Property(name="story_Scenario", type=story_Story, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Story", type=story_Scenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
depends21: BinaryAssociation = BinaryAssociation(
    name="depends21",
    ends={
        Property(name="story_Story22", type=story_Story, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Story20", type=story_Story, multiplicity=Multiplicity(0, 9999))
    }
)
protagonists26: BinaryAssociation = BinaryAssociation(
    name="protagonists26",
    ends={
        Property(name="story_Protagonist28", type=story_Story, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Story27", type=story_Protagonist, multiplicity=Multiplicity(0, 9999))
    }
)
conditionalprotagonists29: BinaryAssociation = BinaryAssociation(
    name="conditionalprotagonists29",
    ends={
        Property(name="story_ConditionalProtagonist", type=story_Story, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Story30", type=story_ConditionalProtagonist, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters31: BinaryAssociation = BinaryAssociation(
    name="parameters31",
    ends={
        Property(name="story_Parameter", type=story_Story, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Story32", type=story_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
themes23: BinaryAssociation = BinaryAssociation(
    name="themes23",
    ends={
        Property(name="story_Theme25", type=story_Story, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Story24", type=story_Theme, multiplicity=Multiplicity(0, 9999))
    }
)
protagonist36: BinaryAssociation = BinaryAssociation(
    name="protagonist36",
    ends={
        Property(name="story_Protagonist38", type=story_ConditionalProtagonist, multiplicity=Multiplicity(1, 1)),
        Property(name="story_ConditionalProtagonist37", type=story_Protagonist, multiplicity=Multiplicity(1, 9999))
    }
)
realizes33: BinaryAssociation = BinaryAssociation(
    name="realizes33",
    ends={
        Property(name="story_Goal35", type=story_Story, multiplicity=Multiplicity(1, 1)),
        Property(name="story_Story34", type=story_Goal, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_story_Catalog_CatalogElement = Generalization(general=CatalogElement, specific=story_Catalog)
gen_story_StoryBase_CatalogElement = Generalization(general=CatalogElement, specific=story_StoryBase)
gen_story_StoryContainer_CatalogElement = Generalization(general=CatalogElement, specific=story_StoryContainer)
gen_story_Protagonist_StoryContainer = Generalization(general=StoryContainer, specific=story_Protagonist)
gen_story_Role_Protagonist = Generalization(general=Protagonist, specific=story_Role)
gen_story_User_Actor = Generalization(general=Actor, specific=story_User)
gen_story_System_Actor = Generalization(general=Actor, specific=story_System)
gen_story_Persona_User = Generalization(general=User, specific=story_Persona)
gen_story_Actor_Protagonist = Generalization(general=Protagonist, specific=story_Actor)
gen_story_Epic_StoryContainer = Generalization(general=StoryContainer, specific=story_Epic)
gen_story_Epic_StoryBase = Generalization(general=StoryBase, specific=story_Epic)
gen_story_Theme_CatalogElement = Generalization(general=CatalogElement, specific=story_Theme)
gen_story_Story_StoryBase = Generalization(general=StoryBase, specific=story_Story)
gen_story_Scenario_CatalogElement = Generalization(general=CatalogElement, specific=story_Scenario)

# Domain Model
domain_model = DomainModel(
    name="story",
    types={story_Catalog, CatalogElement, story_CatalogElement, story_StoryBase, story_StoryContainer, story_Protagonist, StoryContainer, story_EClass, story_Role, Protagonist, story_User, Actor, story_System, story_Persona, User, story_Actor, story_Epic, StoryBase, story_Theme, story_Story, story_Scenario, story_Goal, story_ConditionalProtagonist, story_Parameter},
    associations={elements0, stories1, linkTo2, subRoles4, superRoles6, subActors11, superActors14, goals16, roles8, children18, scenarios19, depends21, protagonists26, conditionalprotagonists29, parameters31, themes23, protagonist36, realizes33},
    generalizations={gen_story_Catalog_CatalogElement, gen_story_StoryBase_CatalogElement, gen_story_StoryContainer_CatalogElement, gen_story_Protagonist_StoryContainer, gen_story_Role_Protagonist, gen_story_User_Actor, gen_story_System_Actor, gen_story_Persona_User, gen_story_Actor_Protagonist, gen_story_Epic_StoryContainer, gen_story_Epic_StoryBase, gen_story_Theme_CatalogElement, gen_story_Story_StoryBase, gen_story_Scenario_CatalogElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)