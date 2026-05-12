import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Casilla,
    Dados,
    Jugador,
    TCobrarJugadores,
    TIrACarcel,
    Monopoly1,
    TAvanzarPagarDoble,
    TAvanzar,
    TCobrarBanco,
    TPagarJugadores,
    TPagarBanco,
    Tarjeta,
    TPagarPorEdificios1,
    TPagarJugadores1,
    TCobrarBanco1,
    TIrACarcel1,
    TAvanzarPagarDoble1,
    TAvanzar1,
    TCobrarJugadores1,
    TPagarPorEdificios,
    TPagarBanco1,
    Tarjeta1,
    TSalirCarcel,
    Impuestos,
    CasillaTarjeta,
    Salida,
    Carcel,
    IrACarcel,
    ParqueoLibre,
    Ferrocarril,
    Propiedad,
    Servicio,
    TituloServicio,
    TituloFerrocarril,
    TituloPropiedad,
    Titulo,
    Monopoly,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_casilla_is_not_abstract():
    assert not inspect.isabstract(Casilla)


def test_casilla_constructor_exists():
    assert callable(Casilla.__init__)


def test_casilla_constructor_args():
    sig = inspect.signature(Casilla.__init__)
    params = list(sig.parameters.keys())



def test_dados_is_not_abstract():
    assert not inspect.isabstract(Dados)


def test_dados_constructor_exists():
    assert callable(Dados.__init__)


def test_dados_constructor_args():
    sig = inspect.signature(Dados.__init__)
    params = list(sig.parameters.keys())



def test_jugador_is_not_abstract():
    assert not inspect.isabstract(Jugador)


def test_jugador_constructor_exists():
    assert callable(Jugador.__init__)


def test_jugador_constructor_args():
    sig = inspect.signature(Jugador.__init__)
    params = list(sig.parameters.keys())



def test_tcobrarjugadores_is_not_abstract():
    assert not inspect.isabstract(TCobrarJugadores)


def test_tcobrarjugadores_constructor_exists():
    assert callable(TCobrarJugadores.__init__)


def test_tcobrarjugadores_constructor_args():
    sig = inspect.signature(TCobrarJugadores.__init__)
    params = list(sig.parameters.keys())



def test_tiracarcel_is_not_abstract():
    assert not inspect.isabstract(TIrACarcel)


def test_tiracarcel_constructor_exists():
    assert callable(TIrACarcel.__init__)


def test_tiracarcel_constructor_args():
    sig = inspect.signature(TIrACarcel.__init__)
    params = list(sig.parameters.keys())



def test_monopoly1_is_not_abstract():
    assert not inspect.isabstract(Monopoly1)


def test_monopoly1_constructor_exists():
    assert callable(Monopoly1.__init__)


