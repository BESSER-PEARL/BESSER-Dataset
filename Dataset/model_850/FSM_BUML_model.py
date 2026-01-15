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
FSM_FSMModel = Class(name="FSM::FSMModel")
NamedElement = Class(name="NamedElement")
FSM_StateMachine = Class(name="FSM::StateMachine")
FSM_State = Class(name="FSM::State")
FSM_NamedElement = Class(name="FSM::NamedElement", is_abstract=True)
FSM_Transition = Class(name="FSM::Transition")

# FSM_FSMModel class attributes and methods

# NamedElement class attributes and methods

# FSM_StateMachine class attributes and methods

# FSM_State class attributes and methods
FSM_State_isFinal: Property = Property(name="isFinal", type=BooleanType)
FSM_State.attributes={FSM_State_isFinal}

# FSM_NamedElement class attributes and methods
FSM_NamedElement_name: Property = Property(name="name", type=StringType)
FSM_NamedElement.attributes={FSM_NamedElement_name}

# FSM_Transition class attributes and methods
FSM_Transition_input: Property = Property(name="input", type=StringType)
FSM_Transition_output: Property = Property(name="output", type=StringType)
FSM_Transition.attributes={FSM_Transition_input, FSM_Transition_output}

# Relationships
statemachines0: BinaryAssociation = BinaryAssociation(
    name="statemachines0",
    ends={
        Property(name="FSM_StateMachine", type=FSM_FSMModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_FSMModel", type=FSM_StateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial1: BinaryAssociation = BinaryAssociation(
    name="initial1",
    ends={
        Property(name="FSM_State", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_StateMachine2", type=FSM_State, multiplicity=Multiplicity(1, 1))
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="FSM_State5", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_StateMachine4", type=FSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions6: BinaryAssociation = BinaryAssociation(
    name="transitions6",
    ends={
        Property(name="Transition", type=FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=FSM_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="FSM_State8", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_Transition", type=FSM_State, multiplicity=Multiplicity(1, 1))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="State", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=FSM_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_FSM_FSMModel_NamedElement = Generalization(general=NamedElement, specific=FSM_FSMModel)
gen_FSM_StateMachine_NamedElement = Generalization(general=NamedElement, specific=FSM_StateMachine)
gen_FSM_State_NamedElement = Generalization(general=NamedElement, specific=FSM_State)

# Domain Model
domain_model = DomainModel(
    name="FSM",
    types={FSM_FSMModel, NamedElement, FSM_StateMachine, FSM_State, FSM_NamedElement, FSM_Transition},
    associations={statemachines0, initial1, states3, transitions6, target7, source9},
    generalizations={gen_FSM_FSMModel_NamedElement, gen_FSM_StateMachine_NamedElement, gen_FSM_State_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)