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
Is_Style: Enumeration = Enumeration(
    name="Is_Style",
    literals={
            EnumerationLiteral(name="style"),
			EnumerationLiteral(name="non_style")
    }
)

# Classes
robotmodel_Port = Class(name="robotmodel::Port")
robotmodel_Property_List = Class(name="robotmodel::Property::List")
robotmodel_System = Class(name="robotmodel::System")
robotmodel_Component = Class(name="robotmodel::Component")
robotmodel_Connector = Class(name="robotmodel::Connector")
robotmodel_Property = Class(name="robotmodel::Property")
robotmodel_State = Class(name="robotmodel::State")
robotmodel_Event = Class(name="robotmodel::Event")
robotmodel_Transition = Class(name="robotmodel::Transition")
robotmodel_Action = Class(name="robotmodel::Action")
robotmodel_Role = Class(name="robotmodel::Role")

# robotmodel_Port class attributes and methods
robotmodel_Port_name: Property = Property(name="name", type=StringType)
robotmodel_Port.attributes={robotmodel_Port_name}

# robotmodel_Property_List class attributes and methods
robotmodel_Property_List_name: Property = Property(name="name", type=StringType)
robotmodel_Property_List.attributes={robotmodel_Property_List_name}

# robotmodel_System class attributes and methods
robotmodel_System_name: Property = Property(name="name", type=StringType)
robotmodel_System_depends: Property = Property(name="depends", type=StringType)
robotmodel_System_description: Property = Property(name="description", type=StringType)
robotmodel_System_author_email: Property = Property(name="author_email", type=StringType)
robotmodel_System_author: Property = Property(name="author", type=StringType)
robotmodel_System.attributes={robotmodel_System_name, robotmodel_System_description, robotmodel_System_author_email, robotmodel_System_author, robotmodel_System_depends}

# robotmodel_Component class attributes and methods
robotmodel_Component_name: Property = Property(name="name", type=StringType)
robotmodel_Component_atype: Property = Property(name="atype", type=StringType)
robotmodel_Component_type: Property = Property(name="type", type=StringType)
robotmodel_Component_depends: Property = Property(name="depends", type=StringType)
robotmodel_Component_frequency: Property = Property(name="frequency", type=FloatType)
robotmodel_Component.attributes={robotmodel_Component_atype, robotmodel_Component_depends, robotmodel_Component_frequency, robotmodel_Component_name, robotmodel_Component_type}

# robotmodel_Connector class attributes and methods
robotmodel_Connector_atype: Property = Property(name="atype", type=StringType)
robotmodel_Connector_type: Property = Property(name="type", type=StringType)
robotmodel_Connector_name: Property = Property(name="name", type=StringType)
robotmodel_Connector.attributes={robotmodel_Connector_atype, robotmodel_Connector_name, robotmodel_Connector_type}

# robotmodel_Property class attributes and methods
robotmodel_Property_name: Property = Property(name="name", type=StringType)
robotmodel_Property_type: Property = Property(name="type", type=StringType)
robotmodel_Property_value: Property = Property(name="value", type=StringType)
robotmodel_Property.attributes={robotmodel_Property_value, robotmodel_Property_name, robotmodel_Property_type}

# robotmodel_State class attributes and methods
robotmodel_State_name: Property = Property(name="name", type=StringType)
robotmodel_State.attributes={robotmodel_State_name}

# robotmodel_Event class attributes and methods
robotmodel_Event_name: Property = Property(name="name", type=StringType)
robotmodel_Event.attributes={robotmodel_Event_name}

# robotmodel_Transition class attributes and methods
robotmodel_Transition_name: Property = Property(name="name", type=StringType)
robotmodel_Transition.attributes={robotmodel_Transition_name}

# robotmodel_Action class attributes and methods
robotmodel_Action_name: Property = Property(name="name", type=StringType)
robotmodel_Action.attributes={robotmodel_Action_name}

# robotmodel_Role class attributes and methods
robotmodel_Role_name: Property = Property(name="name", type=StringType)
robotmodel_Role.attributes={robotmodel_Role_name}

