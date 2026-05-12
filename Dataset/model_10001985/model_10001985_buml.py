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
Brindar_Consultoria_external = Class(name="Brindar_Consultoria_external")
Millenium_S_A_Component = Class(name="Millenium_S_A_Component")
Clientes_Actor = Class(name="Clientes_Actor")
Natural_Actor = Class(name="Natural_Actor")
Juridico_Actor = Class(name="Juridico_Actor")
Departamento_de_inventarios_y_suministros___DIS_Component = Class(name="Departamento_de_inventarios_y_suministros___DIS_Component")
Proveedores_Actor = Class(name="Proveedores_Actor")
Dependencias_Actor = Class(name="Dependencias_Actor")
Component_Component = Class(name="Component_Component")
OrdenesPedidos = Class(name="OrdenesPedidos")
ELementos = Class(name="ELementos")
Dependencia = Class(name="Dependencia")
Factura = Class(name="Factura")
SolicitudSuministro = Class(name="SolicitudSuministro")
Proveedor = Class(name="Proveedor")
Pedidos = Class(name="Pedidos")
Pemsum_Universitario = Class(name="Pemsum_Universitario")
Materias = Class(name="Materias")
Departamento = Class(name="Departamento")
Profesor = Class(name="Profesor")
Horas_de_clase = Class(name="Horas_de_clase")
asignacion_de_creditos = Class(name="asignacion_de_creditos")
Areas_del_Conocimiento = Class(name="Areas_del_Conocimiento")
Creditos = Class(name="Creditos")
Programa = Class(name="Programa")
Servidor_Intel__Node = Class(name="Servidor_Intel__Node")
Persistencia___Factura_Component = Class(name="Persistencia___Factura_Component")
Servidor_WEB_Node = Class(name="Servidor_WEB_Node")
LogicaPresentacion___Factura_Component = Class(name="LogicaPresentacion___Factura_Component")
Servidor_BD_Node = Class(name="Servidor_BD_Node")
Calcular = Class(name="Calcular")
Javaaplication = Class(name="Javaaplication")
Venta = Class(name="Venta")
Producto = Class(name="Producto")
Impuesto = Class(name="Impuesto")
Class4 = Class(name="Class4")
Registrar_proveedores_external = Class(name="Registrar_proveedores_external")
Recibir_productos_external = Class(name="Recibir_productos_external")
Recivir_ordenes_de_suministro_external = Class(name="Recivir_ordenes_de_suministro_external")
Entregar_los_pedidos_external = Class(name="Entregar_los_pedidos_external")

# Brindar_Consultoria_external class attributes and methods

# Millenium_S_A_Component class attributes and methods

# Clientes_Actor class attributes and methods

# Natural_Actor class attributes and methods

# Juridico_Actor class attributes and methods

# Departamento_de_inventarios_y_suministros___DIS_Component class attributes and methods

# Proveedores_Actor class attributes and methods

# Dependencias_Actor class attributes and methods

# Component_Component class attributes and methods

# OrdenesPedidos class attributes and methods
OrdenesPedidos_Fecha: Property = Property(name="Fecha", type=StringType)
OrdenesPedidos_Codigo: Property = Property(name="Codigo", type=StringType)
OrdenesPedidos.attributes={OrdenesPedidos_Codigo, OrdenesPedidos_Fecha}

# ELementos class attributes and methods
ELementos_REferencia: Property = Property(name="REferencia", type=StringType)
ELementos_Clasificacion: Property = Property(name="Clasificacion", type=StringType)
ELementos.attributes={ELementos_REferencia, ELementos_Clasificacion}

# Dependencia class attributes and methods
Dependencia_Codigo: Property = Property(name="Codigo", type=StringType)
Dependencia_Nombre: Property = Property(name="Nombre", type=StringType)
Dependencia_Responsable: Property = Property(name="Responsable", type=StringType)
Dependencia.attributes={Dependencia_Responsable, Dependencia_Codigo, Dependencia_Nombre}

