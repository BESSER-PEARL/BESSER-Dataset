import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Estadio,
    Persona,
    Clasificacion,
    Liga,
    Lesion,
    TipoDeEvento,
    Evento,
    Partido,
    Arbitro,
    Entrenador,
    Jugador,
    Equipo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_estadio_is_not_abstract():
    assert not inspect.isabstract(Estadio)


def test_estadio_constructor_exists():
    assert callable(Estadio.__init__)


def test_estadio_constructor_args():
    sig = inspect.signature(Estadio.__init__)
    params = list(sig.parameters.keys())
    assert "Cod_Estadio" in params, "Missing parameter 'Cod_Estadio'"
    assert "Capacidad" in params, "Missing parameter 'Capacidad'"
    assert "Ubicacion" in params, "Missing parameter 'Ubicacion'"
    assert "Ubicacion1" in params, "Missing parameter 'Ubicacion1'"
    assert "Terreno" in params, "Missing parameter 'Terreno'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "Cod_equipo" in params, "Missing parameter 'Cod_equipo'"

def test_estadio_has_Cod_Estadio():
    assert hasattr(Estadio, "Cod_Estadio")
    descriptor = None
    for klass in Estadio.__mro__:
        if "Cod_Estadio" in klass.__dict__:
            descriptor = klass.__dict__["Cod_Estadio"]
            break
    assert isinstance(descriptor, property)

def test_estadio_has_Capacidad():
    assert hasattr(Estadio, "Capacidad")
    descriptor = None
    for klass in Estadio.__mro__:
        if "Capacidad" in klass.__dict__:
            descriptor = klass.__dict__["Capacidad"]
            break
    assert isinstance(descriptor, property)

def test_estadio_has_Ubicacion():
    assert hasattr(Estadio, "Ubicacion")
    descriptor = None
    for klass in Estadio.__mro__:
        if "Ubicacion" in klass.__dict__:
            descriptor = klass.__dict__["Ubicacion"]
            break
    assert isinstance(descriptor, property)

def test_estadio_has_Ubicacion1():
    assert hasattr(Estadio, "Ubicacion1")
    descriptor = None
    for klass in Estadio.__mro__:
        if "Ubicacion1" in klass.__dict__:
            descriptor = klass.__dict__["Ubicacion1"]
            break
    assert isinstance(descriptor, property)

def test_estadio_has_Terreno():
    assert hasattr(Estadio, "Terreno")
    descriptor = None
    for klass in Estadio.__mro__:
        if "Terreno" in klass.__dict__:
            descriptor = klass.__dict__["Terreno"]
            break
    assert isinstance(descriptor, property)

def test_estadio_has_Nombre():
    assert hasattr(Estadio, "Nombre")
    descriptor = None
    for klass in Estadio.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)

def test_estadio_has_Cod_equipo():
    assert hasattr(Estadio, "Cod_equipo")
    descriptor = None
    for klass in Estadio.__mro__:
        if "Cod_equipo" in klass.__dict__:
            descriptor = klass.__dict__["Cod_equipo"]
            break
    assert isinstance(descriptor, property)



def test_persona_is_not_abstract():
    assert not inspect.isabstract(Persona)


def test_persona_constructor_exists():
    assert callable(Persona.__init__)


def test_persona_constructor_args():
    sig = inspect.signature(Persona.__init__)
    params = list(sig.parameters.keys())
    assert "Apellido" in params, "Missing parameter 'Apellido'"
    assert "Cod_persona" in params, "Missing parameter 'Cod_persona'"
    assert "NombreCorto" in params, "Missing parameter 'NombreCorto'"
    assert "Nacionalidad" in params, "Missing parameter 'Nacionalidad'"
    assert "FechaNacimiento" in params, "Missing parameter 'FechaNacimiento'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"

def test_persona_has_Apellido():
    assert hasattr(Persona, "Apellido")
    descriptor = None
    for klass in Persona.__mro__:
        if "Apellido" in klass.__dict__:
            descriptor = klass.__dict__["Apellido"]
            break
    assert isinstance(descriptor, property)

def test_persona_has_Cod_persona():
    assert hasattr(Persona, "Cod_persona")
    descriptor = None
    for klass in Persona.__mro__:
        if "Cod_persona" in klass.__dict__:
            descriptor = klass.__dict__["Cod_persona"]
            break
    assert isinstance(descriptor, property)

def test_persona_has_NombreCorto():
    assert hasattr(Persona, "NombreCorto")
    descriptor = None
    for klass in Persona.__mro__:
        if "NombreCorto" in klass.__dict__:
            descriptor = klass.__dict__["NombreCorto"]
            break
    assert isinstance(descriptor, property)

def test_persona_has_Nacionalidad():
    assert hasattr(Persona, "Nacionalidad")
    descriptor = None
    for klass in Persona.__mro__:
        if "Nacionalidad" in klass.__dict__:
            descriptor = klass.__dict__["Nacionalidad"]
            break
    assert isinstance(descriptor, property)

def test_persona_has_FechaNacimiento():
    assert hasattr(Persona, "FechaNacimiento")
    descriptor = None
    for klass in Persona.__mro__:
        if "FechaNacimiento" in klass.__dict__:
            descriptor = klass.__dict__["FechaNacimiento"]
            break
    assert isinstance(descriptor, property)

def test_persona_has_Nombre():
    assert hasattr(Persona, "Nombre")
    descriptor = None
    for klass in Persona.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)



def test_clasificacion_is_not_abstract():
    assert not inspect.isabstract(Clasificacion)


def test_clasificacion_constructor_exists():
    assert callable(Clasificacion.__init__)


