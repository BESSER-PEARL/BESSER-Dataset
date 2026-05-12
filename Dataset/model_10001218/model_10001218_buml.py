####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
Equipo = Class(name="Equipo")
Jugador = Class(name="Jugador")
Entrenador = Class(name="Entrenador")
Arbitro = Class(name="Arbitro")
Partido = Class(name="Partido")
Evento = Class(name="Evento")
TipoDeEvento = Class(name="TipoDeEvento")
Lesion = Class(name="Lesion")
Liga = Class(name="Liga")
Clasificacion = Class(name="Clasificacion")
Persona = Class(name="Persona")
Estadio = Class(name="Estadio")

# Equipo class attributes and methods
Equipo_Cod_equipo: Property = Property(name="Cod_equipo", type=StringType)
Equipo_Nombre: Property = Property(name="Nombre", type=StringType)
Equipo_F_fundacion: Property = Property(name="F_fundacion", type=StringType)
Equipo_Ciudad: Property = Property(name="Ciudad", type=StringType)
Equipo_Titulos: Property = Property(name="Titulos", type=StringType)
Equipo_Cod_Entrenador: Property = Property(name="Cod_Entrenador", type=StringType)
Equipo.attributes={Equipo_Ciudad, Equipo_Cod_equipo, Equipo_F_fundacion, Equipo_Cod_Entrenador, Equipo_Nombre, Equipo_Titulos}

# Jugador class attributes and methods
Jugador_Cod_jugador: Property = Property(name="Cod_jugador", type=StringType)
Jugador_Dorsal: Property = Property(name="Dorsal", type=StringType)
Jugador_Posicion: Property = Property(name="Posicion", type=StringType)
Jugador_Altura: Property = Property(name="Altura", type=StringType)
Jugador_Peso: Property = Property(name="Peso", type=StringType)
Jugador_Titulos: Property = Property(name="Titulos", type=StringType)
Jugador_Cod_equipo: Property = Property(name="Cod_equipo", type=StringType)
Jugador_Cod_persona: Property = Property(name="Cod_persona", type=StringType)
Jugador.attributes={Jugador_Peso, Jugador_Cod_persona, Jugador_Titulos, Jugador_Dorsal, Jugador_Cod_jugador, Jugador_Posicion, Jugador_Cod_equipo, Jugador_Altura}

# Entrenador class attributes and methods
Entrenador_Cod_Entrenador: Property = Property(name="Cod_Entrenador", type=StringType)
Entrenador_Titulos: Property = Property(name="Titulos", type=StringType)
Entrenador_Cod_persona: Property = Property(name="Cod_persona", type=StringType)
Entrenador.attributes={Entrenador_Cod_persona, Entrenador_Cod_Entrenador, Entrenador_Titulos}

# Arbitro class attributes and methods
Arbitro_Partidos: Property = Property(name="Partidos", type=StringType)
Arbitro_Cod_Arbitro: Property = Property(name="Cod_Arbitro", type=StringType)
Arbitro_Cod_persona: Property = Property(name="Cod_persona", type=StringType)
Arbitro.attributes={Arbitro_Cod_persona, Arbitro_Partidos, Arbitro_Cod_Arbitro}

# Partido class attributes and methods
Partido_Cod_partido: Property = Property(name="Cod_partido", type=StringType)
Partido_Fecha: Property = Property(name="Fecha", type=StringType)
Partido_Hora: Property = Property(name="Hora", type=StringType)
Partido_Local: Property = Property(name="Local", type=StringType)
Partido_Visita: Property = Property(name="Visita", type=StringType)
Partido_GolLocal: Property = Property(name="GolLocal", type=StringType)
Partido_GolVisita: Property = Property(name="GolVisita", type=StringType)
Partido_Ganador: Property = Property(name="Ganador", type=StringType)
Partido_Cod_liga: Property = Property(name="Cod_liga", type=StringType)
Partido.attributes={Partido_GolLocal, Partido_Ganador, Partido_Fecha, Partido_Local, Partido_Cod_liga, Partido_Hora, Partido_Visita, Partido_GolVisita, Partido_Cod_partido}

# Evento class attributes and methods
Evento_Cod_partido: Property = Property(name="Cod_partido", type=StringType)
Evento_Cod_jugador: Property = Property(name="Cod_jugador", type=StringType)
Evento_Cod_TipodeEvento: Property = Property(name="Cod_TipodeEvento", type=StringType)
Evento.attributes={Evento_Cod_jugador, Evento_Cod_TipodeEvento, Evento_Cod_partido}

