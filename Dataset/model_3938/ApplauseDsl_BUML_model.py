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
RESTVerb: Enumeration = Enumeration(
    name="RESTVerb",
    literals={
            EnumerationLiteral(name="GET"),
			EnumerationLiteral(name="POST"),
			EnumerationLiteral(name="PUT"),
			EnumerationLiteral(name="DELETE")
    }
)

ScreenKind: Enumeration = Enumeration(
    name="ScreenKind",
    literals={
            EnumerationLiteral(name="DefaultList"),
			EnumerationLiteral(name="DefaultDetails")
    }
)

GestureKind: Enumeration = Enumeration(
    name="GestureKind",
    literals={
            EnumerationLiteral(name="tap"),
			EnumerationLiteral(name="swipe"),
			EnumerationLiteral(name="longpress")
    }
)

ActionVerb: Enumeration = Enumeration(
    name="ActionVerb",
    literals={
            EnumerationLiteral(name="edit"),
			EnumerationLiteral(name="display"),
			EnumerationLiteral(name="add")
    }
)

UIActionKind: Enumeration = Enumeration(
    name="UIActionKind",
    literals={
            EnumerationLiteral(name="navigate"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="performaction")
    }
)

# Classes
applauseDsl_Model = Class(name="applauseDsl::Model")
applauseDsl_NamedElement = Class(name="applauseDsl::NamedElement")
applauseDsl_Type = Class(name="applauseDsl::Type")
NamedElement = Class(name="NamedElement")
applauseDsl_DataType = Class(name="applauseDsl::DataType")
Type = Class(name="Type")
UIComponentOrDataType = Class(name="UIComponentOrDataType")
applauseDsl_Entity = Class(name="applauseDsl::Entity")
applauseDsl_Attribute = Class(name="applauseDsl::Attribute")
applauseDsl_UrlFragment = Class(name="applauseDsl::UrlFragment")
applauseDsl_Platform = Class(name="applauseDsl::Platform")
applauseDsl_PlatformMapping = Class(name="applauseDsl::PlatformMapping")
applauseDsl_TypeMapping = Class(name="applauseDsl::TypeMapping")
PlatformMapping = Class(name="PlatformMapping")
applauseDsl_DataSource = Class(name="applauseDsl::DataSource")
applauseDsl_AbsoluteRESTURL = Class(name="applauseDsl::AbsoluteRESTURL")
applauseDsl_DataSourceAccessMethod = Class(name="applauseDsl::DataSourceAccessMethod")
applauseDsl_Parameter = Class(name="applauseDsl::Parameter")
applauseDsl_RESTSpecification = Class(name="applauseDsl::RESTSpecification")
applauseDsl_RESTURL = Class(name="applauseDsl::RESTURL")
applauseDsl_DataSourceBodySpecification = Class(name="applauseDsl::DataSourceBodySpecification")
ReferrableElement = Class(name="ReferrableElement")
applauseDsl_LoopVariable = Class(name="applauseDsl::LoopVariable")
RESTURL = Class(name="RESTURL")
applauseDsl_RelativeRESTURL = Class(name="applauseDsl::RelativeRESTURL")
applauseDsl_UrlPathFragment = Class(name="applauseDsl::UrlPathFragment")
UrlFragment = Class(name="UrlFragment")
applauseDsl_Variable = Class(name="applauseDsl::Variable")
applauseDsl_Screen = Class(name="applauseDsl::Screen")
applauseDsl_DataSourceCall = Class(name="applauseDsl::DataSourceCall")
applauseDsl_ScreenSection = Class(name="applauseDsl::ScreenSection")
applauseDsl_UIAction = Class(name="applauseDsl::UIAction")
applauseDsl_ScreenSectionItems = Class(name="applauseDsl::ScreenSectionItems")
applauseDsl_ScreenListItemCell = Class(name="applauseDsl::ScreenListItemCell")
applauseDsl_ListItemCellDeclaration = Class(name="applauseDsl::ListItemCellDeclaration")
applauseDsl_RESTMethodCall = Class(name="applauseDsl::RESTMethodCall")
applauseDsl_UIComponentOrDataType = Class(name="applauseDsl::UIComponentOrDataType")
applauseDsl_UIComponentMemberConfiguration = Class(name="applauseDsl::UIComponentMemberConfiguration")
applauseDsl_ReferrableElement = Class(name="applauseDsl::ReferrableElement")
applauseDsl_UIActionSpecification = Class(name="applauseDsl::UIActionSpecification")
applauseDsl_UIActionNavigateAction = Class(name="applauseDsl::UIActionNavigateAction")
UIActionSpecification = Class(name="UIActionSpecification")
applauseDsl_UIActionDeleteAction = Class(name="applauseDsl::UIActionDeleteAction")
applauseDsl_UIComponentMemberDeclaration = Class(name="applauseDsl::UIComponentMemberDeclaration")
applauseDsl_UIComponentDeclaration = Class(name="applauseDsl::UIComponentDeclaration")
applauseDsl_UIComponentMemberCall = Class(name="applauseDsl::UIComponentMemberCall")
applauseDsl_Expression = Class(name="applauseDsl::Expression")
applauseDsl_EntityMemberCall = Class(name="applauseDsl::EntityMemberCall")
Expression = Class(name="Expression")
applauseDsl_EntityMemberCallTail = Class(name="applauseDsl::EntityMemberCallTail")
applauseDsl_AttributeReference = Class(name="applauseDsl::AttributeReference")
applauseDsl_StringLiteral = Class(name="applauseDsl::StringLiteral")

