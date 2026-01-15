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
metaModelSM_State = Class(name="metaModelSM::State")
metaModelSM_Triggers = Class(name="metaModelSM::Triggers")
metaModelSM_InitialState = Class(name="metaModelSM::InitialState")
State = Class(name="State")
metaModelSM_FinalState = Class(name="metaModelSM::FinalState")
metaModelSM_Transition = Class(name="metaModelSM::Transition")
metaModelSM_NewEClass1 = Class(name="metaModelSM::NewEClass1")
metaModelSM_NewEClass2 = Class(name="metaModelSM::NewEClass2")
metaModelSM_StateMachine = Class(name="metaModelSM::StateMachine")
metaModelSM_Region = Class(name="metaModelSM::Region")
metaModelSM_Guard = Class(name="metaModelSM::Guard")
metaModelSM_Signal = Class(name="metaModelSM::Signal")

# metaModelSM_State class attributes and methods

# metaModelSM_Triggers class attributes and methods

# metaModelSM_InitialState class attributes and methods

# State class attributes and methods

# metaModelSM_FinalState class attributes and methods

# metaModelSM_Transition class attributes and methods

# metaModelSM_NewEClass1 class attributes and methods

# metaModelSM_NewEClass2 class attributes and methods

# metaModelSM_StateMachine class attributes and methods

# metaModelSM_Region class attributes and methods

# metaModelSM_Guard class attributes and methods

# metaModelSM_Signal class attributes and methods

# Relationships
source2: BinaryAssociation = BinaryAssociation(
    name="source2",
    ends={
        Property(name="metaModelSM_Triggers", type=metaModelSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelSM_State", type=metaModelSM_Triggers, multiplicity=Multiplicity(0, 1))
    }
)
region3: BinaryAssociation = BinaryAssociation(
    name="region3",
    ends={
        Property(name="metaModelSM_Region5", type=metaModelSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelSM_State4", type=metaModelSM_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition6: BinaryAssociation = BinaryAssociation(
    name="transition6",
    ends={
        Property(name="metaModelSM_Transition", type=metaModelSM_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelSM_Region7", type=metaModelSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggered8: BinaryAssociation = BinaryAssociation(
    name="triggered8",
    ends={
        Property(name="metaModelSM_Triggers10", type=metaModelSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelSM_Transition9", type=metaModelSM_Triggers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
neweclass20: BinaryAssociation = BinaryAssociation(
    name="neweclass20",
    ends={
        Property(name="metaModelSM_NewEClass2", type=metaModelSM_NewEClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelSM_NewEClass1", type=metaModelSM_NewEClass2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region1: BinaryAssociation = BinaryAssociation(
    name="region1",
    ends={
        Property(name="metaModelSM_Region", type=metaModelSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelSM_StateMachine", type=metaModelSM_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defines11: BinaryAssociation = BinaryAssociation(
    name="defines11",
    ends={
        Property(name="metaModelSM_Guard", type=metaModelSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelSM_Transition12", type=metaModelSM_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="metaModelSM_State15", type=metaModelSM_Triggers, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelSM_Triggers14", type=metaModelSM_State, multiplicity=Multiplicity(0, 1))
    }
)
signal16: BinaryAssociation = BinaryAssociation(
    name="signal16",
    ends={
        Property(name="metaModelSM_Signal", type=metaModelSM_Triggers, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelSM_Triggers17", type=metaModelSM_Signal, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_metaModelSM_InitialState_State = Generalization(general=State, specific=metaModelSM_InitialState)
gen_metaModelSM_FinalState_State = Generalization(general=State, specific=metaModelSM_FinalState)

# Domain Model
domain_model = DomainModel(
    name="metaModelSM",
    types={metaModelSM_State, metaModelSM_Triggers, metaModelSM_InitialState, State, metaModelSM_FinalState, metaModelSM_Transition, metaModelSM_NewEClass1, metaModelSM_NewEClass2, metaModelSM_StateMachine, metaModelSM_Region, metaModelSM_Guard, metaModelSM_Signal},
    associations={source2, region3, transition6, triggered8, neweclass20, region1, defines11, target13, signal16},
    generalizations={gen_metaModelSM_InitialState_State, gen_metaModelSM_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)