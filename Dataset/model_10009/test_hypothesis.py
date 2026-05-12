import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    itculiacan_Universidad,
    itculiacan_Profesor,
    itculiacan_Materia,
    itculiacan_Aula,
    itculiacan_Grupo,
    itculiacan_PlanEstudio,
    itculiacan_Generacion,
    itculiacan_Alumno,
    Nombramiento,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_itculiacan_universidad_is_not_abstract():
    assert not inspect.isabstract(itculiacan_Universidad)


def test_itculiacan_universidad_constructor_exists():
    assert callable(itculiacan_Universidad.__init__)


def test_itculiacan_universidad_constructor_args():
    sig = inspect.signature(itculiacan_Universidad.__init__)
    params = list(sig.parameters.keys())



def test_itculiacan_profesor_is_not_abstract():
    assert not inspect.isabstract(itculiacan_Profesor)


def test_itculiacan_profesor_constructor_exists():
    assert callable(itculiacan_Profesor.__init__)


def test_itculiacan_profesor_constructor_args():
    sig = inspect.signature(itculiacan_Profesor.__init__)
    params = list(sig.parameters.keys())
    assert "numeroMaterias" in params, "Missing parameter 'numeroMaterias'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "clave" in params, "Missing parameter 'clave'"
    assert "nombramiento" in params, "Missing parameter 'nombramiento'"

