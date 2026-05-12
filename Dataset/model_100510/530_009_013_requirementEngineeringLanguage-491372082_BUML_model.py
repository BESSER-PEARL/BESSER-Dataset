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

# Enumerations
Taxonomy: Enumeration = Enumeration(
    name="Taxonomy",
    literals={
            EnumerationLiteral(name="Proportion"),
			EnumerationLiteral(name="Location"),
			EnumerationLiteral(name="Comparison"),
			EnumerationLiteral(name="Part_to_a_whole"),
			EnumerationLiteral(name="Relationship"),
			EnumerationLiteral(name="Over_time"),
			EnumerationLiteral(name="Distribution"),
			EnumerationLiteral(name="Hierarchy"),
			EnumerationLiteral(name="Reference_tool"),
			EnumerationLiteral(name="Range"),
			EnumerationLiteral(name="Pattern")
    }
)

Reaction: Enumeration = Enumeration(
    name="Reaction",
    literals={
            EnumerationLiteral(name="Synchronize"),
			EnumerationLiteral(name="GoTo"),
			EnumerationLiteral(name="Enable"),
			EnumerationLiteral(name="Disable")
    }
)

State: Enumeration = Enumeration(
    name="State",
    literals={
            EnumerationLiteral(name="Over"),
			EnumerationLiteral(name="Current"),
			EnumerationLiteral(name="Expected")
    }
)

Action: Enumeration = Enumeration(
    name="Action",
    literals={
            EnumerationLiteral(name="next"),
			EnumerationLiteral(name="previous"),
			EnumerationLiteral(name="range"),
			EnumerationLiteral(name="element")
    }
)

ContainerType: Enumeration = Enumeration(
    name="ContainerType",
    literals={
            EnumerationLiteral(name="Building"),
			EnumerationLiteral(name="Floor"),
			EnumerationLiteral(name="Corridor"),
			EnumerationLiteral(name="Room"),
			EnumerationLiteral(name="Furniture"),
			EnumerationLiteral(name="Wall"),
			EnumerationLiteral(name="Window")
    }
)

DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="Temperature"),
			EnumerationLiteral(name="Luminosity"),
			EnumerationLiteral(name="Humidity"),
			EnumerationLiteral(name="Cardiac_frequency"),
			EnumerationLiteral(name="Occupancy"),
			EnumerationLiteral(name="Pressure")
    }
)

Quantifier: Enumeration = Enumeration(
    name="Quantifier",
    literals={
            EnumerationLiteral(name="All"),
			EnumerationLiteral(name="Some"),
			EnumerationLiteral(name="One")
    }
)

# Classes
requirementEngineeringLanguage_Scenario = Class(name="requirementEngineeringLanguage_Scenario")
requirementEngineeringLanguage_When = Class(name="requirementEngineeringLanguage_When", is_abstract=True)
requirementEngineeringLanguage_Then = Class(name="requirementEngineeringLanguage_Then", is_abstract=True)
requirementEngineeringLanguage_Given = Class(name="requirementEngineeringLanguage_Given")
requirementEngineeringLanguage_Data = Class(name="requirementEngineeringLanguage_Data")
requirementEngineeringLanguage_View = Class(name="requirementEngineeringLanguage_View")
requirementEngineeringLanguage_Loading = Class(name="requirementEngineeringLanguage_Loading")
When = Class(name="When")
requirementEngineeringLanguage_Interaction = Class(name="requirementEngineeringLanguage_Interaction")
requirementEngineeringLanguage_Project = Class(name="requirementEngineeringLanguage_Project")
requirementEngineeringLanguage_Feature = Class(name="requirementEngineeringLanguage_Feature")
requirementEngineeringLanguage_Background = Class(name="requirementEngineeringLanguage_Background")
requirementEngineeringLanguage_Update = Class(name="requirementEngineeringLanguage_Update")
Then = Class(name="Then")
requirementEngineeringLanguage_Goal = Class(name="requirementEngineeringLanguage_Goal")

# requirementEngineeringLanguage_Scenario class attributes and methods
requirementEngineeringLanguage_Scenario_name: Property = Property(name="name", type=StringType)
requirementEngineeringLanguage_Scenario.attributes={requirementEngineeringLanguage_Scenario_name}

