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
leek_BreakStatement = Class(name="leek::BreakStatement")
Statement = Class(name="Statement")
leek_ContinueStatement = Class(name="leek::ContinueStatement")
leek_StatementBlock = Class(name="leek::StatementBlock")
leek_AffectationStatement = Class(name="leek::AffectationStatement")
leek_Affectation = Class(name="leek::Affectation")
AffectationStatement = Class(name="AffectationStatement")
IfCondition = Class(name="IfCondition")
ForInitializer = Class(name="ForInitializer")
ForAffectation = Class(name="ForAffectation")
leek_VariableReference = Class(name="leek::VariableReference")
leek_Script = Class(name="leek::Script")
leek_Statement = Class(name="leek::Statement")
leek_While = Class(name="leek::While")
Iteration = Class(name="Iteration")
leek_For = Class(name="leek::For")
leek_ForInitializer = Class(name="leek::ForInitializer")
leek_ForAffectation = Class(name="leek::ForAffectation")
leek_ForIn = Class(name="leek::ForIn")
leek_AffectationDecrement = Class(name="leek::AffectationDecrement")
leek_Expression = Class(name="leek::Expression")
leek_AffectationIncrement = Class(name="leek::AffectationIncrement")
leek_AffectationPostfixStatement = Class(name="leek::AffectationPostfixStatement")
leek_AffectationPrefixStatement = Class(name="leek::AffectationPrefixStatement")
leek_If = Class(name="leek::If")
leek_IfCondition = Class(name="leek::IfCondition")
leek_Iteration = Class(name="leek::Iteration")
leek_GlobalDeclaration = Class(name="leek::GlobalDeclaration")
leek_ArrayLiteral = Class(name="leek::ArrayLiteral")
leek_Postfix = Class(name="leek::Postfix")
leek_Prefix = Class(name="leek::Prefix")
AffectationPostfixStatement = Class(name="AffectationPostfixStatement")
Postfix = Class(name="Postfix")
leek_ForInVariableReference = Class(name="leek::ForInVariableReference")
leek_FunctionDeclaration = Class(name="leek::FunctionDeclaration")
Expression = Class(name="Expression")
leek_VariableDeclaration = Class(name="leek::VariableDeclaration")
ForInVariableReference = Class(name="ForInVariableReference")
leek_LocalDeclaration = Class(name="leek::LocalDeclaration")
leek_PrefixDecrement = Class(name="leek::PrefixDecrement")
AffectationPrefixStatement = Class(name="AffectationPrefixStatement")
Prefix = Class(name="Prefix")
leek_PrefixIncrement = Class(name="leek::PrefixIncrement")
leek_Comparison = Class(name="leek::Comparison")
leek_FunctionCall = Class(name="leek::FunctionCall")
leek_ReturnStatement = Class(name="leek::ReturnStatement")
leek_Include = Class(name="leek::Include")
leek_EmptyStatement = Class(name="leek::EmptyStatement")
leek_PostfixDecrement = Class(name="leek::PostfixDecrement")
leek_PostfixIncrement = Class(name="leek::PostfixIncrement")
leek_Less = Class(name="leek::Less")
leek_MoreOrEquals = Class(name="leek::MoreOrEquals")
leek_Equals = Class(name="leek::Equals")
leek_TypedDifferent = Class(name="leek::TypedDifferent")
leek_Different = Class(name="leek::Different")
leek_LessOrEquals = Class(name="leek::LessOrEquals")
leek_Minus = Class(name="leek::Minus")
leek_Multi = Class(name="leek::Multi")
leek_More = Class(name="leek::More")
leek_Or = Class(name="leek::Or")
leek_And = Class(name="leek::And")
leek_Plus = Class(name="leek::Plus")
leek_Not = Class(name="leek::Not")
leek_RealLiteral = Class(name="leek::RealLiteral")
leek_IntLiteral = Class(name="leek::IntLiteral")
leek_StringLiteral = Class(name="leek::StringLiteral")
leek_NullLiteral = Class(name="leek::NullLiteral")
leek_FalseLiteral = Class(name="leek::FalseLiteral")
leek_Div = Class(name="leek::Div")
leek_TernaryIf = Class(name="leek::TernaryIf")
leek_UnitaryMinus = Class(name="leek::UnitaryMinus")
leek_TrueLiteral = Class(name="leek::TrueLiteral")

