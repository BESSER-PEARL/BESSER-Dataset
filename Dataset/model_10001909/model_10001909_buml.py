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
Pedidos = Class(name="Pedidos")
Milenium_Component = Class(name="Milenium_Component")
Cliente_Actor = Class(name="Cliente_Actor")
Natural_Actor = Class(name="Natural_Actor")
Jur_dica_Actor = Class(name="Jur_dica_Actor")
Departamento_de_Inventarios_y_Suministros_DIS_Component = Class(name="Departamento_de_Inventarios_y_Suministros_DIS_Component")
Proveedores_Actor = Class(name="Proveedores_Actor")
Dependencias_Actor = Class(name="Dependencias_Actor")
Contabilidad_y_Tesorer_a_Actor = Class(name="Contabilidad_y_Tesorer_a_Actor")
Sistema_WEB_M_vil_Recepci_n_de_pedidos_Component = Class(name="Sistema_WEB_M_vil_Recepci_n_de_pedidos_Component")
Responsable_Inventario_Actor = Class(name="Responsable_Inventario_Actor")
OrdenesPedido = Class(name="OrdenesPedido")
Proveedor = Class(name="Proveedor")
Elementos = Class(name="Elementos")
Factura = Class(name="Factura")
SolicitudSuministro = Class(name="SolicitudSuministro")
Dependencia = Class(name="Dependencia")
Documentos = Class(name="Documentos")
Libros = Class(name="Libros")
Ponencias = Class(name="Ponencias")
ArticulosCient_ficos = Class(name="ArticulosCient_ficos")
Editoriales = Class(name="Editoriales")
Autores = Class(name="Autores")
Servidor_intel_I8_Node = Class(name="Servidor_intel_I8_Node")
Director = Class(name="Director")
_a__BicicletaBuilder = Class(name="_a__BicicletaBuilder")
ConcretBuilderBicicletaInfantil = Class(name="ConcretBuilderBicicletaInfantil")
ConcretBuilderBicicletaFemenina = Class(name="ConcretBuilderBicicletaFemenina")
ConcretBuilderBicicletaMasculina = Class(name="ConcretBuilderBicicletaMasculina")
ConcretBuilderBicicletaDoble = Class(name="ConcretBuilderBicicletaDoble")
Calcular_Actor = Class(name="Calcular_Actor")
ProyectoNuevo_Actor = Class(name="ProyectoNuevo_Actor")
Calcular = Class(name="Calcular")
NuevoProyecto = Class(name="NuevoProyecto")
Principal = Class(name="Principal")
Venta = Class(name="Venta")
Producto = Class(name="Producto")
Impuesto = Class(name="Impuesto")
Brindar_consultoria_external = Class(name="Brindar_consultoria_external")
Recibir_productos_o_pedidos_external = Class(name="Recibir_productos_o_pedidos_external")
Registrar_proveedores_external = Class(name="Registrar_proveedores_external")
Recibir_ordenes_de_suministro_external = Class(name="Recibir_ordenes_de_suministro_external")
Entegar_productos_external = Class(name="Entegar_productos_external")
Clasificar_producto_external = Class(name="Clasificar_producto_external")
Revisi_n_de_factura_external = Class(name="Revisi_n_de_factura_external")

# Pedidos class attributes and methods
Pedidos_codigo: Property = Property(name="codigo", type=StringType)
Pedidos_fecha: Property = Property(name="fecha", type=StringType)
Pedidos.attributes={Pedidos_fecha, Pedidos_codigo}

# Milenium_Component class attributes and methods

# Cliente_Actor class attributes and methods

# Natural_Actor class attributes and methods

# Jur_dica_Actor class attributes and methods

# Departamento_de_Inventarios_y_Suministros_DIS_Component class attributes and methods

# Proveedores_Actor class attributes and methods

# Dependencias_Actor class attributes and methods

# Contabilidad_y_Tesorer_a_Actor class attributes and methods

# Sistema_WEB_M_vil_Recepci_n_de_pedidos_Component class attributes and methods

# Responsable_Inventario_Actor class attributes and methods

# OrdenesPedido class attributes and methods
OrdenesPedido_codigo: Property = Property(name="codigo", type=StringType)
OrdenesPedido_fecha: Property = Property(name="fecha", type=StringType)
OrdenesPedido.attributes={OrdenesPedido_codigo, OrdenesPedido_fecha}

