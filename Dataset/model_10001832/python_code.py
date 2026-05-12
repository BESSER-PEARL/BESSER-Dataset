from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Cliente_Actor:

    pass


class Asesor_Actor:

    pass


class Gerente_Actor:

    pass


class Banco_Editar_datos_UseCase:

    pass


class Banco_Consulta_datos_cliente_UseCase:

    pass


class Banco_Valida_saldo_UseCase:

    pass


class Banco_Consultar_saldo_UseCase:

    pass


class Banco_Retirar_UseCase:

    pass


class Banco_Depositar_UseCase:

    pass


class Banco_Realizar_transacci_n_UseCase:

    pass


class Banco_Activar_cliente_UseCase:

    pass


class Banco_Inactivar_cliente_UseCase:

    pass


class Banco_Inactivar_asesor_UseCase:

    pass


class Banco_Activar_asesor_UseCase:

    pass


class Banco_Asociar_cuenta_UseCase:

    pass


class Banco_Crear_cuenta_UseCase:

    pass


class Banco_Editar_cliente_UseCase:

    pass


class Banco_Crear_cliente_UseCase:

    pass


class Banco_Crear_asesor_UseCase:

    pass


class Banco_Iniciar_sesi_n_UseCase:

    pass





class Banco_Editar_datos_UseCase1:

    pass


class Banco_Valida_saldo_UseCase1:

    pass


class Banco_Consultar_saldo_UseCase1:

    pass


class Banco_Retirar_UseCase1:

    pass


class Banco_Depositar_UseCase1:

    pass


class Banco_Realizar_transacci_n_UseCase1:

    pass


class Banco_Iniciar_sesi_n_UseCase5:

    pass


class Cliente_Actor1:

    pass


class Banco_Consulta_datos_cliente_UseCase1:

    pass


class Banco_Activar_cliente_UseCase1:

    pass


class Banco_Inactivar_cliente_UseCase1:

    pass


class Banco_Asociar_cuenta_UseCase1:

    pass


class Banco_Crear_cuenta_UseCase1:

    pass


class Banco_Editar_cliente_UseCase1:

    pass


class Banco_Crear_cliente_UseCase1:

    pass


class Banco_Iniciar_sesi_n_UseCase4:

    pass


class Asesor_Actor1:

    pass


class Banco_Inactivar_asesor_UseCase1:

    pass


class Banco_Activar_asesor_UseCase1:

    pass


class Banco_Crear_asesor_UseCase1:

    pass


class Banco_Iniciar_sesi_n_UseCase3:

    pass


class Gerente_Actor1:

    pass


