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
Selects_NamedElement = Class(name="Selects::NamedElement", is_abstract=True)
Selects_Aplicacion = Class(name="Selects::Aplicacion")
Selects_Fichero = Class(name="Selects::Fichero")
NamedElement = Class(name="NamedElement")
Selects_Select = Class(name="Selects::Select")
Selects_From = Class(name="Selects::From")
Selects_Where = Class(name="Selects::Where")
Selects_Tabla = Class(name="Selects::Tabla")
Selects_Join = Class(name="Selects::Join")
Selects_Operando = Class(name="Selects::Operando")

# Selects_NamedElement class attributes and methods
Selects_NamedElement_nombre: Property = Property(name="nombre", type=StringType)
Selects_NamedElement.attributes={Selects_NamedElement_nombre}

# Selects_Aplicacion class attributes and methods

# Selects_Fichero class attributes and methods

# NamedElement class attributes and methods

# Selects_Select class attributes and methods

# Selects_From class attributes and methods

# Selects_Where class attributes and methods

# Selects_Tabla class attributes and methods
Selects_Tabla_tabAlias: Property = Property(name="tabAlias", type=StringType)
Selects_Tabla.attributes={Selects_Tabla_tabAlias}

# Selects_Join class attributes and methods

# Selects_Operando class attributes and methods
Selects_Operando_columna: Property = Property(name="columna", type=StringType)
Selects_Operando_tabla: Property = Property(name="tabla", type=StringType)
Selects_Operando.attributes={Selects_Operando_tabla, Selects_Operando_columna}

# Relationships
ficheros0: BinaryAssociation = BinaryAssociation(
    name="ficheros0",
    ends={
        Property(name="Selects_Fichero", type=Selects_Aplicacion, multiplicity=Multiplicity(1, 1)),
        Property(name="Selects_Aplicacion", type=Selects_Fichero, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selects1: BinaryAssociation = BinaryAssociation(
    name="selects1",
    ends={
        Property(name="Selects_Select", type=Selects_Fichero, multiplicity=Multiplicity(1, 1)),
        Property(name="Selects_Fichero2", type=Selects_Select, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parte_from3: BinaryAssociation = BinaryAssociation(
    name="parte_from3",
    ends={
        Property(name="Selects_From", type=Selects_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="Selects_Select4", type=Selects_From, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parte_where5: BinaryAssociation = BinaryAssociation(
    name="parte_where5",
    ends={
        Property(name="Selects_Where", type=Selects_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="Selects_Select6", type=Selects_Where, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tablas7: BinaryAssociation = BinaryAssociation(
    name="tablas7",
    ends={
        Property(name="Selects_Tabla", type=Selects_From, multiplicity=Multiplicity(1, 1)),
        Property(name="Selects_From8", type=Selects_Tabla, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
joins9: BinaryAssociation = BinaryAssociation(
    name="joins9",
    ends={
        Property(name="Selects_Join", type=Selects_Where, multiplicity=Multiplicity(1, 1)),
        Property(name="Selects_Where10", type=Selects_Join, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operando111: BinaryAssociation = BinaryAssociation(
    name="operando111",
    ends={
        Property(name="Selects_Operando", type=Selects_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="Selects_Join12", type=Selects_Operando, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operando213: BinaryAssociation = BinaryAssociation(
    name="operando213",
    ends={
        Property(name="Selects_Operando15", type=Selects_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="Selects_Join14", type=Selects_Operando, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Selects_Fichero_NamedElement = Generalization(general=NamedElement, specific=Selects_Fichero)
gen_Selects_Tabla_NamedElement = Generalization(general=NamedElement, specific=Selects_Tabla)

# Domain Model
domain_model = DomainModel(
    name="Selects",
    types={Selects_NamedElement, Selects_Aplicacion, Selects_Fichero, NamedElement, Selects_Select, Selects_From, Selects_Where, Selects_Tabla, Selects_Join, Selects_Operando},
    associations={ficheros0, selects1, parte_from3, parte_where5, tablas7, joins9, operando111, operando213},
    generalizations={gen_Selects_Fichero_NamedElement, gen_Selects_Tabla_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)