import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sample::Comment,
    sample::Node,
    PhysicalNode,
    sample::LocalNode,
    sample::RemoteNode,
    Node,
    sample::VirtualNode,
    sample::PhysicalNode,
    sample::Tree,
    sample::Type,
    sample::DataTypeMap,
    sample::StringMap,
    sample::TypeMapReference,
    sample::TypeMap,
    sample::ETypes,
    sample::TargetObject,
    sample::PrimaryObject,
    sample::Value,
    SomeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample::comment_is_not_abstract():
    assert not inspect.isabstract(sample::Comment)


def test_sample::comment_constructor_exists():
    assert callable(sample::Comment.__init__)


def test_sample::comment_constructor_args():
    sig = inspect.signature(sample::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_sample::comment_has_content():
    assert hasattr(sample::Comment, "content")
    descriptor = None
    for klass in sample::Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_sample::node_is_not_abstract():
    assert not inspect.isabstract(sample::Node)


def test_sample::node_constructor_exists():
    assert callable(sample::Node.__init__)


def test_sample::node_constructor_args():
    sig = inspect.signature(sample::Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_sample::node_has_label():
    assert hasattr(sample::Node, "label")
    descriptor = None
    for klass in sample::Node.__mro__:
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



def test_sample::localnode_is_not_abstract():
    assert not inspect.isabstract(sample::LocalNode)


def test_sample::localnode_constructor_exists():
    assert callable(sample::LocalNode.__init__)


def test_sample::localnode_constructor_args():
    sig = inspect.signature(sample::LocalNode.__init__)
    params = list(sig.parameters.keys())



def test_sample::remotenode_is_not_abstract():
    assert not inspect.isabstract(sample::RemoteNode)


def test_sample::remotenode_constructor_exists():
    assert callable(sample::RemoteNode.__init__)


def test_sample::remotenode_constructor_args():
    sig = inspect.signature(sample::RemoteNode.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_sample::virtualnode_is_not_abstract():
    assert not inspect.isabstract(sample::VirtualNode)


def test_sample::virtualnode_constructor_exists():
    assert callable(sample::VirtualNode.__init__)


def test_sample::virtualnode_constructor_args():
    sig = inspect.signature(sample::VirtualNode.__init__)
    params = list(sig.parameters.keys())



def test_sample::physicalnode_is_not_abstract():
    assert not inspect.isabstract(sample::PhysicalNode)


def test_sample::physicalnode_constructor_exists():
    assert callable(sample::PhysicalNode.__init__)


def test_sample::physicalnode_constructor_args():
    sig = inspect.signature(sample::PhysicalNode.__init__)
    params = list(sig.parameters.keys())



def test_sample::tree_is_not_abstract():
    assert not inspect.isabstract(sample::Tree)


def test_sample::tree_constructor_exists():
    assert callable(sample::Tree.__init__)


def test_sample::tree_constructor_args():
    sig = inspect.signature(sample::Tree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample::tree_has_name():
    assert hasattr(sample::Tree, "name")
    descriptor = None
    for klass in sample::Tree.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample::type_is_not_abstract():
    assert not inspect.isabstract(sample::Type)


def test_sample::type_constructor_exists():
    assert callable(sample::Type.__init__)


def test_sample::type_constructor_args():
    sig = inspect.signature(sample::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample::type_has_name():
    assert hasattr(sample::Type, "name")
    descriptor = None
    for klass in sample::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample::datatypemap_is_not_abstract():
    assert not inspect.isabstract(sample::DataTypeMap)


def test_sample::datatypemap_constructor_exists():
    assert callable(sample::DataTypeMap.__init__)


def test_sample::datatypemap_constructor_args():
    sig = inspect.signature(sample::DataTypeMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_sample::datatypemap_has_value():
    assert hasattr(sample::DataTypeMap, "value")
    descriptor = None
    for klass in sample::DataTypeMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sample::datatypemap_has_key():
    assert hasattr(sample::DataTypeMap, "key")
    descriptor = None
    for klass in sample::DataTypeMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_sample::stringmap_is_not_abstract():
    assert not inspect.isabstract(sample::StringMap)


def test_sample::stringmap_constructor_exists():
    assert callable(sample::StringMap.__init__)


def test_sample::stringmap_constructor_args():
    sig = inspect.signature(sample::StringMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_sample::stringmap_has_key():
    assert hasattr(sample::StringMap, "key")
    descriptor = None
    for klass in sample::StringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_sample::stringmap_has_value():
    assert hasattr(sample::StringMap, "value")
    descriptor = None
    for klass in sample::StringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sample::typemapreference_is_not_abstract():
    assert not inspect.isabstract(sample::TypeMapReference)


def test_sample::typemapreference_constructor_exists():
    assert callable(sample::TypeMapReference.__init__)


def test_sample::typemapreference_constructor_args():
    sig = inspect.signature(sample::TypeMapReference.__init__)
    params = list(sig.parameters.keys())



def test_sample::typemap_is_not_abstract():
    assert not inspect.isabstract(sample::TypeMap)


def test_sample::typemap_constructor_exists():
    assert callable(sample::TypeMap.__init__)


def test_sample::typemap_constructor_args():
    sig = inspect.signature(sample::TypeMap.__init__)
    params = list(sig.parameters.keys())



def test_sample::etypes_is_not_abstract():
    assert not inspect.isabstract(sample::ETypes)


def test_sample::etypes_constructor_exists():
    assert callable(sample::ETypes.__init__)


def test_sample::etypes_constructor_args():
    sig = inspect.signature(sample::ETypes.__init__)
    params = list(sig.parameters.keys())
    assert "uris" in params, "Missing parameter 'uris'"

def test_sample::etypes_has_uris():
    assert hasattr(sample::ETypes, "uris")
    descriptor = None
    for klass in sample::ETypes.__mro__:
        if "uris" in klass.__dict__:
            descriptor = klass.__dict__["uris"]
            break
    assert isinstance(descriptor, property)



def test_sample::targetobject_is_not_abstract():
    assert not inspect.isabstract(sample::TargetObject)


def test_sample::targetobject_constructor_exists():
    assert callable(sample::TargetObject.__init__)


def test_sample::targetobject_constructor_args():
    sig = inspect.signature(sample::TargetObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "singleAttribute" in params, "Missing parameter 'singleAttribute'"
    assert "manyAttributes" in params, "Missing parameter 'manyAttributes'"

def test_sample::targetobject_has_name():
    assert hasattr(sample::TargetObject, "name")
    descriptor = None
    for klass in sample::TargetObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sample::targetobject_has_singleAttribute():
    assert hasattr(sample::TargetObject, "singleAttribute")
    descriptor = None
    for klass in sample::TargetObject.__mro__:
        if "singleAttribute" in klass.__dict__:
            descriptor = klass.__dict__["singleAttribute"]
            break
    assert isinstance(descriptor, property)

def test_sample::targetobject_has_manyAttributes():
    assert hasattr(sample::TargetObject, "manyAttributes")
    descriptor = None
    for klass in sample::TargetObject.__mro__:
        if "manyAttributes" in klass.__dict__:
            descriptor = klass.__dict__["manyAttributes"]
            break
    assert isinstance(descriptor, property)



def test_sample::primaryobject_is_not_abstract():
    assert not inspect.isabstract(sample::PrimaryObject)


def test_sample::primaryobject_constructor_exists():
    assert callable(sample::PrimaryObject.__init__)


def test_sample::primaryobject_constructor_args():
    sig = inspect.signature(sample::PrimaryObject.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "unsettableAttribute" in params, "Missing parameter 'unsettableAttribute'"
    assert "featureMapReferenceCollection" in params, "Missing parameter 'featureMapReferenceCollection'"
    assert "featureMapAttributeCollection" in params, "Missing parameter 'featureMapAttributeCollection'"
    assert "featureMapAttributeType1" in params, "Missing parameter 'featureMapAttributeType1'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "unsettableAttributeWithDefault" in params, "Missing parameter 'unsettableAttributeWithDefault'"
    assert "featureMapAttributeType2" in params, "Missing parameter 'featureMapAttributeType2'"

def test_sample::primaryobject_has_kind():
    assert hasattr(sample::PrimaryObject, "kind")
    descriptor = None
    for klass in sample::PrimaryObject.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_sample::primaryobject_has_unsettableAttribute():
    assert hasattr(sample::PrimaryObject, "unsettableAttribute")
    descriptor = None
    for klass in sample::PrimaryObject.__mro__:
        if "unsettableAttribute" in klass.__dict__:
            descriptor = klass.__dict__["unsettableAttribute"]
            break
    assert isinstance(descriptor, property)

def test_sample::primaryobject_has_featureMapReferenceCollection():
    assert hasattr(sample::PrimaryObject, "featureMapReferenceCollection")
    descriptor = None
    for klass in sample::PrimaryObject.__mro__:
        if "featureMapReferenceCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapReferenceCollection"]
            break
    assert isinstance(descriptor, property)

def test_sample::primaryobject_has_featureMapAttributeCollection():
    assert hasattr(sample::PrimaryObject, "featureMapAttributeCollection")
    descriptor = None
    for klass in sample::PrimaryObject.__mro__:
        if "featureMapAttributeCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeCollection"]
            break
    assert isinstance(descriptor, property)

def test_sample::primaryobject_has_featureMapAttributeType1():
    assert hasattr(sample::PrimaryObject, "featureMapAttributeType1")
    descriptor = None
    for klass in sample::PrimaryObject.__mro__:
        if "featureMapAttributeType1" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeType1"]
            break
    assert isinstance(descriptor, property)

def test_sample::primaryobject_has_id():
    assert hasattr(sample::PrimaryObject, "id")
    descriptor = None
    for klass in sample::PrimaryObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sample::primaryobject_has_name():
    assert hasattr(sample::PrimaryObject, "name")
    descriptor = None
    for klass in sample::PrimaryObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sample::primaryobject_has_unsettableAttributeWithDefault():
    assert hasattr(sample::PrimaryObject, "unsettableAttributeWithDefault")
    descriptor = None
    for klass in sample::PrimaryObject.__mro__:
        if "unsettableAttributeWithDefault" in klass.__dict__:
            descriptor = klass.__dict__["unsettableAttributeWithDefault"]
            break
    assert isinstance(descriptor, property)

def test_sample::primaryobject_has_featureMapAttributeType2():
    assert hasattr(sample::PrimaryObject, "featureMapAttributeType2")
    descriptor = None
    for klass in sample::PrimaryObject.__mro__:
        if "featureMapAttributeType2" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeType2"]
            break
    assert isinstance(descriptor, property)



def test_sample::value_is_not_abstract():
    assert not inspect.isabstract(sample::Value)


def test_sample::value_constructor_exists():
    assert callable(sample::Value.__init__)


def test_sample::value_constructor_args():
    sig = inspect.signature(sample::Value.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sample::value_has_value():
    assert hasattr(sample::Value, "value")
    descriptor = None
    for klass in sample::Value.__mro__:
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
        "Three",
        "Two",
        "one",
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
sample::Comment_strategy = st.builds(
    sample::Comment,
    content=
        safe_text
)
sample::Node_strategy = st.builds(
    sample::Node,
    label=
        safe_text
)
PhysicalNode_strategy = st.builds(
    PhysicalNode,
)
sample::LocalNode_strategy = st.builds(
    sample::LocalNode,
)
sample::RemoteNode_strategy = st.builds(
    sample::RemoteNode,
)
Node_strategy = st.builds(
    Node,
)
sample::VirtualNode_strategy = st.builds(
    sample::VirtualNode,
)
sample::PhysicalNode_strategy = st.builds(
    sample::PhysicalNode,
)
sample::Tree_strategy = st.builds(
    sample::Tree,
    name=
        safe_text
)
sample::Type_strategy = st.builds(
    sample::Type,
    name=
        safe_text
)
sample::DataTypeMap_strategy = st.builds(
    sample::DataTypeMap,
    value=
        safe_text,
    key=
        safe_text
)
sample::StringMap_strategy = st.builds(
    sample::StringMap,
    key=
        safe_text,
    value=
        safe_text
)
sample::TypeMapReference_strategy = st.builds(
    sample::TypeMapReference,
)
sample::TypeMap_strategy = st.builds(
    sample::TypeMap,
)
sample::ETypes_strategy = st.builds(
    sample::ETypes,
    uris=
        safe_text
)
sample::TargetObject_strategy = st.builds(
    sample::TargetObject,
    name=
        safe_text,
    singleAttribute=
        safe_text,
    manyAttributes=
        safe_text
)
sample::PrimaryObject_strategy = st.builds(
    sample::PrimaryObject,
    kind=
        safe_text,
    unsettableAttribute=
        safe_text,
    featureMapReferenceCollection=
        safe_text,
    featureMapAttributeCollection=
        safe_text,
    featureMapAttributeType1=
        safe_text,
    id=
        safe_text,
    name=
        safe_text,
    unsettableAttributeWithDefault=
        safe_text,
    featureMapAttributeType2=
        safe_text
)
sample::Value_strategy = st.builds(
    sample::Value,
    value=
        st.integers()
)

@given(instance=sample::Comment_strategy)
@settings(max_examples=50)
def test_sample::comment_instantiation(instance):
    assert isinstance(instance, sample::Comment)

@given(instance=sample::Comment_strategy)
def test_sample::comment_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=sample::Comment_strategy)
def test_sample::comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=sample::Node_strategy)
@settings(max_examples=50)
def test_sample::node_instantiation(instance):
    assert isinstance(instance, sample::Node)

@given(instance=sample::Node_strategy)
def test_sample::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=sample::Node_strategy)
def test_sample::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=PhysicalNode_strategy)
@settings(max_examples=50)
def test_physicalnode_instantiation(instance):
    assert isinstance(instance, PhysicalNode)

@given(instance=sample::LocalNode_strategy)
@settings(max_examples=50)
def test_sample::localnode_instantiation(instance):
    assert isinstance(instance, sample::LocalNode)

@given(instance=sample::RemoteNode_strategy)
@settings(max_examples=50)
def test_sample::remotenode_instantiation(instance):
    assert isinstance(instance, sample::RemoteNode)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=sample::VirtualNode_strategy)
@settings(max_examples=50)
def test_sample::virtualnode_instantiation(instance):
    assert isinstance(instance, sample::VirtualNode)

@given(instance=sample::PhysicalNode_strategy)
@settings(max_examples=50)
def test_sample::physicalnode_instantiation(instance):
    assert isinstance(instance, sample::PhysicalNode)

@given(instance=sample::Tree_strategy)
@settings(max_examples=50)
def test_sample::tree_instantiation(instance):
    assert isinstance(instance, sample::Tree)

@given(instance=sample::Tree_strategy)
def test_sample::tree_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::Tree_strategy)
def test_sample::tree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample::Type_strategy)
@settings(max_examples=50)
def test_sample::type_instantiation(instance):
    assert isinstance(instance, sample::Type)

@given(instance=sample::Type_strategy)
def test_sample::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::Type_strategy)
def test_sample::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample::DataTypeMap_strategy)
@settings(max_examples=50)
def test_sample::datatypemap_instantiation(instance):
    assert isinstance(instance, sample::DataTypeMap)

