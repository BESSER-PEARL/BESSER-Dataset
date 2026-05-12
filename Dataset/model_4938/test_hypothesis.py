import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fml_SelectionItem,
    fml_PageElement,
    InputElement,
    fml_SelectField,
    fml_TextInput,
    fml_ListItem,
    DisplayElement,
    fml_List,
    fml_TextParagraph,
    fml_Heading,
    PageElement,
    fml_InputElement,
    fml_DisplayElement,
    fml_Page,
    fml_Form,
    TextInputType,
    SelectionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fml_selectionitem_is_not_abstract():
    assert not inspect.isabstract(fml_SelectionItem)


def test_fml_selectionitem_constructor_exists():
    assert callable(fml_SelectionItem.__init__)


def test_fml_selectionitem_constructor_args():
    sig = inspect.signature(fml_SelectionItem.__init__)
    params = list(sig.parameters.keys())
    assert "selected" in params, "Missing parameter 'selected'"
    assert "Text" in params, "Missing parameter 'Text'"
    assert "preselected" in params, "Missing parameter 'preselected'"

def test_fml_selectionitem_has_selected():
    assert hasattr(fml_SelectionItem, "selected")
    descriptor = None
    for klass in fml_SelectionItem.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_fml_selectionitem_has_Text():
    assert hasattr(fml_SelectionItem, "Text")
    descriptor = None
    for klass in fml_SelectionItem.__mro__:
        if "Text" in klass.__dict__:
            descriptor = klass.__dict__["Text"]
            break
    assert isinstance(descriptor, property)

def test_fml_selectionitem_has_preselected():
    assert hasattr(fml_SelectionItem, "preselected")
    descriptor = None
    for klass in fml_SelectionItem.__mro__:
        if "preselected" in klass.__dict__:
            descriptor = klass.__dict__["preselected"]
            break
    assert isinstance(descriptor, property)



def test_fml_pageelement_is_not_abstract():
    assert not inspect.isabstract(fml_PageElement)


def test_fml_pageelement_constructor_exists():
    assert callable(fml_PageElement.__init__)


