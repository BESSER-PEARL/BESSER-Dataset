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
Device: Enumeration = Enumeration(
    name="Device",
    literals={
            EnumerationLiteral(name="iphone"),
			EnumerationLiteral(name="ipad"),
			EnumerationLiteral(name="android4"),
			EnumerationLiteral(name="android2")
    }
)

# Classes
appBuilderDSL_AppBuilder = Class(name="appBuilderDSL::AppBuilder")
appBuilderDSL_AbstractElement = Class(name="appBuilderDSL::AbstractElement")
appBuilderDSL_NamespaceDeclation = Class(name="appBuilderDSL::NamespaceDeclation")
AbstractElement = Class(name="AbstractElement")
appBuilderDSL_System = Class(name="appBuilderDSL::System")
appBuilderDSL_Business = Class(name="appBuilderDSL::Business")
appBuilderDSL_Ui = Class(name="appBuilderDSL::Ui")
appBuilderDSL_Service = Class(name="appBuilderDSL::Service")
appBuilderDSL_InstanceService = Class(name="appBuilderDSL::InstanceService")
Service = Class(name="Service")
appBuilderDSL_Main = Class(name="appBuilderDSL::Main")
appBuilderDSL_Screen = Class(name="appBuilderDSL::Screen")
appBuilderDSL_SimpleScreen = Class(name="appBuilderDSL::SimpleScreen")
Screen = Class(name="Screen")
appBuilderDSL_EntryParameters = Class(name="appBuilderDSL::EntryParameters")
appBuilderDSL_Model = Class(name="appBuilderDSL::Model")
appBuilderDSL_View = Class(name="appBuilderDSL::View")
appBuilderDSL_Controller = Class(name="appBuilderDSL::Controller")
appBuilderDSL_Attribute = Class(name="appBuilderDSL::Attribute")
appBuilderDSL_InitAction = Class(name="appBuilderDSL::InitAction")
appBuilderDSL_Validator = Class(name="appBuilderDSL::Validator")
appBuilderDSL_Action = Class(name="appBuilderDSL::Action")
appBuilderDSL_DataBinding = Class(name="appBuilderDSL::DataBinding")
appBuilderDSL_UiListenerBinding = Class(name="appBuilderDSL::UiListenerBinding")
appBuilderDSL_ValidationBinding = Class(name="appBuilderDSL::ValidationBinding")
appBuilderDSL_Instruction = Class(name="appBuilderDSL::Instruction")
appBuilderDSL_Condition = Class(name="appBuilderDSL::Condition")
appBuilderDSL_Control = Class(name="appBuilderDSL::Control")
appBuilderDSL_SimpleDataBinding = Class(name="appBuilderDSL::SimpleDataBinding")
DataBinding = Class(name="DataBinding")
appBuilderDSL_EnumDataBinding = Class(name="appBuilderDSL::EnumDataBinding")
appBuilderDSL_ConditionExpression = Class(name="appBuilderDSL::ConditionExpression")
appBuilderDSL_SimpleConditionExpression = Class(name="appBuilderDSL::SimpleConditionExpression")
ConditionExpression = Class(name="ConditionExpression")
appBuilderDSL_CompositeConditionExpression = Class(name="appBuilderDSL::CompositeConditionExpression")
appBuilderDSL_UiAction = Class(name="appBuilderDSL::UiAction")
Action = Class(name="Action")
appBuilderDSL_SetInstruction = Class(name="appBuilderDSL::SetInstruction")
Instruction = Class(name="Instruction")
appBuilderDSL_SetInstructionAssignment = Class(name="appBuilderDSL::SetInstructionAssignment")
appBuilderDSL_Navigate = Class(name="appBuilderDSL::Navigate")
appBuilderDSL_ExecuteAction = Class(name="appBuilderDSL::ExecuteAction")
appBuilderDSL_RestCall = Class(name="appBuilderDSL::RestCall")
SetInstructionAssignment = Class(name="SetInstructionAssignment")
appBuilderDSL_ControlValue = Class(name="appBuilderDSL::ControlValue")
appBuilderDSL_List = Class(name="appBuilderDSL::List")
appBuilderDSL_Layout = Class(name="appBuilderDSL::Layout")
Control = Class(name="Control")
appBuilderDSL_GridLayout = Class(name="appBuilderDSL::GridLayout")
Layout = Class(name="Layout")
appBuilderDSL_RowLayout = Class(name="appBuilderDSL::RowLayout")
appBuilderDSL_ScreenLayout = Class(name="appBuilderDSL::ScreenLayout")
appBuilderDSL_Value = Class(name="appBuilderDSL::Value")
appBuilderDSL_DynamicValue = Class(name="appBuilderDSL::DynamicValue")
Value = Class(name="Value")
appBuilderDSL_Expression = Class(name="appBuilderDSL::Expression")
appBuilderDSL_Text = Class(name="appBuilderDSL::Text")
appBuilderDSL_Button = Class(name="appBuilderDSL::Button")
appBuilderDSL_Label = Class(name="appBuilderDSL::Label")
appBuilderDSL_CompositeScreen = Class(name="appBuilderDSL::CompositeScreen")
appBuilderDSL_Import = Class(name="appBuilderDSL::Import")
appBuilderDSL_Type = Class(name="appBuilderDSL::Type")
appBuilderDSL_DataType = Class(name="appBuilderDSL::DataType")
Type = Class(name="Type")
appBuilderDSL_Entity = Class(name="appBuilderDSL::Entity")
appBuilderDSL_Feature = Class(name="appBuilderDSL::Feature")

