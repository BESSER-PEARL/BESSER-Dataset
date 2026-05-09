import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    oclstdlib::UniqueCollection,
    oclstdlib::Set,
    oclstdlib::Sequence,
    oclstdlib::OrderedSet,
    oclstdlib::OrderedCollection,
    OclElement,
    oclstdlib::OclType,
    oclstdlib::OclAny,
    OclAny,
    oclstdlib::OclComparable,
    oclstdlib::OclElement,
    oclstdlib::OclVoid,
    oclstdlib::OclSummable,
    oclstdlib::OclState,
    oclstdlib::OclMessage,
    oclstdlib::OclTuple,
    oclstdlib::Collection,
    oclstdlib::Bag,
    oclstdlib::OclLambda,
    OclVoid,
    oclstdlib::OclInvalid,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclstdlib::uniquecollection_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::UniqueCollection)


def test_oclstdlib::uniquecollection_constructor_exists():
    assert callable(oclstdlib::UniqueCollection.__init__)


def test_oclstdlib::uniquecollection_constructor_args():
    sig = inspect.signature(oclstdlib::UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::set_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::Set)


def test_oclstdlib::set_constructor_exists():
    assert callable(oclstdlib::Set.__init__)


def test_oclstdlib::set_constructor_args():
    sig = inspect.signature(oclstdlib::Set.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::sequence_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::Sequence)


def test_oclstdlib::sequence_constructor_exists():
    assert callable(oclstdlib::Sequence.__init__)


def test_oclstdlib::sequence_constructor_args():
    sig = inspect.signature(oclstdlib::Sequence.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::orderedset_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OrderedSet)


def test_oclstdlib::orderedset_constructor_exists():
    assert callable(oclstdlib::OrderedSet.__init__)


def test_oclstdlib::orderedset_constructor_args():
    sig = inspect.signature(oclstdlib::OrderedSet.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::orderedcollection_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OrderedCollection)


def test_oclstdlib::orderedcollection_constructor_exists():
    assert callable(oclstdlib::OrderedCollection.__init__)


