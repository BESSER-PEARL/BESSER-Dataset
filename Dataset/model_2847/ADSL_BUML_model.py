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
aDSL_Program = Class(name="aDSL::Program")
aDSL_AbstractElements = Class(name="aDSL::AbstractElements")
aDSL_XClass = Class(name="aDSL::XClass")
VarDef = Class(name="VarDef")
aDSL_MainMethod = Class(name="aDSL::MainMethod")
Member = Class(name="Member")
aDSL_VariableType = Class(name="aDSL::VariableType")
aDSL_Body = Class(name="aDSL::Body")
aDSL_PrintInst = Class(name="aDSL::PrintInst")
Statement = Class(name="Statement")
aDSL_Expression = Class(name="aDSL::Expression")
aDSL_Method = Class(name="aDSL::Method")
aDSL_Parameter = Class(name="aDSL::Parameter")
aDSL_Member = Class(name="aDSL::Member")
aDSL_FuncVarDef = Class(name="aDSL::FuncVarDef")
aDSL_VariableDef = Class(name="aDSL::VariableDef")
aDSL_Operator = Class(name="aDSL::Operator")
aDSL_SharedArrayDef = Class(name="aDSL::SharedArrayDef")
SharedDef = Class(name="SharedDef")
aDSL_SharedVarDef = Class(name="aDSL::SharedVarDef")
aDSL_Statement = Class(name="aDSL::Statement")
aDSL_Block = Class(name="aDSL::Block")
aDSL_AsyncStat = Class(name="aDSL::AsyncStat")
aDSL_FinishStat = Class(name="aDSL::FinishStat")
aDSL_AtStat = Class(name="aDSL::AtStat")
aDSL_AtomicStatement = Class(name="aDSL::AtomicStatement")
aDSL_WhenStatement = Class(name="aDSL::WhenStatement")
aDSL_VarDef = Class(name="aDSL::VarDef")
aDSL_SharedDef = Class(name="aDSL::SharedDef")
aDSL_IntegerNegative = Class(name="aDSL::IntegerNegative")
aDSL_TryCatchStat = Class(name="aDSL::TryCatchStat")
aDSL_For2Statement = Class(name="aDSL::For2Statement")
aDSL_WhileStat = Class(name="aDSL::WhileStat")
aDSL_ForStat = Class(name="aDSL::ForStat")
aDSL_ReturnStat = Class(name="aDSL::ReturnStat")
aDSL_Assignment = Class(name="aDSL::Assignment")
Expression = Class(name="Expression")
aDSL_MemberSelection = Class(name="aDSL::MemberSelection")
aDSL_IfStat = Class(name="aDSL::IfStat")
aDSL_Or = Class(name="aDSL::Or")
aDSL_And = Class(name="aDSL::And")
aDSL_Equality = Class(name="aDSL::Equality")
aDSL_Comparison = Class(name="aDSL::Comparison")
aDSL_Plus = Class(name="aDSL::Plus")
aDSL_Minus = Class(name="aDSL::Minus")
aDSL_MulOrDiv = Class(name="aDSL::MulOrDiv")
aDSL_Not = Class(name="aDSL::Not")
aDSL_StringConstant = Class(name="aDSL::StringConstant")
aDSL_IntConstant = Class(name="aDSL::IntConstant")
aDSL_BoolConstant = Class(name="aDSL::BoolConstant")
aDSL_DeRef = Class(name="aDSL::DeRef")
aDSL_This = Class(name="aDSL::This")
aDSL_Null = Class(name="aDSL::Null")
aDSL_Reference = Class(name="aDSL::Reference")
aDSL_New = Class(name="aDSL::New")
aDSL_Init = Class(name="aDSL::Init")
aDSL_Here = Class(name="aDSL::Here")

# aDSL_Program class attributes and methods
aDSL_Program_name: Property = Property(name="name", type=StringType)
aDSL_Program.attributes={aDSL_Program_name}

# aDSL_AbstractElements class attributes and methods
aDSL_AbstractElements_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
aDSL_AbstractElements.attributes={aDSL_AbstractElements_importedNamespace}

# aDSL_XClass class attributes and methods
aDSL_XClass_name: Property = Property(name="name", type=StringType)
aDSL_XClass.attributes={aDSL_XClass_name}

# VarDef class attributes and methods

# aDSL_MainMethod class attributes and methods

# Member class attributes and methods

