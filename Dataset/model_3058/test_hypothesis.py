import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ContainerView,
    classLayout2Frontend_InputForm,
    classLayout2Frontend_IterationContainer,
    PropertyType,
    classLayout2Frontend_PrimitiveType,
    classLayout2Frontend_StaticContainer,
    classLayout2Frontend_ElementView,
    classLayout2Frontend_Enumeration,
    Input,
    classLayout2Frontend_FileUpload,
    classLayout2Frontend_Selection,
    classLayout2Frontend_InputText,
    classLayout2Frontend_IterationFilter,
    AtomicView,
    classLayout2Frontend_Input,
    classLayout2Frontend_Output,
    Output,
    classLayout2Frontend_TextArea,
    classLayout2Frontend_Image,
    Selection,
    classLayout2Frontend_List,
    classLayout2Frontend_RadioButtonGroup,
    classLayout2Frontend_Dropdownlist,
    classLayout2Frontend_CheckList,
    classLayout2Frontend_Autocomplete,
    ElementView,
    classLayout2Frontend_AtomicView,
    classLayout2Frontend_SiteView,
    classLayout2Frontend_EntitiesModel,
    classLayout2Frontend_Project,
    classLayout2Frontend_EntityModelElement,
    EntityModelElement,
    classLayout2Frontend_StructuralFeature,
    classLayout2Frontend_Literal,
    classLayout2Frontend_PropertyType,
    classLayout2Frontend_Entity,
    StructuralFeature,
    classLayout2Frontend_Property,
    classLayout2Frontend_Association,
    Association,
    classLayout2Frontend_Reference,
    classLayout2Frontend_Composition,
    classLayout2Frontend_ContainerView,
    classLayout2Frontend_PageView,
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



def test_classlayout2frontend_inputform_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_InputForm)


def test_classlayout2frontend_inputform_constructor_exists():
    assert callable(classLayout2Frontend_InputForm.__init__)


def test_classlayout2frontend_inputform_constructor_args():
    sig = inspect.signature(classLayout2Frontend_InputForm.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_iterationcontainer_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_IterationContainer)


def test_classlayout2frontend_iterationcontainer_constructor_exists():
    assert callable(classLayout2Frontend_IterationContainer.__init__)


def test_classlayout2frontend_iterationcontainer_constructor_args():
    sig = inspect.signature(classLayout2Frontend_IterationContainer.__init__)
    params = list(sig.parameters.keys())



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_primitivetype_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_PrimitiveType)


def test_classlayout2frontend_primitivetype_constructor_exists():
    assert callable(classLayout2Frontend_PrimitiveType.__init__)


def test_classlayout2frontend_primitivetype_constructor_args():
    sig = inspect.signature(classLayout2Frontend_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_staticcontainer_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_StaticContainer)


def test_classlayout2frontend_staticcontainer_constructor_exists():
    assert callable(classLayout2Frontend_StaticContainer.__init__)


def test_classlayout2frontend_staticcontainer_constructor_args():
    sig = inspect.signature(classLayout2Frontend_StaticContainer.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_elementview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_ElementView)


def test_classlayout2frontend_elementview_constructor_exists():
    assert callable(classLayout2Frontend_ElementView.__init__)


def test_classlayout2frontend_elementview_constructor_args():
    sig = inspect.signature(classLayout2Frontend_ElementView.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend_elementview_has_description():
    assert hasattr(classLayout2Frontend_ElementView, "description")
    descriptor = None
    for klass in classLayout2Frontend_ElementView.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_elementview_has_displayName():
    assert hasattr(classLayout2Frontend_ElementView, "displayName")
    descriptor = None
    for klass in classLayout2Frontend_ElementView.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_elementview_has_name():
    assert hasattr(classLayout2Frontend_ElementView, "name")
    descriptor = None
    for klass in classLayout2Frontend_ElementView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_enumeration_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Enumeration)


def test_classlayout2frontend_enumeration_constructor_exists():
    assert callable(classLayout2Frontend_Enumeration.__init__)


def test_classlayout2frontend_enumeration_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_input_is_not_abstract():
    assert not inspect.isabstract(Input)


def test_input_constructor_exists():
    assert callable(Input.__init__)


def test_input_constructor_args():
    sig = inspect.signature(Input.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_fileupload_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_FileUpload)


def test_classlayout2frontend_fileupload_constructor_exists():
    assert callable(classLayout2Frontend_FileUpload.__init__)


