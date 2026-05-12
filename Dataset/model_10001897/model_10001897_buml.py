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
Juridico_Actor = Class(name="Juridico_Actor")
Departamento_de_inventarios_y_Suminsitros_Component = Class(name="Departamento_de_inventarios_y_Suminsitros_Component")
Proveedores_Actor = Class(name="Proveedores_Actor")
Dependencias_Actor = Class(name="Dependencias_Actor")
Actor_Actor = Class(name="Actor_Actor")
Sistema_Web_Movil___Receccion_de_pedidos_Component = Class(name="Sistema_Web_Movil___Receccion_de_pedidos_Component")
_Actor = Class(name="_Actor")
Factura = Class(name="Factura")
Ordenes_Perdidos = Class(name="Ordenes_Perdidos")
Solicitud_suministro = Class(name="Solicitud_suministro")
Elementos = Class(name="Elementos")
Proveedores = Class(name="Proveedores")
Dependencia = Class(name="Dependencia")
Pedidos = Class(name="Pedidos")
Presupuesto = Class(name="Presupuesto")
Facturas = Class(name="Facturas")
Comerciales = Class(name="Comerciales")
Empresa = Class(name="Empresa")
Imformes = Class(name="Imformes")
TransferenciaCompa_ia = Class(name="TransferenciaCompa_ia")
CuentaBanco = Class(name="CuentaBanco")
Compa_ia = Class(name="Compa_ia")
ventas = Class(name="ventas")
Pago = Class(name="Pago")
Pedidos1 = Class(name="Pedidos1")
Servidor_Intel_Node = Class(name="Servidor_Intel_Node")
Cacular = Class(name="Cacular")
JavaApplication2 = Class(name="JavaApplication2")
venta = Class(name="venta")
producto = Class(name="producto")
impuesto = Class(name="impuesto")
Brindar_consultoria_external = Class(name="Brindar_consultoria_external")
Recibir_productos_o_pedidos_external = Class(name="Recibir_productos_o_pedidos_external")
Registrar_proveedores_external = Class(name="Registrar_proveedores_external")
Resivir_ordenes_de_suministros_external = Class(name="Resivir_ordenes_de_suministros_external")
Entregar_Productos_external = Class(name="Entregar_Productos_external")
Clasificar_Producto_external = Class(name="Clasificar_Producto_external")

# Millenium_Component class attributes and methods

# Cliente_Actor class attributes and methods

# Natural_Actor class attributes and methods

# Juridico_Actor class attributes and methods

# Departamento_de_inventarios_y_Suminsitros_Component class attributes and methods

# Proveedores_Actor class attributes and methods

# Dependencias_Actor class attributes and methods

# Actor_Actor class attributes and methods

# Sistema_Web_Movil___Receccion_de_pedidos_Component class attributes and methods

# _Actor class attributes and methods

# Factura class attributes and methods
Factura_Codigo: Property = Property(name="Codigo", type=StringType)
Factura_Fecha: Property = Property(name="Fecha", type=StringType)
Factura.attributes={Factura_Fecha, Factura_Codigo}

# Ordenes_Perdidos class attributes and methods
Ordenes_Perdidos_Codigo: Property = Property(name="Codigo", type=StringType)
Ordenes_Perdidos_Fecha: Property = Property(name="Fecha", type=StringType)
Ordenes_Perdidos.attributes={Ordenes_Perdidos_Codigo, Ordenes_Perdidos_Fecha}

# Solicitud_suministro class attributes and methods
Solicitud_suministro_Codigo: Property = Property(name="Codigo", type=StringType)
Solicitud_suministro_Fecha: Property = Property(name="Fecha", type=StringType)
Solicitud_suministro.attributes={Solicitud_suministro_Fecha, Solicitud_suministro_Codigo}

# Elementos class attributes and methods
Elementos_Referencia: Property = Property(name="Referencia", type=StringType)
Elementos_Clasificacion: Property = Property(name="Clasificacion", type=StringType)
Elementos.attributes={Elementos_Referencia, Elementos_Clasificacion}

