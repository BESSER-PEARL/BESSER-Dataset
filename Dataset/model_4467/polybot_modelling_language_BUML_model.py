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
polybot_modelling_language_Robot = Class(name="polybot::modelling::language::Robot")
polybot_modelling_language_MoveStraight = Class(name="polybot::modelling::language::MoveStraight")
Instruction = Class(name="Instruction")
polybot_modelling_language_TurnRight = Class(name="polybot::modelling::language::TurnRight")
Turn = Class(name="Turn")
polybot_modelling_language_Instruction = Class(name="polybot::modelling::language::Instruction", is_abstract=True)
polybot_modelling_language_Scene = Class(name="polybot::modelling::language::Scene")
polybot_modelling_language_Release = Class(name="polybot::modelling::language::Release")
polybot_modelling_language_Catch = Class(name="polybot::modelling::language::Catch")
polybot_modelling_language_TurnLeft = Class(name="polybot::modelling::language::TurnLeft")
polybot_modelling_language_Turn = Class(name="polybot::modelling::language::Turn", is_abstract=True)
polybot_modelling_language_ComeHome = Class(name="polybot::modelling::language::ComeHome")

# polybot_modelling_language_Robot class attributes and methods
polybot_modelling_language_Robot_debug: Property = Property(name="debug", type=BooleanType)
polybot_modelling_language_Robot.attributes={polybot_modelling_language_Robot_debug}

# polybot_modelling_language_MoveStraight class attributes and methods
polybot_modelling_language_MoveStraight_distance: Property = Property(name="distance", type=IntegerType)
polybot_modelling_language_MoveStraight.attributes={polybot_modelling_language_MoveStraight_distance}

# Instruction class attributes and methods

# polybot_modelling_language_TurnRight class attributes and methods

# Turn class attributes and methods

# polybot_modelling_language_Instruction class attributes and methods
polybot_modelling_language_Instruction_nextInstructionTrue: Property = Property(name="nextInstructionTrue", type=StringType)
polybot_modelling_language_Instruction_nextInstructionFalse: Property = Property(name="nextInstructionFalse", type=StringType)
polybot_modelling_language_Instruction_name: Property = Property(name="name", type=StringType)
polybot_modelling_language_Instruction_nextInstruction: Property = Property(name="nextInstruction", type=StringType)
polybot_modelling_language_Instruction.attributes={polybot_modelling_language_Instruction_nextInstructionFalse, polybot_modelling_language_Instruction_nextInstruction, polybot_modelling_language_Instruction_name, polybot_modelling_language_Instruction_nextInstructionTrue}

# polybot_modelling_language_Scene class attributes and methods

# polybot_modelling_language_Release class attributes and methods

# polybot_modelling_language_Catch class attributes and methods

# polybot_modelling_language_TurnLeft class attributes and methods

# polybot_modelling_language_Turn class attributes and methods
polybot_modelling_language_Turn_angle: Property = Property(name="angle", type=IntegerType)
polybot_modelling_language_Turn.attributes={polybot_modelling_language_Turn_angle}

# polybot_modelling_language_ComeHome class attributes and methods

# Relationships
robot0: BinaryAssociation = BinaryAssociation(
    name="robot0",
    ends={
        Property(name="polybot_modelling_language_Robot", type=polybot_modelling_language_Scene, multiplicity=Multiplicity(1, 1)),
        Property(name="polybot_modelling_language_Scene", type=polybot_modelling_language_Robot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions1: BinaryAssociation = BinaryAssociation(
    name="instructions1",
    ends={
        Property(name="polybot_modelling_language_Instruction", type=polybot_modelling_language_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="polybot_modelling_language_Robot2", type=polybot_modelling_language_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_polybot_modelling_language_MoveStraight_Instruction = Generalization(general=Instruction, specific=polybot_modelling_language_MoveStraight)
gen_polybot_modelling_language_TurnRight_Turn = Generalization(general=Turn, specific=polybot_modelling_language_TurnRight)
gen_polybot_modelling_language_Release_Instruction = Generalization(general=Instruction, specific=polybot_modelling_language_Release)
gen_polybot_modelling_language_Catch_Instruction = Generalization(general=Instruction, specific=polybot_modelling_language_Catch)
gen_polybot_modelling_language_TurnLeft_Turn = Generalization(general=Turn, specific=polybot_modelling_language_TurnLeft)
gen_polybot_modelling_language_Turn_Instruction = Generalization(general=Instruction, specific=polybot_modelling_language_Turn)
gen_polybot_modelling_language_ComeHome_Instruction = Generalization(general=Instruction, specific=polybot_modelling_language_ComeHome)

# Domain Model
domain_model = DomainModel(
    name="polybot_modelling_language",
    types={polybot_modelling_language_Robot, polybot_modelling_language_MoveStraight, Instruction, polybot_modelling_language_TurnRight, Turn, polybot_modelling_language_Instruction, polybot_modelling_language_Scene, polybot_modelling_language_Release, polybot_modelling_language_Catch, polybot_modelling_language_TurnLeft, polybot_modelling_language_Turn, polybot_modelling_language_ComeHome},
    associations={robot0, instructions1},
    generalizations={gen_polybot_modelling_language_MoveStraight_Instruction, gen_polybot_modelling_language_TurnRight_Turn, gen_polybot_modelling_language_Release_Instruction, gen_polybot_modelling_language_Catch_Instruction, gen_polybot_modelling_language_TurnLeft_Turn, gen_polybot_modelling_language_Turn_Instruction, gen_polybot_modelling_language_ComeHome_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)