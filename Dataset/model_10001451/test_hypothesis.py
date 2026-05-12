import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Ventana,
    JFrame,
    Cuadrado,
    Canvas,
    Figura,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ventana_is_not_abstract():
    assert not inspect.isabstract(Ventana)


def test_ventana_constructor_exists():
    assert callable(Ventana.__init__)


def test_ventana_constructor_args():
    sig = inspect.signature(Ventana.__init__)
    params = list(sig.parameters.keys())
    assert "c3" in params, "Missing parameter 'c3'"
    assert "l2" in params, "Missing parameter 'l2'"
    assert "fig" in params, "Missing parameter 'fig'"
    assert "c1" in params, "Missing parameter 'c1'"
    assert "l1" in params, "Missing parameter 'l1'"
    assert "etiqueta" in params, "Missing parameter 'etiqueta'"
    assert "c2" in params, "Missing parameter 'c2'"

def test_ventana_has_c3():
    assert hasattr(Ventana, "c3")
    descriptor = None
    for klass in Ventana.__mro__:
        if "c3" in klass.__dict__:
            descriptor = klass.__dict__["c3"]
            break
    assert isinstance(descriptor, property)

def test_ventana_has_l2():
    assert hasattr(Ventana, "l2")
    descriptor = None
    for klass in Ventana.__mro__:
        if "l2" in klass.__dict__:
            descriptor = klass.__dict__["l2"]
            break
    assert isinstance(descriptor, property)

def test_ventana_has_fig():
    assert hasattr(Ventana, "fig")
    descriptor = None
    for klass in Ventana.__mro__:
        if "fig" in klass.__dict__:
            descriptor = klass.__dict__["fig"]
            break
    assert isinstance(descriptor, property)

def test_ventana_has_c1():
    assert hasattr(Ventana, "c1")
    descriptor = None
    for klass in Ventana.__mro__:
        if "c1" in klass.__dict__:
            descriptor = klass.__dict__["c1"]
            break
    assert isinstance(descriptor, property)

def test_ventana_has_l1():
    assert hasattr(Ventana, "l1")
    descriptor = None
    for klass in Ventana.__mro__:
        if "l1" in klass.__dict__:
            descriptor = klass.__dict__["l1"]
            break
    assert isinstance(descriptor, property)

def test_ventana_has_etiqueta():
    assert hasattr(Ventana, "etiqueta")
    descriptor = None
    for klass in Ventana.__mro__:
        if "etiqueta" in klass.__dict__:
            descriptor = klass.__dict__["etiqueta"]
            break
    assert isinstance(descriptor, property)

def test_ventana_has_c2():
    assert hasattr(Ventana, "c2")
    descriptor = None
    for klass in Ventana.__mro__:
        if "c2" in klass.__dict__:
            descriptor = klass.__dict__["c2"]
            break
    assert isinstance(descriptor, property)



def test_jframe_is_not_abstract():
    assert not inspect.isabstract(JFrame)


def test_jframe_constructor_exists():
    assert callable(JFrame.__init__)


def test_jframe_constructor_args():
    sig = inspect.signature(JFrame.__init__)
    params = list(sig.parameters.keys())



def test_cuadrado_is_not_abstract():
    assert not inspect.isabstract(Cuadrado)


def test_cuadrado_constructor_exists():
    assert callable(Cuadrado.__init__)


def test_cuadrado_constructor_args():
    sig = inspect.signature(Cuadrado.__init__)
    params = list(sig.parameters.keys())
    assert "v1" in params, "Missing parameter 'v1'"
    assert "img" in params, "Missing parameter 'img'"
    assert "v2" in params, "Missing parameter 'v2'"

def test_cuadrado_has_v1():
    assert hasattr(Cuadrado, "v1")
    descriptor = None
    for klass in Cuadrado.__mro__:
        if "v1" in klass.__dict__:
            descriptor = klass.__dict__["v1"]
            break
    assert isinstance(descriptor, property)

def test_cuadrado_has_img():
    assert hasattr(Cuadrado, "img")
    descriptor = None
    for klass in Cuadrado.__mro__:
        if "img" in klass.__dict__:
            descriptor = klass.__dict__["img"]
            break
    assert isinstance(descriptor, property)

def test_cuadrado_has_v2():
    assert hasattr(Cuadrado, "v2")
    descriptor = None
    for klass in Cuadrado.__mro__:
        if "v2" in klass.__dict__:
            descriptor = klass.__dict__["v2"]
            break
    assert isinstance(descriptor, property)



