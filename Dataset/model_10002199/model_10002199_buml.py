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
Usuario_Actor = Class(name="Usuario_Actor")
_Buscar_un_ejemplar_por_su_nombre___UseCase = Class(name="_Buscar_un_ejemplar_por_su_nombre___UseCase")
Calcular_el_n_mero_de_ejemplares_caninos_por_raza_UseCase = Class(name="Calcular_el_n_mero_de_ejemplares_caninos_por_raza_UseCase")
_Calcular_el_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase = Class(name="_Calcular_el_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase")
Avanzar_hacia_el_siguiente_ejemplar_UseCase = Class(name="Avanzar_hacia_el_siguiente_ejemplar_UseCase")
_Regresar_hacia_el_anterior_ejemplar_UseCase = Class(name="_Regresar_hacia_el_anterior_ejemplar_UseCase")
Desplazarse_hasta_el_primer_ejemplar_UseCase = Class(name="Desplazarse_hasta_el_primer_ejemplar_UseCase")
Desplazarse_hasta_el__ltimo_ejemplar_UseCase = Class(name="Desplazarse_hasta_el__ltimo_ejemplar_UseCase")
Empresa = Class(name="Empresa")
Caninos = Class(name="Caninos")

# Usuario_Actor class attributes and methods

# _Buscar_un_ejemplar_por_su_nombre___UseCase class attributes and methods

# Calcular_el_n_mero_de_ejemplares_caninos_por_raza_UseCase class attributes and methods

# _Calcular_el_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase class attributes and methods

# Avanzar_hacia_el_siguiente_ejemplar_UseCase class attributes and methods

# _Regresar_hacia_el_anterior_ejemplar_UseCase class attributes and methods

# Desplazarse_hasta_el_primer_ejemplar_UseCase class attributes and methods

# Desplazarse_hasta_el__ltimo_ejemplar_UseCase class attributes and methods

# Empresa class attributes and methods

# Caninos class attributes and methods
Caninos_nombre: Property = Property(name="nombre", type=StringType)
Caninos_raza: Property = Property(name="raza", type=StringType)
Caninos_edad: Property = Property(name="edad", type=StringType)
Caninos_altura: Property = Property(name="altura", type=StringType)
Caninos_peso: Property = Property(name="peso", type=StringType)
Caninos_observaciones: Property = Property(name="observaciones", type=StringType)
Caninos.attributes={Caninos_altura, Caninos_nombre, Caninos_edad, Caninos_raza, Caninos_observaciones, Caninos_peso}

# Relationships
Usuario__Buscar_un_ejemplar_por_su_nombre_: BinaryAssociation = BinaryAssociation(
    name="Usuario__Buscar_un_ejemplar_por_su_nombre_",
    ends={
        Property(name="_Buscar_un_ejemplar_por_su_nombre_0", type=_Buscar_un_ejemplar_por_su_nombre___UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario1", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Calcular_el_n_mero_de_ejemplares_caninos_por_raza: BinaryAssociation = BinaryAssociation(
    name="Usuario_Calcular_el_n_mero_de_ejemplares_caninos_por_raza",
    ends={
        Property(name="calcular_el_n_mero_de_ejemplares_caninos_por_raza2", type=Calcular_el_n_mero_de_ejemplares_caninos_por_raza_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario3", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Calcular_el_promedio_de_edad_de_todos_los_ejemplares_caninos_: BinaryAssociation = BinaryAssociation(
    name="Usuario__Calcular_el_promedio_de_edad_de_todos_los_ejemplares_caninos_",
    ends={
        Property(name="_Calcular_el_promedio_de_edad_de_todos_los_ejemplares_caninos_4", type=_Calcular_el_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario5", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Avanzar_hacia_el_siguiente_ejemplar: BinaryAssociation = BinaryAssociation(
    name="Usuario_Avanzar_hacia_el_siguiente_ejemplar",
    ends={
        Property(name="avanzar_hacia_el_siguiente_ejemplar6", type=Avanzar_hacia_el_siguiente_ejemplar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario7", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Regresar_hacia_el_anterior_ejemplar: BinaryAssociation = BinaryAssociation(
    name="Usuario__Regresar_hacia_el_anterior_ejemplar",
    ends={
        Property(name="_Regresar_hacia_el_anterior_ejemplar8", type=_Regresar_hacia_el_anterior_ejemplar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario9", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Desplazarse_hasta_el_primer_ejemplar: BinaryAssociation = BinaryAssociation(
    name="Usuario_Desplazarse_hasta_el_primer_ejemplar",
    ends={
        Property(name="desplazarse_hasta_el_primer_ejemplar10", type=Desplazarse_hasta_el_primer_ejemplar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario11", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Desplazarse_hasta_el__ltimo_ejemplar: BinaryAssociation = BinaryAssociation(
    name="Usuario_Desplazarse_hasta_el__ltimo_ejemplar",
    ends={
        Property(name="desplazarse_hasta_el__ltimo_ejemplar12", type=Desplazarse_hasta_el__ltimo_ejemplar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario13", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Class: BinaryAssociation = BinaryAssociation(
    name="Empresa_Class",
    ends={
        Property(name="canino_114", type=Caninos, multiplicity=Multiplicity(1, 1)),
        Property(name="Empresa_Class_115", type=Empresa, multiplicity=Multiplicity(0, 9999))
    }
)
Empresa________________________Caninos2: BinaryAssociation = BinaryAssociation(
    name="Empresa________________________Caninos2",
    ends={
        Property(name="Empresa________________________Caninos2_119", type=Empresa, multiplicity=Multiplicity(0, 9999)),
        Property(name="canino_318", type=Caninos, multiplicity=Multiplicity(1, 1))
    }
)
Empresa________________________Caninos3: BinaryAssociation = BinaryAssociation(
    name="Empresa________________________Caninos3",
    ends={
        Property(name="canino_420", type=Caninos, multiplicity=Multiplicity(1, 1)),
        Property(name="Empresa________________________Caninos3_121", type=Empresa, multiplicity=Multiplicity(0, 9999))
    }
)
Empresa________________________Caninos: BinaryAssociation = BinaryAssociation(
    name="Empresa________________________Caninos",
    ends={
        Property(name="canino_216", type=Caninos, multiplicity=Multiplicity(0, 9999)),
        Property(name="Empresa________________________Caninos_117", type=Empresa, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_vkhvQJ3PEemddr62D2Sizg",
    types={Usuario_Actor, _Buscar_un_ejemplar_por_su_nombre___UseCase, Calcular_el_n_mero_de_ejemplares_caninos_por_raza_UseCase, _Calcular_el_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase, Avanzar_hacia_el_siguiente_ejemplar_UseCase, _Regresar_hacia_el_anterior_ejemplar_UseCase, Desplazarse_hasta_el_primer_ejemplar_UseCase, Desplazarse_hasta_el__ltimo_ejemplar_UseCase, Empresa, Caninos},
    associations={Usuario__Buscar_un_ejemplar_por_su_nombre_, Usuario_Calcular_el_n_mero_de_ejemplares_caninos_por_raza, Usuario__Calcular_el_promedio_de_edad_de_todos_los_ejemplares_caninos_, Usuario_Avanzar_hacia_el_siguiente_ejemplar, Usuario__Regresar_hacia_el_anterior_ejemplar, Usuario_Desplazarse_hasta_el_primer_ejemplar, Usuario_Desplazarse_hasta_el__ltimo_ejemplar, Empresa_Class, Empresa________________________Caninos2, Empresa________________________Caninos3, Empresa________________________Caninos},
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