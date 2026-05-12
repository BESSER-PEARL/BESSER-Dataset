import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    SistemaApuesta,
    Historico,
    Equipo,
    Marcador,
    ApuestaEquipoGanador,
    ApuestaMarcadorEspecifico,
    Partido,
    Apuesta,
    Usuario,
    Tarjeta,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sistemaapuesta_is_not_abstract():
    assert not inspect.isabstract(SistemaApuesta)


def test_sistemaapuesta_constructor_exists():
    assert callable(SistemaApuesta.__init__)


def test_sistemaapuesta_constructor_args():
    sig = inspect.signature(SistemaApuesta.__init__)
    params = list(sig.parameters.keys())



def test_historico_is_not_abstract():
    assert not inspect.isabstract(Historico)


def test_historico_constructor_exists():
    assert callable(Historico.__init__)


def test_historico_constructor_args():
    sig = inspect.signature(Historico.__init__)
    params = list(sig.parameters.keys())
    assert "numeroPartidosGanados" in params, "Missing parameter 'numeroPartidosGanados'"
    assert "porcentajeApuestasEnFavor" in params, "Missing parameter 'porcentajeApuestasEnFavor'"
    assert "numeroPartidosPerdidos" in params, "Missing parameter 'numeroPartidosPerdidos'"
    assert "numeroPartidosJugados" in params, "Missing parameter 'numeroPartidosJugados'"

def test_historico_has_numeroPartidosGanados():
    assert hasattr(Historico, "numeroPartidosGanados")
    descriptor = None
    for klass in Historico.__mro__:
        if "numeroPartidosGanados" in klass.__dict__:
            descriptor = klass.__dict__["numeroPartidosGanados"]
            break
    assert isinstance(descriptor, property)

def test_historico_has_porcentajeApuestasEnFavor():
    assert hasattr(Historico, "porcentajeApuestasEnFavor")
    descriptor = None
    for klass in Historico.__mro__:
        if "porcentajeApuestasEnFavor" in klass.__dict__:
            descriptor = klass.__dict__["porcentajeApuestasEnFavor"]
            break
    assert isinstance(descriptor, property)

def test_historico_has_numeroPartidosPerdidos():
    assert hasattr(Historico, "numeroPartidosPerdidos")
    descriptor = None
    for klass in Historico.__mro__:
        if "numeroPartidosPerdidos" in klass.__dict__:
            descriptor = klass.__dict__["numeroPartidosPerdidos"]
            break
    assert isinstance(descriptor, property)

def test_historico_has_numeroPartidosJugados():
    assert hasattr(Historico, "numeroPartidosJugados")
    descriptor = None
    for klass in Historico.__mro__:
        if "numeroPartidosJugados" in klass.__dict__:
            descriptor = klass.__dict__["numeroPartidosJugados"]
            break
    assert isinstance(descriptor, property)



def test_equipo_is_not_abstract():
    assert not inspect.isabstract(Equipo)


def test_equipo_constructor_exists():
    assert callable(Equipo.__init__)


def test_equipo_constructor_args():
    sig = inspect.signature(Equipo.__init__)
    params = list(sig.parameters.keys())
    assert "jugadores" in params, "Missing parameter 'jugadores'"
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "porcentajeFavoritismo" in params, "Missing parameter 'porcentajeFavoritismo'"

def test_equipo_has_jugadores():
    assert hasattr(Equipo, "jugadores")
    descriptor = None
    for klass in Equipo.__mro__:
        if "jugadores" in klass.__dict__:
            descriptor = klass.__dict__["jugadores"]
            break
    assert isinstance(descriptor, property)

def test_equipo_has_nombre():
    assert hasattr(Equipo, "nombre")
    descriptor = None
    for klass in Equipo.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_equipo_has_porcentajeFavoritismo():
    assert hasattr(Equipo, "porcentajeFavoritismo")
    descriptor = None
    for klass in Equipo.__mro__:
        if "porcentajeFavoritismo" in klass.__dict__:
            descriptor = klass.__dict__["porcentajeFavoritismo"]
            break
    assert isinstance(descriptor, property)



def test_marcador_is_not_abstract():
    assert not inspect.isabstract(Marcador)


def test_marcador_constructor_exists():
    assert callable(Marcador.__init__)


