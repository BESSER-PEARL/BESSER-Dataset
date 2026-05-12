from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DateTime(Enum):
    pass

############################################
# Definition of Classes
############################################










class historico:

    def __init__(self, historicoID: int, sintoma: str, diagnostico: str, tratamiento: str, observacion: str, consultaID: int, historico_consulta_016: "consulta" = None):
        self.historicoID = historicoID
        self.sintoma = sintoma
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.observacion = observacion
        self.consultaID = consultaID
        self.historico_consulta_016 = historico_consulta_016
        
        pass
    @property
    def diagnostico(self):
        return self.__diagnostico
    @diagnostico.setter
    def diagnostico(self, diagnostico: str):
        self.__diagnostico = diagnostico

    @property
    def tratamiento(self):
        return self.__tratamiento
    @tratamiento.setter
    def tratamiento(self, tratamiento: str):
        self.__tratamiento = tratamiento

    @property
    def sintoma(self):
        return self.__sintoma
    @sintoma.setter
    def sintoma(self, sintoma: str):
        self.__sintoma = sintoma

    @property
    def historicoID(self):
        return self.__historicoID
    @historicoID.setter
    def historicoID(self, historicoID: int):
        self.__historicoID = historicoID

    @property
    def observacion(self):
        return self.__observacion
    @observacion.setter
    def observacion(self, observacion: str):
        self.__observacion = observacion

    @property
    def consultaID(self):
        return self.__consultaID
    @consultaID.setter
    def consultaID(self, consultaID: int):
        self.__consultaID = consultaID

    @property
    def historico_consulta_016(self):
        return self.__historico_consulta_016
    @historico_consulta_016.setter
    def historico_consulta_016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_historico__historico_consulta_016", None)
        self.__historico_consulta_016 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "historico_consulta_117"):
                opp_val = getattr(old_value, "historico_consulta_117", None)
                if opp_val == self:
                    setattr(old_value, "historico_consulta_117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "historico_consulta_117"):
                opp_val = getattr(value, "historico_consulta_117", None)
                setattr(value, "historico_consulta_117", self)



class login:

    def __init__(self, loginID: int, usuario: str, contrasena: str, role: str, login_doctor_012: "doctor" = None, login_empleado_014: "empleado" = None):
        self.loginID = loginID
        self.usuario = usuario
        self.contrasena = contrasena
        self.role = role
        self.login_doctor_012 = login_doctor_012
        self.login_empleado_014 = login_empleado_014
        
        pass
    @property
    def loginID(self):
        return self.__loginID
    @loginID.setter
    def loginID(self, loginID: int):
        self.__loginID = loginID

    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self, usuario: str):
        self.__usuario = usuario

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def contrasena(self):
        return self.__contrasena
    @contrasena.setter
    def contrasena(self, contrasena: str):
        self.__contrasena = contrasena

    @property
    def login_doctor_012(self):
        return self.__login_doctor_012
    @login_doctor_012.setter
    def login_doctor_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_login__login_doctor_012", None)
        self.__login_doctor_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login_doctor_113"):
                opp_val = getattr(old_value, "login_doctor_113", None)
                if opp_val == self:
                    setattr(old_value, "login_doctor_113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login_doctor_113"):
                opp_val = getattr(value, "login_doctor_113", None)
                setattr(value, "login_doctor_113", self)

    @property
    def login_empleado_014(self):
        return self.__login_empleado_014
    @login_empleado_014.setter
    def login_empleado_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_login__login_empleado_014", None)
        self.__login_empleado_014 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login_empleado_115"):
                opp_val = getattr(old_value, "login_empleado_115", None)
                if opp_val == self:
                    setattr(old_value, "login_empleado_115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login_empleado_115"):
                opp_val = getattr(value, "login_empleado_115", None)
                setattr(value, "login_empleado_115", self)