# applauseDsl_Model class attributes and methods

# applauseDsl_NamedElement class attributes and methods
applauseDsl_NamedElement_name: Property = Property(name="name", type=StringType)
applauseDsl_NamedElement.attributes={applauseDsl_NamedElement_name}

# applauseDsl_Type class attributes and methods

# NamedElement class attributes and methods

# applauseDsl_DataType class attributes and methods

# Type class attributes and methods

# UIComponentOrDataType class attributes and methods

# applauseDsl_Entity class attributes and methods
applauseDsl_Entity_abstract: Property = Property(name="abstract", type=BooleanType)
applauseDsl_Entity.attributes={applauseDsl_Entity_abstract}

# applauseDsl_Attribute class attributes and methods
applauseDsl_Attribute_many: Property = Property(name="many", type=BooleanType)
applauseDsl_Attribute_name: Property = Property(name="name", type=StringType)
applauseDsl_Attribute.attributes={applauseDsl_Attribute_many, applauseDsl_Attribute_name}

# applauseDsl_UrlFragment class attributes and methods

# applauseDsl_Platform class attributes and methods

# applauseDsl_PlatformMapping class attributes and methods

# applauseDsl_TypeMapping class attributes and methods
applauseDsl_TypeMapping_simpleName: Property = Property(name="simpleName", type=StringType)
applauseDsl_TypeMapping.attributes={applauseDsl_TypeMapping_simpleName}

# PlatformMapping class attributes and methods

# applauseDsl_DataSource class attributes and methods

# applauseDsl_AbsoluteRESTURL class attributes and methods
applauseDsl_AbsoluteRESTURL_port: Property = Property(name="port", type=IntegerType)
applauseDsl_AbsoluteRESTURL.attributes={applauseDsl_AbsoluteRESTURL_port}

# applauseDsl_DataSourceAccessMethod class attributes and methods
applauseDsl_DataSourceAccessMethod_name: Property = Property(name="name", type=StringType)
applauseDsl_DataSourceAccessMethod_returnsMany: Property = Property(name="returnsMany", type=BooleanType)
applauseDsl_DataSourceAccessMethod.attributes={applauseDsl_DataSourceAccessMethod_name, applauseDsl_DataSourceAccessMethod_returnsMany}

# applauseDsl_Parameter class attributes and methods

# applauseDsl_RESTSpecification class attributes and methods
applauseDsl_RESTSpecification_verb: Property = Property(name="verb", type=StringType)
applauseDsl_RESTSpecification.attributes={applauseDsl_RESTSpecification_verb}

# applauseDsl_RESTURL class attributes and methods

# applauseDsl_DataSourceBodySpecification class attributes and methods

# ReferrableElement class attributes and methods

# applauseDsl_LoopVariable class attributes and methods

# RESTURL class attributes and methods

# applauseDsl_RelativeRESTURL class attributes and methods

# applauseDsl_UrlPathFragment class attributes and methods
applauseDsl_UrlPathFragment_name: Property = Property(name="name", type=StringType)
applauseDsl_UrlPathFragment.attributes={applauseDsl_UrlPathFragment_name}

