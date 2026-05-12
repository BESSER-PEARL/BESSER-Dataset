from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Especialidade:

    def __init__(self, Id: int, Descricao: str, agenda3: set["Agenda"] = None):
        self.Id = Id
        self.Descricao = Descricao
        self.agenda3 = agenda3 if agenda3 is not None else set()
        
        pass
    @property
    def Descricao(self):
        return self.__Descricao
    @Descricao.setter
    def Descricao(self, Descricao: str):
        self.__Descricao = Descricao

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def agenda3(self):
        return self.__agenda3
    @agenda3.setter
    def agenda3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Especialidade__agenda3", None)
        self.__agenda3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "especialidade2"):
                    opp_val = getattr(item, "especialidade2", None)
                    
                    if opp_val == self:
                        setattr(item, "especialidade2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "especialidade2"):
                    opp_val = getattr(item, "especialidade2", None)
                    
                    setattr(item, "especialidade2", self)
                    



class ConsultaExame:

    def __init__(self, Entregue: bool, exame15: "Exame" = None, consulta17: "Consulta" = None):
        self.Entregue = Entregue
        self.exame15 = exame15
        self.consulta17 = consulta17
        
        pass
    @property
    def Entregue(self):
        return self.__Entregue
    @Entregue.setter
    def Entregue(self, Entregue: bool):
        self.__Entregue = Entregue

    @property
    def consulta17(self):
        return self.__consulta17
    @consulta17.setter
    def consulta17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConsultaExame__consulta17", None)
        self.__consulta17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consultaExame16"):
                opp_val = getattr(old_value, "consultaExame16", None)
                if opp_val == self:
                    setattr(old_value, "consultaExame16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consultaExame16"):
                opp_val = getattr(value, "consultaExame16", None)
                setattr(value, "consultaExame16", self)

    @property
    def exame15(self):
        return self.__exame15
    @exame15.setter
    def exame15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConsultaExame__exame15", None)
        self.__exame15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consultaExame14"):
                opp_val = getattr(old_value, "consultaExame14", None)
                if opp_val == self:
                    setattr(old_value, "consultaExame14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consultaExame14"):
                opp_val = getattr(value, "consultaExame14", None)
                setattr(value, "consultaExame14", self)



class ConsultaMedicamento:

    def __init__(self, Posologia: str, MedicamentoId: Medicamento, consulta12: "Consulta" = None, medicamento10: "Medicamento" = None):
        self.Posologia = Posologia
        self.MedicamentoId = MedicamentoId
        self.consulta12 = consulta12
        self.medicamento10 = medicamento10
        
        pass
    @property
    def Posologia(self):
        return self.__Posologia
    @Posologia.setter
    def Posologia(self, Posologia: str):
        self.__Posologia = Posologia

    @property
    def MedicamentoId(self):
        return self.__MedicamentoId
    @MedicamentoId.setter
    def MedicamentoId(self, MedicamentoId: Medicamento):
        self.__MedicamentoId = MedicamentoId

    @property
    def consulta12(self):
        return self.__consulta12
    @consulta12.setter
    def consulta12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConsultaMedicamento__consulta12", None)
        self.__consulta12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consultaMedicamento13"):
                opp_val = getattr(old_value, "consultaMedicamento13", None)
                if opp_val == self:
                    setattr(old_value, "consultaMedicamento13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consultaMedicamento13"):
                opp_val = getattr(value, "consultaMedicamento13", None)
                setattr(value, "consultaMedicamento13", self)

    @property
    def medicamento10(self):
        return self.__medicamento10
    @medicamento10.setter
    def medicamento10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConsultaMedicamento__medicamento10", None)
        self.__medicamento10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consultaMedicamento11"):
                opp_val = getattr(old_value, "consultaMedicamento11", None)
                if opp_val == self:
                    setattr(old_value, "consultaMedicamento11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consultaMedicamento11"):
                opp_val = getattr(value, "consultaMedicamento11", None)
                setattr(value, "consultaMedicamento11", self)



class ConsultaCid:

    def __init__(self, ConsultaId: int, CidId: int, consulta7: set["Consulta"] = None, cid9: "Cid" = None):
        self.ConsultaId = ConsultaId
        self.CidId = CidId
        self.consulta7 = consulta7 if consulta7 is not None else set()
        self.cid9 = cid9
        
        pass
    @property
    def ConsultaId(self):
        return self.__ConsultaId
    @ConsultaId.setter
    def ConsultaId(self, ConsultaId: int):
        self.__ConsultaId = ConsultaId

    @property
    def CidId(self):
        return self.__CidId
    @CidId.setter
    def CidId(self, CidId: int):
        self.__CidId = CidId

    @property
    def consulta7(self):
        return self.__consulta7
    @consulta7.setter
    def consulta7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConsultaCid__consulta7", None)
        self.__consulta7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "consultaCid6"):
                    opp_val = getattr(item, "consultaCid6", None)
                    
                    if opp_val == self:
                        setattr(item, "consultaCid6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "consultaCid6"):
                    opp_val = getattr(item, "consultaCid6", None)
                    
                    setattr(item, "consultaCid6", self)
                    

    @property
    def cid9(self):
        return self.__cid9
    @cid9.setter
    def cid9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConsultaCid__cid9", None)
        self.__cid9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consultaCid8"):
                opp_val = getattr(old_value, "consultaCid8", None)
                if opp_val == self:
                    setattr(old_value, "consultaCid8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consultaCid8"):
                opp_val = getattr(value, "consultaCid8", None)
                setattr(value, "consultaCid8", self)



class Consulta:

    def __init__(self, DataHora: str, PacienteId: Paciente, MedicoId: Funcionario, Queixas: str, consultaMedicamento13: "ConsultaMedicamento" = None, consultaExame16: "ConsultaExame" = None, paciente5: "Paciente" = None, consultaCid6: "ConsultaCid" = None):
        self.DataHora = DataHora
        self.PacienteId = PacienteId
        self.MedicoId = MedicoId
        self.Queixas = Queixas
        self.consultaMedicamento13 = consultaMedicamento13
        self.consultaExame16 = consultaExame16
        self.paciente5 = paciente5
        self.consultaCid6 = consultaCid6
        
        pass
    @property
    def DataHora(self):
        return self.__DataHora
    @DataHora.setter
    def DataHora(self, DataHora: str):
        self.__DataHora = DataHora

    @property
    def PacienteId(self):
        return self.__PacienteId
    @PacienteId.setter
    def PacienteId(self, PacienteId: Paciente):
        self.__PacienteId = PacienteId

    @property
    def Queixas(self):
        return self.__Queixas
    @Queixas.setter
    def Queixas(self, Queixas: str):
        self.__Queixas = Queixas

    @property
    def MedicoId(self):
        return self.__MedicoId
    @MedicoId.setter
    def MedicoId(self, MedicoId: Funcionario):
        self.__MedicoId = MedicoId

    @property
    def consultaCid6(self):
        return self.__consultaCid6
    @consultaCid6.setter
    def consultaCid6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__consultaCid6", None)
        self.__consultaCid6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta7"):
                opp_val = getattr(old_value, "consulta7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta7"):
                opp_val = getattr(value, "consulta7", None)
                if opp_val is None:
                    setattr(value, "consulta7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def consultaExame16(self):
        return self.__consultaExame16
    @consultaExame16.setter
    def consultaExame16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__consultaExame16", None)
        self.__consultaExame16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta17"):
                opp_val = getattr(old_value, "consulta17", None)
                if opp_val == self:
                    setattr(old_value, "consulta17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta17"):
                opp_val = getattr(value, "consulta17", None)
                setattr(value, "consulta17", self)

    @property
    def consultaMedicamento13(self):
        return self.__consultaMedicamento13
    @consultaMedicamento13.setter
    def consultaMedicamento13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__consultaMedicamento13", None)
        self.__consultaMedicamento13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta12"):
                opp_val = getattr(old_value, "consulta12", None)
                if opp_val == self:
                    setattr(old_value, "consulta12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta12"):
                opp_val = getattr(value, "consulta12", None)
                setattr(value, "consulta12", self)

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta4"):
                opp_val = getattr(value, "consulta4", None)
                if opp_val is None:
                    setattr(value, "consulta4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Paciente:

    def __init__(self, Id: int, Nome: str, NomeMae: str, CPF: str, DataNascimento: str, consulta4: set["Consulta"] = None):
        self.Id = Id
        self.Nome = Nome
        self.NomeMae = NomeMae
        self.CPF = CPF
        self.DataNascimento = DataNascimento
        self.consulta4 = consulta4 if consulta4 is not None else set()
        
        pass
    @property
    def DataNascimento(self):
        return self.__DataNascimento
    @DataNascimento.setter
    def DataNascimento(self, DataNascimento: str):
        self.__DataNascimento = DataNascimento

    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def NomeMae(self):
        return self.__NomeMae
    @NomeMae.setter
    def NomeMae(self, NomeMae: str):
        self.__NomeMae = NomeMae

    @property
    def CPF(self):
        return self.__CPF
    @CPF.setter
    def CPF(self, CPF: str):
        self.__CPF = CPF

    @property
    def consulta4(self):
        return self.__consulta4
    @consulta4.setter
    def consulta4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Paciente__consulta4", None)
        self.__consulta4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "paciente5"):
                    opp_val = getattr(item, "paciente5", None)
                    
                    if opp_val == self:
                        setattr(item, "paciente5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "paciente5"):
                    opp_val = getattr(item, "paciente5", None)
                    
                    setattr(item, "paciente5", self)
                    



class Medicamento:

    def __init__(self, Id: int, NomeGenerico: str, NomeComercial: str, Fabricante: str, consultaMedicamento11: "ConsultaMedicamento" = None):
        self.Id = Id
        self.NomeGenerico = NomeGenerico
        self.NomeComercial = NomeComercial
        self.Fabricante = Fabricante
        self.consultaMedicamento11 = consultaMedicamento11
        
        pass
    @property
    def Fabricante(self):
        return self.__Fabricante
    @Fabricante.setter
    def Fabricante(self, Fabricante: str):
        self.__Fabricante = Fabricante

    @property
    def NomeComercial(self):
        return self.__NomeComercial
    @NomeComercial.setter
    def NomeComercial(self, NomeComercial: str):
        self.__NomeComercial = NomeComercial

    @property
    def NomeGenerico(self):
        return self.__NomeGenerico
    @NomeGenerico.setter
    def NomeGenerico(self, NomeGenerico: str):
        self.__NomeGenerico = NomeGenerico

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def consultaMedicamento11(self):
        return self.__consultaMedicamento11
    @consultaMedicamento11.setter
    def consultaMedicamento11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medicamento__consultaMedicamento11", None)
        self.__consultaMedicamento11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medicamento10"):
                opp_val = getattr(old_value, "medicamento10", None)
                if opp_val == self:
                    setattr(old_value, "medicamento10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medicamento10"):
                opp_val = getattr(value, "medicamento10", None)
                setattr(value, "medicamento10", self)



class Exame:

    def __init__(self, Id: int, Codigo: str, Descricao: str, consultaExame14: "ConsultaExame" = None):
        self.Id = Id
        self.Codigo = Codigo
        self.Descricao = Descricao
        self.consultaExame14 = consultaExame14
        
        pass
    @property
    def Descricao(self):
        return self.__Descricao
    @Descricao.setter
    def Descricao(self, Descricao: str):
        self.__Descricao = Descricao

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: str):
        self.__Codigo = Codigo

    @property
    def consultaExame14(self):
        return self.__consultaExame14
    @consultaExame14.setter
    def consultaExame14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exame__consultaExame14", None)
        self.__consultaExame14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exame15"):
                opp_val = getattr(old_value, "exame15", None)
                if opp_val == self:
                    setattr(old_value, "exame15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exame15"):
                opp_val = getattr(value, "exame15", None)
                setattr(value, "exame15", self)



class Cid:

    def __init__(self, Id: int, Codigo: str, Descricao: str, consultaCid8: "ConsultaCid" = None):
        self.Id = Id
        self.Codigo = Codigo
        self.Descricao = Descricao
        self.consultaCid8 = consultaCid8
        
        pass
    @property
    def Descricao(self):
        return self.__Descricao
    @Descricao.setter
    def Descricao(self, Descricao: str):
        self.__Descricao = Descricao

    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: str):
        self.__Codigo = Codigo

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def consultaCid8(self):
        return self.__consultaCid8
    @consultaCid8.setter
    def consultaCid8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cid__consultaCid8", None)
        self.__consultaCid8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cid9"):
                opp_val = getattr(old_value, "cid9", None)
                if opp_val == self:
                    setattr(old_value, "cid9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cid9"):
                opp_val = getattr(value, "cid9", None)
                setattr(value, "cid9", self)



class Agenda:

    pass


class Funcionario:

    def __init__(self, Id: int, Nome: str, Login: str, Senha: str, Perfil: int, agenda1: "Agenda" = None):
        self.Id = Id
        self.Nome = Nome
        self.Login = Login
        self.Senha = Senha
        self.Perfil = Perfil
        self.agenda1 = agenda1
        
        pass
    @property
    def Senha(self):
        return self.__Senha
    @Senha.setter
    def Senha(self, Senha: str):
        self.__Senha = Senha

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Perfil(self):
        return self.__Perfil
    @Perfil.setter
    def Perfil(self, Perfil: int):
        self.__Perfil = Perfil

    @property
    def Login(self):
        return self.__Login
    @Login.setter
    def Login(self, Login: str):
        self.__Login = Login

    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def agenda1(self):
        return self.__agenda1
    @agenda1.setter
    def agenda1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Funcionario__agenda1", None)
        self.__agenda1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "funcionario0"):
                opp_val = getattr(old_value, "funcionario0", None)
                if opp_val == self:
                    setattr(old_value, "funcionario0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "funcionario0"):
                opp_val = getattr(value, "funcionario0", None)
                setattr(value, "funcionario0", self)

