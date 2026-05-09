import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::AbstractFrontElement,
    myDsl::Einterface,
    myDsl::AbstractMethod,
    myDsl::MethodBack,
    myDsl::Attribute,
    Eclass,
    myDsl::NativeClass,
    myDsl::Annotation,
    myDsl::GenericClass,
    myDsl::AbstractClass,
    myDsl::Descriptor,
    myDsl::Library,
    myDsl::Eclass,
    myDsl::JeeProject,
    myDsl::JavaApp,
    myDsl::SublayerSegment,
    myDsl::LayerSegmentRelation,
    myDsl::LayerSegment,
    myDsl::Layer,
    myDsl::RelationArch,
    myDsl::Component,
    myDsl::Epackage,
    myDsl::Subproject,
    myDsl::Operateson,
    myDsl::Transaction,
    myDsl::SpecialEntity,
    AbstractFrontElement,
    myDsl::Container,
    myDsl::ReactApp,
    myDsl::Property,
    myDsl::GeneralEntity,
    myDsl::EntityName,
    myDsl::EObject,
    myDsl::Operation,
    myDsl::Module,
    myDsl::Type,
    myDsl::Technology,
    myDsl::Architecture,
    myDsl::Domain,
    myDsl::System,
    myDsl::Submodule,
    myDsl::RelationDom,
    myDsl::ActionDispatcher,
    myDsl::ActionCreator,
    myDsl::Reducer,
    myDsl::Action,
    File,
    myDsl::Css,
    myDsl::Json,
    myDsl::Js,
    myDsl::Md,
    myDsl::JsMethodArgs,
    myDsl::AxiosRequest,
    myDsl::JsMethod,
    myDsl::UIComponent,
    UIComponent,
    myDsl::Visualizer,
    myDsl::RouterComponent,
    myDsl::ServiceFront,
    myDsl::State,
    myDsl::File,
    myDsl::JsModule,
    myDsl::Directory,
    myDsl::Functionality,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::abstractfrontelement_is_not_abstract():
    assert not inspect.isabstract(myDsl::AbstractFrontElement)


def test_mydsl::abstractfrontelement_constructor_exists():
    assert callable(myDsl::AbstractFrontElement.__init__)


