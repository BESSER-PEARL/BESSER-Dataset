import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Selection,
    classLayout2Frontend_Views_CheckList,
    classLayout2Frontend_Views_List,
    classLayout2Frontend_Views_RadioButtonGroup,
    classLayout2Frontend_Views_Autocomplete,
    classLayout2Frontend_Views_Dropdownlist,
    classLayout2Frontend_Views_IterationFilter,
    classLayout2Frontend_Views_PageView,
    IterationFilter,
    classLayout2Frontend_Views_ElementView,
    ElementView,
    classLayout2Frontend_Views_AtomicView,
    classLayout2Frontend_Views_ContainerView,
    classLayout2Frontend_Views_SiteView,
    Output,
    classLayout2Frontend_Views_Image,
    classLayout2Frontend_Views_TextArea,
    Input,
    classLayout2Frontend_Views_Selection,
    classLayout2Frontend_Views_FileUpload,
    classLayout2Frontend_Views_InputText,
    AtomicView,
    classLayout2Frontend_Views_Output,
    classLayout2Frontend_Views_Input,
    Association,
    classLayout2Frontend_Entities_Reference,
    classLayout2Frontend_Entities_Composition,
    Entity,
    StructuralFeature,
    classLayout2Frontend_Entities_Association,
    classLayout2Frontend_Entities_EntityModelElement,
    EntityModelElement,
    classLayout2Frontend_Entities_Entity,
    classLayout2Frontend_Entities_StructuralFeature,
    classLayout2Frontend_Entities_EntitiesModel,
    ContainerView,
    classLayout2Frontend_Views_StaticContainer,
    classLayout2Frontend_Views_IterationContainer,
    classLayout2Frontend_Views_InputForm,
    classLayout2Frontend_Entities_Literal,
    classLayout2Frontend_Entities_PropertyType,
    Literal,
    PropertyType,
    classLayout2Frontend_Entities_Enumeration,
    classLayout2Frontend_Entities_PrimitiveType,
    classLayout2Frontend_Entities_Property,
    PageView,
    SiteView,
    EntitiesModel,
    classLayout2Frontend_Project,
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



def test_classlayout2frontend_views_checklist_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_CheckList)


def test_classlayout2frontend_views_checklist_constructor_exists():
    assert callable(classLayout2Frontend_Views_CheckList.__init__)


def test_classlayout2frontend_views_checklist_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_CheckList.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_list_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_List)


def test_classlayout2frontend_views_list_constructor_exists():
    assert callable(classLayout2Frontend_Views_List.__init__)


def test_classlayout2frontend_views_list_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_List.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_classlayout2frontend_views_list_has_multiple():
    assert hasattr(classLayout2Frontend_Views_List, "multiple")
    descriptor = None
    for klass in classLayout2Frontend_Views_List.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_views_radiobuttongroup_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_RadioButtonGroup)


def test_classlayout2frontend_views_radiobuttongroup_constructor_exists():
    assert callable(classLayout2Frontend_Views_RadioButtonGroup.__init__)


def test_classlayout2frontend_views_radiobuttongroup_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_RadioButtonGroup.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_autocomplete_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_Autocomplete)


def test_classlayout2frontend_views_autocomplete_constructor_exists():
    assert callable(classLayout2Frontend_Views_Autocomplete.__init__)


def test_classlayout2frontend_views_autocomplete_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_Autocomplete.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_classlayout2frontend_views_autocomplete_has_multiple():
    assert hasattr(classLayout2Frontend_Views_Autocomplete, "multiple")
    descriptor = None
    for klass in classLayout2Frontend_Views_Autocomplete.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_views_dropdownlist_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_Dropdownlist)


def test_classlayout2frontend_views_dropdownlist_constructor_exists():
    assert callable(classLayout2Frontend_Views_Dropdownlist.__init__)


def test_classlayout2frontend_views_dropdownlist_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_Dropdownlist.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_iterationfilter_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_IterationFilter)


