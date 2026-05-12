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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
Vendedor_Actor = Class(name="Vendedor_Actor")
Comprador_Actor = Class(name="Comprador_Actor")
Responder_consultas_UseCase = Class(name="Responder_consultas_UseCase")
Publicar_producto_UseCase = Class(name="Publicar_producto_UseCase")
Enviar_producto_UseCase = Class(name="Enviar_producto_UseCase")
Ver_consultas_sin_responder_UseCase = Class(name="Ver_consultas_sin_responder_UseCase")
Consultar_producto_UseCase = Class(name="Consultar_producto_UseCase")
Realizar_consulta_UseCase = Class(name="Realizar_consulta_UseCase")
Realizar_pedido_UseCase = Class(name="Realizar_pedido_UseCase")
Instructor_Actor = Class(name="Instructor_Actor")
Cliente_Actor = Class(name="Cliente_Actor")
Registrar_datos_de_clientes_UseCase = Class(name="Registrar_datos_de_clientes_UseCase")
Registrar_datos_de_la_clase_a_la_que_asistir__el_cliente_UseCase = Class(name="Registrar_datos_de_la_clase_a_la_que_asistir__el_cliente_UseCase")
Renovar_inscripci_n_UseCase = Class(name="Renovar_inscripci_n_UseCase")
Consultar_asistencia_historica_UseCase = Class(name="Consultar_asistencia_historica_UseCase")
Inscribir_a_una_clase_UseCase = Class(name="Inscribir_a_una_clase_UseCase")
Consultar_inscripci_n_a_otra_clase_UseCase = Class(name="Consultar_inscripci_n_a_otra_clase_UseCase")
Supervisor_Actor = Class(name="Supervisor_Actor")
Registrar_datos_del_producto_UseCase = Class(name="Registrar_datos_del_producto_UseCase")
Registrar_inicio_de_caja_UseCase = Class(name="Registrar_inicio_de_caja_UseCase")
Registrar_cierre_de_caja_UseCase = Class(name="Registrar_cierre_de_caja_UseCase")
Listar_stock_UseCase = Class(name="Listar_stock_UseCase")
Vender_producto_UseCase = Class(name="Vender_producto_UseCase")
Registrar_venta_UseCase = Class(name="Registrar_venta_UseCase")
Vendedor_Actor1 = Class(name="Vendedor_Actor1")
Articulo = Class(name="Articulo")
Articulo1 = Class(name="Articulo1")
T = Class(name="T")
Articulo2 = Class(name="Articulo2")
Real = Class(name="Real")
real = Class(name="real")
Cliente = Class(name="Cliente")
Pedido = Class(name="Pedido")
Consulta = Class(name="Consulta")
Envio = Class(name="Envio")
Detalle = Class(name="Detalle")
Producto = Class(name="Producto")
Supervisor = Class(name="Supervisor")
Ventas = Class(name="Ventas")
Jornada = Class(name="Jornada")
Caja = Class(name="Caja")
usario = Class(name="usario")
Cliente1 = Class(name="Cliente1")
Asistencia = Class(name="Asistencia")
Clase = Class(name="Clase")
Instructor = Class(name="Instructor")
inscripcion = Class(name="inscripcion")
due_o_Actor = Class(name="due_o_Actor")
consulta_producto_UseCase = Class(name="consulta_producto_UseCase")
consulta_caja_UseCase = Class(name="consulta_caja_UseCase")
consulta_ventas_UseCase = Class(name="consulta_ventas_UseCase")

# Vendedor_Actor class attributes and methods

# Comprador_Actor class attributes and methods

# Responder_consultas_UseCase class attributes and methods

# Publicar_producto_UseCase class attributes and methods

# Enviar_producto_UseCase class attributes and methods

# Ver_consultas_sin_responder_UseCase class attributes and methods

# Consultar_producto_UseCase class attributes and methods

# Realizar_consulta_UseCase class attributes and methods

# Realizar_pedido_UseCase class attributes and methods

# Instructor_Actor class attributes and methods

# Cliente_Actor class attributes and methods

# Registrar_datos_de_clientes_UseCase class attributes and methods

# Registrar_datos_de_la_clase_a_la_que_asistir__el_cliente_UseCase class attributes and methods