# Factura class attributes and methods
Factura_Codigo: Property = Property(name="Codigo", type=StringType)
Factura_Fecha: Property = Property(name="Fecha", type=StringType)
Factura.attributes={Factura_Codigo, Factura_Fecha}

# SolicitudSuministro class attributes and methods
SolicitudSuministro_Codigo: Property = Property(name="Codigo", type=StringType)
SolicitudSuministro_Fecha: Property = Property(name="Fecha", type=StringType)
SolicitudSuministro.attributes={SolicitudSuministro_Codigo, SolicitudSuministro_Fecha}

# Proveedor class attributes and methods
Proveedor_Nit: Property = Property(name="Nit", type=StringType)
Proveedor_Razonsocial: Property = Property(name="Razonsocial", type=StringType)
Proveedor_Direccion: Property = Property(name="Direccion", type=StringType)
Proveedor_Telefonos: Property = Property(name="Telefonos", type=StringType)
Proveedor.attributes={Proveedor_Direccion, Proveedor_Telefonos, Proveedor_Nit, Proveedor_Razonsocial}

# Pedidos class attributes and methods
Pedidos_Codigo: Property = Property(name="Codigo", type=StringType)
Pedidos_Fecha: Property = Property(name="Fecha", type=StringType)
Pedidos.attributes={Pedidos_Codigo, Pedidos_Fecha}

# Pemsum_Universitario class attributes and methods
Pemsum_Universitario_Materias: Property = Property(name="Materias", type=StringType)
Pemsum_Universitario_Programa: Property = Property(name="Programa", type=StringType)
Pemsum_Universitario.attributes={Pemsum_Universitario_Programa, Pemsum_Universitario_Materias}

# Materias class attributes and methods
Materias_Codigo: Property = Property(name="Codigo", type=IntegerType)
Materias_Tipo: Property = Property(name="Tipo", type=StringType)
Materias_Creditos: Property = Property(name="Creditos", type=IntegerType)
Materias_Nombre: Property = Property(name="Nombre", type=StringType)
Materias.attributes={Materias_Nombre, Materias_Codigo, Materias_Tipo, Materias_Creditos}

# Departamento class attributes and methods
Departamento_ID_Profesores: Property = Property(name="ID_Profesores", type=IntegerType)
Departamento.attributes={Departamento_ID_Profesores}

# Profesor class attributes and methods
Profesor_ID: Property = Property(name="ID", type=IntegerType)
Profesor_Nombre: Property = Property(name="Nombre", type=StringType)
Profesor_Apellido: Property = Property(name="Apellido", type=StringType)
Profesor_Area: Property = Property(name="Area", type=StringType)
Profesor.attributes={Profesor_ID, Profesor_Apellido, Profesor_Area, Profesor_Nombre}

# Horas_de_clase class attributes and methods
Horas_de_clase_CreditosMateria: Property = Property(name="CreditosMateria", type=StringType)
Horas_de_clase_TipoCreditos: Property = Property(name="TipoCreditos", type=StringType)
Horas_de_clase.attributes={Horas_de_clase_CreditosMateria, Horas_de_clase_TipoCreditos}

# asignacion_de_creditos class attributes and methods
asignacion_de_creditos_Cod_Materia: Property = Property(name="Cod_Materia", type=IntegerType)
asignacion_de_creditos.attributes={asignacion_de_creditos_Cod_Materia}

# Areas_del_Conocimiento class attributes and methods
Areas_del_Conocimiento_NombreArea: Property = Property(name="NombreArea", type=StringType)
Areas_del_Conocimiento_Departamentos: Property = Property(name="Departamentos", type=StringType)
Areas_del_Conocimiento.attributes={Areas_del_Conocimiento_Departamentos, Areas_del_Conocimiento_NombreArea}

# Creditos class attributes and methods
Creditos_Numeros: Property = Property(name="Numeros", type=IntegerType)
Creditos.attributes={Creditos_Numeros}

