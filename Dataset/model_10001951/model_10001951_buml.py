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
Cliente_Actor = Class(name="Cliente_Actor")
Natural_Actor = Class(name="Natural_Actor")
Juridica_Actor = Class(name="Juridica_Actor")
Departamento_de_Inventarios_y_Suministros_Dis_Component = Class(name="Departamento_de_Inventarios_y_Suministros_Dis_Component")
Proveedores_Actor = Class(name="Proveedores_Actor")
Dependencias_Actor = Class(name="Dependencias_Actor")
Contabilidad_y_tesoreria_Actor = Class(name="Contabilidad_y_tesoreria_Actor")
Sistema_Web_Movil___Reccepci_n_de_pedidos_Component = Class(name="Sistema_Web_Movil___Reccepci_n_de_pedidos_Component")
Responsable_inventario_Actor = Class(name="Responsable_inventario_Actor")
OrdenesPedidos = Class(name="OrdenesPedidos")
Proveedor = Class(name="Proveedor")
Factura = Class(name="Factura")
Elementos = Class(name="Elementos")
SolicitudSuministros = Class(name="SolicitudSuministros")
dependencia = Class(name="dependencia")
Pedidos = Class(name="Pedidos")
Brindar_Consultorias_external = Class(name="Brindar_Consultorias_external")
Recibir_productos_o_pedidos_external = Class(name="Recibir_productos_o_pedidos_external")
Registrar_proveedores_external = Class(name="Registrar_proveedores_external")
Recibir_ordenes_de_suministros_external = Class(name="Recibir_ordenes_de_suministros_external")
Entregar_productos_external = Class(name="Entregar_productos_external")
Clasificar_producto_external = Class(name="Clasificar_producto_external")
Revisi_n_de_factura_external = Class(name="Revisi_n_de_factura_external")

# Millenium_Component class attributes and methods

# Cliente_Actor class attributes and methods

# Natural_Actor class attributes and methods

# Juridica_Actor class attributes and methods

# Departamento_de_Inventarios_y_Suministros_Dis_Component class attributes and methods

# Proveedores_Actor class attributes and methods

# Dependencias_Actor class attributes and methods

# Contabilidad_y_tesoreria_Actor class attributes and methods

# Sistema_Web_Movil___Reccepci_n_de_pedidos_Component class attributes and methods

# Responsable_inventario_Actor class attributes and methods

# OrdenesPedidos class attributes and methods
OrdenesPedidos_codigo: Property = Property(name="codigo", type=StringType)
OrdenesPedidos_fecha: Property = Property(name="fecha", type=StringType)
OrdenesPedidos.attributes={OrdenesPedidos_fecha, OrdenesPedidos_codigo}

# Proveedor class attributes and methods
Proveedor_nit: Property = Property(name="nit", type=StringType)
Proveedor_nombre: Property = Property(name="nombre", type=StringType)
Proveedor_direccion: Property = Property(name="direccion", type=StringType)
Proveedor_telefono: Property = Property(name="telefono", type=StringType)
Proveedor.attributes={Proveedor_telefono, Proveedor_nombre, Proveedor_nit, Proveedor_direccion}

# Factura class attributes and methods
Factura_codigo: Property = Property(name="codigo", type=StringType)
Factura_fecha: Property = Property(name="fecha", type=StringType)
Factura.attributes={Factura_codigo, Factura_fecha}

# Elementos class attributes and methods
Elementos_referencia: Property = Property(name="referencia", type=StringType)
Elementos_clasificacion: Property = Property(name="clasificacion", type=StringType)
Elementos.attributes={Elementos_clasificacion, Elementos_referencia}

# SolicitudSuministros class attributes and methods
SolicitudSuministros_codigo: Property = Property(name="codigo", type=StringType)
SolicitudSuministros_fecha: Property = Property(name="fecha", type=StringType)
SolicitudSuministros.attributes={SolicitudSuministros_codigo, SolicitudSuministros_fecha}

# dependencia class attributes and methods
dependencia_codigo: Property = Property(name="codigo", type=StringType)
dependencia_nombre: Property = Property(name="nombre", type=StringType)
dependencia_responsable: Property = Property(name="responsable", type=StringType)
dependencia.attributes={dependencia_nombre, dependencia_responsable, dependencia_codigo}

# Pedidos class attributes and methods
Pedidos_codigo: Property = Property(name="codigo", type=StringType)
Pedidos_fecha: Property = Property(name="fecha", type=StringType)
Pedidos.attributes={Pedidos_fecha, Pedidos_codigo}

# Brindar_Consultorias_external class attributes and methods

# Recibir_productos_o_pedidos_external class attributes and methods

# Registrar_proveedores_external class attributes and methods

# Recibir_ordenes_de_suministros_external class attributes and methods

# Entregar_productos_external class attributes and methods

# Clasificar_producto_external class attributes and methods

# Revisi_n_de_factura_external class attributes and methods

