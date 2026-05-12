import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Jugador,
    Equipo,
    Marcador,
    Partido,
    Fecha,
    Premio,
    Torneo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jugador_is_not_abstract():
    assert not inspect.isabstract(Jugador)


def test_jugador_constructor_exists():
    assert callable(Jugador.__init__)


def test_jugador_constructor_args():
    sig = inspect.signature(Jugador.__init__)
    params = list(sig.parameters.keys())
    assert "nif" in params, "Missing parameter 'nif'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "apellidos" in params, "Missing parameter 'apellidos'"
    assert "telefono" in params, "Missing parameter 'telefono'"

def test_jugador_has_nif():
    assert hasattr(Jugador, "nif")
    descriptor = None
    for klass in Jugador.__mro__:
        if "nif" in klass.__dict__:
            descriptor = klass.__dict__["nif"]
            break
    assert isinstance(descriptor, property)

def test_jugador_has_nombre():
    assert hasattr(Jugador, "nombre")
    descriptor = None
    for klass in Jugador.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_jugador_has_apellidos():
    assert hasattr(Jugador, "apellidos")
    descriptor = None
    for klass in Jugador.__mro__:
        if "apellidos" in klass.__dict__:
            descriptor = klass.__dict__["apellidos"]
            break
    assert isinstance(descriptor, property)

def test_jugador_has_telefono():
    assert hasattr(Jugador, "telefono")
    descriptor = None
    for klass in Jugador.__mro__:
        if "telefono" in klass.__dict__:
            descriptor = klass.__dict__["telefono"]
            break
    assert isinstance(descriptor, property)



def test_equipo_is_not_abstract():
    assert not inspect.isabstract(Equipo)


def test_equipo_constructor_exists():
    assert callable(Equipo.__init__)


