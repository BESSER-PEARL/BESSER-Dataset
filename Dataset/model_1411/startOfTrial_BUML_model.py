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
trialStatemachine_State = Class(name="trialStatemachine::State")
trialStatemachine_LabeledTransition = Class(name="trialStatemachine::LabeledTransition")
trialStatemachine_Action = Class(name="trialStatemachine::Action")
trialStatemachine_Region = Class(name="trialStatemachine::Region")
trialStatemachine_ComplexState = Class(name="trialStatemachine::ComplexState")
State = Class(name="State")
trialStatemachine_Statemachine = Class(name="trialStatemachine::Statemachine")
Region = Class(name="Region")

# trialStatemachine_State class attributes and methods
trialStatemachine_State_name: Property = Property(name="name", type=StringType)
trialStatemachine_State_initialState: Property = Property(name="initialState", type=StringType)
trialStatemachine_State.attributes={trialStatemachine_State_name, trialStatemachine_State_initialState}

# trialStatemachine_LabeledTransition class attributes and methods
trialStatemachine_LabeledTransition_id: Property = Property(name="id", type=StringType)
trialStatemachine_LabeledTransition.attributes={trialStatemachine_LabeledTransition_id}

# trialStatemachine_Action class attributes and methods
trialStatemachine_Action_name: Property = Property(name="name", type=StringType)
trialStatemachine_Action.attributes={trialStatemachine_Action_name}

# trialStatemachine_Region class attributes and methods
trialStatemachine_Region_history: Property = Property(name="history", type=StringType)
trialStatemachine_Region.attributes={trialStatemachine_Region_history}

# trialStatemachine_ComplexState class attributes and methods

# State class attributes and methods

# trialStatemachine_Statemachine class attributes and methods
trialStatemachine_Statemachine_name: Property = Property(name="name", type=StringType)
trialStatemachine_Statemachine.attributes={trialStatemachine_Statemachine_name}

# Region class attributes and methods

# Relationships
actions5: BinaryAssociation = BinaryAssociation(
    name="actions5",
    ends={
        Property(name="trialStatemachine_Action", type=trialStatemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_Statemachine", type=trialStatemachine_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultHistory6: BinaryAssociation = BinaryAssociation(
    name="defaultHistory6",
    ends={
        Property(name="trialStatemachine_State8", type=trialStatemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_Region7", type=trialStatemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
states9: BinaryAssociation = BinaryAssociation(
    name="states9",
    ends={
        Property(name="trialStatemachine_State11", type=trialStatemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_Region10", type=trialStatemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoings0: BinaryAssociation = BinaryAssociation(
    name="outgoings0",
    ends={
        Property(name="trialStatemachine_LabeledTransition", type=trialStatemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_State", type=trialStatemachine_LabeledTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super1: BinaryAssociation = BinaryAssociation(
    name="super1",
    ends={
        Property(name="trialStatemachine_Region", type=trialStatemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_State2", type=trialStatemachine_Region, multiplicity=Multiplicity(1, 1))
    }
)
region3: BinaryAssociation = BinaryAssociation(
    name="region3",
    ends={
        Property(name="trialStatemachine_Region4", type=trialStatemachine_ComplexState, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_ComplexState", type=trialStatemachine_Region, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial12: BinaryAssociation = BinaryAssociation(
    name="initial12",
    ends={
        Property(name="trialStatemachine_State14", type=trialStatemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_Region13", type=trialStatemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
super15: BinaryAssociation = BinaryAssociation(
    name="super15",
    ends={
        Property(name="trialStatemachine_ComplexState17", type=trialStatemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_Region16", type=trialStatemachine_ComplexState, multiplicity=Multiplicity(0, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="trialStatemachine_State20", type=trialStatemachine_LabeledTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_LabeledTransition19", type=trialStatemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
action21: BinaryAssociation = BinaryAssociation(
    name="action21",
    ends={
        Property(name="trialStatemachine_Action23", type=trialStatemachine_LabeledTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="trialStatemachine_LabeledTransition22", type=trialStatemachine_Action, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_trialStatemachine_ComplexState_State = Generalization(general=State, specific=trialStatemachine_ComplexState)
gen_trialStatemachine_Statemachine_Region = Generalization(general=Region, specific=trialStatemachine_Statemachine)

# Domain Model
domain_model = DomainModel(
    name="trialStatemachine",
    types={trialStatemachine_State, trialStatemachine_LabeledTransition, trialStatemachine_Action, trialStatemachine_Region, trialStatemachine_ComplexState, State, trialStatemachine_Statemachine, Region},
    associations={actions5, defaultHistory6, states9, outgoings0, super1, region3, initial12, super15, target18, action21},
    generalizations={gen_trialStatemachine_ComplexState_State, gen_trialStatemachine_Statemachine_Region},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)