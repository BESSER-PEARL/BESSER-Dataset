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
NumericOperator: Enumeration = Enumeration(
    name="NumericOperator",
    literals={
            EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="neq"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="leq"),
			EnumerationLiteral(name="geq")
    }
)

StringOperator: Enumeration = Enumeration(
    name="StringOperator",
    literals={
            EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="neq")
    }
)

BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="neq")
    }
)

# Classes
raspirover_RasPiBoard = Class(name="raspirover::RasPiBoard")
Board = Class(name="Board")
raspirover_DigitalPin = Class(name="raspirover::DigitalPin")
raspirover_AnalogPin = Class(name="raspirover::AnalogPin")
raspirover_Board = Class(name="raspirover::Board", is_abstract=True)
NamedElement = Class(name="NamedElement")
raspirover_Project = Class(name="raspirover::Project")
raspirover_NamedElement = Class(name="raspirover::NamedElement", is_abstract=True)
raspirover_Param = Class(name="raspirover::Param")
raspirover_RclBlock = Class(name="raspirover::RclBlock")
raspirover_Sketch = Class(name="raspirover::Sketch")
raspirover_RoverProgram = Class(name="raspirover::RoverProgram")
raspirover_Block = Class(name="raspirover::Block")
raspirover_Instruction = Class(name="raspirover::Instruction", is_abstract=True)
Pin = Class(name="Pin")
raspirover_ArduinoDigitalModule = Class(name="raspirover::ArduinoDigitalModule", is_abstract=True)
raspirover_Pin = Class(name="raspirover::Pin")
ArduinoModule = Class(name="ArduinoModule")
raspirover_ArduinoModule = Class(name="raspirover::ArduinoModule", is_abstract=True)
Module = Class(name="Module")
raspirover_Module = Class(name="raspirover::Module", is_abstract=True)
raspirover_ArduinoAnalogModule = Class(name="raspirover::ArduinoAnalogModule", is_abstract=True)
raspirover_HumidityQuery = Class(name="raspirover::HumidityQuery")
raspirover_Statement = Class(name="raspirover::Statement", is_abstract=True)
raspirover_VarAssignment = Class(name="raspirover::VarAssignment")
Statement = Class(name="Statement")
raspirover_RoverValue = Class(name="raspirover::RoverValue")
raspirover_Conditional = Class(name="raspirover::Conditional")
raspirover_RoverExpression = Class(name="raspirover::RoverExpression", is_abstract=True)
raspirover_Loop = Class(name="raspirover::Loop")
raspirover_Query = Class(name="raspirover::Query", is_abstract=True)
raspirover_TemperatureQuery = Class(name="raspirover::TemperatureQuery")
Query = Class(name="Query")
NumberValue = Class(name="NumberValue")
raspirover_MessageQuery = Class(name="raspirover::MessageQuery")
StringValue = Class(name="StringValue")
raspirover_ObstacleQuery = Class(name="raspirover::ObstacleQuery")
BooleanValue = Class(name="BooleanValue")
raspirover_NumericExpression = Class(name="raspirover::NumericExpression")
RoverExpression = Class(name="RoverExpression")
raspirover_NumberValue = Class(name="raspirover::NumberValue")
raspirover_StringExpression = Class(name="raspirover::StringExpression")
raspirover_StringValue = Class(name="raspirover::StringValue")
raspirover_BooleanExpression = Class(name="raspirover::BooleanExpression")
raspirover_BooleanValue = Class(name="raspirover::BooleanValue")
RoverValue = Class(name="RoverValue")
raspirover_Quantity = Class(name="raspirover::Quantity")
raspirover_Action = Class(name="raspirover::Action", is_abstract=True)
raspirover_ForwardAction = Class(name="raspirover::ForwardAction")
Action = Class(name="Action")
raspirover_ForwardMinAction = Class(name="raspirover::ForwardMinAction")
raspirover_BackwardAction = Class(name="raspirover::BackwardAction")
raspirover_BackwardMinAction = Class(name="raspirover::BackwardMinAction")
raspirover_TurnAction = Class(name="raspirover::TurnAction")
raspirover_TurnDegAction = Class(name="raspirover::TurnDegAction")
raspirover_LogAction = Class(name="raspirover::LogAction")
raspirover_StopAction = Class(name="raspirover::StopAction")
raspirover_SendAction = Class(name="raspirover::SendAction")
raspirover_VarRef = Class(name="raspirover::VarRef")
raspirover_Unit = Class(name="raspirover::Unit", is_abstract=True)
raspirover_LengthUnit = Class(name="raspirover::LengthUnit", is_abstract=True)
Unit = Class(name="Unit")
raspirover_Centimeter = Class(name="raspirover::Centimeter")
MetricSystemUnit = Class(name="MetricSystemUnit")
LengthUnit = Class(name="LengthUnit")
raspirover_Millimeter = Class(name="raspirover::Millimeter")
raspirover_Meter = Class(name="raspirover::Meter")
raspirover_Foot = Class(name="raspirover::Foot")
ImperialSystemUnit = Class(name="ImperialSystemUnit")
raspirover_Inch = Class(name="raspirover::Inch")
raspirover_Yard = Class(name="raspirover::Yard")
raspirover_MetricSystemUnit = Class(name="raspirover::MetricSystemUnit", is_abstract=True)
raspirover_ImperialSystemUnit = Class(name="raspirover::ImperialSystemUnit", is_abstract=True)
raspirover_AngleUnit = Class(name="raspirover::AngleUnit", is_abstract=True)
raspirover_Radian = Class(name="raspirover::Radian")
AngleUnit = Class(name="AngleUnit")
raspirover_Degree = Class(name="raspirover::Degree")
raspirover_Turn = Class(name="raspirover::Turn")
raspirover_Gradian = Class(name="raspirover::Gradian")
raspirover_Length = Class(name="raspirover::Length")
Quantity = Class(name="Quantity")
raspirover_Angle = Class(name="raspirover::Angle")
raspirover_QuantityOperation = Class(name="raspirover::QuantityOperation", is_abstract=True)
raspirover_LengthOperation = Class(name="raspirover::LengthOperation", is_abstract=True)
QuantityOperation = Class(name="QuantityOperation")
raspirover_LengthAdd = Class(name="raspirover::LengthAdd")
LengthOperation = Class(name="LengthOperation")
QuantityHomogenousOperation = Class(name="QuantityHomogenousOperation")
raspirover_LengthSubtract = Class(name="raspirover::LengthSubtract")
raspirover_LengthScalarMultiply = Class(name="raspirover::LengthScalarMultiply")
QuantityScalarOperation = Class(name="QuantityScalarOperation")
raspirover_LengthScalarDivide = Class(name="raspirover::LengthScalarDivide")
raspirover_LengthEquals = Class(name="raspirover::LengthEquals")
raspirover_LengthDistinct = Class(name="raspirover::LengthDistinct")
raspirover_LengthSmaller = Class(name="raspirover::LengthSmaller")
raspirover_LengthGreater = Class(name="raspirover::LengthGreater")
raspirover_AngleOperation = Class(name="raspirover::AngleOperation", is_abstract=True)
raspirover_AngleAdd = Class(name="raspirover::AngleAdd")
AngleOperation = Class(name="AngleOperation")
raspirover_AngleSubtract = Class(name="raspirover::AngleSubtract")
raspirover_AngleScalarMultiply = Class(name="raspirover::AngleScalarMultiply")
raspirover_AngleScalarDivide = Class(name="raspirover::AngleScalarDivide")
raspirover_AngleEquals = Class(name="raspirover::AngleEquals")
raspirover_AngleDistinct = Class(name="raspirover::AngleDistinct")
raspirover_AngleSmaller = Class(name="raspirover::AngleSmaller")
raspirover_AngleGreater = Class(name="raspirover::AngleGreater")
raspirover_QuantityArithmeticOperation = Class(name="raspirover::QuantityArithmeticOperation", is_abstract=True)
raspirover_QuantityComparisonOperation = Class(name="raspirover::QuantityComparisonOperation", is_abstract=True)
raspirover_QuantityHomogenousOperation = Class(name="raspirover::QuantityHomogenousOperation", is_abstract=True)
raspirover_QuantityScalarOperation = Class(name="raspirover::QuantityScalarOperation", is_abstract=True)

