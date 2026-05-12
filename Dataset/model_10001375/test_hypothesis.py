import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Personas,
    Entrenador,
    Partido,
    Jugadores,
    Equipo,
    Liga,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_personas_is_not_abstract():
    assert not inspect.isabstract(Personas)


def test_personas_constructor_exists():
    assert callable(Personas.__init__)


def test_personas_constructor_args():
    sig = inspect.signature(Personas.__init__)
    params = list(sig.parameters.keys())
    assert "Direccion" in params, "Missing parameter 'Direccion'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"

def test_personas_has_Direccion():
    assert hasattr(Personas, "Direccion")
    descriptor = None
    for klass in Personas.__mro__:
        if "Direccion" in klass.__dict__:
            descriptor = klass.__dict__["Direccion"]
            break
    assert isinstance(descriptor, property)

def test_personas_has_Nombre():
    assert hasattr(Personas, "Nombre")
    descriptor = None
    for klass in Personas.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)



def test_entrenador_is_not_abstract():
    assert not inspect.isabstract(Entrenador)


def test_entrenador_constructor_exists():
    assert callable(Entrenador.__init__)


def test_entrenador_constructor_args():
    sig = inspect.signature(Entrenador.__init__)
    params = list(sig.parameters.keys())
    assert "a_os_de_experiencia" in params, "Missing parameter 'a_os_de_experiencia'"
    assert "nivel_de_acreditaci_n" in params, "Missing parameter 'nivel_de_acreditaci_n'"

def test_entrenador_has_a_os_de_experiencia():
    assert hasattr(Entrenador, "a_os_de_experiencia")
    descriptor = None
    for klass in Entrenador.__mro__:
        if "a_os_de_experiencia" in klass.__dict__:
            descriptor = klass.__dict__["a_os_de_experiencia"]
            break
    assert isinstance(descriptor, property)

def test_entrenador_has_nivel_de_acreditaci_n():
    assert hasattr(Entrenador, "nivel_de_acreditaci_n")
    descriptor = None
    for klass in Entrenador.__mro__:
        if "nivel_de_acreditaci_n" in klass.__dict__:
            descriptor = klass.__dict__["nivel_de_acreditaci_n"]
            break
    assert isinstance(descriptor, property)



def test_partido_is_not_abstract():
    assert not inspect.isabstract(Partido)


def test_partido_constructor_exists():
    assert callable(Partido.__init__)


def test_partido_constructor_args():
    sig = inspect.signature(Partido.__init__)
    params = list(sig.parameters.keys())
    assert "localizaci_n" in params, "Missing parameter 'localizaci_n'"
    assert "resultado" in params, "Missing parameter 'resultado'"

