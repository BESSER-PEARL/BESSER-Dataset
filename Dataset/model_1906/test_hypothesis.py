import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Component,
    UnifiedMetamodel__Front,
    UnifiedMetamodel__Back,
    SubLayerSegment,
    UnifiedMetamodel__Actions,
    UnifiedMetamodel__Reducers,
    UnifiedMetamodel__Descriptor,
    UnifiedMetamodel__AbstractMethod,
    UnifiedMetamodel__EInterface,
    EClass,
    UnifiedMetamodel__NativeClass,
    UnifiedMetamodel__Subproject,
    UnifiedMetamodel__Epackage,
    UnifiedMetamodel__MethodBack,
    UnifiedMetamodel__AbstractClass,
    UnifiedMetamodel__GenericClass,
    UnifiedMetamodel__EClass,
    UnifiedMetamodel__Attribute,
    UnifiedMetamodel__Annotation,
    UnifiedMetamodel__Library,
    UnifiedMetamodel__ReactApp,
    UnifiedMetamodel__JEE_Project,
    UnifiedMetamodel__JavaApp,
    UnifiedMetamodel__ModuleFront,
    UnifiedMetamodel__Reducer,
    UnifiedMetamodel__Action,
    UnifiedMetamodel__State,
    UnifiedMetamodel__ComponentFront,
    UnifiedMetamodel__Functionality,
    UnifiedMetamodel__ServicesFront,
    UIFront,
    UnifiedMetamodel__RouterComponent,
    UnifiedMetamodel__Visualizer,
    ComponentFront,
    UnifiedMetamodel__Container,
    UnifiedMetamodel__UIFront,
    UnifiedMetamodel__Transaction,
    Entity,
    UnifiedMetamodel__SpecialEntity,
    UnifiedMetamodel__File,
    UnifiedMetamodel__Directory,
    File,
    UnifiedMetamodel__JS,
    UnifiedMetamodel__MD,
    UnifiedMetamodel__CSS,
    UnifiedMetamodel__JSON,
    ModuleFront,
    UnifiedMetamodel__React,
    UnifiedMetamodel__APICall,
    UnifiedMetamodel__Redux,
    UnifiedMetamodel__Design,
    UnifiedMetamodel__Router,
    UnifiedMetamodel__ActionCreator,
    UnifiedMetamodel__ActionDispatcher,
    UnifiedMetamodel__RelationDom,
    UnifiedMetamodel__Property,
    UnifiedMetamodel__GeneralEntity,
    UnifiedMetamodel__Submodule,
    UnifiedMetamodel__Module,
    UnifiedMetamodel__ArquitectureMetamodel,
    UnifiedMetamodel__Entity,
    UnifiedMetamodel__Operations,
    RelationDom,
    UnifiedMetamodel__Composition,
    Transaction,
    UnifiedMetamodel__Exchange,
    UnifiedMetamodel__Sale,
    Operations,
    UnifiedMetamodel__Create,
    UnifiedMetamodel__Read,
    UnifiedMetamodel__TechnologyMetamodel,
    UnifiedMetamodel__DomainMetamodel,
    UnifiedMetamodel__Metamodel,
    LayerSegment,
    UnifiedMetamodel__UI,
    UnifiedMetamodel__Containers,
    UnifiedMetamodel__Pojo,
    UnifiedMetamodel__Services,
    UnifiedMetamodel__Util,
    UnifiedMetamodel__Store,
    UnifiedMetamodel__Dto,
    UnifiedMetamodel__RelationArch,
    UnifiedMetamodel__Component,
    UnifiedMetamodel__Facade,
    UnifiedMetamodel__RestEntity,
    UnifiedMetamodel__Layer,
    UnifiedMetamodel__SubLayerSegment,
    UnifiedMetamodel__LayerSegment,
    Layer,
    UnifiedMetamodel__JavaScript,
    UnifiedMetamodel__War,
    UnifiedMetamodel__Ejb,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__front_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Front)


def test_unifiedmetamodel__front_constructor_exists():
    assert callable(UnifiedMetamodel__Front.__init__)


def test_unifiedmetamodel__front_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Front.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__back_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Back)


def test_unifiedmetamodel__back_constructor_exists():
    assert callable(UnifiedMetamodel__Back.__init__)


def test_unifiedmetamodel__back_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Back.__init__)
    params = list(sig.parameters.keys())



def test_sublayersegment_is_not_abstract():
    assert not inspect.isabstract(SubLayerSegment)


def test_sublayersegment_constructor_exists():
    assert callable(SubLayerSegment.__init__)


def test_sublayersegment_constructor_args():
    sig = inspect.signature(SubLayerSegment.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__actions_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Actions)


def test_unifiedmetamodel__actions_constructor_exists():
    assert callable(UnifiedMetamodel__Actions.__init__)


def test_unifiedmetamodel__actions_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Actions.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__reducers_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Reducers)


def test_unifiedmetamodel__reducers_constructor_exists():
    assert callable(UnifiedMetamodel__Reducers.__init__)


def test_unifiedmetamodel__reducers_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Reducers.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__descriptor_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Descriptor)


def test_unifiedmetamodel__descriptor_constructor_exists():
    assert callable(UnifiedMetamodel__Descriptor.__init__)


def test_unifiedmetamodel__descriptor_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Descriptor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "path" in params, "Missing parameter 'path'"

def test_unifiedmetamodel__descriptor_has_name():
    assert hasattr(UnifiedMetamodel__Descriptor, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Descriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_unifiedmetamodel__descriptor_has_path():
    assert hasattr(UnifiedMetamodel__Descriptor, "path")
    descriptor = None
    for klass in UnifiedMetamodel__Descriptor.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__abstractmethod_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__AbstractMethod)


def test_unifiedmetamodel__abstractmethod_constructor_exists():
    assert callable(UnifiedMetamodel__AbstractMethod.__init__)


def test_unifiedmetamodel__abstractmethod_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__AbstractMethod.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__abstractmethod_has_name():
    assert hasattr(UnifiedMetamodel__AbstractMethod, "name")
    descriptor = None
    for klass in UnifiedMetamodel__AbstractMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__einterface_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__EInterface)


def test_unifiedmetamodel__einterface_constructor_exists():
    assert callable(UnifiedMetamodel__EInterface.__init__)


def test_unifiedmetamodel__einterface_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__EInterface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__einterface_has_name():
    assert hasattr(UnifiedMetamodel__EInterface, "name")
    descriptor = None
    for klass in UnifiedMetamodel__EInterface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__nativeclass_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__NativeClass)


