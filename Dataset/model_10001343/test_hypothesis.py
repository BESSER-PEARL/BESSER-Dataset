import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Actor7_Actor,
    Actor6_Actor,
    Actor5_Actor,
    Component3_Component,
    Component2_Component,
    Actor4_Actor,
    Actor3_Actor,
    Actor2_Actor,
    Component_Component,
    Actor_Actor,
    Funcionario,
    Pessoa,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_actor7_actor_is_not_abstract():
    assert not inspect.isabstract(Actor7_Actor)


def test_actor7_actor_constructor_exists():
    assert callable(Actor7_Actor.__init__)


def test_actor7_actor_constructor_args():
    sig = inspect.signature(Actor7_Actor.__init__)
    params = list(sig.parameters.keys())



def test_actor6_actor_is_not_abstract():
    assert not inspect.isabstract(Actor6_Actor)


def test_actor6_actor_constructor_exists():
    assert callable(Actor6_Actor.__init__)


def test_actor6_actor_constructor_args():
    sig = inspect.signature(Actor6_Actor.__init__)
    params = list(sig.parameters.keys())



def test_actor5_actor_is_not_abstract():
    assert not inspect.isabstract(Actor5_Actor)


def test_actor5_actor_constructor_exists():
    assert callable(Actor5_Actor.__init__)


def test_actor5_actor_constructor_args():
    sig = inspect.signature(Actor5_Actor.__init__)
    params = list(sig.parameters.keys())



def test_component3_component_is_not_abstract():
    assert not inspect.isabstract(Component3_Component)


def test_component3_component_constructor_exists():
    assert callable(Component3_Component.__init__)


def test_component3_component_constructor_args():
    sig = inspect.signature(Component3_Component.__init__)
    params = list(sig.parameters.keys())



def test_component2_component_is_not_abstract():
    assert not inspect.isabstract(Component2_Component)


def test_component2_component_constructor_exists():
    assert callable(Component2_Component.__init__)


def test_component2_component_constructor_args():
    sig = inspect.signature(Component2_Component.__init__)
    params = list(sig.parameters.keys())



def test_actor4_actor_is_not_abstract():
    assert not inspect.isabstract(Actor4_Actor)


def test_actor4_actor_constructor_exists():
    assert callable(Actor4_Actor.__init__)


def test_actor4_actor_constructor_args():
    sig = inspect.signature(Actor4_Actor.__init__)
    params = list(sig.parameters.keys())



def test_actor3_actor_is_not_abstract():
    assert not inspect.isabstract(Actor3_Actor)


def test_actor3_actor_constructor_exists():
    assert callable(Actor3_Actor.__init__)


def test_actor3_actor_constructor_args():
    sig = inspect.signature(Actor3_Actor.__init__)
    params = list(sig.parameters.keys())



def test_actor2_actor_is_not_abstract():
    assert not inspect.isabstract(Actor2_Actor)


def test_actor2_actor_constructor_exists():
    assert callable(Actor2_Actor.__init__)