def test_oclstdlib::orderedcollection_constructor_args():
    sig = inspect.signature(oclstdlib::OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_oclelement_is_not_abstract():
    assert not inspect.isabstract(OclElement)


def test_oclelement_constructor_exists():
    assert callable(OclElement.__init__)


def test_oclelement_constructor_args():
    sig = inspect.signature(OclElement.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::ocltype_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclType)


def test_oclstdlib::ocltype_constructor_exists():
    assert callable(oclstdlib::OclType.__init__)


def test_oclstdlib::ocltype_constructor_args():
    sig = inspect.signature(oclstdlib::OclType.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::oclany_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclAny)


def test_oclstdlib::oclany_constructor_exists():
    assert callable(oclstdlib::OclAny.__init__)


def test_oclstdlib::oclany_constructor_args():
    sig = inspect.signature(oclstdlib::OclAny.__init__)
    params = list(sig.parameters.keys())



def test_oclany_is_not_abstract():
    assert not inspect.isabstract(OclAny)


def test_oclany_constructor_exists():
    assert callable(OclAny.__init__)


def test_oclany_constructor_args():
    sig = inspect.signature(OclAny.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::oclcomparable_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclComparable)


def test_oclstdlib::oclcomparable_constructor_exists():
    assert callable(oclstdlib::OclComparable.__init__)


def test_oclstdlib::oclcomparable_constructor_args():
    sig = inspect.signature(oclstdlib::OclComparable.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::oclelement_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclElement)


def test_oclstdlib::oclelement_constructor_exists():
    assert callable(oclstdlib::OclElement.__init__)


def test_oclstdlib::oclelement_constructor_args():
    sig = inspect.signature(oclstdlib::OclElement.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::oclvoid_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclVoid)


def test_oclstdlib::oclvoid_constructor_exists():
    assert callable(oclstdlib::OclVoid.__init__)


def test_oclstdlib::oclvoid_constructor_args():
    sig = inspect.signature(oclstdlib::OclVoid.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::oclsummable_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclSummable)


def test_oclstdlib::oclsummable_constructor_exists():
    assert callable(oclstdlib::OclSummable.__init__)


def test_oclstdlib::oclsummable_constructor_args():
    sig = inspect.signature(oclstdlib::OclSummable.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::oclstate_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclState)


def test_oclstdlib::oclstate_constructor_exists():
    assert callable(oclstdlib::OclState.__init__)


def test_oclstdlib::oclstate_constructor_args():
    sig = inspect.signature(oclstdlib::OclState.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::oclmessage_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclMessage)


def test_oclstdlib::oclmessage_constructor_exists():
    assert callable(oclstdlib::OclMessage.__init__)


def test_oclstdlib::oclmessage_constructor_args():
    sig = inspect.signature(oclstdlib::OclMessage.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::ocltuple_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclTuple)


def test_oclstdlib::ocltuple_constructor_exists():
    assert callable(oclstdlib::OclTuple.__init__)


def test_oclstdlib::ocltuple_constructor_args():
    sig = inspect.signature(oclstdlib::OclTuple.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::collection_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::Collection)


def test_oclstdlib::collection_constructor_exists():
    assert callable(oclstdlib::Collection.__init__)


def test_oclstdlib::collection_constructor_args():
    sig = inspect.signature(oclstdlib::Collection.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_oclstdlib::collection_has_upper():
    assert hasattr(oclstdlib::Collection, "upper")
    descriptor = None
    for klass in oclstdlib::Collection.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_oclstdlib::collection_has_lower():
    assert hasattr(oclstdlib::Collection, "lower")
    descriptor = None
    for klass in oclstdlib::Collection.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_oclstdlib::bag_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::Bag)


def test_oclstdlib::bag_constructor_exists():
    assert callable(oclstdlib::Bag.__init__)


def test_oclstdlib::bag_constructor_args():
    sig = inspect.signature(oclstdlib::Bag.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::ocllambda_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclLambda)


def test_oclstdlib::ocllambda_constructor_exists():
    assert callable(oclstdlib::OclLambda.__init__)


def test_oclstdlib::ocllambda_constructor_args():
    sig = inspect.signature(oclstdlib::OclLambda.__init__)
    params = list(sig.parameters.keys())



def test_oclvoid_is_not_abstract():
    assert not inspect.isabstract(OclVoid)


def test_oclvoid_constructor_exists():
    assert callable(OclVoid.__init__)


def test_oclvoid_constructor_args():
    sig = inspect.signature(OclVoid.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlib::oclinvalid_is_not_abstract():
    assert not inspect.isabstract(oclstdlib::OclInvalid)


def test_oclstdlib::oclinvalid_constructor_exists():
    assert callable(oclstdlib::OclInvalid.__init__)


def test_oclstdlib::oclinvalid_constructor_args():
    sig = inspect.signature(oclstdlib::OclInvalid.__init__)
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
oclstdlib::UniqueCollection_strategy = st.builds(
    oclstdlib::UniqueCollection,
)
oclstdlib::Set_strategy = st.builds(
    oclstdlib::Set,
)
oclstdlib::Sequence_strategy = st.builds(
    oclstdlib::Sequence,
)
oclstdlib::OrderedSet_strategy = st.builds(
    oclstdlib::OrderedSet,
)
oclstdlib::OrderedCollection_strategy = st.builds(
    oclstdlib::OrderedCollection,
)
OclElement_strategy = st.builds(
    OclElement,
)
oclstdlib::OclType_strategy = st.builds(
    oclstdlib::OclType,
)
oclstdlib::OclAny_strategy = st.builds(
    oclstdlib::OclAny,
)
OclAny_strategy = st.builds(
    OclAny,
)
oclstdlib::OclComparable_strategy = st.builds(
    oclstdlib::OclComparable,
)
oclstdlib::OclElement_strategy = st.builds(
    oclstdlib::OclElement,
)
oclstdlib::OclVoid_strategy = st.builds(
    oclstdlib::OclVoid,
)
oclstdlib::OclSummable_strategy = st.builds(
    oclstdlib::OclSummable,
)
oclstdlib::OclState_strategy = st.builds(
    oclstdlib::OclState,
)
oclstdlib::OclMessage_strategy = st.builds(
    oclstdlib::OclMessage,
)
oclstdlib::OclTuple_strategy = st.builds(
    oclstdlib::OclTuple,
)
oclstdlib::Collection_strategy = st.builds(
    oclstdlib::Collection,
    upper=
        safe_text,
    lower=
        safe_text
)
oclstdlib::Bag_strategy = st.builds(
    oclstdlib::Bag,
)
oclstdlib::OclLambda_strategy = st.builds(
    oclstdlib::OclLambda,
)
OclVoid_strategy = st.builds(
    OclVoid,
)
oclstdlib::OclInvalid_strategy = st.builds(
    oclstdlib::OclInvalid,
)

@given(instance=oclstdlib::UniqueCollection_strategy)
@settings(max_examples=50)
def test_oclstdlib::uniquecollection_instantiation(instance):
    assert isinstance(instance, oclstdlib::UniqueCollection)

@given(instance=oclstdlib::Set_strategy)
@settings(max_examples=50)
def test_oclstdlib::set_instantiation(instance):
    assert isinstance(instance, oclstdlib::Set)

@given(instance=oclstdlib::Sequence_strategy)
@settings(max_examples=50)
def test_oclstdlib::sequence_instantiation(instance):
    assert isinstance(instance, oclstdlib::Sequence)

@given(instance=oclstdlib::OrderedSet_strategy)
@settings(max_examples=50)
def test_oclstdlib::orderedset_instantiation(instance):
    assert isinstance(instance, oclstdlib::OrderedSet)

@given(instance=oclstdlib::OrderedCollection_strategy)
@settings(max_examples=50)
def test_oclstdlib::orderedcollection_instantiation(instance):
    assert isinstance(instance, oclstdlib::OrderedCollection)

@given(instance=OclElement_strategy)
@settings(max_examples=50)
def test_oclelement_instantiation(instance):
    assert isinstance(instance, OclElement)

@given(instance=oclstdlib::OclType_strategy)
@settings(max_examples=50)
def test_oclstdlib::ocltype_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclType)

@given(instance=oclstdlib::OclAny_strategy)
@settings(max_examples=50)
def test_oclstdlib::oclany_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclAny)

