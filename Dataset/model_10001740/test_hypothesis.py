import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Cliente,
    Perro,
    Gato,
    Animal,
    ILocalizable_Interface,
    CoordenadaGPS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cliente_is_not_abstract():
    assert not inspect.isabstract(Cliente)


def test_cliente_constructor_exists():
    assert callable(Cliente.__init__)


def test_cliente_constructor_args():
    sig = inspect.signature(Cliente.__init__)
    params = list(sig.parameters.keys())
    assert "listaMascotas" in params, "Missing parameter 'listaMascotas'"
    assert "numeroDeCliente" in params, "Missing parameter 'numeroDeCliente'"
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_cliente_has_listaMascotas():
    assert hasattr(Cliente, "listaMascotas")
    descriptor = None
    for klass in Cliente.__mro__:
        if "listaMascotas" in klass.__dict__:
            descriptor = klass.__dict__["listaMascotas"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_numeroDeCliente():
    assert hasattr(Cliente, "numeroDeCliente")
    descriptor = None
    for klass in Cliente.__mro__:
        if "numeroDeCliente" in klass.__dict__:
            descriptor = klass.__dict__["numeroDeCliente"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_nombre():
    assert hasattr(Cliente, "nombre")
    descriptor = None
    for klass in Cliente.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_perro_is_not_abstract():
    assert not inspect.isabstract(Perro)


def test_perro_constructor_exists():
    assert callable(Perro.__init__)


def test_perro_constructor_args():
    sig = inspect.signature(Perro.__init__)
    params = list(sig.parameters.keys())
    assert "fechaCastracion" in params, "Missing parameter 'fechaCastracion'"

def test_perro_has_fechaCastracion():
    assert hasattr(Perro, "fechaCastracion")
    descriptor = None
    for klass in Perro.__mro__:
        if "fechaCastracion" in klass.__dict__:
            descriptor = klass.__dict__["fechaCastracion"]
            break
    assert isinstance(descriptor, property)



def test_gato_is_not_abstract():
    assert not inspect.isabstract(Gato)


def test_gato_constructor_exists():
    assert callable(Gato.__init__)


def test_gato_constructor_args():
    sig = inspect.signature(Gato.__init__)
    params = list(sig.parameters.keys())
    assert "ultimaDesparasitacion" in params, "Missing parameter 'ultimaDesparasitacion'"
    assert "MESES_ENTRE_DESPARASITACIONES" in params, "Missing parameter 'MESES_ENTRE_DESPARASITACIONES'"

def test_gato_has_ultimaDesparasitacion():
    assert hasattr(Gato, "ultimaDesparasitacion")
    descriptor = None
    for klass in Gato.__mro__:
        if "ultimaDesparasitacion" in klass.__dict__:
            descriptor = klass.__dict__["ultimaDesparasitacion"]
            break
    assert isinstance(descriptor, property)

def test_gato_has_MESES_ENTRE_DESPARASITACIONES():
    assert hasattr(Gato, "MESES_ENTRE_DESPARASITACIONES")
    descriptor = None
    for klass in Gato.__mro__:
        if "MESES_ENTRE_DESPARASITACIONES" in klass.__dict__:
            descriptor = klass.__dict__["MESES_ENTRE_DESPARASITACIONES"]
            break
    assert isinstance(descriptor, property)



def test_animal_is_not_abstract():
    assert not inspect.isabstract(Animal)


def test_animal_constructor_exists():
    assert callable(Animal.__init__)


def test_animal_constructor_args():
    sig = inspect.signature(Animal.__init__)
    params = list(sig.parameters.keys())
    assert "raza" in params, "Missing parameter 'raza'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "identificador" in params, "Missing parameter 'identificador'"

def test_animal_has_raza():
    assert hasattr(Animal, "raza")
    descriptor = None
    for klass in Animal.__mro__:
        if "raza" in klass.__dict__:
            descriptor = klass.__dict__["raza"]
            break
    assert isinstance(descriptor, property)

def test_animal_has_nombre():
    assert hasattr(Animal, "nombre")
    descriptor = None
    for klass in Animal.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_animal_has_identificador():
    assert hasattr(Animal, "identificador")
    descriptor = None
    for klass in Animal.__mro__:
        if "identificador" in klass.__dict__:
            descriptor = klass.__dict__["identificador"]
            break
    assert isinstance(descriptor, property)



def test_ilocalizable_interface_is_not_abstract():
    assert not inspect.isabstract(ILocalizable_Interface)


def test_ilocalizable_interface_constructor_exists():
    assert callable(ILocalizable_Interface.__init__)


def test_ilocalizable_interface_constructor_args():
    sig = inspect.signature(ILocalizable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_coordenadagps_is_not_abstract():
    assert not inspect.isabstract(CoordenadaGPS)


def test_coordenadagps_constructor_exists():
    assert callable(CoordenadaGPS.__init__)


def test_coordenadagps_constructor_args():
    sig = inspect.signature(CoordenadaGPS.__init__)
    params = list(sig.parameters.keys())
    assert "latitud" in params, "Missing parameter 'latitud'"
    assert "longitud" in params, "Missing parameter 'longitud'"

def test_coordenadagps_has_latitud():
    assert hasattr(CoordenadaGPS, "latitud")
    descriptor = None
    for klass in CoordenadaGPS.__mro__:
        if "latitud" in klass.__dict__:
            descriptor = klass.__dict__["latitud"]
            break
    assert isinstance(descriptor, property)

def test_coordenadagps_has_longitud():
    assert hasattr(CoordenadaGPS, "longitud")
    descriptor = None
    for klass in CoordenadaGPS.__mro__:
        if "longitud" in klass.__dict__:
            descriptor = klass.__dict__["longitud"]
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
Cliente_strategy = st.builds(
    Cliente,
    listaMascotas=
        safe_text,
    numeroDeCliente=
        safe_text,
    nombre=
        safe_text
)
Perro_strategy = st.builds(
    Perro,
    fechaCastracion=
        safe_text
)
Gato_strategy = st.builds(
    Gato,
    ultimaDesparasitacion=
        safe_text,
    MESES_ENTRE_DESPARASITACIONES=
        safe_text
)
Animal_strategy = st.builds(
    Animal,
    raza=
        safe_text,
    nombre=
        safe_text,
    identificador=
        safe_text
)
ILocalizable_Interface_strategy = st.builds(
    ILocalizable_Interface,
)
CoordenadaGPS_strategy = st.builds(
    CoordenadaGPS,
    latitud=
        safe_text,
    longitud=
        safe_text
)

@given(instance=Cliente_strategy)
@settings(max_examples=50)
def test_cliente_instantiation(instance):
    assert isinstance(instance, Cliente)



@given(instance=Cliente_strategy)
def test_cliente_listaMascotas_setter(instance):
    original = instance.listaMascotas
    instance.listaMascotas = original
    assert instance.listaMascotas == original



@given(instance=Cliente_strategy)
def test_cliente_numeroDeCliente_setter(instance):
    original = instance.numeroDeCliente
    instance.numeroDeCliente = original
    assert instance.numeroDeCliente == original



@given(instance=Cliente_strategy)
def test_cliente_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Perro_strategy)
@settings(max_examples=50)
def test_perro_instantiation(instance):
    assert isinstance(instance, Perro)



@given(instance=Perro_strategy)
def test_perro_fechaCastracion_setter(instance):
    original = instance.fechaCastracion
    instance.fechaCastracion = original
    assert instance.fechaCastracion == original

@given(instance=Gato_strategy)
@settings(max_examples=50)
def test_gato_instantiation(instance):
    assert isinstance(instance, Gato)



@given(instance=Gato_strategy)
def test_gato_ultimaDesparasitacion_setter(instance):
    original = instance.ultimaDesparasitacion
    instance.ultimaDesparasitacion = original
    assert instance.ultimaDesparasitacion == original



@given(instance=Gato_strategy)
def test_gato_MESES_ENTRE_DESPARASITACIONES_setter(instance):
    original = instance.MESES_ENTRE_DESPARASITACIONES
    instance.MESES_ENTRE_DESPARASITACIONES = original
    assert instance.MESES_ENTRE_DESPARASITACIONES == original

@given(instance=Animal_strategy)
@settings(max_examples=50)
def test_animal_instantiation(instance):
    assert isinstance(instance, Animal)



@given(instance=Animal_strategy)
def test_animal_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original



@given(instance=Animal_strategy)
def test_animal_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Animal_strategy)
def test_animal_identificador_setter(instance):
    original = instance.identificador
    instance.identificador = original
    assert instance.identificador == original

@given(instance=ILocalizable_Interface_strategy)
@settings(max_examples=50)
def test_ilocalizable_interface_instantiation(instance):
    assert isinstance(instance, ILocalizable_Interface)

@given(instance=CoordenadaGPS_strategy)
@settings(max_examples=50)
def test_coordenadagps_instantiation(instance):
    assert isinstance(instance, CoordenadaGPS)



@given(instance=CoordenadaGPS_strategy)
def test_coordenadagps_latitud_setter(instance):
    original = instance.latitud
    instance.latitud = original
    assert instance.latitud == original



@given(instance=CoordenadaGPS_strategy)
def test_coordenadagps_longitud_setter(instance):
    original = instance.longitud
    instance.longitud = original
    assert instance.longitud == original
