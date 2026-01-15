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
simpleStateMachineMetaModel_SimpleStateMachine = Class(name="simpleStateMachineMetaModel::SimpleStateMachine")
simpleStateMachineMetaModel_State = Class(name="simpleStateMachineMetaModel::State")
simpleStateMachineMetaModel_Transition = Class(name="simpleStateMachineMetaModel::Transition")

# simpleStateMachineMetaModel_SimpleStateMachine class attributes and methods
simpleStateMachineMetaModel_SimpleStateMachine_Name: Property = Property(name="Name", type=StringType)
simpleStateMachineMetaModel_SimpleStateMachine.attributes={simpleStateMachineMetaModel_SimpleStateMachine_Name}

# simpleStateMachineMetaModel_State class attributes and methods
simpleStateMachineMetaModel_State_Name: Property = Property(name="Name", type=StringType)
simpleStateMachineMetaModel_State.attributes={simpleStateMachineMetaModel_State_Name}

# simpleStateMachineMetaModel_Transition class attributes and methods
simpleStateMachineMetaModel_Transition_Name: Property = Property(name="Name", type=StringType)
simpleStateMachineMetaModel_Transition.attributes={simpleStateMachineMetaModel_Transition_Name}

# Relationships
States0: BinaryAssociation = BinaryAssociation(
    name="States0",
    ends={
        Property(name="State", type=simpleStateMachineMetaModel_SimpleStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleStateMachine", type=simpleStateMachineMetaModel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transitions1: BinaryAssociation = BinaryAssociation(
    name="Transitions1",
    ends={
        Property(name="Transition", type=simpleStateMachineMetaModel_SimpleStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleStateMachine2", type=simpleStateMachineMetaModel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Source6: BinaryAssociation = BinaryAssociation(
    name="Source6",
    ends={
        Property(name="State7", type=simpleStateMachineMetaModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Outgoing", type=simpleStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1))
    }
)
Target8: BinaryAssociation = BinaryAssociation(
    name="Target8",
    ends={
        Property(name="State9", type=simpleStateMachineMetaModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Incoming", type=simpleStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1))
    }
)
SimpleStateMachine10: BinaryAssociation = BinaryAssociation(
    name="SimpleStateMachine10",
    ends={
        Property(name="SimpleStateMachine11", type=simpleStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="States", type=simpleStateMachineMetaModel_SimpleStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
Outgoing12: BinaryAssociation = BinaryAssociation(
    name="Outgoing12",
    ends={
        Property(name="Transition13", type=simpleStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Source", type=simpleStateMachineMetaModel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
Incoming14: BinaryAssociation = BinaryAssociation(
    name="Incoming14",
    ends={
        Property(name="Transition15", type=simpleStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Target", type=simpleStateMachineMetaModel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
InitialState3: BinaryAssociation = BinaryAssociation(
    name="InitialState3",
    ends={
        Property(name="simpleStateMachineMetaModel_State", type=simpleStateMachineMetaModel_SimpleStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleStateMachineMetaModel_SimpleStateMachine", type=simpleStateMachineMetaModel_State, multiplicity=Multiplicity(0, 1))
    }
)
SimpleStateMachine4: BinaryAssociation = BinaryAssociation(
    name="SimpleStateMachine4",
    ends={
        Property(name="SimpleStateMachine5", type=simpleStateMachineMetaModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Transitions", type=simpleStateMachineMetaModel_SimpleStateMachine, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="simpleStateMachineMetaModel",
    types={simpleStateMachineMetaModel_SimpleStateMachine, simpleStateMachineMetaModel_State, simpleStateMachineMetaModel_Transition},
    associations={States0, Transitions1, Source6, Target8, SimpleStateMachine10, Outgoing12, Incoming14, InitialState3, SimpleStateMachine4},
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