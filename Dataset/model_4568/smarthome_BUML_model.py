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
smarthome_SmartHome = Class(name="smarthome_SmartHome")
smarthome_Item = Class(name="smarthome_Item", is_abstract=True)
smarthome_CommandConnection = Class(name="smarthome_CommandConnection")
smarthome_FilterConnection = Class(name="smarthome_FilterConnection")
smarthome_SwitchItem = Class(name="smarthome_SwitchItem")
smarthome_DimmerItem = Class(name="smarthome_DimmerItem")
smarthome_NumberItem = Class(name="smarthome_NumberItem")
smarthome_EvaluatingNode = Class(name="smarthome_EvaluatingNode")
smarthome_State = Class(name="smarthome_State")
smarthome_Command = Class(name="smarthome_Command")
smarthome_ContactItem = Class(name="smarthome_ContactItem")
Item = Class(name="Item")
smarthome_StateChangeConnection = Class(name="smarthome_StateChangeConnection")

# smarthome_SmartHome class attributes and methods
smarthome_SmartHome_name: Property = Property(name="name", type=StringType)
smarthome_SmartHome.attributes={smarthome_SmartHome_name}

# smarthome_Item class attributes and methods
smarthome_Item_name: Property = Property(name="name", type=StringType)
smarthome_Item.attributes={smarthome_Item_name}

# smarthome_CommandConnection class attributes and methods

# smarthome_FilterConnection class attributes and methods

# smarthome_SwitchItem class attributes and methods

# smarthome_DimmerItem class attributes and methods

# smarthome_NumberItem class attributes and methods

# smarthome_EvaluatingNode class attributes and methods

# smarthome_State class attributes and methods
smarthome_State_state: Property = Property(name="state", type=StringType)
smarthome_State.attributes={smarthome_State_state}

# smarthome_Command class attributes and methods
smarthome_Command_command: Property = Property(name="command", type=StringType)
smarthome_Command.attributes={smarthome_Command_command}

# smarthome_ContactItem class attributes and methods

# Item class attributes and methods

# smarthome_StateChangeConnection class attributes and methods

# Relationships
items0: BinaryAssociation = BinaryAssociation(
    name="items0",
    ends={
        Property(name="smarthome_Item", type=smarthome_SmartHome, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_SmartHome", type=smarthome_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events7: BinaryAssociation = BinaryAssociation(
    name="events7",
    ends={
        Property(name="smarthome_EvaluatingNode8", type=smarthome_StateChangeConnection, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="smarthome_StateChangeConnection", type=smarthome_EvaluatingNode, multiplicity=Multiplicity(1, 1))
    }
)
commands9: BinaryAssociation = BinaryAssociation(
    name="commands9",
    ends={
        Property(name="smarthome_CommandConnection", type=smarthome_EvaluatingNode, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_EvaluatingNode10", type=smarthome_CommandConnection, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
filters11: BinaryAssociation = BinaryAssociation(
    name="filters11",
    ends={
        Property(name="smarthome_FilterConnection", type=smarthome_EvaluatingNode, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_EvaluatingNode12", type=smarthome_FilterConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
item13: BinaryAssociation = BinaryAssociation(
    name="item13",
    ends={
        Property(name="smarthome_Item15", type=smarthome_CommandConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_CommandConnection14", type=smarthome_Item, multiplicity=Multiplicity(1, 1))
    }
)
command16: BinaryAssociation = BinaryAssociation(
    name="command16",
    ends={
        Property(name="smarthome_Command18", type=smarthome_CommandConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_CommandConnection17", type=smarthome_Command, multiplicity=Multiplicity(1, 1))
    }
)
newState19: BinaryAssociation = BinaryAssociation(
    name="newState19",
    ends={
        Property(name="smarthome_State21", type=smarthome_StateChangeConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_StateChangeConnection20", type=smarthome_State, multiplicity=Multiplicity(1, 1))
    }
)
item22: BinaryAssociation = BinaryAssociation(
    name="item22",
    ends={
        Property(name="smarthome_Item24", type=smarthome_StateChangeConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_StateChangeConnection23", type=smarthome_Item, multiplicity=Multiplicity(1, 1))
    }
)
requiredState25: BinaryAssociation = BinaryAssociation(
    name="requiredState25",
    ends={
        Property(name="smarthome_State27", type=smarthome_FilterConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_FilterConnection26", type=smarthome_State, multiplicity=Multiplicity(1, 1))
    }
)
item28: BinaryAssociation = BinaryAssociation(
    name="item28",
    ends={
        Property(name="smarthome_Item30", type=smarthome_FilterConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_FilterConnection29", type=smarthome_Item, multiplicity=Multiplicity(1, 1))
    }
)
rules1: BinaryAssociation = BinaryAssociation(
    name="rules1",
    ends={
        Property(name="smarthome_EvaluatingNode", type=smarthome_SmartHome, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_SmartHome2", type=smarthome_EvaluatingNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="smarthome_State", type=smarthome_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Item4", type=smarthome_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accaptedCommands5: BinaryAssociation = BinaryAssociation(
    name="accaptedCommands5",
    ends={
        Property(name="smarthome_Command", type=smarthome_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="smarthome_Item6", type=smarthome_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_smarthome_SwitchItem_Item = Generalization(general=Item, specific=smarthome_SwitchItem)
gen_smarthome_DimmerItem_Item = Generalization(general=Item, specific=smarthome_DimmerItem)
gen_smarthome_ContactItem_Item = Generalization(general=Item, specific=smarthome_ContactItem)
gen_smarthome_NumberItem_Item = Generalization(general=Item, specific=smarthome_NumberItem)

# Domain Model
domain_model = DomainModel(
    name="smarthome",
    types={smarthome_SmartHome, smarthome_Item, smarthome_CommandConnection, smarthome_FilterConnection, smarthome_SwitchItem, smarthome_DimmerItem, smarthome_NumberItem, smarthome_EvaluatingNode, smarthome_State, smarthome_Command, smarthome_ContactItem, Item, smarthome_StateChangeConnection},
    associations={items0, events7, commands9, filters11, item13, command16, newState19, item22, requiredState25, item28, rules1, states3, accaptedCommands5},
    generalizations={gen_smarthome_SwitchItem_Item, gen_smarthome_DimmerItem_Item, gen_smarthome_ContactItem_Item, gen_smarthome_NumberItem_Item},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)