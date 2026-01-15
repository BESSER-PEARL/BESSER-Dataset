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
HALL_Component = Class(name="HALL::Component", is_abstract=True)
HALL_Data = Class(name="HALL::Data")
FSM = Class(name="FSM")
MessageHandler = Class(name="MessageHandler")
HALL_SystemComponent = Class(name="HALL::SystemComponent")
HALL_Model = Class(name="HALL::Model")
HALL_VisualObject = Class(name="HALL::VisualObject")
Component = Class(name="Component")
ColorData = Class(name="ColorData")
GeometryData = Class(name="GeometryData")
HALL_UserProfile = Class(name="HALL::UserProfile")
HALL_Goal = Class(name="HALL::Goal")
MessageDefinition = Class(name="MessageDefinition")
HALL_TaskObject = Class(name="HALL::TaskObject")
HALL_Geometry_RGBColor = Class(name="HALL::Geometry::RGBColor")
Color = Class(name="Color")
HALL_Geometry_ColorState = Class(name="HALL::Geometry::ColorState", is_abstract=True)
AlphaTransparency = Class(name="AlphaTransparency")
HALL_Parameter = Class(name="HALL::Parameter")
HALL_Geometry_Color = Class(name="HALL::Geometry::Color")
RGBColor = Class(name="RGBColor")
ColorState = Class(name="ColorState")
HALL_Geometry_GeometryData = Class(name="HALL::Geometry::GeometryData", is_abstract=True)
HALL_Geometry_GeometryData3D = Class(name="HALL::Geometry::GeometryData3D")
Face = Class(name="Face")
HALL_Geometry_GeometryData2D = Class(name="HALL::Geometry::GeometryData2D")
Point2D = Class(name="Point2D")
HALL_Geometry_Face = Class(name="HALL::Geometry::Face")
Point3D = Class(name="Point3D")
HALL_Geometry_AlphaTransparency = Class(name="HALL::Geometry::AlphaTransparency")
HALL_Geometry_NormalColors = Class(name="HALL::Geometry::NormalColors")
HALL_Geometry_SelectedColors = Class(name="HALL::Geometry::SelectedColors")
HALL_Geometry_DisabledColors = Class(name="HALL::Geometry::DisabledColors")
HALL_Geometry_ColorData = Class(name="HALL::Geometry::ColorData")
SelectedColors = Class(name="SelectedColors")
DisabledColors = Class(name="DisabledColors")
NormalColors = Class(name="NormalColors")
Geometry_HALL_VisualObject = Class(name="Geometry::HALL::VisualObject")
Instructions_PosConditionMessageExpression = Class(name="Instructions::PosConditionMessageExpression")
Actions_ActionMessageExpression = Class(name="Actions::ActionMessageExpression")
HALL_Messages_NamedMessageState = Class(name="HALL::Messages::NamedMessageState")
HALL_Messages_MessageDefinition = Class(name="HALL::Messages::MessageDefinition")
Messages_HALL_Model = Class(name="Messages::HALL::Model")
Messages_HALL_Parameter = Class(name="Messages::HALL::Parameter")
Messages_HALL_Data = Class(name="Messages::HALL::Data")
HALL_Messages_MessageHandler = Class(name="HALL::Messages::MessageHandler")
GeometryData3D = Class(name="GeometryData3D")
HALL_Geometry_Point3D = Class(name="HALL::Geometry::Point3D")
Point = Class(name="Point")
HALL_Geometry_Point2D = Class(name="HALL::Geometry::Point2D")
GeometryData2D = Class(name="GeometryData2D")
HALL_Geometry_Point = Class(name="HALL::Geometry::Point")
HALL_Messages_MessageTransition = Class(name="HALL::Messages::MessageTransition")
MessageState = Class(name="MessageState")
Conditions_PreConditionMessageExpression = Class(name="Conditions::PreConditionMessageExpression")
HALL_Instructions_VarRef = Class(name="HALL::Instructions::VarRef")
PosConditionMessageExpressionElement = Class(name="PosConditionMessageExpressionElement")
HALL_Instructions_Literal = Class(name="HALL::Instructions::Literal")
HALL_Instructions_BinaryOperator = Class(name="HALL::Instructions::BinaryOperator")
HALL_Instructions_UnaryOperator = Class(name="HALL::Instructions::UnaryOperator")
NamedMessageState = Class(name="NamedMessageState")
InitialMessageState = Class(name="InitialMessageState")
Messages_HALL_Component = Class(name="Messages::HALL::Component")
HALL_Messages_MessageState = Class(name="HALL::Messages::MessageState")
MessageTransition = Class(name="MessageTransition")
HALL_Messages_InitialMessageState = Class(name="HALL::Messages::InitialMessageState")
HALL_Instructions_PosConditionMessageExpression = Class(name="HALL::Instructions::PosConditionMessageExpression", is_abstract=True)
Instructions_PosConditionMessageExpressionElement = Class(name="Instructions::PosConditionMessageExpressionElement")
HALL_Instructions_PosConditionMessageExpressionElement = Class(name="HALL::Instructions::PosConditionMessageExpressionElement", is_abstract=True)
HALL_Instructions_Let = Class(name="HALL::Instructions::Let")
HALL_Instructions_DomainPropertyGet = Class(name="HALL::Instructions::DomainPropertyGet")
HALL_Instructions_GetMessageData = Class(name="HALL::Instructions::GetMessageData")
HALL_Instructions_GetMessageParameter = Class(name="HALL::Instructions::GetMessageParameter")
HALL_Instructions_SetTopDown = Class(name="HALL::Instructions::SetTopDown")
HALL_Instructions_GetData = Class(name="HALL::Instructions::GetData")
Instructions_HALL_Component = Class(name="Instructions::HALL::Component")
HALL_Instructions_GetState = Class(name="HALL::Instructions::GetState")
HALL_Instructions_SetState = Class(name="HALL::Instructions::SetState")
HALL_Instructions_SetData = Class(name="HALL::Instructions::SetData")
HALL_Instructions_SetMessageData = Class(name="HALL::Instructions::SetMessageData")
HALL_Instructions_SetMessageParameter = Class(name="HALL::Instructions::SetMessageParameter")
Conditions_HALL_Component = Class(name="Conditions::HALL::Component")
HALL_Conditions_GetData = Class(name="HALL::Conditions::GetData")
HALL_Conditions_Let = Class(name="HALL::Conditions::Let")
HALL_Conditions_UnaryOperator = Class(name="HALL::Conditions::UnaryOperator")
HALL_Conditions_BinaryOperator = Class(name="HALL::Conditions::BinaryOperator")
HALL_Conditions_PreConditionMessageExpression = Class(name="HALL::Conditions::PreConditionMessageExpression", is_abstract=True)
Conditions_PreConditionMessageExpressionElement = Class(name="Conditions::PreConditionMessageExpressionElement")
HALL_Conditions_PreConditionMessageExpressionElement = Class(name="HALL::Conditions::PreConditionMessageExpressionElement", is_abstract=True)
HALL_Conditions_VarRef = Class(name="HALL::Conditions::VarRef")
PreConditionMessageExpressionElement = Class(name="PreConditionMessageExpressionElement")
HALL_Conditions_Literal = Class(name="HALL::Conditions::Literal")
HALL_Conditions_GetMessageData = Class(name="HALL::Conditions::GetMessageData")
HALL_Conditions_GetMessageParameter = Class(name="HALL::Conditions::GetMessageParameter")
HALL_Conditions_DomainPropertyGet = Class(name="HALL::Conditions::DomainPropertyGet")
HALL_Conditions_GetState = Class(name="HALL::Conditions::GetState")
HALL_Actions_Let = Class(name="HALL::Actions::Let")
HALL_Actions_DomainPropertyGet = Class(name="HALL::Actions::DomainPropertyGet")
HALL_Actions_GetMessageData = Class(name="HALL::Actions::GetMessageData")
HALL_Actions_GetMessageParameter = Class(name="HALL::Actions::GetMessageParameter")
HALL_Actions_ActionMessageExpression = Class(name="HALL::Actions::ActionMessageExpression", is_abstract=True)
Actions_ActionMessageExpressionElement = Class(name="Actions::ActionMessageExpressionElement")
HALL_Actions_ActionMessageExpressionElement = Class(name="HALL::Actions::ActionMessageExpressionElement", is_abstract=True)
HALL_Actions_VarRef = Class(name="HALL::Actions::VarRef")
ActionMessageExpressionElement = Class(name="ActionMessageExpressionElement")
HALL_Actions_Literal = Class(name="HALL::Actions::Literal")
HALL_Actions_BinaryOperator = Class(name="HALL::Actions::BinaryOperator")
HALL_FSM_FSM = Class(name="HALL::FSM::FSM")
FSM_HALL_Component = Class(name="FSM::HALL::Component")
InitialState = Class(name="InitialState")
NamedState = Class(name="NamedState")
HALL_FSM_NamedState = Class(name="HALL::FSM::NamedState")
State = Class(name="State")
HALL_FSM_InitialState = Class(name="HALL::FSM::InitialState")
HALL_FSM_Transition = Class(name="HALL::FSM::Transition")
HALL_Actions_MessageInvocation = Class(name="HALL::Actions::MessageInvocation")
HALL_Actions_UnaryOperator = Class(name="HALL::Actions::UnaryOperator")
HALL_Actions_GetData = Class(name="HALL::Actions::GetData")
Actions_HALL_Component = Class(name="Actions::HALL::Component")
HALL_Actions_DomainPropertySet = Class(name="HALL::Actions::DomainPropertySet")
HALL_Actions_Enable = Class(name="HALL::Actions::Enable")
HALL_Trigger_TriggerExpressionElement = Class(name="HALL::Trigger::TriggerExpressionElement", is_abstract=True)
HALL_Trigger_MessageNotification = Class(name="HALL::Trigger::MessageNotification")
TriggerExpressionElement = Class(name="TriggerExpressionElement")
HALL_Trigger_DomainEventFired = Class(name="HALL::Trigger::DomainEventFired")
HALL_FSMInstructions_PosConditionExpression = Class(name="HALL::FSMInstructions::PosConditionExpression", is_abstract=True)
FSMInstructions_PosConditionExpressionElement = Class(name="FSMInstructions::PosConditionExpressionElement")
HALL_FSMInstructions_PosConditionExpressionElement = Class(name="HALL::FSMInstructions::PosConditionExpressionElement", is_abstract=True)
HALL_FSMInstructions_VarRef = Class(name="HALL::FSMInstructions::VarRef")
PosConditionExpressionElement = Class(name="PosConditionExpressionElement")
FSMConditions_PreConditionExpression = Class(name="FSMConditions::PreConditionExpression")
FSMInstructions_PosConditionExpression = Class(name="FSMInstructions::PosConditionExpression")
FSMActions_ActionExpression = Class(name="FSMActions::ActionExpression")
Trigger_TriggerExpression = Class(name="Trigger::TriggerExpression")
HALL_FSM_State = Class(name="HALL::FSM::State", is_abstract=True)
Transition = Class(name="Transition")
HALL_Trigger_TriggerExpression = Class(name="HALL::Trigger::TriggerExpression")
Trigger_TriggerExpressionElement = Class(name="Trigger::TriggerExpressionElement")
HALL_FSMInstructions_SetData = Class(name="HALL::FSMInstructions::SetData")
HALL_FSMInstructions_Let = Class(name="HALL::FSMInstructions::Let")
HALL_FSMInstructions_DomainPropertyGet = Class(name="HALL::FSMInstructions::DomainPropertyGet")
HALL_FSMInstructions_Literal = Class(name="HALL::FSMInstructions::Literal")
HALL_FSMInstructions_BinaryOperator = Class(name="HALL::FSMInstructions::BinaryOperator")
HALL_FSMInstructions_UnaryOperator = Class(name="HALL::FSMInstructions::UnaryOperator")
HALL_FSMInstructions_GetData = Class(name="HALL::FSMInstructions::GetData")
FSMInstructions_HALL_Component = Class(name="FSMInstructions::HALL::Component")
HALL_FSMInstructions_GetState = Class(name="HALL::FSMInstructions::GetState")
HALL_FSMInstructions_SetState = Class(name="HALL::FSMInstructions::SetState")
HALL_FSMConditions_UnaryOperator = Class(name="HALL::FSMConditions::UnaryOperator")
HALL_FSMConditions_GetState = Class(name="HALL::FSMConditions::GetState")
FSMConditions_HALL_Component = Class(name="FSMConditions::HALL::Component")
HALL_FSMConditions_PreConditionExpression = Class(name="HALL::FSMConditions::PreConditionExpression", is_abstract=True)
FSMConditions_PreConditionExpressionElement = Class(name="FSMConditions::PreConditionExpressionElement")
HALL_FSMConditions_PreConditionExpressionElement = Class(name="HALL::FSMConditions::PreConditionExpressionElement", is_abstract=True)
HALL_FSMConditions_Literal = Class(name="HALL::FSMConditions::Literal")
PreConditionExpressionElement = Class(name="PreConditionExpressionElement")
HALL_FSMConditions_VarRef = Class(name="HALL::FSMConditions::VarRef")
HALL_FSMConditions_BinaryOperator = Class(name="HALL::FSMConditions::BinaryOperator")
FSMActions_ActionExpressionElement = Class(name="FSMActions::ActionExpressionElement")
HALL_FSMActions_ActionExpressionElement = Class(name="HALL::FSMActions::ActionExpressionElement", is_abstract=True)
HALL_FSMActions_VarRef = Class(name="HALL::FSMActions::VarRef")
ActionExpressionElement = Class(name="ActionExpressionElement")
HALL_FSMActions_Literal = Class(name="HALL::FSMActions::Literal")
HALL_FSMActions_DomainPropertyGet = Class(name="HALL::FSMActions::DomainPropertyGet")
HALL_FSMActions_Let = Class(name="HALL::FSMActions::Let")
HALL_FSMConditions_GetData = Class(name="HALL::FSMConditions::GetData")
HALL_FSMConditions_DomainPropertyGet = Class(name="HALL::FSMConditions::DomainPropertyGet")
HALL_FSMConditions_Let = Class(name="HALL::FSMConditions::Let")
HALL_FSMActions_ActionExpression = Class(name="HALL::FSMActions::ActionExpression", is_abstract=True)
HALL_FSMActions_DomainPropertySet = Class(name="HALL::FSMActions::DomainPropertySet")
HALL_FSMActions_GetData = Class(name="HALL::FSMActions::GetData")
FSMActions_HALL_Component = Class(name="FSMActions::HALL::Component")
HALL_FSMActions_BinaryOperator = Class(name="HALL::FSMActions::BinaryOperator")
HALL_FSMActions_UnaryOperator = Class(name="HALL::FSMActions::UnaryOperator")
HALL_FSMActions_MessageInvocation = Class(name="HALL::FSMActions::MessageInvocation")
HALL_FSMActions_Enable = Class(name="HALL::FSMActions::Enable")

