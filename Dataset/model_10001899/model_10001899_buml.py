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
ServidorBSD_Node = Class(name="ServidorBSD_Node")
Brindar_consultoria_external = Class(name="Brindar_consultoria_external")
Recibir_ordenes_de_suministro_external = Class(name="Recibir_ordenes_de_suministro_external")
Registrar_proveedores_external = Class(name="Registrar_proveedores_external")
Recibir_productos_o_pedidos_external = Class(name="Recibir_productos_o_pedidos_external")
Millenium_Component = Class(name="Millenium_Component")
Cliente_Actor = Class(name="Cliente_Actor")
Natural_Actor = Class(name="Natural_Actor")
Juridica_Actor = Class(name="Juridica_Actor")
Departamento_de_Inventarios_y_Suministros_DIS_Component = Class(name="Departamento_de_Inventarios_y_Suministros_DIS_Component")
Proveedores_Actor = Class(name="Proveedores_Actor")
Dependencia_Actor = Class(name="Dependencia_Actor")
Contabilidad_y_Tesoreria_Actor = Class(name="Contabilidad_y_Tesoreria_Actor")
Sistema_WEB_Movil___Recepcion_de_Pedidos_Component = Class(name="Sistema_WEB_Movil___Recepcion_de_Pedidos_Component")
Responsable_Inventario_Actor = Class(name="Responsable_Inventario_Actor")
Ordenes_Pedidos = Class(name="Ordenes_Pedidos")
Proveedor = Class(name="Proveedor")
Dependencia = Class(name="Dependencia")
Factura = Class(name="Factura")
Solicitud_Suministros = Class(name="Solicitud_Suministros")
Pedidos = Class(name="Pedidos")
Elementos = Class(name="Elementos")
Servidor_intel_I8_Node = Class(name="Servidor_intel_I8_Node")
Persistencia_Factura_Component = Class(name="Persistencia_Factura_Component")
LogicaPresentacion_Factura_Component = Class(name="LogicaPresentacion_Factura_Component")
ServidorWEB_Node = Class(name="ServidorWEB_Node")
Entregar_productos_external = Class(name="Entregar_productos_external")
Clasificar_Producto_external = Class(name="Clasificar_Producto_external")

# ServidorBSD_Node class attributes and methods

# Brindar_consultoria_external class attributes and methods

# Recibir_ordenes_de_suministro_external class attributes and methods

# Registrar_proveedores_external class attributes and methods

# Recibir_productos_o_pedidos_external class attributes and methods

# Millenium_Component class attributes and methods

# Cliente_Actor class attributes and methods

# Natural_Actor class attributes and methods

# Juridica_Actor class attributes and methods

# Departamento_de_Inventarios_y_Suministros_DIS_Component class attributes and methods

# Proveedores_Actor class attributes and methods

# Dependencia_Actor class attributes and methods

# Contabilidad_y_Tesoreria_Actor class attributes and methods

# Sistema_WEB_Movil___Recepcion_de_Pedidos_Component class attributes and methods

# Responsable_Inventario_Actor class attributes and methods

# Ordenes_Pedidos class attributes and methods
Ordenes_Pedidos_codigo: Property = Property(name="codigo", type=StringType)
Ordenes_Pedidos_fecha: Property = Property(name="fecha", type=StringType)
Ordenes_Pedidos.attributes={Ordenes_Pedidos_fecha, Ordenes_Pedidos_codigo}

# Proveedor class attributes and methods
Proveedor_nit: Property = Property(name="nit", type=StringType)
Proveedor_razonSocial: Property = Property(name="razonSocial", type=StringType)
Proveedor_direccion: Property = Property(name="direccion", type=StringType)
Proveedor_telefonos: Property = Property(name="telefonos", type=StringType)
Proveedor.attributes={Proveedor_telefonos, Proveedor_razonSocial, Proveedor_nit, Proveedor_direccion}