def test_unifiedmetamodel__nativeclass_constructor_exists():
    assert callable(UnifiedMetamodel__NativeClass.__init__)


def test_unifiedmetamodel__nativeclass_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__NativeClass.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveRef" in params, "Missing parameter 'primitiveRef'"

def test_unifiedmetamodel__nativeclass_has_primitiveRef():
    assert hasattr(UnifiedMetamodel__NativeClass, "primitiveRef")
    descriptor = None
    for klass in UnifiedMetamodel__NativeClass.__mro__:
        if "primitiveRef" in klass.__dict__:
            descriptor = klass.__dict__["primitiveRef"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__subproject_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Subproject)


def test_unifiedmetamodel__subproject_constructor_exists():
    assert callable(UnifiedMetamodel__Subproject.__init__)


def test_unifiedmetamodel__subproject_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Subproject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__subproject_has_name():
    assert hasattr(UnifiedMetamodel__Subproject, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Subproject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__epackage_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Epackage)


def test_unifiedmetamodel__epackage_constructor_exists():
    assert callable(UnifiedMetamodel__Epackage.__init__)


def test_unifiedmetamodel__epackage_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Epackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__epackage_has_name():
    assert hasattr(UnifiedMetamodel__Epackage, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Epackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__methodback_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__MethodBack)


def test_unifiedmetamodel__methodback_constructor_exists():
    assert callable(UnifiedMetamodel__MethodBack.__init__)


def test_unifiedmetamodel__methodback_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__MethodBack.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__methodback_has_name():
    assert hasattr(UnifiedMetamodel__MethodBack, "name")
    descriptor = None
    for klass in UnifiedMetamodel__MethodBack.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__abstractclass_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__AbstractClass)


def test_unifiedmetamodel__abstractclass_constructor_exists():
    assert callable(UnifiedMetamodel__AbstractClass.__init__)


def test_unifiedmetamodel__abstractclass_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__AbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__genericclass_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__GenericClass)


def test_unifiedmetamodel__genericclass_constructor_exists():
    assert callable(UnifiedMetamodel__GenericClass.__init__)


def test_unifiedmetamodel__genericclass_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__GenericClass.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__eclass_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__EClass)


def test_unifiedmetamodel__eclass_constructor_exists():
    assert callable(UnifiedMetamodel__EClass.__init__)


def test_unifiedmetamodel__eclass_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__EClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__eclass_has_name():
    assert hasattr(UnifiedMetamodel__EClass, "name")
    descriptor = None
    for klass in UnifiedMetamodel__EClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__attribute_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Attribute)


def test_unifiedmetamodel__attribute_constructor_exists():
    assert callable(UnifiedMetamodel__Attribute.__init__)


def test_unifiedmetamodel__attribute_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__attribute_has_name():
    assert hasattr(UnifiedMetamodel__Attribute, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__annotation_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Annotation)


def test_unifiedmetamodel__annotation_constructor_exists():
    assert callable(UnifiedMetamodel__Annotation.__init__)


def test_unifiedmetamodel__annotation_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "properties" in params, "Missing parameter 'properties'"

def test_unifiedmetamodel__annotation_has_properties():
    assert hasattr(UnifiedMetamodel__Annotation, "properties")
    descriptor = None
    for klass in UnifiedMetamodel__Annotation.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__library_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Library)


def test_unifiedmetamodel__library_constructor_exists():
    assert callable(UnifiedMetamodel__Library.__init__)


def test_unifiedmetamodel__library_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isNative" in params, "Missing parameter 'isNative'"

def test_unifiedmetamodel__library_has_name():
    assert hasattr(UnifiedMetamodel__Library, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_unifiedmetamodel__library_has_isNative():
    assert hasattr(UnifiedMetamodel__Library, "isNative")
    descriptor = None
    for klass in UnifiedMetamodel__Library.__mro__:
        if "isNative" in klass.__dict__:
            descriptor = klass.__dict__["isNative"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__reactapp_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__ReactApp)


def test_unifiedmetamodel__reactapp_constructor_exists():
    assert callable(UnifiedMetamodel__ReactApp.__init__)


def test_unifiedmetamodel__reactapp_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__ReactApp.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__jee_project_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__JEE_Project)


def test_unifiedmetamodel__jee_project_constructor_exists():
    assert callable(UnifiedMetamodel__JEE_Project.__init__)


def test_unifiedmetamodel__jee_project_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__JEE_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__jee_project_has_name():
    assert hasattr(UnifiedMetamodel__JEE_Project, "name")
    descriptor = None
    for klass in UnifiedMetamodel__JEE_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__javaapp_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__JavaApp)


def test_unifiedmetamodel__javaapp_constructor_exists():
    assert callable(UnifiedMetamodel__JavaApp.__init__)


def test_unifiedmetamodel__javaapp_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__JavaApp.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__modulefront_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__ModuleFront)


def test_unifiedmetamodel__modulefront_constructor_exists():
    assert callable(UnifiedMetamodel__ModuleFront.__init__)


def test_unifiedmetamodel__modulefront_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__ModuleFront.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__modulefront_has_name():
    assert hasattr(UnifiedMetamodel__ModuleFront, "name")
    descriptor = None
    for klass in UnifiedMetamodel__ModuleFront.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__reducer_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Reducer)


def test_unifiedmetamodel__reducer_constructor_exists():
    assert callable(UnifiedMetamodel__Reducer.__init__)


def test_unifiedmetamodel__reducer_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Reducer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__reducer_has_name():
    assert hasattr(UnifiedMetamodel__Reducer, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Reducer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__action_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Action)


def test_unifiedmetamodel__action_constructor_exists():
    assert callable(UnifiedMetamodel__Action.__init__)


def test_unifiedmetamodel__action_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__action_has_name():
    assert hasattr(UnifiedMetamodel__Action, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__state_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__State)


def test_unifiedmetamodel__state_constructor_exists():
    assert callable(UnifiedMetamodel__State.__init__)


def test_unifiedmetamodel__state_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__State.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__componentfront_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__ComponentFront)


def test_unifiedmetamodel__componentfront_constructor_exists():
    assert callable(UnifiedMetamodel__ComponentFront.__init__)


def test_unifiedmetamodel__componentfront_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__ComponentFront.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__componentfront_has_name():
    assert hasattr(UnifiedMetamodel__ComponentFront, "name")
    descriptor = None
    for klass in UnifiedMetamodel__ComponentFront.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__functionality_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Functionality)


def test_unifiedmetamodel__functionality_constructor_exists():
    assert callable(UnifiedMetamodel__Functionality.__init__)


