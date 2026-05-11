import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Activity,
    bpmn::NamedBpmnObject,
    Graph,
    IdentifiableNode,
    bpmn::Vertex,
    ArtifactsContainer,
    bpmn::Graph,
    Artifact,
    bpmn::TextAnnotation,
    bpmn::DataObject,
    EModelElement,
    bpmn::Identifiable,
    bpmn::Association,
    Identifiable,
    bpmn::IdentifiableNode,
    bpmn::BpmnDiagram,
    bpmn::SubProcess,
    bpmn::Group,
    NamedBpmnObject,
    bpmn::MessagingEdge,
    bpmn::ArtifactsContainer,
    bpmn::Artifact,
    bpmn::Pool,
    bpmn::Lane,
    bpmn::SequenceEdge,
    Vertex,
    bpmn::Activity,
    DirectionType,
    SequenceFlowConditionType,
    ActivityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::namedbpmnobject_is_not_abstract():
    assert not inspect.isabstract(bpmn::NamedBpmnObject)


def test_bpmn::namedbpmnobject_constructor_exists():
    assert callable(bpmn::NamedBpmnObject.__init__)


def test_bpmn::namedbpmnobject_constructor_args():
    sig = inspect.signature(bpmn::NamedBpmnObject.__init__)
    params = list(sig.parameters.keys())
    assert "ncname" in params, "Missing parameter 'ncname'"
    assert "name" in params, "Missing parameter 'name'"
    assert "documentation" in params, "Missing parameter 'documentation'"

def test_bpmn::namedbpmnobject_has_ncname():
    assert hasattr(bpmn::NamedBpmnObject, "ncname")
    descriptor = None
    for klass in bpmn::NamedBpmnObject.__mro__:
        if "ncname" in klass.__dict__:
            descriptor = klass.__dict__["ncname"]
            break
    assert isinstance(descriptor, property)

def test_bpmn::namedbpmnobject_has_name():
    assert hasattr(bpmn::NamedBpmnObject, "name")
    descriptor = None
    for klass in bpmn::NamedBpmnObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn::namedbpmnobject_has_documentation():
    assert hasattr(bpmn::NamedBpmnObject, "documentation")
    descriptor = None
    for klass in bpmn::NamedBpmnObject.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)



def test_graph_is_not_abstract():
    assert not inspect.isabstract(Graph)


def test_graph_constructor_exists():
    assert callable(Graph.__init__)


def test_graph_constructor_args():
    sig = inspect.signature(Graph.__init__)
    params = list(sig.parameters.keys())



def test_identifiablenode_is_not_abstract():
    assert not inspect.isabstract(IdentifiableNode)


def test_identifiablenode_constructor_exists():
    assert callable(IdentifiableNode.__init__)