def test_classlayout2frontend_views_iterationfilter_constructor_exists():
    assert callable(classLayout2Frontend_Views_IterationFilter.__init__)


def test_classlayout2frontend_views_iterationfilter_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_IterationFilter.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_pageview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_PageView)


def test_classlayout2frontend_views_pageview_constructor_exists():
    assert callable(classLayout2Frontend_Views_PageView.__init__)


def test_classlayout2frontend_views_pageview_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_PageView.__init__)
    params = list(sig.parameters.keys())
    assert "layoutType" in params, "Missing parameter 'layoutType'"
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend_views_pageview_has_layoutType():
    assert hasattr(classLayout2Frontend_Views_PageView, "layoutType")
    descriptor = None
    for klass in classLayout2Frontend_Views_PageView.__mro__:
        if "layoutType" in klass.__dict__:
            descriptor = klass.__dict__["layoutType"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_views_pageview_has_name():
    assert hasattr(classLayout2Frontend_Views_PageView, "name")
    descriptor = None
    for klass in classLayout2Frontend_Views_PageView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iterationfilter_is_not_abstract():
    assert not inspect.isabstract(IterationFilter)


def test_iterationfilter_constructor_exists():
    assert callable(IterationFilter.__init__)


def test_iterationfilter_constructor_args():
    sig = inspect.signature(IterationFilter.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_elementview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_ElementView)


def test_classlayout2frontend_views_elementview_constructor_exists():
    assert callable(classLayout2Frontend_Views_ElementView.__init__)


def test_classlayout2frontend_views_elementview_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_ElementView.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "dsisplayName" in params, "Missing parameter 'dsisplayName'"

def test_classlayout2frontend_views_elementview_has_name():
    assert hasattr(classLayout2Frontend_Views_ElementView, "name")
    descriptor = None
    for klass in classLayout2Frontend_Views_ElementView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_views_elementview_has_description():
    assert hasattr(classLayout2Frontend_Views_ElementView, "description")
    descriptor = None
    for klass in classLayout2Frontend_Views_ElementView.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_views_elementview_has_dsisplayName():
    assert hasattr(classLayout2Frontend_Views_ElementView, "dsisplayName")
    descriptor = None
    for klass in classLayout2Frontend_Views_ElementView.__mro__:
        if "dsisplayName" in klass.__dict__:
            descriptor = klass.__dict__["dsisplayName"]
            break
    assert isinstance(descriptor, property)



def test_elementview_is_not_abstract():
    assert not inspect.isabstract(ElementView)


def test_elementview_constructor_exists():
    assert callable(ElementView.__init__)


def test_elementview_constructor_args():
    sig = inspect.signature(ElementView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_atomicview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_AtomicView)


def test_classlayout2frontend_views_atomicview_constructor_exists():
    assert callable(classLayout2Frontend_Views_AtomicView.__init__)


def test_classlayout2frontend_views_atomicview_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_AtomicView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_containerview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_ContainerView)


def test_classlayout2frontend_views_containerview_constructor_exists():
    assert callable(classLayout2Frontend_Views_ContainerView.__init__)


def test_classlayout2frontend_views_containerview_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_ContainerView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_siteview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_SiteView)


def test_classlayout2frontend_views_siteview_constructor_exists():
    assert callable(classLayout2Frontend_Views_SiteView.__init__)


def test_classlayout2frontend_views_siteview_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_SiteView.__init__)
    params = list(sig.parameters.keys())
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "templateName" in params, "Missing parameter 'templateName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "templateColor" in params, "Missing parameter 'templateColor'"

