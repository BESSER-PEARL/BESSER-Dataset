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
expression_Model = Class(name="expression::Model")
expression_Phrase = Class(name="expression::Phrase")
expression_StatementList = Class(name="expression::StatementList")
Phrase = Class(name="Phrase")
expression_Statement = Class(name="expression::Statement")
expression_AssignmentStatement = Class(name="expression::AssignmentStatement")
Statement = Class(name="Statement")
expression_Expression = Class(name="expression::Expression")
expression_VariableAssignmentStatement = Class(name="expression::VariableAssignmentStatement")
AssignmentStatement = Class(name="AssignmentStatement")
expression_Designator = Class(name="expression::Designator")
expression_SelfAssignmentStatement = Class(name="expression::SelfAssignmentStatement")
ExpressionRest = Class(name="ExpressionRest")
expression_FunctionCall = Class(name="expression::FunctionCall")
Expression = Class(name="Expression")
Function = Class(name="Function")
expression_ExpressionList = Class(name="expression::ExpressionList")
expression_ProcedureCall = Class(name="expression::ProcedureCall")
expression_Procedure = Class(name="expression::Procedure")
expression_ExpressionRest = Class(name="expression::ExpressionRest")
expression_KeyValuePair = Class(name="expression::KeyValuePair")
KeyValuePairRest = Class(name="KeyValuePairRest")
expression_KeyValuePairRest = Class(name="expression::KeyValuePairRest")
expression_Term = Class(name="expression::Term")
expression_List = Class(name="expression::List")
Term = Class(name="Term")
expression_EObject = Class(name="expression::EObject")
expression_OrExpression = Class(name="expression::OrExpression")
expression_AndExpression = Class(name="expression::AndExpression")
expression_EqualityExpression = Class(name="expression::EqualityExpression")
expression_DashExpression = Class(name="expression::DashExpression")
expression_PointExpression = Class(name="expression::PointExpression")
expression_PowExpression = Class(name="expression::PowExpression")
expression_QualifierExpression = Class(name="expression::QualifierExpression")
expression_ThereIsIn = Class(name="expression::ThereIsIn")
expression_ForallIn = Class(name="expression::ForallIn")
expression_FirstIn = Class(name="expression::FirstIn")
expression_LastIn = Class(name="expression::LastIn")
expression_Count = Class(name="expression::Count")
expression_Reduce = Class(name="expression::Reduce")
expression_Sum = Class(name="expression::Sum")
expression_Map = Class(name="expression::Map")
expression_Apply = Class(name="expression::Apply")
expression_UnaryExpression = Class(name="expression::UnaryExpression")
expression_StructureExpression = Class(name="expression::StructureExpression")
expression_StringValue = Class(name="expression::StringValue")
expression_IntegerValue = Class(name="expression::IntegerValue")
expression_DoubleValue = Class(name="expression::DoubleValue")

# expression_Model class attributes and methods

# expression_Phrase class attributes and methods

# expression_StatementList class attributes and methods

# Phrase class attributes and methods

# expression_Statement class attributes and methods

# expression_AssignmentStatement class attributes and methods

# Statement class attributes and methods

# expression_Expression class attributes and methods

# expression_VariableAssignmentStatement class attributes and methods

# AssignmentStatement class attributes and methods

# expression_Designator class attributes and methods

# expression_SelfAssignmentStatement class attributes and methods

# ExpressionRest class attributes and methods

# expression_FunctionCall class attributes and methods

# Expression class attributes and methods

# Function class attributes and methods

# expression_ExpressionList class attributes and methods

# expression_ProcedureCall class attributes and methods

# expression_Procedure class attributes and methods

# expression_ExpressionRest class attributes and methods

# expression_KeyValuePair class attributes and methods
expression_KeyValuePair_key: Property = Property(name="key", type=StringType)
expression_KeyValuePair.attributes={expression_KeyValuePair_key}

# KeyValuePairRest class attributes and methods

# expression_KeyValuePairRest class attributes and methods

# expression_Term class attributes and methods

# expression_List class attributes and methods

# Term class attributes and methods

# expression_EObject class attributes and methods

# expression_OrExpression class attributes and methods
expression_OrExpression_op: Property = Property(name="op", type=StringType)
expression_OrExpression.attributes={expression_OrExpression_op}

