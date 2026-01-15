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
SerializationFormat: Enumeration = Enumeration(
    name="SerializationFormat",
    literals={
            EnumerationLiteral(name="XML"),
			EnumerationLiteral(name="JSON")
    }
)

TableViewStyle: Enumeration = Enumeration(
    name="TableViewStyle",
    literals={
            EnumerationLiteral(name="Plain"),
			EnumerationLiteral(name="Grouped")
    }
)

CellType: Enumeration = Enumeration(
    name="CellType",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="value1"),
			EnumerationLiteral(name="value2"),
			EnumerationLiteral(name="subtitle")
    }
)

CellAccessory: Enumeration = Enumeration(
    name="CellAccessory",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Link"),
			EnumerationLiteral(name="Detail"),
			EnumerationLiteral(name="Check")
    }
)

# Classes
applauseDsl_PropertyPathPart = Class(name="applauseDsl::PropertyPathPart")
applauseDsl_TypeDescription = Class(name="applauseDsl::TypeDescription")
applauseDsl_Type = Class(name="applauseDsl::Type")
applauseDsl_Parameter = Class(name="applauseDsl::Parameter")
PropertyPathPart = Class(name="PropertyPathPart")
applauseDsl_Model = Class(name="applauseDsl::Model")
applauseDsl_Application = Class(name="applauseDsl::Application")
applauseDsl_ModelElement = Class(name="applauseDsl::ModelElement")
applauseDsl_Property = Class(name="applauseDsl::Property")
applauseDsl_ProviderConstruction = Class(name="applauseDsl::ProviderConstruction")
applauseDsl_ObjectReference = Class(name="applauseDsl::ObjectReference")
Expression = Class(name="Expression")
ScalarExpression = Class(name="ScalarExpression")
CollectionExpression = Class(name="CollectionExpression")
applauseDsl_Expression = Class(name="applauseDsl::Expression")
applauseDsl_ScalarExpression = Class(name="applauseDsl::ScalarExpression")
applauseDsl_CollectionExpression = Class(name="applauseDsl::CollectionExpression")
applauseDsl_StringLiteral = Class(name="applauseDsl::StringLiteral")
applauseDsl_StringFunction = Class(name="applauseDsl::StringFunction")
applauseDsl_CollectionLiteral = Class(name="applauseDsl::CollectionLiteral")
applauseDsl_CollectionFunction = Class(name="applauseDsl::CollectionFunction")
applauseDsl_ViewCall = Class(name="applauseDsl::ViewCall")
ModelElement = Class(name="ModelElement")
applauseDsl_SimpleType = Class(name="applauseDsl::SimpleType")
Type = Class(name="Type")
applauseDsl_Entity = Class(name="applauseDsl::Entity")
applauseDsl_TableView = Class(name="applauseDsl::TableView")
applauseDsl_ContentProvider = Class(name="applauseDsl::ContentProvider")
applauseDsl_ContentProviderImplementation = Class(name="applauseDsl::ContentProviderImplementation")
applauseDsl_FetchingContentProviderImplementation = Class(name="applauseDsl::FetchingContentProviderImplementation")
ContentProviderImplementation = Class(name="ContentProviderImplementation")
applauseDsl_CustomContentProviderImplementation = Class(name="applauseDsl::CustomContentProviderImplementation")
applauseDsl_ProjectClass = Class(name="applauseDsl::ProjectClass")
applauseDsl_View = Class(name="applauseDsl::View")
applauseDsl_TabView = Class(name="applauseDsl::TabView")
View = Class(name="View")
applauseDsl_Tab = Class(name="applauseDsl::Tab")
applauseDsl_Selector = Class(name="applauseDsl::Selector")
ViewAction = Class(name="ViewAction")
applauseDsl_ExternalOpen = Class(name="applauseDsl::ExternalOpen")
applauseDsl_Section = Class(name="applauseDsl::Section")
applauseDsl_CustomView = Class(name="applauseDsl::CustomView")
applauseDsl_ViewContentElement = Class(name="applauseDsl::ViewContentElement")
applauseDsl_CollectionIterator = Class(name="applauseDsl::CollectionIterator")
ViewContentElement = Class(name="ViewContentElement")
applauseDsl_Cell = Class(name="applauseDsl::Cell")
applauseDsl_ViewAction = Class(name="applauseDsl::ViewAction")
applauseDsl_SimpleProviderConstruction = Class(name="applauseDsl::SimpleProviderConstruction")
applauseDsl_StringConcat = Class(name="applauseDsl::StringConcat")
StringFunction = Class(name="StringFunction")
applauseDsl_StringReplace = Class(name="applauseDsl::StringReplace")
applauseDsl_StringUrlConform = Class(name="applauseDsl::StringUrlConform")
applauseDsl_StringSplit = Class(name="applauseDsl::StringSplit")
CollectionFunction = Class(name="CollectionFunction")
applauseDsl_ComplexProviderConstruction = Class(name="applauseDsl::ComplexProviderConstruction")
ProviderConstruction = Class(name="ProviderConstruction")

