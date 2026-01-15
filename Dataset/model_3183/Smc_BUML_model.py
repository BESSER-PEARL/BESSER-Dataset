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

# Enumerations
BlockType: Enumeration = Enumeration(
    name="BlockType",
    literals={
            EnumerationLiteral(name="INSERT"),
			EnumerationLiteral(name="COMP"),
			EnumerationLiteral(name="SEARCH"),
			EnumerationLiteral(name="ANONYMIZATION"),
			EnumerationLiteral(name="ACCESS"),
			EnumerationLiteral(name="PERMISSION")
    }
)

BasicType: Enumeration = Enumeration(
    name="BasicType",
    literals={
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="ENCRYPTED")
    }
)

SecType: Enumeration = Enumeration(
    name="SecType",
    literals={
            EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PUBLIC")
    }
)

# Classes
smc_Smc = Class(name="smc::Smc")
smc_BlockSMC = Class(name="smc::BlockSMC")
smc_MainSMC = Class(name="smc::MainSMC")
smc_While = Class(name="smc::While")
smc_Command = Class(name="smc::Command")
smc_ParamDecl = Class(name="smc::ParamDecl")
Command = Class(name="Command")
smc_InvocationVoid = Class(name="smc::InvocationVoid")
smc_Invocation = Class(name="smc::Invocation")
smc_Print = Class(name="smc::Print")
smc_Expression = Class(name="smc::Expression")
smc_IfThenElse = Class(name="smc::IfThenElse")
smc_VariableDecl = Class(name="smc::VariableDecl")
smc_AbstractAssignment = Class(name="smc::AbstractAssignment")
smc_Tuple = Class(name="smc::Tuple")
Expression = Class(name="Expression")
smc_VariableAssignment = Class(name="smc::VariableAssignment")
smc_Download = Class(name="smc::Download")
AbstractAssignment = Class(name="AbstractAssignment")
smc_Database = Class(name="smc::Database")
Download = Class(name="Download")
smc_Client = Class(name="smc::Client")
smc_Multiplication = Class(name="smc::Multiplication")
Computation = Class(name="Computation")
smc_List = Class(name="smc::List")
smc_Dict = Class(name="smc::Dict")
smc_Functions = Class(name="smc::Functions")
smc_Computation = Class(name="smc::Computation")
Functions = Class(name="Functions")
smc_BellLapadula = Class(name="smc::BellLapadula")
AccessControl = Class(name="AccessControl")
smc_Median = Class(name="smc::Median")
smc_WeightedAvg = Class(name="smc::WeightedAvg")
smc_Average = Class(name="smc::Average")
smc_Count = Class(name="smc::Count")
smc_AccessControl = Class(name="smc::AccessControl")
smc_Covered = Class(name="smc::Covered")
smc_Search = Class(name="smc::Search")
smc_BloomFilter = Class(name="smc::BloomFilter")
smc_Or = Class(name="smc::Or")
smc_CheckTable = Class(name="smc::CheckTable")
smc_AddValues = Class(name="smc::AddValues")
smc_CreateTable = Class(name="smc::CreateTable")
smc_Return = Class(name="smc::Return")
smc_Block = Class(name="smc::Block")
smc_PlusOrMinus = Class(name="smc::PlusOrMinus")
smc_And = Class(name="smc::And")
smc_Equality = Class(name="smc::Equality")
smc_Comparison = Class(name="smc::Comparison")
smc_Not = Class(name="smc::Not")
smc_MulOrDiv = Class(name="smc::MulOrDiv")
smc_VariableRef = Class(name="smc::VariableRef")
smc_IntLiteral = Class(name="smc::IntLiteral")
smc_DoubleLiteral = Class(name="smc::DoubleLiteral")
smc_BooleanLiteral = Class(name="smc::BooleanLiteral")
smc_StringLiteral = Class(name="smc::StringLiteral")
smc_DateLiteral = Class(name="smc::DateLiteral")
smc_TimeLiteral = Class(name="smc::TimeLiteral")