# requirementEngineeringLanguage_When class attributes and methods

# requirementEngineeringLanguage_Then class attributes and methods

# requirementEngineeringLanguage_Given class attributes and methods
requirementEngineeringLanguage_Given_dashboard: Property = Property(name="dashboard", type=StringType)
requirementEngineeringLanguage_Given.attributes={requirementEngineeringLanguage_Given_dashboard}

# requirementEngineeringLanguage_Data class attributes and methods
requirementEngineeringLanguage_Data_type: Property = Property(name="type", type=StringType)
requirementEngineeringLanguage_Data_locationType: Property = Property(name="locationType", type=StringType)
requirementEngineeringLanguage_Data_quantifier: Property = Property(name="quantifier", type=StringType)
requirementEngineeringLanguage_Data_location: Property = Property(name="location", type=StringType)
requirementEngineeringLanguage_Data.attributes={requirementEngineeringLanguage_Data_type, requirementEngineeringLanguage_Data_location, requirementEngineeringLanguage_Data_locationType, requirementEngineeringLanguage_Data_quantifier}

# requirementEngineeringLanguage_View class attributes and methods
requirementEngineeringLanguage_View_name: Property = Property(name="name", type=StringType)
requirementEngineeringLanguage_View_desc: Property = Property(name="desc", type=StringType)
requirementEngineeringLanguage_View.attributes={requirementEngineeringLanguage_View_desc, requirementEngineeringLanguage_View_name}

# requirementEngineeringLanguage_Loading class attributes and methods
requirementEngineeringLanguage_Loading_new: Property = Property(name="new", type=StringType)
requirementEngineeringLanguage_Loading.attributes={requirementEngineeringLanguage_Loading_new}

# When class attributes and methods

# requirementEngineeringLanguage_Interaction class attributes and methods
requirementEngineeringLanguage_Interaction_action: Property = Property(name="action", type=StringType)
requirementEngineeringLanguage_Interaction_target: Property = Property(name="target", type=StringType)
requirementEngineeringLanguage_Interaction.attributes={requirementEngineeringLanguage_Interaction_action, requirementEngineeringLanguage_Interaction_target}

# requirementEngineeringLanguage_Project class attributes and methods
requirementEngineeringLanguage_Project_name: Property = Property(name="name", type=StringType)
requirementEngineeringLanguage_Project.attributes={requirementEngineeringLanguage_Project_name}

# requirementEngineeringLanguage_Feature class attributes and methods
requirementEngineeringLanguage_Feature_name: Property = Property(name="name", type=StringType)
requirementEngineeringLanguage_Feature_desc: Property = Property(name="desc", type=StringType)
requirementEngineeringLanguage_Feature.attributes={requirementEngineeringLanguage_Feature_desc, requirementEngineeringLanguage_Feature_name}

# requirementEngineeringLanguage_Background class attributes and methods
requirementEngineeringLanguage_Background_dashboard: Property = Property(name="dashboard", type=StringType)
requirementEngineeringLanguage_Background.attributes={requirementEngineeringLanguage_Background_dashboard}

# requirementEngineeringLanguage_Update class attributes and methods
requirementEngineeringLanguage_Update_do: Property = Property(name="do", type=StringType)
requirementEngineeringLanguage_Update.attributes={requirementEngineeringLanguage_Update_do}

# Then class attributes and methods

# requirementEngineeringLanguage_Goal class attributes and methods
requirementEngineeringLanguage_Goal_function: Property = Property(name="function", type=StringType)
requirementEngineeringLanguage_Goal_data: Property = Property(name="data", type=StringType)
requirementEngineeringLanguage_Goal.attributes={requirementEngineeringLanguage_Goal_function, requirementEngineeringLanguage_Goal_data}