@given(instance=OclAny_strategy)
@settings(max_examples=50)
def test_oclany_instantiation(instance):
    assert isinstance(instance, OclAny)

@given(instance=oclstdlib::OclComparable_strategy)
@settings(max_examples=50)
def test_oclstdlib::oclcomparable_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclComparable)

@given(instance=oclstdlib::OclElement_strategy)
@settings(max_examples=50)
def test_oclstdlib::oclelement_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclElement)

@given(instance=oclstdlib::OclVoid_strategy)
@settings(max_examples=50)
def test_oclstdlib::oclvoid_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclVoid)

@given(instance=oclstdlib::OclSummable_strategy)
@settings(max_examples=50)
def test_oclstdlib::oclsummable_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclSummable)

@given(instance=oclstdlib::OclState_strategy)
@settings(max_examples=50)
def test_oclstdlib::oclstate_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclState)

@given(instance=oclstdlib::OclMessage_strategy)
@settings(max_examples=50)
def test_oclstdlib::oclmessage_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclMessage)

@given(instance=oclstdlib::OclTuple_strategy)
@settings(max_examples=50)
def test_oclstdlib::ocltuple_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclTuple)

@given(instance=oclstdlib::Collection_strategy)
@settings(max_examples=50)
def test_oclstdlib::collection_instantiation(instance):
    assert isinstance(instance, oclstdlib::Collection)

@given(instance=oclstdlib::Collection_strategy)
def test_oclstdlib::collection_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=oclstdlib::Collection_strategy)
def test_oclstdlib::collection_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=oclstdlib::Collection_strategy)
def test_oclstdlib::collection_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=oclstdlib::Collection_strategy)
def test_oclstdlib::collection_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=oclstdlib::Bag_strategy)
@settings(max_examples=50)
def test_oclstdlib::bag_instantiation(instance):
    assert isinstance(instance, oclstdlib::Bag)

@given(instance=oclstdlib::OclLambda_strategy)
@settings(max_examples=50)
def test_oclstdlib::ocllambda_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclLambda)

@given(instance=OclVoid_strategy)
@settings(max_examples=50)
def test_oclvoid_instantiation(instance):
    assert isinstance(instance, OclVoid)

@given(instance=oclstdlib::OclInvalid_strategy)
@settings(max_examples=50)
def test_oclstdlib::oclinvalid_instantiation(instance):
    assert isinstance(instance, oclstdlib::OclInvalid)