# leek_BreakStatement class attributes and methods

# Statement class attributes and methods

# leek_ContinueStatement class attributes and methods

# leek_StatementBlock class attributes and methods

# leek_AffectationStatement class attributes and methods

# leek_Affectation class attributes and methods

# AffectationStatement class attributes and methods

# IfCondition class attributes and methods

# ForInitializer class attributes and methods

# ForAffectation class attributes and methods

# leek_VariableReference class attributes and methods

# leek_Script class attributes and methods

# leek_Statement class attributes and methods

# leek_While class attributes and methods

# Iteration class attributes and methods

# leek_For class attributes and methods

# leek_ForInitializer class attributes and methods

# leek_ForAffectation class attributes and methods

# leek_ForIn class attributes and methods

# leek_AffectationDecrement class attributes and methods

# leek_Expression class attributes and methods

# leek_AffectationIncrement class attributes and methods

# leek_AffectationPostfixStatement class attributes and methods

# leek_AffectationPrefixStatement class attributes and methods

# leek_If class attributes and methods

# leek_IfCondition class attributes and methods

# leek_Iteration class attributes and methods

# leek_GlobalDeclaration class attributes and methods

# leek_ArrayLiteral class attributes and methods

# leek_Postfix class attributes and methods

# leek_Prefix class attributes and methods

# AffectationPostfixStatement class attributes and methods

# Postfix class attributes and methods

# leek_ForInVariableReference class attributes and methods

# leek_FunctionDeclaration class attributes and methods
leek_FunctionDeclaration_name: Property = Property(name="name", type=StringType)
leek_FunctionDeclaration.attributes={leek_FunctionDeclaration_name}

# Expression class attributes and methods

# leek_VariableDeclaration class attributes and methods
leek_VariableDeclaration_byAdress: Property = Property(name="byAdress", type=BooleanType)
leek_VariableDeclaration_name: Property = Property(name="name", type=StringType)
leek_VariableDeclaration.attributes={leek_VariableDeclaration_name, leek_VariableDeclaration_byAdress}

# ForInVariableReference class attributes and methods

# leek_LocalDeclaration class attributes and methods

# leek_PrefixDecrement class attributes and methods

# AffectationPrefixStatement class attributes and methods

# Prefix class attributes and methods

# leek_PrefixIncrement class attributes and methods

# leek_Comparison class attributes and methods

# leek_FunctionCall class attributes and methods

# leek_ReturnStatement class attributes and methods

# leek_Include class attributes and methods
leek_Include_importURI: Property = Property(name="importURI", type=StringType)
leek_Include.attributes={leek_Include_importURI}

# leek_EmptyStatement class attributes and methods

# leek_PostfixDecrement class attributes and methods

# leek_PostfixIncrement class attributes and methods

# leek_Less class attributes and methods

# leek_MoreOrEquals class attributes and methods

# leek_Equals class attributes and methods

# leek_TypedDifferent class attributes and methods

# leek_Different class attributes and methods

# leek_LessOrEquals class attributes and methods

# leek_Minus class attributes and methods

# leek_Multi class attributes and methods

# leek_More class attributes and methods

# leek_Or class attributes and methods

# leek_And class attributes and methods

# leek_Plus class attributes and methods

# leek_Not class attributes and methods

# leek_RealLiteral class attributes and methods
leek_RealLiteral_value: Property = Property(name="value", type=FloatType)
leek_RealLiteral.attributes={leek_RealLiteral_value}

# leek_IntLiteral class attributes and methods
leek_IntLiteral_value: Property = Property(name="value", type=IntegerType)
leek_IntLiteral.attributes={leek_IntLiteral_value}

# leek_StringLiteral class attributes and methods
leek_StringLiteral_value: Property = Property(name="value", type=StringType)
leek_StringLiteral.attributes={leek_StringLiteral_value}

