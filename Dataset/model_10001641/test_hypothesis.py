import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Datos,
    Veterinario,
    Calcular_el_promedio_de_edad_UseCase,
    Calcular_el_numero_de_ejemplares_UseCase,
    Buscar_un_ejemplar_por_su_nombre_UseCase,
    Desplazarse_hasta_el_ultimo_UseCase,
    Desplazarse_hasta_el_primer_UseCase,
    Regresar_hacia_el_anterior_UseCase,
    Avanzar_hacia_el_siguiente__UseCase,
    Usuario__Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datos_is_not_abstract():
    assert not inspect.isabstract(Datos)


def test_datos_constructor_exists():
    assert callable(Datos.__init__)


def test_datos_constructor_args():
    sig = inspect.signature(Datos.__init__)
    params = list(sig.parameters.keys())
    assert "raza" in params, "Missing parameter 'raza'"
    assert "peso" in params, "Missing parameter 'peso'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "altura" in params, "Missing parameter 'altura'"
    assert "observacion" in params, "Missing parameter 'observacion'"
    assert "Edad" in params, "Missing parameter 'Edad'"

def test_datos_has_raza():
    assert hasattr(Datos, "raza")
    descriptor = None
    for klass in Datos.__mro__:
        if "raza" in klass.__dict__:
            descriptor = klass.__dict__["raza"]
            break
    assert isinstance(descriptor, property)

def test_datos_has_peso():
    assert hasattr(Datos, "peso")
    descriptor = None
    for klass in Datos.__mro__:
        if "peso" in klass.__dict__:
            descriptor = klass.__dict__["peso"]
            break
    assert isinstance(descriptor, property)

def test_datos_has_nombre():
    assert hasattr(Datos, "nombre")
    descriptor = None
    for klass in Datos.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_datos_has_altura():
    assert hasattr(Datos, "altura")
    descriptor = None
    for klass in Datos.__mro__:
        if "altura" in klass.__dict__:
            descriptor = klass.__dict__["altura"]
            break
    assert isinstance(descriptor, property)

def test_datos_has_observacion():
    assert hasattr(Datos, "observacion")
    descriptor = None
    for klass in Datos.__mro__:
        if "observacion" in klass.__dict__:
            descriptor = klass.__dict__["observacion"]
            break
    assert isinstance(descriptor, property)

def test_datos_has_Edad():
    assert hasattr(Datos, "Edad")
    descriptor = None
    for klass in Datos.__mro__:
        if "Edad" in klass.__dict__:
            descriptor = klass.__dict__["Edad"]
            break
    assert isinstance(descriptor, property)



def test_veterinario_is_not_abstract():
    assert not inspect.isabstract(Veterinario)


def test_veterinario_constructor_exists():
    assert callable(Veterinario.__init__)


def test_veterinario_constructor_args():
    sig = inspect.signature(Veterinario.__init__)
    params = list(sig.parameters.keys())



def test_calcular_el_promedio_de_edad_usecase_is_not_abstract():
    assert not inspect.isabstract(Calcular_el_promedio_de_edad_UseCase)


def test_calcular_el_promedio_de_edad_usecase_constructor_exists():
    assert callable(Calcular_el_promedio_de_edad_UseCase.__init__)