# Proveedores class attributes and methods
Proveedores_Nit: Property = Property(name="Nit", type=StringType)
Proveedores_RazonSocial: Property = Property(name="RazonSocial", type=StringType)
Proveedores_Direccion: Property = Property(name="Direccion", type=StringType)
Proveedores_Telefono: Property = Property(name="Telefono", type=StringType)
Proveedores.attributes={Proveedores_Direccion, Proveedores_Telefono, Proveedores_RazonSocial, Proveedores_Nit}

# Dependencia class attributes and methods
Dependencia_Codigo: Property = Property(name="Codigo", type=StringType)
Dependencia_Nombre: Property = Property(name="Nombre", type=StringType)
Dependencia_Responsable: Property = Property(name="Responsable", type=StringType)
Dependencia.attributes={Dependencia_Responsable, Dependencia_Codigo, Dependencia_Nombre}

# Pedidos class attributes and methods
Pedidos_Codigo: Property = Property(name="Codigo", type=StringType)
Pedidos_Fecha: Property = Property(name="Fecha", type=StringType)
Pedidos.attributes={Pedidos_Fecha, Pedidos_Codigo}

# Presupuesto class attributes and methods

# Facturas class attributes and methods
Facturas_codigo: Property = Property(name="codigo", type=StringType)
Facturas_nombre: Property = Property(name="nombre", type=StringType)
Facturas_nif: Property = Property(name="nif", type=StringType)
Facturas_direccionPostal: Property = Property(name="direccionPostal", type=StringType)
Facturas.attributes={Facturas_codigo, Facturas_direccionPostal, Facturas_nombre, Facturas_nif}

# Comerciales class attributes and methods
Comerciales_Id: Property = Property(name="Id", type=StringType)
Comerciales_Nombre: Property = Property(name="Nombre", type=StringType)
Comerciales_Zona: Property = Property(name="Zona", type=StringType)
Comerciales.attributes={Comerciales_Nombre, Comerciales_Id, Comerciales_Zona}

# Empresa class attributes and methods
Empresa_codigo: Property = Property(name="codigo", type=StringType)
Empresa_nombre: Property = Property(name="nombre", type=StringType)
Empresa_ubicacion: Property = Property(name="ubicacion", type=StringType)
Empresa.attributes={Empresa_nombre, Empresa_ubicacion, Empresa_codigo}

# Imformes class attributes and methods

# TransferenciaCompa_ia class attributes and methods
TransferenciaCompa_ia_numerodecuenta: Property = Property(name="numerodecuenta", type=StringType)
TransferenciaCompa_ia.attributes={TransferenciaCompa_ia_numerodecuenta}

# CuentaBanco class attributes and methods
CuentaBanco_nombreBanco: Property = Property(name="nombreBanco", type=StringType)
CuentaBanco_numeroCuenta: Property = Property(name="numeroCuenta", type=StringType)
CuentaBanco_tipoCuenta: Property = Property(name="tipoCuenta", type=StringType)
CuentaBanco.attributes={CuentaBanco_nombreBanco, CuentaBanco_numeroCuenta, CuentaBanco_tipoCuenta}

# Compa_ia class attributes and methods
Compa_ia_codigo: Property = Property(name="codigo", type=StringType)
Compa_ia_zona: Property = Property(name="zona", type=StringType)
Compa_ia.attributes={Compa_ia_codigo, Compa_ia_zona}

# ventas class attributes and methods
ventas_valordeventa: Property = Property(name="valordeventa", type=StringType)
ventas_fechadeventas: Property = Property(name="fechadeventas", type=StringType)
ventas.attributes={ventas_valordeventa, ventas_fechadeventas}

# Pago class attributes and methods
Pago_Codigo: Property = Property(name="Codigo", type=StringType)
Pago_Fecha: Property = Property(name="Fecha", type=StringType)
Pago.attributes={Pago_Fecha, Pago_Codigo}