def test_partido_has_localizaci_n():
    assert hasattr(Partido, "localizaci_n")
    descriptor = None
    for klass in Partido.__mro__:
        if "localizaci_n" in klass.__dict__:
            descriptor = klass.__dict__["localizaci_n"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_resultado():
    assert hasattr(Partido, "resultado")
    descriptor = None
    for klass in Partido.__mro__:
        if "resultado" in klass.__dict__:
            descriptor = klass.__dict__["resultado"]
            break
    assert isinstance(descriptor, property)



def test_jugadores_is_not_abstract():
    assert not inspect.isabstract(Jugadores)


def test_jugadores_constructor_exists():
    assert callable(Jugadores.__init__)


def test_jugadores_constructor_args():
    sig = inspect.signature(Jugadores.__init__)
    params = list(sig.parameters.keys())
    assert "posicion" in params, "Missing parameter 'posicion'"
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_jugadores_has_posicion():
    assert hasattr(Jugadores, "posicion")
    descriptor = None
    for klass in Jugadores.__mro__:
        if "posicion" in klass.__dict__:
            descriptor = klass.__dict__["posicion"]
            break
    assert isinstance(descriptor, property)

def test_jugadores_has_nombre():
    assert hasattr(Jugadores, "nombre")
    descriptor = None
    for klass in Jugadores.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_equipo_is_not_abstract():
    assert not inspect.isabstract(Equipo)


def test_equipo_constructor_exists():
    assert callable(Equipo.__init__)


def test_equipo_constructor_args():
    sig = inspect.signature(Equipo.__init__)
    params = list(sig.parameters.keys())
    assert "registro" in params, "Missing parameter 'registro'"
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_equipo_has_registro():
    assert hasattr(Equipo, "registro")
    descriptor = None
    for klass in Equipo.__mro__:
        if "registro" in klass.__dict__:
            descriptor = klass.__dict__["registro"]
            break
    assert isinstance(descriptor, property)

def test_equipo_has_nombre():
    assert hasattr(Equipo, "nombre")
    descriptor = None
    for klass in Equipo.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_liga_is_not_abstract():
    assert not inspect.isabstract(Liga)


def test_liga_constructor_exists():
    assert callable(Liga.__init__)


def test_liga_constructor_args():
    sig = inspect.signature(Liga.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "datos_finalizaci_n" in params, "Missing parameter 'datos_finalizaci_n'"
    assert "datos_comienzo" in params, "Missing parameter 'datos_comienzo'"

def test_liga_has_nombre():
    assert hasattr(Liga, "nombre")
    descriptor = None
    for klass in Liga.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_liga_has_datos_finalizaci_n():
    assert hasattr(Liga, "datos_finalizaci_n")
    descriptor = None
    for klass in Liga.__mro__:
        if "datos_finalizaci_n" in klass.__dict__:
            descriptor = klass.__dict__["datos_finalizaci_n"]
            break
    assert isinstance(descriptor, property)

def test_liga_has_datos_comienzo():
    assert hasattr(Liga, "datos_comienzo")
    descriptor = None
    for klass in Liga.__mro__:
        if "datos_comienzo" in klass.__dict__:
            descriptor = klass.__dict__["datos_comienzo"]
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
Personas_strategy = st.builds(
    Personas,
    Direccion=
        safe_text,
    Nombre=
        safe_text
)
Entrenador_strategy = st.builds(
    Entrenador,
    a_os_de_experiencia=
        st.integers(),
    nivel_de_acreditaci_n=
        safe_text
)
Partido_strategy = st.builds(
    Partido,
    localizaci_n=
        safe_text,
    resultado=
        st.integers()
)
Jugadores_strategy = st.builds(
    Jugadores,
    posicion=
        st.integers(),
    nombre=
        safe_text
)
Equipo_strategy = st.builds(
    Equipo,
    registro=
        safe_text,
    nombre=
        safe_text
)
Liga_strategy = st.builds(
    Liga,
    nombre=
        safe_text,
    datos_finalizaci_n=
        safe_text,
    datos_comienzo=
        safe_text
)

@given(instance=Personas_strategy)
@settings(max_examples=50)
def test_personas_instantiation(instance):
    assert isinstance(instance, Personas)



@given(instance=Personas_strategy)
def test_personas_Direccion_setter(instance):
    original = instance.Direccion
    instance.Direccion = original
    assert instance.Direccion == original



@given(instance=Personas_strategy)
def test_personas_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original

@given(instance=Entrenador_strategy)
@settings(max_examples=50)
def test_entrenador_instantiation(instance):
    assert isinstance(instance, Entrenador)



@given(instance=Entrenador_strategy)
def test_entrenador_a_os_de_experiencia_setter(instance):
    original = instance.a_os_de_experiencia
    instance.a_os_de_experiencia = original
    assert instance.a_os_de_experiencia == original



@given(instance=Entrenador_strategy)
def test_entrenador_nivel_de_acreditaci_n_setter(instance):
    original = instance.nivel_de_acreditaci_n
    instance.nivel_de_acreditaci_n = original
    assert instance.nivel_de_acreditaci_n == original

@given(instance=Partido_strategy)
@settings(max_examples=50)
def test_partido_instantiation(instance):
    assert isinstance(instance, Partido)



@given(instance=Partido_strategy)
def test_partido_localizaci_n_setter(instance):
    original = instance.localizaci_n
    instance.localizaci_n = original
    assert instance.localizaci_n == original



@given(instance=Partido_strategy)
def test_partido_resultado_setter(instance):
    original = instance.resultado
    instance.resultado = original
    assert instance.resultado == original

@given(instance=Jugadores_strategy)
@settings(max_examples=50)
def test_jugadores_instantiation(instance):
    assert isinstance(instance, Jugadores)



@given(instance=Jugadores_strategy)
def test_jugadores_posicion_setter(instance):
    original = instance.posicion
    instance.posicion = original
    assert instance.posicion == original



@given(instance=Jugadores_strategy)
def test_jugadores_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Equipo_strategy)
@settings(max_examples=50)
def test_equipo_instantiation(instance):
    assert isinstance(instance, Equipo)



@given(instance=Equipo_strategy)
def test_equipo_registro_setter(instance):
    original = instance.registro
    instance.registro = original
    assert instance.registro == original



@given(instance=Equipo_strategy)
def test_equipo_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Liga_strategy)
@settings(max_examples=50)
def test_liga_instantiation(instance):
    assert isinstance(instance, Liga)



@given(instance=Liga_strategy)
def test_liga_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Liga_strategy)
def test_liga_datos_finalizaci_n_setter(instance):
    original = instance.datos_finalizaci_n
    instance.datos_finalizaci_n = original
    assert instance.datos_finalizaci_n == original



@given(instance=Liga_strategy)
def test_liga_datos_comienzo_setter(instance):
    original = instance.datos_comienzo
    instance.datos_comienzo = original
    assert instance.datos_comienzo == original
