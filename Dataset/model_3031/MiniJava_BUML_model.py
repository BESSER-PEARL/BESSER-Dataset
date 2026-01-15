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
miniJava_Class = Class(name="miniJava::Class")
miniJava_Identifier = Class(name="miniJava::Identifier")
miniJava_Program = Class(name="miniJava::Program")
miniJava_MainClass = Class(name="miniJava::MainClass")
miniJava_VariableDeclaration = Class(name="miniJava::VariableDeclaration")
miniJava_MethodDeclaration = Class(name="miniJava::MethodDeclaration")
miniJava_Statement = Class(name="miniJava::Statement")
miniJava_AbstactType = Class(name="miniJava::AbstactType")
miniJava_IntegerArrayType = Class(name="miniJava::IntegerArrayType")
AbstactType = Class(name="AbstactType")
miniJava_BooleanType = Class(name="miniJava::BooleanType")
miniJava_IntegerType = Class(name="miniJava::IntegerType")
miniJava_ClassifierType = Class(name="miniJava::ClassifierType")
miniJava_AbstractExpression = Class(name="miniJava::AbstractExpression")
miniJava_IfStatement = Class(name="miniJava::IfStatement")
miniJava_BlockStatement = Class(name="miniJava::BlockStatement")
Statement = Class(name="Statement")
miniJava_PrintLine = Class(name="miniJava::PrintLine")
miniJava_WhileLoop = Class(name="miniJava::WhileLoop")
miniJava_ArrayAssignment = Class(name="miniJava::ArrayAssignment")
miniJava_Assignment = Class(name="miniJava::Assignment")
miniJava_LessThen = Class(name="miniJava::LessThen")
miniJava_And = Class(name="miniJava::And")
AbstractExpression = Class(name="AbstractExpression")
miniJava_Minus = Class(name="miniJava::Minus")
miniJava_Plus = Class(name="miniJava::Plus")
miniJava_ArrayAccess = Class(name="miniJava::ArrayAccess")
miniJava_LengthOf = Class(name="miniJava::LengthOf")
miniJava_Multiply = Class(name="miniJava::Multiply")
miniJava_FunctionCall = Class(name="miniJava::FunctionCall")
miniJava_ClassifierReference = Class(name="miniJava::ClassifierReference")
miniJava_ThisReference = Class(name="miniJava::ThisReference")
miniJava_IntegerArrayConstruction = Class(name="miniJava::IntegerArrayConstruction")
miniJava_IntLiteral = Class(name="miniJava::IntLiteral")
miniJava_Boolean = Class(name="miniJava::Boolean")
miniJava_BlockExpression = Class(name="miniJava::BlockExpression")
miniJava_ClassConstruction = Class(name="miniJava::ClassConstruction")
miniJava_Negation = Class(name="miniJava::Negation")

# miniJava_Class class attributes and methods

# miniJava_Identifier class attributes and methods
miniJava_Identifier_value: Property = Property(name="value", type=StringType)
miniJava_Identifier.attributes={miniJava_Identifier_value}

# miniJava_Program class attributes and methods

# miniJava_MainClass class attributes and methods

# miniJava_VariableDeclaration class attributes and methods

# miniJava_MethodDeclaration class attributes and methods

# miniJava_Statement class attributes and methods

# miniJava_AbstactType class attributes and methods

# miniJava_IntegerArrayType class attributes and methods

# AbstactType class attributes and methods

# miniJava_BooleanType class attributes and methods

# miniJava_IntegerType class attributes and methods

# miniJava_ClassifierType class attributes and methods

# miniJava_AbstractExpression class attributes and methods

# miniJava_IfStatement class attributes and methods

# miniJava_BlockStatement class attributes and methods

# Statement class attributes and methods

# miniJava_PrintLine class attributes and methods

# miniJava_WhileLoop class attributes and methods

# miniJava_ArrayAssignment class attributes and methods

# miniJava_Assignment class attributes and methods

# miniJava_LessThen class attributes and methods

