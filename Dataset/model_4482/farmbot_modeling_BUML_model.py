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
farmbot_modeling_Farmbot = Class(name="farmbot::modeling::Farmbot")
farmbot_modeling_Instruction = Class(name="farmbot::modeling::Instruction", is_abstract=True)
farmbot_modeling_SequenceCommand = Class(name="farmbot::modeling::SequenceCommand", is_abstract=True)
Command = Class(name="Command")
SequenceInstruction = Class(name="SequenceInstruction")
farmbot_modeling_Move = Class(name="farmbot::modeling::Move", is_abstract=True)
SequenceCommand = Class(name="SequenceCommand")
farmbot_modeling_TurnOnDigital = Class(name="farmbot::modeling::TurnOnDigital")
farmbot_modeling_TurnOff = Class(name="farmbot::modeling::TurnOff")
farmbot_modeling_MoveRelative = Class(name="farmbot::modeling::MoveRelative")
Move = Class(name="Move")
farmbot_modeling_FindHome = Class(name="farmbot::modeling::FindHome")
farmbot_modeling_Wait = Class(name="farmbot::modeling::Wait")
farmbot_modeling_SendMessage = Class(name="farmbot::modeling::SendMessage")
farmbot_modeling_RunFarmware = Class(name="farmbot::modeling::RunFarmware")
farmbot_modeling_TakePhoto = Class(name="farmbot::modeling::TakePhoto")
farmbot_modeling_IsEqualTo = Class(name="farmbot::modeling::IsEqualTo")
BooleanExpression = Class(name="BooleanExpression")
farmbot_modeling_IsNotEqualTo = Class(name="farmbot::modeling::IsNotEqualTo")
farmbot_modeling_IsGreaterThan = Class(name="farmbot::modeling::IsGreaterThan")
farmbot_modeling_IsLowerThan = Class(name="farmbot::modeling::IsLowerThan")
farmbot_modeling_Schedule = Class(name="farmbot::modeling::Schedule")
farmbot_modeling_Sequence = Class(name="farmbot::modeling::Sequence")
Instruction = Class(name="Instruction")
farmbot_modeling_SequenceInstruction = Class(name="farmbot::modeling::SequenceInstruction", is_abstract=True)
farmbot_modeling_If = Class(name="farmbot::modeling::If")
farmbot_modeling_BooleanExpression = Class(name="farmbot::modeling::BooleanExpression", is_abstract=True)
farmbot_modeling_ExecuteSequence = Class(name="farmbot::modeling::ExecuteSequence")
farmbot_modeling_MoveAbsolute = Class(name="farmbot::modeling::MoveAbsolute")
farmbot_modeling_Command = Class(name="farmbot::modeling::Command", is_abstract=True)
farmbot_modeling_ListSequences = Class(name="farmbot::modeling::ListSequences")
farmbot_modeling_ListScheduledEvents = Class(name="farmbot::modeling::ListScheduledEvents")
farmbot_modeling_TurnOnAnalog = Class(name="farmbot::modeling::TurnOnAnalog")

# farmbot_modeling_Farmbot class attributes and methods

# farmbot_modeling_Instruction class attributes and methods

# farmbot_modeling_SequenceCommand class attributes and methods

# Command class attributes and methods

# SequenceInstruction class attributes and methods

# farmbot_modeling_Move class attributes and methods
farmbot_modeling_Move_x: Property = Property(name="x", type=IntegerType)
farmbot_modeling_Move_y: Property = Property(name="y", type=IntegerType)
farmbot_modeling_Move_z: Property = Property(name="z", type=IntegerType)
farmbot_modeling_Move_speed: Property = Property(name="speed", type=IntegerType)
farmbot_modeling_Move.attributes={farmbot_modeling_Move_x, farmbot_modeling_Move_speed, farmbot_modeling_Move_y, farmbot_modeling_Move_z}

# SequenceCommand class attributes and methods

# farmbot_modeling_TurnOnDigital class attributes and methods
farmbot_modeling_TurnOnDigital_pin: Property = Property(name="pin", type=IntegerType)
farmbot_modeling_TurnOnDigital.attributes={farmbot_modeling_TurnOnDigital_pin}

