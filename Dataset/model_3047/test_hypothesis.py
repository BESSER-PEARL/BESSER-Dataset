import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Selection,
    classLayout2Frontend::Views::Autocomplete,
    classLayout2Frontend::Views::RadioButtonGroup,
    classLayout2Frontend::Views::List,
    classLayout2Frontend::Views::CheckList,
    classLayout2Frontend::Views::Dropdownlist,
    classLayout2Frontend::Views::IterationFilter,
    classLayout2Frontend::Views::PageView,
    IterationFilter,
    classLayout2Frontend::Views::ElementView,
    ElementView,
    classLayout2Frontend::Views::AtomicView,
    classLayout2Frontend::Views::ContainerView,
    classLayout2Frontend::Views::SiteView,
    Output,
    classLayout2Frontend::Views::Image,
    classLayout2Frontend::Views::TextArea,
    Input,
    classLayout2Frontend::Views::Selection,
    classLayout2Frontend::Views::FileUpload,
    classLayout2Frontend::Views::InputText,
    AtomicView,
    classLayout2Frontend::Views::Output,
    classLayout2Frontend::Views::Input,
    Association,
    classLayout2Frontend::Entities::Reference,
    classLayout2Frontend::Entities::Composition,
    Entity,
    StructuralFeature,
    classLayout2Frontend::Entities::Association,
    classLayout2Frontend::Entities::EntityModelElement,
    EntityModelElement,
    classLayout2Frontend::Entities::Entity,
    classLayout2Frontend::Entities::StructuralFeature,
    classLayout2Frontend::Entities::EntitiesModel,
    ContainerView,
    classLayout2Frontend::Views::StaticContainer,
    classLayout2Frontend::Views::InputForm,
    classLayout2Frontend::Views::IterationContainer,
    classLayout2Frontend::Entities::Literal,
    classLayout2Frontend::Entities::PropertyType,
    Literal,
    PropertyType,
    classLayout2Frontend::Entities::Enumeration,
    classLayout2Frontend::Entities::PrimitiveType,
    classLayout2Frontend::Entities::Property,
    PageView,
    SiteView,
    EntitiesModel,
    classLayout2Frontend::Project,
    LayoutType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_selection_is_not_abstract():
    assert not inspect.isabstract(Selection)


def test_selection_constructor_exists():
    assert callable(Selection.__init__)


def test_selection_constructor_args():
    sig = inspect.signature(Selection.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::autocomplete_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::Autocomplete)


def test_classlayout2frontend::views::autocomplete_constructor_exists():
    assert callable(classLayout2Frontend::Views::Autocomplete.__init__)


def test_classlayout2frontend::views::autocomplete_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::Autocomplete.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_classlayout2frontend::views::autocomplete_has_multiple():
    assert hasattr(classLayout2Frontend::Views::Autocomplete, "multiple")
    descriptor = None
    for klass in classLayout2Frontend::Views::Autocomplete.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::views::radiobuttongroup_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::RadioButtonGroup)


def test_classlayout2frontend::views::radiobuttongroup_constructor_exists():
    assert callable(classLayout2Frontend::Views::RadioButtonGroup.__init__)


def test_classlayout2frontend::views::radiobuttongroup_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::RadioButtonGroup.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::list_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::List)


def test_classlayout2frontend::views::list_constructor_exists():
    assert callable(classLayout2Frontend::Views::List.__init__)


def test_classlayout2frontend::views::list_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::List.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_classlayout2frontend::views::list_has_multiple():
    assert hasattr(classLayout2Frontend::Views::List, "multiple")
    descriptor = None
    for klass in classLayout2Frontend::Views::List.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::views::checklist_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::CheckList)


def test_classlayout2frontend::views::checklist_constructor_exists():
    assert callable(classLayout2Frontend::Views::CheckList.__init__)


def test_classlayout2frontend::views::checklist_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::CheckList.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::dropdownlist_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::Dropdownlist)


def test_classlayout2frontend::views::dropdownlist_constructor_exists():
    assert callable(classLayout2Frontend::Views::Dropdownlist.__init__)


def test_classlayout2frontend::views::dropdownlist_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::Dropdownlist.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::iterationfilter_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::IterationFilter)


def test_classlayout2frontend::views::iterationfilter_constructor_exists():
    assert callable(classLayout2Frontend::Views::IterationFilter.__init__)


def test_classlayout2frontend::views::iterationfilter_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::IterationFilter.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::pageview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::PageView)


def test_classlayout2frontend::views::pageview_constructor_exists():
    assert callable(classLayout2Frontend::Views::PageView.__init__)


def test_classlayout2frontend::views::pageview_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::PageView.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "layoutType" in params, "Missing parameter 'layoutType'"

