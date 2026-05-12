import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    LabeledShape,
    Plane,
    di_Font,
    Style,
    Label,
    di_BaseElement,
    LabeledEdge,
    di_BPMNPlane,
    di_BPMNLabelStyle,
    Diagram,
    di_DiagramElement,
    di_BPMNShape,
    di_BPMNEdge,
    di_BPMNDiagram,
    di_BPMNLabel,
    di_EStringToStringMapEntry,
    di_DocumentRoot,
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



def test_di_font_is_not_abstract():
    assert not inspect.isabstract(di_Font)


def test_di_font_constructor_exists():
    assert callable(di_Font.__init__)


def test_di_font_constructor_args():
    sig = inspect.signature(di_Font.__init__)
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



def test_di_baseelement_is_not_abstract():
    assert not inspect.isabstract(di_BaseElement)


def test_di_baseelement_constructor_exists():
    assert callable(di_BaseElement.__init__)


def test_di_baseelement_constructor_args():
    sig = inspect.signature(di_BaseElement.__init__)
    params = list(sig.parameters.keys())



def test_labelededge_is_not_abstract():
    assert not inspect.isabstract(LabeledEdge)


def test_labelededge_constructor_exists():
    assert callable(LabeledEdge.__init__)


def test_labelededge_constructor_args():
    sig = inspect.signature(LabeledEdge.__init__)
    params = list(sig.parameters.keys())



def test_di_bpmnplane_is_not_abstract():
    assert not inspect.isabstract(di_BPMNPlane)


def test_di_bpmnplane_constructor_exists():
    assert callable(di_BPMNPlane.__init__)


def test_di_bpmnplane_constructor_args():
    sig = inspect.signature(di_BPMNPlane.__init__)
    params = list(sig.parameters.keys())



def test_di_bpmnlabelstyle_is_not_abstract():
    assert not inspect.isabstract(di_BPMNLabelStyle)


def test_di_bpmnlabelstyle_constructor_exists():
    assert callable(di_BPMNLabelStyle.__init__)