# Programa class attributes and methods
Programa_Codigo: Property = Property(name="Codigo", type=IntegerType)
Programa_Nombre: Property = Property(name="Nombre", type=StringType)
Programa.attributes={Programa_Nombre, Programa_Codigo}

# Servidor_Intel__Node class attributes and methods

# Persistencia___Factura_Component class attributes and methods

# Servidor_WEB_Node class attributes and methods

# LogicaPresentacion___Factura_Component class attributes and methods

# Servidor_BD_Node class attributes and methods

# Calcular class attributes and methods

# Javaaplication class attributes and methods

# Venta class attributes and methods
Venta_Codigo: Property = Property(name="Codigo", type=IntegerType)
Venta_Fecha: Property = Property(name="Fecha", type=StringType)
Venta_RealizarVenta: Property = Property(name="RealizarVenta", type=StringType)
Venta.attributes={Venta_Fecha, Venta_Codigo, Venta_RealizarVenta}

# Producto class attributes and methods
Producto_Codigo: Property = Property(name="Codigo", type=IntegerType)
Producto_Nombre: Property = Property(name="Nombre", type=StringType)
Producto_Precio: Property = Property(name="Precio", type=IntegerType)
Producto_Cantidad: Property = Property(name="Cantidad", type=IntegerType)
Producto_CalcularCosto: Property = Property(name="CalcularCosto", type=IntegerType)
Producto.attributes={Producto_Nombre, Producto_Cantidad, Producto_CalcularCosto, Producto_Codigo, Producto_Precio}

# Impuesto class attributes and methods
Impuesto_Porcentae: Property = Property(name="Porcentae", type=FloatType)
Impuesto_CalcularImpuesto: Property = Property(name="CalcularImpuesto", type=FloatType)
Impuesto.attributes={Impuesto_CalcularImpuesto, Impuesto_Porcentae}

# Class4 class attributes and methods

# Registrar_proveedores_external class attributes and methods

# Recibir_productos_external class attributes and methods

# Recivir_ordenes_de_suministro_external class attributes and methods

# Entregar_los_pedidos_external class attributes and methods

