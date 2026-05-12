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
Proveedores_Actor = Class(name="Proveedores_Actor")
Dependencias_Actor = Class(name="Dependencias_Actor")
Departamento_de_Inventario_y_Suministros_DIS_Component = Class(name="Departamento_de_Inventario_y_Suministros_DIS_Component")
Contabilidad_y_Tesoreria_Actor = Class(name="Contabilidad_y_Tesoreria_Actor")
Servicio_WEB_Movil___Recepcion_de_pedidos_Component = Class(name="Servicio_WEB_Movil___Recepcion_de_pedidos_Component")
Responsable_de_inventario_Actor = Class(name="Responsable_de_inventario_Actor")
OrdenesPedidos = Class(name="OrdenesPedidos")
Proveedor = Class(name="Proveedor")
Elementos = Class(name="Elementos")
Factura = Class(name="Factura")
SolicitudSuministro = Class(name="SolicitudSuministro")
Dependencia = Class(name="Dependencia")
Trabajador = Class(name="Trabajador")
Pedidos = Class(name="Pedidos")
Informe = Class(name="Informe")
Fabricacion = Class(name="Fabricacion")
Distribucion = Class(name="Distribucion")
VentaCalzado = Class(name="VentaCalzado")
EmpresasFiliales = Class(name="EmpresasFiliales")
Servidor_Intel_i8_Node = Class(name="Servidor_Intel_i8_Node")
logicaPresentacionFactura_Component = Class(name="logicaPresentacionFactura_Component")
persistenciaFactura_Component = Class(name="persistenciaFactura_Component")
ServidorWEB_Node = Class(name="ServidorWEB_Node")
ServidorBD_Node = Class(name="ServidorBD_Node")
Cliente2_Actor = Class(name="Cliente2_Actor")
Clientes_Actor = Class(name="Clientes_Actor")
Calcular_Actor = Class(name="Calcular_Actor")
Calcular = Class(name="Calcular")
Clientes = Class(name="Clientes")
Venta = Class(name="Venta")
Producto = Class(name="Producto")
Impuesto = Class(name="Impuesto")
Principal = Class(name="Principal")
Brindar_consultorias_external = Class(name="Brindar_consultorias_external")
Registrar_proveedores_external = Class(name="Registrar_proveedores_external")
Recibir_productos_o_pedidos_external = Class(name="Recibir_productos_o_pedidos_external")
Recibir_ordenes_de_suministro_external = Class(name="Recibir_ordenes_de_suministro_external")
Entregar_productos_external = Class(name="Entregar_productos_external")
Clasificar_producto_external = Class(name="Clasificar_producto_external")

# Millenium_Component class attributes and methods

# Cliente_Actor class attributes and methods

# Natural_Actor class attributes and methods

# Juridica_Actor class attributes and methods

# Proveedores_Actor class attributes and methods

# Dependencias_Actor class attributes and methods

# Departamento_de_Inventario_y_Suministros_DIS_Component class attributes and methods

# Contabilidad_y_Tesoreria_Actor class attributes and methods

# Servicio_WEB_Movil___Recepcion_de_pedidos_Component class attributes and methods

# Responsable_de_inventario_Actor class attributes and methods

# OrdenesPedidos class attributes and methods
OrdenesPedidos_codigo: Property = Property(name="codigo", type=StringType)
OrdenesPedidos_fecha: Property = Property(name="fecha", type=StringType)
OrdenesPedidos.attributes={OrdenesPedidos_codigo, OrdenesPedidos_fecha}

# Proveedor class attributes and methods
Proveedor_nit: Property = Property(name="nit", type=StringType)
Proveedor_razonSocial: Property = Property(name="razonSocial", type=StringType)
Proveedor_direccion: Property = Property(name="direccion", type=StringType)
Proveedor_telefono: Property = Property(name="telefono", type=StringType)
Proveedor.attributes={Proveedor_direccion, Proveedor_telefono, Proveedor_nit, Proveedor_razonSocial}

# Elementos class attributes and methods
Elementos_referencia: Property = Property(name="referencia", type=StringType)
Elementos_clasificacion: Property = Property(name="clasificacion", type=StringType)
Elementos.attributes={Elementos_referencia, Elementos_clasificacion}

# Factura class attributes and methods
Factura_codigo: Property = Property(name="codigo", type=StringType)
Factura_fecha: Property = Property(name="fecha", type=StringType)
Factura.attributes={Factura_fecha, Factura_codigo}

# SolicitudSuministro class attributes and methods
SolicitudSuministro_codigo: Property = Property(name="codigo", type=StringType)
SolicitudSuministro_fecha: Property = Property(name="fecha", type=StringType)
SolicitudSuministro.attributes={SolicitudSuministro_fecha, SolicitudSuministro_codigo}

