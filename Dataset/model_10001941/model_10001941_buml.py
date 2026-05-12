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
Millenium_S_A_Component = Class(name="Millenium_S_A_Component")
Cliente_Actor = Class(name="Cliente_Actor")
Natural_Actor = Class(name="Natural_Actor")
Juridica_Actor = Class(name="Juridica_Actor")
Departamento_de_Inventarios_y_Suministros_DIS_Component = Class(name="Departamento_de_Inventarios_y_Suministros_DIS_Component")
Proveedores_Actor = Class(name="Proveedores_Actor")
Dependencias_Actor = Class(name="Dependencias_Actor")
Sistema_WEB_Movil___Recepci_n_de_pedidos_Component = Class(name="Sistema_WEB_Movil___Recepci_n_de_pedidos_Component")
Responsable_inventariorio_Actor = Class(name="Responsable_inventariorio_Actor")
Contabilidad_y_Tesorer_a_Actor = Class(name="Contabilidad_y_Tesorer_a_Actor")
Proveedor = Class(name="Proveedor")
_rdenesPedido = Class(name="_rdenesPedido")
Elementos = Class(name="Elementos")
Factura = Class(name="Factura")
SolicitudSuministro = Class(name="SolicitudSuministro")
Dependencia = Class(name="Dependencia")
Pedidos = Class(name="Pedidos")
Servidor_Intel_i9_Node = Class(name="Servidor_Intel_i9_Node")
logicaPresentacion_Factura_Component = Class(name="logicaPresentacion_Factura_Component")
Persistencia_Factura_Component = Class(name="Persistencia_Factura_Component")
ServidoWeb_Node = Class(name="ServidoWeb_Node")
ServidorBD_Node = Class(name="ServidorBD_Node")
Brindar_consultor_a_external = Class(name="Brindar_consultor_a_external")
Registrar_Proveedores_external = Class(name="Registrar_Proveedores_external")
Recibir_productos_o_pedidos_external = Class(name="Recibir_productos_o_pedidos_external")
Recibir_ordenes_de_suministros_external = Class(name="Recibir_ordenes_de_suministros_external")
Entregar_productos_external = Class(name="Entregar_productos_external")
Clasificar_producto_external = Class(name="Clasificar_producto_external")
Revisi_n_de_factura_external = Class(name="Revisi_n_de_factura_external")

# Millenium_S_A_Component class attributes and methods

# Cliente_Actor class attributes and methods

# Natural_Actor class attributes and methods

# Juridica_Actor class attributes and methods

# Departamento_de_Inventarios_y_Suministros_DIS_Component class attributes and methods

# Proveedores_Actor class attributes and methods

# Dependencias_Actor class attributes and methods

# Sistema_WEB_Movil___Recepci_n_de_pedidos_Component class attributes and methods

# Responsable_inventariorio_Actor class attributes and methods

# Contabilidad_y_Tesorer_a_Actor class attributes and methods

# Proveedor class attributes and methods
Proveedor_nit: Property = Property(name="nit", type=StringType)
Proveedor_razonSocial: Property = Property(name="razonSocial", type=StringType)
Proveedor_direccion: Property = Property(name="direccion", type=StringType)
Proveedor_telefono: Property = Property(name="telefono", type=StringType)
Proveedor.attributes={Proveedor_telefono, Proveedor_nit, Proveedor_razonSocial, Proveedor_direccion}

# _rdenesPedido class attributes and methods
_rdenesPedido_codigo: Property = Property(name="codigo", type=StringType)
_rdenesPedido_fecha: Property = Property(name="fecha", type=StringType)
_rdenesPedido.attributes={_rdenesPedido_fecha, _rdenesPedido_codigo}

# Elementos class attributes and methods
Elementos_referencia: Property = Property(name="referencia", type=StringType)
Elementos_clasificacion: Property = Property(name="clasificacion", type=StringType)
Elementos.attributes={Elementos_referencia, Elementos_clasificacion}

# Factura class attributes and methods
Factura_codigo: Property = Property(name="codigo", type=StringType)
Factura_fecha: Property = Property(name="fecha", type=StringType)
Factura.attributes={Factura_codigo, Factura_fecha}