# Dependencia class attributes and methods
Dependencia_codigo: Property = Property(name="codigo", type=StringType)
Dependencia_nombre: Property = Property(name="nombre", type=StringType)
Dependencia_responsable: Property = Property(name="responsable", type=StringType)
Dependencia.attributes={Dependencia_nombre, Dependencia_codigo, Dependencia_responsable}

# Factura class attributes and methods
Factura_codigo: Property = Property(name="codigo", type=StringType)
Factura_fecha: Property = Property(name="fecha", type=StringType)
Factura.attributes={Factura_fecha, Factura_codigo}

# Solicitud_Suministros class attributes and methods
Solicitud_Suministros_codigo: Property = Property(name="codigo", type=StringType)
Solicitud_Suministros_fecha: Property = Property(name="fecha", type=StringType)
Solicitud_Suministros.attributes={Solicitud_Suministros_codigo, Solicitud_Suministros_fecha}

# Pedidos class attributes and methods
Pedidos_codigo: Property = Property(name="codigo", type=StringType)
Pedidos_fecha: Property = Property(name="fecha", type=StringType)
Pedidos.attributes={Pedidos_codigo, Pedidos_fecha}

# Elementos class attributes and methods
Elementos_referencia: Property = Property(name="referencia", type=StringType)
Elementos_clasificacion: Property = Property(name="clasificacion", type=StringType)
Elementos.attributes={Elementos_clasificacion, Elementos_referencia}

# Servidor_intel_I8_Node class attributes and methods

# Persistencia_Factura_Component class attributes and methods

# LogicaPresentacion_Factura_Component class attributes and methods

# ServidorWEB_Node class attributes and methods

# Entregar_productos_external class attributes and methods

# Clasificar_Producto_external class attributes and methods

