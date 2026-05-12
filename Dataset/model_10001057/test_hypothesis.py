import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    Foto,
    Telefono,
    Direccion,
    Contacto,
    Agenda,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_foto_is_not_abstract():
    assert not inspect.isabstract(Foto)


def test_foto_constructor_exists():
    assert callable(Foto.__init__)


def test_foto_constructor_args():
    sig = inspect.signature(Foto.__init__)
    params = list(sig.parameters.keys())
    assert "alto" in params, "Missing parameter 'alto'"
    assert "ancho" in params, "Missing parameter 'ancho'"

def test_foto_has_alto():
    assert hasattr(Foto, "alto")
    descriptor = None
    for klass in Foto.__mro__:
        if "alto" in klass.__dict__:
            descriptor = klass.__dict__["alto"]
            break
    assert isinstance(descriptor, property)

def test_foto_has_ancho():
    assert hasattr(Foto, "ancho")
    descriptor = None
    for klass in Foto.__mro__:
        if "ancho" in klass.__dict__:
            descriptor = klass.__dict__["ancho"]
            break
    assert isinstance(descriptor, property)



def test_telefono_is_not_abstract():
    assert not inspect.isabstract(Telefono)


def test_telefono_constructor_exists():
    assert callable(Telefono.__init__)


def test_telefono_constructor_args():
    sig = inspect.signature(Telefono.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"
    assert "numero" in params, "Missing parameter 'numero'"
    assert "prefijo" in params, "Missing parameter 'prefijo'"

def test_telefono_has_codigo():
    assert hasattr(Telefono, "codigo")
    descriptor = None
    for klass in Telefono.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)

def test_telefono_has_numero():
    assert hasattr(Telefono, "numero")
    descriptor = None
    for klass in Telefono.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)

def test_telefono_has_prefijo():
    assert hasattr(Telefono, "prefijo")
    descriptor = None
    for klass in Telefono.__mro__:
        if "prefijo" in klass.__dict__:
            descriptor = klass.__dict__["prefijo"]
            break
    assert isinstance(descriptor, property)



def test_direccion_is_not_abstract():
    assert not inspect.isabstract(Direccion)


def test_direccion_constructor_exists():
    assert callable(Direccion.__init__)