# Proveedor class attributes and methods
Proveedor_nit: Property = Property(name="nit", type=StringType)
Proveedor_razonSocial: Property = Property(name="razonSocial", type=StringType)
Proveedor_direcci_n: Property = Property(name="direcci_n", type=StringType)
Proveedor_tel_fonos: Property = Property(name="tel_fonos", type=StringType)
Proveedor.attributes={Proveedor_direcci_n, Proveedor_razonSocial, Proveedor_tel_fonos, Proveedor_nit}

# Elementos class attributes and methods
Elementos_referencia: Property = Property(name="referencia", type=StringType)
Elementos_clasificaci_n: Property = Property(name="clasificaci_n", type=StringType)
Elementos.attributes={Elementos_referencia, Elementos_clasificaci_n}

# Factura class attributes and methods
Factura_codigo: Property = Property(name="codigo", type=StringType)
Factura_fecha: Property = Property(name="fecha", type=StringType)
Factura.attributes={Factura_codigo, Factura_fecha}

# SolicitudSuministro class attributes and methods
SolicitudSuministro_codigo: Property = Property(name="codigo", type=StringType)
SolicitudSuministro_fecha: Property = Property(name="fecha", type=StringType)
SolicitudSuministro.attributes={SolicitudSuministro_codigo, SolicitudSuministro_fecha}

# Dependencia class attributes and methods
Dependencia_codigo: Property = Property(name="codigo", type=StringType)
Dependencia_nombre: Property = Property(name="nombre", type=StringType)
Dependencia_responsable: Property = Property(name="responsable", type=StringType)
Dependencia.attributes={Dependencia_responsable, Dependencia_codigo, Dependencia_nombre}

# Documentos class attributes and methods
Documentos_titulo: Property = Property(name="titulo", type=StringType)
Documentos_fechaPublicaci_n: Property = Property(name="fechaPublicaci_n", type=StringType)
Documentos_autores: Property = Property(name="autores", type=StringType)
Documentos_ISBN: Property = Property(name="ISBN", type=StringType)
Documentos_mesPublicaci_n: Property = Property(name="mesPublicaci_n", type=StringType)
Documentos_d_a: Property = Property(name="d_a", type=StringType)
Documentos_editorial: Property = Property(name="editorial", type=StringType)
Documentos_fechaCreaci_n: Property = Property(name="fechaCreaci_n", type=StringType)
Documentos.attributes={Documentos_ISBN, Documentos_editorial, Documentos_d_a, Documentos_autores, Documentos_titulo, Documentos_mesPublicaci_n, Documentos_fechaCreaci_n, Documentos_fechaPublicaci_n}

# Libros class attributes and methods
Libros_n_meroP_ginas: Property = Property(name="n_meroP_ginas", type=StringType)
Libros.attributes={Libros_n_meroP_ginas}

# Ponencias class attributes and methods
Ponencias_nombreCongreso: Property = Property(name="nombreCongreso", type=StringType)
Ponencias.attributes={Ponencias_nombreCongreso}

# ArticulosCient_ficos class attributes and methods
ArticulosCient_ficos_SSN: Property = Property(name="SSN", type=StringType)
ArticulosCient_ficos.attributes={ArticulosCient_ficos_SSN}

# Editoriales class attributes and methods
Editoriales_direcci_nEmail: Property = Property(name="direcci_nEmail", type=StringType)
Editoriales_direcci_nF_sica: Property = Property(name="direcci_nF_sica", type=StringType)
Editoriales_n_meroTel_fono: Property = Property(name="n_meroTel_fono", type=StringType)
Editoriales_personaContacto: Property = Property(name="personaContacto", type=StringType)
Editoriales.attributes={Editoriales_n_meroTel_fono, Editoriales_direcci_nF_sica, Editoriales_personaContacto, Editoriales_direcci_nEmail}

# Autores class attributes and methods
Autores_fechaCreaci_n: Property = Property(name="fechaCreaci_n", type=StringType)
Autores_fechamodificaci_n: Property = Property(name="fechamodificaci_n", type=StringType)
Autores_fechaEliminaci_n: Property = Property(name="fechaEliminaci_n", type=StringType)
Autores.attributes={Autores_fechamodificaci_n, Autores_fechaCreaci_n, Autores_fechaEliminaci_n}

# Servidor_intel_I8_Node class attributes and methods

