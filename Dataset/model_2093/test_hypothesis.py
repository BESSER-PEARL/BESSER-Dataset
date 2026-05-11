import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DecisionTree::Property,
    DecisionTree::DecisionTrees,
    DecisionTree::EntityType,
    DecisionTree::DecisionTreeForEntity,
    DecisionTree::PropertySpec2,
    DecisionTree::StructuralVariation,
    DecisionTreeNode,
    DecisionTree::IntermediateNode,
    DecisionTree::LeafNode,
    DecisionTree::DecisionTreeNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_decisiontree::property_is_not_abstract():
    assert not inspect.isabstract(DecisionTree::Property)


def test_decisiontree::property_constructor_exists():
    assert callable(DecisionTree::Property.__init__)


def test_decisiontree::property_constructor_args():
    sig = inspect.signature(DecisionTree::Property.__init__)
    params = list(sig.parameters.keys())



def test_decisiontree::decisiontrees_is_not_abstract():
    assert not inspect.isabstract(DecisionTree::DecisionTrees)


def test_decisiontree::decisiontrees_constructor_exists():
    assert callable(DecisionTree::DecisionTrees.__init__)


def test_decisiontree::decisiontrees_constructor_args():
    sig = inspect.signature(DecisionTree::DecisionTrees.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_decisiontree::decisiontrees_has_name():
    assert hasattr(DecisionTree::DecisionTrees, "name")
    descriptor = None
    for klass in DecisionTree::DecisionTrees.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_decisiontree::entitytype_is_not_abstract():
    assert not inspect.isabstract(DecisionTree::EntityType)


def test_decisiontree::entitytype_constructor_exists():
    assert callable(DecisionTree::EntityType.__init__)


def test_decisiontree::entitytype_constructor_args():
    sig = inspect.signature(DecisionTree::EntityType.__init__)
    params = list(sig.parameters.keys())



def test_decisiontree::decisiontreeforentity_is_not_abstract():
    assert not inspect.isabstract(DecisionTree::DecisionTreeForEntity)


def test_decisiontree::decisiontreeforentity_constructor_exists():
    assert callable(DecisionTree::DecisionTreeForEntity.__init__)


def test_decisiontree::decisiontreeforentity_constructor_args():
    sig = inspect.signature(DecisionTree::DecisionTreeForEntity.__init__)
    params = list(sig.parameters.keys())



def test_decisiontree::propertyspec2_is_not_abstract():
    assert not inspect.isabstract(DecisionTree::PropertySpec2)


def test_decisiontree::propertyspec2_constructor_exists():
    assert callable(DecisionTree::PropertySpec2.__init__)


def test_decisiontree::propertyspec2_constructor_args():
    sig = inspect.signature(DecisionTree::PropertySpec2.__init__)
    params = list(sig.parameters.keys())
    assert "needsTypeCheck" in params, "Missing parameter 'needsTypeCheck'"

def test_decisiontree::propertyspec2_has_needsTypeCheck():
    assert hasattr(DecisionTree::PropertySpec2, "needsTypeCheck")
    descriptor = None
    for klass in DecisionTree::PropertySpec2.__mro__:
        if "needsTypeCheck" in klass.__dict__:
            descriptor = klass.__dict__["needsTypeCheck"]
            break
    assert isinstance(descriptor, property)



def test_decisiontree::structuralvariation_is_not_abstract():
    assert not inspect.isabstract(DecisionTree::StructuralVariation)


def test_decisiontree::structuralvariation_constructor_exists():
    assert callable(DecisionTree::StructuralVariation.__init__)


def test_decisiontree::structuralvariation_constructor_args():
    sig = inspect.signature(DecisionTree::StructuralVariation.__init__)
    params = list(sig.parameters.keys())



def test_decisiontreenode_is_not_abstract():
    assert not inspect.isabstract(DecisionTreeNode)


def test_decisiontreenode_constructor_exists():
    assert callable(DecisionTreeNode.__init__)


def test_decisiontreenode_constructor_args():
    sig = inspect.signature(DecisionTreeNode.__init__)
    params = list(sig.parameters.keys())



def test_decisiontree::intermediatenode_is_not_abstract():
    assert not inspect.isabstract(DecisionTree::IntermediateNode)


def test_decisiontree::intermediatenode_constructor_exists():
    assert callable(DecisionTree::IntermediateNode.__init__)


def test_decisiontree::intermediatenode_constructor_args():
    sig = inspect.signature(DecisionTree::IntermediateNode.__init__)
    params = list(sig.parameters.keys())



def test_decisiontree::leafnode_is_not_abstract():
    assert not inspect.isabstract(DecisionTree::LeafNode)


def test_decisiontree::leafnode_constructor_exists():
    assert callable(DecisionTree::LeafNode.__init__)


def test_decisiontree::leafnode_constructor_args():
    sig = inspect.signature(DecisionTree::LeafNode.__init__)
    params = list(sig.parameters.keys())



def test_decisiontree::decisiontreenode_is_not_abstract():
    assert not inspect.isabstract(DecisionTree::DecisionTreeNode)


def test_decisiontree::decisiontreenode_constructor_exists():
    assert callable(DecisionTree::DecisionTreeNode.__init__)


def test_decisiontree::decisiontreenode_constructor_args():
    sig = inspect.signature(DecisionTree::DecisionTreeNode.__init__)
    params = list(sig.parameters.keys())


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
DecisionTree::Property_strategy = st.builds(
    DecisionTree::Property,
)
DecisionTree::DecisionTrees_strategy = st.builds(
    DecisionTree::DecisionTrees,
    name=
        safe_text
)
DecisionTree::EntityType_strategy = st.builds(
    DecisionTree::EntityType,
)
DecisionTree::DecisionTreeForEntity_strategy = st.builds(
    DecisionTree::DecisionTreeForEntity,
)
DecisionTree::PropertySpec2_strategy = st.builds(
    DecisionTree::PropertySpec2,
    needsTypeCheck=
        st.booleans()
)
DecisionTree::StructuralVariation_strategy = st.builds(
    DecisionTree::StructuralVariation,
)
DecisionTreeNode_strategy = st.builds(
    DecisionTreeNode,
)
DecisionTree::IntermediateNode_strategy = st.builds(
    DecisionTree::IntermediateNode,
)
DecisionTree::LeafNode_strategy = st.builds(
    DecisionTree::LeafNode,
)
DecisionTree::DecisionTreeNode_strategy = st.builds(
    DecisionTree::DecisionTreeNode,
)

@given(instance=DecisionTree::Property_strategy)
@settings(max_examples=50)
def test_decisiontree::property_instantiation(instance):
    assert isinstance(instance, DecisionTree::Property)

@given(instance=DecisionTree::DecisionTrees_strategy)
@settings(max_examples=50)
def test_decisiontree::decisiontrees_instantiation(instance):
    assert isinstance(instance, DecisionTree::DecisionTrees)

@given(instance=DecisionTree::DecisionTrees_strategy)
def test_decisiontree::decisiontrees_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DecisionTree::DecisionTrees_strategy)
def test_decisiontree::decisiontrees_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DecisionTree::EntityType_strategy)
@settings(max_examples=50)
def test_decisiontree::entitytype_instantiation(instance):
    assert isinstance(instance, DecisionTree::EntityType)

