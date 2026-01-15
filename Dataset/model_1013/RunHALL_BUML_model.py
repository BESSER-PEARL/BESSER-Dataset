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
HALL_VisualObject = Class(name="HALL::VisualObject")
Component = Class(name="Component")
ColorData = Class(name="ColorData")
GeometryData = Class(name="GeometryData")
HALL_UserProfile = Class(name="HALL::UserProfile")
HALL_Component = Class(name="HALL::Component", is_abstract=True)
HALL_Data = Class(name="HALL::Data")
FSM = Class(name="FSM")
MessageHandler = Class(name="MessageHandler")
HALL_SystemComponent = Class(name="HALL::SystemComponent")
HALL_Model = Class(name="HALL::Model")
HALL_Parameter = Class(name="HALL::Parameter")
MessageDefinition = Class(name="MessageDefinition")
Type = Class(name="Type")
HALL_Geometry_Color = Class(name="HALL::Geometry::Color")
RGBColor = Class(name="RGBColor")
HALL_TaskObject = Class(name="HALL::TaskObject")
HALL_Goal = Class(name="HALL::Goal")
HALL_Geometry_ColorState = Class(name="HALL::Geometry::ColorState", is_abstract=True)
AlphaTransparency = Class(name="AlphaTransparency")
HALL_Geometry_AlphaTransparency = Class(name="HALL::Geometry::AlphaTransparency")
HALL_Geometry_NormalColors = Class(name="HALL::Geometry::NormalColors")
HALL_Geometry_SelectedColors = Class(name="HALL::Geometry::SelectedColors")
HALL_Geometry_DisabledColors = Class(name="HALL::Geometry::DisabledColors")
HALL_Geometry_ColorData = Class(name="HALL::Geometry::ColorData")
SelectedColors = Class(name="SelectedColors")
DisabledColors = Class(name="DisabledColors")
NormalColors = Class(name="NormalColors")
Geometry_HALL_VisualObject = Class(name="Geometry::HALL::VisualObject")
ColorState = Class(name="ColorState")
HALL_Geometry_RGBColor = Class(name="HALL::Geometry::RGBColor")
Color = Class(name="Color")
HALL_Geometry_Face = Class(name="HALL::Geometry::Face")
Point3D = Class(name="Point3D")
GeometryData3D = Class(name="GeometryData3D")
HALL_Geometry_Point3D = Class(name="HALL::Geometry::Point3D")
Point = Class(name="Point")
HALL_Geometry_Point2D = Class(name="HALL::Geometry::Point2D")
GeometryData2D = Class(name="GeometryData2D")
HALL_Geometry_Point = Class(name="HALL::Geometry::Point")
HALL_Messages_MessageTransition = Class(name="HALL::Messages::MessageTransition")
MessageState = Class(name="MessageState")
Conditions_PreConditionMessage = Class(name="Conditions::PreConditionMessage")
Instructions_PosConditionMessage = Class(name="Instructions::PosConditionMessage")
HALL_Geometry_GeometryData = Class(name="HALL::Geometry::GeometryData", is_abstract=True)
HALL_Geometry_GeometryData3D = Class(name="HALL::Geometry::GeometryData3D")
Face = Class(name="Face")
HALL_Geometry_GeometryData2D = Class(name="HALL::Geometry::GeometryData2D")
Point2D = Class(name="Point2D")
Messages_HALL_Data = Class(name="Messages::HALL::Data")
HALL_Messages_MessageHandler = Class(name="HALL::Messages::MessageHandler")
RegularMessageState = Class(name="RegularMessageState")
InitialMessageState = Class(name="InitialMessageState")
Messages_HALL_Component = Class(name="Messages::HALL::Component")
HALL_Messages_MessageState = Class(name="HALL::Messages::MessageState")
MessageTransition = Class(name="MessageTransition")
HALL_Messages_InitialMessageState = Class(name="HALL::Messages::InitialMessageState")
HALL_Instructions_PosConditionMessage = Class(name="HALL::Instructions::PosConditionMessage")
Instructions_PosConditionMessageExpression = Class(name="Instructions::PosConditionMessageExpression")
HALL_Instructions_PosConditionMessageExpression = Class(name="HALL::Instructions::PosConditionMessageExpression", is_abstract=True)
HALL_Instructions_Literal = Class(name="HALL::Instructions::Literal")
PosConditionMessageExpression = Class(name="PosConditionMessageExpression")
HALL_Instructions_BinaryOperator = Class(name="HALL::Instructions::BinaryOperator")
Actions_ActionMessage = Class(name="Actions::ActionMessage")
HALL_Messages_RegularMessageState = Class(name="HALL::Messages::RegularMessageState")
HALL_Messages_MessageDefinition = Class(name="HALL::Messages::MessageDefinition")
Messages_HALL_Model = Class(name="Messages::HALL::Model")
Messages_HALL_Parameter = Class(name="Messages::HALL::Parameter")
HALL_Instructions_UnaryOperator = Class(name="HALL::Instructions::UnaryOperator")
HALL_Instructions_GetData = Class(name="HALL::Instructions::GetData")
Instructions_HALL_Data = Class(name="Instructions::HALL::Data")
HALL_Instructions_GetState = Class(name="HALL::Instructions::GetState")
HALL_Instructions_SetMessageParameter = Class(name="HALL::Instructions::SetMessageParameter")
HALL_Instructions_Let = Class(name="HALL::Instructions::Let")
HALL_Instructions_DomainPropertyGet = Class(name="HALL::Instructions::DomainPropertyGet")
HALL_Instructions_GetMessageData = Class(name="HALL::Instructions::GetMessageData")
HALL_Instructions_GetMessageParameter = Class(name="HALL::Instructions::GetMessageParameter")
Instructions_HALL_Component = Class(name="Instructions::HALL::Component")
HALL_Instructions_SetState = Class(name="HALL::Instructions::SetState")
State = Class(name="State")
HALL_Instructions_SetData = Class(name="HALL::Instructions::SetData")
HALL_Instructions_SetMessageData = Class(name="HALL::Instructions::SetMessageData")
HALL_Conditions_PreConditionMessageExpression = Class(name="HALL::Conditions::PreConditionMessageExpression", is_abstract=True)
HALL_Conditions_Literal = Class(name="HALL::Conditions::Literal")
PreConditionMessageExpression = Class(name="PreConditionMessageExpression")
HALL_Conditions_GetMessageData = Class(name="HALL::Conditions::GetMessageData")
HALL_Conditions_GetMessageParameter = Class(name="HALL::Conditions::GetMessageParameter")
HALL_Conditions_DomainPropertyGet = Class(name="HALL::Conditions::DomainPropertyGet")
HALL_Conditions_GetState = Class(name="HALL::Conditions::GetState")
Conditions_HALL_Component = Class(name="Conditions::HALL::Component")
HALL_Conditions_GetData = Class(name="HALL::Conditions::GetData")
Conditions_HALL_Data = Class(name="Conditions::HALL::Data")
HALL_Conditions_Let = Class(name="HALL::Conditions::Let")
HALL_Conditions_UnaryOperator = Class(name="HALL::Conditions::UnaryOperator")
HALL_Instructions_SetTopDown = Class(name="HALL::Instructions::SetTopDown")
HALL_Instructions_VarRef = Class(name="HALL::Instructions::VarRef")
Instructions_Let = Class(name="Instructions::Let")
HALL_Conditions_PreConditionMessage = Class(name="HALL::Conditions::PreConditionMessage")
Conditions_PreConditionMessageExpression = Class(name="Conditions::PreConditionMessageExpression")
HALL_Actions_ActionMessage = Class(name="HALL::Actions::ActionMessage")
Actions_ActionMessageExpression = Class(name="Actions::ActionMessageExpression")
HALL_Actions_ActionMessageExpression = Class(name="HALL::Actions::ActionMessageExpression", is_abstract=True)
HALL_Actions_VarRef = Class(name="HALL::Actions::VarRef")
ActionMessageExpression = Class(name="ActionMessageExpression")
Actions_Let = Class(name="Actions::Let")
HALL_Actions_Literal = Class(name="HALL::Actions::Literal")
HALL_Actions_BinaryOperator = Class(name="HALL::Actions::BinaryOperator")
HALL_Conditions_BinaryOperator = Class(name="HALL::Conditions::BinaryOperator")
HALL_Conditions_VarRef = Class(name="HALL::Conditions::VarRef")
HALL_Actions_GetMessageData = Class(name="HALL::Actions::GetMessageData")
Conditions_Let = Class(name="Conditions::Let")
HALL_Actions_GetMessageParameter = Class(name="HALL::Actions::GetMessageParameter")
HALL_Actions_MessageInvocation = Class(name="HALL::Actions::MessageInvocation")
HALL_Actions_UnaryOperator = Class(name="HALL::Actions::UnaryOperator")
HALL_Actions_GetData = Class(name="HALL::Actions::GetData")
Actions_HALL_Component = Class(name="Actions::HALL::Component")
HALL_Actions_DomainPropertySet = Class(name="HALL::Actions::DomainPropertySet")
HALL_Actions_Let = Class(name="HALL::Actions::Let")
HALL_Actions_DomainPropertyGet = Class(name="HALL::Actions::DomainPropertyGet")
HALL_FSM_InitialState = Class(name="HALL::FSM::InitialState")
HALL_FSM_Transition = Class(name="HALL::FSM::Transition")
FSMConditions_PreCondition = Class(name="FSMConditions::PreCondition")
FSMInstructions_PosCondition = Class(name="FSMInstructions::PosCondition")
FSMActions_Action = Class(name="FSMActions::Action")
Trigger_Trigger = Class(name="Trigger::Trigger")
HALL_FSM_State = Class(name="HALL::FSM::State", is_abstract=True)
Transition = Class(name="Transition")
HALL_Trigger_Trigger = Class(name="HALL::Trigger::Trigger")
Trigger_TriggerExpression = Class(name="Trigger::TriggerExpression")
HALL_Actions_Enable = Class(name="HALL::Actions::Enable")
HALL_Trigger_TriggerExpression = Class(name="HALL::Trigger::TriggerExpression", is_abstract=True)
HALL_Trigger_MessageNotification = Class(name="HALL::Trigger::MessageNotification")
TriggerExpression = Class(name="TriggerExpression")
HALL_FSM_FSM = Class(name="HALL::FSM::FSM")
FSM_HALL_Component = Class(name="FSM::HALL::Component")
InitialState = Class(name="InitialState")
RegularState = Class(name="RegularState")
HALL_FSM_RegularState = Class(name="HALL::FSM::RegularState")
HALL_FSMInstructions_UnaryOperator = Class(name="HALL::FSMInstructions::UnaryOperator")
HALL_FSMInstructions_GetData = Class(name="HALL::FSMInstructions::GetData")
FSMInstructions_HALL_Component = Class(name="FSMInstructions::HALL::Component")
HALL_FSMInstructions_GetState = Class(name="HALL::FSMInstructions::GetState")
HALL_FSMInstructions_SetState = Class(name="HALL::FSMInstructions::SetState")
HALL_FSMInstructions_SetData = Class(name="HALL::FSMInstructions::SetData")
FSMInstructions_HALL_Data = Class(name="FSMInstructions::HALL::Data")
HALL_Trigger_DomainEventFired = Class(name="HALL::Trigger::DomainEventFired")
HALL_FSMInstructions_PosCondition = Class(name="HALL::FSMInstructions::PosCondition")
FSMInstructions_PosConditionExpression = Class(name="FSMInstructions::PosConditionExpression")
HALL_FSMInstructions_PosConditionExpression = Class(name="HALL::FSMInstructions::PosConditionExpression", is_abstract=True)
HALL_FSMInstructions_Literal = Class(name="HALL::FSMInstructions::Literal")
PosConditionExpression = Class(name="PosConditionExpression")
HALL_FSMInstructions_BinaryOperator = Class(name="HALL::FSMInstructions::BinaryOperator")
FSMInstructions_Let = Class(name="FSMInstructions::Let")
HALL_FSMConditions_PreCondition = Class(name="HALL::FSMConditions::PreCondition")
FSMConditions_PreConditionExpression = Class(name="FSMConditions::PreConditionExpression")
HALL_FSMConditions_PreConditionExpression = Class(name="HALL::FSMConditions::PreConditionExpression", is_abstract=True)
HALL_FSMConditions_Literal = Class(name="HALL::FSMConditions::Literal")
PreConditionExpression = Class(name="PreConditionExpression")
HALL_FSMConditions_BinaryOperator = Class(name="HALL::FSMConditions::BinaryOperator")
HALL_FSMConditions_UnaryOperator = Class(name="HALL::FSMConditions::UnaryOperator")
HALL_FSMConditions_GetState = Class(name="HALL::FSMConditions::GetState")
FSMConditions_HALL_Component = Class(name="FSMConditions::HALL::Component")
HALL_FSMConditions_GetData = Class(name="HALL::FSMConditions::GetData")
FSMConditions_HALL_Data = Class(name="FSMConditions::HALL::Data")
HALL_FSMConditions_DomainPropertyGet = Class(name="HALL::FSMConditions::DomainPropertyGet")
HALL_FSMInstructions_Let = Class(name="HALL::FSMInstructions::Let")
HALL_FSMInstructions_DomainPropertyGet = Class(name="HALL::FSMInstructions::DomainPropertyGet")
HALL_FSMInstructions_VarRef = Class(name="HALL::FSMInstructions::VarRef")
FSMConditions_Let = Class(name="FSMConditions::Let")
HALL_FSMActions_Action = Class(name="HALL::FSMActions::Action")
FSMActions_ActionExpression = Class(name="FSMActions::ActionExpression")
HALL_FSMActions_ActionExpression = Class(name="HALL::FSMActions::ActionExpression")
HALL_FSMActions_Literal = Class(name="HALL::FSMActions::Literal")
ActionExpression = Class(name="ActionExpression")
HALL_FSMActions_DomainPropertyGet = Class(name="HALL::FSMActions::DomainPropertyGet")
HALL_FSMActions_Let = Class(name="HALL::FSMActions::Let")
HALL_FSMActions_MessageInvocation = Class(name="HALL::FSMActions::MessageInvocation")
HALL_FSMActions_Enable = Class(name="HALL::FSMActions::Enable")
HALL_FSMConditions_Let = Class(name="HALL::FSMConditions::Let")
HALL_FSMConditions_VarRef = Class(name="HALL::FSMConditions::VarRef")
HALL_FSMActions_BinaryOperator = Class(name="HALL::FSMActions::BinaryOperator")
HALL_FSMActions_UnaryOperator = Class(name="HALL::FSMActions::UnaryOperator")
HALL_FSMActions_VarRef = Class(name="HALL::FSMActions::VarRef")
FSMActions_Let = Class(name="FSMActions::Let")
HALL_Types_Type = Class(name="HALL::Types::Type", is_abstract=True)
HALL_Types_SimpleType = Class(name="HALL::Types::SimpleType", is_abstract=True)
Set = Class(name="Set")
HALL_Types_Set = Class(name="HALL::Types::Set")
HALL_FSMActions_DomainPropertySet = Class(name="HALL::FSMActions::DomainPropertySet")
HALL_FSMActions_GetData = Class(name="HALL::FSMActions::GetData")
FSMActions_HALL_Data = Class(name="FSMActions::HALL::Data")
SimpleType = Class(name="SimpleType")
HALL_Types_Boolean = Class(name="HALL::Types::Boolean")
HALL_Types_String = Class(name="HALL::Types::String")
HALL_Types_Number = Class(name="HALL::Types::Number")

