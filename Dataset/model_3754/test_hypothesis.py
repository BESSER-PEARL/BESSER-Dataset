import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BD::Columna,
    BD::Tabla,
    BD::EsquemaBD,
    TipoPrimitivo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bd::columna_is_not_abstract():
    assert not inspect.isabstract(BD::Columna)


def test_bd::columna_constructor_exists():
    assert callable(BD::Columna.__init__)


def test_bd::columna_constructor_args():
    sig = inspect.signature(BD::Columna.__init__)
    params = list(sig.parameters.keys())
    assert "tipo" in params, "Missing parameter 'tipo'"
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_bd::columna_has_tipo():
    assert hasattr(BD::Columna, "tipo")
    descriptor = None
    for klass in BD::Columna.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)

def test_bd::columna_has_nombre():
    assert hasattr(BD::Columna, "nombre")
    descriptor = None
    for klass in BD::Columna.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_bd::tabla_is_not_abstract():
    assert not inspect.isabstract(BD::Tabla)


def test_bd::tabla_constructor_exists():
    assert callable(BD::Tabla.__init__)


def test_bd::tabla_constructor_args():
    sig = inspect.signature(BD::Tabla.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_bd::tabla_has_nombre():
    assert hasattr(BD::Tabla, "nombre")
    descriptor = None
    for klass in BD::Tabla.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_bd::esquemabd_is_not_abstract():
    assert not inspect.isabstract(BD::EsquemaBD)


def test_bd::esquemabd_constructor_exists():
    assert callable(BD::EsquemaBD.__init__)


def test_bd::esquemabd_constructor_args():
    sig = inspect.signature(BD::EsquemaBD.__init__)
    params = list(sig.parameters.keys())

def test_tipoprimitivo_exists():
    # Check that the Enumeration exists
    assert TipoPrimitivo is not None

def test_tipoprimitivo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TipoPrimitivo]
    expected_literals = [
        "Double",
        "Date",
        "String",
        "Integer",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TipoPrimitivo"


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
BD::Columna_strategy = st.builds(
    BD::Columna,
    tipo=
        safe_text,
    nombre=
        safe_text
)
BD::Tabla_strategy = st.builds(
    BD::Tabla,
    nombre=
        safe_text
)
BD::EsquemaBD_strategy = st.builds(
    BD::EsquemaBD,
)

@given(instance=BD::Columna_strategy)
@settings(max_examples=50)
def test_bd::columna_instantiation(instance):
    assert isinstance(instance, BD::Columna)

@given(instance=BD::Columna_strategy)
def test_bd::columna_tipo_type(instance):
    assert isinstance(instance.tipo, str)


@given(instance=BD::Columna_strategy)
def test_bd::columna_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original

@given(instance=BD::Columna_strategy)
def test_bd::columna_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=BD::Columna_strategy)
def test_bd::columna_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=BD::Tabla_strategy)
@settings(max_examples=50)
def test_bd::tabla_instantiation(instance):
    assert isinstance(instance, BD::Tabla)

@given(instance=BD::Tabla_strategy)
def test_bd::tabla_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=BD::Tabla_strategy)
def test_bd::tabla_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=BD::EsquemaBD_strategy)
@settings(max_examples=50)
def test_bd::esquemabd_instantiation(instance):
    assert isinstance(instance, BD::EsquemaBD)