# Pedidos1 class attributes and methods
Pedidos1_codigo: Property = Property(name="codigo", type=StringType)
Pedidos1_fecha: Property = Property(name="fecha", type=StringType)
Pedidos1.attributes={Pedidos1_codigo, Pedidos1_fecha}

# Servidor_Intel_Node class attributes and methods

# Cacular class attributes and methods

# JavaApplication2 class attributes and methods

# venta class attributes and methods
venta_Setcodigo: Property = Property(name="Setcodigo", type=StringType)
venta_setFecha: Property = Property(name="setFecha", type=StringType)
venta.attributes={venta_Setcodigo, venta_setFecha}

# producto class attributes and methods
producto_setCodigo: Property = Property(name="setCodigo", type=StringType)
producto_setNombre: Property = Property(name="setNombre", type=StringType)
producto_setPrecio: Property = Property(name="setPrecio", type=FloatType)
producto_setCantidad: Property = Property(name="setCantidad", type=IntegerType)
producto.attributes={producto_setCodigo, producto_setCantidad, producto_setNombre, producto_setPrecio}

# impuesto class attributes and methods
impuesto_setPorcentaje: Property = Property(name="setPorcentaje", type=FloatType)
impuesto.attributes={impuesto_setPorcentaje}

# Brindar_consultoria_external class attributes and methods

# Recibir_productos_o_pedidos_external class attributes and methods

# Registrar_proveedores_external class attributes and methods

# Resivir_ordenes_de_suministros_external class attributes and methods

# Entregar_Productos_external class attributes and methods

# Clasificar_Producto_external class attributes and methods

