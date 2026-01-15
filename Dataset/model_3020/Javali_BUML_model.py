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
javali_Record = Class(name="javali::Record")
javali_Procedure = Class(name="javali::Procedure")
javali_Type = Class(name="javali::Type")
javali_Identifier = Class(name="javali::Identifier")
javali_Literal = Class(name="javali::Literal")
javali_Module = Class(name="javali::Module")
javali_Constant = Class(name="javali::Constant")
javali_Block = Class(name="javali::Block")
javali_Statement = Class(name="javali::Statement")
javali_Return = Class(name="javali::Return")
Statement = Class(name="Statement")
javali_Expression = Class(name="javali::Expression")
javali_VarDeclaration = Class(name="javali::VarDeclaration")
javali_VarAssign = Class(name="javali::VarAssign")
javali_VarExpression = Class(name="javali::VarExpression")
javali_IfElse = Class(name="javali::IfElse")
javali_While = Class(name="javali::While")
javali_Break = Class(name="javali::Break")
javali_Continue = Class(name="javali::Continue")
javali_DoWhile = Class(name="javali::DoWhile")
javali_Increment = Class(name="javali::Increment")
javali_Decrement = Class(name="javali::Decrement")
javali_For = Class(name="javali::For")
javali_ProcCall = Class(name="javali::ProcCall")
javali_NewArray = Class(name="javali::NewArray")
Expression = Class(name="Expression")
javali_Null = Class(name="javali::Null")
javali_Xor = Class(name="javali::Xor")
javali_And = Class(name="javali::And")
javali_NewObject = Class(name="javali::NewObject")
javali_Or = Class(name="javali::Or")
javali_Addition = Class(name="javali::Addition")
javali_Multiplication = Class(name="javali::Multiplication")
javali_Equality = Class(name="javali::Equality")
javali_Relation = Class(name="javali::Relation")

# javali_Record class attributes and methods

# javali_Procedure class attributes and methods
javali_Procedure_void: Property = Property(name="void", type=BooleanType)
javali_Procedure_comment: Property = Property(name="comment", type=StringType)
javali_Procedure_static: Property = Property(name="static", type=BooleanType)
javali_Procedure.attributes={javali_Procedure_static, javali_Procedure_void, javali_Procedure_comment}

# javali_Type class attributes and methods
javali_Type_arrayDims: Property = Property(name="arrayDims", type=StringType)
javali_Type.attributes={javali_Type_arrayDims}

# javali_Identifier class attributes and methods
javali_Identifier_id: Property = Property(name="id", type=StringType)
javali_Identifier.attributes={javali_Identifier_id}

# javali_Literal class attributes and methods
javali_Literal_value: Property = Property(name="value", type=StringType)
javali_Literal.attributes={javali_Literal_value}

# javali_Module class attributes and methods

# javali_Constant class attributes and methods
javali_Constant_static: Property = Property(name="static", type=BooleanType)
javali_Constant.attributes={javali_Constant_static}

# javali_Block class attributes and methods

# javali_Statement class attributes and methods

# javali_Return class attributes and methods

# Statement class attributes and methods

# javali_Expression class attributes and methods

# javali_VarDeclaration class attributes and methods

# javali_VarAssign class attributes and methods

# javali_VarExpression class attributes and methods

# javali_IfElse class attributes and methods

# javali_While class attributes and methods

# javali_Break class attributes and methods

# javali_Continue class attributes and methods

# javali_DoWhile class attributes and methods

# javali_Increment class attributes and methods

# javali_Decrement class attributes and methods

# javali_For class attributes and methods

# javali_ProcCall class attributes and methods

# javali_NewArray class attributes and methods

# Expression class attributes and methods

# javali_Null class attributes and methods

# javali_Xor class attributes and methods

# javali_And class attributes and methods

# javali_NewObject class attributes and methods

# javali_Or class attributes and methods

# javali_Addition class attributes and methods
javali_Addition_operator: Property = Property(name="operator", type=StringType)
javali_Addition.attributes={javali_Addition_operator}

# javali_Multiplication class attributes and methods
javali_Multiplication_operator: Property = Property(name="operator", type=StringType)
javali_Multiplication.attributes={javali_Multiplication_operator}

# javali_Equality class attributes and methods
javali_Equality_operator: Property = Property(name="operator", type=StringType)
javali_Equality.attributes={javali_Equality_operator}

# javali_Relation class attributes and methods
javali_Relation_operator: Property = Property(name="operator", type=StringType)
javali_Relation.attributes={javali_Relation_operator}

