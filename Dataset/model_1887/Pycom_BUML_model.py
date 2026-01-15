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
pycom_System = Class(name="pycom::System")
pycom_ParameterType = Class(name="pycom::ParameterType")
pycom_Library = Class(name="pycom::Library")
pycom_Import = Class(name="pycom::Import")
pycom_Board = Class(name="pycom::Board")
pycom_Server = Class(name="pycom::Server")
pycom_BoardMember = Class(name="pycom::BoardMember")
pycom_Connection = Class(name="pycom::Connection")
pycom_ConditionalAction = Class(name="pycom::ConditionalAction")
pycom_Host = Class(name="pycom::Host")
pycom_ModuleType = Class(name="pycom::ModuleType")
pycom_ModuleName = Class(name="pycom::ModuleName")
pycom_Pin = Class(name="pycom::Pin")
pycom_Actuator = Class(name="pycom::Actuator")
BoardMember = Class(name="BoardMember")
pycom_Sensor = Class(name="pycom::Sensor")
ExpMember = Class(name="ExpMember")
pycom_Condition = Class(name="pycom::Condition")
pycom_ExpMember = Class(name="pycom::ExpMember")
pycom_PinName = Class(name="pycom::PinName")
pycom_Communication = Class(name="pycom::Communication")
pycom_CommunicationType = Class(name="pycom::CommunicationType")
pycom_ComparisonExp = Class(name="pycom::ComparisonExp")
pycom_Expression = Class(name="pycom::Expression")
pycom_LogicExp = Class(name="pycom::LogicExp")
pycom_Boolean = Class(name="pycom::Boolean")
pycom_Function = Class(name="pycom::Function")

# pycom_System class attributes and methods

# pycom_ParameterType class attributes and methods
pycom_ParameterType_number: Property = Property(name="number", type=IntegerType)
pycom_ParameterType_text: Property = Property(name="text", type=StringType)
pycom_ParameterType.attributes={pycom_ParameterType_number, pycom_ParameterType_text}

# pycom_Library class attributes and methods
pycom_Library_name: Property = Property(name="name", type=StringType)
pycom_Library.attributes={pycom_Library_name}

# pycom_Import class attributes and methods
pycom_Import_name: Property = Property(name="name", type=StringType)
pycom_Import_path: Property = Property(name="path", type=StringType)
pycom_Import.attributes={pycom_Import_name, pycom_Import_path}

# pycom_Board class attributes and methods
pycom_Board_name: Property = Property(name="name", type=StringType)
pycom_Board_boardType: Property = Property(name="boardType", type=StringType)
pycom_Board_communicationRate: Property = Property(name="communicationRate", type=IntegerType)
pycom_Board.attributes={pycom_Board_name, pycom_Board_communicationRate, pycom_Board_boardType}

# pycom_Server class attributes and methods
pycom_Server_name: Property = Property(name="name", type=StringType)
pycom_Server.attributes={pycom_Server_name}

# pycom_BoardMember class attributes and methods

# pycom_Connection class attributes and methods
pycom_Connection_portnumber: Property = Property(name="portnumber", type=IntegerType)
pycom_Connection.attributes={pycom_Connection_portnumber}

# pycom_ConditionalAction class attributes and methods
pycom_ConditionalAction_type: Property = Property(name="type", type=StringType)
pycom_ConditionalAction.attributes={pycom_ConditionalAction_type}

# pycom_Host class attributes and methods
pycom_Host_ipAdr: Property = Property(name="ipAdr", type=StringType)
pycom_Host_website: Property = Property(name="website", type=StringType)
pycom_Host.attributes={pycom_Host_ipAdr, pycom_Host_website}

# pycom_ModuleType class attributes and methods
pycom_ModuleType_name: Property = Property(name="name", type=StringType)
pycom_ModuleType.attributes={pycom_ModuleType_name}

# pycom_ModuleName class attributes and methods
pycom_ModuleName_name: Property = Property(name="name", type=StringType)
pycom_ModuleName.attributes={pycom_ModuleName_name}

# pycom_Pin class attributes and methods

# pycom_Actuator class attributes and methods

# BoardMember class attributes and methods

# pycom_Sensor class attributes and methods

# ExpMember class attributes and methods

# pycom_Condition class attributes and methods
pycom_Condition_operator: Property = Property(name="operator", type=StringType)
pycom_Condition.attributes={pycom_Condition_operator}

# pycom_ExpMember class attributes and methods

# pycom_PinName class attributes and methods
pycom_PinName_name: Property = Property(name="name", type=StringType)
pycom_PinName.attributes={pycom_PinName_name}