# Dependencia class attributes and methods
Dependencia_codigo: Property = Property(name="codigo", type=StringType)
Dependencia_nombre: Property = Property(name="nombre", type=StringType)
Dependencia_responsable: Property = Property(name="responsable", type=StringType)
Dependencia.attributes={Dependencia_nombre, Dependencia_codigo, Dependencia_responsable}

# Trabajador class attributes and methods
Trabajador_DNI: Property = Property(name="DNI", type=IntegerType)
Trabajador_nombre: Property = Property(name="nombre", type=StringType)
Trabajador_HrsTrabajadasMes: Property = Property(name="HrsTrabajadasMes", type=IntegerType)
Trabajador_Sueldo: Property = Property(name="Sueldo", type=IntegerType)
Trabajador.attributes={Trabajador_DNI, Trabajador_nombre, Trabajador_HrsTrabajadasMes, Trabajador_Sueldo}

# Pedidos class attributes and methods
Pedidos_codigo: Property = Property(name="codigo", type=StringType)
Pedidos_fecha: Property = Property(name="fecha", type=StringType)
Pedidos.attributes={Pedidos_fecha, Pedidos_codigo}

# Informe class attributes and methods
Informe_codigo: Property = Property(name="codigo", type=IntegerType)
Informe_nombreTrabajador: Property = Property(name="nombreTrabajador", type=StringType)
Informe_FilialesTrabajados: Property = Property(name="FilialesTrabajados", type=StringType)
Informe_mesesTrabajadosFiliales: Property = Property(name="mesesTrabajadosFiliales", type=IntegerType)
Informe_HrsExtrasFiliales: Property = Property(name="HrsExtrasFiliales", type=StringType)
Informe_HrsTrabajadas: Property = Property(name="HrsTrabajadas", type=IntegerType)
Informe.attributes={Informe_mesesTrabajadosFiliales, Informe_nombreTrabajador, Informe_codigo, Informe_HrsTrabajadas, Informe_HrsExtrasFiliales, Informe_FilialesTrabajados}

# Fabricacion class attributes and methods
Fabricacion_codigo: Property = Property(name="codigo", type=IntegerType)
Fabricacion_razonSocial: Property = Property(name="razonSocial", type=StringType)
Fabricacion_NroTrabajadoresBase: Property = Property(name="NroTrabajadoresBase", type=IntegerType)
Fabricacion_EquipoDirectivo: Property = Property(name="EquipoDirectivo", type=StringType)
Fabricacion_PteEquipoDirectivo: Property = Property(name="PteEquipoDirectivo", type=StringType)
Fabricacion.attributes={Fabricacion_razonSocial, Fabricacion_EquipoDirectivo, Fabricacion_codigo, Fabricacion_NroTrabajadoresBase, Fabricacion_PteEquipoDirectivo}

# Distribucion class attributes and methods
Distribucion_codigo: Property = Property(name="codigo", type=IntegerType)
Distribucion_razonSocial: Property = Property(name="razonSocial", type=StringType)
Distribucion_NroTrabajadoresBase: Property = Property(name="NroTrabajadoresBase", type=IntegerType)
Distribucion_EquipoDirectivo: Property = Property(name="EquipoDirectivo", type=StringType)
Distribucion_PteEquipoDirectivo: Property = Property(name="PteEquipoDirectivo", type=StringType)
Distribucion.attributes={Distribucion_NroTrabajadoresBase, Distribucion_PteEquipoDirectivo, Distribucion_codigo, Distribucion_EquipoDirectivo, Distribucion_razonSocial}

# VentaCalzado class attributes and methods
VentaCalzado_codigo: Property = Property(name="codigo", type=IntegerType)
VentaCalzado_razonSocial: Property = Property(name="razonSocial", type=StringType)
VentaCalzado_NroTrabajadoresBase: Property = Property(name="NroTrabajadoresBase", type=IntegerType)
VentaCalzado_EquipoDirectivo: Property = Property(name="EquipoDirectivo", type=StringType)
VentaCalzado_PteEquipoDirectivo: Property = Property(name="PteEquipoDirectivo", type=StringType)
VentaCalzado.attributes={VentaCalzado_codigo, VentaCalzado_NroTrabajadoresBase, VentaCalzado_razonSocial, VentaCalzado_EquipoDirectivo, VentaCalzado_PteEquipoDirectivo}