def test_classlayout2frontend::views::pageview_has_name():
    assert hasattr(classLayout2Frontend::Views::PageView, "name")
    descriptor = None
    for klass in classLayout2Frontend::Views::PageView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::views::pageview_has_layoutType():
    assert hasattr(classLayout2Frontend::Views::PageView, "layoutType")
    descriptor = None
    for klass in classLayout2Frontend::Views::PageView.__mro__:
        if "layoutType" in klass.__dict__:
            descriptor = klass.__dict__["layoutType"]
            break
    assert isinstance(descriptor, property)



def test_iterationfilter_is_not_abstract():
    assert not inspect.isabstract(IterationFilter)


def test_iterationfilter_constructor_exists():
    assert callable(IterationFilter.__init__)


def test_iterationfilter_constructor_args():
    sig = inspect.signature(IterationFilter.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::elementview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::ElementView)


def test_classlayout2frontend::views::elementview_constructor_exists():
    assert callable(classLayout2Frontend::Views::ElementView.__init__)


def test_classlayout2frontend::views::elementview_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::ElementView.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dsisplayName" in params, "Missing parameter 'dsisplayName'"
    assert "description" in params, "Missing parameter 'description'"

def test_classlayout2frontend::views::elementview_has_name():
    assert hasattr(classLayout2Frontend::Views::ElementView, "name")
    descriptor = None
    for klass in classLayout2Frontend::Views::ElementView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::views::elementview_has_dsisplayName():
    assert hasattr(classLayout2Frontend::Views::ElementView, "dsisplayName")
    descriptor = None
    for klass in classLayout2Frontend::Views::ElementView.__mro__:
        if "dsisplayName" in klass.__dict__:
            descriptor = klass.__dict__["dsisplayName"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::views::elementview_has_description():
    assert hasattr(classLayout2Frontend::Views::ElementView, "description")
    descriptor = None
    for klass in classLayout2Frontend::Views::ElementView.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_elementview_is_not_abstract():
    assert not inspect.isabstract(ElementView)


def test_elementview_constructor_exists():
    assert callable(ElementView.__init__)


def test_elementview_constructor_args():
    sig = inspect.signature(ElementView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::atomicview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::AtomicView)


def test_classlayout2frontend::views::atomicview_constructor_exists():
    assert callable(classLayout2Frontend::Views::AtomicView.__init__)


def test_classlayout2frontend::views::atomicview_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::AtomicView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::containerview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::ContainerView)


def test_classlayout2frontend::views::containerview_constructor_exists():
    assert callable(classLayout2Frontend::Views::ContainerView.__init__)


def test_classlayout2frontend::views::containerview_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::ContainerView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::siteview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::SiteView)


def test_classlayout2frontend::views::siteview_constructor_exists():
    assert callable(classLayout2Frontend::Views::SiteView.__init__)


def test_classlayout2frontend::views::siteview_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::SiteView.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "templateColor" in params, "Missing parameter 'templateColor'"
    assert "templateName" in params, "Missing parameter 'templateName'"
    assert "displayName" in params, "Missing parameter 'displayName'"

def test_classlayout2frontend::views::siteview_has_name():
    assert hasattr(classLayout2Frontend::Views::SiteView, "name")
    descriptor = None
    for klass in classLayout2Frontend::Views::SiteView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::views::siteview_has_templateColor():
    assert hasattr(classLayout2Frontend::Views::SiteView, "templateColor")
    descriptor = None
    for klass in classLayout2Frontend::Views::SiteView.__mro__:
        if "templateColor" in klass.__dict__:
            descriptor = klass.__dict__["templateColor"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::views::siteview_has_templateName():
    assert hasattr(classLayout2Frontend::Views::SiteView, "templateName")
    descriptor = None
    for klass in classLayout2Frontend::Views::SiteView.__mro__:
        if "templateName" in klass.__dict__:
            descriptor = klass.__dict__["templateName"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::views::siteview_has_displayName():
    assert hasattr(classLayout2Frontend::Views::SiteView, "displayName")
    descriptor = None
    for klass in classLayout2Frontend::Views::SiteView.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)



def test_output_is_not_abstract():
    assert not inspect.isabstract(Output)


def test_output_constructor_exists():
    assert callable(Output.__init__)


def test_output_constructor_args():
    sig = inspect.signature(Output.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::image_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::Image)


def test_classlayout2frontend::views::image_constructor_exists():
    assert callable(classLayout2Frontend::Views::Image.__init__)


def test_classlayout2frontend::views::image_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::Image.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_classlayout2frontend::views::image_has_height():
    assert hasattr(classLayout2Frontend::Views::Image, "height")
    descriptor = None
    for klass in classLayout2Frontend::Views::Image.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::views::image_has_width():
    assert hasattr(classLayout2Frontend::Views::Image, "width")
    descriptor = None
    for klass in classLayout2Frontend::Views::Image.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::views::textarea_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::TextArea)