def test_mydsl::abstractfrontelement_constructor_args():
    sig = inspect.signature(myDsl::AbstractFrontElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::einterface_is_not_abstract():
    assert not inspect.isabstract(myDsl::Einterface)


def test_mydsl::einterface_constructor_exists():
    assert callable(myDsl::Einterface.__init__)


def test_mydsl::einterface_constructor_args():
    sig = inspect.signature(myDsl::Einterface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::einterface_has_name():
    assert hasattr(myDsl::Einterface, "name")
    descriptor = None
    for klass in myDsl::Einterface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::abstractmethod_is_not_abstract():
    assert not inspect.isabstract(myDsl::AbstractMethod)


def test_mydsl::abstractmethod_constructor_exists():
    assert callable(myDsl::AbstractMethod.__init__)


def test_mydsl::abstractmethod_constructor_args():
    sig = inspect.signature(myDsl::AbstractMethod.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::abstractmethod_has_name():
    assert hasattr(myDsl::AbstractMethod, "name")
    descriptor = None
    for klass in myDsl::AbstractMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::methodback_is_not_abstract():
    assert not inspect.isabstract(myDsl::MethodBack)


def test_mydsl::methodback_constructor_exists():
    assert callable(myDsl::MethodBack.__init__)


def test_mydsl::methodback_constructor_args():
    sig = inspect.signature(myDsl::MethodBack.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::methodback_has_name():
    assert hasattr(myDsl::MethodBack, "name")
    descriptor = None
    for klass in myDsl::MethodBack.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl::Attribute)


def test_mydsl::attribute_constructor_exists():
    assert callable(myDsl::Attribute.__init__)


def test_mydsl::attribute_constructor_args():
    sig = inspect.signature(myDsl::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::attribute_has_name():
    assert hasattr(myDsl::Attribute, "name")
    descriptor = None
    for klass in myDsl::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(Eclass)


def test_eclass_constructor_exists():
    assert callable(Eclass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(Eclass.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::nativeclass_is_not_abstract():
    assert not inspect.isabstract(myDsl::NativeClass)


def test_mydsl::nativeclass_constructor_exists():
    assert callable(myDsl::NativeClass.__init__)


def test_mydsl::nativeclass_constructor_args():
    sig = inspect.signature(myDsl::NativeClass.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::annotation_is_not_abstract():
    assert not inspect.isabstract(myDsl::Annotation)


def test_mydsl::annotation_constructor_exists():
    assert callable(myDsl::Annotation.__init__)


def test_mydsl::annotation_constructor_args():
    sig = inspect.signature(myDsl::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "propertie" in params, "Missing parameter 'propertie'"

def test_mydsl::annotation_has_propertie():
    assert hasattr(myDsl::Annotation, "propertie")
    descriptor = None
    for klass in myDsl::Annotation.__mro__:
        if "propertie" in klass.__dict__:
            descriptor = klass.__dict__["propertie"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::genericclass_is_not_abstract():
    assert not inspect.isabstract(myDsl::GenericClass)


def test_mydsl::genericclass_constructor_exists():
    assert callable(myDsl::GenericClass.__init__)


def test_mydsl::genericclass_constructor_args():
    sig = inspect.signature(myDsl::GenericClass.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::abstractclass_is_not_abstract():
    assert not inspect.isabstract(myDsl::AbstractClass)


def test_mydsl::abstractclass_constructor_exists():
    assert callable(myDsl::AbstractClass.__init__)


def test_mydsl::abstractclass_constructor_args():
    sig = inspect.signature(myDsl::AbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::descriptor_is_not_abstract():
    assert not inspect.isabstract(myDsl::Descriptor)


def test_mydsl::descriptor_constructor_exists():
    assert callable(myDsl::Descriptor.__init__)


def test_mydsl::descriptor_constructor_args():
    sig = inspect.signature(myDsl::Descriptor.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::descriptor_has_path():
    assert hasattr(myDsl::Descriptor, "path")
    descriptor = None
    for klass in myDsl::Descriptor.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::descriptor_has_name():
    assert hasattr(myDsl::Descriptor, "name")
    descriptor = None
    for klass in myDsl::Descriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::library_is_not_abstract():
    assert not inspect.isabstract(myDsl::Library)


def test_mydsl::library_constructor_exists():
    assert callable(myDsl::Library.__init__)


def test_mydsl::library_constructor_args():
    sig = inspect.signature(myDsl::Library.__init__)
    params = list(sig.parameters.keys())
    assert "isNative" in params, "Missing parameter 'isNative'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::library_has_isNative():
    assert hasattr(myDsl::Library, "isNative")
    descriptor = None
    for klass in myDsl::Library.__mro__:
        if "isNative" in klass.__dict__:
            descriptor = klass.__dict__["isNative"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::library_has_name():
    assert hasattr(myDsl::Library, "name")
    descriptor = None
    for klass in myDsl::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::eclass_is_not_abstract():
    assert not inspect.isabstract(myDsl::Eclass)


def test_mydsl::eclass_constructor_exists():
    assert callable(myDsl::Eclass.__init__)


def test_mydsl::eclass_constructor_args():
    sig = inspect.signature(myDsl::Eclass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::eclass_has_name():
    assert hasattr(myDsl::Eclass, "name")
    descriptor = None
    for klass in myDsl::Eclass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::jeeproject_is_not_abstract():
    assert not inspect.isabstract(myDsl::JeeProject)


def test_mydsl::jeeproject_constructor_exists():
    assert callable(myDsl::JeeProject.__init__)


def test_mydsl::jeeproject_constructor_args():
    sig = inspect.signature(myDsl::JeeProject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::jeeproject_has_name():
    assert hasattr(myDsl::JeeProject, "name")
    descriptor = None
    for klass in myDsl::JeeProject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::javaapp_is_not_abstract():
    assert not inspect.isabstract(myDsl::JavaApp)


def test_mydsl::javaapp_constructor_exists():
    assert callable(myDsl::JavaApp.__init__)


def test_mydsl::javaapp_constructor_args():
    sig = inspect.signature(myDsl::JavaApp.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::sublayersegment_is_not_abstract():
    assert not inspect.isabstract(myDsl::SublayerSegment)


def test_mydsl::sublayersegment_constructor_exists():
    assert callable(myDsl::SublayerSegment.__init__)


def test_mydsl::sublayersegment_constructor_args():
    sig = inspect.signature(myDsl::SublayerSegment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::sublayersegment_has_name():
    assert hasattr(myDsl::SublayerSegment, "name")
    descriptor = None
    for klass in myDsl::SublayerSegment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::layersegmentrelation_is_not_abstract():
    assert not inspect.isabstract(myDsl::LayerSegmentRelation)


def test_mydsl::layersegmentrelation_constructor_exists():
    assert callable(myDsl::LayerSegmentRelation.__init__)


def test_mydsl::layersegmentrelation_constructor_args():
    sig = inspect.signature(myDsl::LayerSegmentRelation.__init__)
    params = list(sig.parameters.keys())
    assert "layerSegment" in params, "Missing parameter 'layerSegment'"

def test_mydsl::layersegmentrelation_has_layerSegment():
    assert hasattr(myDsl::LayerSegmentRelation, "layerSegment")
    descriptor = None
    for klass in myDsl::LayerSegmentRelation.__mro__:
        if "layerSegment" in klass.__dict__:
            descriptor = klass.__dict__["layerSegment"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::layersegment_is_not_abstract():
    assert not inspect.isabstract(myDsl::LayerSegment)


def test_mydsl::layersegment_constructor_exists():
    assert callable(myDsl::LayerSegment.__init__)


def test_mydsl::layersegment_constructor_args():
    sig = inspect.signature(myDsl::LayerSegment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::layersegment_has_name():
    assert hasattr(myDsl::LayerSegment, "name")
    descriptor = None
    for klass in myDsl::LayerSegment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::layer_is_not_abstract():
    assert not inspect.isabstract(myDsl::Layer)


def test_mydsl::layer_constructor_exists():
    assert callable(myDsl::Layer.__init__)


def test_mydsl::layer_constructor_args():
    sig = inspect.signature(myDsl::Layer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::layer_has_name():
    assert hasattr(myDsl::Layer, "name")
    descriptor = None
    for klass in myDsl::Layer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::relationarch_is_not_abstract():
    assert not inspect.isabstract(myDsl::RelationArch)


def test_mydsl::relationarch_constructor_exists():
    assert callable(myDsl::RelationArch.__init__)


def test_mydsl::relationarch_constructor_args():
    sig = inspect.signature(myDsl::RelationArch.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "name" in params, "Missing parameter 'name'"
    assert "target" in params, "Missing parameter 'target'"

def test_mydsl::relationarch_has_source():
    assert hasattr(myDsl::RelationArch, "source")
    descriptor = None
    for klass in myDsl::RelationArch.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::relationarch_has_name():
    assert hasattr(myDsl::RelationArch, "name")
    descriptor = None
    for klass in myDsl::RelationArch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::relationarch_has_target():
    assert hasattr(myDsl::RelationArch, "target")
    descriptor = None
    for klass in myDsl::RelationArch.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::component_is_not_abstract():
    assert not inspect.isabstract(myDsl::Component)


def test_mydsl::component_constructor_exists():
    assert callable(myDsl::Component.__init__)


def test_mydsl::component_constructor_args():
    sig = inspect.signature(myDsl::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::component_has_name():
    assert hasattr(myDsl::Component, "name")
    descriptor = None
    for klass in myDsl::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::epackage_is_not_abstract():
    assert not inspect.isabstract(myDsl::Epackage)


def test_mydsl::epackage_constructor_exists():
    assert callable(myDsl::Epackage.__init__)


def test_mydsl::epackage_constructor_args():
    sig = inspect.signature(myDsl::Epackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::epackage_has_name():
    assert hasattr(myDsl::Epackage, "name")
    descriptor = None
    for klass in myDsl::Epackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::subproject_is_not_abstract():
    assert not inspect.isabstract(myDsl::Subproject)


def test_mydsl::subproject_constructor_exists():
    assert callable(myDsl::Subproject.__init__)


def test_mydsl::subproject_constructor_args():
    sig = inspect.signature(myDsl::Subproject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::subproject_has_name():
    assert hasattr(myDsl::Subproject, "name")
    descriptor = None
    for klass in myDsl::Subproject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::operateson_is_not_abstract():
    assert not inspect.isabstract(myDsl::Operateson)


def test_mydsl::operateson_constructor_exists():
    assert callable(myDsl::Operateson.__init__)


def test_mydsl::operateson_constructor_args():
    sig = inspect.signature(myDsl::Operateson.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::transaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::Transaction)


def test_mydsl::transaction_constructor_exists():
    assert callable(myDsl::Transaction.__init__)


def test_mydsl::transaction_constructor_args():
    sig = inspect.signature(myDsl::Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl::transaction_has_type():
    assert hasattr(myDsl::Transaction, "type")
    descriptor = None
    for klass in myDsl::Transaction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::specialentity_is_not_abstract():
    assert not inspect.isabstract(myDsl::SpecialEntity)


def test_mydsl::specialentity_constructor_exists():
    assert callable(myDsl::SpecialEntity.__init__)


def test_mydsl::specialentity_constructor_args():
    sig = inspect.signature(myDsl::SpecialEntity.__init__)
    params = list(sig.parameters.keys())



def test_abstractfrontelement_is_not_abstract():
    assert not inspect.isabstract(AbstractFrontElement)


def test_abstractfrontelement_constructor_exists():
    assert callable(AbstractFrontElement.__init__)


def test_abstractfrontelement_constructor_args():
    sig = inspect.signature(AbstractFrontElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::container_is_not_abstract():
    assert not inspect.isabstract(myDsl::Container)


def test_mydsl::container_constructor_exists():
    assert callable(myDsl::Container.__init__)


def test_mydsl::container_constructor_args():
    sig = inspect.signature(myDsl::Container.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::container_has_name():
    assert hasattr(myDsl::Container, "name")
    descriptor = None
    for klass in myDsl::Container.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reactapp_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReactApp)


def test_mydsl::reactapp_constructor_exists():
    assert callable(myDsl::ReactApp.__init__)


def test_mydsl::reactapp_constructor_args():
    sig = inspect.signature(myDsl::ReactApp.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::property_is_not_abstract():
    assert not inspect.isabstract(myDsl::Property)


def test_mydsl::property_constructor_exists():
    assert callable(myDsl::Property.__init__)


def test_mydsl::property_constructor_args():
    sig = inspect.signature(myDsl::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::property_has_name():
    assert hasattr(myDsl::Property, "name")
    descriptor = None
    for klass in myDsl::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::generalentity_is_not_abstract():
    assert not inspect.isabstract(myDsl::GeneralEntity)


def test_mydsl::generalentity_constructor_exists():
    assert callable(myDsl::GeneralEntity.__init__)


def test_mydsl::generalentity_constructor_args():
    sig = inspect.signature(myDsl::GeneralEntity.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::entityname_is_not_abstract():
    assert not inspect.isabstract(myDsl::EntityName)


def test_mydsl::entityname_constructor_exists():
    assert callable(myDsl::EntityName.__init__)


def test_mydsl::entityname_constructor_args():
    sig = inspect.signature(myDsl::EntityName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::entityname_has_name():
    assert hasattr(myDsl::EntityName, "name")
    descriptor = None
    for klass in myDsl::EntityName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl::EObject)


def test_mydsl::eobject_constructor_exists():
    assert callable(myDsl::EObject.__init__)


def test_mydsl::eobject_constructor_args():
    sig = inspect.signature(myDsl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::operation_is_not_abstract():
    assert not inspect.isabstract(myDsl::Operation)


def test_mydsl::operation_constructor_exists():
    assert callable(myDsl::Operation.__init__)


def test_mydsl::operation_constructor_args():
    sig = inspect.signature(myDsl::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl::operation_has_type():
    assert hasattr(myDsl::Operation, "type")
    descriptor = None
    for klass in myDsl::Operation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::module_is_not_abstract():
    assert not inspect.isabstract(myDsl::Module)


def test_mydsl::module_constructor_exists():
    assert callable(myDsl::Module.__init__)


def test_mydsl::module_constructor_args():
    sig = inspect.signature(myDsl::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::module_has_name():
    assert hasattr(myDsl::Module, "name")
    descriptor = None
    for klass in myDsl::Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type)


def test_mydsl::type_constructor_exists():
    assert callable(myDsl::Type.__init__)


def test_mydsl::type_constructor_args():
    sig = inspect.signature(myDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::type_has_name():
    assert hasattr(myDsl::Type, "name")
    descriptor = None
    for klass in myDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::technology_is_not_abstract():
    assert not inspect.isabstract(myDsl::Technology)


def test_mydsl::technology_constructor_exists():
    assert callable(myDsl::Technology.__init__)


def test_mydsl::technology_constructor_args():
    sig = inspect.signature(myDsl::Technology.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::architecture_is_not_abstract():
    assert not inspect.isabstract(myDsl::Architecture)


def test_mydsl::architecture_constructor_exists():
    assert callable(myDsl::Architecture.__init__)


def test_mydsl::architecture_constructor_args():
    sig = inspect.signature(myDsl::Architecture.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::domain_is_not_abstract():
    assert not inspect.isabstract(myDsl::Domain)


def test_mydsl::domain_constructor_exists():
    assert callable(myDsl::Domain.__init__)


def test_mydsl::domain_constructor_args():
    sig = inspect.signature(myDsl::Domain.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::system_is_not_abstract():
    assert not inspect.isabstract(myDsl::System)


def test_mydsl::system_constructor_exists():
    assert callable(myDsl::System.__init__)


def test_mydsl::system_constructor_args():
    sig = inspect.signature(myDsl::System.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::submodule_is_not_abstract():
    assert not inspect.isabstract(myDsl::Submodule)


def test_mydsl::submodule_constructor_exists():
    assert callable(myDsl::Submodule.__init__)


def test_mydsl::submodule_constructor_args():
    sig = inspect.signature(myDsl::Submodule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::submodule_has_name():
    assert hasattr(myDsl::Submodule, "name")
    descriptor = None
    for klass in myDsl::Submodule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::relationdom_is_not_abstract():
    assert not inspect.isabstract(myDsl::RelationDom)


def test_mydsl::relationdom_constructor_exists():
    assert callable(myDsl::RelationDom.__init__)


def test_mydsl::relationdom_constructor_args():
    sig = inspect.signature(myDsl::RelationDom.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::actiondispatcher_is_not_abstract():
    assert not inspect.isabstract(myDsl::ActionDispatcher)


def test_mydsl::actiondispatcher_constructor_exists():
    assert callable(myDsl::ActionDispatcher.__init__)


def test_mydsl::actiondispatcher_constructor_args():
    sig = inspect.signature(myDsl::ActionDispatcher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::actiondispatcher_has_name():
    assert hasattr(myDsl::ActionDispatcher, "name")
    descriptor = None
    for klass in myDsl::ActionDispatcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::actioncreator_is_not_abstract():
    assert not inspect.isabstract(myDsl::ActionCreator)


def test_mydsl::actioncreator_constructor_exists():
    assert callable(myDsl::ActionCreator.__init__)


def test_mydsl::actioncreator_constructor_args():
    sig = inspect.signature(myDsl::ActionCreator.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::actioncreator_has_type():
    assert hasattr(myDsl::ActionCreator, "type")
    descriptor = None
    for klass in myDsl::ActionCreator.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::actioncreator_has_name():
    assert hasattr(myDsl::ActionCreator, "name")
    descriptor = None
    for klass in myDsl::ActionCreator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::reducer_is_not_abstract():
    assert not inspect.isabstract(myDsl::Reducer)


def test_mydsl::reducer_constructor_exists():
    assert callable(myDsl::Reducer.__init__)


def test_mydsl::reducer_constructor_args():
    sig = inspect.signature(myDsl::Reducer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::reducer_has_name():
    assert hasattr(myDsl::Reducer, "name")
    descriptor = None
    for klass in myDsl::Reducer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::action_is_not_abstract():
    assert not inspect.isabstract(myDsl::Action)


def test_mydsl::action_constructor_exists():
    assert callable(myDsl::Action.__init__)


def test_mydsl::action_constructor_args():
    sig = inspect.signature(myDsl::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::action_has_name():
    assert hasattr(myDsl::Action, "name")
    descriptor = None
    for klass in myDsl::Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_file_is_not_abstract():
    assert not inspect.isabstract(File)


def test_file_constructor_exists():
    assert callable(File.__init__)


def test_file_constructor_args():
    sig = inspect.signature(File.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::css_is_not_abstract():
    assert not inspect.isabstract(myDsl::Css)


def test_mydsl::css_constructor_exists():
    assert callable(myDsl::Css.__init__)


def test_mydsl::css_constructor_args():
    sig = inspect.signature(myDsl::Css.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::json_is_not_abstract():
    assert not inspect.isabstract(myDsl::Json)


def test_mydsl::json_constructor_exists():
    assert callable(myDsl::Json.__init__)


def test_mydsl::json_constructor_args():
    sig = inspect.signature(myDsl::Json.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::js_is_not_abstract():
    assert not inspect.isabstract(myDsl::Js)


def test_mydsl::js_constructor_exists():
    assert callable(myDsl::Js.__init__)


def test_mydsl::js_constructor_args():
    sig = inspect.signature(myDsl::Js.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::md_is_not_abstract():
    assert not inspect.isabstract(myDsl::Md)


def test_mydsl::md_constructor_exists():
    assert callable(myDsl::Md.__init__)


def test_mydsl::md_constructor_args():
    sig = inspect.signature(myDsl::Md.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::jsmethodargs_is_not_abstract():
    assert not inspect.isabstract(myDsl::JsMethodArgs)


def test_mydsl::jsmethodargs_constructor_exists():
    assert callable(myDsl::JsMethodArgs.__init__)


def test_mydsl::jsmethodargs_constructor_args():
    sig = inspect.signature(myDsl::JsMethodArgs.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::jsmethodargs_has_name():
    assert hasattr(myDsl::JsMethodArgs, "name")
    descriptor = None
    for klass in myDsl::JsMethodArgs.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::axiosrequest_is_not_abstract():
    assert not inspect.isabstract(myDsl::AxiosRequest)


def test_mydsl::axiosrequest_constructor_exists():
    assert callable(myDsl::AxiosRequest.__init__)


def test_mydsl::axiosrequest_constructor_args():
    sig = inspect.signature(myDsl::AxiosRequest.__init__)
    params = list(sig.parameters.keys())
    assert "axiosRestMethod" in params, "Missing parameter 'axiosRestMethod'"
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"

def test_mydsl::axiosrequest_has_axiosRestMethod():
    assert hasattr(myDsl::AxiosRequest, "axiosRestMethod")
    descriptor = None
    for klass in myDsl::AxiosRequest.__mro__:
        if "axiosRestMethod" in klass.__dict__:
            descriptor = klass.__dict__["axiosRestMethod"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::axiosrequest_has_name():
    assert hasattr(myDsl::AxiosRequest, "name")
    descriptor = None
    for klass in myDsl::AxiosRequest.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::axiosrequest_has_url():
    assert hasattr(myDsl::AxiosRequest, "url")
    descriptor = None
    for klass in myDsl::AxiosRequest.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::jsmethod_is_not_abstract():
    assert not inspect.isabstract(myDsl::JsMethod)


def test_mydsl::jsmethod_constructor_exists():
    assert callable(myDsl::JsMethod.__init__)


def test_mydsl::jsmethod_constructor_args():
    sig = inspect.signature(myDsl::JsMethod.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl::jsmethod_has_name():
    assert hasattr(myDsl::JsMethod, "name")
    descriptor = None
    for klass in myDsl::JsMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::jsmethod_has_type():
    assert hasattr(myDsl::JsMethod, "type")
    descriptor = None
    for klass in myDsl::JsMethod.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::uicomponent_is_not_abstract():
    assert not inspect.isabstract(myDsl::UIComponent)


def test_mydsl::uicomponent_constructor_exists():
    assert callable(myDsl::UIComponent.__init__)


def test_mydsl::uicomponent_constructor_args():
    sig = inspect.signature(myDsl::UIComponent.__init__)
    params = list(sig.parameters.keys())



def test_uicomponent_is_not_abstract():
    assert not inspect.isabstract(UIComponent)


def test_uicomponent_constructor_exists():
    assert callable(UIComponent.__init__)


def test_uicomponent_constructor_args():
    sig = inspect.signature(UIComponent.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::visualizer_is_not_abstract():
    assert not inspect.isabstract(myDsl::Visualizer)


def test_mydsl::visualizer_constructor_exists():
    assert callable(myDsl::Visualizer.__init__)


def test_mydsl::visualizer_constructor_args():
    sig = inspect.signature(myDsl::Visualizer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::visualizer_has_name():
    assert hasattr(myDsl::Visualizer, "name")
    descriptor = None
    for klass in myDsl::Visualizer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::routercomponent_is_not_abstract():
    assert not inspect.isabstract(myDsl::RouterComponent)


def test_mydsl::routercomponent_constructor_exists():
    assert callable(myDsl::RouterComponent.__init__)


def test_mydsl::routercomponent_constructor_args():
    sig = inspect.signature(myDsl::RouterComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::routercomponent_has_name():
    assert hasattr(myDsl::RouterComponent, "name")
    descriptor = None
    for klass in myDsl::RouterComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::servicefront_is_not_abstract():
    assert not inspect.isabstract(myDsl::ServiceFront)


def test_mydsl::servicefront_constructor_exists():
    assert callable(myDsl::ServiceFront.__init__)


def test_mydsl::servicefront_constructor_args():
    sig = inspect.signature(myDsl::ServiceFront.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "method" in params, "Missing parameter 'method'"

def test_mydsl::servicefront_has_name():
    assert hasattr(myDsl::ServiceFront, "name")
    descriptor = None
    for klass in myDsl::ServiceFront.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::servicefront_has_method():
    assert hasattr(myDsl::ServiceFront, "method")
    descriptor = None
    for klass in myDsl::ServiceFront.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::state_is_not_abstract():
    assert not inspect.isabstract(myDsl::State)


def test_mydsl::state_constructor_exists():
    assert callable(myDsl::State.__init__)


def test_mydsl::state_constructor_args():
    sig = inspect.signature(myDsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::state_has_name():
    assert hasattr(myDsl::State, "name")
    descriptor = None
    for klass in myDsl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::file_is_not_abstract():
    assert not inspect.isabstract(myDsl::File)


def test_mydsl::file_constructor_exists():
    assert callable(myDsl::File.__init__)


def test_mydsl::file_constructor_args():
    sig = inspect.signature(myDsl::File.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl::file_has_name():
    assert hasattr(myDsl::File, "name")
    descriptor = None
    for klass in myDsl::File.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::file_has_type():
    assert hasattr(myDsl::File, "type")
    descriptor = None
    for klass in myDsl::File.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::jsmodule_is_not_abstract():
    assert not inspect.isabstract(myDsl::JsModule)


def test_mydsl::jsmodule_constructor_exists():
    assert callable(myDsl::JsModule.__init__)


def test_mydsl::jsmodule_constructor_args():
    sig = inspect.signature(myDsl::JsModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::jsmodule_has_name():
    assert hasattr(myDsl::JsModule, "name")
    descriptor = None
    for klass in myDsl::JsModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::directory_is_not_abstract():
    assert not inspect.isabstract(myDsl::Directory)


def test_mydsl::directory_constructor_exists():
    assert callable(myDsl::Directory.__init__)


def test_mydsl::directory_constructor_args():
    sig = inspect.signature(myDsl::Directory.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "purpose" in params, "Missing parameter 'purpose'"

def test_mydsl::directory_has_name():
    assert hasattr(myDsl::Directory, "name")
    descriptor = None
    for klass in myDsl::Directory.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::directory_has_purpose():
    assert hasattr(myDsl::Directory, "purpose")
    descriptor = None
    for klass in myDsl::Directory.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::functionality_is_not_abstract():
    assert not inspect.isabstract(myDsl::Functionality)


def test_mydsl::functionality_constructor_exists():
    assert callable(myDsl::Functionality.__init__)


def test_mydsl::functionality_constructor_args():
    sig = inspect.signature(myDsl::Functionality.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::functionality_has_name():
    assert hasattr(myDsl::Functionality, "name")
    descriptor = None
    for klass in myDsl::Functionality.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
myDsl::AbstractFrontElement_strategy = st.builds(
    myDsl::AbstractFrontElement,
)
myDsl::Einterface_strategy = st.builds(
    myDsl::Einterface,
    name=
        safe_text
)
myDsl::AbstractMethod_strategy = st.builds(
    myDsl::AbstractMethod,
    name=
        safe_text
)
myDsl::MethodBack_strategy = st.builds(
    myDsl::MethodBack,
    name=
        safe_text
)
myDsl::Attribute_strategy = st.builds(
    myDsl::Attribute,
    name=
        safe_text
)
Eclass_strategy = st.builds(
    Eclass,
)
myDsl::NativeClass_strategy = st.builds(
    myDsl::NativeClass,
)
myDsl::Annotation_strategy = st.builds(
    myDsl::Annotation,
    propertie=
        safe_text
)
myDsl::GenericClass_strategy = st.builds(
    myDsl::GenericClass,
)
myDsl::AbstractClass_strategy = st.builds(
    myDsl::AbstractClass,
)
myDsl::Descriptor_strategy = st.builds(
    myDsl::Descriptor,
    path=
        safe_text,
    name=
        safe_text
)
myDsl::Library_strategy = st.builds(
    myDsl::Library,
    isNative=
        safe_text,
    name=
        safe_text
)
myDsl::Eclass_strategy = st.builds(
    myDsl::Eclass,
    name=
        safe_text
)
myDsl::JeeProject_strategy = st.builds(
    myDsl::JeeProject,
    name=
        safe_text
)
myDsl::JavaApp_strategy = st.builds(
    myDsl::JavaApp,
)
myDsl::SublayerSegment_strategy = st.builds(
    myDsl::SublayerSegment,
    name=
        safe_text
)
myDsl::LayerSegmentRelation_strategy = st.builds(
    myDsl::LayerSegmentRelation,
    layerSegment=
        safe_text
)
myDsl::LayerSegment_strategy = st.builds(
    myDsl::LayerSegment,
    name=
        safe_text
)
myDsl::Layer_strategy = st.builds(
    myDsl::Layer,
    name=
        safe_text
)
myDsl::RelationArch_strategy = st.builds(
    myDsl::RelationArch,
    source=
        safe_text,
    name=
        safe_text,
    target=
        safe_text
)
myDsl::Component_strategy = st.builds(
    myDsl::Component,
    name=
        safe_text
)
myDsl::Epackage_strategy = st.builds(
    myDsl::Epackage,
    name=
        safe_text
)
myDsl::Subproject_strategy = st.builds(
    myDsl::Subproject,
    name=
        safe_text
)
myDsl::Operateson_strategy = st.builds(
    myDsl::Operateson,
)
myDsl::Transaction_strategy = st.builds(
    myDsl::Transaction,
    type=
        safe_text
)
myDsl::SpecialEntity_strategy = st.builds(
    myDsl::SpecialEntity,
)
AbstractFrontElement_strategy = st.builds(
    AbstractFrontElement,
)
myDsl::Container_strategy = st.builds(
    myDsl::Container,
    name=
        safe_text
)
myDsl::ReactApp_strategy = st.builds(
    myDsl::ReactApp,
)
myDsl::Property_strategy = st.builds(
    myDsl::Property,
    name=
        safe_text
)
myDsl::GeneralEntity_strategy = st.builds(
    myDsl::GeneralEntity,
)
myDsl::EntityName_strategy = st.builds(
    myDsl::EntityName,
    name=
        safe_text
)
myDsl::EObject_strategy = st.builds(
    myDsl::EObject,
)
myDsl::Operation_strategy = st.builds(
    myDsl::Operation,
    type=
        safe_text
)
myDsl::Module_strategy = st.builds(
    myDsl::Module,
    name=
        safe_text
)
myDsl::Type_strategy = st.builds(
    myDsl::Type,
    name=
        safe_text
)
myDsl::Technology_strategy = st.builds(
    myDsl::Technology,
)
myDsl::Architecture_strategy = st.builds(
    myDsl::Architecture,
)
myDsl::Domain_strategy = st.builds(
    myDsl::Domain,
)
myDsl::System_strategy = st.builds(
    myDsl::System,
)
myDsl::Submodule_strategy = st.builds(
    myDsl::Submodule,
    name=
        safe_text
)
myDsl::RelationDom_strategy = st.builds(
    myDsl::RelationDom,
)
myDsl::ActionDispatcher_strategy = st.builds(
    myDsl::ActionDispatcher,
    name=
        safe_text
)
myDsl::ActionCreator_strategy = st.builds(
    myDsl::ActionCreator,
    type=
        safe_text,
    name=
        safe_text
)
myDsl::Reducer_strategy = st.builds(
    myDsl::Reducer,
    name=
        safe_text
)
myDsl::Action_strategy = st.builds(
    myDsl::Action,
    name=
        safe_text
)
File_strategy = st.builds(
    File,
)
myDsl::Css_strategy = st.builds(
    myDsl::Css,
)
myDsl::Json_strategy = st.builds(
    myDsl::Json,
)
myDsl::Js_strategy = st.builds(
    myDsl::Js,
)
myDsl::Md_strategy = st.builds(
    myDsl::Md,
)
myDsl::JsMethodArgs_strategy = st.builds(
    myDsl::JsMethodArgs,
    name=
        safe_text
)
myDsl::AxiosRequest_strategy = st.builds(
    myDsl::AxiosRequest,
    axiosRestMethod=
        safe_text,
    name=
        safe_text,
    url=
        safe_text
)
myDsl::JsMethod_strategy = st.builds(
    myDsl::JsMethod,
    name=
        safe_text,
    type=
        safe_text
)
myDsl::UIComponent_strategy = st.builds(
    myDsl::UIComponent,
)
UIComponent_strategy = st.builds(
    UIComponent,
)
myDsl::Visualizer_strategy = st.builds(
    myDsl::Visualizer,
    name=
        safe_text
)
myDsl::RouterComponent_strategy = st.builds(
    myDsl::RouterComponent,
    name=
        safe_text
)
myDsl::ServiceFront_strategy = st.builds(
    myDsl::ServiceFront,
    name=
        safe_text,
    method=
        safe_text
)
myDsl::State_strategy = st.builds(
    myDsl::State,
    name=
        safe_text
)
myDsl::File_strategy = st.builds(
    myDsl::File,
    name=
        safe_text,
    type=
        safe_text
)
myDsl::JsModule_strategy = st.builds(
    myDsl::JsModule,
    name=
        safe_text
)
myDsl::Directory_strategy = st.builds(
    myDsl::Directory,
    name=
        safe_text,
    purpose=
        safe_text
)
myDsl::Functionality_strategy = st.builds(
    myDsl::Functionality,
    name=
        safe_text
)

@given(instance=myDsl::AbstractFrontElement_strategy)
@settings(max_examples=50)
def test_mydsl::abstractfrontelement_instantiation(instance):
    assert isinstance(instance, myDsl::AbstractFrontElement)

@given(instance=myDsl::Einterface_strategy)
@settings(max_examples=50)
def test_mydsl::einterface_instantiation(instance):
    assert isinstance(instance, myDsl::Einterface)

@given(instance=myDsl::Einterface_strategy)
def test_mydsl::einterface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Einterface_strategy)
def test_mydsl::einterface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::AbstractMethod_strategy)
@settings(max_examples=50)
def test_mydsl::abstractmethod_instantiation(instance):
    assert isinstance(instance, myDsl::AbstractMethod)

@given(instance=myDsl::AbstractMethod_strategy)
def test_mydsl::abstractmethod_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::AbstractMethod_strategy)
def test_mydsl::abstractmethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::MethodBack_strategy)
@settings(max_examples=50)
def test_mydsl::methodback_instantiation(instance):
    assert isinstance(instance, myDsl::MethodBack)

@given(instance=myDsl::MethodBack_strategy)
def test_mydsl::methodback_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::MethodBack_strategy)
def test_mydsl::methodback_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Attribute_strategy)
@settings(max_examples=50)
def test_mydsl::attribute_instantiation(instance):
    assert isinstance(instance, myDsl::Attribute)

@given(instance=myDsl::Attribute_strategy)
def test_mydsl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Attribute_strategy)
def test_mydsl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Eclass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, Eclass)

@given(instance=myDsl::NativeClass_strategy)
@settings(max_examples=50)
def test_mydsl::nativeclass_instantiation(instance):
    assert isinstance(instance, myDsl::NativeClass)

@given(instance=myDsl::Annotation_strategy)
@settings(max_examples=50)
def test_mydsl::annotation_instantiation(instance):
    assert isinstance(instance, myDsl::Annotation)

@given(instance=myDsl::Annotation_strategy)
def test_mydsl::annotation_propertie_type(instance):
    assert isinstance(instance.propertie, str)


@given(instance=myDsl::Annotation_strategy)
def test_mydsl::annotation_propertie_setter(instance):
    original = instance.propertie
    instance.propertie = original
    assert instance.propertie == original

@given(instance=myDsl::GenericClass_strategy)
@settings(max_examples=50)
def test_mydsl::genericclass_instantiation(instance):
    assert isinstance(instance, myDsl::GenericClass)

@given(instance=myDsl::AbstractClass_strategy)
@settings(max_examples=50)
def test_mydsl::abstractclass_instantiation(instance):
    assert isinstance(instance, myDsl::AbstractClass)

@given(instance=myDsl::Descriptor_strategy)
@settings(max_examples=50)
def test_mydsl::descriptor_instantiation(instance):
    assert isinstance(instance, myDsl::Descriptor)

@given(instance=myDsl::Descriptor_strategy)
def test_mydsl::descriptor_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=myDsl::Descriptor_strategy)
def test_mydsl::descriptor_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=myDsl::Descriptor_strategy)
def test_mydsl::descriptor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Descriptor_strategy)
def test_mydsl::descriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Library_strategy)
@settings(max_examples=50)
def test_mydsl::library_instantiation(instance):
    assert isinstance(instance, myDsl::Library)

@given(instance=myDsl::Library_strategy)
def test_mydsl::library_isNative_type(instance):
    assert isinstance(instance.isNative, str)


@given(instance=myDsl::Library_strategy)
def test_mydsl::library_isNative_setter(instance):
    original = instance.isNative
    instance.isNative = original
    assert instance.isNative == original

@given(instance=myDsl::Library_strategy)
def test_mydsl::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Library_strategy)
def test_mydsl::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Eclass_strategy)
@settings(max_examples=50)
def test_mydsl::eclass_instantiation(instance):
    assert isinstance(instance, myDsl::Eclass)

@given(instance=myDsl::Eclass_strategy)
def test_mydsl::eclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Eclass_strategy)
def test_mydsl::eclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::JeeProject_strategy)
@settings(max_examples=50)
def test_mydsl::jeeproject_instantiation(instance):
    assert isinstance(instance, myDsl::JeeProject)

@given(instance=myDsl::JeeProject_strategy)
def test_mydsl::jeeproject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::JeeProject_strategy)
def test_mydsl::jeeproject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::JavaApp_strategy)
@settings(max_examples=50)
def test_mydsl::javaapp_instantiation(instance):
    assert isinstance(instance, myDsl::JavaApp)

@given(instance=myDsl::SublayerSegment_strategy)
@settings(max_examples=50)
def test_mydsl::sublayersegment_instantiation(instance):
    assert isinstance(instance, myDsl::SublayerSegment)

@given(instance=myDsl::SublayerSegment_strategy)
def test_mydsl::sublayersegment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::SublayerSegment_strategy)
def test_mydsl::sublayersegment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::LayerSegmentRelation_strategy)
@settings(max_examples=50)
def test_mydsl::layersegmentrelation_instantiation(instance):
    assert isinstance(instance, myDsl::LayerSegmentRelation)

@given(instance=myDsl::LayerSegmentRelation_strategy)
def test_mydsl::layersegmentrelation_layerSegment_type(instance):
    assert isinstance(instance.layerSegment, str)


@given(instance=myDsl::LayerSegmentRelation_strategy)
def test_mydsl::layersegmentrelation_layerSegment_setter(instance):
    original = instance.layerSegment
    instance.layerSegment = original
    assert instance.layerSegment == original

@given(instance=myDsl::LayerSegment_strategy)
@settings(max_examples=50)
def test_mydsl::layersegment_instantiation(instance):
    assert isinstance(instance, myDsl::LayerSegment)

@given(instance=myDsl::LayerSegment_strategy)
def test_mydsl::layersegment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::LayerSegment_strategy)
def test_mydsl::layersegment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Layer_strategy)
@settings(max_examples=50)
def test_mydsl::layer_instantiation(instance):
    assert isinstance(instance, myDsl::Layer)

@given(instance=myDsl::Layer_strategy)
def test_mydsl::layer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Layer_strategy)
def test_mydsl::layer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::RelationArch_strategy)
@settings(max_examples=50)
def test_mydsl::relationarch_instantiation(instance):
    assert isinstance(instance, myDsl::RelationArch)

@given(instance=myDsl::RelationArch_strategy)
def test_mydsl::relationarch_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=myDsl::RelationArch_strategy)
def test_mydsl::relationarch_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=myDsl::RelationArch_strategy)
def test_mydsl::relationarch_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::RelationArch_strategy)
def test_mydsl::relationarch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::RelationArch_strategy)
def test_mydsl::relationarch_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=myDsl::RelationArch_strategy)
def test_mydsl::relationarch_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=myDsl::Component_strategy)
@settings(max_examples=50)
def test_mydsl::component_instantiation(instance):
    assert isinstance(instance, myDsl::Component)

@given(instance=myDsl::Component_strategy)
def test_mydsl::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Component_strategy)
def test_mydsl::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Epackage_strategy)
@settings(max_examples=50)
def test_mydsl::epackage_instantiation(instance):
    assert isinstance(instance, myDsl::Epackage)

@given(instance=myDsl::Epackage_strategy)
def test_mydsl::epackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Epackage_strategy)
def test_mydsl::epackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Subproject_strategy)
@settings(max_examples=50)
def test_mydsl::subproject_instantiation(instance):
    assert isinstance(instance, myDsl::Subproject)

@given(instance=myDsl::Subproject_strategy)
def test_mydsl::subproject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Subproject_strategy)
def test_mydsl::subproject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Operateson_strategy)
@settings(max_examples=50)
def test_mydsl::operateson_instantiation(instance):
    assert isinstance(instance, myDsl::Operateson)

@given(instance=myDsl::Transaction_strategy)
@settings(max_examples=50)
def test_mydsl::transaction_instantiation(instance):
    assert isinstance(instance, myDsl::Transaction)

@given(instance=myDsl::Transaction_strategy)
def test_mydsl::transaction_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myDsl::Transaction_strategy)
def test_mydsl::transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl::SpecialEntity_strategy)
@settings(max_examples=50)
def test_mydsl::specialentity_instantiation(instance):
    assert isinstance(instance, myDsl::SpecialEntity)

@given(instance=AbstractFrontElement_strategy)
@settings(max_examples=50)
def test_abstractfrontelement_instantiation(instance):
    assert isinstance(instance, AbstractFrontElement)

@given(instance=myDsl::Container_strategy)
@settings(max_examples=50)
def test_mydsl::container_instantiation(instance):
    assert isinstance(instance, myDsl::Container)

@given(instance=myDsl::Container_strategy)
def test_mydsl::container_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Container_strategy)
def test_mydsl::container_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ReactApp_strategy)
@settings(max_examples=50)
def test_mydsl::reactapp_instantiation(instance):
    assert isinstance(instance, myDsl::ReactApp)

@given(instance=myDsl::Property_strategy)
@settings(max_examples=50)
def test_mydsl::property_instantiation(instance):
    assert isinstance(instance, myDsl::Property)

@given(instance=myDsl::Property_strategy)
def test_mydsl::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Property_strategy)
def test_mydsl::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::GeneralEntity_strategy)
@settings(max_examples=50)
def test_mydsl::generalentity_instantiation(instance):
    assert isinstance(instance, myDsl::GeneralEntity)

@given(instance=myDsl::EntityName_strategy)
@settings(max_examples=50)
def test_mydsl::entityname_instantiation(instance):
    assert isinstance(instance, myDsl::EntityName)

@given(instance=myDsl::EntityName_strategy)
def test_mydsl::entityname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::EntityName_strategy)
def test_mydsl::entityname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::EObject_strategy)
@settings(max_examples=50)
def test_mydsl::eobject_instantiation(instance):
    assert isinstance(instance, myDsl::EObject)

@given(instance=myDsl::Operation_strategy)
@settings(max_examples=50)
def test_mydsl::operation_instantiation(instance):
    assert isinstance(instance, myDsl::Operation)

@given(instance=myDsl::Operation_strategy)
def test_mydsl::operation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myDsl::Operation_strategy)
def test_mydsl::operation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl::Module_strategy)
@settings(max_examples=50)
def test_mydsl::module_instantiation(instance):
    assert isinstance(instance, myDsl::Module)

@given(instance=myDsl::Module_strategy)
def test_mydsl::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Module_strategy)
def test_mydsl::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Type_strategy)
@settings(max_examples=50)
def test_mydsl::type_instantiation(instance):
    assert isinstance(instance, myDsl::Type)

@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Technology_strategy)
@settings(max_examples=50)
def test_mydsl::technology_instantiation(instance):
    assert isinstance(instance, myDsl::Technology)

@given(instance=myDsl::Architecture_strategy)
@settings(max_examples=50)
def test_mydsl::architecture_instantiation(instance):
    assert isinstance(instance, myDsl::Architecture)

@given(instance=myDsl::Domain_strategy)
@settings(max_examples=50)
def test_mydsl::domain_instantiation(instance):
    assert isinstance(instance, myDsl::Domain)

@given(instance=myDsl::System_strategy)
@settings(max_examples=50)
def test_mydsl::system_instantiation(instance):
    assert isinstance(instance, myDsl::System)

@given(instance=myDsl::Submodule_strategy)
@settings(max_examples=50)
def test_mydsl::submodule_instantiation(instance):
    assert isinstance(instance, myDsl::Submodule)

@given(instance=myDsl::Submodule_strategy)
def test_mydsl::submodule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Submodule_strategy)
def test_mydsl::submodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::RelationDom_strategy)
@settings(max_examples=50)
def test_mydsl::relationdom_instantiation(instance):
    assert isinstance(instance, myDsl::RelationDom)

@given(instance=myDsl::ActionDispatcher_strategy)
@settings(max_examples=50)
def test_mydsl::actiondispatcher_instantiation(instance):
    assert isinstance(instance, myDsl::ActionDispatcher)

@given(instance=myDsl::ActionDispatcher_strategy)
def test_mydsl::actiondispatcher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ActionDispatcher_strategy)
def test_mydsl::actiondispatcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ActionCreator_strategy)
@settings(max_examples=50)
def test_mydsl::actioncreator_instantiation(instance):
    assert isinstance(instance, myDsl::ActionCreator)

@given(instance=myDsl::ActionCreator_strategy)
def test_mydsl::actioncreator_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myDsl::ActionCreator_strategy)
def test_mydsl::actioncreator_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl::ActionCreator_strategy)
def test_mydsl::actioncreator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ActionCreator_strategy)
def test_mydsl::actioncreator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Reducer_strategy)
@settings(max_examples=50)
def test_mydsl::reducer_instantiation(instance):
    assert isinstance(instance, myDsl::Reducer)

@given(instance=myDsl::Reducer_strategy)
def test_mydsl::reducer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Reducer_strategy)
def test_mydsl::reducer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Action_strategy)
@settings(max_examples=50)
def test_mydsl::action_instantiation(instance):
    assert isinstance(instance, myDsl::Action)

