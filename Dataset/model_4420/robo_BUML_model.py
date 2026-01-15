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
MotorPort: Enumeration = Enumeration(
    name="MotorPort",
    literals={
            EnumerationLiteral(name="A"),
			EnumerationLiteral(name="B"),
			EnumerationLiteral(name="C"),
			EnumerationLiteral(name="D")
    }
)

MotorType: Enumeration = Enumeration(
    name="MotorType",
    literals={
            EnumerationLiteral(name="LARGE"),
			EnumerationLiteral(name="MEDIUM")
    }
)

SensorPort: Enumeration = Enumeration(
    name="SensorPort",
    literals={
            EnumerationLiteral(name="S1"),
			EnumerationLiteral(name="S2"),
			EnumerationLiteral(name="S3"),
			EnumerationLiteral(name="S4")
    }
)

SensorType: Enumeration = Enumeration(
    name="SensorType",
    literals={
            EnumerationLiteral(name="COLOR")
    }
)

SensorMode: Enumeration = Enumeration(
    name="SensorMode",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="AMBIENT"),
			EnumerationLiteral(name="COLOR_ID")
    }
)

Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="FORWARD"),
			EnumerationLiteral(name="BACKWARD"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

ExprOperation: Enumeration = Enumeration(
    name="ExprOperation",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="MULTIPLY"),
			EnumerationLiteral(name="DIVIDE")
    }
)

ComparisonOperator: Enumeration = Enumeration(
    name="ComparisonOperator",
    literals={
            EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="LESS_OR_EQUAL"),
			EnumerationLiteral(name="GREATER_OR_EQUAL"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="UNEQUAL")
    }
)

# Classes
robo_Robot = Class(name="robo::Robot")
robo_Program = Class(name="robo::Program")
robo_Setup = Class(name="robo::Setup")
robo_Motor = Class(name="robo::Motor")
robo_Sensor = Class(name="robo::Sensor")
Command = Class(name="Command")
robo_command_Command = Class(name="robo::command::Command", is_abstract=True)
robo_command_Drive = Class(name="robo::command::Drive")
Expr = Class(name="Expr")
Condition = Class(name="Condition")
robo_command_Loop = Class(name="robo::command::Loop")
robo_command_Branch = Class(name="robo::command::Branch")
robo_command_Assignment = Class(name="robo::command::Assignment")
robo_expression_Expr = Class(name="robo::expression::Expr", is_abstract=True)
robo_expression_Variable = Class(name="robo::expression::Variable")
robo_expression_Operation = Class(name="robo::expression::Operation")
robo_expression_Literal = Class(name="robo::expression::Literal")
robo_condition_Condition = Class(name="robo::condition::Condition", is_abstract=True)
robo_condition_Comparison = Class(name="robo::condition::Comparison")

# robo_Robot class attributes and methods

# robo_Program class attributes and methods
robo_Program_name: Property = Property(name="name", type=StringType)
robo_Program.attributes={robo_Program_name}

# robo_Setup class attributes and methods

# robo_Motor class attributes and methods
robo_Motor_port: Property = Property(name="port", type=StringType)
robo_Motor_type: Property = Property(name="type", type=StringType)
robo_Motor_speed: Property = Property(name="speed", type=FloatType)
robo_Motor_reversed: Property = Property(name="reversed", type=BooleanType)
robo_Motor.attributes={robo_Motor_type, robo_Motor_speed, robo_Motor_port, robo_Motor_reversed}

# robo_Sensor class attributes and methods
robo_Sensor_port: Property = Property(name="port", type=StringType)
robo_Sensor_type: Property = Property(name="type", type=StringType)
robo_Sensor_mode: Property = Property(name="mode", type=StringType)
robo_Sensor_name: Property = Property(name="name", type=StringType)
robo_Sensor.attributes={robo_Sensor_mode, robo_Sensor_type, robo_Sensor_port, robo_Sensor_name}

# Command class attributes and methods

# robo_command_Command class attributes and methods

# robo_command_Drive class attributes and methods
robo_command_Drive_direction: Property = Property(name="direction", type=StringType)
robo_command_Drive.attributes={robo_command_Drive_direction}

# Expr class attributes and methods

# Condition class attributes and methods

# robo_command_Loop class attributes and methods

# robo_command_Branch class attributes and methods

# robo_command_Assignment class attributes and methods
robo_command_Assignment_variable: Property = Property(name="variable", type=StringType)
robo_command_Assignment.attributes={robo_command_Assignment_variable}

# robo_expression_Expr class attributes and methods
robo_expression_Expr_m_evaluate: Method = Method(name="evaluate", parameters={}, type=FloatType)
robo_expression_Expr.methods={robo_expression_Expr_m_evaluate}

# robo_expression_Variable class attributes and methods
robo_expression_Variable_name: Property = Property(name="name", type=StringType)
robo_expression_Variable.attributes={robo_expression_Variable_name}

# robo_expression_Operation class attributes and methods
robo_expression_Operation_operator: Property = Property(name="operator", type=StringType)
robo_expression_Operation.attributes={robo_expression_Operation_operator}

# robo_expression_Literal class attributes and methods
robo_expression_Literal_value: Property = Property(name="value", type=FloatType)
robo_expression_Literal.attributes={robo_expression_Literal_value}