# expression_AndExpression class attributes and methods
expression_AndExpression_op: Property = Property(name="op", type=StringType)
expression_AndExpression.attributes={expression_AndExpression_op}

# expression_EqualityExpression class attributes and methods
expression_EqualityExpression_op: Property = Property(name="op", type=StringType)
expression_EqualityExpression.attributes={expression_EqualityExpression_op}

# expression_DashExpression class attributes and methods
expression_DashExpression_op: Property = Property(name="op", type=StringType)
expression_DashExpression.attributes={expression_DashExpression_op}

# expression_PointExpression class attributes and methods
expression_PointExpression_op: Property = Property(name="op", type=StringType)
expression_PointExpression.attributes={expression_PointExpression_op}

# expression_PowExpression class attributes and methods
expression_PowExpression_op: Property = Property(name="op", type=StringType)
expression_PowExpression.attributes={expression_PowExpression_op}

# expression_QualifierExpression class attributes and methods
expression_QualifierExpression_op: Property = Property(name="op", type=StringType)
expression_QualifierExpression.attributes={expression_QualifierExpression_op}

# expression_ThereIsIn class attributes and methods

# expression_ForallIn class attributes and methods

# expression_FirstIn class attributes and methods

# expression_LastIn class attributes and methods

# expression_Count class attributes and methods

# expression_Reduce class attributes and methods

# expression_Sum class attributes and methods

# expression_Map class attributes and methods

# expression_Apply class attributes and methods

# expression_UnaryExpression class attributes and methods

# expression_StructureExpression class attributes and methods

# expression_StringValue class attributes and methods
expression_StringValue_value: Property = Property(name="value", type=StringType)
expression_StringValue.attributes={expression_StringValue_value}

# expression_IntegerValue class attributes and methods
expression_IntegerValue_value: Property = Property(name="value", type=IntegerType)
expression_IntegerValue.attributes={expression_IntegerValue_value}

# expression_DoubleValue class attributes and methods
expression_DoubleValue_value: Property = Property(name="value", type=FloatType)
expression_DoubleValue.attributes={expression_DoubleValue_value}

