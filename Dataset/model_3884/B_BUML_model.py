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
PrimitiveTypeEnum: Enumeration = Enumeration(
    name="PrimitiveTypeEnum",
    literals={
            EnumerationLiteral(name="BOOL"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="NAT"),
			EnumerationLiteral(name="NAT1"),
			EnumerationLiteral(name="STRING")
    }
)

InequalityOp: Enumeration = Enumeration(
    name="InequalityOp",
    literals={
            EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="LESS_EQ"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="GREATER_EQ")
    }
)

BoolLiteralEnum: Enumeration = Enumeration(
    name="BoolLiteralEnum",
    literals={
            EnumerationLiteral(name="TRUE"),
			EnumerationLiteral(name="FALSE")
    }
)

# Classes
b_Imports = Class(name="b::Imports")
b_Values = Class(name="b::Values")
b_LocalOperations = Class(name="b::LocalOperations")
b_Abstraction = Class(name="b::Abstraction")
b_Sees = Class(name="b::Sees")
b_ConcreteConstants = Class(name="b::ConcreteConstants")
b_Definitions = Class(name="b::Definitions")
b_Properties = Class(name="b::Properties")
b_Operations = Class(name="b::Operations")
b_Machine = Class(name="b::Machine")
Abstraction = Class(name="Abstraction")
b_ConcreteVariables = Class(name="b::ConcreteVariables")
b_Invariant = Class(name="b::Invariant")
b_Initialisation = Class(name="b::Initialisation")
b_Assertions = Class(name="b::Assertions")
b_Sets = Class(name="b::Sets")
b_Implementation = Class(name="b::Implementation")
b_PropertyExpr = Class(name="b::PropertyExpr")
b_ValueExpr = Class(name="b::ValueExpr")
b_Variable = Class(name="b::Variable")
b_InvariantExpr = Class(name="b::InvariantExpr")
b_Type = Class(name="b::Type")
b_InitialisationExpr = Class(name="b::InitialisationExpr")
b_AssertionExpr = Class(name="b::AssertionExpr")
b_Range = Class(name="b::Range")
b_Set = Class(name="b::Set")
b_Definition = Class(name="b::Definition")
b_LogicalExpr = Class(name="b::LogicalExpr")
b_DefinitionCall = Class(name="b::DefinitionCall")
LogicalExpr = Class(name="LogicalExpr")
b_Arg = Class(name="b::Arg")
b_IntLiteral = Class(name="b::IntLiteral")
Condition = Class(name="Condition")
Arg = Class(name="Arg")
b_Var = Class(name="b::Var")
b_Operation = Class(name="b::Operation")
b_Body = Class(name="b::Body")
b_Expr = Class(name="b::Expr")
b_Skip = Class(name="b::Skip")
Body = Class(name="Body")
Expr = Class(name="Expr")
b_Statement = Class(name="b::Statement")
b_If = Class(name="b::If")
FinalExpr = Class(name="FinalExpr")
b_IfCond = Class(name="b::IfCond")
b_Condition = Class(name="b::Condition")
b_Pre = Class(name="b::Pre")
b_PreExpr = Class(name="b::PreExpr")
BeginBody = Class(name="BeginBody")
b_FinalExpr = Class(name="b::FinalExpr")
b_Call = Class(name="b::Call")
b_Seq = Class(name="b::Seq")
b_Begin = Class(name="b::Begin")
b_BeginBody = Class(name="b::BeginBody")
b_Assign = Class(name="b::Assign")
Statement = Class(name="Statement")
b_ReturnExpr = Class(name="b::ReturnExpr")
b_Return = Class(name="b::Return")
b_ReturnTypeExpr = Class(name="b::ReturnTypeExpr")
Return = Class(name="Return")
b_Case = Class(name="b::Case")
b_CaseExpr = Class(name="b::CaseExpr")
b_AndExpr = Class(name="b::AndExpr")
b_ImplyExpr = Class(name="b::ImplyExpr")
b_InequalityExpr = Class(name="b::InequalityExpr")
b_SimpleCall = Class(name="b::SimpleCall")
b_PrimitiveType = Class(name="b::PrimitiveType")
Type = Class(name="Type")
b_Ref = Class(name="b::Ref")
ReturnExpr = Class(name="ReturnExpr")
b_PropertyTyped = Class(name="b::PropertyTyped")
PropertyExpr = Class(name="PropertyExpr")
b_PropertyRange = Class(name="b::PropertyRange")
b_CondLessThan = Class(name="b::CondLessThan")
b_CondMinus = Class(name="b::CondMinus")
b_EqualExpr = Class(name="b::EqualExpr")
b_NegExpr = Class(name="b::NegExpr")
b_BoolTest = Class(name="b::BoolTest")
b_TypeConstraint = Class(name="b::TypeConstraint")
b_ConstantExpr = Class(name="b::ConstantExpr")
b_CondAnd = Class(name="b::CondAnd")
b_CondEq = Class(name="b::CondEq")
b_StringLiteral = Class(name="b::StringLiteral")
b_Program = Class(name="b::Program")
b_CondNeg = Class(name="b::CondNeg")
b_BoolLiteral = Class(name="b::BoolLiteral")
b_ReturnTuple = Class(name="b::ReturnTuple")
b_ReturnOr = Class(name="b::ReturnOr")
ReturnTypeExpr = Class(name="ReturnTypeExpr")
b_Neg = Class(name="b::Neg")
b_ArgMinus = Class(name="b::ArgMinus")