# robo_condition_Condition class attributes and methods
robo_condition_Condition_m_evaluate: Method = Method(name="evaluate", parameters={}, type=BooleanType)
robo_condition_Condition.methods={robo_condition_Condition_m_evaluate}

# robo_condition_Comparison class attributes and methods
robo_condition_Comparison_operator: Property = Property(name="operator", type=StringType)
robo_condition_Comparison.attributes={robo_condition_Comparison_operator}

# Relationships
programms0: BinaryAssociation = BinaryAssociation(
    name="programms0",
    ends={
        Property(name="robo_Program", type=robo_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_Robot", type=robo_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setup1: BinaryAssociation = BinaryAssociation(
    name="setup1",
    ends={
        Property(name="robo_Setup", type=robo_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_Robot2", type=robo_Setup, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftMotor3: BinaryAssociation = BinaryAssociation(
    name="leftMotor3",
    ends={
        Property(name="robo_Motor", type=robo_Setup, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_Setup4", type=robo_Motor, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightMotor5: BinaryAssociation = BinaryAssociation(
    name="rightMotor5",
    ends={
        Property(name="robo_Motor7", type=robo_Setup, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_Setup6", type=robo_Motor, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sensors8: BinaryAssociation = BinaryAssociation(
    name="sensors8",
    ends={
        Property(name="robo_Sensor", type=robo_Setup, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_Setup9", type=robo_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands10: BinaryAssociation = BinaryAssociation(
    name="commands10",
    ends={
        Property(name="Command", type=robo_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_Program11", type=Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
distance12: BinaryAssociation = BinaryAssociation(
    name="distance12",
    ends={
        Property(name="Expr", type=robo_command_Drive, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_command_Drive", type=Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
until13: BinaryAssociation = BinaryAssociation(
    name="until13",
    ends={
        Property(name="Condition", type=robo_command_Drive, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_command_Drive14", type=Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="Condition16", type=robo_command_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_command_Loop", type=Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
commands17: BinaryAssociation = BinaryAssociation(
    name="commands17",
    ends={
        Property(name="Command19", type=robo_command_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_command_Loop18", type=Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition20: BinaryAssociation = BinaryAssociation(
    name="condition20",
    ends={
        Property(name="Condition21", type=robo_command_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_command_Branch", type=Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
commands22: BinaryAssociation = BinaryAssociation(
    name="commands22",
    ends={
        Property(name="Command24", type=robo_command_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_command_Branch23", type=Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value25: BinaryAssociation = BinaryAssociation(
    name="value25",
    ends={
        Property(name="Expr26", type=robo_command_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_command_Assignment", type=Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left27: BinaryAssociation = BinaryAssociation(
    name="left27",
    ends={
        Property(name="Expr28", type=robo_expression_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_expression_Operation", type=Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right29: BinaryAssociation = BinaryAssociation(
    name="right29",
    ends={
        Property(name="Expr31", type=robo_expression_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_expression_Operation30", type=Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left32: BinaryAssociation = BinaryAssociation(
    name="left32",
    ends={
        Property(name="Expr33", type=robo_condition_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_condition_Comparison", type=Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right34: BinaryAssociation = BinaryAssociation(
    name="right34",
    ends={
        Property(name="Expr36", type=robo_condition_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="robo_condition_Comparison35", type=Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_robo_command_Drive_Command = Generalization(general=Command, specific=robo_command_Drive)
gen_robo_command_Loop_Command = Generalization(general=Command, specific=robo_command_Loop)
gen_robo_command_Branch_Command = Generalization(general=Command, specific=robo_command_Branch)
gen_robo_command_Assignment_Command = Generalization(general=Command, specific=robo_command_Assignment)
gen_robo_expression_Variable_Expr = Generalization(general=Expr, specific=robo_expression_Variable)
gen_robo_expression_Operation_Expr = Generalization(general=Expr, specific=robo_expression_Operation)
gen_robo_expression_Literal_Expr = Generalization(general=Expr, specific=robo_expression_Literal)
gen_robo_condition_Comparison_Condition = Generalization(general=Condition, specific=robo_condition_Comparison)

# Domain Model
domain_model = DomainModel(
    name="robo",
    types={robo_Robot, robo_Program, robo_Setup, robo_Motor, robo_Sensor, Command, robo_command_Command, robo_command_Drive, Expr, Condition, robo_command_Loop, robo_command_Branch, robo_command_Assignment, robo_expression_Expr, robo_expression_Variable, robo_expression_Operation, robo_expression_Literal, robo_condition_Condition, robo_condition_Comparison, MotorPort, MotorType, SensorPort, SensorType, SensorMode, Direction, ExprOperation, ComparisonOperator},
    associations={programms0, setup1, leftMotor3, rightMotor5, sensors8, commands10, distance12, until13, condition15, commands17, condition20, commands22, value25, left27, right29, left32, right34},
    generalizations={gen_robo_command_Drive_Command, gen_robo_command_Loop_Command, gen_robo_command_Branch_Command, gen_robo_command_Assignment_Command, gen_robo_expression_Variable_Expr, gen_robo_expression_Operation_Expr, gen_robo_expression_Literal_Expr, gen_robo_condition_Comparison_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)