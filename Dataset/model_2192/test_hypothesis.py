import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sample_Comment,
    sample_Node,
    PhysicalNode,
    sample_LocalNode,
    sample_RemoteNode,
    Node,
    sample_VirtualNode,
    sample_PhysicalNode,
    sample_Tree,
    sample_Type,
    sample_DataTypeMap,
    sample_StringMap,
    sample_TypeMapReference,
    sample_TypeMap,
    sample_ETypes,
    sample_TargetObject,
    sample_PrimaryObject,
    sample_Value,
    SomeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample_comment_is_not_abstract():
    assert not inspect.isabstract(sample_Comment)


def test_sample_comment_constructor_exists():
    assert callable(sample_Comment.__init__)


def test_sample_comment_constructor_args():
    sig = inspect.signature(sample_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_sample_comment_has_content():
    assert hasattr(sample_Comment, "content")
    descriptor = None
    for klass in sample_Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_sample_node_is_not_abstract():
    assert not inspect.isabstract(sample_Node)


def test_sample_node_constructor_exists():
    assert callable(sample_Node.__init__)


def test_sample_node_constructor_args():
    sig = inspect.signature(sample_Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_sample_node_has_label():
    assert hasattr(sample_Node, "label")
    descriptor = None
    for klass in sample_Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_physicalnode_is_not_abstract():
    assert not inspect.isabstract(PhysicalNode)


def test_physicalnode_constructor_exists():
    assert callable(PhysicalNode.__init__)


def test_physicalnode_constructor_args():
    sig = inspect.signature(PhysicalNode.__init__)
    params = list(sig.parameters.keys())



def test_sample_localnode_is_not_abstract():
    assert not inspect.isabstract(sample_LocalNode)


def test_sample_localnode_constructor_exists():
    assert callable(sample_LocalNode.__init__)


def test_sample_localnode_constructor_args():
    sig = inspect.signature(sample_LocalNode.__init__)
    params = list(sig.parameters.keys())



def test_sample_remotenode_is_not_abstract():
    assert not inspect.isabstract(sample_RemoteNode)


def test_sample_remotenode_constructor_exists():
    assert callable(sample_RemoteNode.__init__)


def test_sample_remotenode_constructor_args():
    sig = inspect.signature(sample_RemoteNode.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_sample_virtualnode_is_not_abstract():
    assert not inspect.isabstract(sample_VirtualNode)


def test_sample_virtualnode_constructor_exists():
    assert callable(sample_VirtualNode.__init__)


def test_sample_virtualnode_constructor_args():
    sig = inspect.signature(sample_VirtualNode.__init__)
    params = list(sig.parameters.keys())



def test_sample_physicalnode_is_not_abstract():
    assert not inspect.isabstract(sample_PhysicalNode)


def test_sample_physicalnode_constructor_exists():
    assert callable(sample_PhysicalNode.__init__)


def test_sample_physicalnode_constructor_args():
    sig = inspect.signature(sample_PhysicalNode.__init__)
    params = list(sig.parameters.keys())



def test_sample_tree_is_not_abstract():
    assert not inspect.isabstract(sample_Tree)


def test_sample_tree_constructor_exists():
    assert callable(sample_Tree.__init__)


def test_sample_tree_constructor_args():
    sig = inspect.signature(sample_Tree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample_tree_has_name():
    assert hasattr(sample_Tree, "name")
    descriptor = None
    for klass in sample_Tree.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample_type_is_not_abstract():
    assert not inspect.isabstract(sample_Type)


def test_sample_type_constructor_exists():
    assert callable(sample_Type.__init__)


def test_sample_type_constructor_args():
    sig = inspect.signature(sample_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample_type_has_name():
    assert hasattr(sample_Type, "name")
    descriptor = None
    for klass in sample_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample_datatypemap_is_not_abstract():
    assert not inspect.isabstract(sample_DataTypeMap)


def test_sample_datatypemap_constructor_exists():
    assert callable(sample_DataTypeMap.__init__)


def test_sample_datatypemap_constructor_args():
    sig = inspect.signature(sample_DataTypeMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sample_datatypemap_has_value():
    assert hasattr(sample_DataTypeMap, "value")
    descriptor = None
    for klass in sample_DataTypeMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sample_datatypemap_has_key():
    assert hasattr(sample_DataTypeMap, "key")
    descriptor = None
    for klass in sample_DataTypeMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_sample_stringmap_is_not_abstract():
    assert not inspect.isabstract(sample_StringMap)


def test_sample_stringmap_constructor_exists():
    assert callable(sample_StringMap.__init__)


def test_sample_stringmap_constructor_args():
    sig = inspect.signature(sample_StringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sample_stringmap_has_value():
    assert hasattr(sample_StringMap, "value")
    descriptor = None
    for klass in sample_StringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sample_stringmap_has_key():
    assert hasattr(sample_StringMap, "key")
    descriptor = None
    for klass in sample_StringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_sample_typemapreference_is_not_abstract():
    assert not inspect.isabstract(sample_TypeMapReference)


def test_sample_typemapreference_constructor_exists():
    assert callable(sample_TypeMapReference.__init__)


def test_sample_typemapreference_constructor_args():
    sig = inspect.signature(sample_TypeMapReference.__init__)
    params = list(sig.parameters.keys())



def test_sample_typemap_is_not_abstract():
    assert not inspect.isabstract(sample_TypeMap)


def test_sample_typemap_constructor_exists():
    assert callable(sample_TypeMap.__init__)


def test_sample_typemap_constructor_args():
    sig = inspect.signature(sample_TypeMap.__init__)
    params = list(sig.parameters.keys())



def test_sample_etypes_is_not_abstract():
    assert not inspect.isabstract(sample_ETypes)


def test_sample_etypes_constructor_exists():
    assert callable(sample_ETypes.__init__)


def test_sample_etypes_constructor_args():
    sig = inspect.signature(sample_ETypes.__init__)
    params = list(sig.parameters.keys())
    assert "uris" in params, "Missing parameter 'uris'"

def test_sample_etypes_has_uris():
    assert hasattr(sample_ETypes, "uris")
    descriptor = None
    for klass in sample_ETypes.__mro__:
        if "uris" in klass.__dict__:
            descriptor = klass.__dict__["uris"]
            break
    assert isinstance(descriptor, property)



def test_sample_targetobject_is_not_abstract():
    assert not inspect.isabstract(sample_TargetObject)


def test_sample_targetobject_constructor_exists():
    assert callable(sample_TargetObject.__init__)


def test_sample_targetobject_constructor_args():
    sig = inspect.signature(sample_TargetObject.__init__)
    params = list(sig.parameters.keys())
    assert "singleAttribute" in params, "Missing parameter 'singleAttribute'"
    assert "name" in params, "Missing parameter 'name'"
    assert "manyAttributes" in params, "Missing parameter 'manyAttributes'"

def test_sample_targetobject_has_singleAttribute():
    assert hasattr(sample_TargetObject, "singleAttribute")
    descriptor = None
    for klass in sample_TargetObject.__mro__:
        if "singleAttribute" in klass.__dict__:
            descriptor = klass.__dict__["singleAttribute"]
            break
    assert isinstance(descriptor, property)

def test_sample_targetobject_has_name():
    assert hasattr(sample_TargetObject, "name")
    descriptor = None
    for klass in sample_TargetObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sample_targetobject_has_manyAttributes():
    assert hasattr(sample_TargetObject, "manyAttributes")
    descriptor = None
    for klass in sample_TargetObject.__mro__:
        if "manyAttributes" in klass.__dict__:
            descriptor = klass.__dict__["manyAttributes"]
            break
    assert isinstance(descriptor, property)



def test_sample_primaryobject_is_not_abstract():
    assert not inspect.isabstract(sample_PrimaryObject)


def test_sample_primaryobject_constructor_exists():
    assert callable(sample_PrimaryObject.__init__)


def test_sample_primaryobject_constructor_args():
    sig = inspect.signature(sample_PrimaryObject.__init__)
    params = list(sig.parameters.keys())
    assert "featureMapReferenceCollection" in params, "Missing parameter 'featureMapReferenceCollection'"
    assert "id" in params, "Missing parameter 'id'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "featureMapAttributeType2" in params, "Missing parameter 'featureMapAttributeType2'"
    assert "featureMapAttributeType1" in params, "Missing parameter 'featureMapAttributeType1'"
    assert "unsettableAttribute" in params, "Missing parameter 'unsettableAttribute'"
    assert "unsettableAttributeWithDefault" in params, "Missing parameter 'unsettableAttributeWithDefault'"
    assert "name" in params, "Missing parameter 'name'"
    assert "featureMapAttributeCollection" in params, "Missing parameter 'featureMapAttributeCollection'"

def test_sample_primaryobject_has_featureMapReferenceCollection():
    assert hasattr(sample_PrimaryObject, "featureMapReferenceCollection")
    descriptor = None
    for klass in sample_PrimaryObject.__mro__:
        if "featureMapReferenceCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapReferenceCollection"]
            break
    assert isinstance(descriptor, property)

def test_sample_primaryobject_has_id():
    assert hasattr(sample_PrimaryObject, "id")
    descriptor = None
    for klass in sample_PrimaryObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sample_primaryobject_has_kind():
    assert hasattr(sample_PrimaryObject, "kind")
    descriptor = None
    for klass in sample_PrimaryObject.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_sample_primaryobject_has_featureMapAttributeType2():
    assert hasattr(sample_PrimaryObject, "featureMapAttributeType2")
    descriptor = None
    for klass in sample_PrimaryObject.__mro__:
        if "featureMapAttributeType2" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeType2"]
            break
    assert isinstance(descriptor, property)

def test_sample_primaryobject_has_featureMapAttributeType1():
    assert hasattr(sample_PrimaryObject, "featureMapAttributeType1")
    descriptor = None
    for klass in sample_PrimaryObject.__mro__:
        if "featureMapAttributeType1" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeType1"]
            break
    assert isinstance(descriptor, property)

def test_sample_primaryobject_has_unsettableAttribute():
    assert hasattr(sample_PrimaryObject, "unsettableAttribute")
    descriptor = None
    for klass in sample_PrimaryObject.__mro__:
        if "unsettableAttribute" in klass.__dict__:
            descriptor = klass.__dict__["unsettableAttribute"]
            break
    assert isinstance(descriptor, property)

def test_sample_primaryobject_has_unsettableAttributeWithDefault():
    assert hasattr(sample_PrimaryObject, "unsettableAttributeWithDefault")
    descriptor = None
    for klass in sample_PrimaryObject.__mro__:
        if "unsettableAttributeWithDefault" in klass.__dict__:
            descriptor = klass.__dict__["unsettableAttributeWithDefault"]
            break
    assert isinstance(descriptor, property)

def test_sample_primaryobject_has_name():
    assert hasattr(sample_PrimaryObject, "name")
    descriptor = None
    for klass in sample_PrimaryObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sample_primaryobject_has_featureMapAttributeCollection():
    assert hasattr(sample_PrimaryObject, "featureMapAttributeCollection")
    descriptor = None
    for klass in sample_PrimaryObject.__mro__:
        if "featureMapAttributeCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeCollection"]
            break
    assert isinstance(descriptor, property)



def test_sample_value_is_not_abstract():
    assert not inspect.isabstract(sample_Value)


def test_sample_value_constructor_exists():
    assert callable(sample_Value.__init__)


def test_sample_value_constructor_args():
    sig = inspect.signature(sample_Value.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sample_value_has_value():
    assert hasattr(sample_Value, "value")
    descriptor = None
    for klass in sample_Value.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_somekind_exists():
    # Check that the Enumeration exists
    assert SomeKind is not None

def test_somekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SomeKind]
    expected_literals = [
        "Two",
        "one",
        "Three",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SomeKind"


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
sample_Comment_strategy = st.builds(
    sample_Comment,
    content=
        safe_text
)
sample_Node_strategy = st.builds(
    sample_Node,
    label=
        safe_text
)
PhysicalNode_strategy = st.builds(
    PhysicalNode,
)
sample_LocalNode_strategy = st.builds(
    sample_LocalNode,
)
sample_RemoteNode_strategy = st.builds(
    sample_RemoteNode,
)
Node_strategy = st.builds(
    Node,
)
sample_VirtualNode_strategy = st.builds(
    sample_VirtualNode,
)
sample_PhysicalNode_strategy = st.builds(
    sample_PhysicalNode,
)
sample_Tree_strategy = st.builds(
    sample_Tree,
    name=
        safe_text
)
sample_Type_strategy = st.builds(
    sample_Type,
    name=
        safe_text
)
sample_DataTypeMap_strategy = st.builds(
    sample_DataTypeMap,
    value=
        safe_text,
    key=
        safe_text
)
sample_StringMap_strategy = st.builds(
    sample_StringMap,
    value=
        safe_text,
    key=
        safe_text
)
sample_TypeMapReference_strategy = st.builds(
    sample_TypeMapReference,
)
sample_TypeMap_strategy = st.builds(
    sample_TypeMap,
)
sample_ETypes_strategy = st.builds(
    sample_ETypes,
    uris=
        safe_text
)
sample_TargetObject_strategy = st.builds(
    sample_TargetObject,
    singleAttribute=
        safe_text,
    name=
        safe_text,
    manyAttributes=
        safe_text
)
sample_PrimaryObject_strategy = st.builds(
    sample_PrimaryObject,
    featureMapReferenceCollection=
        safe_text,
    id=
        safe_text,
    kind=
        safe_text,
    featureMapAttributeType2=
        safe_text,
    featureMapAttributeType1=
        safe_text,
    unsettableAttribute=
        safe_text,
    unsettableAttributeWithDefault=
        safe_text,
    name=
        safe_text,
    featureMapAttributeCollection=
        safe_text
)
sample_Value_strategy = st.builds(
    sample_Value,
    value=
        st.integers()
)

@given(instance=sample_Comment_strategy)
@settings(max_examples=50)
def test_sample_comment_instantiation(instance):
    assert isinstance(instance, sample_Comment)



@given(instance=sample_Comment_strategy)
def test_sample_comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=sample_Node_strategy)
@settings(max_examples=50)
def test_sample_node_instantiation(instance):
    assert isinstance(instance, sample_Node)



@given(instance=sample_Node_strategy)
def test_sample_node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=PhysicalNode_strategy)
@settings(max_examples=50)
def test_physicalnode_instantiation(instance):
    assert isinstance(instance, PhysicalNode)

@given(instance=sample_LocalNode_strategy)
@settings(max_examples=50)
def test_sample_localnode_instantiation(instance):
    assert isinstance(instance, sample_LocalNode)

@given(instance=sample_RemoteNode_strategy)
@settings(max_examples=50)
def test_sample_remotenode_instantiation(instance):
    assert isinstance(instance, sample_RemoteNode)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=sample_VirtualNode_strategy)
@settings(max_examples=50)
def test_sample_virtualnode_instantiation(instance):
    assert isinstance(instance, sample_VirtualNode)

@given(instance=sample_PhysicalNode_strategy)
@settings(max_examples=50)
def test_sample_physicalnode_instantiation(instance):
    assert isinstance(instance, sample_PhysicalNode)

@given(instance=sample_Tree_strategy)
@settings(max_examples=50)
def test_sample_tree_instantiation(instance):
    assert isinstance(instance, sample_Tree)



@given(instance=sample_Tree_strategy)
def test_sample_tree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample_Type_strategy)
@settings(max_examples=50)
def test_sample_type_instantiation(instance):
    assert isinstance(instance, sample_Type)



@given(instance=sample_Type_strategy)
def test_sample_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample_DataTypeMap_strategy)
@settings(max_examples=50)
def test_sample_datatypemap_instantiation(instance):
    assert isinstance(instance, sample_DataTypeMap)



@given(instance=sample_DataTypeMap_strategy)
def test_sample_datatypemap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=sample_DataTypeMap_strategy)
def test_sample_datatypemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=sample_StringMap_strategy)
@settings(max_examples=50)
def test_sample_stringmap_instantiation(instance):
    assert isinstance(instance, sample_StringMap)