def test_calcular_el_promedio_de_edad_usecase_constructor_args():
    sig = inspect.signature(Calcular_el_promedio_de_edad_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_calcular_el_numero_de_ejemplares_usecase_is_not_abstract():
    assert not inspect.isabstract(Calcular_el_numero_de_ejemplares_UseCase)


def test_calcular_el_numero_de_ejemplares_usecase_constructor_exists():
    assert callable(Calcular_el_numero_de_ejemplares_UseCase.__init__)


def test_calcular_el_numero_de_ejemplares_usecase_constructor_args():
    sig = inspect.signature(Calcular_el_numero_de_ejemplares_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_buscar_un_ejemplar_por_su_nombre_usecase_is_not_abstract():
    assert not inspect.isabstract(Buscar_un_ejemplar_por_su_nombre_UseCase)


def test_buscar_un_ejemplar_por_su_nombre_usecase_constructor_exists():
    assert callable(Buscar_un_ejemplar_por_su_nombre_UseCase.__init__)


def test_buscar_un_ejemplar_por_su_nombre_usecase_constructor_args():
    sig = inspect.signature(Buscar_un_ejemplar_por_su_nombre_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_desplazarse_hasta_el_ultimo_usecase_is_not_abstract():
    assert not inspect.isabstract(Desplazarse_hasta_el_ultimo_UseCase)


def test_desplazarse_hasta_el_ultimo_usecase_constructor_exists():
    assert callable(Desplazarse_hasta_el_ultimo_UseCase.__init__)


def test_desplazarse_hasta_el_ultimo_usecase_constructor_args():
    sig = inspect.signature(Desplazarse_hasta_el_ultimo_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_desplazarse_hasta_el_primer_usecase_is_not_abstract():
    assert not inspect.isabstract(Desplazarse_hasta_el_primer_UseCase)


def test_desplazarse_hasta_el_primer_usecase_constructor_exists():
    assert callable(Desplazarse_hasta_el_primer_UseCase.__init__)


def test_desplazarse_hasta_el_primer_usecase_constructor_args():
    sig = inspect.signature(Desplazarse_hasta_el_primer_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_regresar_hacia_el_anterior_usecase_is_not_abstract():
    assert not inspect.isabstract(Regresar_hacia_el_anterior_UseCase)


def test_regresar_hacia_el_anterior_usecase_constructor_exists():
    assert callable(Regresar_hacia_el_anterior_UseCase.__init__)


def test_regresar_hacia_el_anterior_usecase_constructor_args():
    sig = inspect.signature(Regresar_hacia_el_anterior_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_avanzar_hacia_el_siguiente__usecase_is_not_abstract():
    assert not inspect.isabstract(Avanzar_hacia_el_siguiente__UseCase)


def test_avanzar_hacia_el_siguiente__usecase_constructor_exists():
    assert callable(Avanzar_hacia_el_siguiente__UseCase.__init__)


def test_avanzar_hacia_el_siguiente__usecase_constructor_args():
    sig = inspect.signature(Avanzar_hacia_el_siguiente__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usuario__actor_is_not_abstract():
    assert not inspect.isabstract(Usuario__Actor)


def test_usuario__actor_constructor_exists():
    assert callable(Usuario__Actor.__init__)


def test_usuario__actor_constructor_args():
    sig = inspect.signature(Usuario__Actor.__init__)
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
Datos_strategy = st.builds(
    Datos,
    raza=
        safe_text,
    peso=
        safe_text,
    nombre=
        safe_text,
    altura=
        safe_text,
    observacion=
        safe_text,
    Edad=
        st.integers()
)
Veterinario_strategy = st.builds(
    Veterinario,
)
Calcular_el_promedio_de_edad_UseCase_strategy = st.builds(
    Calcular_el_promedio_de_edad_UseCase,
)
Calcular_el_numero_de_ejemplares_UseCase_strategy = st.builds(
    Calcular_el_numero_de_ejemplares_UseCase,
)
Buscar_un_ejemplar_por_su_nombre_UseCase_strategy = st.builds(
    Buscar_un_ejemplar_por_su_nombre_UseCase,
)
Desplazarse_hasta_el_ultimo_UseCase_strategy = st.builds(
    Desplazarse_hasta_el_ultimo_UseCase,
)
Desplazarse_hasta_el_primer_UseCase_strategy = st.builds(
    Desplazarse_hasta_el_primer_UseCase,
)
Regresar_hacia_el_anterior_UseCase_strategy = st.builds(
    Regresar_hacia_el_anterior_UseCase,
)
Avanzar_hacia_el_siguiente__UseCase_strategy = st.builds(
    Avanzar_hacia_el_siguiente__UseCase,
)
Usuario__Actor_strategy = st.builds(
    Usuario__Actor,
)

@given(instance=Datos_strategy)
@settings(max_examples=50)
def test_datos_instantiation(instance):
    assert isinstance(instance, Datos)



@given(instance=Datos_strategy)
def test_datos_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original



@given(instance=Datos_strategy)
def test_datos_peso_setter(instance):
    original = instance.peso
    instance.peso = original
    assert instance.peso == original



@given(instance=Datos_strategy)
def test_datos_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Datos_strategy)
def test_datos_altura_setter(instance):
    original = instance.altura
    instance.altura = original
    assert instance.altura == original



@given(instance=Datos_strategy)
def test_datos_observacion_setter(instance):
    original = instance.observacion
    instance.observacion = original
    assert instance.observacion == original



@given(instance=Datos_strategy)
def test_datos_Edad_setter(instance):
    original = instance.Edad
    instance.Edad = original
    assert instance.Edad == original

@given(instance=Veterinario_strategy)
@settings(max_examples=50)
def test_veterinario_instantiation(instance):
    assert isinstance(instance, Veterinario)

@given(instance=Calcular_el_promedio_de_edad_UseCase_strategy)
@settings(max_examples=50)
def test_calcular_el_promedio_de_edad_usecase_instantiation(instance):
    assert isinstance(instance, Calcular_el_promedio_de_edad_UseCase)

@given(instance=Calcular_el_numero_de_ejemplares_UseCase_strategy)
@settings(max_examples=50)
def test_calcular_el_numero_de_ejemplares_usecase_instantiation(instance):
    assert isinstance(instance, Calcular_el_numero_de_ejemplares_UseCase)

@given(instance=Buscar_un_ejemplar_por_su_nombre_UseCase_strategy)
@settings(max_examples=50)
def test_buscar_un_ejemplar_por_su_nombre_usecase_instantiation(instance):
    assert isinstance(instance, Buscar_un_ejemplar_por_su_nombre_UseCase)

@given(instance=Desplazarse_hasta_el_ultimo_UseCase_strategy)
@settings(max_examples=50)
def test_desplazarse_hasta_el_ultimo_usecase_instantiation(instance):
    assert isinstance(instance, Desplazarse_hasta_el_ultimo_UseCase)

@given(instance=Desplazarse_hasta_el_primer_UseCase_strategy)
@settings(max_examples=50)
def test_desplazarse_hasta_el_primer_usecase_instantiation(instance):
    assert isinstance(instance, Desplazarse_hasta_el_primer_UseCase)

@given(instance=Regresar_hacia_el_anterior_UseCase_strategy)
@settings(max_examples=50)
def test_regresar_hacia_el_anterior_usecase_instantiation(instance):
    assert isinstance(instance, Regresar_hacia_el_anterior_UseCase)

@given(instance=Avanzar_hacia_el_siguiente__UseCase_strategy)
@settings(max_examples=50)
def test_avanzar_hacia_el_siguiente__usecase_instantiation(instance):
    assert isinstance(instance, Avanzar_hacia_el_siguiente__UseCase)

@given(instance=Usuario__Actor_strategy)
@settings(max_examples=50)
def test_usuario__actor_instantiation(instance):
    assert isinstance(instance, Usuario__Actor)