def test_monopoly1_constructor_args():
    sig = inspect.signature(Monopoly1.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_monopoly1_has_attribute():
    assert hasattr(Monopoly1, "attribute")
    descriptor = None
    for klass in Monopoly1.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_tavanzarpagardoble_is_not_abstract():
    assert not inspect.isabstract(TAvanzarPagarDoble)


def test_tavanzarpagardoble_constructor_exists():
    assert callable(TAvanzarPagarDoble.__init__)


def test_tavanzarpagardoble_constructor_args():
    sig = inspect.signature(TAvanzarPagarDoble.__init__)
    params = list(sig.parameters.keys())



def test_tavanzar_is_not_abstract():
    assert not inspect.isabstract(TAvanzar)


def test_tavanzar_constructor_exists():
    assert callable(TAvanzar.__init__)


def test_tavanzar_constructor_args():
    sig = inspect.signature(TAvanzar.__init__)
    params = list(sig.parameters.keys())



def test_tcobrarbanco_is_not_abstract():
    assert not inspect.isabstract(TCobrarBanco)


def test_tcobrarbanco_constructor_exists():
    assert callable(TCobrarBanco.__init__)


def test_tcobrarbanco_constructor_args():
    sig = inspect.signature(TCobrarBanco.__init__)
    params = list(sig.parameters.keys())



def test_tpagarjugadores_is_not_abstract():
    assert not inspect.isabstract(TPagarJugadores)


def test_tpagarjugadores_constructor_exists():
    assert callable(TPagarJugadores.__init__)


def test_tpagarjugadores_constructor_args():
    sig = inspect.signature(TPagarJugadores.__init__)
    params = list(sig.parameters.keys())



def test_tpagarbanco_is_not_abstract():
    assert not inspect.isabstract(TPagarBanco)


def test_tpagarbanco_constructor_exists():
    assert callable(TPagarBanco.__init__)


def test_tpagarbanco_constructor_args():
    sig = inspect.signature(TPagarBanco.__init__)
    params = list(sig.parameters.keys())



def test_tarjeta_is_not_abstract():
    assert not inspect.isabstract(Tarjeta)


def test_tarjeta_constructor_exists():
    assert callable(Tarjeta.__init__)


def test_tarjeta_constructor_args():
    sig = inspect.signature(Tarjeta.__init__)
    params = list(sig.parameters.keys())



def test_tpagarporedificios1_is_not_abstract():
    assert not inspect.isabstract(TPagarPorEdificios1)


def test_tpagarporedificios1_constructor_exists():
    assert callable(TPagarPorEdificios1.__init__)


def test_tpagarporedificios1_constructor_args():
    sig = inspect.signature(TPagarPorEdificios1.__init__)
    params = list(sig.parameters.keys())



def test_tpagarjugadores1_is_not_abstract():
    assert not inspect.isabstract(TPagarJugadores1)


def test_tpagarjugadores1_constructor_exists():
    assert callable(TPagarJugadores1.__init__)


def test_tpagarjugadores1_constructor_args():
    sig = inspect.signature(TPagarJugadores1.__init__)
    params = list(sig.parameters.keys())
    assert "monto" in params, "Missing parameter 'monto'"

def test_tpagarjugadores1_has_monto():
    assert hasattr(TPagarJugadores1, "monto")
    descriptor = None
    for klass in TPagarJugadores1.__mro__:
        if "monto" in klass.__dict__:
            descriptor = klass.__dict__["monto"]
            break
    assert isinstance(descriptor, property)



def test_tcobrarbanco1_is_not_abstract():
    assert not inspect.isabstract(TCobrarBanco1)


def test_tcobrarbanco1_constructor_exists():
    assert callable(TCobrarBanco1.__init__)


def test_tcobrarbanco1_constructor_args():
    sig = inspect.signature(TCobrarBanco1.__init__)
    params = list(sig.parameters.keys())



def test_tiracarcel1_is_not_abstract():
    assert not inspect.isabstract(TIrACarcel1)


def test_tiracarcel1_constructor_exists():
    assert callable(TIrACarcel1.__init__)


def test_tiracarcel1_constructor_args():
    sig = inspect.signature(TIrACarcel1.__init__)
    params = list(sig.parameters.keys())



def test_tavanzarpagardoble1_is_not_abstract():
    assert not inspect.isabstract(TAvanzarPagarDoble1)


def test_tavanzarpagardoble1_constructor_exists():
    assert callable(TAvanzarPagarDoble1.__init__)


def test_tavanzarpagardoble1_constructor_args():
    sig = inspect.signature(TAvanzarPagarDoble1.__init__)
    params = list(sig.parameters.keys())



def test_tavanzar1_is_not_abstract():
    assert not inspect.isabstract(TAvanzar1)


def test_tavanzar1_constructor_exists():
    assert callable(TAvanzar1.__init__)


def test_tavanzar1_constructor_args():
    sig = inspect.signature(TAvanzar1.__init__)
    params = list(sig.parameters.keys())



def test_tcobrarjugadores1_is_not_abstract():
    assert not inspect.isabstract(TCobrarJugadores1)


def test_tcobrarjugadores1_constructor_exists():
    assert callable(TCobrarJugadores1.__init__)


def test_tcobrarjugadores1_constructor_args():
    sig = inspect.signature(TCobrarJugadores1.__init__)
    params = list(sig.parameters.keys())
    assert "monto" in params, "Missing parameter 'monto'"

def test_tcobrarjugadores1_has_monto():
    assert hasattr(TCobrarJugadores1, "monto")
    descriptor = None
    for klass in TCobrarJugadores1.__mro__:
        if "monto" in klass.__dict__:
            descriptor = klass.__dict__["monto"]
            break
    assert isinstance(descriptor, property)



def test_tpagarporedificios_is_not_abstract():
    assert not inspect.isabstract(TPagarPorEdificios)


def test_tpagarporedificios_constructor_exists():
    assert callable(TPagarPorEdificios.__init__)


def test_tpagarporedificios_constructor_args():
    sig = inspect.signature(TPagarPorEdificios.__init__)
    params = list(sig.parameters.keys())



def test_tpagarbanco1_is_not_abstract():
    assert not inspect.isabstract(TPagarBanco1)


def test_tpagarbanco1_constructor_exists():
    assert callable(TPagarBanco1.__init__)


def test_tpagarbanco1_constructor_args():
    sig = inspect.signature(TPagarBanco1.__init__)
    params = list(sig.parameters.keys())
    assert "monto" in params, "Missing parameter 'monto'"

def test_tpagarbanco1_has_monto():
    assert hasattr(TPagarBanco1, "monto")
    descriptor = None
    for klass in TPagarBanco1.__mro__:
        if "monto" in klass.__dict__:
            descriptor = klass.__dict__["monto"]
            break
    assert isinstance(descriptor, property)



def test_tarjeta1_is_not_abstract():
    assert not inspect.isabstract(Tarjeta1)


def test_tarjeta1_constructor_exists():
    assert callable(Tarjeta1.__init__)


def test_tarjeta1_constructor_args():
    sig = inspect.signature(Tarjeta1.__init__)
    params = list(sig.parameters.keys())
    assert "tipoDeCarta" in params, "Missing parameter 'tipoDeCarta'"
    assert "descripcion" in params, "Missing parameter 'descripcion'"

def test_tarjeta1_has_tipoDeCarta():
    assert hasattr(Tarjeta1, "tipoDeCarta")
    descriptor = None
    for klass in Tarjeta1.__mro__:
        if "tipoDeCarta" in klass.__dict__:
            descriptor = klass.__dict__["tipoDeCarta"]
            break
    assert isinstance(descriptor, property)

def test_tarjeta1_has_descripcion():
    assert hasattr(Tarjeta1, "descripcion")
    descriptor = None
    for klass in Tarjeta1.__mro__:
        if "descripcion" in klass.__dict__:
            descriptor = klass.__dict__["descripcion"]
            break
    assert isinstance(descriptor, property)



def test_tsalircarcel_is_not_abstract():
    assert not inspect.isabstract(TSalirCarcel)


def test_tsalircarcel_constructor_exists():
    assert callable(TSalirCarcel.__init__)


def test_tsalircarcel_constructor_args():
    sig = inspect.signature(TSalirCarcel.__init__)
    params = list(sig.parameters.keys())



def test_impuestos_is_not_abstract():
    assert not inspect.isabstract(Impuestos)


def test_impuestos_constructor_exists():
    assert callable(Impuestos.__init__)


def test_impuestos_constructor_args():
    sig = inspect.signature(Impuestos.__init__)
    params = list(sig.parameters.keys())



def test_casillatarjeta_is_not_abstract():
    assert not inspect.isabstract(CasillaTarjeta)


def test_casillatarjeta_constructor_exists():
    assert callable(CasillaTarjeta.__init__)


def test_casillatarjeta_constructor_args():
    sig = inspect.signature(CasillaTarjeta.__init__)
    params = list(sig.parameters.keys())



def test_salida_is_not_abstract():
    assert not inspect.isabstract(Salida)


def test_salida_constructor_exists():
    assert callable(Salida.__init__)


def test_salida_constructor_args():
    sig = inspect.signature(Salida.__init__)
    params = list(sig.parameters.keys())



def test_carcel_is_not_abstract():
    assert not inspect.isabstract(Carcel)


def test_carcel_constructor_exists():
    assert callable(Carcel.__init__)


def test_carcel_constructor_args():
    sig = inspect.signature(Carcel.__init__)
    params = list(sig.parameters.keys())



def test_iracarcel_is_not_abstract():
    assert not inspect.isabstract(IrACarcel)


def test_iracarcel_constructor_exists():
    assert callable(IrACarcel.__init__)


def test_iracarcel_constructor_args():
    sig = inspect.signature(IrACarcel.__init__)
    params = list(sig.parameters.keys())



def test_parqueolibre_is_not_abstract():
    assert not inspect.isabstract(ParqueoLibre)


def test_parqueolibre_constructor_exists():
    assert callable(ParqueoLibre.__init__)


def test_parqueolibre_constructor_args():
    sig = inspect.signature(ParqueoLibre.__init__)
    params = list(sig.parameters.keys())



def test_ferrocarril_is_not_abstract():
    assert not inspect.isabstract(Ferrocarril)


def test_ferrocarril_constructor_exists():
    assert callable(Ferrocarril.__init__)


def test_ferrocarril_constructor_args():
    sig = inspect.signature(Ferrocarril.__init__)
    params = list(sig.parameters.keys())



def test_propiedad_is_not_abstract():
    assert not inspect.isabstract(Propiedad)


def test_propiedad_constructor_exists():
    assert callable(Propiedad.__init__)


def test_propiedad_constructor_args():
    sig = inspect.signature(Propiedad.__init__)
    params = list(sig.parameters.keys())



def test_servicio_is_not_abstract():
    assert not inspect.isabstract(Servicio)


def test_servicio_constructor_exists():
    assert callable(Servicio.__init__)


def test_servicio_constructor_args():
    sig = inspect.signature(Servicio.__init__)
    params = list(sig.parameters.keys())



def test_tituloservicio_is_not_abstract():
    assert not inspect.isabstract(TituloServicio)


def test_tituloservicio_constructor_exists():
    assert callable(TituloServicio.__init__)


def test_tituloservicio_constructor_args():
    sig = inspect.signature(TituloServicio.__init__)
    params = list(sig.parameters.keys())



def test_tituloferrocarril_is_not_abstract():
    assert not inspect.isabstract(TituloFerrocarril)


def test_tituloferrocarril_constructor_exists():
    assert callable(TituloFerrocarril.__init__)


def test_tituloferrocarril_constructor_args():
    sig = inspect.signature(TituloFerrocarril.__init__)
    params = list(sig.parameters.keys())



def test_titulopropiedad_is_not_abstract():
    assert not inspect.isabstract(TituloPropiedad)


def test_titulopropiedad_constructor_exists():
    assert callable(TituloPropiedad.__init__)


def test_titulopropiedad_constructor_args():
    sig = inspect.signature(TituloPropiedad.__init__)
    params = list(sig.parameters.keys())



def test_titulo_is_not_abstract():
    assert not inspect.isabstract(Titulo)


def test_titulo_constructor_exists():
    assert callable(Titulo.__init__)


def test_titulo_constructor_args():
    sig = inspect.signature(Titulo.__init__)
    params = list(sig.parameters.keys())



def test_monopoly_is_not_abstract():
    assert not inspect.isabstract(Monopoly)


def test_monopoly_constructor_exists():
    assert callable(Monopoly.__init__)


def test_monopoly_constructor_args():
    sig = inspect.signature(Monopoly.__init__)
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
Casilla_strategy = st.builds(
    Casilla,
)
Dados_strategy = st.builds(
    Dados,
)
Jugador_strategy = st.builds(
    Jugador,
)
TCobrarJugadores_strategy = st.builds(
    TCobrarJugadores,
)
TIrACarcel_strategy = st.builds(
    TIrACarcel,
)
Monopoly1_strategy = st.builds(
    Monopoly1,
    attribute=
        safe_text
)
TAvanzarPagarDoble_strategy = st.builds(
    TAvanzarPagarDoble,
)
TAvanzar_strategy = st.builds(
    TAvanzar,
)
TCobrarBanco_strategy = st.builds(
    TCobrarBanco,
)
TPagarJugadores_strategy = st.builds(
    TPagarJugadores,
)
TPagarBanco_strategy = st.builds(
    TPagarBanco,
)
Tarjeta_strategy = st.builds(
    Tarjeta,
)
TPagarPorEdificios1_strategy = st.builds(
    TPagarPorEdificios1,
)
TPagarJugadores1_strategy = st.builds(
    TPagarJugadores1,
    monto=
        st.integers()
)
TCobrarBanco1_strategy = st.builds(
    TCobrarBanco1,
)
TIrACarcel1_strategy = st.builds(
    TIrACarcel1,
)
TAvanzarPagarDoble1_strategy = st.builds(
    TAvanzarPagarDoble1,
)
TAvanzar1_strategy = st.builds(
    TAvanzar1,
)
TCobrarJugadores1_strategy = st.builds(
    TCobrarJugadores1,
    monto=
        st.integers()
)
TPagarPorEdificios_strategy = st.builds(
    TPagarPorEdificios,
)
TPagarBanco1_strategy = st.builds(
    TPagarBanco1,
    monto=
        st.integers()
)
Tarjeta1_strategy = st.builds(
    Tarjeta1,
    tipoDeCarta=
        safe_text,
    descripcion=
        safe_text
)
TSalirCarcel_strategy = st.builds(
    TSalirCarcel,
)
Impuestos_strategy = st.builds(
    Impuestos,
)
CasillaTarjeta_strategy = st.builds(
    CasillaTarjeta,
)
Salida_strategy = st.builds(
    Salida,
)
Carcel_strategy = st.builds(
    Carcel,
)
IrACarcel_strategy = st.builds(
    IrACarcel,
)
ParqueoLibre_strategy = st.builds(
    ParqueoLibre,
)
Ferrocarril_strategy = st.builds(
    Ferrocarril,
)
Propiedad_strategy = st.builds(
    Propiedad,
)
Servicio_strategy = st.builds(
    Servicio,
)
TituloServicio_strategy = st.builds(
    TituloServicio,
)
TituloFerrocarril_strategy = st.builds(
    TituloFerrocarril,
)
TituloPropiedad_strategy = st.builds(
    TituloPropiedad,
)
Titulo_strategy = st.builds(
    Titulo,
)
Monopoly_strategy = st.builds(
    Monopoly,
)

@given(instance=Casilla_strategy)
@settings(max_examples=50)
def test_casilla_instantiation(instance):
    assert isinstance(instance, Casilla)

@given(instance=Dados_strategy)
@settings(max_examples=50)
def test_dados_instantiation(instance):
    assert isinstance(instance, Dados)

@given(instance=Jugador_strategy)
@settings(max_examples=50)
def test_jugador_instantiation(instance):
    assert isinstance(instance, Jugador)

@given(instance=TCobrarJugadores_strategy)
@settings(max_examples=50)
def test_tcobrarjugadores_instantiation(instance):
    assert isinstance(instance, TCobrarJugadores)

@given(instance=TIrACarcel_strategy)
@settings(max_examples=50)
def test_tiracarcel_instantiation(instance):
    assert isinstance(instance, TIrACarcel)

@given(instance=Monopoly1_strategy)
@settings(max_examples=50)
def test_monopoly1_instantiation(instance):
    assert isinstance(instance, Monopoly1)



@given(instance=Monopoly1_strategy)
def test_monopoly1_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=TAvanzarPagarDoble_strategy)
@settings(max_examples=50)
def test_tavanzarpagardoble_instantiation(instance):
    assert isinstance(instance, TAvanzarPagarDoble)

