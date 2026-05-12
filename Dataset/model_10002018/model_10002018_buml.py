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
Millenium_Component = Class(name="Millenium_Component")
Millenium_Component1 = Class(name="Millenium_Component1")
Cliente_Actor = Class(name="Cliente_Actor")
Natural_Actor = Class(name="Natural_Actor")
Jur_dica_Actor = Class(name="Jur_dica_Actor")
Deoartamento_de_inventarios_y_suministros_DIS_Component = Class(name="Deoartamento_de_inventarios_y_suministros_DIS_Component")
Proveedores_Actor = Class(name="Proveedores_Actor")
Dependencias_Actor = Class(name="Dependencias_Actor")
Contabilidad_y_tesorer_a_Actor = Class(name="Contabilidad_y_tesorer_a_Actor")
Sistema_WEB_M_vil___Recepci_n_de_pedidos_Component = Class(name="Sistema_WEB_M_vil___Recepci_n_de_pedidos_Component")
Responsable_Inventario_Actor = Class(name="Responsable_Inventario_Actor")
Actor_Actor = Class(name="Actor_Actor")
OrdenesPedidos = Class(name="OrdenesPedidos")
Elementos = Class(name="Elementos")
Dependencias = Class(name="Dependencias")
Proveedor = Class(name="Proveedor")
Factura = Class(name="Factura")
SolicitudSuministro = Class(name="SolicitudSuministro")
Pedidos = Class(name="Pedidos")
Brindar_consultor_as_external = Class(name="Brindar_consultor_as_external")
Registrar_proveedores_external = Class(name="Registrar_proveedores_external")
Recibir_ordenes_de_suministros_external = Class(name="Recibir_ordenes_de_suministros_external")
Entregar_productos_external = Class(name="Entregar_productos_external")
Recibir_productos_o_pedidos_external = Class(name="Recibir_productos_o_pedidos_external")
Clasificar_producto_external = Class(name="Clasificar_producto_external")
Generar_ordenes_de_pedido_external = Class(name="Generar_ordenes_de_pedido_external")

# Millenium_Component class attributes and methods

# Millenium_Component1 class attributes and methods

# Cliente_Actor class attributes and methods

# Natural_Actor class attributes and methods

# Jur_dica_Actor class attributes and methods

# Deoartamento_de_inventarios_y_suministros_DIS_Component class attributes and methods

# Proveedores_Actor class attributes and methods

# Dependencias_Actor class attributes and methods

# Contabilidad_y_tesorer_a_Actor class attributes and methods

# Sistema_WEB_M_vil___Recepci_n_de_pedidos_Component class attributes and methods

# Responsable_Inventario_Actor class attributes and methods

# Actor_Actor class attributes and methods

# OrdenesPedidos class attributes and methods
OrdenesPedidos_codigo: Property = Property(name="codigo", type=StringType)
OrdenesPedidos_fecha: Property = Property(name="fecha", type=StringType)
OrdenesPedidos.attributes={OrdenesPedidos_codigo, OrdenesPedidos_fecha}

# Elementos class attributes and methods
Elementos_referencia: Property = Property(name="referencia", type=StringType)
Elementos_clasificacion: Property = Property(name="clasificacion", type=StringType)
Elementos.attributes={Elementos_clasificacion, Elementos_referencia}

# Dependencias class attributes and methods
Dependencias_codigo: Property = Property(name="codigo", type=StringType)
Dependencias_nombre: Property = Property(name="nombre", type=StringType)
Dependencias_responsable: Property = Property(name="responsable", type=StringType)
Dependencias.attributes={Dependencias_codigo, Dependencias_nombre, Dependencias_responsable}

# Proveedor class attributes and methods
Proveedor_nit: Property = Property(name="nit", type=StringType)
Proveedor_razonSocial: Property = Property(name="razonSocial", type=StringType)
Proveedor_direccion: Property = Property(name="direccion", type=StringType)
Proveedor_telefonos: Property = Property(name="telefonos", type=StringType)
Proveedor.attributes={Proveedor_razonSocial, Proveedor_telefonos, Proveedor_direccion, Proveedor_nit}

# Factura class attributes and methods
Factura_codigo: Property = Property(name="codigo", type=StringType)
Factura_fecha: Property = Property(name="fecha", type=StringType)
Factura.attributes={Factura_fecha, Factura_codigo}

# SolicitudSuministro class attributes and methods
SolicitudSuministro_codigo: Property = Property(name="codigo", type=StringType)
SolicitudSuministro_fecha: Property = Property(name="fecha", type=StringType)
SolicitudSuministro.attributes={SolicitudSuministro_fecha, SolicitudSuministro_codigo}

# Pedidos class attributes and methods
Pedidos_codigo: Property = Property(name="codigo", type=StringType)
Pedidos_fecha: Property = Property(name="fecha", type=StringType)
Pedidos.attributes={Pedidos_codigo, Pedidos_fecha}

# Brindar_consultor_as_external class attributes and methods

# Registrar_proveedores_external class attributes and methods

# Recibir_ordenes_de_suministros_external class attributes and methods

# Entregar_productos_external class attributes and methods

# Recibir_productos_o_pedidos_external class attributes and methods

# Clasificar_producto_external class attributes and methods

# Generar_ordenes_de_pedido_external class attributes and methods

