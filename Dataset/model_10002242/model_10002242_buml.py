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
Buscar_Contactos_UseCase = Class(name="Buscar_Contactos_UseCase")
Crear_Contacto_UseCase = Class(name="Crear_Contacto_UseCase")
Actualizar_COntacto_UseCase = Class(name="Actualizar_COntacto_UseCase")
Eliminar_Contacto_UseCase = Class(name="Eliminar_Contacto_UseCase")
Guardar_UseCase = Class(name="Guardar_UseCase")
Cancelar_UseCase = Class(name="Cancelar_UseCase")
Libro_de_Direcciones = Class(name="Libro_de_Direcciones")
Contacto = Class(name="Contacto")
Direccion = Class(name="Direccion")
Tel_fono = Class(name="Tel_fono")
Foto = Class(name="Foto")
Libro_de_Direcciones1 = Class(name="Libro_de_Direcciones1")
Menu_Principal = Class(name="Menu_Principal")
Buscar = Class(name="Buscar")
Crear_Contacto = Class(name="Crear_Contacto")
Lista_de_COntacto = Class(name="Lista_de_COntacto")

# Usuario_Actor class attributes and methods

# Buscar_Contactos_UseCase class attributes and methods

# Crear_Contacto_UseCase class attributes and methods

# Actualizar_COntacto_UseCase class attributes and methods

# Eliminar_Contacto_UseCase class attributes and methods

# Guardar_UseCase class attributes and methods

# Cancelar_UseCase class attributes and methods

# Libro_de_Direcciones class attributes and methods
Libro_de_Direcciones_Introduccion: Property = Property(name="Introduccion", type=StringType)
Libro_de_Direcciones.attributes={Libro_de_Direcciones_Introduccion}

# Contacto class attributes and methods
Contacto_nombre: Property = Property(name="nombre", type=StringType)
Contacto_email: Property = Property(name="email", type=StringType)
Contacto.attributes={Contacto_email, Contacto_nombre}

# Direccion class attributes and methods
Direccion_nombre: Property = Property(name="nombre", type=StringType)
Direccion_CodigoPostal: Property = Property(name="CodigoPostal", type=IntegerType)
Direccion_Ciudad: Property = Property(name="Ciudad", type=StringType)
Direccion_departamento: Property = Property(name="departamento", type=StringType)
Direccion.attributes={Direccion_nombre, Direccion_CodigoPostal, Direccion_Ciudad, Direccion_departamento}

# Tel_fono class attributes and methods
Tel_fono_Codigo_area: Property = Property(name="Codigo_area", type=IntegerType)
Tel_fono_prefijo: Property = Property(name="prefijo", type=IntegerType)
Tel_fono_numero: Property = Property(name="numero", type=IntegerType)
Tel_fono.attributes={Tel_fono_Codigo_area, Tel_fono_prefijo, Tel_fono_numero}

# Foto class attributes and methods
Foto_largo: Property = Property(name="largo", type=IntegerType)
Foto_ancho: Property = Property(name="ancho", type=IntegerType)
Foto.attributes={Foto_ancho, Foto_largo}

# Libro_de_Direcciones1 class attributes and methods

# Menu_Principal class attributes and methods

# Buscar class attributes and methods

# Crear_Contacto class attributes and methods

# Lista_de_COntacto class attributes and methods

# Relationships
Usuario_Buscar_Contactos: BinaryAssociation = BinaryAssociation(
    name="Usuario_Buscar_Contactos",
    ends={
        Property(name="buscar_Contactos0", type=Buscar_Contactos_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario1", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Crear_Contacto: BinaryAssociation = BinaryAssociation(
    name="Usuario_Crear_Contacto",
    ends={
        Property(name="crear_Contacto2", type=Crear_Contacto_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario3", type=Usuario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_Actualizar_COntacto: BinaryAssociation = BinaryAssociation(
    name="Usuario_Actualizar_COntacto",
    ends={
        Property(name="actualizar_COntacto4", type=Actualizar_COntacto_UseCase, multiplicity=Multiplicity(0, 1)),
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
Contacto_Direccion: BinaryAssociation = BinaryAssociation(
    name="Contacto_Direccion",
    ends={
        Property(name="direccion8", type=Direccion, multiplicity=Multiplicity(0, 1)),
        Property(name="contacto9", type=Contacto, multiplicity=Multiplicity(0, 1))
    }
)
Contacto_Tel_fono: BinaryAssociation = BinaryAssociation(
    name="Contacto_Tel_fono",
    ends={
        Property(name="tel_fono10", type=Tel_fono, multiplicity=Multiplicity(0, 1)),
        Property(name="contacto11", type=Contacto, multiplicity=Multiplicity(0, 1))
    }
)
Contacto_Foto: BinaryAssociation = BinaryAssociation(
    name="Contacto_Foto",
    ends={
        Property(name="foto12", type=Foto, multiplicity=Multiplicity(0, 1)),
        Property(name="contacto13", type=Contacto, multiplicity=Multiplicity(0, 1))
    }
)
Libro_de_Direcciones_Contacto: BinaryAssociation = BinaryAssociation(
    name="Libro_de_Direcciones_Contacto",
    ends={
        Property(name="contacto14", type=Contacto, multiplicity=Multiplicity(0, 1)),
        Property(name="libro_de_Direcciones15", type=Libro_de_Direcciones, multiplicity=Multiplicity(0, 1))
    }
)
Libro_de_Direcciones_Menu_Principal: BinaryAssociation = BinaryAssociation(
    name="Libro_de_Direcciones_Menu_Principal",
    ends={
        Property(name="menu_Principal16", type=Menu_Principal, multiplicity=Multiplicity(0, 1)),
        Property(name="libro_de_Direcciones17", type=Libro_de_Direcciones1, multiplicity=Multiplicity(0, 1))
    }
)
Menu_Principal_Lista_de_COntacto: BinaryAssociation = BinaryAssociation(
    name="Menu_Principal_Lista_de_COntacto",
    ends={
        Property(name="lista_de_COntacto18", type=Lista_de_COntacto, multiplicity=Multiplicity(0, 1)),
        Property(name="menu_Principal19", type=Menu_Principal, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_yrAlQCcYEeiYD9TOdwevwA",
    types={Usuario_Actor, Buscar_Contactos_UseCase, Crear_Contacto_UseCase, Actualizar_COntacto_UseCase, Eliminar_Contacto_UseCase, Guardar_UseCase, Cancelar_UseCase, Libro_de_Direcciones, Contacto, Direccion, Tel_fono, Foto, Libro_de_Direcciones1, Menu_Principal, Buscar, Crear_Contacto, Lista_de_COntacto},
    associations={Usuario_Buscar_Contactos, Usuario_Crear_Contacto, Usuario_Actualizar_COntacto, Usuario_Eliminar_Contacto, Contacto_Direccion, Contacto_Tel_fono, Contacto_Foto, Libro_de_Direcciones_Contacto, Libro_de_Direcciones_Menu_Principal, Menu_Principal_Lista_de_COntacto},
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