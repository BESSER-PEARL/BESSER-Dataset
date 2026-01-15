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

# Enumerations
DistanceUnit: Enumeration = Enumeration(
    name="DistanceUnit",
    literals={
            EnumerationLiteral(name="CENTIMETERS")
    }
)

AngleUnit: Enumeration = Enumeration(
    name="AngleUnit",
    literals={
            EnumerationLiteral(name="DEGREES")
    }
)

TimeUnit: Enumeration = Enumeration(
    name="TimeUnit",
    literals={
            EnumerationLiteral(name="SECONDS"),
			EnumerationLiteral(name="MILLISECONDS")
    }
)

DetectedType: Enumeration = Enumeration(
    name="DetectedType",
    literals={
            EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="BALL"),
			EnumerationLiteral(name="WALL")
    }
)

# Classes
RobotProjectModel_MoveStraight = Class(name="RobotProjectModel::MoveStraight")
TimedInstruction = Class(name="TimedInstruction")
RobotProjectModel_Distance = Class(name="RobotProjectModel::Distance")
RobotProjectModel_Robot = Class(name="RobotProjectModel::Robot")
RobotProjectModel_TimedInstruction = Class(name="RobotProjectModel::TimedInstruction", is_abstract=True)
Instruction = Class(name="Instruction")
RobotProjectModel_Duration = Class(name="RobotProjectModel::Duration")
RobotProjectModel_Turn = Class(name="RobotProjectModel::Turn")
RobotProjectModel_Angle = Class(name="RobotProjectModel::Angle")
RobotProjectModel_Amount = Class(name="RobotProjectModel::Amount")
Amount = Class(name="Amount")
RobotProjectModel_Function = Class(name="RobotProjectModel::Function")
RobotProjectModel_InstructionBlock = Class(name="RobotProjectModel::InstructionBlock")
RobotProjectModel_Instruction = Class(name="RobotProjectModel::Instruction", is_abstract=True)
RobotProjectModel_Condition = Class(name="RobotProjectModel::Condition", is_abstract=True)
RobotProjectModel_SensorActivation = Class(name="RobotProjectModel::SensorActivation")
Condition = Class(name="Condition")
RobotProjectModel_Grab = Class(name="RobotProjectModel::Grab")
RobotProjectModel_Release = Class(name="RobotProjectModel::Release")
RobotProjectModel_Wait = Class(name="RobotProjectModel::Wait")
RobotProjectModel_If = Class(name="RobotProjectModel::If")
RobotProjectModel_DetectedObjectIs = Class(name="RobotProjectModel::DetectedObjectIs")
RobotProjectModel_HomeDirection = Class(name="RobotProjectModel::HomeDirection")
Angle = Class(name="Angle")
RobotProjectModel_Print = Class(name="RobotProjectModel::Print")
RobotProjectModel_Call = Class(name="RobotProjectModel::Call")

# RobotProjectModel_MoveStraight class attributes and methods

# TimedInstruction class attributes and methods

# RobotProjectModel_Distance class attributes and methods
RobotProjectModel_Distance_distanceUnit: Property = Property(name="distanceUnit", type=StringType)
RobotProjectModel_Distance.attributes={RobotProjectModel_Distance_distanceUnit}

# RobotProjectModel_Robot class attributes and methods

# RobotProjectModel_TimedInstruction class attributes and methods

# Instruction class attributes and methods

# RobotProjectModel_Duration class attributes and methods
RobotProjectModel_Duration_timeUnit: Property = Property(name="timeUnit", type=StringType)
RobotProjectModel_Duration.attributes={RobotProjectModel_Duration_timeUnit}

# RobotProjectModel_Turn class attributes and methods

# RobotProjectModel_Angle class attributes and methods
RobotProjectModel_Angle_angleUnit: Property = Property(name="angleUnit", type=StringType)
RobotProjectModel_Angle.attributes={RobotProjectModel_Angle_angleUnit}

# RobotProjectModel_Amount class attributes and methods
RobotProjectModel_Amount_value: Property = Property(name="value", type=IntegerType)
RobotProjectModel_Amount.attributes={RobotProjectModel_Amount_value}