def test_classlayout2frontend_views_siteview_has_displayName():
    assert hasattr(classLayout2Frontend_Views_SiteView, "displayName")
    descriptor = None
    for klass in classLayout2Frontend_Views_SiteView.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_views_siteview_has_templateName():
    assert hasattr(classLayout2Frontend_Views_SiteView, "templateName")
    descriptor = None
    for klass in classLayout2Frontend_Views_SiteView.__mro__:
        if "templateName" in klass.__dict__:
            descriptor = klass.__dict__["templateName"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_views_siteview_has_name():
    assert hasattr(classLayout2Frontend_Views_SiteView, "name")
    descriptor = None
    for klass in classLayout2Frontend_Views_SiteView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_views_siteview_has_templateColor():
    assert hasattr(classLayout2Frontend_Views_SiteView, "templateColor")
    descriptor = None
    for klass in classLayout2Frontend_Views_SiteView.__mro__:
        if "templateColor" in klass.__dict__:
            descriptor = klass.__dict__["templateColor"]
            break
    assert isinstance(descriptor, property)



def test_output_is_not_abstract():
    assert not inspect.isabstract(Output)


def test_output_constructor_exists():
    assert callable(Output.__init__)


def test_output_constructor_args():
    sig = inspect.signature(Output.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_image_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_Image)


def test_classlayout2frontend_views_image_constructor_exists():
    assert callable(classLayout2Frontend_Views_Image.__init__)


def test_classlayout2frontend_views_image_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_Image.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_classlayout2frontend_views_image_has_height():
    assert hasattr(classLayout2Frontend_Views_Image, "height")
    descriptor = None
    for klass in classLayout2Frontend_Views_Image.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_views_image_has_width():
    assert hasattr(classLayout2Frontend_Views_Image, "width")
    descriptor = None
    for klass in classLayout2Frontend_Views_Image.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_views_textarea_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_TextArea)


def test_classlayout2frontend_views_textarea_constructor_exists():
    assert callable(classLayout2Frontend_Views_TextArea.__init__)


def test_classlayout2frontend_views_textarea_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_TextArea.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_classlayout2frontend_views_textarea_has_value():
    assert hasattr(classLayout2Frontend_Views_TextArea, "value")
    descriptor = None
    for klass in classLayout2Frontend_Views_TextArea.__mro__:
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



def test_classlayout2frontend_views_selection_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_Selection)


def test_classlayout2frontend_views_selection_constructor_exists():
    assert callable(classLayout2Frontend_Views_Selection.__init__)


def test_classlayout2frontend_views_selection_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_Selection.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_fileupload_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_FileUpload)


def test_classlayout2frontend_views_fileupload_constructor_exists():
    assert callable(classLayout2Frontend_Views_FileUpload.__init__)


def test_classlayout2frontend_views_fileupload_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_FileUpload.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_inputtext_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_InputText)


def test_classlayout2frontend_views_inputtext_constructor_exists():
    assert callable(classLayout2Frontend_Views_InputText.__init__)


def test_classlayout2frontend_views_inputtext_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_InputText.__init__)
    params = list(sig.parameters.keys())
    assert "multiline" in params, "Missing parameter 'multiline'"

def test_classlayout2frontend_views_inputtext_has_multiline():
    assert hasattr(classLayout2Frontend_Views_InputText, "multiline")
    descriptor = None
    for klass in classLayout2Frontend_Views_InputText.__mro__:
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



def test_classlayout2frontend_views_output_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_Output)


def test_classlayout2frontend_views_output_constructor_exists():
    assert callable(classLayout2Frontend_Views_Output.__init__)


def test_classlayout2frontend_views_output_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_Output.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_input_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_Input)


def test_classlayout2frontend_views_input_constructor_exists():
    assert callable(classLayout2Frontend_Views_Input.__init__)


def test_classlayout2frontend_views_input_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_Input.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_classlayout2frontend_views_input_has_label():
    assert hasattr(classLayout2Frontend_Views_Input, "label")
    descriptor = None
    for klass in classLayout2Frontend_Views_Input.__mro__:
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



def test_classlayout2frontend_entities_reference_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_Reference)


def test_classlayout2frontend_entities_reference_constructor_exists():
    assert callable(classLayout2Frontend_Entities_Reference.__init__)


def test_classlayout2frontend_entities_reference_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_Reference.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_entities_composition_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_Composition)


def test_classlayout2frontend_entities_composition_constructor_exists():
    assert callable(classLayout2Frontend_Entities_Composition.__init__)