# Relationships
trigger0: BinaryAssociation = BinaryAssociation(
    name="trigger0",
    ends={
        Property(name="requirementEngineeringLanguage_When", type=requirementEngineeringLanguage_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementEngineeringLanguage_Scenario", type=requirementEngineeringLanguage_When, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outcome1: BinaryAssociation = BinaryAssociation(
    name="outcome1",
    ends={
        Property(name="requirementEngineeringLanguage_Then", type=requirementEngineeringLanguage_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementEngineeringLanguage_Scenario2", type=requirementEngineeringLanguage_Then, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
system3: BinaryAssociation = BinaryAssociation(
    name="system3",
    ends={
        Property(name="requirementEngineeringLanguage_Given", type=requirementEngineeringLanguage_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementEngineeringLanguage_Scenario4", type=requirementEngineeringLanguage_Given, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
data5: BinaryAssociation = BinaryAssociation(
    name="data5",
    ends={
        Property(name="requirementEngineeringLanguage_Data", type=requirementEngineeringLanguage_Given, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementEngineeringLanguage_Given6", type=requirementEngineeringLanguage_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context7: BinaryAssociation = BinaryAssociation(
    name="context7",
    ends={
        Property(name="requirementEngineeringLanguage_View", type=requirementEngineeringLanguage_When, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementEngineeringLanguage_When8", type=requirementEngineeringLanguage_View, multiplicity=Multiplicity(1, 1))
    }
)
consistOf9: BinaryAssociation = BinaryAssociation(
    name="consistOf9",
    ends={
        Property(name="requirementEngineeringLanguage_Feature", type=requirementEngineeringLanguage_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementEngineeringLanguage_Project", type=requirementEngineeringLanguage_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
background10: BinaryAssociation = BinaryAssociation(
    name="background10",
    ends={
        Property(name="requirementEngineeringLanguage_Background", type=requirementEngineeringLanguage_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementEngineeringLanguage_Project11", type=requirementEngineeringLanguage_Background, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="requirementEngineeringLanguage_View13", type=requirementEngineeringLanguage_Update, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementEngineeringLanguage_Update", type=requirementEngineeringLanguage_View, multiplicity=Multiplicity(1, 1))
    }
)
specifiedBy14: BinaryAssociation = BinaryAssociation(
    name="specifiedBy14",
    ends={
        Property(name="requirementEngineeringLanguage_Scenario16", type=requirementEngineeringLanguage_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementEngineeringLanguage_Feature15", type=requirementEngineeringLanguage_Scenario, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
view17: BinaryAssociation = BinaryAssociation(
    name="view17",
    ends={
        Property(name="requirementEngineeringLanguage_View19", type=requirementEngineeringLanguage_Background, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementEngineeringLanguage_Background18", type=requirementEngineeringLanguage_View, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_requirementEngineeringLanguage_Loading_When = Generalization(general=When, specific=requirementEngineeringLanguage_Loading)
gen_requirementEngineeringLanguage_Interaction_When = Generalization(general=When, specific=requirementEngineeringLanguage_Interaction)
gen_requirementEngineeringLanguage_Update_Then = Generalization(general=Then, specific=requirementEngineeringLanguage_Update)
gen_requirementEngineeringLanguage_Goal_Then = Generalization(general=Then, specific=requirementEngineeringLanguage_Goal)

# Domain Model
domain_model = DomainModel(
    name="requirementEngineeringLanguage",
    types={requirementEngineeringLanguage_Scenario, requirementEngineeringLanguage_When, requirementEngineeringLanguage_Then, requirementEngineeringLanguage_Given, requirementEngineeringLanguage_Data, requirementEngineeringLanguage_View, requirementEngineeringLanguage_Loading, When, requirementEngineeringLanguage_Interaction, requirementEngineeringLanguage_Project, requirementEngineeringLanguage_Feature, requirementEngineeringLanguage_Background, requirementEngineeringLanguage_Update, Then, requirementEngineeringLanguage_Goal, Taxonomy, Reaction, State, Action, ContainerType, DataType, Quantifier},
    associations={trigger0, outcome1, system3, data5, context7, consistOf9, background10, target12, specifiedBy14, view17},
    generalizations={gen_requirementEngineeringLanguage_Loading_When, gen_requirementEngineeringLanguage_Interaction_When, gen_requirementEngineeringLanguage_Update_Then, gen_requirementEngineeringLanguage_Goal_Then},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)