# applauseDsl_PropertyPathPart class attributes and methods
applauseDsl_PropertyPathPart_name: Property = Property(name="name", type=StringType)
applauseDsl_PropertyPathPart.attributes={applauseDsl_PropertyPathPart_name}

# applauseDsl_TypeDescription class attributes and methods
applauseDsl_TypeDescription_many: Property = Property(name="many", type=BooleanType)
applauseDsl_TypeDescription.attributes={applauseDsl_TypeDescription_many}

# applauseDsl_Type class attributes and methods

# applauseDsl_Parameter class attributes and methods

# PropertyPathPart class attributes and methods

# applauseDsl_Model class attributes and methods

# applauseDsl_Application class attributes and methods
applauseDsl_Application_name: Property = Property(name="name", type=StringType)
applauseDsl_Application.attributes={applauseDsl_Application_name}

# applauseDsl_ModelElement class attributes and methods
applauseDsl_ModelElement_name: Property = Property(name="name", type=StringType)
applauseDsl_ModelElement.attributes={applauseDsl_ModelElement_name}

# applauseDsl_Property class attributes and methods
applauseDsl_Property_derived: Property = Property(name="derived", type=BooleanType)
applauseDsl_Property.attributes={applauseDsl_Property_derived}

# applauseDsl_ProviderConstruction class attributes and methods

# applauseDsl_ObjectReference class attributes and methods

# Expression class attributes and methods

# ScalarExpression class attributes and methods

# CollectionExpression class attributes and methods

# applauseDsl_Expression class attributes and methods

# applauseDsl_ScalarExpression class attributes and methods

# applauseDsl_CollectionExpression class attributes and methods

# applauseDsl_StringLiteral class attributes and methods
applauseDsl_StringLiteral_value: Property = Property(name="value", type=StringType)
applauseDsl_StringLiteral.attributes={applauseDsl_StringLiteral_value}

# applauseDsl_StringFunction class attributes and methods

# applauseDsl_CollectionLiteral class attributes and methods

# applauseDsl_CollectionFunction class attributes and methods

# applauseDsl_ViewCall class attributes and methods

# ModelElement class attributes and methods

# applauseDsl_SimpleType class attributes and methods
applauseDsl_SimpleType_platformType: Property = Property(name="platformType", type=StringType)
applauseDsl_SimpleType.attributes={applauseDsl_SimpleType_platformType}

# Type class attributes and methods

# applauseDsl_Entity class attributes and methods
applauseDsl_Entity_runtimeType: Property = Property(name="runtimeType", type=BooleanType)
applauseDsl_Entity.attributes={applauseDsl_Entity_runtimeType}

# applauseDsl_TableView class attributes and methods
applauseDsl_TableView_style: Property = Property(name="style", type=StringType)
applauseDsl_TableView.attributes={applauseDsl_TableView_style}

# applauseDsl_ContentProvider class attributes and methods
applauseDsl_ContentProvider_storing: Property = Property(name="storing", type=BooleanType)
applauseDsl_ContentProvider_many: Property = Property(name="many", type=BooleanType)
applauseDsl_ContentProvider.attributes={applauseDsl_ContentProvider_storing, applauseDsl_ContentProvider_many}

# applauseDsl_ContentProviderImplementation class attributes and methods

