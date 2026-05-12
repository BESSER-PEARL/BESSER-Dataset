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
Brinda_consultoria_external = Class(name="Brinda_consultoria_external")
Mileninum_Component = Class(name="Mileninum_Component")
Departamento_de_contabilidad_y_tesoreria_Actor = Class(name="Departamento_de_contabilidad_y_tesoreria_Actor")
Natural_Actor = Class(name="Natural_Actor")
Juridica_Actor = Class(name="Juridica_Actor")
Departamento_de_Inventarios_y_Suministros___Dis_Component = Class(name="Departamento_de_Inventarios_y_Suministros___Dis_Component")
Proveedores_Actor = Class(name="Proveedores_Actor")
Dependencia_Actor = Class(name="Dependencia_Actor")
Actor_Actor = Class(name="Actor_Actor")
Sistema_WEB_Movil___Recceci_n_de_pedidos_Component = Class(name="Sistema_WEB_Movil___Recceci_n_de_pedidos_Component")
OrdenesPedido = Class(name="OrdenesPedido")
Elementos = Class(name="Elementos")
Proveedores = Class(name="Proveedores")
Dependencia = Class(name="Dependencia")
Factura = Class(name="Factura")
SolucitudSuministro = Class(name="SolucitudSuministro")
Pedidos = Class(name="Pedidos")
Obras = Class(name="Obras")
Planos = Class(name="Planos")
Permisos = Class(name="Permisos")
Trabajadores = Class(name="Trabajadores")
Historial_trabajadores = Class(name="Historial_trabajadores")
Comprador = Class(name="Comprador")
facturas_pagos_ = Class(name="facturas_pagos_")
Encargos = Class(name="Encargos")
Ejecuci_n = Class(name="Ejecuci_n")
PlanosTerreno = Class(name="PlanosTerreno")
Sistema_Electrico = Class(name="Sistema_Electrico")
Sistema_desplegable = Class(name="Sistema_desplegable")
Profesores = Class(name="Profesores")
Departamento = Class(name="Departamento")
_reasConocimiento = Class(name="_reasConocimiento")
Servidor_intel_i8_Node = Class(name="Servidor_intel_i8_Node")
Registrar_proveedores_external = Class(name="Registrar_proveedores_external")
Recibir_productos_y_pedidos_external = Class(name="Recibir_productos_y_pedidos_external")
Recibir_ordenes_de_suministro_external = Class(name="Recibir_ordenes_de_suministro_external")
Generar_ordenes_de_pedidos_external = Class(name="Generar_ordenes_de_pedidos_external")
Clasificar_Producto_external = Class(name="Clasificar_Producto_external")

# Brinda_consultoria_external class attributes and methods

# Mileninum_Component class attributes and methods

# Departamento_de_contabilidad_y_tesoreria_Actor class attributes and methods

# Natural_Actor class attributes and methods

# Juridica_Actor class attributes and methods

# Departamento_de_Inventarios_y_Suministros___Dis_Component class attributes and methods

# Proveedores_Actor class attributes and methods

# Dependencia_Actor class attributes and methods

# Actor_Actor class attributes and methods

# Sistema_WEB_Movil___Recceci_n_de_pedidos_Component class attributes and methods

# OrdenesPedido class attributes and methods
OrdenesPedido_codigo: Property = Property(name="codigo", type=StringType)
OrdenesPedido_fecha: Property = Property(name="fecha", type=StringType)
OrdenesPedido.attributes={OrdenesPedido_codigo, OrdenesPedido_fecha}

# Elementos class attributes and methods
Elementos_referencia: Property = Property(name="referencia", type=StringType)
Elementos_clasificacion: Property = Property(name="clasificacion", type=StringType)
Elementos.attributes={Elementos_referencia, Elementos_clasificacion}

# Proveedores class attributes and methods
Proveedores_nit: Property = Property(name="nit", type=StringType)
Proveedores_razonSocial: Property = Property(name="razonSocial", type=StringType)
Proveedores_direccion: Property = Property(name="direccion", type=StringType)
Proveedores_telefonos: Property = Property(name="telefonos", type=IntegerType)
Proveedores.attributes={Proveedores_telefonos, Proveedores_nit, Proveedores_razonSocial, Proveedores_direccion}

# Dependencia class attributes and methods
Dependencia_codigo: Property = Property(name="codigo", type=StringType)
Dependencia_nombre: Property = Property(name="nombre", type=StringType)
Dependencia_responsable: Property = Property(name="responsable", type=StringType)
Dependencia.attributes={Dependencia_codigo, Dependencia_nombre, Dependencia_responsable}

# Factura class attributes and methods
Factura_codigo: Property = Property(name="codigo", type=StringType)
Factura_fecha: Property = Property(name="fecha", type=StringType)
Factura.attributes={Factura_codigo, Factura_fecha}

