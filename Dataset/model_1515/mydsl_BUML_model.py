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
mydsl_FSM = Class(name="mydsl::FSM")
mydsl_State = Class(name="mydsl::State")
mydsl_Transition = Class(name="mydsl::Transition")
mydsl_Final = Class(name="mydsl::Final")
mydsl_Initial = Class(name="mydsl::Initial")
State = Class(name="State")

# mydsl_FSM class attributes and methods
mydsl_FSM_name: Property = Property(name="name", type=StringType)
mydsl_FSM.attributes={mydsl_FSM_name}

# mydsl_State class attributes and methods
mydsl_State_name: Property = Property(name="name", type=StringType)
mydsl_State.attributes={mydsl_State_name}

# mydsl_Transition class attributes and methods
mydsl_Transition_name: Property = Property(name="name", type=StringType)
mydsl_Transition_trigger: Property = Property(name="trigger", type=StringType)
mydsl_Transition.attributes={mydsl_Transition_name, mydsl_Transition_trigger}

# mydsl_Final class attributes and methods

# mydsl_Initial class attributes and methods

# State class attributes and methods

# Relationships
state7: BinaryAssociation = BinaryAssociation(
    name="state7",
    ends={
        Property(name="mydsl_State9", type=mydsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_Transition8", type=mydsl_State, multiplicity=Multiplicity(2, 2))
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
final3: BinaryAssociation = BinaryAssociation(
    name="final3",
    ends={
        Property(name="mydsl_Final", type=mydsl_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_FSM4", type=mydsl_Final, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initial5: BinaryAssociation = BinaryAssociation(
    name="initial5",
    ends={
        Property(name="mydsl_Initial", type=mydsl_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_FSM6", type=mydsl_Initial, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_mydsl_Initial_State = Generalization(general=State, specific=mydsl_Initial)
gen_mydsl_Final_State = Generalization(general=State, specific=mydsl_Final)

# Domain Model
domain_model = DomainModel(
    name="mydsl",
    types={mydsl_FSM, mydsl_State, mydsl_Transition, mydsl_Final, mydsl_Initial, State},
    associations={state7, state0, transition1, final3, initial5},
    generalizations={gen_mydsl_Initial_State, gen_mydsl_Final_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)