# appBuilderDSL_AppBuilder class attributes and methods

# appBuilderDSL_AbstractElement class attributes and methods
appBuilderDSL_AbstractElement_name: Property = Property(name="name", type=StringType)
appBuilderDSL_AbstractElement.attributes={appBuilderDSL_AbstractElement_name}

# appBuilderDSL_NamespaceDeclation class attributes and methods

# AbstractElement class attributes and methods

# appBuilderDSL_System class attributes and methods

# appBuilderDSL_Business class attributes and methods

# appBuilderDSL_Ui class attributes and methods

# appBuilderDSL_Service class attributes and methods

# appBuilderDSL_InstanceService class attributes and methods
appBuilderDSL_InstanceService_instanceName: Property = Property(name="instanceName", type=StringType)
appBuilderDSL_InstanceService.attributes={appBuilderDSL_InstanceService_instanceName}

# Service class attributes and methods

# appBuilderDSL_Main class attributes and methods
appBuilderDSL_Main_appName: Property = Property(name="appName", type=StringType)
appBuilderDSL_Main_appVersion: Property = Property(name="appVersion", type=StringType)
appBuilderDSL_Main_devices: Property = Property(name="devices", type=StringType)
appBuilderDSL_Main_generalStyle: Property = Property(name="generalStyle", type=StringType)
appBuilderDSL_Main.attributes={appBuilderDSL_Main_generalStyle, appBuilderDSL_Main_devices, appBuilderDSL_Main_appVersion, appBuilderDSL_Main_appName}

# appBuilderDSL_Screen class attributes and methods
appBuilderDSL_Screen_name: Property = Property(name="name", type=StringType)
appBuilderDSL_Screen.attributes={appBuilderDSL_Screen_name}

# appBuilderDSL_SimpleScreen class attributes and methods

# Screen class attributes and methods

# appBuilderDSL_EntryParameters class attributes and methods

# appBuilderDSL_Model class attributes and methods

# appBuilderDSL_View class attributes and methods

# appBuilderDSL_Controller class attributes and methods

# appBuilderDSL_Attribute class attributes and methods
appBuilderDSL_Attribute_name: Property = Property(name="name", type=StringType)
appBuilderDSL_Attribute_type: Property = Property(name="type", type=StringType)
appBuilderDSL_Attribute.attributes={appBuilderDSL_Attribute_name, appBuilderDSL_Attribute_type}

# appBuilderDSL_InitAction class attributes and methods

# appBuilderDSL_Validator class attributes and methods

# appBuilderDSL_Action class attributes and methods

# appBuilderDSL_DataBinding class attributes and methods
appBuilderDSL_DataBinding_controlAccess: Property = Property(name="controlAccess", type=StringType)
appBuilderDSL_DataBinding.attributes={appBuilderDSL_DataBinding_controlAccess}

# appBuilderDSL_UiListenerBinding class attributes and methods
appBuilderDSL_UiListenerBinding_controlAccess: Property = Property(name="controlAccess", type=StringType)
appBuilderDSL_UiListenerBinding.attributes={appBuilderDSL_UiListenerBinding_controlAccess}

# appBuilderDSL_ValidationBinding class attributes and methods
appBuilderDSL_ValidationBinding_controlAccess: Property = Property(name="controlAccess", type=StringType)
appBuilderDSL_ValidationBinding.attributes={appBuilderDSL_ValidationBinding_controlAccess}

