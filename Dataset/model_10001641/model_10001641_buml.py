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
Avanzar_hacia_el_siguiente__UseCase = Class(name="Avanzar_hacia_el_siguiente__UseCase")
Regresar_hacia_el_anterior_UseCase = Class(name="Regresar_hacia_el_anterior_UseCase")
Desplazarse_hasta_el_primer_UseCase = Class(name="Desplazarse_hasta_el_primer_UseCase")
Desplazarse_hasta_el_ultimo_UseCase = Class(name="Desplazarse_hasta_el_ultimo_UseCase")
Buscar_un_ejemplar_por_su_nombre_UseCase = Class(name="Buscar_un_ejemplar_por_su_nombre_UseCase")
Calcular_el_numero_de_ejemplares_UseCase = Class(name="Calcular_el_numero_de_ejemplares_UseCase")
Calcular_el_promedio_de_edad_UseCase = Class(name="Calcular_el_promedio_de_edad_UseCase")
Veterinario = Class(name="Veterinario")
Datos = Class(name="Datos")

# Usuario__Actor class attributes and methods

# Avanzar_hacia_el_siguiente__UseCase class attributes and methods

# Regresar_hacia_el_anterior_UseCase class attributes and methods

# Desplazarse_hasta_el_primer_UseCase class attributes and methods

# Desplazarse_hasta_el_ultimo_UseCase class attributes and methods

# Buscar_un_ejemplar_por_su_nombre_UseCase class attributes and methods

# Calcular_el_numero_de_ejemplares_UseCase class attributes and methods

# Calcular_el_promedio_de_edad_UseCase class attributes and methods

# Veterinario class attributes and methods

# Datos class attributes and methods
Datos_nombre: Property = Property(name="nombre", type=StringType)
Datos_raza: Property = Property(name="raza", type=StringType)
Datos_Edad: Property = Property(name="Edad", type=IntegerType)
Datos_peso: Property = Property(name="peso", type=StringType)
Datos_altura: Property = Property(name="altura", type=StringType)
Datos_observacion: Property = Property(name="observacion", type=StringType)
Datos.attributes={Datos_altura, Datos_Edad, Datos_nombre, Datos_observacion, Datos_raza, Datos_peso}

# Relationships
Avanzar_hacia_el_siguiente__Usuario: BinaryAssociation = BinaryAssociation(
    name="Avanzar_hacia_el_siguiente__Usuario",
    ends={
        Property(name="usuario0", type=Usuario__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="avanzar_hacia_el_siguiente1", type=Avanzar_hacia_el_siguiente__UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Regresar_hacia_el_anterior_Usuario: BinaryAssociation = BinaryAssociation(
    name="Regresar_hacia_el_anterior_Usuario",
    ends={
        Property(name="usuario2", type=Usuario__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="regresar_hacia_el_anterior3", type=Regresar_hacia_el_anterior_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Desplazarse_hasta_el_primer_Usuario: BinaryAssociation = BinaryAssociation(
    name="Desplazarse_hasta_el_primer_Usuario",
    ends={
        Property(name="usuario4", type=Usuario__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="desplazarse_hasta_el_primer5", type=Desplazarse_hasta_el_primer_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Desplazarse_hasta_el_ultimo_Usuario: BinaryAssociation = BinaryAssociation(
    name="Desplazarse_hasta_el_ultimo_Usuario",
    ends={
        Property(name="usuario6", type=Usuario__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="desplazarse_hasta_el_ultimo7", type=Desplazarse_hasta_el_ultimo_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Buscar_un_ejemplar_por_su_nombre_Usuario: BinaryAssociation = BinaryAssociation(
    name="Buscar_un_ejemplar_por_su_nombre_Usuario",
    ends={
        Property(name="usuario8", type=Usuario__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="buscar_un_ejemplar_por_su_nombre9", type=Buscar_un_ejemplar_por_su_nombre_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Calcular_el_numero_de_ejemplares_Usuario: BinaryAssociation = BinaryAssociation(
    name="Calcular_el_numero_de_ejemplares_Usuario",
    ends={
        Property(name="usuario10", type=Usuario__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="calcular_el_numero_de_ejemplares11", type=Calcular_el_numero_de_ejemplares_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Calcular_el_promedio_de_edad_Usuario: BinaryAssociation = BinaryAssociation(
    name="Calcular_el_promedio_de_edad_Usuario",
    ends={
        Property(name="usuario12", type=Usuario__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="calcular_el_promedio_de_edad13", type=Calcular_el_promedio_de_edad_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Veterinario_Datos: BinaryAssociation = BinaryAssociation(
    name="Veterinario_Datos",
    ends={
        Property(name="Veterinario_Datos_014", type=Datos, multiplicity=Multiplicity(0, 1)),
        Property(name="veterinario15", type=Veterinario, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_LEaWYJ3REemddr62D2Sizg",
    types={Usuario__Actor, Avanzar_hacia_el_siguiente__UseCase, Regresar_hacia_el_anterior_UseCase, Desplazarse_hasta_el_primer_UseCase, Desplazarse_hasta_el_ultimo_UseCase, Buscar_un_ejemplar_por_su_nombre_UseCase, Calcular_el_numero_de_ejemplares_UseCase, Calcular_el_promedio_de_edad_UseCase, Veterinario, Datos},
    associations={Avanzar_hacia_el_siguiente__Usuario, Regresar_hacia_el_anterior_Usuario, Desplazarse_hasta_el_primer_Usuario, Desplazarse_hasta_el_ultimo_Usuario, Buscar_un_ejemplar_por_su_nombre_Usuario, Calcular_el_numero_de_ejemplares_Usuario, Calcular_el_promedio_de_edad_Usuario, Veterinario_Datos},
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