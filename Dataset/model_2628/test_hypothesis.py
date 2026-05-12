import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PersonalizedElement,
    cevinedit_Link,
    cevinedit_NodeEClass,
    cevinedit_PersonalizedElement,
    cevinedit_Diagram,
    cevinedit_CEViNEditRoot,
    cevinedit_LabelEAttribute,
    cevinedit_AffixedEReferenceCont,
    cevinedit_CompartmentEReferenceCont,
    Link,
    cevinedit_LinkEReferenceNonCont,
    cevinedit_LinkEClass,
    LayoutCompartment,
    Texture,
    FontStyle,
    NodeFigure,
    Brightness,
    Placement,
    LinkFigure,
    Color,
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



def test_cevinedit_link_is_not_abstract():
    assert not inspect.isabstract(cevinedit_Link)


def test_cevinedit_link_constructor_exists():
    assert callable(cevinedit_Link.__init__)


def test_cevinedit_link_constructor_args():
    sig = inspect.signature(cevinedit_Link.__init__)
    params = list(sig.parameters.keys())
    assert "labelFontStyle" in params, "Missing parameter 'labelFontStyle'"
    assert "width" in params, "Missing parameter 'width'"
    assert "targetDecoration" in params, "Missing parameter 'targetDecoration'"
    assert "label" in params, "Missing parameter 'label'"
    assert "sourceDecoration" in params, "Missing parameter 'sourceDecoration'"
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "texture" in params, "Missing parameter 'texture'"
    assert "color" in params, "Missing parameter 'color'"