def test_direccion_constructor_args():
    sig = inspect.signature(Direccion.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"
    assert "pais" in params, "Missing parameter 'pais'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "ciudad" in params, "Missing parameter 'ciudad'"

def test_direccion_has_codigo():
    assert hasattr(Direccion, "codigo")
    descriptor = None
    for klass in Direccion.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_pais():
    assert hasattr(Direccion, "pais")
    descriptor = None
    for klass in Direccion.__mro__:
        if "pais" in klass.__dict__:
            descriptor = klass.__dict__["pais"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_nombre():
    assert hasattr(Direccion, "nombre")
    descriptor = None
    for klass in Direccion.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_ciudad():
    assert hasattr(Direccion, "ciudad")
    descriptor = None
    for klass in Direccion.__mro__:
        if "ciudad" in klass.__dict__:
            descriptor = klass.__dict__["ciudad"]
            break
    assert isinstance(descriptor, property)



def test_contacto_is_not_abstract():
    assert not inspect.isabstract(Contacto)


def test_contacto_constructor_exists():
    assert callable(Contacto.__init__)


def test_contacto_constructor_args():
    sig = inspect.signature(Contacto.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "email" in params, "Missing parameter 'email'"

def test_contacto_has_nombre():
    assert hasattr(Contacto, "nombre")
    descriptor = None
    for klass in Contacto.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_contacto_has_email():
    assert hasattr(Contacto, "email")
    descriptor = None
    for klass in Contacto.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_agenda_is_not_abstract():
    assert not inspect.isabstract(Agenda)


def test_agenda_constructor_exists():
    assert callable(Agenda.__init__)


def test_agenda_constructor_args():
    sig = inspect.signature(Agenda.__init__)
    params = list(sig.parameters.keys())
    assert "Introduccion" in params, "Missing parameter 'Introduccion'"

def test_agenda_has_Introduccion():
    assert hasattr(Agenda, "Introduccion")
    descriptor = None
    for klass in Agenda.__mro__:
        if "Introduccion" in klass.__dict__:
            descriptor = klass.__dict__["Introduccion"]
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
Foto_strategy = st.builds(
    Foto,
    alto=
        st.integers(),
    ancho=
        st.integers()
)
Telefono_strategy = st.builds(
    Telefono,
    codigo=
        st.integers(),
    numero=
        st.integers(),
    prefijo=
        st.integers()
)
Direccion_strategy = st.builds(
    Direccion,
    codigo=
        st.integers(),
    pais=
        safe_text,
    nombre=
        safe_text,
    ciudad=
        safe_text
)
Contacto_strategy = st.builds(
    Contacto,
    nombre=
        safe_text,
    email=
        safe_text
)
Agenda_strategy = st.builds(
    Agenda,
    Introduccion=
        safe_text
)

@given(instance=Foto_strategy)
@settings(max_examples=50)
def test_foto_instantiation(instance):
    assert isinstance(instance, Foto)

@given(instance=Foto_strategy)
def test_foto_alto_type(instance):
    assert isinstance(instance.alto, int)


@given(instance=Foto_strategy)
def test_foto_alto_setter(instance):
    original = instance.alto
    instance.alto = original
    assert instance.alto == original

@given(instance=Foto_strategy)
def test_foto_ancho_type(instance):
    assert isinstance(instance.ancho, int)


@given(instance=Foto_strategy)
def test_foto_ancho_setter(instance):
    original = instance.ancho
    instance.ancho = original
    assert instance.ancho == original

@given(instance=Telefono_strategy)
@settings(max_examples=50)
def test_telefono_instantiation(instance):
    assert isinstance(instance, Telefono)

@given(instance=Telefono_strategy)
def test_telefono_codigo_type(instance):
    assert isinstance(instance.codigo, int)


@given(instance=Telefono_strategy)
def test_telefono_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=Telefono_strategy)
def test_telefono_numero_type(instance):
    assert isinstance(instance.numero, int)


@given(instance=Telefono_strategy)
def test_telefono_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original

@given(instance=Telefono_strategy)
def test_telefono_prefijo_type(instance):
    assert isinstance(instance.prefijo, int)


@given(instance=Telefono_strategy)
def test_telefono_prefijo_setter(instance):
    original = instance.prefijo
    instance.prefijo = original
    assert instance.prefijo == original

@given(instance=Direccion_strategy)
@settings(max_examples=50)
def test_direccion_instantiation(instance):
    assert isinstance(instance, Direccion)

@given(instance=Direccion_strategy)
def test_direccion_codigo_type(instance):
    assert isinstance(instance.codigo, int)


@given(instance=Direccion_strategy)
def test_direccion_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=Direccion_strategy)
def test_direccion_pais_type(instance):
    assert isinstance(instance.pais, str)


@given(instance=Direccion_strategy)
def test_direccion_pais_setter(instance):
    original = instance.pais
    instance.pais = original
    assert instance.pais == original

@given(instance=Direccion_strategy)
def test_direccion_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=Direccion_strategy)
def test_direccion_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Direccion_strategy)
def test_direccion_ciudad_type(instance):
    assert isinstance(instance.ciudad, str)


@given(instance=Direccion_strategy)
def test_direccion_ciudad_setter(instance):
    original = instance.ciudad
    instance.ciudad = original
    assert instance.ciudad == original

@given(instance=Contacto_strategy)
@settings(max_examples=50)
def test_contacto_instantiation(instance):
    assert isinstance(instance, Contacto)

@given(instance=Contacto_strategy)
def test_contacto_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=Contacto_strategy)
def test_contacto_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Contacto_strategy)
def test_contacto_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=Contacto_strategy)
def test_contacto_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Agenda_strategy)
@settings(max_examples=50)
def test_agenda_instantiation(instance):
    assert isinstance(instance, Agenda)

@given(instance=Agenda_strategy)
def test_agenda_Introduccion_type(instance):
    assert isinstance(instance.Introduccion, str)


@given(instance=Agenda_strategy)
def test_agenda_Introduccion_setter(instance):
    original = instance.Introduccion
    instance.Introduccion = original
    assert instance.Introduccion == original
