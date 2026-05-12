import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    File,
    myDsl_Css,
    myDsl_Json,
    myDsl_Js,
    myDsl_Md,
    myDsl_JsMethodArgs,
    myDsl_JsMethod,
    myDsl_UIComponent,
    UIComponent,
    myDsl_AbstractFrontElement,
    myDsl_Einterface,
    myDsl_AbstractMethod,
    myDsl_MethodBack,
    myDsl_Attribute,
    Eclass,
    myDsl_Annotation,
    myDsl_NativeClass,
    myDsl_GenericClass,
    myDsl_AbstractClass,
    myDsl_Descriptor,
    myDsl_Library,
    myDsl_Eclass,
    myDsl_JeeProject,
    myDsl_JavaApp,
    myDsl_SublayerSegment,
    myDsl_LayerSegmentRelation,
    myDsl_LayerSegment,
    myDsl_Layer,
    myDsl_RelationArch,
    myDsl_Component,
    myDsl_Epackage,
    myDsl_Subproject,
    myDsl_Operateson,
    myDsl_Transaction,
    myDsl_SpecialEntity,
    AbstractFrontElement,
    myDsl_ActionDispatcher,
    myDsl_Visualizer,
    myDsl_Action,
    myDsl_ServiceFront,
    myDsl_AxiosRequest,
    myDsl_File,
    myDsl_RouterComponent,
    myDsl_Directory,
    myDsl_Functionality,
    myDsl_Reducer,
    myDsl_ReactApp,
    myDsl_JsModule,
    myDsl_ActionCreator,
    myDsl_Container,
    myDsl_State,
    myDsl_Property,
    myDsl_GeneralEntity,
    myDsl_EntityName,
    myDsl_EObject,
    myDsl_Operation,
    myDsl_Module,
    myDsl_Type,
    myDsl_Technology,
    myDsl_Architecture,
    myDsl_Domain,
    myDsl_System,
    myDsl_Submodule,
    myDsl_RelationDom,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_file_is_not_abstract():
    assert not inspect.isabstract(File)


def test_file_constructor_exists():
    assert callable(File.__init__)


