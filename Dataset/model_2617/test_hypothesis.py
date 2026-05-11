import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Freemind::IconType,
    Freemind::HookType,
    Freemind::FontType,
    Freemind::TextType,
    Freemind::ParametersType,
    Freemind::NodeType,
    Freemind::MapType,
    Freemind::CloudType,
    Freemind::EdgeType,
    Freemind::EStringToStringMapEntry,
    Freemind::DocumentRoot,
    Freemind::ArrowlinkType,
    ITALICType,
    BOLDType,
    FOLDEDType,
    POSITIONType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_freemind::icontype_is_not_abstract():
    assert not inspect.isabstract(Freemind::IconType)


def test_freemind::icontype_constructor_exists():
    assert callable(Freemind::IconType.__init__)


def test_freemind::icontype_constructor_args():
    sig = inspect.signature(Freemind::IconType.__init__)
    params = list(sig.parameters.keys())
    assert "Builtin" in params, "Missing parameter 'Builtin'"

def test_freemind::icontype_has_Builtin():
    assert hasattr(Freemind::IconType, "Builtin")
    descriptor = None
    for klass in Freemind::IconType.__mro__:
        if "Builtin" in klass.__dict__:
            descriptor = klass.__dict__["Builtin"]
            break
    assert isinstance(descriptor, property)



def test_freemind::hooktype_is_not_abstract():
    assert not inspect.isabstract(Freemind::HookType)


def test_freemind::hooktype_constructor_exists():
    assert callable(Freemind::HookType.__init__)