def test_fml_pageelement_constructor_args():
    sig = inspect.signature(fml_PageElement.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_fml_pageelement_has_ID():
    assert hasattr(fml_PageElement, "ID")
    descriptor = None
    for klass in fml_PageElement.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_inputelement_is_not_abstract():
    assert not inspect.isabstract(InputElement)


def test_inputelement_constructor_exists():
    assert callable(InputElement.__init__)


def test_inputelement_constructor_args():
    sig = inspect.signature(InputElement.__init__)
    params = list(sig.parameters.keys())



def test_fml_selectfield_is_not_abstract():
    assert not inspect.isabstract(fml_SelectField)


def test_fml_selectfield_constructor_exists():
    assert callable(fml_SelectField.__init__)


def test_fml_selectfield_constructor_args():
    sig = inspect.signature(fml_SelectField.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Label" in params, "Missing parameter 'Label'"

def test_fml_selectfield_has_Type():
    assert hasattr(fml_SelectField, "Type")
    descriptor = None
    for klass in fml_SelectField.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_fml_selectfield_has_Label():
    assert hasattr(fml_SelectField, "Label")
    descriptor = None
    for klass in fml_SelectField.__mro__:
        if "Label" in klass.__dict__:
            descriptor = klass.__dict__["Label"]
            break
    assert isinstance(descriptor, property)



def test_fml_textinput_is_not_abstract():
    assert not inspect.isabstract(fml_TextInput)


def test_fml_textinput_constructor_exists():
    assert callable(fml_TextInput.__init__)


def test_fml_textinput_constructor_args():
    sig = inspect.signature(fml_TextInput.__init__)
    params = list(sig.parameters.keys())
    assert "Label" in params, "Missing parameter 'Label'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Content" in params, "Missing parameter 'Content'"

def test_fml_textinput_has_Label():
    assert hasattr(fml_TextInput, "Label")
    descriptor = None
    for klass in fml_TextInput.__mro__:
        if "Label" in klass.__dict__:
            descriptor = klass.__dict__["Label"]
            break
    assert isinstance(descriptor, property)

def test_fml_textinput_has_Type():
    assert hasattr(fml_TextInput, "Type")
    descriptor = None
    for klass in fml_TextInput.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_fml_textinput_has_Content():
    assert hasattr(fml_TextInput, "Content")
    descriptor = None
    for klass in fml_TextInput.__mro__:
        if "Content" in klass.__dict__:
            descriptor = klass.__dict__["Content"]
            break
    assert isinstance(descriptor, property)



def test_fml_listitem_is_not_abstract():
    assert not inspect.isabstract(fml_ListItem)


def test_fml_listitem_constructor_exists():
    assert callable(fml_ListItem.__init__)


def test_fml_listitem_constructor_args():
    sig = inspect.signature(fml_ListItem.__init__)
    params = list(sig.parameters.keys())
    assert "Text" in params, "Missing parameter 'Text'"

def test_fml_listitem_has_Text():
    assert hasattr(fml_ListItem, "Text")
    descriptor = None
    for klass in fml_ListItem.__mro__:
        if "Text" in klass.__dict__:
            descriptor = klass.__dict__["Text"]
            break
    assert isinstance(descriptor, property)



def test_displayelement_is_not_abstract():
    assert not inspect.isabstract(DisplayElement)


def test_displayelement_constructor_exists():
    assert callable(DisplayElement.__init__)


def test_displayelement_constructor_args():
    sig = inspect.signature(DisplayElement.__init__)
    params = list(sig.parameters.keys())



def test_fml_list_is_not_abstract():
    assert not inspect.isabstract(fml_List)


def test_fml_list_constructor_exists():
    assert callable(fml_List.__init__)


def test_fml_list_constructor_args():
    sig = inspect.signature(fml_List.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_fml_list_has_isOrdered():
    assert hasattr(fml_List, "isOrdered")
    descriptor = None
    for klass in fml_List.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_fml_textparagraph_is_not_abstract():
    assert not inspect.isabstract(fml_TextParagraph)


def test_fml_textparagraph_constructor_exists():
    assert callable(fml_TextParagraph.__init__)


def test_fml_textparagraph_constructor_args():
    sig = inspect.signature(fml_TextParagraph.__init__)
    params = list(sig.parameters.keys())
    assert "Text" in params, "Missing parameter 'Text'"

def test_fml_textparagraph_has_Text():
    assert hasattr(fml_TextParagraph, "Text")
    descriptor = None
    for klass in fml_TextParagraph.__mro__:
        if "Text" in klass.__dict__:
            descriptor = klass.__dict__["Text"]
            break
    assert isinstance(descriptor, property)



def test_fml_heading_is_not_abstract():
    assert not inspect.isabstract(fml_Heading)


def test_fml_heading_constructor_exists():
    assert callable(fml_Heading.__init__)


def test_fml_heading_constructor_args():
    sig = inspect.signature(fml_Heading.__init__)
    params = list(sig.parameters.keys())
    assert "Level" in params, "Missing parameter 'Level'"
    assert "Text" in params, "Missing parameter 'Text'"

def test_fml_heading_has_Level():
    assert hasattr(fml_Heading, "Level")
    descriptor = None
    for klass in fml_Heading.__mro__:
        if "Level" in klass.__dict__:
            descriptor = klass.__dict__["Level"]
            break
    assert isinstance(descriptor, property)

def test_fml_heading_has_Text():
    assert hasattr(fml_Heading, "Text")
    descriptor = None
    for klass in fml_Heading.__mro__:
        if "Text" in klass.__dict__:
            descriptor = klass.__dict__["Text"]
            break
    assert isinstance(descriptor, property)



def test_pageelement_is_not_abstract():
    assert not inspect.isabstract(PageElement)


def test_pageelement_constructor_exists():
    assert callable(PageElement.__init__)


def test_pageelement_constructor_args():
    sig = inspect.signature(PageElement.__init__)
    params = list(sig.parameters.keys())



def test_fml_inputelement_is_not_abstract():
    assert not inspect.isabstract(fml_InputElement)


def test_fml_inputelement_constructor_exists():
    assert callable(fml_InputElement.__init__)


def test_fml_inputelement_constructor_args():
    sig = inspect.signature(fml_InputElement.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_fml_inputelement_has_isMandatory():
    assert hasattr(fml_InputElement, "isMandatory")
    descriptor = None
    for klass in fml_InputElement.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_fml_displayelement_is_not_abstract():
    assert not inspect.isabstract(fml_DisplayElement)


def test_fml_displayelement_constructor_exists():
    assert callable(fml_DisplayElement.__init__)


def test_fml_displayelement_constructor_args():
    sig = inspect.signature(fml_DisplayElement.__init__)
    params = list(sig.parameters.keys())



def test_fml_page_is_not_abstract():
    assert not inspect.isabstract(fml_Page)


def test_fml_page_constructor_exists():
    assert callable(fml_Page.__init__)


def test_fml_page_constructor_args():
    sig = inspect.signature(fml_Page.__init__)
    params = list(sig.parameters.keys())
    assert "Title" in params, "Missing parameter 'Title'"
    assert "isWelcome" in params, "Missing parameter 'isWelcome'"

def test_fml_page_has_Title():
    assert hasattr(fml_Page, "Title")
    descriptor = None
    for klass in fml_Page.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)

def test_fml_page_has_isWelcome():
    assert hasattr(fml_Page, "isWelcome")
    descriptor = None
    for klass in fml_Page.__mro__:
        if "isWelcome" in klass.__dict__:
            descriptor = klass.__dict__["isWelcome"]
            break
    assert isinstance(descriptor, property)



def test_fml_form_is_not_abstract():
    assert not inspect.isabstract(fml_Form)


def test_fml_form_constructor_exists():
    assert callable(fml_Form.__init__)


def test_fml_form_constructor_args():
    sig = inspect.signature(fml_Form.__init__)
    params = list(sig.parameters.keys())

def test_textinputtype_exists():
    # Check that the Enumeration exists
    assert TextInputType is not None

def test_textinputtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextInputType]
    expected_literals = [
        "ENCRYPTED_TEXTFIELD",
        "TEXTFIELD",
        "TEXTAREA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextInputType"

def test_selectiontype_exists():
    # Check that the Enumeration exists
    assert SelectionType is not None

def test_selectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectionType]
    expected_literals = [
        "CHECKBOX",
        "RADIO",
        "COMBOBOX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectionType"


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
fml_SelectionItem_strategy = st.builds(
    fml_SelectionItem,
    selected=
        st.booleans(),
    Text=
        safe_text,
    preselected=
        st.booleans()
)
fml_PageElement_strategy = st.builds(
    fml_PageElement,
    ID=
        safe_text
)
InputElement_strategy = st.builds(
    InputElement,
)
fml_SelectField_strategy = st.builds(
    fml_SelectField,
    Type=
        safe_text,
    Label=
        safe_text
)
fml_TextInput_strategy = st.builds(
    fml_TextInput,
    Label=
        safe_text,
    Type=
        safe_text,
    Content=
        safe_text
)
fml_ListItem_strategy = st.builds(
    fml_ListItem,
    Text=
        safe_text
)
DisplayElement_strategy = st.builds(
    DisplayElement,
)
fml_List_strategy = st.builds(
    fml_List,
    isOrdered=
        st.booleans()
)
fml_TextParagraph_strategy = st.builds(
    fml_TextParagraph,
    Text=
        safe_text
)
fml_Heading_strategy = st.builds(
    fml_Heading,
    Level=
        safe_text,
    Text=
        safe_text
)
PageElement_strategy = st.builds(
    PageElement,
)
fml_InputElement_strategy = st.builds(
    fml_InputElement,
    isMandatory=
        st.booleans()
)
fml_DisplayElement_strategy = st.builds(
    fml_DisplayElement,
)
fml_Page_strategy = st.builds(
    fml_Page,
    Title=
        safe_text,
    isWelcome=
        st.booleans()
)
fml_Form_strategy = st.builds(
    fml_Form,
)

@given(instance=fml_SelectionItem_strategy)
@settings(max_examples=50)
def test_fml_selectionitem_instantiation(instance):
    assert isinstance(instance, fml_SelectionItem)



@given(instance=fml_SelectionItem_strategy)
def test_fml_selectionitem_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original



@given(instance=fml_SelectionItem_strategy)
def test_fml_selectionitem_Text_setter(instance):
    original = instance.Text
    instance.Text = original
    assert instance.Text == original



@given(instance=fml_SelectionItem_strategy)
def test_fml_selectionitem_preselected_setter(instance):
    original = instance.preselected
    instance.preselected = original
    assert instance.preselected == original

@given(instance=fml_PageElement_strategy)
@settings(max_examples=50)
def test_fml_pageelement_instantiation(instance):
    assert isinstance(instance, fml_PageElement)



@given(instance=fml_PageElement_strategy)
def test_fml_pageelement_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=InputElement_strategy)
@settings(max_examples=50)
def test_inputelement_instantiation(instance):
    assert isinstance(instance, InputElement)

@given(instance=fml_SelectField_strategy)
@settings(max_examples=50)
def test_fml_selectfield_instantiation(instance):
    assert isinstance(instance, fml_SelectField)



@given(instance=fml_SelectField_strategy)
def test_fml_selectfield_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=fml_SelectField_strategy)
def test_fml_selectfield_Label_setter(instance):
    original = instance.Label
    instance.Label = original
    assert instance.Label == original

@given(instance=fml_TextInput_strategy)
@settings(max_examples=50)
def test_fml_textinput_instantiation(instance):
    assert isinstance(instance, fml_TextInput)



@given(instance=fml_TextInput_strategy)
def test_fml_textinput_Label_setter(instance):
    original = instance.Label
    instance.Label = original
    assert instance.Label == original



@given(instance=fml_TextInput_strategy)
def test_fml_textinput_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=fml_TextInput_strategy)
def test_fml_textinput_Content_setter(instance):
    original = instance.Content
    instance.Content = original
    assert instance.Content == original

