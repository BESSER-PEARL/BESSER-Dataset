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
iOTConnector_Program = Class(name="iOTConnector::Program")
iOTConnector_Webserver = Class(name="iOTConnector::Webserver")
iOTConnector_Wifi = Class(name="iOTConnector::Wifi")
iOTConnector_Config = Class(name="iOTConnector::Config")
iOTConnector_Board = Class(name="iOTConnector::Board")
iOTConnector_Output = Class(name="iOTConnector::Output")
iOTConnector_Function = Class(name="iOTConnector::Function")
iOTConnector_Send = Class(name="iOTConnector::Send")
iOTConnector_ReadingName = Class(name="iOTConnector::ReadingName")
iOTConnector_Sample = Class(name="iOTConnector::Sample")
Function = Class(name="Function")
iOTConnector_SampleAction = Class(name="iOTConnector::SampleAction")
iOTConnector_ReadingNameWithConfigScope = Class(name="iOTConnector::ReadingNameWithConfigScope")
iOTConnector_Sensor = Class(name="iOTConnector::Sensor")
iOTConnector_SensorConfig = Class(name="iOTConnector::SensorConfig")
iOTConnector_BitwiseOperator = Class(name="iOTConnector::BitwiseOperator")
iOTConnector_Process = Class(name="iOTConnector::Process")
iOTConnector_ProcessAction = Class(name="iOTConnector::ProcessAction")
iOTConnector_Expression = Class(name="iOTConnector::Expression")
iOTConnector_RelationalOperator = Class(name="iOTConnector::RelationalOperator")
iOTConnector_TimeUnit = Class(name="iOTConnector::TimeUnit")
iOTConnector_Filter = Class(name="iOTConnector::Filter")
iOTConnector_FilterAction = Class(name="iOTConnector::FilterAction")
iOTConnector_FilterType = Class(name="iOTConnector::FilterType")
iOTConnector_FilterExp = Class(name="iOTConnector::FilterExp")
iOTConnector_Plus = Class(name="iOTConnector::Plus")
Expression = Class(name="Expression")
iOTConnector_Minus = Class(name="iOTConnector::Minus")
iOTConnector_Mult = Class(name="iOTConnector::Mult")
iOTConnector_Div = Class(name="iOTConnector::Div")
iOTConnector_SendAction = Class(name="iOTConnector::SendAction")
iOTConnector_Num = Class(name="iOTConnector::Num")
iOTConnector_Var = Class(name="iOTConnector::Var")

# iOTConnector_Program class attributes and methods

# iOTConnector_Webserver class attributes and methods
iOTConnector_Webserver_url: Property = Property(name="url", type=StringType)
iOTConnector_Webserver_port: Property = Property(name="port", type=IntegerType)
iOTConnector_Webserver.attributes={iOTConnector_Webserver_port, iOTConnector_Webserver_url}

# iOTConnector_Wifi class attributes and methods
iOTConnector_Wifi_ssid: Property = Property(name="ssid", type=StringType)
iOTConnector_Wifi_password: Property = Property(name="password", type=StringType)
iOTConnector_Wifi.attributes={iOTConnector_Wifi_password, iOTConnector_Wifi_ssid}

# iOTConnector_Config class attributes and methods
iOTConnector_Config_name: Property = Property(name="name", type=StringType)
iOTConnector_Config.attributes={iOTConnector_Config_name}

# iOTConnector_Board class attributes and methods
iOTConnector_Board_name: Property = Property(name="name", type=StringType)
iOTConnector_Board.attributes={iOTConnector_Board_name}

# iOTConnector_Output class attributes and methods

# iOTConnector_Function class attributes and methods

# iOTConnector_Send class attributes and methods

# iOTConnector_ReadingName class attributes and methods
iOTConnector_ReadingName_name: Property = Property(name="name", type=StringType)
iOTConnector_ReadingName.attributes={iOTConnector_ReadingName_name}

# iOTConnector_Sample class attributes and methods

# Function class attributes and methods