# Relationships
port3: BinaryAssociation = BinaryAssociation(
    name="port3",
    ends={
        Property(name="robotmodel_Port", type=robotmodel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Component4", type=robotmodel_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property_list5: BinaryAssociation = BinaryAssociation(
    name="property_list5",
    ends={
        Property(name="robotmodel_Property_List", type=robotmodel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Component6", type=robotmodel_Property_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
component8: BinaryAssociation = BinaryAssociation(
    name="component8",
    ends={
        Property(name="robotmodel_Component9", type=robotmodel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Component7", type=robotmodel_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
component0: BinaryAssociation = BinaryAssociation(
    name="component0",
    ends={
        Property(name="robotmodel_Component", type=robotmodel_System, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_System", type=robotmodel_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connector1: BinaryAssociation = BinaryAssociation(
    name="connector1",
    ends={
        Property(name="robotmodel_Connector", type=robotmodel_System, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_System2", type=robotmodel_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role21: BinaryAssociation = BinaryAssociation(
    name="role21",
    ends={
        Property(name="robotmodel_Role", type=robotmodel_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Connector22", type=robotmodel_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role23: BinaryAssociation = BinaryAssociation(
    name="role23",
    ends={
        Property(name="robotmodel_Role25", type=robotmodel_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Port24", type=robotmodel_Role, multiplicity=Multiplicity(0, 1))
    }
)
property26: BinaryAssociation = BinaryAssociation(
    name="property26",
    ends={
        Property(name="robotmodel_Property", type=robotmodel_Property_List, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Property_List27", type=robotmodel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state10: BinaryAssociation = BinaryAssociation(
    name="state10",
    ends={
        Property(name="robotmodel_State", type=robotmodel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Component11", type=robotmodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event12: BinaryAssociation = BinaryAssociation(
    name="event12",
    ends={
        Property(name="robotmodel_Event", type=robotmodel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Component13", type=robotmodel_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition14: BinaryAssociation = BinaryAssociation(
    name="transition14",
    ends={
        Property(name="robotmodel_Transition", type=robotmodel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Component15", type=robotmodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action16: BinaryAssociation = BinaryAssociation(
    name="action16",
    ends={
        Property(name="robotmodel_Action", type=robotmodel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Component17", type=robotmodel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property_list18: BinaryAssociation = BinaryAssociation(
    name="property_list18",
    ends={
        Property(name="robotmodel_Property_List20", type=robotmodel_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Connector19", type=robotmodel_Property_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action46: BinaryAssociation = BinaryAssociation(
    name="action46",
    ends={
        Property(name="robotmodel_Action48", type=robotmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Transition47", type=robotmodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
guard49: BinaryAssociation = BinaryAssociation(
    name="guard49",
    ends={
        Property(name="robotmodel_Action51", type=robotmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Transition50", type=robotmodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
source52: BinaryAssociation = BinaryAssociation(
    name="source52",
    ends={
        Property(name="robotmodel_State54", type=robotmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Transition53", type=robotmodel_State, multiplicity=Multiplicity(1, 1))
    }
)
target55: BinaryAssociation = BinaryAssociation(
    name="target55",
    ends={
        Property(name="robotmodel_State57", type=robotmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Transition56", type=robotmodel_State, multiplicity=Multiplicity(1, 1))
    }
)
substate29: BinaryAssociation = BinaryAssociation(
    name="substate29",
    ends={
        Property(name="robotmodel_State30", type=robotmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_State28", type=robotmodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action31: BinaryAssociation = BinaryAssociation(
    name="action31",
    ends={
        Property(name="robotmodel_Action33", type=robotmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_State32", type=robotmodel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition34: BinaryAssociation = BinaryAssociation(
    name="transition34",
    ends={
        Property(name="robotmodel_Transition36", type=robotmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_State35", type=robotmodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryaction37: BinaryAssociation = BinaryAssociation(
    name="entryaction37",
    ends={
        Property(name="robotmodel_Action39", type=robotmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_State38", type=robotmodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
exitaction40: BinaryAssociation = BinaryAssociation(
    name="exitaction40",
    ends={
        Property(name="robotmodel_Action42", type=robotmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_State41", type=robotmodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
event43: BinaryAssociation = BinaryAssociation(
    name="event43",
    ends={
        Property(name="robotmodel_Event45", type=robotmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_State44", type=robotmodel_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition58: BinaryAssociation = BinaryAssociation(
    name="transition58",
    ends={
        Property(name="robotmodel_Transition60", type=robotmodel_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="robotmodel_Event59", type=robotmodel_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="robotmodel",
    types={robotmodel_Port, robotmodel_Property_List, robotmodel_System, robotmodel_Component, robotmodel_Connector, robotmodel_Property, robotmodel_State, robotmodel_Event, robotmodel_Transition, robotmodel_Action, robotmodel_Role, Is_Style},
    associations={port3, property_list5, component8, component0, connector1, role21, role23, property26, state10, event12, transition14, action16, property_list18, action46, guard49, source52, target55, substate29, action31, transition34, entryaction37, exitaction40, event43, transition58},
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