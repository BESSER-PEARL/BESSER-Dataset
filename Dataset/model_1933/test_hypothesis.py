import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MenuExtensionRef,
    ChildrenHolder,
    SourcesPointer,
    domain::DataControl,
    Uielement,
    domain::SourcesPointer,
    domain::Formatable,
    domain::ItemIcon,
    domain::AreaRef,
    MenuHolder,
    EnabledUIItem,
    domain::EnabledUIItem,
    Context,
    domain::FlexFields,
    domain::NickNamed,
    InputElement,
    domain::OptionSelection,
    domain::StyleElement,
    ContextParameters,
    ContextValue,
    domain::StyleClass,
    domain::ContextParameters,
    domain::ExpressionPart,
    domain::ContextValue,
    domain::ContextParameter,
    domain::ChildrenHolder,
    domain::InputElement,
    domain::LinkToMessage,
    domain::LinkToLabel,
    domain::Controls,
    Trigger,
    domain::CanvasView,
    domain::ViewPortTrigger,
    ViewElement,
    Orderable,
    domain::ViewPort,
    domain::ViewArea,
    domain::MenuView,
    FlexFields,
    MultiLangLabel,
    domain::Label,
    domain::MessageElement,
    DefaultCavas,
    ViewPortHolder,
    CanvasFrame,
    NickNamed,
    domain::DefaultCavas,
    StyleElement,
    domain::Selection,
    domain::Context,
    domain::MultiLangLabel,
    domain::Orderable,
    domain::TabPagesInheritance,
    domain::ViewInheritance,
    domain::CanvasFrame,
    domain::Views,
    domain::FormDataControls,
    domain::FormView,
    domain::Form,
    domain::EnumAttribute,
    Secured,
    TypeElement,
    domain::Enumarator,
    domain::Primitive,
    domain::Link,
    RelationShip,
    domain::Generalization,
    domain::Assosiation,
    domain::References,
    domain::TypeElement,
    domain::Package,
    domain::TypePointer,
    domain::ArtifactRef,
    domain::QueryVariable,
    domain::KeyValuePair,
    domain::TypeDefinition,
    domain::Query,
    domain::MappingSpecifier,
    ArtifactRef,
    domain::HashProperty,
    domain::Property,
    Component,
    domain::JavaComponent,
    UsingMappers,
    domain::ModelMapper,
    domain::DeploymentStarStep,
    domain::DeploymentComponent,
    domain::DeploymentComponents,
    domain::ConfigExtension,
    domain::DeploymentSequence,
    domain::Infrastructure,
    domain::Configuration,
    domain::Recipe,
    domain::UsingMappers,
    TypeMapper,
    domain::JavaScriptMapper,
    domain::JavaMapper,
    Mapper,
    domain::CSSMapper,
    domain::RoleMapper,
    domain::Mapper,
    domain::StyleLibrary,
    domain::Group,
    domain::StyleSet,
    domain::Translation,
    domain::Message,
    domain::LanguageRef,
    Categorized,
    domain::RelationShip,
    domain::PopupCanvas,
    domain::Type,
    domain::Window,
    domain::Canvas,
    domain::MenuDefinition,
    domain::ViewElement,
    domain::FlexField,
    domain::Uielement,
    domain::TabPage,
    domain::TabCanvas,
    domain::Language,
    domain::MessageLibrary,
    domain::Operation,
    TypePointer,
    domain::FormParameter,
    domain::TypeReference,
    domain::Attribute,
    domain::TypeMapper,
    domain::ReturnValue,
    domain::Parameter,
    domain::MethodPointer,
    domain::Mappers,
    domain::ApplicationMapper,
    domain::Recipes,
    domain::ApplicationRecipe,
    domain::UIPackage,
    domain::ApplicationUIPackage,
    domain::Styles,
    domain::Roles,
    domain::Messages,
    domain::ApplicationMessages,
    domain::ApplicationRole,
    domain::ApplicationInfrastructureLayer,
    domain::StylesPackage,
    domain::Option,
    domain::QueryParameter,
    domain::Specifier,
    domain::ModelQuery,
    domain::ConfigHash,
    domain::ConfigVariable,
    domain::Artifact,
    DomainArtifact,
    domain::JPAService,
    domain::EJBService,
    domain::ContinuousIintegration,
    domain::ORMEntity,
    domain::Artifacts,
    domain::Application,
    domain::DomainArtifact,
    HTMLLayerHolder,
    domain::ApplicationStyle,
    domain::Types,
    domain::Ingredient,
    domain::ApplicationMappers,
    domain::Component,
    domain::ApplicationRecipes,
    domain::ViewPortHolder,
    domain::LayerHolder,
    domain::ApplicationUILayer,
    domain::Role,
    domain::DomainApplication,
    domain::GrantAccess,
    domain::Secured,
    domain::GenerationHint,
    domain::Classifier,
    domain::Categorized,
    domain::HTMLLayerHolder,
    domain::EObject,
    domain::DomainApplications,
    domain::DomainTypes,
    domain::DomainArtifacts,
    domain::Domain,
    domain::TypesRepository,
    MenuElement,
    domain::MenuSeparator,
    domain::MenuExtensionPoint,
    domain::MenuElement,
    domain::MenuExtensionRef,
    domain::MenuHolder,
    domain::InfrastructureComponent,
    domain::InfrastructureLayer,
    domain::Subsystem,
    InfrastructureComponent,
    domain::Hub,
    domain::ServerClaster,
    domain::Router,
    domain::Storage,
    domain::Server,
    domain::EnterpriseInfrastructure,
    domain::InfrastructureConnection,
    domain::Datacenter,
    domain::OrderBy,
    domain::Orders,
    domain::ArtificialField,
    domain::FormVariable,
    ProxiesList,
    domain::SearchTrigger,
    domain::DeleteTrigger,
    domain::InsertTrigger,
    domain::CreateTrigger,
    domain::ProxiesList,
    domain::PREUpdateTrigger,
    domain::POSTCreateTrigger,
    domain::PREDeleteTrigger,
    domain::PREInsertTrigger,
    domain::POSTQueryTrigger,
    domain::PREQueryTrigger,
    domain::PREFormTrigger,
    MethodPointer,
    domain::Trigger,
    domain::Dependency,
    domain::UpdateTrigger,
    domain::Root,
    domain::Tree,
    domain::Menu,
    domain::Table,
    domain::Column,
    ItemIcon,
    domain::MenuItem,
    domain::SubMenu,
    domain::Button,
    domain::MenuFolder,
    domain::Relation,
    domain::Image,
    OptionSelection,
    domain::DropDownSelection,
    domain::CheckBox,
    Formatable,
    domain::Date,
    domain::InputText,
    domain::Password,
    domain::OutputText,
    Orientation,
    PlatformLayers,
    Comparator,
    RelationType,
    Order,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_menuextensionref_is_not_abstract():
    assert not inspect.isabstract(MenuExtensionRef)


def test_menuextensionref_constructor_exists():
    assert callable(MenuExtensionRef.__init__)


def test_menuextensionref_constructor_args():
    sig = inspect.signature(MenuExtensionRef.__init__)
    params = list(sig.parameters.keys())



def test_childrenholder_is_not_abstract():
    assert not inspect.isabstract(ChildrenHolder)


def test_childrenholder_constructor_exists():
    assert callable(ChildrenHolder.__init__)


def test_childrenholder_constructor_args():
    sig = inspect.signature(ChildrenHolder.__init__)
    params = list(sig.parameters.keys())



def test_sourcespointer_is_not_abstract():
    assert not inspect.isabstract(SourcesPointer)


def test_sourcespointer_constructor_exists():
    assert callable(SourcesPointer.__init__)


def test_sourcespointer_constructor_args():
    sig = inspect.signature(SourcesPointer.__init__)
    params = list(sig.parameters.keys())



def test_domain::datacontrol_is_not_abstract():
    assert not inspect.isabstract(domain::DataControl)


def test_domain::datacontrol_constructor_exists():
    assert callable(domain::DataControl.__init__)