# smc_Smc class attributes and methods

# smc_BlockSMC class attributes and methods
smc_BlockSMC_type: Property = Property(name="type", type=StringType)
smc_BlockSMC_name: Property = Property(name="name", type=StringType)
smc_BlockSMC.attributes={smc_BlockSMC_name, smc_BlockSMC_type}

# smc_MainSMC class attributes and methods

# smc_While class attributes and methods

# smc_Command class attributes and methods

# smc_ParamDecl class attributes and methods
smc_ParamDecl_name: Property = Property(name="name", type=StringType)
smc_ParamDecl_stype: Property = Property(name="stype", type=StringType)
smc_ParamDecl_btype: Property = Property(name="btype", type=StringType)
smc_ParamDecl_parName: Property = Property(name="parName", type=StringType)
smc_ParamDecl.attributes={smc_ParamDecl_btype, smc_ParamDecl_stype, smc_ParamDecl_name, smc_ParamDecl_parName}

# Command class attributes and methods

# smc_InvocationVoid class attributes and methods

# smc_Invocation class attributes and methods

# smc_Print class attributes and methods

# smc_Expression class attributes and methods

# smc_IfThenElse class attributes and methods

# smc_VariableDecl class attributes and methods
smc_VariableDecl_visibility: Property = Property(name="visibility", type=StringType)
smc_VariableDecl_type: Property = Property(name="type", type=StringType)
smc_VariableDecl_array: Property = Property(name="array", type=BooleanType)
smc_VariableDecl_length: Property = Property(name="length", type=IntegerType)
smc_VariableDecl_name: Property = Property(name="name", type=StringType)
smc_VariableDecl.attributes={smc_VariableDecl_name, smc_VariableDecl_visibility, smc_VariableDecl_array, smc_VariableDecl_length, smc_VariableDecl_type}

# smc_AbstractAssignment class attributes and methods

# smc_Tuple class attributes and methods

# Expression class attributes and methods

# smc_VariableAssignment class attributes and methods

# smc_Download class attributes and methods

# AbstractAssignment class attributes and methods

# smc_Database class attributes and methods
smc_Database_clm: Property = Property(name="clm", type=StringType)
smc_Database.attributes={smc_Database_clm}

# Download class attributes and methods

# smc_Client class attributes and methods
smc_Client_arg: Property = Property(name="arg", type=StringType)
smc_Client.attributes={smc_Client_arg}

# smc_Multiplication class attributes and methods

# Computation class attributes and methods

# smc_List class attributes and methods

# smc_Dict class attributes and methods

# smc_Functions class attributes and methods

# smc_Computation class attributes and methods

# Functions class attributes and methods

# smc_BellLapadula class attributes and methods
smc_BellLapadula_mode: Property = Property(name="mode", type=StringType)
smc_BellLapadula.attributes={smc_BellLapadula_mode}

# AccessControl class attributes and methods

# smc_Median class attributes and methods

# smc_WeightedAvg class attributes and methods

# smc_Average class attributes and methods

# smc_Count class attributes and methods

# smc_AccessControl class attributes and methods

# smc_Covered class attributes and methods

# smc_Search class attributes and methods
smc_Search_column: Property = Property(name="column", type=StringType)
smc_Search.attributes={smc_Search_column}

# smc_BloomFilter class attributes and methods

# smc_Or class attributes and methods

# smc_CheckTable class attributes and methods

# smc_AddValues class attributes and methods

# smc_CreateTable class attributes and methods

# smc_Return class attributes and methods

# smc_Block class attributes and methods

# smc_PlusOrMinus class attributes and methods
smc_PlusOrMinus_op: Property = Property(name="op", type=StringType)
smc_PlusOrMinus.attributes={smc_PlusOrMinus_op}

# smc_And class attributes and methods

# smc_Equality class attributes and methods
smc_Equality_op: Property = Property(name="op", type=StringType)
smc_Equality.attributes={smc_Equality_op}