def test_classlayout2frontend::views::textarea_constructor_exists():
    assert callable(classLayout2Frontend::Views::TextArea.__init__)


def test_classlayout2frontend::views::textarea_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::TextArea.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_classlayout2frontend::views::textarea_has_value():
    assert hasattr(classLayout2Frontend::Views::TextArea, "value")
    descriptor = None
    for klass in classLayout2Frontend::Views::TextArea.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_input_is_not_abstract():
    assert not inspect.isabstract(Input)


def test_input_constructor_exists():
    assert callable(Input.__init__)


def test_input_constructor_args():
    sig = inspect.signature(Input.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::selection_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::Selection)


def test_classlayout2frontend::views::selection_constructor_exists():
    assert callable(classLayout2Frontend::Views::Selection.__init__)


def test_classlayout2frontend::views::selection_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::Selection.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::fileupload_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::FileUpload)


def test_classlayout2frontend::views::fileupload_constructor_exists():
    assert callable(classLayout2Frontend::Views::FileUpload.__init__)


def test_classlayout2frontend::views::fileupload_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::FileUpload.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::inputtext_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::InputText)


def test_classlayout2frontend::views::inputtext_constructor_exists():
    assert callable(classLayout2Frontend::Views::InputText.__init__)


def test_classlayout2frontend::views::inputtext_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::InputText.__init__)
    params = list(sig.parameters.keys())
    assert "multiline" in params, "Missing parameter 'multiline'"

def test_classlayout2frontend::views::inputtext_has_multiline():
    assert hasattr(classLayout2Frontend::Views::InputText, "multiline")
    descriptor = None
    for klass in classLayout2Frontend::Views::InputText.__mro__:
        if "multiline" in klass.__dict__:
            descriptor = klass.__dict__["multiline"]
            break
    assert isinstance(descriptor, property)



def test_atomicview_is_not_abstract():
    assert not inspect.isabstract(AtomicView)


def test_atomicview_constructor_exists():
    assert callable(AtomicView.__init__)


def test_atomicview_constructor_args():
    sig = inspect.signature(AtomicView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::output_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::Output)


def test_classlayout2frontend::views::output_constructor_exists():
    assert callable(classLayout2Frontend::Views::Output.__init__)


def test_classlayout2frontend::views::output_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::Output.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::input_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::Input)


def test_classlayout2frontend::views::input_constructor_exists():
    assert callable(classLayout2Frontend::Views::Input.__init__)


def test_classlayout2frontend::views::input_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::Input.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_classlayout2frontend::views::input_has_label():
    assert hasattr(classLayout2Frontend::Views::Input, "label")
    descriptor = None
    for klass in classLayout2Frontend::Views::Input.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::entities::reference_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::Reference)


def test_classlayout2frontend::entities::reference_constructor_exists():
    assert callable(classLayout2Frontend::Entities::Reference.__init__)


def test_classlayout2frontend::entities::reference_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::Reference.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::entities::composition_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::Composition)


def test_classlayout2frontend::entities::composition_constructor_exists():
    assert callable(classLayout2Frontend::Entities::Composition.__init__)


def test_classlayout2frontend::entities::composition_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::Composition.__init__)
    params = list(sig.parameters.keys())



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::entities::association_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::Association)


def test_classlayout2frontend::entities::association_constructor_exists():
    assert callable(classLayout2Frontend::Entities::Association.__init__)


def test_classlayout2frontend::entities::association_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::Association.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_classlayout2frontend::entities::association_has_many():
    assert hasattr(classLayout2Frontend::Entities::Association, "many")
    descriptor = None
    for klass in classLayout2Frontend::Entities::Association.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::entities::entitymodelelement_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::EntityModelElement)


def test_classlayout2frontend::entities::entitymodelelement_constructor_exists():
    assert callable(classLayout2Frontend::Entities::EntityModelElement.__init__)


def test_classlayout2frontend::entities::entitymodelelement_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::EntityModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "displayName" in params, "Missing parameter 'displayName'"

def test_classlayout2frontend::entities::entitymodelelement_has_description():
    assert hasattr(classLayout2Frontend::Entities::EntityModelElement, "description")
    descriptor = None
    for klass in classLayout2Frontend::Entities::EntityModelElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::entities::entitymodelelement_has_name():
    assert hasattr(classLayout2Frontend::Entities::EntityModelElement, "name")
    descriptor = None
    for klass in classLayout2Frontend::Entities::EntityModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::entities::entitymodelelement_has_displayName():
    assert hasattr(classLayout2Frontend::Entities::EntityModelElement, "displayName")
    descriptor = None
    for klass in classLayout2Frontend::Entities::EntityModelElement.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)



