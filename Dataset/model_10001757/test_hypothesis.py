import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Foto_de_perfil,
    Telefono,
    Direccion,
    Contacto,
    Directorio,
    User_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_foto_de_perfil_is_not_abstract():
    assert not inspect.isabstract(Foto_de_perfil)


def test_foto_de_perfil_constructor_exists():
    assert callable(Foto_de_perfil.__init__)


def test_foto_de_perfil_constructor_args():
    sig = inspect.signature(Foto_de_perfil.__init__)
    params = list(sig.parameters.keys())



def test_telefono_is_not_abstract():
    assert not inspect.isabstract(Telefono)


def test_telefono_constructor_exists():
    assert callable(Telefono.__init__)


def test_telefono_constructor_args():
    sig = inspect.signature(Telefono.__init__)
    params = list(sig.parameters.keys())
    assert "Codigo_de_Area" in params, "Missing parameter 'Codigo_de_Area'"
    assert "Prefijo" in params, "Missing parameter 'Prefijo'"
    assert "Numero" in params, "Missing parameter 'Numero'"

def test_telefono_has_Codigo_de_Area():
    assert hasattr(Telefono, "Codigo_de_Area")
    descriptor = None
    for klass in Telefono.__mro__:
        if "Codigo_de_Area" in klass.__dict__:
            descriptor = klass.__dict__["Codigo_de_Area"]
            break
    assert isinstance(descriptor, property)

def test_telefono_has_Prefijo():
    assert hasattr(Telefono, "Prefijo")
    descriptor = None
    for klass in Telefono.__mro__:
        if "Prefijo" in klass.__dict__:
            descriptor = klass.__dict__["Prefijo"]
            break
    assert isinstance(descriptor, property)

def test_telefono_has_Numero():
    assert hasattr(Telefono, "Numero")
    descriptor = None
    for klass in Telefono.__mro__:
        if "Numero" in klass.__dict__:
            descriptor = klass.__dict__["Numero"]
            break
    assert isinstance(descriptor, property)



def test_direccion_is_not_abstract():
    assert not inspect.isabstract(Direccion)


def test_direccion_constructor_exists():
    assert callable(Direccion.__init__)


def test_direccion_constructor_args():
    sig = inspect.signature(Direccion.__init__)
    params = list(sig.parameters.keys())
    assert "Pais" in params, "Missing parameter 'Pais'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "Ciudad" in params, "Missing parameter 'Ciudad'"
    assert "Codigo_Postal" in params, "Missing parameter 'Codigo_Postal'"