def test_clasificacion_constructor_args():
    sig = inspect.signature(Clasificacion.__init__)
    params = list(sig.parameters.keys())
    assert "JE" in params, "Missing parameter 'JE'"
    assert "Puntos" in params, "Missing parameter 'Puntos'"
    assert "DG" in params, "Missing parameter 'DG'"
    assert "JJ" in params, "Missing parameter 'JJ'"
    assert "GC" in params, "Missing parameter 'GC'"
    assert "Posicion" in params, "Missing parameter 'Posicion'"
    assert "Cod_Equipo" in params, "Missing parameter 'Cod_Equipo'"
    assert "JG" in params, "Missing parameter 'JG'"
    assert "GF" in params, "Missing parameter 'GF'"
    assert "JP" in params, "Missing parameter 'JP'"

def test_clasificacion_has_JE():
    assert hasattr(Clasificacion, "JE")
    descriptor = None
    for klass in Clasificacion.__mro__:
        if "JE" in klass.__dict__:
            descriptor = klass.__dict__["JE"]
            break
    assert isinstance(descriptor, property)

def test_clasificacion_has_Puntos():
    assert hasattr(Clasificacion, "Puntos")
    descriptor = None
    for klass in Clasificacion.__mro__:
        if "Puntos" in klass.__dict__:
            descriptor = klass.__dict__["Puntos"]
            break
    assert isinstance(descriptor, property)

def test_clasificacion_has_DG():
    assert hasattr(Clasificacion, "DG")
    descriptor = None
    for klass in Clasificacion.__mro__:
        if "DG" in klass.__dict__:
            descriptor = klass.__dict__["DG"]
            break
    assert isinstance(descriptor, property)

def test_clasificacion_has_JJ():
    assert hasattr(Clasificacion, "JJ")
    descriptor = None
    for klass in Clasificacion.__mro__:
        if "JJ" in klass.__dict__:
            descriptor = klass.__dict__["JJ"]
            break
    assert isinstance(descriptor, property)

def test_clasificacion_has_GC():
    assert hasattr(Clasificacion, "GC")
    descriptor = None
    for klass in Clasificacion.__mro__:
        if "GC" in klass.__dict__:
            descriptor = klass.__dict__["GC"]
            break
    assert isinstance(descriptor, property)

def test_clasificacion_has_Posicion():
    assert hasattr(Clasificacion, "Posicion")
    descriptor = None
    for klass in Clasificacion.__mro__:
        if "Posicion" in klass.__dict__:
            descriptor = klass.__dict__["Posicion"]
            break
    assert isinstance(descriptor, property)

def test_clasificacion_has_Cod_Equipo():
    assert hasattr(Clasificacion, "Cod_Equipo")
    descriptor = None
    for klass in Clasificacion.__mro__:
        if "Cod_Equipo" in klass.__dict__:
            descriptor = klass.__dict__["Cod_Equipo"]
            break
    assert isinstance(descriptor, property)

def test_clasificacion_has_JG():
    assert hasattr(Clasificacion, "JG")
    descriptor = None
    for klass in Clasificacion.__mro__:
        if "JG" in klass.__dict__:
            descriptor = klass.__dict__["JG"]
            break
    assert isinstance(descriptor, property)

def test_clasificacion_has_GF():
    assert hasattr(Clasificacion, "GF")
    descriptor = None
    for klass in Clasificacion.__mro__:
        if "GF" in klass.__dict__:
            descriptor = klass.__dict__["GF"]
            break
    assert isinstance(descriptor, property)

def test_clasificacion_has_JP():
    assert hasattr(Clasificacion, "JP")
    descriptor = None
    for klass in Clasificacion.__mro__:
        if "JP" in klass.__dict__:
            descriptor = klass.__dict__["JP"]
            break
    assert isinstance(descriptor, property)



def test_liga_is_not_abstract():
    assert not inspect.isabstract(Liga)


def test_liga_constructor_exists():
    assert callable(Liga.__init__)


def test_liga_constructor_args():
    sig = inspect.signature(Liga.__init__)
    params = list(sig.parameters.keys())
    assert "Cod_Clasificacion" in params, "Missing parameter 'Cod_Clasificacion'"
    assert "Cod_liga" in params, "Missing parameter 'Cod_liga'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "Num_equipos" in params, "Missing parameter 'Num_equipos'"
    assert "Inferior" in params, "Missing parameter 'Inferior'"
    assert "Superior" in params, "Missing parameter 'Superior'"

def test_liga_has_Cod_Clasificacion():
    assert hasattr(Liga, "Cod_Clasificacion")
    descriptor = None
    for klass in Liga.__mro__:
        if "Cod_Clasificacion" in klass.__dict__:
            descriptor = klass.__dict__["Cod_Clasificacion"]
            break
    assert isinstance(descriptor, property)

def test_liga_has_Cod_liga():
    assert hasattr(Liga, "Cod_liga")
    descriptor = None
    for klass in Liga.__mro__:
        if "Cod_liga" in klass.__dict__:
            descriptor = klass.__dict__["Cod_liga"]
            break
    assert isinstance(descriptor, property)

def test_liga_has_Nombre():
    assert hasattr(Liga, "Nombre")
    descriptor = None
    for klass in Liga.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)

def test_liga_has_Num_equipos():
    assert hasattr(Liga, "Num_equipos")
    descriptor = None
    for klass in Liga.__mro__:
        if "Num_equipos" in klass.__dict__:
            descriptor = klass.__dict__["Num_equipos"]
            break
    assert isinstance(descriptor, property)

def test_liga_has_Inferior():
    assert hasattr(Liga, "Inferior")
    descriptor = None
    for klass in Liga.__mro__:
        if "Inferior" in klass.__dict__:
            descriptor = klass.__dict__["Inferior"]
            break
    assert isinstance(descriptor, property)

