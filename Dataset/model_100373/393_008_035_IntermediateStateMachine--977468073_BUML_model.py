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
MDAIntermediateStateMachine_Operation = Class(name="MDAIntermediateStateMachine_Operation")
MDAIntermediateStateMachine_Content = Class(name="MDAIntermediateStateMachine_Content")
MDAIntermediateStateMachine_State = Class(name="MDAIntermediateStateMachine_State")
MDAIntermediateStateMachine_Automaton = Class(name="MDAIntermediateStateMachine_Automaton")
MDAIntermediateStateMachine_Participant = Class(name="MDAIntermediateStateMachine_Participant")
MDAIntermediateStateMachine_Message = Class(name="MDAIntermediateStateMachine_Message")
MDAIntermediateStateMachine_MessageSequence = Class(name="MDAIntermediateStateMachine_MessageSequence")
MDAIntermediateStateMachine_Transition = Class(name="MDAIntermediateStateMachine_Transition")
MDAIntermediateStateMachine_Value = Class(name="MDAIntermediateStateMachine_Value")

# MDAIntermediateStateMachine_Operation class attributes and methods
MDAIntermediateStateMachine_Operation_name: Property = Property(name="name", type=StringType)
MDAIntermediateStateMachine_Operation.attributes={MDAIntermediateStateMachine_Operation_name}

# MDAIntermediateStateMachine_Content class attributes and methods
MDAIntermediateStateMachine_Content_name: Property = Property(name="name", type=StringType)
MDAIntermediateStateMachine_Content.attributes={MDAIntermediateStateMachine_Content_name}

# MDAIntermediateStateMachine_State class attributes and methods
MDAIntermediateStateMachine_State_name: Property = Property(name="name", type=StringType)
MDAIntermediateStateMachine_State.attributes={MDAIntermediateStateMachine_State_name}

# MDAIntermediateStateMachine_Automaton class attributes and methods
MDAIntermediateStateMachine_Automaton_name: Property = Property(name="name", type=StringType)
MDAIntermediateStateMachine_Automaton.attributes={MDAIntermediateStateMachine_Automaton_name}

# MDAIntermediateStateMachine_Participant class attributes and methods
MDAIntermediateStateMachine_Participant_name: Property = Property(name="name", type=StringType)
MDAIntermediateStateMachine_Participant.attributes={MDAIntermediateStateMachine_Participant_name}

# MDAIntermediateStateMachine_Message class attributes and methods

# MDAIntermediateStateMachine_MessageSequence class attributes and methods

# MDAIntermediateStateMachine_Transition class attributes and methods

