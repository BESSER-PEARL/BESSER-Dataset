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
Behavior_System = Class(name="Behavior::System")
NamedElement = Class(name="NamedElement")
Behavior_Component = Class(name="Behavior::Component")
Behavior_Event = Class(name="Behavior::Event")
Behavior_State = Class(name="Behavior::State")
Behavior_Transition = Class(name="Behavior::Transition")
Behavior_NamedElement = Class(name="Behavior::NamedElement", is_abstract=True)

# Behavior_System class attributes and methods

# NamedElement class attributes and methods

# Behavior_Component class attributes and methods

# Behavior_Event class attributes and methods

# Behavior_State class attributes and methods

# Behavior_Transition class attributes and methods

# Behavior_NamedElement class attributes and methods
Behavior_NamedElement_name: Property = Property(name="name", type=StringType)
Behavior_NamedElement.attributes={Behavior_NamedElement_name}

# Relationships
components0: BinaryAssociation = BinaryAssociation(
    name="components0",
    ends={
        Property(name="Behavior_Component", type=Behavior_System, multiplicity=Multiplicity(1, 1)),
        Property(name="Behavior_System", type=Behavior_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="Behavior_Event", type=Behavior_System, multiplicity=Multiplicity(1, 1)),
        Property(name="Behavior_System2", type=Behavior_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="Behavior_State", type=Behavior_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="Behavior_Component4", type=Behavior_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="Behavior_Transition", type=Behavior_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="Behavior_Component6", type=Behavior_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState7: BinaryAssociation = BinaryAssociation(
    name="currentState7",
    ends={
        Property(name="Behavior_State9", type=Behavior_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="Behavior_Component8", type=Behavior_State, multiplicity=Multiplicity(0, 1))
    }
)
fromState10: BinaryAssociation = BinaryAssociation(
    name="fromState10",
    ends={
        Property(name="Behavior_State12", type=Behavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Behavior_Transition11", type=Behavior_State, multiplicity=Multiplicity(0, 1))
    }
)
toState13: BinaryAssociation = BinaryAssociation(
    name="toState13",
    ends={
        Property(name="Behavior_State15", type=Behavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Behavior_Transition14", type=Behavior_State, multiplicity=Multiplicity(0, 1))
    }
)
guardStates16: BinaryAssociation = BinaryAssociation(
    name="guardStates16",
    ends={
        Property(name="Behavior_State18", type=Behavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Behavior_Transition17", type=Behavior_State, multiplicity=Multiplicity(0, 9999))
    }
)
triggeringEvent19: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent19",
    ends={
        Property(name="Behavior_Event21", type=Behavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Behavior_Transition20", type=Behavior_Event, multiplicity=Multiplicity(0, 1))
    }
)
generatedEvent22: BinaryAssociation = BinaryAssociation(
    name="generatedEvent22",
    ends={
        Property(name="Behavior_Event24", type=Behavior_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Behavior_Transition23", type=Behavior_Event, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Behavior_System_NamedElement = Generalization(general=NamedElement, specific=Behavior_System)
gen_Behavior_Component_NamedElement = Generalization(general=NamedElement, specific=Behavior_Component)
gen_Behavior_Event_NamedElement = Generalization(general=NamedElement, specific=Behavior_Event)
gen_Behavior_Transition_NamedElement = Generalization(general=NamedElement, specific=Behavior_Transition)
gen_Behavior_State_NamedElement = Generalization(general=NamedElement, specific=Behavior_State)

# Domain Model
domain_model = DomainModel(
    name="Behavior",
    types={Behavior_System, NamedElement, Behavior_Component, Behavior_Event, Behavior_State, Behavior_Transition, Behavior_NamedElement},
    associations={components0, events1, states3, transitions5, currentState7, fromState10, toState13, guardStates16, triggeringEvent19, generatedEvent22},
    generalizations={gen_Behavior_System_NamedElement, gen_Behavior_Component_NamedElement, gen_Behavior_Event_NamedElement, gen_Behavior_Transition_NamedElement, gen_Behavior_State_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)