def test_classlayout2frontend_fileupload_constructor_args():
    sig = inspect.signature(classLayout2Frontend_FileUpload.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_selection_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Selection)


def test_classlayout2frontend_selection_constructor_exists():
    assert callable(classLayout2Frontend_Selection.__init__)


def test_classlayout2frontend_selection_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Selection.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_inputtext_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_InputText)


def test_classlayout2frontend_inputtext_constructor_exists():
    assert callable(classLayout2Frontend_InputText.__init__)


def test_classlayout2frontend_inputtext_constructor_args():
    sig = inspect.signature(classLayout2Frontend_InputText.__init__)
    params = list(sig.parameters.keys())
    assert "multiline" in params, "Missing parameter 'multiline'"

def test_classlayout2frontend_inputtext_has_multiline():
    assert hasattr(classLayout2Frontend_InputText, "multiline")
    descriptor = None
    for klass in classLayout2Frontend_InputText.__mro__:
        if "multiline" in klass.__dict__:
            descriptor = klass.__dict__["multiline"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_iterationfilter_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_IterationFilter)


def test_classlayout2frontend_iterationfilter_constructor_exists():
    assert callable(classLayout2Frontend_IterationFilter.__init__)


def test_classlayout2frontend_iterationfilter_constructor_args():
    sig = inspect.signature(classLayout2Frontend_IterationFilter.__init__)
    params = list(sig.parameters.keys())



def test_atomicview_is_not_abstract():
    assert not inspect.isabstract(AtomicView)


def test_atomicview_constructor_exists():
    assert callable(AtomicView.__init__)


def test_atomicview_constructor_args():
    sig = inspect.signature(AtomicView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_input_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Input)


def test_classlayout2frontend_input_constructor_exists():
    assert callable(classLayout2Frontend_Input.__init__)


def test_classlayout2frontend_input_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Input.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_classlayout2frontend_input_has_label():
    assert hasattr(classLayout2Frontend_Input, "label")
    descriptor = None
    for klass in classLayout2Frontend_Input.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_output_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Output)


def test_classlayout2frontend_output_constructor_exists():
    assert callable(classLayout2Frontend_Output.__init__)


def test_classlayout2frontend_output_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Output.__init__)
    params = list(sig.parameters.keys())



def test_output_is_not_abstract():
    assert not inspect.isabstract(Output)


def test_output_constructor_exists():
    assert callable(Output.__init__)


def test_output_constructor_args():
    sig = inspect.signature(Output.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_textarea_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_TextArea)


def test_classlayout2frontend_textarea_constructor_exists():
    assert callable(classLayout2Frontend_TextArea.__init__)


def test_classlayout2frontend_textarea_constructor_args():
    sig = inspect.signature(classLayout2Frontend_TextArea.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "isTitle" in params, "Missing parameter 'isTitle'"

def test_classlayout2frontend_textarea_has_value():
    assert hasattr(classLayout2Frontend_TextArea, "value")
    descriptor = None
    for klass in classLayout2Frontend_TextArea.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_textarea_has_isTitle():
    assert hasattr(classLayout2Frontend_TextArea, "isTitle")
    descriptor = None
    for klass in classLayout2Frontend_TextArea.__mro__:
        if "isTitle" in klass.__dict__:
            descriptor = klass.__dict__["isTitle"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_image_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Image)


def test_classlayout2frontend_image_constructor_exists():
    assert callable(classLayout2Frontend_Image.__init__)


def test_classlayout2frontend_image_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Image.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_classlayout2frontend_image_has_height():
    assert hasattr(classLayout2Frontend_Image, "height")
    descriptor = None
    for klass in classLayout2Frontend_Image.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_image_has_width():
    assert hasattr(classLayout2Frontend_Image, "width")
    descriptor = None
    for klass in classLayout2Frontend_Image.__mro__:
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



def test_classlayout2frontend_list_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_List)


def test_classlayout2frontend_list_constructor_exists():
    assert callable(classLayout2Frontend_List.__init__)


def test_classlayout2frontend_list_constructor_args():
    sig = inspect.signature(classLayout2Frontend_List.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_classlayout2frontend_list_has_multiple():
    assert hasattr(classLayout2Frontend_List, "multiple")
    descriptor = None
    for klass in classLayout2Frontend_List.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_radiobuttongroup_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_RadioButtonGroup)


