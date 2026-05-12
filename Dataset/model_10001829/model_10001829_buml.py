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
int: Enumeration = Enumeration(
    name="int",
    literals={
            
    }
)

# Classes
Servicios = Class(name="Servicios")
Mascotas = Class(name="Mascotas")
Registro = Class(name="Registro")
Cliente = Class(name="Cliente")
Guacales = Class(name="Guacales")
Auxiliar = Class(name="Auxiliar")
Profesionales = Class(name="Profesionales")
Insumos = Class(name="Insumos")
Estados = Class(name="Estados")
Tipo_mascota = Class(name="Tipo_mascota")
Reporte = Class(name="Reporte")

# Servicios class attributes and methods
Servicios_id_servicio: Property = Property(name="id_servicio", type=IntegerType)
Servicios_Nombre_servicio: Property = Property(name="Nombre_servicio", type=StringType)
Servicios_Tiempo: Property = Property(name="Tiempo", type=IntegerType)
Servicios_Valor: Property = Property(name="Valor", type=IntegerType)
Servicios_Profesional: Property = Property(name="Profesional", type=Profesionales)
Servicios_Insumos: Property = Property(name="Insumos", type=Insumos)
Servicios.attributes={Servicios_Tiempo, Servicios_Profesional, Servicios_Insumos, Servicios_id_servicio, Servicios_Nombre_servicio, Servicios_Valor}

# Mascotas class attributes and methods
Mascotas_Id_mascota: Property = Property(name="Id_mascota", type=IntegerType)
Mascotas_tipo_mascota: Property = Property(name="tipo_mascota", type=Tipo_mascota)
Mascotas.attributes={Mascotas_tipo_mascota, Mascotas_Id_mascota}

# Registro class attributes and methods
Registro_Hora_entrada: Property = Property(name="Hora_entrada", type=StringType)
Registro_Hora_salida: Property = Property(name="Hora_salida", type=StringType)
Registro_Tipo_Mascota: Property = Property(name="Tipo_Mascota", type=Tipo_mascota)
Registro_Cliente: Property = Property(name="Cliente", type=Cliente)
Registro_Auxiliar: Property = Property(name="Auxiliar", type=Auxiliar)
Registro.attributes={Registro_Tipo_Mascota, Registro_Auxiliar, Registro_Hora_entrada, Registro_Hora_salida, Registro_Cliente}

# Cliente class attributes and methods
Cliente_C_dula: Property = Property(name="C_dula", type=StringType)
Cliente_Tel_fono: Property = Property(name="Tel_fono", type=IntegerType)
Cliente.attributes={Cliente_Tel_fono, Cliente_C_dula}

# Guacales class attributes and methods
Guacales_Id_guacal: Property = Property(name="Id_guacal", type=IntegerType)
Guacales.attributes={Guacales_Id_guacal}

# Auxiliar class attributes and methods
Auxiliar_Nombre_auxiliar: Property = Property(name="Nombre_auxiliar", type=StringType)
Auxiliar_Id_auxiliar: Property = Property(name="Id_auxiliar", type=StringType)
Auxiliar.attributes={Auxiliar_Id_auxiliar, Auxiliar_Nombre_auxiliar}

# Profesionales class attributes and methods
Profesionales_Nombre_profesional: Property = Property(name="Nombre_profesional", type=StringType)
Profesionales_id_profesional: Property = Property(name="id_profesional", type=IntegerType)
Profesionales.attributes={Profesionales_Nombre_profesional, Profesionales_id_profesional}

# Insumos class attributes and methods
Insumos_Nombre_insumo: Property = Property(name="Nombre_insumo", type=StringType)
Insumos_Id_insumo: Property = Property(name="Id_insumo", type=IntegerType)
Insumos.attributes={Insumos_Nombre_insumo, Insumos_Id_insumo}

# Estados class attributes and methods
Estados_Nombre_estados: Property = Property(name="Nombre_estados", type=StringType)
Estados_id_estados: Property = Property(name="id_estados", type=IntegerType)
Estados.attributes={Estados_id_estados, Estados_Nombre_estados}

# Tipo_mascota class attributes and methods
Tipo_mascota_Nombre_Tipo: Property = Property(name="Nombre_Tipo", type=StringType)
Tipo_mascota_id_Tipo_Mascota: Property = Property(name="id_Tipo_Mascota", type=IntegerType)
Tipo_mascota.attributes={Tipo_mascota_id_Tipo_Mascota, Tipo_mascota_Nombre_Tipo}

# Reporte class attributes and methods

