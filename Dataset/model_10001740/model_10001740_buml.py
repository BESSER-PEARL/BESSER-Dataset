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
CoordenadaGPS = Class(name="CoordenadaGPS")
ILocalizable_Interface = Class(name="ILocalizable_Interface")
Animal = Class(name="Animal", is_abstract=True)
Gato = Class(name="Gato")
Perro = Class(name="Perro")
Cliente = Class(name="Cliente")

# CoordenadaGPS class attributes and methods
CoordenadaGPS_latitud: Property = Property(name="latitud", type=StringType)
CoordenadaGPS_longitud: Property = Property(name="longitud", type=StringType)
CoordenadaGPS.attributes={CoordenadaGPS_latitud, CoordenadaGPS_longitud}

# ILocalizable_Interface class attributes and methods

# Animal class attributes and methods
Animal_identificador: Property = Property(name="identificador", type=StringType)
Animal_raza: Property = Property(name="raza", type=StringType)
Animal_nombre: Property = Property(name="nombre", type=StringType)
Animal.attributes={Animal_identificador, Animal_nombre, Animal_raza}

# Gato class attributes and methods
Gato_ultimaDesparasitacion: Property = Property(name="ultimaDesparasitacion", type=StringType)
Gato_MESES_ENTRE_DESPARASITACIONES: Property = Property(name="MESES_ENTRE_DESPARASITACIONES", type=StringType)
Gato.attributes={Gato_MESES_ENTRE_DESPARASITACIONES, Gato_ultimaDesparasitacion}

# Perro class attributes and methods
Perro_fechaCastracion: Property = Property(name="fechaCastracion", type=StringType)
Perro.attributes={Perro_fechaCastracion}

# Cliente class attributes and methods
Cliente_numeroDeCliente: Property = Property(name="numeroDeCliente", type=StringType)
Cliente_nombre: Property = Property(name="nombre", type=StringType)
Cliente_listaMascotas: Property = Property(name="listaMascotas", type=StringType)
Cliente.attributes={Cliente_numeroDeCliente, Cliente_nombre, Cliente_listaMascotas}

# Domain Model
domain_model = DomainModel(
    name="_SE8ckBEgEeimSO_GhE8jew",
    types={CoordenadaGPS, ILocalizable_Interface, Animal, Gato, Perro, Cliente},
    associations={},
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