def test_classlayout2frontend_entities_composition_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_Composition.__init__)
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



def test_classlayout2frontend_entities_association_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_Association)


def test_classlayout2frontend_entities_association_constructor_exists():
    assert callable(classLayout2Frontend_Entities_Association.__init__)


def test_classlayout2frontend_entities_association_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_Association.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_classlayout2frontend_entities_association_has_many():
    assert hasattr(classLayout2Frontend_Entities_Association, "many")
    descriptor = None
    for klass in classLayout2Frontend_Entities_Association.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_entities_entitymodelelement_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_EntityModelElement)


def test_classlayout2frontend_entities_entitymodelelement_constructor_exists():
    assert callable(classLayout2Frontend_Entities_EntityModelElement.__init__)


def test_classlayout2frontend_entities_entitymodelelement_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_EntityModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "displayName" in params, "Missing parameter 'displayName'"

def test_classlayout2frontend_entities_entitymodelelement_has_name():
    assert hasattr(classLayout2Frontend_Entities_EntityModelElement, "name")
    descriptor = None
    for klass in classLayout2Frontend_Entities_EntityModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_entities_entitymodelelement_has_description():
    assert hasattr(classLayout2Frontend_Entities_EntityModelElement, "description")
    descriptor = None
    for klass in classLayout2Frontend_Entities_EntityModelElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_entities_entitymodelelement_has_displayName():
    assert hasattr(classLayout2Frontend_Entities_EntityModelElement, "displayName")
    descriptor = None
    for klass in classLayout2Frontend_Entities_EntityModelElement.__mro__:
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



def test_classlayout2frontend_entities_entity_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_Entity)


def test_classlayout2frontend_entities_entity_constructor_exists():
    assert callable(classLayout2Frontend_Entities_Entity.__init__)


def test_classlayout2frontend_entities_entity_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_classlayout2frontend_entities_entity_has_isAbstract():
    assert hasattr(classLayout2Frontend_Entities_Entity, "isAbstract")
    descriptor = None
    for klass in classLayout2Frontend_Entities_Entity.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_entities_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_StructuralFeature)


def test_classlayout2frontend_entities_structuralfeature_constructor_exists():
    assert callable(classLayout2Frontend_Entities_StructuralFeature.__init__)


def test_classlayout2frontend_entities_structuralfeature_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"

def test_classlayout2frontend_entities_structuralfeature_has_required():
    assert hasattr(classLayout2Frontend_Entities_StructuralFeature, "required")
    descriptor = None
    for klass in classLayout2Frontend_Entities_StructuralFeature.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_entities_entitiesmodel_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_EntitiesModel)


def test_classlayout2frontend_entities_entitiesmodel_constructor_exists():
    assert callable(classLayout2Frontend_Entities_EntitiesModel.__init__)


def test_classlayout2frontend_entities_entitiesmodel_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_EntitiesModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend_entities_entitiesmodel_has_name():
    assert hasattr(classLayout2Frontend_Entities_EntitiesModel, "name")
    descriptor = None
    for klass in classLayout2Frontend_Entities_EntitiesModel.__mro__:
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



def test_classlayout2frontend_views_staticcontainer_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_StaticContainer)


def test_classlayout2frontend_views_staticcontainer_constructor_exists():
    assert callable(classLayout2Frontend_Views_StaticContainer.__init__)


def test_classlayout2frontend_views_staticcontainer_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_StaticContainer.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_iterationcontainer_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_IterationContainer)


def test_classlayout2frontend_views_iterationcontainer_constructor_exists():
    assert callable(classLayout2Frontend_Views_IterationContainer.__init__)


def test_classlayout2frontend_views_iterationcontainer_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_IterationContainer.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_views_inputform_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Views_InputForm)


def test_classlayout2frontend_views_inputform_constructor_exists():
    assert callable(classLayout2Frontend_Views_InputForm.__init__)


def test_classlayout2frontend_views_inputform_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Views_InputForm.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_entities_literal_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_Literal)