@given(instance=sample_StringMap_strategy)
def test_sample_stringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=sample_StringMap_strategy)
def test_sample_stringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=sample_TypeMapReference_strategy)
@settings(max_examples=50)
def test_sample_typemapreference_instantiation(instance):
    assert isinstance(instance, sample_TypeMapReference)

@given(instance=sample_TypeMap_strategy)
@settings(max_examples=50)
def test_sample_typemap_instantiation(instance):
    assert isinstance(instance, sample_TypeMap)

@given(instance=sample_ETypes_strategy)
@settings(max_examples=50)
def test_sample_etypes_instantiation(instance):
    assert isinstance(instance, sample_ETypes)



@given(instance=sample_ETypes_strategy)
def test_sample_etypes_uris_setter(instance):
    original = instance.uris
    instance.uris = original
    assert instance.uris == original

@given(instance=sample_TargetObject_strategy)
@settings(max_examples=50)
def test_sample_targetobject_instantiation(instance):
    assert isinstance(instance, sample_TargetObject)



@given(instance=sample_TargetObject_strategy)
def test_sample_targetobject_singleAttribute_setter(instance):
    original = instance.singleAttribute
    instance.singleAttribute = original
    assert instance.singleAttribute == original



@given(instance=sample_TargetObject_strategy)
def test_sample_targetobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sample_TargetObject_strategy)
def test_sample_targetobject_manyAttributes_setter(instance):
    original = instance.manyAttributes
    instance.manyAttributes = original
    assert instance.manyAttributes == original

