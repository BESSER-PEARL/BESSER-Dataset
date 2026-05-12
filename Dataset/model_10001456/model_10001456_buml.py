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
SistemaApuesta = Class(name="SistemaApuesta")
Tarjeta = Class(name="Tarjeta")
Usuario = Class(name="Usuario")
Apuesta = Class(name="Apuesta")
Partido = Class(name="Partido")
ApuestaMarcadorEspecifico = Class(name="ApuestaMarcadorEspecifico")
ApuestaEquipoGanador = Class(name="ApuestaEquipoGanador")
Marcador = Class(name="Marcador")
Equipo = Class(name="Equipo")
Historico = Class(name="Historico")

# SistemaApuesta class attributes and methods

# Tarjeta class attributes and methods
Tarjeta_numeroTarje: Property = Property(name="numeroTarje", type=IntegerType)
Tarjeta_codigoSeguridad: Property = Property(name="codigoSeguridad", type=IntegerType)
Tarjeta.attributes={Tarjeta_codigoSeguridad, Tarjeta_numeroTarje}

# Usuario class attributes and methods
Usuario_userName: Property = Property(name="userName", type=StringType)
Usuario_passWord: Property = Property(name="passWord", type=StringType)
Usuario.attributes={Usuario_passWord, Usuario_userName}

# Apuesta class attributes and methods
Apuesta_valorApuesta: Property = Property(name="valorApuesta", type=StringType)
Apuesta_porcentajeGanancia: Property = Property(name="porcentajeGanancia", type=StringType)
Apuesta_id: Property = Property(name="id", type=StringType)
Apuesta.attributes={Apuesta_valorApuesta, Apuesta_porcentajeGanancia, Apuesta_id}

# Partido class attributes and methods
Partido_numeroApuestas: Property = Property(name="numeroApuestas", type=StringType)
Partido_idPartido: Property = Property(name="idPartido", type=StringType)
Partido.attributes={Partido_idPartido, Partido_numeroApuestas}

# ApuestaMarcadorEspecifico class attributes and methods
ApuestaMarcadorEspecifico_nombreEquipoGanador: Property = Property(name="nombreEquipoGanador", type=StringType)
ApuestaMarcadorEspecifico_porcentajeAciertoMarcador: Property = Property(name="porcentajeAciertoMarcador", type=StringType)
ApuestaMarcadorEspecifico_numeroGolesEquipo1: Property = Property(name="numeroGolesEquipo1", type=IntegerType)
ApuestaMarcadorEspecifico_numeroGolesEquipo2: Property = Property(name="numeroGolesEquipo2", type=IntegerType)
ApuestaMarcadorEspecifico.attributes={ApuestaMarcadorEspecifico_nombreEquipoGanador, ApuestaMarcadorEspecifico_porcentajeAciertoMarcador, ApuestaMarcadorEspecifico_numeroGolesEquipo1, ApuestaMarcadorEspecifico_numeroGolesEquipo2}

# ApuestaEquipoGanador class attributes and methods
ApuestaEquipoGanador_nombreEquipoGnador: Property = Property(name="nombreEquipoGnador", type=StringType)
ApuestaEquipoGanador.attributes={ApuestaEquipoGanador_nombreEquipoGnador}

# Marcador class attributes and methods
Marcador_nombreEquipoGanador: Property = Property(name="nombreEquipoGanador", type=StringType)
Marcador_numeroGolesEquipo1: Property = Property(name="numeroGolesEquipo1", type=IntegerType)
Marcador_numeroGolesEquipo2: Property = Property(name="numeroGolesEquipo2", type=IntegerType)
Marcador.attributes={Marcador_numeroGolesEquipo1, Marcador_nombreEquipoGanador, Marcador_numeroGolesEquipo2}

# Equipo class attributes and methods
Equipo_nombre: Property = Property(name="nombre", type=StringType)
Equipo_jugadores: Property = Property(name="jugadores", type=StringType)
Equipo_porcentajeFavoritismo: Property = Property(name="porcentajeFavoritismo", type=StringType)
Equipo.attributes={Equipo_nombre, Equipo_porcentajeFavoritismo, Equipo_jugadores}

