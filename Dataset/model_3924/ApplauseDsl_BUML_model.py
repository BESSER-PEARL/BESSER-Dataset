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
CellType: Enumeration = Enumeration(
    name="CellType",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="defaultWithDisclosure"),
			EnumerationLiteral(name="value2"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="subtitle"),
			EnumerationLiteral(name="maps")
    }
)

Position: Enumeration = Enumeration(
    name="Position",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="center"),
			EnumerationLiteral(name="right")
    }
)

# Classes
applauseDsl_ApplauseModel = Class(name="applauseDsl::ApplauseModel")
applauseDsl_Application = Class(name="applauseDsl::Application")
applauseDsl_ModelElement = Class(name="applauseDsl::ModelElement")
applauseDsl_Expression = Class(name="applauseDsl::Expression")
applauseDsl_CollectionExpression = Class(name="applauseDsl::CollectionExpression")
applauseDsl_StringLiteral = Class(name="applauseDsl::StringLiteral")
applauseDsl_PredefinedParameter = Class(name="applauseDsl::PredefinedParameter")
applauseDsl_SectionId = Class(name="applauseDsl::SectionId")
PredefinedParameter = Class(name="PredefinedParameter")
applauseDsl_StringFunction = Class(name="applauseDsl::StringFunction")
applauseDsl_CollectionLiteral = Class(name="applauseDsl::CollectionLiteral")
applauseDsl_NavigationBarItem = Class(name="applauseDsl::NavigationBarItem")
ModelElement = Class(name="ModelElement")
applauseDsl_ScalarExpression = Class(name="applauseDsl::ScalarExpression")
applauseDsl_VariableDeclaration = Class(name="applauseDsl::VariableDeclaration")
applauseDsl_TypeDescription = Class(name="applauseDsl::TypeDescription")
applauseDsl_Type = Class(name="applauseDsl::Type")
applauseDsl_Parameter = Class(name="applauseDsl::Parameter")
VariableDeclaration = Class(name="VariableDeclaration")
applauseDsl_ObjectReference = Class(name="applauseDsl::ObjectReference")
Expression = Class(name="Expression")
ScalarExpression = Class(name="ScalarExpression")
CollectionExpression = Class(name="CollectionExpression")
applauseDsl_Entity = Class(name="applauseDsl::Entity")
applauseDsl_Property = Class(name="applauseDsl::Property")
applauseDsl_ContentProvider = Class(name="applauseDsl::ContentProvider")
applauseDsl_CollectionFunction = Class(name="applauseDsl::CollectionFunction")
applauseDsl_ViewCall = Class(name="applauseDsl::ViewCall")
applauseDsl_Button = Class(name="applauseDsl::Button")
applauseDsl_SimpleType = Class(name="applauseDsl::SimpleType")
Type = Class(name="Type")
applauseDsl_ViewForAllSections = Class(name="applauseDsl::ViewForAllSections")
applauseDsl_ViewSection = Class(name="applauseDsl::ViewSection")
applauseDsl_TableView = Class(name="applauseDsl::TableView")
SectionedView = Class(name="SectionedView")
applauseDsl_DetailsView = Class(name="applauseDsl::DetailsView")
applauseDsl_ViewHeader = Class(name="applauseDsl::ViewHeader")
applauseDsl_WebView = Class(name="applauseDsl::WebView")
applauseDsl_ProviderConstruction = Class(name="applauseDsl::ProviderConstruction")
applauseDsl_View = Class(name="applauseDsl::View")
applauseDsl_SectionedView = Class(name="applauseDsl::SectionedView")
View = Class(name="View")
applauseDsl_CollectionIterator = Class(name="applauseDsl::CollectionIterator")
applauseDsl_CustomView = Class(name="applauseDsl::CustomView")
applauseDsl_SectionCell = Class(name="applauseDsl::SectionCell")
applauseDsl_StringConcat = Class(name="applauseDsl::StringConcat")
StringFunction = Class(name="StringFunction")
applauseDsl_StringReplace = Class(name="applauseDsl::StringReplace")
applauseDsl_ViewAction = Class(name="applauseDsl::ViewAction")
applauseDsl_ActionDelegate = Class(name="applauseDsl::ActionDelegate")
ViewAction = Class(name="ViewAction")
applauseDsl_ExternalOpen = Class(name="applauseDsl::ExternalOpen")
applauseDsl_StringUrlConform = Class(name="applauseDsl::StringUrlConform")
applauseDsl_StringSplit = Class(name="applauseDsl::StringSplit")
CollectionFunction = Class(name="CollectionFunction")
applauseDsl_Constant = Class(name="applauseDsl::Constant")