@given(instance=TAvanzar_strategy)
@settings(max_examples=50)
def test_tavanzar_instantiation(instance):
    assert isinstance(instance, TAvanzar)

@given(instance=TCobrarBanco_strategy)
@settings(max_examples=50)
def test_tcobrarbanco_instantiation(instance):
    assert isinstance(instance, TCobrarBanco)

@given(instance=TPagarJugadores_strategy)
@settings(max_examples=50)
def test_tpagarjugadores_instantiation(instance):
    assert isinstance(instance, TPagarJugadores)

@given(instance=TPagarBanco_strategy)
@settings(max_examples=50)
def test_tpagarbanco_instantiation(instance):
    assert isinstance(instance, TPagarBanco)

@given(instance=Tarjeta_strategy)
@settings(max_examples=50)
def test_tarjeta_instantiation(instance):
    assert isinstance(instance, Tarjeta)

@given(instance=TPagarPorEdificios1_strategy)
@settings(max_examples=50)
def test_tpagarporedificios1_instantiation(instance):
    assert isinstance(instance, TPagarPorEdificios1)

@given(instance=TPagarJugadores1_strategy)
@settings(max_examples=50)
def test_tpagarjugadores1_instantiation(instance):
    assert isinstance(instance, TPagarJugadores1)



@given(instance=TPagarJugadores1_strategy)
def test_tpagarjugadores1_monto_setter(instance):
    original = instance.monto
    instance.monto = original
    assert instance.monto == original

