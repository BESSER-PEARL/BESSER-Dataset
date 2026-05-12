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
Usuario__Actor = Class(name="Usuario__Actor")
Interfaz_veterinaria_UseCase = Class(name="Interfaz_veterinaria_UseCase")
Avanzar_UseCase = Class(name="Avanzar_UseCase")
Anterior_UseCase = Class(name="Anterior_UseCase")
Ir_al_primero_UseCase = Class(name="Ir_al_primero_UseCase")
Ir_al_ultimo_UseCase = Class(name="Ir_al_ultimo_UseCase")
Buscar_perro_por_nombre_UseCase = Class(name="Buscar_perro_por_nombre_UseCase")
Calcular_cantidad_por_raza_UseCase = Class(name="Calcular_cantidad_por_raza_UseCase")
Calcular_promedio_edad_perros_UseCase = Class(name="Calcular_promedio_edad_perros_UseCase")
Empresa = Class(name="Empresa")
Caninos = Class(name="Caninos")
int = Class(name="int")
double = Class(name="double")
Empresa1 = Class(name="Empresa1")
Caninos1 = Class(name="Caninos1")
Empresa2 = Class(name="Empresa2")
Caninos2 = Class(name="Caninos2")

# Usuario__Actor class attributes and methods

# Interfaz_veterinaria_UseCase class attributes and methods

# Avanzar_UseCase class attributes and methods

# Anterior_UseCase class attributes and methods

# Ir_al_primero_UseCase class attributes and methods

# Ir_al_ultimo_UseCase class attributes and methods

# Buscar_perro_por_nombre_UseCase class attributes and methods

# Calcular_cantidad_por_raza_UseCase class attributes and methods

# Calcular_promedio_edad_perros_UseCase class attributes and methods

# Empresa class attributes and methods
Empresa_ArrayList: Property = Property(name="ArrayList", type=Caninos)
Empresa_Empresa: Property = Property(name="Empresa", type=StringType)
Empresa_getCaninos: Property = Property(name="getCaninos", type=StringType)
Empresa_getCaninos1: Property = Property(name="getCaninos1", type=StringType)
Empresa_getCaninos2: Property = Property(name="getCaninos2", type=StringType)
Empresa_getCaninos3: Property = Property(name="getCaninos3", type=StringType)
Empresa_Cantidad_razaCanina: Property = Property(name="Cantidad_razaCanina", type=StringType)
Empresa_Promedio_canino: Property = Property(name="Promedio_canino", type=StringType)
Empresa_buscarCaninos: Property = Property(name="buscarCaninos", type=StringType)
Empresa.attributes={Empresa_Empresa, Empresa_getCaninos, Empresa_getCaninos2, Empresa_buscarCaninos, Empresa_getCaninos3, Empresa_getCaninos1, Empresa_Promedio_canino, Empresa_Cantidad_razaCanina, Empresa_ArrayList}

# Caninos class attributes and methods
Caninos_nombre: Property = Property(name="nombre", type=StringType)
Caninos_raza: Property = Property(name="raza", type=StringType)
Caninos_edad: Property = Property(name="edad", type=IntegerType)
Caninos_peso: Property = Property(name="peso", type=double)
Caninos_altura: Property = Property(name="altura", type=IntegerType)
Caninos_observaciones: Property = Property(name="observaciones", type=StringType)
Caninos_attribute: Property = Property(name="attribute", type=StringType)
Caninos.attributes={Caninos_raza, Caninos_attribute, Caninos_edad, Caninos_peso, Caninos_observaciones, Caninos_altura, Caninos_nombre}

# int class attributes and methods

# double class attributes and methods

# Empresa1 class attributes and methods

# Caninos1 class attributes and methods
Caninos1_nombre: Property = Property(name="nombre", type=StringType)
Caninos1_raza: Property = Property(name="raza", type=StringType)
Caninos1_edad: Property = Property(name="edad", type=IntegerType)
Caninos1_peso: Property = Property(name="peso", type=IntegerType)
Caninos1_altura: Property = Property(name="altura", type=double)
Caninos1_observaciones: Property = Property(name="observaciones", type=StringType)
Caninos1.attributes={Caninos1_raza, Caninos1_edad, Caninos1_nombre, Caninos1_peso, Caninos1_observaciones, Caninos1_altura}

# Empresa2 class attributes and methods

# Caninos2 class attributes and methods

