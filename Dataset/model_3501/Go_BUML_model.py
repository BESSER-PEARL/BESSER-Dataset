####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
go_Init = Class(name="go::Init")
go_GoDecl = Class(name="go::GoDecl")
go_BOOLEAN_VALUE = Class(name="go::BOOLEAN::VALUE")
go_EXPRESSAOLINHA = Class(name="go::EXPRESSAOLINHA")
go_ForDecl = Class(name="go::ForDecl")
go_ForClause = Class(name="go::ForClause")
go_RangeDecl = Class(name="go::RangeDecl")
go_VarDecl = Class(name="go::VarDecl")
go_FunctionType = Class(name="go::FunctionType")
go_IDList = Class(name="go::IDList")
go_IGUAL = Class(name="go::IGUAL")
go_PONTOSIGUAL = Class(name="go::PONTOSIGUAL")
go_VarCall = Class(name="go::VarCall")
go_Condition = Class(name="go::Condition")
go_PostStmt = Class(name="go::PostStmt")
go_ARIT_EXPR = Class(name="go::ARIT::EXPR")
go_FunctionCall = Class(name="go::FunctionCall")
go_InitStmt = Class(name="go::InitStmt")
go_COMPARISON = Class(name="go::COMPARISON")
go_EXPRESSAO = Class(name="go::EXPRESSAO")
go_ArrayType = Class(name="go::ArrayType")
go_SignatureDel = Class(name="go::SignatureDel")
go_Assignment = Class(name="go::Assignment")
go_TIPO = Class(name="go::TIPO")
go_Types = Class(name="go::Types")
go_Var = Class(name="go::Var")
go_Const = Class(name="go::Const")
go_BINARY_EXP = Class(name="go::BINARY::EXP")
go_LITERAIS_BASICOS = Class(name="go::LITERAIS::BASICOS")
go_IfStmt = Class(name="go::IfStmt")
go_ReturnStmt = Class(name="go::ReturnStmt")
go_LiteraisList = Class(name="go::LiteraisList")
go_EObject = Class(name="go::EObject")
go_ArrayValue = Class(name="go::ArrayValue")
go_Chamada = Class(name="go::Chamada")
go_BOOL_OP = Class(name="go::BOOL::OP")
go_Signature = Class(name="go::Signature")
go_BLOCK = Class(name="go::BLOCK")
go_IfCondition = Class(name="go::IfCondition")
ElseIfCondition = Class(name="ElseIfCondition")
go_ElseIfCondition = Class(name="go::ElseIfCondition")
go_ElseCondition = Class(name="go::ElseCondition")
go_Parameters = Class(name="go::Parameters")
go_PARAMETERS_LIST = Class(name="go::PARAMETERS::LIST")
go_BasicType = Class(name="go::BasicType")
go_PARAMETER = Class(name="go::PARAMETER")

# go_Init class attributes and methods

# go_GoDecl class attributes and methods

# go_BOOLEAN_VALUE class attributes and methods
go_BOOLEAN_VALUE_verdadeiro: Property = Property(name="verdadeiro", type=StringType)
go_BOOLEAN_VALUE_falso: Property = Property(name="falso", type=StringType)
go_BOOLEAN_VALUE.attributes={go_BOOLEAN_VALUE_falso, go_BOOLEAN_VALUE_verdadeiro}

# go_EXPRESSAOLINHA class attributes and methods

# go_ForDecl class attributes and methods

# go_ForClause class attributes and methods

# go_RangeDecl class attributes and methods

# go_VarDecl class attributes and methods

# go_FunctionType class attributes and methods
go_FunctionType_nome: Property = Property(name="nome", type=StringType)
go_FunctionType.attributes={go_FunctionType_nome}

# go_IDList class attributes and methods
go_IDList_idList: Property = Property(name="idList", type=StringType)
go_IDList_vir: Property = Property(name="vir", type=StringType)
go_IDList.attributes={go_IDList_vir, go_IDList_idList}

