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
Visualizar_hoja_de_vida_de_cada_perrito__UseCase = Class(name="Visualizar_hoja_de_vida_de_cada_perrito__UseCase")
Avanzar_hacia_el_siguiendo_ejemplar__UseCase = Class(name="Avanzar_hacia_el_siguiendo_ejemplar__UseCase")
Regresar_hacia_el_anterior_ejemplar__UseCase = Class(name="Regresar_hacia_el_anterior_ejemplar__UseCase")
Desplazarse_hasta_el_primer_ejemplar_UseCase = Class(name="Desplazarse_hasta_el_primer_ejemplar_UseCase")
Desplazarse_hasta_el_ultimo_ejemplar__UseCase = Class(name="Desplazarse_hasta_el_ultimo_ejemplar__UseCase")
Buscar_un_ejemplar_por_su_nombre__UseCase = Class(name="Buscar_un_ejemplar_por_su_nombre__UseCase")
Calcular_el_numero_de_ejemplares_por_raza__UseCase = Class(name="Calcular_el_numero_de_ejemplares_por_raza__UseCase")
Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase = Class(name="Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase")
Canino = Class(name="Canino")
Empresa = Class(name="Empresa")
void = Class(name="void")
double = Class(name="double")
Int = Class(name="Int")
String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones = Class(name="String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones")
Int2 = Class(name="Int2")
String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2 = Class(name="String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2")

# Usuario_Actor class attributes and methods

# Visualizar_hoja_de_vida_de_cada_perrito__UseCase class attributes and methods

# Avanzar_hacia_el_siguiendo_ejemplar__UseCase class attributes and methods

# Regresar_hacia_el_anterior_ejemplar__UseCase class attributes and methods

# Desplazarse_hasta_el_primer_ejemplar_UseCase class attributes and methods

# Desplazarse_hasta_el_ultimo_ejemplar__UseCase class attributes and methods

# Buscar_un_ejemplar_por_su_nombre__UseCase class attributes and methods

# Calcular_el_numero_de_ejemplares_por_raza__UseCase class attributes and methods

# Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase class attributes and methods

# Canino class attributes and methods
Canino_nombre: Property = Property(name="nombre", type=StringType)
Canino_raza: Property = Property(name="raza", type=StringType)
Canino_edad: Property = Property(name="edad", type=Int)
Canino_peso: Property = Property(name="peso", type=Int)
Canino_altura: Property = Property(name="altura", type=Int)
Canino_observaciones: Property = Property(name="observaciones", type=StringType)
Canino.attributes={Canino_observaciones, Canino_raza, Canino_peso, Canino_edad, Canino_nombre, Canino_altura}

# Empresa class attributes and methods
Empresa_ejemplaresCaninos: Property = Property(name="ejemplaresCaninos", type=StringType)
Empresa.attributes={Empresa_ejemplaresCaninos}

# void class attributes and methods

# double class attributes and methods

# Int class attributes and methods

# String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones class attributes and methods

# Int2 class attributes and methods

# String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2 class attributes and methods

# Relationships
Usuario_UseCase: BinaryAssociation = BinaryAssociation(
    name="Usuario_UseCase",
    ends={
        Property(name="Usuario_UseCase_00", type=Visualizar_hoja_de_vida_de_cada_perrito__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario1", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Usuario_UseCase2",
    ends={
        Property(name="useCase22", type=Avanzar_hacia_el_siguiendo_ejemplar__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario3", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_UseCase3: BinaryAssociation = BinaryAssociation(
    name="Usuario_UseCase3",
    ends={
        Property(name="useCase34", type=Regresar_hacia_el_anterior_ejemplar__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario5", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_UseCase4: BinaryAssociation = BinaryAssociation(
    name="Usuario_UseCase4",
    ends={
        Property(name="useCase46", type=Desplazarse_hasta_el_primer_ejemplar_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario7", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_UseCase5: BinaryAssociation = BinaryAssociation(
    name="Usuario_UseCase5",
    ends={
        Property(name="useCase58", type=Desplazarse_hasta_el_ultimo_ejemplar__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario9", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_UseCase6: BinaryAssociation = BinaryAssociation(
    name="Usuario_UseCase6",
    ends={
        Property(name="useCase610", type=Buscar_un_ejemplar_por_su_nombre__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario11", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_UseCase7: BinaryAssociation = BinaryAssociation(
    name="Usuario_UseCase7",
    ends={
        Property(name="useCase12", type=Calcular_el_numero_de_ejemplares_por_raza__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario13", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_UseCase22: BinaryAssociation = BinaryAssociation(
    name="Usuario_UseCase22",
    ends={
        Property(name="useCase214", type=Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario15", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_VtpQ0J3PEemddr62D2Sizg",
    types={Usuario_Actor, Visualizar_hoja_de_vida_de_cada_perrito__UseCase, Avanzar_hacia_el_siguiendo_ejemplar__UseCase, Regresar_hacia_el_anterior_ejemplar__UseCase, Desplazarse_hasta_el_primer_ejemplar_UseCase, Desplazarse_hasta_el_ultimo_ejemplar__UseCase, Buscar_un_ejemplar_por_su_nombre__UseCase, Calcular_el_numero_de_ejemplares_por_raza__UseCase, Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase, Canino, Empresa, void, double, Int, String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones, Int2, String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2},
    associations={Usuario_UseCase, Usuario_UseCase2, Usuario_UseCase3, Usuario_UseCase4, Usuario_UseCase5, Usuario_UseCase6, Usuario_UseCase7, Usuario_UseCase22},
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