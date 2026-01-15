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
sgraph_Pseudostate = Class(name="sgraph::Pseudostate", is_abstract=True)
Vertex = Class(name="Vertex")
sgraph_Vertex = Class(name="sgraph::Vertex", is_abstract=True)
NamedElement = Class(name="NamedElement")
sgraph_Region = Class(name="sgraph::Region")
sgraph_Transition = Class(name="sgraph::Transition")
sgraph_CompositeElement = Class(name="sgraph::CompositeElement", is_abstract=True)
SpecificationElement = Class(name="SpecificationElement")
Reaction = Class(name="Reaction")
DocumentedElement = Class(name="DocumentedElement")
sgraph_FinalState = Class(name="sgraph::FinalState")
RegularState = Class(name="RegularState")
sgraph_Choice = Class(name="sgraph::Choice")
Pseudostate = Class(name="Pseudostate")
sgraph_Statechart = Class(name="sgraph::Statechart")
ReactiveElement = Class(name="ReactiveElement")
ScopedElement = Class(name="ScopedElement")
CompositeElement = Class(name="CompositeElement")
DomainElement = Class(name="DomainElement")
sgraph_Entry = Class(name="sgraph::Entry")
sgraph_Exit = Class(name="sgraph::Exit")
sgraph_ReactiveElement = Class(name="sgraph::ReactiveElement", is_abstract=True)
sgraph_Reaction = Class(name="sgraph::Reaction", is_abstract=True)
sgraph_Trigger = Class(name="sgraph::Trigger", is_abstract=True)
sgraph_Effect = Class(name="sgraph::Effect", is_abstract=True)
sgraph_ReactionProperty = Class(name="sgraph::ReactionProperty")
sgraph_SpecificationElement = Class(name="sgraph::SpecificationElement", is_abstract=True)
sgraph_Scope = Class(name="sgraph::Scope")
sgraph_Declaration = Class(name="sgraph::Declaration")
sgraph_Event = Class(name="sgraph::Event")
sgraph_Property = Class(name="sgraph::Property")
sgraph_ScopedElement = Class(name="sgraph::ScopedElement", is_abstract=True)
sgraph_Synchronization = Class(name="sgraph::Synchronization")
sgraph_State = Class(name="sgraph::State")
sgraph_RegularState = Class(name="sgraph::RegularState", is_abstract=True)
sgraph_ImportDeclaration = Class(name="sgraph::ImportDeclaration")
Declaration = Class(name="Declaration")

# sgraph_Pseudostate class attributes and methods

# Vertex class attributes and methods

# sgraph_Vertex class attributes and methods

# NamedElement class attributes and methods

# sgraph_Region class attributes and methods

# sgraph_Transition class attributes and methods

# sgraph_CompositeElement class attributes and methods

# SpecificationElement class attributes and methods

# Reaction class attributes and methods

# DocumentedElement class attributes and methods

# sgraph_FinalState class attributes and methods

# RegularState class attributes and methods

# sgraph_Choice class attributes and methods
sgraph_Choice_kind: Property = Property(name="kind", type=StringType)
sgraph_Choice.attributes={sgraph_Choice_kind}

# Pseudostate class attributes and methods

# sgraph_Statechart class attributes and methods

# ReactiveElement class attributes and methods

# ScopedElement class attributes and methods

# CompositeElement class attributes and methods

# DomainElement class attributes and methods

# sgraph_Entry class attributes and methods
sgraph_Entry_kind: Property = Property(name="kind", type=StringType)
sgraph_Entry.attributes={sgraph_Entry_kind}

# sgraph_Exit class attributes and methods

# sgraph_ReactiveElement class attributes and methods

# sgraph_Reaction class attributes and methods

# sgraph_Trigger class attributes and methods

# sgraph_Effect class attributes and methods

# sgraph_ReactionProperty class attributes and methods

# sgraph_SpecificationElement class attributes and methods
sgraph_SpecificationElement_specification: Property = Property(name="specification", type=StringType)
sgraph_SpecificationElement.attributes={sgraph_SpecificationElement_specification}

# sgraph_Scope class attributes and methods

# sgraph_Declaration class attributes and methods

# sgraph_Event class attributes and methods

# sgraph_Property class attributes and methods

# sgraph_ScopedElement class attributes and methods
sgraph_ScopedElement_namespace: Property = Property(name="namespace", type=StringType)
sgraph_ScopedElement.attributes={sgraph_ScopedElement_namespace}

