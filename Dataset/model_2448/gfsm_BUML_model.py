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
gfsm_Guard = Class(name="gfsm::Guard")
gfsm_Transition = Class(name="gfsm::Transition")
gfsm_State = Class(name="gfsm::State")
gfsm_Machine = Class(name="gfsm::Machine")

# gfsm_Guard class attributes and methods
gfsm_Guard_value: Property = Property(name="value", type=StringType)
gfsm_Guard.attributes={gfsm_Guard_value}

# gfsm_Transition class attributes and methods
gfsm_Transition_event: Property = Property(name="event", type=StringType)
gfsm_Transition.attributes={gfsm_Transition_event}

# gfsm_State class attributes and methods
gfsm_State_name: Property = Property(name="name", type=StringType)
gfsm_State.attributes={gfsm_State_name}

# gfsm_Machine class attributes and methods

# Relationships
from0: BinaryAssociation = BinaryAssociation(
    name="from0",
    ends={
        Property(name="State", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=gfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
to1: BinaryAssociation = BinaryAssociation(
    name="to1",
    ends={
        Property(name="State2", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incommings", type=gfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
guard3: BinaryAssociation = BinaryAssociation(
    name="guard3",
    ends={
        Property(name="gfsm_Guard", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_Transition", type=gfsm_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
states7: BinaryAssociation = BinaryAssociation(
    name="states7",
    ends={
        Property(name="gfsm_State", type=gfsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_Machine", type=gfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoings4: BinaryAssociation = BinaryAssociation(
    name="outgoings4",
    ends={
        Property(name="Transition", type=gfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=gfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incommings5: BinaryAssociation = BinaryAssociation(
    name="incommings5",
    ends={
        Property(name="Transition6", type=gfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=gfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
transitions8: BinaryAssociation = BinaryAssociation(
    name="transitions8",
    ends={
        Property(name="gfsm_Transition10", type=gfsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_Machine9", type=gfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState11: BinaryAssociation = BinaryAssociation(
    name="initialState11",
    ends={
        Property(name="gfsm_State13", type=gfsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_Machine12", type=gfsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="gfsm",
    types={gfsm_Guard, gfsm_Transition, gfsm_State, gfsm_Machine},
    associations={from0, to1, guard3, states7, outgoings4, incommings5, transitions8, initialState11},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)