def test_classlayout2frontend_entities_literal_constructor_exists():
    assert callable(classLayout2Frontend_Entities_Literal.__init__)


def test_classlayout2frontend_entities_literal_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_classlayout2frontend_entities_literal_has_value():
    assert hasattr(classLayout2Frontend_Entities_Literal, "value")
    descriptor = None
    for klass in classLayout2Frontend_Entities_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_entities_propertytype_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_PropertyType)


def test_classlayout2frontend_entities_propertytype_constructor_exists():
    assert callable(classLayout2Frontend_Entities_PropertyType.__init__)


def test_classlayout2frontend_entities_propertytype_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_PropertyType.__init__)
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



def test_classlayout2frontend_entities_enumeration_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_Enumeration)


def test_classlayout2frontend_entities_enumeration_constructor_exists():
    assert callable(classLayout2Frontend_Entities_Enumeration.__init__)


def test_classlayout2frontend_entities_enumeration_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_entities_primitivetype_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_PrimitiveType)


def test_classlayout2frontend_entities_primitivetype_constructor_exists():
    assert callable(classLayout2Frontend_Entities_PrimitiveType.__init__)


def test_classlayout2frontend_entities_primitivetype_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_entities_property_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entities_Property)


def test_classlayout2frontend_entities_property_constructor_exists():
    assert callable(classLayout2Frontend_Entities_Property.__init__)


def test_classlayout2frontend_entities_property_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entities_Property.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_classlayout2frontend_entities_property_has_defaultValue():
    assert hasattr(classLayout2Frontend_Entities_Property, "defaultValue")
    descriptor = None
    for klass in classLayout2Frontend_Entities_Property.__mro__:
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



def test_classlayout2frontend_project_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Project)


def test_classlayout2frontend_project_constructor_exists():
    assert callable(classLayout2Frontend_Project.__init__)


