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
GeometryData = Class(name="GeometryData")
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
HALL_TaskObject = Class(name="HALL_TaskObject")
HALL_Goal = Class(name="HALL_Goal")
MessageDefinition = Class(name="MessageDefinition")
Type = Class(name="Type")
HALL_Geometry_Color = Class(name="HALL_Geometry_Color")
RGBColor = Class(name="RGBColor")
ColorState = Class(name="ColorState")
HALL_Geometry_RGBColor = Class(name="HALL_Geometry_RGBColor")
Color = Class(name="Color")
HALL_Geometry_ColorState = Class(name="HALL_Geometry_ColorState", is_abstract=True)
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
HALL_Geometry_GeometryData2D = Class(name="HALL_Geometry_GeometryData2D")
Point2D = Class(name="Point2D")
AlphaTransparency = Class(name="AlphaTransparency")
HALL_Geometry_AlphaTransparency = Class(name="HALL_Geometry_AlphaTransparency")
HALL_Geometry_NormalColors = Class(name="HALL_Geometry_NormalColors")
HALL_Geometry_Point2D = Class(name="HALL_Geometry_Point2D")
GeometryData2D = Class(name="GeometryData2D")
HALL_Geometry_Point = Class(name="HALL_Geometry_Point")
HALL_Messages_MessageTransition = Class(name="HALL_Messages_MessageTransition")
MessageState = Class(name="MessageState")
Conditions_PreConditionMessage = Class(name="Conditions_PreConditionMessage")
Instructions_PosConditionMessage = Class(name="Instructions_PosConditionMessage")
Actions_ActionMessage = Class(name="Actions_ActionMessage")
HALL_Messages_RegularMessageState = Class(name="HALL_Messages_RegularMessageState")
HALL_Messages_MessageDefinition = Class(name="HALL_Messages_MessageDefinition")
Messages_HALL_Model = Class(name="Messages_HALL_Model")
Messages_HALL_Parameter = Class(name="Messages_HALL_Parameter")
HALL_Geometry_Face = Class(name="HALL_Geometry_Face")
Point3D = Class(name="Point3D")
GeometryData3D = Class(name="GeometryData3D")
HALL_Geometry_Point3D = Class(name="HALL_Geometry_Point3D")
Point = Class(name="Point")
InitialMessageState = Class(name="InitialMessageState")
Messages_HALL_Component = Class(name="Messages_HALL_Component")
HALL_Messages_MessageState = Class(name="HALL_Messages_MessageState")
MessageTransition = Class(name="MessageTransition")
HALL_Messages_InitialMessageState = Class(name="HALL_Messages_InitialMessageState")
HALL_Instructions_PosConditionMessage = Class(name="HALL_Instructions_PosConditionMessage")
Instructions_PosConditionMessageExpression = Class(name="Instructions_PosConditionMessageExpression")
HALL_Instructions_PosConditionMessageExpression = Class(name="HALL_Instructions_PosConditionMessageExpression", is_abstract=True)
HALL_Instructions_Literal = Class(name="HALL_Instructions_Literal")
PosConditionMessageExpression = Class(name="PosConditionMessageExpression")
HALL_Instructions_BinaryOperator = Class(name="HALL_Instructions_BinaryOperator")
Messages_HALL_Data = Class(name="Messages_HALL_Data")
HALL_Messages_MessageHandler = Class(name="HALL_Messages_MessageHandler")
RegularMessageState = Class(name="RegularMessageState")
HALL_Instructions_SetState = Class(name="HALL_Instructions_SetState")
State = Class(name="State")
HALL_Instructions_SetData = Class(name="HALL_Instructions_SetData")
HALL_Instructions_SetMessageData = Class(name="HALL_Instructions_SetMessageData")
HALL_Instructions_SetMessageParameter = Class(name="HALL_Instructions_SetMessageParameter")
HALL_Instructions_Let = Class(name="HALL_Instructions_Let")
HALL_Instructions_DomainPropertyGet = Class(name="HALL_Instructions_DomainPropertyGet")
HALL_Instructions_UnaryOperator = Class(name="HALL_Instructions_UnaryOperator")
HALL_Instructions_GetData = Class(name="HALL_Instructions_GetData")
Instructions_HALL_Data = Class(name="Instructions_HALL_Data")
HALL_Instructions_GetState = Class(name="HALL_Instructions_GetState")
Instructions_HALL_Component = Class(name="Instructions_HALL_Component")
Instructions_Let = Class(name="Instructions_Let")
HALL_Conditions_PreConditionMessage = Class(name="HALL_Conditions_PreConditionMessage")
Conditions_PreConditionMessageExpression = Class(name="Conditions_PreConditionMessageExpression")
HALL_Conditions_PreConditionMessageExpression = Class(name="HALL_Conditions_PreConditionMessageExpression", is_abstract=True)
HALL_Conditions_Literal = Class(name="HALL_Conditions_Literal")
PreConditionMessageExpression = Class(name="PreConditionMessageExpression")
HALL_Conditions_GetMessageData = Class(name="HALL_Conditions_GetMessageData")
HALL_Conditions_GetMessageParameter = Class(name="HALL_Conditions_GetMessageParameter")
HALL_Conditions_DomainPropertyGet = Class(name="HALL_Conditions_DomainPropertyGet")
HALL_Conditions_GetState = Class(name="HALL_Conditions_GetState")
Conditions_HALL_Component = Class(name="Conditions_HALL_Component")
HALL_Conditions_GetData = Class(name="HALL_Conditions_GetData")
Conditions_HALL_Data = Class(name="Conditions_HALL_Data")
HALL_Conditions_Let = Class(name="HALL_Conditions_Let")
HALL_Instructions_GetMessageData = Class(name="HALL_Instructions_GetMessageData")
HALL_Instructions_GetMessageParameter = Class(name="HALL_Instructions_GetMessageParameter")
HALL_Instructions_SetTopDown = Class(name="HALL_Instructions_SetTopDown")
HALL_Instructions_VarRef = Class(name="HALL_Instructions_VarRef")
HALL_Conditions_VarRef = Class(name="HALL_Conditions_VarRef")
Conditions_Let = Class(name="Conditions_Let")
HALL_Actions_ActionMessage = Class(name="HALL_Actions_ActionMessage")
Actions_ActionMessageExpression = Class(name="Actions_ActionMessageExpression")
HALL_Actions_ActionMessageExpression = Class(name="HALL_Actions_ActionMessageExpression", is_abstract=True)
HALL_Actions_VarRef = Class(name="HALL_Actions_VarRef")
ActionMessageExpression = Class(name="ActionMessageExpression")
Actions_Let = Class(name="Actions_Let")
HALL_Actions_Literal = Class(name="HALL_Actions_Literal")
HALL_Actions_BinaryOperator = Class(name="HALL_Actions_BinaryOperator")
HALL_Actions_Let = Class(name="HALL_Actions_Let")
HALL_Conditions_UnaryOperator = Class(name="HALL_Conditions_UnaryOperator")
HALL_Conditions_BinaryOperator = Class(name="HALL_Conditions_BinaryOperator")
HALL_Actions_MessageInvocation = Class(name="HALL_Actions_MessageInvocation")
HALL_Actions_UnaryOperator = Class(name="HALL_Actions_UnaryOperator")
HALL_Actions_GetData = Class(name="HALL_Actions_GetData")
Actions_HALL_Component = Class(name="Actions_HALL_Component")
HALL_Actions_DomainPropertySet = Class(name="HALL_Actions_DomainPropertySet")
HALL_Actions_Enable = Class(name="HALL_Actions_Enable")
HALL_Actions_DomainPropertyGet = Class(name="HALL_Actions_DomainPropertyGet")
HALL_Actions_GetMessageData = Class(name="HALL_Actions_GetMessageData")
HALL_Actions_GetMessageParameter = Class(name="HALL_Actions_GetMessageParameter")
HALL_FSM_InitialState = Class(name="HALL_FSM_InitialState")
HALL_FSM_Transition = Class(name="HALL_FSM_Transition")
FSMConditions_PreCondition = Class(name="FSMConditions_PreCondition")
FSMInstructions_PosCondition = Class(name="FSMInstructions_PosCondition")
FSMActions_Action = Class(name="FSMActions_Action")
Trigger_Trigger = Class(name="Trigger_Trigger")
HALL_FSM_State = Class(name="HALL_FSM_State", is_abstract=True)
Transition = Class(name="Transition")
HALL_FSM_FSM = Class(name="HALL_FSM_FSM")
FSM_HALL_Component = Class(name="FSM_HALL_Component")
InitialState = Class(name="InitialState")
RegularState = Class(name="RegularState")
HALL_FSM_RegularState = Class(name="HALL_FSM_RegularState")
HALL_Trigger_DomainEventFired = Class(name="HALL_Trigger_DomainEventFired")
HALL_FSMInstructions_PosCondition = Class(name="HALL_FSMInstructions_PosCondition")
FSMInstructions_PosConditionExpression = Class(name="FSMInstructions_PosConditionExpression")
HALL_FSMInstructions_PosConditionExpression = Class(name="HALL_FSMInstructions_PosConditionExpression", is_abstract=True)
HALL_FSMInstructions_Literal = Class(name="HALL_FSMInstructions_Literal")
PosConditionExpression = Class(name="PosConditionExpression")
HALL_FSMInstructions_BinaryOperator = Class(name="HALL_FSMInstructions_BinaryOperator")
HALL_FSMInstructions_UnaryOperator = Class(name="HALL_FSMInstructions_UnaryOperator")
HALL_FSMInstructions_GetData = Class(name="HALL_FSMInstructions_GetData")
FSMInstructions_HALL_Component = Class(name="FSMInstructions_HALL_Component")
HALL_Trigger_Trigger = Class(name="HALL_Trigger_Trigger")
Trigger_TriggerExpression = Class(name="Trigger_TriggerExpression")
HALL_Trigger_TriggerExpression = Class(name="HALL_Trigger_TriggerExpression", is_abstract=True)
HALL_Trigger_MessageNotification = Class(name="HALL_Trigger_MessageNotification")
TriggerExpression = Class(name="TriggerExpression")
FSMInstructions_HALL_Data = Class(name="FSMInstructions_HALL_Data")
HALL_FSMInstructions_Let = Class(name="HALL_FSMInstructions_Let")
HALL_FSMInstructions_DomainPropertyGet = Class(name="HALL_FSMInstructions_DomainPropertyGet")
HALL_FSMInstructions_VarRef = Class(name="HALL_FSMInstructions_VarRef")
FSMInstructions_Let = Class(name="FSMInstructions_Let")
HALL_FSMConditions_PreCondition = Class(name="HALL_FSMConditions_PreCondition")
FSMConditions_PreConditionExpression = Class(name="FSMConditions_PreConditionExpression")
HALL_FSMConditions_PreConditionExpression = Class(name="HALL_FSMConditions_PreConditionExpression", is_abstract=True)
HALL_FSMConditions_Literal = Class(name="HALL_FSMConditions_Literal")
PreConditionExpression = Class(name="PreConditionExpression")
HALL_FSMConditions_BinaryOperator = Class(name="HALL_FSMConditions_BinaryOperator")
HALL_FSMInstructions_GetState = Class(name="HALL_FSMInstructions_GetState")
HALL_FSMInstructions_SetState = Class(name="HALL_FSMInstructions_SetState")
HALL_FSMInstructions_SetData = Class(name="HALL_FSMInstructions_SetData")
HALL_FSMConditions_GetData = Class(name="HALL_FSMConditions_GetData")
FSMConditions_HALL_Data = Class(name="FSMConditions_HALL_Data")
HALL_FSMConditions_DomainPropertyGet = Class(name="HALL_FSMConditions_DomainPropertyGet")
HALL_FSMConditions_Let = Class(name="HALL_FSMConditions_Let")
HALL_FSMConditions_VarRef = Class(name="HALL_FSMConditions_VarRef")
FSMConditions_Let = Class(name="FSMConditions_Let")
HALL_FSMActions_Action = Class(name="HALL_FSMActions_Action")
FSMActions_ActionExpression = Class(name="FSMActions_ActionExpression")
HALL_FSMActions_ActionExpression = Class(name="HALL_FSMActions_ActionExpression")
HALL_FSMActions_Literal = Class(name="HALL_FSMActions_Literal")
ActionExpression = Class(name="ActionExpression")
HALL_FSMConditions_UnaryOperator = Class(name="HALL_FSMConditions_UnaryOperator")
HALL_FSMConditions_GetState = Class(name="HALL_FSMConditions_GetState")
FSMConditions_HALL_Component = Class(name="FSMConditions_HALL_Component")
HALL_FSMActions_Enable = Class(name="HALL_FSMActions_Enable")
HALL_FSMActions_DomainPropertySet = Class(name="HALL_FSMActions_DomainPropertySet")
HALL_FSMActions_GetData = Class(name="HALL_FSMActions_GetData")
FSMActions_HALL_Data = Class(name="FSMActions_HALL_Data")
HALL_FSMActions_BinaryOperator = Class(name="HALL_FSMActions_BinaryOperator")
HALL_FSMActions_DomainPropertyGet = Class(name="HALL_FSMActions_DomainPropertyGet")
HALL_FSMActions_Let = Class(name="HALL_FSMActions_Let")
HALL_FSMActions_MessageInvocation = Class(name="HALL_FSMActions_MessageInvocation")
HALL_Types_Type = Class(name="HALL_Types_Type", is_abstract=True)
HALL_Types_SimpleType = Class(name="HALL_Types_SimpleType", is_abstract=True)
Set = Class(name="Set")
HALL_Types_Set = Class(name="HALL_Types_Set")
SimpleType = Class(name="SimpleType")
HALL_Types_Boolean = Class(name="HALL_Types_Boolean")
HALL_Types_String = Class(name="HALL_Types_String")
HALL_Types_Number = Class(name="HALL_Types_Number")
HALL_FSMActions_UnaryOperator = Class(name="HALL_FSMActions_UnaryOperator")
HALL_FSMActions_VarRef = Class(name="HALL_FSMActions_VarRef")
FSMActions_Let = Class(name="FSMActions_Let")

