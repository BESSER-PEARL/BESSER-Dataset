import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    grammar::features::SecondRoot,
    Child,
    grammar::features::StarNonContainment,
    grammar::features::ClassWithAttributes,
    grammar::features::CompoundPlus,
    grammar::features::StarPrefix,
    grammar::features::OptionalPrefix,
    grammar::features::PlusPrefix,
    grammar::features::CompoundStar,
    grammar::features::CompoundOptional,
    grammar::features::AlternativeSyntax,
    grammar::features::Child,
    grammar::features::Root,
    grammar::features::PlusNonContainment,
    grammar::features::MandatoryNonContainment,
    grammar::features::OptionalNonContainment,
    grammar::features::StarContainment,
    grammar::features::PlusContainment,
    grammar::features::MandatoryContainment,
    grammar::features::X,
    grammar::features::OptionalContainment,
    AbstractSuperclass,
    grammar::features::ConcreteSubclassB,
    grammar::features::ConcreteSubclassA,
    grammar::features::AbstractSuperclass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_grammar::features::secondroot_is_not_abstract():
    assert not inspect.isabstract(grammar::features::SecondRoot)


def test_grammar::features::secondroot_constructor_exists():
    assert callable(grammar::features::SecondRoot.__init__)


def test_grammar::features::secondroot_constructor_args():
    sig = inspect.signature(grammar::features::SecondRoot.__init__)
    params = list(sig.parameters.keys())



def test_child_is_not_abstract():
    assert not inspect.isabstract(Child)


def test_child_constructor_exists():
    assert callable(Child.__init__)


