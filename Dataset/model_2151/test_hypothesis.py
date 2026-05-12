import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Activity,
    bpmn_NamedBpmnObject,
    Graph,
    IdentifiableNode,
    bpmn_Vertex,
    ArtifactsContainer,
    bpmn_Graph,
    Artifact,
    bpmn_TextAnnotation,
    bpmn_DataObject,
    EModelElement,
    bpmn_Identifiable,
    bpmn_Association,
    Identifiable,
    bpmn_IdentifiableNode,
    bpmn_BpmnDiagram,
    bpmn_SubProcess,
    bpmn_Group,
    NamedBpmnObject,
    bpmn_Pool,
    bpmn_ArtifactsContainer,
    bpmn_Lane,
    bpmn_MessagingEdge,
    bpmn_Artifact,
    bpmn_SequenceEdge,
    Vertex,
    bpmn_Activity,
    SequenceFlowConditionType,
    DirectionType,
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



def test_bpmn_namedbpmnobject_is_not_abstract():
    assert not inspect.isabstract(bpmn_NamedBpmnObject)


def test_bpmn_namedbpmnobject_constructor_exists():
    assert callable(bpmn_NamedBpmnObject.__init__)


def test_bpmn_namedbpmnobject_constructor_args():
    sig = inspect.signature(bpmn_NamedBpmnObject.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "name" in params, "Missing parameter 'name'"
    assert "ncname" in params, "Missing parameter 'ncname'"

def test_bpmn_namedbpmnobject_has_documentation():
    assert hasattr(bpmn_NamedBpmnObject, "documentation")
    descriptor = None
    for klass in bpmn_NamedBpmnObject.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_bpmn_namedbpmnobject_has_name():
    assert hasattr(bpmn_NamedBpmnObject, "name")
    descriptor = None
    for klass in bpmn_NamedBpmnObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn_namedbpmnobject_has_ncname():
    assert hasattr(bpmn_NamedBpmnObject, "ncname")
    descriptor = None
    for klass in bpmn_NamedBpmnObject.__mro__:
        if "ncname" in klass.__dict__:
            descriptor = klass.__dict__["ncname"]
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



def test_bpmn_vertex_is_not_abstract():
    assert not inspect.isabstract(bpmn_Vertex)


def test_bpmn_vertex_constructor_exists():
    assert callable(bpmn_Vertex.__init__)


def test_bpmn_vertex_constructor_args():
    sig = inspect.signature(bpmn_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_artifactscontainer_is_not_abstract():
    assert not inspect.isabstract(ArtifactsContainer)


def test_artifactscontainer_constructor_exists():
    assert callable(ArtifactsContainer.__init__)


def test_artifactscontainer_constructor_args():
    sig = inspect.signature(ArtifactsContainer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_graph_is_not_abstract():
    assert not inspect.isabstract(bpmn_Graph)


def test_bpmn_graph_constructor_exists():
    assert callable(bpmn_Graph.__init__)


def test_bpmn_graph_constructor_args():
    sig = inspect.signature(bpmn_Graph.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_textannotation_is_not_abstract():
    assert not inspect.isabstract(bpmn_TextAnnotation)


def test_bpmn_textannotation_constructor_exists():
    assert callable(bpmn_TextAnnotation.__init__)


def test_bpmn_textannotation_constructor_args():
    sig = inspect.signature(bpmn_TextAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_dataobject_is_not_abstract():
    assert not inspect.isabstract(bpmn_DataObject)


def test_bpmn_dataobject_constructor_exists():
    assert callable(bpmn_DataObject.__init__)


def test_bpmn_dataobject_constructor_args():
    sig = inspect.signature(bpmn_DataObject.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_identifiable_is_not_abstract():
    assert not inspect.isabstract(bpmn_Identifiable)


def test_bpmn_identifiable_constructor_exists():
    assert callable(bpmn_Identifiable.__init__)


def test_bpmn_identifiable_constructor_args():
    sig = inspect.signature(bpmn_Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_bpmn_identifiable_has_iD():
    assert hasattr(bpmn_Identifiable, "iD")
    descriptor = None
    for klass in bpmn_Identifiable.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_bpmn_association_is_not_abstract():
    assert not inspect.isabstract(bpmn_Association)


def test_bpmn_association_constructor_exists():
    assert callable(bpmn_Association.__init__)


def test_bpmn_association_constructor_args():
    sig = inspect.signature(bpmn_Association.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_bpmn_association_has_direction():
    assert hasattr(bpmn_Association, "direction")
    descriptor = None
    for klass in bpmn_Association.__mro__:
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



def test_bpmn_identifiablenode_is_not_abstract():
    assert not inspect.isabstract(bpmn_IdentifiableNode)


def test_bpmn_identifiablenode_constructor_exists():
    assert callable(bpmn_IdentifiableNode.__init__)


def test_bpmn_identifiablenode_constructor_args():
    sig = inspect.signature(bpmn_IdentifiableNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_bpmndiagram_is_not_abstract():
    assert not inspect.isabstract(bpmn_BpmnDiagram)


def test_bpmn_bpmndiagram_constructor_exists():
    assert callable(bpmn_BpmnDiagram.__init__)


def test_bpmn_bpmndiagram_constructor_args():
    sig = inspect.signature(bpmn_BpmnDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "title" in params, "Missing parameter 'title'"

def test_bpmn_bpmndiagram_has_author():
    assert hasattr(bpmn_BpmnDiagram, "author")
    descriptor = None
    for klass in bpmn_BpmnDiagram.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bpmn_bpmndiagram_has_title():
    assert hasattr(bpmn_BpmnDiagram, "title")
    descriptor = None
    for klass in bpmn_BpmnDiagram.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bpmn_subprocess_is_not_abstract():
    assert not inspect.isabstract(bpmn_SubProcess)


def test_bpmn_subprocess_constructor_exists():
    assert callable(bpmn_SubProcess.__init__)


def test_bpmn_subprocess_constructor_args():
    sig = inspect.signature(bpmn_SubProcess.__init__)
    params = list(sig.parameters.keys())
    assert "isTransaction" in params, "Missing parameter 'isTransaction'"

def test_bpmn_subprocess_has_isTransaction():
    assert hasattr(bpmn_SubProcess, "isTransaction")
    descriptor = None
    for klass in bpmn_SubProcess.__mro__:
        if "isTransaction" in klass.__dict__:
            descriptor = klass.__dict__["isTransaction"]
            break
    assert isinstance(descriptor, property)



def test_bpmn_group_is_not_abstract():
    assert not inspect.isabstract(bpmn_Group)


def test_bpmn_group_constructor_exists():
    assert callable(bpmn_Group.__init__)


def test_bpmn_group_constructor_args():
    sig = inspect.signature(bpmn_Group.__init__)
    params = list(sig.parameters.keys())



def test_namedbpmnobject_is_not_abstract():
    assert not inspect.isabstract(NamedBpmnObject)


def test_namedbpmnobject_constructor_exists():
    assert callable(NamedBpmnObject.__init__)


def test_namedbpmnobject_constructor_args():
    sig = inspect.signature(NamedBpmnObject.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_pool_is_not_abstract():
    assert not inspect.isabstract(bpmn_Pool)


def test_bpmn_pool_constructor_exists():
    assert callable(bpmn_Pool.__init__)


def test_bpmn_pool_constructor_args():
    sig = inspect.signature(bpmn_Pool.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_artifactscontainer_is_not_abstract():
    assert not inspect.isabstract(bpmn_ArtifactsContainer)


def test_bpmn_artifactscontainer_constructor_exists():
    assert callable(bpmn_ArtifactsContainer.__init__)


def test_bpmn_artifactscontainer_constructor_args():
    sig = inspect.signature(bpmn_ArtifactsContainer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_lane_is_not_abstract():
    assert not inspect.isabstract(bpmn_Lane)


def test_bpmn_lane_constructor_exists():
    assert callable(bpmn_Lane.__init__)


def test_bpmn_lane_constructor_args():
    sig = inspect.signature(bpmn_Lane.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_messagingedge_is_not_abstract():
    assert not inspect.isabstract(bpmn_MessagingEdge)


def test_bpmn_messagingedge_constructor_exists():
    assert callable(bpmn_MessagingEdge.__init__)


def test_bpmn_messagingedge_constructor_args():
    sig = inspect.signature(bpmn_MessagingEdge.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_artifact_is_not_abstract():
    assert not inspect.isabstract(bpmn_Artifact)


def test_bpmn_artifact_constructor_exists():
    assert callable(bpmn_Artifact.__init__)


def test_bpmn_artifact_constructor_args():
    sig = inspect.signature(bpmn_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_sequenceedge_is_not_abstract():
    assert not inspect.isabstract(bpmn_SequenceEdge)


def test_bpmn_sequenceedge_constructor_exists():
    assert callable(bpmn_SequenceEdge.__init__)


def test_bpmn_sequenceedge_constructor_args():
    sig = inspect.signature(bpmn_SequenceEdge.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"
    assert "conditionType" in params, "Missing parameter 'conditionType'"

def test_bpmn_sequenceedge_has_isDefault():
    assert hasattr(bpmn_SequenceEdge, "isDefault")
    descriptor = None
    for klass in bpmn_SequenceEdge.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)

def test_bpmn_sequenceedge_has_conditionType():
    assert hasattr(bpmn_SequenceEdge, "conditionType")
    descriptor = None
    for klass in bpmn_SequenceEdge.__mro__:
        if "conditionType" in klass.__dict__:
            descriptor = klass.__dict__["conditionType"]
            break
    assert isinstance(descriptor, property)



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_bpmn_activity_is_not_abstract():
    assert not inspect.isabstract(bpmn_Activity)


def test_bpmn_activity_constructor_exists():
    assert callable(bpmn_Activity.__init__)


def test_bpmn_activity_constructor_args():
    sig = inspect.signature(bpmn_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "activityType" in params, "Missing parameter 'activityType'"
    assert "orderedMessages" in params, "Missing parameter 'orderedMessages'"
    assert "looping" in params, "Missing parameter 'looping'"

def test_bpmn_activity_has_activityType():
    assert hasattr(bpmn_Activity, "activityType")
    descriptor = None
    for klass in bpmn_Activity.__mro__:
        if "activityType" in klass.__dict__:
            descriptor = klass.__dict__["activityType"]
            break
    assert isinstance(descriptor, property)

def test_bpmn_activity_has_orderedMessages():
    assert hasattr(bpmn_Activity, "orderedMessages")
    descriptor = None
    for klass in bpmn_Activity.__mro__:
        if "orderedMessages" in klass.__dict__:
            descriptor = klass.__dict__["orderedMessages"]
            break
    assert isinstance(descriptor, property)

def test_bpmn_activity_has_looping():
    assert hasattr(bpmn_Activity, "looping")
    descriptor = None
    for klass in bpmn_Activity.__mro__:
        if "looping" in klass.__dict__:
            descriptor = klass.__dict__["looping"]
            break
    assert isinstance(descriptor, property)

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

def test_directiontype_exists():
    # Check that the Enumeration exists
    assert DirectionType is not None

def test_directiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionType]
    expected_literals = [
        "None_",
        "Both",
        "From",
        "To",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionType"

def test_activitytype_exists():
    # Check that the Enumeration exists
    assert ActivityType is not None

def test_activitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityType]
    expected_literals = [
        "GatewayEventBasedExclusive",
        "EventEndCompensation",
        "EventStartMultiple",
        "SubProcess",
        "Task",
        "EventEndMultiple",
        "EventStartEmpty",
        "EventIntermediateRule",
        "EventEndLink",
        "GatewayDataBasedInclusive",
        "EventIntermediateTimer",
        "EventIntermediateMultiple",
        "EventIntermediateEmpty",
        "EventIntermediateCancel",
        "EventStartRule",
        "EventIntermediateLink",
        "EventIntermediateError",
        "EventEndTerminate",
        "EventEndMessage",
        "EventStartLink",
        "EventEndCancel",
        "GatewayComplex",
        "EventEndEmpty",
        "GatewayParallel",
        "EventIntermediateMessage",
        "GatewayDataBasedExclusive",
        "EventStartMessage",
        "EventEndError",
        "EventStartTimer",
        "EventIntermediateCompensation",
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
bpmn_NamedBpmnObject_strategy = st.builds(
    bpmn_NamedBpmnObject,
    documentation=
        safe_text,
    name=
        safe_text,
    ncname=
        safe_text
)
Graph_strategy = st.builds(
    Graph,
)
IdentifiableNode_strategy = st.builds(
    IdentifiableNode,
)
bpmn_Vertex_strategy = st.builds(
    bpmn_Vertex,
)
ArtifactsContainer_strategy = st.builds(
    ArtifactsContainer,
)
bpmn_Graph_strategy = st.builds(
    bpmn_Graph,
)
Artifact_strategy = st.builds(
    Artifact,
)
bpmn_TextAnnotation_strategy = st.builds(
    bpmn_TextAnnotation,
)
bpmn_DataObject_strategy = st.builds(
    bpmn_DataObject,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
bpmn_Identifiable_strategy = st.builds(
    bpmn_Identifiable,
    iD=
        safe_text
)
bpmn_Association_strategy = st.builds(
    bpmn_Association,
    direction=
        safe_text
)
Identifiable_strategy = st.builds(
    Identifiable,
)
bpmn_IdentifiableNode_strategy = st.builds(
    bpmn_IdentifiableNode,
)
bpmn_BpmnDiagram_strategy = st.builds(
    bpmn_BpmnDiagram,
    author=
        safe_text,
    title=
        safe_text
)
bpmn_SubProcess_strategy = st.builds(
    bpmn_SubProcess,
    isTransaction=
        safe_text
)
bpmn_Group_strategy = st.builds(
    bpmn_Group,
)
NamedBpmnObject_strategy = st.builds(
    NamedBpmnObject,
)
bpmn_Pool_strategy = st.builds(
    bpmn_Pool,
)
bpmn_ArtifactsContainer_strategy = st.builds(
    bpmn_ArtifactsContainer,
)
bpmn_Lane_strategy = st.builds(
    bpmn_Lane,
)
bpmn_MessagingEdge_strategy = st.builds(
    bpmn_MessagingEdge,
)
bpmn_Artifact_strategy = st.builds(
    bpmn_Artifact,
)
bpmn_SequenceEdge_strategy = st.builds(
    bpmn_SequenceEdge,
    isDefault=
        safe_text,
    conditionType=
        safe_text
)
Vertex_strategy = st.builds(
    Vertex,
)
bpmn_Activity_strategy = st.builds(
    bpmn_Activity,
    activityType=
        safe_text,
    orderedMessages=
        safe_text,
    looping=
        safe_text
)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=bpmn_NamedBpmnObject_strategy)
@settings(max_examples=50)
def test_bpmn_namedbpmnobject_instantiation(instance):
    assert isinstance(instance, bpmn_NamedBpmnObject)



@given(instance=bpmn_NamedBpmnObject_strategy)
def test_bpmn_namedbpmnobject_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=bpmn_NamedBpmnObject_strategy)
def test_bpmn_namedbpmnobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bpmn_NamedBpmnObject_strategy)
def test_bpmn_namedbpmnobject_ncname_setter(instance):
    original = instance.ncname
    instance.ncname = original
    assert instance.ncname == original

@given(instance=Graph_strategy)
@settings(max_examples=50)
def test_graph_instantiation(instance):
    assert isinstance(instance, Graph)

@given(instance=IdentifiableNode_strategy)
@settings(max_examples=50)
def test_identifiablenode_instantiation(instance):
    assert isinstance(instance, IdentifiableNode)

@given(instance=bpmn_Vertex_strategy)
@settings(max_examples=50)
def test_bpmn_vertex_instantiation(instance):
    assert isinstance(instance, bpmn_Vertex)

@given(instance=ArtifactsContainer_strategy)
@settings(max_examples=50)
def test_artifactscontainer_instantiation(instance):
    assert isinstance(instance, ArtifactsContainer)

@given(instance=bpmn_Graph_strategy)
@settings(max_examples=50)
def test_bpmn_graph_instantiation(instance):
    assert isinstance(instance, bpmn_Graph)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=bpmn_TextAnnotation_strategy)
@settings(max_examples=50)
def test_bpmn_textannotation_instantiation(instance):
    assert isinstance(instance, bpmn_TextAnnotation)

@given(instance=bpmn_DataObject_strategy)
@settings(max_examples=50)
def test_bpmn_dataobject_instantiation(instance):
    assert isinstance(instance, bpmn_DataObject)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=bpmn_Identifiable_strategy)
@settings(max_examples=50)
def test_bpmn_identifiable_instantiation(instance):
    assert isinstance(instance, bpmn_Identifiable)



@given(instance=bpmn_Identifiable_strategy)
def test_bpmn_identifiable_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=bpmn_Association_strategy)
@settings(max_examples=50)
def test_bpmn_association_instantiation(instance):
    assert isinstance(instance, bpmn_Association)



@given(instance=bpmn_Association_strategy)
def test_bpmn_association_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=bpmn_IdentifiableNode_strategy)
@settings(max_examples=50)
def test_bpmn_identifiablenode_instantiation(instance):
    assert isinstance(instance, bpmn_IdentifiableNode)

@given(instance=bpmn_BpmnDiagram_strategy)
@settings(max_examples=50)
def test_bpmn_bpmndiagram_instantiation(instance):
    assert isinstance(instance, bpmn_BpmnDiagram)



@given(instance=bpmn_BpmnDiagram_strategy)
def test_bpmn_bpmndiagram_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=bpmn_BpmnDiagram_strategy)
def test_bpmn_bpmndiagram_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bpmn_SubProcess_strategy)
@settings(max_examples=50)
def test_bpmn_subprocess_instantiation(instance):
    assert isinstance(instance, bpmn_SubProcess)



@given(instance=bpmn_SubProcess_strategy)
def test_bpmn_subprocess_isTransaction_setter(instance):
    original = instance.isTransaction
    instance.isTransaction = original
    assert instance.isTransaction == original

@given(instance=bpmn_Group_strategy)
@settings(max_examples=50)
def test_bpmn_group_instantiation(instance):
    assert isinstance(instance, bpmn_Group)

@given(instance=NamedBpmnObject_strategy)
@settings(max_examples=50)
def test_namedbpmnobject_instantiation(instance):
    assert isinstance(instance, NamedBpmnObject)

@given(instance=bpmn_Pool_strategy)
@settings(max_examples=50)
def test_bpmn_pool_instantiation(instance):
    assert isinstance(instance, bpmn_Pool)

@given(instance=bpmn_ArtifactsContainer_strategy)
@settings(max_examples=50)
def test_bpmn_artifactscontainer_instantiation(instance):
    assert isinstance(instance, bpmn_ArtifactsContainer)

@given(instance=bpmn_Lane_strategy)
@settings(max_examples=50)
def test_bpmn_lane_instantiation(instance):
    assert isinstance(instance, bpmn_Lane)

@given(instance=bpmn_MessagingEdge_strategy)
@settings(max_examples=50)
def test_bpmn_messagingedge_instantiation(instance):
    assert isinstance(instance, bpmn_MessagingEdge)

@given(instance=bpmn_Artifact_strategy)
@settings(max_examples=50)
def test_bpmn_artifact_instantiation(instance):
    assert isinstance(instance, bpmn_Artifact)

@given(instance=bpmn_SequenceEdge_strategy)
@settings(max_examples=50)
def test_bpmn_sequenceedge_instantiation(instance):
    assert isinstance(instance, bpmn_SequenceEdge)



@given(instance=bpmn_SequenceEdge_strategy)
def test_bpmn_sequenceedge_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original



@given(instance=bpmn_SequenceEdge_strategy)
def test_bpmn_sequenceedge_conditionType_setter(instance):
    original = instance.conditionType
    instance.conditionType = original
    assert instance.conditionType == original

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=bpmn_Activity_strategy)
@settings(max_examples=50)
def test_bpmn_activity_instantiation(instance):
    assert isinstance(instance, bpmn_Activity)



@given(instance=bpmn_Activity_strategy)
def test_bpmn_activity_activityType_setter(instance):
    original = instance.activityType
    instance.activityType = original
    assert instance.activityType == original



@given(instance=bpmn_Activity_strategy)
def test_bpmn_activity_orderedMessages_setter(instance):
    original = instance.orderedMessages
    instance.orderedMessages = original
    assert instance.orderedMessages == original



@given(instance=bpmn_Activity_strategy)
def test_bpmn_activity_looping_setter(instance):
    original = instance.looping
    instance.looping = original
    assert instance.looping == original