def test_liga_has_Superior():
    assert hasattr(Liga, "Superior")
    descriptor = None
    for klass in Liga.__mro__:
        if "Superior" in klass.__dict__:
            descriptor = klass.__dict__["Superior"]
            break
    assert isinstance(descriptor, property)



def test_lesion_is_not_abstract():
    assert not inspect.isabstract(Lesion)


def test_lesion_constructor_exists():
    assert callable(Lesion.__init__)


def test_lesion_constructor_args():
    sig = inspect.signature(Lesion.__init__)
    params = list(sig.parameters.keys())
    assert "Condicion" in params, "Missing parameter 'Condicion'"
    assert "Cod_jugador" in params, "Missing parameter 'Cod_jugador'"
    assert "FechaLesion" in params, "Missing parameter 'FechaLesion'"
    assert "TiempoLesion" in params, "Missing parameter 'TiempoLesion'"

def test_lesion_has_Condicion():
    assert hasattr(Lesion, "Condicion")
    descriptor = None
    for klass in Lesion.__mro__:
        if "Condicion" in klass.__dict__:
            descriptor = klass.__dict__["Condicion"]
            break
    assert isinstance(descriptor, property)

def test_lesion_has_Cod_jugador():
    assert hasattr(Lesion, "Cod_jugador")
    descriptor = None
    for klass in Lesion.__mro__:
        if "Cod_jugador" in klass.__dict__:
            descriptor = klass.__dict__["Cod_jugador"]
            break
    assert isinstance(descriptor, property)

def test_lesion_has_FechaLesion():
    assert hasattr(Lesion, "FechaLesion")
    descriptor = None
    for klass in Lesion.__mro__:
        if "FechaLesion" in klass.__dict__:
            descriptor = klass.__dict__["FechaLesion"]
            break
    assert isinstance(descriptor, property)

def test_lesion_has_TiempoLesion():
    assert hasattr(Lesion, "TiempoLesion")
    descriptor = None
    for klass in Lesion.__mro__:
        if "TiempoLesion" in klass.__dict__:
            descriptor = klass.__dict__["TiempoLesion"]
            break
    assert isinstance(descriptor, property)



def test_tipodeevento_is_not_abstract():
    assert not inspect.isabstract(TipoDeEvento)


def test_tipodeevento_constructor_exists():
    assert callable(TipoDeEvento.__init__)


def test_tipodeevento_constructor_args():
    sig = inspect.signature(TipoDeEvento.__init__)
    params = list(sig.parameters.keys())
    assert "Evento" in params, "Missing parameter 'Evento'"
    assert "Cod_TipodeEvento" in params, "Missing parameter 'Cod_TipodeEvento'"

def test_tipodeevento_has_Evento():
    assert hasattr(TipoDeEvento, "Evento")
    descriptor = None
    for klass in TipoDeEvento.__mro__:
        if "Evento" in klass.__dict__:
            descriptor = klass.__dict__["Evento"]
            break
    assert isinstance(descriptor, property)

def test_tipodeevento_has_Cod_TipodeEvento():
    assert hasattr(TipoDeEvento, "Cod_TipodeEvento")
    descriptor = None
    for klass in TipoDeEvento.__mro__:
        if "Cod_TipodeEvento" in klass.__dict__:
            descriptor = klass.__dict__["Cod_TipodeEvento"]
            break
    assert isinstance(descriptor, property)



def test_evento_is_not_abstract():
    assert not inspect.isabstract(Evento)


def test_evento_constructor_exists():
    assert callable(Evento.__init__)


def test_evento_constructor_args():
    sig = inspect.signature(Evento.__init__)
    params = list(sig.parameters.keys())
    assert "Cod_TipodeEvento" in params, "Missing parameter 'Cod_TipodeEvento'"
    assert "Cod_partido" in params, "Missing parameter 'Cod_partido'"
    assert "Cod_jugador" in params, "Missing parameter 'Cod_jugador'"

def test_evento_has_Cod_TipodeEvento():
    assert hasattr(Evento, "Cod_TipodeEvento")
    descriptor = None
    for klass in Evento.__mro__:
        if "Cod_TipodeEvento" in klass.__dict__:
            descriptor = klass.__dict__["Cod_TipodeEvento"]
            break
    assert isinstance(descriptor, property)

def test_evento_has_Cod_partido():
    assert hasattr(Evento, "Cod_partido")
    descriptor = None
    for klass in Evento.__mro__:
        if "Cod_partido" in klass.__dict__:
            descriptor = klass.__dict__["Cod_partido"]
            break
    assert isinstance(descriptor, property)

def test_evento_has_Cod_jugador():
    assert hasattr(Evento, "Cod_jugador")
    descriptor = None
    for klass in Evento.__mro__:
        if "Cod_jugador" in klass.__dict__:
            descriptor = klass.__dict__["Cod_jugador"]
            break
    assert isinstance(descriptor, property)



def test_partido_is_not_abstract():
    assert not inspect.isabstract(Partido)


def test_partido_constructor_exists():
    assert callable(Partido.__init__)


def test_partido_constructor_args():
    sig = inspect.signature(Partido.__init__)
    params = list(sig.parameters.keys())
    assert "GolLocal" in params, "Missing parameter 'GolLocal'"
    assert "GolVisita" in params, "Missing parameter 'GolVisita'"
    assert "Cod_partido" in params, "Missing parameter 'Cod_partido'"
    assert "Hora" in params, "Missing parameter 'Hora'"
    assert "Ganador" in params, "Missing parameter 'Ganador'"
    assert "Local" in params, "Missing parameter 'Local'"
    assert "Visita" in params, "Missing parameter 'Visita'"
    assert "Fecha" in params, "Missing parameter 'Fecha'"
    assert "Cod_liga" in params, "Missing parameter 'Cod_liga'"