# applauseDsl_FetchingContentProviderImplementation class attributes and methods
applauseDsl_FetchingContentProviderImplementation_format: Property = Property(name="format", type=StringType)
applauseDsl_FetchingContentProviderImplementation.attributes={applauseDsl_FetchingContentProviderImplementation_format}

# ContentProviderImplementation class attributes and methods

# applauseDsl_CustomContentProviderImplementation class attributes and methods

# applauseDsl_ProjectClass class attributes and methods
applauseDsl_ProjectClass_name: Property = Property(name="name", type=StringType)
applauseDsl_ProjectClass.attributes={applauseDsl_ProjectClass_name}

# applauseDsl_View class attributes and methods

# applauseDsl_TabView class attributes and methods

# View class attributes and methods

# applauseDsl_Tab class attributes and methods

# applauseDsl_Selector class attributes and methods
applauseDsl_Selector_name: Property = Property(name="name", type=StringType)
applauseDsl_Selector.attributes={applauseDsl_Selector_name}

# ViewAction class attributes and methods

# applauseDsl_ExternalOpen class attributes and methods

# applauseDsl_Section class attributes and methods

# applauseDsl_CustomView class attributes and methods
applauseDsl_CustomView_className: Property = Property(name="className", type=StringType)
applauseDsl_CustomView.attributes={applauseDsl_CustomView_className}

# applauseDsl_ViewContentElement class attributes and methods

# applauseDsl_CollectionIterator class attributes and methods

# ViewContentElement class attributes and methods

# applauseDsl_Cell class attributes and methods
applauseDsl_Cell_type: Property = Property(name="type", type=StringType)
applauseDsl_Cell_accessory: Property = Property(name="accessory", type=StringType)
applauseDsl_Cell.attributes={applauseDsl_Cell_type, applauseDsl_Cell_accessory}

# applauseDsl_ViewAction class attributes and methods

# applauseDsl_SimpleProviderConstruction class attributes and methods

# applauseDsl_StringConcat class attributes and methods

# StringFunction class attributes and methods

# applauseDsl_StringReplace class attributes and methods

# applauseDsl_StringUrlConform class attributes and methods

# applauseDsl_StringSplit class attributes and methods

# CollectionFunction class attributes and methods

# applauseDsl_ComplexProviderConstruction class attributes and methods

# ProviderConstruction class attributes and methods

