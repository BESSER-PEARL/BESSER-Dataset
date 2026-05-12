from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class M_dico:

    def __init__(self, Nome: str, Especialidade: str, CPF: int):
        self.Nome = Nome
        self.Especialidade = Especialidade
        self.CPF = CPF
        
        pass
    @property
    def Especialidade(self):
        return self.__Especialidade
    @Especialidade.setter
    def Especialidade(self, Especialidade: str):
        self.__Especialidade = Especialidade

    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def CPF(self):
        return self.__CPF
    @CPF.setter
    def CPF(self, CPF: int):
        self.__CPF = CPF



class Agendamento:

    def __init__(self, TipoAgendamento: str, Especialista: str, Sede: str, Medico: str, Dia_e_Horario: str, exame0: "Exame" = None, consulta2: "Consulta" = None):
        self.TipoAgendamento = TipoAgendamento
        self.Especialista = Especialista
        self.Sede = Sede
        self.Medico = Medico
        self.Dia_e_Horario = Dia_e_Horario
        self.exame0 = exame0
        self.consulta2 = consulta2
        
        pass
    @property
    def TipoAgendamento(self):
        return self.__TipoAgendamento
    @TipoAgendamento.setter
    def TipoAgendamento(self, TipoAgendamento: str):
        self.__TipoAgendamento = TipoAgendamento

    @property
    def Medico(self):
        return self.__Medico
    @Medico.setter
    def Medico(self, Medico: str):
        self.__Medico = Medico

    @property
    def Especialista(self):
        return self.__Especialista
    @Especialista.setter
    def Especialista(self, Especialista: str):
        self.__Especialista = Especialista

    @property
    def Sede(self):
        return self.__Sede
    @Sede.setter
    def Sede(self, Sede: str):
        self.__Sede = Sede

    @property
    def Dia_e_Horario(self):
        return self.__Dia_e_Horario
    @Dia_e_Horario.setter
    def Dia_e_Horario(self, Dia_e_Horario: str):
        self.__Dia_e_Horario = Dia_e_Horario

    @property
    def exame0(self):
        return self.__exame0
    @exame0.setter
    def exame0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Agendamento__exame0", None)
        self.__exame0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agendamento1"):
                opp_val = getattr(old_value, "agendamento1", None)
                if opp_val == self:
                    setattr(old_value, "agendamento1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agendamento1"):
                opp_val = getattr(value, "agendamento1", None)
                setattr(value, "agendamento1", self)

    @property
    def consulta2(self):
        return self.__consulta2
    @consulta2.setter
    def consulta2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Agendamento__consulta2", None)
        self.__consulta2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agendamento3"):
                opp_val = getattr(old_value, "agendamento3", None)
                if opp_val == self:
                    setattr(old_value, "agendamento3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agendamento3"):
                opp_val = getattr(value, "agendamento3", None)
                setattr(value, "agendamento3", self)



class Funcion_rio:

    def __init__(self, Usuario: str, Senha: str):
        self.Usuario = Usuario
        self.Senha = Senha
        
        pass
    @property
    def Senha(self):
        return self.__Senha
    @Senha.setter
    def Senha(self, Senha: str):
        self.__Senha = Senha

    @property
    def Usuario(self):
        return self.__Usuario
    @Usuario.setter
    def Usuario(self, Usuario: str):
        self.__Usuario = Usuario



class Consulta:

    def __init__(self, TipoConsulta: str, Especialista: str, Medico: str, Sede: str, agendamento3: "Agendamento" = None):
        self.TipoConsulta = TipoConsulta
        self.Especialista = Especialista
        self.Medico = Medico
        self.Sede = Sede
        self.agendamento3 = agendamento3
        
        pass
    @property
    def Medico(self):
        return self.__Medico
    @Medico.setter
    def Medico(self, Medico: str):
        self.__Medico = Medico

    @property
    def TipoConsulta(self):
        return self.__TipoConsulta
    @TipoConsulta.setter
    def TipoConsulta(self, TipoConsulta: str):
        self.__TipoConsulta = TipoConsulta

    @property
    def Especialista(self):
        return self.__Especialista
    @Especialista.setter
    def Especialista(self, Especialista: str):
        self.__Especialista = Especialista

    @property
    def Sede(self):
        return self.__Sede
    @Sede.setter
    def Sede(self, Sede: str):
        self.__Sede = Sede

    @property
    def agendamento3(self):
        return self.__agendamento3
    @agendamento3.setter
    def agendamento3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__agendamento3", None)
        self.__agendamento3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta2"):
                opp_val = getattr(old_value, "consulta2", None)
                if opp_val == self:
                    setattr(old_value, "consulta2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta2"):
                opp_val = getattr(value, "consulta2", None)
                setattr(value, "consulta2", self)



