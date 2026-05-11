import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ContainerView,
    classLayout2Frontend::InputForm,
    classLayout2Frontend::IterationContainer,
    PropertyType,
    classLayout2Frontend::Enumeration,
    classLayout2Frontend::PrimitiveType,
    classLayout2Frontend::StaticContainer,
    classLayout2Frontend::ElementView,
    Input,
    classLayout2Frontend::Selection,
    classLayout2Frontend::FileUpload,
    classLayout2Frontend::InputText,
    classLayout2Frontend::IterationFilter,
    AtomicView,
    classLayout2Frontend::Input,
    classLayout2Frontend::Output,
    Output,
    classLayout2Frontend::TextArea,
    classLayout2Frontend::Image,
    Selection,
    classLayout2Frontend::CheckList,
    classLayout2Frontend::List,
    classLayout2Frontend::Dropdownlist,
    classLayout2Frontend::RadioButtonGroup,
    classLayout2Frontend::Autocomplete,
    ElementView,
    classLayout2Frontend::AtomicView,
    classLayout2Frontend::SiteView,
    classLayout2Frontend::EntitiesModel,
    classLayout2Frontend::Project,
    classLayout2Frontend::EntityModelElement,
    EntityModelElement,
    classLayout2Frontend::Literal,
    classLayout2Frontend::StructuralFeature,
    classLayout2Frontend::PropertyType,
    classLayout2Frontend::Entity,
    StructuralFeature,
    classLayout2Frontend::Property,
    classLayout2Frontend::Association,
    Association,
    classLayout2Frontend::Reference,
    classLayout2Frontend::Composition,
    classLayout2Frontend::ContainerView,
    classLayout2Frontend::PageView,
    LayoutType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_containerview_is_not_abstract():
    assert not inspect.isabstract(ContainerView)


def test_containerview_constructor_exists():
    assert callable(ContainerView.__init__)


def test_containerview_constructor_args():
    sig = inspect.signature(ContainerView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::inputform_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::InputForm)


def test_classlayout2frontend::inputform_constructor_exists():
    assert callable(classLayout2Frontend::InputForm.__init__)


def test_classlayout2frontend::inputform_constructor_args():
    sig = inspect.signature(classLayout2Frontend::InputForm.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::iterationcontainer_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::IterationContainer)


def test_classlayout2frontend::iterationcontainer_constructor_exists():
    assert callable(classLayout2Frontend::IterationContainer.__init__)


def test_classlayout2frontend::iterationcontainer_constructor_args():
    sig = inspect.signature(classLayout2Frontend::IterationContainer.__init__)
    params = list(sig.parameters.keys())



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::enumeration_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Enumeration)


def test_classlayout2frontend::enumeration_constructor_exists():
    assert callable(classLayout2Frontend::Enumeration.__init__)


def test_classlayout2frontend::enumeration_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::primitivetype_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::PrimitiveType)


def test_classlayout2frontend::primitivetype_constructor_exists():
    assert callable(classLayout2Frontend::PrimitiveType.__init__)


def test_classlayout2frontend::primitivetype_constructor_args():
    sig = inspect.signature(classLayout2Frontend::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::staticcontainer_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::StaticContainer)


def test_classlayout2frontend::staticcontainer_constructor_exists():
    assert callable(classLayout2Frontend::StaticContainer.__init__)


def test_classlayout2frontend::staticcontainer_constructor_args():
    sig = inspect.signature(classLayout2Frontend::StaticContainer.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::elementview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::ElementView)


def test_classlayout2frontend::elementview_constructor_exists():
    assert callable(classLayout2Frontend::ElementView.__init__)


def test_classlayout2frontend::elementview_constructor_args():
    sig = inspect.signature(classLayout2Frontend::ElementView.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "displayName" in params, "Missing parameter 'displayName'"

def test_classlayout2frontend::elementview_has_name():
    assert hasattr(classLayout2Frontend::ElementView, "name")
    descriptor = None
    for klass in classLayout2Frontend::ElementView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::elementview_has_description():
    assert hasattr(classLayout2Frontend::ElementView, "description")
    descriptor = None
    for klass in classLayout2Frontend::ElementView.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::elementview_has_displayName():
    assert hasattr(classLayout2Frontend::ElementView, "displayName")
    descriptor = None
    for klass in classLayout2Frontend::ElementView.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)