# applauseDsl_ApplauseModel class attributes and methods

# applauseDsl_Application class attributes and methods
applauseDsl_Application_tabbarApplication: Property = Property(name="tabbarApplication", type=BooleanType)
applauseDsl_Application_name: Property = Property(name="name", type=StringType)
applauseDsl_Application.attributes={applauseDsl_Application_name, applauseDsl_Application_tabbarApplication}

# applauseDsl_ModelElement class attributes and methods

# applauseDsl_Expression class attributes and methods

# applauseDsl_CollectionExpression class attributes and methods

# applauseDsl_StringLiteral class attributes and methods
applauseDsl_StringLiteral_value: Property = Property(name="value", type=StringType)
applauseDsl_StringLiteral.attributes={applauseDsl_StringLiteral_value}

# applauseDsl_PredefinedParameter class attributes and methods

# applauseDsl_SectionId class attributes and methods

# PredefinedParameter class attributes and methods

# applauseDsl_StringFunction class attributes and methods

# applauseDsl_CollectionLiteral class attributes and methods

# applauseDsl_NavigationBarItem class attributes and methods
applauseDsl_NavigationBarItem_position: Property = Property(name="position", type=StringType)
applauseDsl_NavigationBarItem.attributes={applauseDsl_NavigationBarItem_position}

# ModelElement class attributes and methods

# applauseDsl_ScalarExpression class attributes and methods

# applauseDsl_VariableDeclaration class attributes and methods
applauseDsl_VariableDeclaration_name: Property = Property(name="name", type=StringType)
applauseDsl_VariableDeclaration.attributes={applauseDsl_VariableDeclaration_name}

# applauseDsl_TypeDescription class attributes and methods
applauseDsl_TypeDescription_many: Property = Property(name="many", type=BooleanType)
applauseDsl_TypeDescription.attributes={applauseDsl_TypeDescription_many}

# applauseDsl_Type class attributes and methods
applauseDsl_Type_name: Property = Property(name="name", type=StringType)
applauseDsl_Type.attributes={applauseDsl_Type_name}

# applauseDsl_Parameter class attributes and methods

# VariableDeclaration class attributes and methods

# applauseDsl_ObjectReference class attributes and methods

# Expression class attributes and methods

# ScalarExpression class attributes and methods

# CollectionExpression class attributes and methods

# applauseDsl_Entity class attributes and methods

# applauseDsl_Property class attributes and methods
applauseDsl_Property_derived: Property = Property(name="derived", type=BooleanType)
applauseDsl_Property.attributes={applauseDsl_Property_derived}

# applauseDsl_ContentProvider class attributes and methods
applauseDsl_ContentProvider_name: Property = Property(name="name", type=StringType)
applauseDsl_ContentProvider_resolver: Property = Property(name="resolver", type=BooleanType)
applauseDsl_ContentProvider_many: Property = Property(name="many", type=BooleanType)
applauseDsl_ContentProvider_xml: Property = Property(name="xml", type=BooleanType)
applauseDsl_ContentProvider_html: Property = Property(name="html", type=BooleanType)
applauseDsl_ContentProvider.attributes={applauseDsl_ContentProvider_resolver, applauseDsl_ContentProvider_xml, applauseDsl_ContentProvider_name, applauseDsl_ContentProvider_many, applauseDsl_ContentProvider_html}

# applauseDsl_CollectionFunction class attributes and methods

# applauseDsl_ViewCall class attributes and methods