# raspirover_RasPiBoard class attributes and methods

# Board class attributes and methods

# raspirover_DigitalPin class attributes and methods

# raspirover_AnalogPin class attributes and methods

# raspirover_Board class attributes and methods

# NamedElement class attributes and methods

# raspirover_Project class attributes and methods
raspirover_Project_m_execute: Method = Method(name="execute", parameters={})
raspirover_Project.methods={raspirover_Project_m_execute}

# raspirover_NamedElement class attributes and methods
raspirover_NamedElement_name: Property = Property(name="name", type=StringType)
raspirover_NamedElement.attributes={raspirover_NamedElement_name}

# raspirover_Param class attributes and methods
raspirover_Param_name: Property = Property(name="name", type=StringType)
raspirover_Param.attributes={raspirover_Param_name}

# raspirover_RclBlock class attributes and methods
raspirover_RclBlock_m_eval: Method = Method(name="eval", parameters={})
raspirover_RclBlock.methods={raspirover_RclBlock_m_eval}

# raspirover_Sketch class attributes and methods

# raspirover_RoverProgram class attributes and methods
raspirover_RoverProgram_name: Property = Property(name="name", type=StringType)
raspirover_RoverProgram_m_getVar: Method = Method(name="getVar", parameters={Parameter(name='n')}, type=StringType)
raspirover_RoverProgram_m_bindVar: Method = Method(name="bindVar", parameters={Parameter(name='n'), Parameter(name='v')})
raspirover_RoverProgram_m_run: Method = Method(name="run", parameters={})
raspirover_RoverProgram.attributes={raspirover_RoverProgram_name}
raspirover_RoverProgram.methods={raspirover_RoverProgram_m_getVar, raspirover_RoverProgram_m_bindVar, raspirover_RoverProgram_m_run}

# raspirover_Block class attributes and methods
raspirover_Block_m_execute: Method = Method(name="execute", parameters={})
raspirover_Block.methods={raspirover_Block_m_execute}

# raspirover_Instruction class attributes and methods
raspirover_Instruction_m_execute: Method = Method(name="execute", parameters={})
raspirover_Instruction_m_finalize: Method = Method(name="finalize", parameters={})
raspirover_Instruction.methods={raspirover_Instruction_m_execute, raspirover_Instruction_m_finalize}

# Pin class attributes and methods

# raspirover_ArduinoDigitalModule class attributes and methods

# raspirover_Pin class attributes and methods
raspirover_Pin_level: Property = Property(name="level", type=IntegerType)
raspirover_Pin.attributes={raspirover_Pin_level}

# ArduinoModule class attributes and methods

# raspirover_ArduinoModule class attributes and methods

# Module class attributes and methods

# raspirover_Module class attributes and methods

# raspirover_ArduinoAnalogModule class attributes and methods

# raspirover_HumidityQuery class attributes and methods
raspirover_HumidityQuery_m_getIntValue: Method = Method(name="getIntValue", parameters={})
raspirover_HumidityQuery.methods={raspirover_HumidityQuery_m_getIntValue}

# raspirover_Statement class attributes and methods
raspirover_Statement_m_eval: Method = Method(name="eval", parameters={})
raspirover_Statement_m_getProgram: Method = Method(name="getProgram", parameters={}, type=StringType)
raspirover_Statement.methods={raspirover_Statement_m_eval, raspirover_Statement_m_getProgram}

# raspirover_VarAssignment class attributes and methods
raspirover_VarAssignment_name: Property = Property(name="name", type=BooleanType)
raspirover_VarAssignment_m_eval: Method = Method(name="eval", parameters={})
raspirover_VarAssignment.attributes={raspirover_VarAssignment_name}
raspirover_VarAssignment.methods={raspirover_VarAssignment_m_eval}

# Statement class attributes and methods

# raspirover_RoverValue class attributes and methods

# raspirover_Conditional class attributes and methods
raspirover_Conditional_m_eval: Method = Method(name="eval", parameters={})
raspirover_Conditional.methods={raspirover_Conditional_m_eval}

# raspirover_RoverExpression class attributes and methods
raspirover_RoverExpression_m_eval: Method = Method(name="eval", parameters={})
raspirover_RoverExpression.methods={raspirover_RoverExpression_m_eval}

# raspirover_Loop class attributes and methods
raspirover_Loop_m_eval: Method = Method(name="eval", parameters={})
raspirover_Loop.methods={raspirover_Loop_m_eval}

# raspirover_Query class attributes and methods

# raspirover_TemperatureQuery class attributes and methods
raspirover_TemperatureQuery_m_getIntValue: Method = Method(name="getIntValue", parameters={})
raspirover_TemperatureQuery.methods={raspirover_TemperatureQuery_m_getIntValue}

# Query class attributes and methods

# NumberValue class attributes and methods

# raspirover_MessageQuery class attributes and methods
raspirover_MessageQuery_m_getStringValue: Method = Method(name="getStringValue", parameters={})
raspirover_MessageQuery.methods={raspirover_MessageQuery_m_getStringValue}

# StringValue class attributes and methods

# raspirover_ObstacleQuery class attributes and methods
raspirover_ObstacleQuery_front: Property = Property(name="front", type=BooleanType)
raspirover_ObstacleQuery_m_getBooleanValue: Method = Method(name="getBooleanValue", parameters={})
raspirover_ObstacleQuery.attributes={raspirover_ObstacleQuery_front}
raspirover_ObstacleQuery.methods={raspirover_ObstacleQuery_m_getBooleanValue}

