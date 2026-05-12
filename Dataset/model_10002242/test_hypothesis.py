import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Lista_de_COntacto,
    Crear_Contacto,
    Buscar,
    Menu_Principal,
    Libro_de_Direcciones1,
    Foto,
    Tel_fono,
    Direccion,
    Contacto,
    Libro_de_Direcciones,
    Cancelar_UseCase,
    Guardar_UseCase,
    Eliminar_Contacto_UseCase,
    Actualizar_COntacto_UseCase,
    Crear_Contacto_UseCase,
    Buscar_Contactos_UseCase,
    Usuario_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lista_de_contacto_is_not_abstract():
    assert not inspect.isabstract(Lista_de_COntacto)


def test_lista_de_contacto_constructor_exists():
    assert callable(Lista_de_COntacto.__init__)


def test_lista_de_contacto_constructor_args():
    sig = inspect.signature(Lista_de_COntacto.__init__)
    params = list(sig.parameters.keys())



def test_crear_contacto_is_not_abstract():
    assert not inspect.isabstract(Crear_Contacto)


def test_crear_contacto_constructor_exists():
    assert callable(Crear_Contacto.__init__)


def test_crear_contacto_constructor_args():
    sig = inspect.signature(Crear_Contacto.__init__)
    params = list(sig.parameters.keys())



def test_buscar_is_not_abstract():
    assert not inspect.isabstract(Buscar)


def test_buscar_constructor_exists():
    assert callable(Buscar.__init__)


def test_buscar_constructor_args():
    sig = inspect.signature(Buscar.__init__)
    params = list(sig.parameters.keys())



def test_menu_principal_is_not_abstract():
    assert not inspect.isabstract(Menu_Principal)


def test_menu_principal_constructor_exists():
    assert callable(Menu_Principal.__init__)


def test_menu_principal_constructor_args():
    sig = inspect.signature(Menu_Principal.__init__)
    params = list(sig.parameters.keys())



def test_libro_de_direcciones1_is_not_abstract():
    assert not inspect.isabstract(Libro_de_Direcciones1)


def test_libro_de_direcciones1_constructor_exists():
    assert callable(Libro_de_Direcciones1.__init__)


def test_libro_de_direcciones1_constructor_args():
    sig = inspect.signature(Libro_de_Direcciones1.__init__)
    params = list(sig.parameters.keys())



def test_foto_is_not_abstract():
    assert not inspect.isabstract(Foto)


def test_foto_constructor_exists():
    assert callable(Foto.__init__)


def test_foto_constructor_args():
    sig = inspect.signature(Foto.__init__)
    params = list(sig.parameters.keys())
    assert "largo" in params, "Missing parameter 'largo'"
    assert "ancho" in params, "Missing parameter 'ancho'"

def test_foto_has_largo():
    assert hasattr(Foto, "largo")
    descriptor = None
    for klass in Foto.__mro__:
        if "largo" in klass.__dict__:
            descriptor = klass.__dict__["largo"]
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



def test_tel_fono_is_not_abstract():
    assert not inspect.isabstract(Tel_fono)


def test_tel_fono_constructor_exists():
    assert callable(Tel_fono.__init__)


def test_tel_fono_constructor_args():
    sig = inspect.signature(Tel_fono.__init__)
    params = list(sig.parameters.keys())
    assert "Codigo_area" in params, "Missing parameter 'Codigo_area'"
    assert "numero" in params, "Missing parameter 'numero'"
    assert "prefijo" in params, "Missing parameter 'prefijo'"

def test_tel_fono_has_Codigo_area():
    assert hasattr(Tel_fono, "Codigo_area")
    descriptor = None
    for klass in Tel_fono.__mro__:
        if "Codigo_area" in klass.__dict__:
            descriptor = klass.__dict__["Codigo_area"]
            break
    assert isinstance(descriptor, property)

def test_tel_fono_has_numero():
    assert hasattr(Tel_fono, "numero")
    descriptor = None
    for klass in Tel_fono.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)

def test_tel_fono_has_prefijo():
    assert hasattr(Tel_fono, "prefijo")
    descriptor = None
    for klass in Tel_fono.__mro__:
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
    assert "departamento" in params, "Missing parameter 'departamento'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "CodigoPostal" in params, "Missing parameter 'CodigoPostal'"
    assert "Ciudad" in params, "Missing parameter 'Ciudad'"

def test_direccion_has_departamento():
    assert hasattr(Direccion, "departamento")
    descriptor = None
    for klass in Direccion.__mro__:
        if "departamento" in klass.__dict__:
            descriptor = klass.__dict__["departamento"]
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

def test_direccion_has_CodigoPostal():
    assert hasattr(Direccion, "CodigoPostal")
    descriptor = None
    for klass in Direccion.__mro__:
        if "CodigoPostal" in klass.__dict__:
            descriptor = klass.__dict__["CodigoPostal"]
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



def test_contacto_is_not_abstract():
    assert not inspect.isabstract(Contacto)


def test_contacto_constructor_exists():
    assert callable(Contacto.__init__)