# b_Imports class attributes and methods

# b_Values class attributes and methods

# b_LocalOperations class attributes and methods

# b_Abstraction class attributes and methods
b_Abstraction_name: Property = Property(name="name", type=StringType)
b_Abstraction.attributes={b_Abstraction_name}

# b_Sees class attributes and methods

# b_ConcreteConstants class attributes and methods

# b_Definitions class attributes and methods

# b_Properties class attributes and methods

# b_Operations class attributes and methods

# b_Machine class attributes and methods

# Abstraction class attributes and methods

# b_ConcreteVariables class attributes and methods

# b_Invariant class attributes and methods

# b_Initialisation class attributes and methods

# b_Assertions class attributes and methods

# b_Sets class attributes and methods

# b_Implementation class attributes and methods

# b_PropertyExpr class attributes and methods

# b_ValueExpr class attributes and methods
b_ValueExpr_value: Property = Property(name="value", type=StringType)
b_ValueExpr.attributes={b_ValueExpr_value}

# b_Variable class attributes and methods
b_Variable_name: Property = Property(name="name", type=StringType)
b_Variable.attributes={b_Variable_name}

# b_InvariantExpr class attributes and methods

# b_Type class attributes and methods

# b_InitialisationExpr class attributes and methods

# b_AssertionExpr class attributes and methods

# b_Range class attributes and methods
b_Range_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
b_Range.attributes={b_Range_lowerBound}

# b_Set class attributes and methods

# b_Definition class attributes and methods
b_Definition_name: Property = Property(name="name", type=StringType)
b_Definition.attributes={b_Definition_name}

# b_LogicalExpr class attributes and methods

# b_DefinitionCall class attributes and methods

# LogicalExpr class attributes and methods

# b_Arg class attributes and methods

# b_IntLiteral class attributes and methods
b_IntLiteral_value: Property = Property(name="value", type=IntegerType)
b_IntLiteral.attributes={b_IntLiteral_value}

# Condition class attributes and methods

# Arg class attributes and methods

# b_Var class attributes and methods

# b_Operation class attributes and methods
b_Operation_name: Property = Property(name="name", type=StringType)
b_Operation.attributes={b_Operation_name}

# b_Body class attributes and methods

# b_Expr class attributes and methods

# b_Skip class attributes and methods

# Body class attributes and methods

# Expr class attributes and methods

# b_Statement class attributes and methods

# b_If class attributes and methods

# FinalExpr class attributes and methods

# b_IfCond class attributes and methods

# b_Condition class attributes and methods

# b_Pre class attributes and methods

# b_PreExpr class attributes and methods

# BeginBody class attributes and methods

# b_FinalExpr class attributes and methods

# b_Call class attributes and methods

# b_Seq class attributes and methods

# b_Begin class attributes and methods

# b_BeginBody class attributes and methods

# b_Assign class attributes and methods

# Statement class attributes and methods

# b_ReturnExpr class attributes and methods

# b_Return class attributes and methods

# b_ReturnTypeExpr class attributes and methods

# Return class attributes and methods

# b_Case class attributes and methods

# b_CaseExpr class attributes and methods

# b_AndExpr class attributes and methods

# b_ImplyExpr class attributes and methods

# b_InequalityExpr class attributes and methods
b_InequalityExpr_op: Property = Property(name="op", type=StringType)
b_InequalityExpr.attributes={b_InequalityExpr_op}

# b_SimpleCall class attributes and methods

# b_PrimitiveType class attributes and methods
b_PrimitiveType_type: Property = Property(name="type", type=StringType)
b_PrimitiveType.attributes={b_PrimitiveType_type}

# Type class attributes and methods

# b_Ref class attributes and methods

# ReturnExpr class attributes and methods

# b_PropertyTyped class attributes and methods

# PropertyExpr class attributes and methods

# b_PropertyRange class attributes and methods

# b_CondLessThan class attributes and methods

# b_CondMinus class attributes and methods

# b_EqualExpr class attributes and methods

# b_NegExpr class attributes and methods

# b_BoolTest class attributes and methods

# b_TypeConstraint class attributes and methods

# b_ConstantExpr class attributes and methods
b_ConstantExpr_constant: Property = Property(name="constant", type=StringType)
b_ConstantExpr.attributes={b_ConstantExpr_constant}

# b_CondAnd class attributes and methods

# b_CondEq class attributes and methods

# b_StringLiteral class attributes and methods
b_StringLiteral_value: Property = Property(name="value", type=StringType)
b_StringLiteral.attributes={b_StringLiteral_value}

# b_Program class attributes and methods

# b_CondNeg class attributes and methods

# b_BoolLiteral class attributes and methods
b_BoolLiteral_value: Property = Property(name="value", type=StringType)
b_BoolLiteral_constant: Property = Property(name="constant", type=StringType)
b_BoolLiteral.attributes={b_BoolLiteral_constant, b_BoolLiteral_value}