# Relationships
Cliente_Brindar_consultoria: BinaryAssociation = BinaryAssociation(
    name="Cliente_Brindar_consultoria",
    ends={
        Property(name="cliente0", type=Cliente_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="brindar_consultoria1", type=Brindar_consultoria_external, multiplicity=Multiplicity(0, 1))
    }
)
UseCase_Dependencia: BinaryAssociation = BinaryAssociation(
    name="UseCase_Dependencia",
    ends={
        Property(name="useCase2", type=Recibir_ordenes_de_suministro_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dependencia3", type=Dependencia_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registrar_proveedores_Contabilidad_y_Tesoreria: BinaryAssociation = BinaryAssociation(
    name="Registrar_proveedores_Contabilidad_y_Tesoreria",
    ends={
        Property(name="registrar_proveedores4", type=Registrar_proveedores_external, multiplicity=Multiplicity(0, 1)),
        Property(name="contabilidad_y_Tesoreria5", type=Contabilidad_y_Tesoreria_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Registrar_proveedores: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Registrar_proveedores",
    ends={
        Property(name="proveedores6", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_proveedores7", type=Registrar_proveedores_external, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Proveedores_UseCase2",
    ends={
        Property(name="proveedores8", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase29", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencia_Entregar_productos: BinaryAssociation = BinaryAssociation(
    name="Dependencia_Entregar_productos",
    ends={
        Property(name="dependencia10", type=Dependencia_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="entregar_productos11", type=Entregar_productos_external, multiplicity=Multiplicity(0, 1))
    }
)
Responsable_Inventario_Clasificar_Producto: BinaryAssociation = BinaryAssociation(
    name="Responsable_Inventario_Clasificar_Producto",
    ends={
        Property(name="responsable_Inventario12", type=Responsable_Inventario_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="clasificar_Producto13", type=Clasificar_Producto_external, multiplicity=Multiplicity(0, 1))
    }
)
Ordenes_Pedidos_Proveedor: BinaryAssociation = BinaryAssociation(
    name="Ordenes_Pedidos_Proveedor",
    ends={
        Property(name="ordenes_Pedidos14", type=Ordenes_Pedidos, multiplicity=Multiplicity(0, 9999)),
        Property(name="proveedor15", type=Proveedor, multiplicity=Multiplicity(0, 1))
    }
)
Proveedor_Pedidos: BinaryAssociation = BinaryAssociation(
    name="Proveedor_Pedidos",
    ends={
        Property(name="proveedor16", type=Proveedor, multiplicity=Multiplicity(1, 1)),
        Property(name="pedidos17", type=Pedidos, multiplicity=Multiplicity(0, 9999))
    }
)
Ordenes_Pedidos_Elementos: BinaryAssociation = BinaryAssociation(
    name="Ordenes_Pedidos_Elementos",
    ends={
        Property(name="ordenes_Pedidos18", type=Ordenes_Pedidos, multiplicity=Multiplicity(0, 9999)),
        Property(name="elementos19", type=Elementos, multiplicity=Multiplicity(1, 9999))
    }
)
Elementos_Solicitud_Suministros: BinaryAssociation = BinaryAssociation(
    name="Elementos_Solicitud_Suministros",
    ends={
        Property(name="elementos20", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="solicitud_Suministros21", type=Solicitud_Suministros, multiplicity=Multiplicity(0, 9999))
    }
)
Solicitud_Suministros_Ordenes_Pedidos: BinaryAssociation = BinaryAssociation(
    name="Solicitud_Suministros_Ordenes_Pedidos",
    ends={
        Property(name="solicitud_Suministros22", type=Solicitud_Suministros, multiplicity=Multiplicity(1, 9999)),
        Property(name="ordenes_Pedidos23", type=Ordenes_Pedidos, multiplicity=Multiplicity(0, 1))
    }
)
Dependencia_Solicitud_Suministros: BinaryAssociation = BinaryAssociation(
    name="Dependencia_Solicitud_Suministros",
    ends={
        Property(name="dependencia24", type=Dependencia, multiplicity=Multiplicity(1, 1)),
        Property(name="solicitud_Suministros25", type=Solicitud_Suministros, multiplicity=Multiplicity(1, 9999))
    }
)
Elementos_Factura: BinaryAssociation = BinaryAssociation(
    name="Elementos_Factura",
    ends={
        Property(name="elementos26", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="factura27", type=Factura, multiplicity=Multiplicity(0, 9999))
    }
)
Proveedor_Factura: BinaryAssociation = BinaryAssociation(
    name="Proveedor_Factura",
    ends={
        Property(name="proveedor28", type=Proveedor, multiplicity=Multiplicity(0, 1)),
        Property(name="factura29", type=Factura, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_cB5e4G3dEeqhRdvvYtDJdw",
    types={ServidorBSD_Node, Brindar_consultoria_external, Recibir_ordenes_de_suministro_external, Registrar_proveedores_external, Recibir_productos_o_pedidos_external, Millenium_Component, Cliente_Actor, Natural_Actor, Juridica_Actor, Departamento_de_Inventarios_y_Suministros_DIS_Component, Proveedores_Actor, Dependencia_Actor, Contabilidad_y_Tesoreria_Actor, Sistema_WEB_Movil___Recepcion_de_Pedidos_Component, Responsable_Inventario_Actor, Ordenes_Pedidos, Proveedor, Dependencia, Factura, Solicitud_Suministros, Pedidos, Elementos, Servidor_intel_I8_Node, Persistencia_Factura_Component, LogicaPresentacion_Factura_Component, ServidorWEB_Node, Entregar_productos_external, Clasificar_Producto_external},
    associations={Cliente_Brindar_consultoria, UseCase_Dependencia, Registrar_proveedores_Contabilidad_y_Tesoreria, Proveedores_Registrar_proveedores, Proveedores_UseCase2, Dependencia_Entregar_productos, Responsable_Inventario_Clasificar_Producto, Ordenes_Pedidos_Proveedor, Proveedor_Pedidos, Ordenes_Pedidos_Elementos, Elementos_Solicitud_Suministros, Solicitud_Suministros_Ordenes_Pedidos, Dependencia_Solicitud_Suministros, Elementos_Factura, Proveedor_Factura},
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