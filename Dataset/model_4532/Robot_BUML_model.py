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
robotG_robot_Turn = Class(name="robotG::robot::Turn")
robotG_robot_SetTurnAngle = Class(name="robotG::robot::SetTurnAngle")
robotG_robot_HasTurned = Class(name="robotG::robot::HasTurned")
flow_ExprBool = Class(name="flow::ExprBool")
robot_CommandeRobot = Class(name="robot::CommandeRobot")
robotG_robot_Display = Class(name="robotG::robot::Display")
robotG_robot_Obstacle = Class(name="robotG::robot::Obstacle")
robotG_robot_StopEngine = Class(name="robotG::robot::StopEngine")
robotG_robot_CommandeRobot = Class(name="robotG::robot::CommandeRobot", is_abstract=True)
Expr = Class(name="Expr")
robotG_flow_While = Class(name="robotG::flow::While")
ExprBool = Class(name="ExprBool")
robotG_flow_If = Class(name="robotG::flow::If")
robotG_flow_Not = Class(name="robotG::flow::Not")
OpUnaire = Class(name="OpUnaire")
robotG_flow_ExprBool = Class(name="robotG::flow::ExprBool", is_abstract=True)
robotG_flow_StopProgram = Class(name="robotG::flow::StopProgram")
robotG_robot_Move = Class(name="robotG::robot::Move")
CommandeRobot = Class(name="CommandeRobot")
robotG_robot_Bip = Class(name="robotG::robot::Bip")
robotG_flow_And = Class(name="robotG::flow::And")
OpBinaire = Class(name="OpBinaire")
robotG_flow_Or = Class(name="robotG::flow::Or")
robotG_flow_Programme = Class(name="robotG::flow::Programme")
robotG_flow_Expr = Class(name="robotG::flow::Expr", is_abstract=True)
robotG_flow_OpUnaire = Class(name="robotG::flow::OpUnaire", is_abstract=True)
robotG_flow_OpBinaire = Class(name="robotG::flow::OpBinaire", is_abstract=True)

# robotG_robot_Turn class attributes and methods
robotG_robot_Turn_power: Property = Property(name="power", type=IntegerType)
robotG_robot_Turn_angle: Property = Property(name="angle", type=IntegerType)
robotG_robot_Turn.attributes={robotG_robot_Turn_power, robotG_robot_Turn_angle}

# robotG_robot_SetTurnAngle class attributes and methods
robotG_robot_SetTurnAngle_angle: Property = Property(name="angle", type=IntegerType)
robotG_robot_SetTurnAngle.attributes={robotG_robot_SetTurnAngle_angle}

# robotG_robot_HasTurned class attributes and methods
robotG_robot_HasTurned_angle: Property = Property(name="angle", type=IntegerType)
robotG_robot_HasTurned.attributes={robotG_robot_HasTurned_angle}

# flow_ExprBool class attributes and methods

# robot_CommandeRobot class attributes and methods

# robotG_robot_Display class attributes and methods
robotG_robot_Display_msg: Property = Property(name="msg", type=StringType)
robotG_robot_Display_duration: Property = Property(name="duration", type=IntegerType)
robotG_robot_Display_line: Property = Property(name="line", type=IntegerType)
robotG_robot_Display_col: Property = Property(name="col", type=IntegerType)
robotG_robot_Display.attributes={robotG_robot_Display_col, robotG_robot_Display_duration, robotG_robot_Display_line, robotG_robot_Display_msg}

# robotG_robot_Obstacle class attributes and methods
robotG_robot_Obstacle_distance: Property = Property(name="distance", type=IntegerType)
robotG_robot_Obstacle.attributes={robotG_robot_Obstacle_distance}

# robotG_robot_StopEngine class attributes and methods

# robotG_robot_CommandeRobot class attributes and methods

# Expr class attributes and methods

# robotG_flow_While class attributes and methods

# ExprBool class attributes and methods

# robotG_flow_If class attributes and methods

# robotG_flow_Not class attributes and methods

