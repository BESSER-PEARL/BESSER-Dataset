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
ModelPropertyType: Enumeration = Enumeration(
    name="ModelPropertyType",
    literals={
            EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="DATETIME"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="DOUBLE")
    }
)

Cardinality: Enumeration = Enumeration(
    name="Cardinality",
    literals={
            EnumerationLiteral(name="MANY_TO_MANY"),
			EnumerationLiteral(name="ONE_TO_MANY"),
			EnumerationLiteral(name="ONE_TO_ONE")
    }
)

ActionMethodParameterType: Enumeration = Enumeration(
    name="ActionMethodParameterType",
    literals={
            EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="STRING")
    }
)

RequestType: Enumeration = Enumeration(
    name="RequestType",
    literals={
            EnumerationLiteral(name="REGULAR_HTTP"),
			EnumerationLiteral(name="AJAX")
    }
)

HttpMethod: Enumeration = Enumeration(
    name="HttpMethod",
    literals={
            EnumerationLiteral(name="GET"),
			EnumerationLiteral(name="POST")
    }
)

ModelCardinality: Enumeration = Enumeration(
    name="ModelCardinality",
    literals={
            EnumerationLiteral(name="ONE"),
			EnumerationLiteral(name="ALL")
    }
)

ModelOperation: Enumeration = Enumeration(
    name="ModelOperation",
    literals={
            EnumerationLiteral(name="CREATE"),
			EnumerationLiteral(name="READ"),
			EnumerationLiteral(name="UPDATE"),
			EnumerationLiteral(name="DELETE")
    }
)

ActionMethodReturnType: Enumeration = Enumeration(
    name="ActionMethodReturnType",
    literals={
            EnumerationLiteral(name="View"),
			EnumerationLiteral(name="PartialView"),
			EnumerationLiteral(name="RedirectToAction"),
			EnumerationLiteral(name="Json"),
			EnumerationLiteral(name="Content")
    }
)

ButtonType: Enumeration = Enumeration(
    name="ButtonType",
    literals={
            EnumerationLiteral(name="SUBMIT"),
			EnumerationLiteral(name="RESET")
    }
)

InputDataType: Enumeration = Enumeration(
    name="InputDataType",
    literals={
            EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="NUMBER"),
			EnumerationLiteral(name="PASSWORD"),
			EnumerationLiteral(name="EMAIL"),
			EnumerationLiteral(name="TEL"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="FILE")
    }
)

MultipleChoiceType: Enumeration = Enumeration(
    name="MultipleChoiceType",
    literals={
            EnumerationLiteral(name="CHECKBOX_GROUP"),
			EnumerationLiteral(name="DROPDOWN_LIST"),
			EnumerationLiteral(name="RADIO_BUTTON")
    }
)