# Relationships
Cliente_Brindar_consultoria: BinaryAssociation = BinaryAssociation(
    name="Cliente_Brindar_consultoria",
    ends={
        Property(name="cliente0", type=Cliente_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="brindar_consultoria1", type=Brindar_consultoria_external, multiplicity=Multiplicity(0, 1))
    }
)
Recibir_productos_o_pedidos_Actor: BinaryAssociation = BinaryAssociation(
    name="Recibir_productos_o_pedidos_Actor",
    ends={
        Property(name="recibir_productos_o_pedidos2", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor3", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Registrar_proveedores: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Registrar_proveedores",
    ends={
        Property(name="proveedores4", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_proveedores5", type=Registrar_proveedores_external, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Recibir_productos_o_pedidos: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Recibir_productos_o_pedidos",
    ends={
        Property(name="proveedores6", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_productos_o_pedidos7", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencias_Resivir_ordenes_de_suministros: BinaryAssociation = BinaryAssociation(
    name="Dependencias_Resivir_ordenes_de_suministros",
    ends={
        Property(name="dependencias8", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="resivir_ordenes_de_suministros9", type=Resivir_ordenes_de_suministros_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencias_Entregar_Productos: BinaryAssociation = BinaryAssociation(
    name="Dependencias_Entregar_Productos",
    ends={
        Property(name="dependencias10", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="entregar_Productos11", type=Entregar_Productos_external, multiplicity=Multiplicity(0, 1))
    }
)
Actor2_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor2_UseCase",
    ends={
        Property(name="actor212", type=_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase13", type=Clasificar_Producto_external, multiplicity=Multiplicity(0, 1))
    }
)
Ordenes_Perdidos_Proveedores: BinaryAssociation = BinaryAssociation(
    name="Ordenes_Perdidos_Proveedores",
    ends={
        Property(name="ordenes_Perdidos14", type=Ordenes_Perdidos, multiplicity=Multiplicity(0, 9999)),
        Property(name="proveedores15", type=Proveedores, multiplicity=Multiplicity(1, 1))
    }
)
Provee: BinaryAssociation = BinaryAssociation(
    name="Provee",
    ends={
        Property(name="pedidos16", type=Pedidos, multiplicity=Multiplicity(0, 9999)),
        Property(name="proveedores17", type=Proveedores, multiplicity=Multiplicity(1, 1))
    }
)
Conforma: BinaryAssociation = BinaryAssociation(
    name="Conforma",
    ends={
        Property(name="elementos18", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="ordenes_Perdidos19", type=Ordenes_Perdidos, multiplicity=Multiplicity(0, 9999))
    }
)
Relaciones: BinaryAssociation = BinaryAssociation(
    name="Relaciones",
    ends={
        Property(name="elementos20", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="solicitud_suministro21", type=Solicitud_suministro, multiplicity=Multiplicity(0, 9999))
    }
)
Genera: BinaryAssociation = BinaryAssociation(
    name="Genera",
    ends={
        Property(name="ordenes_Perdidos22", type=Ordenes_Perdidos, multiplicity=Multiplicity(0, 1)),
        Property(name="solicitud_suministro23", type=Solicitud_suministro, multiplicity=Multiplicity(1, 9999))
    }
)
Realiza: BinaryAssociation = BinaryAssociation(
    name="Realiza",
    ends={
        Property(name="solicitud_suministro24", type=Solicitud_suministro, multiplicity=Multiplicity(1, 9999)),
        Property(name="dependencia25", type=Dependencia, multiplicity=Multiplicity(1, 1))
    }
)
Elabora: BinaryAssociation = BinaryAssociation(
    name="Elabora",
    ends={
        Property(name="proveedores26", type=Proveedores, multiplicity=Multiplicity(1, 1)),
        Property(name="factura27", type=Factura, multiplicity=Multiplicity(0, 9999))
    }
)
Factura: BinaryAssociation = BinaryAssociation(
    name="Factura",
    ends={
        Property(name="factura28", type=Factura, multiplicity=Multiplicity(0, 9999)),
        Property(name="elementos29", type=Elementos, multiplicity=Multiplicity(0, 1))
    }
)
Realiza1: BinaryAssociation = BinaryAssociation(
    name="Realiza1",
    ends={
        Property(name="comerciales30", type=Comerciales, multiplicity=Multiplicity(1, 1)),
        Property(name="gastos31", type=Presupuesto, multiplicity=Multiplicity(1, 1))
    }
)
Asigna: BinaryAssociation = BinaryAssociation(
    name="Asigna",
    ends={
        Property(name="empresa32", type=Empresa, multiplicity=Multiplicity(1, 1)),
        Property(name="gastos33", type=Presupuesto, multiplicity=Multiplicity(0, 9999))
    }
)
Paga: BinaryAssociation = BinaryAssociation(
    name="Paga",
    ends={
        Property(name="facturas34", type=Facturas, multiplicity=Multiplicity(1, 1)),
        Property(name="comerciales35", type=Comerciales, multiplicity=Multiplicity(1, 9999))
    }
)
Genera1: BinaryAssociation = BinaryAssociation(
    name="Genera1",
    ends={
        Property(name="comerciales36", type=Comerciales, multiplicity=Multiplicity(1, 1)),
        Property(name="ingresos37", type=Imformes, multiplicity=Multiplicity(0, 9999))
    }
)
Factura1: BinaryAssociation = BinaryAssociation(
    name="Factura1",
    ends={
        Property(name="empresa38", type=Empresa, multiplicity=Multiplicity(1, 1)),
        Property(name="facturas39", type=Facturas, multiplicity=Multiplicity(1, 9999))
    }
)
visita: BinaryAssociation = BinaryAssociation(
    name="visita",
    ends={
        Property(name="comerciales40", type=Comerciales, multiplicity=Multiplicity(1, 9999)),
        Property(name="compa_ia41", type=Compa_ia, multiplicity=Multiplicity(1, 1))
    }
)
hace: BinaryAssociation = BinaryAssociation(
    name="hace",
    ends={
        Property(name="comerciales42", type=Comerciales, multiplicity=Multiplicity(1, 1)),
        Property(name="ventas43", type=ventas, multiplicity=Multiplicity(0, 9999))
    }
)
assoc__px0D3ZfBEeqEM7mFKilpXw: BinaryAssociation = BinaryAssociation(
    name="assoc__px0D3ZfBEeqEM7mFKilpXw",
    ends={
        Property(name="cancela44", type=Pago, multiplicity=Multiplicity(1, 1)),
        Property(name="facturas45", type=Facturas, multiplicity=Multiplicity(1, 9999))
    }
)
Emite: BinaryAssociation = BinaryAssociation(
    name="Emite",
    ends={
        Property(name="compa_ia46", type=Compa_ia, multiplicity=Multiplicity(1, 1)),
        Property(name="facturas47", type=Facturas, multiplicity=Multiplicity(0, 9999))
    }
)
Provee1: BinaryAssociation = BinaryAssociation(
    name="Provee1",
    ends={
        Property(name="empresa48", type=Empresa, multiplicity=Multiplicity(1, 1)),
        Property(name="pedidos49", type=Pedidos1, multiplicity=Multiplicity(0, 9999))
    }
)
Realiza2: BinaryAssociation = BinaryAssociation(
    name="Realiza2",
    ends={
        Property(name="pedidos50", type=Pedidos1, multiplicity=Multiplicity(0, 9999)),
        Property(name="compa_ia51", type=Compa_ia, multiplicity=Multiplicity(0, 9999))
    }
)
producto_impuesto: BinaryAssociation = BinaryAssociation(
    name="producto_impuesto",
    ends={
        Property(name="producto56", type=producto, multiplicity=Multiplicity(1, 1)),
        Property(name="impuesto57", type=impuesto, multiplicity=Multiplicity(1, 1))
    }
)
Cacular_Java: BinaryAssociation = BinaryAssociation(
    name="Cacular_Java",
    ends={
        Property(name="cacular52", type=Cacular, multiplicity=Multiplicity(0, 1)),
        Property(name="JavaApplication253", type=JavaApplication2, multiplicity=Multiplicity(0, 1))
    }
)
venta_producto: BinaryAssociation = BinaryAssociation(
    name="venta_producto",
    ends={
        Property(name="venta54", type=venta, multiplicity=Multiplicity(1, 1)),
        Property(name="producto55", type=producto, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_c4_Q0G3dEeqhRdvvYtDJdw",
    types={Millenium_Component, Cliente_Actor, Natural_Actor, Juridico_Actor, Departamento_de_inventarios_y_Suminsitros_Component, Proveedores_Actor, Dependencias_Actor, Actor_Actor, Sistema_Web_Movil___Receccion_de_pedidos_Component, _Actor, Factura, Ordenes_Perdidos, Solicitud_suministro, Elementos, Proveedores, Dependencia, Pedidos, Presupuesto, Facturas, Comerciales, Empresa, Imformes, TransferenciaCompa_ia, CuentaBanco, Compa_ia, ventas, Pago, Pedidos1, Servidor_Intel_Node, Cacular, JavaApplication2, venta, producto, impuesto, Brindar_consultoria_external, Recibir_productos_o_pedidos_external, Registrar_proveedores_external, Resivir_ordenes_de_suministros_external, Entregar_Productos_external, Clasificar_Producto_external},
    associations={Cliente_Brindar_consultoria, Recibir_productos_o_pedidos_Actor, Proveedores_Registrar_proveedores, Proveedores_Recibir_productos_o_pedidos, Dependencias_Resivir_ordenes_de_suministros, Dependencias_Entregar_Productos, Actor2_UseCase, Ordenes_Perdidos_Proveedores, Provee, Conforma, Relaciones, Genera, Realiza, Elabora, Factura, Realiza1, Asigna, Paga, Genera1, Factura1, visita, hace, assoc__px0D3ZfBEeqEM7mFKilpXw, Emite, Provee1, Realiza2, producto_impuesto, Cacular_Java, venta_producto},
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