import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    caninos3,
    veterinaria3,
    caninos2,
    veterinaria2,
    caninos1,
    veterinaria1,
    caninos,
    veterinaria,
    _1,
    producto,
    Tienda,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_caninos3_is_not_abstract():
    assert not inspect.isabstract(caninos3)


def test_caninos3_constructor_exists():
    assert callable(caninos3.__init__)


def test_caninos3_constructor_args():
    sig = inspect.signature(caninos3.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "observaciones" in params, "Missing parameter 'observaciones'"
    assert "edad" in params, "Missing parameter 'edad'"
    assert "altura" in params, "Missing parameter 'altura'"
    assert "peso" in params, "Missing parameter 'peso'"
    assert "raza" in params, "Missing parameter 'raza'"

def test_caninos3_has_nombre():
    assert hasattr(caninos3, "nombre")
    descriptor = None
    for klass in caninos3.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_caninos3_has_observaciones():
    assert hasattr(caninos3, "observaciones")
    descriptor = None
    for klass in caninos3.__mro__:
        if "observaciones" in klass.__dict__:
            descriptor = klass.__dict__["observaciones"]
            break
    assert isinstance(descriptor, property)

def test_caninos3_has_edad():
    assert hasattr(caninos3, "edad")
    descriptor = None
    for klass in caninos3.__mro__:
        if "edad" in klass.__dict__:
            descriptor = klass.__dict__["edad"]
            break
    assert isinstance(descriptor, property)

def test_caninos3_has_altura():
    assert hasattr(caninos3, "altura")
    descriptor = None
    for klass in caninos3.__mro__:
        if "altura" in klass.__dict__:
            descriptor = klass.__dict__["altura"]
            break
    assert isinstance(descriptor, property)

def test_caninos3_has_peso():
    assert hasattr(caninos3, "peso")
    descriptor = None
    for klass in caninos3.__mro__:
        if "peso" in klass.__dict__:
            descriptor = klass.__dict__["peso"]
            break
    assert isinstance(descriptor, property)

def test_caninos3_has_raza():
    assert hasattr(caninos3, "raza")
    descriptor = None
    for klass in caninos3.__mro__:
        if "raza" in klass.__dict__:
            descriptor = klass.__dict__["raza"]
            break
    assert isinstance(descriptor, property)



def test_veterinaria3_is_not_abstract():
    assert not inspect.isabstract(veterinaria3)


def test_veterinaria3_constructor_exists():
    assert callable(veterinaria3.__init__)


def test_veterinaria3_constructor_args():
    sig = inspect.signature(veterinaria3.__init__)
    params = list(sig.parameters.keys())
    assert "_attr" in params, "Missing parameter '_attr'"

def test_veterinaria3_has__attr():
    assert hasattr(veterinaria3, "_attr")
    descriptor = None
    for klass in veterinaria3.__mro__:
        if "_attr" in klass.__dict__:
            descriptor = klass.__dict__["_attr"]
            break
    assert isinstance(descriptor, property)



def test_caninos2_is_not_abstract():
    assert not inspect.isabstract(caninos2)


def test_caninos2_constructor_exists():
    assert callable(caninos2.__init__)


def test_caninos2_constructor_args():
    sig = inspect.signature(caninos2.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "altura" in params, "Missing parameter 'altura'"
    assert "raza" in params, "Missing parameter 'raza'"
    assert "observaciones" in params, "Missing parameter 'observaciones'"
    assert "edad" in params, "Missing parameter 'edad'"
    assert "peso" in params, "Missing parameter 'peso'"

def test_caninos2_has_nombre():
    assert hasattr(caninos2, "nombre")
    descriptor = None
    for klass in caninos2.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_caninos2_has_altura():
    assert hasattr(caninos2, "altura")
    descriptor = None
    for klass in caninos2.__mro__:
        if "altura" in klass.__dict__:
            descriptor = klass.__dict__["altura"]
            break
    assert isinstance(descriptor, property)

def test_caninos2_has_raza():
    assert hasattr(caninos2, "raza")
    descriptor = None
    for klass in caninos2.__mro__:
        if "raza" in klass.__dict__:
            descriptor = klass.__dict__["raza"]
            break
    assert isinstance(descriptor, property)

def test_caninos2_has_observaciones():
    assert hasattr(caninos2, "observaciones")
    descriptor = None
    for klass in caninos2.__mro__:
        if "observaciones" in klass.__dict__:
            descriptor = klass.__dict__["observaciones"]
            break
    assert isinstance(descriptor, property)

def test_caninos2_has_edad():
    assert hasattr(caninos2, "edad")
    descriptor = None
    for klass in caninos2.__mro__:
        if "edad" in klass.__dict__:
            descriptor = klass.__dict__["edad"]
            break
    assert isinstance(descriptor, property)

def test_caninos2_has_peso():
    assert hasattr(caninos2, "peso")
    descriptor = None
    for klass in caninos2.__mro__:
        if "peso" in klass.__dict__:
            descriptor = klass.__dict__["peso"]
            break
    assert isinstance(descriptor, property)



def test_veterinaria2_is_not_abstract():
    assert not inspect.isabstract(veterinaria2)


def test_veterinaria2_constructor_exists():
    assert callable(veterinaria2.__init__)


def test_veterinaria2_constructor_args():
    sig = inspect.signature(veterinaria2.__init__)
    params = list(sig.parameters.keys())
    assert "_" in params, "Missing parameter '_'"

def test_veterinaria2_has__():
    assert hasattr(veterinaria2, "_")
    descriptor = None
    for klass in veterinaria2.__mro__:
        if "_" in klass.__dict__:
            descriptor = klass.__dict__["_"]
            break
    assert isinstance(descriptor, property)



def test_caninos1_is_not_abstract():
    assert not inspect.isabstract(caninos1)


def test_caninos1_constructor_exists():
    assert callable(caninos1.__init__)


def test_caninos1_constructor_args():
    sig = inspect.signature(caninos1.__init__)
    params = list(sig.parameters.keys())
    assert "obsercaciones" in params, "Missing parameter 'obsercaciones'"
    assert "altura" in params, "Missing parameter 'altura'"
    assert "edad" in params, "Missing parameter 'edad'"
    assert "peso" in params, "Missing parameter 'peso'"
    assert "raza" in params, "Missing parameter 'raza'"
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_caninos1_has_obsercaciones():
    assert hasattr(caninos1, "obsercaciones")
    descriptor = None
    for klass in caninos1.__mro__:
        if "obsercaciones" in klass.__dict__:
            descriptor = klass.__dict__["obsercaciones"]
            break
    assert isinstance(descriptor, property)

def test_caninos1_has_altura():
    assert hasattr(caninos1, "altura")
    descriptor = None
    for klass in caninos1.__mro__:
        if "altura" in klass.__dict__:
            descriptor = klass.__dict__["altura"]
            break
    assert isinstance(descriptor, property)

def test_caninos1_has_edad():
    assert hasattr(caninos1, "edad")
    descriptor = None
    for klass in caninos1.__mro__:
        if "edad" in klass.__dict__:
            descriptor = klass.__dict__["edad"]
            break
    assert isinstance(descriptor, property)

def test_caninos1_has_peso():
    assert hasattr(caninos1, "peso")
    descriptor = None
    for klass in caninos1.__mro__:
        if "peso" in klass.__dict__:
            descriptor = klass.__dict__["peso"]
            break
    assert isinstance(descriptor, property)

def test_caninos1_has_raza():
    assert hasattr(caninos1, "raza")
    descriptor = None
    for klass in caninos1.__mro__:
        if "raza" in klass.__dict__:
            descriptor = klass.__dict__["raza"]
            break
    assert isinstance(descriptor, property)

def test_caninos1_has_nombre():
    assert hasattr(caninos1, "nombre")
    descriptor = None
    for klass in caninos1.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_veterinaria1_is_not_abstract():
    assert not inspect.isabstract(veterinaria1)


def test_veterinaria1_constructor_exists():
    assert callable(veterinaria1.__init__)


def test_veterinaria1_constructor_args():
    sig = inspect.signature(veterinaria1.__init__)
    params = list(sig.parameters.keys())



def test_caninos_is_not_abstract():
    assert not inspect.isabstract(caninos)


def test_caninos_constructor_exists():
    assert callable(caninos.__init__)


def test_caninos_constructor_args():
    sig = inspect.signature(caninos.__init__)
    params = list(sig.parameters.keys())
    assert "raza" in params, "Missing parameter 'raza'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "peso" in params, "Missing parameter 'peso'"
    assert "altura" in params, "Missing parameter 'altura'"
    assert "observaciones" in params, "Missing parameter 'observaciones'"
    assert "edad" in params, "Missing parameter 'edad'"

def test_caninos_has_raza():
    assert hasattr(caninos, "raza")
    descriptor = None
    for klass in caninos.__mro__:
        if "raza" in klass.__dict__:
            descriptor = klass.__dict__["raza"]
            break
    assert isinstance(descriptor, property)

def test_caninos_has_nombre():
    assert hasattr(caninos, "nombre")
    descriptor = None
    for klass in caninos.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_caninos_has_peso():
    assert hasattr(caninos, "peso")
    descriptor = None
    for klass in caninos.__mro__:
        if "peso" in klass.__dict__:
            descriptor = klass.__dict__["peso"]
            break
    assert isinstance(descriptor, property)

def test_caninos_has_altura():
    assert hasattr(caninos, "altura")
    descriptor = None
    for klass in caninos.__mro__:
        if "altura" in klass.__dict__:
            descriptor = klass.__dict__["altura"]
            break
    assert isinstance(descriptor, property)

def test_caninos_has_observaciones():
    assert hasattr(caninos, "observaciones")
    descriptor = None
    for klass in caninos.__mro__:
        if "observaciones" in klass.__dict__:
            descriptor = klass.__dict__["observaciones"]
            break
    assert isinstance(descriptor, property)

def test_caninos_has_edad():
    assert hasattr(caninos, "edad")
    descriptor = None
    for klass in caninos.__mro__:
        if "edad" in klass.__dict__:
            descriptor = klass.__dict__["edad"]
            break
    assert isinstance(descriptor, property)



def test_veterinaria_is_not_abstract():
    assert not inspect.isabstract(veterinaria)


def test_veterinaria_constructor_exists():
    assert callable(veterinaria.__init__)


def test_veterinaria_constructor_args():
    sig = inspect.signature(veterinaria.__init__)
    params = list(sig.parameters.keys())



def test__1_is_not_abstract():
    assert not inspect.isabstract(_1)


def test__1_constructor_exists():
    assert callable(_1.__init__)


def test__1_constructor_args():
    sig = inspect.signature(_1.__init__)
    params = list(sig.parameters.keys())



def test_producto_is_not_abstract():
    assert not inspect.isabstract(producto)


def test_producto_constructor_exists():
    assert callable(producto.__init__)


def test_producto_constructor_args():
    sig = inspect.signature(producto.__init__)
    params = list(sig.parameters.keys())
    assert "tipo" in params, "Missing parameter 'tipo'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "cantidadVendida" in params, "Missing parameter 'cantidadVendida'"
    assert "SUPERMERCADO" in params, "Missing parameter 'SUPERMERCADO'"
    assert "PAPELERIA" in params, "Missing parameter 'PAPELERIA'"
    assert "IVA_DROGUERIA" in params, "Missing parameter 'IVA_DROGUERIA'"
    assert "cantidadBodega" in params, "Missing parameter 'cantidadBodega'"
    assert "DROGUERIA" in params, "Missing parameter 'DROGUERIA'"
    assert "cantidadMinima" in params, "Missing parameter 'cantidadMinima'"
    assert "IVA_PAPELERIA" in params, "Missing parameter 'IVA_PAPELERIA'"
    assert "precioVenta" in params, "Missing parameter 'precioVenta'"
    assert "IVA_SUPERMERCADO" in params, "Missing parameter 'IVA_SUPERMERCADO'"

def test_producto_has_tipo():
    assert hasattr(producto, "tipo")
    descriptor = None
    for klass in producto.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_nombre():
    assert hasattr(producto, "nombre")
    descriptor = None
    for klass in producto.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_cantidadVendida():
    assert hasattr(producto, "cantidadVendida")
    descriptor = None
    for klass in producto.__mro__:
        if "cantidadVendida" in klass.__dict__:
            descriptor = klass.__dict__["cantidadVendida"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_SUPERMERCADO():
    assert hasattr(producto, "SUPERMERCADO")
    descriptor = None
    for klass in producto.__mro__:
        if "SUPERMERCADO" in klass.__dict__:
            descriptor = klass.__dict__["SUPERMERCADO"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_PAPELERIA():
    assert hasattr(producto, "PAPELERIA")
    descriptor = None
    for klass in producto.__mro__:
        if "PAPELERIA" in klass.__dict__:
            descriptor = klass.__dict__["PAPELERIA"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_IVA_DROGUERIA():
    assert hasattr(producto, "IVA_DROGUERIA")
    descriptor = None
    for klass in producto.__mro__:
        if "IVA_DROGUERIA" in klass.__dict__:
            descriptor = klass.__dict__["IVA_DROGUERIA"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_cantidadBodega():
    assert hasattr(producto, "cantidadBodega")
    descriptor = None
    for klass in producto.__mro__:
        if "cantidadBodega" in klass.__dict__:
            descriptor = klass.__dict__["cantidadBodega"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_DROGUERIA():
    assert hasattr(producto, "DROGUERIA")
    descriptor = None
    for klass in producto.__mro__:
        if "DROGUERIA" in klass.__dict__:
            descriptor = klass.__dict__["DROGUERIA"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_cantidadMinima():
    assert hasattr(producto, "cantidadMinima")
    descriptor = None
    for klass in producto.__mro__:
        if "cantidadMinima" in klass.__dict__:
            descriptor = klass.__dict__["cantidadMinima"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_IVA_PAPELERIA():
    assert hasattr(producto, "IVA_PAPELERIA")
    descriptor = None
    for klass in producto.__mro__:
        if "IVA_PAPELERIA" in klass.__dict__:
            descriptor = klass.__dict__["IVA_PAPELERIA"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_precioVenta():
    assert hasattr(producto, "precioVenta")
    descriptor = None
    for klass in producto.__mro__:
        if "precioVenta" in klass.__dict__:
            descriptor = klass.__dict__["precioVenta"]
            break
    assert isinstance(descriptor, property)

def test_producto_has_IVA_SUPERMERCADO():
    assert hasattr(producto, "IVA_SUPERMERCADO")
    descriptor = None
    for klass in producto.__mro__:
        if "IVA_SUPERMERCADO" in klass.__dict__:
            descriptor = klass.__dict__["IVA_SUPERMERCADO"]
            break
    assert isinstance(descriptor, property)



def test_tienda_is_not_abstract():
    assert not inspect.isabstract(Tienda)


def test_tienda_constructor_exists():
    assert callable(Tienda.__init__)


def test_tienda_constructor_args():
    sig = inspect.signature(Tienda.__init__)
    params = list(sig.parameters.keys())
    assert "getProducto1" in params, "Missing parameter 'getProducto1'"
    assert "getProducto4" in params, "Missing parameter 'getProducto4'"
    assert "getProducto3" in params, "Missing parameter 'getProducto3'"
    assert "Tienda" in params, "Missing parameter 'Tienda'"
    assert "getProducto2" in params, "Missing parameter 'getProducto2'"

def test_tienda_has_getProducto1():
    assert hasattr(Tienda, "getProducto1")
    descriptor = None
    for klass in Tienda.__mro__:
        if "getProducto1" in klass.__dict__:
            descriptor = klass.__dict__["getProducto1"]
            break
    assert isinstance(descriptor, property)

def test_tienda_has_getProducto4():
    assert hasattr(Tienda, "getProducto4")
    descriptor = None
    for klass in Tienda.__mro__:
        if "getProducto4" in klass.__dict__:
            descriptor = klass.__dict__["getProducto4"]
            break
    assert isinstance(descriptor, property)

def test_tienda_has_getProducto3():
    assert hasattr(Tienda, "getProducto3")
    descriptor = None
    for klass in Tienda.__mro__:
        if "getProducto3" in klass.__dict__:
            descriptor = klass.__dict__["getProducto3"]
            break
    assert isinstance(descriptor, property)

def test_tienda_has_Tienda():
    assert hasattr(Tienda, "Tienda")
    descriptor = None
    for klass in Tienda.__mro__:
        if "Tienda" in klass.__dict__:
            descriptor = klass.__dict__["Tienda"]
            break
    assert isinstance(descriptor, property)

def test_tienda_has_getProducto2():
    assert hasattr(Tienda, "getProducto2")
    descriptor = None
    for klass in Tienda.__mro__:
        if "getProducto2" in klass.__dict__:
            descriptor = klass.__dict__["getProducto2"]
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
caninos3_strategy = st.builds(
    caninos3,
    nombre=
        safe_text,
    observaciones=
        safe_text,
    edad=
        safe_text,
    altura=
        safe_text,
    peso=
        safe_text,
    raza=
        safe_text
)
veterinaria3_strategy = st.builds(
    veterinaria3,
    _attr=
        safe_text
)
caninos2_strategy = st.builds(
    caninos2,
    nombre=
        safe_text,
    altura=
        safe_text,
    raza=
        safe_text,
    observaciones=
        safe_text,
    edad=
        safe_text,
    peso=
        safe_text
)
veterinaria2_strategy = st.builds(
    veterinaria2,
    _=
        safe_text
)
caninos1_strategy = st.builds(
    caninos1,
    obsercaciones=
        safe_text,
    altura=
        safe_text,
    edad=
        safe_text,
    peso=
        safe_text,
    raza=
        safe_text,
    nombre=
        safe_text
)
veterinaria1_strategy = st.builds(
    veterinaria1,
)
caninos_strategy = st.builds(
    caninos,
    raza=
        safe_text,
    nombre=
        safe_text,
    peso=
        safe_text,
    altura=
        safe_text,
    observaciones=
        safe_text,
    edad=
        safe_text
)
veterinaria_strategy = st.builds(
    veterinaria,
)
_1_strategy = st.builds(
    _1,
)
producto_strategy = st.builds(
    producto,
    tipo=
        safe_text,
    nombre=
        safe_text,
    cantidadVendida=
        safe_text,
    SUPERMERCADO=
        safe_text,
    PAPELERIA=
        safe_text,
    IVA_DROGUERIA=
        safe_text,
    cantidadBodega=
        safe_text,
    DROGUERIA=
        safe_text,
    cantidadMinima=
        safe_text,
    IVA_PAPELERIA=
        safe_text,
    precioVenta=
        safe_text,
    IVA_SUPERMERCADO=
        safe_text
)
Tienda_strategy = st.builds(
    Tienda,
    getProducto1=
        safe_text,
    getProducto4=
        safe_text,
    getProducto3=
        safe_text,
    Tienda=
        safe_text,
    getProducto2=
        safe_text
)

@given(instance=caninos3_strategy)
@settings(max_examples=50)
def test_caninos3_instantiation(instance):
    assert isinstance(instance, caninos3)



@given(instance=caninos3_strategy)
def test_caninos3_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=caninos3_strategy)
def test_caninos3_observaciones_setter(instance):
    original = instance.observaciones
    instance.observaciones = original
    assert instance.observaciones == original



@given(instance=caninos3_strategy)
def test_caninos3_edad_setter(instance):
    original = instance.edad
    instance.edad = original
    assert instance.edad == original



@given(instance=caninos3_strategy)
def test_caninos3_altura_setter(instance):
    original = instance.altura
    instance.altura = original
    assert instance.altura == original



@given(instance=caninos3_strategy)
def test_caninos3_peso_setter(instance):
    original = instance.peso
    instance.peso = original
    assert instance.peso == original



@given(instance=caninos3_strategy)
def test_caninos3_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original

@given(instance=veterinaria3_strategy)
@settings(max_examples=50)
def test_veterinaria3_instantiation(instance):
    assert isinstance(instance, veterinaria3)



@given(instance=veterinaria3_strategy)
def test_veterinaria3__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original

@given(instance=caninos2_strategy)
@settings(max_examples=50)
def test_caninos2_instantiation(instance):
    assert isinstance(instance, caninos2)



@given(instance=caninos2_strategy)
def test_caninos2_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=caninos2_strategy)
def test_caninos2_altura_setter(instance):
    original = instance.altura
    instance.altura = original
    assert instance.altura == original



@given(instance=caninos2_strategy)
def test_caninos2_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original



@given(instance=caninos2_strategy)
def test_caninos2_observaciones_setter(instance):
    original = instance.observaciones
    instance.observaciones = original
    assert instance.observaciones == original



@given(instance=caninos2_strategy)
def test_caninos2_edad_setter(instance):
    original = instance.edad
    instance.edad = original
    assert instance.edad == original



@given(instance=caninos2_strategy)
def test_caninos2_peso_setter(instance):
    original = instance.peso
    instance.peso = original
    assert instance.peso == original

@given(instance=veterinaria2_strategy)
@settings(max_examples=50)
def test_veterinaria2_instantiation(instance):
    assert isinstance(instance, veterinaria2)



@given(instance=veterinaria2_strategy)
def test_veterinaria2___setter(instance):
    original = instance._
    instance._ = original
    assert instance._ == original

@given(instance=caninos1_strategy)
@settings(max_examples=50)
def test_caninos1_instantiation(instance):
    assert isinstance(instance, caninos1)



@given(instance=caninos1_strategy)
def test_caninos1_obsercaciones_setter(instance):
    original = instance.obsercaciones
    instance.obsercaciones = original
    assert instance.obsercaciones == original



@given(instance=caninos1_strategy)
def test_caninos1_altura_setter(instance):
    original = instance.altura
    instance.altura = original
    assert instance.altura == original



@given(instance=caninos1_strategy)
def test_caninos1_edad_setter(instance):
    original = instance.edad
    instance.edad = original
    assert instance.edad == original



@given(instance=caninos1_strategy)
def test_caninos1_peso_setter(instance):
    original = instance.peso
    instance.peso = original
    assert instance.peso == original



@given(instance=caninos1_strategy)
def test_caninos1_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original



@given(instance=caninos1_strategy)
def test_caninos1_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=veterinaria1_strategy)
@settings(max_examples=50)
def test_veterinaria1_instantiation(instance):
    assert isinstance(instance, veterinaria1)

@given(instance=caninos_strategy)
@settings(max_examples=50)
def test_caninos_instantiation(instance):
    assert isinstance(instance, caninos)



@given(instance=caninos_strategy)
def test_caninos_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original



@given(instance=caninos_strategy)
def test_caninos_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=caninos_strategy)
def test_caninos_peso_setter(instance):
    original = instance.peso
    instance.peso = original
    assert instance.peso == original



@given(instance=caninos_strategy)
def test_caninos_altura_setter(instance):
    original = instance.altura
    instance.altura = original
    assert instance.altura == original



@given(instance=caninos_strategy)
def test_caninos_observaciones_setter(instance):
    original = instance.observaciones
    instance.observaciones = original
    assert instance.observaciones == original



@given(instance=caninos_strategy)
def test_caninos_edad_setter(instance):
    original = instance.edad
    instance.edad = original
    assert instance.edad == original

@given(instance=veterinaria_strategy)
@settings(max_examples=50)
def test_veterinaria_instantiation(instance):
    assert isinstance(instance, veterinaria)

@given(instance=_1_strategy)
@settings(max_examples=50)
def test__1_instantiation(instance):
    assert isinstance(instance, _1)

@given(instance=producto_strategy)
@settings(max_examples=50)
def test_producto_instantiation(instance):
    assert isinstance(instance, producto)



@given(instance=producto_strategy)
def test_producto_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original



@given(instance=producto_strategy)
def test_producto_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=producto_strategy)
def test_producto_cantidadVendida_setter(instance):
    original = instance.cantidadVendida
    instance.cantidadVendida = original
    assert instance.cantidadVendida == original



@given(instance=producto_strategy)
def test_producto_SUPERMERCADO_setter(instance):
    original = instance.SUPERMERCADO
    instance.SUPERMERCADO = original
    assert instance.SUPERMERCADO == original



@given(instance=producto_strategy)
def test_producto_PAPELERIA_setter(instance):
    original = instance.PAPELERIA
    instance.PAPELERIA = original
    assert instance.PAPELERIA == original



@given(instance=producto_strategy)
def test_producto_IVA_DROGUERIA_setter(instance):
    original = instance.IVA_DROGUERIA
    instance.IVA_DROGUERIA = original
    assert instance.IVA_DROGUERIA == original



@given(instance=producto_strategy)
def test_producto_cantidadBodega_setter(instance):
    original = instance.cantidadBodega
    instance.cantidadBodega = original
    assert instance.cantidadBodega == original



@given(instance=producto_strategy)
def test_producto_DROGUERIA_setter(instance):
    original = instance.DROGUERIA
    instance.DROGUERIA = original
    assert instance.DROGUERIA == original



@given(instance=producto_strategy)
def test_producto_cantidadMinima_setter(instance):
    original = instance.cantidadMinima
    instance.cantidadMinima = original
    assert instance.cantidadMinima == original



@given(instance=producto_strategy)
def test_producto_IVA_PAPELERIA_setter(instance):
    original = instance.IVA_PAPELERIA
    instance.IVA_PAPELERIA = original
    assert instance.IVA_PAPELERIA == original



@given(instance=producto_strategy)
def test_producto_precioVenta_setter(instance):
    original = instance.precioVenta
    instance.precioVenta = original
    assert instance.precioVenta == original



@given(instance=producto_strategy)
def test_producto_IVA_SUPERMERCADO_setter(instance):
    original = instance.IVA_SUPERMERCADO
    instance.IVA_SUPERMERCADO = original
    assert instance.IVA_SUPERMERCADO == original

@given(instance=Tienda_strategy)
@settings(max_examples=50)
def test_tienda_instantiation(instance):
    assert isinstance(instance, Tienda)



@given(instance=Tienda_strategy)
def test_tienda_getProducto1_setter(instance):
    original = instance.getProducto1
    instance.getProducto1 = original
    assert instance.getProducto1 == original



@given(instance=Tienda_strategy)
def test_tienda_getProducto4_setter(instance):
    original = instance.getProducto4
    instance.getProducto4 = original
    assert instance.getProducto4 == original



@given(instance=Tienda_strategy)
def test_tienda_getProducto3_setter(instance):
    original = instance.getProducto3
    instance.getProducto3 = original
    assert instance.getProducto3 == original



@given(instance=Tienda_strategy)
def test_tienda_Tienda_setter(instance):
    original = instance.Tienda
    instance.Tienda = original
    assert instance.Tienda == original



@given(instance=Tienda_strategy)
def test_tienda_getProducto2_setter(instance):
    original = instance.getProducto2
    instance.getProducto2 = original
    assert instance.getProducto2 == original