def test_unifiedmetamodel__functionality_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Functionality.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__functionality_has_name():
    assert hasattr(UnifiedMetamodel__Functionality, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Functionality.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__servicesfront_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__ServicesFront)


def test_unifiedmetamodel__servicesfront_constructor_exists():
    assert callable(UnifiedMetamodel__ServicesFront.__init__)


def test_unifiedmetamodel__servicesfront_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__ServicesFront.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__servicesfront_has_name():
    assert hasattr(UnifiedMetamodel__ServicesFront, "name")
    descriptor = None
    for klass in UnifiedMetamodel__ServicesFront.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uifront_is_not_abstract():
    assert not inspect.isabstract(UIFront)


def test_uifront_constructor_exists():
    assert callable(UIFront.__init__)


def test_uifront_constructor_args():
    sig = inspect.signature(UIFront.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__routercomponent_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__RouterComponent)


def test_unifiedmetamodel__routercomponent_constructor_exists():
    assert callable(UnifiedMetamodel__RouterComponent.__init__)


def test_unifiedmetamodel__routercomponent_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__RouterComponent.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__visualizer_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Visualizer)


def test_unifiedmetamodel__visualizer_constructor_exists():
    assert callable(UnifiedMetamodel__Visualizer.__init__)


def test_unifiedmetamodel__visualizer_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Visualizer.__init__)
    params = list(sig.parameters.keys())



def test_componentfront_is_not_abstract():
    assert not inspect.isabstract(ComponentFront)


def test_componentfront_constructor_exists():
    assert callable(ComponentFront.__init__)


def test_componentfront_constructor_args():
    sig = inspect.signature(ComponentFront.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__container_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Container)


def test_unifiedmetamodel__container_constructor_exists():
    assert callable(UnifiedMetamodel__Container.__init__)


def test_unifiedmetamodel__container_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Container.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__uifront_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__UIFront)


def test_unifiedmetamodel__uifront_constructor_exists():
    assert callable(UnifiedMetamodel__UIFront.__init__)


def test_unifiedmetamodel__uifront_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__UIFront.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__transaction_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Transaction)


def test_unifiedmetamodel__transaction_constructor_exists():
    assert callable(UnifiedMetamodel__Transaction.__init__)


def test_unifiedmetamodel__transaction_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Transaction.__init__)
    params = list(sig.parameters.keys())



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__specialentity_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__SpecialEntity)


def test_unifiedmetamodel__specialentity_constructor_exists():
    assert callable(UnifiedMetamodel__SpecialEntity.__init__)


def test_unifiedmetamodel__specialentity_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__SpecialEntity.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__file_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__File)


def test_unifiedmetamodel__file_constructor_exists():
    assert callable(UnifiedMetamodel__File.__init__)


def test_unifiedmetamodel__file_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__File.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__file_has_type():
    assert hasattr(UnifiedMetamodel__File, "type")
    descriptor = None
    for klass in UnifiedMetamodel__File.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_unifiedmetamodel__file_has_name():
    assert hasattr(UnifiedMetamodel__File, "name")
    descriptor = None
    for klass in UnifiedMetamodel__File.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__directory_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Directory)


def test_unifiedmetamodel__directory_constructor_exists():
    assert callable(UnifiedMetamodel__Directory.__init__)


def test_unifiedmetamodel__directory_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Directory.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "isRoot" in params, "Missing parameter 'isRoot'"

def test_unifiedmetamodel__directory_has_name():
    assert hasattr(UnifiedMetamodel__Directory, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Directory.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_unifiedmetamodel__directory_has_purpose():
    assert hasattr(UnifiedMetamodel__Directory, "purpose")
    descriptor = None
    for klass in UnifiedMetamodel__Directory.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)

def test_unifiedmetamodel__directory_has_isRoot():
    assert hasattr(UnifiedMetamodel__Directory, "isRoot")
    descriptor = None
    for klass in UnifiedMetamodel__Directory.__mro__:
        if "isRoot" in klass.__dict__:
            descriptor = klass.__dict__["isRoot"]
            break
    assert isinstance(descriptor, property)



def test_file_is_not_abstract():
    assert not inspect.isabstract(File)


def test_file_constructor_exists():
    assert callable(File.__init__)


def test_file_constructor_args():
    sig = inspect.signature(File.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__js_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__JS)


def test_unifiedmetamodel__js_constructor_exists():
    assert callable(UnifiedMetamodel__JS.__init__)


def test_unifiedmetamodel__js_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__JS.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__md_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__MD)


def test_unifiedmetamodel__md_constructor_exists():
    assert callable(UnifiedMetamodel__MD.__init__)


def test_unifiedmetamodel__md_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__MD.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__css_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__CSS)


def test_unifiedmetamodel__css_constructor_exists():
    assert callable(UnifiedMetamodel__CSS.__init__)


def test_unifiedmetamodel__css_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__CSS.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__json_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__JSON)


def test_unifiedmetamodel__json_constructor_exists():
    assert callable(UnifiedMetamodel__JSON.__init__)


def test_unifiedmetamodel__json_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__JSON.__init__)
    params = list(sig.parameters.keys())



def test_modulefront_is_not_abstract():
    assert not inspect.isabstract(ModuleFront)


def test_modulefront_constructor_exists():
    assert callable(ModuleFront.__init__)


def test_modulefront_constructor_args():
    sig = inspect.signature(ModuleFront.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__react_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__React)


def test_unifiedmetamodel__react_constructor_exists():
    assert callable(UnifiedMetamodel__React.__init__)


def test_unifiedmetamodel__react_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__React.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__apicall_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__APICall)


def test_unifiedmetamodel__apicall_constructor_exists():
    assert callable(UnifiedMetamodel__APICall.__init__)


def test_unifiedmetamodel__apicall_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__APICall.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__redux_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Redux)


def test_unifiedmetamodel__redux_constructor_exists():
    assert callable(UnifiedMetamodel__Redux.__init__)


def test_unifiedmetamodel__redux_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Redux.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__design_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Design)


def test_unifiedmetamodel__design_constructor_exists():
    assert callable(UnifiedMetamodel__Design.__init__)


def test_unifiedmetamodel__design_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Design.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__router_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Router)


def test_unifiedmetamodel__router_constructor_exists():
    assert callable(UnifiedMetamodel__Router.__init__)


def test_unifiedmetamodel__router_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Router.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__actioncreator_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__ActionCreator)


def test_unifiedmetamodel__actioncreator_constructor_exists():
    assert callable(UnifiedMetamodel__ActionCreator.__init__)