# Renovar_inscripci_n_UseCase class attributes and methods

# Consultar_asistencia_historica_UseCase class attributes and methods

# Inscribir_a_una_clase_UseCase class attributes and methods

# Consultar_inscripci_n_a_otra_clase_UseCase class attributes and methods

# Supervisor_Actor class attributes and methods

# Registrar_datos_del_producto_UseCase class attributes and methods

# Registrar_inicio_de_caja_UseCase class attributes and methods

# Registrar_cierre_de_caja_UseCase class attributes and methods

# Listar_stock_UseCase class attributes and methods

# Vender_producto_UseCase class attributes and methods

# Registrar_venta_UseCase class attributes and methods

# Vendedor_Actor1 class attributes and methods

# Articulo class attributes and methods
Articulo_Nombre: Property = Property(name="Nombre", type=StringType)
Articulo.attributes={Articulo_Nombre}

# Articulo1 class attributes and methods

# T class attributes and methods

# Articulo2 class attributes and methods
Articulo2_Descripci_n: Property = Property(name="Descripci_n", type=StringType)
Articulo2_Precio: Property = Property(name="Precio", type=real)
Articulo2_Nombre: Property = Property(name="Nombre", type=StringType)
Articulo2.attributes={Articulo2_Precio, Articulo2_Descripci_n, Articulo2_Nombre}

# Real class attributes and methods

# real class attributes and methods

# Cliente class attributes and methods
Cliente_Nombre: Property = Property(name="Nombre", type=StringType)
Cliente_Apellido: Property = Property(name="Apellido", type=StringType)
Cliente_Direccion: Property = Property(name="Direccion", type=StringType)
Cliente_Email: Property = Property(name="Email", type=StringType)
Cliente.attributes={Cliente_Apellido, Cliente_Email, Cliente_Nombre, Cliente_Direccion}

# Pedido class attributes and methods
Pedido_Numero: Property = Property(name="Numero", type=StringType)
Pedido_Fecha: Property = Property(name="Fecha", type=StringType)
Pedido.attributes={Pedido_Fecha, Pedido_Numero}

# Consulta class attributes and methods
Consulta_Fecha: Property = Property(name="Fecha", type=StringType)
Consulta_Producto: Property = Property(name="Producto", type=StringType)
Consulta.attributes={Consulta_Fecha, Consulta_Producto}

# Envio class attributes and methods
Envio_Fecha: Property = Property(name="Fecha", type=StringType)
Envio_Codigo: Property = Property(name="Codigo", type=StringType)
Envio.attributes={Envio_Fecha, Envio_Codigo}

# Detalle class attributes and methods
Detalle_Cantidad: Property = Property(name="Cantidad", type=StringType)
Detalle_Precio: Property = Property(name="Precio", type=real)
Detalle_Producto: Property = Property(name="Producto", type=StringType)
Detalle.attributes={Detalle_Cantidad, Detalle_Precio, Detalle_Producto}

# Producto class attributes and methods
Producto_Stock: Property = Property(name="Stock", type=StringType)
Producto_Precio: Property = Property(name="Precio", type=real)
Producto_Modo_de_venta: Property = Property(name="Modo_de_venta", type=StringType)
Producto.attributes={Producto_Precio, Producto_Stock, Producto_Modo_de_venta}

# Supervisor class attributes and methods
Supervisor_Clave: Property = Property(name="Clave", type=StringType)
Supervisor.attributes={Supervisor_Clave}

# Ventas class attributes and methods
Ventas_Cantidad: Property = Property(name="Cantidad", type=StringType)
Ventas_Producto: Property = Property(name="Producto", type=StringType)
Ventas_Monto: Property = Property(name="Monto", type=real)
Ventas_Fecha: Property = Property(name="Fecha", type=StringType)
Ventas.attributes={Ventas_Monto, Ventas_Fecha, Ventas_Cantidad, Ventas_Producto}

# Jornada class attributes and methods
Jornada_Stock: Property = Property(name="Stock", type=StringType)
Jornada_Dinero_en_caja: Property = Property(name="Dinero_en_caja", type=real)
Jornada_Arqueo: Property = Property(name="Arqueo", type=real)
Jornada.attributes={Jornada_Arqueo, Jornada_Stock, Jornada_Dinero_en_caja}

