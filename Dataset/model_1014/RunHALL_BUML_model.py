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
HALL_UserProfile = Class(name="HALL_UserProfile")
HALL_Component = Class(name="HALL_Component", is_abstract=True)
HALL_Data = Class(name="HALL_Data")
FSM = Class(name="FSM")
MessageHandler = Class(name="MessageHandler")
HALL_SystemComponent = Class(name="HALL_SystemComponent")
HALL_Model = Class(name="HALL_Model")
HALL_VisualObject = Class(name="HALL_VisualObject")
Component = Class(name="Component")
ColorData = Class(name="ColorData")
GeometryData = Class(name="GeometryData")
HALL_TaskObject = Class(name="HALL_TaskObject")
HALL_Goal = Class(name="HALL_Goal")
MessageDefinition = Class(name="MessageDefinition")
HALL_Geometry_Color = Class(name="HALL_Geometry_Color")
RGBColor = Class(name="RGBColor")
ColorState = Class(name="ColorState")
HALL_Geometry_RGBColor = Class(name="HALL_Geometry_RGBColor")
Color = Class(name="Color")
HALL_Parameter = Class(name="HALL_Parameter")
HALL_Geometry_SelectedColors = Class(name="HALL_Geometry_SelectedColors")
HALL_Geometry_DisabledColors = Class(name="HALL_Geometry_DisabledColors")
HALL_Geometry_ColorData = Class(name="HALL_Geometry_ColorData")
SelectedColors = Class(name="SelectedColors")
DisabledColors = Class(name="DisabledColors")
NormalColors = Class(name="NormalColors")
Geometry_HALL_VisualObject = Class(name="Geometry_HALL_VisualObject")
HALL_Geometry_GeometryData = Class(name="HALL_Geometry_GeometryData", is_abstract=True)
HALL_Geometry_GeometryData3D = Class(name="HALL_Geometry_GeometryData3D")
Face = Class(name="Face")
HALL_Geometry_ColorState = Class(name="HALL_Geometry_ColorState", is_abstract=True)
AlphaTransparency = Class(name="AlphaTransparency")
HALL_Geometry_AlphaTransparency = Class(name="HALL_Geometry_AlphaTransparency")
HALL_Geometry_NormalColors = Class(name="HALL_Geometry_NormalColors")
HALL_Geometry_Point = Class(name="HALL_Geometry_Point")
HALL_Messages_MessageTransition = Class(name="HALL_Messages_MessageTransition")
MessageState = Class(name="MessageState")
Conditions_PreConditionMessageExpression = Class(name="Conditions_PreConditionMessageExpression")
Instructions_PosConditionMessageExpression = Class(name="Instructions_PosConditionMessageExpression")
Actions_ActionMessageExpression = Class(name="Actions_ActionMessageExpression")
HALL_Messages_NamedMessageState = Class(name="HALL_Messages_NamedMessageState")
HALL_Messages_MessageDefinition = Class(name="HALL_Messages_MessageDefinition")
Messages_HALL_Model = Class(name="Messages_HALL_Model")
Messages_HALL_Parameter = Class(name="Messages_HALL_Parameter")
HALL_Geometry_GeometryData2D = Class(name="HALL_Geometry_GeometryData2D")
Point2D = Class(name="Point2D")
HALL_Geometry_Face = Class(name="HALL_Geometry_Face")
Point3D = Class(name="Point3D")
GeometryData3D = Class(name="GeometryData3D")
HALL_Geometry_Point3D = Class(name="HALL_Geometry_Point3D")
Point = Class(name="Point")
HALL_Geometry_Point2D = Class(name="HALL_Geometry_Point2D")
GeometryData2D = Class(name="GeometryData2D")
Instructions_PosConditionMessageExpressionElement = Class(name="Instructions_PosConditionMessageExpressionElement")
HALL_Instructions_PosConditionMessageExpressionElement = Class(name="HALL_Instructions_PosConditionMessageExpressionElement", is_abstract=True)
HALL_Instructions_VarRef = Class(name="HALL_Instructions_VarRef")
PosConditionMessageExpressionElement = Class(name="PosConditionMessageExpressionElement")
HALL_Instructions_Literal = Class(name="HALL_Instructions_Literal")
HALL_Instructions_BinaryOperator = Class(name="HALL_Instructions_BinaryOperator")
HALL_Instructions_UnaryOperator = Class(name="HALL_Instructions_UnaryOperator")
HALL_Instructions_GetData = Class(name="HALL_Instructions_GetData")
Instructions_HALL_Component = Class(name="Instructions_HALL_Component")
Messages_HALL_Data = Class(name="Messages_HALL_Data")
HALL_Messages_MessageHandler = Class(name="HALL_Messages_MessageHandler")
NamedMessageState = Class(name="NamedMessageState")
InitialMessageState = Class(name="InitialMessageState")
Messages_HALL_Component = Class(name="Messages_HALL_Component")
HALL_Messages_MessageState = Class(name="HALL_Messages_MessageState")
MessageTransition = Class(name="MessageTransition")
HALL_Messages_InitialMessageState = Class(name="HALL_Messages_InitialMessageState")
HALL_Instructions_PosConditionMessageExpression = Class(name="HALL_Instructions_PosConditionMessageExpression", is_abstract=True)
HALL_Instructions_Let = Class(name="HALL_Instructions_Let")
HALL_Instructions_DomainPropertyGet = Class(name="HALL_Instructions_DomainPropertyGet")
HALL_Instructions_GetMessageData = Class(name="HALL_Instructions_GetMessageData")
HALL_Instructions_GetMessageParameter = Class(name="HALL_Instructions_GetMessageParameter")
HALL_Instructions_SetTopDown = Class(name="HALL_Instructions_SetTopDown")
HALL_Conditions_PreConditionMessageExpression = Class(name="HALL_Conditions_PreConditionMessageExpression", is_abstract=True)
HALL_Instructions_GetState = Class(name="HALL_Instructions_GetState")
HALL_Instructions_SetState = Class(name="HALL_Instructions_SetState")
HALL_Instructions_SetData = Class(name="HALL_Instructions_SetData")
HALL_Instructions_SetMessageData = Class(name="HALL_Instructions_SetMessageData")
HALL_Instructions_SetMessageParameter = Class(name="HALL_Instructions_SetMessageParameter")
HALL_Conditions_Let = Class(name="HALL_Conditions_Let")
HALL_Conditions_UnaryOperator = Class(name="HALL_Conditions_UnaryOperator")
HALL_Conditions_BinaryOperator = Class(name="HALL_Conditions_BinaryOperator")
HALL_Actions_ActionMessageExpression = Class(name="HALL_Actions_ActionMessageExpression", is_abstract=True)
Actions_ActionMessageExpressionElement = Class(name="Actions_ActionMessageExpressionElement")
Conditions_PreConditionMessageExpressionElement = Class(name="Conditions_PreConditionMessageExpressionElement")
HALL_Conditions_PreConditionMessageExpressionElement = Class(name="HALL_Conditions_PreConditionMessageExpressionElement", is_abstract=True)
HALL_Conditions_VarRef = Class(name="HALL_Conditions_VarRef")
PreConditionMessageExpressionElement = Class(name="PreConditionMessageExpressionElement")
HALL_Conditions_Literal = Class(name="HALL_Conditions_Literal")
HALL_Conditions_GetMessageData = Class(name="HALL_Conditions_GetMessageData")
HALL_Conditions_GetMessageParameter = Class(name="HALL_Conditions_GetMessageParameter")
HALL_Conditions_DomainPropertyGet = Class(name="HALL_Conditions_DomainPropertyGet")
HALL_Conditions_GetState = Class(name="HALL_Conditions_GetState")
Conditions_HALL_Component = Class(name="Conditions_HALL_Component")
HALL_Conditions_GetData = Class(name="HALL_Conditions_GetData")
HALL_Actions_GetMessageData = Class(name="HALL_Actions_GetMessageData")
HALL_Actions_GetMessageParameter = Class(name="HALL_Actions_GetMessageParameter")
HALL_Actions_MessageInvocation = Class(name="HALL_Actions_MessageInvocation")
HALL_Actions_UnaryOperator = Class(name="HALL_Actions_UnaryOperator")
HALL_Actions_GetData = Class(name="HALL_Actions_GetData")
Actions_HALL_Component = Class(name="Actions_HALL_Component")
HALL_Actions_DomainPropertySet = Class(name="HALL_Actions_DomainPropertySet")
HALL_Actions_Enable = Class(name="HALL_Actions_Enable")
HALL_Actions_ActionMessageExpressionElement = Class(name="HALL_Actions_ActionMessageExpressionElement", is_abstract=True)
HALL_Actions_VarRef = Class(name="HALL_Actions_VarRef")
ActionMessageExpressionElement = Class(name="ActionMessageExpressionElement")
HALL_Actions_Literal = Class(name="HALL_Actions_Literal")
HALL_Actions_BinaryOperator = Class(name="HALL_Actions_BinaryOperator")
HALL_Actions_Let = Class(name="HALL_Actions_Let")
HALL_Actions_DomainPropertyGet = Class(name="HALL_Actions_DomainPropertyGet")
HALL_FSM_Transition = Class(name="HALL_FSM_Transition")
FSMConditions_PreConditionExpression = Class(name="FSMConditions_PreConditionExpression")
FSMInstructions_PosConditionExpression = Class(name="FSMInstructions_PosConditionExpression")
FSMActions_ActionExpression = Class(name="FSMActions_ActionExpression")
Trigger_TriggerExpression = Class(name="Trigger_TriggerExpression")
HALL_FSM_State = Class(name="HALL_FSM_State", is_abstract=True)
Transition = Class(name="Transition")
HALL_Trigger_TriggerExpression = Class(name="HALL_Trigger_TriggerExpression")
Trigger_TriggerExpressionElement = Class(name="Trigger_TriggerExpressionElement")
HALL_FSM_FSM = Class(name="HALL_FSM_FSM")
FSM_HALL_Component = Class(name="FSM_HALL_Component")
InitialState = Class(name="InitialState")
NamedState = Class(name="NamedState")
HALL_FSM_NamedState = Class(name="HALL_FSM_NamedState")
State = Class(name="State")
HALL_FSM_InitialState = Class(name="HALL_FSM_InitialState")
HALL_FSMInstructions_BinaryOperator = Class(name="HALL_FSMInstructions_BinaryOperator")
HALL_FSMInstructions_UnaryOperator = Class(name="HALL_FSMInstructions_UnaryOperator")
HALL_FSMInstructions_GetData = Class(name="HALL_FSMInstructions_GetData")
FSMInstructions_HALL_Component = Class(name="FSMInstructions_HALL_Component")
HALL_FSMInstructions_GetState = Class(name="HALL_FSMInstructions_GetState")
HALL_FSMInstructions_SetState = Class(name="HALL_FSMInstructions_SetState")
HALL_FSMInstructions_SetData = Class(name="HALL_FSMInstructions_SetData")
HALL_Trigger_TriggerExpressionElement = Class(name="HALL_Trigger_TriggerExpressionElement", is_abstract=True)
HALL_Trigger_MessageNotification = Class(name="HALL_Trigger_MessageNotification")
TriggerExpressionElement = Class(name="TriggerExpressionElement")
HALL_Trigger_DomainEventFired = Class(name="HALL_Trigger_DomainEventFired")
HALL_FSMInstructions_PosConditionExpression = Class(name="HALL_FSMInstructions_PosConditionExpression", is_abstract=True)
FSMInstructions_PosConditionExpressionElement = Class(name="FSMInstructions_PosConditionExpressionElement")
HALL_FSMInstructions_PosConditionExpressionElement = Class(name="HALL_FSMInstructions_PosConditionExpressionElement", is_abstract=True)
HALL_FSMInstructions_VarRef = Class(name="HALL_FSMInstructions_VarRef")
PosConditionExpressionElement = Class(name="PosConditionExpressionElement")
HALL_FSMInstructions_Literal = Class(name="HALL_FSMInstructions_Literal")
HALL_FSMConditions_Literal = Class(name="HALL_FSMConditions_Literal")
PreConditionExpressionElement = Class(name="PreConditionExpressionElement")
HALL_FSMConditions_VarRef = Class(name="HALL_FSMConditions_VarRef")
HALL_FSMConditions_BinaryOperator = Class(name="HALL_FSMConditions_BinaryOperator")
HALL_FSMConditions_UnaryOperator = Class(name="HALL_FSMConditions_UnaryOperator")
HALL_FSMConditions_GetState = Class(name="HALL_FSMConditions_GetState")
FSMConditions_HALL_Component = Class(name="FSMConditions_HALL_Component")
HALL_FSMConditions_GetData = Class(name="HALL_FSMConditions_GetData")
HALL_FSMInstructions_Let = Class(name="HALL_FSMInstructions_Let")
HALL_FSMInstructions_DomainPropertyGet = Class(name="HALL_FSMInstructions_DomainPropertyGet")
HALL_FSMConditions_PreConditionExpression = Class(name="HALL_FSMConditions_PreConditionExpression", is_abstract=True)
FSMConditions_PreConditionExpressionElement = Class(name="FSMConditions_PreConditionExpressionElement")
HALL_FSMConditions_PreConditionExpressionElement = Class(name="HALL_FSMConditions_PreConditionExpressionElement", is_abstract=True)
HALL_FSMActions_Literal = Class(name="HALL_FSMActions_Literal")
HALL_FSMActions_DomainPropertyGet = Class(name="HALL_FSMActions_DomainPropertyGet")
HALL_FSMActions_Let = Class(name="HALL_FSMActions_Let")
HALL_FSMActions_MessageInvocation = Class(name="HALL_FSMActions_MessageInvocation")
HALL_FSMActions_Enable = Class(name="HALL_FSMActions_Enable")
HALL_FSMActions_DomainPropertySet = Class(name="HALL_FSMActions_DomainPropertySet")
HALL_FSMConditions_DomainPropertyGet = Class(name="HALL_FSMConditions_DomainPropertyGet")
HALL_FSMConditions_Let = Class(name="HALL_FSMConditions_Let")
HALL_FSMActions_ActionExpression = Class(name="HALL_FSMActions_ActionExpression", is_abstract=True)
FSMActions_ActionExpressionElement = Class(name="FSMActions_ActionExpressionElement")
HALL_FSMActions_ActionExpressionElement = Class(name="HALL_FSMActions_ActionExpressionElement", is_abstract=True)
HALL_FSMActions_VarRef = Class(name="HALL_FSMActions_VarRef")
ActionExpressionElement = Class(name="ActionExpressionElement")
HALL_FSMActions_GetData = Class(name="HALL_FSMActions_GetData")
FSMActions_HALL_Component = Class(name="FSMActions_HALL_Component")
HALL_FSMActions_BinaryOperator = Class(name="HALL_FSMActions_BinaryOperator")
HALL_FSMActions_UnaryOperator = Class(name="HALL_FSMActions_UnaryOperator")