def test_unifiedmetamodel__actioncreator_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__ActionCreator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__actioncreator_has_name():
    assert hasattr(UnifiedMetamodel__ActionCreator, "name")
    descriptor = None
    for klass in UnifiedMetamodel__ActionCreator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__actiondispatcher_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__ActionDispatcher)


def test_unifiedmetamodel__actiondispatcher_constructor_exists():
    assert callable(UnifiedMetamodel__ActionDispatcher.__init__)


def test_unifiedmetamodel__actiondispatcher_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__ActionDispatcher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__actiondispatcher_has_name():
    assert hasattr(UnifiedMetamodel__ActionDispatcher, "name")
    descriptor = None
    for klass in UnifiedMetamodel__ActionDispatcher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__relationdom_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__RelationDom)


def test_unifiedmetamodel__relationdom_constructor_exists():
    assert callable(UnifiedMetamodel__RelationDom.__init__)


def test_unifiedmetamodel__relationdom_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__RelationDom.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__property_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Property)


def test_unifiedmetamodel__property_constructor_exists():
    assert callable(UnifiedMetamodel__Property.__init__)


def test_unifiedmetamodel__property_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Property.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__property_has_type():
    assert hasattr(UnifiedMetamodel__Property, "type")
    descriptor = None
    for klass in UnifiedMetamodel__Property.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_unifiedmetamodel__property_has_name():
    assert hasattr(UnifiedMetamodel__Property, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__generalentity_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__GeneralEntity)


def test_unifiedmetamodel__generalentity_constructor_exists():
    assert callable(UnifiedMetamodel__GeneralEntity.__init__)


def test_unifiedmetamodel__generalentity_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__GeneralEntity.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__submodule_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Submodule)


def test_unifiedmetamodel__submodule_constructor_exists():
    assert callable(UnifiedMetamodel__Submodule.__init__)


def test_unifiedmetamodel__submodule_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Submodule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__submodule_has_name():
    assert hasattr(UnifiedMetamodel__Submodule, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Submodule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__module_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Module)


def test_unifiedmetamodel__module_constructor_exists():
    assert callable(UnifiedMetamodel__Module.__init__)


def test_unifiedmetamodel__module_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__module_has_name():
    assert hasattr(UnifiedMetamodel__Module, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__arquitecturemetamodel_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__ArquitectureMetamodel)


def test_unifiedmetamodel__arquitecturemetamodel_constructor_exists():
    assert callable(UnifiedMetamodel__ArquitectureMetamodel.__init__)


def test_unifiedmetamodel__arquitecturemetamodel_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__ArquitectureMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__entity_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Entity)


def test_unifiedmetamodel__entity_constructor_exists():
    assert callable(UnifiedMetamodel__Entity.__init__)


def test_unifiedmetamodel__entity_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__entity_has_name():
    assert hasattr(UnifiedMetamodel__Entity, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__operations_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Operations)


def test_unifiedmetamodel__operations_constructor_exists():
    assert callable(UnifiedMetamodel__Operations.__init__)


def test_unifiedmetamodel__operations_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Operations.__init__)
    params = list(sig.parameters.keys())



def test_relationdom_is_not_abstract():
    assert not inspect.isabstract(RelationDom)


def test_relationdom_constructor_exists():
    assert callable(RelationDom.__init__)


def test_relationdom_constructor_args():
    sig = inspect.signature(RelationDom.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__composition_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Composition)


def test_unifiedmetamodel__composition_constructor_exists():
    assert callable(UnifiedMetamodel__Composition.__init__)


def test_unifiedmetamodel__composition_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Composition.__init__)
    params = list(sig.parameters.keys())



def test_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__exchange_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Exchange)


def test_unifiedmetamodel__exchange_constructor_exists():
    assert callable(UnifiedMetamodel__Exchange.__init__)


def test_unifiedmetamodel__exchange_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Exchange.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__sale_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Sale)


def test_unifiedmetamodel__sale_constructor_exists():
    assert callable(UnifiedMetamodel__Sale.__init__)


def test_unifiedmetamodel__sale_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Sale.__init__)
    params = list(sig.parameters.keys())



def test_operations_is_not_abstract():
    assert not inspect.isabstract(Operations)


def test_operations_constructor_exists():
    assert callable(Operations.__init__)


def test_operations_constructor_args():
    sig = inspect.signature(Operations.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__create_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Create)


def test_unifiedmetamodel__create_constructor_exists():
    assert callable(UnifiedMetamodel__Create.__init__)


def test_unifiedmetamodel__create_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Create.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__read_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Read)


def test_unifiedmetamodel__read_constructor_exists():
    assert callable(UnifiedMetamodel__Read.__init__)


def test_unifiedmetamodel__read_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Read.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__technologymetamodel_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__TechnologyMetamodel)


def test_unifiedmetamodel__technologymetamodel_constructor_exists():
    assert callable(UnifiedMetamodel__TechnologyMetamodel.__init__)


def test_unifiedmetamodel__technologymetamodel_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__TechnologyMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__domainmetamodel_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__DomainMetamodel)


def test_unifiedmetamodel__domainmetamodel_constructor_exists():
    assert callable(UnifiedMetamodel__DomainMetamodel.__init__)


def test_unifiedmetamodel__domainmetamodel_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__DomainMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__metamodel_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Metamodel)


def test_unifiedmetamodel__metamodel_constructor_exists():
    assert callable(UnifiedMetamodel__Metamodel.__init__)


def test_unifiedmetamodel__metamodel_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Metamodel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__metamodel_has_name():
    assert hasattr(UnifiedMetamodel__Metamodel, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Metamodel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_layersegment_is_not_abstract():
    assert not inspect.isabstract(LayerSegment)


def test_layersegment_constructor_exists():
    assert callable(LayerSegment.__init__)


def test_layersegment_constructor_args():
    sig = inspect.signature(LayerSegment.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__ui_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__UI)


def test_unifiedmetamodel__ui_constructor_exists():
    assert callable(UnifiedMetamodel__UI.__init__)


def test_unifiedmetamodel__ui_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__UI.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__containers_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Containers)


def test_unifiedmetamodel__containers_constructor_exists():
    assert callable(UnifiedMetamodel__Containers.__init__)


def test_unifiedmetamodel__containers_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Containers.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__pojo_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Pojo)


def test_unifiedmetamodel__pojo_constructor_exists():
    assert callable(UnifiedMetamodel__Pojo.__init__)


def test_unifiedmetamodel__pojo_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Pojo.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__services_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Services)


def test_unifiedmetamodel__services_constructor_exists():
    assert callable(UnifiedMetamodel__Services.__init__)


def test_unifiedmetamodel__services_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Services.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__util_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Util)


