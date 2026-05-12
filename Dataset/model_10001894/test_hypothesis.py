import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Dash2,
    Dash,
    Spell,
    Weapon,
    Action,
    CastSpell,
    WeaponAttack,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dash2_is_not_abstract():
    assert not inspect.isabstract(Dash2)


def test_dash2_constructor_exists():
    assert callable(Dash2.__init__)


def test_dash2_constructor_args():
    sig = inspect.signature(Dash2.__init__)
    params = list(sig.parameters.keys())
    assert "execute__" in params, "Missing parameter 'execute__'"

def test_dash2_has_execute__():
    assert hasattr(Dash2, "execute__")
    descriptor = None
    for klass in Dash2.__mro__:
        if "execute__" in klass.__dict__:
            descriptor = klass.__dict__["execute__"]
            break
    assert isinstance(descriptor, property)



def test_dash_is_not_abstract():
    assert not inspect.isabstract(Dash)


def test_dash_constructor_exists():
    assert callable(Dash.__init__)


def test_dash_constructor_args():
    sig = inspect.signature(Dash.__init__)
    params = list(sig.parameters.keys())
    assert "execute__" in params, "Missing parameter 'execute__'"

def test_dash_has_execute__():
    assert hasattr(Dash, "execute__")
    descriptor = None
    for klass in Dash.__mro__:
        if "execute__" in klass.__dict__:
            descriptor = klass.__dict__["execute__"]
            break
    assert isinstance(descriptor, property)



def test_spell_is_not_abstract():
    assert not inspect.isabstract(Spell)


def test_spell_constructor_exists():
    assert callable(Spell.__init__)


def test_spell_constructor_args():
    sig = inspect.signature(Spell.__init__)
    params = list(sig.parameters.keys())



def test_weapon_is_not_abstract():
    assert not inspect.isabstract(Weapon)


def test_weapon_constructor_exists():
    assert callable(Weapon.__init__)


def test_weapon_constructor_args():
    sig = inspect.signature(Weapon.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())
    assert "execute__" in params, "Missing parameter 'execute__'"

def test_action_has_execute__():
    assert hasattr(Action, "execute__")
    descriptor = None
    for klass in Action.__mro__:
        if "execute__" in klass.__dict__:
            descriptor = klass.__dict__["execute__"]
            break
    assert isinstance(descriptor, property)



def test_castspell_is_not_abstract():
    assert not inspect.isabstract(CastSpell)


def test_castspell_constructor_exists():
    assert callable(CastSpell.__init__)


def test_castspell_constructor_args():
    sig = inspect.signature(CastSpell.__init__)
    params = list(sig.parameters.keys())
    assert "spell" in params, "Missing parameter 'spell'"
    assert "execute__" in params, "Missing parameter 'execute__'"

def test_castspell_has_spell():
    assert hasattr(CastSpell, "spell")
    descriptor = None
    for klass in CastSpell.__mro__:
        if "spell" in klass.__dict__:
            descriptor = klass.__dict__["spell"]
            break
    assert isinstance(descriptor, property)

def test_castspell_has_execute__():
    assert hasattr(CastSpell, "execute__")
    descriptor = None
    for klass in CastSpell.__mro__:
        if "execute__" in klass.__dict__:
            descriptor = klass.__dict__["execute__"]
            break
    assert isinstance(descriptor, property)



def test_weaponattack_is_not_abstract():
    assert not inspect.isabstract(WeaponAttack)


def test_weaponattack_constructor_exists():
    assert callable(WeaponAttack.__init__)


def test_weaponattack_constructor_args():
    sig = inspect.signature(WeaponAttack.__init__)
    params = list(sig.parameters.keys())
    assert "execute__" in params, "Missing parameter 'execute__'"
    assert "weapon" in params, "Missing parameter 'weapon'"

def test_weaponattack_has_execute__():
    assert hasattr(WeaponAttack, "execute__")
    descriptor = None
    for klass in WeaponAttack.__mro__:
        if "execute__" in klass.__dict__:
            descriptor = klass.__dict__["execute__"]
            break
    assert isinstance(descriptor, property)

def test_weaponattack_has_weapon():
    assert hasattr(WeaponAttack, "weapon")
    descriptor = None
    for klass in WeaponAttack.__mro__:
        if "weapon" in klass.__dict__:
            descriptor = klass.__dict__["weapon"]
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
Dash2_strategy = st.builds(
    Dash2,
    execute__=
        safe_text
)
Dash_strategy = st.builds(
    Dash,
    execute__=
        safe_text
)
Spell_strategy = st.builds(
    Spell,
)
Weapon_strategy = st.builds(
    Weapon,
)
Action_strategy = st.builds(
    Action,
    execute__=
        safe_text
)
CastSpell_strategy = st.builds(
    CastSpell,
    spell=
        st.none(),
    execute__=
        safe_text
)
WeaponAttack_strategy = st.builds(
    WeaponAttack,
    execute__=
        safe_text,
    weapon=
        st.none()
)

@given(instance=Dash2_strategy)
@settings(max_examples=50)
def test_dash2_instantiation(instance):
    assert isinstance(instance, Dash2)



@given(instance=Dash2_strategy)
def test_dash2_execute___setter(instance):
    original = instance.execute__
    instance.execute__ = original
    assert instance.execute__ == original

@given(instance=Dash_strategy)
@settings(max_examples=50)
def test_dash_instantiation(instance):
    assert isinstance(instance, Dash)



@given(instance=Dash_strategy)
def test_dash_execute___setter(instance):
    original = instance.execute__
    instance.execute__ = original
    assert instance.execute__ == original

@given(instance=Spell_strategy)
@settings(max_examples=50)
def test_spell_instantiation(instance):
    assert isinstance(instance, Spell)

@given(instance=Weapon_strategy)
@settings(max_examples=50)
def test_weapon_instantiation(instance):
    assert isinstance(instance, Weapon)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)



@given(instance=Action_strategy)
def test_action_execute___setter(instance):
    original = instance.execute__
    instance.execute__ = original
    assert instance.execute__ == original

@given(instance=CastSpell_strategy)
@settings(max_examples=50)
def test_castspell_instantiation(instance):
    assert isinstance(instance, CastSpell)



@given(instance=CastSpell_strategy)
def test_castspell_spell_setter(instance):
    original = instance.spell
    instance.spell = original
    assert instance.spell == original



@given(instance=CastSpell_strategy)
def test_castspell_execute___setter(instance):
    original = instance.execute__
    instance.execute__ = original
    assert instance.execute__ == original

@given(instance=WeaponAttack_strategy)
@settings(max_examples=50)
def test_weaponattack_instantiation(instance):
    assert isinstance(instance, WeaponAttack)



@given(instance=WeaponAttack_strategy)
def test_weaponattack_execute___setter(instance):
    original = instance.execute__
    instance.execute__ = original
    assert instance.execute__ == original



@given(instance=WeaponAttack_strategy)
def test_weaponattack_weapon_setter(instance):
    original = instance.weapon
    instance.weapon = original
    assert instance.weapon == original
