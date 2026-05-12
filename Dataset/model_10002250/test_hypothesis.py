import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Zdravstveni_karton,
    Pregled,
    Lekar,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_zdravstveni_karton_is_not_abstract():
    assert not inspect.isabstract(Zdravstveni_karton)


def test_zdravstveni_karton_constructor_exists():
    assert callable(Zdravstveni_karton.__init__)


def test_zdravstveni_karton_constructor_args():
    sig = inspect.signature(Zdravstveni_karton.__init__)
    params = list(sig.parameters.keys())
    assert "BrKart" in params, "Missing parameter 'BrKart'"

def test_zdravstveni_karton_has_BrKart():
    assert hasattr(Zdravstveni_karton, "BrKart")
    descriptor = None
    for klass in Zdravstveni_karton.__mro__:
        if "BrKart" in klass.__dict__:
            descriptor = klass.__dict__["BrKart"]
            break
    assert isinstance(descriptor, property)



def test_pregled_is_not_abstract():
    assert not inspect.isabstract(Pregled)


def test_pregled_constructor_exists():
    assert callable(Pregled.__init__)


def test_pregled_constructor_args():
    sig = inspect.signature(Pregled.__init__)
    params = list(sig.parameters.keys())
    assert "DatumP" in params, "Missing parameter 'DatumP'"
    assert "BrPregled" in params, "Missing parameter 'BrPregled'"

def test_pregled_has_DatumP():
    assert hasattr(Pregled, "DatumP")
    descriptor = None
    for klass in Pregled.__mro__:
        if "DatumP" in klass.__dict__:
            descriptor = klass.__dict__["DatumP"]
            break
    assert isinstance(descriptor, property)

def test_pregled_has_BrPregled():
    assert hasattr(Pregled, "BrPregled")
    descriptor = None
    for klass in Pregled.__mro__:
        if "BrPregled" in klass.__dict__:
            descriptor = klass.__dict__["BrPregled"]
            break
    assert isinstance(descriptor, property)



def test_lekar_is_not_abstract():
    assert not inspect.isabstract(Lekar)


def test_lekar_constructor_exists():
    assert callable(Lekar.__init__)


def test_lekar_constructor_args():
    sig = inspect.signature(Lekar.__init__)
    params = list(sig.parameters.keys())
    assert "ImeZap" in params, "Missing parameter 'ImeZap'"
    assert "AdrZap" in params, "Missing parameter 'AdrZap'"
    assert "DatZavSk" in params, "Missing parameter 'DatZavSk'"
    assert "PrzZap" in params, "Missing parameter 'PrzZap'"
    assert "RadStaz" in params, "Missing parameter 'RadStaz'"
    assert "Zaposleni_ID" in params, "Missing parameter 'Zaposleni_ID'"
    assert "Fakultet" in params, "Missing parameter 'Fakultet'"
    assert "BrTelZap" in params, "Missing parameter 'BrTelZap'"

def test_lekar_has_ImeZap():
    assert hasattr(Lekar, "ImeZap")
    descriptor = None
    for klass in Lekar.__mro__:
        if "ImeZap" in klass.__dict__:
            descriptor = klass.__dict__["ImeZap"]
            break
    assert isinstance(descriptor, property)

def test_lekar_has_AdrZap():
    assert hasattr(Lekar, "AdrZap")
    descriptor = None
    for klass in Lekar.__mro__:
        if "AdrZap" in klass.__dict__:
            descriptor = klass.__dict__["AdrZap"]
            break
    assert isinstance(descriptor, property)

def test_lekar_has_DatZavSk():
    assert hasattr(Lekar, "DatZavSk")
    descriptor = None
    for klass in Lekar.__mro__:
        if "DatZavSk" in klass.__dict__:
            descriptor = klass.__dict__["DatZavSk"]
            break
    assert isinstance(descriptor, property)

def test_lekar_has_PrzZap():
    assert hasattr(Lekar, "PrzZap")
    descriptor = None
    for klass in Lekar.__mro__:
        if "PrzZap" in klass.__dict__:
            descriptor = klass.__dict__["PrzZap"]
            break
    assert isinstance(descriptor, property)

def test_lekar_has_RadStaz():
    assert hasattr(Lekar, "RadStaz")
    descriptor = None
    for klass in Lekar.__mro__:
        if "RadStaz" in klass.__dict__:
            descriptor = klass.__dict__["RadStaz"]
            break
    assert isinstance(descriptor, property)

