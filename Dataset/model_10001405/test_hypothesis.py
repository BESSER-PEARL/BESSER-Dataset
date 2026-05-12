import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mundo_Ratite,
    mundo_Tinamues,
    mundo_Neoaves,
    mundo_Galloanserae,
    mundo_Paleognato,
    mundo_Neognato,
    mundo_Neornithe,
    mundo_Ave,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mundo_ratite_is_not_abstract():
    assert not inspect.isabstract(mundo_Ratite)


def test_mundo_ratite_constructor_exists():
    assert callable(mundo_Ratite.__init__)


def test_mundo_ratite_constructor_args():
    sig = inspect.signature(mundo_Ratite.__init__)
    params = list(sig.parameters.keys())
    assert "quilla" in params, "Missing parameter 'quilla'"

def test_mundo_ratite_has_quilla():
    assert hasattr(mundo_Ratite, "quilla")
    descriptor = None
    for klass in mundo_Ratite.__mro__:
        if "quilla" in klass.__dict__:
            descriptor = klass.__dict__["quilla"]
            break
    assert isinstance(descriptor, property)



def test_mundo_tinamues_is_not_abstract():
    assert not inspect.isabstract(mundo_Tinamues)


def test_mundo_tinamues_constructor_exists():
    assert callable(mundo_Tinamues.__init__)


def test_mundo_tinamues_constructor_args():
    sig = inspect.signature(mundo_Tinamues.__init__)
    params = list(sig.parameters.keys())
    assert "velocidadTierra" in params, "Missing parameter 'velocidadTierra'"

def test_mundo_tinamues_has_velocidadTierra():
    assert hasattr(mundo_Tinamues, "velocidadTierra")
    descriptor = None
    for klass in mundo_Tinamues.__mro__:
        if "velocidadTierra" in klass.__dict__:
            descriptor = klass.__dict__["velocidadTierra"]
            break
    assert isinstance(descriptor, property)



def test_mundo_neoaves_is_not_abstract():
    assert not inspect.isabstract(mundo_Neoaves)


def test_mundo_neoaves_constructor_exists():
    assert callable(mundo_Neoaves.__init__)


def test_mundo_neoaves_constructor_args():
    sig = inspect.signature(mundo_Neoaves.__init__)
    params = list(sig.parameters.keys())
    assert "longitudPatas" in params, "Missing parameter 'longitudPatas'"
    assert "numeroDedosPatas" in params, "Missing parameter 'numeroDedosPatas'"

def test_mundo_neoaves_has_longitudPatas():
    assert hasattr(mundo_Neoaves, "longitudPatas")
    descriptor = None
    for klass in mundo_Neoaves.__mro__:
        if "longitudPatas" in klass.__dict__:
            descriptor = klass.__dict__["longitudPatas"]
            break
    assert isinstance(descriptor, property)

def test_mundo_neoaves_has_numeroDedosPatas():
    assert hasattr(mundo_Neoaves, "numeroDedosPatas")
    descriptor = None
    for klass in mundo_Neoaves.__mro__:
        if "numeroDedosPatas" in klass.__dict__:
            descriptor = klass.__dict__["numeroDedosPatas"]
            break
    assert isinstance(descriptor, property)



def test_mundo_galloanserae_is_not_abstract():
    assert not inspect.isabstract(mundo_Galloanserae)


def test_mundo_galloanserae_constructor_exists():
    assert callable(mundo_Galloanserae.__init__)


def test_mundo_galloanserae_constructor_args():
    sig = inspect.signature(mundo_Galloanserae.__init__)
    params = list(sig.parameters.keys())
    assert "CAZA" in params, "Missing parameter 'CAZA'"
    assert "reproduccion" in params, "Missing parameter 'reproduccion'"
    assert "POLIGAMA" in params, "Missing parameter 'POLIGAMA'"
    assert "tipo" in params, "Missing parameter 'tipo'"
    assert "MONOGAMA" in params, "Missing parameter 'MONOGAMA'"
    assert "DOMESTICA" in params, "Missing parameter 'DOMESTICA'"