def test_unifiedmetamodel__util_constructor_exists():
    assert callable(UnifiedMetamodel__Util.__init__)


def test_unifiedmetamodel__util_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Util.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__store_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Store)


def test_unifiedmetamodel__store_constructor_exists():
    assert callable(UnifiedMetamodel__Store.__init__)


def test_unifiedmetamodel__store_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Store.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__dto_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Dto)


def test_unifiedmetamodel__dto_constructor_exists():
    assert callable(UnifiedMetamodel__Dto.__init__)


def test_unifiedmetamodel__dto_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Dto.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__relationarch_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__RelationArch)


def test_unifiedmetamodel__relationarch_constructor_exists():
    assert callable(UnifiedMetamodel__RelationArch.__init__)


def test_unifiedmetamodel__relationarch_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__RelationArch.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__relationarch_has_name():
    assert hasattr(UnifiedMetamodel__RelationArch, "name")
    descriptor = None
    for klass in UnifiedMetamodel__RelationArch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__component_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Component)


def test_unifiedmetamodel__component_constructor_exists():
    assert callable(UnifiedMetamodel__Component.__init__)


def test_unifiedmetamodel__component_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__component_has_name():
    assert hasattr(UnifiedMetamodel__Component, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__facade_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Facade)


def test_unifiedmetamodel__facade_constructor_exists():
    assert callable(UnifiedMetamodel__Facade.__init__)


def test_unifiedmetamodel__facade_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Facade.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__restentity_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__RestEntity)


def test_unifiedmetamodel__restentity_constructor_exists():
    assert callable(UnifiedMetamodel__RestEntity.__init__)


def test_unifiedmetamodel__restentity_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__RestEntity.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__layer_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Layer)


def test_unifiedmetamodel__layer_constructor_exists():
    assert callable(UnifiedMetamodel__Layer.__init__)


def test_unifiedmetamodel__layer_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Layer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_unifiedmetamodel__layer_has_name():
    assert hasattr(UnifiedMetamodel__Layer, "name")
    descriptor = None
    for klass in UnifiedMetamodel__Layer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unifiedmetamodel__sublayersegment_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__SubLayerSegment)


def test_unifiedmetamodel__sublayersegment_constructor_exists():
    assert callable(UnifiedMetamodel__SubLayerSegment.__init__)


def test_unifiedmetamodel__sublayersegment_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__SubLayerSegment.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__layersegment_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__LayerSegment)


def test_unifiedmetamodel__layersegment_constructor_exists():
    assert callable(UnifiedMetamodel__LayerSegment.__init__)


def test_unifiedmetamodel__layersegment_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__LayerSegment.__init__)
    params = list(sig.parameters.keys())



def test_layer_is_not_abstract():
    assert not inspect.isabstract(Layer)


def test_layer_constructor_exists():
    assert callable(Layer.__init__)


def test_layer_constructor_args():
    sig = inspect.signature(Layer.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__javascript_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__JavaScript)


def test_unifiedmetamodel__javascript_constructor_exists():
    assert callable(UnifiedMetamodel__JavaScript.__init__)


def test_unifiedmetamodel__javascript_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__JavaScript.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__war_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__War)


def test_unifiedmetamodel__war_constructor_exists():
    assert callable(UnifiedMetamodel__War.__init__)


def test_unifiedmetamodel__war_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__War.__init__)
    params = list(sig.parameters.keys())



def test_unifiedmetamodel__ejb_is_not_abstract():
    assert not inspect.isabstract(UnifiedMetamodel__Ejb)


def test_unifiedmetamodel__ejb_constructor_exists():
    assert callable(UnifiedMetamodel__Ejb.__init__)