@given(instance=TCobrarBanco1_strategy)
@settings(max_examples=50)
def test_tcobrarbanco1_instantiation(instance):
    assert isinstance(instance, TCobrarBanco1)

@given(instance=TIrACarcel1_strategy)
@settings(max_examples=50)
def test_tiracarcel1_instantiation(instance):
    assert isinstance(instance, TIrACarcel1)

@given(instance=TAvanzarPagarDoble1_strategy)
@settings(max_examples=50)
def test_tavanzarpagardoble1_instantiation(instance):
    assert isinstance(instance, TAvanzarPagarDoble1)

@given(instance=TAvanzar1_strategy)
@settings(max_examples=50)
def test_tavanzar1_instantiation(instance):
    assert isinstance(instance, TAvanzar1)

@given(instance=TCobrarJugadores1_strategy)
@settings(max_examples=50)
def test_tcobrarjugadores1_instantiation(instance):
    assert isinstance(instance, TCobrarJugadores1)



@given(instance=TCobrarJugadores1_strategy)
def test_tcobrarjugadores1_monto_setter(instance):
    original = instance.monto
    instance.monto = original
    assert instance.monto == original

@given(instance=TPagarPorEdificios_strategy)
@settings(max_examples=50)
def test_tpagarporedificios_instantiation(instance):
    assert isinstance(instance, TPagarPorEdificios)

