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
ContentElementLiteral: Enumeration = Enumeration(
    name="ContentElementLiteral",
    literals={
            EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="BUTTON"),
			EnumerationLiteral(name="LABEL"),
			EnumerationLiteral(name="LIST"),
			EnumerationLiteral(name="IMAGE")
    }
)

PropertyNameLiteral: Enumeration = Enumeration(
    name="PropertyNameLiteral",
    literals={
            EnumerationLiteral(name="STYLE"),
			EnumerationLiteral(name="PATH"),
			EnumerationLiteral(name="LABEL_PROVIDER"),
			EnumerationLiteral(name="CSS_ITEM"),
			EnumerationLiteral(name="TOOLTIP"),
			EnumerationLiteral(name="RESOURCE_KEY"),
			EnumerationLiteral(name="TYPE"),
			EnumerationLiteral(name="COLUMNS")
    }
)

ContainerElementLiteral: Enumeration = Enumeration(
    name="ContainerElementLiteral",
    literals={
            EnumerationLiteral(name="LAYOUT"),
			EnumerationLiteral(name="SCREEN")
    }
)

UIElementReceiverKey: Enumeration = Enumeration(
    name="UIElementReceiverKey",
    literals={
            EnumerationLiteral(name="SELECTION"),
			EnumerationLiteral(name="VALUES_"),
			EnumerationLiteral(name="ON_SELECTION"),
			EnumerationLiteral(name="TEXT")
    }
)

# Classes
domainmodel_Domainmodel = Class(name="domainmodel::Domainmodel")
domainmodel_AbstractElement = Class(name="domainmodel::AbstractElement")
domainmodel_Type = Class(name="domainmodel::Type")
domainmodel_Import = Class(name="domainmodel::Import")
AbstractNamespaceElement = Class(name="AbstractNamespaceElement")
domainmodel_DataType = Class(name="domainmodel::DataType")
Type = Class(name="Type")
domainmodel_NamespaceDeclaration = Class(name="domainmodel::NamespaceDeclaration")
AbstractElement = Class(name="AbstractElement")
domainmodel_AbstractNamespaceElement = Class(name="domainmodel::AbstractNamespaceElement")
domainmodel_Feature = Class(name="domainmodel::Feature")
domainmodel_DomainEntity = Class(name="domainmodel::DomainEntity")
domainmodel_MethodParameter = Class(name="domainmodel::MethodParameter")
domainmodel_MethodParameters = Class(name="domainmodel::MethodParameters")
domainmodel_MethodCall = Class(name="domainmodel::MethodCall")
domainmodel_InterfaceOperation = Class(name="domainmodel::InterfaceOperation")
domainmodel_InterfaceDeclaration = Class(name="domainmodel::InterfaceDeclaration")
BusinessFeatureType = Class(name="BusinessFeatureType")
domainmodel_InterfaceOperationUsageRule = Class(name="domainmodel::InterfaceOperationUsageRule")
domainmodel_InterfaceOperationsUsageRule = Class(name="domainmodel::InterfaceOperationsUsageRule")
domainmodel_StatelessComponent = Class(name="domainmodel::StatelessComponent")
domainmodel_DomainRepository = Class(name="domainmodel::DomainRepository")
domainmodel_EntryParametersModule = Class(name="domainmodel::EntryParametersModule")
ScreenModule = Class(name="ScreenModule")
domainmodel_ModelFeature = Class(name="domainmodel::ModelFeature")
domainmodel_ModelModule = Class(name="domainmodel::ModelModule")
domainmodel_InitActionModule = Class(name="domainmodel::InitActionModule")
ControllerElement = Class(name="ControllerElement")
domainmodel_ElementFeature = Class(name="domainmodel::ElementFeature")
domainmodel_ContentElement = Class(name="domainmodel::ContentElement")
ViewElement = Class(name="ViewElement")
domainmodel_ContainerElement = Class(name="domainmodel::ContainerElement")
domainmodel_ViewElement = Class(name="domainmodel::ViewElement")
domainmodel_ViewModule = Class(name="domainmodel::ViewModule")
domainmodel_ValidateAction = Class(name="domainmodel::ValidateAction")
InitActionFeature = Class(name="InitActionFeature")
domainmodel_ValidatorFeature = Class(name="domainmodel::ValidatorFeature")
domainmodel_SetUIElementReceiver = Class(name="domainmodel::SetUIElementReceiver")
domainmodel_AttachAction = Class(name="domainmodel::AttachAction")
domainmodel_UIActionModule = Class(name="domainmodel::UIActionModule")
domainmodel_BindEnumSource = Class(name="domainmodel::BindEnumSource")
BindSource = Class(name="BindSource")
domainmodel_BindSource = Class(name="domainmodel::BindSource")
domainmodel_BindAction = Class(name="domainmodel::BindAction")
domainmodel_InitActionFeature = Class(name="domainmodel::InitActionFeature")
domainmodel_ValidatorRule = Class(name="domainmodel::ValidatorRule")
domainmodel_ValidatorRules = Class(name="domainmodel::ValidatorRules")
domainmodel_ValidatorModule = Class(name="domainmodel::ValidatorModule")
domainmodel_ScreenModelParameter = Class(name="domainmodel::ScreenModelParameter")
domainmodel_ScreenModelParameters = Class(name="domainmodel::ScreenModelParameters")
domainmodel_NavigateToAction = Class(name="domainmodel::NavigateToAction")
UIActionFeature = Class(name="UIActionFeature")
domainmodel_ScreenFeature = Class(name="domainmodel::ScreenFeature")
domainmodel_ExecuteAction = Class(name="domainmodel::ExecuteAction")
domainmodel_SetRestCallReceiverURLParameter = Class(name="domainmodel::SetRestCallReceiverURLParameter")
SetRestCallReceiverParameter = Class(name="SetRestCallReceiverParameter")
domainmodel_SetRestCallReceiverReturnTypeParameter = Class(name="domainmodel::SetRestCallReceiverReturnTypeParameter")
domainmodel_SetRestCallReceiverIDParameter = Class(name="domainmodel::SetRestCallReceiverIDParameter")
domainmodel_SetRestCallReceiverParameter = Class(name="domainmodel::SetRestCallReceiverParameter")
domainmodel_SetRestCallReceiverParameters = Class(name="domainmodel::SetRestCallReceiverParameters")
domainmodel_SetRestCallReceiver = Class(name="domainmodel::SetRestCallReceiver")
SetActionReceiver = Class(name="SetActionReceiver")
domainmodel_MainFeatureOption = Class(name="domainmodel::MainFeatureOption")
domainmodel_SetActionReceiver = Class(name="domainmodel::SetActionReceiver")
domainmodel_SetAction = Class(name="domainmodel::SetAction")
domainmodel_InterfaceMethodCallParameter = Class(name="domainmodel::InterfaceMethodCallParameter")
domainmodel_InterfaceMethodCallParameters = Class(name="domainmodel::InterfaceMethodCallParameters")
domainmodel_InterfaceMethodCall = Class(name="domainmodel::InterfaceMethodCall")
domainmodel_BusinessFeature = Class(name="domainmodel::BusinessFeature")
domainmodel_UIActionFeature = Class(name="domainmodel::UIActionFeature")
domainmodel_ControllerElement = Class(name="domainmodel::ControllerElement")
domainmodel_ControllerModule = Class(name="domainmodel::ControllerModule")
domainmodel_ScreenModule = Class(name="domainmodel::ScreenModule")
UIFeature = Class(name="UIFeature")
domainmodel_MainFeature = Class(name="domainmodel::MainFeature")
domainmodel_UIFeature = Class(name="domainmodel::UIFeature")
domainmodel_UIModule = Class(name="domainmodel::UIModule")
SystemModule = Class(name="SystemModule")
domainmodel_BusinessFeatureType = Class(name="domainmodel::BusinessFeatureType")
domainmodel_BusinessFeatures = Class(name="domainmodel::BusinessFeatures")
BusinessModule = Class(name="BusinessModule")
domainmodel_BusinessModule = Class(name="domainmodel::BusinessModule")
domainmodel_SystemModule = Class(name="domainmodel::SystemModule")
domainmodel_SystemDefinition = Class(name="domainmodel::SystemDefinition")