def test_marcador_constructor_args():
    sig = inspect.signature(Marcador.__init__)
    params = list(sig.parameters.keys())
    assert "numeroGolesEquipo1" in params, "Missing parameter 'numeroGolesEquipo1'"
    assert "nombreEquipoGanador" in params, "Missing parameter 'nombreEquipoGanador'"
    assert "numeroGolesEquipo2" in params, "Missing parameter 'numeroGolesEquipo2'"

def test_marcador_has_numeroGolesEquipo1():
    assert hasattr(Marcador, "numeroGolesEquipo1")
    descriptor = None
    for klass in Marcador.__mro__:
        if "numeroGolesEquipo1" in klass.__dict__:
            descriptor = klass.__dict__["numeroGolesEquipo1"]
            break
    assert isinstance(descriptor, property)

def test_marcador_has_nombreEquipoGanador():
    assert hasattr(Marcador, "nombreEquipoGanador")
    descriptor = None
    for klass in Marcador.__mro__:
        if "nombreEquipoGanador" in klass.__dict__:
            descriptor = klass.__dict__["nombreEquipoGanador"]
            break
    assert isinstance(descriptor, property)

def test_marcador_has_numeroGolesEquipo2():
    assert hasattr(Marcador, "numeroGolesEquipo2")
    descriptor = None
    for klass in Marcador.__mro__:
        if "numeroGolesEquipo2" in klass.__dict__:
            descriptor = klass.__dict__["numeroGolesEquipo2"]
            break
    assert isinstance(descriptor, property)



def test_apuestaequipoganador_is_not_abstract():
    assert not inspect.isabstract(ApuestaEquipoGanador)


def test_apuestaequipoganador_constructor_exists():
    assert callable(ApuestaEquipoGanador.__init__)


def test_apuestaequipoganador_constructor_args():
    sig = inspect.signature(ApuestaEquipoGanador.__init__)
    params = list(sig.parameters.keys())
    assert "nombreEquipoGnador" in params, "Missing parameter 'nombreEquipoGnador'"

def test_apuestaequipoganador_has_nombreEquipoGnador():
    assert hasattr(ApuestaEquipoGanador, "nombreEquipoGnador")
    descriptor = None
    for klass in ApuestaEquipoGanador.__mro__:
        if "nombreEquipoGnador" in klass.__dict__:
            descriptor = klass.__dict__["nombreEquipoGnador"]
            break
    assert isinstance(descriptor, property)



def test_apuestamarcadorespecifico_is_not_abstract():
    assert not inspect.isabstract(ApuestaMarcadorEspecifico)


def test_apuestamarcadorespecifico_constructor_exists():
    assert callable(ApuestaMarcadorEspecifico.__init__)


def test_apuestamarcadorespecifico_constructor_args():
    sig = inspect.signature(ApuestaMarcadorEspecifico.__init__)
    params = list(sig.parameters.keys())
    assert "numeroGolesEquipo2" in params, "Missing parameter 'numeroGolesEquipo2'"
    assert "porcentajeAciertoMarcador" in params, "Missing parameter 'porcentajeAciertoMarcador'"
    assert "numeroGolesEquipo1" in params, "Missing parameter 'numeroGolesEquipo1'"
    assert "nombreEquipoGanador" in params, "Missing parameter 'nombreEquipoGanador'"

def test_apuestamarcadorespecifico_has_numeroGolesEquipo2():
    assert hasattr(ApuestaMarcadorEspecifico, "numeroGolesEquipo2")
    descriptor = None
    for klass in ApuestaMarcadorEspecifico.__mro__:
        if "numeroGolesEquipo2" in klass.__dict__:
            descriptor = klass.__dict__["numeroGolesEquipo2"]
            break
    assert isinstance(descriptor, property)

def test_apuestamarcadorespecifico_has_porcentajeAciertoMarcador():
    assert hasattr(ApuestaMarcadorEspecifico, "porcentajeAciertoMarcador")
    descriptor = None
    for klass in ApuestaMarcadorEspecifico.__mro__:
        if "porcentajeAciertoMarcador" in klass.__dict__:
            descriptor = klass.__dict__["porcentajeAciertoMarcador"]
            break
    assert isinstance(descriptor, property)

def test_apuestamarcadorespecifico_has_numeroGolesEquipo1():
    assert hasattr(ApuestaMarcadorEspecifico, "numeroGolesEquipo1")
    descriptor = None
    for klass in ApuestaMarcadorEspecifico.__mro__:
        if "numeroGolesEquipo1" in klass.__dict__:
            descriptor = klass.__dict__["numeroGolesEquipo1"]
            break
    assert isinstance(descriptor, property)