# MDAIntermediateStateMachine_Value class attributes and methods
MDAIntermediateStateMachine_Value_value: Property = Property(name="value", type=StringType)
MDAIntermediateStateMachine_Value.attributes={MDAIntermediateStateMachine_Value_value}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="MDAIntermediateStateMachine_State", type=MDAIntermediateStateMachine_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Content", type=MDAIntermediateStateMachine_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
automatons1: BinaryAssociation = BinaryAssociation(
    name="automatons1",
    ends={
        Property(name="MDAIntermediateStateMachine_Automaton", type=MDAIntermediateStateMachine_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Content2", type=MDAIntermediateStateMachine_Automaton, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states14: BinaryAssociation = BinaryAssociation(
    name="states14",
    ends={
        Property(name="MDAIntermediateStateMachine_Automaton15", type=MDAIntermediateStateMachine_State, multiplicity=Multiplicity(1, 9999)),
        Property(name="MDAIntermediateStateMachine_State16", type=MDAIntermediateStateMachine_Automaton, multiplicity=Multiplicity(1, 1))
    }
)
operations3: BinaryAssociation = BinaryAssociation(
    name="operations3",
    ends={
        Property(name="MDAIntermediateStateMachine_Operation", type=MDAIntermediateStateMachine_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Content4", type=MDAIntermediateStateMachine_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
participants5: BinaryAssociation = BinaryAssociation(
    name="participants5",
    ends={
        Property(name="MDAIntermediateStateMachine_Participant", type=MDAIntermediateStateMachine_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Content6", type=MDAIntermediateStateMachine_Participant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messages7: BinaryAssociation = BinaryAssociation(
    name="messages7",
    ends={
        Property(name="MDAIntermediateStateMachine_Message", type=MDAIntermediateStateMachine_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Content8", type=MDAIntermediateStateMachine_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequences9: BinaryAssociation = BinaryAssociation(
    name="sequences9",
    ends={
        Property(name="MDAIntermediateStateMachine_MessageSequence", type=MDAIntermediateStateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_State10", type=MDAIntermediateStateMachine_MessageSequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState11: BinaryAssociation = BinaryAssociation(
    name="initialState11",
    ends={
        Property(name="MDAIntermediateStateMachine_State13", type=MDAIntermediateStateMachine_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Automaton12", type=MDAIntermediateStateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
transitions17: BinaryAssociation = BinaryAssociation(
    name="transitions17",
    ends={
        Property(name="MDAIntermediateStateMachine_Transition", type=MDAIntermediateStateMachine_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Automaton18", type=MDAIntermediateStateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participant19: BinaryAssociation = BinaryAssociation(
    name="participant19",
    ends={
        Property(name="MDAIntermediateStateMachine_Participant21", type=MDAIntermediateStateMachine_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Automaton20", type=MDAIntermediateStateMachine_Participant, multiplicity=Multiplicity(1, 1))
    }
)
preState22: BinaryAssociation = BinaryAssociation(
    name="preState22",
    ends={
        Property(name="MDAIntermediateStateMachine_State24", type=MDAIntermediateStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Transition23", type=MDAIntermediateStateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
postState25: BinaryAssociation = BinaryAssociation(
    name="postState25",
    ends={
        Property(name="MDAIntermediateStateMachine_State27", type=MDAIntermediateStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Transition26", type=MDAIntermediateStateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
input28: BinaryAssociation = BinaryAssociation(
    name="input28",
    ends={
        Property(name="MDAIntermediateStateMachine_Operation30", type=MDAIntermediateStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Transition29", type=MDAIntermediateStateMachine_Operation, multiplicity=Multiplicity(0, 1))
    }
)
returnValue31: BinaryAssociation = BinaryAssociation(
    name="returnValue31",
    ends={
        Property(name="MDAIntermediateStateMachine_Value", type=MDAIntermediateStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Transition32", type=MDAIntermediateStateMachine_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation33: BinaryAssociation = BinaryAssociation(
    name="operation33",
    ends={
        Property(name="MDAIntermediateStateMachine_Operation35", type=MDAIntermediateStateMachine_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Message34", type=MDAIntermediateStateMachine_Operation, multiplicity=Multiplicity(1, 1))
    }
)
receiver36: BinaryAssociation = BinaryAssociation(
    name="receiver36",
    ends={
        Property(name="MDAIntermediateStateMachine_Participant38", type=MDAIntermediateStateMachine_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Message37", type=MDAIntermediateStateMachine_Participant, multiplicity=Multiplicity(1, 1))
    }
)
returnValue39: BinaryAssociation = BinaryAssociation(
    name="returnValue39",
    ends={
        Property(name="MDAIntermediateStateMachine_Value41", type=MDAIntermediateStateMachine_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_Message40", type=MDAIntermediateStateMachine_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messages42: BinaryAssociation = BinaryAssociation(
    name="messages42",
    ends={
        Property(name="MDAIntermediateStateMachine_Message44", type=MDAIntermediateStateMachine_MessageSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="MDAIntermediateStateMachine_MessageSequence43", type=MDAIntermediateStateMachine_Message, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="MDAIntermediateStateMachine",
    types={MDAIntermediateStateMachine_Operation, MDAIntermediateStateMachine_Content, MDAIntermediateStateMachine_State, MDAIntermediateStateMachine_Automaton, MDAIntermediateStateMachine_Participant, MDAIntermediateStateMachine_Message, MDAIntermediateStateMachine_MessageSequence, MDAIntermediateStateMachine_Transition, MDAIntermediateStateMachine_Value},
    associations={states0, automatons1, states14, operations3, participants5, messages7, sequences9, initialState11, transitions17, participant19, preState22, postState25, input28, returnValue31, operation33, receiver36, returnValue39, messages42},
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