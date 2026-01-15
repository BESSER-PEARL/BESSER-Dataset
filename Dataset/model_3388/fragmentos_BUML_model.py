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
Fragmentos_Fragmento = Class(name="Fragmentos::Fragmento")
Fragmentos_Aplicacion = Class(name="Fragmentos::Aplicacion")
Fragmentos_Fichero = Class(name="Fragmentos::Fichero")

# Fragmentos_Fragmento class attributes and methods
Fragmentos_Fragmento_numLinea: Property = Property(name="numLinea", type=IntegerType)
Fragmentos_Fragmento_posCaracter: Property = Property(name="posCaracter", type=IntegerType)
Fragmentos_Fragmento_texto: Property = Property(name="texto", type=StringType)
Fragmentos_Fragmento.attributes={Fragmentos_Fragmento_numLinea, Fragmentos_Fragmento_texto, Fragmentos_Fragmento_posCaracter}

# Fragmentos_Aplicacion class attributes and methods

# Fragmentos_Fichero class attributes and methods
Fragmentos_Fichero_nombre: Property = Property(name="nombre", type=StringType)
Fragmentos_Fichero.attributes={Fragmentos_Fichero_nombre}

# Relationships
ficheros0: BinaryAssociation = BinaryAssociation(
    name="ficheros0",
    ends={
        Property(name="Fragmentos_Aplicacion", type=Fragmentos_Fichero, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Fragmentos_Fichero", type=Fragmentos_Aplicacion, multiplicity=Multiplicity(1, 1))
    }
)
fragmentos1: BinaryAssociation = BinaryAssociation(
    name="fragmentos1",
    ends={
        Property(name="Fragmentos_Fragmento", type=Fragmentos_Fichero, multiplicity=Multiplicity(1, 1)),
        Property(name="Fragmentos_Fichero2", type=Fragmentos_Fragmento, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragmentosSelect3: BinaryAssociation = BinaryAssociation(
    name="fragmentosSelect3",
    ends={
        Property(name="Fragmentos_Fragmento5", type=Fragmentos_Fichero, multiplicity=Multiplicity(1, 1)),
        Property(name="Fragmentos_Fichero4", type=Fragmentos_Fragmento, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sigFragmento7: BinaryAssociation = BinaryAssociation(
    name="sigFragmento7",
    ends={
        Property(name="Fragmentos_Fragmento8", type=Fragmentos_Fragmento, multiplicity=Multiplicity(1, 1)),
        Property(name="Fragmentos_Fragmento6", type=Fragmentos_Fragmento, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Fragmentos",
    types={Fragmentos_Fragmento, Fragmentos_Aplicacion, Fragmentos_Fichero},
    associations={ficheros0, fragmentos1, fragmentosSelect3, sigFragmento7},
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