@given(instance=myDsl::Action_strategy)
def test_mydsl::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Action_strategy)
def test_mydsl::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=File_strategy)
@settings(max_examples=50)
def test_file_instantiation(instance):
    assert isinstance(instance, File)

@given(instance=myDsl::Css_strategy)
@settings(max_examples=50)
def test_mydsl::css_instantiation(instance):
    assert isinstance(instance, myDsl::Css)

@given(instance=myDsl::Json_strategy)
@settings(max_examples=50)
def test_mydsl::json_instantiation(instance):
    assert isinstance(instance, myDsl::Json)

@given(instance=myDsl::Js_strategy)
@settings(max_examples=50)
def test_mydsl::js_instantiation(instance):
    assert isinstance(instance, myDsl::Js)

@given(instance=myDsl::Md_strategy)
@settings(max_examples=50)
def test_mydsl::md_instantiation(instance):
    assert isinstance(instance, myDsl::Md)

@given(instance=myDsl::JsMethodArgs_strategy)
@settings(max_examples=50)
def test_mydsl::jsmethodargs_instantiation(instance):
    assert isinstance(instance, myDsl::JsMethodArgs)

@given(instance=myDsl::JsMethodArgs_strategy)
def test_mydsl::jsmethodargs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::JsMethodArgs_strategy)
def test_mydsl::jsmethodargs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::AxiosRequest_strategy)
@settings(max_examples=50)
def test_mydsl::axiosrequest_instantiation(instance):
    assert isinstance(instance, myDsl::AxiosRequest)