def test_classlayout2frontend_project_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend_project_has_name():
    assert hasattr(classLayout2Frontend_Project, "name")
    descriptor = None
    for klass in classLayout2Frontend_Project.__mro__:
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
        "THREE_COLUMNS",
        "SINGLE_COLUMN",
        "RIGHT_BAR",
        "LEFT_BAR",
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
classLayout2Frontend_Views_CheckList_strategy = st.builds(
    classLayout2Frontend_Views_CheckList,
)
classLayout2Frontend_Views_List_strategy = st.builds(
    classLayout2Frontend_Views_List,
    multiple=
        st.booleans()
)
classLayout2Frontend_Views_RadioButtonGroup_strategy = st.builds(
    classLayout2Frontend_Views_RadioButtonGroup,
)
classLayout2Frontend_Views_Autocomplete_strategy = st.builds(
    classLayout2Frontend_Views_Autocomplete,
    multiple=
        st.booleans()
)
classLayout2Frontend_Views_Dropdownlist_strategy = st.builds(
    classLayout2Frontend_Views_Dropdownlist,
)
classLayout2Frontend_Views_IterationFilter_strategy = st.builds(
    classLayout2Frontend_Views_IterationFilter,
)
classLayout2Frontend_Views_PageView_strategy = st.builds(
    classLayout2Frontend_Views_PageView,
    layoutType=
        safe_text,
    name=
        safe_text
)
IterationFilter_strategy = st.builds(
    IterationFilter,
)
classLayout2Frontend_Views_ElementView_strategy = st.builds(
    classLayout2Frontend_Views_ElementView,
    name=
        safe_text,
    description=
        safe_text,
    dsisplayName=
        safe_text
)
ElementView_strategy = st.builds(
    ElementView,
)
classLayout2Frontend_Views_AtomicView_strategy = st.builds(
    classLayout2Frontend_Views_AtomicView,
)
classLayout2Frontend_Views_ContainerView_strategy = st.builds(
    classLayout2Frontend_Views_ContainerView,
)
classLayout2Frontend_Views_SiteView_strategy = st.builds(
    classLayout2Frontend_Views_SiteView,
    displayName=
        safe_text,
    templateName=
        safe_text,
    name=
        safe_text,
    templateColor=
        safe_text
)
Output_strategy = st.builds(
    Output,
)
classLayout2Frontend_Views_Image_strategy = st.builds(
    classLayout2Frontend_Views_Image,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
classLayout2Frontend_Views_TextArea_strategy = st.builds(
    classLayout2Frontend_Views_TextArea,
    value=
        safe_text
)
Input_strategy = st.builds(
    Input,
)
classLayout2Frontend_Views_Selection_strategy = st.builds(
    classLayout2Frontend_Views_Selection,
)
classLayout2Frontend_Views_FileUpload_strategy = st.builds(
    classLayout2Frontend_Views_FileUpload,
)
classLayout2Frontend_Views_InputText_strategy = st.builds(
    classLayout2Frontend_Views_InputText,
    multiline=
        st.booleans()
)
AtomicView_strategy = st.builds(
    AtomicView,
)
classLayout2Frontend_Views_Output_strategy = st.builds(
    classLayout2Frontend_Views_Output,
)
classLayout2Frontend_Views_Input_strategy = st.builds(
    classLayout2Frontend_Views_Input,
    label=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
classLayout2Frontend_Entities_Reference_strategy = st.builds(
    classLayout2Frontend_Entities_Reference,
)
classLayout2Frontend_Entities_Composition_strategy = st.builds(
    classLayout2Frontend_Entities_Composition,
)
Entity_strategy = st.builds(
    Entity,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
classLayout2Frontend_Entities_Association_strategy = st.builds(
    classLayout2Frontend_Entities_Association,
    many=
        st.booleans()
)
classLayout2Frontend_Entities_EntityModelElement_strategy = st.builds(
    classLayout2Frontend_Entities_EntityModelElement,
    name=
        safe_text,
    description=
        safe_text,
    displayName=
        safe_text
)
EntityModelElement_strategy = st.builds(
    EntityModelElement,
)
classLayout2Frontend_Entities_Entity_strategy = st.builds(
    classLayout2Frontend_Entities_Entity,
    isAbstract=
        st.booleans()
)
classLayout2Frontend_Entities_StructuralFeature_strategy = st.builds(
    classLayout2Frontend_Entities_StructuralFeature,
    required=
        st.booleans()
)
classLayout2Frontend_Entities_EntitiesModel_strategy = st.builds(
    classLayout2Frontend_Entities_EntitiesModel,
    name=
        safe_text
)
ContainerView_strategy = st.builds(
    ContainerView,
)
classLayout2Frontend_Views_StaticContainer_strategy = st.builds(
    classLayout2Frontend_Views_StaticContainer,
)
classLayout2Frontend_Views_IterationContainer_strategy = st.builds(
    classLayout2Frontend_Views_IterationContainer,
)
classLayout2Frontend_Views_InputForm_strategy = st.builds(
    classLayout2Frontend_Views_InputForm,
)
classLayout2Frontend_Entities_Literal_strategy = st.builds(
    classLayout2Frontend_Entities_Literal,
    value=
        st.integers()
)
classLayout2Frontend_Entities_PropertyType_strategy = st.builds(
    classLayout2Frontend_Entities_PropertyType,
)
Literal_strategy = st.builds(
    Literal,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
classLayout2Frontend_Entities_Enumeration_strategy = st.builds(
    classLayout2Frontend_Entities_Enumeration,
)
classLayout2Frontend_Entities_PrimitiveType_strategy = st.builds(
    classLayout2Frontend_Entities_PrimitiveType,
)
classLayout2Frontend_Entities_Property_strategy = st.builds(
    classLayout2Frontend_Entities_Property,
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
classLayout2Frontend_Project_strategy = st.builds(
    classLayout2Frontend_Project,
    name=
        safe_text
)

@given(instance=Selection_strategy)
@settings(max_examples=50)
def test_selection_instantiation(instance):
    assert isinstance(instance, Selection)

@given(instance=classLayout2Frontend_Views_CheckList_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_checklist_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_CheckList)

@given(instance=classLayout2Frontend_Views_List_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_list_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_List)



@given(instance=classLayout2Frontend_Views_List_strategy)
def test_classlayout2frontend_views_list_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=classLayout2Frontend_Views_RadioButtonGroup_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_radiobuttongroup_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_RadioButtonGroup)

@given(instance=classLayout2Frontend_Views_Autocomplete_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_autocomplete_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_Autocomplete)



@given(instance=classLayout2Frontend_Views_Autocomplete_strategy)
def test_classlayout2frontend_views_autocomplete_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=classLayout2Frontend_Views_Dropdownlist_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_dropdownlist_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_Dropdownlist)

@given(instance=classLayout2Frontend_Views_IterationFilter_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_iterationfilter_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_IterationFilter)

@given(instance=classLayout2Frontend_Views_PageView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_pageview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_PageView)



@given(instance=classLayout2Frontend_Views_PageView_strategy)
def test_classlayout2frontend_views_pageview_layoutType_setter(instance):
    original = instance.layoutType
    instance.layoutType = original
    assert instance.layoutType == original



@given(instance=classLayout2Frontend_Views_PageView_strategy)
def test_classlayout2frontend_views_pageview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IterationFilter_strategy)
@settings(max_examples=50)
def test_iterationfilter_instantiation(instance):
    assert isinstance(instance, IterationFilter)

@given(instance=classLayout2Frontend_Views_ElementView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_elementview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_ElementView)



@given(instance=classLayout2Frontend_Views_ElementView_strategy)
def test_classlayout2frontend_views_elementview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=classLayout2Frontend_Views_ElementView_strategy)
def test_classlayout2frontend_views_elementview_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=classLayout2Frontend_Views_ElementView_strategy)
def test_classlayout2frontend_views_elementview_dsisplayName_setter(instance):
    original = instance.dsisplayName
    instance.dsisplayName = original
    assert instance.dsisplayName == original