def test_contacto_constructor_args():
    sig = inspect.signature(Contacto.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_contacto_has_email():
    assert hasattr(Contacto, "email")
    descriptor = None
    for klass in Contacto.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_contacto_has_nombre():
    assert hasattr(Contacto, "nombre")
    descriptor = None
    for klass in Contacto.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_libro_de_direcciones_is_not_abstract():
    assert not inspect.isabstract(Libro_de_Direcciones)


def test_libro_de_direcciones_constructor_exists():
    assert callable(Libro_de_Direcciones.__init__)


def test_libro_de_direcciones_constructor_args():
    sig = inspect.signature(Libro_de_Direcciones.__init__)
    params = list(sig.parameters.keys())
    assert "Introduccion" in params, "Missing parameter 'Introduccion'"

def test_libro_de_direcciones_has_Introduccion():
    assert hasattr(Libro_de_Direcciones, "Introduccion")
    descriptor = None
    for klass in Libro_de_Direcciones.__mro__:
        if "Introduccion" in klass.__dict__:
            descriptor = klass.__dict__["Introduccion"]
            break
    assert isinstance(descriptor, property)



def test_cancelar_usecase_is_not_abstract():
    assert not inspect.isabstract(Cancelar_UseCase)


def test_cancelar_usecase_constructor_exists():
    assert callable(Cancelar_UseCase.__init__)


def test_cancelar_usecase_constructor_args():
    sig = inspect.signature(Cancelar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_guardar_usecase_is_not_abstract():
    assert not inspect.isabstract(Guardar_UseCase)


def test_guardar_usecase_constructor_exists():
    assert callable(Guardar_UseCase.__init__)


def test_guardar_usecase_constructor_args():
    sig = inspect.signature(Guardar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_eliminar_contacto_usecase_is_not_abstract():
    assert not inspect.isabstract(Eliminar_Contacto_UseCase)


def test_eliminar_contacto_usecase_constructor_exists():
    assert callable(Eliminar_Contacto_UseCase.__init__)


def test_eliminar_contacto_usecase_constructor_args():
    sig = inspect.signature(Eliminar_Contacto_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_actualizar_contacto_usecase_is_not_abstract():
    assert not inspect.isabstract(Actualizar_COntacto_UseCase)


def test_actualizar_contacto_usecase_constructor_exists():
    assert callable(Actualizar_COntacto_UseCase.__init__)


def test_actualizar_contacto_usecase_constructor_args():
    sig = inspect.signature(Actualizar_COntacto_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_crear_contacto_usecase_is_not_abstract():
    assert not inspect.isabstract(Crear_Contacto_UseCase)


def test_crear_contacto_usecase_constructor_exists():
    assert callable(Crear_Contacto_UseCase.__init__)


def test_crear_contacto_usecase_constructor_args():
    sig = inspect.signature(Crear_Contacto_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_buscar_contactos_usecase_is_not_abstract():
    assert not inspect.isabstract(Buscar_Contactos_UseCase)


def test_buscar_contactos_usecase_constructor_exists():
    assert callable(Buscar_Contactos_UseCase.__init__)


def test_buscar_contactos_usecase_constructor_args():
    sig = inspect.signature(Buscar_Contactos_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usuario_actor_is_not_abstract():
    assert not inspect.isabstract(Usuario_Actor)


def test_usuario_actor_constructor_exists():
    assert callable(Usuario_Actor.__init__)


def test_usuario_actor_constructor_args():
    sig = inspect.signature(Usuario_Actor.__init__)
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
Lista_de_COntacto_strategy = st.builds(
    Lista_de_COntacto,
)
Crear_Contacto_strategy = st.builds(
    Crear_Contacto,
)
Buscar_strategy = st.builds(
    Buscar,
)
Menu_Principal_strategy = st.builds(
    Menu_Principal,
)
Libro_de_Direcciones1_strategy = st.builds(
    Libro_de_Direcciones1,
)
Foto_strategy = st.builds(
    Foto,
    largo=
        st.integers(),
    ancho=
        st.integers()
)
Tel_fono_strategy = st.builds(
    Tel_fono,
    Codigo_area=
        st.integers(),
    numero=
        st.integers(),
    prefijo=
        st.integers()
)
Direccion_strategy = st.builds(
    Direccion,
    departamento=
        safe_text,
    nombre=
        safe_text,
    CodigoPostal=
        st.integers(),
    Ciudad=
        safe_text
)
Contacto_strategy = st.builds(
    Contacto,
    email=
        safe_text,
    nombre=
        safe_text
)
Libro_de_Direcciones_strategy = st.builds(
    Libro_de_Direcciones,
    Introduccion=
        safe_text
)
Cancelar_UseCase_strategy = st.builds(
    Cancelar_UseCase,
)
Guardar_UseCase_strategy = st.builds(
    Guardar_UseCase,
)
Eliminar_Contacto_UseCase_strategy = st.builds(
    Eliminar_Contacto_UseCase,
)
Actualizar_COntacto_UseCase_strategy = st.builds(
    Actualizar_COntacto_UseCase,
)
Crear_Contacto_UseCase_strategy = st.builds(
    Crear_Contacto_UseCase,
)
Buscar_Contactos_UseCase_strategy = st.builds(
    Buscar_Contactos_UseCase,
)
Usuario_Actor_strategy = st.builds(
    Usuario_Actor,
)

@given(instance=Lista_de_COntacto_strategy)
@settings(max_examples=50)
def test_lista_de_contacto_instantiation(instance):
    assert isinstance(instance, Lista_de_COntacto)

@given(instance=Crear_Contacto_strategy)
@settings(max_examples=50)
def test_crear_contacto_instantiation(instance):
    assert isinstance(instance, Crear_Contacto)

@given(instance=Buscar_strategy)
@settings(max_examples=50)
def test_buscar_instantiation(instance):
    assert isinstance(instance, Buscar)

@given(instance=Menu_Principal_strategy)
@settings(max_examples=50)
def test_menu_principal_instantiation(instance):
    assert isinstance(instance, Menu_Principal)

@given(instance=Libro_de_Direcciones1_strategy)
@settings(max_examples=50)
def test_libro_de_direcciones1_instantiation(instance):
    assert isinstance(instance, Libro_de_Direcciones1)

@given(instance=Foto_strategy)
@settings(max_examples=50)
def test_foto_instantiation(instance):
    assert isinstance(instance, Foto)



@given(instance=Foto_strategy)
def test_foto_largo_setter(instance):
    original = instance.largo
    instance.largo = original
    assert instance.largo == original



@given(instance=Foto_strategy)
def test_foto_ancho_setter(instance):
    original = instance.ancho
    instance.ancho = original
    assert instance.ancho == original

@given(instance=Tel_fono_strategy)
@settings(max_examples=50)
def test_tel_fono_instantiation(instance):
    assert isinstance(instance, Tel_fono)



@given(instance=Tel_fono_strategy)
def test_tel_fono_Codigo_area_setter(instance):
    original = instance.Codigo_area
    instance.Codigo_area = original
    assert instance.Codigo_area == original



@given(instance=Tel_fono_strategy)
def test_tel_fono_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=Tel_fono_strategy)
def test_tel_fono_prefijo_setter(instance):
    original = instance.prefijo
    instance.prefijo = original
    assert instance.prefijo == original

@given(instance=Direccion_strategy)
@settings(max_examples=50)
def test_direccion_instantiation(instance):
    assert isinstance(instance, Direccion)



@given(instance=Direccion_strategy)
def test_direccion_departamento_setter(instance):
    original = instance.departamento
    instance.departamento = original
    assert instance.departamento == original



@given(instance=Direccion_strategy)
def test_direccion_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Direccion_strategy)
def test_direccion_CodigoPostal_setter(instance):
    original = instance.CodigoPostal
    instance.CodigoPostal = original
    assert instance.CodigoPostal == original



@given(instance=Direccion_strategy)
def test_direccion_Ciudad_setter(instance):
    original = instance.Ciudad
    instance.Ciudad = original
    assert instance.Ciudad == original

@given(instance=Contacto_strategy)
@settings(max_examples=50)
def test_contacto_instantiation(instance):
    assert isinstance(instance, Contacto)



@given(instance=Contacto_strategy)
def test_contacto_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Contacto_strategy)
def test_contacto_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Libro_de_Direcciones_strategy)
@settings(max_examples=50)
def test_libro_de_direcciones_instantiation(instance):
    assert isinstance(instance, Libro_de_Direcciones)



@given(instance=Libro_de_Direcciones_strategy)
def test_libro_de_direcciones_Introduccion_setter(instance):
    original = instance.Introduccion
    instance.Introduccion = original
    assert instance.Introduccion == original

@given(instance=Cancelar_UseCase_strategy)
@settings(max_examples=50)
def test_cancelar_usecase_instantiation(instance):
    assert isinstance(instance, Cancelar_UseCase)

@given(instance=Guardar_UseCase_strategy)
@settings(max_examples=50)
def test_guardar_usecase_instantiation(instance):
    assert isinstance(instance, Guardar_UseCase)

@given(instance=Eliminar_Contacto_UseCase_strategy)
@settings(max_examples=50)
def test_eliminar_contacto_usecase_instantiation(instance):
    assert isinstance(instance, Eliminar_Contacto_UseCase)

@given(instance=Actualizar_COntacto_UseCase_strategy)
@settings(max_examples=50)
def test_actualizar_contacto_usecase_instantiation(instance):
    assert isinstance(instance, Actualizar_COntacto_UseCase)

@given(instance=Crear_Contacto_UseCase_strategy)
@settings(max_examples=50)
def test_crear_contacto_usecase_instantiation(instance):
    assert isinstance(instance, Crear_Contacto_UseCase)

@given(instance=Buscar_Contactos_UseCase_strategy)
@settings(max_examples=50)
def test_buscar_contactos_usecase_instantiation(instance):
    assert isinstance(instance, Buscar_Contactos_UseCase)

@given(instance=Usuario_Actor_strategy)
@settings(max_examples=50)
def test_usuario_actor_instantiation(instance):
    assert isinstance(instance, Usuario_Actor)
