import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Caninos,
    Empresa,
    Desplazarse_hasta_el__ltimo_ejemplar__UseCase,
    Desplazarse_hasta_el_primer_ejemplar__UseCase,
    Regresar_hacia_el_anterior_ejemplar__UseCase,
    Avanzar_hacia_el_siguiente_ejemplar__UseCase,
    Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase,
    Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase,
    Buscar_ejemplar_por_su_nombre__UseCase,
    Usuario_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_caninos_is_not_abstract():
    assert not inspect.isabstract(Caninos)


def test_caninos_constructor_exists():
    assert callable(Caninos.__init__)


def test_caninos_constructor_args():
    sig = inspect.signature(Caninos.__init__)
    params = list(sig.parameters.keys())
    assert "raza" in params, "Missing parameter 'raza'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "edad" in params, "Missing parameter 'edad'"
    assert "observaciones" in params, "Missing parameter 'observaciones'"
    assert "altura" in params, "Missing parameter 'altura'"
    assert "peso" in params, "Missing parameter 'peso'"

def test_caninos_has_raza():
    assert hasattr(Caninos, "raza")
    descriptor = None
    for klass in Caninos.__mro__:
        if "raza" in klass.__dict__:
            descriptor = klass.__dict__["raza"]
            break
    assert isinstance(descriptor, property)

def test_caninos_has_nombre():
    assert hasattr(Caninos, "nombre")
    descriptor = None
    for klass in Caninos.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_caninos_has_edad():
    assert hasattr(Caninos, "edad")
    descriptor = None
    for klass in Caninos.__mro__:
        if "edad" in klass.__dict__:
            descriptor = klass.__dict__["edad"]
            break
    assert isinstance(descriptor, property)

def test_caninos_has_observaciones():
    assert hasattr(Caninos, "observaciones")
    descriptor = None
    for klass in Caninos.__mro__:
        if "observaciones" in klass.__dict__:
            descriptor = klass.__dict__["observaciones"]
            break
    assert isinstance(descriptor, property)

def test_caninos_has_altura():
    assert hasattr(Caninos, "altura")
    descriptor = None
    for klass in Caninos.__mro__:
        if "altura" in klass.__dict__:
            descriptor = klass.__dict__["altura"]
            break
    assert isinstance(descriptor, property)

def test_caninos_has_peso():
    assert hasattr(Caninos, "peso")
    descriptor = None
    for klass in Caninos.__mro__:
        if "peso" in klass.__dict__:
            descriptor = klass.__dict__["peso"]
            break
    assert isinstance(descriptor, property)



def test_empresa_is_not_abstract():
    assert not inspect.isabstract(Empresa)


def test_empresa_constructor_exists():
    assert callable(Empresa.__init__)


def test_empresa_constructor_args():
    sig = inspect.signature(Empresa.__init__)
    params = list(sig.parameters.keys())



def test_desplazarse_hasta_el__ltimo_ejemplar__usecase_is_not_abstract():
    assert not inspect.isabstract(Desplazarse_hasta_el__ltimo_ejemplar__UseCase)


def test_desplazarse_hasta_el__ltimo_ejemplar__usecase_constructor_exists():
    assert callable(Desplazarse_hasta_el__ltimo_ejemplar__UseCase.__init__)


