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
ExpMember = Class(name="ExpMember")
pycom_Condition = Class(name="pycom_Condition")
pycom_System = Class(name="pycom_System")
pycom_ExpMember = Class(name="pycom_ExpMember")
pycom_Board = Class(name="pycom_Board")
pycom_Sensor = Class(name="pycom_Sensor")
BoardMember = Class(name="BoardMember")
pycom_ModuleType = Class(name="pycom_ModuleType")
pycom_Server = Class(name="pycom_Server")
pycom_Actuator = Class(name="pycom_Actuator")
pycom_Connection = Class(name="pycom_Connection")
pycom_Communication = Class(name="pycom_Communication")
pycom_ConditionalAction = Class(name="pycom_ConditionalAction")
pycom_Host = Class(name="pycom_Host")
pycom_BoardMember = Class(name="pycom_BoardMember")
pycom_LogicExp = Class(name="pycom_LogicExp")
pycom_Boolean = Class(name="pycom_Boolean")
pycom_ComparisonExp = Class(name="pycom_ComparisonExp")
pycom_Expression = Class(name="pycom_Expression")
pycom_Function = Class(name="pycom_Function")
pycom_Pin = Class(name="pycom_Pin")
pycom_PinName = Class(name="pycom_PinName")
pycom_ActuatorType = Class(name="pycom_ActuatorType")
ModuleType = Class(name="ModuleType")
pycom_SensorType = Class(name="pycom_SensorType")
pycom_FunctionName = Class(name="pycom_FunctionName")
pycom_ModuleFunction = Class(name="pycom_ModuleFunction")
Function = Class(name="Function")

# ExpMember class attributes and methods

# pycom_Condition class attributes and methods
pycom_Condition_operator: Property = Property(name="operator", type=StringType)
pycom_Condition.attributes={pycom_Condition_operator}

# pycom_System class attributes and methods

# pycom_ExpMember class attributes and methods

# pycom_Board class attributes and methods
pycom_Board_name: Property = Property(name="name", type=StringType)
pycom_Board.attributes={pycom_Board_name}

# pycom_Sensor class attributes and methods

# BoardMember class attributes and methods

# pycom_ModuleType class attributes and methods
pycom_ModuleType_typeName: Property = Property(name="typeName", type=StringType)
pycom_ModuleType_name: Property = Property(name="name", type=StringType)
pycom_ModuleType.attributes={pycom_ModuleType_name, pycom_ModuleType_typeName}

# pycom_Server class attributes and methods
pycom_Server_name: Property = Property(name="name", type=StringType)
pycom_Server.attributes={pycom_Server_name}

# pycom_Actuator class attributes and methods

# pycom_Connection class attributes and methods
pycom_Connection_portnumber: Property = Property(name="portnumber", type=StringType)
pycom_Connection.attributes={pycom_Connection_portnumber}

# pycom_Communication class attributes and methods
pycom_Communication_type: Property = Property(name="type", type=StringType)
pycom_Communication.attributes={pycom_Communication_type}

# pycom_ConditionalAction class attributes and methods
pycom_ConditionalAction_type: Property = Property(name="type", type=StringType)
pycom_ConditionalAction.attributes={pycom_ConditionalAction_type}

# pycom_Host class attributes and methods
pycom_Host_ipAdr: Property = Property(name="ipAdr", type=StringType)
pycom_Host_website: Property = Property(name="website", type=StringType)
pycom_Host.attributes={pycom_Host_ipAdr, pycom_Host_website}

# pycom_BoardMember class attributes and methods

# pycom_LogicExp class attributes and methods

# pycom_Boolean class attributes and methods
pycom_Boolean_value: Property = Property(name="value", type=StringType)
pycom_Boolean.attributes={pycom_Boolean_value}

# pycom_ComparisonExp class attributes and methods
pycom_ComparisonExp_op: Property = Property(name="op", type=StringType)
pycom_ComparisonExp.attributes={pycom_ComparisonExp_op}