# Caja class attributes and methods
Caja_Dinero_Inicio: Property = Property(name="Dinero_Inicio", type=real)
Caja_Arqueo: Property = Property(name="Arqueo", type=Real)
Caja_Fecha: Property = Property(name="Fecha", type=StringType)
Caja_moto_final: Property = Property(name="moto_final", type=Real)
Caja.attributes={Caja_moto_final, Caja_Fecha, Caja_Arqueo, Caja_Dinero_Inicio}

# usario class attributes and methods
usario_nombre: Property = Property(name="nombre", type=StringType)
usario.attributes={usario_nombre}

# Cliente1 class attributes and methods
Cliente1_Nombre: Property = Property(name="Nombre", type=StringType)
Cliente1_Apellido: Property = Property(name="Apellido", type=StringType)
Cliente1_DNI: Property = Property(name="DNI", type=StringType)
Cliente1_Fecha_de_Nac: Property = Property(name="Fecha_de_Nac", type=StringType)
Cliente1_Telefono: Property = Property(name="Telefono", type=StringType)
Cliente1_Email: Property = Property(name="Email", type=StringType)
Cliente1.attributes={Cliente1_Nombre, Cliente1_Apellido, Cliente1_Telefono, Cliente1_Email, Cliente1_DNI, Cliente1_Fecha_de_Nac}

# Asistencia class attributes and methods
Asistencia_Ingreso: Property = Property(name="Ingreso", type=StringType)
Asistencia_Sucursal: Property = Property(name="Sucursal", type=StringType)
Asistencia.attributes={Asistencia_Sucursal, Asistencia_Ingreso}

# Clase class attributes and methods
Clase_Nombre: Property = Property(name="Nombre", type=StringType)
Clase_Asistencia: Property = Property(name="Asistencia", type=StringType)
Clase.attributes={Clase_Asistencia, Clase_Nombre}

# Instructor class attributes and methods
Instructor_Nombre: Property = Property(name="Nombre", type=StringType)
Instructor.attributes={Instructor_Nombre}

# inscripcion class attributes and methods
inscripcion_pago: Property = Property(name="pago", type=Real)
inscripcion_fecha: Property = Property(name="fecha", type=StringType)
inscripcion.attributes={inscripcion_pago, inscripcion_fecha}

# due_o_Actor class attributes and methods

# consulta_producto_UseCase class attributes and methods

# consulta_caja_UseCase class attributes and methods

# consulta_ventas_UseCase class attributes and methods