@given(instance=myDsl::AxiosRequest_strategy)
def test_mydsl::axiosrequest_axiosRestMethod_type(instance):
    assert isinstance(instance.axiosRestMethod, str)


@given(instance=myDsl::AxiosRequest_strategy)
def test_mydsl::axiosrequest_axiosRestMethod_setter(instance):
    original = instance.axiosRestMethod
    instance.axiosRestMethod = original
    assert instance.axiosRestMethod == original

@given(instance=myDsl::AxiosRequest_strategy)
def test_mydsl::axiosrequest_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::AxiosRequest_strategy)
def test_mydsl::axiosrequest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::AxiosRequest_strategy)
def test_mydsl::axiosrequest_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=myDsl::AxiosRequest_strategy)
def test_mydsl::axiosrequest_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=myDsl::JsMethod_strategy)
@settings(max_examples=50)
def test_mydsl::jsmethod_instantiation(instance):
    assert isinstance(instance, myDsl::JsMethod)

@given(instance=myDsl::JsMethod_strategy)
def test_mydsl::jsmethod_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::JsMethod_strategy)
def test_mydsl::jsmethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::JsMethod_strategy)
def test_mydsl::jsmethod_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myDsl::JsMethod_strategy)
def test_mydsl::jsmethod_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl::UIComponent_strategy)
@settings(max_examples=50)
def test_mydsl::uicomponent_instantiation(instance):
    assert isinstance(instance, myDsl::UIComponent)