# leek_NullLiteral class attributes and methods

# leek_FalseLiteral class attributes and methods

# leek_Div class attributes and methods

# leek_TernaryIf class attributes and methods

# leek_UnitaryMinus class attributes and methods

# leek_TrueLiteral class attributes and methods

# Relationships
statements1: BinaryAssociation = BinaryAssociation(
    name="statements1",
    ends={
        Property(name="leek_Statement2", type=leek_StatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_StatementBlock", type=leek_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable3: BinaryAssociation = BinaryAssociation(
    name="variable3",
    ends={
        Property(name="leek_VariableReference", type=leek_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Affectation", type=leek_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="leek_Statement", type=leek_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Script", type=leek_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition22: BinaryAssociation = BinaryAssociation(
    name="condition22",
    ends={
        Property(name="leek_Expression23", type=leek_While, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_While", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer24: BinaryAssociation = BinaryAssociation(
    name="initializer24",
    ends={
        Property(name="leek_ForInitializer", type=leek_For, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_For", type=leek_ForInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition25: BinaryAssociation = BinaryAssociation(
    name="condition25",
    ends={
        Property(name="leek_Expression27", type=leek_For, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_For26", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
increment28: BinaryAssociation = BinaryAssociation(
    name="increment28",
    ends={
        Property(name="leek_ForAffectation", type=leek_For, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_For29", type=leek_ForAffectation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable4: BinaryAssociation = BinaryAssociation(
    name="variable4",
    ends={
        Property(name="leek_VariableReference5", type=leek_AffectationDecrement, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_AffectationDecrement", type=leek_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decrement6: BinaryAssociation = BinaryAssociation(
    name="decrement6",
    ends={
        Property(name="leek_Expression", type=leek_AffectationDecrement, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_AffectationDecrement7", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable8: BinaryAssociation = BinaryAssociation(
    name="variable8",
    ends={
        Property(name="leek_VariableReference9", type=leek_AffectationIncrement, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_AffectationIncrement", type=leek_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
increment10: BinaryAssociation = BinaryAssociation(
    name="increment10",
    ends={
        Property(name="leek_Expression12", type=leek_AffectationIncrement, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_AffectationIncrement11", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition13: BinaryAssociation = BinaryAssociation(
    name="condition13",
    ends={
        Property(name="leek_IfCondition", type=leek_If, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_If", type=leek_IfCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then14: BinaryAssociation = BinaryAssociation(
    name="then14",
    ends={
        Property(name="leek_Statement16", type=leek_If, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_If15", type=leek_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else17: BinaryAssociation = BinaryAssociation(
    name="else17",
    ends={
        Property(name="leek_Statement19", type=leek_If, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_If18", type=leek_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement20: BinaryAssociation = BinaryAssociation(
    name="statement20",
    ends={
        Property(name="leek_Statement21", type=leek_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Iteration", type=leek_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables46: BinaryAssociation = BinaryAssociation(
    name="variables46",
    ends={
        Property(name="leek_VariableDeclaration47", type=leek_GlobalDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_GlobalDeclaration", type=leek_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values48: BinaryAssociation = BinaryAssociation(
    name="values48",
    ends={
        Property(name="leek_Expression49", type=leek_ArrayLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_ArrayLiteral", type=leek_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key30: BinaryAssociation = BinaryAssociation(
    name="key30",
    ends={
        Property(name="leek_ForInVariableReference", type=leek_ForIn, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_ForIn", type=leek_ForInVariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value31: BinaryAssociation = BinaryAssociation(
    name="value31",
    ends={
        Property(name="leek_ForInVariableReference33", type=leek_ForIn, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_ForIn32", type=leek_ForInVariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array34: BinaryAssociation = BinaryAssociation(
    name="array34",
    ends={
        Property(name="leek_Expression36", type=leek_ForIn, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_ForIn35", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value37: BinaryAssociation = BinaryAssociation(
    name="value37",
    ends={
        Property(name="leek_Expression39", type=leek_ForInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_ForInitializer38", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters40: BinaryAssociation = BinaryAssociation(
    name="parameters40",
    ends={
        Property(name="leek_VariableDeclaration", type=leek_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_FunctionDeclaration", type=leek_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body41: BinaryAssociation = BinaryAssociation(
    name="body41",
    ends={
        Property(name="leek_StatementBlock43", type=leek_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_FunctionDeclaration42", type=leek_StatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables44: BinaryAssociation = BinaryAssociation(
    name="variables44",
    ends={
        Property(name="leek_VariableDeclaration45", type=leek_LocalDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_LocalDeclaration", type=leek_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value65: BinaryAssociation = BinaryAssociation(
    name="value65",
    ends={
        Property(name="leek_PostfixIncrement", type=leek_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="leek_VariableReference66", type=leek_PostfixIncrement, multiplicity=Multiplicity(1, 1))
    }
)
right67: BinaryAssociation = BinaryAssociation(
    name="right67",
    ends={
        Property(name="leek_VariableReference68", type=leek_PrefixDecrement, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_PrefixDecrement", type=leek_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right69: BinaryAssociation = BinaryAssociation(
    name="right69",
    ends={
        Property(name="leek_VariableReference70", type=leek_PrefixIncrement, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_PrefixIncrement", type=leek_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left71: BinaryAssociation = BinaryAssociation(
    name="left71",
    ends={
        Property(name="leek_Expression72", type=leek_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Comparison", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable50: BinaryAssociation = BinaryAssociation(
    name="variable50",
    ends={
        Property(name="leek_VariableDeclaration52", type=leek_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_VariableReference51", type=leek_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
dimensions53: BinaryAssociation = BinaryAssociation(
    name="dimensions53",
    ends={
        Property(name="leek_Expression55", type=leek_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_VariableReference54", type=leek_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function56: BinaryAssociation = BinaryAssociation(
    name="function56",
    ends={
        Property(name="leek_FunctionDeclaration57", type=leek_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_FunctionCall", type=leek_FunctionDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
args58: BinaryAssociation = BinaryAssociation(
    name="args58",
    ends={
        Property(name="leek_Expression60", type=leek_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_FunctionCall59", type=leek_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value61: BinaryAssociation = BinaryAssociation(
    name="value61",
    ends={
        Property(name="leek_Expression62", type=leek_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_ReturnStatement", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value63: BinaryAssociation = BinaryAssociation(
    name="value63",
    ends={
        Property(name="leek_VariableReference64", type=leek_PostfixDecrement, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_PostfixDecrement", type=leek_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right93: BinaryAssociation = BinaryAssociation(
    name="right93",
    ends={
        Property(name="leek_Expression95", type=leek_LessOrEquals, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_LessOrEquals94", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left96: BinaryAssociation = BinaryAssociation(
    name="left96",
    ends={
        Property(name="leek_Expression97", type=leek_Less, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Less", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right98: BinaryAssociation = BinaryAssociation(
    name="right98",
    ends={
        Property(name="leek_Expression100", type=leek_Less, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Less99", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left101: BinaryAssociation = BinaryAssociation(
    name="left101",
    ends={
        Property(name="leek_Expression102", type=leek_MoreOrEquals, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_MoreOrEquals", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right103: BinaryAssociation = BinaryAssociation(
    name="right103",
    ends={
        Property(name="leek_Expression105", type=leek_MoreOrEquals, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_MoreOrEquals104", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right73: BinaryAssociation = BinaryAssociation(
    name="right73",
    ends={
        Property(name="leek_Expression75", type=leek_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Comparison74", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left76: BinaryAssociation = BinaryAssociation(
    name="left76",
    ends={
        Property(name="leek_Expression77", type=leek_Equals, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Equals", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right78: BinaryAssociation = BinaryAssociation(
    name="right78",
    ends={
        Property(name="leek_Expression80", type=leek_Equals, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Equals79", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left81: BinaryAssociation = BinaryAssociation(
    name="left81",
    ends={
        Property(name="leek_Expression82", type=leek_TypedDifferent, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_TypedDifferent", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right83: BinaryAssociation = BinaryAssociation(
    name="right83",
    ends={
        Property(name="leek_Expression85", type=leek_TypedDifferent, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_TypedDifferent84", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left86: BinaryAssociation = BinaryAssociation(
    name="left86",
    ends={
        Property(name="leek_Expression87", type=leek_Different, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Different", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right88: BinaryAssociation = BinaryAssociation(
    name="right88",
    ends={
        Property(name="leek_Expression90", type=leek_Different, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Different89", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left91: BinaryAssociation = BinaryAssociation(
    name="left91",
    ends={
        Property(name="leek_Expression92", type=leek_LessOrEquals, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_LessOrEquals", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right123: BinaryAssociation = BinaryAssociation(
    name="right123",
    ends={
        Property(name="leek_Expression125", type=leek_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Plus124", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left126: BinaryAssociation = BinaryAssociation(
    name="left126",
    ends={
        Property(name="leek_Expression127", type=leek_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Minus", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right128: BinaryAssociation = BinaryAssociation(
    name="right128",
    ends={
        Property(name="leek_Expression130", type=leek_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Minus129", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left131: BinaryAssociation = BinaryAssociation(
    name="left131",
    ends={
        Property(name="leek_Expression132", type=leek_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Multi", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left106: BinaryAssociation = BinaryAssociation(
    name="left106",
    ends={
        Property(name="leek_Expression107", type=leek_More, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_More", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right108: BinaryAssociation = BinaryAssociation(
    name="right108",
    ends={
        Property(name="leek_Expression110", type=leek_More, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_More109", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left111: BinaryAssociation = BinaryAssociation(
    name="left111",
    ends={
        Property(name="leek_Expression112", type=leek_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Or", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right113: BinaryAssociation = BinaryAssociation(
    name="right113",
    ends={
        Property(name="leek_Expression115", type=leek_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Or114", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left116: BinaryAssociation = BinaryAssociation(
    name="left116",
    ends={
        Property(name="leek_Expression117", type=leek_And, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_And", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right118: BinaryAssociation = BinaryAssociation(
    name="right118",
    ends={
        Property(name="leek_Expression120", type=leek_And, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_And119", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left121: BinaryAssociation = BinaryAssociation(
    name="left121",
    ends={
        Property(name="leek_Expression122", type=leek_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Plus", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression151: BinaryAssociation = BinaryAssociation(
    name="expression151",
    ends={
        Property(name="leek_Expression152", type=leek_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Not", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right133: BinaryAssociation = BinaryAssociation(
    name="right133",
    ends={
        Property(name="leek_Expression135", type=leek_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Multi134", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left136: BinaryAssociation = BinaryAssociation(
    name="left136",
    ends={
        Property(name="leek_Expression137", type=leek_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Div", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right138: BinaryAssociation = BinaryAssociation(
    name="right138",
    ends={
        Property(name="leek_Expression140", type=leek_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_Div139", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left141: BinaryAssociation = BinaryAssociation(
    name="left141",
    ends={
        Property(name="leek_Expression142", type=leek_TernaryIf, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_TernaryIf", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then143: BinaryAssociation = BinaryAssociation(
    name="then143",
    ends={
        Property(name="leek_Expression145", type=leek_TernaryIf, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_TernaryIf144", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else146: BinaryAssociation = BinaryAssociation(
    name="else146",
    ends={
        Property(name="leek_Expression148", type=leek_TernaryIf, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_TernaryIf147", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression149: BinaryAssociation = BinaryAssociation(
    name="expression149",
    ends={
        Property(name="leek_Expression150", type=leek_UnitaryMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="leek_UnitaryMinus", type=leek_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_leek_BreakStatement_Statement = Generalization(general=Statement, specific=leek_BreakStatement)
gen_leek_ContinueStatement_Statement = Generalization(general=Statement, specific=leek_ContinueStatement)
gen_leek_StatementBlock_Statement = Generalization(general=Statement, specific=leek_StatementBlock)
gen_leek_AffectationStatement_Statement = Generalization(general=Statement, specific=leek_AffectationStatement)
gen_leek_Affectation_AffectationStatement = Generalization(general=AffectationStatement, specific=leek_Affectation)
gen_leek_Affectation_IfCondition = Generalization(general=IfCondition, specific=leek_Affectation)
gen_leek_Affectation_ForInitializer = Generalization(general=ForInitializer, specific=leek_Affectation)
gen_leek_Affectation_ForAffectation = Generalization(general=ForAffectation, specific=leek_Affectation)
gen_leek_While_Iteration = Generalization(general=Iteration, specific=leek_While)
gen_leek_For_Iteration = Generalization(general=Iteration, specific=leek_For)
gen_leek_AffectationDecrement_AffectationStatement = Generalization(general=AffectationStatement, specific=leek_AffectationDecrement)
gen_leek_AffectationIncrement_AffectationStatement = Generalization(general=AffectationStatement, specific=leek_AffectationIncrement)
gen_leek_AffectationPostfixStatement_AffectationStatement = Generalization(general=AffectationStatement, specific=leek_AffectationPostfixStatement)
gen_leek_AffectationPrefixStatement_AffectationStatement = Generalization(general=AffectationStatement, specific=leek_AffectationPrefixStatement)
gen_leek_If_Statement = Generalization(general=Statement, specific=leek_If)
gen_leek_Iteration_Statement = Generalization(general=Statement, specific=leek_Iteration)
gen_leek_GlobalDeclaration_Statement = Generalization(general=Statement, specific=leek_GlobalDeclaration)
gen_leek_Expression_IfCondition = Generalization(general=IfCondition, specific=leek_Expression)
gen_leek_Expression_ForAffectation = Generalization(general=ForAffectation, specific=leek_Expression)
gen_leek_ArrayLiteral_Expression = Generalization(general=Expression, specific=leek_ArrayLiteral)
gen_leek_Postfix_Expression = Generalization(general=Expression, specific=leek_Postfix)
gen_leek_Prefix_Expression = Generalization(general=Expression, specific=leek_Prefix)
gen_leek_VariableReference_AffectationPostfixStatement = Generalization(general=AffectationPostfixStatement, specific=leek_VariableReference)
gen_leek_VariableReference_ForInVariableReference = Generalization(general=ForInVariableReference, specific=leek_VariableReference)
gen_leek_VariableReference_Postfix = Generalization(general=Postfix, specific=leek_VariableReference)
gen_leek_ForIn_Iteration = Generalization(general=Iteration, specific=leek_ForIn)
gen_leek_FunctionDeclaration_Statement = Generalization(general=Statement, specific=leek_FunctionDeclaration)
gen_leek_FunctionDeclaration_Expression = Generalization(general=Expression, specific=leek_FunctionDeclaration)
gen_leek_VariableDeclaration_ForInVariableReference = Generalization(general=ForInVariableReference, specific=leek_VariableDeclaration)
gen_leek_VariableDeclaration_ForInitializer = Generalization(general=ForInitializer, specific=leek_VariableDeclaration)
gen_leek_LocalDeclaration_Statement = Generalization(general=Statement, specific=leek_LocalDeclaration)
gen_leek_PrefixDecrement_AffectationPrefixStatement = Generalization(general=AffectationPrefixStatement, specific=leek_PrefixDecrement)
gen_leek_PrefixDecrement_Prefix = Generalization(general=Prefix, specific=leek_PrefixDecrement)
gen_leek_PrefixIncrement_AffectationPrefixStatement = Generalization(general=AffectationPrefixStatement, specific=leek_PrefixIncrement)
gen_leek_PrefixIncrement_Prefix = Generalization(general=Prefix, specific=leek_PrefixIncrement)
gen_leek_Comparison_Expression = Generalization(general=Expression, specific=leek_Comparison)
gen_leek_FunctionCall_Statement = Generalization(general=Statement, specific=leek_FunctionCall)
gen_leek_FunctionCall_Expression = Generalization(general=Expression, specific=leek_FunctionCall)
gen_leek_ReturnStatement_Statement = Generalization(general=Statement, specific=leek_ReturnStatement)
gen_leek_Include_Statement = Generalization(general=Statement, specific=leek_Include)
gen_leek_EmptyStatement_Statement = Generalization(general=Statement, specific=leek_EmptyStatement)
gen_leek_PostfixDecrement_AffectationPostfixStatement = Generalization(general=AffectationPostfixStatement, specific=leek_PostfixDecrement)
gen_leek_PostfixDecrement_Postfix = Generalization(general=Postfix, specific=leek_PostfixDecrement)
gen_leek_PostfixIncrement_AffectationPostfixStatement = Generalization(general=AffectationPostfixStatement, specific=leek_PostfixIncrement)
gen_leek_PostfixIncrement_Postfix = Generalization(general=Postfix, specific=leek_PostfixIncrement)
gen_leek_Less_Expression = Generalization(general=Expression, specific=leek_Less)
gen_leek_MoreOrEquals_Expression = Generalization(general=Expression, specific=leek_MoreOrEquals)
gen_leek_Equals_Expression = Generalization(general=Expression, specific=leek_Equals)
gen_leek_TypedDifferent_Expression = Generalization(general=Expression, specific=leek_TypedDifferent)
gen_leek_Different_Expression = Generalization(general=Expression, specific=leek_Different)
gen_leek_LessOrEquals_Expression = Generalization(general=Expression, specific=leek_LessOrEquals)
gen_leek_Minus_Expression = Generalization(general=Expression, specific=leek_Minus)
gen_leek_Multi_Expression = Generalization(general=Expression, specific=leek_Multi)
gen_leek_More_Expression = Generalization(general=Expression, specific=leek_More)
gen_leek_Or_Expression = Generalization(general=Expression, specific=leek_Or)
gen_leek_And_Expression = Generalization(general=Expression, specific=leek_And)
gen_leek_Plus_Expression = Generalization(general=Expression, specific=leek_Plus)
gen_leek_Not_Expression = Generalization(general=Expression, specific=leek_Not)
gen_leek_RealLiteral_Expression = Generalization(general=Expression, specific=leek_RealLiteral)
gen_leek_IntLiteral_Expression = Generalization(general=Expression, specific=leek_IntLiteral)
gen_leek_StringLiteral_Expression = Generalization(general=Expression, specific=leek_StringLiteral)
gen_leek_NullLiteral_Expression = Generalization(general=Expression, specific=leek_NullLiteral)
gen_leek_Div_Expression = Generalization(general=Expression, specific=leek_Div)
gen_leek_TernaryIf_Expression = Generalization(general=Expression, specific=leek_TernaryIf)
gen_leek_UnitaryMinus_Expression = Generalization(general=Expression, specific=leek_UnitaryMinus)
gen_leek_FalseLiteral_Expression = Generalization(general=Expression, specific=leek_FalseLiteral)
gen_leek_TrueLiteral_Expression = Generalization(general=Expression, specific=leek_TrueLiteral)

# Domain Model
domain_model = DomainModel(
    name="leek",
    types={leek_BreakStatement, Statement, leek_ContinueStatement, leek_StatementBlock, leek_AffectationStatement, leek_Affectation, AffectationStatement, IfCondition, ForInitializer, ForAffectation, leek_VariableReference, leek_Script, leek_Statement, leek_While, Iteration, leek_For, leek_ForInitializer, leek_ForAffectation, leek_ForIn, leek_AffectationDecrement, leek_Expression, leek_AffectationIncrement, leek_AffectationPostfixStatement, leek_AffectationPrefixStatement, leek_If, leek_IfCondition, leek_Iteration, leek_GlobalDeclaration, leek_ArrayLiteral, leek_Postfix, leek_Prefix, AffectationPostfixStatement, Postfix, leek_ForInVariableReference, leek_FunctionDeclaration, Expression, leek_VariableDeclaration, ForInVariableReference, leek_LocalDeclaration, leek_PrefixDecrement, AffectationPrefixStatement, Prefix, leek_PrefixIncrement, leek_Comparison, leek_FunctionCall, leek_ReturnStatement, leek_Include, leek_EmptyStatement, leek_PostfixDecrement, leek_PostfixIncrement, leek_Less, leek_MoreOrEquals, leek_Equals, leek_TypedDifferent, leek_Different, leek_LessOrEquals, leek_Minus, leek_Multi, leek_More, leek_Or, leek_And, leek_Plus, leek_Not, leek_RealLiteral, leek_IntLiteral, leek_StringLiteral, leek_NullLiteral, leek_FalseLiteral, leek_Div, leek_TernaryIf, leek_UnitaryMinus, leek_TrueLiteral},
    associations={statements1, variable3, statements0, condition22, initializer24, condition25, increment28, variable4, decrement6, variable8, increment10, condition13, then14, else17, statement20, variables46, values48, key30, value31, array34, value37, parameters40, body41, variables44, value65, right67, right69, left71, variable50, dimensions53, function56, args58, value61, value63, right93, left96, right98, left101, right103, right73, left76, right78, left81, right83, left86, right88, left91, right123, left126, right128, left131, left106, right108, left111, right113, left116, right118, left121, expression151, right133, left136, right138, left141, then143, else146, expression149},
    generalizations={gen_leek_BreakStatement_Statement, gen_leek_ContinueStatement_Statement, gen_leek_StatementBlock_Statement, gen_leek_AffectationStatement_Statement, gen_leek_Affectation_AffectationStatement, gen_leek_Affectation_IfCondition, gen_leek_Affectation_ForInitializer, gen_leek_Affectation_ForAffectation, gen_leek_While_Iteration, gen_leek_For_Iteration, gen_leek_AffectationDecrement_AffectationStatement, gen_leek_AffectationIncrement_AffectationStatement, gen_leek_AffectationPostfixStatement_AffectationStatement, gen_leek_AffectationPrefixStatement_AffectationStatement, gen_leek_If_Statement, gen_leek_Iteration_Statement, gen_leek_GlobalDeclaration_Statement, gen_leek_Expression_IfCondition, gen_leek_Expression_ForAffectation, gen_leek_ArrayLiteral_Expression, gen_leek_Postfix_Expression, gen_leek_Prefix_Expression, gen_leek_VariableReference_AffectationPostfixStatement, gen_leek_VariableReference_ForInVariableReference, gen_leek_VariableReference_Postfix, gen_leek_ForIn_Iteration, gen_leek_FunctionDeclaration_Statement, gen_leek_FunctionDeclaration_Expression, gen_leek_VariableDeclaration_ForInVariableReference, gen_leek_VariableDeclaration_ForInitializer, gen_leek_LocalDeclaration_Statement, gen_leek_PrefixDecrement_AffectationPrefixStatement, gen_leek_PrefixDecrement_Prefix, gen_leek_PrefixIncrement_AffectationPrefixStatement, gen_leek_PrefixIncrement_Prefix, gen_leek_Comparison_Expression, gen_leek_FunctionCall_Statement, gen_leek_FunctionCall_Expression, gen_leek_ReturnStatement_Statement, gen_leek_Include_Statement, gen_leek_EmptyStatement_Statement, gen_leek_PostfixDecrement_AffectationPostfixStatement, gen_leek_PostfixDecrement_Postfix, gen_leek_PostfixIncrement_AffectationPostfixStatement, gen_leek_PostfixIncrement_Postfix, gen_leek_Less_Expression, gen_leek_MoreOrEquals_Expression, gen_leek_Equals_Expression, gen_leek_TypedDifferent_Expression, gen_leek_Different_Expression, gen_leek_LessOrEquals_Expression, gen_leek_Minus_Expression, gen_leek_Multi_Expression, gen_leek_More_Expression, gen_leek_Or_Expression, gen_leek_And_Expression, gen_leek_Plus_Expression, gen_leek_Not_Expression, gen_leek_RealLiteral_Expression, gen_leek_IntLiteral_Expression, gen_leek_StringLiteral_Expression, gen_leek_NullLiteral_Expression, gen_leek_Div_Expression, gen_leek_TernaryIf_Expression, gen_leek_UnitaryMinus_Expression, gen_leek_FalseLiteral_Expression, gen_leek_TrueLiteral_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)