def test_classlayout2frontend_radiobuttongroup_constructor_exists():
    assert callable(classLayout2Frontend_RadioButtonGroup.__init__)


def test_classlayout2frontend_radiobuttongroup_constructor_args():
    sig = inspect.signature(classLayout2Frontend_RadioButtonGroup.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_dropdownlist_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Dropdownlist)


def test_classlayout2frontend_dropdownlist_constructor_exists():
    assert callable(classLayout2Frontend_Dropdownlist.__init__)


def test_classlayout2frontend_dropdownlist_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Dropdownlist.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_checklist_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_CheckList)


def test_classlayout2frontend_checklist_constructor_exists():
    assert callable(classLayout2Frontend_CheckList.__init__)


def test_classlayout2frontend_checklist_constructor_args():
    sig = inspect.signature(classLayout2Frontend_CheckList.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_autocomplete_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Autocomplete)


def test_classlayout2frontend_autocomplete_constructor_exists():
    assert callable(classLayout2Frontend_Autocomplete.__init__)


def test_classlayout2frontend_autocomplete_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Autocomplete.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_classlayout2frontend_autocomplete_has_multiple():
    assert hasattr(classLayout2Frontend_Autocomplete, "multiple")
    descriptor = None
    for klass in classLayout2Frontend_Autocomplete.__mro__:
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



def test_classlayout2frontend_atomicview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_AtomicView)


def test_classlayout2frontend_atomicview_constructor_exists():
    assert callable(classLayout2Frontend_AtomicView.__init__)


def test_classlayout2frontend_atomicview_constructor_args():
    sig = inspect.signature(classLayout2Frontend_AtomicView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_siteview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_SiteView)


def test_classlayout2frontend_siteview_constructor_exists():
    assert callable(classLayout2Frontend_SiteView.__init__)


def test_classlayout2frontend_siteview_constructor_args():
    sig = inspect.signature(classLayout2Frontend_SiteView.__init__)
    params = list(sig.parameters.keys())
    assert "templateName" in params, "Missing parameter 'templateName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "templateColor" in params, "Missing parameter 'templateColor'"
    assert "displayName" in params, "Missing parameter 'displayName'"