def test_identifiablenode_constructor_args():
    sig = inspect.signature(IdentifiableNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::vertex_is_not_abstract():
    assert not inspect.isabstract(bpmn::Vertex)


def test_bpmn::vertex_constructor_exists():
    assert callable(bpmn::Vertex.__init__)


def test_bpmn::vertex_constructor_args():
    sig = inspect.signature(bpmn::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_artifactscontainer_is_not_abstract():
    assert not inspect.isabstract(ArtifactsContainer)


def test_artifactscontainer_constructor_exists():
    assert callable(ArtifactsContainer.__init__)


def test_artifactscontainer_constructor_args():
    sig = inspect.signature(ArtifactsContainer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::graph_is_not_abstract():
    assert not inspect.isabstract(bpmn::Graph)


def test_bpmn::graph_constructor_exists():
    assert callable(bpmn::Graph.__init__)


def test_bpmn::graph_constructor_args():
    sig = inspect.signature(bpmn::Graph.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::textannotation_is_not_abstract():
    assert not inspect.isabstract(bpmn::TextAnnotation)


def test_bpmn::textannotation_constructor_exists():
    assert callable(bpmn::TextAnnotation.__init__)


def test_bpmn::textannotation_constructor_args():
    sig = inspect.signature(bpmn::TextAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::dataobject_is_not_abstract():
    assert not inspect.isabstract(bpmn::DataObject)


def test_bpmn::dataobject_constructor_exists():
    assert callable(bpmn::DataObject.__init__)


def test_bpmn::dataobject_constructor_args():
    sig = inspect.signature(bpmn::DataObject.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::identifiable_is_not_abstract():
    assert not inspect.isabstract(bpmn::Identifiable)


def test_bpmn::identifiable_constructor_exists():
    assert callable(bpmn::Identifiable.__init__)


def test_bpmn::identifiable_constructor_args():
    sig = inspect.signature(bpmn::Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_bpmn::identifiable_has_iD():
    assert hasattr(bpmn::Identifiable, "iD")
    descriptor = None
    for klass in bpmn::Identifiable.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_bpmn::association_is_not_abstract():
    assert not inspect.isabstract(bpmn::Association)


def test_bpmn::association_constructor_exists():
    assert callable(bpmn::Association.__init__)


def test_bpmn::association_constructor_args():
    sig = inspect.signature(bpmn::Association.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_bpmn::association_has_direction():
    assert hasattr(bpmn::Association, "direction")
    descriptor = None
    for klass in bpmn::Association.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::identifiablenode_is_not_abstract():
    assert not inspect.isabstract(bpmn::IdentifiableNode)


def test_bpmn::identifiablenode_constructor_exists():
    assert callable(bpmn::IdentifiableNode.__init__)


def test_bpmn::identifiablenode_constructor_args():
    sig = inspect.signature(bpmn::IdentifiableNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::bpmndiagram_is_not_abstract():
    assert not inspect.isabstract(bpmn::BpmnDiagram)


def test_bpmn::bpmndiagram_constructor_exists():
    assert callable(bpmn::BpmnDiagram.__init__)


def test_bpmn::bpmndiagram_constructor_args():
    sig = inspect.signature(bpmn::BpmnDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "title" in params, "Missing parameter 'title'"

def test_bpmn::bpmndiagram_has_author():
    assert hasattr(bpmn::BpmnDiagram, "author")
    descriptor = None
    for klass in bpmn::BpmnDiagram.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bpmn::bpmndiagram_has_title():
    assert hasattr(bpmn::BpmnDiagram, "title")
    descriptor = None
    for klass in bpmn::BpmnDiagram.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bpmn::subprocess_is_not_abstract():
    assert not inspect.isabstract(bpmn::SubProcess)


def test_bpmn::subprocess_constructor_exists():
    assert callable(bpmn::SubProcess.__init__)


def test_bpmn::subprocess_constructor_args():
    sig = inspect.signature(bpmn::SubProcess.__init__)
    params = list(sig.parameters.keys())
    assert "isTransaction" in params, "Missing parameter 'isTransaction'"

def test_bpmn::subprocess_has_isTransaction():
    assert hasattr(bpmn::SubProcess, "isTransaction")
    descriptor = None
    for klass in bpmn::SubProcess.__mro__:
        if "isTransaction" in klass.__dict__:
            descriptor = klass.__dict__["isTransaction"]
            break
    assert isinstance(descriptor, property)



def test_bpmn::group_is_not_abstract():
    assert not inspect.isabstract(bpmn::Group)


def test_bpmn::group_constructor_exists():
    assert callable(bpmn::Group.__init__)


def test_bpmn::group_constructor_args():
    sig = inspect.signature(bpmn::Group.__init__)
    params = list(sig.parameters.keys())



def test_namedbpmnobject_is_not_abstract():
    assert not inspect.isabstract(NamedBpmnObject)


def test_namedbpmnobject_constructor_exists():
    assert callable(NamedBpmnObject.__init__)


def test_namedbpmnobject_constructor_args():
    sig = inspect.signature(NamedBpmnObject.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::messagingedge_is_not_abstract():
    assert not inspect.isabstract(bpmn::MessagingEdge)


def test_bpmn::messagingedge_constructor_exists():
    assert callable(bpmn::MessagingEdge.__init__)


def test_bpmn::messagingedge_constructor_args():
    sig = inspect.signature(bpmn::MessagingEdge.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::artifactscontainer_is_not_abstract():
    assert not inspect.isabstract(bpmn::ArtifactsContainer)


def test_bpmn::artifactscontainer_constructor_exists():
    assert callable(bpmn::ArtifactsContainer.__init__)


def test_bpmn::artifactscontainer_constructor_args():
    sig = inspect.signature(bpmn::ArtifactsContainer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::artifact_is_not_abstract():
    assert not inspect.isabstract(bpmn::Artifact)


def test_bpmn::artifact_constructor_exists():
    assert callable(bpmn::Artifact.__init__)


def test_bpmn::artifact_constructor_args():
    sig = inspect.signature(bpmn::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::pool_is_not_abstract():
    assert not inspect.isabstract(bpmn::Pool)


def test_bpmn::pool_constructor_exists():
    assert callable(bpmn::Pool.__init__)


def test_bpmn::pool_constructor_args():
    sig = inspect.signature(bpmn::Pool.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::lane_is_not_abstract():
    assert not inspect.isabstract(bpmn::Lane)


def test_bpmn::lane_constructor_exists():
    assert callable(bpmn::Lane.__init__)


def test_bpmn::lane_constructor_args():
    sig = inspect.signature(bpmn::Lane.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::sequenceedge_is_not_abstract():
    assert not inspect.isabstract(bpmn::SequenceEdge)


def test_bpmn::sequenceedge_constructor_exists():
    assert callable(bpmn::SequenceEdge.__init__)


def test_bpmn::sequenceedge_constructor_args():
    sig = inspect.signature(bpmn::SequenceEdge.__init__)
    params = list(sig.parameters.keys())
    assert "conditionType" in params, "Missing parameter 'conditionType'"
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_bpmn::sequenceedge_has_conditionType():
    assert hasattr(bpmn::SequenceEdge, "conditionType")
    descriptor = None
    for klass in bpmn::SequenceEdge.__mro__:
        if "conditionType" in klass.__dict__:
            descriptor = klass.__dict__["conditionType"]
            break
    assert isinstance(descriptor, property)

def test_bpmn::sequenceedge_has_isDefault():
    assert hasattr(bpmn::SequenceEdge, "isDefault")
    descriptor = None
    for klass in bpmn::SequenceEdge.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_bpmn::activity_is_not_abstract():
    assert not inspect.isabstract(bpmn::Activity)


def test_bpmn::activity_constructor_exists():
    assert callable(bpmn::Activity.__init__)


def test_bpmn::activity_constructor_args():
    sig = inspect.signature(bpmn::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "looping" in params, "Missing parameter 'looping'"
    assert "orderedMessages" in params, "Missing parameter 'orderedMessages'"
    assert "activityType" in params, "Missing parameter 'activityType'"

def test_bpmn::activity_has_looping():
    assert hasattr(bpmn::Activity, "looping")
    descriptor = None
    for klass in bpmn::Activity.__mro__:
        if "looping" in klass.__dict__:
            descriptor = klass.__dict__["looping"]
            break
    assert isinstance(descriptor, property)

def test_bpmn::activity_has_orderedMessages():
    assert hasattr(bpmn::Activity, "orderedMessages")
    descriptor = None
    for klass in bpmn::Activity.__mro__:
        if "orderedMessages" in klass.__dict__:
            descriptor = klass.__dict__["orderedMessages"]
            break
    assert isinstance(descriptor, property)

def test_bpmn::activity_has_activityType():
    assert hasattr(bpmn::Activity, "activityType")
    descriptor = None
    for klass in bpmn::Activity.__mro__:
        if "activityType" in klass.__dict__:
            descriptor = klass.__dict__["activityType"]
            break
    assert isinstance(descriptor, property)

def test_directiontype_exists():
    # Check that the Enumeration exists
    assert DirectionType is not None

def test_directiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionType]
    expected_literals = [
        "To",
        "From",
        "None_",
        "Both",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionType"

def test_sequenceflowconditiontype_exists():
    # Check that the Enumeration exists
    assert SequenceFlowConditionType is not None

def test_sequenceflowconditiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SequenceFlowConditionType]
    expected_literals = [
        "Default",
        "Expression",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SequenceFlowConditionType"

def test_activitytype_exists():
    # Check that the Enumeration exists
    assert ActivityType is not None

def test_activitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityType]
    expected_literals = [
        "EventStartMultiple",
        "EventIntermediateCancel",
        "EventIntermediateMessage",
        "EventIntermediateCompensation",
        "EventEndCancel",
        "EventIntermediateMultiple",
        "GatewayEventBasedExclusive",
        "EventStartTimer",
        "GatewayDataBasedExclusive",
        "EventIntermediateLink",
        "EventIntermediateError",
        "EventEndMessage",
        "EventIntermediateTimer",
        "GatewayComplex",
        "EventEndError",
        "GatewayDataBasedInclusive",
        "EventIntermediateEmpty",
        "EventIntermediateRule",
        "EventStartRule",
        "EventEndEmpty",
        "SubProcess",
        "EventEndCompensation",
        "EventEndLink",
        "EventEndTerminate",
        "EventEndMultiple",
        "EventStartEmpty",
        "EventStartMessage",
        "Task",
        "EventStartLink",
        "GatewayParallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityType"


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
Activity_strategy = st.builds(
    Activity,
)
bpmn::NamedBpmnObject_strategy = st.builds(
    bpmn::NamedBpmnObject,
    ncname=
        safe_text,
    name=
        safe_text,
    documentation=
        safe_text
)
Graph_strategy = st.builds(
    Graph,
)
IdentifiableNode_strategy = st.builds(
    IdentifiableNode,
)
bpmn::Vertex_strategy = st.builds(
    bpmn::Vertex,
)
ArtifactsContainer_strategy = st.builds(
    ArtifactsContainer,
)
bpmn::Graph_strategy = st.builds(
    bpmn::Graph,
)
Artifact_strategy = st.builds(
    Artifact,
)
bpmn::TextAnnotation_strategy = st.builds(
    bpmn::TextAnnotation,
)
bpmn::DataObject_strategy = st.builds(
    bpmn::DataObject,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
bpmn::Identifiable_strategy = st.builds(
    bpmn::Identifiable,
    iD=
        safe_text
)
bpmn::Association_strategy = st.builds(
    bpmn::Association,
    direction=
        safe_text
)
Identifiable_strategy = st.builds(
    Identifiable,
)
bpmn::IdentifiableNode_strategy = st.builds(
    bpmn::IdentifiableNode,
)
bpmn::BpmnDiagram_strategy = st.builds(
    bpmn::BpmnDiagram,
    author=
        safe_text,
    title=
        safe_text
)
bpmn::SubProcess_strategy = st.builds(
    bpmn::SubProcess,
    isTransaction=
        safe_text
)
bpmn::Group_strategy = st.builds(
    bpmn::Group,
)
NamedBpmnObject_strategy = st.builds(
    NamedBpmnObject,
)
bpmn::MessagingEdge_strategy = st.builds(
    bpmn::MessagingEdge,
)
bpmn::ArtifactsContainer_strategy = st.builds(
    bpmn::ArtifactsContainer,
)
bpmn::Artifact_strategy = st.builds(
    bpmn::Artifact,
)
bpmn::Pool_strategy = st.builds(
    bpmn::Pool,
)
bpmn::Lane_strategy = st.builds(
    bpmn::Lane,
)
bpmn::SequenceEdge_strategy = st.builds(
    bpmn::SequenceEdge,
    conditionType=
        safe_text,
    isDefault=
        safe_text
)
Vertex_strategy = st.builds(
    Vertex,
)
bpmn::Activity_strategy = st.builds(
    bpmn::Activity,
    looping=
        safe_text,
    orderedMessages=
        safe_text,
    activityType=
        safe_text
)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=bpmn::NamedBpmnObject_strategy)
@settings(max_examples=50)
def test_bpmn::namedbpmnobject_instantiation(instance):
    assert isinstance(instance, bpmn::NamedBpmnObject)

@given(instance=bpmn::NamedBpmnObject_strategy)
def test_bpmn::namedbpmnobject_ncname_type(instance):
    assert isinstance(instance.ncname, str)


@given(instance=bpmn::NamedBpmnObject_strategy)
def test_bpmn::namedbpmnobject_ncname_setter(instance):
    original = instance.ncname
    instance.ncname = original
    assert instance.ncname == original

@given(instance=bpmn::NamedBpmnObject_strategy)
def test_bpmn::namedbpmnobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bpmn::NamedBpmnObject_strategy)
def test_bpmn::namedbpmnobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn::NamedBpmnObject_strategy)
def test_bpmn::namedbpmnobject_documentation_type(instance):
    assert isinstance(instance.documentation, str)


@given(instance=bpmn::NamedBpmnObject_strategy)
def test_bpmn::namedbpmnobject_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=Graph_strategy)
@settings(max_examples=50)
def test_graph_instantiation(instance):
    assert isinstance(instance, Graph)

@given(instance=IdentifiableNode_strategy)
@settings(max_examples=50)
def test_identifiablenode_instantiation(instance):
    assert isinstance(instance, IdentifiableNode)

@given(instance=bpmn::Vertex_strategy)
@settings(max_examples=50)
def test_bpmn::vertex_instantiation(instance):
    assert isinstance(instance, bpmn::Vertex)

@given(instance=ArtifactsContainer_strategy)
@settings(max_examples=50)
def test_artifactscontainer_instantiation(instance):
    assert isinstance(instance, ArtifactsContainer)

@given(instance=bpmn::Graph_strategy)
@settings(max_examples=50)
def test_bpmn::graph_instantiation(instance):
    assert isinstance(instance, bpmn::Graph)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=bpmn::TextAnnotation_strategy)
@settings(max_examples=50)
def test_bpmn::textannotation_instantiation(instance):
    assert isinstance(instance, bpmn::TextAnnotation)

@given(instance=bpmn::DataObject_strategy)
@settings(max_examples=50)
def test_bpmn::dataobject_instantiation(instance):
    assert isinstance(instance, bpmn::DataObject)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=bpmn::Identifiable_strategy)
@settings(max_examples=50)
def test_bpmn::identifiable_instantiation(instance):
    assert isinstance(instance, bpmn::Identifiable)

@given(instance=bpmn::Identifiable_strategy)
def test_bpmn::identifiable_iD_type(instance):
    assert isinstance(instance.iD, str)


@given(instance=bpmn::Identifiable_strategy)
def test_bpmn::identifiable_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=bpmn::Association_strategy)
@settings(max_examples=50)
def test_bpmn::association_instantiation(instance):
    assert isinstance(instance, bpmn::Association)

@given(instance=bpmn::Association_strategy)
def test_bpmn::association_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=bpmn::Association_strategy)
def test_bpmn::association_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=bpmn::IdentifiableNode_strategy)
@settings(max_examples=50)
def test_bpmn::identifiablenode_instantiation(instance):
    assert isinstance(instance, bpmn::IdentifiableNode)

@given(instance=bpmn::BpmnDiagram_strategy)
@settings(max_examples=50)
def test_bpmn::bpmndiagram_instantiation(instance):
    assert isinstance(instance, bpmn::BpmnDiagram)

@given(instance=bpmn::BpmnDiagram_strategy)
def test_bpmn::bpmndiagram_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bpmn::BpmnDiagram_strategy)
def test_bpmn::bpmndiagram_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bpmn::BpmnDiagram_strategy)
def test_bpmn::bpmndiagram_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bpmn::BpmnDiagram_strategy)
def test_bpmn::bpmndiagram_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bpmn::SubProcess_strategy)
@settings(max_examples=50)
def test_bpmn::subprocess_instantiation(instance):
    assert isinstance(instance, bpmn::SubProcess)

@given(instance=bpmn::SubProcess_strategy)
def test_bpmn::subprocess_isTransaction_type(instance):
    assert isinstance(instance.isTransaction, str)


@given(instance=bpmn::SubProcess_strategy)
def test_bpmn::subprocess_isTransaction_setter(instance):
    original = instance.isTransaction
    instance.isTransaction = original
    assert instance.isTransaction == original

@given(instance=bpmn::Group_strategy)
@settings(max_examples=50)
def test_bpmn::group_instantiation(instance):
    assert isinstance(instance, bpmn::Group)

@given(instance=NamedBpmnObject_strategy)
@settings(max_examples=50)
def test_namedbpmnobject_instantiation(instance):
    assert isinstance(instance, NamedBpmnObject)

@given(instance=bpmn::MessagingEdge_strategy)
@settings(max_examples=50)
def test_bpmn::messagingedge_instantiation(instance):
    assert isinstance(instance, bpmn::MessagingEdge)

@given(instance=bpmn::ArtifactsContainer_strategy)
@settings(max_examples=50)
def test_bpmn::artifactscontainer_instantiation(instance):
    assert isinstance(instance, bpmn::ArtifactsContainer)

@given(instance=bpmn::Artifact_strategy)
@settings(max_examples=50)
def test_bpmn::artifact_instantiation(instance):
    assert isinstance(instance, bpmn::Artifact)

@given(instance=bpmn::Pool_strategy)
@settings(max_examples=50)
def test_bpmn::pool_instantiation(instance):
    assert isinstance(instance, bpmn::Pool)

@given(instance=bpmn::Lane_strategy)
@settings(max_examples=50)
def test_bpmn::lane_instantiation(instance):
    assert isinstance(instance, bpmn::Lane)

@given(instance=bpmn::SequenceEdge_strategy)
@settings(max_examples=50)
def test_bpmn::sequenceedge_instantiation(instance):
    assert isinstance(instance, bpmn::SequenceEdge)

@given(instance=bpmn::SequenceEdge_strategy)
def test_bpmn::sequenceedge_conditionType_type(instance):
    assert isinstance(instance.conditionType, str)


@given(instance=bpmn::SequenceEdge_strategy)
def test_bpmn::sequenceedge_conditionType_setter(instance):
    original = instance.conditionType
    instance.conditionType = original
    assert instance.conditionType == original

@given(instance=bpmn::SequenceEdge_strategy)
def test_bpmn::sequenceedge_isDefault_type(instance):
    assert isinstance(instance.isDefault, str)


@given(instance=bpmn::SequenceEdge_strategy)
def test_bpmn::sequenceedge_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=bpmn::Activity_strategy)
@settings(max_examples=50)
def test_bpmn::activity_instantiation(instance):
    assert isinstance(instance, bpmn::Activity)

@given(instance=bpmn::Activity_strategy)
def test_bpmn::activity_looping_type(instance):
    assert isinstance(instance.looping, str)


@given(instance=bpmn::Activity_strategy)
def test_bpmn::activity_looping_setter(instance):
    original = instance.looping
    instance.looping = original
    assert instance.looping == original

@given(instance=bpmn::Activity_strategy)
def test_bpmn::activity_orderedMessages_type(instance):
    assert isinstance(instance.orderedMessages, str)


@given(instance=bpmn::Activity_strategy)
def test_bpmn::activity_orderedMessages_setter(instance):
    original = instance.orderedMessages
    instance.orderedMessages = original
    assert instance.orderedMessages == original

@given(instance=bpmn::Activity_strategy)
def test_bpmn::activity_activityType_type(instance):
    assert isinstance(instance.activityType, str)


@given(instance=bpmn::Activity_strategy)
def test_bpmn::activity_activityType_setter(instance):
    original = instance.activityType
    instance.activityType = original
    assert instance.activityType == original
