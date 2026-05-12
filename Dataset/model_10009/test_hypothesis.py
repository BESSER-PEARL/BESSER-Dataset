import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    itculiacan::Universidad,
    itculiacan::Profesor,
    itculiacan::Materia,
    itculiacan::Aula,
    itculiacan::Grupo,
    itculiacan::PlanEstudio,
    itculiacan::Generacion,
    itculiacan::Alumno,
    Nombramiento,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_itculiacan::universidad_is_not_abstract():
    assert not inspect.isabstract(itculiacan::Universidad)


def test_itculiacan::universidad_constructor_exists():
    assert callable(itculiacan::Universidad.__init__)


def test_itculiacan::universidad_constructor_args():
    sig = inspect.signature(itculiacan::Universidad.__init__)
    params = list(sig.parameters.keys())



def test_itculiacan::profesor_is_not_abstract():
    assert not inspect.isabstract(itculiacan::Profesor)


def test_itculiacan::profesor_constructor_exists():
    assert callable(itculiacan::Profesor.__init__)


def test_itculiacan::profesor_constructor_args():
    sig = inspect.signature(itculiacan::Profesor.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "nombramiento" in params, "Missing parameter 'nombramiento'"
    assert "clave" in params, "Missing parameter 'clave'"
    assert "numeroMaterias" in params, "Missing parameter 'numeroMaterias'"

def test_itculiacan::profesor_has_nombre():
    assert hasattr(itculiacan::Profesor, "nombre")
    descriptor = None
    for klass in itculiacan::Profesor.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan::profesor_has_nombramiento():
    assert hasattr(itculiacan::Profesor, "nombramiento")
    descriptor = None
    for klass in itculiacan::Profesor.__mro__:
        if "nombramiento" in klass.__dict__:
            descriptor = klass.__dict__["nombramiento"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan::profesor_has_clave():
    assert hasattr(itculiacan::Profesor, "clave")
    descriptor = None
    for klass in itculiacan::Profesor.__mro__:
        if "clave" in klass.__dict__:
            descriptor = klass.__dict__["clave"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan::profesor_has_numeroMaterias():
    assert hasattr(itculiacan::Profesor, "numeroMaterias")
    descriptor = None
    for klass in itculiacan::Profesor.__mro__:
        if "numeroMaterias" in klass.__dict__:
            descriptor = klass.__dict__["numeroMaterias"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan::materia_is_not_abstract():
    assert not inspect.isabstract(itculiacan::Materia)


def test_itculiacan::materia_constructor_exists():
    assert callable(itculiacan::Materia.__init__)


def test_itculiacan::materia_constructor_args():
    sig = inspect.signature(itculiacan::Materia.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "clave" in params, "Missing parameter 'clave'"

def test_itculiacan::materia_has_nombre():
    assert hasattr(itculiacan::Materia, "nombre")
    descriptor = None
    for klass in itculiacan::Materia.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan::materia_has_clave():
    assert hasattr(itculiacan::Materia, "clave")
    descriptor = None
    for klass in itculiacan::Materia.__mro__:
        if "clave" in klass.__dict__:
            descriptor = klass.__dict__["clave"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan::aula_is_not_abstract():
    assert not inspect.isabstract(itculiacan::Aula)


def test_itculiacan::aula_constructor_exists():
    assert callable(itculiacan::Aula.__init__)


def test_itculiacan::aula_constructor_args():
    sig = inspect.signature(itculiacan::Aula.__init__)
    params = list(sig.parameters.keys())
    assert "capacidad" in params, "Missing parameter 'capacidad'"
    assert "clave" in params, "Missing parameter 'clave'"

def test_itculiacan::aula_has_capacidad():
    assert hasattr(itculiacan::Aula, "capacidad")
    descriptor = None
    for klass in itculiacan::Aula.__mro__:
        if "capacidad" in klass.__dict__:
            descriptor = klass.__dict__["capacidad"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan::aula_has_clave():
    assert hasattr(itculiacan::Aula, "clave")
    descriptor = None
    for klass in itculiacan::Aula.__mro__:
        if "clave" in klass.__dict__:
            descriptor = klass.__dict__["clave"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan::grupo_is_not_abstract():
    assert not inspect.isabstract(itculiacan::Grupo)


def test_itculiacan::grupo_constructor_exists():
    assert callable(itculiacan::Grupo.__init__)


def test_itculiacan::grupo_constructor_args():
    sig = inspect.signature(itculiacan::Grupo.__init__)
    params = list(sig.parameters.keys())
    assert "clave" in params, "Missing parameter 'clave'"

def test_itculiacan::grupo_has_clave():
    assert hasattr(itculiacan::Grupo, "clave")
    descriptor = None
    for klass in itculiacan::Grupo.__mro__:
        if "clave" in klass.__dict__:
            descriptor = klass.__dict__["clave"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan::planestudio_is_not_abstract():
    assert not inspect.isabstract(itculiacan::PlanEstudio)


def test_itculiacan::planestudio_constructor_exists():
    assert callable(itculiacan::PlanEstudio.__init__)


def test_itculiacan::planestudio_constructor_args():
    sig = inspect.signature(itculiacan::PlanEstudio.__init__)
    params = list(sig.parameters.keys())
    assert "clave" in params, "Missing parameter 'clave'"
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_itculiacan::planestudio_has_clave():
    assert hasattr(itculiacan::PlanEstudio, "clave")
    descriptor = None
    for klass in itculiacan::PlanEstudio.__mro__:
        if "clave" in klass.__dict__:
            descriptor = klass.__dict__["clave"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan::planestudio_has_nombre():
    assert hasattr(itculiacan::PlanEstudio, "nombre")
    descriptor = None
    for klass in itculiacan::PlanEstudio.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan::generacion_is_not_abstract():
    assert not inspect.isabstract(itculiacan::Generacion)


def test_itculiacan::generacion_constructor_exists():
    assert callable(itculiacan::Generacion.__init__)


def test_itculiacan::generacion_constructor_args():
    sig = inspect.signature(itculiacan::Generacion.__init__)
    params = list(sig.parameters.keys())
    assert "fechaInicio" in params, "Missing parameter 'fechaInicio'"
    assert "fechaFin" in params, "Missing parameter 'fechaFin'"

def test_itculiacan::generacion_has_fechaInicio():
    assert hasattr(itculiacan::Generacion, "fechaInicio")
    descriptor = None
    for klass in itculiacan::Generacion.__mro__:
        if "fechaInicio" in klass.__dict__:
            descriptor = klass.__dict__["fechaInicio"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan::generacion_has_fechaFin():
    assert hasattr(itculiacan::Generacion, "fechaFin")
    descriptor = None
    for klass in itculiacan::Generacion.__mro__:
        if "fechaFin" in klass.__dict__:
            descriptor = klass.__dict__["fechaFin"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan::alumno_is_not_abstract():
    assert not inspect.isabstract(itculiacan::Alumno)


def test_itculiacan::alumno_constructor_exists():
    assert callable(itculiacan::Alumno.__init__)


def test_itculiacan::alumno_constructor_args():
    sig = inspect.signature(itculiacan::Alumno.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "numeroControl" in params, "Missing parameter 'numeroControl'"

def test_itculiacan::alumno_has_nombre():
    assert hasattr(itculiacan::Alumno, "nombre")
    descriptor = None
    for klass in itculiacan::Alumno.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan::alumno_has_numeroControl():
    assert hasattr(itculiacan::Alumno, "numeroControl")
    descriptor = None
    for klass in itculiacan::Alumno.__mro__:
        if "numeroControl" in klass.__dict__:
            descriptor = klass.__dict__["numeroControl"]
            break
    assert isinstance(descriptor, property)

def test_nombramiento_exists():
    # Check that the Enumeration exists
    assert Nombramiento is not None

def test_nombramiento_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Nombramiento]
    expected_literals = [
        "tiempoCompleto",
        "medioTiempo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Nombramiento"


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
itculiacan::Universidad_strategy = st.builds(
    itculiacan::Universidad,
)
itculiacan::Profesor_strategy = st.builds(
    itculiacan::Profesor,
    nombre=
        safe_text,
    nombramiento=
        safe_text,
    clave=
        st.integers(),
    numeroMaterias=
        st.integers()
)
itculiacan::Materia_strategy = st.builds(
    itculiacan::Materia,
    nombre=
        safe_text,
    clave=
        st.integers()
)
itculiacan::Aula_strategy = st.builds(
    itculiacan::Aula,
    capacidad=
        st.integers(),
    clave=
        st.integers()
)
itculiacan::Grupo_strategy = st.builds(
    itculiacan::Grupo,
    clave=
        st.integers()
)
itculiacan::PlanEstudio_strategy = st.builds(
    itculiacan::PlanEstudio,
    clave=
        st.integers(),
    nombre=
        safe_text
)
itculiacan::Generacion_strategy = st.builds(
    itculiacan::Generacion,
    fechaInicio=
        st.dates(),
    fechaFin=
        st.dates()
)
itculiacan::Alumno_strategy = st.builds(
    itculiacan::Alumno,
    nombre=
        safe_text,
    numeroControl=
        st.integers()
)

@given(instance=itculiacan::Universidad_strategy)
@settings(max_examples=50)
def test_itculiacan::universidad_instantiation(instance):
    assert isinstance(instance, itculiacan::Universidad)

@given(instance=itculiacan::Profesor_strategy)
@settings(max_examples=50)
def test_itculiacan::profesor_instantiation(instance):
    assert isinstance(instance, itculiacan::Profesor)

@given(instance=itculiacan::Profesor_strategy)
def test_itculiacan::profesor_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=itculiacan::Profesor_strategy)
def test_itculiacan::profesor_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=itculiacan::Profesor_strategy)
def test_itculiacan::profesor_nombramiento_type(instance):
    assert isinstance(instance.nombramiento, str)


@given(instance=itculiacan::Profesor_strategy)
def test_itculiacan::profesor_nombramiento_setter(instance):
    original = instance.nombramiento
    instance.nombramiento = original
    assert instance.nombramiento == original

@given(instance=itculiacan::Profesor_strategy)
def test_itculiacan::profesor_clave_type(instance):
    assert isinstance(instance.clave, int)


@given(instance=itculiacan::Profesor_strategy)
def test_itculiacan::profesor_clave_setter(instance):
    original = instance.clave
    instance.clave = original
    assert instance.clave == original

@given(instance=itculiacan::Profesor_strategy)
def test_itculiacan::profesor_numeroMaterias_type(instance):
    assert isinstance(instance.numeroMaterias, int)


@given(instance=itculiacan::Profesor_strategy)
def test_itculiacan::profesor_numeroMaterias_setter(instance):
    original = instance.numeroMaterias
    instance.numeroMaterias = original
    assert instance.numeroMaterias == original

@given(instance=itculiacan::Materia_strategy)
@settings(max_examples=50)
def test_itculiacan::materia_instantiation(instance):
    assert isinstance(instance, itculiacan::Materia)

@given(instance=itculiacan::Materia_strategy)
def test_itculiacan::materia_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=itculiacan::Materia_strategy)
def test_itculiacan::materia_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=itculiacan::Materia_strategy)
def test_itculiacan::materia_clave_type(instance):
    assert isinstance(instance.clave, int)


@given(instance=itculiacan::Materia_strategy)
def test_itculiacan::materia_clave_setter(instance):
    original = instance.clave
    instance.clave = original
    assert instance.clave == original

@given(instance=itculiacan::Aula_strategy)
@settings(max_examples=50)
def test_itculiacan::aula_instantiation(instance):
    assert isinstance(instance, itculiacan::Aula)

@given(instance=itculiacan::Aula_strategy)
def test_itculiacan::aula_capacidad_type(instance):
    assert isinstance(instance.capacidad, int)


@given(instance=itculiacan::Aula_strategy)
def test_itculiacan::aula_capacidad_setter(instance):
    original = instance.capacidad
    instance.capacidad = original
    assert instance.capacidad == original

@given(instance=itculiacan::Aula_strategy)
def test_itculiacan::aula_clave_type(instance):
    assert isinstance(instance.clave, int)


@given(instance=itculiacan::Aula_strategy)
def test_itculiacan::aula_clave_setter(instance):
    original = instance.clave
    instance.clave = original
    assert instance.clave == original

@given(instance=itculiacan::Grupo_strategy)
@settings(max_examples=50)
def test_itculiacan::grupo_instantiation(instance):
    assert isinstance(instance, itculiacan::Grupo)

@given(instance=itculiacan::Grupo_strategy)
def test_itculiacan::grupo_clave_type(instance):
    assert isinstance(instance.clave, int)


@given(instance=itculiacan::Grupo_strategy)
def test_itculiacan::grupo_clave_setter(instance):
    original = instance.clave
    instance.clave = original
    assert instance.clave == original

@given(instance=itculiacan::PlanEstudio_strategy)
@settings(max_examples=50)
def test_itculiacan::planestudio_instantiation(instance):
    assert isinstance(instance, itculiacan::PlanEstudio)

@given(instance=itculiacan::PlanEstudio_strategy)
def test_itculiacan::planestudio_clave_type(instance):
    assert isinstance(instance.clave, int)


@given(instance=itculiacan::PlanEstudio_strategy)
def test_itculiacan::planestudio_clave_setter(instance):
    original = instance.clave
    instance.clave = original
    assert instance.clave == original

@given(instance=itculiacan::PlanEstudio_strategy)
def test_itculiacan::planestudio_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=itculiacan::PlanEstudio_strategy)
def test_itculiacan::planestudio_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=itculiacan::Generacion_strategy)
@settings(max_examples=50)
def test_itculiacan::generacion_instantiation(instance):
    assert isinstance(instance, itculiacan::Generacion)

@given(instance=itculiacan::Generacion_strategy)
def test_itculiacan::generacion_fechaInicio_type(instance):
    assert isinstance(instance.fechaInicio, date)


@given(instance=itculiacan::Generacion_strategy)
def test_itculiacan::generacion_fechaInicio_setter(instance):
    original = instance.fechaInicio
    instance.fechaInicio = original
    assert instance.fechaInicio == original

@given(instance=itculiacan::Generacion_strategy)
def test_itculiacan::generacion_fechaFin_type(instance):
    assert isinstance(instance.fechaFin, date)


@given(instance=itculiacan::Generacion_strategy)
def test_itculiacan::generacion_fechaFin_setter(instance):
    original = instance.fechaFin
    instance.fechaFin = original
    assert instance.fechaFin == original

@given(instance=itculiacan::Alumno_strategy)
@settings(max_examples=50)
def test_itculiacan::alumno_instantiation(instance):
    assert isinstance(instance, itculiacan::Alumno)

@given(instance=itculiacan::Alumno_strategy)
def test_itculiacan::alumno_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=itculiacan::Alumno_strategy)
def test_itculiacan::alumno_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=itculiacan::Alumno_strategy)
def test_itculiacan::alumno_numeroControl_type(instance):
    assert isinstance(instance.numeroControl, int)


@given(instance=itculiacan::Alumno_strategy)
def test_itculiacan::alumno_numeroControl_setter(instance):
    original = instance.numeroControl
    instance.numeroControl = original
    assert instance.numeroControl == original