# SolicitudSuministro class attributes and methods
SolicitudSuministro_solicitud: Property = Property(name="solicitud", type=StringType)
SolicitudSuministro_fecha: Property = Property(name="fecha", type=StringType)
SolicitudSuministro.attributes={SolicitudSuministro_solicitud, SolicitudSuministro_fecha}

# Dependencia class attributes and methods
Dependencia_codgio: Property = Property(name="codgio", type=StringType)
Dependencia_nombre: Property = Property(name="nombre", type=StringType)
Dependencia_reponsable: Property = Property(name="reponsable", type=StringType)
Dependencia.attributes={Dependencia_nombre, Dependencia_codgio, Dependencia_reponsable}

# Pedidos class attributes and methods
Pedidos_codigo: Property = Property(name="codigo", type=StringType)
Pedidos_fecha: Property = Property(name="fecha", type=StringType)
Pedidos.attributes={Pedidos_fecha, Pedidos_codigo}

# Servidor_Intel_i9_Node class attributes and methods

# logicaPresentacion_Factura_Component class attributes and methods

# Persistencia_Factura_Component class attributes and methods

# ServidoWeb_Node class attributes and methods

# ServidorBD_Node class attributes and methods

# Brindar_consultor_a_external class attributes and methods

# Registrar_Proveedores_external class attributes and methods

# Recibir_productos_o_pedidos_external class attributes and methods

# Recibir_ordenes_de_suministros_external class attributes and methods

# Entregar_productos_external class attributes and methods

# Clasificar_producto_external class attributes and methods

# Revisi_n_de_factura_external class attributes and methods