# go_IGUAL class attributes and methods
go_IGUAL_igual: Property = Property(name="igual", type=StringType)
go_IGUAL.attributes={go_IGUAL_igual}

# go_PONTOSIGUAL class attributes and methods
go_PONTOSIGUAL_op: Property = Property(name="op", type=StringType)
go_PONTOSIGUAL.attributes={go_PONTOSIGUAL_op}

# go_VarCall class attributes and methods
go_VarCall_id: Property = Property(name="id", type=StringType)
go_VarCall.attributes={go_VarCall_id}

# go_Condition class attributes and methods

# go_PostStmt class attributes and methods

# go_ARIT_EXPR class attributes and methods
go_ARIT_EXPR_num1: Property = Property(name="num1", type=StringType)
go_ARIT_EXPR_op: Property = Property(name="op", type=StringType)
go_ARIT_EXPR_num2: Property = Property(name="num2", type=StringType)
go_ARIT_EXPR_atr: Property = Property(name="atr", type=StringType)
go_ARIT_EXPR_num: Property = Property(name="num", type=StringType)
go_ARIT_EXPR.attributes={go_ARIT_EXPR_atr, go_ARIT_EXPR_num2, go_ARIT_EXPR_op, go_ARIT_EXPR_num, go_ARIT_EXPR_num1}

# go_FunctionCall class attributes and methods
go_FunctionCall_id: Property = Property(name="id", type=StringType)
go_FunctionCall.attributes={go_FunctionCall_id}

# go_InitStmt class attributes and methods

# go_COMPARISON class attributes and methods
go_COMPARISON_igual: Property = Property(name="igual", type=StringType)
go_COMPARISON_maiorigualque: Property = Property(name="maiorigualque", type=StringType)
go_COMPARISON_menorigualque: Property = Property(name="menorigualque", type=StringType)
go_COMPARISON_maiorque: Property = Property(name="maiorque", type=StringType)
go_COMPARISON_menorque: Property = Property(name="menorque", type=StringType)
go_COMPARISON.attributes={go_COMPARISON_maiorque, go_COMPARISON_igual, go_COMPARISON_maiorigualque, go_COMPARISON_menorque, go_COMPARISON_menorigualque}

# go_EXPRESSAO class attributes and methods

# go_ArrayType class attributes and methods
go_ArrayType_qtd: Property = Property(name="qtd", type=StringType)
go_ArrayType.attributes={go_ArrayType_qtd}

# go_SignatureDel class attributes and methods
go_SignatureDel_id: Property = Property(name="id", type=StringType)
go_SignatureDel.attributes={go_SignatureDel_id}

# go_Assignment class attributes and methods
go_Assignment_id: Property = Property(name="id", type=StringType)
go_Assignment_qtd: Property = Property(name="qtd", type=StringType)
go_Assignment.attributes={go_Assignment_qtd, go_Assignment_id}

# go_TIPO class attributes and methods

# go_Types class attributes and methods

# go_Var class attributes and methods
go_Var_var: Property = Property(name="var", type=StringType)
go_Var.attributes={go_Var_var}

# go_Const class attributes and methods
go_Const_const: Property = Property(name="const", type=StringType)
go_Const.attributes={go_Const_const}

# go_BINARY_EXP class attributes and methods
go_BINARY_EXP_arit: Property = Property(name="arit", type=StringType)
go_BINARY_EXP.attributes={go_BINARY_EXP_arit}

# go_LITERAIS_BASICOS class attributes and methods
go_LITERAIS_BASICOS_numero: Property = Property(name="numero", type=StringType)
go_LITERAIS_BASICOS_string: Property = Property(name="string", type=StringType)
go_LITERAIS_BASICOS.attributes={go_LITERAIS_BASICOS_string, go_LITERAIS_BASICOS_numero}

# go_IfStmt class attributes and methods

# go_ReturnStmt class attributes and methods