# farmbot_modeling_TurnOff class attributes and methods
farmbot_modeling_TurnOff_pin: Property = Property(name="pin", type=IntegerType)
farmbot_modeling_TurnOff.attributes={farmbot_modeling_TurnOff_pin}

# farmbot_modeling_MoveRelative class attributes and methods

# Move class attributes and methods

# farmbot_modeling_FindHome class attributes and methods
farmbot_modeling_FindHome_axis: Property = Property(name="axis", type=StringType)
farmbot_modeling_FindHome.attributes={farmbot_modeling_FindHome_axis}

# farmbot_modeling_Wait class attributes and methods
farmbot_modeling_Wait_duration: Property = Property(name="duration", type=FloatType)
farmbot_modeling_Wait.attributes={farmbot_modeling_Wait_duration}

# farmbot_modeling_SendMessage class attributes and methods
farmbot_modeling_SendMessage_message: Property = Property(name="message", type=StringType)
farmbot_modeling_SendMessage_messageType: Property = Property(name="messageType", type=StringType)
farmbot_modeling_SendMessage.attributes={farmbot_modeling_SendMessage_message, farmbot_modeling_SendMessage_messageType}

# farmbot_modeling_RunFarmware class attributes and methods
farmbot_modeling_RunFarmware_name: Property = Property(name="name", type=StringType)
farmbot_modeling_RunFarmware.attributes={farmbot_modeling_RunFarmware_name}

# farmbot_modeling_TakePhoto class attributes and methods

# farmbot_modeling_IsEqualTo class attributes and methods

# BooleanExpression class attributes and methods

# farmbot_modeling_IsNotEqualTo class attributes and methods

# farmbot_modeling_IsGreaterThan class attributes and methods

# farmbot_modeling_IsLowerThan class attributes and methods

# farmbot_modeling_Schedule class attributes and methods
farmbot_modeling_Schedule_sequence: Property = Property(name="sequence", type=IntegerType)
farmbot_modeling_Schedule_startDate: Property = Property(name="startDate", type=StringType)
farmbot_modeling_Schedule_startTime: Property = Property(name="startTime", type=StringType)
farmbot_modeling_Schedule_repeat: Property = Property(name="repeat", type=BooleanType)
farmbot_modeling_Schedule_repeatUnit: Property = Property(name="repeatUnit", type=StringType)
farmbot_modeling_Schedule_endDate: Property = Property(name="endDate", type=StringType)
farmbot_modeling_Schedule_endTime: Property = Property(name="endTime", type=StringType)
farmbot_modeling_Schedule.attributes={farmbot_modeling_Schedule_endDate, farmbot_modeling_Schedule_repeat, farmbot_modeling_Schedule_repeatUnit, farmbot_modeling_Schedule_sequence, farmbot_modeling_Schedule_startTime, farmbot_modeling_Schedule_endTime, farmbot_modeling_Schedule_startDate}

# farmbot_modeling_Sequence class attributes and methods
farmbot_modeling_Sequence_name: Property = Property(name="name", type=StringType)
farmbot_modeling_Sequence.attributes={farmbot_modeling_Sequence_name}

# Instruction class attributes and methods

# farmbot_modeling_SequenceInstruction class attributes and methods

# farmbot_modeling_If class attributes and methods

# farmbot_modeling_BooleanExpression class attributes and methods
farmbot_modeling_BooleanExpression_value: Property = Property(name="value", type=IntegerType)
farmbot_modeling_BooleanExpression_axe: Property = Property(name="axe", type=StringType)
farmbot_modeling_BooleanExpression_pinNumber: Property = Property(name="pinNumber", type=IntegerType)
farmbot_modeling_BooleanExpression.attributes={farmbot_modeling_BooleanExpression_pinNumber, farmbot_modeling_BooleanExpression_axe, farmbot_modeling_BooleanExpression_value}

# farmbot_modeling_ExecuteSequence class attributes and methods
farmbot_modeling_ExecuteSequence_id: Property = Property(name="id", type=IntegerType)
farmbot_modeling_ExecuteSequence.attributes={farmbot_modeling_ExecuteSequence_id}

# farmbot_modeling_MoveAbsolute class attributes and methods

# farmbot_modeling_Command class attributes and methods

# farmbot_modeling_ListSequences class attributes and methods

# farmbot_modeling_ListScheduledEvents class attributes and methods