# Director class attributes and methods
Director_bicicletaBuilder: Property = Property(name="bicicletaBuilder", type=_a__BicicletaBuilder)
Director_void_construirBicicleta: Property = Property(name="void_construirBicicleta", type=StringType)
Director.attributes={Director_bicicletaBuilder, Director_void_construirBicicleta}

# _a__BicicletaBuilder class attributes and methods

# ConcretBuilderBicicletaInfantil class attributes and methods

# ConcretBuilderBicicletaFemenina class attributes and methods

# ConcretBuilderBicicletaMasculina class attributes and methods

# ConcretBuilderBicicletaDoble class attributes and methods

# Calcular_Actor class attributes and methods

# ProyectoNuevo_Actor class attributes and methods

# Calcular class attributes and methods

# NuevoProyecto class attributes and methods

# Principal class attributes and methods

# Venta class attributes and methods

# Producto class attributes and methods

# Impuesto class attributes and methods

# Brindar_consultoria_external class attributes and methods

# Recibir_productos_o_pedidos_external class attributes and methods

# Registrar_proveedores_external class attributes and methods

# Recibir_ordenes_de_suministro_external class attributes and methods

# Entegar_productos_external class attributes and methods

# Clasificar_producto_external class attributes and methods

# Revisi_n_de_factura_external class attributes and methods