@given(instance=fml_ListItem_strategy)
@settings(max_examples=50)
def test_fml_listitem_instantiation(instance):
    assert isinstance(instance, fml_ListItem)



@given(instance=fml_ListItem_strategy)
def test_fml_listitem_Text_setter(instance):
    original = instance.Text
    instance.Text = original
    assert instance.Text == original

@given(instance=DisplayElement_strategy)
@settings(max_examples=50)
def test_displayelement_instantiation(instance):
    assert isinstance(instance, DisplayElement)

@given(instance=fml_List_strategy)
@settings(max_examples=50)
def test_fml_list_instantiation(instance):
    assert isinstance(instance, fml_List)



@given(instance=fml_List_strategy)
def test_fml_list_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=fml_TextParagraph_strategy)
@settings(max_examples=50)
def test_fml_textparagraph_instantiation(instance):
    assert isinstance(instance, fml_TextParagraph)



@given(instance=fml_TextParagraph_strategy)
def test_fml_textparagraph_Text_setter(instance):
    original = instance.Text
    instance.Text = original
    assert instance.Text == original

@given(instance=fml_Heading_strategy)
@settings(max_examples=50)
def test_fml_heading_instantiation(instance):
    assert isinstance(instance, fml_Heading)



@given(instance=fml_Heading_strategy)
def test_fml_heading_Level_setter(instance):
    original = instance.Level
    instance.Level = original
    assert instance.Level == original



