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
EntryKind: Enumeration = Enumeration(
    name="EntryKind",
    literals={
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="deepHistory")
    }
)

ChoiceKind: Enumeration = Enumeration(
    name="ChoiceKind",
    literals={
            EnumerationLiteral(name="dynamic"),
			EnumerationLiteral(name="static")
    }
)

# Classes
sgraph_Pseudostate = Class(name="sgraph_Pseudostate", is_abstract=True)
Vertex = Class(name="Vertex")
sgraph_Vertex = Class(name="sgraph_Vertex", is_abstract=True)
NamedElement = Class(name="NamedElement")
sgraph_CompositeElement = Class(name="sgraph_CompositeElement", is_abstract=True)
SpecificationElement = Class(name="SpecificationElement")
Reaction = Class(name="Reaction")
sgraph_Region = Class(name="sgraph_Region")
sgraph_Transition = Class(name="sgraph_Transition")
sgraph_FinalState = Class(name="sgraph_FinalState")
RegularState = Class(name="RegularState")
sgraph_Variable = Class(name="sgraph_Variable", is_abstract=True)
Declaration = Class(name="Declaration")
sgraph_Event = Class(name="sgraph_Event", is_abstract=True)
sgraph_Choice = Class(name="sgraph_Choice")
Pseudostate = Class(name="Pseudostate")
sgraph_Statechart = Class(name="sgraph_Statechart")
ReactiveElement = Class(name="ReactiveElement")
ScopedElement = Class(name="ScopedElement")
CompositeElement = Class(name="CompositeElement")
sgraph_Entry = Class(name="sgraph_Entry")
sgraph_Trigger = Class(name="sgraph_Trigger", is_abstract=True)
sgraph_Effect = Class(name="sgraph_Effect", is_abstract=True)
sgraph_SpecificationElement = Class(name="sgraph_SpecificationElement", is_abstract=True)
sgraph_Declaration = Class(name="sgraph_Declaration", is_abstract=True)
sgraph_Reaction = Class(name="sgraph_Reaction", is_abstract=True)
sgraph_Exit = Class(name="sgraph_Exit")
sgraph_Scope = Class(name="sgraph_Scope")
sgraph_ScopedElement = Class(name="sgraph_ScopedElement", is_abstract=True)
sgraph_Synchronization = Class(name="sgraph_Synchronization")
sgraph_State = Class(name="sgraph_State")
sgraph_Statement = Class(name="sgraph_Statement")
sgraph_RegularState = Class(name="sgraph_RegularState")
sgraph_ReactiveElement = Class(name="sgraph_ReactiveElement", is_abstract=True)

# sgraph_Pseudostate class attributes and methods

# Vertex class attributes and methods

# sgraph_Vertex class attributes and methods

# NamedElement class attributes and methods

# sgraph_CompositeElement class attributes and methods

# SpecificationElement class attributes and methods

# Reaction class attributes and methods

# sgraph_Region class attributes and methods
sgraph_Region_priority: Property = Property(name="priority", type=IntegerType)
sgraph_Region.attributes={sgraph_Region_priority}

# sgraph_Transition class attributes and methods
sgraph_Transition_priority: Property = Property(name="priority", type=IntegerType)
sgraph_Transition.attributes={sgraph_Transition_priority}

# sgraph_FinalState class attributes and methods

# RegularState class attributes and methods

# sgraph_Variable class attributes and methods

# Declaration class attributes and methods

# sgraph_Event class attributes and methods

# sgraph_Choice class attributes and methods
sgraph_Choice_kind: Property = Property(name="kind", type=StringType)
sgraph_Choice.attributes={sgraph_Choice_kind}

# Pseudostate class attributes and methods

# sgraph_Statechart class attributes and methods

# ReactiveElement class attributes and methods

# ScopedElement class attributes and methods

# CompositeElement class attributes and methods

# sgraph_Entry class attributes and methods
sgraph_Entry_kind: Property = Property(name="kind", type=StringType)
sgraph_Entry.attributes={sgraph_Entry_kind}

# sgraph_Trigger class attributes and methods

# sgraph_Effect class attributes and methods

# sgraph_SpecificationElement class attributes and methods
sgraph_SpecificationElement_specification: Property = Property(name="specification", type=StringType)
sgraph_SpecificationElement.attributes={sgraph_SpecificationElement_specification}

# sgraph_Declaration class attributes and methods

# sgraph_Reaction class attributes and methods

# sgraph_Exit class attributes and methods

# sgraph_Scope class attributes and methods

# sgraph_ScopedElement class attributes and methods
sgraph_ScopedElement_namespace: Property = Property(name="namespace", type=StringType)
sgraph_ScopedElement.attributes={sgraph_ScopedElement_namespace}