# iOTConnector_SampleAction class attributes and methods
iOTConnector_SampleAction_number: Property = Property(name="number", type=IntegerType)
iOTConnector_SampleAction_amountOfTime: Property = Property(name="amountOfTime", type=IntegerType)
iOTConnector_SampleAction.attributes={iOTConnector_SampleAction_number, iOTConnector_SampleAction_amountOfTime}

# iOTConnector_ReadingNameWithConfigScope class attributes and methods

# iOTConnector_Sensor class attributes and methods
iOTConnector_Sensor_name: Property = Property(name="name", type=StringType)
iOTConnector_Sensor_type: Property = Property(name="type", type=StringType)
iOTConnector_Sensor.attributes={iOTConnector_Sensor_type, iOTConnector_Sensor_name}

# iOTConnector_SensorConfig class attributes and methods
iOTConnector_SensorConfig_pinOut: Property = Property(name="pinOut", type=StringType)
iOTConnector_SensorConfig_name: Property = Property(name="name", type=StringType)
iOTConnector_SensorConfig_pinIn: Property = Property(name="pinIn", type=StringType)
iOTConnector_SensorConfig.attributes={iOTConnector_SensorConfig_name, iOTConnector_SensorConfig_pinIn, iOTConnector_SensorConfig_pinOut}

# iOTConnector_BitwiseOperator class attributes and methods
iOTConnector_BitwiseOperator_value: Property = Property(name="value", type=StringType)
iOTConnector_BitwiseOperator.attributes={iOTConnector_BitwiseOperator_value}

# iOTConnector_Process class attributes and methods

# iOTConnector_ProcessAction class attributes and methods

# iOTConnector_Expression class attributes and methods

# iOTConnector_RelationalOperator class attributes and methods
iOTConnector_RelationalOperator_value: Property = Property(name="value", type=StringType)
iOTConnector_RelationalOperator.attributes={iOTConnector_RelationalOperator_value}

# iOTConnector_TimeUnit class attributes and methods
iOTConnector_TimeUnit_value: Property = Property(name="value", type=StringType)
iOTConnector_TimeUnit.attributes={iOTConnector_TimeUnit_value}

# iOTConnector_Filter class attributes and methods

# iOTConnector_FilterAction class attributes and methods
iOTConnector_FilterAction_number: Property = Property(name="number", type=IntegerType)
iOTConnector_FilterAction.attributes={iOTConnector_FilterAction_number}

# iOTConnector_FilterType class attributes and methods
iOTConnector_FilterType_value: Property = Property(name="value", type=StringType)
iOTConnector_FilterType.attributes={iOTConnector_FilterType_value}

# iOTConnector_FilterExp class attributes and methods
iOTConnector_FilterExp_number: Property = Property(name="number", type=IntegerType)
iOTConnector_FilterExp.attributes={iOTConnector_FilterExp_number}

# iOTConnector_Plus class attributes and methods

# Expression class attributes and methods

# iOTConnector_Minus class attributes and methods

# iOTConnector_Mult class attributes and methods

# iOTConnector_Div class attributes and methods

# iOTConnector_SendAction class attributes and methods
iOTConnector_SendAction_number: Property = Property(name="number", type=IntegerType)
iOTConnector_SendAction.attributes={iOTConnector_SendAction_number}

# iOTConnector_Num class attributes and methods
iOTConnector_Num_value: Property = Property(name="value", type=IntegerType)
iOTConnector_Num.attributes={iOTConnector_Num_value}

# iOTConnector_Var class attributes and methods