# HALL_Component class attributes and methods
HALL_Component_name: Property = Property(name="name", type=StringType)
HALL_Component.attributes={HALL_Component_name}

# HALL_Data class attributes and methods
HALL_Data_name: Property = Property(name="name", type=StringType)
HALL_Data_type: Property = Property(name="type", type=StringType)
HALL_Data_initValue: Property = Property(name="initValue", type=StringType)
HALL_Data_currentValue: Property = Property(name="currentValue", type=StringType)
HALL_Data.attributes={HALL_Data_name, HALL_Data_initValue, HALL_Data_type, HALL_Data_currentValue}

# FSM class attributes and methods

# MessageHandler class attributes and methods

# HALL_SystemComponent class attributes and methods

# HALL_Model class attributes and methods

# HALL_VisualObject class attributes and methods

# Component class attributes and methods

# ColorData class attributes and methods

# GeometryData class attributes and methods

# HALL_UserProfile class attributes and methods
HALL_UserProfile_numberofcompletedtasks: Property = Property(name="numberofcompletedtasks", type=IntegerType)
HALL_UserProfile.attributes={HALL_UserProfile_numberofcompletedtasks}

# HALL_Goal class attributes and methods
HALL_Goal_condition: Property = Property(name="condition", type=StringType)
HALL_Goal.attributes={HALL_Goal_condition}

# MessageDefinition class attributes and methods

# HALL_TaskObject class attributes and methods
HALL_TaskObject_completionTime: Property = Property(name="completionTime", type=IntegerType)
HALL_TaskObject_numberofgoalscompleted: Property = Property(name="numberofgoalscompleted", type=IntegerType)
HALL_TaskObject.attributes={HALL_TaskObject_numberofgoalscompleted, HALL_TaskObject_completionTime}

# HALL_Geometry_RGBColor class attributes and methods
HALL_Geometry_RGBColor_redValue: Property = Property(name="redValue", type=IntegerType)
HALL_Geometry_RGBColor_greenValue: Property = Property(name="greenValue", type=IntegerType)
HALL_Geometry_RGBColor_blueValue: Property = Property(name="blueValue", type=IntegerType)
HALL_Geometry_RGBColor.attributes={HALL_Geometry_RGBColor_redValue, HALL_Geometry_RGBColor_blueValue, HALL_Geometry_RGBColor_greenValue}

# Color class attributes and methods

# HALL_Geometry_ColorState class attributes and methods

# AlphaTransparency class attributes and methods

# HALL_Parameter class attributes and methods
HALL_Parameter_name: Property = Property(name="name", type=StringType)
HALL_Parameter_type: Property = Property(name="type", type=StringType)
HALL_Parameter.attributes={HALL_Parameter_type, HALL_Parameter_name}

# HALL_Geometry_Color class attributes and methods

# RGBColor class attributes and methods

# ColorState class attributes and methods

# HALL_Geometry_GeometryData class attributes and methods

# HALL_Geometry_GeometryData3D class attributes and methods

# Face class attributes and methods

# HALL_Geometry_GeometryData2D class attributes and methods
HALL_Geometry_GeometryData2D_labelText: Property = Property(name="labelText", type=StringType)
HALL_Geometry_GeometryData2D.attributes={HALL_Geometry_GeometryData2D_labelText}

# Point2D class attributes and methods

# HALL_Geometry_Face class attributes and methods
HALL_Geometry_Face_labelText: Property = Property(name="labelText", type=StringType)
HALL_Geometry_Face.attributes={HALL_Geometry_Face_labelText}

# Point3D class attributes and methods

# HALL_Geometry_AlphaTransparency class attributes and methods
HALL_Geometry_AlphaTransparency_value: Property = Property(name="value", type=IntegerType)
HALL_Geometry_AlphaTransparency.attributes={HALL_Geometry_AlphaTransparency_value}

# HALL_Geometry_NormalColors class attributes and methods

# HALL_Geometry_SelectedColors class attributes and methods

# HALL_Geometry_DisabledColors class attributes and methods

# HALL_Geometry_ColorData class attributes and methods

# SelectedColors class attributes and methods

# DisabledColors class attributes and methods

# NormalColors class attributes and methods

# Geometry_HALL_VisualObject class attributes and methods

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

# Messages_HALL_Data class attributes and methods

# HALL_Messages_MessageHandler class attributes and methods
HALL_Messages_MessageHandler_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageHandler.attributes={HALL_Messages_MessageHandler_name}

# GeometryData3D class attributes and methods

# HALL_Geometry_Point3D class attributes and methods
HALL_Geometry_Point3D_zCoord: Property = Property(name="zCoord", type=IntegerType)
HALL_Geometry_Point3D.attributes={HALL_Geometry_Point3D_zCoord}

# Point class attributes and methods

# HALL_Geometry_Point2D class attributes and methods

# GeometryData2D class attributes and methods

# HALL_Geometry_Point class attributes and methods
HALL_Geometry_Point_xCoord: Property = Property(name="xCoord", type=IntegerType)
HALL_Geometry_Point_yCoord: Property = Property(name="yCoord", type=IntegerType)
HALL_Geometry_Point.attributes={HALL_Geometry_Point_xCoord, HALL_Geometry_Point_yCoord}

# HALL_Messages_MessageTransition class attributes and methods
HALL_Messages_MessageTransition_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageTransition.attributes={HALL_Messages_MessageTransition_name}

# MessageState class attributes and methods

# Conditions_PreConditionMessageExpression class attributes and methods

# HALL_Instructions_VarRef class attributes and methods
HALL_Instructions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_Instructions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_Instructions_VarRef.attributes={HALL_Instructions_VarRef_name, HALL_Instructions_VarRef_type}

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

# NamedMessageState class attributes and methods

# InitialMessageState class attributes and methods

# Messages_HALL_Component class attributes and methods