# pycom_Expression class attributes and methods
pycom_Expression_outputValue: Property = Property(name="outputValue", type=IntegerType)
pycom_Expression.attributes={pycom_Expression_outputValue}

# pycom_Function class attributes and methods

# pycom_Pin class attributes and methods

# pycom_PinName class attributes and methods
pycom_PinName_name: Property = Property(name="name", type=StringType)
pycom_PinName.attributes={pycom_PinName_name}

# pycom_ActuatorType class attributes and methods

# ModuleType class attributes and methods

# pycom_SensorType class attributes and methods

# pycom_FunctionName class attributes and methods
pycom_FunctionName_name: Property = Property(name="name", type=StringType)
pycom_FunctionName.attributes={pycom_FunctionName_name}

# pycom_ModuleFunction class attributes and methods

# Function class attributes and methods

# Relationships
condition11: BinaryAssociation = BinaryAssociation(
    name="condition11",
    ends={
        Property(name="pycom_Condition", type=pycom_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_ConditionalAction12", type=pycom_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpMembers13: BinaryAssociation = BinaryAssociation(
    name="ExpMembers13",
    ends={
        Property(name="pycom_ExpMember", type=pycom_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_ConditionalAction14", type=pycom_ExpMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boards0: BinaryAssociation = BinaryAssociation(
    name="boards0",
    ends={
        Property(name="pycom_Board", type=pycom_System, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_System", type=pycom_Board, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensorTypes15: BinaryAssociation = BinaryAssociation(
    name="sensorTypes15",
    ends={
        Property(name="pycom_ModuleType", type=pycom_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Sensor", type=pycom_ModuleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
servers1: BinaryAssociation = BinaryAssociation(
    name="servers1",
    ends={
        Property(name="pycom_Server", type=pycom_System, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_System2", type=pycom_Server, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actuatorTypes16: BinaryAssociation = BinaryAssociation(
    name="actuatorTypes16",
    ends={
        Property(name="pycom_ModuleType17", type=pycom_Actuator, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Actuator", type=pycom_ModuleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conn3: BinaryAssociation = BinaryAssociation(
    name="conn3",
    ends={
        Property(name="pycom_Connection", type=pycom_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Server4", type=pycom_Connection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exps5: BinaryAssociation = BinaryAssociation(
    name="exps5",
    ends={
        Property(name="pycom_ConditionalAction", type=pycom_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Server6", type=pycom_ConditionalAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
host7: BinaryAssociation = BinaryAssociation(
    name="host7",
    ends={
        Property(name="pycom_Host", type=pycom_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Connection8", type=pycom_Host, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boardMembers9: BinaryAssociation = BinaryAssociation(
    name="boardMembers9",
    ends={
        Property(name="pycom_BoardMember", type=pycom_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Board10", type=pycom_BoardMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicEx25: BinaryAssociation = BinaryAssociation(
    name="logicEx25",
    ends={
        Property(name="pycom_LogicExp", type=pycom_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Condition26", type=pycom_LogicExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedCondition28: BinaryAssociation = BinaryAssociation(
    name="nestedCondition28",
    ends={
        Property(name="pycom_Condition29", type=pycom_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Condition27", type=pycom_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boolVal30: BinaryAssociation = BinaryAssociation(
    name="boolVal30",
    ends={
        Property(name="pycom_Boolean", type=pycom_LogicExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_LogicExp31", type=pycom_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compExp32: BinaryAssociation = BinaryAssociation(
    name="compExp32",
    ends={
        Property(name="pycom_ComparisonExp", type=pycom_LogicExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_LogicExp33", type=pycom_ComparisonExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left34: BinaryAssociation = BinaryAssociation(
    name="left34",
    ends={
        Property(name="pycom_Expression", type=pycom_ComparisonExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_ComparisonExp35", type=pycom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right36: BinaryAssociation = BinaryAssociation(
    name="right36",
    ends={
        Property(name="pycom_Expression38", type=pycom_ComparisonExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_ComparisonExp37", type=pycom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pins18: BinaryAssociation = BinaryAssociation(
    name="pins18",
    ends={
        Property(name="pycom_Pin", type=pycom_ModuleType, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_ModuleType19", type=pycom_Pin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
power20: BinaryAssociation = BinaryAssociation(
    name="power20",
    ends={
        Property(name="pycom_PinName", type=pycom_Pin, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Pin21", type=pycom_PinName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input22: BinaryAssociation = BinaryAssociation(
    name="input22",
    ends={
        Property(name="pycom_PinName24", type=pycom_Pin, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Pin23", type=pycom_PinName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputfunction39: BinaryAssociation = BinaryAssociation(
    name="outputfunction39",
    ends={
        Property(name="pycom_Function", type=pycom_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Expression40", type=pycom_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
board41: BinaryAssociation = BinaryAssociation(
    name="board41",
    ends={
        Property(name="pycom_Board43", type=pycom_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Function42", type=pycom_Board, multiplicity=Multiplicity(0, 1))
    }
)
functionName44: BinaryAssociation = BinaryAssociation(
    name="functionName44",
    ends={
        Property(name="pycom_FunctionName", type=pycom_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Function45", type=pycom_FunctionName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
moduleType46: BinaryAssociation = BinaryAssociation(
    name="moduleType46",
    ends={
        Property(name="pycom_ModuleType47", type=pycom_ModuleFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_ModuleFunction", type=pycom_ModuleType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pycom_ConditionalAction_ExpMember = Generalization(general=ExpMember, specific=pycom_ConditionalAction)
gen_pycom_Sensor_BoardMember = Generalization(general=BoardMember, specific=pycom_Sensor)
gen_pycom_Actuator_BoardMember = Generalization(general=BoardMember, specific=pycom_Actuator)
gen_pycom_Communication_BoardMember = Generalization(general=BoardMember, specific=pycom_Communication)
gen_pycom_ActuatorType_ModuleType = Generalization(general=ModuleType, specific=pycom_ActuatorType)
gen_pycom_SensorType_ModuleType = Generalization(general=ModuleType, specific=pycom_SensorType)
gen_pycom_Function_ExpMember = Generalization(general=ExpMember, specific=pycom_Function)
gen_pycom_ModuleFunction_Function = Generalization(general=Function, specific=pycom_ModuleFunction)

# Domain Model
domain_model = DomainModel(
    name="pycom",
    types={ExpMember, pycom_Condition, pycom_System, pycom_ExpMember, pycom_Board, pycom_Sensor, BoardMember, pycom_ModuleType, pycom_Server, pycom_Actuator, pycom_Connection, pycom_Communication, pycom_ConditionalAction, pycom_Host, pycom_BoardMember, pycom_LogicExp, pycom_Boolean, pycom_ComparisonExp, pycom_Expression, pycom_Function, pycom_Pin, pycom_PinName, pycom_ActuatorType, ModuleType, pycom_SensorType, pycom_FunctionName, pycom_ModuleFunction, Function},
    associations={condition11, ExpMembers13, boards0, sensorTypes15, servers1, actuatorTypes16, conn3, exps5, host7, boardMembers9, logicEx25, nestedCondition28, boolVal30, compExp32, left34, right36, pins18, power20, input22, outputfunction39, board41, functionName44, moduleType46},
    generalizations={gen_pycom_ConditionalAction_ExpMember, gen_pycom_Sensor_BoardMember, gen_pycom_Actuator_BoardMember, gen_pycom_Communication_BoardMember, gen_pycom_ActuatorType_ModuleType, gen_pycom_SensorType_ModuleType, gen_pycom_Function_ExpMember, gen_pycom_ModuleFunction_Function},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)