def test_di_bpmnlabelstyle_constructor_args():
    sig = inspect.signature(di_BPMNLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_di_diagramelement_is_not_abstract():
    assert not inspect.isabstract(di_DiagramElement)


def test_di_diagramelement_constructor_exists():
    assert callable(di_DiagramElement.__init__)


def test_di_diagramelement_constructor_args():
    sig = inspect.signature(di_DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_di_bpmnshape_is_not_abstract():
    assert not inspect.isabstract(di_BPMNShape)


def test_di_bpmnshape_constructor_exists():
    assert callable(di_BPMNShape.__init__)


def test_di_bpmnshape_constructor_args():
    sig = inspect.signature(di_BPMNShape.__init__)
    params = list(sig.parameters.keys())
    assert "participantBandKind" in params, "Missing parameter 'participantBandKind'"
    assert "isMessageVisible" in params, "Missing parameter 'isMessageVisible'"
    assert "isExpanded" in params, "Missing parameter 'isExpanded'"
    assert "isHorizontal" in params, "Missing parameter 'isHorizontal'"
    assert "isMarkerVisible" in params, "Missing parameter 'isMarkerVisible'"

def test_di_bpmnshape_has_participantBandKind():
    assert hasattr(di_BPMNShape, "participantBandKind")
    descriptor = None
    for klass in di_BPMNShape.__mro__:
        if "participantBandKind" in klass.__dict__:
            descriptor = klass.__dict__["participantBandKind"]
            break
    assert isinstance(descriptor, property)

def test_di_bpmnshape_has_isMessageVisible():
    assert hasattr(di_BPMNShape, "isMessageVisible")
    descriptor = None
    for klass in di_BPMNShape.__mro__:
        if "isMessageVisible" in klass.__dict__:
            descriptor = klass.__dict__["isMessageVisible"]
            break
    assert isinstance(descriptor, property)

def test_di_bpmnshape_has_isExpanded():
    assert hasattr(di_BPMNShape, "isExpanded")
    descriptor = None
    for klass in di_BPMNShape.__mro__:
        if "isExpanded" in klass.__dict__:
            descriptor = klass.__dict__["isExpanded"]
            break
    assert isinstance(descriptor, property)

def test_di_bpmnshape_has_isHorizontal():
    assert hasattr(di_BPMNShape, "isHorizontal")
    descriptor = None
    for klass in di_BPMNShape.__mro__:
        if "isHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["isHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_di_bpmnshape_has_isMarkerVisible():
    assert hasattr(di_BPMNShape, "isMarkerVisible")
    descriptor = None
    for klass in di_BPMNShape.__mro__:
        if "isMarkerVisible" in klass.__dict__:
            descriptor = klass.__dict__["isMarkerVisible"]
            break
    assert isinstance(descriptor, property)



def test_di_bpmnedge_is_not_abstract():
    assert not inspect.isabstract(di_BPMNEdge)


def test_di_bpmnedge_constructor_exists():
    assert callable(di_BPMNEdge.__init__)


def test_di_bpmnedge_constructor_args():
    sig = inspect.signature(di_BPMNEdge.__init__)
    params = list(sig.parameters.keys())
    assert "messageVisibleKind" in params, "Missing parameter 'messageVisibleKind'"

def test_di_bpmnedge_has_messageVisibleKind():
    assert hasattr(di_BPMNEdge, "messageVisibleKind")
    descriptor = None
    for klass in di_BPMNEdge.__mro__:
        if "messageVisibleKind" in klass.__dict__:
            descriptor = klass.__dict__["messageVisibleKind"]
            break
    assert isinstance(descriptor, property)



def test_di_bpmndiagram_is_not_abstract():
    assert not inspect.isabstract(di_BPMNDiagram)


def test_di_bpmndiagram_constructor_exists():
    assert callable(di_BPMNDiagram.__init__)


def test_di_bpmndiagram_constructor_args():
    sig = inspect.signature(di_BPMNDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "featureModel" in params, "Missing parameter 'featureModel'"
    assert "location" in params, "Missing parameter 'location'"
    assert "phase" in params, "Missing parameter 'phase'"

def test_di_bpmndiagram_has_version():
    assert hasattr(di_BPMNDiagram, "version")
    descriptor = None
    for klass in di_BPMNDiagram.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_di_bpmndiagram_has_featureModel():
    assert hasattr(di_BPMNDiagram, "featureModel")
    descriptor = None
    for klass in di_BPMNDiagram.__mro__:
        if "featureModel" in klass.__dict__:
            descriptor = klass.__dict__["featureModel"]
            break
    assert isinstance(descriptor, property)

def test_di_bpmndiagram_has_location():
    assert hasattr(di_BPMNDiagram, "location")
    descriptor = None
    for klass in di_BPMNDiagram.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_di_bpmndiagram_has_phase():
    assert hasattr(di_BPMNDiagram, "phase")
    descriptor = None
    for klass in di_BPMNDiagram.__mro__:
        if "phase" in klass.__dict__:
            descriptor = klass.__dict__["phase"]
            break
    assert isinstance(descriptor, property)



def test_di_bpmnlabel_is_not_abstract():
    assert not inspect.isabstract(di_BPMNLabel)


def test_di_bpmnlabel_constructor_exists():
    assert callable(di_BPMNLabel.__init__)


def test_di_bpmnlabel_constructor_args():
    sig = inspect.signature(di_BPMNLabel.__init__)
    params = list(sig.parameters.keys())



def test_di_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(di_EStringToStringMapEntry)


def test_di_estringtostringmapentry_constructor_exists():
    assert callable(di_EStringToStringMapEntry.__init__)


def test_di_estringtostringmapentry_constructor_args():
    sig = inspect.signature(di_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_di_documentroot_is_not_abstract():
    assert not inspect.isabstract(di_DocumentRoot)


def test_di_documentroot_constructor_exists():
    assert callable(di_DocumentRoot.__init__)


def test_di_documentroot_constructor_args():
    sig = inspect.signature(di_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_di_documentroot_has_mixed():
    assert hasattr(di_DocumentRoot, "mixed")
    descriptor = None
    for klass in di_DocumentRoot.__mro__:
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
        "initiating",
        "non_initiating",
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
        "bottom_non_initiating",
        "top_non_initiating",
        "bottom_initiating",
        "middle_initiating",
        "middle_non_initiating",
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
di_Font_strategy = st.builds(
    di_Font,
)
Style_strategy = st.builds(
    Style,
)
Label_strategy = st.builds(
    Label,
)
di_BaseElement_strategy = st.builds(
    di_BaseElement,
)
LabeledEdge_strategy = st.builds(
    LabeledEdge,
)
di_BPMNPlane_strategy = st.builds(
    di_BPMNPlane,
)
di_BPMNLabelStyle_strategy = st.builds(
    di_BPMNLabelStyle,
)
Diagram_strategy = st.builds(
    Diagram,
)
di_DiagramElement_strategy = st.builds(
    di_DiagramElement,
)
di_BPMNShape_strategy = st.builds(
    di_BPMNShape,
    participantBandKind=
        safe_text,
    isMessageVisible=
        st.booleans(),
    isExpanded=
        st.booleans(),
    isHorizontal=
        st.booleans(),
    isMarkerVisible=
        st.booleans()
)
di_BPMNEdge_strategy = st.builds(
    di_BPMNEdge,
    messageVisibleKind=
        safe_text
)
di_BPMNDiagram_strategy = st.builds(
    di_BPMNDiagram,
    version=
        safe_text,
    featureModel=
        safe_text,
    location=
        safe_text,
    phase=
        safe_text
)
di_BPMNLabel_strategy = st.builds(
    di_BPMNLabel,
)
di_EStringToStringMapEntry_strategy = st.builds(
    di_EStringToStringMapEntry,
)
di_DocumentRoot_strategy = st.builds(
    di_DocumentRoot,
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

@given(instance=di_Font_strategy)
@settings(max_examples=50)
def test_di_font_instantiation(instance):
    assert isinstance(instance, di_Font)

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=di_BaseElement_strategy)
@settings(max_examples=50)
def test_di_baseelement_instantiation(instance):
    assert isinstance(instance, di_BaseElement)

@given(instance=LabeledEdge_strategy)
@settings(max_examples=50)
def test_labelededge_instantiation(instance):
    assert isinstance(instance, LabeledEdge)

@given(instance=di_BPMNPlane_strategy)
@settings(max_examples=50)
def test_di_bpmnplane_instantiation(instance):
    assert isinstance(instance, di_BPMNPlane)

@given(instance=di_BPMNLabelStyle_strategy)
@settings(max_examples=50)
def test_di_bpmnlabelstyle_instantiation(instance):
    assert isinstance(instance, di_BPMNLabelStyle)

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=di_DiagramElement_strategy)
@settings(max_examples=50)
def test_di_diagramelement_instantiation(instance):
    assert isinstance(instance, di_DiagramElement)

@given(instance=di_BPMNShape_strategy)
@settings(max_examples=50)
def test_di_bpmnshape_instantiation(instance):
    assert isinstance(instance, di_BPMNShape)



@given(instance=di_BPMNShape_strategy)
def test_di_bpmnshape_participantBandKind_setter(instance):
    original = instance.participantBandKind
    instance.participantBandKind = original
    assert instance.participantBandKind == original



@given(instance=di_BPMNShape_strategy)
def test_di_bpmnshape_isMessageVisible_setter(instance):
    original = instance.isMessageVisible
    instance.isMessageVisible = original
    assert instance.isMessageVisible == original



@given(instance=di_BPMNShape_strategy)
def test_di_bpmnshape_isExpanded_setter(instance):
    original = instance.isExpanded
    instance.isExpanded = original
    assert instance.isExpanded == original



@given(instance=di_BPMNShape_strategy)
def test_di_bpmnshape_isHorizontal_setter(instance):
    original = instance.isHorizontal
    instance.isHorizontal = original
    assert instance.isHorizontal == original



@given(instance=di_BPMNShape_strategy)
def test_di_bpmnshape_isMarkerVisible_setter(instance):
    original = instance.isMarkerVisible
    instance.isMarkerVisible = original
    assert instance.isMarkerVisible == original

@given(instance=di_BPMNEdge_strategy)
@settings(max_examples=50)
def test_di_bpmnedge_instantiation(instance):
    assert isinstance(instance, di_BPMNEdge)



@given(instance=di_BPMNEdge_strategy)
def test_di_bpmnedge_messageVisibleKind_setter(instance):
    original = instance.messageVisibleKind
    instance.messageVisibleKind = original
    assert instance.messageVisibleKind == original

@given(instance=di_BPMNDiagram_strategy)
@settings(max_examples=50)
def test_di_bpmndiagram_instantiation(instance):
    assert isinstance(instance, di_BPMNDiagram)



@given(instance=di_BPMNDiagram_strategy)
def test_di_bpmndiagram_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=di_BPMNDiagram_strategy)
def test_di_bpmndiagram_featureModel_setter(instance):
    original = instance.featureModel
    instance.featureModel = original
    assert instance.featureModel == original



@given(instance=di_BPMNDiagram_strategy)
def test_di_bpmndiagram_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=di_BPMNDiagram_strategy)
def test_di_bpmndiagram_phase_setter(instance):
    original = instance.phase
    instance.phase = original
    assert instance.phase == original

@given(instance=di_BPMNLabel_strategy)
@settings(max_examples=50)
def test_di_bpmnlabel_instantiation(instance):
    assert isinstance(instance, di_BPMNLabel)

@given(instance=di_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_di_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, di_EStringToStringMapEntry)

@given(instance=di_DocumentRoot_strategy)
@settings(max_examples=50)
def test_di_documentroot_instantiation(instance):
    assert isinstance(instance, di_DocumentRoot)



@given(instance=di_DocumentRoot_strategy)
def test_di_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original
