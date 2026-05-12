import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Freemind_IconType,
    Freemind_HookType,
    Freemind_FontType,
    Freemind_TextType,
    Freemind_ParametersType,
    Freemind_NodeType,
    Freemind_MapType,
    Freemind_CloudType,
    Freemind_EdgeType,
    Freemind_EStringToStringMapEntry,
    Freemind_DocumentRoot,
    Freemind_ArrowlinkType,
    ITALICType,
    BOLDType,
    FOLDEDType,
    POSITIONType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_freemind_icontype_is_not_abstract():
    assert not inspect.isabstract(Freemind_IconType)


def test_freemind_icontype_constructor_exists():
    assert callable(Freemind_IconType.__init__)


def test_freemind_icontype_constructor_args():
    sig = inspect.signature(Freemind_IconType.__init__)
    params = list(sig.parameters.keys())
    assert "Builtin" in params, "Missing parameter 'Builtin'"

def test_freemind_icontype_has_Builtin():
    assert hasattr(Freemind_IconType, "Builtin")
    descriptor = None
    for klass in Freemind_IconType.__mro__:
        if "Builtin" in klass.__dict__:
            descriptor = klass.__dict__["Builtin"]
            break
    assert isinstance(descriptor, property)



def test_freemind_hooktype_is_not_abstract():
    assert not inspect.isabstract(Freemind_HookType)


def test_freemind_hooktype_constructor_exists():
    assert callable(Freemind_HookType.__init__)