@given(instance=sample::DataTypeMap_strategy)
def test_sample::datatypemap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sample::DataTypeMap_strategy)
def test_sample::datatypemap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sample::DataTypeMap_strategy)
def test_sample::datatypemap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=sample::DataTypeMap_strategy)
def test_sample::datatypemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=sample::StringMap_strategy)
@settings(max_examples=50)
def test_sample::stringmap_instantiation(instance):
    assert isinstance(instance, sample::StringMap)

@given(instance=sample::StringMap_strategy)
def test_sample::stringmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=sample::StringMap_strategy)
def test_sample::stringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=sample::StringMap_strategy)
def test_sample::stringmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sample::StringMap_strategy)
def test_sample::stringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sample::TypeMapReference_strategy)
@settings(max_examples=50)
def test_sample::typemapreference_instantiation(instance):
    assert isinstance(instance, sample::TypeMapReference)

@given(instance=sample::TypeMap_strategy)
@settings(max_examples=50)
def test_sample::typemap_instantiation(instance):
    assert isinstance(instance, sample::TypeMap)

@given(instance=sample::ETypes_strategy)
@settings(max_examples=50)
def test_sample::etypes_instantiation(instance):
    assert isinstance(instance, sample::ETypes)

@given(instance=sample::ETypes_strategy)
def test_sample::etypes_uris_type(instance):
    assert isinstance(instance.uris, str)