@given(instance=UIComponent_strategy)
@settings(max_examples=50)
def test_uicomponent_instantiation(instance):
    assert isinstance(instance, UIComponent)

@given(instance=myDsl::Visualizer_strategy)
@settings(max_examples=50)
def test_mydsl::visualizer_instantiation(instance):
    assert isinstance(instance, myDsl::Visualizer)

@given(instance=myDsl::Visualizer_strategy)
def test_mydsl::visualizer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Visualizer_strategy)
def test_mydsl::visualizer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::RouterComponent_strategy)
@settings(max_examples=50)
def test_mydsl::routercomponent_instantiation(instance):
    assert isinstance(instance, myDsl::RouterComponent)

@given(instance=myDsl::RouterComponent_strategy)
def test_mydsl::routercomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::RouterComponent_strategy)
def test_mydsl::routercomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ServiceFront_strategy)
@settings(max_examples=50)
def test_mydsl::servicefront_instantiation(instance):
    assert isinstance(instance, myDsl::ServiceFront)

@given(instance=myDsl::ServiceFront_strategy)
def test_mydsl::servicefront_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::ServiceFront_strategy)
def test_mydsl::servicefront_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::ServiceFront_strategy)
def test_mydsl::servicefront_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=myDsl::ServiceFront_strategy)
def test_mydsl::servicefront_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=myDsl::State_strategy)
@settings(max_examples=50)
def test_mydsl::state_instantiation(instance):
    assert isinstance(instance, myDsl::State)