def test_freemind_hooktype_constructor_args():
    sig = inspect.signature(Freemind_HookType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_freemind_hooktype_has_Name():
    assert hasattr(Freemind_HookType, "Name")
    descriptor = None
    for klass in Freemind_HookType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_freemind_fonttype_is_not_abstract():
    assert not inspect.isabstract(Freemind_FontType)


def test_freemind_fonttype_constructor_exists():
    assert callable(Freemind_FontType.__init__)


def test_freemind_fonttype_constructor_args():
    sig = inspect.signature(Freemind_FontType.__init__)
    params = list(sig.parameters.keys())
    assert "Bold" in params, "Missing parameter 'Bold'"
    assert "Size" in params, "Missing parameter 'Size'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Italic" in params, "Missing parameter 'Italic'"

def test_freemind_fonttype_has_Bold():
    assert hasattr(Freemind_FontType, "Bold")
    descriptor = None
    for klass in Freemind_FontType.__mro__:
        if "Bold" in klass.__dict__:
            descriptor = klass.__dict__["Bold"]
            break
    assert isinstance(descriptor, property)

def test_freemind_fonttype_has_Size():
    assert hasattr(Freemind_FontType, "Size")
    descriptor = None
    for klass in Freemind_FontType.__mro__:
        if "Size" in klass.__dict__:
            descriptor = klass.__dict__["Size"]
            break
    assert isinstance(descriptor, property)

def test_freemind_fonttype_has_Name():
    assert hasattr(Freemind_FontType, "Name")
    descriptor = None
    for klass in Freemind_FontType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_freemind_fonttype_has_Italic():
    assert hasattr(Freemind_FontType, "Italic")
    descriptor = None
    for klass in Freemind_FontType.__mro__:
        if "Italic" in klass.__dict__:
            descriptor = klass.__dict__["Italic"]
            break
    assert isinstance(descriptor, property)



def test_freemind_texttype_is_not_abstract():
    assert not inspect.isabstract(Freemind_TextType)


def test_freemind_texttype_constructor_exists():
    assert callable(Freemind_TextType.__init__)


def test_freemind_texttype_constructor_args():
    sig = inspect.signature(Freemind_TextType.__init__)
    params = list(sig.parameters.keys())



def test_freemind_parameterstype_is_not_abstract():
    assert not inspect.isabstract(Freemind_ParametersType)


def test_freemind_parameterstype_constructor_exists():
    assert callable(Freemind_ParametersType.__init__)


def test_freemind_parameterstype_constructor_args():
    sig = inspect.signature(Freemind_ParametersType.__init__)
    params = list(sig.parameters.keys())
    assert "RemindUserAt" in params, "Missing parameter 'RemindUserAt'"

def test_freemind_parameterstype_has_RemindUserAt():
    assert hasattr(Freemind_ParametersType, "RemindUserAt")
    descriptor = None
    for klass in Freemind_ParametersType.__mro__:
        if "RemindUserAt" in klass.__dict__:
            descriptor = klass.__dict__["RemindUserAt"]
            break
    assert isinstance(descriptor, property)



def test_freemind_nodetype_is_not_abstract():
    assert not inspect.isabstract(Freemind_NodeType)


def test_freemind_nodetype_constructor_exists():
    assert callable(Freemind_NodeType.__init__)


def test_freemind_nodetype_constructor_args():
    sig = inspect.signature(Freemind_NodeType.__init__)
    params = list(sig.parameters.keys())
    assert "EncryptedContent" in params, "Missing parameter 'EncryptedContent'"
    assert "Text" in params, "Missing parameter 'Text'"
    assert "Vgap" in params, "Missing parameter 'Vgap'"
    assert "group" in params, "Missing parameter 'group'"
    assert "Style" in params, "Missing parameter 'Style'"
    assert "BackgroundColor" in params, "Missing parameter 'BackgroundColor'"
    assert "Modified" in params, "Missing parameter 'Modified'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Link" in params, "Missing parameter 'Link'"
    assert "Folded" in params, "Missing parameter 'Folded'"
    assert "Created" in params, "Missing parameter 'Created'"
    assert "Color" in params, "Missing parameter 'Color'"
    assert "Position" in params, "Missing parameter 'Position'"
    assert "Vshift" in params, "Missing parameter 'Vshift'"
    assert "Hgap" in params, "Missing parameter 'Hgap'"

def test_freemind_nodetype_has_EncryptedContent():
    assert hasattr(Freemind_NodeType, "EncryptedContent")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "EncryptedContent" in klass.__dict__:
            descriptor = klass.__dict__["EncryptedContent"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Text():
    assert hasattr(Freemind_NodeType, "Text")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Text" in klass.__dict__:
            descriptor = klass.__dict__["Text"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Vgap():
    assert hasattr(Freemind_NodeType, "Vgap")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Vgap" in klass.__dict__:
            descriptor = klass.__dict__["Vgap"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_group():
    assert hasattr(Freemind_NodeType, "group")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Style():
    assert hasattr(Freemind_NodeType, "Style")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Style" in klass.__dict__:
            descriptor = klass.__dict__["Style"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_BackgroundColor():
    assert hasattr(Freemind_NodeType, "BackgroundColor")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "BackgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["BackgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Modified():
    assert hasattr(Freemind_NodeType, "Modified")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Modified" in klass.__dict__:
            descriptor = klass.__dict__["Modified"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Id():
    assert hasattr(Freemind_NodeType, "Id")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Link():
    assert hasattr(Freemind_NodeType, "Link")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Link" in klass.__dict__:
            descriptor = klass.__dict__["Link"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Folded():
    assert hasattr(Freemind_NodeType, "Folded")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Folded" in klass.__dict__:
            descriptor = klass.__dict__["Folded"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Created():
    assert hasattr(Freemind_NodeType, "Created")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Created" in klass.__dict__:
            descriptor = klass.__dict__["Created"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Color():
    assert hasattr(Freemind_NodeType, "Color")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Position():
    assert hasattr(Freemind_NodeType, "Position")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Position" in klass.__dict__:
            descriptor = klass.__dict__["Position"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Vshift():
    assert hasattr(Freemind_NodeType, "Vshift")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Vshift" in klass.__dict__:
            descriptor = klass.__dict__["Vshift"]
            break
    assert isinstance(descriptor, property)

def test_freemind_nodetype_has_Hgap():
    assert hasattr(Freemind_NodeType, "Hgap")
    descriptor = None
    for klass in Freemind_NodeType.__mro__:
        if "Hgap" in klass.__dict__:
            descriptor = klass.__dict__["Hgap"]
            break
    assert isinstance(descriptor, property)



def test_freemind_maptype_is_not_abstract():
    assert not inspect.isabstract(Freemind_MapType)


def test_freemind_maptype_constructor_exists():
    assert callable(Freemind_MapType.__init__)


def test_freemind_maptype_constructor_args():
    sig = inspect.signature(Freemind_MapType.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_freemind_maptype_has_version():
    assert hasattr(Freemind_MapType, "version")
    descriptor = None
    for klass in Freemind_MapType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_freemind_cloudtype_is_not_abstract():
    assert not inspect.isabstract(Freemind_CloudType)


def test_freemind_cloudtype_constructor_exists():
    assert callable(Freemind_CloudType.__init__)


def test_freemind_cloudtype_constructor_args():
    sig = inspect.signature(Freemind_CloudType.__init__)
    params = list(sig.parameters.keys())
    assert "Color" in params, "Missing parameter 'Color'"

def test_freemind_cloudtype_has_Color():
    assert hasattr(Freemind_CloudType, "Color")
    descriptor = None
    for klass in Freemind_CloudType.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)



def test_freemind_edgetype_is_not_abstract():
    assert not inspect.isabstract(Freemind_EdgeType)


def test_freemind_edgetype_constructor_exists():
    assert callable(Freemind_EdgeType.__init__)


def test_freemind_edgetype_constructor_args():
    sig = inspect.signature(Freemind_EdgeType.__init__)
    params = list(sig.parameters.keys())
    assert "Color" in params, "Missing parameter 'Color'"
    assert "Width" in params, "Missing parameter 'Width'"
    assert "Style" in params, "Missing parameter 'Style'"

def test_freemind_edgetype_has_Color():
    assert hasattr(Freemind_EdgeType, "Color")
    descriptor = None
    for klass in Freemind_EdgeType.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)

def test_freemind_edgetype_has_Width():
    assert hasattr(Freemind_EdgeType, "Width")
    descriptor = None
    for klass in Freemind_EdgeType.__mro__:
        if "Width" in klass.__dict__:
            descriptor = klass.__dict__["Width"]
            break
    assert isinstance(descriptor, property)

def test_freemind_edgetype_has_Style():
    assert hasattr(Freemind_EdgeType, "Style")
    descriptor = None
    for klass in Freemind_EdgeType.__mro__:
        if "Style" in klass.__dict__:
            descriptor = klass.__dict__["Style"]
            break
    assert isinstance(descriptor, property)



def test_freemind_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(Freemind_EStringToStringMapEntry)


def test_freemind_estringtostringmapentry_constructor_exists():
    assert callable(Freemind_EStringToStringMapEntry.__init__)


def test_freemind_estringtostringmapentry_constructor_args():
    sig = inspect.signature(Freemind_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_freemind_documentroot_is_not_abstract():
    assert not inspect.isabstract(Freemind_DocumentRoot)


def test_freemind_documentroot_constructor_exists():
    assert callable(Freemind_DocumentRoot.__init__)


def test_freemind_documentroot_constructor_args():
    sig = inspect.signature(Freemind_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_freemind_documentroot_has_mixed():
    assert hasattr(Freemind_DocumentRoot, "mixed")
    descriptor = None
    for klass in Freemind_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_freemind_arrowlinktype_is_not_abstract():
    assert not inspect.isabstract(Freemind_ArrowlinkType)


def test_freemind_arrowlinktype_constructor_exists():
    assert callable(Freemind_ArrowlinkType.__init__)


def test_freemind_arrowlinktype_constructor_args():
    sig = inspect.signature(Freemind_ArrowlinkType.__init__)
    params = list(sig.parameters.keys())
    assert "EndInclination" in params, "Missing parameter 'EndInclination'"
    assert "EndArrow" in params, "Missing parameter 'EndArrow'"
    assert "StartInclination" in params, "Missing parameter 'StartInclination'"
    assert "StartArrow" in params, "Missing parameter 'StartArrow'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Color" in params, "Missing parameter 'Color'"
    assert "Destination" in params, "Missing parameter 'Destination'"

def test_freemind_arrowlinktype_has_EndInclination():
    assert hasattr(Freemind_ArrowlinkType, "EndInclination")
    descriptor = None
    for klass in Freemind_ArrowlinkType.__mro__:
        if "EndInclination" in klass.__dict__:
            descriptor = klass.__dict__["EndInclination"]
            break
    assert isinstance(descriptor, property)

def test_freemind_arrowlinktype_has_EndArrow():
    assert hasattr(Freemind_ArrowlinkType, "EndArrow")
    descriptor = None
    for klass in Freemind_ArrowlinkType.__mro__:
        if "EndArrow" in klass.__dict__:
            descriptor = klass.__dict__["EndArrow"]
            break
    assert isinstance(descriptor, property)

def test_freemind_arrowlinktype_has_StartInclination():
    assert hasattr(Freemind_ArrowlinkType, "StartInclination")
    descriptor = None
    for klass in Freemind_ArrowlinkType.__mro__:
        if "StartInclination" in klass.__dict__:
            descriptor = klass.__dict__["StartInclination"]
            break
    assert isinstance(descriptor, property)

def test_freemind_arrowlinktype_has_StartArrow():
    assert hasattr(Freemind_ArrowlinkType, "StartArrow")
    descriptor = None
    for klass in Freemind_ArrowlinkType.__mro__:
        if "StartArrow" in klass.__dict__:
            descriptor = klass.__dict__["StartArrow"]
            break
    assert isinstance(descriptor, property)

def test_freemind_arrowlinktype_has_Id():
    assert hasattr(Freemind_ArrowlinkType, "Id")
    descriptor = None
    for klass in Freemind_ArrowlinkType.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_freemind_arrowlinktype_has_Color():
    assert hasattr(Freemind_ArrowlinkType, "Color")
    descriptor = None
    for klass in Freemind_ArrowlinkType.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)

def test_freemind_arrowlinktype_has_Destination():
    assert hasattr(Freemind_ArrowlinkType, "Destination")
    descriptor = None
    for klass in Freemind_ArrowlinkType.__mro__:
        if "Destination" in klass.__dict__:
            descriptor = klass.__dict__["Destination"]
            break
    assert isinstance(descriptor, property)

def test_italictype_exists():
    # Check that the Enumeration exists
    assert ITALICType is not None

def test_italictype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ITALICType]
    expected_literals = [
        "true",
        "false",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ITALICType"

def test_boldtype_exists():
    # Check that the Enumeration exists
    assert BOLDType is not None

def test_boldtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BOLDType]
    expected_literals = [
        "true",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BOLDType"

def test_foldedtype_exists():
    # Check that the Enumeration exists
    assert FOLDEDType is not None

def test_foldedtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FOLDEDType]
    expected_literals = [
        "false",
        "true",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FOLDEDType"

def test_positiontype_exists():
    # Check that the Enumeration exists
    assert POSITIONType is not None

def test_positiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in POSITIONType]
    expected_literals = [
        "left",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in POSITIONType"


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
Freemind_IconType_strategy = st.builds(
    Freemind_IconType,
    Builtin=
        safe_text
)
Freemind_HookType_strategy = st.builds(
    Freemind_HookType,
    Name=
        safe_text
)
Freemind_FontType_strategy = st.builds(
    Freemind_FontType,
    Bold=
        safe_text,
    Size=
        safe_text,
    Name=
        safe_text,
    Italic=
        safe_text
)
Freemind_TextType_strategy = st.builds(
    Freemind_TextType,
)
Freemind_ParametersType_strategy = st.builds(
    Freemind_ParametersType,
    RemindUserAt=
        safe_text
)
Freemind_NodeType_strategy = st.builds(
    Freemind_NodeType,
    EncryptedContent=
        safe_text,
    Text=
        safe_text,
    Vgap=
        safe_text,
    group=
        safe_text,
    Style=
        safe_text,
    BackgroundColor=
        safe_text,
    Modified=
        safe_text,
    Id=
        safe_text,
    Link=
        safe_text,
    Folded=
        safe_text,
    Created=
        safe_text,
    Color=
        safe_text,
    Position=
        safe_text,
    Vshift=
        safe_text,
    Hgap=
        safe_text
)
Freemind_MapType_strategy = st.builds(
    Freemind_MapType,
    version=
        safe_text
)
Freemind_CloudType_strategy = st.builds(
    Freemind_CloudType,
    Color=
        safe_text
)
Freemind_EdgeType_strategy = st.builds(
    Freemind_EdgeType,
    Color=
        safe_text,
    Width=
        safe_text,
    Style=
        safe_text
)
Freemind_EStringToStringMapEntry_strategy = st.builds(
    Freemind_EStringToStringMapEntry,
)
Freemind_DocumentRoot_strategy = st.builds(
    Freemind_DocumentRoot,
    mixed=
        safe_text
)
Freemind_ArrowlinkType_strategy = st.builds(
    Freemind_ArrowlinkType,
    EndInclination=
        safe_text,
    EndArrow=
        safe_text,
    StartInclination=
        safe_text,
    StartArrow=
        safe_text,
    Id=
        safe_text,
    Color=
        safe_text,
    Destination=
        safe_text
)

@given(instance=Freemind_IconType_strategy)
@settings(max_examples=50)
def test_freemind_icontype_instantiation(instance):
    assert isinstance(instance, Freemind_IconType)



@given(instance=Freemind_IconType_strategy)
def test_freemind_icontype_Builtin_setter(instance):
    original = instance.Builtin
    instance.Builtin = original
    assert instance.Builtin == original

@given(instance=Freemind_HookType_strategy)
@settings(max_examples=50)
def test_freemind_hooktype_instantiation(instance):
    assert isinstance(instance, Freemind_HookType)



@given(instance=Freemind_HookType_strategy)
def test_freemind_hooktype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Freemind_FontType_strategy)
@settings(max_examples=50)
def test_freemind_fonttype_instantiation(instance):
    assert isinstance(instance, Freemind_FontType)



@given(instance=Freemind_FontType_strategy)
def test_freemind_fonttype_Bold_setter(instance):
    original = instance.Bold
    instance.Bold = original
    assert instance.Bold == original



@given(instance=Freemind_FontType_strategy)
def test_freemind_fonttype_Size_setter(instance):
    original = instance.Size
    instance.Size = original
    assert instance.Size == original



@given(instance=Freemind_FontType_strategy)
def test_freemind_fonttype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Freemind_FontType_strategy)
def test_freemind_fonttype_Italic_setter(instance):
    original = instance.Italic
    instance.Italic = original
    assert instance.Italic == original

@given(instance=Freemind_TextType_strategy)
@settings(max_examples=50)
def test_freemind_texttype_instantiation(instance):
    assert isinstance(instance, Freemind_TextType)

@given(instance=Freemind_ParametersType_strategy)
@settings(max_examples=50)
def test_freemind_parameterstype_instantiation(instance):
    assert isinstance(instance, Freemind_ParametersType)



@given(instance=Freemind_ParametersType_strategy)
def test_freemind_parameterstype_RemindUserAt_setter(instance):
    original = instance.RemindUserAt
    instance.RemindUserAt = original
    assert instance.RemindUserAt == original

@given(instance=Freemind_NodeType_strategy)
@settings(max_examples=50)
def test_freemind_nodetype_instantiation(instance):
    assert isinstance(instance, Freemind_NodeType)



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_EncryptedContent_setter(instance):
    original = instance.EncryptedContent
    instance.EncryptedContent = original
    assert instance.EncryptedContent == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Text_setter(instance):
    original = instance.Text
    instance.Text = original
    assert instance.Text == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Vgap_setter(instance):
    original = instance.Vgap
    instance.Vgap = original
    assert instance.Vgap == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Style_setter(instance):
    original = instance.Style
    instance.Style = original
    assert instance.Style == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_BackgroundColor_setter(instance):
    original = instance.BackgroundColor
    instance.BackgroundColor = original
    assert instance.BackgroundColor == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Modified_setter(instance):
    original = instance.Modified
    instance.Modified = original
    assert instance.Modified == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Link_setter(instance):
    original = instance.Link
    instance.Link = original
    assert instance.Link == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Folded_setter(instance):
    original = instance.Folded
    instance.Folded = original
    assert instance.Folded == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Created_setter(instance):
    original = instance.Created
    instance.Created = original
    assert instance.Created == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Position_setter(instance):
    original = instance.Position
    instance.Position = original
    assert instance.Position == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Vshift_setter(instance):
    original = instance.Vshift
    instance.Vshift = original
    assert instance.Vshift == original



@given(instance=Freemind_NodeType_strategy)
def test_freemind_nodetype_Hgap_setter(instance):
    original = instance.Hgap
    instance.Hgap = original
    assert instance.Hgap == original

@given(instance=Freemind_MapType_strategy)
@settings(max_examples=50)
def test_freemind_maptype_instantiation(instance):
    assert isinstance(instance, Freemind_MapType)



@given(instance=Freemind_MapType_strategy)
def test_freemind_maptype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Freemind_CloudType_strategy)
@settings(max_examples=50)
def test_freemind_cloudtype_instantiation(instance):
    assert isinstance(instance, Freemind_CloudType)



@given(instance=Freemind_CloudType_strategy)
def test_freemind_cloudtype_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original

@given(instance=Freemind_EdgeType_strategy)
@settings(max_examples=50)
def test_freemind_edgetype_instantiation(instance):
    assert isinstance(instance, Freemind_EdgeType)



@given(instance=Freemind_EdgeType_strategy)
def test_freemind_edgetype_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original



@given(instance=Freemind_EdgeType_strategy)
def test_freemind_edgetype_Width_setter(instance):
    original = instance.Width
    instance.Width = original
    assert instance.Width == original



@given(instance=Freemind_EdgeType_strategy)
def test_freemind_edgetype_Style_setter(instance):
    original = instance.Style
    instance.Style = original
    assert instance.Style == original

@given(instance=Freemind_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_freemind_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, Freemind_EStringToStringMapEntry)

@given(instance=Freemind_DocumentRoot_strategy)
@settings(max_examples=50)
def test_freemind_documentroot_instantiation(instance):
    assert isinstance(instance, Freemind_DocumentRoot)



@given(instance=Freemind_DocumentRoot_strategy)
def test_freemind_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Freemind_ArrowlinkType_strategy)
@settings(max_examples=50)
def test_freemind_arrowlinktype_instantiation(instance):
    assert isinstance(instance, Freemind_ArrowlinkType)



@given(instance=Freemind_ArrowlinkType_strategy)
def test_freemind_arrowlinktype_EndInclination_setter(instance):
    original = instance.EndInclination
    instance.EndInclination = original
    assert instance.EndInclination == original



@given(instance=Freemind_ArrowlinkType_strategy)
def test_freemind_arrowlinktype_EndArrow_setter(instance):
    original = instance.EndArrow
    instance.EndArrow = original
    assert instance.EndArrow == original



@given(instance=Freemind_ArrowlinkType_strategy)
def test_freemind_arrowlinktype_StartInclination_setter(instance):
    original = instance.StartInclination
    instance.StartInclination = original
    assert instance.StartInclination == original



@given(instance=Freemind_ArrowlinkType_strategy)
def test_freemind_arrowlinktype_StartArrow_setter(instance):
    original = instance.StartArrow
    instance.StartArrow = original
    assert instance.StartArrow == original



@given(instance=Freemind_ArrowlinkType_strategy)
def test_freemind_arrowlinktype_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Freemind_ArrowlinkType_strategy)
def test_freemind_arrowlinktype_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original



@given(instance=Freemind_ArrowlinkType_strategy)
def test_freemind_arrowlinktype_Destination_setter(instance):
    original = instance.Destination
    instance.Destination = original
    assert instance.Destination == original
