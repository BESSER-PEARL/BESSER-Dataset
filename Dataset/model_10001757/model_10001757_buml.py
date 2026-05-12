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
User_Actor = Class(name="User_Actor")
Directorio = Class(name="Directorio")
Contacto = Class(name="Contacto")
Direccion = Class(name="Direccion")
Telefono = Class(name="Telefono")
Foto_de_perfil = Class(name="Foto_de_perfil")

# User_Actor class attributes and methods

# Directorio class attributes and methods
Directorio_Introducir: Property = Property(name="Introducir", type=StringType)
Directorio.attributes={Directorio_Introducir}

# Contacto class attributes and methods
Contacto_Nombre: Property = Property(name="Nombre", type=StringType)
Contacto_Correo: Property = Property(name="Correo", type=StringType)
Contacto.attributes={Contacto_Nombre, Contacto_Correo}

# Direccion class attributes and methods
Direccion_Nombre: Property = Property(name="Nombre", type=StringType)
Direccion_Codigo_Postal: Property = Property(name="Codigo_Postal", type=IntegerType)
Direccion_Ciudad: Property = Property(name="Ciudad", type=StringType)
Direccion_Pais: Property = Property(name="Pais", type=StringType)
Direccion.attributes={Direccion_Ciudad, Direccion_Pais, Direccion_Codigo_Postal, Direccion_Nombre}

# Telefono class attributes and methods
Telefono_Codigo_de_Area: Property = Property(name="Codigo_de_Area", type=IntegerType)
Telefono_Prefijo: Property = Property(name="Prefijo", type=IntegerType)
Telefono_Numero: Property = Property(name="Numero", type=IntegerType)
Telefono.attributes={Telefono_Prefijo, Telefono_Numero, Telefono_Codigo_de_Area}

# Foto_de_perfil class attributes and methods

# Relationships
Directorio_Contacto: BinaryAssociation = BinaryAssociation(
    name="Directorio_Contacto",
    ends={
        Property(name="contacto0", type=Contacto, multiplicity=Multiplicity(0, 1)),
        Property(name="directorio1", type=Directorio, multiplicity=Multiplicity(0, 1))
    }
)
Contacto_Direccion: BinaryAssociation = BinaryAssociation(
    name="Contacto_Direccion",
    ends={
        Property(name="direccion_Principal2", type=Direccion, multiplicity=Multiplicity(0, 1)),
        Property(name="contacto3", type=Contacto, multiplicity=Multiplicity(0, 1))
    }
)
Contacto_Direccion2: BinaryAssociation = BinaryAssociation(
    name="Contacto_Direccion2",
    ends={
        Property(name="direccion4", type=Direccion, multiplicity=Multiplicity(0, 1)),
        Property(name="contacto5", type=Contacto, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_TV_0wCcZEeiYD9TOdwevwA",
    types={User_Actor, Directorio, Contacto, Direccion, Telefono, Foto_de_perfil},
    associations={Directorio_Contacto, Contacto_Direccion, Contacto_Direccion2},
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