def test_apuestamarcadorespecifico_has_nombreEquipoGanador():
    assert hasattr(ApuestaMarcadorEspecifico, "nombreEquipoGanador")
    descriptor = None
    for klass in ApuestaMarcadorEspecifico.__mro__:
        if "nombreEquipoGanador" in klass.__dict__:
            descriptor = klass.__dict__["nombreEquipoGanador"]
            break
    assert isinstance(descriptor, property)



def test_partido_is_not_abstract():
    assert not inspect.isabstract(Partido)


def test_partido_constructor_exists():
    assert callable(Partido.__init__)


def test_partido_constructor_args():
    sig = inspect.signature(Partido.__init__)
    params = list(sig.parameters.keys())
    assert "idPartido" in params, "Missing parameter 'idPartido'"
    assert "numeroApuestas" in params, "Missing parameter 'numeroApuestas'"

def test_partido_has_idPartido():
    assert hasattr(Partido, "idPartido")
    descriptor = None
    for klass in Partido.__mro__:
        if "idPartido" in klass.__dict__:
            descriptor = klass.__dict__["idPartido"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_numeroApuestas():
    assert hasattr(Partido, "numeroApuestas")
    descriptor = None
    for klass in Partido.__mro__:
        if "numeroApuestas" in klass.__dict__:
            descriptor = klass.__dict__["numeroApuestas"]
            break
    assert isinstance(descriptor, property)



def test_apuesta_is_not_abstract():
    assert not inspect.isabstract(Apuesta)


def test_apuesta_constructor_exists():
    assert callable(Apuesta.__init__)


def test_apuesta_constructor_args():
    sig = inspect.signature(Apuesta.__init__)
    params = list(sig.parameters.keys())
    assert "valorApuesta" in params, "Missing parameter 'valorApuesta'"
    assert "porcentajeGanancia" in params, "Missing parameter 'porcentajeGanancia'"
    assert "id" in params, "Missing parameter 'id'"

def test_apuesta_has_valorApuesta():
    assert hasattr(Apuesta, "valorApuesta")
    descriptor = None
    for klass in Apuesta.__mro__:
        if "valorApuesta" in klass.__dict__:
            descriptor = klass.__dict__["valorApuesta"]
            break
    assert isinstance(descriptor, property)

def test_apuesta_has_porcentajeGanancia():
    assert hasattr(Apuesta, "porcentajeGanancia")
    descriptor = None
    for klass in Apuesta.__mro__:
        if "porcentajeGanancia" in klass.__dict__:
            descriptor = klass.__dict__["porcentajeGanancia"]
            break
    assert isinstance(descriptor, property)

def test_apuesta_has_id():
    assert hasattr(Apuesta, "id")
    descriptor = None
    for klass in Apuesta.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_usuario_is_not_abstract():
    assert not inspect.isabstract(Usuario)


def test_usuario_constructor_exists():
    assert callable(Usuario.__init__)


def test_usuario_constructor_args():
    sig = inspect.signature(Usuario.__init__)
    params = list(sig.parameters.keys())
    assert "passWord" in params, "Missing parameter 'passWord'"
    assert "userName" in params, "Missing parameter 'userName'"

def test_usuario_has_passWord():
    assert hasattr(Usuario, "passWord")
    descriptor = None
    for klass in Usuario.__mro__:
        if "passWord" in klass.__dict__:
            descriptor = klass.__dict__["passWord"]
            break
    assert isinstance(descriptor, property)

def test_usuario_has_userName():
    assert hasattr(Usuario, "userName")
    descriptor = None
    for klass in Usuario.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)



def test_tarjeta_is_not_abstract():
    assert not inspect.isabstract(Tarjeta)


def test_tarjeta_constructor_exists():
    assert callable(Tarjeta.__init__)


def test_tarjeta_constructor_args():
    sig = inspect.signature(Tarjeta.__init__)
    params = list(sig.parameters.keys())
    assert "numeroTarje" in params, "Missing parameter 'numeroTarje'"
    assert "codigoSeguridad" in params, "Missing parameter 'codigoSeguridad'"

