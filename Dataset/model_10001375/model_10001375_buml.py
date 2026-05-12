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
Liga = Class(name="Liga")
Equipo = Class(name="Equipo")
Jugadores = Class(name="Jugadores")
Partido = Class(name="Partido")
Entrenador = Class(name="Entrenador")
Personas = Class(name="Personas")

# Liga class attributes and methods
Liga_nombre: Property = Property(name="nombre", type=StringType)
Liga_datos_comienzo: Property = Property(name="datos_comienzo", type=StringType)
Liga_datos_finalizaci_n: Property = Property(name="datos_finalizaci_n", type=StringType)
Liga.attributes={Liga_nombre, Liga_datos_finalizaci_n, Liga_datos_comienzo}

# Equipo class attributes and methods
Equipo_nombre: Property = Property(name="nombre", type=StringType)
Equipo_registro: Property = Property(name="registro", type=StringType)
Equipo.attributes={Equipo_registro, Equipo_nombre}

# Jugadores class attributes and methods
Jugadores_nombre: Property = Property(name="nombre", type=StringType)
Jugadores_posicion: Property = Property(name="posicion", type=IntegerType)
Jugadores.attributes={Jugadores_posicion, Jugadores_nombre}

# Partido class attributes and methods
Partido_resultado: Property = Property(name="resultado", type=IntegerType)
Partido_localizaci_n: Property = Property(name="localizaci_n", type=StringType)
Partido.attributes={Partido_localizaci_n, Partido_resultado}

# Entrenador class attributes and methods
Entrenador_nivel_de_acreditaci_n: Property = Property(name="nivel_de_acreditaci_n", type=StringType)
Entrenador_a_os_de_experiencia: Property = Property(name="a_os_de_experiencia", type=IntegerType)
Entrenador.attributes={Entrenador_nivel_de_acreditaci_n, Entrenador_a_os_de_experiencia}

# Personas class attributes and methods
Personas_Nombre: Property = Property(name="Nombre", type=StringType)
Personas_Direccion: Property = Property(name="Direccion", type=StringType)
Personas.attributes={Personas_Direccion, Personas_Nombre}

# Relationships
Liga_Equipo: BinaryAssociation = BinaryAssociation(
    name="Liga_Equipo",
    ends={
        Property(name="equipo0", type=Equipo, multiplicity=Multiplicity(0, 1)),
        Property(name="liga1", type=Liga, multiplicity=Multiplicity(1, 1))
    }
)
Equipo_Jugadores: BinaryAssociation = BinaryAssociation(
    name="Equipo_Jugadores",
    ends={
        Property(name="jugadores2", type=Jugadores, multiplicity=Multiplicity(0, 1)),
        Property(name="equipo3", type=Equipo, multiplicity=Multiplicity(1, 1))
    }
)
Jugadores_Equipo: BinaryAssociation = BinaryAssociation(
    name="Jugadores_Equipo",
    ends={
        Property(name="equipo4", type=Equipo, multiplicity=Multiplicity(1, 1)),
        Property(name="jugadores5", type=Jugadores, multiplicity=Multiplicity(1, 1))
    }
)
Equipo_Partido: BinaryAssociation = BinaryAssociation(
    name="Equipo_Partido",
    ends={
        Property(name="partido6", type=Partido, multiplicity=Multiplicity(1, 9999)),
        Property(name="equipo7", type=Equipo, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_32s_wFNIEeqK2M3E1LfZ7Q",
    types={Liga, Equipo, Jugadores, Partido, Entrenador, Personas},
    associations={Liga_Equipo, Equipo_Jugadores, Jugadores_Equipo, Equipo_Partido},
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