@given(instance=ElementView_strategy)
@settings(max_examples=50)
def test_elementview_instantiation(instance):
    assert isinstance(instance, ElementView)

@given(instance=classLayout2Frontend_Views_AtomicView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_atomicview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_AtomicView)

@given(instance=classLayout2Frontend_Views_ContainerView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_containerview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_ContainerView)

@given(instance=classLayout2Frontend_Views_SiteView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_siteview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_SiteView)



@given(instance=classLayout2Frontend_Views_SiteView_strategy)
def test_classlayout2frontend_views_siteview_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=classLayout2Frontend_Views_SiteView_strategy)
def test_classlayout2frontend_views_siteview_templateName_setter(instance):
    original = instance.templateName
    instance.templateName = original
    assert instance.templateName == original



@given(instance=classLayout2Frontend_Views_SiteView_strategy)
def test_classlayout2frontend_views_siteview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=classLayout2Frontend_Views_SiteView_strategy)
def test_classlayout2frontend_views_siteview_templateColor_setter(instance):
    original = instance.templateColor
    instance.templateColor = original
    assert instance.templateColor == original

@given(instance=Output_strategy)
@settings(max_examples=50)
def test_output_instantiation(instance):
    assert isinstance(instance, Output)

@given(instance=classLayout2Frontend_Views_Image_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_image_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_Image)



@given(instance=classLayout2Frontend_Views_Image_strategy)
def test_classlayout2frontend_views_image_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=classLayout2Frontend_Views_Image_strategy)
def test_classlayout2frontend_views_image_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=classLayout2Frontend_Views_TextArea_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_textarea_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_TextArea)



@given(instance=classLayout2Frontend_Views_TextArea_strategy)
def test_classlayout2frontend_views_textarea_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Input_strategy)
@settings(max_examples=50)
def test_input_instantiation(instance):
    assert isinstance(instance, Input)

@given(instance=classLayout2Frontend_Views_Selection_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_selection_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_Selection)

