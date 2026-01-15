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
robot_HasTurned = Class(name="robot::HasTurned")
robot_And = Class(name="robot::And")
robot_Program = Class(name="robot::Program")
robot_Instruction = Class(name="robot::Instruction", is_abstract=True)
robot_Bip = Class(name="robot::Bip")
Instruction = Class(name="Instruction")
robot_SetTurnAngle = Class(name="robot::SetTurnAngle")
robot_Turn = Class(name="robot::Turn")
robot_Move = Class(name="robot::Move")
robot_StopEngine = Class(name="robot::StopEngine")
robot_StopProgram = Class(name="robot::StopProgram")
robot_Obstacle = Class(name="robot::Obstacle")
ExpBool = Class(name="ExpBool")
robot_While = Class(name="robot::While")
robot_ExpBool = Class(name="robot::ExpBool", is_abstract=True)
robot_Not = Class(name="robot::Not")
robot_If = Class(name="robot::If")

# robot_HasTurned class attributes and methods

# robot_And class attributes and methods

# robot_Program class attributes and methods

# robot_Instruction class attributes and methods

# robot_Bip class attributes and methods

# Instruction class attributes and methods

# robot_SetTurnAngle class attributes and methods

# robot_Turn class attributes and methods

# robot_Move class attributes and methods

# robot_StopEngine class attributes and methods

# robot_StopProgram class attributes and methods

# robot_Obstacle class attributes and methods

# ExpBool class attributes and methods

# robot_While class attributes and methods

# robot_ExpBool class attributes and methods

# robot_Not class attributes and methods

# robot_If class attributes and methods

# Relationships
expbool7: BinaryAssociation = BinaryAssociation(
    name="expbool7",
    ends={
        Property(name="robot_ExpBool8", type=robot_If, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_If", type=robot_ExpBool, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
instruction9: BinaryAssociation = BinaryAssociation(
    name="instruction9",
    ends={
        Property(name="robot_Instruction11", type=robot_If, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_If10", type=robot_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instruction0: BinaryAssociation = BinaryAssociation(
    name="instruction0",
    ends={
        Property(name="robot_Instruction", type=robot_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Program", type=robot_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expbool1: BinaryAssociation = BinaryAssociation(
    name="expbool1",
    ends={
        Property(name="robot_ExpBool", type=robot_While, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_While", type=robot_ExpBool, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
instruction2: BinaryAssociation = BinaryAssociation(
    name="instruction2",
    ends={
        Property(name="robot_Instruction4", type=robot_While, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_While3", type=robot_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expbool5: BinaryAssociation = BinaryAssociation(
    name="expbool5",
    ends={
        Property(name="robot_ExpBool6", type=robot_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Not", type=robot_ExpBool, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
left12: BinaryAssociation = BinaryAssociation(
    name="left12",
    ends={
        Property(name="robot_ExpBool13", type=robot_And, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_And", type=robot_ExpBool, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
right14: BinaryAssociation = BinaryAssociation(
    name="right14",
    ends={
        Property(name="robot_ExpBool16", type=robot_And, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_And15", type=robot_ExpBool, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_robot_HasTurned_ExpBool = Generalization(general=ExpBool, specific=robot_HasTurned)
gen_robot_And_ExpBool = Generalization(general=ExpBool, specific=robot_And)
gen_robot_Bip_Instruction = Generalization(general=Instruction, specific=robot_Bip)
gen_robot_SetTurnAngle_Instruction = Generalization(general=Instruction, specific=robot_SetTurnAngle)
gen_robot_Turn_Instruction = Generalization(general=Instruction, specific=robot_Turn)
gen_robot_Move_Instruction = Generalization(general=Instruction, specific=robot_Move)
gen_robot_StopEngine_Instruction = Generalization(general=Instruction, specific=robot_StopEngine)
gen_robot_StopProgram_Instruction = Generalization(general=Instruction, specific=robot_StopProgram)
gen_robot_Obstacle_ExpBool = Generalization(general=ExpBool, specific=robot_Obstacle)
gen_robot_While_ExpBool = Generalization(general=ExpBool, specific=robot_While)
gen_robot_Not_ExpBool = Generalization(general=ExpBool, specific=robot_Not)
gen_robot_If_ExpBool = Generalization(general=ExpBool, specific=robot_If)

# Domain Model
domain_model = DomainModel(
    name="robot",
    types={robot_HasTurned, robot_And, robot_Program, robot_Instruction, robot_Bip, Instruction, robot_SetTurnAngle, robot_Turn, robot_Move, robot_StopEngine, robot_StopProgram, robot_Obstacle, ExpBool, robot_While, robot_ExpBool, robot_Not, robot_If},
    associations={expbool7, instruction9, instruction0, expbool1, instruction2, expbool5, left12, right14},
    generalizations={gen_robot_HasTurned_ExpBool, gen_robot_And_ExpBool, gen_robot_Bip_Instruction, gen_robot_SetTurnAngle_Instruction, gen_robot_Turn_Instruction, gen_robot_Move_Instruction, gen_robot_StopEngine_Instruction, gen_robot_StopProgram_Instruction, gen_robot_Obstacle_ExpBool, gen_robot_While_ExpBool, gen_robot_Not_ExpBool, gen_robot_If_ExpBool},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)