# Relationships
Calcular_Javaaplication: BinaryAssociation = BinaryAssociation(
    name="Calcular_Javaaplication",
    ends={
        Property(name="calcular46", type=Calcular, multiplicity=Multiplicity(0, 1)),
        Property(name="javaaplication47", type=Javaaplication, multiplicity=Multiplicity(0, 1))
    }
)
Venta_Producto: BinaryAssociation = BinaryAssociation(
    name="Venta_Producto",
    ends={
        Property(name="venta48", type=Venta, multiplicity=Multiplicity(0, 1)),
        Property(name="producto49", type=Producto, multiplicity=Multiplicity(0, 1))
    }
)
Venta_Impuesto: BinaryAssociation = BinaryAssociation(
    name="Venta_Impuesto",
    ends={
        Property(name="venta50", type=Venta, multiplicity=Multiplicity(0, 1)),
        Property(name="impuesto51", type=Impuesto, multiplicity=Multiplicity(0, 1))
    }
)
Producto_Impuesto: BinaryAssociation = BinaryAssociation(
    name="Producto_Impuesto",
    ends={
        Property(name="producto52", type=Producto, multiplicity=Multiplicity(0, 1)),
        Property(name="impuesto53", type=Impuesto, multiplicity=Multiplicity(0, 1))
    }
)
Clientes_Brindar_Consultoria: BinaryAssociation = BinaryAssociation(
    name="Clientes_Brindar_Consultoria",
    ends={
        Property(name="clientes0", type=Clientes_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="brindar_Consultoria1", type=Brindar_Consultoria_external, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Registrar_proveedores: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Registrar_proveedores",
    ends={
        Property(name="proveedores2", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_proveedores3", type=Registrar_proveedores_external, multiplicity=Multiplicity(0, 1))
    }
)
Proveedores_Recibir_productos: BinaryAssociation = BinaryAssociation(
    name="Proveedores_Recibir_productos",
    ends={
        Property(name="proveedores4", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_productos5", type=Recibir_productos_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencias_Recivir_ordenes_de_suministro: BinaryAssociation = BinaryAssociation(
    name="Dependencias_Recivir_ordenes_de_suministro",
    ends={
        Property(name="dependencias6", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recivir_ordenes_de_suministro7", type=Recivir_ordenes_de_suministro_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencias_Entregar_los_pedidos: BinaryAssociation = BinaryAssociation(
    name="Dependencias_Entregar_los_pedidos",
    ends={
        Property(name="dependencias8", type=Dependencias_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="entregar_los_pedidos9", type=Entregar_los_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Es_Enviado: BinaryAssociation = BinaryAssociation(
    name="Es_Enviado",
    ends={
        Property(name="ordenesPedidos10", type=OrdenesPedidos, multiplicity=Multiplicity(0, 9999)),
        Property(name="proveedor11", type=Proveedor, multiplicity=Multiplicity(1, 1))
    }
)
Provee: BinaryAssociation = BinaryAssociation(
    name="Provee",
    ends={
        Property(name="proveedor12", type=Proveedor, multiplicity=Multiplicity(1, 1)),
        Property(name="pedidos13", type=Pedidos, multiplicity=Multiplicity(0, 9999))
    }
)
Conforma: BinaryAssociation = BinaryAssociation(
    name="Conforma",
    ends={
        Property(name="eLementos14", type=ELementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="ordenesPedidos15", type=OrdenesPedidos, multiplicity=Multiplicity(0, 9999))
    }
)
Relasiona: BinaryAssociation = BinaryAssociation(
    name="Relasiona",
    ends={
        Property(name="eLementos16", type=ELementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="solicitudSuministro17", type=SolicitudSuministro, multiplicity=Multiplicity(0, 9999))
    }
)
Genera: BinaryAssociation = BinaryAssociation(
    name="Genera",
    ends={
        Property(name="ordenesPedidos18", type=OrdenesPedidos, multiplicity=Multiplicity(0, 1)),
        Property(name="solicitudSuministro19", type=SolicitudSuministro, multiplicity=Multiplicity(1, 9999))
    }
)
Realiza: BinaryAssociation = BinaryAssociation(
    name="Realiza",
    ends={
        Property(name="solicitudSuministro20", type=SolicitudSuministro, multiplicity=Multiplicity(1, 9999)),
        Property(name="dependencia21", type=Dependencia, multiplicity=Multiplicity(1, 1))
    }
)
Elabora: BinaryAssociation = BinaryAssociation(
    name="Elabora",
    ends={
        Property(name="proveedor22", type=Proveedor, multiplicity=Multiplicity(1, 1)),
        Property(name="factura23", type=Factura, multiplicity=Multiplicity(0, 9999))
    }
)
Factura: BinaryAssociation = BinaryAssociation(
    name="Factura",
    ends={
        Property(name="eLementos24", type=ELementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="factura25", type=Factura, multiplicity=Multiplicity(0, 9999))
    }
)
Contiene: BinaryAssociation = BinaryAssociation(
    name="Contiene",
    ends={
        Property(name="pemsum_Universitario26", type=Pemsum_Universitario, multiplicity=Multiplicity(1, 1)),
        Property(name="materias27", type=Materias, multiplicity=Multiplicity(1, 9999))
    }
)
Asignada_por: BinaryAssociation = BinaryAssociation(
    name="Asignada_por",
    ends={
        Property(name="materias28", type=Materias, multiplicity=Multiplicity(1, 9999)),
        Property(name="profesores29", type=Profesor, multiplicity=Multiplicity(1, 9999))
    }
)
Tiene: BinaryAssociation = BinaryAssociation(
    name="Tiene",
    ends={
        Property(name="materias30", type=Materias, multiplicity=Multiplicity(1, 1)),
        Property(name="creditos31", type=Creditos, multiplicity=Multiplicity(0, 9999))
    }
)
Tiene1: BinaryAssociation = BinaryAssociation(
    name="Tiene1",
    ends={
        Property(name="horas_de_clase32", type=Horas_de_clase, multiplicity=Multiplicity(1, 9999)),
        Property(name="materias33", type=Materias, multiplicity=Multiplicity(1, 1))
    }
)
Ayudan_a: BinaryAssociation = BinaryAssociation(
    name="Ayudan_a",
    ends={
        Property(name="departamento34", type=Departamento, multiplicity=Multiplicity(1, 1)),
        Property(name="pemsum_Universitario35", type=Pemsum_Universitario, multiplicity=Multiplicity(1, 1))
    }
)
Ayudan_a1: BinaryAssociation = BinaryAssociation(
    name="Ayudan_a1",
    ends={
        Property(name="areas_del_Conocimiento36", type=Areas_del_Conocimiento, multiplicity=Multiplicity(1, 9999)),
        Property(name="pemsum_Universitario37", type=Pemsum_Universitario, multiplicity=Multiplicity(1, 1))
    }
)
Hace: BinaryAssociation = BinaryAssociation(
    name="Hace",
    ends={
        Property(name="areas_del_Conocimiento38", type=Areas_del_Conocimiento, multiplicity=Multiplicity(1, 9999)),
        Property(name="asignacion_de_creditos39", type=asignacion_de_creditos, multiplicity=Multiplicity(0, 9999))
    }
)
Hace1: BinaryAssociation = BinaryAssociation(
    name="Hace1",
    ends={
        Property(name="departamento40", type=Departamento, multiplicity=Multiplicity(1, 1)),
        Property(name="asignacion_de_creditos41", type=asignacion_de_creditos, multiplicity=Multiplicity(0, 9999))
    }
)
Forma: BinaryAssociation = BinaryAssociation(
    name="Forma",
    ends={
        Property(name="asignacion_de_creditos42", type=asignacion_de_creditos, multiplicity=Multiplicity(0, 9999)),
        Property(name="creditos43", type=Creditos, multiplicity=Multiplicity(0, 9999))
    }
)
Contiene1: BinaryAssociation = BinaryAssociation(
    name="Contiene1",
    ends={
        Property(name="programa44", type=Programa, multiplicity=Multiplicity(1, 9999)),
        Property(name="pemsum_Universitario45", type=Pemsum_Universitario, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_hoX_MG3dEeqhRdvvYtDJdw",
    types={Brindar_Consultoria_external, Millenium_S_A_Component, Clientes_Actor, Natural_Actor, Juridico_Actor, Departamento_de_inventarios_y_suministros___DIS_Component, Proveedores_Actor, Dependencias_Actor, Component_Component, OrdenesPedidos, ELementos, Dependencia, Factura, SolicitudSuministro, Proveedor, Pedidos, Pemsum_Universitario, Materias, Departamento, Profesor, Horas_de_clase, asignacion_de_creditos, Areas_del_Conocimiento, Creditos, Programa, Servidor_Intel__Node, Persistencia___Factura_Component, Servidor_WEB_Node, LogicaPresentacion___Factura_Component, Servidor_BD_Node, Calcular, Javaaplication, Venta, Producto, Impuesto, Class4, Registrar_proveedores_external, Recibir_productos_external, Recivir_ordenes_de_suministro_external, Entregar_los_pedidos_external},
    associations={Calcular_Javaaplication, Venta_Producto, Venta_Impuesto, Producto_Impuesto, Clientes_Brindar_Consultoria, Proveedores_Registrar_proveedores, Proveedores_Recibir_productos, Dependencias_Recivir_ordenes_de_suministro, Dependencias_Entregar_los_pedidos, Es_Enviado, Provee, Conforma, Relasiona, Genera, Realiza, Elabora, Factura, Contiene, Asignada_por, Tiene, Tiene1, Ayudan_a, Ayudan_a1, Hace, Hace1, Forma, Contiene1},
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