def test_classlayout2frontend_siteview_has_templateName():
    assert hasattr(classLayout2Frontend_SiteView, "templateName")
    descriptor = None
    for klass in classLayout2Frontend_SiteView.__mro__:
        if "templateName" in klass.__dict__:
            descriptor = klass.__dict__["templateName"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_siteview_has_name():
    assert hasattr(classLayout2Frontend_SiteView, "name")
    descriptor = None
    for klass in classLayout2Frontend_SiteView.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_siteview_has_templateColor():
    assert hasattr(classLayout2Frontend_SiteView, "templateColor")
    descriptor = None
    for klass in classLayout2Frontend_SiteView.__mro__:
        if "templateColor" in klass.__dict__:
            descriptor = klass.__dict__["templateColor"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_siteview_has_displayName():
    assert hasattr(classLayout2Frontend_SiteView, "displayName")
    descriptor = None
    for klass in classLayout2Frontend_SiteView.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_entitiesmodel_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_EntitiesModel)


def test_classlayout2frontend_entitiesmodel_constructor_exists():
    assert callable(classLayout2Frontend_EntitiesModel.__init__)


def test_classlayout2frontend_entitiesmodel_constructor_args():
    sig = inspect.signature(classLayout2Frontend_EntitiesModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend_entitiesmodel_has_name():
    assert hasattr(classLayout2Frontend_EntitiesModel, "name")
    descriptor = None
    for klass in classLayout2Frontend_EntitiesModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_classlayout2frontend_entitymodelelement_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_EntityModelElement)


def test_classlayout2frontend_entitymodelelement_constructor_exists():
    assert callable(classLayout2Frontend_EntityModelElement.__init__)


def test_classlayout2frontend_entitymodelelement_constructor_args():
    sig = inspect.signature(classLayout2Frontend_EntityModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend_entitymodelelement_has_displayName():
    assert hasattr(classLayout2Frontend_EntityModelElement, "displayName")
    descriptor = None
    for klass in classLayout2Frontend_EntityModelElement.__mro__:
        if "displayName" in klass.__dict__:
            descriptor = klass.__dict__["displayName"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_entitymodelelement_has_description():
    assert hasattr(classLayout2Frontend_EntityModelElement, "description")
    descriptor = None
    for klass in classLayout2Frontend_EntityModelElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_entitymodelelement_has_name():
    assert hasattr(classLayout2Frontend_EntityModelElement, "name")
    descriptor = None
    for klass in classLayout2Frontend_EntityModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitymodelelement_is_not_abstract():
    assert not inspect.isabstract(EntityModelElement)


def test_entitymodelelement_constructor_exists():
    assert callable(EntityModelElement.__init__)


def test_entitymodelelement_constructor_args():
    sig = inspect.signature(EntityModelElement.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_StructuralFeature)


def test_classlayout2frontend_structuralfeature_constructor_exists():
    assert callable(classLayout2Frontend_StructuralFeature.__init__)


def test_classlayout2frontend_structuralfeature_constructor_args():
    sig = inspect.signature(classLayout2Frontend_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"

def test_classlayout2frontend_structuralfeature_has_required():
    assert hasattr(classLayout2Frontend_StructuralFeature, "required")
    descriptor = None
    for klass in classLayout2Frontend_StructuralFeature.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_literal_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Literal)


def test_classlayout2frontend_literal_constructor_exists():
    assert callable(classLayout2Frontend_Literal.__init__)


def test_classlayout2frontend_literal_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_classlayout2frontend_literal_has_value():
    assert hasattr(classLayout2Frontend_Literal, "value")
    descriptor = None
    for klass in classLayout2Frontend_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_propertytype_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_PropertyType)


def test_classlayout2frontend_propertytype_constructor_exists():
    assert callable(classLayout2Frontend_PropertyType.__init__)


def test_classlayout2frontend_propertytype_constructor_args():
    sig = inspect.signature(classLayout2Frontend_PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_entity_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Entity)


def test_classlayout2frontend_entity_constructor_exists():
    assert callable(classLayout2Frontend_Entity.__init__)


def test_classlayout2frontend_entity_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_classlayout2frontend_entity_has_isAbstract():
    assert hasattr(classLayout2Frontend_Entity, "isAbstract")
    descriptor = None
    for klass in classLayout2Frontend_Entity.__mro__:
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



def test_classlayout2frontend_property_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Property)


def test_classlayout2frontend_property_constructor_exists():
    assert callable(classLayout2Frontend_Property.__init__)


def test_classlayout2frontend_property_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Property.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_classlayout2frontend_property_has_defaultValue():
    assert hasattr(classLayout2Frontend_Property, "defaultValue")
    descriptor = None
    for klass in classLayout2Frontend_Property.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_classlayout2frontend_association_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Association)


def test_classlayout2frontend_association_constructor_exists():
    assert callable(classLayout2Frontend_Association.__init__)


def test_classlayout2frontend_association_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Association.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_classlayout2frontend_association_has_many():
    assert hasattr(classLayout2Frontend_Association, "many")
    descriptor = None
    for klass in classLayout2Frontend_Association.__mro__:
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



def test_classlayout2frontend_reference_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Reference)


def test_classlayout2frontend_reference_constructor_exists():
    assert callable(classLayout2Frontend_Reference.__init__)


def test_classlayout2frontend_reference_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Reference.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_composition_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_Composition)


def test_classlayout2frontend_composition_constructor_exists():
    assert callable(classLayout2Frontend_Composition.__init__)


def test_classlayout2frontend_composition_constructor_args():
    sig = inspect.signature(classLayout2Frontend_Composition.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_containerview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_ContainerView)


def test_classlayout2frontend_containerview_constructor_exists():
    assert callable(classLayout2Frontend_ContainerView.__init__)


def test_classlayout2frontend_containerview_constructor_args():
    sig = inspect.signature(classLayout2Frontend_ContainerView.__init__)
    params = list(sig.parameters.keys())



def test_classlayout2frontend_pageview_is_not_abstract():
    assert not inspect.isabstract(classLayout2Frontend_PageView)


def test_classlayout2frontend_pageview_constructor_exists():
    assert callable(classLayout2Frontend_PageView.__init__)


def test_classlayout2frontend_pageview_constructor_args():
    sig = inspect.signature(classLayout2Frontend_PageView.__init__)
    params = list(sig.parameters.keys())
    assert "layoutType" in params, "Missing parameter 'layoutType'"
    assert "name" in params, "Missing parameter 'name'"

