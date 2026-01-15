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
PseudoStateType: Enumeration = Enumeration(
    name="PseudoStateType",
    literals={
            EnumerationLiteral(name="Initial"),
			EnumerationLiteral(name="Junction"),
			EnumerationLiteral(name="ShadowHistory"),
			EnumerationLiteral(name="DeepHistory"),
			EnumerationLiteral(name="Terminate"),
			EnumerationLiteral(name="EntryPoint"),
			EnumerationLiteral(name="ExitPoint"),
			EnumerationLiteral(name="Choice"),
			EnumerationLiteral(name="Join"),
			EnumerationLiteral(name="Fork")
    }
)

# Classes
stateChart_Vertex = Class(name="stateChart::Vertex", is_abstract=True)
stateChart_PseudoState = Class(name="stateChart::PseudoState")
Vertex = Class(name="Vertex")
stateChart_SimpleState = Class(name="stateChart::SimpleState")
State = Class(name="State")
stateChart_FinalState = Class(name="stateChart::FinalState")
stateChart_Region = Class(name="stateChart::Region")
stateChart_State = Class(name="stateChart::State", is_abstract=True)
stateChart_Transient = Class(name="stateChart::Transient")
stateChart_StateMachine = Class(name="stateChart::StateMachine")
stateChart_CompositeState = Class(name="stateChart::CompositeState")

# stateChart_Vertex class attributes and methods
stateChart_Vertex_note: Property = Property(name="note", type=StringType)
stateChart_Vertex_name: Property = Property(name="name", type=StringType)
stateChart_Vertex_isActive: Property = Property(name="isActive", type=BooleanType)
stateChart_Vertex.attributes={stateChart_Vertex_note, stateChart_Vertex_isActive, stateChart_Vertex_name}

# stateChart_PseudoState class attributes and methods
stateChart_PseudoState_PseudoStateType: Property = Property(name="PseudoStateType", type=StringType)
stateChart_PseudoState.attributes={stateChart_PseudoState_PseudoStateType}

# Vertex class attributes and methods

# stateChart_SimpleState class attributes and methods

# State class attributes and methods

# stateChart_FinalState class attributes and methods

# stateChart_Region class attributes and methods
stateChart_Region_name: Property = Property(name="name", type=StringType)
stateChart_Region_note: Property = Property(name="note", type=StringType)
stateChart_Region.attributes={stateChart_Region_note, stateChart_Region_name}

# stateChart_State class attributes and methods
stateChart_State_exit: Property = Property(name="exit", type=StringType)
stateChart_State_action: Property = Property(name="action", type=StringType)
stateChart_State_entry: Property = Property(name="entry", type=StringType)
stateChart_State.attributes={stateChart_State_exit, stateChart_State_action, stateChart_State_entry}

# stateChart_Transient class attributes and methods
stateChart_Transient_name: Property = Property(name="name", type=StringType)
stateChart_Transient_trigger: Property = Property(name="trigger", type=StringType)
stateChart_Transient_guard: Property = Property(name="guard", type=StringType)
stateChart_Transient_effect: Property = Property(name="effect", type=StringType)
stateChart_Transient_priority: Property = Property(name="priority", type=IntegerType)
stateChart_Transient.attributes={stateChart_Transient_trigger, stateChart_Transient_priority, stateChart_Transient_guard, stateChart_Transient_name, stateChart_Transient_effect}

# stateChart_StateMachine class attributes and methods
stateChart_StateMachine_name: Property = Property(name="name", type=StringType)
stateChart_StateMachine.attributes={stateChart_StateMachine_name}

# stateChart_CompositeState class attributes and methods

# Relationships
vertex1: BinaryAssociation = BinaryAssociation(
    name="vertex1",
    ends={
        Property(name="stateChart_Region2", type=stateChart_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="stateChart_Vertex", type=stateChart_Region, multiplicity=Multiplicity(1, 1))
    }
)
transient0: BinaryAssociation = BinaryAssociation(
    name="transient0",
    ends={
        Property(name="stateChart_Transient", type=stateChart_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Region", type=stateChart_Transient, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainRegion9: BinaryAssociation = BinaryAssociation(
    name="mainRegion9",
    ends={
        Property(name="stateChart_Region10", type=stateChart_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_StateMachine", type=stateChart_Region, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="stateChart_Vertex5", type=stateChart_Transient, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Transient4", type=stateChart_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="stateChart_Vertex8", type=stateChart_Transient, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Transient7", type=stateChart_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
element11: BinaryAssociation = BinaryAssociation(
    name="element11",
    ends={
        Property(name="stateChart_Region12", type=stateChart_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_CompositeState", type=stateChart_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_stateChart_PseudoState_Vertex = Generalization(general=Vertex, specific=stateChart_PseudoState)
gen_stateChart_SimpleState_State = Generalization(general=State, specific=stateChart_SimpleState)
gen_stateChart_FinalState_State = Generalization(general=State, specific=stateChart_FinalState)
gen_stateChart_State_Vertex = Generalization(general=Vertex, specific=stateChart_State)
gen_stateChart_CompositeState_State = Generalization(general=State, specific=stateChart_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="stateChart",
    types={stateChart_Vertex, stateChart_PseudoState, Vertex, stateChart_SimpleState, State, stateChart_FinalState, stateChart_Region, stateChart_State, stateChart_Transient, stateChart_StateMachine, stateChart_CompositeState, PseudoStateType},
    associations={vertex1, transient0, mainRegion9, source3, target6, element11},
    generalizations={gen_stateChart_PseudoState_Vertex, gen_stateChart_SimpleState_State, gen_stateChart_FinalState_State, gen_stateChart_State_Vertex, gen_stateChart_CompositeState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)