def test_mundo_galloanserae_has_CAZA():
    assert hasattr(mundo_Galloanserae, "CAZA")
    descriptor = None
    for klass in mundo_Galloanserae.__mro__:
        if "CAZA" in klass.__dict__:
            descriptor = klass.__dict__["CAZA"]
            break
    assert isinstance(descriptor, property)

def test_mundo_galloanserae_has_reproduccion():
    assert hasattr(mundo_Galloanserae, "reproduccion")
    descriptor = None
    for klass in mundo_Galloanserae.__mro__:
        if "reproduccion" in klass.__dict__:
            descriptor = klass.__dict__["reproduccion"]
            break
    assert isinstance(descriptor, property)

def test_mundo_galloanserae_has_POLIGAMA():
    assert hasattr(mundo_Galloanserae, "POLIGAMA")
    descriptor = None
    for klass in mundo_Galloanserae.__mro__:
        if "POLIGAMA" in klass.__dict__:
            descriptor = klass.__dict__["POLIGAMA"]
            break
    assert isinstance(descriptor, property)

def test_mundo_galloanserae_has_tipo():
    assert hasattr(mundo_Galloanserae, "tipo")
    descriptor = None
    for klass in mundo_Galloanserae.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)

def test_mundo_galloanserae_has_MONOGAMA():
    assert hasattr(mundo_Galloanserae, "MONOGAMA")
    descriptor = None
    for klass in mundo_Galloanserae.__mro__:
        if "MONOGAMA" in klass.__dict__:
            descriptor = klass.__dict__["MONOGAMA"]
            break
    assert isinstance(descriptor, property)

def test_mundo_galloanserae_has_DOMESTICA():
    assert hasattr(mundo_Galloanserae, "DOMESTICA")
    descriptor = None
    for klass in mundo_Galloanserae.__mro__:
        if "DOMESTICA" in klass.__dict__:
            descriptor = klass.__dict__["DOMESTICA"]
            break
    assert isinstance(descriptor, property)



def test_mundo_paleognato_is_not_abstract():
    assert not inspect.isabstract(mundo_Paleognato)


def test_mundo_paleognato_constructor_exists():
    assert callable(mundo_Paleognato.__init__)


def test_mundo_paleognato_constructor_args():
    sig = inspect.signature(mundo_Paleognato.__init__)
    params = list(sig.parameters.keys())
    assert "numeroHuesosPaladar" in params, "Missing parameter 'numeroHuesosPaladar'"

def test_mundo_paleognato_has_numeroHuesosPaladar():
    assert hasattr(mundo_Paleognato, "numeroHuesosPaladar")
    descriptor = None
    for klass in mundo_Paleognato.__mro__:
        if "numeroHuesosPaladar" in klass.__dict__:
            descriptor = klass.__dict__["numeroHuesosPaladar"]
            break
    assert isinstance(descriptor, property)



def test_mundo_neognato_is_not_abstract():
    assert not inspect.isabstract(mundo_Neognato)


def test_mundo_neognato_constructor_exists():
    assert callable(mundo_Neognato.__init__)


def test_mundo_neognato_constructor_args():
    sig = inspect.signature(mundo_Neognato.__init__)
    params = list(sig.parameters.keys())
    assert "numeroHuesosPata" in params, "Missing parameter 'numeroHuesosPata'"
    assert "longitudTercerDedo" in params, "Missing parameter 'longitudTercerDedo'"

def test_mundo_neognato_has_numeroHuesosPata():
    assert hasattr(mundo_Neognato, "numeroHuesosPata")
    descriptor = None
    for klass in mundo_Neognato.__mro__:
        if "numeroHuesosPata" in klass.__dict__:
            descriptor = klass.__dict__["numeroHuesosPata"]
            break
    assert isinstance(descriptor, property)