def test_unifiedmetamodel__ejb_constructor_args():
    sig = inspect.signature(UnifiedMetamodel__Ejb.__init__)
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
Component_strategy = st.builds(
    Component,
)
UnifiedMetamodel__Front_strategy = st.builds(
    UnifiedMetamodel__Front,
)
UnifiedMetamodel__Back_strategy = st.builds(
    UnifiedMetamodel__Back,
)
SubLayerSegment_strategy = st.builds(
    SubLayerSegment,
)
UnifiedMetamodel__Actions_strategy = st.builds(
    UnifiedMetamodel__Actions,
)
UnifiedMetamodel__Reducers_strategy = st.builds(
    UnifiedMetamodel__Reducers,
)
UnifiedMetamodel__Descriptor_strategy = st.builds(
    UnifiedMetamodel__Descriptor,
    name=
        safe_text,
    path=
        safe_text
)
UnifiedMetamodel__AbstractMethod_strategy = st.builds(
    UnifiedMetamodel__AbstractMethod,
    name=
        safe_text
)
UnifiedMetamodel__EInterface_strategy = st.builds(
    UnifiedMetamodel__EInterface,
    name=
        safe_text
)
EClass_strategy = st.builds(
    EClass,
)
UnifiedMetamodel__NativeClass_strategy = st.builds(
    UnifiedMetamodel__NativeClass,
    primitiveRef=
        safe_text
)
UnifiedMetamodel__Subproject_strategy = st.builds(
    UnifiedMetamodel__Subproject,
    name=
        safe_text
)
UnifiedMetamodel__Epackage_strategy = st.builds(
    UnifiedMetamodel__Epackage,
    name=
        safe_text
)
UnifiedMetamodel__MethodBack_strategy = st.builds(
    UnifiedMetamodel__MethodBack,
    name=
        safe_text
)
UnifiedMetamodel__AbstractClass_strategy = st.builds(
    UnifiedMetamodel__AbstractClass,
)
UnifiedMetamodel__GenericClass_strategy = st.builds(
    UnifiedMetamodel__GenericClass,
)
UnifiedMetamodel__EClass_strategy = st.builds(
    UnifiedMetamodel__EClass,
    name=
        safe_text
)
UnifiedMetamodel__Attribute_strategy = st.builds(
    UnifiedMetamodel__Attribute,
    name=
        safe_text
)
UnifiedMetamodel__Annotation_strategy = st.builds(
    UnifiedMetamodel__Annotation,
    properties=
        safe_text
)
UnifiedMetamodel__Library_strategy = st.builds(
    UnifiedMetamodel__Library,
    name=
        safe_text,
    isNative=
        st.booleans()
)
UnifiedMetamodel__ReactApp_strategy = st.builds(
    UnifiedMetamodel__ReactApp,
)
UnifiedMetamodel__JEE_Project_strategy = st.builds(
    UnifiedMetamodel__JEE_Project,
    name=
        safe_text
)
UnifiedMetamodel__JavaApp_strategy = st.builds(
    UnifiedMetamodel__JavaApp,
)
UnifiedMetamodel__ModuleFront_strategy = st.builds(
    UnifiedMetamodel__ModuleFront,
    name=
        safe_text
)
UnifiedMetamodel__Reducer_strategy = st.builds(
    UnifiedMetamodel__Reducer,
    name=
        safe_text
)
UnifiedMetamodel__Action_strategy = st.builds(
    UnifiedMetamodel__Action,
    name=
        safe_text
)
UnifiedMetamodel__State_strategy = st.builds(
    UnifiedMetamodel__State,
)
UnifiedMetamodel__ComponentFront_strategy = st.builds(
    UnifiedMetamodel__ComponentFront,
    name=
        safe_text
)
UnifiedMetamodel__Functionality_strategy = st.builds(
    UnifiedMetamodel__Functionality,
    name=
        safe_text
)
UnifiedMetamodel__ServicesFront_strategy = st.builds(
    UnifiedMetamodel__ServicesFront,
    name=
        safe_text
)
UIFront_strategy = st.builds(
    UIFront,
)
UnifiedMetamodel__RouterComponent_strategy = st.builds(
    UnifiedMetamodel__RouterComponent,
)
UnifiedMetamodel__Visualizer_strategy = st.builds(
    UnifiedMetamodel__Visualizer,
)
ComponentFront_strategy = st.builds(
    ComponentFront,
)
UnifiedMetamodel__Container_strategy = st.builds(
    UnifiedMetamodel__Container,
)
UnifiedMetamodel__UIFront_strategy = st.builds(
    UnifiedMetamodel__UIFront,
)
UnifiedMetamodel__Transaction_strategy = st.builds(
    UnifiedMetamodel__Transaction,
)
Entity_strategy = st.builds(
    Entity,
)
UnifiedMetamodel__SpecialEntity_strategy = st.builds(
    UnifiedMetamodel__SpecialEntity,
)
UnifiedMetamodel__File_strategy = st.builds(
    UnifiedMetamodel__File,
    type=
        safe_text,
    name=
        safe_text
)
UnifiedMetamodel__Directory_strategy = st.builds(
    UnifiedMetamodel__Directory,
    name=
        safe_text,
    purpose=
        safe_text,
    isRoot=
        st.booleans()
)
File_strategy = st.builds(
    File,
)
UnifiedMetamodel__JS_strategy = st.builds(
    UnifiedMetamodel__JS,
)
UnifiedMetamodel__MD_strategy = st.builds(
    UnifiedMetamodel__MD,
)
UnifiedMetamodel__CSS_strategy = st.builds(
    UnifiedMetamodel__CSS,
)
UnifiedMetamodel__JSON_strategy = st.builds(
    UnifiedMetamodel__JSON,
)
ModuleFront_strategy = st.builds(
    ModuleFront,
)
UnifiedMetamodel__React_strategy = st.builds(
    UnifiedMetamodel__React,
)
UnifiedMetamodel__APICall_strategy = st.builds(
    UnifiedMetamodel__APICall,
)
UnifiedMetamodel__Redux_strategy = st.builds(
    UnifiedMetamodel__Redux,
)
UnifiedMetamodel__Design_strategy = st.builds(
    UnifiedMetamodel__Design,
)
UnifiedMetamodel__Router_strategy = st.builds(
    UnifiedMetamodel__Router,
)
UnifiedMetamodel__ActionCreator_strategy = st.builds(
    UnifiedMetamodel__ActionCreator,
    name=
        safe_text
)
UnifiedMetamodel__ActionDispatcher_strategy = st.builds(
    UnifiedMetamodel__ActionDispatcher,
    name=
        safe_text
)
UnifiedMetamodel__RelationDom_strategy = st.builds(
    UnifiedMetamodel__RelationDom,
)
UnifiedMetamodel__Property_strategy = st.builds(
    UnifiedMetamodel__Property,
    type=
        safe_text,
    name=
        safe_text
)
UnifiedMetamodel__GeneralEntity_strategy = st.builds(
    UnifiedMetamodel__GeneralEntity,
)
UnifiedMetamodel__Submodule_strategy = st.builds(
    UnifiedMetamodel__Submodule,
    name=
        safe_text
)
UnifiedMetamodel__Module_strategy = st.builds(
    UnifiedMetamodel__Module,
    name=
        safe_text
)
UnifiedMetamodel__ArquitectureMetamodel_strategy = st.builds(
    UnifiedMetamodel__ArquitectureMetamodel,
)
UnifiedMetamodel__Entity_strategy = st.builds(
    UnifiedMetamodel__Entity,
    name=
        safe_text
)
UnifiedMetamodel__Operations_strategy = st.builds(
    UnifiedMetamodel__Operations,
)
RelationDom_strategy = st.builds(
    RelationDom,
)
UnifiedMetamodel__Composition_strategy = st.builds(
    UnifiedMetamodel__Composition,
)
Transaction_strategy = st.builds(
    Transaction,
)
UnifiedMetamodel__Exchange_strategy = st.builds(
    UnifiedMetamodel__Exchange,
)
UnifiedMetamodel__Sale_strategy = st.builds(
    UnifiedMetamodel__Sale,
)
Operations_strategy = st.builds(
    Operations,
)
UnifiedMetamodel__Create_strategy = st.builds(
    UnifiedMetamodel__Create,
)
UnifiedMetamodel__Read_strategy = st.builds(
    UnifiedMetamodel__Read,
)
UnifiedMetamodel__TechnologyMetamodel_strategy = st.builds(
    UnifiedMetamodel__TechnologyMetamodel,
)
UnifiedMetamodel__DomainMetamodel_strategy = st.builds(
    UnifiedMetamodel__DomainMetamodel,
)
UnifiedMetamodel__Metamodel_strategy = st.builds(
    UnifiedMetamodel__Metamodel,
    name=
        safe_text
)
LayerSegment_strategy = st.builds(
    LayerSegment,
)
UnifiedMetamodel__UI_strategy = st.builds(
    UnifiedMetamodel__UI,
)
UnifiedMetamodel__Containers_strategy = st.builds(
    UnifiedMetamodel__Containers,
)
UnifiedMetamodel__Pojo_strategy = st.builds(
    UnifiedMetamodel__Pojo,
)
UnifiedMetamodel__Services_strategy = st.builds(
    UnifiedMetamodel__Services,
)
UnifiedMetamodel__Util_strategy = st.builds(
    UnifiedMetamodel__Util,
)
UnifiedMetamodel__Store_strategy = st.builds(
    UnifiedMetamodel__Store,
)
UnifiedMetamodel__Dto_strategy = st.builds(
    UnifiedMetamodel__Dto,
)
UnifiedMetamodel__RelationArch_strategy = st.builds(
    UnifiedMetamodel__RelationArch,
    name=
        safe_text
)
UnifiedMetamodel__Component_strategy = st.builds(
    UnifiedMetamodel__Component,
    name=
        safe_text
)
UnifiedMetamodel__Facade_strategy = st.builds(
    UnifiedMetamodel__Facade,
)
UnifiedMetamodel__RestEntity_strategy = st.builds(
    UnifiedMetamodel__RestEntity,
)
UnifiedMetamodel__Layer_strategy = st.builds(
    UnifiedMetamodel__Layer,
    name=
        safe_text
)
UnifiedMetamodel__SubLayerSegment_strategy = st.builds(
    UnifiedMetamodel__SubLayerSegment,
)
UnifiedMetamodel__LayerSegment_strategy = st.builds(
    UnifiedMetamodel__LayerSegment,
)
Layer_strategy = st.builds(
    Layer,
)
UnifiedMetamodel__JavaScript_strategy = st.builds(
    UnifiedMetamodel__JavaScript,
)
UnifiedMetamodel__War_strategy = st.builds(
    UnifiedMetamodel__War,
)
UnifiedMetamodel__Ejb_strategy = st.builds(
    UnifiedMetamodel__Ejb,
)

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=UnifiedMetamodel__Front_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__front_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Front)