@given(instance=fml_Heading_strategy)
def test_fml_heading_Text_setter(instance):
    original = instance.Text
    instance.Text = original
    assert instance.Text == original

@given(instance=PageElement_strategy)
@settings(max_examples=50)
def test_pageelement_instantiation(instance):
    assert isinstance(instance, PageElement)

@given(instance=fml_InputElement_strategy)
@settings(max_examples=50)
def test_fml_inputelement_instantiation(instance):
    assert isinstance(instance, fml_InputElement)



@given(instance=fml_InputElement_strategy)
def test_fml_inputelement_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=fml_DisplayElement_strategy)
@settings(max_examples=50)
def test_fml_displayelement_instantiation(instance):
    assert isinstance(instance, fml_DisplayElement)

@given(instance=fml_Page_strategy)
@settings(max_examples=50)
def test_fml_page_instantiation(instance):
    assert isinstance(instance, fml_Page)



@given(instance=fml_Page_strategy)
def test_fml_page_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original



@given(instance=fml_Page_strategy)
def test_fml_page_isWelcome_setter(instance):
    original = instance.isWelcome
    instance.isWelcome = original
    assert instance.isWelcome == original

@given(instance=fml_Form_strategy)
@settings(max_examples=50)
def test_fml_form_instantiation(instance):
    assert isinstance(instance, fml_Form)
