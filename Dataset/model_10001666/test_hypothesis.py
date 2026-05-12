import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Caninos2,
    Empresa2,
    Caninos1,
    Empresa1,
    double,
    int,
    Caninos,
    Empresa,
    Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase,
    Calcular_el_numero_ejemplar_por_raza__UseCase,
    Calcular_el_ejemplear_por_nombre__UseCase,
    Desplazarse_hasta_el_ultimo_ejemplar_UseCase,
    Desplazarse_hasta_el_primer_ejemplar__UseCase,
    Regresar_hacia_el_anterior_ejemplar_UseCase,
    Avanzar_hasta_el_siguiente_ejemplar__UseCase,
    Visualizar_Hoja_de_vida_de_los_caninos__UseCase,
    Usuario__Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_caninos2_is_not_abstract():
    assert not inspect.isabstract(Caninos2)


def test_caninos2_constructor_exists():
    assert callable(Caninos2.__init__)


def test_caninos2_constructor_args():
    sig = inspect.signature(Caninos2.__init__)
    params = list(sig.parameters.keys())



def test_empresa2_is_not_abstract():
    assert not inspect.isabstract(Empresa2)


def test_empresa2_constructor_exists():
    assert callable(Empresa2.__init__)


def test_empresa2_constructor_args():
    sig = inspect.signature(Empresa2.__init__)
    params = list(sig.parameters.keys())



def test_caninos1_is_not_abstract():
    assert not inspect.isabstract(Caninos1)


def test_caninos1_constructor_exists():
    assert callable(Caninos1.__init__)


def test_caninos1_constructor_args():
    sig = inspect.signature(Caninos1.__init__)
    params = list(sig.parameters.keys())
    assert "observaciones" in params, "Missing parameter 'observaciones'"
    assert "edad" in params, "Missing parameter 'edad'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "raza" in params, "Missing parameter 'raza'"
    assert "altura" in params, "Missing parameter 'altura'"
    assert "peso" in params, "Missing parameter 'peso'"

def test_caninos1_has_observaciones():
    assert hasattr(Caninos1, "observaciones")
    descriptor = None
    for klass in Caninos1.__mro__:
        if "observaciones" in klass.__dict__:
            descriptor = klass.__dict__["observaciones"]
            break
    assert isinstance(descriptor, property)

def test_caninos1_has_edad():
    assert hasattr(Caninos1, "edad")
    descriptor = None
    for klass in Caninos1.__mro__:
        if "edad" in klass.__dict__:
            descriptor = klass.__dict__["edad"]
            break
    assert isinstance(descriptor, property)

def test_caninos1_has_nombre():
    assert hasattr(Caninos1, "nombre")
    descriptor = None
    for klass in Caninos1.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_caninos1_has_raza():
    assert hasattr(Caninos1, "raza")
    descriptor = None
    for klass in Caninos1.__mro__:
        if "raza" in klass.__dict__:
            descriptor = klass.__dict__["raza"]
            break
    assert isinstance(descriptor, property)

def test_caninos1_has_altura():
    assert hasattr(Caninos1, "altura")
    descriptor = None
    for klass in Caninos1.__mro__:
        if "altura" in klass.__dict__:
            descriptor = klass.__dict__["altura"]
            break
    assert isinstance(descriptor, property)

def test_caninos1_has_peso():
    assert hasattr(Caninos1, "peso")
    descriptor = None
    for klass in Caninos1.__mro__:
        if "peso" in klass.__dict__:
            descriptor = klass.__dict__["peso"]
            break
    assert isinstance(descriptor, property)



def test_empresa1_is_not_abstract():
    assert not inspect.isabstract(Empresa1)


def test_empresa1_constructor_exists():
    assert callable(Empresa1.__init__)


def test_empresa1_constructor_args():
    sig = inspect.signature(Empresa1.__init__)
    params = list(sig.parameters.keys())



def test_double_is_not_abstract():
    assert not inspect.isabstract(double)


def test_double_constructor_exists():
    assert callable(double.__init__)


def test_double_constructor_args():
    sig = inspect.signature(double.__init__)
    params = list(sig.parameters.keys())



def test_int_is_not_abstract():
    assert not inspect.isabstract(int)


def test_int_constructor_exists():
    assert callable(int.__init__)


def test_int_constructor_args():
    sig = inspect.signature(int.__init__)
    params = list(sig.parameters.keys())