# Classes
ryz_Package = Class(name="ryz::Package", is_abstract=True)
ryz_ComponentPackage = Class(name="ryz::ComponentPackage", is_abstract=True)
Package = Class(name="Package")
ryz_MvcPackage = Class(name="ryz::MvcPackage")
ryz_Project = Class(name="ryz::Project")
NamedElement = Class(name="NamedElement")
ryz_ViewPackage = Class(name="ryz::ViewPackage")
ryz_AbstractView = Class(name="ryz::AbstractView", is_abstract=True)
ryz_ControllerPackage = Class(name="ryz::ControllerPackage")
ryz_Controller = Class(name="ryz::Controller")
ryz_MainComponent = Class(name="ryz::MainComponent", is_abstract=True)
ryz_MainComponentRelation = Class(name="ryz::MainComponentRelation", is_abstract=True)
ryz_NamedElement = Class(name="ryz::NamedElement", is_abstract=True)
ryz_ModelPackage = Class(name="ryz::ModelPackage")
ComponentPackage = Class(name="ComponentPackage")
ryz_Model = Class(name="ryz::Model")
ryz_ModelAssociation = Class(name="ryz::ModelAssociation")
ryz_Partial = Class(name="ryz::Partial")
ryz_HelperForSendingRequest = Class(name="ryz::HelperForSendingRequest", is_abstract=True)
ryz_PresentationElement = Class(name="ryz::PresentationElement", is_abstract=True)
MainComponent = Class(name="MainComponent")
ryz_Property = Class(name="ryz::Property")
ryz_TableKey = Class(name="ryz::TableKey")
ryz_ActionMethod = Class(name="ryz::ActionMethod")
ryz_UseCase = Class(name="ryz::UseCase")
ryz_Layout = Class(name="ryz::Layout")
ryz_View = Class(name="ryz::View")
AbstractView = Class(name="AbstractView")
ryz_Parameter = Class(name="ryz::Parameter")
ryz_ViewToControllerRelation = Class(name="ryz::ViewToControllerRelation")
MainComponentRelation = Class(name="MainComponentRelation")
ryz_ActionLink = Class(name="ryz::ActionLink")
HelperForSendingRequest = Class(name="HelperForSendingRequest")
ryz_Form = Class(name="ryz::Form")
ryz_ControllerToModelRelation = Class(name="ryz::ControllerToModelRelation")
ryz_ControllerToViewRelation = Class(name="ryz::ControllerToViewRelation")
ryz_UseCaseActorPackage = Class(name="ryz::UseCaseActorPackage")
ryz_Actor = Class(name="ryz::Actor")
ryz_UseCasePackage = Class(name="ryz::UseCasePackage")
ryz_ViewToModelRelation = Class(name="ryz::ViewToModelRelation")
ryz_PresentationForm = Class(name="ryz::PresentationForm")
PresentationElement = Class(name="PresentationElement")
ryz_PresentationFormElement = Class(name="ryz::PresentationFormElement", is_abstract=True)
ryz_MultipleChoice = Class(name="ryz::MultipleChoice")
PresentationFormElement = Class(name="PresentationFormElement")
ryz_Choice = Class(name="ryz::Choice")
ryz_Button = Class(name="ryz::Button")
ryz_Input = Class(name="ryz::Input")
ryz_FormElementToPropertyKeyRelation = Class(name="ryz::FormElementToPropertyKeyRelation")
ryz_Link = Class(name="ryz::Link")
ryz_Table = Class(name="ryz::Table")
ryz_Header = Class(name="ryz::Header")
ryz_PresentationFormElementToPropertyKey = Class(name="ryz::PresentationFormElementToPropertyKey")

# ryz_Package class attributes and methods

# ryz_ComponentPackage class attributes and methods

# Package class attributes and methods

# ryz_MvcPackage class attributes and methods

# ryz_Project class attributes and methods

# NamedElement class attributes and methods

# ryz_ViewPackage class attributes and methods

# ryz_AbstractView class attributes and methods

# ryz_ControllerPackage class attributes and methods

# ryz_Controller class attributes and methods

# ryz_MainComponent class attributes and methods

# ryz_MainComponentRelation class attributes and methods

# ryz_NamedElement class attributes and methods
ryz_NamedElement_name: Property = Property(name="name", type=StringType)
ryz_NamedElement.attributes={ryz_NamedElement_name}

# ryz_ModelPackage class attributes and methods

# ComponentPackage class attributes and methods

# ryz_Model class attributes and methods
ryz_Model_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
ryz_Model.attributes={ryz_Model_isAbstract}

# ryz_ModelAssociation class attributes and methods
ryz_ModelAssociation_cardinality: Property = Property(name="cardinality", type=StringType)
ryz_ModelAssociation_isRequired: Property = Property(name="isRequired", type=BooleanType)
ryz_ModelAssociation_principalRoleName: Property = Property(name="principalRoleName", type=StringType)
ryz_ModelAssociation_dependentRoleName: Property = Property(name="dependentRoleName", type=StringType)
ryz_ModelAssociation.attributes={ryz_ModelAssociation_principalRoleName, ryz_ModelAssociation_dependentRoleName, ryz_ModelAssociation_isRequired, ryz_ModelAssociation_cardinality}

# ryz_Partial class attributes and methods

# ryz_HelperForSendingRequest class attributes and methods
ryz_HelperForSendingRequest_requestType: Property = Property(name="requestType", type=StringType)
ryz_HelperForSendingRequest_httpMethod: Property = Property(name="httpMethod", type=StringType)
ryz_HelperForSendingRequest_text: Property = Property(name="text", type=StringType)
ryz_HelperForSendingRequest.attributes={ryz_HelperForSendingRequest_httpMethod, ryz_HelperForSendingRequest_requestType, ryz_HelperForSendingRequest_text}

# ryz_PresentationElement class attributes and methods

# MainComponent class attributes and methods

# ryz_Property class attributes and methods
ryz_Property_type: Property = Property(name="type", type=StringType)
ryz_Property_isRequired: Property = Property(name="isRequired", type=BooleanType)
ryz_Property.attributes={ryz_Property_type, ryz_Property_isRequired}