@given(instance=sample::ETypes_strategy)
def test_sample::etypes_uris_setter(instance):
    original = instance.uris
    instance.uris = original
    assert instance.uris == original

@given(instance=sample::TargetObject_strategy)
@settings(max_examples=50)
def test_sample::targetobject_instantiation(instance):
    assert isinstance(instance, sample::TargetObject)

@given(instance=sample::TargetObject_strategy)
def test_sample::targetobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::TargetObject_strategy)
def test_sample::targetobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample::TargetObject_strategy)
def test_sample::targetobject_singleAttribute_type(instance):
    assert isinstance(instance.singleAttribute, str)


@given(instance=sample::TargetObject_strategy)
def test_sample::targetobject_singleAttribute_setter(instance):
    original = instance.singleAttribute
    instance.singleAttribute = original
    assert instance.singleAttribute == original

@given(instance=sample::TargetObject_strategy)
def test_sample::targetobject_manyAttributes_type(instance):
    assert isinstance(instance.manyAttributes, str)


@given(instance=sample::TargetObject_strategy)
def test_sample::targetobject_manyAttributes_setter(instance):
    original = instance.manyAttributes
    instance.manyAttributes = original
    assert instance.manyAttributes == original

@given(instance=sample::PrimaryObject_strategy)
@settings(max_examples=50)
def test_sample::primaryobject_instantiation(instance):
    assert isinstance(instance, sample::PrimaryObject)