def test_input_is_not_abstract():
    assert not inspect.isabstract(Input)


def test_input_constructor_exists():
    assert callable(Input.__init__)


def test_input_constructor_args():
    sig = inspect.signature(Input.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::selection_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Selection)


def test_classlayout2frontend::selection_constructor_exists():
    assert callable(classLayout2Frontend::Selection.__init__)


def test_classlayout2frontend::selection_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Selection.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::fileupload_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::FileUpload)


def test_classlayout2frontend::fileupload_constructor_exists():
    assert callable(classLayout2Frontend::FileUpload.__init__)


def test_classlayout2frontend::fileupload_constructor_args():
    sig = inspect.signature(classLayout2Frontend::FileUpload.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::inputtext_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::InputText)


def test_classlayout2frontend::inputtext_constructor_exists():
    assert callable(classLayout2Frontend::InputText.__init__)


def test_classlayout2frontend::inputtext_constructor_args():
    sig = inspect.signature(classLayout2Frontend::InputText.__init__)
    params = list(sig.parameters.keys())
    assert "multiline" in params, "Missing parameter 'multiline'"

def test_classlayout2frontend::inputtext_has_multiline():
    assert hasattr(classLayout2Frontend::InputText, "multiline")
    descriptor = None
    for klass in classLayout2Frontend::InputText.__mro__:
        if "multiline" in klass.__dict__:
            descriptor = klass.__dict__["multiline"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::iterationfilter_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::IterationFilter)


def test_classlayout2frontend::iterationfilter_constructor_exists():
    assert callable(classLayout2Frontend::IterationFilter.__init__)


def test_classlayout2frontend::iterationfilter_constructor_args():
    sig = inspect.signature(classLayout2Frontend::IterationFilter.__init__)
    params = list(sig.parameters.keys())



def test_atomicview_is_not_abstract():
    assert not inspect.isabstract(AtomicView)


def test_atomicview_constructor_exists():
    assert callable(AtomicView.__init__)


def test_atomicview_constructor_args():
    sig = inspect.signature(AtomicView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::input_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Input)


def test_classlayout2frontend::input_constructor_exists():
    assert callable(classLayout2Frontend::Input.__init__)


def test_classlayout2frontend::input_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Input.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_classlayout2frontend::input_has_label():
    assert hasattr(classLayout2Frontend::Input, "label")
    descriptor = None
    for klass in classLayout2Frontend::Input.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::output_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Output)


def test_classlayout2frontend::output_constructor_exists():
    assert callable(classLayout2Frontend::Output.__init__)


def test_classlayout2frontend::output_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Output.__init__)
    params = list(sig.parameters.keys())



def test_output_is_not_abstract():
    assert not inspect.isabstract(Output)


def test_output_constructor_exists():
    assert callable(Output.__init__)


def test_output_constructor_args():
    sig = inspect.signature(Output.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::textarea_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::TextArea)


def test_classlayout2frontend::textarea_constructor_exists():
    assert callable(classLayout2Frontend::TextArea.__init__)


def test_classlayout2frontend::textarea_constructor_args():
    sig = inspect.signature(classLayout2Frontend::TextArea.__init__)
    params = list(sig.parameters.keys())
    assert "isTitle" in params, "Missing parameter 'isTitle'"
    assert "value" in params, "Missing parameter 'value'"

def test_classlayout2frontend::textarea_has_isTitle():
    assert hasattr(classLayout2Frontend::TextArea, "isTitle")
    descriptor = None
    for klass in classLayout2Frontend::TextArea.__mro__:
        if "isTitle" in klass.__dict__:
            descriptor = klass.__dict__["isTitle"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::textarea_has_value():
    assert hasattr(classLayout2Frontend::TextArea, "value")
    descriptor = None
    for klass in classLayout2Frontend::TextArea.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::image_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Image)


def test_classlayout2frontend::image_constructor_exists():
    assert callable(classLayout2Frontend::Image.__init__)