# Relationships
Actor_Actor2: BinaryAssociation = BinaryAssociation(
    name="Actor_Actor2",
    ends={
        Property(name="actor0", type=Natural_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="actor21", type=Juridica_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cliente_Brindar_consultor_a: BinaryAssociation = BinaryAssociation(
    name="Cliente_Brindar_consultor_a",
    ends={
        Property(name="cliente2", type=Cliente_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="brindar_consultor_a3", type=Brindar_consultor_a_external, multiplicity=Multiplicity(0, 1))
    }
)
Registrar_Proveedores_Contabilidad_y_Tesorer_a: BinaryAssociation = BinaryAssociation(
    name="Registrar_Proveedores_Contabilidad_y_Tesorer_a",
    ends={
        Property(name="registrar_Proveedores4", type=Registrar_Proveedores_external, multiplicity=Multiplicity(0, 1)),
        Property(name="contabilidad_y_Tesorer_a5", type=Contabilidad_y_Tesorer_a_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Registrar_Proveedores: BinaryAssociation = BinaryAssociation(
    name="Actor_Registrar_Proveedores",
    ends={
        Property(name="actor6", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_Proveedores7", type=Registrar_Proveedores_external, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Recibir_productos: BinaryAssociation = BinaryAssociation(
    name="Actor_Recibir_productos",
    ends={
        Property(name="actor8", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_productos9", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencias_Recibir_ordenes_de_suministros: BinaryAssociation = BinaryAssociation(
    name="Dependencias_Recibir_ordenes_de_suministros",
    ends={
        Property(name="dependencias10", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_ordenes_de_suministros11", type=Recibir_ordenes_de_suministros_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencias_Entregar_productos: BinaryAssociation = BinaryAssociation(
    name="Dependencias_Entregar_productos",
    ends={
        Property(name="dependencias12", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="entregar_productos13", type=Entregar_productos_external, multiplicity=Multiplicity(0, 1))
    }
)
Responsable_inventariorio_Clasificar_producto: BinaryAssociation = BinaryAssociation(
    name="Responsable_inventariorio_Clasificar_producto",
    ends={
        Property(name="responsable_inventariorio14", type=Responsable_inventariorio_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="clasificar_producto15", type=Clasificar_producto_external, multiplicity=Multiplicity(0, 1))
    }
)
Responsable_inventariorio_Revisi_n_de_factura: BinaryAssociation = BinaryAssociation(
    name="Responsable_inventariorio_Revisi_n_de_factura",
    ends={
        Property(name="responsable_inventariorio16", type=Responsable_inventariorio_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="revisi_n_de_factura17", type=Revisi_n_de_factura_external, multiplicity=Multiplicity(0, 1))
    }
)
es_enviado: BinaryAssociation = BinaryAssociation(
    name="es_enviado",
    ends={
        Property(name="proveedor18", type=Proveedor, multiplicity=Multiplicity(1, 1)),
        Property(name="_rdenesPedido19", type=_rdenesPedido, multiplicity=Multiplicity(0, 9999))
    }
)
Provee: BinaryAssociation = BinaryAssociation(
    name="Provee",
    ends={
        Property(name="proveedor20", type=Proveedor, multiplicity=Multiplicity(1, 1)),
        Property(name="pedidos21", type=Pedidos, multiplicity=Multiplicity(0, 9999))
    }
)
Conforma: BinaryAssociation = BinaryAssociation(
    name="Conforma",
    ends={
        Property(name="_rdenesPedido22", type=_rdenesPedido, multiplicity=Multiplicity(0, 9999)),
        Property(name="elementos23", type=Elementos, multiplicity=Multiplicity(1, 9999))
    }
)
relaciona: BinaryAssociation = BinaryAssociation(
    name="relaciona",
    ends={
        Property(name="elementos24", type=Elementos, multiplicity=Multiplicity(0, 1)),
        Property(name="solicitudSuministro25", type=SolicitudSuministro, multiplicity=Multiplicity(0, 1))
    }
)
genera: BinaryAssociation = BinaryAssociation(
    name="genera",
    ends={
        Property(name="solicitudSuministro26", type=SolicitudSuministro, multiplicity=Multiplicity(1, 9999)),
        Property(name="_rdenesPedido27", type=_rdenesPedido, multiplicity=Multiplicity(0, 1))
    }
)
realiza: BinaryAssociation = BinaryAssociation(
    name="realiza",
    ends={
        Property(name="solicitudSuministro28", type=SolicitudSuministro, multiplicity=Multiplicity(1, 9999)),
        Property(name="dependencia29", type=Dependencia, multiplicity=Multiplicity(1, 1))
    }
)
elabora: BinaryAssociation = BinaryAssociation(
    name="elabora",
    ends={
        Property(name="proveedor30", type=Proveedor, multiplicity=Multiplicity(1, 1)),
        Property(name="factura31", type=Factura, multiplicity=Multiplicity(0, 9999))
    }
)
factura: BinaryAssociation = BinaryAssociation(
    name="factura",
    ends={
        Property(name="factura32", type=Factura, multiplicity=Multiplicity(0, 9999)),
        Property(name="elementos33", type=Elementos, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_exXV0G3dEeqhRdvvYtDJdw",
    types={Millenium_S_A_Component, Cliente_Actor, Natural_Actor, Juridica_Actor, Departamento_de_Inventarios_y_Suministros_DIS_Component, Proveedores_Actor, Dependencias_Actor, Sistema_WEB_Movil___Recepci_n_de_pedidos_Component, Responsable_inventariorio_Actor, Contabilidad_y_Tesorer_a_Actor, Proveedor, _rdenesPedido, Elementos, Factura, SolicitudSuministro, Dependencia, Pedidos, Servidor_Intel_i9_Node, logicaPresentacion_Factura_Component, Persistencia_Factura_Component, ServidoWeb_Node, ServidorBD_Node, Brindar_consultor_a_external, Registrar_Proveedores_external, Recibir_productos_o_pedidos_external, Recibir_ordenes_de_suministros_external, Entregar_productos_external, Clasificar_producto_external, Revisi_n_de_factura_external},
    associations={Actor_Actor2, Cliente_Brindar_consultor_a, Registrar_Proveedores_Contabilidad_y_Tesorer_a, Actor_Registrar_Proveedores, Actor_Recibir_productos, Dependencias_Recibir_ordenes_de_suministros, Dependencias_Entregar_productos, Responsable_inventariorio_Clasificar_producto, Responsable_inventariorio_Revisi_n_de_factura, es_enviado, Provee, Conforma, relaciona, genera, realiza, elabora, factura},
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