# UrlFragment class attributes and methods

# applauseDsl_Variable class attributes and methods

# applauseDsl_Screen class attributes and methods
applauseDsl_Screen_kind: Property = Property(name="kind", type=StringType)
applauseDsl_Screen_title: Property = Property(name="title", type=StringType)
applauseDsl_Screen.attributes={applauseDsl_Screen_kind, applauseDsl_Screen_title}

# applauseDsl_DataSourceCall class attributes and methods
applauseDsl_DataSourceCall_name: Property = Property(name="name", type=StringType)
applauseDsl_DataSourceCall.attributes={applauseDsl_DataSourceCall_name}

# applauseDsl_ScreenSection class attributes and methods
applauseDsl_ScreenSection_title: Property = Property(name="title", type=StringType)
applauseDsl_ScreenSection.attributes={applauseDsl_ScreenSection_title}

# applauseDsl_UIAction class attributes and methods
applauseDsl_UIAction_title: Property = Property(name="title", type=StringType)
applauseDsl_UIAction_icon: Property = Property(name="icon", type=StringType)
applauseDsl_UIAction_gesture: Property = Property(name="gesture", type=StringType)
applauseDsl_UIAction_order: Property = Property(name="order", type=IntegerType)
applauseDsl_UIAction.attributes={applauseDsl_UIAction_order, applauseDsl_UIAction_gesture, applauseDsl_UIAction_icon, applauseDsl_UIAction_title}

# applauseDsl_ScreenSectionItems class attributes and methods

# applauseDsl_ScreenListItemCell class attributes and methods

# applauseDsl_ListItemCellDeclaration class attributes and methods

# applauseDsl_RESTMethodCall class attributes and methods

# applauseDsl_UIComponentOrDataType class attributes and methods

# applauseDsl_UIComponentMemberConfiguration class attributes and methods

# applauseDsl_ReferrableElement class attributes and methods
applauseDsl_ReferrableElement_name: Property = Property(name="name", type=StringType)
applauseDsl_ReferrableElement.attributes={applauseDsl_ReferrableElement_name}

# applauseDsl_UIActionSpecification class attributes and methods

# applauseDsl_UIActionNavigateAction class attributes and methods
applauseDsl_UIActionNavigateAction_actionVerb: Property = Property(name="actionVerb", type=StringType)
applauseDsl_UIActionNavigateAction.attributes={applauseDsl_UIActionNavigateAction_actionVerb}

# UIActionSpecification class attributes and methods

# applauseDsl_UIActionDeleteAction class attributes and methods

# applauseDsl_UIComponentMemberDeclaration class attributes and methods
applauseDsl_UIComponentMemberDeclaration_name: Property = Property(name="name", type=StringType)
applauseDsl_UIComponentMemberDeclaration.attributes={applauseDsl_UIComponentMemberDeclaration_name}

# applauseDsl_UIComponentDeclaration class attributes and methods

# applauseDsl_UIComponentMemberCall class attributes and methods

# applauseDsl_Expression class attributes and methods

# applauseDsl_EntityMemberCall class attributes and methods

# Expression class attributes and methods

# applauseDsl_EntityMemberCallTail class attributes and methods

# applauseDsl_AttributeReference class attributes and methods