def test_freemind::hooktype_constructor_args():
    sig = inspect.signature(Freemind::HookType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_freemind::hooktype_has_Name():
    assert hasattr(Freemind::HookType, "Name")
    descriptor = None
    for klass in Freemind::HookType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_freemind::fonttype_is_not_abstract():
    assert not inspect.isabstract(Freemind::FontType)


def test_freemind::fonttype_constructor_exists():
    assert callable(Freemind::FontType.__init__)


def test_freemind::fonttype_constructor_args():
    sig = inspect.signature(Freemind::FontType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Size" in params, "Missing parameter 'Size'"
    assert "Italic" in params, "Missing parameter 'Italic'"
    assert "Bold" in params, "Missing parameter 'Bold'"

def test_freemind::fonttype_has_Name():
    assert hasattr(Freemind::FontType, "Name")
    descriptor = None
    for klass in Freemind::FontType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_freemind::fonttype_has_Size():
    assert hasattr(Freemind::FontType, "Size")
    descriptor = None
    for klass in Freemind::FontType.__mro__:
        if "Size" in klass.__dict__:
            descriptor = klass.__dict__["Size"]
            break
    assert isinstance(descriptor, property)

def test_freemind::fonttype_has_Italic():
    assert hasattr(Freemind::FontType, "Italic")
    descriptor = None
    for klass in Freemind::FontType.__mro__:
        if "Italic" in klass.__dict__:
            descriptor = klass.__dict__["Italic"]
            break
    assert isinstance(descriptor, property)

def test_freemind::fonttype_has_Bold():
    assert hasattr(Freemind::FontType, "Bold")
    descriptor = None
    for klass in Freemind::FontType.__mro__:
        if "Bold" in klass.__dict__:
            descriptor = klass.__dict__["Bold"]
            break
    assert isinstance(descriptor, property)



def test_freemind::texttype_is_not_abstract():
    assert not inspect.isabstract(Freemind::TextType)


def test_freemind::texttype_constructor_exists():
    assert callable(Freemind::TextType.__init__)


def test_freemind::texttype_constructor_args():
    sig = inspect.signature(Freemind::TextType.__init__)
    params = list(sig.parameters.keys())



def test_freemind::parameterstype_is_not_abstract():
    assert not inspect.isabstract(Freemind::ParametersType)


def test_freemind::parameterstype_constructor_exists():
    assert callable(Freemind::ParametersType.__init__)


def test_freemind::parameterstype_constructor_args():
    sig = inspect.signature(Freemind::ParametersType.__init__)
    params = list(sig.parameters.keys())
    assert "RemindUserAt" in params, "Missing parameter 'RemindUserAt'"

def test_freemind::parameterstype_has_RemindUserAt():
    assert hasattr(Freemind::ParametersType, "RemindUserAt")
    descriptor = None
    for klass in Freemind::ParametersType.__mro__:
        if "RemindUserAt" in klass.__dict__:
            descriptor = klass.__dict__["RemindUserAt"]
            break
    assert isinstance(descriptor, property)



def test_freemind::nodetype_is_not_abstract():
    assert not inspect.isabstract(Freemind::NodeType)


def test_freemind::nodetype_constructor_exists():
    assert callable(Freemind::NodeType.__init__)


def test_freemind::nodetype_constructor_args():
    sig = inspect.signature(Freemind::NodeType.__init__)
    params = list(sig.parameters.keys())
    assert "Text" in params, "Missing parameter 'Text'"
    assert "Folded" in params, "Missing parameter 'Folded'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Vshift" in params, "Missing parameter 'Vshift'"
    assert "Vgap" in params, "Missing parameter 'Vgap'"
    assert "BackgroundColor" in params, "Missing parameter 'BackgroundColor'"
    assert "group" in params, "Missing parameter 'group'"
    assert "Color" in params, "Missing parameter 'Color'"
    assert "Style" in params, "Missing parameter 'Style'"
    assert "Hgap" in params, "Missing parameter 'Hgap'"
    assert "Modified" in params, "Missing parameter 'Modified'"
    assert "EncryptedContent" in params, "Missing parameter 'EncryptedContent'"
    assert "Created" in params, "Missing parameter 'Created'"
    assert "Position" in params, "Missing parameter 'Position'"
    assert "Link" in params, "Missing parameter 'Link'"

def test_freemind::nodetype_has_Text():
    assert hasattr(Freemind::NodeType, "Text")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Text" in klass.__dict__:
            descriptor = klass.__dict__["Text"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Folded():
    assert hasattr(Freemind::NodeType, "Folded")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Folded" in klass.__dict__:
            descriptor = klass.__dict__["Folded"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Id():
    assert hasattr(Freemind::NodeType, "Id")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Vshift():
    assert hasattr(Freemind::NodeType, "Vshift")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Vshift" in klass.__dict__:
            descriptor = klass.__dict__["Vshift"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Vgap():
    assert hasattr(Freemind::NodeType, "Vgap")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Vgap" in klass.__dict__:
            descriptor = klass.__dict__["Vgap"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_BackgroundColor():
    assert hasattr(Freemind::NodeType, "BackgroundColor")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "BackgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["BackgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_group():
    assert hasattr(Freemind::NodeType, "group")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Color():
    assert hasattr(Freemind::NodeType, "Color")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Style():
    assert hasattr(Freemind::NodeType, "Style")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Style" in klass.__dict__:
            descriptor = klass.__dict__["Style"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Hgap():
    assert hasattr(Freemind::NodeType, "Hgap")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Hgap" in klass.__dict__:
            descriptor = klass.__dict__["Hgap"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Modified():
    assert hasattr(Freemind::NodeType, "Modified")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Modified" in klass.__dict__:
            descriptor = klass.__dict__["Modified"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_EncryptedContent():
    assert hasattr(Freemind::NodeType, "EncryptedContent")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "EncryptedContent" in klass.__dict__:
            descriptor = klass.__dict__["EncryptedContent"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Created():
    assert hasattr(Freemind::NodeType, "Created")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Created" in klass.__dict__:
            descriptor = klass.__dict__["Created"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Position():
    assert hasattr(Freemind::NodeType, "Position")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Position" in klass.__dict__:
            descriptor = klass.__dict__["Position"]
            break
    assert isinstance(descriptor, property)

def test_freemind::nodetype_has_Link():
    assert hasattr(Freemind::NodeType, "Link")
    descriptor = None
    for klass in Freemind::NodeType.__mro__:
        if "Link" in klass.__dict__:
            descriptor = klass.__dict__["Link"]
            break
    assert isinstance(descriptor, property)



def test_freemind::maptype_is_not_abstract():
    assert not inspect.isabstract(Freemind::MapType)


def test_freemind::maptype_constructor_exists():
    assert callable(Freemind::MapType.__init__)


def test_freemind::maptype_constructor_args():
    sig = inspect.signature(Freemind::MapType.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_freemind::maptype_has_version():
    assert hasattr(Freemind::MapType, "version")
    descriptor = None
    for klass in Freemind::MapType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_freemind::cloudtype_is_not_abstract():
    assert not inspect.isabstract(Freemind::CloudType)


def test_freemind::cloudtype_constructor_exists():
    assert callable(Freemind::CloudType.__init__)


def test_freemind::cloudtype_constructor_args():
    sig = inspect.signature(Freemind::CloudType.__init__)
    params = list(sig.parameters.keys())
    assert "Color" in params, "Missing parameter 'Color'"

def test_freemind::cloudtype_has_Color():
    assert hasattr(Freemind::CloudType, "Color")
    descriptor = None
    for klass in Freemind::CloudType.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)



def test_freemind::edgetype_is_not_abstract():
    assert not inspect.isabstract(Freemind::EdgeType)


def test_freemind::edgetype_constructor_exists():
    assert callable(Freemind::EdgeType.__init__)


def test_freemind::edgetype_constructor_args():
    sig = inspect.signature(Freemind::EdgeType.__init__)
    params = list(sig.parameters.keys())
    assert "Style" in params, "Missing parameter 'Style'"
    assert "Width" in params, "Missing parameter 'Width'"
    assert "Color" in params, "Missing parameter 'Color'"

def test_freemind::edgetype_has_Style():
    assert hasattr(Freemind::EdgeType, "Style")
    descriptor = None
    for klass in Freemind::EdgeType.__mro__:
        if "Style" in klass.__dict__:
            descriptor = klass.__dict__["Style"]
            break
    assert isinstance(descriptor, property)

def test_freemind::edgetype_has_Width():
    assert hasattr(Freemind::EdgeType, "Width")
    descriptor = None
    for klass in Freemind::EdgeType.__mro__:
        if "Width" in klass.__dict__:
            descriptor = klass.__dict__["Width"]
            break
    assert isinstance(descriptor, property)

def test_freemind::edgetype_has_Color():
    assert hasattr(Freemind::EdgeType, "Color")
    descriptor = None
    for klass in Freemind::EdgeType.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)



def test_freemind::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(Freemind::EStringToStringMapEntry)


def test_freemind::estringtostringmapentry_constructor_exists():
    assert callable(Freemind::EStringToStringMapEntry.__init__)


def test_freemind::estringtostringmapentry_constructor_args():
    sig = inspect.signature(Freemind::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_freemind::documentroot_is_not_abstract():
    assert not inspect.isabstract(Freemind::DocumentRoot)


def test_freemind::documentroot_constructor_exists():
    assert callable(Freemind::DocumentRoot.__init__)


def test_freemind::documentroot_constructor_args():
    sig = inspect.signature(Freemind::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_freemind::documentroot_has_mixed():
    assert hasattr(Freemind::DocumentRoot, "mixed")
    descriptor = None
    for klass in Freemind::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_freemind::arrowlinktype_is_not_abstract():
    assert not inspect.isabstract(Freemind::ArrowlinkType)


def test_freemind::arrowlinktype_constructor_exists():
    assert callable(Freemind::ArrowlinkType.__init__)


def test_freemind::arrowlinktype_constructor_args():
    sig = inspect.signature(Freemind::ArrowlinkType.__init__)
    params = list(sig.parameters.keys())
    assert "Color" in params, "Missing parameter 'Color'"
    assert "StartInclination" in params, "Missing parameter 'StartInclination'"
    assert "EndArrow" in params, "Missing parameter 'EndArrow'"
    assert "EndInclination" in params, "Missing parameter 'EndInclination'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "StartArrow" in params, "Missing parameter 'StartArrow'"
    assert "Destination" in params, "Missing parameter 'Destination'"

def test_freemind::arrowlinktype_has_Color():
    assert hasattr(Freemind::ArrowlinkType, "Color")
    descriptor = None
    for klass in Freemind::ArrowlinkType.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)

def test_freemind::arrowlinktype_has_StartInclination():
    assert hasattr(Freemind::ArrowlinkType, "StartInclination")
    descriptor = None
    for klass in Freemind::ArrowlinkType.__mro__:
        if "StartInclination" in klass.__dict__:
            descriptor = klass.__dict__["StartInclination"]
            break
    assert isinstance(descriptor, property)

def test_freemind::arrowlinktype_has_EndArrow():
    assert hasattr(Freemind::ArrowlinkType, "EndArrow")
    descriptor = None
    for klass in Freemind::ArrowlinkType.__mro__:
        if "EndArrow" in klass.__dict__:
            descriptor = klass.__dict__["EndArrow"]
            break
    assert isinstance(descriptor, property)

def test_freemind::arrowlinktype_has_EndInclination():
    assert hasattr(Freemind::ArrowlinkType, "EndInclination")
    descriptor = None
    for klass in Freemind::ArrowlinkType.__mro__:
        if "EndInclination" in klass.__dict__:
            descriptor = klass.__dict__["EndInclination"]
            break
    assert isinstance(descriptor, property)

def test_freemind::arrowlinktype_has_Id():
    assert hasattr(Freemind::ArrowlinkType, "Id")
    descriptor = None
    for klass in Freemind::ArrowlinkType.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_freemind::arrowlinktype_has_StartArrow():
    assert hasattr(Freemind::ArrowlinkType, "StartArrow")
    descriptor = None
    for klass in Freemind::ArrowlinkType.__mro__:
        if "StartArrow" in klass.__dict__:
            descriptor = klass.__dict__["StartArrow"]
            break
    assert isinstance(descriptor, property)

def test_freemind::arrowlinktype_has_Destination():
    assert hasattr(Freemind::ArrowlinkType, "Destination")
    descriptor = None
    for klass in Freemind::ArrowlinkType.__mro__:
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
        "false",
        "true",
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
        "true",
        "false",
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
Freemind::IconType_strategy = st.builds(
    Freemind::IconType,
    Builtin=
        safe_text
)
Freemind::HookType_strategy = st.builds(
    Freemind::HookType,
    Name=
        safe_text
)
Freemind::FontType_strategy = st.builds(
    Freemind::FontType,
    Name=
        safe_text,
    Size=
        safe_text,
    Italic=
        safe_text,
    Bold=
        safe_text
)
Freemind::TextType_strategy = st.builds(
    Freemind::TextType,
)
Freemind::ParametersType_strategy = st.builds(
    Freemind::ParametersType,
    RemindUserAt=
        safe_text
)
Freemind::NodeType_strategy = st.builds(
    Freemind::NodeType,
    Text=
        safe_text,
    Folded=
        safe_text,
    Id=
        safe_text,
    Vshift=
        safe_text,
    Vgap=
        safe_text,
    BackgroundColor=
        safe_text,
    group=
        safe_text,
    Color=
        safe_text,
    Style=
        safe_text,
    Hgap=
        safe_text,
    Modified=
        safe_text,
    EncryptedContent=
        safe_text,
    Created=
        safe_text,
    Position=
        safe_text,
    Link=
        safe_text
)
Freemind::MapType_strategy = st.builds(
    Freemind::MapType,
    version=
        safe_text
)
Freemind::CloudType_strategy = st.builds(
    Freemind::CloudType,
    Color=
        safe_text
)
Freemind::EdgeType_strategy = st.builds(
    Freemind::EdgeType,
    Style=
        safe_text,
    Width=
        safe_text,
    Color=
        safe_text
)
Freemind::EStringToStringMapEntry_strategy = st.builds(
    Freemind::EStringToStringMapEntry,
)
Freemind::DocumentRoot_strategy = st.builds(
    Freemind::DocumentRoot,
    mixed=
        safe_text
)
Freemind::ArrowlinkType_strategy = st.builds(
    Freemind::ArrowlinkType,
    Color=
        safe_text,
    StartInclination=
        safe_text,
    EndArrow=
        safe_text,
    EndInclination=
        safe_text,
    Id=
        safe_text,
    StartArrow=
        safe_text,
    Destination=
        safe_text
)

@given(instance=Freemind::IconType_strategy)
@settings(max_examples=50)
def test_freemind::icontype_instantiation(instance):
    assert isinstance(instance, Freemind::IconType)

@given(instance=Freemind::IconType_strategy)
def test_freemind::icontype_Builtin_type(instance):
    assert isinstance(instance.Builtin, str)


@given(instance=Freemind::IconType_strategy)
def test_freemind::icontype_Builtin_setter(instance):
    original = instance.Builtin
    instance.Builtin = original
    assert instance.Builtin == original

@given(instance=Freemind::HookType_strategy)
@settings(max_examples=50)
def test_freemind::hooktype_instantiation(instance):
    assert isinstance(instance, Freemind::HookType)

@given(instance=Freemind::HookType_strategy)
def test_freemind::hooktype_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Freemind::HookType_strategy)
def test_freemind::hooktype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Freemind::FontType_strategy)
@settings(max_examples=50)
def test_freemind::fonttype_instantiation(instance):
    assert isinstance(instance, Freemind::FontType)

@given(instance=Freemind::FontType_strategy)
def test_freemind::fonttype_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Freemind::FontType_strategy)
def test_freemind::fonttype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Freemind::FontType_strategy)
def test_freemind::fonttype_Size_type(instance):
    assert isinstance(instance.Size, str)


@given(instance=Freemind::FontType_strategy)
def test_freemind::fonttype_Size_setter(instance):
    original = instance.Size
    instance.Size = original
    assert instance.Size == original

@given(instance=Freemind::FontType_strategy)
def test_freemind::fonttype_Italic_type(instance):
    assert isinstance(instance.Italic, str)


@given(instance=Freemind::FontType_strategy)
def test_freemind::fonttype_Italic_setter(instance):
    original = instance.Italic
    instance.Italic = original
    assert instance.Italic == original

@given(instance=Freemind::FontType_strategy)
def test_freemind::fonttype_Bold_type(instance):
    assert isinstance(instance.Bold, str)


@given(instance=Freemind::FontType_strategy)
def test_freemind::fonttype_Bold_setter(instance):
    original = instance.Bold
    instance.Bold = original
    assert instance.Bold == original

@given(instance=Freemind::TextType_strategy)
@settings(max_examples=50)
def test_freemind::texttype_instantiation(instance):
    assert isinstance(instance, Freemind::TextType)

@given(instance=Freemind::ParametersType_strategy)
@settings(max_examples=50)
def test_freemind::parameterstype_instantiation(instance):
    assert isinstance(instance, Freemind::ParametersType)

@given(instance=Freemind::ParametersType_strategy)
def test_freemind::parameterstype_RemindUserAt_type(instance):
    assert isinstance(instance.RemindUserAt, str)


@given(instance=Freemind::ParametersType_strategy)
def test_freemind::parameterstype_RemindUserAt_setter(instance):
    original = instance.RemindUserAt
    instance.RemindUserAt = original
    assert instance.RemindUserAt == original

@given(instance=Freemind::NodeType_strategy)
@settings(max_examples=50)
def test_freemind::nodetype_instantiation(instance):
    assert isinstance(instance, Freemind::NodeType)

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Text_type(instance):
    assert isinstance(instance.Text, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Text_setter(instance):
    original = instance.Text
    instance.Text = original
    assert instance.Text == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Folded_type(instance):
    assert isinstance(instance.Folded, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Folded_setter(instance):
    original = instance.Folded
    instance.Folded = original
    assert instance.Folded == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Id_type(instance):
    assert isinstance(instance.Id, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Vshift_type(instance):
    assert isinstance(instance.Vshift, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Vshift_setter(instance):
    original = instance.Vshift
    instance.Vshift = original
    assert instance.Vshift == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Vgap_type(instance):
    assert isinstance(instance.Vgap, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Vgap_setter(instance):
    original = instance.Vgap
    instance.Vgap = original
    assert instance.Vgap == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_BackgroundColor_type(instance):
    assert isinstance(instance.BackgroundColor, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_BackgroundColor_setter(instance):
    original = instance.BackgroundColor
    instance.BackgroundColor = original
    assert instance.BackgroundColor == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Color_type(instance):
    assert isinstance(instance.Color, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Style_type(instance):
    assert isinstance(instance.Style, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Style_setter(instance):
    original = instance.Style
    instance.Style = original
    assert instance.Style == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Hgap_type(instance):
    assert isinstance(instance.Hgap, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Hgap_setter(instance):
    original = instance.Hgap
    instance.Hgap = original
    assert instance.Hgap == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Modified_type(instance):
    assert isinstance(instance.Modified, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Modified_setter(instance):
    original = instance.Modified
    instance.Modified = original
    assert instance.Modified == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_EncryptedContent_type(instance):
    assert isinstance(instance.EncryptedContent, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_EncryptedContent_setter(instance):
    original = instance.EncryptedContent
    instance.EncryptedContent = original
    assert instance.EncryptedContent == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Created_type(instance):
    assert isinstance(instance.Created, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Created_setter(instance):
    original = instance.Created
    instance.Created = original
    assert instance.Created == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Position_type(instance):
    assert isinstance(instance.Position, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Position_setter(instance):
    original = instance.Position
    instance.Position = original
    assert instance.Position == original

@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Link_type(instance):
    assert isinstance(instance.Link, str)


@given(instance=Freemind::NodeType_strategy)
def test_freemind::nodetype_Link_setter(instance):
    original = instance.Link
    instance.Link = original
    assert instance.Link == original

@given(instance=Freemind::MapType_strategy)
@settings(max_examples=50)
def test_freemind::maptype_instantiation(instance):
    assert isinstance(instance, Freemind::MapType)

@given(instance=Freemind::MapType_strategy)
def test_freemind::maptype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=Freemind::MapType_strategy)
def test_freemind::maptype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Freemind::CloudType_strategy)
@settings(max_examples=50)
def test_freemind::cloudtype_instantiation(instance):
    assert isinstance(instance, Freemind::CloudType)

@given(instance=Freemind::CloudType_strategy)
def test_freemind::cloudtype_Color_type(instance):
    assert isinstance(instance.Color, str)


@given(instance=Freemind::CloudType_strategy)
def test_freemind::cloudtype_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original

@given(instance=Freemind::EdgeType_strategy)
@settings(max_examples=50)
def test_freemind::edgetype_instantiation(instance):
    assert isinstance(instance, Freemind::EdgeType)

@given(instance=Freemind::EdgeType_strategy)
def test_freemind::edgetype_Style_type(instance):
    assert isinstance(instance.Style, str)


@given(instance=Freemind::EdgeType_strategy)
def test_freemind::edgetype_Style_setter(instance):
    original = instance.Style
    instance.Style = original
    assert instance.Style == original

@given(instance=Freemind::EdgeType_strategy)
def test_freemind::edgetype_Width_type(instance):
    assert isinstance(instance.Width, str)


@given(instance=Freemind::EdgeType_strategy)
def test_freemind::edgetype_Width_setter(instance):
    original = instance.Width
    instance.Width = original
    assert instance.Width == original

@given(instance=Freemind::EdgeType_strategy)
def test_freemind::edgetype_Color_type(instance):
    assert isinstance(instance.Color, str)


@given(instance=Freemind::EdgeType_strategy)
def test_freemind::edgetype_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original

@given(instance=Freemind::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_freemind::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, Freemind::EStringToStringMapEntry)

@given(instance=Freemind::DocumentRoot_strategy)
@settings(max_examples=50)
def test_freemind::documentroot_instantiation(instance):
    assert isinstance(instance, Freemind::DocumentRoot)

@given(instance=Freemind::DocumentRoot_strategy)
def test_freemind::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Freemind::DocumentRoot_strategy)
def test_freemind::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Freemind::ArrowlinkType_strategy)
@settings(max_examples=50)
def test_freemind::arrowlinktype_instantiation(instance):
    assert isinstance(instance, Freemind::ArrowlinkType)

@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_Color_type(instance):
    assert isinstance(instance.Color, str)


@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original

@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_StartInclination_type(instance):
    assert isinstance(instance.StartInclination, str)


@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_StartInclination_setter(instance):
    original = instance.StartInclination
    instance.StartInclination = original
    assert instance.StartInclination == original

@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_EndArrow_type(instance):
    assert isinstance(instance.EndArrow, str)


@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_EndArrow_setter(instance):
    original = instance.EndArrow
    instance.EndArrow = original
    assert instance.EndArrow == original

@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_EndInclination_type(instance):
    assert isinstance(instance.EndInclination, str)


@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_EndInclination_setter(instance):
    original = instance.EndInclination
    instance.EndInclination = original
    assert instance.EndInclination == original

@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_Id_type(instance):
    assert isinstance(instance.Id, str)


@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_StartArrow_type(instance):
    assert isinstance(instance.StartArrow, str)


@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_StartArrow_setter(instance):
    original = instance.StartArrow
    instance.StartArrow = original
    assert instance.StartArrow == original

@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_Destination_type(instance):
    assert isinstance(instance.Destination, str)


@given(instance=Freemind::ArrowlinkType_strategy)
def test_freemind::arrowlinktype_Destination_setter(instance):
    original = instance.Destination
    instance.Destination = original
    assert instance.Destination == original