# EmpresasFiliales class attributes and methods
EmpresasFiliales_codigo: Property = Property(name="codigo", type=IntegerType)
EmpresasFiliales_razonSocial: Property = Property(name="razonSocial", type=StringType)
EmpresasFiliales.attributes={EmpresasFiliales_razonSocial, EmpresasFiliales_codigo}

# Servidor_Intel_i8_Node class attributes and methods

# logicaPresentacionFactura_Component class attributes and methods

# persistenciaFactura_Component class attributes and methods

# ServidorWEB_Node class attributes and methods

# ServidorBD_Node class attributes and methods

# Cliente2_Actor class attributes and methods

# Clientes_Actor class attributes and methods

# Calcular_Actor class attributes and methods

# Calcular class attributes and methods

# Clientes class attributes and methods

# Venta class attributes and methods
Venta_codigo: Property = Property(name="codigo", type=IntegerType)
Venta_fecha: Property = Property(name="fecha", type=StringType)
Venta.attributes={Venta_fecha, Venta_codigo}

# Producto class attributes and methods
Producto_cantidad: Property = Property(name="cantidad", type=IntegerType)
Producto_codigo: Property = Property(name="codigo", type=IntegerType)
Producto_nombre: Property = Property(name="nombre", type=StringType)
Producto_precio: Property = Property(name="precio", type=FloatType)
Producto.attributes={Producto_nombre, Producto_cantidad, Producto_precio, Producto_codigo}

# Impuesto class attributes and methods
Impuesto_porcentaje: Property = Property(name="porcentaje", type=FloatType)
Impuesto.attributes={Impuesto_porcentaje}

# Principal class attributes and methods

# Brindar_consultorias_external class attributes and methods

# Registrar_proveedores_external class attributes and methods

# Recibir_productos_o_pedidos_external class attributes and methods

# Recibir_ordenes_de_suministro_external class attributes and methods

# Entregar_productos_external class attributes and methods

# Clasificar_producto_external class attributes and methods