# appBuilderDSL_Instruction class attributes and methods

# appBuilderDSL_Condition class attributes and methods
appBuilderDSL_Condition_name: Property = Property(name="name", type=StringType)
appBuilderDSL_Condition.attributes={appBuilderDSL_Condition_name}

# appBuilderDSL_Control class attributes and methods

# appBuilderDSL_SimpleDataBinding class attributes and methods
appBuilderDSL_SimpleDataBinding_modelAccess: Property = Property(name="modelAccess", type=StringType)
appBuilderDSL_SimpleDataBinding.attributes={appBuilderDSL_SimpleDataBinding_modelAccess}

# DataBinding class attributes and methods

# appBuilderDSL_EnumDataBinding class attributes and methods
appBuilderDSL_EnumDataBinding_enumClassName: Property = Property(name="enumClassName", type=StringType)
appBuilderDSL_EnumDataBinding.attributes={appBuilderDSL_EnumDataBinding_enumClassName}

# appBuilderDSL_ConditionExpression class attributes and methods

# appBuilderDSL_SimpleConditionExpression class attributes and methods
appBuilderDSL_SimpleConditionExpression_variableName: Property = Property(name="variableName", type=StringType)
appBuilderDSL_SimpleConditionExpression.attributes={appBuilderDSL_SimpleConditionExpression_variableName}

# ConditionExpression class attributes and methods

# appBuilderDSL_CompositeConditionExpression class attributes and methods

# appBuilderDSL_UiAction class attributes and methods
appBuilderDSL_UiAction_name: Property = Property(name="name", type=StringType)
appBuilderDSL_UiAction.attributes={appBuilderDSL_UiAction_name}

# Action class attributes and methods

# appBuilderDSL_SetInstruction class attributes and methods
appBuilderDSL_SetInstruction_modelAccess: Property = Property(name="modelAccess", type=StringType)
appBuilderDSL_SetInstruction.attributes={appBuilderDSL_SetInstruction_modelAccess}

# Instruction class attributes and methods

# appBuilderDSL_SetInstructionAssignment class attributes and methods

# appBuilderDSL_Navigate class attributes and methods
appBuilderDSL_Navigate_params: Property = Property(name="params", type=StringType)
appBuilderDSL_Navigate.attributes={appBuilderDSL_Navigate_params}

# appBuilderDSL_ExecuteAction class attributes and methods

# appBuilderDSL_RestCall class attributes and methods
appBuilderDSL_RestCall_url: Property = Property(name="url", type=StringType)
appBuilderDSL_RestCall.attributes={appBuilderDSL_RestCall_url}

# SetInstructionAssignment class attributes and methods

# appBuilderDSL_ControlValue class attributes and methods
appBuilderDSL_ControlValue_controlAccess: Property = Property(name="controlAccess", type=StringType)
appBuilderDSL_ControlValue.attributes={appBuilderDSL_ControlValue_controlAccess}

# appBuilderDSL_List class attributes and methods
appBuilderDSL_List_name: Property = Property(name="name", type=StringType)
appBuilderDSL_List.attributes={appBuilderDSL_List_name}

# appBuilderDSL_Layout class attributes and methods
appBuilderDSL_Layout_type: Property = Property(name="type", type=StringType)
appBuilderDSL_Layout.attributes={appBuilderDSL_Layout_type}

# Control class attributes and methods

# appBuilderDSL_GridLayout class attributes and methods
appBuilderDSL_GridLayout_columns: Property = Property(name="columns", type=IntegerType)
appBuilderDSL_GridLayout.attributes={appBuilderDSL_GridLayout_columns}

# Layout class attributes and methods

# appBuilderDSL_RowLayout class attributes and methods

# appBuilderDSL_ScreenLayout class attributes and methods

# appBuilderDSL_Value class attributes and methods

# appBuilderDSL_DynamicValue class attributes and methods
appBuilderDSL_DynamicValue_variableName: Property = Property(name="variableName", type=StringType)
appBuilderDSL_DynamicValue_type: Property = Property(name="type", type=StringType)
appBuilderDSL_DynamicValue.attributes={appBuilderDSL_DynamicValue_type, appBuilderDSL_DynamicValue_variableName}

# Value class attributes and methods

# appBuilderDSL_Expression class attributes and methods
appBuilderDSL_Expression_terms: Property = Property(name="terms", type=StringType)
appBuilderDSL_Expression.attributes={appBuilderDSL_Expression_terms}