class tipoSeguro:

    def __init__(self, tipoSeguraID: int, descripcion: str, tipoSeguro_aseguradora_08: set["aseguradora"] = None):
        self.tipoSeguraID = tipoSeguraID
        self.descripcion = descripcion
        self.tipoSeguro_aseguradora_08 = tipoSeguro_aseguradora_08 if tipoSeguro_aseguradora_08 is not None else set()
        
        pass
    @property
    def tipoSeguraID(self):
        return self.__tipoSeguraID
    @tipoSeguraID.setter
    def tipoSeguraID(self, tipoSeguraID: int):
        self.__tipoSeguraID = tipoSeguraID

    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, descripcion: str):
        self.__descripcion = descripcion

    @property
    def tipoSeguro_aseguradora_08(self):
        return self.__tipoSeguro_aseguradora_08
    @tipoSeguro_aseguradora_08.setter
    def tipoSeguro_aseguradora_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tipoSeguro__tipoSeguro_aseguradora_08", None)
        self.__tipoSeguro_aseguradora_08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tipoSeguro_aseguradora_19"):
                    opp_val = getattr(item, "tipoSeguro_aseguradora_19", None)
                    
                    if opp_val == self:
                        setattr(item, "tipoSeguro_aseguradora_19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tipoSeguro_aseguradora_19"):
                    opp_val = getattr(item, "tipoSeguro_aseguradora_19", None)
                    
                    setattr(item, "tipoSeguro_aseguradora_19", self)
                    



