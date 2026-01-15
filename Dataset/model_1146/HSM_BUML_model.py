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
hsm_StateMachine = Class(name="hsm::StateMachine")
hsm_Transition = Class(name="hsm::Transition")
hsm_AbstractState = Class(name="hsm::AbstractState", is_abstract=True)
hsm_CompositeState = Class(name="hsm::CompositeState")
hsm_InitialState = Class(name="hsm::InitialState")
AbstractState = Class(name="AbstractState")
hsm_RegularState = Class(name="hsm::RegularState")
hsm_Root = Class(name="hsm::Root")

# hsm_StateMachine class attributes and methods
hsm_StateMachine_name: Property = Property(name="name", type=StringType)
hsm_StateMachine.attributes={hsm_StateMachine_name}

# hsm_Transition class attributes and methods
hsm_Transition_label: Property = Property(name="label", type=StringType)
hsm_Transition.attributes={hsm_Transition_label}

# hsm_AbstractState class attributes and methods
hsm_AbstractState_name: Property = Property(name="name", type=StringType)
hsm_AbstractState.attributes={hsm_AbstractState_name}

# hsm_CompositeState class attributes and methods

# hsm_InitialState class attributes and methods

# AbstractState class attributes and methods

# hsm_RegularState class attributes and methods

# hsm_Root class attributes and methods

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="Transition", type=hsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=hsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="AbstractState", type=hsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine2", type=hsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine3: BinaryAssociation = BinaryAssociation(
    name="stateMachine3",
    ends={
        Property(name="StateMachine", type=hsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=hsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="hsm_AbstractState", type=hsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="hsm_Transition", type=hsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
compositeStates10: BinaryAssociation = BinaryAssociation(
    name="compositeStates10",
    ends={
        Property(name="CompositeState", type=hsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states11", type=hsm_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
states12: BinaryAssociation = BinaryAssociation(
    name="states12",
    ends={
        Property(name="AbstractState13", type=hsm_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeStates", type=hsm_AbstractState, multiplicity=Multiplicity(0, 9999))
    }
)
statemachines14: BinaryAssociation = BinaryAssociation(
    name="statemachines14",
    ends={
        Property(name="hsm_StateMachine", type=hsm_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="hsm_Root", type=hsm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="hsm_AbstractState7", type=hsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="hsm_Transition6", type=hsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
stateMachine8: BinaryAssociation = BinaryAssociation(
    name="stateMachine8",
    ends={
        Property(name="StateMachine9", type=hsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=hsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_hsm_InitialState_AbstractState = Generalization(general=AbstractState, specific=hsm_InitialState)
gen_hsm_RegularState_AbstractState = Generalization(general=AbstractState, specific=hsm_RegularState)
gen_hsm_CompositeState_AbstractState = Generalization(general=AbstractState, specific=hsm_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="hsm",
    types={hsm_StateMachine, hsm_Transition, hsm_AbstractState, hsm_CompositeState, hsm_InitialState, AbstractState, hsm_RegularState, hsm_Root},
    associations={transitions0, states1, stateMachine3, source4, compositeStates10, states12, statemachines14, target5, stateMachine8},
    generalizations={gen_hsm_InitialState_AbstractState, gen_hsm_RegularState_AbstractState, gen_hsm_CompositeState_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)