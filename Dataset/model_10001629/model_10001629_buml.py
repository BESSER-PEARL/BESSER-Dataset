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
Buscar_ejemplar_por_su_nombre__UseCase = Class(name="Buscar_ejemplar_por_su_nombre__UseCase")
Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase = Class(name="Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase")
Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase = Class(name="Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase")
Avanzar_hacia_el_siguiente_ejemplar__UseCase = Class(name="Avanzar_hacia_el_siguiente_ejemplar__UseCase")
Regresar_hacia_el_anterior_ejemplar__UseCase = Class(name="Regresar_hacia_el_anterior_ejemplar__UseCase")
Desplazarse_hasta_el_primer_ejemplar__UseCase = Class(name="Desplazarse_hasta_el_primer_ejemplar__UseCase")
Desplazarse_hasta_el__ltimo_ejemplar__UseCase = Class(name="Desplazarse_hasta_el__ltimo_ejemplar__UseCase")
Empresa = Class(name="Empresa")
Caninos = Class(name="Caninos")

# Usuario_Actor class attributes and methods

# Buscar_ejemplar_por_su_nombre__UseCase class attributes and methods

# Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase class attributes and methods

# Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase class attributes and methods

# Avanzar_hacia_el_siguiente_ejemplar__UseCase class attributes and methods

# Regresar_hacia_el_anterior_ejemplar__UseCase class attributes and methods

# Desplazarse_hasta_el_primer_ejemplar__UseCase class attributes and methods

# Desplazarse_hasta_el__ltimo_ejemplar__UseCase class attributes and methods

# Empresa class attributes and methods

# Caninos class attributes and methods
Caninos_nombre: Property = Property(name="nombre", type=StringType)
Caninos_raza: Property = Property(name="raza", type=StringType)
Caninos_edad: Property = Property(name="edad", type=StringType)
Caninos_peso: Property = Property(name="peso", type=StringType)
Caninos_altura: Property = Property(name="altura", type=StringType)
Caninos_observaciones: Property = Property(name="observaciones", type=StringType)
Caninos.attributes={Caninos_peso, Caninos_observaciones, Caninos_edad, Caninos_altura, Caninos_nombre, Caninos_raza}

# Relationships
Empresa_Caninos: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos",
    ends={
        Property(name="caninos14", type=Caninos, multiplicity=Multiplicity(0, 9999)),
        Property(name="Empresa_Caninos_115", type=Empresa, multiplicity=Multiplicity(0, 9999))
    }
)
Usuario_Buscar_ejemplar_por_su_nombre_: BinaryAssociation = BinaryAssociation(
    name="Usuario_Buscar_ejemplar_por_su_nombre_",
    ends={
        Property(name="buscar_ejemplar_por_su_nombre_0", type=Buscar_ejemplar_por_su_nombre__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario1", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Calcular_n_mero_de_ejemplares_caninos_por_raza_: BinaryAssociation = BinaryAssociation(
    name="Usuario_Calcular_n_mero_de_ejemplares_caninos_por_raza_",
    ends={
        Property(name="calcular_n_mero_de_ejemplares_caninos_por_raza_2", type=Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario3", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos_: BinaryAssociation = BinaryAssociation(
    name="Usuario_Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos_",
    ends={
        Property(name="calcular_promedio_de_edad_de_todos_los_ejemplares_caninos_4", type=Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario5", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Avanzar_hacia_el_siguiente_ejemplar_: BinaryAssociation = BinaryAssociation(
    name="Usuario_Avanzar_hacia_el_siguiente_ejemplar_",
    ends={
        Property(name="avanzar_hacia_el_siguiente_ejemplar_6", type=Avanzar_hacia_el_siguiente_ejemplar__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario7", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Regresar_hacia_el_anterior_ejemplar_: BinaryAssociation = BinaryAssociation(
    name="Usuario_Regresar_hacia_el_anterior_ejemplar_",
    ends={
        Property(name="regresar_hacia_el_anterior_ejemplar_8", type=Regresar_hacia_el_anterior_ejemplar__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario9", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Desplazarse_hasta_el_primer_ejemplar_: BinaryAssociation = BinaryAssociation(
    name="Usuario_Desplazarse_hasta_el_primer_ejemplar_",
    ends={
        Property(name="desplazarse_hasta_el_primer_ejemplar_10", type=Desplazarse_hasta_el_primer_ejemplar__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario11", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Desplazarse_hasta_el__ltimo_ejemplar_: BinaryAssociation = BinaryAssociation(
    name="Usuario_Desplazarse_hasta_el__ltimo_ejemplar_",
    ends={
        Property(name="desplazarse_hasta_el__ltimo_ejemplar_12", type=Desplazarse_hasta_el__ltimo_ejemplar__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario13", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_KHUpwJ3WEemddr62D2Sizg",
    types={Usuario_Actor, Buscar_ejemplar_por_su_nombre__UseCase, Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase, Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase, Avanzar_hacia_el_siguiente_ejemplar__UseCase, Regresar_hacia_el_anterior_ejemplar__UseCase, Desplazarse_hasta_el_primer_ejemplar__UseCase, Desplazarse_hasta_el__ltimo_ejemplar__UseCase, Empresa, Caninos},
    associations={Empresa_Caninos, Usuario_Buscar_ejemplar_por_su_nombre_, Usuario_Calcular_n_mero_de_ejemplares_caninos_por_raza_, Usuario_Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos_, Usuario_Avanzar_hacia_el_siguiente_ejemplar_, Usuario_Regresar_hacia_el_anterior_ejemplar_, Usuario_Desplazarse_hasta_el_primer_ejemplar_, Usuario_Desplazarse_hasta_el__ltimo_ejemplar_},
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