def test_domain::datacontrol_constructor_args():
    sig = inspect.signature(domain::DataControl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::datacontrol_has_name():
    assert hasattr(domain::DataControl, "name")
    descriptor = None
    for klass in domain::DataControl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::datacontrol_has_uid():
    assert hasattr(domain::DataControl, "uid")
    descriptor = None
    for klass in domain::DataControl.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_uielement_is_not_abstract():
    assert not inspect.isabstract(Uielement)


def test_uielement_constructor_exists():
    assert callable(Uielement.__init__)


def test_uielement_constructor_args():
    sig = inspect.signature(Uielement.__init__)
    params = list(sig.parameters.keys())



def test_domain::sourcespointer_is_not_abstract():
    assert not inspect.isabstract(domain::SourcesPointer)


def test_domain::sourcespointer_constructor_exists():
    assert callable(domain::SourcesPointer.__init__)


def test_domain::sourcespointer_constructor_args():
    sig = inspect.signature(domain::SourcesPointer.__init__)
    params = list(sig.parameters.keys())



def test_domain::formatable_is_not_abstract():
    assert not inspect.isabstract(domain::Formatable)


def test_domain::formatable_constructor_exists():
    assert callable(domain::Formatable.__init__)


def test_domain::formatable_constructor_args():
    sig = inspect.signature(domain::Formatable.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_domain::formatable_has_format():
    assert hasattr(domain::Formatable, "format")
    descriptor = None
    for klass in domain::Formatable.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_domain::itemicon_is_not_abstract():
    assert not inspect.isabstract(domain::ItemIcon)


def test_domain::itemicon_constructor_exists():
    assert callable(domain::ItemIcon.__init__)


def test_domain::itemicon_constructor_args():
    sig = inspect.signature(domain::ItemIcon.__init__)
    params = list(sig.parameters.keys())



def test_domain::arearef_is_not_abstract():
    assert not inspect.isabstract(domain::AreaRef)


def test_domain::arearef_constructor_exists():
    assert callable(domain::AreaRef.__init__)


def test_domain::arearef_constructor_args():
    sig = inspect.signature(domain::AreaRef.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_domain::arearef_has_group():
    assert hasattr(domain::AreaRef, "group")
    descriptor = None
    for klass in domain::AreaRef.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_menuholder_is_not_abstract():
    assert not inspect.isabstract(MenuHolder)


def test_menuholder_constructor_exists():
    assert callable(MenuHolder.__init__)


def test_menuholder_constructor_args():
    sig = inspect.signature(MenuHolder.__init__)
    params = list(sig.parameters.keys())



def test_enableduiitem_is_not_abstract():
    assert not inspect.isabstract(EnabledUIItem)


def test_enableduiitem_constructor_exists():
    assert callable(EnabledUIItem.__init__)


def test_enableduiitem_constructor_args():
    sig = inspect.signature(EnabledUIItem.__init__)
    params = list(sig.parameters.keys())



def test_domain::enableduiitem_is_not_abstract():
    assert not inspect.isabstract(domain::EnabledUIItem)


def test_domain::enableduiitem_constructor_exists():
    assert callable(domain::EnabledUIItem.__init__)


def test_domain::enableduiitem_constructor_args():
    sig = inspect.signature(domain::EnabledUIItem.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_domain::flexfields_is_not_abstract():
    assert not inspect.isabstract(domain::FlexFields)


def test_domain::flexfields_constructor_exists():
    assert callable(domain::FlexFields.__init__)


def test_domain::flexfields_constructor_args():
    sig = inspect.signature(domain::FlexFields.__init__)
    params = list(sig.parameters.keys())



def test_domain::nicknamed_is_not_abstract():
    assert not inspect.isabstract(domain::NickNamed)


def test_domain::nicknamed_constructor_exists():
    assert callable(domain::NickNamed.__init__)


def test_domain::nicknamed_constructor_args():
    sig = inspect.signature(domain::NickNamed.__init__)
    params = list(sig.parameters.keys())
    assert "nickname" in params, "Missing parameter 'nickname'"

def test_domain::nicknamed_has_nickname():
    assert hasattr(domain::NickNamed, "nickname")
    descriptor = None
    for klass in domain::NickNamed.__mro__:
        if "nickname" in klass.__dict__:
            descriptor = klass.__dict__["nickname"]
            break
    assert isinstance(descriptor, property)



def test_inputelement_is_not_abstract():
    assert not inspect.isabstract(InputElement)


def test_inputelement_constructor_exists():
    assert callable(InputElement.__init__)


def test_inputelement_constructor_args():
    sig = inspect.signature(InputElement.__init__)
    params = list(sig.parameters.keys())



def test_domain::optionselection_is_not_abstract():
    assert not inspect.isabstract(domain::OptionSelection)


def test_domain::optionselection_constructor_exists():
    assert callable(domain::OptionSelection.__init__)


def test_domain::optionselection_constructor_args():
    sig = inspect.signature(domain::OptionSelection.__init__)
    params = list(sig.parameters.keys())



def test_domain::styleelement_is_not_abstract():
    assert not inspect.isabstract(domain::StyleElement)


def test_domain::styleelement_constructor_exists():
    assert callable(domain::StyleElement.__init__)


def test_domain::styleelement_constructor_args():
    sig = inspect.signature(domain::StyleElement.__init__)
    params = list(sig.parameters.keys())



def test_contextparameters_is_not_abstract():
    assert not inspect.isabstract(ContextParameters)


def test_contextparameters_constructor_exists():
    assert callable(ContextParameters.__init__)


def test_contextparameters_constructor_args():
    sig = inspect.signature(ContextParameters.__init__)
    params = list(sig.parameters.keys())



def test_contextvalue_is_not_abstract():
    assert not inspect.isabstract(ContextValue)


def test_contextvalue_constructor_exists():
    assert callable(ContextValue.__init__)


def test_contextvalue_constructor_args():
    sig = inspect.signature(ContextValue.__init__)
    params = list(sig.parameters.keys())



def test_domain::styleclass_is_not_abstract():
    assert not inspect.isabstract(domain::StyleClass)


def test_domain::styleclass_constructor_exists():
    assert callable(domain::StyleClass.__init__)


def test_domain::styleclass_constructor_args():
    sig = inspect.signature(domain::StyleClass.__init__)
    params = list(sig.parameters.keys())



def test_domain::contextparameters_is_not_abstract():
    assert not inspect.isabstract(domain::ContextParameters)


def test_domain::contextparameters_constructor_exists():
    assert callable(domain::ContextParameters.__init__)


def test_domain::contextparameters_constructor_args():
    sig = inspect.signature(domain::ContextParameters.__init__)
    params = list(sig.parameters.keys())



def test_domain::expressionpart_is_not_abstract():
    assert not inspect.isabstract(domain::ExpressionPart)


def test_domain::expressionpart_constructor_exists():
    assert callable(domain::ExpressionPart.__init__)


def test_domain::expressionpart_constructor_args():
    sig = inspect.signature(domain::ExpressionPart.__init__)
    params = list(sig.parameters.keys())
    assert "expressionType" in params, "Missing parameter 'expressionType'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "order" in params, "Missing parameter 'order'"

def test_domain::expressionpart_has_expressionType():
    assert hasattr(domain::ExpressionPart, "expressionType")
    descriptor = None
    for klass in domain::ExpressionPart.__mro__:
        if "expressionType" in klass.__dict__:
            descriptor = klass.__dict__["expressionType"]
            break
    assert isinstance(descriptor, property)

def test_domain::expressionpart_has_uid():
    assert hasattr(domain::ExpressionPart, "uid")
    descriptor = None
    for klass in domain::ExpressionPart.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::expressionpart_has_order():
    assert hasattr(domain::ExpressionPart, "order")
    descriptor = None
    for klass in domain::ExpressionPart.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_domain::contextvalue_is_not_abstract():
    assert not inspect.isabstract(domain::ContextValue)


def test_domain::contextvalue_constructor_exists():
    assert callable(domain::ContextValue.__init__)


def test_domain::contextvalue_constructor_args():
    sig = inspect.signature(domain::ContextValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_domain::contextvalue_has_value():
    assert hasattr(domain::ContextValue, "value")
    descriptor = None
    for klass in domain::ContextValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domain::contextvalue_has_uid():
    assert hasattr(domain::ContextValue, "uid")
    descriptor = None
    for klass in domain::ContextValue.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::contextvalue_has_constant():
    assert hasattr(domain::ContextValue, "constant")
    descriptor = None
    for klass in domain::ContextValue.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_domain::contextparameter_is_not_abstract():
    assert not inspect.isabstract(domain::ContextParameter)


def test_domain::contextparameter_constructor_exists():
    assert callable(domain::ContextParameter.__init__)


def test_domain::contextparameter_constructor_args():
    sig = inspect.signature(domain::ContextParameter.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::contextparameter_has_operation():
    assert hasattr(domain::ContextParameter, "operation")
    descriptor = None
    for klass in domain::ContextParameter.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)

def test_domain::contextparameter_has_uid():
    assert hasattr(domain::ContextParameter, "uid")
    descriptor = None
    for klass in domain::ContextParameter.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::childrenholder_is_not_abstract():
    assert not inspect.isabstract(domain::ChildrenHolder)


def test_domain::childrenholder_constructor_exists():
    assert callable(domain::ChildrenHolder.__init__)


def test_domain::childrenholder_constructor_args():
    sig = inspect.signature(domain::ChildrenHolder.__init__)
    params = list(sig.parameters.keys())



def test_domain::inputelement_is_not_abstract():
    assert not inspect.isabstract(domain::InputElement)


def test_domain::inputelement_constructor_exists():
    assert callable(domain::InputElement.__init__)


def test_domain::inputelement_constructor_args():
    sig = inspect.signature(domain::InputElement.__init__)
    params = list(sig.parameters.keys())



def test_domain::linktomessage_is_not_abstract():
    assert not inspect.isabstract(domain::LinkToMessage)


def test_domain::linktomessage_constructor_exists():
    assert callable(domain::LinkToMessage.__init__)


def test_domain::linktomessage_constructor_args():
    sig = inspect.signature(domain::LinkToMessage.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::linktomessage_has_uid():
    assert hasattr(domain::LinkToMessage, "uid")
    descriptor = None
    for klass in domain::LinkToMessage.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::linktolabel_is_not_abstract():
    assert not inspect.isabstract(domain::LinkToLabel)


def test_domain::linktolabel_constructor_exists():
    assert callable(domain::LinkToLabel.__init__)


def test_domain::linktolabel_constructor_args():
    sig = inspect.signature(domain::LinkToLabel.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::linktolabel_has_uid():
    assert hasattr(domain::LinkToLabel, "uid")
    descriptor = None
    for klass in domain::LinkToLabel.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::controls_is_not_abstract():
    assert not inspect.isabstract(domain::Controls)


def test_domain::controls_constructor_exists():
    assert callable(domain::Controls.__init__)


def test_domain::controls_constructor_args():
    sig = inspect.signature(domain::Controls.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::controls_has_uid():
    assert hasattr(domain::Controls, "uid")
    descriptor = None
    for klass in domain::Controls.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_domain::canvasview_is_not_abstract():
    assert not inspect.isabstract(domain::CanvasView)


def test_domain::canvasview_constructor_exists():
    assert callable(domain::CanvasView.__init__)


def test_domain::canvasview_constructor_args():
    sig = inspect.signature(domain::CanvasView.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::canvasview_has_uid():
    assert hasattr(domain::CanvasView, "uid")
    descriptor = None
    for klass in domain::CanvasView.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::viewporttrigger_is_not_abstract():
    assert not inspect.isabstract(domain::ViewPortTrigger)


def test_domain::viewporttrigger_constructor_exists():
    assert callable(domain::ViewPortTrigger.__init__)


def test_domain::viewporttrigger_constructor_args():
    sig = inspect.signature(domain::ViewPortTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::viewporttrigger_has_uid():
    assert hasattr(domain::ViewPortTrigger, "uid")
    descriptor = None
    for klass in domain::ViewPortTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_viewelement_is_not_abstract():
    assert not inspect.isabstract(ViewElement)


def test_viewelement_constructor_exists():
    assert callable(ViewElement.__init__)


def test_viewelement_constructor_args():
    sig = inspect.signature(ViewElement.__init__)
    params = list(sig.parameters.keys())



def test_orderable_is_not_abstract():
    assert not inspect.isabstract(Orderable)


def test_orderable_constructor_exists():
    assert callable(Orderable.__init__)


def test_orderable_constructor_args():
    sig = inspect.signature(Orderable.__init__)
    params = list(sig.parameters.keys())



def test_domain::viewport_is_not_abstract():
    assert not inspect.isabstract(domain::ViewPort)


def test_domain::viewport_constructor_exists():
    assert callable(domain::ViewPort.__init__)


def test_domain::viewport_constructor_args():
    sig = inspect.signature(domain::ViewPort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::viewport_has_name():
    assert hasattr(domain::ViewPort, "name")
    descriptor = None
    for klass in domain::ViewPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::viewport_has_uid():
    assert hasattr(domain::ViewPort, "uid")
    descriptor = None
    for klass in domain::ViewPort.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::viewarea_is_not_abstract():
    assert not inspect.isabstract(domain::ViewArea)


def test_domain::viewarea_constructor_exists():
    assert callable(domain::ViewArea.__init__)


def test_domain::viewarea_constructor_args():
    sig = inspect.signature(domain::ViewArea.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::viewarea_has_name():
    assert hasattr(domain::ViewArea, "name")
    descriptor = None
    for klass in domain::ViewArea.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::viewarea_has_uid():
    assert hasattr(domain::ViewArea, "uid")
    descriptor = None
    for klass in domain::ViewArea.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::menuview_is_not_abstract():
    assert not inspect.isabstract(domain::MenuView)


def test_domain::menuview_constructor_exists():
    assert callable(domain::MenuView.__init__)


def test_domain::menuview_constructor_args():
    sig = inspect.signature(domain::MenuView.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::menuview_has_uid():
    assert hasattr(domain::MenuView, "uid")
    descriptor = None
    for klass in domain::MenuView.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_flexfields_is_not_abstract():
    assert not inspect.isabstract(FlexFields)


def test_flexfields_constructor_exists():
    assert callable(FlexFields.__init__)


def test_flexfields_constructor_args():
    sig = inspect.signature(FlexFields.__init__)
    params = list(sig.parameters.keys())



def test_multilanglabel_is_not_abstract():
    assert not inspect.isabstract(MultiLangLabel)


def test_multilanglabel_constructor_exists():
    assert callable(MultiLangLabel.__init__)


def test_multilanglabel_constructor_args():
    sig = inspect.signature(MultiLangLabel.__init__)
    params = list(sig.parameters.keys())



def test_domain::label_is_not_abstract():
    assert not inspect.isabstract(domain::Label)


def test_domain::label_constructor_exists():
    assert callable(domain::Label.__init__)


def test_domain::label_constructor_args():
    sig = inspect.signature(domain::Label.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_domain::label_has_label():
    assert hasattr(domain::Label, "label")
    descriptor = None
    for klass in domain::Label.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_domain::messageelement_is_not_abstract():
    assert not inspect.isabstract(domain::MessageElement)


def test_domain::messageelement_constructor_exists():
    assert callable(domain::MessageElement.__init__)


def test_domain::messageelement_constructor_args():
    sig = inspect.signature(domain::MessageElement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_domain::messageelement_has_label():
    assert hasattr(domain::MessageElement, "label")
    descriptor = None
    for klass in domain::MessageElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_defaultcavas_is_not_abstract():
    assert not inspect.isabstract(DefaultCavas)


def test_defaultcavas_constructor_exists():
    assert callable(DefaultCavas.__init__)


def test_defaultcavas_constructor_args():
    sig = inspect.signature(DefaultCavas.__init__)
    params = list(sig.parameters.keys())



def test_viewportholder_is_not_abstract():
    assert not inspect.isabstract(ViewPortHolder)


def test_viewportholder_constructor_exists():
    assert callable(ViewPortHolder.__init__)


def test_viewportholder_constructor_args():
    sig = inspect.signature(ViewPortHolder.__init__)
    params = list(sig.parameters.keys())



def test_canvasframe_is_not_abstract():
    assert not inspect.isabstract(CanvasFrame)


def test_canvasframe_constructor_exists():
    assert callable(CanvasFrame.__init__)


def test_canvasframe_constructor_args():
    sig = inspect.signature(CanvasFrame.__init__)
    params = list(sig.parameters.keys())



def test_nicknamed_is_not_abstract():
    assert not inspect.isabstract(NickNamed)


def test_nicknamed_constructor_exists():
    assert callable(NickNamed.__init__)


def test_nicknamed_constructor_args():
    sig = inspect.signature(NickNamed.__init__)
    params = list(sig.parameters.keys())



def test_domain::defaultcavas_is_not_abstract():
    assert not inspect.isabstract(domain::DefaultCavas)


def test_domain::defaultcavas_constructor_exists():
    assert callable(domain::DefaultCavas.__init__)


def test_domain::defaultcavas_constructor_args():
    sig = inspect.signature(domain::DefaultCavas.__init__)
    params = list(sig.parameters.keys())
    assert "defaultCanvas" in params, "Missing parameter 'defaultCanvas'"

def test_domain::defaultcavas_has_defaultCanvas():
    assert hasattr(domain::DefaultCavas, "defaultCanvas")
    descriptor = None
    for klass in domain::DefaultCavas.__mro__:
        if "defaultCanvas" in klass.__dict__:
            descriptor = klass.__dict__["defaultCanvas"]
            break
    assert isinstance(descriptor, property)



def test_styleelement_is_not_abstract():
    assert not inspect.isabstract(StyleElement)


def test_styleelement_constructor_exists():
    assert callable(StyleElement.__init__)


def test_styleelement_constructor_args():
    sig = inspect.signature(StyleElement.__init__)
    params = list(sig.parameters.keys())



def test_domain::selection_is_not_abstract():
    assert not inspect.isabstract(domain::Selection)


def test_domain::selection_constructor_exists():
    assert callable(domain::Selection.__init__)


def test_domain::selection_constructor_args():
    sig = inspect.signature(domain::Selection.__init__)
    params = list(sig.parameters.keys())



def test_domain::context_is_not_abstract():
    assert not inspect.isabstract(domain::Context)


def test_domain::context_constructor_exists():
    assert callable(domain::Context.__init__)


def test_domain::context_constructor_args():
    sig = inspect.signature(domain::Context.__init__)
    params = list(sig.parameters.keys())



def test_domain::multilanglabel_is_not_abstract():
    assert not inspect.isabstract(domain::MultiLangLabel)


def test_domain::multilanglabel_constructor_exists():
    assert callable(domain::MultiLangLabel.__init__)


def test_domain::multilanglabel_constructor_args():
    sig = inspect.signature(domain::MultiLangLabel.__init__)
    params = list(sig.parameters.keys())



def test_domain::orderable_is_not_abstract():
    assert not inspect.isabstract(domain::Orderable)


def test_domain::orderable_constructor_exists():
    assert callable(domain::Orderable.__init__)


def test_domain::orderable_constructor_args():
    sig = inspect.signature(domain::Orderable.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_domain::orderable_has_order():
    assert hasattr(domain::Orderable, "order")
    descriptor = None
    for klass in domain::Orderable.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_domain::tabpagesinheritance_is_not_abstract():
    assert not inspect.isabstract(domain::TabPagesInheritance)


def test_domain::tabpagesinheritance_constructor_exists():
    assert callable(domain::TabPagesInheritance.__init__)


def test_domain::tabpagesinheritance_constructor_args():
    sig = inspect.signature(domain::TabPagesInheritance.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::tabpagesinheritance_has_uid():
    assert hasattr(domain::TabPagesInheritance, "uid")
    descriptor = None
    for klass in domain::TabPagesInheritance.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::viewinheritance_is_not_abstract():
    assert not inspect.isabstract(domain::ViewInheritance)


def test_domain::viewinheritance_constructor_exists():
    assert callable(domain::ViewInheritance.__init__)


def test_domain::viewinheritance_constructor_args():
    sig = inspect.signature(domain::ViewInheritance.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::viewinheritance_has_uid():
    assert hasattr(domain::ViewInheritance, "uid")
    descriptor = None
    for klass in domain::ViewInheritance.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::canvasframe_is_not_abstract():
    assert not inspect.isabstract(domain::CanvasFrame)


def test_domain::canvasframe_constructor_exists():
    assert callable(domain::CanvasFrame.__init__)


def test_domain::canvasframe_constructor_args():
    sig = inspect.signature(domain::CanvasFrame.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::canvasframe_has_uid():
    assert hasattr(domain::CanvasFrame, "uid")
    descriptor = None
    for klass in domain::CanvasFrame.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::canvasframe_has_name():
    assert hasattr(domain::CanvasFrame, "name")
    descriptor = None
    for klass in domain::CanvasFrame.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::views_is_not_abstract():
    assert not inspect.isabstract(domain::Views)


def test_domain::views_constructor_exists():
    assert callable(domain::Views.__init__)


def test_domain::views_constructor_args():
    sig = inspect.signature(domain::Views.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::views_has_uid():
    assert hasattr(domain::Views, "uid")
    descriptor = None
    for klass in domain::Views.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::formdatacontrols_is_not_abstract():
    assert not inspect.isabstract(domain::FormDataControls)


def test_domain::formdatacontrols_constructor_exists():
    assert callable(domain::FormDataControls.__init__)


def test_domain::formdatacontrols_constructor_args():
    sig = inspect.signature(domain::FormDataControls.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::formdatacontrols_has_uid():
    assert hasattr(domain::FormDataControls, "uid")
    descriptor = None
    for klass in domain::FormDataControls.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::formdatacontrols_has_name():
    assert hasattr(domain::FormDataControls, "name")
    descriptor = None
    for klass in domain::FormDataControls.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::formview_is_not_abstract():
    assert not inspect.isabstract(domain::FormView)


def test_domain::formview_constructor_exists():
    assert callable(domain::FormView.__init__)


def test_domain::formview_constructor_args():
    sig = inspect.signature(domain::FormView.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::formview_has_name():
    assert hasattr(domain::FormView, "name")
    descriptor = None
    for klass in domain::FormView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::formview_has_uid():
    assert hasattr(domain::FormView, "uid")
    descriptor = None
    for klass in domain::FormView.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::form_is_not_abstract():
    assert not inspect.isabstract(domain::Form)


def test_domain::form_constructor_exists():
    assert callable(domain::Form.__init__)


def test_domain::form_constructor_args():
    sig = inspect.signature(domain::Form.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::form_has_name():
    assert hasattr(domain::Form, "name")
    descriptor = None
    for klass in domain::Form.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::form_has_uid():
    assert hasattr(domain::Form, "uid")
    descriptor = None
    for klass in domain::Form.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::enumattribute_is_not_abstract():
    assert not inspect.isabstract(domain::EnumAttribute)


def test_domain::enumattribute_constructor_exists():
    assert callable(domain::EnumAttribute.__init__)


def test_domain::enumattribute_constructor_args():
    sig = inspect.signature(domain::EnumAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::enumattribute_has_value():
    assert hasattr(domain::EnumAttribute, "value")
    descriptor = None
    for klass in domain::EnumAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domain::enumattribute_has_name():
    assert hasattr(domain::EnumAttribute, "name")
    descriptor = None
    for klass in domain::EnumAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::enumattribute_has_uid():
    assert hasattr(domain::EnumAttribute, "uid")
    descriptor = None
    for klass in domain::EnumAttribute.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_secured_is_not_abstract():
    assert not inspect.isabstract(Secured)


def test_secured_constructor_exists():
    assert callable(Secured.__init__)


def test_secured_constructor_args():
    sig = inspect.signature(Secured.__init__)
    params = list(sig.parameters.keys())



def test_typeelement_is_not_abstract():
    assert not inspect.isabstract(TypeElement)


def test_typeelement_constructor_exists():
    assert callable(TypeElement.__init__)


def test_typeelement_constructor_args():
    sig = inspect.signature(TypeElement.__init__)
    params = list(sig.parameters.keys())



def test_domain::enumarator_is_not_abstract():
    assert not inspect.isabstract(domain::Enumarator)


def test_domain::enumarator_constructor_exists():
    assert callable(domain::Enumarator.__init__)


def test_domain::enumarator_constructor_args():
    sig = inspect.signature(domain::Enumarator.__init__)
    params = list(sig.parameters.keys())



def test_domain::primitive_is_not_abstract():
    assert not inspect.isabstract(domain::Primitive)


def test_domain::primitive_constructor_exists():
    assert callable(domain::Primitive.__init__)


def test_domain::primitive_constructor_args():
    sig = inspect.signature(domain::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_domain::link_is_not_abstract():
    assert not inspect.isabstract(domain::Link)


def test_domain::link_constructor_exists():
    assert callable(domain::Link.__init__)


def test_domain::link_constructor_args():
    sig = inspect.signature(domain::Link.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::link_has_uid():
    assert hasattr(domain::Link, "uid")
    descriptor = None
    for klass in domain::Link.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(RelationShip)


def test_relationship_constructor_exists():
    assert callable(RelationShip.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(RelationShip.__init__)
    params = list(sig.parameters.keys())



def test_domain::generalization_is_not_abstract():
    assert not inspect.isabstract(domain::Generalization)


def test_domain::generalization_constructor_exists():
    assert callable(domain::Generalization.__init__)


def test_domain::generalization_constructor_args():
    sig = inspect.signature(domain::Generalization.__init__)
    params = list(sig.parameters.keys())



def test_domain::assosiation_is_not_abstract():
    assert not inspect.isabstract(domain::Assosiation)


def test_domain::assosiation_constructor_exists():
    assert callable(domain::Assosiation.__init__)


def test_domain::assosiation_constructor_args():
    sig = inspect.signature(domain::Assosiation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_domain::assosiation_has_type():
    assert hasattr(domain::Assosiation, "type")
    descriptor = None
    for klass in domain::Assosiation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_domain::references_is_not_abstract():
    assert not inspect.isabstract(domain::References)


def test_domain::references_constructor_exists():
    assert callable(domain::References.__init__)


def test_domain::references_constructor_args():
    sig = inspect.signature(domain::References.__init__)
    params = list(sig.parameters.keys())



def test_domain::typeelement_is_not_abstract():
    assert not inspect.isabstract(domain::TypeElement)


def test_domain::typeelement_constructor_exists():
    assert callable(domain::TypeElement.__init__)


def test_domain::typeelement_constructor_args():
    sig = inspect.signature(domain::TypeElement.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::typeelement_has_uid():
    assert hasattr(domain::TypeElement, "uid")
    descriptor = None
    for klass in domain::TypeElement.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::typeelement_has_name():
    assert hasattr(domain::TypeElement, "name")
    descriptor = None
    for klass in domain::TypeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::package_is_not_abstract():
    assert not inspect.isabstract(domain::Package)


def test_domain::package_constructor_exists():
    assert callable(domain::Package.__init__)


def test_domain::package_constructor_args():
    sig = inspect.signature(domain::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::package_has_name():
    assert hasattr(domain::Package, "name")
    descriptor = None
    for klass in domain::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::package_has_uid():
    assert hasattr(domain::Package, "uid")
    descriptor = None
    for klass in domain::Package.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::typepointer_is_not_abstract():
    assert not inspect.isabstract(domain::TypePointer)


def test_domain::typepointer_constructor_exists():
    assert callable(domain::TypePointer.__init__)


def test_domain::typepointer_constructor_args():
    sig = inspect.signature(domain::TypePointer.__init__)
    params = list(sig.parameters.keys())
    assert "fakeTypeName" in params, "Missing parameter 'fakeTypeName'"
    assert "fakePackageName" in params, "Missing parameter 'fakePackageName'"

def test_domain::typepointer_has_fakeTypeName():
    assert hasattr(domain::TypePointer, "fakeTypeName")
    descriptor = None
    for klass in domain::TypePointer.__mro__:
        if "fakeTypeName" in klass.__dict__:
            descriptor = klass.__dict__["fakeTypeName"]
            break
    assert isinstance(descriptor, property)

def test_domain::typepointer_has_fakePackageName():
    assert hasattr(domain::TypePointer, "fakePackageName")
    descriptor = None
    for klass in domain::TypePointer.__mro__:
        if "fakePackageName" in klass.__dict__:
            descriptor = klass.__dict__["fakePackageName"]
            break
    assert isinstance(descriptor, property)



def test_domain::artifactref_is_not_abstract():
    assert not inspect.isabstract(domain::ArtifactRef)


def test_domain::artifactref_constructor_exists():
    assert callable(domain::ArtifactRef.__init__)


def test_domain::artifactref_constructor_args():
    sig = inspect.signature(domain::ArtifactRef.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::artifactref_has_uid():
    assert hasattr(domain::ArtifactRef, "uid")
    descriptor = None
    for klass in domain::ArtifactRef.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::queryvariable_is_not_abstract():
    assert not inspect.isabstract(domain::QueryVariable)


def test_domain::queryvariable_constructor_exists():
    assert callable(domain::QueryVariable.__init__)


def test_domain::queryvariable_constructor_args():
    sig = inspect.signature(domain::QueryVariable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::queryvariable_has_value():
    assert hasattr(domain::QueryVariable, "value")
    descriptor = None
    for klass in domain::QueryVariable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domain::queryvariable_has_uid():
    assert hasattr(domain::QueryVariable, "uid")
    descriptor = None
    for klass in domain::QueryVariable.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::keyvaluepair_is_not_abstract():
    assert not inspect.isabstract(domain::KeyValuePair)


def test_domain::keyvaluepair_constructor_exists():
    assert callable(domain::KeyValuePair.__init__)


def test_domain::keyvaluepair_constructor_args():
    sig = inspect.signature(domain::KeyValuePair.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::keyvaluepair_has_key():
    assert hasattr(domain::KeyValuePair, "key")
    descriptor = None
    for klass in domain::KeyValuePair.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_domain::keyvaluepair_has_value():
    assert hasattr(domain::KeyValuePair, "value")
    descriptor = None
    for klass in domain::KeyValuePair.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_domain::keyvaluepair_has_uid():
    assert hasattr(domain::KeyValuePair, "uid")
    descriptor = None
    for klass in domain::KeyValuePair.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::typedefinition_is_not_abstract():
    assert not inspect.isabstract(domain::TypeDefinition)


def test_domain::typedefinition_constructor_exists():
    assert callable(domain::TypeDefinition.__init__)


def test_domain::typedefinition_constructor_args():
    sig = inspect.signature(domain::TypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::typedefinition_has_uid():
    assert hasattr(domain::TypeDefinition, "uid")
    descriptor = None
    for klass in domain::TypeDefinition.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::query_is_not_abstract():
    assert not inspect.isabstract(domain::Query)


def test_domain::query_constructor_exists():
    assert callable(domain::Query.__init__)


def test_domain::query_constructor_args():
    sig = inspect.signature(domain::Query.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::query_has_uid():
    assert hasattr(domain::Query, "uid")
    descriptor = None
    for klass in domain::Query.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::query_has_name():
    assert hasattr(domain::Query, "name")
    descriptor = None
    for klass in domain::Query.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::mappingspecifier_is_not_abstract():
    assert not inspect.isabstract(domain::MappingSpecifier)


def test_domain::mappingspecifier_constructor_exists():
    assert callable(domain::MappingSpecifier.__init__)


def test_domain::mappingspecifier_constructor_args():
    sig = inspect.signature(domain::MappingSpecifier.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::mappingspecifier_has_uid():
    assert hasattr(domain::MappingSpecifier, "uid")
    descriptor = None
    for klass in domain::MappingSpecifier.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_artifactref_is_not_abstract():
    assert not inspect.isabstract(ArtifactRef)


def test_artifactref_constructor_exists():
    assert callable(ArtifactRef.__init__)


def test_artifactref_constructor_args():
    sig = inspect.signature(ArtifactRef.__init__)
    params = list(sig.parameters.keys())



def test_domain::hashproperty_is_not_abstract():
    assert not inspect.isabstract(domain::HashProperty)


def test_domain::hashproperty_constructor_exists():
    assert callable(domain::HashProperty.__init__)


def test_domain::hashproperty_constructor_args():
    sig = inspect.signature(domain::HashProperty.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "fakeName" in params, "Missing parameter 'fakeName'"

def test_domain::hashproperty_has_uid():
    assert hasattr(domain::HashProperty, "uid")
    descriptor = None
    for klass in domain::HashProperty.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::hashproperty_has_fakeName():
    assert hasattr(domain::HashProperty, "fakeName")
    descriptor = None
    for klass in domain::HashProperty.__mro__:
        if "fakeName" in klass.__dict__:
            descriptor = klass.__dict__["fakeName"]
            break
    assert isinstance(descriptor, property)



def test_domain::property_is_not_abstract():
    assert not inspect.isabstract(domain::Property)


def test_domain::property_constructor_exists():
    assert callable(domain::Property.__init__)


def test_domain::property_constructor_args():
    sig = inspect.signature(domain::Property.__init__)
    params = list(sig.parameters.keys())
    assert "fakeName" in params, "Missing parameter 'fakeName'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "value" in params, "Missing parameter 'value'"

def test_domain::property_has_fakeName():
    assert hasattr(domain::Property, "fakeName")
    descriptor = None
    for klass in domain::Property.__mro__:
        if "fakeName" in klass.__dict__:
            descriptor = klass.__dict__["fakeName"]
            break
    assert isinstance(descriptor, property)

def test_domain::property_has_uid():
    assert hasattr(domain::Property, "uid")
    descriptor = None
    for klass in domain::Property.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::property_has_value():
    assert hasattr(domain::Property, "value")
    descriptor = None
    for klass in domain::Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_domain::javacomponent_is_not_abstract():
    assert not inspect.isabstract(domain::JavaComponent)


def test_domain::javacomponent_constructor_exists():
    assert callable(domain::JavaComponent.__init__)


def test_domain::javacomponent_constructor_args():
    sig = inspect.signature(domain::JavaComponent.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "artifactId" in params, "Missing parameter 'artifactId'"
    assert "basePackage" in params, "Missing parameter 'basePackage'"

def test_domain::javacomponent_has_version():
    assert hasattr(domain::JavaComponent, "version")
    descriptor = None
    for klass in domain::JavaComponent.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_domain::javacomponent_has_groupId():
    assert hasattr(domain::JavaComponent, "groupId")
    descriptor = None
    for klass in domain::JavaComponent.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_domain::javacomponent_has_artifactId():
    assert hasattr(domain::JavaComponent, "artifactId")
    descriptor = None
    for klass in domain::JavaComponent.__mro__:
        if "artifactId" in klass.__dict__:
            descriptor = klass.__dict__["artifactId"]
            break
    assert isinstance(descriptor, property)

def test_domain::javacomponent_has_basePackage():
    assert hasattr(domain::JavaComponent, "basePackage")
    descriptor = None
    for klass in domain::JavaComponent.__mro__:
        if "basePackage" in klass.__dict__:
            descriptor = klass.__dict__["basePackage"]
            break
    assert isinstance(descriptor, property)



def test_usingmappers_is_not_abstract():
    assert not inspect.isabstract(UsingMappers)


def test_usingmappers_constructor_exists():
    assert callable(UsingMappers.__init__)


def test_usingmappers_constructor_args():
    sig = inspect.signature(UsingMappers.__init__)
    params = list(sig.parameters.keys())



def test_domain::modelmapper_is_not_abstract():
    assert not inspect.isabstract(domain::ModelMapper)


def test_domain::modelmapper_constructor_exists():
    assert callable(domain::ModelMapper.__init__)


def test_domain::modelmapper_constructor_args():
    sig = inspect.signature(domain::ModelMapper.__init__)
    params = list(sig.parameters.keys())
    assert "artifactExecutionString" in params, "Missing parameter 'artifactExecutionString'"
    assert "name" in params, "Missing parameter 'name'"
    assert "artifactRoot" in params, "Missing parameter 'artifactRoot'"

def test_domain::modelmapper_has_artifactExecutionString():
    assert hasattr(domain::ModelMapper, "artifactExecutionString")
    descriptor = None
    for klass in domain::ModelMapper.__mro__:
        if "artifactExecutionString" in klass.__dict__:
            descriptor = klass.__dict__["artifactExecutionString"]
            break
    assert isinstance(descriptor, property)

def test_domain::modelmapper_has_name():
    assert hasattr(domain::ModelMapper, "name")
    descriptor = None
    for klass in domain::ModelMapper.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::modelmapper_has_artifactRoot():
    assert hasattr(domain::ModelMapper, "artifactRoot")
    descriptor = None
    for klass in domain::ModelMapper.__mro__:
        if "artifactRoot" in klass.__dict__:
            descriptor = klass.__dict__["artifactRoot"]
            break
    assert isinstance(descriptor, property)



def test_domain::deploymentstarstep_is_not_abstract():
    assert not inspect.isabstract(domain::DeploymentStarStep)


def test_domain::deploymentstarstep_constructor_exists():
    assert callable(domain::DeploymentStarStep.__init__)


def test_domain::deploymentstarstep_constructor_args():
    sig = inspect.signature(domain::DeploymentStarStep.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::deploymentstarstep_has_uid():
    assert hasattr(domain::DeploymentStarStep, "uid")
    descriptor = None
    for klass in domain::DeploymentStarStep.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::deploymentstarstep_has_name():
    assert hasattr(domain::DeploymentStarStep, "name")
    descriptor = None
    for klass in domain::DeploymentStarStep.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::deploymentcomponent_is_not_abstract():
    assert not inspect.isabstract(domain::DeploymentComponent)


def test_domain::deploymentcomponent_constructor_exists():
    assert callable(domain::DeploymentComponent.__init__)


def test_domain::deploymentcomponent_constructor_args():
    sig = inspect.signature(domain::DeploymentComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::deploymentcomponent_has_name():
    assert hasattr(domain::DeploymentComponent, "name")
    descriptor = None
    for klass in domain::DeploymentComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::deploymentcomponent_has_uid():
    assert hasattr(domain::DeploymentComponent, "uid")
    descriptor = None
    for klass in domain::DeploymentComponent.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::deploymentcomponents_is_not_abstract():
    assert not inspect.isabstract(domain::DeploymentComponents)


def test_domain::deploymentcomponents_constructor_exists():
    assert callable(domain::DeploymentComponents.__init__)


def test_domain::deploymentcomponents_constructor_args():
    sig = inspect.signature(domain::DeploymentComponents.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::deploymentcomponents_has_uid():
    assert hasattr(domain::DeploymentComponents, "uid")
    descriptor = None
    for klass in domain::DeploymentComponents.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::configextension_is_not_abstract():
    assert not inspect.isabstract(domain::ConfigExtension)


def test_domain::configextension_constructor_exists():
    assert callable(domain::ConfigExtension.__init__)


def test_domain::configextension_constructor_args():
    sig = inspect.signature(domain::ConfigExtension.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::configextension_has_uid():
    assert hasattr(domain::ConfigExtension, "uid")
    descriptor = None
    for klass in domain::ConfigExtension.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::deploymentsequence_is_not_abstract():
    assert not inspect.isabstract(domain::DeploymentSequence)


def test_domain::deploymentsequence_constructor_exists():
    assert callable(domain::DeploymentSequence.__init__)


def test_domain::deploymentsequence_constructor_args():
    sig = inspect.signature(domain::DeploymentSequence.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::deploymentsequence_has_name():
    assert hasattr(domain::DeploymentSequence, "name")
    descriptor = None
    for klass in domain::DeploymentSequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::deploymentsequence_has_uid():
    assert hasattr(domain::DeploymentSequence, "uid")
    descriptor = None
    for klass in domain::DeploymentSequence.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::infrastructure_is_not_abstract():
    assert not inspect.isabstract(domain::Infrastructure)


def test_domain::infrastructure_constructor_exists():
    assert callable(domain::Infrastructure.__init__)


def test_domain::infrastructure_constructor_args():
    sig = inspect.signature(domain::Infrastructure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::infrastructure_has_name():
    assert hasattr(domain::Infrastructure, "name")
    descriptor = None
    for klass in domain::Infrastructure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::infrastructure_has_uid():
    assert hasattr(domain::Infrastructure, "uid")
    descriptor = None
    for klass in domain::Infrastructure.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::configuration_is_not_abstract():
    assert not inspect.isabstract(domain::Configuration)


def test_domain::configuration_constructor_exists():
    assert callable(domain::Configuration.__init__)


def test_domain::configuration_constructor_args():
    sig = inspect.signature(domain::Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::configuration_has_name():
    assert hasattr(domain::Configuration, "name")
    descriptor = None
    for klass in domain::Configuration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::configuration_has_uid():
    assert hasattr(domain::Configuration, "uid")
    descriptor = None
    for klass in domain::Configuration.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::recipe_is_not_abstract():
    assert not inspect.isabstract(domain::Recipe)


def test_domain::recipe_constructor_exists():
    assert callable(domain::Recipe.__init__)


def test_domain::recipe_constructor_args():
    sig = inspect.signature(domain::Recipe.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::recipe_has_name():
    assert hasattr(domain::Recipe, "name")
    descriptor = None
    for klass in domain::Recipe.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::recipe_has_uid():
    assert hasattr(domain::Recipe, "uid")
    descriptor = None
    for klass in domain::Recipe.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::usingmappers_is_not_abstract():
    assert not inspect.isabstract(domain::UsingMappers)


def test_domain::usingmappers_constructor_exists():
    assert callable(domain::UsingMappers.__init__)


def test_domain::usingmappers_constructor_args():
    sig = inspect.signature(domain::UsingMappers.__init__)
    params = list(sig.parameters.keys())



def test_typemapper_is_not_abstract():
    assert not inspect.isabstract(TypeMapper)


def test_typemapper_constructor_exists():
    assert callable(TypeMapper.__init__)


def test_typemapper_constructor_args():
    sig = inspect.signature(TypeMapper.__init__)
    params = list(sig.parameters.keys())



def test_domain::javascriptmapper_is_not_abstract():
    assert not inspect.isabstract(domain::JavaScriptMapper)


def test_domain::javascriptmapper_constructor_exists():
    assert callable(domain::JavaScriptMapper.__init__)


def test_domain::javascriptmapper_constructor_args():
    sig = inspect.signature(domain::JavaScriptMapper.__init__)
    params = list(sig.parameters.keys())
    assert "libraryUrl" in params, "Missing parameter 'libraryUrl'"

def test_domain::javascriptmapper_has_libraryUrl():
    assert hasattr(domain::JavaScriptMapper, "libraryUrl")
    descriptor = None
    for klass in domain::JavaScriptMapper.__mro__:
        if "libraryUrl" in klass.__dict__:
            descriptor = klass.__dict__["libraryUrl"]
            break
    assert isinstance(descriptor, property)



def test_domain::javamapper_is_not_abstract():
    assert not inspect.isabstract(domain::JavaMapper)


def test_domain::javamapper_constructor_exists():
    assert callable(domain::JavaMapper.__init__)


def test_domain::javamapper_constructor_args():
    sig = inspect.signature(domain::JavaMapper.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "artifactType" in params, "Missing parameter 'artifactType'"
    assert "mappedToPackageName" in params, "Missing parameter 'mappedToPackageName'"
    assert "libraryName" in params, "Missing parameter 'libraryName'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "artifactId" in params, "Missing parameter 'artifactId'"
    assert "mappedToClassName" in params, "Missing parameter 'mappedToClassName'"

def test_domain::javamapper_has_version():
    assert hasattr(domain::JavaMapper, "version")
    descriptor = None
    for klass in domain::JavaMapper.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_domain::javamapper_has_artifactType():
    assert hasattr(domain::JavaMapper, "artifactType")
    descriptor = None
    for klass in domain::JavaMapper.__mro__:
        if "artifactType" in klass.__dict__:
            descriptor = klass.__dict__["artifactType"]
            break
    assert isinstance(descriptor, property)

def test_domain::javamapper_has_mappedToPackageName():
    assert hasattr(domain::JavaMapper, "mappedToPackageName")
    descriptor = None
    for klass in domain::JavaMapper.__mro__:
        if "mappedToPackageName" in klass.__dict__:
            descriptor = klass.__dict__["mappedToPackageName"]
            break
    assert isinstance(descriptor, property)

def test_domain::javamapper_has_libraryName():
    assert hasattr(domain::JavaMapper, "libraryName")
    descriptor = None
    for klass in domain::JavaMapper.__mro__:
        if "libraryName" in klass.__dict__:
            descriptor = klass.__dict__["libraryName"]
            break
    assert isinstance(descriptor, property)

def test_domain::javamapper_has_groupId():
    assert hasattr(domain::JavaMapper, "groupId")
    descriptor = None
    for klass in domain::JavaMapper.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_domain::javamapper_has_artifactId():
    assert hasattr(domain::JavaMapper, "artifactId")
    descriptor = None
    for klass in domain::JavaMapper.__mro__:
        if "artifactId" in klass.__dict__:
            descriptor = klass.__dict__["artifactId"]
            break
    assert isinstance(descriptor, property)

def test_domain::javamapper_has_mappedToClassName():
    assert hasattr(domain::JavaMapper, "mappedToClassName")
    descriptor = None
    for klass in domain::JavaMapper.__mro__:
        if "mappedToClassName" in klass.__dict__:
            descriptor = klass.__dict__["mappedToClassName"]
            break
    assert isinstance(descriptor, property)



def test_mapper_is_not_abstract():
    assert not inspect.isabstract(Mapper)


def test_mapper_constructor_exists():
    assert callable(Mapper.__init__)


def test_mapper_constructor_args():
    sig = inspect.signature(Mapper.__init__)
    params = list(sig.parameters.keys())



def test_domain::cssmapper_is_not_abstract():
    assert not inspect.isabstract(domain::CSSMapper)


def test_domain::cssmapper_constructor_exists():
    assert callable(domain::CSSMapper.__init__)


def test_domain::cssmapper_constructor_args():
    sig = inspect.signature(domain::CSSMapper.__init__)
    params = list(sig.parameters.keys())
    assert "fakePackageName" in params, "Missing parameter 'fakePackageName'"
    assert "fakeTypeName" in params, "Missing parameter 'fakeTypeName'"
    assert "libraryUrl" in params, "Missing parameter 'libraryUrl'"

def test_domain::cssmapper_has_fakePackageName():
    assert hasattr(domain::CSSMapper, "fakePackageName")
    descriptor = None
    for klass in domain::CSSMapper.__mro__:
        if "fakePackageName" in klass.__dict__:
            descriptor = klass.__dict__["fakePackageName"]
            break
    assert isinstance(descriptor, property)

def test_domain::cssmapper_has_fakeTypeName():
    assert hasattr(domain::CSSMapper, "fakeTypeName")
    descriptor = None
    for klass in domain::CSSMapper.__mro__:
        if "fakeTypeName" in klass.__dict__:
            descriptor = klass.__dict__["fakeTypeName"]
            break
    assert isinstance(descriptor, property)

def test_domain::cssmapper_has_libraryUrl():
    assert hasattr(domain::CSSMapper, "libraryUrl")
    descriptor = None
    for klass in domain::CSSMapper.__mro__:
        if "libraryUrl" in klass.__dict__:
            descriptor = klass.__dict__["libraryUrl"]
            break
    assert isinstance(descriptor, property)



def test_domain::rolemapper_is_not_abstract():
    assert not inspect.isabstract(domain::RoleMapper)


def test_domain::rolemapper_constructor_exists():
    assert callable(domain::RoleMapper.__init__)


def test_domain::rolemapper_constructor_args():
    sig = inspect.signature(domain::RoleMapper.__init__)
    params = list(sig.parameters.keys())
    assert "localRoleName" in params, "Missing parameter 'localRoleName'"
    assert "globalRoleName" in params, "Missing parameter 'globalRoleName'"
    assert "fakeRoleName" in params, "Missing parameter 'fakeRoleName'"

def test_domain::rolemapper_has_localRoleName():
    assert hasattr(domain::RoleMapper, "localRoleName")
    descriptor = None
    for klass in domain::RoleMapper.__mro__:
        if "localRoleName" in klass.__dict__:
            descriptor = klass.__dict__["localRoleName"]
            break
    assert isinstance(descriptor, property)

def test_domain::rolemapper_has_globalRoleName():
    assert hasattr(domain::RoleMapper, "globalRoleName")
    descriptor = None
    for klass in domain::RoleMapper.__mro__:
        if "globalRoleName" in klass.__dict__:
            descriptor = klass.__dict__["globalRoleName"]
            break
    assert isinstance(descriptor, property)

def test_domain::rolemapper_has_fakeRoleName():
    assert hasattr(domain::RoleMapper, "fakeRoleName")
    descriptor = None
    for klass in domain::RoleMapper.__mro__:
        if "fakeRoleName" in klass.__dict__:
            descriptor = klass.__dict__["fakeRoleName"]
            break
    assert isinstance(descriptor, property)



def test_domain::mapper_is_not_abstract():
    assert not inspect.isabstract(domain::Mapper)


def test_domain::mapper_constructor_exists():
    assert callable(domain::Mapper.__init__)


def test_domain::mapper_constructor_args():
    sig = inspect.signature(domain::Mapper.__init__)
    params = list(sig.parameters.keys())
    assert "uiLayer" in params, "Missing parameter 'uiLayer'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "serviceLayer" in params, "Missing parameter 'serviceLayer'"

def test_domain::mapper_has_uiLayer():
    assert hasattr(domain::Mapper, "uiLayer")
    descriptor = None
    for klass in domain::Mapper.__mro__:
        if "uiLayer" in klass.__dict__:
            descriptor = klass.__dict__["uiLayer"]
            break
    assert isinstance(descriptor, property)

def test_domain::mapper_has_uid():
    assert hasattr(domain::Mapper, "uid")
    descriptor = None
    for klass in domain::Mapper.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::mapper_has_serviceLayer():
    assert hasattr(domain::Mapper, "serviceLayer")
    descriptor = None
    for klass in domain::Mapper.__mro__:
        if "serviceLayer" in klass.__dict__:
            descriptor = klass.__dict__["serviceLayer"]
            break
    assert isinstance(descriptor, property)



def test_domain::stylelibrary_is_not_abstract():
    assert not inspect.isabstract(domain::StyleLibrary)


def test_domain::stylelibrary_constructor_exists():
    assert callable(domain::StyleLibrary.__init__)


def test_domain::stylelibrary_constructor_args():
    sig = inspect.signature(domain::StyleLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::stylelibrary_has_uid():
    assert hasattr(domain::StyleLibrary, "uid")
    descriptor = None
    for klass in domain::StyleLibrary.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::stylelibrary_has_name():
    assert hasattr(domain::StyleLibrary, "name")
    descriptor = None
    for klass in domain::StyleLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::group_is_not_abstract():
    assert not inspect.isabstract(domain::Group)


def test_domain::group_constructor_exists():
    assert callable(domain::Group.__init__)


def test_domain::group_constructor_args():
    sig = inspect.signature(domain::Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::group_has_name():
    assert hasattr(domain::Group, "name")
    descriptor = None
    for klass in domain::Group.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::group_has_uid():
    assert hasattr(domain::Group, "uid")
    descriptor = None
    for klass in domain::Group.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::styleset_is_not_abstract():
    assert not inspect.isabstract(domain::StyleSet)


def test_domain::styleset_constructor_exists():
    assert callable(domain::StyleSet.__init__)


def test_domain::styleset_constructor_args():
    sig = inspect.signature(domain::StyleSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::styleset_has_name():
    assert hasattr(domain::StyleSet, "name")
    descriptor = None
    for klass in domain::StyleSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::styleset_has_uid():
    assert hasattr(domain::StyleSet, "uid")
    descriptor = None
    for klass in domain::StyleSet.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::translation_is_not_abstract():
    assert not inspect.isabstract(domain::Translation)


def test_domain::translation_constructor_exists():
    assert callable(domain::Translation.__init__)


def test_domain::translation_constructor_args():
    sig = inspect.signature(domain::Translation.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "translation" in params, "Missing parameter 'translation'"

def test_domain::translation_has_uid():
    assert hasattr(domain::Translation, "uid")
    descriptor = None
    for klass in domain::Translation.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::translation_has_translation():
    assert hasattr(domain::Translation, "translation")
    descriptor = None
    for klass in domain::Translation.__mro__:
        if "translation" in klass.__dict__:
            descriptor = klass.__dict__["translation"]
            break
    assert isinstance(descriptor, property)



def test_domain::message_is_not_abstract():
    assert not inspect.isabstract(domain::Message)


def test_domain::message_constructor_exists():
    assert callable(domain::Message.__init__)


def test_domain::message_constructor_args():
    sig = inspect.signature(domain::Message.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::message_has_uid():
    assert hasattr(domain::Message, "uid")
    descriptor = None
    for klass in domain::Message.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::message_has_name():
    assert hasattr(domain::Message, "name")
    descriptor = None
    for klass in domain::Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::languageref_is_not_abstract():
    assert not inspect.isabstract(domain::LanguageRef)


def test_domain::languageref_constructor_exists():
    assert callable(domain::LanguageRef.__init__)


def test_domain::languageref_constructor_args():
    sig = inspect.signature(domain::LanguageRef.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::languageref_has_uid():
    assert hasattr(domain::LanguageRef, "uid")
    descriptor = None
    for klass in domain::LanguageRef.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_categorized_is_not_abstract():
    assert not inspect.isabstract(Categorized)


def test_categorized_constructor_exists():
    assert callable(Categorized.__init__)


def test_categorized_constructor_args():
    sig = inspect.signature(Categorized.__init__)
    params = list(sig.parameters.keys())



def test_domain::relationship_is_not_abstract():
    assert not inspect.isabstract(domain::RelationShip)


def test_domain::relationship_constructor_exists():
    assert callable(domain::RelationShip.__init__)


def test_domain::relationship_constructor_args():
    sig = inspect.signature(domain::RelationShip.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::relationship_has_uid():
    assert hasattr(domain::RelationShip, "uid")
    descriptor = None
    for klass in domain::RelationShip.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::popupcanvas_is_not_abstract():
    assert not inspect.isabstract(domain::PopupCanvas)


def test_domain::popupcanvas_constructor_exists():
    assert callable(domain::PopupCanvas.__init__)


def test_domain::popupcanvas_constructor_args():
    sig = inspect.signature(domain::PopupCanvas.__init__)
    params = list(sig.parameters.keys())
    assert "modal" in params, "Missing parameter 'modal'"

def test_domain::popupcanvas_has_modal():
    assert hasattr(domain::PopupCanvas, "modal")
    descriptor = None
    for klass in domain::PopupCanvas.__mro__:
        if "modal" in klass.__dict__:
            descriptor = klass.__dict__["modal"]
            break
    assert isinstance(descriptor, property)



def test_domain::type_is_not_abstract():
    assert not inspect.isabstract(domain::Type)


def test_domain::type_constructor_exists():
    assert callable(domain::Type.__init__)


def test_domain::type_constructor_args():
    sig = inspect.signature(domain::Type.__init__)
    params = list(sig.parameters.keys())



def test_domain::window_is_not_abstract():
    assert not inspect.isabstract(domain::Window)


def test_domain::window_constructor_exists():
    assert callable(domain::Window.__init__)


def test_domain::window_constructor_args():
    sig = inspect.signature(domain::Window.__init__)
    params = list(sig.parameters.keys())



def test_domain::canvas_is_not_abstract():
    assert not inspect.isabstract(domain::Canvas)


def test_domain::canvas_constructor_exists():
    assert callable(domain::Canvas.__init__)


def test_domain::canvas_constructor_args():
    sig = inspect.signature(domain::Canvas.__init__)
    params = list(sig.parameters.keys())



def test_domain::menudefinition_is_not_abstract():
    assert not inspect.isabstract(domain::MenuDefinition)


def test_domain::menudefinition_constructor_exists():
    assert callable(domain::MenuDefinition.__init__)


def test_domain::menudefinition_constructor_args():
    sig = inspect.signature(domain::MenuDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::menudefinition_has_uid():
    assert hasattr(domain::MenuDefinition, "uid")
    descriptor = None
    for klass in domain::MenuDefinition.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::menudefinition_has_name():
    assert hasattr(domain::MenuDefinition, "name")
    descriptor = None
    for klass in domain::MenuDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::viewelement_is_not_abstract():
    assert not inspect.isabstract(domain::ViewElement)


def test_domain::viewelement_constructor_exists():
    assert callable(domain::ViewElement.__init__)


def test_domain::viewelement_constructor_args():
    sig = inspect.signature(domain::ViewElement.__init__)
    params = list(sig.parameters.keys())



def test_domain::flexfield_is_not_abstract():
    assert not inspect.isabstract(domain::FlexField)


def test_domain::flexfield_constructor_exists():
    assert callable(domain::FlexField.__init__)


def test_domain::flexfield_constructor_args():
    sig = inspect.signature(domain::FlexField.__init__)
    params = list(sig.parameters.keys())



def test_domain::uielement_is_not_abstract():
    assert not inspect.isabstract(domain::Uielement)


def test_domain::uielement_constructor_exists():
    assert callable(domain::Uielement.__init__)


def test_domain::uielement_constructor_args():
    sig = inspect.signature(domain::Uielement.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::uielement_has_uid():
    assert hasattr(domain::Uielement, "uid")
    descriptor = None
    for klass in domain::Uielement.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::tabpage_is_not_abstract():
    assert not inspect.isabstract(domain::TabPage)


def test_domain::tabpage_constructor_exists():
    assert callable(domain::TabPage.__init__)


def test_domain::tabpage_constructor_args():
    sig = inspect.signature(domain::TabPage.__init__)
    params = list(sig.parameters.keys())



def test_domain::tabcanvas_is_not_abstract():
    assert not inspect.isabstract(domain::TabCanvas)


def test_domain::tabcanvas_constructor_exists():
    assert callable(domain::TabCanvas.__init__)


def test_domain::tabcanvas_constructor_args():
    sig = inspect.signature(domain::TabCanvas.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_domain::tabcanvas_has_orientation():
    assert hasattr(domain::TabCanvas, "orientation")
    descriptor = None
    for klass in domain::TabCanvas.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_domain::language_is_not_abstract():
    assert not inspect.isabstract(domain::Language)


def test_domain::language_constructor_exists():
    assert callable(domain::Language.__init__)


def test_domain::language_constructor_args():
    sig = inspect.signature(domain::Language.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "code" in params, "Missing parameter 'code'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "defaultLang" in params, "Missing parameter 'defaultLang'"

def test_domain::language_has_lang():
    assert hasattr(domain::Language, "lang")
    descriptor = None
    for klass in domain::Language.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)

def test_domain::language_has_code():
    assert hasattr(domain::Language, "code")
    descriptor = None
    for klass in domain::Language.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_domain::language_has_uid():
    assert hasattr(domain::Language, "uid")
    descriptor = None
    for klass in domain::Language.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::language_has_defaultLang():
    assert hasattr(domain::Language, "defaultLang")
    descriptor = None
    for klass in domain::Language.__mro__:
        if "defaultLang" in klass.__dict__:
            descriptor = klass.__dict__["defaultLang"]
            break
    assert isinstance(descriptor, property)



def test_domain::messagelibrary_is_not_abstract():
    assert not inspect.isabstract(domain::MessageLibrary)


def test_domain::messagelibrary_constructor_exists():
    assert callable(domain::MessageLibrary.__init__)


def test_domain::messagelibrary_constructor_args():
    sig = inspect.signature(domain::MessageLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::messagelibrary_has_name():
    assert hasattr(domain::MessageLibrary, "name")
    descriptor = None
    for klass in domain::MessageLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::messagelibrary_has_uid():
    assert hasattr(domain::MessageLibrary, "uid")
    descriptor = None
    for klass in domain::MessageLibrary.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::operation_is_not_abstract():
    assert not inspect.isabstract(domain::Operation)


def test_domain::operation_constructor_exists():
    assert callable(domain::Operation.__init__)


def test_domain::operation_constructor_args():
    sig = inspect.signature(domain::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::operation_has_uid():
    assert hasattr(domain::Operation, "uid")
    descriptor = None
    for klass in domain::Operation.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::operation_has_name():
    assert hasattr(domain::Operation, "name")
    descriptor = None
    for klass in domain::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typepointer_is_not_abstract():
    assert not inspect.isabstract(TypePointer)


def test_typepointer_constructor_exists():
    assert callable(TypePointer.__init__)


def test_typepointer_constructor_args():
    sig = inspect.signature(TypePointer.__init__)
    params = list(sig.parameters.keys())



def test_domain::formparameter_is_not_abstract():
    assert not inspect.isabstract(domain::FormParameter)


def test_domain::formparameter_constructor_exists():
    assert callable(domain::FormParameter.__init__)


def test_domain::formparameter_constructor_args():
    sig = inspect.signature(domain::FormParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::formparameter_has_name():
    assert hasattr(domain::FormParameter, "name")
    descriptor = None
    for klass in domain::FormParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::formparameter_has_uid():
    assert hasattr(domain::FormParameter, "uid")
    descriptor = None
    for klass in domain::FormParameter.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::typereference_is_not_abstract():
    assert not inspect.isabstract(domain::TypeReference)


def test_domain::typereference_constructor_exists():
    assert callable(domain::TypeReference.__init__)


def test_domain::typereference_constructor_args():
    sig = inspect.signature(domain::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_domain::attribute_is_not_abstract():
    assert not inspect.isabstract(domain::Attribute)


def test_domain::attribute_constructor_exists():
    assert callable(domain::Attribute.__init__)


def test_domain::attribute_constructor_args():
    sig = inspect.signature(domain::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "pk" in params, "Missing parameter 'pk'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::attribute_has_uid():
    assert hasattr(domain::Attribute, "uid")
    descriptor = None
    for klass in domain::Attribute.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::attribute_has_pk():
    assert hasattr(domain::Attribute, "pk")
    descriptor = None
    for klass in domain::Attribute.__mro__:
        if "pk" in klass.__dict__:
            descriptor = klass.__dict__["pk"]
            break
    assert isinstance(descriptor, property)

def test_domain::attribute_has_name():
    assert hasattr(domain::Attribute, "name")
    descriptor = None
    for klass in domain::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::typemapper_is_not_abstract():
    assert not inspect.isabstract(domain::TypeMapper)


def test_domain::typemapper_constructor_exists():
    assert callable(domain::TypeMapper.__init__)


def test_domain::typemapper_constructor_args():
    sig = inspect.signature(domain::TypeMapper.__init__)
    params = list(sig.parameters.keys())



def test_domain::returnvalue_is_not_abstract():
    assert not inspect.isabstract(domain::ReturnValue)


def test_domain::returnvalue_constructor_exists():
    assert callable(domain::ReturnValue.__init__)


def test_domain::returnvalue_constructor_args():
    sig = inspect.signature(domain::ReturnValue.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::returnvalue_has_uid():
    assert hasattr(domain::ReturnValue, "uid")
    descriptor = None
    for klass in domain::ReturnValue.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::parameter_is_not_abstract():
    assert not inspect.isabstract(domain::Parameter)


def test_domain::parameter_constructor_exists():
    assert callable(domain::Parameter.__init__)


def test_domain::parameter_constructor_args():
    sig = inspect.signature(domain::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "order" in params, "Missing parameter 'order'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::parameter_has_name():
    assert hasattr(domain::Parameter, "name")
    descriptor = None
    for klass in domain::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::parameter_has_order():
    assert hasattr(domain::Parameter, "order")
    descriptor = None
    for klass in domain::Parameter.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_domain::parameter_has_uid():
    assert hasattr(domain::Parameter, "uid")
    descriptor = None
    for klass in domain::Parameter.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::methodpointer_is_not_abstract():
    assert not inspect.isabstract(domain::MethodPointer)


def test_domain::methodpointer_constructor_exists():
    assert callable(domain::MethodPointer.__init__)


def test_domain::methodpointer_constructor_args():
    sig = inspect.signature(domain::MethodPointer.__init__)
    params = list(sig.parameters.keys())
    assert "fakeMethod" in params, "Missing parameter 'fakeMethod'"

def test_domain::methodpointer_has_fakeMethod():
    assert hasattr(domain::MethodPointer, "fakeMethod")
    descriptor = None
    for klass in domain::MethodPointer.__mro__:
        if "fakeMethod" in klass.__dict__:
            descriptor = klass.__dict__["fakeMethod"]
            break
    assert isinstance(descriptor, property)



def test_domain::mappers_is_not_abstract():
    assert not inspect.isabstract(domain::Mappers)


def test_domain::mappers_constructor_exists():
    assert callable(domain::Mappers.__init__)


def test_domain::mappers_constructor_args():
    sig = inspect.signature(domain::Mappers.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::mappers_has_uid():
    assert hasattr(domain::Mappers, "uid")
    descriptor = None
    for klass in domain::Mappers.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::applicationmapper_is_not_abstract():
    assert not inspect.isabstract(domain::ApplicationMapper)


def test_domain::applicationmapper_constructor_exists():
    assert callable(domain::ApplicationMapper.__init__)


def test_domain::applicationmapper_constructor_args():
    sig = inspect.signature(domain::ApplicationMapper.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::applicationmapper_has_uid():
    assert hasattr(domain::ApplicationMapper, "uid")
    descriptor = None
    for klass in domain::ApplicationMapper.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::applicationmapper_has_name():
    assert hasattr(domain::ApplicationMapper, "name")
    descriptor = None
    for klass in domain::ApplicationMapper.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::recipes_is_not_abstract():
    assert not inspect.isabstract(domain::Recipes)


def test_domain::recipes_constructor_exists():
    assert callable(domain::Recipes.__init__)


def test_domain::recipes_constructor_args():
    sig = inspect.signature(domain::Recipes.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::recipes_has_uid():
    assert hasattr(domain::Recipes, "uid")
    descriptor = None
    for klass in domain::Recipes.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::applicationrecipe_is_not_abstract():
    assert not inspect.isabstract(domain::ApplicationRecipe)


def test_domain::applicationrecipe_constructor_exists():
    assert callable(domain::ApplicationRecipe.__init__)


def test_domain::applicationrecipe_constructor_args():
    sig = inspect.signature(domain::ApplicationRecipe.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::applicationrecipe_has_uid():
    assert hasattr(domain::ApplicationRecipe, "uid")
    descriptor = None
    for klass in domain::ApplicationRecipe.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::applicationrecipe_has_name():
    assert hasattr(domain::ApplicationRecipe, "name")
    descriptor = None
    for klass in domain::ApplicationRecipe.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::uipackage_is_not_abstract():
    assert not inspect.isabstract(domain::UIPackage)


def test_domain::uipackage_constructor_exists():
    assert callable(domain::UIPackage.__init__)


def test_domain::uipackage_constructor_args():
    sig = inspect.signature(domain::UIPackage.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::uipackage_has_uid():
    assert hasattr(domain::UIPackage, "uid")
    descriptor = None
    for klass in domain::UIPackage.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::applicationuipackage_is_not_abstract():
    assert not inspect.isabstract(domain::ApplicationUIPackage)


def test_domain::applicationuipackage_constructor_exists():
    assert callable(domain::ApplicationUIPackage.__init__)


def test_domain::applicationuipackage_constructor_args():
    sig = inspect.signature(domain::ApplicationUIPackage.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::applicationuipackage_has_uid():
    assert hasattr(domain::ApplicationUIPackage, "uid")
    descriptor = None
    for klass in domain::ApplicationUIPackage.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::applicationuipackage_has_name():
    assert hasattr(domain::ApplicationUIPackage, "name")
    descriptor = None
    for klass in domain::ApplicationUIPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::styles_is_not_abstract():
    assert not inspect.isabstract(domain::Styles)


def test_domain::styles_constructor_exists():
    assert callable(domain::Styles.__init__)


def test_domain::styles_constructor_args():
    sig = inspect.signature(domain::Styles.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::styles_has_uid():
    assert hasattr(domain::Styles, "uid")
    descriptor = None
    for klass in domain::Styles.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::roles_is_not_abstract():
    assert not inspect.isabstract(domain::Roles)


def test_domain::roles_constructor_exists():
    assert callable(domain::Roles.__init__)


def test_domain::roles_constructor_args():
    sig = inspect.signature(domain::Roles.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::roles_has_uid():
    assert hasattr(domain::Roles, "uid")
    descriptor = None
    for klass in domain::Roles.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::messages_is_not_abstract():
    assert not inspect.isabstract(domain::Messages)


def test_domain::messages_constructor_exists():
    assert callable(domain::Messages.__init__)


def test_domain::messages_constructor_args():
    sig = inspect.signature(domain::Messages.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::messages_has_uid():
    assert hasattr(domain::Messages, "uid")
    descriptor = None
    for klass in domain::Messages.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::applicationmessages_is_not_abstract():
    assert not inspect.isabstract(domain::ApplicationMessages)


def test_domain::applicationmessages_constructor_exists():
    assert callable(domain::ApplicationMessages.__init__)


def test_domain::applicationmessages_constructor_args():
    sig = inspect.signature(domain::ApplicationMessages.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::applicationmessages_has_name():
    assert hasattr(domain::ApplicationMessages, "name")
    descriptor = None
    for klass in domain::ApplicationMessages.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::applicationmessages_has_uid():
    assert hasattr(domain::ApplicationMessages, "uid")
    descriptor = None
    for klass in domain::ApplicationMessages.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::applicationrole_is_not_abstract():
    assert not inspect.isabstract(domain::ApplicationRole)


def test_domain::applicationrole_constructor_exists():
    assert callable(domain::ApplicationRole.__init__)


def test_domain::applicationrole_constructor_args():
    sig = inspect.signature(domain::ApplicationRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::applicationrole_has_name():
    assert hasattr(domain::ApplicationRole, "name")
    descriptor = None
    for klass in domain::ApplicationRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::applicationrole_has_uid():
    assert hasattr(domain::ApplicationRole, "uid")
    descriptor = None
    for klass in domain::ApplicationRole.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::applicationinfrastructurelayer_is_not_abstract():
    assert not inspect.isabstract(domain::ApplicationInfrastructureLayer)


def test_domain::applicationinfrastructurelayer_constructor_exists():
    assert callable(domain::ApplicationInfrastructureLayer.__init__)


def test_domain::applicationinfrastructurelayer_constructor_args():
    sig = inspect.signature(domain::ApplicationInfrastructureLayer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::applicationinfrastructurelayer_has_name():
    assert hasattr(domain::ApplicationInfrastructureLayer, "name")
    descriptor = None
    for klass in domain::ApplicationInfrastructureLayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::applicationinfrastructurelayer_has_uid():
    assert hasattr(domain::ApplicationInfrastructureLayer, "uid")
    descriptor = None
    for klass in domain::ApplicationInfrastructureLayer.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::stylespackage_is_not_abstract():
    assert not inspect.isabstract(domain::StylesPackage)


def test_domain::stylespackage_constructor_exists():
    assert callable(domain::StylesPackage.__init__)


def test_domain::stylespackage_constructor_args():
    sig = inspect.signature(domain::StylesPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::stylespackage_has_name():
    assert hasattr(domain::StylesPackage, "name")
    descriptor = None
    for klass in domain::StylesPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::stylespackage_has_uid():
    assert hasattr(domain::StylesPackage, "uid")
    descriptor = None
    for klass in domain::StylesPackage.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::option_is_not_abstract():
    assert not inspect.isabstract(domain::Option)


def test_domain::option_constructor_exists():
    assert callable(domain::Option.__init__)


def test_domain::option_constructor_args():
    sig = inspect.signature(domain::Option.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "value" in params, "Missing parameter 'value'"

def test_domain::option_has_uid():
    assert hasattr(domain::Option, "uid")
    descriptor = None
    for klass in domain::Option.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::option_has_value():
    assert hasattr(domain::Option, "value")
    descriptor = None
    for klass in domain::Option.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_domain::queryparameter_is_not_abstract():
    assert not inspect.isabstract(domain::QueryParameter)


def test_domain::queryparameter_constructor_exists():
    assert callable(domain::QueryParameter.__init__)


def test_domain::queryparameter_constructor_args():
    sig = inspect.signature(domain::QueryParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::queryparameter_has_name():
    assert hasattr(domain::QueryParameter, "name")
    descriptor = None
    for klass in domain::QueryParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::queryparameter_has_uid():
    assert hasattr(domain::QueryParameter, "uid")
    descriptor = None
    for klass in domain::QueryParameter.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::specifier_is_not_abstract():
    assert not inspect.isabstract(domain::Specifier)


def test_domain::specifier_constructor_exists():
    assert callable(domain::Specifier.__init__)


def test_domain::specifier_constructor_args():
    sig = inspect.signature(domain::Specifier.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::specifier_has_uid():
    assert hasattr(domain::Specifier, "uid")
    descriptor = None
    for klass in domain::Specifier.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::specifier_has_name():
    assert hasattr(domain::Specifier, "name")
    descriptor = None
    for klass in domain::Specifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::modelquery_is_not_abstract():
    assert not inspect.isabstract(domain::ModelQuery)


def test_domain::modelquery_constructor_exists():
    assert callable(domain::ModelQuery.__init__)


def test_domain::modelquery_constructor_args():
    sig = inspect.signature(domain::ModelQuery.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "query" in params, "Missing parameter 'query'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::modelquery_has_uid():
    assert hasattr(domain::ModelQuery, "uid")
    descriptor = None
    for klass in domain::ModelQuery.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::modelquery_has_query():
    assert hasattr(domain::ModelQuery, "query")
    descriptor = None
    for klass in domain::ModelQuery.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_domain::modelquery_has_name():
    assert hasattr(domain::ModelQuery, "name")
    descriptor = None
    for klass in domain::ModelQuery.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::confighash_is_not_abstract():
    assert not inspect.isabstract(domain::ConfigHash)


def test_domain::confighash_constructor_exists():
    assert callable(domain::ConfigHash.__init__)


def test_domain::confighash_constructor_args():
    sig = inspect.signature(domain::ConfigHash.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::confighash_has_name():
    assert hasattr(domain::ConfigHash, "name")
    descriptor = None
    for klass in domain::ConfigHash.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::confighash_has_uid():
    assert hasattr(domain::ConfigHash, "uid")
    descriptor = None
    for klass in domain::ConfigHash.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::configvariable_is_not_abstract():
    assert not inspect.isabstract(domain::ConfigVariable)


def test_domain::configvariable_constructor_exists():
    assert callable(domain::ConfigVariable.__init__)


def test_domain::configvariable_constructor_args():
    sig = inspect.signature(domain::ConfigVariable.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::configvariable_has_uid():
    assert hasattr(domain::ConfigVariable, "uid")
    descriptor = None
    for klass in domain::ConfigVariable.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::configvariable_has_name():
    assert hasattr(domain::ConfigVariable, "name")
    descriptor = None
    for klass in domain::ConfigVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::artifact_is_not_abstract():
    assert not inspect.isabstract(domain::Artifact)


def test_domain::artifact_constructor_exists():
    assert callable(domain::Artifact.__init__)


def test_domain::artifact_constructor_args():
    sig = inspect.signature(domain::Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "template" in params, "Missing parameter 'template'"
    assert "description" in params, "Missing parameter 'description'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::artifact_has_template():
    assert hasattr(domain::Artifact, "template")
    descriptor = None
    for klass in domain::Artifact.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_domain::artifact_has_description():
    assert hasattr(domain::Artifact, "description")
    descriptor = None
    for klass in domain::Artifact.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_domain::artifact_has_uid():
    assert hasattr(domain::Artifact, "uid")
    descriptor = None
    for klass in domain::Artifact.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::artifact_has_name():
    assert hasattr(domain::Artifact, "name")
    descriptor = None
    for klass in domain::Artifact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainartifact_is_not_abstract():
    assert not inspect.isabstract(DomainArtifact)


def test_domainartifact_constructor_exists():
    assert callable(DomainArtifact.__init__)


def test_domainartifact_constructor_args():
    sig = inspect.signature(DomainArtifact.__init__)
    params = list(sig.parameters.keys())



def test_domain::jpaservice_is_not_abstract():
    assert not inspect.isabstract(domain::JPAService)


def test_domain::jpaservice_constructor_exists():
    assert callable(domain::JPAService.__init__)


def test_domain::jpaservice_constructor_args():
    sig = inspect.signature(domain::JPAService.__init__)
    params = list(sig.parameters.keys())



def test_domain::ejbservice_is_not_abstract():
    assert not inspect.isabstract(domain::EJBService)


def test_domain::ejbservice_constructor_exists():
    assert callable(domain::EJBService.__init__)


def test_domain::ejbservice_constructor_args():
    sig = inspect.signature(domain::EJBService.__init__)
    params = list(sig.parameters.keys())



def test_domain::continuousiintegration_is_not_abstract():
    assert not inspect.isabstract(domain::ContinuousIintegration)


def test_domain::continuousiintegration_constructor_exists():
    assert callable(domain::ContinuousIintegration.__init__)


def test_domain::continuousiintegration_constructor_args():
    sig = inspect.signature(domain::ContinuousIintegration.__init__)
    params = list(sig.parameters.keys())



def test_domain::ormentity_is_not_abstract():
    assert not inspect.isabstract(domain::ORMEntity)


def test_domain::ormentity_constructor_exists():
    assert callable(domain::ORMEntity.__init__)


def test_domain::ormentity_constructor_args():
    sig = inspect.signature(domain::ORMEntity.__init__)
    params = list(sig.parameters.keys())



def test_domain::artifacts_is_not_abstract():
    assert not inspect.isabstract(domain::Artifacts)


def test_domain::artifacts_constructor_exists():
    assert callable(domain::Artifacts.__init__)


def test_domain::artifacts_constructor_args():
    sig = inspect.signature(domain::Artifacts.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::artifacts_has_uid():
    assert hasattr(domain::Artifacts, "uid")
    descriptor = None
    for klass in domain::Artifacts.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::application_is_not_abstract():
    assert not inspect.isabstract(domain::Application)


def test_domain::application_constructor_exists():
    assert callable(domain::Application.__init__)


def test_domain::application_constructor_args():
    sig = inspect.signature(domain::Application.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::application_has_uid():
    assert hasattr(domain::Application, "uid")
    descriptor = None
    for klass in domain::Application.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::domainartifact_is_not_abstract():
    assert not inspect.isabstract(domain::DomainArtifact)


def test_domain::domainartifact_constructor_exists():
    assert callable(domain::DomainArtifact.__init__)


def test_domain::domainartifact_constructor_args():
    sig = inspect.signature(domain::DomainArtifact.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::domainartifact_has_name():
    assert hasattr(domain::DomainArtifact, "name")
    descriptor = None
    for klass in domain::DomainArtifact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::domainartifact_has_uid():
    assert hasattr(domain::DomainArtifact, "uid")
    descriptor = None
    for klass in domain::DomainArtifact.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_htmllayerholder_is_not_abstract():
    assert not inspect.isabstract(HTMLLayerHolder)


def test_htmllayerholder_constructor_exists():
    assert callable(HTMLLayerHolder.__init__)


def test_htmllayerholder_constructor_args():
    sig = inspect.signature(HTMLLayerHolder.__init__)
    params = list(sig.parameters.keys())



def test_domain::applicationstyle_is_not_abstract():
    assert not inspect.isabstract(domain::ApplicationStyle)


def test_domain::applicationstyle_constructor_exists():
    assert callable(domain::ApplicationStyle.__init__)


def test_domain::applicationstyle_constructor_args():
    sig = inspect.signature(domain::ApplicationStyle.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::applicationstyle_has_name():
    assert hasattr(domain::ApplicationStyle, "name")
    descriptor = None
    for klass in domain::ApplicationStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::applicationstyle_has_uid():
    assert hasattr(domain::ApplicationStyle, "uid")
    descriptor = None
    for klass in domain::ApplicationStyle.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::types_is_not_abstract():
    assert not inspect.isabstract(domain::Types)


def test_domain::types_constructor_exists():
    assert callable(domain::Types.__init__)


def test_domain::types_constructor_args():
    sig = inspect.signature(domain::Types.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::types_has_uid():
    assert hasattr(domain::Types, "uid")
    descriptor = None
    for klass in domain::Types.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::types_has_name():
    assert hasattr(domain::Types, "name")
    descriptor = None
    for klass in domain::Types.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::ingredient_is_not_abstract():
    assert not inspect.isabstract(domain::Ingredient)


def test_domain::ingredient_constructor_exists():
    assert callable(domain::Ingredient.__init__)


def test_domain::ingredient_constructor_args():
    sig = inspect.signature(domain::Ingredient.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "layer" in params, "Missing parameter 'layer'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::ingredient_has_uid():
    assert hasattr(domain::Ingredient, "uid")
    descriptor = None
    for klass in domain::Ingredient.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::ingredient_has_layer():
    assert hasattr(domain::Ingredient, "layer")
    descriptor = None
    for klass in domain::Ingredient.__mro__:
        if "layer" in klass.__dict__:
            descriptor = klass.__dict__["layer"]
            break
    assert isinstance(descriptor, property)

def test_domain::ingredient_has_name():
    assert hasattr(domain::Ingredient, "name")
    descriptor = None
    for klass in domain::Ingredient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::applicationmappers_is_not_abstract():
    assert not inspect.isabstract(domain::ApplicationMappers)


def test_domain::applicationmappers_constructor_exists():
    assert callable(domain::ApplicationMappers.__init__)


def test_domain::applicationmappers_constructor_args():
    sig = inspect.signature(domain::ApplicationMappers.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::applicationmappers_has_name():
    assert hasattr(domain::ApplicationMappers, "name")
    descriptor = None
    for klass in domain::ApplicationMappers.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::applicationmappers_has_uid():
    assert hasattr(domain::ApplicationMappers, "uid")
    descriptor = None
    for klass in domain::ApplicationMappers.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::component_is_not_abstract():
    assert not inspect.isabstract(domain::Component)


def test_domain::component_constructor_exists():
    assert callable(domain::Component.__init__)


def test_domain::component_constructor_args():
    sig = inspect.signature(domain::Component.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"
    assert "componentRoot" in params, "Missing parameter 'componentRoot'"

def test_domain::component_has_uid():
    assert hasattr(domain::Component, "uid")
    descriptor = None
    for klass in domain::Component.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::component_has_name():
    assert hasattr(domain::Component, "name")
    descriptor = None
    for klass in domain::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::component_has_componentRoot():
    assert hasattr(domain::Component, "componentRoot")
    descriptor = None
    for klass in domain::Component.__mro__:
        if "componentRoot" in klass.__dict__:
            descriptor = klass.__dict__["componentRoot"]
            break
    assert isinstance(descriptor, property)



def test_domain::applicationrecipes_is_not_abstract():
    assert not inspect.isabstract(domain::ApplicationRecipes)


def test_domain::applicationrecipes_constructor_exists():
    assert callable(domain::ApplicationRecipes.__init__)


def test_domain::applicationrecipes_constructor_args():
    sig = inspect.signature(domain::ApplicationRecipes.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::applicationrecipes_has_uid():
    assert hasattr(domain::ApplicationRecipes, "uid")
    descriptor = None
    for klass in domain::ApplicationRecipes.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::applicationrecipes_has_name():
    assert hasattr(domain::ApplicationRecipes, "name")
    descriptor = None
    for klass in domain::ApplicationRecipes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::viewportholder_is_not_abstract():
    assert not inspect.isabstract(domain::ViewPortHolder)


def test_domain::viewportholder_constructor_exists():
    assert callable(domain::ViewPortHolder.__init__)


def test_domain::viewportholder_constructor_args():
    sig = inspect.signature(domain::ViewPortHolder.__init__)
    params = list(sig.parameters.keys())



def test_domain::layerholder_is_not_abstract():
    assert not inspect.isabstract(domain::LayerHolder)


def test_domain::layerholder_constructor_exists():
    assert callable(domain::LayerHolder.__init__)


def test_domain::layerholder_constructor_args():
    sig = inspect.signature(domain::LayerHolder.__init__)
    params = list(sig.parameters.keys())



def test_domain::applicationuilayer_is_not_abstract():
    assert not inspect.isabstract(domain::ApplicationUILayer)


def test_domain::applicationuilayer_constructor_exists():
    assert callable(domain::ApplicationUILayer.__init__)


def test_domain::applicationuilayer_constructor_args():
    sig = inspect.signature(domain::ApplicationUILayer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::applicationuilayer_has_name():
    assert hasattr(domain::ApplicationUILayer, "name")
    descriptor = None
    for klass in domain::ApplicationUILayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::applicationuilayer_has_uid():
    assert hasattr(domain::ApplicationUILayer, "uid")
    descriptor = None
    for klass in domain::ApplicationUILayer.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::role_is_not_abstract():
    assert not inspect.isabstract(domain::Role)


def test_domain::role_constructor_exists():
    assert callable(domain::Role.__init__)


def test_domain::role_constructor_args():
    sig = inspect.signature(domain::Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::role_has_name():
    assert hasattr(domain::Role, "name")
    descriptor = None
    for klass in domain::Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::role_has_uid():
    assert hasattr(domain::Role, "uid")
    descriptor = None
    for klass in domain::Role.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::domainapplication_is_not_abstract():
    assert not inspect.isabstract(domain::DomainApplication)


def test_domain::domainapplication_constructor_exists():
    assert callable(domain::DomainApplication.__init__)


def test_domain::domainapplication_constructor_args():
    sig = inspect.signature(domain::DomainApplication.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::domainapplication_has_uid():
    assert hasattr(domain::DomainApplication, "uid")
    descriptor = None
    for klass in domain::DomainApplication.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::domainapplication_has_name():
    assert hasattr(domain::DomainApplication, "name")
    descriptor = None
    for klass in domain::DomainApplication.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::grantaccess_is_not_abstract():
    assert not inspect.isabstract(domain::GrantAccess)


def test_domain::grantaccess_constructor_exists():
    assert callable(domain::GrantAccess.__init__)


def test_domain::grantaccess_constructor_args():
    sig = inspect.signature(domain::GrantAccess.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::grantaccess_has_uid():
    assert hasattr(domain::GrantAccess, "uid")
    descriptor = None
    for klass in domain::GrantAccess.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::secured_is_not_abstract():
    assert not inspect.isabstract(domain::Secured)


def test_domain::secured_constructor_exists():
    assert callable(domain::Secured.__init__)


def test_domain::secured_constructor_args():
    sig = inspect.signature(domain::Secured.__init__)
    params = list(sig.parameters.keys())



def test_domain::generationhint_is_not_abstract():
    assert not inspect.isabstract(domain::GenerationHint)


def test_domain::generationhint_constructor_exists():
    assert callable(domain::GenerationHint.__init__)


def test_domain::generationhint_constructor_args():
    sig = inspect.signature(domain::GenerationHint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "applyedClass" in params, "Missing parameter 'applyedClass'"

def test_domain::generationhint_has_name():
    assert hasattr(domain::GenerationHint, "name")
    descriptor = None
    for klass in domain::GenerationHint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::generationhint_has_uid():
    assert hasattr(domain::GenerationHint, "uid")
    descriptor = None
    for klass in domain::GenerationHint.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::generationhint_has_applyedClass():
    assert hasattr(domain::GenerationHint, "applyedClass")
    descriptor = None
    for klass in domain::GenerationHint.__mro__:
        if "applyedClass" in klass.__dict__:
            descriptor = klass.__dict__["applyedClass"]
            break
    assert isinstance(descriptor, property)



def test_domain::classifier_is_not_abstract():
    assert not inspect.isabstract(domain::Classifier)


def test_domain::classifier_constructor_exists():
    assert callable(domain::Classifier.__init__)


def test_domain::classifier_constructor_args():
    sig = inspect.signature(domain::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "details" in params, "Missing parameter 'details'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::classifier_has_details():
    assert hasattr(domain::Classifier, "details")
    descriptor = None
    for klass in domain::Classifier.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_domain::classifier_has_uid():
    assert hasattr(domain::Classifier, "uid")
    descriptor = None
    for klass in domain::Classifier.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::categorized_is_not_abstract():
    assert not inspect.isabstract(domain::Categorized)


def test_domain::categorized_constructor_exists():
    assert callable(domain::Categorized.__init__)


def test_domain::categorized_constructor_args():
    sig = inspect.signature(domain::Categorized.__init__)
    params = list(sig.parameters.keys())



def test_domain::htmllayerholder_is_not_abstract():
    assert not inspect.isabstract(domain::HTMLLayerHolder)


def test_domain::htmllayerholder_constructor_exists():
    assert callable(domain::HTMLLayerHolder.__init__)


def test_domain::htmllayerholder_constructor_args():
    sig = inspect.signature(domain::HTMLLayerHolder.__init__)
    params = list(sig.parameters.keys())
    assert "columns" in params, "Missing parameter 'columns'"

def test_domain::htmllayerholder_has_columns():
    assert hasattr(domain::HTMLLayerHolder, "columns")
    descriptor = None
    for klass in domain::HTMLLayerHolder.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)



def test_domain::eobject_is_not_abstract():
    assert not inspect.isabstract(domain::EObject)


def test_domain::eobject_constructor_exists():
    assert callable(domain::EObject.__init__)


def test_domain::eobject_constructor_args():
    sig = inspect.signature(domain::EObject.__init__)
    params = list(sig.parameters.keys())



def test_domain::domainapplications_is_not_abstract():
    assert not inspect.isabstract(domain::DomainApplications)


def test_domain::domainapplications_constructor_exists():
    assert callable(domain::DomainApplications.__init__)


def test_domain::domainapplications_constructor_args():
    sig = inspect.signature(domain::DomainApplications.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::domainapplications_has_uid():
    assert hasattr(domain::DomainApplications, "uid")
    descriptor = None
    for klass in domain::DomainApplications.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::domainapplications_has_name():
    assert hasattr(domain::DomainApplications, "name")
    descriptor = None
    for klass in domain::DomainApplications.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::domaintypes_is_not_abstract():
    assert not inspect.isabstract(domain::DomainTypes)


def test_domain::domaintypes_constructor_exists():
    assert callable(domain::DomainTypes.__init__)


def test_domain::domaintypes_constructor_args():
    sig = inspect.signature(domain::DomainTypes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::domaintypes_has_name():
    assert hasattr(domain::DomainTypes, "name")
    descriptor = None
    for klass in domain::DomainTypes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::domaintypes_has_uid():
    assert hasattr(domain::DomainTypes, "uid")
    descriptor = None
    for klass in domain::DomainTypes.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::domainartifacts_is_not_abstract():
    assert not inspect.isabstract(domain::DomainArtifacts)


def test_domain::domainartifacts_constructor_exists():
    assert callable(domain::DomainArtifacts.__init__)


def test_domain::domainartifacts_constructor_args():
    sig = inspect.signature(domain::DomainArtifacts.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::domainartifacts_has_uid():
    assert hasattr(domain::DomainArtifacts, "uid")
    descriptor = None
    for klass in domain::DomainArtifacts.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::domainartifacts_has_name():
    assert hasattr(domain::DomainArtifacts, "name")
    descriptor = None
    for klass in domain::DomainArtifacts.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::domain_is_not_abstract():
    assert not inspect.isabstract(domain::Domain)


def test_domain::domain_constructor_exists():
    assert callable(domain::Domain.__init__)


def test_domain::domain_constructor_args():
    sig = inspect.signature(domain::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::domain_has_uid():
    assert hasattr(domain::Domain, "uid")
    descriptor = None
    for klass in domain::Domain.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::typesrepository_is_not_abstract():
    assert not inspect.isabstract(domain::TypesRepository)


def test_domain::typesrepository_constructor_exists():
    assert callable(domain::TypesRepository.__init__)


def test_domain::typesrepository_constructor_args():
    sig = inspect.signature(domain::TypesRepository.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::typesrepository_has_uid():
    assert hasattr(domain::TypesRepository, "uid")
    descriptor = None
    for klass in domain::TypesRepository.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_menuelement_is_not_abstract():
    assert not inspect.isabstract(MenuElement)


def test_menuelement_constructor_exists():
    assert callable(MenuElement.__init__)


def test_menuelement_constructor_args():
    sig = inspect.signature(MenuElement.__init__)
    params = list(sig.parameters.keys())



def test_domain::menuseparator_is_not_abstract():
    assert not inspect.isabstract(domain::MenuSeparator)


def test_domain::menuseparator_constructor_exists():
    assert callable(domain::MenuSeparator.__init__)


def test_domain::menuseparator_constructor_args():
    sig = inspect.signature(domain::MenuSeparator.__init__)
    params = list(sig.parameters.keys())



def test_domain::menuextensionpoint_is_not_abstract():
    assert not inspect.isabstract(domain::MenuExtensionPoint)


def test_domain::menuextensionpoint_constructor_exists():
    assert callable(domain::MenuExtensionPoint.__init__)


def test_domain::menuextensionpoint_constructor_args():
    sig = inspect.signature(domain::MenuExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_domain::menuelement_is_not_abstract():
    assert not inspect.isabstract(domain::MenuElement)


def test_domain::menuelement_constructor_exists():
    assert callable(domain::MenuElement.__init__)


def test_domain::menuelement_constructor_args():
    sig = inspect.signature(domain::MenuElement.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::menuelement_has_uid():
    assert hasattr(domain::MenuElement, "uid")
    descriptor = None
    for klass in domain::MenuElement.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::menuelement_has_name():
    assert hasattr(domain::MenuElement, "name")
    descriptor = None
    for klass in domain::MenuElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::menuextensionref_is_not_abstract():
    assert not inspect.isabstract(domain::MenuExtensionRef)


def test_domain::menuextensionref_constructor_exists():
    assert callable(domain::MenuExtensionRef.__init__)


def test_domain::menuextensionref_constructor_args():
    sig = inspect.signature(domain::MenuExtensionRef.__init__)
    params = list(sig.parameters.keys())



def test_domain::menuholder_is_not_abstract():
    assert not inspect.isabstract(domain::MenuHolder)


def test_domain::menuholder_constructor_exists():
    assert callable(domain::MenuHolder.__init__)


def test_domain::menuholder_constructor_args():
    sig = inspect.signature(domain::MenuHolder.__init__)
    params = list(sig.parameters.keys())



def test_domain::infrastructurecomponent_is_not_abstract():
    assert not inspect.isabstract(domain::InfrastructureComponent)


def test_domain::infrastructurecomponent_constructor_exists():
    assert callable(domain::InfrastructureComponent.__init__)


def test_domain::infrastructurecomponent_constructor_args():
    sig = inspect.signature(domain::InfrastructureComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::infrastructurecomponent_has_name():
    assert hasattr(domain::InfrastructureComponent, "name")
    descriptor = None
    for klass in domain::InfrastructureComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::infrastructurecomponent_has_uid():
    assert hasattr(domain::InfrastructureComponent, "uid")
    descriptor = None
    for klass in domain::InfrastructureComponent.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::infrastructurelayer_is_not_abstract():
    assert not inspect.isabstract(domain::InfrastructureLayer)


def test_domain::infrastructurelayer_constructor_exists():
    assert callable(domain::InfrastructureLayer.__init__)


def test_domain::infrastructurelayer_constructor_args():
    sig = inspect.signature(domain::InfrastructureLayer.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::infrastructurelayer_has_uid():
    assert hasattr(domain::InfrastructureLayer, "uid")
    descriptor = None
    for klass in domain::InfrastructureLayer.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::infrastructurelayer_has_name():
    assert hasattr(domain::InfrastructureLayer, "name")
    descriptor = None
    for klass in domain::InfrastructureLayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::subsystem_is_not_abstract():
    assert not inspect.isabstract(domain::Subsystem)


def test_domain::subsystem_constructor_exists():
    assert callable(domain::Subsystem.__init__)


def test_domain::subsystem_constructor_args():
    sig = inspect.signature(domain::Subsystem.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::subsystem_has_uid():
    assert hasattr(domain::Subsystem, "uid")
    descriptor = None
    for klass in domain::Subsystem.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::subsystem_has_name():
    assert hasattr(domain::Subsystem, "name")
    descriptor = None
    for klass in domain::Subsystem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_infrastructurecomponent_is_not_abstract():
    assert not inspect.isabstract(InfrastructureComponent)


def test_infrastructurecomponent_constructor_exists():
    assert callable(InfrastructureComponent.__init__)


def test_infrastructurecomponent_constructor_args():
    sig = inspect.signature(InfrastructureComponent.__init__)
    params = list(sig.parameters.keys())



def test_domain::hub_is_not_abstract():
    assert not inspect.isabstract(domain::Hub)


def test_domain::hub_constructor_exists():
    assert callable(domain::Hub.__init__)


def test_domain::hub_constructor_args():
    sig = inspect.signature(domain::Hub.__init__)
    params = list(sig.parameters.keys())



def test_domain::serverclaster_is_not_abstract():
    assert not inspect.isabstract(domain::ServerClaster)


def test_domain::serverclaster_constructor_exists():
    assert callable(domain::ServerClaster.__init__)


def test_domain::serverclaster_constructor_args():
    sig = inspect.signature(domain::ServerClaster.__init__)
    params = list(sig.parameters.keys())



def test_domain::router_is_not_abstract():
    assert not inspect.isabstract(domain::Router)


def test_domain::router_constructor_exists():
    assert callable(domain::Router.__init__)


def test_domain::router_constructor_args():
    sig = inspect.signature(domain::Router.__init__)
    params = list(sig.parameters.keys())



def test_domain::storage_is_not_abstract():
    assert not inspect.isabstract(domain::Storage)


def test_domain::storage_constructor_exists():
    assert callable(domain::Storage.__init__)


def test_domain::storage_constructor_args():
    sig = inspect.signature(domain::Storage.__init__)
    params = list(sig.parameters.keys())



def test_domain::server_is_not_abstract():
    assert not inspect.isabstract(domain::Server)


def test_domain::server_constructor_exists():
    assert callable(domain::Server.__init__)


def test_domain::server_constructor_args():
    sig = inspect.signature(domain::Server.__init__)
    params = list(sig.parameters.keys())



def test_domain::enterpriseinfrastructure_is_not_abstract():
    assert not inspect.isabstract(domain::EnterpriseInfrastructure)


def test_domain::enterpriseinfrastructure_constructor_exists():
    assert callable(domain::EnterpriseInfrastructure.__init__)


def test_domain::enterpriseinfrastructure_constructor_args():
    sig = inspect.signature(domain::EnterpriseInfrastructure.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::enterpriseinfrastructure_has_uid():
    assert hasattr(domain::EnterpriseInfrastructure, "uid")
    descriptor = None
    for klass in domain::EnterpriseInfrastructure.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::infrastructureconnection_is_not_abstract():
    assert not inspect.isabstract(domain::InfrastructureConnection)


def test_domain::infrastructureconnection_constructor_exists():
    assert callable(domain::InfrastructureConnection.__init__)


def test_domain::infrastructureconnection_constructor_args():
    sig = inspect.signature(domain::InfrastructureConnection.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::infrastructureconnection_has_uid():
    assert hasattr(domain::InfrastructureConnection, "uid")
    descriptor = None
    for klass in domain::InfrastructureConnection.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::datacenter_is_not_abstract():
    assert not inspect.isabstract(domain::Datacenter)


def test_domain::datacenter_constructor_exists():
    assert callable(domain::Datacenter.__init__)


def test_domain::datacenter_constructor_args():
    sig = inspect.signature(domain::Datacenter.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::datacenter_has_uid():
    assert hasattr(domain::Datacenter, "uid")
    descriptor = None
    for klass in domain::Datacenter.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::datacenter_has_name():
    assert hasattr(domain::Datacenter, "name")
    descriptor = None
    for klass in domain::Datacenter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::orderby_is_not_abstract():
    assert not inspect.isabstract(domain::OrderBy)


def test_domain::orderby_constructor_exists():
    assert callable(domain::OrderBy.__init__)


def test_domain::orderby_constructor_args():
    sig = inspect.signature(domain::OrderBy.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "order" in params, "Missing parameter 'order'"

def test_domain::orderby_has_uid():
    assert hasattr(domain::OrderBy, "uid")
    descriptor = None
    for klass in domain::OrderBy.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::orderby_has_order():
    assert hasattr(domain::OrderBy, "order")
    descriptor = None
    for klass in domain::OrderBy.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_domain::orders_is_not_abstract():
    assert not inspect.isabstract(domain::Orders)


def test_domain::orders_constructor_exists():
    assert callable(domain::Orders.__init__)


def test_domain::orders_constructor_args():
    sig = inspect.signature(domain::Orders.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::orders_has_uid():
    assert hasattr(domain::Orders, "uid")
    descriptor = None
    for klass in domain::Orders.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::artificialfield_is_not_abstract():
    assert not inspect.isabstract(domain::ArtificialField)


def test_domain::artificialfield_constructor_exists():
    assert callable(domain::ArtificialField.__init__)


def test_domain::artificialfield_constructor_args():
    sig = inspect.signature(domain::ArtificialField.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::artificialfield_has_uid():
    assert hasattr(domain::ArtificialField, "uid")
    descriptor = None
    for klass in domain::ArtificialField.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::artificialfield_has_name():
    assert hasattr(domain::ArtificialField, "name")
    descriptor = None
    for klass in domain::ArtificialField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::formvariable_is_not_abstract():
    assert not inspect.isabstract(domain::FormVariable)


def test_domain::formvariable_constructor_exists():
    assert callable(domain::FormVariable.__init__)


def test_domain::formvariable_constructor_args():
    sig = inspect.signature(domain::FormVariable.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::formvariable_has_uid():
    assert hasattr(domain::FormVariable, "uid")
    descriptor = None
    for klass in domain::FormVariable.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::formvariable_has_name():
    assert hasattr(domain::FormVariable, "name")
    descriptor = None
    for klass in domain::FormVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_proxieslist_is_not_abstract():
    assert not inspect.isabstract(ProxiesList)


def test_proxieslist_constructor_exists():
    assert callable(ProxiesList.__init__)


def test_proxieslist_constructor_args():
    sig = inspect.signature(ProxiesList.__init__)
    params = list(sig.parameters.keys())



def test_domain::searchtrigger_is_not_abstract():
    assert not inspect.isabstract(domain::SearchTrigger)


def test_domain::searchtrigger_constructor_exists():
    assert callable(domain::SearchTrigger.__init__)


def test_domain::searchtrigger_constructor_args():
    sig = inspect.signature(domain::SearchTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::searchtrigger_has_uid():
    assert hasattr(domain::SearchTrigger, "uid")
    descriptor = None
    for klass in domain::SearchTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::deletetrigger_is_not_abstract():
    assert not inspect.isabstract(domain::DeleteTrigger)


def test_domain::deletetrigger_constructor_exists():
    assert callable(domain::DeleteTrigger.__init__)


def test_domain::deletetrigger_constructor_args():
    sig = inspect.signature(domain::DeleteTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::deletetrigger_has_uid():
    assert hasattr(domain::DeleteTrigger, "uid")
    descriptor = None
    for klass in domain::DeleteTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::inserttrigger_is_not_abstract():
    assert not inspect.isabstract(domain::InsertTrigger)


def test_domain::inserttrigger_constructor_exists():
    assert callable(domain::InsertTrigger.__init__)


def test_domain::inserttrigger_constructor_args():
    sig = inspect.signature(domain::InsertTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::inserttrigger_has_uid():
    assert hasattr(domain::InsertTrigger, "uid")
    descriptor = None
    for klass in domain::InsertTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::createtrigger_is_not_abstract():
    assert not inspect.isabstract(domain::CreateTrigger)


def test_domain::createtrigger_constructor_exists():
    assert callable(domain::CreateTrigger.__init__)


def test_domain::createtrigger_constructor_args():
    sig = inspect.signature(domain::CreateTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::createtrigger_has_uid():
    assert hasattr(domain::CreateTrigger, "uid")
    descriptor = None
    for klass in domain::CreateTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::proxieslist_is_not_abstract():
    assert not inspect.isabstract(domain::ProxiesList)


def test_domain::proxieslist_constructor_exists():
    assert callable(domain::ProxiesList.__init__)


def test_domain::proxieslist_constructor_args():
    sig = inspect.signature(domain::ProxiesList.__init__)
    params = list(sig.parameters.keys())



def test_domain::preupdatetrigger_is_not_abstract():
    assert not inspect.isabstract(domain::PREUpdateTrigger)


def test_domain::preupdatetrigger_constructor_exists():
    assert callable(domain::PREUpdateTrigger.__init__)


def test_domain::preupdatetrigger_constructor_args():
    sig = inspect.signature(domain::PREUpdateTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::preupdatetrigger_has_uid():
    assert hasattr(domain::PREUpdateTrigger, "uid")
    descriptor = None
    for klass in domain::PREUpdateTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::postcreatetrigger_is_not_abstract():
    assert not inspect.isabstract(domain::POSTCreateTrigger)


def test_domain::postcreatetrigger_constructor_exists():
    assert callable(domain::POSTCreateTrigger.__init__)


def test_domain::postcreatetrigger_constructor_args():
    sig = inspect.signature(domain::POSTCreateTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::postcreatetrigger_has_uid():
    assert hasattr(domain::POSTCreateTrigger, "uid")
    descriptor = None
    for klass in domain::POSTCreateTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::predeletetrigger_is_not_abstract():
    assert not inspect.isabstract(domain::PREDeleteTrigger)


def test_domain::predeletetrigger_constructor_exists():
    assert callable(domain::PREDeleteTrigger.__init__)


def test_domain::predeletetrigger_constructor_args():
    sig = inspect.signature(domain::PREDeleteTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::predeletetrigger_has_uid():
    assert hasattr(domain::PREDeleteTrigger, "uid")
    descriptor = None
    for klass in domain::PREDeleteTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::preinserttrigger_is_not_abstract():
    assert not inspect.isabstract(domain::PREInsertTrigger)


def test_domain::preinserttrigger_constructor_exists():
    assert callable(domain::PREInsertTrigger.__init__)


def test_domain::preinserttrigger_constructor_args():
    sig = inspect.signature(domain::PREInsertTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::preinserttrigger_has_uid():
    assert hasattr(domain::PREInsertTrigger, "uid")
    descriptor = None
    for klass in domain::PREInsertTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::postquerytrigger_is_not_abstract():
    assert not inspect.isabstract(domain::POSTQueryTrigger)


def test_domain::postquerytrigger_constructor_exists():
    assert callable(domain::POSTQueryTrigger.__init__)


def test_domain::postquerytrigger_constructor_args():
    sig = inspect.signature(domain::POSTQueryTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::postquerytrigger_has_uid():
    assert hasattr(domain::POSTQueryTrigger, "uid")
    descriptor = None
    for klass in domain::POSTQueryTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::prequerytrigger_is_not_abstract():
    assert not inspect.isabstract(domain::PREQueryTrigger)


def test_domain::prequerytrigger_constructor_exists():
    assert callable(domain::PREQueryTrigger.__init__)


def test_domain::prequerytrigger_constructor_args():
    sig = inspect.signature(domain::PREQueryTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::prequerytrigger_has_uid():
    assert hasattr(domain::PREQueryTrigger, "uid")
    descriptor = None
    for klass in domain::PREQueryTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::preformtrigger_is_not_abstract():
    assert not inspect.isabstract(domain::PREFormTrigger)


def test_domain::preformtrigger_constructor_exists():
    assert callable(domain::PREFormTrigger.__init__)


def test_domain::preformtrigger_constructor_args():
    sig = inspect.signature(domain::PREFormTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::preformtrigger_has_uid():
    assert hasattr(domain::PREFormTrigger, "uid")
    descriptor = None
    for klass in domain::PREFormTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_methodpointer_is_not_abstract():
    assert not inspect.isabstract(MethodPointer)


def test_methodpointer_constructor_exists():
    assert callable(MethodPointer.__init__)


def test_methodpointer_constructor_args():
    sig = inspect.signature(MethodPointer.__init__)
    params = list(sig.parameters.keys())



def test_domain::trigger_is_not_abstract():
    assert not inspect.isabstract(domain::Trigger)


def test_domain::trigger_constructor_exists():
    assert callable(domain::Trigger.__init__)


def test_domain::trigger_constructor_args():
    sig = inspect.signature(domain::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_domain::dependency_is_not_abstract():
    assert not inspect.isabstract(domain::Dependency)


def test_domain::dependency_constructor_exists():
    assert callable(domain::Dependency.__init__)


def test_domain::dependency_constructor_args():
    sig = inspect.signature(domain::Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::dependency_has_name():
    assert hasattr(domain::Dependency, "name")
    descriptor = None
    for klass in domain::Dependency.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::dependency_has_uid():
    assert hasattr(domain::Dependency, "uid")
    descriptor = None
    for klass in domain::Dependency.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::updatetrigger_is_not_abstract():
    assert not inspect.isabstract(domain::UpdateTrigger)


def test_domain::updatetrigger_constructor_exists():
    assert callable(domain::UpdateTrigger.__init__)


def test_domain::updatetrigger_constructor_args():
    sig = inspect.signature(domain::UpdateTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::updatetrigger_has_uid():
    assert hasattr(domain::UpdateTrigger, "uid")
    descriptor = None
    for klass in domain::UpdateTrigger.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::root_is_not_abstract():
    assert not inspect.isabstract(domain::Root)


def test_domain::root_constructor_exists():
    assert callable(domain::Root.__init__)


def test_domain::root_constructor_args():
    sig = inspect.signature(domain::Root.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::root_has_name():
    assert hasattr(domain::Root, "name")
    descriptor = None
    for klass in domain::Root.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domain::root_has_uid():
    assert hasattr(domain::Root, "uid")
    descriptor = None
    for klass in domain::Root.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_domain::tree_is_not_abstract():
    assert not inspect.isabstract(domain::Tree)


def test_domain::tree_constructor_exists():
    assert callable(domain::Tree.__init__)


def test_domain::tree_constructor_args():
    sig = inspect.signature(domain::Tree.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_domain::tree_has_label():
    assert hasattr(domain::Tree, "label")
    descriptor = None
    for klass in domain::Tree.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_domain::menu_is_not_abstract():
    assert not inspect.isabstract(domain::Menu)


def test_domain::menu_constructor_exists():
    assert callable(domain::Menu.__init__)


def test_domain::menu_constructor_args():
    sig = inspect.signature(domain::Menu.__init__)
    params = list(sig.parameters.keys())
    assert "fakeName" in params, "Missing parameter 'fakeName'"

def test_domain::menu_has_fakeName():
    assert hasattr(domain::Menu, "fakeName")
    descriptor = None
    for klass in domain::Menu.__mro__:
        if "fakeName" in klass.__dict__:
            descriptor = klass.__dict__["fakeName"]
            break
    assert isinstance(descriptor, property)



def test_domain::table_is_not_abstract():
    assert not inspect.isabstract(domain::Table)


def test_domain::table_constructor_exists():
    assert callable(domain::Table.__init__)


def test_domain::table_constructor_args():
    sig = inspect.signature(domain::Table.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "rowNumber" in params, "Missing parameter 'rowNumber'"

def test_domain::table_has_label():
    assert hasattr(domain::Table, "label")
    descriptor = None
    for klass in domain::Table.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_domain::table_has_rowNumber():
    assert hasattr(domain::Table, "rowNumber")
    descriptor = None
    for klass in domain::Table.__mro__:
        if "rowNumber" in klass.__dict__:
            descriptor = klass.__dict__["rowNumber"]
            break
    assert isinstance(descriptor, property)



def test_domain::column_is_not_abstract():
    assert not inspect.isabstract(domain::Column)


def test_domain::column_constructor_exists():
    assert callable(domain::Column.__init__)


def test_domain::column_constructor_args():
    sig = inspect.signature(domain::Column.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "uid" in params, "Missing parameter 'uid'"

def test_domain::column_has_label():
    assert hasattr(domain::Column, "label")
    descriptor = None
    for klass in domain::Column.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_domain::column_has_uid():
    assert hasattr(domain::Column, "uid")
    descriptor = None
    for klass in domain::Column.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_itemicon_is_not_abstract():
    assert not inspect.isabstract(ItemIcon)


def test_itemicon_constructor_exists():
    assert callable(ItemIcon.__init__)


def test_itemicon_constructor_args():
    sig = inspect.signature(ItemIcon.__init__)
    params = list(sig.parameters.keys())



def test_domain::menuitem_is_not_abstract():
    assert not inspect.isabstract(domain::MenuItem)


def test_domain::menuitem_constructor_exists():
    assert callable(domain::MenuItem.__init__)


def test_domain::menuitem_constructor_args():
    sig = inspect.signature(domain::MenuItem.__init__)
    params = list(sig.parameters.keys())



def test_domain::submenu_is_not_abstract():
    assert not inspect.isabstract(domain::SubMenu)


def test_domain::submenu_constructor_exists():
    assert callable(domain::SubMenu.__init__)


def test_domain::submenu_constructor_args():
    sig = inspect.signature(domain::SubMenu.__init__)
    params = list(sig.parameters.keys())



def test_domain::button_is_not_abstract():
    assert not inspect.isabstract(domain::Button)


def test_domain::button_constructor_exists():
    assert callable(domain::Button.__init__)


def test_domain::button_constructor_args():
    sig = inspect.signature(domain::Button.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_domain::button_has_label():
    assert hasattr(domain::Button, "label")
    descriptor = None
    for klass in domain::Button.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_domain::menufolder_is_not_abstract():
    assert not inspect.isabstract(domain::MenuFolder)


def test_domain::menufolder_constructor_exists():
    assert callable(domain::MenuFolder.__init__)


def test_domain::menufolder_constructor_args():
    sig = inspect.signature(domain::MenuFolder.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "extensionPoint" in params, "Missing parameter 'extensionPoint'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::menufolder_has_uid():
    assert hasattr(domain::MenuFolder, "uid")
    descriptor = None
    for klass in domain::MenuFolder.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::menufolder_has_extensionPoint():
    assert hasattr(domain::MenuFolder, "extensionPoint")
    descriptor = None
    for klass in domain::MenuFolder.__mro__:
        if "extensionPoint" in klass.__dict__:
            descriptor = klass.__dict__["extensionPoint"]
            break
    assert isinstance(descriptor, property)

def test_domain::menufolder_has_name():
    assert hasattr(domain::MenuFolder, "name")
    descriptor = None
    for klass in domain::MenuFolder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::relation_is_not_abstract():
    assert not inspect.isabstract(domain::Relation)


def test_domain::relation_constructor_exists():
    assert callable(domain::Relation.__init__)


def test_domain::relation_constructor_args():
    sig = inspect.signature(domain::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "isTree" in params, "Missing parameter 'isTree'"
    assert "name" in params, "Missing parameter 'name'"

def test_domain::relation_has_uid():
    assert hasattr(domain::Relation, "uid")
    descriptor = None
    for klass in domain::Relation.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_domain::relation_has_isTree():
    assert hasattr(domain::Relation, "isTree")
    descriptor = None
    for klass in domain::Relation.__mro__:
        if "isTree" in klass.__dict__:
            descriptor = klass.__dict__["isTree"]
            break
    assert isinstance(descriptor, property)

def test_domain::relation_has_name():
    assert hasattr(domain::Relation, "name")
    descriptor = None
    for klass in domain::Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain::image_is_not_abstract():
    assert not inspect.isabstract(domain::Image)


def test_domain::image_constructor_exists():
    assert callable(domain::Image.__init__)


def test_domain::image_constructor_args():
    sig = inspect.signature(domain::Image.__init__)
    params = list(sig.parameters.keys())



def test_optionselection_is_not_abstract():
    assert not inspect.isabstract(OptionSelection)


def test_optionselection_constructor_exists():
    assert callable(OptionSelection.__init__)


def test_optionselection_constructor_args():
    sig = inspect.signature(OptionSelection.__init__)
    params = list(sig.parameters.keys())



def test_domain::dropdownselection_is_not_abstract():
    assert not inspect.isabstract(domain::DropDownSelection)


def test_domain::dropdownselection_constructor_exists():
    assert callable(domain::DropDownSelection.__init__)


def test_domain::dropdownselection_constructor_args():
    sig = inspect.signature(domain::DropDownSelection.__init__)
    params = list(sig.parameters.keys())
    assert "initialOptionValue" in params, "Missing parameter 'initialOptionValue'"

def test_domain::dropdownselection_has_initialOptionValue():
    assert hasattr(domain::DropDownSelection, "initialOptionValue")
    descriptor = None
    for klass in domain::DropDownSelection.__mro__:
        if "initialOptionValue" in klass.__dict__:
            descriptor = klass.__dict__["initialOptionValue"]
            break
    assert isinstance(descriptor, property)



def test_domain::checkbox_is_not_abstract():
    assert not inspect.isabstract(domain::CheckBox)


def test_domain::checkbox_constructor_exists():
    assert callable(domain::CheckBox.__init__)


def test_domain::checkbox_constructor_args():
    sig = inspect.signature(domain::CheckBox.__init__)
    params = list(sig.parameters.keys())



def test_formatable_is_not_abstract():
    assert not inspect.isabstract(Formatable)


def test_formatable_constructor_exists():
    assert callable(Formatable.__init__)


def test_formatable_constructor_args():
    sig = inspect.signature(Formatable.__init__)
    params = list(sig.parameters.keys())



def test_domain::date_is_not_abstract():
    assert not inspect.isabstract(domain::Date)


def test_domain::date_constructor_exists():
    assert callable(domain::Date.__init__)


def test_domain::date_constructor_args():
    sig = inspect.signature(domain::Date.__init__)
    params = list(sig.parameters.keys())



def test_domain::inputtext_is_not_abstract():
    assert not inspect.isabstract(domain::InputText)


def test_domain::inputtext_constructor_exists():
    assert callable(domain::InputText.__init__)


def test_domain::inputtext_constructor_args():
    sig = inspect.signature(domain::InputText.__init__)
    params = list(sig.parameters.keys())



def test_domain::password_is_not_abstract():
    assert not inspect.isabstract(domain::Password)


def test_domain::password_constructor_exists():
    assert callable(domain::Password.__init__)


def test_domain::password_constructor_args():
    sig = inspect.signature(domain::Password.__init__)
    params = list(sig.parameters.keys())



def test_domain::outputtext_is_not_abstract():
    assert not inspect.isabstract(domain::OutputText)


def test_domain::outputtext_constructor_exists():
    assert callable(domain::OutputText.__init__)


def test_domain::outputtext_constructor_args():
    sig = inspect.signature(domain::OutputText.__init__)
    params = list(sig.parameters.keys())

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "Bottom",
        "Left",
        "Top",
        "Right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_platformlayers_exists():
    # Check that the Enumeration exists
    assert PlatformLayers is not None

def test_platformlayers_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PlatformLayers]
    expected_literals = [
        "ServiceLayer",
        "UILayer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PlatformLayers"

def test_comparator_exists():
    # Check that the Enumeration exists
    assert Comparator is not None

def test_comparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Comparator]
    expected_literals = [
        "GEQ",
        "GT",
        "LEQ",
        "LT",
        "NEQ",
        "EQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Comparator"

def test_relationtype_exists():
    # Check that the Enumeration exists
    assert RelationType is not None

def test_relationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationType]
    expected_literals = [
        "Many2Many",
        "One2One",
        "One2Many",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationType"

def test_order_exists():
    # Check that the Enumeration exists
    assert Order is not None

def test_order_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Order]
    expected_literals = [
        "ASC",
        "DESC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Order"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
MenuExtensionRef_strategy = st.builds(
    MenuExtensionRef,
)
ChildrenHolder_strategy = st.builds(
    ChildrenHolder,
)
SourcesPointer_strategy = st.builds(
    SourcesPointer,
)
domain::DataControl_strategy = st.builds(
    domain::DataControl,
    name=
        safe_text,
    uid=
        safe_text
)
Uielement_strategy = st.builds(
    Uielement,
)
domain::SourcesPointer_strategy = st.builds(
    domain::SourcesPointer,
)
domain::Formatable_strategy = st.builds(
    domain::Formatable,
    format=
        safe_text
)
domain::ItemIcon_strategy = st.builds(
    domain::ItemIcon,
)
domain::AreaRef_strategy = st.builds(
    domain::AreaRef,
    group=
        st.integers()
)
MenuHolder_strategy = st.builds(
    MenuHolder,
)
EnabledUIItem_strategy = st.builds(
    EnabledUIItem,
)
domain::EnabledUIItem_strategy = st.builds(
    domain::EnabledUIItem,
)
Context_strategy = st.builds(
    Context,
)
domain::FlexFields_strategy = st.builds(
    domain::FlexFields,
)
domain::NickNamed_strategy = st.builds(
    domain::NickNamed,
    nickname=
        safe_text
)
InputElement_strategy = st.builds(
    InputElement,
)
domain::OptionSelection_strategy = st.builds(
    domain::OptionSelection,
)
domain::StyleElement_strategy = st.builds(
    domain::StyleElement,
)
ContextParameters_strategy = st.builds(
    ContextParameters,
)
ContextValue_strategy = st.builds(
    ContextValue,
)
domain::StyleClass_strategy = st.builds(
    domain::StyleClass,
)
domain::ContextParameters_strategy = st.builds(
    domain::ContextParameters,
)
domain::ExpressionPart_strategy = st.builds(
    domain::ExpressionPart,
    expressionType=
        safe_text,
    uid=
        safe_text,
    order=
        st.integers()
)
domain::ContextValue_strategy = st.builds(
    domain::ContextValue,
    value=
        safe_text,
    uid=
        safe_text,
    constant=
        st.booleans()
)
domain::ContextParameter_strategy = st.builds(
    domain::ContextParameter,
    operation=
        safe_text,
    uid=
        safe_text
)
domain::ChildrenHolder_strategy = st.builds(
    domain::ChildrenHolder,
)
domain::InputElement_strategy = st.builds(
    domain::InputElement,
)
domain::LinkToMessage_strategy = st.builds(
    domain::LinkToMessage,
    uid=
        safe_text
)
domain::LinkToLabel_strategy = st.builds(
    domain::LinkToLabel,
    uid=
        safe_text
)
domain::Controls_strategy = st.builds(
    domain::Controls,
    uid=
        safe_text
)
Trigger_strategy = st.builds(
    Trigger,
)
domain::CanvasView_strategy = st.builds(
    domain::CanvasView,
    uid=
        safe_text
)
domain::ViewPortTrigger_strategy = st.builds(
    domain::ViewPortTrigger,
    uid=
        safe_text
)
ViewElement_strategy = st.builds(
    ViewElement,
)
Orderable_strategy = st.builds(
    Orderable,
)
domain::ViewPort_strategy = st.builds(
    domain::ViewPort,
    name=
        safe_text,
    uid=
        safe_text
)
domain::ViewArea_strategy = st.builds(
    domain::ViewArea,
    name=
        safe_text,
    uid=
        safe_text
)
domain::MenuView_strategy = st.builds(
    domain::MenuView,
    uid=
        safe_text
)
FlexFields_strategy = st.builds(
    FlexFields,
)
MultiLangLabel_strategy = st.builds(
    MultiLangLabel,
)
domain::Label_strategy = st.builds(
    domain::Label,
    label=
        safe_text
)
domain::MessageElement_strategy = st.builds(
    domain::MessageElement,
    label=
        safe_text
)
DefaultCavas_strategy = st.builds(
    DefaultCavas,
)
ViewPortHolder_strategy = st.builds(
    ViewPortHolder,
)
CanvasFrame_strategy = st.builds(
    CanvasFrame,
)
NickNamed_strategy = st.builds(
    NickNamed,
)
domain::DefaultCavas_strategy = st.builds(
    domain::DefaultCavas,
    defaultCanvas=
        st.booleans()
)
StyleElement_strategy = st.builds(
    StyleElement,
)
domain::Selection_strategy = st.builds(
    domain::Selection,
)
domain::Context_strategy = st.builds(
    domain::Context,
)
domain::MultiLangLabel_strategy = st.builds(
    domain::MultiLangLabel,
)
domain::Orderable_strategy = st.builds(
    domain::Orderable,
    order=
        st.integers()
)
domain::TabPagesInheritance_strategy = st.builds(
    domain::TabPagesInheritance,
    uid=
        safe_text
)
domain::ViewInheritance_strategy = st.builds(
    domain::ViewInheritance,
    uid=
        safe_text
)
domain::CanvasFrame_strategy = st.builds(
    domain::CanvasFrame,
    uid=
        safe_text,
    name=
        safe_text
)
domain::Views_strategy = st.builds(
    domain::Views,
    uid=
        safe_text
)
domain::FormDataControls_strategy = st.builds(
    domain::FormDataControls,
    uid=
        safe_text,
    name=
        safe_text
)
domain::FormView_strategy = st.builds(
    domain::FormView,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Form_strategy = st.builds(
    domain::Form,
    name=
        safe_text,
    uid=
        safe_text
)
domain::EnumAttribute_strategy = st.builds(
    domain::EnumAttribute,
    value=
        safe_text,
    name=
        safe_text,
    uid=
        safe_text
)
Secured_strategy = st.builds(
    Secured,
)
TypeElement_strategy = st.builds(
    TypeElement,
)
domain::Enumarator_strategy = st.builds(
    domain::Enumarator,
)
domain::Primitive_strategy = st.builds(
    domain::Primitive,
)
domain::Link_strategy = st.builds(
    domain::Link,
    uid=
        safe_text
)
RelationShip_strategy = st.builds(
    RelationShip,
)
domain::Generalization_strategy = st.builds(
    domain::Generalization,
)
domain::Assosiation_strategy = st.builds(
    domain::Assosiation,
    type=
        safe_text
)
domain::References_strategy = st.builds(
    domain::References,
)
domain::TypeElement_strategy = st.builds(
    domain::TypeElement,
    uid=
        safe_text,
    name=
        safe_text
)
domain::Package_strategy = st.builds(
    domain::Package,
    name=
        safe_text,
    uid=
        safe_text
)
domain::TypePointer_strategy = st.builds(
    domain::TypePointer,
    fakeTypeName=
        safe_text,
    fakePackageName=
        safe_text
)
domain::ArtifactRef_strategy = st.builds(
    domain::ArtifactRef,
    uid=
        safe_text
)
domain::QueryVariable_strategy = st.builds(
    domain::QueryVariable,
    value=
        safe_text,
    uid=
        safe_text
)
domain::KeyValuePair_strategy = st.builds(
    domain::KeyValuePair,
    key=
        safe_text,
    value=
        safe_text,
    uid=
        safe_text
)
domain::TypeDefinition_strategy = st.builds(
    domain::TypeDefinition,
    uid=
        safe_text
)
domain::Query_strategy = st.builds(
    domain::Query,
    uid=
        safe_text,
    name=
        safe_text
)
domain::MappingSpecifier_strategy = st.builds(
    domain::MappingSpecifier,
    uid=
        safe_text
)
ArtifactRef_strategy = st.builds(
    ArtifactRef,
)
domain::HashProperty_strategy = st.builds(
    domain::HashProperty,
    uid=
        safe_text,
    fakeName=
        safe_text
)
domain::Property_strategy = st.builds(
    domain::Property,
    fakeName=
        safe_text,
    uid=
        safe_text,
    value=
        safe_text
)
Component_strategy = st.builds(
    Component,
)
domain::JavaComponent_strategy = st.builds(
    domain::JavaComponent,
    version=
        safe_text,
    groupId=
        safe_text,
    artifactId=
        safe_text,
    basePackage=
        safe_text
)
UsingMappers_strategy = st.builds(
    UsingMappers,
)
domain::ModelMapper_strategy = st.builds(
    domain::ModelMapper,
    artifactExecutionString=
        safe_text,
    name=
        safe_text,
    artifactRoot=
        safe_text
)
domain::DeploymentStarStep_strategy = st.builds(
    domain::DeploymentStarStep,
    uid=
        safe_text,
    name=
        safe_text
)
domain::DeploymentComponent_strategy = st.builds(
    domain::DeploymentComponent,
    name=
        safe_text,
    uid=
        safe_text
)
domain::DeploymentComponents_strategy = st.builds(
    domain::DeploymentComponents,
    uid=
        safe_text
)
domain::ConfigExtension_strategy = st.builds(
    domain::ConfigExtension,
    uid=
        safe_text
)
domain::DeploymentSequence_strategy = st.builds(
    domain::DeploymentSequence,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Infrastructure_strategy = st.builds(
    domain::Infrastructure,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Configuration_strategy = st.builds(
    domain::Configuration,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Recipe_strategy = st.builds(
    domain::Recipe,
    name=
        safe_text,
    uid=
        safe_text
)
domain::UsingMappers_strategy = st.builds(
    domain::UsingMappers,
)
TypeMapper_strategy = st.builds(
    TypeMapper,
)
domain::JavaScriptMapper_strategy = st.builds(
    domain::JavaScriptMapper,
    libraryUrl=
        safe_text
)
domain::JavaMapper_strategy = st.builds(
    domain::JavaMapper,
    version=
        safe_text,
    artifactType=
        safe_text,
    mappedToPackageName=
        safe_text,
    libraryName=
        safe_text,
    groupId=
        safe_text,
    artifactId=
        safe_text,
    mappedToClassName=
        safe_text
)
Mapper_strategy = st.builds(
    Mapper,
)
domain::CSSMapper_strategy = st.builds(
    domain::CSSMapper,
    fakePackageName=
        safe_text,
    fakeTypeName=
        safe_text,
    libraryUrl=
        safe_text
)
domain::RoleMapper_strategy = st.builds(
    domain::RoleMapper,
    localRoleName=
        safe_text,
    globalRoleName=
        safe_text,
    fakeRoleName=
        safe_text
)
domain::Mapper_strategy = st.builds(
    domain::Mapper,
    uiLayer=
        st.booleans(),
    uid=
        safe_text,
    serviceLayer=
        st.booleans()
)
domain::StyleLibrary_strategy = st.builds(
    domain::StyleLibrary,
    uid=
        safe_text,
    name=
        safe_text
)
domain::Group_strategy = st.builds(
    domain::Group,
    name=
        safe_text,
    uid=
        safe_text
)
domain::StyleSet_strategy = st.builds(
    domain::StyleSet,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Translation_strategy = st.builds(
    domain::Translation,
    uid=
        safe_text,
    translation=
        safe_text
)
domain::Message_strategy = st.builds(
    domain::Message,
    uid=
        safe_text,
    name=
        safe_text
)
domain::LanguageRef_strategy = st.builds(
    domain::LanguageRef,
    uid=
        safe_text
)
Categorized_strategy = st.builds(
    Categorized,
)
domain::RelationShip_strategy = st.builds(
    domain::RelationShip,
    uid=
        safe_text
)
domain::PopupCanvas_strategy = st.builds(
    domain::PopupCanvas,
    modal=
        st.booleans()
)
domain::Type_strategy = st.builds(
    domain::Type,
)
domain::Window_strategy = st.builds(
    domain::Window,
)
domain::Canvas_strategy = st.builds(
    domain::Canvas,
)
domain::MenuDefinition_strategy = st.builds(
    domain::MenuDefinition,
    uid=
        safe_text,
    name=
        safe_text
)
domain::ViewElement_strategy = st.builds(
    domain::ViewElement,
)
domain::FlexField_strategy = st.builds(
    domain::FlexField,
)
domain::Uielement_strategy = st.builds(
    domain::Uielement,
    uid=
        safe_text
)
domain::TabPage_strategy = st.builds(
    domain::TabPage,
)
domain::TabCanvas_strategy = st.builds(
    domain::TabCanvas,
    orientation=
        safe_text
)
domain::Language_strategy = st.builds(
    domain::Language,
    lang=
        safe_text,
    code=
        safe_text,
    uid=
        safe_text,
    defaultLang=
        st.booleans()
)
domain::MessageLibrary_strategy = st.builds(
    domain::MessageLibrary,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Operation_strategy = st.builds(
    domain::Operation,
    uid=
        safe_text,
    name=
        safe_text
)
TypePointer_strategy = st.builds(
    TypePointer,
)
domain::FormParameter_strategy = st.builds(
    domain::FormParameter,
    name=
        safe_text,
    uid=
        safe_text
)
domain::TypeReference_strategy = st.builds(
    domain::TypeReference,
)
domain::Attribute_strategy = st.builds(
    domain::Attribute,
    uid=
        safe_text,
    pk=
        st.booleans(),
    name=
        safe_text
)
domain::TypeMapper_strategy = st.builds(
    domain::TypeMapper,
)
domain::ReturnValue_strategy = st.builds(
    domain::ReturnValue,
    uid=
        safe_text
)
domain::Parameter_strategy = st.builds(
    domain::Parameter,
    name=
        safe_text,
    order=
        st.integers(),
    uid=
        safe_text
)
domain::MethodPointer_strategy = st.builds(
    domain::MethodPointer,
    fakeMethod=
        safe_text
)
domain::Mappers_strategy = st.builds(
    domain::Mappers,
    uid=
        safe_text
)
domain::ApplicationMapper_strategy = st.builds(
    domain::ApplicationMapper,
    uid=
        safe_text,
    name=
        safe_text
)
domain::Recipes_strategy = st.builds(
    domain::Recipes,
    uid=
        safe_text
)
domain::ApplicationRecipe_strategy = st.builds(
    domain::ApplicationRecipe,
    uid=
        safe_text,
    name=
        safe_text
)
domain::UIPackage_strategy = st.builds(
    domain::UIPackage,
    uid=
        safe_text
)
domain::ApplicationUIPackage_strategy = st.builds(
    domain::ApplicationUIPackage,
    uid=
        safe_text,
    name=
        safe_text
)
domain::Styles_strategy = st.builds(
    domain::Styles,
    uid=
        safe_text
)
domain::Roles_strategy = st.builds(
    domain::Roles,
    uid=
        safe_text
)
domain::Messages_strategy = st.builds(
    domain::Messages,
    uid=
        safe_text
)
domain::ApplicationMessages_strategy = st.builds(
    domain::ApplicationMessages,
    name=
        safe_text,
    uid=
        safe_text
)
domain::ApplicationRole_strategy = st.builds(
    domain::ApplicationRole,
    name=
        safe_text,
    uid=
        safe_text
)
domain::ApplicationInfrastructureLayer_strategy = st.builds(
    domain::ApplicationInfrastructureLayer,
    name=
        safe_text,
    uid=
        safe_text
)
domain::StylesPackage_strategy = st.builds(
    domain::StylesPackage,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Option_strategy = st.builds(
    domain::Option,
    uid=
        safe_text,
    value=
        safe_text
)
domain::QueryParameter_strategy = st.builds(
    domain::QueryParameter,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Specifier_strategy = st.builds(
    domain::Specifier,
    uid=
        safe_text,
    name=
        safe_text
)
domain::ModelQuery_strategy = st.builds(
    domain::ModelQuery,
    uid=
        safe_text,
    query=
        safe_text,
    name=
        safe_text
)
domain::ConfigHash_strategy = st.builds(
    domain::ConfigHash,
    name=
        safe_text,
    uid=
        safe_text
)
domain::ConfigVariable_strategy = st.builds(
    domain::ConfigVariable,
    uid=
        safe_text,
    name=
        safe_text
)
domain::Artifact_strategy = st.builds(
    domain::Artifact,
    template=
        safe_text,
    description=
        safe_text,
    uid=
        safe_text,
    name=
        safe_text
)
DomainArtifact_strategy = st.builds(
    DomainArtifact,
)
domain::JPAService_strategy = st.builds(
    domain::JPAService,
)
domain::EJBService_strategy = st.builds(
    domain::EJBService,
)
domain::ContinuousIintegration_strategy = st.builds(
    domain::ContinuousIintegration,
)
domain::ORMEntity_strategy = st.builds(
    domain::ORMEntity,
)
domain::Artifacts_strategy = st.builds(
    domain::Artifacts,
    uid=
        safe_text
)
domain::Application_strategy = st.builds(
    domain::Application,
    uid=
        safe_text
)
domain::DomainArtifact_strategy = st.builds(
    domain::DomainArtifact,
    name=
        safe_text,
    uid=
        safe_text
)
HTMLLayerHolder_strategy = st.builds(
    HTMLLayerHolder,
)
domain::ApplicationStyle_strategy = st.builds(
    domain::ApplicationStyle,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Types_strategy = st.builds(
    domain::Types,
    uid=
        safe_text,
    name=
        safe_text
)
domain::Ingredient_strategy = st.builds(
    domain::Ingredient,
    uid=
        safe_text,
    layer=
        safe_text,
    name=
        safe_text
)
domain::ApplicationMappers_strategy = st.builds(
    domain::ApplicationMappers,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Component_strategy = st.builds(
    domain::Component,
    uid=
        safe_text,
    name=
        safe_text,
    componentRoot=
        safe_text
)
domain::ApplicationRecipes_strategy = st.builds(
    domain::ApplicationRecipes,
    uid=
        safe_text,
    name=
        safe_text
)
domain::ViewPortHolder_strategy = st.builds(
    domain::ViewPortHolder,
)
domain::LayerHolder_strategy = st.builds(
    domain::LayerHolder,
)
domain::ApplicationUILayer_strategy = st.builds(
    domain::ApplicationUILayer,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Role_strategy = st.builds(
    domain::Role,
    name=
        safe_text,
    uid=
        safe_text
)
domain::DomainApplication_strategy = st.builds(
    domain::DomainApplication,
    uid=
        safe_text,
    name=
        safe_text
)
domain::GrantAccess_strategy = st.builds(
    domain::GrantAccess,
    uid=
        safe_text
)
domain::Secured_strategy = st.builds(
    domain::Secured,
)
domain::GenerationHint_strategy = st.builds(
    domain::GenerationHint,
    name=
        safe_text,
    uid=
        safe_text,
    applyedClass=
        safe_text
)
domain::Classifier_strategy = st.builds(
    domain::Classifier,
    details=
        safe_text,
    uid=
        safe_text
)
domain::Categorized_strategy = st.builds(
    domain::Categorized,
)
domain::HTMLLayerHolder_strategy = st.builds(
    domain::HTMLLayerHolder,
    columns=
        st.integers()
)
domain::EObject_strategy = st.builds(
    domain::EObject,
)
domain::DomainApplications_strategy = st.builds(
    domain::DomainApplications,
    uid=
        safe_text,
    name=
        safe_text
)
domain::DomainTypes_strategy = st.builds(
    domain::DomainTypes,
    name=
        safe_text,
    uid=
        safe_text
)
domain::DomainArtifacts_strategy = st.builds(
    domain::DomainArtifacts,
    uid=
        safe_text,
    name=
        safe_text
)
domain::Domain_strategy = st.builds(
    domain::Domain,
    uid=
        safe_text
)
domain::TypesRepository_strategy = st.builds(
    domain::TypesRepository,
    uid=
        safe_text
)
MenuElement_strategy = st.builds(
    MenuElement,
)
domain::MenuSeparator_strategy = st.builds(
    domain::MenuSeparator,
)
domain::MenuExtensionPoint_strategy = st.builds(
    domain::MenuExtensionPoint,
)
domain::MenuElement_strategy = st.builds(
    domain::MenuElement,
    uid=
        safe_text,
    name=
        safe_text
)
domain::MenuExtensionRef_strategy = st.builds(
    domain::MenuExtensionRef,
)
domain::MenuHolder_strategy = st.builds(
    domain::MenuHolder,
)
domain::InfrastructureComponent_strategy = st.builds(
    domain::InfrastructureComponent,
    name=
        safe_text,
    uid=
        safe_text
)
domain::InfrastructureLayer_strategy = st.builds(
    domain::InfrastructureLayer,
    uid=
        safe_text,
    name=
        safe_text
)
domain::Subsystem_strategy = st.builds(
    domain::Subsystem,
    uid=
        safe_text,
    name=
        safe_text
)
InfrastructureComponent_strategy = st.builds(
    InfrastructureComponent,
)
domain::Hub_strategy = st.builds(
    domain::Hub,
)
domain::ServerClaster_strategy = st.builds(
    domain::ServerClaster,
)
domain::Router_strategy = st.builds(
    domain::Router,
)
domain::Storage_strategy = st.builds(
    domain::Storage,
)
domain::Server_strategy = st.builds(
    domain::Server,
)
domain::EnterpriseInfrastructure_strategy = st.builds(
    domain::EnterpriseInfrastructure,
    uid=
        safe_text
)
domain::InfrastructureConnection_strategy = st.builds(
    domain::InfrastructureConnection,
    uid=
        safe_text
)
domain::Datacenter_strategy = st.builds(
    domain::Datacenter,
    uid=
        safe_text,
    name=
        safe_text
)
domain::OrderBy_strategy = st.builds(
    domain::OrderBy,
    uid=
        safe_text,
    order=
        safe_text
)
domain::Orders_strategy = st.builds(
    domain::Orders,
    uid=
        safe_text
)
domain::ArtificialField_strategy = st.builds(
    domain::ArtificialField,
    uid=
        safe_text,
    name=
        safe_text
)
domain::FormVariable_strategy = st.builds(
    domain::FormVariable,
    uid=
        safe_text,
    name=
        safe_text
)
ProxiesList_strategy = st.builds(
    ProxiesList,
)
domain::SearchTrigger_strategy = st.builds(
    domain::SearchTrigger,
    uid=
        safe_text
)
domain::DeleteTrigger_strategy = st.builds(
    domain::DeleteTrigger,
    uid=
        safe_text
)
domain::InsertTrigger_strategy = st.builds(
    domain::InsertTrigger,
    uid=
        safe_text
)
domain::CreateTrigger_strategy = st.builds(
    domain::CreateTrigger,
    uid=
        safe_text
)
domain::ProxiesList_strategy = st.builds(
    domain::ProxiesList,
)
domain::PREUpdateTrigger_strategy = st.builds(
    domain::PREUpdateTrigger,
    uid=
        safe_text
)
domain::POSTCreateTrigger_strategy = st.builds(
    domain::POSTCreateTrigger,
    uid=
        safe_text
)
domain::PREDeleteTrigger_strategy = st.builds(
    domain::PREDeleteTrigger,
    uid=
        safe_text
)
domain::PREInsertTrigger_strategy = st.builds(
    domain::PREInsertTrigger,
    uid=
        safe_text
)
domain::POSTQueryTrigger_strategy = st.builds(
    domain::POSTQueryTrigger,
    uid=
        safe_text
)
domain::PREQueryTrigger_strategy = st.builds(
    domain::PREQueryTrigger,
    uid=
        safe_text
)
domain::PREFormTrigger_strategy = st.builds(
    domain::PREFormTrigger,
    uid=
        safe_text
)
MethodPointer_strategy = st.builds(
    MethodPointer,
)
domain::Trigger_strategy = st.builds(
    domain::Trigger,
)
domain::Dependency_strategy = st.builds(
    domain::Dependency,
    name=
        safe_text,
    uid=
        safe_text
)
domain::UpdateTrigger_strategy = st.builds(
    domain::UpdateTrigger,
    uid=
        safe_text
)
domain::Root_strategy = st.builds(
    domain::Root,
    name=
        safe_text,
    uid=
        safe_text
)
domain::Tree_strategy = st.builds(
    domain::Tree,
    label=
        safe_text
)
domain::Menu_strategy = st.builds(
    domain::Menu,
    fakeName=
        safe_text
)
domain::Table_strategy = st.builds(
    domain::Table,
    label=
        safe_text,
    rowNumber=
        st.integers()
)
domain::Column_strategy = st.builds(
    domain::Column,
    label=
        safe_text,
    uid=
        safe_text
)
ItemIcon_strategy = st.builds(
    ItemIcon,
)
domain::MenuItem_strategy = st.builds(
    domain::MenuItem,
)
domain::SubMenu_strategy = st.builds(
    domain::SubMenu,
)
domain::Button_strategy = st.builds(
    domain::Button,
    label=
        safe_text
)
domain::MenuFolder_strategy = st.builds(
    domain::MenuFolder,
    uid=
        safe_text,
    extensionPoint=
        st.booleans(),
    name=
        safe_text
)
domain::Relation_strategy = st.builds(
    domain::Relation,
    uid=
        safe_text,
    isTree=
        st.booleans(),
    name=
        safe_text
)
domain::Image_strategy = st.builds(
    domain::Image,
)
OptionSelection_strategy = st.builds(
    OptionSelection,
)
domain::DropDownSelection_strategy = st.builds(
    domain::DropDownSelection,
    initialOptionValue=
        safe_text
)
domain::CheckBox_strategy = st.builds(
    domain::CheckBox,
)
Formatable_strategy = st.builds(
    Formatable,
)
domain::Date_strategy = st.builds(
    domain::Date,
)
domain::InputText_strategy = st.builds(
    domain::InputText,
)
domain::Password_strategy = st.builds(
    domain::Password,
)
domain::OutputText_strategy = st.builds(
    domain::OutputText,
)

@given(instance=MenuExtensionRef_strategy)
@settings(max_examples=50)
def test_menuextensionref_instantiation(instance):
    assert isinstance(instance, MenuExtensionRef)

@given(instance=ChildrenHolder_strategy)
@settings(max_examples=50)
def test_childrenholder_instantiation(instance):
    assert isinstance(instance, ChildrenHolder)

@given(instance=SourcesPointer_strategy)
@settings(max_examples=50)
def test_sourcespointer_instantiation(instance):
    assert isinstance(instance, SourcesPointer)

@given(instance=domain::DataControl_strategy)
@settings(max_examples=50)
def test_domain::datacontrol_instantiation(instance):
    assert isinstance(instance, domain::DataControl)

@given(instance=domain::DataControl_strategy)
def test_domain::datacontrol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::DataControl_strategy)
def test_domain::datacontrol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::DataControl_strategy)
def test_domain::datacontrol_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DataControl_strategy)
def test_domain::datacontrol_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=Uielement_strategy)
@settings(max_examples=50)
def test_uielement_instantiation(instance):
    assert isinstance(instance, Uielement)

@given(instance=domain::SourcesPointer_strategy)
@settings(max_examples=50)
def test_domain::sourcespointer_instantiation(instance):
    assert isinstance(instance, domain::SourcesPointer)

@given(instance=domain::Formatable_strategy)
@settings(max_examples=50)
def test_domain::formatable_instantiation(instance):
    assert isinstance(instance, domain::Formatable)

@given(instance=domain::Formatable_strategy)
def test_domain::formatable_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=domain::Formatable_strategy)
def test_domain::formatable_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=domain::ItemIcon_strategy)
@settings(max_examples=50)
def test_domain::itemicon_instantiation(instance):
    assert isinstance(instance, domain::ItemIcon)

@given(instance=domain::AreaRef_strategy)
@settings(max_examples=50)
def test_domain::arearef_instantiation(instance):
    assert isinstance(instance, domain::AreaRef)

@given(instance=domain::AreaRef_strategy)
def test_domain::arearef_group_type(instance):
    assert isinstance(instance.group, int)


@given(instance=domain::AreaRef_strategy)
def test_domain::arearef_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=MenuHolder_strategy)
@settings(max_examples=50)
def test_menuholder_instantiation(instance):
    assert isinstance(instance, MenuHolder)

@given(instance=EnabledUIItem_strategy)
@settings(max_examples=50)
def test_enableduiitem_instantiation(instance):
    assert isinstance(instance, EnabledUIItem)

@given(instance=domain::EnabledUIItem_strategy)
@settings(max_examples=50)
def test_domain::enableduiitem_instantiation(instance):
    assert isinstance(instance, domain::EnabledUIItem)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=domain::FlexFields_strategy)
@settings(max_examples=50)
def test_domain::flexfields_instantiation(instance):
    assert isinstance(instance, domain::FlexFields)

@given(instance=domain::NickNamed_strategy)
@settings(max_examples=50)
def test_domain::nicknamed_instantiation(instance):
    assert isinstance(instance, domain::NickNamed)

@given(instance=domain::NickNamed_strategy)
def test_domain::nicknamed_nickname_type(instance):
    assert isinstance(instance.nickname, str)


@given(instance=domain::NickNamed_strategy)
def test_domain::nicknamed_nickname_setter(instance):
    original = instance.nickname
    instance.nickname = original
    assert instance.nickname == original

@given(instance=InputElement_strategy)
@settings(max_examples=50)
def test_inputelement_instantiation(instance):
    assert isinstance(instance, InputElement)

@given(instance=domain::OptionSelection_strategy)
@settings(max_examples=50)
def test_domain::optionselection_instantiation(instance):
    assert isinstance(instance, domain::OptionSelection)

@given(instance=domain::StyleElement_strategy)
@settings(max_examples=50)
def test_domain::styleelement_instantiation(instance):
    assert isinstance(instance, domain::StyleElement)

@given(instance=ContextParameters_strategy)
@settings(max_examples=50)
def test_contextparameters_instantiation(instance):
    assert isinstance(instance, ContextParameters)

@given(instance=ContextValue_strategy)
@settings(max_examples=50)
def test_contextvalue_instantiation(instance):
    assert isinstance(instance, ContextValue)

@given(instance=domain::StyleClass_strategy)
@settings(max_examples=50)
def test_domain::styleclass_instantiation(instance):
    assert isinstance(instance, domain::StyleClass)

@given(instance=domain::ContextParameters_strategy)
@settings(max_examples=50)
def test_domain::contextparameters_instantiation(instance):
    assert isinstance(instance, domain::ContextParameters)

@given(instance=domain::ExpressionPart_strategy)
@settings(max_examples=50)
def test_domain::expressionpart_instantiation(instance):
    assert isinstance(instance, domain::ExpressionPart)

@given(instance=domain::ExpressionPart_strategy)
def test_domain::expressionpart_expressionType_type(instance):
    assert isinstance(instance.expressionType, str)


@given(instance=domain::ExpressionPart_strategy)
def test_domain::expressionpart_expressionType_setter(instance):
    original = instance.expressionType
    instance.expressionType = original
    assert instance.expressionType == original

@given(instance=domain::ExpressionPart_strategy)
def test_domain::expressionpart_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ExpressionPart_strategy)
def test_domain::expressionpart_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ExpressionPart_strategy)
def test_domain::expressionpart_order_type(instance):
    assert isinstance(instance.order, int)


@given(instance=domain::ExpressionPart_strategy)
def test_domain::expressionpart_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=domain::ContextValue_strategy)
@settings(max_examples=50)
def test_domain::contextvalue_instantiation(instance):
    assert isinstance(instance, domain::ContextValue)

@given(instance=domain::ContextValue_strategy)
def test_domain::contextvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=domain::ContextValue_strategy)
def test_domain::contextvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=domain::ContextValue_strategy)
def test_domain::contextvalue_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ContextValue_strategy)
def test_domain::contextvalue_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ContextValue_strategy)
def test_domain::contextvalue_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=domain::ContextValue_strategy)
def test_domain::contextvalue_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=domain::ContextParameter_strategy)
@settings(max_examples=50)
def test_domain::contextparameter_instantiation(instance):
    assert isinstance(instance, domain::ContextParameter)

@given(instance=domain::ContextParameter_strategy)
def test_domain::contextparameter_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=domain::ContextParameter_strategy)
def test_domain::contextparameter_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=domain::ContextParameter_strategy)
def test_domain::contextparameter_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ContextParameter_strategy)
def test_domain::contextparameter_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ChildrenHolder_strategy)
@settings(max_examples=50)
def test_domain::childrenholder_instantiation(instance):
    assert isinstance(instance, domain::ChildrenHolder)

@given(instance=domain::InputElement_strategy)
@settings(max_examples=50)
def test_domain::inputelement_instantiation(instance):
    assert isinstance(instance, domain::InputElement)

@given(instance=domain::LinkToMessage_strategy)
@settings(max_examples=50)
def test_domain::linktomessage_instantiation(instance):
    assert isinstance(instance, domain::LinkToMessage)

@given(instance=domain::LinkToMessage_strategy)
def test_domain::linktomessage_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::LinkToMessage_strategy)
def test_domain::linktomessage_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::LinkToLabel_strategy)
@settings(max_examples=50)
def test_domain::linktolabel_instantiation(instance):
    assert isinstance(instance, domain::LinkToLabel)

@given(instance=domain::LinkToLabel_strategy)
def test_domain::linktolabel_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::LinkToLabel_strategy)
def test_domain::linktolabel_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Controls_strategy)
@settings(max_examples=50)
def test_domain::controls_instantiation(instance):
    assert isinstance(instance, domain::Controls)

@given(instance=domain::Controls_strategy)
def test_domain::controls_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Controls_strategy)
def test_domain::controls_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=domain::CanvasView_strategy)
@settings(max_examples=50)
def test_domain::canvasview_instantiation(instance):
    assert isinstance(instance, domain::CanvasView)

@given(instance=domain::CanvasView_strategy)
def test_domain::canvasview_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::CanvasView_strategy)
def test_domain::canvasview_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ViewPortTrigger_strategy)
@settings(max_examples=50)
def test_domain::viewporttrigger_instantiation(instance):
    assert isinstance(instance, domain::ViewPortTrigger)

@given(instance=domain::ViewPortTrigger_strategy)
def test_domain::viewporttrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ViewPortTrigger_strategy)
def test_domain::viewporttrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=ViewElement_strategy)
@settings(max_examples=50)
def test_viewelement_instantiation(instance):
    assert isinstance(instance, ViewElement)

@given(instance=Orderable_strategy)
@settings(max_examples=50)
def test_orderable_instantiation(instance):
    assert isinstance(instance, Orderable)

@given(instance=domain::ViewPort_strategy)
@settings(max_examples=50)
def test_domain::viewport_instantiation(instance):
    assert isinstance(instance, domain::ViewPort)

@given(instance=domain::ViewPort_strategy)
def test_domain::viewport_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ViewPort_strategy)
def test_domain::viewport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ViewPort_strategy)
def test_domain::viewport_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ViewPort_strategy)
def test_domain::viewport_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ViewArea_strategy)
@settings(max_examples=50)
def test_domain::viewarea_instantiation(instance):
    assert isinstance(instance, domain::ViewArea)

@given(instance=domain::ViewArea_strategy)
def test_domain::viewarea_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ViewArea_strategy)
def test_domain::viewarea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ViewArea_strategy)
def test_domain::viewarea_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ViewArea_strategy)
def test_domain::viewarea_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::MenuView_strategy)
@settings(max_examples=50)
def test_domain::menuview_instantiation(instance):
    assert isinstance(instance, domain::MenuView)

@given(instance=domain::MenuView_strategy)
def test_domain::menuview_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::MenuView_strategy)
def test_domain::menuview_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=FlexFields_strategy)
@settings(max_examples=50)
def test_flexfields_instantiation(instance):
    assert isinstance(instance, FlexFields)

@given(instance=MultiLangLabel_strategy)
@settings(max_examples=50)
def test_multilanglabel_instantiation(instance):
    assert isinstance(instance, MultiLangLabel)

@given(instance=domain::Label_strategy)
@settings(max_examples=50)
def test_domain::label_instantiation(instance):
    assert isinstance(instance, domain::Label)

@given(instance=domain::Label_strategy)
def test_domain::label_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=domain::Label_strategy)
def test_domain::label_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=domain::MessageElement_strategy)
@settings(max_examples=50)
def test_domain::messageelement_instantiation(instance):
    assert isinstance(instance, domain::MessageElement)

@given(instance=domain::MessageElement_strategy)
def test_domain::messageelement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=domain::MessageElement_strategy)
def test_domain::messageelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=DefaultCavas_strategy)
@settings(max_examples=50)
def test_defaultcavas_instantiation(instance):
    assert isinstance(instance, DefaultCavas)

@given(instance=ViewPortHolder_strategy)
@settings(max_examples=50)
def test_viewportholder_instantiation(instance):
    assert isinstance(instance, ViewPortHolder)

@given(instance=CanvasFrame_strategy)
@settings(max_examples=50)
def test_canvasframe_instantiation(instance):
    assert isinstance(instance, CanvasFrame)

@given(instance=NickNamed_strategy)
@settings(max_examples=50)
def test_nicknamed_instantiation(instance):
    assert isinstance(instance, NickNamed)

@given(instance=domain::DefaultCavas_strategy)
@settings(max_examples=50)
def test_domain::defaultcavas_instantiation(instance):
    assert isinstance(instance, domain::DefaultCavas)

@given(instance=domain::DefaultCavas_strategy)
def test_domain::defaultcavas_defaultCanvas_type(instance):
    assert isinstance(instance.defaultCanvas, bool)


@given(instance=domain::DefaultCavas_strategy)
def test_domain::defaultcavas_defaultCanvas_setter(instance):
    original = instance.defaultCanvas
    instance.defaultCanvas = original
    assert instance.defaultCanvas == original

@given(instance=StyleElement_strategy)
@settings(max_examples=50)
def test_styleelement_instantiation(instance):
    assert isinstance(instance, StyleElement)

@given(instance=domain::Selection_strategy)
@settings(max_examples=50)
def test_domain::selection_instantiation(instance):
    assert isinstance(instance, domain::Selection)

@given(instance=domain::Context_strategy)
@settings(max_examples=50)
def test_domain::context_instantiation(instance):
    assert isinstance(instance, domain::Context)

@given(instance=domain::MultiLangLabel_strategy)
@settings(max_examples=50)
def test_domain::multilanglabel_instantiation(instance):
    assert isinstance(instance, domain::MultiLangLabel)

@given(instance=domain::Orderable_strategy)
@settings(max_examples=50)
def test_domain::orderable_instantiation(instance):
    assert isinstance(instance, domain::Orderable)

@given(instance=domain::Orderable_strategy)
def test_domain::orderable_order_type(instance):
    assert isinstance(instance.order, int)


@given(instance=domain::Orderable_strategy)
def test_domain::orderable_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=domain::TabPagesInheritance_strategy)
@settings(max_examples=50)
def test_domain::tabpagesinheritance_instantiation(instance):
    assert isinstance(instance, domain::TabPagesInheritance)

@given(instance=domain::TabPagesInheritance_strategy)
def test_domain::tabpagesinheritance_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::TabPagesInheritance_strategy)
def test_domain::tabpagesinheritance_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ViewInheritance_strategy)
@settings(max_examples=50)
def test_domain::viewinheritance_instantiation(instance):
    assert isinstance(instance, domain::ViewInheritance)

@given(instance=domain::ViewInheritance_strategy)
def test_domain::viewinheritance_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ViewInheritance_strategy)
def test_domain::viewinheritance_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::CanvasFrame_strategy)
@settings(max_examples=50)
def test_domain::canvasframe_instantiation(instance):
    assert isinstance(instance, domain::CanvasFrame)

@given(instance=domain::CanvasFrame_strategy)
def test_domain::canvasframe_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::CanvasFrame_strategy)
def test_domain::canvasframe_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::CanvasFrame_strategy)
def test_domain::canvasframe_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::CanvasFrame_strategy)
def test_domain::canvasframe_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Views_strategy)
@settings(max_examples=50)
def test_domain::views_instantiation(instance):
    assert isinstance(instance, domain::Views)

@given(instance=domain::Views_strategy)
def test_domain::views_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Views_strategy)
def test_domain::views_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::FormDataControls_strategy)
@settings(max_examples=50)
def test_domain::formdatacontrols_instantiation(instance):
    assert isinstance(instance, domain::FormDataControls)

@given(instance=domain::FormDataControls_strategy)
def test_domain::formdatacontrols_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::FormDataControls_strategy)
def test_domain::formdatacontrols_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::FormDataControls_strategy)
def test_domain::formdatacontrols_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::FormDataControls_strategy)
def test_domain::formdatacontrols_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::FormView_strategy)
@settings(max_examples=50)
def test_domain::formview_instantiation(instance):
    assert isinstance(instance, domain::FormView)

@given(instance=domain::FormView_strategy)
def test_domain::formview_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::FormView_strategy)
def test_domain::formview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::FormView_strategy)
def test_domain::formview_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::FormView_strategy)
def test_domain::formview_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Form_strategy)
@settings(max_examples=50)
def test_domain::form_instantiation(instance):
    assert isinstance(instance, domain::Form)

@given(instance=domain::Form_strategy)
def test_domain::form_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Form_strategy)
def test_domain::form_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Form_strategy)
def test_domain::form_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Form_strategy)
def test_domain::form_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::EnumAttribute_strategy)
@settings(max_examples=50)
def test_domain::enumattribute_instantiation(instance):
    assert isinstance(instance, domain::EnumAttribute)

@given(instance=domain::EnumAttribute_strategy)
def test_domain::enumattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=domain::EnumAttribute_strategy)
def test_domain::enumattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=domain::EnumAttribute_strategy)
def test_domain::enumattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::EnumAttribute_strategy)
def test_domain::enumattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::EnumAttribute_strategy)
def test_domain::enumattribute_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::EnumAttribute_strategy)
def test_domain::enumattribute_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=Secured_strategy)
@settings(max_examples=50)
def test_secured_instantiation(instance):
    assert isinstance(instance, Secured)

@given(instance=TypeElement_strategy)
@settings(max_examples=50)
def test_typeelement_instantiation(instance):
    assert isinstance(instance, TypeElement)

@given(instance=domain::Enumarator_strategy)
@settings(max_examples=50)
def test_domain::enumarator_instantiation(instance):
    assert isinstance(instance, domain::Enumarator)

@given(instance=domain::Primitive_strategy)
@settings(max_examples=50)
def test_domain::primitive_instantiation(instance):
    assert isinstance(instance, domain::Primitive)

@given(instance=domain::Link_strategy)
@settings(max_examples=50)
def test_domain::link_instantiation(instance):
    assert isinstance(instance, domain::Link)

@given(instance=domain::Link_strategy)
def test_domain::link_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Link_strategy)
def test_domain::link_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=RelationShip_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, RelationShip)

@given(instance=domain::Generalization_strategy)
@settings(max_examples=50)
def test_domain::generalization_instantiation(instance):
    assert isinstance(instance, domain::Generalization)

@given(instance=domain::Assosiation_strategy)
@settings(max_examples=50)
def test_domain::assosiation_instantiation(instance):
    assert isinstance(instance, domain::Assosiation)

@given(instance=domain::Assosiation_strategy)
def test_domain::assosiation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=domain::Assosiation_strategy)
def test_domain::assosiation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=domain::References_strategy)
@settings(max_examples=50)
def test_domain::references_instantiation(instance):
    assert isinstance(instance, domain::References)

@given(instance=domain::TypeElement_strategy)
@settings(max_examples=50)
def test_domain::typeelement_instantiation(instance):
    assert isinstance(instance, domain::TypeElement)

@given(instance=domain::TypeElement_strategy)
def test_domain::typeelement_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::TypeElement_strategy)
def test_domain::typeelement_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::TypeElement_strategy)
def test_domain::typeelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::TypeElement_strategy)
def test_domain::typeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Package_strategy)
@settings(max_examples=50)
def test_domain::package_instantiation(instance):
    assert isinstance(instance, domain::Package)

@given(instance=domain::Package_strategy)
def test_domain::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Package_strategy)
def test_domain::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Package_strategy)
def test_domain::package_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Package_strategy)
def test_domain::package_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::TypePointer_strategy)
@settings(max_examples=50)
def test_domain::typepointer_instantiation(instance):
    assert isinstance(instance, domain::TypePointer)

@given(instance=domain::TypePointer_strategy)
def test_domain::typepointer_fakeTypeName_type(instance):
    assert isinstance(instance.fakeTypeName, str)


@given(instance=domain::TypePointer_strategy)
def test_domain::typepointer_fakeTypeName_setter(instance):
    original = instance.fakeTypeName
    instance.fakeTypeName = original
    assert instance.fakeTypeName == original

@given(instance=domain::TypePointer_strategy)
def test_domain::typepointer_fakePackageName_type(instance):
    assert isinstance(instance.fakePackageName, str)


@given(instance=domain::TypePointer_strategy)
def test_domain::typepointer_fakePackageName_setter(instance):
    original = instance.fakePackageName
    instance.fakePackageName = original
    assert instance.fakePackageName == original

@given(instance=domain::ArtifactRef_strategy)
@settings(max_examples=50)
def test_domain::artifactref_instantiation(instance):
    assert isinstance(instance, domain::ArtifactRef)

@given(instance=domain::ArtifactRef_strategy)
def test_domain::artifactref_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ArtifactRef_strategy)
def test_domain::artifactref_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::QueryVariable_strategy)
@settings(max_examples=50)
def test_domain::queryvariable_instantiation(instance):
    assert isinstance(instance, domain::QueryVariable)

@given(instance=domain::QueryVariable_strategy)
def test_domain::queryvariable_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=domain::QueryVariable_strategy)
def test_domain::queryvariable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=domain::QueryVariable_strategy)
def test_domain::queryvariable_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::QueryVariable_strategy)
def test_domain::queryvariable_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::KeyValuePair_strategy)
@settings(max_examples=50)
def test_domain::keyvaluepair_instantiation(instance):
    assert isinstance(instance, domain::KeyValuePair)

@given(instance=domain::KeyValuePair_strategy)
def test_domain::keyvaluepair_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=domain::KeyValuePair_strategy)
def test_domain::keyvaluepair_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=domain::KeyValuePair_strategy)
def test_domain::keyvaluepair_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=domain::KeyValuePair_strategy)
def test_domain::keyvaluepair_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=domain::KeyValuePair_strategy)
def test_domain::keyvaluepair_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::KeyValuePair_strategy)
def test_domain::keyvaluepair_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::TypeDefinition_strategy)
@settings(max_examples=50)
def test_domain::typedefinition_instantiation(instance):
    assert isinstance(instance, domain::TypeDefinition)

@given(instance=domain::TypeDefinition_strategy)
def test_domain::typedefinition_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::TypeDefinition_strategy)
def test_domain::typedefinition_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Query_strategy)
@settings(max_examples=50)
def test_domain::query_instantiation(instance):
    assert isinstance(instance, domain::Query)

@given(instance=domain::Query_strategy)
def test_domain::query_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Query_strategy)
def test_domain::query_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Query_strategy)
def test_domain::query_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Query_strategy)
def test_domain::query_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::MappingSpecifier_strategy)
@settings(max_examples=50)
def test_domain::mappingspecifier_instantiation(instance):
    assert isinstance(instance, domain::MappingSpecifier)

@given(instance=domain::MappingSpecifier_strategy)
def test_domain::mappingspecifier_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::MappingSpecifier_strategy)
def test_domain::mappingspecifier_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=ArtifactRef_strategy)
@settings(max_examples=50)
def test_artifactref_instantiation(instance):
    assert isinstance(instance, ArtifactRef)

@given(instance=domain::HashProperty_strategy)
@settings(max_examples=50)
def test_domain::hashproperty_instantiation(instance):
    assert isinstance(instance, domain::HashProperty)

@given(instance=domain::HashProperty_strategy)
def test_domain::hashproperty_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::HashProperty_strategy)
def test_domain::hashproperty_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::HashProperty_strategy)
def test_domain::hashproperty_fakeName_type(instance):
    assert isinstance(instance.fakeName, str)


@given(instance=domain::HashProperty_strategy)
def test_domain::hashproperty_fakeName_setter(instance):
    original = instance.fakeName
    instance.fakeName = original
    assert instance.fakeName == original

@given(instance=domain::Property_strategy)
@settings(max_examples=50)
def test_domain::property_instantiation(instance):
    assert isinstance(instance, domain::Property)

@given(instance=domain::Property_strategy)
def test_domain::property_fakeName_type(instance):
    assert isinstance(instance.fakeName, str)


@given(instance=domain::Property_strategy)
def test_domain::property_fakeName_setter(instance):
    original = instance.fakeName
    instance.fakeName = original
    assert instance.fakeName == original

@given(instance=domain::Property_strategy)
def test_domain::property_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Property_strategy)
def test_domain::property_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Property_strategy)
def test_domain::property_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=domain::Property_strategy)
def test_domain::property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=domain::JavaComponent_strategy)
@settings(max_examples=50)
def test_domain::javacomponent_instantiation(instance):
    assert isinstance(instance, domain::JavaComponent)

@given(instance=domain::JavaComponent_strategy)
def test_domain::javacomponent_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=domain::JavaComponent_strategy)
def test_domain::javacomponent_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=domain::JavaComponent_strategy)
def test_domain::javacomponent_groupId_type(instance):
    assert isinstance(instance.groupId, str)


@given(instance=domain::JavaComponent_strategy)
def test_domain::javacomponent_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original

@given(instance=domain::JavaComponent_strategy)
def test_domain::javacomponent_artifactId_type(instance):
    assert isinstance(instance.artifactId, str)


@given(instance=domain::JavaComponent_strategy)
def test_domain::javacomponent_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original

@given(instance=domain::JavaComponent_strategy)
def test_domain::javacomponent_basePackage_type(instance):
    assert isinstance(instance.basePackage, str)


@given(instance=domain::JavaComponent_strategy)
def test_domain::javacomponent_basePackage_setter(instance):
    original = instance.basePackage
    instance.basePackage = original
    assert instance.basePackage == original

@given(instance=UsingMappers_strategy)
@settings(max_examples=50)
def test_usingmappers_instantiation(instance):
    assert isinstance(instance, UsingMappers)

@given(instance=domain::ModelMapper_strategy)
@settings(max_examples=50)
def test_domain::modelmapper_instantiation(instance):
    assert isinstance(instance, domain::ModelMapper)

@given(instance=domain::ModelMapper_strategy)
def test_domain::modelmapper_artifactExecutionString_type(instance):
    assert isinstance(instance.artifactExecutionString, str)


@given(instance=domain::ModelMapper_strategy)
def test_domain::modelmapper_artifactExecutionString_setter(instance):
    original = instance.artifactExecutionString
    instance.artifactExecutionString = original
    assert instance.artifactExecutionString == original

@given(instance=domain::ModelMapper_strategy)
def test_domain::modelmapper_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ModelMapper_strategy)
def test_domain::modelmapper_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ModelMapper_strategy)
def test_domain::modelmapper_artifactRoot_type(instance):
    assert isinstance(instance.artifactRoot, str)


@given(instance=domain::ModelMapper_strategy)
def test_domain::modelmapper_artifactRoot_setter(instance):
    original = instance.artifactRoot
    instance.artifactRoot = original
    assert instance.artifactRoot == original

@given(instance=domain::DeploymentStarStep_strategy)
@settings(max_examples=50)
def test_domain::deploymentstarstep_instantiation(instance):
    assert isinstance(instance, domain::DeploymentStarStep)

@given(instance=domain::DeploymentStarStep_strategy)
def test_domain::deploymentstarstep_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DeploymentStarStep_strategy)
def test_domain::deploymentstarstep_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::DeploymentStarStep_strategy)
def test_domain::deploymentstarstep_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::DeploymentStarStep_strategy)
def test_domain::deploymentstarstep_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::DeploymentComponent_strategy)
@settings(max_examples=50)
def test_domain::deploymentcomponent_instantiation(instance):
    assert isinstance(instance, domain::DeploymentComponent)

@given(instance=domain::DeploymentComponent_strategy)
def test_domain::deploymentcomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::DeploymentComponent_strategy)
def test_domain::deploymentcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::DeploymentComponent_strategy)
def test_domain::deploymentcomponent_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DeploymentComponent_strategy)
def test_domain::deploymentcomponent_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::DeploymentComponents_strategy)
@settings(max_examples=50)
def test_domain::deploymentcomponents_instantiation(instance):
    assert isinstance(instance, domain::DeploymentComponents)

@given(instance=domain::DeploymentComponents_strategy)
def test_domain::deploymentcomponents_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DeploymentComponents_strategy)
def test_domain::deploymentcomponents_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ConfigExtension_strategy)
@settings(max_examples=50)
def test_domain::configextension_instantiation(instance):
    assert isinstance(instance, domain::ConfigExtension)

@given(instance=domain::ConfigExtension_strategy)
def test_domain::configextension_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ConfigExtension_strategy)
def test_domain::configextension_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::DeploymentSequence_strategy)
@settings(max_examples=50)
def test_domain::deploymentsequence_instantiation(instance):
    assert isinstance(instance, domain::DeploymentSequence)

@given(instance=domain::DeploymentSequence_strategy)
def test_domain::deploymentsequence_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::DeploymentSequence_strategy)
def test_domain::deploymentsequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::DeploymentSequence_strategy)
def test_domain::deploymentsequence_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DeploymentSequence_strategy)
def test_domain::deploymentsequence_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Infrastructure_strategy)
@settings(max_examples=50)
def test_domain::infrastructure_instantiation(instance):
    assert isinstance(instance, domain::Infrastructure)

@given(instance=domain::Infrastructure_strategy)
def test_domain::infrastructure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Infrastructure_strategy)
def test_domain::infrastructure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Infrastructure_strategy)
def test_domain::infrastructure_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Infrastructure_strategy)
def test_domain::infrastructure_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Configuration_strategy)
@settings(max_examples=50)
def test_domain::configuration_instantiation(instance):
    assert isinstance(instance, domain::Configuration)

@given(instance=domain::Configuration_strategy)
def test_domain::configuration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Configuration_strategy)
def test_domain::configuration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Configuration_strategy)
def test_domain::configuration_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Configuration_strategy)
def test_domain::configuration_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Recipe_strategy)
@settings(max_examples=50)
def test_domain::recipe_instantiation(instance):
    assert isinstance(instance, domain::Recipe)

@given(instance=domain::Recipe_strategy)
def test_domain::recipe_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Recipe_strategy)
def test_domain::recipe_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Recipe_strategy)
def test_domain::recipe_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Recipe_strategy)
def test_domain::recipe_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::UsingMappers_strategy)
@settings(max_examples=50)
def test_domain::usingmappers_instantiation(instance):
    assert isinstance(instance, domain::UsingMappers)

@given(instance=TypeMapper_strategy)
@settings(max_examples=50)
def test_typemapper_instantiation(instance):
    assert isinstance(instance, TypeMapper)

@given(instance=domain::JavaScriptMapper_strategy)
@settings(max_examples=50)
def test_domain::javascriptmapper_instantiation(instance):
    assert isinstance(instance, domain::JavaScriptMapper)

@given(instance=domain::JavaScriptMapper_strategy)
def test_domain::javascriptmapper_libraryUrl_type(instance):
    assert isinstance(instance.libraryUrl, str)


@given(instance=domain::JavaScriptMapper_strategy)
def test_domain::javascriptmapper_libraryUrl_setter(instance):
    original = instance.libraryUrl
    instance.libraryUrl = original
    assert instance.libraryUrl == original

@given(instance=domain::JavaMapper_strategy)
@settings(max_examples=50)
def test_domain::javamapper_instantiation(instance):
    assert isinstance(instance, domain::JavaMapper)

@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_artifactType_type(instance):
    assert isinstance(instance.artifactType, str)


@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_artifactType_setter(instance):
    original = instance.artifactType
    instance.artifactType = original
    assert instance.artifactType == original

@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_mappedToPackageName_type(instance):
    assert isinstance(instance.mappedToPackageName, str)


@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_mappedToPackageName_setter(instance):
    original = instance.mappedToPackageName
    instance.mappedToPackageName = original
    assert instance.mappedToPackageName == original

@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_libraryName_type(instance):
    assert isinstance(instance.libraryName, str)


@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_libraryName_setter(instance):
    original = instance.libraryName
    instance.libraryName = original
    assert instance.libraryName == original

@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_groupId_type(instance):
    assert isinstance(instance.groupId, str)


@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original

@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_artifactId_type(instance):
    assert isinstance(instance.artifactId, str)


@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original

@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_mappedToClassName_type(instance):
    assert isinstance(instance.mappedToClassName, str)


@given(instance=domain::JavaMapper_strategy)
def test_domain::javamapper_mappedToClassName_setter(instance):
    original = instance.mappedToClassName
    instance.mappedToClassName = original
    assert instance.mappedToClassName == original

@given(instance=Mapper_strategy)
@settings(max_examples=50)
def test_mapper_instantiation(instance):
    assert isinstance(instance, Mapper)

@given(instance=domain::CSSMapper_strategy)
@settings(max_examples=50)
def test_domain::cssmapper_instantiation(instance):
    assert isinstance(instance, domain::CSSMapper)

@given(instance=domain::CSSMapper_strategy)
def test_domain::cssmapper_fakePackageName_type(instance):
    assert isinstance(instance.fakePackageName, str)


@given(instance=domain::CSSMapper_strategy)
def test_domain::cssmapper_fakePackageName_setter(instance):
    original = instance.fakePackageName
    instance.fakePackageName = original
    assert instance.fakePackageName == original

@given(instance=domain::CSSMapper_strategy)
def test_domain::cssmapper_fakeTypeName_type(instance):
    assert isinstance(instance.fakeTypeName, str)


@given(instance=domain::CSSMapper_strategy)
def test_domain::cssmapper_fakeTypeName_setter(instance):
    original = instance.fakeTypeName
    instance.fakeTypeName = original
    assert instance.fakeTypeName == original

@given(instance=domain::CSSMapper_strategy)
def test_domain::cssmapper_libraryUrl_type(instance):
    assert isinstance(instance.libraryUrl, str)


@given(instance=domain::CSSMapper_strategy)
def test_domain::cssmapper_libraryUrl_setter(instance):
    original = instance.libraryUrl
    instance.libraryUrl = original
    assert instance.libraryUrl == original

@given(instance=domain::RoleMapper_strategy)
@settings(max_examples=50)
def test_domain::rolemapper_instantiation(instance):
    assert isinstance(instance, domain::RoleMapper)

@given(instance=domain::RoleMapper_strategy)
def test_domain::rolemapper_localRoleName_type(instance):
    assert isinstance(instance.localRoleName, str)


@given(instance=domain::RoleMapper_strategy)
def test_domain::rolemapper_localRoleName_setter(instance):
    original = instance.localRoleName
    instance.localRoleName = original
    assert instance.localRoleName == original

@given(instance=domain::RoleMapper_strategy)
def test_domain::rolemapper_globalRoleName_type(instance):
    assert isinstance(instance.globalRoleName, str)


@given(instance=domain::RoleMapper_strategy)
def test_domain::rolemapper_globalRoleName_setter(instance):
    original = instance.globalRoleName
    instance.globalRoleName = original
    assert instance.globalRoleName == original

@given(instance=domain::RoleMapper_strategy)
def test_domain::rolemapper_fakeRoleName_type(instance):
    assert isinstance(instance.fakeRoleName, str)


@given(instance=domain::RoleMapper_strategy)
def test_domain::rolemapper_fakeRoleName_setter(instance):
    original = instance.fakeRoleName
    instance.fakeRoleName = original
    assert instance.fakeRoleName == original

@given(instance=domain::Mapper_strategy)
@settings(max_examples=50)
def test_domain::mapper_instantiation(instance):
    assert isinstance(instance, domain::Mapper)

@given(instance=domain::Mapper_strategy)
def test_domain::mapper_uiLayer_type(instance):
    assert isinstance(instance.uiLayer, bool)


@given(instance=domain::Mapper_strategy)
def test_domain::mapper_uiLayer_setter(instance):
    original = instance.uiLayer
    instance.uiLayer = original
    assert instance.uiLayer == original

@given(instance=domain::Mapper_strategy)
def test_domain::mapper_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Mapper_strategy)
def test_domain::mapper_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Mapper_strategy)
def test_domain::mapper_serviceLayer_type(instance):
    assert isinstance(instance.serviceLayer, bool)


@given(instance=domain::Mapper_strategy)
def test_domain::mapper_serviceLayer_setter(instance):
    original = instance.serviceLayer
    instance.serviceLayer = original
    assert instance.serviceLayer == original

@given(instance=domain::StyleLibrary_strategy)
@settings(max_examples=50)
def test_domain::stylelibrary_instantiation(instance):
    assert isinstance(instance, domain::StyleLibrary)

@given(instance=domain::StyleLibrary_strategy)
def test_domain::stylelibrary_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::StyleLibrary_strategy)
def test_domain::stylelibrary_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::StyleLibrary_strategy)
def test_domain::stylelibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::StyleLibrary_strategy)
def test_domain::stylelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Group_strategy)
@settings(max_examples=50)
def test_domain::group_instantiation(instance):
    assert isinstance(instance, domain::Group)