# appBuilderDSL_Text class attributes and methods
appBuilderDSL_Text_name: Property = Property(name="name", type=StringType)
appBuilderDSL_Text.attributes={appBuilderDSL_Text_name}

# appBuilderDSL_Button class attributes and methods
appBuilderDSL_Button_name: Property = Property(name="name", type=StringType)
appBuilderDSL_Button.attributes={appBuilderDSL_Button_name}

# appBuilderDSL_Label class attributes and methods
appBuilderDSL_Label_name: Property = Property(name="name", type=StringType)
appBuilderDSL_Label.attributes={appBuilderDSL_Label_name}

# appBuilderDSL_CompositeScreen class attributes and methods

# appBuilderDSL_Import class attributes and methods
appBuilderDSL_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
appBuilderDSL_Import.attributes={appBuilderDSL_Import_importedNamespace}

# appBuilderDSL_Type class attributes and methods
appBuilderDSL_Type_name: Property = Property(name="name", type=StringType)
appBuilderDSL_Type.attributes={appBuilderDSL_Type_name}

# appBuilderDSL_DataType class attributes and methods

# Type class attributes and methods

# appBuilderDSL_Entity class attributes and methods

# appBuilderDSL_Feature class attributes and methods
appBuilderDSL_Feature_many: Property = Property(name="many", type=BooleanType)
appBuilderDSL_Feature_name: Property = Property(name="name", type=StringType)
appBuilderDSL_Feature.attributes={appBuilderDSL_Feature_many, appBuilderDSL_Feature_name}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="appBuilderDSL_AbstractElement", type=appBuilderDSL_AppBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_AppBuilder", type=appBuilderDSL_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
business1: BinaryAssociation = BinaryAssociation(
    name="business1",
    ends={
        Property(name="appBuilderDSL_Business", type=appBuilderDSL_System, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_System", type=appBuilderDSL_Business, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ui2: BinaryAssociation = BinaryAssociation(
    name="ui2",
    ends={
        Property(name="appBuilderDSL_Ui", type=appBuilderDSL_System, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_System3", type=appBuilderDSL_Ui, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements4: BinaryAssociation = BinaryAssociation(
    name="elements4",
    ends={
        Property(name="appBuilderDSL_Service", type=appBuilderDSL_Business, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Business5", type=appBuilderDSL_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
main6: BinaryAssociation = BinaryAssociation(
    name="main6",
    ends={
        Property(name="appBuilderDSL_Main", type=appBuilderDSL_Ui, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Ui7", type=appBuilderDSL_Main, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
services8: BinaryAssociation = BinaryAssociation(
    name="services8",
    ends={
        Property(name="appBuilderDSL_Service10", type=appBuilderDSL_Ui, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Ui9", type=appBuilderDSL_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
screens11: BinaryAssociation = BinaryAssociation(
    name="screens11",
    ends={
        Property(name="appBuilderDSL_Screen", type=appBuilderDSL_Ui, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Ui12", type=appBuilderDSL_Screen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
screen13: BinaryAssociation = BinaryAssociation(
    name="screen13",
    ends={
        Property(name="appBuilderDSL_Screen15", type=appBuilderDSL_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Main14", type=appBuilderDSL_Screen, multiplicity=Multiplicity(0, 1))
    }
)
entryParameters16: BinaryAssociation = BinaryAssociation(
    name="entryParameters16",
    ends={
        Property(name="appBuilderDSL_EntryParameters", type=appBuilderDSL_SimpleScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_SimpleScreen", type=appBuilderDSL_EntryParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model17: BinaryAssociation = BinaryAssociation(
    name="model17",
    ends={
        Property(name="appBuilderDSL_Model", type=appBuilderDSL_SimpleScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_SimpleScreen18", type=appBuilderDSL_Model, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
view19: BinaryAssociation = BinaryAssociation(
    name="view19",
    ends={
        Property(name="appBuilderDSL_View", type=appBuilderDSL_SimpleScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_SimpleScreen20", type=appBuilderDSL_View, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
controller21: BinaryAssociation = BinaryAssociation(
    name="controller21",
    ends={
        Property(name="appBuilderDSL_Controller", type=appBuilderDSL_SimpleScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_SimpleScreen22", type=appBuilderDSL_Controller, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes23: BinaryAssociation = BinaryAssociation(
    name="attributes23",
    ends={
        Property(name="appBuilderDSL_Attribute", type=appBuilderDSL_EntryParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_EntryParameters24", type=appBuilderDSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initAction25: BinaryAssociation = BinaryAssociation(
    name="initAction25",
    ends={
        Property(name="appBuilderDSL_InitAction", type=appBuilderDSL_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Controller26", type=appBuilderDSL_InitAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validator27: BinaryAssociation = BinaryAssociation(
    name="validator27",
    ends={
        Property(name="appBuilderDSL_Validator", type=appBuilderDSL_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Controller28", type=appBuilderDSL_Validator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions29: BinaryAssociation = BinaryAssociation(
    name="actions29",
    ends={
        Property(name="appBuilderDSL_Action", type=appBuilderDSL_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Controller30", type=appBuilderDSL_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
databindings31: BinaryAssociation = BinaryAssociation(
    name="databindings31",
    ends={
        Property(name="appBuilderDSL_DataBinding", type=appBuilderDSL_InitAction, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_InitAction32", type=appBuilderDSL_DataBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uiListenerBindingss33: BinaryAssociation = BinaryAssociation(
    name="uiListenerBindingss33",
    ends={
        Property(name="appBuilderDSL_UiListenerBinding", type=appBuilderDSL_InitAction, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_InitAction34", type=appBuilderDSL_UiListenerBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validationBindings35: BinaryAssociation = BinaryAssociation(
    name="validationBindings35",
    ends={
        Property(name="appBuilderDSL_ValidationBinding", type=appBuilderDSL_InitAction, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_InitAction36", type=appBuilderDSL_ValidationBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions37: BinaryAssociation = BinaryAssociation(
    name="instructions37",
    ends={
        Property(name="appBuilderDSL_Instruction", type=appBuilderDSL_InitAction, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_InitAction38", type=appBuilderDSL_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition39: BinaryAssociation = BinaryAssociation(
    name="condition39",
    ends={
        Property(name="appBuilderDSL_Condition", type=appBuilderDSL_ValidationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_ValidationBinding40", type=appBuilderDSL_Condition, multiplicity=Multiplicity(0, 1))
    }
)
control41: BinaryAssociation = BinaryAssociation(
    name="control41",
    ends={
        Property(name="appBuilderDSL_Control", type=appBuilderDSL_ValidationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_ValidationBinding42", type=appBuilderDSL_Control, multiplicity=Multiplicity(0, 1))
    }
)
action43: BinaryAssociation = BinaryAssociation(
    name="action43",
    ends={
        Property(name="appBuilderDSL_Action45", type=appBuilderDSL_UiListenerBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_UiListenerBinding44", type=appBuilderDSL_Action, multiplicity=Multiplicity(0, 1))
    }
)
control46: BinaryAssociation = BinaryAssociation(
    name="control46",
    ends={
        Property(name="appBuilderDSL_Control48", type=appBuilderDSL_UiListenerBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_UiListenerBinding47", type=appBuilderDSL_Control, multiplicity=Multiplicity(0, 1))
    }
)
control49: BinaryAssociation = BinaryAssociation(
    name="control49",
    ends={
        Property(name="appBuilderDSL_Control51", type=appBuilderDSL_DataBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_DataBinding50", type=appBuilderDSL_Control, multiplicity=Multiplicity(0, 1))
    }
)
model52: BinaryAssociation = BinaryAssociation(
    name="model52",
    ends={
        Property(name="appBuilderDSL_SimpleDataBinding", type=appBuilderDSL_Attribute, multiplicity=Multiplicity(0, 1)),
        Property(name="appBuilderDSL_Attribute53", type=appBuilderDSL_SimpleDataBinding, multiplicity=Multiplicity(1, 1))
    }
)
conditions54: BinaryAssociation = BinaryAssociation(
    name="conditions54",
    ends={
        Property(name="appBuilderDSL_Condition56", type=appBuilderDSL_Validator, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Validator55", type=appBuilderDSL_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionExpression57: BinaryAssociation = BinaryAssociation(
    name="conditionExpression57",
    ends={
        Property(name="appBuilderDSL_ConditionExpression", type=appBuilderDSL_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Condition58", type=appBuilderDSL_ConditionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditions59: BinaryAssociation = BinaryAssociation(
    name="conditions59",
    ends={
        Property(name="appBuilderDSL_Condition60", type=appBuilderDSL_CompositeConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_CompositeConditionExpression", type=appBuilderDSL_Condition, multiplicity=Multiplicity(0, 9999))
    }
)
instructions61: BinaryAssociation = BinaryAssociation(
    name="instructions61",
    ends={
        Property(name="appBuilderDSL_Instruction62", type=appBuilderDSL_UiAction, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_UiAction", type=appBuilderDSL_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model63: BinaryAssociation = BinaryAssociation(
    name="model63",
    ends={
        Property(name="appBuilderDSL_Attribute64", type=appBuilderDSL_SetInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_SetInstruction", type=appBuilderDSL_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
assignment65: BinaryAssociation = BinaryAssociation(
    name="assignment65",
    ends={
        Property(name="appBuilderDSL_SetInstructionAssignment", type=appBuilderDSL_SetInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_SetInstruction66", type=appBuilderDSL_SetInstructionAssignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
screen67: BinaryAssociation = BinaryAssociation(
    name="screen67",
    ends={
        Property(name="appBuilderDSL_Screen68", type=appBuilderDSL_Navigate, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Navigate", type=appBuilderDSL_Screen, multiplicity=Multiplicity(0, 1))
    }
)
action69: BinaryAssociation = BinaryAssociation(
    name="action69",
    ends={
        Property(name="appBuilderDSL_Action70", type=appBuilderDSL_ExecuteAction, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_ExecuteAction", type=appBuilderDSL_Action, multiplicity=Multiplicity(0, 1))
    }
)
control71: BinaryAssociation = BinaryAssociation(
    name="control71",
    ends={
        Property(name="appBuilderDSL_Control72", type=appBuilderDSL_ControlValue, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_ControlValue", type=appBuilderDSL_Control, multiplicity=Multiplicity(0, 1))
    }
)
attributes73: BinaryAssociation = BinaryAssociation(
    name="attributes73",
    ends={
        Property(name="appBuilderDSL_Attribute75", type=appBuilderDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Model74", type=appBuilderDSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layouts76: BinaryAssociation = BinaryAssociation(
    name="layouts76",
    ends={
        Property(name="appBuilderDSL_Layout", type=appBuilderDSL_View, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_View77", type=appBuilderDSL_Layout, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controls78: BinaryAssociation = BinaryAssociation(
    name="controls78",
    ends={
        Property(name="appBuilderDSL_Control80", type=appBuilderDSL_Layout, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Layout79", type=appBuilderDSL_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
screen81: BinaryAssociation = BinaryAssociation(
    name="screen81",
    ends={
        Property(name="appBuilderDSL_Screen82", type=appBuilderDSL_ScreenLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_ScreenLayout", type=appBuilderDSL_Screen, multiplicity=Multiplicity(0, 1))
    }
)
labelprovider83: BinaryAssociation = BinaryAssociation(
    name="labelprovider83",
    ends={
        Property(name="appBuilderDSL_Value", type=appBuilderDSL_List, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_List", type=appBuilderDSL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cssStyle84: BinaryAssociation = BinaryAssociation(
    name="cssStyle84",
    ends={
        Property(name="appBuilderDSL_Value86", type=appBuilderDSL_List, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_List85", type=appBuilderDSL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tooltip87: BinaryAssociation = BinaryAssociation(
    name="tooltip87",
    ends={
        Property(name="appBuilderDSL_Value89", type=appBuilderDSL_List, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_List88", type=appBuilderDSL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression90: BinaryAssociation = BinaryAssociation(
    name="expression90",
    ends={
        Property(name="appBuilderDSL_Expression", type=appBuilderDSL_DynamicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_DynamicValue", type=appBuilderDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cssStyle91: BinaryAssociation = BinaryAssociation(
    name="cssStyle91",
    ends={
        Property(name="appBuilderDSL_Value92", type=appBuilderDSL_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Text", type=appBuilderDSL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceKey93: BinaryAssociation = BinaryAssociation(
    name="resourceKey93",
    ends={
        Property(name="appBuilderDSL_Value95", type=appBuilderDSL_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Text94", type=appBuilderDSL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cssStyle96: BinaryAssociation = BinaryAssociation(
    name="cssStyle96",
    ends={
        Property(name="appBuilderDSL_Value97", type=appBuilderDSL_Button, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Button", type=appBuilderDSL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceKey98: BinaryAssociation = BinaryAssociation(
    name="resourceKey98",
    ends={
        Property(name="appBuilderDSL_Value100", type=appBuilderDSL_Button, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Button99", type=appBuilderDSL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceKey101: BinaryAssociation = BinaryAssociation(
    name="resourceKey101",
    ends={
        Property(name="appBuilderDSL_Value102", type=appBuilderDSL_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Label", type=appBuilderDSL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layouts103: BinaryAssociation = BinaryAssociation(
    name="layouts103",
    ends={
        Property(name="appBuilderDSL_Layout104", type=appBuilderDSL_CompositeScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_CompositeScreen", type=appBuilderDSL_Layout, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType106: BinaryAssociation = BinaryAssociation(
    name="superType106",
    ends={
        Property(name="appBuilderDSL_Entity", type=appBuilderDSL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Entity105", type=appBuilderDSL_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features107: BinaryAssociation = BinaryAssociation(
    name="features107",
    ends={
        Property(name="appBuilderDSL_Feature", type=appBuilderDSL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Entity108", type=appBuilderDSL_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type109: BinaryAssociation = BinaryAssociation(
    name="type109",
    ends={
        Property(name="appBuilderDSL_Type", type=appBuilderDSL_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="appBuilderDSL_Feature110", type=appBuilderDSL_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_appBuilderDSL_NamespaceDeclation_AbstractElement = Generalization(general=AbstractElement, specific=appBuilderDSL_NamespaceDeclation)
gen_appBuilderDSL_System_AbstractElement = Generalization(general=AbstractElement, specific=appBuilderDSL_System)
gen_appBuilderDSL_InstanceService_Service = Generalization(general=Service, specific=appBuilderDSL_InstanceService)
gen_appBuilderDSL_SimpleScreen_Screen = Generalization(general=Screen, specific=appBuilderDSL_SimpleScreen)
gen_appBuilderDSL_SimpleDataBinding_DataBinding = Generalization(general=DataBinding, specific=appBuilderDSL_SimpleDataBinding)
gen_appBuilderDSL_EnumDataBinding_DataBinding = Generalization(general=DataBinding, specific=appBuilderDSL_EnumDataBinding)
gen_appBuilderDSL_SimpleConditionExpression_ConditionExpression = Generalization(general=ConditionExpression, specific=appBuilderDSL_SimpleConditionExpression)
gen_appBuilderDSL_CompositeConditionExpression_ConditionExpression = Generalization(general=ConditionExpression, specific=appBuilderDSL_CompositeConditionExpression)
gen_appBuilderDSL_UiAction_Action = Generalization(general=Action, specific=appBuilderDSL_UiAction)
gen_appBuilderDSL_SetInstruction_Instruction = Generalization(general=Instruction, specific=appBuilderDSL_SetInstruction)
gen_appBuilderDSL_Navigate_Instruction = Generalization(general=Instruction, specific=appBuilderDSL_Navigate)
gen_appBuilderDSL_ExecuteAction_Instruction = Generalization(general=Instruction, specific=appBuilderDSL_ExecuteAction)
gen_appBuilderDSL_RestCall_SetInstructionAssignment = Generalization(general=SetInstructionAssignment, specific=appBuilderDSL_RestCall)
gen_appBuilderDSL_ControlValue_SetInstructionAssignment = Generalization(general=SetInstructionAssignment, specific=appBuilderDSL_ControlValue)
gen_appBuilderDSL_Layout_Control = Generalization(general=Control, specific=appBuilderDSL_Layout)
gen_appBuilderDSL_GridLayout_Layout = Generalization(general=Layout, specific=appBuilderDSL_GridLayout)
gen_appBuilderDSL_RowLayout_Layout = Generalization(general=Layout, specific=appBuilderDSL_RowLayout)
gen_appBuilderDSL_ScreenLayout_Control = Generalization(general=Control, specific=appBuilderDSL_ScreenLayout)
gen_appBuilderDSL_List_Control = Generalization(general=Control, specific=appBuilderDSL_List)
gen_appBuilderDSL_DynamicValue_SetInstructionAssignment = Generalization(general=SetInstructionAssignment, specific=appBuilderDSL_DynamicValue)
gen_appBuilderDSL_DynamicValue_Value = Generalization(general=Value, specific=appBuilderDSL_DynamicValue)
gen_appBuilderDSL_Text_Control = Generalization(general=Control, specific=appBuilderDSL_Text)
gen_appBuilderDSL_Button_Control = Generalization(general=Control, specific=appBuilderDSL_Button)
gen_appBuilderDSL_Label_Control = Generalization(general=Control, specific=appBuilderDSL_Label)
gen_appBuilderDSL_CompositeScreen_Screen = Generalization(general=Screen, specific=appBuilderDSL_CompositeScreen)
gen_appBuilderDSL_DataType_Type = Generalization(general=Type, specific=appBuilderDSL_DataType)
gen_appBuilderDSL_Entity_Type = Generalization(general=Type, specific=appBuilderDSL_Entity)

# Domain Model
domain_model = DomainModel(
    name="appBuilderDSL",
    types={appBuilderDSL_AppBuilder, appBuilderDSL_AbstractElement, appBuilderDSL_NamespaceDeclation, AbstractElement, appBuilderDSL_System, appBuilderDSL_Business, appBuilderDSL_Ui, appBuilderDSL_Service, appBuilderDSL_InstanceService, Service, appBuilderDSL_Main, appBuilderDSL_Screen, appBuilderDSL_SimpleScreen, Screen, appBuilderDSL_EntryParameters, appBuilderDSL_Model, appBuilderDSL_View, appBuilderDSL_Controller, appBuilderDSL_Attribute, appBuilderDSL_InitAction, appBuilderDSL_Validator, appBuilderDSL_Action, appBuilderDSL_DataBinding, appBuilderDSL_UiListenerBinding, appBuilderDSL_ValidationBinding, appBuilderDSL_Instruction, appBuilderDSL_Condition, appBuilderDSL_Control, appBuilderDSL_SimpleDataBinding, DataBinding, appBuilderDSL_EnumDataBinding, appBuilderDSL_ConditionExpression, appBuilderDSL_SimpleConditionExpression, ConditionExpression, appBuilderDSL_CompositeConditionExpression, appBuilderDSL_UiAction, Action, appBuilderDSL_SetInstruction, Instruction, appBuilderDSL_SetInstructionAssignment, appBuilderDSL_Navigate, appBuilderDSL_ExecuteAction, appBuilderDSL_RestCall, SetInstructionAssignment, appBuilderDSL_ControlValue, appBuilderDSL_List, appBuilderDSL_Layout, Control, appBuilderDSL_GridLayout, Layout, appBuilderDSL_RowLayout, appBuilderDSL_ScreenLayout, appBuilderDSL_Value, appBuilderDSL_DynamicValue, Value, appBuilderDSL_Expression, appBuilderDSL_Text, appBuilderDSL_Button, appBuilderDSL_Label, appBuilderDSL_CompositeScreen, appBuilderDSL_Import, appBuilderDSL_Type, appBuilderDSL_DataType, Type, appBuilderDSL_Entity, appBuilderDSL_Feature, Device},
    associations={elements0, business1, ui2, elements4, main6, services8, screens11, screen13, entryParameters16, model17, view19, controller21, attributes23, initAction25, validator27, actions29, databindings31, uiListenerBindingss33, validationBindings35, instructions37, condition39, control41, action43, control46, control49, model52, conditions54, conditionExpression57, conditions59, instructions61, model63, assignment65, screen67, action69, control71, attributes73, layouts76, controls78, screen81, labelprovider83, cssStyle84, tooltip87, expression90, cssStyle91, resourceKey93, cssStyle96, resourceKey98, resourceKey101, layouts103, superType106, features107, type109},
    generalizations={gen_appBuilderDSL_NamespaceDeclation_AbstractElement, gen_appBuilderDSL_System_AbstractElement, gen_appBuilderDSL_InstanceService_Service, gen_appBuilderDSL_SimpleScreen_Screen, gen_appBuilderDSL_SimpleDataBinding_DataBinding, gen_appBuilderDSL_EnumDataBinding_DataBinding, gen_appBuilderDSL_SimpleConditionExpression_ConditionExpression, gen_appBuilderDSL_CompositeConditionExpression_ConditionExpression, gen_appBuilderDSL_UiAction_Action, gen_appBuilderDSL_SetInstruction_Instruction, gen_appBuilderDSL_Navigate_Instruction, gen_appBuilderDSL_ExecuteAction_Instruction, gen_appBuilderDSL_RestCall_SetInstructionAssignment, gen_appBuilderDSL_ControlValue_SetInstructionAssignment, gen_appBuilderDSL_Layout_Control, gen_appBuilderDSL_GridLayout_Layout, gen_appBuilderDSL_RowLayout_Layout, gen_appBuilderDSL_ScreenLayout_Control, gen_appBuilderDSL_List_Control, gen_appBuilderDSL_DynamicValue_SetInstructionAssignment, gen_appBuilderDSL_DynamicValue_Value, gen_appBuilderDSL_Text_Control, gen_appBuilderDSL_Button_Control, gen_appBuilderDSL_Label_Control, gen_appBuilderDSL_CompositeScreen_Screen, gen_appBuilderDSL_DataType_Type, gen_appBuilderDSL_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)