# pycom_Communication class attributes and methods

# pycom_CommunicationType class attributes and methods
pycom_CommunicationType_name: Property = Property(name="name", type=StringType)
pycom_CommunicationType_ssid: Property = Property(name="ssid", type=StringType)
pycom_CommunicationType_password: Property = Property(name="password", type=StringType)
pycom_CommunicationType.attributes={pycom_CommunicationType_ssid, pycom_CommunicationType_name, pycom_CommunicationType_password}

# pycom_ComparisonExp class attributes and methods
pycom_ComparisonExp_op: Property = Property(name="op", type=StringType)
pycom_ComparisonExp.attributes={pycom_ComparisonExp_op}

# pycom_Expression class attributes and methods
pycom_Expression_outputValue: Property = Property(name="outputValue", type=IntegerType)
pycom_Expression.attributes={pycom_Expression_outputValue}

# pycom_LogicExp class attributes and methods

# pycom_Boolean class attributes and methods
pycom_Boolean_value: Property = Property(name="value", type=StringType)
pycom_Boolean.attributes={pycom_Boolean_value}

# pycom_Function class attributes and methods

# Relationships
imports7: BinaryAssociation = BinaryAssociation(
    name="imports7",
    ends={
        Property(name="pycom_Import9", type=pycom_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Library8", type=pycom_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter10: BinaryAssociation = BinaryAssociation(
    name="parameter10",
    ends={
        Property(name="pycom_ParameterType", type=pycom_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Import11", type=pycom_ParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries0: BinaryAssociation = BinaryAssociation(
    name="libraries0",
    ends={
        Property(name="pycom_Library", type=pycom_System, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_System", type=pycom_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="pycom_Import", type=pycom_System, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_System2", type=pycom_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boards3: BinaryAssociation = BinaryAssociation(
    name="boards3",
    ends={
        Property(name="pycom_Board", type=pycom_System, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_System4", type=pycom_Board, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
servers5: BinaryAssociation = BinaryAssociation(
    name="servers5",
    ends={
        Property(name="pycom_Server", type=pycom_System, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_System6", type=pycom_Server, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library18: BinaryAssociation = BinaryAssociation(
    name="library18",
    ends={
        Property(name="pycom_Library20", type=pycom_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Board19", type=pycom_Library, multiplicity=Multiplicity(0, 9999))
    }
)
boardMembers21: BinaryAssociation = BinaryAssociation(
    name="boardMembers21",
    ends={
        Property(name="pycom_BoardMember", type=pycom_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Board22", type=pycom_BoardMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conn12: BinaryAssociation = BinaryAssociation(
    name="conn12",
    ends={
        Property(name="pycom_Connection", type=pycom_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Server13", type=pycom_Connection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exps14: BinaryAssociation = BinaryAssociation(
    name="exps14",
    ends={
        Property(name="pycom_ConditionalAction", type=pycom_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Server15", type=pycom_ConditionalAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
host16: BinaryAssociation = BinaryAssociation(
    name="host16",
    ends={
        Property(name="pycom_Host", type=pycom_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Connection17", type=pycom_Host, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName29: BinaryAssociation = BinaryAssociation(
    name="typeName29",
    ends={
        Property(name="pycom_ModuleType", type=pycom_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Sensor30", type=pycom_ModuleType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensorName31: BinaryAssociation = BinaryAssociation(
    name="sensorName31",
    ends={
        Property(name="pycom_ModuleName", type=pycom_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Sensor32", type=pycom_ModuleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pins33: BinaryAssociation = BinaryAssociation(
    name="pins33",
    ends={
        Property(name="pycom_Pin", type=pycom_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Sensor34", type=pycom_Pin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName35: BinaryAssociation = BinaryAssociation(
    name="typeName35",
    ends={
        Property(name="pycom_ModuleType36", type=pycom_Actuator, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Actuator", type=pycom_ModuleType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boardMember23: BinaryAssociation = BinaryAssociation(
    name="boardMember23",
    ends={
        Property(name="pycom_Sensor", type=pycom_BoardMember, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_BoardMember24", type=pycom_Sensor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition25: BinaryAssociation = BinaryAssociation(
    name="condition25",
    ends={
        Property(name="pycom_Condition", type=pycom_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_ConditionalAction26", type=pycom_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpMembers27: BinaryAssociation = BinaryAssociation(
    name="ExpMembers27",
    ends={
        Property(name="pycom_ExpMember", type=pycom_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_ConditionalAction28", type=pycom_ExpMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type43: BinaryAssociation = BinaryAssociation(
    name="type43",
    ends={
        Property(name="pycom_CommunicationType", type=pycom_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Communication", type=pycom_CommunicationType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
power44: BinaryAssociation = BinaryAssociation(
    name="power44",
    ends={
        Property(name="pycom_PinName", type=pycom_Pin, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Pin45", type=pycom_PinName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input46: BinaryAssociation = BinaryAssociation(
    name="input46",
    ends={
        Property(name="pycom_PinName48", type=pycom_Pin, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Pin47", type=pycom_PinName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actuatorName37: BinaryAssociation = BinaryAssociation(
    name="actuatorName37",
    ends={
        Property(name="pycom_ModuleName39", type=pycom_Actuator, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Actuator38", type=pycom_ModuleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pins40: BinaryAssociation = BinaryAssociation(
    name="pins40",
    ends={
        Property(name="pycom_Pin42", type=pycom_Actuator, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Actuator41", type=pycom_Pin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compExp56: BinaryAssociation = BinaryAssociation(
    name="compExp56",
    ends={
        Property(name="pycom_ComparisonExp", type=pycom_LogicExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_LogicExp57", type=pycom_ComparisonExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left58: BinaryAssociation = BinaryAssociation(
    name="left58",
    ends={
        Property(name="pycom_Expression", type=pycom_ComparisonExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_ComparisonExp59", type=pycom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right60: BinaryAssociation = BinaryAssociation(
    name="right60",
    ends={
        Property(name="pycom_Expression62", type=pycom_ComparisonExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_ComparisonExp61", type=pycom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logicEx49: BinaryAssociation = BinaryAssociation(
    name="logicEx49",
    ends={
        Property(name="pycom_LogicExp", type=pycom_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Condition50", type=pycom_LogicExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedCondition52: BinaryAssociation = BinaryAssociation(
    name="nestedCondition52",
    ends={
        Property(name="pycom_Condition53", type=pycom_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Condition51", type=pycom_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boolVal54: BinaryAssociation = BinaryAssociation(
    name="boolVal54",
    ends={
        Property(name="pycom_Boolean", type=pycom_LogicExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_LogicExp55", type=pycom_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputfunction63: BinaryAssociation = BinaryAssociation(
    name="outputfunction63",
    ends={
        Property(name="pycom_Function", type=pycom_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Expression64", type=pycom_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
board65: BinaryAssociation = BinaryAssociation(
    name="board65",
    ends={
        Property(name="pycom_Board67", type=pycom_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Function66", type=pycom_Board, multiplicity=Multiplicity(0, 1))
    }
)
functionName68: BinaryAssociation = BinaryAssociation(
    name="functionName68",
    ends={
        Property(name="pycom_Import70", type=pycom_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Function69", type=pycom_Import, multiplicity=Multiplicity(0, 1))
    }
)
pins71: BinaryAssociation = BinaryAssociation(
    name="pins71",
    ends={
        Property(name="pycom_Pin73", type=pycom_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="pycom_Function72", type=pycom_Pin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pycom_Actuator_BoardMember = Generalization(general=BoardMember, specific=pycom_Actuator)
gen_pycom_ConditionalAction_ExpMember = Generalization(general=ExpMember, specific=pycom_ConditionalAction)
gen_pycom_Communication_BoardMember = Generalization(general=BoardMember, specific=pycom_Communication)
gen_pycom_Function_ExpMember = Generalization(general=ExpMember, specific=pycom_Function)

# Domain Model
domain_model = DomainModel(
    name="pycom",
    types={pycom_System, pycom_ParameterType, pycom_Library, pycom_Import, pycom_Board, pycom_Server, pycom_BoardMember, pycom_Connection, pycom_ConditionalAction, pycom_Host, pycom_ModuleType, pycom_ModuleName, pycom_Pin, pycom_Actuator, BoardMember, pycom_Sensor, ExpMember, pycom_Condition, pycom_ExpMember, pycom_PinName, pycom_Communication, pycom_CommunicationType, pycom_ComparisonExp, pycom_Expression, pycom_LogicExp, pycom_Boolean, pycom_Function},
    associations={imports7, parameter10, libraries0, imports1, boards3, servers5, library18, boardMembers21, conn12, exps14, host16, typeName29, sensorName31, pins33, typeName35, boardMember23, condition25, ExpMembers27, type43, power44, input46, actuatorName37, pins40, compExp56, left58, right60, logicEx49, nestedCondition52, boolVal54, outputfunction63, board65, functionName68, pins71},
    generalizations={gen_pycom_Actuator_BoardMember, gen_pycom_ConditionalAction_ExpMember, gen_pycom_Communication_BoardMember, gen_pycom_Function_ExpMember},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)