# HALL_VisualObject class attributes and methods
HALL_VisualObject_vtype: Property = Property(name="vtype", type=StringType)
HALL_VisualObject.attributes={HALL_VisualObject_vtype}

# Component class attributes and methods

# ColorData class attributes and methods

# GeometryData class attributes and methods

# HALL_UserProfile class attributes and methods
HALL_UserProfile_numberofcompletedtasks: Property = Property(name="numberofcompletedtasks", type=IntegerType)
HALL_UserProfile.attributes={HALL_UserProfile_numberofcompletedtasks}

# HALL_Component class attributes and methods
HALL_Component_name: Property = Property(name="name", type=StringType)
HALL_Component.attributes={HALL_Component_name}

# HALL_Data class attributes and methods
HALL_Data_name: Property = Property(name="name", type=StringType)
HALL_Data_initValue: Property = Property(name="initValue", type=StringType)
HALL_Data_currentValue: Property = Property(name="currentValue", type=StringType)
HALL_Data.attributes={HALL_Data_currentValue, HALL_Data_name, HALL_Data_initValue}

# FSM class attributes and methods

# MessageHandler class attributes and methods

# HALL_SystemComponent class attributes and methods

# HALL_Model class attributes and methods

# HALL_Parameter class attributes and methods
HALL_Parameter_name: Property = Property(name="name", type=StringType)
HALL_Parameter.attributes={HALL_Parameter_name}

# MessageDefinition class attributes and methods

# Type class attributes and methods

# HALL_Geometry_Color class attributes and methods

# RGBColor class attributes and methods

# HALL_TaskObject class attributes and methods
HALL_TaskObject_completionTime: Property = Property(name="completionTime", type=IntegerType)
HALL_TaskObject_numberofgoalscompleted: Property = Property(name="numberofgoalscompleted", type=IntegerType)
HALL_TaskObject.attributes={HALL_TaskObject_completionTime, HALL_TaskObject_numberofgoalscompleted}

# HALL_Goal class attributes and methods
HALL_Goal_condition: Property = Property(name="condition", type=StringType)
HALL_Goal.attributes={HALL_Goal_condition}

# HALL_Geometry_ColorState class attributes and methods

# AlphaTransparency class attributes and methods

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

# ColorState class attributes and methods

# HALL_Geometry_RGBColor class attributes and methods
HALL_Geometry_RGBColor_redValue: Property = Property(name="redValue", type=IntegerType)
HALL_Geometry_RGBColor_greenValue: Property = Property(name="greenValue", type=IntegerType)
HALL_Geometry_RGBColor_blueValue: Property = Property(name="blueValue", type=IntegerType)
HALL_Geometry_RGBColor.attributes={HALL_Geometry_RGBColor_redValue, HALL_Geometry_RGBColor_blueValue, HALL_Geometry_RGBColor_greenValue}

# Color class attributes and methods

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

# HALL_Geometry_Point class attributes and methods
HALL_Geometry_Point_xCoord: Property = Property(name="xCoord", type=IntegerType)
HALL_Geometry_Point_yCoord: Property = Property(name="yCoord", type=IntegerType)
HALL_Geometry_Point.attributes={HALL_Geometry_Point_xCoord, HALL_Geometry_Point_yCoord}

# HALL_Messages_MessageTransition class attributes and methods
HALL_Messages_MessageTransition_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageTransition.attributes={HALL_Messages_MessageTransition_name}

# MessageState class attributes and methods

# Conditions_PreConditionMessage class attributes and methods

# Instructions_PosConditionMessage class attributes and methods

# HALL_Geometry_GeometryData class attributes and methods

# HALL_Geometry_GeometryData3D class attributes and methods

# Face class attributes and methods

# HALL_Geometry_GeometryData2D class attributes and methods
HALL_Geometry_GeometryData2D_labelText: Property = Property(name="labelText", type=StringType)
HALL_Geometry_GeometryData2D.attributes={HALL_Geometry_GeometryData2D_labelText}

# Point2D class attributes and methods

# Messages_HALL_Data class attributes and methods

# HALL_Messages_MessageHandler class attributes and methods

# RegularMessageState class attributes and methods

# InitialMessageState class attributes and methods

# Messages_HALL_Component class attributes and methods

# HALL_Messages_MessageState class attributes and methods
HALL_Messages_MessageState_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageState_isEnd: Property = Property(name="isEnd", type=BooleanType)
HALL_Messages_MessageState_isContinue: Property = Property(name="isContinue", type=BooleanType)
HALL_Messages_MessageState_isActive: Property = Property(name="isActive", type=BooleanType)
HALL_Messages_MessageState.attributes={HALL_Messages_MessageState_isContinue, HALL_Messages_MessageState_isActive, HALL_Messages_MessageState_name, HALL_Messages_MessageState_isEnd}

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

# Actions_ActionMessage class attributes and methods

# HALL_Messages_RegularMessageState class attributes and methods

# HALL_Messages_MessageDefinition class attributes and methods
HALL_Messages_MessageDefinition_name: Property = Property(name="name", type=StringType)
HALL_Messages_MessageDefinition.attributes={HALL_Messages_MessageDefinition_name}

# Messages_HALL_Model class attributes and methods

# Messages_HALL_Parameter class attributes and methods

# HALL_Instructions_UnaryOperator class attributes and methods
HALL_Instructions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Instructions_UnaryOperator.attributes={HALL_Instructions_UnaryOperator_operatorname}

# HALL_Instructions_GetData class attributes and methods

# Instructions_HALL_Data class attributes and methods

