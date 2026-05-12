from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Atestado:

    def __init__(self, dataInicioDoAtestado: str, dataFimDoAtestado: str, consulta: Consulta, quantidadeDias: str, consulta28: "Consulta" = None):
        self.dataInicioDoAtestado = dataInicioDoAtestado
        self.dataFimDoAtestado = dataFimDoAtestado
        self.consulta = consulta
        self.quantidadeDias = quantidadeDias
        self.consulta28 = consulta28
        
        pass
    @property
    def dataFimDoAtestado(self):
        return self.__dataFimDoAtestado
    @dataFimDoAtestado.setter
    def dataFimDoAtestado(self, dataFimDoAtestado: str):
        self.__dataFimDoAtestado = dataFimDoAtestado

    @property
    def dataInicioDoAtestado(self):
        return self.__dataInicioDoAtestado
    @dataInicioDoAtestado.setter
    def dataInicioDoAtestado(self, dataInicioDoAtestado: str):
        self.__dataInicioDoAtestado = dataInicioDoAtestado

    @property
    def quantidadeDias(self):
        return self.__quantidadeDias
    @quantidadeDias.setter
    def quantidadeDias(self, quantidadeDias: str):
        self.__quantidadeDias = quantidadeDias

    @property
    def consulta(self):
        return self.__consulta
    @consulta.setter
    def consulta(self, consulta: Consulta):
        self.__consulta = consulta

    @property
    def consulta28(self):
        return self.__consulta28
    @consulta28.setter
    def consulta28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Atestado__consulta28", None)
        self.__consulta28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atestado29"):
                opp_val = getattr(old_value, "atestado29", None)
                if opp_val == self:
                    setattr(old_value, "atestado29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atestado29"):
                opp_val = getattr(value, "atestado29", None)
                setattr(value, "atestado29", self)



class Consulta:

    def __init__(self, triagem: Triagem, medico: Medico, medicamentos: str, diagnostico: str, atestado: bool, codigoDiagnostico: str, medico24: "Medico" = None, triagem26: "Triagem" = None, atestado29: "Atestado" = None):
        self.triagem = triagem
        self.medico = medico
        self.medicamentos = medicamentos
        self.diagnostico = diagnostico
        self.atestado = atestado
        self.codigoDiagnostico = codigoDiagnostico
        self.medico24 = medico24
        self.triagem26 = triagem26
        self.atestado29 = atestado29
        
        pass
    @property
    def atestado(self):
        return self.__atestado
    @atestado.setter
    def atestado(self, atestado: bool):
        self.__atestado = atestado

    @property
    def codigoDiagnostico(self):
        return self.__codigoDiagnostico
    @codigoDiagnostico.setter
    def codigoDiagnostico(self, codigoDiagnostico: str):
        self.__codigoDiagnostico = codigoDiagnostico

    @property
    def triagem(self):
        return self.__triagem
    @triagem.setter
    def triagem(self, triagem: Triagem):
        self.__triagem = triagem

    @property
    def medicamentos(self):
        return self.__medicamentos
    @medicamentos.setter
    def medicamentos(self, medicamentos: str):
        self.__medicamentos = medicamentos

    @property
    def diagnostico(self):
        return self.__diagnostico
    @diagnostico.setter
    def diagnostico(self, diagnostico: str):
        self.__diagnostico = diagnostico

    @property
    def medico(self):
        return self.__medico
    @medico.setter
    def medico(self, medico: Medico):
        self.__medico = medico

    @property
    def triagem26(self):
        return self.__triagem26
    @triagem26.setter
    def triagem26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__triagem26", None)
        self.__triagem26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta7"):
                opp_val = getattr(old_value, "consulta7", None)
                if opp_val == self:
                    setattr(old_value, "consulta7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta7"):
                opp_val = getattr(value, "consulta7", None)
                setattr(value, "consulta7", self)

    @property
    def medico24(self):
        return self.__medico24
    @medico24.setter
    def medico24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__medico24", None)
        self.__medico24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta5"):
                opp_val = getattr(old_value, "consulta5", None)
                if opp_val == self:
                    setattr(old_value, "consulta5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta5"):
                opp_val = getattr(value, "consulta5", None)
                setattr(value, "consulta5", self)

    @property
    def atestado29(self):
        return self.__atestado29
    @atestado29.setter
    def atestado29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__atestado29", None)
        self.__atestado29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta28"):
                opp_val = getattr(old_value, "consulta28", None)
                if opp_val == self:
                    setattr(old_value, "consulta28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta28"):
                opp_val = getattr(value, "consulta28", None)
                setattr(value, "consulta28", self)