@given(instance=UnifiedMetamodel__Back_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__back_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Back)

@given(instance=SubLayerSegment_strategy)
@settings(max_examples=50)
def test_sublayersegment_instantiation(instance):
    assert isinstance(instance, SubLayerSegment)

@given(instance=UnifiedMetamodel__Actions_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__actions_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Actions)

@given(instance=UnifiedMetamodel__Reducers_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__reducers_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Reducers)

@given(instance=UnifiedMetamodel__Descriptor_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__descriptor_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Descriptor)



@given(instance=UnifiedMetamodel__Descriptor_strategy)
def test_unifiedmetamodel__descriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=UnifiedMetamodel__Descriptor_strategy)
def test_unifiedmetamodel__descriptor_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=UnifiedMetamodel__AbstractMethod_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__abstractmethod_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__AbstractMethod)



@given(instance=UnifiedMetamodel__AbstractMethod_strategy)
def test_unifiedmetamodel__abstractmethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__EInterface_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__einterface_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__EInterface)



@given(instance=UnifiedMetamodel__EInterface_strategy)
def test_unifiedmetamodel__einterface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=UnifiedMetamodel__NativeClass_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__nativeclass_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__NativeClass)



@given(instance=UnifiedMetamodel__NativeClass_strategy)
def test_unifiedmetamodel__nativeclass_primitiveRef_setter(instance):
    original = instance.primitiveRef
    instance.primitiveRef = original
    assert instance.primitiveRef == original

@given(instance=UnifiedMetamodel__Subproject_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__subproject_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Subproject)



@given(instance=UnifiedMetamodel__Subproject_strategy)
def test_unifiedmetamodel__subproject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Epackage_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__epackage_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Epackage)



@given(instance=UnifiedMetamodel__Epackage_strategy)
def test_unifiedmetamodel__epackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__MethodBack_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__methodback_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__MethodBack)



@given(instance=UnifiedMetamodel__MethodBack_strategy)
def test_unifiedmetamodel__methodback_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__AbstractClass_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__abstractclass_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__AbstractClass)

@given(instance=UnifiedMetamodel__GenericClass_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__genericclass_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__GenericClass)

@given(instance=UnifiedMetamodel__EClass_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__eclass_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__EClass)



@given(instance=UnifiedMetamodel__EClass_strategy)
def test_unifiedmetamodel__eclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Attribute_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__attribute_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Attribute)



@given(instance=UnifiedMetamodel__Attribute_strategy)
def test_unifiedmetamodel__attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Annotation_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__annotation_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Annotation)



@given(instance=UnifiedMetamodel__Annotation_strategy)
def test_unifiedmetamodel__annotation_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original

@given(instance=UnifiedMetamodel__Library_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__library_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Library)



@given(instance=UnifiedMetamodel__Library_strategy)
def test_unifiedmetamodel__library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=UnifiedMetamodel__Library_strategy)
def test_unifiedmetamodel__library_isNative_setter(instance):
    original = instance.isNative
    instance.isNative = original
    assert instance.isNative == original

@given(instance=UnifiedMetamodel__ReactApp_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__reactapp_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__ReactApp)

@given(instance=UnifiedMetamodel__JEE_Project_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__jee_project_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__JEE_Project)



@given(instance=UnifiedMetamodel__JEE_Project_strategy)
def test_unifiedmetamodel__jee_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__JavaApp_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__javaapp_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__JavaApp)

@given(instance=UnifiedMetamodel__ModuleFront_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__modulefront_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__ModuleFront)



@given(instance=UnifiedMetamodel__ModuleFront_strategy)
def test_unifiedmetamodel__modulefront_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Reducer_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__reducer_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Reducer)



@given(instance=UnifiedMetamodel__Reducer_strategy)
def test_unifiedmetamodel__reducer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Action_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__action_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Action)



@given(instance=UnifiedMetamodel__Action_strategy)
def test_unifiedmetamodel__action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__State_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__state_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__State)

@given(instance=UnifiedMetamodel__ComponentFront_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__componentfront_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__ComponentFront)



@given(instance=UnifiedMetamodel__ComponentFront_strategy)
def test_unifiedmetamodel__componentfront_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Functionality_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__functionality_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Functionality)



@given(instance=UnifiedMetamodel__Functionality_strategy)
def test_unifiedmetamodel__functionality_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__ServicesFront_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__servicesfront_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__ServicesFront)



@given(instance=UnifiedMetamodel__ServicesFront_strategy)
def test_unifiedmetamodel__servicesfront_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UIFront_strategy)
@settings(max_examples=50)
def test_uifront_instantiation(instance):
    assert isinstance(instance, UIFront)

@given(instance=UnifiedMetamodel__RouterComponent_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__routercomponent_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__RouterComponent)

@given(instance=UnifiedMetamodel__Visualizer_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__visualizer_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Visualizer)

@given(instance=ComponentFront_strategy)
@settings(max_examples=50)
def test_componentfront_instantiation(instance):
    assert isinstance(instance, ComponentFront)

@given(instance=UnifiedMetamodel__Container_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__container_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Container)

@given(instance=UnifiedMetamodel__UIFront_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__uifront_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__UIFront)