@given(instance=sample_PrimaryObject_strategy)
@settings(max_examples=50)
def test_sample_primaryobject_instantiation(instance):
    assert isinstance(instance, sample_PrimaryObject)



@given(instance=sample_PrimaryObject_strategy)
def test_sample_primaryobject_featureMapReferenceCollection_setter(instance):
    original = instance.featureMapReferenceCollection
    instance.featureMapReferenceCollection = original
    assert instance.featureMapReferenceCollection == original



@given(instance=sample_PrimaryObject_strategy)
def test_sample_primaryobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=sample_PrimaryObject_strategy)
def test_sample_primaryobject_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=sample_PrimaryObject_strategy)
def test_sample_primaryobject_featureMapAttributeType2_setter(instance):
    original = instance.featureMapAttributeType2
    instance.featureMapAttributeType2 = original
    assert instance.featureMapAttributeType2 == original



@given(instance=sample_PrimaryObject_strategy)
def test_sample_primaryobject_featureMapAttributeType1_setter(instance):
    original = instance.featureMapAttributeType1
    instance.featureMapAttributeType1 = original
    assert instance.featureMapAttributeType1 == original



@given(instance=sample_PrimaryObject_strategy)
def test_sample_primaryobject_unsettableAttribute_setter(instance):
    original = instance.unsettableAttribute
    instance.unsettableAttribute = original
    assert instance.unsettableAttribute == original



@given(instance=sample_PrimaryObject_strategy)
def test_sample_primaryobject_unsettableAttributeWithDefault_setter(instance):
    original = instance.unsettableAttributeWithDefault
    instance.unsettableAttributeWithDefault = original
    assert instance.unsettableAttributeWithDefault == original



@given(instance=sample_PrimaryObject_strategy)
def test_sample_primaryobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sample_PrimaryObject_strategy)
def test_sample_primaryobject_featureMapAttributeCollection_setter(instance):
    original = instance.featureMapAttributeCollection
    instance.featureMapAttributeCollection = original
    assert instance.featureMapAttributeCollection == original

@given(instance=sample_Value_strategy)
@settings(max_examples=50)
def test_sample_value_instantiation(instance):
    assert isinstance(instance, sample_Value)



@given(instance=sample_Value_strategy)
def test_sample_value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
