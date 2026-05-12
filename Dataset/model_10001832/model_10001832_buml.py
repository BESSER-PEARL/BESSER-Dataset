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
Banco_Iniciar_sesi_n_UseCase = Class(name="Banco_Iniciar_sesi_n_UseCase")
Banco_Iniciar_sesi_n_UseCase1 = Class(name="Banco_Iniciar_sesi_n_UseCase1")
Banco_Iniciar_sesi_n_UseCase2 = Class(name="Banco_Iniciar_sesi_n_UseCase2")
Banco_Crear_asesor_UseCase = Class(name="Banco_Crear_asesor_UseCase")
Banco_Crear_cliente_UseCase = Class(name="Banco_Crear_cliente_UseCase")
Banco_Editar_cliente_UseCase = Class(name="Banco_Editar_cliente_UseCase")
Banco_Crear_cuenta_UseCase = Class(name="Banco_Crear_cuenta_UseCase")
Banco_Asociar_cuenta_UseCase = Class(name="Banco_Asociar_cuenta_UseCase")
Banco_Activar_asesor_UseCase = Class(name="Banco_Activar_asesor_UseCase")
Banco_Inactivar_asesor_UseCase = Class(name="Banco_Inactivar_asesor_UseCase")
Banco_Inactivar_cliente_UseCase = Class(name="Banco_Inactivar_cliente_UseCase")
Banco_Activar_cliente_UseCase = Class(name="Banco_Activar_cliente_UseCase")
Banco_Realizar_transacci_n_UseCase = Class(name="Banco_Realizar_transacci_n_UseCase")
Banco_Depositar_UseCase = Class(name="Banco_Depositar_UseCase")
Banco_Retirar_UseCase = Class(name="Banco_Retirar_UseCase")
Banco_Consultar_saldo_UseCase = Class(name="Banco_Consultar_saldo_UseCase")
Banco_Valida_saldo_UseCase = Class(name="Banco_Valida_saldo_UseCase")
Banco_Consulta_datos_cliente_UseCase = Class(name="Banco_Consulta_datos_cliente_UseCase")
Banco_Editar_datos_UseCase = Class(name="Banco_Editar_datos_UseCase")
Gerente_Actor = Class(name="Gerente_Actor")
Asesor_Actor = Class(name="Asesor_Actor")
Cliente_Actor = Class(name="Cliente_Actor")
Cuenta = Class(name="Cuenta")
Class_ = Class(name="Class")
TipoCuenta = Class(name="TipoCuenta")
Cliente = Class(name="Cliente")
Asesor = Class(name="Asesor")
Sucursal = Class(name="Sucursal")
Gerente = Class(name="Gerente")
Transacci_n = Class(name="Transacci_n")
Gerente_Actor1 = Class(name="Gerente_Actor1")
Banco_Iniciar_sesi_n_UseCase3 = Class(name="Banco_Iniciar_sesi_n_UseCase3")
Banco_Crear_asesor_UseCase1 = Class(name="Banco_Crear_asesor_UseCase1")
Banco_Activar_asesor_UseCase1 = Class(name="Banco_Activar_asesor_UseCase1")
Banco_Inactivar_asesor_UseCase1 = Class(name="Banco_Inactivar_asesor_UseCase1")
Asesor_Actor1 = Class(name="Asesor_Actor1")
Banco_Iniciar_sesi_n_UseCase4 = Class(name="Banco_Iniciar_sesi_n_UseCase4")
Banco_Crear_cliente_UseCase1 = Class(name="Banco_Crear_cliente_UseCase1")
Banco_Editar_cliente_UseCase1 = Class(name="Banco_Editar_cliente_UseCase1")
Banco_Crear_cuenta_UseCase1 = Class(name="Banco_Crear_cuenta_UseCase1")
Banco_Asociar_cuenta_UseCase1 = Class(name="Banco_Asociar_cuenta_UseCase1")
Banco_Inactivar_cliente_UseCase1 = Class(name="Banco_Inactivar_cliente_UseCase1")
Banco_Activar_cliente_UseCase1 = Class(name="Banco_Activar_cliente_UseCase1")
Banco_Consulta_datos_cliente_UseCase1 = Class(name="Banco_Consulta_datos_cliente_UseCase1")
Cliente_Actor1 = Class(name="Cliente_Actor1")
Banco_Iniciar_sesi_n_UseCase5 = Class(name="Banco_Iniciar_sesi_n_UseCase5")
Banco_Realizar_transacci_n_UseCase1 = Class(name="Banco_Realizar_transacci_n_UseCase1")
Banco_Depositar_UseCase1 = Class(name="Banco_Depositar_UseCase1")
Banco_Retirar_UseCase1 = Class(name="Banco_Retirar_UseCase1")
Banco_Consultar_saldo_UseCase1 = Class(name="Banco_Consultar_saldo_UseCase1")
Banco_Valida_saldo_UseCase1 = Class(name="Banco_Valida_saldo_UseCase1")
Banco_Editar_datos_UseCase1 = Class(name="Banco_Editar_datos_UseCase1")
Cuenta_external = Class(name="Cuenta_external")

