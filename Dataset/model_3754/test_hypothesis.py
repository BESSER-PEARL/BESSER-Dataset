import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BD_Columna,
    BD_Tabla,
    BD_EsquemaBD,
    TipoPrimitivo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bd_columna_is_not_abstract():
    assert not inspect.isabstract(BD_Columna)


def test_bd_columna_constructor_exists():
    assert callable(BD_Columna.__init__)


def test_bd_columna_constructor_args():
    sig = inspect.signature(BD_Columna.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "tipo" in params, "Missing parameter 'tipo'"

def test_bd_columna_has_nombre():
    assert hasattr(BD_Columna, "nombre")
    descriptor = None
    for klass in BD_Columna.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_bd_columna_has_tipo():
    assert hasattr(BD_Columna, "tipo")
    descriptor = None
    for klass in BD_Columna.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)



def test_bd_tabla_is_not_abstract():
    assert not inspect.isabstract(BD_Tabla)


def test_bd_tabla_constructor_exists():
    assert callable(BD_Tabla.__init__)


def test_bd_tabla_constructor_args():
    sig = inspect.signature(BD_Tabla.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_bd_tabla_has_nombre():
    assert hasattr(BD_Tabla, "nombre")
    descriptor = None
    for klass in BD_Tabla.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_bd_esquemabd_is_not_abstract():
    assert not inspect.isabstract(BD_EsquemaBD)


def test_bd_esquemabd_constructor_exists():
    assert callable(BD_EsquemaBD.__init__)


def test_bd_esquemabd_constructor_args():
    sig = inspect.signature(BD_EsquemaBD.__init__)
    params = list(sig.parameters.keys())

def test_tipoprimitivo_exists():
    # Check that the Enumeration exists
    assert TipoPrimitivo is not None

def test_tipoprimitivo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TipoPrimitivo]
    expected_literals = [
        "Integer",
        "Double",
        "Boolean",
        "String",
        "Date",
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
BD_Columna_strategy = st.builds(
    BD_Columna,
    nombre=
        safe_text,
    tipo=
        safe_text
)
BD_Tabla_strategy = st.builds(
    BD_Tabla,
    nombre=
        safe_text
)
BD_EsquemaBD_strategy = st.builds(
    BD_EsquemaBD,
)

@given(instance=BD_Columna_strategy)
@settings(max_examples=50)
def test_bd_columna_instantiation(instance):
    assert isinstance(instance, BD_Columna)



@given(instance=BD_Columna_strategy)
def test_bd_columna_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=BD_Columna_strategy)
def test_bd_columna_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original

@given(instance=BD_Tabla_strategy)
@settings(max_examples=50)
def test_bd_tabla_instantiation(instance):
    assert isinstance(instance, BD_Tabla)



@given(instance=BD_Tabla_strategy)
def test_bd_tabla_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=BD_EsquemaBD_strategy)
@settings(max_examples=50)
def test_bd_esquemabd_instantiation(instance):
    assert isinstance(instance, BD_EsquemaBD)