# ryz_TableKey class attributes and methods
ryz_TableKey_type: Property = Property(name="type", type=StringType)
ryz_TableKey_isRequired: Property = Property(name="isRequired", type=BooleanType)
ryz_TableKey_isPrimaryKey: Property = Property(name="isPrimaryKey", type=BooleanType)
ryz_TableKey_isForeignKey: Property = Property(name="isForeignKey", type=BooleanType)
ryz_TableKey.attributes={ryz_TableKey_isForeignKey, ryz_TableKey_isPrimaryKey, ryz_TableKey_isRequired, ryz_TableKey_type}

# ryz_ActionMethod class attributes and methods
ryz_ActionMethod_returns: Property = Property(name="returns", type=StringType)
ryz_ActionMethod_httpMethod: Property = Property(name="httpMethod", type=StringType)
ryz_ActionMethod.attributes={ryz_ActionMethod_returns, ryz_ActionMethod_httpMethod}

# ryz_UseCase class attributes and methods

# ryz_Layout class attributes and methods

# ryz_View class attributes and methods

# AbstractView class attributes and methods

# ryz_Parameter class attributes and methods
ryz_Parameter_type: Property = Property(name="type", type=StringType)
ryz_Parameter_isNullable: Property = Property(name="isNullable", type=BooleanType)
ryz_Parameter_isList: Property = Property(name="isList", type=BooleanType)
ryz_Parameter.attributes={ryz_Parameter_type, ryz_Parameter_isList, ryz_Parameter_isNullable}

# ryz_ViewToControllerRelation class attributes and methods

# MainComponentRelation class attributes and methods

# ryz_ActionLink class attributes and methods

# HelperForSendingRequest class attributes and methods

# ryz_Form class attributes and methods

# ryz_ControllerToModelRelation class attributes and methods
ryz_ControllerToModelRelation_modelCardinality: Property = Property(name="modelCardinality", type=StringType)
ryz_ControllerToModelRelation_modelOperation: Property = Property(name="modelOperation", type=StringType)
ryz_ControllerToModelRelation.attributes={ryz_ControllerToModelRelation_modelOperation, ryz_ControllerToModelRelation_modelCardinality}

# ryz_ControllerToViewRelation class attributes and methods

# ryz_UseCaseActorPackage class attributes and methods

# ryz_Actor class attributes and methods

# ryz_UseCasePackage class attributes and methods

# ryz_ViewToModelRelation class attributes and methods
ryz_ViewToModelRelation_modelcardinality: Property = Property(name="modelcardinality", type=StringType)
ryz_ViewToModelRelation.attributes={ryz_ViewToModelRelation_modelcardinality}

# ryz_PresentationForm class attributes and methods

# PresentationElement class attributes and methods

# ryz_PresentationFormElement class attributes and methods
ryz_PresentationFormElement_labelText: Property = Property(name="labelText", type=StringType)
ryz_PresentationFormElement.attributes={ryz_PresentationFormElement_labelText}

# ryz_MultipleChoice class attributes and methods
ryz_MultipleChoice_multipleChoiceType: Property = Property(name="multipleChoiceType", type=StringType)
ryz_MultipleChoice_multipleSelection: Property = Property(name="multipleSelection", type=BooleanType)
ryz_MultipleChoice.attributes={ryz_MultipleChoice_multipleChoiceType, ryz_MultipleChoice_multipleSelection}

# PresentationFormElement class attributes and methods

# ryz_Choice class attributes and methods
ryz_Choice_text: Property = Property(name="text", type=StringType)
ryz_Choice_value: Property = Property(name="value", type=StringType)
ryz_Choice_selected: Property = Property(name="selected", type=StringType)
ryz_Choice.attributes={ryz_Choice_selected, ryz_Choice_value, ryz_Choice_text}

# ryz_Button class attributes and methods
ryz_Button_buttonType: Property = Property(name="buttonType", type=StringType)
ryz_Button.attributes={ryz_Button_buttonType}

# ryz_Input class attributes and methods
ryz_Input_inputDataType: Property = Property(name="inputDataType", type=StringType)
ryz_Input_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
ryz_Input_isHidden: Property = Property(name="isHidden", type=BooleanType)
ryz_Input.attributes={ryz_Input_isHidden, ryz_Input_inputDataType, ryz_Input_isReadOnly}