@given(instance=domain::Group_strategy)
def test_domain::group_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Group_strategy)
def test_domain::group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Group_strategy)
def test_domain::group_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Group_strategy)
def test_domain::group_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::StyleSet_strategy)
@settings(max_examples=50)
def test_domain::styleset_instantiation(instance):
    assert isinstance(instance, domain::StyleSet)

@given(instance=domain::StyleSet_strategy)
def test_domain::styleset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::StyleSet_strategy)
def test_domain::styleset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::StyleSet_strategy)
def test_domain::styleset_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::StyleSet_strategy)
def test_domain::styleset_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Translation_strategy)
@settings(max_examples=50)
def test_domain::translation_instantiation(instance):
    assert isinstance(instance, domain::Translation)

@given(instance=domain::Translation_strategy)
def test_domain::translation_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Translation_strategy)
def test_domain::translation_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Translation_strategy)
def test_domain::translation_translation_type(instance):
    assert isinstance(instance.translation, str)


@given(instance=domain::Translation_strategy)
def test_domain::translation_translation_setter(instance):
    original = instance.translation
    instance.translation = original
    assert instance.translation == original

@given(instance=domain::Message_strategy)
@settings(max_examples=50)
def test_domain::message_instantiation(instance):
    assert isinstance(instance, domain::Message)