# go_LiteraisList class attributes and methods
go_LiteraisList_vir: Property = Property(name="vir", type=StringType)
go_LiteraisList.attributes={go_LiteraisList_vir}

# go_EObject class attributes and methods

# go_ArrayValue class attributes and methods

# go_Chamada class attributes and methods

# go_BOOL_OP class attributes and methods

# go_Signature class attributes and methods

# go_BLOCK class attributes and methods

# go_IfCondition class attributes and methods

# ElseIfCondition class attributes and methods

# go_ElseIfCondition class attributes and methods

# go_ElseCondition class attributes and methods

# go_Parameters class attributes and methods

# go_PARAMETERS_LIST class attributes and methods
go_PARAMETERS_LIST_vir: Property = Property(name="vir", type=StringType)
go_PARAMETERS_LIST.attributes={go_PARAMETERS_LIST_vir}

# go_BasicType class attributes and methods
go_BasicType_string: Property = Property(name="string", type=StringType)
go_BasicType_int: Property = Property(name="int", type=StringType)
go_BasicType_float: Property = Property(name="float", type=StringType)
go_BasicType_boolean: Property = Property(name="boolean", type=StringType)
go_BasicType.attributes={go_BasicType_float, go_BasicType_boolean, go_BasicType_int, go_BasicType_string}