class aseguradora:

    def __init__(self, aseguradoraID: int, nombre: str, tipoSeguroID: int, aseguradora_paciente_06: set["paciente"] = None, tipoSeguro_aseguradora_19: "tipoSeguro" = None):
        self.aseguradoraID = aseguradoraID
        self.nombre = nombre
        self.tipoSeguroID = tipoSeguroID
        self.aseguradora_paciente_06 = aseguradora_paciente_06 if aseguradora_paciente_06 is not None else set()
        self.tipoSeguro_aseguradora_19 = tipoSeguro_aseguradora_19
        
        pass
    @property
    def tipoSeguroID(self):
        return self.__tipoSeguroID
    @tipoSeguroID.setter
    def tipoSeguroID(self, tipoSeguroID: int):
        self.__tipoSeguroID = tipoSeguroID

    @property
    def aseguradoraID(self):
        return self.__aseguradoraID
    @aseguradoraID.setter
    def aseguradoraID(self, aseguradoraID: int):
        self.__aseguradoraID = aseguradoraID

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def aseguradora_paciente_06(self):
        return self.__aseguradora_paciente_06
    @aseguradora_paciente_06.setter
    def aseguradora_paciente_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aseguradora__aseguradora_paciente_06", None)
        self.__aseguradora_paciente_06 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aseguradora_paciente_17"):
                    opp_val = getattr(item, "aseguradora_paciente_17", None)
                    
                    if opp_val == self:
                        setattr(item, "aseguradora_paciente_17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aseguradora_paciente_17"):
                    opp_val = getattr(item, "aseguradora_paciente_17", None)
                    
                    setattr(item, "aseguradora_paciente_17", self)
                    

    @property
    def tipoSeguro_aseguradora_19(self):
        return self.__tipoSeguro_aseguradora_19
    @tipoSeguro_aseguradora_19.setter
    def tipoSeguro_aseguradora_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aseguradora__tipoSeguro_aseguradora_19", None)
        self.__tipoSeguro_aseguradora_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tipoSeguro_aseguradora_08"):
                opp_val = getattr(old_value, "tipoSeguro_aseguradora_08", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tipoSeguro_aseguradora_08"):
                opp_val = getattr(value, "tipoSeguro_aseguradora_08", None)
                if opp_val is None:
                    setattr(value, "tipoSeguro_aseguradora_08", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class alergia:

    def __init__(self, alergiaID: int, nombre: str):
        self.alergiaID = alergiaID
        self.nombre = nombre
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def alergiaID(self):
        return self.__alergiaID
    @alergiaID.setter
    def alergiaID(self, alergiaID: int):
        self.__alergiaID = alergiaID



class especialidad:

    def __init__(self, especialidadID: int, nombre: str, especialidad_doctor_04: set["doctor"] = None):
        self.especialidadID = especialidadID
        self.nombre = nombre
        self.especialidad_doctor_04 = especialidad_doctor_04 if especialidad_doctor_04 is not None else set()
        
        pass
    @property
    def especialidadID(self):
        return self.__especialidadID
    @especialidadID.setter
    def especialidadID(self, especialidadID: int):
        self.__especialidadID = especialidadID

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def especialidad_doctor_04(self):
        return self.__especialidad_doctor_04
    @especialidad_doctor_04.setter
    def especialidad_doctor_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_especialidad__especialidad_doctor_04", None)
        self.__especialidad_doctor_04 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "especialidad_doctor_15"):
                    opp_val = getattr(item, "especialidad_doctor_15", None)
                    
                    if opp_val == self:
                        setattr(item, "especialidad_doctor_15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "especialidad_doctor_15"):
                    opp_val = getattr(item, "especialidad_doctor_15", None)
                    
                    setattr(item, "especialidad_doctor_15", self)
                    



class empleado:

    def __init__(self, empleadoID: int, apMaterno: str, apPaterno: str, nombre: str, codigoEmpleado: str, fechaNacimiento: DateTime, nroDocumento: int, loginID: int, trabajador_consulta_02: set["consulta"] = None, login_empleado_115: "login" = None):
        self.empleadoID = empleadoID
        self.apMaterno = apMaterno
        self.apPaterno = apPaterno
        self.nombre = nombre
        self.codigoEmpleado = codigoEmpleado
        self.fechaNacimiento = fechaNacimiento
        self.nroDocumento = nroDocumento
        self.loginID = loginID
        self.trabajador_consulta_02 = trabajador_consulta_02 if trabajador_consulta_02 is not None else set()
        self.login_empleado_115 = login_empleado_115
        
        pass
    @property
    def apMaterno(self):
        return self.__apMaterno
    @apMaterno.setter
    def apMaterno(self, apMaterno: str):
        self.__apMaterno = apMaterno

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNacimiento: DateTime):
        self.__fechaNacimiento = fechaNacimiento

    @property
    def loginID(self):
        return self.__loginID
    @loginID.setter
    def loginID(self, loginID: int):
        self.__loginID = loginID

    @property
    def codigoEmpleado(self):
        return self.__codigoEmpleado
    @codigoEmpleado.setter
    def codigoEmpleado(self, codigoEmpleado: str):
        self.__codigoEmpleado = codigoEmpleado

    @property
    def nroDocumento(self):
        return self.__nroDocumento
    @nroDocumento.setter
    def nroDocumento(self, nroDocumento: int):
        self.__nroDocumento = nroDocumento

    @property
    def apPaterno(self):
        return self.__apPaterno
    @apPaterno.setter
    def apPaterno(self, apPaterno: str):
        self.__apPaterno = apPaterno

    @property
    def empleadoID(self):
        return self.__empleadoID
    @empleadoID.setter
    def empleadoID(self, empleadoID: int):
        self.__empleadoID = empleadoID

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def login_empleado_115(self):
        return self.__login_empleado_115
    @login_empleado_115.setter
    def login_empleado_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_empleado__login_empleado_115", None)
        self.__login_empleado_115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login_empleado_014"):
                opp_val = getattr(old_value, "login_empleado_014", None)
                if opp_val == self:
                    setattr(old_value, "login_empleado_014", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login_empleado_014"):
                opp_val = getattr(value, "login_empleado_014", None)
                setattr(value, "login_empleado_014", self)

    @property
    def trabajador_consulta_02(self):
        return self.__trabajador_consulta_02
    @trabajador_consulta_02.setter
    def trabajador_consulta_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_empleado__trabajador_consulta_02", None)
        self.__trabajador_consulta_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trabajador_consulta_13"):
                    opp_val = getattr(item, "trabajador_consulta_13", None)
                    
                    if opp_val == self:
                        setattr(item, "trabajador_consulta_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trabajador_consulta_13"):
                    opp_val = getattr(item, "trabajador_consulta_13", None)
                    
                    setattr(item, "trabajador_consulta_13", self)
                    



class doctor:

    def __init__(self, doctorID: int, apMaterno: str, apPaterno: str, nombre: str, codigoDoctor: str, fechaNacimiento: DateTime, nroDocumento: int, especialidadID: int, loginID: int, doctor_consulta_00: set["consulta"] = None, especialidad_doctor_15: "especialidad" = None, login_doctor_113: "login" = None):
        self.doctorID = doctorID
        self.apMaterno = apMaterno
        self.apPaterno = apPaterno
        self.nombre = nombre
        self.codigoDoctor = codigoDoctor
        self.fechaNacimiento = fechaNacimiento
        self.nroDocumento = nroDocumento
        self.especialidadID = especialidadID
        self.loginID = loginID
        self.doctor_consulta_00 = doctor_consulta_00 if doctor_consulta_00 is not None else set()
        self.especialidad_doctor_15 = especialidad_doctor_15
        self.login_doctor_113 = login_doctor_113
        
        pass
    @property
    def apPaterno(self):
        return self.__apPaterno
    @apPaterno.setter
    def apPaterno(self, apPaterno: str):
        self.__apPaterno = apPaterno

    @property
    def loginID(self):
        return self.__loginID
    @loginID.setter
    def loginID(self, loginID: int):
        self.__loginID = loginID

    @property
    def doctorID(self):
        return self.__doctorID
    @doctorID.setter
    def doctorID(self, doctorID: int):
        self.__doctorID = doctorID

    @property
    def especialidadID(self):
        return self.__especialidadID
    @especialidadID.setter
    def especialidadID(self, especialidadID: int):
        self.__especialidadID = especialidadID

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNacimiento: DateTime):
        self.__fechaNacimiento = fechaNacimiento

    @property
    def codigoDoctor(self):
        return self.__codigoDoctor
    @codigoDoctor.setter
    def codigoDoctor(self, codigoDoctor: str):
        self.__codigoDoctor = codigoDoctor

    @property
    def apMaterno(self):
        return self.__apMaterno
    @apMaterno.setter
    def apMaterno(self, apMaterno: str):
        self.__apMaterno = apMaterno

    @property
    def nroDocumento(self):
        return self.__nroDocumento
    @nroDocumento.setter
    def nroDocumento(self, nroDocumento: int):
        self.__nroDocumento = nroDocumento

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def doctor_consulta_00(self):
        return self.__doctor_consulta_00
    @doctor_consulta_00.setter
    def doctor_consulta_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__doctor_consulta_00", None)
        self.__doctor_consulta_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor_consulta_11"):
                    opp_val = getattr(item, "doctor_consulta_11", None)
                    
                    if opp_val == self:
                        setattr(item, "doctor_consulta_11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor_consulta_11"):
                    opp_val = getattr(item, "doctor_consulta_11", None)
                    
                    setattr(item, "doctor_consulta_11", self)
                    

    @property
    def login_doctor_113(self):
        return self.__login_doctor_113
    @login_doctor_113.setter
    def login_doctor_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__login_doctor_113", None)
        self.__login_doctor_113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login_doctor_012"):
                opp_val = getattr(old_value, "login_doctor_012", None)
                if opp_val == self:
                    setattr(old_value, "login_doctor_012", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login_doctor_012"):
                opp_val = getattr(value, "login_doctor_012", None)
                setattr(value, "login_doctor_012", self)

    @property
    def especialidad_doctor_15(self):
        return self.__especialidad_doctor_15
    @especialidad_doctor_15.setter
    def especialidad_doctor_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__especialidad_doctor_15", None)
        self.__especialidad_doctor_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "especialidad_doctor_04"):
                opp_val = getattr(old_value, "especialidad_doctor_04", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "especialidad_doctor_04"):
                opp_val = getattr(value, "especialidad_doctor_04", None)
                if opp_val is None:
                    setattr(value, "especialidad_doctor_04", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class consulta:

    def __init__(self, consultaID: int, fechaConsulta: DateTime, doctorID: int, empleadoID: int, pacienteID: int, doctor_consulta_11: "doctor" = None, trabajador_consulta_13: "empleado" = None, paciente_consulta_111: "paciente" = None, historico_consulta_117: "historico" = None):
        self.consultaID = consultaID
        self.fechaConsulta = fechaConsulta
        self.doctorID = doctorID
        self.empleadoID = empleadoID
        self.pacienteID = pacienteID
        self.doctor_consulta_11 = doctor_consulta_11
        self.trabajador_consulta_13 = trabajador_consulta_13
        self.paciente_consulta_111 = paciente_consulta_111
        self.historico_consulta_117 = historico_consulta_117
        
        pass
    @property
    def consultaID(self):
        return self.__consultaID
    @consultaID.setter
    def consultaID(self, consultaID: int):
        self.__consultaID = consultaID

    @property
    def fechaConsulta(self):
        return self.__fechaConsulta
    @fechaConsulta.setter
    def fechaConsulta(self, fechaConsulta: DateTime):
        self.__fechaConsulta = fechaConsulta

    @property
    def empleadoID(self):
        return self.__empleadoID
    @empleadoID.setter
    def empleadoID(self, empleadoID: int):
        self.__empleadoID = empleadoID

    @property
    def pacienteID(self):
        return self.__pacienteID
    @pacienteID.setter
    def pacienteID(self, pacienteID: int):
        self.__pacienteID = pacienteID

    @property
    def doctorID(self):
        return self.__doctorID
    @doctorID.setter
    def doctorID(self, doctorID: int):
        self.__doctorID = doctorID

    @property
    def doctor_consulta_11(self):
        return self.__doctor_consulta_11
    @doctor_consulta_11.setter
    def doctor_consulta_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_consulta__doctor_consulta_11", None)
        self.__doctor_consulta_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor_consulta_00"):
                opp_val = getattr(old_value, "doctor_consulta_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor_consulta_00"):
                opp_val = getattr(value, "doctor_consulta_00", None)
                if opp_val is None:
                    setattr(value, "doctor_consulta_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def paciente_consulta_111(self):
        return self.__paciente_consulta_111
    @paciente_consulta_111.setter
    def paciente_consulta_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_consulta__paciente_consulta_111", None)
        self.__paciente_consulta_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paciente_consulta_010"):
                opp_val = getattr(old_value, "paciente_consulta_010", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paciente_consulta_010"):
                opp_val = getattr(value, "paciente_consulta_010", None)
                if opp_val is None:
                    setattr(value, "paciente_consulta_010", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trabajador_consulta_13(self):
        return self.__trabajador_consulta_13
    @trabajador_consulta_13.setter
    def trabajador_consulta_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_consulta__trabajador_consulta_13", None)
        self.__trabajador_consulta_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trabajador_consulta_02"):
                opp_val = getattr(old_value, "trabajador_consulta_02", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trabajador_consulta_02"):
                opp_val = getattr(value, "trabajador_consulta_02", None)
                if opp_val is None:
                    setattr(value, "trabajador_consulta_02", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def historico_consulta_117(self):
        return self.__historico_consulta_117
    @historico_consulta_117.setter
    def historico_consulta_117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_consulta__historico_consulta_117", None)
        self.__historico_consulta_117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "historico_consulta_016"):
                opp_val = getattr(old_value, "historico_consulta_016", None)
                if opp_val == self:
                    setattr(old_value, "historico_consulta_016", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "historico_consulta_016"):
                opp_val = getattr(value, "historico_consulta_016", None)
                setattr(value, "historico_consulta_016", self)



class paciente:

    def __init__(self, tipoSangre: str, aseguradoID: int, pacienteID: int, apMaterno: str, apPaterno: str, nombre: str, codigoAsegurado: str, fechaAfiliacion: DateTime, fechaNacimiento: DateTime, nroDocumento: int, razonSocial: str, aseguradora_paciente_17: "aseguradora" = None, paciente_consulta_010: set["consulta"] = None):
        self.tipoSangre = tipoSangre
        self.aseguradoID = aseguradoID
        self.pacienteID = pacienteID
        self.apMaterno = apMaterno
        self.apPaterno = apPaterno
        self.nombre = nombre
        self.codigoAsegurado = codigoAsegurado
        self.fechaAfiliacion = fechaAfiliacion
        self.fechaNacimiento = fechaNacimiento
        self.nroDocumento = nroDocumento
        self.razonSocial = razonSocial
        self.aseguradora_paciente_17 = aseguradora_paciente_17
        self.paciente_consulta_010 = paciente_consulta_010 if paciente_consulta_010 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def pacienteID(self):
        return self.__pacienteID
    @pacienteID.setter
    def pacienteID(self, pacienteID: int):
        self.__pacienteID = pacienteID

    @property
    def nroDocumento(self):
        return self.__nroDocumento
    @nroDocumento.setter
    def nroDocumento(self, nroDocumento: int):
        self.__nroDocumento = nroDocumento

    @property
    def razonSocial(self):
        return self.__razonSocial
    @razonSocial.setter
    def razonSocial(self, razonSocial: str):
        self.__razonSocial = razonSocial

    @property
    def tipoSangre(self):
        return self.__tipoSangre
    @tipoSangre.setter
    def tipoSangre(self, tipoSangre: str):
        self.__tipoSangre = tipoSangre

    @property
    def apPaterno(self):
        return self.__apPaterno
    @apPaterno.setter
    def apPaterno(self, apPaterno: str):
        self.__apPaterno = apPaterno

    @property
    def fechaAfiliacion(self):
        return self.__fechaAfiliacion
    @fechaAfiliacion.setter
    def fechaAfiliacion(self, fechaAfiliacion: DateTime):
        self.__fechaAfiliacion = fechaAfiliacion

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNacimiento: DateTime):
        self.__fechaNacimiento = fechaNacimiento

    @property
    def aseguradoID(self):
        return self.__aseguradoID
    @aseguradoID.setter
    def aseguradoID(self, aseguradoID: int):
        self.__aseguradoID = aseguradoID

    @property
    def codigoAsegurado(self):
        return self.__codigoAsegurado
    @codigoAsegurado.setter
    def codigoAsegurado(self, codigoAsegurado: str):
        self.__codigoAsegurado = codigoAsegurado

    @property
    def apMaterno(self):
        return self.__apMaterno
    @apMaterno.setter
    def apMaterno(self, apMaterno: str):
        self.__apMaterno = apMaterno

    @property
    def paciente_consulta_010(self):
        return self.__paciente_consulta_010
    @paciente_consulta_010.setter
    def paciente_consulta_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paciente__paciente_consulta_010", None)
        self.__paciente_consulta_010 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "paciente_consulta_111"):
                    opp_val = getattr(item, "paciente_consulta_111", None)
                    
                    if opp_val == self:
                        setattr(item, "paciente_consulta_111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "paciente_consulta_111"):
                    opp_val = getattr(item, "paciente_consulta_111", None)
                    
                    setattr(item, "paciente_consulta_111", self)
                    

    @property
    def aseguradora_paciente_17(self):
        return self.__aseguradora_paciente_17
    @aseguradora_paciente_17.setter
    def aseguradora_paciente_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paciente__aseguradora_paciente_17", None)
        self.__aseguradora_paciente_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aseguradora_paciente_06"):
                opp_val = getattr(old_value, "aseguradora_paciente_06", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aseguradora_paciente_06"):
                opp_val = getattr(value, "aseguradora_paciente_06", None)
                if opp_val is None:
                    setattr(value, "aseguradora_paciente_06", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