@given(instance=domain::Message_strategy)
def test_domain::message_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Message_strategy)
def test_domain::message_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Message_strategy)
def test_domain::message_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Message_strategy)
def test_domain::message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::LanguageRef_strategy)
@settings(max_examples=50)
def test_domain::languageref_instantiation(instance):
    assert isinstance(instance, domain::LanguageRef)

@given(instance=domain::LanguageRef_strategy)
def test_domain::languageref_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::LanguageRef_strategy)
def test_domain::languageref_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=Categorized_strategy)
@settings(max_examples=50)
def test_categorized_instantiation(instance):
    assert isinstance(instance, Categorized)

@given(instance=domain::RelationShip_strategy)
@settings(max_examples=50)
def test_domain::relationship_instantiation(instance):
    assert isinstance(instance, domain::RelationShip)

@given(instance=domain::RelationShip_strategy)
def test_domain::relationship_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::RelationShip_strategy)
def test_domain::relationship_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::PopupCanvas_strategy)
@settings(max_examples=50)
def test_domain::popupcanvas_instantiation(instance):
    assert isinstance(instance, domain::PopupCanvas)

@given(instance=domain::PopupCanvas_strategy)
def test_domain::popupcanvas_modal_type(instance):
    assert isinstance(instance.modal, bool)