def test_tarjeta_has_numeroTarje():
    assert hasattr(Tarjeta, "numeroTarje")
    descriptor = None
    for klass in Tarjeta.__mro__:
        if "numeroTarje" in klass.__dict__:
            descriptor = klass.__dict__["numeroTarje"]
            break
    assert isinstance(descriptor, property)

def test_tarjeta_has_codigoSeguridad():
    assert hasattr(Tarjeta, "codigoSeguridad")
    descriptor = None
    for klass in Tarjeta.__mro__:
        if "codigoSeguridad" in klass.__dict__:
            descriptor = klass.__dict__["codigoSeguridad"]
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
SistemaApuesta_strategy = st.builds(
    SistemaApuesta,
)
Historico_strategy = st.builds(
    Historico,
    numeroPartidosGanados=
        st.integers(),
    porcentajeApuestasEnFavor=
        safe_text,
    numeroPartidosPerdidos=
        st.integers(),
    numeroPartidosJugados=
        st.integers()
)
Equipo_strategy = st.builds(
    Equipo,
    jugadores=
        safe_text,
    nombre=
        safe_text,
    porcentajeFavoritismo=
        safe_text
)
Marcador_strategy = st.builds(
    Marcador,
    numeroGolesEquipo1=
        st.integers(),
    nombreEquipoGanador=
        safe_text,
    numeroGolesEquipo2=
        st.integers()
)
ApuestaEquipoGanador_strategy = st.builds(
    ApuestaEquipoGanador,
    nombreEquipoGnador=
        safe_text
)
ApuestaMarcadorEspecifico_strategy = st.builds(
    ApuestaMarcadorEspecifico,
    numeroGolesEquipo2=
        st.integers(),
    porcentajeAciertoMarcador=
        safe_text,
    numeroGolesEquipo1=
        st.integers(),
    nombreEquipoGanador=
        safe_text
)
Partido_strategy = st.builds(
    Partido,
    idPartido=
        safe_text,
    numeroApuestas=
        safe_text
)
Apuesta_strategy = st.builds(
    Apuesta,
    valorApuesta=
        safe_text,
    porcentajeGanancia=
        safe_text,
    id=
        safe_text
)
Usuario_strategy = st.builds(
    Usuario,
    passWord=
        safe_text,
    userName=
        safe_text
)
Tarjeta_strategy = st.builds(
    Tarjeta,
    numeroTarje=
        st.integers(),
    codigoSeguridad=
        st.integers()
)

@given(instance=SistemaApuesta_strategy)
@settings(max_examples=50)
def test_sistemaapuesta_instantiation(instance):
    assert isinstance(instance, SistemaApuesta)

@given(instance=Historico_strategy)
@settings(max_examples=50)
def test_historico_instantiation(instance):
    assert isinstance(instance, Historico)

@given(instance=Historico_strategy)
def test_historico_numeroPartidosGanados_type(instance):
    assert isinstance(instance.numeroPartidosGanados, int)


@given(instance=Historico_strategy)
def test_historico_numeroPartidosGanados_setter(instance):
    original = instance.numeroPartidosGanados
    instance.numeroPartidosGanados = original
    assert instance.numeroPartidosGanados == original

@given(instance=Historico_strategy)
def test_historico_porcentajeApuestasEnFavor_type(instance):
    assert isinstance(instance.porcentajeApuestasEnFavor, str)


@given(instance=Historico_strategy)
def test_historico_porcentajeApuestasEnFavor_setter(instance):
    original = instance.porcentajeApuestasEnFavor
    instance.porcentajeApuestasEnFavor = original
    assert instance.porcentajeApuestasEnFavor == original

@given(instance=Historico_strategy)
def test_historico_numeroPartidosPerdidos_type(instance):
    assert isinstance(instance.numeroPartidosPerdidos, int)


@given(instance=Historico_strategy)
def test_historico_numeroPartidosPerdidos_setter(instance):
    original = instance.numeroPartidosPerdidos
    instance.numeroPartidosPerdidos = original
    assert instance.numeroPartidosPerdidos == original

@given(instance=Historico_strategy)
def test_historico_numeroPartidosJugados_type(instance):
    assert isinstance(instance.numeroPartidosJugados, int)


@given(instance=Historico_strategy)
def test_historico_numeroPartidosJugados_setter(instance):
    original = instance.numeroPartidosJugados
    instance.numeroPartidosJugados = original
    assert instance.numeroPartidosJugados == original

