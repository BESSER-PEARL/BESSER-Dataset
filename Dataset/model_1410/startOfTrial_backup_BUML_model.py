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
trialStatemachine_Region = Class(name="trialStatemachine_Region")
trialStatemachine_Statemachine = Class(name="trialStatemachine_Statemachine")
Region = Class(name="Region")
trialStatemachine_Action = Class(name="trialStatemachine_Action")
trialStatemachine_State = Class(name="trialStatemachine_State")
trialStatemachine_LabeledTransition = Class(name="trialStatemachine_LabeledTransition")
trialStatemachine_ComplexState = Class(name="trialStatemachine_ComplexState")
State = Class(name="State")

# trialStatemachine_Region class attributes and methods
trialStatemachine_Region_history: Property = Property(name="history", type=StringType)
trialStatemachine_Region.attributes={trialStatemachine_Region_history}

# trialStatemachine_Statemachine class attributes and methods
trialStatemachine_Statemachine_name: Property = Property(name="name", type=StringType)
trialStatemachine_Statemachine.attributes={trialStatemachine_Statemachine_name}

# Region class attributes and methods

# trialStatemachine_Action class attributes and methods
trialStatemachine_Action_name: Property = Property(name="name", type=StringType)
trialStatemachine_Action.attributes={trialStatemachine_Action_name}

# trialStatemachine_State class attributes and methods
trialStatemachine_State_name: Property = Property(name="name", type=StringType)
trialStatemachine_State.attributes={trialStatemachine_State_name}

# trialStatemachine_LabeledTransition class attributes and methods
trialStatemachine_LabeledTransition_id: Property = Property(name="id", type=StringType)
trialStatemachine_LabeledTransition.attributes={trialStatemachine_LabeledTransition_id}

# trialStatemachine_ComplexState class attributes and methods

# State class attributes and methods

# Relationships
region1: BinaryAssociation = BinaryAssociation(
    name="region1",
    ends={
        Property(name="trialStatemachine_Region", type=trialStatemachine_ComplexState, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_ComplexState", type=trialStatemachine_Region, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions2: BinaryAssociation = BinaryAssociation(
    name="actions2",
    ends={
        Property(name="trialStatemachine_Action", type=trialStatemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_Statemachine", type=trialStatemachine_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultHistory3: BinaryAssociation = BinaryAssociation(
    name="defaultHistory3",
    ends={
        Property(name="trialStatemachine_State5", type=trialStatemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_Region4", type=trialStatemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
states6: BinaryAssociation = BinaryAssociation(
    name="states6",
    ends={
        Property(name="trialStatemachine_State8", type=trialStatemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_Region7", type=trialStatemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial9: BinaryAssociation = BinaryAssociation(
    name="initial9",
    ends={
        Property(name="trialStatemachine_State11", type=trialStatemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_Region10", type=trialStatemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="trialStatemachine_State14", type=trialStatemachine_LabeledTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_LabeledTransition13", type=trialStatemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
action15: BinaryAssociation = BinaryAssociation(
    name="action15",
    ends={
        Property(name="trialStatemachine_Action17", type=trialStatemachine_LabeledTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_LabeledTransition16", type=trialStatemachine_Action, multiplicity=Multiplicity(1, 1))
    }
)
outgoings0: BinaryAssociation = BinaryAssociation(
    name="outgoings0",
    ends={
        Property(name="trialStatemachine_LabeledTransition", type=trialStatemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_State", type=trialStatemachine_LabeledTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_trialStatemachine_Statemachine_Region = Generalization(general=Region, specific=trialStatemachine_Statemachine)
gen_trialStatemachine_ComplexState_State = Generalization(general=State, specific=trialStatemachine_ComplexState)

# Domain Model
domain_model = DomainModel(
    name="trialStatemachine",
    types={trialStatemachine_Region, trialStatemachine_Statemachine, Region, trialStatemachine_Action, trialStatemachine_State, trialStatemachine_LabeledTransition, trialStatemachine_ComplexState, State},
    associations={region1, actions2, defaultHistory3, states6, initial9, target12, action15, outgoings0},
    generalizations={gen_trialStatemachine_Statemachine_Region, gen_trialStatemachine_ComplexState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)