def test_child_constructor_args():
    sig = inspect.signature(Child.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::starnoncontainment_is_not_abstract():
    assert not inspect.isabstract(grammar::features::StarNonContainment)


def test_grammar::features::starnoncontainment_constructor_exists():
    assert callable(grammar::features::StarNonContainment.__init__)


def test_grammar::features::starnoncontainment_constructor_args():
    sig = inspect.signature(grammar::features::StarNonContainment.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::classwithattributes_is_not_abstract():
    assert not inspect.isabstract(grammar::features::ClassWithAttributes)


def test_grammar::features::classwithattributes_constructor_exists():
    assert callable(grammar::features::ClassWithAttributes.__init__)


def test_grammar::features::classwithattributes_constructor_args():
    sig = inspect.signature(grammar::features::ClassWithAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "a1" in params, "Missing parameter 'a1'"
    assert "a2" in params, "Missing parameter 'a2'"

def test_grammar::features::classwithattributes_has_a1():
    assert hasattr(grammar::features::ClassWithAttributes, "a1")
    descriptor = None
    for klass in grammar::features::ClassWithAttributes.__mro__:
        if "a1" in klass.__dict__:
            descriptor = klass.__dict__["a1"]
            break
    assert isinstance(descriptor, property)

def test_grammar::features::classwithattributes_has_a2():
    assert hasattr(grammar::features::ClassWithAttributes, "a2")
    descriptor = None
    for klass in grammar::features::ClassWithAttributes.__mro__:
        if "a2" in klass.__dict__:
            descriptor = klass.__dict__["a2"]
            break
    assert isinstance(descriptor, property)



def test_grammar::features::compoundplus_is_not_abstract():
    assert not inspect.isabstract(grammar::features::CompoundPlus)


def test_grammar::features::compoundplus_constructor_exists():
    assert callable(grammar::features::CompoundPlus.__init__)


def test_grammar::features::compoundplus_constructor_args():
    sig = inspect.signature(grammar::features::CompoundPlus.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::starprefix_is_not_abstract():
    assert not inspect.isabstract(grammar::features::StarPrefix)


def test_grammar::features::starprefix_constructor_exists():
    assert callable(grammar::features::StarPrefix.__init__)


def test_grammar::features::starprefix_constructor_args():
    sig = inspect.signature(grammar::features::StarPrefix.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::optionalprefix_is_not_abstract():
    assert not inspect.isabstract(grammar::features::OptionalPrefix)


def test_grammar::features::optionalprefix_constructor_exists():
    assert callable(grammar::features::OptionalPrefix.__init__)


def test_grammar::features::optionalprefix_constructor_args():
    sig = inspect.signature(grammar::features::OptionalPrefix.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::plusprefix_is_not_abstract():
    assert not inspect.isabstract(grammar::features::PlusPrefix)


def test_grammar::features::plusprefix_constructor_exists():
    assert callable(grammar::features::PlusPrefix.__init__)


def test_grammar::features::plusprefix_constructor_args():
    sig = inspect.signature(grammar::features::PlusPrefix.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::compoundstar_is_not_abstract():
    assert not inspect.isabstract(grammar::features::CompoundStar)


def test_grammar::features::compoundstar_constructor_exists():
    assert callable(grammar::features::CompoundStar.__init__)


def test_grammar::features::compoundstar_constructor_args():
    sig = inspect.signature(grammar::features::CompoundStar.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::compoundoptional_is_not_abstract():
    assert not inspect.isabstract(grammar::features::CompoundOptional)


def test_grammar::features::compoundoptional_constructor_exists():
    assert callable(grammar::features::CompoundOptional.__init__)


def test_grammar::features::compoundoptional_constructor_args():
    sig = inspect.signature(grammar::features::CompoundOptional.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::alternativesyntax_is_not_abstract():
    assert not inspect.isabstract(grammar::features::AlternativeSyntax)


def test_grammar::features::alternativesyntax_constructor_exists():
    assert callable(grammar::features::AlternativeSyntax.__init__)


def test_grammar::features::alternativesyntax_constructor_args():
    sig = inspect.signature(grammar::features::AlternativeSyntax.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::child_is_not_abstract():
    assert not inspect.isabstract(grammar::features::Child)


def test_grammar::features::child_constructor_exists():
    assert callable(grammar::features::Child.__init__)


def test_grammar::features::child_constructor_args():
    sig = inspect.signature(grammar::features::Child.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::root_is_not_abstract():
    assert not inspect.isabstract(grammar::features::Root)


def test_grammar::features::root_constructor_exists():
    assert callable(grammar::features::Root.__init__)


def test_grammar::features::root_constructor_args():
    sig = inspect.signature(grammar::features::Root.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::plusnoncontainment_is_not_abstract():
    assert not inspect.isabstract(grammar::features::PlusNonContainment)


def test_grammar::features::plusnoncontainment_constructor_exists():
    assert callable(grammar::features::PlusNonContainment.__init__)


def test_grammar::features::plusnoncontainment_constructor_args():
    sig = inspect.signature(grammar::features::PlusNonContainment.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::mandatorynoncontainment_is_not_abstract():
    assert not inspect.isabstract(grammar::features::MandatoryNonContainment)


def test_grammar::features::mandatorynoncontainment_constructor_exists():
    assert callable(grammar::features::MandatoryNonContainment.__init__)


def test_grammar::features::mandatorynoncontainment_constructor_args():
    sig = inspect.signature(grammar::features::MandatoryNonContainment.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::optionalnoncontainment_is_not_abstract():
    assert not inspect.isabstract(grammar::features::OptionalNonContainment)


def test_grammar::features::optionalnoncontainment_constructor_exists():
    assert callable(grammar::features::OptionalNonContainment.__init__)


def test_grammar::features::optionalnoncontainment_constructor_args():
    sig = inspect.signature(grammar::features::OptionalNonContainment.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::starcontainment_is_not_abstract():
    assert not inspect.isabstract(grammar::features::StarContainment)


def test_grammar::features::starcontainment_constructor_exists():
    assert callable(grammar::features::StarContainment.__init__)


def test_grammar::features::starcontainment_constructor_args():
    sig = inspect.signature(grammar::features::StarContainment.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::pluscontainment_is_not_abstract():
    assert not inspect.isabstract(grammar::features::PlusContainment)


def test_grammar::features::pluscontainment_constructor_exists():
    assert callable(grammar::features::PlusContainment.__init__)


def test_grammar::features::pluscontainment_constructor_args():
    sig = inspect.signature(grammar::features::PlusContainment.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::mandatorycontainment_is_not_abstract():
    assert not inspect.isabstract(grammar::features::MandatoryContainment)


def test_grammar::features::mandatorycontainment_constructor_exists():
    assert callable(grammar::features::MandatoryContainment.__init__)


def test_grammar::features::mandatorycontainment_constructor_args():
    sig = inspect.signature(grammar::features::MandatoryContainment.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::x_is_not_abstract():
    assert not inspect.isabstract(grammar::features::X)


def test_grammar::features::x_constructor_exists():
    assert callable(grammar::features::X.__init__)


def test_grammar::features::x_constructor_args():
    sig = inspect.signature(grammar::features::X.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_grammar::features::x_has_name():
    assert hasattr(grammar::features::X, "name")
    descriptor = None
    for klass in grammar::features::X.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_grammar::features::optionalcontainment_is_not_abstract():
    assert not inspect.isabstract(grammar::features::OptionalContainment)


def test_grammar::features::optionalcontainment_constructor_exists():
    assert callable(grammar::features::OptionalContainment.__init__)


def test_grammar::features::optionalcontainment_constructor_args():
    sig = inspect.signature(grammar::features::OptionalContainment.__init__)
    params = list(sig.parameters.keys())



def test_abstractsuperclass_is_not_abstract():
    assert not inspect.isabstract(AbstractSuperclass)


def test_abstractsuperclass_constructor_exists():
    assert callable(AbstractSuperclass.__init__)


def test_abstractsuperclass_constructor_args():
    sig = inspect.signature(AbstractSuperclass.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::concretesubclassb_is_not_abstract():
    assert not inspect.isabstract(grammar::features::ConcreteSubclassB)


def test_grammar::features::concretesubclassb_constructor_exists():
    assert callable(grammar::features::ConcreteSubclassB.__init__)


def test_grammar::features::concretesubclassb_constructor_args():
    sig = inspect.signature(grammar::features::ConcreteSubclassB.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::concretesubclassa_is_not_abstract():
    assert not inspect.isabstract(grammar::features::ConcreteSubclassA)


def test_grammar::features::concretesubclassa_constructor_exists():
    assert callable(grammar::features::ConcreteSubclassA.__init__)


def test_grammar::features::concretesubclassa_constructor_args():
    sig = inspect.signature(grammar::features::ConcreteSubclassA.__init__)
    params = list(sig.parameters.keys())



def test_grammar::features::abstractsuperclass_is_not_abstract():
    assert not inspect.isabstract(grammar::features::AbstractSuperclass)


def test_grammar::features::abstractsuperclass_constructor_exists():
    assert callable(grammar::features::AbstractSuperclass.__init__)


def test_grammar::features::abstractsuperclass_constructor_args():
    sig = inspect.signature(grammar::features::AbstractSuperclass.__init__)
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
grammar::features::SecondRoot_strategy = st.builds(
    grammar::features::SecondRoot,
)
Child_strategy = st.builds(
    Child,
)
grammar::features::StarNonContainment_strategy = st.builds(
    grammar::features::StarNonContainment,
)
grammar::features::ClassWithAttributes_strategy = st.builds(
    grammar::features::ClassWithAttributes,
    a1=
        safe_text,
    a2=
        st.booleans()
)
grammar::features::CompoundPlus_strategy = st.builds(
    grammar::features::CompoundPlus,
)
grammar::features::StarPrefix_strategy = st.builds(
    grammar::features::StarPrefix,
)
grammar::features::OptionalPrefix_strategy = st.builds(
    grammar::features::OptionalPrefix,
)
grammar::features::PlusPrefix_strategy = st.builds(
    grammar::features::PlusPrefix,
)
grammar::features::CompoundStar_strategy = st.builds(
    grammar::features::CompoundStar,
)
grammar::features::CompoundOptional_strategy = st.builds(
    grammar::features::CompoundOptional,
)
grammar::features::AlternativeSyntax_strategy = st.builds(
    grammar::features::AlternativeSyntax,
)
grammar::features::Child_strategy = st.builds(
    grammar::features::Child,
)
grammar::features::Root_strategy = st.builds(
    grammar::features::Root,
)
grammar::features::PlusNonContainment_strategy = st.builds(
    grammar::features::PlusNonContainment,
)
grammar::features::MandatoryNonContainment_strategy = st.builds(
    grammar::features::MandatoryNonContainment,
)
grammar::features::OptionalNonContainment_strategy = st.builds(
    grammar::features::OptionalNonContainment,
)
grammar::features::StarContainment_strategy = st.builds(
    grammar::features::StarContainment,
)
grammar::features::PlusContainment_strategy = st.builds(
    grammar::features::PlusContainment,
)
grammar::features::MandatoryContainment_strategy = st.builds(
    grammar::features::MandatoryContainment,
)
grammar::features::X_strategy = st.builds(
    grammar::features::X,
    name=
        safe_text
)
grammar::features::OptionalContainment_strategy = st.builds(
    grammar::features::OptionalContainment,
)
AbstractSuperclass_strategy = st.builds(
    AbstractSuperclass,
)
grammar::features::ConcreteSubclassB_strategy = st.builds(
    grammar::features::ConcreteSubclassB,
)
grammar::features::ConcreteSubclassA_strategy = st.builds(
    grammar::features::ConcreteSubclassA,
)
grammar::features::AbstractSuperclass_strategy = st.builds(
    grammar::features::AbstractSuperclass,
)

@given(instance=grammar::features::SecondRoot_strategy)
@settings(max_examples=50)
def test_grammar::features::secondroot_instantiation(instance):
    assert isinstance(instance, grammar::features::SecondRoot)

@given(instance=Child_strategy)
@settings(max_examples=50)
def test_child_instantiation(instance):
    assert isinstance(instance, Child)

@given(instance=grammar::features::StarNonContainment_strategy)
@settings(max_examples=50)
def test_grammar::features::starnoncontainment_instantiation(instance):
    assert isinstance(instance, grammar::features::StarNonContainment)

@given(instance=grammar::features::ClassWithAttributes_strategy)
@settings(max_examples=50)
def test_grammar::features::classwithattributes_instantiation(instance):
    assert isinstance(instance, grammar::features::ClassWithAttributes)

@given(instance=grammar::features::ClassWithAttributes_strategy)
def test_grammar::features::classwithattributes_a1_type(instance):
    assert isinstance(instance.a1, str)


@given(instance=grammar::features::ClassWithAttributes_strategy)
def test_grammar::features::classwithattributes_a1_setter(instance):
    original = instance.a1
    instance.a1 = original
    assert instance.a1 == original

@given(instance=grammar::features::ClassWithAttributes_strategy)
def test_grammar::features::classwithattributes_a2_type(instance):
    assert isinstance(instance.a2, bool)


@given(instance=grammar::features::ClassWithAttributes_strategy)
def test_grammar::features::classwithattributes_a2_setter(instance):
    original = instance.a2
    instance.a2 = original
    assert instance.a2 == original

@given(instance=grammar::features::CompoundPlus_strategy)
@settings(max_examples=50)
def test_grammar::features::compoundplus_instantiation(instance):
    assert isinstance(instance, grammar::features::CompoundPlus)

@given(instance=grammar::features::StarPrefix_strategy)
@settings(max_examples=50)
def test_grammar::features::starprefix_instantiation(instance):
    assert isinstance(instance, grammar::features::StarPrefix)

@given(instance=grammar::features::OptionalPrefix_strategy)
@settings(max_examples=50)
def test_grammar::features::optionalprefix_instantiation(instance):
    assert isinstance(instance, grammar::features::OptionalPrefix)

@given(instance=grammar::features::PlusPrefix_strategy)
@settings(max_examples=50)
def test_grammar::features::plusprefix_instantiation(instance):
    assert isinstance(instance, grammar::features::PlusPrefix)

@given(instance=grammar::features::CompoundStar_strategy)
@settings(max_examples=50)
def test_grammar::features::compoundstar_instantiation(instance):
    assert isinstance(instance, grammar::features::CompoundStar)

@given(instance=grammar::features::CompoundOptional_strategy)
@settings(max_examples=50)
def test_grammar::features::compoundoptional_instantiation(instance):
    assert isinstance(instance, grammar::features::CompoundOptional)

@given(instance=grammar::features::AlternativeSyntax_strategy)
@settings(max_examples=50)
def test_grammar::features::alternativesyntax_instantiation(instance):
    assert isinstance(instance, grammar::features::AlternativeSyntax)

@given(instance=grammar::features::Child_strategy)
@settings(max_examples=50)
def test_grammar::features::child_instantiation(instance):
    assert isinstance(instance, grammar::features::Child)

@given(instance=grammar::features::Root_strategy)
@settings(max_examples=50)
def test_grammar::features::root_instantiation(instance):
    assert isinstance(instance, grammar::features::Root)

@given(instance=grammar::features::PlusNonContainment_strategy)
@settings(max_examples=50)
def test_grammar::features::plusnoncontainment_instantiation(instance):
    assert isinstance(instance, grammar::features::PlusNonContainment)

@given(instance=grammar::features::MandatoryNonContainment_strategy)
@settings(max_examples=50)
def test_grammar::features::mandatorynoncontainment_instantiation(instance):
    assert isinstance(instance, grammar::features::MandatoryNonContainment)

@given(instance=grammar::features::OptionalNonContainment_strategy)
@settings(max_examples=50)
def test_grammar::features::optionalnoncontainment_instantiation(instance):
    assert isinstance(instance, grammar::features::OptionalNonContainment)

@given(instance=grammar::features::StarContainment_strategy)
@settings(max_examples=50)
def test_grammar::features::starcontainment_instantiation(instance):
    assert isinstance(instance, grammar::features::StarContainment)

@given(instance=grammar::features::PlusContainment_strategy)
@settings(max_examples=50)
def test_grammar::features::pluscontainment_instantiation(instance):
    assert isinstance(instance, grammar::features::PlusContainment)

@given(instance=grammar::features::MandatoryContainment_strategy)
@settings(max_examples=50)
def test_grammar::features::mandatorycontainment_instantiation(instance):
    assert isinstance(instance, grammar::features::MandatoryContainment)

@given(instance=grammar::features::X_strategy)
@settings(max_examples=50)
def test_grammar::features::x_instantiation(instance):
    assert isinstance(instance, grammar::features::X)

@given(instance=grammar::features::X_strategy)
def test_grammar::features::x_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=grammar::features::X_strategy)
def test_grammar::features::x_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=grammar::features::OptionalContainment_strategy)
@settings(max_examples=50)
def test_grammar::features::optionalcontainment_instantiation(instance):
    assert isinstance(instance, grammar::features::OptionalContainment)

@given(instance=AbstractSuperclass_strategy)
@settings(max_examples=50)
def test_abstractsuperclass_instantiation(instance):
    assert isinstance(instance, AbstractSuperclass)

@given(instance=grammar::features::ConcreteSubclassB_strategy)
@settings(max_examples=50)
def test_grammar::features::concretesubclassb_instantiation(instance):
    assert isinstance(instance, grammar::features::ConcreteSubclassB)

@given(instance=grammar::features::ConcreteSubclassA_strategy)
@settings(max_examples=50)
def test_grammar::features::concretesubclassa_instantiation(instance):
    assert isinstance(instance, grammar::features::ConcreteSubclassA)

@given(instance=grammar::features::AbstractSuperclass_strategy)
@settings(max_examples=50)
def test_grammar::features::abstractsuperclass_instantiation(instance):
    assert isinstance(instance, grammar::features::AbstractSuperclass)
