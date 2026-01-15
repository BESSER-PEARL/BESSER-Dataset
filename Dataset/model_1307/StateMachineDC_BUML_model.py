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
SimplStateMachineDC_InitialState = Class(name="SimplStateMachineDC::InitialState")
SimplStateMachineDC_StateMachine = Class(name="SimplStateMachineDC::StateMachine")
SimplStateMachineDC_Transition = Class(name="SimplStateMachineDC::Transition")
SimplStateMachineDC_State = Class(name="SimplStateMachineDC::State")
SimplStateMachineDC_CompositeState = Class(name="SimplStateMachineDC::CompositeState")
State = Class(name="State")
SimplStateMachineDC_PseudoState = Class(name="SimplStateMachineDC::PseudoState", is_abstract=True)
PseudoState = Class(name="PseudoState")

# SimplStateMachineDC_InitialState class attributes and methods

# SimplStateMachineDC_StateMachine class attributes and methods

# SimplStateMachineDC_Transition class attributes and methods
SimplStateMachineDC_Transition_event: Property = Property(name="event", type=StringType)
SimplStateMachineDC_Transition.attributes={SimplStateMachineDC_Transition_event}

# SimplStateMachineDC_State class attributes and methods
SimplStateMachineDC_State_name: Property = Property(name="name", type=StringType)
SimplStateMachineDC_State_isActive: Property = Property(name="isActive", type=BooleanType)
SimplStateMachineDC_State_Ord: Property = Property(name="Ord", type=StringType)
SimplStateMachineDC_State_Inh: Property = Property(name="Inh", type=StringType)
SimplStateMachineDC_State_OrdIf: Property = Property(name="OrdIf", type=StringType)
SimplStateMachineDC_State_InhIf: Property = Property(name="InhIf", type=StringType)
SimplStateMachineDC_State.attributes={SimplStateMachineDC_State_name, SimplStateMachineDC_State_OrdIf, SimplStateMachineDC_State_isActive, SimplStateMachineDC_State_Ord, SimplStateMachineDC_State_InhIf, SimplStateMachineDC_State_Inh}

# SimplStateMachineDC_CompositeState class attributes and methods

# State class attributes and methods

# SimplStateMachineDC_PseudoState class attributes and methods

# PseudoState class attributes and methods

# Relationships
initialState5: BinaryAssociation = BinaryAssociation(
    name="initialState5",
    ends={
        Property(name="SimplStateMachineDC_InitialState", type=SimplStateMachineDC_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachineDC_CompositeState", type=SimplStateMachineDC_InitialState, multiplicity=Multiplicity(1, 1))
    }
)
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="SimplStateMachineDC_Transition", type=SimplStateMachineDC_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachineDC_StateMachine", type=SimplStateMachineDC_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="SimplStateMachineDC_State", type=SimplStateMachineDC_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachineDC_StateMachine2", type=SimplStateMachineDC_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container3: BinaryAssociation = BinaryAssociation(
    name="container3",
    ends={
        Property(name="CompositeState", type=SimplStateMachineDC_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=SimplStateMachineDC_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
states4: BinaryAssociation = BinaryAssociation(
    name="states4",
    ends={
        Property(name="State", type=SimplStateMachineDC_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=SimplStateMachineDC_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
referencedState6: BinaryAssociation = BinaryAssociation(
    name="referencedState6",
    ends={
        Property(name="SimplStateMachineDC_State7", type=SimplStateMachineDC_PseudoState, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachineDC_PseudoState", type=SimplStateMachineDC_State, multiplicity=Multiplicity(0, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="SimplStateMachineDC_State10", type=SimplStateMachineDC_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachineDC_Transition9", type=SimplStateMachineDC_State, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="SimplStateMachineDC_State13", type=SimplStateMachineDC_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachineDC_Transition12", type=SimplStateMachineDC_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimplStateMachineDC_CompositeState_State = Generalization(general=State, specific=SimplStateMachineDC_CompositeState)
gen_SimplStateMachineDC_PseudoState_State = Generalization(general=State, specific=SimplStateMachineDC_PseudoState)
gen_SimplStateMachineDC_InitialState_PseudoState = Generalization(general=PseudoState, specific=SimplStateMachineDC_InitialState)

# Domain Model
domain_model = DomainModel(
    name="SimplStateMachineDC",
    types={SimplStateMachineDC_InitialState, SimplStateMachineDC_StateMachine, SimplStateMachineDC_Transition, SimplStateMachineDC_State, SimplStateMachineDC_CompositeState, State, SimplStateMachineDC_PseudoState, PseudoState},
    associations={initialState5, transitions0, states1, container3, states4, referencedState6, source8, target11},
    generalizations={gen_SimplStateMachineDC_CompositeState_State, gen_SimplStateMachineDC_PseudoState_State, gen_SimplStateMachineDC_InitialState_PseudoState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)