# GeometryData class attributes and methods

# HALL_UserProfile class attributes and methods
HALL_UserProfile_numberofcompletedtasks: Property = Property(name="numberofcompletedtasks", type=IntegerType)
HALL_UserProfile.attributes={HALL_UserProfile_numberofcompletedtasks}

# HALL_Component class attributes and methods
HALL_Component_name: Property = Property(name="name", type=StringType)
HALL_Component.attributes={HALL_Component_name}

# HALL_Data class attributes and methods
HALL_Data_currentValue: Property = Property(name="currentValue", type=StringType)
HALL_Data_name: Property = Property(name="name", type=StringType)
HALL_Data_initValue: Property = Property(name="initValue", type=StringType)
HALL_Data.attributes={HALL_Data_name, HALL_Data_initValue, HALL_Data_currentValue}

# FSM class attributes and methods

# MessageHandler class attributes and methods

# HALL_SystemComponent class attributes and methods

# HALL_Model class attributes and methods

# HALL_VisualObject class attributes and methods
HALL_VisualObject_vtype: Property = Property(name="vtype", type=StringType)
HALL_VisualObject.attributes={HALL_VisualObject_vtype}

# Component class attributes and methods

# ColorData class attributes and methods

# HALL_TaskObject class attributes and methods
HALL_TaskObject_completionTime: Property = Property(name="completionTime", type=IntegerType)
HALL_TaskObject_numberofgoalscompleted: Property = Property(name="numberofgoalscompleted", type=IntegerType)
HALL_TaskObject.attributes={HALL_TaskObject_numberofgoalscompleted, HALL_TaskObject_completionTime}

# HALL_Goal class attributes and methods
HALL_Goal_condition: Property = Property(name="condition", type=StringType)
HALL_Goal.attributes={HALL_Goal_condition}

# MessageDefinition class attributes and methods

# Type class attributes and methods

# HALL_Geometry_Color class attributes and methods

# RGBColor class attributes and methods

# ColorState class attributes and methods

# HALL_Geometry_RGBColor class attributes and methods
HALL_Geometry_RGBColor_redValue: Property = Property(name="redValue", type=IntegerType)
HALL_Geometry_RGBColor_greenValue: Property = Property(name="greenValue", type=IntegerType)
HALL_Geometry_RGBColor_blueValue: Property = Property(name="blueValue", type=IntegerType)
HALL_Geometry_RGBColor.attributes={HALL_Geometry_RGBColor_greenValue, HALL_Geometry_RGBColor_blueValue, HALL_Geometry_RGBColor_redValue}

# Color class attributes and methods

# HALL_Geometry_ColorState class attributes and methods

# HALL_Parameter class attributes and methods
HALL_Parameter_name: Property = Property(name="name", type=StringType)
HALL_Parameter.attributes={HALL_Parameter_name}

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

# HALL_Geometry_GeometryData2D class attributes and methods
HALL_Geometry_GeometryData2D_labelText: Property = Property(name="labelText", type=StringType)
HALL_Geometry_GeometryData2D.attributes={HALL_Geometry_GeometryData2D_labelText}

# Point2D class attributes and methods

# AlphaTransparency class attributes and methods

# HALL_Geometry_AlphaTransparency class attributes and methods
HALL_Geometry_AlphaTransparency_value: Property = Property(name="value", type=IntegerType)
HALL_Geometry_AlphaTransparency.attributes={HALL_Geometry_AlphaTransparency_value}

# HALL_Geometry_NormalColors class attributes and methods

# HALL_Geometry_Point2D class attributes and methods

# GeometryData2D class attributes and methods

# HALL_Geometry_Point class attributes and methods
HALL_Geometry_Point_xCoord: Property = Property(name="xCoord", type=IntegerType)
HALL_Geometry_Point_yCoord: Property = Property(name="yCoord", type=IntegerType)
HALL_Geometry_Point.attributes={HALL_Geometry_Point_yCoord, HALL_Geometry_Point_xCoord}

# HALL_Messages_MessageTransition class attributes and methods
HALL_Messages_MessageTransition_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageTransition.attributes={HALL_Messages_MessageTransition_name}

# MessageState class attributes and methods

# Conditions_PreConditionMessage class attributes and methods

# Instructions_PosConditionMessage class attributes and methods

# Actions_ActionMessage class attributes and methods

# HALL_Messages_RegularMessageState class attributes and methods

# HALL_Messages_MessageDefinition class attributes and methods
HALL_Messages_MessageDefinition_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageDefinition.attributes={HALL_Messages_MessageDefinition_name}

# Messages_HALL_Model class attributes and methods

# Messages_HALL_Parameter class attributes and methods

# HALL_Geometry_Face class attributes and methods
HALL_Geometry_Face_labelText: Property = Property(name="labelText", type=StringType)
HALL_Geometry_Face.attributes={HALL_Geometry_Face_labelText}

# Point3D class attributes and methods

# GeometryData3D class attributes and methods

# HALL_Geometry_Point3D class attributes and methods
HALL_Geometry_Point3D_zCoord: Property = Property(name="zCoord", type=IntegerType)
HALL_Geometry_Point3D.attributes={HALL_Geometry_Point3D_zCoord}

# Point class attributes and methods

# InitialMessageState class attributes and methods

# Messages_HALL_Component class attributes and methods

# HALL_Messages_MessageState class attributes and methods
HALL_Messages_MessageState_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageState_isEnd: Property = Property(name="isEnd", type=BooleanType)
HALL_Messages_MessageState_isContinue: Property = Property(name="isContinue", type=BooleanType)
HALL_Messages_MessageState_isActive: Property = Property(name="isActive", type=BooleanType)
HALL_Messages_MessageState.attributes={HALL_Messages_MessageState_name, HALL_Messages_MessageState_isEnd, HALL_Messages_MessageState_isContinue, HALL_Messages_MessageState_isActive}

# MessageTransition class attributes and methods

# HALL_Messages_InitialMessageState class attributes and methods

# HALL_Instructions_PosConditionMessage class attributes and methods

# Instructions_PosConditionMessageExpression class attributes and methods

# HALL_Instructions_PosConditionMessageExpression class attributes and methods

# HALL_Instructions_Literal class attributes and methods
HALL_Instructions_Literal_value: Property = Property(name="value", type=StringType)
HALL_Instructions_Literal.attributes={HALL_Instructions_Literal_value}

# PosConditionMessageExpression class attributes and methods

# HALL_Instructions_BinaryOperator class attributes and methods
HALL_Instructions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Instructions_BinaryOperator.attributes={HALL_Instructions_BinaryOperator_operatorname}

# Messages_HALL_Data class attributes and methods

# HALL_Messages_MessageHandler class attributes and methods

# RegularMessageState class attributes and methods

# HALL_Instructions_SetState class attributes and methods

# State class attributes and methods

# HALL_Instructions_SetData class attributes and methods

# HALL_Instructions_SetMessageData class attributes and methods
HALL_Instructions_SetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Instructions_SetMessageData.attributes={HALL_Instructions_SetMessageData_field}

# HALL_Instructions_SetMessageParameter class attributes and methods
HALL_Instructions_SetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Instructions_SetMessageParameter.attributes={HALL_Instructions_SetMessageParameter_field}