# BooleanValue class attributes and methods

# raspirover_NumericExpression class attributes and methods
raspirover_NumericExpression_op: Property = Property(name="op", type=BooleanType)
raspirover_NumericExpression_m_eval: Method = Method(name="eval", parameters={})
raspirover_NumericExpression.attributes={raspirover_NumericExpression_op}
raspirover_NumericExpression.methods={raspirover_NumericExpression_m_eval}

# RoverExpression class attributes and methods

# raspirover_NumberValue class attributes and methods
raspirover_NumberValue_nValue: Property = Property(name="nValue", type=StringType)
raspirover_NumberValue_m_getIntValue: Method = Method(name="getIntValue", parameters={})
raspirover_NumberValue_m_print: Method = Method(name="print", parameters={})
raspirover_NumberValue.attributes={raspirover_NumberValue_nValue}
raspirover_NumberValue.methods={raspirover_NumberValue_m_getIntValue, raspirover_NumberValue_m_print}

# raspirover_StringExpression class attributes and methods
raspirover_StringExpression_op: Property = Property(name="op", type=BooleanType)
raspirover_StringExpression_m_eval: Method = Method(name="eval", parameters={})
raspirover_StringExpression.attributes={raspirover_StringExpression_op}
raspirover_StringExpression.methods={raspirover_StringExpression_m_eval}

# raspirover_StringValue class attributes and methods
raspirover_StringValue_sValue: Property = Property(name="sValue", type=BooleanType)
raspirover_StringValue_m_getStringValue: Method = Method(name="getStringValue", parameters={})
raspirover_StringValue.attributes={raspirover_StringValue_sValue}
raspirover_StringValue.methods={raspirover_StringValue_m_getStringValue}

# raspirover_BooleanExpression class attributes and methods
raspirover_BooleanExpression_op: Property = Property(name="op", type=StringType)
raspirover_BooleanExpression_m_eval: Method = Method(name="eval", parameters={})
raspirover_BooleanExpression.attributes={raspirover_BooleanExpression_op}
raspirover_BooleanExpression.methods={raspirover_BooleanExpression_m_eval}

# raspirover_BooleanValue class attributes and methods
raspirover_BooleanValue_bValue: Property = Property(name="bValue", type=BooleanType)
raspirover_BooleanValue_m_getBooleanValue: Method = Method(name="getBooleanValue", parameters={})
raspirover_BooleanValue.attributes={raspirover_BooleanValue_bValue}
raspirover_BooleanValue.methods={raspirover_BooleanValue_m_getBooleanValue}

# RoverValue class attributes and methods

# raspirover_Quantity class attributes and methods
raspirover_Quantity_value: Property = Property(name="value", type=StringType)
raspirover_Quantity_m_print: Method = Method(name="print", parameters={})
raspirover_Quantity_m_getNormalized: Method = Method(name="getNormalized", parameters={})
raspirover_Quantity.attributes={raspirover_Quantity_value}
raspirover_Quantity.methods={raspirover_Quantity_m_getNormalized, raspirover_Quantity_m_print}

# raspirover_Action class attributes and methods

# raspirover_ForwardAction class attributes and methods
raspirover_ForwardAction_m_eval: Method = Method(name="eval", parameters={})
raspirover_ForwardAction.methods={raspirover_ForwardAction_m_eval}

# Action class attributes and methods

# raspirover_ForwardMinAction class attributes and methods
raspirover_ForwardMinAction_m_eval: Method = Method(name="eval", parameters={})
raspirover_ForwardMinAction.methods={raspirover_ForwardMinAction_m_eval}

# raspirover_BackwardAction class attributes and methods
raspirover_BackwardAction_m_eval: Method = Method(name="eval", parameters={})
raspirover_BackwardAction.methods={raspirover_BackwardAction_m_eval}

# raspirover_BackwardMinAction class attributes and methods
raspirover_BackwardMinAction_m_eval: Method = Method(name="eval", parameters={})
raspirover_BackwardMinAction.methods={raspirover_BackwardMinAction_m_eval}

# raspirover_TurnAction class attributes and methods
raspirover_TurnAction_m_eval: Method = Method(name="eval", parameters={})
raspirover_TurnAction.methods={raspirover_TurnAction_m_eval}

# raspirover_TurnDegAction class attributes and methods
raspirover_TurnDegAction_m_eval: Method = Method(name="eval", parameters={})
raspirover_TurnDegAction.methods={raspirover_TurnDegAction_m_eval}

# raspirover_LogAction class attributes and methods
raspirover_LogAction_message: Property = Property(name="message", type=StringType)
raspirover_LogAction_m_eval: Method = Method(name="eval", parameters={})
raspirover_LogAction.attributes={raspirover_LogAction_message}
raspirover_LogAction.methods={raspirover_LogAction_m_eval}

# raspirover_StopAction class attributes and methods
raspirover_StopAction_m_eval: Method = Method(name="eval", parameters={})
raspirover_StopAction.methods={raspirover_StopAction_m_eval}

# raspirover_SendAction class attributes and methods
raspirover_SendAction_message: Property = Property(name="message", type=StringType)
raspirover_SendAction_m_eval: Method = Method(name="eval", parameters={})
raspirover_SendAction.attributes={raspirover_SendAction_message}
raspirover_SendAction.methods={raspirover_SendAction_m_eval}

# raspirover_VarRef class attributes and methods
raspirover_VarRef_name: Property = Property(name="name", type=FloatType)
raspirover_VarRef_m_getIntValue: Method = Method(name="getIntValue", parameters={})
raspirover_VarRef_m_getBooleanValue: Method = Method(name="getBooleanValue", parameters={})
raspirover_VarRef_m_getStringValue: Method = Method(name="getStringValue", parameters={})
raspirover_VarRef_m_eval: Method = Method(name="eval", parameters={})
raspirover_VarRef.attributes={raspirover_VarRef_name}
raspirover_VarRef.methods={raspirover_VarRef_m_getBooleanValue, raspirover_VarRef_m_getStringValue, raspirover_VarRef_m_getIntValue, raspirover_VarRef_m_eval}

# raspirover_Unit class attributes and methods
raspirover_Unit_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Unit.methods={raspirover_Unit_m_getSymbol}

# raspirover_LengthUnit class attributes and methods
raspirover_LengthUnit_m_toCm: Method = Method(name="toCm", parameters={Parameter(name='value')})
raspirover_LengthUnit.methods={raspirover_LengthUnit_m_toCm}

# Unit class attributes and methods

# raspirover_Centimeter class attributes and methods
raspirover_Centimeter_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Centimeter_m_toCm: Method = Method(name="toCm", parameters={Parameter(name='value')})
raspirover_Centimeter.methods={raspirover_Centimeter_m_getSymbol, raspirover_Centimeter_m_toCm}

