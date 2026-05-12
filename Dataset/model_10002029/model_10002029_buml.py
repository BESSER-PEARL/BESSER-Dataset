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
DateTime: Enumeration = Enumeration(
    name="DateTime",
    literals={
            
    }
)

# Classes
paciente = Class(name="paciente")
consulta = Class(name="consulta")
doctor = Class(name="doctor")
empleado = Class(name="empleado")
especialidad = Class(name="especialidad")
alergia = Class(name="alergia")
aseguradora = Class(name="aseguradora")
tipoSeguro = Class(name="tipoSeguro")
login = Class(name="login")
historico = Class(name="historico")

# paciente class attributes and methods
paciente_tipoSangre: Property = Property(name="tipoSangre", type=StringType)
paciente_aseguradoID: Property = Property(name="aseguradoID", type=IntegerType)
paciente_pacienteID: Property = Property(name="pacienteID", type=IntegerType)
paciente_apMaterno: Property = Property(name="apMaterno", type=StringType)
paciente_apPaterno: Property = Property(name="apPaterno", type=StringType)
paciente_nombre: Property = Property(name="nombre", type=StringType)
paciente_codigoAsegurado: Property = Property(name="codigoAsegurado", type=StringType)
paciente_fechaAfiliacion: Property = Property(name="fechaAfiliacion", type=DateTime)
paciente_fechaNacimiento: Property = Property(name="fechaNacimiento", type=DateTime)
paciente_nroDocumento: Property = Property(name="nroDocumento", type=IntegerType)
paciente_razonSocial: Property = Property(name="razonSocial", type=StringType)
paciente.attributes={paciente_aseguradoID, paciente_razonSocial, paciente_apMaterno, paciente_fechaNacimiento, paciente_nombre, paciente_pacienteID, paciente_tipoSangre, paciente_nroDocumento, paciente_codigoAsegurado, paciente_apPaterno, paciente_fechaAfiliacion}

# consulta class attributes and methods
consulta_consultaID: Property = Property(name="consultaID", type=IntegerType)
consulta_fechaConsulta: Property = Property(name="fechaConsulta", type=DateTime)
consulta_doctorID: Property = Property(name="doctorID", type=IntegerType)
consulta_empleadoID: Property = Property(name="empleadoID", type=IntegerType)
consulta_pacienteID: Property = Property(name="pacienteID", type=IntegerType)
consulta.attributes={consulta_doctorID, consulta_pacienteID, consulta_consultaID, consulta_empleadoID, consulta_fechaConsulta}

# doctor class attributes and methods
doctor_doctorID: Property = Property(name="doctorID", type=IntegerType)
doctor_apMaterno: Property = Property(name="apMaterno", type=StringType)
doctor_apPaterno: Property = Property(name="apPaterno", type=StringType)
doctor_nombre: Property = Property(name="nombre", type=StringType)
doctor_codigoDoctor: Property = Property(name="codigoDoctor", type=StringType)
doctor_fechaNacimiento: Property = Property(name="fechaNacimiento", type=DateTime)
doctor_nroDocumento: Property = Property(name="nroDocumento", type=IntegerType)
doctor_especialidadID: Property = Property(name="especialidadID", type=IntegerType)
doctor_loginID: Property = Property(name="loginID", type=IntegerType)
doctor.attributes={doctor_doctorID, doctor_especialidadID, doctor_loginID, doctor_nroDocumento, doctor_nombre, doctor_apPaterno, doctor_codigoDoctor, doctor_fechaNacimiento, doctor_apMaterno}

# empleado class attributes and methods
empleado_empleadoID: Property = Property(name="empleadoID", type=IntegerType)
empleado_apMaterno: Property = Property(name="apMaterno", type=StringType)
empleado_apPaterno: Property = Property(name="apPaterno", type=StringType)
empleado_nombre: Property = Property(name="nombre", type=StringType)
empleado_codigoEmpleado: Property = Property(name="codigoEmpleado", type=StringType)
empleado_fechaNacimiento: Property = Property(name="fechaNacimiento", type=DateTime)
empleado_nroDocumento: Property = Property(name="nroDocumento", type=IntegerType)
empleado_loginID: Property = Property(name="loginID", type=IntegerType)
empleado.attributes={empleado_codigoEmpleado, empleado_loginID, empleado_nroDocumento, empleado_apMaterno, empleado_fechaNacimiento, empleado_apPaterno, empleado_nombre, empleado_empleadoID}

# especialidad class attributes and methods
especialidad_especialidadID: Property = Property(name="especialidadID", type=IntegerType)
especialidad_nombre: Property = Property(name="nombre", type=StringType)
especialidad.attributes={especialidad_especialidadID, especialidad_nombre}

# alergia class attributes and methods
alergia_alergiaID: Property = Property(name="alergiaID", type=IntegerType)
alergia_nombre: Property = Property(name="nombre", type=StringType)
alergia.attributes={alergia_alergiaID, alergia_nombre}

