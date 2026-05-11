import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Selects::Operando,
    Selects::Join,
    Selects::Where,
    Selects::From,
    Selects::Select,
    NamedElement,
    Selects::Tabla,
    Selects::Fichero,
    Selects::Aplicacion,
    Selects::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_selects::operando_is_not_abstract():
    assert not inspect.isabstract(Selects::Operando)


def test_selects::operando_constructor_exists():
    assert callable(Selects::Operando.__init__)


def test_selects::operando_constructor_args():
    sig = inspect.signature(Selects::Operando.__init__)
    params = list(sig.parameters.keys())
    assert "columna" in params, "Missing parameter 'columna'"
    assert "tabla" in params, "Missing parameter 'tabla'"

def test_selects::operando_has_columna():
    assert hasattr(Selects::Operando, "columna")
    descriptor = None
    for klass in Selects::Operando.__mro__:
        if "columna" in klass.__dict__:
            descriptor = klass.__dict__["columna"]
            break
    assert isinstance(descriptor, property)

def test_selects::operando_has_tabla():
    assert hasattr(Selects::Operando, "tabla")
    descriptor = None
    for klass in Selects::Operando.__mro__:
        if "tabla" in klass.__dict__:
            descriptor = klass.__dict__["tabla"]
            break
    assert isinstance(descriptor, property)



def test_selects::join_is_not_abstract():
    assert not inspect.isabstract(Selects::Join)


def test_selects::join_constructor_exists():
    assert callable(Selects::Join.__init__)


def test_selects::join_constructor_args():
    sig = inspect.signature(Selects::Join.__init__)
    params = list(sig.parameters.keys())



def test_selects::where_is_not_abstract():
    assert not inspect.isabstract(Selects::Where)


def test_selects::where_constructor_exists():
    assert callable(Selects::Where.__init__)


def test_selects::where_constructor_args():
    sig = inspect.signature(Selects::Where.__init__)
    params = list(sig.parameters.keys())



def test_selects::from_is_not_abstract():
    assert not inspect.isabstract(Selects::From)


def test_selects::from_constructor_exists():
    assert callable(Selects::From.__init__)


def test_selects::from_constructor_args():
    sig = inspect.signature(Selects::From.__init__)
    params = list(sig.parameters.keys())



def test_selects::select_is_not_abstract():
    assert not inspect.isabstract(Selects::Select)


def test_selects::select_constructor_exists():
    assert callable(Selects::Select.__init__)