def test_entitymodelelement_is_not_abstract():
    assert not inspect.isabstract(EntityModelElement)


def test_entitymodelelement_constructor_exists():
    assert callable(EntityModelElement.__init__)


def test_entitymodelelement_constructor_args():
    sig = inspect.signature(EntityModelElement.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::entities::entity_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::Entity)


def test_classlayout2frontend::entities::entity_constructor_exists():
    assert callable(classLayout2Frontend::Entities::Entity.__init__)


def test_classlayout2frontend::entities::entity_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_classlayout2frontend::entities::entity_has_isAbstract():
    assert hasattr(classLayout2Frontend::Entities::Entity, "isAbstract")
    descriptor = None
    for klass in classLayout2Frontend::Entities::Entity.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::entities::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::StructuralFeature)


def test_classlayout2frontend::entities::structuralfeature_constructor_exists():
    assert callable(classLayout2Frontend::Entities::StructuralFeature.__init__)


def test_classlayout2frontend::entities::structuralfeature_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"

def test_classlayout2frontend::entities::structuralfeature_has_required():
    assert hasattr(classLayout2Frontend::Entities::StructuralFeature, "required")
    descriptor = None
    for klass in classLayout2Frontend::Entities::StructuralFeature.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::entities::entitiesmodel_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::EntitiesModel)


def test_classlayout2frontend::entities::entitiesmodel_constructor_exists():
    assert callable(classLayout2Frontend::Entities::EntitiesModel.__init__)


def test_classlayout2frontend::entities::entitiesmodel_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::EntitiesModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend::entities::entitiesmodel_has_name():
    assert hasattr(classLayout2Frontend::Entities::EntitiesModel, "name")
    descriptor = None
    for klass in classLayout2Frontend::Entities::EntitiesModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_containerview_is_not_abstract():
    assert not inspect.isabstract(ContainerView)


def test_containerview_constructor_exists():
    assert callable(ContainerView.__init__)


def test_containerview_constructor_args():
    sig = inspect.signature(ContainerView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::staticcontainer_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::StaticContainer)


def test_classlayout2frontend::views::staticcontainer_constructor_exists():
    assert callable(classLayout2Frontend::Views::StaticContainer.__init__)


def test_classlayout2frontend::views::staticcontainer_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::StaticContainer.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::inputform_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::InputForm)


def test_classlayout2frontend::views::inputform_constructor_exists():
    assert callable(classLayout2Frontend::Views::InputForm.__init__)


def test_classlayout2frontend::views::inputform_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::InputForm.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::views::iterationcontainer_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Views::IterationContainer)


def test_classlayout2frontend::views::iterationcontainer_constructor_exists():
    assert callable(classLayout2Frontend::Views::IterationContainer.__init__)


def test_classlayout2frontend::views::iterationcontainer_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Views::IterationContainer.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::entities::literal_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::Literal)


def test_classlayout2frontend::entities::literal_constructor_exists():
    assert callable(classLayout2Frontend::Entities::Literal.__init__)


def test_classlayout2frontend::entities::literal_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_classlayout2frontend::entities::literal_has_value():
    assert hasattr(classLayout2Frontend::Entities::Literal, "value")
    descriptor = None
    for klass in classLayout2Frontend::Entities::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::entities::propertytype_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::PropertyType)


def test_classlayout2frontend::entities::propertytype_constructor_exists():
    assert callable(classLayout2Frontend::Entities::PropertyType.__init__)


def test_classlayout2frontend::entities::propertytype_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::entities::enumeration_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::Enumeration)


def test_classlayout2frontend::entities::enumeration_constructor_exists():
    assert callable(classLayout2Frontend::Entities::Enumeration.__init__)


def test_classlayout2frontend::entities::enumeration_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::entities::primitivetype_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::PrimitiveType)


def test_classlayout2frontend::entities::primitivetype_constructor_exists():
    assert callable(classLayout2Frontend::Entities::PrimitiveType.__init__)


def test_classlayout2frontend::entities::primitivetype_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::entities::property_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entities::Property)


def test_classlayout2frontend::entities::property_constructor_exists():
    assert callable(classLayout2Frontend::Entities::Property.__init__)


def test_classlayout2frontend::entities::property_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entities::Property.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_classlayout2frontend::entities::property_has_defaultValue():
    assert hasattr(classLayout2Frontend::Entities::Property, "defaultValue")
    descriptor = None
    for klass in classLayout2Frontend::Entities::Property.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_pageview_is_not_abstract():
    assert not inspect.isabstract(PageView)


def test_pageview_constructor_exists():
    assert callable(PageView.__init__)


def test_pageview_constructor_args():
    sig = inspect.signature(PageView.__init__)
    params = list(sig.parameters.keys())



def test_siteview_is_not_abstract():
    assert not inspect.isabstract(SiteView)


