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
finitestatemachines_StateMachine = Class(name="finitestatemachines::StateMachine")
NamedElement = Class(name="NamedElement")
finitestatemachines_NamedElement = Class(name="finitestatemachines::NamedElement")
finitestatemachines_FinalState = Class(name="finitestatemachines::FinalState")
finitestatemachines_State2 = Class(name="finitestatemachines::State2")
finitestatemachines_Transition2 = Class(name="finitestatemachines::Transition2")
finitestatemachines_TimedTransition = Class(name="finitestatemachines::TimedTransition")
Transition2 = Class(name="Transition2")
State2 = Class(name="State2")
finitestatemachines_InitialState = Class(name="finitestatemachines::InitialState")
finitestatemachines_Trigger2 = Class(name="finitestatemachines::Trigger2")
finitestatemachines_Pseudostate = Class(name="finitestatemachines::Pseudostate")
finitestatemachines_Fork = Class(name="finitestatemachines::Fork")
Pseudostate = Class(name="Pseudostate")
finitestatemachines_Join2 = Class(name="finitestatemachines::Join2")

# finitestatemachines_StateMachine class attributes and methods

# NamedElement class attributes and methods

# finitestatemachines_NamedElement class attributes and methods
finitestatemachines_NamedElement_name: Property = Property(name="name", type=StringType)
finitestatemachines_NamedElement.attributes={finitestatemachines_NamedElement_name}

# finitestatemachines_FinalState class attributes and methods

# finitestatemachines_State2 class attributes and methods
finitestatemachines_State2_finalTime: Property = Property(name="finalTime", type=IntegerType)
finitestatemachines_State2_initialTime2: Property = Property(name="initialTime2", type=IntegerType)
finitestatemachines_State2.attributes={finitestatemachines_State2_initialTime2, finitestatemachines_State2_finalTime}

# finitestatemachines_Transition2 class attributes and methods
finitestatemachines_Transition2_initialTime: Property = Property(name="initialTime", type=IntegerType)
finitestatemachines_Transition2_finalTime2: Property = Property(name="finalTime2", type=IntegerType)
finitestatemachines_Transition2.attributes={finitestatemachines_Transition2_initialTime, finitestatemachines_Transition2_finalTime2}

# finitestatemachines_TimedTransition class attributes and methods
finitestatemachines_TimedTransition_duration: Property = Property(name="duration", type=IntegerType)
finitestatemachines_TimedTransition.attributes={finitestatemachines_TimedTransition_duration}

# Transition2 class attributes and methods

# State2 class attributes and methods

# finitestatemachines_InitialState class attributes and methods

# finitestatemachines_Trigger2 class attributes and methods
finitestatemachines_Trigger2_expression: Property = Property(name="expression", type=StringType)
finitestatemachines_Trigger2.attributes={finitestatemachines_Trigger2_expression}

# finitestatemachines_Pseudostate class attributes and methods

# finitestatemachines_Fork class attributes and methods

# Pseudostate class attributes and methods

# finitestatemachines_Join2 class attributes and methods

# Relationships
states20: BinaryAssociation = BinaryAssociation(
    name="states20",
    ends={
        Property(name="1", type=finitestatemachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=finitestatemachines_State2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions22: BinaryAssociation = BinaryAssociation(
    name="transitions22",
    ends={
        Property(name="4", type=finitestatemachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=finitestatemachines_Transition2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="7", type=finitestatemachines_State2, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=finitestatemachines_Transition2, multiplicity=Multiplicity(0, 9999))
    }
)
incoming8: BinaryAssociation = BinaryAssociation(
    name="incoming8",
    ends={
        Property(name="10", type=finitestatemachines_State2, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=finitestatemachines_Transition2, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachine211: BinaryAssociation = BinaryAssociation(
    name="stateMachine211",
    ends={
        Property(name="13", type=finitestatemachines_State2, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=finitestatemachines_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="16", type=finitestatemachines_Transition2, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=finitestatemachines_State2, multiplicity=Multiplicity(1, 1))
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="19", type=finitestatemachines_Transition2, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=finitestatemachines_State2, multiplicity=Multiplicity(1, 1))
    }
)
trigger20: BinaryAssociation = BinaryAssociation(
    name="trigger20",
    ends={
        Property(name="finitestatemachines_Trigger2", type=finitestatemachines_Transition2, multiplicity=Multiplicity(1, 1)),
        Property(name="finitestatemachines_Transition2", type=finitestatemachines_Trigger2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateMachine21: BinaryAssociation = BinaryAssociation(
    name="stateMachine21",
    ends={
        Property(name="23", type=finitestatemachines_Transition2, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=finitestatemachines_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_finitestatemachines_StateMachine_NamedElement = Generalization(general=NamedElement, specific=finitestatemachines_StateMachine)
gen_finitestatemachines_State2_NamedElement = Generalization(general=NamedElement, specific=finitestatemachines_State2)
gen_finitestatemachines_TimedTransition_Transition2 = Generalization(general=Transition2, specific=finitestatemachines_TimedTransition)
gen_finitestatemachines_FinalState_State2 = Generalization(general=State2, specific=finitestatemachines_FinalState)
gen_finitestatemachines_InitialState_State2 = Generalization(general=State2, specific=finitestatemachines_InitialState)
gen_finitestatemachines_Transition2_NamedElement = Generalization(general=NamedElement, specific=finitestatemachines_Transition2)
gen_finitestatemachines_Pseudostate_State2 = Generalization(general=State2, specific=finitestatemachines_Pseudostate)
gen_finitestatemachines_Fork_Pseudostate = Generalization(general=Pseudostate, specific=finitestatemachines_Fork)
gen_finitestatemachines_Join2_Pseudostate = Generalization(general=Pseudostate, specific=finitestatemachines_Join2)

# Domain Model
domain_model = DomainModel(
    name="finitestatemachines",
    types={finitestatemachines_StateMachine, NamedElement, finitestatemachines_NamedElement, finitestatemachines_FinalState, finitestatemachines_State2, finitestatemachines_Transition2, finitestatemachines_TimedTransition, Transition2, State2, finitestatemachines_InitialState, finitestatemachines_Trigger2, finitestatemachines_Pseudostate, finitestatemachines_Fork, Pseudostate, finitestatemachines_Join2},
    associations={states20, transitions22, outgoing5, incoming8, stateMachine211, target14, source17, trigger20, stateMachine21},
    generalizations={gen_finitestatemachines_StateMachine_NamedElement, gen_finitestatemachines_State2_NamedElement, gen_finitestatemachines_TimedTransition_Transition2, gen_finitestatemachines_FinalState_State2, gen_finitestatemachines_InitialState_State2, gen_finitestatemachines_Transition2_NamedElement, gen_finitestatemachines_Pseudostate_State2, gen_finitestatemachines_Fork_Pseudostate, gen_finitestatemachines_Join2_Pseudostate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)