# applauseDsl_Button class attributes and methods
applauseDsl_Button_handler: Property = Property(name="handler", type=StringType)
applauseDsl_Button.attributes={applauseDsl_Button_handler}

# applauseDsl_SimpleType class attributes and methods
applauseDsl_SimpleType_platformType: Property = Property(name="platformType", type=StringType)
applauseDsl_SimpleType.attributes={applauseDsl_SimpleType_platformType}

# Type class attributes and methods

# applauseDsl_ViewForAllSections class attributes and methods

# applauseDsl_ViewSection class attributes and methods

# applauseDsl_TableView class attributes and methods

# SectionedView class attributes and methods

# applauseDsl_DetailsView class attributes and methods

# applauseDsl_ViewHeader class attributes and methods

# applauseDsl_WebView class attributes and methods

# applauseDsl_ProviderConstruction class attributes and methods

# applauseDsl_View class attributes and methods
applauseDsl_View_name: Property = Property(name="name", type=StringType)
applauseDsl_View.attributes={applauseDsl_View_name}

# applauseDsl_SectionedView class attributes and methods

# View class attributes and methods

# applauseDsl_CollectionIterator class attributes and methods

# applauseDsl_CustomView class attributes and methods
applauseDsl_CustomView_objclass: Property = Property(name="objclass", type=StringType)
applauseDsl_CustomView.attributes={applauseDsl_CustomView_objclass}

# applauseDsl_SectionCell class attributes and methods
applauseDsl_SectionCell_type: Property = Property(name="type", type=StringType)
applauseDsl_SectionCell.attributes={applauseDsl_SectionCell_type}

# applauseDsl_StringConcat class attributes and methods

# StringFunction class attributes and methods

# applauseDsl_StringReplace class attributes and methods

# applauseDsl_ViewAction class attributes and methods

# applauseDsl_ActionDelegate class attributes and methods

# ViewAction class attributes and methods

# applauseDsl_ExternalOpen class attributes and methods

# applauseDsl_StringUrlConform class attributes and methods

# applauseDsl_StringSplit class attributes and methods

# CollectionFunction class attributes and methods

# applauseDsl_Constant class attributes and methods
applauseDsl_Constant_language: Property = Property(name="language", type=StringType)
applauseDsl_Constant.attributes={applauseDsl_Constant_language}