# Relationships
records1: BinaryAssociation = BinaryAssociation(
    name="records1",
    ends={
        Property(name="javali_Record", type=javali_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Module2", type=javali_Record, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures3: BinaryAssociation = BinaryAssociation(
    name="procedures3",
    ends={
        Property(name="javali_Procedure", type=javali_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Module4", type=javali_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="javali_Type", type=javali_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Constant6", type=javali_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id7: BinaryAssociation = BinaryAssociation(
    name="id7",
    ends={
        Property(name="javali_Identifier", type=javali_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Constant8", type=javali_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value9: BinaryAssociation = BinaryAssociation(
    name="value9",
    ends={
        Property(name="javali_Literal", type=javali_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Constant10", type=javali_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constants0: BinaryAssociation = BinaryAssociation(
    name="constants0",
    ends={
        Property(name="javali_Constant", type=javali_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Module", type=javali_Constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id19: BinaryAssociation = BinaryAssociation(
    name="id19",
    ends={
        Property(name="javali_Identifier21", type=javali_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Procedure20", type=javali_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params22: BinaryAssociation = BinaryAssociation(
    name="params22",
    ends={
        Property(name="javali_VarDeclaration24", type=javali_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Procedure23", type=javali_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body25: BinaryAssociation = BinaryAssociation(
    name="body25",
    ends={
        Property(name="javali_Block", type=javali_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Procedure26", type=javali_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements27: BinaryAssociation = BinaryAssociation(
    name="statements27",
    ends={
        Property(name="javali_Statement", type=javali_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Block28", type=javali_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp29: BinaryAssociation = BinaryAssociation(
    name="exp29",
    ends={
        Property(name="javali_Expression", type=javali_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Return", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id11: BinaryAssociation = BinaryAssociation(
    name="id11",
    ends={
        Property(name="javali_Identifier13", type=javali_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Record12", type=javali_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields14: BinaryAssociation = BinaryAssociation(
    name="fields14",
    ends={
        Property(name="javali_VarDeclaration", type=javali_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Record15", type=javali_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
retType16: BinaryAssociation = BinaryAssociation(
    name="retType16",
    ends={
        Property(name="javali_Type18", type=javali_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Procedure17", type=javali_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var39: BinaryAssociation = BinaryAssociation(
    name="var39",
    ends={
        Property(name="javali_VarExpression", type=javali_VarAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_VarAssign", type=javali_VarExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp40: BinaryAssociation = BinaryAssociation(
    name="exp40",
    ends={
        Property(name="javali_Expression42", type=javali_VarAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_VarAssign41", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard43: BinaryAssociation = BinaryAssociation(
    name="guard43",
    ends={
        Property(name="javali_Expression44", type=javali_IfElse, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_IfElse", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectionBlock45: BinaryAssociation = BinaryAssociation(
    name="selectionBlock45",
    ends={
        Property(name="javali_Block47", type=javali_IfElse, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_IfElse46", type=javali_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alternativeBlock48: BinaryAssociation = BinaryAssociation(
    name="alternativeBlock48",
    ends={
        Property(name="javali_Block50", type=javali_IfElse, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_IfElse49", type=javali_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type30: BinaryAssociation = BinaryAssociation(
    name="type30",
    ends={
        Property(name="javali_Type32", type=javali_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_VarDeclaration31", type=javali_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id33: BinaryAssociation = BinaryAssociation(
    name="id33",
    ends={
        Property(name="javali_Identifier35", type=javali_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_VarDeclaration34", type=javali_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init36: BinaryAssociation = BinaryAssociation(
    name="init36",
    ends={
        Property(name="javali_Expression38", type=javali_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_VarDeclaration37", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
progressStatements61: BinaryAssociation = BinaryAssociation(
    name="progressStatements61",
    ends={
        Property(name="javali_Statement63", type=javali_For, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_For62", type=javali_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block64: BinaryAssociation = BinaryAssociation(
    name="block64",
    ends={
        Property(name="javali_Block66", type=javali_For, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_For65", type=javali_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block67: BinaryAssociation = BinaryAssociation(
    name="block67",
    ends={
        Property(name="javali_Block68", type=javali_DoWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_DoWhile", type=javali_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard69: BinaryAssociation = BinaryAssociation(
    name="guard69",
    ends={
        Property(name="javali_Expression71", type=javali_DoWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_DoWhile70", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id72: BinaryAssociation = BinaryAssociation(
    name="id72",
    ends={
        Property(name="javali_Identifier73", type=javali_Increment, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Increment", type=javali_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard51: BinaryAssociation = BinaryAssociation(
    name="guard51",
    ends={
        Property(name="javali_Expression52", type=javali_While, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_While", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block53: BinaryAssociation = BinaryAssociation(
    name="block53",
    ends={
        Property(name="javali_Block55", type=javali_While, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_While54", type=javali_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initStatements56: BinaryAssociation = BinaryAssociation(
    name="initStatements56",
    ends={
        Property(name="javali_Statement57", type=javali_For, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_For", type=javali_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard58: BinaryAssociation = BinaryAssociation(
    name="guard58",
    ends={
        Property(name="javali_Expression60", type=javali_For, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_For59", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayIndexes79: BinaryAssociation = BinaryAssociation(
    name="arrayIndexes79",
    ends={
        Property(name="javali_Expression81", type=javali_VarExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_VarExpression80", type=javali_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id82: BinaryAssociation = BinaryAssociation(
    name="id82",
    ends={
        Property(name="javali_Identifier83", type=javali_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_ProcCall", type=javali_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args84: BinaryAssociation = BinaryAssociation(
    name="args84",
    ends={
        Property(name="javali_Expression86", type=javali_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_ProcCall85", type=javali_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id87: BinaryAssociation = BinaryAssociation(
    name="id87",
    ends={
        Property(name="javali_Identifier89", type=javali_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Type88", type=javali_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id74: BinaryAssociation = BinaryAssociation(
    name="id74",
    ends={
        Property(name="javali_Identifier75", type=javali_Decrement, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Decrement", type=javali_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts76: BinaryAssociation = BinaryAssociation(
    name="parts76",
    ends={
        Property(name="javali_Identifier78", type=javali_VarExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_VarExpression77", type=javali_Identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left97: BinaryAssociation = BinaryAssociation(
    name="left97",
    ends={
        Property(name="javali_Expression98", type=javali_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Or", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right99: BinaryAssociation = BinaryAssociation(
    name="right99",
    ends={
        Property(name="javali_Expression101", type=javali_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Or100", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left102: BinaryAssociation = BinaryAssociation(
    name="left102",
    ends={
        Property(name="javali_Expression103", type=javali_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Xor", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right104: BinaryAssociation = BinaryAssociation(
    name="right104",
    ends={
        Property(name="javali_Expression106", type=javali_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Xor105", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left107: BinaryAssociation = BinaryAssociation(
    name="left107",
    ends={
        Property(name="javali_Expression108", type=javali_And, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_And", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type90: BinaryAssociation = BinaryAssociation(
    name="type90",
    ends={
        Property(name="javali_Identifier91", type=javali_NewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_NewArray", type=javali_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayDims92: BinaryAssociation = BinaryAssociation(
    name="arrayDims92",
    ends={
        Property(name="javali_Expression94", type=javali_NewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_NewArray93", type=javali_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type95: BinaryAssociation = BinaryAssociation(
    name="type95",
    ends={
        Property(name="javali_Identifier96", type=javali_NewObject, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_NewObject", type=javali_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left117: BinaryAssociation = BinaryAssociation(
    name="left117",
    ends={
        Property(name="javali_Expression118", type=javali_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Relation", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right119: BinaryAssociation = BinaryAssociation(
    name="right119",
    ends={
        Property(name="javali_Expression121", type=javali_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Relation120", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left122: BinaryAssociation = BinaryAssociation(
    name="left122",
    ends={
        Property(name="javali_Expression123", type=javali_Addition, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Addition", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right124: BinaryAssociation = BinaryAssociation(
    name="right124",
    ends={
        Property(name="javali_Expression126", type=javali_Addition, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Addition125", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right109: BinaryAssociation = BinaryAssociation(
    name="right109",
    ends={
        Property(name="javali_Expression111", type=javali_And, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_And110", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left112: BinaryAssociation = BinaryAssociation(
    name="left112",
    ends={
        Property(name="javali_Expression113", type=javali_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Equality", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right114: BinaryAssociation = BinaryAssociation(
    name="right114",
    ends={
        Property(name="javali_Expression116", type=javali_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Equality115", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left127: BinaryAssociation = BinaryAssociation(
    name="left127",
    ends={
        Property(name="javali_Expression128", type=javali_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Multiplication", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right129: BinaryAssociation = BinaryAssociation(
    name="right129",
    ends={
        Property(name="javali_Expression131", type=javali_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="javali_Multiplication130", type=javali_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_javali_Return_Statement = Generalization(general=Statement, specific=javali_Return)
gen_javali_VarAssign_Statement = Generalization(general=Statement, specific=javali_VarAssign)
gen_javali_IfElse_Statement = Generalization(general=Statement, specific=javali_IfElse)
gen_javali_While_Statement = Generalization(general=Statement, specific=javali_While)
gen_javali_Break_Statement = Generalization(general=Statement, specific=javali_Break)
gen_javali_Continue_Statement = Generalization(general=Statement, specific=javali_Continue)
gen_javali_VarDeclaration_Statement = Generalization(general=Statement, specific=javali_VarDeclaration)
gen_javali_DoWhile_Statement = Generalization(general=Statement, specific=javali_DoWhile)
gen_javali_Increment_Statement = Generalization(general=Statement, specific=javali_Increment)
gen_javali_Decrement_Statement = Generalization(general=Statement, specific=javali_Decrement)
gen_javali_For_Statement = Generalization(general=Statement, specific=javali_For)
gen_javali_ProcCall_Statement = Generalization(general=Statement, specific=javali_ProcCall)
gen_javali_ProcCall_Expression = Generalization(general=Expression, specific=javali_ProcCall)
gen_javali_NewArray_Expression = Generalization(general=Expression, specific=javali_NewArray)
gen_javali_Literal_Expression = Generalization(general=Expression, specific=javali_Literal)
gen_javali_Null_Expression = Generalization(general=Expression, specific=javali_Null)
gen_javali_VarExpression_Expression = Generalization(general=Expression, specific=javali_VarExpression)
gen_javali_Or_Expression = Generalization(general=Expression, specific=javali_Or)
gen_javali_Xor_Expression = Generalization(general=Expression, specific=javali_Xor)
gen_javali_And_Expression = Generalization(general=Expression, specific=javali_And)
gen_javali_NewObject_Expression = Generalization(general=Expression, specific=javali_NewObject)
gen_javali_Relation_Expression = Generalization(general=Expression, specific=javali_Relation)
gen_javali_Addition_Expression = Generalization(general=Expression, specific=javali_Addition)
gen_javali_Multiplication_Expression = Generalization(general=Expression, specific=javali_Multiplication)
gen_javali_Equality_Expression = Generalization(general=Expression, specific=javali_Equality)

# Domain Model
domain_model = DomainModel(
    name="javali",
    types={javali_Record, javali_Procedure, javali_Type, javali_Identifier, javali_Literal, javali_Module, javali_Constant, javali_Block, javali_Statement, javali_Return, Statement, javali_Expression, javali_VarDeclaration, javali_VarAssign, javali_VarExpression, javali_IfElse, javali_While, javali_Break, javali_Continue, javali_DoWhile, javali_Increment, javali_Decrement, javali_For, javali_ProcCall, javali_NewArray, Expression, javali_Null, javali_Xor, javali_And, javali_NewObject, javali_Or, javali_Addition, javali_Multiplication, javali_Equality, javali_Relation},
    associations={records1, procedures3, type5, id7, value9, constants0, id19, params22, body25, statements27, exp29, id11, fields14, retType16, var39, exp40, guard43, selectionBlock45, alternativeBlock48, type30, id33, init36, progressStatements61, block64, block67, guard69, id72, guard51, block53, initStatements56, guard58, arrayIndexes79, id82, args84, id87, id74, parts76, left97, right99, left102, right104, left107, type90, arrayDims92, type95, left117, right119, left122, right124, right109, left112, right114, left127, right129},
    generalizations={gen_javali_Return_Statement, gen_javali_VarAssign_Statement, gen_javali_IfElse_Statement, gen_javali_While_Statement, gen_javali_Break_Statement, gen_javali_Continue_Statement, gen_javali_VarDeclaration_Statement, gen_javali_DoWhile_Statement, gen_javali_Increment_Statement, gen_javali_Decrement_Statement, gen_javali_For_Statement, gen_javali_ProcCall_Statement, gen_javali_ProcCall_Expression, gen_javali_NewArray_Expression, gen_javali_Literal_Expression, gen_javali_Null_Expression, gen_javali_VarExpression_Expression, gen_javali_Or_Expression, gen_javali_Xor_Expression, gen_javali_And_Expression, gen_javali_NewObject_Expression, gen_javali_Relation_Expression, gen_javali_Addition_Expression, gen_javali_Multiplication_Expression, gen_javali_Equality_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)