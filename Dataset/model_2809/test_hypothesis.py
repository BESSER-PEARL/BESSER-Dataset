import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cs_CSPoint,
    cs_EClass,
    cs_CSLayout,
    cs_EStructuralFeature,
    cs_EObject,
    cs_CSTransform,
    CSNode,
    cs_CSTemplateDescription,
    cs_CSText,
    cs_CSConnectionEnd,
    cs_CSColor,
    cs_CSStroke,
    ENamedElement,
    cs_CSShape,
    cs_CSElement,
    CSElement,
    cs_CSNode,
    cs_CSConnection,
    cs_CSRoot,
    CSOrientation,
    CSFitType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cs_cspoint_is_not_abstract():
    assert not inspect.isabstract(cs_CSPoint)


def test_cs_cspoint_constructor_exists():
    assert callable(cs_CSPoint.__init__)


def test_cs_cspoint_constructor_args():
    sig = inspect.signature(cs_CSPoint.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_cs_cspoint_has_x():
    assert hasattr(cs_CSPoint, "x")
    descriptor = None
    for klass in cs_CSPoint.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_cs_cspoint_has_y():
    assert hasattr(cs_CSPoint, "y")
    descriptor = None
    for klass in cs_CSPoint.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_cs_eclass_is_not_abstract():
    assert not inspect.isabstract(cs_EClass)


def test_cs_eclass_constructor_exists():
    assert callable(cs_EClass.__init__)


def test_cs_eclass_constructor_args():
    sig = inspect.signature(cs_EClass.__init__)
    params = list(sig.parameters.keys())



def test_cs_cslayout_is_not_abstract():
    assert not inspect.isabstract(cs_CSLayout)


def test_cs_cslayout_constructor_exists():
    assert callable(cs_CSLayout.__init__)


def test_cs_cslayout_constructor_args():
    sig = inspect.signature(cs_CSLayout.__init__)
    params = list(sig.parameters.keys())



def test_cs_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(cs_EStructuralFeature)


def test_cs_estructuralfeature_constructor_exists():
    assert callable(cs_EStructuralFeature.__init__)


def test_cs_estructuralfeature_constructor_args():
    sig = inspect.signature(cs_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_cs_eobject_is_not_abstract():
    assert not inspect.isabstract(cs_EObject)


def test_cs_eobject_constructor_exists():
    assert callable(cs_EObject.__init__)


def test_cs_eobject_constructor_args():
    sig = inspect.signature(cs_EObject.__init__)
    params = list(sig.parameters.keys())



def test_cs_cstransform_is_not_abstract():
    assert not inspect.isabstract(cs_CSTransform)


def test_cs_cstransform_constructor_exists():
    assert callable(cs_CSTransform.__init__)


def test_cs_cstransform_constructor_args():
    sig = inspect.signature(cs_CSTransform.__init__)
    params = list(sig.parameters.keys())
    assert "m12" in params, "Missing parameter 'm12'"
    assert "m10" in params, "Missing parameter 'm10'"
    assert "m02" in params, "Missing parameter 'm02'"
    assert "m20" in params, "Missing parameter 'm20'"
    assert "m01" in params, "Missing parameter 'm01'"
    assert "m21" in params, "Missing parameter 'm21'"
    assert "m22" in params, "Missing parameter 'm22'"
    assert "m00" in params, "Missing parameter 'm00'"
    assert "m11" in params, "Missing parameter 'm11'"

def test_cs_cstransform_has_m12():
    assert hasattr(cs_CSTransform, "m12")
    descriptor = None
    for klass in cs_CSTransform.__mro__:
        if "m12" in klass.__dict__:
            descriptor = klass.__dict__["m12"]
            break
    assert isinstance(descriptor, property)

def test_cs_cstransform_has_m10():
    assert hasattr(cs_CSTransform, "m10")
    descriptor = None
    for klass in cs_CSTransform.__mro__:
        if "m10" in klass.__dict__:
            descriptor = klass.__dict__["m10"]
            break
    assert isinstance(descriptor, property)

def test_cs_cstransform_has_m02():
    assert hasattr(cs_CSTransform, "m02")
    descriptor = None
    for klass in cs_CSTransform.__mro__:
        if "m02" in klass.__dict__:
            descriptor = klass.__dict__["m02"]
            break
    assert isinstance(descriptor, property)

def test_cs_cstransform_has_m20():
    assert hasattr(cs_CSTransform, "m20")
    descriptor = None
    for klass in cs_CSTransform.__mro__:
        if "m20" in klass.__dict__:
            descriptor = klass.__dict__["m20"]
            break
    assert isinstance(descriptor, property)

def test_cs_cstransform_has_m01():
    assert hasattr(cs_CSTransform, "m01")
    descriptor = None
    for klass in cs_CSTransform.__mro__:
        if "m01" in klass.__dict__:
            descriptor = klass.__dict__["m01"]
            break
    assert isinstance(descriptor, property)

def test_cs_cstransform_has_m21():
    assert hasattr(cs_CSTransform, "m21")
    descriptor = None
    for klass in cs_CSTransform.__mro__:
        if "m21" in klass.__dict__:
            descriptor = klass.__dict__["m21"]
            break
    assert isinstance(descriptor, property)

def test_cs_cstransform_has_m22():
    assert hasattr(cs_CSTransform, "m22")
    descriptor = None
    for klass in cs_CSTransform.__mro__:
        if "m22" in klass.__dict__:
            descriptor = klass.__dict__["m22"]
            break
    assert isinstance(descriptor, property)

def test_cs_cstransform_has_m00():
    assert hasattr(cs_CSTransform, "m00")
    descriptor = None
    for klass in cs_CSTransform.__mro__:
        if "m00" in klass.__dict__:
            descriptor = klass.__dict__["m00"]
            break
    assert isinstance(descriptor, property)

def test_cs_cstransform_has_m11():
    assert hasattr(cs_CSTransform, "m11")
    descriptor = None
    for klass in cs_CSTransform.__mro__:
        if "m11" in klass.__dict__:
            descriptor = klass.__dict__["m11"]
            break
    assert isinstance(descriptor, property)



def test_csnode_is_not_abstract():
    assert not inspect.isabstract(CSNode)


def test_csnode_constructor_exists():
    assert callable(CSNode.__init__)


def test_csnode_constructor_args():
    sig = inspect.signature(CSNode.__init__)
    params = list(sig.parameters.keys())



def test_cs_cstemplatedescription_is_not_abstract():
    assert not inspect.isabstract(cs_CSTemplateDescription)


def test_cs_cstemplatedescription_constructor_exists():
    assert callable(cs_CSTemplateDescription.__init__)


def test_cs_cstemplatedescription_constructor_args():
    sig = inspect.signature(cs_CSTemplateDescription.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"

def test_cs_cstemplatedescription_has_scale():
    assert hasattr(cs_CSTemplateDescription, "scale")
    descriptor = None
    for klass in cs_CSTemplateDescription.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_cs_cstext_is_not_abstract():
    assert not inspect.isabstract(cs_CSText)


def test_cs_cstext_constructor_exists():
    assert callable(cs_CSText.__init__)


def test_cs_cstext_constructor_args():
    sig = inspect.signature(cs_CSText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_cs_cstext_has_text():
    assert hasattr(cs_CSText, "text")
    descriptor = None
    for klass in cs_CSText.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_cs_csconnectionend_is_not_abstract():
    assert not inspect.isabstract(cs_CSConnectionEnd)


def test_cs_csconnectionend_constructor_exists():
    assert callable(cs_CSConnectionEnd.__init__)


def test_cs_csconnectionend_constructor_args():
    sig = inspect.signature(cs_CSConnectionEnd.__init__)
    params = list(sig.parameters.keys())
    assert "tipType" in params, "Missing parameter 'tipType'"

def test_cs_csconnectionend_has_tipType():
    assert hasattr(cs_CSConnectionEnd, "tipType")
    descriptor = None
    for klass in cs_CSConnectionEnd.__mro__:
        if "tipType" in klass.__dict__:
            descriptor = klass.__dict__["tipType"]
            break
    assert isinstance(descriptor, property)



def test_cs_cscolor_is_not_abstract():
    assert not inspect.isabstract(cs_CSColor)


def test_cs_cscolor_constructor_exists():
    assert callable(cs_CSColor.__init__)


def test_cs_cscolor_constructor_args():
    sig = inspect.signature(cs_CSColor.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "g" in params, "Missing parameter 'g'"
    assert "r" in params, "Missing parameter 'r'"
    assert "b" in params, "Missing parameter 'b'"

def test_cs_cscolor_has_a():
    assert hasattr(cs_CSColor, "a")
    descriptor = None
    for klass in cs_CSColor.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_cs_cscolor_has_g():
    assert hasattr(cs_CSColor, "g")
    descriptor = None
    for klass in cs_CSColor.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_cs_cscolor_has_r():
    assert hasattr(cs_CSColor, "r")
    descriptor = None
    for klass in cs_CSColor.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_cs_cscolor_has_b():
    assert hasattr(cs_CSColor, "b")
    descriptor = None
    for klass in cs_CSColor.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_cs_csstroke_is_not_abstract():
    assert not inspect.isabstract(cs_CSStroke)


def test_cs_csstroke_constructor_exists():
    assert callable(cs_CSStroke.__init__)


def test_cs_csstroke_constructor_args():
    sig = inspect.signature(cs_CSStroke.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "cap" in params, "Missing parameter 'cap'"
    assert "join" in params, "Missing parameter 'join'"
    assert "miterlimit" in params, "Missing parameter 'miterlimit'"
    assert "dash_phase" in params, "Missing parameter 'dash_phase'"
    assert "dash" in params, "Missing parameter 'dash'"

def test_cs_csstroke_has_width():
    assert hasattr(cs_CSStroke, "width")
    descriptor = None
    for klass in cs_CSStroke.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_cs_csstroke_has_cap():
    assert hasattr(cs_CSStroke, "cap")
    descriptor = None
    for klass in cs_CSStroke.__mro__:
        if "cap" in klass.__dict__:
            descriptor = klass.__dict__["cap"]
            break
    assert isinstance(descriptor, property)

def test_cs_csstroke_has_join():
    assert hasattr(cs_CSStroke, "join")
    descriptor = None
    for klass in cs_CSStroke.__mro__:
        if "join" in klass.__dict__:
            descriptor = klass.__dict__["join"]
            break
    assert isinstance(descriptor, property)

def test_cs_csstroke_has_miterlimit():
    assert hasattr(cs_CSStroke, "miterlimit")
    descriptor = None
    for klass in cs_CSStroke.__mro__:
        if "miterlimit" in klass.__dict__:
            descriptor = klass.__dict__["miterlimit"]
            break
    assert isinstance(descriptor, property)

def test_cs_csstroke_has_dash_phase():
    assert hasattr(cs_CSStroke, "dash_phase")
    descriptor = None
    for klass in cs_CSStroke.__mro__:
        if "dash_phase" in klass.__dict__:
            descriptor = klass.__dict__["dash_phase"]
            break
    assert isinstance(descriptor, property)

def test_cs_csstroke_has_dash():
    assert hasattr(cs_CSStroke, "dash")
    descriptor = None
    for klass in cs_CSStroke.__mro__:
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



def test_cs_csshape_is_not_abstract():
    assert not inspect.isabstract(cs_CSShape)


def test_cs_csshape_constructor_exists():
    assert callable(cs_CSShape.__init__)


def test_cs_csshape_constructor_args():
    sig = inspect.signature(cs_CSShape.__init__)
    params = list(sig.parameters.keys())
    assert "closed" in params, "Missing parameter 'closed'"

def test_cs_csshape_has_closed():
    assert hasattr(cs_CSShape, "closed")
    descriptor = None
    for klass in cs_CSShape.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)



def test_cs_cselement_is_not_abstract():
    assert not inspect.isabstract(cs_CSElement)


def test_cs_cselement_constructor_exists():
    assert callable(cs_CSElement.__init__)


def test_cs_cselement_constructor_args():
    sig = inspect.signature(cs_CSElement.__init__)
    params = list(sig.parameters.keys())
    assert "resizable" in params, "Missing parameter 'resizable'"
    assert "minZoom" in params, "Missing parameter 'minZoom'"
    assert "draggable" in params, "Missing parameter 'draggable'"
    assert "selectable" in params, "Missing parameter 'selectable'"
    assert "maxZoom" in params, "Missing parameter 'maxZoom'"
    assert "templateRoot" in params, "Missing parameter 'templateRoot'"

def test_cs_cselement_has_resizable():
    assert hasattr(cs_CSElement, "resizable")
    descriptor = None
    for klass in cs_CSElement.__mro__:
        if "resizable" in klass.__dict__:
            descriptor = klass.__dict__["resizable"]
            break
    assert isinstance(descriptor, property)

def test_cs_cselement_has_minZoom():
    assert hasattr(cs_CSElement, "minZoom")
    descriptor = None
    for klass in cs_CSElement.__mro__:
        if "minZoom" in klass.__dict__:
            descriptor = klass.__dict__["minZoom"]
            break
    assert isinstance(descriptor, property)

def test_cs_cselement_has_draggable():
    assert hasattr(cs_CSElement, "draggable")
    descriptor = None
    for klass in cs_CSElement.__mro__:
        if "draggable" in klass.__dict__:
            descriptor = klass.__dict__["draggable"]
            break
    assert isinstance(descriptor, property)

def test_cs_cselement_has_selectable():
    assert hasattr(cs_CSElement, "selectable")
    descriptor = None
    for klass in cs_CSElement.__mro__:
        if "selectable" in klass.__dict__:
            descriptor = klass.__dict__["selectable"]
            break
    assert isinstance(descriptor, property)

def test_cs_cselement_has_maxZoom():
    assert hasattr(cs_CSElement, "maxZoom")
    descriptor = None
    for klass in cs_CSElement.__mro__:
        if "maxZoom" in klass.__dict__:
            descriptor = klass.__dict__["maxZoom"]
            break
    assert isinstance(descriptor, property)

def test_cs_cselement_has_templateRoot():
    assert hasattr(cs_CSElement, "templateRoot")
    descriptor = None
    for klass in cs_CSElement.__mro__:
        if "templateRoot" in klass.__dict__:
            descriptor = klass.__dict__["templateRoot"]
            break
    assert isinstance(descriptor, property)



def test_cselement_is_not_abstract():
    assert not inspect.isabstract(CSElement)


def test_cselement_constructor_exists():
    assert callable(CSElement.__init__)


def test_cselement_constructor_args():
    sig = inspect.signature(CSElement.__init__)
    params = list(sig.parameters.keys())



def test_cs_csnode_is_not_abstract():
    assert not inspect.isabstract(cs_CSNode)


def test_cs_csnode_constructor_exists():
    assert callable(cs_CSNode.__init__)


def test_cs_csnode_constructor_args():
    sig = inspect.signature(cs_CSNode.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "widthRatioToParent" in params, "Missing parameter 'widthRatioToParent'"
    assert "maxHeight" in params, "Missing parameter 'maxHeight'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "minWidth" in params, "Missing parameter 'minWidth'"
    assert "verticalAlign" in params, "Missing parameter 'verticalAlign'"
    assert "minHeight" in params, "Missing parameter 'minHeight'"
    assert "heightRatioToParent" in params, "Missing parameter 'heightRatioToParent'"
    assert "maxWidth" in params, "Missing parameter 'maxWidth'"
    assert "horizontalAlign" in params, "Missing parameter 'horizontalAlign'"
    assert "y" in params, "Missing parameter 'y'"

def test_cs_csnode_has_x():
    assert hasattr(cs_CSNode, "x")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_widthRatioToParent():
    assert hasattr(cs_CSNode, "widthRatioToParent")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "widthRatioToParent" in klass.__dict__:
            descriptor = klass.__dict__["widthRatioToParent"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_maxHeight():
    assert hasattr(cs_CSNode, "maxHeight")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "maxHeight" in klass.__dict__:
            descriptor = klass.__dict__["maxHeight"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_height():
    assert hasattr(cs_CSNode, "height")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_width():
    assert hasattr(cs_CSNode, "width")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_minWidth():
    assert hasattr(cs_CSNode, "minWidth")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "minWidth" in klass.__dict__:
            descriptor = klass.__dict__["minWidth"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_verticalAlign():
    assert hasattr(cs_CSNode, "verticalAlign")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "verticalAlign" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlign"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_minHeight():
    assert hasattr(cs_CSNode, "minHeight")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "minHeight" in klass.__dict__:
            descriptor = klass.__dict__["minHeight"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_heightRatioToParent():
    assert hasattr(cs_CSNode, "heightRatioToParent")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "heightRatioToParent" in klass.__dict__:
            descriptor = klass.__dict__["heightRatioToParent"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_maxWidth():
    assert hasattr(cs_CSNode, "maxWidth")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "maxWidth" in klass.__dict__:
            descriptor = klass.__dict__["maxWidth"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_horizontalAlign():
    assert hasattr(cs_CSNode, "horizontalAlign")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "horizontalAlign" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlign"]
            break
    assert isinstance(descriptor, property)

def test_cs_csnode_has_y():
    assert hasattr(cs_CSNode, "y")
    descriptor = None
    for klass in cs_CSNode.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_cs_csconnection_is_not_abstract():
    assert not inspect.isabstract(cs_CSConnection)


def test_cs_csconnection_constructor_exists():
    assert callable(cs_CSConnection.__init__)


def test_cs_csconnection_constructor_args():
    sig = inspect.signature(cs_CSConnection.__init__)
    params = list(sig.parameters.keys())



def test_cs_csroot_is_not_abstract():
    assert not inspect.isabstract(cs_CSRoot)


def test_cs_csroot_constructor_exists():
    assert callable(cs_CSRoot.__init__)


def test_cs_csroot_constructor_args():
    sig = inspect.signature(cs_CSRoot.__init__)
    params = list(sig.parameters.keys())

def test_csorientation_exists():
    # Check that the Enumeration exists
    assert CSOrientation is not None

def test_csorientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSOrientation]
    expected_literals = [
        "HORIZONTAL",
        "VERTICAL",
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
        "FIT_TO_CHILDREN",
        "AUTO_EXPAND",
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
cs_CSPoint_strategy = st.builds(
    cs_CSPoint,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cs_EClass_strategy = st.builds(
    cs_EClass,
)
cs_CSLayout_strategy = st.builds(
    cs_CSLayout,
)
cs_EStructuralFeature_strategy = st.builds(
    cs_EStructuralFeature,
)
cs_EObject_strategy = st.builds(
    cs_EObject,
)
cs_CSTransform_strategy = st.builds(
    cs_CSTransform,
    m12=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m10=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m02=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m20=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m01=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m21=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m22=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m00=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    m11=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CSNode_strategy = st.builds(
    CSNode,
)
cs_CSTemplateDescription_strategy = st.builds(
    cs_CSTemplateDescription,
    scale=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cs_CSText_strategy = st.builds(
    cs_CSText,
    text=
        safe_text
)
cs_CSConnectionEnd_strategy = st.builds(
    cs_CSConnectionEnd,
    tipType=
        st.integers()
)
cs_CSColor_strategy = st.builds(
    cs_CSColor,
    a=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    g=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    r=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    b=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cs_CSStroke_strategy = st.builds(
    cs_CSStroke,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cap=
        st.integers(),
    join=
        st.integers(),
    miterlimit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    dash_phase=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    dash=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
cs_CSShape_strategy = st.builds(
    cs_CSShape,
    closed=
        st.booleans()
)
cs_CSElement_strategy = st.builds(
    cs_CSElement,
    resizable=
        st.booleans(),
    minZoom=
        safe_text,
    draggable=
        st.booleans(),
    selectable=
        safe_text,
    maxZoom=
        safe_text,
    templateRoot=
        st.booleans()
)
CSElement_strategy = st.builds(
    CSElement,
)
cs_CSNode_strategy = st.builds(
    cs_CSNode,
    x=
        safe_text,
    widthRatioToParent=
        safe_text,
    maxHeight=
        safe_text,
    height=
        safe_text,
    width=
        safe_text,
    minWidth=
        safe_text,
    verticalAlign=
        safe_text,
    minHeight=
        safe_text,
    heightRatioToParent=
        safe_text,
    maxWidth=
        safe_text,
    horizontalAlign=
        safe_text,
    y=
        safe_text
)
cs_CSConnection_strategy = st.builds(
    cs_CSConnection,
)
cs_CSRoot_strategy = st.builds(
    cs_CSRoot,
)

@given(instance=cs_CSPoint_strategy)
@settings(max_examples=50)
def test_cs_cspoint_instantiation(instance):
    assert isinstance(instance, cs_CSPoint)



@given(instance=cs_CSPoint_strategy)
def test_cs_cspoint_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=cs_CSPoint_strategy)
def test_cs_cspoint_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=cs_EClass_strategy)
@settings(max_examples=50)
def test_cs_eclass_instantiation(instance):
    assert isinstance(instance, cs_EClass)

@given(instance=cs_CSLayout_strategy)
@settings(max_examples=50)
def test_cs_cslayout_instantiation(instance):
    assert isinstance(instance, cs_CSLayout)

@given(instance=cs_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_cs_estructuralfeature_instantiation(instance):
    assert isinstance(instance, cs_EStructuralFeature)

@given(instance=cs_EObject_strategy)
@settings(max_examples=50)
def test_cs_eobject_instantiation(instance):
    assert isinstance(instance, cs_EObject)

@given(instance=cs_CSTransform_strategy)
@settings(max_examples=50)
def test_cs_cstransform_instantiation(instance):
    assert isinstance(instance, cs_CSTransform)



@given(instance=cs_CSTransform_strategy)
def test_cs_cstransform_m12_setter(instance):
    original = instance.m12
    instance.m12 = original
    assert instance.m12 == original



@given(instance=cs_CSTransform_strategy)
def test_cs_cstransform_m10_setter(instance):
    original = instance.m10
    instance.m10 = original
    assert instance.m10 == original



@given(instance=cs_CSTransform_strategy)
def test_cs_cstransform_m02_setter(instance):
    original = instance.m02
    instance.m02 = original
    assert instance.m02 == original



@given(instance=cs_CSTransform_strategy)
def test_cs_cstransform_m20_setter(instance):
    original = instance.m20
    instance.m20 = original
    assert instance.m20 == original



@given(instance=cs_CSTransform_strategy)
def test_cs_cstransform_m01_setter(instance):
    original = instance.m01
    instance.m01 = original
    assert instance.m01 == original



@given(instance=cs_CSTransform_strategy)
def test_cs_cstransform_m21_setter(instance):
    original = instance.m21
    instance.m21 = original
    assert instance.m21 == original



@given(instance=cs_CSTransform_strategy)
def test_cs_cstransform_m22_setter(instance):
    original = instance.m22
    instance.m22 = original
    assert instance.m22 == original



@given(instance=cs_CSTransform_strategy)
def test_cs_cstransform_m00_setter(instance):
    original = instance.m00
    instance.m00 = original
    assert instance.m00 == original



@given(instance=cs_CSTransform_strategy)
def test_cs_cstransform_m11_setter(instance):
    original = instance.m11
    instance.m11 = original
    assert instance.m11 == original

@given(instance=CSNode_strategy)
@settings(max_examples=50)
def test_csnode_instantiation(instance):
    assert isinstance(instance, CSNode)

@given(instance=cs_CSTemplateDescription_strategy)
@settings(max_examples=50)
def test_cs_cstemplatedescription_instantiation(instance):
    assert isinstance(instance, cs_CSTemplateDescription)



@given(instance=cs_CSTemplateDescription_strategy)
def test_cs_cstemplatedescription_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=cs_CSText_strategy)
@settings(max_examples=50)
def test_cs_cstext_instantiation(instance):
    assert isinstance(instance, cs_CSText)



@given(instance=cs_CSText_strategy)
def test_cs_cstext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=cs_CSConnectionEnd_strategy)
@settings(max_examples=50)
def test_cs_csconnectionend_instantiation(instance):
    assert isinstance(instance, cs_CSConnectionEnd)



@given(instance=cs_CSConnectionEnd_strategy)
def test_cs_csconnectionend_tipType_setter(instance):
    original = instance.tipType
    instance.tipType = original
    assert instance.tipType == original

@given(instance=cs_CSColor_strategy)
@settings(max_examples=50)
def test_cs_cscolor_instantiation(instance):
    assert isinstance(instance, cs_CSColor)



@given(instance=cs_CSColor_strategy)
def test_cs_cscolor_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=cs_CSColor_strategy)
def test_cs_cscolor_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original



@given(instance=cs_CSColor_strategy)
def test_cs_cscolor_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original



@given(instance=cs_CSColor_strategy)
def test_cs_cscolor_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=cs_CSStroke_strategy)
@settings(max_examples=50)
def test_cs_csstroke_instantiation(instance):
    assert isinstance(instance, cs_CSStroke)



@given(instance=cs_CSStroke_strategy)
def test_cs_csstroke_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cs_CSStroke_strategy)
def test_cs_csstroke_cap_setter(instance):
    original = instance.cap
    instance.cap = original
    assert instance.cap == original



@given(instance=cs_CSStroke_strategy)
def test_cs_csstroke_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original



@given(instance=cs_CSStroke_strategy)
def test_cs_csstroke_miterlimit_setter(instance):
    original = instance.miterlimit
    instance.miterlimit = original
    assert instance.miterlimit == original



@given(instance=cs_CSStroke_strategy)
def test_cs_csstroke_dash_phase_setter(instance):
    original = instance.dash_phase
    instance.dash_phase = original
    assert instance.dash_phase == original



@given(instance=cs_CSStroke_strategy)
def test_cs_csstroke_dash_setter(instance):
    original = instance.dash
    instance.dash = original
    assert instance.dash == original

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=cs_CSShape_strategy)
@settings(max_examples=50)
def test_cs_csshape_instantiation(instance):
    assert isinstance(instance, cs_CSShape)



@given(instance=cs_CSShape_strategy)
def test_cs_csshape_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original

@given(instance=cs_CSElement_strategy)
@settings(max_examples=50)
def test_cs_cselement_instantiation(instance):
    assert isinstance(instance, cs_CSElement)



@given(instance=cs_CSElement_strategy)
def test_cs_cselement_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original



@given(instance=cs_CSElement_strategy)
def test_cs_cselement_minZoom_setter(instance):
    original = instance.minZoom
    instance.minZoom = original
    assert instance.minZoom == original



@given(instance=cs_CSElement_strategy)
def test_cs_cselement_draggable_setter(instance):
    original = instance.draggable
    instance.draggable = original
    assert instance.draggable == original



@given(instance=cs_CSElement_strategy)
def test_cs_cselement_selectable_setter(instance):
    original = instance.selectable
    instance.selectable = original
    assert instance.selectable == original



@given(instance=cs_CSElement_strategy)
def test_cs_cselement_maxZoom_setter(instance):
    original = instance.maxZoom
    instance.maxZoom = original
    assert instance.maxZoom == original



@given(instance=cs_CSElement_strategy)
def test_cs_cselement_templateRoot_setter(instance):
    original = instance.templateRoot
    instance.templateRoot = original
    assert instance.templateRoot == original

@given(instance=CSElement_strategy)
@settings(max_examples=50)
def test_cselement_instantiation(instance):
    assert isinstance(instance, CSElement)

@given(instance=cs_CSNode_strategy)
@settings(max_examples=50)
def test_cs_csnode_instantiation(instance):
    assert isinstance(instance, cs_CSNode)



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_widthRatioToParent_setter(instance):
    original = instance.widthRatioToParent
    instance.widthRatioToParent = original
    assert instance.widthRatioToParent == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_maxHeight_setter(instance):
    original = instance.maxHeight
    instance.maxHeight = original
    assert instance.maxHeight == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_minWidth_setter(instance):
    original = instance.minWidth
    instance.minWidth = original
    assert instance.minWidth == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_verticalAlign_setter(instance):
    original = instance.verticalAlign
    instance.verticalAlign = original
    assert instance.verticalAlign == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_minHeight_setter(instance):
    original = instance.minHeight
    instance.minHeight = original
    assert instance.minHeight == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_heightRatioToParent_setter(instance):
    original = instance.heightRatioToParent
    instance.heightRatioToParent = original
    assert instance.heightRatioToParent == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_maxWidth_setter(instance):
    original = instance.maxWidth
    instance.maxWidth = original
    assert instance.maxWidth == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_horizontalAlign_setter(instance):
    original = instance.horizontalAlign
    instance.horizontalAlign = original
    assert instance.horizontalAlign == original



@given(instance=cs_CSNode_strategy)
def test_cs_csnode_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=cs_CSConnection_strategy)
@settings(max_examples=50)
def test_cs_csconnection_instantiation(instance):
    assert isinstance(instance, cs_CSConnection)

@given(instance=cs_CSRoot_strategy)
@settings(max_examples=50)
def test_cs_csroot_instantiation(instance):
    assert isinstance(instance, cs_CSRoot)