# HALL_UserProfile class attributes and methods
HALL_UserProfile_numberofcompletedtasks: Property = Property(name="numberofcompletedtasks", type=IntegerType)
HALL_UserProfile.attributes={HALL_UserProfile_numberofcompletedtasks}

# HALL_Component class attributes and methods
HALL_Component_name: Property = Property(name="name", type=StringType)
HALL_Component.attributes={HALL_Component_name}

# HALL_Data class attributes and methods
HALL_Data_name: Property = Property(name="name", type=StringType)
HALL_Data_type: Property = Property(name="type", type=StringType)
HALL_Data_initValue: Property = Property(name="initValue", type=StringType)
HALL_Data_currentValue: Property = Property(name="currentValue", type=StringType)
HALL_Data.attributes={HALL_Data_name, HALL_Data_type, HALL_Data_initValue, HALL_Data_currentValue}

# FSM class attributes and methods

# MessageHandler class attributes and methods

# HALL_SystemComponent class attributes and methods

# HALL_Model class attributes and methods

# HALL_VisualObject class attributes and methods

# Component class attributes and methods

# ColorData class attributes and methods

# GeometryData class attributes and methods

# HALL_TaskObject class attributes and methods
HALL_TaskObject_completionTime: Property = Property(name="completionTime", type=IntegerType)
HALL_TaskObject_numberofgoalscompleted: Property = Property(name="numberofgoalscompleted", type=IntegerType)
HALL_TaskObject.attributes={HALL_TaskObject_numberofgoalscompleted, HALL_TaskObject_completionTime}

# HALL_Goal class attributes and methods
HALL_Goal_condition: Property = Property(name="condition", type=StringType)
HALL_Goal.attributes={HALL_Goal_condition}

# MessageDefinition class attributes and methods

# HALL_Geometry_Color class attributes and methods

# RGBColor class attributes and methods

# ColorState class attributes and methods

# HALL_Geometry_RGBColor class attributes and methods
HALL_Geometry_RGBColor_redValue: Property = Property(name="redValue", type=IntegerType)
HALL_Geometry_RGBColor_greenValue: Property = Property(name="greenValue", type=IntegerType)
HALL_Geometry_RGBColor_blueValue: Property = Property(name="blueValue", type=IntegerType)
HALL_Geometry_RGBColor.attributes={HALL_Geometry_RGBColor_blueValue, HALL_Geometry_RGBColor_redValue, HALL_Geometry_RGBColor_greenValue}

# Color class attributes and methods

# HALL_Parameter class attributes and methods
HALL_Parameter_name: Property = Property(name="name", type=StringType)
HALL_Parameter_type: Property = Property(name="type", type=StringType)
HALL_Parameter.attributes={HALL_Parameter_name, HALL_Parameter_type}

# HALL_Geometry_SelectedColors class attributes and methods

# HALL_Geometry_DisabledColors class attributes and methods

# HALL_Geometry_ColorData class attributes and methods

# SelectedColors class attributes and methods

# DisabledColors class attributes and methods

# NormalColors class attributes and methods

# Geometry_HALL_VisualObject class attributes and methods

# HALL_Geometry_GeometryData class attributes and methods

# HALL_Geometry_GeometryData3D class attributes and methods

# Face class attributes and methods

# HALL_Geometry_ColorState class attributes and methods

# AlphaTransparency class attributes and methods

# HALL_Geometry_AlphaTransparency class attributes and methods
HALL_Geometry_AlphaTransparency_value: Property = Property(name="value", type=IntegerType)
HALL_Geometry_AlphaTransparency.attributes={HALL_Geometry_AlphaTransparency_value}

# HALL_Geometry_NormalColors class attributes and methods

# HALL_Geometry_Point class attributes and methods
HALL_Geometry_Point_xCoord: Property = Property(name="xCoord", type=IntegerType)
HALL_Geometry_Point_yCoord: Property = Property(name="yCoord", type=IntegerType)
HALL_Geometry_Point.attributes={HALL_Geometry_Point_xCoord, HALL_Geometry_Point_yCoord}

# HALL_Messages_MessageTransition class attributes and methods
HALL_Messages_MessageTransition_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageTransition.attributes={HALL_Messages_MessageTransition_name}

# MessageState class attributes and methods

# Conditions_PreConditionMessageExpression class attributes and methods

# Instructions_PosConditionMessageExpression class attributes and methods

# Actions_ActionMessageExpression class attributes and methods

# HALL_Messages_NamedMessageState class attributes and methods
HALL_Messages_NamedMessageState_name: Property = Property(name="name", type=StringType)
HALL_Messages_NamedMessageState.attributes={HALL_Messages_NamedMessageState_name}

# HALL_Messages_MessageDefinition class attributes and methods
HALL_Messages_MessageDefinition_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageDefinition.attributes={HALL_Messages_MessageDefinition_name}

# Messages_HALL_Model class attributes and methods

# Messages_HALL_Parameter class attributes and methods

# HALL_Geometry_GeometryData2D class attributes and methods
HALL_Geometry_GeometryData2D_labelText: Property = Property(name="labelText", type=StringType)
HALL_Geometry_GeometryData2D.attributes={HALL_Geometry_GeometryData2D_labelText}

# Point2D class attributes and methods

# HALL_Geometry_Face class attributes and methods
HALL_Geometry_Face_labelText: Property = Property(name="labelText", type=StringType)
HALL_Geometry_Face.attributes={HALL_Geometry_Face_labelText}

# Point3D class attributes and methods

# GeometryData3D class attributes and methods

# HALL_Geometry_Point3D class attributes and methods
HALL_Geometry_Point3D_zCoord: Property = Property(name="zCoord", type=IntegerType)
HALL_Geometry_Point3D.attributes={HALL_Geometry_Point3D_zCoord}

# Point class attributes and methods

# HALL_Geometry_Point2D class attributes and methods

# GeometryData2D class attributes and methods

# Instructions_PosConditionMessageExpressionElement class attributes and methods

# HALL_Instructions_PosConditionMessageExpressionElement class attributes and methods

# HALL_Instructions_VarRef class attributes and methods
HALL_Instructions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_Instructions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_Instructions_VarRef.attributes={HALL_Instructions_VarRef_type, HALL_Instructions_VarRef_name}

# PosConditionMessageExpressionElement class attributes and methods

# HALL_Instructions_Literal class attributes and methods
HALL_Instructions_Literal_value: Property = Property(name="value", type=StringType)
HALL_Instructions_Literal.attributes={HALL_Instructions_Literal_value}

# HALL_Instructions_BinaryOperator class attributes and methods
HALL_Instructions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Instructions_BinaryOperator.attributes={HALL_Instructions_BinaryOperator_operatorname}

# HALL_Instructions_UnaryOperator class attributes and methods
HALL_Instructions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Instructions_UnaryOperator.attributes={HALL_Instructions_UnaryOperator_operatorname}

# HALL_Instructions_GetData class attributes and methods
HALL_Instructions_GetData_field: Property = Property(name="field", type=StringType)
HALL_Instructions_GetData.attributes={HALL_Instructions_GetData_field}

# Instructions_HALL_Component class attributes and methods

# Messages_HALL_Data class attributes and methods

# HALL_Messages_MessageHandler class attributes and methods
HALL_Messages_MessageHandler_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageHandler.attributes={HALL_Messages_MessageHandler_name}

# NamedMessageState class attributes and methods

# InitialMessageState class attributes and methods

# Messages_HALL_Component class attributes and methods