# HALL_Instructions_GetState class attributes and methods

# HALL_Instructions_SetMessageParameter class attributes and methods
HALL_Instructions_SetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Instructions_SetMessageParameter.attributes={HALL_Instructions_SetMessageParameter_field}

# HALL_Instructions_Let class attributes and methods
HALL_Instructions_Let_name: Property = Property(name="name", type=StringType)
HALL_Instructions_Let.attributes={HALL_Instructions_Let_name}

# HALL_Instructions_DomainPropertyGet class attributes and methods
HALL_Instructions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_Instructions_DomainPropertyGet.attributes={HALL_Instructions_DomainPropertyGet_name}

# HALL_Instructions_GetMessageData class attributes and methods
HALL_Instructions_GetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Instructions_GetMessageData.attributes={HALL_Instructions_GetMessageData_field}

# HALL_Instructions_GetMessageParameter class attributes and methods
HALL_Instructions_GetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Instructions_GetMessageParameter.attributes={HALL_Instructions_GetMessageParameter_field}

# Instructions_HALL_Component class attributes and methods

# HALL_Instructions_SetState class attributes and methods

# State class attributes and methods

# HALL_Instructions_SetData class attributes and methods

# HALL_Instructions_SetMessageData class attributes and methods
HALL_Instructions_SetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Instructions_SetMessageData.attributes={HALL_Instructions_SetMessageData_field}

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

# HALL_Conditions_UnaryOperator class attributes and methods
HALL_Conditions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Conditions_UnaryOperator.attributes={HALL_Conditions_UnaryOperator_operatorname}

# HALL_Instructions_SetTopDown class attributes and methods

# HALL_Instructions_VarRef class attributes and methods

# Instructions_Let class attributes and methods

# HALL_Conditions_PreConditionMessage class attributes and methods

# Conditions_PreConditionMessageExpression class attributes and methods

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

# HALL_Conditions_BinaryOperator class attributes and methods
HALL_Conditions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_Conditions_BinaryOperator.attributes={HALL_Conditions_BinaryOperator_operatorname}

# HALL_Conditions_VarRef class attributes and methods

# HALL_Actions_GetMessageData class attributes and methods
HALL_Actions_GetMessageData_field: Property = Property(name="field", type=StringType)
HALL_Actions_GetMessageData.attributes={HALL_Actions_GetMessageData_field}

# Conditions_Let class attributes and methods

# HALL_Actions_GetMessageParameter class attributes and methods
HALL_Actions_GetMessageParameter_field: Property = Property(name="field", type=StringType)
HALL_Actions_GetMessageParameter.attributes={HALL_Actions_GetMessageParameter_field}

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

# HALL_Actions_Let class attributes and methods

# HALL_Actions_DomainPropertyGet class attributes and methods
HALL_Actions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_Actions_DomainPropertyGet.attributes={HALL_Actions_DomainPropertyGet_name}

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

# HALL_Trigger_Trigger class attributes and methods

# Trigger_TriggerExpression class attributes and methods

# HALL_Actions_Enable class attributes and methods

# HALL_Trigger_TriggerExpression class attributes and methods

# HALL_Trigger_MessageNotification class attributes and methods

# TriggerExpression class attributes and methods

# HALL_FSM_FSM class attributes and methods

# FSM_HALL_Component class attributes and methods

# InitialState class attributes and methods

# RegularState class attributes and methods

# HALL_FSM_RegularState class attributes and methods

# HALL_FSMInstructions_UnaryOperator class attributes and methods
HALL_FSMInstructions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMInstructions_UnaryOperator.attributes={HALL_FSMInstructions_UnaryOperator_operatorname}

# HALL_FSMInstructions_GetData class attributes and methods
HALL_FSMInstructions_GetData_field: Property = Property(name="field", type=StringType)
HALL_FSMInstructions_GetData.attributes={HALL_FSMInstructions_GetData_field}

# FSMInstructions_HALL_Component class attributes and methods

# HALL_FSMInstructions_GetState class attributes and methods

# HALL_FSMInstructions_SetState class attributes and methods

# HALL_FSMInstructions_SetData class attributes and methods
HALL_FSMInstructions_SetData_field: Property = Property(name="field", type=StringType)
HALL_FSMInstructions_SetData.attributes={HALL_FSMInstructions_SetData_field}

# FSMInstructions_HALL_Data class attributes and methods

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

# HALL_FSMConditions_UnaryOperator class attributes and methods
HALL_FSMConditions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMConditions_UnaryOperator.attributes={HALL_FSMConditions_UnaryOperator_operatorname}

# HALL_FSMConditions_GetState class attributes and methods

# FSMConditions_HALL_Component class attributes and methods

# HALL_FSMConditions_GetData class attributes and methods

# FSMConditions_HALL_Data class attributes and methods

# HALL_FSMConditions_DomainPropertyGet class attributes and methods
HALL_FSMConditions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMConditions_DomainPropertyGet.attributes={HALL_FSMConditions_DomainPropertyGet_name}

# HALL_FSMInstructions_Let class attributes and methods
HALL_FSMInstructions_Let_name: Property = Property(name="name", type=StringType)
HALL_FSMInstructions_Let.attributes={HALL_FSMInstructions_Let_name}

# HALL_FSMInstructions_DomainPropertyGet class attributes and methods
HALL_FSMInstructions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMInstructions_DomainPropertyGet.attributes={HALL_FSMInstructions_DomainPropertyGet_name}

# HALL_FSMInstructions_VarRef class attributes and methods

# FSMConditions_Let class attributes and methods

# HALL_FSMActions_Action class attributes and methods

# FSMActions_ActionExpression class attributes and methods

# HALL_FSMActions_ActionExpression class attributes and methods

# HALL_FSMActions_Literal class attributes and methods
HALL_FSMActions_Literal_value: Property = Property(name="value", type=StringType)
HALL_FSMActions_Literal.attributes={HALL_FSMActions_Literal_value}

# ActionExpression class attributes and methods

# HALL_FSMActions_DomainPropertyGet class attributes and methods
HALL_FSMActions_DomainPropertyGet_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_DomainPropertyGet.attributes={HALL_FSMActions_DomainPropertyGet_name}

# HALL_FSMActions_Let class attributes and methods
HALL_FSMActions_Let_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_Let.attributes={HALL_FSMActions_Let_name}

# HALL_FSMActions_MessageInvocation class attributes and methods
HALL_FSMActions_MessageInvocation_isTopDown: Property = Property(name="isTopDown", type=BooleanType)
HALL_FSMActions_MessageInvocation.attributes={HALL_FSMActions_MessageInvocation_isTopDown}

# HALL_FSMActions_Enable class attributes and methods

# HALL_FSMConditions_Let class attributes and methods
HALL_FSMConditions_Let_name: Property = Property(name="name", type=StringType)
HALL_FSMConditions_Let.attributes={HALL_FSMConditions_Let_name}

# HALL_FSMConditions_VarRef class attributes and methods

# HALL_FSMActions_BinaryOperator class attributes and methods
HALL_FSMActions_BinaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMActions_BinaryOperator.attributes={HALL_FSMActions_BinaryOperator_operatorname}

# HALL_FSMActions_UnaryOperator class attributes and methods
HALL_FSMActions_UnaryOperator_operatorname: Property = Property(name="operatorname", type=StringType)
HALL_FSMActions_UnaryOperator.attributes={HALL_FSMActions_UnaryOperator_operatorname}

# HALL_FSMActions_VarRef class attributes and methods

# FSMActions_Let class attributes and methods

# HALL_Types_Type class attributes and methods
HALL_Types_Type_name: Property = Property(name="name", type=StringType)
HALL_Types_Type.attributes={HALL_Types_Type_name}

# HALL_Types_SimpleType class attributes and methods

# Set class attributes and methods

# HALL_Types_Set class attributes and methods

# HALL_FSMActions_DomainPropertySet class attributes and methods
HALL_FSMActions_DomainPropertySet_name: Property = Property(name="name", type=StringType)
HALL_FSMActions_DomainPropertySet.attributes={HALL_FSMActions_DomainPropertySet_name}

# HALL_FSMActions_GetData class attributes and methods

# FSMActions_HALL_Data class attributes and methods

# SimpleType class attributes and methods

# HALL_Types_Boolean class attributes and methods

# HALL_Types_String class attributes and methods

# HALL_Types_Number class attributes and methods