def test_caninos_is_not_abstract():
    assert not inspect.isabstract(Caninos)


def test_caninos_constructor_exists():
    assert callable(Caninos.__init__)


def test_caninos_constructor_args():
    sig = inspect.signature(Caninos.__init__)
    params = list(sig.parameters.keys())
    assert "altura" in params, "Missing parameter 'altura'"
    assert "raza" in params, "Missing parameter 'raza'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "peso" in params, "Missing parameter 'peso'"
    assert "observaciones" in params, "Missing parameter 'observaciones'"
    assert "edad" in params, "Missing parameter 'edad'"

def test_caninos_has_altura():
    assert hasattr(Caninos, "altura")
    descriptor = None
    for klass in Caninos.__mro__:
        if "altura" in klass.__dict__:
            descriptor = klass.__dict__["altura"]
            break
    assert isinstance(descriptor, property)

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

def test_caninos_has_peso():
    assert hasattr(Caninos, "peso")
    descriptor = None
    for klass in Caninos.__mro__:
        if "peso" in klass.__dict__:
            descriptor = klass.__dict__["peso"]
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

def test_caninos_has_edad():
    assert hasattr(Caninos, "edad")
    descriptor = None
    for klass in Caninos.__mro__:
        if "edad" in klass.__dict__:
            descriptor = klass.__dict__["edad"]
            break
    assert isinstance(descriptor, property)



def test_empresa_is_not_abstract():
    assert not inspect.isabstract(Empresa)


def test_empresa_constructor_exists():
    assert callable(Empresa.__init__)


def test_empresa_constructor_args():
    sig = inspect.signature(Empresa.__init__)
    params = list(sig.parameters.keys())
    assert "getImagen" in params, "Missing parameter 'getImagen'"
    assert "Caninos_BuscarCanino" in params, "Missing parameter 'Caninos_BuscarCanino'"
    assert "getCaninos1" in params, "Missing parameter 'getCaninos1'"
    assert "ArrayList" in params, "Missing parameter 'ArrayList'"
    assert "Empresa" in params, "Missing parameter 'Empresa'"
    assert "getCaninos4" in params, "Missing parameter 'getCaninos4'"
    assert "setImagen" in params, "Missing parameter 'setImagen'"
    assert "getCaninos2" in params, "Missing parameter 'getCaninos2'"
    assert "Caninos_informacion" in params, "Missing parameter 'Caninos_informacion'"
    assert "getCaninos" in params, "Missing parameter 'getCaninos'"
    assert "agregarCaninos" in params, "Missing parameter 'agregarCaninos'"
    assert "nuevoCanino" in params, "Missing parameter 'nuevoCanino'"
    assert "getCaninos5" in params, "Missing parameter 'getCaninos5'"
    assert "getCaninos3" in params, "Missing parameter 'getCaninos3'"
    assert "cantidadRazaCanina" in params, "Missing parameter 'cantidadRazaCanina'"