# Relationships
webserver0: BinaryAssociation = BinaryAssociation(
    name="webserver0",
    ends={
        Property(name="iOTConnector_Webserver", type=iOTConnector_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Program", type=iOTConnector_Webserver, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wifis1: BinaryAssociation = BinaryAssociation(
    name="wifis1",
    ends={
        Property(name="iOTConnector_Wifi", type=iOTConnector_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Program2", type=iOTConnector_Wifi, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configs3: BinaryAssociation = BinaryAssociation(
    name="configs3",
    ends={
        Property(name="iOTConnector_Config", type=iOTConnector_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Program4", type=iOTConnector_Config, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boards5: BinaryAssociation = BinaryAssociation(
    name="boards5",
    ends={
        Property(name="iOTConnector_Board", type=iOTConnector_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Program6", type=iOTConnector_Board, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output14: BinaryAssociation = BinaryAssociation(
    name="output14",
    ends={
        Property(name="iOTConnector_Output", type=iOTConnector_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Sensor15", type=iOTConnector_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions16: BinaryAssociation = BinaryAssociation(
    name="functions16",
    ends={
        Property(name="iOTConnector_Function", type=iOTConnector_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Sensor17", type=iOTConnector_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send18: BinaryAssociation = BinaryAssociation(
    name="send18",
    ends={
        Property(name="iOTConnector_Send", type=iOTConnector_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Sensor19", type=iOTConnector_Send, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
readingNames20: BinaryAssociation = BinaryAssociation(
    name="readingNames20",
    ends={
        Property(name="iOTConnector_ReadingName", type=iOTConnector_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Output21", type=iOTConnector_ReadingName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sampleActions22: BinaryAssociation = BinaryAssociation(
    name="sampleActions22",
    ends={
        Property(name="iOTConnector_SampleAction", type=iOTConnector_Sample, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Sample", type=iOTConnector_SampleAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readingName23: BinaryAssociation = BinaryAssociation(
    name="readingName23",
    ends={
        Property(name="iOTConnector_ReadingName25", type=iOTConnector_SampleAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_SampleAction24", type=iOTConnector_ReadingName, multiplicity=Multiplicity(0, 1))
    }
)
readingNameToCompare26: BinaryAssociation = BinaryAssociation(
    name="readingNameToCompare26",
    ends={
        Property(name="iOTConnector_ReadingNameWithConfigScope", type=iOTConnector_SampleAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_SampleAction27", type=iOTConnector_ReadingNameWithConfigScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensors7: BinaryAssociation = BinaryAssociation(
    name="sensors7",
    ends={
        Property(name="iOTConnector_Sensor", type=iOTConnector_Config, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Config8", type=iOTConnector_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensorConfigs9: BinaryAssociation = BinaryAssociation(
    name="sensorConfigs9",
    ends={
        Property(name="iOTConnector_SensorConfig", type=iOTConnector_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Board10", type=iOTConnector_SensorConfig, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configName11: BinaryAssociation = BinaryAssociation(
    name="configName11",
    ends={
        Property(name="iOTConnector_Config13", type=iOTConnector_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Board12", type=iOTConnector_Config, multiplicity=Multiplicity(0, 1))
    }
)
filterExp38: BinaryAssociation = BinaryAssociation(
    name="filterExp38",
    ends={
        Property(name="iOTConnector_FilterAction39", type=iOTConnector_FilterExp, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="iOTConnector_FilterExp", type=iOTConnector_FilterAction, multiplicity=Multiplicity(1, 1))
    }
)
readingName40: BinaryAssociation = BinaryAssociation(
    name="readingName40",
    ends={
        Property(name="iOTConnector_ReadingNameWithConfigScope42", type=iOTConnector_FilterExp, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_FilterExp41", type=iOTConnector_ReadingNameWithConfigScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationalOperator43: BinaryAssociation = BinaryAssociation(
    name="relationalOperator43",
    ends={
        Property(name="iOTConnector_RelationalOperator45", type=iOTConnector_FilterExp, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_FilterExp44", type=iOTConnector_RelationalOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bitwiseOperator46: BinaryAssociation = BinaryAssociation(
    name="bitwiseOperator46",
    ends={
        Property(name="iOTConnector_BitwiseOperator", type=iOTConnector_FilterExp, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_FilterExp47", type=iOTConnector_BitwiseOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterExp49: BinaryAssociation = BinaryAssociation(
    name="filterExp49",
    ends={
        Property(name="iOTConnector_FilterExp50", type=iOTConnector_FilterExp, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_FilterExp48", type=iOTConnector_FilterExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processActions51: BinaryAssociation = BinaryAssociation(
    name="processActions51",
    ends={
        Property(name="iOTConnector_ProcessAction", type=iOTConnector_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Process", type=iOTConnector_ProcessAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readingName52: BinaryAssociation = BinaryAssociation(
    name="readingName52",
    ends={
        Property(name="iOTConnector_ReadingName54", type=iOTConnector_ProcessAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_ProcessAction53", type=iOTConnector_ReadingName, multiplicity=Multiplicity(0, 1))
    }
)
exp55: BinaryAssociation = BinaryAssociation(
    name="exp55",
    ends={
        Property(name="iOTConnector_Expression", type=iOTConnector_ProcessAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_ProcessAction56", type=iOTConnector_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationalOperator28: BinaryAssociation = BinaryAssociation(
    name="relationalOperator28",
    ends={
        Property(name="iOTConnector_RelationalOperator", type=iOTConnector_SampleAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_SampleAction29", type=iOTConnector_RelationalOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeUnit30: BinaryAssociation = BinaryAssociation(
    name="timeUnit30",
    ends={
        Property(name="iOTConnector_TimeUnit", type=iOTConnector_SampleAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_SampleAction31", type=iOTConnector_TimeUnit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterActions32: BinaryAssociation = BinaryAssociation(
    name="filterActions32",
    ends={
        Property(name="iOTConnector_FilterAction", type=iOTConnector_Filter, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Filter", type=iOTConnector_FilterAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readingName33: BinaryAssociation = BinaryAssociation(
    name="readingName33",
    ends={
        Property(name="iOTConnector_ReadingName35", type=iOTConnector_FilterAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_FilterAction34", type=iOTConnector_ReadingName, multiplicity=Multiplicity(0, 1))
    }
)
filterType36: BinaryAssociation = BinaryAssociation(
    name="filterType36",
    ends={
        Property(name="iOTConnector_FilterType", type=iOTConnector_FilterAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_FilterAction37", type=iOTConnector_FilterType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left68: BinaryAssociation = BinaryAssociation(
    name="left68",
    ends={
        Property(name="iOTConnector_Expression69", type=iOTConnector_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Plus", type=iOTConnector_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right70: BinaryAssociation = BinaryAssociation(
    name="right70",
    ends={
        Property(name="iOTConnector_Expression72", type=iOTConnector_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Plus71", type=iOTConnector_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left73: BinaryAssociation = BinaryAssociation(
    name="left73",
    ends={
        Property(name="iOTConnector_Expression74", type=iOTConnector_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Minus", type=iOTConnector_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right75: BinaryAssociation = BinaryAssociation(
    name="right75",
    ends={
        Property(name="iOTConnector_Expression77", type=iOTConnector_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Minus76", type=iOTConnector_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left78: BinaryAssociation = BinaryAssociation(
    name="left78",
    ends={
        Property(name="iOTConnector_Expression79", type=iOTConnector_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Mult", type=iOTConnector_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right80: BinaryAssociation = BinaryAssociation(
    name="right80",
    ends={
        Property(name="iOTConnector_Expression82", type=iOTConnector_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Mult81", type=iOTConnector_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left83: BinaryAssociation = BinaryAssociation(
    name="left83",
    ends={
        Property(name="iOTConnector_Expression84", type=iOTConnector_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Div", type=iOTConnector_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sendActions57: BinaryAssociation = BinaryAssociation(
    name="sendActions57",
    ends={
        Property(name="iOTConnector_SendAction", type=iOTConnector_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Send58", type=iOTConnector_SendAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readingName59: BinaryAssociation = BinaryAssociation(
    name="readingName59",
    ends={
        Property(name="iOTConnector_ReadingName61", type=iOTConnector_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_SendAction60", type=iOTConnector_ReadingName, multiplicity=Multiplicity(0, 1))
    }
)
relationalOperator62: BinaryAssociation = BinaryAssociation(
    name="relationalOperator62",
    ends={
        Property(name="iOTConnector_RelationalOperator64", type=iOTConnector_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_SendAction63", type=iOTConnector_RelationalOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name65: BinaryAssociation = BinaryAssociation(
    name="name65",
    ends={
        Property(name="iOTConnector_ReadingName67", type=iOTConnector_ReadingNameWithConfigScope, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_ReadingNameWithConfigScope66", type=iOTConnector_ReadingName, multiplicity=Multiplicity(0, 1))
    }
)
right85: BinaryAssociation = BinaryAssociation(
    name="right85",
    ends={
        Property(name="iOTConnector_Expression87", type=iOTConnector_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Div86", type=iOTConnector_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
readingName88: BinaryAssociation = BinaryAssociation(
    name="readingName88",
    ends={
        Property(name="iOTConnector_ReadingNameWithConfigScope89", type=iOTConnector_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="iOTConnector_Var", type=iOTConnector_ReadingNameWithConfigScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_iOTConnector_Sample_Function = Generalization(general=Function, specific=iOTConnector_Sample)
gen_iOTConnector_Process_Function = Generalization(general=Function, specific=iOTConnector_Process)
gen_iOTConnector_Filter_Function = Generalization(general=Function, specific=iOTConnector_Filter)
gen_iOTConnector_Plus_Expression = Generalization(general=Expression, specific=iOTConnector_Plus)
gen_iOTConnector_Minus_Expression = Generalization(general=Expression, specific=iOTConnector_Minus)
gen_iOTConnector_Mult_Expression = Generalization(general=Expression, specific=iOTConnector_Mult)
gen_iOTConnector_Div_Expression = Generalization(general=Expression, specific=iOTConnector_Div)
gen_iOTConnector_Num_Expression = Generalization(general=Expression, specific=iOTConnector_Num)
gen_iOTConnector_Var_Expression = Generalization(general=Expression, specific=iOTConnector_Var)

# Domain Model
domain_model = DomainModel(
    name="iOTConnector",
    types={iOTConnector_Program, iOTConnector_Webserver, iOTConnector_Wifi, iOTConnector_Config, iOTConnector_Board, iOTConnector_Output, iOTConnector_Function, iOTConnector_Send, iOTConnector_ReadingName, iOTConnector_Sample, Function, iOTConnector_SampleAction, iOTConnector_ReadingNameWithConfigScope, iOTConnector_Sensor, iOTConnector_SensorConfig, iOTConnector_BitwiseOperator, iOTConnector_Process, iOTConnector_ProcessAction, iOTConnector_Expression, iOTConnector_RelationalOperator, iOTConnector_TimeUnit, iOTConnector_Filter, iOTConnector_FilterAction, iOTConnector_FilterType, iOTConnector_FilterExp, iOTConnector_Plus, Expression, iOTConnector_Minus, iOTConnector_Mult, iOTConnector_Div, iOTConnector_SendAction, iOTConnector_Num, iOTConnector_Var},
    associations={webserver0, wifis1, configs3, boards5, output14, functions16, send18, readingNames20, sampleActions22, readingName23, readingNameToCompare26, sensors7, sensorConfigs9, configName11, filterExp38, readingName40, relationalOperator43, bitwiseOperator46, filterExp49, processActions51, readingName52, exp55, relationalOperator28, timeUnit30, filterActions32, readingName33, filterType36, left68, right70, left73, right75, left78, right80, left83, sendActions57, readingName59, relationalOperator62, name65, right85, readingName88},
    generalizations={gen_iOTConnector_Sample_Function, gen_iOTConnector_Process_Function, gen_iOTConnector_Filter_Function, gen_iOTConnector_Plus_Expression, gen_iOTConnector_Minus_Expression, gen_iOTConnector_Mult_Expression, gen_iOTConnector_Div_Expression, gen_iOTConnector_Num_Expression, gen_iOTConnector_Var_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)