def test_mundo_neognato_has_longitudTercerDedo():
    assert hasattr(mundo_Neognato, "longitudTercerDedo")
    descriptor = None
    for klass in mundo_Neognato.__mro__:
        if "longitudTercerDedo" in klass.__dict__:
            descriptor = klass.__dict__["longitudTercerDedo"]
            break
    assert isinstance(descriptor, property)



def test_mundo_neornithe_is_not_abstract():
    assert not inspect.isabstract(mundo_Neornithe)


def test_mundo_neornithe_constructor_exists():
    assert callable(mundo_Neornithe.__init__)


def test_mundo_neornithe_constructor_args():
    sig = inspect.signature(mundo_Neornithe.__init__)
    params = list(sig.parameters.keys())
    assert "rangoMetabolico" in params, "Missing parameter 'rangoMetabolico'"
    assert "longitudCola" in params, "Missing parameter 'longitudCola'"
    assert "ALTO" in params, "Missing parameter 'ALTO'"
    assert "BAJO" in params, "Missing parameter 'BAJO'"
    assert "MEDIO" in params, "Missing parameter 'MEDIO'"
    assert "densidadOsea" in params, "Missing parameter 'densidadOsea'"

def test_mundo_neornithe_has_rangoMetabolico():
    assert hasattr(mundo_Neornithe, "rangoMetabolico")
    descriptor = None
    for klass in mundo_Neornithe.__mro__:
        if "rangoMetabolico" in klass.__dict__:
            descriptor = klass.__dict__["rangoMetabolico"]
            break
    assert isinstance(descriptor, property)

def test_mundo_neornithe_has_longitudCola():
    assert hasattr(mundo_Neornithe, "longitudCola")
    descriptor = None
    for klass in mundo_Neornithe.__mro__:
        if "longitudCola" in klass.__dict__:
            descriptor = klass.__dict__["longitudCola"]
            break
    assert isinstance(descriptor, property)

def test_mundo_neornithe_has_ALTO():
    assert hasattr(mundo_Neornithe, "ALTO")
    descriptor = None
    for klass in mundo_Neornithe.__mro__:
        if "ALTO" in klass.__dict__:
            descriptor = klass.__dict__["ALTO"]
            break
    assert isinstance(descriptor, property)

def test_mundo_neornithe_has_BAJO():
    assert hasattr(mundo_Neornithe, "BAJO")
    descriptor = None
    for klass in mundo_Neornithe.__mro__:
        if "BAJO" in klass.__dict__:
            descriptor = klass.__dict__["BAJO"]
            break
    assert isinstance(descriptor, property)

def test_mundo_neornithe_has_MEDIO():
    assert hasattr(mundo_Neornithe, "MEDIO")
    descriptor = None
    for klass in mundo_Neornithe.__mro__:
        if "MEDIO" in klass.__dict__:
            descriptor = klass.__dict__["MEDIO"]
            break
    assert isinstance(descriptor, property)

def test_mundo_neornithe_has_densidadOsea():
    assert hasattr(mundo_Neornithe, "densidadOsea")
    descriptor = None
    for klass in mundo_Neornithe.__mro__:
        if "densidadOsea" in klass.__dict__:
            descriptor = klass.__dict__["densidadOsea"]
            break
    assert isinstance(descriptor, property)



def test_mundo_ave_is_not_abstract():
    assert not inspect.isabstract(mundo_Ave)


def test_mundo_ave_constructor_exists():
    assert callable(mundo_Ave.__init__)


def test_mundo_ave_constructor_args():
    sig = inspect.signature(mundo_Ave.__init__)
    params = list(sig.parameters.keys())
    assert "altura" in params, "Missing parameter 'altura'"
    assert "color" in params, "Missing parameter 'color'"
    assert "factorPeso" in params, "Missing parameter 'factorPeso'"

def test_mundo_ave_has_altura():
    assert hasattr(mundo_Ave, "altura")
    descriptor = None
    for klass in mundo_Ave.__mro__:
        if "altura" in klass.__dict__:
            descriptor = klass.__dict__["altura"]
            break
    assert isinstance(descriptor, property)