@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_unsettableAttribute_type(instance):
    assert isinstance(instance.unsettableAttribute, str)


@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_unsettableAttribute_setter(instance):
    original = instance.unsettableAttribute
    instance.unsettableAttribute = original
    assert instance.unsettableAttribute == original

@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_featureMapReferenceCollection_type(instance):
    assert isinstance(instance.featureMapReferenceCollection, str)


@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_featureMapReferenceCollection_setter(instance):
    original = instance.featureMapReferenceCollection
    instance.featureMapReferenceCollection = original
    assert instance.featureMapReferenceCollection == original

@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_featureMapAttributeCollection_type(instance):
    assert isinstance(instance.featureMapAttributeCollection, str)


@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_featureMapAttributeCollection_setter(instance):
    original = instance.featureMapAttributeCollection
    instance.featureMapAttributeCollection = original
    assert instance.featureMapAttributeCollection == original

@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_featureMapAttributeType1_type(instance):
    assert isinstance(instance.featureMapAttributeType1, str)


@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_featureMapAttributeType1_setter(instance):
    original = instance.featureMapAttributeType1
    instance.featureMapAttributeType1 = original
    assert instance.featureMapAttributeType1 == original

@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_unsettableAttributeWithDefault_type(instance):
    assert isinstance(instance.unsettableAttributeWithDefault, str)


@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_unsettableAttributeWithDefault_setter(instance):
    original = instance.unsettableAttributeWithDefault
    instance.unsettableAttributeWithDefault = original
    assert instance.unsettableAttributeWithDefault == original

@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_featureMapAttributeType2_type(instance):
    assert isinstance(instance.featureMapAttributeType2, str)


@given(instance=sample::PrimaryObject_strategy)
def test_sample::primaryobject_featureMapAttributeType2_setter(instance):
    original = instance.featureMapAttributeType2
    instance.featureMapAttributeType2 = original
    assert instance.featureMapAttributeType2 == original

@given(instance=sample::Value_strategy)
@settings(max_examples=50)
def test_sample::value_instantiation(instance):
    assert isinstance(instance, sample::Value)

@given(instance=sample::Value_strategy)
def test_sample::value_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=sample::Value_strategy)
def test_sample::value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
