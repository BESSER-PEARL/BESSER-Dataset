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
zhu_StateMachine = Class(name="zhu::StateMachine")
zhu_TopRegion = Class(name="zhu::TopRegion")
zhu_States = Class(name="zhu::States")
zhu_Region = Class(name="zhu::Region")
zhu_Transitions = Class(name="zhu::Transitions")
zhu_Transition = Class(name="zhu::Transition")
zhu_State = Class(name="zhu::State")
zhu_Triggers = Class(name="zhu::Triggers")
zhu_StatesSeparated = Class(name="zhu::StatesSeparated")
zhu_TriggersSeparated = Class(name="zhu::TriggersSeparated")

# zhu_StateMachine class attributes and methods

# zhu_TopRegion class attributes and methods

# zhu_States class attributes and methods

# zhu_Region class attributes and methods
zhu_Region_name: Property = Property(name="name", type=StringType)
zhu_Region.attributes={zhu_Region_name}

# zhu_Transitions class attributes and methods

# zhu_Transition class attributes and methods
zhu_Transition_guard: Property = Property(name="guard", type=StringType)
zhu_Transition_behaviour: Property = Property(name="behaviour", type=StringType)
zhu_Transition.attributes={zhu_Transition_behaviour, zhu_Transition_guard}

# zhu_State class attributes and methods
zhu_State_name: Property = Property(name="name", type=StringType)
zhu_State.attributes={zhu_State_name}

# zhu_Triggers class attributes and methods

# zhu_StatesSeparated class attributes and methods

# zhu_TriggersSeparated class attributes and methods
zhu_TriggersSeparated_firstTrigger: Property = Property(name="firstTrigger", type=StringType)
zhu_TriggersSeparated_followingTriggers: Property = Property(name="followingTriggers", type=StringType)
zhu_TriggersSeparated.attributes={zhu_TriggersSeparated_firstTrigger, zhu_TriggersSeparated_followingTriggers}

# Relationships
states7: BinaryAssociation = BinaryAssociation(
    name="states7",
    ends={
        Property(name="zhu_States9", type=zhu_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_Region8", type=zhu_States, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
regions11: BinaryAssociation = BinaryAssociation(
    name="regions11",
    ends={
        Property(name="zhu_Region12", type=zhu_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_Region10", type=zhu_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions13: BinaryAssociation = BinaryAssociation(
    name="transitions13",
    ends={
        Property(name="zhu_Transitions15", type=zhu_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_Region14", type=zhu_Transitions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
region0: BinaryAssociation = BinaryAssociation(
    name="region0",
    ends={
        Property(name="zhu_TopRegion", type=zhu_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_StateMachine", type=zhu_TopRegion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="zhu_States", type=zhu_TopRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_TopRegion2", type=zhu_States, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
regions3: BinaryAssociation = BinaryAssociation(
    name="regions3",
    ends={
        Property(name="zhu_Region", type=zhu_TopRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_TopRegion4", type=zhu_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="zhu_Transitions", type=zhu_TopRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_TopRegion6", type=zhu_Transitions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states28: BinaryAssociation = BinaryAssociation(
    name="states28",
    ends={
        Property(name="zhu_StatesSeparated", type=zhu_States, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_States29", type=zhu_StatesSeparated, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstState30: BinaryAssociation = BinaryAssociation(
    name="firstState30",
    ends={
        Property(name="zhu_State32", type=zhu_StatesSeparated, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_StatesSeparated31", type=zhu_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
followingStates33: BinaryAssociation = BinaryAssociation(
    name="followingStates33",
    ends={
        Property(name="zhu_State35", type=zhu_StatesSeparated, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_StatesSeparated34", type=zhu_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstTransition16: BinaryAssociation = BinaryAssociation(
    name="firstTransition16",
    ends={
        Property(name="zhu_Transition", type=zhu_Transitions, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_Transitions17", type=zhu_Transition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
followingTransitions18: BinaryAssociation = BinaryAssociation(
    name="followingTransitions18",
    ends={
        Property(name="zhu_Transition20", type=zhu_Transitions, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_Transitions19", type=zhu_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="zhu_State", type=zhu_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_Transition22", type=zhu_State, multiplicity=Multiplicity(0, 1))
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="zhu_State25", type=zhu_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_Transition24", type=zhu_State, multiplicity=Multiplicity(0, 1))
    }
)
triggers26: BinaryAssociation = BinaryAssociation(
    name="triggers26",
    ends={
        Property(name="zhu_Triggers", type=zhu_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_Transition27", type=zhu_Triggers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggers36: BinaryAssociation = BinaryAssociation(
    name="triggers36",
    ends={
        Property(name="zhu_TriggersSeparated", type=zhu_Triggers, multiplicity=Multiplicity(1, 1)),
        Property(name="zhu_Triggers37", type=zhu_TriggersSeparated, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="zhu",
    types={zhu_StateMachine, zhu_TopRegion, zhu_States, zhu_Region, zhu_Transitions, zhu_Transition, zhu_State, zhu_Triggers, zhu_StatesSeparated, zhu_TriggersSeparated},
    associations={states7, regions11, transitions13, region0, states1, regions3, transitions5, states28, firstState30, followingStates33, firstTransition16, followingTransitions18, source21, target23, triggers26, triggers36},
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