def test_classlayout2frontend::image_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Image.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_classlayout2frontend::image_has_height():
    assert hasattr(classLayout2Frontend::Image, "height")
    descriptor = None
    for klass in classLayout2Frontend::Image.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::image_has_width():
    assert hasattr(classLayout2Frontend::Image, "width")
    descriptor = None
    for klass in classLayout2Frontend::Image.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_selection_is_not_abstract():
    assert not inspect.isabstract(Selection)


def test_selection_constructor_exists():
    assert callable(Selection.__init__)


def test_selection_constructor_args():
    sig = inspect.signature(Selection.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::checklist_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::CheckList)


def test_classlayout2frontend::checklist_constructor_exists():
    assert callable(classLayout2Frontend::CheckList.__init__)


def test_classlayout2frontend::checklist_constructor_args():
    sig = inspect.signature(classLayout2Frontend::CheckList.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::list_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::List)


def test_classlayout2frontend::list_constructor_exists():
    assert callable(classLayout2Frontend::List.__init__)


def test_classlayout2frontend::list_constructor_args():
    sig = inspect.signature(classLayout2Frontend::List.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_classlayout2frontend::list_has_multiple():
    assert hasattr(classLayout2Frontend::List, "multiple")
    descriptor = None
    for klass in classLayout2Frontend::List.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::dropdownlist_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Dropdownlist)


def test_classlayout2frontend::dropdownlist_constructor_exists():
    assert callable(classLayout2Frontend::Dropdownlist.__init__)


def test_classlayout2frontend::dropdownlist_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Dropdownlist.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::radiobuttongroup_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::RadioButtonGroup)


def test_classlayout2frontend::radiobuttongroup_constructor_exists():
    assert callable(classLayout2Frontend::RadioButtonGroup.__init__)


def test_classlayout2frontend::radiobuttongroup_constructor_args():
    sig = inspect.signature(classLayout2Frontend::RadioButtonGroup.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::autocomplete_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Autocomplete)


def test_classlayout2frontend::autocomplete_constructor_exists():
    assert callable(classLayout2Frontend::Autocomplete.__init__)


def test_classlayout2frontend::autocomplete_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Autocomplete.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_classlayout2frontend::autocomplete_has_multiple():
    assert hasattr(classLayout2Frontend::Autocomplete, "multiple")
    descriptor = None
    for klass in classLayout2Frontend::Autocomplete.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_elementview_is_not_abstract():
    assert not inspect.isabstract(ElementView)


def test_elementview_constructor_exists():
    assert callable(ElementView.__init__)


def test_elementview_constructor_args():
    sig = inspect.signature(ElementView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::atomicview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::AtomicView)


def test_classlayout2frontend::atomicview_constructor_exists():
    assert callable(classLayout2Frontend::AtomicView.__init__)


def test_classlayout2frontend::atomicview_constructor_args():
    sig = inspect.signature(classLayout2Frontend::AtomicView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::siteview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::SiteView)


def test_classlayout2frontend::siteview_constructor_exists():
    assert callable(classLayout2Frontend::SiteView.__init__)