@given(instance=domain::PopupCanvas_strategy)
def test_domain::popupcanvas_modal_setter(instance):
    original = instance.modal
    instance.modal = original
    assert instance.modal == original

@given(instance=domain::Type_strategy)
@settings(max_examples=50)
def test_domain::type_instantiation(instance):
    assert isinstance(instance, domain::Type)

@given(instance=domain::Window_strategy)
@settings(max_examples=50)
def test_domain::window_instantiation(instance):
    assert isinstance(instance, domain::Window)

@given(instance=domain::Canvas_strategy)
@settings(max_examples=50)
def test_domain::canvas_instantiation(instance):
    assert isinstance(instance, domain::Canvas)

@given(instance=domain::MenuDefinition_strategy)
@settings(max_examples=50)
def test_domain::menudefinition_instantiation(instance):
    assert isinstance(instance, domain::MenuDefinition)

@given(instance=domain::MenuDefinition_strategy)
def test_domain::menudefinition_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::MenuDefinition_strategy)
def test_domain::menudefinition_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::MenuDefinition_strategy)
def test_domain::menudefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::MenuDefinition_strategy)
def test_domain::menudefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ViewElement_strategy)
@settings(max_examples=50)
def test_domain::viewelement_instantiation(instance):
    assert isinstance(instance, domain::ViewElement)