@given(instance=DecisionTree::DecisionTreeForEntity_strategy)
@settings(max_examples=50)
def test_decisiontree::decisiontreeforentity_instantiation(instance):
    assert isinstance(instance, DecisionTree::DecisionTreeForEntity)

@given(instance=DecisionTree::PropertySpec2_strategy)
@settings(max_examples=50)
def test_decisiontree::propertyspec2_instantiation(instance):
    assert isinstance(instance, DecisionTree::PropertySpec2)

@given(instance=DecisionTree::PropertySpec2_strategy)
def test_decisiontree::propertyspec2_needsTypeCheck_type(instance):
    assert isinstance(instance.needsTypeCheck, bool)


@given(instance=DecisionTree::PropertySpec2_strategy)
def test_decisiontree::propertyspec2_needsTypeCheck_setter(instance):
    original = instance.needsTypeCheck
    instance.needsTypeCheck = original
    assert instance.needsTypeCheck == original

@given(instance=DecisionTree::StructuralVariation_strategy)
@settings(max_examples=50)
def test_decisiontree::structuralvariation_instantiation(instance):
    assert isinstance(instance, DecisionTree::StructuralVariation)

@given(instance=DecisionTreeNode_strategy)
@settings(max_examples=50)
def test_decisiontreenode_instantiation(instance):
    assert isinstance(instance, DecisionTreeNode)

@given(instance=DecisionTree::IntermediateNode_strategy)
@settings(max_examples=50)
def test_decisiontree::intermediatenode_instantiation(instance):
    assert isinstance(instance, DecisionTree::IntermediateNode)

@given(instance=DecisionTree::LeafNode_strategy)
@settings(max_examples=50)
def test_decisiontree::leafnode_instantiation(instance):
    assert isinstance(instance, DecisionTree::LeafNode)

@given(instance=DecisionTree::DecisionTreeNode_strategy)
@settings(max_examples=50)
def test_decisiontree::decisiontreenode_instantiation(instance):
    assert isinstance(instance, DecisionTree::DecisionTreeNode)
