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
Torneo = Class(name="Torneo")
Premio = Class(name="Premio")
Fecha = Class(name="Fecha")
Partido = Class(name="Partido")
Marcador = Class(name="Marcador")
Equipo = Class(name="Equipo")
Jugador = Class(name="Jugador")

# Torneo class attributes and methods
Torneo_Nombre: Property = Property(name="Nombre", type=StringType)
Torneo_Pais: Property = Property(name="Pais", type=StringType)
Torneo.attributes={Torneo_Nombre, Torneo_Pais}

# Premio class attributes and methods
Premio_Puesto: Property = Property(name="Puesto", type=IntegerType)
Premio_Dinero: Property = Property(name="Dinero", type=IntegerType)
Premio_Puntos: Property = Property(name="Puntos", type=IntegerType)
Premio.attributes={Premio_Dinero, Premio_Puntos, Premio_Puesto}

# Fecha class attributes and methods
Fecha_anio: Property = Property(name="anio", type=IntegerType)
Fecha_mes: Property = Property(name="mes", type=IntegerType)
Fecha_dia: Property = Property(name="dia", type=IntegerType)
Fecha.attributes={Fecha_anio, Fecha_dia, Fecha_mes}

# Partido class attributes and methods
Partido_id: Property = Property(name="id", type=IntegerType)
Partido_ronda: Property = Property(name="ronda", type=StringType)
Partido.attributes={Partido_id, Partido_ronda}

# Marcador class attributes and methods
Marcador_equipo1: Property = Property(name="equipo1", type=IntegerType)
Marcador_equipo2: Property = Property(name="equipo2", type=IntegerType)
Marcador_tiempoSet: Property = Property(name="tiempoSet", type=IntegerType)
Marcador.attributes={Marcador_equipo2, Marcador_tiempoSet, Marcador_equipo1}

# Equipo class attributes and methods
Equipo_nombre: Property = Property(name="nombre", type=StringType)
Equipo.attributes={Equipo_nombre}

# Jugador class attributes and methods
Jugador_nombre: Property = Property(name="nombre", type=StringType)
Jugador_apellidos: Property = Property(name="apellidos", type=StringType)
Jugador_telefono: Property = Property(name="telefono", type=IntegerType)
Jugador_nif: Property = Property(name="nif", type=StringType)
Jugador.attributes={Jugador_nif, Jugador_nombre, Jugador_telefono, Jugador_apellidos}

# Relationships
Torneo_Premio: BinaryAssociation = BinaryAssociation(
    name="Torneo_Premio",
    ends={
        Property(name="premio0", type=Premio, multiplicity=Multiplicity(0, 9999)),
        Property(name="torneo1", type=Torneo, multiplicity=Multiplicity(0, 1))
    }
)
Partido_Marcador: BinaryAssociation = BinaryAssociation(
    name="Partido_Marcador",
    ends={
        Property(name="marcador2", type=Marcador, multiplicity=Multiplicity(1, 5)),
        Property(name="partido3", type=Partido, multiplicity=Multiplicity(0, 1))
    }
)
Partido_Equipo: BinaryAssociation = BinaryAssociation(
    name="Partido_Equipo",
    ends={
        Property(name="equipo4", type=Equipo, multiplicity=Multiplicity(2, 2)),
        Property(name="partido5", type=Partido, multiplicity=Multiplicity(0, 1))
    }
)
Equipo_Jugador: BinaryAssociation = BinaryAssociation(
    name="Equipo_Jugador",
    ends={
        Property(name="jugador6", type=Jugador, multiplicity=Multiplicity(1, 2)),
        Property(name="equipo7", type=Equipo, multiplicity=Multiplicity(0, 1))
    }
)
Jugador_Fecha_Nacimiento: BinaryAssociation = BinaryAssociation(
    name="Jugador_Fecha_Nacimiento",
    ends={
        Property(name="fechaNacimiento8", type=Fecha, multiplicity=Multiplicity(1, 1)),
        Property(name="jugador9", type=Jugador, multiplicity=Multiplicity(1, 1))
    }
)
Torneo_Fecha_Inicio: BinaryAssociation = BinaryAssociation(
    name="Torneo_Fecha_Inicio",
    ends={
        Property(name="fechaInicio10", type=Fecha, multiplicity=Multiplicity(1, 1)),
        Property(name="torneo11", type=Torneo, multiplicity=Multiplicity(1, 1))
    }
)
Torneo_Fecha_Fin: BinaryAssociation = BinaryAssociation(
    name="Torneo_Fecha_Fin",
    ends={
        Property(name="fechaFin12", type=Fecha, multiplicity=Multiplicity(0, 1)),
        Property(name="torneo13", type=Torneo, multiplicity=Multiplicity(1, 1))
    }
)
Torneo_Partido: BinaryAssociation = BinaryAssociation(
    name="Torneo_Partido",
    ends={
        Property(name="partido14", type=Partido, multiplicity=Multiplicity(1, 9999)),
        Property(name="torneo15", type=Torneo, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_XEp5kIJQEemGPZyN8msRcg",
    types={Torneo, Premio, Fecha, Partido, Marcador, Equipo, Jugador},
    associations={Torneo_Premio, Partido_Marcador, Partido_Equipo, Equipo_Jugador, Jugador_Fecha_Nacimiento, Torneo_Fecha_Inicio, Torneo_Fecha_Fin, Torneo_Partido},
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