# HALL_Instructions_Let class attributes and methods
HALL_Instructions_Let_name: Property = Property(name="name", type=StringType)
HALL_Instructions_Let.attributes={HALL_Instructions_Let_name}

# HALL_Instructions_DomainPropertyGet class attributes and methods
HALL_Instructions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_Instructions_DomainPropertyGet.attributes={HALL_Instructions_DomainPropertyGet_name}

# HALL_Instructions_UnaryOperator class attributes and methods
HALL_Instructions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Instructions_UnaryOperator.attributes={HALL_Instructions_UnaryOperator_operatorname}

# HALL_Instructions_GetData class attributes and methods

# Instructions_HALL_Data class attributes and methods

# HALL_Instructions_GetState class attributes and methods

# Instructions_HALL_Component class attributes and methods

# Instructions_Let class attributes and methods

# HALL_Conditions_PreConditionMessage class attributes and methods

# Conditions_PreConditionMessageExpression class attributes and methods

# HALL_Conditions_PreConditionMessageExpression class attributes and methods

# HALL_Conditions_Literal class attributes and methods
HALL_Conditions_Literal_value: Property = Property(name="value", type=StringType)
HALL_Conditions_Literal.attributes={HALL_Conditions_Literal_value}

# PreConditionMessageExpression class attributes and methods

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

# Conditions_HALL_Data class attributes and methods

# HALL_Conditions_Let class attributes and methods
HALL_Conditions_Let_name: Property = Property(name="name", type=StringType)
HALL_Conditions_Let.attributes={HALL_Conditions_Let_name}

# HALL_Instructions_GetMessageData class attributes and methods
HALL_Instructions_GetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Instructions_GetMessageData.attributes={HALL_Instructions_GetMessageData_field}

# HALL_Instructions_GetMessageParameter class attributes and methods
HALL_Instructions_GetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Instructions_GetMessageParameter.attributes={HALL_Instructions_GetMessageParameter_field}

# HALL_Instructions_SetTopDown class attributes and methods

# HALL_Instructions_VarRef class attributes and methods

# HALL_Conditions_VarRef class attributes and methods

# Conditions_Let class attributes and methods

# HALL_Actions_ActionMessage class attributes and methods

# Actions_ActionMessageExpression class attributes and methods

# HALL_Actions_ActionMessageExpression class attributes and methods

# HALL_Actions_VarRef class attributes and methods

# ActionMessageExpression class attributes and methods

# Actions_Let class attributes and methods

# HALL_Actions_Literal class attributes and methods
HALL_Actions_Literal_value: Property = Property(name="value", type=StringType)
HALL_Actions_Literal.attributes={HALL_Actions_Literal_value}

# HALL_Actions_BinaryOperator class attributes and methods
HALL_Actions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Actions_BinaryOperator.attributes={HALL_Actions_BinaryOperator_operatorname}

# HALL_Actions_Let class attributes and methods

# HALL_Conditions_UnaryOperator class attributes and methods
HALL_Conditions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Conditions_UnaryOperator.attributes={HALL_Conditions_UnaryOperator_operatorname}

# HALL_Conditions_BinaryOperator class attributes and methods
HALL_Conditions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Conditions_BinaryOperator.attributes={HALL_Conditions_BinaryOperator_operatorname}

# HALL_Actions_MessageInvocation class attributes and methods
HALL_Actions_MessageInvocation_isTopDown: Property = Property(name="isTopDown", type=BooleanType)
HALL_Actions_MessageInvocation.attributes={HALL_Actions_MessageInvocation_isTopDown}

# HALL_Actions_UnaryOperator class attributes and methods
HALL_Actions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Actions_UnaryOperator.attributes={HALL_Actions_UnaryOperator_operatorname}

# HALL_Actions_GetData class attributes and methods

# Actions_HALL_Component class attributes and methods

# HALL_Actions_DomainPropertySet class attributes and methods
HALL_Actions_DomainPropertySet_name: Property = Property(name="name", type=StringType)
HALL_Actions_DomainPropertySet.attributes={HALL_Actions_DomainPropertySet_name}

# HALL_Actions_Enable class attributes and methods

# HALL_Actions_DomainPropertyGet class attributes and methods
HALL_Actions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_Actions_DomainPropertyGet.attributes={HALL_Actions_DomainPropertyGet_name}

# HALL_Actions_GetMessageData class attributes and methods
HALL_Actions_GetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Actions_GetMessageData.attributes={HALL_Actions_GetMessageData_field}

# HALL_Actions_GetMessageParameter class attributes and methods
HALL_Actions_GetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Actions_GetMessageParameter.attributes={HALL_Actions_GetMessageParameter_field}

# HALL_FSM_InitialState class attributes and methods

# HALL_FSM_Transition class attributes and methods
HALL_FSM_Transition_name: Property = Property(name="name", type=StringType)
HALL_FSM_Transition.attributes={HALL_FSM_Transition_name}

# FSMConditions_PreCondition class attributes and methods

# FSMInstructions_PosCondition class attributes and methods

# FSMActions_Action class attributes and methods

# Trigger_Trigger class attributes and methods

# HALL_FSM_State class attributes and methods
HALL_FSM_State_isActive: Property = Property(name="isActive", type=BooleanType)
HALL_FSM_State_name: Property = Property(name="name", type=StringType)
HALL_FSM_State.attributes={HALL_FSM_State_isActive, HALL_FSM_State_name}

# Transition class attributes and methods

# HALL_FSM_FSM class attributes and methods

# FSM_HALL_Component class attributes and methods

# InitialState class attributes and methods

# RegularState class attributes and methods

# HALL_FSM_RegularState class attributes and methods

# HALL_Trigger_DomainEventFired class attributes and methods
HALL_Trigger_DomainEventFired_name: Property = Property(name="name", type=StringType)
HALL_Trigger_DomainEventFired.attributes={HALL_Trigger_DomainEventFired_name}

# HALL_FSMInstructions_PosCondition class attributes and methods

# FSMInstructions_PosConditionExpression class attributes and methods

# HALL_FSMInstructions_PosConditionExpression class attributes and methods

# HALL_FSMInstructions_Literal class attributes and methods
HALL_FSMInstructions_Literal_value: Property = Property(name="value", type=StringType)
HALL_FSMInstructions_Literal.attributes={HALL_FSMInstructions_Literal_value}

# PosConditionExpression class attributes and methods

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

# HALL_Trigger_Trigger class attributes and methods

# Trigger_TriggerExpression class attributes and methods

# HALL_Trigger_TriggerExpression class attributes and methods

# HALL_Trigger_MessageNotification class attributes and methods

# TriggerExpression class attributes and methods

# FSMInstructions_HALL_Data class attributes and methods

# HALL_FSMInstructions_Let class attributes and methods
HALL_FSMInstructions_Let_name: Property = Property(name="name", type=StringType)
HALL_FSMInstructions_Let.attributes={HALL_FSMInstructions_Let_name}

# HALL_FSMInstructions_DomainPropertyGet class attributes and methods
HALL_FSMInstructions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMInstructions_DomainPropertyGet.attributes={HALL_FSMInstructions_DomainPropertyGet_name}

# HALL_FSMInstructions_VarRef class attributes and methods

# FSMInstructions_Let class attributes and methods

# HALL_FSMConditions_PreCondition class attributes and methods

# FSMConditions_PreConditionExpression class attributes and methods

# HALL_FSMConditions_PreConditionExpression class attributes and methods

# HALL_FSMConditions_Literal class attributes and methods
HALL_FSMConditions_Literal_value: Property = Property(name="value", type=StringType)
HALL_FSMConditions_Literal.attributes={HALL_FSMConditions_Literal_value}

# PreConditionExpression class attributes and methods

# HALL_FSMConditions_BinaryOperator class attributes and methods
HALL_FSMConditions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMConditions_BinaryOperator.attributes={HALL_FSMConditions_BinaryOperator_operatorname}

# HALL_FSMInstructions_GetState class attributes and methods

# HALL_FSMInstructions_SetState class attributes and methods

# HALL_FSMInstructions_SetData class attributes and methods
HALL_FSMInstructions_SetData_field: Property = Property(name="field", type=StringType)
HALL_FSMInstructions_SetData.attributes={HALL_FSMInstructions_SetData_field}

# HALL_FSMConditions_GetData class attributes and methods

# FSMConditions_HALL_Data class attributes and methods

# HALL_FSMConditions_DomainPropertyGet class attributes and methods
HALL_FSMConditions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMConditions_DomainPropertyGet.attributes={HALL_FSMConditions_DomainPropertyGet_name}

# HALL_FSMConditions_Let class attributes and methods
HALL_FSMConditions_Let_name: Property = Property(name="name", type=StringType)
HALL_FSMConditions_Let.attributes={HALL_FSMConditions_Let_name}

# HALL_FSMConditions_VarRef class attributes and methods

# FSMConditions_Let class attributes and methods

# HALL_FSMActions_Action class attributes and methods

# FSMActions_ActionExpression class attributes and methods

# HALL_FSMActions_ActionExpression class attributes and methods

# HALL_FSMActions_Literal class attributes and methods
HALL_FSMActions_Literal_value: Property = Property(name="value", type=StringType)
HALL_FSMActions_Literal.attributes={HALL_FSMActions_Literal_value}

# ActionExpression class attributes and methods

# HALL_FSMConditions_UnaryOperator class attributes and methods
HALL_FSMConditions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMConditions_UnaryOperator.attributes={HALL_FSMConditions_UnaryOperator_operatorname}

# HALL_FSMConditions_GetState class attributes and methods

# FSMConditions_HALL_Component class attributes and methods

# HALL_FSMActions_Enable class attributes and methods

# HALL_FSMActions_DomainPropertySet class attributes and methods
HALL_FSMActions_DomainPropertySet_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_DomainPropertySet.attributes={HALL_FSMActions_DomainPropertySet_name}

# HALL_FSMActions_GetData class attributes and methods

# FSMActions_HALL_Data class attributes and methods

# HALL_FSMActions_BinaryOperator class attributes and methods
HALL_FSMActions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMActions_BinaryOperator.attributes={HALL_FSMActions_BinaryOperator_operatorname}

# HALL_FSMActions_DomainPropertyGet class attributes and methods
HALL_FSMActions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_DomainPropertyGet.attributes={HALL_FSMActions_DomainPropertyGet_name}

# HALL_FSMActions_Let class attributes and methods
HALL_FSMActions_Let_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_Let.attributes={HALL_FSMActions_Let_name}

# HALL_FSMActions_MessageInvocation class attributes and methods
HALL_FSMActions_MessageInvocation_isTopDown: Property = Property(name="isTopDown", type=BooleanType)
HALL_FSMActions_MessageInvocation.attributes={HALL_FSMActions_MessageInvocation_isTopDown}