# domainmodel_Domainmodel class attributes and methods

# domainmodel_AbstractElement class attributes and methods
domainmodel_AbstractElement_name: Property = Property(name="name", type=StringType)
domainmodel_AbstractElement.attributes={domainmodel_AbstractElement_name}

# domainmodel_Type class attributes and methods

# domainmodel_Import class attributes and methods
domainmodel_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
domainmodel_Import.attributes={domainmodel_Import_importedNamespace}

# AbstractNamespaceElement class attributes and methods

# domainmodel_DataType class attributes and methods
domainmodel_DataType_name: Property = Property(name="name", type=StringType)
domainmodel_DataType_mappedType: Property = Property(name="mappedType", type=StringType)
domainmodel_DataType_initValue: Property = Property(name="initValue", type=StringType)
domainmodel_DataType.attributes={domainmodel_DataType_initValue, domainmodel_DataType_name, domainmodel_DataType_mappedType}

# Type class attributes and methods

# domainmodel_NamespaceDeclaration class attributes and methods

# AbstractElement class attributes and methods

# domainmodel_AbstractNamespaceElement class attributes and methods

# domainmodel_Feature class attributes and methods
domainmodel_Feature_name: Property = Property(name="name", type=StringType)
domainmodel_Feature_mappingOption: Property = Property(name="mappingOption", type=StringType)
domainmodel_Feature_mapName: Property = Property(name="mapName", type=StringType)
domainmodel_Feature.attributes={domainmodel_Feature_mapName, domainmodel_Feature_name, domainmodel_Feature_mappingOption}

# domainmodel_DomainEntity class attributes and methods
domainmodel_DomainEntity_name: Property = Property(name="name", type=StringType)
domainmodel_DomainEntity.attributes={domainmodel_DomainEntity_name}

# domainmodel_MethodParameter class attributes and methods
domainmodel_MethodParameter_name: Property = Property(name="name", type=StringType)
domainmodel_MethodParameter.attributes={domainmodel_MethodParameter_name}

# domainmodel_MethodParameters class attributes and methods

# domainmodel_MethodCall class attributes and methods
domainmodel_MethodCall_name: Property = Property(name="name", type=StringType)
domainmodel_MethodCall.attributes={domainmodel_MethodCall_name}

# domainmodel_InterfaceOperation class attributes and methods
domainmodel_InterfaceOperation_restOperation: Property = Property(name="restOperation", type=StringType)
domainmodel_InterfaceOperation.attributes={domainmodel_InterfaceOperation_restOperation}

# domainmodel_InterfaceDeclaration class attributes and methods
domainmodel_InterfaceDeclaration_name: Property = Property(name="name", type=StringType)
domainmodel_InterfaceDeclaration.attributes={domainmodel_InterfaceDeclaration_name}

# BusinessFeatureType class attributes and methods

# domainmodel_InterfaceOperationUsageRule class attributes and methods
domainmodel_InterfaceOperationUsageRule_name: Property = Property(name="name", type=StringType)
domainmodel_InterfaceOperationUsageRule.attributes={domainmodel_InterfaceOperationUsageRule_name}

# domainmodel_InterfaceOperationsUsageRule class attributes and methods

# domainmodel_StatelessComponent class attributes and methods
domainmodel_StatelessComponent_name: Property = Property(name="name", type=StringType)
domainmodel_StatelessComponent.attributes={domainmodel_StatelessComponent_name}