def test_empresa_has_getImagen():
    assert hasattr(Empresa, "getImagen")
    descriptor = None
    for klass in Empresa.__mro__:
        if "getImagen" in klass.__dict__:
            descriptor = klass.__dict__["getImagen"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_Caninos_BuscarCanino():
    assert hasattr(Empresa, "Caninos_BuscarCanino")
    descriptor = None
    for klass in Empresa.__mro__:
        if "Caninos_BuscarCanino" in klass.__dict__:
            descriptor = klass.__dict__["Caninos_BuscarCanino"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_getCaninos1():
    assert hasattr(Empresa, "getCaninos1")
    descriptor = None
    for klass in Empresa.__mro__:
        if "getCaninos1" in klass.__dict__:
            descriptor = klass.__dict__["getCaninos1"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_ArrayList():
    assert hasattr(Empresa, "ArrayList")
    descriptor = None
    for klass in Empresa.__mro__:
        if "ArrayList" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_Empresa():
    assert hasattr(Empresa, "Empresa")
    descriptor = None
    for klass in Empresa.__mro__:
        if "Empresa" in klass.__dict__:
            descriptor = klass.__dict__["Empresa"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_getCaninos4():
    assert hasattr(Empresa, "getCaninos4")
    descriptor = None
    for klass in Empresa.__mro__:
        if "getCaninos4" in klass.__dict__:
            descriptor = klass.__dict__["getCaninos4"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_setImagen():
    assert hasattr(Empresa, "setImagen")
    descriptor = None
    for klass in Empresa.__mro__:
        if "setImagen" in klass.__dict__:
            descriptor = klass.__dict__["setImagen"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_getCaninos2():
    assert hasattr(Empresa, "getCaninos2")
    descriptor = None
    for klass in Empresa.__mro__:
        if "getCaninos2" in klass.__dict__:
            descriptor = klass.__dict__["getCaninos2"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_Caninos_informacion():
    assert hasattr(Empresa, "Caninos_informacion")
    descriptor = None
    for klass in Empresa.__mro__:
        if "Caninos_informacion" in klass.__dict__:
            descriptor = klass.__dict__["Caninos_informacion"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_getCaninos():
    assert hasattr(Empresa, "getCaninos")
    descriptor = None
    for klass in Empresa.__mro__:
        if "getCaninos" in klass.__dict__:
            descriptor = klass.__dict__["getCaninos"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_agregarCaninos():
    assert hasattr(Empresa, "agregarCaninos")
    descriptor = None
    for klass in Empresa.__mro__:
        if "agregarCaninos" in klass.__dict__:
            descriptor = klass.__dict__["agregarCaninos"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_nuevoCanino():
    assert hasattr(Empresa, "nuevoCanino")
    descriptor = None
    for klass in Empresa.__mro__:
        if "nuevoCanino" in klass.__dict__:
            descriptor = klass.__dict__["nuevoCanino"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_getCaninos5():
    assert hasattr(Empresa, "getCaninos5")
    descriptor = None
    for klass in Empresa.__mro__:
        if "getCaninos5" in klass.__dict__:
            descriptor = klass.__dict__["getCaninos5"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_getCaninos3():
    assert hasattr(Empresa, "getCaninos3")
    descriptor = None
    for klass in Empresa.__mro__:
        if "getCaninos3" in klass.__dict__:
            descriptor = klass.__dict__["getCaninos3"]
            break
    assert isinstance(descriptor, property)

def test_empresa_has_cantidadRazaCanina():
    assert hasattr(Empresa, "cantidadRazaCanina")
    descriptor = None
    for klass in Empresa.__mro__:
        if "cantidadRazaCanina" in klass.__dict__:
            descriptor = klass.__dict__["cantidadRazaCanina"]
            break
    assert isinstance(descriptor, property)



def test_calcular_el_primedio_de_edad_de_los_ejemplares__usecase_is_not_abstract():
    assert not inspect.isabstract(Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase)


def test_calcular_el_primedio_de_edad_de_los_ejemplares__usecase_constructor_exists():
    assert callable(Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase.__init__)


def test_calcular_el_primedio_de_edad_de_los_ejemplares__usecase_constructor_args():
    sig = inspect.signature(Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_calcular_el_numero_ejemplar_por_raza__usecase_is_not_abstract():
    assert not inspect.isabstract(Calcular_el_numero_ejemplar_por_raza__UseCase)


def test_calcular_el_numero_ejemplar_por_raza__usecase_constructor_exists():
    assert callable(Calcular_el_numero_ejemplar_por_raza__UseCase.__init__)


def test_calcular_el_numero_ejemplar_por_raza__usecase_constructor_args():
    sig = inspect.signature(Calcular_el_numero_ejemplar_por_raza__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_calcular_el_ejemplear_por_nombre__usecase_is_not_abstract():
    assert not inspect.isabstract(Calcular_el_ejemplear_por_nombre__UseCase)


def test_calcular_el_ejemplear_por_nombre__usecase_constructor_exists():
    assert callable(Calcular_el_ejemplear_por_nombre__UseCase.__init__)


def test_calcular_el_ejemplear_por_nombre__usecase_constructor_args():
    sig = inspect.signature(Calcular_el_ejemplear_por_nombre__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_desplazarse_hasta_el_ultimo_ejemplar_usecase_is_not_abstract():
    assert not inspect.isabstract(Desplazarse_hasta_el_ultimo_ejemplar_UseCase)


def test_desplazarse_hasta_el_ultimo_ejemplar_usecase_constructor_exists():
    assert callable(Desplazarse_hasta_el_ultimo_ejemplar_UseCase.__init__)


def test_desplazarse_hasta_el_ultimo_ejemplar_usecase_constructor_args():
    sig = inspect.signature(Desplazarse_hasta_el_ultimo_ejemplar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_desplazarse_hasta_el_primer_ejemplar__usecase_is_not_abstract():
    assert not inspect.isabstract(Desplazarse_hasta_el_primer_ejemplar__UseCase)


def test_desplazarse_hasta_el_primer_ejemplar__usecase_constructor_exists():
    assert callable(Desplazarse_hasta_el_primer_ejemplar__UseCase.__init__)


def test_desplazarse_hasta_el_primer_ejemplar__usecase_constructor_args():
    sig = inspect.signature(Desplazarse_hasta_el_primer_ejemplar__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_regresar_hacia_el_anterior_ejemplar_usecase_is_not_abstract():
    assert not inspect.isabstract(Regresar_hacia_el_anterior_ejemplar_UseCase)


def test_regresar_hacia_el_anterior_ejemplar_usecase_constructor_exists():
    assert callable(Regresar_hacia_el_anterior_ejemplar_UseCase.__init__)


def test_regresar_hacia_el_anterior_ejemplar_usecase_constructor_args():
    sig = inspect.signature(Regresar_hacia_el_anterior_ejemplar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_avanzar_hasta_el_siguiente_ejemplar__usecase_is_not_abstract():
    assert not inspect.isabstract(Avanzar_hasta_el_siguiente_ejemplar__UseCase)


def test_avanzar_hasta_el_siguiente_ejemplar__usecase_constructor_exists():
    assert callable(Avanzar_hasta_el_siguiente_ejemplar__UseCase.__init__)


def test_avanzar_hasta_el_siguiente_ejemplar__usecase_constructor_args():
    sig = inspect.signature(Avanzar_hasta_el_siguiente_ejemplar__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_visualizar_hoja_de_vida_de_los_caninos__usecase_is_not_abstract():
    assert not inspect.isabstract(Visualizar_Hoja_de_vida_de_los_caninos__UseCase)


def test_visualizar_hoja_de_vida_de_los_caninos__usecase_constructor_exists():
    assert callable(Visualizar_Hoja_de_vida_de_los_caninos__UseCase.__init__)


def test_visualizar_hoja_de_vida_de_los_caninos__usecase_constructor_args():
    sig = inspect.signature(Visualizar_Hoja_de_vida_de_los_caninos__UseCase.__init__)
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
Caninos2_strategy = st.builds(
    Caninos2,
)
Empresa2_strategy = st.builds(
    Empresa2,
)
Caninos1_strategy = st.builds(
    Caninos1,
    observaciones=
        safe_text,
    edad=
        st.integers(),
    nombre=
        safe_text,
    raza=
        safe_text,
    altura=
        st.none(),
    peso=
        st.integers()
)
Empresa1_strategy = st.builds(
    Empresa1,
)
double_strategy = st.builds(
    double,
)
int_strategy = st.builds(
    int,
)
Caninos_strategy = st.builds(
    Caninos,
    altura=
        st.none(),
    raza=
        safe_text,
    nombre=
        safe_text,
    peso=
        st.integers(),
    observaciones=
        safe_text,
    edad=
        st.integers()
)
Empresa_strategy = st.builds(
    Empresa,
    getImagen=
        st.integers(),
    Caninos_BuscarCanino=
        safe_text,
    getCaninos1=
        st.integers(),
    ArrayList=
        st.none(),
    Empresa=
        safe_text,
    getCaninos4=
        safe_text,
    setImagen=
        safe_text,
    getCaninos2=
        safe_text,
    Caninos_informacion=
        safe_text,
    getCaninos=
        safe_text,
    agregarCaninos=
        safe_text,
    nuevoCanino=
        safe_text,
    getCaninos5=
        safe_text,
    getCaninos3=
        safe_text,
    cantidadRazaCanina=
        st.none()
)
Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase_strategy = st.builds(
    Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase,
)
Calcular_el_numero_ejemplar_por_raza__UseCase_strategy = st.builds(
    Calcular_el_numero_ejemplar_por_raza__UseCase,
)
Calcular_el_ejemplear_por_nombre__UseCase_strategy = st.builds(
    Calcular_el_ejemplear_por_nombre__UseCase,
)
Desplazarse_hasta_el_ultimo_ejemplar_UseCase_strategy = st.builds(
    Desplazarse_hasta_el_ultimo_ejemplar_UseCase,
)
Desplazarse_hasta_el_primer_ejemplar__UseCase_strategy = st.builds(
    Desplazarse_hasta_el_primer_ejemplar__UseCase,
)
Regresar_hacia_el_anterior_ejemplar_UseCase_strategy = st.builds(
    Regresar_hacia_el_anterior_ejemplar_UseCase,
)
Avanzar_hasta_el_siguiente_ejemplar__UseCase_strategy = st.builds(
    Avanzar_hasta_el_siguiente_ejemplar__UseCase,
)
Visualizar_Hoja_de_vida_de_los_caninos__UseCase_strategy = st.builds(
    Visualizar_Hoja_de_vida_de_los_caninos__UseCase,
)
Usuario__Actor_strategy = st.builds(
    Usuario__Actor,
)

@given(instance=Caninos2_strategy)
@settings(max_examples=50)
def test_caninos2_instantiation(instance):
    assert isinstance(instance, Caninos2)

@given(instance=Empresa2_strategy)
@settings(max_examples=50)
def test_empresa2_instantiation(instance):
    assert isinstance(instance, Empresa2)

@given(instance=Caninos1_strategy)
@settings(max_examples=50)
def test_caninos1_instantiation(instance):
    assert isinstance(instance, Caninos1)



@given(instance=Caninos1_strategy)
def test_caninos1_observaciones_setter(instance):
    original = instance.observaciones
    instance.observaciones = original
    assert instance.observaciones == original



@given(instance=Caninos1_strategy)
def test_caninos1_edad_setter(instance):
    original = instance.edad
    instance.edad = original
    assert instance.edad == original



@given(instance=Caninos1_strategy)
def test_caninos1_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Caninos1_strategy)
def test_caninos1_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original



@given(instance=Caninos1_strategy)
def test_caninos1_altura_setter(instance):
    original = instance.altura
    instance.altura = original
    assert instance.altura == original



@given(instance=Caninos1_strategy)
def test_caninos1_peso_setter(instance):
    original = instance.peso
    instance.peso = original
    assert instance.peso == original

@given(instance=Empresa1_strategy)
@settings(max_examples=50)
def test_empresa1_instantiation(instance):
    assert isinstance(instance, Empresa1)

@given(instance=double_strategy)
@settings(max_examples=50)
def test_double_instantiation(instance):
    assert isinstance(instance, double)

@given(instance=int_strategy)
@settings(max_examples=50)
def test_int_instantiation(instance):
    assert isinstance(instance, int)

@given(instance=Caninos_strategy)
@settings(max_examples=50)
def test_caninos_instantiation(instance):
    assert isinstance(instance, Caninos)



@given(instance=Caninos_strategy)
def test_caninos_altura_setter(instance):
    original = instance.altura
    instance.altura = original
    assert instance.altura == original



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
def test_caninos_peso_setter(instance):
    original = instance.peso
    instance.peso = original
    assert instance.peso == original



@given(instance=Caninos_strategy)
def test_caninos_observaciones_setter(instance):
    original = instance.observaciones
    instance.observaciones = original
    assert instance.observaciones == original



@given(instance=Caninos_strategy)
def test_caninos_edad_setter(instance):
    original = instance.edad
    instance.edad = original
    assert instance.edad == original

@given(instance=Empresa_strategy)
@settings(max_examples=50)
def test_empresa_instantiation(instance):
    assert isinstance(instance, Empresa)



@given(instance=Empresa_strategy)
def test_empresa_getImagen_setter(instance):
    original = instance.getImagen
    instance.getImagen = original
    assert instance.getImagen == original



@given(instance=Empresa_strategy)
def test_empresa_Caninos_BuscarCanino_setter(instance):
    original = instance.Caninos_BuscarCanino
    instance.Caninos_BuscarCanino = original
    assert instance.Caninos_BuscarCanino == original



@given(instance=Empresa_strategy)
def test_empresa_getCaninos1_setter(instance):
    original = instance.getCaninos1
    instance.getCaninos1 = original
    assert instance.getCaninos1 == original



@given(instance=Empresa_strategy)
def test_empresa_ArrayList_setter(instance):
    original = instance.ArrayList
    instance.ArrayList = original
    assert instance.ArrayList == original



@given(instance=Empresa_strategy)
def test_empresa_Empresa_setter(instance):
    original = instance.Empresa
    instance.Empresa = original
    assert instance.Empresa == original



@given(instance=Empresa_strategy)
def test_empresa_getCaninos4_setter(instance):
    original = instance.getCaninos4
    instance.getCaninos4 = original
    assert instance.getCaninos4 == original



@given(instance=Empresa_strategy)
def test_empresa_setImagen_setter(instance):
    original = instance.setImagen
    instance.setImagen = original
    assert instance.setImagen == original



@given(instance=Empresa_strategy)
def test_empresa_getCaninos2_setter(instance):
    original = instance.getCaninos2
    instance.getCaninos2 = original
    assert instance.getCaninos2 == original



@given(instance=Empresa_strategy)
def test_empresa_Caninos_informacion_setter(instance):
    original = instance.Caninos_informacion
    instance.Caninos_informacion = original
    assert instance.Caninos_informacion == original



@given(instance=Empresa_strategy)
def test_empresa_getCaninos_setter(instance):
    original = instance.getCaninos
    instance.getCaninos = original
    assert instance.getCaninos == original



@given(instance=Empresa_strategy)
def test_empresa_agregarCaninos_setter(instance):
    original = instance.agregarCaninos
    instance.agregarCaninos = original
    assert instance.agregarCaninos == original



@given(instance=Empresa_strategy)
def test_empresa_nuevoCanino_setter(instance):
    original = instance.nuevoCanino
    instance.nuevoCanino = original
    assert instance.nuevoCanino == original



@given(instance=Empresa_strategy)
def test_empresa_getCaninos5_setter(instance):
    original = instance.getCaninos5
    instance.getCaninos5 = original
    assert instance.getCaninos5 == original



@given(instance=Empresa_strategy)
def test_empresa_getCaninos3_setter(instance):
    original = instance.getCaninos3
    instance.getCaninos3 = original
    assert instance.getCaninos3 == original



@given(instance=Empresa_strategy)
def test_empresa_cantidadRazaCanina_setter(instance):
    original = instance.cantidadRazaCanina
    instance.cantidadRazaCanina = original
    assert instance.cantidadRazaCanina == original

@given(instance=Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase_strategy)
@settings(max_examples=50)
def test_calcular_el_primedio_de_edad_de_los_ejemplares__usecase_instantiation(instance):
    assert isinstance(instance, Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase)

@given(instance=Calcular_el_numero_ejemplar_por_raza__UseCase_strategy)
@settings(max_examples=50)
def test_calcular_el_numero_ejemplar_por_raza__usecase_instantiation(instance):
    assert isinstance(instance, Calcular_el_numero_ejemplar_por_raza__UseCase)

@given(instance=Calcular_el_ejemplear_por_nombre__UseCase_strategy)
@settings(max_examples=50)
def test_calcular_el_ejemplear_por_nombre__usecase_instantiation(instance):
    assert isinstance(instance, Calcular_el_ejemplear_por_nombre__UseCase)

@given(instance=Desplazarse_hasta_el_ultimo_ejemplar_UseCase_strategy)
@settings(max_examples=50)
def test_desplazarse_hasta_el_ultimo_ejemplar_usecase_instantiation(instance):
    assert isinstance(instance, Desplazarse_hasta_el_ultimo_ejemplar_UseCase)

@given(instance=Desplazarse_hasta_el_primer_ejemplar__UseCase_strategy)
@settings(max_examples=50)
def test_desplazarse_hasta_el_primer_ejemplar__usecase_instantiation(instance):
    assert isinstance(instance, Desplazarse_hasta_el_primer_ejemplar__UseCase)

@given(instance=Regresar_hacia_el_anterior_ejemplar_UseCase_strategy)
@settings(max_examples=50)
def test_regresar_hacia_el_anterior_ejemplar_usecase_instantiation(instance):
    assert isinstance(instance, Regresar_hacia_el_anterior_ejemplar_UseCase)

@given(instance=Avanzar_hasta_el_siguiente_ejemplar__UseCase_strategy)
@settings(max_examples=50)
def test_avanzar_hasta_el_siguiente_ejemplar__usecase_instantiation(instance):
    assert isinstance(instance, Avanzar_hasta_el_siguiente_ejemplar__UseCase)

@given(instance=Visualizar_Hoja_de_vida_de_los_caninos__UseCase_strategy)
@settings(max_examples=50)
def test_visualizar_hoja_de_vida_de_los_caninos__usecase_instantiation(instance):
    assert isinstance(instance, Visualizar_Hoja_de_vida_de_los_caninos__UseCase)

@given(instance=Usuario__Actor_strategy)
@settings(max_examples=50)
def test_usuario__actor_instantiation(instance):
    assert isinstance(instance, Usuario__Actor)