# miniJava_And class attributes and methods

# AbstractExpression class attributes and methods

# miniJava_Minus class attributes and methods

# miniJava_Plus class attributes and methods

# miniJava_ArrayAccess class attributes and methods

# miniJava_LengthOf class attributes and methods

# miniJava_Multiply class attributes and methods

# miniJava_FunctionCall class attributes and methods

# miniJava_ClassifierReference class attributes and methods

# miniJava_ThisReference class attributes and methods

# miniJava_IntegerArrayConstruction class attributes and methods

# miniJava_IntLiteral class attributes and methods
miniJava_IntLiteral_resultInt: Property = Property(name="resultInt", type=IntegerType)
miniJava_IntLiteral.attributes={miniJava_IntLiteral_resultInt}

# miniJava_Boolean class attributes and methods
miniJava_Boolean_result: Property = Property(name="result", type=BooleanType)
miniJava_Boolean.attributes={miniJava_Boolean_result}

# miniJava_BlockExpression class attributes and methods

# miniJava_ClassConstruction class attributes and methods

# miniJava_Negation class attributes and methods

# Relationships
classes1: BinaryAssociation = BinaryAssociation(
    name="classes1",
    ends={
        Property(name="miniJava_Class", type=miniJava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Program2", type=miniJava_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name3: BinaryAssociation = BinaryAssociation(
    name="name3",
    ends={
        Property(name="miniJava_Identifier", type=miniJava_MainClass, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MainClass4", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commandLineArguments5: BinaryAssociation = BinaryAssociation(
    name="commandLineArguments5",
    ends={
        Property(name="miniJava_Identifier7", type=miniJava_MainClass, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MainClass6", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mainClass0: BinaryAssociation = BinaryAssociation(
    name="mainClass0",
    ends={
        Property(name="miniJava_MainClass", type=miniJava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Program", type=miniJava_MainClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superClass13: BinaryAssociation = BinaryAssociation(
    name="superClass13",
    ends={
        Property(name="miniJava_Identifier15", type=miniJava_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Class14", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables16: BinaryAssociation = BinaryAssociation(
    name="variables16",
    ends={
        Property(name="miniJava_VariableDeclaration", type=miniJava_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Class17", type=miniJava_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods18: BinaryAssociation = BinaryAssociation(
    name="methods18",
    ends={
        Property(name="miniJava_MethodDeclaration", type=miniJava_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Class19", type=miniJava_MethodDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements8: BinaryAssociation = BinaryAssociation(
    name="statements8",
    ends={
        Property(name="miniJava_Statement", type=miniJava_MainClass, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MainClass9", type=miniJava_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name10: BinaryAssociation = BinaryAssociation(
    name="name10",
    ends={
        Property(name="miniJava_Identifier12", type=miniJava_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Class11", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType25: BinaryAssociation = BinaryAssociation(
    name="returnType25",
    ends={
        Property(name="miniJava_AbstactType27", type=miniJava_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodDeclaration26", type=miniJava_AbstactType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name28: BinaryAssociation = BinaryAssociation(
    name="name28",
    ends={
        Property(name="miniJava_Identifier30", type=miniJava_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodDeclaration29", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments31: BinaryAssociation = BinaryAssociation(
    name="arguments31",
    ends={
        Property(name="miniJava_VariableDeclaration33", type=miniJava_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodDeclaration32", type=miniJava_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables34: BinaryAssociation = BinaryAssociation(
    name="variables34",
    ends={
        Property(name="miniJava_VariableDeclaration36", type=miniJava_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodDeclaration35", type=miniJava_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type20: BinaryAssociation = BinaryAssociation(
    name="type20",
    ends={
        Property(name="miniJava_AbstactType", type=miniJava_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_VariableDeclaration21", type=miniJava_AbstactType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name22: BinaryAssociation = BinaryAssociation(
    name="name22",
    ends={
        Property(name="miniJava_Identifier24", type=miniJava_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_VariableDeclaration23", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements37: BinaryAssociation = BinaryAssociation(
    name="statements37",
    ends={
        Property(name="miniJava_Statement39", type=miniJava_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodDeclaration38", type=miniJava_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnStatement40: BinaryAssociation = BinaryAssociation(
    name="returnStatement40",
    ends={
        Property(name="miniJava_AbstractExpression", type=miniJava_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodDeclaration41", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements44: BinaryAssociation = BinaryAssociation(
    name="statements44",
    ends={
        Property(name="miniJava_Statement45", type=miniJava_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_BlockStatement", type=miniJava_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition46: BinaryAssociation = BinaryAssociation(
    name="condition46",
    ends={
        Property(name="miniJava_AbstractExpression47", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then48: BinaryAssociation = BinaryAssociation(
    name="then48",
    ends={
        Property(name="miniJava_Statement50", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement49", type=miniJava_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name42: BinaryAssociation = BinaryAssociation(
    name="name42",
    ends={
        Property(name="miniJava_Identifier43", type=miniJava_ClassifierType, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClassifierType", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
do56: BinaryAssociation = BinaryAssociation(
    name="do56",
    ends={
        Property(name="miniJava_Statement58", type=miniJava_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_WhileLoop57", type=miniJava_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
print59: BinaryAssociation = BinaryAssociation(
    name="print59",
    ends={
        Property(name="miniJava_AbstractExpression60", type=miniJava_PrintLine, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_PrintLine", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else51: BinaryAssociation = BinaryAssociation(
    name="else51",
    ends={
        Property(name="miniJava_Statement53", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement52", type=miniJava_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition54: BinaryAssociation = BinaryAssociation(
    name="condition54",
    ends={
        Property(name="miniJava_AbstractExpression55", type=miniJava_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_WhileLoop", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value63: BinaryAssociation = BinaryAssociation(
    name="value63",
    ends={
        Property(name="miniJava_AbstractExpression65", type=miniJava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Assignment64", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier66: BinaryAssociation = BinaryAssociation(
    name="identifier66",
    ends={
        Property(name="miniJava_Identifier67", type=miniJava_ArrayAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAssignment", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index68: BinaryAssociation = BinaryAssociation(
    name="index68",
    ends={
        Property(name="miniJava_AbstractExpression70", type=miniJava_ArrayAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAssignment69", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier61: BinaryAssociation = BinaryAssociation(
    name="identifier61",
    ends={
        Property(name="miniJava_Identifier62", type=miniJava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Assignment", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left74: BinaryAssociation = BinaryAssociation(
    name="left74",
    ends={
        Property(name="miniJava_And", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="miniJava_AbstractExpression75", type=miniJava_And, multiplicity=Multiplicity(1, 1))
    }
)
right76: BinaryAssociation = BinaryAssociation(
    name="right76",
    ends={
        Property(name="miniJava_AbstractExpression78", type=miniJava_And, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_And77", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left79: BinaryAssociation = BinaryAssociation(
    name="left79",
    ends={
        Property(name="miniJava_AbstractExpression80", type=miniJava_LessThen, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_LessThen", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right81: BinaryAssociation = BinaryAssociation(
    name="right81",
    ends={
        Property(name="miniJava_AbstractExpression83", type=miniJava_LessThen, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_LessThen82", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value71: BinaryAssociation = BinaryAssociation(
    name="value71",
    ends={
        Property(name="miniJava_AbstractExpression73", type=miniJava_ArrayAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAssignment72", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right86: BinaryAssociation = BinaryAssociation(
    name="right86",
    ends={
        Property(name="miniJava_AbstractExpression88", type=miniJava_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Plus87", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left89: BinaryAssociation = BinaryAssociation(
    name="left89",
    ends={
        Property(name="miniJava_AbstractExpression90", type=miniJava_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Minus", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right91: BinaryAssociation = BinaryAssociation(
    name="right91",
    ends={
        Property(name="miniJava_AbstractExpression93", type=miniJava_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Minus92", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left84: BinaryAssociation = BinaryAssociation(
    name="left84",
    ends={
        Property(name="miniJava_AbstractExpression85", type=miniJava_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Plus", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right96: BinaryAssociation = BinaryAssociation(
    name="right96",
    ends={
        Property(name="miniJava_AbstractExpression98", type=miniJava_Multiply, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Multiply97", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array99: BinaryAssociation = BinaryAssociation(
    name="array99",
    ends={
        Property(name="miniJava_AbstractExpression100", type=miniJava_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAccess", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index101: BinaryAssociation = BinaryAssociation(
    name="index101",
    ends={
        Property(name="miniJava_AbstractExpression103", type=miniJava_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAccess102", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left94: BinaryAssociation = BinaryAssociation(
    name="left94",
    ends={
        Property(name="miniJava_AbstractExpression95", type=miniJava_Multiply, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Multiply", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
on106: BinaryAssociation = BinaryAssociation(
    name="on106",
    ends={
        Property(name="miniJava_AbstractExpression107", type=miniJava_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FunctionCall", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function108: BinaryAssociation = BinaryAssociation(
    name="function108",
    ends={
        Property(name="miniJava_Identifier110", type=miniJava_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FunctionCall109", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments111: BinaryAssociation = BinaryAssociation(
    name="arguments111",
    ends={
        Property(name="miniJava_AbstractExpression113", type=miniJava_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FunctionCall112", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value104: BinaryAssociation = BinaryAssociation(
    name="value104",
    ends={
        Property(name="miniJava_AbstractExpression105", type=miniJava_LengthOf, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_LengthOf", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referenceTo114: BinaryAssociation = BinaryAssociation(
    name="referenceTo114",
    ends={
        Property(name="miniJava_Identifier115", type=miniJava_ClassifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClassifierReference", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultSubExpression122: BinaryAssociation = BinaryAssociation(
    name="resultSubExpression122",
    ends={
        Property(name="miniJava_AbstractExpression123", type=miniJava_BlockExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_BlockExpression", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sizeExpression116: BinaryAssociation = BinaryAssociation(
    name="sizeExpression116",
    ends={
        Property(name="miniJava_AbstractExpression117", type=miniJava_IntegerArrayConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IntegerArrayConstruction", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class118: BinaryAssociation = BinaryAssociation(
    name="class118",
    ends={
        Property(name="miniJava_Identifier119", type=miniJava_ClassConstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClassConstruction", type=miniJava_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
not120: BinaryAssociation = BinaryAssociation(
    name="not120",
    ends={
        Property(name="miniJava_AbstractExpression121", type=miniJava_Negation, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Negation", type=miniJava_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_miniJava_IntegerArrayType_AbstactType = Generalization(general=AbstactType, specific=miniJava_IntegerArrayType)
gen_miniJava_BooleanType_AbstactType = Generalization(general=AbstactType, specific=miniJava_BooleanType)
gen_miniJava_IntegerType_AbstactType = Generalization(general=AbstactType, specific=miniJava_IntegerType)
gen_miniJava_ClassifierType_AbstactType = Generalization(general=AbstactType, specific=miniJava_ClassifierType)
gen_miniJava_IfStatement_Statement = Generalization(general=Statement, specific=miniJava_IfStatement)
gen_miniJava_BlockStatement_Statement = Generalization(general=Statement, specific=miniJava_BlockStatement)
gen_miniJava_PrintLine_Statement = Generalization(general=Statement, specific=miniJava_PrintLine)
gen_miniJava_WhileLoop_Statement = Generalization(general=Statement, specific=miniJava_WhileLoop)
gen_miniJava_ArrayAssignment_Statement = Generalization(general=Statement, specific=miniJava_ArrayAssignment)
gen_miniJava_Assignment_Statement = Generalization(general=Statement, specific=miniJava_Assignment)
gen_miniJava_LessThen_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_LessThen)
gen_miniJava_And_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_And)
gen_miniJava_Minus_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_Minus)
gen_miniJava_Plus_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_Plus)
gen_miniJava_ArrayAccess_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_ArrayAccess)
gen_miniJava_Multiply_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_Multiply)
gen_miniJava_FunctionCall_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_FunctionCall)
gen_miniJava_LengthOf_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_LengthOf)
gen_miniJava_ClassifierReference_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_ClassifierReference)
gen_miniJava_ThisReference_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_ThisReference)
gen_miniJava_IntegerArrayConstruction_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_IntegerArrayConstruction)
gen_miniJava_IntLiteral_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_IntLiteral)
gen_miniJava_Boolean_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_Boolean)
gen_miniJava_BlockExpression_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_BlockExpression)
gen_miniJava_ClassConstruction_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_ClassConstruction)
gen_miniJava_Negation_AbstractExpression = Generalization(general=AbstractExpression, specific=miniJava_Negation)

# Domain Model
domain_model = DomainModel(
    name="miniJava",
    types={miniJava_Class, miniJava_Identifier, miniJava_Program, miniJava_MainClass, miniJava_VariableDeclaration, miniJava_MethodDeclaration, miniJava_Statement, miniJava_AbstactType, miniJava_IntegerArrayType, AbstactType, miniJava_BooleanType, miniJava_IntegerType, miniJava_ClassifierType, miniJava_AbstractExpression, miniJava_IfStatement, miniJava_BlockStatement, Statement, miniJava_PrintLine, miniJava_WhileLoop, miniJava_ArrayAssignment, miniJava_Assignment, miniJava_LessThen, miniJava_And, AbstractExpression, miniJava_Minus, miniJava_Plus, miniJava_ArrayAccess, miniJava_LengthOf, miniJava_Multiply, miniJava_FunctionCall, miniJava_ClassifierReference, miniJava_ThisReference, miniJava_IntegerArrayConstruction, miniJava_IntLiteral, miniJava_Boolean, miniJava_BlockExpression, miniJava_ClassConstruction, miniJava_Negation},
    associations={classes1, name3, commandLineArguments5, mainClass0, superClass13, variables16, methods18, statements8, name10, returnType25, name28, arguments31, variables34, type20, name22, statements37, returnStatement40, statements44, condition46, then48, name42, do56, print59, else51, condition54, value63, identifier66, index68, identifier61, left74, right76, left79, right81, value71, right86, left89, right91, left84, right96, array99, index101, left94, on106, function108, arguments111, value104, referenceTo114, resultSubExpression122, sizeExpression116, class118, not120},
    generalizations={gen_miniJava_IntegerArrayType_AbstactType, gen_miniJava_BooleanType_AbstactType, gen_miniJava_IntegerType_AbstactType, gen_miniJava_ClassifierType_AbstactType, gen_miniJava_IfStatement_Statement, gen_miniJava_BlockStatement_Statement, gen_miniJava_PrintLine_Statement, gen_miniJava_WhileLoop_Statement, gen_miniJava_ArrayAssignment_Statement, gen_miniJava_Assignment_Statement, gen_miniJava_LessThen_AbstractExpression, gen_miniJava_And_AbstractExpression, gen_miniJava_Minus_AbstractExpression, gen_miniJava_Plus_AbstractExpression, gen_miniJava_ArrayAccess_AbstractExpression, gen_miniJava_Multiply_AbstractExpression, gen_miniJava_FunctionCall_AbstractExpression, gen_miniJava_LengthOf_AbstractExpression, gen_miniJava_ClassifierReference_AbstractExpression, gen_miniJava_ThisReference_AbstractExpression, gen_miniJava_IntegerArrayConstruction_AbstractExpression, gen_miniJava_IntLiteral_AbstractExpression, gen_miniJava_Boolean_AbstractExpression, gen_miniJava_BlockExpression_AbstractExpression, gen_miniJava_ClassConstruction_AbstractExpression, gen_miniJava_Negation_AbstractExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)