def test_classlayout2frontend_pageview_has_layoutType():
    assert hasattr(classLayout2Frontend_PageView, "layoutType")
    descriptor = None
    for klass in classLayout2Frontend_PageView.__mro__:
        if "layoutType" in klass.__dict__:
            descriptor = klass.__dict__["layoutType"]
            break
    assert isinstance(descriptor, property)

def test_classlayout2frontend_pageview_has_name():
    assert hasattr(classLayout2Frontend_PageView, "name")
    descriptor = None
    for klass in classLayout2Frontend_PageView.__mro__:
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
        "THREE_COLUMNS",
        "LEFT_BAR",
        "TWO_COLUMNS",
        "RIGHT_BAR",
        "SINGLE_COLUMN",
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
classLayout2Frontend_InputForm_strategy = st.builds(
    classLayout2Frontend_InputForm,
)
classLayout2Frontend_IterationContainer_strategy = st.builds(
    classLayout2Frontend_IterationContainer,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
classLayout2Frontend_PrimitiveType_strategy = st.builds(
    classLayout2Frontend_PrimitiveType,
)
classLayout2Frontend_StaticContainer_strategy = st.builds(
    classLayout2Frontend_StaticContainer,
)
classLayout2Frontend_ElementView_strategy = st.builds(
    classLayout2Frontend_ElementView,
    description=
        safe_text,
    displayName=
        safe_text,
    name=
        safe_text
)
classLayout2Frontend_Enumeration_strategy = st.builds(
    classLayout2Frontend_Enumeration,
)
Input_strategy = st.builds(
    Input,
)
classLayout2Frontend_FileUpload_strategy = st.builds(
    classLayout2Frontend_FileUpload,
)
classLayout2Frontend_Selection_strategy = st.builds(
    classLayout2Frontend_Selection,
)
classLayout2Frontend_InputText_strategy = st.builds(
    classLayout2Frontend_InputText,
    multiline=
        st.booleans()
)
classLayout2Frontend_IterationFilter_strategy = st.builds(
    classLayout2Frontend_IterationFilter,
)
AtomicView_strategy = st.builds(
    AtomicView,
)
classLayout2Frontend_Input_strategy = st.builds(
    classLayout2Frontend_Input,
    label=
        safe_text
)
classLayout2Frontend_Output_strategy = st.builds(
    classLayout2Frontend_Output,
)
Output_strategy = st.builds(
    Output,
)
classLayout2Frontend_TextArea_strategy = st.builds(
    classLayout2Frontend_TextArea,
    value=
        safe_text,
    isTitle=
        st.booleans()
)
classLayout2Frontend_Image_strategy = st.builds(
    classLayout2Frontend_Image,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Selection_strategy = st.builds(
    Selection,
)
classLayout2Frontend_List_strategy = st.builds(
    classLayout2Frontend_List,
    multiple=
        st.booleans()
)
classLayout2Frontend_RadioButtonGroup_strategy = st.builds(
    classLayout2Frontend_RadioButtonGroup,
)
classLayout2Frontend_Dropdownlist_strategy = st.builds(
    classLayout2Frontend_Dropdownlist,
)
classLayout2Frontend_CheckList_strategy = st.builds(
    classLayout2Frontend_CheckList,
)
classLayout2Frontend_Autocomplete_strategy = st.builds(
    classLayout2Frontend_Autocomplete,
    multiple=
        st.booleans()
)
ElementView_strategy = st.builds(
    ElementView,
)
classLayout2Frontend_AtomicView_strategy = st.builds(
    classLayout2Frontend_AtomicView,
)
classLayout2Frontend_SiteView_strategy = st.builds(
    classLayout2Frontend_SiteView,
    templateName=
        safe_text,
    name=
        safe_text,
    templateColor=
        safe_text,
    displayName=
        safe_text
)
classLayout2Frontend_EntitiesModel_strategy = st.builds(
    classLayout2Frontend_EntitiesModel,
    name=
        safe_text
)
classLayout2Frontend_Project_strategy = st.builds(
    classLayout2Frontend_Project,
    name=
        safe_text
)
classLayout2Frontend_EntityModelElement_strategy = st.builds(
    classLayout2Frontend_EntityModelElement,
    displayName=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
EntityModelElement_strategy = st.builds(
    EntityModelElement,
)
classLayout2Frontend_StructuralFeature_strategy = st.builds(
    classLayout2Frontend_StructuralFeature,
    required=
        st.booleans()
)
classLayout2Frontend_Literal_strategy = st.builds(
    classLayout2Frontend_Literal,
    value=
        st.integers()
)
classLayout2Frontend_PropertyType_strategy = st.builds(
    classLayout2Frontend_PropertyType,
)
classLayout2Frontend_Entity_strategy = st.builds(
    classLayout2Frontend_Entity,
    isAbstract=
        st.booleans()
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
classLayout2Frontend_Property_strategy = st.builds(
    classLayout2Frontend_Property,
    defaultValue=
        safe_text
)
classLayout2Frontend_Association_strategy = st.builds(
    classLayout2Frontend_Association,
    many=
        st.booleans()
)
Association_strategy = st.builds(
    Association,
)
classLayout2Frontend_Reference_strategy = st.builds(
    classLayout2Frontend_Reference,
)
classLayout2Frontend_Composition_strategy = st.builds(
    classLayout2Frontend_Composition,
)
classLayout2Frontend_ContainerView_strategy = st.builds(
    classLayout2Frontend_ContainerView,
)
classLayout2Frontend_PageView_strategy = st.builds(
    classLayout2Frontend_PageView,
    layoutType=
        safe_text,
    name=
        safe_text
)

@given(instance=ContainerView_strategy)
@settings(max_examples=50)
def test_containerview_instantiation(instance):
    assert isinstance(instance, ContainerView)

@given(instance=classLayout2Frontend_InputForm_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_inputform_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_InputForm)

@given(instance=classLayout2Frontend_IterationContainer_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_iterationcontainer_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_IterationContainer)

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=classLayout2Frontend_PrimitiveType_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_primitivetype_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_PrimitiveType)

@given(instance=classLayout2Frontend_StaticContainer_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_staticcontainer_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_StaticContainer)

@given(instance=classLayout2Frontend_ElementView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_elementview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_ElementView)



@given(instance=classLayout2Frontend_ElementView_strategy)
def test_classlayout2frontend_elementview_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=classLayout2Frontend_ElementView_strategy)
def test_classlayout2frontend_elementview_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=classLayout2Frontend_ElementView_strategy)
def test_classlayout2frontend_elementview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classLayout2Frontend_Enumeration_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_enumeration_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Enumeration)