# aDSL_VariableType class attributes and methods
aDSL_VariableType_isarray: Property = Property(name="isarray", type=BooleanType)
aDSL_VariableType.attributes={aDSL_VariableType_isarray}

# aDSL_Body class attributes and methods

# aDSL_PrintInst class attributes and methods

# Statement class attributes and methods

# aDSL_Expression class attributes and methods

# aDSL_Method class attributes and methods
aDSL_Method_isconst: Property = Property(name="isconst", type=BooleanType)
aDSL_Method_name: Property = Property(name="name", type=StringType)
aDSL_Method_istyped: Property = Property(name="istyped", type=BooleanType)
aDSL_Method.attributes={aDSL_Method_istyped, aDSL_Method_name, aDSL_Method_isconst}

# aDSL_Parameter class attributes and methods
aDSL_Parameter_name: Property = Property(name="name", type=StringType)
aDSL_Parameter_istyped: Property = Property(name="istyped", type=BooleanType)
aDSL_Parameter.attributes={aDSL_Parameter_istyped, aDSL_Parameter_name}

# aDSL_Member class attributes and methods

# aDSL_FuncVarDef class attributes and methods
aDSL_FuncVarDef_name: Property = Property(name="name", type=StringType)
aDSL_FuncVarDef.attributes={aDSL_FuncVarDef_name}

# aDSL_VariableDef class attributes and methods
aDSL_VariableDef_isstatic: Property = Property(name="isstatic", type=BooleanType)
aDSL_VariableDef_vartype: Property = Property(name="vartype", type=StringType)
aDSL_VariableDef_name: Property = Property(name="name", type=StringType)
aDSL_VariableDef_istyped: Property = Property(name="istyped", type=BooleanType)
aDSL_VariableDef_isinit: Property = Property(name="isinit", type=BooleanType)
aDSL_VariableDef.attributes={aDSL_VariableDef_isstatic, aDSL_VariableDef_vartype, aDSL_VariableDef_istyped, aDSL_VariableDef_name, aDSL_VariableDef_isinit}

# aDSL_Operator class attributes and methods
aDSL_Operator_opName: Property = Property(name="opName", type=StringType)
aDSL_Operator.attributes={aDSL_Operator_opName}

# aDSL_SharedArrayDef class attributes and methods

# SharedDef class attributes and methods

# aDSL_SharedVarDef class attributes and methods

# aDSL_Statement class attributes and methods

# aDSL_Block class attributes and methods
aDSL_Block_ispar: Property = Property(name="ispar", type=BooleanType)
aDSL_Block.attributes={aDSL_Block_ispar}

# aDSL_AsyncStat class attributes and methods

# aDSL_FinishStat class attributes and methods

# aDSL_AtStat class attributes and methods

# aDSL_AtomicStatement class attributes and methods

# aDSL_WhenStatement class attributes and methods

# aDSL_VarDef class attributes and methods

# aDSL_SharedDef class attributes and methods
aDSL_SharedDef_replicas: Property = Property(name="replicas", type=BooleanType)
aDSL_SharedDef_name: Property = Property(name="name", type=StringType)
aDSL_SharedDef.attributes={aDSL_SharedDef_replicas, aDSL_SharedDef_name}

# aDSL_IntegerNegative class attributes and methods
aDSL_IntegerNegative_isneg: Property = Property(name="isneg", type=BooleanType)
aDSL_IntegerNegative_value: Property = Property(name="value", type=IntegerType)
aDSL_IntegerNegative.attributes={aDSL_IntegerNegative_isneg, aDSL_IntegerNegative_value}

# aDSL_TryCatchStat class attributes and methods
aDSL_TryCatchStat_name: Property = Property(name="name", type=StringType)
aDSL_TryCatchStat.attributes={aDSL_TryCatchStat_name}

# aDSL_For2Statement class attributes and methods

# aDSL_WhileStat class attributes and methods

# aDSL_ForStat class attributes and methods

# aDSL_ReturnStat class attributes and methods

# aDSL_Assignment class attributes and methods

# Expression class attributes and methods

# aDSL_MemberSelection class attributes and methods
aDSL_MemberSelection_ispar: Property = Property(name="ispar", type=BooleanType)
aDSL_MemberSelection_methodinvocation: Property = Property(name="methodinvocation", type=BooleanType)
aDSL_MemberSelection.attributes={aDSL_MemberSelection_methodinvocation, aDSL_MemberSelection_ispar}