# Relationships
Cliente_Brindar_Consultorias: BinaryAssociation = BinaryAssociation(
    name="Cliente_Brindar_Consultorias",
    ends={
        Property(name="cliente0", type=Cliente_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="brindar_Consultorias1", type=Brindar_Consultorias_external, multiplicity=Multiplicity(0, 1))
    }
)
Recibir_productos_o_pedidos_Actor: BinaryAssociation = BinaryAssociation(
    name="Recibir_productos_o_pedidos_Actor",
    ends={
        Property(name="recibir_productos_o_pedidos2", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor3", type=Contabilidad_y_tesoreria_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Registrar_proveedores: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Registrar_proveedores",
    ends={
        Property(name="proveedores4", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_proveedores5", type=Registrar_proveedores_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencias_Recibir_ordenes_de_suministros: BinaryAssociation = BinaryAssociation(
    name="Dependencias_Recibir_ordenes_de_suministros",
    ends={
        Property(name="dependencias8", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_ordenes_de_suministros9", type=Recibir_ordenes_de_suministros_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencias_Entregar_productos: BinaryAssociation = BinaryAssociation(
    name="Dependencias_Entregar_productos",
    ends={
        Property(name="dependencias10", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="entregar_productos11", type=Entregar_productos_external, multiplicity=Multiplicity(0, 1))
    }
)
Responsable_inventario_Clasificar_roducto: BinaryAssociation = BinaryAssociation(
    name="Responsable_inventario_Clasificar_roducto",
    ends={
        Property(name="responsable_inventario12", type=Responsable_inventario_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="clasificar_roducto13", type=Clasificar_producto_external, multiplicity=Multiplicity(0, 1))
    }
)
Responsable_inventario_Revisi_n_de_factura: BinaryAssociation = BinaryAssociation(
    name="Responsable_inventario_Revisi_n_de_factura",
    ends={
        Property(name="responsable_inventario14", type=Responsable_inventario_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="revisi_n_de_factura15", type=Revisi_n_de_factura_external, multiplicity=Multiplicity(0, 1))
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
        Property(name="elementos20", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="ordenesPedidos21", type=OrdenesPedidos, multiplicity=Multiplicity(0, 9999))
    }
)
relaciona: BinaryAssociation = BinaryAssociation(
    name="relaciona",
    ends={
        Property(name="elementos22", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="solicitudSuministros23", type=SolicitudSuministros, multiplicity=Multiplicity(0, 9999))
    }
)
genera: BinaryAssociation = BinaryAssociation(
    name="genera",
    ends={
        Property(name="ordenesPedidos24", type=OrdenesPedidos, multiplicity=Multiplicity(0, 1)),
        Property(name="solicitudSuministros25", type=SolicitudSuministros, multiplicity=Multiplicity(1, 9999))
    }
)
Proveedores_Recibir_productos_o_pedidos: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Recibir_productos_o_pedidos",
    ends={
        Property(name="proveedores6", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_productos_o_pedidos7", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
elabora: BinaryAssociation = BinaryAssociation(
    name="elabora",
    ends={
        Property(name="proveedor28", type=Proveedor, multiplicity=Multiplicity(1, 1)),
        Property(name="factura29", type=Factura, multiplicity=Multiplicity(0, 9999))
    }
)
factura: BinaryAssociation = BinaryAssociation(
    name="factura",
    ends={
        Property(name="elementos30", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="factura31", type=Factura, multiplicity=Multiplicity(0, 9999))
    }
)
realiza: BinaryAssociation = BinaryAssociation(
    name="realiza",
    ends={
        Property(name="solicitudSuministros26", type=SolicitudSuministros, multiplicity=Multiplicity(1, 9999)),
        Property(name="dependencia27", type=dependencia, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_fMJ0YG3dEeqhRdvvYtDJdw",
    types={Millenium_Component, Cliente_Actor, Natural_Actor, Juridica_Actor, Departamento_de_Inventarios_y_Suministros_Dis_Component, Proveedores_Actor, Dependencias_Actor, Contabilidad_y_tesoreria_Actor, Sistema_Web_Movil___Reccepci_n_de_pedidos_Component, Responsable_inventario_Actor, OrdenesPedidos, Proveedor, Factura, Elementos, SolicitudSuministros, dependencia, Pedidos, Brindar_Consultorias_external, Recibir_productos_o_pedidos_external, Registrar_proveedores_external, Recibir_ordenes_de_suministros_external, Entregar_productos_external, Clasificar_producto_external, Revisi_n_de_factura_external},
    associations={Cliente_Brindar_Consultorias, Recibir_productos_o_pedidos_Actor, Proveedores_Registrar_proveedores, Dependencias_Recibir_ordenes_de_suministros, Dependencias_Entregar_productos, Responsable_inventario_Clasificar_roducto, Responsable_inventario_Revisi_n_de_factura, es_enviado, provee, conforma, relaciona, genera, Proveedores_Recibir_productos_o_pedidos, elabora, factura, realiza},
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