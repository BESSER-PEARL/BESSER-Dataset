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
Visualizar_Hoja_de_vida_de_los_caninos__UseCase = Class(name="Visualizar_Hoja_de_vida_de_los_caninos__UseCase")
Avanzar_hasta_el_siguiente_ejemplar__UseCase = Class(name="Avanzar_hasta_el_siguiente_ejemplar__UseCase")
Regresar_hacia_el_anterior_ejemplar_UseCase = Class(name="Regresar_hacia_el_anterior_ejemplar_UseCase")
Desplazarse_hasta_el_primer_ejemplar__UseCase = Class(name="Desplazarse_hasta_el_primer_ejemplar__UseCase")
Desplazarse_hasta_el_ultimo_ejemplar_UseCase = Class(name="Desplazarse_hasta_el_ultimo_ejemplar_UseCase")
Calcular_el_ejemplear_por_nombre__UseCase = Class(name="Calcular_el_ejemplear_por_nombre__UseCase")
Calcular_el_numero_ejemplar_por_raza__UseCase = Class(name="Calcular_el_numero_ejemplar_por_raza__UseCase")
Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase = Class(name="Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase")
Empresa = Class(name="Empresa")
Caninos = Class(name="Caninos")
int = Class(name="int")
double = Class(name="double")
Empresa1 = Class(name="Empresa1")
Caninos1 = Class(name="Caninos1")
Empresa2 = Class(name="Empresa2")
Caninos2 = Class(name="Caninos2")

# Usuario__Actor class attributes and methods

# Visualizar_Hoja_de_vida_de_los_caninos__UseCase class attributes and methods

# Avanzar_hasta_el_siguiente_ejemplar__UseCase class attributes and methods

# Regresar_hacia_el_anterior_ejemplar_UseCase class attributes and methods

# Desplazarse_hasta_el_primer_ejemplar__UseCase class attributes and methods

# Desplazarse_hasta_el_ultimo_ejemplar_UseCase class attributes and methods

# Calcular_el_ejemplear_por_nombre__UseCase class attributes and methods

# Calcular_el_numero_ejemplar_por_raza__UseCase class attributes and methods

# Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase class attributes and methods

# Empresa class attributes and methods
Empresa_ArrayList: Property = Property(name="ArrayList", type=Caninos)
Empresa_Empresa: Property = Property(name="Empresa", type=StringType)
Empresa_Caninos_informacion: Property = Property(name="Caninos_informacion", type=StringType)
Empresa_getCaninos: Property = Property(name="getCaninos", type=StringType)
Empresa_getCaninos1: Property = Property(name="getCaninos1", type=IntegerType)
Empresa_getCaninos2: Property = Property(name="getCaninos2", type=StringType)
Empresa_getCaninos3: Property = Property(name="getCaninos3", type=StringType)
Empresa_getCaninos4: Property = Property(name="getCaninos4", type=StringType)
Empresa_getCaninos5: Property = Property(name="getCaninos5", type=StringType)
Empresa_getImagen: Property = Property(name="getImagen", type=IntegerType)
Empresa_setImagen: Property = Property(name="setImagen", type=StringType)
Empresa_nuevoCanino: Property = Property(name="nuevoCanino", type=StringType)
Empresa_agregarCaninos: Property = Property(name="agregarCaninos", type=StringType)
Empresa_cantidadRazaCanina: Property = Property(name="cantidadRazaCanina", type=double)
Empresa_Caninos_BuscarCanino: Property = Property(name="Caninos_BuscarCanino", type=StringType)
Empresa.attributes={Empresa_Caninos_informacion, Empresa_getCaninos, Empresa_agregarCaninos, Empresa_getCaninos3, Empresa_ArrayList, Empresa_cantidadRazaCanina, Empresa_getImagen, Empresa_getCaninos5, Empresa_Caninos_BuscarCanino, Empresa_getCaninos4, Empresa_setImagen, Empresa_getCaninos1, Empresa_Empresa, Empresa_getCaninos2, Empresa_nuevoCanino}

# Caninos class attributes and methods
Caninos_nombre: Property = Property(name="nombre", type=StringType)
Caninos_raza: Property = Property(name="raza", type=StringType)
Caninos_edad: Property = Property(name="edad", type=IntegerType)
Caninos_peso: Property = Property(name="peso", type=IntegerType)
Caninos_altura: Property = Property(name="altura", type=double)
Caninos_observaciones: Property = Property(name="observaciones", type=StringType)
Caninos.attributes={Caninos_edad, Caninos_peso, Caninos_observaciones, Caninos_altura, Caninos_nombre, Caninos_raza}

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
Caninos1.attributes={Caninos1_edad, Caninos1_peso, Caninos1_nombre, Caninos1_raza, Caninos1_altura, Caninos1_observaciones}

# Empresa2 class attributes and methods

# Caninos2 class attributes and methods

