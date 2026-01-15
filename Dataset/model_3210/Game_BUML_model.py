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
EqualityKind: Enumeration = Enumeration(
    name="EqualityKind",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="notEqual")
    }
)

AccessKind: Enumeration = Enumeration(
    name="AccessKind",
    literals={
            EnumerationLiteral(name="exist"),
			EnumerationLiteral(name="read"),
			EnumerationLiteral(name="write")
    }
)

ComparisonKind: Enumeration = Enumeration(
    name="ComparisonKind",
    literals={
            EnumerationLiteral(name="lower"),
			EnumerationLiteral(name="lowerOrEqual"),
			EnumerationLiteral(name="greaterOrEqual"),
			EnumerationLiteral(name="greater")
    }
)

AdditiveKind: Enumeration = Enumeration(
    name="AdditiveKind",
    literals={
            EnumerationLiteral(name="add"),
			EnumerationLiteral(name="subtract")
    }
)

MultiplicativeKind: Enumeration = Enumeration(
    name="MultiplicativeKind",
    literals={
            EnumerationLiteral(name="multiply"),
			EnumerationLiteral(name="divide"),
			EnumerationLiteral(name="remainder")
    }
)

# Classes
game_System = Class(name="game::System")
game_ComponentData = Class(name="game::ComponentData")
game_End = Class(name="game::End")
game_Game = Class(name="game::Game")
game_Type = Class(name="game::Type")
game_Access = Class(name="game::Access")
game_Function = Class(name="game::Function")
game_Statement = Class(name="game::Statement", is_abstract=True)
game_Query = Class(name="game::Query")
game_Variable = Class(name="game::Variable")
game_Assignment = Class(name="game::Assignment")
game_Selection = Class(name="game::Selection")
Statement = Class(name="Statement")
game_Expression = Class(name="game::Expression", is_abstract=True)
game_Iteration = Class(name="game::Iteration")
game_Forall = Class(name="game::Forall")
game_Addable = Class(name="game::Addable", is_abstract=True)
Comparable = Class(name="Comparable")
game_Multipliable = Class(name="game::Multipliable", is_abstract=True)
Addable = Class(name="Addable")
game_Setable = Class(name="game::Setable", is_abstract=True)
Multipliable = Class(name="Multipliable")
game_Or = Class(name="game::Or")
game_Subprocess = Class(name="game::Subprocess")
game_Call = Class(name="game::Call")
game_Orable = Class(name="game::Orable", is_abstract=True)
Expression = Class(name="Expression")
game_Andable = Class(name="game::Andable", is_abstract=True)
Orable = Class(name="Orable")
game_Equatable = Class(name="game::Equatable", is_abstract=True)
Andable = Class(name="Andable")
game_Comparable = Class(name="game::Comparable", is_abstract=True)
Equatable = Class(name="Equatable")
game_Addition = Class(name="game::Addition")
game_And = Class(name="game::And")
game_Equality = Class(name="game::Equality")
game_Comparison = Class(name="game::Comparison")
game_LogicalNot = Class(name="game::LogicalNot")
game_Multiplication = Class(name="game::Multiplication")
game_SetExpression = Class(name="game::SetExpression")
Setable = Class(name="Setable")
game_Primary = Class(name="game::Primary", is_abstract=True)
Primary = Class(name="Primary")
game_Atom = Class(name="game::Atom", is_abstract=True)
Index = Class(name="Index")
game_Index = Class(name="game::Index")
game_Cardinal = Class(name="game::Cardinal")
game_Collection = Class(name="game::Collection", is_abstract=True)
game_Brackets = Class(name="game::Brackets")
Collection = Class(name="Collection")
game_Join = Class(name="game::Join")
game_ImplicitSet = Class(name="game::ImplicitSet")
Atom = Class(name="Atom")
game_Cell = Class(name="game::Cell")

# game_System class attributes and methods
game_System_name: Property = Property(name="name", type=StringType)
game_System.attributes={game_System_name}

# game_ComponentData class attributes and methods
game_ComponentData_name: Property = Property(name="name", type=StringType)
game_ComponentData.attributes={game_ComponentData_name}

# game_End class attributes and methods

# game_Game class attributes and methods
game_Game_name: Property = Property(name="name", type=StringType)
game_Game_version: Property = Property(name="version", type=StringType)
game_Game.attributes={game_Game_name, game_Game_version}