# domainmodel_DomainRepository class attributes and methods
domainmodel_DomainRepository_name: Property = Property(name="name", type=StringType)
domainmodel_DomainRepository.attributes={domainmodel_DomainRepository_name}

# domainmodel_EntryParametersModule class attributes and methods

# ScreenModule class attributes and methods

# domainmodel_ModelFeature class attributes and methods
domainmodel_ModelFeature_name: Property = Property(name="name", type=StringType)
domainmodel_ModelFeature.attributes={domainmodel_ModelFeature_name}

# domainmodel_ModelModule class attributes and methods

# domainmodel_InitActionModule class attributes and methods

# ControllerElement class attributes and methods

# domainmodel_ElementFeature class attributes and methods
domainmodel_ElementFeature_propertyName: Property = Property(name="propertyName", type=StringType)
domainmodel_ElementFeature_propertyValue: Property = Property(name="propertyValue", type=StringType)
domainmodel_ElementFeature.attributes={domainmodel_ElementFeature_propertyValue, domainmodel_ElementFeature_propertyName}

# domainmodel_ContentElement class attributes and methods
domainmodel_ContentElement_contentElement: Property = Property(name="contentElement", type=StringType)
domainmodel_ContentElement.attributes={domainmodel_ContentElement_contentElement}

# ViewElement class attributes and methods

# domainmodel_ContainerElement class attributes and methods
domainmodel_ContainerElement_container: Property = Property(name="container", type=StringType)
domainmodel_ContainerElement.attributes={domainmodel_ContainerElement_container}

# domainmodel_ViewElement class attributes and methods
domainmodel_ViewElement_name: Property = Property(name="name", type=StringType)
domainmodel_ViewElement.attributes={domainmodel_ViewElement_name}

# domainmodel_ViewModule class attributes and methods

# domainmodel_ValidateAction class attributes and methods

# InitActionFeature class attributes and methods

# domainmodel_ValidatorFeature class attributes and methods
domainmodel_ValidatorFeature_name: Property = Property(name="name", type=StringType)
domainmodel_ValidatorFeature.attributes={domainmodel_ValidatorFeature_name}

# domainmodel_SetUIElementReceiver class attributes and methods
domainmodel_SetUIElementReceiver_uiKey: Property = Property(name="uiKey", type=StringType)
domainmodel_SetUIElementReceiver.attributes={domainmodel_SetUIElementReceiver_uiKey}

# domainmodel_AttachAction class attributes and methods

# domainmodel_UIActionModule class attributes and methods
domainmodel_UIActionModule_name: Property = Property(name="name", type=StringType)
domainmodel_UIActionModule.attributes={domainmodel_UIActionModule_name}

# domainmodel_BindEnumSource class attributes and methods
domainmodel_BindEnumSource_enumType: Property = Property(name="enumType", type=StringType)
domainmodel_BindEnumSource.attributes={domainmodel_BindEnumSource_enumType}

# BindSource class attributes and methods

# domainmodel_BindSource class attributes and methods

# domainmodel_BindAction class attributes and methods
domainmodel_BindAction_attribute: Property = Property(name="attribute", type=StringType)
domainmodel_BindAction.attributes={domainmodel_BindAction_attribute}

# domainmodel_InitActionFeature class attributes and methods

# domainmodel_ValidatorRule class attributes and methods
domainmodel_ValidatorRule_stringRule: Property = Property(name="stringRule", type=StringType)
domainmodel_ValidatorRule.attributes={domainmodel_ValidatorRule_stringRule}

# domainmodel_ValidatorRules class attributes and methods

# domainmodel_ValidatorModule class attributes and methods

# domainmodel_ScreenModelParameter class attributes and methods
domainmodel_ScreenModelParameter_modelFeatureValue: Property = Property(name="modelFeatureValue", type=StringType)
domainmodel_ScreenModelParameter.attributes={domainmodel_ScreenModelParameter_modelFeatureValue}

# domainmodel_ScreenModelParameters class attributes and methods

# domainmodel_NavigateToAction class attributes and methods

# UIActionFeature class attributes and methods

# domainmodel_ScreenFeature class attributes and methods
domainmodel_ScreenFeature_name: Property = Property(name="name", type=StringType)
domainmodel_ScreenFeature.attributes={domainmodel_ScreenFeature_name}

# domainmodel_ExecuteAction class attributes and methods

# domainmodel_SetRestCallReceiverURLParameter class attributes and methods
domainmodel_SetRestCallReceiverURLParameter_parameterType: Property = Property(name="parameterType", type=StringType)
domainmodel_SetRestCallReceiverURLParameter.attributes={domainmodel_SetRestCallReceiverURLParameter_parameterType}

# SetRestCallReceiverParameter class attributes and methods

# domainmodel_SetRestCallReceiverReturnTypeParameter class attributes and methods

# domainmodel_SetRestCallReceiverIDParameter class attributes and methods
domainmodel_SetRestCallReceiverIDParameter_parameterType: Property = Property(name="parameterType", type=StringType)
domainmodel_SetRestCallReceiverIDParameter.attributes={domainmodel_SetRestCallReceiverIDParameter_parameterType}

# domainmodel_SetRestCallReceiverParameter class attributes and methods

# domainmodel_SetRestCallReceiverParameters class attributes and methods

# domainmodel_SetRestCallReceiver class attributes and methods

# SetActionReceiver class attributes and methods

# domainmodel_MainFeatureOption class attributes and methods
domainmodel_MainFeatureOption_name: Property = Property(name="name", type=StringType)
domainmodel_MainFeatureOption.attributes={domainmodel_MainFeatureOption_name}

# domainmodel_SetActionReceiver class attributes and methods

# domainmodel_SetAction class attributes and methods