# MetricSystemUnit class attributes and methods

# LengthUnit class attributes and methods

# raspirover_Millimeter class attributes and methods
raspirover_Millimeter_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Millimeter_m_toCm: Method = Method(name="toCm", parameters={Parameter(name='value')})
raspirover_Millimeter.methods={raspirover_Millimeter_m_toCm, raspirover_Millimeter_m_getSymbol}

# raspirover_Meter class attributes and methods
raspirover_Meter_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Meter_m_toCm: Method = Method(name="toCm", parameters={Parameter(name='value')})
raspirover_Meter.methods={raspirover_Meter_m_toCm, raspirover_Meter_m_getSymbol}

# raspirover_Foot class attributes and methods
raspirover_Foot_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Foot_m_toCm: Method = Method(name="toCm", parameters={Parameter(name='value')})
raspirover_Foot.methods={raspirover_Foot_m_getSymbol, raspirover_Foot_m_toCm}

# ImperialSystemUnit class attributes and methods

# raspirover_Inch class attributes and methods
raspirover_Inch_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Inch_m_toCm: Method = Method(name="toCm", parameters={Parameter(name='value')})
raspirover_Inch.methods={raspirover_Inch_m_getSymbol, raspirover_Inch_m_toCm}

# raspirover_Yard class attributes and methods
raspirover_Yard_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Yard_m_toCm: Method = Method(name="toCm", parameters={Parameter(name='value')})
raspirover_Yard.methods={raspirover_Yard_m_toCm, raspirover_Yard_m_getSymbol}

# raspirover_MetricSystemUnit class attributes and methods

# raspirover_ImperialSystemUnit class attributes and methods

# raspirover_AngleUnit class attributes and methods
raspirover_AngleUnit_m_toRad: Method = Method(name="toRad", parameters={Parameter(name='value')})
raspirover_AngleUnit.methods={raspirover_AngleUnit_m_toRad}

# raspirover_Radian class attributes and methods
raspirover_Radian_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Radian_m_toRad: Method = Method(name="toRad", parameters={Parameter(name='value')})
raspirover_Radian.methods={raspirover_Radian_m_toRad, raspirover_Radian_m_getSymbol}

# AngleUnit class attributes and methods

# raspirover_Degree class attributes and methods
raspirover_Degree_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Degree_m_toRad: Method = Method(name="toRad", parameters={Parameter(name='value')})
raspirover_Degree.methods={raspirover_Degree_m_getSymbol, raspirover_Degree_m_toRad}

# raspirover_Turn class attributes and methods
raspirover_Turn_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Turn_m_toRad: Method = Method(name="toRad", parameters={Parameter(name='value')})
raspirover_Turn.methods={raspirover_Turn_m_getSymbol, raspirover_Turn_m_toRad}

# raspirover_Gradian class attributes and methods
raspirover_Gradian_m_getSymbol: Method = Method(name="getSymbol", parameters={})
raspirover_Gradian_m_toRad: Method = Method(name="toRad", parameters={Parameter(name='value')})
raspirover_Gradian.methods={raspirover_Gradian_m_toRad, raspirover_Gradian_m_getSymbol}

# raspirover_Length class attributes and methods
raspirover_Length_m_toCm: Method = Method(name="toCm", parameters={})
raspirover_Length_m_print: Method = Method(name="print", parameters={})
raspirover_Length.methods={raspirover_Length_m_toCm, raspirover_Length_m_print}

# Quantity class attributes and methods

# raspirover_Angle class attributes and methods
raspirover_Angle_m_toRad: Method = Method(name="toRad", parameters={})
raspirover_Angle_m_print: Method = Method(name="print", parameters={})
raspirover_Angle.methods={raspirover_Angle_m_toRad, raspirover_Angle_m_print}

# raspirover_QuantityOperation class attributes and methods

# raspirover_LengthOperation class attributes and methods

# QuantityOperation class attributes and methods

# raspirover_LengthAdd class attributes and methods

# LengthOperation class attributes and methods

# QuantityHomogenousOperation class attributes and methods

# raspirover_LengthSubtract class attributes and methods

# raspirover_LengthScalarMultiply class attributes and methods

# QuantityScalarOperation class attributes and methods

# raspirover_LengthScalarDivide class attributes and methods

# raspirover_LengthEquals class attributes and methods

# raspirover_LengthDistinct class attributes and methods

# raspirover_LengthSmaller class attributes and methods

# raspirover_LengthGreater class attributes and methods

# raspirover_AngleOperation class attributes and methods

# raspirover_AngleAdd class attributes and methods

# AngleOperation class attributes and methods

# raspirover_AngleSubtract class attributes and methods

# raspirover_AngleScalarMultiply class attributes and methods

# raspirover_AngleScalarDivide class attributes and methods

# raspirover_AngleEquals class attributes and methods

# raspirover_AngleDistinct class attributes and methods

# raspirover_AngleSmaller class attributes and methods

# raspirover_AngleGreater class attributes and methods

# raspirover_QuantityArithmeticOperation class attributes and methods

# raspirover_QuantityComparisonOperation class attributes and methods

# raspirover_QuantityHomogenousOperation class attributes and methods

# raspirover_QuantityScalarOperation class attributes and methods
raspirover_QuantityScalarOperation_rhs: Property = Property(name="rhs", type=FloatType)
raspirover_QuantityScalarOperation.attributes={raspirover_QuantityScalarOperation_rhs}