# OpUnaire class attributes and methods

# robotG_flow_ExprBool class attributes and methods

# robotG_flow_StopProgram class attributes and methods

# robotG_robot_Move class attributes and methods
robotG_robot_Move_power: Property = Property(name="power", type=IntegerType)
robotG_robot_Move.attributes={robotG_robot_Move_power}

# CommandeRobot class attributes and methods

# robotG_robot_Bip class attributes and methods
robotG_robot_Bip_duration: Property = Property(name="duration", type=IntegerType)
robotG_robot_Bip_power: Property = Property(name="power", type=IntegerType)
robotG_robot_Bip_repeat: Property = Property(name="repeat", type=BooleanType)
robotG_robot_Bip.attributes={robotG_robot_Bip_power, robotG_robot_Bip_duration, robotG_robot_Bip_repeat}

# robotG_flow_And class attributes and methods

# OpBinaire class attributes and methods

# robotG_flow_Or class attributes and methods

# robotG_flow_Programme class attributes and methods

# robotG_flow_Expr class attributes and methods

# robotG_flow_OpUnaire class attributes and methods

# robotG_flow_OpBinaire class attributes and methods

# Relationships
condition0: BinaryAssociation = BinaryAssociation(
    name="condition0",
    ends={
        Property(name="ExprBool", type=robotG_flow_While, multiplicity=Multiplicity(1, 1)),
        Property(name="robotG_flow_While", type=ExprBool, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions1: BinaryAssociation = BinaryAssociation(
    name="instructions1",
    ends={
        Property(name="Expr", type=robotG_flow_While, multiplicity=Multiplicity(1, 1)),
        Property(name="robotG_flow_While2", type=Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition3: BinaryAssociation = BinaryAssociation(
    name="condition3",
    ends={
        Property(name="ExprBool4", type=robotG_flow_If, multiplicity=Multiplicity(1, 1)),
        Property(name="robotG_flow_If", type=ExprBool, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions5: BinaryAssociation = BinaryAssociation(
    name="instructions5",
    ends={
        Property(name="Expr7", type=robotG_flow_If, multiplicity=Multiplicity(1, 1)),
        Property(name="robotG_flow_If6", type=Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programme15: BinaryAssociation = BinaryAssociation(
    name="programme15",
    ends={
        Property(name="Expr16", type=robotG_flow_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="robotG_flow_Programme", type=Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression8: BinaryAssociation = BinaryAssociation(
    name="expression8",
    ends={
        Property(name="ExprBool9", type=robotG_flow_OpUnaire, multiplicity=Multiplicity(1, 1)),
        Property(name="robotG_flow_OpUnaire", type=ExprBool, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
filsGauche10: BinaryAssociation = BinaryAssociation(
    name="filsGauche10",
    ends={
        Property(name="ExprBool11", type=robotG_flow_OpBinaire, multiplicity=Multiplicity(1, 1)),
        Property(name="robotG_flow_OpBinaire", type=ExprBool, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
filsDroit12: BinaryAssociation = BinaryAssociation(
    name="filsDroit12",
    ends={
        Property(name="ExprBool14", type=robotG_flow_OpBinaire, multiplicity=Multiplicity(1, 1)),
        Property(name="robotG_flow_OpBinaire13", type=ExprBool, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_robotG_robot_Turn_CommandeRobot = Generalization(general=CommandeRobot, specific=robotG_robot_Turn)
gen_robotG_robot_SetTurnAngle_CommandeRobot = Generalization(general=CommandeRobot, specific=robotG_robot_SetTurnAngle)
gen_robotG_robot_HasTurned_flow_ExprBool = Generalization(general=flow_ExprBool, specific=robotG_robot_HasTurned)
gen_robotG_robot_HasTurned_robot_CommandeRobot = Generalization(general=robot_CommandeRobot, specific=robotG_robot_HasTurned)
gen_robotG_robot_Display_CommandeRobot = Generalization(general=CommandeRobot, specific=robotG_robot_Display)
gen_robotG_robot_Obstacle_flow_ExprBool = Generalization(general=flow_ExprBool, specific=robotG_robot_Obstacle)
gen_robotG_robot_Obstacle_robot_CommandeRobot = Generalization(general=robot_CommandeRobot, specific=robotG_robot_Obstacle)
gen_robotG_robot_StopEngine_CommandeRobot = Generalization(general=CommandeRobot, specific=robotG_robot_StopEngine)
gen_robotG_robot_CommandeRobot_Expr = Generalization(general=Expr, specific=robotG_robot_CommandeRobot)
gen_robotG_flow_While_Expr = Generalization(general=Expr, specific=robotG_flow_While)
gen_robotG_flow_If_Expr = Generalization(general=Expr, specific=robotG_flow_If)
gen_robotG_flow_Not_OpUnaire = Generalization(general=OpUnaire, specific=robotG_flow_Not)
gen_robotG_flow_ExprBool_Expr = Generalization(general=Expr, specific=robotG_flow_ExprBool)
gen_robotG_flow_StopProgram_Expr = Generalization(general=Expr, specific=robotG_flow_StopProgram)
gen_robotG_robot_Move_CommandeRobot = Generalization(general=CommandeRobot, specific=robotG_robot_Move)
gen_robotG_robot_Bip_CommandeRobot = Generalization(general=CommandeRobot, specific=robotG_robot_Bip)
gen_robotG_flow_And_OpBinaire = Generalization(general=OpBinaire, specific=robotG_flow_And)
gen_robotG_flow_Or_OpBinaire = Generalization(general=OpBinaire, specific=robotG_flow_Or)
gen_robotG_flow_OpUnaire_ExprBool = Generalization(general=ExprBool, specific=robotG_flow_OpUnaire)
gen_robotG_flow_OpBinaire_ExprBool = Generalization(general=ExprBool, specific=robotG_flow_OpBinaire)

# Domain Model
domain_model = DomainModel(
    name="robotG",
    types={robotG_robot_Turn, robotG_robot_SetTurnAngle, robotG_robot_HasTurned, flow_ExprBool, robot_CommandeRobot, robotG_robot_Display, robotG_robot_Obstacle, robotG_robot_StopEngine, robotG_robot_CommandeRobot, Expr, robotG_flow_While, ExprBool, robotG_flow_If, robotG_flow_Not, OpUnaire, robotG_flow_ExprBool, robotG_flow_StopProgram, robotG_robot_Move, CommandeRobot, robotG_robot_Bip, robotG_flow_And, OpBinaire, robotG_flow_Or, robotG_flow_Programme, robotG_flow_Expr, robotG_flow_OpUnaire, robotG_flow_OpBinaire},
    associations={condition0, instructions1, condition3, instructions5, programme15, expression8, filsGauche10, filsDroit12},
    generalizations={gen_robotG_robot_Turn_CommandeRobot, gen_robotG_robot_SetTurnAngle_CommandeRobot, gen_robotG_robot_HasTurned_flow_ExprBool, gen_robotG_robot_HasTurned_robot_CommandeRobot, gen_robotG_robot_Display_CommandeRobot, gen_robotG_robot_Obstacle_flow_ExprBool, gen_robotG_robot_Obstacle_robot_CommandeRobot, gen_robotG_robot_StopEngine_CommandeRobot, gen_robotG_robot_CommandeRobot_Expr, gen_robotG_flow_While_Expr, gen_robotG_flow_If_Expr, gen_robotG_flow_Not_OpUnaire, gen_robotG_flow_ExprBool_Expr, gen_robotG_flow_StopProgram_Expr, gen_robotG_robot_Move_CommandeRobot, gen_robotG_robot_Bip_CommandeRobot, gen_robotG_flow_And_OpBinaire, gen_robotG_flow_Or_OpBinaire, gen_robotG_flow_OpUnaire_ExprBool, gen_robotG_flow_OpBinaire_ExprBool},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)