# Relationships
Cliente_Mascotas: BinaryAssociation = BinaryAssociation(
    name="Cliente_Mascotas",
    ends={
        Property(name="mascotas14", type=Mascotas, multiplicity=Multiplicity(1, 9999)),
        Property(name="cliente15", type=Cliente, multiplicity=Multiplicity(1, 1))
    }
)
Tipo_mascota_Mascotas: BinaryAssociation = BinaryAssociation(
    name="Tipo_mascota_Mascotas",
    ends={
        Property(name="mascotas16", type=Mascotas, multiplicity=Multiplicity(1, 9999)),
        Property(name="tipo_mascota217", type=Tipo_mascota, multiplicity=Multiplicity(1, 1))
    }
)
Auxiliar_Registro: BinaryAssociation = BinaryAssociation(
    name="Auxiliar_Registro",
    ends={
        Property(name="registro18", type=Registro, multiplicity=Multiplicity(1, 9999)),
        Property(name="auxiliar19", type=Auxiliar, multiplicity=Multiplicity(1, 1))
    }
)
Reporte_Mascotas: BinaryAssociation = BinaryAssociation(
    name="Reporte_Mascotas",
    ends={
        Property(name="mascotas20", type=Mascotas, multiplicity=Multiplicity(1, 9999)),
        Property(name="reporte21", type=Reporte, multiplicity=Multiplicity(1, 9999))
    }
)
Reporte_Servicios: BinaryAssociation = BinaryAssociation(
    name="Reporte_Servicios",
    ends={
        Property(name="servicios22", type=Servicios, multiplicity=Multiplicity(1, 9999)),
        Property(name="reporte23", type=Reporte, multiplicity=Multiplicity(1, 9999))
    }
)
Servicios_Mascotas: BinaryAssociation = BinaryAssociation(
    name="Servicios_Mascotas",
    ends={
        Property(name="mascotas0", type=Mascotas, multiplicity=Multiplicity(1, 9999)),
        Property(name="servicios1", type=Servicios, multiplicity=Multiplicity(1, 9999))
    }
)
Servicios_Insumos: BinaryAssociation = BinaryAssociation(
    name="Servicios_Insumos",
    ends={
        Property(name="insumos2", type=Insumos, multiplicity=Multiplicity(1, 9999)),
        Property(name="servicios3", type=Servicios, multiplicity=Multiplicity(1, 1))
    }
)
Servicios_Profesionales: BinaryAssociation = BinaryAssociation(
    name="Servicios_Profesionales",
    ends={
        Property(name="profesionales4", type=Profesionales, multiplicity=Multiplicity(1, 1)),
        Property(name="servicios5", type=Servicios, multiplicity=Multiplicity(1, 1))
    }
)
Mascotas_Estados: BinaryAssociation = BinaryAssociation(
    name="Mascotas_Estados",
    ends={
        Property(name="estados6", type=Estados, multiplicity=Multiplicity(1, 1)),
        Property(name="mascotas7", type=Mascotas, multiplicity=Multiplicity(1, 1))
    }
)
Mascotas_Guacales: BinaryAssociation = BinaryAssociation(
    name="Mascotas_Guacales",
    ends={
        Property(name="guacales8", type=Guacales, multiplicity=Multiplicity(1, 1)),
        Property(name="mascotas9", type=Mascotas, multiplicity=Multiplicity(1, 1))
    }
)
Mascotas_Registro: BinaryAssociation = BinaryAssociation(
    name="Mascotas_Registro",
    ends={
        Property(name="registro10", type=Registro, multiplicity=Multiplicity(1, 9999)),
        Property(name="mascotas11", type=Mascotas, multiplicity=Multiplicity(1, 1))
    }
)
Cliente_Registro: BinaryAssociation = BinaryAssociation(
    name="Cliente_Registro",
    ends={
        Property(name="registro12", type=Registro, multiplicity=Multiplicity(1, 9999)),
        Property(name="cliente13", type=Cliente, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_YX3MIM_nEemalJMtXLKA2A",
    types={Servicios, Mascotas, Registro, Cliente, Guacales, Auxiliar, Profesionales, Insumos, Estados, Tipo_mascota, Reporte, int},
    associations={Cliente_Mascotas, Tipo_mascota_Mascotas, Auxiliar_Registro, Reporte_Mascotas, Reporte_Servicios, Servicios_Mascotas, Servicios_Insumos, Servicios_Profesionales, Mascotas_Estados, Mascotas_Guacales, Mascotas_Registro, Cliente_Registro},
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