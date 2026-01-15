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
			EnumerationLiteral(name="subtitle")
    }
)

# Classes
applauseDsl_Model = Class(name="applauseDsl::Model")
applauseDsl_Application = Class(name="applauseDsl::Application")
applauseDsl_ModelElement = Class(name="applauseDsl::ModelElement")
applauseDsl_Expression = Class(name="applauseDsl::Expression")
applauseDsl_ScalarExpression = Class(name="applauseDsl::ScalarExpression")
applauseDsl_CollectionExpression = Class(name="applauseDsl::CollectionExpression")
applauseDsl_StringLiteral = Class(name="applauseDsl::StringLiteral")
applauseDsl_StringFunction = Class(name="applauseDsl::StringFunction")
applauseDsl_CollectionLiteral = Class(name="applauseDsl::CollectionLiteral")
applauseDsl_CollectionFunction = Class(name="applauseDsl::CollectionFunction")
applauseDsl_TabbarButton = Class(name="applauseDsl::TabbarButton")
applauseDsl_VariableDeclaration = Class(name="applauseDsl::VariableDeclaration")
applauseDsl_TypeDescription = Class(name="applauseDsl::TypeDescription")
applauseDsl_Type = Class(name="applauseDsl::Type")
applauseDsl_Parameter = Class(name="applauseDsl::Parameter")
VariableDeclaration = Class(name="VariableDeclaration")
applauseDsl_ObjectReference = Class(name="applauseDsl::ObjectReference")
Expression = Class(name="Expression")
ScalarExpression = Class(name="ScalarExpression")
CollectionExpression = Class(name="CollectionExpression")
applauseDsl_ContentProvider = Class(name="applauseDsl::ContentProvider")
applauseDsl_ProviderConstruction = Class(name="applauseDsl::ProviderConstruction")
applauseDsl_View = Class(name="applauseDsl::View")
applauseDsl_SectionedView = Class(name="applauseDsl::SectionedView")
View = Class(name="View")
applauseDsl_ViewSection = Class(name="applauseDsl::ViewSection")
applauseDsl_TableView = Class(name="applauseDsl::TableView")
SectionedView = Class(name="SectionedView")
applauseDsl_DetailsView = Class(name="applauseDsl::DetailsView")
applauseDsl_ViewCall = Class(name="applauseDsl::ViewCall")
ModelElement = Class(name="ModelElement")
applauseDsl_SimpleType = Class(name="applauseDsl::SimpleType")
Type = Class(name="Type")
applauseDsl_Entity = Class(name="applauseDsl::Entity")
applauseDsl_Property = Class(name="applauseDsl::Property")
applauseDsl_SectionCell = Class(name="applauseDsl::SectionCell")
applauseDsl_CollectionIterator = Class(name="applauseDsl::CollectionIterator")
applauseDsl_ViewAction = Class(name="applauseDsl::ViewAction")
applauseDsl_ViewHeader = Class(name="applauseDsl::ViewHeader")
applauseDsl_CustomView = Class(name="applauseDsl::CustomView")
applauseDsl_StringReplace = Class(name="applauseDsl::StringReplace")
applauseDsl_StringUrlConform = Class(name="applauseDsl::StringUrlConform")
applauseDsl_StringSplit = Class(name="applauseDsl::StringSplit")
CollectionFunction = Class(name="CollectionFunction")
applauseDsl_ComplexProviderConstruction = Class(name="applauseDsl::ComplexProviderConstruction")
ProviderConstruction = Class(name="ProviderConstruction")
applauseDsl_SimpleProviderConstruction = Class(name="applauseDsl::SimpleProviderConstruction")
applauseDsl_ExternalOpen = Class(name="applauseDsl::ExternalOpen")
ViewAction = Class(name="ViewAction")
applauseDsl_StringConcat = Class(name="applauseDsl::StringConcat")
StringFunction = Class(name="StringFunction")

# applauseDsl_Model class attributes and methods

# applauseDsl_Application class attributes and methods
applauseDsl_Application_name: Property = Property(name="name", type=StringType)
applauseDsl_Application.attributes={applauseDsl_Application_name}