# Amount class attributes and methods

# RobotProjectModel_Function class attributes and methods
RobotProjectModel_Function_name: Property = Property(name="name", type=StringType)
RobotProjectModel_Function.attributes={RobotProjectModel_Function_name}

# RobotProjectModel_InstructionBlock class attributes and methods

# RobotProjectModel_Instruction class attributes and methods

# RobotProjectModel_Condition class attributes and methods

# RobotProjectModel_SensorActivation class attributes and methods

# Condition class attributes and methods

# RobotProjectModel_Grab class attributes and methods

# RobotProjectModel_Release class attributes and methods

# RobotProjectModel_Wait class attributes and methods

# RobotProjectModel_If class attributes and methods

# RobotProjectModel_DetectedObjectIs class attributes and methods
RobotProjectModel_DetectedObjectIs_rightOperand: Property = Property(name="rightOperand", type=StringType)
RobotProjectModel_DetectedObjectIs.attributes={RobotProjectModel_DetectedObjectIs_rightOperand}

# RobotProjectModel_HomeDirection class attributes and methods

# Angle class attributes and methods

# RobotProjectModel_Print class attributes and methods
RobotProjectModel_Print_string: Property = Property(name="string", type=StringType)
RobotProjectModel_Print.attributes={RobotProjectModel_Print_string}

# RobotProjectModel_Call class attributes and methods