@given(instance=myDsl::State_strategy)
def test_mydsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::State_strategy)
def test_mydsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::File_strategy)
@settings(max_examples=50)
def test_mydsl::file_instantiation(instance):
    assert isinstance(instance, myDsl::File)

@given(instance=myDsl::File_strategy)
def test_mydsl::file_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::File_strategy)
def test_mydsl::file_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::File_strategy)
def test_mydsl::file_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myDsl::File_strategy)
def test_mydsl::file_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl::JsModule_strategy)
@settings(max_examples=50)
def test_mydsl::jsmodule_instantiation(instance):
    assert isinstance(instance, myDsl::JsModule)

@given(instance=myDsl::JsModule_strategy)
def test_mydsl::jsmodule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::JsModule_strategy)
def test_mydsl::jsmodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Directory_strategy)
@settings(max_examples=50)
def test_mydsl::directory_instantiation(instance):
    assert isinstance(instance, myDsl::Directory)

@given(instance=myDsl::Directory_strategy)
def test_mydsl::directory_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Directory_strategy)
def test_mydsl::directory_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Directory_strategy)
def test_mydsl::directory_purpose_type(instance):
    assert isinstance(instance.purpose, str)


@given(instance=myDsl::Directory_strategy)
def test_mydsl::directory_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original

@given(instance=myDsl::Functionality_strategy)
@settings(max_examples=50)
def test_mydsl::functionality_instantiation(instance):
    assert isinstance(instance, myDsl::Functionality)

@given(instance=myDsl::Functionality_strategy)
def test_mydsl::functionality_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Functionality_strategy)
def test_mydsl::functionality_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