# applauseDsl_ModelElement class attributes and methods
applauseDsl_ModelElement_name: Property = Property(name="name", type=StringType)
applauseDsl_ModelElement.attributes={applauseDsl_ModelElement_name}

# applauseDsl_Expression class attributes and methods

# applauseDsl_ScalarExpression class attributes and methods

# applauseDsl_CollectionExpression class attributes and methods

# applauseDsl_StringLiteral class attributes and methods
applauseDsl_StringLiteral_value: Property = Property(name="value", type=StringType)
applauseDsl_StringLiteral.attributes={applauseDsl_StringLiteral_value}

# applauseDsl_StringFunction class attributes and methods

# applauseDsl_CollectionLiteral class attributes and methods

# applauseDsl_CollectionFunction class attributes and methods

# applauseDsl_TabbarButton class attributes and methods

# applauseDsl_VariableDeclaration class attributes and methods
applauseDsl_VariableDeclaration_name: Property = Property(name="name", type=StringType)
applauseDsl_VariableDeclaration.attributes={applauseDsl_VariableDeclaration_name}

# applauseDsl_TypeDescription class attributes and methods
applauseDsl_TypeDescription_many: Property = Property(name="many", type=BooleanType)
applauseDsl_TypeDescription.attributes={applauseDsl_TypeDescription_many}

# applauseDsl_Type class attributes and methods

# applauseDsl_Parameter class attributes and methods

# VariableDeclaration class attributes and methods

# applauseDsl_ObjectReference class attributes and methods

# Expression class attributes and methods

# ScalarExpression class attributes and methods

# CollectionExpression class attributes and methods

# applauseDsl_ContentProvider class attributes and methods
applauseDsl_ContentProvider_many: Property = Property(name="many", type=BooleanType)
applauseDsl_ContentProvider.attributes={applauseDsl_ContentProvider_many}

# applauseDsl_ProviderConstruction class attributes and methods

# applauseDsl_View class attributes and methods

# applauseDsl_SectionedView class attributes and methods

# View class attributes and methods

# applauseDsl_ViewSection class attributes and methods

# applauseDsl_TableView class attributes and methods

# SectionedView class attributes and methods

# applauseDsl_DetailsView class attributes and methods

# applauseDsl_ViewCall class attributes and methods

# ModelElement class attributes and methods

# applauseDsl_SimpleType class attributes and methods
applauseDsl_SimpleType_platformType: Property = Property(name="platformType", type=StringType)
applauseDsl_SimpleType.attributes={applauseDsl_SimpleType_platformType}

# Type class attributes and methods

# applauseDsl_Entity class attributes and methods

# applauseDsl_Property class attributes and methods
applauseDsl_Property_derived: Property = Property(name="derived", type=BooleanType)
applauseDsl_Property.attributes={applauseDsl_Property_derived}

# applauseDsl_SectionCell class attributes and methods
applauseDsl_SectionCell_type: Property = Property(name="type", type=StringType)
applauseDsl_SectionCell.attributes={applauseDsl_SectionCell_type}

# applauseDsl_CollectionIterator class attributes and methods

# applauseDsl_ViewAction class attributes and methods

# applauseDsl_ViewHeader class attributes and methods

# applauseDsl_CustomView class attributes and methods
applauseDsl_CustomView_objclass: Property = Property(name="objclass", type=StringType)
applauseDsl_CustomView.attributes={applauseDsl_CustomView_objclass}

# applauseDsl_StringReplace class attributes and methods

# applauseDsl_StringUrlConform class attributes and methods

# applauseDsl_StringSplit class attributes and methods

# CollectionFunction class attributes and methods

# applauseDsl_ComplexProviderConstruction class attributes and methods

# ProviderConstruction class attributes and methods

# applauseDsl_SimpleProviderConstruction class attributes and methods

# applauseDsl_ExternalOpen class attributes and methods

# ViewAction class attributes and methods

# applauseDsl_StringConcat class attributes and methods

# StringFunction class attributes and methods