# go_PARAMETER class attributes and methods
go_PARAMETER_id: Property = Property(name="id", type=StringType)
go_PARAMETER.attributes={go_PARAMETER_id}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="go_GoDecl", type=go_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Init", type=go_GoDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressao5: BinaryAssociation = BinaryAssociation(
    name="expressao5",
    ends={
        Property(name="go_EXPRESSAOLINHA", type=go_GoDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_GoDecl6", type=go_EXPRESSAOLINHA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clause7: BinaryAssociation = BinaryAssociation(
    name="clause7",
    ends={
        Property(name="go_ForClause", type=go_ForDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForDecl", type=go_ForClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var1: BinaryAssociation = BinaryAssociation(
    name="var1",
    ends={
        Property(name="go_VarDecl", type=go_GoDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_GoDecl2", type=go_VarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func3: BinaryAssociation = BinaryAssociation(
    name="func3",
    ends={
        Property(name="go_FunctionType", type=go_GoDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_GoDecl4", type=go_FunctionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
idList13: BinaryAssociation = BinaryAssociation(
    name="idList13",
    ends={
        Property(name="go_IDList", type=go_RangeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RangeDecl14", type=go_IDList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
igual15: BinaryAssociation = BinaryAssociation(
    name="igual15",
    ends={
        Property(name="go_IGUAL", type=go_RangeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RangeDecl16", type=go_IGUAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op17: BinaryAssociation = BinaryAssociation(
    name="op17",
    ends={
        Property(name="go_PONTOSIGUAL", type=go_RangeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RangeDecl18", type=go_PONTOSIGUAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variavel19: BinaryAssociation = BinaryAssociation(
    name="variavel19",
    ends={
        Property(name="go_VarCall", type=go_RangeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RangeDecl20", type=go_VarCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
range8: BinaryAssociation = BinaryAssociation(
    name="range8",
    ends={
        Property(name="go_RangeDecl", type=go_ForDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForDecl9", type=go_RangeDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comandos10: BinaryAssociation = BinaryAssociation(
    name="comandos10",
    ends={
        Property(name="go_GoDecl12", type=go_ForDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForDecl11", type=go_GoDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition25: BinaryAssociation = BinaryAssociation(
    name="condition25",
    ends={
        Property(name="go_Condition", type=go_ForClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForClause26", type=go_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
post27: BinaryAssociation = BinaryAssociation(
    name="post27",
    ends={
        Property(name="go_PostStmt", type=go_ForClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForClause28", type=go_PostStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varDecl29: BinaryAssociation = BinaryAssociation(
    name="varDecl29",
    ends={
        Property(name="go_VarDecl31", type=go_InitStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_InitStmt30", type=go_VarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func21: BinaryAssociation = BinaryAssociation(
    name="func21",
    ends={
        Property(name="go_FunctionCall", type=go_RangeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RangeDecl22", type=go_FunctionCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init23: BinaryAssociation = BinaryAssociation(
    name="init23",
    ends={
        Property(name="go_InitStmt", type=go_ForClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForClause24", type=go_InitStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comparador36: BinaryAssociation = BinaryAssociation(
    name="comparador36",
    ends={
        Property(name="go_COMPARISON", type=go_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Condition37", type=go_COMPARISON, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr238: BinaryAssociation = BinaryAssociation(
    name="expr238",
    ends={
        Property(name="go_EXPRESSAO40", type=go_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Condition39", type=go_EXPRESSAO, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list42: BinaryAssociation = BinaryAssociation(
    name="list42",
    ends={
        Property(name="go_IDList43", type=go_IDList, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IDList41", type=go_IDList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
art32: BinaryAssociation = BinaryAssociation(
    name="art32",
    ends={
        Property(name="go_ARIT_EXPR", type=go_PostStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PostStmt33", type=go_ARIT_EXPR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr134: BinaryAssociation = BinaryAssociation(
    name="expr134",
    ends={
        Property(name="go_EXPRESSAO", type=go_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Condition35", type=go_EXPRESSAO, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atribuicao46: BinaryAssociation = BinaryAssociation(
    name="atribuicao46",
    ends={
        Property(name="go_VarDecl47", type=go_IGUAL, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="go_IGUAL48", type=go_VarDecl, multiplicity=Multiplicity(1, 1))
    }
)
pront49: BinaryAssociation = BinaryAssociation(
    name="pront49",
    ends={
        Property(name="go_PONTOSIGUAL51", type=go_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_VarDecl50", type=go_PONTOSIGUAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array52: BinaryAssociation = BinaryAssociation(
    name="array52",
    ends={
        Property(name="go_ArrayType", type=go_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_VarDecl53", type=go_ArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressao54: BinaryAssociation = BinaryAssociation(
    name="expressao54",
    ends={
        Property(name="go_EXPRESSAOLINHA56", type=go_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_VarDecl55", type=go_EXPRESSAOLINHA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature44: BinaryAssociation = BinaryAssociation(
    name="signature44",
    ends={
        Property(name="go_SignatureDel", type=go_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_VarDecl45", type=go_SignatureDel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
igual61: BinaryAssociation = BinaryAssociation(
    name="igual61",
    ends={
        Property(name="go_IGUAL62", type=go_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Assignment", type=go_IGUAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dois63: BinaryAssociation = BinaryAssociation(
    name="dois63",
    ends={
        Property(name="go_PONTOSIGUAL65", type=go_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Assignment64", type=go_PONTOSIGUAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressao66: BinaryAssociation = BinaryAssociation(
    name="expressao66",
    ends={
        Property(name="go_EXPRESSAOLINHA68", type=go_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Assignment67", type=go_EXPRESSAOLINHA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipoDecl57: BinaryAssociation = BinaryAssociation(
    name="tipoDecl57",
    ends={
        Property(name="go_TIPO", type=go_SignatureDel, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SignatureDel58", type=go_TIPO, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type59: BinaryAssociation = BinaryAssociation(
    name="type59",
    ends={
        Property(name="go_Types", type=go_SignatureDel, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SignatureDel60", type=go_Types, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constante71: BinaryAssociation = BinaryAssociation(
    name="constante71",
    ends={
        Property(name="go_Const", type=go_TIPO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TIPO72", type=go_Const, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variavel69: BinaryAssociation = BinaryAssociation(
    name="variavel69",
    ends={
        Property(name="go_Var", type=go_TIPO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TIPO70", type=go_Var, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declFunction79: BinaryAssociation = BinaryAssociation(
    name="declFunction79",
    ends={
        Property(name="go_FunctionType81", type=go_EXPRESSAO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAO80", type=go_FunctionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
binary_exp82: BinaryAssociation = BinaryAssociation(
    name="binary_exp82",
    ends={
        Property(name="go_BINARY_EXP", type=go_EXPRESSAO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAO83", type=go_BINARY_EXP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basic84: BinaryAssociation = BinaryAssociation(
    name="basic84",
    ends={
        Property(name="go_LITERAIS_BASICOS", type=go_EXPRESSAO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAO85", type=go_LITERAIS_BASICOS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment86: BinaryAssociation = BinaryAssociation(
    name="assignment86",
    ends={
        Property(name="go_Assignment88", type=go_EXPRESSAO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAO87", type=go_Assignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
for89: BinaryAssociation = BinaryAssociation(
    name="for89",
    ends={
        Property(name="go_ForDecl91", type=go_EXPRESSAO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAO90", type=go_ForDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp73: BinaryAssociation = BinaryAssociation(
    name="exp73",
    ends={
        Property(name="go_EXPRESSAO75", type=go_EXPRESSAOLINHA, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAOLINHA74", type=go_EXPRESSAO, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
explinha77: BinaryAssociation = BinaryAssociation(
    name="explinha77",
    ends={
        Property(name="go_EXPRESSAOLINHA78", type=go_EXPRESSAOLINHA, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAOLINHA76", type=go_EXPRESSAOLINHA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if99: BinaryAssociation = BinaryAssociation(
    name="if99",
    ends={
        Property(name="go_IfStmt", type=go_EXPRESSAO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAO100", type=go_IfStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basic101: BinaryAssociation = BinaryAssociation(
    name="basic101",
    ends={
        Property(name="go_LITERAIS_BASICOS102", type=go_ReturnStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ReturnStmt", type=go_LITERAIS_BASICOS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func103: BinaryAssociation = BinaryAssociation(
    name="func103",
    ends={
        Property(name="go_FunctionCall105", type=go_ReturnStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ReturnStmt104", type=go_FunctionCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
idVar106: BinaryAssociation = BinaryAssociation(
    name="idVar106",
    ends={
        Property(name="go_VarCall108", type=go_ReturnStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ReturnStmt107", type=go_VarCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lit109: BinaryAssociation = BinaryAssociation(
    name="lit109",
    ends={
        Property(name="go_LiteraisList", type=go_ArrayValue, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ArrayValue110", type=go_LiteraisList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lit111: BinaryAssociation = BinaryAssociation(
    name="lit111",
    ends={
        Property(name="go_EObject", type=go_LiteraisList, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LiteraisList112", type=go_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayValue92: BinaryAssociation = BinaryAssociation(
    name="arrayValue92",
    ends={
        Property(name="go_ArrayValue", type=go_EXPRESSAO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAO93", type=go_ArrayValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variaveis94: BinaryAssociation = BinaryAssociation(
    name="variaveis94",
    ends={
        Property(name="go_VarDecl96", type=go_EXPRESSAO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAO95", type=go_VarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cham97: BinaryAssociation = BinaryAssociation(
    name="cham97",
    ends={
        Property(name="go_Chamada", type=go_EXPRESSAO, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EXPRESSAO98", type=go_Chamada, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basic115: BinaryAssociation = BinaryAssociation(
    name="basic115",
    ends={
        Property(name="go_LITERAIS_BASICOS117", type=go_BINARY_EXP, multiplicity=Multiplicity(1, 1)),
        Property(name="go_BINARY_EXP116", type=go_LITERAIS_BASICOS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varCal118: BinaryAssociation = BinaryAssociation(
    name="varCal118",
    ends={
        Property(name="go_VarCall120", type=go_BINARY_EXP, multiplicity=Multiplicity(1, 1)),
        Property(name="go_BINARY_EXP119", type=go_VarCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
func121: BinaryAssociation = BinaryAssociation(
    name="func121",
    ends={
        Property(name="go_FunctionCall123", type=go_BINARY_EXP, multiplicity=Multiplicity(1, 1)),
        Property(name="go_BINARY_EXP122", type=go_FunctionCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bool124: BinaryAssociation = BinaryAssociation(
    name="bool124",
    ends={
        Property(name="go_BOOL_OP", type=go_BINARY_EXP, multiplicity=Multiplicity(1, 1)),
        Property(name="go_BINARY_EXP125", type=go_BOOL_OP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assinatura126: BinaryAssociation = BinaryAssociation(
    name="assinatura126",
    ends={
        Property(name="go_Signature", type=go_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionType127", type=go_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bloco128: BinaryAssociation = BinaryAssociation(
    name="bloco128",
    ends={
        Property(name="go_BLOCK", type=go_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionType129", type=go_BLOCK, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
booleano113: BinaryAssociation = BinaryAssociation(
    name="booleano113",
    ends={
        Property(name="go_BOOLEAN_VALUE", type=go_LITERAIS_BASICOS, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LITERAIS_BASICOS114", type=go_BOOLEAN_VALUE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond137: BinaryAssociation = BinaryAssociation(
    name="cond137",
    ends={
        Property(name="go_Condition138", type=go_IfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfCondition", type=go_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then139: BinaryAssociation = BinaryAssociation(
    name="then139",
    ends={
        Property(name="go_EXPRESSAO141", type=go_IfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfCondition140", type=go_EXPRESSAO, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
then142: BinaryAssociation = BinaryAssociation(
    name="then142",
    ends={
        Property(name="go_EXPRESSAO143", type=go_ElseCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ElseCondition", type=go_EXPRESSAO, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listaDeComandos144: BinaryAssociation = BinaryAssociation(
    name="listaDeComandos144",
    ends={
        Property(name="go_EXPRESSAO146", type=go_BLOCK, multiplicity=Multiplicity(1, 1)),
        Property(name="go_BLOCK145", type=go_EXPRESSAO, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
retorno147: BinaryAssociation = BinaryAssociation(
    name="retorno147",
    ends={
        Property(name="go_ReturnStmt149", type=go_BLOCK, multiplicity=Multiplicity(1, 1)),
        Property(name="go_BLOCK148", type=go_ReturnStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params130: BinaryAssociation = BinaryAssociation(
    name="params130",
    ends={
        Property(name="go_Parameters", type=go_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Signature131", type=go_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
retorno132: BinaryAssociation = BinaryAssociation(
    name="retorno132",
    ends={
        Property(name="go_Types134", type=go_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Signature133", type=go_Types, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params135: BinaryAssociation = BinaryAssociation(
    name="params135",
    ends={
        Property(name="go_PARAMETERS_LIST", type=go_Parameters, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Parameters136", type=go_PARAMETERS_LIST, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipo155: BinaryAssociation = BinaryAssociation(
    name="tipo155",
    ends={
        Property(name="go_Types157", type=go_PARAMETER, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PARAMETER156", type=go_Types, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basic158: BinaryAssociation = BinaryAssociation(
    name="basic158",
    ends={
        Property(name="go_BasicType", type=go_Types, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Types159", type=go_BasicType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array160: BinaryAssociation = BinaryAssociation(
    name="array160",
    ends={
        Property(name="go_ArrayType162", type=go_Types, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Types161", type=go_ArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params150: BinaryAssociation = BinaryAssociation(
    name="params150",
    ends={
        Property(name="go_PARAMETER", type=go_PARAMETERS_LIST, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PARAMETERS_LIST151", type=go_PARAMETER, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basico152: BinaryAssociation = BinaryAssociation(
    name="basico152",
    ends={
        Property(name="go_LITERAIS_BASICOS154", type=go_PARAMETER, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PARAMETER153", type=go_LITERAIS_BASICOS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params166: BinaryAssociation = BinaryAssociation(
    name="params166",
    ends={
        Property(name="go_PARAMETERS_LIST168", type=go_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionCall167", type=go_PARAMETERS_LIST, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basic163: BinaryAssociation = BinaryAssociation(
    name="basic163",
    ends={
        Property(name="go_BasicType165", type=go_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ArrayType164", type=go_BasicType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var1172: BinaryAssociation = BinaryAssociation(
    name="var1172",
    ends={
        Property(name="go_VarCall174", type=go_ARIT_EXPR, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ARIT_EXPR173", type=go_VarCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var2175: BinaryAssociation = BinaryAssociation(
    name="var2175",
    ends={
        Property(name="go_VarCall177", type=go_ARIT_EXPR, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ARIT_EXPR176", type=go_VarCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cham169: BinaryAssociation = BinaryAssociation(
    name="cham169",
    ends={
        Property(name="go_EObject171", type=go_Chamada, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Chamada170", type=go_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if181: BinaryAssociation = BinaryAssociation(
    name="if181",
    ends={
        Property(name="go_IfCondition183", type=go_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfStmt182", type=go_IfCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseif184: BinaryAssociation = BinaryAssociation(
    name="elseif184",
    ends={
        Property(name="go_ElseIfCondition", type=go_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfStmt185", type=go_ElseIfCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else186: BinaryAssociation = BinaryAssociation(
    name="else186",
    ends={
        Property(name="go_ElseCondition188", type=go_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfStmt187", type=go_ElseCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var178: BinaryAssociation = BinaryAssociation(
    name="var178",
    ends={
        Property(name="go_VarCall180", type=go_ARIT_EXPR, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ARIT_EXPR179", type=go_VarCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_go_IfCondition_ElseIfCondition = Generalization(general=ElseIfCondition, specific=go_IfCondition)

# Domain Model
domain_model = DomainModel(
    name="go",
    types={go_Init, go_GoDecl, go_BOOLEAN_VALUE, go_EXPRESSAOLINHA, go_ForDecl, go_ForClause, go_RangeDecl, go_VarDecl, go_FunctionType, go_IDList, go_IGUAL, go_PONTOSIGUAL, go_VarCall, go_Condition, go_PostStmt, go_ARIT_EXPR, go_FunctionCall, go_InitStmt, go_COMPARISON, go_EXPRESSAO, go_ArrayType, go_SignatureDel, go_Assignment, go_TIPO, go_Types, go_Var, go_Const, go_BINARY_EXP, go_LITERAIS_BASICOS, go_IfStmt, go_ReturnStmt, go_LiteraisList, go_EObject, go_ArrayValue, go_Chamada, go_BOOL_OP, go_Signature, go_BLOCK, go_IfCondition, ElseIfCondition, go_ElseIfCondition, go_ElseCondition, go_Parameters, go_PARAMETERS_LIST, go_BasicType, go_PARAMETER},
    associations={elements0, expressao5, clause7, var1, func3, idList13, igual15, op17, variavel19, range8, comandos10, condition25, post27, varDecl29, func21, init23, comparador36, expr238, list42, art32, expr134, atribuicao46, pront49, array52, expressao54, signature44, igual61, dois63, expressao66, tipoDecl57, type59, constante71, variavel69, declFunction79, binary_exp82, basic84, assignment86, for89, exp73, explinha77, if99, basic101, func103, idVar106, lit109, lit111, arrayValue92, variaveis94, cham97, basic115, varCal118, func121, bool124, assinatura126, bloco128, booleano113, cond137, then139, then142, listaDeComandos144, retorno147, params130, retorno132, params135, tipo155, basic158, array160, params150, basico152, params166, basic163, var1172, var2175, cham169, if181, elseif184, else186, var178},
    generalizations={gen_go_IfCondition_ElseIfCondition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)