def test_siteview_constructor_exists():
    assert callable(SiteView.__init__)


def test_siteview_constructor_args():
    sig = inspect.signature(SiteView.__init__)
    params = list(sig.parameters.keys())



def test_entitiesmodel_is_not_abstract():
    assert not inspect.isabstract(EntitiesModel)


def test_entitiesmodel_constructor_exists():
    assert callable(EntitiesModel.__init__)


def test_entitiesmodel_constructor_args():
    sig = inspect.signature(EntitiesModel.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::project_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Project)


def test_classlayout2frontend::project_constructor_exists():
    assert callable(classLayout2Frontend::Project.__init__)


def test_classlayout2frontend::project_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend::project_has_name():
    assert hasattr(classLayout2Frontend::Project, "name")
    descriptor = None
    for klass in classLayout2Frontend::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_layouttype_exists():
    # Check that the Enumeration exists
    assert LayoutType is not None

def test_layouttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LayoutType]
    expected_literals = [
        "TWO_COLUMNS",
        "RIGHT_BAR",
        "SINGLE_COLUMN",
        "LEFT_BAR",
        "THREE_COLUMNS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LayoutType"


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
Selection_strategy = st.builds(
    Selection,
)
classLayout2Frontend::Views::Autocomplete_strategy = st.builds(
    classLayout2Frontend::Views::Autocomplete,
    multiple=
        st.booleans()
)
classLayout2Frontend::Views::RadioButtonGroup_strategy = st.builds(
    classLayout2Frontend::Views::RadioButtonGroup,
)
classLayout2Frontend::Views::List_strategy = st.builds(
    classLayout2Frontend::Views::List,
    multiple=
        st.booleans()
)
classLayout2Frontend::Views::CheckList_strategy = st.builds(
    classLayout2Frontend::Views::CheckList,
)
classLayout2Frontend::Views::Dropdownlist_strategy = st.builds(
    classLayout2Frontend::Views::Dropdownlist,
)
classLayout2Frontend::Views::IterationFilter_strategy = st.builds(
    classLayout2Frontend::Views::IterationFilter,
)
classLayout2Frontend::Views::PageView_strategy = st.builds(
    classLayout2Frontend::Views::PageView,
    name=
        safe_text,
    layoutType=
        safe_text
)
IterationFilter_strategy = st.builds(
    IterationFilter,
)
classLayout2Frontend::Views::ElementView_strategy = st.builds(
    classLayout2Frontend::Views::ElementView,
    name=
        safe_text,
    dsisplayName=
        safe_text,
    description=
        safe_text
)
ElementView_strategy = st.builds(
    ElementView,
)
classLayout2Frontend::Views::AtomicView_strategy = st.builds(
    classLayout2Frontend::Views::AtomicView,
)
classLayout2Frontend::Views::ContainerView_strategy = st.builds(
    classLayout2Frontend::Views::ContainerView,
)
classLayout2Frontend::Views::SiteView_strategy = st.builds(
    classLayout2Frontend::Views::SiteView,
    name=
        safe_text,
    templateColor=
        safe_text,
    templateName=
        safe_text,
    displayName=
        safe_text
)
Output_strategy = st.builds(
    Output,
)
classLayout2Frontend::Views::Image_strategy = st.builds(
    classLayout2Frontend::Views::Image,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
classLayout2Frontend::Views::TextArea_strategy = st.builds(
    classLayout2Frontend::Views::TextArea,
    value=
        safe_text
)
Input_strategy = st.builds(
    Input,
)
classLayout2Frontend::Views::Selection_strategy = st.builds(
    classLayout2Frontend::Views::Selection,
)
classLayout2Frontend::Views::FileUpload_strategy = st.builds(
    classLayout2Frontend::Views::FileUpload,
)
classLayout2Frontend::Views::InputText_strategy = st.builds(
    classLayout2Frontend::Views::InputText,
    multiline=
        st.booleans()
)
AtomicView_strategy = st.builds(
    AtomicView,
)
classLayout2Frontend::Views::Output_strategy = st.builds(
    classLayout2Frontend::Views::Output,
)
classLayout2Frontend::Views::Input_strategy = st.builds(
    classLayout2Frontend::Views::Input,
    label=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
classLayout2Frontend::Entities::Reference_strategy = st.builds(
    classLayout2Frontend::Entities::Reference,
)
classLayout2Frontend::Entities::Composition_strategy = st.builds(
    classLayout2Frontend::Entities::Composition,
)
Entity_strategy = st.builds(
    Entity,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
classLayout2Frontend::Entities::Association_strategy = st.builds(
    classLayout2Frontend::Entities::Association,
    many=
        st.booleans()
)
classLayout2Frontend::Entities::EntityModelElement_strategy = st.builds(
    classLayout2Frontend::Entities::EntityModelElement,
    description=
        safe_text,
    name=
        safe_text,
    displayName=
        safe_text
)
EntityModelElement_strategy = st.builds(
    EntityModelElement,
)
classLayout2Frontend::Entities::Entity_strategy = st.builds(
    classLayout2Frontend::Entities::Entity,
    isAbstract=
        st.booleans()
)
classLayout2Frontend::Entities::StructuralFeature_strategy = st.builds(
    classLayout2Frontend::Entities::StructuralFeature,
    required=
        st.booleans()
)
classLayout2Frontend::Entities::EntitiesModel_strategy = st.builds(
    classLayout2Frontend::Entities::EntitiesModel,
    name=
        safe_text
)
ContainerView_strategy = st.builds(
    ContainerView,
)
classLayout2Frontend::Views::StaticContainer_strategy = st.builds(
    classLayout2Frontend::Views::StaticContainer,
)
classLayout2Frontend::Views::InputForm_strategy = st.builds(
    classLayout2Frontend::Views::InputForm,
)
classLayout2Frontend::Views::IterationContainer_strategy = st.builds(
    classLayout2Frontend::Views::IterationContainer,
)
classLayout2Frontend::Entities::Literal_strategy = st.builds(
    classLayout2Frontend::Entities::Literal,
    value=
        st.integers()
)
classLayout2Frontend::Entities::PropertyType_strategy = st.builds(
    classLayout2Frontend::Entities::PropertyType,
)
Literal_strategy = st.builds(
    Literal,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
classLayout2Frontend::Entities::Enumeration_strategy = st.builds(
    classLayout2Frontend::Entities::Enumeration,
)
classLayout2Frontend::Entities::PrimitiveType_strategy = st.builds(
    classLayout2Frontend::Entities::PrimitiveType,
)
classLayout2Frontend::Entities::Property_strategy = st.builds(
    classLayout2Frontend::Entities::Property,
    defaultValue=
        safe_text
)
PageView_strategy = st.builds(
    PageView,
)
SiteView_strategy = st.builds(
    SiteView,
)
EntitiesModel_strategy = st.builds(
    EntitiesModel,
)
classLayout2Frontend::Project_strategy = st.builds(
    classLayout2Frontend::Project,
    name=
        safe_text
)

@given(instance=Selection_strategy)
@settings(max_examples=50)
def test_selection_instantiation(instance):
    assert isinstance(instance, Selection)

@given(instance=classLayout2Frontend::Views::Autocomplete_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::autocomplete_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::Autocomplete)

@given(instance=classLayout2Frontend::Views::Autocomplete_strategy)
def test_classlayout2frontend::views::autocomplete_multiple_type(instance):
    assert isinstance(instance.multiple, bool)


@given(instance=classLayout2Frontend::Views::Autocomplete_strategy)
def test_classlayout2frontend::views::autocomplete_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=classLayout2Frontend::Views::RadioButtonGroup_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::radiobuttongroup_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::RadioButtonGroup)

@given(instance=classLayout2Frontend::Views::List_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::list_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::List)

@given(instance=classLayout2Frontend::Views::List_strategy)
def test_classlayout2frontend::views::list_multiple_type(instance):
    assert isinstance(instance.multiple, bool)


@given(instance=classLayout2Frontend::Views::List_strategy)
def test_classlayout2frontend::views::list_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=classLayout2Frontend::Views::CheckList_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::checklist_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::CheckList)

@given(instance=classLayout2Frontend::Views::Dropdownlist_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::dropdownlist_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::Dropdownlist)

@given(instance=classLayout2Frontend::Views::IterationFilter_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::iterationfilter_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::IterationFilter)

@given(instance=classLayout2Frontend::Views::PageView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::pageview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::PageView)

@given(instance=classLayout2Frontend::Views::PageView_strategy)
def test_classlayout2frontend::views::pageview_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::Views::PageView_strategy)
def test_classlayout2frontend::views::pageview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classLayout2Frontend::Views::PageView_strategy)
def test_classlayout2frontend::views::pageview_layoutType_type(instance):
    assert isinstance(instance.layoutType, str)


@given(instance=classLayout2Frontend::Views::PageView_strategy)
def test_classlayout2frontend::views::pageview_layoutType_setter(instance):
    original = instance.layoutType
    instance.layoutType = original
    assert instance.layoutType == original

@given(instance=IterationFilter_strategy)
@settings(max_examples=50)
def test_iterationfilter_instantiation(instance):
    assert isinstance(instance, IterationFilter)

@given(instance=classLayout2Frontend::Views::ElementView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::elementview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::ElementView)

@given(instance=classLayout2Frontend::Views::ElementView_strategy)
def test_classlayout2frontend::views::elementview_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::Views::ElementView_strategy)
def test_classlayout2frontend::views::elementview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classLayout2Frontend::Views::ElementView_strategy)
def test_classlayout2frontend::views::elementview_dsisplayName_type(instance):
    assert isinstance(instance.dsisplayName, str)


