import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    LabeledShape,
    Plane,
    di::Font,
    Style,
    Label,
    di::DiagramElement,
    di::BaseElement,
    LabeledEdge,
    Diagram,
    di::BPMNShape,
    di::BPMNPlane,
    di::BPMNLabelStyle,
    di::BPMNLabel,
    di::BPMNEdge,
    di::BPMNDiagram,
    di::EStringToStringMapEntry,
    di::DocumentRoot,
    MessageVisibleKind,
    ParticipantBandKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_labeledshape_is_not_abstract():
    assert not inspect.isabstract(LabeledShape)


def test_labeledshape_constructor_exists():
    assert callable(LabeledShape.__init__)


def test_labeledshape_constructor_args():
    sig = inspect.signature(LabeledShape.__init__)
    params = list(sig.parameters.keys())



def test_plane_is_not_abstract():
    assert not inspect.isabstract(Plane)


def test_plane_constructor_exists():
    assert callable(Plane.__init__)


def test_plane_constructor_args():
    sig = inspect.signature(Plane.__init__)
    params = list(sig.parameters.keys())



def test_di::font_is_not_abstract():
    assert not inspect.isabstract(di::Font)


def test_di::font_constructor_exists():
    assert callable(di::Font.__init__)


def test_di::font_constructor_args():
    sig = inspect.signature(di::Font.__init__)
    params = list(sig.parameters.keys())



def test_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_style_constructor_exists():
    assert callable(Style.__init__)


def test_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_di::diagramelement_is_not_abstract():
    assert not inspect.isabstract(di::DiagramElement)


def test_di::diagramelement_constructor_exists():
    assert callable(di::DiagramElement.__init__)