# game_Type class attributes and methods
game_Type_valueType: Property = Property(name="valueType", type=BooleanType)
game_Type_namespace: Property = Property(name="namespace", type=StringType)
game_Type_name: Property = Property(name="name", type=StringType)
game_Type.attributes={game_Type_name, game_Type_valueType, game_Type_namespace}

# game_Access class attributes and methods
game_Access_name: Property = Property(name="name", type=StringType)
game_Access_kind: Property = Property(name="kind", type=StringType)
game_Access.attributes={game_Access_name, game_Access_kind}

# game_Function class attributes and methods
game_Function_name: Property = Property(name="name", type=StringType)
game_Function.attributes={game_Function_name}

# game_Statement class attributes and methods

# game_Query class attributes and methods
game_Query_name: Property = Property(name="name", type=StringType)
game_Query.attributes={game_Query_name}

# game_Variable class attributes and methods
game_Variable_name: Property = Property(name="name", type=StringType)
game_Variable.attributes={game_Variable_name}

# game_Assignment class attributes and methods

# game_Selection class attributes and methods

# Statement class attributes and methods

# game_Expression class attributes and methods

# game_Iteration class attributes and methods

# game_Forall class attributes and methods

# game_Addable class attributes and methods

# Comparable class attributes and methods

# game_Multipliable class attributes and methods

# Addable class attributes and methods

# game_Setable class attributes and methods

# Multipliable class attributes and methods

# game_Or class attributes and methods

# game_Subprocess class attributes and methods

# game_Call class attributes and methods
game_Call_name: Property = Property(name="name", type=StringType)
game_Call.attributes={game_Call_name}

# game_Orable class attributes and methods

# Expression class attributes and methods

# game_Andable class attributes and methods

# Orable class attributes and methods

# game_Equatable class attributes and methods

# Andable class attributes and methods

# game_Comparable class attributes and methods

# Equatable class attributes and methods

# game_Addition class attributes and methods
game_Addition_kind: Property = Property(name="kind", type=StringType)
game_Addition.attributes={game_Addition_kind}

# game_And class attributes and methods

# game_Equality class attributes and methods
game_Equality_kind: Property = Property(name="kind", type=StringType)
game_Equality.attributes={game_Equality_kind}

# game_Comparison class attributes and methods
game_Comparison_kind: Property = Property(name="kind", type=StringType)
game_Comparison.attributes={game_Comparison_kind}

# game_LogicalNot class attributes and methods

# game_Multiplication class attributes and methods
game_Multiplication_kind: Property = Property(name="kind", type=StringType)
game_Multiplication.attributes={game_Multiplication_kind}

# game_SetExpression class attributes and methods

# Setable class attributes and methods

# game_Primary class attributes and methods

# Primary class attributes and methods

# game_Atom class attributes and methods

# Index class attributes and methods

# game_Index class attributes and methods

# game_Cardinal class attributes and methods

# game_Collection class attributes and methods

# game_Brackets class attributes and methods

# Collection class attributes and methods

# game_Join class attributes and methods

# game_ImplicitSet class attributes and methods

# Atom class attributes and methods