# SolucitudSuministro class attributes and methods
SolucitudSuministro_codigo: Property = Property(name="codigo", type=StringType)
SolucitudSuministro_fecha: Property = Property(name="fecha", type=StringType)
SolucitudSuministro.attributes={SolucitudSuministro_fecha, SolucitudSuministro_codigo}

# Pedidos class attributes and methods
Pedidos_codigo: Property = Property(name="codigo", type=StringType)
Pedidos_fecha: Property = Property(name="fecha", type=StringType)
Pedidos.attributes={Pedidos_fecha, Pedidos_codigo}

# Obras class attributes and methods
Obras_codigo: Property = Property(name="codigo", type=StringType)
Obras_direccion: Property = Property(name="direccion", type=StringType)
Obras.attributes={Obras_direccion, Obras_codigo}

# Planos class attributes and methods
Planos_Codigo: Property = Property(name="Codigo", type=StringType)
Planos_Escala: Property = Property(name="Escala", type=StringType)
Planos_Fecha: Property = Property(name="Fecha", type=StringType)
Planos.attributes={Planos_Fecha, Planos_Escala, Planos_Codigo}

# Permisos class attributes and methods
Permisos_Codigo: Property = Property(name="Codigo", type=StringType)
Permisos_Estado: Property = Property(name="Estado", type=StringType)
Permisos_Fecha: Property = Property(name="Fecha", type=StringType)
Permisos.attributes={Permisos_Fecha, Permisos_Estado, Permisos_Codigo}

# Trabajadores class attributes and methods
Trabajadores_identificacion: Property = Property(name="identificacion", type=StringType)
Trabajadores_nombre: Property = Property(name="nombre", type=StringType)
Trabajadores_Telefono: Property = Property(name="Telefono", type=IntegerType)
Trabajadores.attributes={Trabajadores_nombre, Trabajadores_identificacion, Trabajadores_Telefono}

# Historial_trabajadores class attributes and methods
Historial_trabajadores_codigo: Property = Property(name="codigo", type=StringType)
Historial_trabajadores_TrabajoAntiguo: Property = Property(name="TrabajoAntiguo", type=StringType)
Historial_trabajadores_horasTrabajadas: Property = Property(name="horasTrabajadas", type=StringType)
Historial_trabajadores.attributes={Historial_trabajadores_codigo, Historial_trabajadores_horasTrabajadas, Historial_trabajadores_TrabajoAntiguo}

# Comprador class attributes and methods
Comprador_identificacion: Property = Property(name="identificacion", type=StringType)
Comprador_Nombre: Property = Property(name="Nombre", type=StringType)
Comprador_telefono: Property = Property(name="telefono", type=StringType)
Comprador.attributes={Comprador_identificacion, Comprador_Nombre, Comprador_telefono}

# facturas_pagos_ class attributes and methods
facturas_pagos__codigo: Property = Property(name="codigo", type=StringType)
facturas_pagos__total: Property = Property(name="total", type=StringType)
facturas_pagos__pagoNomina: Property = Property(name="pagoNomina", type=IntegerType)
facturas_pagos_.attributes={facturas_pagos__codigo, facturas_pagos__total, facturas_pagos__pagoNomina}

# Encargos class attributes and methods
Encargos_codigo: Property = Property(name="codigo", type=StringType)
Encargos_detalles: Property = Property(name="detalles", type=StringType)
Encargos.attributes={Encargos_detalles, Encargos_codigo}

# Ejecuci_n class attributes and methods
Ejecuci_n_codigo: Property = Property(name="codigo", type=StringType)
Ejecuci_n.attributes={Ejecuci_n_codigo}

# PlanosTerreno class attributes and methods
PlanosTerreno_Ublicacion: Property = Property(name="Ublicacion", type=StringType)
PlanosTerreno.attributes={PlanosTerreno_Ublicacion}

# Sistema_Electrico class attributes and methods
Sistema_Electrico_codigo: Property = Property(name="codigo", type=StringType)
Sistema_Electrico.attributes={Sistema_Electrico_codigo}

# Sistema_desplegable class attributes and methods
Sistema_desplegable_codigo: Property = Property(name="codigo", type=StringType)
Sistema_desplegable.attributes={Sistema_desplegable_codigo}

# Profesores class attributes and methods

# Departamento class attributes and methods

# _reasConocimiento class attributes and methods

# Servidor_intel_i8_Node class attributes and methods

# Registrar_proveedores_external class attributes and methods

# Recibir_productos_y_pedidos_external class attributes and methods

# Recibir_ordenes_de_suministro_external class attributes and methods

# Generar_ordenes_de_pedidos_external class attributes and methods