# smc_Comparison class attributes and methods
smc_Comparison_op: Property = Property(name="op", type=StringType)
smc_Comparison.attributes={smc_Comparison_op}

# smc_Not class attributes and methods

# smc_MulOrDiv class attributes and methods
smc_MulOrDiv_op: Property = Property(name="op", type=StringType)
smc_MulOrDiv.attributes={smc_MulOrDiv_op}

# smc_VariableRef class attributes and methods

# smc_IntLiteral class attributes and methods
smc_IntLiteral_value: Property = Property(name="value", type=IntegerType)
smc_IntLiteral.attributes={smc_IntLiteral_value}

# smc_DoubleLiteral class attributes and methods
smc_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
smc_DoubleLiteral.attributes={smc_DoubleLiteral_value}

# smc_BooleanLiteral class attributes and methods
smc_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
smc_BooleanLiteral.attributes={smc_BooleanLiteral_value}

# smc_StringLiteral class attributes and methods
smc_StringLiteral_value: Property = Property(name="value", type=StringType)
smc_StringLiteral.attributes={smc_StringLiteral_value}

# smc_DateLiteral class attributes and methods
smc_DateLiteral_value: Property = Property(name="value", type=StringType)
smc_DateLiteral.attributes={smc_DateLiteral_value}

# smc_TimeLiteral class attributes and methods
smc_TimeLiteral_value: Property = Property(name="value", type=StringType)
smc_TimeLiteral.attributes={smc_TimeLiteral_value}