def test_lekar_has_Zaposleni_ID():
    assert hasattr(Lekar, "Zaposleni_ID")
    descriptor = None
    for klass in Lekar.__mro__:
        if "Zaposleni_ID" in klass.__dict__:
            descriptor = klass.__dict__["Zaposleni_ID"]
            break
    assert isinstance(descriptor, property)

def test_lekar_has_Fakultet():
    assert hasattr(Lekar, "Fakultet")
    descriptor = None
    for klass in Lekar.__mro__:
        if "Fakultet" in klass.__dict__:
            descriptor = klass.__dict__["Fakultet"]
            break
    assert isinstance(descriptor, property)

def test_lekar_has_BrTelZap():
    assert hasattr(Lekar, "BrTelZap")
    descriptor = None
    for klass in Lekar.__mro__:
        if "BrTelZap" in klass.__dict__:
            descriptor = klass.__dict__["BrTelZap"]
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
Zdravstveni_karton_strategy = st.builds(
    Zdravstveni_karton,
    BrKart=
        st.integers()
)
Pregled_strategy = st.builds(
    Pregled,
    DatumP=
        safe_text,
    BrPregled=
        st.integers()
)
Lekar_strategy = st.builds(
    Lekar,
    ImeZap=
        safe_text,
    AdrZap=
        safe_text,
    DatZavSk=
        safe_text,
    PrzZap=
        safe_text,
    RadStaz=
        st.integers(),
    Zaposleni_ID=
        safe_text,
    Fakultet=
        safe_text,
    BrTelZap=
        safe_text
)

@given(instance=Zdravstveni_karton_strategy)
@settings(max_examples=50)
def test_zdravstveni_karton_instantiation(instance):
    assert isinstance(instance, Zdravstveni_karton)



@given(instance=Zdravstveni_karton_strategy)
def test_zdravstveni_karton_BrKart_setter(instance):
    original = instance.BrKart
    instance.BrKart = original
    assert instance.BrKart == original

@given(instance=Pregled_strategy)
@settings(max_examples=50)
def test_pregled_instantiation(instance):
    assert isinstance(instance, Pregled)



@given(instance=Pregled_strategy)
def test_pregled_DatumP_setter(instance):
    original = instance.DatumP
    instance.DatumP = original
    assert instance.DatumP == original



@given(instance=Pregled_strategy)
def test_pregled_BrPregled_setter(instance):
    original = instance.BrPregled
    instance.BrPregled = original
    assert instance.BrPregled == original

@given(instance=Lekar_strategy)
@settings(max_examples=50)
def test_lekar_instantiation(instance):
    assert isinstance(instance, Lekar)



@given(instance=Lekar_strategy)
def test_lekar_ImeZap_setter(instance):
    original = instance.ImeZap
    instance.ImeZap = original
    assert instance.ImeZap == original



@given(instance=Lekar_strategy)
def test_lekar_AdrZap_setter(instance):
    original = instance.AdrZap
    instance.AdrZap = original
    assert instance.AdrZap == original



@given(instance=Lekar_strategy)
def test_lekar_DatZavSk_setter(instance):
    original = instance.DatZavSk
    instance.DatZavSk = original
    assert instance.DatZavSk == original



@given(instance=Lekar_strategy)
def test_lekar_PrzZap_setter(instance):
    original = instance.PrzZap
    instance.PrzZap = original
    assert instance.PrzZap == original



@given(instance=Lekar_strategy)
def test_lekar_RadStaz_setter(instance):
    original = instance.RadStaz
    instance.RadStaz = original
    assert instance.RadStaz == original



@given(instance=Lekar_strategy)
def test_lekar_Zaposleni_ID_setter(instance):
    original = instance.Zaposleni_ID
    instance.Zaposleni_ID = original
    assert instance.Zaposleni_ID == original



@given(instance=Lekar_strategy)
def test_lekar_Fakultet_setter(instance):
    original = instance.Fakultet
    instance.Fakultet = original
    assert instance.Fakultet == original



@given(instance=Lekar_strategy)
def test_lekar_BrTelZap_setter(instance):
    original = instance.BrTelZap
    instance.BrTelZap = original
    assert instance.BrTelZap == original