class Paciente:

    def __init__(self, CPF: Paciente, Nome: str, Sobrenome: str, DataNascimento: str, CPF1: int, RG: int, Nacionalidade: str, Estado: str, Cidade: str, CEP: int, Endereco: str, Sexo: str, EstadoCivil: str, Telefone: int, Celular: int, Email: str, ConvenioMedico: str):
        self.CPF = CPF
        self.Nome = Nome
        self.Sobrenome = Sobrenome
        self.DataNascimento = DataNascimento
        self.CPF1 = CPF1
        self.RG = RG
        self.Nacionalidade = Nacionalidade
        self.Estado = Estado
        self.Cidade = Cidade
        self.CEP = CEP
        self.Endereco = Endereco
        self.Sexo = Sexo
        self.EstadoCivil = EstadoCivil
        self.Telefone = Telefone
        self.Celular = Celular
        self.Email = Email
        self.ConvenioMedico = ConvenioMedico
        
        pass
    @property
    def Cidade(self):
        return self.__Cidade
    @Cidade.setter
    def Cidade(self, Cidade: str):
        self.__Cidade = Cidade

    @property
    def ConvenioMedico(self):
        return self.__ConvenioMedico
    @ConvenioMedico.setter
    def ConvenioMedico(self, ConvenioMedico: str):
        self.__ConvenioMedico = ConvenioMedico

    @property
    def Nacionalidade(self):
        return self.__Nacionalidade
    @Nacionalidade.setter
    def Nacionalidade(self, Nacionalidade: str):
        self.__Nacionalidade = Nacionalidade

    @property
    def Estado(self):
        return self.__Estado
    @Estado.setter
    def Estado(self, Estado: str):
        self.__Estado = Estado

    @property
    def EstadoCivil(self):
        return self.__EstadoCivil
    @EstadoCivil.setter
    def EstadoCivil(self, EstadoCivil: str):
        self.__EstadoCivil = EstadoCivil

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Endereco(self):
        return self.__Endereco
    @Endereco.setter
    def Endereco(self, Endereco: str):
        self.__Endereco = Endereco

    @property
    def CPF1(self):
        return self.__CPF1
    @CPF1.setter
    def CPF1(self, CPF1: int):
        self.__CPF1 = CPF1

    @property
    def RG(self):
        return self.__RG
    @RG.setter
    def RG(self, RG: int):
        self.__RG = RG

    @property
    def CEP(self):
        return self.__CEP
    @CEP.setter
    def CEP(self, CEP: int):
        self.__CEP = CEP

    @property
    def Sobrenome(self):
        return self.__Sobrenome
    @Sobrenome.setter
    def Sobrenome(self, Sobrenome: str):
        self.__Sobrenome = Sobrenome

    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def Sexo(self):
        return self.__Sexo
    @Sexo.setter
    def Sexo(self, Sexo: str):
        self.__Sexo = Sexo

    @property
    def Telefone(self):
        return self.__Telefone
    @Telefone.setter
    def Telefone(self, Telefone: int):
        self.__Telefone = Telefone

    @property
    def DataNascimento(self):
        return self.__DataNascimento
    @DataNascimento.setter
    def DataNascimento(self, DataNascimento: str):
        self.__DataNascimento = DataNascimento

    @property
    def CPF(self):
        return self.__CPF
    @CPF.setter
    def CPF(self, CPF: Paciente):
        self.__CPF = CPF

    @property
    def Celular(self):
        return self.__Celular
    @Celular.setter
    def Celular(self, Celular: int):
        self.__Celular = Celular



class Exame:

    def __init__(self, TipoExame: str, Especialista: str, Medico: str, Sede: str, agendamento1: "Agendamento" = None):
        self.TipoExame = TipoExame
        self.Especialista = Especialista
        self.Medico = Medico
        self.Sede = Sede
        self.agendamento1 = agendamento1
        
        pass
    @property
    def Medico(self):
        return self.__Medico
    @Medico.setter
    def Medico(self, Medico: str):
        self.__Medico = Medico

    @property
    def Sede(self):
        return self.__Sede
    @Sede.setter
    def Sede(self, Sede: str):
        self.__Sede = Sede

    @property
    def TipoExame(self):
        return self.__TipoExame
    @TipoExame.setter
    def TipoExame(self, TipoExame: str):
        self.__TipoExame = TipoExame

    @property
    def Especialista(self):
        return self.__Especialista
    @Especialista.setter
    def Especialista(self, Especialista: str):
        self.__Especialista = Especialista

    @property
    def agendamento1(self):
        return self.__agendamento1
    @agendamento1.setter
    def agendamento1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exame__agendamento1", None)
        self.__agendamento1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exame0"):
                opp_val = getattr(old_value, "exame0", None)
                if opp_val == self:
                    setattr(old_value, "exame0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exame0"):
                opp_val = getattr(value, "exame0", None)
                setattr(value, "exame0", self)

