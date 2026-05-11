import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PersonalizedElement,
    cevinedit::Link,
    cevinedit::NodeEClass,
    cevinedit::PersonalizedElement,
    cevinedit::Diagram,
    cevinedit::CEViNEditRoot,
    cevinedit::LabelEAttribute,
    cevinedit::AffixedEReferenceCont,
    cevinedit::CompartmentEReferenceCont,
    Link,
    cevinedit::LinkEReferenceNonCont,
    cevinedit::LinkEClass,
    Brightness,
    FontStyle,
    Texture,
    LinkFigure,
    Placement,
    LayoutCompartment,
    Color,
    NodeFigure,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_personalizedelement_is_not_abstract():
    assert not inspect.isabstract(PersonalizedElement)


def test_personalizedelement_constructor_exists():
    assert callable(PersonalizedElement.__init__)


def test_personalizedelement_constructor_args():
    sig = inspect.signature(PersonalizedElement.__init__)
    params = list(sig.parameters.keys())



def test_cevinedit::link_is_not_abstract():
    assert not inspect.isabstract(cevinedit::Link)


def test_cevinedit::link_constructor_exists():
    assert callable(cevinedit::Link.__init__)


def test_cevinedit::link_constructor_args():
    sig = inspect.signature(cevinedit::Link.__init__)
    params = list(sig.parameters.keys())
    assert "texture" in params, "Missing parameter 'texture'"
    assert "width" in params, "Missing parameter 'width'"
    assert "targetDecoration" in params, "Missing parameter 'targetDecoration'"
    assert "color" in params, "Missing parameter 'color'"
    assert "sourceDecoration" in params, "Missing parameter 'sourceDecoration'"
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "labelFontStyle" in params, "Missing parameter 'labelFontStyle'"
    assert "label" in params, "Missing parameter 'label'"