@given(instance=TPagarBanco1_strategy)
@settings(max_examples=50)
def test_tpagarbanco1_instantiation(instance):
    assert isinstance(instance, TPagarBanco1)



@given(instance=TPagarBanco1_strategy)
def test_tpagarbanco1_monto_setter(instance):
    original = instance.monto
    instance.monto = original
    assert instance.monto == original

@given(instance=Tarjeta1_strategy)
@settings(max_examples=50)
def test_tarjeta1_instantiation(instance):
    assert isinstance(instance, Tarjeta1)



@given(instance=Tarjeta1_strategy)
def test_tarjeta1_tipoDeCarta_setter(instance):
    original = instance.tipoDeCarta
    instance.tipoDeCarta = original
    assert instance.tipoDeCarta == original



@given(instance=Tarjeta1_strategy)
def test_tarjeta1_descripcion_setter(instance):
    original = instance.descripcion
    instance.descripcion = original
    assert instance.descripcion == original

@given(instance=TSalirCarcel_strategy)
@settings(max_examples=50)
def test_tsalircarcel_instantiation(instance):
    assert isinstance(instance, TSalirCarcel)

@given(instance=Impuestos_strategy)
@settings(max_examples=50)
def test_impuestos_instantiation(instance):
    assert isinstance(instance, Impuestos)