# domainmodel_InterfaceMethodCallParameter class attributes and methods
domainmodel_InterfaceMethodCallParameter_parameterType: Property = Property(name="parameterType", type=StringType)
domainmodel_InterfaceMethodCallParameter.attributes={domainmodel_InterfaceMethodCallParameter_parameterType}

# domainmodel_InterfaceMethodCallParameters class attributes and methods

# domainmodel_InterfaceMethodCall class attributes and methods

# domainmodel_BusinessFeature class attributes and methods
domainmodel_BusinessFeature_name: Property = Property(name="name", type=StringType)
domainmodel_BusinessFeature_connectPoint1: Property = Property(name="connectPoint1", type=StringType)
domainmodel_BusinessFeature_connectEnd: Property = Property(name="connectEnd", type=StringType)
domainmodel_BusinessFeature.attributes={domainmodel_BusinessFeature_connectEnd, domainmodel_BusinessFeature_name, domainmodel_BusinessFeature_connectPoint1}

# domainmodel_UIActionFeature class attributes and methods

# domainmodel_ControllerElement class attributes and methods

# domainmodel_ControllerModule class attributes and methods

# domainmodel_ScreenModule class attributes and methods

# UIFeature class attributes and methods

# domainmodel_MainFeature class attributes and methods

# domainmodel_UIFeature class attributes and methods

# domainmodel_UIModule class attributes and methods

# SystemModule class attributes and methods

# domainmodel_BusinessFeatureType class attributes and methods

# domainmodel_BusinessFeatures class attributes and methods

# BusinessModule class attributes and methods

# domainmodel_BusinessModule class attributes and methods

# domainmodel_SystemModule class attributes and methods

# domainmodel_SystemDefinition class attributes and methods