@given(instance=domain::FlexField_strategy)
@settings(max_examples=50)
def test_domain::flexfield_instantiation(instance):
    assert isinstance(instance, domain::FlexField)

@given(instance=domain::Uielement_strategy)
@settings(max_examples=50)
def test_domain::uielement_instantiation(instance):
    assert isinstance(instance, domain::Uielement)

@given(instance=domain::Uielement_strategy)
def test_domain::uielement_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Uielement_strategy)
def test_domain::uielement_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::TabPage_strategy)
@settings(max_examples=50)
def test_domain::tabpage_instantiation(instance):
    assert isinstance(instance, domain::TabPage)

@given(instance=domain::TabCanvas_strategy)
@settings(max_examples=50)
def test_domain::tabcanvas_instantiation(instance):
    assert isinstance(instance, domain::TabCanvas)

@given(instance=domain::TabCanvas_strategy)
def test_domain::tabcanvas_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=domain::TabCanvas_strategy)
def test_domain::tabcanvas_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=domain::Language_strategy)
@settings(max_examples=50)
def test_domain::language_instantiation(instance):
    assert isinstance(instance, domain::Language)

@given(instance=domain::Language_strategy)
def test_domain::language_lang_type(instance):
    assert isinstance(instance.lang, str)


@given(instance=domain::Language_strategy)
def test_domain::language_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=domain::Language_strategy)
def test_domain::language_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=domain::Language_strategy)
def test_domain::language_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=domain::Language_strategy)
def test_domain::language_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Language_strategy)
def test_domain::language_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Language_strategy)
def test_domain::language_defaultLang_type(instance):
    assert isinstance(instance.defaultLang, bool)