# Historico class attributes and methods
Historico_numeroPartidosPerdidos: Property = Property(name="numeroPartidosPerdidos", type=IntegerType)
Historico_numeroPartidosGanados: Property = Property(name="numeroPartidosGanados", type=IntegerType)
Historico_numeroPartidosJugados: Property = Property(name="numeroPartidosJugados", type=IntegerType)
Historico_porcentajeApuestasEnFavor: Property = Property(name="porcentajeApuestasEnFavor", type=StringType)
Historico.attributes={Historico_numeroPartidosGanados, Historico_numeroPartidosJugados, Historico_numeroPartidosPerdidos, Historico_porcentajeApuestasEnFavor}

# Relationships
SistemaApuesta_Usuario: BinaryAssociation = BinaryAssociation(
    name="SistemaApuesta_Usuario",
    ends={
        Property(name="usuario0", type=Usuario, multiplicity=Multiplicity(0, 9999)),
        Property(name="sistemaApuesta1", type=SistemaApuesta, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Tarjeta: BinaryAssociation = BinaryAssociation(
    name="Usuario_Tarjeta",
    ends={
        Property(name="tarjeta2", type=Tarjeta, multiplicity=Multiplicity(1, 9999)),
        Property(name="usuario3", type=Usuario, multiplicity=Multiplicity(1, 1))
    }
)
Usuario_Apuesta: BinaryAssociation = BinaryAssociation(
    name="Usuario_Apuesta",
    ends={
        Property(name="apuesta4", type=Apuesta, multiplicity=Multiplicity(0, 9999)),
        Property(name="usuario5", type=Usuario, multiplicity=Multiplicity(1, 1))
    }
)
Apuesta_Partido: BinaryAssociation = BinaryAssociation(
    name="Apuesta_Partido",
    ends={
        Property(name="partido6", type=Partido, multiplicity=Multiplicity(1, 1)),
        Property(name="apuesta7", type=Apuesta, multiplicity=Multiplicity(0, 9999))
    }
)
Partido_Equipo: BinaryAssociation = BinaryAssociation(
    name="Partido_Equipo",
    ends={
        Property(name="eq_18", type=Equipo, multiplicity=Multiplicity(0, 1)),
        Property(name="partido9", type=Partido, multiplicity=Multiplicity(0, 1))
    }
)
Partido_Equipo2: BinaryAssociation = BinaryAssociation(
    name="Partido_Equipo2",
    ends={
        Property(name="eq_210", type=Equipo, multiplicity=Multiplicity(0, 1)),
        Property(name="partido11", type=Partido, multiplicity=Multiplicity(0, 1))
    }
)
Equipo_Historico: BinaryAssociation = BinaryAssociation(
    name="Equipo_Historico",
    ends={
        Property(name="historico12", type=Historico, multiplicity=Multiplicity(1, 1)),
        Property(name="equipo13", type=Equipo, multiplicity=Multiplicity(0, 1))
    }
)
Historico__Partido: BinaryAssociation = BinaryAssociation(
    name="Historico__Partido",
    ends={
        Property(name="partido14", type=Partido, multiplicity=Multiplicity(1, 9999)),
        Property(name="historico15", type=Historico, multiplicity=Multiplicity(0, 1))
    }
)
Partido_Marcador: BinaryAssociation = BinaryAssociation(
    name="Partido_Marcador",
    ends={
        Property(name="marcador16", type=Marcador, multiplicity=Multiplicity(1, 1)),
        Property(name="partido17", type=Partido, multiplicity=Multiplicity(1, 1))
    }
)
SistemaApuesta_Apuesta: BinaryAssociation = BinaryAssociation(
    name="SistemaApuesta_Apuesta",
    ends={
        Property(name="apuesta18", type=Apuesta, multiplicity=Multiplicity(0, 9999)),
        Property(name="sistemaApuesta19", type=SistemaApuesta, multiplicity=Multiplicity(0, 1))
    }
)
SistemaApuesta_Partido: BinaryAssociation = BinaryAssociation(
    name="SistemaApuesta_Partido",
    ends={
        Property(name="partido20", type=Partido, multiplicity=Multiplicity(1, 9999)),
        Property(name="sistemaApuesta21", type=SistemaApuesta, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7jW3QAnSEeihOuC11hdjgA",
    types={SistemaApuesta, Tarjeta, Usuario, Apuesta, Partido, ApuestaMarcadorEspecifico, ApuestaEquipoGanador, Marcador, Equipo, Historico},
    associations={SistemaApuesta_Usuario, Usuario_Tarjeta, Usuario_Apuesta, Apuesta_Partido, Partido_Equipo, Partido_Equipo2, Equipo_Historico, Historico__Partido, Partido_Marcador, SistemaApuesta_Apuesta, SistemaApuesta_Partido},
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