@given(instance=classLayout2Frontend::Views::ElementView_strategy)
def test_classlayout2frontend::views::elementview_dsisplayName_setter(instance):
    original = instance.dsisplayName
    instance.dsisplayName = original
    assert instance.dsisplayName == original

@given(instance=classLayout2Frontend::Views::ElementView_strategy)
def test_classlayout2frontend::views::elementview_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=classLayout2Frontend::Views::ElementView_strategy)
def test_classlayout2frontend::views::elementview_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ElementView_strategy)
@settings(max_examples=50)
def test_elementview_instantiation(instance):
    assert isinstance(instance, ElementView)

@given(instance=classLayout2Frontend::Views::AtomicView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::atomicview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::AtomicView)

@given(instance=classLayout2Frontend::Views::ContainerView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::containerview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::ContainerView)

@given(instance=classLayout2Frontend::Views::SiteView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::siteview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::SiteView)

@given(instance=classLayout2Frontend::Views::SiteView_strategy)
def test_classlayout2frontend::views::siteview_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::Views::SiteView_strategy)
def test_classlayout2frontend::views::siteview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classLayout2Frontend::Views::SiteView_strategy)
def test_classlayout2frontend::views::siteview_templateColor_type(instance):
    assert isinstance(instance.templateColor, str)