# game_Cell class attributes and methods

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="game_Game", type=game_Type, multiplicity=Multiplicity(0, 9999)),
        Property(name="game_Type", type=game_Game, multiplicity=Multiplicity(1, 1))
    }
)
systems1: BinaryAssociation = BinaryAssociation(
    name="systems1",
    ends={
        Property(name="game_System", type=game_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Game2", type=game_System, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components3: BinaryAssociation = BinaryAssociation(
    name="components3",
    ends={
        Property(name="game_ComponentData", type=game_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Game4", type=game_ComponentData, multiplicity=Multiplicity(0, 9999))
    }
)
end5: BinaryAssociation = BinaryAssociation(
    name="end5",
    ends={
        Property(name="game_End", type=game_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Game6", type=game_End, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
queries20: BinaryAssociation = BinaryAssociation(
    name="queries20",
    ends={
        Property(name="game_Query", type=game_System, multiplicity=Multiplicity(1, 1)),
        Property(name="game_System21", type=game_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accesses22: BinaryAssociation = BinaryAssociation(
    name="accesses22",
    ends={
        Property(name="game_Access", type=game_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Query23", type=game_Access, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions7: BinaryAssociation = BinaryAssociation(
    name="functions7",
    ends={
        Property(name="game_Function", type=game_Game, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Game8", type=game_Function, multiplicity=Multiplicity(0, 9999))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="game_Type11", type=game_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Function10", type=game_Type, multiplicity=Multiplicity(0, 1))
    }
)
statements12: BinaryAssociation = BinaryAssociation(
    name="statements12",
    ends={
        Property(name="game_Statement", type=game_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Function13", type=game_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="game_Type16", type=game_ComponentData, multiplicity=Multiplicity(1, 1)),
        Property(name="game_ComponentData15", type=game_Type, multiplicity=Multiplicity(0, 1))
    }
)
statements17: BinaryAssociation = BinaryAssociation(
    name="statements17",
    ends={
        Property(name="game_Statement19", type=game_System, multiplicity=Multiplicity(1, 1)),
        Property(name="game_System18", type=game_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition36: BinaryAssociation = BinaryAssociation(
    name="condition36",
    ends={
        Property(name="game_Expression37", type=game_Forall, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Forall", type=game_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements38: BinaryAssociation = BinaryAssociation(
    name="statements38",
    ends={
        Property(name="game_Statement40", type=game_Forall, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Forall39", type=game_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable41: BinaryAssociation = BinaryAssociation(
    name="variable41",
    ends={
        Property(name="game_Variable", type=game_Forall, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Forall42", type=game_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition24: BinaryAssociation = BinaryAssociation(
    name="condition24",
    ends={
        Property(name="game_Expression", type=game_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Selection", type=game_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positiveStatements25: BinaryAssociation = BinaryAssociation(
    name="positiveStatements25",
    ends={
        Property(name="game_Statement27", type=game_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Selection26", type=game_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
negativeStatements28: BinaryAssociation = BinaryAssociation(
    name="negativeStatements28",
    ends={
        Property(name="game_Statement30", type=game_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Selection29", type=game_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition31: BinaryAssociation = BinaryAssociation(
    name="condition31",
    ends={
        Property(name="game_Expression32", type=game_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Iteration", type=game_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements33: BinaryAssociation = BinaryAssociation(
    name="statements33",
    ends={
        Property(name="game_Statement35", type=game_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Iteration34", type=game_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left52: BinaryAssociation = BinaryAssociation(
    name="left52",
    ends={
        Property(name="game_Orable", type=game_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Or", type=game_Orable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atom43: BinaryAssociation = BinaryAssociation(
    name="atom43",
    ends={
        Property(name="game_Expression44", type=game_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Assignment", type=game_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression45: BinaryAssociation = BinaryAssociation(
    name="expression45",
    ends={
        Property(name="game_Expression47", type=game_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Assignment46", type=game_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
call48: BinaryAssociation = BinaryAssociation(
    name="call48",
    ends={
        Property(name="game_Call", type=game_Subprocess, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Subprocess", type=game_Call, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="game_Type51", type=game_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Expression50", type=game_Type, multiplicity=Multiplicity(0, 1))
    }
)
left63: BinaryAssociation = BinaryAssociation(
    name="left63",
    ends={
        Property(name="game_Comparable64", type=game_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Comparison", type=game_Comparable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right65: BinaryAssociation = BinaryAssociation(
    name="right65",
    ends={
        Property(name="game_Addable", type=game_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Comparison66", type=game_Addable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left67: BinaryAssociation = BinaryAssociation(
    name="left67",
    ends={
        Property(name="game_Addable68", type=game_Addition, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Addition", type=game_Addable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right53: BinaryAssociation = BinaryAssociation(
    name="right53",
    ends={
        Property(name="game_Andable", type=game_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Or54", type=game_Andable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left55: BinaryAssociation = BinaryAssociation(
    name="left55",
    ends={
        Property(name="game_Andable56", type=game_And, multiplicity=Multiplicity(1, 1)),
        Property(name="game_And", type=game_Andable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right57: BinaryAssociation = BinaryAssociation(
    name="right57",
    ends={
        Property(name="game_Equatable", type=game_And, multiplicity=Multiplicity(1, 1)),
        Property(name="game_And58", type=game_Equatable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left59: BinaryAssociation = BinaryAssociation(
    name="left59",
    ends={
        Property(name="game_Equatable60", type=game_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Equality", type=game_Equatable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right61: BinaryAssociation = BinaryAssociation(
    name="right61",
    ends={
        Property(name="game_Comparable", type=game_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Equality62", type=game_Comparable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments79: BinaryAssociation = BinaryAssociation(
    name="arguments79",
    ends={
        Property(name="game_Expression81", type=game_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Call80", type=game_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression82: BinaryAssociation = BinaryAssociation(
    name="expression82",
    ends={
        Property(name="game_Primary83", type=game_LogicalNot, multiplicity=Multiplicity(1, 1)),
        Property(name="game_LogicalNot", type=game_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right69: BinaryAssociation = BinaryAssociation(
    name="right69",
    ends={
        Property(name="game_Multipliable", type=game_Addition, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Addition70", type=game_Multipliable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left71: BinaryAssociation = BinaryAssociation(
    name="left71",
    ends={
        Property(name="game_Multipliable72", type=game_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Multiplication", type=game_Multipliable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right73: BinaryAssociation = BinaryAssociation(
    name="right73",
    ends={
        Property(name="game_Setable", type=game_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Multiplication74", type=game_Setable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left75: BinaryAssociation = BinaryAssociation(
    name="left75",
    ends={
        Property(name="game_Setable76", type=game_SetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="game_SetExpression", type=game_Setable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right77: BinaryAssociation = BinaryAssociation(
    name="right77",
    ends={
        Property(name="game_Primary", type=game_SetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="game_SetExpression78", type=game_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable92: BinaryAssociation = BinaryAssociation(
    name="variable92",
    ends={
        Property(name="game_ImplicitSet93", type=game_Variable, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="game_Variable94", type=game_ImplicitSet, multiplicity=Multiplicity(1, 1))
    }
)
index95: BinaryAssociation = BinaryAssociation(
    name="index95",
    ends={
        Property(name="game_Expression96", type=game_Atom, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Atom", type=game_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression84: BinaryAssociation = BinaryAssociation(
    name="expression84",
    ends={
        Property(name="game_Primary85", type=game_Cardinal, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Cardinal", type=game_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression86: BinaryAssociation = BinaryAssociation(
    name="expression86",
    ends={
        Property(name="game_Expression87", type=game_Brackets, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Brackets", type=game_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries88: BinaryAssociation = BinaryAssociation(
    name="entries88",
    ends={
        Property(name="game_Expression89", type=game_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Join", type=game_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predicate90: BinaryAssociation = BinaryAssociation(
    name="predicate90",
    ends={
        Property(name="game_Expression91", type=game_ImplicitSet, multiplicity=Multiplicity(1, 1)),
        Property(name="game_ImplicitSet", type=game_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atom97: BinaryAssociation = BinaryAssociation(
    name="atom97",
    ends={
        Property(name="game_Atom98", type=game_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Index", type=game_Atom, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression99: BinaryAssociation = BinaryAssociation(
    name="expression99",
    ends={
        Property(name="game_Expression101", type=game_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Index100", type=game_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity102: BinaryAssociation = BinaryAssociation(
    name="entity102",
    ends={
        Property(name="game_Variable103", type=game_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Cell", type=game_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
component104: BinaryAssociation = BinaryAssociation(
    name="component104",
    ends={
        Property(name="game_Variable106", type=game_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Cell105", type=game_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters108: BinaryAssociation = BinaryAssociation(
    name="parameters108",
    ends={
        Property(name="game_Type109", type=game_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="game_Type107", type=game_Type, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_game_Assignment_Statement = Generalization(general=Statement, specific=game_Assignment)
gen_game_Selection_Statement = Generalization(general=Statement, specific=game_Selection)
gen_game_Iteration_Statement = Generalization(general=Statement, specific=game_Iteration)
gen_game_Forall_Statement = Generalization(general=Statement, specific=game_Forall)
gen_game_Addable_Comparable = Generalization(general=Comparable, specific=game_Addable)
gen_game_Multipliable_Addable = Generalization(general=Addable, specific=game_Multipliable)
gen_game_Setable_Multipliable = Generalization(general=Multipliable, specific=game_Setable)
gen_game_Or_Orable = Generalization(general=Orable, specific=game_Or)
gen_game_Subprocess_Statement = Generalization(general=Statement, specific=game_Subprocess)
gen_game_Orable_Expression = Generalization(general=Expression, specific=game_Orable)
gen_game_Andable_Orable = Generalization(general=Orable, specific=game_Andable)
gen_game_Equatable_Andable = Generalization(general=Andable, specific=game_Equatable)
gen_game_Comparable_Equatable = Generalization(general=Equatable, specific=game_Comparable)
gen_game_Addition_Addable = Generalization(general=Addable, specific=game_Addition)
gen_game_And_Andable = Generalization(general=Andable, specific=game_And)
gen_game_Equality_Equatable = Generalization(general=Equatable, specific=game_Equality)
gen_game_Comparison_Comparable = Generalization(general=Comparable, specific=game_Comparison)
gen_game_LogicalNot_Primary = Generalization(general=Primary, specific=game_LogicalNot)
gen_game_Multiplication_Multipliable = Generalization(general=Multipliable, specific=game_Multiplication)
gen_game_SetExpression_Setable = Generalization(general=Setable, specific=game_SetExpression)
gen_game_Primary_Setable = Generalization(general=Setable, specific=game_Primary)
gen_game_Call_Primary = Generalization(general=Primary, specific=game_Call)
gen_game_Atom_Index = Generalization(general=Index, specific=game_Atom)
gen_game_Index_Primary = Generalization(general=Primary, specific=game_Index)
gen_game_Cardinal_Primary = Generalization(general=Primary, specific=game_Cardinal)
gen_game_Collection_Primary = Generalization(general=Primary, specific=game_Collection)
gen_game_Brackets_Collection = Generalization(general=Collection, specific=game_Brackets)
gen_game_Join_Collection = Generalization(general=Collection, specific=game_Join)
gen_game_ImplicitSet_Collection = Generalization(general=Collection, specific=game_ImplicitSet)
gen_game_Variable_Atom = Generalization(general=Atom, specific=game_Variable)
gen_game_Cell_Atom = Generalization(general=Atom, specific=game_Cell)

# Domain Model
domain_model = DomainModel(
    name="game",
    types={game_System, game_ComponentData, game_End, game_Game, game_Type, game_Access, game_Function, game_Statement, game_Query, game_Variable, game_Assignment, game_Selection, Statement, game_Expression, game_Iteration, game_Forall, game_Addable, Comparable, game_Multipliable, Addable, game_Setable, Multipliable, game_Or, game_Subprocess, game_Call, game_Orable, Expression, game_Andable, Orable, game_Equatable, Andable, game_Comparable, Equatable, game_Addition, game_And, game_Equality, game_Comparison, game_LogicalNot, game_Multiplication, game_SetExpression, Setable, game_Primary, Primary, game_Atom, Index, game_Index, game_Cardinal, game_Collection, game_Brackets, Collection, game_Join, game_ImplicitSet, Atom, game_Cell, EqualityKind, AccessKind, ComparisonKind, AdditiveKind, MultiplicativeKind},
    associations={types0, systems1, components3, end5, queries20, accesses22, functions7, type9, statements12, type14, statements17, condition36, statements38, variable41, condition24, positiveStatements25, negativeStatements28, condition31, statements33, left52, atom43, expression45, call48, type49, left63, right65, left67, right53, left55, right57, left59, right61, arguments79, expression82, right69, left71, right73, left75, right77, variable92, index95, expression84, expression86, entries88, predicate90, atom97, expression99, entity102, component104, parameters108},
    generalizations={gen_game_Assignment_Statement, gen_game_Selection_Statement, gen_game_Iteration_Statement, gen_game_Forall_Statement, gen_game_Addable_Comparable, gen_game_Multipliable_Addable, gen_game_Setable_Multipliable, gen_game_Or_Orable, gen_game_Subprocess_Statement, gen_game_Orable_Expression, gen_game_Andable_Orable, gen_game_Equatable_Andable, gen_game_Comparable_Equatable, gen_game_Addition_Addable, gen_game_And_Andable, gen_game_Equality_Equatable, gen_game_Comparison_Comparable, gen_game_LogicalNot_Primary, gen_game_Multiplication_Multipliable, gen_game_SetExpression_Setable, gen_game_Primary_Setable, gen_game_Call_Primary, gen_game_Atom_Index, gen_game_Index_Primary, gen_game_Cardinal_Primary, gen_game_Collection_Primary, gen_game_Brackets_Collection, gen_game_Join_Collection, gen_game_ImplicitSet_Collection, gen_game_Variable_Atom, gen_game_Cell_Atom},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)