def test_cevinedit::link_has_texture():
    assert hasattr(cevinedit::Link, "texture")
    descriptor = None
    for klass in cevinedit::Link.__mro__:
        if "texture" in klass.__dict__:
            descriptor = klass.__dict__["texture"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::link_has_width():
    assert hasattr(cevinedit::Link, "width")
    descriptor = None
    for klass in cevinedit::Link.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::link_has_targetDecoration():
    assert hasattr(cevinedit::Link, "targetDecoration")
    descriptor = None
    for klass in cevinedit::Link.__mro__:
        if "targetDecoration" in klass.__dict__:
            descriptor = klass.__dict__["targetDecoration"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::link_has_color():
    assert hasattr(cevinedit::Link, "color")
    descriptor = None
    for klass in cevinedit::Link.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::link_has_sourceDecoration():
    assert hasattr(cevinedit::Link, "sourceDecoration")
    descriptor = None
    for klass in cevinedit::Link.__mro__:
        if "sourceDecoration" in klass.__dict__:
            descriptor = klass.__dict__["sourceDecoration"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::link_has_brightness():
    assert hasattr(cevinedit::Link, "brightness")
    descriptor = None
    for klass in cevinedit::Link.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::link_has_labelFontStyle():
    assert hasattr(cevinedit::Link, "labelFontStyle")
    descriptor = None
    for klass in cevinedit::Link.__mro__:
        if "labelFontStyle" in klass.__dict__:
            descriptor = klass.__dict__["labelFontStyle"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::link_has_label():
    assert hasattr(cevinedit::Link, "label")
    descriptor = None
    for klass in cevinedit::Link.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_cevinedit::nodeeclass_is_not_abstract():
    assert not inspect.isabstract(cevinedit::NodeEClass)


def test_cevinedit::nodeeclass_constructor_exists():
    assert callable(cevinedit::NodeEClass.__init__)


def test_cevinedit::nodeeclass_constructor_args():
    sig = inspect.signature(cevinedit::NodeEClass.__init__)
    params = list(sig.parameters.keys())
    assert "borderWidth" in params, "Missing parameter 'borderWidth'"
    assert "figure" in params, "Missing parameter 'figure'"
    assert "listPointsPolygon" in params, "Missing parameter 'listPointsPolygon'"
    assert "labelPlacement" in params, "Missing parameter 'labelPlacement'"
    assert "resizable" in params, "Missing parameter 'resizable'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "size" in params, "Missing parameter 'size'"
    assert "labelFontStyle" in params, "Missing parameter 'labelFontStyle'"
    assert "imagePath" in params, "Missing parameter 'imagePath'"
    assert "borderTexture" in params, "Missing parameter 'borderTexture'"
    assert "borderColor" in params, "Missing parameter 'borderColor'"
    assert "label" in params, "Missing parameter 'label'"

def test_cevinedit::nodeeclass_has_borderWidth():
    assert hasattr(cevinedit::NodeEClass, "borderWidth")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "borderWidth" in klass.__dict__:
            descriptor = klass.__dict__["borderWidth"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_figure():
    assert hasattr(cevinedit::NodeEClass, "figure")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "figure" in klass.__dict__:
            descriptor = klass.__dict__["figure"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_listPointsPolygon():
    assert hasattr(cevinedit::NodeEClass, "listPointsPolygon")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "listPointsPolygon" in klass.__dict__:
            descriptor = klass.__dict__["listPointsPolygon"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_labelPlacement():
    assert hasattr(cevinedit::NodeEClass, "labelPlacement")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "labelPlacement" in klass.__dict__:
            descriptor = klass.__dict__["labelPlacement"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_resizable():
    assert hasattr(cevinedit::NodeEClass, "resizable")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "resizable" in klass.__dict__:
            descriptor = klass.__dict__["resizable"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_backgroundColor():
    assert hasattr(cevinedit::NodeEClass, "backgroundColor")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_brightness():
    assert hasattr(cevinedit::NodeEClass, "brightness")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_size():
    assert hasattr(cevinedit::NodeEClass, "size")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_labelFontStyle():
    assert hasattr(cevinedit::NodeEClass, "labelFontStyle")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "labelFontStyle" in klass.__dict__:
            descriptor = klass.__dict__["labelFontStyle"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_imagePath():
    assert hasattr(cevinedit::NodeEClass, "imagePath")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "imagePath" in klass.__dict__:
            descriptor = klass.__dict__["imagePath"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_borderTexture():
    assert hasattr(cevinedit::NodeEClass, "borderTexture")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "borderTexture" in klass.__dict__:
            descriptor = klass.__dict__["borderTexture"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_borderColor():
    assert hasattr(cevinedit::NodeEClass, "borderColor")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "borderColor" in klass.__dict__:
            descriptor = klass.__dict__["borderColor"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::nodeeclass_has_label():
    assert hasattr(cevinedit::NodeEClass, "label")
    descriptor = None
    for klass in cevinedit::NodeEClass.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_cevinedit::personalizedelement_is_not_abstract():
    assert not inspect.isabstract(cevinedit::PersonalizedElement)


def test_cevinedit::personalizedelement_constructor_exists():
    assert callable(cevinedit::PersonalizedElement.__init__)


def test_cevinedit::personalizedelement_constructor_args():
    sig = inspect.signature(cevinedit::PersonalizedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "icon" in params, "Missing parameter 'icon'"

def test_cevinedit::personalizedelement_has_name():
    assert hasattr(cevinedit::PersonalizedElement, "name")
    descriptor = None
    for klass in cevinedit::PersonalizedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::personalizedelement_has_icon():
    assert hasattr(cevinedit::PersonalizedElement, "icon")
    descriptor = None
    for klass in cevinedit::PersonalizedElement.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_cevinedit::diagram_is_not_abstract():
    assert not inspect.isabstract(cevinedit::Diagram)


def test_cevinedit::diagram_constructor_exists():
    assert callable(cevinedit::Diagram.__init__)


def test_cevinedit::diagram_constructor_args():
    sig = inspect.signature(cevinedit::Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "modelExtension" in params, "Missing parameter 'modelExtension'"
    assert "name" in params, "Missing parameter 'name'"

def test_cevinedit::diagram_has_modelExtension():
    assert hasattr(cevinedit::Diagram, "modelExtension")
    descriptor = None
    for klass in cevinedit::Diagram.__mro__:
        if "modelExtension" in klass.__dict__:
            descriptor = klass.__dict__["modelExtension"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::diagram_has_name():
    assert hasattr(cevinedit::Diagram, "name")
    descriptor = None
    for klass in cevinedit::Diagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cevinedit::cevineditroot_is_not_abstract():
    assert not inspect.isabstract(cevinedit::CEViNEditRoot)


def test_cevinedit::cevineditroot_constructor_exists():
    assert callable(cevinedit::CEViNEditRoot.__init__)


def test_cevinedit::cevineditroot_constructor_args():
    sig = inspect.signature(cevinedit::CEViNEditRoot.__init__)
    params = list(sig.parameters.keys())
    assert "sourceMM" in params, "Missing parameter 'sourceMM'"

def test_cevinedit::cevineditroot_has_sourceMM():
    assert hasattr(cevinedit::CEViNEditRoot, "sourceMM")
    descriptor = None
    for klass in cevinedit::CEViNEditRoot.__mro__:
        if "sourceMM" in klass.__dict__:
            descriptor = klass.__dict__["sourceMM"]
            break
    assert isinstance(descriptor, property)



def test_cevinedit::labeleattribute_is_not_abstract():
    assert not inspect.isabstract(cevinedit::LabelEAttribute)


def test_cevinedit::labeleattribute_constructor_exists():
    assert callable(cevinedit::LabelEAttribute.__init__)


def test_cevinedit::labeleattribute_constructor_args():
    sig = inspect.signature(cevinedit::LabelEAttribute.__init__)
    params = list(sig.parameters.keys())



def test_cevinedit::affixedereferencecont_is_not_abstract():
    assert not inspect.isabstract(cevinedit::AffixedEReferenceCont)


def test_cevinedit::affixedereferencecont_constructor_exists():
    assert callable(cevinedit::AffixedEReferenceCont.__init__)


def test_cevinedit::affixedereferencecont_constructor_args():
    sig = inspect.signature(cevinedit::AffixedEReferenceCont.__init__)
    params = list(sig.parameters.keys())



def test_cevinedit::compartmentereferencecont_is_not_abstract():
    assert not inspect.isabstract(cevinedit::CompartmentEReferenceCont)


def test_cevinedit::compartmentereferencecont_constructor_exists():
    assert callable(cevinedit::CompartmentEReferenceCont.__init__)


def test_cevinedit::compartmentereferencecont_constructor_args():
    sig = inspect.signature(cevinedit::CompartmentEReferenceCont.__init__)
    params = list(sig.parameters.keys())
    assert "collapsible" in params, "Missing parameter 'collapsible'"
    assert "layout" in params, "Missing parameter 'layout'"

def test_cevinedit::compartmentereferencecont_has_collapsible():
    assert hasattr(cevinedit::CompartmentEReferenceCont, "collapsible")
    descriptor = None
    for klass in cevinedit::CompartmentEReferenceCont.__mro__:
        if "collapsible" in klass.__dict__:
            descriptor = klass.__dict__["collapsible"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::compartmentereferencecont_has_layout():
    assert hasattr(cevinedit::CompartmentEReferenceCont, "layout")
    descriptor = None
    for klass in cevinedit::CompartmentEReferenceCont.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_link_constructor_exists():
    assert callable(Link.__init__)


def test_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_cevinedit::linkereferencenoncont_is_not_abstract():
    assert not inspect.isabstract(cevinedit::LinkEReferenceNonCont)


def test_cevinedit::linkereferencenoncont_constructor_exists():
    assert callable(cevinedit::LinkEReferenceNonCont.__init__)


def test_cevinedit::linkereferencenoncont_constructor_args():
    sig = inspect.signature(cevinedit::LinkEReferenceNonCont.__init__)
    params = list(sig.parameters.keys())



def test_cevinedit::linkeclass_is_not_abstract():
    assert not inspect.isabstract(cevinedit::LinkEClass)


def test_cevinedit::linkeclass_constructor_exists():
    assert callable(cevinedit::LinkEClass.__init__)


def test_cevinedit::linkeclass_constructor_args():
    sig = inspect.signature(cevinedit::LinkEClass.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "target" in params, "Missing parameter 'target'"

def test_cevinedit::linkeclass_has_source():
    assert hasattr(cevinedit::LinkEClass, "source")
    descriptor = None
    for klass in cevinedit::LinkEClass.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit::linkeclass_has_target():
    assert hasattr(cevinedit::LinkEClass, "target")
    descriptor = None
    for klass in cevinedit::LinkEClass.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_brightness_exists():
    # Check that the Enumeration exists
    assert Brightness is not None

def test_brightness_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Brightness]
    expected_literals = [
        "Default",
        "Light",
        "Dark",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Brightness"

def test_fontstyle_exists():
    # Check that the Enumeration exists
    assert FontStyle is not None

def test_fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontStyle]
    expected_literals = [
        "Italic",
        "Bold",
        "Default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontStyle"

def test_texture_exists():
    # Check that the Enumeration exists
    assert Texture is not None

def test_texture_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Texture]
    expected_literals = [
        "Dash",
        "Dot",
        "Default",
        "Solid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Texture"

def test_linkfigure_exists():
    # Check that the Enumeration exists
    assert LinkFigure is not None

def test_linkfigure_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkFigure]
    expected_literals = [
        "Square",
        "Arrow",
        "FilledSquare",
        "Rhomb",
        "FilledRhomb",
        "None_",
        "ClosedArrow",
        "FilledClosedArrow",
        "Default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkFigure"

def test_placement_exists():
    # Check that the Enumeration exists
    assert Placement is not None

def test_placement_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Placement]
    expected_literals = [
        "None_",
        "Internal",
        "External",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Placement"

def test_layoutcompartment_exists():
    # Check that the Enumeration exists
    assert LayoutCompartment is not None

def test_layoutcompartment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LayoutCompartment]
    expected_literals = [
        "Free",
        "List",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LayoutCompartment"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "Green",
        "Black",
        "Blue",
        "Yellow",
        "Orange",
        "Default",
        "White",
        "Cyan",
        "Gray",
        "Red",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_nodefigure_exists():
    # Check that the Enumeration exists
    assert NodeFigure is not None

def test_nodefigure_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeFigure]
    expected_literals = [
        "Image",
        "Polygon",
        "Ellipse",
        "SVG",
        "Rounded",
        "Default",
        "Rectangle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeFigure"


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
PersonalizedElement_strategy = st.builds(
    PersonalizedElement,
)
cevinedit::Link_strategy = st.builds(
    cevinedit::Link,
    texture=
        safe_text,
    width=
        st.integers(),
    targetDecoration=
        safe_text,
    color=
        safe_text,
    sourceDecoration=
        safe_text,
    brightness=
        safe_text,
    labelFontStyle=
        safe_text,
    label=
        safe_text
)
cevinedit::NodeEClass_strategy = st.builds(
    cevinedit::NodeEClass,
    borderWidth=
        st.integers(),
    figure=
        safe_text,
    listPointsPolygon=
        safe_text,
    labelPlacement=
        safe_text,
    resizable=
        st.booleans(),
    backgroundColor=
        safe_text,
    brightness=
        safe_text,
    size=
        safe_text,
    labelFontStyle=
        safe_text,
    imagePath=
        safe_text,
    borderTexture=
        safe_text,
    borderColor=
        safe_text,
    label=
        safe_text
)
cevinedit::PersonalizedElement_strategy = st.builds(
    cevinedit::PersonalizedElement,
    name=
        safe_text,
    icon=
        safe_text
)
cevinedit::Diagram_strategy = st.builds(
    cevinedit::Diagram,
    modelExtension=
        safe_text,
    name=
        safe_text
)
cevinedit::CEViNEditRoot_strategy = st.builds(
    cevinedit::CEViNEditRoot,
    sourceMM=
        safe_text
)
cevinedit::LabelEAttribute_strategy = st.builds(
    cevinedit::LabelEAttribute,
)
cevinedit::AffixedEReferenceCont_strategy = st.builds(
    cevinedit::AffixedEReferenceCont,
)
cevinedit::CompartmentEReferenceCont_strategy = st.builds(
    cevinedit::CompartmentEReferenceCont,
    collapsible=
        st.booleans(),
    layout=
        safe_text
)
Link_strategy = st.builds(
    Link,
)
cevinedit::LinkEReferenceNonCont_strategy = st.builds(
    cevinedit::LinkEReferenceNonCont,
)
cevinedit::LinkEClass_strategy = st.builds(
    cevinedit::LinkEClass,
    source=
        safe_text,
    target=
        safe_text
)

@given(instance=PersonalizedElement_strategy)
@settings(max_examples=50)
def test_personalizedelement_instantiation(instance):
    assert isinstance(instance, PersonalizedElement)

@given(instance=cevinedit::Link_strategy)
@settings(max_examples=50)
def test_cevinedit::link_instantiation(instance):
    assert isinstance(instance, cevinedit::Link)

@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_texture_type(instance):
    assert isinstance(instance.texture, str)


@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_texture_setter(instance):
    original = instance.texture
    instance.texture = original
    assert instance.texture == original

@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_targetDecoration_type(instance):
    assert isinstance(instance.targetDecoration, str)


@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_targetDecoration_setter(instance):
    original = instance.targetDecoration
    instance.targetDecoration = original
    assert instance.targetDecoration == original

@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_sourceDecoration_type(instance):
    assert isinstance(instance.sourceDecoration, str)


@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_sourceDecoration_setter(instance):
    original = instance.sourceDecoration
    instance.sourceDecoration = original
    assert instance.sourceDecoration == original

@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_brightness_type(instance):
    assert isinstance(instance.brightness, str)


@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original

@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_labelFontStyle_type(instance):
    assert isinstance(instance.labelFontStyle, str)


@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_labelFontStyle_setter(instance):
    original = instance.labelFontStyle
    instance.labelFontStyle = original
    assert instance.labelFontStyle == original

@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=cevinedit::Link_strategy)
def test_cevinedit::link_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=cevinedit::NodeEClass_strategy)
@settings(max_examples=50)
def test_cevinedit::nodeeclass_instantiation(instance):
    assert isinstance(instance, cevinedit::NodeEClass)

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_borderWidth_type(instance):
    assert isinstance(instance.borderWidth, int)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_borderWidth_setter(instance):
    original = instance.borderWidth
    instance.borderWidth = original
    assert instance.borderWidth == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_figure_type(instance):
    assert isinstance(instance.figure, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_figure_setter(instance):
    original = instance.figure
    instance.figure = original
    assert instance.figure == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_listPointsPolygon_type(instance):
    assert isinstance(instance.listPointsPolygon, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_listPointsPolygon_setter(instance):
    original = instance.listPointsPolygon
    instance.listPointsPolygon = original
    assert instance.listPointsPolygon == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_labelPlacement_type(instance):
    assert isinstance(instance.labelPlacement, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_labelPlacement_setter(instance):
    original = instance.labelPlacement
    instance.labelPlacement = original
    assert instance.labelPlacement == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_resizable_type(instance):
    assert isinstance(instance.resizable, bool)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_backgroundColor_type(instance):
    assert isinstance(instance.backgroundColor, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_brightness_type(instance):
    assert isinstance(instance.brightness, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_labelFontStyle_type(instance):
    assert isinstance(instance.labelFontStyle, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_labelFontStyle_setter(instance):
    original = instance.labelFontStyle
    instance.labelFontStyle = original
    assert instance.labelFontStyle == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_imagePath_type(instance):
    assert isinstance(instance.imagePath, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_imagePath_setter(instance):
    original = instance.imagePath
    instance.imagePath = original
    assert instance.imagePath == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_borderTexture_type(instance):
    assert isinstance(instance.borderTexture, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_borderTexture_setter(instance):
    original = instance.borderTexture
    instance.borderTexture = original
    assert instance.borderTexture == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_borderColor_type(instance):
    assert isinstance(instance.borderColor, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_borderColor_setter(instance):
    original = instance.borderColor
    instance.borderColor = original
    assert instance.borderColor == original

@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=cevinedit::NodeEClass_strategy)
def test_cevinedit::nodeeclass_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=cevinedit::PersonalizedElement_strategy)
@settings(max_examples=50)
def test_cevinedit::personalizedelement_instantiation(instance):
    assert isinstance(instance, cevinedit::PersonalizedElement)

@given(instance=cevinedit::PersonalizedElement_strategy)
def test_cevinedit::personalizedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cevinedit::PersonalizedElement_strategy)
def test_cevinedit::personalizedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cevinedit::PersonalizedElement_strategy)
def test_cevinedit::personalizedelement_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=cevinedit::PersonalizedElement_strategy)
def test_cevinedit::personalizedelement_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=cevinedit::Diagram_strategy)
@settings(max_examples=50)
def test_cevinedit::diagram_instantiation(instance):
    assert isinstance(instance, cevinedit::Diagram)

@given(instance=cevinedit::Diagram_strategy)
def test_cevinedit::diagram_modelExtension_type(instance):
    assert isinstance(instance.modelExtension, str)


@given(instance=cevinedit::Diagram_strategy)
def test_cevinedit::diagram_modelExtension_setter(instance):
    original = instance.modelExtension
    instance.modelExtension = original
    assert instance.modelExtension == original

@given(instance=cevinedit::Diagram_strategy)
def test_cevinedit::diagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cevinedit::Diagram_strategy)
def test_cevinedit::diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cevinedit::CEViNEditRoot_strategy)
@settings(max_examples=50)
def test_cevinedit::cevineditroot_instantiation(instance):
    assert isinstance(instance, cevinedit::CEViNEditRoot)

@given(instance=cevinedit::CEViNEditRoot_strategy)
def test_cevinedit::cevineditroot_sourceMM_type(instance):
    assert isinstance(instance.sourceMM, str)


@given(instance=cevinedit::CEViNEditRoot_strategy)
def test_cevinedit::cevineditroot_sourceMM_setter(instance):
    original = instance.sourceMM
    instance.sourceMM = original
    assert instance.sourceMM == original

@given(instance=cevinedit::LabelEAttribute_strategy)
@settings(max_examples=50)
def test_cevinedit::labeleattribute_instantiation(instance):
    assert isinstance(instance, cevinedit::LabelEAttribute)

@given(instance=cevinedit::AffixedEReferenceCont_strategy)
@settings(max_examples=50)
def test_cevinedit::affixedereferencecont_instantiation(instance):
    assert isinstance(instance, cevinedit::AffixedEReferenceCont)

@given(instance=cevinedit::CompartmentEReferenceCont_strategy)
@settings(max_examples=50)
def test_cevinedit::compartmentereferencecont_instantiation(instance):
    assert isinstance(instance, cevinedit::CompartmentEReferenceCont)

@given(instance=cevinedit::CompartmentEReferenceCont_strategy)
def test_cevinedit::compartmentereferencecont_collapsible_type(instance):
    assert isinstance(instance.collapsible, bool)


@given(instance=cevinedit::CompartmentEReferenceCont_strategy)
def test_cevinedit::compartmentereferencecont_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original

@given(instance=cevinedit::CompartmentEReferenceCont_strategy)
def test_cevinedit::compartmentereferencecont_layout_type(instance):
    assert isinstance(instance.layout, str)


@given(instance=cevinedit::CompartmentEReferenceCont_strategy)
def test_cevinedit::compartmentereferencecont_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=Link_strategy)
@settings(max_examples=50)
def test_link_instantiation(instance):
    assert isinstance(instance, Link)

@given(instance=cevinedit::LinkEReferenceNonCont_strategy)
@settings(max_examples=50)
def test_cevinedit::linkereferencenoncont_instantiation(instance):
    assert isinstance(instance, cevinedit::LinkEReferenceNonCont)

@given(instance=cevinedit::LinkEClass_strategy)
@settings(max_examples=50)
def test_cevinedit::linkeclass_instantiation(instance):
    assert isinstance(instance, cevinedit::LinkEClass)

@given(instance=cevinedit::LinkEClass_strategy)
def test_cevinedit::linkeclass_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=cevinedit::LinkEClass_strategy)
def test_cevinedit::linkeclass_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=cevinedit::LinkEClass_strategy)
def test_cevinedit::linkeclass_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=cevinedit::LinkEClass_strategy)
def test_cevinedit::linkeclass_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original