# Relationships
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="applauseDsl_Type", type=applauseDsl_TypeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TypeDescription", type=applauseDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
application0: BinaryAssociation = BinaryAssociation(
    name="application0",
    ends={
        Property(name="applauseDsl_Application", type=applauseDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Model", type=applauseDsl_Application, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="applauseDsl_ModelElement", type=applauseDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Model2", type=applauseDsl_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties20: BinaryAssociation = BinaryAssociation(
    name="properties20",
    ends={
        Property(name="applauseDsl_Property", type=applauseDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Entity21", type=applauseDsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description22: BinaryAssociation = BinaryAssociation(
    name="description22",
    ends={
        Property(name="applauseDsl_TypeDescription24", type=applauseDsl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Property23", type=applauseDsl_TypeDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description4: BinaryAssociation = BinaryAssociation(
    name="description4",
    ends={
        Property(name="applauseDsl_TypeDescription5", type=applauseDsl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Parameter", type=applauseDsl_TypeDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value6: BinaryAssociation = BinaryAssociation(
    name="value6",
    ends={
        Property(name="applauseDsl_ProviderConstruction", type=applauseDsl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Parameter7", type=applauseDsl_ProviderConstruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object8: BinaryAssociation = BinaryAssociation(
    name="object8",
    ends={
        Property(name="applauseDsl_PropertyPathPart", type=applauseDsl_ObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ObjectReference", type=applauseDsl_PropertyPathPart, multiplicity=Multiplicity(0, 1))
    }
)
tail10: BinaryAssociation = BinaryAssociation(
    name="tail10",
    ends={
        Property(name="applauseDsl_ObjectReference11", type=applauseDsl_ObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ObjectReference9", type=applauseDsl_ObjectReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items12: BinaryAssociation = BinaryAssociation(
    name="items12",
    ends={
        Property(name="applauseDsl_ScalarExpression", type=applauseDsl_CollectionLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_CollectionLiteral", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
background13: BinaryAssociation = BinaryAssociation(
    name="background13",
    ends={
        Property(name="applauseDsl_ScalarExpression15", type=applauseDsl_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Application14", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startView16: BinaryAssociation = BinaryAssociation(
    name="startView16",
    ends={
        Property(name="applauseDsl_ViewCall", type=applauseDsl_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Application17", type=applauseDsl_ViewCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends19: BinaryAssociation = BinaryAssociation(
    name="extends19",
    ends={
        Property(name="applauseDsl_Entity", type=applauseDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Entity18", type=applauseDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
variables50: BinaryAssociation = BinaryAssociation(
    name="variables50",
    ends={
        Property(name="applauseDsl_Parameter51", type=applauseDsl_TableView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TableView", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter25: BinaryAssociation = BinaryAssociation(
    name="parameter25",
    ends={
        Property(name="applauseDsl_Parameter26", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="applauseDsl_Type29", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider28", type=applauseDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
implementation30: BinaryAssociation = BinaryAssociation(
    name="implementation30",
    ends={
        Property(name="applauseDsl_ContentProviderImplementation", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider31", type=applauseDsl_ContentProviderImplementation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
url32: BinaryAssociation = BinaryAssociation(
    name="url32",
    ends={
        Property(name="applauseDsl_ScalarExpression33", type=applauseDsl_FetchingContentProviderImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_FetchingContentProviderImplementation", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection34: BinaryAssociation = BinaryAssociation(
    name="selection34",
    ends={
        Property(name="applauseDsl_ScalarExpression36", type=applauseDsl_FetchingContentProviderImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_FetchingContentProviderImplementation35", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
providerClass37: BinaryAssociation = BinaryAssociation(
    name="providerClass37",
    ends={
        Property(name="applauseDsl_ProjectClass", type=applauseDsl_CustomContentProviderImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_CustomContentProviderImplementation", type=applauseDsl_ProjectClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content38: BinaryAssociation = BinaryAssociation(
    name="content38",
    ends={
        Property(name="applauseDsl_Parameter39", type=applauseDsl_View, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_View", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tabs40: BinaryAssociation = BinaryAssociation(
    name="tabs40",
    ends={
        Property(name="applauseDsl_Tab", type=applauseDsl_TabView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TabView", type=applauseDsl_Tab, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title41: BinaryAssociation = BinaryAssociation(
    name="title41",
    ends={
        Property(name="applauseDsl_ScalarExpression43", type=applauseDsl_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Tab42", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
icon44: BinaryAssociation = BinaryAssociation(
    name="icon44",
    ends={
        Property(name="applauseDsl_ScalarExpression46", type=applauseDsl_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Tab45", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
view47: BinaryAssociation = BinaryAssociation(
    name="view47",
    ends={
        Property(name="applauseDsl_ViewCall49", type=applauseDsl_Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Tab48", type=applauseDsl_ViewCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection77: BinaryAssociation = BinaryAssociation(
    name="collection77",
    ends={
        Property(name="applauseDsl_CollectionExpression", type=applauseDsl_CollectionIterator, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_CollectionIterator78", type=applauseDsl_CollectionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title52: BinaryAssociation = BinaryAssociation(
    name="title52",
    ends={
        Property(name="applauseDsl_ScalarExpression54", type=applauseDsl_TableView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TableView53", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
titleImage55: BinaryAssociation = BinaryAssociation(
    name="titleImage55",
    ends={
        Property(name="applauseDsl_ScalarExpression57", type=applauseDsl_TableView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TableView56", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections58: BinaryAssociation = BinaryAssociation(
    name="sections58",
    ends={
        Property(name="applauseDsl_Section", type=applauseDsl_TableView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TableView59", type=applauseDsl_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator60: BinaryAssociation = BinaryAssociation(
    name="iterator60",
    ends={
        Property(name="applauseDsl_CollectionIterator", type=applauseDsl_ViewContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewContentElement", type=applauseDsl_CollectionIterator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title61: BinaryAssociation = BinaryAssociation(
    name="title61",
    ends={
        Property(name="applauseDsl_ScalarExpression63", type=applauseDsl_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Section62", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cells64: BinaryAssociation = BinaryAssociation(
    name="cells64",
    ends={
        Property(name="applauseDsl_Cell", type=applauseDsl_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Section65", type=applauseDsl_Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
text66: BinaryAssociation = BinaryAssociation(
    name="text66",
    ends={
        Property(name="applauseDsl_ScalarExpression68", type=applauseDsl_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Cell67", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
details69: BinaryAssociation = BinaryAssociation(
    name="details69",
    ends={
        Property(name="applauseDsl_ScalarExpression71", type=applauseDsl_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Cell70", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
image72: BinaryAssociation = BinaryAssociation(
    name="image72",
    ends={
        Property(name="applauseDsl_ScalarExpression74", type=applauseDsl_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Cell73", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action75: BinaryAssociation = BinaryAssociation(
    name="action75",
    ends={
        Property(name="applauseDsl_ViewAction", type=applauseDsl_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Cell76", type=applauseDsl_ViewAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument106: BinaryAssociation = BinaryAssociation(
    name="argument106",
    ends={
        Property(name="applauseDsl_Expression", type=applauseDsl_ComplexProviderConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ComplexProviderConstruction107", type=applauseDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression108: BinaryAssociation = BinaryAssociation(
    name="expression108",
    ends={
        Property(name="applauseDsl_Expression109", type=applauseDsl_SimpleProviderConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SimpleProviderConstruction", type=applauseDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
url79: BinaryAssociation = BinaryAssociation(
    name="url79",
    ends={
        Property(name="applauseDsl_ScalarExpression80", type=applauseDsl_ExternalOpen, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ExternalOpen", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
view81: BinaryAssociation = BinaryAssociation(
    name="view81",
    ends={
        Property(name="applauseDsl_View83", type=applauseDsl_ViewCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewCall82", type=applauseDsl_View, multiplicity=Multiplicity(0, 1))
    }
)
provider84: BinaryAssociation = BinaryAssociation(
    name="provider84",
    ends={
        Property(name="applauseDsl_ProviderConstruction86", type=applauseDsl_ViewCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewCall85", type=applauseDsl_ProviderConstruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values87: BinaryAssociation = BinaryAssociation(
    name="values87",
    ends={
        Property(name="applauseDsl_ScalarExpression88", type=applauseDsl_StringConcat, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringConcat", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value89: BinaryAssociation = BinaryAssociation(
    name="value89",
    ends={
        Property(name="applauseDsl_ScalarExpression90", type=applauseDsl_StringReplace, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringReplace", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
match91: BinaryAssociation = BinaryAssociation(
    name="match91",
    ends={
        Property(name="applauseDsl_ScalarExpression93", type=applauseDsl_StringReplace, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringReplace92", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
replacement94: BinaryAssociation = BinaryAssociation(
    name="replacement94",
    ends={
        Property(name="applauseDsl_ScalarExpression96", type=applauseDsl_StringReplace, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringReplace95", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value97: BinaryAssociation = BinaryAssociation(
    name="value97",
    ends={
        Property(name="applauseDsl_ScalarExpression98", type=applauseDsl_StringUrlConform, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringUrlConform", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value99: BinaryAssociation = BinaryAssociation(
    name="value99",
    ends={
        Property(name="applauseDsl_ScalarExpression100", type=applauseDsl_StringSplit, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringSplit", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delimiter101: BinaryAssociation = BinaryAssociation(
    name="delimiter101",
    ends={
        Property(name="applauseDsl_ScalarExpression103", type=applauseDsl_StringSplit, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringSplit102", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
provider104: BinaryAssociation = BinaryAssociation(
    name="provider104",
    ends={
        Property(name="applauseDsl_ContentProvider105", type=applauseDsl_ComplexProviderConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ComplexProviderConstruction", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_applauseDsl_Property_PropertyPathPart = Generalization(general=PropertyPathPart, specific=applauseDsl_Property)
gen_applauseDsl_Parameter_PropertyPathPart = Generalization(general=PropertyPathPart, specific=applauseDsl_Parameter)
gen_applauseDsl_ObjectReference_Expression = Generalization(general=Expression, specific=applauseDsl_ObjectReference)
gen_applauseDsl_ObjectReference_ScalarExpression = Generalization(general=ScalarExpression, specific=applauseDsl_ObjectReference)
gen_applauseDsl_ObjectReference_CollectionExpression = Generalization(general=CollectionExpression, specific=applauseDsl_ObjectReference)
gen_applauseDsl_StringLiteral_Expression = Generalization(general=Expression, specific=applauseDsl_StringLiteral)
gen_applauseDsl_StringLiteral_ScalarExpression = Generalization(general=ScalarExpression, specific=applauseDsl_StringLiteral)
gen_applauseDsl_StringFunction_Expression = Generalization(general=Expression, specific=applauseDsl_StringFunction)
gen_applauseDsl_StringFunction_ScalarExpression = Generalization(general=ScalarExpression, specific=applauseDsl_StringFunction)
gen_applauseDsl_CollectionLiteral_Expression = Generalization(general=Expression, specific=applauseDsl_CollectionLiteral)
gen_applauseDsl_CollectionLiteral_CollectionExpression = Generalization(general=CollectionExpression, specific=applauseDsl_CollectionLiteral)
gen_applauseDsl_CollectionFunction_Expression = Generalization(general=Expression, specific=applauseDsl_CollectionFunction)
gen_applauseDsl_CollectionFunction_CollectionExpression = Generalization(general=CollectionExpression, specific=applauseDsl_CollectionFunction)
gen_applauseDsl_Type_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_Type)
gen_applauseDsl_SimpleType_Type = Generalization(general=Type, specific=applauseDsl_SimpleType)
gen_applauseDsl_Entity_Type = Generalization(general=Type, specific=applauseDsl_Entity)
gen_applauseDsl_TableView_View = Generalization(general=View, specific=applauseDsl_TableView)
gen_applauseDsl_ContentProvider_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_ContentProvider)
gen_applauseDsl_FetchingContentProviderImplementation_ContentProviderImplementation = Generalization(general=ContentProviderImplementation, specific=applauseDsl_FetchingContentProviderImplementation)
gen_applauseDsl_CustomContentProviderImplementation_ContentProviderImplementation = Generalization(general=ContentProviderImplementation, specific=applauseDsl_CustomContentProviderImplementation)
gen_applauseDsl_View_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_View)
gen_applauseDsl_TabView_View = Generalization(general=View, specific=applauseDsl_TabView)
gen_applauseDsl_CollectionIterator_PropertyPathPart = Generalization(general=PropertyPathPart, specific=applauseDsl_CollectionIterator)
gen_applauseDsl_Selector_ViewAction = Generalization(general=ViewAction, specific=applauseDsl_Selector)
gen_applauseDsl_ExternalOpen_ViewAction = Generalization(general=ViewAction, specific=applauseDsl_ExternalOpen)
gen_applauseDsl_CustomView_View = Generalization(general=View, specific=applauseDsl_CustomView)
gen_applauseDsl_Section_ViewContentElement = Generalization(general=ViewContentElement, specific=applauseDsl_Section)
gen_applauseDsl_Cell_ViewContentElement = Generalization(general=ViewContentElement, specific=applauseDsl_Cell)
gen_applauseDsl_SimpleProviderConstruction_ProviderConstruction = Generalization(general=ProviderConstruction, specific=applauseDsl_SimpleProviderConstruction)
gen_applauseDsl_ViewCall_ViewAction = Generalization(general=ViewAction, specific=applauseDsl_ViewCall)
gen_applauseDsl_StringConcat_StringFunction = Generalization(general=StringFunction, specific=applauseDsl_StringConcat)
gen_applauseDsl_StringReplace_StringFunction = Generalization(general=StringFunction, specific=applauseDsl_StringReplace)
gen_applauseDsl_StringUrlConform_StringFunction = Generalization(general=StringFunction, specific=applauseDsl_StringUrlConform)
gen_applauseDsl_StringSplit_CollectionFunction = Generalization(general=CollectionFunction, specific=applauseDsl_StringSplit)
gen_applauseDsl_ComplexProviderConstruction_ProviderConstruction = Generalization(general=ProviderConstruction, specific=applauseDsl_ComplexProviderConstruction)

# Domain Model
domain_model = DomainModel(
    name="applauseDsl",
    types={applauseDsl_PropertyPathPart, applauseDsl_TypeDescription, applauseDsl_Type, applauseDsl_Parameter, PropertyPathPart, applauseDsl_Model, applauseDsl_Application, applauseDsl_ModelElement, applauseDsl_Property, applauseDsl_ProviderConstruction, applauseDsl_ObjectReference, Expression, ScalarExpression, CollectionExpression, applauseDsl_Expression, applauseDsl_ScalarExpression, applauseDsl_CollectionExpression, applauseDsl_StringLiteral, applauseDsl_StringFunction, applauseDsl_CollectionLiteral, applauseDsl_CollectionFunction, applauseDsl_ViewCall, ModelElement, applauseDsl_SimpleType, Type, applauseDsl_Entity, applauseDsl_TableView, applauseDsl_ContentProvider, applauseDsl_ContentProviderImplementation, applauseDsl_FetchingContentProviderImplementation, ContentProviderImplementation, applauseDsl_CustomContentProviderImplementation, applauseDsl_ProjectClass, applauseDsl_View, applauseDsl_TabView, View, applauseDsl_Tab, applauseDsl_Selector, ViewAction, applauseDsl_ExternalOpen, applauseDsl_Section, applauseDsl_CustomView, applauseDsl_ViewContentElement, applauseDsl_CollectionIterator, ViewContentElement, applauseDsl_Cell, applauseDsl_ViewAction, applauseDsl_SimpleProviderConstruction, applauseDsl_StringConcat, StringFunction, applauseDsl_StringReplace, applauseDsl_StringUrlConform, applauseDsl_StringSplit, CollectionFunction, applauseDsl_ComplexProviderConstruction, ProviderConstruction, SerializationFormat, TableViewStyle, CellType, CellAccessory},
    associations={type3, application0, elements1, properties20, description22, description4, value6, object8, tail10, items12, background13, startView16, extends19, variables50, parameter25, type27, implementation30, url32, selection34, providerClass37, content38, tabs40, title41, icon44, view47, collection77, title52, titleImage55, sections58, iterator60, title61, cells64, text66, details69, image72, action75, argument106, expression108, url79, view81, provider84, values87, value89, match91, replacement94, value97, value99, delimiter101, provider104},
    generalizations={gen_applauseDsl_Property_PropertyPathPart, gen_applauseDsl_Parameter_PropertyPathPart, gen_applauseDsl_ObjectReference_Expression, gen_applauseDsl_ObjectReference_ScalarExpression, gen_applauseDsl_ObjectReference_CollectionExpression, gen_applauseDsl_StringLiteral_Expression, gen_applauseDsl_StringLiteral_ScalarExpression, gen_applauseDsl_StringFunction_Expression, gen_applauseDsl_StringFunction_ScalarExpression, gen_applauseDsl_CollectionLiteral_Expression, gen_applauseDsl_CollectionLiteral_CollectionExpression, gen_applauseDsl_CollectionFunction_Expression, gen_applauseDsl_CollectionFunction_CollectionExpression, gen_applauseDsl_Type_ModelElement, gen_applauseDsl_SimpleType_Type, gen_applauseDsl_Entity_Type, gen_applauseDsl_TableView_View, gen_applauseDsl_ContentProvider_ModelElement, gen_applauseDsl_FetchingContentProviderImplementation_ContentProviderImplementation, gen_applauseDsl_CustomContentProviderImplementation_ContentProviderImplementation, gen_applauseDsl_View_ModelElement, gen_applauseDsl_TabView_View, gen_applauseDsl_CollectionIterator_PropertyPathPart, gen_applauseDsl_Selector_ViewAction, gen_applauseDsl_ExternalOpen_ViewAction, gen_applauseDsl_CustomView_View, gen_applauseDsl_Section_ViewContentElement, gen_applauseDsl_Cell_ViewContentElement, gen_applauseDsl_SimpleProviderConstruction_ProviderConstruction, gen_applauseDsl_ViewCall_ViewAction, gen_applauseDsl_StringConcat_StringFunction, gen_applauseDsl_StringReplace_StringFunction, gen_applauseDsl_StringUrlConform_StringFunction, gen_applauseDsl_StringSplit_CollectionFunction, gen_applauseDsl_ComplexProviderConstruction_ProviderConstruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)