@given(instance=Input_strategy)
@settings(max_examples=50)
def test_input_instantiation(instance):
    assert isinstance(instance, Input)

@given(instance=classLayout2Frontend_FileUpload_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_fileupload_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_FileUpload)

@given(instance=classLayout2Frontend_Selection_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_selection_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Selection)

@given(instance=classLayout2Frontend_InputText_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_inputtext_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_InputText)



@given(instance=classLayout2Frontend_InputText_strategy)
def test_classlayout2frontend_inputtext_multiline_setter(instance):
    original = instance.multiline
    instance.multiline = original
    assert instance.multiline == original

@given(instance=classLayout2Frontend_IterationFilter_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_iterationfilter_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_IterationFilter)

@given(instance=AtomicView_strategy)
@settings(max_examples=50)
def test_atomicview_instantiation(instance):
    assert isinstance(instance, AtomicView)

@given(instance=classLayout2Frontend_Input_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_input_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Input)



@given(instance=classLayout2Frontend_Input_strategy)
def test_classlayout2frontend_input_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=classLayout2Frontend_Output_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_output_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Output)

@given(instance=Output_strategy)
@settings(max_examples=50)
def test_output_instantiation(instance):
    assert isinstance(instance, Output)

@given(instance=classLayout2Frontend_TextArea_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_textarea_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_TextArea)



@given(instance=classLayout2Frontend_TextArea_strategy)
def test_classlayout2frontend_textarea_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=classLayout2Frontend_TextArea_strategy)
def test_classlayout2frontend_textarea_isTitle_setter(instance):
    original = instance.isTitle
    instance.isTitle = original
    assert instance.isTitle == original

@given(instance=classLayout2Frontend_Image_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_image_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Image)



@given(instance=classLayout2Frontend_Image_strategy)
def test_classlayout2frontend_image_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=classLayout2Frontend_Image_strategy)
def test_classlayout2frontend_image_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=Selection_strategy)
@settings(max_examples=50)
def test_selection_instantiation(instance):
    assert isinstance(instance, Selection)

