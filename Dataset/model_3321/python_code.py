from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class exp_aux:

    pass
class variable_declarator:

    pass
class simpleJava_package_name_aux:

    def __init__(self, nomePacote: str, simpleJava_package_name_aux: "simpleJava_name" = None, simpleJava_package_name_aux239: "simpleJava_package_name_aux" = None, simpleJava_package_name_aux237: "simpleJava_package_name_aux" = None):
        self.nomePacote = nomePacote
        self.simpleJava_package_name_aux = simpleJava_package_name_aux
        self.simpleJava_package_name_aux239 = simpleJava_package_name_aux239
        self.simpleJava_package_name_aux237 = simpleJava_package_name_aux237
        
    @property
    def nomePacote(self) -> str:
        return self.__nomePacote

    @nomePacote.setter
    def nomePacote(self, nomePacote: str):
        self.__nomePacote = nomePacote

    @property
    def simpleJava_package_name_aux239(self):
        return self.__simpleJava_package_name_aux239

    @simpleJava_package_name_aux239.setter
    def simpleJava_package_name_aux239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_package_name_aux__simpleJava_package_name_aux239", None)
        self.__simpleJava_package_name_aux239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_package_name_aux237"):
                opp_val = getattr(old_value, "simpleJava_package_name_aux237", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_package_name_aux237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_package_name_aux237"):
                opp_val = getattr(value, "simpleJava_package_name_aux237", None)
                setattr(value, "simpleJava_package_name_aux237", self)

    @property
    def simpleJava_package_name_aux(self):
        return self.__simpleJava_package_name_aux

    @simpleJava_package_name_aux.setter
    def simpleJava_package_name_aux(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_package_name_aux__simpleJava_package_name_aux", None)
        self.__simpleJava_package_name_aux = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_name236"):
                opp_val = getattr(old_value, "simpleJava_name236", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_name236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_name236"):
                opp_val = getattr(value, "simpleJava_name236", None)
                setattr(value, "simpleJava_name236", self)

    @property
    def simpleJava_package_name_aux237(self):
        return self.__simpleJava_package_name_aux237

    @simpleJava_package_name_aux237.setter
    def simpleJava_package_name_aux237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_package_name_aux__simpleJava_package_name_aux237", None)
        self.__simpleJava_package_name_aux237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_package_name_aux239"):
                opp_val = getattr(old_value, "simpleJava_package_name_aux239", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_package_name_aux239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_package_name_aux239"):
                opp_val = getattr(value, "simpleJava_package_name_aux239", None)
                setattr(value, "simpleJava_package_name_aux239", self)

class creating_aux:

    pass
class simpleJava_mais_aux:

    def __init__(self, operador: str, simpleJava_mais_aux: "simpleJava_expression_aux" = None):
        self.operador = operador
        self.simpleJava_mais_aux = simpleJava_mais_aux
        
    @property
    def operador(self) -> str:
        return self.__operador

    @operador.setter
    def operador(self, operador: str):
        self.__operador = operador

    @property
    def simpleJava_mais_aux(self):
        return self.__simpleJava_mais_aux

    @simpleJava_mais_aux.setter
    def simpleJava_mais_aux(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_mais_aux__simpleJava_mais_aux", None)
        self.__simpleJava_mais_aux = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression_aux211"):
                opp_val = getattr(old_value, "simpleJava_expression_aux211", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression_aux211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression_aux211"):
                opp_val = getattr(value, "simpleJava_expression_aux211", None)
                setattr(value, "simpleJava_expression_aux211", self)

class simpleJava_arglist(variable_declarator):

    def __init__(self, nomeParametro: str, simpleJava_arglist: "simpleJava_expression_aux" = None, simpleJava_arglist217: "simpleJava_creating_aux" = None, simpleJava_arglist230: set["simpleJava_expression"] = None, simpleJava_arglist233: set["simpleJava_type"] = None):
        self.nomeParametro = nomeParametro
        self.simpleJava_arglist = simpleJava_arglist
        self.simpleJava_arglist217 = simpleJava_arglist217
        self.simpleJava_arglist230 = simpleJava_arglist230 if simpleJava_arglist230 is not None else set()
        self.simpleJava_arglist233 = simpleJava_arglist233 if simpleJava_arglist233 is not None else set()
        
    @property
    def nomeParametro(self) -> str:
        return self.__nomeParametro

    @nomeParametro.setter
    def nomeParametro(self, nomeParametro: str):
        self.__nomeParametro = nomeParametro

    @property
    def simpleJava_arglist233(self):
        return self.__simpleJava_arglist233

    @simpleJava_arglist233.setter
    def simpleJava_arglist233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_arglist__simpleJava_arglist233", None)
        self.__simpleJava_arglist233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleJava_type234"):
                    opp_val = getattr(item, "simpleJava_type234", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleJava_type234", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleJava_type234"):
                    opp_val = getattr(item, "simpleJava_type234", None)
                    
                    setattr(item, "simpleJava_type234", self)
                    

    @property
    def simpleJava_arglist(self):
        return self.__simpleJava_arglist

    @simpleJava_arglist.setter
    def simpleJava_arglist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_arglist__simpleJava_arglist", None)
        self.__simpleJava_arglist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression_aux"):
                opp_val = getattr(old_value, "simpleJava_expression_aux", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression_aux", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression_aux"):
                opp_val = getattr(value, "simpleJava_expression_aux", None)
                setattr(value, "simpleJava_expression_aux", self)

    @property
    def simpleJava_arglist230(self):
        return self.__simpleJava_arglist230

    @simpleJava_arglist230.setter
    def simpleJava_arglist230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_arglist__simpleJava_arglist230", None)
        self.__simpleJava_arglist230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleJava_expression231"):
                    opp_val = getattr(item, "simpleJava_expression231", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleJava_expression231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleJava_expression231"):
                    opp_val = getattr(item, "simpleJava_expression231", None)
                    
                    setattr(item, "simpleJava_expression231", self)
                    

    @property
    def simpleJava_arglist217(self):
        return self.__simpleJava_arglist217

    @simpleJava_arglist217.setter
    def simpleJava_arglist217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_arglist__simpleJava_arglist217", None)
        self.__simpleJava_arglist217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_creating_aux216"):
                opp_val = getattr(old_value, "simpleJava_creating_aux216", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_creating_aux216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_creating_aux216"):
                opp_val = getattr(value, "simpleJava_creating_aux216", None)
                setattr(value, "simpleJava_creating_aux216", self)

class simpleJava_expression_aux:

    def __init__(self, operador: str, simpleJava_expression_aux: "simpleJava_arglist" = None, simpleJava_expression_aux208: "simpleJava_expression" = None, simpleJava_expression_aux211: "simpleJava_mais_aux" = None, simpleJava_expression_aux214: "simpleJava_expression_aux" = None, simpleJava_expression_aux212: "simpleJava_expression_aux" = None):
        self.operador = operador
        self.simpleJava_expression_aux = simpleJava_expression_aux
        self.simpleJava_expression_aux208 = simpleJava_expression_aux208
        self.simpleJava_expression_aux211 = simpleJava_expression_aux211
        self.simpleJava_expression_aux214 = simpleJava_expression_aux214
        self.simpleJava_expression_aux212 = simpleJava_expression_aux212
        
    @property
    def operador(self) -> str:
        return self.__operador

    @operador.setter
    def operador(self, operador: str):
        self.__operador = operador

    @property
    def simpleJava_expression_aux(self):
        return self.__simpleJava_expression_aux

    @simpleJava_expression_aux.setter
    def simpleJava_expression_aux(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression_aux__simpleJava_expression_aux", None)
        self.__simpleJava_expression_aux = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_arglist"):
                opp_val = getattr(old_value, "simpleJava_arglist", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_arglist", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_arglist"):
                opp_val = getattr(value, "simpleJava_arglist", None)
                setattr(value, "simpleJava_arglist", self)

    @property
    def simpleJava_expression_aux208(self):
        return self.__simpleJava_expression_aux208

    @simpleJava_expression_aux208.setter
    def simpleJava_expression_aux208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression_aux__simpleJava_expression_aux208", None)
        self.__simpleJava_expression_aux208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression209"):
                opp_val = getattr(old_value, "simpleJava_expression209", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression209"):
                opp_val = getattr(value, "simpleJava_expression209", None)
                setattr(value, "simpleJava_expression209", self)

    @property
    def simpleJava_expression_aux211(self):
        return self.__simpleJava_expression_aux211

    @simpleJava_expression_aux211.setter
    def simpleJava_expression_aux211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression_aux__simpleJava_expression_aux211", None)
        self.__simpleJava_expression_aux211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_mais_aux"):
                opp_val = getattr(old_value, "simpleJava_mais_aux", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_mais_aux", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_mais_aux"):
                opp_val = getattr(value, "simpleJava_mais_aux", None)
                setattr(value, "simpleJava_mais_aux", self)

    @property
    def simpleJava_expression_aux212(self):
        return self.__simpleJava_expression_aux212

    @simpleJava_expression_aux212.setter
    def simpleJava_expression_aux212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression_aux__simpleJava_expression_aux212", None)
        self.__simpleJava_expression_aux212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression_aux214"):
                opp_val = getattr(old_value, "simpleJava_expression_aux214", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression_aux214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression_aux214"):
                opp_val = getattr(value, "simpleJava_expression_aux214", None)
                setattr(value, "simpleJava_expression_aux214", self)

    @property
    def simpleJava_expression_aux214(self):
        return self.__simpleJava_expression_aux214

    @simpleJava_expression_aux214.setter
    def simpleJava_expression_aux214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression_aux__simpleJava_expression_aux214", None)
        self.__simpleJava_expression_aux214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression_aux212"):
                opp_val = getattr(old_value, "simpleJava_expression_aux212", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression_aux212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression_aux212"):
                opp_val = getattr(value, "simpleJava_expression_aux212", None)
                setattr(value, "simpleJava_expression_aux212", self)

class simpleJava_literal_expression:

    def __init__(self, decimal: str, inteiro: str, l_float: str, string: str, simpleJava_literal_expression: "simpleJava_expression" = None):
        self.decimal = decimal
        self.inteiro = inteiro
        self.l_float = l_float
        self.string = string
        self.simpleJava_literal_expression = simpleJava_literal_expression
        
    @property
    def l_float(self) -> str:
        return self.__l_float

    @l_float.setter
    def l_float(self, l_float: str):
        self.__l_float = l_float

    @property
    def inteiro(self) -> str:
        return self.__inteiro

    @inteiro.setter
    def inteiro(self, inteiro: str):
        self.__inteiro = inteiro

    @property
    def decimal(self) -> str:
        return self.__decimal

    @decimal.setter
    def decimal(self, decimal: str):
        self.__decimal = decimal

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def simpleJava_literal_expression(self):
        return self.__simpleJava_literal_expression

    @simpleJava_literal_expression.setter
    def simpleJava_literal_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_literal_expression__simpleJava_literal_expression", None)
        self.__simpleJava_literal_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression205"):
                opp_val = getattr(old_value, "simpleJava_expression205", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression205"):
                opp_val = getattr(value, "simpleJava_expression205", None)
                setattr(value, "simpleJava_expression205", self)

class simpleJava_numeric_expression:

    def __init__(self, operador: str, simpleJava_numeric_expression: "simpleJava_expression" = None, simpleJava_numeric_expression227: "simpleJava_expression" = None):
        self.operador = operador
        self.simpleJava_numeric_expression = simpleJava_numeric_expression
        self.simpleJava_numeric_expression227 = simpleJava_numeric_expression227
        
    @property
    def operador(self) -> str:
        return self.__operador

    @operador.setter
    def operador(self, operador: str):
        self.__operador = operador

    @property
    def simpleJava_numeric_expression(self):
        return self.__simpleJava_numeric_expression

    @simpleJava_numeric_expression.setter
    def simpleJava_numeric_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_numeric_expression__simpleJava_numeric_expression", None)
        self.__simpleJava_numeric_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression198"):
                opp_val = getattr(old_value, "simpleJava_expression198", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression198"):
                opp_val = getattr(value, "simpleJava_expression198", None)
                setattr(value, "simpleJava_expression198", self)

    @property
    def simpleJava_numeric_expression227(self):
        return self.__simpleJava_numeric_expression227

    @simpleJava_numeric_expression227.setter
    def simpleJava_numeric_expression227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_numeric_expression__simpleJava_numeric_expression227", None)
        self.__simpleJava_numeric_expression227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression228"):
                opp_val = getattr(old_value, "simpleJava_expression228", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression228"):
                opp_val = getattr(value, "simpleJava_expression228", None)
                setattr(value, "simpleJava_expression228", self)

class simpleJava_logical_expression:

    def __init__(self, operador: str, simpleJava_logical_expression: "simpleJava_expression" = None, simpleJava_logical_expression221: "simpleJava_expression" = None):
        self.operador = operador
        self.simpleJava_logical_expression = simpleJava_logical_expression
        self.simpleJava_logical_expression221 = simpleJava_logical_expression221
        
    @property
    def operador(self) -> str:
        return self.__operador

    @operador.setter
    def operador(self, operador: str):
        self.__operador = operador

    @property
    def simpleJava_logical_expression(self):
        return self.__simpleJava_logical_expression

    @simpleJava_logical_expression.setter
    def simpleJava_logical_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_logical_expression__simpleJava_logical_expression", None)
        self.__simpleJava_logical_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression196"):
                opp_val = getattr(old_value, "simpleJava_expression196", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression196"):
                opp_val = getattr(value, "simpleJava_expression196", None)
                setattr(value, "simpleJava_expression196", self)

    @property
    def simpleJava_logical_expression221(self):
        return self.__simpleJava_logical_expression221

    @simpleJava_logical_expression221.setter
    def simpleJava_logical_expression221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_logical_expression__simpleJava_logical_expression221", None)
        self.__simpleJava_logical_expression221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression222"):
                opp_val = getattr(old_value, "simpleJava_expression222", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression222"):
                opp_val = getattr(value, "simpleJava_expression222", None)
                setattr(value, "simpleJava_expression222", self)

class expression_aux:

    pass
class simpleJava_aux(creating_aux, expression_aux):

    pass
class expression:

    pass
class simpleJava_exp_aux(expression):

    pass
class simpleJava_newBlock:

    pass
class simpleJava_type_specifier:

    def __init__(self, nome: str, simpleJava_type_specifier: "simpleJava_creating_expression" = None, simpleJava_type_specifier242: "simpleJava_type" = None):
        self.nome = nome
        self.simpleJava_type_specifier = simpleJava_type_specifier
        self.simpleJava_type_specifier242 = simpleJava_type_specifier242
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def simpleJava_type_specifier242(self):
        return self.__simpleJava_type_specifier242

    @simpleJava_type_specifier242.setter
    def simpleJava_type_specifier242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_type_specifier__simpleJava_type_specifier242", None)
        self.__simpleJava_type_specifier242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_type241"):
                opp_val = getattr(old_value, "simpleJava_type241", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_type241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_type241"):
                opp_val = getattr(value, "simpleJava_type241", None)
                setattr(value, "simpleJava_type241", self)

    @property
    def simpleJava_type_specifier(self):
        return self.__simpleJava_type_specifier

    @simpleJava_type_specifier.setter
    def simpleJava_type_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_type_specifier__simpleJava_type_specifier", None)
        self.__simpleJava_type_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_creating_expression187"):
                opp_val = getattr(old_value, "simpleJava_creating_expression187", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_creating_expression187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_creating_expression187"):
                opp_val = getattr(value, "simpleJava_creating_expression187", None)
                setattr(value, "simpleJava_creating_expression187", self)

class simpleJava_creating_aux:

    pass
class simpleJava_bit_expression:

    def __init__(self, operador: str, simpleJava_bit_expression: "simpleJava_expression" = None, simpleJava_bit_expression224: "simpleJava_expression" = None):
        self.operador = operador
        self.simpleJava_bit_expression = simpleJava_bit_expression
        self.simpleJava_bit_expression224 = simpleJava_bit_expression224
        
    @property
    def operador(self) -> str:
        return self.__operador

    @operador.setter
    def operador(self, operador: str):
        self.__operador = operador

    @property
    def simpleJava_bit_expression224(self):
        return self.__simpleJava_bit_expression224

    @simpleJava_bit_expression224.setter
    def simpleJava_bit_expression224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_bit_expression__simpleJava_bit_expression224", None)
        self.__simpleJava_bit_expression224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression225"):
                opp_val = getattr(old_value, "simpleJava_expression225", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression225"):
                opp_val = getattr(value, "simpleJava_expression225", None)
                setattr(value, "simpleJava_expression225", self)

    @property
    def simpleJava_bit_expression(self):
        return self.__simpleJava_bit_expression

    @simpleJava_bit_expression.setter
    def simpleJava_bit_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_bit_expression__simpleJava_bit_expression", None)
        self.__simpleJava_bit_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression200"):
                opp_val = getattr(old_value, "simpleJava_expression200", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression200"):
                opp_val = getattr(value, "simpleJava_expression200", None)
                setattr(value, "simpleJava_expression200", self)

class newBlock:

    pass
class simpleJava_creating_expression:

    pass
class simpleJava_variable_initializer:

    pass
class simpleJava_switch_statement:

    pass
class simpleJava_try_statement:

    pass
class simpleJava_for_statement:

    pass
class simpleJava_variable_declarator:

    def __init__(self, nomeVariavel: str, op: str, simpleJava_variable_declarator: "simpleJava_variable_declaration" = None, simpleJava_variable_declarator106: "simpleJava_variable_initializer" = None):
        self.nomeVariavel = nomeVariavel
        self.op = op
        self.simpleJava_variable_declarator = simpleJava_variable_declarator
        self.simpleJava_variable_declarator106 = simpleJava_variable_declarator106
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nomeVariavel(self) -> str:
        return self.__nomeVariavel

    @nomeVariavel.setter
    def nomeVariavel(self, nomeVariavel: str):
        self.__nomeVariavel = nomeVariavel

    @property
    def simpleJava_variable_declarator106(self):
        return self.__simpleJava_variable_declarator106

    @simpleJava_variable_declarator106.setter
    def simpleJava_variable_declarator106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_variable_declarator__simpleJava_variable_declarator106", None)
        self.__simpleJava_variable_declarator106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_variable_initializer"):
                opp_val = getattr(old_value, "simpleJava_variable_initializer", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_variable_initializer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_variable_initializer"):
                opp_val = getattr(value, "simpleJava_variable_initializer", None)
                setattr(value, "simpleJava_variable_initializer", self)

    @property
    def simpleJava_variable_declarator(self):
        return self.__simpleJava_variable_declarator

    @simpleJava_variable_declarator.setter
    def simpleJava_variable_declarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_variable_declarator__simpleJava_variable_declarator", None)
        self.__simpleJava_variable_declarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_variable_declaration101"):
                opp_val = getattr(old_value, "simpleJava_variable_declaration101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_variable_declaration101"):
                opp_val = getattr(value, "simpleJava_variable_declaration101", None)
                if opp_val is None:
                    setattr(value, "simpleJava_variable_declaration101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleJava_expression(expression_aux):

    def __init__(self, identificador: str, simpleJava_expression: "simpleJava_statement" = None, simpleJava_expression84: "simpleJava_statement" = None, simpleJava_expression90: "simpleJava_statement" = None, simpleJava_expression93: "simpleJava_statement" = None, simpleJava_expression127: "simpleJava_do_statement" = None, simpleJava_expression109: "simpleJava_variable_initializer" = None, simpleJava_expression115: "simpleJava_if_statement" = None, simpleJava_expression130: "simpleJava_while_statement" = None, simpleJava_expression139: "simpleJava_for_statement" = None, simpleJava_expression142: "simpleJava_for_statement" = None, simpleJava_expression145: "simpleJava_for_statement" = None, simpleJava_expression163: "simpleJava_switch_statement" = None, simpleJava_expression166: "simpleJava_switch_statement" = None, simpleJava_expression200: "simpleJava_bit_expression" = None, simpleJava_expression190: "simpleJava_creating_expression" = None, simpleJava_expression194: "simpleJava_exp_aux" = None, simpleJava_expression196: "simpleJava_logical_expression" = None, simpleJava_expression198: "simpleJava_numeric_expression" = None, simpleJava_expression219: "simpleJava_aux" = None, simpleJava_expression202: "simpleJava_creating_expression" = None, simpleJava_expression205: "simpleJava_literal_expression" = None, simpleJava_expression209: "simpleJava_expression_aux" = None, simpleJava_expression222: "simpleJava_logical_expression" = None, simpleJava_expression225: "simpleJava_bit_expression" = None, simpleJava_expression228: "simpleJava_numeric_expression" = None, simpleJava_expression231: "simpleJava_arglist" = None):
        self.identificador = identificador
        self.simpleJava_expression = simpleJava_expression
        self.simpleJava_expression84 = simpleJava_expression84
        self.simpleJava_expression90 = simpleJava_expression90
        self.simpleJava_expression93 = simpleJava_expression93
        self.simpleJava_expression127 = simpleJava_expression127
        self.simpleJava_expression109 = simpleJava_expression109
        self.simpleJava_expression115 = simpleJava_expression115
        self.simpleJava_expression130 = simpleJava_expression130
        self.simpleJava_expression139 = simpleJava_expression139
        self.simpleJava_expression142 = simpleJava_expression142
        self.simpleJava_expression145 = simpleJava_expression145
        self.simpleJava_expression163 = simpleJava_expression163
        self.simpleJava_expression166 = simpleJava_expression166
        self.simpleJava_expression200 = simpleJava_expression200
        self.simpleJava_expression190 = simpleJava_expression190
        self.simpleJava_expression194 = simpleJava_expression194
        self.simpleJava_expression196 = simpleJava_expression196
        self.simpleJava_expression198 = simpleJava_expression198
        self.simpleJava_expression219 = simpleJava_expression219
        self.simpleJava_expression202 = simpleJava_expression202
        self.simpleJava_expression205 = simpleJava_expression205
        self.simpleJava_expression209 = simpleJava_expression209
        self.simpleJava_expression222 = simpleJava_expression222
        self.simpleJava_expression225 = simpleJava_expression225
        self.simpleJava_expression228 = simpleJava_expression228
        self.simpleJava_expression231 = simpleJava_expression231
        
    @property
    def identificador(self) -> str:
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador: str):
        self.__identificador = identificador

    @property
    def simpleJava_expression205(self):
        return self.__simpleJava_expression205

    @simpleJava_expression205.setter
    def simpleJava_expression205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression205", None)
        self.__simpleJava_expression205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_literal_expression"):
                opp_val = getattr(old_value, "simpleJava_literal_expression", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_literal_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_literal_expression"):
                opp_val = getattr(value, "simpleJava_literal_expression", None)
                setattr(value, "simpleJava_literal_expression", self)

    @property
    def simpleJava_expression190(self):
        return self.__simpleJava_expression190

    @simpleJava_expression190.setter
    def simpleJava_expression190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression190", None)
        self.__simpleJava_expression190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_creating_expression189"):
                opp_val = getattr(old_value, "simpleJava_creating_expression189", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_creating_expression189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_creating_expression189"):
                opp_val = getattr(value, "simpleJava_creating_expression189", None)
                setattr(value, "simpleJava_creating_expression189", self)

    @property
    def simpleJava_expression200(self):
        return self.__simpleJava_expression200

    @simpleJava_expression200.setter
    def simpleJava_expression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression200", None)
        self.__simpleJava_expression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_bit_expression"):
                opp_val = getattr(old_value, "simpleJava_bit_expression", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_bit_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_bit_expression"):
                opp_val = getattr(value, "simpleJava_bit_expression", None)
                setattr(value, "simpleJava_bit_expression", self)

    @property
    def simpleJava_expression130(self):
        return self.__simpleJava_expression130

    @simpleJava_expression130.setter
    def simpleJava_expression130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression130", None)
        self.__simpleJava_expression130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_while_statement129"):
                opp_val = getattr(old_value, "simpleJava_while_statement129", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_while_statement129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_while_statement129"):
                opp_val = getattr(value, "simpleJava_while_statement129", None)
                setattr(value, "simpleJava_while_statement129", self)

    @property
    def simpleJava_expression194(self):
        return self.__simpleJava_expression194

    @simpleJava_expression194.setter
    def simpleJava_expression194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression194", None)
        self.__simpleJava_expression194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_exp_aux"):
                opp_val = getattr(old_value, "simpleJava_exp_aux", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_exp_aux", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_exp_aux"):
                opp_val = getattr(value, "simpleJava_exp_aux", None)
                setattr(value, "simpleJava_exp_aux", self)

    @property
    def simpleJava_expression198(self):
        return self.__simpleJava_expression198

    @simpleJava_expression198.setter
    def simpleJava_expression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression198", None)
        self.__simpleJava_expression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_numeric_expression"):
                opp_val = getattr(old_value, "simpleJava_numeric_expression", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_numeric_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_numeric_expression"):
                opp_val = getattr(value, "simpleJava_numeric_expression", None)
                setattr(value, "simpleJava_numeric_expression", self)

    @property
    def simpleJava_expression139(self):
        return self.__simpleJava_expression139

    @simpleJava_expression139.setter
    def simpleJava_expression139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression139", None)
        self.__simpleJava_expression139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_for_statement138"):
                opp_val = getattr(old_value, "simpleJava_for_statement138", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_for_statement138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_for_statement138"):
                opp_val = getattr(value, "simpleJava_for_statement138", None)
                setattr(value, "simpleJava_for_statement138", self)

    @property
    def simpleJava_expression93(self):
        return self.__simpleJava_expression93

    @simpleJava_expression93.setter
    def simpleJava_expression93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression93", None)
        self.__simpleJava_expression93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_statement92"):
                opp_val = getattr(old_value, "simpleJava_statement92", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_statement92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_statement92"):
                opp_val = getattr(value, "simpleJava_statement92", None)
                setattr(value, "simpleJava_statement92", self)

    @property
    def simpleJava_expression225(self):
        return self.__simpleJava_expression225

    @simpleJava_expression225.setter
    def simpleJava_expression225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression225", None)
        self.__simpleJava_expression225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_bit_expression224"):
                opp_val = getattr(old_value, "simpleJava_bit_expression224", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_bit_expression224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_bit_expression224"):
                opp_val = getattr(value, "simpleJava_bit_expression224", None)
                setattr(value, "simpleJava_bit_expression224", self)

    @property
    def simpleJava_expression145(self):
        return self.__simpleJava_expression145

    @simpleJava_expression145.setter
    def simpleJava_expression145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression145", None)
        self.__simpleJava_expression145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_for_statement144"):
                opp_val = getattr(old_value, "simpleJava_for_statement144", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_for_statement144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_for_statement144"):
                opp_val = getattr(value, "simpleJava_for_statement144", None)
                setattr(value, "simpleJava_for_statement144", self)

    @property
    def simpleJava_expression166(self):
        return self.__simpleJava_expression166

    @simpleJava_expression166.setter
    def simpleJava_expression166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression166", None)
        self.__simpleJava_expression166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_switch_statement165"):
                opp_val = getattr(old_value, "simpleJava_switch_statement165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_switch_statement165"):
                opp_val = getattr(value, "simpleJava_switch_statement165", None)
                if opp_val is None:
                    setattr(value, "simpleJava_switch_statement165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleJava_expression(self):
        return self.__simpleJava_expression

    @simpleJava_expression.setter
    def simpleJava_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression", None)
        self.__simpleJava_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_statement66"):
                opp_val = getattr(old_value, "simpleJava_statement66", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_statement66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_statement66"):
                opp_val = getattr(value, "simpleJava_statement66", None)
                setattr(value, "simpleJava_statement66", self)

    @property
    def simpleJava_expression209(self):
        return self.__simpleJava_expression209

    @simpleJava_expression209.setter
    def simpleJava_expression209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression209", None)
        self.__simpleJava_expression209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression_aux208"):
                opp_val = getattr(old_value, "simpleJava_expression_aux208", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression_aux208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression_aux208"):
                opp_val = getattr(value, "simpleJava_expression_aux208", None)
                setattr(value, "simpleJava_expression_aux208", self)

    @property
    def simpleJava_expression109(self):
        return self.__simpleJava_expression109

    @simpleJava_expression109.setter
    def simpleJava_expression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression109", None)
        self.__simpleJava_expression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_variable_initializer108"):
                opp_val = getattr(old_value, "simpleJava_variable_initializer108", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_variable_initializer108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_variable_initializer108"):
                opp_val = getattr(value, "simpleJava_variable_initializer108", None)
                setattr(value, "simpleJava_variable_initializer108", self)

    @property
    def simpleJava_expression219(self):
        return self.__simpleJava_expression219

    @simpleJava_expression219.setter
    def simpleJava_expression219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression219", None)
        self.__simpleJava_expression219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_aux"):
                opp_val = getattr(old_value, "simpleJava_aux", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_aux", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_aux"):
                opp_val = getattr(value, "simpleJava_aux", None)
                setattr(value, "simpleJava_aux", self)

    @property
    def simpleJava_expression231(self):
        return self.__simpleJava_expression231

    @simpleJava_expression231.setter
    def simpleJava_expression231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression231", None)
        self.__simpleJava_expression231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_arglist230"):
                opp_val = getattr(old_value, "simpleJava_arglist230", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_arglist230"):
                opp_val = getattr(value, "simpleJava_arglist230", None)
                if opp_val is None:
                    setattr(value, "simpleJava_arglist230", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleJava_expression222(self):
        return self.__simpleJava_expression222

    @simpleJava_expression222.setter
    def simpleJava_expression222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression222", None)
        self.__simpleJava_expression222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_logical_expression221"):
                opp_val = getattr(old_value, "simpleJava_logical_expression221", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_logical_expression221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_logical_expression221"):
                opp_val = getattr(value, "simpleJava_logical_expression221", None)
                setattr(value, "simpleJava_logical_expression221", self)

    @property
    def simpleJava_expression84(self):
        return self.__simpleJava_expression84

    @simpleJava_expression84.setter
    def simpleJava_expression84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression84", None)
        self.__simpleJava_expression84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_statement83"):
                opp_val = getattr(old_value, "simpleJava_statement83", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_statement83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_statement83"):
                opp_val = getattr(value, "simpleJava_statement83", None)
                setattr(value, "simpleJava_statement83", self)

    @property
    def simpleJava_expression202(self):
        return self.__simpleJava_expression202

    @simpleJava_expression202.setter
    def simpleJava_expression202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression202", None)
        self.__simpleJava_expression202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_creating_expression203"):
                opp_val = getattr(old_value, "simpleJava_creating_expression203", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_creating_expression203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_creating_expression203"):
                opp_val = getattr(value, "simpleJava_creating_expression203", None)
                setattr(value, "simpleJava_creating_expression203", self)

    @property
    def simpleJava_expression228(self):
        return self.__simpleJava_expression228

    @simpleJava_expression228.setter
    def simpleJava_expression228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression228", None)
        self.__simpleJava_expression228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_numeric_expression227"):
                opp_val = getattr(old_value, "simpleJava_numeric_expression227", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_numeric_expression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_numeric_expression227"):
                opp_val = getattr(value, "simpleJava_numeric_expression227", None)
                setattr(value, "simpleJava_numeric_expression227", self)

    @property
    def simpleJava_expression90(self):
        return self.__simpleJava_expression90

    @simpleJava_expression90.setter
    def simpleJava_expression90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression90", None)
        self.__simpleJava_expression90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_statement89"):
                opp_val = getattr(old_value, "simpleJava_statement89", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_statement89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_statement89"):
                opp_val = getattr(value, "simpleJava_statement89", None)
                setattr(value, "simpleJava_statement89", self)

    @property
    def simpleJava_expression127(self):
        return self.__simpleJava_expression127

    @simpleJava_expression127.setter
    def simpleJava_expression127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression127", None)
        self.__simpleJava_expression127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_do_statement126"):
                opp_val = getattr(old_value, "simpleJava_do_statement126", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_do_statement126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_do_statement126"):
                opp_val = getattr(value, "simpleJava_do_statement126", None)
                setattr(value, "simpleJava_do_statement126", self)

    @property
    def simpleJava_expression163(self):
        return self.__simpleJava_expression163

    @simpleJava_expression163.setter
    def simpleJava_expression163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression163", None)
        self.__simpleJava_expression163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_switch_statement162"):
                opp_val = getattr(old_value, "simpleJava_switch_statement162", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_switch_statement162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_switch_statement162"):
                opp_val = getattr(value, "simpleJava_switch_statement162", None)
                setattr(value, "simpleJava_switch_statement162", self)

    @property
    def simpleJava_expression196(self):
        return self.__simpleJava_expression196

    @simpleJava_expression196.setter
    def simpleJava_expression196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression196", None)
        self.__simpleJava_expression196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_logical_expression"):
                opp_val = getattr(old_value, "simpleJava_logical_expression", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_logical_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_logical_expression"):
                opp_val = getattr(value, "simpleJava_logical_expression", None)
                setattr(value, "simpleJava_logical_expression", self)

    @property
    def simpleJava_expression115(self):
        return self.__simpleJava_expression115

    @simpleJava_expression115.setter
    def simpleJava_expression115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression115", None)
        self.__simpleJava_expression115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_if_statement114"):
                opp_val = getattr(old_value, "simpleJava_if_statement114", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_if_statement114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_if_statement114"):
                opp_val = getattr(value, "simpleJava_if_statement114", None)
                setattr(value, "simpleJava_if_statement114", self)

    @property
    def simpleJava_expression142(self):
        return self.__simpleJava_expression142

    @simpleJava_expression142.setter
    def simpleJava_expression142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_expression__simpleJava_expression142", None)
        self.__simpleJava_expression142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_for_statement141"):
                opp_val = getattr(old_value, "simpleJava_for_statement141", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_for_statement141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_for_statement141"):
                opp_val = getattr(value, "simpleJava_for_statement141", None)
                setattr(value, "simpleJava_for_statement141", self)

class simpleJava_statement:

    def __init__(self, break: str, continue: str, simpleJava_statement71: "simpleJava_if_statement" = None, simpleJava_statement73: "simpleJava_do_statement" = None, simpleJava_statement: "simpleJava_statement_block" = None, simpleJava_statement63: "simpleJava_variable_declaration" = None, simpleJava_statement66: "simpleJava_expression" = None, simpleJava_statement68: "simpleJava_statement_block" = None, simpleJava_statement75: "simpleJava_while_statement" = None, simpleJava_statement77: "simpleJava_for_statement" = None, simpleJava_statement79: "simpleJava_try_statement" = None, simpleJava_statement81: "simpleJava_switch_statement" = None, simpleJava_statement83: "simpleJava_expression" = None, simpleJava_statement87: "simpleJava_statement" = None, simpleJava_statement85: "simpleJava_statement" = None, simpleJava_statement89: "simpleJava_expression" = None, simpleJava_statement92: "simpleJava_expression" = None, simpleJava_statement124: "simpleJava_do_statement" = None, simpleJava_statement118: "simpleJava_if_statement" = None, simpleJava_statement121: "simpleJava_if_statement" = None, simpleJava_statement133: "simpleJava_while_statement" = None, simpleJava_statement148: "simpleJava_for_statement" = None, simpleJava_statement169: "simpleJava_switch_statement" = None):
        self.break = break
        self.continue = continue
        self.simpleJava_statement71 = simpleJava_statement71
        self.simpleJava_statement73 = simpleJava_statement73
        self.simpleJava_statement = simpleJava_statement
        self.simpleJava_statement63 = simpleJava_statement63
        self.simpleJava_statement66 = simpleJava_statement66
        self.simpleJava_statement68 = simpleJava_statement68
        self.simpleJava_statement75 = simpleJava_statement75
        self.simpleJava_statement77 = simpleJava_statement77
        self.simpleJava_statement79 = simpleJava_statement79
        self.simpleJava_statement81 = simpleJava_statement81
        self.simpleJava_statement83 = simpleJava_statement83
        self.simpleJava_statement87 = simpleJava_statement87
        self.simpleJava_statement85 = simpleJava_statement85
        self.simpleJava_statement89 = simpleJava_statement89
        self.simpleJava_statement92 = simpleJava_statement92
        self.simpleJava_statement124 = simpleJava_statement124
        self.simpleJava_statement118 = simpleJava_statement118
        self.simpleJava_statement121 = simpleJava_statement121
        self.simpleJava_statement133 = simpleJava_statement133
        self.simpleJava_statement148 = simpleJava_statement148
        self.simpleJava_statement169 = simpleJava_statement169
        
    @property
    def break(self) -> str:
        return self.__break

    @break.setter
    def break(self, break: str):
        self.__break = break

    @property
    def continue(self) -> str:
        return self.__continue

    @continue.setter
    def continue(self, continue: str):
        self.__continue = continue

    @property
    def simpleJava_statement121(self):
        return self.__simpleJava_statement121

    @simpleJava_statement121.setter
    def simpleJava_statement121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement121", None)
        self.__simpleJava_statement121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_if_statement120"):
                opp_val = getattr(old_value, "simpleJava_if_statement120", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_if_statement120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_if_statement120"):
                opp_val = getattr(value, "simpleJava_if_statement120", None)
                setattr(value, "simpleJava_if_statement120", self)

    @property
    def simpleJava_statement68(self):
        return self.__simpleJava_statement68

    @simpleJava_statement68.setter
    def simpleJava_statement68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement68", None)
        self.__simpleJava_statement68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_statement_block69"):
                opp_val = getattr(old_value, "simpleJava_statement_block69", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_statement_block69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_statement_block69"):
                opp_val = getattr(value, "simpleJava_statement_block69", None)
                setattr(value, "simpleJava_statement_block69", self)

    @property
    def simpleJava_statement169(self):
        return self.__simpleJava_statement169

    @simpleJava_statement169.setter
    def simpleJava_statement169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement169", None)
        self.__simpleJava_statement169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_switch_statement168"):
                opp_val = getattr(old_value, "simpleJava_switch_statement168", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_switch_statement168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_switch_statement168"):
                opp_val = getattr(value, "simpleJava_switch_statement168", None)
                setattr(value, "simpleJava_switch_statement168", self)

    @property
    def simpleJava_statement83(self):
        return self.__simpleJava_statement83

    @simpleJava_statement83.setter
    def simpleJava_statement83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement83", None)
        self.__simpleJava_statement83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression84"):
                opp_val = getattr(old_value, "simpleJava_expression84", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression84"):
                opp_val = getattr(value, "simpleJava_expression84", None)
                setattr(value, "simpleJava_expression84", self)

    @property
    def simpleJava_statement63(self):
        return self.__simpleJava_statement63

    @simpleJava_statement63.setter
    def simpleJava_statement63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement63", None)
        self.__simpleJava_statement63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_variable_declaration64"):
                opp_val = getattr(old_value, "simpleJava_variable_declaration64", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_variable_declaration64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_variable_declaration64"):
                opp_val = getattr(value, "simpleJava_variable_declaration64", None)
                setattr(value, "simpleJava_variable_declaration64", self)

    @property
    def simpleJava_statement124(self):
        return self.__simpleJava_statement124

    @simpleJava_statement124.setter
    def simpleJava_statement124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement124", None)
        self.__simpleJava_statement124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_do_statement123"):
                opp_val = getattr(old_value, "simpleJava_do_statement123", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_do_statement123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_do_statement123"):
                opp_val = getattr(value, "simpleJava_do_statement123", None)
                setattr(value, "simpleJava_do_statement123", self)

    @property
    def simpleJava_statement92(self):
        return self.__simpleJava_statement92

    @simpleJava_statement92.setter
    def simpleJava_statement92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement92", None)
        self.__simpleJava_statement92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression93"):
                opp_val = getattr(old_value, "simpleJava_expression93", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression93"):
                opp_val = getattr(value, "simpleJava_expression93", None)
                setattr(value, "simpleJava_expression93", self)

    @property
    def simpleJava_statement85(self):
        return self.__simpleJava_statement85

    @simpleJava_statement85.setter
    def simpleJava_statement85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement85", None)
        self.__simpleJava_statement85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_statement87"):
                opp_val = getattr(old_value, "simpleJava_statement87", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_statement87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_statement87"):
                opp_val = getattr(value, "simpleJava_statement87", None)
                setattr(value, "simpleJava_statement87", self)

    @property
    def simpleJava_statement81(self):
        return self.__simpleJava_statement81

    @simpleJava_statement81.setter
    def simpleJava_statement81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement81", None)
        self.__simpleJava_statement81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_switch_statement"):
                opp_val = getattr(old_value, "simpleJava_switch_statement", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_switch_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_switch_statement"):
                opp_val = getattr(value, "simpleJava_switch_statement", None)
                setattr(value, "simpleJava_switch_statement", self)

    @property
    def simpleJava_statement118(self):
        return self.__simpleJava_statement118

    @simpleJava_statement118.setter
    def simpleJava_statement118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement118", None)
        self.__simpleJava_statement118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_if_statement117"):
                opp_val = getattr(old_value, "simpleJava_if_statement117", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_if_statement117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_if_statement117"):
                opp_val = getattr(value, "simpleJava_if_statement117", None)
                setattr(value, "simpleJava_if_statement117", self)

    @property
    def simpleJava_statement79(self):
        return self.__simpleJava_statement79

    @simpleJava_statement79.setter
    def simpleJava_statement79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement79", None)
        self.__simpleJava_statement79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_try_statement"):
                opp_val = getattr(old_value, "simpleJava_try_statement", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_try_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_try_statement"):
                opp_val = getattr(value, "simpleJava_try_statement", None)
                setattr(value, "simpleJava_try_statement", self)

    @property
    def simpleJava_statement66(self):
        return self.__simpleJava_statement66

    @simpleJava_statement66.setter
    def simpleJava_statement66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement66", None)
        self.__simpleJava_statement66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression"):
                opp_val = getattr(old_value, "simpleJava_expression", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression"):
                opp_val = getattr(value, "simpleJava_expression", None)
                setattr(value, "simpleJava_expression", self)

    @property
    def simpleJava_statement71(self):
        return self.__simpleJava_statement71

    @simpleJava_statement71.setter
    def simpleJava_statement71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement71", None)
        self.__simpleJava_statement71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_if_statement"):
                opp_val = getattr(old_value, "simpleJava_if_statement", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_if_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_if_statement"):
                opp_val = getattr(value, "simpleJava_if_statement", None)
                setattr(value, "simpleJava_if_statement", self)

    @property
    def simpleJava_statement(self):
        return self.__simpleJava_statement

    @simpleJava_statement.setter
    def simpleJava_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement", None)
        self.__simpleJava_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_statement_block61"):
                opp_val = getattr(old_value, "simpleJava_statement_block61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_statement_block61"):
                opp_val = getattr(value, "simpleJava_statement_block61", None)
                if opp_val is None:
                    setattr(value, "simpleJava_statement_block61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleJava_statement133(self):
        return self.__simpleJava_statement133

    @simpleJava_statement133.setter
    def simpleJava_statement133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement133", None)
        self.__simpleJava_statement133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_while_statement132"):
                opp_val = getattr(old_value, "simpleJava_while_statement132", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_while_statement132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_while_statement132"):
                opp_val = getattr(value, "simpleJava_while_statement132", None)
                setattr(value, "simpleJava_while_statement132", self)

    @property
    def simpleJava_statement89(self):
        return self.__simpleJava_statement89

    @simpleJava_statement89.setter
    def simpleJava_statement89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement89", None)
        self.__simpleJava_statement89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_expression90"):
                opp_val = getattr(old_value, "simpleJava_expression90", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_expression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_expression90"):
                opp_val = getattr(value, "simpleJava_expression90", None)
                setattr(value, "simpleJava_expression90", self)

    @property
    def simpleJava_statement87(self):
        return self.__simpleJava_statement87

    @simpleJava_statement87.setter
    def simpleJava_statement87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement87", None)
        self.__simpleJava_statement87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_statement85"):
                opp_val = getattr(old_value, "simpleJava_statement85", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_statement85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_statement85"):
                opp_val = getattr(value, "simpleJava_statement85", None)
                setattr(value, "simpleJava_statement85", self)

    @property
    def simpleJava_statement73(self):
        return self.__simpleJava_statement73

    @simpleJava_statement73.setter
    def simpleJava_statement73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement73", None)
        self.__simpleJava_statement73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_do_statement"):
                opp_val = getattr(old_value, "simpleJava_do_statement", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_do_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_do_statement"):
                opp_val = getattr(value, "simpleJava_do_statement", None)
                setattr(value, "simpleJava_do_statement", self)

    @property
    def simpleJava_statement148(self):
        return self.__simpleJava_statement148

    @simpleJava_statement148.setter
    def simpleJava_statement148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement148", None)
        self.__simpleJava_statement148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_for_statement147"):
                opp_val = getattr(old_value, "simpleJava_for_statement147", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_for_statement147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_for_statement147"):
                opp_val = getattr(value, "simpleJava_for_statement147", None)
                setattr(value, "simpleJava_for_statement147", self)

    @property
    def simpleJava_statement77(self):
        return self.__simpleJava_statement77

    @simpleJava_statement77.setter
    def simpleJava_statement77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement77", None)
        self.__simpleJava_statement77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_for_statement"):
                opp_val = getattr(old_value, "simpleJava_for_statement", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_for_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_for_statement"):
                opp_val = getattr(value, "simpleJava_for_statement", None)
                setattr(value, "simpleJava_for_statement", self)

    @property
    def simpleJava_statement75(self):
        return self.__simpleJava_statement75

    @simpleJava_statement75.setter
    def simpleJava_statement75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_statement__simpleJava_statement75", None)
        self.__simpleJava_statement75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_while_statement"):
                opp_val = getattr(old_value, "simpleJava_while_statement", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_while_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_while_statement"):
                opp_val = getattr(value, "simpleJava_while_statement", None)
                setattr(value, "simpleJava_while_statement", self)

class simpleJava_parameter:

    def __init__(self, nomeParametro: str, simpleJava_parameter: "simpleJava_type" = None, simpleJava_parameter59: "simpleJava_parameter_list" = None, simpleJava_parameter154: "simpleJava_try_statement" = None):
        self.nomeParametro = nomeParametro
        self.simpleJava_parameter = simpleJava_parameter
        self.simpleJava_parameter59 = simpleJava_parameter59
        self.simpleJava_parameter154 = simpleJava_parameter154
        
    @property
    def nomeParametro(self) -> str:
        return self.__nomeParametro

    @nomeParametro.setter
    def nomeParametro(self, nomeParametro: str):
        self.__nomeParametro = nomeParametro

    @property
    def simpleJava_parameter154(self):
        return self.__simpleJava_parameter154

    @simpleJava_parameter154.setter
    def simpleJava_parameter154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_parameter__simpleJava_parameter154", None)
        self.__simpleJava_parameter154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_try_statement153"):
                opp_val = getattr(old_value, "simpleJava_try_statement153", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_try_statement153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_try_statement153"):
                opp_val = getattr(value, "simpleJava_try_statement153", None)
                setattr(value, "simpleJava_try_statement153", self)

    @property
    def simpleJava_parameter(self):
        return self.__simpleJava_parameter

    @simpleJava_parameter.setter
    def simpleJava_parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_parameter__simpleJava_parameter", None)
        self.__simpleJava_parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_type56"):
                opp_val = getattr(old_value, "simpleJava_type56", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_type56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_type56"):
                opp_val = getattr(value, "simpleJava_type56", None)
                setattr(value, "simpleJava_type56", self)

    @property
    def simpleJava_parameter59(self):
        return self.__simpleJava_parameter59

    @simpleJava_parameter59.setter
    def simpleJava_parameter59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_parameter__simpleJava_parameter59", None)
        self.__simpleJava_parameter59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_parameter_list58"):
                opp_val = getattr(old_value, "simpleJava_parameter_list58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_parameter_list58"):
                opp_val = getattr(value, "simpleJava_parameter_list58", None)
                if opp_val is None:
                    setattr(value, "simpleJava_parameter_list58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleJava_statement_block:

    pass
class simpleJava_while_statement:

    pass
class simpleJava_do_statement:

    pass
class simpleJava_if_statement:

    pass
class simpleJava_static_initializer:

    pass
class simpleJava_variable_declaration:

    pass
class simpleJava_constructor_declaration(newBlock):

    def __init__(self, nomeContrutor: str, simpleJava_constructor_declaration: "simpleJava_field_declaration" = None, simpleJava_constructor_declaration171: "simpleJava_MODIFIER" = None, simpleJava_constructor_declaration174: "simpleJava_parameter_list" = None, simpleJava_constructor_declaration177: "simpleJava_statement_block" = None):
        self.nomeContrutor = nomeContrutor
        self.simpleJava_constructor_declaration = simpleJava_constructor_declaration
        self.simpleJava_constructor_declaration171 = simpleJava_constructor_declaration171
        self.simpleJava_constructor_declaration174 = simpleJava_constructor_declaration174
        self.simpleJava_constructor_declaration177 = simpleJava_constructor_declaration177
        
    @property
    def nomeContrutor(self) -> str:
        return self.__nomeContrutor

    @nomeContrutor.setter
    def nomeContrutor(self, nomeContrutor: str):
        self.__nomeContrutor = nomeContrutor

    @property
    def simpleJava_constructor_declaration177(self):
        return self.__simpleJava_constructor_declaration177

    @simpleJava_constructor_declaration177.setter
    def simpleJava_constructor_declaration177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_constructor_declaration__simpleJava_constructor_declaration177", None)
        self.__simpleJava_constructor_declaration177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_statement_block178"):
                opp_val = getattr(old_value, "simpleJava_statement_block178", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_statement_block178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_statement_block178"):
                opp_val = getattr(value, "simpleJava_statement_block178", None)
                setattr(value, "simpleJava_statement_block178", self)

    @property
    def simpleJava_constructor_declaration171(self):
        return self.__simpleJava_constructor_declaration171

    @simpleJava_constructor_declaration171.setter
    def simpleJava_constructor_declaration171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_constructor_declaration__simpleJava_constructor_declaration171", None)
        self.__simpleJava_constructor_declaration171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_MODIFIER172"):
                opp_val = getattr(old_value, "simpleJava_MODIFIER172", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_MODIFIER172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_MODIFIER172"):
                opp_val = getattr(value, "simpleJava_MODIFIER172", None)
                setattr(value, "simpleJava_MODIFIER172", self)

    @property
    def simpleJava_constructor_declaration174(self):
        return self.__simpleJava_constructor_declaration174

    @simpleJava_constructor_declaration174.setter
    def simpleJava_constructor_declaration174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_constructor_declaration__simpleJava_constructor_declaration174", None)
        self.__simpleJava_constructor_declaration174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_parameter_list175"):
                opp_val = getattr(old_value, "simpleJava_parameter_list175", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_parameter_list175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_parameter_list175"):
                opp_val = getattr(value, "simpleJava_parameter_list175", None)
                setattr(value, "simpleJava_parameter_list175", self)

    @property
    def simpleJava_constructor_declaration(self):
        return self.__simpleJava_constructor_declaration

    @simpleJava_constructor_declaration.setter
    def simpleJava_constructor_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_constructor_declaration__simpleJava_constructor_declaration", None)
        self.__simpleJava_constructor_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_field_declaration41"):
                opp_val = getattr(old_value, "simpleJava_field_declaration41", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_field_declaration41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_field_declaration41"):
                opp_val = getattr(value, "simpleJava_field_declaration41", None)
                setattr(value, "simpleJava_field_declaration41", self)

class simpleJava_method_declaration:

    def __init__(self, nomeMetodo: str, simpleJava_method_declaration47: "simpleJava_MODIFIER" = None, simpleJava_method_declaration50: "simpleJava_type" = None, simpleJava_method_declaration: "simpleJava_field_declaration" = None, simpleJava_method_declaration52: "simpleJava_parameter_list" = None, simpleJava_method_declaration54: "simpleJava_statement_block" = None):
        self.nomeMetodo = nomeMetodo
        self.simpleJava_method_declaration47 = simpleJava_method_declaration47
        self.simpleJava_method_declaration50 = simpleJava_method_declaration50
        self.simpleJava_method_declaration = simpleJava_method_declaration
        self.simpleJava_method_declaration52 = simpleJava_method_declaration52
        self.simpleJava_method_declaration54 = simpleJava_method_declaration54
        
    @property
    def nomeMetodo(self) -> str:
        return self.__nomeMetodo

    @nomeMetodo.setter
    def nomeMetodo(self, nomeMetodo: str):
        self.__nomeMetodo = nomeMetodo

    @property
    def simpleJava_method_declaration52(self):
        return self.__simpleJava_method_declaration52

    @simpleJava_method_declaration52.setter
    def simpleJava_method_declaration52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_method_declaration__simpleJava_method_declaration52", None)
        self.__simpleJava_method_declaration52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_parameter_list"):
                opp_val = getattr(old_value, "simpleJava_parameter_list", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_parameter_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_parameter_list"):
                opp_val = getattr(value, "simpleJava_parameter_list", None)
                setattr(value, "simpleJava_parameter_list", self)

    @property
    def simpleJava_method_declaration54(self):
        return self.__simpleJava_method_declaration54

    @simpleJava_method_declaration54.setter
    def simpleJava_method_declaration54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_method_declaration__simpleJava_method_declaration54", None)
        self.__simpleJava_method_declaration54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_statement_block"):
                opp_val = getattr(old_value, "simpleJava_statement_block", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_statement_block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_statement_block"):
                opp_val = getattr(value, "simpleJava_statement_block", None)
                setattr(value, "simpleJava_statement_block", self)

    @property
    def simpleJava_method_declaration47(self):
        return self.__simpleJava_method_declaration47

    @simpleJava_method_declaration47.setter
    def simpleJava_method_declaration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_method_declaration__simpleJava_method_declaration47", None)
        self.__simpleJava_method_declaration47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_MODIFIER48"):
                opp_val = getattr(old_value, "simpleJava_MODIFIER48", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_MODIFIER48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_MODIFIER48"):
                opp_val = getattr(value, "simpleJava_MODIFIER48", None)
                setattr(value, "simpleJava_MODIFIER48", self)

    @property
    def simpleJava_method_declaration50(self):
        return self.__simpleJava_method_declaration50

    @simpleJava_method_declaration50.setter
    def simpleJava_method_declaration50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_method_declaration__simpleJava_method_declaration50", None)
        self.__simpleJava_method_declaration50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_type"):
                opp_val = getattr(old_value, "simpleJava_type", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_type"):
                opp_val = getattr(value, "simpleJava_type", None)
                setattr(value, "simpleJava_type", self)

    @property
    def simpleJava_method_declaration(self):
        return self.__simpleJava_method_declaration

    @simpleJava_method_declaration.setter
    def simpleJava_method_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_method_declaration__simpleJava_method_declaration", None)
        self.__simpleJava_method_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_field_declaration39"):
                opp_val = getattr(old_value, "simpleJava_field_declaration39", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_field_declaration39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_field_declaration39"):
                opp_val = getattr(value, "simpleJava_field_declaration39", None)
                setattr(value, "simpleJava_field_declaration39", self)

class simpleJava_parameter_list:

    pass
class simpleJava_type(exp_aux):

    pass
class simpleJava_field_declaration:

    pass
class simpleJava_MODIFIER:

    def __init__(self, modificador: str, simpleJava_MODIFIER29: "simpleJava_interface_declaration" = None, simpleJava_MODIFIER: "simpleJava_class_declaration" = None, simpleJava_MODIFIER48: "simpleJava_method_declaration" = None, simpleJava_MODIFIER96: "simpleJava_variable_declaration" = None, simpleJava_MODIFIER172: "simpleJava_constructor_declaration" = None):
        self.modificador = modificador
        self.simpleJava_MODIFIER29 = simpleJava_MODIFIER29
        self.simpleJava_MODIFIER = simpleJava_MODIFIER
        self.simpleJava_MODIFIER48 = simpleJava_MODIFIER48
        self.simpleJava_MODIFIER96 = simpleJava_MODIFIER96
        self.simpleJava_MODIFIER172 = simpleJava_MODIFIER172
        
    @property
    def modificador(self) -> str:
        return self.__modificador

    @modificador.setter
    def modificador(self, modificador: str):
        self.__modificador = modificador

    @property
    def simpleJava_MODIFIER29(self):
        return self.__simpleJava_MODIFIER29

    @simpleJava_MODIFIER29.setter
    def simpleJava_MODIFIER29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_MODIFIER__simpleJava_MODIFIER29", None)
        self.__simpleJava_MODIFIER29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_interface_declaration28"):
                opp_val = getattr(old_value, "simpleJava_interface_declaration28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_interface_declaration28"):
                opp_val = getattr(value, "simpleJava_interface_declaration28", None)
                if opp_val is None:
                    setattr(value, "simpleJava_interface_declaration28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleJava_MODIFIER48(self):
        return self.__simpleJava_MODIFIER48

    @simpleJava_MODIFIER48.setter
    def simpleJava_MODIFIER48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_MODIFIER__simpleJava_MODIFIER48", None)
        self.__simpleJava_MODIFIER48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_method_declaration47"):
                opp_val = getattr(old_value, "simpleJava_method_declaration47", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_method_declaration47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_method_declaration47"):
                opp_val = getattr(value, "simpleJava_method_declaration47", None)
                setattr(value, "simpleJava_method_declaration47", self)

    @property
    def simpleJava_MODIFIER172(self):
        return self.__simpleJava_MODIFIER172

    @simpleJava_MODIFIER172.setter
    def simpleJava_MODIFIER172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_MODIFIER__simpleJava_MODIFIER172", None)
        self.__simpleJava_MODIFIER172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_constructor_declaration171"):
                opp_val = getattr(old_value, "simpleJava_constructor_declaration171", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_constructor_declaration171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_constructor_declaration171"):
                opp_val = getattr(value, "simpleJava_constructor_declaration171", None)
                setattr(value, "simpleJava_constructor_declaration171", self)

    @property
    def simpleJava_MODIFIER96(self):
        return self.__simpleJava_MODIFIER96

    @simpleJava_MODIFIER96.setter
    def simpleJava_MODIFIER96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_MODIFIER__simpleJava_MODIFIER96", None)
        self.__simpleJava_MODIFIER96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_variable_declaration95"):
                opp_val = getattr(old_value, "simpleJava_variable_declaration95", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_variable_declaration95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_variable_declaration95"):
                opp_val = getattr(value, "simpleJava_variable_declaration95", None)
                setattr(value, "simpleJava_variable_declaration95", self)

    @property
    def simpleJava_MODIFIER(self):
        return self.__simpleJava_MODIFIER

    @simpleJava_MODIFIER.setter
    def simpleJava_MODIFIER(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_MODIFIER__simpleJava_MODIFIER", None)
        self.__simpleJava_MODIFIER = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_class_declaration15"):
                opp_val = getattr(old_value, "simpleJava_class_declaration15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_class_declaration15"):
                opp_val = getattr(value, "simpleJava_class_declaration15", None)
                if opp_val is None:
                    setattr(value, "simpleJava_class_declaration15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class type_declaration:

    pass
class simpleJava_doc_comment(type_declaration):

    def __init__(self, comentario: str, simpleJava_doc_comment: "simpleJava_field_declaration" = None):
        self.comentario = comentario
        self.simpleJava_doc_comment = simpleJava_doc_comment
        
    @property
    def comentario(self) -> str:
        return self.__comentario

    @comentario.setter
    def comentario(self, comentario: str):
        self.__comentario = comentario

    @property
    def simpleJava_doc_comment(self):
        return self.__simpleJava_doc_comment

    @simpleJava_doc_comment.setter
    def simpleJava_doc_comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_doc_comment__simpleJava_doc_comment", None)
        self.__simpleJava_doc_comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_field_declaration37"):
                opp_val = getattr(old_value, "simpleJava_field_declaration37", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_field_declaration37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_field_declaration37"):
                opp_val = getattr(value, "simpleJava_field_declaration37", None)
                setattr(value, "simpleJava_field_declaration37", self)

class simpleJava_interface_declaration:

    def __init__(self, nomeInterface: str, simpleJava_interface_declaration28: set["simpleJava_MODIFIER"] = None, simpleJava_interface_declaration: "simpleJava_type_declaration" = None, simpleJava_interface_declaration31: set["simpleJava_name"] = None, simpleJava_interface_declaration34: set["simpleJava_field_declaration"] = None):
        self.nomeInterface = nomeInterface
        self.simpleJava_interface_declaration28 = simpleJava_interface_declaration28 if simpleJava_interface_declaration28 is not None else set()
        self.simpleJava_interface_declaration = simpleJava_interface_declaration
        self.simpleJava_interface_declaration31 = simpleJava_interface_declaration31 if simpleJava_interface_declaration31 is not None else set()
        self.simpleJava_interface_declaration34 = simpleJava_interface_declaration34 if simpleJava_interface_declaration34 is not None else set()
        
    @property
    def nomeInterface(self) -> str:
        return self.__nomeInterface

    @nomeInterface.setter
    def nomeInterface(self, nomeInterface: str):
        self.__nomeInterface = nomeInterface

    @property
    def simpleJava_interface_declaration28(self):
        return self.__simpleJava_interface_declaration28

    @simpleJava_interface_declaration28.setter
    def simpleJava_interface_declaration28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_interface_declaration__simpleJava_interface_declaration28", None)
        self.__simpleJava_interface_declaration28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleJava_MODIFIER29"):
                    opp_val = getattr(item, "simpleJava_MODIFIER29", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleJava_MODIFIER29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleJava_MODIFIER29"):
                    opp_val = getattr(item, "simpleJava_MODIFIER29", None)
                    
                    setattr(item, "simpleJava_MODIFIER29", self)
                    

    @property
    def simpleJava_interface_declaration31(self):
        return self.__simpleJava_interface_declaration31

    @simpleJava_interface_declaration31.setter
    def simpleJava_interface_declaration31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_interface_declaration__simpleJava_interface_declaration31", None)
        self.__simpleJava_interface_declaration31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleJava_name32"):
                    opp_val = getattr(item, "simpleJava_name32", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleJava_name32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleJava_name32"):
                    opp_val = getattr(item, "simpleJava_name32", None)
                    
                    setattr(item, "simpleJava_name32", self)
                    

    @property
    def simpleJava_interface_declaration(self):
        return self.__simpleJava_interface_declaration

    @simpleJava_interface_declaration.setter
    def simpleJava_interface_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_interface_declaration__simpleJava_interface_declaration", None)
        self.__simpleJava_interface_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_type_declaration13"):
                opp_val = getattr(old_value, "simpleJava_type_declaration13", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_type_declaration13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_type_declaration13"):
                opp_val = getattr(value, "simpleJava_type_declaration13", None)
                setattr(value, "simpleJava_type_declaration13", self)

    @property
    def simpleJava_interface_declaration34(self):
        return self.__simpleJava_interface_declaration34

    @simpleJava_interface_declaration34.setter
    def simpleJava_interface_declaration34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_interface_declaration__simpleJava_interface_declaration34", None)
        self.__simpleJava_interface_declaration34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleJava_field_declaration35"):
                    opp_val = getattr(item, "simpleJava_field_declaration35", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleJava_field_declaration35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleJava_field_declaration35"):
                    opp_val = getattr(item, "simpleJava_field_declaration35", None)
                    
                    setattr(item, "simpleJava_field_declaration35", self)
                    

class simpleJava_class_declaration:

    def __init__(self, nomeClasse: str, simpleJava_class_declaration23: set["simpleJava_field_declaration"] = None, simpleJava_class_declaration26: "simpleJava_class_declaration" = None, simpleJava_class_declaration24: set["simpleJava_class_declaration"] = None, simpleJava_class_declaration: "simpleJava_type_declaration" = None, simpleJava_class_declaration15: set["simpleJava_MODIFIER"] = None, simpleJava_class_declaration17: "simpleJava_name" = None, simpleJava_class_declaration20: set["simpleJava_name"] = None):
        self.nomeClasse = nomeClasse
        self.simpleJava_class_declaration23 = simpleJava_class_declaration23 if simpleJava_class_declaration23 is not None else set()
        self.simpleJava_class_declaration26 = simpleJava_class_declaration26
        self.simpleJava_class_declaration24 = simpleJava_class_declaration24 if simpleJava_class_declaration24 is not None else set()
        self.simpleJava_class_declaration = simpleJava_class_declaration
        self.simpleJava_class_declaration15 = simpleJava_class_declaration15 if simpleJava_class_declaration15 is not None else set()
        self.simpleJava_class_declaration17 = simpleJava_class_declaration17
        self.simpleJava_class_declaration20 = simpleJava_class_declaration20 if simpleJava_class_declaration20 is not None else set()
        
    @property
    def nomeClasse(self) -> str:
        return self.__nomeClasse

    @nomeClasse.setter
    def nomeClasse(self, nomeClasse: str):
        self.__nomeClasse = nomeClasse

    @property
    def simpleJava_class_declaration(self):
        return self.__simpleJava_class_declaration

    @simpleJava_class_declaration.setter
    def simpleJava_class_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_class_declaration__simpleJava_class_declaration", None)
        self.__simpleJava_class_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_type_declaration11"):
                opp_val = getattr(old_value, "simpleJava_type_declaration11", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_type_declaration11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_type_declaration11"):
                opp_val = getattr(value, "simpleJava_type_declaration11", None)
                setattr(value, "simpleJava_type_declaration11", self)

    @property
    def simpleJava_class_declaration23(self):
        return self.__simpleJava_class_declaration23

    @simpleJava_class_declaration23.setter
    def simpleJava_class_declaration23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_class_declaration__simpleJava_class_declaration23", None)
        self.__simpleJava_class_declaration23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleJava_field_declaration"):
                    opp_val = getattr(item, "simpleJava_field_declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleJava_field_declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleJava_field_declaration"):
                    opp_val = getattr(item, "simpleJava_field_declaration", None)
                    
                    setattr(item, "simpleJava_field_declaration", self)
                    

    @property
    def simpleJava_class_declaration20(self):
        return self.__simpleJava_class_declaration20

    @simpleJava_class_declaration20.setter
    def simpleJava_class_declaration20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_class_declaration__simpleJava_class_declaration20", None)
        self.__simpleJava_class_declaration20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleJava_name21"):
                    opp_val = getattr(item, "simpleJava_name21", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleJava_name21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleJava_name21"):
                    opp_val = getattr(item, "simpleJava_name21", None)
                    
                    setattr(item, "simpleJava_name21", self)
                    

    @property
    def simpleJava_class_declaration26(self):
        return self.__simpleJava_class_declaration26

    @simpleJava_class_declaration26.setter
    def simpleJava_class_declaration26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_class_declaration__simpleJava_class_declaration26", None)
        self.__simpleJava_class_declaration26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_class_declaration24"):
                opp_val = getattr(old_value, "simpleJava_class_declaration24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_class_declaration24"):
                opp_val = getattr(value, "simpleJava_class_declaration24", None)
                if opp_val is None:
                    setattr(value, "simpleJava_class_declaration24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleJava_class_declaration15(self):
        return self.__simpleJava_class_declaration15

    @simpleJava_class_declaration15.setter
    def simpleJava_class_declaration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_class_declaration__simpleJava_class_declaration15", None)
        self.__simpleJava_class_declaration15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleJava_MODIFIER"):
                    opp_val = getattr(item, "simpleJava_MODIFIER", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleJava_MODIFIER", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleJava_MODIFIER"):
                    opp_val = getattr(item, "simpleJava_MODIFIER", None)
                    
                    setattr(item, "simpleJava_MODIFIER", self)
                    

    @property
    def simpleJava_class_declaration17(self):
        return self.__simpleJava_class_declaration17

    @simpleJava_class_declaration17.setter
    def simpleJava_class_declaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_class_declaration__simpleJava_class_declaration17", None)
        self.__simpleJava_class_declaration17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_name18"):
                opp_val = getattr(old_value, "simpleJava_name18", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_name18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_name18"):
                opp_val = getattr(value, "simpleJava_name18", None)
                setattr(value, "simpleJava_name18", self)

    @property
    def simpleJava_class_declaration24(self):
        return self.__simpleJava_class_declaration24

    @simpleJava_class_declaration24.setter
    def simpleJava_class_declaration24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_class_declaration__simpleJava_class_declaration24", None)
        self.__simpleJava_class_declaration24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleJava_class_declaration26"):
                    opp_val = getattr(item, "simpleJava_class_declaration26", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleJava_class_declaration26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleJava_class_declaration26"):
                    opp_val = getattr(item, "simpleJava_class_declaration26", None)
                    
                    setattr(item, "simpleJava_class_declaration26", self)
                    

class simpleJava_import_statement:

    pass
class simpleJava_package_statement:

    pass
class Model:

    pass
class simpleJava_compilation_unit(Model):

    pass
class simpleJava_Model:

    pass
class simpleJava_name(expression_aux):

    def __init__(self, nome: str, simpleJava_name: "simpleJava_package_statement" = None, simpleJava_name9: "simpleJava_import_statement" = None, simpleJava_name18: "simpleJava_class_declaration" = None, simpleJava_name21: "simpleJava_class_declaration" = None, simpleJava_name32: "simpleJava_interface_declaration" = None, simpleJava_name183: "simpleJava_creating_expression" = None, simpleJava_name236: "simpleJava_package_name_aux" = None, simpleJava_name245: "simpleJava_type" = None):
        self.nome = nome
        self.simpleJava_name = simpleJava_name
        self.simpleJava_name9 = simpleJava_name9
        self.simpleJava_name18 = simpleJava_name18
        self.simpleJava_name21 = simpleJava_name21
        self.simpleJava_name32 = simpleJava_name32
        self.simpleJava_name183 = simpleJava_name183
        self.simpleJava_name236 = simpleJava_name236
        self.simpleJava_name245 = simpleJava_name245
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def simpleJava_name18(self):
        return self.__simpleJava_name18

    @simpleJava_name18.setter
    def simpleJava_name18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_name__simpleJava_name18", None)
        self.__simpleJava_name18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_class_declaration17"):
                opp_val = getattr(old_value, "simpleJava_class_declaration17", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_class_declaration17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_class_declaration17"):
                opp_val = getattr(value, "simpleJava_class_declaration17", None)
                setattr(value, "simpleJava_class_declaration17", self)

    @property
    def simpleJava_name236(self):
        return self.__simpleJava_name236

    @simpleJava_name236.setter
    def simpleJava_name236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_name__simpleJava_name236", None)
        self.__simpleJava_name236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_package_name_aux"):
                opp_val = getattr(old_value, "simpleJava_package_name_aux", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_package_name_aux", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_package_name_aux"):
                opp_val = getattr(value, "simpleJava_package_name_aux", None)
                setattr(value, "simpleJava_package_name_aux", self)

    @property
    def simpleJava_name21(self):
        return self.__simpleJava_name21

    @simpleJava_name21.setter
    def simpleJava_name21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_name__simpleJava_name21", None)
        self.__simpleJava_name21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_class_declaration20"):
                opp_val = getattr(old_value, "simpleJava_class_declaration20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_class_declaration20"):
                opp_val = getattr(value, "simpleJava_class_declaration20", None)
                if opp_val is None:
                    setattr(value, "simpleJava_class_declaration20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleJava_name(self):
        return self.__simpleJava_name

    @simpleJava_name.setter
    def simpleJava_name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_name__simpleJava_name", None)
        self.__simpleJava_name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_package_statement6"):
                opp_val = getattr(old_value, "simpleJava_package_statement6", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_package_statement6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_package_statement6"):
                opp_val = getattr(value, "simpleJava_package_statement6", None)
                setattr(value, "simpleJava_package_statement6", self)

    @property
    def simpleJava_name183(self):
        return self.__simpleJava_name183

    @simpleJava_name183.setter
    def simpleJava_name183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_name__simpleJava_name183", None)
        self.__simpleJava_name183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_creating_expression"):
                opp_val = getattr(old_value, "simpleJava_creating_expression", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_creating_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_creating_expression"):
                opp_val = getattr(value, "simpleJava_creating_expression", None)
                setattr(value, "simpleJava_creating_expression", self)

    @property
    def simpleJava_name9(self):
        return self.__simpleJava_name9

    @simpleJava_name9.setter
    def simpleJava_name9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_name__simpleJava_name9", None)
        self.__simpleJava_name9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_import_statement8"):
                opp_val = getattr(old_value, "simpleJava_import_statement8", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_import_statement8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_import_statement8"):
                opp_val = getattr(value, "simpleJava_import_statement8", None)
                setattr(value, "simpleJava_import_statement8", self)

    @property
    def simpleJava_name245(self):
        return self.__simpleJava_name245

    @simpleJava_name245.setter
    def simpleJava_name245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_name__simpleJava_name245", None)
        self.__simpleJava_name245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_type244"):
                opp_val = getattr(old_value, "simpleJava_type244", None)
                if opp_val == self:
                    setattr(old_value, "simpleJava_type244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_type244"):
                opp_val = getattr(value, "simpleJava_type244", None)
                setattr(value, "simpleJava_type244", self)

    @property
    def simpleJava_name32(self):
        return self.__simpleJava_name32

    @simpleJava_name32.setter
    def simpleJava_name32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleJava_name__simpleJava_name32", None)
        self.__simpleJava_name32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleJava_interface_declaration31"):
                opp_val = getattr(old_value, "simpleJava_interface_declaration31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleJava_interface_declaration31"):
                opp_val = getattr(value, "simpleJava_interface_declaration31", None)
                if opp_val is None:
                    setattr(value, "simpleJava_interface_declaration31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleJava_type_declaration:

    pass