def test_desplazarse_hasta_el__ltimo_ejemplar__usecase_constructor_args():
    sig = inspect.signature(Desplazarse_hasta_el__ltimo_ejemplar__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_desplazarse_hasta_el_primer_ejemplar__usecase_is_not_abstract():
    assert not inspect.isabstract(Desplazarse_hasta_el_primer_ejemplar__UseCase)


def test_desplazarse_hasta_el_primer_ejemplar__usecase_constructor_exists():
    assert callable(Desplazarse_hasta_el_primer_ejemplar__UseCase.__init__)


def test_desplazarse_hasta_el_primer_ejemplar__usecase_constructor_args():
    sig = inspect.signature(Desplazarse_hasta_el_primer_ejemplar__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_regresar_hacia_el_anterior_ejemplar__usecase_is_not_abstract():
    assert not inspect.isabstract(Regresar_hacia_el_anterior_ejemplar__UseCase)


def test_regresar_hacia_el_anterior_ejemplar__usecase_constructor_exists():
    assert callable(Regresar_hacia_el_anterior_ejemplar__UseCase.__init__)


def test_regresar_hacia_el_anterior_ejemplar__usecase_constructor_args():
    sig = inspect.signature(Regresar_hacia_el_anterior_ejemplar__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_avanzar_hacia_el_siguiente_ejemplar__usecase_is_not_abstract():
    assert not inspect.isabstract(Avanzar_hacia_el_siguiente_ejemplar__UseCase)


def test_avanzar_hacia_el_siguiente_ejemplar__usecase_constructor_exists():
    assert callable(Avanzar_hacia_el_siguiente_ejemplar__UseCase.__init__)


def test_avanzar_hacia_el_siguiente_ejemplar__usecase_constructor_args():
    sig = inspect.signature(Avanzar_hacia_el_siguiente_ejemplar__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__usecase_is_not_abstract():
    assert not inspect.isabstract(Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase)


def test_calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__usecase_constructor_exists():
    assert callable(Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase.__init__)


def test_calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__usecase_constructor_args():
    sig = inspect.signature(Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_calcular_n_mero_de_ejemplares_caninos_por_raza__usecase_is_not_abstract():
    assert not inspect.isabstract(Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase)


def test_calcular_n_mero_de_ejemplares_caninos_por_raza__usecase_constructor_exists():
    assert callable(Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase.__init__)


def test_calcular_n_mero_de_ejemplares_caninos_por_raza__usecase_constructor_args():
    sig = inspect.signature(Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_buscar_ejemplar_por_su_nombre__usecase_is_not_abstract():
    assert not inspect.isabstract(Buscar_ejemplar_por_su_nombre__UseCase)


def test_buscar_ejemplar_por_su_nombre__usecase_constructor_exists():
    assert callable(Buscar_ejemplar_por_su_nombre__UseCase.__init__)


def test_buscar_ejemplar_por_su_nombre__usecase_constructor_args():
    sig = inspect.signature(Buscar_ejemplar_por_su_nombre__UseCase.__init__)
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
Caninos_strategy = st.builds(
    Caninos,
    raza=
        safe_text,
    nombre=
        safe_text,
    edad=
        safe_text,
    observaciones=
        safe_text,
    altura=
        safe_text,
    peso=
        safe_text
)
Empresa_strategy = st.builds(
    Empresa,
)
Desplazarse_hasta_el__ltimo_ejemplar__UseCase_strategy = st.builds(
    Desplazarse_hasta_el__ltimo_ejemplar__UseCase,
)
Desplazarse_hasta_el_primer_ejemplar__UseCase_strategy = st.builds(
    Desplazarse_hasta_el_primer_ejemplar__UseCase,
)
Regresar_hacia_el_anterior_ejemplar__UseCase_strategy = st.builds(
    Regresar_hacia_el_anterior_ejemplar__UseCase,
)
Avanzar_hacia_el_siguiente_ejemplar__UseCase_strategy = st.builds(
    Avanzar_hacia_el_siguiente_ejemplar__UseCase,
)
Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase_strategy = st.builds(
    Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase,
)
Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase_strategy = st.builds(
    Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase,
)
Buscar_ejemplar_por_su_nombre__UseCase_strategy = st.builds(
    Buscar_ejemplar_por_su_nombre__UseCase,
)
Usuario_Actor_strategy = st.builds(
    Usuario_Actor,
)

@given(instance=Caninos_strategy)
@settings(max_examples=50)
def test_caninos_instantiation(instance):
    assert isinstance(instance, Caninos)



@given(instance=Caninos_strategy)
def test_caninos_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original



@given(instance=Caninos_strategy)
def test_caninos_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Caninos_strategy)
def test_caninos_edad_setter(instance):
    original = instance.edad
    instance.edad = original
    assert instance.edad == original



@given(instance=Caninos_strategy)
def test_caninos_observaciones_setter(instance):
    original = instance.observaciones
    instance.observaciones = original
    assert instance.observaciones == original



@given(instance=Caninos_strategy)
def test_caninos_altura_setter(instance):
    original = instance.altura
    instance.altura = original
    assert instance.altura == original



@given(instance=Caninos_strategy)
def test_caninos_peso_setter(instance):
    original = instance.peso
    instance.peso = original
    assert instance.peso == original

@given(instance=Empresa_strategy)
@settings(max_examples=50)
def test_empresa_instantiation(instance):
    assert isinstance(instance, Empresa)

@given(instance=Desplazarse_hasta_el__ltimo_ejemplar__UseCase_strategy)
@settings(max_examples=50)
def test_desplazarse_hasta_el__ltimo_ejemplar__usecase_instantiation(instance):
    assert isinstance(instance, Desplazarse_hasta_el__ltimo_ejemplar__UseCase)

@given(instance=Desplazarse_hasta_el_primer_ejemplar__UseCase_strategy)
@settings(max_examples=50)
def test_desplazarse_hasta_el_primer_ejemplar__usecase_instantiation(instance):
    assert isinstance(instance, Desplazarse_hasta_el_primer_ejemplar__UseCase)

@given(instance=Regresar_hacia_el_anterior_ejemplar__UseCase_strategy)
@settings(max_examples=50)
def test_regresar_hacia_el_anterior_ejemplar__usecase_instantiation(instance):
    assert isinstance(instance, Regresar_hacia_el_anterior_ejemplar__UseCase)

@given(instance=Avanzar_hacia_el_siguiente_ejemplar__UseCase_strategy)
@settings(max_examples=50)
def test_avanzar_hacia_el_siguiente_ejemplar__usecase_instantiation(instance):
    assert isinstance(instance, Avanzar_hacia_el_siguiente_ejemplar__UseCase)

@given(instance=Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase_strategy)
@settings(max_examples=50)
def test_calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__usecase_instantiation(instance):
    assert isinstance(instance, Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase)

@given(instance=Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase_strategy)
@settings(max_examples=50)
def test_calcular_n_mero_de_ejemplares_caninos_por_raza__usecase_instantiation(instance):
    assert isinstance(instance, Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase)

@given(instance=Buscar_ejemplar_por_su_nombre__UseCase_strategy)
@settings(max_examples=50)
def test_buscar_ejemplar_por_su_nombre__usecase_instantiation(instance):
    assert isinstance(instance, Buscar_ejemplar_por_su_nombre__UseCase)

@given(instance=Usuario_Actor_strategy)
@settings(max_examples=50)
def test_usuario_actor_instantiation(instance):
    assert isinstance(instance, Usuario_Actor)