# HALL_Messages_MessageState class attributes and methods
HALL_Messages_MessageState_isEnd: Property = Property(name="isEnd", type=BooleanType)
HALL_Messages_MessageState_isContinue: Property = Property(name="isContinue", type=BooleanType)
HALL_Messages_MessageState_isActive: Property = Property(name="isActive", type=BooleanType)
HALL_Messages_MessageState.attributes={HALL_Messages_MessageState_isActive, HALL_Messages_MessageState_isEnd, HALL_Messages_MessageState_isContinue}

# MessageTransition class attributes and methods

# HALL_Messages_InitialMessageState class attributes and methods

# HALL_Instructions_PosConditionMessageExpression class attributes and methods

# HALL_Instructions_Let class attributes and methods
HALL_Instructions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_Instructions_Let.attributes={HALL_Instructions_Let_namevar}

# HALL_Instructions_DomainPropertyGet class attributes and methods
HALL_Instructions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_Instructions_DomainPropertyGet.attributes={HALL_Instructions_DomainPropertyGet_name}

# HALL_Instructions_GetMessageData class attributes and methods
HALL_Instructions_GetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Instructions_GetMessageData.attributes={HALL_Instructions_GetMessageData_field}

# HALL_Instructions_GetMessageParameter class attributes and methods
HALL_Instructions_GetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Instructions_GetMessageParameter.attributes={HALL_Instructions_GetMessageParameter_field}

# HALL_Instructions_SetTopDown class attributes and methods

# HALL_Conditions_PreConditionMessageExpression class attributes and methods

# HALL_Instructions_GetState class attributes and methods

# HALL_Instructions_SetState class attributes and methods
HALL_Instructions_SetState_name: Property = Property(name="name", type=StringType)
HALL_Instructions_SetState.attributes={HALL_Instructions_SetState_name}

# HALL_Instructions_SetData class attributes and methods
HALL_Instructions_SetData_field: Property = Property(name="field", type=StringType)
HALL_Instructions_SetData.attributes={HALL_Instructions_SetData_field}

# HALL_Instructions_SetMessageData class attributes and methods
HALL_Instructions_SetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Instructions_SetMessageData.attributes={HALL_Instructions_SetMessageData_field}

# HALL_Instructions_SetMessageParameter class attributes and methods
HALL_Instructions_SetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Instructions_SetMessageParameter.attributes={HALL_Instructions_SetMessageParameter_field}

# HALL_Conditions_Let class attributes and methods
HALL_Conditions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_Conditions_Let.attributes={HALL_Conditions_Let_namevar}

# HALL_Conditions_UnaryOperator class attributes and methods
HALL_Conditions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Conditions_UnaryOperator.attributes={HALL_Conditions_UnaryOperator_operatorname}

# HALL_Conditions_BinaryOperator class attributes and methods
HALL_Conditions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Conditions_BinaryOperator.attributes={HALL_Conditions_BinaryOperator_operatorname}

# HALL_Actions_ActionMessageExpression class attributes and methods

# Actions_ActionMessageExpressionElement class attributes and methods

# Conditions_PreConditionMessageExpressionElement class attributes and methods

# HALL_Conditions_PreConditionMessageExpressionElement class attributes and methods

# HALL_Conditions_VarRef class attributes and methods
HALL_Conditions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_Conditions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_Conditions_VarRef.attributes={HALL_Conditions_VarRef_type, HALL_Conditions_VarRef_name}

# PreConditionMessageExpressionElement class attributes and methods

# HALL_Conditions_Literal class attributes and methods
HALL_Conditions_Literal_value: Property = Property(name="value", type=StringType)
HALL_Conditions_Literal.attributes={HALL_Conditions_Literal_value}

# HALL_Conditions_GetMessageData class attributes and methods
HALL_Conditions_GetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Conditions_GetMessageData.attributes={HALL_Conditions_GetMessageData_field}

# HALL_Conditions_GetMessageParameter class attributes and methods
HALL_Conditions_GetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Conditions_GetMessageParameter.attributes={HALL_Conditions_GetMessageParameter_field}

# HALL_Conditions_DomainPropertyGet class attributes and methods
HALL_Conditions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_Conditions_DomainPropertyGet.attributes={HALL_Conditions_DomainPropertyGet_name}

# HALL_Conditions_GetState class attributes and methods

# Conditions_HALL_Component class attributes and methods

# HALL_Conditions_GetData class attributes and methods
HALL_Conditions_GetData_field: Property = Property(name="field", type=StringType)
HALL_Conditions_GetData.attributes={HALL_Conditions_GetData_field}

# HALL_Actions_GetMessageData class attributes and methods
HALL_Actions_GetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Actions_GetMessageData.attributes={HALL_Actions_GetMessageData_field}

# HALL_Actions_GetMessageParameter class attributes and methods
HALL_Actions_GetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Actions_GetMessageParameter.attributes={HALL_Actions_GetMessageParameter_field}

# HALL_Actions_MessageInvocation class attributes and methods
HALL_Actions_MessageInvocation_name: Property = Property(name="name", type=StringType)
HALL_Actions_MessageInvocation_isTopDown: Property = Property(name="isTopDown", type=BooleanType)
HALL_Actions_MessageInvocation.attributes={HALL_Actions_MessageInvocation_name, HALL_Actions_MessageInvocation_isTopDown}

# HALL_Actions_UnaryOperator class attributes and methods
HALL_Actions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Actions_UnaryOperator.attributes={HALL_Actions_UnaryOperator_operatorname}

# HALL_Actions_GetData class attributes and methods
HALL_Actions_GetData_field: Property = Property(name="field", type=StringType)
HALL_Actions_GetData.attributes={HALL_Actions_GetData_field}

# Actions_HALL_Component class attributes and methods

# HALL_Actions_DomainPropertySet class attributes and methods
HALL_Actions_DomainPropertySet_name: Property = Property(name="name", type=StringType)
HALL_Actions_DomainPropertySet.attributes={HALL_Actions_DomainPropertySet_name}

# HALL_Actions_Enable class attributes and methods

# HALL_Actions_ActionMessageExpressionElement class attributes and methods

# HALL_Actions_VarRef class attributes and methods
HALL_Actions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_Actions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_Actions_VarRef.attributes={HALL_Actions_VarRef_name, HALL_Actions_VarRef_type}

# ActionMessageExpressionElement class attributes and methods

# HALL_Actions_Literal class attributes and methods
HALL_Actions_Literal_value: Property = Property(name="value", type=StringType)
HALL_Actions_Literal.attributes={HALL_Actions_Literal_value}

# HALL_Actions_BinaryOperator class attributes and methods
HALL_Actions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Actions_BinaryOperator.attributes={HALL_Actions_BinaryOperator_operatorname}

# HALL_Actions_Let class attributes and methods
HALL_Actions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_Actions_Let.attributes={HALL_Actions_Let_namevar}

# HALL_Actions_DomainPropertyGet class attributes and methods
HALL_Actions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_Actions_DomainPropertyGet.attributes={HALL_Actions_DomainPropertyGet_name}

# HALL_FSM_Transition class attributes and methods
HALL_FSM_Transition_name: Property = Property(name="name", type=StringType)
HALL_FSM_Transition.attributes={HALL_FSM_Transition_name}

# FSMConditions_PreConditionExpression class attributes and methods

# FSMInstructions_PosConditionExpression class attributes and methods

# FSMActions_ActionExpression class attributes and methods

# Trigger_TriggerExpression class attributes and methods

# HALL_FSM_State class attributes and methods
HALL_FSM_State_isActive: Property = Property(name="isActive", type=BooleanType)
HALL_FSM_State.attributes={HALL_FSM_State_isActive}

# Transition class attributes and methods

# HALL_Trigger_TriggerExpression class attributes and methods

# Trigger_TriggerExpressionElement class attributes and methods

# HALL_FSM_FSM class attributes and methods

# FSM_HALL_Component class attributes and methods

# InitialState class attributes and methods

# NamedState class attributes and methods

# HALL_FSM_NamedState class attributes and methods
HALL_FSM_NamedState_name: Property = Property(name="name", type=StringType)
HALL_FSM_NamedState.attributes={HALL_FSM_NamedState_name}

# State class attributes and methods

# HALL_FSM_InitialState class attributes and methods

# HALL_FSMInstructions_BinaryOperator class attributes and methods
HALL_FSMInstructions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMInstructions_BinaryOperator.attributes={HALL_FSMInstructions_BinaryOperator_operatorname}

# HALL_FSMInstructions_UnaryOperator class attributes and methods
HALL_FSMInstructions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMInstructions_UnaryOperator.attributes={HALL_FSMInstructions_UnaryOperator_operatorname}

# HALL_FSMInstructions_GetData class attributes and methods
HALL_FSMInstructions_GetData_field: Property = Property(name="field", type=StringType)
HALL_FSMInstructions_GetData.attributes={HALL_FSMInstructions_GetData_field}

# FSMInstructions_HALL_Component class attributes and methods

# HALL_FSMInstructions_GetState class attributes and methods

# HALL_FSMInstructions_SetState class attributes and methods
HALL_FSMInstructions_SetState_name: Property = Property(name="name", type=StringType)
HALL_FSMInstructions_SetState.attributes={HALL_FSMInstructions_SetState_name}

# HALL_FSMInstructions_SetData class attributes and methods
HALL_FSMInstructions_SetData_field: Property = Property(name="field", type=StringType)
HALL_FSMInstructions_SetData.attributes={HALL_FSMInstructions_SetData_field}

# HALL_Trigger_TriggerExpressionElement class attributes and methods
HALL_Trigger_TriggerExpressionElement_String: Property = Property(name="String", type=StringType)
HALL_Trigger_TriggerExpressionElement.attributes={HALL_Trigger_TriggerExpressionElement_String}

# HALL_Trigger_MessageNotification class attributes and methods

# TriggerExpressionElement class attributes and methods

# HALL_Trigger_DomainEventFired class attributes and methods

# HALL_FSMInstructions_PosConditionExpression class attributes and methods

# FSMInstructions_PosConditionExpressionElement class attributes and methods

# HALL_FSMInstructions_PosConditionExpressionElement class attributes and methods

# HALL_FSMInstructions_VarRef class attributes and methods
HALL_FSMInstructions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_FSMInstructions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_FSMInstructions_VarRef.attributes={HALL_FSMInstructions_VarRef_name, HALL_FSMInstructions_VarRef_type}

# PosConditionExpressionElement class attributes and methods

# HALL_FSMInstructions_Literal class attributes and methods
HALL_FSMInstructions_Literal_value: Property = Property(name="value", type=StringType)
HALL_FSMInstructions_Literal.attributes={HALL_FSMInstructions_Literal_value}

# HALL_FSMConditions_Literal class attributes and methods
HALL_FSMConditions_Literal_value: Property = Property(name="value", type=StringType)
HALL_FSMConditions_Literal.attributes={HALL_FSMConditions_Literal_value}

# PreConditionExpressionElement class attributes and methods

# HALL_FSMConditions_VarRef class attributes and methods
HALL_FSMConditions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_FSMConditions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_FSMConditions_VarRef.attributes={HALL_FSMConditions_VarRef_type, HALL_FSMConditions_VarRef_name}

# HALL_FSMConditions_BinaryOperator class attributes and methods
HALL_FSMConditions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMConditions_BinaryOperator.attributes={HALL_FSMConditions_BinaryOperator_operatorname}

# HALL_FSMConditions_UnaryOperator class attributes and methods
HALL_FSMConditions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMConditions_UnaryOperator.attributes={HALL_FSMConditions_UnaryOperator_operatorname}