# sgraph_Synchronization class attributes and methods

# sgraph_State class attributes and methods
sgraph_State_orthogonal: Property = Property(name="orthogonal", type=BooleanType)
sgraph_State_substatechartId: Property = Property(name="substatechartId", type=StringType)
sgraph_State_subchart: Property = Property(name="subchart", type=BooleanType)
sgraph_State_simple: Property = Property(name="simple", type=BooleanType)
sgraph_State_composite: Property = Property(name="composite", type=BooleanType)
sgraph_State_leaf: Property = Property(name="leaf", type=BooleanType)
sgraph_State.attributes={sgraph_State_subchart, sgraph_State_composite, sgraph_State_simple, sgraph_State_leaf, sgraph_State_substatechartId, sgraph_State_orthogonal}

# sgraph_Statement class attributes and methods

# sgraph_RegularState class attributes and methods

# sgraph_ReactiveElement class attributes and methods

# Relationships
outgoingTransitions2: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions2",
    ends={
        Property(name="Transition3", type=sgraph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=sgraph_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertices4: BinaryAssociation = BinaryAssociation(
    name="vertices4",
    ends={
        Property(name="Vertex", type=sgraph_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="parentRegion", type=sgraph_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
composite5: BinaryAssociation = BinaryAssociation(
    name="composite5",
    ends={
        Property(name="CompositeElement", type=sgraph_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="regions", type=sgraph_CompositeElement, multiplicity=Multiplicity(1, 1))
    }
)
parentRegion0: BinaryAssociation = BinaryAssociation(
    name="parentRegion0",
    ends={
        Property(name="Region", type=sgraph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertices", type=sgraph_Region, multiplicity=Multiplicity(1, 1))
    }
)
incomingTransitions1: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions1",
    ends={
        Property(name="Transition", type=sgraph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=sgraph_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="outgoingTransitions", type=sgraph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="Vertex9", type=sgraph_Transition, multiplicity=Multiplicity(1, 1))
    }
)
trigger10: BinaryAssociation = BinaryAssociation(
    name="trigger10",
    ends={
        Property(name="sgraph_Trigger", type=sgraph_Reaction, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Reaction", type=sgraph_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect11: BinaryAssociation = BinaryAssociation(
    name="effect11",
    ends={
        Property(name="sgraph_Effect", type=sgraph_Reaction, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Reaction12", type=sgraph_Effect, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="Vertex7", type=sgraph_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=sgraph_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
localReactions15: BinaryAssociation = BinaryAssociation(
    name="localReactions15",
    ends={
        Property(name="sgraph_Reaction17", type=sgraph_ReactiveElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_ReactiveElement16", type=sgraph_Reaction, multiplicity=Multiplicity(0, 9999))
    }
)
declarations18: BinaryAssociation = BinaryAssociation(
    name="declarations18",
    ends={
        Property(name="sgraph_Declaration", type=sgraph_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Scope", type=sgraph_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events19: BinaryAssociation = BinaryAssociation(
    name="events19",
    ends={
        Property(name="sgraph_Event", type=sgraph_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Scope20", type=sgraph_Event, multiplicity=Multiplicity(0, 9999))
    }
)
variables21: BinaryAssociation = BinaryAssociation(
    name="variables21",
    ends={
        Property(name="sgraph_Variable", type=sgraph_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Scope22", type=sgraph_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
scopes23: BinaryAssociation = BinaryAssociation(
    name="scopes23",
    ends={
        Property(name="sgraph_Scope24", type=sgraph_ScopedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_ScopedElement", type=sgraph_Scope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substatechart25: BinaryAssociation = BinaryAssociation(
    name="substatechart25",
    ends={
        Property(name="sgraph_Statechart", type=sgraph_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_State", type=sgraph_Statechart, multiplicity=Multiplicity(0, 1))
    }
)
reactions13: BinaryAssociation = BinaryAssociation(
    name="reactions13",
    ends={
        Property(name="sgraph_Reaction14", type=sgraph_ReactiveElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_ReactiveElement", type=sgraph_Reaction, multiplicity=Multiplicity(0, 9999))
    }
)
regions26: BinaryAssociation = BinaryAssociation(
    name="regions26",
    ends={
        Property(name="Region27", type=sgraph_CompositeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="composite", type=sgraph_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sgraph_Pseudostate_Vertex = Generalization(general=Vertex, specific=sgraph_Pseudostate)
gen_sgraph_Vertex_NamedElement = Generalization(general=NamedElement, specific=sgraph_Vertex)
gen_sgraph_Region_NamedElement = Generalization(general=NamedElement, specific=sgraph_Region)
gen_sgraph_Transition_SpecificationElement = Generalization(general=SpecificationElement, specific=sgraph_Transition)
gen_sgraph_Transition_Reaction = Generalization(general=Reaction, specific=sgraph_Transition)
gen_sgraph_FinalState_RegularState = Generalization(general=RegularState, specific=sgraph_FinalState)
gen_sgraph_Variable_Declaration = Generalization(general=Declaration, specific=sgraph_Variable)
gen_sgraph_Event_Declaration = Generalization(general=Declaration, specific=sgraph_Event)
gen_sgraph_Choice_Pseudostate = Generalization(general=Pseudostate, specific=sgraph_Choice)
gen_sgraph_Statechart_SpecificationElement = Generalization(general=SpecificationElement, specific=sgraph_Statechart)
gen_sgraph_Statechart_ReactiveElement = Generalization(general=ReactiveElement, specific=sgraph_Statechart)
gen_sgraph_Statechart_ScopedElement = Generalization(general=ScopedElement, specific=sgraph_Statechart)
gen_sgraph_Statechart_CompositeElement = Generalization(general=CompositeElement, specific=sgraph_Statechart)
gen_sgraph_Statechart_NamedElement = Generalization(general=NamedElement, specific=sgraph_Statechart)
gen_sgraph_Entry_Pseudostate = Generalization(general=Pseudostate, specific=sgraph_Entry)
gen_sgraph_Declaration_NamedElement = Generalization(general=NamedElement, specific=sgraph_Declaration)
gen_sgraph_Exit_Pseudostate = Generalization(general=Pseudostate, specific=sgraph_Exit)
gen_sgraph_Synchronization_Pseudostate = Generalization(general=Pseudostate, specific=sgraph_Synchronization)
gen_sgraph_State_SpecificationElement = Generalization(general=SpecificationElement, specific=sgraph_State)
gen_sgraph_State_ReactiveElement = Generalization(general=ReactiveElement, specific=sgraph_State)
gen_sgraph_State_ScopedElement = Generalization(general=ScopedElement, specific=sgraph_State)
gen_sgraph_State_RegularState = Generalization(general=RegularState, specific=sgraph_State)
gen_sgraph_State_CompositeElement = Generalization(general=CompositeElement, specific=sgraph_State)
gen_sgraph_RegularState_Vertex = Generalization(general=Vertex, specific=sgraph_RegularState)

# Domain Model
domain_model = DomainModel(
    name="sgraph",
    types={sgraph_Pseudostate, Vertex, sgraph_Vertex, NamedElement, sgraph_CompositeElement, SpecificationElement, Reaction, sgraph_Region, sgraph_Transition, sgraph_FinalState, RegularState, sgraph_Variable, Declaration, sgraph_Event, sgraph_Choice, Pseudostate, sgraph_Statechart, ReactiveElement, ScopedElement, CompositeElement, sgraph_Entry, sgraph_Trigger, sgraph_Effect, sgraph_SpecificationElement, sgraph_Declaration, sgraph_Reaction, sgraph_Exit, sgraph_Scope, sgraph_ScopedElement, sgraph_Synchronization, sgraph_State, sgraph_Statement, sgraph_RegularState, sgraph_ReactiveElement, EntryKind, ChoiceKind},
    associations={outgoingTransitions2, vertices4, composite5, parentRegion0, incomingTransitions1, source8, trigger10, effect11, target6, localReactions15, declarations18, events19, variables21, scopes23, substatechart25, reactions13, regions26},
    generalizations={gen_sgraph_Pseudostate_Vertex, gen_sgraph_Vertex_NamedElement, gen_sgraph_Region_NamedElement, gen_sgraph_Transition_SpecificationElement, gen_sgraph_Transition_Reaction, gen_sgraph_FinalState_RegularState, gen_sgraph_Variable_Declaration, gen_sgraph_Event_Declaration, gen_sgraph_Choice_Pseudostate, gen_sgraph_Statechart_SpecificationElement, gen_sgraph_Statechart_ReactiveElement, gen_sgraph_Statechart_ScopedElement, gen_sgraph_Statechart_CompositeElement, gen_sgraph_Statechart_NamedElement, gen_sgraph_Entry_Pseudostate, gen_sgraph_Declaration_NamedElement, gen_sgraph_Exit_Pseudostate, gen_sgraph_Synchronization_Pseudostate, gen_sgraph_State_SpecificationElement, gen_sgraph_State_ReactiveElement, gen_sgraph_State_ScopedElement, gen_sgraph_State_RegularState, gen_sgraph_State_CompositeElement, gen_sgraph_RegularState_Vertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)