def test_di::diagramelement_constructor_args():
    sig = inspect.signature(di::DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_di::baseelement_is_not_abstract():
    assert not inspect.isabstract(di::BaseElement)


def test_di::baseelement_constructor_exists():
    assert callable(di::BaseElement.__init__)


def test_di::baseelement_constructor_args():
    sig = inspect.signature(di::BaseElement.__init__)
    params = list(sig.parameters.keys())



def test_labelededge_is_not_abstract():
    assert not inspect.isabstract(LabeledEdge)


def test_labelededge_constructor_exists():
    assert callable(LabeledEdge.__init__)


def test_labelededge_constructor_args():
    sig = inspect.signature(LabeledEdge.__init__)
    params = list(sig.parameters.keys())



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_di::bpmnshape_is_not_abstract():
    assert not inspect.isabstract(di::BPMNShape)


def test_di::bpmnshape_constructor_exists():
    assert callable(di::BPMNShape.__init__)


def test_di::bpmnshape_constructor_args():
    sig = inspect.signature(di::BPMNShape.__init__)
    params = list(sig.parameters.keys())
    assert "isExpanded" in params, "Missing parameter 'isExpanded'"
    assert "isHorizontal" in params, "Missing parameter 'isHorizontal'"
    assert "isMarkerVisible" in params, "Missing parameter 'isMarkerVisible'"
    assert "participantBandKind" in params, "Missing parameter 'participantBandKind'"
    assert "isMessageVisible" in params, "Missing parameter 'isMessageVisible'"

def test_di::bpmnshape_has_isExpanded():
    assert hasattr(di::BPMNShape, "isExpanded")
    descriptor = None
    for klass in di::BPMNShape.__mro__:
        if "isExpanded" in klass.__dict__:
            descriptor = klass.__dict__["isExpanded"]
            break
    assert isinstance(descriptor, property)

def test_di::bpmnshape_has_isHorizontal():
    assert hasattr(di::BPMNShape, "isHorizontal")
    descriptor = None
    for klass in di::BPMNShape.__mro__:
        if "isHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["isHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_di::bpmnshape_has_isMarkerVisible():
    assert hasattr(di::BPMNShape, "isMarkerVisible")
    descriptor = None
    for klass in di::BPMNShape.__mro__:
        if "isMarkerVisible" in klass.__dict__:
            descriptor = klass.__dict__["isMarkerVisible"]
            break
    assert isinstance(descriptor, property)

def test_di::bpmnshape_has_participantBandKind():
    assert hasattr(di::BPMNShape, "participantBandKind")
    descriptor = None
    for klass in di::BPMNShape.__mro__:
        if "participantBandKind" in klass.__dict__:
            descriptor = klass.__dict__["participantBandKind"]
            break
    assert isinstance(descriptor, property)

def test_di::bpmnshape_has_isMessageVisible():
    assert hasattr(di::BPMNShape, "isMessageVisible")
    descriptor = None
    for klass in di::BPMNShape.__mro__:
        if "isMessageVisible" in klass.__dict__:
            descriptor = klass.__dict__["isMessageVisible"]
            break
    assert isinstance(descriptor, property)



def test_di::bpmnplane_is_not_abstract():
    assert not inspect.isabstract(di::BPMNPlane)


def test_di::bpmnplane_constructor_exists():
    assert callable(di::BPMNPlane.__init__)


def test_di::bpmnplane_constructor_args():
    sig = inspect.signature(di::BPMNPlane.__init__)
    params = list(sig.parameters.keys())



def test_di::bpmnlabelstyle_is_not_abstract():
    assert not inspect.isabstract(di::BPMNLabelStyle)


def test_di::bpmnlabelstyle_constructor_exists():
    assert callable(di::BPMNLabelStyle.__init__)


def test_di::bpmnlabelstyle_constructor_args():
    sig = inspect.signature(di::BPMNLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_di::bpmnlabel_is_not_abstract():
    assert not inspect.isabstract(di::BPMNLabel)


def test_di::bpmnlabel_constructor_exists():
    assert callable(di::BPMNLabel.__init__)


def test_di::bpmnlabel_constructor_args():
    sig = inspect.signature(di::BPMNLabel.__init__)
    params = list(sig.parameters.keys())



def test_di::bpmnedge_is_not_abstract():
    assert not inspect.isabstract(di::BPMNEdge)


def test_di::bpmnedge_constructor_exists():
    assert callable(di::BPMNEdge.__init__)


def test_di::bpmnedge_constructor_args():
    sig = inspect.signature(di::BPMNEdge.__init__)
    params = list(sig.parameters.keys())
    assert "messageVisibleKind" in params, "Missing parameter 'messageVisibleKind'"

def test_di::bpmnedge_has_messageVisibleKind():
    assert hasattr(di::BPMNEdge, "messageVisibleKind")
    descriptor = None
    for klass in di::BPMNEdge.__mro__:
        if "messageVisibleKind" in klass.__dict__:
            descriptor = klass.__dict__["messageVisibleKind"]
            break
    assert isinstance(descriptor, property)



def test_di::bpmndiagram_is_not_abstract():
    assert not inspect.isabstract(di::BPMNDiagram)


def test_di::bpmndiagram_constructor_exists():
    assert callable(di::BPMNDiagram.__init__)


def test_di::bpmndiagram_constructor_args():
    sig = inspect.signature(di::BPMNDiagram.__init__)
    params = list(sig.parameters.keys())



def test_di::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(di::EStringToStringMapEntry)


def test_di::estringtostringmapentry_constructor_exists():
    assert callable(di::EStringToStringMapEntry.__init__)


def test_di::estringtostringmapentry_constructor_args():
    sig = inspect.signature(di::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_di::documentroot_is_not_abstract():
    assert not inspect.isabstract(di::DocumentRoot)


def test_di::documentroot_constructor_exists():
    assert callable(di::DocumentRoot.__init__)


def test_di::documentroot_constructor_args():
    sig = inspect.signature(di::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_di::documentroot_has_mixed():
    assert hasattr(di::DocumentRoot, "mixed")
    descriptor = None
    for klass in di::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_messagevisiblekind_exists():
    # Check that the Enumeration exists
    assert MessageVisibleKind is not None

def test_messagevisiblekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageVisibleKind]
    expected_literals = [
        "non_initiating",
        "initiating",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageVisibleKind"

def test_participantbandkind_exists():
    # Check that the Enumeration exists
    assert ParticipantBandKind is not None

def test_participantbandkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParticipantBandKind]
    expected_literals = [
        "top_initiating",
        "middle_non_initiating",
        "top_non_initiating",
        "bottom_non_initiating",
        "bottom_initiating",
        "middle_initiating",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParticipantBandKind"


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
LabeledShape_strategy = st.builds(
    LabeledShape,
)
Plane_strategy = st.builds(
    Plane,
)
di::Font_strategy = st.builds(
    di::Font,
)
Style_strategy = st.builds(
    Style,
)
Label_strategy = st.builds(
    Label,
)
di::DiagramElement_strategy = st.builds(
    di::DiagramElement,
)
di::BaseElement_strategy = st.builds(
    di::BaseElement,
)
LabeledEdge_strategy = st.builds(
    LabeledEdge,
)
Diagram_strategy = st.builds(
    Diagram,
)
di::BPMNShape_strategy = st.builds(
    di::BPMNShape,
    isExpanded=
        st.booleans(),
    isHorizontal=
        st.booleans(),
    isMarkerVisible=
        st.booleans(),
    participantBandKind=
        safe_text,
    isMessageVisible=
        st.booleans()
)
di::BPMNPlane_strategy = st.builds(
    di::BPMNPlane,
)
di::BPMNLabelStyle_strategy = st.builds(
    di::BPMNLabelStyle,
)
di::BPMNLabel_strategy = st.builds(
    di::BPMNLabel,
)
di::BPMNEdge_strategy = st.builds(
    di::BPMNEdge,
    messageVisibleKind=
        safe_text
)
di::BPMNDiagram_strategy = st.builds(
    di::BPMNDiagram,
)
di::EStringToStringMapEntry_strategy = st.builds(
    di::EStringToStringMapEntry,
)
di::DocumentRoot_strategy = st.builds(
    di::DocumentRoot,
    mixed=
        safe_text
)

@given(instance=LabeledShape_strategy)
@settings(max_examples=50)
def test_labeledshape_instantiation(instance):
    assert isinstance(instance, LabeledShape)

@given(instance=Plane_strategy)
@settings(max_examples=50)
def test_plane_instantiation(instance):
    assert isinstance(instance, Plane)

@given(instance=di::Font_strategy)
@settings(max_examples=50)
def test_di::font_instantiation(instance):
    assert isinstance(instance, di::Font)

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=di::DiagramElement_strategy)
@settings(max_examples=50)
def test_di::diagramelement_instantiation(instance):
    assert isinstance(instance, di::DiagramElement)

@given(instance=di::BaseElement_strategy)
@settings(max_examples=50)
def test_di::baseelement_instantiation(instance):
    assert isinstance(instance, di::BaseElement)

@given(instance=LabeledEdge_strategy)
@settings(max_examples=50)
def test_labelededge_instantiation(instance):
    assert isinstance(instance, LabeledEdge)

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=di::BPMNShape_strategy)
@settings(max_examples=50)
def test_di::bpmnshape_instantiation(instance):
    assert isinstance(instance, di::BPMNShape)

@given(instance=di::BPMNShape_strategy)
def test_di::bpmnshape_isExpanded_type(instance):
    assert isinstance(instance.isExpanded, bool)


@given(instance=di::BPMNShape_strategy)
def test_di::bpmnshape_isExpanded_setter(instance):
    original = instance.isExpanded
    instance.isExpanded = original
    assert instance.isExpanded == original

@given(instance=di::BPMNShape_strategy)
def test_di::bpmnshape_isHorizontal_type(instance):
    assert isinstance(instance.isHorizontal, bool)


@given(instance=di::BPMNShape_strategy)
def test_di::bpmnshape_isHorizontal_setter(instance):
    original = instance.isHorizontal
    instance.isHorizontal = original
    assert instance.isHorizontal == original

@given(instance=di::BPMNShape_strategy)
def test_di::bpmnshape_isMarkerVisible_type(instance):
    assert isinstance(instance.isMarkerVisible, bool)


@given(instance=di::BPMNShape_strategy)
def test_di::bpmnshape_isMarkerVisible_setter(instance):
    original = instance.isMarkerVisible
    instance.isMarkerVisible = original
    assert instance.isMarkerVisible == original

@given(instance=di::BPMNShape_strategy)
def test_di::bpmnshape_participantBandKind_type(instance):
    assert isinstance(instance.participantBandKind, str)


@given(instance=di::BPMNShape_strategy)
def test_di::bpmnshape_participantBandKind_setter(instance):
    original = instance.participantBandKind
    instance.participantBandKind = original
    assert instance.participantBandKind == original

@given(instance=di::BPMNShape_strategy)
def test_di::bpmnshape_isMessageVisible_type(instance):
    assert isinstance(instance.isMessageVisible, bool)


@given(instance=di::BPMNShape_strategy)
def test_di::bpmnshape_isMessageVisible_setter(instance):
    original = instance.isMessageVisible
    instance.isMessageVisible = original
    assert instance.isMessageVisible == original

@given(instance=di::BPMNPlane_strategy)
@settings(max_examples=50)
def test_di::bpmnplane_instantiation(instance):
    assert isinstance(instance, di::BPMNPlane)

@given(instance=di::BPMNLabelStyle_strategy)
@settings(max_examples=50)
def test_di::bpmnlabelstyle_instantiation(instance):
    assert isinstance(instance, di::BPMNLabelStyle)

@given(instance=di::BPMNLabel_strategy)
@settings(max_examples=50)
def test_di::bpmnlabel_instantiation(instance):
    assert isinstance(instance, di::BPMNLabel)

@given(instance=di::BPMNEdge_strategy)
@settings(max_examples=50)
def test_di::bpmnedge_instantiation(instance):
    assert isinstance(instance, di::BPMNEdge)

@given(instance=di::BPMNEdge_strategy)
def test_di::bpmnedge_messageVisibleKind_type(instance):
    assert isinstance(instance.messageVisibleKind, str)


@given(instance=di::BPMNEdge_strategy)
def test_di::bpmnedge_messageVisibleKind_setter(instance):
    original = instance.messageVisibleKind
    instance.messageVisibleKind = original
    assert instance.messageVisibleKind == original

@given(instance=di::BPMNDiagram_strategy)
@settings(max_examples=50)
def test_di::bpmndiagram_instantiation(instance):
    assert isinstance(instance, di::BPMNDiagram)

@given(instance=di::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_di::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, di::EStringToStringMapEntry)

@given(instance=di::DocumentRoot_strategy)
@settings(max_examples=50)
def test_di::documentroot_instantiation(instance):
    assert isinstance(instance, di::DocumentRoot)

@given(instance=di::DocumentRoot_strategy)
def test_di::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=di::DocumentRoot_strategy)
def test_di::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original