# HALL_FSMConditions_GetState class attributes and methods

# FSMConditions_HALL_Component class attributes and methods

# HALL_FSMConditions_GetData class attributes and methods
HALL_FSMConditions_GetData_field: Property = Property(name="field", type=StringType)
HALL_FSMConditions_GetData.attributes={HALL_FSMConditions_GetData_field}

# HALL_FSMInstructions_Let class attributes and methods
HALL_FSMInstructions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_FSMInstructions_Let.attributes={HALL_FSMInstructions_Let_namevar}

# HALL_FSMInstructions_DomainPropertyGet class attributes and methods
HALL_FSMInstructions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMInstructions_DomainPropertyGet.attributes={HALL_FSMInstructions_DomainPropertyGet_name}

# HALL_FSMConditions_PreConditionExpression class attributes and methods

# FSMConditions_PreConditionExpressionElement class attributes and methods

# HALL_FSMConditions_PreConditionExpressionElement class attributes and methods

# HALL_FSMActions_Literal class attributes and methods
HALL_FSMActions_Literal_value: Property = Property(name="value", type=StringType)
HALL_FSMActions_Literal.attributes={HALL_FSMActions_Literal_value}

# HALL_FSMActions_DomainPropertyGet class attributes and methods
HALL_FSMActions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_DomainPropertyGet.attributes={HALL_FSMActions_DomainPropertyGet_name}

# HALL_FSMActions_Let class attributes and methods
HALL_FSMActions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_FSMActions_Let.attributes={HALL_FSMActions_Let_namevar}

# HALL_FSMActions_MessageInvocation class attributes and methods
HALL_FSMActions_MessageInvocation_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_MessageInvocation_isTopDown: Property = Property(name="isTopDown", type=BooleanType)
HALL_FSMActions_MessageInvocation.attributes={HALL_FSMActions_MessageInvocation_name, HALL_FSMActions_MessageInvocation_isTopDown}

# HALL_FSMActions_Enable class attributes and methods

# HALL_FSMActions_DomainPropertySet class attributes and methods
HALL_FSMActions_DomainPropertySet_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_DomainPropertySet.attributes={HALL_FSMActions_DomainPropertySet_name}

# HALL_FSMConditions_DomainPropertyGet class attributes and methods
HALL_FSMConditions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMConditions_DomainPropertyGet.attributes={HALL_FSMConditions_DomainPropertyGet_name}

# HALL_FSMConditions_Let class attributes and methods
HALL_FSMConditions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_FSMConditions_Let.attributes={HALL_FSMConditions_Let_namevar}

# HALL_FSMActions_ActionExpression class attributes and methods

# FSMActions_ActionExpressionElement class attributes and methods

# HALL_FSMActions_ActionExpressionElement class attributes and methods

# HALL_FSMActions_VarRef class attributes and methods
HALL_FSMActions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_FSMActions_VarRef.attributes={HALL_FSMActions_VarRef_type, HALL_FSMActions_VarRef_name}

# ActionExpressionElement class attributes and methods

# HALL_FSMActions_GetData class attributes and methods
HALL_FSMActions_GetData_field: Property = Property(name="field", type=StringType)
HALL_FSMActions_GetData.attributes={HALL_FSMActions_GetData_field}

# FSMActions_HALL_Component class attributes and methods

# HALL_FSMActions_BinaryOperator class attributes and methods
HALL_FSMActions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMActions_BinaryOperator.attributes={HALL_FSMActions_BinaryOperator_operatorname}

# HALL_FSMActions_UnaryOperator class attributes and methods
HALL_FSMActions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMActions_UnaryOperator.attributes={HALL_FSMActions_UnaryOperator_operatorname}