# HALL_Types_Type class attributes and methods
HALL_Types_Type_name: Property = Property(name="name", type=StringType)
HALL_Types_Type.attributes={HALL_Types_Type_name}

# HALL_Types_SimpleType class attributes and methods

# Set class attributes and methods

# HALL_Types_Set class attributes and methods

# SimpleType class attributes and methods

# HALL_Types_Boolean class attributes and methods

# HALL_Types_String class attributes and methods

# HALL_Types_Number class attributes and methods

# HALL_FSMActions_UnaryOperator class attributes and methods
HALL_FSMActions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMActions_UnaryOperator.attributes={HALL_FSMActions_UnaryOperator_operatorname}

# HALL_FSMActions_VarRef class attributes and methods

# FSMActions_Let class attributes and methods

# Relationships
geometryData1: BinaryAssociation = BinaryAssociation(
    name="geometryData1",
    ends={
        Property(name="GeometryData", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="geometryDataInv", type=GeometryData, multiplicity=Multiplicity(0, 1), is_composite=True)
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
        Property(name="componentSetInv", type=HALL_VisualObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="componentSetInv14", type=HALL_SystemComponent, multiplicity=Multiplicity(0, 9999))
    }
)
colorData0: BinaryAssociation = BinaryAssociation(
    name="colorData0",
    ends={
        Property(name="ColorData", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="colorDataInv", type=ColorData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visualObject25: BinaryAssociation = BinaryAssociation(
    name="visualObject25",
    ends={
        Property(name="VisualObject26", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="visualObjectInv", type=HALL_VisualObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskObject27: BinaryAssociation = BinaryAssociation(
    name="taskObject27",
    ends={
        Property(name="TaskObject", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="taskObjectInv", type=HALL_TaskObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userProfileInv28: BinaryAssociation = BinaryAssociation(
    name="userProfileInv28",
    ends={
        Property(name="Model29", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="userProfile", type=HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
componentSet31: BinaryAssociation = BinaryAssociation(
    name="componentSet31",
    ends={
        Property(name="UserProfile33", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv32", type=HALL_UserProfile, multiplicity=Multiplicity(0, 9999))
    }
)
componentSetInv35: BinaryAssociation = BinaryAssociation(
    name="componentSetInv35",
    ends={
        Property(name="UserProfile37", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet36", type=HALL_UserProfile, multiplicity=Multiplicity(0, 1))
    }
)
goal38: BinaryAssociation = BinaryAssociation(
    name="goal38",
    ends={
        Property(name="Goal", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="goalInv", type=HALL_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskObjectInv39: BinaryAssociation = BinaryAssociation(
    name="taskObjectInv39",
    ends={
        Property(name="UserProfile40", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="taskObject", type=HALL_UserProfile, multiplicity=Multiplicity(0, 1))
    }
)
componentSet42: BinaryAssociation = BinaryAssociation(
    name="componentSet42",
    ends={
        Property(name="TaskObject44", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv43", type=HALL_TaskObject, multiplicity=Multiplicity(0, 9999))
    }
)
componentSetInv46: BinaryAssociation = BinaryAssociation(
    name="componentSetInv46",
    ends={
        Property(name="TaskObject48", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet47", type=HALL_TaskObject, multiplicity=Multiplicity(0, 1))
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
typeDefinition24: BinaryAssociation = BinaryAssociation(
    name="typeDefinition24",
    ends={
        Property(name="Type", type=HALL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Model", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInvMessageDefinition57: BinaryAssociation = BinaryAssociation(
    name="dataInvMessageDefinition57",
    ends={
        Property(name="MessageDefinition58", type=HALL_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="data", type=MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
dataInvComponent59: BinaryAssociation = BinaryAssociation(
    name="dataInvComponent59",
    ends={
        Property(name="Component", type=HALL_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="data60", type=HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
ambianceColor61: BinaryAssociation = BinaryAssociation(
    name="ambianceColor61",
    ends={
        Property(name="RGBColor", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="ambianceColorInv", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
difuseColor62: BinaryAssociation = BinaryAssociation(
    name="difuseColor62",
    ends={
        Property(name="RGBColor63", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="difuseColorInv", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specularColor64: BinaryAssociation = BinaryAssociation(
    name="specularColor64",
    ends={
        Property(name="RGBColor65", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="specularColorInv", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColorInv66: BinaryAssociation = BinaryAssociation(
    name="foregroundColorInv66",
    ends={
        Property(name="ColorState", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="foregroundColor", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColorInv67: BinaryAssociation = BinaryAssociation(
    name="backgroundColorInv67",
    ends={
        Property(name="ColorState68", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="backgroundColor", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
ambianceColorInv69: BinaryAssociation = BinaryAssociation(
    name="ambianceColorInv69",
    ends={
        Property(name="Color", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="ambianceColor", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
difuseColorInv70: BinaryAssociation = BinaryAssociation(
    name="difuseColorInv70",
    ends={
        Property(name="Color71", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="difuseColor", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
specularColorInv72: BinaryAssociation = BinaryAssociation(
    name="specularColorInv72",
    ends={
        Property(name="Color73", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="specularColor", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
goalInv49: BinaryAssociation = BinaryAssociation(
    name="goalInv49",
    ends={
        Property(name="TaskObject50", type=HALL_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goal", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1))
    }
)
type51: BinaryAssociation = BinaryAssociation(
    name="type51",
    ends={
        Property(name="Type52", type=HALL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Parameter", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
parameterInv53: BinaryAssociation = BinaryAssociation(
    name="parameterInv53",
    ends={
        Property(name="MessageDefinition54", type=HALL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
type55: BinaryAssociation = BinaryAssociation(
    name="type55",
    ends={
        Property(name="Type56", type=HALL_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Data", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
normalColorsInv81: BinaryAssociation = BinaryAssociation(
    name="normalColorsInv81",
    ends={
        Property(name="ColorData82", type=HALL_Geometry_NormalColors, multiplicity=Multiplicity(1, 1)),
        Property(name="normalColors", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
selectedColorsInv83: BinaryAssociation = BinaryAssociation(
    name="selectedColorsInv83",
    ends={
        Property(name="ColorData84", type=HALL_Geometry_SelectedColors, multiplicity=Multiplicity(1, 1)),
        Property(name="selectedColors", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
disabledColorsInv85: BinaryAssociation = BinaryAssociation(
    name="disabledColorsInv85",
    ends={
        Property(name="ColorData86", type=HALL_Geometry_DisabledColors, multiplicity=Multiplicity(1, 1)),
        Property(name="disabledColors", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
selectedColors87: BinaryAssociation = BinaryAssociation(
    name="selectedColors87",
    ends={
        Property(name="SelectedColors", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="selectedColorsInv", type=SelectedColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
disabledColors88: BinaryAssociation = BinaryAssociation(
    name="disabledColors88",
    ends={
        Property(name="DisabledColors", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="disabledColorsInv", type=DisabledColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
normalColors89: BinaryAssociation = BinaryAssociation(
    name="normalColors89",
    ends={
        Property(name="NormalColors", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="normalColorsInv", type=NormalColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colorDataInv90: BinaryAssociation = BinaryAssociation(
    name="colorDataInv90",
    ends={
        Property(name="VisualObject91", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="colorData", type=Geometry_HALL_VisualObject, multiplicity=Multiplicity(0, 1))
    }
)
geometryDataInv92: BinaryAssociation = BinaryAssociation(
    name="geometryDataInv92",
    ends={
        Property(name="VisualObject93", type=HALL_Geometry_GeometryData, multiplicity=Multiplicity(1, 1)),
        Property(name="geometryData", type=Geometry_HALL_VisualObject, multiplicity=Multiplicity(0, 1))
    }
)
face94: BinaryAssociation = BinaryAssociation(
    name="face94",
    ends={
        Property(name="Face", type=HALL_Geometry_GeometryData3D, multiplicity=Multiplicity(1, 1)),
        Property(name="faceInv", type=Face, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
point2d95: BinaryAssociation = BinaryAssociation(
    name="point2d95",
    ends={
        Property(name="Point2D", type=HALL_Geometry_GeometryData2D, multiplicity=Multiplicity(1, 1)),
        Property(name="point2dInv", type=Point2D, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
foregroundColor74: BinaryAssociation = BinaryAssociation(
    name="foregroundColor74",
    ends={
        Property(name="Color75", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="foregroundColorInv", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor76: BinaryAssociation = BinaryAssociation(
    name="backgroundColor76",
    ends={
        Property(name="Color77", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="backgroundColorInv", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alphaTransparency78: BinaryAssociation = BinaryAssociation(
    name="alphaTransparency78",
    ends={
        Property(name="AlphaTransparency", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="alphaTransparencyInv", type=AlphaTransparency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alphaTransparencyInv79: BinaryAssociation = BinaryAssociation(
    name="alphaTransparencyInv79",
    ends={
        Property(name="ColorState80", type=HALL_Geometry_AlphaTransparency, multiplicity=Multiplicity(1, 1)),
        Property(name="alphaTransparency", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
point2dInv101: BinaryAssociation = BinaryAssociation(
    name="point2dInv101",
    ends={
        Property(name="GeometryData2D", type=HALL_Geometry_Point2D, multiplicity=Multiplicity(1, 1)),
        Property(name="point2d", type=GeometryData2D, multiplicity=Multiplicity(0, 1))
    }
)
transitionsInvMessageState102: BinaryAssociation = BinaryAssociation(
    name="transitionsInvMessageState102",
    ends={
        Property(name="MessageState", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=MessageState, multiplicity=Multiplicity(0, 1))
    }
)
stateRef103: BinaryAssociation = BinaryAssociation(
    name="stateRef103",
    ends={
        Property(name="MessageState104", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageTransition", type=MessageState, multiplicity=Multiplicity(1, 1))
    }
)
PreCondition105: BinaryAssociation = BinaryAssociation(
    name="PreCondition105",
    ends={
        Property(name="Conditions_PreConditionMessage", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageTransition106", type=Conditions_PreConditionMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PosCondition107: BinaryAssociation = BinaryAssociation(
    name="PosCondition107",
    ends={
        Property(name="Instructions_PosConditionMessage", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageTransition108", type=Instructions_PosConditionMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ActionMessage109: BinaryAssociation = BinaryAssociation(
    name="ActionMessage109",
    ends={
        Property(name="Actions_ActionMessage", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageTransition110", type=Actions_ActionMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageStateInv111: BinaryAssociation = BinaryAssociation(
    name="messageStateInv111",
    ends={
        Property(name="MessageHandler112", type=HALL_Messages_RegularMessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="messageState", type=MessageHandler, multiplicity=Multiplicity(0, 1))
    }
)
messageDefinitionInv113: BinaryAssociation = BinaryAssociation(
    name="messageDefinitionInv113",
    ends={
        Property(name="Model114", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition", type=Messages_HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
point3d96: BinaryAssociation = BinaryAssociation(
    name="point3d96",
    ends={
        Property(name="Point3D", type=HALL_Geometry_Face, multiplicity=Multiplicity(1, 1)),
        Property(name="point2dInv97", type=Point3D, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
faceInv98: BinaryAssociation = BinaryAssociation(
    name="faceInv98",
    ends={
        Property(name="GeometryData3D", type=HALL_Geometry_Face, multiplicity=Multiplicity(1, 1)),
        Property(name="face", type=GeometryData3D, multiplicity=Multiplicity(0, 1))
    }
)
point2dInv99: BinaryAssociation = BinaryAssociation(
    name="point2dInv99",
    ends={
        Property(name="Face100", type=HALL_Geometry_Point3D, multiplicity=Multiplicity(1, 1)),
        Property(name="point3d", type=Face, multiplicity=Multiplicity(0, 1))
    }
)
initialMessageState121: BinaryAssociation = BinaryAssociation(
    name="initialMessageState121",
    ends={
        Property(name="InitialMessageState", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="initialMessageStateInv", type=InitialMessageState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageHandlerSetInv122: BinaryAssociation = BinaryAssociation(
    name="messageHandlerSetInv122",
    ends={
        Property(name="Component123", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="messageHandlerSet", type=Messages_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
transitions124: BinaryAssociation = BinaryAssociation(
    name="transitions124",
    ends={
        Property(name="MessageTransition", type=HALL_Messages_MessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="transitionsInvMessageState", type=MessageTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialMessageStateInv125: BinaryAssociation = BinaryAssociation(
    name="initialMessageStateInv125",
    ends={
        Property(name="MessageHandler126", type=HALL_Messages_InitialMessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="initialMessageState", type=MessageHandler, multiplicity=Multiplicity(0, 1))
    }
)
expression127: BinaryAssociation = BinaryAssociation(
    name="expression127",
    ends={
        Property(name="Instructions_PosConditionMessageExpression", type=HALL_Instructions_PosConditionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_PosConditionMessage", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftexpression128: BinaryAssociation = BinaryAssociation(
    name="leftexpression128",
    ends={
        Property(name="Instructions_PosConditionMessageExpression129", type=HALL_Instructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_BinaryOperator", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression130: BinaryAssociation = BinaryAssociation(
    name="rightexpression130",
    ends={
        Property(name="Instructions_PosConditionMessageExpression132", type=HALL_Instructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_BinaryOperator131", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter115: BinaryAssociation = BinaryAssociation(
    name="parameter115",
    ends={
        Property(name="Parameter", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterInv", type=Messages_HALL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data116: BinaryAssociation = BinaryAssociation(
    name="data116",
    ends={
        Property(name="Data117", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInvMessageDefinition", type=Messages_HALL_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message118: BinaryAssociation = BinaryAssociation(
    name="message118",
    ends={
        Property(name="MessageDefinition119", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageHandler", type=MessageDefinition, multiplicity=Multiplicity(1, 1))
    }
)
messageState120: BinaryAssociation = BinaryAssociation(
    name="messageState120",
    ends={
        Property(name="RegularMessageState", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="messageStateInv", type=RegularMessageState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state137: BinaryAssociation = BinaryAssociation(
    name="state137",
    ends={
        Property(name="State", type=HALL_Instructions_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetState", type=State, multiplicity=Multiplicity(1, 1))
    }
)
value138: BinaryAssociation = BinaryAssociation(
    name="value138",
    ends={
        Property(name="Instructions_PosConditionMessageExpression139", type=HALL_Instructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetData", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference140: BinaryAssociation = BinaryAssociation(
    name="reference140",
    ends={
        Property(name="Instructions_HALL_Data142", type=HALL_Instructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetData141", type=Instructions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
value143: BinaryAssociation = BinaryAssociation(
    name="value143",
    ends={
        Property(name="Instructions_PosConditionMessageExpression144", type=HALL_Instructions_SetMessageData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetMessageData", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value145: BinaryAssociation = BinaryAssociation(
    name="value145",
    ends={
        Property(name="Instructions_PosConditionMessageExpression146", type=HALL_Instructions_SetMessageParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetMessageParameter", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_147: BinaryAssociation = BinaryAssociation(
    name="in_147",
    ends={
        Property(name="Instructions_PosConditionMessageExpression148", type=HALL_Instructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_Let", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization149: BinaryAssociation = BinaryAssociation(
    name="initialization149",
    ends={
        Property(name="Instructions_PosConditionMessageExpression151", type=HALL_Instructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_Let150", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type152: BinaryAssociation = BinaryAssociation(
    name="type152",
    ends={
        Property(name="Type154", type=HALL_Instructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_Let153", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
expression133: BinaryAssociation = BinaryAssociation(
    name="expression133",
    ends={
        Property(name="Instructions_PosConditionMessageExpression134", type=HALL_Instructions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_UnaryOperator", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference135: BinaryAssociation = BinaryAssociation(
    name="reference135",
    ends={
        Property(name="Instructions_HALL_Data", type=HALL_Instructions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_GetData", type=Instructions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
reference136: BinaryAssociation = BinaryAssociation(
    name="reference136",
    ends={
        Property(name="Instructions_HALL_Component", type=HALL_Instructions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_GetState", type=Instructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
valueof157: BinaryAssociation = BinaryAssociation(
    name="valueof157",
    ends={
        Property(name="Instructions_Let", type=HALL_Instructions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_VarRef", type=Instructions_Let, multiplicity=Multiplicity(1, 1))
    }
)
expression158: BinaryAssociation = BinaryAssociation(
    name="expression158",
    ends={
        Property(name="Conditions_PreConditionMessageExpression", type=HALL_Conditions_PreConditionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_PreConditionMessage", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference159: BinaryAssociation = BinaryAssociation(
    name="reference159",
    ends={
        Property(name="Conditions_HALL_Component", type=HALL_Conditions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_GetState", type=Conditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference160: BinaryAssociation = BinaryAssociation(
    name="reference160",
    ends={
        Property(name="Conditions_HALL_Data", type=HALL_Conditions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_GetData", type=Conditions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
type161: BinaryAssociation = BinaryAssociation(
    name="type161",
    ends={
        Property(name="Type162", type=HALL_Conditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_Let", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
value155: BinaryAssociation = BinaryAssociation(
    name="value155",
    ends={
        Property(name="Instructions_PosConditionMessageExpression156", type=HALL_Instructions_SetTopDown, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetTopDown", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftexpression171: BinaryAssociation = BinaryAssociation(
    name="leftexpression171",
    ends={
        Property(name="Conditions_PreConditionMessageExpression172", type=HALL_Conditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_BinaryOperator", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression173: BinaryAssociation = BinaryAssociation(
    name="rightexpression173",
    ends={
        Property(name="Conditions_PreConditionMessageExpression175", type=HALL_Conditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_BinaryOperator174", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueof176: BinaryAssociation = BinaryAssociation(
    name="valueof176",
    ends={
        Property(name="Conditions_Let", type=HALL_Conditions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_VarRef", type=Conditions_Let, multiplicity=Multiplicity(1, 1))
    }
)
expression177: BinaryAssociation = BinaryAssociation(
    name="expression177",
    ends={
        Property(name="Actions_ActionMessageExpression", type=HALL_Actions_ActionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_ActionMessage", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueof178: BinaryAssociation = BinaryAssociation(
    name="valueof178",
    ends={
        Property(name="Actions_Let", type=HALL_Actions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_VarRef", type=Actions_Let, multiplicity=Multiplicity(1, 1))
    }
)
leftexpression179: BinaryAssociation = BinaryAssociation(
    name="leftexpression179",
    ends={
        Property(name="Actions_ActionMessageExpression180", type=HALL_Actions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_BinaryOperator", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression181: BinaryAssociation = BinaryAssociation(
    name="rightexpression181",
    ends={
        Property(name="Actions_ActionMessageExpression183", type=HALL_Actions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_BinaryOperator182", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_163: BinaryAssociation = BinaryAssociation(
    name="in_163",
    ends={
        Property(name="Conditions_PreConditionMessageExpression165", type=HALL_Conditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_Let164", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization166: BinaryAssociation = BinaryAssociation(
    name="initialization166",
    ends={
        Property(name="Conditions_PreConditionMessageExpression168", type=HALL_Conditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_Let167", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression169: BinaryAssociation = BinaryAssociation(
    name="expression169",
    ends={
        Property(name="Conditions_PreConditionMessageExpression170", type=HALL_Conditions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_UnaryOperator", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message192: BinaryAssociation = BinaryAssociation(
    name="message192",
    ends={
        Property(name="MessageDefinition193", type=HALL_Actions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_MessageInvocation", type=MessageDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualset194: BinaryAssociation = BinaryAssociation(
    name="actualset194",
    ends={
        Property(name="Actions_ActionMessageExpression196", type=HALL_Actions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_MessageInvocation195", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression197: BinaryAssociation = BinaryAssociation(
    name="expression197",
    ends={
        Property(name="Actions_ActionMessageExpression198", type=HALL_Actions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_UnaryOperator", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference199: BinaryAssociation = BinaryAssociation(
    name="reference199",
    ends={
        Property(name="Actions_HALL_Component", type=HALL_Actions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_GetData", type=Actions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
value200: BinaryAssociation = BinaryAssociation(
    name="value200",
    ends={
        Property(name="Actions_ActionMessageExpression201", type=HALL_Actions_DomainPropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_DomainPropertySet", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value202: BinaryAssociation = BinaryAssociation(
    name="value202",
    ends={
        Property(name="Actions_ActionMessageExpression203", type=HALL_Actions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Enable", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in_184: BinaryAssociation = BinaryAssociation(
    name="in_184",
    ends={
        Property(name="Actions_ActionMessageExpression185", type=HALL_Actions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Let", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization186: BinaryAssociation = BinaryAssociation(
    name="initialization186",
    ends={
        Property(name="Actions_ActionMessageExpression188", type=HALL_Actions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Let187", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type189: BinaryAssociation = BinaryAssociation(
    name="type189",
    ends={
        Property(name="Type191", type=HALL_Actions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Let190", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
source213: BinaryAssociation = BinaryAssociation(
    name="source213",
    ends={
        Property(name="State215", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions214", type=State, multiplicity=Multiplicity(1, 1))
    }
)
stateRef216: BinaryAssociation = BinaryAssociation(
    name="stateRef216",
    ends={
        Property(name="State217", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition", type=State, multiplicity=Multiplicity(1, 1))
    }
)
PreCondition218: BinaryAssociation = BinaryAssociation(
    name="PreCondition218",
    ends={
        Property(name="FSMConditions_PreCondition", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition219", type=FSMConditions_PreCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PosCondition220: BinaryAssociation = BinaryAssociation(
    name="PosCondition220",
    ends={
        Property(name="FSMInstructions_PosCondition", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition221", type=FSMInstructions_PosCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Action222: BinaryAssociation = BinaryAssociation(
    name="Action222",
    ends={
        Property(name="FSMActions_Action", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition223", type=FSMActions_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Trigger224: BinaryAssociation = BinaryAssociation(
    name="Trigger224",
    ends={
        Property(name="Trigger_Trigger", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition225", type=Trigger_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions226: BinaryAssociation = BinaryAssociation(
    name="transitions226",
    ends={
        Property(name="Transition", type=HALL_FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference204: BinaryAssociation = BinaryAssociation(
    name="reference204",
    ends={
        Property(name="MessageDefinition206", type=HALL_Actions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Enable205", type=MessageDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FSMInv207: BinaryAssociation = BinaryAssociation(
    name="FSMInv207",
    ends={
        Property(name="Component209", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM208", type=FSM_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
initialState210: BinaryAssociation = BinaryAssociation(
    name="initialState210",
    ends={
        Property(name="InitialState", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_FSM", type=InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
state211: BinaryAssociation = BinaryAssociation(
    name="state211",
    ends={
        Property(name="RegularState", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_FSM212", type=RegularState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message230: BinaryAssociation = BinaryAssociation(
    name="message230",
    ends={
        Property(name="MessageDefinition231", type=HALL_Trigger_MessageNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Trigger_MessageNotification", type=MessageDefinition, multiplicity=Multiplicity(1, 1))
    }
)
expression232: BinaryAssociation = BinaryAssociation(
    name="expression232",
    ends={
        Property(name="FSMInstructions_PosConditionExpression", type=HALL_FSMInstructions_PosCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_PosCondition", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftexpression233: BinaryAssociation = BinaryAssociation(
    name="leftexpression233",
    ends={
        Property(name="FSMInstructions_PosConditionExpression234", type=HALL_FSMInstructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_BinaryOperator", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression235: BinaryAssociation = BinaryAssociation(
    name="rightexpression235",
    ends={
        Property(name="FSMInstructions_PosConditionExpression237", type=HALL_FSMInstructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_BinaryOperator236", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression238: BinaryAssociation = BinaryAssociation(
    name="expression238",
    ends={
        Property(name="FSMInstructions_PosConditionExpression239", type=HALL_FSMInstructions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_UnaryOperator", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference240: BinaryAssociation = BinaryAssociation(
    name="reference240",
    ends={
        Property(name="FSMInstructions_HALL_Component", type=HALL_FSMInstructions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_GetData", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
fsm227: BinaryAssociation = BinaryAssociation(
    name="fsm227",
    ends={
        Property(name="FSM228", type=HALL_FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_State", type=FSM, multiplicity=Multiplicity(0, 1))
    }
)
expression229: BinaryAssociation = BinaryAssociation(
    name="expression229",
    ends={
        Property(name="Trigger_TriggerExpression", type=HALL_Trigger_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Trigger_Trigger", type=Trigger_TriggerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference250: BinaryAssociation = BinaryAssociation(
    name="reference250",
    ends={
        Property(name="FSMInstructions_HALL_Data", type=HALL_FSMInstructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetData251", type=FSMInstructions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
in_252: BinaryAssociation = BinaryAssociation(
    name="in_252",
    ends={
        Property(name="FSMInstructions_PosConditionExpression253", type=HALL_FSMInstructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_Let", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization254: BinaryAssociation = BinaryAssociation(
    name="initialization254",
    ends={
        Property(name="FSMInstructions_PosConditionExpression256", type=HALL_FSMInstructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_Let255", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type257: BinaryAssociation = BinaryAssociation(
    name="type257",
    ends={
        Property(name="Type259", type=HALL_FSMInstructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_Let258", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
valueof260: BinaryAssociation = BinaryAssociation(
    name="valueof260",
    ends={
        Property(name="FSMInstructions_Let", type=HALL_FSMInstructions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_VarRef", type=FSMInstructions_Let, multiplicity=Multiplicity(1, 1))
    }
)
expression261: BinaryAssociation = BinaryAssociation(
    name="expression261",
    ends={
        Property(name="FSMConditions_PreConditionExpression", type=HALL_FSMConditions_PreCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_PreCondition", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference241: BinaryAssociation = BinaryAssociation(
    name="reference241",
    ends={
        Property(name="FSMInstructions_HALL_Component242", type=HALL_FSMInstructions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_GetState", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference243: BinaryAssociation = BinaryAssociation(
    name="reference243",
    ends={
        Property(name="FSMInstructions_HALL_Component244", type=HALL_FSMInstructions_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetState", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
state245: BinaryAssociation = BinaryAssociation(
    name="state245",
    ends={
        Property(name="State247", type=HALL_FSMInstructions_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetState246", type=State, multiplicity=Multiplicity(1, 1))
    }
)
value248: BinaryAssociation = BinaryAssociation(
    name="value248",
    ends={
        Property(name="FSMInstructions_PosConditionExpression249", type=HALL_FSMInstructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetData", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference269: BinaryAssociation = BinaryAssociation(
    name="reference269",
    ends={
        Property(name="FSMConditions_HALL_Component", type=HALL_FSMConditions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_GetState", type=FSMConditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference270: BinaryAssociation = BinaryAssociation(
    name="reference270",
    ends={
        Property(name="FSMConditions_HALL_Data", type=HALL_FSMConditions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_GetData", type=FSMConditions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
initialization271: BinaryAssociation = BinaryAssociation(
    name="initialization271",
    ends={
        Property(name="FSMConditions_PreConditionExpression272", type=HALL_FSMConditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_Let", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_273: BinaryAssociation = BinaryAssociation(
    name="in_273",
    ends={
        Property(name="FSMConditions_PreConditionExpression275", type=HALL_FSMConditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_Let274", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type276: BinaryAssociation = BinaryAssociation(
    name="type276",
    ends={
        Property(name="Type278", type=HALL_FSMConditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_Let277", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
valueof279: BinaryAssociation = BinaryAssociation(
    name="valueof279",
    ends={
        Property(name="FSMConditions_Let", type=HALL_FSMConditions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_VarRef", type=FSMConditions_Let, multiplicity=Multiplicity(1, 1))
    }
)
expression280: BinaryAssociation = BinaryAssociation(
    name="expression280",
    ends={
        Property(name="FSMActions_ActionExpression", type=HALL_FSMActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Action", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftexpression262: BinaryAssociation = BinaryAssociation(
    name="leftexpression262",
    ends={
        Property(name="FSMConditions_PreConditionExpression263", type=HALL_FSMConditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_BinaryOperator", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression264: BinaryAssociation = BinaryAssociation(
    name="rightexpression264",
    ends={
        Property(name="FSMConditions_PreConditionExpression266", type=HALL_FSMConditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_BinaryOperator265", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression267: BinaryAssociation = BinaryAssociation(
    name="expression267",
    ends={
        Property(name="FSMConditions_PreConditionExpression268", type=HALL_FSMConditions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_UnaryOperator", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message289: BinaryAssociation = BinaryAssociation(
    name="message289",
    ends={
        Property(name="MessageDefinition290", type=HALL_FSMActions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_MessageInvocation", type=MessageDefinition, multiplicity=Multiplicity(1, 1))
    }
)
actualset291: BinaryAssociation = BinaryAssociation(
    name="actualset291",
    ends={
        Property(name="FSMActions_ActionExpression293", type=HALL_FSMActions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_MessageInvocation292", type=FSMActions_ActionExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message294: BinaryAssociation = BinaryAssociation(
    name="message294",
    ends={
        Property(name="MessageDefinition295", type=HALL_FSMActions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Enable", type=MessageDefinition, multiplicity=Multiplicity(1, 1))
    }
)
value296: BinaryAssociation = BinaryAssociation(
    name="value296",
    ends={
        Property(name="FSMActions_ActionExpression298", type=HALL_FSMActions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Enable297", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value299: BinaryAssociation = BinaryAssociation(
    name="value299",
    ends={
        Property(name="FSMActions_ActionExpression300", type=HALL_FSMActions_DomainPropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_DomainPropertySet", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference301: BinaryAssociation = BinaryAssociation(
    name="reference301",
    ends={
        Property(name="FSMActions_HALL_Data", type=HALL_FSMActions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_GetData", type=FSMActions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
leftoperator302: BinaryAssociation = BinaryAssociation(
    name="leftoperator302",
    ends={
        Property(name="FSMActions_ActionExpression303", type=HALL_FSMActions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_BinaryOperator", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression304: BinaryAssociation = BinaryAssociation(
    name="rightexpression304",
    ends={
        Property(name="FSMActions_ActionExpression306", type=HALL_FSMActions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_BinaryOperator305", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_281: BinaryAssociation = BinaryAssociation(
    name="in_281",
    ends={
        Property(name="FSMActions_ActionExpression282", type=HALL_FSMActions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Let", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization283: BinaryAssociation = BinaryAssociation(
    name="initialization283",
    ends={
        Property(name="FSMActions_ActionExpression285", type=HALL_FSMActions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Let284", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type286: BinaryAssociation = BinaryAssociation(
    name="type286",
    ends={
        Property(name="Type288", type=HALL_FSMActions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Let287", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
elementsTypeInv310: BinaryAssociation = BinaryAssociation(
    name="elementsTypeInv310",
    ends={
        Property(name="Set", type=HALL_Types_SimpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementsType", type=Set, multiplicity=Multiplicity(0, 1))
    }
)
elementsType311: BinaryAssociation = BinaryAssociation(
    name="elementsType311",
    ends={
        Property(name="SimpleType", type=HALL_Types_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="elementsTypeInv", type=SimpleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression307: BinaryAssociation = BinaryAssociation(
    name="expression307",
    ends={
        Property(name="FSMActions_ActionExpression308", type=HALL_FSMActions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_UnaryOperator", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueof309: BinaryAssociation = BinaryAssociation(
    name="valueof309",
    ends={
        Property(name="FSMActions_Let", type=HALL_FSMActions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_VarRef", type=FSMActions_Let, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_HALL_SystemComponent_Component = Generalization(general=Component, specific=HALL_SystemComponent)
gen_HALL_VisualObject_Component = Generalization(general=Component, specific=HALL_VisualObject)
gen_HALL_UserProfile_Component = Generalization(general=Component, specific=HALL_UserProfile)
gen_HALL_TaskObject_Component = Generalization(general=Component, specific=HALL_TaskObject)
gen_HALL_Geometry_SelectedColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_SelectedColors)
gen_HALL_Geometry_DisabledColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_DisabledColors)
gen_HALL_Geometry_GeometryData3D_GeometryData = Generalization(general=GeometryData, specific=HALL_Geometry_GeometryData3D)
gen_HALL_Geometry_GeometryData2D_GeometryData = Generalization(general=GeometryData, specific=HALL_Geometry_GeometryData2D)
gen_HALL_Geometry_NormalColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_NormalColors)
gen_HALL_Geometry_Point2D_Point = Generalization(general=Point, specific=HALL_Geometry_Point2D)
gen_HALL_Messages_RegularMessageState_MessageState = Generalization(general=MessageState, specific=HALL_Messages_RegularMessageState)
gen_HALL_Geometry_Point3D_Point = Generalization(general=Point, specific=HALL_Geometry_Point3D)
gen_HALL_Messages_InitialMessageState_MessageState = Generalization(general=MessageState, specific=HALL_Messages_InitialMessageState)
gen_HALL_Instructions_Literal_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_Literal)
gen_HALL_Instructions_BinaryOperator_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_BinaryOperator)
gen_HALL_Instructions_SetState_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_SetState)
gen_HALL_Instructions_SetData_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_SetData)
gen_HALL_Instructions_SetMessageData_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_SetMessageData)
gen_HALL_Instructions_SetMessageParameter_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_SetMessageParameter)
gen_HALL_Instructions_Let_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_Let)
gen_HALL_Instructions_DomainPropertyGet_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_DomainPropertyGet)
gen_HALL_Instructions_UnaryOperator_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_UnaryOperator)
gen_HALL_Instructions_GetData_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_GetData)
gen_HALL_Instructions_GetState_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_GetState)
gen_HALL_Conditions_Literal_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_Literal)
gen_HALL_Conditions_GetMessageData_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_GetMessageData)
gen_HALL_Conditions_GetMessageParameter_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_GetMessageParameter)
gen_HALL_Conditions_DomainPropertyGet_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_DomainPropertyGet)
gen_HALL_Conditions_GetState_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_GetState)
gen_HALL_Conditions_GetData_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_GetData)
gen_HALL_Conditions_Let_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_Let)
gen_HALL_Instructions_GetMessageData_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_GetMessageData)
gen_HALL_Instructions_GetMessageParameter_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_GetMessageParameter)
gen_HALL_Instructions_SetTopDown_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_SetTopDown)
gen_HALL_Instructions_VarRef_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_VarRef)
gen_HALL_Conditions_VarRef_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_VarRef)
gen_HALL_Actions_VarRef_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_VarRef)
gen_HALL_Actions_Literal_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_Literal)
gen_HALL_Actions_BinaryOperator_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_BinaryOperator)
gen_HALL_Actions_Let_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_Let)
gen_HALL_Conditions_UnaryOperator_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_UnaryOperator)
gen_HALL_Conditions_BinaryOperator_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_BinaryOperator)
gen_HALL_Actions_MessageInvocation_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_MessageInvocation)
gen_HALL_Actions_UnaryOperator_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_UnaryOperator)
gen_HALL_Actions_GetData_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_GetData)
gen_HALL_Actions_DomainPropertySet_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_DomainPropertySet)
gen_HALL_Actions_Enable_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_Enable)
gen_HALL_Actions_DomainPropertyGet_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_DomainPropertyGet)
gen_HALL_Actions_GetMessageData_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_GetMessageData)
gen_HALL_Actions_GetMessageParameter_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_GetMessageParameter)
gen_HALL_FSM_InitialState_State = Generalization(general=State, specific=HALL_FSM_InitialState)
gen_HALL_FSM_RegularState_State = Generalization(general=State, specific=HALL_FSM_RegularState)
gen_HALL_Trigger_DomainEventFired_TriggerExpression = Generalization(general=TriggerExpression, specific=HALL_Trigger_DomainEventFired)
gen_HALL_FSMInstructions_Literal_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_Literal)
gen_HALL_FSMInstructions_BinaryOperator_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_BinaryOperator)
gen_HALL_FSMInstructions_UnaryOperator_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_UnaryOperator)
gen_HALL_FSMInstructions_GetData_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_GetData)
gen_HALL_Trigger_MessageNotification_TriggerExpression = Generalization(general=TriggerExpression, specific=HALL_Trigger_MessageNotification)
gen_HALL_FSMInstructions_Let_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_Let)
gen_HALL_FSMInstructions_DomainPropertyGet_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_DomainPropertyGet)
gen_HALL_FSMInstructions_VarRef_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_VarRef)
gen_HALL_FSMConditions_Literal_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_Literal)
gen_HALL_FSMConditions_BinaryOperator_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_BinaryOperator)
gen_HALL_FSMInstructions_GetState_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_GetState)
gen_HALL_FSMInstructions_SetState_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_SetState)
gen_HALL_FSMInstructions_SetData_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_SetData)
gen_HALL_FSMConditions_GetData_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_GetData)
gen_HALL_FSMConditions_DomainPropertyGet_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_DomainPropertyGet)
gen_HALL_FSMConditions_Let_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_Let)
gen_HALL_FSMConditions_VarRef_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_VarRef)
gen_HALL_FSMActions_Literal_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_Literal)
gen_HALL_FSMConditions_UnaryOperator_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_UnaryOperator)
gen_HALL_FSMConditions_GetState_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_GetState)
gen_HALL_FSMActions_Enable_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_FSMActions_Enable)
gen_HALL_FSMActions_DomainPropertySet_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_DomainPropertySet)
gen_HALL_FSMActions_GetData_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_GetData)
gen_HALL_FSMActions_BinaryOperator_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_BinaryOperator)
gen_HALL_FSMActions_DomainPropertyGet_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_DomainPropertyGet)
gen_HALL_FSMActions_Let_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_Let)
gen_HALL_FSMActions_MessageInvocation_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_MessageInvocation)
gen_HALL_Types_SimpleType_Type = Generalization(general=Type, specific=HALL_Types_SimpleType)
gen_HALL_Types_Set_Type = Generalization(general=Type, specific=HALL_Types_Set)
gen_HALL_Types_Boolean_SimpleType = Generalization(general=SimpleType, specific=HALL_Types_Boolean)
gen_HALL_Types_String_SimpleType = Generalization(general=SimpleType, specific=HALL_Types_String)
gen_HALL_Types_Number_SimpleType = Generalization(general=SimpleType, specific=HALL_Types_Number)
gen_HALL_FSMActions_UnaryOperator_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_UnaryOperator)
gen_HALL_FSMActions_VarRef_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_VarRef)

# Domain Model
domain_model = DomainModel(
    name="HALL",
    types={GeometryData, HALL_UserProfile, HALL_Component, HALL_Data, FSM, MessageHandler, HALL_SystemComponent, HALL_Model, HALL_VisualObject, Component, ColorData, HALL_TaskObject, HALL_Goal, MessageDefinition, Type, HALL_Geometry_Color, RGBColor, ColorState, HALL_Geometry_RGBColor, Color, HALL_Geometry_ColorState, HALL_Parameter, HALL_Geometry_SelectedColors, HALL_Geometry_DisabledColors, HALL_Geometry_ColorData, SelectedColors, DisabledColors, NormalColors, Geometry_HALL_VisualObject, HALL_Geometry_GeometryData, HALL_Geometry_GeometryData3D, Face, HALL_Geometry_GeometryData2D, Point2D, AlphaTransparency, HALL_Geometry_AlphaTransparency, HALL_Geometry_NormalColors, HALL_Geometry_Point2D, GeometryData2D, HALL_Geometry_Point, HALL_Messages_MessageTransition, MessageState, Conditions_PreConditionMessage, Instructions_PosConditionMessage, Actions_ActionMessage, HALL_Messages_RegularMessageState, HALL_Messages_MessageDefinition, Messages_HALL_Model, Messages_HALL_Parameter, HALL_Geometry_Face, Point3D, GeometryData3D, HALL_Geometry_Point3D, Point, InitialMessageState, Messages_HALL_Component, HALL_Messages_MessageState, MessageTransition, HALL_Messages_InitialMessageState, HALL_Instructions_PosConditionMessage, Instructions_PosConditionMessageExpression, HALL_Instructions_PosConditionMessageExpression, HALL_Instructions_Literal, PosConditionMessageExpression, HALL_Instructions_BinaryOperator, Messages_HALL_Data, HALL_Messages_MessageHandler, RegularMessageState, HALL_Instructions_SetState, State, HALL_Instructions_SetData, HALL_Instructions_SetMessageData, HALL_Instructions_SetMessageParameter, HALL_Instructions_Let, HALL_Instructions_DomainPropertyGet, HALL_Instructions_UnaryOperator, HALL_Instructions_GetData, Instructions_HALL_Data, HALL_Instructions_GetState, Instructions_HALL_Component, Instructions_Let, HALL_Conditions_PreConditionMessage, Conditions_PreConditionMessageExpression, HALL_Conditions_PreConditionMessageExpression, HALL_Conditions_Literal, PreConditionMessageExpression, HALL_Conditions_GetMessageData, HALL_Conditions_GetMessageParameter, HALL_Conditions_DomainPropertyGet, HALL_Conditions_GetState, Conditions_HALL_Component, HALL_Conditions_GetData, Conditions_HALL_Data, HALL_Conditions_Let, HALL_Instructions_GetMessageData, HALL_Instructions_GetMessageParameter, HALL_Instructions_SetTopDown, HALL_Instructions_VarRef, HALL_Conditions_VarRef, Conditions_Let, HALL_Actions_ActionMessage, Actions_ActionMessageExpression, HALL_Actions_ActionMessageExpression, HALL_Actions_VarRef, ActionMessageExpression, Actions_Let, HALL_Actions_Literal, HALL_Actions_BinaryOperator, HALL_Actions_Let, HALL_Conditions_UnaryOperator, HALL_Conditions_BinaryOperator, HALL_Actions_MessageInvocation, HALL_Actions_UnaryOperator, HALL_Actions_GetData, Actions_HALL_Component, HALL_Actions_DomainPropertySet, HALL_Actions_Enable, HALL_Actions_DomainPropertyGet, HALL_Actions_GetMessageData, HALL_Actions_GetMessageParameter, HALL_FSM_InitialState, HALL_FSM_Transition, FSMConditions_PreCondition, FSMInstructions_PosCondition, FSMActions_Action, Trigger_Trigger, HALL_FSM_State, Transition, HALL_FSM_FSM, FSM_HALL_Component, InitialState, RegularState, HALL_FSM_RegularState, HALL_Trigger_DomainEventFired, HALL_FSMInstructions_PosCondition, FSMInstructions_PosConditionExpression, HALL_FSMInstructions_PosConditionExpression, HALL_FSMInstructions_Literal, PosConditionExpression, HALL_FSMInstructions_BinaryOperator, HALL_FSMInstructions_UnaryOperator, HALL_FSMInstructions_GetData, FSMInstructions_HALL_Component, HALL_Trigger_Trigger, Trigger_TriggerExpression, HALL_Trigger_TriggerExpression, HALL_Trigger_MessageNotification, TriggerExpression, FSMInstructions_HALL_Data, HALL_FSMInstructions_Let, HALL_FSMInstructions_DomainPropertyGet, HALL_FSMInstructions_VarRef, FSMInstructions_Let, HALL_FSMConditions_PreCondition, FSMConditions_PreConditionExpression, HALL_FSMConditions_PreConditionExpression, HALL_FSMConditions_Literal, PreConditionExpression, HALL_FSMConditions_BinaryOperator, HALL_FSMInstructions_GetState, HALL_FSMInstructions_SetState, HALL_FSMInstructions_SetData, HALL_FSMConditions_GetData, FSMConditions_HALL_Data, HALL_FSMConditions_DomainPropertyGet, HALL_FSMConditions_Let, HALL_FSMConditions_VarRef, FSMConditions_Let, HALL_FSMActions_Action, FSMActions_ActionExpression, HALL_FSMActions_ActionExpression, HALL_FSMActions_Literal, ActionExpression, HALL_FSMConditions_UnaryOperator, HALL_FSMConditions_GetState, FSMConditions_HALL_Component, HALL_FSMActions_Enable, HALL_FSMActions_DomainPropertySet, HALL_FSMActions_GetData, FSMActions_HALL_Data, HALL_FSMActions_BinaryOperator, HALL_FSMActions_DomainPropertyGet, HALL_FSMActions_Let, HALL_FSMActions_MessageInvocation, HALL_Types_Type, HALL_Types_SimpleType, Set, HALL_Types_Set, SimpleType, HALL_Types_Boolean, HALL_Types_String, HALL_Types_Number, HALL_FSMActions_UnaryOperator, HALL_FSMActions_VarRef, FSMActions_Let},
    associations={geometryData1, visualObjectInv2, componentSet4, componentSetInv6, data8, FSM9, messageHandlerSet10, systemComponentInv11, componentSet13, colorData0, visualObject25, taskObject27, userProfileInv28, componentSet31, componentSetInv35, goal38, taskObjectInv39, componentSet42, componentSetInv46, componentSetInv16, userProfile19, systemComponent21, messageDefinition23, typeDefinition24, dataInvMessageDefinition57, dataInvComponent59, ambianceColor61, difuseColor62, specularColor64, foregroundColorInv66, backgroundColorInv67, ambianceColorInv69, difuseColorInv70, specularColorInv72, goalInv49, type51, parameterInv53, type55, normalColorsInv81, selectedColorsInv83, disabledColorsInv85, selectedColors87, disabledColors88, normalColors89, colorDataInv90, geometryDataInv92, face94, point2d95, foregroundColor74, backgroundColor76, alphaTransparency78, alphaTransparencyInv79, point2dInv101, transitionsInvMessageState102, stateRef103, PreCondition105, PosCondition107, ActionMessage109, messageStateInv111, messageDefinitionInv113, point3d96, faceInv98, point2dInv99, initialMessageState121, messageHandlerSetInv122, transitions124, initialMessageStateInv125, expression127, leftexpression128, rightexpression130, parameter115, data116, message118, messageState120, state137, value138, reference140, value143, value145, in_147, initialization149, type152, expression133, reference135, reference136, valueof157, expression158, reference159, reference160, type161, value155, leftexpression171, rightexpression173, valueof176, expression177, valueof178, leftexpression179, rightexpression181, in_163, initialization166, expression169, message192, actualset194, expression197, reference199, value200, value202, in_184, initialization186, type189, source213, stateRef216, PreCondition218, PosCondition220, Action222, Trigger224, transitions226, reference204, FSMInv207, initialState210, state211, message230, expression232, leftexpression233, rightexpression235, expression238, reference240, fsm227, expression229, reference250, in_252, initialization254, type257, valueof260, expression261, reference241, reference243, state245, value248, reference269, reference270, initialization271, in_273, type276, valueof279, expression280, leftexpression262, rightexpression264, expression267, message289, actualset291, message294, value296, value299, reference301, leftoperator302, rightexpression304, in_281, initialization283, type286, elementsTypeInv310, elementsType311, expression307, valueof309},
    generalizations={gen_HALL_SystemComponent_Component, gen_HALL_VisualObject_Component, gen_HALL_UserProfile_Component, gen_HALL_TaskObject_Component, gen_HALL_Geometry_SelectedColors_ColorState, gen_HALL_Geometry_DisabledColors_ColorState, gen_HALL_Geometry_GeometryData3D_GeometryData, gen_HALL_Geometry_GeometryData2D_GeometryData, gen_HALL_Geometry_NormalColors_ColorState, gen_HALL_Geometry_Point2D_Point, gen_HALL_Messages_RegularMessageState_MessageState, gen_HALL_Geometry_Point3D_Point, gen_HALL_Messages_InitialMessageState_MessageState, gen_HALL_Instructions_Literal_PosConditionMessageExpression, gen_HALL_Instructions_BinaryOperator_PosConditionMessageExpression, gen_HALL_Instructions_SetState_PosConditionMessageExpression, gen_HALL_Instructions_SetData_PosConditionMessageExpression, gen_HALL_Instructions_SetMessageData_PosConditionMessageExpression, gen_HALL_Instructions_SetMessageParameter_PosConditionMessageExpression, gen_HALL_Instructions_Let_PosConditionMessageExpression, gen_HALL_Instructions_DomainPropertyGet_PosConditionMessageExpression, gen_HALL_Instructions_UnaryOperator_PosConditionMessageExpression, gen_HALL_Instructions_GetData_PosConditionMessageExpression, gen_HALL_Instructions_GetState_PosConditionMessageExpression, gen_HALL_Conditions_Literal_PreConditionMessageExpression, gen_HALL_Conditions_GetMessageData_PreConditionMessageExpression, gen_HALL_Conditions_GetMessageParameter_PreConditionMessageExpression, gen_HALL_Conditions_DomainPropertyGet_PreConditionMessageExpression, gen_HALL_Conditions_GetState_PreConditionMessageExpression, gen_HALL_Conditions_GetData_PreConditionMessageExpression, gen_HALL_Conditions_Let_PreConditionMessageExpression, gen_HALL_Instructions_GetMessageData_PosConditionMessageExpression, gen_HALL_Instructions_GetMessageParameter_PosConditionMessageExpression, gen_HALL_Instructions_SetTopDown_PosConditionMessageExpression, gen_HALL_Instructions_VarRef_PosConditionMessageExpression, gen_HALL_Conditions_VarRef_PreConditionMessageExpression, gen_HALL_Actions_VarRef_ActionMessageExpression, gen_HALL_Actions_Literal_ActionMessageExpression, gen_HALL_Actions_BinaryOperator_ActionMessageExpression, gen_HALL_Actions_Let_ActionMessageExpression, gen_HALL_Conditions_UnaryOperator_PreConditionMessageExpression, gen_HALL_Conditions_BinaryOperator_PreConditionMessageExpression, gen_HALL_Actions_MessageInvocation_ActionMessageExpression, gen_HALL_Actions_UnaryOperator_ActionMessageExpression, gen_HALL_Actions_GetData_ActionMessageExpression, gen_HALL_Actions_DomainPropertySet_ActionMessageExpression, gen_HALL_Actions_Enable_ActionMessageExpression, gen_HALL_Actions_DomainPropertyGet_ActionMessageExpression, gen_HALL_Actions_GetMessageData_ActionMessageExpression, gen_HALL_Actions_GetMessageParameter_ActionMessageExpression, gen_HALL_FSM_InitialState_State, gen_HALL_FSM_RegularState_State, gen_HALL_Trigger_DomainEventFired_TriggerExpression, gen_HALL_FSMInstructions_Literal_PosConditionExpression, gen_HALL_FSMInstructions_BinaryOperator_PosConditionExpression, gen_HALL_FSMInstructions_UnaryOperator_PosConditionExpression, gen_HALL_FSMInstructions_GetData_PosConditionExpression, gen_HALL_Trigger_MessageNotification_TriggerExpression, gen_HALL_FSMInstructions_Let_PosConditionExpression, gen_HALL_FSMInstructions_DomainPropertyGet_PosConditionExpression, gen_HALL_FSMInstructions_VarRef_PosConditionExpression, gen_HALL_FSMConditions_Literal_PreConditionExpression, gen_HALL_FSMConditions_BinaryOperator_PreConditionExpression, gen_HALL_FSMInstructions_GetState_PosConditionExpression, gen_HALL_FSMInstructions_SetState_PosConditionExpression, gen_HALL_FSMInstructions_SetData_PosConditionExpression, gen_HALL_FSMConditions_GetData_PreConditionExpression, gen_HALL_FSMConditions_DomainPropertyGet_PreConditionExpression, gen_HALL_FSMConditions_Let_PreConditionExpression, gen_HALL_FSMConditions_VarRef_PreConditionExpression, gen_HALL_FSMActions_Literal_ActionExpression, gen_HALL_FSMConditions_UnaryOperator_PreConditionExpression, gen_HALL_FSMConditions_GetState_PreConditionExpression, gen_HALL_FSMActions_Enable_ActionMessageExpression, gen_HALL_FSMActions_DomainPropertySet_ActionExpression, gen_HALL_FSMActions_GetData_ActionExpression, gen_HALL_FSMActions_BinaryOperator_ActionExpression, gen_HALL_FSMActions_DomainPropertyGet_ActionExpression, gen_HALL_FSMActions_Let_ActionExpression, gen_HALL_FSMActions_MessageInvocation_ActionExpression, gen_HALL_Types_SimpleType_Type, gen_HALL_Types_Set_Type, gen_HALL_Types_Boolean_SimpleType, gen_HALL_Types_String_SimpleType, gen_HALL_Types_Number_SimpleType, gen_HALL_FSMActions_UnaryOperator_ActionExpression, gen_HALL_FSMActions_VarRef_ActionExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)