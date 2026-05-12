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
TranslationKind: Enumeration = Enumeration(
    name="TranslationKind",
    literals={
            EnumerationLiteral(name="MULTIVAR"),
			EnumerationLiteral(name="SINGLEVAR"),
			EnumerationLiteral(name="REFINEDVAR")
    }
)

# Classes
statemachines_Statemachine = Class(name="statemachines_Statemachine")
EventBNamedCommentedElement = Class(name="EventBNamedCommentedElement")
AbstractExtension = Class(name="AbstractExtension")
Diagram = Class(name="Diagram")
statemachines_AbstractNode = Class(name="statemachines_AbstractNode", is_abstract=True)
statemachines_EventBNamedCommentedElement = Class(name="statemachines_EventBNamedCommentedElement")
statemachines_StatemachineOwner = Class(name="statemachines_StatemachineOwner", is_abstract=True)
EventBCommentedElement = Class(name="EventBCommentedElement")
EventBLabeled = Class(name="EventBLabeled")
Event = Class(name="Event")
statemachines_Transition = Class(name="statemachines_Transition")
EventBElement = Class(name="EventBElement")
statemachines_State = Class(name="statemachines_State")
AbstractNode = Class(name="AbstractNode")
EventBNamed = Class(name="EventBNamed")
StatemachineOwner = Class(name="StatemachineOwner")
statemachines_EventBElement = Class(name="statemachines_EventBElement")
statemachines_Initial = Class(name="statemachines_Initial")
statemachines_Final = Class(name="statemachines_Final")
Invariant = Class(name="Invariant")

# statemachines_Statemachine class attributes and methods
statemachines_Statemachine_translation: Property = Property(name="translation", type=StringType)
statemachines_Statemachine_selfName: Property = Property(name="selfName", type=StringType)
statemachines_Statemachine.attributes={statemachines_Statemachine_translation, statemachines_Statemachine_selfName}

# EventBNamedCommentedElement class attributes and methods

# AbstractExtension class attributes and methods

# Diagram class attributes and methods

# statemachines_AbstractNode class attributes and methods

# statemachines_EventBNamedCommentedElement class attributes and methods

# statemachines_StatemachineOwner class attributes and methods

# EventBCommentedElement class attributes and methods

# EventBLabeled class attributes and methods

# Event class attributes and methods

# statemachines_Transition class attributes and methods
statemachines_Transition_operations: Property = Property(name="operations", type=StringType)
statemachines_Transition.attributes={statemachines_Transition_operations}

# EventBElement class attributes and methods

# statemachines_State class attributes and methods
statemachines_State_active: Property = Property(name="active", type=BooleanType)
statemachines_State.attributes={statemachines_State_active}

# AbstractNode class attributes and methods

# EventBNamed class attributes and methods

# StatemachineOwner class attributes and methods

# statemachines_EventBElement class attributes and methods

# statemachines_Initial class attributes and methods

# statemachines_Final class attributes and methods

# Invariant class attributes and methods