# Relationships
Usuario__Calcular_el_ejemplear_por_nombre: BinaryAssociation = BinaryAssociation(
    name="Usuario__Calcular_el_ejemplear_por_nombre",
    ends={
        Property(name="calcular_el_ejemplear_por_nombre8", type=Buscar_perro_por_nombre_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario9", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Calcular_el_numero_ejemplar_por_raza: BinaryAssociation = BinaryAssociation(
    name="Usuario__Calcular_el_numero_ejemplar_por_raza",
    ends={
        Property(name="calcular_el_numero_ejemplar_por_raza10", type=Calcular_cantidad_por_raza_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario11", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Avanzar_hasta_el_siguiente_ejemplar: BinaryAssociation = BinaryAssociation(
    name="Usuario__Avanzar_hasta_el_siguiente_ejemplar",
    ends={
        Property(name="avanzar_hasta_el_siguiente_ejemplar0", type=Avanzar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario1", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Regresar_hacia_el_anterior_ejemplar: BinaryAssociation = BinaryAssociation(
    name="Usuario__Regresar_hacia_el_anterior_ejemplar",
    ends={
        Property(name="regresar_hacia_el_anterior_ejemplar2", type=Anterior_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario3", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Desplazarse_hasta_el_primer_ejemplar: BinaryAssociation = BinaryAssociation(
    name="Usuario__Desplazarse_hasta_el_primer_ejemplar",
    ends={
        Property(name="desplazarse_hasta_el_primer_ejemplar4", type=Ir_al_primero_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario5", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Desplazarse_hasta_el_primer_ejemplar1: BinaryAssociation = BinaryAssociation(
    name="Usuario__Desplazarse_hasta_el_primer_ejemplar1",
    ends={
        Property(name="desplazarse_hasta_el_primer_ejemplar6", type=Ir_al_ultimo_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario7", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Visualizar_Hoja_de_vida_de_los_caninos: BinaryAssociation = BinaryAssociation(
    name="Usuario__Visualizar_Hoja_de_vida_de_los_caninos",
    ends={
        Property(name="visualizar_Hoja_de_vida_de_los_caninos12", type=Interfaz_veterinaria_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario13", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Calcular_el_primedio_de_edad_de_los_ejemplares: BinaryAssociation = BinaryAssociation(
    name="Usuario__Calcular_el_primedio_de_edad_de_los_ejemplares",
    ends={
        Property(name="calcular_el_primedio_de_edad_de_los_ejemplares14", type=Calcular_promedio_edad_perros_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario15", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Veterinaria_Ejemplares_caninos: BinaryAssociation = BinaryAssociation(
    name="Veterinaria_Ejemplares_caninos",
    ends={
        Property(name="ejemplares_caninos16", type=Caninos, multiplicity=Multiplicity(0, 1)),
        Property(name="veterinaria17", type=Empresa, multiplicity=Multiplicity(0, 1))
    }
)
Veterinaria_Ejemplares_caninos_2: BinaryAssociation = BinaryAssociation(
    name="Veterinaria_Ejemplares_caninos_2",
    ends={
        Property(name="ejemplares_caninos18", type=Caninos, multiplicity=Multiplicity(0, 1)),
        Property(name="veterinaria19", type=Empresa, multiplicity=Multiplicity(0, 1))
    }
)
Veterinaria_Ejemplares_caninos_3: BinaryAssociation = BinaryAssociation(
    name="Veterinaria_Ejemplares_caninos_3",
    ends={
        Property(name="ejemplares_caninos20", type=Caninos, multiplicity=Multiplicity(0, 1)),
        Property(name="veterinaria21", type=Empresa, multiplicity=Multiplicity(0, 1))
    }
)
Veterinaria_Ejemplares_caninos_4: BinaryAssociation = BinaryAssociation(
    name="Veterinaria_Ejemplares_caninos_4",
    ends={
        Property(name="ejemplares_caninos22", type=Caninos, multiplicity=Multiplicity(0, 1)),
        Property(name="veterinaria23", type=Empresa, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos",
    ends={
        Property(name="caninos24", type=Caninos1, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa25", type=Empresa1, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos_2: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos_2",
    ends={
        Property(name="caninos26", type=Caninos1, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa27", type=Empresa1, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos_3: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos_3",
    ends={
        Property(name="caninos28", type=Caninos1, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa29", type=Empresa1, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos_4: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos_4",
    ends={
        Property(name="caninos30", type=Caninos1, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa31", type=Empresa1, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos1: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos1",
    ends={
        Property(name="caninos32", type=Caninos2, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa33", type=Empresa2, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos2: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos2",
    ends={
        Property(name="caninos34", type=Caninos2, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa35", type=Empresa2, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos3: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos3",
    ends={
        Property(name="caninos36", type=Caninos2, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa37", type=Empresa2, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos4: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos4",
    ends={
        Property(name="caninos38", type=Caninos2, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa39", type=Empresa2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="daab2f1b_749d_4e06_8f0f_07cf9b5da404",
    types={Usuario__Actor, Interfaz_veterinaria_UseCase, Avanzar_UseCase, Anterior_UseCase, Ir_al_primero_UseCase, Ir_al_ultimo_UseCase, Buscar_perro_por_nombre_UseCase, Calcular_cantidad_por_raza_UseCase, Calcular_promedio_edad_perros_UseCase, Empresa, Caninos, int, double, Empresa1, Caninos1, Empresa2, Caninos2},
    associations={Usuario__Calcular_el_ejemplear_por_nombre, Usuario__Calcular_el_numero_ejemplar_por_raza, Usuario__Avanzar_hasta_el_siguiente_ejemplar, Usuario__Regresar_hacia_el_anterior_ejemplar, Usuario__Desplazarse_hasta_el_primer_ejemplar, Usuario__Desplazarse_hasta_el_primer_ejemplar1, Usuario__Visualizar_Hoja_de_vida_de_los_caninos, Usuario__Calcular_el_primedio_de_edad_de_los_ejemplares, Veterinaria_Ejemplares_caninos, Veterinaria_Ejemplares_caninos_2, Veterinaria_Ejemplares_caninos_3, Veterinaria_Ejemplares_caninos_4, Empresa_Caninos, Empresa_Caninos_2, Empresa_Caninos_3, Empresa_Caninos_4, Empresa_Caninos1, Empresa_Caninos2, Empresa_Caninos3, Empresa_Caninos4},
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