# Relationships
Cliente_Brindar_consultorias: BinaryAssociation = BinaryAssociation(
    name="Cliente_Brindar_consultorias",
    ends={
        Property(name="cliente0", type=Cliente_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="brindar_consultorias1", type=Brindar_consultorias_external, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Registrar_proveedores: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Registrar_proveedores",
    ends={
        Property(name="proveedores2", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_proveedores3", type=Registrar_proveedores_external, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Recibir_productos_o_pedidos: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Recibir_productos_o_pedidos",
    ends={
        Property(name="proveedores4", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_productos_o_pedidos5", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencias_Recibir_ordenes_de_suministro: BinaryAssociation = BinaryAssociation(
    name="Dependencias_Recibir_ordenes_de_suministro",
    ends={
        Property(name="dependencias6", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_ordenes_de_suministro7", type=Recibir_ordenes_de_suministro_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencias_Entregar_productos: BinaryAssociation = BinaryAssociation(
    name="Dependencias_Entregar_productos",
    ends={
        Property(name="dependencias8", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="entregar_productos9", type=Entregar_productos_external, multiplicity=Multiplicity(0, 1))
    }
)
Contabilidad_y_Tesoreria_Recibir_productos_o_pedidos: BinaryAssociation = BinaryAssociation(
    name="Contabilidad_y_Tesoreria_Recibir_productos_o_pedidos",
    ends={
        Property(name="contabilidad_y_Tesoreria10", type=Contabilidad_y_Tesoreria_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_productos_o_pedidos11", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase",
    ends={
        Property(name="actor12", type=Responsable_de_inventario_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase13", type=Clasificar_producto_external, multiplicity=Multiplicity(0, 1))
    }
)
es_enviado: BinaryAssociation = BinaryAssociation(
    name="es_enviado",
    ends={
        Property(name="ordenesPedidos14", type=OrdenesPedidos, multiplicity=Multiplicity(0, 9999)),
        Property(name="proveedor15", type=Proveedor, multiplicity=Multiplicity(1, 1))
    }
)
provee: BinaryAssociation = BinaryAssociation(
    name="provee",
    ends={
        Property(name="pedidos16", type=Pedidos, multiplicity=Multiplicity(0, 9999)),
        Property(name="proveedor17", type=Proveedor, multiplicity=Multiplicity(1, 1))
    }
)
conforma: BinaryAssociation = BinaryAssociation(
    name="conforma",
    ends={
        Property(name="elementos18", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="ordenesPedidos19", type=OrdenesPedidos, multiplicity=Multiplicity(0, 9999))
    }
)
relaciona: BinaryAssociation = BinaryAssociation(
    name="relaciona",
    ends={
        Property(name="elementos20", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="solicitudSuministro21", type=SolicitudSuministro, multiplicity=Multiplicity(0, 9999))
    }
)
genera: BinaryAssociation = BinaryAssociation(
    name="genera",
    ends={
        Property(name="ordenesPedidos22", type=OrdenesPedidos, multiplicity=Multiplicity(0, 1)),
        Property(name="solicitudSuministro23", type=SolicitudSuministro, multiplicity=Multiplicity(1, 9999))
    }
)
realiza: BinaryAssociation = BinaryAssociation(
    name="realiza",
    ends={
        Property(name="dependencia24", type=Dependencia, multiplicity=Multiplicity(1, 1)),
        Property(name="solicitudSuministro25", type=SolicitudSuministro, multiplicity=Multiplicity(0, 1))
    }
)
elabora: BinaryAssociation = BinaryAssociation(
    name="elabora",
    ends={
        Property(name="factura26", type=Factura, multiplicity=Multiplicity(0, 9999)),
        Property(name="proveedor27", type=Proveedor, multiplicity=Multiplicity(1, 1))
    }
)
factura: BinaryAssociation = BinaryAssociation(
    name="factura",
    ends={
        Property(name="elementos28", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="factura29", type=Factura, multiplicity=Multiplicity(0, 9999))
    }
)
realiza_anualmente: BinaryAssociation = BinaryAssociation(
    name="realiza_anualmente",
    ends={
        Property(name="informe30", type=Informe, multiplicity=Multiplicity(1, 1)),
        Property(name="trabajador31", type=Trabajador, multiplicity=Multiplicity(0, 9999))
    }
)
contrata: BinaryAssociation = BinaryAssociation(
    name="contrata",
    ends={
        Property(name="empresasFiliales32", type=EmpresasFiliales, multiplicity=Multiplicity(1, 9999)),
        Property(name="trabajador33", type=Trabajador, multiplicity=Multiplicity(0, 9999))
    }
)
Calcular_Clientes: BinaryAssociation = BinaryAssociation(
    name="Calcular_Clientes",
    ends={
        Property(name="calcular34", type=Calcular, multiplicity=Multiplicity(0, 1)),
        Property(name="clientes35", type=Clientes, multiplicity=Multiplicity(0, 1))
    }
)
contiene: BinaryAssociation = BinaryAssociation(
    name="contiene",
    ends={
        Property(name="venta36", type=Venta, multiplicity=Multiplicity(1, 9999)),
        Property(name="producto37", type=Producto, multiplicity=Multiplicity(1, 9999))
    }
)
tiene: BinaryAssociation = BinaryAssociation(
    name="tiene",
    ends={
        Property(name="producto38", type=Producto, multiplicity=Multiplicity(1, 1)),
        Property(name="impuesto39", type=Impuesto, multiplicity=Multiplicity(1, 1))
    }
)
Principal_Venta: BinaryAssociation = BinaryAssociation(
    name="Principal_Venta",
    ends={
        Property(name="principal40", type=Principal, multiplicity=Multiplicity(0, 1)),
        Property(name="venta41", type=Venta, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_d_5_IG3dEeqhRdvvYtDJdw",
    types={Millenium_Component, Cliente_Actor, Natural_Actor, Juridica_Actor, Proveedores_Actor, Dependencias_Actor, Departamento_de_Inventario_y_Suministros_DIS_Component, Contabilidad_y_Tesoreria_Actor, Servicio_WEB_Movil___Recepcion_de_pedidos_Component, Responsable_de_inventario_Actor, OrdenesPedidos, Proveedor, Elementos, Factura, SolicitudSuministro, Dependencia, Trabajador, Pedidos, Informe, Fabricacion, Distribucion, VentaCalzado, EmpresasFiliales, Servidor_Intel_i8_Node, logicaPresentacionFactura_Component, persistenciaFactura_Component, ServidorWEB_Node, ServidorBD_Node, Cliente2_Actor, Clientes_Actor, Calcular_Actor, Calcular, Clientes, Venta, Producto, Impuesto, Principal, Brindar_consultorias_external, Registrar_proveedores_external, Recibir_productos_o_pedidos_external, Recibir_ordenes_de_suministro_external, Entregar_productos_external, Clasificar_producto_external},
    associations={Cliente_Brindar_consultorias, Proveedores_Registrar_proveedores, Proveedores_Recibir_productos_o_pedidos, Dependencias_Recibir_ordenes_de_suministro, Dependencias_Entregar_productos, Contabilidad_y_Tesoreria_Recibir_productos_o_pedidos, Actor_UseCase, es_enviado, provee, conforma, relaciona, genera, realiza, elabora, factura, realiza_anualmente, contrata, Calcular_Clientes, contiene, tiene, Principal_Venta},
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