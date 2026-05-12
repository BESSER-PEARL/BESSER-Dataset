from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class enu(Enum):
    pass

############################################
# Definition of Classes
############################################










class LinhaCuidado:

    def __init__(self, nome: str, descricao: int, mensagem15: set["Mensagem"] = None):
        self.nome = nome
        self.descricao = descricao
        self.mensagem15 = mensagem15 if mensagem15 is not None else set()
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao: int):
        self.__descricao = descricao

    @property
    def mensagem15(self):
        return self.__mensagem15
    @mensagem15.setter
    def mensagem15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LinhaCuidado__mensagem15", None)
        self.__mensagem15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "linhaCuidado14"):
                    opp_val = getattr(item, "linhaCuidado14", None)
                    
                    if opp_val == self:
                        setattr(item, "linhaCuidado14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "linhaCuidado14"):
                    opp_val = getattr(item, "linhaCuidado14", None)
                    
                    setattr(item, "linhaCuidado14", self)
                    



class Mensagem:

    def __init__(self, assunto: str, mensagem: str, dataEnvio: str, geral: bool, linhaCuidado14: "LinhaCuidado" = None, interacao17: set["Interacao"] = None, paciente21: "Paciente" = None, profissionalSaude13: "ProfissionalSaude" = None):
        self.assunto = assunto
        self.mensagem = mensagem
        self.dataEnvio = dataEnvio
        self.geral = geral
        self.linhaCuidado14 = linhaCuidado14
        self.interacao17 = interacao17 if interacao17 is not None else set()
        self.paciente21 = paciente21
        self.profissionalSaude13 = profissionalSaude13
        
        pass
    @property
    def geral(self):
        return self.__geral
    @geral.setter
    def geral(self, geral: bool):
        self.__geral = geral

    @property
    def mensagem(self):
        return self.__mensagem
    @mensagem.setter
    def mensagem(self, mensagem: str):
        self.__mensagem = mensagem

    @property
    def assunto(self):
        return self.__assunto
    @assunto.setter
    def assunto(self, assunto: str):
        self.__assunto = assunto

    @property
    def dataEnvio(self):
        return self.__dataEnvio
    @dataEnvio.setter
    def dataEnvio(self, dataEnvio: str):
        self.__dataEnvio = dataEnvio

    @property
    def profissionalSaude13(self):
        return self.__profissionalSaude13
    @profissionalSaude13.setter
    def profissionalSaude13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mensagem__profissionalSaude13", None)
        self.__profissionalSaude13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mensagem12"):
                opp_val = getattr(old_value, "mensagem12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mensagem12"):
                opp_val = getattr(value, "mensagem12", None)
                if opp_val is None:
                    setattr(value, "mensagem12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linhaCuidado14(self):
        return self.__linhaCuidado14
    @linhaCuidado14.setter
    def linhaCuidado14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mensagem__linhaCuidado14", None)
        self.__linhaCuidado14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mensagem15"):
                opp_val = getattr(old_value, "mensagem15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mensagem15"):
                opp_val = getattr(value, "mensagem15", None)
                if opp_val is None:
                    setattr(value, "mensagem15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def paciente21(self):
        return self.__paciente21
    @paciente21.setter
    def paciente21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mensagem__paciente21", None)
        self.__paciente21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mensagem20"):
                opp_val = getattr(old_value, "mensagem20", None)
                if opp_val == self:
                    setattr(old_value, "mensagem20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mensagem20"):
                opp_val = getattr(value, "mensagem20", None)
                setattr(value, "mensagem20", self)

    @property
    def interacao17(self):
        return self.__interacao17
    @interacao17.setter
    def interacao17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mensagem__interacao17", None)
        self.__interacao17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mensagem16"):
                    opp_val = getattr(item, "mensagem16", None)
                    
                    if opp_val == self:
                        setattr(item, "mensagem16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mensagem16"):
                    opp_val = getattr(item, "mensagem16", None)
                    
                    setattr(item, "mensagem16", self)
                    



class ProfissionalSaude:

    pass


class Naturalidade:

    def __init__(self, naturalidade: str, pessoa11: set["Pessoa"] = None):
        self.naturalidade = naturalidade
        self.pessoa11 = pessoa11 if pessoa11 is not None else set()
        
        pass
    @property
    def naturalidade(self):
        return self.__naturalidade
    @naturalidade.setter
    def naturalidade(self, naturalidade: str):
        self.__naturalidade = naturalidade

    @property
    def pessoa11(self):
        return self.__pessoa11
    @pessoa11.setter
    def pessoa11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Naturalidade__pessoa11", None)
        self.__pessoa11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "naturalidade10"):
                    opp_val = getattr(item, "naturalidade10", None)
                    
                    if opp_val == self:
                        setattr(item, "naturalidade10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "naturalidade10"):
                    opp_val = getattr(item, "naturalidade10", None)
                    
                    setattr(item, "naturalidade10", self)
                    



class Medicamento:

    def __init__(self, nome: str, descricao: str, horaInicial: str, ativo: bool, intervaloTempo: int, dataInicio: str, dataFim: str, paciente9: "Paciente" = None):
        self.nome = nome
        self.descricao = descricao
        self.horaInicial = horaInicial
        self.ativo = ativo
        self.intervaloTempo = intervaloTempo
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.paciente9 = paciente9
        
        pass
    @property
    def dataInicio(self):
        return self.__dataInicio
    @dataInicio.setter
    def dataInicio(self, dataInicio: str):
        self.__dataInicio = dataInicio

    @property
    def intervaloTempo(self):
        return self.__intervaloTempo
    @intervaloTempo.setter
    def intervaloTempo(self, intervaloTempo: int):
        self.__intervaloTempo = intervaloTempo

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def horaInicial(self):
        return self.__horaInicial
    @horaInicial.setter
    def horaInicial(self, horaInicial: str):
        self.__horaInicial = horaInicial

    @property
    def dataFim(self):
        return self.__dataFim
    @dataFim.setter
    def dataFim(self, dataFim: str):
        self.__dataFim = dataFim

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def ativo(self):
        return self.__ativo
    @ativo.setter
    def ativo(self, ativo: bool):
        self.__ativo = ativo

    @property
    def paciente9(self):
        return self.__paciente9
    @paciente9.setter
    def paciente9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medicamento__paciente9", None)
        self.__paciente9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medicamento8"):
                opp_val = getattr(old_value, "medicamento8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medicamento8"):
                opp_val = getattr(value, "medicamento8", None)
                if opp_val is None:
                    setattr(value, "medicamento8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Paciente:

    pass


class Telefone:

    def __init__(self, ddd: int, tipo: str, numero: str, pessoa7: "Pessoa" = None):
        self.ddd = ddd
        self.tipo = tipo
        self.numero = numero
        self.pessoa7 = pessoa7
        
        pass
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def ddd(self):
        return self.__ddd
    @ddd.setter
    def ddd(self, ddd: int):
        self.__ddd = ddd

    @property
    def pessoa7(self):
        return self.__pessoa7
    @pessoa7.setter
    def pessoa7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Telefone__pessoa7", None)
        self.__pessoa7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "telefone6"):
                opp_val = getattr(old_value, "telefone6", None)
                if opp_val == self:
                    setattr(old_value, "telefone6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "telefone6"):
                opp_val = getattr(value, "telefone6", None)
                setattr(value, "telefone6", self)



class Pessoa:

    def __init__(self, dataNascimento: str, cpf: str, dataInclusao: str, sexo: str, email: str, senha: str, ultimoAcesso: str, endereco5: "Endereco" = None, telefone6: "Telefone" = None, naturalidade10: "Naturalidade" = None):
        self.dataNascimento = dataNascimento
        self.cpf = cpf
        self.dataInclusao = dataInclusao
        self.sexo = sexo
        self.email = email
        self.senha = senha
        self.ultimoAcesso = ultimoAcesso
        self.endereco5 = endereco5
        self.telefone6 = telefone6
        self.naturalidade10 = naturalidade10
        
        pass
    @property
    def ultimoAcesso(self):
        return self.__ultimoAcesso
    @ultimoAcesso.setter
    def ultimoAcesso(self, ultimoAcesso: str):
        self.__ultimoAcesso = ultimoAcesso

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def dataNascimento(self):
        return self.__dataNascimento
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento: str):
        self.__dataNascimento = dataNascimento

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha

    @property
    def dataInclusao(self):
        return self.__dataInclusao
    @dataInclusao.setter
    def dataInclusao(self, dataInclusao: str):
        self.__dataInclusao = dataInclusao

    @property
    def sexo(self):
        return self.__sexo
    @sexo.setter
    def sexo(self, sexo: str):
        self.__sexo = sexo

    @property
    def telefone6(self):
        return self.__telefone6
    @telefone6.setter
    def telefone6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pessoa__telefone6", None)
        self.__telefone6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pessoa7"):
                opp_val = getattr(old_value, "pessoa7", None)
                if opp_val == self:
                    setattr(old_value, "pessoa7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pessoa7"):
                opp_val = getattr(value, "pessoa7", None)
                setattr(value, "pessoa7", self)

    @property
    def naturalidade10(self):
        return self.__naturalidade10
    @naturalidade10.setter
    def naturalidade10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pessoa__naturalidade10", None)
        self.__naturalidade10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pessoa11"):
                opp_val = getattr(old_value, "pessoa11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pessoa11"):
                opp_val = getattr(value, "pessoa11", None)
                if opp_val is None:
                    setattr(value, "pessoa11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def endereco5(self):
        return self.__endereco5
    @endereco5.setter
    def endereco5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pessoa__endereco5", None)
        self.__endereco5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pessoa4"):
                opp_val = getattr(old_value, "pessoa4", None)
                if opp_val == self:
                    setattr(old_value, "pessoa4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pessoa4"):
                opp_val = getattr(value, "pessoa4", None)
                setattr(value, "pessoa4", self)



class Endereco:

    def __init__(self, numero: int, logradouro: str, bairro: str, cidade: str, cep: str, localExame3: "LocalExame" = None, pessoa4: "Pessoa" = None):
        self.numero = numero
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.localExame3 = localExame3
        self.pessoa4 = pessoa4
        
        pass
    @property
    def logradouro(self):
        return self.__logradouro
    @logradouro.setter
    def logradouro(self, logradouro: str):
        self.__logradouro = logradouro

    @property
    def cidade(self):
        return self.__cidade
    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @property
    def cep(self):
        return self.__cep
    @cep.setter
    def cep(self, cep: str):
        self.__cep = cep

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @property
    def bairro(self):
        return self.__bairro
    @bairro.setter
    def bairro(self, bairro: str):
        self.__bairro = bairro

    @property
    def pessoa4(self):
        return self.__pessoa4
    @pessoa4.setter
    def pessoa4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Endereco__pessoa4", None)
        self.__pessoa4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "endereco5"):
                opp_val = getattr(old_value, "endereco5", None)
                if opp_val == self:
                    setattr(old_value, "endereco5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "endereco5"):
                opp_val = getattr(value, "endereco5", None)
                setattr(value, "endereco5", self)

    @property
    def localExame3(self):
        return self.__localExame3
    @localExame3.setter
    def localExame3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Endereco__localExame3", None)
        self.__localExame3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "endereco2"):
                opp_val = getattr(old_value, "endereco2", None)
                if opp_val == self:
                    setattr(old_value, "endereco2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "endereco2"):
                opp_val = getattr(value, "endereco2", None)
                setattr(value, "endereco2", self)



class Exame:

    def __init__(self, data: str, nome: str, descricao: str, localExame1: "LocalExame" = None):
        self.data = data
        self.nome = nome
        self.descricao = descricao
        self.localExame1 = localExame1
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def localExame1(self):
        return self.__localExame1
    @localExame1.setter
    def localExame1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exame__localExame1", None)
        self.__localExame1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exame0"):
                opp_val = getattr(old_value, "exame0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exame0"):
                opp_val = getattr(value, "exame0", None)
                if opp_val is None:
                    setattr(value, "exame0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class LocalExame:

    def __init__(self, nome: str, exame0: set["Exame"] = None, endereco2: "Endereco" = None):
        self.nome = nome
        self.exame0 = exame0 if exame0 is not None else set()
        self.endereco2 = endereco2
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def exame0(self):
        return self.__exame0
    @exame0.setter
    def exame0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LocalExame__exame0", None)
        self.__exame0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "localExame1"):
                    opp_val = getattr(item, "localExame1", None)
                    
                    if opp_val == self:
                        setattr(item, "localExame1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "localExame1"):
                    opp_val = getattr(item, "localExame1", None)
                    
                    setattr(item, "localExame1", self)
                    

    @property
    def endereco2(self):
        return self.__endereco2
    @endereco2.setter
    def endereco2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LocalExame__endereco2", None)
        self.__endereco2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "localExame3"):
                opp_val = getattr(old_value, "localExame3", None)
                if opp_val == self:
                    setattr(old_value, "localExame3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "localExame3"):
                opp_val = getattr(value, "localExame3", None)
                setattr(value, "localExame3", self)



class TipoMedicamento:

    def __init__(self, nome: str):
        self.nome = nome
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome



class TipoSanguineo:

    def __init__(self, nome: str, paciente22: set["Paciente"] = None):
        self.nome = nome
        self.paciente22 = paciente22 if paciente22 is not None else set()
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def paciente22(self):
        return self.__paciente22
    @paciente22.setter
    def paciente22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TipoSanguineo__paciente22", None)
        self.__paciente22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tipoSanguineo23"):
                    opp_val = getattr(item, "tipoSanguineo23", None)
                    
                    if opp_val == self:
                        setattr(item, "tipoSanguineo23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tipoSanguineo23"):
                    opp_val = getattr(item, "tipoSanguineo23", None)
                    
                    setattr(item, "tipoSanguineo23", self)
                    



class Interacao:

    pass