# ryz_FormElementToPropertyKeyRelation class attributes and methods

# ryz_Link class attributes and methods
ryz_Link_text: Property = Property(name="text", type=StringType)
ryz_Link.attributes={ryz_Link_text}

# ryz_Table class attributes and methods

# ryz_Header class attributes and methods
ryz_Header_name: Property = Property(name="name", type=StringType)
ryz_Header_labelText: Property = Property(name="labelText", type=StringType)
ryz_Header.attributes={ryz_Header_labelText, ryz_Header_name}

# ryz_PresentationFormElementToPropertyKey class attributes and methods

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="ryz_Package", type=ryz_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_Project", type=ryz_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelassociations5: BinaryAssociation = BinaryAssociation(
    name="modelassociations5",
    ends={
        Property(name="ryz_ModelAssociation", type=ryz_ModelPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ModelPackage6", type=ryz_ModelAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views7: BinaryAssociation = BinaryAssociation(
    name="views7",
    ends={
        Property(name="ryz_AbstractView", type=ryz_ViewPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ViewPackage", type=ryz_AbstractView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maincomponents1: BinaryAssociation = BinaryAssociation(
    name="maincomponents1",
    ends={
        Property(name="ryz_MainComponent", type=ryz_MvcPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_MvcPackage", type=ryz_MainComponent, multiplicity=Multiplicity(0, 9999))
    }
)
maincomponentrelations2: BinaryAssociation = BinaryAssociation(
    name="maincomponentrelations2",
    ends={
        Property(name="ryz_MainComponentRelation", type=ryz_MvcPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_MvcPackage3", type=ryz_MainComponentRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
models4: BinaryAssociation = BinaryAssociation(
    name="models4",
    ends={
        Property(name="ryz_Model", type=ryz_ModelPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ModelPackage", type=ryz_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
renders16: BinaryAssociation = BinaryAssociation(
    name="renders16",
    ends={
        Property(name="ryz_Partial", type=ryz_AbstractView, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_AbstractView17", type=ryz_Partial, multiplicity=Multiplicity(0, 9999))
    }
)
htmlelements18: BinaryAssociation = BinaryAssociation(
    name="htmlelements18",
    ends={
        Property(name="ryz_HelperForSendingRequest", type=ryz_AbstractView, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_AbstractView19", type=ryz_HelperForSendingRequest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
presentationelement20: BinaryAssociation = BinaryAssociation(
    name="presentationelement20",
    ends={
        Property(name="ryz_PresentationElement", type=ryz_AbstractView, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_AbstractView21", type=ryz_PresentationElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controllers8: BinaryAssociation = BinaryAssociation(
    name="controllers8",
    ends={
        Property(name="ryz_Controller", type=ryz_ControllerPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ControllerPackage", type=ryz_Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="ryz_Property", type=ryz_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_Model10", type=ryz_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inherits12: BinaryAssociation = BinaryAssociation(
    name="inherits12",
    ends={
        Property(name="ryz_Model13", type=ryz_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_Model11", type=ryz_Model, multiplicity=Multiplicity(0, 1))
    }
)
tablekeys14: BinaryAssociation = BinaryAssociation(
    name="tablekeys14",
    ends={
        Property(name="ryz_TableKey", type=ryz_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_Model15", type=ryz_TableKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
principal24: BinaryAssociation = BinaryAssociation(
    name="principal24",
    ends={
        Property(name="ryz_Model26", type=ryz_ModelAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ModelAssociation25", type=ryz_Model, multiplicity=Multiplicity(1, 1))
    }
)
dependent27: BinaryAssociation = BinaryAssociation(
    name="dependent27",
    ends={
        Property(name="ryz_Model29", type=ryz_ModelAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ModelAssociation28", type=ryz_Model, multiplicity=Multiplicity(1, 1))
    }
)
actionmethods22: BinaryAssociation = BinaryAssociation(
    name="actionmethods22",
    ends={
        Property(name="ryz_ActionMethod", type=ryz_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_Controller23", type=ryz_ActionMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters30: BinaryAssociation = BinaryAssociation(
    name="parameters30",
    ends={
        Property(name="ryz_Parameter", type=ryz_ActionMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ActionMethod31", type=ryz_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usecase32: BinaryAssociation = BinaryAssociation(
    name="usecase32",
    ends={
        Property(name="UseCase", type=ryz_ActionMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="actionmethod", type=ryz_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
helperforsendingrequest34: BinaryAssociation = BinaryAssociation(
    name="helperforsendingrequest34",
    ends={
        Property(name="ryz_HelperForSendingRequest35", type=ryz_ViewToControllerRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ViewToControllerRelation", type=ryz_HelperForSendingRequest, multiplicity=Multiplicity(1, 1))
    }
)
actionmethod36: BinaryAssociation = BinaryAssociation(
    name="actionmethod36",
    ends={
        Property(name="ryz_ActionMethod38", type=ryz_ViewToControllerRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ViewToControllerRelation37", type=ryz_ActionMethod, multiplicity=Multiplicity(1, 1))
    }
)
model39: BinaryAssociation = BinaryAssociation(
    name="model39",
    ends={
        Property(name="ryz_Model41", type=ryz_ViewToControllerRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ViewToControllerRelation40", type=ryz_Model, multiplicity=Multiplicity(0, 1))
    }
)
layout33: BinaryAssociation = BinaryAssociation(
    name="layout33",
    ends={
        Property(name="ryz_Layout", type=ryz_View, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_View", type=ryz_Layout, multiplicity=Multiplicity(0, 1))
    }
)
properties42: BinaryAssociation = BinaryAssociation(
    name="properties42",
    ends={
        Property(name="ryz_Property44", type=ryz_ViewToControllerRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ViewToControllerRelation43", type=ryz_Property, multiplicity=Multiplicity(0, 9999))
    }
)
actionmethod45: BinaryAssociation = BinaryAssociation(
    name="actionmethod45",
    ends={
        Property(name="ryz_ActionMethod46", type=ryz_ControllerToModelRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ControllerToModelRelation", type=ryz_ActionMethod, multiplicity=Multiplicity(1, 1))
    }
)
model47: BinaryAssociation = BinaryAssociation(
    name="model47",
    ends={
        Property(name="ryz_Model49", type=ryz_ControllerToModelRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ControllerToModelRelation48", type=ryz_Model, multiplicity=Multiplicity(1, 1))
    }
)
modelproperties50: BinaryAssociation = BinaryAssociation(
    name="modelproperties50",
    ends={
        Property(name="ryz_Property52", type=ryz_ControllerToModelRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ControllerToModelRelation51", type=ryz_Property, multiplicity=Multiplicity(0, 9999))
    }
)
presentationelement55: BinaryAssociation = BinaryAssociation(
    name="presentationelement55",
    ends={
        Property(name="PresentationElement", type=ryz_HelperForSendingRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="helperforsendingrequest56", type=ryz_PresentationElement, multiplicity=Multiplicity(0, 9999))
    }
)
usecase53: BinaryAssociation = BinaryAssociation(
    name="usecase53",
    ends={
        Property(name="UseCase54", type=ryz_HelperForSendingRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="helperforsendingrequest", type=ryz_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
actionmethod57: BinaryAssociation = BinaryAssociation(
    name="actionmethod57",
    ends={
        Property(name="ryz_ActionMethod58", type=ryz_ControllerToViewRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ControllerToViewRelation", type=ryz_ActionMethod, multiplicity=Multiplicity(1, 1))
    }
)
returns59: BinaryAssociation = BinaryAssociation(
    name="returns59",
    ends={
        Property(name="ryz_AbstractView61", type=ryz_ControllerToViewRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ControllerToViewRelation60", type=ryz_AbstractView, multiplicity=Multiplicity(1, 1))
    }
)
actors70: BinaryAssociation = BinaryAssociation(
    name="actors70",
    ends={
        Property(name="ryz_Actor", type=ryz_UseCaseActorPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_UseCaseActorPackage", type=ryz_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usecasepackages71: BinaryAssociation = BinaryAssociation(
    name="usecasepackages71",
    ends={
        Property(name="ryz_UseCasePackage", type=ryz_UseCaseActorPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_UseCaseActorPackage72", type=ryz_UseCasePackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstractview62: BinaryAssociation = BinaryAssociation(
    name="abstractview62",
    ends={
        Property(name="ryz_AbstractView63", type=ryz_ViewToModelRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ViewToModelRelation", type=ryz_AbstractView, multiplicity=Multiplicity(1, 1))
    }
)
model64: BinaryAssociation = BinaryAssociation(
    name="model64",
    ends={
        Property(name="ryz_Model66", type=ryz_ViewToModelRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ViewToModelRelation65", type=ryz_Model, multiplicity=Multiplicity(1, 1))
    }
)
properties67: BinaryAssociation = BinaryAssociation(
    name="properties67",
    ends={
        Property(name="ryz_Property69", type=ryz_ViewToModelRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_ViewToModelRelation68", type=ryz_Property, multiplicity=Multiplicity(0, 9999))
    }
)
usecases80: BinaryAssociation = BinaryAssociation(
    name="usecases80",
    ends={
        Property(name="ryz_UseCase", type=ryz_UseCasePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_UseCasePackage81", type=ryz_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helperforsendingrequest82: BinaryAssociation = BinaryAssociation(
    name="helperforsendingrequest82",
    ends={
        Property(name="HelperForSendingRequest83", type=ryz_PresentationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="presentationelement", type=ryz_HelperForSendingRequest, multiplicity=Multiplicity(0, 9999))
    }
)
usecase73: BinaryAssociation = BinaryAssociation(
    name="usecase73",
    ends={
        Property(name="UseCase74", type=ryz_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actor", type=ryz_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
actor75: BinaryAssociation = BinaryAssociation(
    name="actor75",
    ends={
        Property(name="Actor", type=ryz_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="usecase", type=ryz_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
helperforsendingrequest76: BinaryAssociation = BinaryAssociation(
    name="helperforsendingrequest76",
    ends={
        Property(name="HelperForSendingRequest", type=ryz_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="usecase77", type=ryz_HelperForSendingRequest, multiplicity=Multiplicity(0, 9999))
    }
)
actionmethod78: BinaryAssociation = BinaryAssociation(
    name="actionmethod78",
    ends={
        Property(name="ActionMethod", type=ryz_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="usecase79", type=ryz_ActionMethod, multiplicity=Multiplicity(0, 9999))
    }
)
presentationformelement84: BinaryAssociation = BinaryAssociation(
    name="presentationformelement84",
    ends={
        Property(name="ryz_PresentationFormElement", type=ryz_PresentationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_PresentationForm", type=ryz_PresentationFormElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choice85: BinaryAssociation = BinaryAssociation(
    name="choice85",
    ends={
        Property(name="ryz_Choice", type=ryz_MultipleChoice, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_MultipleChoice", type=ryz_Choice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helperforsendingrequest87: BinaryAssociation = BinaryAssociation(
    name="helperforsendingrequest87",
    ends={
        Property(name="ryz_HelperForSendingRequest88", type=ryz_FormElementToPropertyKeyRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_FormElementToPropertyKeyRelation", type=ryz_HelperForSendingRequest, multiplicity=Multiplicity(1, 1))
    }
)
model89: BinaryAssociation = BinaryAssociation(
    name="model89",
    ends={
        Property(name="ryz_Model91", type=ryz_FormElementToPropertyKeyRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_FormElementToPropertyKeyRelation90", type=ryz_Model, multiplicity=Multiplicity(1, 1))
    }
)
header86: BinaryAssociation = BinaryAssociation(
    name="header86",
    ends={
        Property(name="ryz_Header", type=ryz_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_Table", type=ryz_Header, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
presentationformelementtoproperty92: BinaryAssociation = BinaryAssociation(
    name="presentationformelementtoproperty92",
    ends={
        Property(name="ryz_PresentationFormElementToPropertyKey", type=ryz_FormElementToPropertyKeyRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_FormElementToPropertyKeyRelation93", type=ryz_PresentationFormElementToPropertyKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
presentationformelement94: BinaryAssociation = BinaryAssociation(
    name="presentationformelement94",
    ends={
        Property(name="ryz_PresentationFormElement96", type=ryz_PresentationFormElementToPropertyKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_PresentationFormElementToPropertyKey95", type=ryz_PresentationFormElement, multiplicity=Multiplicity(1, 1))
    }
)
property97: BinaryAssociation = BinaryAssociation(
    name="property97",
    ends={
        Property(name="ryz_Property99", type=ryz_PresentationFormElementToPropertyKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_PresentationFormElementToPropertyKey98", type=ryz_Property, multiplicity=Multiplicity(0, 1))
    }
)
tablekey100: BinaryAssociation = BinaryAssociation(
    name="tablekey100",
    ends={
        Property(name="ryz_TableKey102", type=ryz_PresentationFormElementToPropertyKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ryz_PresentationFormElementToPropertyKey101", type=ryz_TableKey, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ryz_Package_NamedElement = Generalization(general=NamedElement, specific=ryz_Package)
gen_ryz_ComponentPackage_Package = Generalization(general=Package, specific=ryz_ComponentPackage)
gen_ryz_MvcPackage_Package = Generalization(general=Package, specific=ryz_MvcPackage)
gen_ryz_Project_NamedElement = Generalization(general=NamedElement, specific=ryz_Project)
gen_ryz_ViewPackage_ComponentPackage = Generalization(general=ComponentPackage, specific=ryz_ViewPackage)
gen_ryz_ControllerPackage_ComponentPackage = Generalization(general=ComponentPackage, specific=ryz_ControllerPackage)
gen_ryz_ModelPackage_ComponentPackage = Generalization(general=ComponentPackage, specific=ryz_ModelPackage)
gen_ryz_Model_MainComponent = Generalization(general=MainComponent, specific=ryz_Model)
gen_ryz_AbstractView_MainComponent = Generalization(general=MainComponent, specific=ryz_AbstractView)
gen_ryz_ModelAssociation_NamedElement = Generalization(general=NamedElement, specific=ryz_ModelAssociation)
gen_ryz_Controller_MainComponent = Generalization(general=MainComponent, specific=ryz_Controller)
gen_ryz_MainComponent_NamedElement = Generalization(general=NamedElement, specific=ryz_MainComponent)
gen_ryz_Property_NamedElement = Generalization(general=NamedElement, specific=ryz_Property)
gen_ryz_Layout_AbstractView = Generalization(general=AbstractView, specific=ryz_Layout)
gen_ryz_View_AbstractView = Generalization(general=AbstractView, specific=ryz_View)
gen_ryz_Partial_AbstractView = Generalization(general=AbstractView, specific=ryz_Partial)
gen_ryz_ActionMethod_NamedElement = Generalization(general=NamedElement, specific=ryz_ActionMethod)
gen_ryz_Parameter_NamedElement = Generalization(general=NamedElement, specific=ryz_Parameter)
gen_ryz_MainComponentRelation_NamedElement = Generalization(general=NamedElement, specific=ryz_MainComponentRelation)
gen_ryz_ViewToControllerRelation_MainComponentRelation = Generalization(general=MainComponentRelation, specific=ryz_ViewToControllerRelation)
gen_ryz_ActionLink_HelperForSendingRequest = Generalization(general=HelperForSendingRequest, specific=ryz_ActionLink)
gen_ryz_Form_HelperForSendingRequest = Generalization(general=HelperForSendingRequest, specific=ryz_Form)
gen_ryz_ControllerToModelRelation_MainComponentRelation = Generalization(general=MainComponentRelation, specific=ryz_ControllerToModelRelation)
gen_ryz_TableKey_NamedElement = Generalization(general=NamedElement, specific=ryz_TableKey)
gen_ryz_ControllerToViewRelation_MainComponentRelation = Generalization(general=MainComponentRelation, specific=ryz_ControllerToViewRelation)
gen_ryz_UseCaseActorPackage_Package = Generalization(general=Package, specific=ryz_UseCaseActorPackage)
gen_ryz_ViewToModelRelation_MainComponentRelation = Generalization(general=MainComponentRelation, specific=ryz_ViewToModelRelation)
gen_ryz_UseCasePackage_NamedElement = Generalization(general=NamedElement, specific=ryz_UseCasePackage)
gen_ryz_PresentationElement_NamedElement = Generalization(general=NamedElement, specific=ryz_PresentationElement)
gen_ryz_Actor_NamedElement = Generalization(general=NamedElement, specific=ryz_Actor)
gen_ryz_UseCase_NamedElement = Generalization(general=NamedElement, specific=ryz_UseCase)
gen_ryz_PresentationForm_PresentationElement = Generalization(general=PresentationElement, specific=ryz_PresentationForm)
gen_ryz_MultipleChoice_PresentationFormElement = Generalization(general=PresentationFormElement, specific=ryz_MultipleChoice)
gen_ryz_Button_PresentationFormElement = Generalization(general=PresentationFormElement, specific=ryz_Button)
gen_ryz_Input_PresentationFormElement = Generalization(general=PresentationFormElement, specific=ryz_Input)
gen_ryz_FormElementToPropertyKeyRelation_MainComponentRelation = Generalization(general=MainComponentRelation, specific=ryz_FormElementToPropertyKeyRelation)
gen_ryz_Link_PresentationElement = Generalization(general=PresentationElement, specific=ryz_Link)
gen_ryz_Table_PresentationElement = Generalization(general=PresentationElement, specific=ryz_Table)

# Domain Model
domain_model = DomainModel(
    name="ryz",
    types={ryz_Package, ryz_ComponentPackage, Package, ryz_MvcPackage, ryz_Project, NamedElement, ryz_ViewPackage, ryz_AbstractView, ryz_ControllerPackage, ryz_Controller, ryz_MainComponent, ryz_MainComponentRelation, ryz_NamedElement, ryz_ModelPackage, ComponentPackage, ryz_Model, ryz_ModelAssociation, ryz_Partial, ryz_HelperForSendingRequest, ryz_PresentationElement, MainComponent, ryz_Property, ryz_TableKey, ryz_ActionMethod, ryz_UseCase, ryz_Layout, ryz_View, AbstractView, ryz_Parameter, ryz_ViewToControllerRelation, MainComponentRelation, ryz_ActionLink, HelperForSendingRequest, ryz_Form, ryz_ControllerToModelRelation, ryz_ControllerToViewRelation, ryz_UseCaseActorPackage, ryz_Actor, ryz_UseCasePackage, ryz_ViewToModelRelation, ryz_PresentationForm, PresentationElement, ryz_PresentationFormElement, ryz_MultipleChoice, PresentationFormElement, ryz_Choice, ryz_Button, ryz_Input, ryz_FormElementToPropertyKeyRelation, ryz_Link, ryz_Table, ryz_Header, ryz_PresentationFormElementToPropertyKey, ModelPropertyType, Cardinality, ActionMethodParameterType, RequestType, HttpMethod, ModelCardinality, ModelOperation, ActionMethodReturnType, ButtonType, InputDataType, MultipleChoiceType},
    associations={packages0, modelassociations5, views7, maincomponents1, maincomponentrelations2, models4, renders16, htmlelements18, presentationelement20, controllers8, properties9, inherits12, tablekeys14, principal24, dependent27, actionmethods22, parameters30, usecase32, helperforsendingrequest34, actionmethod36, model39, layout33, properties42, actionmethod45, model47, modelproperties50, presentationelement55, usecase53, actionmethod57, returns59, actors70, usecasepackages71, abstractview62, model64, properties67, usecases80, helperforsendingrequest82, usecase73, actor75, helperforsendingrequest76, actionmethod78, presentationformelement84, choice85, helperforsendingrequest87, model89, header86, presentationformelementtoproperty92, presentationformelement94, property97, tablekey100},
    generalizations={gen_ryz_Package_NamedElement, gen_ryz_ComponentPackage_Package, gen_ryz_MvcPackage_Package, gen_ryz_Project_NamedElement, gen_ryz_ViewPackage_ComponentPackage, gen_ryz_ControllerPackage_ComponentPackage, gen_ryz_ModelPackage_ComponentPackage, gen_ryz_Model_MainComponent, gen_ryz_AbstractView_MainComponent, gen_ryz_ModelAssociation_NamedElement, gen_ryz_Controller_MainComponent, gen_ryz_MainComponent_NamedElement, gen_ryz_Property_NamedElement, gen_ryz_Layout_AbstractView, gen_ryz_View_AbstractView, gen_ryz_Partial_AbstractView, gen_ryz_ActionMethod_NamedElement, gen_ryz_Parameter_NamedElement, gen_ryz_MainComponentRelation_NamedElement, gen_ryz_ViewToControllerRelation_MainComponentRelation, gen_ryz_ActionLink_HelperForSendingRequest, gen_ryz_Form_HelperForSendingRequest, gen_ryz_ControllerToModelRelation_MainComponentRelation, gen_ryz_TableKey_NamedElement, gen_ryz_ControllerToViewRelation_MainComponentRelation, gen_ryz_UseCaseActorPackage_Package, gen_ryz_ViewToModelRelation_MainComponentRelation, gen_ryz_UseCasePackage_NamedElement, gen_ryz_PresentationElement_NamedElement, gen_ryz_Actor_NamedElement, gen_ryz_UseCase_NamedElement, gen_ryz_PresentationForm_PresentationElement, gen_ryz_MultipleChoice_PresentationFormElement, gen_ryz_Button_PresentationFormElement, gen_ryz_Input_PresentationFormElement, gen_ryz_FormElementToPropertyKeyRelation_MainComponentRelation, gen_ryz_Link_PresentationElement, gen_ryz_Table_PresentationElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)