def test_file_constructor_args():
    sig = inspect.signature(File.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_css_is_not_abstract():
    assert not inspect.isabstract(myDsl_Css)


def test_mydsl_css_constructor_exists():
    assert callable(myDsl_Css.__init__)


def test_mydsl_css_constructor_args():
    sig = inspect.signature(myDsl_Css.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_json_is_not_abstract():
    assert not inspect.isabstract(myDsl_Json)


def test_mydsl_json_constructor_exists():
    assert callable(myDsl_Json.__init__)


def test_mydsl_json_constructor_args():
    sig = inspect.signature(myDsl_Json.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_js_is_not_abstract():
    assert not inspect.isabstract(myDsl_Js)


def test_mydsl_js_constructor_exists():
    assert callable(myDsl_Js.__init__)


def test_mydsl_js_constructor_args():
    sig = inspect.signature(myDsl_Js.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_md_is_not_abstract():
    assert not inspect.isabstract(myDsl_Md)


def test_mydsl_md_constructor_exists():
    assert callable(myDsl_Md.__init__)


def test_mydsl_md_constructor_args():
    sig = inspect.signature(myDsl_Md.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_jsmethodargs_is_not_abstract():
    assert not inspect.isabstract(myDsl_JsMethodArgs)


def test_mydsl_jsmethodargs_constructor_exists():
    assert callable(myDsl_JsMethodArgs.__init__)


def test_mydsl_jsmethodargs_constructor_args():
    sig = inspect.signature(myDsl_JsMethodArgs.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_jsmethodargs_has_name():
    assert hasattr(myDsl_JsMethodArgs, "name")
    descriptor = None
    for klass in myDsl_JsMethodArgs.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_jsmethod_is_not_abstract():
    assert not inspect.isabstract(myDsl_JsMethod)


def test_mydsl_jsmethod_constructor_exists():
    assert callable(myDsl_JsMethod.__init__)


def test_mydsl_jsmethod_constructor_args():
    sig = inspect.signature(myDsl_JsMethod.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_jsmethod_has_type():
    assert hasattr(myDsl_JsMethod, "type")
    descriptor = None
    for klass in myDsl_JsMethod.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_jsmethod_has_name():
    assert hasattr(myDsl_JsMethod, "name")
    descriptor = None
    for klass in myDsl_JsMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_uicomponent_is_not_abstract():
    assert not inspect.isabstract(myDsl_UIComponent)


def test_mydsl_uicomponent_constructor_exists():
    assert callable(myDsl_UIComponent.__init__)


def test_mydsl_uicomponent_constructor_args():
    sig = inspect.signature(myDsl_UIComponent.__init__)
    params = list(sig.parameters.keys())



def test_uicomponent_is_not_abstract():
    assert not inspect.isabstract(UIComponent)


def test_uicomponent_constructor_exists():
    assert callable(UIComponent.__init__)


def test_uicomponent_constructor_args():
    sig = inspect.signature(UIComponent.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_abstractfrontelement_is_not_abstract():
    assert not inspect.isabstract(myDsl_AbstractFrontElement)


def test_mydsl_abstractfrontelement_constructor_exists():
    assert callable(myDsl_AbstractFrontElement.__init__)


def test_mydsl_abstractfrontelement_constructor_args():
    sig = inspect.signature(myDsl_AbstractFrontElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_einterface_is_not_abstract():
    assert not inspect.isabstract(myDsl_Einterface)


def test_mydsl_einterface_constructor_exists():
    assert callable(myDsl_Einterface.__init__)


def test_mydsl_einterface_constructor_args():
    sig = inspect.signature(myDsl_Einterface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_einterface_has_name():
    assert hasattr(myDsl_Einterface, "name")
    descriptor = None
    for klass in myDsl_Einterface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_abstractmethod_is_not_abstract():
    assert not inspect.isabstract(myDsl_AbstractMethod)


def test_mydsl_abstractmethod_constructor_exists():
    assert callable(myDsl_AbstractMethod.__init__)


def test_mydsl_abstractmethod_constructor_args():
    sig = inspect.signature(myDsl_AbstractMethod.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_abstractmethod_has_name():
    assert hasattr(myDsl_AbstractMethod, "name")
    descriptor = None
    for klass in myDsl_AbstractMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_methodback_is_not_abstract():
    assert not inspect.isabstract(myDsl_MethodBack)


def test_mydsl_methodback_constructor_exists():
    assert callable(myDsl_MethodBack.__init__)


def test_mydsl_methodback_constructor_args():
    sig = inspect.signature(myDsl_MethodBack.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_methodback_has_name():
    assert hasattr(myDsl_MethodBack, "name")
    descriptor = None
    for klass in myDsl_MethodBack.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl_Attribute)


def test_mydsl_attribute_constructor_exists():
    assert callable(myDsl_Attribute.__init__)


def test_mydsl_attribute_constructor_args():
    sig = inspect.signature(myDsl_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_attribute_has_name():
    assert hasattr(myDsl_Attribute, "name")
    descriptor = None
    for klass in myDsl_Attribute.__mro__:
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



def test_mydsl_annotation_is_not_abstract():
    assert not inspect.isabstract(myDsl_Annotation)


def test_mydsl_annotation_constructor_exists():
    assert callable(myDsl_Annotation.__init__)


def test_mydsl_annotation_constructor_args():
    sig = inspect.signature(myDsl_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "propertie" in params, "Missing parameter 'propertie'"

def test_mydsl_annotation_has_propertie():
    assert hasattr(myDsl_Annotation, "propertie")
    descriptor = None
    for klass in myDsl_Annotation.__mro__:
        if "propertie" in klass.__dict__:
            descriptor = klass.__dict__["propertie"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_nativeclass_is_not_abstract():
    assert not inspect.isabstract(myDsl_NativeClass)


def test_mydsl_nativeclass_constructor_exists():
    assert callable(myDsl_NativeClass.__init__)


def test_mydsl_nativeclass_constructor_args():
    sig = inspect.signature(myDsl_NativeClass.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_genericclass_is_not_abstract():
    assert not inspect.isabstract(myDsl_GenericClass)


def test_mydsl_genericclass_constructor_exists():
    assert callable(myDsl_GenericClass.__init__)


def test_mydsl_genericclass_constructor_args():
    sig = inspect.signature(myDsl_GenericClass.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_abstractclass_is_not_abstract():
    assert not inspect.isabstract(myDsl_AbstractClass)


def test_mydsl_abstractclass_constructor_exists():
    assert callable(myDsl_AbstractClass.__init__)


def test_mydsl_abstractclass_constructor_args():
    sig = inspect.signature(myDsl_AbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_descriptor_is_not_abstract():
    assert not inspect.isabstract(myDsl_Descriptor)


def test_mydsl_descriptor_constructor_exists():
    assert callable(myDsl_Descriptor.__init__)


def test_mydsl_descriptor_constructor_args():
    sig = inspect.signature(myDsl_Descriptor.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_descriptor_has_path():
    assert hasattr(myDsl_Descriptor, "path")
    descriptor = None
    for klass in myDsl_Descriptor.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_descriptor_has_name():
    assert hasattr(myDsl_Descriptor, "name")
    descriptor = None
    for klass in myDsl_Descriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_library_is_not_abstract():
    assert not inspect.isabstract(myDsl_Library)


def test_mydsl_library_constructor_exists():
    assert callable(myDsl_Library.__init__)


def test_mydsl_library_constructor_args():
    sig = inspect.signature(myDsl_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isNative" in params, "Missing parameter 'isNative'"

def test_mydsl_library_has_name():
    assert hasattr(myDsl_Library, "name")
    descriptor = None
    for klass in myDsl_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_library_has_isNative():
    assert hasattr(myDsl_Library, "isNative")
    descriptor = None
    for klass in myDsl_Library.__mro__:
        if "isNative" in klass.__dict__:
            descriptor = klass.__dict__["isNative"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_eclass_is_not_abstract():
    assert not inspect.isabstract(myDsl_Eclass)


def test_mydsl_eclass_constructor_exists():
    assert callable(myDsl_Eclass.__init__)


def test_mydsl_eclass_constructor_args():
    sig = inspect.signature(myDsl_Eclass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_eclass_has_name():
    assert hasattr(myDsl_Eclass, "name")
    descriptor = None
    for klass in myDsl_Eclass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_jeeproject_is_not_abstract():
    assert not inspect.isabstract(myDsl_JeeProject)


def test_mydsl_jeeproject_constructor_exists():
    assert callable(myDsl_JeeProject.__init__)


def test_mydsl_jeeproject_constructor_args():
    sig = inspect.signature(myDsl_JeeProject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_jeeproject_has_name():
    assert hasattr(myDsl_JeeProject, "name")
    descriptor = None
    for klass in myDsl_JeeProject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_javaapp_is_not_abstract():
    assert not inspect.isabstract(myDsl_JavaApp)


def test_mydsl_javaapp_constructor_exists():
    assert callable(myDsl_JavaApp.__init__)


def test_mydsl_javaapp_constructor_args():
    sig = inspect.signature(myDsl_JavaApp.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_sublayersegment_is_not_abstract():
    assert not inspect.isabstract(myDsl_SublayerSegment)


def test_mydsl_sublayersegment_constructor_exists():
    assert callable(myDsl_SublayerSegment.__init__)


def test_mydsl_sublayersegment_constructor_args():
    sig = inspect.signature(myDsl_SublayerSegment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_sublayersegment_has_name():
    assert hasattr(myDsl_SublayerSegment, "name")
    descriptor = None
    for klass in myDsl_SublayerSegment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_layersegmentrelation_is_not_abstract():
    assert not inspect.isabstract(myDsl_LayerSegmentRelation)


def test_mydsl_layersegmentrelation_constructor_exists():
    assert callable(myDsl_LayerSegmentRelation.__init__)


def test_mydsl_layersegmentrelation_constructor_args():
    sig = inspect.signature(myDsl_LayerSegmentRelation.__init__)
    params = list(sig.parameters.keys())
    assert "layerSegment" in params, "Missing parameter 'layerSegment'"

def test_mydsl_layersegmentrelation_has_layerSegment():
    assert hasattr(myDsl_LayerSegmentRelation, "layerSegment")
    descriptor = None
    for klass in myDsl_LayerSegmentRelation.__mro__:
        if "layerSegment" in klass.__dict__:
            descriptor = klass.__dict__["layerSegment"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_layersegment_is_not_abstract():
    assert not inspect.isabstract(myDsl_LayerSegment)


def test_mydsl_layersegment_constructor_exists():
    assert callable(myDsl_LayerSegment.__init__)


def test_mydsl_layersegment_constructor_args():
    sig = inspect.signature(myDsl_LayerSegment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_layersegment_has_name():
    assert hasattr(myDsl_LayerSegment, "name")
    descriptor = None
    for klass in myDsl_LayerSegment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_layer_is_not_abstract():
    assert not inspect.isabstract(myDsl_Layer)


def test_mydsl_layer_constructor_exists():
    assert callable(myDsl_Layer.__init__)


def test_mydsl_layer_constructor_args():
    sig = inspect.signature(myDsl_Layer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_layer_has_name():
    assert hasattr(myDsl_Layer, "name")
    descriptor = None
    for klass in myDsl_Layer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_relationarch_is_not_abstract():
    assert not inspect.isabstract(myDsl_RelationArch)


def test_mydsl_relationarch_constructor_exists():
    assert callable(myDsl_RelationArch.__init__)


def test_mydsl_relationarch_constructor_args():
    sig = inspect.signature(myDsl_RelationArch.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "name" in params, "Missing parameter 'name'"
    assert "target" in params, "Missing parameter 'target'"

def test_mydsl_relationarch_has_source():
    assert hasattr(myDsl_RelationArch, "source")
    descriptor = None
    for klass in myDsl_RelationArch.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_relationarch_has_name():
    assert hasattr(myDsl_RelationArch, "name")
    descriptor = None
    for klass in myDsl_RelationArch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_relationarch_has_target():
    assert hasattr(myDsl_RelationArch, "target")
    descriptor = None
    for klass in myDsl_RelationArch.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_component_is_not_abstract():
    assert not inspect.isabstract(myDsl_Component)


def test_mydsl_component_constructor_exists():
    assert callable(myDsl_Component.__init__)


def test_mydsl_component_constructor_args():
    sig = inspect.signature(myDsl_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_component_has_name():
    assert hasattr(myDsl_Component, "name")
    descriptor = None
    for klass in myDsl_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_epackage_is_not_abstract():
    assert not inspect.isabstract(myDsl_Epackage)


def test_mydsl_epackage_constructor_exists():
    assert callable(myDsl_Epackage.__init__)


def test_mydsl_epackage_constructor_args():
    sig = inspect.signature(myDsl_Epackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_epackage_has_name():
    assert hasattr(myDsl_Epackage, "name")
    descriptor = None
    for klass in myDsl_Epackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_subproject_is_not_abstract():
    assert not inspect.isabstract(myDsl_Subproject)


def test_mydsl_subproject_constructor_exists():
    assert callable(myDsl_Subproject.__init__)


def test_mydsl_subproject_constructor_args():
    sig = inspect.signature(myDsl_Subproject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_subproject_has_name():
    assert hasattr(myDsl_Subproject, "name")
    descriptor = None
    for klass in myDsl_Subproject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_operateson_is_not_abstract():
    assert not inspect.isabstract(myDsl_Operateson)


def test_mydsl_operateson_constructor_exists():
    assert callable(myDsl_Operateson.__init__)


def test_mydsl_operateson_constructor_args():
    sig = inspect.signature(myDsl_Operateson.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_transaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_Transaction)


def test_mydsl_transaction_constructor_exists():
    assert callable(myDsl_Transaction.__init__)


def test_mydsl_transaction_constructor_args():
    sig = inspect.signature(myDsl_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl_transaction_has_type():
    assert hasattr(myDsl_Transaction, "type")
    descriptor = None
    for klass in myDsl_Transaction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_specialentity_is_not_abstract():
    assert not inspect.isabstract(myDsl_SpecialEntity)


def test_mydsl_specialentity_constructor_exists():
    assert callable(myDsl_SpecialEntity.__init__)


def test_mydsl_specialentity_constructor_args():
    sig = inspect.signature(myDsl_SpecialEntity.__init__)
    params = list(sig.parameters.keys())



def test_abstractfrontelement_is_not_abstract():
    assert not inspect.isabstract(AbstractFrontElement)


def test_abstractfrontelement_constructor_exists():
    assert callable(AbstractFrontElement.__init__)


def test_abstractfrontelement_constructor_args():
    sig = inspect.signature(AbstractFrontElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_actiondispatcher_is_not_abstract():
    assert not inspect.isabstract(myDsl_ActionDispatcher)


def test_mydsl_actiondispatcher_constructor_exists():
    assert callable(myDsl_ActionDispatcher.__init__)


def test_mydsl_actiondispatcher_constructor_args():
    sig = inspect.signature(myDsl_ActionDispatcher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_actiondispatcher_has_name():
    assert hasattr(myDsl_ActionDispatcher, "name")
    descriptor = None
    for klass in myDsl_ActionDispatcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_visualizer_is_not_abstract():
    assert not inspect.isabstract(myDsl_Visualizer)


def test_mydsl_visualizer_constructor_exists():
    assert callable(myDsl_Visualizer.__init__)


def test_mydsl_visualizer_constructor_args():
    sig = inspect.signature(myDsl_Visualizer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_visualizer_has_name():
    assert hasattr(myDsl_Visualizer, "name")
    descriptor = None
    for klass in myDsl_Visualizer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_action_is_not_abstract():
    assert not inspect.isabstract(myDsl_Action)


def test_mydsl_action_constructor_exists():
    assert callable(myDsl_Action.__init__)


def test_mydsl_action_constructor_args():
    sig = inspect.signature(myDsl_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_action_has_name():
    assert hasattr(myDsl_Action, "name")
    descriptor = None
    for klass in myDsl_Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_servicefront_is_not_abstract():
    assert not inspect.isabstract(myDsl_ServiceFront)


def test_mydsl_servicefront_constructor_exists():
    assert callable(myDsl_ServiceFront.__init__)


def test_mydsl_servicefront_constructor_args():
    sig = inspect.signature(myDsl_ServiceFront.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "method" in params, "Missing parameter 'method'"

def test_mydsl_servicefront_has_name():
    assert hasattr(myDsl_ServiceFront, "name")
    descriptor = None
    for klass in myDsl_ServiceFront.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_servicefront_has_method():
    assert hasattr(myDsl_ServiceFront, "method")
    descriptor = None
    for klass in myDsl_ServiceFront.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_axiosrequest_is_not_abstract():
    assert not inspect.isabstract(myDsl_AxiosRequest)


def test_mydsl_axiosrequest_constructor_exists():
    assert callable(myDsl_AxiosRequest.__init__)


def test_mydsl_axiosrequest_constructor_args():
    sig = inspect.signature(myDsl_AxiosRequest.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "axiosRestMethod" in params, "Missing parameter 'axiosRestMethod'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_axiosrequest_has_url():
    assert hasattr(myDsl_AxiosRequest, "url")
    descriptor = None
    for klass in myDsl_AxiosRequest.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_axiosrequest_has_axiosRestMethod():
    assert hasattr(myDsl_AxiosRequest, "axiosRestMethod")
    descriptor = None
    for klass in myDsl_AxiosRequest.__mro__:
        if "axiosRestMethod" in klass.__dict__:
            descriptor = klass.__dict__["axiosRestMethod"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_axiosrequest_has_name():
    assert hasattr(myDsl_AxiosRequest, "name")
    descriptor = None
    for klass in myDsl_AxiosRequest.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_file_is_not_abstract():
    assert not inspect.isabstract(myDsl_File)


def test_mydsl_file_constructor_exists():
    assert callable(myDsl_File.__init__)


def test_mydsl_file_constructor_args():
    sig = inspect.signature(myDsl_File.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_file_has_type():
    assert hasattr(myDsl_File, "type")
    descriptor = None
    for klass in myDsl_File.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_file_has_name():
    assert hasattr(myDsl_File, "name")
    descriptor = None
    for klass in myDsl_File.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_routercomponent_is_not_abstract():
    assert not inspect.isabstract(myDsl_RouterComponent)


def test_mydsl_routercomponent_constructor_exists():
    assert callable(myDsl_RouterComponent.__init__)


def test_mydsl_routercomponent_constructor_args():
    sig = inspect.signature(myDsl_RouterComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_routercomponent_has_name():
    assert hasattr(myDsl_RouterComponent, "name")
    descriptor = None
    for klass in myDsl_RouterComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_directory_is_not_abstract():
    assert not inspect.isabstract(myDsl_Directory)


def test_mydsl_directory_constructor_exists():
    assert callable(myDsl_Directory.__init__)


def test_mydsl_directory_constructor_args():
    sig = inspect.signature(myDsl_Directory.__init__)
    params = list(sig.parameters.keys())
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_directory_has_purpose():
    assert hasattr(myDsl_Directory, "purpose")
    descriptor = None
    for klass in myDsl_Directory.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_directory_has_name():
    assert hasattr(myDsl_Directory, "name")
    descriptor = None
    for klass in myDsl_Directory.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_functionality_is_not_abstract():
    assert not inspect.isabstract(myDsl_Functionality)


def test_mydsl_functionality_constructor_exists():
    assert callable(myDsl_Functionality.__init__)


def test_mydsl_functionality_constructor_args():
    sig = inspect.signature(myDsl_Functionality.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_functionality_has_name():
    assert hasattr(myDsl_Functionality, "name")
    descriptor = None
    for klass in myDsl_Functionality.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_reducer_is_not_abstract():
    assert not inspect.isabstract(myDsl_Reducer)


def test_mydsl_reducer_constructor_exists():
    assert callable(myDsl_Reducer.__init__)


def test_mydsl_reducer_constructor_args():
    sig = inspect.signature(myDsl_Reducer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_reducer_has_name():
    assert hasattr(myDsl_Reducer, "name")
    descriptor = None
    for klass in myDsl_Reducer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_reactapp_is_not_abstract():
    assert not inspect.isabstract(myDsl_ReactApp)


def test_mydsl_reactapp_constructor_exists():
    assert callable(myDsl_ReactApp.__init__)


def test_mydsl_reactapp_constructor_args():
    sig = inspect.signature(myDsl_ReactApp.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_jsmodule_is_not_abstract():
    assert not inspect.isabstract(myDsl_JsModule)


def test_mydsl_jsmodule_constructor_exists():
    assert callable(myDsl_JsModule.__init__)


def test_mydsl_jsmodule_constructor_args():
    sig = inspect.signature(myDsl_JsModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_jsmodule_has_name():
    assert hasattr(myDsl_JsModule, "name")
    descriptor = None
    for klass in myDsl_JsModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_actioncreator_is_not_abstract():
    assert not inspect.isabstract(myDsl_ActionCreator)


def test_mydsl_actioncreator_constructor_exists():
    assert callable(myDsl_ActionCreator.__init__)


def test_mydsl_actioncreator_constructor_args():
    sig = inspect.signature(myDsl_ActionCreator.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_actioncreator_has_type():
    assert hasattr(myDsl_ActionCreator, "type")
    descriptor = None
    for klass in myDsl_ActionCreator.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_actioncreator_has_name():
    assert hasattr(myDsl_ActionCreator, "name")
    descriptor = None
    for klass in myDsl_ActionCreator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_container_is_not_abstract():
    assert not inspect.isabstract(myDsl_Container)


def test_mydsl_container_constructor_exists():
    assert callable(myDsl_Container.__init__)


def test_mydsl_container_constructor_args():
    sig = inspect.signature(myDsl_Container.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_container_has_name():
    assert hasattr(myDsl_Container, "name")
    descriptor = None
    for klass in myDsl_Container.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_state_is_not_abstract():
    assert not inspect.isabstract(myDsl_State)


def test_mydsl_state_constructor_exists():
    assert callable(myDsl_State.__init__)


def test_mydsl_state_constructor_args():
    sig = inspect.signature(myDsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_state_has_name():
    assert hasattr(myDsl_State, "name")
    descriptor = None
    for klass in myDsl_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_property_is_not_abstract():
    assert not inspect.isabstract(myDsl_Property)


def test_mydsl_property_constructor_exists():
    assert callable(myDsl_Property.__init__)


def test_mydsl_property_constructor_args():
    sig = inspect.signature(myDsl_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_property_has_name():
    assert hasattr(myDsl_Property, "name")
    descriptor = None
    for klass in myDsl_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_generalentity_is_not_abstract():
    assert not inspect.isabstract(myDsl_GeneralEntity)


def test_mydsl_generalentity_constructor_exists():
    assert callable(myDsl_GeneralEntity.__init__)


def test_mydsl_generalentity_constructor_args():
    sig = inspect.signature(myDsl_GeneralEntity.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_entityname_is_not_abstract():
    assert not inspect.isabstract(myDsl_EntityName)


def test_mydsl_entityname_constructor_exists():
    assert callable(myDsl_EntityName.__init__)


def test_mydsl_entityname_constructor_args():
    sig = inspect.signature(myDsl_EntityName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_entityname_has_name():
    assert hasattr(myDsl_EntityName, "name")
    descriptor = None
    for klass in myDsl_EntityName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl_EObject)


def test_mydsl_eobject_constructor_exists():
    assert callable(myDsl_EObject.__init__)


def test_mydsl_eobject_constructor_args():
    sig = inspect.signature(myDsl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_operation_is_not_abstract():
    assert not inspect.isabstract(myDsl_Operation)


def test_mydsl_operation_constructor_exists():
    assert callable(myDsl_Operation.__init__)


def test_mydsl_operation_constructor_args():
    sig = inspect.signature(myDsl_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl_operation_has_type():
    assert hasattr(myDsl_Operation, "type")
    descriptor = None
    for klass in myDsl_Operation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_module_is_not_abstract():
    assert not inspect.isabstract(myDsl_Module)


def test_mydsl_module_constructor_exists():
    assert callable(myDsl_Module.__init__)


def test_mydsl_module_constructor_args():
    sig = inspect.signature(myDsl_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_module_has_name():
    assert hasattr(myDsl_Module, "name")
    descriptor = None
    for klass in myDsl_Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_type_is_not_abstract():
    assert not inspect.isabstract(myDsl_Type)


def test_mydsl_type_constructor_exists():
    assert callable(myDsl_Type.__init__)


def test_mydsl_type_constructor_args():
    sig = inspect.signature(myDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_type_has_name():
    assert hasattr(myDsl_Type, "name")
    descriptor = None
    for klass in myDsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_technology_is_not_abstract():
    assert not inspect.isabstract(myDsl_Technology)


def test_mydsl_technology_constructor_exists():
    assert callable(myDsl_Technology.__init__)


def test_mydsl_technology_constructor_args():
    sig = inspect.signature(myDsl_Technology.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_architecture_is_not_abstract():
    assert not inspect.isabstract(myDsl_Architecture)


def test_mydsl_architecture_constructor_exists():
    assert callable(myDsl_Architecture.__init__)


def test_mydsl_architecture_constructor_args():
    sig = inspect.signature(myDsl_Architecture.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_domain_is_not_abstract():
    assert not inspect.isabstract(myDsl_Domain)


def test_mydsl_domain_constructor_exists():
    assert callable(myDsl_Domain.__init__)


def test_mydsl_domain_constructor_args():
    sig = inspect.signature(myDsl_Domain.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_system_is_not_abstract():
    assert not inspect.isabstract(myDsl_System)


def test_mydsl_system_constructor_exists():
    assert callable(myDsl_System.__init__)


def test_mydsl_system_constructor_args():
    sig = inspect.signature(myDsl_System.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_submodule_is_not_abstract():
    assert not inspect.isabstract(myDsl_Submodule)


def test_mydsl_submodule_constructor_exists():
    assert callable(myDsl_Submodule.__init__)


def test_mydsl_submodule_constructor_args():
    sig = inspect.signature(myDsl_Submodule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_submodule_has_name():
    assert hasattr(myDsl_Submodule, "name")
    descriptor = None
    for klass in myDsl_Submodule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_relationdom_is_not_abstract():
    assert not inspect.isabstract(myDsl_RelationDom)


def test_mydsl_relationdom_constructor_exists():
    assert callable(myDsl_RelationDom.__init__)


def test_mydsl_relationdom_constructor_args():
    sig = inspect.signature(myDsl_RelationDom.__init__)
    params = list(sig.parameters.keys())


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
File_strategy = st.builds(
    File,
)
myDsl_Css_strategy = st.builds(
    myDsl_Css,
)
myDsl_Json_strategy = st.builds(
    myDsl_Json,
)
myDsl_Js_strategy = st.builds(
    myDsl_Js,
)
myDsl_Md_strategy = st.builds(
    myDsl_Md,
)
myDsl_JsMethodArgs_strategy = st.builds(
    myDsl_JsMethodArgs,
    name=
        safe_text
)
myDsl_JsMethod_strategy = st.builds(
    myDsl_JsMethod,
    type=
        safe_text,
    name=
        safe_text
)
myDsl_UIComponent_strategy = st.builds(
    myDsl_UIComponent,
)
UIComponent_strategy = st.builds(
    UIComponent,
)
myDsl_AbstractFrontElement_strategy = st.builds(
    myDsl_AbstractFrontElement,
)
myDsl_Einterface_strategy = st.builds(
    myDsl_Einterface,
    name=
        safe_text
)
myDsl_AbstractMethod_strategy = st.builds(
    myDsl_AbstractMethod,
    name=
        safe_text
)
myDsl_MethodBack_strategy = st.builds(
    myDsl_MethodBack,
    name=
        safe_text
)
myDsl_Attribute_strategy = st.builds(
    myDsl_Attribute,
    name=
        safe_text
)
Eclass_strategy = st.builds(
    Eclass,
)
myDsl_Annotation_strategy = st.builds(
    myDsl_Annotation,
    propertie=
        safe_text
)
myDsl_NativeClass_strategy = st.builds(
    myDsl_NativeClass,
)
myDsl_GenericClass_strategy = st.builds(
    myDsl_GenericClass,
)
myDsl_AbstractClass_strategy = st.builds(
    myDsl_AbstractClass,
)
myDsl_Descriptor_strategy = st.builds(
    myDsl_Descriptor,
    path=
        safe_text,
    name=
        safe_text
)
myDsl_Library_strategy = st.builds(
    myDsl_Library,
    name=
        safe_text,
    isNative=
        safe_text
)
myDsl_Eclass_strategy = st.builds(
    myDsl_Eclass,
    name=
        safe_text
)
myDsl_JeeProject_strategy = st.builds(
    myDsl_JeeProject,
    name=
        safe_text
)
myDsl_JavaApp_strategy = st.builds(
    myDsl_JavaApp,
)
myDsl_SublayerSegment_strategy = st.builds(
    myDsl_SublayerSegment,
    name=
        safe_text
)
myDsl_LayerSegmentRelation_strategy = st.builds(
    myDsl_LayerSegmentRelation,
    layerSegment=
        safe_text
)
myDsl_LayerSegment_strategy = st.builds(
    myDsl_LayerSegment,
    name=
        safe_text
)
myDsl_Layer_strategy = st.builds(
    myDsl_Layer,
    name=
        safe_text
)
myDsl_RelationArch_strategy = st.builds(
    myDsl_RelationArch,
    source=
        safe_text,
    name=
        safe_text,
    target=
        safe_text
)
myDsl_Component_strategy = st.builds(
    myDsl_Component,
    name=
        safe_text
)
myDsl_Epackage_strategy = st.builds(
    myDsl_Epackage,
    name=
        safe_text
)
myDsl_Subproject_strategy = st.builds(
    myDsl_Subproject,
    name=
        safe_text
)
myDsl_Operateson_strategy = st.builds(
    myDsl_Operateson,
)
myDsl_Transaction_strategy = st.builds(
    myDsl_Transaction,
    type=
        safe_text
)
myDsl_SpecialEntity_strategy = st.builds(
    myDsl_SpecialEntity,
)
AbstractFrontElement_strategy = st.builds(
    AbstractFrontElement,
)
myDsl_ActionDispatcher_strategy = st.builds(
    myDsl_ActionDispatcher,
    name=
        safe_text
)
myDsl_Visualizer_strategy = st.builds(
    myDsl_Visualizer,
    name=
        safe_text
)
myDsl_Action_strategy = st.builds(
    myDsl_Action,
    name=
        safe_text
)
myDsl_ServiceFront_strategy = st.builds(
    myDsl_ServiceFront,
    name=
        safe_text,
    method=
        safe_text
)
myDsl_AxiosRequest_strategy = st.builds(
    myDsl_AxiosRequest,
    url=
        safe_text,
    axiosRestMethod=
        safe_text,
    name=
        safe_text
)
myDsl_File_strategy = st.builds(
    myDsl_File,
    type=
        safe_text,
    name=
        safe_text
)
myDsl_RouterComponent_strategy = st.builds(
    myDsl_RouterComponent,
    name=
        safe_text
)
myDsl_Directory_strategy = st.builds(
    myDsl_Directory,
    purpose=
        safe_text,
    name=
        safe_text
)
myDsl_Functionality_strategy = st.builds(
    myDsl_Functionality,
    name=
        safe_text
)
myDsl_Reducer_strategy = st.builds(
    myDsl_Reducer,
    name=
        safe_text
)
myDsl_ReactApp_strategy = st.builds(
    myDsl_ReactApp,
)
myDsl_JsModule_strategy = st.builds(
    myDsl_JsModule,
    name=
        safe_text
)
myDsl_ActionCreator_strategy = st.builds(
    myDsl_ActionCreator,
    type=
        safe_text,
    name=
        safe_text
)
myDsl_Container_strategy = st.builds(
    myDsl_Container,
    name=
        safe_text
)
myDsl_State_strategy = st.builds(
    myDsl_State,
    name=
        safe_text
)
myDsl_Property_strategy = st.builds(
    myDsl_Property,
    name=
        safe_text
)
myDsl_GeneralEntity_strategy = st.builds(
    myDsl_GeneralEntity,
)
myDsl_EntityName_strategy = st.builds(
    myDsl_EntityName,
    name=
        safe_text
)
myDsl_EObject_strategy = st.builds(
    myDsl_EObject,
)
myDsl_Operation_strategy = st.builds(
    myDsl_Operation,
    type=
        safe_text
)
myDsl_Module_strategy = st.builds(
    myDsl_Module,
    name=
        safe_text
)
myDsl_Type_strategy = st.builds(
    myDsl_Type,
    name=
        safe_text
)
myDsl_Technology_strategy = st.builds(
    myDsl_Technology,
)
myDsl_Architecture_strategy = st.builds(
    myDsl_Architecture,
)
myDsl_Domain_strategy = st.builds(
    myDsl_Domain,
)
myDsl_System_strategy = st.builds(
    myDsl_System,
)
myDsl_Submodule_strategy = st.builds(
    myDsl_Submodule,
    name=
        safe_text
)
myDsl_RelationDom_strategy = st.builds(
    myDsl_RelationDom,
)

@given(instance=File_strategy)
@settings(max_examples=50)
def test_file_instantiation(instance):
    assert isinstance(instance, File)

@given(instance=myDsl_Css_strategy)
@settings(max_examples=50)
def test_mydsl_css_instantiation(instance):
    assert isinstance(instance, myDsl_Css)

@given(instance=myDsl_Json_strategy)
@settings(max_examples=50)
def test_mydsl_json_instantiation(instance):
    assert isinstance(instance, myDsl_Json)

@given(instance=myDsl_Js_strategy)
@settings(max_examples=50)
def test_mydsl_js_instantiation(instance):
    assert isinstance(instance, myDsl_Js)

@given(instance=myDsl_Md_strategy)
@settings(max_examples=50)
def test_mydsl_md_instantiation(instance):
    assert isinstance(instance, myDsl_Md)

@given(instance=myDsl_JsMethodArgs_strategy)
@settings(max_examples=50)
def test_mydsl_jsmethodargs_instantiation(instance):
    assert isinstance(instance, myDsl_JsMethodArgs)



@given(instance=myDsl_JsMethodArgs_strategy)
def test_mydsl_jsmethodargs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_JsMethod_strategy)
@settings(max_examples=50)
def test_mydsl_jsmethod_instantiation(instance):
    assert isinstance(instance, myDsl_JsMethod)



@given(instance=myDsl_JsMethod_strategy)
def test_mydsl_jsmethod_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=myDsl_JsMethod_strategy)
def test_mydsl_jsmethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_UIComponent_strategy)
@settings(max_examples=50)
def test_mydsl_uicomponent_instantiation(instance):
    assert isinstance(instance, myDsl_UIComponent)

@given(instance=UIComponent_strategy)
@settings(max_examples=50)
def test_uicomponent_instantiation(instance):
    assert isinstance(instance, UIComponent)

@given(instance=myDsl_AbstractFrontElement_strategy)
@settings(max_examples=50)
def test_mydsl_abstractfrontelement_instantiation(instance):
    assert isinstance(instance, myDsl_AbstractFrontElement)

@given(instance=myDsl_Einterface_strategy)
@settings(max_examples=50)
def test_mydsl_einterface_instantiation(instance):
    assert isinstance(instance, myDsl_Einterface)



@given(instance=myDsl_Einterface_strategy)
def test_mydsl_einterface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_AbstractMethod_strategy)
@settings(max_examples=50)
def test_mydsl_abstractmethod_instantiation(instance):
    assert isinstance(instance, myDsl_AbstractMethod)



@given(instance=myDsl_AbstractMethod_strategy)
def test_mydsl_abstractmethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_MethodBack_strategy)
@settings(max_examples=50)
def test_mydsl_methodback_instantiation(instance):
    assert isinstance(instance, myDsl_MethodBack)



@given(instance=myDsl_MethodBack_strategy)
def test_mydsl_methodback_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Attribute_strategy)
@settings(max_examples=50)
def test_mydsl_attribute_instantiation(instance):
    assert isinstance(instance, myDsl_Attribute)



@given(instance=myDsl_Attribute_strategy)
def test_mydsl_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Eclass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, Eclass)

@given(instance=myDsl_Annotation_strategy)
@settings(max_examples=50)
def test_mydsl_annotation_instantiation(instance):
    assert isinstance(instance, myDsl_Annotation)



@given(instance=myDsl_Annotation_strategy)
def test_mydsl_annotation_propertie_setter(instance):
    original = instance.propertie
    instance.propertie = original
    assert instance.propertie == original

@given(instance=myDsl_NativeClass_strategy)
@settings(max_examples=50)
def test_mydsl_nativeclass_instantiation(instance):
    assert isinstance(instance, myDsl_NativeClass)

@given(instance=myDsl_GenericClass_strategy)
@settings(max_examples=50)
def test_mydsl_genericclass_instantiation(instance):
    assert isinstance(instance, myDsl_GenericClass)

@given(instance=myDsl_AbstractClass_strategy)
@settings(max_examples=50)
def test_mydsl_abstractclass_instantiation(instance):
    assert isinstance(instance, myDsl_AbstractClass)

@given(instance=myDsl_Descriptor_strategy)
@settings(max_examples=50)
def test_mydsl_descriptor_instantiation(instance):
    assert isinstance(instance, myDsl_Descriptor)



@given(instance=myDsl_Descriptor_strategy)
def test_mydsl_descriptor_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=myDsl_Descriptor_strategy)
def test_mydsl_descriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Library_strategy)
@settings(max_examples=50)
def test_mydsl_library_instantiation(instance):
    assert isinstance(instance, myDsl_Library)



@given(instance=myDsl_Library_strategy)
def test_mydsl_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Library_strategy)
def test_mydsl_library_isNative_setter(instance):
    original = instance.isNative
    instance.isNative = original
    assert instance.isNative == original

@given(instance=myDsl_Eclass_strategy)
@settings(max_examples=50)
def test_mydsl_eclass_instantiation(instance):
    assert isinstance(instance, myDsl_Eclass)



@given(instance=myDsl_Eclass_strategy)
def test_mydsl_eclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_JeeProject_strategy)
@settings(max_examples=50)
def test_mydsl_jeeproject_instantiation(instance):
    assert isinstance(instance, myDsl_JeeProject)



@given(instance=myDsl_JeeProject_strategy)
def test_mydsl_jeeproject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_JavaApp_strategy)
@settings(max_examples=50)
def test_mydsl_javaapp_instantiation(instance):
    assert isinstance(instance, myDsl_JavaApp)

@given(instance=myDsl_SublayerSegment_strategy)
@settings(max_examples=50)
def test_mydsl_sublayersegment_instantiation(instance):
    assert isinstance(instance, myDsl_SublayerSegment)



@given(instance=myDsl_SublayerSegment_strategy)
def test_mydsl_sublayersegment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_LayerSegmentRelation_strategy)
@settings(max_examples=50)
def test_mydsl_layersegmentrelation_instantiation(instance):
    assert isinstance(instance, myDsl_LayerSegmentRelation)



@given(instance=myDsl_LayerSegmentRelation_strategy)
def test_mydsl_layersegmentrelation_layerSegment_setter(instance):
    original = instance.layerSegment
    instance.layerSegment = original
    assert instance.layerSegment == original

@given(instance=myDsl_LayerSegment_strategy)
@settings(max_examples=50)
def test_mydsl_layersegment_instantiation(instance):
    assert isinstance(instance, myDsl_LayerSegment)



@given(instance=myDsl_LayerSegment_strategy)
def test_mydsl_layersegment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Layer_strategy)
@settings(max_examples=50)
def test_mydsl_layer_instantiation(instance):
    assert isinstance(instance, myDsl_Layer)



@given(instance=myDsl_Layer_strategy)
def test_mydsl_layer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_RelationArch_strategy)
@settings(max_examples=50)
def test_mydsl_relationarch_instantiation(instance):
    assert isinstance(instance, myDsl_RelationArch)



@given(instance=myDsl_RelationArch_strategy)
def test_mydsl_relationarch_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=myDsl_RelationArch_strategy)
def test_mydsl_relationarch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_RelationArch_strategy)
def test_mydsl_relationarch_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=myDsl_Component_strategy)
@settings(max_examples=50)
def test_mydsl_component_instantiation(instance):
    assert isinstance(instance, myDsl_Component)



@given(instance=myDsl_Component_strategy)
def test_mydsl_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Epackage_strategy)
@settings(max_examples=50)
def test_mydsl_epackage_instantiation(instance):
    assert isinstance(instance, myDsl_Epackage)



@given(instance=myDsl_Epackage_strategy)
def test_mydsl_epackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Subproject_strategy)
@settings(max_examples=50)
def test_mydsl_subproject_instantiation(instance):
    assert isinstance(instance, myDsl_Subproject)



@given(instance=myDsl_Subproject_strategy)
def test_mydsl_subproject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Operateson_strategy)
@settings(max_examples=50)
def test_mydsl_operateson_instantiation(instance):
    assert isinstance(instance, myDsl_Operateson)

@given(instance=myDsl_Transaction_strategy)
@settings(max_examples=50)
def test_mydsl_transaction_instantiation(instance):
    assert isinstance(instance, myDsl_Transaction)



@given(instance=myDsl_Transaction_strategy)
def test_mydsl_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl_SpecialEntity_strategy)
@settings(max_examples=50)
def test_mydsl_specialentity_instantiation(instance):
    assert isinstance(instance, myDsl_SpecialEntity)

@given(instance=AbstractFrontElement_strategy)
@settings(max_examples=50)
def test_abstractfrontelement_instantiation(instance):
    assert isinstance(instance, AbstractFrontElement)

@given(instance=myDsl_ActionDispatcher_strategy)
@settings(max_examples=50)
def test_mydsl_actiondispatcher_instantiation(instance):
    assert isinstance(instance, myDsl_ActionDispatcher)



@given(instance=myDsl_ActionDispatcher_strategy)
def test_mydsl_actiondispatcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Visualizer_strategy)
@settings(max_examples=50)
def test_mydsl_visualizer_instantiation(instance):
    assert isinstance(instance, myDsl_Visualizer)



@given(instance=myDsl_Visualizer_strategy)
def test_mydsl_visualizer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Action_strategy)
@settings(max_examples=50)
def test_mydsl_action_instantiation(instance):
    assert isinstance(instance, myDsl_Action)



@given(instance=myDsl_Action_strategy)
def test_mydsl_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_ServiceFront_strategy)
@settings(max_examples=50)
def test_mydsl_servicefront_instantiation(instance):
    assert isinstance(instance, myDsl_ServiceFront)



@given(instance=myDsl_ServiceFront_strategy)
def test_mydsl_servicefront_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_ServiceFront_strategy)
def test_mydsl_servicefront_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=myDsl_AxiosRequest_strategy)
@settings(max_examples=50)
def test_mydsl_axiosrequest_instantiation(instance):
    assert isinstance(instance, myDsl_AxiosRequest)



@given(instance=myDsl_AxiosRequest_strategy)
def test_mydsl_axiosrequest_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=myDsl_AxiosRequest_strategy)
def test_mydsl_axiosrequest_axiosRestMethod_setter(instance):
    original = instance.axiosRestMethod
    instance.axiosRestMethod = original
    assert instance.axiosRestMethod == original



@given(instance=myDsl_AxiosRequest_strategy)
def test_mydsl_axiosrequest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_File_strategy)
@settings(max_examples=50)
def test_mydsl_file_instantiation(instance):
    assert isinstance(instance, myDsl_File)



@given(instance=myDsl_File_strategy)
def test_mydsl_file_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=myDsl_File_strategy)
def test_mydsl_file_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_RouterComponent_strategy)
@settings(max_examples=50)
def test_mydsl_routercomponent_instantiation(instance):
    assert isinstance(instance, myDsl_RouterComponent)



@given(instance=myDsl_RouterComponent_strategy)
def test_mydsl_routercomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Directory_strategy)
@settings(max_examples=50)
def test_mydsl_directory_instantiation(instance):
    assert isinstance(instance, myDsl_Directory)



@given(instance=myDsl_Directory_strategy)
def test_mydsl_directory_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original



@given(instance=myDsl_Directory_strategy)
def test_mydsl_directory_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Functionality_strategy)
@settings(max_examples=50)
def test_mydsl_functionality_instantiation(instance):
    assert isinstance(instance, myDsl_Functionality)



@given(instance=myDsl_Functionality_strategy)
def test_mydsl_functionality_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Reducer_strategy)
@settings(max_examples=50)
def test_mydsl_reducer_instantiation(instance):
    assert isinstance(instance, myDsl_Reducer)



@given(instance=myDsl_Reducer_strategy)
def test_mydsl_reducer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_ReactApp_strategy)
@settings(max_examples=50)
def test_mydsl_reactapp_instantiation(instance):
    assert isinstance(instance, myDsl_ReactApp)

@given(instance=myDsl_JsModule_strategy)
@settings(max_examples=50)
def test_mydsl_jsmodule_instantiation(instance):
    assert isinstance(instance, myDsl_JsModule)



@given(instance=myDsl_JsModule_strategy)
def test_mydsl_jsmodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_ActionCreator_strategy)
@settings(max_examples=50)
def test_mydsl_actioncreator_instantiation(instance):
    assert isinstance(instance, myDsl_ActionCreator)



@given(instance=myDsl_ActionCreator_strategy)
def test_mydsl_actioncreator_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=myDsl_ActionCreator_strategy)
def test_mydsl_actioncreator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Container_strategy)
@settings(max_examples=50)
def test_mydsl_container_instantiation(instance):
    assert isinstance(instance, myDsl_Container)



@given(instance=myDsl_Container_strategy)
def test_mydsl_container_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_State_strategy)
@settings(max_examples=50)
def test_mydsl_state_instantiation(instance):
    assert isinstance(instance, myDsl_State)



@given(instance=myDsl_State_strategy)
def test_mydsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Property_strategy)
@settings(max_examples=50)
def test_mydsl_property_instantiation(instance):
    assert isinstance(instance, myDsl_Property)



@given(instance=myDsl_Property_strategy)
def test_mydsl_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_GeneralEntity_strategy)
@settings(max_examples=50)
def test_mydsl_generalentity_instantiation(instance):
    assert isinstance(instance, myDsl_GeneralEntity)

@given(instance=myDsl_EntityName_strategy)
@settings(max_examples=50)
def test_mydsl_entityname_instantiation(instance):
    assert isinstance(instance, myDsl_EntityName)



@given(instance=myDsl_EntityName_strategy)
def test_mydsl_entityname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_EObject_strategy)
@settings(max_examples=50)
def test_mydsl_eobject_instantiation(instance):
    assert isinstance(instance, myDsl_EObject)

@given(instance=myDsl_Operation_strategy)
@settings(max_examples=50)
def test_mydsl_operation_instantiation(instance):
    assert isinstance(instance, myDsl_Operation)



@given(instance=myDsl_Operation_strategy)
def test_mydsl_operation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl_Module_strategy)
@settings(max_examples=50)
def test_mydsl_module_instantiation(instance):
    assert isinstance(instance, myDsl_Module)



@given(instance=myDsl_Module_strategy)
def test_mydsl_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Type_strategy)
@settings(max_examples=50)
def test_mydsl_type_instantiation(instance):
    assert isinstance(instance, myDsl_Type)



@given(instance=myDsl_Type_strategy)
def test_mydsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Technology_strategy)
@settings(max_examples=50)
def test_mydsl_technology_instantiation(instance):
    assert isinstance(instance, myDsl_Technology)

@given(instance=myDsl_Architecture_strategy)
@settings(max_examples=50)
def test_mydsl_architecture_instantiation(instance):
    assert isinstance(instance, myDsl_Architecture)

@given(instance=myDsl_Domain_strategy)
@settings(max_examples=50)
def test_mydsl_domain_instantiation(instance):
    assert isinstance(instance, myDsl_Domain)

@given(instance=myDsl_System_strategy)
@settings(max_examples=50)
def test_mydsl_system_instantiation(instance):
    assert isinstance(instance, myDsl_System)

@given(instance=myDsl_Submodule_strategy)
@settings(max_examples=50)
def test_mydsl_submodule_instantiation(instance):
    assert isinstance(instance, myDsl_Submodule)



@given(instance=myDsl_Submodule_strategy)
def test_mydsl_submodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_RelationDom_strategy)
@settings(max_examples=50)
def test_mydsl_relationdom_instantiation(instance):
    assert isinstance(instance, myDsl_RelationDom)