# Relationships
Brindar_consultor_as_Actor: BinaryAssociation = BinaryAssociation(
    name="Brindar_consultor_as_Actor",
    ends={
        Property(name="brindar_consultor_as0", type=Brindar_consultor_as_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor1", type=Cliente_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registrar_proveedores_Proveedores: BinaryAssociation = BinaryAssociation(
    name="Registrar_proveedores_Proveedores",
    ends={
        Property(name="registrar_proveedores2", type=Registrar_proveedores_external, multiplicity=Multiplicity(0, 1)),
        Property(name="proveedores3", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Recibir_ordenes_de_suministros_Dependencias: BinaryAssociation = BinaryAssociation(
    name="Recibir_ordenes_de_suministros_Dependencias",
    ends={
        Property(name="recibir_ordenes_de_suministros4", type=Recibir_ordenes_de_suministros_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dependencias5", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Entregar_productos_Dependencias: BinaryAssociation = BinaryAssociation(
    name="Entregar_productos_Dependencias",
    ends={
        Property(name="entregar_productos6", type=Entregar_productos_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dependencias7", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Recibir_productos_o_pedidos: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Recibir_productos_o_pedidos",
    ends={
        Property(name="proveedores8", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_productos_o_pedidos9", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Recibir_productos_o_pedidos: BinaryAssociation = BinaryAssociation(
    name="Actor_Recibir_productos_o_pedidos",
    ends={
        Property(name="actor10", type=Contabilidad_y_tesorer_a_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_productos_o_pedidos11", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Clasificar_producto_Responsable_Inventario: BinaryAssociation = BinaryAssociation(
    name="Clasificar_producto_Responsable_Inventario",
    ends={
        Property(name="clasificar_producto12", type=Clasificar_producto_external, multiplicity=Multiplicity(0, 1)),
        Property(name="responsable_Inventario13", type=Responsable_Inventario_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Generar_ordenes_de_pedido_Actor: BinaryAssociation = BinaryAssociation(
    name="Generar_ordenes_de_pedido_Actor",
    ends={
        Property(name="generar_ordenes_de_pedido14", type=Generar_ordenes_de_pedido_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor15", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
es_enviado: BinaryAssociation = BinaryAssociation(
    name="es_enviado",
    ends={
        Property(name="ordenesPedidos16", type=OrdenesPedidos, multiplicity=Multiplicity(0, 9999)),
        Property(name="proveedor17", type=Proveedor, multiplicity=Multiplicity(1, 1))
    }
)
provee: BinaryAssociation = BinaryAssociation(
    name="provee",
    ends={
        Property(name="proveedor18", type=Proveedor, multiplicity=Multiplicity(1, 1)),
        Property(name="pedidos19", type=Pedidos, multiplicity=Multiplicity(0, 9999))
    }
)
conforma: BinaryAssociation = BinaryAssociation(
    name="conforma",
    ends={
        Property(name="ordenesPedidos20", type=OrdenesPedidos, multiplicity=Multiplicity(0, 9999)),
        Property(name="elementos21", type=Elementos, multiplicity=Multiplicity(0, 1))
    }
)
genera: BinaryAssociation = BinaryAssociation(
    name="genera",
    ends={
        Property(name="ordenesPedidos22", type=OrdenesPedidos, multiplicity=Multiplicity(0, 1)),
        Property(name="solicitudSuministro23", type=SolicitudSuministro, multiplicity=Multiplicity(1, 9999))
    }
)
relaciona: BinaryAssociation = BinaryAssociation(
    name="relaciona",
    ends={
        Property(name="solicitudSuministro24", type=SolicitudSuministro, multiplicity=Multiplicity(0, 9999)),
        Property(name="elementos25", type=Elementos, multiplicity=Multiplicity(1, 9999))
    }
)
realiza: BinaryAssociation = BinaryAssociation(
    name="realiza",
    ends={
        Property(name="solicitudSuministro26", type=SolicitudSuministro, multiplicity=Multiplicity(1, 9999)),
        Property(name="dependencias27", type=Dependencias, multiplicity=Multiplicity(1, 1))
    }
)
elabora: BinaryAssociation = BinaryAssociation(
    name="elabora",
    ends={
        Property(name="proveedor28", type=Proveedor, multiplicity=Multiplicity(1, 1)),
        Property(name="factura29", type=Factura, multiplicity=Multiplicity(0, 9999))
    }
)
Factura_Elementos: BinaryAssociation = BinaryAssociation(
    name="Factura_Elementos",
    ends={
        Property(name="factura30", type=Factura, multiplicity=Multiplicity(0, 9999)),
        Property(name="elementos31", type=Elementos, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_jnq9cG3dEeqhRdvvYtDJdw",
    types={Millenium_Component, Millenium_Component1, Cliente_Actor, Natural_Actor, Jur_dica_Actor, Deoartamento_de_inventarios_y_suministros_DIS_Component, Proveedores_Actor, Dependencias_Actor, Contabilidad_y_tesorer_a_Actor, Sistema_WEB_M_vil___Recepci_n_de_pedidos_Component, Responsable_Inventario_Actor, Actor_Actor, OrdenesPedidos, Elementos, Dependencias, Proveedor, Factura, SolicitudSuministro, Pedidos, Brindar_consultor_as_external, Registrar_proveedores_external, Recibir_ordenes_de_suministros_external, Entregar_productos_external, Recibir_productos_o_pedidos_external, Clasificar_producto_external, Generar_ordenes_de_pedido_external},
    associations={Brindar_consultor_as_Actor, Registrar_proveedores_Proveedores, Recibir_ordenes_de_suministros_Dependencias, Entregar_productos_Dependencias, Proveedores_Recibir_productos_o_pedidos, Actor_Recibir_productos_o_pedidos, Clasificar_producto_Responsable_Inventario, Generar_ordenes_de_pedido_Actor, es_enviado, provee, conforma, genera, relaciona, realiza, elabora, Factura_Elementos},
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