def test_actor2_actor_constructor_args():
    sig = inspect.signature(Actor2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_component_component_is_not_abstract():
    assert not inspect.isabstract(Component_Component)


def test_component_component_constructor_exists():
    assert callable(Component_Component.__init__)


def test_component_component_constructor_args():
    sig = inspect.signature(Component_Component.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_funcionario_is_not_abstract():
    assert not inspect.isabstract(Funcionario)


def test_funcionario_constructor_exists():
    assert callable(Funcionario.__init__)


def test_funcionario_constructor_args():
    sig = inspect.signature(Funcionario.__init__)
    params = list(sig.parameters.keys())
    assert "cracha" in params, "Missing parameter 'cracha'"

def test_funcionario_has_cracha():
    assert hasattr(Funcionario, "cracha")
    descriptor = None
    for klass in Funcionario.__mro__:
        if "cracha" in klass.__dict__:
            descriptor = klass.__dict__["cracha"]
            break
    assert isinstance(descriptor, property)



def test_pessoa_is_not_abstract():
    assert not inspect.isabstract(Pessoa)


def test_pessoa_constructor_exists():
    assert callable(Pessoa.__init__)


def test_pessoa_constructor_args():
    sig = inspect.signature(Pessoa.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "idade" in params, "Missing parameter 'idade'"

def test_pessoa_has_id():
    assert hasattr(Pessoa, "id")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pessoa_has_Nome():
    assert hasattr(Pessoa, "Nome")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)

def test_pessoa_has_idade():
    assert hasattr(Pessoa, "idade")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "idade" in klass.__dict__:
            descriptor = klass.__dict__["idade"]
            break
    assert isinstance(descriptor, property)


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
Actor7_Actor_strategy = st.builds(
    Actor7_Actor,
)
Actor6_Actor_strategy = st.builds(
    Actor6_Actor,
)
Actor5_Actor_strategy = st.builds(
    Actor5_Actor,
)
Component3_Component_strategy = st.builds(
    Component3_Component,
)
Component2_Component_strategy = st.builds(
    Component2_Component,
)
Actor4_Actor_strategy = st.builds(
    Actor4_Actor,
)
Actor3_Actor_strategy = st.builds(
    Actor3_Actor,
)
Actor2_Actor_strategy = st.builds(
    Actor2_Actor,
)
Component_Component_strategy = st.builds(
    Component_Component,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
Funcionario_strategy = st.builds(
    Funcionario,
    cracha=
        st.integers()
)
Pessoa_strategy = st.builds(
    Pessoa,
    id=
        st.integers(),
    Nome=
        safe_text,
    idade=
        st.integers()
)

@given(instance=Actor7_Actor_strategy)
@settings(max_examples=50)
def test_actor7_actor_instantiation(instance):
    assert isinstance(instance, Actor7_Actor)

@given(instance=Actor6_Actor_strategy)
@settings(max_examples=50)
def test_actor6_actor_instantiation(instance):
    assert isinstance(instance, Actor6_Actor)

@given(instance=Actor5_Actor_strategy)
@settings(max_examples=50)
def test_actor5_actor_instantiation(instance):
    assert isinstance(instance, Actor5_Actor)

@given(instance=Component3_Component_strategy)
@settings(max_examples=50)
def test_component3_component_instantiation(instance):
    assert isinstance(instance, Component3_Component)

@given(instance=Component2_Component_strategy)
@settings(max_examples=50)
def test_component2_component_instantiation(instance):
    assert isinstance(instance, Component2_Component)

@given(instance=Actor4_Actor_strategy)
@settings(max_examples=50)
def test_actor4_actor_instantiation(instance):
    assert isinstance(instance, Actor4_Actor)

@given(instance=Actor3_Actor_strategy)
@settings(max_examples=50)
def test_actor3_actor_instantiation(instance):
    assert isinstance(instance, Actor3_Actor)

@given(instance=Actor2_Actor_strategy)
@settings(max_examples=50)
def test_actor2_actor_instantiation(instance):
    assert isinstance(instance, Actor2_Actor)

@given(instance=Component_Component_strategy)
@settings(max_examples=50)
def test_component_component_instantiation(instance):
    assert isinstance(instance, Component_Component)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=Funcionario_strategy)
@settings(max_examples=50)
def test_funcionario_instantiation(instance):
    assert isinstance(instance, Funcionario)



@given(instance=Funcionario_strategy)
def test_funcionario_cracha_setter(instance):
    original = instance.cracha
    instance.cracha = original
    assert instance.cracha == original

@given(instance=Pessoa_strategy)
@settings(max_examples=50)
def test_pessoa_instantiation(instance):
    assert isinstance(instance, Pessoa)



@given(instance=Pessoa_strategy)
def test_pessoa_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Pessoa_strategy)
def test_pessoa_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=Pessoa_strategy)
def test_pessoa_idade_setter(instance):
    original = instance.idade
    instance.idade = original
    assert instance.idade == original