# farmbot_modeling_TurnOnAnalog class attributes and methods
farmbot_modeling_TurnOnAnalog_pin: Property = Property(name="pin", type=IntegerType)
farmbot_modeling_TurnOnAnalog_value: Property = Property(name="value", type=IntegerType)
farmbot_modeling_TurnOnAnalog.attributes={farmbot_modeling_TurnOnAnalog_pin, farmbot_modeling_TurnOnAnalog_value}

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="farmbot_modeling_Instruction", type=farmbot_modeling_Farmbot, multiplicity=Multiplicity(1, 1)),
        Property(name="farmbot_modeling_Farmbot", type=farmbot_modeling_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceInstructions1: BinaryAssociation = BinaryAssociation(
    name="sequenceInstructions1",
    ends={
        Property(name="farmbot_modeling_SequenceInstruction", type=farmbot_modeling_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="farmbot_modeling_Sequence", type=farmbot_modeling_SequenceInstruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booleanExpression2: BinaryAssociation = BinaryAssociation(
    name="booleanExpression2",
    ends={
        Property(name="farmbot_modeling_BooleanExpression", type=farmbot_modeling_If, multiplicity=Multiplicity(1, 1)),
        Property(name="farmbot_modeling_If", type=farmbot_modeling_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then3: BinaryAssociation = BinaryAssociation(
    name="then3",
    ends={
        Property(name="farmbot_modeling_ExecuteSequence", type=farmbot_modeling_If, multiplicity=Multiplicity(1, 1)),
        Property(name="farmbot_modeling_If4", type=farmbot_modeling_ExecuteSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else5: BinaryAssociation = BinaryAssociation(
    name="else5",
    ends={
        Property(name="farmbot_modeling_ExecuteSequence7", type=farmbot_modeling_If, multiplicity=Multiplicity(1, 1)),
        Property(name="farmbot_modeling_If6", type=farmbot_modeling_ExecuteSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_farmbot_modeling_SequenceCommand_Command = Generalization(general=Command, specific=farmbot_modeling_SequenceCommand)
gen_farmbot_modeling_SequenceCommand_SequenceInstruction = Generalization(general=SequenceInstruction, specific=farmbot_modeling_SequenceCommand)
gen_farmbot_modeling_Move_SequenceCommand = Generalization(general=SequenceCommand, specific=farmbot_modeling_Move)
gen_farmbot_modeling_TurnOnDigital_SequenceCommand = Generalization(general=SequenceCommand, specific=farmbot_modeling_TurnOnDigital)
gen_farmbot_modeling_TurnOff_SequenceCommand = Generalization(general=SequenceCommand, specific=farmbot_modeling_TurnOff)
gen_farmbot_modeling_MoveRelative_Move = Generalization(general=Move, specific=farmbot_modeling_MoveRelative)
gen_farmbot_modeling_FindHome_SequenceCommand = Generalization(general=SequenceCommand, specific=farmbot_modeling_FindHome)
gen_farmbot_modeling_ExecuteSequence_SequenceCommand = Generalization(general=SequenceCommand, specific=farmbot_modeling_ExecuteSequence)
gen_farmbot_modeling_Wait_SequenceCommand = Generalization(general=SequenceCommand, specific=farmbot_modeling_Wait)
gen_farmbot_modeling_SendMessage_SequenceCommand = Generalization(general=SequenceCommand, specific=farmbot_modeling_SendMessage)
gen_farmbot_modeling_RunFarmware_SequenceCommand = Generalization(general=SequenceCommand, specific=farmbot_modeling_RunFarmware)
gen_farmbot_modeling_TakePhoto_SequenceCommand = Generalization(general=SequenceCommand, specific=farmbot_modeling_TakePhoto)
gen_farmbot_modeling_SequenceInstruction_Instruction = Generalization(general=Instruction, specific=farmbot_modeling_SequenceInstruction)
gen_farmbot_modeling_IsEqualTo_BooleanExpression = Generalization(general=BooleanExpression, specific=farmbot_modeling_IsEqualTo)
gen_farmbot_modeling_IsNotEqualTo_BooleanExpression = Generalization(general=BooleanExpression, specific=farmbot_modeling_IsNotEqualTo)
gen_farmbot_modeling_IsGreaterThan_BooleanExpression = Generalization(general=BooleanExpression, specific=farmbot_modeling_IsGreaterThan)
gen_farmbot_modeling_IsLowerThan_BooleanExpression = Generalization(general=BooleanExpression, specific=farmbot_modeling_IsLowerThan)
gen_farmbot_modeling_Schedule_Command = Generalization(general=Command, specific=farmbot_modeling_Schedule)
gen_farmbot_modeling_Sequence_Instruction = Generalization(general=Instruction, specific=farmbot_modeling_Sequence)
gen_farmbot_modeling_If_SequenceInstruction = Generalization(general=SequenceInstruction, specific=farmbot_modeling_If)
gen_farmbot_modeling_MoveAbsolute_Move = Generalization(general=Move, specific=farmbot_modeling_MoveAbsolute)
gen_farmbot_modeling_Command_Instruction = Generalization(general=Instruction, specific=farmbot_modeling_Command)
gen_farmbot_modeling_ListSequences_Command = Generalization(general=Command, specific=farmbot_modeling_ListSequences)
gen_farmbot_modeling_ListScheduledEvents_Command = Generalization(general=Command, specific=farmbot_modeling_ListScheduledEvents)
gen_farmbot_modeling_TurnOnAnalog_SequenceCommand = Generalization(general=SequenceCommand, specific=farmbot_modeling_TurnOnAnalog)

# Domain Model
domain_model = DomainModel(
    name="farmbot_modeling",
    types={farmbot_modeling_Farmbot, farmbot_modeling_Instruction, farmbot_modeling_SequenceCommand, Command, SequenceInstruction, farmbot_modeling_Move, SequenceCommand, farmbot_modeling_TurnOnDigital, farmbot_modeling_TurnOff, farmbot_modeling_MoveRelative, Move, farmbot_modeling_FindHome, farmbot_modeling_Wait, farmbot_modeling_SendMessage, farmbot_modeling_RunFarmware, farmbot_modeling_TakePhoto, farmbot_modeling_IsEqualTo, BooleanExpression, farmbot_modeling_IsNotEqualTo, farmbot_modeling_IsGreaterThan, farmbot_modeling_IsLowerThan, farmbot_modeling_Schedule, farmbot_modeling_Sequence, Instruction, farmbot_modeling_SequenceInstruction, farmbot_modeling_If, farmbot_modeling_BooleanExpression, farmbot_modeling_ExecuteSequence, farmbot_modeling_MoveAbsolute, farmbot_modeling_Command, farmbot_modeling_ListSequences, farmbot_modeling_ListScheduledEvents, farmbot_modeling_TurnOnAnalog},
    associations={instructions0, sequenceInstructions1, booleanExpression2, then3, else5},
    generalizations={gen_farmbot_modeling_SequenceCommand_Command, gen_farmbot_modeling_SequenceCommand_SequenceInstruction, gen_farmbot_modeling_Move_SequenceCommand, gen_farmbot_modeling_TurnOnDigital_SequenceCommand, gen_farmbot_modeling_TurnOff_SequenceCommand, gen_farmbot_modeling_MoveRelative_Move, gen_farmbot_modeling_FindHome_SequenceCommand, gen_farmbot_modeling_ExecuteSequence_SequenceCommand, gen_farmbot_modeling_Wait_SequenceCommand, gen_farmbot_modeling_SendMessage_SequenceCommand, gen_farmbot_modeling_RunFarmware_SequenceCommand, gen_farmbot_modeling_TakePhoto_SequenceCommand, gen_farmbot_modeling_SequenceInstruction_Instruction, gen_farmbot_modeling_IsEqualTo_BooleanExpression, gen_farmbot_modeling_IsNotEqualTo_BooleanExpression, gen_farmbot_modeling_IsGreaterThan_BooleanExpression, gen_farmbot_modeling_IsLowerThan_BooleanExpression, gen_farmbot_modeling_Schedule_Command, gen_farmbot_modeling_Sequence_Instruction, gen_farmbot_modeling_If_SequenceInstruction, gen_farmbot_modeling_MoveAbsolute_Move, gen_farmbot_modeling_Command_Instruction, gen_farmbot_modeling_ListSequences_Command, gen_farmbot_modeling_ListScheduledEvents_Command, gen_farmbot_modeling_TurnOnAnalog_SequenceCommand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)