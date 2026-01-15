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
nicoLang_FSM = Class(name="nicoLang::FSM")
nicoLang_Transition = Class(name="nicoLang::Transition")
nicoLang_State = Class(name="nicoLang::State")
nicoLang_InitState = Class(name="nicoLang::InitState")
State = Class(name="State")
nicoLang_FinalState = Class(name="nicoLang::FinalState")

# nicoLang_FSM class attributes and methods
nicoLang_FSM_name: Property = Property(name="name", type=StringType)
nicoLang_FSM.attributes={nicoLang_FSM_name}

# nicoLang_Transition class attributes and methods
nicoLang_Transition_name: Property = Property(name="name", type=StringType)
nicoLang_Transition_trigger: Property = Property(name="trigger", type=StringType)
nicoLang_Transition.attributes={nicoLang_Transition_name, nicoLang_Transition_trigger}

# nicoLang_State class attributes and methods
nicoLang_State_name: Property = Property(name="name", type=StringType)
nicoLang_State.attributes={nicoLang_State_name}

# nicoLang_InitState class attributes and methods

# State class attributes and methods

# nicoLang_FinalState class attributes and methods

# Relationships
transition0: BinaryAssociation = BinaryAssociation(
    name="transition0",
    ends={
        Property(name="nicoLang_Transition", type=nicoLang_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="nicoLang_FSM", type=nicoLang_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state1: BinaryAssociation = BinaryAssociation(
    name="state1",
    ends={
        Property(name="nicoLang_State", type=nicoLang_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="nicoLang_FSM2", type=nicoLang_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="nicoLang_State5", type=nicoLang_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="nicoLang_Transition4", type=nicoLang_State, multiplicity=Multiplicity(1, 1))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="nicoLang_State8", type=nicoLang_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="nicoLang_Transition7", type=nicoLang_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_nicoLang_InitState_State = Generalization(general=State, specific=nicoLang_InitState)
gen_nicoLang_FinalState_State = Generalization(general=State, specific=nicoLang_FinalState)

# Domain Model
domain_model = DomainModel(
    name="nicoLang",
    types={nicoLang_FSM, nicoLang_Transition, nicoLang_State, nicoLang_InitState, State, nicoLang_FinalState},
    associations={transition0, state1, target3, source6},
    generalizations={gen_nicoLang_InitState_State, gen_nicoLang_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)