# Relationships
refines1: BinaryAssociation = BinaryAssociation(
    name="refines1",
    ends={
        Property(name="statemachines_Statemachine", type=statemachines_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Statemachine0", type=statemachines_Statemachine, multiplicity=Multiplicity(0, 1))
    }
)
nodes2: BinaryAssociation = BinaryAssociation(
    name="nodes2",
    ends={
        Property(name="statemachines_AbstractNode", type=statemachines_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Statemachine3", type=statemachines_AbstractNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instances6: BinaryAssociation = BinaryAssociation(
    name="instances6",
    ends={
        Property(name="statemachines_EventBNamedCommentedElement", type=statemachines_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Statemachine7", type=statemachines_EventBNamedCommentedElement, multiplicity=Multiplicity(0, 1))
    }
)
statemachines8: BinaryAssociation = BinaryAssociation(
    name="statemachines8",
    ends={
        Property(name="statemachines_Statemachine9", type=statemachines_StatemachineOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_StatemachineOwner", type=statemachines_Statemachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="AbstractNode", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=statemachines_AbstractNode, multiplicity=Multiplicity(1, 1))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="AbstractNode12", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=statemachines_AbstractNode, multiplicity=Multiplicity(1, 1))
    }
)
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="statemachines_Transition", type=statemachines_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Statemachine5", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetContainer17: BinaryAssociation = BinaryAssociation(
    name="targetContainer17",
    ends={
        Property(name="statemachines_EventBElement19", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition18", type=statemachines_EventBElement, multiplicity=Multiplicity(0, 1))
    }
)
incoming20: BinaryAssociation = BinaryAssociation(
    name="incoming20",
    ends={
        Property(name="Transition", type=statemachines_AbstractNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing21: BinaryAssociation = BinaryAssociation(
    name="outgoing21",
    ends={
        Property(name="Transition22", type=statemachines_AbstractNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
elaborates13: BinaryAssociation = BinaryAssociation(
    name="elaborates13",
    ends={
        Property(name="Event", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition14", type=Event, multiplicity=Multiplicity(0, 9999))
    }
)
sourceContainer15: BinaryAssociation = BinaryAssociation(
    name="sourceContainer15",
    ends={
        Property(name="statemachines_EventBElement", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition16", type=statemachines_EventBElement, multiplicity=Multiplicity(0, 1))
    }
)
refines24: BinaryAssociation = BinaryAssociation(
    name="refines24",
    ends={
        Property(name="statemachines_State", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State23", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)
invariants25: BinaryAssociation = BinaryAssociation(
    name="invariants25",
    ends={
        Property(name="Invariant", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State26", type=Invariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statemachines_Statemachine_EventBNamedCommentedElement = Generalization(general=EventBNamedCommentedElement, specific=statemachines_Statemachine)
gen_statemachines_Statemachine_AbstractExtension = Generalization(general=AbstractExtension, specific=statemachines_Statemachine)
gen_statemachines_Statemachine_Diagram = Generalization(general=Diagram, specific=statemachines_Statemachine)
gen_statemachines_Transition_EventBCommentedElement = Generalization(general=EventBCommentedElement, specific=statemachines_Transition)
gen_statemachines_Transition_EventBLabeled = Generalization(general=EventBLabeled, specific=statemachines_Transition)
gen_statemachines_AbstractNode_EventBElement = Generalization(general=EventBElement, specific=statemachines_AbstractNode)
gen_statemachines_State_AbstractNode = Generalization(general=AbstractNode, specific=statemachines_State)
gen_statemachines_State_EventBNamed = Generalization(general=EventBNamed, specific=statemachines_State)
gen_statemachines_State_StatemachineOwner = Generalization(general=StatemachineOwner, specific=statemachines_State)
gen_statemachines_Initial_AbstractNode = Generalization(general=AbstractNode, specific=statemachines_Initial)
gen_statemachines_Final_AbstractNode = Generalization(general=AbstractNode, specific=statemachines_Final)

# Domain Model
domain_model = DomainModel(
    name="statemachines",
    types={statemachines_Statemachine, EventBNamedCommentedElement, AbstractExtension, Diagram, statemachines_AbstractNode, statemachines_EventBNamedCommentedElement, statemachines_StatemachineOwner, EventBCommentedElement, EventBLabeled, Event, statemachines_Transition, EventBElement, statemachines_State, AbstractNode, EventBNamed, StatemachineOwner, statemachines_EventBElement, statemachines_Initial, statemachines_Final, Invariant, TranslationKind},
    associations={refines1, nodes2, instances6, statemachines8, target10, source11, transitions4, targetContainer17, incoming20, outgoing21, elaborates13, sourceContainer15, refines24, invariants25},
    generalizations={gen_statemachines_Statemachine_EventBNamedCommentedElement, gen_statemachines_Statemachine_AbstractExtension, gen_statemachines_Statemachine_Diagram, gen_statemachines_Transition_EventBCommentedElement, gen_statemachines_Transition_EventBLabeled, gen_statemachines_AbstractNode_EventBElement, gen_statemachines_State_AbstractNode, gen_statemachines_State_EventBNamed, gen_statemachines_State_StatemachineOwner, gen_statemachines_Initial_AbstractNode, gen_statemachines_Final_AbstractNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)