# Relationships
blocks0: BinaryAssociation = BinaryAssociation(
    name="blocks0",
    ends={
        Property(name="smc_BlockSMC", type=smc_Smc, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Smc", type=smc_BlockSMC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
main1: BinaryAssociation = BinaryAssociation(
    name="main1",
    ends={
        Property(name="smc_MainSMC", type=smc_Smc, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Smc2", type=smc_MainSMC, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition7: BinaryAssociation = BinaryAssociation(
    name="condition7",
    ends={
        Property(name="smc_Expression8", type=smc_While, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_While", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands3: BinaryAssociation = BinaryAssociation(
    name="commands3",
    ends={
        Property(name="smc_Command", type=smc_MainSMC, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_MainSMC4", type=smc_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
call5: BinaryAssociation = BinaryAssociation(
    name="call5",
    ends={
        Property(name="smc_Invocation", type=smc_InvocationVoid, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_InvocationVoid", type=smc_Invocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value6: BinaryAssociation = BinaryAssociation(
    name="value6",
    ends={
        Property(name="smc_Expression", type=smc_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Print", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body9: BinaryAssociation = BinaryAssociation(
    name="body9",
    ends={
        Property(name="smc_Command11", type=smc_While, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_While10", type=smc_Command, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition12: BinaryAssociation = BinaryAssociation(
    name="condition12",
    ends={
        Property(name="smc_Expression13", type=smc_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_IfThenElse", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBrach14: BinaryAssociation = BinaryAssociation(
    name="thenBrach14",
    ends={
        Property(name="smc_Command16", type=smc_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_IfThenElse15", type=smc_Command, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBranch17: BinaryAssociation = BinaryAssociation(
    name="elseBranch17",
    ends={
        Property(name="smc_Command19", type=smc_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_IfThenElse18", type=smc_Command, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
option20: BinaryAssociation = BinaryAssociation(
    name="option20",
    ends={
        Property(name="smc_AbstractAssignment", type=smc_VariableDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_VariableDecl", type=smc_AbstractAssignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var21: BinaryAssociation = BinaryAssociation(
    name="var21",
    ends={
        Property(name="smc_VariableDecl22", type=smc_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_VariableAssignment", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
option23: BinaryAssociation = BinaryAssociation(
    name="option23",
    ends={
        Property(name="smc_AbstractAssignment25", type=smc_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_VariableAssignment24", type=smc_AbstractAssignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tbl26: BinaryAssociation = BinaryAssociation(
    name="tbl26",
    ends={
        Property(name="smc_Expression27", type=smc_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Database", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg128: BinaryAssociation = BinaryAssociation(
    name="arg128",
    ends={
        Property(name="smc_Expression29", type=smc_Tuple, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Tuple", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
x45: BinaryAssociation = BinaryAssociation(
    name="x45",
    ends={
        Property(name="smc_VariableDecl46", type=smc_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Multiplication", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
arg230: BinaryAssociation = BinaryAssociation(
    name="arg230",
    ends={
        Property(name="smc_Expression32", type=smc_Tuple, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Tuple31", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args33: BinaryAssociation = BinaryAssociation(
    name="args33",
    ends={
        Property(name="smc_Expression34", type=smc_List, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_List", type=smc_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key35: BinaryAssociation = BinaryAssociation(
    name="key35",
    ends={
        Property(name="smc_Expression36", type=smc_Dict, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Dict", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value37: BinaryAssociation = BinaryAssociation(
    name="value37",
    ends={
        Property(name="smc_List39", type=smc_Dict, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Dict38", type=smc_List, multiplicity=Multiplicity(0, 1))
    }
)
blockName40: BinaryAssociation = BinaryAssociation(
    name="blockName40",
    ends={
        Property(name="smc_BlockSMC42", type=smc_Invocation, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Invocation41", type=smc_BlockSMC, multiplicity=Multiplicity(0, 1))
    }
)
funcName43: BinaryAssociation = BinaryAssociation(
    name="funcName43",
    ends={
        Property(name="smc_Functions", type=smc_Invocation, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Invocation44", type=smc_Functions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
v_lvl63: BinaryAssociation = BinaryAssociation(
    name="v_lvl63",
    ends={
        Property(name="smc_VariableDecl65", type=smc_AccessControl, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_AccessControl64", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
y47: BinaryAssociation = BinaryAssociation(
    name="y47",
    ends={
        Property(name="smc_VariableDecl49", type=smc_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Multiplication48", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
array50: BinaryAssociation = BinaryAssociation(
    name="array50",
    ends={
        Property(name="smc_VariableDecl51", type=smc_Median, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Median", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
weights52: BinaryAssociation = BinaryAssociation(
    name="weights52",
    ends={
        Property(name="smc_VariableDecl53", type=smc_WeightedAvg, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_WeightedAvg", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
elems54: BinaryAssociation = BinaryAssociation(
    name="elems54",
    ends={
        Property(name="smc_VariableDecl56", type=smc_WeightedAvg, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_WeightedAvg55", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
array57: BinaryAssociation = BinaryAssociation(
    name="array57",
    ends={
        Property(name="smc_VariableDecl58", type=smc_Average, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Average", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
array59: BinaryAssociation = BinaryAssociation(
    name="array59",
    ends={
        Property(name="smc_VariableDecl60", type=smc_Count, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Count", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
c_lvls61: BinaryAssociation = BinaryAssociation(
    name="c_lvls61",
    ends={
        Property(name="smc_VariableDecl62", type=smc_AccessControl, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_AccessControl", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
pre78: BinaryAssociation = BinaryAssociation(
    name="pre78",
    ends={
        Property(name="smc_BloomFilter", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1)),
        Property(name="smc_VariableDecl79", type=smc_BloomFilter, multiplicity=Multiplicity(1, 1))
    }
)
post80: BinaryAssociation = BinaryAssociation(
    name="post80",
    ends={
        Property(name="smc_VariableDecl82", type=smc_BloomFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_BloomFilter81", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
cur66: BinaryAssociation = BinaryAssociation(
    name="cur66",
    ends={
        Property(name="smc_VariableDecl67", type=smc_BellLapadula, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_BellLapadula", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
match68: BinaryAssociation = BinaryAssociation(
    name="match68",
    ends={
        Property(name="smc_VariableDecl69", type=smc_Covered, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Covered", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
covered70: BinaryAssociation = BinaryAssociation(
    name="covered70",
    ends={
        Property(name="smc_VariableDecl72", type=smc_Covered, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Covered71", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
tblname73: BinaryAssociation = BinaryAssociation(
    name="tblname73",
    ends={
        Property(name="smc_VariableDecl74", type=smc_Search, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Search", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
keyword75: BinaryAssociation = BinaryAssociation(
    name="keyword75",
    ends={
        Property(name="smc_VariableDecl77", type=smc_Search, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Search76", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
commands94: BinaryAssociation = BinaryAssociation(
    name="commands94",
    ends={
        Property(name="smc_Command95", type=smc_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Block", type=smc_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tblname83: BinaryAssociation = BinaryAssociation(
    name="tblname83",
    ends={
        Property(name="smc_VariableDecl84", type=smc_CheckTable, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_CheckTable", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
tblname85: BinaryAssociation = BinaryAssociation(
    name="tblname85",
    ends={
        Property(name="smc_VariableDecl86", type=smc_AddValues, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_AddValues", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
args87: BinaryAssociation = BinaryAssociation(
    name="args87",
    ends={
        Property(name="smc_VariableDecl89", type=smc_AddValues, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_AddValues88", type=smc_VariableDecl, multiplicity=Multiplicity(0, 9999))
    }
)
tblname90: BinaryAssociation = BinaryAssociation(
    name="tblname90",
    ends={
        Property(name="smc_VariableDecl91", type=smc_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_CreateTable", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)
params92: BinaryAssociation = BinaryAssociation(
    name="params92",
    ends={
        Property(name="smc_ParamDecl", type=smc_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_CreateTable93", type=smc_ParamDecl, multiplicity=Multiplicity(0, 9999))
    }
)
right113: BinaryAssociation = BinaryAssociation(
    name="right113",
    ends={
        Property(name="smc_Expression115", type=smc_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Comparison114", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left96: BinaryAssociation = BinaryAssociation(
    name="left96",
    ends={
        Property(name="smc_Expression97", type=smc_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Or", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right98: BinaryAssociation = BinaryAssociation(
    name="right98",
    ends={
        Property(name="smc_Expression100", type=smc_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Or99", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left101: BinaryAssociation = BinaryAssociation(
    name="left101",
    ends={
        Property(name="smc_Expression102", type=smc_And, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_And", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right103: BinaryAssociation = BinaryAssociation(
    name="right103",
    ends={
        Property(name="smc_Expression105", type=smc_And, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_And104", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left106: BinaryAssociation = BinaryAssociation(
    name="left106",
    ends={
        Property(name="smc_Expression107", type=smc_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Equality", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right108: BinaryAssociation = BinaryAssociation(
    name="right108",
    ends={
        Property(name="smc_Expression110", type=smc_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Equality109", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left111: BinaryAssociation = BinaryAssociation(
    name="left111",
    ends={
        Property(name="smc_Expression112", type=smc_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Comparison", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="smc_Expression127", type=smc_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_Not", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left116: BinaryAssociation = BinaryAssociation(
    name="left116",
    ends={
        Property(name="smc_Expression117", type=smc_PlusOrMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_PlusOrMinus", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right118: BinaryAssociation = BinaryAssociation(
    name="right118",
    ends={
        Property(name="smc_Expression120", type=smc_PlusOrMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_PlusOrMinus119", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left121: BinaryAssociation = BinaryAssociation(
    name="left121",
    ends={
        Property(name="smc_Expression122", type=smc_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_MulOrDiv", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right123: BinaryAssociation = BinaryAssociation(
    name="right123",
    ends={
        Property(name="smc_Expression125", type=smc_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_MulOrDiv124", type=smc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable128: BinaryAssociation = BinaryAssociation(
    name="variable128",
    ends={
        Property(name="smc_VariableDecl129", type=smc_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="smc_VariableRef", type=smc_VariableDecl, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_smc_While_Command = Generalization(general=Command, specific=smc_While)
gen_smc_ParamDecl_Command = Generalization(general=Command, specific=smc_ParamDecl)
gen_smc_InvocationVoid_Command = Generalization(general=Command, specific=smc_InvocationVoid)
gen_smc_Print_Command = Generalization(general=Command, specific=smc_Print)
gen_smc_IfThenElse_Command = Generalization(general=Command, specific=smc_IfThenElse)
gen_smc_VariableDecl_Command = Generalization(general=Command, specific=smc_VariableDecl)
gen_smc_Tuple_Expression = Generalization(general=Expression, specific=smc_Tuple)
gen_smc_VariableAssignment_Command = Generalization(general=Command, specific=smc_VariableAssignment)
gen_smc_Download_AbstractAssignment = Generalization(general=AbstractAssignment, specific=smc_Download)
gen_smc_Database_Download = Generalization(general=Download, specific=smc_Database)
gen_smc_Client_Download = Generalization(general=Download, specific=smc_Client)
gen_smc_Expression_AbstractAssignment = Generalization(general=AbstractAssignment, specific=smc_Expression)
gen_smc_Computation_Functions = Generalization(general=Functions, specific=smc_Computation)
gen_smc_Multiplication_Computation = Generalization(general=Computation, specific=smc_Multiplication)
gen_smc_List_Expression = Generalization(general=Expression, specific=smc_List)
gen_smc_Dict_Expression = Generalization(general=Expression, specific=smc_Dict)
gen_smc_Invocation_Expression = Generalization(general=Expression, specific=smc_Invocation)
gen_smc_BellLapadula_AccessControl = Generalization(general=AccessControl, specific=smc_BellLapadula)
gen_smc_Median_Computation = Generalization(general=Computation, specific=smc_Median)
gen_smc_WeightedAvg_Computation = Generalization(general=Computation, specific=smc_WeightedAvg)
gen_smc_Average_Computation = Generalization(general=Computation, specific=smc_Average)
gen_smc_Count_Computation = Generalization(general=Computation, specific=smc_Count)
gen_smc_AccessControl_Functions = Generalization(general=Functions, specific=smc_AccessControl)
gen_smc_Covered_AccessControl = Generalization(general=AccessControl, specific=smc_Covered)
gen_smc_Search_Functions = Generalization(general=Functions, specific=smc_Search)
gen_smc_BloomFilter_Functions = Generalization(general=Functions, specific=smc_BloomFilter)
gen_smc_Or_Expression = Generalization(general=Expression, specific=smc_Or)
gen_smc_CheckTable_Functions = Generalization(general=Functions, specific=smc_CheckTable)
gen_smc_AddValues_Functions = Generalization(general=Functions, specific=smc_AddValues)
gen_smc_CreateTable_Functions = Generalization(general=Functions, specific=smc_CreateTable)
gen_smc_Return_Command = Generalization(general=Command, specific=smc_Return)
gen_smc_Block_Command = Generalization(general=Command, specific=smc_Block)
gen_smc_And_Expression = Generalization(general=Expression, specific=smc_And)
gen_smc_Equality_Expression = Generalization(general=Expression, specific=smc_Equality)
gen_smc_Comparison_Expression = Generalization(general=Expression, specific=smc_Comparison)
gen_smc_Not_Expression = Generalization(general=Expression, specific=smc_Not)
gen_smc_PlusOrMinus_Expression = Generalization(general=Expression, specific=smc_PlusOrMinus)
gen_smc_MulOrDiv_Expression = Generalization(general=Expression, specific=smc_MulOrDiv)
gen_smc_VariableRef_Expression = Generalization(general=Expression, specific=smc_VariableRef)
gen_smc_IntLiteral_Expression = Generalization(general=Expression, specific=smc_IntLiteral)
gen_smc_DoubleLiteral_Expression = Generalization(general=Expression, specific=smc_DoubleLiteral)
gen_smc_BooleanLiteral_Expression = Generalization(general=Expression, specific=smc_BooleanLiteral)
gen_smc_StringLiteral_Expression = Generalization(general=Expression, specific=smc_StringLiteral)
gen_smc_DateLiteral_Expression = Generalization(general=Expression, specific=smc_DateLiteral)
gen_smc_TimeLiteral_Expression = Generalization(general=Expression, specific=smc_TimeLiteral)

# Domain Model
domain_model = DomainModel(
    name="smc",
    types={smc_Smc, smc_BlockSMC, smc_MainSMC, smc_While, smc_Command, smc_ParamDecl, Command, smc_InvocationVoid, smc_Invocation, smc_Print, smc_Expression, smc_IfThenElse, smc_VariableDecl, smc_AbstractAssignment, smc_Tuple, Expression, smc_VariableAssignment, smc_Download, AbstractAssignment, smc_Database, Download, smc_Client, smc_Multiplication, Computation, smc_List, smc_Dict, smc_Functions, smc_Computation, Functions, smc_BellLapadula, AccessControl, smc_Median, smc_WeightedAvg, smc_Average, smc_Count, smc_AccessControl, smc_Covered, smc_Search, smc_BloomFilter, smc_Or, smc_CheckTable, smc_AddValues, smc_CreateTable, smc_Return, smc_Block, smc_PlusOrMinus, smc_And, smc_Equality, smc_Comparison, smc_Not, smc_MulOrDiv, smc_VariableRef, smc_IntLiteral, smc_DoubleLiteral, smc_BooleanLiteral, smc_StringLiteral, smc_DateLiteral, smc_TimeLiteral, BlockType, BasicType, SecType},
    associations={blocks0, main1, condition7, commands3, call5, value6, body9, condition12, thenBrach14, elseBranch17, option20, var21, option23, tbl26, arg128, x45, arg230, args33, key35, value37, blockName40, funcName43, v_lvl63, y47, array50, weights52, elems54, array57, array59, c_lvls61, pre78, post80, cur66, match68, covered70, tblname73, keyword75, commands94, tblname83, tblname85, args87, tblname90, params92, right113, left96, right98, left101, right103, left106, right108, left111, expression126, left116, right118, left121, right123, variable128},
    generalizations={gen_smc_While_Command, gen_smc_ParamDecl_Command, gen_smc_InvocationVoid_Command, gen_smc_Print_Command, gen_smc_IfThenElse_Command, gen_smc_VariableDecl_Command, gen_smc_Tuple_Expression, gen_smc_VariableAssignment_Command, gen_smc_Download_AbstractAssignment, gen_smc_Database_Download, gen_smc_Client_Download, gen_smc_Expression_AbstractAssignment, gen_smc_Computation_Functions, gen_smc_Multiplication_Computation, gen_smc_List_Expression, gen_smc_Dict_Expression, gen_smc_Invocation_Expression, gen_smc_BellLapadula_AccessControl, gen_smc_Median_Computation, gen_smc_WeightedAvg_Computation, gen_smc_Average_Computation, gen_smc_Count_Computation, gen_smc_AccessControl_Functions, gen_smc_Covered_AccessControl, gen_smc_Search_Functions, gen_smc_BloomFilter_Functions, gen_smc_Or_Expression, gen_smc_CheckTable_Functions, gen_smc_AddValues_Functions, gen_smc_CreateTable_Functions, gen_smc_Return_Command, gen_smc_Block_Command, gen_smc_And_Expression, gen_smc_Equality_Expression, gen_smc_Comparison_Expression, gen_smc_Not_Expression, gen_smc_PlusOrMinus_Expression, gen_smc_MulOrDiv_Expression, gen_smc_VariableRef_Expression, gen_smc_IntLiteral_Expression, gen_smc_DoubleLiteral_Expression, gen_smc_BooleanLiteral_Expression, gen_smc_StringLiteral_Expression, gen_smc_DateLiteral_Expression, gen_smc_TimeLiteral_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)