def test_classlayout2frontend::siteview_constructor_args():
    sig = inspect.signature(classLayout2Frontend::SiteView.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "templateColor" in params, "Missing parameter 'templateColor'"
    assert "templateName" in params, "Missing parameter 'templateName'"

def test_classlayout2frontend::siteview_has_name():
    assert hasattr(classLayout2Frontend::SiteView, "name")
    descriptor = None
    for klass in classLayout2Frontend::SiteView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::siteview_has_displayName():
    assert hasattr(classLayout2Frontend::SiteView, "displayName")
    descriptor = None
    for klass in classLayout2Frontend::SiteView.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::siteview_has_templateColor():
    assert hasattr(classLayout2Frontend::SiteView, "templateColor")
    descriptor = None
    for klass in classLayout2Frontend::SiteView.__mro__:
        if "templateColor" in klass.__dict__:
            descriptor = klass.__dict__["templateColor"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::siteview_has_templateName():
    assert hasattr(classLayout2Frontend::SiteView, "templateName")
    descriptor = None
    for klass in classLayout2Frontend::SiteView.__mro__:
        if "templateName" in klass.__dict__:
            descriptor = klass.__dict__["templateName"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::entitiesmodel_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::EntitiesModel)


def test_classlayout2frontend::entitiesmodel_constructor_exists():
    assert callable(classLayout2Frontend::EntitiesModel.__init__)


def test_classlayout2frontend::entitiesmodel_constructor_args():
    sig = inspect.signature(classLayout2Frontend::EntitiesModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend::entitiesmodel_has_name():
    assert hasattr(classLayout2Frontend::EntitiesModel, "name")
    descriptor = None
    for klass in classLayout2Frontend::EntitiesModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_classlayout2frontend::entitymodelelement_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::EntityModelElement)


def test_classlayout2frontend::entitymodelelement_constructor_exists():
    assert callable(classLayout2Frontend::EntityModelElement.__init__)


def test_classlayout2frontend::entitymodelelement_constructor_args():
    sig = inspect.signature(classLayout2Frontend::EntityModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_classlayout2frontend::entitymodelelement_has_displayName():
    assert hasattr(classLayout2Frontend::EntityModelElement, "displayName")
    descriptor = None
    for klass in classLayout2Frontend::EntityModelElement.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::entitymodelelement_has_name():
    assert hasattr(classLayout2Frontend::EntityModelElement, "name")
    descriptor = None
    for klass in classLayout2Frontend::EntityModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::entitymodelelement_has_description():
    assert hasattr(classLayout2Frontend::EntityModelElement, "description")
    descriptor = None
    for klass in classLayout2Frontend::EntityModelElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_entitymodelelement_is_not_abstract():
    assert not inspect.isabstract(EntityModelElement)


def test_entitymodelelement_constructor_exists():
    assert callable(EntityModelElement.__init__)


def test_entitymodelelement_constructor_args():
    sig = inspect.signature(EntityModelElement.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::literal_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Literal)


def test_classlayout2frontend::literal_constructor_exists():
    assert callable(classLayout2Frontend::Literal.__init__)


def test_classlayout2frontend::literal_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_classlayout2frontend::literal_has_value():
    assert hasattr(classLayout2Frontend::Literal, "value")
    descriptor = None
    for klass in classLayout2Frontend::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::StructuralFeature)


def test_classlayout2frontend::structuralfeature_constructor_exists():
    assert callable(classLayout2Frontend::StructuralFeature.__init__)


def test_classlayout2frontend::structuralfeature_constructor_args():
    sig = inspect.signature(classLayout2Frontend::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"

def test_classlayout2frontend::structuralfeature_has_required():
    assert hasattr(classLayout2Frontend::StructuralFeature, "required")
    descriptor = None
    for klass in classLayout2Frontend::StructuralFeature.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::propertytype_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::PropertyType)


def test_classlayout2frontend::propertytype_constructor_exists():
    assert callable(classLayout2Frontend::PropertyType.__init__)


def test_classlayout2frontend::propertytype_constructor_args():
    sig = inspect.signature(classLayout2Frontend::PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::entity_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Entity)


def test_classlayout2frontend::entity_constructor_exists():
    assert callable(classLayout2Frontend::Entity.__init__)


def test_classlayout2frontend::entity_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_classlayout2frontend::entity_has_isAbstract():
    assert hasattr(classLayout2Frontend::Entity, "isAbstract")
    descriptor = None
    for klass in classLayout2Frontend::Entity.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::property_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Property)


def test_classlayout2frontend::property_constructor_exists():
    assert callable(classLayout2Frontend::Property.__init__)


def test_classlayout2frontend::property_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Property.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_classlayout2frontend::property_has_defaultValue():
    assert hasattr(classLayout2Frontend::Property, "defaultValue")
    descriptor = None
    for klass in classLayout2Frontend::Property.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend::association_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Association)


def test_classlayout2frontend::association_constructor_exists():
    assert callable(classLayout2Frontend::Association.__init__)


def test_classlayout2frontend::association_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Association.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_classlayout2frontend::association_has_many():
    assert hasattr(classLayout2Frontend::Association, "many")
    descriptor = None
    for klass in classLayout2Frontend::Association.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::reference_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Reference)


def test_classlayout2frontend::reference_constructor_exists():
    assert callable(classLayout2Frontend::Reference.__init__)


def test_classlayout2frontend::reference_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Reference.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::composition_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::Composition)


def test_classlayout2frontend::composition_constructor_exists():
    assert callable(classLayout2Frontend::Composition.__init__)


