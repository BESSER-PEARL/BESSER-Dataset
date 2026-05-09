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
mydsl_FinalState = Class(name="mydsl_FinalState")
mydsl_FSM = Class(name="mydsl_FSM")
mydsl_State = Class(name="mydsl_State")
mydsl_Transition = Class(name="mydsl_Transition")
mydsl_IntitialState = Class(name="mydsl_IntitialState")
State = Class(name="State")

# mydsl_FinalState class attributes and methods

# mydsl_FSM class attributes and methods
mydsl_FSM_name: Property = Property(name="name", type=StringType)
mydsl_FSM.attributes={mydsl_FSM_name}

# mydsl_State class attributes and methods
mydsl_State_name: Property = Property(name="name", type=StringType)
mydsl_State.attributes={mydsl_State_name}

# mydsl_Transition class attributes and methods
mydsl_Transition_name: Property = Property(name="name", type=StringType)
mydsl_Transition.attributes={mydsl_Transition_name}

# mydsl_IntitialState class attributes and methods

# State class attributes and methods

# Relationships
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="mydsl_State5", type=mydsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_Transition4", type=mydsl_State, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="mydsl_State8", type=mydsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_Transition7", type=mydsl_State, multiplicity=Multiplicity(1, 1))
    }
)
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="mydsl_State", type=mydsl_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_FSM", type=mydsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="mydsl_Transition", type=mydsl_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_FSM2", type=mydsl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mydsl_FinalState_State = Generalization(general=State, specific=mydsl_FinalState)
gen_mydsl_IntitialState_State = Generalization(general=State, specific=mydsl_IntitialState)

# Domain Model
domain_model = DomainModel(
    name="mydsl",
    types={mydsl_FinalState, mydsl_FSM, mydsl_State, mydsl_Transition, mydsl_IntitialState, State},
    associations={source3, target6, state0, transition1},
    generalizations={gen_mydsl_FinalState_State, gen_mydsl_IntitialState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)