# HALL_Messages_MessageState class attributes and methods
HALL_Messages_MessageState_isEnd: Property = Property(name="isEnd", type=BooleanType)
HALL_Messages_MessageState_isContinue: Property = Property(name="isContinue", type=BooleanType)
HALL_Messages_MessageState_isActive: Property = Property(name="isActive", type=BooleanType)
HALL_Messages_MessageState.attributes={HALL_Messages_MessageState_isContinue, HALL_Messages_MessageState_isActive, HALL_Messages_MessageState_isEnd}

# MessageTransition class attributes and methods

# HALL_Messages_InitialMessageState class attributes and methods

# HALL_Instructions_PosConditionMessageExpression class attributes and methods

# Instructions_PosConditionMessageExpressionElement class attributes and methods

# HALL_Instructions_PosConditionMessageExpressionElement class attributes and methods

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

# HALL_Instructions_GetData class attributes and methods
HALL_Instructions_GetData_field: Property = Property(name="field", type=StringType)
HALL_Instructions_GetData.attributes={HALL_Instructions_GetData_field}

# Instructions_HALL_Component class attributes and methods

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

# Conditions_HALL_Component class attributes and methods

# HALL_Conditions_GetData class attributes and methods
HALL_Conditions_GetData_field: Property = Property(name="field", type=StringType)
HALL_Conditions_GetData.attributes={HALL_Conditions_GetData_field}

# HALL_Conditions_Let class attributes and methods
HALL_Conditions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_Conditions_Let.attributes={HALL_Conditions_Let_namevar}

# HALL_Conditions_UnaryOperator class attributes and methods
HALL_Conditions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Conditions_UnaryOperator.attributes={HALL_Conditions_UnaryOperator_operatorname}

# HALL_Conditions_BinaryOperator class attributes and methods
HALL_Conditions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Conditions_BinaryOperator.attributes={HALL_Conditions_BinaryOperator_operatorname}

# HALL_Conditions_PreConditionMessageExpression class attributes and methods

# Conditions_PreConditionMessageExpressionElement class attributes and methods

# HALL_Conditions_PreConditionMessageExpressionElement class attributes and methods

# HALL_Conditions_VarRef class attributes and methods
HALL_Conditions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_Conditions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_Conditions_VarRef.attributes={HALL_Conditions_VarRef_name, HALL_Conditions_VarRef_type}

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

# HALL_Actions_Let class attributes and methods
HALL_Actions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_Actions_Let.attributes={HALL_Actions_Let_namevar}

# HALL_Actions_DomainPropertyGet class attributes and methods
HALL_Actions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_Actions_DomainPropertyGet.attributes={HALL_Actions_DomainPropertyGet_name}

# HALL_Actions_GetMessageData class attributes and methods
HALL_Actions_GetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Actions_GetMessageData.attributes={HALL_Actions_GetMessageData_field}

# HALL_Actions_GetMessageParameter class attributes and methods
HALL_Actions_GetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Actions_GetMessageParameter.attributes={HALL_Actions_GetMessageParameter_field}

# HALL_Actions_ActionMessageExpression class attributes and methods

# Actions_ActionMessageExpressionElement class attributes and methods

# HALL_Actions_ActionMessageExpressionElement class attributes and methods

# HALL_Actions_VarRef class attributes and methods
HALL_Actions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_Actions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_Actions_VarRef.attributes={HALL_Actions_VarRef_type, HALL_Actions_VarRef_name}

# ActionMessageExpressionElement class attributes and methods

# HALL_Actions_Literal class attributes and methods
HALL_Actions_Literal_value: Property = Property(name="value", type=StringType)
HALL_Actions_Literal.attributes={HALL_Actions_Literal_value}

# HALL_Actions_BinaryOperator class attributes and methods
HALL_Actions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Actions_BinaryOperator.attributes={HALL_Actions_BinaryOperator_operatorname}

# HALL_FSM_FSM class attributes and methods

# FSM_HALL_Component class attributes and methods

# InitialState class attributes and methods

# NamedState class attributes and methods

# HALL_FSM_NamedState class attributes and methods
HALL_FSM_NamedState_name: Property = Property(name="name", type=StringType)
HALL_FSM_NamedState.attributes={HALL_FSM_NamedState_name}

# State class attributes and methods

# HALL_FSM_InitialState class attributes and methods

# HALL_FSM_Transition class attributes and methods
HALL_FSM_Transition_name: Property = Property(name="name", type=StringType)
HALL_FSM_Transition.attributes={HALL_FSM_Transition_name}

# HALL_Actions_MessageInvocation class attributes and methods
HALL_Actions_MessageInvocation_name: Property = Property(name="name", type=StringType)
HALL_Actions_MessageInvocation_isTopDown: Property = Property(name="isTopDown", type=BooleanType)
HALL_Actions_MessageInvocation.attributes={HALL_Actions_MessageInvocation_isTopDown, HALL_Actions_MessageInvocation_name}

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

# HALL_FSMInstructions_SetData class attributes and methods
HALL_FSMInstructions_SetData_field: Property = Property(name="field", type=StringType)
HALL_FSMInstructions_SetData.attributes={HALL_FSMInstructions_SetData_field}

# HALL_FSMInstructions_Let class attributes and methods
HALL_FSMInstructions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_FSMInstructions_Let.attributes={HALL_FSMInstructions_Let_namevar}

# HALL_FSMInstructions_DomainPropertyGet class attributes and methods
HALL_FSMInstructions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMInstructions_DomainPropertyGet.attributes={HALL_FSMInstructions_DomainPropertyGet_name}

# HALL_FSMInstructions_Literal class attributes and methods
HALL_FSMInstructions_Literal_value: Property = Property(name="value", type=StringType)
HALL_FSMInstructions_Literal.attributes={HALL_FSMInstructions_Literal_value}

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

# HALL_FSMConditions_UnaryOperator class attributes and methods
HALL_FSMConditions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMConditions_UnaryOperator.attributes={HALL_FSMConditions_UnaryOperator_operatorname}

# HALL_FSMConditions_GetState class attributes and methods

# FSMConditions_HALL_Component class attributes and methods

# HALL_FSMConditions_PreConditionExpression class attributes and methods

# FSMConditions_PreConditionExpressionElement class attributes and methods

# HALL_FSMConditions_PreConditionExpressionElement class attributes and methods

# HALL_FSMConditions_Literal class attributes and methods
HALL_FSMConditions_Literal_value: Property = Property(name="value", type=StringType)
HALL_FSMConditions_Literal.attributes={HALL_FSMConditions_Literal_value}

# PreConditionExpressionElement class attributes and methods

# HALL_FSMConditions_VarRef class attributes and methods
HALL_FSMConditions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_FSMConditions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_FSMConditions_VarRef.attributes={HALL_FSMConditions_VarRef_name, HALL_FSMConditions_VarRef_type}

# HALL_FSMConditions_BinaryOperator class attributes and methods
HALL_FSMConditions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMConditions_BinaryOperator.attributes={HALL_FSMConditions_BinaryOperator_operatorname}

# FSMActions_ActionExpressionElement class attributes and methods

# HALL_FSMActions_ActionExpressionElement class attributes and methods

# HALL_FSMActions_VarRef class attributes and methods
HALL_FSMActions_VarRef_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_VarRef_type: Property = Property(name="type", type=StringType)
HALL_FSMActions_VarRef.attributes={HALL_FSMActions_VarRef_name, HALL_FSMActions_VarRef_type}

# ActionExpressionElement class attributes and methods

# HALL_FSMActions_Literal class attributes and methods
HALL_FSMActions_Literal_value: Property = Property(name="value", type=StringType)
HALL_FSMActions_Literal.attributes={HALL_FSMActions_Literal_value}

# HALL_FSMActions_DomainPropertyGet class attributes and methods
HALL_FSMActions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_DomainPropertyGet.attributes={HALL_FSMActions_DomainPropertyGet_name}

# HALL_FSMActions_Let class attributes and methods
HALL_FSMActions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_FSMActions_Let.attributes={HALL_FSMActions_Let_namevar}

# HALL_FSMConditions_GetData class attributes and methods
HALL_FSMConditions_GetData_field: Property = Property(name="field", type=StringType)
HALL_FSMConditions_GetData.attributes={HALL_FSMConditions_GetData_field}

# HALL_FSMConditions_DomainPropertyGet class attributes and methods
HALL_FSMConditions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMConditions_DomainPropertyGet.attributes={HALL_FSMConditions_DomainPropertyGet_name}

# HALL_FSMConditions_Let class attributes and methods
HALL_FSMConditions_Let_namevar: Property = Property(name="namevar", type=StringType)
HALL_FSMConditions_Let.attributes={HALL_FSMConditions_Let_namevar}

# HALL_FSMActions_ActionExpression class attributes and methods

# HALL_FSMActions_DomainPropertySet class attributes and methods
HALL_FSMActions_DomainPropertySet_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_DomainPropertySet.attributes={HALL_FSMActions_DomainPropertySet_name}

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

# HALL_FSMActions_MessageInvocation class attributes and methods
HALL_FSMActions_MessageInvocation_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_MessageInvocation_isTopDown: Property = Property(name="isTopDown", type=BooleanType)
HALL_FSMActions_MessageInvocation.attributes={HALL_FSMActions_MessageInvocation_isTopDown, HALL_FSMActions_MessageInvocation_name}

# HALL_FSMActions_Enable class attributes and methods