def test_classlayout2frontend::composition_constructor_args():
    sig = inspect.signature(classLayout2Frontend::Composition.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::containerview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::ContainerView)


def test_classlayout2frontend::containerview_constructor_exists():
    assert callable(classLayout2Frontend::ContainerView.__init__)


def test_classlayout2frontend::containerview_constructor_args():
    sig = inspect.signature(classLayout2Frontend::ContainerView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend::pageview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend::PageView)


def test_classlayout2frontend::pageview_constructor_exists():
    assert callable(classLayout2Frontend::PageView.__init__)


def test_classlayout2frontend::pageview_constructor_args():
    sig = inspect.signature(classLayout2Frontend::PageView.__init__)
    params = list(sig.parameters.keys())
    assert "layoutType" in params, "Missing parameter 'layoutType'"
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend::pageview_has_layoutType():
    assert hasattr(classLayout2Frontend::PageView, "layoutType")
    descriptor = None
    for klass in classLayout2Frontend::PageView.__mro__:
        if "layoutType" in klass.__dict__:
            descriptor = klass.__dict__["layoutType"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend::pageview_has_name():
    assert hasattr(classLayout2Frontend::PageView, "name")
    descriptor = None
    for klass in classLayout2Frontend::PageView.__mro__:
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
        "SINGLE_COLUMN",
        "THREE_COLUMNS",
        "LEFT_BAR",
        "RIGHT_BAR",
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
ContainerView_strategy = st.builds(
    ContainerView,
)
classLayout2Frontend::InputForm_strategy = st.builds(
    classLayout2Frontend::InputForm,
)
classLayout2Frontend::IterationContainer_strategy = st.builds(
    classLayout2Frontend::IterationContainer,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
classLayout2Frontend::Enumeration_strategy = st.builds(
    classLayout2Frontend::Enumeration,
)
classLayout2Frontend::PrimitiveType_strategy = st.builds(
    classLayout2Frontend::PrimitiveType,
)
classLayout2Frontend::StaticContainer_strategy = st.builds(
    classLayout2Frontend::StaticContainer,
)
classLayout2Frontend::ElementView_strategy = st.builds(
    classLayout2Frontend::ElementView,
    name=
        safe_text,
    description=
        safe_text,
    displayName=
        safe_text
)
Input_strategy = st.builds(
    Input,
)
classLayout2Frontend::Selection_strategy = st.builds(
    classLayout2Frontend::Selection,
)
classLayout2Frontend::FileUpload_strategy = st.builds(
    classLayout2Frontend::FileUpload,
)
classLayout2Frontend::InputText_strategy = st.builds(
    classLayout2Frontend::InputText,
    multiline=
        st.booleans()
)
classLayout2Frontend::IterationFilter_strategy = st.builds(
    classLayout2Frontend::IterationFilter,
)
AtomicView_strategy = st.builds(
    AtomicView,
)
classLayout2Frontend::Input_strategy = st.builds(
    classLayout2Frontend::Input,
    label=
        safe_text
)
classLayout2Frontend::Output_strategy = st.builds(
    classLayout2Frontend::Output,
)
Output_strategy = st.builds(
    Output,
)
classLayout2Frontend::TextArea_strategy = st.builds(
    classLayout2Frontend::TextArea,
    isTitle=
        st.booleans(),
    value=
        safe_text
)
classLayout2Frontend::Image_strategy = st.builds(
    classLayout2Frontend::Image,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Selection_strategy = st.builds(
    Selection,
)
classLayout2Frontend::CheckList_strategy = st.builds(
    classLayout2Frontend::CheckList,
)
classLayout2Frontend::List_strategy = st.builds(
    classLayout2Frontend::List,
    multiple=
        st.booleans()
)
classLayout2Frontend::Dropdownlist_strategy = st.builds(
    classLayout2Frontend::Dropdownlist,
)
classLayout2Frontend::RadioButtonGroup_strategy = st.builds(
    classLayout2Frontend::RadioButtonGroup,
)
classLayout2Frontend::Autocomplete_strategy = st.builds(
    classLayout2Frontend::Autocomplete,
    multiple=
        st.booleans()
)
ElementView_strategy = st.builds(
    ElementView,
)
classLayout2Frontend::AtomicView_strategy = st.builds(
    classLayout2Frontend::AtomicView,
)
classLayout2Frontend::SiteView_strategy = st.builds(
    classLayout2Frontend::SiteView,
    name=
        safe_text,
    displayName=
        safe_text,
    templateColor=
        safe_text,
    templateName=
        safe_text
)
classLayout2Frontend::EntitiesModel_strategy = st.builds(
    classLayout2Frontend::EntitiesModel,
    name=
        safe_text
)
classLayout2Frontend::Project_strategy = st.builds(
    classLayout2Frontend::Project,
    name=
        safe_text
)
classLayout2Frontend::EntityModelElement_strategy = st.builds(
    classLayout2Frontend::EntityModelElement,
    displayName=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
EntityModelElement_strategy = st.builds(
    EntityModelElement,
)
classLayout2Frontend::Literal_strategy = st.builds(
    classLayout2Frontend::Literal,
    value=
        st.integers()
)
classLayout2Frontend::StructuralFeature_strategy = st.builds(
    classLayout2Frontend::StructuralFeature,
    required=
        st.booleans()
)
classLayout2Frontend::PropertyType_strategy = st.builds(
    classLayout2Frontend::PropertyType,
)
classLayout2Frontend::Entity_strategy = st.builds(
    classLayout2Frontend::Entity,
    isAbstract=
        st.booleans()
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
classLayout2Frontend::Property_strategy = st.builds(
    classLayout2Frontend::Property,
    defaultValue=
        safe_text
)
classLayout2Frontend::Association_strategy = st.builds(
    classLayout2Frontend::Association,
    many=
        st.booleans()
)
Association_strategy = st.builds(
    Association,
)
classLayout2Frontend::Reference_strategy = st.builds(
    classLayout2Frontend::Reference,
)
classLayout2Frontend::Composition_strategy = st.builds(
    classLayout2Frontend::Composition,
)
classLayout2Frontend::ContainerView_strategy = st.builds(
    classLayout2Frontend::ContainerView,
)
classLayout2Frontend::PageView_strategy = st.builds(
    classLayout2Frontend::PageView,
    layoutType=
        safe_text,
    name=
        safe_text
)

@given(instance=ContainerView_strategy)
@settings(max_examples=50)
def test_containerview_instantiation(instance):
    assert isinstance(instance, ContainerView)

@given(instance=classLayout2Frontend::InputForm_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::inputform_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::InputForm)

@given(instance=classLayout2Frontend::IterationContainer_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::iterationcontainer_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::IterationContainer)

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=classLayout2Frontend::Enumeration_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::enumeration_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Enumeration)

@given(instance=classLayout2Frontend::PrimitiveType_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::primitivetype_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::PrimitiveType)

@given(instance=classLayout2Frontend::StaticContainer_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::staticcontainer_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::StaticContainer)

@given(instance=classLayout2Frontend::ElementView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::elementview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::ElementView)

@given(instance=classLayout2Frontend::ElementView_strategy)
def test_classlayout2frontend::elementview_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::ElementView_strategy)
def test_classlayout2frontend::elementview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classLayout2Frontend::ElementView_strategy)
def test_classlayout2frontend::elementview_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=classLayout2Frontend::ElementView_strategy)
def test_classlayout2frontend::elementview_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=classLayout2Frontend::ElementView_strategy)
def test_classlayout2frontend::elementview_displayName_type(instance):
    assert isinstance(instance.displayName, str)