# aDSL_IfStat class attributes and methods
aDSL_IfStat_iselse: Property = Property(name="iselse", type=BooleanType)
aDSL_IfStat.attributes={aDSL_IfStat_iselse}

# aDSL_Or class attributes and methods

# aDSL_And class attributes and methods

# aDSL_Equality class attributes and methods
aDSL_Equality_op: Property = Property(name="op", type=StringType)
aDSL_Equality.attributes={aDSL_Equality_op}

# aDSL_Comparison class attributes and methods
aDSL_Comparison_op: Property = Property(name="op", type=StringType)
aDSL_Comparison.attributes={aDSL_Comparison_op}

# aDSL_Plus class attributes and methods

# aDSL_Minus class attributes and methods

# aDSL_MulOrDiv class attributes and methods
aDSL_MulOrDiv_op: Property = Property(name="op", type=StringType)
aDSL_MulOrDiv.attributes={aDSL_MulOrDiv_op}

# aDSL_Not class attributes and methods

# aDSL_StringConstant class attributes and methods
aDSL_StringConstant_value: Property = Property(name="value", type=StringType)
aDSL_StringConstant.attributes={aDSL_StringConstant_value}

# aDSL_IntConstant class attributes and methods

# aDSL_BoolConstant class attributes and methods
aDSL_BoolConstant_value: Property = Property(name="value", type=StringType)
aDSL_BoolConstant.attributes={aDSL_BoolConstant_value}

# aDSL_DeRef class attributes and methods

# aDSL_This class attributes and methods

# aDSL_Null class attributes and methods

# aDSL_Reference class attributes and methods
aDSL_Reference_isarray: Property = Property(name="isarray", type=BooleanType)
aDSL_Reference.attributes={aDSL_Reference_isarray}

# aDSL_New class attributes and methods

# aDSL_Init class attributes and methods

# aDSL_Here class attributes and methods

