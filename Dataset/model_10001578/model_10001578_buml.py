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
Tienda = Class(name="Tienda")
producto = Class(name="producto")
_1 = Class(name="_1")
veterinaria = Class(name="veterinaria")
caninos = Class(name="caninos")
veterinaria1 = Class(name="veterinaria1")
caninos1 = Class(name="caninos1")
veterinaria2 = Class(name="veterinaria2")
caninos2 = Class(name="caninos2")
veterinaria3 = Class(name="veterinaria3")
caninos3 = Class(name="caninos3")

# Tienda class attributes and methods
Tienda_Tienda: Property = Property(name="Tienda", type=StringType)
Tienda_getProducto1: Property = Property(name="getProducto1", type=StringType)
Tienda_getProducto2: Property = Property(name="getProducto2", type=StringType)
Tienda_getProducto3: Property = Property(name="getProducto3", type=StringType)
Tienda_getProducto4: Property = Property(name="getProducto4", type=StringType)
Tienda.attributes={Tienda_getProducto3, Tienda_getProducto1, Tienda_getProducto2, Tienda_Tienda, Tienda_getProducto4}

# producto class attributes and methods
producto_IVA_DROGUERIA: Property = Property(name="IVA_DROGUERIA", type=StringType)
producto_nombre: Property = Property(name="nombre", type=StringType)
producto_tipo: Property = Property(name="tipo", type=StringType)
producto_cantidadBodega: Property = Property(name="cantidadBodega", type=StringType)
producto_cantidadMinima: Property = Property(name="cantidadMinima", type=StringType)
producto_cantidadVendida: Property = Property(name="cantidadVendida", type=StringType)
producto_precioVenta: Property = Property(name="precioVenta", type=StringType)
producto_PAPELERIA: Property = Property(name="PAPELERIA", type=StringType)
producto_SUPERMERCADO: Property = Property(name="SUPERMERCADO", type=StringType)
producto_DROGUERIA: Property = Property(name="DROGUERIA", type=StringType)
producto_IVA_PAPELERIA: Property = Property(name="IVA_PAPELERIA", type=StringType)
producto_IVA_SUPERMERCADO: Property = Property(name="IVA_SUPERMERCADO", type=StringType)
producto.attributes={producto_cantidadMinima, producto_IVA_PAPELERIA, producto_SUPERMERCADO, producto_nombre, producto_cantidadBodega, producto_IVA_SUPERMERCADO, producto_precioVenta, producto_cantidadVendida, producto_IVA_DROGUERIA, producto_PAPELERIA, producto_tipo, producto_DROGUERIA}

# _1 class attributes and methods

# veterinaria class attributes and methods

# caninos class attributes and methods
caninos_nombre: Property = Property(name="nombre", type=StringType)
caninos_raza: Property = Property(name="raza", type=StringType)
caninos_edad: Property = Property(name="edad", type=StringType)
caninos_peso: Property = Property(name="peso", type=StringType)
caninos_altura: Property = Property(name="altura", type=StringType)
caninos_observaciones: Property = Property(name="observaciones", type=StringType)
caninos.attributes={caninos_raza, caninos_edad, caninos_nombre, caninos_altura, caninos_observaciones, caninos_peso}

# veterinaria1 class attributes and methods

# caninos1 class attributes and methods
caninos1_nombre: Property = Property(name="nombre", type=StringType)
caninos1_raza: Property = Property(name="raza", type=StringType)
caninos1_edad: Property = Property(name="edad", type=StringType)
caninos1_peso: Property = Property(name="peso", type=StringType)
caninos1_altura: Property = Property(name="altura", type=StringType)
caninos1_obsercaciones: Property = Property(name="obsercaciones", type=StringType)
caninos1.attributes={caninos1_peso, caninos1_obsercaciones, caninos1_edad, caninos1_altura, caninos1_raza, caninos1_nombre}

# veterinaria2 class attributes and methods
veterinaria2__: Property = Property(name="_", type=StringType)
veterinaria2.attributes={veterinaria2__}