@given(instance=domain::Language_strategy)
def test_domain::language_defaultLang_setter(instance):
    original = instance.defaultLang
    instance.defaultLang = original
    assert instance.defaultLang == original

@given(instance=domain::MessageLibrary_strategy)
@settings(max_examples=50)
def test_domain::messagelibrary_instantiation(instance):
    assert isinstance(instance, domain::MessageLibrary)

@given(instance=domain::MessageLibrary_strategy)
def test_domain::messagelibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::MessageLibrary_strategy)
def test_domain::messagelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::MessageLibrary_strategy)
def test_domain::messagelibrary_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::MessageLibrary_strategy)
def test_domain::messagelibrary_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Operation_strategy)
@settings(max_examples=50)
def test_domain::operation_instantiation(instance):
    assert isinstance(instance, domain::Operation)

@given(instance=domain::Operation_strategy)
def test_domain::operation_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Operation_strategy)
def test_domain::operation_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Operation_strategy)
def test_domain::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Operation_strategy)
def test_domain::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypePointer_strategy)
@settings(max_examples=50)
def test_typepointer_instantiation(instance):
    assert isinstance(instance, TypePointer)

@given(instance=domain::FormParameter_strategy)
@settings(max_examples=50)
def test_domain::formparameter_instantiation(instance):
    assert isinstance(instance, domain::FormParameter)

@given(instance=domain::FormParameter_strategy)
def test_domain::formparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::FormParameter_strategy)
def test_domain::formparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::FormParameter_strategy)
def test_domain::formparameter_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::FormParameter_strategy)
def test_domain::formparameter_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::TypeReference_strategy)
@settings(max_examples=50)
def test_domain::typereference_instantiation(instance):
    assert isinstance(instance, domain::TypeReference)

@given(instance=domain::Attribute_strategy)
@settings(max_examples=50)
def test_domain::attribute_instantiation(instance):
    assert isinstance(instance, domain::Attribute)

@given(instance=domain::Attribute_strategy)
def test_domain::attribute_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Attribute_strategy)
def test_domain::attribute_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Attribute_strategy)
def test_domain::attribute_pk_type(instance):
    assert isinstance(instance.pk, bool)


@given(instance=domain::Attribute_strategy)
def test_domain::attribute_pk_setter(instance):
    original = instance.pk
    instance.pk = original
    assert instance.pk == original

@given(instance=domain::Attribute_strategy)
def test_domain::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Attribute_strategy)
def test_domain::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::TypeMapper_strategy)
@settings(max_examples=50)
def test_domain::typemapper_instantiation(instance):
    assert isinstance(instance, domain::TypeMapper)

@given(instance=domain::ReturnValue_strategy)
@settings(max_examples=50)
def test_domain::returnvalue_instantiation(instance):
    assert isinstance(instance, domain::ReturnValue)

@given(instance=domain::ReturnValue_strategy)
def test_domain::returnvalue_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ReturnValue_strategy)
def test_domain::returnvalue_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Parameter_strategy)
@settings(max_examples=50)
def test_domain::parameter_instantiation(instance):
    assert isinstance(instance, domain::Parameter)

@given(instance=domain::Parameter_strategy)
def test_domain::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Parameter_strategy)
def test_domain::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Parameter_strategy)
def test_domain::parameter_order_type(instance):
    assert isinstance(instance.order, int)


@given(instance=domain::Parameter_strategy)
def test_domain::parameter_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=domain::Parameter_strategy)
def test_domain::parameter_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Parameter_strategy)
def test_domain::parameter_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::MethodPointer_strategy)
@settings(max_examples=50)
def test_domain::methodpointer_instantiation(instance):
    assert isinstance(instance, domain::MethodPointer)

@given(instance=domain::MethodPointer_strategy)
def test_domain::methodpointer_fakeMethod_type(instance):
    assert isinstance(instance.fakeMethod, str)


@given(instance=domain::MethodPointer_strategy)
def test_domain::methodpointer_fakeMethod_setter(instance):
    original = instance.fakeMethod
    instance.fakeMethod = original
    assert instance.fakeMethod == original

@given(instance=domain::Mappers_strategy)
@settings(max_examples=50)
def test_domain::mappers_instantiation(instance):
    assert isinstance(instance, domain::Mappers)

@given(instance=domain::Mappers_strategy)
def test_domain::mappers_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Mappers_strategy)
def test_domain::mappers_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ApplicationMapper_strategy)
@settings(max_examples=50)
def test_domain::applicationmapper_instantiation(instance):
    assert isinstance(instance, domain::ApplicationMapper)

@given(instance=domain::ApplicationMapper_strategy)
def test_domain::applicationmapper_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ApplicationMapper_strategy)
def test_domain::applicationmapper_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ApplicationMapper_strategy)
def test_domain::applicationmapper_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ApplicationMapper_strategy)
def test_domain::applicationmapper_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Recipes_strategy)
@settings(max_examples=50)
def test_domain::recipes_instantiation(instance):
    assert isinstance(instance, domain::Recipes)

@given(instance=domain::Recipes_strategy)
def test_domain::recipes_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Recipes_strategy)
def test_domain::recipes_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ApplicationRecipe_strategy)
@settings(max_examples=50)
def test_domain::applicationrecipe_instantiation(instance):
    assert isinstance(instance, domain::ApplicationRecipe)

@given(instance=domain::ApplicationRecipe_strategy)
def test_domain::applicationrecipe_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ApplicationRecipe_strategy)
def test_domain::applicationrecipe_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ApplicationRecipe_strategy)
def test_domain::applicationrecipe_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ApplicationRecipe_strategy)
def test_domain::applicationrecipe_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::UIPackage_strategy)
@settings(max_examples=50)
def test_domain::uipackage_instantiation(instance):
    assert isinstance(instance, domain::UIPackage)

@given(instance=domain::UIPackage_strategy)
def test_domain::uipackage_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::UIPackage_strategy)
def test_domain::uipackage_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ApplicationUIPackage_strategy)
@settings(max_examples=50)
def test_domain::applicationuipackage_instantiation(instance):
    assert isinstance(instance, domain::ApplicationUIPackage)

@given(instance=domain::ApplicationUIPackage_strategy)
def test_domain::applicationuipackage_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ApplicationUIPackage_strategy)
def test_domain::applicationuipackage_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ApplicationUIPackage_strategy)
def test_domain::applicationuipackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ApplicationUIPackage_strategy)
def test_domain::applicationuipackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Styles_strategy)
@settings(max_examples=50)
def test_domain::styles_instantiation(instance):
    assert isinstance(instance, domain::Styles)

@given(instance=domain::Styles_strategy)
def test_domain::styles_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Styles_strategy)
def test_domain::styles_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Roles_strategy)
@settings(max_examples=50)
def test_domain::roles_instantiation(instance):
    assert isinstance(instance, domain::Roles)

@given(instance=domain::Roles_strategy)
def test_domain::roles_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Roles_strategy)
def test_domain::roles_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Messages_strategy)
@settings(max_examples=50)
def test_domain::messages_instantiation(instance):
    assert isinstance(instance, domain::Messages)

@given(instance=domain::Messages_strategy)
def test_domain::messages_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Messages_strategy)
def test_domain::messages_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ApplicationMessages_strategy)
@settings(max_examples=50)
def test_domain::applicationmessages_instantiation(instance):
    assert isinstance(instance, domain::ApplicationMessages)

@given(instance=domain::ApplicationMessages_strategy)
def test_domain::applicationmessages_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ApplicationMessages_strategy)
def test_domain::applicationmessages_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ApplicationMessages_strategy)
def test_domain::applicationmessages_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ApplicationMessages_strategy)
def test_domain::applicationmessages_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ApplicationRole_strategy)
@settings(max_examples=50)
def test_domain::applicationrole_instantiation(instance):
    assert isinstance(instance, domain::ApplicationRole)

@given(instance=domain::ApplicationRole_strategy)
def test_domain::applicationrole_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ApplicationRole_strategy)
def test_domain::applicationrole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ApplicationRole_strategy)
def test_domain::applicationrole_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ApplicationRole_strategy)
def test_domain::applicationrole_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ApplicationInfrastructureLayer_strategy)
@settings(max_examples=50)
def test_domain::applicationinfrastructurelayer_instantiation(instance):
    assert isinstance(instance, domain::ApplicationInfrastructureLayer)

@given(instance=domain::ApplicationInfrastructureLayer_strategy)
def test_domain::applicationinfrastructurelayer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ApplicationInfrastructureLayer_strategy)
def test_domain::applicationinfrastructurelayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ApplicationInfrastructureLayer_strategy)
def test_domain::applicationinfrastructurelayer_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ApplicationInfrastructureLayer_strategy)
def test_domain::applicationinfrastructurelayer_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::StylesPackage_strategy)
@settings(max_examples=50)
def test_domain::stylespackage_instantiation(instance):
    assert isinstance(instance, domain::StylesPackage)

@given(instance=domain::StylesPackage_strategy)
def test_domain::stylespackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::StylesPackage_strategy)
def test_domain::stylespackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::StylesPackage_strategy)
def test_domain::stylespackage_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::StylesPackage_strategy)
def test_domain::stylespackage_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Option_strategy)
@settings(max_examples=50)
def test_domain::option_instantiation(instance):
    assert isinstance(instance, domain::Option)

@given(instance=domain::Option_strategy)
def test_domain::option_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Option_strategy)
def test_domain::option_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Option_strategy)
def test_domain::option_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=domain::Option_strategy)
def test_domain::option_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=domain::QueryParameter_strategy)
@settings(max_examples=50)
def test_domain::queryparameter_instantiation(instance):
    assert isinstance(instance, domain::QueryParameter)

@given(instance=domain::QueryParameter_strategy)
def test_domain::queryparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::QueryParameter_strategy)
def test_domain::queryparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::QueryParameter_strategy)
def test_domain::queryparameter_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::QueryParameter_strategy)
def test_domain::queryparameter_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Specifier_strategy)
@settings(max_examples=50)
def test_domain::specifier_instantiation(instance):
    assert isinstance(instance, domain::Specifier)

@given(instance=domain::Specifier_strategy)
def test_domain::specifier_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Specifier_strategy)
def test_domain::specifier_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Specifier_strategy)
def test_domain::specifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Specifier_strategy)
def test_domain::specifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ModelQuery_strategy)
@settings(max_examples=50)
def test_domain::modelquery_instantiation(instance):
    assert isinstance(instance, domain::ModelQuery)

@given(instance=domain::ModelQuery_strategy)
def test_domain::modelquery_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ModelQuery_strategy)
def test_domain::modelquery_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ModelQuery_strategy)
def test_domain::modelquery_query_type(instance):
    assert isinstance(instance.query, str)


@given(instance=domain::ModelQuery_strategy)
def test_domain::modelquery_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=domain::ModelQuery_strategy)
def test_domain::modelquery_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ModelQuery_strategy)
def test_domain::modelquery_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ConfigHash_strategy)
@settings(max_examples=50)
def test_domain::confighash_instantiation(instance):
    assert isinstance(instance, domain::ConfigHash)

@given(instance=domain::ConfigHash_strategy)
def test_domain::confighash_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ConfigHash_strategy)
def test_domain::confighash_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ConfigHash_strategy)
def test_domain::confighash_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ConfigHash_strategy)
def test_domain::confighash_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ConfigVariable_strategy)
@settings(max_examples=50)
def test_domain::configvariable_instantiation(instance):
    assert isinstance(instance, domain::ConfigVariable)

@given(instance=domain::ConfigVariable_strategy)
def test_domain::configvariable_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ConfigVariable_strategy)
def test_domain::configvariable_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ConfigVariable_strategy)
def test_domain::configvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ConfigVariable_strategy)
def test_domain::configvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Artifact_strategy)
@settings(max_examples=50)
def test_domain::artifact_instantiation(instance):
    assert isinstance(instance, domain::Artifact)