@given(instance=Equipo_strategy)
@settings(max_examples=50)
def test_equipo_instantiation(instance):
    assert isinstance(instance, Equipo)

@given(instance=Equipo_strategy)
def test_equipo_jugadores_type(instance):
    assert isinstance(instance.jugadores, str)


@given(instance=Equipo_strategy)
def test_equipo_jugadores_setter(instance):
    original = instance.jugadores
    instance.jugadores = original
    assert instance.jugadores == original

@given(instance=Equipo_strategy)
def test_equipo_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=Equipo_strategy)
def test_equipo_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Equipo_strategy)
def test_equipo_porcentajeFavoritismo_type(instance):
    assert isinstance(instance.porcentajeFavoritismo, str)


@given(instance=Equipo_strategy)
def test_equipo_porcentajeFavoritismo_setter(instance):
    original = instance.porcentajeFavoritismo
    instance.porcentajeFavoritismo = original
    assert instance.porcentajeFavoritismo == original

@given(instance=Marcador_strategy)
@settings(max_examples=50)
def test_marcador_instantiation(instance):
    assert isinstance(instance, Marcador)

@given(instance=Marcador_strategy)
def test_marcador_numeroGolesEquipo1_type(instance):
    assert isinstance(instance.numeroGolesEquipo1, int)


@given(instance=Marcador_strategy)
def test_marcador_numeroGolesEquipo1_setter(instance):
    original = instance.numeroGolesEquipo1
    instance.numeroGolesEquipo1 = original
    assert instance.numeroGolesEquipo1 == original

@given(instance=Marcador_strategy)
def test_marcador_nombreEquipoGanador_type(instance):
    assert isinstance(instance.nombreEquipoGanador, str)


@given(instance=Marcador_strategy)
def test_marcador_nombreEquipoGanador_setter(instance):
    original = instance.nombreEquipoGanador
    instance.nombreEquipoGanador = original
    assert instance.nombreEquipoGanador == original

@given(instance=Marcador_strategy)
def test_marcador_numeroGolesEquipo2_type(instance):
    assert isinstance(instance.numeroGolesEquipo2, int)


@given(instance=Marcador_strategy)
def test_marcador_numeroGolesEquipo2_setter(instance):
    original = instance.numeroGolesEquipo2
    instance.numeroGolesEquipo2 = original
    assert instance.numeroGolesEquipo2 == original

@given(instance=ApuestaEquipoGanador_strategy)
@settings(max_examples=50)
def test_apuestaequipoganador_instantiation(instance):
    assert isinstance(instance, ApuestaEquipoGanador)

@given(instance=ApuestaEquipoGanador_strategy)
def test_apuestaequipoganador_nombreEquipoGnador_type(instance):
    assert isinstance(instance.nombreEquipoGnador, str)


@given(instance=ApuestaEquipoGanador_strategy)
def test_apuestaequipoganador_nombreEquipoGnador_setter(instance):
    original = instance.nombreEquipoGnador
    instance.nombreEquipoGnador = original
    assert instance.nombreEquipoGnador == original

@given(instance=ApuestaMarcadorEspecifico_strategy)
@settings(max_examples=50)
def test_apuestamarcadorespecifico_instantiation(instance):
    assert isinstance(instance, ApuestaMarcadorEspecifico)

@given(instance=ApuestaMarcadorEspecifico_strategy)
def test_apuestamarcadorespecifico_numeroGolesEquipo2_type(instance):
    assert isinstance(instance.numeroGolesEquipo2, int)


@given(instance=ApuestaMarcadorEspecifico_strategy)
def test_apuestamarcadorespecifico_numeroGolesEquipo2_setter(instance):
    original = instance.numeroGolesEquipo2
    instance.numeroGolesEquipo2 = original
    assert instance.numeroGolesEquipo2 == original

@given(instance=ApuestaMarcadorEspecifico_strategy)
def test_apuestamarcadorespecifico_porcentajeAciertoMarcador_type(instance):
    assert isinstance(instance.porcentajeAciertoMarcador, str)


@given(instance=ApuestaMarcadorEspecifico_strategy)
def test_apuestamarcadorespecifico_porcentajeAciertoMarcador_setter(instance):
    original = instance.porcentajeAciertoMarcador
    instance.porcentajeAciertoMarcador = original
    assert instance.porcentajeAciertoMarcador == original