# Relationships
Cliente_Brindar_consultoria: BinaryAssociation = BinaryAssociation(
    name="Cliente_Brindar_consultoria",
    ends={
        Property(name="cliente0", type=Cliente_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="brindar_consultoria1", type=Brindar_consultoria_external, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Recibir_productos_o_pedidos: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Recibir_productos_o_pedidos",
    ends={
        Property(name="proveedores2", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_productos_o_pedidos3", type=Recibir_productos_o_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Registrar_proveedores: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Registrar_proveedores",
    ends={
        Property(name="proveedores4", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_proveedores5", type=Registrar_proveedores_external, multiplicity=Multiplicity(0, 1))
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
        Property(name="entregar_productos9", type=Entegar_productos_external, multiplicity=Multiplicity(0, 1))
    }
)
Contabilidad_y_Tesorer_a_Registrar_proveedores: BinaryAssociation = BinaryAssociation(
    name="Contabilidad_y_Tesorer_a_Registrar_proveedores",
    ends={
        Property(name="contabilidad_y_Tesorer_a10", type=Contabilidad_y_Tesorer_a_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_proveedores11", type=Registrar_proveedores_external, multiplicity=Multiplicity(0, 1))
    }
)
Responsable_Inventario_Clasificar_producto: BinaryAssociation = BinaryAssociation(
    name="Responsable_Inventario_Clasificar_producto",
    ends={
        Property(name="responsable_Inventario12", type=Responsable_Inventario_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="clasificar_producto13", type=Clasificar_producto_external, multiplicity=Multiplicity(0, 1))
    }
)
Responsable_Inventario_Revisar_factura: BinaryAssociation = BinaryAssociation(
    name="Responsable_Inventario_Revisar_factura",
    ends={
        Property(name="responsable_Inventario14", type=Responsable_Inventario_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="revisar_factura15", type=Revisi_n_de_factura_external, multiplicity=Multiplicity(0, 1))
    }
)
es_enviado: BinaryAssociation = BinaryAssociation(
    name="es_enviado",
    ends={
        Property(name="ordenesPedido16", type=OrdenesPedido, multiplicity=Multiplicity(0, 9999)),
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
        Property(name="ordenesPedido21", type=OrdenesPedido, multiplicity=Multiplicity(0, 9999))
    }
)
relaciona: BinaryAssociation = BinaryAssociation(
    name="relaciona",
    ends={
        Property(name="elementos22", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="solicitudSuministro23", type=SolicitudSuministro, multiplicity=Multiplicity(0, 9999))
    }
)
genera: BinaryAssociation = BinaryAssociation(
    name="genera",
    ends={
        Property(name="solicitudSuministro24", type=SolicitudSuministro, multiplicity=Multiplicity(1, 9999)),
        Property(name="ordenesPedidos25", type=OrdenesPedido, multiplicity=Multiplicity(0, 1))
    }
)
realiza: BinaryAssociation = BinaryAssociation(
    name="realiza",
    ends={
        Property(name="solicitudSuministro26", type=SolicitudSuministro, multiplicity=Multiplicity(1, 9999)),
        Property(name="dependencia27", type=Dependencia, multiplicity=Multiplicity(1, 1))
    }
)
elabora: BinaryAssociation = BinaryAssociation(
    name="elabora",
    ends={
        Property(name="factura28", type=Factura, multiplicity=Multiplicity(0, 9999)),
        Property(name="proveedor29", type=Proveedor, multiplicity=Multiplicity(1, 1))
    }
)
factura: BinaryAssociation = BinaryAssociation(
    name="factura",
    ends={
        Property(name="factura30", type=Factura, multiplicity=Multiplicity(0, 9999)),
        Property(name="elementos31", type=Elementos, multiplicity=Multiplicity(1, 9999))
    }
)
crean: BinaryAssociation = BinaryAssociation(
    name="crean",
    ends={
        Property(name="autores232", type=Autores, multiplicity=Multiplicity(1, 9999)),
        Property(name="documentos33", type=Documentos, multiplicity=Multiplicity(0, 9999))
    }
)
contienen: BinaryAssociation = BinaryAssociation(
    name="contienen",
    ends={
        Property(name="libros34", type=Libros, multiplicity=Multiplicity(0, 9999)),
        Property(name="documentos35", type=Documentos, multiplicity=Multiplicity(1, 9999))
    }
)
contienen1: BinaryAssociation = BinaryAssociation(
    name="contienen1",
    ends={
        Property(name="articulosCient_ficos36", type=ArticulosCient_ficos, multiplicity=Multiplicity(0, 9999)),
        Property(name="documentos37", type=Documentos, multiplicity=Multiplicity(1, 9999))
    }
)
tienen: BinaryAssociation = BinaryAssociation(
    name="tienen",
    ends={
        Property(name="editoriales38", type=Editoriales, multiplicity=Multiplicity(1, 9999)),
        Property(name="documentos39", type=Documentos, multiplicity=Multiplicity(0, 9999))
    }
)
tienen1: BinaryAssociation = BinaryAssociation(
    name="tienen1",
    ends={
        Property(name="ponencias40", type=Ponencias, multiplicity=Multiplicity(0, 9999)),
        Property(name="documentos41", type=Documentos, multiplicity=Multiplicity(1, 9999))
    }
)
Calcular_NuevoProyecto: BinaryAssociation = BinaryAssociation(
    name="Calcular_NuevoProyecto",
    ends={
        Property(name="calcular42", type=Calcular, multiplicity=Multiplicity(0, 1)),
        Property(name="nuevoProyecto43", type=NuevoProyecto, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_cbit8G3dEeqhRdvvYtDJdw",
    types={Pedidos, Milenium_Component, Cliente_Actor, Natural_Actor, Jur_dica_Actor, Departamento_de_Inventarios_y_Suministros_DIS_Component, Proveedores_Actor, Dependencias_Actor, Contabilidad_y_Tesorer_a_Actor, Sistema_WEB_M_vil_Recepci_n_de_pedidos_Component, Responsable_Inventario_Actor, OrdenesPedido, Proveedor, Elementos, Factura, SolicitudSuministro, Dependencia, Documentos, Libros, Ponencias, ArticulosCient_ficos, Editoriales, Autores, Servidor_intel_I8_Node, Director, _a__BicicletaBuilder, ConcretBuilderBicicletaInfantil, ConcretBuilderBicicletaFemenina, ConcretBuilderBicicletaMasculina, ConcretBuilderBicicletaDoble, Calcular_Actor, ProyectoNuevo_Actor, Calcular, NuevoProyecto, Principal, Venta, Producto, Impuesto, Brindar_consultoria_external, Recibir_productos_o_pedidos_external, Registrar_proveedores_external, Recibir_ordenes_de_suministro_external, Entegar_productos_external, Clasificar_producto_external, Revisi_n_de_factura_external},
    associations={Cliente_Brindar_consultoria, Proveedores_Recibir_productos_o_pedidos, Proveedores_Registrar_proveedores, Dependencias_Recibir_ordenes_de_suministro, Dependencias_Entregar_productos, Contabilidad_y_Tesorer_a_Registrar_proveedores, Responsable_Inventario_Clasificar_producto, Responsable_Inventario_Revisar_factura, es_enviado, provee, conforma, relaciona, genera, realiza, elabora, factura, crean, contienen, contienen1, tienen, tienen1, Calcular_NuevoProyecto},
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