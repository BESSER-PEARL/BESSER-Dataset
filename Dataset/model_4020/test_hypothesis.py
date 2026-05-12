import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Data_Modele,
    Data_DeclarationType,
    Data_Attribut,
    DeclarationType,
    Data_Classe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_modele_is_not_abstract():
    assert not inspect.isabstract(Data_Modele)


def test_data_modele_constructor_exists():
    assert callable(Data_Modele.__init__)


def test_data_modele_constructor_args():
    sig = inspect.signature(Data_Modele.__init__)
    params = list(sig.parameters.keys())



def test_data_declarationtype_is_not_abstract():
    assert not inspect.isabstract(Data_DeclarationType)


def test_data_declarationtype_constructor_exists():
    assert callable(Data_DeclarationType.__init__)


def test_data_declarationtype_constructor_args():
    sig = inspect.signature(Data_DeclarationType.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_data_declarationtype_has_nom():
    assert hasattr(Data_DeclarationType, "nom")
    descriptor = None
    for klass in Data_DeclarationType.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_data_attribut_is_not_abstract():
    assert not inspect.isabstract(Data_Attribut)


def test_data_attribut_constructor_exists():
    assert callable(Data_Attribut.__init__)


def test_data_attribut_constructor_args():
    sig = inspect.signature(Data_Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "estTableau" in params, "Missing parameter 'estTableau'"
    assert "typeStr" in params, "Missing parameter 'typeStr'"
    assert "nom" in params, "Missing parameter 'nom'"

def test_data_attribut_has_estTableau():
    assert hasattr(Data_Attribut, "estTableau")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "estTableau" in klass.__dict__:
            descriptor = klass.__dict__["estTableau"]
            break
    assert isinstance(descriptor, property)

def test_data_attribut_has_typeStr():
    assert hasattr(Data_Attribut, "typeStr")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "typeStr" in klass.__dict__:
            descriptor = klass.__dict__["typeStr"]
            break
    assert isinstance(descriptor, property)

def test_data_attribut_has_nom():
    assert hasattr(Data_Attribut, "nom")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_declarationtype_is_not_abstract():
    assert not inspect.isabstract(DeclarationType)


def test_declarationtype_constructor_exists():
    assert callable(DeclarationType.__init__)


def test_declarationtype_constructor_args():
    sig = inspect.signature(DeclarationType.__init__)
    params = list(sig.parameters.keys())



def test_data_classe_is_not_abstract():
    assert not inspect.isabstract(Data_Classe)


def test_data_classe_constructor_exists():
    assert callable(Data_Classe.__init__)


def test_data_classe_constructor_args():
    sig = inspect.signature(Data_Classe.__init__)
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
Data_Modele_strategy = st.builds(
    Data_Modele,
)
Data_DeclarationType_strategy = st.builds(
    Data_DeclarationType,
    nom=
        safe_text
)
Data_Attribut_strategy = st.builds(
    Data_Attribut,
    estTableau=
        st.booleans(),
    typeStr=
        safe_text,
    nom=
        safe_text
)
DeclarationType_strategy = st.builds(
    DeclarationType,
)
Data_Classe_strategy = st.builds(
    Data_Classe,
)

@given(instance=Data_Modele_strategy)
@settings(max_examples=50)
def test_data_modele_instantiation(instance):
    assert isinstance(instance, Data_Modele)

@given(instance=Data_DeclarationType_strategy)
@settings(max_examples=50)
def test_data_declarationtype_instantiation(instance):
    assert isinstance(instance, Data_DeclarationType)



@given(instance=Data_DeclarationType_strategy)
def test_data_declarationtype_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=Data_Attribut_strategy)
@settings(max_examples=50)
def test_data_attribut_instantiation(instance):
    assert isinstance(instance, Data_Attribut)



@given(instance=Data_Attribut_strategy)
def test_data_attribut_estTableau_setter(instance):
    original = instance.estTableau
    instance.estTableau = original
    assert instance.estTableau == original



@given(instance=Data_Attribut_strategy)
def test_data_attribut_typeStr_setter(instance):
    original = instance.typeStr
    instance.typeStr = original
    assert instance.typeStr == original



@given(instance=Data_Attribut_strategy)
def test_data_attribut_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=DeclarationType_strategy)
@settings(max_examples=50)
def test_declarationtype_instantiation(instance):
    assert isinstance(instance, DeclarationType)

@given(instance=Data_Classe_strategy)
@settings(max_examples=50)
def test_data_classe_instantiation(instance):
    assert isinstance(instance, Data_Classe)