@given(instance=classLayout2Frontend::Views::SiteView_strategy)
def test_classlayout2frontend::views::siteview_templateColor_setter(instance):
    original = instance.templateColor
    instance.templateColor = original
    assert instance.templateColor == original

@given(instance=classLayout2Frontend::Views::SiteView_strategy)
def test_classlayout2frontend::views::siteview_templateName_type(instance):
    assert isinstance(instance.templateName, str)


@given(instance=classLayout2Frontend::Views::SiteView_strategy)
def test_classlayout2frontend::views::siteview_templateName_setter(instance):
    original = instance.templateName
    instance.templateName = original
    assert instance.templateName == original

@given(instance=classLayout2Frontend::Views::SiteView_strategy)
def test_classlayout2frontend::views::siteview_displayName_type(instance):
    assert isinstance(instance.displayName, str)


@given(instance=classLayout2Frontend::Views::SiteView_strategy)
def test_classlayout2frontend::views::siteview_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original

@given(instance=Output_strategy)
@settings(max_examples=50)
def test_output_instantiation(instance):
    assert isinstance(instance, Output)

@given(instance=classLayout2Frontend::Views::Image_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::image_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::Image)

@given(instance=classLayout2Frontend::Views::Image_strategy)
def test_classlayout2frontend::views::image_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=classLayout2Frontend::Views::Image_strategy)
def test_classlayout2frontend::views::image_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=classLayout2Frontend::Views::Image_strategy)
def test_classlayout2frontend::views::image_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=classLayout2Frontend::Views::Image_strategy)
def test_classlayout2frontend::views::image_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=classLayout2Frontend::Views::TextArea_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::textarea_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::TextArea)

@given(instance=classLayout2Frontend::Views::TextArea_strategy)
def test_classlayout2frontend::views::textarea_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=classLayout2Frontend::Views::TextArea_strategy)
def test_classlayout2frontend::views::textarea_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Input_strategy)
@settings(max_examples=50)
def test_input_instantiation(instance):
    assert isinstance(instance, Input)

@given(instance=classLayout2Frontend::Views::Selection_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::selection_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::Selection)

@given(instance=classLayout2Frontend::Views::FileUpload_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::fileupload_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::FileUpload)

@given(instance=classLayout2Frontend::Views::InputText_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::inputtext_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::InputText)

@given(instance=classLayout2Frontend::Views::InputText_strategy)
def test_classlayout2frontend::views::inputtext_multiline_type(instance):
    assert isinstance(instance.multiline, bool)


@given(instance=classLayout2Frontend::Views::InputText_strategy)
def test_classlayout2frontend::views::inputtext_multiline_setter(instance):
    original = instance.multiline
    instance.multiline = original
    assert instance.multiline == original

@given(instance=AtomicView_strategy)
@settings(max_examples=50)
def test_atomicview_instantiation(instance):
    assert isinstance(instance, AtomicView)

@given(instance=classLayout2Frontend::Views::Output_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::output_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::Output)

@given(instance=classLayout2Frontend::Views::Input_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::input_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::Input)

@given(instance=classLayout2Frontend::Views::Input_strategy)
def test_classlayout2frontend::views::input_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=classLayout2Frontend::Views::Input_strategy)
def test_classlayout2frontend::views::input_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=classLayout2Frontend::Entities::Reference_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::reference_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::Reference)