def test_selects::select_constructor_args():
    sig = inspect.signature(Selects::Select.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_selects::tabla_is_not_abstract():
    assert not inspect.isabstract(Selects::Tabla)


def test_selects::tabla_constructor_exists():
    assert callable(Selects::Tabla.__init__)


def test_selects::tabla_constructor_args():
    sig = inspect.signature(Selects::Tabla.__init__)
    params = list(sig.parameters.keys())
    assert "tabAlias" in params, "Missing parameter 'tabAlias'"

def test_selects::tabla_has_tabAlias():
    assert hasattr(Selects::Tabla, "tabAlias")
    descriptor = None
    for klass in Selects::Tabla.__mro__:
        if "tabAlias" in klass.__dict__:
            descriptor = klass.__dict__["tabAlias"]
            break
    assert isinstance(descriptor, property)



def test_selects::fichero_is_not_abstract():
    assert not inspect.isabstract(Selects::Fichero)


def test_selects::fichero_constructor_exists():
    assert callable(Selects::Fichero.__init__)


def test_selects::fichero_constructor_args():
    sig = inspect.signature(Selects::Fichero.__init__)
    params = list(sig.parameters.keys())



def test_selects::aplicacion_is_not_abstract():
    assert not inspect.isabstract(Selects::Aplicacion)


def test_selects::aplicacion_constructor_exists():
    assert callable(Selects::Aplicacion.__init__)


def test_selects::aplicacion_constructor_args():
    sig = inspect.signature(Selects::Aplicacion.__init__)
    params = list(sig.parameters.keys())



def test_selects::namedelement_is_not_abstract():
    assert not inspect.isabstract(Selects::NamedElement)


def test_selects::namedelement_constructor_exists():
    assert callable(Selects::NamedElement.__init__)


def test_selects::namedelement_constructor_args():
    sig = inspect.signature(Selects::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_selects::namedelement_has_nombre():
    assert hasattr(Selects::NamedElement, "nombre")
    descriptor = None
    for klass in Selects::NamedElement.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
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
Selects::Operando_strategy = st.builds(
    Selects::Operando,
    columna=
        safe_text,
    tabla=
        safe_text
)
Selects::Join_strategy = st.builds(
    Selects::Join,
)
Selects::Where_strategy = st.builds(
    Selects::Where,
)
Selects::From_strategy = st.builds(
    Selects::From,
)
Selects::Select_strategy = st.builds(
    Selects::Select,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Selects::Tabla_strategy = st.builds(
    Selects::Tabla,
    tabAlias=
        safe_text
)
Selects::Fichero_strategy = st.builds(
    Selects::Fichero,
)
Selects::Aplicacion_strategy = st.builds(
    Selects::Aplicacion,
)
Selects::NamedElement_strategy = st.builds(
    Selects::NamedElement,
    nombre=
        safe_text
)

@given(instance=Selects::Operando_strategy)
@settings(max_examples=50)
def test_selects::operando_instantiation(instance):
    assert isinstance(instance, Selects::Operando)

@given(instance=Selects::Operando_strategy)
def test_selects::operando_columna_type(instance):
    assert isinstance(instance.columna, str)


@given(instance=Selects::Operando_strategy)
def test_selects::operando_columna_setter(instance):
    original = instance.columna
    instance.columna = original
    assert instance.columna == original

@given(instance=Selects::Operando_strategy)
def test_selects::operando_tabla_type(instance):
    assert isinstance(instance.tabla, str)


@given(instance=Selects::Operando_strategy)
def test_selects::operando_tabla_setter(instance):
    original = instance.tabla
    instance.tabla = original
    assert instance.tabla == original

@given(instance=Selects::Join_strategy)
@settings(max_examples=50)
def test_selects::join_instantiation(instance):
    assert isinstance(instance, Selects::Join)

@given(instance=Selects::Where_strategy)
@settings(max_examples=50)
def test_selects::where_instantiation(instance):
    assert isinstance(instance, Selects::Where)

@given(instance=Selects::From_strategy)
@settings(max_examples=50)
def test_selects::from_instantiation(instance):
    assert isinstance(instance, Selects::From)

@given(instance=Selects::Select_strategy)
@settings(max_examples=50)
def test_selects::select_instantiation(instance):
    assert isinstance(instance, Selects::Select)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Selects::Tabla_strategy)
@settings(max_examples=50)
def test_selects::tabla_instantiation(instance):
    assert isinstance(instance, Selects::Tabla)

@given(instance=Selects::Tabla_strategy)
def test_selects::tabla_tabAlias_type(instance):
    assert isinstance(instance.tabAlias, str)


@given(instance=Selects::Tabla_strategy)
def test_selects::tabla_tabAlias_setter(instance):
    original = instance.tabAlias
    instance.tabAlias = original
    assert instance.tabAlias == original

@given(instance=Selects::Fichero_strategy)
@settings(max_examples=50)
def test_selects::fichero_instantiation(instance):
    assert isinstance(instance, Selects::Fichero)

@given(instance=Selects::Aplicacion_strategy)
@settings(max_examples=50)
def test_selects::aplicacion_instantiation(instance):
    assert isinstance(instance, Selects::Aplicacion)

@given(instance=Selects::NamedElement_strategy)
@settings(max_examples=50)
def test_selects::namedelement_instantiation(instance):
    assert isinstance(instance, Selects::NamedElement)

@given(instance=Selects::NamedElement_strategy)
def test_selects::namedelement_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=Selects::NamedElement_strategy)
def test_selects::namedelement_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original