class Transacci_n:

    def __init__(self, id: int, fecha: datetime, detalle: str, monto: float, receptor23: "Cuenta_external" = None, emisor27: "Cuenta_external" = None):
        self.id = id
        self.fecha = fecha
        self.detalle = detalle
        self.monto = monto
        self.receptor23 = receptor23
        self.emisor27 = emisor27
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def monto(self):
        return self.__monto
    @monto.setter
    def monto(self, monto: float):
        self.__monto = monto

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha: datetime):
        self.__fecha = fecha

    @property
    def detalle(self):
        return self.__detalle
    @detalle.setter
    def detalle(self, detalle: str):
        self.__detalle = detalle

    @property
    def receptor23(self):
        return self.__receptor23
    @receptor23.setter
    def receptor23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transacci_n__receptor23", None)
        self.__receptor23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recibe22"):
                opp_val = getattr(old_value, "recibe22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recibe22"):
                opp_val = getattr(value, "recibe22", None)
                if opp_val is None:
                    setattr(value, "recibe22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def emisor27(self):
        return self.__emisor27
    @emisor27.setter
    def emisor27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transacci_n__emisor27", None)
        self.__emisor27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "realiza26"):
                opp_val = getattr(old_value, "realiza26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "realiza26"):
                opp_val = getattr(value, "realiza26", None)
                if opp_val is None:
                    setattr(value, "realiza26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Gerente:

    def __init__(self, id: int, user: str, pass1: str, puede_ser28: "Cliente" = None, sucursal35: "Sucursal" = None):
        self.id = id
        self.user = user
        self.pass1 = pass1
        self.puede_ser28 = puede_ser28
        self.sucursal35 = sucursal35
        
        pass
    @property
    def pass1(self):
        return self.__pass1
    @pass1.setter
    def pass1(self, pass1: str):
        self.__pass1 = pass1

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def puede_ser28(self):
        return self.__puede_ser28
    @puede_ser28.setter
    def puede_ser28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Gerente__puede_ser28", None)
        self.__puede_ser28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gerente29"):
                opp_val = getattr(old_value, "gerente29", None)
                if opp_val == self:
                    setattr(old_value, "gerente29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gerente29"):
                opp_val = getattr(value, "gerente29", None)
                setattr(value, "gerente29", self)

    @property
    def sucursal35(self):
        return self.__sucursal35
    @sucursal35.setter
    def sucursal35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Gerente__sucursal35", None)
        self.__sucursal35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tiene34"):
                opp_val = getattr(old_value, "tiene34", None)
                if opp_val == self:
                    setattr(old_value, "tiene34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tiene34"):
                opp_val = getattr(value, "tiene34", None)
                setattr(value, "tiene34", self)



class Sucursal:

    def __init__(self, id: int, nombre: str, tiene33: set["Asesor"] = None, tiene34: "Gerente" = None):
        self.id = id
        self.nombre = nombre
        self.tiene33 = tiene33 if tiene33 is not None else set()
        self.tiene34 = tiene34
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def tiene34(self):
        return self.__tiene34
    @tiene34.setter
    def tiene34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sucursal__tiene34", None)
        self.__tiene34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sucursal35"):
                opp_val = getattr(old_value, "sucursal35", None)
                if opp_val == self:
                    setattr(old_value, "sucursal35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sucursal35"):
                opp_val = getattr(value, "sucursal35", None)
                setattr(value, "sucursal35", self)

    @property
    def tiene33(self):
        return self.__tiene33
    @tiene33.setter
    def tiene33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sucursal__tiene33", None)
        self.__tiene33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sucursal32"):
                    opp_val = getattr(item, "sucursal32", None)
                    
                    if opp_val == self:
                        setattr(item, "sucursal32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sucursal32"):
                    opp_val = getattr(item, "sucursal32", None)
                    
                    setattr(item, "sucursal32", self)
                    



class Asesor:

    def __init__(self, id: int, user: str, pass1: str, puede_ser30: "Cliente" = None, sucursal32: "Sucursal" = None):
        self.id = id
        self.user = user
        self.pass1 = pass1
        self.puede_ser30 = puede_ser30
        self.sucursal32 = sucursal32
        
        pass
    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def pass1(self):
        return self.__pass1
    @pass1.setter
    def pass1(self, pass1: str):
        self.__pass1 = pass1

    @property
    def sucursal32(self):
        return self.__sucursal32
    @sucursal32.setter
    def sucursal32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Asesor__sucursal32", None)
        self.__sucursal32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tiene33"):
                opp_val = getattr(old_value, "tiene33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tiene33"):
                opp_val = getattr(value, "tiene33", None)
                if opp_val is None:
                    setattr(value, "tiene33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def puede_ser30(self):
        return self.__puede_ser30
    @puede_ser30.setter
    def puede_ser30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Asesor__puede_ser30", None)
        self.__puede_ser30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "asesor31"):
                opp_val = getattr(old_value, "asesor31", None)
                if opp_val == self:
                    setattr(old_value, "asesor31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "asesor31"):
                opp_val = getattr(value, "asesor31", None)
                setattr(value, "asesor31", self)



class Cliente:

    def __init__(self, id: int, user: str, pass1: str, telefono: int, celular: int, correo: str, foto: str, estado: bool, tiene24: set["Cuenta_external"] = None, gerente29: "Gerente" = None, asesor31: "Asesor" = None):
        self.id = id
        self.user = user
        self.pass1 = pass1
        self.telefono = telefono
        self.celular = celular
        self.correo = correo
        self.foto = foto
        self.estado = estado
        self.tiene24 = tiene24 if tiene24 is not None else set()
        self.gerente29 = gerente29
        self.asesor31 = asesor31
        
        pass
    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self, correo: str):
        self.__correo = correo

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado: bool):
        self.__estado = estado

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono: int):
        self.__telefono = telefono

    @property
    def celular(self):
        return self.__celular
    @celular.setter
    def celular(self, celular: int):
        self.__celular = celular

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def pass1(self):
        return self.__pass1
    @pass1.setter
    def pass1(self, pass1: str):
        self.__pass1 = pass1

    @property
    def foto(self):
        return self.__foto
    @foto.setter
    def foto(self, foto: str):
        self.__foto = foto

    @property
    def tiene24(self):
        return self.__tiene24
    @tiene24.setter
    def tiene24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__tiene24", None)
        self.__tiene24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cliente25"):
                    opp_val = getattr(item, "cliente25", None)
                    
                    if opp_val == self:
                        setattr(item, "cliente25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cliente25"):
                    opp_val = getattr(item, "cliente25", None)
                    
                    setattr(item, "cliente25", self)
                    

    @property
    def gerente29(self):
        return self.__gerente29
    @gerente29.setter
    def gerente29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__gerente29", None)
        self.__gerente29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "puede_ser28"):
                opp_val = getattr(old_value, "puede_ser28", None)
                if opp_val == self:
                    setattr(old_value, "puede_ser28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "puede_ser28"):
                opp_val = getattr(value, "puede_ser28", None)
                setattr(value, "puede_ser28", self)

    @property
    def asesor31(self):
        return self.__asesor31
    @asesor31.setter
    def asesor31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__asesor31", None)
        self.__asesor31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "puede_ser30"):
                opp_val = getattr(old_value, "puede_ser30", None)
                if opp_val == self:
                    setattr(old_value, "puede_ser30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "puede_ser30"):
                opp_val = getattr(value, "puede_ser30", None)
                setattr(value, "puede_ser30", self)



class TipoCuenta:

    def __init__(self, id: int, tipo: str, estado: bool, cuenta21: set["Cuenta_external"] = None):
        self.id = id
        self.tipo = tipo
        self.estado = estado
        self.cuenta21 = cuenta21 if cuenta21 is not None else set()
        
        pass
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado: bool):
        self.__estado = estado

    @property
    def cuenta21(self):
        return self.__cuenta21
    @cuenta21.setter
    def cuenta21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TipoCuenta__cuenta21", None)
        self.__cuenta21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tipo_de_cuenta20"):
                    opp_val = getattr(item, "tipo_de_cuenta20", None)
                    
                    if opp_val == self:
                        setattr(item, "tipo_de_cuenta20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tipo_de_cuenta20"):
                    opp_val = getattr(item, "tipo_de_cuenta20", None)
                    
                    setattr(item, "tipo_de_cuenta20", self)
                    



class Class:

    pass


class Cuenta:

    def __init__(self, tipoCuenta: str):
        self.tipoCuenta = tipoCuenta
        
        pass
    @property
    def tipoCuenta(self):
        return self.__tipoCuenta
    @tipoCuenta.setter
    def tipoCuenta(self, tipoCuenta: str):
        self.__tipoCuenta = tipoCuenta



class Banco_Iniciar_sesi_n_UseCase2:

    pass


class Cuenta_external:

    pass


class Banco_Iniciar_sesi_n_UseCase1:

    pass