# b_ReturnTuple class attributes and methods

# b_ReturnOr class attributes and methods

# ReturnTypeExpr class attributes and methods

# b_Neg class attributes and methods

# b_ArgMinus class attributes and methods

# Relationships
refine18: BinaryAssociation = BinaryAssociation(
    name="refine18",
    ends={
        Property(name="b_Machine19", type=b_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Implementation", type=b_Machine, multiplicity=Multiplicity(0, 1))
    }
)
imports20: BinaryAssociation = BinaryAssociation(
    name="imports20",
    ends={
        Property(name="b_Imports", type=b_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Implementation21", type=b_Imports, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values22: BinaryAssociation = BinaryAssociation(
    name="values22",
    ends={
        Property(name="b_Values", type=b_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Implementation23", type=b_Values, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localOperations24: BinaryAssociation = BinaryAssociation(
    name="localOperations24",
    ends={
        Property(name="b_LocalOperations", type=b_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Implementation25", type=b_LocalOperations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
seens26: BinaryAssociation = BinaryAssociation(
    name="seens26",
    ends={
        Property(name="b_Abstraction28", type=b_Sees, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Sees27", type=b_Abstraction, multiplicity=Multiplicity(0, 9999))
    }
)
sees0: BinaryAssociation = BinaryAssociation(
    name="sees0",
    ends={
        Property(name="b_Sees", type=b_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Abstraction", type=b_Sees, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concreteConstants1: BinaryAssociation = BinaryAssociation(
    name="concreteConstants1",
    ends={
        Property(name="b_ConcreteConstants", type=b_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Abstraction2", type=b_ConcreteConstants, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitions3: BinaryAssociation = BinaryAssociation(
    name="definitions3",
    ends={
        Property(name="b_Definitions", type=b_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Abstraction4", type=b_Definitions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties5: BinaryAssociation = BinaryAssociation(
    name="properties5",
    ends={
        Property(name="b_Properties", type=b_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Abstraction6", type=b_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operations7: BinaryAssociation = BinaryAssociation(
    name="operations7",
    ends={
        Property(name="b_Operations", type=b_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Abstraction8", type=b_Operations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concreteVariables9: BinaryAssociation = BinaryAssociation(
    name="concreteVariables9",
    ends={
        Property(name="b_ConcreteVariables", type=b_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Machine", type=b_ConcreteVariables, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invariant10: BinaryAssociation = BinaryAssociation(
    name="invariant10",
    ends={
        Property(name="b_Invariant", type=b_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Machine11", type=b_Invariant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialisation12: BinaryAssociation = BinaryAssociation(
    name="initialisation12",
    ends={
        Property(name="b_Initialisation", type=b_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Machine13", type=b_Initialisation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertions14: BinaryAssociation = BinaryAssociation(
    name="assertions14",
    ends={
        Property(name="b_Assertions", type=b_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Machine15", type=b_Assertions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sets16: BinaryAssociation = BinaryAssociation(
    name="sets16",
    ends={
        Property(name="b_Sets", type=b_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Machine17", type=b_Sets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs49: BinaryAssociation = BinaryAssociation(
    name="exprs49",
    ends={
        Property(name="b_InitialisationExpr", type=b_Initialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Initialisation50", type=b_InitialisationExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable51: BinaryAssociation = BinaryAssociation(
    name="variable51",
    ends={
        Property(name="b_Variable53", type=b_InitialisationExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_InitialisationExpr52", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="b_Type56", type=b_InitialisationExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_InitialisationExpr55", type=b_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs57: BinaryAssociation = BinaryAssociation(
    name="exprs57",
    ends={
        Property(name="b_PropertyExpr", type=b_Properties, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Properties58", type=b_PropertyExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr59: BinaryAssociation = BinaryAssociation(
    name="expr59",
    ends={
        Property(name="b_PropertyExpr61", type=b_Properties, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Properties60", type=b_PropertyExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports29: BinaryAssociation = BinaryAssociation(
    name="imports29",
    ends={
        Property(name="b_Abstraction31", type=b_Imports, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Imports30", type=b_Abstraction, multiplicity=Multiplicity(0, 9999))
    }
)
exprs32: BinaryAssociation = BinaryAssociation(
    name="exprs32",
    ends={
        Property(name="b_ValueExpr", type=b_Values, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Values33", type=b_ValueExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant34: BinaryAssociation = BinaryAssociation(
    name="constant34",
    ends={
        Property(name="b_Variable", type=b_ValueExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ValueExpr35", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
variables36: BinaryAssociation = BinaryAssociation(
    name="variables36",
    ends={
        Property(name="b_Variable38", type=b_ConcreteVariables, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ConcreteVariables37", type=b_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants39: BinaryAssociation = BinaryAssociation(
    name="constants39",
    ends={
        Property(name="b_Variable41", type=b_ConcreteConstants, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ConcreteConstants40", type=b_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprs42: BinaryAssociation = BinaryAssociation(
    name="exprs42",
    ends={
        Property(name="b_InvariantExpr", type=b_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Invariant43", type=b_InvariantExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable44: BinaryAssociation = BinaryAssociation(
    name="variable44",
    ends={
        Property(name="b_Variable46", type=b_InvariantExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_InvariantExpr45", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
type47: BinaryAssociation = BinaryAssociation(
    name="type47",
    ends={
        Property(name="b_Type", type=b_InvariantExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_InvariantExpr48", type=b_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs67: BinaryAssociation = BinaryAssociation(
    name="exprs67",
    ends={
        Property(name="b_AssertionExpr", type=b_Assertions, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Assertions68", type=b_AssertionExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant62: BinaryAssociation = BinaryAssociation(
    name="constant62",
    ends={
        Property(name="b_Variable64", type=b_PropertyExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_PropertyExpr63", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
upperBound65: BinaryAssociation = BinaryAssociation(
    name="upperBound65",
    ends={
        Property(name="b_Variable66", type=b_Range, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Range", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
exprs86: BinaryAssociation = BinaryAssociation(
    name="exprs86",
    ends={
        Property(name="b_Set", type=b_Sets, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Sets87", type=b_Set, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name88: BinaryAssociation = BinaryAssociation(
    name="name88",
    ends={
        Property(name="b_Variable90", type=b_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Set89", type=b_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elems91: BinaryAssociation = BinaryAssociation(
    name="elems91",
    ends={
        Property(name="b_Variable93", type=b_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Set92", type=b_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant69: BinaryAssociation = BinaryAssociation(
    name="constant69",
    ends={
        Property(name="b_Variable71", type=b_AssertionExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_AssertionExpr70", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
type72: BinaryAssociation = BinaryAssociation(
    name="type72",
    ends={
        Property(name="b_Type74", type=b_AssertionExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_AssertionExpr73", type=b_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs75: BinaryAssociation = BinaryAssociation(
    name="exprs75",
    ends={
        Property(name="b_Definition", type=b_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Definitions76", type=b_Definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args77: BinaryAssociation = BinaryAssociation(
    name="args77",
    ends={
        Property(name="b_Variable79", type=b_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Definition78", type=b_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr80: BinaryAssociation = BinaryAssociation(
    name="expr80",
    ends={
        Property(name="b_LogicalExpr", type=b_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Definition81", type=b_LogicalExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
def82: BinaryAssociation = BinaryAssociation(
    name="def82",
    ends={
        Property(name="b_Definition83", type=b_DefinitionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="b_DefinitionCall", type=b_Definition, multiplicity=Multiplicity(0, 1))
    }
)
args84: BinaryAssociation = BinaryAssociation(
    name="args84",
    ends={
        Property(name="b_Arg", type=b_DefinitionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="b_DefinitionCall85", type=b_Arg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr113: BinaryAssociation = BinaryAssociation(
    name="expr113",
    ends={
        Property(name="b_Expr115", type=b_Pre, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Pre114", type=b_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var116: BinaryAssociation = BinaryAssociation(
    name="var116",
    ends={
        Property(name="b_Variable118", type=b_PreExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_PreExpr117", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
type119: BinaryAssociation = BinaryAssociation(
    name="type119",
    ends={
        Property(name="b_Type121", type=b_PreExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_PreExpr120", type=b_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars122: BinaryAssociation = BinaryAssociation(
    name="vars122",
    ends={
        Property(name="b_Variable123", type=b_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Var", type=b_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations94: BinaryAssociation = BinaryAssociation(
    name="operations94",
    ends={
        Property(name="b_Operation", type=b_Operations, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Operations95", type=b_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs96: BinaryAssociation = BinaryAssociation(
    name="outputs96",
    ends={
        Property(name="b_Variable98", type=b_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Operation97", type=b_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args99: BinaryAssociation = BinaryAssociation(
    name="args99",
    ends={
        Property(name="b_Variable101", type=b_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Operation100", type=b_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body102: BinaryAssociation = BinaryAssociation(
    name="body102",
    ends={
        Property(name="b_Body", type=b_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Operation103", type=b_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs104: BinaryAssociation = BinaryAssociation(
    name="exprs104",
    ends={
        Property(name="b_IfCond", type=b_If, multiplicity=Multiplicity(1, 1)),
        Property(name="b_If", type=b_IfCond, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else105: BinaryAssociation = BinaryAssociation(
    name="else105",
    ends={
        Property(name="b_Expr", type=b_If, multiplicity=Multiplicity(1, 1)),
        Property(name="b_If106", type=b_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition107: BinaryAssociation = BinaryAssociation(
    name="condition107",
    ends={
        Property(name="b_Condition", type=b_IfCond, multiplicity=Multiplicity(1, 1)),
        Property(name="b_IfCond108", type=b_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then109: BinaryAssociation = BinaryAssociation(
    name="then109",
    ends={
        Property(name="b_Expr111", type=b_IfCond, multiplicity=Multiplicity(1, 1)),
        Property(name="b_IfCond110", type=b_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs112: BinaryAssociation = BinaryAssociation(
    name="exprs112",
    ends={
        Property(name="b_PreExpr", type=b_Pre, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Pre", type=b_PreExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprs146: BinaryAssociation = BinaryAssociation(
    name="exprs146",
    ends={
        Property(name="b_Expr148", type=b_Seq, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Seq147", type=b_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rets149: BinaryAssociation = BinaryAssociation(
    name="rets149",
    ends={
        Property(name="b_Variable150", type=b_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Call", type=b_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
in124: BinaryAssociation = BinaryAssociation(
    name="in124",
    ends={
        Property(name="b_Seq", type=b_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Var125", type=b_Seq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr126: BinaryAssociation = BinaryAssociation(
    name="expr126",
    ends={
        Property(name="b_BeginBody", type=b_Begin, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Begin", type=b_BeginBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var127: BinaryAssociation = BinaryAssociation(
    name="var127",
    ends={
        Property(name="b_Variable128", type=b_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Assign", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
value129: BinaryAssociation = BinaryAssociation(
    name="value129",
    ends={
        Property(name="b_ReturnExpr", type=b_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Assign130", type=b_ReturnExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var131: BinaryAssociation = BinaryAssociation(
    name="var131",
    ends={
        Property(name="b_Variable132", type=b_ReturnTypeExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ReturnTypeExpr", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
type133: BinaryAssociation = BinaryAssociation(
    name="type133",
    ends={
        Property(name="b_Type135", type=b_ReturnTypeExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ReturnTypeExpr134", type=b_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var136: BinaryAssociation = BinaryAssociation(
    name="var136",
    ends={
        Property(name="b_Variable137", type=b_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Case", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
cases138: BinaryAssociation = BinaryAssociation(
    name="cases138",
    ends={
        Property(name="b_CaseExpr", type=b_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Case139", type=b_CaseExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test140: BinaryAssociation = BinaryAssociation(
    name="test140",
    ends={
        Property(name="b_Variable142", type=b_CaseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_CaseExpr141", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
expr143: BinaryAssociation = BinaryAssociation(
    name="expr143",
    ends={
        Property(name="b_Expr145", type=b_CaseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_CaseExpr144", type=b_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs174: BinaryAssociation = BinaryAssociation(
    name="exprs174",
    ends={
        Property(name="b_LogicalExpr175", type=b_AndExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_AndExpr", type=b_LogicalExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left176: BinaryAssociation = BinaryAssociation(
    name="left176",
    ends={
        Property(name="b_LogicalExpr177", type=b_ImplyExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ImplyExpr", type=b_LogicalExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right178: BinaryAssociation = BinaryAssociation(
    name="right178",
    ends={
        Property(name="b_LogicalExpr180", type=b_ImplyExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ImplyExpr179", type=b_LogicalExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op151: BinaryAssociation = BinaryAssociation(
    name="op151",
    ends={
        Property(name="b_Operation153", type=b_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Call152", type=b_Operation, multiplicity=Multiplicity(0, 1))
    }
)
args154: BinaryAssociation = BinaryAssociation(
    name="args154",
    ends={
        Property(name="b_Arg156", type=b_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Call155", type=b_Arg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op157: BinaryAssociation = BinaryAssociation(
    name="op157",
    ends={
        Property(name="b_Operation158", type=b_SimpleCall, multiplicity=Multiplicity(1, 1)),
        Property(name="b_SimpleCall", type=b_Operation, multiplicity=Multiplicity(0, 1))
    }
)
args159: BinaryAssociation = BinaryAssociation(
    name="args159",
    ends={
        Property(name="b_Arg161", type=b_SimpleCall, multiplicity=Multiplicity(1, 1)),
        Property(name="b_SimpleCall160", type=b_Arg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations162: BinaryAssociation = BinaryAssociation(
    name="operations162",
    ends={
        Property(name="b_Operation164", type=b_LocalOperations, multiplicity=Multiplicity(1, 1)),
        Property(name="b_LocalOperations163", type=b_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type165: BinaryAssociation = BinaryAssociation(
    name="type165",
    ends={
        Property(name="b_Variable166", type=b_Ref, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Ref", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
var167: BinaryAssociation = BinaryAssociation(
    name="var167",
    ends={
        Property(name="b_Variable169", type=b_Ref, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Ref168", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
type170: BinaryAssociation = BinaryAssociation(
    name="type170",
    ends={
        Property(name="b_Type171", type=b_PropertyTyped, multiplicity=Multiplicity(1, 1)),
        Property(name="b_PropertyTyped", type=b_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
range172: BinaryAssociation = BinaryAssociation(
    name="range172",
    ends={
        Property(name="b_Range173", type=b_PropertyRange, multiplicity=Multiplicity(1, 1)),
        Property(name="b_PropertyRange", type=b_Range, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left202: BinaryAssociation = BinaryAssociation(
    name="left202",
    ends={
        Property(name="b_Condition203", type=b_CondEq, multiplicity=Multiplicity(1, 1)),
        Property(name="b_CondEq", type=b_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right204: BinaryAssociation = BinaryAssociation(
    name="right204",
    ends={
        Property(name="b_Condition206", type=b_CondEq, multiplicity=Multiplicity(1, 1)),
        Property(name="b_CondEq205", type=b_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left207: BinaryAssociation = BinaryAssociation(
    name="left207",
    ends={
        Property(name="b_Condition208", type=b_CondLessThan, multiplicity=Multiplicity(1, 1)),
        Property(name="b_CondLessThan", type=b_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right209: BinaryAssociation = BinaryAssociation(
    name="right209",
    ends={
        Property(name="b_Condition211", type=b_CondLessThan, multiplicity=Multiplicity(1, 1)),
        Property(name="b_CondLessThan210", type=b_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left181: BinaryAssociation = BinaryAssociation(
    name="left181",
    ends={
        Property(name="b_LogicalExpr182", type=b_InequalityExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_InequalityExpr", type=b_LogicalExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right183: BinaryAssociation = BinaryAssociation(
    name="right183",
    ends={
        Property(name="b_LogicalExpr185", type=b_InequalityExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_InequalityExpr184", type=b_LogicalExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left186: BinaryAssociation = BinaryAssociation(
    name="left186",
    ends={
        Property(name="b_LogicalExpr187", type=b_EqualExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_EqualExpr", type=b_LogicalExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right188: BinaryAssociation = BinaryAssociation(
    name="right188",
    ends={
        Property(name="b_LogicalExpr190", type=b_EqualExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_EqualExpr189", type=b_LogicalExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr191: BinaryAssociation = BinaryAssociation(
    name="expr191",
    ends={
        Property(name="b_LogicalExpr192", type=b_NegExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_NegExpr", type=b_LogicalExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr193: BinaryAssociation = BinaryAssociation(
    name="expr193",
    ends={
        Property(name="b_LogicalExpr194", type=b_BoolTest, multiplicity=Multiplicity(1, 1)),
        Property(name="b_BoolTest", type=b_LogicalExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var195: BinaryAssociation = BinaryAssociation(
    name="var195",
    ends={
        Property(name="b_Variable196", type=b_TypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="b_TypeConstraint", type=b_Variable, multiplicity=Multiplicity(0, 1))
    }
)
type197: BinaryAssociation = BinaryAssociation(
    name="type197",
    ends={
        Property(name="b_Type199", type=b_TypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="b_TypeConstraint198", type=b_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs200: BinaryAssociation = BinaryAssociation(
    name="exprs200",
    ends={
        Property(name="b_Condition201", type=b_CondAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="b_CondAnd", type=b_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
machines233: BinaryAssociation = BinaryAssociation(
    name="machines233",
    ends={
        Property(name="b_Machine234", type=b_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Program", type=b_Machine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementations235: BinaryAssociation = BinaryAssociation(
    name="implementations235",
    ends={
        Property(name="b_Implementation237", type=b_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Program236", type=b_Implementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left212: BinaryAssociation = BinaryAssociation(
    name="left212",
    ends={
        Property(name="b_Condition213", type=b_CondMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="b_CondMinus", type=b_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right214: BinaryAssociation = BinaryAssociation(
    name="right214",
    ends={
        Property(name="b_Condition216", type=b_CondMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="b_CondMinus215", type=b_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr217: BinaryAssociation = BinaryAssociation(
    name="expr217",
    ends={
        Property(name="b_Condition218", type=b_CondNeg, multiplicity=Multiplicity(1, 1)),
        Property(name="b_CondNeg", type=b_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars219: BinaryAssociation = BinaryAssociation(
    name="vars219",
    ends={
        Property(name="b_Variable220", type=b_ReturnTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ReturnTuple", type=b_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
value221: BinaryAssociation = BinaryAssociation(
    name="value221",
    ends={
        Property(name="b_LogicalExpr223", type=b_ReturnTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ReturnTuple222", type=b_LogicalExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs224: BinaryAssociation = BinaryAssociation(
    name="exprs224",
    ends={
        Property(name="b_ReturnTypeExpr225", type=b_ReturnOr, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ReturnOr", type=b_ReturnTypeExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr226: BinaryAssociation = BinaryAssociation(
    name="expr226",
    ends={
        Property(name="b_ReturnExpr227", type=b_Neg, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Neg", type=b_ReturnExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left228: BinaryAssociation = BinaryAssociation(
    name="left228",
    ends={
        Property(name="b_Arg229", type=b_ArgMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ArgMinus", type=b_Arg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right230: BinaryAssociation = BinaryAssociation(
    name="right230",
    ends={
        Property(name="b_Arg232", type=b_ArgMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="b_ArgMinus231", type=b_Arg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_b_Implementation_Abstraction = Generalization(general=Abstraction, specific=b_Implementation)
gen_b_Machine_Abstraction = Generalization(general=Abstraction, specific=b_Machine)
gen_b_DefinitionCall_LogicalExpr = Generalization(general=LogicalExpr, specific=b_DefinitionCall)
gen_b_IntLiteral_LogicalExpr = Generalization(general=LogicalExpr, specific=b_IntLiteral)
gen_b_IntLiteral_Condition = Generalization(general=Condition, specific=b_IntLiteral)
gen_b_IntLiteral_Arg = Generalization(general=Arg, specific=b_IntLiteral)
gen_b_Var_Body = Generalization(general=Body, specific=b_Var)
gen_b_Var_Expr = Generalization(general=Expr, specific=b_Var)
gen_b_Var_FinalExpr = Generalization(general=FinalExpr, specific=b_Var)
gen_b_Skip_Body = Generalization(general=Body, specific=b_Skip)
gen_b_Skip_Expr = Generalization(general=Expr, specific=b_Skip)
gen_b_If_Body = Generalization(general=Body, specific=b_If)
gen_b_If_Expr = Generalization(general=Expr, specific=b_If)
gen_b_If_FinalExpr = Generalization(general=FinalExpr, specific=b_If)
gen_b_Pre_Body = Generalization(general=Body, specific=b_Pre)
gen_b_Seq_Body = Generalization(general=Body, specific=b_Seq)
gen_b_Seq_BeginBody = Generalization(general=BeginBody, specific=b_Seq)
gen_b_FinalExpr_BeginBody = Generalization(general=BeginBody, specific=b_FinalExpr)
gen_b_Call_Expr = Generalization(general=Expr, specific=b_Call)
gen_b_Call_Statement = Generalization(general=Statement, specific=b_Call)
gen_b_Begin_Body = Generalization(general=Body, specific=b_Begin)
gen_b_Assign_Expr = Generalization(general=Expr, specific=b_Assign)
gen_b_Assign_Statement = Generalization(general=Statement, specific=b_Assign)
gen_b_Return_Expr = Generalization(general=Expr, specific=b_Return)
gen_b_Return_FinalExpr = Generalization(general=FinalExpr, specific=b_Return)
gen_b_ReturnTypeExpr_Return = Generalization(general=Return, specific=b_ReturnTypeExpr)
gen_b_Case_Expr = Generalization(general=Expr, specific=b_Case)
gen_b_Case_FinalExpr = Generalization(general=FinalExpr, specific=b_Case)
gen_b_AndExpr_LogicalExpr = Generalization(general=LogicalExpr, specific=b_AndExpr)
gen_b_ImplyExpr_LogicalExpr = Generalization(general=LogicalExpr, specific=b_ImplyExpr)
gen_b_InequalityExpr_LogicalExpr = Generalization(general=LogicalExpr, specific=b_InequalityExpr)
gen_b_PrimitiveType_Type = Generalization(general=Type, specific=b_PrimitiveType)
gen_b_Ref_Type = Generalization(general=Type, specific=b_Ref)
gen_b_Ref_LogicalExpr = Generalization(general=LogicalExpr, specific=b_Ref)
gen_b_Ref_Condition = Generalization(general=Condition, specific=b_Ref)
gen_b_Ref_ReturnExpr = Generalization(general=ReturnExpr, specific=b_Ref)
gen_b_Ref_Arg = Generalization(general=Arg, specific=b_Ref)
gen_b_PropertyTyped_PropertyExpr = Generalization(general=PropertyExpr, specific=b_PropertyTyped)
gen_b_PropertyRange_PropertyExpr = Generalization(general=PropertyExpr, specific=b_PropertyRange)
gen_b_CondLessThan_Condition = Generalization(general=Condition, specific=b_CondLessThan)
gen_b_CondMinus_Condition = Generalization(general=Condition, specific=b_CondMinus)
gen_b_EqualExpr_LogicalExpr = Generalization(general=LogicalExpr, specific=b_EqualExpr)
gen_b_NegExpr_LogicalExpr = Generalization(general=LogicalExpr, specific=b_NegExpr)
gen_b_BoolTest_LogicalExpr = Generalization(general=LogicalExpr, specific=b_BoolTest)
gen_b_BoolTest_ReturnExpr = Generalization(general=ReturnExpr, specific=b_BoolTest)
gen_b_TypeConstraint_LogicalExpr = Generalization(general=LogicalExpr, specific=b_TypeConstraint)
gen_b_ConstantExpr_LogicalExpr = Generalization(general=LogicalExpr, specific=b_ConstantExpr)
gen_b_CondAnd_Condition = Generalization(general=Condition, specific=b_CondAnd)
gen_b_CondEq_Condition = Generalization(general=Condition, specific=b_CondEq)
gen_b_StringLiteral_Arg = Generalization(general=Arg, specific=b_StringLiteral)
gen_b_CondNeg_Condition = Generalization(general=Condition, specific=b_CondNeg)
gen_b_BoolLiteral_Condition = Generalization(general=Condition, specific=b_BoolLiteral)
gen_b_BoolLiteral_ReturnExpr = Generalization(general=ReturnExpr, specific=b_BoolLiteral)
gen_b_BoolLiteral_Arg = Generalization(general=Arg, specific=b_BoolLiteral)
gen_b_ReturnTuple_Return = Generalization(general=Return, specific=b_ReturnTuple)
gen_b_ReturnOr_ReturnTypeExpr = Generalization(general=ReturnTypeExpr, specific=b_ReturnOr)
gen_b_Neg_ReturnExpr = Generalization(general=ReturnExpr, specific=b_Neg)
gen_b_ArgMinus_Arg = Generalization(general=Arg, specific=b_ArgMinus)

# Domain Model
domain_model = DomainModel(
    name="b",
    types={b_Imports, b_Values, b_LocalOperations, b_Abstraction, b_Sees, b_ConcreteConstants, b_Definitions, b_Properties, b_Operations, b_Machine, Abstraction, b_ConcreteVariables, b_Invariant, b_Initialisation, b_Assertions, b_Sets, b_Implementation, b_PropertyExpr, b_ValueExpr, b_Variable, b_InvariantExpr, b_Type, b_InitialisationExpr, b_AssertionExpr, b_Range, b_Set, b_Definition, b_LogicalExpr, b_DefinitionCall, LogicalExpr, b_Arg, b_IntLiteral, Condition, Arg, b_Var, b_Operation, b_Body, b_Expr, b_Skip, Body, Expr, b_Statement, b_If, FinalExpr, b_IfCond, b_Condition, b_Pre, b_PreExpr, BeginBody, b_FinalExpr, b_Call, b_Seq, b_Begin, b_BeginBody, b_Assign, Statement, b_ReturnExpr, b_Return, b_ReturnTypeExpr, Return, b_Case, b_CaseExpr, b_AndExpr, b_ImplyExpr, b_InequalityExpr, b_SimpleCall, b_PrimitiveType, Type, b_Ref, ReturnExpr, b_PropertyTyped, PropertyExpr, b_PropertyRange, b_CondLessThan, b_CondMinus, b_EqualExpr, b_NegExpr, b_BoolTest, b_TypeConstraint, b_ConstantExpr, b_CondAnd, b_CondEq, b_StringLiteral, b_Program, b_CondNeg, b_BoolLiteral, b_ReturnTuple, b_ReturnOr, ReturnTypeExpr, b_Neg, b_ArgMinus, PrimitiveTypeEnum, InequalityOp, BoolLiteralEnum},
    associations={refine18, imports20, values22, localOperations24, seens26, sees0, concreteConstants1, definitions3, properties5, operations7, concreteVariables9, invariant10, initialisation12, assertions14, sets16, exprs49, variable51, type54, exprs57, expr59, imports29, exprs32, constant34, variables36, constants39, exprs42, variable44, type47, exprs67, constant62, upperBound65, exprs86, name88, elems91, constant69, type72, exprs75, args77, expr80, def82, args84, expr113, var116, type119, vars122, operations94, outputs96, args99, body102, exprs104, else105, condition107, then109, exprs112, exprs146, rets149, in124, expr126, var127, value129, var131, type133, var136, cases138, test140, expr143, exprs174, left176, right178, op151, args154, op157, args159, operations162, type165, var167, type170, range172, left202, right204, left207, right209, left181, right183, left186, right188, expr191, expr193, var195, type197, exprs200, machines233, implementations235, left212, right214, expr217, vars219, value221, exprs224, expr226, left228, right230},
    generalizations={gen_b_Implementation_Abstraction, gen_b_Machine_Abstraction, gen_b_DefinitionCall_LogicalExpr, gen_b_IntLiteral_LogicalExpr, gen_b_IntLiteral_Condition, gen_b_IntLiteral_Arg, gen_b_Var_Body, gen_b_Var_Expr, gen_b_Var_FinalExpr, gen_b_Skip_Body, gen_b_Skip_Expr, gen_b_If_Body, gen_b_If_Expr, gen_b_If_FinalExpr, gen_b_Pre_Body, gen_b_Seq_Body, gen_b_Seq_BeginBody, gen_b_FinalExpr_BeginBody, gen_b_Call_Expr, gen_b_Call_Statement, gen_b_Begin_Body, gen_b_Assign_Expr, gen_b_Assign_Statement, gen_b_Return_Expr, gen_b_Return_FinalExpr, gen_b_ReturnTypeExpr_Return, gen_b_Case_Expr, gen_b_Case_FinalExpr, gen_b_AndExpr_LogicalExpr, gen_b_ImplyExpr_LogicalExpr, gen_b_InequalityExpr_LogicalExpr, gen_b_PrimitiveType_Type, gen_b_Ref_Type, gen_b_Ref_LogicalExpr, gen_b_Ref_Condition, gen_b_Ref_ReturnExpr, gen_b_Ref_Arg, gen_b_PropertyTyped_PropertyExpr, gen_b_PropertyRange_PropertyExpr, gen_b_CondLessThan_Condition, gen_b_CondMinus_Condition, gen_b_EqualExpr_LogicalExpr, gen_b_NegExpr_LogicalExpr, gen_b_BoolTest_LogicalExpr, gen_b_BoolTest_ReturnExpr, gen_b_TypeConstraint_LogicalExpr, gen_b_ConstantExpr_LogicalExpr, gen_b_CondAnd_Condition, gen_b_CondEq_Condition, gen_b_StringLiteral_Arg, gen_b_CondNeg_Condition, gen_b_BoolLiteral_Condition, gen_b_BoolLiteral_ReturnExpr, gen_b_BoolLiteral_Arg, gen_b_ReturnTuple_Return, gen_b_ReturnOr_ReturnTypeExpr, gen_b_Neg_ReturnExpr, gen_b_ArgMinus_Arg},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)