# Relationships
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
        Property(name="componentSetInv", type=HALL_VisualObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
componentSet45: BinaryAssociation = BinaryAssociation(
    name="componentSet45",
    ends={
        Property(name="TaskObject47", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv46", type=HALL_TaskObject, multiplicity=Multiplicity(0, 9999))
    }
)
messageHandlerSet12: BinaryAssociation = BinaryAssociation(
    name="messageHandlerSet12",
    ends={
        Property(name="Messages", type=HALL_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageHandler", type=MessageHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentSetInv49: BinaryAssociation = BinaryAssociation(
    name="componentSetInv49",
    ends={
        Property(name="TaskObject51", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet50", type=HALL_TaskObject, multiplicity=Multiplicity(0, 1))
    }
)
systemComponentInv13: BinaryAssociation = BinaryAssociation(
    name="systemComponentInv13",
    ends={
        Property(name="Model", type=HALL_SystemComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="systemComponent", type=HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
goalInv52: BinaryAssociation = BinaryAssociation(
    name="goalInv52",
    ends={
        Property(name="TaskObject53", type=HALL_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goal", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1))
    }
)
componentSet15: BinaryAssociation = BinaryAssociation(
    name="componentSet15",
    ends={
        Property(name="SystemComponent", type=HALL_SystemComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv16", type=HALL_SystemComponent, multiplicity=Multiplicity(0, 9999))
    }
)
componentSetInv18: BinaryAssociation = BinaryAssociation(
    name="componentSetInv18",
    ends={
        Property(name="SystemComponent20", type=HALL_SystemComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet19", type=HALL_SystemComponent, multiplicity=Multiplicity(0, 1))
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="Type55", type=HALL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Parameter", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
parameterInv56: BinaryAssociation = BinaryAssociation(
    name="parameterInv56",
    ends={
        Property(name="Messages58", type=HALL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageDefinition57", type=MessageDefinition, multiplicity=Multiplicity(0, 1))
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
type59: BinaryAssociation = BinaryAssociation(
    name="type59",
    ends={
        Property(name="Type60", type=HALL_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Data", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
messageDefinition25: BinaryAssociation = BinaryAssociation(
    name="messageDefinition25",
    ends={
        Property(name="Messages26", type=HALL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageDefinition", type=MessageDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInvMessageDefinition61: BinaryAssociation = BinaryAssociation(
    name="dataInvMessageDefinition61",
    ends={
        Property(name="Messages63", type=HALL_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageDefinition62", type=MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
typeDefinition27: BinaryAssociation = BinaryAssociation(
    name="typeDefinition27",
    ends={
        Property(name="Type", type=HALL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Model", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInvComponent64: BinaryAssociation = BinaryAssociation(
    name="dataInvComponent64",
    ends={
        Property(name="Component", type=HALL_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="data", type=HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
visualObject28: BinaryAssociation = BinaryAssociation(
    name="visualObject28",
    ends={
        Property(name="VisualObject29", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="visualObjectInv", type=HALL_VisualObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ambianceColor65: BinaryAssociation = BinaryAssociation(
    name="ambianceColor65",
    ends={
        Property(name="Geometry66", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="RGBColor", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
taskObject30: BinaryAssociation = BinaryAssociation(
    name="taskObject30",
    ends={
        Property(name="TaskObject", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="taskObjectInv", type=HALL_TaskObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userProfileInv31: BinaryAssociation = BinaryAssociation(
    name="userProfileInv31",
    ends={
        Property(name="Model32", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="userProfile", type=HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
componentSet34: BinaryAssociation = BinaryAssociation(
    name="componentSet34",
    ends={
        Property(name="UserProfile36", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSetInv35", type=HALL_UserProfile, multiplicity=Multiplicity(0, 9999))
    }
)
componentSetInv38: BinaryAssociation = BinaryAssociation(
    name="componentSetInv38",
    ends={
        Property(name="UserProfile40", type=HALL_UserProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="componentSet39", type=HALL_UserProfile, multiplicity=Multiplicity(0, 1))
    }
)
goal41: BinaryAssociation = BinaryAssociation(
    name="goal41",
    ends={
        Property(name="Goal", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="goalInv", type=HALL_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskObjectInv42: BinaryAssociation = BinaryAssociation(
    name="taskObjectInv42",
    ends={
        Property(name="UserProfile43", type=HALL_TaskObject, multiplicity=Multiplicity(1, 1)),
        Property(name="taskObject", type=HALL_UserProfile, multiplicity=Multiplicity(0, 1))
    }
)
foregroundColor86: BinaryAssociation = BinaryAssociation(
    name="foregroundColor86",
    ends={
        Property(name="Geometry88", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="Color87", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor89: BinaryAssociation = BinaryAssociation(
    name="backgroundColor89",
    ends={
        Property(name="Geometry91", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="Color90", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alphaTransparency92: BinaryAssociation = BinaryAssociation(
    name="alphaTransparency92",
    ends={
        Property(name="Geometry93", type=HALL_Geometry_ColorState, multiplicity=Multiplicity(1, 1)),
        Property(name="AlphaTransparency", type=AlphaTransparency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alphaTransparencyInv94: BinaryAssociation = BinaryAssociation(
    name="alphaTransparencyInv94",
    ends={
        Property(name="Geometry96", type=HALL_Geometry_AlphaTransparency, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorState95", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
normalColorsInv97: BinaryAssociation = BinaryAssociation(
    name="normalColorsInv97",
    ends={
        Property(name="Geometry99", type=HALL_Geometry_NormalColors, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorData98", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
selectedColorsInv100: BinaryAssociation = BinaryAssociation(
    name="selectedColorsInv100",
    ends={
        Property(name="Geometry102", type=HALL_Geometry_SelectedColors, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorData101", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
disabledColorsInv103: BinaryAssociation = BinaryAssociation(
    name="disabledColorsInv103",
    ends={
        Property(name="Geometry105", type=HALL_Geometry_DisabledColors, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorData104", type=ColorData, multiplicity=Multiplicity(0, 1))
    }
)
selectedColors106: BinaryAssociation = BinaryAssociation(
    name="selectedColors106",
    ends={
        Property(name="Geometry107", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="SelectedColors", type=SelectedColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
disabledColors108: BinaryAssociation = BinaryAssociation(
    name="disabledColors108",
    ends={
        Property(name="Geometry109", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="DisabledColors", type=DisabledColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
normalColors110: BinaryAssociation = BinaryAssociation(
    name="normalColors110",
    ends={
        Property(name="Geometry111", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="NormalColors", type=NormalColors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
difuseColor67: BinaryAssociation = BinaryAssociation(
    name="difuseColor67",
    ends={
        Property(name="Geometry69", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="RGBColor68", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specularColor70: BinaryAssociation = BinaryAssociation(
    name="specularColor70",
    ends={
        Property(name="Geometry72", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="RGBColor71", type=RGBColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colorDataInv112: BinaryAssociation = BinaryAssociation(
    name="colorDataInv112",
    ends={
        Property(name="VisualObject113", type=HALL_Geometry_ColorData, multiplicity=Multiplicity(1, 1)),
        Property(name="colorData", type=Geometry_HALL_VisualObject, multiplicity=Multiplicity(0, 1))
    }
)
foregroundColorInv73: BinaryAssociation = BinaryAssociation(
    name="foregroundColorInv73",
    ends={
        Property(name="Geometry74", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorState", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColorInv75: BinaryAssociation = BinaryAssociation(
    name="backgroundColorInv75",
    ends={
        Property(name="Geometry77", type=HALL_Geometry_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorState76", type=ColorState, multiplicity=Multiplicity(0, 1))
    }
)
ambianceColorInv78: BinaryAssociation = BinaryAssociation(
    name="ambianceColorInv78",
    ends={
        Property(name="Geometry79", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="Color", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
difuseColorInv80: BinaryAssociation = BinaryAssociation(
    name="difuseColorInv80",
    ends={
        Property(name="Geometry82", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="Color81", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
specularColorInv83: BinaryAssociation = BinaryAssociation(
    name="specularColorInv83",
    ends={
        Property(name="Geometry85", type=HALL_Geometry_RGBColor, multiplicity=Multiplicity(1, 1)),
        Property(name="Color84", type=Color, multiplicity=Multiplicity(0, 1))
    }
)
point3d120: BinaryAssociation = BinaryAssociation(
    name="point3d120",
    ends={
        Property(name="Geometry121", type=HALL_Geometry_Face, multiplicity=Multiplicity(1, 1)),
        Property(name="Point3D", type=Point3D, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
faceInv122: BinaryAssociation = BinaryAssociation(
    name="faceInv122",
    ends={
        Property(name="Geometry123", type=HALL_Geometry_Face, multiplicity=Multiplicity(1, 1)),
        Property(name="GeometryData3D", type=GeometryData3D, multiplicity=Multiplicity(0, 1))
    }
)
point2dInv124: BinaryAssociation = BinaryAssociation(
    name="point2dInv124",
    ends={
        Property(name="Geometry126", type=HALL_Geometry_Point3D, multiplicity=Multiplicity(1, 1)),
        Property(name="Face125", type=Face, multiplicity=Multiplicity(0, 1))
    }
)
point2dInv127: BinaryAssociation = BinaryAssociation(
    name="point2dInv127",
    ends={
        Property(name="Geometry128", type=HALL_Geometry_Point2D, multiplicity=Multiplicity(1, 1)),
        Property(name="GeometryData2D", type=GeometryData2D, multiplicity=Multiplicity(0, 1))
    }
)
transitionsInvMessageState129: BinaryAssociation = BinaryAssociation(
    name="transitionsInvMessageState129",
    ends={
        Property(name="Messages130", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageState", type=MessageState, multiplicity=Multiplicity(0, 1))
    }
)
stateRef131: BinaryAssociation = BinaryAssociation(
    name="stateRef131",
    ends={
        Property(name="MessageState132", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageTransition", type=MessageState, multiplicity=Multiplicity(1, 1))
    }
)
PreCondition133: BinaryAssociation = BinaryAssociation(
    name="PreCondition133",
    ends={
        Property(name="Conditions_PreConditionMessage", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageTransition134", type=Conditions_PreConditionMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PosCondition135: BinaryAssociation = BinaryAssociation(
    name="PosCondition135",
    ends={
        Property(name="Instructions_PosConditionMessage", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageTransition136", type=Instructions_PosConditionMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
geometryDataInv114: BinaryAssociation = BinaryAssociation(
    name="geometryDataInv114",
    ends={
        Property(name="VisualObject115", type=HALL_Geometry_GeometryData, multiplicity=Multiplicity(1, 1)),
        Property(name="geometryData", type=Geometry_HALL_VisualObject, multiplicity=Multiplicity(0, 1))
    }
)
face116: BinaryAssociation = BinaryAssociation(
    name="face116",
    ends={
        Property(name="Geometry117", type=HALL_Geometry_GeometryData3D, multiplicity=Multiplicity(1, 1)),
        Property(name="Face", type=Face, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
point2d118: BinaryAssociation = BinaryAssociation(
    name="point2d118",
    ends={
        Property(name="Geometry119", type=HALL_Geometry_GeometryData2D, multiplicity=Multiplicity(1, 1)),
        Property(name="Point2D", type=Point2D, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
data145: BinaryAssociation = BinaryAssociation(
    name="data145",
    ends={
        Property(name="Data146", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dataInvMessageDefinition", type=Messages_HALL_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message147: BinaryAssociation = BinaryAssociation(
    name="message147",
    ends={
        Property(name="MessageDefinition148", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageHandler", type=MessageDefinition, multiplicity=Multiplicity(1, 1))
    }
)
messageState149: BinaryAssociation = BinaryAssociation(
    name="messageState149",
    ends={
        Property(name="Messages150", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="RegularMessageState", type=RegularMessageState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialMessageState151: BinaryAssociation = BinaryAssociation(
    name="initialMessageState151",
    ends={
        Property(name="Messages152", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="InitialMessageState", type=InitialMessageState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageHandlerSetInv153: BinaryAssociation = BinaryAssociation(
    name="messageHandlerSetInv153",
    ends={
        Property(name="Component154", type=HALL_Messages_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="messageHandlerSet", type=Messages_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
transitions155: BinaryAssociation = BinaryAssociation(
    name="transitions155",
    ends={
        Property(name="Messages156", type=HALL_Messages_MessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageTransition", type=MessageTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialMessageStateInv157: BinaryAssociation = BinaryAssociation(
    name="initialMessageStateInv157",
    ends={
        Property(name="Messages159", type=HALL_Messages_InitialMessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageHandler158", type=MessageHandler, multiplicity=Multiplicity(0, 1))
    }
)
expression160: BinaryAssociation = BinaryAssociation(
    name="expression160",
    ends={
        Property(name="Instructions_PosConditionMessageExpression", type=HALL_Instructions_PosConditionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_PosConditionMessage", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ActionMessage137: BinaryAssociation = BinaryAssociation(
    name="ActionMessage137",
    ends={
        Property(name="Actions_ActionMessage", type=HALL_Messages_MessageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Messages_MessageTransition138", type=Actions_ActionMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageStateInv139: BinaryAssociation = BinaryAssociation(
    name="messageStateInv139",
    ends={
        Property(name="Messages141", type=HALL_Messages_RegularMessageState, multiplicity=Multiplicity(1, 1)),
        Property(name="MessageHandler140", type=MessageHandler, multiplicity=Multiplicity(0, 1))
    }
)
messageDefinitionInv142: BinaryAssociation = BinaryAssociation(
    name="messageDefinitionInv142",
    ends={
        Property(name="Model143", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition", type=Messages_HALL_Model, multiplicity=Multiplicity(0, 1))
    }
)
parameter144: BinaryAssociation = BinaryAssociation(
    name="parameter144",
    ends={
        Property(name="Parameter", type=HALL_Messages_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterInv", type=Messages_HALL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightexpression163: BinaryAssociation = BinaryAssociation(
    name="rightexpression163",
    ends={
        Property(name="Instructions_PosConditionMessageExpression165", type=HALL_Instructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_BinaryOperator164", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression166: BinaryAssociation = BinaryAssociation(
    name="expression166",
    ends={
        Property(name="Instructions_PosConditionMessageExpression167", type=HALL_Instructions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_UnaryOperator", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference168: BinaryAssociation = BinaryAssociation(
    name="reference168",
    ends={
        Property(name="Instructions_HALL_Data", type=HALL_Instructions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_GetData", type=Instructions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
leftexpression161: BinaryAssociation = BinaryAssociation(
    name="leftexpression161",
    ends={
        Property(name="Instructions_PosConditionMessageExpression162", type=HALL_Instructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_BinaryOperator", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value176: BinaryAssociation = BinaryAssociation(
    name="value176",
    ends={
        Property(name="Instructions_PosConditionMessageExpression177", type=HALL_Instructions_SetMessageData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetMessageData", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value178: BinaryAssociation = BinaryAssociation(
    name="value178",
    ends={
        Property(name="Instructions_PosConditionMessageExpression179", type=HALL_Instructions_SetMessageParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetMessageParameter", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in180: BinaryAssociation = BinaryAssociation(
    name="in180",
    ends={
        Property(name="Instructions_PosConditionMessageExpression181", type=HALL_Instructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_Let", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization182: BinaryAssociation = BinaryAssociation(
    name="initialization182",
    ends={
        Property(name="Instructions_PosConditionMessageExpression184", type=HALL_Instructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_Let183", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type185: BinaryAssociation = BinaryAssociation(
    name="type185",
    ends={
        Property(name="Type187", type=HALL_Instructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_Let186", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
reference169: BinaryAssociation = BinaryAssociation(
    name="reference169",
    ends={
        Property(name="Instructions_HALL_Component", type=HALL_Instructions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_GetState", type=Instructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
state170: BinaryAssociation = BinaryAssociation(
    name="state170",
    ends={
        Property(name="State", type=HALL_Instructions_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetState", type=State, multiplicity=Multiplicity(1, 1))
    }
)
value171: BinaryAssociation = BinaryAssociation(
    name="value171",
    ends={
        Property(name="Instructions_PosConditionMessageExpression172", type=HALL_Instructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetData", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference173: BinaryAssociation = BinaryAssociation(
    name="reference173",
    ends={
        Property(name="Instructions_HALL_Data175", type=HALL_Instructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetData174", type=Instructions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
reference192: BinaryAssociation = BinaryAssociation(
    name="reference192",
    ends={
        Property(name="Conditions_HALL_Component", type=HALL_Conditions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_GetState", type=Conditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference193: BinaryAssociation = BinaryAssociation(
    name="reference193",
    ends={
        Property(name="Conditions_HALL_Data", type=HALL_Conditions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_GetData", type=Conditions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
type194: BinaryAssociation = BinaryAssociation(
    name="type194",
    ends={
        Property(name="Type195", type=HALL_Conditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_Let", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
in196: BinaryAssociation = BinaryAssociation(
    name="in196",
    ends={
        Property(name="Conditions_PreConditionMessageExpression198", type=HALL_Conditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_Let197", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization199: BinaryAssociation = BinaryAssociation(
    name="initialization199",
    ends={
        Property(name="Conditions_PreConditionMessageExpression201", type=HALL_Conditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_Let200", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value188: BinaryAssociation = BinaryAssociation(
    name="value188",
    ends={
        Property(name="Instructions_PosConditionMessageExpression189", type=HALL_Instructions_SetTopDown, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_SetTopDown", type=Instructions_PosConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueof190: BinaryAssociation = BinaryAssociation(
    name="valueof190",
    ends={
        Property(name="Instructions_Let", type=HALL_Instructions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Instructions_VarRef", type=Instructions_Let, multiplicity=Multiplicity(1, 1))
    }
)
expression191: BinaryAssociation = BinaryAssociation(
    name="expression191",
    ends={
        Property(name="Conditions_PreConditionMessageExpression", type=HALL_Conditions_PreConditionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_PreConditionMessage", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression210: BinaryAssociation = BinaryAssociation(
    name="expression210",
    ends={
        Property(name="Actions_ActionMessageExpression", type=HALL_Actions_ActionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_ActionMessage", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueof211: BinaryAssociation = BinaryAssociation(
    name="valueof211",
    ends={
        Property(name="Actions_Let", type=HALL_Actions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_VarRef", type=Actions_Let, multiplicity=Multiplicity(1, 1))
    }
)
expression202: BinaryAssociation = BinaryAssociation(
    name="expression202",
    ends={
        Property(name="Conditions_PreConditionMessageExpression203", type=HALL_Conditions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_UnaryOperator", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftexpression204: BinaryAssociation = BinaryAssociation(
    name="leftexpression204",
    ends={
        Property(name="Conditions_PreConditionMessageExpression205", type=HALL_Conditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_BinaryOperator", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression206: BinaryAssociation = BinaryAssociation(
    name="rightexpression206",
    ends={
        Property(name="Conditions_PreConditionMessageExpression208", type=HALL_Conditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_BinaryOperator207", type=Conditions_PreConditionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueof209: BinaryAssociation = BinaryAssociation(
    name="valueof209",
    ends={
        Property(name="Conditions_Let", type=HALL_Conditions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Conditions_VarRef", type=Conditions_Let, multiplicity=Multiplicity(1, 1))
    }
)
message225: BinaryAssociation = BinaryAssociation(
    name="message225",
    ends={
        Property(name="MessageDefinition226", type=HALL_Actions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_MessageInvocation", type=MessageDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualset227: BinaryAssociation = BinaryAssociation(
    name="actualset227",
    ends={
        Property(name="Actions_ActionMessageExpression229", type=HALL_Actions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_MessageInvocation228", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression230: BinaryAssociation = BinaryAssociation(
    name="expression230",
    ends={
        Property(name="Actions_ActionMessageExpression231", type=HALL_Actions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_UnaryOperator", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference232: BinaryAssociation = BinaryAssociation(
    name="reference232",
    ends={
        Property(name="Actions_HALL_Component", type=HALL_Actions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_GetData", type=Actions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
leftexpression212: BinaryAssociation = BinaryAssociation(
    name="leftexpression212",
    ends={
        Property(name="Actions_ActionMessageExpression213", type=HALL_Actions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_BinaryOperator", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression214: BinaryAssociation = BinaryAssociation(
    name="rightexpression214",
    ends={
        Property(name="Actions_ActionMessageExpression216", type=HALL_Actions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_BinaryOperator215", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in217: BinaryAssociation = BinaryAssociation(
    name="in217",
    ends={
        Property(name="Actions_ActionMessageExpression218", type=HALL_Actions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Let", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization219: BinaryAssociation = BinaryAssociation(
    name="initialization219",
    ends={
        Property(name="Actions_ActionMessageExpression221", type=HALL_Actions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Let220", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type222: BinaryAssociation = BinaryAssociation(
    name="type222",
    ends={
        Property(name="Type224", type=HALL_Actions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Let223", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
source246: BinaryAssociation = BinaryAssociation(
    name="source246",
    ends={
        Property(name="FSM248", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="State247", type=State, multiplicity=Multiplicity(1, 1))
    }
)
stateRef249: BinaryAssociation = BinaryAssociation(
    name="stateRef249",
    ends={
        Property(name="State250", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition", type=State, multiplicity=Multiplicity(1, 1))
    }
)
PreCondition251: BinaryAssociation = BinaryAssociation(
    name="PreCondition251",
    ends={
        Property(name="FSMConditions_PreCondition", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition252", type=FSMConditions_PreCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PosCondition253: BinaryAssociation = BinaryAssociation(
    name="PosCondition253",
    ends={
        Property(name="FSMInstructions_PosCondition", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition254", type=FSMInstructions_PosCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Action255: BinaryAssociation = BinaryAssociation(
    name="Action255",
    ends={
        Property(name="FSMActions_Action", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition256", type=FSMActions_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Trigger257: BinaryAssociation = BinaryAssociation(
    name="Trigger257",
    ends={
        Property(name="Trigger_Trigger", type=HALL_FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_Transition258", type=Trigger_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions259: BinaryAssociation = BinaryAssociation(
    name="transitions259",
    ends={
        Property(name="FSM260", type=HALL_FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fsm261: BinaryAssociation = BinaryAssociation(
    name="fsm261",
    ends={
        Property(name="FSM262", type=HALL_FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_State", type=FSM, multiplicity=Multiplicity(0, 1))
    }
)
value233: BinaryAssociation = BinaryAssociation(
    name="value233",
    ends={
        Property(name="Actions_ActionMessageExpression234", type=HALL_Actions_DomainPropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_DomainPropertySet", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression263: BinaryAssociation = BinaryAssociation(
    name="expression263",
    ends={
        Property(name="Trigger_TriggerExpression", type=HALL_Trigger_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Trigger_Trigger", type=Trigger_TriggerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value235: BinaryAssociation = BinaryAssociation(
    name="value235",
    ends={
        Property(name="Actions_ActionMessageExpression236", type=HALL_Actions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Enable", type=Actions_ActionMessageExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference237: BinaryAssociation = BinaryAssociation(
    name="reference237",
    ends={
        Property(name="MessageDefinition239", type=HALL_Actions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Actions_Enable238", type=MessageDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FSMInv240: BinaryAssociation = BinaryAssociation(
    name="FSMInv240",
    ends={
        Property(name="Component242", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM241", type=FSM_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
initialState243: BinaryAssociation = BinaryAssociation(
    name="initialState243",
    ends={
        Property(name="InitialState", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_FSM", type=InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
state244: BinaryAssociation = BinaryAssociation(
    name="state244",
    ends={
        Property(name="RegularState", type=HALL_FSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSM_FSM245", type=RegularState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftexpression267: BinaryAssociation = BinaryAssociation(
    name="leftexpression267",
    ends={
        Property(name="FSMInstructions_PosConditionExpression268", type=HALL_FSMInstructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_BinaryOperator", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression269: BinaryAssociation = BinaryAssociation(
    name="rightexpression269",
    ends={
        Property(name="FSMInstructions_PosConditionExpression271", type=HALL_FSMInstructions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_BinaryOperator270", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression272: BinaryAssociation = BinaryAssociation(
    name="expression272",
    ends={
        Property(name="FSMInstructions_PosConditionExpression273", type=HALL_FSMInstructions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_UnaryOperator", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference274: BinaryAssociation = BinaryAssociation(
    name="reference274",
    ends={
        Property(name="FSMInstructions_HALL_Component", type=HALL_FSMInstructions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_GetData", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference275: BinaryAssociation = BinaryAssociation(
    name="reference275",
    ends={
        Property(name="FSMInstructions_HALL_Component276", type=HALL_FSMInstructions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_GetState", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference277: BinaryAssociation = BinaryAssociation(
    name="reference277",
    ends={
        Property(name="FSMInstructions_HALL_Component278", type=HALL_FSMInstructions_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetState", type=FSMInstructions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
state279: BinaryAssociation = BinaryAssociation(
    name="state279",
    ends={
        Property(name="State281", type=HALL_FSMInstructions_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetState280", type=State, multiplicity=Multiplicity(1, 1))
    }
)
value282: BinaryAssociation = BinaryAssociation(
    name="value282",
    ends={
        Property(name="FSMInstructions_PosConditionExpression283", type=HALL_FSMInstructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetData", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference284: BinaryAssociation = BinaryAssociation(
    name="reference284",
    ends={
        Property(name="FSMInstructions_HALL_Data", type=HALL_FSMInstructions_SetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_SetData285", type=FSMInstructions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
message264: BinaryAssociation = BinaryAssociation(
    name="message264",
    ends={
        Property(name="MessageDefinition265", type=HALL_Trigger_MessageNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_Trigger_MessageNotification", type=MessageDefinition, multiplicity=Multiplicity(1, 1))
    }
)
expression266: BinaryAssociation = BinaryAssociation(
    name="expression266",
    ends={
        Property(name="FSMInstructions_PosConditionExpression", type=HALL_FSMInstructions_PosCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_PosCondition", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueof294: BinaryAssociation = BinaryAssociation(
    name="valueof294",
    ends={
        Property(name="FSMInstructions_Let", type=HALL_FSMInstructions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_VarRef", type=FSMInstructions_Let, multiplicity=Multiplicity(1, 1))
    }
)
expression295: BinaryAssociation = BinaryAssociation(
    name="expression295",
    ends={
        Property(name="FSMConditions_PreConditionExpression", type=HALL_FSMConditions_PreCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_PreCondition", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftexpression296: BinaryAssociation = BinaryAssociation(
    name="leftexpression296",
    ends={
        Property(name="FSMConditions_PreConditionExpression297", type=HALL_FSMConditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_BinaryOperator", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression298: BinaryAssociation = BinaryAssociation(
    name="rightexpression298",
    ends={
        Property(name="FSMConditions_PreConditionExpression300", type=HALL_FSMConditions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_BinaryOperator299", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression301: BinaryAssociation = BinaryAssociation(
    name="expression301",
    ends={
        Property(name="FSMConditions_PreConditionExpression302", type=HALL_FSMConditions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_UnaryOperator", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference303: BinaryAssociation = BinaryAssociation(
    name="reference303",
    ends={
        Property(name="FSMConditions_HALL_Component", type=HALL_FSMConditions_GetState, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_GetState", type=FSMConditions_HALL_Component, multiplicity=Multiplicity(0, 1))
    }
)
reference304: BinaryAssociation = BinaryAssociation(
    name="reference304",
    ends={
        Property(name="FSMConditions_HALL_Data", type=HALL_FSMConditions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_GetData", type=FSMConditions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
in286: BinaryAssociation = BinaryAssociation(
    name="in286",
    ends={
        Property(name="FSMInstructions_PosConditionExpression287", type=HALL_FSMInstructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_Let", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization288: BinaryAssociation = BinaryAssociation(
    name="initialization288",
    ends={
        Property(name="FSMInstructions_PosConditionExpression290", type=HALL_FSMInstructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_Let289", type=FSMInstructions_PosConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type291: BinaryAssociation = BinaryAssociation(
    name="type291",
    ends={
        Property(name="Type293", type=HALL_FSMInstructions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMInstructions_Let292", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
valueof313: BinaryAssociation = BinaryAssociation(
    name="valueof313",
    ends={
        Property(name="FSMConditions_Let", type=HALL_FSMConditions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_VarRef", type=FSMConditions_Let, multiplicity=Multiplicity(1, 1))
    }
)
expression314: BinaryAssociation = BinaryAssociation(
    name="expression314",
    ends={
        Property(name="FSMActions_ActionExpression", type=HALL_FSMActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Action", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in315: BinaryAssociation = BinaryAssociation(
    name="in315",
    ends={
        Property(name="FSMActions_ActionExpression316", type=HALL_FSMActions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Let", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization317: BinaryAssociation = BinaryAssociation(
    name="initialization317",
    ends={
        Property(name="FSMActions_ActionExpression319", type=HALL_FSMActions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Let318", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type320: BinaryAssociation = BinaryAssociation(
    name="type320",
    ends={
        Property(name="Type322", type=HALL_FSMActions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Let321", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
message323: BinaryAssociation = BinaryAssociation(
    name="message323",
    ends={
        Property(name="MessageDefinition324", type=HALL_FSMActions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_MessageInvocation", type=MessageDefinition, multiplicity=Multiplicity(1, 1))
    }
)
actualset325: BinaryAssociation = BinaryAssociation(
    name="actualset325",
    ends={
        Property(name="FSMActions_ActionExpression327", type=HALL_FSMActions_MessageInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_MessageInvocation326", type=FSMActions_ActionExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialization305: BinaryAssociation = BinaryAssociation(
    name="initialization305",
    ends={
        Property(name="FSMConditions_PreConditionExpression306", type=HALL_FSMConditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_Let", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in307: BinaryAssociation = BinaryAssociation(
    name="in307",
    ends={
        Property(name="FSMConditions_PreConditionExpression309", type=HALL_FSMConditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_Let308", type=FSMConditions_PreConditionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type310: BinaryAssociation = BinaryAssociation(
    name="type310",
    ends={
        Property(name="Type312", type=HALL_FSMConditions_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMConditions_Let311", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
leftoperator336: BinaryAssociation = BinaryAssociation(
    name="leftoperator336",
    ends={
        Property(name="FSMActions_ActionExpression337", type=HALL_FSMActions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_BinaryOperator", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightexpression338: BinaryAssociation = BinaryAssociation(
    name="rightexpression338",
    ends={
        Property(name="FSMActions_ActionExpression340", type=HALL_FSMActions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_BinaryOperator339", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression341: BinaryAssociation = BinaryAssociation(
    name="expression341",
    ends={
        Property(name="FSMActions_ActionExpression342", type=HALL_FSMActions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_UnaryOperator", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueof343: BinaryAssociation = BinaryAssociation(
    name="valueof343",
    ends={
        Property(name="FSMActions_Let", type=HALL_FSMActions_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_VarRef", type=FSMActions_Let, multiplicity=Multiplicity(1, 1))
    }
)
elementsTypeInv344: BinaryAssociation = BinaryAssociation(
    name="elementsTypeInv344",
    ends={
        Property(name="Types", type=HALL_Types_SimpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="Set", type=Set, multiplicity=Multiplicity(0, 1))
    }
)
message328: BinaryAssociation = BinaryAssociation(
    name="message328",
    ends={
        Property(name="MessageDefinition329", type=HALL_FSMActions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Enable", type=MessageDefinition, multiplicity=Multiplicity(1, 1))
    }
)
value330: BinaryAssociation = BinaryAssociation(
    name="value330",
    ends={
        Property(name="FSMActions_ActionExpression332", type=HALL_FSMActions_Enable, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_Enable331", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value333: BinaryAssociation = BinaryAssociation(
    name="value333",
    ends={
        Property(name="FSMActions_ActionExpression334", type=HALL_FSMActions_DomainPropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_DomainPropertySet", type=FSMActions_ActionExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference335: BinaryAssociation = BinaryAssociation(
    name="reference335",
    ends={
        Property(name="FSMActions_HALL_Data", type=HALL_FSMActions_GetData, multiplicity=Multiplicity(1, 1)),
        Property(name="HALL_FSMActions_GetData", type=FSMActions_HALL_Data, multiplicity=Multiplicity(0, 1))
    }
)
elementsType345: BinaryAssociation = BinaryAssociation(
    name="elementsType345",
    ends={
        Property(name="Types346", type=HALL_Types_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleType", type=SimpleType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_HALL_VisualObject_Component = Generalization(general=Component, specific=HALL_VisualObject)
gen_HALL_SystemComponent_Component = Generalization(general=Component, specific=HALL_SystemComponent)
gen_HALL_UserProfile_Component = Generalization(general=Component, specific=HALL_UserProfile)
gen_HALL_TaskObject_Component = Generalization(general=Component, specific=HALL_TaskObject)
gen_HALL_Geometry_NormalColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_NormalColors)
gen_HALL_Geometry_SelectedColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_SelectedColors)
gen_HALL_Geometry_DisabledColors_ColorState = Generalization(general=ColorState, specific=HALL_Geometry_DisabledColors)
gen_HALL_Geometry_Point3D_Point = Generalization(general=Point, specific=HALL_Geometry_Point3D)
gen_HALL_Geometry_Point2D_Point = Generalization(general=Point, specific=HALL_Geometry_Point2D)
gen_HALL_Geometry_GeometryData3D_GeometryData = Generalization(general=GeometryData, specific=HALL_Geometry_GeometryData3D)
gen_HALL_Geometry_GeometryData2D_GeometryData = Generalization(general=GeometryData, specific=HALL_Geometry_GeometryData2D)
gen_HALL_Messages_InitialMessageState_MessageState = Generalization(general=MessageState, specific=HALL_Messages_InitialMessageState)
gen_HALL_Instructions_Literal_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_Literal)
gen_HALL_Instructions_BinaryOperator_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_BinaryOperator)
gen_HALL_Messages_RegularMessageState_MessageState = Generalization(general=MessageState, specific=HALL_Messages_RegularMessageState)
gen_HALL_Instructions_UnaryOperator_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_UnaryOperator)
gen_HALL_Instructions_GetData_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_GetData)
gen_HALL_Instructions_SetMessageParameter_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_SetMessageParameter)
gen_HALL_Instructions_Let_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_Let)
gen_HALL_Instructions_DomainPropertyGet_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_DomainPropertyGet)
gen_HALL_Instructions_GetMessageData_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_GetMessageData)
gen_HALL_Instructions_GetState_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_GetState)
gen_HALL_Instructions_GetMessageParameter_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_GetMessageParameter)
gen_HALL_Instructions_SetState_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_SetState)
gen_HALL_Instructions_SetData_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_SetData)
gen_HALL_Instructions_SetMessageData_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_SetMessageData)
gen_HALL_Conditions_Literal_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_Literal)
gen_HALL_Conditions_GetMessageData_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_GetMessageData)
gen_HALL_Conditions_GetMessageParameter_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_GetMessageParameter)
gen_HALL_Conditions_DomainPropertyGet_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_DomainPropertyGet)
gen_HALL_Conditions_GetState_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_GetState)
gen_HALL_Conditions_GetData_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_GetData)
gen_HALL_Conditions_Let_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_Let)
gen_HALL_Conditions_UnaryOperator_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_UnaryOperator)
gen_HALL_Instructions_SetTopDown_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_SetTopDown)
gen_HALL_Instructions_VarRef_PosConditionMessageExpression = Generalization(general=PosConditionMessageExpression, specific=HALL_Instructions_VarRef)
gen_HALL_Actions_VarRef_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_VarRef)
gen_HALL_Actions_Literal_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_Literal)
gen_HALL_Actions_BinaryOperator_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_BinaryOperator)
gen_HALL_Conditions_BinaryOperator_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_BinaryOperator)
gen_HALL_Conditions_VarRef_PreConditionMessageExpression = Generalization(general=PreConditionMessageExpression, specific=HALL_Conditions_VarRef)
gen_HALL_Actions_GetMessageData_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_GetMessageData)
gen_HALL_Actions_GetMessageParameter_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_GetMessageParameter)
gen_HALL_Actions_MessageInvocation_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_MessageInvocation)
gen_HALL_Actions_UnaryOperator_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_UnaryOperator)
gen_HALL_Actions_GetData_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_GetData)
gen_HALL_Actions_DomainPropertySet_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_DomainPropertySet)
gen_HALL_Actions_Let_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_Let)
gen_HALL_Actions_DomainPropertyGet_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_DomainPropertyGet)
gen_HALL_FSM_RegularState_State = Generalization(general=State, specific=HALL_FSM_RegularState)
gen_HALL_FSM_InitialState_State = Generalization(general=State, specific=HALL_FSM_InitialState)
gen_HALL_Actions_Enable_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_Actions_Enable)
gen_HALL_Trigger_MessageNotification_TriggerExpression = Generalization(general=TriggerExpression, specific=HALL_Trigger_MessageNotification)
gen_HALL_FSMInstructions_BinaryOperator_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_BinaryOperator)
gen_HALL_FSMInstructions_UnaryOperator_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_UnaryOperator)
gen_HALL_FSMInstructions_GetData_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_GetData)
gen_HALL_FSMInstructions_GetState_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_GetState)
gen_HALL_FSMInstructions_SetState_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_SetState)
gen_HALL_FSMInstructions_SetData_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_SetData)
gen_HALL_Trigger_DomainEventFired_TriggerExpression = Generalization(general=TriggerExpression, specific=HALL_Trigger_DomainEventFired)
gen_HALL_FSMInstructions_Literal_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_Literal)
gen_HALL_FSMInstructions_VarRef_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_VarRef)
gen_HALL_FSMConditions_Literal_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_Literal)
gen_HALL_FSMConditions_BinaryOperator_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_BinaryOperator)
gen_HALL_FSMConditions_UnaryOperator_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_UnaryOperator)
gen_HALL_FSMConditions_GetState_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_GetState)
gen_HALL_FSMConditions_GetData_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_GetData)
gen_HALL_FSMConditions_DomainPropertyGet_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_DomainPropertyGet)
gen_HALL_FSMInstructions_Let_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_Let)
gen_HALL_FSMInstructions_DomainPropertyGet_PosConditionExpression = Generalization(general=PosConditionExpression, specific=HALL_FSMInstructions_DomainPropertyGet)
gen_HALL_FSMActions_Literal_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_Literal)
gen_HALL_FSMActions_DomainPropertyGet_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_DomainPropertyGet)
gen_HALL_FSMActions_Let_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_Let)
gen_HALL_FSMActions_MessageInvocation_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_MessageInvocation)
gen_HALL_FSMActions_Enable_ActionMessageExpression = Generalization(general=ActionMessageExpression, specific=HALL_FSMActions_Enable)
gen_HALL_FSMConditions_Let_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_Let)
gen_HALL_FSMConditions_VarRef_PreConditionExpression = Generalization(general=PreConditionExpression, specific=HALL_FSMConditions_VarRef)
gen_HALL_FSMActions_BinaryOperator_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_BinaryOperator)
gen_HALL_FSMActions_UnaryOperator_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_UnaryOperator)
gen_HALL_FSMActions_VarRef_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_VarRef)
gen_HALL_Types_SimpleType_Type = Generalization(general=Type, specific=HALL_Types_SimpleType)
gen_HALL_Types_Set_Type = Generalization(general=Type, specific=HALL_Types_Set)
gen_HALL_FSMActions_DomainPropertySet_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_DomainPropertySet)
gen_HALL_FSMActions_GetData_ActionExpression = Generalization(general=ActionExpression, specific=HALL_FSMActions_GetData)
gen_HALL_Types_Boolean_SimpleType = Generalization(general=SimpleType, specific=HALL_Types_Boolean)
gen_HALL_Types_String_SimpleType = Generalization(general=SimpleType, specific=HALL_Types_String)
gen_HALL_Types_Number_SimpleType = Generalization(general=SimpleType, specific=HALL_Types_Number)

# Domain Model
domain_model = DomainModel(
    name="HALL",
    types={HALL_VisualObject, Component, ColorData, GeometryData, HALL_UserProfile, HALL_Component, HALL_Data, FSM, MessageHandler, HALL_SystemComponent, HALL_Model, HALL_Parameter, MessageDefinition, Type, HALL_Geometry_Color, RGBColor, HALL_TaskObject, HALL_Goal, HALL_Geometry_ColorState, AlphaTransparency, HALL_Geometry_AlphaTransparency, HALL_Geometry_NormalColors, HALL_Geometry_SelectedColors, HALL_Geometry_DisabledColors, HALL_Geometry_ColorData, SelectedColors, DisabledColors, NormalColors, Geometry_HALL_VisualObject, ColorState, HALL_Geometry_RGBColor, Color, HALL_Geometry_Face, Point3D, GeometryData3D, HALL_Geometry_Point3D, Point, HALL_Geometry_Point2D, GeometryData2D, HALL_Geometry_Point, HALL_Messages_MessageTransition, MessageState, Conditions_PreConditionMessage, Instructions_PosConditionMessage, HALL_Geometry_GeometryData, HALL_Geometry_GeometryData3D, Face, HALL_Geometry_GeometryData2D, Point2D, Messages_HALL_Data, HALL_Messages_MessageHandler, RegularMessageState, InitialMessageState, Messages_HALL_Component, HALL_Messages_MessageState, MessageTransition, HALL_Messages_InitialMessageState, HALL_Instructions_PosConditionMessage, Instructions_PosConditionMessageExpression, HALL_Instructions_PosConditionMessageExpression, HALL_Instructions_Literal, PosConditionMessageExpression, HALL_Instructions_BinaryOperator, Actions_ActionMessage, HALL_Messages_RegularMessageState, HALL_Messages_MessageDefinition, Messages_HALL_Model, Messages_HALL_Parameter, HALL_Instructions_UnaryOperator, HALL_Instructions_GetData, Instructions_HALL_Data, HALL_Instructions_GetState, HALL_Instructions_SetMessageParameter, HALL_Instructions_Let, HALL_Instructions_DomainPropertyGet, HALL_Instructions_GetMessageData, HALL_Instructions_GetMessageParameter, Instructions_HALL_Component, HALL_Instructions_SetState, State, HALL_Instructions_SetData, HALL_Instructions_SetMessageData, HALL_Conditions_PreConditionMessageExpression, HALL_Conditions_Literal, PreConditionMessageExpression, HALL_Conditions_GetMessageData, HALL_Conditions_GetMessageParameter, HALL_Conditions_DomainPropertyGet, HALL_Conditions_GetState, Conditions_HALL_Component, HALL_Conditions_GetData, Conditions_HALL_Data, HALL_Conditions_Let, HALL_Conditions_UnaryOperator, HALL_Instructions_SetTopDown, HALL_Instructions_VarRef, Instructions_Let, HALL_Conditions_PreConditionMessage, Conditions_PreConditionMessageExpression, HALL_Actions_ActionMessage, Actions_ActionMessageExpression, HALL_Actions_ActionMessageExpression, HALL_Actions_VarRef, ActionMessageExpression, Actions_Let, HALL_Actions_Literal, HALL_Actions_BinaryOperator, HALL_Conditions_BinaryOperator, HALL_Conditions_VarRef, HALL_Actions_GetMessageData, Conditions_Let, HALL_Actions_GetMessageParameter, HALL_Actions_MessageInvocation, HALL_Actions_UnaryOperator, HALL_Actions_GetData, Actions_HALL_Component, HALL_Actions_DomainPropertySet, HALL_Actions_Let, HALL_Actions_DomainPropertyGet, HALL_FSM_InitialState, HALL_FSM_Transition, FSMConditions_PreCondition, FSMInstructions_PosCondition, FSMActions_Action, Trigger_Trigger, HALL_FSM_State, Transition, HALL_Trigger_Trigger, Trigger_TriggerExpression, HALL_Actions_Enable, HALL_Trigger_TriggerExpression, HALL_Trigger_MessageNotification, TriggerExpression, HALL_FSM_FSM, FSM_HALL_Component, InitialState, RegularState, HALL_FSM_RegularState, HALL_FSMInstructions_UnaryOperator, HALL_FSMInstructions_GetData, FSMInstructions_HALL_Component, HALL_FSMInstructions_GetState, HALL_FSMInstructions_SetState, HALL_FSMInstructions_SetData, FSMInstructions_HALL_Data, HALL_Trigger_DomainEventFired, HALL_FSMInstructions_PosCondition, FSMInstructions_PosConditionExpression, HALL_FSMInstructions_PosConditionExpression, HALL_FSMInstructions_Literal, PosConditionExpression, HALL_FSMInstructions_BinaryOperator, FSMInstructions_Let, HALL_FSMConditions_PreCondition, FSMConditions_PreConditionExpression, HALL_FSMConditions_PreConditionExpression, HALL_FSMConditions_Literal, PreConditionExpression, HALL_FSMConditions_BinaryOperator, HALL_FSMConditions_UnaryOperator, HALL_FSMConditions_GetState, FSMConditions_HALL_Component, HALL_FSMConditions_GetData, FSMConditions_HALL_Data, HALL_FSMConditions_DomainPropertyGet, HALL_FSMInstructions_Let, HALL_FSMInstructions_DomainPropertyGet, HALL_FSMInstructions_VarRef, FSMConditions_Let, HALL_FSMActions_Action, FSMActions_ActionExpression, HALL_FSMActions_ActionExpression, HALL_FSMActions_Literal, ActionExpression, HALL_FSMActions_DomainPropertyGet, HALL_FSMActions_Let, HALL_FSMActions_MessageInvocation, HALL_FSMActions_Enable, HALL_FSMConditions_Let, HALL_FSMConditions_VarRef, HALL_FSMActions_BinaryOperator, HALL_FSMActions_UnaryOperator, HALL_FSMActions_VarRef, FSMActions_Let, HALL_Types_Type, HALL_Types_SimpleType, Set, HALL_Types_Set, HALL_FSMActions_DomainPropertySet, HALL_FSMActions_GetData, FSMActions_HALL_Data, SimpleType, HALL_Types_Boolean, HALL_Types_String, HALL_Types_Number},
    associations={colorData0, geometryData1, visualObjectInv3, componentSet5, componentSetInv7, data9, FSM10, componentSet45, messageHandlerSet12, componentSetInv49, systemComponentInv13, goalInv52, componentSet15, componentSetInv18, type54, parameterInv56, userProfile21, systemComponent23, type59, messageDefinition25, dataInvMessageDefinition61, typeDefinition27, dataInvComponent64, visualObject28, ambianceColor65, taskObject30, userProfileInv31, componentSet34, componentSetInv38, goal41, taskObjectInv42, foregroundColor86, backgroundColor89, alphaTransparency92, alphaTransparencyInv94, normalColorsInv97, selectedColorsInv100, disabledColorsInv103, selectedColors106, disabledColors108, normalColors110, difuseColor67, specularColor70, colorDataInv112, foregroundColorInv73, backgroundColorInv75, ambianceColorInv78, difuseColorInv80, specularColorInv83, point3d120, faceInv122, point2dInv124, point2dInv127, transitionsInvMessageState129, stateRef131, PreCondition133, PosCondition135, geometryDataInv114, face116, point2d118, data145, message147, messageState149, initialMessageState151, messageHandlerSetInv153, transitions155, initialMessageStateInv157, expression160, ActionMessage137, messageStateInv139, messageDefinitionInv142, parameter144, rightexpression163, expression166, reference168, leftexpression161, value176, value178, in180, initialization182, type185, reference169, state170, value171, reference173, reference192, reference193, type194, in196, initialization199, value188, valueof190, expression191, expression210, valueof211, expression202, leftexpression204, rightexpression206, valueof209, message225, actualset227, expression230, reference232, leftexpression212, rightexpression214, in217, initialization219, type222, source246, stateRef249, PreCondition251, PosCondition253, Action255, Trigger257, transitions259, fsm261, value233, expression263, value235, reference237, FSMInv240, initialState243, state244, leftexpression267, rightexpression269, expression272, reference274, reference275, reference277, state279, value282, reference284, message264, expression266, valueof294, expression295, leftexpression296, rightexpression298, expression301, reference303, reference304, in286, initialization288, type291, valueof313, expression314, in315, initialization317, type320, message323, actualset325, initialization305, in307, type310, leftoperator336, rightexpression338, expression341, valueof343, elementsTypeInv344, message328, value330, value333, reference335, elementsType345},
    generalizations={gen_HALL_VisualObject_Component, gen_HALL_SystemComponent_Component, gen_HALL_UserProfile_Component, gen_HALL_TaskObject_Component, gen_HALL_Geometry_NormalColors_ColorState, gen_HALL_Geometry_SelectedColors_ColorState, gen_HALL_Geometry_DisabledColors_ColorState, gen_HALL_Geometry_Point3D_Point, gen_HALL_Geometry_Point2D_Point, gen_HALL_Geometry_GeometryData3D_GeometryData, gen_HALL_Geometry_GeometryData2D_GeometryData, gen_HALL_Messages_InitialMessageState_MessageState, gen_HALL_Instructions_Literal_PosConditionMessageExpression, gen_HALL_Instructions_BinaryOperator_PosConditionMessageExpression, gen_HALL_Messages_RegularMessageState_MessageState, gen_HALL_Instructions_UnaryOperator_PosConditionMessageExpression, gen_HALL_Instructions_GetData_PosConditionMessageExpression, gen_HALL_Instructions_SetMessageParameter_PosConditionMessageExpression, gen_HALL_Instructions_Let_PosConditionMessageExpression, gen_HALL_Instructions_DomainPropertyGet_PosConditionMessageExpression, gen_HALL_Instructions_GetMessageData_PosConditionMessageExpression, gen_HALL_Instructions_GetState_PosConditionMessageExpression, gen_HALL_Instructions_GetMessageParameter_PosConditionMessageExpression, gen_HALL_Instructions_SetState_PosConditionMessageExpression, gen_HALL_Instructions_SetData_PosConditionMessageExpression, gen_HALL_Instructions_SetMessageData_PosConditionMessageExpression, gen_HALL_Conditions_Literal_PreConditionMessageExpression, gen_HALL_Conditions_GetMessageData_PreConditionMessageExpression, gen_HALL_Conditions_GetMessageParameter_PreConditionMessageExpression, gen_HALL_Conditions_DomainPropertyGet_PreConditionMessageExpression, gen_HALL_Conditions_GetState_PreConditionMessageExpression, gen_HALL_Conditions_GetData_PreConditionMessageExpression, gen_HALL_Conditions_Let_PreConditionMessageExpression, gen_HALL_Conditions_UnaryOperator_PreConditionMessageExpression, gen_HALL_Instructions_SetTopDown_PosConditionMessageExpression, gen_HALL_Instructions_VarRef_PosConditionMessageExpression, gen_HALL_Actions_VarRef_ActionMessageExpression, gen_HALL_Actions_Literal_ActionMessageExpression, gen_HALL_Actions_BinaryOperator_ActionMessageExpression, gen_HALL_Conditions_BinaryOperator_PreConditionMessageExpression, gen_HALL_Conditions_VarRef_PreConditionMessageExpression, gen_HALL_Actions_GetMessageData_ActionMessageExpression, gen_HALL_Actions_GetMessageParameter_ActionMessageExpression, gen_HALL_Actions_MessageInvocation_ActionMessageExpression, gen_HALL_Actions_UnaryOperator_ActionMessageExpression, gen_HALL_Actions_GetData_ActionMessageExpression, gen_HALL_Actions_DomainPropertySet_ActionMessageExpression, gen_HALL_Actions_Let_ActionMessageExpression, gen_HALL_Actions_DomainPropertyGet_ActionMessageExpression, gen_HALL_FSM_RegularState_State, gen_HALL_FSM_InitialState_State, gen_HALL_Actions_Enable_ActionMessageExpression, gen_HALL_Trigger_MessageNotification_TriggerExpression, gen_HALL_FSMInstructions_BinaryOperator_PosConditionExpression, gen_HALL_FSMInstructions_UnaryOperator_PosConditionExpression, gen_HALL_FSMInstructions_GetData_PosConditionExpression, gen_HALL_FSMInstructions_GetState_PosConditionExpression, gen_HALL_FSMInstructions_SetState_PosConditionExpression, gen_HALL_FSMInstructions_SetData_PosConditionExpression, gen_HALL_Trigger_DomainEventFired_TriggerExpression, gen_HALL_FSMInstructions_Literal_PosConditionExpression, gen_HALL_FSMInstructions_VarRef_PosConditionExpression, gen_HALL_FSMConditions_Literal_PreConditionExpression, gen_HALL_FSMConditions_BinaryOperator_PreConditionExpression, gen_HALL_FSMConditions_UnaryOperator_PreConditionExpression, gen_HALL_FSMConditions_GetState_PreConditionExpression, gen_HALL_FSMConditions_GetData_PreConditionExpression, gen_HALL_FSMConditions_DomainPropertyGet_PreConditionExpression, gen_HALL_FSMInstructions_Let_PosConditionExpression, gen_HALL_FSMInstructions_DomainPropertyGet_PosConditionExpression, gen_HALL_FSMActions_Literal_ActionExpression, gen_HALL_FSMActions_DomainPropertyGet_ActionExpression, gen_HALL_FSMActions_Let_ActionExpression, gen_HALL_FSMActions_MessageInvocation_ActionExpression, gen_HALL_FSMActions_Enable_ActionMessageExpression, gen_HALL_FSMConditions_Let_PreConditionExpression, gen_HALL_FSMConditions_VarRef_PreConditionExpression, gen_HALL_FSMActions_BinaryOperator_ActionExpression, gen_HALL_FSMActions_UnaryOperator_ActionExpression, gen_HALL_FSMActions_VarRef_ActionExpression, gen_HALL_Types_SimpleType_Type, gen_HALL_Types_Set_Type, gen_HALL_FSMActions_DomainPropertySet_ActionExpression, gen_HALL_FSMActions_GetData_ActionExpression, gen_HALL_Types_Boolean_SimpleType, gen_HALL_Types_String_SimpleType, gen_HALL_Types_Number_SimpleType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)