# Banco_Iniciar_sesi_n_UseCase class attributes and methods

# Banco_Iniciar_sesi_n_UseCase1 class attributes and methods

# Banco_Iniciar_sesi_n_UseCase2 class attributes and methods

# Banco_Crear_asesor_UseCase class attributes and methods

# Banco_Crear_cliente_UseCase class attributes and methods

# Banco_Editar_cliente_UseCase class attributes and methods

# Banco_Crear_cuenta_UseCase class attributes and methods

# Banco_Asociar_cuenta_UseCase class attributes and methods

# Banco_Activar_asesor_UseCase class attributes and methods

# Banco_Inactivar_asesor_UseCase class attributes and methods

# Banco_Inactivar_cliente_UseCase class attributes and methods

# Banco_Activar_cliente_UseCase class attributes and methods

# Banco_Realizar_transacci_n_UseCase class attributes and methods

# Banco_Depositar_UseCase class attributes and methods

# Banco_Retirar_UseCase class attributes and methods

# Banco_Consultar_saldo_UseCase class attributes and methods

# Banco_Valida_saldo_UseCase class attributes and methods

# Banco_Consulta_datos_cliente_UseCase class attributes and methods

# Banco_Editar_datos_UseCase class attributes and methods

# Gerente_Actor class attributes and methods

# Asesor_Actor class attributes and methods

# Cliente_Actor class attributes and methods

# Cuenta class attributes and methods
Cuenta_tipoCuenta: Property = Property(name="tipoCuenta", type=StringType)
Cuenta.attributes={Cuenta_tipoCuenta}

# Class class attributes and methods

# TipoCuenta class attributes and methods
TipoCuenta_id: Property = Property(name="id", type=IntegerType)
TipoCuenta_tipo: Property = Property(name="tipo", type=StringType)
TipoCuenta_estado: Property = Property(name="estado", type=BooleanType)
TipoCuenta.attributes={TipoCuenta_id, TipoCuenta_tipo, TipoCuenta_estado}

# Cliente class attributes and methods
Cliente_id: Property = Property(name="id", type=IntegerType)
Cliente_user: Property = Property(name="user", type=StringType)
Cliente_pass: Property = Property(name="pass", type=StringType)
Cliente_telefono: Property = Property(name="telefono", type=IntegerType)
Cliente_celular: Property = Property(name="celular", type=IntegerType)
Cliente_correo: Property = Property(name="correo", type=StringType)
Cliente_foto: Property = Property(name="foto", type=StringType)
Cliente_estado: Property = Property(name="estado", type=BooleanType)
Cliente.attributes={Cliente_user, Cliente_celular, Cliente_estado, Cliente_correo, Cliente_foto, Cliente_id, Cliente_pass, Cliente_telefono}

# Asesor class attributes and methods
Asesor_id: Property = Property(name="id", type=IntegerType)
Asesor_user: Property = Property(name="user", type=StringType)
Asesor_pass: Property = Property(name="pass", type=StringType)
Asesor.attributes={Asesor_id, Asesor_user, Asesor_pass}

# Sucursal class attributes and methods
Sucursal_id: Property = Property(name="id", type=IntegerType)
Sucursal_nombre: Property = Property(name="nombre", type=StringType)
Sucursal.attributes={Sucursal_id, Sucursal_nombre}

# Gerente class attributes and methods
Gerente_id: Property = Property(name="id", type=IntegerType)
Gerente_user: Property = Property(name="user", type=StringType)
Gerente_pass: Property = Property(name="pass", type=StringType)
Gerente.attributes={Gerente_user, Gerente_pass, Gerente_id}

