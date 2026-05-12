from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Consulta:

    def __init__(self, data: str, pre_o: str, medico2: "Medico" = None, paciente5: "Paciente" = None):
        self.data = data
        self.pre_o = pre_o
        self.medico2 = medico2
        self.paciente5 = paciente5
        
        pass
    @property
    def pre_o(self):
        return self.__pre_o
    @pre_o.setter
    def pre_o(self, pre_o: str):
        self.__pre_o = pre_o

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def paciente5(self):
        return self.__paciente5
    @paciente5.setter
    def paciente5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__paciente5", None)
        self.__paciente5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta4"):
                opp_val = getattr(old_value, "consulta4", None)
                if opp_val == self:
                    setattr(old_value, "consulta4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta4"):
                opp_val = getattr(value, "consulta4", None)
                setattr(value, "consulta4", self)

    @property
    def medico2(self):
        return self.__medico2
    @medico2.setter
    def medico2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__medico2", None)
        self.__medico2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta3"):
                opp_val = getattr(old_value, "consulta3", None)
                if opp_val == self:
                    setattr(old_value, "consulta3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta3"):
                opp_val = getattr(value, "consulta3", None)
                setattr(value, "consulta3", self)



class Especialidade:

    def __init__(self, descricao: str, medico1: "Medico" = None):
        self.descricao = descricao
        self.medico1 = medico1
        
        pass
    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def medico1(self):
        return self.__medico1
    @medico1.setter
    def medico1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Especialidade__medico1", None)
        self.__medico1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "especialidade0"):
                opp_val = getattr(old_value, "especialidade0", None)
                if opp_val == self:
                    setattr(old_value, "especialidade0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "especialidade0"):
                opp_val = getattr(value, "especialidade0", None)
                setattr(value, "especialidade0", self)



class Paciente:

    def __init__(self, nome: str, celular: str, endere_o: str, consulta4: "Consulta" = None):
        self.nome = nome
        self.celular = celular
        self.endere_o = endere_o
        self.consulta4 = consulta4
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def celular(self):
        return self.__celular
    @celular.setter
    def celular(self, celular: str):
        self.__celular = celular

    @property
    def endere_o(self):
        return self.__endere_o
    @endere_o.setter
    def endere_o(self, endere_o: str):
        self.__endere_o = endere_o

    @property
    def consulta4(self):
        return self.__consulta4
    @consulta4.setter
    def consulta4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Paciente__consulta4", None)
        self.__consulta4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paciente5"):
                opp_val = getattr(old_value, "paciente5", None)
                if opp_val == self:
                    setattr(old_value, "paciente5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paciente5"):
                opp_val = getattr(value, "paciente5", None)
                setattr(value, "paciente5", self)



class Medico:

    def __init__(self, nome: str, endereco: str, crm: str, foto: str, especialidade0: "Especialidade" = None, consulta3: "Consulta" = None):
        self.nome = nome
        self.endereco = endereco
        self.crm = crm
        self.foto = foto
        self.especialidade0 = especialidade0
        self.consulta3 = consulta3
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def foto(self):
        return self.__foto
    @foto.setter
    def foto(self, foto: str):
        self.__foto = foto

    @property
    def crm(self):
        return self.__crm
    @crm.setter
    def crm(self, crm: str):
        self.__crm = crm

    @property
    def especialidade0(self):
        return self.__especialidade0
    @especialidade0.setter
    def especialidade0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medico__especialidade0", None)
        self.__especialidade0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medico1"):
                opp_val = getattr(old_value, "medico1", None)
                if opp_val == self:
                    setattr(old_value, "medico1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medico1"):
                opp_val = getattr(value, "medico1", None)
                setattr(value, "medico1", self)

    @property
    def consulta3(self):
        return self.__consulta3
    @consulta3.setter
    def consulta3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medico__consulta3", None)
        self.__consulta3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medico2"):
                opp_val = getattr(old_value, "medico2", None)
                if opp_val == self:
                    setattr(old_value, "medico2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medico2"):
                opp_val = getattr(value, "medico2", None)
                setattr(value, "medico2", self)