# aseguradora class attributes and methods
aseguradora_aseguradoraID: Property = Property(name="aseguradoraID", type=IntegerType)
aseguradora_nombre: Property = Property(name="nombre", type=StringType)
aseguradora_tipoSeguroID: Property = Property(name="tipoSeguroID", type=IntegerType)
aseguradora.attributes={aseguradora_nombre, aseguradora_aseguradoraID, aseguradora_tipoSeguroID}

# tipoSeguro class attributes and methods
tipoSeguro_tipoSeguraID: Property = Property(name="tipoSeguraID", type=IntegerType)
tipoSeguro_descripcion: Property = Property(name="descripcion", type=StringType)
tipoSeguro.attributes={tipoSeguro_descripcion, tipoSeguro_tipoSeguraID}

# login class attributes and methods
login_loginID: Property = Property(name="loginID", type=IntegerType)
login_usuario: Property = Property(name="usuario", type=StringType)
login_contrasena: Property = Property(name="contrasena", type=StringType)
login_role: Property = Property(name="role", type=StringType)
login.attributes={login_contrasena, login_loginID, login_usuario, login_role}

# historico class attributes and methods
historico_historicoID: Property = Property(name="historicoID", type=IntegerType)
historico_sintoma: Property = Property(name="sintoma", type=StringType)
historico_diagnostico: Property = Property(name="diagnostico", type=StringType)
historico_tratamiento: Property = Property(name="tratamiento", type=StringType)
historico_observacion: Property = Property(name="observacion", type=StringType)
historico_consultaID: Property = Property(name="consultaID", type=IntegerType)
historico.attributes={historico_historicoID, historico_observacion, historico_sintoma, historico_consultaID, historico_diagnostico, historico_tratamiento}

# Relationships
doctor_consulta: BinaryAssociation = BinaryAssociation(
    name="doctor_consulta",
    ends={
        Property(name="doctor_consulta_00", type=consulta, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctor_consulta_11", type=doctor, multiplicity=Multiplicity(1, 1))
    }
)
trabajador_consulta: BinaryAssociation = BinaryAssociation(
    name="trabajador_consulta",
    ends={
        Property(name="trabajador_consulta_02", type=consulta, multiplicity=Multiplicity(1, 9999)),
        Property(name="trabajador_consulta_13", type=empleado, multiplicity=Multiplicity(1, 1))
    }
)
especialidad_doctor: BinaryAssociation = BinaryAssociation(
    name="especialidad_doctor",
    ends={
        Property(name="especialidad_doctor_04", type=doctor, multiplicity=Multiplicity(1, 9999)),
        Property(name="especialidad_doctor_15", type=especialidad, multiplicity=Multiplicity(1, 1))
    }
)
aseguradora_paciente: BinaryAssociation = BinaryAssociation(
    name="aseguradora_paciente",
    ends={
        Property(name="aseguradora_paciente_06", type=paciente, multiplicity=Multiplicity(1, 9999)),
        Property(name="aseguradora_paciente_17", type=aseguradora, multiplicity=Multiplicity(1, 1))
    }
)
tipoSeguro_aseguradora: BinaryAssociation = BinaryAssociation(
    name="tipoSeguro_aseguradora",
    ends={
        Property(name="tipoSeguro_aseguradora_08", type=aseguradora, multiplicity=Multiplicity(1, 9999)),
        Property(name="tipoSeguro_aseguradora_19", type=tipoSeguro, multiplicity=Multiplicity(1, 1))
    }
)
paciente_consulta: BinaryAssociation = BinaryAssociation(
    name="paciente_consulta",
    ends={
        Property(name="paciente_consulta_010", type=consulta, multiplicity=Multiplicity(1, 9999)),
        Property(name="paciente_consulta_111", type=paciente, multiplicity=Multiplicity(1, 1))
    }
)
login_doctor: BinaryAssociation = BinaryAssociation(
    name="login_doctor",
    ends={
        Property(name="login_doctor_012", type=doctor, multiplicity=Multiplicity(1, 1)),
        Property(name="login_doctor_113", type=login, multiplicity=Multiplicity(1, 1))
    }
)
login_empleado: BinaryAssociation = BinaryAssociation(
    name="login_empleado",
    ends={
        Property(name="login_empleado_014", type=empleado, multiplicity=Multiplicity(1, 1)),
        Property(name="login_empleado_115", type=login, multiplicity=Multiplicity(1, 1))
    }
)
historico_consulta: BinaryAssociation = BinaryAssociation(
    name="historico_consulta",
    ends={
        Property(name="historico_consulta_016", type=consulta, multiplicity=Multiplicity(1, 1)),
        Property(name="historico_consulta_117", type=historico, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_kh_G0NcIEei47sN0sCkjiA",
    types={paciente, consulta, doctor, empleado, especialidad, alergia, aseguradora, tipoSeguro, login, historico, DateTime},
    associations={doctor_consulta, trabajador_consulta, especialidad_doctor, aseguradora_paciente, tipoSeguro_aseguradora, paciente_consulta, login_doctor, login_empleado, historico_consulta},
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