def test_partido_has_GolLocal():
    assert hasattr(Partido, "GolLocal")
    descriptor = None
    for klass in Partido.__mro__:
        if "GolLocal" in klass.__dict__:
            descriptor = klass.__dict__["GolLocal"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_GolVisita():
    assert hasattr(Partido, "GolVisita")
    descriptor = None
    for klass in Partido.__mro__:
        if "GolVisita" in klass.__dict__:
            descriptor = klass.__dict__["GolVisita"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_Cod_partido():
    assert hasattr(Partido, "Cod_partido")
    descriptor = None
    for klass in Partido.__mro__:
        if "Cod_partido" in klass.__dict__:
            descriptor = klass.__dict__["Cod_partido"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_Hora():
    assert hasattr(Partido, "Hora")
    descriptor = None
    for klass in Partido.__mro__:
        if "Hora" in klass.__dict__:
            descriptor = klass.__dict__["Hora"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_Ganador():
    assert hasattr(Partido, "Ganador")
    descriptor = None
    for klass in Partido.__mro__:
        if "Ganador" in klass.__dict__:
            descriptor = klass.__dict__["Ganador"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_Local():
    assert hasattr(Partido, "Local")
    descriptor = None
    for klass in Partido.__mro__:
        if "Local" in klass.__dict__:
            descriptor = klass.__dict__["Local"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_Visita():
    assert hasattr(Partido, "Visita")
    descriptor = None
    for klass in Partido.__mro__:
        if "Visita" in klass.__dict__:
            descriptor = klass.__dict__["Visita"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_Fecha():
    assert hasattr(Partido, "Fecha")
    descriptor = None
    for klass in Partido.__mro__:
        if "Fecha" in klass.__dict__:
            descriptor = klass.__dict__["Fecha"]
            break
    assert isinstance(descriptor, property)

def test_partido_has_Cod_liga():
    assert hasattr(Partido, "Cod_liga")
    descriptor = None
    for klass in Partido.__mro__:
        if "Cod_liga" in klass.__dict__:
            descriptor = klass.__dict__["Cod_liga"]
            break
    assert isinstance(descriptor, property)



def test_arbitro_is_not_abstract():
    assert not inspect.isabstract(Arbitro)


def test_arbitro_constructor_exists():
    assert callable(Arbitro.__init__)


def test_arbitro_constructor_args():
    sig = inspect.signature(Arbitro.__init__)
    params = list(sig.parameters.keys())
    assert "Cod_Arbitro" in params, "Missing parameter 'Cod_Arbitro'"
    assert "Partidos" in params, "Missing parameter 'Partidos'"
    assert "Cod_persona" in params, "Missing parameter 'Cod_persona'"

def test_arbitro_has_Cod_Arbitro():
    assert hasattr(Arbitro, "Cod_Arbitro")
    descriptor = None
    for klass in Arbitro.__mro__:
        if "Cod_Arbitro" in klass.__dict__:
            descriptor = klass.__dict__["Cod_Arbitro"]
            break
    assert isinstance(descriptor, property)

def test_arbitro_has_Partidos():
    assert hasattr(Arbitro, "Partidos")
    descriptor = None
    for klass in Arbitro.__mro__:
        if "Partidos" in klass.__dict__:
            descriptor = klass.__dict__["Partidos"]
            break
    assert isinstance(descriptor, property)

def test_arbitro_has_Cod_persona():
    assert hasattr(Arbitro, "Cod_persona")
    descriptor = None
    for klass in Arbitro.__mro__:
        if "Cod_persona" in klass.__dict__:
            descriptor = klass.__dict__["Cod_persona"]
            break
    assert isinstance(descriptor, property)



def test_entrenador_is_not_abstract():
    assert not inspect.isabstract(Entrenador)


def test_entrenador_constructor_exists():
    assert callable(Entrenador.__init__)


def test_entrenador_constructor_args():
    sig = inspect.signature(Entrenador.__init__)
    params = list(sig.parameters.keys())
    assert "Titulos" in params, "Missing parameter 'Titulos'"
    assert "Cod_Entrenador" in params, "Missing parameter 'Cod_Entrenador'"
    assert "Cod_persona" in params, "Missing parameter 'Cod_persona'"

def test_entrenador_has_Titulos():
    assert hasattr(Entrenador, "Titulos")
    descriptor = None
    for klass in Entrenador.__mro__:
        if "Titulos" in klass.__dict__:
            descriptor = klass.__dict__["Titulos"]
            break
    assert isinstance(descriptor, property)

def test_entrenador_has_Cod_Entrenador():
    assert hasattr(Entrenador, "Cod_Entrenador")
    descriptor = None
    for klass in Entrenador.__mro__:
        if "Cod_Entrenador" in klass.__dict__:
            descriptor = klass.__dict__["Cod_Entrenador"]
            break
    assert isinstance(descriptor, property)

def test_entrenador_has_Cod_persona():
    assert hasattr(Entrenador, "Cod_persona")
    descriptor = None
    for klass in Entrenador.__mro__:
        if "Cod_persona" in klass.__dict__:
            descriptor = klass.__dict__["Cod_persona"]
            break
    assert isinstance(descriptor, property)



def test_jugador_is_not_abstract():
    assert not inspect.isabstract(Jugador)


def test_jugador_constructor_exists():
    assert callable(Jugador.__init__)


def test_jugador_constructor_args():
    sig = inspect.signature(Jugador.__init__)
    params = list(sig.parameters.keys())
    assert "Titulos" in params, "Missing parameter 'Titulos'"
    assert "Altura" in params, "Missing parameter 'Altura'"
    assert "Posicion" in params, "Missing parameter 'Posicion'"
    assert "Cod_equipo" in params, "Missing parameter 'Cod_equipo'"
    assert "Cod_jugador" in params, "Missing parameter 'Cod_jugador'"
    assert "Cod_persona" in params, "Missing parameter 'Cod_persona'"
    assert "Peso" in params, "Missing parameter 'Peso'"
    assert "Dorsal" in params, "Missing parameter 'Dorsal'"

def test_jugador_has_Titulos():
    assert hasattr(Jugador, "Titulos")
    descriptor = None
    for klass in Jugador.__mro__:
        if "Titulos" in klass.__dict__:
            descriptor = klass.__dict__["Titulos"]
            break
    assert isinstance(descriptor, property)

def test_jugador_has_Altura():
    assert hasattr(Jugador, "Altura")
    descriptor = None
    for klass in Jugador.__mro__:
        if "Altura" in klass.__dict__:
            descriptor = klass.__dict__["Altura"]
            break
    assert isinstance(descriptor, property)

def test_jugador_has_Posicion():
    assert hasattr(Jugador, "Posicion")
    descriptor = None
    for klass in Jugador.__mro__:
        if "Posicion" in klass.__dict__:
            descriptor = klass.__dict__["Posicion"]
            break
    assert isinstance(descriptor, property)

def test_jugador_has_Cod_equipo():
    assert hasattr(Jugador, "Cod_equipo")
    descriptor = None
    for klass in Jugador.__mro__:
        if "Cod_equipo" in klass.__dict__:
            descriptor = klass.__dict__["Cod_equipo"]
            break
    assert isinstance(descriptor, property)

def test_jugador_has_Cod_jugador():
    assert hasattr(Jugador, "Cod_jugador")
    descriptor = None
    for klass in Jugador.__mro__:
        if "Cod_jugador" in klass.__dict__:
            descriptor = klass.__dict__["Cod_jugador"]
            break
    assert isinstance(descriptor, property)

def test_jugador_has_Cod_persona():
    assert hasattr(Jugador, "Cod_persona")
    descriptor = None
    for klass in Jugador.__mro__:
        if "Cod_persona" in klass.__dict__:
            descriptor = klass.__dict__["Cod_persona"]
            break
    assert isinstance(descriptor, property)

def test_jugador_has_Peso():
    assert hasattr(Jugador, "Peso")
    descriptor = None
    for klass in Jugador.__mro__:
        if "Peso" in klass.__dict__:
            descriptor = klass.__dict__["Peso"]
            break
    assert isinstance(descriptor, property)

def test_jugador_has_Dorsal():
    assert hasattr(Jugador, "Dorsal")
    descriptor = None
    for klass in Jugador.__mro__:
        if "Dorsal" in klass.__dict__:
            descriptor = klass.__dict__["Dorsal"]
            break
    assert isinstance(descriptor, property)



def test_equipo_is_not_abstract():
    assert not inspect.isabstract(Equipo)


def test_equipo_constructor_exists():
    assert callable(Equipo.__init__)


def test_equipo_constructor_args():
    sig = inspect.signature(Equipo.__init__)
    params = list(sig.parameters.keys())
    assert "Cod_equipo" in params, "Missing parameter 'Cod_equipo'"
    assert "Titulos" in params, "Missing parameter 'Titulos'"
    assert "F_fundacion" in params, "Missing parameter 'F_fundacion'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "Cod_Entrenador" in params, "Missing parameter 'Cod_Entrenador'"
    assert "Ciudad" in params, "Missing parameter 'Ciudad'"

def test_equipo_has_Cod_equipo():
    assert hasattr(Equipo, "Cod_equipo")
    descriptor = None
    for klass in Equipo.__mro__:
        if "Cod_equipo" in klass.__dict__:
            descriptor = klass.__dict__["Cod_equipo"]
            break
    assert isinstance(descriptor, property)

def test_equipo_has_Titulos():
    assert hasattr(Equipo, "Titulos")
    descriptor = None
    for klass in Equipo.__mro__:
        if "Titulos" in klass.__dict__:
            descriptor = klass.__dict__["Titulos"]
            break
    assert isinstance(descriptor, property)

def test_equipo_has_F_fundacion():
    assert hasattr(Equipo, "F_fundacion")
    descriptor = None
    for klass in Equipo.__mro__:
        if "F_fundacion" in klass.__dict__:
            descriptor = klass.__dict__["F_fundacion"]
            break
    assert isinstance(descriptor, property)

def test_equipo_has_Nombre():
    assert hasattr(Equipo, "Nombre")
    descriptor = None
    for klass in Equipo.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)

def test_equipo_has_Cod_Entrenador():
    assert hasattr(Equipo, "Cod_Entrenador")
    descriptor = None
    for klass in Equipo.__mro__:
        if "Cod_Entrenador" in klass.__dict__:
            descriptor = klass.__dict__["Cod_Entrenador"]
            break
    assert isinstance(descriptor, property)

def test_equipo_has_Ciudad():
    assert hasattr(Equipo, "Ciudad")
    descriptor = None
    for klass in Equipo.__mro__:
        if "Ciudad" in klass.__dict__:
            descriptor = klass.__dict__["Ciudad"]
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
Estadio_strategy = st.builds(
    Estadio,
    Cod_Estadio=
        safe_text,
    Capacidad=
        safe_text,
    Ubicacion=
        safe_text,
    Ubicacion1=
        safe_text,
    Terreno=
        safe_text,
    Nombre=
        safe_text,
    Cod_equipo=
        safe_text
)
Persona_strategy = st.builds(
    Persona,
    Apellido=
        safe_text,
    Cod_persona=
        safe_text,
    NombreCorto=
        safe_text,
    Nacionalidad=
        safe_text,
    FechaNacimiento=
        safe_text,
    Nombre=
        safe_text
)
Clasificacion_strategy = st.builds(
    Clasificacion,
    JE=
        safe_text,
    Puntos=
        safe_text,
    DG=
        safe_text,
    JJ=
        safe_text,
    GC=
        safe_text,
    Posicion=
        safe_text,
    Cod_Equipo=
        safe_text,
    JG=
        safe_text,
    GF=
        safe_text,
    JP=
        safe_text
)
Liga_strategy = st.builds(
    Liga,
    Cod_Clasificacion=
        safe_text,
    Cod_liga=
        safe_text,
    Nombre=
        safe_text,
    Num_equipos=
        safe_text,
    Inferior=
        safe_text,
    Superior=
        safe_text
)
Lesion_strategy = st.builds(
    Lesion,
    Condicion=
        safe_text,
    Cod_jugador=
        safe_text,
    FechaLesion=
        safe_text,
    TiempoLesion=
        safe_text
)
TipoDeEvento_strategy = st.builds(
    TipoDeEvento,
    Evento=
        safe_text,
    Cod_TipodeEvento=
        safe_text
)
Evento_strategy = st.builds(
    Evento,
    Cod_TipodeEvento=
        safe_text,
    Cod_partido=
        safe_text,
    Cod_jugador=
        safe_text
)
Partido_strategy = st.builds(
    Partido,
    GolLocal=
        safe_text,
    GolVisita=
        safe_text,
    Cod_partido=
        safe_text,
    Hora=
        safe_text,
    Ganador=
        safe_text,
    Local=
        safe_text,
    Visita=
        safe_text,
    Fecha=
        safe_text,
    Cod_liga=
        safe_text
)
Arbitro_strategy = st.builds(
    Arbitro,
    Cod_Arbitro=
        safe_text,
    Partidos=
        safe_text,
    Cod_persona=
        safe_text
)
Entrenador_strategy = st.builds(
    Entrenador,
    Titulos=
        safe_text,
    Cod_Entrenador=
        safe_text,
    Cod_persona=
        safe_text
)
Jugador_strategy = st.builds(
    Jugador,
    Titulos=
        safe_text,
    Altura=
        safe_text,
    Posicion=
        safe_text,
    Cod_equipo=
        safe_text,
    Cod_jugador=
        safe_text,
    Cod_persona=
        safe_text,
    Peso=
        safe_text,
    Dorsal=
        safe_text
)
Equipo_strategy = st.builds(
    Equipo,
    Cod_equipo=
        safe_text,
    Titulos=
        safe_text,
    F_fundacion=
        safe_text,
    Nombre=
        safe_text,
    Cod_Entrenador=
        safe_text,
    Ciudad=
        safe_text
)

@given(instance=Estadio_strategy)
@settings(max_examples=50)
def test_estadio_instantiation(instance):
    assert isinstance(instance, Estadio)



@given(instance=Estadio_strategy)
def test_estadio_Cod_Estadio_setter(instance):
    original = instance.Cod_Estadio
    instance.Cod_Estadio = original
    assert instance.Cod_Estadio == original



@given(instance=Estadio_strategy)
def test_estadio_Capacidad_setter(instance):
    original = instance.Capacidad
    instance.Capacidad = original
    assert instance.Capacidad == original



@given(instance=Estadio_strategy)
def test_estadio_Ubicacion_setter(instance):
    original = instance.Ubicacion
    instance.Ubicacion = original
    assert instance.Ubicacion == original



@given(instance=Estadio_strategy)
def test_estadio_Ubicacion1_setter(instance):
    original = instance.Ubicacion1
    instance.Ubicacion1 = original
    assert instance.Ubicacion1 == original



@given(instance=Estadio_strategy)
def test_estadio_Terreno_setter(instance):
    original = instance.Terreno
    instance.Terreno = original
    assert instance.Terreno == original



@given(instance=Estadio_strategy)
def test_estadio_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=Estadio_strategy)
def test_estadio_Cod_equipo_setter(instance):
    original = instance.Cod_equipo
    instance.Cod_equipo = original
    assert instance.Cod_equipo == original

@given(instance=Persona_strategy)
@settings(max_examples=50)
def test_persona_instantiation(instance):
    assert isinstance(instance, Persona)



@given(instance=Persona_strategy)
def test_persona_Apellido_setter(instance):
    original = instance.Apellido
    instance.Apellido = original
    assert instance.Apellido == original



@given(instance=Persona_strategy)
def test_persona_Cod_persona_setter(instance):
    original = instance.Cod_persona
    instance.Cod_persona = original
    assert instance.Cod_persona == original



@given(instance=Persona_strategy)
def test_persona_NombreCorto_setter(instance):
    original = instance.NombreCorto
    instance.NombreCorto = original
    assert instance.NombreCorto == original



@given(instance=Persona_strategy)
def test_persona_Nacionalidad_setter(instance):
    original = instance.Nacionalidad
    instance.Nacionalidad = original
    assert instance.Nacionalidad == original



@given(instance=Persona_strategy)
def test_persona_FechaNacimiento_setter(instance):
    original = instance.FechaNacimiento
    instance.FechaNacimiento = original
    assert instance.FechaNacimiento == original



@given(instance=Persona_strategy)
def test_persona_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original

@given(instance=Clasificacion_strategy)
@settings(max_examples=50)
def test_clasificacion_instantiation(instance):
    assert isinstance(instance, Clasificacion)



@given(instance=Clasificacion_strategy)
def test_clasificacion_JE_setter(instance):
    original = instance.JE
    instance.JE = original
    assert instance.JE == original



@given(instance=Clasificacion_strategy)
def test_clasificacion_Puntos_setter(instance):
    original = instance.Puntos
    instance.Puntos = original
    assert instance.Puntos == original



@given(instance=Clasificacion_strategy)
def test_clasificacion_DG_setter(instance):
    original = instance.DG
    instance.DG = original
    assert instance.DG == original



@given(instance=Clasificacion_strategy)
def test_clasificacion_JJ_setter(instance):
    original = instance.JJ
    instance.JJ = original
    assert instance.JJ == original



@given(instance=Clasificacion_strategy)
def test_clasificacion_GC_setter(instance):
    original = instance.GC
    instance.GC = original
    assert instance.GC == original



@given(instance=Clasificacion_strategy)
def test_clasificacion_Posicion_setter(instance):
    original = instance.Posicion
    instance.Posicion = original
    assert instance.Posicion == original



@given(instance=Clasificacion_strategy)
def test_clasificacion_Cod_Equipo_setter(instance):
    original = instance.Cod_Equipo
    instance.Cod_Equipo = original
    assert instance.Cod_Equipo == original



@given(instance=Clasificacion_strategy)
def test_clasificacion_JG_setter(instance):
    original = instance.JG
    instance.JG = original
    assert instance.JG == original



@given(instance=Clasificacion_strategy)
def test_clasificacion_GF_setter(instance):
    original = instance.GF
    instance.GF = original
    assert instance.GF == original



@given(instance=Clasificacion_strategy)
def test_clasificacion_JP_setter(instance):
    original = instance.JP
    instance.JP = original
    assert instance.JP == original

@given(instance=Liga_strategy)
@settings(max_examples=50)
def test_liga_instantiation(instance):
    assert isinstance(instance, Liga)



@given(instance=Liga_strategy)
def test_liga_Cod_Clasificacion_setter(instance):
    original = instance.Cod_Clasificacion
    instance.Cod_Clasificacion = original
    assert instance.Cod_Clasificacion == original



@given(instance=Liga_strategy)
def test_liga_Cod_liga_setter(instance):
    original = instance.Cod_liga
    instance.Cod_liga = original
    assert instance.Cod_liga == original



@given(instance=Liga_strategy)
def test_liga_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=Liga_strategy)
def test_liga_Num_equipos_setter(instance):
    original = instance.Num_equipos
    instance.Num_equipos = original
    assert instance.Num_equipos == original



@given(instance=Liga_strategy)
def test_liga_Inferior_setter(instance):
    original = instance.Inferior
    instance.Inferior = original
    assert instance.Inferior == original



@given(instance=Liga_strategy)
def test_liga_Superior_setter(instance):
    original = instance.Superior
    instance.Superior = original
    assert instance.Superior == original

@given(instance=Lesion_strategy)
@settings(max_examples=50)
def test_lesion_instantiation(instance):
    assert isinstance(instance, Lesion)



@given(instance=Lesion_strategy)
def test_lesion_Condicion_setter(instance):
    original = instance.Condicion
    instance.Condicion = original
    assert instance.Condicion == original



@given(instance=Lesion_strategy)
def test_lesion_Cod_jugador_setter(instance):
    original = instance.Cod_jugador
    instance.Cod_jugador = original
    assert instance.Cod_jugador == original



@given(instance=Lesion_strategy)
def test_lesion_FechaLesion_setter(instance):
    original = instance.FechaLesion
    instance.FechaLesion = original
    assert instance.FechaLesion == original



@given(instance=Lesion_strategy)
def test_lesion_TiempoLesion_setter(instance):
    original = instance.TiempoLesion
    instance.TiempoLesion = original
    assert instance.TiempoLesion == original

@given(instance=TipoDeEvento_strategy)
@settings(max_examples=50)
def test_tipodeevento_instantiation(instance):
    assert isinstance(instance, TipoDeEvento)



@given(instance=TipoDeEvento_strategy)
def test_tipodeevento_Evento_setter(instance):
    original = instance.Evento
    instance.Evento = original
    assert instance.Evento == original



@given(instance=TipoDeEvento_strategy)
def test_tipodeevento_Cod_TipodeEvento_setter(instance):
    original = instance.Cod_TipodeEvento
    instance.Cod_TipodeEvento = original
    assert instance.Cod_TipodeEvento == original

@given(instance=Evento_strategy)
@settings(max_examples=50)
def test_evento_instantiation(instance):
    assert isinstance(instance, Evento)



@given(instance=Evento_strategy)
def test_evento_Cod_TipodeEvento_setter(instance):
    original = instance.Cod_TipodeEvento
    instance.Cod_TipodeEvento = original
    assert instance.Cod_TipodeEvento == original



@given(instance=Evento_strategy)
def test_evento_Cod_partido_setter(instance):
    original = instance.Cod_partido
    instance.Cod_partido = original
    assert instance.Cod_partido == original



@given(instance=Evento_strategy)
def test_evento_Cod_jugador_setter(instance):
    original = instance.Cod_jugador
    instance.Cod_jugador = original
    assert instance.Cod_jugador == original

@given(instance=Partido_strategy)
@settings(max_examples=50)
def test_partido_instantiation(instance):
    assert isinstance(instance, Partido)



@given(instance=Partido_strategy)
def test_partido_GolLocal_setter(instance):
    original = instance.GolLocal
    instance.GolLocal = original
    assert instance.GolLocal == original



@given(instance=Partido_strategy)
def test_partido_GolVisita_setter(instance):
    original = instance.GolVisita
    instance.GolVisita = original
    assert instance.GolVisita == original



@given(instance=Partido_strategy)
def test_partido_Cod_partido_setter(instance):
    original = instance.Cod_partido
    instance.Cod_partido = original
    assert instance.Cod_partido == original



@given(instance=Partido_strategy)
def test_partido_Hora_setter(instance):
    original = instance.Hora
    instance.Hora = original
    assert instance.Hora == original



@given(instance=Partido_strategy)
def test_partido_Ganador_setter(instance):
    original = instance.Ganador
    instance.Ganador = original
    assert instance.Ganador == original



@given(instance=Partido_strategy)
def test_partido_Local_setter(instance):
    original = instance.Local
    instance.Local = original
    assert instance.Local == original



@given(instance=Partido_strategy)
def test_partido_Visita_setter(instance):
    original = instance.Visita
    instance.Visita = original
    assert instance.Visita == original



@given(instance=Partido_strategy)
def test_partido_Fecha_setter(instance):
    original = instance.Fecha
    instance.Fecha = original
    assert instance.Fecha == original



@given(instance=Partido_strategy)
def test_partido_Cod_liga_setter(instance):
    original = instance.Cod_liga
    instance.Cod_liga = original
    assert instance.Cod_liga == original

@given(instance=Arbitro_strategy)
@settings(max_examples=50)
def test_arbitro_instantiation(instance):
    assert isinstance(instance, Arbitro)



@given(instance=Arbitro_strategy)
def test_arbitro_Cod_Arbitro_setter(instance):
    original = instance.Cod_Arbitro
    instance.Cod_Arbitro = original
    assert instance.Cod_Arbitro == original



@given(instance=Arbitro_strategy)
def test_arbitro_Partidos_setter(instance):
    original = instance.Partidos
    instance.Partidos = original
    assert instance.Partidos == original



@given(instance=Arbitro_strategy)
def test_arbitro_Cod_persona_setter(instance):
    original = instance.Cod_persona
    instance.Cod_persona = original
    assert instance.Cod_persona == original

@given(instance=Entrenador_strategy)
@settings(max_examples=50)
def test_entrenador_instantiation(instance):
    assert isinstance(instance, Entrenador)



@given(instance=Entrenador_strategy)
def test_entrenador_Titulos_setter(instance):
    original = instance.Titulos
    instance.Titulos = original
    assert instance.Titulos == original



@given(instance=Entrenador_strategy)
def test_entrenador_Cod_Entrenador_setter(instance):
    original = instance.Cod_Entrenador
    instance.Cod_Entrenador = original
    assert instance.Cod_Entrenador == original



@given(instance=Entrenador_strategy)
def test_entrenador_Cod_persona_setter(instance):
    original = instance.Cod_persona
    instance.Cod_persona = original
    assert instance.Cod_persona == original

@given(instance=Jugador_strategy)
@settings(max_examples=50)
def test_jugador_instantiation(instance):
    assert isinstance(instance, Jugador)



@given(instance=Jugador_strategy)
def test_jugador_Titulos_setter(instance):
    original = instance.Titulos
    instance.Titulos = original
    assert instance.Titulos == original



@given(instance=Jugador_strategy)
def test_jugador_Altura_setter(instance):
    original = instance.Altura
    instance.Altura = original
    assert instance.Altura == original



@given(instance=Jugador_strategy)
def test_jugador_Posicion_setter(instance):
    original = instance.Posicion
    instance.Posicion = original
    assert instance.Posicion == original



@given(instance=Jugador_strategy)
def test_jugador_Cod_equipo_setter(instance):
    original = instance.Cod_equipo
    instance.Cod_equipo = original
    assert instance.Cod_equipo == original



@given(instance=Jugador_strategy)
def test_jugador_Cod_jugador_setter(instance):
    original = instance.Cod_jugador
    instance.Cod_jugador = original
    assert instance.Cod_jugador == original



@given(instance=Jugador_strategy)
def test_jugador_Cod_persona_setter(instance):
    original = instance.Cod_persona
    instance.Cod_persona = original
    assert instance.Cod_persona == original



@given(instance=Jugador_strategy)
def test_jugador_Peso_setter(instance):
    original = instance.Peso
    instance.Peso = original
    assert instance.Peso == original



@given(instance=Jugador_strategy)
def test_jugador_Dorsal_setter(instance):
    original = instance.Dorsal
    instance.Dorsal = original
    assert instance.Dorsal == original

@given(instance=Equipo_strategy)
@settings(max_examples=50)
def test_equipo_instantiation(instance):
    assert isinstance(instance, Equipo)



@given(instance=Equipo_strategy)
def test_equipo_Cod_equipo_setter(instance):
    original = instance.Cod_equipo
    instance.Cod_equipo = original
    assert instance.Cod_equipo == original



@given(instance=Equipo_strategy)
def test_equipo_Titulos_setter(instance):
    original = instance.Titulos
    instance.Titulos = original
    assert instance.Titulos == original



@given(instance=Equipo_strategy)
def test_equipo_F_fundacion_setter(instance):
    original = instance.F_fundacion
    instance.F_fundacion = original
    assert instance.F_fundacion == original



@given(instance=Equipo_strategy)
def test_equipo_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=Equipo_strategy)
def test_equipo_Cod_Entrenador_setter(instance):
    original = instance.Cod_Entrenador
    instance.Cod_Entrenador = original
    assert instance.Cod_Entrenador == original



@given(instance=Equipo_strategy)
def test_equipo_Ciudad_setter(instance):
    original = instance.Ciudad
    instance.Ciudad = original
    assert instance.Ciudad == original