# Clasificar_Producto_external class attributes and methods

# Relationships
Aciente_Brinda_consultoria: BinaryAssociation = BinaryAssociation(
    name="Aciente_Brinda_consultoria",
    ends={
        Property(name="aciente0", type=Departamento_de_contabilidad_y_tesoreria_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="brinda_consultoria1", type=Brinda_consultoria_external, multiplicity=Multiplicity(0, 1))
    }
)
Registrar_proveedores_Proveedores: BinaryAssociation = BinaryAssociation(
    name="Registrar_proveedores_Proveedores",
    ends={
        Property(name="registrar_proveedores2", type=Registrar_proveedores_external, multiplicity=Multiplicity(0, 1)),
        Property(name="proveedores3", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Recibir_productos_y_pedidos_Proveedores: BinaryAssociation = BinaryAssociation(
    name="Recibir_productos_y_pedidos_Proveedores",
    ends={
        Property(name="recibir_productos_y_pedidos4", type=Recibir_productos_y_pedidos_external, multiplicity=Multiplicity(0, 1)),
        Property(name="proveedores5", type=Proveedores_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dependencia_Generar_ordenes_de_pedidos: BinaryAssociation = BinaryAssociation(
    name="Dependencia_Generar_ordenes_de_pedidos",
    ends={
        Property(name="dependencia6", type=Dependencia_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="generar_ordenes_de_pedidos7", type=Recibir_ordenes_de_suministro_external, multiplicity=Multiplicity(0, 1))
    }
)
Dependencia_Generar_ordenes_de_pedidos_2: BinaryAssociation = BinaryAssociation(
    name="Dependencia_Generar_ordenes_de_pedidos_2",
    ends={
        Property(name="dependencia8", type=Dependencia_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="generar_ordenes_de_pedidos9", type=Generar_ordenes_de_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Departamento_de_contabilidad_y_tesoreria_Recibir_productos_y_pedidos: BinaryAssociation = BinaryAssociation(
    name="Departamento_de_contabilidad_y_tesoreria_Recibir_productos_y_pedidos",
    ends={
        Property(name="departamento_de_contabilidad_y_tesoreria10", type=Departamento_de_contabilidad_y_tesoreria_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="recibir_productos_y_pedidos11", type=Recibir_productos_y_pedidos_external, multiplicity=Multiplicity(0, 1))
    }
)
Actor_Clasificar_Producto: BinaryAssociation = BinaryAssociation(
    name="Actor_Clasificar_Producto",
    ends={
        Property(name="actor12", type=Actor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="clasificar_Producto13", type=Clasificar_Producto_external, multiplicity=Multiplicity(0, 1))
    }
)
es_enviado: BinaryAssociation = BinaryAssociation(
    name="es_enviado",
    ends={
        Property(name="ordenesPedido14", type=OrdenesPedido, multiplicity=Multiplicity(0, 9999)),
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
conformada: BinaryAssociation = BinaryAssociation(
    name="conformada",
    ends={
        Property(name="ordenesPedido18", type=OrdenesPedido, multiplicity=Multiplicity(0, 9999)),
        Property(name="elementos19", type=Elementos, multiplicity=Multiplicity(1, 9999))
    }
)
relaciona: BinaryAssociation = BinaryAssociation(
    name="relaciona",
    ends={
        Property(name="elementos20", type=Elementos, multiplicity=Multiplicity(1, 9999)),
        Property(name="solucitudSuministro21", type=SolucitudSuministro, multiplicity=Multiplicity(0, 1))
    }
)
genera: BinaryAssociation = BinaryAssociation(
    name="genera",
    ends={
        Property(name="solucitudSuministro22", type=SolucitudSuministro, multiplicity=Multiplicity(1, 9999)),
        Property(name="ordenesPedido23", type=OrdenesPedido, multiplicity=Multiplicity(0, 1))
    }
)
elabora: BinaryAssociation = BinaryAssociation(
    name="elabora",
    ends={
        Property(name="factura24", type=Factura, multiplicity=Multiplicity(0, 9999)),
        Property(name="proveedores25", type=Proveedores, multiplicity=Multiplicity(1, 1))
    }
)
Realiza: BinaryAssociation = BinaryAssociation(
    name="Realiza",
    ends={
        Property(name="solucitudSuministro26", type=SolucitudSuministro, multiplicity=Multiplicity(1, 9999)),
        Property(name="dependencia27", type=Dependencia, multiplicity=Multiplicity(1, 1))
    }
)
factura: BinaryAssociation = BinaryAssociation(
    name="factura",
    ends={
        Property(name="factura28", type=Factura, multiplicity=Multiplicity(1, 9999)),
        Property(name="elementos29", type=Elementos, multiplicity=Multiplicity(1, 9999))
    }
)
contiene: BinaryAssociation = BinaryAssociation(
    name="contiene",
    ends={
        Property(name="his_trabajores30", type=Historial_trabajadores, multiplicity=Multiplicity(0, 9999)),
        Property(name="trabajadores31", type=Trabajadores, multiplicity=Multiplicity(1, 1))
    }
)
genera1: BinaryAssociation = BinaryAssociation(
    name="genera1",
    ends={
        Property(name="obras32", type=Obras, multiplicity=Multiplicity(1, 1)),
        Property(name="factura33", type=facturas_pagos_, multiplicity=Multiplicity(0, 9999))
    }
)
nesecita: BinaryAssociation = BinaryAssociation(
    name="nesecita",
    ends={
        Property(name="obras34", type=Obras, multiplicity=Multiplicity(1, 1)),
        Property(name="planos35", type=Planos, multiplicity=Multiplicity(0, 9999))
    }
)
Realiza1: BinaryAssociation = BinaryAssociation(
    name="Realiza1",
    ends={
        Property(name="obras36", type=Obras, multiplicity=Multiplicity(1, 1)),
        Property(name="trabajadores37", type=Trabajadores, multiplicity=Multiplicity(0, 9999))
    }
)
requiere: BinaryAssociation = BinaryAssociation(
    name="requiere",
    ends={
        Property(name="planos38", type=Planos, multiplicity=Multiplicity(1, 1)),
        Property(name="permisos39", type=Permisos, multiplicity=Multiplicity(1, 9999))
    }
)
factura1: BinaryAssociation = BinaryAssociation(
    name="factura1",
    ends={
        Property(name="trabajadores40", type=Trabajadores, multiplicity=Multiplicity(0, 9999)),
        Property(name="factura41", type=facturas_pagos_, multiplicity=Multiplicity(1, 1))
    }
)
hace: BinaryAssociation = BinaryAssociation(
    name="hace",
    ends={
        Property(name="comprador42", type=Comprador, multiplicity=Multiplicity(1, 1)),
        Property(name="encargos43", type=Encargos, multiplicity=Multiplicity(1, 9999))
    }
)
realiza: BinaryAssociation = BinaryAssociation(
    name="realiza",
    ends={
        Property(name="encargos44", type=Encargos, multiplicity=Multiplicity(1, 1)),
        Property(name="obras45", type=Obras, multiplicity=Multiplicity(1, 9999))
    }
)
Departamento__reasConocimiento: BinaryAssociation = BinaryAssociation(
    name="Departamento__reasConocimiento",
    ends={
        Property(name="departamento46", type=Departamento, multiplicity=Multiplicity(1, 1)),
        Property(name="_reasConocimiento47", type=_reasConocimiento, multiplicity=Multiplicity(1, 9999))
    }
)
_reasConocimiento_Profesores: BinaryAssociation = BinaryAssociation(
    name="_reasConocimiento_Profesores",
    ends={
        Property(name="_reasConocimiento48", type=_reasConocimiento, multiplicity=Multiplicity(1, 1)),
        Property(name="profesores49", type=Profesores, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_cAOq8G3dEeqhRdvvYtDJdw",
    types={Brinda_consultoria_external, Mileninum_Component, Departamento_de_contabilidad_y_tesoreria_Actor, Natural_Actor, Juridica_Actor, Departamento_de_Inventarios_y_Suministros___Dis_Component, Proveedores_Actor, Dependencia_Actor, Actor_Actor, Sistema_WEB_Movil___Recceci_n_de_pedidos_Component, OrdenesPedido, Elementos, Proveedores, Dependencia, Factura, SolucitudSuministro, Pedidos, Obras, Planos, Permisos, Trabajadores, Historial_trabajadores, Comprador, facturas_pagos_, Encargos, Ejecuci_n, PlanosTerreno, Sistema_Electrico, Sistema_desplegable, Profesores, Departamento, _reasConocimiento, Servidor_intel_i8_Node, Registrar_proveedores_external, Recibir_productos_y_pedidos_external, Recibir_ordenes_de_suministro_external, Generar_ordenes_de_pedidos_external, Clasificar_Producto_external},
    associations={Aciente_Brinda_consultoria, Registrar_proveedores_Proveedores, Recibir_productos_y_pedidos_Proveedores, Dependencia_Generar_ordenes_de_pedidos, Dependencia_Generar_ordenes_de_pedidos_2, Departamento_de_contabilidad_y_tesoreria_Recibir_productos_y_pedidos, Actor_Clasificar_Producto, es_enviado, Provee, conformada, relaciona, genera, elabora, Realiza, factura, contiene, genera1, nesecita, Realiza1, requiere, factura1, hace, realiza, Departamento__reasConocimiento, _reasConocimiento_Profesores},
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