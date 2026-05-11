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
lts_InitialState = Class(name="lts_InitialState")
lts_IntermediateState = Class(name="lts_IntermediateState")
lts_FinalState = Class(name="lts_FinalState")
lts_State = Class(name="lts_State")
lts_LTS = Class(name="lts_LTS")
lts_Transition = Class(name="lts_Transition")
State = Class(name="State")

# lts_InitialState class attributes and methods

# lts_IntermediateState class attributes and methods

# lts_FinalState class attributes and methods

# lts_State class attributes and methods
lts_State_Id: Property = Property(name="Id", type=StringType)
lts_State.attributes={lts_State_Id}

# lts_LTS class attributes and methods
lts_LTS_name: Property = Property(name="name", type=StringType)
lts_LTS.attributes={lts_LTS_name}

# lts_Transition class attributes and methods
lts_Transition_label: Property = Property(name="label", type=StringType)
lts_Transition.attributes={lts_Transition_label}

# State class attributes and methods

# Relationships
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
outgoing11: BinaryAssociation = BinaryAssociation(
    name="outgoing11",
    ends={
        Property(name="Transition12", type=lts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=lts_Transition, multiplicity=Multiplicity(0, 9999))
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

# Generalizations
gen_lts_InitialState_State = Generalization(general=State, specific=lts_InitialState)
gen_lts_FinalState_State = Generalization(general=State, specific=lts_FinalState)
gen_lts_IntermediateState_State = Generalization(general=State, specific=lts_IntermediateState)

# Domain Model
domain_model = DomainModel(
    name="lts",
    types={lts_InitialState, lts_IntermediateState, lts_FinalState, lts_State, lts_LTS, lts_Transition, State},
    associations={transitions0, initialState1, intermediateStates3, finalState5, target7, outgoing11, source8, incoming10},
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