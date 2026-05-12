import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Selects_Operando,
    Selects_Join,
    Selects_Where,
    Selects_From,
    Selects_Select,
    NamedElement,
    Selects_Tabla,
    Selects_Fichero,
    Selects_Aplicacion,
    Selects_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_selects_operando_is_not_abstract():
    assert not inspect.isabstract(Selects_Operando)


def test_selects_operando_constructor_exists():
    assert callable(Selects_Operando.__init__)


def test_selects_operando_constructor_args():
    sig = inspect.signature(Selects_Operando.__init__)
    params = list(sig.parameters.keys())
    assert "columna" in params, "Missing parameter 'columna'"
    assert "tabla" in params, "Missing parameter 'tabla'"

def test_selects_operando_has_columna():
    assert hasattr(Selects_Operando, "columna")
    descriptor = None
    for klass in Selects_Operando.__mro__:
        if "columna" in klass.__dict__:
            descriptor = klass.__dict__["columna"]
            break
    assert isinstance(descriptor, property)

def test_selects_operando_has_tabla():
    assert hasattr(Selects_Operando, "tabla")
    descriptor = None
    for klass in Selects_Operando.__mro__:
        if "tabla" in klass.__dict__:
            descriptor = klass.__dict__["tabla"]
            break
    assert isinstance(descriptor, property)



def test_selects_join_is_not_abstract():
    assert not inspect.isabstract(Selects_Join)


def test_selects_join_constructor_exists():
    assert callable(Selects_Join.__init__)


def test_selects_join_constructor_args():
    sig = inspect.signature(Selects_Join.__init__)
    params = list(sig.parameters.keys())



def test_selects_where_is_not_abstract():
    assert not inspect.isabstract(Selects_Where)


def test_selects_where_constructor_exists():
    assert callable(Selects_Where.__init__)


def test_selects_where_constructor_args():
    sig = inspect.signature(Selects_Where.__init__)
    params = list(sig.parameters.keys())



def test_selects_from_is_not_abstract():
    assert not inspect.isabstract(Selects_From)


def test_selects_from_constructor_exists():
    assert callable(Selects_From.__init__)


def test_selects_from_constructor_args():
    sig = inspect.signature(Selects_From.__init__)
    params = list(sig.parameters.keys())



def test_selects_select_is_not_abstract():
    assert not inspect.isabstract(Selects_Select)


def test_selects_select_constructor_exists():
    assert callable(Selects_Select.__init__)


def test_selects_select_constructor_args():
    sig = inspect.signature(Selects_Select.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_selects_tabla_is_not_abstract():
    assert not inspect.isabstract(Selects_Tabla)


def test_selects_tabla_constructor_exists():
    assert callable(Selects_Tabla.__init__)


def test_selects_tabla_constructor_args():
    sig = inspect.signature(Selects_Tabla.__init__)
    params = list(sig.parameters.keys())
    assert "tabAlias" in params, "Missing parameter 'tabAlias'"

def test_selects_tabla_has_tabAlias():
    assert hasattr(Selects_Tabla, "tabAlias")
    descriptor = None
    for klass in Selects_Tabla.__mro__:
        if "tabAlias" in klass.__dict__:
            descriptor = klass.__dict__["tabAlias"]
            break
    assert isinstance(descriptor, property)



def test_selects_fichero_is_not_abstract():
    assert not inspect.isabstract(Selects_Fichero)


def test_selects_fichero_constructor_exists():
    assert callable(Selects_Fichero.__init__)


def test_selects_fichero_constructor_args():
    sig = inspect.signature(Selects_Fichero.__init__)
    params = list(sig.parameters.keys())



def test_selects_aplicacion_is_not_abstract():
    assert not inspect.isabstract(Selects_Aplicacion)


def test_selects_aplicacion_constructor_exists():
    assert callable(Selects_Aplicacion.__init__)


def test_selects_aplicacion_constructor_args():
    sig = inspect.signature(Selects_Aplicacion.__init__)
    params = list(sig.parameters.keys())



def test_selects_namedelement_is_not_abstract():
    assert not inspect.isabstract(Selects_NamedElement)


def test_selects_namedelement_constructor_exists():
    assert callable(Selects_NamedElement.__init__)


def test_selects_namedelement_constructor_args():
    sig = inspect.signature(Selects_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_selects_namedelement_has_nombre():
    assert hasattr(Selects_NamedElement, "nombre")
    descriptor = None
    for klass in Selects_NamedElement.__mro__:
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
Selects_Operando_strategy = st.builds(
    Selects_Operando,
    columna=
        safe_text,
    tabla=
        safe_text
)
Selects_Join_strategy = st.builds(
    Selects_Join,
)
Selects_Where_strategy = st.builds(
    Selects_Where,
)
Selects_From_strategy = st.builds(
    Selects_From,
)
Selects_Select_strategy = st.builds(
    Selects_Select,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Selects_Tabla_strategy = st.builds(
    Selects_Tabla,
    tabAlias=
        safe_text
)
Selects_Fichero_strategy = st.builds(
    Selects_Fichero,
)
Selects_Aplicacion_strategy = st.builds(
    Selects_Aplicacion,
)
Selects_NamedElement_strategy = st.builds(
    Selects_NamedElement,
    nombre=
        safe_text
)

@given(instance=Selects_Operando_strategy)
@settings(max_examples=50)
def test_selects_operando_instantiation(instance):
    assert isinstance(instance, Selects_Operando)



@given(instance=Selects_Operando_strategy)
def test_selects_operando_columna_setter(instance):
    original = instance.columna
    instance.columna = original
    assert instance.columna == original



@given(instance=Selects_Operando_strategy)
def test_selects_operando_tabla_setter(instance):
    original = instance.tabla
    instance.tabla = original
    assert instance.tabla == original

@given(instance=Selects_Join_strategy)
@settings(max_examples=50)
def test_selects_join_instantiation(instance):
    assert isinstance(instance, Selects_Join)

@given(instance=Selects_Where_strategy)
@settings(max_examples=50)
def test_selects_where_instantiation(instance):
    assert isinstance(instance, Selects_Where)

@given(instance=Selects_From_strategy)
@settings(max_examples=50)
def test_selects_from_instantiation(instance):
    assert isinstance(instance, Selects_From)

@given(instance=Selects_Select_strategy)
@settings(max_examples=50)
def test_selects_select_instantiation(instance):
    assert isinstance(instance, Selects_Select)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Selects_Tabla_strategy)
@settings(max_examples=50)
def test_selects_tabla_instantiation(instance):
    assert isinstance(instance, Selects_Tabla)



@given(instance=Selects_Tabla_strategy)
def test_selects_tabla_tabAlias_setter(instance):
    original = instance.tabAlias
    instance.tabAlias = original
    assert instance.tabAlias == original

@given(instance=Selects_Fichero_strategy)
@settings(max_examples=50)
def test_selects_fichero_instantiation(instance):
    assert isinstance(instance, Selects_Fichero)

@given(instance=Selects_Aplicacion_strategy)
@settings(max_examples=50)
def test_selects_aplicacion_instantiation(instance):
    assert isinstance(instance, Selects_Aplicacion)

@given(instance=Selects_NamedElement_strategy)
@settings(max_examples=50)
def test_selects_namedelement_instantiation(instance):
    assert isinstance(instance, Selects_NamedElement)



@given(instance=Selects_NamedElement_strategy)
def test_selects_namedelement_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original