def test_canvas_is_not_abstract():
    assert not inspect.isabstract(Canvas)


def test_canvas_constructor_exists():
    assert callable(Canvas.__init__)


def test_canvas_constructor_args():
    sig = inspect.signature(Canvas.__init__)
    params = list(sig.parameters.keys())



def test_figura_is_not_abstract():
    assert not inspect.isabstract(Figura)


def test_figura_constructor_exists():
    assert callable(Figura.__init__)


def test_figura_constructor_args():
    sig = inspect.signature(Figura.__init__)
    params = list(sig.parameters.keys())
    assert "estado" in params, "Missing parameter 'estado'"
    assert "valor" in params, "Missing parameter 'valor'"

def test_figura_has_estado():
    assert hasattr(Figura, "estado")
    descriptor = None
    for klass in Figura.__mro__:
        if "estado" in klass.__dict__:
            descriptor = klass.__dict__["estado"]
            break
    assert isinstance(descriptor, property)

def test_figura_has_valor():
    assert hasattr(Figura, "valor")
    descriptor = None
    for klass in Figura.__mro__:
        if "valor" in klass.__dict__:
            descriptor = klass.__dict__["valor"]
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
Ventana_strategy = st.builds(
    Ventana,
    c3=
        st.none(),
    l2=
        st.integers(),
    fig=
        st.none(),
    c1=
        st.none(),
    l1=
        st.integers(),
    etiqueta=
        safe_text,
    c2=
        st.none()
)
JFrame_strategy = st.builds(
    JFrame,
)
Cuadrado_strategy = st.builds(
    Cuadrado,
    v1=
        st.integers(),
    img=
        safe_text,
    v2=
        st.integers()
)
Canvas_strategy = st.builds(
    Canvas,
)
Figura_strategy = st.builds(
    Figura,
    estado=
        st.booleans(),
    valor=
        st.integers()
)

@given(instance=Ventana_strategy)
@settings(max_examples=50)
def test_ventana_instantiation(instance):
    assert isinstance(instance, Ventana)



@given(instance=Ventana_strategy)
def test_ventana_c3_setter(instance):
    original = instance.c3
    instance.c3 = original
    assert instance.c3 == original



@given(instance=Ventana_strategy)
def test_ventana_l2_setter(instance):
    original = instance.l2
    instance.l2 = original
    assert instance.l2 == original



@given(instance=Ventana_strategy)
def test_ventana_fig_setter(instance):
    original = instance.fig
    instance.fig = original
    assert instance.fig == original



@given(instance=Ventana_strategy)
def test_ventana_c1_setter(instance):
    original = instance.c1
    instance.c1 = original
    assert instance.c1 == original



@given(instance=Ventana_strategy)
def test_ventana_l1_setter(instance):
    original = instance.l1
    instance.l1 = original
    assert instance.l1 == original



@given(instance=Ventana_strategy)
def test_ventana_etiqueta_setter(instance):
    original = instance.etiqueta
    instance.etiqueta = original
    assert instance.etiqueta == original



@given(instance=Ventana_strategy)
def test_ventana_c2_setter(instance):
    original = instance.c2
    instance.c2 = original
    assert instance.c2 == original

@given(instance=JFrame_strategy)
@settings(max_examples=50)
def test_jframe_instantiation(instance):
    assert isinstance(instance, JFrame)

@given(instance=Cuadrado_strategy)
@settings(max_examples=50)
def test_cuadrado_instantiation(instance):
    assert isinstance(instance, Cuadrado)



@given(instance=Cuadrado_strategy)
def test_cuadrado_v1_setter(instance):
    original = instance.v1
    instance.v1 = original
    assert instance.v1 == original



@given(instance=Cuadrado_strategy)
def test_cuadrado_img_setter(instance):
    original = instance.img
    instance.img = original
    assert instance.img == original



@given(instance=Cuadrado_strategy)
def test_cuadrado_v2_setter(instance):
    original = instance.v2
    instance.v2 = original
    assert instance.v2 == original

@given(instance=Canvas_strategy)
@settings(max_examples=50)
def test_canvas_instantiation(instance):
    assert isinstance(instance, Canvas)

@given(instance=Figura_strategy)
@settings(max_examples=50)
def test_figura_instantiation(instance):
    assert isinstance(instance, Figura)



@given(instance=Figura_strategy)
def test_figura_estado_setter(instance):
    original = instance.estado
    instance.estado = original
    assert instance.estado == original



@given(instance=Figura_strategy)
def test_figura_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original