@given(instance=domain::Artifact_strategy)
def test_domain::artifact_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=domain::Artifact_strategy)
def test_domain::artifact_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=domain::Artifact_strategy)
def test_domain::artifact_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=domain::Artifact_strategy)
def test_domain::artifact_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=domain::Artifact_strategy)
def test_domain::artifact_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Artifact_strategy)
def test_domain::artifact_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Artifact_strategy)
def test_domain::artifact_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Artifact_strategy)
def test_domain::artifact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DomainArtifact_strategy)
@settings(max_examples=50)
def test_domainartifact_instantiation(instance):
    assert isinstance(instance, DomainArtifact)

@given(instance=domain::JPAService_strategy)
@settings(max_examples=50)
def test_domain::jpaservice_instantiation(instance):
    assert isinstance(instance, domain::JPAService)

@given(instance=domain::EJBService_strategy)
@settings(max_examples=50)
def test_domain::ejbservice_instantiation(instance):
    assert isinstance(instance, domain::EJBService)

@given(instance=domain::ContinuousIintegration_strategy)
@settings(max_examples=50)
def test_domain::continuousiintegration_instantiation(instance):
    assert isinstance(instance, domain::ContinuousIintegration)

@given(instance=domain::ORMEntity_strategy)
@settings(max_examples=50)
def test_domain::ormentity_instantiation(instance):
    assert isinstance(instance, domain::ORMEntity)

@given(instance=domain::Artifacts_strategy)
@settings(max_examples=50)
def test_domain::artifacts_instantiation(instance):
    assert isinstance(instance, domain::Artifacts)

@given(instance=domain::Artifacts_strategy)
def test_domain::artifacts_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Artifacts_strategy)
def test_domain::artifacts_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Application_strategy)
@settings(max_examples=50)
def test_domain::application_instantiation(instance):
    assert isinstance(instance, domain::Application)

@given(instance=domain::Application_strategy)
def test_domain::application_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Application_strategy)
def test_domain::application_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::DomainArtifact_strategy)
@settings(max_examples=50)
def test_domain::domainartifact_instantiation(instance):
    assert isinstance(instance, domain::DomainArtifact)

@given(instance=domain::DomainArtifact_strategy)
def test_domain::domainartifact_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::DomainArtifact_strategy)
def test_domain::domainartifact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::DomainArtifact_strategy)
def test_domain::domainartifact_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DomainArtifact_strategy)
def test_domain::domainartifact_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=HTMLLayerHolder_strategy)
@settings(max_examples=50)
def test_htmllayerholder_instantiation(instance):
    assert isinstance(instance, HTMLLayerHolder)

@given(instance=domain::ApplicationStyle_strategy)
@settings(max_examples=50)
def test_domain::applicationstyle_instantiation(instance):
    assert isinstance(instance, domain::ApplicationStyle)

@given(instance=domain::ApplicationStyle_strategy)
def test_domain::applicationstyle_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ApplicationStyle_strategy)
def test_domain::applicationstyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ApplicationStyle_strategy)
def test_domain::applicationstyle_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ApplicationStyle_strategy)
def test_domain::applicationstyle_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Types_strategy)
@settings(max_examples=50)
def test_domain::types_instantiation(instance):
    assert isinstance(instance, domain::Types)

@given(instance=domain::Types_strategy)
def test_domain::types_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Types_strategy)
def test_domain::types_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Types_strategy)
def test_domain::types_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Types_strategy)
def test_domain::types_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Ingredient_strategy)
@settings(max_examples=50)
def test_domain::ingredient_instantiation(instance):
    assert isinstance(instance, domain::Ingredient)

@given(instance=domain::Ingredient_strategy)
def test_domain::ingredient_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Ingredient_strategy)
def test_domain::ingredient_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Ingredient_strategy)
def test_domain::ingredient_layer_type(instance):
    assert isinstance(instance.layer, str)


@given(instance=domain::Ingredient_strategy)
def test_domain::ingredient_layer_setter(instance):
    original = instance.layer
    instance.layer = original
    assert instance.layer == original

@given(instance=domain::Ingredient_strategy)
def test_domain::ingredient_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Ingredient_strategy)
def test_domain::ingredient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ApplicationMappers_strategy)
@settings(max_examples=50)
def test_domain::applicationmappers_instantiation(instance):
    assert isinstance(instance, domain::ApplicationMappers)

@given(instance=domain::ApplicationMappers_strategy)
def test_domain::applicationmappers_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ApplicationMappers_strategy)
def test_domain::applicationmappers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ApplicationMappers_strategy)
def test_domain::applicationmappers_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ApplicationMappers_strategy)
def test_domain::applicationmappers_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Component_strategy)
@settings(max_examples=50)
def test_domain::component_instantiation(instance):
    assert isinstance(instance, domain::Component)

@given(instance=domain::Component_strategy)
def test_domain::component_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Component_strategy)
def test_domain::component_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Component_strategy)
def test_domain::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Component_strategy)
def test_domain::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Component_strategy)
def test_domain::component_componentRoot_type(instance):
    assert isinstance(instance.componentRoot, str)


@given(instance=domain::Component_strategy)
def test_domain::component_componentRoot_setter(instance):
    original = instance.componentRoot
    instance.componentRoot = original
    assert instance.componentRoot == original

@given(instance=domain::ApplicationRecipes_strategy)
@settings(max_examples=50)
def test_domain::applicationrecipes_instantiation(instance):
    assert isinstance(instance, domain::ApplicationRecipes)

@given(instance=domain::ApplicationRecipes_strategy)
def test_domain::applicationrecipes_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ApplicationRecipes_strategy)
def test_domain::applicationrecipes_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ApplicationRecipes_strategy)
def test_domain::applicationrecipes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ApplicationRecipes_strategy)
def test_domain::applicationrecipes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ViewPortHolder_strategy)
@settings(max_examples=50)
def test_domain::viewportholder_instantiation(instance):
    assert isinstance(instance, domain::ViewPortHolder)

@given(instance=domain::LayerHolder_strategy)
@settings(max_examples=50)
def test_domain::layerholder_instantiation(instance):
    assert isinstance(instance, domain::LayerHolder)

@given(instance=domain::ApplicationUILayer_strategy)
@settings(max_examples=50)
def test_domain::applicationuilayer_instantiation(instance):
    assert isinstance(instance, domain::ApplicationUILayer)

@given(instance=domain::ApplicationUILayer_strategy)
def test_domain::applicationuilayer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ApplicationUILayer_strategy)
def test_domain::applicationuilayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::ApplicationUILayer_strategy)
def test_domain::applicationuilayer_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ApplicationUILayer_strategy)
def test_domain::applicationuilayer_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Role_strategy)
@settings(max_examples=50)
def test_domain::role_instantiation(instance):
    assert isinstance(instance, domain::Role)

@given(instance=domain::Role_strategy)
def test_domain::role_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Role_strategy)
def test_domain::role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Role_strategy)
def test_domain::role_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Role_strategy)
def test_domain::role_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::DomainApplication_strategy)
@settings(max_examples=50)
def test_domain::domainapplication_instantiation(instance):
    assert isinstance(instance, domain::DomainApplication)

@given(instance=domain::DomainApplication_strategy)
def test_domain::domainapplication_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DomainApplication_strategy)
def test_domain::domainapplication_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::DomainApplication_strategy)
def test_domain::domainapplication_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::DomainApplication_strategy)
def test_domain::domainapplication_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::GrantAccess_strategy)
@settings(max_examples=50)
def test_domain::grantaccess_instantiation(instance):
    assert isinstance(instance, domain::GrantAccess)

@given(instance=domain::GrantAccess_strategy)
def test_domain::grantaccess_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::GrantAccess_strategy)
def test_domain::grantaccess_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Secured_strategy)
@settings(max_examples=50)
def test_domain::secured_instantiation(instance):
    assert isinstance(instance, domain::Secured)

@given(instance=domain::GenerationHint_strategy)
@settings(max_examples=50)
def test_domain::generationhint_instantiation(instance):
    assert isinstance(instance, domain::GenerationHint)

@given(instance=domain::GenerationHint_strategy)
def test_domain::generationhint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::GenerationHint_strategy)
def test_domain::generationhint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::GenerationHint_strategy)
def test_domain::generationhint_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::GenerationHint_strategy)
def test_domain::generationhint_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::GenerationHint_strategy)
def test_domain::generationhint_applyedClass_type(instance):
    assert isinstance(instance.applyedClass, str)


@given(instance=domain::GenerationHint_strategy)
def test_domain::generationhint_applyedClass_setter(instance):
    original = instance.applyedClass
    instance.applyedClass = original
    assert instance.applyedClass == original

@given(instance=domain::Classifier_strategy)
@settings(max_examples=50)
def test_domain::classifier_instantiation(instance):
    assert isinstance(instance, domain::Classifier)

@given(instance=domain::Classifier_strategy)
def test_domain::classifier_details_type(instance):
    assert isinstance(instance.details, str)


@given(instance=domain::Classifier_strategy)
def test_domain::classifier_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=domain::Classifier_strategy)
def test_domain::classifier_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Classifier_strategy)
def test_domain::classifier_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Categorized_strategy)
@settings(max_examples=50)
def test_domain::categorized_instantiation(instance):
    assert isinstance(instance, domain::Categorized)

@given(instance=domain::HTMLLayerHolder_strategy)
@settings(max_examples=50)
def test_domain::htmllayerholder_instantiation(instance):
    assert isinstance(instance, domain::HTMLLayerHolder)

@given(instance=domain::HTMLLayerHolder_strategy)
def test_domain::htmllayerholder_columns_type(instance):
    assert isinstance(instance.columns, int)


@given(instance=domain::HTMLLayerHolder_strategy)
def test_domain::htmllayerholder_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=domain::EObject_strategy)
@settings(max_examples=50)
def test_domain::eobject_instantiation(instance):
    assert isinstance(instance, domain::EObject)

@given(instance=domain::DomainApplications_strategy)
@settings(max_examples=50)
def test_domain::domainapplications_instantiation(instance):
    assert isinstance(instance, domain::DomainApplications)

@given(instance=domain::DomainApplications_strategy)
def test_domain::domainapplications_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DomainApplications_strategy)
def test_domain::domainapplications_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::DomainApplications_strategy)
def test_domain::domainapplications_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::DomainApplications_strategy)
def test_domain::domainapplications_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::DomainTypes_strategy)
@settings(max_examples=50)
def test_domain::domaintypes_instantiation(instance):
    assert isinstance(instance, domain::DomainTypes)

@given(instance=domain::DomainTypes_strategy)
def test_domain::domaintypes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::DomainTypes_strategy)
def test_domain::domaintypes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::DomainTypes_strategy)
def test_domain::domaintypes_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DomainTypes_strategy)
def test_domain::domaintypes_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::DomainArtifacts_strategy)
@settings(max_examples=50)
def test_domain::domainartifacts_instantiation(instance):
    assert isinstance(instance, domain::DomainArtifacts)

@given(instance=domain::DomainArtifacts_strategy)
def test_domain::domainartifacts_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DomainArtifacts_strategy)
def test_domain::domainartifacts_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::DomainArtifacts_strategy)
def test_domain::domainartifacts_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::DomainArtifacts_strategy)
def test_domain::domainartifacts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Domain_strategy)
@settings(max_examples=50)
def test_domain::domain_instantiation(instance):
    assert isinstance(instance, domain::Domain)

@given(instance=domain::Domain_strategy)
def test_domain::domain_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Domain_strategy)
def test_domain::domain_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::TypesRepository_strategy)
@settings(max_examples=50)
def test_domain::typesrepository_instantiation(instance):
    assert isinstance(instance, domain::TypesRepository)

@given(instance=domain::TypesRepository_strategy)
def test_domain::typesrepository_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::TypesRepository_strategy)
def test_domain::typesrepository_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=MenuElement_strategy)
@settings(max_examples=50)
def test_menuelement_instantiation(instance):
    assert isinstance(instance, MenuElement)

@given(instance=domain::MenuSeparator_strategy)
@settings(max_examples=50)
def test_domain::menuseparator_instantiation(instance):
    assert isinstance(instance, domain::MenuSeparator)

@given(instance=domain::MenuExtensionPoint_strategy)
@settings(max_examples=50)
def test_domain::menuextensionpoint_instantiation(instance):
    assert isinstance(instance, domain::MenuExtensionPoint)

@given(instance=domain::MenuElement_strategy)
@settings(max_examples=50)
def test_domain::menuelement_instantiation(instance):
    assert isinstance(instance, domain::MenuElement)

@given(instance=domain::MenuElement_strategy)
def test_domain::menuelement_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::MenuElement_strategy)
def test_domain::menuelement_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::MenuElement_strategy)
def test_domain::menuelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::MenuElement_strategy)
def test_domain::menuelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::MenuExtensionRef_strategy)
@settings(max_examples=50)
def test_domain::menuextensionref_instantiation(instance):
    assert isinstance(instance, domain::MenuExtensionRef)

@given(instance=domain::MenuHolder_strategy)
@settings(max_examples=50)
def test_domain::menuholder_instantiation(instance):
    assert isinstance(instance, domain::MenuHolder)

@given(instance=domain::InfrastructureComponent_strategy)
@settings(max_examples=50)
def test_domain::infrastructurecomponent_instantiation(instance):
    assert isinstance(instance, domain::InfrastructureComponent)

@given(instance=domain::InfrastructureComponent_strategy)
def test_domain::infrastructurecomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::InfrastructureComponent_strategy)
def test_domain::infrastructurecomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::InfrastructureComponent_strategy)
def test_domain::infrastructurecomponent_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::InfrastructureComponent_strategy)
def test_domain::infrastructurecomponent_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::InfrastructureLayer_strategy)
@settings(max_examples=50)
def test_domain::infrastructurelayer_instantiation(instance):
    assert isinstance(instance, domain::InfrastructureLayer)

@given(instance=domain::InfrastructureLayer_strategy)
def test_domain::infrastructurelayer_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::InfrastructureLayer_strategy)
def test_domain::infrastructurelayer_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::InfrastructureLayer_strategy)
def test_domain::infrastructurelayer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::InfrastructureLayer_strategy)
def test_domain::infrastructurelayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Subsystem_strategy)
@settings(max_examples=50)
def test_domain::subsystem_instantiation(instance):
    assert isinstance(instance, domain::Subsystem)

@given(instance=domain::Subsystem_strategy)
def test_domain::subsystem_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Subsystem_strategy)
def test_domain::subsystem_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Subsystem_strategy)
def test_domain::subsystem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Subsystem_strategy)
def test_domain::subsystem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=InfrastructureComponent_strategy)
@settings(max_examples=50)
def test_infrastructurecomponent_instantiation(instance):
    assert isinstance(instance, InfrastructureComponent)

@given(instance=domain::Hub_strategy)
@settings(max_examples=50)
def test_domain::hub_instantiation(instance):
    assert isinstance(instance, domain::Hub)

@given(instance=domain::ServerClaster_strategy)
@settings(max_examples=50)
def test_domain::serverclaster_instantiation(instance):
    assert isinstance(instance, domain::ServerClaster)

@given(instance=domain::Router_strategy)
@settings(max_examples=50)
def test_domain::router_instantiation(instance):
    assert isinstance(instance, domain::Router)

@given(instance=domain::Storage_strategy)
@settings(max_examples=50)
def test_domain::storage_instantiation(instance):
    assert isinstance(instance, domain::Storage)

@given(instance=domain::Server_strategy)
@settings(max_examples=50)
def test_domain::server_instantiation(instance):
    assert isinstance(instance, domain::Server)

@given(instance=domain::EnterpriseInfrastructure_strategy)
@settings(max_examples=50)
def test_domain::enterpriseinfrastructure_instantiation(instance):
    assert isinstance(instance, domain::EnterpriseInfrastructure)

@given(instance=domain::EnterpriseInfrastructure_strategy)
def test_domain::enterpriseinfrastructure_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::EnterpriseInfrastructure_strategy)
def test_domain::enterpriseinfrastructure_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::InfrastructureConnection_strategy)
@settings(max_examples=50)
def test_domain::infrastructureconnection_instantiation(instance):
    assert isinstance(instance, domain::InfrastructureConnection)

@given(instance=domain::InfrastructureConnection_strategy)
def test_domain::infrastructureconnection_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::InfrastructureConnection_strategy)
def test_domain::infrastructureconnection_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Datacenter_strategy)
@settings(max_examples=50)
def test_domain::datacenter_instantiation(instance):
    assert isinstance(instance, domain::Datacenter)

@given(instance=domain::Datacenter_strategy)
def test_domain::datacenter_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Datacenter_strategy)
def test_domain::datacenter_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Datacenter_strategy)
def test_domain::datacenter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Datacenter_strategy)
def test_domain::datacenter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::OrderBy_strategy)
@settings(max_examples=50)
def test_domain::orderby_instantiation(instance):
    assert isinstance(instance, domain::OrderBy)

@given(instance=domain::OrderBy_strategy)
def test_domain::orderby_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::OrderBy_strategy)
def test_domain::orderby_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::OrderBy_strategy)
def test_domain::orderby_order_type(instance):
    assert isinstance(instance.order, str)


@given(instance=domain::OrderBy_strategy)
def test_domain::orderby_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=domain::Orders_strategy)
@settings(max_examples=50)
def test_domain::orders_instantiation(instance):
    assert isinstance(instance, domain::Orders)

@given(instance=domain::Orders_strategy)
def test_domain::orders_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Orders_strategy)
def test_domain::orders_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ArtificialField_strategy)
@settings(max_examples=50)
def test_domain::artificialfield_instantiation(instance):
    assert isinstance(instance, domain::ArtificialField)

@given(instance=domain::ArtificialField_strategy)
def test_domain::artificialfield_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::ArtificialField_strategy)
def test_domain::artificialfield_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ArtificialField_strategy)
def test_domain::artificialfield_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::ArtificialField_strategy)
def test_domain::artificialfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::FormVariable_strategy)
@settings(max_examples=50)
def test_domain::formvariable_instantiation(instance):
    assert isinstance(instance, domain::FormVariable)

@given(instance=domain::FormVariable_strategy)
def test_domain::formvariable_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::FormVariable_strategy)
def test_domain::formvariable_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::FormVariable_strategy)
def test_domain::formvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::FormVariable_strategy)
def test_domain::formvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ProxiesList_strategy)
@settings(max_examples=50)
def test_proxieslist_instantiation(instance):
    assert isinstance(instance, ProxiesList)

@given(instance=domain::SearchTrigger_strategy)
@settings(max_examples=50)
def test_domain::searchtrigger_instantiation(instance):
    assert isinstance(instance, domain::SearchTrigger)

@given(instance=domain::SearchTrigger_strategy)
def test_domain::searchtrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::SearchTrigger_strategy)
def test_domain::searchtrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::DeleteTrigger_strategy)
@settings(max_examples=50)
def test_domain::deletetrigger_instantiation(instance):
    assert isinstance(instance, domain::DeleteTrigger)

@given(instance=domain::DeleteTrigger_strategy)
def test_domain::deletetrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::DeleteTrigger_strategy)
def test_domain::deletetrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::InsertTrigger_strategy)
@settings(max_examples=50)
def test_domain::inserttrigger_instantiation(instance):
    assert isinstance(instance, domain::InsertTrigger)

@given(instance=domain::InsertTrigger_strategy)
def test_domain::inserttrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::InsertTrigger_strategy)
def test_domain::inserttrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::CreateTrigger_strategy)
@settings(max_examples=50)
def test_domain::createtrigger_instantiation(instance):
    assert isinstance(instance, domain::CreateTrigger)

@given(instance=domain::CreateTrigger_strategy)
def test_domain::createtrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::CreateTrigger_strategy)
def test_domain::createtrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::ProxiesList_strategy)
@settings(max_examples=50)
def test_domain::proxieslist_instantiation(instance):
    assert isinstance(instance, domain::ProxiesList)

@given(instance=domain::PREUpdateTrigger_strategy)
@settings(max_examples=50)
def test_domain::preupdatetrigger_instantiation(instance):
    assert isinstance(instance, domain::PREUpdateTrigger)

@given(instance=domain::PREUpdateTrigger_strategy)
def test_domain::preupdatetrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::PREUpdateTrigger_strategy)
def test_domain::preupdatetrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::POSTCreateTrigger_strategy)
@settings(max_examples=50)
def test_domain::postcreatetrigger_instantiation(instance):
    assert isinstance(instance, domain::POSTCreateTrigger)

@given(instance=domain::POSTCreateTrigger_strategy)
def test_domain::postcreatetrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::POSTCreateTrigger_strategy)
def test_domain::postcreatetrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::PREDeleteTrigger_strategy)
@settings(max_examples=50)
def test_domain::predeletetrigger_instantiation(instance):
    assert isinstance(instance, domain::PREDeleteTrigger)

@given(instance=domain::PREDeleteTrigger_strategy)
def test_domain::predeletetrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::PREDeleteTrigger_strategy)
def test_domain::predeletetrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::PREInsertTrigger_strategy)
@settings(max_examples=50)
def test_domain::preinserttrigger_instantiation(instance):
    assert isinstance(instance, domain::PREInsertTrigger)

@given(instance=domain::PREInsertTrigger_strategy)
def test_domain::preinserttrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::PREInsertTrigger_strategy)
def test_domain::preinserttrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::POSTQueryTrigger_strategy)
@settings(max_examples=50)
def test_domain::postquerytrigger_instantiation(instance):
    assert isinstance(instance, domain::POSTQueryTrigger)

@given(instance=domain::POSTQueryTrigger_strategy)
def test_domain::postquerytrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::POSTQueryTrigger_strategy)
def test_domain::postquerytrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::PREQueryTrigger_strategy)
@settings(max_examples=50)
def test_domain::prequerytrigger_instantiation(instance):
    assert isinstance(instance, domain::PREQueryTrigger)

@given(instance=domain::PREQueryTrigger_strategy)
def test_domain::prequerytrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::PREQueryTrigger_strategy)
def test_domain::prequerytrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::PREFormTrigger_strategy)
@settings(max_examples=50)
def test_domain::preformtrigger_instantiation(instance):
    assert isinstance(instance, domain::PREFormTrigger)

@given(instance=domain::PREFormTrigger_strategy)
def test_domain::preformtrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::PREFormTrigger_strategy)
def test_domain::preformtrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=MethodPointer_strategy)
@settings(max_examples=50)
def test_methodpointer_instantiation(instance):
    assert isinstance(instance, MethodPointer)

@given(instance=domain::Trigger_strategy)
@settings(max_examples=50)
def test_domain::trigger_instantiation(instance):
    assert isinstance(instance, domain::Trigger)

@given(instance=domain::Dependency_strategy)
@settings(max_examples=50)
def test_domain::dependency_instantiation(instance):
    assert isinstance(instance, domain::Dependency)

@given(instance=domain::Dependency_strategy)
def test_domain::dependency_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Dependency_strategy)
def test_domain::dependency_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Dependency_strategy)
def test_domain::dependency_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Dependency_strategy)
def test_domain::dependency_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::UpdateTrigger_strategy)
@settings(max_examples=50)
def test_domain::updatetrigger_instantiation(instance):
    assert isinstance(instance, domain::UpdateTrigger)

@given(instance=domain::UpdateTrigger_strategy)
def test_domain::updatetrigger_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::UpdateTrigger_strategy)
def test_domain::updatetrigger_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Root_strategy)
@settings(max_examples=50)
def test_domain::root_instantiation(instance):
    assert isinstance(instance, domain::Root)

@given(instance=domain::Root_strategy)
def test_domain::root_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Root_strategy)
def test_domain::root_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Root_strategy)
def test_domain::root_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Root_strategy)
def test_domain::root_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Tree_strategy)
@settings(max_examples=50)
def test_domain::tree_instantiation(instance):
    assert isinstance(instance, domain::Tree)

@given(instance=domain::Tree_strategy)
def test_domain::tree_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=domain::Tree_strategy)
def test_domain::tree_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=domain::Menu_strategy)
@settings(max_examples=50)
def test_domain::menu_instantiation(instance):
    assert isinstance(instance, domain::Menu)

@given(instance=domain::Menu_strategy)
def test_domain::menu_fakeName_type(instance):
    assert isinstance(instance.fakeName, str)


@given(instance=domain::Menu_strategy)
def test_domain::menu_fakeName_setter(instance):
    original = instance.fakeName
    instance.fakeName = original
    assert instance.fakeName == original

@given(instance=domain::Table_strategy)
@settings(max_examples=50)
def test_domain::table_instantiation(instance):
    assert isinstance(instance, domain::Table)

@given(instance=domain::Table_strategy)
def test_domain::table_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=domain::Table_strategy)
def test_domain::table_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=domain::Table_strategy)
def test_domain::table_rowNumber_type(instance):
    assert isinstance(instance.rowNumber, int)


@given(instance=domain::Table_strategy)
def test_domain::table_rowNumber_setter(instance):
    original = instance.rowNumber
    instance.rowNumber = original
    assert instance.rowNumber == original

@given(instance=domain::Column_strategy)
@settings(max_examples=50)
def test_domain::column_instantiation(instance):
    assert isinstance(instance, domain::Column)

@given(instance=domain::Column_strategy)
def test_domain::column_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=domain::Column_strategy)
def test_domain::column_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=domain::Column_strategy)
def test_domain::column_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Column_strategy)
def test_domain::column_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=ItemIcon_strategy)
@settings(max_examples=50)
def test_itemicon_instantiation(instance):
    assert isinstance(instance, ItemIcon)

@given(instance=domain::MenuItem_strategy)
@settings(max_examples=50)
def test_domain::menuitem_instantiation(instance):
    assert isinstance(instance, domain::MenuItem)

@given(instance=domain::SubMenu_strategy)
@settings(max_examples=50)
def test_domain::submenu_instantiation(instance):
    assert isinstance(instance, domain::SubMenu)

@given(instance=domain::Button_strategy)
@settings(max_examples=50)
def test_domain::button_instantiation(instance):
    assert isinstance(instance, domain::Button)

@given(instance=domain::Button_strategy)
def test_domain::button_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=domain::Button_strategy)
def test_domain::button_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=domain::MenuFolder_strategy)
@settings(max_examples=50)
def test_domain::menufolder_instantiation(instance):
    assert isinstance(instance, domain::MenuFolder)

@given(instance=domain::MenuFolder_strategy)
def test_domain::menufolder_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::MenuFolder_strategy)
def test_domain::menufolder_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::MenuFolder_strategy)
def test_domain::menufolder_extensionPoint_type(instance):
    assert isinstance(instance.extensionPoint, bool)


@given(instance=domain::MenuFolder_strategy)
def test_domain::menufolder_extensionPoint_setter(instance):
    original = instance.extensionPoint
    instance.extensionPoint = original
    assert instance.extensionPoint == original

@given(instance=domain::MenuFolder_strategy)
def test_domain::menufolder_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::MenuFolder_strategy)
def test_domain::menufolder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Relation_strategy)
@settings(max_examples=50)
def test_domain::relation_instantiation(instance):
    assert isinstance(instance, domain::Relation)

@given(instance=domain::Relation_strategy)
def test_domain::relation_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=domain::Relation_strategy)
def test_domain::relation_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=domain::Relation_strategy)
def test_domain::relation_isTree_type(instance):
    assert isinstance(instance.isTree, bool)


@given(instance=domain::Relation_strategy)
def test_domain::relation_isTree_setter(instance):
    original = instance.isTree
    instance.isTree = original
    assert instance.isTree == original

@given(instance=domain::Relation_strategy)
def test_domain::relation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domain::Relation_strategy)
def test_domain::relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domain::Image_strategy)
@settings(max_examples=50)
def test_domain::image_instantiation(instance):
    assert isinstance(instance, domain::Image)

@given(instance=OptionSelection_strategy)
@settings(max_examples=50)
def test_optionselection_instantiation(instance):
    assert isinstance(instance, OptionSelection)

@given(instance=domain::DropDownSelection_strategy)
@settings(max_examples=50)
def test_domain::dropdownselection_instantiation(instance):
    assert isinstance(instance, domain::DropDownSelection)

@given(instance=domain::DropDownSelection_strategy)
def test_domain::dropdownselection_initialOptionValue_type(instance):
    assert isinstance(instance.initialOptionValue, str)


@given(instance=domain::DropDownSelection_strategy)
def test_domain::dropdownselection_initialOptionValue_setter(instance):
    original = instance.initialOptionValue
    instance.initialOptionValue = original
    assert instance.initialOptionValue == original

@given(instance=domain::CheckBox_strategy)
@settings(max_examples=50)
def test_domain::checkbox_instantiation(instance):
    assert isinstance(instance, domain::CheckBox)

@given(instance=Formatable_strategy)
@settings(max_examples=50)
def test_formatable_instantiation(instance):
    assert isinstance(instance, Formatable)

@given(instance=domain::Date_strategy)
@settings(max_examples=50)
def test_domain::date_instantiation(instance):
    assert isinstance(instance, domain::Date)

@given(instance=domain::InputText_strategy)
@settings(max_examples=50)
def test_domain::inputtext_instantiation(instance):
    assert isinstance(instance, domain::InputText)

@given(instance=domain::Password_strategy)
@settings(max_examples=50)
def test_domain::password_instantiation(instance):
    assert isinstance(instance, domain::Password)

@given(instance=domain::OutputText_strategy)
@settings(max_examples=50)
def test_domain::outputtext_instantiation(instance):
    assert isinstance(instance, domain::OutputText)