# Relationships
Usuario__Avanzar_hasta_el_siguiente_ejemplar: BinaryAssociation = BinaryAssociation(
    name="Usuario__Avanzar_hasta_el_siguiente_ejemplar",
    ends={
        Property(name="avanzar_hasta_el_siguiente_ejemplar0", type=Avanzar_hasta_el_siguiente_ejemplar__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario1", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Regresar_hacia_el_anterior_ejemplar: BinaryAssociation = BinaryAssociation(
    name="Usuario__Regresar_hacia_el_anterior_ejemplar",
    ends={
        Property(name="regresar_hacia_el_anterior_ejemplar2", type=Regresar_hacia_el_anterior_ejemplar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario3", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Desplazarse_hasta_el_primer_ejemplar: BinaryAssociation = BinaryAssociation(
    name="Usuario__Desplazarse_hasta_el_primer_ejemplar",
    ends={
        Property(name="desplazarse_hasta_el_primer_ejemplar4", type=Desplazarse_hasta_el_primer_ejemplar__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario5", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Desplazarse_hasta_el_primer_ejemplar1: BinaryAssociation = BinaryAssociation(
    name="Usuario__Desplazarse_hasta_el_primer_ejemplar1",
    ends={
        Property(name="desplazarse_hasta_el_primer_ejemplar6", type=Desplazarse_hasta_el_ultimo_ejemplar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario7", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos_2: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos_2",
    ends={
        Property(name="caninos24", type=Caninos1, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa25", type=Empresa1, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos_3: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos_3",
    ends={
        Property(name="caninos26", type=Caninos1, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa27", type=Empresa1, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos_4: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos_4",
    ends={
        Property(name="caninos28", type=Caninos1, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa29", type=Empresa1, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos1: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos1",
    ends={
        Property(name="caninos30", type=Caninos2, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa31", type=Empresa2, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos2: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos2",
    ends={
        Property(name="caninos32", type=Caninos2, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa33", type=Empresa2, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos3: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos3",
    ends={
        Property(name="caninos34", type=Caninos2, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa35", type=Empresa2, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos4: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos4",
    ends={
        Property(name="caninos36", type=Caninos2, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa37", type=Empresa2, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos5: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos5",
    ends={
        Property(name="caninos38", type=Caninos, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa39", type=Empresa, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Calcular_el_ejemplear_por_nombre: BinaryAssociation = BinaryAssociation(
    name="Usuario__Calcular_el_ejemplear_por_nombre",
    ends={
        Property(name="calcular_el_ejemplear_por_nombre8", type=Calcular_el_ejemplear_por_nombre__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario9", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Calcular_el_numero_ejemplar_por_raza: BinaryAssociation = BinaryAssociation(
    name="Usuario__Calcular_el_numero_ejemplar_por_raza",
    ends={
        Property(name="calcular_el_numero_ejemplar_por_raza10", type=Calcular_el_numero_ejemplar_por_raza__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario11", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Visualizar_Hoja_de_vida_de_los_caninos: BinaryAssociation = BinaryAssociation(
    name="Usuario__Visualizar_Hoja_de_vida_de_los_caninos",
    ends={
        Property(name="visualizar_Hoja_de_vida_de_los_caninos12", type=Visualizar_Hoja_de_vida_de_los_caninos__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario13", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario__Calcular_el_primedio_de_edad_de_los_ejemplares: BinaryAssociation = BinaryAssociation(
    name="Usuario__Calcular_el_primedio_de_edad_de_los_ejemplares",
    ends={
        Property(name="calcular_el_primedio_de_edad_de_los_ejemplares14", type=Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario15", type=Usuario__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Veterinaria_Ejemplares_caninos_2: BinaryAssociation = BinaryAssociation(
    name="Veterinaria_Ejemplares_caninos_2",
    ends={
        Property(name="Caninos16", type=Caninos, multiplicity=Multiplicity(0, 1)),
        Property(name="veterinaria17", type=Empresa, multiplicity=Multiplicity(0, 1))
    }
)
Veterinaria_Ejemplares_caninos_3: BinaryAssociation = BinaryAssociation(
    name="Veterinaria_Ejemplares_caninos_3",
    ends={
        Property(name="Caninos18", type=Caninos, multiplicity=Multiplicity(0, 1)),
        Property(name="veterinaria19", type=Empresa, multiplicity=Multiplicity(0, 1))
    }
)
Veterinaria_Ejemplares_caninos_4: BinaryAssociation = BinaryAssociation(
    name="Veterinaria_Ejemplares_caninos_4",
    ends={
        Property(name="Caninos20", type=Caninos, multiplicity=Multiplicity(0, 1)),
        Property(name="veterinaria21", type=Empresa, multiplicity=Multiplicity(0, 1))
    }
)
Empresa_Caninos: BinaryAssociation = BinaryAssociation(
    name="Empresa_Caninos",
    ends={
        Property(name="caninos22", type=Caninos1, multiplicity=Multiplicity(0, 1)),
        Property(name="empresa23", type=Empresa1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_NXLYUJ3TEemddr62D2Sizg",
    types={Usuario__Actor, Visualizar_Hoja_de_vida_de_los_caninos__UseCase, Avanzar_hasta_el_siguiente_ejemplar__UseCase, Regresar_hacia_el_anterior_ejemplar_UseCase, Desplazarse_hasta_el_primer_ejemplar__UseCase, Desplazarse_hasta_el_ultimo_ejemplar_UseCase, Calcular_el_ejemplear_por_nombre__UseCase, Calcular_el_numero_ejemplar_por_raza__UseCase, Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase, Empresa, Caninos, int, double, Empresa1, Caninos1, Empresa2, Caninos2},
    associations={Usuario__Avanzar_hasta_el_siguiente_ejemplar, Usuario__Regresar_hacia_el_anterior_ejemplar, Usuario__Desplazarse_hasta_el_primer_ejemplar, Usuario__Desplazarse_hasta_el_primer_ejemplar1, Empresa_Caninos_2, Empresa_Caninos_3, Empresa_Caninos_4, Empresa_Caninos1, Empresa_Caninos2, Empresa_Caninos3, Empresa_Caninos4, Empresa_Caninos5, Usuario__Calcular_el_ejemplear_por_nombre, Usuario__Calcular_el_numero_ejemplar_por_raza, Usuario__Visualizar_Hoja_de_vida_de_los_caninos, Usuario__Calcular_el_primedio_de_edad_de_los_ejemplares, Veterinaria_Ejemplares_caninos_2, Veterinaria_Ejemplares_caninos_3, Veterinaria_Ejemplares_caninos_4, Empresa_Caninos},
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