# Relationships
phrase0: BinaryAssociation = BinaryAssociation(
    name="phrase0",
    ends={
        Property(name="expression_Phrase", type=expression_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Model", type=expression_Phrase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
head1: BinaryAssociation = BinaryAssociation(
    name="head1",
    ends={
        Property(name="expression_Statement", type=expression_StatementList, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_StatementList", type=expression_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tail3: BinaryAssociation = BinaryAssociation(
    name="tail3",
    ends={
        Property(name="expression_StatementList4", type=expression_StatementList, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_StatementList2", type=expression_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression5: BinaryAssociation = BinaryAssociation(
    name="expression5",
    ends={
        Property(name="expression_Expression", type=expression_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_AssignmentStatement", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator6: BinaryAssociation = BinaryAssociation(
    name="designator6",
    ends={
        Property(name="expression_Designator", type=expression_VariableAssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_VariableAssignmentStatement", type=expression_Designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition8: BinaryAssociation = BinaryAssociation(
    name="condition8",
    ends={
        Property(name="expression_Expression9", type=expression_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Expression7", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function10: BinaryAssociation = BinaryAssociation(
    name="function10",
    ends={
        Property(name="Function", type=expression_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_FunctionCall", type=Function, multiplicity=Multiplicity(0, 1))
    }
)
params11: BinaryAssociation = BinaryAssociation(
    name="params11",
    ends={
        Property(name="expression_ExpressionList", type=expression_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_FunctionCall12", type=expression_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure13: BinaryAssociation = BinaryAssociation(
    name="procedure13",
    ends={
        Property(name="expression_Procedure", type=expression_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ProcedureCall", type=expression_Procedure, multiplicity=Multiplicity(0, 1))
    }
)
params14: BinaryAssociation = BinaryAssociation(
    name="params14",
    ends={
        Property(name="expression_ExpressionList16", type=expression_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ProcedureCall15", type=expression_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
head17: BinaryAssociation = BinaryAssociation(
    name="head17",
    ends={
        Property(name="expression_Expression19", type=expression_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ExpressionList18", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tail20: BinaryAssociation = BinaryAssociation(
    name="tail20",
    ends={
        Property(name="expression_ExpressionRest", type=expression_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ExpressionList21", type=expression_ExpressionRest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value22: BinaryAssociation = BinaryAssociation(
    name="value22",
    ends={
        Property(name="expression_Expression23", type=expression_KeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_KeyValuePair", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest24: BinaryAssociation = BinaryAssociation(
    name="rest24",
    ends={
        Property(name="expression_KeyValuePairRest", type=expression_KeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_KeyValuePair25", type=expression_KeyValuePairRest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredExpression26: BinaryAssociation = BinaryAssociation(
    name="structuredExpression26",
    ends={
        Property(name="expression_Expression27", type=expression_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Term", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms28: BinaryAssociation = BinaryAssociation(
    name="terms28",
    ends={
        Property(name="expression_Term29", type=expression_List, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_List", type=expression_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value30: BinaryAssociation = BinaryAssociation(
    name="value30",
    ends={
        Property(name="expression_EObject", type=expression_Designator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Designator31", type=expression_EObject, multiplicity=Multiplicity(0, 1))
    }
)
left32: BinaryAssociation = BinaryAssociation(
    name="left32",
    ends={
        Property(name="expression_Expression33", type=expression_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_OrExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right34: BinaryAssociation = BinaryAssociation(
    name="right34",
    ends={
        Property(name="expression_Expression36", type=expression_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_OrExpression35", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left37: BinaryAssociation = BinaryAssociation(
    name="left37",
    ends={
        Property(name="expression_Expression38", type=expression_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_AndExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right39: BinaryAssociation = BinaryAssociation(
    name="right39",
    ends={
        Property(name="expression_Expression41", type=expression_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_AndExpression40", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left42: BinaryAssociation = BinaryAssociation(
    name="left42",
    ends={
        Property(name="expression_Expression43", type=expression_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_EqualityExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right44: BinaryAssociation = BinaryAssociation(
    name="right44",
    ends={
        Property(name="expression_Expression46", type=expression_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_EqualityExpression45", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left47: BinaryAssociation = BinaryAssociation(
    name="left47",
    ends={
        Property(name="expression_Expression48", type=expression_DashExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_DashExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right49: BinaryAssociation = BinaryAssociation(
    name="right49",
    ends={
        Property(name="expression_Expression51", type=expression_DashExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_DashExpression50", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left52: BinaryAssociation = BinaryAssociation(
    name="left52",
    ends={
        Property(name="expression_Expression53", type=expression_PointExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PointExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right54: BinaryAssociation = BinaryAssociation(
    name="right54",
    ends={
        Property(name="expression_Expression56", type=expression_PointExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PointExpression55", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left57: BinaryAssociation = BinaryAssociation(
    name="left57",
    ends={
        Property(name="expression_Expression58", type=expression_PowExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PowExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right59: BinaryAssociation = BinaryAssociation(
    name="right59",
    ends={
        Property(name="expression_Expression61", type=expression_PowExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PowExpression60", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left62: BinaryAssociation = BinaryAssociation(
    name="left62",
    ends={
        Property(name="expression_Expression63", type=expression_QualifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_QualifierExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right64: BinaryAssociation = BinaryAssociation(
    name="right64",
    ends={
        Property(name="expression_Expression66", type=expression_QualifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_QualifierExpression65", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr67: BinaryAssociation = BinaryAssociation(
    name="expr67",
    ends={
        Property(name="expression_Expression68", type=expression_ThereIsIn, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ThereIsIn", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr69: BinaryAssociation = BinaryAssociation(
    name="expr69",
    ends={
        Property(name="expression_Expression70", type=expression_ForallIn, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ForallIn", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr71: BinaryAssociation = BinaryAssociation(
    name="expr71",
    ends={
        Property(name="expression_Expression72", type=expression_FirstIn, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_FirstIn", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr73: BinaryAssociation = BinaryAssociation(
    name="expr73",
    ends={
        Property(name="expression_Expression74", type=expression_LastIn, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_LastIn", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr75: BinaryAssociation = BinaryAssociation(
    name="expr75",
    ends={
        Property(name="expression_Expression76", type=expression_Count, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Count", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr77: BinaryAssociation = BinaryAssociation(
    name="expr77",
    ends={
        Property(name="expression_Expression78", type=expression_Reduce, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Reduce", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usingExpr79: BinaryAssociation = BinaryAssociation(
    name="usingExpr79",
    ends={
        Property(name="expression_Expression81", type=expression_Reduce, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Reduce80", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initValue82: BinaryAssociation = BinaryAssociation(
    name="initValue82",
    ends={
        Property(name="expression_Expression84", type=expression_Reduce, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Reduce83", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr85: BinaryAssociation = BinaryAssociation(
    name="expr85",
    ends={
        Property(name="expression_Expression86", type=expression_Sum, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Sum", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usingExpr87: BinaryAssociation = BinaryAssociation(
    name="usingExpr87",
    ends={
        Property(name="expression_Expression89", type=expression_Sum, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Sum88", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr90: BinaryAssociation = BinaryAssociation(
    name="expr90",
    ends={
        Property(name="expression_Expression91", type=expression_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Map", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usingExpr92: BinaryAssociation = BinaryAssociation(
    name="usingExpr92",
    ends={
        Property(name="expression_Expression94", type=expression_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Map93", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applyExpr95: BinaryAssociation = BinaryAssociation(
    name="applyExpr95",
    ends={
        Property(name="expression_Expression96", type=expression_Apply, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Apply", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr97: BinaryAssociation = BinaryAssociation(
    name="expr97",
    ends={
        Property(name="expression_Expression99", type=expression_Apply, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Apply98", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr100: BinaryAssociation = BinaryAssociation(
    name="expr100",
    ends={
        Property(name="expression_Expression101", type=expression_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_UnaryExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredExpression102: BinaryAssociation = BinaryAssociation(
    name="structuredExpression102",
    ends={
        Property(name="expression_Expression104", type=expression_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_UnaryExpression103", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyValuePair105: BinaryAssociation = BinaryAssociation(
    name="keyValuePair105",
    ends={
        Property(name="expression_KeyValuePair106", type=expression_StructureExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_StructureExpression", type=expression_KeyValuePair, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredExpressions107: BinaryAssociation = BinaryAssociation(
    name="structuredExpressions107",
    ends={
        Property(name="expression_Expression109", type=expression_StructureExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_StructureExpression108", type=expression_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_expression_StatementList_Phrase = Generalization(general=Phrase, specific=expression_StatementList)
gen_expression_AssignmentStatement_Statement = Generalization(general=Statement, specific=expression_AssignmentStatement)
gen_expression_VariableAssignmentStatement_AssignmentStatement = Generalization(general=AssignmentStatement, specific=expression_VariableAssignmentStatement)
gen_expression_SelfAssignmentStatement_AssignmentStatement = Generalization(general=AssignmentStatement, specific=expression_SelfAssignmentStatement)
gen_expression_Expression_Phrase = Generalization(general=Phrase, specific=expression_Expression)
gen_expression_Expression_ExpressionRest = Generalization(general=ExpressionRest, specific=expression_Expression)
gen_expression_FunctionCall_Expression = Generalization(general=Expression, specific=expression_FunctionCall)
gen_expression_KeyValuePair_KeyValuePairRest = Generalization(general=KeyValuePairRest, specific=expression_KeyValuePair)
gen_expression_Term_Expression = Generalization(general=Expression, specific=expression_Term)
gen_expression_List_Term = Generalization(general=Term, specific=expression_List)
gen_expression_Designator_Term = Generalization(general=Term, specific=expression_Designator)
gen_expression_OrExpression_Expression = Generalization(general=Expression, specific=expression_OrExpression)
gen_expression_AndExpression_Expression = Generalization(general=Expression, specific=expression_AndExpression)
gen_expression_EqualityExpression_Expression = Generalization(general=Expression, specific=expression_EqualityExpression)
gen_expression_DashExpression_Expression = Generalization(general=Expression, specific=expression_DashExpression)
gen_expression_PointExpression_Expression = Generalization(general=Expression, specific=expression_PointExpression)
gen_expression_PowExpression_Expression = Generalization(general=Expression, specific=expression_PowExpression)
gen_expression_QualifierExpression_Expression = Generalization(general=Expression, specific=expression_QualifierExpression)
gen_expression_ThereIsIn_Expression = Generalization(general=Expression, specific=expression_ThereIsIn)
gen_expression_ForallIn_Expression = Generalization(general=Expression, specific=expression_ForallIn)
gen_expression_FirstIn_Expression = Generalization(general=Expression, specific=expression_FirstIn)
gen_expression_LastIn_Expression = Generalization(general=Expression, specific=expression_LastIn)
gen_expression_Count_Expression = Generalization(general=Expression, specific=expression_Count)
gen_expression_Reduce_Expression = Generalization(general=Expression, specific=expression_Reduce)
gen_expression_Sum_Expression = Generalization(general=Expression, specific=expression_Sum)
gen_expression_Map_Expression = Generalization(general=Expression, specific=expression_Map)
gen_expression_Apply_Expression = Generalization(general=Expression, specific=expression_Apply)
gen_expression_UnaryExpression_Expression = Generalization(general=Expression, specific=expression_UnaryExpression)
gen_expression_StructureExpression_Expression = Generalization(general=Expression, specific=expression_StructureExpression)
gen_expression_StringValue_Term = Generalization(general=Term, specific=expression_StringValue)
gen_expression_IntegerValue_Term = Generalization(general=Term, specific=expression_IntegerValue)
gen_expression_DoubleValue_Term = Generalization(general=Term, specific=expression_DoubleValue)

# Domain Model
domain_model = DomainModel(
    name="expression",
    types={expression_Model, expression_Phrase, expression_StatementList, Phrase, expression_Statement, expression_AssignmentStatement, Statement, expression_Expression, expression_VariableAssignmentStatement, AssignmentStatement, expression_Designator, expression_SelfAssignmentStatement, ExpressionRest, expression_FunctionCall, Expression, Function, expression_ExpressionList, expression_ProcedureCall, expression_Procedure, expression_ExpressionRest, expression_KeyValuePair, KeyValuePairRest, expression_KeyValuePairRest, expression_Term, expression_List, Term, expression_EObject, expression_OrExpression, expression_AndExpression, expression_EqualityExpression, expression_DashExpression, expression_PointExpression, expression_PowExpression, expression_QualifierExpression, expression_ThereIsIn, expression_ForallIn, expression_FirstIn, expression_LastIn, expression_Count, expression_Reduce, expression_Sum, expression_Map, expression_Apply, expression_UnaryExpression, expression_StructureExpression, expression_StringValue, expression_IntegerValue, expression_DoubleValue},
    associations={phrase0, head1, tail3, expression5, designator6, condition8, function10, params11, procedure13, params14, head17, tail20, value22, rest24, structuredExpression26, terms28, value30, left32, right34, left37, right39, left42, right44, left47, right49, left52, right54, left57, right59, left62, right64, expr67, expr69, expr71, expr73, expr75, expr77, usingExpr79, initValue82, expr85, usingExpr87, expr90, usingExpr92, applyExpr95, expr97, expr100, structuredExpression102, keyValuePair105, structuredExpressions107},
    generalizations={gen_expression_StatementList_Phrase, gen_expression_AssignmentStatement_Statement, gen_expression_VariableAssignmentStatement_AssignmentStatement, gen_expression_SelfAssignmentStatement_AssignmentStatement, gen_expression_Expression_Phrase, gen_expression_Expression_ExpressionRest, gen_expression_FunctionCall_Expression, gen_expression_KeyValuePair_KeyValuePairRest, gen_expression_Term_Expression, gen_expression_List_Term, gen_expression_Designator_Term, gen_expression_OrExpression_Expression, gen_expression_AndExpression_Expression, gen_expression_EqualityExpression_Expression, gen_expression_DashExpression_Expression, gen_expression_PointExpression_Expression, gen_expression_PowExpression_Expression, gen_expression_QualifierExpression_Expression, gen_expression_ThereIsIn_Expression, gen_expression_ForallIn_Expression, gen_expression_FirstIn_Expression, gen_expression_LastIn_Expression, gen_expression_Count_Expression, gen_expression_Reduce_Expression, gen_expression_Sum_Expression, gen_expression_Map_Expression, gen_expression_Apply_Expression, gen_expression_UnaryExpression_Expression, gen_expression_StructureExpression_Expression, gen_expression_StringValue_Term, gen_expression_IntegerValue_Term, gen_expression_DoubleValue_Term},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)