@given(instance=classLayout2Frontend_List_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_list_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_List)



@given(instance=classLayout2Frontend_List_strategy)
def test_classlayout2frontend_list_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=classLayout2Frontend_RadioButtonGroup_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_radiobuttongroup_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_RadioButtonGroup)

@given(instance=classLayout2Frontend_Dropdownlist_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_dropdownlist_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Dropdownlist)

@given(instance=classLayout2Frontend_CheckList_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_checklist_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_CheckList)

@given(instance=classLayout2Frontend_Autocomplete_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_autocomplete_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Autocomplete)



@given(instance=classLayout2Frontend_Autocomplete_strategy)
def test_classlayout2frontend_autocomplete_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=ElementView_strategy)
@settings(max_examples=50)
def test_elementview_instantiation(instance):
    assert isinstance(instance, ElementView)

@given(instance=classLayout2Frontend_AtomicView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_atomicview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_AtomicView)

@given(instance=classLayout2Frontend_SiteView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_siteview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_SiteView)



@given(instance=classLayout2Frontend_SiteView_strategy)
def test_classlayout2frontend_siteview_templateName_setter(instance):
    original = instance.templateName
    instance.templateName = original
    assert instance.templateName == original



@given(instance=classLayout2Frontend_SiteView_strategy)
def test_classlayout2frontend_siteview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=classLayout2Frontend_SiteView_strategy)
def test_classlayout2frontend_siteview_templateColor_setter(instance):
    original = instance.templateColor
    instance.templateColor = original
    assert instance.templateColor == original



@given(instance=classLayout2Frontend_SiteView_strategy)
def test_classlayout2frontend_siteview_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original

@given(instance=classLayout2Frontend_EntitiesModel_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entitiesmodel_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_EntitiesModel)



@given(instance=classLayout2Frontend_EntitiesModel_strategy)
def test_classlayout2frontend_entitiesmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classLayout2Frontend_Project_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_project_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Project)



@given(instance=classLayout2Frontend_Project_strategy)
def test_classlayout2frontend_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classLayout2Frontend_EntityModelElement_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entitymodelelement_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_EntityModelElement)



@given(instance=classLayout2Frontend_EntityModelElement_strategy)
def test_classlayout2frontend_entitymodelelement_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=classLayout2Frontend_EntityModelElement_strategy)
def test_classlayout2frontend_entitymodelelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=classLayout2Frontend_EntityModelElement_strategy)
def test_classlayout2frontend_entitymodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EntityModelElement_strategy)
@settings(max_examples=50)
def test_entitymodelelement_instantiation(instance):
    assert isinstance(instance, EntityModelElement)

@given(instance=classLayout2Frontend_StructuralFeature_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_structuralfeature_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_StructuralFeature)



@given(instance=classLayout2Frontend_StructuralFeature_strategy)
def test_classlayout2frontend_structuralfeature_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=classLayout2Frontend_Literal_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_literal_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Literal)



@given(instance=classLayout2Frontend_Literal_strategy)
def test_classlayout2frontend_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=classLayout2Frontend_PropertyType_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_propertytype_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_PropertyType)

@given(instance=classLayout2Frontend_Entity_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_entity_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Entity)



@given(instance=classLayout2Frontend_Entity_strategy)
def test_classlayout2frontend_entity_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=classLayout2Frontend_Property_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_property_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Property)



@given(instance=classLayout2Frontend_Property_strategy)
def test_classlayout2frontend_property_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=classLayout2Frontend_Association_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_association_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Association)



@given(instance=classLayout2Frontend_Association_strategy)
def test_classlayout2frontend_association_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=classLayout2Frontend_Reference_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_reference_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Reference)

@given(instance=classLayout2Frontend_Composition_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_composition_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_Composition)

@given(instance=classLayout2Frontend_ContainerView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_containerview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_ContainerView)

@given(instance=classLayout2Frontend_PageView_strategy)
@settings(max_examples=50)
def test_classlayout2frontend_pageview_instantiation(instance):
    assert isinstance(instance, classLayout2Frontend_PageView)



@given(instance=classLayout2Frontend_PageView_strategy)
def test_classlayout2frontend_pageview_layoutType_setter(instance):
    original = instance.layoutType
    instance.layoutType = original
    assert instance.layoutType == original



@given(instance=classLayout2Frontend_PageView_strategy)
def test_classlayout2frontend_pageview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
