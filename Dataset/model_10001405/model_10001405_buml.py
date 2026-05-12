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
mundo_Ave = Class(name="mundo_Ave")
mundo_Neornithe = Class(name="mundo_Neornithe")
mundo_Neognato = Class(name="mundo_Neognato")
mundo_Paleognato = Class(name="mundo_Paleognato")
mundo_Galloanserae = Class(name="mundo_Galloanserae")
mundo_Neoaves = Class(name="mundo_Neoaves")
mundo_Tinamues = Class(name="mundo_Tinamues")
mundo_Ratite = Class(name="mundo_Ratite")

# mundo_Ave class attributes and methods
mundo_Ave_color: Property = Property(name="color", type=StringType)
mundo_Ave_altura: Property = Property(name="altura", type=StringType)
mundo_Ave_factorPeso: Property = Property(name="factorPeso", type=StringType)
mundo_Ave.attributes={mundo_Ave_altura, mundo_Ave_factorPeso, mundo_Ave_color}

# mundo_Neornithe class attributes and methods
mundo_Neornithe_rangoMetabolico: Property = Property(name="rangoMetabolico", type=StringType)
mundo_Neornithe_ALTO: Property = Property(name="ALTO", type=StringType)
mundo_Neornithe_BAJO: Property = Property(name="BAJO", type=StringType)
mundo_Neornithe_MEDIO: Property = Property(name="MEDIO", type=StringType)
mundo_Neornithe_longitudCola: Property = Property(name="longitudCola", type=StringType)
mundo_Neornithe_densidadOsea: Property = Property(name="densidadOsea", type=StringType)
mundo_Neornithe.attributes={mundo_Neornithe_MEDIO, mundo_Neornithe_densidadOsea, mundo_Neornithe_longitudCola, mundo_Neornithe_BAJO, mundo_Neornithe_ALTO, mundo_Neornithe_rangoMetabolico}

# mundo_Neognato class attributes and methods
mundo_Neognato_numeroHuesosPata: Property = Property(name="numeroHuesosPata", type=StringType)
mundo_Neognato_longitudTercerDedo: Property = Property(name="longitudTercerDedo", type=StringType)
mundo_Neognato.attributes={mundo_Neognato_longitudTercerDedo, mundo_Neognato_numeroHuesosPata}

# mundo_Paleognato class attributes and methods
mundo_Paleognato_numeroHuesosPaladar: Property = Property(name="numeroHuesosPaladar", type=StringType)
mundo_Paleognato.attributes={mundo_Paleognato_numeroHuesosPaladar}

# mundo_Galloanserae class attributes and methods
mundo_Galloanserae_tipo: Property = Property(name="tipo", type=StringType)
mundo_Galloanserae_reproduccion: Property = Property(name="reproduccion", type=StringType)
mundo_Galloanserae_DOMESTICA: Property = Property(name="DOMESTICA", type=StringType)
mundo_Galloanserae_CAZA: Property = Property(name="CAZA", type=StringType)
mundo_Galloanserae_POLIGAMA: Property = Property(name="POLIGAMA", type=StringType)
mundo_Galloanserae_MONOGAMA: Property = Property(name="MONOGAMA", type=StringType)
mundo_Galloanserae.attributes={mundo_Galloanserae_tipo, mundo_Galloanserae_MONOGAMA, mundo_Galloanserae_CAZA, mundo_Galloanserae_POLIGAMA, mundo_Galloanserae_DOMESTICA, mundo_Galloanserae_reproduccion}

# mundo_Neoaves class attributes and methods
mundo_Neoaves_longitudPatas: Property = Property(name="longitudPatas", type=StringType)
mundo_Neoaves_numeroDedosPatas: Property = Property(name="numeroDedosPatas", type=StringType)
mundo_Neoaves.attributes={mundo_Neoaves_numeroDedosPatas, mundo_Neoaves_longitudPatas}

# mundo_Tinamues class attributes and methods
mundo_Tinamues_velocidadTierra: Property = Property(name="velocidadTierra", type=StringType)
mundo_Tinamues.attributes={mundo_Tinamues_velocidadTierra}

# mundo_Ratite class attributes and methods
mundo_Ratite_quilla: Property = Property(name="quilla", type=BooleanType)
mundo_Ratite.attributes={mundo_Ratite_quilla}

# Domain Model
domain_model = DomainModel(
    name="_4xf1kMiVEeeM1PgT03_3Vg",
    types={mundo_Ave, mundo_Neornithe, mundo_Neognato, mundo_Paleognato, mundo_Galloanserae, mundo_Neoaves, mundo_Tinamues, mundo_Ratite},
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