# Transacci_n class attributes and methods
Transacci_n_id: Property = Property(name="id", type=IntegerType)
Transacci_n_fecha: Property = Property(name="fecha", type=DateTimeType)
Transacci_n_detalle: Property = Property(name="detalle", type=StringType)
Transacci_n_monto: Property = Property(name="monto", type=FloatType)
Transacci_n.attributes={Transacci_n_detalle, Transacci_n_monto, Transacci_n_id, Transacci_n_fecha}

# Gerente_Actor1 class attributes and methods

# Banco_Iniciar_sesi_n_UseCase3 class attributes and methods

# Banco_Crear_asesor_UseCase1 class attributes and methods

# Banco_Activar_asesor_UseCase1 class attributes and methods

# Banco_Inactivar_asesor_UseCase1 class attributes and methods

# Asesor_Actor1 class attributes and methods

# Banco_Iniciar_sesi_n_UseCase4 class attributes and methods

# Banco_Crear_cliente_UseCase1 class attributes and methods

# Banco_Editar_cliente_UseCase1 class attributes and methods

# Banco_Crear_cuenta_UseCase1 class attributes and methods

# Banco_Asociar_cuenta_UseCase1 class attributes and methods

# Banco_Inactivar_cliente_UseCase1 class attributes and methods

# Banco_Activar_cliente_UseCase1 class attributes and methods

# Banco_Consulta_datos_cliente_UseCase1 class attributes and methods

# Cliente_Actor1 class attributes and methods

# Banco_Iniciar_sesi_n_UseCase5 class attributes and methods

# Banco_Realizar_transacci_n_UseCase1 class attributes and methods

# Banco_Depositar_UseCase1 class attributes and methods

# Banco_Retirar_UseCase1 class attributes and methods

# Banco_Consultar_saldo_UseCase1 class attributes and methods

# Banco_Valida_saldo_UseCase1 class attributes and methods

# Banco_Editar_datos_UseCase1 class attributes and methods

# Cuenta_external class attributes and methods