# Relationships
Vendedor_Responder_consultas: BinaryAssociation = BinaryAssociation(
    name="Vendedor_Responder_consultas",
    ends={
        Property(name="responder_consultas0", type=Responder_consultas_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="vendedor1", type=Vendedor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Vendedor_Publicar_producto: BinaryAssociation = BinaryAssociation(
    name="Vendedor_Publicar_producto",
    ends={
        Property(name="publicar_producto2", type=Publicar_producto_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="vendedor3", type=Vendedor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Vendedor_Enviar_producto: BinaryAssociation = BinaryAssociation(
    name="Vendedor_Enviar_producto",
    ends={
        Property(name="enviar_producto4", type=Enviar_producto_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="vendedor5", type=Vendedor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Consultar_producto_Comprador: BinaryAssociation = BinaryAssociation(
    name="Consultar_producto_Comprador",
    ends={
        Property(name="comprador6", type=Comprador_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="consultar_producto7", type=Consultar_producto_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Realizar_consulta_Comprador: BinaryAssociation = BinaryAssociation(
    name="Realizar_consulta_Comprador",
    ends={
        Property(name="comprador8", type=Comprador_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="realizar_consulta9", type=Realizar_consulta_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Realizar_pedido_Comprador: BinaryAssociation = BinaryAssociation(
    name="Realizar_pedido_Comprador",
    ends={
        Property(name="comprador10", type=Comprador_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="realizar_pedido11", type=Realizar_pedido_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Instructor_Registrar_datos_de_clientes: BinaryAssociation = BinaryAssociation(
    name="Instructor_Registrar_datos_de_clientes",
    ends={
        Property(name="registrar_datos_de_clientes12", type=Registrar_datos_de_clientes_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="instructor13", type=Instructor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Registrar_datos_de_la_clase_a_la_que_asistir__el_cliente_Instructor: BinaryAssociation = BinaryAssociation(
    name="Registrar_datos_de_la_clase_a_la_que_asistir__el_cliente_Instructor",
    ends={
        Property(name="instructor14", type=Instructor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_datos_de_la_clase_a_la_que_asistir__el_cliente15", type=Registrar_datos_de_la_clase_a_la_que_asistir__el_cliente_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Renovar_inscripci_n_Cliente: BinaryAssociation = BinaryAssociation(
    name="Renovar_inscripci_n_Cliente",
    ends={
        Property(name="cliente16", type=Cliente_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="renovar_inscripci_n17", type=Renovar_inscripci_n_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Consultar_asistencia_historica_Cliente: BinaryAssociation = BinaryAssociation(
    name="Consultar_asistencia_historica_Cliente",
    ends={
        Property(name="cliente18", type=Cliente_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="consultar_asistencia_historica19", type=Consultar_asistencia_historica_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Inscribir_a_una_clase_Cliente: BinaryAssociation = BinaryAssociation(
    name="Inscribir_a_una_clase_Cliente",
    ends={
        Property(name="cliente20", type=Instructor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="inscribir_a_una_clase21", type=Inscribir_a_una_clase_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Registrar_datos_del_producto_Supervisor: BinaryAssociation = BinaryAssociation(
    name="Registrar_datos_del_producto_Supervisor",
    ends={
        Property(name="supervisor22", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_datos_del_producto23", type=Registrar_datos_del_producto_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Registrar_inicio_de_caja_Supervisor: BinaryAssociation = BinaryAssociation(
    name="Registrar_inicio_de_caja_Supervisor",
    ends={
        Property(name="supervisor24", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_inicio_de_caja25", type=Registrar_inicio_de_caja_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Registrar_cierre_de_caja_Supervisor: BinaryAssociation = BinaryAssociation(
    name="Registrar_cierre_de_caja_Supervisor",
    ends={
        Property(name="supervisor26", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_cierre_de_caja27", type=Registrar_cierre_de_caja_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Listar_stock_Supervisor: BinaryAssociation = BinaryAssociation(
    name="Listar_stock_Supervisor",
    ends={
        Property(name="supervisor28", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="listar_stock29", type=Listar_stock_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Supervisor_Caja: BinaryAssociation = BinaryAssociation(
    name="Supervisor_Caja",
    ends={
        Property(name="caja50", type=Caja, multiplicity=Multiplicity(1, 9999)),
        Property(name="supervisor51", type=Supervisor, multiplicity=Multiplicity(1, 1))
    }
)
Ventas_Caja: BinaryAssociation = BinaryAssociation(
    name="Ventas_Caja",
    ends={
        Property(name="caja52", type=Caja, multiplicity=Multiplicity(1, 1)),
        Property(name="ventas53", type=Ventas, multiplicity=Multiplicity(1, 9999))
    }
)
Producto_Ventas: BinaryAssociation = BinaryAssociation(
    name="Producto_Ventas",
    ends={
        Property(name="ventas54", type=Ventas, multiplicity=Multiplicity(0, 9999)),
        Property(name="producto55", type=Producto, multiplicity=Multiplicity(1, 1))
    }
)
Jornada_Caja: BinaryAssociation = BinaryAssociation(
    name="Jornada_Caja",
    ends={
        Property(name="caja56", type=Caja, multiplicity=Multiplicity(0, 1)),
        Property(name="jornada57", type=Jornada, multiplicity=Multiplicity(1, 9999))
    }
)
Articulo_Envio: BinaryAssociation = BinaryAssociation(
    name="Articulo_Envio",
    ends={
        Property(name="envio58", type=Envio, multiplicity=Multiplicity(0, 1)),
        Property(name="articulo59", type=Articulo2, multiplicity=Multiplicity(1, 9999))
    }
)
Cliente_Asistencia: BinaryAssociation = BinaryAssociation(
    name="Cliente_Asistencia",
    ends={
        Property(name="asistencia60", type=Asistencia, multiplicity=Multiplicity(1, 9999)),
        Property(name="cliente61", type=Cliente1, multiplicity=Multiplicity(1, 1))
    }
)
Asistencia_Instructor: BinaryAssociation = BinaryAssociation(
    name="Asistencia_Instructor",
    ends={
        Property(name="instructor62", type=Instructor, multiplicity=Multiplicity(1, 1)),
        Property(name="asistencia63", type=Asistencia, multiplicity=Multiplicity(1, 9999))
    }
)
Asistencia_Clase: BinaryAssociation = BinaryAssociation(
    name="Asistencia_Clase",
    ends={
        Property(name="clase64", type=Clase, multiplicity=Multiplicity(1, 1)),
        Property(name="asistencia65", type=Asistencia, multiplicity=Multiplicity(1, 9999))
    }
)
Articulo_Detalle: BinaryAssociation = BinaryAssociation(
    name="Articulo_Detalle",
    ends={
        Property(name="detalle66", type=Detalle, multiplicity=Multiplicity(1, 1)),
        Property(name="articulo67", type=Articulo2, multiplicity=Multiplicity(1, 9999))
    }
)
Cliente_inscripcion: BinaryAssociation = BinaryAssociation(
    name="Cliente_inscripcion",
    ends={
        Property(name="Cliente_inscripcion_068", type=inscripcion, multiplicity=Multiplicity(1, 9999)),
        Property(name="Cliente_inscripcion_169", type=Cliente1, multiplicity=Multiplicity(1, 1))
    }
)
Registrar_venta_Vendedor: BinaryAssociation = BinaryAssociation(
    name="Registrar_venta_Vendedor",
    ends={
        Property(name="vendedor70", type=Vendedor_Actor1, multiplicity=Multiplicity(0, 1)),
        Property(name="registrar_venta71", type=Registrar_venta_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
consulta_producto_due_o: BinaryAssociation = BinaryAssociation(
    name="consulta_producto_due_o",
    ends={
        Property(name="due_o72", type=due_o_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="consulta_producto73", type=consulta_producto_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
consulta_caja_due_o: BinaryAssociation = BinaryAssociation(
    name="consulta_caja_due_o",
    ends={
        Property(name="due_o74", type=due_o_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="consulta_caja75", type=consulta_caja_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
consulta_ventas_due_o: BinaryAssociation = BinaryAssociation(
    name="consulta_ventas_due_o",
    ends={
        Property(name="due_o76", type=due_o_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="consulta_ventas77", type=consulta_ventas_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Vender_producto_Vendedor: BinaryAssociation = BinaryAssociation(
    name="Vender_producto_Vendedor",
    ends={
        Property(name="vendedor30", type=Vendedor_Actor1, multiplicity=Multiplicity(0, 1)),
        Property(name="vender_producto31", type=Vender_producto_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Cliente_Envio: BinaryAssociation = BinaryAssociation(
    name="Cliente_Envio",
    ends={
        Property(name="envio32", type=Envio, multiplicity=Multiplicity(0, 1)),
        Property(name="cliente33", type=Cliente, multiplicity=Multiplicity(0, 1))
    }
)
Articulo_Consulta: BinaryAssociation = BinaryAssociation(
    name="Articulo_Consulta",
    ends={
        Property(name="consulta34", type=Consulta, multiplicity=Multiplicity(1, 9999)),
        Property(name="articulo35", type=Articulo2, multiplicity=Multiplicity(1, 1))
    }
)
Articulo_Cliente: BinaryAssociation = BinaryAssociation(
    name="Articulo_Cliente",
    ends={
        Property(name="Articulo_Cliente_036", type=Cliente, multiplicity=Multiplicity(1, 9999)),
        Property(name="Articulo_Cliente_137", type=Articulo2, multiplicity=Multiplicity(1, 9999))
    }
)
Cliente_Pedido: BinaryAssociation = BinaryAssociation(
    name="Cliente_Pedido",
    ends={
        Property(name="pedido38", type=Pedido, multiplicity=Multiplicity(0, 9999)),
        Property(name="cliente39", type=Cliente, multiplicity=Multiplicity(1, 1))
    }
)
Pedido_Detalle: BinaryAssociation = BinaryAssociation(
    name="Pedido_Detalle",
    ends={
        Property(name="detalle40", type=Detalle, multiplicity=Multiplicity(1, 9999)),
        Property(name="pedido41", type=Pedido, multiplicity=Multiplicity(1, 1))
    }
)
Cliente_Consulta: BinaryAssociation = BinaryAssociation(
    name="Cliente_Consulta",
    ends={
        Property(name="consulta42", type=Consulta, multiplicity=Multiplicity(1, 9999)),
        Property(name="cliente43", type=Cliente, multiplicity=Multiplicity(1, 1))
    }
)
Pedido_Envio: BinaryAssociation = BinaryAssociation(
    name="Pedido_Envio",
    ends={
        Property(name="envio44", type=Envio, multiplicity=Multiplicity(1, 1)),
        Property(name="pedido45", type=Pedido, multiplicity=Multiplicity(1, 1))
    }
)
Producto_Jornada: BinaryAssociation = BinaryAssociation(
    name="Producto_Jornada",
    ends={
        Property(name="jornada46", type=Jornada, multiplicity=Multiplicity(1, 9999)),
        Property(name="producto47", type=Producto, multiplicity=Multiplicity(0, 9999))
    }
)
Jornada_Supervisor: BinaryAssociation = BinaryAssociation(
    name="Jornada_Supervisor",
    ends={
        Property(name="supervisor48", type=Supervisor, multiplicity=Multiplicity(1, 1)),
        Property(name="jornada49", type=Jornada, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_NqL8cNYREemWXYASHrbj8g",
    types={Vendedor_Actor, Comprador_Actor, Responder_consultas_UseCase, Publicar_producto_UseCase, Enviar_producto_UseCase, Ver_consultas_sin_responder_UseCase, Consultar_producto_UseCase, Realizar_consulta_UseCase, Realizar_pedido_UseCase, Instructor_Actor, Cliente_Actor, Registrar_datos_de_clientes_UseCase, Registrar_datos_de_la_clase_a_la_que_asistir__el_cliente_UseCase, Renovar_inscripci_n_UseCase, Consultar_asistencia_historica_UseCase, Inscribir_a_una_clase_UseCase, Consultar_inscripci_n_a_otra_clase_UseCase, Supervisor_Actor, Registrar_datos_del_producto_UseCase, Registrar_inicio_de_caja_UseCase, Registrar_cierre_de_caja_UseCase, Listar_stock_UseCase, Vender_producto_UseCase, Registrar_venta_UseCase, Vendedor_Actor1, Articulo, Articulo1, T, Articulo2, Real, real, Cliente, Pedido, Consulta, Envio, Detalle, Producto, Supervisor, Ventas, Jornada, Caja, usario, Cliente1, Asistencia, Clase, Instructor, inscripcion, due_o_Actor, consulta_producto_UseCase, consulta_caja_UseCase, consulta_ventas_UseCase, Enumeration_},
    associations={Vendedor_Responder_consultas, Vendedor_Publicar_producto, Vendedor_Enviar_producto, Consultar_producto_Comprador, Realizar_consulta_Comprador, Realizar_pedido_Comprador, Instructor_Registrar_datos_de_clientes, Registrar_datos_de_la_clase_a_la_que_asistir__el_cliente_Instructor, Renovar_inscripci_n_Cliente, Consultar_asistencia_historica_Cliente, Inscribir_a_una_clase_Cliente, Registrar_datos_del_producto_Supervisor, Registrar_inicio_de_caja_Supervisor, Registrar_cierre_de_caja_Supervisor, Listar_stock_Supervisor, Supervisor_Caja, Ventas_Caja, Producto_Ventas, Jornada_Caja, Articulo_Envio, Cliente_Asistencia, Asistencia_Instructor, Asistencia_Clase, Articulo_Detalle, Cliente_inscripcion, Registrar_venta_Vendedor, consulta_producto_due_o, consulta_caja_due_o, consulta_ventas_due_o, Vender_producto_Vendedor, Cliente_Envio, Articulo_Consulta, Articulo_Cliente, Cliente_Pedido, Pedido_Detalle, Cliente_Consulta, Pedido_Envio, Producto_Jornada, Jornada_Supervisor},
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