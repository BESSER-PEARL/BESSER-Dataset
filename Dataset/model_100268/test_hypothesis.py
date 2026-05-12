import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Label,
    cpndefinition::CPNInscription,
    CPNInscription,
    cpndefinition::Sort,
    Page,
    cpndefinition::Page,
    cpndefinition::Guard,
    Transition,
    cpndefinition::Transition,
    cpndefinition::ArcExpression,
    Arc,
    cpndefinition::Arc,
    cpndefinition::InitialMarking,
    Place,
    cpndefinition::Place,
    PetriNetType,
    cpndefinition::CPN,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_cpndefinition::cpninscription_is_not_abstract():
    assert not inspect.isabstract(cpndefinition::CPNInscription)


def test_cpndefinition::cpninscription_constructor_exists():
    assert callable(cpndefinition::CPNInscription.__init__)


def test_cpndefinition::cpninscription_constructor_args():
    sig = inspect.signature(cpndefinition::CPNInscription.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_cpndefinition::cpninscription_has_text():
    assert hasattr(cpndefinition::CPNInscription, "text")
    descriptor = None
    for klass in cpndefinition::CPNInscription.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_cpninscription_is_not_abstract():
    assert not inspect.isabstract(CPNInscription)


def test_cpninscription_constructor_exists():
    assert callable(CPNInscription.__init__)


def test_cpninscription_constructor_args():
    sig = inspect.signature(CPNInscription.__init__)
    params = list(sig.parameters.keys())



def test_cpndefinition::sort_is_not_abstract():
    assert not inspect.isabstract(cpndefinition::Sort)


def test_cpndefinition::sort_constructor_exists():
    assert callable(cpndefinition::Sort.__init__)


def test_cpndefinition::sort_constructor_args():
    sig = inspect.signature(cpndefinition::Sort.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_cpndefinition::page_is_not_abstract():
    assert not inspect.isabstract(cpndefinition::Page)


def test_cpndefinition::page_constructor_exists():
    assert callable(cpndefinition::Page.__init__)


def test_cpndefinition::page_constructor_args():
    sig = inspect.signature(cpndefinition::Page.__init__)
    params = list(sig.parameters.keys())



def test_cpndefinition::guard_is_not_abstract():
    assert not inspect.isabstract(cpndefinition::Guard)


def test_cpndefinition::guard_constructor_exists():
    assert callable(cpndefinition::Guard.__init__)


def test_cpndefinition::guard_constructor_args():
    sig = inspect.signature(cpndefinition::Guard.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_cpndefinition::transition_is_not_abstract():
    assert not inspect.isabstract(cpndefinition::Transition)


def test_cpndefinition::transition_constructor_exists():
    assert callable(cpndefinition::Transition.__init__)


def test_cpndefinition::transition_constructor_args():
    sig = inspect.signature(cpndefinition::Transition.__init__)
    params = list(sig.parameters.keys())



def test_cpndefinition::arcexpression_is_not_abstract():
    assert not inspect.isabstract(cpndefinition::ArcExpression)


def test_cpndefinition::arcexpression_constructor_exists():
    assert callable(cpndefinition::ArcExpression.__init__)


def test_cpndefinition::arcexpression_constructor_args():
    sig = inspect.signature(cpndefinition::ArcExpression.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_cpndefinition::arc_is_not_abstract():
    assert not inspect.isabstract(cpndefinition::Arc)


def test_cpndefinition::arc_constructor_exists():
    assert callable(cpndefinition::Arc.__init__)


def test_cpndefinition::arc_constructor_args():
    sig = inspect.signature(cpndefinition::Arc.__init__)
    params = list(sig.parameters.keys())



def test_cpndefinition::initialmarking_is_not_abstract():
    assert not inspect.isabstract(cpndefinition::InitialMarking)


def test_cpndefinition::initialmarking_constructor_exists():
    assert callable(cpndefinition::InitialMarking.__init__)


def test_cpndefinition::initialmarking_constructor_args():
    sig = inspect.signature(cpndefinition::InitialMarking.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_cpndefinition::place_is_not_abstract():
    assert not inspect.isabstract(cpndefinition::Place)


def test_cpndefinition::place_constructor_exists():
    assert callable(cpndefinition::Place.__init__)


def test_cpndefinition::place_constructor_args():
    sig = inspect.signature(cpndefinition::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinettype_is_not_abstract():
    assert not inspect.isabstract(PetriNetType)


def test_petrinettype_constructor_exists():
    assert callable(PetriNetType.__init__)


def test_petrinettype_constructor_args():
    sig = inspect.signature(PetriNetType.__init__)
    params = list(sig.parameters.keys())



def test_cpndefinition::cpn_is_not_abstract():
    assert not inspect.isabstract(cpndefinition::CPN)


def test_cpndefinition::cpn_constructor_exists():
    assert callable(cpndefinition::CPN.__init__)


def test_cpndefinition::cpn_constructor_args():
    sig = inspect.signature(cpndefinition::CPN.__init__)
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
Label_strategy = st.builds(
    Label,
)
cpndefinition::CPNInscription_strategy = st.builds(
    cpndefinition::CPNInscription,
    text=
        safe_text
)
CPNInscription_strategy = st.builds(
    CPNInscription,
)
cpndefinition::Sort_strategy = st.builds(
    cpndefinition::Sort,
)
Page_strategy = st.builds(
    Page,
)
cpndefinition::Page_strategy = st.builds(
    cpndefinition::Page,
)
cpndefinition::Guard_strategy = st.builds(
    cpndefinition::Guard,
)
Transition_strategy = st.builds(
    Transition,
)
cpndefinition::Transition_strategy = st.builds(
    cpndefinition::Transition,
)
cpndefinition::ArcExpression_strategy = st.builds(
    cpndefinition::ArcExpression,
)
Arc_strategy = st.builds(
    Arc,
)
cpndefinition::Arc_strategy = st.builds(
    cpndefinition::Arc,
)
cpndefinition::InitialMarking_strategy = st.builds(
    cpndefinition::InitialMarking,
)
Place_strategy = st.builds(
    Place,
)
cpndefinition::Place_strategy = st.builds(
    cpndefinition::Place,
)
PetriNetType_strategy = st.builds(
    PetriNetType,
)
cpndefinition::CPN_strategy = st.builds(
    cpndefinition::CPN,
)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=cpndefinition::CPNInscription_strategy)
@settings(max_examples=50)
def test_cpndefinition::cpninscription_instantiation(instance):
    assert isinstance(instance, cpndefinition::CPNInscription)

@given(instance=cpndefinition::CPNInscription_strategy)
def test_cpndefinition::cpninscription_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=cpndefinition::CPNInscription_strategy)
def test_cpndefinition::cpninscription_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=CPNInscription_strategy)
@settings(max_examples=50)
def test_cpninscription_instantiation(instance):
    assert isinstance(instance, CPNInscription)

@given(instance=cpndefinition::Sort_strategy)
@settings(max_examples=50)
def test_cpndefinition::sort_instantiation(instance):
    assert isinstance(instance, cpndefinition::Sort)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=cpndefinition::Page_strategy)
@settings(max_examples=50)
def test_cpndefinition::page_instantiation(instance):
    assert isinstance(instance, cpndefinition::Page)

@given(instance=cpndefinition::Guard_strategy)
@settings(max_examples=50)
def test_cpndefinition::guard_instantiation(instance):
    assert isinstance(instance, cpndefinition::Guard)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=cpndefinition::Transition_strategy)
@settings(max_examples=50)
def test_cpndefinition::transition_instantiation(instance):
    assert isinstance(instance, cpndefinition::Transition)

@given(instance=cpndefinition::ArcExpression_strategy)
@settings(max_examples=50)
def test_cpndefinition::arcexpression_instantiation(instance):
    assert isinstance(instance, cpndefinition::ArcExpression)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=cpndefinition::Arc_strategy)
@settings(max_examples=50)
def test_cpndefinition::arc_instantiation(instance):
    assert isinstance(instance, cpndefinition::Arc)

@given(instance=cpndefinition::InitialMarking_strategy)
@settings(max_examples=50)
def test_cpndefinition::initialmarking_instantiation(instance):
    assert isinstance(instance, cpndefinition::InitialMarking)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=cpndefinition::Place_strategy)
@settings(max_examples=50)
def test_cpndefinition::place_instantiation(instance):
    assert isinstance(instance, cpndefinition::Place)

@given(instance=PetriNetType_strategy)
@settings(max_examples=50)
def test_petrinettype_instantiation(instance):
    assert isinstance(instance, PetriNetType)

@given(instance=cpndefinition::CPN_strategy)
@settings(max_examples=50)
def test_cpndefinition::cpn_instantiation(instance):
    assert isinstance(instance, cpndefinition::CPN)