@given(instance=classLayout2Frontend::ElementView_strategy)
def test_classlayout2frontend::elementview_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original

@given(instance=Input_strategy)
@settings(max_examples=50)
def test_input_instantiation(instance):
    assert isinstance(instance, Input)

@given(instance=classLayout2Frontend::Selection_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::selection_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Selection)

@given(instance=classLayout2Frontend::FileUpload_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::fileupload_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::FileUpload)

@given(instance=classLayout2Frontend::InputText_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::inputtext_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::InputText)

@given(instance=classLayout2Frontend::InputText_strategy)
def test_classlayout2frontend::inputtext_multiline_type(instance):
    assert isinstance(instance.multiline, bool)


@given(instance=classLayout2Frontend::InputText_strategy)
def test_classlayout2frontend::inputtext_multiline_setter(instance):
    original = instance.multiline
    instance.multiline = original
    assert instance.multiline == original

@given(instance=classLayout2Frontend::IterationFilter_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::iterationfilter_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::IterationFilter)

@given(instance=AtomicView_strategy)
@settings(max_examples=50)
def test_atomicview_instantiation(instance):
    assert isinstance(instance, AtomicView)

@given(instance=classLayout2Frontend::Input_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::input_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Input)

@given(instance=classLayout2Frontend::Input_strategy)
def test_classlayout2frontend::input_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=classLayout2Frontend::Input_strategy)
def test_classlayout2frontend::input_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=classLayout2Frontend::Output_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::output_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Output)