# Relationships
digitalPins0: BinaryAssociation = BinaryAssociation(
    name="digitalPins0",
    ends={
        Property(name="raspirover_DigitalPin", type=raspirover_RasPiBoard, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_RasPiBoard", type=raspirover_DigitalPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
analogPins1: BinaryAssociation = BinaryAssociation(
    name="analogPins1",
    ends={
        Property(name="raspirover_AnalogPin", type=raspirover_RasPiBoard, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_RasPiBoard2", type=raspirover_AnalogPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project3: BinaryAssociation = BinaryAssociation(
    name="project3",
    ends={
        Property(name="4", type=raspirover_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=raspirover_Project, multiplicity=Multiplicity(1, 1))
    }
)
params24: BinaryAssociation = BinaryAssociation(
    name="params24",
    ends={
        Property(name="raspirover_Param", type=raspirover_RoverProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_RoverProgram25", type=raspirover_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boards5: BinaryAssociation = BinaryAssociation(
    name="boards5",
    ends={
        Property(name="7", type=raspirover_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=raspirover_Board, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sketches8: BinaryAssociation = BinaryAssociation(
    name="sketches8",
    ends={
        Property(name="10", type=raspirover_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=raspirover_Sketch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program11: BinaryAssociation = BinaryAssociation(
    name="program11",
    ends={
        Property(name="raspirover_RoverProgram", type=raspirover_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Project", type=raspirover_RoverProgram, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
project12: BinaryAssociation = BinaryAssociation(
    name="project12",
    ends={
        Property(name="14", type=raspirover_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=raspirover_Project, multiplicity=Multiplicity(1, 1))
    }
)
block15: BinaryAssociation = BinaryAssociation(
    name="block15",
    ends={
        Property(name="raspirover_Block", type=raspirover_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Sketch", type=raspirover_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
board16: BinaryAssociation = BinaryAssociation(
    name="board16",
    ends={
        Property(name="raspirover_Board", type=raspirover_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Sketch17", type=raspirover_Board, multiplicity=Multiplicity(0, 1))
    }
)
instructions18: BinaryAssociation = BinaryAssociation(
    name="instructions18",
    ends={
        Property(name="raspirover_Instruction", type=raspirover_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Block19", type=raspirover_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module20: BinaryAssociation = BinaryAssociation(
    name="module20",
    ends={
        Property(name="raspirover_ArduinoDigitalModule", type=raspirover_DigitalPin, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_DigitalPin21", type=raspirover_ArduinoDigitalModule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
module22: BinaryAssociation = BinaryAssociation(
    name="module22",
    ends={
        Property(name="raspirover_ArduinoAnalogModule", type=raspirover_AnalogPin, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_AnalogPin23", type=raspirover_ArduinoAnalogModule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block26: BinaryAssociation = BinaryAssociation(
    name="block26",
    ends={
        Property(name="raspirover_RclBlock", type=raspirover_RoverProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_RoverProgram27", type=raspirover_RclBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enclosing28: BinaryAssociation = BinaryAssociation(
    name="enclosing28",
    ends={
        Property(name="30", type=raspirover_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="29", type=raspirover_RclBlock, multiplicity=Multiplicity(0, 1))
    }
)
value31: BinaryAssociation = BinaryAssociation(
    name="value31",
    ends={
        Property(name="raspirover_RoverValue", type=raspirover_VarAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_VarAssignment", type=raspirover_RoverValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr32: BinaryAssociation = BinaryAssociation(
    name="expr32",
    ends={
        Property(name="raspirover_RoverExpression", type=raspirover_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Conditional", type=raspirover_RoverExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condTrue33: BinaryAssociation = BinaryAssociation(
    name="condTrue33",
    ends={
        Property(name="raspirover_RclBlock35", type=raspirover_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Conditional34", type=raspirover_RclBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condFalse36: BinaryAssociation = BinaryAssociation(
    name="condFalse36",
    ends={
        Property(name="raspirover_RclBlock38", type=raspirover_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Conditional37", type=raspirover_RclBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr39: BinaryAssociation = BinaryAssociation(
    name="expr39",
    ends={
        Property(name="raspirover_RoverExpression40", type=raspirover_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Loop", type=raspirover_RoverExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block41: BinaryAssociation = BinaryAssociation(
    name="block41",
    ends={
        Property(name="raspirover_RclBlock43", type=raspirover_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Loop42", type=raspirover_RclBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmts44: BinaryAssociation = BinaryAssociation(
    name="stmts44",
    ends={
        Property(name="46", type=raspirover_RclBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="45", type=raspirover_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs47: BinaryAssociation = BinaryAssociation(
    name="lhs47",
    ends={
        Property(name="raspirover_NumberValue", type=raspirover_NumericExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_NumericExpression", type=raspirover_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs48: BinaryAssociation = BinaryAssociation(
    name="rhs48",
    ends={
        Property(name="raspirover_NumberValue50", type=raspirover_NumericExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_NumericExpression49", type=raspirover_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs51: BinaryAssociation = BinaryAssociation(
    name="lhs51",
    ends={
        Property(name="raspirover_StringValue", type=raspirover_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_StringExpression", type=raspirover_StringValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs52: BinaryAssociation = BinaryAssociation(
    name="rhs52",
    ends={
        Property(name="raspirover_StringValue54", type=raspirover_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_StringExpression53", type=raspirover_StringValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs55: BinaryAssociation = BinaryAssociation(
    name="lhs55",
    ends={
        Property(name="raspirover_BooleanValue", type=raspirover_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_BooleanExpression", type=raspirover_BooleanValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs56: BinaryAssociation = BinaryAssociation(
    name="rhs56",
    ends={
        Property(name="raspirover_BooleanValue58", type=raspirover_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_BooleanExpression57", type=raspirover_BooleanValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
quantity59: BinaryAssociation = BinaryAssociation(
    name="quantity59",
    ends={
        Property(name="raspirover_Quantity", type=raspirover_NumberValue, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_NumberValue60", type=raspirover_Quantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associatedPin61: BinaryAssociation = BinaryAssociation(
    name="associatedPin61",
    ends={
        Property(name="raspirover_Pin", type=raspirover_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Action", type=raspirover_Pin, multiplicity=Multiplicity(0, 1))
    }
)
distance62: BinaryAssociation = BinaryAssociation(
    name="distance62",
    ends={
        Property(name="raspirover_NumberValue63", type=raspirover_ForwardMinAction, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_ForwardMinAction", type=raspirover_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
distance64: BinaryAssociation = BinaryAssociation(
    name="distance64",
    ends={
        Property(name="raspirover_NumberValue65", type=raspirover_BackwardMinAction, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_BackwardMinAction", type=raspirover_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
degrees66: BinaryAssociation = BinaryAssociation(
    name="degrees66",
    ends={
        Property(name="raspirover_NumberValue67", type=raspirover_TurnDegAction, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_TurnDegAction", type=raspirover_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unit68: BinaryAssociation = BinaryAssociation(
    name="unit68",
    ends={
        Property(name="raspirover_Unit", type=raspirover_Quantity, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_Quantity69", type=raspirover_Unit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs70: BinaryAssociation = BinaryAssociation(
    name="lhs70",
    ends={
        Property(name="raspirover_Quantity71", type=raspirover_QuantityHomogenousOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_QuantityHomogenousOperation", type=raspirover_Quantity, multiplicity=Multiplicity(1, 1))
    }
)
rhs72: BinaryAssociation = BinaryAssociation(
    name="rhs72",
    ends={
        Property(name="raspirover_Quantity74", type=raspirover_QuantityHomogenousOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_QuantityHomogenousOperation73", type=raspirover_Quantity, multiplicity=Multiplicity(1, 1))
    }
)
lhs75: BinaryAssociation = BinaryAssociation(
    name="lhs75",
    ends={
        Property(name="raspirover_Quantity76", type=raspirover_QuantityScalarOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="raspirover_QuantityScalarOperation", type=raspirover_Quantity, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_raspirover_RasPiBoard_Board = Generalization(general=Board, specific=raspirover_RasPiBoard)
gen_raspirover_Board_NamedElement = Generalization(general=NamedElement, specific=raspirover_Board)
gen_raspirover_Sketch_NamedElement = Generalization(general=NamedElement, specific=raspirover_Sketch)
gen_raspirover_DigitalPin_Pin = Generalization(general=Pin, specific=raspirover_DigitalPin)
gen_raspirover_Pin_NamedElement = Generalization(general=NamedElement, specific=raspirover_Pin)
gen_raspirover_ArduinoDigitalModule_ArduinoModule = Generalization(general=ArduinoModule, specific=raspirover_ArduinoDigitalModule)
gen_raspirover_ArduinoModule_Module = Generalization(general=Module, specific=raspirover_ArduinoModule)
gen_raspirover_Module_NamedElement = Generalization(general=NamedElement, specific=raspirover_Module)
gen_raspirover_AnalogPin_Pin = Generalization(general=Pin, specific=raspirover_AnalogPin)
gen_raspirover_ArduinoAnalogModule_ArduinoModule = Generalization(general=ArduinoModule, specific=raspirover_ArduinoAnalogModule)
gen_raspirover_HumidityQuery_Query = Generalization(general=Query, specific=raspirover_HumidityQuery)
gen_raspirover_HumidityQuery_NumberValue = Generalization(general=NumberValue, specific=raspirover_HumidityQuery)
gen_raspirover_VarAssignment_Statement = Generalization(general=Statement, specific=raspirover_VarAssignment)
gen_raspirover_Conditional_Statement = Generalization(general=Statement, specific=raspirover_Conditional)
gen_raspirover_Loop_Statement = Generalization(general=Statement, specific=raspirover_Loop)
gen_raspirover_RclBlock_Statement = Generalization(general=Statement, specific=raspirover_RclBlock)
gen_raspirover_TemperatureQuery_Query = Generalization(general=Query, specific=raspirover_TemperatureQuery)
gen_raspirover_TemperatureQuery_NumberValue = Generalization(general=NumberValue, specific=raspirover_TemperatureQuery)
gen_raspirover_StringValue_RoverValue = Generalization(general=RoverValue, specific=raspirover_StringValue)
gen_raspirover_BooleanValue_RoverValue = Generalization(general=RoverValue, specific=raspirover_BooleanValue)
gen_raspirover_MessageQuery_Query = Generalization(general=Query, specific=raspirover_MessageQuery)
gen_raspirover_MessageQuery_StringValue = Generalization(general=StringValue, specific=raspirover_MessageQuery)
gen_raspirover_ObstacleQuery_Query = Generalization(general=Query, specific=raspirover_ObstacleQuery)
gen_raspirover_ObstacleQuery_BooleanValue = Generalization(general=BooleanValue, specific=raspirover_ObstacleQuery)
gen_raspirover_NumericExpression_RoverExpression = Generalization(general=RoverExpression, specific=raspirover_NumericExpression)
gen_raspirover_StringExpression_RoverExpression = Generalization(general=RoverExpression, specific=raspirover_StringExpression)
gen_raspirover_BooleanExpression_RoverExpression = Generalization(general=RoverExpression, specific=raspirover_BooleanExpression)
gen_raspirover_NumberValue_RoverValue = Generalization(general=RoverValue, specific=raspirover_NumberValue)
gen_raspirover_Action_Statement = Generalization(general=Statement, specific=raspirover_Action)
gen_raspirover_ForwardAction_Action = Generalization(general=Action, specific=raspirover_ForwardAction)
gen_raspirover_ForwardMinAction_Action = Generalization(general=Action, specific=raspirover_ForwardMinAction)
gen_raspirover_BackwardAction_Action = Generalization(general=Action, specific=raspirover_BackwardAction)
gen_raspirover_BackwardMinAction_Action = Generalization(general=Action, specific=raspirover_BackwardMinAction)
gen_raspirover_TurnAction_Action = Generalization(general=Action, specific=raspirover_TurnAction)
gen_raspirover_TurnDegAction_Action = Generalization(general=Action, specific=raspirover_TurnDegAction)
gen_raspirover_LogAction_Action = Generalization(general=Action, specific=raspirover_LogAction)
gen_raspirover_StopAction_Action = Generalization(general=Action, specific=raspirover_StopAction)
gen_raspirover_SendAction_Action = Generalization(general=Action, specific=raspirover_SendAction)
gen_raspirover_VarRef_BooleanValue = Generalization(general=BooleanValue, specific=raspirover_VarRef)
gen_raspirover_VarRef_NumberValue = Generalization(general=NumberValue, specific=raspirover_VarRef)
gen_raspirover_VarRef_StringValue = Generalization(general=StringValue, specific=raspirover_VarRef)
gen_raspirover_VarRef_Statement = Generalization(general=Statement, specific=raspirover_VarRef)
gen_raspirover_LengthUnit_Unit = Generalization(general=Unit, specific=raspirover_LengthUnit)
gen_raspirover_Centimeter_MetricSystemUnit = Generalization(general=MetricSystemUnit, specific=raspirover_Centimeter)
gen_raspirover_Centimeter_LengthUnit = Generalization(general=LengthUnit, specific=raspirover_Centimeter)
gen_raspirover_Millimeter_MetricSystemUnit = Generalization(general=MetricSystemUnit, specific=raspirover_Millimeter)
gen_raspirover_Millimeter_LengthUnit = Generalization(general=LengthUnit, specific=raspirover_Millimeter)
gen_raspirover_Meter_MetricSystemUnit = Generalization(general=MetricSystemUnit, specific=raspirover_Meter)
gen_raspirover_Meter_LengthUnit = Generalization(general=LengthUnit, specific=raspirover_Meter)
gen_raspirover_Foot_ImperialSystemUnit = Generalization(general=ImperialSystemUnit, specific=raspirover_Foot)
gen_raspirover_Foot_LengthUnit = Generalization(general=LengthUnit, specific=raspirover_Foot)
gen_raspirover_Inch_ImperialSystemUnit = Generalization(general=ImperialSystemUnit, specific=raspirover_Inch)
gen_raspirover_Inch_LengthUnit = Generalization(general=LengthUnit, specific=raspirover_Inch)
gen_raspirover_Yard_ImperialSystemUnit = Generalization(general=ImperialSystemUnit, specific=raspirover_Yard)
gen_raspirover_Yard_LengthUnit = Generalization(general=LengthUnit, specific=raspirover_Yard)
gen_raspirover_MetricSystemUnit_Unit = Generalization(general=Unit, specific=raspirover_MetricSystemUnit)
gen_raspirover_ImperialSystemUnit_Unit = Generalization(general=Unit, specific=raspirover_ImperialSystemUnit)
gen_raspirover_AngleUnit_Unit = Generalization(general=Unit, specific=raspirover_AngleUnit)
gen_raspirover_Radian_AngleUnit = Generalization(general=AngleUnit, specific=raspirover_Radian)
gen_raspirover_Degree_AngleUnit = Generalization(general=AngleUnit, specific=raspirover_Degree)
gen_raspirover_Turn_AngleUnit = Generalization(general=AngleUnit, specific=raspirover_Turn)
gen_raspirover_Gradian_AngleUnit = Generalization(general=AngleUnit, specific=raspirover_Gradian)
gen_raspirover_Length_Quantity = Generalization(general=Quantity, specific=raspirover_Length)
gen_raspirover_Angle_Quantity = Generalization(general=Quantity, specific=raspirover_Angle)
gen_raspirover_LengthOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=raspirover_LengthOperation)
gen_raspirover_LengthAdd_LengthOperation = Generalization(general=LengthOperation, specific=raspirover_LengthAdd)
gen_raspirover_LengthAdd_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_LengthAdd)
gen_raspirover_LengthSubtract_LengthOperation = Generalization(general=LengthOperation, specific=raspirover_LengthSubtract)
gen_raspirover_LengthSubtract_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_LengthSubtract)
gen_raspirover_LengthScalarMultiply_LengthOperation = Generalization(general=LengthOperation, specific=raspirover_LengthScalarMultiply)
gen_raspirover_LengthScalarMultiply_QuantityScalarOperation = Generalization(general=QuantityScalarOperation, specific=raspirover_LengthScalarMultiply)
gen_raspirover_LengthScalarDivide_LengthOperation = Generalization(general=LengthOperation, specific=raspirover_LengthScalarDivide)
gen_raspirover_LengthScalarDivide_QuantityScalarOperation = Generalization(general=QuantityScalarOperation, specific=raspirover_LengthScalarDivide)
gen_raspirover_LengthEquals_LengthOperation = Generalization(general=LengthOperation, specific=raspirover_LengthEquals)
gen_raspirover_LengthEquals_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_LengthEquals)
gen_raspirover_LengthDistinct_LengthOperation = Generalization(general=LengthOperation, specific=raspirover_LengthDistinct)
gen_raspirover_LengthDistinct_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_LengthDistinct)
gen_raspirover_LengthSmaller_LengthOperation = Generalization(general=LengthOperation, specific=raspirover_LengthSmaller)
gen_raspirover_LengthSmaller_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_LengthSmaller)
gen_raspirover_LengthGreater_LengthOperation = Generalization(general=LengthOperation, specific=raspirover_LengthGreater)
gen_raspirover_LengthGreater_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_LengthGreater)
gen_raspirover_AngleOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=raspirover_AngleOperation)
gen_raspirover_AngleAdd_AngleOperation = Generalization(general=AngleOperation, specific=raspirover_AngleAdd)
gen_raspirover_AngleAdd_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_AngleAdd)
gen_raspirover_AngleSubtract_AngleOperation = Generalization(general=AngleOperation, specific=raspirover_AngleSubtract)
gen_raspirover_AngleSubtract_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_AngleSubtract)
gen_raspirover_AngleScalarMultiply_AngleOperation = Generalization(general=AngleOperation, specific=raspirover_AngleScalarMultiply)
gen_raspirover_AngleScalarMultiply_QuantityScalarOperation = Generalization(general=QuantityScalarOperation, specific=raspirover_AngleScalarMultiply)
gen_raspirover_AngleScalarDivide_AngleOperation = Generalization(general=AngleOperation, specific=raspirover_AngleScalarDivide)
gen_raspirover_AngleScalarDivide_QuantityScalarOperation = Generalization(general=QuantityScalarOperation, specific=raspirover_AngleScalarDivide)
gen_raspirover_AngleEquals_AngleOperation = Generalization(general=AngleOperation, specific=raspirover_AngleEquals)
gen_raspirover_AngleEquals_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_AngleEquals)
gen_raspirover_AngleDistinct_AngleOperation = Generalization(general=AngleOperation, specific=raspirover_AngleDistinct)
gen_raspirover_AngleDistinct_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_AngleDistinct)
gen_raspirover_AngleSmaller_AngleOperation = Generalization(general=AngleOperation, specific=raspirover_AngleSmaller)
gen_raspirover_AngleSmaller_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_AngleSmaller)
gen_raspirover_AngleGreater_AngleOperation = Generalization(general=AngleOperation, specific=raspirover_AngleGreater)
gen_raspirover_AngleGreater_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=raspirover_AngleGreater)
gen_raspirover_QuantityArithmeticOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=raspirover_QuantityArithmeticOperation)
gen_raspirover_QuantityComparisonOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=raspirover_QuantityComparisonOperation)
gen_raspirover_QuantityHomogenousOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=raspirover_QuantityHomogenousOperation)
gen_raspirover_QuantityScalarOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=raspirover_QuantityScalarOperation)

# Domain Model
domain_model = DomainModel(
    name="raspirover",
    types={raspirover_RasPiBoard, Board, raspirover_DigitalPin, raspirover_AnalogPin, raspirover_Board, NamedElement, raspirover_Project, raspirover_NamedElement, raspirover_Param, raspirover_RclBlock, raspirover_Sketch, raspirover_RoverProgram, raspirover_Block, raspirover_Instruction, Pin, raspirover_ArduinoDigitalModule, raspirover_Pin, ArduinoModule, raspirover_ArduinoModule, Module, raspirover_Module, raspirover_ArduinoAnalogModule, raspirover_HumidityQuery, raspirover_Statement, raspirover_VarAssignment, Statement, raspirover_RoverValue, raspirover_Conditional, raspirover_RoverExpression, raspirover_Loop, raspirover_Query, raspirover_TemperatureQuery, Query, NumberValue, raspirover_MessageQuery, StringValue, raspirover_ObstacleQuery, BooleanValue, raspirover_NumericExpression, RoverExpression, raspirover_NumberValue, raspirover_StringExpression, raspirover_StringValue, raspirover_BooleanExpression, raspirover_BooleanValue, RoverValue, raspirover_Quantity, raspirover_Action, raspirover_ForwardAction, Action, raspirover_ForwardMinAction, raspirover_BackwardAction, raspirover_BackwardMinAction, raspirover_TurnAction, raspirover_TurnDegAction, raspirover_LogAction, raspirover_StopAction, raspirover_SendAction, raspirover_VarRef, raspirover_Unit, raspirover_LengthUnit, Unit, raspirover_Centimeter, MetricSystemUnit, LengthUnit, raspirover_Millimeter, raspirover_Meter, raspirover_Foot, ImperialSystemUnit, raspirover_Inch, raspirover_Yard, raspirover_MetricSystemUnit, raspirover_ImperialSystemUnit, raspirover_AngleUnit, raspirover_Radian, AngleUnit, raspirover_Degree, raspirover_Turn, raspirover_Gradian, raspirover_Length, Quantity, raspirover_Angle, raspirover_QuantityOperation, raspirover_LengthOperation, QuantityOperation, raspirover_LengthAdd, LengthOperation, QuantityHomogenousOperation, raspirover_LengthSubtract, raspirover_LengthScalarMultiply, QuantityScalarOperation, raspirover_LengthScalarDivide, raspirover_LengthEquals, raspirover_LengthDistinct, raspirover_LengthSmaller, raspirover_LengthGreater, raspirover_AngleOperation, raspirover_AngleAdd, AngleOperation, raspirover_AngleSubtract, raspirover_AngleScalarMultiply, raspirover_AngleScalarDivide, raspirover_AngleEquals, raspirover_AngleDistinct, raspirover_AngleSmaller, raspirover_AngleGreater, raspirover_QuantityArithmeticOperation, raspirover_QuantityComparisonOperation, raspirover_QuantityHomogenousOperation, raspirover_QuantityScalarOperation, NumericOperator, StringOperator, BooleanOperator},
    associations={digitalPins0, analogPins1, project3, params24, boards5, sketches8, program11, project12, block15, board16, instructions18, module20, module22, block26, enclosing28, value31, expr32, condTrue33, condFalse36, expr39, block41, stmts44, lhs47, rhs48, lhs51, rhs52, lhs55, rhs56, quantity59, associatedPin61, distance62, distance64, degrees66, unit68, lhs70, rhs72, lhs75},
    generalizations={gen_raspirover_RasPiBoard_Board, gen_raspirover_Board_NamedElement, gen_raspirover_Sketch_NamedElement, gen_raspirover_DigitalPin_Pin, gen_raspirover_Pin_NamedElement, gen_raspirover_ArduinoDigitalModule_ArduinoModule, gen_raspirover_ArduinoModule_Module, gen_raspirover_Module_NamedElement, gen_raspirover_AnalogPin_Pin, gen_raspirover_ArduinoAnalogModule_ArduinoModule, gen_raspirover_HumidityQuery_Query, gen_raspirover_HumidityQuery_NumberValue, gen_raspirover_VarAssignment_Statement, gen_raspirover_Conditional_Statement, gen_raspirover_Loop_Statement, gen_raspirover_RclBlock_Statement, gen_raspirover_TemperatureQuery_Query, gen_raspirover_TemperatureQuery_NumberValue, gen_raspirover_StringValue_RoverValue, gen_raspirover_BooleanValue_RoverValue, gen_raspirover_MessageQuery_Query, gen_raspirover_MessageQuery_StringValue, gen_raspirover_ObstacleQuery_Query, gen_raspirover_ObstacleQuery_BooleanValue, gen_raspirover_NumericExpression_RoverExpression, gen_raspirover_StringExpression_RoverExpression, gen_raspirover_BooleanExpression_RoverExpression, gen_raspirover_NumberValue_RoverValue, gen_raspirover_Action_Statement, gen_raspirover_ForwardAction_Action, gen_raspirover_ForwardMinAction_Action, gen_raspirover_BackwardAction_Action, gen_raspirover_BackwardMinAction_Action, gen_raspirover_TurnAction_Action, gen_raspirover_TurnDegAction_Action, gen_raspirover_LogAction_Action, gen_raspirover_StopAction_Action, gen_raspirover_SendAction_Action, gen_raspirover_VarRef_BooleanValue, gen_raspirover_VarRef_NumberValue, gen_raspirover_VarRef_StringValue, gen_raspirover_VarRef_Statement, gen_raspirover_LengthUnit_Unit, gen_raspirover_Centimeter_MetricSystemUnit, gen_raspirover_Centimeter_LengthUnit, gen_raspirover_Millimeter_MetricSystemUnit, gen_raspirover_Millimeter_LengthUnit, gen_raspirover_Meter_MetricSystemUnit, gen_raspirover_Meter_LengthUnit, gen_raspirover_Foot_ImperialSystemUnit, gen_raspirover_Foot_LengthUnit, gen_raspirover_Inch_ImperialSystemUnit, gen_raspirover_Inch_LengthUnit, gen_raspirover_Yard_ImperialSystemUnit, gen_raspirover_Yard_LengthUnit, gen_raspirover_MetricSystemUnit_Unit, gen_raspirover_ImperialSystemUnit_Unit, gen_raspirover_AngleUnit_Unit, gen_raspirover_Radian_AngleUnit, gen_raspirover_Degree_AngleUnit, gen_raspirover_Turn_AngleUnit, gen_raspirover_Gradian_AngleUnit, gen_raspirover_Length_Quantity, gen_raspirover_Angle_Quantity, gen_raspirover_LengthOperation_QuantityOperation, gen_raspirover_LengthAdd_LengthOperation, gen_raspirover_LengthAdd_QuantityHomogenousOperation, gen_raspirover_LengthSubtract_LengthOperation, gen_raspirover_LengthSubtract_QuantityHomogenousOperation, gen_raspirover_LengthScalarMultiply_LengthOperation, gen_raspirover_LengthScalarMultiply_QuantityScalarOperation, gen_raspirover_LengthScalarDivide_LengthOperation, gen_raspirover_LengthScalarDivide_QuantityScalarOperation, gen_raspirover_LengthEquals_LengthOperation, gen_raspirover_LengthEquals_QuantityHomogenousOperation, gen_raspirover_LengthDistinct_LengthOperation, gen_raspirover_LengthDistinct_QuantityHomogenousOperation, gen_raspirover_LengthSmaller_LengthOperation, gen_raspirover_LengthSmaller_QuantityHomogenousOperation, gen_raspirover_LengthGreater_LengthOperation, gen_raspirover_LengthGreater_QuantityHomogenousOperation, gen_raspirover_AngleOperation_QuantityOperation, gen_raspirover_AngleAdd_AngleOperation, gen_raspirover_AngleAdd_QuantityHomogenousOperation, gen_raspirover_AngleSubtract_AngleOperation, gen_raspirover_AngleSubtract_QuantityHomogenousOperation, gen_raspirover_AngleScalarMultiply_AngleOperation, gen_raspirover_AngleScalarMultiply_QuantityScalarOperation, gen_raspirover_AngleScalarDivide_AngleOperation, gen_raspirover_AngleScalarDivide_QuantityScalarOperation, gen_raspirover_AngleEquals_AngleOperation, gen_raspirover_AngleEquals_QuantityHomogenousOperation, gen_raspirover_AngleDistinct_AngleOperation, gen_raspirover_AngleDistinct_QuantityHomogenousOperation, gen_raspirover_AngleSmaller_AngleOperation, gen_raspirover_AngleSmaller_QuantityHomogenousOperation, gen_raspirover_AngleGreater_AngleOperation, gen_raspirover_AngleGreater_QuantityHomogenousOperation, gen_raspirover_QuantityArithmeticOperation_QuantityOperation, gen_raspirover_QuantityComparisonOperation_QuantityOperation, gen_raspirover_QuantityHomogenousOperation_QuantityOperation, gen_raspirover_QuantityScalarOperation_QuantityOperation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)