# TipoDeEvento class attributes and methods
TipoDeEvento_Cod_TipodeEvento: Property = Property(name="Cod_TipodeEvento", type=StringType)
TipoDeEvento_Evento: Property = Property(name="Evento", type=StringType)
TipoDeEvento.attributes={TipoDeEvento_Cod_TipodeEvento, TipoDeEvento_Evento}

# Lesion class attributes and methods
Lesion_Cod_jugador: Property = Property(name="Cod_jugador", type=StringType)
Lesion_FechaLesion: Property = Property(name="FechaLesion", type=StringType)
Lesion_TiempoLesion: Property = Property(name="TiempoLesion", type=StringType)
Lesion_Condicion: Property = Property(name="Condicion", type=StringType)
Lesion.attributes={Lesion_TiempoLesion, Lesion_FechaLesion, Lesion_Cod_jugador, Lesion_Condicion}

# Liga class attributes and methods
Liga_Cod_liga: Property = Property(name="Cod_liga", type=StringType)
Liga_Nombre: Property = Property(name="Nombre", type=StringType)
Liga_Num_equipos: Property = Property(name="Num_equipos", type=StringType)
Liga_Superior: Property = Property(name="Superior", type=StringType)
Liga_Inferior: Property = Property(name="Inferior", type=StringType)
Liga_Cod_Clasificacion: Property = Property(name="Cod_Clasificacion", type=StringType)
Liga.attributes={Liga_Cod_Clasificacion, Liga_Num_equipos, Liga_Inferior, Liga_Nombre, Liga_Cod_liga, Liga_Superior}

# Clasificacion class attributes and methods
Clasificacion_Cod_Equipo: Property = Property(name="Cod_Equipo", type=StringType)
Clasificacion_Posicion: Property = Property(name="Posicion", type=StringType)
Clasificacion_JJ: Property = Property(name="JJ", type=StringType)
Clasificacion_JP: Property = Property(name="JP", type=StringType)
Clasificacion_JE: Property = Property(name="JE", type=StringType)
Clasificacion_JG: Property = Property(name="JG", type=StringType)
Clasificacion_GF: Property = Property(name="GF", type=StringType)
Clasificacion_GC: Property = Property(name="GC", type=StringType)
Clasificacion_DG: Property = Property(name="DG", type=StringType)
Clasificacion_Puntos: Property = Property(name="Puntos", type=StringType)
Clasificacion.attributes={Clasificacion_JG, Clasificacion_Puntos, Clasificacion_DG, Clasificacion_GF, Clasificacion_GC, Clasificacion_Cod_Equipo, Clasificacion_JE, Clasificacion_JP, Clasificacion_Posicion, Clasificacion_JJ}

# Persona class attributes and methods
Persona_Cod_persona: Property = Property(name="Cod_persona", type=StringType)
Persona_Nombre: Property = Property(name="Nombre", type=StringType)
Persona_Apellido: Property = Property(name="Apellido", type=StringType)
Persona_NombreCorto: Property = Property(name="NombreCorto", type=StringType)
Persona_FechaNacimiento: Property = Property(name="FechaNacimiento", type=StringType)
Persona_Nacionalidad: Property = Property(name="Nacionalidad", type=StringType)
Persona.attributes={Persona_Nombre, Persona_Apellido, Persona_Nacionalidad, Persona_Cod_persona, Persona_NombreCorto, Persona_FechaNacimiento}

# Estadio class attributes and methods
Estadio_Nombre: Property = Property(name="Nombre", type=StringType)
Estadio_Ubicacion: Property = Property(name="Ubicacion", type=StringType)
Estadio_Capacidad: Property = Property(name="Capacidad", type=StringType)
Estadio_Terreno: Property = Property(name="Terreno", type=StringType)
Estadio_Ubicacion1: Property = Property(name="Ubicacion1", type=StringType)
Estadio_Cod_equipo: Property = Property(name="Cod_equipo", type=StringType)
Estadio_Cod_Estadio: Property = Property(name="Cod_Estadio", type=StringType)
Estadio.attributes={Estadio_Terreno, Estadio_Nombre, Estadio_Cod_Estadio, Estadio_Cod_equipo, Estadio_Ubicacion, Estadio_Capacidad, Estadio_Ubicacion1}

