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
Agenda = Class(name="Agenda")
Contacto = Class(name="Contacto")
Direccion = Class(name="Direccion")
Telefono = Class(name="Telefono")
Foto = Class(name="Foto")

# Agenda class attributes and methods
Agenda_Introduccion: Property = Property(name="Introduccion", type=StringType)
Agenda.attributes={Agenda_Introduccion}

# Contacto class attributes and methods
Contacto_nombre: Property = Property(name="nombre", type=StringType)
Contacto_email: Property = Property(name="email", type=StringType)
Contacto.attributes={Contacto_nombre, Contacto_email}

# Direccion class attributes and methods
Direccion_nombre: Property = Property(name="nombre", type=StringType)
Direccion_codigo: Property = Property(name="codigo", type=IntegerType)
Direccion_ciudad: Property = Property(name="ciudad", type=StringType)
Direccion_pais: Property = Property(name="pais", type=StringType)
Direccion.attributes={Direccion_nombre, Direccion_codigo, Direccion_pais, Direccion_ciudad}

# Telefono class attributes and methods
Telefono_codigo: Property = Property(name="codigo", type=IntegerType)
Telefono_prefijo: Property = Property(name="prefijo", type=IntegerType)
Telefono_numero: Property = Property(name="numero", type=IntegerType)
Telefono.attributes={Telefono_numero, Telefono_codigo, Telefono_prefijo}

# Foto class attributes and methods
Foto_alto: Property = Property(name="alto", type=IntegerType)
Foto_ancho: Property = Property(name="ancho", type=IntegerType)
Foto.attributes={Foto_ancho, Foto_alto}

# Relationships
Agenda_Contacto: BinaryAssociation = BinaryAssociation(
    name="Agenda_Contacto",
    ends={
        Property(name="contacto0", type=Contacto, multiplicity=Multiplicity(0, 9999)),
        Property(name="agenda1", type=Agenda, multiplicity=Multiplicity(1, 1))
    }
)
Direccion_Contacto: BinaryAssociation = BinaryAssociation(
    name="Direccion_Contacto",
    ends={
        Property(name="contacto2", type=Contacto, multiplicity=Multiplicity(1, 1)),
        Property(name="direccionPrincipal3", type=Direccion, multiplicity=Multiplicity(1, 1))
    }
)
Direccion_Contacto2: BinaryAssociation = BinaryAssociation(
    name="Direccion_Contacto2",
    ends={
        Property(name="contacto4", type=Contacto, multiplicity=Multiplicity(1, 1)),
        Property(name="direccionAlternativa5", type=Direccion, multiplicity=Multiplicity(1, 1))
    }
)
Telefono_Contacto: BinaryAssociation = BinaryAssociation(
    name="Telefono_Contacto",
    ends={
        Property(name="contacto6", type=Contacto, multiplicity=Multiplicity(1, 1)),
        Property(name="telefonoPrincipal7", type=Telefono, multiplicity=Multiplicity(1, 1))
    }
)
Telefono_Contacto2: BinaryAssociation = BinaryAssociation(
    name="Telefono_Contacto2",
    ends={
        Property(name="contacto8", type=Contacto, multiplicity=Multiplicity(1, 1)),
        Property(name="telefonoAlternativo9", type=Telefono, multiplicity=Multiplicity(1, 1))
    }
)
Foto_Contacto: BinaryAssociation = BinaryAssociation(
    name="Foto_Contacto",
    ends={
        Property(name="contacto10", type=Contacto, multiplicity=Multiplicity(1, 1)),
        Property(name="foto11", type=Foto, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_80c448ca_68f9_4030_8a3e_ac3e89e10e6f",
    types={Agenda, Contacto, Direccion, Telefono, Foto},
    associations={Agenda_Contacto, Direccion_Contacto, Direccion_Contacto2, Telefono_Contacto, Telefono_Contacto2, Foto_Contacto},
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