def test_equipo_constructor_args():
    sig = inspect.signature(Equipo.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_equipo_has_nombre():
    assert hasattr(Equipo, "nombre")
    descriptor = None
    for klass in Equipo.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_marcador_is_not_abstract():
    assert not inspect.isabstract(Marcador)


def test_marcador_constructor_exists():
    assert callable(Marcador.__init__)


def test_marcador_constructor_args():
    sig = inspect.signature(Marcador.__init__)
    params = list(sig.parameters.keys())
    assert "equipo2" in params, "Missing parameter 'equipo2'"
    assert "tiempoSet" in params, "Missing parameter 'tiempoSet'"
    assert "equipo1" in params, "Missing parameter 'equipo1'"

def test_marcador_has_equipo2():
    assert hasattr(Marcador, "equipo2")
    descriptor = None
    for klass in Marcador.__mro__:
        if "equipo2" in klass.__dict__:
            descriptor = klass.__dict__["equipo2"]
            break
    assert isinstance(descriptor, property)

def test_marcador_has_tiempoSet():
    assert hasattr(Marcador, "tiempoSet")
    descriptor = None
    for klass in Marcador.__mro__:
        if "tiempoSet" in klass.__dict__:
            descriptor = klass.__dict__["tiempoSet"]
            break
    assert isinstance(descriptor, property)

def test_marcador_has_equipo1():
    assert hasattr(Marcador, "equipo1")
    descriptor = None
    for klass in Marcador.__mro__:
        if "equipo1" in klass.__dict__:
            descriptor = klass.__dict__["equipo1"]
            break
    assert isinstance(descriptor, property)



def test_partido_is_not_abstract():
    assert not inspect.isabstract(Partido)


def test_partido_constructor_exists():
    assert callable(Partido.__init__)


def test_partido_constructor_args():
    sig = inspect.signature(Partido.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "ronda" in params, "Missing parameter 'ronda'"

def test_partido_has_id():
    assert hasattr(Partido, "id")
    descriptor = None
    for klass in Partido.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_ronda():
    assert hasattr(Partido, "ronda")
    descriptor = None
    for klass in Partido.__mro__:
        if "ronda" in klass.__dict__:
            descriptor = klass.__dict__["ronda"]
            break
    assert isinstance(descriptor, property)



def test_fecha_is_not_abstract():
    assert not inspect.isabstract(Fecha)


def test_fecha_constructor_exists():
    assert callable(Fecha.__init__)


def test_fecha_constructor_args():
    sig = inspect.signature(Fecha.__init__)
    params = list(sig.parameters.keys())
    assert "anio" in params, "Missing parameter 'anio'"
    assert "dia" in params, "Missing parameter 'dia'"
    assert "mes" in params, "Missing parameter 'mes'"

def test_fecha_has_anio():
    assert hasattr(Fecha, "anio")
    descriptor = None
    for klass in Fecha.__mro__:
        if "anio" in klass.__dict__:
            descriptor = klass.__dict__["anio"]
            break
    assert isinstance(descriptor, property)

def test_fecha_has_dia():
    assert hasattr(Fecha, "dia")
    descriptor = None
    for klass in Fecha.__mro__:
        if "dia" in klass.__dict__:
            descriptor = klass.__dict__["dia"]
            break
    assert isinstance(descriptor, property)

def test_fecha_has_mes():
    assert hasattr(Fecha, "mes")
    descriptor = None
    for klass in Fecha.__mro__:
        if "mes" in klass.__dict__:
            descriptor = klass.__dict__["mes"]
            break
    assert isinstance(descriptor, property)



def test_premio_is_not_abstract():
    assert not inspect.isabstract(Premio)


def test_premio_constructor_exists():
    assert callable(Premio.__init__)


def test_premio_constructor_args():
    sig = inspect.signature(Premio.__init__)
    params = list(sig.parameters.keys())
    assert "Puesto" in params, "Missing parameter 'Puesto'"
    assert "Puntos" in params, "Missing parameter 'Puntos'"
    assert "Dinero" in params, "Missing parameter 'Dinero'"

def test_premio_has_Puesto():
    assert hasattr(Premio, "Puesto")
    descriptor = None
    for klass in Premio.__mro__:
        if "Puesto" in klass.__dict__:
            descriptor = klass.__dict__["Puesto"]
            break
    assert isinstance(descriptor, property)

def test_premio_has_Puntos():
    assert hasattr(Premio, "Puntos")
    descriptor = None
    for klass in Premio.__mro__:
        if "Puntos" in klass.__dict__:
            descriptor = klass.__dict__["Puntos"]
            break
    assert isinstance(descriptor, property)

def test_premio_has_Dinero():
    assert hasattr(Premio, "Dinero")
    descriptor = None
    for klass in Premio.__mro__:
        if "Dinero" in klass.__dict__:
            descriptor = klass.__dict__["Dinero"]
            break
    assert isinstance(descriptor, property)



def test_torneo_is_not_abstract():
    assert not inspect.isabstract(Torneo)


def test_torneo_constructor_exists():
    assert callable(Torneo.__init__)


def test_torneo_constructor_args():
    sig = inspect.signature(Torneo.__init__)
    params = list(sig.parameters.keys())
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "Pais" in params, "Missing parameter 'Pais'"

def test_torneo_has_Nombre():
    assert hasattr(Torneo, "Nombre")
    descriptor = None
    for klass in Torneo.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)

def test_torneo_has_Pais():
    assert hasattr(Torneo, "Pais")
    descriptor = None
    for klass in Torneo.__mro__:
        if "Pais" in klass.__dict__:
            descriptor = klass.__dict__["Pais"]
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
Jugador_strategy = st.builds(
    Jugador,
    nif=
        safe_text,
    nombre=
        safe_text,
    apellidos=
        safe_text,
    telefono=
        st.integers()
)
Equipo_strategy = st.builds(
    Equipo,
    nombre=
        safe_text
)
Marcador_strategy = st.builds(
    Marcador,
    equipo2=
        st.integers(),
    tiempoSet=
        st.integers(),
    equipo1=
        st.integers()
)
Partido_strategy = st.builds(
    Partido,
    id=
        st.integers(),
    ronda=
        safe_text
)
Fecha_strategy = st.builds(
    Fecha,
    anio=
        st.integers(),
    dia=
        st.integers(),
    mes=
        st.integers()
)
Premio_strategy = st.builds(
    Premio,
    Puesto=
        st.integers(),
    Puntos=
        st.integers(),
    Dinero=
        st.integers()
)
Torneo_strategy = st.builds(
    Torneo,
    Nombre=
        safe_text,
    Pais=
        safe_text
)

@given(instance=Jugador_strategy)
@settings(max_examples=50)
def test_jugador_instantiation(instance):
    assert isinstance(instance, Jugador)



@given(instance=Jugador_strategy)
def test_jugador_nif_setter(instance):
    original = instance.nif
    instance.nif = original
    assert instance.nif == original



@given(instance=Jugador_strategy)
def test_jugador_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Jugador_strategy)
def test_jugador_apellidos_setter(instance):
    original = instance.apellidos
    instance.apellidos = original
    assert instance.apellidos == original