@given(instance=classLayout2Frontend_Views_FileUpload_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_fileupload_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_FileUpload)

@given(instance=classLayout2Frontend_Views_InputText_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_inputtext_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_InputText)



@given(instance=classLayout2Frontend_Views_InputText_strategy)
def test_classlayout2frontend_views_inputtext_multiline_setter(instance):
    original = instance.multiline
    instance.multiline = original
    assert instance.multiline == original

@given(instance=AtomicView_strategy)
@settings(max_examples=50)
def test_atomicview_instantiation(instance):
    assert isinstance(instance, AtomicView)

@given(instance=classLayout2Frontend_Views_Output_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_output_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_Output)

@given(instance=classLayout2Frontend_Views_Input_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_input_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_Input)



@given(instance=classLayout2Frontend_Views_Input_strategy)
def test_classlayout2frontend_views_input_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=classLayout2Frontend_Entities_Reference_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_reference_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_Reference)

@given(instance=classLayout2Frontend_Entities_Composition_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_composition_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_Composition)

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=classLayout2Frontend_Entities_Association_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_association_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_Association)



@given(instance=classLayout2Frontend_Entities_Association_strategy)
def test_classlayout2frontend_entities_association_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=classLayout2Frontend_Entities_EntityModelElement_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_entitymodelelement_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_EntityModelElement)



@given(instance=classLayout2Frontend_Entities_EntityModelElement_strategy)
def test_classlayout2frontend_entities_entitymodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=classLayout2Frontend_Entities_EntityModelElement_strategy)
def test_classlayout2frontend_entities_entitymodelelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=classLayout2Frontend_Entities_EntityModelElement_strategy)
def test_classlayout2frontend_entities_entitymodelelement_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original

@given(instance=EntityModelElement_strategy)
@settings(max_examples=50)
def test_entitymodelelement_instantiation(instance):
    assert isinstance(instance, EntityModelElement)

@given(instance=classLayout2Frontend_Entities_Entity_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_entity_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_Entity)



@given(instance=classLayout2Frontend_Entities_Entity_strategy)
def test_classlayout2frontend_entities_entity_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=classLayout2Frontend_Entities_StructuralFeature_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_structuralfeature_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_StructuralFeature)



@given(instance=classLayout2Frontend_Entities_StructuralFeature_strategy)
def test_classlayout2frontend_entities_structuralfeature_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=classLayout2Frontend_Entities_EntitiesModel_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_entitiesmodel_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_EntitiesModel)



@given(instance=classLayout2Frontend_Entities_EntitiesModel_strategy)
def test_classlayout2frontend_entities_entitiesmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ContainerView_strategy)
@settings(max_examples=50)
def test_containerview_instantiation(instance):
    assert isinstance(instance, ContainerView)

@given(instance=classLayout2Frontend_Views_StaticContainer_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_staticcontainer_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_StaticContainer)

@given(instance=classLayout2Frontend_Views_IterationContainer_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_iterationcontainer_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_IterationContainer)

@given(instance=classLayout2Frontend_Views_InputForm_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_views_inputform_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Views_InputForm)

@given(instance=classLayout2Frontend_Entities_Literal_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_literal_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_Literal)



@given(instance=classLayout2Frontend_Entities_Literal_strategy)
def test_classlayout2frontend_entities_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=classLayout2Frontend_Entities_PropertyType_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_propertytype_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_PropertyType)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=classLayout2Frontend_Entities_Enumeration_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_enumeration_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_Enumeration)

@given(instance=classLayout2Frontend_Entities_PrimitiveType_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_primitivetype_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_PrimitiveType)

@given(instance=classLayout2Frontend_Entities_Property_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entities_property_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entities_Property)



@given(instance=classLayout2Frontend_Entities_Property_strategy)
def test_classlayout2frontend_entities_property_defaultValue_setter(instance):
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

@given(instance=classLayout2Frontend_Project_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_project_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Project)



@given(instance=classLayout2Frontend_Project_strategy)
def test_classlayout2frontend_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