# Relationships
application0: BinaryAssociation = BinaryAssociation(
    name="application0",
    ends={
        Property(name="applauseDsl_Application", type=applauseDsl_ApplauseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ApplauseModel", type=applauseDsl_Application, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tail12: BinaryAssociation = BinaryAssociation(
    name="tail12",
    ends={
        Property(name="applauseDsl_ObjectReference13", type=applauseDsl_ObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ObjectReference11", type=applauseDsl_ObjectReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items14: BinaryAssociation = BinaryAssociation(
    name="items14",
    ends={
        Property(name="applauseDsl_ScalarExpression15", type=applauseDsl_CollectionLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_CollectionLiteral", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="applauseDsl_ModelElement", type=applauseDsl_ApplauseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ApplauseModel2", type=applauseDsl_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icon3: BinaryAssociation = BinaryAssociation(
    name="icon3",
    ends={
        Property(name="applauseDsl_ScalarExpression", type=applauseDsl_NavigationBarItem, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_NavigationBarItem", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggers4: BinaryAssociation = BinaryAssociation(
    name="triggers4",
    ends={
        Property(name="applauseDsl_ScalarExpression6", type=applauseDsl_NavigationBarItem, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_NavigationBarItem5", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="applauseDsl_Type", type=applauseDsl_TypeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TypeDescription", type=applauseDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
description8: BinaryAssociation = BinaryAssociation(
    name="description8",
    ends={
        Property(name="applauseDsl_TypeDescription9", type=applauseDsl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Parameter", type=applauseDsl_TypeDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object10: BinaryAssociation = BinaryAssociation(
    name="object10",
    ends={
        Property(name="applauseDsl_VariableDeclaration", type=applauseDsl_ObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ObjectReference", type=applauseDsl_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
extends36: BinaryAssociation = BinaryAssociation(
    name="extends36",
    ends={
        Property(name="applauseDsl_Entity", type=applauseDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Entity35", type=applauseDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
properties37: BinaryAssociation = BinaryAssociation(
    name="properties37",
    ends={
        Property(name="applauseDsl_Property", type=applauseDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Entity38", type=applauseDsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description39: BinaryAssociation = BinaryAssociation(
    name="description39",
    ends={
        Property(name="applauseDsl_TypeDescription41", type=applauseDsl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Property40", type=applauseDsl_TypeDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter42: BinaryAssociation = BinaryAssociation(
    name="parameter42",
    ends={
        Property(name="applauseDsl_Parameter43", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
appicon16: BinaryAssociation = BinaryAssociation(
    name="appicon16",
    ends={
        Property(name="applauseDsl_ScalarExpression18", type=applauseDsl_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Application17", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
splash19: BinaryAssociation = BinaryAssociation(
    name="splash19",
    ends={
        Property(name="applauseDsl_ScalarExpression21", type=applauseDsl_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Application20", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mainview22: BinaryAssociation = BinaryAssociation(
    name="mainview22",
    ends={
        Property(name="applauseDsl_ViewCall", type=applauseDsl_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Application23", type=applauseDsl_ViewCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buttons24: BinaryAssociation = BinaryAssociation(
    name="buttons24",
    ends={
        Property(name="applauseDsl_Button", type=applauseDsl_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Application25", type=applauseDsl_Button, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title26: BinaryAssociation = BinaryAssociation(
    name="title26",
    ends={
        Property(name="applauseDsl_ScalarExpression28", type=applauseDsl_Button, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Button27", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
icon29: BinaryAssociation = BinaryAssociation(
    name="icon29",
    ends={
        Property(name="applauseDsl_ScalarExpression31", type=applauseDsl_Button, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Button30", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
view32: BinaryAssociation = BinaryAssociation(
    name="view32",
    ends={
        Property(name="applauseDsl_ViewCall34", type=applauseDsl_Button, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Button33", type=applauseDsl_ViewCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content67: BinaryAssociation = BinaryAssociation(
    name="content67",
    ends={
        Property(name="applauseDsl_Parameter68", type=applauseDsl_SectionedView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionedView", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superView70: BinaryAssociation = BinaryAssociation(
    name="superView70",
    ends={
        Property(name="applauseDsl_SectionedView71", type=applauseDsl_SectionedView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionedView69", type=applauseDsl_SectionedView, multiplicity=Multiplicity(0, 1))
    }
)
forAllSections72: BinaryAssociation = BinaryAssociation(
    name="forAllSections72",
    ends={
        Property(name="applauseDsl_ViewForAllSections", type=applauseDsl_SectionedView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionedView73", type=applauseDsl_ViewForAllSections, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections74: BinaryAssociation = BinaryAssociation(
    name="sections74",
    ends={
        Property(name="applauseDsl_ViewSection", type=applauseDsl_SectionedView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionedView75", type=applauseDsl_ViewSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
header76: BinaryAssociation = BinaryAssociation(
    name="header76",
    ends={
        Property(name="applauseDsl_ViewHeader", type=applauseDsl_DetailsView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_DetailsView", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type44: BinaryAssociation = BinaryAssociation(
    name="type44",
    ends={
        Property(name="applauseDsl_Type46", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider45", type=applauseDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
url47: BinaryAssociation = BinaryAssociation(
    name="url47",
    ends={
        Property(name="applauseDsl_ScalarExpression49", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider48", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection50: BinaryAssociation = BinaryAssociation(
    name="selection50",
    ends={
        Property(name="applauseDsl_ScalarExpression52", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider51", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
provider53: BinaryAssociation = BinaryAssociation(
    name="provider53",
    ends={
        Property(name="applauseDsl_ContentProvider54", type=applauseDsl_ProviderConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ProviderConstruction", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(0, 1))
    }
)
argument55: BinaryAssociation = BinaryAssociation(
    name="argument55",
    ends={
        Property(name="applauseDsl_Expression", type=applauseDsl_ProviderConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ProviderConstruction56", type=applauseDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predefinedParameter57: BinaryAssociation = BinaryAssociation(
    name="predefinedParameter57",
    ends={
        Property(name="applauseDsl_PredefinedParameter", type=applauseDsl_ProviderConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ProviderConstruction58", type=applauseDsl_PredefinedParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title59: BinaryAssociation = BinaryAssociation(
    name="title59",
    ends={
        Property(name="applauseDsl_ScalarExpression60", type=applauseDsl_View, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_View", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buttons61: BinaryAssociation = BinaryAssociation(
    name="buttons61",
    ends={
        Property(name="applauseDsl_Button63", type=applauseDsl_View, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_View62", type=applauseDsl_Button, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions64: BinaryAssociation = BinaryAssociation(
    name="actions64",
    ends={
        Property(name="applauseDsl_VariableDeclaration66", type=applauseDsl_View, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_View65", type=applauseDsl_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title104: BinaryAssociation = BinaryAssociation(
    name="title104",
    ends={
        Property(name="applauseDsl_ViewForAllSections105", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="applauseDsl_ScalarExpression106", type=applauseDsl_ViewForAllSections, multiplicity=Multiplicity(1, 1))
    }
)
provider107: BinaryAssociation = BinaryAssociation(
    name="provider107",
    ends={
        Property(name="applauseDsl_ProviderConstruction109", type=applauseDsl_ViewForAllSections, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewForAllSections108", type=applauseDsl_ProviderConstruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cells110: BinaryAssociation = BinaryAssociation(
    name="cells110",
    ends={
        Property(name="applauseDsl_SectionCell112", type=applauseDsl_ViewForAllSections, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewForAllSections111", type=applauseDsl_SectionCell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator113: BinaryAssociation = BinaryAssociation(
    name="iterator113",
    ends={
        Property(name="applauseDsl_CollectionIterator", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell114", type=applauseDsl_CollectionIterator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
text115: BinaryAssociation = BinaryAssociation(
    name="text115",
    ends={
        Property(name="applauseDsl_ScalarExpression117", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell116", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
details118: BinaryAssociation = BinaryAssociation(
    name="details118",
    ends={
        Property(name="applauseDsl_ScalarExpression120", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell119", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
header77: BinaryAssociation = BinaryAssociation(
    name="header77",
    ends={
        Property(name="applauseDsl_ViewHeader78", type=applauseDsl_WebView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_WebView", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forAllSections79: BinaryAssociation = BinaryAssociation(
    name="forAllSections79",
    ends={
        Property(name="applauseDsl_ViewForAllSections81", type=applauseDsl_WebView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_WebView80", type=applauseDsl_ViewForAllSections, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections82: BinaryAssociation = BinaryAssociation(
    name="sections82",
    ends={
        Property(name="applauseDsl_ViewSection84", type=applauseDsl_WebView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_WebView83", type=applauseDsl_ViewSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content85: BinaryAssociation = BinaryAssociation(
    name="content85",
    ends={
        Property(name="applauseDsl_Parameter86", type=applauseDsl_CustomView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_CustomView", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title87: BinaryAssociation = BinaryAssociation(
    name="title87",
    ends={
        Property(name="applauseDsl_ScalarExpression89", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewHeader88", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtitle90: BinaryAssociation = BinaryAssociation(
    name="subtitle90",
    ends={
        Property(name="applauseDsl_ScalarExpression92", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewHeader91", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
details93: BinaryAssociation = BinaryAssociation(
    name="details93",
    ends={
        Property(name="applauseDsl_ScalarExpression95", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewHeader94", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
image96: BinaryAssociation = BinaryAssociation(
    name="image96",
    ends={
        Property(name="applauseDsl_ScalarExpression98", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewHeader97", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title99: BinaryAssociation = BinaryAssociation(
    name="title99",
    ends={
        Property(name="applauseDsl_ScalarExpression101", type=applauseDsl_ViewSection, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewSection100", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cells102: BinaryAssociation = BinaryAssociation(
    name="cells102",
    ends={
        Property(name="applauseDsl_SectionCell", type=applauseDsl_ViewSection, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewSection103", type=applauseDsl_SectionCell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
view136: BinaryAssociation = BinaryAssociation(
    name="view136",
    ends={
        Property(name="applauseDsl_View138", type=applauseDsl_ViewCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewCall137", type=applauseDsl_View, multiplicity=Multiplicity(0, 1))
    }
)
provider139: BinaryAssociation = BinaryAssociation(
    name="provider139",
    ends={
        Property(name="applauseDsl_ProviderConstruction141", type=applauseDsl_ViewCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewCall140", type=applauseDsl_ProviderConstruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action142: BinaryAssociation = BinaryAssociation(
    name="action142",
    ends={
        Property(name="applauseDsl_ObjectReference144", type=applauseDsl_ViewCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewCall143", type=applauseDsl_ObjectReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values145: BinaryAssociation = BinaryAssociation(
    name="values145",
    ends={
        Property(name="applauseDsl_ScalarExpression146", type=applauseDsl_StringConcat, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringConcat", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
image121: BinaryAssociation = BinaryAssociation(
    name="image121",
    ends={
        Property(name="applauseDsl_ScalarExpression123", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell122", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query124: BinaryAssociation = BinaryAssociation(
    name="query124",
    ends={
        Property(name="applauseDsl_ScalarExpression126", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell125", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action127: BinaryAssociation = BinaryAssociation(
    name="action127",
    ends={
        Property(name="applauseDsl_ViewAction", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell128", type=applauseDsl_ViewAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buttonAction129: BinaryAssociation = BinaryAssociation(
    name="buttonAction129",
    ends={
        Property(name="applauseDsl_ViewAction131", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell130", type=applauseDsl_ViewAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection132: BinaryAssociation = BinaryAssociation(
    name="collection132",
    ends={
        Property(name="applauseDsl_CollectionExpression", type=applauseDsl_CollectionIterator, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_CollectionIterator133", type=applauseDsl_CollectionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
url134: BinaryAssociation = BinaryAssociation(
    name="url134",
    ends={
        Property(name="applauseDsl_ScalarExpression135", type=applauseDsl_ExternalOpen, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ExternalOpen", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value147: BinaryAssociation = BinaryAssociation(
    name="value147",
    ends={
        Property(name="applauseDsl_ScalarExpression148", type=applauseDsl_StringReplace, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringReplace", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
match149: BinaryAssociation = BinaryAssociation(
    name="match149",
    ends={
        Property(name="applauseDsl_ScalarExpression151", type=applauseDsl_StringReplace, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringReplace150", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
replacement152: BinaryAssociation = BinaryAssociation(
    name="replacement152",
    ends={
        Property(name="applauseDsl_ScalarExpression154", type=applauseDsl_StringReplace, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringReplace153", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value155: BinaryAssociation = BinaryAssociation(
    name="value155",
    ends={
        Property(name="applauseDsl_ScalarExpression156", type=applauseDsl_StringUrlConform, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringUrlConform", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value157: BinaryAssociation = BinaryAssociation(
    name="value157",
    ends={
        Property(name="applauseDsl_ScalarExpression158", type=applauseDsl_StringSplit, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringSplit", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delimiter159: BinaryAssociation = BinaryAssociation(
    name="delimiter159",
    ends={
        Property(name="applauseDsl_ScalarExpression161", type=applauseDsl_StringSplit, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringSplit160", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value162: BinaryAssociation = BinaryAssociation(
    name="value162",
    ends={
        Property(name="applauseDsl_ScalarExpression163", type=applauseDsl_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Constant", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_applauseDsl_StringLiteral_Expression = Generalization(general=Expression, specific=applauseDsl_StringLiteral)
gen_applauseDsl_StringLiteral_ScalarExpression = Generalization(general=ScalarExpression, specific=applauseDsl_StringLiteral)
gen_applauseDsl_SectionId_PredefinedParameter = Generalization(general=PredefinedParameter, specific=applauseDsl_SectionId)
gen_applauseDsl_StringFunction_Expression = Generalization(general=Expression, specific=applauseDsl_StringFunction)
gen_applauseDsl_StringFunction_ScalarExpression = Generalization(general=ScalarExpression, specific=applauseDsl_StringFunction)
gen_applauseDsl_CollectionLiteral_Expression = Generalization(general=Expression, specific=applauseDsl_CollectionLiteral)
gen_applauseDsl_CollectionLiteral_CollectionExpression = Generalization(general=CollectionExpression, specific=applauseDsl_CollectionLiteral)
gen_applauseDsl_NavigationBarItem_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_NavigationBarItem)
gen_applauseDsl_VariableDeclaration_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_VariableDeclaration)
gen_applauseDsl_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=applauseDsl_Parameter)
gen_applauseDsl_ObjectReference_Expression = Generalization(general=Expression, specific=applauseDsl_ObjectReference)
gen_applauseDsl_ObjectReference_ScalarExpression = Generalization(general=ScalarExpression, specific=applauseDsl_ObjectReference)
gen_applauseDsl_ObjectReference_CollectionExpression = Generalization(general=CollectionExpression, specific=applauseDsl_ObjectReference)
gen_applauseDsl_Entity_Type = Generalization(general=Type, specific=applauseDsl_Entity)
gen_applauseDsl_Property_VariableDeclaration = Generalization(general=VariableDeclaration, specific=applauseDsl_Property)
gen_applauseDsl_ContentProvider_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_ContentProvider)
gen_applauseDsl_CollectionFunction_Expression = Generalization(general=Expression, specific=applauseDsl_CollectionFunction)
gen_applauseDsl_CollectionFunction_CollectionExpression = Generalization(general=CollectionExpression, specific=applauseDsl_CollectionFunction)
gen_applauseDsl_Type_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_Type)
gen_applauseDsl_SimpleType_Type = Generalization(general=Type, specific=applauseDsl_SimpleType)
gen_applauseDsl_TableView_SectionedView = Generalization(general=SectionedView, specific=applauseDsl_TableView)
gen_applauseDsl_DetailsView_SectionedView = Generalization(general=SectionedView, specific=applauseDsl_DetailsView)
gen_applauseDsl_WebView_View = Generalization(general=View, specific=applauseDsl_WebView)
gen_applauseDsl_View_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_View)
gen_applauseDsl_SectionedView_View = Generalization(general=View, specific=applauseDsl_SectionedView)
gen_applauseDsl_CustomView_View = Generalization(general=View, specific=applauseDsl_CustomView)
gen_applauseDsl_ViewCall_ViewAction = Generalization(general=ViewAction, specific=applauseDsl_ViewCall)
gen_applauseDsl_StringConcat_StringFunction = Generalization(general=StringFunction, specific=applauseDsl_StringConcat)
gen_applauseDsl_StringReplace_StringFunction = Generalization(general=StringFunction, specific=applauseDsl_StringReplace)
gen_applauseDsl_CollectionIterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=applauseDsl_CollectionIterator)
gen_applauseDsl_ActionDelegate_ViewAction = Generalization(general=ViewAction, specific=applauseDsl_ActionDelegate)
gen_applauseDsl_ExternalOpen_ViewAction = Generalization(general=ViewAction, specific=applauseDsl_ExternalOpen)
gen_applauseDsl_StringUrlConform_StringFunction = Generalization(general=StringFunction, specific=applauseDsl_StringUrlConform)
gen_applauseDsl_StringSplit_CollectionFunction = Generalization(general=CollectionFunction, specific=applauseDsl_StringSplit)
gen_applauseDsl_Constant_VariableDeclaration = Generalization(general=VariableDeclaration, specific=applauseDsl_Constant)

# Domain Model
domain_model = DomainModel(
    name="applauseDsl",
    types={applauseDsl_ApplauseModel, applauseDsl_Application, applauseDsl_ModelElement, applauseDsl_Expression, applauseDsl_CollectionExpression, applauseDsl_StringLiteral, applauseDsl_PredefinedParameter, applauseDsl_SectionId, PredefinedParameter, applauseDsl_StringFunction, applauseDsl_CollectionLiteral, applauseDsl_NavigationBarItem, ModelElement, applauseDsl_ScalarExpression, applauseDsl_VariableDeclaration, applauseDsl_TypeDescription, applauseDsl_Type, applauseDsl_Parameter, VariableDeclaration, applauseDsl_ObjectReference, Expression, ScalarExpression, CollectionExpression, applauseDsl_Entity, applauseDsl_Property, applauseDsl_ContentProvider, applauseDsl_CollectionFunction, applauseDsl_ViewCall, applauseDsl_Button, applauseDsl_SimpleType, Type, applauseDsl_ViewForAllSections, applauseDsl_ViewSection, applauseDsl_TableView, SectionedView, applauseDsl_DetailsView, applauseDsl_ViewHeader, applauseDsl_WebView, applauseDsl_ProviderConstruction, applauseDsl_View, applauseDsl_SectionedView, View, applauseDsl_CollectionIterator, applauseDsl_CustomView, applauseDsl_SectionCell, applauseDsl_StringConcat, StringFunction, applauseDsl_StringReplace, applauseDsl_ViewAction, applauseDsl_ActionDelegate, ViewAction, applauseDsl_ExternalOpen, applauseDsl_StringUrlConform, applauseDsl_StringSplit, CollectionFunction, applauseDsl_Constant, CellType, Position},
    associations={application0, tail12, items14, elements1, icon3, triggers4, type7, description8, object10, extends36, properties37, description39, parameter42, appicon16, splash19, mainview22, buttons24, title26, icon29, view32, content67, superView70, forAllSections72, sections74, header76, type44, url47, selection50, provider53, argument55, predefinedParameter57, title59, buttons61, actions64, title104, provider107, cells110, iterator113, text115, details118, header77, forAllSections79, sections82, content85, title87, subtitle90, details93, image96, title99, cells102, view136, provider139, action142, values145, image121, query124, action127, buttonAction129, collection132, url134, value147, match149, replacement152, value155, value157, delimiter159, value162},
    generalizations={gen_applauseDsl_StringLiteral_Expression, gen_applauseDsl_StringLiteral_ScalarExpression, gen_applauseDsl_SectionId_PredefinedParameter, gen_applauseDsl_StringFunction_Expression, gen_applauseDsl_StringFunction_ScalarExpression, gen_applauseDsl_CollectionLiteral_Expression, gen_applauseDsl_CollectionLiteral_CollectionExpression, gen_applauseDsl_NavigationBarItem_ModelElement, gen_applauseDsl_VariableDeclaration_ModelElement, gen_applauseDsl_Parameter_VariableDeclaration, gen_applauseDsl_ObjectReference_Expression, gen_applauseDsl_ObjectReference_ScalarExpression, gen_applauseDsl_ObjectReference_CollectionExpression, gen_applauseDsl_Entity_Type, gen_applauseDsl_Property_VariableDeclaration, gen_applauseDsl_ContentProvider_ModelElement, gen_applauseDsl_CollectionFunction_Expression, gen_applauseDsl_CollectionFunction_CollectionExpression, gen_applauseDsl_Type_ModelElement, gen_applauseDsl_SimpleType_Type, gen_applauseDsl_TableView_SectionedView, gen_applauseDsl_DetailsView_SectionedView, gen_applauseDsl_WebView_View, gen_applauseDsl_View_ModelElement, gen_applauseDsl_SectionedView_View, gen_applauseDsl_CustomView_View, gen_applauseDsl_ViewCall_ViewAction, gen_applauseDsl_StringConcat_StringFunction, gen_applauseDsl_StringReplace_StringFunction, gen_applauseDsl_CollectionIterator_VariableDeclaration, gen_applauseDsl_ActionDelegate_ViewAction, gen_applauseDsl_ExternalOpen_ViewAction, gen_applauseDsl_StringUrlConform_StringFunction, gen_applauseDsl_StringSplit_CollectionFunction, gen_applauseDsl_Constant_VariableDeclaration},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)