@given(instance=Jugador_strategy)
def test_jugador_telefono_setter(instance):
    original = instance.telefono
    instance.telefono = original
    assert instance.telefono == original

@given(instance=Equipo_strategy)
@settings(max_examples=50)
def test_equipo_instantiation(instance):
    assert isinstance(instance, Equipo)



@given(instance=Equipo_strategy)
def test_equipo_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Marcador_strategy)
@settings(max_examples=50)
def test_marcador_instantiation(instance):
    assert isinstance(instance, Marcador)



@given(instance=Marcador_strategy)
def test_marcador_equipo2_setter(instance):
    original = instance.equipo2
    instance.equipo2 = original
    assert instance.equipo2 == original



@given(instance=Marcador_strategy)
def test_marcador_tiempoSet_setter(instance):
    original = instance.tiempoSet
    instance.tiempoSet = original
    assert instance.tiempoSet == original



@given(instance=Marcador_strategy)
def test_marcador_equipo1_setter(instance):
    original = instance.equipo1
    instance.equipo1 = original
    assert instance.equipo1 == original

@given(instance=Partido_strategy)
@settings(max_examples=50)
def test_partido_instantiation(instance):
    assert isinstance(instance, Partido)



@given(instance=Partido_strategy)
def test_partido_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Partido_strategy)
def test_partido_ronda_setter(instance):
    original = instance.ronda
    instance.ronda = original
    assert instance.ronda == original

@given(instance=Fecha_strategy)
@settings(max_examples=50)
def test_fecha_instantiation(instance):
    assert isinstance(instance, Fecha)



@given(instance=Fecha_strategy)
def test_fecha_anio_setter(instance):
    original = instance.anio
    instance.anio = original
    assert instance.anio == original



@given(instance=Fecha_strategy)
def test_fecha_dia_setter(instance):
    original = instance.dia
    instance.dia = original
    assert instance.dia == original



@given(instance=Fecha_strategy)
def test_fecha_mes_setter(instance):
    original = instance.mes
    instance.mes = original
    assert instance.mes == original

@given(instance=Premio_strategy)
@settings(max_examples=50)
def test_premio_instantiation(instance):
    assert isinstance(instance, Premio)



@given(instance=Premio_strategy)
def test_premio_Puesto_setter(instance):
    original = instance.Puesto
    instance.Puesto = original
    assert instance.Puesto == original



@given(instance=Premio_strategy)
def test_premio_Puntos_setter(instance):
    original = instance.Puntos
    instance.Puntos = original
    assert instance.Puntos == original



@given(instance=Premio_strategy)
def test_premio_Dinero_setter(instance):
    original = instance.Dinero
    instance.Dinero = original
    assert instance.Dinero == original

@given(instance=Torneo_strategy)
@settings(max_examples=50)
def test_torneo_instantiation(instance):
    assert isinstance(instance, Torneo)



@given(instance=Torneo_strategy)
def test_torneo_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=Torneo_strategy)
def test_torneo_Pais_setter(instance):
    original = instance.Pais
    instance.Pais = original
    assert instance.Pais == original
