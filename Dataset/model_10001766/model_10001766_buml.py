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
FOTO = Class(name="FOTO")
LIBRO_DE__DIRECCIONES = Class(name="LIBRO_DE__DIRECCIONES")
CONTACTO = Class(name="CONTACTO")
DIRECCION = Class(name="DIRECCION")
TELEFONO = Class(name="TELEFONO")
Actor_Actor = Class(name="Actor_Actor")
Libro_de__Direcciones_Component = Class(name="Libro_de__Direcciones_Component")
Buscar_Contactos_external = Class(name="Buscar_Contactos_external")
Actor_external = Class(name="Actor_external")
Crear_Contacto_external = Class(name="Crear_Contacto_external")
Actualizar__contacto_external = Class(name="Actualizar__contacto_external")
Eliminar_Contacto_external = Class(name="Eliminar_Contacto_external")

# FOTO class attributes and methods
FOTO_ANCHO: Property = Property(name="ANCHO", type=IntegerType)
FOTO_ALTURA: Property = Property(name="ALTURA", type=IntegerType)
FOTO.attributes={FOTO_ANCHO, FOTO_ALTURA}

# LIBRO_DE__DIRECCIONES class attributes and methods
LIBRO_DE__DIRECCIONES_INTRODUCCION: Property = Property(name="INTRODUCCION", type=StringType)
LIBRO_DE__DIRECCIONES.attributes={LIBRO_DE__DIRECCIONES_INTRODUCCION}

# CONTACTO class attributes and methods
CONTACTO_NOMBRE: Property = Property(name="NOMBRE", type=StringType)
CONTACTO_CORREO: Property = Property(name="CORREO", type=StringType)
CONTACTO.attributes={CONTACTO_NOMBRE, CONTACTO_CORREO}

# DIRECCION class attributes and methods
DIRECCION_NOMBRE: Property = Property(name="NOMBRE", type=StringType)
DIRECCION_CODIGO_POSTAL: Property = Property(name="CODIGO_POSTAL", type=StringType)
DIRECCION_CIUDAD: Property = Property(name="CIUDAD", type=StringType)
DIRECCION_ESTADO: Property = Property(name="ESTADO", type=StringType)
DIRECCION.attributes={DIRECCION_CIUDAD, DIRECCION_NOMBRE, DIRECCION_ESTADO, DIRECCION_CODIGO_POSTAL}

# TELEFONO class attributes and methods
TELEFONO_CODIGO_DE__AREA: Property = Property(name="CODIGO_DE__AREA", type=StringType)
TELEFONO_PREFIJO: Property = Property(name="PREFIJO", type=IntegerType)
TELEFONO_NUMBER: Property = Property(name="NUMBER", type=IntegerType)
TELEFONO.attributes={TELEFONO_CODIGO_DE__AREA, TELEFONO_NUMBER, TELEFONO_PREFIJO}

# Actor_Actor class attributes and methods

# Libro_de__Direcciones_Component class attributes and methods

# Buscar_Contactos_external class attributes and methods

# Actor_external class attributes and methods

# Crear_Contacto_external class attributes and methods

# Actualizar__contacto_external class attributes and methods

# Eliminar_Contacto_external class attributes and methods

# Relationships
LIBRO_DE__DIRECCIONES_CONTACTO: BinaryAssociation = BinaryAssociation(
    name="LIBRO_DE__DIRECCIONES_CONTACTO",
    ends={
        Property(name="cONTACTO0", type=CONTACTO, multiplicity=Multiplicity(0, 1)),
        Property(name="LIBRO_DE__DIRECCIONES1", type=LIBRO_DE__DIRECCIONES, multiplicity=Multiplicity(0, 1))
    }
)
CONTACTO__TELEFONO: BinaryAssociation = BinaryAssociation(
    name="CONTACTO__TELEFONO",
    ends={
        Property(name="tELEFONO2", type=TELEFONO, multiplicity=Multiplicity(0, 1)),
        Property(name="cONTACTO3", type=CONTACTO, multiplicity=Multiplicity(0, 1))
    }
)
CONTACTO__FOTO: BinaryAssociation = BinaryAssociation(
    name="CONTACTO__FOTO",
    ends={
        Property(name="fOTO4", type=FOTO, multiplicity=Multiplicity(0, 1)),
        Property(name="cONTACTO5", type=CONTACTO, multiplicity=Multiplicity(0, 1))
    }
)
CONTACTO__DIRECCION: BinaryAssociation = BinaryAssociation(
    name="CONTACTO__DIRECCION",
    ends={
        Property(name="dIRECCION6", type=DIRECCION, multiplicity=Multiplicity(0, 1)),
        Property(name="cONTACTO7", type=CONTACTO, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Buscar_Contactos: BinaryAssociation = BinaryAssociation(
    name="Actor_Buscar_Contactos",
    ends={
        Property(name="buscar_Contactos8", type=Buscar_Contactos_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor9", type=Actor_external, multiplicity=Multiplicity(0, 1))
    }
)
Actor__Crear_Contacto: BinaryAssociation = BinaryAssociation(
    name="Actor__Crear_Contacto",
    ends={
        Property(name="Crear_Contacto10", type=Crear_Contacto_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor11", type=Actor_external, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Actualizar__contacto: BinaryAssociation = BinaryAssociation(
    name="Actor_Actualizar__contacto",
    ends={
        Property(name="actualizar__contacto12", type=Actualizar__contacto_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor13", type=Actor_external, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Eliminar_Contacto: BinaryAssociation = BinaryAssociation(
    name="Actor_Eliminar_Contacto",
    ends={
        Property(name="eliminar_Contacto14", type=Eliminar_Contacto_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor15", type=Actor_external, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_UBNRwCcVEeiYD9TOdwevwA",
    types={FOTO, LIBRO_DE__DIRECCIONES, CONTACTO, DIRECCION, TELEFONO, Actor_Actor, Libro_de__Direcciones_Component, Buscar_Contactos_external, Actor_external, Crear_Contacto_external, Actualizar__contacto_external, Eliminar_Contacto_external},
    associations={LIBRO_DE__DIRECCIONES_CONTACTO, CONTACTO__TELEFONO, CONTACTO__FOTO, CONTACTO__DIRECCION, Actor_Buscar_Contactos, Actor__Crear_Contacto, Actor_Actualizar__contacto, Actor_Eliminar_Contacto},
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