# Relationships
Iniciar_sesi_n_Crear_asesor: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Crear_asesor",
    ends={
        Property(name="crear_asesor0", type=Banco_Crear_asesor_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n1", type=Banco_Iniciar_sesi_n_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Crear_cliente: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Crear_cliente",
    ends={
        Property(name="crear_cliente2", type=Banco_Crear_cliente_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n3", type=Banco_Iniciar_sesi_n_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Editar_cliente: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Editar_cliente",
    ends={
        Property(name="editar_cliente4", type=Banco_Editar_cliente_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n5", type=Banco_Iniciar_sesi_n_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Asociar_cuenta: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Asociar_cuenta",
    ends={
        Property(name="asociar_cuenta6", type=Banco_Crear_cuenta_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n7", type=Banco_Iniciar_sesi_n_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Realizar_transacci_n: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Realizar_transacci_n",
    ends={
        Property(name="realizar_transacci_n8", type=Banco_Realizar_transacci_n_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n9", type=Banco_Iniciar_sesi_n_UseCase2, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Consulta_datos_cliente: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Consulta_datos_cliente",
    ends={
        Property(name="consulta_datos_cliente10", type=Banco_Consulta_datos_cliente_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n11", type=Banco_Iniciar_sesi_n_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Editar_datos: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Editar_datos",
    ends={
        Property(name="editar_datos12", type=Banco_Editar_datos_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n13", type=Banco_Iniciar_sesi_n_UseCase2, multiplicity=Multiplicity(0, 1))
    }
)
Gerente_Iniciar_sesi_n: BinaryAssociation = BinaryAssociation(
    name="Gerente_Iniciar_sesi_n",
    ends={
        Property(name="iniciar_sesi_n14", type=Banco_Iniciar_sesi_n_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="gerente15", type=Gerente_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Asesor_Iniciar_sesi_n: BinaryAssociation = BinaryAssociation(
    name="Asesor_Iniciar_sesi_n",
    ends={
        Property(name="iniciar_sesi_n16", type=Banco_Iniciar_sesi_n_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="asesor17", type=Asesor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cliente_Iniciar_sesi_n: BinaryAssociation = BinaryAssociation(
    name="Cliente_Iniciar_sesi_n",
    ends={
        Property(name="iniciar_sesi_n18", type=Banco_Iniciar_sesi_n_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="cliente19", type=Cliente_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Bank_Account_Account_Type: BinaryAssociation = BinaryAssociation(
    name="Bank_Account_Account_Type",
    ends={
        Property(name="tipo_de_cuenta20", type=TipoCuenta, multiplicity=Multiplicity(1, 1)),
        Property(name="cuenta21", type=Cuenta_external, multiplicity=Multiplicity(0, 9999))
    }
)
Bank_Account_Transaction2: BinaryAssociation = BinaryAssociation(
    name="Bank_Account_Transaction2",
    ends={
        Property(name="recibe22", type=Transacci_n, multiplicity=Multiplicity(0, 9999)),
        Property(name="receptor23", type=Cuenta_external, multiplicity=Multiplicity(1, 1))
    }
)
Cliente_Cuenta: BinaryAssociation = BinaryAssociation(
    name="Cliente_Cuenta",
    ends={
        Property(name="tiene24", type=Cuenta_external, multiplicity=Multiplicity(1, 9999)),
        Property(name="cliente25", type=Cliente, multiplicity=Multiplicity(1, 1))
    }
)
Bank_Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Bank_Account_Transaction",
    ends={
        Property(name="realiza26", type=Transacci_n, multiplicity=Multiplicity(0, 9999)),
        Property(name="emisor27", type=Cuenta_external, multiplicity=Multiplicity(1, 1))
    }
)
Gerente_Cliente: BinaryAssociation = BinaryAssociation(
    name="Gerente_Cliente",
    ends={
        Property(name="puede_ser28", type=Cliente, multiplicity=Multiplicity(0, 1)),
        Property(name="gerente29", type=Gerente, multiplicity=Multiplicity(1, 1))
    }
)
Asesor_Cliente: BinaryAssociation = BinaryAssociation(
    name="Asesor_Cliente",
    ends={
        Property(name="puede_ser30", type=Cliente, multiplicity=Multiplicity(0, 1)),
        Property(name="asesor31", type=Asesor, multiplicity=Multiplicity(1, 1))
    }
)
Asesor_Sucursal: BinaryAssociation = BinaryAssociation(
    name="Asesor_Sucursal",
    ends={
        Property(name="sucursal32", type=Sucursal, multiplicity=Multiplicity(1, 1)),
        Property(name="tiene33", type=Asesor, multiplicity=Multiplicity(0, 9999))
    }
)
Sucursal_Gerente: BinaryAssociation = BinaryAssociation(
    name="Sucursal_Gerente",
    ends={
        Property(name="tiene34", type=Gerente, multiplicity=Multiplicity(1, 1)),
        Property(name="sucursal35", type=Sucursal, multiplicity=Multiplicity(1, 1))
    }
)
Iniciar_sesi_n_Crear_asesor1: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Crear_asesor1",
    ends={
        Property(name="crear_asesor36", type=Banco_Crear_asesor_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n37", type=Banco_Iniciar_sesi_n_UseCase3, multiplicity=Multiplicity(0, 1))
    }
)
Gerente_Iniciar_sesi_n2: BinaryAssociation = BinaryAssociation(
    name="Gerente_Iniciar_sesi_n2",
    ends={
        Property(name="iniciar_sesi_n38", type=Banco_Iniciar_sesi_n_UseCase3, multiplicity=Multiplicity(0, 1)),
        Property(name="gerente39", type=Gerente_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Crear_cliente1: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Crear_cliente1",
    ends={
        Property(name="crear_cliente40", type=Banco_Crear_cliente_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n41", type=Banco_Iniciar_sesi_n_UseCase4, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Editar_cliente1: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Editar_cliente1",
    ends={
        Property(name="editar_cliente42", type=Banco_Editar_cliente_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n43", type=Banco_Iniciar_sesi_n_UseCase4, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Asociar_cuenta1: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Asociar_cuenta1",
    ends={
        Property(name="asociar_cuenta44", type=Banco_Crear_cuenta_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n45", type=Banco_Iniciar_sesi_n_UseCase4, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Consulta_datos_cliente1: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Consulta_datos_cliente1",
    ends={
        Property(name="consulta_datos_cliente46", type=Banco_Consulta_datos_cliente_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n47", type=Banco_Iniciar_sesi_n_UseCase4, multiplicity=Multiplicity(0, 1))
    }
)
Asesor_Iniciar_sesi_n2: BinaryAssociation = BinaryAssociation(
    name="Asesor_Iniciar_sesi_n2",
    ends={
        Property(name="iniciar_sesi_n48", type=Banco_Iniciar_sesi_n_UseCase4, multiplicity=Multiplicity(0, 1)),
        Property(name="asesor49", type=Asesor_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Realizar_transacci_n1: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Realizar_transacci_n1",
    ends={
        Property(name="realizar_transacci_n50", type=Banco_Realizar_transacci_n_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n51", type=Banco_Iniciar_sesi_n_UseCase5, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_sesi_n_Editar_datos1: BinaryAssociation = BinaryAssociation(
    name="Iniciar_sesi_n_Editar_datos1",
    ends={
        Property(name="editar_datos52", type=Banco_Editar_datos_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_sesi_n53", type=Banco_Iniciar_sesi_n_UseCase5, multiplicity=Multiplicity(0, 1))
    }
)
Cliente_Iniciar_sesi_n2: BinaryAssociation = BinaryAssociation(
    name="Cliente_Iniciar_sesi_n2",
    ends={
        Property(name="iniciar_sesi_n54", type=Banco_Iniciar_sesi_n_UseCase5, multiplicity=Multiplicity(0, 1)),
        Property(name="cliente55", type=Cliente_Actor1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_YooAUGW0EeiFf_G6LQ_COg",
    types={Banco_Iniciar_sesi_n_UseCase, Banco_Iniciar_sesi_n_UseCase1, Banco_Iniciar_sesi_n_UseCase2, Banco_Crear_asesor_UseCase, Banco_Crear_cliente_UseCase, Banco_Editar_cliente_UseCase, Banco_Crear_cuenta_UseCase, Banco_Asociar_cuenta_UseCase, Banco_Activar_asesor_UseCase, Banco_Inactivar_asesor_UseCase, Banco_Inactivar_cliente_UseCase, Banco_Activar_cliente_UseCase, Banco_Realizar_transacci_n_UseCase, Banco_Depositar_UseCase, Banco_Retirar_UseCase, Banco_Consultar_saldo_UseCase, Banco_Valida_saldo_UseCase, Banco_Consulta_datos_cliente_UseCase, Banco_Editar_datos_UseCase, Gerente_Actor, Asesor_Actor, Cliente_Actor, Cuenta, Class_, TipoCuenta, Cliente, Asesor, Sucursal, Gerente, Transacci_n, Gerente_Actor1, Banco_Iniciar_sesi_n_UseCase3, Banco_Crear_asesor_UseCase1, Banco_Activar_asesor_UseCase1, Banco_Inactivar_asesor_UseCase1, Asesor_Actor1, Banco_Iniciar_sesi_n_UseCase4, Banco_Crear_cliente_UseCase1, Banco_Editar_cliente_UseCase1, Banco_Crear_cuenta_UseCase1, Banco_Asociar_cuenta_UseCase1, Banco_Inactivar_cliente_UseCase1, Banco_Activar_cliente_UseCase1, Banco_Consulta_datos_cliente_UseCase1, Cliente_Actor1, Banco_Iniciar_sesi_n_UseCase5, Banco_Realizar_transacci_n_UseCase1, Banco_Depositar_UseCase1, Banco_Retirar_UseCase1, Banco_Consultar_saldo_UseCase1, Banco_Valida_saldo_UseCase1, Banco_Editar_datos_UseCase1, Cuenta_external},
    associations={Iniciar_sesi_n_Crear_asesor, Iniciar_sesi_n_Crear_cliente, Iniciar_sesi_n_Editar_cliente, Iniciar_sesi_n_Asociar_cuenta, Iniciar_sesi_n_Realizar_transacci_n, Iniciar_sesi_n_Consulta_datos_cliente, Iniciar_sesi_n_Editar_datos, Gerente_Iniciar_sesi_n, Asesor_Iniciar_sesi_n, Cliente_Iniciar_sesi_n, Bank_Account_Account_Type, Bank_Account_Transaction2, Cliente_Cuenta, Bank_Account_Transaction, Gerente_Cliente, Asesor_Cliente, Asesor_Sucursal, Sucursal_Gerente, Iniciar_sesi_n_Crear_asesor1, Gerente_Iniciar_sesi_n2, Iniciar_sesi_n_Crear_cliente1, Iniciar_sesi_n_Editar_cliente1, Iniciar_sesi_n_Asociar_cuenta1, Iniciar_sesi_n_Consulta_datos_cliente1, Asesor_Iniciar_sesi_n2, Iniciar_sesi_n_Realizar_transacci_n1, Iniciar_sesi_n_Editar_datos1, Cliente_Iniciar_sesi_n2},
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