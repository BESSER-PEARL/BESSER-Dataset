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
complexStateMachineMetaModel_State = Class(name="complexStateMachineMetaModel::State")
complexStateMachineMetaModel_Transition = Class(name="complexStateMachineMetaModel::Transition")
complexStateMachineMetaModel_ComplexStateMachine = Class(name="complexStateMachineMetaModel::ComplexStateMachine")
complexStateMachineMetaModel_CompositeState = Class(name="complexStateMachineMetaModel::CompositeState")
State = Class(name="State")

# complexStateMachineMetaModel_State class attributes and methods
complexStateMachineMetaModel_State_Name: Property = Property(name="Name", type=StringType)
complexStateMachineMetaModel_State.attributes={complexStateMachineMetaModel_State_Name}

# complexStateMachineMetaModel_Transition class attributes and methods
complexStateMachineMetaModel_Transition_Name: Property = Property(name="Name", type=StringType)
complexStateMachineMetaModel_Transition.attributes={complexStateMachineMetaModel_Transition_Name}

# complexStateMachineMetaModel_ComplexStateMachine class attributes and methods
complexStateMachineMetaModel_ComplexStateMachine_Name: Property = Property(name="Name", type=StringType)
complexStateMachineMetaModel_ComplexStateMachine.attributes={complexStateMachineMetaModel_ComplexStateMachine_Name}

# complexStateMachineMetaModel_CompositeState class attributes and methods

# State class attributes and methods

# Relationships
States0: BinaryAssociation = BinaryAssociation(
    name="States0",
    ends={
        Property(name="State", type=complexStateMachineMetaModel_ComplexStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ComplexStateMachine", type=complexStateMachineMetaModel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transitions1: BinaryAssociation = BinaryAssociation(
    name="Transitions1",
    ends={
        Property(name="Transition", type=complexStateMachineMetaModel_ComplexStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ComplexStateMachine2", type=complexStateMachineMetaModel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialState3: BinaryAssociation = BinaryAssociation(
    name="InitialState3",
    ends={
        Property(name="complexStateMachineMetaModel_State", type=complexStateMachineMetaModel_ComplexStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="complexStateMachineMetaModel_ComplexStateMachine", type=complexStateMachineMetaModel_State, multiplicity=Multiplicity(0, 1))
    }
)
ComplexStateMachine4: BinaryAssociation = BinaryAssociation(
    name="ComplexStateMachine4",
    ends={
        Property(name="ComplexStateMachine5", type=complexStateMachineMetaModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Transitions", type=complexStateMachineMetaModel_ComplexStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
Source6: BinaryAssociation = BinaryAssociation(
    name="Source6",
    ends={
        Property(name="State7", type=complexStateMachineMetaModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Outgoing", type=complexStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1))
    }
)
Target8: BinaryAssociation = BinaryAssociation(
    name="Target8",
    ends={
        Property(name="State9", type=complexStateMachineMetaModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Incoming", type=complexStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1))
    }
)
ComplexStateMachine10: BinaryAssociation = BinaryAssociation(
    name="ComplexStateMachine10",
    ends={
        Property(name="ComplexStateMachine11", type=complexStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="States", type=complexStateMachineMetaModel_ComplexStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
Outgoing12: BinaryAssociation = BinaryAssociation(
    name="Outgoing12",
    ends={
        Property(name="Transition13", type=complexStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Source", type=complexStateMachineMetaModel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
Incoming14: BinaryAssociation = BinaryAssociation(
    name="Incoming14",
    ends={
        Property(name="Transition15", type=complexStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Target", type=complexStateMachineMetaModel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
CompositeState16: BinaryAssociation = BinaryAssociation(
    name="CompositeState16",
    ends={
        Property(name="CompositeState", type=complexStateMachineMetaModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="States17", type=complexStateMachineMetaModel_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
States18: BinaryAssociation = BinaryAssociation(
    name="States18",
    ends={
        Property(name="State20", type=complexStateMachineMetaModel_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeState19", type=complexStateMachineMetaModel_State, multiplicity=Multiplicity(0, 9999))
    }
)
InitialState21: BinaryAssociation = BinaryAssociation(
    name="InitialState21",
    ends={
        Property(name="complexStateMachineMetaModel_State22", type=complexStateMachineMetaModel_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="complexStateMachineMetaModel_CompositeState", type=complexStateMachineMetaModel_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_complexStateMachineMetaModel_CompositeState_State = Generalization(general=State, specific=complexStateMachineMetaModel_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="complexStateMachineMetaModel",
    types={complexStateMachineMetaModel_State, complexStateMachineMetaModel_Transition, complexStateMachineMetaModel_ComplexStateMachine, complexStateMachineMetaModel_CompositeState, State},
    associations={States0, Transitions1, InitialState3, ComplexStateMachine4, Source6, Target8, ComplexStateMachine10, Outgoing12, Incoming14, CompositeState16, States18, InitialState21},
    generalizations={gen_complexStateMachineMetaModel_CompositeState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)