@given(instance=CasillaTarjeta_strategy)
@settings(max_examples=50)
def test_casillatarjeta_instantiation(instance):
    assert isinstance(instance, CasillaTarjeta)

@given(instance=Salida_strategy)
@settings(max_examples=50)
def test_salida_instantiation(instance):
    assert isinstance(instance, Salida)

@given(instance=Carcel_strategy)
@settings(max_examples=50)
def test_carcel_instantiation(instance):
    assert isinstance(instance, Carcel)

@given(instance=IrACarcel_strategy)
@settings(max_examples=50)
def test_iracarcel_instantiation(instance):
    assert isinstance(instance, IrACarcel)

@given(instance=ParqueoLibre_strategy)
@settings(max_examples=50)
def test_parqueolibre_instantiation(instance):
    assert isinstance(instance, ParqueoLibre)

@given(instance=Ferrocarril_strategy)
@settings(max_examples=50)
def test_ferrocarril_instantiation(instance):
    assert isinstance(instance, Ferrocarril)

@given(instance=Propiedad_strategy)
@settings(max_examples=50)
def test_propiedad_instantiation(instance):
    assert isinstance(instance, Propiedad)

@given(instance=Servicio_strategy)
@settings(max_examples=50)
def test_servicio_instantiation(instance):
    assert isinstance(instance, Servicio)

@given(instance=TituloServicio_strategy)
@settings(max_examples=50)
def test_tituloservicio_instantiation(instance):
    assert isinstance(instance, TituloServicio)

@given(instance=TituloFerrocarril_strategy)
@settings(max_examples=50)
def test_tituloferrocarril_instantiation(instance):
    assert isinstance(instance, TituloFerrocarril)

@given(instance=TituloPropiedad_strategy)
@settings(max_examples=50)
def test_titulopropiedad_instantiation(instance):
    assert isinstance(instance, TituloPropiedad)

@given(instance=Titulo_strategy)
@settings(max_examples=50)
def test_titulo_instantiation(instance):
    assert isinstance(instance, Titulo)

@given(instance=Monopoly_strategy)
@settings(max_examples=50)
def test_monopoly_instantiation(instance):
    assert isinstance(instance, Monopoly)