# caninos2 class attributes and methods
caninos2_nombre: Property = Property(name="nombre", type=StringType)
caninos2_raza: Property = Property(name="raza", type=StringType)
caninos2_edad: Property = Property(name="edad", type=StringType)
caninos2_peso: Property = Property(name="peso", type=StringType)
caninos2_altura: Property = Property(name="altura", type=StringType)
caninos2_observaciones: Property = Property(name="observaciones", type=StringType)
caninos2.attributes={caninos2_raza, caninos2_observaciones, caninos2_peso, caninos2_altura, caninos2_edad, caninos2_nombre}

# veterinaria3 class attributes and methods
veterinaria3__attr: Property = Property(name="_attr", type=StringType)
veterinaria3.attributes={veterinaria3__attr}

# caninos3 class attributes and methods
caninos3_nombre: Property = Property(name="nombre", type=StringType)
caninos3_raza: Property = Property(name="raza", type=StringType)
caninos3_edad: Property = Property(name="edad", type=StringType)
caninos3_peso: Property = Property(name="peso", type=StringType)
caninos3_altura: Property = Property(name="altura", type=StringType)
caninos3_observaciones: Property = Property(name="observaciones", type=StringType)
caninos3.attributes={caninos3_nombre, caninos3_edad, caninos3_altura, caninos3_raza, caninos3_peso, caninos3_observaciones}

# Relationships
producto_Tienda: BinaryAssociation = BinaryAssociation(
    name="producto_Tienda",
    ends={
        Property(name="tienda0", type=Tienda, multiplicity=Multiplicity(0, 1)),
        Property(name="producto21", type=producto, multiplicity=Multiplicity(1, 1))
    }
)
producto_Tienda2: BinaryAssociation = BinaryAssociation(
    name="producto_Tienda2",
    ends={
        Property(name="tienda2", type=Tienda, multiplicity=Multiplicity(0, 1)),
        Property(name="producto33", type=producto, multiplicity=Multiplicity(1, 1))
    }
)
producto_Tienda3: BinaryAssociation = BinaryAssociation(
    name="producto_Tienda3",
    ends={
        Property(name="tienda4", type=Tienda, multiplicity=Multiplicity(0, 1)),
        Property(name="producto15", type=producto, multiplicity=Multiplicity(1, 1))
    }
)
producto_Tienda4: BinaryAssociation = BinaryAssociation(
    name="producto_Tienda4",
    ends={
        Property(name="tienda6", type=Tienda, multiplicity=Multiplicity(0, 1)),
        Property(name="producto47", type=producto, multiplicity=Multiplicity(1, 1))
    }
)
veterinaria_caninos2: BinaryAssociation = BinaryAssociation(
    name="veterinaria_caninos2",
    ends={
        Property(name="Caninos8", type=caninos, multiplicity=Multiplicity(1, 1)),
        Property(name="veterinaria_caninos2_19", type=veterinaria, multiplicity=Multiplicity(0, 9999))
    }
)
veterinaria_caninos: BinaryAssociation = BinaryAssociation(
    name="veterinaria_caninos",
    ends={
        Property(name="caninos10", type=caninos1, multiplicity=Multiplicity(1, 1)),
        Property(name="veterinaria_caninos_111", type=veterinaria1, multiplicity=Multiplicity(0, 9999))
    }
)
veterinaria_caninos3: BinaryAssociation = BinaryAssociation(
    name="veterinaria_caninos3",
    ends={
        Property(name="caninos12", type=caninos2, multiplicity=Multiplicity(1, 1)),
        Property(name="veterinaria_caninos3_113", type=veterinaria2, multiplicity=Multiplicity(0, 9999))
    }
)
veterinaria_caninos4: BinaryAssociation = BinaryAssociation(
    name="veterinaria_caninos4",
    ends={
        Property(name="caninos14", type=caninos3, multiplicity=Multiplicity(1, 1)),
        Property(name="veterinaria_caninos4_115", type=veterinaria3, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_GlLV0Ga5Eem1gqqnDzZRVA",
    types={Tienda, producto, _1, veterinaria, caninos, veterinaria1, caninos1, veterinaria2, caninos2, veterinaria3, caninos3},
    associations={producto_Tienda, producto_Tienda2, producto_Tienda3, producto_Tienda4, veterinaria_caninos2, veterinaria_caninos, veterinaria_caninos3, veterinaria_caninos4},
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