# Relationships
visualObjectInv3: BinaryAssociation = BinaryAssociation(
    name="visualObjectInv3",
    ends={
        Property(name="UserProfile", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="visualObject", type=HALL_UserProfile, multiplicity=Multiplicity(0, 1))
    }
)
componentSet5: BinaryAssociation = BinaryAssociation(
    name="componentSet5",
    ends={
        Property(name="VisualObject", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv", type=HALL_VisualObject, multiplicity=Multiplicity(0, 9999))
    }
)
componentSetInv7: BinaryAssociation = BinaryAssociation(
    name="componentSetInv7",
    ends={
        Property(name="VisualObject8", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet", type=HALL_VisualObject, multiplicity=Multiplicity(0, 1))
    }
)
data9: BinaryAssociation = BinaryAssociation(
    name="data9",
    ends={
        Property(name="Data", type=HALL_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInvComponent", type=HALL_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
FSM10: BinaryAssociation = BinaryAssociation(
    name="FSM10",
    ends={
        Property(name="FSM11", type=HALL_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM", type=FSM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageHandlerSet12: BinaryAssociation = BinaryAssociation(
    name="messageHandlerSet12",
    ends={
        Property(name="Messages", type=HALL_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageHandler", type=MessageHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemComponentInv13: BinaryAssociation = BinaryAssociation(
    name="systemComponentInv13",
    ends={
        Property(name="Model", type=HALL_SystemComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="systemComponent", type=HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
colorData0: BinaryAssociation = BinaryAssociation(
    name="colorData0",
    ends={
        Property(name="Geometry", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorData", type=ColorData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
geometryData1: BinaryAssociation = BinaryAssociation(
    name="geometryData1",
    ends={
        Property(name="Geometry2", type=HALL_VisualObject, multiplicity=Multiplicity(1, 1)),
        Property(name="GeometryData", type=GeometryData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentSetInv37: BinaryAssociation = BinaryAssociation(
    name="componentSetInv37",
    ends={
        Property(name="UserProfile39", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet38", type=HALL_UserProfile, multiplicity=Multiplicity(0, 1))
    }
)
goal40: BinaryAssociation = BinaryAssociation(
    name="goal40",
    ends={
        Property(name="Goal", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="goalInv", type=HALL_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskObjectInv41: BinaryAssociation = BinaryAssociation(
    name="taskObjectInv41",
    ends={
        Property(name="UserProfile42", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="taskObject", type=HALL_UserProfile, multiplicity=Multiplicity(0, 1))
    }
)
componentSet44: BinaryAssociation = BinaryAssociation(
    name="componentSet44",
    ends={
        Property(name="TaskObject46", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv45", type=HALL_TaskObject, multiplicity=Multiplicity(0, 9999))
    }
)
componentSetInv48: BinaryAssociation = BinaryAssociation(
    name="componentSetInv48",
    ends={
        Property(name="TaskObject50", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet49", type=HALL_TaskObject, multiplicity=Multiplicity(0, 1))
    }
)
goalInv51: BinaryAssociation = BinaryAssociation(
    name="goalInv51",
    ends={
        Property(name="TaskObject52", type=HALL_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goal", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1))
    }
)
componentSet15: BinaryAssociation = BinaryAssociation(
    name="componentSet15",
    ends={
        Property(name="SystemComponent", type=HALL_SystemComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv16", type=HALL_SystemComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentSetInv18: BinaryAssociation = BinaryAssociation(
    name="componentSetInv18",
    ends={
        Property(name="SystemComponent20", type=HALL_SystemComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet19", type=HALL_SystemComponent, multiplicity=Multiplicity(0, 1))
    }
)
userProfile21: BinaryAssociation = BinaryAssociation(
    name="userProfile21",
    ends={
        Property(name="UserProfile22", type=HALL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="userProfileInv", type=HALL_UserProfile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemComponent23: BinaryAssociation = BinaryAssociation(
    name="systemComponent23",
    ends={
        Property(name="SystemComponent24", type=HALL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="systemComponentInv", type=HALL_SystemComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageDefinition25: BinaryAssociation = BinaryAssociation(
    name="messageDefinition25",
    ends={
        Property(name="Messages26", type=HALL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageDefinition", type=MessageDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
visualObject27: BinaryAssociation = BinaryAssociation(
    name="visualObject27",
    ends={
        Property(name="VisualObject28", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="visualObjectInv", type=HALL_VisualObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskObject29: BinaryAssociation = BinaryAssociation(
    name="taskObject29",
    ends={
        Property(name="TaskObject", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="taskObjectInv", type=HALL_TaskObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userProfileInv30: BinaryAssociation = BinaryAssociation(
    name="userProfileInv30",
    ends={
        Property(name="Model31", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="userProfile", type=HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
componentSet33: BinaryAssociation = BinaryAssociation(
    name="componentSet33",
    ends={
        Property(name="UserProfile35", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv34", type=HALL_UserProfile, multiplicity=Multiplicity(0, 9999))
    }
)
foregroundColorInv68: BinaryAssociation = BinaryAssociation(
    name="foregroundColorInv68",
    ends={
        Property(name="Geometry69", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorState", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColorInv70: BinaryAssociation = BinaryAssociation(
    name="backgroundColorInv70",
    ends={
        Property(name="Geometry72", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorState71", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
ambianceColorInv73: BinaryAssociation = BinaryAssociation(
    name="ambianceColorInv73",
    ends={
        Property(name="Geometry74", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="Color", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
difuseColorInv75: BinaryAssociation = BinaryAssociation(
    name="difuseColorInv75",
    ends={
        Property(name="Geometry77", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="Color76", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
specularColorInv78: BinaryAssociation = BinaryAssociation(
    name="specularColorInv78",
    ends={
        Property(name="Geometry80", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="Color79", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
foregroundColor81: BinaryAssociation = BinaryAssociation(
    name="foregroundColor81",
    ends={
        Property(name="Geometry83", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="Color82", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor84: BinaryAssociation = BinaryAssociation(
    name="backgroundColor84",
    ends={
        Property(name="Geometry86", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="Color85", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterInv53: BinaryAssociation = BinaryAssociation(
    name="parameterInv53",
    ends={
        Property(name="Messages55", type=HALL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageDefinition54", type=MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
dataInvMessageDefinition56: BinaryAssociation = BinaryAssociation(
    name="dataInvMessageDefinition56",
    ends={
        Property(name="Messages58", type=HALL_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageDefinition57", type=MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
dataInvComponent59: BinaryAssociation = BinaryAssociation(
    name="dataInvComponent59",
    ends={
        Property(name="Component", type=HALL_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="data", type=HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
ambianceColor60: BinaryAssociation = BinaryAssociation(
    name="ambianceColor60",
    ends={
        Property(name="Geometry61", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="RGBColor", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
difuseColor62: BinaryAssociation = BinaryAssociation(
    name="difuseColor62",
    ends={
        Property(name="Geometry64", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="RGBColor63", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specularColor65: BinaryAssociation = BinaryAssociation(
    name="specularColor65",
    ends={
        Property(name="Geometry67", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="RGBColor66", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
geometryDataInv109: BinaryAssociation = BinaryAssociation(
    name="geometryDataInv109",
    ends={
        Property(name="VisualObject110", type=HALL_Geometry_GeometryData, multiplicity=Multiplicity(1, 1)),
        Property(name="geometryData", type=Geometry_HALL_VisualObject, multiplicity=Multiplicity(0, 1))
    }
)
face111: BinaryAssociation = BinaryAssociation(
    name="face111",
    ends={
        Property(name="Geometry112", type=HALL_Geometry_GeometryData3D, multiplicity=Multiplicity(1, 1)),
        Property(name="Face", type=Face, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
point2d113: BinaryAssociation = BinaryAssociation(
    name="point2d113",
    ends={
        Property(name="Geometry114", type=HALL_Geometry_GeometryData2D, multiplicity=Multiplicity(1, 1)),
        Property(name="Point2D", type=Point2D, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
alphaTransparency87: BinaryAssociation = BinaryAssociation(
    name="alphaTransparency87",
    ends={
        Property(name="Geometry88", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="AlphaTransparency", type=AlphaTransparency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alphaTransparencyInv89: BinaryAssociation = BinaryAssociation(
    name="alphaTransparencyInv89",
    ends={
        Property(name="Geometry91", type=HALL_Geometry_AlphaTransparency, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorState90", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
normalColorsInv92: BinaryAssociation = BinaryAssociation(
    name="normalColorsInv92",
    ends={
        Property(name="Geometry94", type=HALL_Geometry_NormalColors, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorData93", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
selectedColorsInv95: BinaryAssociation = BinaryAssociation(
    name="selectedColorsInv95",
    ends={
        Property(name="Geometry97", type=HALL_Geometry_SelectedColors, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorData96", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
disabledColorsInv98: BinaryAssociation = BinaryAssociation(
    name="disabledColorsInv98",
    ends={
        Property(name="Geometry100", type=HALL_Geometry_DisabledColors, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorData99", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
selectedColors101: BinaryAssociation = BinaryAssociation(
    name="selectedColors101",
    ends={
        Property(name="Geometry102", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="SelectedColors", type=SelectedColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
disabledColors103: BinaryAssociation = BinaryAssociation(
    name="disabledColors103",
    ends={
        Property(name="Geometry104", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="DisabledColors", type=DisabledColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
normalColors105: BinaryAssociation = BinaryAssociation(
    name="normalColors105",
    ends={
        Property(name="Geometry106", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="NormalColors", type=NormalColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colorDataInv107: BinaryAssociation = BinaryAssociation(
    name="colorDataInv107",
    ends={
        Property(name="VisualObject108", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="colorData", type=Geometry_HALL_VisualObject, multiplicity=Multiplicity(0, 1))
    }
)
PosCondition130: BinaryAssociation = BinaryAssociation(
    name="PosCondition130",
    ends={
        Property(name="Messages131", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Instructions", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ActionMessage132: BinaryAssociation = BinaryAssociation(
    name="ActionMessage132",
    ends={
        Property(name="Messages133", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageStateInv134: BinaryAssociation = BinaryAssociation(
    name="messageStateInv134",
    ends={
        Property(name="Messages136", type=HALL_Messages_NamedMessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageHandler135", type=MessageHandler, multiplicity=Multiplicity(0, 1))
    }
)
messageDefinitionInv137: BinaryAssociation = BinaryAssociation(
    name="messageDefinitionInv137",
    ends={
        Property(name="Model138", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition", type=Messages_HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
parameter139: BinaryAssociation = BinaryAssociation(
    name="parameter139",
    ends={
        Property(name="Parameter", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterInv", type=Messages_HALL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data140: BinaryAssociation = BinaryAssociation(
    name="data140",
    ends={
        Property(name="Data141", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInvMessageDefinition", type=Messages_HALL_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
point3d115: BinaryAssociation = BinaryAssociation(
    name="point3d115",
    ends={
        Property(name="Geometry116", type=HALL_Geometry_Face, multiplicity=Multiplicity(1, 1)),
        Property(name="Point3D", type=Point3D, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
faceInv117: BinaryAssociation = BinaryAssociation(
    name="faceInv117",
    ends={
        Property(name="Geometry118", type=HALL_Geometry_Face, multiplicity=Multiplicity(1, 1)),
        Property(name="GeometryData3D", type=GeometryData3D, multiplicity=Multiplicity(0, 1))
    }
)
point2dInv119: BinaryAssociation = BinaryAssociation(
    name="point2dInv119",
    ends={
        Property(name="Geometry121", type=HALL_Geometry_Point3D, multiplicity=Multiplicity(1, 1)),
        Property(name="Face120", type=Face, multiplicity=Multiplicity(0, 1))
    }
)
point2dInv122: BinaryAssociation = BinaryAssociation(
    name="point2dInv122",
    ends={
        Property(name="Geometry123", type=HALL_Geometry_Point2D, multiplicity=Multiplicity(1, 1)),
        Property(name="GeometryData2D", type=GeometryData2D, multiplicity=Multiplicity(0, 1))
    }
)
transitionsInvMessageState124: BinaryAssociation = BinaryAssociation(
    name="transitionsInvMessageState124",
    ends={
        Property(name="Messages125", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageState", type=MessageState, multiplicity=Multiplicity(0, 1))
    }
)
stateRef126: BinaryAssociation = BinaryAssociation(
    name="stateRef126",
    ends={
        Property(name="MessageState127", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageTransition", type=MessageState, multiplicity=Multiplicity(1, 1))
    }
)
PreCondition128: BinaryAssociation = BinaryAssociation(
    name="PreCondition128",
    ends={
        Property(name="Messages129", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Conditions", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PosConditionSetInv159: BinaryAssociation = BinaryAssociation(
    name="PosConditionSetInv159",
    ends={
        Property(name="Messages161", type=HALL_Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Instructions160", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(0, 1))
    }
)
leftexpression162: BinaryAssociation = BinaryAssociation(
    name="leftexpression162",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement", type=HALL_Instructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_BinaryOperator", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
rightexpression163: BinaryAssociation = BinaryAssociation(
    name="rightexpression163",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement165", type=HALL_Instructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_BinaryOperator164", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
expression166: BinaryAssociation = BinaryAssociation(
    name="expression166",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement167", type=HALL_Instructions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_UnaryOperator", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
messageState142: BinaryAssociation = BinaryAssociation(
    name="messageState142",
    ends={
        Property(name="Messages143", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedMessageState", type=NamedMessageState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialMessageState144: BinaryAssociation = BinaryAssociation(
    name="initialMessageState144",
    ends={
        Property(name="Messages145", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="InitialMessageState", type=InitialMessageState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageHandlerSetInv146: BinaryAssociation = BinaryAssociation(
    name="messageHandlerSetInv146",
    ends={
        Property(name="Component147", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="messageHandlerSet", type=Messages_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
transitions148: BinaryAssociation = BinaryAssociation(
    name="transitions148",
    ends={
        Property(name="Messages149", type=HALL_Messages_MessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageTransition", type=MessageTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialMessageStateInv150: BinaryAssociation = BinaryAssociation(
    name="initialMessageStateInv150",
    ends={
        Property(name="Messages152", type=HALL_Messages_InitialMessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageHandler151", type=MessageHandler, multiplicity=Multiplicity(0, 1))
    }
)
PosConditionInv153: BinaryAssociation = BinaryAssociation(
    name="PosConditionInv153",
    ends={
        Property(name="Messages155", type=HALL_Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageTransition154", type=MessageTransition, multiplicity=Multiplicity(0, 1))
    }
)
PosConditionSet156: BinaryAssociation = BinaryAssociation(
    name="PosConditionSet156",
    ends={
        Property(name="Messages158", type=HALL_Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Instructions157", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value180: BinaryAssociation = BinaryAssociation(
    name="value180",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement181", type=HALL_Instructions_SetMessageParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetMessageParameter", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
in182: BinaryAssociation = BinaryAssociation(
    name="in182",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement183", type=HALL_Instructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_Let", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
initialization184: BinaryAssociation = BinaryAssociation(
    name="initialization184",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement186", type=HALL_Instructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_Let185", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
value187: BinaryAssociation = BinaryAssociation(
    name="value187",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement188", type=HALL_Instructions_SetTopDown, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetTopDown", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference168: BinaryAssociation = BinaryAssociation(
    name="reference168",
    ends={
        Property(name="Instructions_HALL_Component", type=HALL_Instructions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_GetData", type=Instructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference169: BinaryAssociation = BinaryAssociation(
    name="reference169",
    ends={
        Property(name="Instructions_HALL_Component170", type=HALL_Instructions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_GetState", type=Instructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference171: BinaryAssociation = BinaryAssociation(
    name="reference171",
    ends={
        Property(name="Instructions_HALL_Component172", type=HALL_Instructions_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetState", type=Instructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
value173: BinaryAssociation = BinaryAssociation(
    name="value173",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement174", type=HALL_Instructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetData", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference175: BinaryAssociation = BinaryAssociation(
    name="reference175",
    ends={
        Property(name="Instructions_HALL_Component177", type=HALL_Instructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetData176", type=Instructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
value178: BinaryAssociation = BinaryAssociation(
    name="value178",
    ends={
        Property(name="Instructions_PosConditionMessageExpressionElement179", type=HALL_Instructions_SetMessageData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetMessageData", type=Instructions_PosConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference198: BinaryAssociation = BinaryAssociation(
    name="reference198",
    ends={
        Property(name="Conditions_HALL_Component", type=HALL_Conditions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_GetState", type=Conditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference199: BinaryAssociation = BinaryAssociation(
    name="reference199",
    ends={
        Property(name="Conditions_HALL_Component200", type=HALL_Conditions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_GetData", type=Conditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
in201: BinaryAssociation = BinaryAssociation(
    name="in201",
    ends={
        Property(name="Conditions_PreConditionMessageExpressionElement", type=HALL_Conditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_Let", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
initialization202: BinaryAssociation = BinaryAssociation(
    name="initialization202",
    ends={
        Property(name="Conditions_PreConditionMessageExpressionElement204", type=HALL_Conditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_Let203", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
expression205: BinaryAssociation = BinaryAssociation(
    name="expression205",
    ends={
        Property(name="Conditions_PreConditionMessageExpressionElement206", type=HALL_Conditions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_UnaryOperator", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
PreConditionInv189: BinaryAssociation = BinaryAssociation(
    name="PreConditionInv189",
    ends={
        Property(name="Messages191", type=HALL_Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageTransition190", type=MessageTransition, multiplicity=Multiplicity(0, 1))
    }
)
PreConditionSet192: BinaryAssociation = BinaryAssociation(
    name="PreConditionSet192",
    ends={
        Property(name="Messages194", type=HALL_Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Conditions193", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PreConditionSetInv195: BinaryAssociation = BinaryAssociation(
    name="PreConditionSetInv195",
    ends={
        Property(name="Messages197", type=HALL_Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Conditions196", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(0, 1))
    }
)
leftexpression221: BinaryAssociation = BinaryAssociation(
    name="leftexpression221",
    ends={
        Property(name="Actions_ActionMessageExpressionElement", type=HALL_Actions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_BinaryOperator", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
rightexpression222: BinaryAssociation = BinaryAssociation(
    name="rightexpression222",
    ends={
        Property(name="Actions_ActionMessageExpressionElement224", type=HALL_Actions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_BinaryOperator223", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
in225: BinaryAssociation = BinaryAssociation(
    name="in225",
    ends={
        Property(name="Actions_ActionMessageExpressionElement226", type=HALL_Actions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Let", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
initialization227: BinaryAssociation = BinaryAssociation(
    name="initialization227",
    ends={
        Property(name="Actions_ActionMessageExpressionElement229", type=HALL_Actions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Let228", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
leftexpression207: BinaryAssociation = BinaryAssociation(
    name="leftexpression207",
    ends={
        Property(name="Conditions_PreConditionMessageExpressionElement208", type=HALL_Conditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_BinaryOperator", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
rightexpression209: BinaryAssociation = BinaryAssociation(
    name="rightexpression209",
    ends={
        Property(name="Conditions_PreConditionMessageExpressionElement211", type=HALL_Conditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_BinaryOperator210", type=Conditions_PreConditionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
ActionMessageInv212: BinaryAssociation = BinaryAssociation(
    name="ActionMessageInv212",
    ends={
        Property(name="Messages214", type=HALL_Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageTransition213", type=MessageTransition, multiplicity=Multiplicity(0, 1))
    }
)
ActionMessageSet215: BinaryAssociation = BinaryAssociation(
    name="ActionMessageSet215",
    ends={
        Property(name="Messages217", type=HALL_Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions216", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActionMessageSetInv218: BinaryAssociation = BinaryAssociation(
    name="ActionMessageSetInv218",
    ends={
        Property(name="Messages220", type=HALL_Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Actions219", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(0, 1))
    }
)
FSMInv242: BinaryAssociation = BinaryAssociation(
    name="FSMInv242",
    ends={
        Property(name="Component244", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM243", type=FSM_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
initialState245: BinaryAssociation = BinaryAssociation(
    name="initialState245",
    ends={
        Property(name="FSM246", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="InitialState", type=InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
state247: BinaryAssociation = BinaryAssociation(
    name="state247",
    ends={
        Property(name="FSM248", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedState", type=NamedState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fsm249: BinaryAssociation = BinaryAssociation(
    name="fsm249",
    ends={
        Property(name="FSM251", type=HALL_FSM_NamedState, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM250", type=FSM, multiplicity=Multiplicity(0, 1))
    }
)
fsm252: BinaryAssociation = BinaryAssociation(
    name="fsm252",
    ends={
        Property(name="FSM254", type=HALL_FSM_InitialState, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM253", type=FSM, multiplicity=Multiplicity(0, 1))
    }
)
actualset230: BinaryAssociation = BinaryAssociation(
    name="actualset230",
    ends={
        Property(name="Actions_ActionMessageExpressionElement231", type=HALL_Actions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_MessageInvocation", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(0, 1))
    }
)
expression232: BinaryAssociation = BinaryAssociation(
    name="expression232",
    ends={
        Property(name="Actions_ActionMessageExpressionElement233", type=HALL_Actions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_UnaryOperator", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference234: BinaryAssociation = BinaryAssociation(
    name="reference234",
    ends={
        Property(name="Actions_HALL_Component", type=HALL_Actions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_GetData", type=Actions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
value235: BinaryAssociation = BinaryAssociation(
    name="value235",
    ends={
        Property(name="Actions_ActionMessageExpressionElement236", type=HALL_Actions_DomainPropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_DomainPropertySet", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
value237: BinaryAssociation = BinaryAssociation(
    name="value237",
    ends={
        Property(name="Actions_ActionMessageExpressionElement238", type=HALL_Actions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Enable", type=Actions_ActionMessageExpressionElement, multiplicity=Multiplicity(0, 9999))
    }
)
reference239: BinaryAssociation = BinaryAssociation(
    name="reference239",
    ends={
        Property(name="MessageDefinition241", type=HALL_Actions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Enable240", type=MessageDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TriggerExpressionSetInv275: BinaryAssociation = BinaryAssociation(
    name="TriggerExpressionSetInv275",
    ends={
        Property(name="FSM277", type=HALL_Trigger_TriggerExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Trigger276", type=Trigger_TriggerExpression, multiplicity=Multiplicity(0, 1))
    }
)
PosConditionSet278: BinaryAssociation = BinaryAssociation(
    name="PosConditionSet278",
    ends={
        Property(name="FSM280", type=HALL_FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMInstructions279", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PosConditionInv281: BinaryAssociation = BinaryAssociation(
    name="PosConditionInv281",
    ends={
        Property(name="FSM283", type=HALL_FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition282", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
PosConditionSetInv284: BinaryAssociation = BinaryAssociation(
    name="PosConditionSetInv284",
    ends={
        Property(name="FSM286", type=HALL_FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMInstructions285", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(0, 1))
    }
)
source255: BinaryAssociation = BinaryAssociation(
    name="source255",
    ends={
        Property(name="FSM256", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="State", type=State, multiplicity=Multiplicity(1, 1))
    }
)
stateRef257: BinaryAssociation = BinaryAssociation(
    name="stateRef257",
    ends={
        Property(name="State258", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition", type=State, multiplicity=Multiplicity(1, 1))
    }
)
PreCondition259: BinaryAssociation = BinaryAssociation(
    name="PreCondition259",
    ends={
        Property(name="FSM260", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMConditions", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PosCondition261: BinaryAssociation = BinaryAssociation(
    name="PosCondition261",
    ends={
        Property(name="FSM262", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMInstructions", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Action263: BinaryAssociation = BinaryAssociation(
    name="Action263",
    ends={
        Property(name="FSM264", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMActions", type=FSMActions_ActionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Trigger265: BinaryAssociation = BinaryAssociation(
    name="Trigger265",
    ends={
        Property(name="FSM266", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Trigger", type=Trigger_TriggerExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions267: BinaryAssociation = BinaryAssociation(
    name="transitions267",
    ends={
        Property(name="FSM268", type=HALL_FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TriggerExpressionSet269: BinaryAssociation = BinaryAssociation(
    name="TriggerExpressionSet269",
    ends={
        Property(name="FSM271", type=HALL_Trigger_TriggerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Trigger270", type=Trigger_TriggerExpressionElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TriggerInv272: BinaryAssociation = BinaryAssociation(
    name="TriggerInv272",
    ends={
        Property(name="FSM274", type=HALL_Trigger_TriggerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition273", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
reference296: BinaryAssociation = BinaryAssociation(
    name="reference296",
    ends={
        Property(name="FSMInstructions_HALL_Component297", type=HALL_FSMInstructions_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetState", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
value298: BinaryAssociation = BinaryAssociation(
    name="value298",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement299", type=HALL_FSMInstructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetData", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference300: BinaryAssociation = BinaryAssociation(
    name="reference300",
    ends={
        Property(name="FSMInstructions_HALL_Component302", type=HALL_FSMInstructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetData301", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
in303: BinaryAssociation = BinaryAssociation(
    name="in303",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement304", type=HALL_FSMInstructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_Let", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
initialization305: BinaryAssociation = BinaryAssociation(
    name="initialization305",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement307", type=HALL_FSMInstructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_Let306", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
rightexpression287: BinaryAssociation = BinaryAssociation(
    name="rightexpression287",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement", type=HALL_FSMInstructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_BinaryOperator", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
leftexpression288: BinaryAssociation = BinaryAssociation(
    name="leftexpression288",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement290", type=HALL_FSMInstructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_BinaryOperator289", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
expression291: BinaryAssociation = BinaryAssociation(
    name="expression291",
    ends={
        Property(name="FSMInstructions_PosConditionExpressionElement292", type=HALL_FSMInstructions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_UnaryOperator", type=FSMInstructions_PosConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference293: BinaryAssociation = BinaryAssociation(
    name="reference293",
    ends={
        Property(name="FSMInstructions_HALL_Component", type=HALL_FSMInstructions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_GetData", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference294: BinaryAssociation = BinaryAssociation(
    name="reference294",
    ends={
        Property(name="FSMInstructions_HALL_Component295", type=HALL_FSMInstructions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_GetState", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
leftexpression318: BinaryAssociation = BinaryAssociation(
    name="leftexpression318",
    ends={
        Property(name="FSMConditions_PreConditionExpressionElement320", type=HALL_FSMConditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_BinaryOperator319", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
expression321: BinaryAssociation = BinaryAssociation(
    name="expression321",
    ends={
        Property(name="FSMConditions_PreConditionExpressionElement322", type=HALL_FSMConditions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_UnaryOperator", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference323: BinaryAssociation = BinaryAssociation(
    name="reference323",
    ends={
        Property(name="FSMConditions_HALL_Component", type=HALL_FSMConditions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_GetState", type=FSMConditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
PreConditionSet308: BinaryAssociation = BinaryAssociation(
    name="PreConditionSet308",
    ends={
        Property(name="FSM310", type=HALL_FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMConditions309", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PreConditionInv311: BinaryAssociation = BinaryAssociation(
    name="PreConditionInv311",
    ends={
        Property(name="FSM313", type=HALL_FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition312", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
PreConditionSetInv314: BinaryAssociation = BinaryAssociation(
    name="PreConditionSetInv314",
    ends={
        Property(name="FSM316", type=HALL_FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMConditions315", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(0, 1))
    }
)
rightexpression317: BinaryAssociation = BinaryAssociation(
    name="rightexpression317",
    ends={
        Property(name="FSMConditions_PreConditionExpressionElement", type=HALL_FSMConditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_BinaryOperator", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
ActionExpressionSet334: BinaryAssociation = BinaryAssociation(
    name="ActionExpressionSet334",
    ends={
        Property(name="FSM336", type=HALL_FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMActions335", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActionExpressionSetInv337: BinaryAssociation = BinaryAssociation(
    name="ActionExpressionSetInv337",
    ends={
        Property(name="FSM339", type=HALL_FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMActions338", type=FSMActions_ActionExpression, multiplicity=Multiplicity(0, 1))
    }
)
in340: BinaryAssociation = BinaryAssociation(
    name="in340",
    ends={
        Property(name="FSMActions_ActionExpressionElement", type=HALL_FSMActions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Let", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference324: BinaryAssociation = BinaryAssociation(
    name="reference324",
    ends={
        Property(name="FSMConditions_HALL_Component325", type=HALL_FSMConditions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_GetData", type=FSMConditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
initialization326: BinaryAssociation = BinaryAssociation(
    name="initialization326",
    ends={
        Property(name="FSMConditions_PreConditionExpressionElement327", type=HALL_FSMConditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_Let", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
in328: BinaryAssociation = BinaryAssociation(
    name="in328",
    ends={
        Property(name="FSMConditions_PreConditionExpressionElement330", type=HALL_FSMConditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_Let329", type=FSMConditions_PreConditionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
ActionInv331: BinaryAssociation = BinaryAssociation(
    name="ActionInv331",
    ends={
        Property(name="FSM333", type=HALL_FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition332", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
message348: BinaryAssociation = BinaryAssociation(
    name="message348",
    ends={
        Property(name="MessageDefinition350", type=HALL_FSMActions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Enable349", type=MessageDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value351: BinaryAssociation = BinaryAssociation(
    name="value351",
    ends={
        Property(name="FSMActions_ActionExpressionElement352", type=HALL_FSMActions_DomainPropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_DomainPropertySet", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
reference353: BinaryAssociation = BinaryAssociation(
    name="reference353",
    ends={
        Property(name="FSMActions_HALL_Component", type=HALL_FSMActions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_GetData", type=FSMActions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
leftoperator354: BinaryAssociation = BinaryAssociation(
    name="leftoperator354",
    ends={
        Property(name="FSMActions_ActionExpressionElement355", type=HALL_FSMActions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_BinaryOperator", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
initialization341: BinaryAssociation = BinaryAssociation(
    name="initialization341",
    ends={
        Property(name="FSMActions_ActionExpressionElement343", type=HALL_FSMActions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Let342", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
rightexpression356: BinaryAssociation = BinaryAssociation(
    name="rightexpression356",
    ends={
        Property(name="FSMActions_ActionExpressionElement358", type=HALL_FSMActions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_BinaryOperator357", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
expression359: BinaryAssociation = BinaryAssociation(
    name="expression359",
    ends={
        Property(name="FSMActions_ActionExpressionElement360", type=HALL_FSMActions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_UnaryOperator", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(1, 1))
    }
)
actualset344: BinaryAssociation = BinaryAssociation(
    name="actualset344",
    ends={
        Property(name="FSMActions_ActionExpressionElement345", type=HALL_FSMActions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_MessageInvocation", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(0, 9999))
    }
)
value346: BinaryAssociation = BinaryAssociation(
    name="value346",
    ends={
        Property(name="FSMActions_ActionExpressionElement347", type=HALL_FSMActions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Enable", type=FSMActions_ActionExpressionElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_HALL_SystemComponent_Component = Generalization(general=Component, specific=HALL_SystemComponent)
gen_HALL_VisualObject_Component = Generalization(general=Component, specific=HALL_VisualObject)
gen_HALL_TaskObject_Component = Generalization(general=Component, specific=HALL_TaskObject)
gen_HALL_UserProfile_Component = Generalization(general=Component, specific=HALL_UserProfile)
gen_HALL_Geometry_GeometryData3D_GeometryData = Generalization(general=GeometryData, specific=HALL_Geometry_GeometryData3D)
gen_HALL_Geometry_GeometryData2D_GeometryData = Generalization(general=GeometryData, specific=HALL_Geometry_GeometryData2D)
gen_HALL_Geometry_NormalColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_NormalColors)
gen_HALL_Geometry_SelectedColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_SelectedColors)
gen_HALL_Geometry_DisabledColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_DisabledColors)
gen_HALL_Messages_NamedMessageState_MessageState = Generalization(general=MessageState, specific=HALL_Messages_NamedMessageState)
gen_HALL_Geometry_Point3D_Point = Generalization(general=Point, specific=HALL_Geometry_Point3D)
gen_HALL_Geometry_Point2D_Point = Generalization(general=Point, specific=HALL_Geometry_Point2D)
gen_HALL_Instructions_VarRef_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_VarRef)
gen_HALL_Instructions_Literal_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_Literal)
gen_HALL_Instructions_BinaryOperator_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_BinaryOperator)
gen_HALL_Instructions_UnaryOperator_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_UnaryOperator)
gen_HALL_Messages_InitialMessageState_MessageState = Generalization(general=MessageState, specific=HALL_Messages_InitialMessageState)
gen_HALL_Instructions_Let_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_Let)
gen_HALL_Instructions_DomainPropertyGet_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_DomainPropertyGet)
gen_HALL_Instructions_GetMessageData_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_GetMessageData)
gen_HALL_Instructions_GetMessageParameter_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_GetMessageParameter)
gen_HALL_Instructions_SetTopDown_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_SetTopDown)
gen_HALL_Instructions_GetData_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_GetData)
gen_HALL_Instructions_GetState_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_GetState)
gen_HALL_Instructions_SetState_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_SetState)
gen_HALL_Instructions_SetData_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_SetData)
gen_HALL_Instructions_SetMessageData_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_SetMessageData)
gen_HALL_Instructions_SetMessageParameter_PosConditionMessageExpressionElement = Generalization(general=PosConditionMessageExpressionElement, specific=HALL_Instructions_SetMessageParameter)
gen_HALL_Conditions_GetData_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_GetData)
gen_HALL_Conditions_Let_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_Let)
gen_HALL_Conditions_UnaryOperator_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_UnaryOperator)
gen_HALL_Conditions_BinaryOperator_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_BinaryOperator)
gen_HALL_Conditions_VarRef_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_VarRef)
gen_HALL_Conditions_Literal_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_Literal)
gen_HALL_Conditions_GetMessageData_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_GetMessageData)
gen_HALL_Conditions_GetMessageParameter_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_GetMessageParameter)
gen_HALL_Conditions_DomainPropertyGet_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_DomainPropertyGet)
gen_HALL_Conditions_GetState_PreConditionMessageExpressionElement = Generalization(general=PreConditionMessageExpressionElement, specific=HALL_Conditions_GetState)
gen_HALL_Actions_Let_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_Let)
gen_HALL_Actions_DomainPropertyGet_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_DomainPropertyGet)
gen_HALL_Actions_GetMessageData_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_GetMessageData)
gen_HALL_Actions_GetMessageParameter_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_GetMessageParameter)
gen_HALL_Actions_VarRef_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_VarRef)
gen_HALL_Actions_Literal_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_Literal)
gen_HALL_Actions_BinaryOperator_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_BinaryOperator)
gen_HALL_FSM_NamedState_State = Generalization(general=State, specific=HALL_FSM_NamedState)
gen_HALL_FSM_InitialState_State = Generalization(general=State, specific=HALL_FSM_InitialState)
gen_HALL_Actions_MessageInvocation_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_MessageInvocation)
gen_HALL_Actions_UnaryOperator_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_UnaryOperator)
gen_HALL_Actions_GetData_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_GetData)
gen_HALL_Actions_DomainPropertySet_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_DomainPropertySet)
gen_HALL_Actions_Enable_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_Actions_Enable)
gen_HALL_Trigger_MessageNotification_TriggerExpressionElement = Generalization(general=TriggerExpressionElement, specific=HALL_Trigger_MessageNotification)
gen_HALL_Trigger_DomainEventFired_TriggerExpressionElement = Generalization(general=TriggerExpressionElement, specific=HALL_Trigger_DomainEventFired)
gen_HALL_FSMInstructions_VarRef_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_VarRef)
gen_HALL_FSMInstructions_SetData_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_SetData)
gen_HALL_FSMInstructions_Let_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_Let)
gen_HALL_FSMInstructions_DomainPropertyGet_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_DomainPropertyGet)
gen_HALL_FSMInstructions_Literal_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_Literal)
gen_HALL_FSMInstructions_BinaryOperator_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_BinaryOperator)
gen_HALL_FSMInstructions_UnaryOperator_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_UnaryOperator)
gen_HALL_FSMInstructions_GetData_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_GetData)
gen_HALL_FSMInstructions_GetState_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_GetState)
gen_HALL_FSMInstructions_SetState_PosConditionExpressionElement = Generalization(general=PosConditionExpressionElement, specific=HALL_FSMInstructions_SetState)
gen_HALL_FSMConditions_UnaryOperator_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_UnaryOperator)
gen_HALL_FSMConditions_GetState_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_GetState)
gen_HALL_FSMConditions_Literal_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_Literal)
gen_HALL_FSMConditions_VarRef_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_VarRef)
gen_HALL_FSMConditions_BinaryOperator_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_BinaryOperator)
gen_HALL_FSMActions_VarRef_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_VarRef)
gen_HALL_FSMActions_Literal_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_Literal)
gen_HALL_FSMActions_DomainPropertyGet_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_DomainPropertyGet)
gen_HALL_FSMActions_Let_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_Let)
gen_HALL_FSMConditions_GetData_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_GetData)
gen_HALL_FSMConditions_DomainPropertyGet_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_DomainPropertyGet)
gen_HALL_FSMConditions_Let_PreConditionExpressionElement = Generalization(general=PreConditionExpressionElement, specific=HALL_FSMConditions_Let)
gen_HALL_FSMActions_DomainPropertySet_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_DomainPropertySet)
gen_HALL_FSMActions_GetData_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_GetData)
gen_HALL_FSMActions_BinaryOperator_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_BinaryOperator)
gen_HALL_FSMActions_UnaryOperator_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_UnaryOperator)
gen_HALL_FSMActions_MessageInvocation_ActionExpressionElement = Generalization(general=ActionExpressionElement, specific=HALL_FSMActions_MessageInvocation)
gen_HALL_FSMActions_Enable_ActionMessageExpressionElement = Generalization(general=ActionMessageExpressionElement, specific=HALL_FSMActions_Enable)

# Domain Model
domain_model = DomainModel(
    name="HALL",
    types={HALL_Component, HALL_Data, FSM, MessageHandler, HALL_SystemComponent, HALL_Model, HALL_VisualObject, Component, ColorData, GeometryData, HALL_UserProfile, HALL_Goal, MessageDefinition, HALL_TaskObject, HALL_Geometry_RGBColor, Color, HALL_Geometry_ColorState, AlphaTransparency, HALL_Parameter, HALL_Geometry_Color, RGBColor, ColorState, HALL_Geometry_GeometryData, HALL_Geometry_GeometryData3D, Face, HALL_Geometry_GeometryData2D, Point2D, HALL_Geometry_Face, Point3D, HALL_Geometry_AlphaTransparency, HALL_Geometry_NormalColors, HALL_Geometry_SelectedColors, HALL_Geometry_DisabledColors, HALL_Geometry_ColorData, SelectedColors, DisabledColors, NormalColors, Geometry_HALL_VisualObject, Instructions_PosConditionMessageExpression, Actions_ActionMessageExpression, HALL_Messages_NamedMessageState, HALL_Messages_MessageDefinition, Messages_HALL_Model, Messages_HALL_Parameter, Messages_HALL_Data, HALL_Messages_MessageHandler, GeometryData3D, HALL_Geometry_Point3D, Point, HALL_Geometry_Point2D, GeometryData2D, HALL_Geometry_Point, HALL_Messages_MessageTransition, MessageState, Conditions_PreConditionMessageExpression, HALL_Instructions_VarRef, PosConditionMessageExpressionElement, HALL_Instructions_Literal, HALL_Instructions_BinaryOperator, HALL_Instructions_UnaryOperator, NamedMessageState, InitialMessageState, Messages_HALL_Component, HALL_Messages_MessageState, MessageTransition, HALL_Messages_InitialMessageState, HALL_Instructions_PosConditionMessageExpression, Instructions_PosConditionMessageExpressionElement, HALL_Instructions_PosConditionMessageExpressionElement, HALL_Instructions_Let, HALL_Instructions_DomainPropertyGet, HALL_Instructions_GetMessageData, HALL_Instructions_GetMessageParameter, HALL_Instructions_SetTopDown, HALL_Instructions_GetData, Instructions_HALL_Component, HALL_Instructions_GetState, HALL_Instructions_SetState, HALL_Instructions_SetData, HALL_Instructions_SetMessageData, HALL_Instructions_SetMessageParameter, Conditions_HALL_Component, HALL_Conditions_GetData, HALL_Conditions_Let, HALL_Conditions_UnaryOperator, HALL_Conditions_BinaryOperator, HALL_Conditions_PreConditionMessageExpression, Conditions_PreConditionMessageExpressionElement, HALL_Conditions_PreConditionMessageExpressionElement, HALL_Conditions_VarRef, PreConditionMessageExpressionElement, HALL_Conditions_Literal, HALL_Conditions_GetMessageData, HALL_Conditions_GetMessageParameter, HALL_Conditions_DomainPropertyGet, HALL_Conditions_GetState, HALL_Actions_Let, HALL_Actions_DomainPropertyGet, HALL_Actions_GetMessageData, HALL_Actions_GetMessageParameter, HALL_Actions_ActionMessageExpression, Actions_ActionMessageExpressionElement, HALL_Actions_ActionMessageExpressionElement, HALL_Actions_VarRef, ActionMessageExpressionElement, HALL_Actions_Literal, HALL_Actions_BinaryOperator, HALL_FSM_FSM, FSM_HALL_Component, InitialState, NamedState, HALL_FSM_NamedState, State, HALL_FSM_InitialState, HALL_FSM_Transition, HALL_Actions_MessageInvocation, HALL_Actions_UnaryOperator, HALL_Actions_GetData, Actions_HALL_Component, HALL_Actions_DomainPropertySet, HALL_Actions_Enable, HALL_Trigger_TriggerExpressionElement, HALL_Trigger_MessageNotification, TriggerExpressionElement, HALL_Trigger_DomainEventFired, HALL_FSMInstructions_PosConditionExpression, FSMInstructions_PosConditionExpressionElement, HALL_FSMInstructions_PosConditionExpressionElement, HALL_FSMInstructions_VarRef, PosConditionExpressionElement, FSMConditions_PreConditionExpression, FSMInstructions_PosConditionExpression, FSMActions_ActionExpression, Trigger_TriggerExpression, HALL_FSM_State, Transition, HALL_Trigger_TriggerExpression, Trigger_TriggerExpressionElement, HALL_FSMInstructions_SetData, HALL_FSMInstructions_Let, HALL_FSMInstructions_DomainPropertyGet, HALL_FSMInstructions_Literal, HALL_FSMInstructions_BinaryOperator, HALL_FSMInstructions_UnaryOperator, HALL_FSMInstructions_GetData, FSMInstructions_HALL_Component, HALL_FSMInstructions_GetState, HALL_FSMInstructions_SetState, HALL_FSMConditions_UnaryOperator, HALL_FSMConditions_GetState, FSMConditions_HALL_Component, HALL_FSMConditions_PreConditionExpression, FSMConditions_PreConditionExpressionElement, HALL_FSMConditions_PreConditionExpressionElement, HALL_FSMConditions_Literal, PreConditionExpressionElement, HALL_FSMConditions_VarRef, HALL_FSMConditions_BinaryOperator, FSMActions_ActionExpressionElement, HALL_FSMActions_ActionExpressionElement, HALL_FSMActions_VarRef, ActionExpressionElement, HALL_FSMActions_Literal, HALL_FSMActions_DomainPropertyGet, HALL_FSMActions_Let, HALL_FSMConditions_GetData, HALL_FSMConditions_DomainPropertyGet, HALL_FSMConditions_Let, HALL_FSMActions_ActionExpression, HALL_FSMActions_DomainPropertySet, HALL_FSMActions_GetData, FSMActions_HALL_Component, HALL_FSMActions_BinaryOperator, HALL_FSMActions_UnaryOperator, HALL_FSMActions_MessageInvocation, HALL_FSMActions_Enable},
    associations={visualObjectInv3, componentSet5, componentSetInv7, data9, FSM10, messageHandlerSet12, systemComponentInv13, colorData0, geometryData1, componentSetInv37, goal40, taskObjectInv41, componentSet44, componentSetInv48, goalInv51, componentSet15, componentSetInv18, userProfile21, systemComponent23, messageDefinition25, visualObject27, taskObject29, userProfileInv30, componentSet33, foregroundColorInv68, backgroundColorInv70, ambianceColorInv73, difuseColorInv75, specularColorInv78, foregroundColor81, backgroundColor84, parameterInv53, dataInvMessageDefinition56, dataInvComponent59, ambianceColor60, difuseColor62, specularColor65, geometryDataInv109, face111, point2d113, alphaTransparency87, alphaTransparencyInv89, normalColorsInv92, selectedColorsInv95, disabledColorsInv98, selectedColors101, disabledColors103, normalColors105, colorDataInv107, PosCondition130, ActionMessage132, messageStateInv134, messageDefinitionInv137, parameter139, data140, point3d115, faceInv117, point2dInv119, point2dInv122, transitionsInvMessageState124, stateRef126, PreCondition128, PosConditionSetInv159, leftexpression162, rightexpression163, expression166, messageState142, initialMessageState144, messageHandlerSetInv146, transitions148, initialMessageStateInv150, PosConditionInv153, PosConditionSet156, value180, in182, initialization184, value187, reference168, reference169, reference171, value173, reference175, value178, reference198, reference199, in201, initialization202, expression205, PreConditionInv189, PreConditionSet192, PreConditionSetInv195, leftexpression221, rightexpression222, in225, initialization227, leftexpression207, rightexpression209, ActionMessageInv212, ActionMessageSet215, ActionMessageSetInv218, FSMInv242, initialState245, state247, fsm249, fsm252, actualset230, expression232, reference234, value235, value237, reference239, TriggerExpressionSetInv275, PosConditionSet278, PosConditionInv281, PosConditionSetInv284, source255, stateRef257, PreCondition259, PosCondition261, Action263, Trigger265, transitions267, TriggerExpressionSet269, TriggerInv272, reference296, value298, reference300, in303, initialization305, rightexpression287, leftexpression288, expression291, reference293, reference294, leftexpression318, expression321, reference323, PreConditionSet308, PreConditionInv311, PreConditionSetInv314, rightexpression317, ActionExpressionSet334, ActionExpressionSetInv337, in340, reference324, initialization326, in328, ActionInv331, message348, value351, reference353, leftoperator354, initialization341, rightexpression356, expression359, actualset344, value346},
    generalizations={gen_HALL_SystemComponent_Component, gen_HALL_VisualObject_Component, gen_HALL_TaskObject_Component, gen_HALL_UserProfile_Component, gen_HALL_Geometry_GeometryData3D_GeometryData, gen_HALL_Geometry_GeometryData2D_GeometryData, gen_HALL_Geometry_NormalColors_ColorState, gen_HALL_Geometry_SelectedColors_ColorState, gen_HALL_Geometry_DisabledColors_ColorState, gen_HALL_Messages_NamedMessageState_MessageState, gen_HALL_Geometry_Point3D_Point, gen_HALL_Geometry_Point2D_Point, gen_HALL_Instructions_VarRef_PosConditionMessageExpressionElement, gen_HALL_Instructions_Literal_PosConditionMessageExpressionElement, gen_HALL_Instructions_BinaryOperator_PosConditionMessageExpressionElement, gen_HALL_Instructions_UnaryOperator_PosConditionMessageExpressionElement, gen_HALL_Messages_InitialMessageState_MessageState, gen_HALL_Instructions_Let_PosConditionMessageExpressionElement, gen_HALL_Instructions_DomainPropertyGet_PosConditionMessageExpressionElement, gen_HALL_Instructions_GetMessageData_PosConditionMessageExpressionElement, gen_HALL_Instructions_GetMessageParameter_PosConditionMessageExpressionElement, gen_HALL_Instructions_SetTopDown_PosConditionMessageExpressionElement, gen_HALL_Instructions_GetData_PosConditionMessageExpressionElement, gen_HALL_Instructions_GetState_PosConditionMessageExpressionElement, gen_HALL_Instructions_SetState_PosConditionMessageExpressionElement, gen_HALL_Instructions_SetData_PosConditionMessageExpressionElement, gen_HALL_Instructions_SetMessageData_PosConditionMessageExpressionElement, gen_HALL_Instructions_SetMessageParameter_PosConditionMessageExpressionElement, gen_HALL_Conditions_GetData_PreConditionMessageExpressionElement, gen_HALL_Conditions_Let_PreConditionMessageExpressionElement, gen_HALL_Conditions_UnaryOperator_PreConditionMessageExpressionElement, gen_HALL_Conditions_BinaryOperator_PreConditionMessageExpressionElement, gen_HALL_Conditions_VarRef_PreConditionMessageExpressionElement, gen_HALL_Conditions_Literal_PreConditionMessageExpressionElement, gen_HALL_Conditions_GetMessageData_PreConditionMessageExpressionElement, gen_HALL_Conditions_GetMessageParameter_PreConditionMessageExpressionElement, gen_HALL_Conditions_DomainPropertyGet_PreConditionMessageExpressionElement, gen_HALL_Conditions_GetState_PreConditionMessageExpressionElement, gen_HALL_Actions_Let_ActionMessageExpressionElement, gen_HALL_Actions_DomainPropertyGet_ActionMessageExpressionElement, gen_HALL_Actions_GetMessageData_ActionMessageExpressionElement, gen_HALL_Actions_GetMessageParameter_ActionMessageExpressionElement, gen_HALL_Actions_VarRef_ActionMessageExpressionElement, gen_HALL_Actions_Literal_ActionMessageExpressionElement, gen_HALL_Actions_BinaryOperator_ActionMessageExpressionElement, gen_HALL_FSM_NamedState_State, gen_HALL_FSM_InitialState_State, gen_HALL_Actions_MessageInvocation_ActionMessageExpressionElement, gen_HALL_Actions_UnaryOperator_ActionMessageExpressionElement, gen_HALL_Actions_GetData_ActionMessageExpressionElement, gen_HALL_Actions_DomainPropertySet_ActionMessageExpressionElement, gen_HALL_Actions_Enable_ActionMessageExpressionElement, gen_HALL_Trigger_MessageNotification_TriggerExpressionElement, gen_HALL_Trigger_DomainEventFired_TriggerExpressionElement, gen_HALL_FSMInstructions_VarRef_PosConditionExpressionElement, gen_HALL_FSMInstructions_SetData_PosConditionExpressionElement, gen_HALL_FSMInstructions_Let_PosConditionExpressionElement, gen_HALL_FSMInstructions_DomainPropertyGet_PosConditionExpressionElement, gen_HALL_FSMInstructions_Literal_PosConditionExpressionElement, gen_HALL_FSMInstructions_BinaryOperator_PosConditionExpressionElement, gen_HALL_FSMInstructions_UnaryOperator_PosConditionExpressionElement, gen_HALL_FSMInstructions_GetData_PosConditionExpressionElement, gen_HALL_FSMInstructions_GetState_PosConditionExpressionElement, gen_HALL_FSMInstructions_SetState_PosConditionExpressionElement, gen_HALL_FSMConditions_UnaryOperator_PreConditionExpressionElement, gen_HALL_FSMConditions_GetState_PreConditionExpressionElement, gen_HALL_FSMConditions_Literal_PreConditionExpressionElement, gen_HALL_FSMConditions_VarRef_PreConditionExpressionElement, gen_HALL_FSMConditions_BinaryOperator_PreConditionExpressionElement, gen_HALL_FSMActions_VarRef_ActionExpressionElement, gen_HALL_FSMActions_Literal_ActionExpressionElement, gen_HALL_FSMActions_DomainPropertyGet_ActionExpressionElement, gen_HALL_FSMActions_Let_ActionExpressionElement, gen_HALL_FSMConditions_GetData_PreConditionExpressionElement, gen_HALL_FSMConditions_DomainPropertyGet_PreConditionExpressionElement, gen_HALL_FSMConditions_Let_PreConditionExpressionElement, gen_HALL_FSMActions_DomainPropertySet_ActionExpressionElement, gen_HALL_FSMActions_GetData_ActionExpressionElement, gen_HALL_FSMActions_BinaryOperator_ActionExpressionElement, gen_HALL_FSMActions_UnaryOperator_ActionExpressionElement, gen_HALL_FSMActions_MessageInvocation_ActionExpressionElement, gen_HALL_FSMActions_Enable_ActionMessageExpressionElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)