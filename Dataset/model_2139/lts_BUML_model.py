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
lts_IntermediateState = Class(name="lts::IntermediateState")
lts_FinalState = Class(name="lts::FinalState")
lts_State = Class(name="lts::State")
State = Class(name="State")
lts_LTS = Class(name="lts::LTS")
lts_Transition = Class(name="lts::Transition")
lts_InitialState = Class(name="lts::InitialState")

# lts_IntermediateState class attributes and methods

# lts_FinalState class attributes and methods

# lts_State class attributes and methods
lts_State_Id: Property = Property(name="Id", type=StringType)
lts_State.attributes={lts_State_Id}

# State class attributes and methods

# lts_LTS class attributes and methods
lts_LTS_name: Property = Property(name="name", type=StringType)
lts_LTS.attributes={lts_LTS_name}

# lts_Transition class attributes and methods
lts_Transition_label: Property = Property(name="label", type=StringType)
lts_Transition.attributes={lts_Transition_label}

# lts_InitialState class attributes and methods

# Relationships
intermediateStates3: BinaryAssociation = BinaryAssociation(
    name="intermediateStates3",
    ends={
        Property(name="lts_IntermediateState", type=lts_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_LTS4", type=lts_IntermediateState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalState5: BinaryAssociation = BinaryAssociation(
    name="finalState5",
    ends={
        Property(name="lts_FinalState", type=lts_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_LTS6", type=lts_FinalState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="State", type=lts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=lts_State, multiplicity=Multiplicity(0, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="State9", type=lts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=lts_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming10: BinaryAssociation = BinaryAssociation(
    name="incoming10",
    ends={
        Property(name="Transition", type=lts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=lts_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing11: BinaryAssociation = BinaryAssociation(
    name="outgoing11",
    ends={
        Property(name="Transition12", type=lts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=lts_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="lts_Transition", type=lts_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_LTS", type=lts_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="lts_InitialState", type=lts_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_LTS2", type=lts_InitialState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_lts_InitialState_State = Generalization(general=State, specific=lts_InitialState)
gen_lts_FinalState_State = Generalization(general=State, specific=lts_FinalState)
gen_lts_IntermediateState_State = Generalization(general=State, specific=lts_IntermediateState)

# Domain Model
domain_model = DomainModel(
    name="lts",
    types={lts_IntermediateState, lts_FinalState, lts_State, State, lts_LTS, lts_Transition, lts_InitialState},
    associations={intermediateStates3, finalState5, target7, source8, incoming10, outgoing11, transitions0, initialState1},
    generalizations={gen_lts_InitialState_State, gen_lts_FinalState_State, gen_lts_IntermediateState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)