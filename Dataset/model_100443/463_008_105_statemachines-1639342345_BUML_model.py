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
EventBNamedCommentedDataElaborationElement = Class(name="EventBNamedCommentedDataElaborationElement")
AbstractExtension = Class(name="AbstractExtension")
Diagram = Class(name="Diagram")
statemachines_AbstractNode = Class(name="statemachines_AbstractNode", is_abstract=True)
statemachines_Transition = Class(name="statemachines_Transition")
statemachines_EventBNamedCommentedElement = Class(name="statemachines_EventBNamedCommentedElement")
statemachines_StatemachineOwner = Class(name="statemachines_StatemachineOwner", is_abstract=True)
EventBCommentedLabeledEventGroupElement = Class(name="EventBCommentedLabeledEventGroupElement")
statemachines_EventBElement = Class(name="statemachines_EventBElement")
Invariant = Class(name="Invariant")
EventBElement = Class(name="EventBElement")
statemachines_State = Class(name="statemachines_State")
AbstractNode = Class(name="AbstractNode")
EventBNamed = Class(name="EventBNamed")
StatemachineOwner = Class(name="StatemachineOwner")
statemachines_Initial = Class(name="statemachines_Initial")
statemachines_Final = Class(name="statemachines_Final")
statemachines_Any = Class(name="statemachines_Any")
statemachines_Junction = Class(name="statemachines_Junction")
statemachines_Fork = Class(name="statemachines_Fork")

# statemachines_Statemachine class attributes and methods
statemachines_Statemachine_selfName: Property = Property(name="selfName", type=StringType)
statemachines_Statemachine_translation: Property = Property(name="translation", type=StringType)
statemachines_Statemachine.attributes={statemachines_Statemachine_translation, statemachines_Statemachine_selfName}

# EventBNamedCommentedDataElaborationElement class attributes and methods

# AbstractExtension class attributes and methods

# Diagram class attributes and methods

# statemachines_AbstractNode class attributes and methods

# statemachines_Transition class attributes and methods
statemachines_Transition_operations: Property = Property(name="operations", type=StringType)
statemachines_Transition.attributes={statemachines_Transition_operations}

# statemachines_EventBNamedCommentedElement class attributes and methods

# statemachines_StatemachineOwner class attributes and methods

# EventBCommentedLabeledEventGroupElement class attributes and methods

# statemachines_EventBElement class attributes and methods

# Invariant class attributes and methods

# EventBElement class attributes and methods

# statemachines_State class attributes and methods
statemachines_State_active: Property = Property(name="active", type=BooleanType)
statemachines_State.attributes={statemachines_State_active}

# AbstractNode class attributes and methods

# EventBNamed class attributes and methods

# StatemachineOwner class attributes and methods

# statemachines_Initial class attributes and methods

# statemachines_Final class attributes and methods

# statemachines_Any class attributes and methods

# statemachines_Junction class attributes and methods

# statemachines_Fork class attributes and methods
statemachines_Fork_m_isFork: Method = Method(name="isFork", parameters={}, type=BooleanType)
statemachines_Fork_m_isJoin: Method = Method(name="isJoin", parameters={}, type=BooleanType)
statemachines_Fork.methods={statemachines_Fork_m_isJoin, statemachines_Fork_m_isFork}

