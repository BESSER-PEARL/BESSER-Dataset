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
EOperator: Enumeration = Enumeration(
    name="EOperator",
    literals={
            EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="DIFF"),
			EnumerationLiteral(name="GTE"),
			EnumerationLiteral(name="LTE"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

ESensor: Enumeration = Enumeration(
    name="ESensor",
    literals={
            EnumerationLiteral(name="distanceFRF"),
			EnumerationLiteral(name="distanceFRB"),
			EnumerationLiteral(name="distanceR"),
			EnumerationLiteral(name="distanceBR"),
			EnumerationLiteral(name="distanceBL"),
			EnumerationLiteral(name="distanceL"),
			EnumerationLiteral(name="distanceFLB"),
			EnumerationLiteral(name="distanceFLF"),
			EnumerationLiteral(name="lightFRF"),
			EnumerationLiteral(name="lightFRB"),
			EnumerationLiteral(name="lightR"),
			EnumerationLiteral(name="lightBR"),
			EnumerationLiteral(name="lightBL"),
			EnumerationLiteral(name="lightL"),
			EnumerationLiteral(name="lightFLB"),
			EnumerationLiteral(name="lightFLF")
    }
)

# Classes
robot_Mission = Class(name="robot::Mission")
robot_Sequence = Class(name="robot::Sequence")
robot_Forward = Class(name="robot::Forward")
Movement = Class(name="Movement")
robot_Backward = Class(name="robot::Backward")
robot_TurnLeft = Class(name="robot::TurnLeft")
robot_TurnRight = Class(name="robot::TurnRight")
robot_Alternative = Class(name="robot::Alternative")
robot_Condition = Class(name="robot::Condition")
robot_Event = Class(name="robot::Event")
robot_Values = Class(name="robot::Values")
robot_Sensor = Class(name="robot::Sensor")
Values = Class(name="Values")
robot_TInteger = Class(name="robot::TInteger")
robot_TString = Class(name="robot::TString")
robot_TFloat = Class(name="robot::TFloat")
robot_TBoolean = Class(name="robot::TBoolean")
Operation = Class(name="Operation")
robot_Operator = Class(name="robot::Operator")
robot_Different = Class(name="robot::Different")
Operator = Class(name="Operator")
robot_Operation = Class(name="robot::Operation")
robot_Movement = Class(name="robot::Movement")
robot_Var = Class(name="robot::Var")
robot_Variable = Class(name="robot::Variable")
robot_Stop = Class(name="robot::Stop")
robot_Sleep = Class(name="robot::Sleep")
robot_Whenever = Class(name="robot::Whenever")
robot_Affectation = Class(name="robot::Affectation")
Var = Class(name="Var")
robot_Declaration = Class(name="robot::Declaration")
robot_While = Class(name="robot::While")
robot_Value = Class(name="robot::Value")
Condition = Class(name="Condition")
robot_Echo = Class(name="robot::Echo")
robot_Compare = Class(name="robot::Compare")

# robot_Mission class attributes and methods

# robot_Sequence class attributes and methods

# robot_Forward class attributes and methods

# Movement class attributes and methods

# robot_Backward class attributes and methods

# robot_TurnLeft class attributes and methods

# robot_TurnRight class attributes and methods

# robot_Alternative class attributes and methods

# robot_Condition class attributes and methods

# robot_Event class attributes and methods

# robot_Values class attributes and methods

# robot_Sensor class attributes and methods
robot_Sensor_name: Property = Property(name="name", type=StringType)
robot_Sensor.attributes={robot_Sensor_name}

# Values class attributes and methods

# robot_TInteger class attributes and methods
robot_TInteger_Value: Property = Property(name="Value", type=StringType)
robot_TInteger.attributes={robot_TInteger_Value}

# robot_TString class attributes and methods
robot_TString_Value: Property = Property(name="Value", type=StringType)
robot_TString.attributes={robot_TString_Value}

# robot_TFloat class attributes and methods
robot_TFloat_Value: Property = Property(name="Value", type=StringType)
robot_TFloat.attributes={robot_TFloat_Value}

# robot_TBoolean class attributes and methods
robot_TBoolean_Value: Property = Property(name="Value", type=StringType)
robot_TBoolean.attributes={robot_TBoolean_Value}

# Operation class attributes and methods

# robot_Operator class attributes and methods
robot_Operator_type: Property = Property(name="type", type=StringType)
robot_Operator.attributes={robot_Operator_type}

# robot_Different class attributes and methods

# Operator class attributes and methods

# robot_Operation class attributes and methods

# robot_Movement class attributes and methods
robot_Movement_duration: Property = Property(name="duration", type=FloatType)
robot_Movement.attributes={robot_Movement_duration}

# robot_Var class attributes and methods
robot_Var_Name: Property = Property(name="Name", type=StringType)
robot_Var.attributes={robot_Var_Name}

# robot_Variable class attributes and methods
robot_Variable_Name: Property = Property(name="Name", type=StringType)
robot_Variable.attributes={robot_Variable_Name}

# robot_Stop class attributes and methods

# robot_Sleep class attributes and methods

# robot_Whenever class attributes and methods

# robot_Affectation class attributes and methods

# Var class attributes and methods

# robot_Declaration class attributes and methods

# robot_While class attributes and methods

# robot_Value class attributes and methods

# Condition class attributes and methods

# robot_Echo class attributes and methods
robot_Echo_param: Property = Property(name="param", type=StringType)
robot_Echo.attributes={robot_Echo_param}

# robot_Compare class attributes and methods

# Relationships
Sequence0: BinaryAssociation = BinaryAssociation(
    name="Sequence0",
    ends={
        Property(name="robot_Sequence", type=robot_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Mission", type=robot_Sequence, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Consequence3: BinaryAssociation = BinaryAssociation(
    name="Consequence3",
    ends={
        Property(name="robot_Operation4", type=robot_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Alternative", type=robot_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Alternative5: BinaryAssociation = BinaryAssociation(
    name="Alternative5",
    ends={
        Property(name="robot_Operation7", type=robot_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Alternative6", type=robot_Operation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Condition8: BinaryAssociation = BinaryAssociation(
    name="Condition8",
    ends={
        Property(name="robot_Condition", type=robot_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Alternative9", type=robot_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
At10: BinaryAssociation = BinaryAssociation(
    name="At10",
    ends={
        Property(name="robot_Operation11", type=robot_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Event", type=robot_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Onleave12: BinaryAssociation = BinaryAssociation(
    name="Onleave12",
    ends={
        Property(name="robot_Operation14", type=robot_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Event13", type=robot_Operation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Condition15: BinaryAssociation = BinaryAssociation(
    name="Condition15",
    ends={
        Property(name="robot_Condition17", type=robot_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Event16", type=robot_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Operations1: BinaryAssociation = BinaryAssociation(
    name="Operations1",
    ends={
        Property(name="robot_Operation", type=robot_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Sequence2", type=robot_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Value18: BinaryAssociation = BinaryAssociation(
    name="Value18",
    ends={
        Property(name="robot_Values", type=robot_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Var", type=robot_Values, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Condition19: BinaryAssociation = BinaryAssociation(
    name="Condition19",
    ends={
        Property(name="robot_Condition20", type=robot_Whenever, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Whenever", type=robot_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Whenever21: BinaryAssociation = BinaryAssociation(
    name="Whenever21",
    ends={
        Property(name="robot_Operation23", type=robot_Whenever, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Whenever22", type=robot_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Else24: BinaryAssociation = BinaryAssociation(
    name="Else24",
    ends={
        Property(name="robot_Operation26", type=robot_Whenever, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Whenever25", type=robot_Operation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Operation27: BinaryAssociation = BinaryAssociation(
    name="Operation27",
    ends={
        Property(name="robot_Operation28", type=robot_While, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_While", type=robot_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Condition29: BinaryAssociation = BinaryAssociation(
    name="Condition29",
    ends={
        Property(name="robot_Condition31", type=robot_While, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_While30", type=robot_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Variable32: BinaryAssociation = BinaryAssociation(
    name="Variable32",
    ends={
        Property(name="robot_Values33", type=robot_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Value", type=robot_Values, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Operator34: BinaryAssociation = BinaryAssociation(
    name="Operator34",
    ends={
        Property(name="robot_Operator", type=robot_Compare, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Compare", type=robot_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Condition235: BinaryAssociation = BinaryAssociation(
    name="Condition235",
    ends={
        Property(name="robot_Condition37", type=robot_Compare, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Compare36", type=robot_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Condition138: BinaryAssociation = BinaryAssociation(
    name="Condition138",
    ends={
        Property(name="robot_Condition40", type=robot_Compare, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Compare39", type=robot_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_robot_Forward_Movement = Generalization(general=Movement, specific=robot_Forward)
gen_robot_Backward_Movement = Generalization(general=Movement, specific=robot_Backward)
gen_robot_TurnLeft_Movement = Generalization(general=Movement, specific=robot_TurnLeft)
gen_robot_TurnRight_Movement = Generalization(general=Movement, specific=robot_TurnRight)
gen_robot_Alternative_Operation = Generalization(general=Operation, specific=robot_Alternative)
gen_robot_Event_Operation = Generalization(general=Operation, specific=robot_Event)
gen_robot_Sensor_Values = Generalization(general=Values, specific=robot_Sensor)
gen_robot_TInteger_Values = Generalization(general=Values, specific=robot_TInteger)
gen_robot_TString_Values = Generalization(general=Values, specific=robot_TString)
gen_robot_TFloat_Values = Generalization(general=Values, specific=robot_TFloat)
gen_robot_TBoolean_Values = Generalization(general=Values, specific=robot_TBoolean)
gen_robot_Sequence_Operation = Generalization(general=Operation, specific=robot_Sequence)
gen_robot_Different_Operator = Generalization(general=Operator, specific=robot_Different)
gen_robot_Movement_Operation = Generalization(general=Operation, specific=robot_Movement)
gen_robot_Var_Operation = Generalization(general=Operation, specific=robot_Var)
gen_robot_Variable_Values = Generalization(general=Values, specific=robot_Variable)
gen_robot_Stop_Movement = Generalization(general=Movement, specific=robot_Stop)
gen_robot_Sleep_Movement = Generalization(general=Movement, specific=robot_Sleep)
gen_robot_Whenever_Operation = Generalization(general=Operation, specific=robot_Whenever)
gen_robot_Affectation_Var = Generalization(general=Var, specific=robot_Affectation)
gen_robot_Declaration_Var = Generalization(general=Var, specific=robot_Declaration)
gen_robot_While_Operation = Generalization(general=Operation, specific=robot_While)
gen_robot_Value_Condition = Generalization(general=Condition, specific=robot_Value)
gen_robot_Echo_Operation = Generalization(general=Operation, specific=robot_Echo)
gen_robot_Compare_Condition = Generalization(general=Condition, specific=robot_Compare)

# Domain Model
domain_model = DomainModel(
    name="robot",
    types={robot_Mission, robot_Sequence, robot_Forward, Movement, robot_Backward, robot_TurnLeft, robot_TurnRight, robot_Alternative, robot_Condition, robot_Event, robot_Values, robot_Sensor, Values, robot_TInteger, robot_TString, robot_TFloat, robot_TBoolean, Operation, robot_Operator, robot_Different, Operator, robot_Operation, robot_Movement, robot_Var, robot_Variable, robot_Stop, robot_Sleep, robot_Whenever, robot_Affectation, Var, robot_Declaration, robot_While, robot_Value, Condition, robot_Echo, robot_Compare, EOperator, ESensor},
    associations={Sequence0, Consequence3, Alternative5, Condition8, At10, Onleave12, Condition15, Operations1, Value18, Condition19, Whenever21, Else24, Operation27, Condition29, Variable32, Operator34, Condition235, Condition138},
    generalizations={gen_robot_Forward_Movement, gen_robot_Backward_Movement, gen_robot_TurnLeft_Movement, gen_robot_TurnRight_Movement, gen_robot_Alternative_Operation, gen_robot_Event_Operation, gen_robot_Sensor_Values, gen_robot_TInteger_Values, gen_robot_TString_Values, gen_robot_TFloat_Values, gen_robot_TBoolean_Values, gen_robot_Sequence_Operation, gen_robot_Different_Operator, gen_robot_Movement_Operation, gen_robot_Var_Operation, gen_robot_Variable_Values, gen_robot_Stop_Movement, gen_robot_Sleep_Movement, gen_robot_Whenever_Operation, gen_robot_Affectation_Var, gen_robot_Declaration_Var, gen_robot_While_Operation, gen_robot_Value_Condition, gen_robot_Echo_Operation, gen_robot_Compare_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)