# Relationships
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
tail8: BinaryAssociation = BinaryAssociation(
    name="tail8",
    ends={
        Property(name="applauseDsl_ObjectReference9", type=applauseDsl_ObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ObjectReference7", type=applauseDsl_ObjectReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items10: BinaryAssociation = BinaryAssociation(
    name="items10",
    ends={
        Property(name="applauseDsl_ScalarExpression", type=applauseDsl_CollectionLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_CollectionLiteral", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
background11: BinaryAssociation = BinaryAssociation(
    name="background11",
    ends={
        Property(name="applauseDsl_ScalarExpression13", type=applauseDsl_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Application12", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buttons14: BinaryAssociation = BinaryAssociation(
    name="buttons14",
    ends={
        Property(name="applauseDsl_TabbarButton", type=applauseDsl_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Application15", type=applauseDsl_TabbarButton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title16: BinaryAssociation = BinaryAssociation(
    name="title16",
    ends={
        Property(name="applauseDsl_ScalarExpression18", type=applauseDsl_TabbarButton, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TabbarButton17", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="applauseDsl_Type", type=applauseDsl_TypeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TypeDescription", type=applauseDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
description4: BinaryAssociation = BinaryAssociation(
    name="description4",
    ends={
        Property(name="applauseDsl_TypeDescription5", type=applauseDsl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Parameter", type=applauseDsl_TypeDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object6: BinaryAssociation = BinaryAssociation(
    name="object6",
    ends={
        Property(name="applauseDsl_VariableDeclaration", type=applauseDsl_ObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ObjectReference", type=applauseDsl_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
description28: BinaryAssociation = BinaryAssociation(
    name="description28",
    ends={
        Property(name="applauseDsl_TypeDescription30", type=applauseDsl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Property29", type=applauseDsl_TypeDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter31: BinaryAssociation = BinaryAssociation(
    name="parameter31",
    ends={
        Property(name="applauseDsl_Parameter32", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="applauseDsl_Type35", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider34", type=applauseDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
url36: BinaryAssociation = BinaryAssociation(
    name="url36",
    ends={
        Property(name="applauseDsl_ScalarExpression38", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider37", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection39: BinaryAssociation = BinaryAssociation(
    name="selection39",
    ends={
        Property(name="applauseDsl_ScalarExpression41", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ContentProvider40", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content42: BinaryAssociation = BinaryAssociation(
    name="content42",
    ends={
        Property(name="applauseDsl_Parameter43", type=applauseDsl_View, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_View", type=applauseDsl_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title44: BinaryAssociation = BinaryAssociation(
    name="title44",
    ends={
        Property(name="applauseDsl_ScalarExpression45", type=applauseDsl_SectionedView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionedView", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections46: BinaryAssociation = BinaryAssociation(
    name="sections46",
    ends={
        Property(name="applauseDsl_ViewSection", type=applauseDsl_SectionedView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionedView47", type=applauseDsl_ViewSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icon19: BinaryAssociation = BinaryAssociation(
    name="icon19",
    ends={
        Property(name="applauseDsl_ScalarExpression21", type=applauseDsl_TabbarButton, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TabbarButton20", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
view22: BinaryAssociation = BinaryAssociation(
    name="view22",
    ends={
        Property(name="applauseDsl_ViewCall", type=applauseDsl_TabbarButton, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_TabbarButton23", type=applauseDsl_ViewCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends25: BinaryAssociation = BinaryAssociation(
    name="extends25",
    ends={
        Property(name="applauseDsl_Entity", type=applauseDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Entity24", type=applauseDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
properties26: BinaryAssociation = BinaryAssociation(
    name="properties26",
    ends={
        Property(name="applauseDsl_Property", type=applauseDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_Entity27", type=applauseDsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title61: BinaryAssociation = BinaryAssociation(
    name="title61",
    ends={
        Property(name="applauseDsl_ViewSection62", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="applauseDsl_ScalarExpression63", type=applauseDsl_ViewSection, multiplicity=Multiplicity(1, 1))
    }
)
cells64: BinaryAssociation = BinaryAssociation(
    name="cells64",
    ends={
        Property(name="applauseDsl_SectionCell", type=applauseDsl_ViewSection, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewSection65", type=applauseDsl_SectionCell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator66: BinaryAssociation = BinaryAssociation(
    name="iterator66",
    ends={
        Property(name="applauseDsl_CollectionIterator", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell67", type=applauseDsl_CollectionIterator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
text68: BinaryAssociation = BinaryAssociation(
    name="text68",
    ends={
        Property(name="applauseDsl_ScalarExpression70", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell69", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
details71: BinaryAssociation = BinaryAssociation(
    name="details71",
    ends={
        Property(name="applauseDsl_ScalarExpression73", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell72", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
image74: BinaryAssociation = BinaryAssociation(
    name="image74",
    ends={
        Property(name="applauseDsl_ScalarExpression76", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell75", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action77: BinaryAssociation = BinaryAssociation(
    name="action77",
    ends={
        Property(name="applauseDsl_ViewAction", type=applauseDsl_SectionCell, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SectionCell78", type=applauseDsl_ViewAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection79: BinaryAssociation = BinaryAssociation(
    name="collection79",
    ends={
        Property(name="applauseDsl_CollectionExpression", type=applauseDsl_CollectionIterator, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_CollectionIterator80", type=applauseDsl_CollectionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
header48: BinaryAssociation = BinaryAssociation(
    name="header48",
    ends={
        Property(name="applauseDsl_ViewHeader", type=applauseDsl_DetailsView, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_DetailsView", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
title49: BinaryAssociation = BinaryAssociation(
    name="title49",
    ends={
        Property(name="applauseDsl_ScalarExpression51", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewHeader50", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtitle52: BinaryAssociation = BinaryAssociation(
    name="subtitle52",
    ends={
        Property(name="applauseDsl_ScalarExpression54", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewHeader53", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
details55: BinaryAssociation = BinaryAssociation(
    name="details55",
    ends={
        Property(name="applauseDsl_ScalarExpression57", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewHeader56", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
image58: BinaryAssociation = BinaryAssociation(
    name="image58",
    ends={
        Property(name="applauseDsl_ScalarExpression60", type=applauseDsl_ViewHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewHeader59", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value90: BinaryAssociation = BinaryAssociation(
    name="value90",
    ends={
        Property(name="applauseDsl_ScalarExpression91", type=applauseDsl_StringReplace, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringReplace", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
match92: BinaryAssociation = BinaryAssociation(
    name="match92",
    ends={
        Property(name="applauseDsl_ScalarExpression94", type=applauseDsl_StringReplace, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringReplace93", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
replacement95: BinaryAssociation = BinaryAssociation(
    name="replacement95",
    ends={
        Property(name="applauseDsl_ScalarExpression97", type=applauseDsl_StringReplace, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringReplace96", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value98: BinaryAssociation = BinaryAssociation(
    name="value98",
    ends={
        Property(name="applauseDsl_ScalarExpression99", type=applauseDsl_StringUrlConform, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringUrlConform", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value100: BinaryAssociation = BinaryAssociation(
    name="value100",
    ends={
        Property(name="applauseDsl_ScalarExpression101", type=applauseDsl_StringSplit, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringSplit", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delimiter102: BinaryAssociation = BinaryAssociation(
    name="delimiter102",
    ends={
        Property(name="applauseDsl_ScalarExpression104", type=applauseDsl_StringSplit, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringSplit103", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
provider105: BinaryAssociation = BinaryAssociation(
    name="provider105",
    ends={
        Property(name="applauseDsl_ContentProvider106", type=applauseDsl_ComplexProviderConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ComplexProviderConstruction", type=applauseDsl_ContentProvider, multiplicity=Multiplicity(0, 1))
    }
)
argument107: BinaryAssociation = BinaryAssociation(
    name="argument107",
    ends={
        Property(name="applauseDsl_Expression", type=applauseDsl_ComplexProviderConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ComplexProviderConstruction108", type=applauseDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
url81: BinaryAssociation = BinaryAssociation(
    name="url81",
    ends={
        Property(name="applauseDsl_ScalarExpression82", type=applauseDsl_ExternalOpen, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ExternalOpen", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
view83: BinaryAssociation = BinaryAssociation(
    name="view83",
    ends={
        Property(name="applauseDsl_View85", type=applauseDsl_ViewCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewCall84", type=applauseDsl_View, multiplicity=Multiplicity(0, 1))
    }
)
provider86: BinaryAssociation = BinaryAssociation(
    name="provider86",
    ends={
        Property(name="applauseDsl_ProviderConstruction", type=applauseDsl_ViewCall, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_ViewCall87", type=applauseDsl_ProviderConstruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values88: BinaryAssociation = BinaryAssociation(
    name="values88",
    ends={
        Property(name="applauseDsl_ScalarExpression89", type=applauseDsl_StringConcat, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_StringConcat", type=applauseDsl_ScalarExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression109: BinaryAssociation = BinaryAssociation(
    name="expression109",
    ends={
        Property(name="applauseDsl_Expression110", type=applauseDsl_SimpleProviderConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="applauseDsl_SimpleProviderConstruction", type=applauseDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_applauseDsl_StringLiteral_Expression = Generalization(general=Expression, specific=applauseDsl_StringLiteral)
gen_applauseDsl_StringLiteral_ScalarExpression = Generalization(general=ScalarExpression, specific=applauseDsl_StringLiteral)
gen_applauseDsl_StringFunction_Expression = Generalization(general=Expression, specific=applauseDsl_StringFunction)
gen_applauseDsl_StringFunction_ScalarExpression = Generalization(general=ScalarExpression, specific=applauseDsl_StringFunction)
gen_applauseDsl_CollectionLiteral_Expression = Generalization(general=Expression, specific=applauseDsl_CollectionLiteral)
gen_applauseDsl_CollectionLiteral_CollectionExpression = Generalization(general=CollectionExpression, specific=applauseDsl_CollectionLiteral)
gen_applauseDsl_CollectionFunction_Expression = Generalization(general=Expression, specific=applauseDsl_CollectionFunction)
gen_applauseDsl_CollectionFunction_CollectionExpression = Generalization(general=CollectionExpression, specific=applauseDsl_CollectionFunction)
gen_applauseDsl_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=applauseDsl_Parameter)
gen_applauseDsl_ObjectReference_Expression = Generalization(general=Expression, specific=applauseDsl_ObjectReference)
gen_applauseDsl_ObjectReference_ScalarExpression = Generalization(general=ScalarExpression, specific=applauseDsl_ObjectReference)
gen_applauseDsl_ObjectReference_CollectionExpression = Generalization(general=CollectionExpression, specific=applauseDsl_ObjectReference)
gen_applauseDsl_ContentProvider_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_ContentProvider)
gen_applauseDsl_View_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_View)
gen_applauseDsl_SectionedView_View = Generalization(general=View, specific=applauseDsl_SectionedView)
gen_applauseDsl_TableView_SectionedView = Generalization(general=SectionedView, specific=applauseDsl_TableView)
gen_applauseDsl_DetailsView_SectionedView = Generalization(general=SectionedView, specific=applauseDsl_DetailsView)
gen_applauseDsl_Type_ModelElement = Generalization(general=ModelElement, specific=applauseDsl_Type)
gen_applauseDsl_SimpleType_Type = Generalization(general=Type, specific=applauseDsl_SimpleType)
gen_applauseDsl_Entity_Type = Generalization(general=Type, specific=applauseDsl_Entity)
gen_applauseDsl_Property_VariableDeclaration = Generalization(general=VariableDeclaration, specific=applauseDsl_Property)
gen_applauseDsl_CollectionIterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=applauseDsl_CollectionIterator)
gen_applauseDsl_CustomView_View = Generalization(general=View, specific=applauseDsl_CustomView)
gen_applauseDsl_StringReplace_StringFunction = Generalization(general=StringFunction, specific=applauseDsl_StringReplace)
gen_applauseDsl_StringUrlConform_StringFunction = Generalization(general=StringFunction, specific=applauseDsl_StringUrlConform)
gen_applauseDsl_StringSplit_CollectionFunction = Generalization(general=CollectionFunction, specific=applauseDsl_StringSplit)
gen_applauseDsl_ComplexProviderConstruction_ProviderConstruction = Generalization(general=ProviderConstruction, specific=applauseDsl_ComplexProviderConstruction)
gen_applauseDsl_SimpleProviderConstruction_ProviderConstruction = Generalization(general=ProviderConstruction, specific=applauseDsl_SimpleProviderConstruction)
gen_applauseDsl_ExternalOpen_ViewAction = Generalization(general=ViewAction, specific=applauseDsl_ExternalOpen)
gen_applauseDsl_ViewCall_ViewAction = Generalization(general=ViewAction, specific=applauseDsl_ViewCall)
gen_applauseDsl_StringConcat_StringFunction = Generalization(general=StringFunction, specific=applauseDsl_StringConcat)

# Domain Model
domain_model = DomainModel(
    name="applauseDsl",
    types={applauseDsl_Model, applauseDsl_Application, applauseDsl_ModelElement, applauseDsl_Expression, applauseDsl_ScalarExpression, applauseDsl_CollectionExpression, applauseDsl_StringLiteral, applauseDsl_StringFunction, applauseDsl_CollectionLiteral, applauseDsl_CollectionFunction, applauseDsl_TabbarButton, applauseDsl_VariableDeclaration, applauseDsl_TypeDescription, applauseDsl_Type, applauseDsl_Parameter, VariableDeclaration, applauseDsl_ObjectReference, Expression, ScalarExpression, CollectionExpression, applauseDsl_ContentProvider, applauseDsl_ProviderConstruction, applauseDsl_View, applauseDsl_SectionedView, View, applauseDsl_ViewSection, applauseDsl_TableView, SectionedView, applauseDsl_DetailsView, applauseDsl_ViewCall, ModelElement, applauseDsl_SimpleType, Type, applauseDsl_Entity, applauseDsl_Property, applauseDsl_SectionCell, applauseDsl_CollectionIterator, applauseDsl_ViewAction, applauseDsl_ViewHeader, applauseDsl_CustomView, applauseDsl_StringReplace, applauseDsl_StringUrlConform, applauseDsl_StringSplit, CollectionFunction, applauseDsl_ComplexProviderConstruction, ProviderConstruction, applauseDsl_SimpleProviderConstruction, applauseDsl_ExternalOpen, ViewAction, applauseDsl_StringConcat, StringFunction, CellType},
    associations={application0, elements1, tail8, items10, background11, buttons14, title16, type3, description4, object6, description28, parameter31, type33, url36, selection39, content42, title44, sections46, icon19, view22, extends25, properties26, title61, cells64, iterator66, text68, details71, image74, action77, collection79, header48, title49, subtitle52, details55, image58, value90, match92, replacement95, value98, value100, delimiter102, provider105, argument107, url81, view83, provider86, values88, expression109},
    generalizations={gen_applauseDsl_StringLiteral_Expression, gen_applauseDsl_StringLiteral_ScalarExpression, gen_applauseDsl_StringFunction_Expression, gen_applauseDsl_StringFunction_ScalarExpression, gen_applauseDsl_CollectionLiteral_Expression, gen_applauseDsl_CollectionLiteral_CollectionExpression, gen_applauseDsl_CollectionFunction_Expression, gen_applauseDsl_CollectionFunction_CollectionExpression, gen_applauseDsl_Parameter_VariableDeclaration, gen_applauseDsl_ObjectReference_Expression, gen_applauseDsl_ObjectReference_ScalarExpression, gen_applauseDsl_ObjectReference_CollectionExpression, gen_applauseDsl_ContentProvider_ModelElement, gen_applauseDsl_View_ModelElement, gen_applauseDsl_SectionedView_View, gen_applauseDsl_TableView_SectionedView, gen_applauseDsl_DetailsView_SectionedView, gen_applauseDsl_Type_ModelElement, gen_applauseDsl_SimpleType_Type, gen_applauseDsl_Entity_Type, gen_applauseDsl_Property_VariableDeclaration, gen_applauseDsl_CollectionIterator_VariableDeclaration, gen_applauseDsl_CustomView_View, gen_applauseDsl_StringReplace_StringFunction, gen_applauseDsl_StringUrlConform_StringFunction, gen_applauseDsl_StringSplit_CollectionFunction, gen_applauseDsl_ComplexProviderConstruction_ProviderConstruction, gen_applauseDsl_SimpleProviderConstruction_ProviderConstruction, gen_applauseDsl_ExternalOpen_ViewAction, gen_applauseDsl_ViewCall_ViewAction, gen_applauseDsl_StringConcat_StringFunction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)