# Relationships
Entrenador_Equipo: BinaryAssociation = BinaryAssociation(
    name="Entrenador_Equipo",
    ends={
        Property(name="equipo0", type=Equipo, multiplicity=Multiplicity(1, 1)),
        Property(name="entrenador1", type=Entrenador, multiplicity=Multiplicity(1, 1))
    }
)
Jugador_Equipo: BinaryAssociation = BinaryAssociation(
    name="Jugador_Equipo",
    ends={
        Property(name="equipo2", type=Equipo, multiplicity=Multiplicity(1, 1)),
        Property(name="jugador3", type=Jugador, multiplicity=Multiplicity(0, 9999))
    }
)
Partido_Estadio: BinaryAssociation = BinaryAssociation(
    name="Partido_Estadio",
    ends={
        Property(name="estadio4", type=Estadio, multiplicity=Multiplicity(1, 1)),
        Property(name="partido5", type=Partido, multiplicity=Multiplicity(0, 9999))
    }
)
Partido_Equipo: BinaryAssociation = BinaryAssociation(
    name="Partido_Equipo",
    ends={
        Property(name="equipo6", type=Equipo, multiplicity=Multiplicity(1, 1)),
        Property(name="partido7", type=Partido, multiplicity=Multiplicity(0, 9999))
    }
)
Equipo_Partido: BinaryAssociation = BinaryAssociation(
    name="Equipo_Partido",
    ends={
        Property(name="partido8", type=Partido, multiplicity=Multiplicity(0, 9999)),
        Property(name="equipo9", type=Equipo, multiplicity=Multiplicity(1, 1))
    }
)
Jugador_Evento: BinaryAssociation = BinaryAssociation(
    name="Jugador_Evento",
    ends={
        Property(name="evento10", type=Evento, multiplicity=Multiplicity(0, 9999)),
        Property(name="jugador11", type=Jugador, multiplicity=Multiplicity(1, 1))
    }
)
Evento_Partido: BinaryAssociation = BinaryAssociation(
    name="Evento_Partido",
    ends={
        Property(name="partido12", type=Partido, multiplicity=Multiplicity(1, 1)),
        Property(name="evento13", type=Evento, multiplicity=Multiplicity(0, 9999))
    }
)
TipoDeEvento_Evento: BinaryAssociation = BinaryAssociation(
    name="TipoDeEvento_Evento",
    ends={
        Property(name="evento14", type=Evento, multiplicity=Multiplicity(0, 9999)),
        Property(name="tipoDeEvento15", type=TipoDeEvento, multiplicity=Multiplicity(1, 1))
    }
)
Persona_Arbitro: BinaryAssociation = BinaryAssociation(
    name="Persona_Arbitro",
    ends={
        Property(name="arbitro16", type=Arbitro, multiplicity=Multiplicity(0, 9999)),
        Property(name="persona17", type=Persona, multiplicity=Multiplicity(1, 1))
    }
)
Persona_Jugador: BinaryAssociation = BinaryAssociation(
    name="Persona_Jugador",
    ends={
        Property(name="jugador18", type=Jugador, multiplicity=Multiplicity(0, 9999)),
        Property(name="persona19", type=Persona, multiplicity=Multiplicity(1, 1))
    }
)
Persona_Entrenador: BinaryAssociation = BinaryAssociation(
    name="Persona_Entrenador",
    ends={
        Property(name="entrenador20", type=Entrenador, multiplicity=Multiplicity(0, 9999)),
        Property(name="persona21", type=Persona, multiplicity=Multiplicity(1, 1))
    }
)
Jugador_Lesion: BinaryAssociation = BinaryAssociation(
    name="Jugador_Lesion",
    ends={
        Property(name="lesion22", type=Lesion, multiplicity=Multiplicity(0, 9999)),
        Property(name="jugador23", type=Jugador, multiplicity=Multiplicity(1, 1))
    }
)
Liga_Partido: BinaryAssociation = BinaryAssociation(
    name="Liga_Partido",
    ends={
        Property(name="partido24", type=Partido, multiplicity=Multiplicity(0, 9999)),
        Property(name="liga25", type=Liga, multiplicity=Multiplicity(1, 1))
    }
)
Liga_Clasificacion: BinaryAssociation = BinaryAssociation(
    name="Liga_Clasificacion",
    ends={
        Property(name="clasificacion26", type=Clasificacion, multiplicity=Multiplicity(1, 1)),
        Property(name="liga27", type=Liga, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_944ac5a8_50d4_4c7a_91d1_5da14dbb8170",
    types={Equipo, Jugador, Entrenador, Arbitro, Partido, Evento, TipoDeEvento, Lesion, Liga, Clasificacion, Persona, Estadio},
    associations={Entrenador_Equipo, Jugador_Equipo, Partido_Estadio, Partido_Equipo, Equipo_Partido, Jugador_Evento, Evento_Partido, TipoDeEvento_Evento, Persona_Arbitro, Persona_Jugador, Persona_Entrenador, Jugador_Lesion, Liga_Partido, Liga_Clasificacion},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)