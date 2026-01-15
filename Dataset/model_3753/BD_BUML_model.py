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

# Enumerations
TipoPrimitivo: Enumeration = Enumeration(
    name="TipoPrimitivo",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Boolean")
    }
)

# Classes
BD_EsquemaBD = Class(name="BD::EsquemaBD")
BD_Tabla = Class(name="BD::Tabla")
BD_Columna = Class(name="BD::Columna")

# BD_EsquemaBD class attributes and methods

# BD_Tabla class attributes and methods
BD_Tabla_nombre: Property = Property(name="nombre", type=StringType)
BD_Tabla.attributes={BD_Tabla_nombre}

# BD_Columna class attributes and methods
BD_Columna_nombre: Property = Property(name="nombre", type=StringType)
BD_Columna_tipo: Property = Property(name="tipo", type=StringType)
BD_Columna.attributes={BD_Columna_nombre, BD_Columna_tipo}

# Relationships
tablas0: BinaryAssociation = BinaryAssociation(
    name="tablas0",
    ends={
        Property(name="BD_Tabla", type=BD_EsquemaBD, multiplicity=Multiplicity(1, 1)),
        Property(name="BD_EsquemaBD", type=BD_Tabla, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columnas1: BinaryAssociation = BinaryAssociation(
    name="columnas1",
    ends={
        Property(name="BD_Columna", type=BD_Tabla, multiplicity=Multiplicity(1, 1)),
        Property(name="BD_Tabla2", type=BD_Columna, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="BD",
    types={BD_EsquemaBD, BD_Tabla, BD_Columna, TipoPrimitivo},
    associations={tablas0, columnas1},
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