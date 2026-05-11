import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cs::CSPoint,
    cs::EClass,
    cs::CSLayout,
    cs::EStructuralFeature,
    cs::EObject,
    cs::CSTransform,
    CSNode,
    cs::CSTemplateDescription,
    cs::CSText,
    cs::CSConnectionEnd,
    cs::CSColor,
    cs::CSStroke,
    ENamedElement,
    cs::CSShape,
    cs::CSElement,
    CSElement,
    cs::CSNode,
    cs::CSConnection,
    cs::CSRoot,
    CSOrientation,
    CSFitType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cs::cspoint_is_not_abstract():
    assert not inspect.isabstract(cs::CSPoint)


def test_cs::cspoint_constructor_exists():
    assert callable(cs::CSPoint.__init__)


def test_cs::cspoint_constructor_args():
    sig = inspect.signature(cs::CSPoint.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_cs::cspoint_has_x():
    assert hasattr(cs::CSPoint, "x")
    descriptor = None
    for klass in cs::CSPoint.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_cs::cspoint_has_y():
    assert hasattr(cs::CSPoint, "y")
    descriptor = None
    for klass in cs::CSPoint.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_cs::eclass_is_not_abstract():
    assert not inspect.isabstract(cs::EClass)


def test_cs::eclass_constructor_exists():
    assert callable(cs::EClass.__init__)


def test_cs::eclass_constructor_args():
    sig = inspect.signature(cs::EClass.__init__)
    params = list(sig.parameters.keys())



def test_cs::cslayout_is_not_abstract():
    assert not inspect.isabstract(cs::CSLayout)


def test_cs::cslayout_constructor_exists():
    assert callable(cs::CSLayout.__init__)


def test_cs::cslayout_constructor_args():
    sig = inspect.signature(cs::CSLayout.__init__)
    params = list(sig.parameters.keys())



def test_cs::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(cs::EStructuralFeature)


def test_cs::estructuralfeature_constructor_exists():
    assert callable(cs::EStructuralFeature.__init__)


def test_cs::estructuralfeature_constructor_args():
    sig = inspect.signature(cs::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_cs::eobject_is_not_abstract():
    assert not inspect.isabstract(cs::EObject)


def test_cs::eobject_constructor_exists():
    assert callable(cs::EObject.__init__)


def test_cs::eobject_constructor_args():
    sig = inspect.signature(cs::EObject.__init__)
    params = list(sig.parameters.keys())



def test_cs::cstransform_is_not_abstract():
    assert not inspect.isabstract(cs::CSTransform)


def test_cs::cstransform_constructor_exists():
    assert callable(cs::CSTransform.__init__)


def test_cs::cstransform_constructor_args():
    sig = inspect.signature(cs::CSTransform.__init__)
    params = list(sig.parameters.keys())
    assert "m21" in params, "Missing parameter 'm21'"
    assert "m11" in params, "Missing parameter 'm11'"
    assert "m01" in params, "Missing parameter 'm01'"
    assert "m12" in params, "Missing parameter 'm12'"
    assert "m00" in params, "Missing parameter 'm00'"
    assert "m02" in params, "Missing parameter 'm02'"
    assert "m22" in params, "Missing parameter 'm22'"
    assert "m10" in params, "Missing parameter 'm10'"
    assert "m20" in params, "Missing parameter 'm20'"

def test_cs::cstransform_has_m21():
    assert hasattr(cs::CSTransform, "m21")
    descriptor = None
    for klass in cs::CSTransform.__mro__:
        if "m21" in klass.__dict__:
            descriptor = klass.__dict__["m21"]
            break
    assert isinstance(descriptor, property)

def test_cs::cstransform_has_m11():
    assert hasattr(cs::CSTransform, "m11")
    descriptor = None
    for klass in cs::CSTransform.__mro__:
        if "m11" in klass.__dict__:
            descriptor = klass.__dict__["m11"]
            break
    assert isinstance(descriptor, property)

def test_cs::cstransform_has_m01():
    assert hasattr(cs::CSTransform, "m01")
    descriptor = None
    for klass in cs::CSTransform.__mro__:
        if "m01" in klass.__dict__:
            descriptor = klass.__dict__["m01"]
            break
    assert isinstance(descriptor, property)

def test_cs::cstransform_has_m12():
    assert hasattr(cs::CSTransform, "m12")
    descriptor = None
    for klass in cs::CSTransform.__mro__:
        if "m12" in klass.__dict__:
            descriptor = klass.__dict__["m12"]
            break
    assert isinstance(descriptor, property)

def test_cs::cstransform_has_m00():
    assert hasattr(cs::CSTransform, "m00")
    descriptor = None
    for klass in cs::CSTransform.__mro__:
        if "m00" in klass.__dict__:
            descriptor = klass.__dict__["m00"]
            break
    assert isinstance(descriptor, property)

def test_cs::cstransform_has_m02():
    assert hasattr(cs::CSTransform, "m02")
    descriptor = None
    for klass in cs::CSTransform.__mro__:
        if "m02" in klass.__dict__:
            descriptor = klass.__dict__["m02"]
            break
    assert isinstance(descriptor, property)

def test_cs::cstransform_has_m22():
    assert hasattr(cs::CSTransform, "m22")
    descriptor = None
    for klass in cs::CSTransform.__mro__:
        if "m22" in klass.__dict__:
            descriptor = klass.__dict__["m22"]
            break
    assert isinstance(descriptor, property)

def test_cs::cstransform_has_m10():
    assert hasattr(cs::CSTransform, "m10")
    descriptor = None
    for klass in cs::CSTransform.__mro__:
        if "m10" in klass.__dict__:
            descriptor = klass.__dict__["m10"]
            break
    assert isinstance(descriptor, property)

def test_cs::cstransform_has_m20():
    assert hasattr(cs::CSTransform, "m20")
    descriptor = None
    for klass in cs::CSTransform.__mro__:
        if "m20" in klass.__dict__:
            descriptor = klass.__dict__["m20"]
            break
    assert isinstance(descriptor, property)



def test_csnode_is_not_abstract():
    assert not inspect.isabstract(CSNode)


def test_csnode_constructor_exists():
    assert callable(CSNode.__init__)


def test_csnode_constructor_args():
    sig = inspect.signature(CSNode.__init__)
    params = list(sig.parameters.keys())



def test_cs::cstemplatedescription_is_not_abstract():
    assert not inspect.isabstract(cs::CSTemplateDescription)


def test_cs::cstemplatedescription_constructor_exists():
    assert callable(cs::CSTemplateDescription.__init__)


def test_cs::cstemplatedescription_constructor_args():
    sig = inspect.signature(cs::CSTemplateDescription.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"

def test_cs::cstemplatedescription_has_scale():
    assert hasattr(cs::CSTemplateDescription, "scale")
    descriptor = None
    for klass in cs::CSTemplateDescription.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_cs::cstext_is_not_abstract():
    assert not inspect.isabstract(cs::CSText)


def test_cs::cstext_constructor_exists():
    assert callable(cs::CSText.__init__)


def test_cs::cstext_constructor_args():
    sig = inspect.signature(cs::CSText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_cs::cstext_has_text():
    assert hasattr(cs::CSText, "text")
    descriptor = None
    for klass in cs::CSText.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_cs::csconnectionend_is_not_abstract():
    assert not inspect.isabstract(cs::CSConnectionEnd)


def test_cs::csconnectionend_constructor_exists():
    assert callable(cs::CSConnectionEnd.__init__)


def test_cs::csconnectionend_constructor_args():
    sig = inspect.signature(cs::CSConnectionEnd.__init__)
    params = list(sig.parameters.keys())
    assert "tipType" in params, "Missing parameter 'tipType'"

def test_cs::csconnectionend_has_tipType():
    assert hasattr(cs::CSConnectionEnd, "tipType")
    descriptor = None
    for klass in cs::CSConnectionEnd.__mro__:
        if "tipType" in klass.__dict__:
            descriptor = klass.__dict__["tipType"]
            break
    assert isinstance(descriptor, property)



def test_cs::cscolor_is_not_abstract():
    assert not inspect.isabstract(cs::CSColor)


def test_cs::cscolor_constructor_exists():
    assert callable(cs::CSColor.__init__)


def test_cs::cscolor_constructor_args():
    sig = inspect.signature(cs::CSColor.__init__)
    params = list(sig.parameters.keys())
    assert "r" in params, "Missing parameter 'r'"
    assert "a" in params, "Missing parameter 'a'"
    assert "g" in params, "Missing parameter 'g'"
    assert "b" in params, "Missing parameter 'b'"

def test_cs::cscolor_has_r():
    assert hasattr(cs::CSColor, "r")
    descriptor = None
    for klass in cs::CSColor.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_cs::cscolor_has_a():
    assert hasattr(cs::CSColor, "a")
    descriptor = None
    for klass in cs::CSColor.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_cs::cscolor_has_g():
    assert hasattr(cs::CSColor, "g")
    descriptor = None
    for klass in cs::CSColor.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_cs::cscolor_has_b():
    assert hasattr(cs::CSColor, "b")
    descriptor = None
    for klass in cs::CSColor.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_cs::csstroke_is_not_abstract():
    assert not inspect.isabstract(cs::CSStroke)


def test_cs::csstroke_constructor_exists():
    assert callable(cs::CSStroke.__init__)


def test_cs::csstroke_constructor_args():
    sig = inspect.signature(cs::CSStroke.__init__)
    params = list(sig.parameters.keys())
    assert "dash_phase" in params, "Missing parameter 'dash_phase'"
    assert "width" in params, "Missing parameter 'width'"
    assert "join" in params, "Missing parameter 'join'"
    assert "cap" in params, "Missing parameter 'cap'"
    assert "miterlimit" in params, "Missing parameter 'miterlimit'"
    assert "dash" in params, "Missing parameter 'dash'"

def test_cs::csstroke_has_dash_phase():
    assert hasattr(cs::CSStroke, "dash_phase")
    descriptor = None
    for klass in cs::CSStroke.__mro__:
        if "dash_phase" in klass.__dict__:
            descriptor = klass.__dict__["dash_phase"]
            break
    assert isinstance(descriptor, property)

def test_cs::csstroke_has_width():
    assert hasattr(cs::CSStroke, "width")
    descriptor = None
    for klass in cs::CSStroke.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_cs::csstroke_has_join():
    assert hasattr(cs::CSStroke, "join")
    descriptor = None
    for klass in cs::CSStroke.__mro__:
        if "join" in klass.__dict__:
            descriptor = klass.__dict__["join"]
            break
    assert isinstance(descriptor, property)

def test_cs::csstroke_has_cap():
    assert hasattr(cs::CSStroke, "cap")
    descriptor = None
    for klass in cs::CSStroke.__mro__:
        if "cap" in klass.__dict__:
            descriptor = klass.__dict__["cap"]
            break
    assert isinstance(descriptor, property)

def test_cs::csstroke_has_miterlimit():
    assert hasattr(cs::CSStroke, "miterlimit")
    descriptor = None
    for klass in cs::CSStroke.__mro__:
        if "miterlimit" in klass.__dict__:
            descriptor = klass.__dict__["miterlimit"]
            break
    assert isinstance(descriptor, property)

def test_cs::csstroke_has_dash():
    assert hasattr(cs::CSStroke, "dash")
    descriptor = None
    for klass in cs::CSStroke.__mro__:
        if "dash" in klass.__dict__:
            descriptor = klass.__dict__["dash"]
            break
    assert isinstance(descriptor, property)



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_cs::csshape_is_not_abstract():
    assert not inspect.isabstract(cs::CSShape)


def test_cs::csshape_constructor_exists():
    assert callable(cs::CSShape.__init__)


def test_cs::csshape_constructor_args():
    sig = inspect.signature(cs::CSShape.__init__)
    params = list(sig.parameters.keys())
    assert "closed" in params, "Missing parameter 'closed'"

def test_cs::csshape_has_closed():
    assert hasattr(cs::CSShape, "closed")
    descriptor = None
    for klass in cs::CSShape.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)



def test_cs::cselement_is_not_abstract():
    assert not inspect.isabstract(cs::CSElement)


def test_cs::cselement_constructor_exists():
    assert callable(cs::CSElement.__init__)


def test_cs::cselement_constructor_args():
    sig = inspect.signature(cs::CSElement.__init__)
    params = list(sig.parameters.keys())
    assert "minZoom" in params, "Missing parameter 'minZoom'"
    assert "resizable" in params, "Missing parameter 'resizable'"
    assert "selectable" in params, "Missing parameter 'selectable'"
    assert "maxZoom" in params, "Missing parameter 'maxZoom'"
    assert "templateRoot" in params, "Missing parameter 'templateRoot'"
    assert "draggable" in params, "Missing parameter 'draggable'"

def test_cs::cselement_has_minZoom():
    assert hasattr(cs::CSElement, "minZoom")
    descriptor = None
    for klass in cs::CSElement.__mro__:
        if "minZoom" in klass.__dict__:
            descriptor = klass.__dict__["minZoom"]
            break
    assert isinstance(descriptor, property)

def test_cs::cselement_has_resizable():
    assert hasattr(cs::CSElement, "resizable")
    descriptor = None
    for klass in cs::CSElement.__mro__:
        if "resizable" in klass.__dict__:
            descriptor = klass.__dict__["resizable"]
            break
    assert isinstance(descriptor, property)

def test_cs::cselement_has_selectable():
    assert hasattr(cs::CSElement, "selectable")
    descriptor = None
    for klass in cs::CSElement.__mro__:
        if "selectable" in klass.__dict__:
            descriptor = klass.__dict__["selectable"]
            break
    assert isinstance(descriptor, property)

def test_cs::cselement_has_maxZoom():
    assert hasattr(cs::CSElement, "maxZoom")
    descriptor = None
    for klass in cs::CSElement.__mro__:
        if "maxZoom" in klass.__dict__:
            descriptor = klass.__dict__["maxZoom"]
            break
    assert isinstance(descriptor, property)

def test_cs::cselement_has_templateRoot():
    assert hasattr(cs::CSElement, "templateRoot")
    descriptor = None
    for klass in cs::CSElement.__mro__:
        if "templateRoot" in klass.__dict__:
            descriptor = klass.__dict__["templateRoot"]
            break
    assert isinstance(descriptor, property)

def test_cs::cselement_has_draggable():
    assert hasattr(cs::CSElement, "draggable")
    descriptor = None
    for klass in cs::CSElement.__mro__:
        if "draggable" in klass.__dict__:
            descriptor = klass.__dict__["draggable"]
            break
    assert isinstance(descriptor, property)



def test_cselement_is_not_abstract():
    assert not inspect.isabstract(CSElement)


def test_cselement_constructor_exists():
    assert callable(CSElement.__init__)


def test_cselement_constructor_args():
    sig = inspect.signature(CSElement.__init__)
    params = list(sig.parameters.keys())



def test_cs::csnode_is_not_abstract():
    assert not inspect.isabstract(cs::CSNode)


def test_cs::csnode_constructor_exists():
    assert callable(cs::CSNode.__init__)


def test_cs::csnode_constructor_args():
    sig = inspect.signature(cs::CSNode.__init__)
    params = list(sig.parameters.keys())
    assert "minWidth" in params, "Missing parameter 'minWidth'"
    assert "x" in params, "Missing parameter 'x'"
    assert "widthRatioToParent" in params, "Missing parameter 'widthRatioToParent'"
    assert "maxWidth" in params, "Missing parameter 'maxWidth'"
    assert "maxHeight" in params, "Missing parameter 'maxHeight'"
    assert "heightRatioToParent" in params, "Missing parameter 'heightRatioToParent'"
    assert "minHeight" in params, "Missing parameter 'minHeight'"
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "verticalAlign" in params, "Missing parameter 'verticalAlign'"
    assert "horizontalAlign" in params, "Missing parameter 'horizontalAlign'"

def test_cs::csnode_has_minWidth():
    assert hasattr(cs::CSNode, "minWidth")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "minWidth" in klass.__dict__:
            descriptor = klass.__dict__["minWidth"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_x():
    assert hasattr(cs::CSNode, "x")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_widthRatioToParent():
    assert hasattr(cs::CSNode, "widthRatioToParent")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "widthRatioToParent" in klass.__dict__:
            descriptor = klass.__dict__["widthRatioToParent"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_maxWidth():
    assert hasattr(cs::CSNode, "maxWidth")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "maxWidth" in klass.__dict__:
            descriptor = klass.__dict__["maxWidth"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_maxHeight():
    assert hasattr(cs::CSNode, "maxHeight")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "maxHeight" in klass.__dict__:
            descriptor = klass.__dict__["maxHeight"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_heightRatioToParent():
    assert hasattr(cs::CSNode, "heightRatioToParent")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "heightRatioToParent" in klass.__dict__:
            descriptor = klass.__dict__["heightRatioToParent"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_minHeight():
    assert hasattr(cs::CSNode, "minHeight")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "minHeight" in klass.__dict__:
            descriptor = klass.__dict__["minHeight"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_y():
    assert hasattr(cs::CSNode, "y")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_width():
    assert hasattr(cs::CSNode, "width")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_height():
    assert hasattr(cs::CSNode, "height")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_verticalAlign():
    assert hasattr(cs::CSNode, "verticalAlign")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "verticalAlign" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlign"]
            break
    assert isinstance(descriptor, property)

def test_cs::csnode_has_horizontalAlign():
    assert hasattr(cs::CSNode, "horizontalAlign")
    descriptor = None
    for klass in cs::CSNode.__mro__:
        if "horizontalAlign" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlign"]
            break
    assert isinstance(descriptor, property)



def test_cs::csconnection_is_not_abstract():
    assert not inspect.isabstract(cs::CSConnection)


def test_cs::csconnection_constructor_exists():
    assert callable(cs::CSConnection.__init__)


def test_cs::csconnection_constructor_args():
    sig = inspect.signature(cs::CSConnection.__init__)
    params = list(sig.parameters.keys())



def test_cs::csroot_is_not_abstract():
    assert not inspect.isabstract(cs::CSRoot)


def test_cs::csroot_constructor_exists():
    assert callable(cs::CSRoot.__init__)


def test_cs::csroot_constructor_args():
    sig = inspect.signature(cs::CSRoot.__init__)
    params = list(sig.parameters.keys())

def test_csorientation_exists():
    # Check that the Enumeration exists
    assert CSOrientation is not None

def test_csorientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSOrientation]
    expected_literals = [
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSOrientation"

def test_csfittype_exists():
    # Check that the Enumeration exists
    assert CSFitType is not None

def test_csfittype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSFitType]
    expected_literals = [
        "AUTO_EXPAND",
        "FIT_TO_CHILDREN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSFitType"


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
cs::CSPoint_strategy = st.builds(
    cs::CSPoint,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cs::EClass_strategy = st.builds(
    cs::EClass,
)
cs::CSLayout_strategy = st.builds(
    cs::CSLayout,
)
cs::EStructuralFeature_strategy = st.builds(
    cs::EStructuralFeature,
)
cs::EObject_strategy = st.builds(
    cs::EObject,
)
cs::CSTransform_strategy = st.builds(
    cs::CSTransform,
    m21=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m11=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m01=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m12=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m00=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m02=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m22=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m10=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m20=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CSNode_strategy = st.builds(
    CSNode,
)
cs::CSTemplateDescription_strategy = st.builds(
    cs::CSTemplateDescription,
    scale=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cs::CSText_strategy = st.builds(
    cs::CSText,
    text=
        safe_text
)
cs::CSConnectionEnd_strategy = st.builds(
    cs::CSConnectionEnd,
    tipType=
        st.integers()
)
cs::CSColor_strategy = st.builds(
    cs::CSColor,
    r=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    a=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    g=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    b=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cs::CSStroke_strategy = st.builds(
    cs::CSStroke,
    dash_phase=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    join=
        st.integers(),
    cap=
        st.integers(),
    miterlimit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    dash=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
cs::CSShape_strategy = st.builds(
    cs::CSShape,
    closed=
        st.booleans()
)
cs::CSElement_strategy = st.builds(
    cs::CSElement,
    minZoom=
        safe_text,
    resizable=
        st.booleans(),
    selectable=
        safe_text,
    maxZoom=
        safe_text,
    templateRoot=
        st.booleans(),
    draggable=
        st.booleans()
)
CSElement_strategy = st.builds(
    CSElement,
)
cs::CSNode_strategy = st.builds(
    cs::CSNode,
    minWidth=
        safe_text,
    x=
        safe_text,
    widthRatioToParent=
        safe_text,
    maxWidth=
        safe_text,
    maxHeight=
        safe_text,
    heightRatioToParent=
        safe_text,
    minHeight=
        safe_text,
    y=
        safe_text,
    width=
        safe_text,
    height=
        safe_text,
    verticalAlign=
        safe_text,
    horizontalAlign=
        safe_text
)
cs::CSConnection_strategy = st.builds(
    cs::CSConnection,
)
cs::CSRoot_strategy = st.builds(
    cs::CSRoot,
)

@given(instance=cs::CSPoint_strategy)
@settings(max_examples=50)
def test_cs::cspoint_instantiation(instance):
    assert isinstance(instance, cs::CSPoint)

@given(instance=cs::CSPoint_strategy)
def test_cs::cspoint_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=cs::CSPoint_strategy)
def test_cs::cspoint_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=cs::CSPoint_strategy)
def test_cs::cspoint_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=cs::CSPoint_strategy)
def test_cs::cspoint_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=cs::EClass_strategy)
@settings(max_examples=50)
def test_cs::eclass_instantiation(instance):
    assert isinstance(instance, cs::EClass)

@given(instance=cs::CSLayout_strategy)
@settings(max_examples=50)
def test_cs::cslayout_instantiation(instance):
    assert isinstance(instance, cs::CSLayout)

@given(instance=cs::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_cs::estructuralfeature_instantiation(instance):
    assert isinstance(instance, cs::EStructuralFeature)

@given(instance=cs::EObject_strategy)
@settings(max_examples=50)
def test_cs::eobject_instantiation(instance):
    assert isinstance(instance, cs::EObject)

@given(instance=cs::CSTransform_strategy)
@settings(max_examples=50)
def test_cs::cstransform_instantiation(instance):
    assert isinstance(instance, cs::CSTransform)

@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m21_type(instance):
    assert isinstance(instance.m21, float)


@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m21_setter(instance):
    original = instance.m21
    instance.m21 = original
    assert instance.m21 == original

@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m11_type(instance):
    assert isinstance(instance.m11, float)


@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m11_setter(instance):
    original = instance.m11
    instance.m11 = original
    assert instance.m11 == original

@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m01_type(instance):
    assert isinstance(instance.m01, float)


@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m01_setter(instance):
    original = instance.m01
    instance.m01 = original
    assert instance.m01 == original

@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m12_type(instance):
    assert isinstance(instance.m12, float)


@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m12_setter(instance):
    original = instance.m12
    instance.m12 = original
    assert instance.m12 == original

@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m00_type(instance):
    assert isinstance(instance.m00, float)


@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m00_setter(instance):
    original = instance.m00
    instance.m00 = original
    assert instance.m00 == original

@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m02_type(instance):
    assert isinstance(instance.m02, float)


@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m02_setter(instance):
    original = instance.m02
    instance.m02 = original
    assert instance.m02 == original

@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m22_type(instance):
    assert isinstance(instance.m22, float)


@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m22_setter(instance):
    original = instance.m22
    instance.m22 = original
    assert instance.m22 == original

@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m10_type(instance):
    assert isinstance(instance.m10, float)


@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m10_setter(instance):
    original = instance.m10
    instance.m10 = original
    assert instance.m10 == original

@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m20_type(instance):
    assert isinstance(instance.m20, float)


@given(instance=cs::CSTransform_strategy)
def test_cs::cstransform_m20_setter(instance):
    original = instance.m20
    instance.m20 = original
    assert instance.m20 == original

@given(instance=CSNode_strategy)
@settings(max_examples=50)
def test_csnode_instantiation(instance):
    assert isinstance(instance, CSNode)

@given(instance=cs::CSTemplateDescription_strategy)
@settings(max_examples=50)
def test_cs::cstemplatedescription_instantiation(instance):
    assert isinstance(instance, cs::CSTemplateDescription)

@given(instance=cs::CSTemplateDescription_strategy)
def test_cs::cstemplatedescription_scale_type(instance):
    assert isinstance(instance.scale, float)


@given(instance=cs::CSTemplateDescription_strategy)
def test_cs::cstemplatedescription_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=cs::CSText_strategy)
@settings(max_examples=50)
def test_cs::cstext_instantiation(instance):
    assert isinstance(instance, cs::CSText)

@given(instance=cs::CSText_strategy)
def test_cs::cstext_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=cs::CSText_strategy)
def test_cs::cstext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=cs::CSConnectionEnd_strategy)
@settings(max_examples=50)
def test_cs::csconnectionend_instantiation(instance):
    assert isinstance(instance, cs::CSConnectionEnd)

@given(instance=cs::CSConnectionEnd_strategy)
def test_cs::csconnectionend_tipType_type(instance):
    assert isinstance(instance.tipType, int)


@given(instance=cs::CSConnectionEnd_strategy)
def test_cs::csconnectionend_tipType_setter(instance):
    original = instance.tipType
    instance.tipType = original
    assert instance.tipType == original

@given(instance=cs::CSColor_strategy)
@settings(max_examples=50)
def test_cs::cscolor_instantiation(instance):
    assert isinstance(instance, cs::CSColor)

@given(instance=cs::CSColor_strategy)
def test_cs::cscolor_r_type(instance):
    assert isinstance(instance.r, float)


@given(instance=cs::CSColor_strategy)
def test_cs::cscolor_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original

@given(instance=cs::CSColor_strategy)
def test_cs::cscolor_a_type(instance):
    assert isinstance(instance.a, float)


@given(instance=cs::CSColor_strategy)
def test_cs::cscolor_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=cs::CSColor_strategy)
def test_cs::cscolor_g_type(instance):
    assert isinstance(instance.g, float)


@given(instance=cs::CSColor_strategy)
def test_cs::cscolor_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original

@given(instance=cs::CSColor_strategy)
def test_cs::cscolor_b_type(instance):
    assert isinstance(instance.b, float)


@given(instance=cs::CSColor_strategy)
def test_cs::cscolor_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=cs::CSStroke_strategy)
@settings(max_examples=50)
def test_cs::csstroke_instantiation(instance):
    assert isinstance(instance, cs::CSStroke)

@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_dash_phase_type(instance):
    assert isinstance(instance.dash_phase, float)


@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_dash_phase_setter(instance):
    original = instance.dash_phase
    instance.dash_phase = original
    assert instance.dash_phase == original

@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_join_type(instance):
    assert isinstance(instance.join, int)


@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original

@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_cap_type(instance):
    assert isinstance(instance.cap, int)


@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_cap_setter(instance):
    original = instance.cap
    instance.cap = original
    assert instance.cap == original

@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_miterlimit_type(instance):
    assert isinstance(instance.miterlimit, float)


@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_miterlimit_setter(instance):
    original = instance.miterlimit
    instance.miterlimit = original
    assert instance.miterlimit == original

@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_dash_type(instance):
    assert isinstance(instance.dash, float)


@given(instance=cs::CSStroke_strategy)
def test_cs::csstroke_dash_setter(instance):
    original = instance.dash
    instance.dash = original
    assert instance.dash == original

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=cs::CSShape_strategy)
@settings(max_examples=50)
def test_cs::csshape_instantiation(instance):
    assert isinstance(instance, cs::CSShape)

@given(instance=cs::CSShape_strategy)
def test_cs::csshape_closed_type(instance):
    assert isinstance(instance.closed, bool)


@given(instance=cs::CSShape_strategy)
def test_cs::csshape_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original

@given(instance=cs::CSElement_strategy)
@settings(max_examples=50)
def test_cs::cselement_instantiation(instance):
    assert isinstance(instance, cs::CSElement)

@given(instance=cs::CSElement_strategy)
def test_cs::cselement_minZoom_type(instance):
    assert isinstance(instance.minZoom, str)


@given(instance=cs::CSElement_strategy)
def test_cs::cselement_minZoom_setter(instance):
    original = instance.minZoom
    instance.minZoom = original
    assert instance.minZoom == original

@given(instance=cs::CSElement_strategy)
def test_cs::cselement_resizable_type(instance):
    assert isinstance(instance.resizable, bool)


@given(instance=cs::CSElement_strategy)
def test_cs::cselement_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original

@given(instance=cs::CSElement_strategy)
def test_cs::cselement_selectable_type(instance):
    assert isinstance(instance.selectable, str)


@given(instance=cs::CSElement_strategy)
def test_cs::cselement_selectable_setter(instance):
    original = instance.selectable
    instance.selectable = original
    assert instance.selectable == original

@given(instance=cs::CSElement_strategy)
def test_cs::cselement_maxZoom_type(instance):
    assert isinstance(instance.maxZoom, str)


@given(instance=cs::CSElement_strategy)
def test_cs::cselement_maxZoom_setter(instance):
    original = instance.maxZoom
    instance.maxZoom = original
    assert instance.maxZoom == original

@given(instance=cs::CSElement_strategy)
def test_cs::cselement_templateRoot_type(instance):
    assert isinstance(instance.templateRoot, bool)


@given(instance=cs::CSElement_strategy)
def test_cs::cselement_templateRoot_setter(instance):
    original = instance.templateRoot
    instance.templateRoot = original
    assert instance.templateRoot == original

@given(instance=cs::CSElement_strategy)
def test_cs::cselement_draggable_type(instance):
    assert isinstance(instance.draggable, bool)


@given(instance=cs::CSElement_strategy)
def test_cs::cselement_draggable_setter(instance):
    original = instance.draggable
    instance.draggable = original
    assert instance.draggable == original

@given(instance=CSElement_strategy)
@settings(max_examples=50)
def test_cselement_instantiation(instance):
    assert isinstance(instance, CSElement)

@given(instance=cs::CSNode_strategy)
@settings(max_examples=50)
def test_cs::csnode_instantiation(instance):
    assert isinstance(instance, cs::CSNode)

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_minWidth_type(instance):
    assert isinstance(instance.minWidth, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_minWidth_setter(instance):
    original = instance.minWidth
    instance.minWidth = original
    assert instance.minWidth == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_widthRatioToParent_type(instance):
    assert isinstance(instance.widthRatioToParent, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_widthRatioToParent_setter(instance):
    original = instance.widthRatioToParent
    instance.widthRatioToParent = original
    assert instance.widthRatioToParent == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_maxWidth_type(instance):
    assert isinstance(instance.maxWidth, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_maxWidth_setter(instance):
    original = instance.maxWidth
    instance.maxWidth = original
    assert instance.maxWidth == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_maxHeight_type(instance):
    assert isinstance(instance.maxHeight, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_maxHeight_setter(instance):
    original = instance.maxHeight
    instance.maxHeight = original
    assert instance.maxHeight == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_heightRatioToParent_type(instance):
    assert isinstance(instance.heightRatioToParent, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_heightRatioToParent_setter(instance):
    original = instance.heightRatioToParent
    instance.heightRatioToParent = original
    assert instance.heightRatioToParent == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_minHeight_type(instance):
    assert isinstance(instance.minHeight, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_minHeight_setter(instance):
    original = instance.minHeight
    instance.minHeight = original
    assert instance.minHeight == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_verticalAlign_type(instance):
    assert isinstance(instance.verticalAlign, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_verticalAlign_setter(instance):
    original = instance.verticalAlign
    instance.verticalAlign = original
    assert instance.verticalAlign == original

@given(instance=cs::CSNode_strategy)
def test_cs::csnode_horizontalAlign_type(instance):
    assert isinstance(instance.horizontalAlign, str)


@given(instance=cs::CSNode_strategy)
def test_cs::csnode_horizontalAlign_setter(instance):
    original = instance.horizontalAlign
    instance.horizontalAlign = original
    assert instance.horizontalAlign == original

@given(instance=cs::CSConnection_strategy)
@settings(max_examples=50)
def test_cs::csconnection_instantiation(instance):
    assert isinstance(instance, cs::CSConnection)

@given(instance=cs::CSRoot_strategy)
@settings(max_examples=50)
def test_cs::csroot_instantiation(instance):
    assert isinstance(instance, cs::CSRoot)