def test_cevinedit_link_has_labelFontStyle():
    assert hasattr(cevinedit_Link, "labelFontStyle")
    descriptor = None
    for klass in cevinedit_Link.__mro__:
        if "labelFontStyle" in klass.__dict__:
            descriptor = klass.__dict__["labelFontStyle"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_link_has_width():
    assert hasattr(cevinedit_Link, "width")
    descriptor = None
    for klass in cevinedit_Link.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_link_has_targetDecoration():
    assert hasattr(cevinedit_Link, "targetDecoration")
    descriptor = None
    for klass in cevinedit_Link.__mro__:
        if "targetDecoration" in klass.__dict__:
            descriptor = klass.__dict__["targetDecoration"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_link_has_label():
    assert hasattr(cevinedit_Link, "label")
    descriptor = None
    for klass in cevinedit_Link.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_link_has_sourceDecoration():
    assert hasattr(cevinedit_Link, "sourceDecoration")
    descriptor = None
    for klass in cevinedit_Link.__mro__:
        if "sourceDecoration" in klass.__dict__:
            descriptor = klass.__dict__["sourceDecoration"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_link_has_brightness():
    assert hasattr(cevinedit_Link, "brightness")
    descriptor = None
    for klass in cevinedit_Link.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_link_has_texture():
    assert hasattr(cevinedit_Link, "texture")
    descriptor = None
    for klass in cevinedit_Link.__mro__:
        if "texture" in klass.__dict__:
            descriptor = klass.__dict__["texture"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_link_has_color():
    assert hasattr(cevinedit_Link, "color")
    descriptor = None
    for klass in cevinedit_Link.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_cevinedit_nodeeclass_is_not_abstract():
    assert not inspect.isabstract(cevinedit_NodeEClass)


def test_cevinedit_nodeeclass_constructor_exists():
    assert callable(cevinedit_NodeEClass.__init__)


def test_cevinedit_nodeeclass_constructor_args():
    sig = inspect.signature(cevinedit_NodeEClass.__init__)
    params = list(sig.parameters.keys())
    assert "borderWidth" in params, "Missing parameter 'borderWidth'"
    assert "listPointsPolygon" in params, "Missing parameter 'listPointsPolygon'"
    assert "borderColor" in params, "Missing parameter 'borderColor'"
    assert "figure" in params, "Missing parameter 'figure'"
    assert "labelPlacement" in params, "Missing parameter 'labelPlacement'"
    assert "borderTexture" in params, "Missing parameter 'borderTexture'"
    assert "size" in params, "Missing parameter 'size'"
    assert "labelFontStyle" in params, "Missing parameter 'labelFontStyle'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "label" in params, "Missing parameter 'label'"
    assert "imagePath" in params, "Missing parameter 'imagePath'"
    assert "resizable" in params, "Missing parameter 'resizable'"

def test_cevinedit_nodeeclass_has_borderWidth():
    assert hasattr(cevinedit_NodeEClass, "borderWidth")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "borderWidth" in klass.__dict__:
            descriptor = klass.__dict__["borderWidth"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_listPointsPolygon():
    assert hasattr(cevinedit_NodeEClass, "listPointsPolygon")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "listPointsPolygon" in klass.__dict__:
            descriptor = klass.__dict__["listPointsPolygon"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_borderColor():
    assert hasattr(cevinedit_NodeEClass, "borderColor")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "borderColor" in klass.__dict__:
            descriptor = klass.__dict__["borderColor"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_figure():
    assert hasattr(cevinedit_NodeEClass, "figure")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "figure" in klass.__dict__:
            descriptor = klass.__dict__["figure"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_labelPlacement():
    assert hasattr(cevinedit_NodeEClass, "labelPlacement")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "labelPlacement" in klass.__dict__:
            descriptor = klass.__dict__["labelPlacement"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_borderTexture():
    assert hasattr(cevinedit_NodeEClass, "borderTexture")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "borderTexture" in klass.__dict__:
            descriptor = klass.__dict__["borderTexture"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_size():
    assert hasattr(cevinedit_NodeEClass, "size")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_labelFontStyle():
    assert hasattr(cevinedit_NodeEClass, "labelFontStyle")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "labelFontStyle" in klass.__dict__:
            descriptor = klass.__dict__["labelFontStyle"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_backgroundColor():
    assert hasattr(cevinedit_NodeEClass, "backgroundColor")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_brightness():
    assert hasattr(cevinedit_NodeEClass, "brightness")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_label():
    assert hasattr(cevinedit_NodeEClass, "label")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_imagePath():
    assert hasattr(cevinedit_NodeEClass, "imagePath")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "imagePath" in klass.__dict__:
            descriptor = klass.__dict__["imagePath"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_nodeeclass_has_resizable():
    assert hasattr(cevinedit_NodeEClass, "resizable")
    descriptor = None
    for klass in cevinedit_NodeEClass.__mro__:
        if "resizable" in klass.__dict__:
            descriptor = klass.__dict__["resizable"]
            break
    assert isinstance(descriptor, property)



def test_cevinedit_personalizedelement_is_not_abstract():
    assert not inspect.isabstract(cevinedit_PersonalizedElement)


def test_cevinedit_personalizedelement_constructor_exists():
    assert callable(cevinedit_PersonalizedElement.__init__)


def test_cevinedit_personalizedelement_constructor_args():
    sig = inspect.signature(cevinedit_PersonalizedElement.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"
    assert "name" in params, "Missing parameter 'name'"

def test_cevinedit_personalizedelement_has_icon():
    assert hasattr(cevinedit_PersonalizedElement, "icon")
    descriptor = None
    for klass in cevinedit_PersonalizedElement.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_personalizedelement_has_name():
    assert hasattr(cevinedit_PersonalizedElement, "name")
    descriptor = None
    for klass in cevinedit_PersonalizedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cevinedit_diagram_is_not_abstract():
    assert not inspect.isabstract(cevinedit_Diagram)


def test_cevinedit_diagram_constructor_exists():
    assert callable(cevinedit_Diagram.__init__)


def test_cevinedit_diagram_constructor_args():
    sig = inspect.signature(cevinedit_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "modelExtension" in params, "Missing parameter 'modelExtension'"
    assert "name" in params, "Missing parameter 'name'"

def test_cevinedit_diagram_has_modelExtension():
    assert hasattr(cevinedit_Diagram, "modelExtension")
    descriptor = None
    for klass in cevinedit_Diagram.__mro__:
        if "modelExtension" in klass.__dict__:
            descriptor = klass.__dict__["modelExtension"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_diagram_has_name():
    assert hasattr(cevinedit_Diagram, "name")
    descriptor = None
    for klass in cevinedit_Diagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cevinedit_cevineditroot_is_not_abstract():
    assert not inspect.isabstract(cevinedit_CEViNEditRoot)


def test_cevinedit_cevineditroot_constructor_exists():
    assert callable(cevinedit_CEViNEditRoot.__init__)


def test_cevinedit_cevineditroot_constructor_args():
    sig = inspect.signature(cevinedit_CEViNEditRoot.__init__)
    params = list(sig.parameters.keys())
    assert "sourceMM" in params, "Missing parameter 'sourceMM'"

def test_cevinedit_cevineditroot_has_sourceMM():
    assert hasattr(cevinedit_CEViNEditRoot, "sourceMM")
    descriptor = None
    for klass in cevinedit_CEViNEditRoot.__mro__:
        if "sourceMM" in klass.__dict__:
            descriptor = klass.__dict__["sourceMM"]
            break
    assert isinstance(descriptor, property)



def test_cevinedit_labeleattribute_is_not_abstract():
    assert not inspect.isabstract(cevinedit_LabelEAttribute)


def test_cevinedit_labeleattribute_constructor_exists():
    assert callable(cevinedit_LabelEAttribute.__init__)


def test_cevinedit_labeleattribute_constructor_args():
    sig = inspect.signature(cevinedit_LabelEAttribute.__init__)
    params = list(sig.parameters.keys())



def test_cevinedit_affixedereferencecont_is_not_abstract():
    assert not inspect.isabstract(cevinedit_AffixedEReferenceCont)


def test_cevinedit_affixedereferencecont_constructor_exists():
    assert callable(cevinedit_AffixedEReferenceCont.__init__)


def test_cevinedit_affixedereferencecont_constructor_args():
    sig = inspect.signature(cevinedit_AffixedEReferenceCont.__init__)
    params = list(sig.parameters.keys())



def test_cevinedit_compartmentereferencecont_is_not_abstract():
    assert not inspect.isabstract(cevinedit_CompartmentEReferenceCont)


def test_cevinedit_compartmentereferencecont_constructor_exists():
    assert callable(cevinedit_CompartmentEReferenceCont.__init__)


def test_cevinedit_compartmentereferencecont_constructor_args():
    sig = inspect.signature(cevinedit_CompartmentEReferenceCont.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"
    assert "collapsible" in params, "Missing parameter 'collapsible'"

def test_cevinedit_compartmentereferencecont_has_layout():
    assert hasattr(cevinedit_CompartmentEReferenceCont, "layout")
    descriptor = None
    for klass in cevinedit_CompartmentEReferenceCont.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_compartmentereferencecont_has_collapsible():
    assert hasattr(cevinedit_CompartmentEReferenceCont, "collapsible")
    descriptor = None
    for klass in cevinedit_CompartmentEReferenceCont.__mro__:
        if "collapsible" in klass.__dict__:
            descriptor = klass.__dict__["collapsible"]
            break
    assert isinstance(descriptor, property)



def test_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_link_constructor_exists():
    assert callable(Link.__init__)


def test_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_cevinedit_linkereferencenoncont_is_not_abstract():
    assert not inspect.isabstract(cevinedit_LinkEReferenceNonCont)


def test_cevinedit_linkereferencenoncont_constructor_exists():
    assert callable(cevinedit_LinkEReferenceNonCont.__init__)


def test_cevinedit_linkereferencenoncont_constructor_args():
    sig = inspect.signature(cevinedit_LinkEReferenceNonCont.__init__)
    params = list(sig.parameters.keys())



def test_cevinedit_linkeclass_is_not_abstract():
    assert not inspect.isabstract(cevinedit_LinkEClass)


def test_cevinedit_linkeclass_constructor_exists():
    assert callable(cevinedit_LinkEClass.__init__)


def test_cevinedit_linkeclass_constructor_args():
    sig = inspect.signature(cevinedit_LinkEClass.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "target" in params, "Missing parameter 'target'"

def test_cevinedit_linkeclass_has_source():
    assert hasattr(cevinedit_LinkEClass, "source")
    descriptor = None
    for klass in cevinedit_LinkEClass.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_cevinedit_linkeclass_has_target():
    assert hasattr(cevinedit_LinkEClass, "target")
    descriptor = None
    for klass in cevinedit_LinkEClass.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_layoutcompartment_exists():
    # Check that the Enumeration exists
    assert LayoutCompartment is not None

def test_layoutcompartment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LayoutCompartment]
    expected_literals = [
        "List",
        "Free",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LayoutCompartment"

def test_texture_exists():
    # Check that the Enumeration exists
    assert Texture is not None

def test_texture_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Texture]
    expected_literals = [
        "Dash",
        "Dot",
        "Solid",
        "Default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Texture"

def test_fontstyle_exists():
    # Check that the Enumeration exists
    assert FontStyle is not None

def test_fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontStyle]
    expected_literals = [
        "Bold",
        "Default",
        "Italic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontStyle"

def test_nodefigure_exists():
    # Check that the Enumeration exists
    assert NodeFigure is not None

def test_nodefigure_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeFigure]
    expected_literals = [
        "Image",
        "Default",
        "Rectangle",
        "Ellipse",
        "SVG",
        "Polygon",
        "Rounded",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeFigure"

def test_brightness_exists():
    # Check that the Enumeration exists
    assert Brightness is not None

def test_brightness_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Brightness]
    expected_literals = [
        "Dark",
        "Default",
        "Light",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Brightness"

def test_placement_exists():
    # Check that the Enumeration exists
    assert Placement is not None

def test_placement_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Placement]
    expected_literals = [
        "Internal",
        "None_",
        "External",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Placement"

def test_linkfigure_exists():
    # Check that the Enumeration exists
    assert LinkFigure is not None

def test_linkfigure_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkFigure]
    expected_literals = [
        "Square",
        "Default",
        "Rhomb",
        "None_",
        "ClosedArrow",
        "FilledSquare",
        "Arrow",
        "FilledRhomb",
        "FilledClosedArrow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkFigure"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "Default",
        "Cyan",
        "Orange",
        "Gray",
        "White",
        "Yellow",
        "Red",
        "Green",
        "Black",
        "Blue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
cevinedit_Link_strategy = st.builds(
    cevinedit_Link,
    labelFontStyle=
        safe_text,
    width=
        st.integers(),
    targetDecoration=
        safe_text,
    label=
        safe_text,
    sourceDecoration=
        safe_text,
    brightness=
        safe_text,
    texture=
        safe_text,
    color=
        safe_text
)
cevinedit_NodeEClass_strategy = st.builds(
    cevinedit_NodeEClass,
    borderWidth=
        st.integers(),
    listPointsPolygon=
        safe_text,
    borderColor=
        safe_text,
    figure=
        safe_text,
    labelPlacement=
        safe_text,
    borderTexture=
        safe_text,
    size=
        safe_text,
    labelFontStyle=
        safe_text,
    backgroundColor=
        safe_text,
    brightness=
        safe_text,
    label=
        safe_text,
    imagePath=
        safe_text,
    resizable=
        st.booleans()
)
cevinedit_PersonalizedElement_strategy = st.builds(
    cevinedit_PersonalizedElement,
    icon=
        safe_text,
    name=
        safe_text
)
cevinedit_Diagram_strategy = st.builds(
    cevinedit_Diagram,
    modelExtension=
        safe_text,
    name=
        safe_text
)
cevinedit_CEViNEditRoot_strategy = st.builds(
    cevinedit_CEViNEditRoot,
    sourceMM=
        safe_text
)
cevinedit_LabelEAttribute_strategy = st.builds(
    cevinedit_LabelEAttribute,
)
cevinedit_AffixedEReferenceCont_strategy = st.builds(
    cevinedit_AffixedEReferenceCont,
)
cevinedit_CompartmentEReferenceCont_strategy = st.builds(
    cevinedit_CompartmentEReferenceCont,
    layout=
        safe_text,
    collapsible=
        st.booleans()
)
Link_strategy = st.builds(
    Link,
)
cevinedit_LinkEReferenceNonCont_strategy = st.builds(
    cevinedit_LinkEReferenceNonCont,
)
cevinedit_LinkEClass_strategy = st.builds(
    cevinedit_LinkEClass,
    source=
        safe_text,
    target=
        safe_text
)

@given(instance=PersonalizedElement_strategy)
@settings(max_examples=50)
def test_personalizedelement_instantiation(instance):
    assert isinstance(instance, PersonalizedElement)

@given(instance=cevinedit_Link_strategy)
@settings(max_examples=50)
def test_cevinedit_link_instantiation(instance):
    assert isinstance(instance, cevinedit_Link)



@given(instance=cevinedit_Link_strategy)
def test_cevinedit_link_labelFontStyle_setter(instance):
    original = instance.labelFontStyle
    instance.labelFontStyle = original
    assert instance.labelFontStyle == original



@given(instance=cevinedit_Link_strategy)
def test_cevinedit_link_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cevinedit_Link_strategy)
def test_cevinedit_link_targetDecoration_setter(instance):
    original = instance.targetDecoration
    instance.targetDecoration = original
    assert instance.targetDecoration == original



@given(instance=cevinedit_Link_strategy)
def test_cevinedit_link_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=cevinedit_Link_strategy)
def test_cevinedit_link_sourceDecoration_setter(instance):
    original = instance.sourceDecoration
    instance.sourceDecoration = original
    assert instance.sourceDecoration == original



@given(instance=cevinedit_Link_strategy)
def test_cevinedit_link_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original



@given(instance=cevinedit_Link_strategy)
def test_cevinedit_link_texture_setter(instance):
    original = instance.texture
    instance.texture = original
    assert instance.texture == original



@given(instance=cevinedit_Link_strategy)
def test_cevinedit_link_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=cevinedit_NodeEClass_strategy)
@settings(max_examples=50)
def test_cevinedit_nodeeclass_instantiation(instance):
    assert isinstance(instance, cevinedit_NodeEClass)



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_borderWidth_setter(instance):
    original = instance.borderWidth
    instance.borderWidth = original
    assert instance.borderWidth == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_listPointsPolygon_setter(instance):
    original = instance.listPointsPolygon
    instance.listPointsPolygon = original
    assert instance.listPointsPolygon == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_borderColor_setter(instance):
    original = instance.borderColor
    instance.borderColor = original
    assert instance.borderColor == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_figure_setter(instance):
    original = instance.figure
    instance.figure = original
    assert instance.figure == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_labelPlacement_setter(instance):
    original = instance.labelPlacement
    instance.labelPlacement = original
    assert instance.labelPlacement == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_borderTexture_setter(instance):
    original = instance.borderTexture
    instance.borderTexture = original
    assert instance.borderTexture == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_labelFontStyle_setter(instance):
    original = instance.labelFontStyle
    instance.labelFontStyle = original
    assert instance.labelFontStyle == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_imagePath_setter(instance):
    original = instance.imagePath
    instance.imagePath = original
    assert instance.imagePath == original



@given(instance=cevinedit_NodeEClass_strategy)
def test_cevinedit_nodeeclass_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original

@given(instance=cevinedit_PersonalizedElement_strategy)
@settings(max_examples=50)
def test_cevinedit_personalizedelement_instantiation(instance):
    assert isinstance(instance, cevinedit_PersonalizedElement)



@given(instance=cevinedit_PersonalizedElement_strategy)
def test_cevinedit_personalizedelement_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=cevinedit_PersonalizedElement_strategy)
def test_cevinedit_personalizedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cevinedit_Diagram_strategy)
@settings(max_examples=50)
def test_cevinedit_diagram_instantiation(instance):
    assert isinstance(instance, cevinedit_Diagram)



@given(instance=cevinedit_Diagram_strategy)
def test_cevinedit_diagram_modelExtension_setter(instance):
    original = instance.modelExtension
    instance.modelExtension = original
    assert instance.modelExtension == original



@given(instance=cevinedit_Diagram_strategy)
def test_cevinedit_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cevinedit_CEViNEditRoot_strategy)
@settings(max_examples=50)
def test_cevinedit_cevineditroot_instantiation(instance):
    assert isinstance(instance, cevinedit_CEViNEditRoot)



@given(instance=cevinedit_CEViNEditRoot_strategy)
def test_cevinedit_cevineditroot_sourceMM_setter(instance):
    original = instance.sourceMM
    instance.sourceMM = original
    assert instance.sourceMM == original

@given(instance=cevinedit_LabelEAttribute_strategy)
@settings(max_examples=50)
def test_cevinedit_labeleattribute_instantiation(instance):
    assert isinstance(instance, cevinedit_LabelEAttribute)

@given(instance=cevinedit_AffixedEReferenceCont_strategy)
@settings(max_examples=50)
def test_cevinedit_affixedereferencecont_instantiation(instance):
    assert isinstance(instance, cevinedit_AffixedEReferenceCont)

@given(instance=cevinedit_CompartmentEReferenceCont_strategy)
@settings(max_examples=50)
def test_cevinedit_compartmentereferencecont_instantiation(instance):
    assert isinstance(instance, cevinedit_CompartmentEReferenceCont)



@given(instance=cevinedit_CompartmentEReferenceCont_strategy)
def test_cevinedit_compartmentereferencecont_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original



@given(instance=cevinedit_CompartmentEReferenceCont_strategy)
def test_cevinedit_compartmentereferencecont_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original

@given(instance=Link_strategy)
@settings(max_examples=50)
def test_link_instantiation(instance):
    assert isinstance(instance, Link)

@given(instance=cevinedit_LinkEReferenceNonCont_strategy)
@settings(max_examples=50)
def test_cevinedit_linkereferencenoncont_instantiation(instance):
    assert isinstance(instance, cevinedit_LinkEReferenceNonCont)

@given(instance=cevinedit_LinkEClass_strategy)
@settings(max_examples=50)
def test_cevinedit_linkeclass_instantiation(instance):
    assert isinstance(instance, cevinedit_LinkEClass)



@given(instance=cevinedit_LinkEClass_strategy)
def test_cevinedit_linkeclass_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=cevinedit_LinkEClass_strategy)
def test_cevinedit_linkeclass_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original