@given(instance=Output_strategy)
@settings(max_examples=50)
def test_output_instantiation(instance):
    assert isinstance(instance, Output)

@given(instance=classLayout2Frontend::TextArea_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::textarea_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::TextArea)

@given(instance=classLayout2Frontend::TextArea_strategy)
def test_classlayout2frontend::textarea_isTitle_type(instance):
    assert isinstance(instance.isTitle, bool)


@given(instance=classLayout2Frontend::TextArea_strategy)
def test_classlayout2frontend::textarea_isTitle_setter(instance):
    original = instance.isTitle
    instance.isTitle = original
    assert instance.isTitle == original

@given(instance=classLayout2Frontend::TextArea_strategy)
def test_classlayout2frontend::textarea_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=classLayout2Frontend::TextArea_strategy)
def test_classlayout2frontend::textarea_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=classLayout2Frontend::Image_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::image_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Image)

@given(instance=classLayout2Frontend::Image_strategy)
def test_classlayout2frontend::image_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=classLayout2Frontend::Image_strategy)
def test_classlayout2frontend::image_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=classLayout2Frontend::Image_strategy)
def test_classlayout2frontend::image_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=classLayout2Frontend::Image_strategy)
def test_classlayout2frontend::image_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=Selection_strategy)
@settings(max_examples=50)
def test_selection_instantiation(instance):
    assert isinstance(instance, Selection)

@given(instance=classLayout2Frontend::CheckList_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::checklist_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::CheckList)

@given(instance=classLayout2Frontend::List_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::list_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::List)

@given(instance=classLayout2Frontend::List_strategy)
def test_classlayout2frontend::list_multiple_type(instance):
    assert isinstance(instance.multiple, bool)


@given(instance=classLayout2Frontend::List_strategy)
def test_classlayout2frontend::list_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=classLayout2Frontend::Dropdownlist_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::dropdownlist_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Dropdownlist)

@given(instance=classLayout2Frontend::RadioButtonGroup_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::radiobuttongroup_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::RadioButtonGroup)

@given(instance=classLayout2Frontend::Autocomplete_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::autocomplete_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Autocomplete)

@given(instance=classLayout2Frontend::Autocomplete_strategy)
def test_classlayout2frontend::autocomplete_multiple_type(instance):
    assert isinstance(instance.multiple, bool)


@given(instance=classLayout2Frontend::Autocomplete_strategy)
def test_classlayout2frontend::autocomplete_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=ElementView_strategy)
@settings(max_examples=50)
def test_elementview_instantiation(instance):
    assert isinstance(instance, ElementView)

@given(instance=classLayout2Frontend::AtomicView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::atomicview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::AtomicView)

@given(instance=classLayout2Frontend::SiteView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::siteview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::SiteView)

@given(instance=classLayout2Frontend::SiteView_strategy)
def test_classlayout2frontend::siteview_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::SiteView_strategy)
def test_classlayout2frontend::siteview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classLayout2Frontend::SiteView_strategy)
def test_classlayout2frontend::siteview_displayName_type(instance):
    assert isinstance(instance.displayName, str)


@given(instance=classLayout2Frontend::SiteView_strategy)
def test_classlayout2frontend::siteview_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original

@given(instance=classLayout2Frontend::SiteView_strategy)
def test_classlayout2frontend::siteview_templateColor_type(instance):
    assert isinstance(instance.templateColor, str)


@given(instance=classLayout2Frontend::SiteView_strategy)
def test_classlayout2frontend::siteview_templateColor_setter(instance):
    original = instance.templateColor
    instance.templateColor = original
    assert instance.templateColor == original

