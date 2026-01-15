from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class go_PARAMETER:

    def __init__(self, id: str, go_PARAMETER156: "go_Types" = None, go_PARAMETER: "go_PARAMETERS_LIST" = None, go_PARAMETER153: "go_LITERAIS_BASICOS" = None):
        self.id = id
        self.go_PARAMETER156 = go_PARAMETER156
        self.go_PARAMETER = go_PARAMETER
        self.go_PARAMETER153 = go_PARAMETER153
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def go_PARAMETER153(self):
        return self.__go_PARAMETER153

    @go_PARAMETER153.setter
    def go_PARAMETER153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_PARAMETER__go_PARAMETER153", None)
        self.__go_PARAMETER153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_LITERAIS_BASICOS154"):
                opp_val = getattr(old_value, "go_LITERAIS_BASICOS154", None)
                if opp_val == self:
                    setattr(old_value, "go_LITERAIS_BASICOS154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_LITERAIS_BASICOS154"):
                opp_val = getattr(value, "go_LITERAIS_BASICOS154", None)
                setattr(value, "go_LITERAIS_BASICOS154", self)

    @property
    def go_PARAMETER(self):
        return self.__go_PARAMETER

    @go_PARAMETER.setter
    def go_PARAMETER(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_PARAMETER__go_PARAMETER", None)
        self.__go_PARAMETER = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_PARAMETERS_LIST151"):
                opp_val = getattr(old_value, "go_PARAMETERS_LIST151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_PARAMETERS_LIST151"):
                opp_val = getattr(value, "go_PARAMETERS_LIST151", None)
                if opp_val is None:
                    setattr(value, "go_PARAMETERS_LIST151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def go_PARAMETER156(self):
        return self.__go_PARAMETER156

    @go_PARAMETER156.setter
    def go_PARAMETER156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_PARAMETER__go_PARAMETER156", None)
        self.__go_PARAMETER156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Types157"):
                opp_val = getattr(old_value, "go_Types157", None)
                if opp_val == self:
                    setattr(old_value, "go_Types157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Types157"):
                opp_val = getattr(value, "go_Types157", None)
                setattr(value, "go_Types157", self)

class go_BasicType:

    def __init__(self, string: str, int: str, float: str, boolean: str, go_BasicType: "go_Types" = None, go_BasicType165: "go_ArrayType" = None):
        self.string = string
        self.int = int
        self.float = float
        self.boolean = boolean
        self.go_BasicType = go_BasicType
        self.go_BasicType165 = go_BasicType165
        
    @property
    def float(self) -> str:
        return self.__float

    @float.setter
    def float(self, float: str):
        self.__float = float

    @property
    def boolean(self) -> str:
        return self.__boolean

    @boolean.setter
    def boolean(self, boolean: str):
        self.__boolean = boolean

    @property
    def int(self) -> str:
        return self.__int

    @int.setter
    def int(self, int: str):
        self.__int = int

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def go_BasicType165(self):
        return self.__go_BasicType165

    @go_BasicType165.setter
    def go_BasicType165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BasicType__go_BasicType165", None)
        self.__go_BasicType165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ArrayType164"):
                opp_val = getattr(old_value, "go_ArrayType164", None)
                if opp_val == self:
                    setattr(old_value, "go_ArrayType164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ArrayType164"):
                opp_val = getattr(value, "go_ArrayType164", None)
                setattr(value, "go_ArrayType164", self)

    @property
    def go_BasicType(self):
        return self.__go_BasicType

    @go_BasicType.setter
    def go_BasicType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BasicType__go_BasicType", None)
        self.__go_BasicType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Types159"):
                opp_val = getattr(old_value, "go_Types159", None)
                if opp_val == self:
                    setattr(old_value, "go_Types159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Types159"):
                opp_val = getattr(value, "go_Types159", None)
                setattr(value, "go_Types159", self)

class go_PARAMETERS_LIST:

    def __init__(self, vir: str, go_PARAMETERS_LIST: "go_Parameters" = None, go_PARAMETERS_LIST151: set["go_PARAMETER"] = None, go_PARAMETERS_LIST168: "go_FunctionCall" = None):
        self.vir = vir
        self.go_PARAMETERS_LIST = go_PARAMETERS_LIST
        self.go_PARAMETERS_LIST151 = go_PARAMETERS_LIST151 if go_PARAMETERS_LIST151 is not None else set()
        self.go_PARAMETERS_LIST168 = go_PARAMETERS_LIST168
        
    @property
    def vir(self) -> str:
        return self.__vir

    @vir.setter
    def vir(self, vir: str):
        self.__vir = vir

    @property
    def go_PARAMETERS_LIST151(self):
        return self.__go_PARAMETERS_LIST151

    @go_PARAMETERS_LIST151.setter
    def go_PARAMETERS_LIST151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_PARAMETERS_LIST__go_PARAMETERS_LIST151", None)
        self.__go_PARAMETERS_LIST151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "go_PARAMETER"):
                    opp_val = getattr(item, "go_PARAMETER", None)
                    
                    if opp_val == self:
                        setattr(item, "go_PARAMETER", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "go_PARAMETER"):
                    opp_val = getattr(item, "go_PARAMETER", None)
                    
                    setattr(item, "go_PARAMETER", self)
                    

    @property
    def go_PARAMETERS_LIST(self):
        return self.__go_PARAMETERS_LIST

    @go_PARAMETERS_LIST.setter
    def go_PARAMETERS_LIST(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_PARAMETERS_LIST__go_PARAMETERS_LIST", None)
        self.__go_PARAMETERS_LIST = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Parameters136"):
                opp_val = getattr(old_value, "go_Parameters136", None)
                if opp_val == self:
                    setattr(old_value, "go_Parameters136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Parameters136"):
                opp_val = getattr(value, "go_Parameters136", None)
                setattr(value, "go_Parameters136", self)

    @property
    def go_PARAMETERS_LIST168(self):
        return self.__go_PARAMETERS_LIST168

    @go_PARAMETERS_LIST168.setter
    def go_PARAMETERS_LIST168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_PARAMETERS_LIST__go_PARAMETERS_LIST168", None)
        self.__go_PARAMETERS_LIST168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_FunctionCall167"):
                opp_val = getattr(old_value, "go_FunctionCall167", None)
                if opp_val == self:
                    setattr(old_value, "go_FunctionCall167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_FunctionCall167"):
                opp_val = getattr(value, "go_FunctionCall167", None)
                setattr(value, "go_FunctionCall167", self)

class go_Parameters:

    pass
class go_ElseCondition:

    pass
class go_ElseIfCondition:

    pass
class ElseIfCondition:

    pass
class go_IfCondition(ElseIfCondition):

    pass
class go_BLOCK:

    pass
class go_Signature:

    pass
class go_BOOL_OP:

    pass
class go_Chamada:

    pass
class go_ArrayValue:

    pass
class go_EObject:

    pass
class go_LiteraisList:

    def __init__(self, vir: str, go_LiteraisList: "go_ArrayValue" = None, go_LiteraisList112: set["go_EObject"] = None):
        self.vir = vir
        self.go_LiteraisList = go_LiteraisList
        self.go_LiteraisList112 = go_LiteraisList112 if go_LiteraisList112 is not None else set()
        
    @property
    def vir(self) -> str:
        return self.__vir

    @vir.setter
    def vir(self, vir: str):
        self.__vir = vir

    @property
    def go_LiteraisList(self):
        return self.__go_LiteraisList

    @go_LiteraisList.setter
    def go_LiteraisList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_LiteraisList__go_LiteraisList", None)
        self.__go_LiteraisList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ArrayValue110"):
                opp_val = getattr(old_value, "go_ArrayValue110", None)
                if opp_val == self:
                    setattr(old_value, "go_ArrayValue110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ArrayValue110"):
                opp_val = getattr(value, "go_ArrayValue110", None)
                setattr(value, "go_ArrayValue110", self)

    @property
    def go_LiteraisList112(self):
        return self.__go_LiteraisList112

    @go_LiteraisList112.setter
    def go_LiteraisList112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_LiteraisList__go_LiteraisList112", None)
        self.__go_LiteraisList112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "go_EObject"):
                    opp_val = getattr(item, "go_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "go_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "go_EObject"):
                    opp_val = getattr(item, "go_EObject", None)
                    
                    setattr(item, "go_EObject", self)
                    

class go_ReturnStmt:

    pass
class go_IfStmt:

    pass
class go_LITERAIS_BASICOS:

    def __init__(self, numero: str, string: str, go_LITERAIS_BASICOS: "go_EXPRESSAO" = None, go_LITERAIS_BASICOS102: "go_ReturnStmt" = None, go_LITERAIS_BASICOS117: "go_BINARY_EXP" = None, go_LITERAIS_BASICOS114: "go_BOOLEAN_VALUE" = None, go_LITERAIS_BASICOS154: "go_PARAMETER" = None):
        self.numero = numero
        self.string = string
        self.go_LITERAIS_BASICOS = go_LITERAIS_BASICOS
        self.go_LITERAIS_BASICOS102 = go_LITERAIS_BASICOS102
        self.go_LITERAIS_BASICOS117 = go_LITERAIS_BASICOS117
        self.go_LITERAIS_BASICOS114 = go_LITERAIS_BASICOS114
        self.go_LITERAIS_BASICOS154 = go_LITERAIS_BASICOS154
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def numero(self) -> str:
        return self.__numero

    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero

    @property
    def go_LITERAIS_BASICOS(self):
        return self.__go_LITERAIS_BASICOS

    @go_LITERAIS_BASICOS.setter
    def go_LITERAIS_BASICOS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_LITERAIS_BASICOS__go_LITERAIS_BASICOS", None)
        self.__go_LITERAIS_BASICOS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_EXPRESSAO85"):
                opp_val = getattr(old_value, "go_EXPRESSAO85", None)
                if opp_val == self:
                    setattr(old_value, "go_EXPRESSAO85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_EXPRESSAO85"):
                opp_val = getattr(value, "go_EXPRESSAO85", None)
                setattr(value, "go_EXPRESSAO85", self)

    @property
    def go_LITERAIS_BASICOS117(self):
        return self.__go_LITERAIS_BASICOS117

    @go_LITERAIS_BASICOS117.setter
    def go_LITERAIS_BASICOS117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_LITERAIS_BASICOS__go_LITERAIS_BASICOS117", None)
        self.__go_LITERAIS_BASICOS117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_BINARY_EXP116"):
                opp_val = getattr(old_value, "go_BINARY_EXP116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_BINARY_EXP116"):
                opp_val = getattr(value, "go_BINARY_EXP116", None)
                if opp_val is None:
                    setattr(value, "go_BINARY_EXP116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def go_LITERAIS_BASICOS154(self):
        return self.__go_LITERAIS_BASICOS154

    @go_LITERAIS_BASICOS154.setter
    def go_LITERAIS_BASICOS154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_LITERAIS_BASICOS__go_LITERAIS_BASICOS154", None)
        self.__go_LITERAIS_BASICOS154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_PARAMETER153"):
                opp_val = getattr(old_value, "go_PARAMETER153", None)
                if opp_val == self:
                    setattr(old_value, "go_PARAMETER153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_PARAMETER153"):
                opp_val = getattr(value, "go_PARAMETER153", None)
                setattr(value, "go_PARAMETER153", self)

    @property
    def go_LITERAIS_BASICOS102(self):
        return self.__go_LITERAIS_BASICOS102

    @go_LITERAIS_BASICOS102.setter
    def go_LITERAIS_BASICOS102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_LITERAIS_BASICOS__go_LITERAIS_BASICOS102", None)
        self.__go_LITERAIS_BASICOS102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ReturnStmt"):
                opp_val = getattr(old_value, "go_ReturnStmt", None)
                if opp_val == self:
                    setattr(old_value, "go_ReturnStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ReturnStmt"):
                opp_val = getattr(value, "go_ReturnStmt", None)
                setattr(value, "go_ReturnStmt", self)

    @property
    def go_LITERAIS_BASICOS114(self):
        return self.__go_LITERAIS_BASICOS114

    @go_LITERAIS_BASICOS114.setter
    def go_LITERAIS_BASICOS114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_LITERAIS_BASICOS__go_LITERAIS_BASICOS114", None)
        self.__go_LITERAIS_BASICOS114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_BOOLEAN_VALUE"):
                opp_val = getattr(old_value, "go_BOOLEAN_VALUE", None)
                if opp_val == self:
                    setattr(old_value, "go_BOOLEAN_VALUE", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_BOOLEAN_VALUE"):
                opp_val = getattr(value, "go_BOOLEAN_VALUE", None)
                setattr(value, "go_BOOLEAN_VALUE", self)

class go_BINARY_EXP:

    def __init__(self, arit: str, go_BINARY_EXP: "go_EXPRESSAO" = None, go_BINARY_EXP116: set["go_LITERAIS_BASICOS"] = None, go_BINARY_EXP119: set["go_VarCall"] = None, go_BINARY_EXP122: set["go_FunctionCall"] = None, go_BINARY_EXP125: "go_BOOL_OP" = None):
        self.arit = arit
        self.go_BINARY_EXP = go_BINARY_EXP
        self.go_BINARY_EXP116 = go_BINARY_EXP116 if go_BINARY_EXP116 is not None else set()
        self.go_BINARY_EXP119 = go_BINARY_EXP119 if go_BINARY_EXP119 is not None else set()
        self.go_BINARY_EXP122 = go_BINARY_EXP122 if go_BINARY_EXP122 is not None else set()
        self.go_BINARY_EXP125 = go_BINARY_EXP125
        
    @property
    def arit(self) -> str:
        return self.__arit

    @arit.setter
    def arit(self, arit: str):
        self.__arit = arit

    @property
    def go_BINARY_EXP122(self):
        return self.__go_BINARY_EXP122

    @go_BINARY_EXP122.setter
    def go_BINARY_EXP122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BINARY_EXP__go_BINARY_EXP122", None)
        self.__go_BINARY_EXP122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "go_FunctionCall123"):
                    opp_val = getattr(item, "go_FunctionCall123", None)
                    
                    if opp_val == self:
                        setattr(item, "go_FunctionCall123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "go_FunctionCall123"):
                    opp_val = getattr(item, "go_FunctionCall123", None)
                    
                    setattr(item, "go_FunctionCall123", self)
                    

    @property
    def go_BINARY_EXP119(self):
        return self.__go_BINARY_EXP119

    @go_BINARY_EXP119.setter
    def go_BINARY_EXP119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BINARY_EXP__go_BINARY_EXP119", None)
        self.__go_BINARY_EXP119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "go_VarCall120"):
                    opp_val = getattr(item, "go_VarCall120", None)
                    
                    if opp_val == self:
                        setattr(item, "go_VarCall120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "go_VarCall120"):
                    opp_val = getattr(item, "go_VarCall120", None)
                    
                    setattr(item, "go_VarCall120", self)
                    

    @property
    def go_BINARY_EXP125(self):
        return self.__go_BINARY_EXP125

    @go_BINARY_EXP125.setter
    def go_BINARY_EXP125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BINARY_EXP__go_BINARY_EXP125", None)
        self.__go_BINARY_EXP125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_BOOL_OP"):
                opp_val = getattr(old_value, "go_BOOL_OP", None)
                if opp_val == self:
                    setattr(old_value, "go_BOOL_OP", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_BOOL_OP"):
                opp_val = getattr(value, "go_BOOL_OP", None)
                setattr(value, "go_BOOL_OP", self)

    @property
    def go_BINARY_EXP(self):
        return self.__go_BINARY_EXP

    @go_BINARY_EXP.setter
    def go_BINARY_EXP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BINARY_EXP__go_BINARY_EXP", None)
        self.__go_BINARY_EXP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_EXPRESSAO83"):
                opp_val = getattr(old_value, "go_EXPRESSAO83", None)
                if opp_val == self:
                    setattr(old_value, "go_EXPRESSAO83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_EXPRESSAO83"):
                opp_val = getattr(value, "go_EXPRESSAO83", None)
                setattr(value, "go_EXPRESSAO83", self)

    @property
    def go_BINARY_EXP116(self):
        return self.__go_BINARY_EXP116

    @go_BINARY_EXP116.setter
    def go_BINARY_EXP116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BINARY_EXP__go_BINARY_EXP116", None)
        self.__go_BINARY_EXP116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "go_LITERAIS_BASICOS117"):
                    opp_val = getattr(item, "go_LITERAIS_BASICOS117", None)
                    
                    if opp_val == self:
                        setattr(item, "go_LITERAIS_BASICOS117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "go_LITERAIS_BASICOS117"):
                    opp_val = getattr(item, "go_LITERAIS_BASICOS117", None)
                    
                    setattr(item, "go_LITERAIS_BASICOS117", self)
                    

class go_Const:

    def __init__(self, const: str, go_Const: "go_TIPO" = None):
        self.const = const
        self.go_Const = go_Const
        
    @property
    def const(self) -> str:
        return self.__const

    @const.setter
    def const(self, const: str):
        self.__const = const

    @property
    def go_Const(self):
        return self.__go_Const

    @go_Const.setter
    def go_Const(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Const__go_Const", None)
        self.__go_Const = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_TIPO72"):
                opp_val = getattr(old_value, "go_TIPO72", None)
                if opp_val == self:
                    setattr(old_value, "go_TIPO72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_TIPO72"):
                opp_val = getattr(value, "go_TIPO72", None)
                setattr(value, "go_TIPO72", self)

class go_Var:

    def __init__(self, var: str, go_Var: "go_TIPO" = None):
        self.var = var
        self.go_Var = go_Var
        
    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def go_Var(self):
        return self.__go_Var

    @go_Var.setter
    def go_Var(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Var__go_Var", None)
        self.__go_Var = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_TIPO70"):
                opp_val = getattr(old_value, "go_TIPO70", None)
                if opp_val == self:
                    setattr(old_value, "go_TIPO70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_TIPO70"):
                opp_val = getattr(value, "go_TIPO70", None)
                setattr(value, "go_TIPO70", self)

class go_Types:

    pass
class go_TIPO:

    pass
class go_Assignment:

    def __init__(self, id: str, qtd: str, go_Assignment: "go_IGUAL" = None, go_Assignment64: "go_PONTOSIGUAL" = None, go_Assignment67: "go_EXPRESSAOLINHA" = None, go_Assignment88: "go_EXPRESSAO" = None):
        self.id = id
        self.qtd = qtd
        self.go_Assignment = go_Assignment
        self.go_Assignment64 = go_Assignment64
        self.go_Assignment67 = go_Assignment67
        self.go_Assignment88 = go_Assignment88
        
    @property
    def qtd(self) -> str:
        return self.__qtd

    @qtd.setter
    def qtd(self, qtd: str):
        self.__qtd = qtd

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def go_Assignment64(self):
        return self.__go_Assignment64

    @go_Assignment64.setter
    def go_Assignment64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Assignment__go_Assignment64", None)
        self.__go_Assignment64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_PONTOSIGUAL65"):
                opp_val = getattr(old_value, "go_PONTOSIGUAL65", None)
                if opp_val == self:
                    setattr(old_value, "go_PONTOSIGUAL65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_PONTOSIGUAL65"):
                opp_val = getattr(value, "go_PONTOSIGUAL65", None)
                setattr(value, "go_PONTOSIGUAL65", self)

    @property
    def go_Assignment88(self):
        return self.__go_Assignment88

    @go_Assignment88.setter
    def go_Assignment88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Assignment__go_Assignment88", None)
        self.__go_Assignment88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_EXPRESSAO87"):
                opp_val = getattr(old_value, "go_EXPRESSAO87", None)
                if opp_val == self:
                    setattr(old_value, "go_EXPRESSAO87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_EXPRESSAO87"):
                opp_val = getattr(value, "go_EXPRESSAO87", None)
                setattr(value, "go_EXPRESSAO87", self)

    @property
    def go_Assignment(self):
        return self.__go_Assignment

    @go_Assignment.setter
    def go_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Assignment__go_Assignment", None)
        self.__go_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_IGUAL62"):
                opp_val = getattr(old_value, "go_IGUAL62", None)
                if opp_val == self:
                    setattr(old_value, "go_IGUAL62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_IGUAL62"):
                opp_val = getattr(value, "go_IGUAL62", None)
                setattr(value, "go_IGUAL62", self)

    @property
    def go_Assignment67(self):
        return self.__go_Assignment67

    @go_Assignment67.setter
    def go_Assignment67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_Assignment__go_Assignment67", None)
        self.__go_Assignment67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_EXPRESSAOLINHA68"):
                opp_val = getattr(old_value, "go_EXPRESSAOLINHA68", None)
                if opp_val == self:
                    setattr(old_value, "go_EXPRESSAOLINHA68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_EXPRESSAOLINHA68"):
                opp_val = getattr(value, "go_EXPRESSAOLINHA68", None)
                setattr(value, "go_EXPRESSAOLINHA68", self)

class go_SignatureDel:

    def __init__(self, id: str, go_SignatureDel: "go_VarDecl" = None, go_SignatureDel58: "go_TIPO" = None, go_SignatureDel60: "go_Types" = None):
        self.id = id
        self.go_SignatureDel = go_SignatureDel
        self.go_SignatureDel58 = go_SignatureDel58
        self.go_SignatureDel60 = go_SignatureDel60
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def go_SignatureDel60(self):
        return self.__go_SignatureDel60

    @go_SignatureDel60.setter
    def go_SignatureDel60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SignatureDel__go_SignatureDel60", None)
        self.__go_SignatureDel60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Types"):
                opp_val = getattr(old_value, "go_Types", None)
                if opp_val == self:
                    setattr(old_value, "go_Types", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Types"):
                opp_val = getattr(value, "go_Types", None)
                setattr(value, "go_Types", self)

    @property
    def go_SignatureDel(self):
        return self.__go_SignatureDel

    @go_SignatureDel.setter
    def go_SignatureDel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SignatureDel__go_SignatureDel", None)
        self.__go_SignatureDel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_VarDecl45"):
                opp_val = getattr(old_value, "go_VarDecl45", None)
                if opp_val == self:
                    setattr(old_value, "go_VarDecl45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_VarDecl45"):
                opp_val = getattr(value, "go_VarDecl45", None)
                setattr(value, "go_VarDecl45", self)

    @property
    def go_SignatureDel58(self):
        return self.__go_SignatureDel58

    @go_SignatureDel58.setter
    def go_SignatureDel58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_SignatureDel__go_SignatureDel58", None)
        self.__go_SignatureDel58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_TIPO"):
                opp_val = getattr(old_value, "go_TIPO", None)
                if opp_val == self:
                    setattr(old_value, "go_TIPO", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_TIPO"):
                opp_val = getattr(value, "go_TIPO", None)
                setattr(value, "go_TIPO", self)

class go_ArrayType:

    def __init__(self, qtd: str, go_ArrayType: "go_VarDecl" = None, go_ArrayType162: "go_Types" = None, go_ArrayType164: "go_BasicType" = None):
        self.qtd = qtd
        self.go_ArrayType = go_ArrayType
        self.go_ArrayType162 = go_ArrayType162
        self.go_ArrayType164 = go_ArrayType164
        
    @property
    def qtd(self) -> str:
        return self.__qtd

    @qtd.setter
    def qtd(self, qtd: str):
        self.__qtd = qtd

    @property
    def go_ArrayType162(self):
        return self.__go_ArrayType162

    @go_ArrayType162.setter
    def go_ArrayType162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_ArrayType__go_ArrayType162", None)
        self.__go_ArrayType162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Types161"):
                opp_val = getattr(old_value, "go_Types161", None)
                if opp_val == self:
                    setattr(old_value, "go_Types161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Types161"):
                opp_val = getattr(value, "go_Types161", None)
                setattr(value, "go_Types161", self)

    @property
    def go_ArrayType(self):
        return self.__go_ArrayType

    @go_ArrayType.setter
    def go_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_ArrayType__go_ArrayType", None)
        self.__go_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_VarDecl53"):
                opp_val = getattr(old_value, "go_VarDecl53", None)
                if opp_val == self:
                    setattr(old_value, "go_VarDecl53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_VarDecl53"):
                opp_val = getattr(value, "go_VarDecl53", None)
                setattr(value, "go_VarDecl53", self)

    @property
    def go_ArrayType164(self):
        return self.__go_ArrayType164

    @go_ArrayType164.setter
    def go_ArrayType164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_ArrayType__go_ArrayType164", None)
        self.__go_ArrayType164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_BasicType165"):
                opp_val = getattr(old_value, "go_BasicType165", None)
                if opp_val == self:
                    setattr(old_value, "go_BasicType165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_BasicType165"):
                opp_val = getattr(value, "go_BasicType165", None)
                setattr(value, "go_BasicType165", self)

class go_EXPRESSAO:

    pass
class go_COMPARISON:

    def __init__(self, igual: str, maiorigualque: str, menorigualque: str, maiorque: str, menorque: str, go_COMPARISON: "go_Condition" = None):
        self.igual = igual
        self.maiorigualque = maiorigualque
        self.menorigualque = menorigualque
        self.maiorque = maiorque
        self.menorque = menorque
        self.go_COMPARISON = go_COMPARISON
        
    @property
    def maiorque(self) -> str:
        return self.__maiorque

    @maiorque.setter
    def maiorque(self, maiorque: str):
        self.__maiorque = maiorque

    @property
    def igual(self) -> str:
        return self.__igual

    @igual.setter
    def igual(self, igual: str):
        self.__igual = igual

    @property
    def maiorigualque(self) -> str:
        return self.__maiorigualque

    @maiorigualque.setter
    def maiorigualque(self, maiorigualque: str):
        self.__maiorigualque = maiorigualque

    @property
    def menorque(self) -> str:
        return self.__menorque

    @menorque.setter
    def menorque(self, menorque: str):
        self.__menorque = menorque

    @property
    def menorigualque(self) -> str:
        return self.__menorigualque

    @menorigualque.setter
    def menorigualque(self, menorigualque: str):
        self.__menorigualque = menorigualque

    @property
    def go_COMPARISON(self):
        return self.__go_COMPARISON

    @go_COMPARISON.setter
    def go_COMPARISON(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_COMPARISON__go_COMPARISON", None)
        self.__go_COMPARISON = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Condition37"):
                opp_val = getattr(old_value, "go_Condition37", None)
                if opp_val == self:
                    setattr(old_value, "go_Condition37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Condition37"):
                opp_val = getattr(value, "go_Condition37", None)
                setattr(value, "go_Condition37", self)

class go_InitStmt:

    pass
class go_FunctionCall:

    def __init__(self, id: str, go_FunctionCall: "go_RangeDecl" = None, go_FunctionCall105: "go_ReturnStmt" = None, go_FunctionCall123: "go_BINARY_EXP" = None, go_FunctionCall167: "go_PARAMETERS_LIST" = None):
        self.id = id
        self.go_FunctionCall = go_FunctionCall
        self.go_FunctionCall105 = go_FunctionCall105
        self.go_FunctionCall123 = go_FunctionCall123
        self.go_FunctionCall167 = go_FunctionCall167
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def go_FunctionCall123(self):
        return self.__go_FunctionCall123

    @go_FunctionCall123.setter
    def go_FunctionCall123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_FunctionCall__go_FunctionCall123", None)
        self.__go_FunctionCall123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_BINARY_EXP122"):
                opp_val = getattr(old_value, "go_BINARY_EXP122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_BINARY_EXP122"):
                opp_val = getattr(value, "go_BINARY_EXP122", None)
                if opp_val is None:
                    setattr(value, "go_BINARY_EXP122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def go_FunctionCall(self):
        return self.__go_FunctionCall

    @go_FunctionCall.setter
    def go_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_FunctionCall__go_FunctionCall", None)
        self.__go_FunctionCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_RangeDecl22"):
                opp_val = getattr(old_value, "go_RangeDecl22", None)
                if opp_val == self:
                    setattr(old_value, "go_RangeDecl22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_RangeDecl22"):
                opp_val = getattr(value, "go_RangeDecl22", None)
                setattr(value, "go_RangeDecl22", self)

    @property
    def go_FunctionCall167(self):
        return self.__go_FunctionCall167

    @go_FunctionCall167.setter
    def go_FunctionCall167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_FunctionCall__go_FunctionCall167", None)
        self.__go_FunctionCall167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_PARAMETERS_LIST168"):
                opp_val = getattr(old_value, "go_PARAMETERS_LIST168", None)
                if opp_val == self:
                    setattr(old_value, "go_PARAMETERS_LIST168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_PARAMETERS_LIST168"):
                opp_val = getattr(value, "go_PARAMETERS_LIST168", None)
                setattr(value, "go_PARAMETERS_LIST168", self)

    @property
    def go_FunctionCall105(self):
        return self.__go_FunctionCall105

    @go_FunctionCall105.setter
    def go_FunctionCall105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_FunctionCall__go_FunctionCall105", None)
        self.__go_FunctionCall105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ReturnStmt104"):
                opp_val = getattr(old_value, "go_ReturnStmt104", None)
                if opp_val == self:
                    setattr(old_value, "go_ReturnStmt104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ReturnStmt104"):
                opp_val = getattr(value, "go_ReturnStmt104", None)
                setattr(value, "go_ReturnStmt104", self)

class go_ARIT_EXPR:

    def __init__(self, num1: str, op: str, num2: str, atr: str, num: str, go_ARIT_EXPR: "go_PostStmt" = None, go_ARIT_EXPR173: "go_VarCall" = None, go_ARIT_EXPR176: "go_VarCall" = None, go_ARIT_EXPR179: "go_VarCall" = None):
        self.num1 = num1
        self.op = op
        self.num2 = num2
        self.atr = atr
        self.num = num
        self.go_ARIT_EXPR = go_ARIT_EXPR
        self.go_ARIT_EXPR173 = go_ARIT_EXPR173
        self.go_ARIT_EXPR176 = go_ARIT_EXPR176
        self.go_ARIT_EXPR179 = go_ARIT_EXPR179
        
    @property
    def atr(self) -> str:
        return self.__atr

    @atr.setter
    def atr(self, atr: str):
        self.__atr = atr

    @property
    def num2(self) -> str:
        return self.__num2

    @num2.setter
    def num2(self, num2: str):
        self.__num2 = num2

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def num(self) -> str:
        return self.__num

    @num.setter
    def num(self, num: str):
        self.__num = num

    @property
    def num1(self) -> str:
        return self.__num1

    @num1.setter
    def num1(self, num1: str):
        self.__num1 = num1

    @property
    def go_ARIT_EXPR173(self):
        return self.__go_ARIT_EXPR173

    @go_ARIT_EXPR173.setter
    def go_ARIT_EXPR173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_ARIT_EXPR__go_ARIT_EXPR173", None)
        self.__go_ARIT_EXPR173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_VarCall174"):
                opp_val = getattr(old_value, "go_VarCall174", None)
                if opp_val == self:
                    setattr(old_value, "go_VarCall174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_VarCall174"):
                opp_val = getattr(value, "go_VarCall174", None)
                setattr(value, "go_VarCall174", self)

    @property
    def go_ARIT_EXPR176(self):
        return self.__go_ARIT_EXPR176

    @go_ARIT_EXPR176.setter
    def go_ARIT_EXPR176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_ARIT_EXPR__go_ARIT_EXPR176", None)
        self.__go_ARIT_EXPR176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_VarCall177"):
                opp_val = getattr(old_value, "go_VarCall177", None)
                if opp_val == self:
                    setattr(old_value, "go_VarCall177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_VarCall177"):
                opp_val = getattr(value, "go_VarCall177", None)
                setattr(value, "go_VarCall177", self)

    @property
    def go_ARIT_EXPR(self):
        return self.__go_ARIT_EXPR

    @go_ARIT_EXPR.setter
    def go_ARIT_EXPR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_ARIT_EXPR__go_ARIT_EXPR", None)
        self.__go_ARIT_EXPR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_PostStmt33"):
                opp_val = getattr(old_value, "go_PostStmt33", None)
                if opp_val == self:
                    setattr(old_value, "go_PostStmt33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_PostStmt33"):
                opp_val = getattr(value, "go_PostStmt33", None)
                setattr(value, "go_PostStmt33", self)

    @property
    def go_ARIT_EXPR179(self):
        return self.__go_ARIT_EXPR179

    @go_ARIT_EXPR179.setter
    def go_ARIT_EXPR179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_ARIT_EXPR__go_ARIT_EXPR179", None)
        self.__go_ARIT_EXPR179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_VarCall180"):
                opp_val = getattr(old_value, "go_VarCall180", None)
                if opp_val == self:
                    setattr(old_value, "go_VarCall180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_VarCall180"):
                opp_val = getattr(value, "go_VarCall180", None)
                setattr(value, "go_VarCall180", self)

class go_PostStmt:

    pass
class go_Condition:

    pass
class go_VarCall:

    def __init__(self, id: str, go_VarCall: "go_RangeDecl" = None, go_VarCall108: "go_ReturnStmt" = None, go_VarCall120: "go_BINARY_EXP" = None, go_VarCall174: "go_ARIT_EXPR" = None, go_VarCall177: "go_ARIT_EXPR" = None, go_VarCall180: "go_ARIT_EXPR" = None):
        self.id = id
        self.go_VarCall = go_VarCall
        self.go_VarCall108 = go_VarCall108
        self.go_VarCall120 = go_VarCall120
        self.go_VarCall174 = go_VarCall174
        self.go_VarCall177 = go_VarCall177
        self.go_VarCall180 = go_VarCall180
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def go_VarCall(self):
        return self.__go_VarCall

    @go_VarCall.setter
    def go_VarCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_VarCall__go_VarCall", None)
        self.__go_VarCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_RangeDecl20"):
                opp_val = getattr(old_value, "go_RangeDecl20", None)
                if opp_val == self:
                    setattr(old_value, "go_RangeDecl20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_RangeDecl20"):
                opp_val = getattr(value, "go_RangeDecl20", None)
                setattr(value, "go_RangeDecl20", self)

    @property
    def go_VarCall174(self):
        return self.__go_VarCall174

    @go_VarCall174.setter
    def go_VarCall174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_VarCall__go_VarCall174", None)
        self.__go_VarCall174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ARIT_EXPR173"):
                opp_val = getattr(old_value, "go_ARIT_EXPR173", None)
                if opp_val == self:
                    setattr(old_value, "go_ARIT_EXPR173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ARIT_EXPR173"):
                opp_val = getattr(value, "go_ARIT_EXPR173", None)
                setattr(value, "go_ARIT_EXPR173", self)

    @property
    def go_VarCall120(self):
        return self.__go_VarCall120

    @go_VarCall120.setter
    def go_VarCall120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_VarCall__go_VarCall120", None)
        self.__go_VarCall120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_BINARY_EXP119"):
                opp_val = getattr(old_value, "go_BINARY_EXP119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_BINARY_EXP119"):
                opp_val = getattr(value, "go_BINARY_EXP119", None)
                if opp_val is None:
                    setattr(value, "go_BINARY_EXP119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def go_VarCall108(self):
        return self.__go_VarCall108

    @go_VarCall108.setter
    def go_VarCall108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_VarCall__go_VarCall108", None)
        self.__go_VarCall108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ReturnStmt107"):
                opp_val = getattr(old_value, "go_ReturnStmt107", None)
                if opp_val == self:
                    setattr(old_value, "go_ReturnStmt107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ReturnStmt107"):
                opp_val = getattr(value, "go_ReturnStmt107", None)
                setattr(value, "go_ReturnStmt107", self)

    @property
    def go_VarCall180(self):
        return self.__go_VarCall180

    @go_VarCall180.setter
    def go_VarCall180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_VarCall__go_VarCall180", None)
        self.__go_VarCall180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ARIT_EXPR179"):
                opp_val = getattr(old_value, "go_ARIT_EXPR179", None)
                if opp_val == self:
                    setattr(old_value, "go_ARIT_EXPR179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ARIT_EXPR179"):
                opp_val = getattr(value, "go_ARIT_EXPR179", None)
                setattr(value, "go_ARIT_EXPR179", self)

    @property
    def go_VarCall177(self):
        return self.__go_VarCall177

    @go_VarCall177.setter
    def go_VarCall177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_VarCall__go_VarCall177", None)
        self.__go_VarCall177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_ARIT_EXPR176"):
                opp_val = getattr(old_value, "go_ARIT_EXPR176", None)
                if opp_val == self:
                    setattr(old_value, "go_ARIT_EXPR176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_ARIT_EXPR176"):
                opp_val = getattr(value, "go_ARIT_EXPR176", None)
                setattr(value, "go_ARIT_EXPR176", self)

class go_PONTOSIGUAL:

    def __init__(self, op: str, go_PONTOSIGUAL: "go_RangeDecl" = None, go_PONTOSIGUAL51: "go_VarDecl" = None, go_PONTOSIGUAL65: "go_Assignment" = None):
        self.op = op
        self.go_PONTOSIGUAL = go_PONTOSIGUAL
        self.go_PONTOSIGUAL51 = go_PONTOSIGUAL51
        self.go_PONTOSIGUAL65 = go_PONTOSIGUAL65
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def go_PONTOSIGUAL51(self):
        return self.__go_PONTOSIGUAL51

    @go_PONTOSIGUAL51.setter
    def go_PONTOSIGUAL51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_PONTOSIGUAL__go_PONTOSIGUAL51", None)
        self.__go_PONTOSIGUAL51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_VarDecl50"):
                opp_val = getattr(old_value, "go_VarDecl50", None)
                if opp_val == self:
                    setattr(old_value, "go_VarDecl50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_VarDecl50"):
                opp_val = getattr(value, "go_VarDecl50", None)
                setattr(value, "go_VarDecl50", self)

    @property
    def go_PONTOSIGUAL65(self):
        return self.__go_PONTOSIGUAL65

    @go_PONTOSIGUAL65.setter
    def go_PONTOSIGUAL65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_PONTOSIGUAL__go_PONTOSIGUAL65", None)
        self.__go_PONTOSIGUAL65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Assignment64"):
                opp_val = getattr(old_value, "go_Assignment64", None)
                if opp_val == self:
                    setattr(old_value, "go_Assignment64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Assignment64"):
                opp_val = getattr(value, "go_Assignment64", None)
                setattr(value, "go_Assignment64", self)

    @property
    def go_PONTOSIGUAL(self):
        return self.__go_PONTOSIGUAL

    @go_PONTOSIGUAL.setter
    def go_PONTOSIGUAL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_PONTOSIGUAL__go_PONTOSIGUAL", None)
        self.__go_PONTOSIGUAL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_RangeDecl18"):
                opp_val = getattr(old_value, "go_RangeDecl18", None)
                if opp_val == self:
                    setattr(old_value, "go_RangeDecl18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_RangeDecl18"):
                opp_val = getattr(value, "go_RangeDecl18", None)
                setattr(value, "go_RangeDecl18", self)

class go_IGUAL:

    def __init__(self, igual: str, go_IGUAL: "go_RangeDecl" = None, go_IGUAL48: "go_VarDecl" = None, go_IGUAL62: "go_Assignment" = None):
        self.igual = igual
        self.go_IGUAL = go_IGUAL
        self.go_IGUAL48 = go_IGUAL48
        self.go_IGUAL62 = go_IGUAL62
        
    @property
    def igual(self) -> str:
        return self.__igual

    @igual.setter
    def igual(self, igual: str):
        self.__igual = igual

    @property
    def go_IGUAL(self):
        return self.__go_IGUAL

    @go_IGUAL.setter
    def go_IGUAL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_IGUAL__go_IGUAL", None)
        self.__go_IGUAL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_RangeDecl16"):
                opp_val = getattr(old_value, "go_RangeDecl16", None)
                if opp_val == self:
                    setattr(old_value, "go_RangeDecl16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_RangeDecl16"):
                opp_val = getattr(value, "go_RangeDecl16", None)
                setattr(value, "go_RangeDecl16", self)

    @property
    def go_IGUAL62(self):
        return self.__go_IGUAL62

    @go_IGUAL62.setter
    def go_IGUAL62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_IGUAL__go_IGUAL62", None)
        self.__go_IGUAL62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Assignment"):
                opp_val = getattr(old_value, "go_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "go_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Assignment"):
                opp_val = getattr(value, "go_Assignment", None)
                setattr(value, "go_Assignment", self)

    @property
    def go_IGUAL48(self):
        return self.__go_IGUAL48

    @go_IGUAL48.setter
    def go_IGUAL48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_IGUAL__go_IGUAL48", None)
        self.__go_IGUAL48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_VarDecl47"):
                opp_val = getattr(old_value, "go_VarDecl47", None)
                if opp_val == self:
                    setattr(old_value, "go_VarDecl47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_VarDecl47"):
                opp_val = getattr(value, "go_VarDecl47", None)
                setattr(value, "go_VarDecl47", self)

class go_IDList:

    def __init__(self, idList: str, vir: str, go_IDList: "go_RangeDecl" = None, go_IDList43: "go_IDList" = None, go_IDList41: set["go_IDList"] = None):
        self.idList = idList
        self.vir = vir
        self.go_IDList = go_IDList
        self.go_IDList43 = go_IDList43
        self.go_IDList41 = go_IDList41 if go_IDList41 is not None else set()
        
    @property
    def vir(self) -> str:
        return self.__vir

    @vir.setter
    def vir(self, vir: str):
        self.__vir = vir

    @property
    def idList(self) -> str:
        return self.__idList

    @idList.setter
    def idList(self, idList: str):
        self.__idList = idList

    @property
    def go_IDList43(self):
        return self.__go_IDList43

    @go_IDList43.setter
    def go_IDList43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_IDList__go_IDList43", None)
        self.__go_IDList43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_IDList41"):
                opp_val = getattr(old_value, "go_IDList41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_IDList41"):
                opp_val = getattr(value, "go_IDList41", None)
                if opp_val is None:
                    setattr(value, "go_IDList41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def go_IDList(self):
        return self.__go_IDList

    @go_IDList.setter
    def go_IDList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_IDList__go_IDList", None)
        self.__go_IDList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_RangeDecl14"):
                opp_val = getattr(old_value, "go_RangeDecl14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_RangeDecl14"):
                opp_val = getattr(value, "go_RangeDecl14", None)
                if opp_val is None:
                    setattr(value, "go_RangeDecl14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def go_IDList41(self):
        return self.__go_IDList41

    @go_IDList41.setter
    def go_IDList41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_IDList__go_IDList41", None)
        self.__go_IDList41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "go_IDList43"):
                    opp_val = getattr(item, "go_IDList43", None)
                    
                    if opp_val == self:
                        setattr(item, "go_IDList43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "go_IDList43"):
                    opp_val = getattr(item, "go_IDList43", None)
                    
                    setattr(item, "go_IDList43", self)
                    

class go_FunctionType:

    def __init__(self, nome: str, go_FunctionType: "go_GoDecl" = None, go_FunctionType81: "go_EXPRESSAO" = None, go_FunctionType127: "go_Signature" = None, go_FunctionType129: "go_BLOCK" = None):
        self.nome = nome
        self.go_FunctionType = go_FunctionType
        self.go_FunctionType81 = go_FunctionType81
        self.go_FunctionType127 = go_FunctionType127
        self.go_FunctionType129 = go_FunctionType129
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def go_FunctionType81(self):
        return self.__go_FunctionType81

    @go_FunctionType81.setter
    def go_FunctionType81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_FunctionType__go_FunctionType81", None)
        self.__go_FunctionType81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_EXPRESSAO80"):
                opp_val = getattr(old_value, "go_EXPRESSAO80", None)
                if opp_val == self:
                    setattr(old_value, "go_EXPRESSAO80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_EXPRESSAO80"):
                opp_val = getattr(value, "go_EXPRESSAO80", None)
                setattr(value, "go_EXPRESSAO80", self)

    @property
    def go_FunctionType129(self):
        return self.__go_FunctionType129

    @go_FunctionType129.setter
    def go_FunctionType129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_FunctionType__go_FunctionType129", None)
        self.__go_FunctionType129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_BLOCK"):
                opp_val = getattr(old_value, "go_BLOCK", None)
                if opp_val == self:
                    setattr(old_value, "go_BLOCK", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_BLOCK"):
                opp_val = getattr(value, "go_BLOCK", None)
                setattr(value, "go_BLOCK", self)

    @property
    def go_FunctionType127(self):
        return self.__go_FunctionType127

    @go_FunctionType127.setter
    def go_FunctionType127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_FunctionType__go_FunctionType127", None)
        self.__go_FunctionType127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_Signature"):
                opp_val = getattr(old_value, "go_Signature", None)
                if opp_val == self:
                    setattr(old_value, "go_Signature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_Signature"):
                opp_val = getattr(value, "go_Signature", None)
                setattr(value, "go_Signature", self)

    @property
    def go_FunctionType(self):
        return self.__go_FunctionType

    @go_FunctionType.setter
    def go_FunctionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_FunctionType__go_FunctionType", None)
        self.__go_FunctionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_GoDecl4"):
                opp_val = getattr(old_value, "go_GoDecl4", None)
                if opp_val == self:
                    setattr(old_value, "go_GoDecl4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_GoDecl4"):
                opp_val = getattr(value, "go_GoDecl4", None)
                setattr(value, "go_GoDecl4", self)

class go_VarDecl:

    pass
class go_RangeDecl:

    pass
class go_ForClause:

    pass
class go_ForDecl:

    pass
class go_EXPRESSAOLINHA:

    pass
class go_BOOLEAN_VALUE:

    def __init__(self, verdadeiro: str, falso: str, go_BOOLEAN_VALUE: "go_LITERAIS_BASICOS" = None):
        self.verdadeiro = verdadeiro
        self.falso = falso
        self.go_BOOLEAN_VALUE = go_BOOLEAN_VALUE
        
    @property
    def falso(self) -> str:
        return self.__falso

    @falso.setter
    def falso(self, falso: str):
        self.__falso = falso

    @property
    def verdadeiro(self) -> str:
        return self.__verdadeiro

    @verdadeiro.setter
    def verdadeiro(self, verdadeiro: str):
        self.__verdadeiro = verdadeiro

    @property
    def go_BOOLEAN_VALUE(self):
        return self.__go_BOOLEAN_VALUE

    @go_BOOLEAN_VALUE.setter
    def go_BOOLEAN_VALUE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_go_BOOLEAN_VALUE__go_BOOLEAN_VALUE", None)
        self.__go_BOOLEAN_VALUE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "go_LITERAIS_BASICOS114"):
                opp_val = getattr(old_value, "go_LITERAIS_BASICOS114", None)
                if opp_val == self:
                    setattr(old_value, "go_LITERAIS_BASICOS114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "go_LITERAIS_BASICOS114"):
                opp_val = getattr(value, "go_LITERAIS_BASICOS114", None)
                setattr(value, "go_LITERAIS_BASICOS114", self)

class go_GoDecl:

    pass
class go_Init:

    pass