def test_mundo_ave_has_color():
    assert hasattr(mundo_Ave, "color")
    descriptor = None
    for klass in mundo_Ave.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_mundo_ave_has_factorPeso():
    assert hasattr(mundo_Ave, "factorPeso")
    descriptor = None
    for klass in mundo_Ave.__mro__:
        if "factorPeso" in klass.__dict__:
            descriptor = klass.__dict__["factorPeso"]
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
mundo_Ratite_strategy = st.builds(
    mundo_Ratite,
    quilla=
        st.booleans()
)
mundo_Tinamues_strategy = st.builds(
    mundo_Tinamues,
    velocidadTierra=
        safe_text
)
mundo_Neoaves_strategy = st.builds(
    mundo_Neoaves,
    longitudPatas=
        safe_text,
    numeroDedosPatas=
        safe_text
)
mundo_Galloanserae_strategy = st.builds(
    mundo_Galloanserae,
    CAZA=
        safe_text,
    reproduccion=
        safe_text,
    POLIGAMA=
        safe_text,
    tipo=
        safe_text,
    MONOGAMA=
        safe_text,
    DOMESTICA=
        safe_text
)
mundo_Paleognato_strategy = st.builds(
    mundo_Paleognato,
    numeroHuesosPaladar=
        safe_text
)
mundo_Neognato_strategy = st.builds(
    mundo_Neognato,
    numeroHuesosPata=
        safe_text,
    longitudTercerDedo=
        safe_text
)
mundo_Neornithe_strategy = st.builds(
    mundo_Neornithe,
    rangoMetabolico=
        safe_text,
    longitudCola=
        safe_text,
    ALTO=
        safe_text,
    BAJO=
        safe_text,
    MEDIO=
        safe_text,
    densidadOsea=
        safe_text
)
mundo_Ave_strategy = st.builds(
    mundo_Ave,
    altura=
        safe_text,
    color=
        safe_text,
    factorPeso=
        safe_text
)

@given(instance=mundo_Ratite_strategy)
@settings(max_examples=50)
def test_mundo_ratite_instantiation(instance):
    assert isinstance(instance, mundo_Ratite)



@given(instance=mundo_Ratite_strategy)
def test_mundo_ratite_quilla_setter(instance):
    original = instance.quilla
    instance.quilla = original
    assert instance.quilla == original

@given(instance=mundo_Tinamues_strategy)
@settings(max_examples=50)
def test_mundo_tinamues_instantiation(instance):
    assert isinstance(instance, mundo_Tinamues)



@given(instance=mundo_Tinamues_strategy)
def test_mundo_tinamues_velocidadTierra_setter(instance):
    original = instance.velocidadTierra
    instance.velocidadTierra = original
    assert instance.velocidadTierra == original

@given(instance=mundo_Neoaves_strategy)
@settings(max_examples=50)
def test_mundo_neoaves_instantiation(instance):
    assert isinstance(instance, mundo_Neoaves)



@given(instance=mundo_Neoaves_strategy)
def test_mundo_neoaves_longitudPatas_setter(instance):
    original = instance.longitudPatas
    instance.longitudPatas = original
    assert instance.longitudPatas == original



@given(instance=mundo_Neoaves_strategy)
def test_mundo_neoaves_numeroDedosPatas_setter(instance):
    original = instance.numeroDedosPatas
    instance.numeroDedosPatas = original
    assert instance.numeroDedosPatas == original

@given(instance=mundo_Galloanserae_strategy)
@settings(max_examples=50)
def test_mundo_galloanserae_instantiation(instance):
    assert isinstance(instance, mundo_Galloanserae)



@given(instance=mundo_Galloanserae_strategy)
def test_mundo_galloanserae_CAZA_setter(instance):
    original = instance.CAZA
    instance.CAZA = original
    assert instance.CAZA == original



@given(instance=mundo_Galloanserae_strategy)
def test_mundo_galloanserae_reproduccion_setter(instance):
    original = instance.reproduccion
    instance.reproduccion = original
    assert instance.reproduccion == original