@given(instance=classLayout2Frontend::Entities::Composition_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::composition_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::Composition)

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=classLayout2Frontend::Entities::Association_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::association_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::Association)

@given(instance=classLayout2Frontend::Entities::Association_strategy)
def test_classlayout2frontend::entities::association_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=classLayout2Frontend::Entities::Association_strategy)
def test_classlayout2frontend::entities::association_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=classLayout2Frontend::Entities::EntityModelElement_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::entitymodelelement_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::EntityModelElement)

@given(instance=classLayout2Frontend::Entities::EntityModelElement_strategy)
def test_classlayout2frontend::entities::entitymodelelement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=classLayout2Frontend::Entities::EntityModelElement_strategy)
def test_classlayout2frontend::entities::entitymodelelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=classLayout2Frontend::Entities::EntityModelElement_strategy)
def test_classlayout2frontend::entities::entitymodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::Entities::EntityModelElement_strategy)
def test_classlayout2frontend::entities::entitymodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classLayout2Frontend::Entities::EntityModelElement_strategy)
def test_classlayout2frontend::entities::entitymodelelement_displayName_type(instance):
    assert isinstance(instance.displayName, str)


@given(instance=classLayout2Frontend::Entities::EntityModelElement_strategy)
def test_classlayout2frontend::entities::entitymodelelement_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original

@given(instance=EntityModelElement_strategy)
@settings(max_examples=50)
def test_entitymodelelement_instantiation(instance):
    assert isinstance(instance, EntityModelElement)

@given(instance=classLayout2Frontend::Entities::Entity_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::entity_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::Entity)

@given(instance=classLayout2Frontend::Entities::Entity_strategy)
def test_classlayout2frontend::entities::entity_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=classLayout2Frontend::Entities::Entity_strategy)
def test_classlayout2frontend::entities::entity_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=classLayout2Frontend::Entities::StructuralFeature_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::structuralfeature_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::StructuralFeature)

@given(instance=classLayout2Frontend::Entities::StructuralFeature_strategy)
def test_classlayout2frontend::entities::structuralfeature_required_type(instance):
    assert isinstance(instance.required, bool)


@given(instance=classLayout2Frontend::Entities::StructuralFeature_strategy)
def test_classlayout2frontend::entities::structuralfeature_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=classLayout2Frontend::Entities::EntitiesModel_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::entitiesmodel_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::EntitiesModel)

@given(instance=classLayout2Frontend::Entities::EntitiesModel_strategy)
def test_classlayout2frontend::entities::entitiesmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::Entities::EntitiesModel_strategy)
def test_classlayout2frontend::entities::entitiesmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ContainerView_strategy)
@settings(max_examples=50)
def test_containerview_instantiation(instance):
    assert isinstance(instance, ContainerView)

@given(instance=classLayout2Frontend::Views::StaticContainer_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::staticcontainer_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::StaticContainer)

@given(instance=classLayout2Frontend::Views::InputForm_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::inputform_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::InputForm)

@given(instance=classLayout2Frontend::Views::IterationContainer_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::views::iterationcontainer_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Views::IterationContainer)

@given(instance=classLayout2Frontend::Entities::Literal_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::literal_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::Literal)

@given(instance=classLayout2Frontend::Entities::Literal_strategy)
def test_classlayout2frontend::entities::literal_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=classLayout2Frontend::Entities::Literal_strategy)
def test_classlayout2frontend::entities::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=classLayout2Frontend::Entities::PropertyType_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::propertytype_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::PropertyType)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=classLayout2Frontend::Entities::Enumeration_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::enumeration_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::Enumeration)

@given(instance=classLayout2Frontend::Entities::PrimitiveType_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::primitivetype_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::PrimitiveType)

@given(instance=classLayout2Frontend::Entities::Property_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entities::property_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entities::Property)

@given(instance=classLayout2Frontend::Entities::Property_strategy)
def test_classlayout2frontend::entities::property_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=classLayout2Frontend::Entities::Property_strategy)
def test_classlayout2frontend::entities::property_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=PageView_strategy)
@settings(max_examples=50)
def test_pageview_instantiation(instance):
    assert isinstance(instance, PageView)

@given(instance=SiteView_strategy)
@settings(max_examples=50)
def test_siteview_instantiation(instance):
    assert isinstance(instance, SiteView)

@given(instance=EntitiesModel_strategy)
@settings(max_examples=50)
def test_entitiesmodel_instantiation(instance):
    assert isinstance(instance, EntitiesModel)

@given(instance=classLayout2Frontend::Project_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::project_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Project)

@given(instance=classLayout2Frontend::Project_strategy)
def test_classlayout2frontend::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::Project_strategy)
def test_classlayout2frontend::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