@given(instance=classLayout2Frontend::SiteView_strategy)
def test_classlayout2frontend::siteview_templateName_type(instance):
    assert isinstance(instance.templateName, str)


@given(instance=classLayout2Frontend::SiteView_strategy)
def test_classlayout2frontend::siteview_templateName_setter(instance):
    original = instance.templateName
    instance.templateName = original
    assert instance.templateName == original

@given(instance=classLayout2Frontend::EntitiesModel_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entitiesmodel_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::EntitiesModel)

@given(instance=classLayout2Frontend::EntitiesModel_strategy)
def test_classlayout2frontend::entitiesmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::EntitiesModel_strategy)
def test_classlayout2frontend::entitiesmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=classLayout2Frontend::EntityModelElement_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entitymodelelement_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::EntityModelElement)

@given(instance=classLayout2Frontend::EntityModelElement_strategy)
def test_classlayout2frontend::entitymodelelement_displayName_type(instance):
    assert isinstance(instance.displayName, str)


@given(instance=classLayout2Frontend::EntityModelElement_strategy)
def test_classlayout2frontend::entitymodelelement_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original

@given(instance=classLayout2Frontend::EntityModelElement_strategy)
def test_classlayout2frontend::entitymodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::EntityModelElement_strategy)
def test_classlayout2frontend::entitymodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classLayout2Frontend::EntityModelElement_strategy)
def test_classlayout2frontend::entitymodelelement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=classLayout2Frontend::EntityModelElement_strategy)
def test_classlayout2frontend::entitymodelelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=EntityModelElement_strategy)
@settings(max_examples=50)
def test_entitymodelelement_instantiation(instance):
    assert isinstance(instance, EntityModelElement)

@given(instance=classLayout2Frontend::Literal_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::literal_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Literal)

@given(instance=classLayout2Frontend::Literal_strategy)
def test_classlayout2frontend::literal_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=classLayout2Frontend::Literal_strategy)
def test_classlayout2frontend::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=classLayout2Frontend::StructuralFeature_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::structuralfeature_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::StructuralFeature)

@given(instance=classLayout2Frontend::StructuralFeature_strategy)
def test_classlayout2frontend::structuralfeature_required_type(instance):
    assert isinstance(instance.required, bool)


@given(instance=classLayout2Frontend::StructuralFeature_strategy)
def test_classlayout2frontend::structuralfeature_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=classLayout2Frontend::PropertyType_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::propertytype_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::PropertyType)

@given(instance=classLayout2Frontend::Entity_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::entity_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Entity)

@given(instance=classLayout2Frontend::Entity_strategy)
def test_classlayout2frontend::entity_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=classLayout2Frontend::Entity_strategy)
def test_classlayout2frontend::entity_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=classLayout2Frontend::Property_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::property_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Property)

@given(instance=classLayout2Frontend::Property_strategy)
def test_classlayout2frontend::property_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=classLayout2Frontend::Property_strategy)
def test_classlayout2frontend::property_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=classLayout2Frontend::Association_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::association_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Association)

@given(instance=classLayout2Frontend::Association_strategy)
def test_classlayout2frontend::association_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=classLayout2Frontend::Association_strategy)
def test_classlayout2frontend::association_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=classLayout2Frontend::Reference_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::reference_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Reference)

@given(instance=classLayout2Frontend::Composition_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::composition_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::Composition)

@given(instance=classLayout2Frontend::ContainerView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::containerview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::ContainerView)

@given(instance=classLayout2Frontend::PageView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend::pageview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend::PageView)

@given(instance=classLayout2Frontend::PageView_strategy)
def test_classlayout2frontend::pageview_layoutType_type(instance):
    assert isinstance(instance.layoutType, str)


@given(instance=classLayout2Frontend::PageView_strategy)
def test_classlayout2frontend::pageview_layoutType_setter(instance):
    original = instance.layoutType
    instance.layoutType = original
    assert instance.layoutType == original

@given(instance=classLayout2Frontend::PageView_strategy)
def test_classlayout2frontend::pageview_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classLayout2Frontend::PageView_strategy)
def test_classlayout2frontend::pageview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
