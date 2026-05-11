import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data::Modele,
    Data::DeclarationType,
    Data::Attribut,
    DeclarationType,
    Data::Classe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data::modele_is_not_abstract():
    assert not inspect.isabstract(Data::Modele)


def test_data::modele_constructor_exists():
    assert callable(Data::Modele.__init__)


def test_data::modele_constructor_args():
    sig = inspect.signature(Data::Modele.__init__)
    params = list(sig.parameters.keys())



def test_data::declarationtype_is_not_abstract():
    assert not inspect.isabstract(Data::DeclarationType)


def test_data::declarationtype_constructor_exists():
    assert callable(Data::DeclarationType.__init__)


def test_data::declarationtype_constructor_args():
    sig = inspect.signature(Data::DeclarationType.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_data::declarationtype_has_nom():
    assert hasattr(Data::DeclarationType, "nom")
    descriptor = None
    for klass in Data::DeclarationType.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_data::attribut_is_not_abstract():
    assert not inspect.isabstract(Data::Attribut)


def test_data::attribut_constructor_exists():
    assert callable(Data::Attribut.__init__)


def test_data::attribut_constructor_args():
    sig = inspect.signature(Data::Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "estTableau" in params, "Missing parameter 'estTableau'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "typeStr" in params, "Missing parameter 'typeStr'"

def test_data::attribut_has_estTableau():
    assert hasattr(Data::Attribut, "estTableau")
    descriptor = None
    for klass in Data::Attribut.__mro__:
        if "estTableau" in klass.__dict__:
            descriptor = klass.__dict__["estTableau"]
            break
    assert isinstance(descriptor, property)

def test_data::attribut_has_nom():
    assert hasattr(Data::Attribut, "nom")
    descriptor = None
    for klass in Data::Attribut.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_data::attribut_has_typeStr():
    assert hasattr(Data::Attribut, "typeStr")
    descriptor = None
    for klass in Data::Attribut.__mro__:
        if "typeStr" in klass.__dict__:
            descriptor = klass.__dict__["typeStr"]
            break
    assert isinstance(descriptor, property)



def test_declarationtype_is_not_abstract():
    assert not inspect.isabstract(DeclarationType)


def test_declarationtype_constructor_exists():
    assert callable(DeclarationType.__init__)


def test_declarationtype_constructor_args():
    sig = inspect.signature(DeclarationType.__init__)
    params = list(sig.parameters.keys())



def test_data::classe_is_not_abstract():
    assert not inspect.isabstract(Data::Classe)


def test_data::classe_constructor_exists():
    assert callable(Data::Classe.__init__)


def test_data::classe_constructor_args():
    sig = inspect.signature(Data::Classe.__init__)
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
Data::Modele_strategy = st.builds(
    Data::Modele,
)
Data::DeclarationType_strategy = st.builds(
    Data::DeclarationType,
    nom=
        safe_text
)
Data::Attribut_strategy = st.builds(
    Data::Attribut,
    estTableau=
        st.booleans(),
    nom=
        safe_text,
    typeStr=
        safe_text
)
DeclarationType_strategy = st.builds(
    DeclarationType,
)
Data::Classe_strategy = st.builds(
    Data::Classe,
)

@given(instance=Data::Modele_strategy)
@settings(max_examples=50)
def test_data::modele_instantiation(instance):
    assert isinstance(instance, Data::Modele)

@given(instance=Data::DeclarationType_strategy)
@settings(max_examples=50)
def test_data::declarationtype_instantiation(instance):
    assert isinstance(instance, Data::DeclarationType)

@given(instance=Data::DeclarationType_strategy)
def test_data::declarationtype_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=Data::DeclarationType_strategy)
def test_data::declarationtype_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=Data::Attribut_strategy)
@settings(max_examples=50)
def test_data::attribut_instantiation(instance):
    assert isinstance(instance, Data::Attribut)

@given(instance=Data::Attribut_strategy)
def test_data::attribut_estTableau_type(instance):
    assert isinstance(instance.estTableau, bool)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_estTableau_setter(instance):
    original = instance.estTableau
    instance.estTableau = original
    assert instance.estTableau == original

@given(instance=Data::Attribut_strategy)
def test_data::attribut_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=Data::Attribut_strategy)
def test_data::attribut_typeStr_type(instance):
    assert isinstance(instance.typeStr, str)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_typeStr_setter(instance):
    original = instance.typeStr
    instance.typeStr = original
    assert instance.typeStr == original

@given(instance=DeclarationType_strategy)
@settings(max_examples=50)
def test_declarationtype_instantiation(instance):
    assert isinstance(instance, DeclarationType)

@given(instance=Data::Classe_strategy)
@settings(max_examples=50)
def test_data::classe_instantiation(instance):
    assert isinstance(instance, Data::Classe)