@given(instance=mundo_Galloanserae_strategy)
def test_mundo_galloanserae_POLIGAMA_setter(instance):
    original = instance.POLIGAMA
    instance.POLIGAMA = original
    assert instance.POLIGAMA == original



@given(instance=mundo_Galloanserae_strategy)
def test_mundo_galloanserae_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original



@given(instance=mundo_Galloanserae_strategy)
def test_mundo_galloanserae_MONOGAMA_setter(instance):
    original = instance.MONOGAMA
    instance.MONOGAMA = original
    assert instance.MONOGAMA == original



@given(instance=mundo_Galloanserae_strategy)
def test_mundo_galloanserae_DOMESTICA_setter(instance):
    original = instance.DOMESTICA
    instance.DOMESTICA = original
    assert instance.DOMESTICA == original

@given(instance=mundo_Paleognato_strategy)
@settings(max_examples=50)
def test_mundo_paleognato_instantiation(instance):
    assert isinstance(instance, mundo_Paleognato)



@given(instance=mundo_Paleognato_strategy)
def test_mundo_paleognato_numeroHuesosPaladar_setter(instance):
    original = instance.numeroHuesosPaladar
    instance.numeroHuesosPaladar = original
    assert instance.numeroHuesosPaladar == original

@given(instance=mundo_Neognato_strategy)
@settings(max_examples=50)
def test_mundo_neognato_instantiation(instance):
    assert isinstance(instance, mundo_Neognato)



@given(instance=mundo_Neognato_strategy)
def test_mundo_neognato_numeroHuesosPata_setter(instance):
    original = instance.numeroHuesosPata
    instance.numeroHuesosPata = original
    assert instance.numeroHuesosPata == original



@given(instance=mundo_Neognato_strategy)
def test_mundo_neognato_longitudTercerDedo_setter(instance):
    original = instance.longitudTercerDedo
    instance.longitudTercerDedo = original
    assert instance.longitudTercerDedo == original

@given(instance=mundo_Neornithe_strategy)
@settings(max_examples=50)
def test_mundo_neornithe_instantiation(instance):
    assert isinstance(instance, mundo_Neornithe)



@given(instance=mundo_Neornithe_strategy)
def test_mundo_neornithe_rangoMetabolico_setter(instance):
    original = instance.rangoMetabolico
    instance.rangoMetabolico = original
    assert instance.rangoMetabolico == original



@given(instance=mundo_Neornithe_strategy)
def test_mundo_neornithe_longitudCola_setter(instance):
    original = instance.longitudCola
    instance.longitudCola = original
    assert instance.longitudCola == original



@given(instance=mundo_Neornithe_strategy)
def test_mundo_neornithe_ALTO_setter(instance):
    original = instance.ALTO
    instance.ALTO = original
    assert instance.ALTO == original



@given(instance=mundo_Neornithe_strategy)
def test_mundo_neornithe_BAJO_setter(instance):
    original = instance.BAJO
    instance.BAJO = original
    assert instance.BAJO == original



@given(instance=mundo_Neornithe_strategy)
def test_mundo_neornithe_MEDIO_setter(instance):
    original = instance.MEDIO
    instance.MEDIO = original
    assert instance.MEDIO == original



@given(instance=mundo_Neornithe_strategy)
def test_mundo_neornithe_densidadOsea_setter(instance):
    original = instance.densidadOsea
    instance.densidadOsea = original
    assert instance.densidadOsea == original

@given(instance=mundo_Ave_strategy)
@settings(max_examples=50)
def test_mundo_ave_instantiation(instance):
    assert isinstance(instance, mundo_Ave)



@given(instance=mundo_Ave_strategy)
def test_mundo_ave_altura_setter(instance):
    original = instance.altura
    instance.altura = original
    assert instance.altura == original



@given(instance=mundo_Ave_strategy)
def test_mundo_ave_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=mundo_Ave_strategy)
def test_mundo_ave_factorPeso_setter(instance):
    original = instance.factorPeso
    instance.factorPeso = original
    assert instance.factorPeso == original