# Relationships
refines1: BinaryAssociation = BinaryAssociation(
    name="refines1",
    ends={
        Property(name="statemachines_Statemachine", type=statemachines_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Statemachine0", type=statemachines_Statemachine, multiplicity=Multiplicity(0, 1))
    }
)
instances6: BinaryAssociation = BinaryAssociation(
    name="instances6",
    ends={
        Property(name="statemachines_EventBNamedCommentedElement", type=statemachines_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Statemachine7", type=statemachines_EventBNamedCommentedElement, multiplicity=Multiplicity(0, 1))
    }
)
nodes2: BinaryAssociation = BinaryAssociation(
    name="nodes2",
    ends={
        Property(name="statemachines_AbstractNode", type=statemachines_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Statemachine3", type=statemachines_AbstractNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="statemachines_Transition", type=statemachines_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Statemachine5", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetContainer15: BinaryAssociation = BinaryAssociation(
    name="targetContainer15",
    ends={
        Property(name="statemachines_EventBElement17", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition16", type=statemachines_EventBElement, multiplicity=Multiplicity(0, 1))
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
sourceContainer13: BinaryAssociation = BinaryAssociation(
    name="sourceContainer13",
    ends={
        Property(name="statemachines_EventBElement", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition14", type=statemachines_EventBElement, multiplicity=Multiplicity(0, 1))
    }
)
invariants23: BinaryAssociation = BinaryAssociation(
    name="invariants23",
    ends={
        Property(name="Invariant", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State24", type=Invariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming18: BinaryAssociation = BinaryAssociation(
    name="incoming18",
    ends={
        Property(name="Transition", type=statemachines_AbstractNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing19: BinaryAssociation = BinaryAssociation(
    name="outgoing19",
    ends={
        Property(name="Transition20", type=statemachines_AbstractNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
refines22: BinaryAssociation = BinaryAssociation(
    name="refines22",
    ends={
        Property(name="statemachines_State", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State21", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_statemachines_Statemachine_EventBNamedCommentedDataElaborationElement = Generalization(general=EventBNamedCommentedDataElaborationElement, specific=statemachines_Statemachine)
gen_statemachines_Statemachine_AbstractExtension = Generalization(general=AbstractExtension, specific=statemachines_Statemachine)
gen_statemachines_Statemachine_Diagram = Generalization(general=Diagram, specific=statemachines_Statemachine)
gen_statemachines_Transition_EventBCommentedLabeledEventGroupElement = Generalization(general=EventBCommentedLabeledEventGroupElement, specific=statemachines_Transition)
gen_statemachines_AbstractNode_EventBElement = Generalization(general=EventBElement, specific=statemachines_AbstractNode)
gen_statemachines_State_AbstractNode = Generalization(general=AbstractNode, specific=statemachines_State)
gen_statemachines_State_EventBNamed = Generalization(general=EventBNamed, specific=statemachines_State)
gen_statemachines_State_StatemachineOwner = Generalization(general=StatemachineOwner, specific=statemachines_State)
gen_statemachines_Initial_AbstractNode = Generalization(general=AbstractNode, specific=statemachines_Initial)
gen_statemachines_Final_AbstractNode = Generalization(general=AbstractNode, specific=statemachines_Final)
gen_statemachines_Any_AbstractNode = Generalization(general=AbstractNode, specific=statemachines_Any)
gen_statemachines_Junction_AbstractNode = Generalization(general=AbstractNode, specific=statemachines_Junction)
gen_statemachines_Fork_AbstractNode = Generalization(general=AbstractNode, specific=statemachines_Fork)

# Domain Model
domain_model = DomainModel(
    name="statemachines",
    types={statemachines_Statemachine, EventBNamedCommentedDataElaborationElement, AbstractExtension, Diagram, statemachines_AbstractNode, statemachines_Transition, statemachines_EventBNamedCommentedElement, statemachines_StatemachineOwner, EventBCommentedLabeledEventGroupElement, statemachines_EventBElement, Invariant, EventBElement, statemachines_State, AbstractNode, EventBNamed, StatemachineOwner, statemachines_Initial, statemachines_Final, statemachines_Any, statemachines_Junction, statemachines_Fork, TranslationKind},
    associations={refines1, instances6, nodes2, transitions4, targetContainer15, statemachines8, target10, source11, sourceContainer13, invariants23, incoming18, outgoing19, refines22},
    generalizations={gen_statemachines_Statemachine_EventBNamedCommentedDataElaborationElement, gen_statemachines_Statemachine_AbstractExtension, gen_statemachines_Statemachine_Diagram, gen_statemachines_Transition_EventBCommentedLabeledEventGroupElement, gen_statemachines_AbstractNode_EventBElement, gen_statemachines_State_AbstractNode, gen_statemachines_State_EventBNamed, gen_statemachines_State_StatemachineOwner, gen_statemachines_Initial_AbstractNode, gen_statemachines_Final_AbstractNode, gen_statemachines_Any_AbstractNode, gen_statemachines_Junction_AbstractNode, gen_statemachines_Fork_AbstractNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)