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
finitestatemachines_FinalState = Class(name="finitestatemachines_FinalState")
State2 = Class(name="State2")
finitestatemachines_InitialState = Class(name="finitestatemachines_InitialState")
finitestatemachines_Trigger2 = Class(name="finitestatemachines_Trigger2")
finitestatemachines_NamedElement = Class(name="finitestatemachines_NamedElement")
finitestatemachines_StateMachine = Class(name="finitestatemachines_StateMachine")
NamedElement = Class(name="NamedElement")
finitestatemachines_State2 = Class(name="finitestatemachines_State2")
finitestatemachines_Transition2 = Class(name="finitestatemachines_Transition2")
finitestatemachines_TimedTransition = Class(name="finitestatemachines_TimedTransition")
Transition2 = Class(name="Transition2")
finitestatemachines_Pseudostate = Class(name="finitestatemachines_Pseudostate")
finitestatemachines_Fork = Class(name="finitestatemachines_Fork")
Pseudostate = Class(name="Pseudostate")
finitestatemachines_Join2 = Class(name="finitestatemachines_Join2")

# finitestatemachines_FinalState class attributes and methods

# State2 class attributes and methods

# finitestatemachines_InitialState class attributes and methods

# finitestatemachines_Trigger2 class attributes and methods
finitestatemachines_Trigger2_expression: Property = Property(name="expression", type=StringType)
finitestatemachines_Trigger2.attributes={finitestatemachines_Trigger2_expression}

# finitestatemachines_NamedElement class attributes and methods
finitestatemachines_NamedElement_name: Property = Property(name="name", type=StringType)
finitestatemachines_NamedElement.attributes={finitestatemachines_NamedElement_name}

# finitestatemachines_StateMachine class attributes and methods

# NamedElement class attributes and methods

# finitestatemachines_State2 class attributes and methods
finitestatemachines_State2_initialTime2: Property = Property(name="initialTime2", type=IntegerType)
finitestatemachines_State2_finalTime: Property = Property(name="finalTime", type=IntegerType)
finitestatemachines_State2.attributes={finitestatemachines_State2_initialTime2, finitestatemachines_State2_finalTime}

# finitestatemachines_Transition2 class attributes and methods
finitestatemachines_Transition2_initialTime: Property = Property(name="initialTime", type=IntegerType)
finitestatemachines_Transition2_finalTime2: Property = Property(name="finalTime2", type=IntegerType)
finitestatemachines_Transition2.attributes={finitestatemachines_Transition2_finalTime2, finitestatemachines_Transition2_initialTime}

# finitestatemachines_TimedTransition class attributes and methods
finitestatemachines_TimedTransition_duration: Property = Property(name="duration", type=IntegerType)
finitestatemachines_TimedTransition.attributes={finitestatemachines_TimedTransition_duration}

# Transition2 class attributes and methods

# finitestatemachines_Pseudostate class attributes and methods

# finitestatemachines_Fork class attributes and methods

# Pseudostate class attributes and methods

# finitestatemachines_Join2 class attributes and methods

# Relationships
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="State28", type=finitestatemachines_Transition2, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=finitestatemachines_State2, multiplicity=Multiplicity(1, 1))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="State210", type=finitestatemachines_Transition2, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=finitestatemachines_State2, multiplicity=Multiplicity(1, 1))
    }
)
trigger11: BinaryAssociation = BinaryAssociation(
    name="trigger11",
    ends={
        Property(name="finitestatemachines_Trigger2", type=finitestatemachines_Transition2, multiplicity=Multiplicity(1, 1)),
        Property(name="finitestatemachines_Transition2", type=finitestatemachines_Trigger2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateMachine12: BinaryAssociation = BinaryAssociation(
    name="stateMachine12",
    ends={
        Property(name="StateMachine13", type=finitestatemachines_Transition2, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions2", type=finitestatemachines_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
states20: BinaryAssociation = BinaryAssociation(
    name="states20",
    ends={
        Property(name="State2", type=finitestatemachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine2", type=finitestatemachines_State2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions21: BinaryAssociation = BinaryAssociation(
    name="transitions21",
    ends={
        Property(name="Transition2", type=finitestatemachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=finitestatemachines_Transition2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing2: BinaryAssociation = BinaryAssociation(
    name="outgoing2",
    ends={
        Property(name="Transition23", type=finitestatemachines_State2, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=finitestatemachines_Transition2, multiplicity=Multiplicity(0, 9999))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition25", type=finitestatemachines_State2, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=finitestatemachines_Transition2, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachine26: BinaryAssociation = BinaryAssociation(
    name="stateMachine26",
    ends={
        Property(name="StateMachine", type=finitestatemachines_State2, multiplicity=Multiplicity(1, 1)),
        Property(name="states2", type=finitestatemachines_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_finitestatemachines_FinalState_State2 = Generalization(general=State2, specific=finitestatemachines_FinalState)
gen_finitestatemachines_InitialState_State2 = Generalization(general=State2, specific=finitestatemachines_InitialState)
gen_finitestatemachines_Transition2_NamedElement = Generalization(general=NamedElement, specific=finitestatemachines_Transition2)
gen_finitestatemachines_StateMachine_NamedElement = Generalization(general=NamedElement, specific=finitestatemachines_StateMachine)
gen_finitestatemachines_State2_NamedElement = Generalization(general=NamedElement, specific=finitestatemachines_State2)
gen_finitestatemachines_TimedTransition_Transition2 = Generalization(general=Transition2, specific=finitestatemachines_TimedTransition)
gen_finitestatemachines_Pseudostate_State2 = Generalization(general=State2, specific=finitestatemachines_Pseudostate)
gen_finitestatemachines_Fork_Pseudostate = Generalization(general=Pseudostate, specific=finitestatemachines_Fork)
gen_finitestatemachines_Join2_Pseudostate = Generalization(general=Pseudostate, specific=finitestatemachines_Join2)

# Domain Model
domain_model = DomainModel(
    name="finitestatemachines",
    types={finitestatemachines_FinalState, State2, finitestatemachines_InitialState, finitestatemachines_Trigger2, finitestatemachines_NamedElement, finitestatemachines_StateMachine, NamedElement, finitestatemachines_State2, finitestatemachines_Transition2, finitestatemachines_TimedTransition, Transition2, finitestatemachines_Pseudostate, finitestatemachines_Fork, Pseudostate, finitestatemachines_Join2},
    associations={target7, source9, trigger11, stateMachine12, states20, transitions21, outgoing2, incoming4, stateMachine26},
    generalizations={gen_finitestatemachines_FinalState_State2, gen_finitestatemachines_InitialState_State2, gen_finitestatemachines_Transition2_NamedElement, gen_finitestatemachines_StateMachine_NamedElement, gen_finitestatemachines_State2_NamedElement, gen_finitestatemachines_TimedTransition_Transition2, gen_finitestatemachines_Pseudostate_State2, gen_finitestatemachines_Fork_Pseudostate, gen_finitestatemachines_Join2_Pseudostate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)