# Relationships
geometryData1: BinaryAssociation = BinaryAssociation(
    name="geometryData1",
    ends={
        Property(name="geometryDataInv", type=GeometryData, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="GeometryData", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1))
    }
)
visualObjectInv2: BinaryAssociation = BinaryAssociation(
    name="visualObjectInv2",
    ends={
        Property(name="UserProfile", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="visualObject", type=HALL_UserProfile, multiplicity=Multiplicity(0, 1))
    }
)
componentSet4: BinaryAssociation = BinaryAssociation(
    name="componentSet4",
    ends={
        Property(name="VisualObject", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv", type=HALL_VisualObject, multiplicity=Multiplicity(0, 9999))
    }
)
componentSetInv6: BinaryAssociation = BinaryAssociation(
    name="componentSetInv6",
    ends={
        Property(name="VisualObject7", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet", type=HALL_VisualObject, multiplicity=Multiplicity(0, 1))
    }
)
data8: BinaryAssociation = BinaryAssociation(
    name="data8",
    ends={
        Property(name="Data", type=HALL_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInvComponent", type=HALL_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
FSM9: BinaryAssociation = BinaryAssociation(
    name="FSM9",
    ends={
        Property(name="FSM", type=HALL_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMInv", type=FSM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageHandlerSet10: BinaryAssociation = BinaryAssociation(
    name="messageHandlerSet10",
    ends={
        Property(name="MessageHandler", type=HALL_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="messageHandlerSetInv", type=MessageHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colorData0: BinaryAssociation = BinaryAssociation(
    name="colorData0",
    ends={
        Property(name="ColorData", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="colorDataInv", type=ColorData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
taskObject26: BinaryAssociation = BinaryAssociation(
    name="taskObject26",
    ends={
        Property(name="TaskObject", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="taskObjectInv", type=HALL_TaskObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userProfileInv27: BinaryAssociation = BinaryAssociation(
    name="userProfileInv27",
    ends={
        Property(name="Model28", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="userProfile", type=HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
componentSet30: BinaryAssociation = BinaryAssociation(
    name="componentSet30",
    ends={
        Property(name="UserProfile32", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv31", type=HALL_UserProfile, multiplicity=Multiplicity(0, 9999))
    }
)
componentSetInv34: BinaryAssociation = BinaryAssociation(
    name="componentSetInv34",
    ends={
        Property(name="UserProfile36", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet35", type=HALL_UserProfile, multiplicity=Multiplicity(0, 1))
    }
)
goal37: BinaryAssociation = BinaryAssociation(
    name="goal37",
    ends={
        Property(name="Goal", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="goalInv", type=HALL_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskObjectInv38: BinaryAssociation = BinaryAssociation(
    name="taskObjectInv38",
    ends={
        Property(name="UserProfile39", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="taskObject", type=HALL_UserProfile, multiplicity=Multiplicity(0, 1))
    }
)
componentSet41: BinaryAssociation = BinaryAssociation(
    name="componentSet41",
    ends={
        Property(name="TaskObject43", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv42", type=HALL_TaskObject, multiplicity=Multiplicity(0, 9999))
    }
)
componentSetInv45: BinaryAssociation = BinaryAssociation(
    name="componentSetInv45",
    ends={
        Property(name="TaskObject47", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet46", type=HALL_TaskObject, multiplicity=Multiplicity(0, 1))
    }
)
systemComponentInv11: BinaryAssociation = BinaryAssociation(
    name="systemComponentInv11",
    ends={
        Property(name="Model", type=HALL_SystemComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="systemComponent", type=HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
componentSet13: BinaryAssociation = BinaryAssociation(
    name="componentSet13",
    ends={
        Property(name="SystemComponent", type=HALL_SystemComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv14", type=HALL_SystemComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentSetInv16: BinaryAssociation = BinaryAssociation(
    name="componentSetInv16",
    ends={
        Property(name="SystemComponent18", type=HALL_SystemComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet17", type=HALL_SystemComponent, multiplicity=Multiplicity(0, 1))
    }
)
userProfile19: BinaryAssociation = BinaryAssociation(
    name="userProfile19",
    ends={
        Property(name="UserProfile20", type=HALL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="userProfileInv", type=HALL_UserProfile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemComponent21: BinaryAssociation = BinaryAssociation(
    name="systemComponent21",
    ends={
        Property(name="SystemComponent22", type=HALL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="systemComponentInv", type=HALL_SystemComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageDefinition23: BinaryAssociation = BinaryAssociation(
    name="messageDefinition23",
    ends={
        Property(name="MessageDefinition", type=HALL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinitionInv", type=MessageDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
visualObject24: BinaryAssociation = BinaryAssociation(
    name="visualObject24",
    ends={
        Property(name="VisualObject25", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="visualObjectInv", type=HALL_VisualObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ambianceColor56: BinaryAssociation = BinaryAssociation(
    name="ambianceColor56",
    ends={
        Property(name="RGBColor", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="ambianceColorInv", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
difuseColor57: BinaryAssociation = BinaryAssociation(
    name="difuseColor57",
    ends={
        Property(name="RGBColor58", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="difuseColorInv", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specularColor59: BinaryAssociation = BinaryAssociation(
    name="specularColor59",
    ends={
        Property(name="RGBColor60", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="specularColorInv", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColorInv61: BinaryAssociation = BinaryAssociation(
    name="foregroundColorInv61",
    ends={
        Property(name="ColorState", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="foregroundColor", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColorInv62: BinaryAssociation = BinaryAssociation(
    name="backgroundColorInv62",
    ends={
        Property(name="ColorState63", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="backgroundColor", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
ambianceColorInv64: BinaryAssociation = BinaryAssociation(
    name="ambianceColorInv64",
    ends={
        Property(name="Color", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="ambianceColor", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
difuseColorInv65: BinaryAssociation = BinaryAssociation(
    name="difuseColorInv65",
    ends={
        Property(name="Color66", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="difuseColor", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
specularColorInv67: BinaryAssociation = BinaryAssociation(
    name="specularColorInv67",
    ends={
        Property(name="Color68", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="specularColor", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
goalInv48: BinaryAssociation = BinaryAssociation(
    name="goalInv48",
    ends={
        Property(name="TaskObject49", type=HALL_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goal", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1))
    }
)
parameterInv50: BinaryAssociation = BinaryAssociation(
    name="parameterInv50",
    ends={
        Property(name="MessageDefinition51", type=HALL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
dataInvMessageDefinition52: BinaryAssociation = BinaryAssociation(
    name="dataInvMessageDefinition52",
    ends={
        Property(name="MessageDefinition53", type=HALL_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="data", type=MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
dataInvComponent54: BinaryAssociation = BinaryAssociation(
    name="dataInvComponent54",
    ends={
        Property(name="Component", type=HALL_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="data55", type=HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
normalColorsInv76: BinaryAssociation = BinaryAssociation(
    name="normalColorsInv76",
    ends={
        Property(name="ColorData77", type=HALL_Geometry_NormalColors, multiplicity=Multiplicity(1, 1)),
        Property(name="normalColors", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
selectedColorsInv78: BinaryAssociation = BinaryAssociation(
    name="selectedColorsInv78",
    ends={
        Property(name="ColorData79", type=HALL_Geometry_SelectedColors, multiplicity=Multiplicity(1, 1)),
        Property(name="selectedColors", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
disabledColorsInv80: BinaryAssociation = BinaryAssociation(
    name="disabledColorsInv80",
    ends={
        Property(name="ColorData81", type=HALL_Geometry_DisabledColors, multiplicity=Multiplicity(1, 1)),
        Property(name="disabledColors", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
selectedColors82: BinaryAssociation = BinaryAssociation(
    name="selectedColors82",
    ends={
        Property(name="SelectedColors", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="selectedColorsInv", type=SelectedColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
disabledColors83: BinaryAssociation = BinaryAssociation(
    name="disabledColors83",
    ends={
        Property(name="DisabledColors", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="disabledColorsInv", type=DisabledColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
normalColors84: BinaryAssociation = BinaryAssociation(
    name="normalColors84",
    ends={
        Property(name="NormalColors", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="normalColorsInv", type=NormalColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colorDataInv85: BinaryAssociation = BinaryAssociation(
    name="colorDataInv85",
    ends={
        Property(name="VisualObject86", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="colorData", type=Geometry_HALL_VisualObject, multiplicity=Multiplicity(0, 1))
    }
)
geometryDataInv87: BinaryAssociation = BinaryAssociation(
    name="geometryDataInv87",
    ends={
        Property(name="VisualObject88", type=HALL_Geometry_GeometryData, multiplicity=Multiplicity(1, 1)),
        Property(name="geometryData", type=Geometry_HALL_VisualObject, multiplicity=Multiplicity(0, 1))
    }
)
foregroundColor69: BinaryAssociation = BinaryAssociation(
    name="foregroundColor69",
    ends={
        Property(name="Color70", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="foregroundColorInv", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor71: BinaryAssociation = BinaryAssociation(
    name="backgroundColor71",
    ends={
        Property(name="Color72", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="backgroundColorInv", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alphaTransparency73: BinaryAssociation = BinaryAssociation(
    name="alphaTransparency73",
    ends={
        Property(name="AlphaTransparency", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="alphaTransparencyInv", type=AlphaTransparency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alphaTransparencyInv74: BinaryAssociation = BinaryAssociation(
    name="alphaTransparencyInv74",
    ends={
        Property(name="ColorState75", type=HALL_Geometry_AlphaTransparency, multiplicity=Multiplicity(1, 1)),
        Property(name="alphaTransparency", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
transitionsInvMessageState97: BinaryAssociation = BinaryAssociation(
    name="transitionsInvMessageState97",
    ends={
        Property(name="MessageState", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=MessageState, multiplicity=Multiplicity(0, 1))
    }
)
stateRef98: BinaryAssociation = BinaryAssociation(
    name="stateRef98",
    ends={
        Property(name="MessageState99", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageTransition", type=MessageState, multiplicity=Multiplicity(1, 1))
    }
)
PreCondition100: BinaryAssociation = BinaryAssociation(
    name="PreCondition100",
    ends={
        Property(name="PreConditionMessageExpression", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="PreConditionInv", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PosCondition101: BinaryAssociation = BinaryAssociation(
    name="PosCondition101",
    ends={
        Property(name="PosConditionMessageExpression", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="PosConditionInv", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ActionMessage102: BinaryAssociation = BinaryAssociation(
    name="ActionMessage102",
    ends={
        Property(name="ActionMessageExpression", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionMessageInv", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageStateInv103: BinaryAssociation = BinaryAssociation(
    name="messageStateInv103",
    ends={
        Property(name="MessageHandler104", type=HALL_Messages_NamedMessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="messageState", type=MessageHandler, multiplicity=Multiplicity(0, 1))
    }
)
messageDefinitionInv105: BinaryAssociation = BinaryAssociation(
    name="messageDefinitionInv105",
    ends={
        Property(name="Model106", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition", type=Messages_HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
parameter107: BinaryAssociation = BinaryAssociation(
    name="parameter107",
    ends={
        Property(name="Parameter", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterInv", type=Messages_HALL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
face89: BinaryAssociation = BinaryAssociation(
    name="face89",
    ends={
        Property(name="Face", type=HALL_Geometry_GeometryData3D, multiplicity=Multiplicity(1, 1)),
        Property(name="faceInv", type=Face, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
point2d90: BinaryAssociation = BinaryAssociation(
    name="point2d90",
    ends={
        Property(name="Point2D", type=HALL_Geometry_GeometryData2D, multiplicity=Multiplicity(1, 1)),
        Property(name="point2dInv", type=Point2D, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
point3d91: BinaryAssociation = BinaryAssociation(
    name="point3d91",
    ends={
        Property(name="Point3D", type=HALL_Geometry_Face, multiplicity=Multiplicity(1, 1)),
        Property(name="point2dInv92", type=Point3D, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
faceInv93: BinaryAssociation = BinaryAssociation(
    name="faceInv93",
    ends={
        Property(name="GeometryData3D", type=HALL_Geometry_Face, multiplicity=Multiplicity(1, 1)),
        Property(name="face", type=GeometryData3D, multiplicity=Multiplicity(0, 1))
    }
)
point2dInv94: BinaryAssociation = BinaryAssociation(
    name="point2dInv94",
    ends={
        Property(name="Face95", type=HALL_Geometry_Point3D, multiplicity=Multiplicity(1, 1)),
        Property(name="point3d", type=Face, multiplicity=Multiplicity(0, 1))
    }
)
point2dInv96: BinaryAssociation = BinaryAssociation(
    name="point2dInv96",
    ends={
        Property(name="GeometryData2D", type=HALL_Geometry_Point2D, multiplicity=Multiplicity(1, 1)),
        Property(name="point2d", type=GeometryData2D, multiplicity=Multiplicity(0, 1))
    }
)
PosConditionInv117: BinaryAssociation = BinaryAssociation(
    name="PosConditionInv117",
    ends={
        Property(name="MessageTransition118", type=HALL_Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PosCondition", type=MessageTransition, multiplicity=Multiplicity(0, 1))
    }
)
PosConditionSet119: BinaryAssociation = BinaryAssociation(
    name="PosConditionSet119",
    ends={
        Property(name="PosConditionMessageExpressionElement", type=HALL_Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PosConditionSetInv", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PosConditionSetInv120: BinaryAssociation = BinaryAssociation(
    name="PosConditionSetInv120",
    ends={
        Property(name="PosConditionMessageExpression121", type=HALL_Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PosConditionSet", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(0, 1))
    }
)
leftexpression122: BinaryAssociation = BinaryAssociation(
    name="leftexpression122",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement", type=HALL_Instructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_BinaryOperator", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
rightexpression123: BinaryAssociation = BinaryAssociation(
    name="rightexpression123",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement125", type=HALL_Instructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_BinaryOperator124", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement127", type=HALL_Instructions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_UnaryOperator", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
data108: BinaryAssociation = BinaryAssociation(
    name="data108",
    ends={
        Property(name="Data109", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInvMessageDefinition", type=Messages_HALL_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageState110: BinaryAssociation = BinaryAssociation(
    name="messageState110",
    ends={
        Property(name="NamedMessageState", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="messageStateInv", type=NamedMessageState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialMessageState111: BinaryAssociation = BinaryAssociation(
    name="initialMessageState111",
    ends={
        Property(name="InitialMessageState", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="initialMessageStateInv", type=InitialMessageState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageHandlerSetInv112: BinaryAssociation = BinaryAssociation(
    name="messageHandlerSetInv112",
    ends={
        Property(name="Component113", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="messageHandlerSet", type=Messages_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
transitions114: BinaryAssociation = BinaryAssociation(
    name="transitions114",
    ends={
        Property(name="MessageTransition", type=HALL_Messages_MessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="transitionsInvMessageState", type=MessageTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialMessageStateInv115: BinaryAssociation = BinaryAssociation(
    name="initialMessageStateInv115",
    ends={
        Property(name="MessageHandler116", type=HALL_Messages_InitialMessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="initialMessageState", type=MessageHandler, multiplicity=Multiplicity(0, 1))
    }
)
value140: BinaryAssociation = BinaryAssociation(
    name="value140",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement141", type=HALL_Instructions_SetMessageParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetMessageParameter", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
in_142: BinaryAssociation = BinaryAssociation(
    name="in_142",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement143", type=HALL_Instructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_Let", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
initialization144: BinaryAssociation = BinaryAssociation(
    name="initialization144",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement146", type=HALL_Instructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_Let145", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
value147: BinaryAssociation = BinaryAssociation(
    name="value147",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement148", type=HALL_Instructions_SetTopDown, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetTopDown", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
PreConditionInv149: BinaryAssociation = BinaryAssociation(
    name="PreConditionInv149",
    ends={
        Property(name="MessageTransition150", type=HALL_Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PreCondition", type=MessageTransition, multiplicity=Multiplicity(0, 1))
    }
)
reference128: BinaryAssociation = BinaryAssociation(
    name="reference128",
    ends={
        Property(name="Instructions_HALL_Component", type=HALL_Instructions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_GetData", type=Instructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference129: BinaryAssociation = BinaryAssociation(
    name="reference129",
    ends={
        Property(name="Instructions_HALL_Component130", type=HALL_Instructions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_GetState", type=Instructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference131: BinaryAssociation = BinaryAssociation(
    name="reference131",
    ends={
        Property(name="Instructions_HALL_Component132", type=HALL_Instructions_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetState", type=Instructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
value133: BinaryAssociation = BinaryAssociation(
    name="value133",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement134", type=HALL_Instructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetData", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference135: BinaryAssociation = BinaryAssociation(
    name="reference135",
    ends={
        Property(name="Instructions_HALL_Component137", type=HALL_Instructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetData136", type=Instructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
value138: BinaryAssociation = BinaryAssociation(
    name="value138",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement139", type=HALL_Instructions_SetMessageData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetMessageData", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference155: BinaryAssociation = BinaryAssociation(
    name="reference155",
    ends={
        Property(name="Conditions_HALL_Component156", type=HALL_Conditions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_GetData", type=Conditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
in_157: BinaryAssociation = BinaryAssociation(
    name="in_157",
    ends={
        Property(name="Conditions_PreConditionMessageExpressionElement", type=HALL_Conditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_Let", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
initialization158: BinaryAssociation = BinaryAssociation(
    name="initialization158",
    ends={
        Property(name="Conditions_PreConditionMessageExpressionElement160", type=HALL_Conditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_Let159", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
expression161: BinaryAssociation = BinaryAssociation(
    name="expression161",
    ends={
        Property(name="Conditions_PreConditionMessageExpressionElement162", type=HALL_Conditions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_UnaryOperator", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
leftexpression163: BinaryAssociation = BinaryAssociation(
    name="leftexpression163",
    ends={
        Property(name="Conditions_PreConditionMessageExpressionElement164", type=HALL_Conditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_BinaryOperator", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
rightexpression165: BinaryAssociation = BinaryAssociation(
    name="rightexpression165",
    ends={
        Property(name="Conditions_PreConditionMessageExpressionElement167", type=HALL_Conditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_BinaryOperator166", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
ActionMessageInv168: BinaryAssociation = BinaryAssociation(
    name="ActionMessageInv168",
    ends={
        Property(name="MessageTransition169", type=HALL_Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionMessage", type=MessageTransition, multiplicity=Multiplicity(0, 1))
    }
)
ActionMessageSet170: BinaryAssociation = BinaryAssociation(
    name="ActionMessageSet170",
    ends={
        Property(name="ActionMessageExpressionElement", type=HALL_Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionMessageSetInv", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PreConditionSet151: BinaryAssociation = BinaryAssociation(
    name="PreConditionSet151",
    ends={
        Property(name="PreConditionMessageExpressionElement", type=HALL_Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PreConditionSetInv", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PreConditionSetInv152: BinaryAssociation = BinaryAssociation(
    name="PreConditionSetInv152",
    ends={
        Property(name="PreConditionMessageExpression153", type=HALL_Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PreConditionSet", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(0, 1))
    }
)
reference154: BinaryAssociation = BinaryAssociation(
    name="reference154",
    ends={
        Property(name="Conditions_HALL_Component", type=HALL_Conditions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_GetState", type=Conditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
actualset182: BinaryAssociation = BinaryAssociation(
    name="actualset182",
    ends={
        Property(name="Actions_ActionMessageExpressionElement183", type=HALL_Actions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_MessageInvocation", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(0, 1))
    }
)
expression184: BinaryAssociation = BinaryAssociation(
    name="expression184",
    ends={
        Property(name="Actions_ActionMessageExpressionElement185", type=HALL_Actions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_UnaryOperator", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference186: BinaryAssociation = BinaryAssociation(
    name="reference186",
    ends={
        Property(name="Actions_HALL_Component", type=HALL_Actions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_GetData", type=Actions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
value187: BinaryAssociation = BinaryAssociation(
    name="value187",
    ends={
        Property(name="Actions_ActionMessageExpressionElement188", type=HALL_Actions_DomainPropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_DomainPropertySet", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
ActionMessageSetInv171: BinaryAssociation = BinaryAssociation(
    name="ActionMessageSetInv171",
    ends={
        Property(name="ActionMessageExpression172", type=HALL_Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionMessageSet", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(0, 1))
    }
)
leftexpression173: BinaryAssociation = BinaryAssociation(
    name="leftexpression173",
    ends={
        Property(name="Actions_ActionMessageExpressionElement", type=HALL_Actions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_BinaryOperator", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
rightexpression174: BinaryAssociation = BinaryAssociation(
    name="rightexpression174",
    ends={
        Property(name="Actions_ActionMessageExpressionElement176", type=HALL_Actions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_BinaryOperator175", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
in_177: BinaryAssociation = BinaryAssociation(
    name="in_177",
    ends={
        Property(name="Actions_ActionMessageExpressionElement178", type=HALL_Actions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Let", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
initialization179: BinaryAssociation = BinaryAssociation(
    name="initialization179",
    ends={
        Property(name="Actions_ActionMessageExpressionElement181", type=HALL_Actions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Let180", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
source204: BinaryAssociation = BinaryAssociation(
    name="source204",
    ends={
        Property(name="State", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions205", type=State, multiplicity=Multiplicity(1, 1))
    }
)
stateRef206: BinaryAssociation = BinaryAssociation(
    name="stateRef206",
    ends={
        Property(name="State207", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition", type=State, multiplicity=Multiplicity(1, 1))
    }
)
PreCondition208: BinaryAssociation = BinaryAssociation(
    name="PreCondition208",
    ends={
        Property(name="PreConditionExpression", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PreConditionInv209", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PosCondition210: BinaryAssociation = BinaryAssociation(
    name="PosCondition210",
    ends={
        Property(name="PosConditionExpression", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PosConditionInv211", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Action212: BinaryAssociation = BinaryAssociation(
    name="Action212",
    ends={
        Property(name="ActionExpression", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionInv", type=FSMActions_ActionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Trigger213: BinaryAssociation = BinaryAssociation(
    name="Trigger213",
    ends={
        Property(name="TriggerExpression", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="TriggerInv", type=Trigger_TriggerExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions214: BinaryAssociation = BinaryAssociation(
    name="transitions214",
    ends={
        Property(name="Transition", type=HALL_FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TriggerExpressionSet215: BinaryAssociation = BinaryAssociation(
    name="TriggerExpressionSet215",
    ends={
        Property(name="TriggerExpressionElement", type=HALL_Trigger_TriggerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TriggerExpressionSetInv", type=Trigger_TriggerExpressionElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TriggerInv216: BinaryAssociation = BinaryAssociation(
    name="TriggerInv216",
    ends={
        Property(name="Transition217", type=HALL_Trigger_TriggerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Trigger", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
value189: BinaryAssociation = BinaryAssociation(
    name="value189",
    ends={
        Property(name="Actions_ActionMessageExpressionElement190", type=HALL_Actions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Enable", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(0, 9999))
    }
)
reference191: BinaryAssociation = BinaryAssociation(
    name="reference191",
    ends={
        Property(name="MessageDefinition193", type=HALL_Actions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Enable192", type=MessageDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FSMInv194: BinaryAssociation = BinaryAssociation(
    name="FSMInv194",
    ends={
        Property(name="Component196", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM195", type=FSM_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
initialState197: BinaryAssociation = BinaryAssociation(
    name="initialState197",
    ends={
        Property(name="InitialState", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm", type=InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
state198: BinaryAssociation = BinaryAssociation(
    name="state198",
    ends={
        Property(name="NamedState", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm199", type=NamedState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fsm200: BinaryAssociation = BinaryAssociation(
    name="fsm200",
    ends={
        Property(name="FSM201", type=HALL_FSM_NamedState, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=FSM, multiplicity=Multiplicity(0, 1))
    }
)
fsm202: BinaryAssociation = BinaryAssociation(
    name="fsm202",
    ends={
        Property(name="FSM203", type=HALL_FSM_InitialState, multiplicity=Multiplicity(1, 1)),
        Property(name="initialState", type=FSM, multiplicity=Multiplicity(0, 1))
    }
)
rightexpression228: BinaryAssociation = BinaryAssociation(
    name="rightexpression228",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement", type=HALL_FSMInstructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_BinaryOperator", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
leftexpression229: BinaryAssociation = BinaryAssociation(
    name="leftexpression229",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement231", type=HALL_FSMInstructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_BinaryOperator230", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
expression232: BinaryAssociation = BinaryAssociation(
    name="expression232",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement233", type=HALL_FSMInstructions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_UnaryOperator", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference234: BinaryAssociation = BinaryAssociation(
    name="reference234",
    ends={
        Property(name="FSMInstructions_HALL_Component", type=HALL_FSMInstructions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_GetData", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference235: BinaryAssociation = BinaryAssociation(
    name="reference235",
    ends={
        Property(name="FSMInstructions_HALL_Component236", type=HALL_FSMInstructions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_GetState", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference237: BinaryAssociation = BinaryAssociation(
    name="reference237",
    ends={
        Property(name="FSMInstructions_HALL_Component238", type=HALL_FSMInstructions_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetState", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
TriggerExpressionSetInv218: BinaryAssociation = BinaryAssociation(
    name="TriggerExpressionSetInv218",
    ends={
        Property(name="TriggerExpression219", type=HALL_Trigger_TriggerExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TriggerExpressionSet", type=Trigger_TriggerExpression, multiplicity=Multiplicity(0, 1))
    }
)
PosConditionSet220: BinaryAssociation = BinaryAssociation(
    name="PosConditionSet220",
    ends={
        Property(name="PosConditionExpressionElement", type=HALL_FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PosConditionSetInv221", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PosConditionInv222: BinaryAssociation = BinaryAssociation(
    name="PosConditionInv222",
    ends={
        Property(name="Transition224", type=HALL_FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PosCondition223", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
PosConditionSetInv225: BinaryAssociation = BinaryAssociation(
    name="PosConditionSetInv225",
    ends={
        Property(name="PosConditionExpression227", type=HALL_FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PosConditionSet226", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(0, 1))
    }
)
PreConditionSetInv254: BinaryAssociation = BinaryAssociation(
    name="PreConditionSetInv254",
    ends={
        Property(name="PreConditionExpression256", type=HALL_FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PreConditionSet255", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(0, 1))
    }
)
rightexpression257: BinaryAssociation = BinaryAssociation(
    name="rightexpression257",
    ends={
        Property(name="FSMConditions_PreConditionExpressionElement", type=HALL_FSMConditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_BinaryOperator", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
leftexpression258: BinaryAssociation = BinaryAssociation(
    name="leftexpression258",
    ends={
        Property(name="FSMConditions_PreConditionExpressionElement260", type=HALL_FSMConditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_BinaryOperator259", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
expression261: BinaryAssociation = BinaryAssociation(
    name="expression261",
    ends={
        Property(name="FSMConditions_PreConditionExpressionElement262", type=HALL_FSMConditions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_UnaryOperator", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference263: BinaryAssociation = BinaryAssociation(
    name="reference263",
    ends={
        Property(name="FSMConditions_HALL_Component", type=HALL_FSMConditions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_GetState", type=FSMConditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
value239: BinaryAssociation = BinaryAssociation(
    name="value239",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement240", type=HALL_FSMInstructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetData", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference241: BinaryAssociation = BinaryAssociation(
    name="reference241",
    ends={
        Property(name="FSMInstructions_HALL_Component243", type=HALL_FSMInstructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetData242", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
in_244: BinaryAssociation = BinaryAssociation(
    name="in_244",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement245", type=HALL_FSMInstructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_Let", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
initialization246: BinaryAssociation = BinaryAssociation(
    name="initialization246",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement248", type=HALL_FSMInstructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_Let247", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
PreConditionSet249: BinaryAssociation = BinaryAssociation(
    name="PreConditionSet249",
    ends={
        Property(name="PreConditionExpressionElement", type=HALL_FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PreConditionSetInv250", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PreConditionInv251: BinaryAssociation = BinaryAssociation(
    name="PreConditionInv251",
    ends={
        Property(name="Transition253", type=HALL_FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PreCondition252", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
in_276: BinaryAssociation = BinaryAssociation(
    name="in_276",
    ends={
        Property(name="FSMActions_ActionExpressionElement", type=HALL_FSMActions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Let", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
initialization277: BinaryAssociation = BinaryAssociation(
    name="initialization277",
    ends={
        Property(name="FSMActions_ActionExpressionElement279", type=HALL_FSMActions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Let278", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
actualset280: BinaryAssociation = BinaryAssociation(
    name="actualset280",
    ends={
        Property(name="FSMActions_ActionExpressionElement281", type=HALL_FSMActions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_MessageInvocation", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(0, 9999))
    }
)
value282: BinaryAssociation = BinaryAssociation(
    name="value282",
    ends={
        Property(name="FSMActions_ActionExpressionElement283", type=HALL_FSMActions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Enable", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(0, 1))
    }
)
message284: BinaryAssociation = BinaryAssociation(
    name="message284",
    ends={
        Property(name="MessageDefinition286", type=HALL_FSMActions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Enable285", type=MessageDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference264: BinaryAssociation = BinaryAssociation(
    name="reference264",
    ends={
        Property(name="FSMConditions_HALL_Component265", type=HALL_FSMConditions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_GetData", type=FSMConditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
initialization266: BinaryAssociation = BinaryAssociation(
    name="initialization266",
    ends={
        Property(name="FSMConditions_PreConditionExpressionElement267", type=HALL_FSMConditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_Let", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
in_268: BinaryAssociation = BinaryAssociation(
    name="in_268",
    ends={
        Property(name="FSMConditions_PreConditionExpressionElement270", type=HALL_FSMConditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_Let269", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
ActionInv271: BinaryAssociation = BinaryAssociation(
    name="ActionInv271",
    ends={
        Property(name="Transition272", type=HALL_FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Action", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
ActionExpressionSet273: BinaryAssociation = BinaryAssociation(
    name="ActionExpressionSet273",
    ends={
        Property(name="ActionExpressionElement", type=HALL_FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionExpressionSetInv", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActionExpressionSetInv274: BinaryAssociation = BinaryAssociation(
    name="ActionExpressionSetInv274",
    ends={
        Property(name="ActionExpression275", type=HALL_FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionExpressionSet", type=FSMActions_ActionExpression, multiplicity=Multiplicity(0, 1))
    }
)
value287: BinaryAssociation = BinaryAssociation(
    name="value287",
    ends={
        Property(name="FSMActions_ActionExpressionElement288", type=HALL_FSMActions_DomainPropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_DomainPropertySet", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference289: BinaryAssociation = BinaryAssociation(
    name="reference289",
    ends={
        Property(name="FSMActions_HALL_Component", type=HALL_FSMActions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_GetData", type=FSMActions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
leftoperator290: BinaryAssociation = BinaryAssociation(
    name="leftoperator290",
    ends={
        Property(name="FSMActions_ActionExpressionElement291", type=HALL_FSMActions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_BinaryOperator", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
rightexpression292: BinaryAssociation = BinaryAssociation(
    name="rightexpression292",
    ends={
        Property(name="FSMActions_ActionExpressionElement294", type=HALL_FSMActions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_BinaryOperator293", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
expression295: BinaryAssociation = BinaryAssociation(
    name="expression295",
    ends={
        Property(name="FSMActions_ActionExpressionElement296", type=HALL_FSMActions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_UnaryOperator", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_HALL_SystemComponent_Component = Generalization(general=Component, specific=HALL_SystemComponent)
gen_HALL_VisualObject_Component = Generalization(general=Component, specific=HALL_VisualObject)
gen_HALL_TaskObject_Component = Generalization(general=Component, specific=HALL_TaskObject)
gen_HALL_UserProfile_Component = Generalization(general=Component, specific=HALL_UserProfile)
gen_HALL_Geometry_NormalColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_NormalColors)
gen_HALL_Geometry_SelectedColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_SelectedColors)
gen_HALL_Geometry_DisabledColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_DisabledColors)
gen_HALL_Geometry_GeometryData3D_GeometryData = Generalization(general=GeometryData, specific=HALL_Geometry_GeometryData3D)
gen_HALL_Messages_NamedMessageState_MessageState = Generalization(general=MessageState, specific=HALL_Messages_NamedMessageState)
gen_HALL_Geometry_GeometryData2D_GeometryData = Generalization(general=GeometryData, specific=HALL_Geometry_GeometryData2D)
gen_HALL_Geometry_Point3D_Point = Generalization(general=Point, specific=HALL_Geometry_Point3D)
gen_HALL_Geometry_Point2D_Point = Generalization(general=Point, specific=HALL_Geometry_Point2D)
gen_HALL_Instructions_VarRef_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_VarRef)
gen_HALL_Instructions_Literal_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_Literal)
gen_HALL_Instructions_BinaryOperator_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_BinaryOperator)
gen_HALL_Instructions_UnaryOperator_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_UnaryOperator)
gen_HALL_Instructions_GetData_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_GetData)
gen_HALL_Messages_InitialMessageState_MessageState = Generalization(general=MessageState, specific=HALL_Messages_InitialMessageState)
gen_HALL_Instructions_Let_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_Let)
gen_HALL_Instructions_DomainPropertyGet_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_DomainPropertyGet)
gen_HALL_Instructions_GetMessageData_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_GetMessageData)
gen_HALL_Instructions_GetMessageParameter_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_GetMessageParameter)
gen_HALL_Instructions_SetTopDown_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_SetTopDown)
gen_HALL_Instructions_GetState_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_GetState)
gen_HALL_Instructions_SetState_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_SetState)
gen_HALL_Instructions_SetData_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_SetData)
gen_HALL_Instructions_SetMessageData_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_SetMessageData)
gen_HALL_Instructions_SetMessageParameter_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_SetMessageParameter)
gen_HALL_Conditions_Let_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_Let)
gen_HALL_Conditions_UnaryOperator_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_UnaryOperator)
gen_HALL_Conditions_BinaryOperator_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_BinaryOperator)
gen_HALL_Conditions_VarRef_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_VarRef)
gen_HALL_Conditions_Literal_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_Literal)
gen_HALL_Conditions_GetMessageData_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_GetMessageData)
gen_HALL_Conditions_GetMessageParameter_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_GetMessageParameter)
gen_HALL_Conditions_DomainPropertyGet_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_DomainPropertyGet)
gen_HALL_Conditions_GetState_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_GetState)
gen_HALL_Conditions_GetData_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_GetData)
gen_HALL_Actions_GetMessageData_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_GetMessageData)
gen_HALL_Actions_GetMessageParameter_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_GetMessageParameter)
gen_HALL_Actions_MessageInvocation_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_MessageInvocation)
gen_HALL_Actions_UnaryOperator_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_UnaryOperator)
gen_HALL_Actions_GetData_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_GetData)
gen_HALL_Actions_DomainPropertySet_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_DomainPropertySet)
gen_HALL_Actions_Enable_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_Enable)
gen_HALL_Actions_VarRef_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_VarRef)
gen_HALL_Actions_Literal_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_Literal)
gen_HALL_Actions_BinaryOperator_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_BinaryOperator)
gen_HALL_Actions_Let_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_Let)
gen_HALL_Actions_DomainPropertyGet_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_DomainPropertyGet)
gen_HALL_FSM_NamedState_State = Generalization(general=State, specific=HALL_FSM_NamedState)
gen_HALL_FSM_InitialState_State = Generalization(general=State, specific=HALL_FSM_InitialState)
gen_HALL_FSMInstructions_BinaryOperator_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_BinaryOperator)
gen_HALL_FSMInstructions_UnaryOperator_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_UnaryOperator)
gen_HALL_FSMInstructions_GetData_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_GetData)
gen_HALL_FSMInstructions_GetState_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_GetState)
gen_HALL_FSMInstructions_SetState_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_SetState)
gen_HALL_FSMInstructions_SetData_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_SetData)
gen_HALL_Trigger_MessageNotification_TriggerExpressionElement = Generalization(general=TriggerExpressionElement, specific=HALL_Trigger_MessageNotification)
gen_HALL_Trigger_DomainEventFired_TriggerExpressionElement = Generalization(general=TriggerExpressionElement, specific=HALL_Trigger_DomainEventFired)
gen_HALL_FSMInstructions_VarRef_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_VarRef)
gen_HALL_FSMInstructions_Literal_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_Literal)
gen_HALL_FSMConditions_Literal_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_Literal)
gen_HALL_FSMConditions_VarRef_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_VarRef)
gen_HALL_FSMConditions_BinaryOperator_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_BinaryOperator)
gen_HALL_FSMConditions_UnaryOperator_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_UnaryOperator)
gen_HALL_FSMConditions_GetState_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_GetState)
gen_HALL_FSMConditions_GetData_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_GetData)
gen_HALL_FSMInstructions_Let_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_Let)
gen_HALL_FSMInstructions_DomainPropertyGet_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_DomainPropertyGet)
gen_HALL_FSMActions_Literal_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_Literal)
gen_HALL_FSMActions_DomainPropertyGet_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_DomainPropertyGet)
gen_HALL_FSMActions_Let_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_Let)
gen_HALL_FSMActions_MessageInvocation_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_MessageInvocation)
gen_HALL_FSMActions_Enable_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_FSMActions_Enable)
gen_HALL_FSMActions_DomainPropertySet_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_DomainPropertySet)
gen_HALL_FSMConditions_DomainPropertyGet_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_DomainPropertyGet)
gen_HALL_FSMConditions_Let_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_Let)
gen_HALL_FSMActions_VarRef_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_VarRef)
gen_HALL_FSMActions_GetData_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_GetData)
gen_HALL_FSMActions_BinaryOperator_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_BinaryOperator)
gen_HALL_FSMActions_UnaryOperator_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_UnaryOperator)

# Domain Model
domain_model = DomainModel(
    name="HALL",
    types={HALL_UserProfile, HALL_Component, HALL_Data, FSM, MessageHandler, HALL_SystemComponent, HALL_Model, HALL_VisualObject, Component, ColorData, GeometryData, HALL_TaskObject, HALL_Goal, MessageDefinition, HALL_Geometry_Color, RGBColor, ColorState, HALL_Geometry_RGBColor, Color, HALL_Parameter, HALL_Geometry_SelectedColors, HALL_Geometry_DisabledColors, HALL_Geometry_ColorData, SelectedColors, DisabledColors, NormalColors, Geometry_HALL_VisualObject, HALL_Geometry_GeometryData, HALL_Geometry_GeometryData3D, Face, HALL_Geometry_ColorState, AlphaTransparency, HALL_Geometry_AlphaTransparency, HALL_Geometry_NormalColors, HALL_Geometry_Point, HALL_Messages_MessageTransition, MessageState, Conditions_PreConditionMessageExpression, Instructions_PosConditionMessageExpression, Actions_ActionMessageExpression, HALL_Messages_NamedMessageState, HALL_Messages_MessageDefinition, Messages_HALL_Model, Messages_HALL_Parameter, HALL_Geometry_GeometryData2D, Point2D, HALL_Geometry_Face, Point3D, GeometryData3D, HALL_Geometry_Point3D, Point, HALL_Geometry_Point2D, GeometryData2D, Instructions_PosConditionMessageExpressionElement, HALL_Instructions_PosConditionMessageExpressionElement, HALL_Instructions_VarRef, PosConditionMessageExpressionElement, HALL_Instructions_Literal, HALL_Instructions_BinaryOperator, HALL_Instructions_UnaryOperator, HALL_Instructions_GetData, Instructions_HALL_Component, Messages_HALL_Data, HALL_Messages_MessageHandler, NamedMessageState, InitialMessageState, Messages_HALL_Component, HALL_Messages_MessageState, MessageTransition, HALL_Messages_InitialMessageState, HALL_Instructions_PosConditionMessageExpression, HALL_Instructions_Let, HALL_Instructions_DomainPropertyGet, HALL_Instructions_GetMessageData, HALL_Instructions_GetMessageParameter, HALL_Instructions_SetTopDown, HALL_Conditions_PreConditionMessageExpression, HALL_Instructions_GetState, HALL_Instructions_SetState, HALL_Instructions_SetData, HALL_Instructions_SetMessageData, HALL_Instructions_SetMessageParameter, HALL_Conditions_Let, HALL_Conditions_UnaryOperator, HALL_Conditions_BinaryOperator, HALL_Actions_ActionMessageExpression, Actions_ActionMessageExpressionElement, Conditions_PreConditionMessageExpressionElement, HALL_Conditions_PreConditionMessageExpressionElement, HALL_Conditions_VarRef, PreConditionMessageExpressionElement, HALL_Conditions_Literal, HALL_Conditions_GetMessageData, HALL_Conditions_GetMessageParameter, HALL_Conditions_DomainPropertyGet, HALL_Conditions_GetState, Conditions_HALL_Component, HALL_Conditions_GetData, HALL_Actions_GetMessageData, HALL_Actions_GetMessageParameter, HALL_Actions_MessageInvocation, HALL_Actions_UnaryOperator, HALL_Actions_GetData, Actions_HALL_Component, HALL_Actions_DomainPropertySet, HALL_Actions_Enable, HALL_Actions_ActionMessageExpressionElement, HALL_Actions_VarRef, ActionMessageExpressionElement, HALL_Actions_Literal, HALL_Actions_BinaryOperator, HALL_Actions_Let, HALL_Actions_DomainPropertyGet, HALL_FSM_Transition, FSMConditions_PreConditionExpression, FSMInstructions_PosConditionExpression, FSMActions_ActionExpression, Trigger_TriggerExpression, HALL_FSM_State, Transition, HALL_Trigger_TriggerExpression, Trigger_TriggerExpressionElement, HALL_FSM_FSM, FSM_HALL_Component, InitialState, NamedState, HALL_FSM_NamedState, State, HALL_FSM_InitialState, HALL_FSMInstructions_BinaryOperator, HALL_FSMInstructions_UnaryOperator, HALL_FSMInstructions_GetData, FSMInstructions_HALL_Component, HALL_FSMInstructions_GetState, HALL_FSMInstructions_SetState, HALL_FSMInstructions_SetData, HALL_Trigger_TriggerExpressionElement, HALL_Trigger_MessageNotification, TriggerExpressionElement, HALL_Trigger_DomainEventFired, HALL_FSMInstructions_PosConditionExpression, FSMInstructions_PosConditionExpressionElement, HALL_FSMInstructions_PosConditionExpressionElement, HALL_FSMInstructions_VarRef, PosConditionExpressionElement, HALL_FSMInstructions_Literal, HALL_FSMConditions_Literal, PreConditionExpressionElement, HALL_FSMConditions_VarRef, HALL_FSMConditions_BinaryOperator, HALL_FSMConditions_UnaryOperator, HALL_FSMConditions_GetState, FSMConditions_HALL_Component, HALL_FSMConditions_GetData, HALL_FSMInstructions_Let, HALL_FSMInstructions_DomainPropertyGet, HALL_FSMConditions_PreConditionExpression, FSMConditions_PreConditionExpressionElement, HALL_FSMConditions_PreConditionExpressionElement, HALL_FSMActions_Literal, HALL_FSMActions_DomainPropertyGet, HALL_FSMActions_Let, HALL_FSMActions_MessageInvocation, HALL_FSMActions_Enable, HALL_FSMActions_DomainPropertySet, HALL_FSMConditions_DomainPropertyGet, HALL_FSMConditions_Let, HALL_FSMActions_ActionExpression, FSMActions_ActionExpressionElement, HALL_FSMActions_ActionExpressionElement, HALL_FSMActions_VarRef, ActionExpressionElement, HALL_FSMActions_GetData, FSMActions_HALL_Component, HALL_FSMActions_BinaryOperator, HALL_FSMActions_UnaryOperator},
    associations={geometryData1, visualObjectInv2, componentSet4, componentSetInv6, data8, FSM9, messageHandlerSet10, colorData0, taskObject26, userProfileInv27, componentSet30, componentSetInv34, goal37, taskObjectInv38, componentSet41, componentSetInv45, systemComponentInv11, componentSet13, componentSetInv16, userProfile19, systemComponent21, messageDefinition23, visualObject24, ambianceColor56, difuseColor57, specularColor59, foregroundColorInv61, backgroundColorInv62, ambianceColorInv64, difuseColorInv65, specularColorInv67, goalInv48, parameterInv50, dataInvMessageDefinition52, dataInvComponent54, normalColorsInv76, selectedColorsInv78, disabledColorsInv80, selectedColors82, disabledColors83, normalColors84, colorDataInv85, geometryDataInv87, foregroundColor69, backgroundColor71, alphaTransparency73, alphaTransparencyInv74, transitionsInvMessageState97, stateRef98, PreCondition100, PosCondition101, ActionMessage102, messageStateInv103, messageDefinitionInv105, parameter107, face89, point2d90, point3d91, faceInv93, point2dInv94, point2dInv96, PosConditionInv117, PosConditionSet119, PosConditionSetInv120, leftexpression122, rightexpression123, expression126, data108, messageState110, initialMessageState111, messageHandlerSetInv112, transitions114, initialMessageStateInv115, value140, in_142, initialization144, value147, PreConditionInv149, reference128, reference129, reference131, value133, reference135, value138, reference155, in_157, initialization158, expression161, leftexpression163, rightexpression165, ActionMessageInv168, ActionMessageSet170, PreConditionSet151, PreConditionSetInv152, reference154, actualset182, expression184, reference186, value187, ActionMessageSetInv171, leftexpression173, rightexpression174, in_177, initialization179, source204, stateRef206, PreCondition208, PosCondition210, Action212, Trigger213, transitions214, TriggerExpressionSet215, TriggerInv216, value189, reference191, FSMInv194, initialState197, state198, fsm200, fsm202, rightexpression228, leftexpression229, expression232, reference234, reference235, reference237, TriggerExpressionSetInv218, PosConditionSet220, PosConditionInv222, PosConditionSetInv225, PreConditionSetInv254, rightexpression257, leftexpression258, expression261, reference263, value239, reference241, in_244, initialization246, PreConditionSet249, PreConditionInv251, in_276, initialization277, actualset280, value282, message284, reference264, initialization266, in_268, ActionInv271, ActionExpressionSet273, ActionExpressionSetInv274, value287, reference289, leftoperator290, rightexpression292, expression295},
    generalizations={gen_HALL_SystemComponent_Component, gen_HALL_VisualObject_Component, gen_HALL_TaskObject_Component, gen_HALL_UserProfile_Component, gen_HALL_Geometry_NormalColors_ColorState, gen_HALL_Geometry_SelectedColors_ColorState, gen_HALL_Geometry_DisabledColors_ColorState, gen_HALL_Geometry_GeometryData3D_GeometryData, gen_HALL_Messages_NamedMessageState_MessageState, gen_HALL_Geometry_GeometryData2D_GeometryData, gen_HALL_Geometry_Point3D_Point, gen_HALL_Geometry_Point2D_Point, gen_HALL_Instructions_VarRef_PosConditionMessageExpressionElement, gen_HALL_Instructions_Literal_PosConditionMessageExpressionElement, gen_HALL_Instructions_BinaryOperator_PosConditionMessageExpressionElement, gen_HALL_Instructions_UnaryOperator_PosConditionMessageExpressionElement, gen_HALL_Instructions_GetData_PosConditionMessageExpressionElement, gen_HALL_Messages_InitialMessageState_MessageState, gen_HALL_Instructions_Let_PosConditionMessageExpressionElement, gen_HALL_Instructions_DomainPropertyGet_PosConditionMessageExpressionElement, gen_HALL_Instructions_GetMessageData_PosConditionMessageExpressionElement, gen_HALL_Instructions_GetMessageParameter_PosConditionMessageExpressionElement, gen_HALL_Instructions_SetTopDown_PosConditionMessageExpressionElement, gen_HALL_Instructions_GetState_PosConditionMessageExpressionElement, gen_HALL_Instructions_SetState_PosConditionMessageExpressionElement, gen_HALL_Instructions_SetData_PosConditionMessageExpressionElement, gen_HALL_Instructions_SetMessageData_PosConditionMessageExpressionElement, gen_HALL_Instructions_SetMessageParameter_PosConditionMessageExpressionElement, gen_HALL_Conditions_Let_PreConditionMessageExpressionElement, gen_HALL_Conditions_UnaryOperator_PreConditionMessageExpressionElement, gen_HALL_Conditions_BinaryOperator_PreConditionMessageExpressionElement, gen_HALL_Conditions_VarRef_PreConditionMessageExpressionElement, gen_HALL_Conditions_Literal_PreConditionMessageExpressionElement, gen_HALL_Conditions_GetMessageData_PreConditionMessageExpressionElement, gen_HALL_Conditions_GetMessageParameter_PreConditionMessageExpressionElement, gen_HALL_Conditions_DomainPropertyGet_PreConditionMessageExpressionElement, gen_HALL_Conditions_GetState_PreConditionMessageExpressionElement, gen_HALL_Conditions_GetData_PreConditionMessageExpressionElement, gen_HALL_Actions_GetMessageData_ActionMessageExpressionElement, gen_HALL_Actions_GetMessageParameter_ActionMessageExpressionElement, gen_HALL_Actions_MessageInvocation_ActionMessageExpressionElement, gen_HALL_Actions_UnaryOperator_ActionMessageExpressionElement, gen_HALL_Actions_GetData_ActionMessageExpressionElement, gen_HALL_Actions_DomainPropertySet_ActionMessageExpressionElement, gen_HALL_Actions_Enable_ActionMessageExpressionElement, gen_HALL_Actions_VarRef_ActionMessageExpressionElement, gen_HALL_Actions_Literal_ActionMessageExpressionElement, gen_HALL_Actions_BinaryOperator_ActionMessageExpressionElement, gen_HALL_Actions_Let_ActionMessageExpressionElement, gen_HALL_Actions_DomainPropertyGet_ActionMessageExpressionElement, gen_HALL_FSM_NamedState_State, gen_HALL_FSM_InitialState_State, gen_HALL_FSMInstructions_BinaryOperator_PosConditionExpressionElement, gen_HALL_FSMInstructions_UnaryOperator_PosConditionExpressionElement, gen_HALL_FSMInstructions_GetData_PosConditionExpressionElement, gen_HALL_FSMInstructions_GetState_PosConditionExpressionElement, gen_HALL_FSMInstructions_SetState_PosConditionExpressionElement, gen_HALL_FSMInstructions_SetData_PosConditionExpressionElement, gen_HALL_Trigger_MessageNotification_TriggerExpressionElement, gen_HALL_Trigger_DomainEventFired_TriggerExpressionElement, gen_HALL_FSMInstructions_VarRef_PosConditionExpressionElement, gen_HALL_FSMInstructions_Literal_PosConditionExpressionElement, gen_HALL_FSMConditions_Literal_PreConditionExpressionElement, gen_HALL_FSMConditions_VarRef_PreConditionExpressionElement, gen_HALL_FSMConditions_BinaryOperator_PreConditionExpressionElement, gen_HALL_FSMConditions_UnaryOperator_PreConditionExpressionElement, gen_HALL_FSMConditions_GetState_PreConditionExpressionElement, gen_HALL_FSMConditions_GetData_PreConditionExpressionElement, gen_HALL_FSMInstructions_Let_PosConditionExpressionElement, gen_HALL_FSMInstructions_DomainPropertyGet_PosConditionExpressionElement, gen_HALL_FSMActions_Literal_ActionExpressionElement, gen_HALL_FSMActions_DomainPropertyGet_ActionExpressionElement, gen_HALL_FSMActions_Let_ActionExpressionElement, gen_HALL_FSMActions_MessageInvocation_ActionExpressionElement, gen_HALL_FSMActions_Enable_ActionMessageExpressionElement, gen_HALL_FSMActions_DomainPropertySet_ActionExpressionElement, gen_HALL_FSMConditions_DomainPropertyGet_PreConditionExpressionElement, gen_HALL_FSMConditions_Let_PreConditionExpressionElement, gen_HALL_FSMActions_VarRef_ActionExpressionElement, gen_HALL_FSMActions_GetData_ActionExpressionElement, gen_HALL_FSMActions_BinaryOperator_ActionExpressionElement, gen_HALL_FSMActions_UnaryOperator_ActionExpressionElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)