# Relationships
distance0: BinaryAssociation = BinaryAssociation(
    name="distance0",
    ends={
        Property(name="RobotProjectModel_Distance", type=RobotProjectModel_MoveStraight, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotProjectModel_MoveStraight", type=RobotProjectModel_Distance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instructions1: BinaryAssociation = BinaryAssociation(
    name="instructions1",
    ends={
        Property(name="RobotProjectModel_Instruction", type=RobotProjectModel_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotProjectModel_Robot", type=RobotProjectModel_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duration2: BinaryAssociation = BinaryAssociation(
    name="duration2",
    ends={
        Property(name="RobotProjectModel_Duration", type=RobotProjectModel_TimedInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotProjectModel_TimedInstruction", type=RobotProjectModel_Duration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle3: BinaryAssociation = BinaryAssociation(
    name="angle3",
    ends={
        Property(name="RobotProjectModel_Angle", type=RobotProjectModel_Turn, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotProjectModel_Turn", type=RobotProjectModel_Angle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructionBlock4: BinaryAssociation = BinaryAssociation(
    name="instructionBlock4",
    ends={
        Property(name="RobotProjectModel_InstructionBlock", type=RobotProjectModel_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotProjectModel_Function", type=RobotProjectModel_InstructionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition7: BinaryAssociation = BinaryAssociation(
    name="condition7",
    ends={
        Property(name="RobotProjectModel_Condition", type=RobotProjectModel_If, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotProjectModel_If", type=RobotProjectModel_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseBlock8: BinaryAssociation = BinaryAssociation(
    name="falseBlock8",
    ends={
        Property(name="RobotProjectModel_InstructionBlock10", type=RobotProjectModel_If, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotProjectModel_If9", type=RobotProjectModel_InstructionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trueBlock11: BinaryAssociation = BinaryAssociation(
    name="trueBlock11",
    ends={
        Property(name="RobotProjectModel_InstructionBlock13", type=RobotProjectModel_If, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotProjectModel_If12", type=RobotProjectModel_InstructionBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions14: BinaryAssociation = BinaryAssociation(
    name="instructions14",
    ends={
        Property(name="RobotProjectModel_Instruction16", type=RobotProjectModel_InstructionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotProjectModel_InstructionBlock15", type=RobotProjectModel_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
destination5: BinaryAssociation = BinaryAssociation(
    name="destination5",
    ends={
        Property(name="RobotProjectModel_Function6", type=RobotProjectModel_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="RobotProjectModel_Call", type=RobotProjectModel_Function, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_RobotProjectModel_MoveStraight_TimedInstruction = Generalization(general=TimedInstruction, specific=RobotProjectModel_MoveStraight)
gen_RobotProjectModel_TimedInstruction_Instruction = Generalization(general=Instruction, specific=RobotProjectModel_TimedInstruction)
gen_RobotProjectModel_Turn_TimedInstruction = Generalization(general=TimedInstruction, specific=RobotProjectModel_Turn)
gen_RobotProjectModel_Duration_Amount = Generalization(general=Amount, specific=RobotProjectModel_Duration)
gen_RobotProjectModel_Function_Instruction = Generalization(general=Instruction, specific=RobotProjectModel_Function)
gen_RobotProjectModel_Angle_Amount = Generalization(general=Amount, specific=RobotProjectModel_Angle)
gen_RobotProjectModel_SensorActivation_Condition = Generalization(general=Condition, specific=RobotProjectModel_SensorActivation)
gen_RobotProjectModel_Grab_Instruction = Generalization(general=Instruction, specific=RobotProjectModel_Grab)
gen_RobotProjectModel_Release_Instruction = Generalization(general=Instruction, specific=RobotProjectModel_Release)
gen_RobotProjectModel_Wait_TimedInstruction = Generalization(general=TimedInstruction, specific=RobotProjectModel_Wait)
gen_RobotProjectModel_If_Instruction = Generalization(general=Instruction, specific=RobotProjectModel_If)
gen_RobotProjectModel_InstructionBlock_Instruction = Generalization(general=Instruction, specific=RobotProjectModel_InstructionBlock)
gen_RobotProjectModel_DetectedObjectIs_Condition = Generalization(general=Condition, specific=RobotProjectModel_DetectedObjectIs)
gen_RobotProjectModel_HomeDirection_Angle = Generalization(general=Angle, specific=RobotProjectModel_HomeDirection)
gen_RobotProjectModel_Print_Instruction = Generalization(general=Instruction, specific=RobotProjectModel_Print)
gen_RobotProjectModel_Call_Instruction = Generalization(general=Instruction, specific=RobotProjectModel_Call)
gen_RobotProjectModel_Distance_Amount = Generalization(general=Amount, specific=RobotProjectModel_Distance)

# Domain Model
domain_model = DomainModel(
    name="RobotProjectModel",
    types={RobotProjectModel_MoveStraight, TimedInstruction, RobotProjectModel_Distance, RobotProjectModel_Robot, RobotProjectModel_TimedInstruction, Instruction, RobotProjectModel_Duration, RobotProjectModel_Turn, RobotProjectModel_Angle, RobotProjectModel_Amount, Amount, RobotProjectModel_Function, RobotProjectModel_InstructionBlock, RobotProjectModel_Instruction, RobotProjectModel_Condition, RobotProjectModel_SensorActivation, Condition, RobotProjectModel_Grab, RobotProjectModel_Release, RobotProjectModel_Wait, RobotProjectModel_If, RobotProjectModel_DetectedObjectIs, RobotProjectModel_HomeDirection, Angle, RobotProjectModel_Print, RobotProjectModel_Call, DistanceUnit, AngleUnit, TimeUnit, DetectedType},
    associations={distance0, instructions1, duration2, angle3, instructionBlock4, condition7, falseBlock8, trueBlock11, instructions14, destination5},
    generalizations={gen_RobotProjectModel_MoveStraight_TimedInstruction, gen_RobotProjectModel_TimedInstruction_Instruction, gen_RobotProjectModel_Turn_TimedInstruction, gen_RobotProjectModel_Duration_Amount, gen_RobotProjectModel_Function_Instruction, gen_RobotProjectModel_Angle_Amount, gen_RobotProjectModel_SensorActivation_Condition, gen_RobotProjectModel_Grab_Instruction, gen_RobotProjectModel_Release_Instruction, gen_RobotProjectModel_Wait_TimedInstruction, gen_RobotProjectModel_If_Instruction, gen_RobotProjectModel_InstructionBlock_Instruction, gen_RobotProjectModel_DetectedObjectIs_Condition, gen_RobotProjectModel_HomeDirection_Angle, gen_RobotProjectModel_Print_Instruction, gen_RobotProjectModel_Call_Instruction, gen_RobotProjectModel_Distance_Amount},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)