def test_direccion_has_Pais():
    assert hasattr(Direccion, "Pais")
    descriptor = None
    for klass in Direccion.__mro__:
        if "Pais" in klass.__dict__:
            descriptor = klass.__dict__["Pais"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_Nombre():
    assert hasattr(Direccion, "Nombre")
    descriptor = None
    for klass in Direccion.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_Ciudad():
    assert hasattr(Direccion, "Ciudad")
    descriptor = None
    for klass in Direccion.__mro__:
        if "Ciudad" in klass.__dict__:
            descriptor = klass.__dict__["Ciudad"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_Codigo_Postal():
    assert hasattr(Direccion, "Codigo_Postal")
    descriptor = None
    for klass in Direccion.__mro__:
        if "Codigo_Postal" in klass.__dict__:
            descriptor = klass.__dict__["Codigo_Postal"]
            break
    assert isinstance(descriptor, property)



def test_contacto_is_not_abstract():
    assert not inspect.isabstract(Contacto)


def test_contacto_constructor_exists():
    assert callable(Contacto.__init__)


def test_contacto_constructor_args():
    sig = inspect.signature(Contacto.__init__)
    params = list(sig.parameters.keys())
    assert "Correo" in params, "Missing parameter 'Correo'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"

def test_contacto_has_Correo():
    assert hasattr(Contacto, "Correo")
    descriptor = None
    for klass in Contacto.__mro__:
        if "Correo" in klass.__dict__:
            descriptor = klass.__dict__["Correo"]
            break
    assert isinstance(descriptor, property)

def test_contacto_has_Nombre():
    assert hasattr(Contacto, "Nombre")
    descriptor = None
    for klass in Contacto.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)



def test_directorio_is_not_abstract():
    assert not inspect.isabstract(Directorio)


def test_directorio_constructor_exists():
    assert callable(Directorio.__init__)


def test_directorio_constructor_args():
    sig = inspect.signature(Directorio.__init__)
    params = list(sig.parameters.keys())
    assert "Introducir" in params, "Missing parameter 'Introducir'"

def test_directorio_has_Introducir():
    assert hasattr(Directorio, "Introducir")
    descriptor = None
    for klass in Directorio.__mro__:
        if "Introducir" in klass.__dict__:
            descriptor = klass.__dict__["Introducir"]
            break
    assert isinstance(descriptor, property)



def test_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
    params = list(sig.parameters.keys())


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
Foto_de_perfil_strategy = st.builds(
    Foto_de_perfil,
)
Telefono_strategy = st.builds(
    Telefono,
    Codigo_de_Area=
        st.integers(),
    Prefijo=
        st.integers(),
    Numero=
        st.integers()
)
Direccion_strategy = st.builds(
    Direccion,
    Pais=
        safe_text,
    Nombre=
        safe_text,
    Ciudad=
        safe_text,
    Codigo_Postal=
        st.integers()
)
Contacto_strategy = st.builds(
    Contacto,
    Correo=
        safe_text,
    Nombre=
        safe_text
)
Directorio_strategy = st.builds(
    Directorio,
    Introducir=
        safe_text
)
User_Actor_strategy = st.builds(
    User_Actor,
)

@given(instance=Foto_de_perfil_strategy)
@settings(max_examples=50)
def test_foto_de_perfil_instantiation(instance):
    assert isinstance(instance, Foto_de_perfil)

@given(instance=Telefono_strategy)
@settings(max_examples=50)
def test_telefono_instantiation(instance):
    assert isinstance(instance, Telefono)



@given(instance=Telefono_strategy)
def test_telefono_Codigo_de_Area_setter(instance):
    original = instance.Codigo_de_Area
    instance.Codigo_de_Area = original
    assert instance.Codigo_de_Area == original



@given(instance=Telefono_strategy)
def test_telefono_Prefijo_setter(instance):
    original = instance.Prefijo
    instance.Prefijo = original
    assert instance.Prefijo == original



@given(instance=Telefono_strategy)
def test_telefono_Numero_setter(instance):
    original = instance.Numero
    instance.Numero = original
    assert instance.Numero == original

@given(instance=Direccion_strategy)
@settings(max_examples=50)
def test_direccion_instantiation(instance):
    assert isinstance(instance, Direccion)



@given(instance=Direccion_strategy)
def test_direccion_Pais_setter(instance):
    original = instance.Pais
    instance.Pais = original
    assert instance.Pais == original



@given(instance=Direccion_strategy)
def test_direccion_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=Direccion_strategy)
def test_direccion_Ciudad_setter(instance):
    original = instance.Ciudad
    instance.Ciudad = original
    assert instance.Ciudad == original



@given(instance=Direccion_strategy)
def test_direccion_Codigo_Postal_setter(instance):
    original = instance.Codigo_Postal
    instance.Codigo_Postal = original
    assert instance.Codigo_Postal == original

@given(instance=Contacto_strategy)
@settings(max_examples=50)
def test_contacto_instantiation(instance):
    assert isinstance(instance, Contacto)



@given(instance=Contacto_strategy)
def test_contacto_Correo_setter(instance):
    original = instance.Correo
    instance.Correo = original
    assert instance.Correo == original



@given(instance=Contacto_strategy)
def test_contacto_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original

@given(instance=Directorio_strategy)
@settings(max_examples=50)
def test_directorio_instantiation(instance):
    assert isinstance(instance, Directorio)



@given(instance=Directorio_strategy)
def test_directorio_Introducir_setter(instance):
    original = instance.Introducir
    instance.Introducir = original
    assert instance.Introducir == original

@given(instance=User_Actor_strategy)
@settings(max_examples=50)
def test_user_actor_instantiation(instance):
    assert isinstance(instance, User_Actor)
