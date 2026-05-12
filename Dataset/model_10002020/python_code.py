from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class clinicasaudeperfeita_Consulta_UseCase:

    pass


class clinicasaudeperfeita_Medico_Actor:

    pass


class clinicasaudeperfeita_Marca_consulta_UseCase:

    pass


class clinicasaudeperfeita_Recepcionista_Actor:

    pass


class clinicasaudeperfeita_Analisa_consulta_UseCase:

    pass


class clinicasaudeperfeita_Paciente_Actor:

    pass





class Exame:

    pass


class clinicasaudeperfeita_Medico:

    def __init__(self, nome: str, idade: int, cpf: str, agenda: clinicasaudeperfeita_Compromisso, prescrita2: set["clinicasaudeperfeita_Consulta"] = None, tem5: set["clinicasaudeperfeita_Compromisso"] = None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.agenda = agenda
        self.prescrita2 = prescrita2 if prescrita2 is not None else set()
        self.tem5 = tem5 if tem5 is not None else set()
        
        pass
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def agenda(self):
        return self.__agenda
    @agenda.setter
    def agenda(self, agenda: clinicasaudeperfeita_Compromisso):
        self.__agenda = agenda

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def prescrita2(self):
        return self.__prescrita2
    @prescrita2.setter
    def prescrita2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Medico__prescrita2", None)
        self.__prescrita2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "prescreve3"):
                    opp_val = getattr(item, "prescreve3", None)
                    
                    if opp_val == self:
                        setattr(item, "prescreve3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "prescreve3"):
                    opp_val = getattr(item, "prescreve3", None)
                    
                    setattr(item, "prescreve3", self)
                    

    @property
    def tem5(self):
        return self.__tem5
    @tem5.setter
    def tem5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Medico__tem5", None)
        self.__tem5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "medico4"):
                    opp_val = getattr(item, "medico4", None)
                    
                    if opp_val == self:
                        setattr(item, "medico4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "medico4"):
                    opp_val = getattr(item, "medico4", None)
                    
                    setattr(item, "medico4", self)
                    



class clinicasaudeperfeita_Recepcionista:

    def __init__(self, nome: str, idade: int, cpf: str, consulta10: set["clinicasaudeperfeita_Consulta"] = None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.consulta10 = consulta10 if consulta10 is not None else set()
        
        pass
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def consulta10(self):
        return self.__consulta10
    @consulta10.setter
    def consulta10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Recepcionista__consulta10", None)
        self.__consulta10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "recepcionista11"):
                    opp_val = getattr(item, "recepcionista11", None)
                    
                    if opp_val == self:
                        setattr(item, "recepcionista11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "recepcionista11"):
                    opp_val = getattr(item, "recepcionista11", None)
                    
                    setattr(item, "recepcionista11", self)
                    



class clinicasaudeperfeita_Medicamento:

    def __init__(self, nome: str, consulta6: "clinicasaudeperfeita_Consulta" = None):
        self.nome = nome
        self.consulta6 = consulta6
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def consulta6(self):
        return self.__consulta6
    @consulta6.setter
    def consulta6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Medicamento__consulta6", None)
        self.__consulta6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prescreve7"):
                opp_val = getattr(old_value, "prescreve7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prescreve7"):
                opp_val = getattr(value, "prescreve7", None)
                if opp_val is None:
                    setattr(value, "prescreve7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class clinicasaudeperfeita_Exame:

    def __init__(self, nome: str, consulta8: "clinicasaudeperfeita_Consulta" = None):
        self.nome = nome
        self.consulta8 = consulta8
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def consulta8(self):
        return self.__consulta8
    @consulta8.setter
    def consulta8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Exame__consulta8", None)
        self.__consulta8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicita9"):
                opp_val = getattr(old_value, "solicita9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicita9"):
                opp_val = getattr(value, "solicita9", None)
                if opp_val is None:
                    setattr(value, "solicita9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class clinicasaudeperfeita_Consulta:

    def __init__(self, problemasPaciente: str, orientacoesMedicas: str, medico: clinicasaudeperfeita_Medico, paciente: clinicasaudeperfeita_Paciente, data: str, hora: str, marcada: bool, realizada: bool, medicamentos: clinicasaudeperfeita_Medicamento, exame: Exame, prescreve3: "clinicasaudeperfeita_Medico" = None, prescreve7: set["clinicasaudeperfeita_Medicamento"] = None, solicita9: set["clinicasaudeperfeita_Exame"] = None, recepcionista11: "clinicasaudeperfeita_Recepcionista" = None, consultado1: "clinicasaudeperfeita_Paciente" = None):
        self.problemasPaciente = problemasPaciente
        self.orientacoesMedicas = orientacoesMedicas
        self.medico = medico
        self.paciente = paciente
        self.data = data
        self.hora = hora
        self.marcada = marcada
        self.realizada = realizada
        self.medicamentos = medicamentos
        self.exame = exame
        self.prescreve3 = prescreve3
        self.prescreve7 = prescreve7 if prescreve7 is not None else set()
        self.solicita9 = solicita9 if solicita9 is not None else set()
        self.recepcionista11 = recepcionista11
        self.consultado1 = consultado1
        
        pass
    @property
    def hora(self):
        return self.__hora
    @hora.setter
    def hora(self, hora: str):
        self.__hora = hora

    @property
    def problemasPaciente(self):
        return self.__problemasPaciente
    @problemasPaciente.setter
    def problemasPaciente(self, problemasPaciente: str):
        self.__problemasPaciente = problemasPaciente

    @property
    def medicamentos(self):
        return self.__medicamentos
    @medicamentos.setter
    def medicamentos(self, medicamentos: clinicasaudeperfeita_Medicamento):
        self.__medicamentos = medicamentos

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def realizada(self):
        return self.__realizada
    @realizada.setter
    def realizada(self, realizada: bool):
        self.__realizada = realizada

    @property
    def marcada(self):
        return self.__marcada
    @marcada.setter
    def marcada(self, marcada: bool):
        self.__marcada = marcada

    @property
    def orientacoesMedicas(self):
        return self.__orientacoesMedicas
    @orientacoesMedicas.setter
    def orientacoesMedicas(self, orientacoesMedicas: str):
        self.__orientacoesMedicas = orientacoesMedicas

    @property
    def exame(self):
        return self.__exame
    @exame.setter
    def exame(self, exame: Exame):
        self.__exame = exame

    @property
    def paciente(self):
        return self.__paciente
    @paciente.setter
    def paciente(self, paciente: clinicasaudeperfeita_Paciente):
        self.__paciente = paciente

    @property
    def medico(self):
        return self.__medico
    @medico.setter
    def medico(self, medico: clinicasaudeperfeita_Medico):
        self.__medico = medico

    @property
    def recepcionista11(self):
        return self.__recepcionista11
    @recepcionista11.setter
    def recepcionista11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Consulta__recepcionista11", None)
        self.__recepcionista11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta10"):
                opp_val = getattr(old_value, "consulta10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta10"):
                opp_val = getattr(value, "consulta10", None)
                if opp_val is None:
                    setattr(value, "consulta10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def consultado1(self):
        return self.__consultado1
    @consultado1.setter
    def consultado1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Consulta__consultado1", None)
        self.__consultado1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "__consultado0"):
                opp_val = getattr(old_value, "__consultado0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "__consultado0"):
                opp_val = getattr(value, "__consultado0", None)
                if opp_val is None:
                    setattr(value, "__consultado0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def prescreve7(self):
        return self.__prescreve7
    @prescreve7.setter
    def prescreve7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Consulta__prescreve7", None)
        self.__prescreve7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "consulta6"):
                    opp_val = getattr(item, "consulta6", None)
                    
                    if opp_val == self:
                        setattr(item, "consulta6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "consulta6"):
                    opp_val = getattr(item, "consulta6", None)
                    
                    setattr(item, "consulta6", self)
                    

    @property
    def prescreve3(self):
        return self.__prescreve3
    @prescreve3.setter
    def prescreve3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Consulta__prescreve3", None)
        self.__prescreve3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prescrita2"):
                opp_val = getattr(old_value, "prescrita2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prescrita2"):
                opp_val = getattr(value, "prescrita2", None)
                if opp_val is None:
                    setattr(value, "prescrita2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def solicita9(self):
        return self.__solicita9
    @solicita9.setter
    def solicita9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Consulta__solicita9", None)
        self.__solicita9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "consulta8"):
                    opp_val = getattr(item, "consulta8", None)
                    
                    if opp_val == self:
                        setattr(item, "consulta8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "consulta8"):
                    opp_val = getattr(item, "consulta8", None)
                    
                    setattr(item, "consulta8", self)
                    



class clinicasaudeperfeita_Compromisso:

    def __init__(self, descricao: str, data: str, hora: str, medico4: "clinicasaudeperfeita_Medico" = None):
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.medico4 = medico4
        
        pass
    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def hora(self):
        return self.__hora
    @hora.setter
    def hora(self, hora: str):
        self.__hora = hora

    @property
    def medico4(self):
        return self.__medico4
    @medico4.setter
    def medico4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Compromisso__medico4", None)
        self.__medico4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tem5"):
                opp_val = getattr(old_value, "tem5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tem5"):
                opp_val = getattr(value, "tem5", None)
                if opp_val is None:
                    setattr(value, "tem5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class clinicasaudeperfeita_Paciente:

    def __init__(self, nome: str, idade: int, cpf: str, cSus: str, __consultado0: set["clinicasaudeperfeita_Consulta"] = None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cSus = cSus
        self.__consultado0 = __consultado0 if __consultado0 is not None else set()
        
        pass
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    @property
    def cSus(self):
        return self.__cSus
    @cSus.setter
    def cSus(self, cSus: str):
        self.__cSus = cSus

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def __consultado0(self):
        return self.____consultado0
    @__consultado0.setter
    def __consultado0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinicasaudeperfeita_Paciente____consultado0", None)
        self.____consultado0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "consultado1"):
                    opp_val = getattr(item, "consultado1", None)
                    
                    if opp_val == self:
                        setattr(item, "consultado1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "consultado1"):
                    opp_val = getattr(item, "consultado1", None)
                    
                    setattr(item, "consultado1", self)
                    