# Relationships
methodCall11: BinaryAssociation = BinaryAssociation(
    name="methodCall11",
    ends={
        Property(name="domainmodel_MethodCall12", type=domainmodel_InterfaceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InterfaceOperation", type=domainmodel_MethodCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="domainmodel_AbstractElement", type=domainmodel_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Domainmodel", type=domainmodel_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespaceElements1: BinaryAssociation = BinaryAssociation(
    name="namespaceElements1",
    ends={
        Property(name="domainmodel_AbstractNamespaceElement", type=domainmodel_NamespaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_NamespaceDeclaration", type=domainmodel_AbstractNamespaceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="domainmodel_Type", type=domainmodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Feature", type=domainmodel_Type, multiplicity=Multiplicity(0, 1))
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="domainmodel_Feature4", type=domainmodel_DomainEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_DomainEntity", type=domainmodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="domainmodel_Type6", type=domainmodel_MethodParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_MethodParameter", type=domainmodel_Type, multiplicity=Multiplicity(0, 1))
    }
)
parameters7: BinaryAssociation = BinaryAssociation(
    name="parameters7",
    ends={
        Property(name="domainmodel_MethodParameter8", type=domainmodel_MethodParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_MethodParameters", type=domainmodel_MethodParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters9: BinaryAssociation = BinaryAssociation(
    name="parameters9",
    ends={
        Property(name="domainmodel_MethodParameters10", type=domainmodel_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_MethodCall", type=domainmodel_MethodParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="domainmodel_Type15", type=domainmodel_InterfaceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InterfaceOperation14", type=domainmodel_Type, multiplicity=Multiplicity(0, 1))
    }
)
operations16: BinaryAssociation = BinaryAssociation(
    name="operations16",
    ends={
        Property(name="domainmodel_InterfaceOperation17", type=domainmodel_InterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InterfaceDeclaration", type=domainmodel_InterfaceOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceName18: BinaryAssociation = BinaryAssociation(
    name="interfaceName18",
    ends={
        Property(name="domainmodel_InterfaceDeclaration19", type=domainmodel_InterfaceOperationUsageRule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InterfaceOperationUsageRule", type=domainmodel_InterfaceDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
usageOperations20: BinaryAssociation = BinaryAssociation(
    name="usageOperations20",
    ends={
        Property(name="domainmodel_InterfaceOperationUsageRule21", type=domainmodel_InterfaceOperationsUsageRule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InterfaceOperationsUsageRule", type=domainmodel_InterfaceOperationUsageRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations22: BinaryAssociation = BinaryAssociation(
    name="operations22",
    ends={
        Property(name="domainmodel_InterfaceOperationsUsageRule23", type=domainmodel_StatelessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_StatelessComponent", type=domainmodel_InterfaceOperationsUsageRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entityType24: BinaryAssociation = BinaryAssociation(
    name="entityType24",
    ends={
        Property(name="domainmodel_DomainEntity25", type=domainmodel_DomainRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_DomainRepository", type=domainmodel_DomainEntity, multiplicity=Multiplicity(0, 1))
    }
)
operations26: BinaryAssociation = BinaryAssociation(
    name="operations26",
    ends={
        Property(name="domainmodel_InterfaceOperationsUsageRule28", type=domainmodel_DomainRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_DomainRepository27", type=domainmodel_InterfaceOperationsUsageRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryFeatures29: BinaryAssociation = BinaryAssociation(
    name="entryFeatures29",
    ends={
        Property(name="domainmodel_ModelFeature", type=domainmodel_EntryParametersModule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_EntryParametersModule", type=domainmodel_ModelFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type30: BinaryAssociation = BinaryAssociation(
    name="type30",
    ends={
        Property(name="domainmodel_Type32", type=domainmodel_ModelFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ModelFeature31", type=domainmodel_Type, multiplicity=Multiplicity(0, 1))
    }
)
modelFeatures33: BinaryAssociation = BinaryAssociation(
    name="modelFeatures33",
    ends={
        Property(name="domainmodel_ModelFeature34", type=domainmodel_ModelModule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ModelModule", type=domainmodel_ModelFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements35: BinaryAssociation = BinaryAssociation(
    name="elements35",
    ends={
        Property(name="domainmodel_ViewElement", type=domainmodel_ContainerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ContainerElement", type=domainmodel_ViewElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features36: BinaryAssociation = BinaryAssociation(
    name="features36",
    ends={
        Property(name="domainmodel_ElementFeature", type=domainmodel_ViewElement, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ViewElement37", type=domainmodel_ElementFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements38: BinaryAssociation = BinaryAssociation(
    name="elements38",
    ends={
        Property(name="domainmodel_ViewElement39", type=domainmodel_ViewModule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ViewModule", type=domainmodel_ViewElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition40: BinaryAssociation = BinaryAssociation(
    name="condition40",
    ends={
        Property(name="domainmodel_ValidatorFeature", type=domainmodel_ValidateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ValidateAction", type=domainmodel_ValidatorFeature, multiplicity=Multiplicity(0, 1))
    }
)
uiReceiver41: BinaryAssociation = BinaryAssociation(
    name="uiReceiver41",
    ends={
        Property(name="domainmodel_SetUIElementReceiver", type=domainmodel_ValidateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ValidateAction42", type=domainmodel_SetUIElementReceiver, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uiAction43: BinaryAssociation = BinaryAssociation(
    name="uiAction43",
    ends={
        Property(name="domainmodel_UIActionModule", type=domainmodel_AttachAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_AttachAction", type=domainmodel_UIActionModule, multiplicity=Multiplicity(0, 1))
    }
)
uiReceiver44: BinaryAssociation = BinaryAssociation(
    name="uiReceiver44",
    ends={
        Property(name="domainmodel_SetUIElementReceiver46", type=domainmodel_AttachAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_AttachAction45", type=domainmodel_SetUIElementReceiver, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelFeatureName47: BinaryAssociation = BinaryAssociation(
    name="modelFeatureName47",
    ends={
        Property(name="domainmodel_ModelFeature48", type=domainmodel_BindSource, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_BindSource", type=domainmodel_ModelFeature, multiplicity=Multiplicity(0, 1))
    }
)
bindSource49: BinaryAssociation = BinaryAssociation(
    name="bindSource49",
    ends={
        Property(name="domainmodel_BindSource50", type=domainmodel_BindAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_BindAction", type=domainmodel_BindSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uiReceiver51: BinaryAssociation = BinaryAssociation(
    name="uiReceiver51",
    ends={
        Property(name="domainmodel_SetUIElementReceiver53", type=domainmodel_BindAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_BindAction52", type=domainmodel_SetUIElementReceiver, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters77: BinaryAssociation = BinaryAssociation(
    name="parameters77",
    ends={
        Property(name="domainmodel_SetRestCallReceiverParameters78", type=domainmodel_SetRestCallReceiver, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_SetRestCallReceiver", type=domainmodel_SetRestCallReceiverParameters, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initActionFeatures54: BinaryAssociation = BinaryAssociation(
    name="initActionFeatures54",
    ends={
        Property(name="domainmodel_InitActionFeature", type=domainmodel_InitActionModule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InitActionModule", type=domainmodel_InitActionFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionName55: BinaryAssociation = BinaryAssociation(
    name="conditionName55",
    ends={
        Property(name="domainmodel_ValidatorFeature56", type=domainmodel_ValidatorRule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ValidatorRule", type=domainmodel_ValidatorFeature, multiplicity=Multiplicity(0, 1))
    }
)
validatorRules57: BinaryAssociation = BinaryAssociation(
    name="validatorRules57",
    ends={
        Property(name="domainmodel_ValidatorRule58", type=domainmodel_ValidatorRules, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ValidatorRules", type=domainmodel_ValidatorRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validatorRules59: BinaryAssociation = BinaryAssociation(
    name="validatorRules59",
    ends={
        Property(name="domainmodel_ValidatorRules61", type=domainmodel_ValidatorFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ValidatorFeature60", type=domainmodel_ValidatorRules, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validatorFeatures62: BinaryAssociation = BinaryAssociation(
    name="validatorFeatures62",
    ends={
        Property(name="domainmodel_ValidatorFeature63", type=domainmodel_ValidatorModule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ValidatorModule", type=domainmodel_ValidatorFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelFeatureName64: BinaryAssociation = BinaryAssociation(
    name="modelFeatureName64",
    ends={
        Property(name="domainmodel_ModelFeature65", type=domainmodel_ScreenModelParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ScreenModelParameter", type=domainmodel_ModelFeature, multiplicity=Multiplicity(0, 1))
    }
)
parameters66: BinaryAssociation = BinaryAssociation(
    name="parameters66",
    ends={
        Property(name="domainmodel_ScreenModelParameter67", type=domainmodel_ScreenModelParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ScreenModelParameters", type=domainmodel_ScreenModelParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
screenElementId68: BinaryAssociation = BinaryAssociation(
    name="screenElementId68",
    ends={
        Property(name="domainmodel_ScreenFeature", type=domainmodel_NavigateToAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_NavigateToAction", type=domainmodel_ScreenFeature, multiplicity=Multiplicity(0, 1))
    }
)
modelFeatures69: BinaryAssociation = BinaryAssociation(
    name="modelFeatures69",
    ends={
        Property(name="domainmodel_ScreenModelParameters71", type=domainmodel_NavigateToAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_NavigateToAction70", type=domainmodel_ScreenModelParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uiActionName72: BinaryAssociation = BinaryAssociation(
    name="uiActionName72",
    ends={
        Property(name="domainmodel_UIActionModule73", type=domainmodel_ExecuteAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ExecuteAction", type=domainmodel_UIActionModule, multiplicity=Multiplicity(0, 1))
    }
)
parameterType74: BinaryAssociation = BinaryAssociation(
    name="parameterType74",
    ends={
        Property(name="domainmodel_Type75", type=domainmodel_SetRestCallReceiverReturnTypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_SetRestCallReceiverReturnTypeParameter", type=domainmodel_Type, multiplicity=Multiplicity(0, 1))
    }
)
parameters76: BinaryAssociation = BinaryAssociation(
    name="parameters76",
    ends={
        Property(name="domainmodel_SetRestCallReceiverParameter", type=domainmodel_SetRestCallReceiverParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_SetRestCallReceiverParameters", type=domainmodel_SetRestCallReceiverParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
widgetName79: BinaryAssociation = BinaryAssociation(
    name="widgetName79",
    ends={
        Property(name="domainmodel_ViewElement81", type=domainmodel_SetUIElementReceiver, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_SetUIElementReceiver80", type=domainmodel_ViewElement, multiplicity=Multiplicity(0, 1))
    }
)
modelFeatureName82: BinaryAssociation = BinaryAssociation(
    name="modelFeatureName82",
    ends={
        Property(name="domainmodel_ModelFeature83", type=domainmodel_SetAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_SetAction", type=domainmodel_ModelFeature, multiplicity=Multiplicity(0, 1))
    }
)
setActionReceiver84: BinaryAssociation = BinaryAssociation(
    name="setActionReceiver84",
    ends={
        Property(name="domainmodel_SetActionReceiver", type=domainmodel_SetAction, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_SetAction85", type=domainmodel_SetActionReceiver, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterName86: BinaryAssociation = BinaryAssociation(
    name="parameterName86",
    ends={
        Property(name="domainmodel_MethodParameter87", type=domainmodel_InterfaceMethodCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InterfaceMethodCallParameter", type=domainmodel_MethodParameter, multiplicity=Multiplicity(0, 1))
    }
)
parameters88: BinaryAssociation = BinaryAssociation(
    name="parameters88",
    ends={
        Property(name="domainmodel_InterfaceMethodCallParameter89", type=domainmodel_InterfaceMethodCallParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InterfaceMethodCallParameters", type=domainmodel_InterfaceMethodCallParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceInstanceName90: BinaryAssociation = BinaryAssociation(
    name="interfaceInstanceName90",
    ends={
        Property(name="domainmodel_BusinessFeature", type=domainmodel_InterfaceMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InterfaceMethodCall", type=domainmodel_BusinessFeature, multiplicity=Multiplicity(0, 1))
    }
)
methodName91: BinaryAssociation = BinaryAssociation(
    name="methodName91",
    ends={
        Property(name="domainmodel_MethodCall93", type=domainmodel_InterfaceMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InterfaceMethodCall92", type=domainmodel_MethodCall, multiplicity=Multiplicity(0, 1))
    }
)
parameters94: BinaryAssociation = BinaryAssociation(
    name="parameters94",
    ends={
        Property(name="domainmodel_InterfaceMethodCallParameters96", type=domainmodel_InterfaceMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_InterfaceMethodCall95", type=domainmodel_InterfaceMethodCallParameters, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uiActionFeatures97: BinaryAssociation = BinaryAssociation(
    name="uiActionFeatures97",
    ends={
        Property(name="domainmodel_UIActionFeature", type=domainmodel_UIActionModule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_UIActionModule98", type=domainmodel_UIActionFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements99: BinaryAssociation = BinaryAssociation(
    name="elements99",
    ends={
        Property(name="domainmodel_ControllerElement", type=domainmodel_ControllerModule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ControllerModule", type=domainmodel_ControllerElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
screenModules100: BinaryAssociation = BinaryAssociation(
    name="screenModules100",
    ends={
        Property(name="domainmodel_ScreenModule", type=domainmodel_ScreenFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_ScreenFeature101", type=domainmodel_ScreenModule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features102: BinaryAssociation = BinaryAssociation(
    name="features102",
    ends={
        Property(name="domainmodel_MainFeatureOption", type=domainmodel_MainFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_MainFeature", type=domainmodel_MainFeatureOption, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uiFeatures103: BinaryAssociation = BinaryAssociation(
    name="uiFeatures103",
    ends={
        Property(name="domainmodel_UIFeature", type=domainmodel_UIModule, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_UIModule", type=domainmodel_UIFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type104: BinaryAssociation = BinaryAssociation(
    name="type104",
    ends={
        Property(name="domainmodel_BusinessFeatureType", type=domainmodel_BusinessFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_BusinessFeature105", type=domainmodel_BusinessFeatureType, multiplicity=Multiplicity(0, 1))
    }
)
connectPoint2107: BinaryAssociation = BinaryAssociation(
    name="connectPoint2107",
    ends={
        Property(name="domainmodel_BusinessFeature108", type=domainmodel_BusinessFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_BusinessFeature106", type=domainmodel_BusinessFeature, multiplicity=Multiplicity(0, 1))
    }
)
features109: BinaryAssociation = BinaryAssociation(
    name="features109",
    ends={
        Property(name="domainmodel_BusinessFeature110", type=domainmodel_BusinessFeatures, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_BusinessFeatures", type=domainmodel_BusinessFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules111: BinaryAssociation = BinaryAssociation(
    name="modules111",
    ends={
        Property(name="domainmodel_SystemModule", type=domainmodel_SystemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_SystemDefinition", type=domainmodel_SystemModule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_domainmodel_Import_AbstractNamespaceElement = Generalization(general=AbstractNamespaceElement, specific=domainmodel_Import)
gen_domainmodel_DataType_Type = Generalization(general=Type, specific=domainmodel_DataType)
gen_domainmodel_DataType_AbstractNamespaceElement = Generalization(general=AbstractNamespaceElement, specific=domainmodel_DataType)
gen_domainmodel_NamespaceDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_NamespaceDeclaration)
gen_domainmodel_DomainEntity_Type = Generalization(general=Type, specific=domainmodel_DomainEntity)
gen_domainmodel_DomainEntity_AbstractNamespaceElement = Generalization(general=AbstractNamespaceElement, specific=domainmodel_DomainEntity)
gen_domainmodel_InterfaceDeclaration_AbstractNamespaceElement = Generalization(general=AbstractNamespaceElement, specific=domainmodel_InterfaceDeclaration)
gen_domainmodel_InterfaceDeclaration_BusinessFeatureType = Generalization(general=BusinessFeatureType, specific=domainmodel_InterfaceDeclaration)
gen_domainmodel_StatelessComponent_AbstractNamespaceElement = Generalization(general=AbstractNamespaceElement, specific=domainmodel_StatelessComponent)
gen_domainmodel_StatelessComponent_BusinessFeatureType = Generalization(general=BusinessFeatureType, specific=domainmodel_StatelessComponent)
gen_domainmodel_DomainRepository_AbstractNamespaceElement = Generalization(general=AbstractNamespaceElement, specific=domainmodel_DomainRepository)
gen_domainmodel_DomainRepository_BusinessFeatureType = Generalization(general=BusinessFeatureType, specific=domainmodel_DomainRepository)
gen_domainmodel_EntryParametersModule_ScreenModule = Generalization(general=ScreenModule, specific=domainmodel_EntryParametersModule)
gen_domainmodel_ModelModule_ScreenModule = Generalization(general=ScreenModule, specific=domainmodel_ModelModule)
gen_domainmodel_InitActionModule_ControllerElement = Generalization(general=ControllerElement, specific=domainmodel_InitActionModule)
gen_domainmodel_ContentElement_ViewElement = Generalization(general=ViewElement, specific=domainmodel_ContentElement)
gen_domainmodel_ContainerElement_ViewElement = Generalization(general=ViewElement, specific=domainmodel_ContainerElement)
gen_domainmodel_ViewModule_ScreenModule = Generalization(general=ScreenModule, specific=domainmodel_ViewModule)
gen_domainmodel_ValidateAction_InitActionFeature = Generalization(general=InitActionFeature, specific=domainmodel_ValidateAction)
gen_domainmodel_AttachAction_InitActionFeature = Generalization(general=InitActionFeature, specific=domainmodel_AttachAction)
gen_domainmodel_BindEnumSource_BindSource = Generalization(general=BindSource, specific=domainmodel_BindEnumSource)
gen_domainmodel_BindAction_InitActionFeature = Generalization(general=InitActionFeature, specific=domainmodel_BindAction)
gen_domainmodel_ValidatorModule_ControllerElement = Generalization(general=ControllerElement, specific=domainmodel_ValidatorModule)
gen_domainmodel_NavigateToAction_UIActionFeature = Generalization(general=UIActionFeature, specific=domainmodel_NavigateToAction)
gen_domainmodel_ExecuteAction_UIActionFeature = Generalization(general=UIActionFeature, specific=domainmodel_ExecuteAction)
gen_domainmodel_SetRestCallReceiverURLParameter_SetRestCallReceiverParameter = Generalization(general=SetRestCallReceiverParameter, specific=domainmodel_SetRestCallReceiverURLParameter)
gen_domainmodel_SetRestCallReceiverReturnTypeParameter_SetRestCallReceiverParameter = Generalization(general=SetRestCallReceiverParameter, specific=domainmodel_SetRestCallReceiverReturnTypeParameter)
gen_domainmodel_SetRestCallReceiverIDParameter_SetRestCallReceiverParameter = Generalization(general=SetRestCallReceiverParameter, specific=domainmodel_SetRestCallReceiverIDParameter)
gen_domainmodel_SetRestCallReceiver_SetActionReceiver = Generalization(general=SetActionReceiver, specific=domainmodel_SetRestCallReceiver)
gen_domainmodel_SetUIElementReceiver_SetActionReceiver = Generalization(general=SetActionReceiver, specific=domainmodel_SetUIElementReceiver)
gen_domainmodel_SetAction_InitActionFeature = Generalization(general=InitActionFeature, specific=domainmodel_SetAction)
gen_domainmodel_SetAction_UIActionFeature = Generalization(general=UIActionFeature, specific=domainmodel_SetAction)
gen_domainmodel_InterfaceMethodCall_UIActionFeature = Generalization(general=UIActionFeature, specific=domainmodel_InterfaceMethodCall)
gen_domainmodel_UIActionModule_ControllerElement = Generalization(general=ControllerElement, specific=domainmodel_UIActionModule)
gen_domainmodel_ControllerModule_ScreenModule = Generalization(general=ScreenModule, specific=domainmodel_ControllerModule)
gen_domainmodel_ScreenFeature_UIFeature = Generalization(general=UIFeature, specific=domainmodel_ScreenFeature)
gen_domainmodel_MainFeature_UIFeature = Generalization(general=UIFeature, specific=domainmodel_MainFeature)
gen_domainmodel_UIModule_SystemModule = Generalization(general=SystemModule, specific=domainmodel_UIModule)
gen_domainmodel_BusinessFeatures_BusinessModule = Generalization(general=BusinessModule, specific=domainmodel_BusinessFeatures)
gen_domainmodel_BusinessModule_SystemModule = Generalization(general=SystemModule, specific=domainmodel_BusinessModule)
gen_domainmodel_SystemDefinition_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_SystemDefinition)

# Domain Model
domain_model = DomainModel(
    name="domainmodel",
    types={domainmodel_Domainmodel, domainmodel_AbstractElement, domainmodel_Type, domainmodel_Import, AbstractNamespaceElement, domainmodel_DataType, Type, domainmodel_NamespaceDeclaration, AbstractElement, domainmodel_AbstractNamespaceElement, domainmodel_Feature, domainmodel_DomainEntity, domainmodel_MethodParameter, domainmodel_MethodParameters, domainmodel_MethodCall, domainmodel_InterfaceOperation, domainmodel_InterfaceDeclaration, BusinessFeatureType, domainmodel_InterfaceOperationUsageRule, domainmodel_InterfaceOperationsUsageRule, domainmodel_StatelessComponent, domainmodel_DomainRepository, domainmodel_EntryParametersModule, ScreenModule, domainmodel_ModelFeature, domainmodel_ModelModule, domainmodel_InitActionModule, ControllerElement, domainmodel_ElementFeature, domainmodel_ContentElement, ViewElement, domainmodel_ContainerElement, domainmodel_ViewElement, domainmodel_ViewModule, domainmodel_ValidateAction, InitActionFeature, domainmodel_ValidatorFeature, domainmodel_SetUIElementReceiver, domainmodel_AttachAction, domainmodel_UIActionModule, domainmodel_BindEnumSource, BindSource, domainmodel_BindSource, domainmodel_BindAction, domainmodel_InitActionFeature, domainmodel_ValidatorRule, domainmodel_ValidatorRules, domainmodel_ValidatorModule, domainmodel_ScreenModelParameter, domainmodel_ScreenModelParameters, domainmodel_NavigateToAction, UIActionFeature, domainmodel_ScreenFeature, domainmodel_ExecuteAction, domainmodel_SetRestCallReceiverURLParameter, SetRestCallReceiverParameter, domainmodel_SetRestCallReceiverReturnTypeParameter, domainmodel_SetRestCallReceiverIDParameter, domainmodel_SetRestCallReceiverParameter, domainmodel_SetRestCallReceiverParameters, domainmodel_SetRestCallReceiver, SetActionReceiver, domainmodel_MainFeatureOption, domainmodel_SetActionReceiver, domainmodel_SetAction, domainmodel_InterfaceMethodCallParameter, domainmodel_InterfaceMethodCallParameters, domainmodel_InterfaceMethodCall, domainmodel_BusinessFeature, domainmodel_UIActionFeature, domainmodel_ControllerElement, domainmodel_ControllerModule, domainmodel_ScreenModule, UIFeature, domainmodel_MainFeature, domainmodel_UIFeature, domainmodel_UIModule, SystemModule, domainmodel_BusinessFeatureType, domainmodel_BusinessFeatures, BusinessModule, domainmodel_BusinessModule, domainmodel_SystemModule, domainmodel_SystemDefinition, ContentElementLiteral, PropertyNameLiteral, ContainerElementLiteral, UIElementReceiverKey},
    associations={methodCall11, elements0, namespaceElements1, type2, features3, type5, parameters7, parameters9, type13, operations16, interfaceName18, usageOperations20, operations22, entityType24, operations26, entryFeatures29, type30, modelFeatures33, elements35, features36, elements38, condition40, uiReceiver41, uiAction43, uiReceiver44, modelFeatureName47, bindSource49, uiReceiver51, parameters77, initActionFeatures54, conditionName55, validatorRules57, validatorRules59, validatorFeatures62, modelFeatureName64, parameters66, screenElementId68, modelFeatures69, uiActionName72, parameterType74, parameters76, widgetName79, modelFeatureName82, setActionReceiver84, parameterName86, parameters88, interfaceInstanceName90, methodName91, parameters94, uiActionFeatures97, elements99, screenModules100, features102, uiFeatures103, type104, connectPoint2107, features109, modules111},
    generalizations={gen_domainmodel_Import_AbstractNamespaceElement, gen_domainmodel_DataType_Type, gen_domainmodel_DataType_AbstractNamespaceElement, gen_domainmodel_NamespaceDeclaration_AbstractElement, gen_domainmodel_DomainEntity_Type, gen_domainmodel_DomainEntity_AbstractNamespaceElement, gen_domainmodel_InterfaceDeclaration_AbstractNamespaceElement, gen_domainmodel_InterfaceDeclaration_BusinessFeatureType, gen_domainmodel_StatelessComponent_AbstractNamespaceElement, gen_domainmodel_StatelessComponent_BusinessFeatureType, gen_domainmodel_DomainRepository_AbstractNamespaceElement, gen_domainmodel_DomainRepository_BusinessFeatureType, gen_domainmodel_EntryParametersModule_ScreenModule, gen_domainmodel_ModelModule_ScreenModule, gen_domainmodel_InitActionModule_ControllerElement, gen_domainmodel_ContentElement_ViewElement, gen_domainmodel_ContainerElement_ViewElement, gen_domainmodel_ViewModule_ScreenModule, gen_domainmodel_ValidateAction_InitActionFeature, gen_domainmodel_AttachAction_InitActionFeature, gen_domainmodel_BindEnumSource_BindSource, gen_domainmodel_BindAction_InitActionFeature, gen_domainmodel_ValidatorModule_ControllerElement, gen_domainmodel_NavigateToAction_UIActionFeature, gen_domainmodel_ExecuteAction_UIActionFeature, gen_domainmodel_SetRestCallReceiverURLParameter_SetRestCallReceiverParameter, gen_domainmodel_SetRestCallReceiverReturnTypeParameter_SetRestCallReceiverParameter, gen_domainmodel_SetRestCallReceiverIDParameter_SetRestCallReceiverParameter, gen_domainmodel_SetRestCallReceiver_SetActionReceiver, gen_domainmodel_SetUIElementReceiver_SetActionReceiver, gen_domainmodel_SetAction_InitActionFeature, gen_domainmodel_SetAction_UIActionFeature, gen_domainmodel_InterfaceMethodCall_UIActionFeature, gen_domainmodel_UIActionModule_ControllerElement, gen_domainmodel_ControllerModule_ScreenModule, gen_domainmodel_ScreenFeature_UIFeature, gen_domainmodel_MainFeature_UIFeature, gen_domainmodel_UIModule_SystemModule, gen_domainmodel_BusinessFeatures_BusinessModule, gen_domainmodel_BusinessModule_SystemModule, gen_domainmodel_SystemDefinition_AbstractElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)