@given(instance=ApuestaMarcadorEspecifico_strategy)
def test_apuestamarcadorespecifico_numeroGolesEquipo1_type(instance):
    assert isinstance(instance.numeroGolesEquipo1, int)


@given(instance=ApuestaMarcadorEspecifico_strategy)
def test_apuestamarcadorespecifico_numeroGolesEquipo1_setter(instance):
    original = instance.numeroGolesEquipo1
    instance.numeroGolesEquipo1 = original
    assert instance.numeroGolesEquipo1 == original

@given(instance=ApuestaMarcadorEspecifico_strategy)
def test_apuestamarcadorespecifico_nombreEquipoGanador_type(instance):
    assert isinstance(instance.nombreEquipoGanador, str)


@given(instance=ApuestaMarcadorEspecifico_strategy)
def test_apuestamarcadorespecifico_nombreEquipoGanador_setter(instance):
    original = instance.nombreEquipoGanador
    instance.nombreEquipoGanador = original
    assert instance.nombreEquipoGanador == original

@given(instance=Partido_strategy)
@settings(max_examples=50)
def test_partido_instantiation(instance):
    assert isinstance(instance, Partido)

@given(instance=Partido_strategy)
def test_partido_idPartido_type(instance):
    assert isinstance(instance.idPartido, str)


@given(instance=Partido_strategy)
def test_partido_idPartido_setter(instance):
    original = instance.idPartido
    instance.idPartido = original
    assert instance.idPartido == original

@given(instance=Partido_strategy)
def test_partido_numeroApuestas_type(instance):
    assert isinstance(instance.numeroApuestas, str)


@given(instance=Partido_strategy)
def test_partido_numeroApuestas_setter(instance):
    original = instance.numeroApuestas
    instance.numeroApuestas = original
    assert instance.numeroApuestas == original

@given(instance=Apuesta_strategy)
@settings(max_examples=50)
def test_apuesta_instantiation(instance):
    assert isinstance(instance, Apuesta)

@given(instance=Apuesta_strategy)
def test_apuesta_valorApuesta_type(instance):
    assert isinstance(instance.valorApuesta, str)


@given(instance=Apuesta_strategy)
def test_apuesta_valorApuesta_setter(instance):
    original = instance.valorApuesta
    instance.valorApuesta = original
    assert instance.valorApuesta == original

@given(instance=Apuesta_strategy)
def test_apuesta_porcentajeGanancia_type(instance):
    assert isinstance(instance.porcentajeGanancia, str)


@given(instance=Apuesta_strategy)
def test_apuesta_porcentajeGanancia_setter(instance):
    original = instance.porcentajeGanancia
    instance.porcentajeGanancia = original
    assert instance.porcentajeGanancia == original

@given(instance=Apuesta_strategy)
def test_apuesta_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Apuesta_strategy)
def test_apuesta_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Usuario_strategy)
@settings(max_examples=50)
def test_usuario_instantiation(instance):
    assert isinstance(instance, Usuario)

@given(instance=Usuario_strategy)
def test_usuario_passWord_type(instance):
    assert isinstance(instance.passWord, str)


@given(instance=Usuario_strategy)
def test_usuario_passWord_setter(instance):
    original = instance.passWord
    instance.passWord = original
    assert instance.passWord == original

@given(instance=Usuario_strategy)
def test_usuario_userName_type(instance):
    assert isinstance(instance.userName, str)


@given(instance=Usuario_strategy)
def test_usuario_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=Tarjeta_strategy)
@settings(max_examples=50)
def test_tarjeta_instantiation(instance):
    assert isinstance(instance, Tarjeta)

@given(instance=Tarjeta_strategy)
def test_tarjeta_numeroTarje_type(instance):
    assert isinstance(instance.numeroTarje, int)


@given(instance=Tarjeta_strategy)
def test_tarjeta_numeroTarje_setter(instance):
    original = instance.numeroTarje
    instance.numeroTarje = original
    assert instance.numeroTarje == original

@given(instance=Tarjeta_strategy)
def test_tarjeta_codigoSeguridad_type(instance):
    assert isinstance(instance.codigoSeguridad, int)


@given(instance=Tarjeta_strategy)
def test_tarjeta_codigoSeguridad_setter(instance):
    original = instance.codigoSeguridad
    instance.codigoSeguridad = original
    assert instance.codigoSeguridad == original
