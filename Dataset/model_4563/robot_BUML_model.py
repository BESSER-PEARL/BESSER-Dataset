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
robot_robot_Command = Class(name="robot::robot::Command", is_abstract=True)
Expression = Class(name="Expression")
robot_robot_MoveCmd = Class(name="robot::robot::MoveCmd")
Command = Class(name="Command")
robot_robot_ObstacleCmd = Class(name="robot::robot::ObstacleCmd")
FlotCtrl_BoolExp = Class(name="FlotCtrl::BoolExp")
robot_Command = Class(name="robot::Command")
BoolExp = Class(name="BoolExp")
robot_FlotCtrl_NegExp = Class(name="robot::FlotCtrl::NegExp")
robot_FlotCtrl_BoolExp = Class(name="robot::FlotCtrl::BoolExp", is_abstract=True)
robot_FlotCtrl_AndExp = Class(name="robot::FlotCtrl::AndExp")
robot_robot_Bip = Class(name="robot::robot::Bip")
robot_robot_SetTurnAngleCmd = Class(name="robot::robot::SetTurnAngleCmd")
robot_robot_HasTurnedCmd = Class(name="robot::robot::HasTurnedCmd")
robot_robot_TurnCmd = Class(name="robot::robot::TurnCmd")
robot_robot_StopEngineCmd = Class(name="robot::robot::StopEngineCmd")
robot_robot_StopProgramCmd = Class(name="robot::robot::StopProgramCmd")
robot_robot_PrintCmd = Class(name="robot::robot::PrintCmd")
robot_robot_ProgramUnit = Class(name="robot::robot::ProgramUnit")
robot_FlotCtrl_Expression = Class(name="robot::FlotCtrl::Expression", is_abstract=True)
robot_FlotCtrl_WhileLoop = Class(name="robot::FlotCtrl::WhileLoop")
robot_FlotCtrl_IfBlock = Class(name="robot::FlotCtrl::IfBlock")

# robot_robot_Command class attributes and methods

# Expression class attributes and methods

# robot_robot_MoveCmd class attributes and methods
robot_robot_MoveCmd_power: Property = Property(name="power", type=StringType)
robot_robot_MoveCmd.attributes={robot_robot_MoveCmd_power}

# Command class attributes and methods

# robot_robot_ObstacleCmd class attributes and methods
robot_robot_ObstacleCmd_distance: Property = Property(name="distance", type=StringType)
robot_robot_ObstacleCmd.attributes={robot_robot_ObstacleCmd_distance}

# FlotCtrl_BoolExp class attributes and methods

# robot_Command class attributes and methods

# BoolExp class attributes and methods

# robot_FlotCtrl_NegExp class attributes and methods

# robot_FlotCtrl_BoolExp class attributes and methods

# robot_FlotCtrl_AndExp class attributes and methods

# robot_robot_Bip class attributes and methods
robot_robot_Bip_duration: Property = Property(name="duration", type=StringType)
robot_robot_Bip_power: Property = Property(name="power", type=StringType)
robot_robot_Bip_repet: Property = Property(name="repet", type=StringType)
robot_robot_Bip.attributes={robot_robot_Bip_power, robot_robot_Bip_repet, robot_robot_Bip_duration}

# robot_robot_SetTurnAngleCmd class attributes and methods
robot_robot_SetTurnAngleCmd_angle: Property = Property(name="angle", type=StringType)
robot_robot_SetTurnAngleCmd.attributes={robot_robot_SetTurnAngleCmd_angle}

# robot_robot_HasTurnedCmd class attributes and methods
robot_robot_HasTurnedCmd_angle: Property = Property(name="angle", type=StringType)
robot_robot_HasTurnedCmd.attributes={robot_robot_HasTurnedCmd_angle}

# robot_robot_TurnCmd class attributes and methods
robot_robot_TurnCmd_power: Property = Property(name="power", type=StringType)
robot_robot_TurnCmd_angle: Property = Property(name="angle", type=StringType)
robot_robot_TurnCmd.attributes={robot_robot_TurnCmd_power, robot_robot_TurnCmd_angle}

# robot_robot_StopEngineCmd class attributes and methods

# robot_robot_StopProgramCmd class attributes and methods

# robot_robot_PrintCmd class attributes and methods
robot_robot_PrintCmd_msg: Property = Property(name="msg", type=StringType)
robot_robot_PrintCmd_duration: Property = Property(name="duration", type=StringType)
robot_robot_PrintCmd_line: Property = Property(name="line", type=StringType)
robot_robot_PrintCmd_col: Property = Property(name="col", type=StringType)
robot_robot_PrintCmd.attributes={robot_robot_PrintCmd_duration, robot_robot_PrintCmd_msg, robot_robot_PrintCmd_col, robot_robot_PrintCmd_line}

# robot_robot_ProgramUnit class attributes and methods

# robot_FlotCtrl_Expression class attributes and methods

# robot_FlotCtrl_WhileLoop class attributes and methods

# robot_FlotCtrl_IfBlock class attributes and methods

