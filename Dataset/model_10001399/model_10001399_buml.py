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
AGENDA_TELEFONICA_Component = Class(name="AGENDA_TELEFONICA_Component")
Agregar_Contactos_UseCase = Class(name="Agregar_Contactos_UseCase")
Buscar_Contactos_UseCase = Class(name="Buscar_Contactos_UseCase")
Eliminar_Contacto_UseCase = Class(name="Eliminar_Contacto_UseCase")
Editar_Contacto_UseCase = Class(name="Editar_Contacto_UseCase")
Salir_de_la_aplicacion_UseCase = Class(name="Salir_de_la_aplicacion_UseCase")
Ver_detalles_de_contacto_UseCase = Class(name="Ver_detalles_de_contacto_UseCase")
Actualizar_Coredata_UseCase = Class(name="Actualizar_Coredata_UseCase")
Usuario_Actor = Class(name="Usuario_Actor")
Contacto = Class(name="Contacto")
Ver_Contactos_external = Class(name="Ver_Contactos_external")

# AGENDA_TELEFONICA_Component class attributes and methods

# Agregar_Contactos_UseCase class attributes and methods

# Buscar_Contactos_UseCase class attributes and methods

# Eliminar_Contacto_UseCase class attributes and methods

# Editar_Contacto_UseCase class attributes and methods

# Salir_de_la_aplicacion_UseCase class attributes and methods

# Ver_detalles_de_contacto_UseCase class attributes and methods

# Actualizar_Coredata_UseCase class attributes and methods

# Usuario_Actor class attributes and methods

# Contacto class attributes and methods
Contacto_Nombre: Property = Property(name="Nombre", type=StringType)
Contacto_Apellido: Property = Property(name="Apellido", type=StringType)
Contacto_Email: Property = Property(name="Email", type=StringType)
Contacto_Telefono: Property = Property(name="Telefono", type=IntegerType)
Contacto_Foto: Property = Property(name="Foto", type=StringType)
Contacto_user: Property = Property(name="user", type=StringType)
Contacto_id: Property = Property(name="id", type=IntegerType)
Contacto_Groups: Property = Property(name="Groups", type=StringType)
Contacto.attributes={Contacto_Telefono, Contacto_id, Contacto_Email, Contacto_user, Contacto_Groups, Contacto_Apellido, Contacto_Nombre, Contacto_Foto}

# Ver_Contactos_external class attributes and methods

# Relationships
Usuario_Agregar_Contactos: BinaryAssociation = BinaryAssociation(
    name="Usuario_Agregar_Contactos",
    ends={
        Property(name="agregar_Contactos2", type=Agregar_Contactos_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario3", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Buscar_Contactos: BinaryAssociation = BinaryAssociation(
    name="Usuario_Buscar_Contactos",
    ends={
        Property(name="buscar_Contactos4", type=Buscar_Contactos_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario5", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Eliminar_Contacto: BinaryAssociation = BinaryAssociation(
    name="Usuario_Eliminar_Contacto",
    ends={
        Property(name="eliminar_Contacto6", type=Eliminar_Contacto_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario7", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Editar_Contacto: BinaryAssociation = BinaryAssociation(
    name="Usuario_Editar_Contacto",
    ends={
        Property(name="editar_Contacto8", type=Editar_Contacto_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario9", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Salir_de_la_aplicacion: BinaryAssociation = BinaryAssociation(
    name="Usuario_Salir_de_la_aplicacion",
    ends={
        Property(name="salir_de_la_aplicacion10", type=Salir_de_la_aplicacion_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario11", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Ver_detalles_de_contacto: BinaryAssociation = BinaryAssociation(
    name="Usuario_Ver_detalles_de_contacto",
    ends={
        Property(name="ver_detalles_de_contacto12", type=Ver_detalles_de_contacto_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario13", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Ver_Contactos: BinaryAssociation = BinaryAssociation(
    name="Usuario_Ver_Contactos",
    ends={
        Property(name="ver_Contactos0", type=Ver_Contactos_external, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario1", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4Q2DUGTvEeepGY91r9Nuow",
    types={AGENDA_TELEFONICA_Component, Agregar_Contactos_UseCase, Buscar_Contactos_UseCase, Eliminar_Contacto_UseCase, Editar_Contacto_UseCase, Salir_de_la_aplicacion_UseCase, Ver_detalles_de_contacto_UseCase, Actualizar_Coredata_UseCase, Usuario_Actor, Contacto, Ver_Contactos_external},
    associations={Usuario_Agregar_Contactos, Usuario_Buscar_Contactos, Usuario_Eliminar_Contacto, Usuario_Editar_Contacto, Usuario_Salir_de_la_aplicacion, Usuario_Ver_detalles_de_contacto, Usuario_Ver_Contactos},
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