class String_Interface:

    pass


class Triagem:

    def __init__(self, enfermeira: Enfermeira, paciente: Paciente, pressao: String_Interface, temperatura: str, sintoma: str, alergias: str, peso: str, altura: str, IMC: str, febre: bool, enfermeira22: "Enfermeira" = None, consulta7: "Consulta" = None, paciente20: "Paciente" = None):
        self.enfermeira = enfermeira
        self.paciente = paciente
        self.pressao = pressao
        self.temperatura = temperatura
        self.sintoma = sintoma
        self.alergias = alergias
        self.peso = peso
        self.altura = altura
        self.IMC = IMC
        self.febre = febre
        self.enfermeira22 = enfermeira22
        self.consulta7 = consulta7
        self.paciente20 = paciente20
        
        pass
    @property
    def febre(self):
        return self.__febre
    @febre.setter
    def febre(self, febre: bool):
        self.__febre = febre

    @property
    def pressao(self):
        return self.__pressao
    @pressao.setter
    def pressao(self, pressao: String_Interface):
        self.__pressao = pressao

    @property
    def alergias(self):
        return self.__alergias
    @alergias.setter
    def alergias(self, alergias: str):
        self.__alergias = alergias

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: str):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: str):
        self.__altura = altura

    @property
    def enfermeira(self):
        return self.__enfermeira
    @enfermeira.setter
    def enfermeira(self, enfermeira: Enfermeira):
        self.__enfermeira = enfermeira

    @property
    def IMC(self):
        return self.__IMC
    @IMC.setter
    def IMC(self, IMC: str):
        self.__IMC = IMC

    @property
    def sintoma(self):
        return self.__sintoma
    @sintoma.setter
    def sintoma(self, sintoma: str):
        self.__sintoma = sintoma

    @property
    def temperatura(self):
        return self.__temperatura
    @temperatura.setter
    def temperatura(self, temperatura: str):
        self.__temperatura = temperatura

    @property
    def paciente(self):
        return self.__paciente
    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente

    @property
    def paciente20(self):
        return self.__paciente20
    @paciente20.setter
    def paciente20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Triagem__paciente20", None)
        self.__paciente20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "triagem1"):
                opp_val = getattr(old_value, "triagem1", None)
                if opp_val == self:
                    setattr(old_value, "triagem1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "triagem1"):
                opp_val = getattr(value, "triagem1", None)
                setattr(value, "triagem1", self)

    @property
    def consulta7(self):
        return self.__consulta7
    @consulta7.setter
    def consulta7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Triagem__consulta7", None)
        self.__consulta7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "triagem26"):
                opp_val = getattr(old_value, "triagem26", None)
                if opp_val == self:
                    setattr(old_value, "triagem26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "triagem26"):
                opp_val = getattr(value, "triagem26", None)
                setattr(value, "triagem26", self)

    @property
    def enfermeira22(self):
        return self.__enfermeira22
    @enfermeira22.setter
    def enfermeira22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Triagem__enfermeira22", None)
        self.__enfermeira22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "triagem3"):
                opp_val = getattr(old_value, "triagem3", None)
                if opp_val == self:
                    setattr(old_value, "triagem3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "triagem3"):
                opp_val = getattr(value, "triagem3", None)
                setattr(value, "triagem3", self)



class Enfermeira:

    def __init__(self, cofen: str, setor: str, triagem3: "Triagem" = None):
        self.cofen = cofen
        self.setor = setor
        self.triagem3 = triagem3
        
        pass
    @property
    def cofen(self):
        return self.__cofen
    @cofen.setter
    def cofen(self, cofen: str):
        self.__cofen = cofen

    @property
    def setor(self):
        return self.__setor
    @setor.setter
    def setor(self, setor: str):
        self.__setor = setor

    @property
    def triagem3(self):
        return self.__triagem3
    @triagem3.setter
    def triagem3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Enfermeira__triagem3", None)
        self.__triagem3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enfermeira22"):
                opp_val = getattr(old_value, "enfermeira22", None)
                if opp_val == self:
                    setattr(old_value, "enfermeira22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enfermeira22"):
                opp_val = getattr(value, "enfermeira22", None)
                setattr(value, "enfermeira22", self)



class Medico:

    def __init__(self, crm: str, especialidade: str, setor: str, consulta5: "Consulta" = None):
        self.crm = crm
        self.especialidade = especialidade
        self.setor = setor
        self.consulta5 = consulta5
        
        pass
    @property
    def crm(self):
        return self.__crm
    @crm.setter
    def crm(self, crm: str):
        self.__crm = crm

    @property
    def setor(self):
        return self.__setor
    @setor.setter
    def setor(self, setor: str):
        self.__setor = setor

    @property
    def especialidade(self):
        return self.__especialidade
    @especialidade.setter
    def especialidade(self, especialidade: str):
        self.__especialidade = especialidade

    @property
    def consulta5(self):
        return self.__consulta5
    @consulta5.setter
    def consulta5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medico__consulta5", None)
        self.__consulta5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medico24"):
                opp_val = getattr(old_value, "medico24", None)
                if opp_val == self:
                    setattr(old_value, "medico24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medico24"):
                opp_val = getattr(value, "medico24", None)
                setattr(value, "medico24", self)



class Paciente:

    def __init__(self, id: str, numeroSus: str, responsavel: Pessoa, triagem1: "Triagem" = None):
        self.id = id
        self.numeroSus = numeroSus
        self.responsavel = responsavel
        self.triagem1 = triagem1
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def responsavel(self):
        return self.__responsavel
    @responsavel.setter
    def responsavel(self, responsavel: Pessoa):
        self.__responsavel = responsavel

    @property
    def numeroSus(self):
        return self.__numeroSus
    @numeroSus.setter
    def numeroSus(self, numeroSus: str):
        self.__numeroSus = numeroSus

    @property
    def triagem1(self):
        return self.__triagem1
    @triagem1.setter
    def triagem1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Paciente__triagem1", None)
        self.__triagem1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paciente20"):
                opp_val = getattr(old_value, "paciente20", None)
                if opp_val == self:
                    setattr(old_value, "paciente20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paciente20"):
                opp_val = getattr(value, "paciente20", None)
                setattr(value, "paciente20", self)



class Pessoa:

    def __init__(self, nome: str, dataNascimento: str, cpf: str, rg: str, endereco: str, telefone: str, estadoCivil: str, sexo: str):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.telefone = telefone
        self.estadoCivil = estadoCivil
        self.sexo = sexo
        
        pass
    @property
    def sexo(self):
        return self.__sexo
    @sexo.setter
    def sexo(self, sexo: str):
        self.__sexo = sexo

    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @property
    def dataNascimento(self):
        return self.__dataNascimento
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento: str):
        self.__dataNascimento = dataNascimento

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def estadoCivil(self):
        return self.__estadoCivil
    @estadoCivil.setter
    def estadoCivil(self, estadoCivil: str):
        self.__estadoCivil = estadoCivil

    @property
    def rg(self):
        return self.__rg
    @rg.setter
    def rg(self, rg: str):
        self.__rg = rg

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