# Relationships
importElements0: BinaryAssociation = BinaryAssociation(
    name="importElements0",
    ends={
        Property(name="aDSL_AbstractElements", type=aDSL_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Program", type=aDSL_AbstractElements, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xclass1: BinaryAssociation = BinaryAssociation(
    name="xclass1",
    ends={
        Property(name="aDSL_XClass", type=aDSL_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Program2", type=aDSL_XClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members6: BinaryAssociation = BinaryAssociation(
    name="members6",
    ends={
        Property(name="aDSL_Member", type=aDSL_XClass, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_XClass7", type=aDSL_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="aDSL_VariableType", type=aDSL_MainMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_MainMethod", type=aDSL_VariableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body9: BinaryAssociation = BinaryAssociation(
    name="body9",
    ends={
        Property(name="aDSL_Body", type=aDSL_MainMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_MainMethod10", type=aDSL_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression11: BinaryAssociation = BinaryAssociation(
    name="expression11",
    ends={
        Property(name="aDSL_Expression", type=aDSL_PrintInst, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_PrintInst", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params12: BinaryAssociation = BinaryAssociation(
    name="params12",
    ends={
        Property(name="aDSL_Parameter", type=aDSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Method", type=aDSL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="aDSL_VariableType15", type=aDSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Method14", type=aDSL_VariableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body16: BinaryAssociation = BinaryAssociation(
    name="body16",
    ends={
        Property(name="aDSL_Body18", type=aDSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Method17", type=aDSL_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superclass4: BinaryAssociation = BinaryAssociation(
    name="superclass4",
    ends={
        Property(name="aDSL_XClass5", type=aDSL_XClass, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_XClass3", type=aDSL_XClass, multiplicity=Multiplicity(0, 1))
    }
)
params19: BinaryAssociation = BinaryAssociation(
    name="params19",
    ends={
        Property(name="aDSL_Parameter20", type=aDSL_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Operator", type=aDSL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression21: BinaryAssociation = BinaryAssociation(
    name="expression21",
    ends={
        Property(name="aDSL_Expression23", type=aDSL_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Operator22", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params24: BinaryAssociation = BinaryAssociation(
    name="params24",
    ends={
        Property(name="aDSL_Parameter25", type=aDSL_FuncVarDef, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_FuncVarDef", type=aDSL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="aDSL_VariableType28", type=aDSL_FuncVarDef, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_FuncVarDef27", type=aDSL_VariableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body29: BinaryAssociation = BinaryAssociation(
    name="body29",
    ends={
        Property(name="aDSL_Body31", type=aDSL_FuncVarDef, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_FuncVarDef30", type=aDSL_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type32: BinaryAssociation = BinaryAssociation(
    name="type32",
    ends={
        Property(name="aDSL_VariableType33", type=aDSL_VariableDef, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_VariableDef", type=aDSL_VariableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression37: BinaryAssociation = BinaryAssociation(
    name="expression37",
    ends={
        Property(name="aDSL_VariableDef38", type=aDSL_SharedArrayDef, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_SharedArrayDef", type=aDSL_VariableDef, multiplicity=Multiplicity(0, 1))
    }
)
expression39: BinaryAssociation = BinaryAssociation(
    name="expression39",
    ends={
        Property(name="aDSL_Expression40", type=aDSL_SharedVarDef, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_SharedVarDef", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type41: BinaryAssociation = BinaryAssociation(
    name="type41",
    ends={
        Property(name="aDSL_VariableType43", type=aDSL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Parameter42", type=aDSL_VariableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements44: BinaryAssociation = BinaryAssociation(
    name="statements44",
    ends={
        Property(name="aDSL_Statement", type=aDSL_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Body45", type=aDSL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements46: BinaryAssociation = BinaryAssociation(
    name="statements46",
    ends={
        Property(name="aDSL_Statement47", type=aDSL_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Block", type=aDSL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type48: BinaryAssociation = BinaryAssociation(
    name="type48",
    ends={
        Property(name="aDSL_XClass50", type=aDSL_VariableType, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_VariableType49", type=aDSL_XClass, multiplicity=Multiplicity(0, 1))
    }
)
expression34: BinaryAssociation = BinaryAssociation(
    name="expression34",
    ends={
        Property(name="aDSL_Expression36", type=aDSL_VariableDef, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_VariableDef35", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerType52: BinaryAssociation = BinaryAssociation(
    name="innerType52",
    ends={
        Property(name="aDSL_VariableType53", type=aDSL_VariableType, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_VariableType51", type=aDSL_VariableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body54: BinaryAssociation = BinaryAssociation(
    name="body54",
    ends={
        Property(name="aDSL_Block55", type=aDSL_AsyncStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_AsyncStat", type=aDSL_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body56: BinaryAssociation = BinaryAssociation(
    name="body56",
    ends={
        Property(name="aDSL_Block57", type=aDSL_FinishStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_FinishStat", type=aDSL_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp58: BinaryAssociation = BinaryAssociation(
    name="exp58",
    ends={
        Property(name="aDSL_Expression59", type=aDSL_AtStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_AtStat", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body60: BinaryAssociation = BinaryAssociation(
    name="body60",
    ends={
        Property(name="aDSL_Block62", type=aDSL_AtStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_AtStat61", type=aDSL_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement63: BinaryAssociation = BinaryAssociation(
    name="statement63",
    ends={
        Property(name="aDSL_Statement64", type=aDSL_AtomicStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_AtomicStatement", type=aDSL_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression65: BinaryAssociation = BinaryAssociation(
    name="expression65",
    ends={
        Property(name="aDSL_Expression66", type=aDSL_WhenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_WhenStatement", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
par70: BinaryAssociation = BinaryAssociation(
    name="par70",
    ends={
        Property(name="aDSL_Parameter71", type=aDSL_For2Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_For2Statement", type=aDSL_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
data72: BinaryAssociation = BinaryAssociation(
    name="data72",
    ends={
        Property(name="aDSL_Expression74", type=aDSL_For2Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_For2Statement73", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body75: BinaryAssociation = BinaryAssociation(
    name="body75",
    ends={
        Property(name="aDSL_Block77", type=aDSL_For2Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_For2Statement76", type=aDSL_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type78: BinaryAssociation = BinaryAssociation(
    name="type78",
    ends={
        Property(name="aDSL_VariableType79", type=aDSL_SharedDef, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_SharedDef", type=aDSL_VariableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sym80: BinaryAssociation = BinaryAssociation(
    name="sym80",
    ends={
        Property(name="aDSL_VarDef", type=aDSL_SharedDef, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_SharedDef81", type=aDSL_VarDef, multiplicity=Multiplicity(0, 1))
    }
)
statement67: BinaryAssociation = BinaryAssociation(
    name="statement67",
    ends={
        Property(name="aDSL_Statement69", type=aDSL_WhenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_WhenStatement68", type=aDSL_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyCatch84: BinaryAssociation = BinaryAssociation(
    name="bodyCatch84",
    ends={
        Property(name="aDSL_Body86", type=aDSL_TryCatchStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_TryCatchStat85", type=aDSL_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression87: BinaryAssociation = BinaryAssociation(
    name="expression87",
    ends={
        Property(name="aDSL_Expression88", type=aDSL_WhileStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_WhileStat", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body89: BinaryAssociation = BinaryAssociation(
    name="body89",
    ends={
        Property(name="aDSL_Body91", type=aDSL_WhileStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_WhileStat90", type=aDSL_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
temp92: BinaryAssociation = BinaryAssociation(
    name="temp92",
    ends={
        Property(name="aDSL_VariableDef93", type=aDSL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_ForStat", type=aDSL_VariableDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition94: BinaryAssociation = BinaryAssociation(
    name="condition94",
    ends={
        Property(name="aDSL_Expression96", type=aDSL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_ForStat95", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalexp97: BinaryAssociation = BinaryAssociation(
    name="finalexp97",
    ends={
        Property(name="aDSL_Expression99", type=aDSL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_ForStat98", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body100: BinaryAssociation = BinaryAssociation(
    name="body100",
    ends={
        Property(name="aDSL_Block102", type=aDSL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_ForStat101", type=aDSL_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression103: BinaryAssociation = BinaryAssociation(
    name="expression103",
    ends={
        Property(name="aDSL_Expression104", type=aDSL_ReturnStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_ReturnStat", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyTry82: BinaryAssociation = BinaryAssociation(
    name="bodyTry82",
    ends={
        Property(name="aDSL_Body83", type=aDSL_TryCatchStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_TryCatchStat", type=aDSL_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression105: BinaryAssociation = BinaryAssociation(
    name="expression105",
    ends={
        Property(name="aDSL_IfStat", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="aDSL_Expression106", type=aDSL_IfStat, multiplicity=Multiplicity(1, 1))
    }
)
thenBlock107: BinaryAssociation = BinaryAssociation(
    name="thenBlock107",
    ends={
        Property(name="aDSL_Block109", type=aDSL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_IfStat108", type=aDSL_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock110: BinaryAssociation = BinaryAssociation(
    name="elseBlock110",
    ends={
        Property(name="aDSL_Block112", type=aDSL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_IfStat111", type=aDSL_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left113: BinaryAssociation = BinaryAssociation(
    name="left113",
    ends={
        Property(name="aDSL_Expression114", type=aDSL_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Assignment", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right115: BinaryAssociation = BinaryAssociation(
    name="right115",
    ends={
        Property(name="aDSL_Expression117", type=aDSL_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Assignment116", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver118: BinaryAssociation = BinaryAssociation(
    name="receiver118",
    ends={
        Property(name="aDSL_Expression119", type=aDSL_MemberSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_MemberSelection", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member120: BinaryAssociation = BinaryAssociation(
    name="member120",
    ends={
        Property(name="aDSL_Member122", type=aDSL_MemberSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_MemberSelection121", type=aDSL_Member, multiplicity=Multiplicity(0, 1))
    }
)
par123: BinaryAssociation = BinaryAssociation(
    name="par123",
    ends={
        Property(name="aDSL_XClass125", type=aDSL_MemberSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_MemberSelection124", type=aDSL_XClass, multiplicity=Multiplicity(0, 1))
    }
)
left129: BinaryAssociation = BinaryAssociation(
    name="left129",
    ends={
        Property(name="aDSL_Expression130", type=aDSL_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Or", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right131: BinaryAssociation = BinaryAssociation(
    name="right131",
    ends={
        Property(name="aDSL_Expression133", type=aDSL_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Or132", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left134: BinaryAssociation = BinaryAssociation(
    name="left134",
    ends={
        Property(name="aDSL_Expression135", type=aDSL_And, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_And", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right136: BinaryAssociation = BinaryAssociation(
    name="right136",
    ends={
        Property(name="aDSL_Expression138", type=aDSL_And, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_And137", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left139: BinaryAssociation = BinaryAssociation(
    name="left139",
    ends={
        Property(name="aDSL_Expression140", type=aDSL_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Equality", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args126: BinaryAssociation = BinaryAssociation(
    name="args126",
    ends={
        Property(name="aDSL_Expression128", type=aDSL_MemberSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_MemberSelection127", type=aDSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left144: BinaryAssociation = BinaryAssociation(
    name="left144",
    ends={
        Property(name="aDSL_Expression145", type=aDSL_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Comparison", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right146: BinaryAssociation = BinaryAssociation(
    name="right146",
    ends={
        Property(name="aDSL_Expression148", type=aDSL_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Comparison147", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left149: BinaryAssociation = BinaryAssociation(
    name="left149",
    ends={
        Property(name="aDSL_Expression150", type=aDSL_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Plus", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right151: BinaryAssociation = BinaryAssociation(
    name="right151",
    ends={
        Property(name="aDSL_Expression153", type=aDSL_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Plus152", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left154: BinaryAssociation = BinaryAssociation(
    name="left154",
    ends={
        Property(name="aDSL_Expression155", type=aDSL_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Minus", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right156: BinaryAssociation = BinaryAssociation(
    name="right156",
    ends={
        Property(name="aDSL_Expression158", type=aDSL_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Minus157", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right141: BinaryAssociation = BinaryAssociation(
    name="right141",
    ends={
        Property(name="aDSL_Expression143", type=aDSL_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Equality142", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right161: BinaryAssociation = BinaryAssociation(
    name="right161",
    ends={
        Property(name="aDSL_Expression163", type=aDSL_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_MulOrDiv162", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression164: BinaryAssociation = BinaryAssociation(
    name="expression164",
    ends={
        Property(name="aDSL_Expression165", type=aDSL_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Not", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value166: BinaryAssociation = BinaryAssociation(
    name="value166",
    ends={
        Property(name="aDSL_IntegerNegative", type=aDSL_IntConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_IntConstant", type=aDSL_IntegerNegative, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref167: BinaryAssociation = BinaryAssociation(
    name="ref167",
    ends={
        Property(name="aDSL_VarDef168", type=aDSL_DeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_DeRef", type=aDSL_VarDef, multiplicity=Multiplicity(0, 1))
    }
)
left159: BinaryAssociation = BinaryAssociation(
    name="left159",
    ends={
        Property(name="aDSL_Expression160", type=aDSL_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_MulOrDiv", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base169: BinaryAssociation = BinaryAssociation(
    name="base169",
    ends={
        Property(name="aDSL_VarDef170", type=aDSL_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Reference", type=aDSL_VarDef, multiplicity=Multiplicity(0, 1))
    }
)
params171: BinaryAssociation = BinaryAssociation(
    name="params171",
    ends={
        Property(name="aDSL_Expression173", type=aDSL_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Reference172", type=aDSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type174: BinaryAssociation = BinaryAssociation(
    name="type174",
    ends={
        Property(name="aDSL_VariableType175", type=aDSL_New, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_New", type=aDSL_VariableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args176: BinaryAssociation = BinaryAssociation(
    name="args176",
    ends={
        Property(name="aDSL_Expression178", type=aDSL_New, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_New177", type=aDSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type179: BinaryAssociation = BinaryAssociation(
    name="type179",
    ends={
        Property(name="aDSL_VariableType180", type=aDSL_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Init", type=aDSL_VariableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression181: BinaryAssociation = BinaryAssociation(
    name="expression181",
    ends={
        Property(name="aDSL_Expression183", type=aDSL_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="aDSL_Init182", type=aDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_aDSL_XClass_VarDef = Generalization(general=VarDef, specific=aDSL_XClass)
gen_aDSL_MainMethod_Member = Generalization(general=Member, specific=aDSL_MainMethod)
gen_aDSL_PrintInst_Member = Generalization(general=Member, specific=aDSL_PrintInst)
gen_aDSL_PrintInst_Statement = Generalization(general=Statement, specific=aDSL_PrintInst)
gen_aDSL_Method_Member = Generalization(general=Member, specific=aDSL_Method)
gen_aDSL_FuncVarDef_Member = Generalization(general=Member, specific=aDSL_FuncVarDef)
gen_aDSL_FuncVarDef_Statement = Generalization(general=Statement, specific=aDSL_FuncVarDef)
gen_aDSL_FuncVarDef_VarDef = Generalization(general=VarDef, specific=aDSL_FuncVarDef)
gen_aDSL_VariableDef_Member = Generalization(general=Member, specific=aDSL_VariableDef)
gen_aDSL_VariableDef_Statement = Generalization(general=Statement, specific=aDSL_VariableDef)
gen_aDSL_VariableDef_VarDef = Generalization(general=VarDef, specific=aDSL_VariableDef)
gen_aDSL_Operator_Member = Generalization(general=Member, specific=aDSL_Operator)
gen_aDSL_SharedArrayDef_SharedDef = Generalization(general=SharedDef, specific=aDSL_SharedArrayDef)
gen_aDSL_SharedVarDef_SharedDef = Generalization(general=SharedDef, specific=aDSL_SharedVarDef)
gen_aDSL_Parameter_VarDef = Generalization(general=VarDef, specific=aDSL_Parameter)
gen_aDSL_VariableType_VarDef = Generalization(general=VarDef, specific=aDSL_VariableType)
gen_aDSL_AsyncStat_Statement = Generalization(general=Statement, specific=aDSL_AsyncStat)
gen_aDSL_FinishStat_Statement = Generalization(general=Statement, specific=aDSL_FinishStat)
gen_aDSL_AtStat_Statement = Generalization(general=Statement, specific=aDSL_AtStat)
gen_aDSL_AtomicStatement_Statement = Generalization(general=Statement, specific=aDSL_AtomicStatement)
gen_aDSL_WhenStatement_Statement = Generalization(general=Statement, specific=aDSL_WhenStatement)
gen_aDSL_SharedDef_Member = Generalization(general=Member, specific=aDSL_SharedDef)
gen_aDSL_SharedDef_Statement = Generalization(general=Statement, specific=aDSL_SharedDef)
gen_aDSL_SharedDef_VarDef = Generalization(general=VarDef, specific=aDSL_SharedDef)
gen_aDSL_Expression_Statement = Generalization(general=Statement, specific=aDSL_Expression)
gen_aDSL_TryCatchStat_Statement = Generalization(general=Statement, specific=aDSL_TryCatchStat)
gen_aDSL_For2Statement_Statement = Generalization(general=Statement, specific=aDSL_For2Statement)
gen_aDSL_WhileStat_Statement = Generalization(general=Statement, specific=aDSL_WhileStat)
gen_aDSL_ForStat_Statement = Generalization(general=Statement, specific=aDSL_ForStat)
gen_aDSL_ReturnStat_Statement = Generalization(general=Statement, specific=aDSL_ReturnStat)
gen_aDSL_Assignment_Expression = Generalization(general=Expression, specific=aDSL_Assignment)
gen_aDSL_MemberSelection_Expression = Generalization(general=Expression, specific=aDSL_MemberSelection)
gen_aDSL_IfStat_Statement = Generalization(general=Statement, specific=aDSL_IfStat)
gen_aDSL_Or_Expression = Generalization(general=Expression, specific=aDSL_Or)
gen_aDSL_And_Expression = Generalization(general=Expression, specific=aDSL_And)
gen_aDSL_Equality_Expression = Generalization(general=Expression, specific=aDSL_Equality)
gen_aDSL_Comparison_Expression = Generalization(general=Expression, specific=aDSL_Comparison)
gen_aDSL_Plus_Expression = Generalization(general=Expression, specific=aDSL_Plus)
gen_aDSL_Minus_Expression = Generalization(general=Expression, specific=aDSL_Minus)
gen_aDSL_MulOrDiv_Expression = Generalization(general=Expression, specific=aDSL_MulOrDiv)
gen_aDSL_Not_Expression = Generalization(general=Expression, specific=aDSL_Not)
gen_aDSL_StringConstant_Expression = Generalization(general=Expression, specific=aDSL_StringConstant)
gen_aDSL_IntConstant_Expression = Generalization(general=Expression, specific=aDSL_IntConstant)
gen_aDSL_BoolConstant_Expression = Generalization(general=Expression, specific=aDSL_BoolConstant)
gen_aDSL_DeRef_Expression = Generalization(general=Expression, specific=aDSL_DeRef)
gen_aDSL_This_Expression = Generalization(general=Expression, specific=aDSL_This)
gen_aDSL_Reference_Expression = Generalization(general=Expression, specific=aDSL_Reference)
gen_aDSL_New_Expression = Generalization(general=Expression, specific=aDSL_New)
gen_aDSL_Init_Expression = Generalization(general=Expression, specific=aDSL_Init)
gen_aDSL_Null_Expression = Generalization(general=Expression, specific=aDSL_Null)
gen_aDSL_Here_Expression = Generalization(general=Expression, specific=aDSL_Here)

# Domain Model
domain_model = DomainModel(
    name="aDSL",
    types={aDSL_Program, aDSL_AbstractElements, aDSL_XClass, VarDef, aDSL_MainMethod, Member, aDSL_VariableType, aDSL_Body, aDSL_PrintInst, Statement, aDSL_Expression, aDSL_Method, aDSL_Parameter, aDSL_Member, aDSL_FuncVarDef, aDSL_VariableDef, aDSL_Operator, aDSL_SharedArrayDef, SharedDef, aDSL_SharedVarDef, aDSL_Statement, aDSL_Block, aDSL_AsyncStat, aDSL_FinishStat, aDSL_AtStat, aDSL_AtomicStatement, aDSL_WhenStatement, aDSL_VarDef, aDSL_SharedDef, aDSL_IntegerNegative, aDSL_TryCatchStat, aDSL_For2Statement, aDSL_WhileStat, aDSL_ForStat, aDSL_ReturnStat, aDSL_Assignment, Expression, aDSL_MemberSelection, aDSL_IfStat, aDSL_Or, aDSL_And, aDSL_Equality, aDSL_Comparison, aDSL_Plus, aDSL_Minus, aDSL_MulOrDiv, aDSL_Not, aDSL_StringConstant, aDSL_IntConstant, aDSL_BoolConstant, aDSL_DeRef, aDSL_This, aDSL_Null, aDSL_Reference, aDSL_New, aDSL_Init, aDSL_Here},
    associations={importElements0, xclass1, members6, type8, body9, expression11, params12, type13, body16, superclass4, params19, expression21, params24, type26, body29, type32, expression37, expression39, type41, statements44, statements46, type48, expression34, innerType52, body54, body56, exp58, body60, statement63, expression65, par70, data72, body75, type78, sym80, statement67, bodyCatch84, expression87, body89, temp92, condition94, finalexp97, body100, expression103, bodyTry82, expression105, thenBlock107, elseBlock110, left113, right115, receiver118, member120, par123, left129, right131, left134, right136, left139, args126, left144, right146, left149, right151, left154, right156, right141, right161, expression164, value166, ref167, left159, base169, params171, type174, args176, type179, expression181},
    generalizations={gen_aDSL_XClass_VarDef, gen_aDSL_MainMethod_Member, gen_aDSL_PrintInst_Member, gen_aDSL_PrintInst_Statement, gen_aDSL_Method_Member, gen_aDSL_FuncVarDef_Member, gen_aDSL_FuncVarDef_Statement, gen_aDSL_FuncVarDef_VarDef, gen_aDSL_VariableDef_Member, gen_aDSL_VariableDef_Statement, gen_aDSL_VariableDef_VarDef, gen_aDSL_Operator_Member, gen_aDSL_SharedArrayDef_SharedDef, gen_aDSL_SharedVarDef_SharedDef, gen_aDSL_Parameter_VarDef, gen_aDSL_VariableType_VarDef, gen_aDSL_AsyncStat_Statement, gen_aDSL_FinishStat_Statement, gen_aDSL_AtStat_Statement, gen_aDSL_AtomicStatement_Statement, gen_aDSL_WhenStatement_Statement, gen_aDSL_SharedDef_Member, gen_aDSL_SharedDef_Statement, gen_aDSL_SharedDef_VarDef, gen_aDSL_Expression_Statement, gen_aDSL_TryCatchStat_Statement, gen_aDSL_For2Statement_Statement, gen_aDSL_WhileStat_Statement, gen_aDSL_ForStat_Statement, gen_aDSL_ReturnStat_Statement, gen_aDSL_Assignment_Expression, gen_aDSL_MemberSelection_Expression, gen_aDSL_IfStat_Statement, gen_aDSL_Or_Expression, gen_aDSL_And_Expression, gen_aDSL_Equality_Expression, gen_aDSL_Comparison_Expression, gen_aDSL_Plus_Expression, gen_aDSL_Minus_Expression, gen_aDSL_MulOrDiv_Expression, gen_aDSL_Not_Expression, gen_aDSL_StringConstant_Expression, gen_aDSL_IntConstant_Expression, gen_aDSL_BoolConstant_Expression, gen_aDSL_DeRef_Expression, gen_aDSL_This_Expression, gen_aDSL_Reference_Expression, gen_aDSL_New_Expression, gen_aDSL_Init_Expression, gen_aDSL_Null_Expression, gen_aDSL_Here_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)