# applauseDsl_StringLiteral class attributes and methods
applauseDsl_StringLiteral_value: Property = Property(name="value", type=StringType)
applauseDsl_StringLiteral.attributes={applauseDsl_StringLiteral_value}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="applauseDsl_NamedElement", type=applauseDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Model", type=applauseDsl_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="applauseDsl_Entity", type=applauseDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Entity1", type=applauseDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="applauseDsl_Attribute", type=applauseDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Entity4", type=applauseDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="applauseDsl_Type", type=applauseDsl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Attribute6", type=applauseDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
fragments29: BinaryAssociation = BinaryAssociation(
    name="fragments29",
    ends={
        Property(name="applauseDsl_UrlFragment", type=applauseDsl_RESTURL, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_RESTURL30", type=applauseDsl_UrlFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings7: BinaryAssociation = BinaryAssociation(
    name="mappings7",
    ends={
        Property(name="applauseDsl_PlatformMapping", type=applauseDsl_Platform, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Platform", type=applauseDsl_PlatformMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="applauseDsl_DataType", type=applauseDsl_TypeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TypeMapping", type=applauseDsl_DataType, multiplicity=Multiplicity(0, 1))
    }
)
baseUrl9: BinaryAssociation = BinaryAssociation(
    name="baseUrl9",
    ends={
        Property(name="applauseDsl_AbsoluteRESTURL", type=applauseDsl_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_DataSource", type=applauseDsl_AbsoluteRESTURL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceType10: BinaryAssociation = BinaryAssociation(
    name="resourceType10",
    ends={
        Property(name="applauseDsl_Entity12", type=applauseDsl_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_DataSource11", type=applauseDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
methods13: BinaryAssociation = BinaryAssociation(
    name="methods13",
    ends={
        Property(name="applauseDsl_DataSourceAccessMethod", type=applauseDsl_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_DataSource14", type=applauseDsl_DataSourceAccessMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaredParameters15: BinaryAssociation = BinaryAssociation(
    name="declaredParameters15",
    ends={
        Property(name="applauseDsl_Parameter", type=applauseDsl_DataSourceAccessMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_DataSourceAccessMethod16", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
restSpecification17: BinaryAssociation = BinaryAssociation(
    name="restSpecification17",
    ends={
        Property(name="applauseDsl_RESTSpecification", type=applauseDsl_DataSourceAccessMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_DataSourceAccessMethod18", type=applauseDsl_RESTSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path19: BinaryAssociation = BinaryAssociation(
    name="path19",
    ends={
        Property(name="applauseDsl_RESTURL", type=applauseDsl_RESTSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_RESTSpecification20", type=applauseDsl_RESTURL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body21: BinaryAssociation = BinaryAssociation(
    name="body21",
    ends={
        Property(name="applauseDsl_DataSourceBodySpecification", type=applauseDsl_RESTSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_RESTSpecification22", type=applauseDsl_DataSourceBodySpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodycontents23: BinaryAssociation = BinaryAssociation(
    name="bodycontents23",
    ends={
        Property(name="applauseDsl_Parameter25", type=applauseDsl_DataSourceBodySpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_DataSourceBodySpecification24", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="applauseDsl_Type28", type=applauseDsl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Parameter27", type=applauseDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
variable55: BinaryAssociation = BinaryAssociation(
    name="variable55",
    ends={
        Property(name="applauseDsl_LoopVariable", type=applauseDsl_ScreenListItemCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ScreenListItemCell56", type=applauseDsl_LoopVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
host31: BinaryAssociation = BinaryAssociation(
    name="host31",
    ends={
        Property(name="applauseDsl_UrlFragment33", type=applauseDsl_AbsoluteRESTURL, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_AbsoluteRESTURL32", type=applauseDsl_UrlFragment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterReference34: BinaryAssociation = BinaryAssociation(
    name="parameterReference34",
    ends={
        Property(name="applauseDsl_Parameter35", type=applauseDsl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Variable", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
inputParameter36: BinaryAssociation = BinaryAssociation(
    name="inputParameter36",
    ends={
        Property(name="applauseDsl_Parameter37", type=applauseDsl_Screen, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Screen", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
datasource38: BinaryAssociation = BinaryAssociation(
    name="datasource38",
    ends={
        Property(name="applauseDsl_DataSourceCall", type=applauseDsl_Screen, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Screen39", type=applauseDsl_DataSourceCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections40: BinaryAssociation = BinaryAssociation(
    name="sections40",
    ends={
        Property(name="applauseDsl_ScreenSection", type=applauseDsl_Screen, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Screen41", type=applauseDsl_ScreenSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions42: BinaryAssociation = BinaryAssociation(
    name="actions42",
    ends={
        Property(name="applauseDsl_UIAction", type=applauseDsl_Screen, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Screen43", type=applauseDsl_UIAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datasource44: BinaryAssociation = BinaryAssociation(
    name="datasource44",
    ends={
        Property(name="applauseDsl_DataSourceCall46", type=applauseDsl_ScreenSection, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ScreenSection45", type=applauseDsl_DataSourceCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items47: BinaryAssociation = BinaryAssociation(
    name="items47",
    ends={
        Property(name="applauseDsl_ScreenSectionItems", type=applauseDsl_ScreenSection, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ScreenSection48", type=applauseDsl_ScreenSectionItems, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items49: BinaryAssociation = BinaryAssociation(
    name="items49",
    ends={
        Property(name="applauseDsl_ScreenListItemCell", type=applauseDsl_ScreenSectionItems, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ScreenSectionItems50", type=applauseDsl_ScreenListItemCell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type51: BinaryAssociation = BinaryAssociation(
    name="type51",
    ends={
        Property(name="applauseDsl_ListItemCellDeclaration", type=applauseDsl_ScreenListItemCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ScreenListItemCell52", type=applauseDsl_ListItemCellDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
restMethod53: BinaryAssociation = BinaryAssociation(
    name="restMethod53",
    ends={
        Property(name="applauseDsl_RESTMethodCall", type=applauseDsl_ScreenListItemCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ScreenListItemCell54", type=applauseDsl_RESTMethodCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type72: BinaryAssociation = BinaryAssociation(
    name="type72",
    ends={
        Property(name="applauseDsl_UIComponentOrDataType", type=applauseDsl_UIComponentMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_UIComponentMemberDeclaration73", type=applauseDsl_UIComponentOrDataType, multiplicity=Multiplicity(0, 1))
    }
)
configurations57: BinaryAssociation = BinaryAssociation(
    name="configurations57",
    ends={
        Property(name="applauseDsl_UIComponentMemberConfiguration", type=applauseDsl_ScreenListItemCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ScreenListItemCell58", type=applauseDsl_UIComponentMemberConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions59: BinaryAssociation = BinaryAssociation(
    name="actions59",
    ends={
        Property(name="applauseDsl_UIAction61", type=applauseDsl_ScreenListItemCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ScreenListItemCell60", type=applauseDsl_UIAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action62: BinaryAssociation = BinaryAssociation(
    name="action62",
    ends={
        Property(name="applauseDsl_UIActionSpecification", type=applauseDsl_UIAction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_UIAction63", type=applauseDsl_UIActionSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetScreen64: BinaryAssociation = BinaryAssociation(
    name="targetScreen64",
    ends={
        Property(name="applauseDsl_Screen65", type=applauseDsl_UIActionNavigateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_UIActionNavigateAction", type=applauseDsl_Screen, multiplicity=Multiplicity(0, 1))
    }
)
variable66: BinaryAssociation = BinaryAssociation(
    name="variable66",
    ends={
        Property(name="applauseDsl_ReferrableElement", type=applauseDsl_UIActionNavigateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_UIActionNavigateAction67", type=applauseDsl_ReferrableElement, multiplicity=Multiplicity(0, 1))
    }
)
members68: BinaryAssociation = BinaryAssociation(
    name="members68",
    ends={
        Property(name="applauseDsl_UIComponentMemberDeclaration", type=applauseDsl_ListItemCellDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ListItemCellDeclaration69", type=applauseDsl_UIComponentMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members70: BinaryAssociation = BinaryAssociation(
    name="members70",
    ends={
        Property(name="applauseDsl_UIComponentMemberDeclaration71", type=applauseDsl_UIComponentDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_UIComponentDeclaration", type=applauseDsl_UIComponentMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datasource74: BinaryAssociation = BinaryAssociation(
    name="datasource74",
    ends={
        Property(name="applauseDsl_DataSourceCall76", type=applauseDsl_RESTMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_RESTMethodCall75", type=applauseDsl_DataSourceCall, multiplicity=Multiplicity(0, 1))
    }
)
restMethod77: BinaryAssociation = BinaryAssociation(
    name="restMethod77",
    ends={
        Property(name="applauseDsl_DataSourceAccessMethod79", type=applauseDsl_RESTMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_RESTMethodCall78", type=applauseDsl_DataSourceAccessMethod, multiplicity=Multiplicity(0, 1))
    }
)
datasource80: BinaryAssociation = BinaryAssociation(
    name="datasource80",
    ends={
        Property(name="applauseDsl_DataSource82", type=applauseDsl_DataSourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_DataSourceCall81", type=applauseDsl_DataSource, multiplicity=Multiplicity(0, 1))
    }
)
type83: BinaryAssociation = BinaryAssociation(
    name="type83",
    ends={
        Property(name="applauseDsl_UIComponentMemberCall", type=applauseDsl_UIComponentMemberConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_UIComponentMemberConfiguration84", type=applauseDsl_UIComponentMemberCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value85: BinaryAssociation = BinaryAssociation(
    name="value85",
    ends={
        Property(name="applauseDsl_Expression", type=applauseDsl_UIComponentMemberConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_UIComponentMemberConfiguration86", type=applauseDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
component87: BinaryAssociation = BinaryAssociation(
    name="component87",
    ends={
        Property(name="applauseDsl_UIComponentMemberDeclaration89", type=applauseDsl_UIComponentMemberCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_UIComponentMemberCall88", type=applauseDsl_UIComponentMemberDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
member90: BinaryAssociation = BinaryAssociation(
    name="member90",
    ends={
        Property(name="applauseDsl_UIComponentMemberDeclaration92", type=applauseDsl_UIComponentMemberCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_UIComponentMemberCall91", type=applauseDsl_UIComponentMemberDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
head93: BinaryAssociation = BinaryAssociation(
    name="head93",
    ends={
        Property(name="applauseDsl_Attribute94", type=applauseDsl_EntityMemberCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_EntityMemberCall", type=applauseDsl_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
tail95: BinaryAssociation = BinaryAssociation(
    name="tail95",
    ends={
        Property(name="applauseDsl_EntityMemberCallTail", type=applauseDsl_EntityMemberCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_EntityMemberCall96", type=applauseDsl_EntityMemberCallTail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
head97: BinaryAssociation = BinaryAssociation(
    name="head97",
    ends={
        Property(name="applauseDsl_Attribute99", type=applauseDsl_EntityMemberCallTail, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_EntityMemberCallTail98", type=applauseDsl_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
tail101: BinaryAssociation = BinaryAssociation(
    name="tail101",
    ends={
        Property(name="applauseDsl_EntityMemberCallTail102", type=applauseDsl_EntityMemberCallTail, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_EntityMemberCallTail100", type=applauseDsl_EntityMemberCallTail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value103: BinaryAssociation = BinaryAssociation(
    name="value103",
    ends={
        Property(name="applauseDsl_Attribute104", type=applauseDsl_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_AttributeReference", type=applauseDsl_Attribute, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_applauseDsl_Type_NamedElement = Generalization(general=NamedElement, specific=applauseDsl_Type)
gen_applauseDsl_DataType_Type = Generalization(general=Type, specific=applauseDsl_DataType)
gen_applauseDsl_DataType_UIComponentOrDataType = Generalization(general=UIComponentOrDataType, specific=applauseDsl_DataType)
gen_applauseDsl_Entity_Type = Generalization(general=Type, specific=applauseDsl_Entity)
gen_applauseDsl_Platform_NamedElement = Generalization(general=NamedElement, specific=applauseDsl_Platform)
gen_applauseDsl_TypeMapping_PlatformMapping = Generalization(general=PlatformMapping, specific=applauseDsl_TypeMapping)
gen_applauseDsl_DataSource_NamedElement = Generalization(general=NamedElement, specific=applauseDsl_DataSource)
gen_applauseDsl_Parameter_ReferrableElement = Generalization(general=ReferrableElement, specific=applauseDsl_Parameter)
gen_applauseDsl_AbsoluteRESTURL_RESTURL = Generalization(general=RESTURL, specific=applauseDsl_AbsoluteRESTURL)
gen_applauseDsl_RelativeRESTURL_RESTURL = Generalization(general=RESTURL, specific=applauseDsl_RelativeRESTURL)
gen_applauseDsl_UrlPathFragment_UrlFragment = Generalization(general=UrlFragment, specific=applauseDsl_UrlPathFragment)
gen_applauseDsl_Variable_UrlFragment = Generalization(general=UrlFragment, specific=applauseDsl_Variable)
gen_applauseDsl_Screen_NamedElement = Generalization(general=NamedElement, specific=applauseDsl_Screen)
gen_applauseDsl_LoopVariable_ReferrableElement = Generalization(general=ReferrableElement, specific=applauseDsl_LoopVariable)
gen_applauseDsl_UIActionNavigateAction_UIActionSpecification = Generalization(general=UIActionSpecification, specific=applauseDsl_UIActionNavigateAction)
gen_applauseDsl_UIActionDeleteAction_UIActionSpecification = Generalization(general=UIActionSpecification, specific=applauseDsl_UIActionDeleteAction)
gen_applauseDsl_ListItemCellDeclaration_NamedElement = Generalization(general=NamedElement, specific=applauseDsl_ListItemCellDeclaration)
gen_applauseDsl_UIComponentDeclaration_NamedElement = Generalization(general=NamedElement, specific=applauseDsl_UIComponentDeclaration)
gen_applauseDsl_UIComponentDeclaration_UIComponentOrDataType = Generalization(general=UIComponentOrDataType, specific=applauseDsl_UIComponentDeclaration)
gen_applauseDsl_EntityMemberCall_Expression = Generalization(general=Expression, specific=applauseDsl_EntityMemberCall)
gen_applauseDsl_StringLiteral_Expression = Generalization(general=Expression, specific=applauseDsl_StringLiteral)

# Domain Model
domain_model = DomainModel(
    name="applauseDsl",
    types={applauseDsl_Model, applauseDsl_NamedElement, applauseDsl_Type, NamedElement, applauseDsl_DataType, Type, UIComponentOrDataType, applauseDsl_Entity, applauseDsl_Attribute, applauseDsl_UrlFragment, applauseDsl_Platform, applauseDsl_PlatformMapping, applauseDsl_TypeMapping, PlatformMapping, applauseDsl_DataSource, applauseDsl_AbsoluteRESTURL, applauseDsl_DataSourceAccessMethod, applauseDsl_Parameter, applauseDsl_RESTSpecification, applauseDsl_RESTURL, applauseDsl_DataSourceBodySpecification, ReferrableElement, applauseDsl_LoopVariable, RESTURL, applauseDsl_RelativeRESTURL, applauseDsl_UrlPathFragment, UrlFragment, applauseDsl_Variable, applauseDsl_Screen, applauseDsl_DataSourceCall, applauseDsl_ScreenSection, applauseDsl_UIAction, applauseDsl_ScreenSectionItems, applauseDsl_ScreenListItemCell, applauseDsl_ListItemCellDeclaration, applauseDsl_RESTMethodCall, applauseDsl_UIComponentOrDataType, applauseDsl_UIComponentMemberConfiguration, applauseDsl_ReferrableElement, applauseDsl_UIActionSpecification, applauseDsl_UIActionNavigateAction, UIActionSpecification, applauseDsl_UIActionDeleteAction, applauseDsl_UIComponentMemberDeclaration, applauseDsl_UIComponentDeclaration, applauseDsl_UIComponentMemberCall, applauseDsl_Expression, applauseDsl_EntityMemberCall, Expression, applauseDsl_EntityMemberCallTail, applauseDsl_AttributeReference, applauseDsl_StringLiteral, RESTVerb, ScreenKind, GestureKind, ActionVerb, UIActionKind},
    associations={elements0, superType2, attributes3, type5, fragments29, mappings7, type8, baseUrl9, resourceType10, methods13, declaredParameters15, restSpecification17, path19, body21, bodycontents23, type26, variable55, host31, parameterReference34, inputParameter36, datasource38, sections40, actions42, datasource44, items47, items49, type51, restMethod53, type72, configurations57, actions59, action62, targetScreen64, variable66, members68, members70, datasource74, restMethod77, datasource80, type83, value85, component87, member90, head93, tail95, head97, tail101, value103},
    generalizations={gen_applauseDsl_Type_NamedElement, gen_applauseDsl_DataType_Type, gen_applauseDsl_DataType_UIComponentOrDataType, gen_applauseDsl_Entity_Type, gen_applauseDsl_Platform_NamedElement, gen_applauseDsl_TypeMapping_PlatformMapping, gen_applauseDsl_DataSource_NamedElement, gen_applauseDsl_Parameter_ReferrableElement, gen_applauseDsl_AbsoluteRESTURL_RESTURL, gen_applauseDsl_RelativeRESTURL_RESTURL, gen_applauseDsl_UrlPathFragment_UrlFragment, gen_applauseDsl_Variable_UrlFragment, gen_applauseDsl_Screen_NamedElement, gen_applauseDsl_LoopVariable_ReferrableElement, gen_applauseDsl_UIActionNavigateAction_UIActionSpecification, gen_applauseDsl_UIActionDeleteAction_UIActionSpecification, gen_applauseDsl_ListItemCellDeclaration_NamedElement, gen_applauseDsl_UIComponentDeclaration_NamedElement, gen_applauseDsl_UIComponentDeclaration_UIComponentOrDataType, gen_applauseDsl_EntityMemberCall_Expression, gen_applauseDsl_StringLiteral_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)