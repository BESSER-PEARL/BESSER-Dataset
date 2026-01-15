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
FSM_FStateMachine = Class(name="FSM::FStateMachine")
FSM_FTransition = Class(name="FSM::FTransition")
FSM_FAbstractState = Class(name="FSM::FAbstractState", is_abstract=True)
FSM_FInitialState = Class(name="FSM::FInitialState")
FAbstractState = Class(name="FAbstractState")
FSM_FRegularState = Class(name="FSM::FRegularState")

# FSM_FStateMachine class attributes and methods
FSM_FStateMachine_name: Property = Property(name="name", type=StringType)
FSM_FStateMachine.attributes={FSM_FStateMachine_name}

# FSM_FTransition class attributes and methods
FSM_FTransition_label: Property = Property(name="label", type=StringType)
FSM_FTransition.attributes={FSM_FTransition_label}

# FSM_FAbstractState class attributes and methods
FSM_FAbstractState_name: Property = Property(name="name", type=StringType)
FSM_FAbstractState.attributes={FSM_FAbstractState_name}

# FSM_FInitialState class attributes and methods

# FAbstractState class attributes and methods

# FSM_FRegularState class attributes and methods

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="FTransition", type=FSM_FStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=FSM_FTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="FAbstractState", type=FSM_FStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine2", type=FSM_FAbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine3: BinaryAssociation = BinaryAssociation(
    name="stateMachine3",
    ends={
        Property(name="FStateMachine", type=FSM_FTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=FSM_FStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="FSM_FAbstractState", type=FSM_FTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_FTransition", type=FSM_FAbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="FSM_FAbstractState7", type=FSM_FTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_FTransition6", type=FSM_FAbstractState, multiplicity=Multiplicity(1, 1))
    }
)
stateMachine8: BinaryAssociation = BinaryAssociation(
    name="stateMachine8",
    ends={
        Property(name="FStateMachine9", type=FSM_FAbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=FSM_FStateMachine, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_FSM_FInitialState_FAbstractState = Generalization(general=FAbstractState, specific=FSM_FInitialState)
gen_FSM_FRegularState_FAbstractState = Generalization(general=FAbstractState, specific=FSM_FRegularState)

# Domain Model
domain_model = DomainModel(
    name="FSM",
    types={FSM_FStateMachine, FSM_FTransition, FSM_FAbstractState, FSM_FInitialState, FAbstractState, FSM_FRegularState},
    associations={transitions0, states1, stateMachine3, source4, target5, stateMachine8},
    generalizations={gen_FSM_FInitialState_FAbstractState, gen_FSM_FRegularState_FAbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)