# Relationships
loopCond1: BinaryAssociation = BinaryAssociation(
    name="loopCond1",
    ends={
        Property(name="BoolExp", type=robot_FlotCtrl_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_FlotCtrl_WhileLoop", type=BoolExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block2: BinaryAssociation = BinaryAssociation(
    name="block2",
    ends={
        Property(name="Expression4", type=robot_FlotCtrl_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_FlotCtrl_WhileLoop3", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp5: BinaryAssociation = BinaryAssociation(
    name="exp5",
    ends={
        Property(name="BoolExp6", type=robot_FlotCtrl_NegExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_FlotCtrl_NegExp", type=BoolExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftExp7: BinaryAssociation = BinaryAssociation(
    name="leftExp7",
    ends={
        Property(name="BoolExp8", type=robot_FlotCtrl_AndExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_FlotCtrl_AndExp", type=BoolExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block0: BinaryAssociation = BinaryAssociation(
    name="block0",
    ends={
        Property(name="Expression", type=robot_robot_ProgramUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_robot_ProgramUnit", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightExp9: BinaryAssociation = BinaryAssociation(
    name="rightExp9",
    ends={
        Property(name="BoolExp11", type=robot_FlotCtrl_AndExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_FlotCtrl_AndExp10", type=BoolExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition12: BinaryAssociation = BinaryAssociation(
    name="condition12",
    ends={
        Property(name="BoolExp13", type=robot_FlotCtrl_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_FlotCtrl_IfBlock", type=BoolExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenBlock14: BinaryAssociation = BinaryAssociation(
    name="thenBlock14",
    ends={
        Property(name="Expression16", type=robot_FlotCtrl_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_FlotCtrl_IfBlock15", type=Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elseBlock17: BinaryAssociation = BinaryAssociation(
    name="elseBlock17",
    ends={
        Property(name="Expression19", type=robot_FlotCtrl_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_FlotCtrl_IfBlock18", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_robot_robot_Command_Expression = Generalization(general=Expression, specific=robot_robot_Command)
gen_robot_robot_MoveCmd_Command = Generalization(general=Command, specific=robot_robot_MoveCmd)
gen_robot_robot_ObstacleCmd_FlotCtrl_BoolExp = Generalization(general=FlotCtrl_BoolExp, specific=robot_robot_ObstacleCmd)
gen_robot_robot_ObstacleCmd_robot_Command = Generalization(general=robot_Command, specific=robot_robot_ObstacleCmd)
gen_robot_FlotCtrl_NegExp_BoolExp = Generalization(general=BoolExp, specific=robot_FlotCtrl_NegExp)
gen_robot_FlotCtrl_BoolExp_Expression = Generalization(general=Expression, specific=robot_FlotCtrl_BoolExp)
gen_robot_FlotCtrl_AndExp_BoolExp = Generalization(general=BoolExp, specific=robot_FlotCtrl_AndExp)
gen_robot_robot_Bip_Command = Generalization(general=Command, specific=robot_robot_Bip)
gen_robot_robot_SetTurnAngleCmd_Command = Generalization(general=Command, specific=robot_robot_SetTurnAngleCmd)
gen_robot_robot_HasTurnedCmd_FlotCtrl_BoolExp = Generalization(general=FlotCtrl_BoolExp, specific=robot_robot_HasTurnedCmd)
gen_robot_robot_HasTurnedCmd_robot_Command = Generalization(general=robot_Command, specific=robot_robot_HasTurnedCmd)
gen_robot_robot_TurnCmd_Command = Generalization(general=Command, specific=robot_robot_TurnCmd)
gen_robot_robot_StopEngineCmd_Command = Generalization(general=Command, specific=robot_robot_StopEngineCmd)
gen_robot_robot_StopProgramCmd_Command = Generalization(general=Command, specific=robot_robot_StopProgramCmd)
gen_robot_robot_PrintCmd_Command = Generalization(general=Command, specific=robot_robot_PrintCmd)
gen_robot_FlotCtrl_WhileLoop_Expression = Generalization(general=Expression, specific=robot_FlotCtrl_WhileLoop)
gen_robot_FlotCtrl_IfBlock_Expression = Generalization(general=Expression, specific=robot_FlotCtrl_IfBlock)

# Domain Model
domain_model = DomainModel(
    name="robot",
    types={robot_robot_Command, Expression, robot_robot_MoveCmd, Command, robot_robot_ObstacleCmd, FlotCtrl_BoolExp, robot_Command, BoolExp, robot_FlotCtrl_NegExp, robot_FlotCtrl_BoolExp, robot_FlotCtrl_AndExp, robot_robot_Bip, robot_robot_SetTurnAngleCmd, robot_robot_HasTurnedCmd, robot_robot_TurnCmd, robot_robot_StopEngineCmd, robot_robot_StopProgramCmd, robot_robot_PrintCmd, robot_robot_ProgramUnit, robot_FlotCtrl_Expression, robot_FlotCtrl_WhileLoop, robot_FlotCtrl_IfBlock},
    associations={loopCond1, block2, exp5, leftExp7, block0, rightExp9, condition12, thenBlock14, elseBlock17},
    generalizations={gen_robot_robot_Command_Expression, gen_robot_robot_MoveCmd_Command, gen_robot_robot_ObstacleCmd_FlotCtrl_BoolExp, gen_robot_robot_ObstacleCmd_robot_Command, gen_robot_FlotCtrl_NegExp_BoolExp, gen_robot_FlotCtrl_BoolExp_Expression, gen_robot_FlotCtrl_AndExp_BoolExp, gen_robot_robot_Bip_Command, gen_robot_robot_SetTurnAngleCmd_Command, gen_robot_robot_HasTurnedCmd_FlotCtrl_BoolExp, gen_robot_robot_HasTurnedCmd_robot_Command, gen_robot_robot_TurnCmd_Command, gen_robot_robot_StopEngineCmd_Command, gen_robot_robot_StopProgramCmd_Command, gen_robot_robot_PrintCmd_Command, gen_robot_FlotCtrl_WhileLoop_Expression, gen_robot_FlotCtrl_IfBlock_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)