def test_itculiacan_profesor_has_numeroMaterias():
    assert hasattr(itculiacan_Profesor, "numeroMaterias")
    descriptor = None
    for klass in itculiacan_Profesor.__mro__:
        if "numeroMaterias" in klass.__dict__:
            descriptor = klass.__dict__["numeroMaterias"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan_profesor_has_nombre():
    assert hasattr(itculiacan_Profesor, "nombre")
    descriptor = None
    for klass in itculiacan_Profesor.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan_profesor_has_clave():
    assert hasattr(itculiacan_Profesor, "clave")
    descriptor = None
    for klass in itculiacan_Profesor.__mro__:
        if "clave" in klass.__dict__:
            descriptor = klass.__dict__["clave"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan_profesor_has_nombramiento():
    assert hasattr(itculiacan_Profesor, "nombramiento")
    descriptor = None
    for klass in itculiacan_Profesor.__mro__:
        if "nombramiento" in klass.__dict__:
            descriptor = klass.__dict__["nombramiento"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan_materia_is_not_abstract():
    assert not inspect.isabstract(itculiacan_Materia)


def test_itculiacan_materia_constructor_exists():
    assert callable(itculiacan_Materia.__init__)


def test_itculiacan_materia_constructor_args():
    sig = inspect.signature(itculiacan_Materia.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "clave" in params, "Missing parameter 'clave'"

def test_itculiacan_materia_has_nombre():
    assert hasattr(itculiacan_Materia, "nombre")
    descriptor = None
    for klass in itculiacan_Materia.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan_materia_has_clave():
    assert hasattr(itculiacan_Materia, "clave")
    descriptor = None
    for klass in itculiacan_Materia.__mro__:
        if "clave" in klass.__dict__:
            descriptor = klass.__dict__["clave"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan_aula_is_not_abstract():
    assert not inspect.isabstract(itculiacan_Aula)


def test_itculiacan_aula_constructor_exists():
    assert callable(itculiacan_Aula.__init__)


def test_itculiacan_aula_constructor_args():
    sig = inspect.signature(itculiacan_Aula.__init__)
    params = list(sig.parameters.keys())
    assert "clave" in params, "Missing parameter 'clave'"
    assert "capacidad" in params, "Missing parameter 'capacidad'"

def test_itculiacan_aula_has_clave():
    assert hasattr(itculiacan_Aula, "clave")
    descriptor = None
    for klass in itculiacan_Aula.__mro__:
        if "clave" in klass.__dict__:
            descriptor = klass.__dict__["clave"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan_aula_has_capacidad():
    assert hasattr(itculiacan_Aula, "capacidad")
    descriptor = None
    for klass in itculiacan_Aula.__mro__:
        if "capacidad" in klass.__dict__:
            descriptor = klass.__dict__["capacidad"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan_grupo_is_not_abstract():
    assert not inspect.isabstract(itculiacan_Grupo)


def test_itculiacan_grupo_constructor_exists():
    assert callable(itculiacan_Grupo.__init__)


def test_itculiacan_grupo_constructor_args():
    sig = inspect.signature(itculiacan_Grupo.__init__)
    params = list(sig.parameters.keys())
    assert "clave" in params, "Missing parameter 'clave'"

def test_itculiacan_grupo_has_clave():
    assert hasattr(itculiacan_Grupo, "clave")
    descriptor = None
    for klass in itculiacan_Grupo.__mro__:
        if "clave" in klass.__dict__:
            descriptor = klass.__dict__["clave"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan_planestudio_is_not_abstract():
    assert not inspect.isabstract(itculiacan_PlanEstudio)


def test_itculiacan_planestudio_constructor_exists():
    assert callable(itculiacan_PlanEstudio.__init__)


def test_itculiacan_planestudio_constructor_args():
    sig = inspect.signature(itculiacan_PlanEstudio.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "clave" in params, "Missing parameter 'clave'"

def test_itculiacan_planestudio_has_nombre():
    assert hasattr(itculiacan_PlanEstudio, "nombre")
    descriptor = None
    for klass in itculiacan_PlanEstudio.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan_planestudio_has_clave():
    assert hasattr(itculiacan_PlanEstudio, "clave")
    descriptor = None
    for klass in itculiacan_PlanEstudio.__mro__:
        if "clave" in klass.__dict__:
            descriptor = klass.__dict__["clave"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan_generacion_is_not_abstract():
    assert not inspect.isabstract(itculiacan_Generacion)


def test_itculiacan_generacion_constructor_exists():
    assert callable(itculiacan_Generacion.__init__)


def test_itculiacan_generacion_constructor_args():
    sig = inspect.signature(itculiacan_Generacion.__init__)
    params = list(sig.parameters.keys())
    assert "fechaInicio" in params, "Missing parameter 'fechaInicio'"
    assert "fechaFin" in params, "Missing parameter 'fechaFin'"

def test_itculiacan_generacion_has_fechaInicio():
    assert hasattr(itculiacan_Generacion, "fechaInicio")
    descriptor = None
    for klass in itculiacan_Generacion.__mro__:
        if "fechaInicio" in klass.__dict__:
            descriptor = klass.__dict__["fechaInicio"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan_generacion_has_fechaFin():
    assert hasattr(itculiacan_Generacion, "fechaFin")
    descriptor = None
    for klass in itculiacan_Generacion.__mro__:
        if "fechaFin" in klass.__dict__:
            descriptor = klass.__dict__["fechaFin"]
            break
    assert isinstance(descriptor, property)



def test_itculiacan_alumno_is_not_abstract():
    assert not inspect.isabstract(itculiacan_Alumno)


def test_itculiacan_alumno_constructor_exists():
    assert callable(itculiacan_Alumno.__init__)


def test_itculiacan_alumno_constructor_args():
    sig = inspect.signature(itculiacan_Alumno.__init__)
    params = list(sig.parameters.keys())
    assert "numeroControl" in params, "Missing parameter 'numeroControl'"
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_itculiacan_alumno_has_numeroControl():
    assert hasattr(itculiacan_Alumno, "numeroControl")
    descriptor = None
    for klass in itculiacan_Alumno.__mro__:
        if "numeroControl" in klass.__dict__:
            descriptor = klass.__dict__["numeroControl"]
            break
    assert isinstance(descriptor, property)

def test_itculiacan_alumno_has_nombre():
    assert hasattr(itculiacan_Alumno, "nombre")
    descriptor = None
    for klass in itculiacan_Alumno.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
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
itculiacan_Universidad_strategy = st.builds(
    itculiacan_Universidad,
)
itculiacan_Profesor_strategy = st.builds(
    itculiacan_Profesor,
    numeroMaterias=
        st.integers(),
    nombre=
        safe_text,
    clave=
        st.integers(),
    nombramiento=
        safe_text
)
itculiacan_Materia_strategy = st.builds(
    itculiacan_Materia,
    nombre=
        safe_text,
    clave=
        st.integers()
)
itculiacan_Aula_strategy = st.builds(
    itculiacan_Aula,
    clave=
        st.integers(),
    capacidad=
        st.integers()
)
itculiacan_Grupo_strategy = st.builds(
    itculiacan_Grupo,
    clave=
        st.integers()
)
itculiacan_PlanEstudio_strategy = st.builds(
    itculiacan_PlanEstudio,
    nombre=
        safe_text,
    clave=
        st.integers()
)
itculiacan_Generacion_strategy = st.builds(
    itculiacan_Generacion,
    fechaInicio=
        st.dates(),
    fechaFin=
        st.dates()
)
itculiacan_Alumno_strategy = st.builds(
    itculiacan_Alumno,
    numeroControl=
        st.integers(),
    nombre=
        safe_text
)

@given(instance=itculiacan_Universidad_strategy)
@settings(max_examples=50)
def test_itculiacan_universidad_instantiation(instance):
    assert isinstance(instance, itculiacan_Universidad)

@given(instance=itculiacan_Profesor_strategy)
@settings(max_examples=50)
def test_itculiacan_profesor_instantiation(instance):
    assert isinstance(instance, itculiacan_Profesor)



@given(instance=itculiacan_Profesor_strategy)
def test_itculiacan_profesor_numeroMaterias_setter(instance):
    original = instance.numeroMaterias
    instance.numeroMaterias = original
    assert instance.numeroMaterias == original



@given(instance=itculiacan_Profesor_strategy)
def test_itculiacan_profesor_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=itculiacan_Profesor_strategy)
def test_itculiacan_profesor_clave_setter(instance):
    original = instance.clave
    instance.clave = original
    assert instance.clave == original



@given(instance=itculiacan_Profesor_strategy)
def test_itculiacan_profesor_nombramiento_setter(instance):
    original = instance.nombramiento
    instance.nombramiento = original
    assert instance.nombramiento == original

@given(instance=itculiacan_Materia_strategy)
@settings(max_examples=50)
def test_itculiacan_materia_instantiation(instance):
    assert isinstance(instance, itculiacan_Materia)



@given(instance=itculiacan_Materia_strategy)
def test_itculiacan_materia_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=itculiacan_Materia_strategy)
def test_itculiacan_materia_clave_setter(instance):
    original = instance.clave
    instance.clave = original
    assert instance.clave == original

@given(instance=itculiacan_Aula_strategy)
@settings(max_examples=50)
def test_itculiacan_aula_instantiation(instance):
    assert isinstance(instance, itculiacan_Aula)



@given(instance=itculiacan_Aula_strategy)
def test_itculiacan_aula_clave_setter(instance):
    original = instance.clave
    instance.clave = original
    assert instance.clave == original



@given(instance=itculiacan_Aula_strategy)
def test_itculiacan_aula_capacidad_setter(instance):
    original = instance.capacidad
    instance.capacidad = original
    assert instance.capacidad == original

@given(instance=itculiacan_Grupo_strategy)
@settings(max_examples=50)
def test_itculiacan_grupo_instantiation(instance):
    assert isinstance(instance, itculiacan_Grupo)



@given(instance=itculiacan_Grupo_strategy)
def test_itculiacan_grupo_clave_setter(instance):
    original = instance.clave
    instance.clave = original
    assert instance.clave == original

@given(instance=itculiacan_PlanEstudio_strategy)
@settings(max_examples=50)
def test_itculiacan_planestudio_instantiation(instance):
    assert isinstance(instance, itculiacan_PlanEstudio)



@given(instance=itculiacan_PlanEstudio_strategy)
def test_itculiacan_planestudio_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=itculiacan_PlanEstudio_strategy)
def test_itculiacan_planestudio_clave_setter(instance):
    original = instance.clave
    instance.clave = original
    assert instance.clave == original

@given(instance=itculiacan_Generacion_strategy)
@settings(max_examples=50)
def test_itculiacan_generacion_instantiation(instance):
    assert isinstance(instance, itculiacan_Generacion)



@given(instance=itculiacan_Generacion_strategy)
def test_itculiacan_generacion_fechaInicio_setter(instance):
    original = instance.fechaInicio
    instance.fechaInicio = original
    assert instance.fechaInicio == original



@given(instance=itculiacan_Generacion_strategy)
def test_itculiacan_generacion_fechaFin_setter(instance):
    original = instance.fechaFin
    instance.fechaFin = original
    assert instance.fechaFin == original

@given(instance=itculiacan_Alumno_strategy)
@settings(max_examples=50)
def test_itculiacan_alumno_instantiation(instance):
    assert isinstance(instance, itculiacan_Alumno)



@given(instance=itculiacan_Alumno_strategy)
def test_itculiacan_alumno_numeroControl_setter(instance):
    original = instance.numeroControl
    instance.numeroControl = original
    assert instance.numeroControl == original



@given(instance=itculiacan_Alumno_strategy)
def test_itculiacan_alumno_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original