@given(instance=UnifiedMetamodel__Transaction_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__transaction_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Transaction)

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=UnifiedMetamodel__SpecialEntity_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__specialentity_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__SpecialEntity)

@given(instance=UnifiedMetamodel__File_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__file_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__File)



@given(instance=UnifiedMetamodel__File_strategy)
def test_unifiedmetamodel__file_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=UnifiedMetamodel__File_strategy)
def test_unifiedmetamodel__file_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Directory_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__directory_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Directory)



@given(instance=UnifiedMetamodel__Directory_strategy)
def test_unifiedmetamodel__directory_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=UnifiedMetamodel__Directory_strategy)
def test_unifiedmetamodel__directory_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original



@given(instance=UnifiedMetamodel__Directory_strategy)
def test_unifiedmetamodel__directory_isRoot_setter(instance):
    original = instance.isRoot
    instance.isRoot = original
    assert instance.isRoot == original

@given(instance=File_strategy)
@settings(max_examples=50)
def test_file_instantiation(instance):
    assert isinstance(instance, File)

@given(instance=UnifiedMetamodel__JS_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__js_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__JS)

@given(instance=UnifiedMetamodel__MD_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__md_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__MD)

@given(instance=UnifiedMetamodel__CSS_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__css_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__CSS)

@given(instance=UnifiedMetamodel__JSON_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__json_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__JSON)

@given(instance=ModuleFront_strategy)
@settings(max_examples=50)
def test_modulefront_instantiation(instance):
    assert isinstance(instance, ModuleFront)

@given(instance=UnifiedMetamodel__React_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__react_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__React)

@given(instance=UnifiedMetamodel__APICall_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__apicall_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__APICall)

@given(instance=UnifiedMetamodel__Redux_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__redux_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Redux)

@given(instance=UnifiedMetamodel__Design_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__design_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Design)

@given(instance=UnifiedMetamodel__Router_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__router_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Router)

@given(instance=UnifiedMetamodel__ActionCreator_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__actioncreator_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__ActionCreator)



@given(instance=UnifiedMetamodel__ActionCreator_strategy)
def test_unifiedmetamodel__actioncreator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__ActionDispatcher_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__actiondispatcher_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__ActionDispatcher)



@given(instance=UnifiedMetamodel__ActionDispatcher_strategy)
def test_unifiedmetamodel__actiondispatcher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__RelationDom_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__relationdom_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__RelationDom)

@given(instance=UnifiedMetamodel__Property_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__property_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Property)



@given(instance=UnifiedMetamodel__Property_strategy)
def test_unifiedmetamodel__property_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=UnifiedMetamodel__Property_strategy)
def test_unifiedmetamodel__property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__GeneralEntity_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__generalentity_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__GeneralEntity)

@given(instance=UnifiedMetamodel__Submodule_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__submodule_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Submodule)



@given(instance=UnifiedMetamodel__Submodule_strategy)
def test_unifiedmetamodel__submodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Module_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__module_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Module)



@given(instance=UnifiedMetamodel__Module_strategy)
def test_unifiedmetamodel__module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__ArquitectureMetamodel_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__arquitecturemetamodel_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__ArquitectureMetamodel)

@given(instance=UnifiedMetamodel__Entity_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__entity_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Entity)



@given(instance=UnifiedMetamodel__Entity_strategy)
def test_unifiedmetamodel__entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Operations_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__operations_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Operations)

@given(instance=RelationDom_strategy)
@settings(max_examples=50)
def test_relationdom_instantiation(instance):
    assert isinstance(instance, RelationDom)

@given(instance=UnifiedMetamodel__Composition_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__composition_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Composition)

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)

@given(instance=UnifiedMetamodel__Exchange_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__exchange_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Exchange)

@given(instance=UnifiedMetamodel__Sale_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__sale_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Sale)

@given(instance=Operations_strategy)
@settings(max_examples=50)
def test_operations_instantiation(instance):
    assert isinstance(instance, Operations)

@given(instance=UnifiedMetamodel__Create_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__create_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Create)

@given(instance=UnifiedMetamodel__Read_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__read_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Read)

@given(instance=UnifiedMetamodel__TechnologyMetamodel_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__technologymetamodel_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__TechnologyMetamodel)

@given(instance=UnifiedMetamodel__DomainMetamodel_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__domainmetamodel_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__DomainMetamodel)

@given(instance=UnifiedMetamodel__Metamodel_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__metamodel_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Metamodel)



@given(instance=UnifiedMetamodel__Metamodel_strategy)
def test_unifiedmetamodel__metamodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LayerSegment_strategy)
@settings(max_examples=50)
def test_layersegment_instantiation(instance):
    assert isinstance(instance, LayerSegment)

@given(instance=UnifiedMetamodel__UI_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__ui_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__UI)

@given(instance=UnifiedMetamodel__Containers_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__containers_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Containers)

@given(instance=UnifiedMetamodel__Pojo_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__pojo_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Pojo)

@given(instance=UnifiedMetamodel__Services_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__services_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Services)

@given(instance=UnifiedMetamodel__Util_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__util_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Util)

@given(instance=UnifiedMetamodel__Store_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__store_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Store)

@given(instance=UnifiedMetamodel__Dto_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__dto_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Dto)

@given(instance=UnifiedMetamodel__RelationArch_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__relationarch_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__RelationArch)



@given(instance=UnifiedMetamodel__RelationArch_strategy)
def test_unifiedmetamodel__relationarch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Component_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__component_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Component)



@given(instance=UnifiedMetamodel__Component_strategy)
def test_unifiedmetamodel__component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__Facade_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__facade_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Facade)

@given(instance=UnifiedMetamodel__RestEntity_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__restentity_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__RestEntity)

@given(instance=UnifiedMetamodel__Layer_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__layer_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Layer)



@given(instance=UnifiedMetamodel__Layer_strategy)
def test_unifiedmetamodel__layer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UnifiedMetamodel__SubLayerSegment_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__sublayersegment_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__SubLayerSegment)

@given(instance=UnifiedMetamodel__LayerSegment_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__layersegment_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__LayerSegment)

@given(instance=Layer_strategy)
@settings(max_examples=50)
def test_layer_instantiation(instance):
    assert isinstance(instance, Layer)

@given(instance=UnifiedMetamodel__JavaScript_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__javascript_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__JavaScript)

@given(instance=UnifiedMetamodel__War_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__war_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__War)

@given(instance=UnifiedMetamodel__Ejb_strategy)
@settings(max_examples=50)
def test_unifiedmetamodel__ejb_instantiation(instance):
    assert isinstance(instance, UnifiedMetamodel__Ejb)