# sgraph_Synchronization class attributes and methods

# sgraph_State class attributes and methods
sgraph_State_orthogonal: Property = Property(name="orthogonal", type=BooleanType)
sgraph_State_simple: Property = Property(name="simple", type=BooleanType)
sgraph_State_composite: Property = Property(name="composite", type=BooleanType)
sgraph_State_leaf: Property = Property(name="leaf", type=BooleanType)
sgraph_State.attributes={sgraph_State_leaf, sgraph_State_simple, sgraph_State_orthogonal, sgraph_State_composite}

# sgraph_RegularState class attributes and methods

# sgraph_ImportDeclaration class attributes and methods

# Declaration class attributes and methods

# Relationships
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
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="Vertex7", type=sgraph_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=sgraph_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="Vertex9", type=sgraph_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=sgraph_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
localReactions10: BinaryAssociation = BinaryAssociation(
    name="localReactions10",
    ends={
        Property(name="sgraph_Reaction", type=sgraph_ReactiveElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_ReactiveElement", type=sgraph_Reaction, multiplicity=Multiplicity(0, 9999))
    }
)
trigger11: BinaryAssociation = BinaryAssociation(
    name="trigger11",
    ends={
        Property(name="sgraph_Trigger", type=sgraph_Reaction, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Reaction12", type=sgraph_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect13: BinaryAssociation = BinaryAssociation(
    name="effect13",
    ends={
        Property(name="sgraph_Effect", type=sgraph_Reaction, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Reaction14", type=sgraph_Effect, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties15: BinaryAssociation = BinaryAssociation(
    name="properties15",
    ends={
        Property(name="sgraph_ReactionProperty", type=sgraph_Reaction, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Reaction16", type=sgraph_ReactionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations17: BinaryAssociation = BinaryAssociation(
    name="declarations17",
    ends={
        Property(name="sgraph_Declaration", type=sgraph_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Scope", type=sgraph_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events18: BinaryAssociation = BinaryAssociation(
    name="events18",
    ends={
        Property(name="sgraph_Event", type=sgraph_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Scope19", type=sgraph_Event, multiplicity=Multiplicity(0, 9999))
    }
)
variables20: BinaryAssociation = BinaryAssociation(
    name="variables20",
    ends={
        Property(name="sgraph_Property", type=sgraph_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Scope21", type=sgraph_Property, multiplicity=Multiplicity(0, 9999))
    }
)
reactions22: BinaryAssociation = BinaryAssociation(
    name="reactions22",
    ends={
        Property(name="sgraph_Reaction24", type=sgraph_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_Scope23", type=sgraph_Reaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopes25: BinaryAssociation = BinaryAssociation(
    name="scopes25",
    ends={
        Property(name="sgraph_Scope26", type=sgraph_ScopedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_ScopedElement", type=sgraph_Scope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regions27: BinaryAssociation = BinaryAssociation(
    name="regions27",
    ends={
        Property(name="Region28", type=sgraph_CompositeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="composite", type=sgraph_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration29: BinaryAssociation = BinaryAssociation(
    name="declaration29",
    ends={
        Property(name="sgraph_Declaration30", type=sgraph_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sgraph_ImportDeclaration", type=sgraph_Declaration, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sgraph_Pseudostate_Vertex = Generalization(general=Vertex, specific=sgraph_Pseudostate)
gen_sgraph_Vertex_NamedElement = Generalization(general=NamedElement, specific=sgraph_Vertex)
gen_sgraph_Region_NamedElement = Generalization(general=NamedElement, specific=sgraph_Region)
gen_sgraph_Transition_SpecificationElement = Generalization(general=SpecificationElement, specific=sgraph_Transition)
gen_sgraph_Transition_Reaction = Generalization(general=Reaction, specific=sgraph_Transition)
gen_sgraph_Transition_DocumentedElement = Generalization(general=DocumentedElement, specific=sgraph_Transition)
gen_sgraph_FinalState_RegularState = Generalization(general=RegularState, specific=sgraph_FinalState)
gen_sgraph_Choice_Pseudostate = Generalization(general=Pseudostate, specific=sgraph_Choice)
gen_sgraph_Statechart_SpecificationElement = Generalization(general=SpecificationElement, specific=sgraph_Statechart)
gen_sgraph_Statechart_ReactiveElement = Generalization(general=ReactiveElement, specific=sgraph_Statechart)
gen_sgraph_Statechart_ScopedElement = Generalization(general=ScopedElement, specific=sgraph_Statechart)
gen_sgraph_Statechart_CompositeElement = Generalization(general=CompositeElement, specific=sgraph_Statechart)
gen_sgraph_Statechart_NamedElement = Generalization(general=NamedElement, specific=sgraph_Statechart)
gen_sgraph_Statechart_DocumentedElement = Generalization(general=DocumentedElement, specific=sgraph_Statechart)
gen_sgraph_Statechart_DomainElement = Generalization(general=DomainElement, specific=sgraph_Statechart)
gen_sgraph_Entry_Pseudostate = Generalization(general=Pseudostate, specific=sgraph_Entry)
gen_sgraph_Exit_Pseudostate = Generalization(general=Pseudostate, specific=sgraph_Exit)
gen_sgraph_State_DocumentedElement = Generalization(general=DocumentedElement, specific=sgraph_State)
gen_sgraph_Synchronization_Pseudostate = Generalization(general=Pseudostate, specific=sgraph_Synchronization)
gen_sgraph_State_SpecificationElement = Generalization(general=SpecificationElement, specific=sgraph_State)
gen_sgraph_State_ReactiveElement = Generalization(general=ReactiveElement, specific=sgraph_State)
gen_sgraph_State_ScopedElement = Generalization(general=ScopedElement, specific=sgraph_State)
gen_sgraph_State_RegularState = Generalization(general=RegularState, specific=sgraph_State)
gen_sgraph_State_CompositeElement = Generalization(general=CompositeElement, specific=sgraph_State)
gen_sgraph_RegularState_Vertex = Generalization(general=Vertex, specific=sgraph_RegularState)
gen_sgraph_ImportDeclaration_Declaration = Generalization(general=Declaration, specific=sgraph_ImportDeclaration)

# Domain Model
domain_model = DomainModel(
    name="sgraph",
    types={sgraph_Pseudostate, Vertex, sgraph_Vertex, NamedElement, sgraph_Region, sgraph_Transition, sgraph_CompositeElement, SpecificationElement, Reaction, DocumentedElement, sgraph_FinalState, RegularState, sgraph_Choice, Pseudostate, sgraph_Statechart, ReactiveElement, ScopedElement, CompositeElement, DomainElement, sgraph_Entry, sgraph_Exit, sgraph_ReactiveElement, sgraph_Reaction, sgraph_Trigger, sgraph_Effect, sgraph_ReactionProperty, sgraph_SpecificationElement, sgraph_Scope, sgraph_Declaration, sgraph_Event, sgraph_Property, sgraph_ScopedElement, sgraph_Synchronization, sgraph_State, sgraph_RegularState, sgraph_ImportDeclaration, Declaration, EntryKind, ChoiceKind},
    associations={parentRegion0, incomingTransitions1, outgoingTransitions2, vertices4, composite5, target6, source8, localReactions10, trigger11, effect13, properties15, declarations17, events18, variables20, reactions22, scopes25, regions27, declaration29},
    generalizations={gen_sgraph_Pseudostate_Vertex, gen_sgraph_Vertex_NamedElement, gen_sgraph_Region_NamedElement, gen_sgraph_Transition_SpecificationElement, gen_sgraph_Transition_Reaction, gen_sgraph_Transition_DocumentedElement, gen_sgraph_FinalState_RegularState, gen_sgraph_Choice_Pseudostate, gen_sgraph_Statechart_SpecificationElement, gen_sgraph_Statechart_ReactiveElement, gen_sgraph_Statechart_ScopedElement, gen_sgraph_Statechart_CompositeElement, gen_sgraph_Statechart_NamedElement, gen_sgraph_Statechart_DocumentedElement, gen_sgraph_Statechart_DomainElement, gen_sgraph_Entry_Pseudostate, gen_sgraph_Exit_Pseudostate, gen_sgraph_State_DocumentedElement, gen_sgraph_Synchronization_Pseudostate, gen_sgraph_State_SpecificationElement, gen_sgraph_State_ReactiveElement, gen_sgraph_State_ScopedElement, gen_sgraph_State_RegularState, gen_sgraph_State_CompositeElement, gen_sgraph_RegularState_Vertex, gen_sgraph_ImportDeclaration_Declaration},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)