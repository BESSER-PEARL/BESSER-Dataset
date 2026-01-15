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
miniJava_Program = Class(name="miniJava::Program")
miniJava_ClassDecl = Class(name="miniJava::ClassDecl")
miniJava_MainMethod = Class(name="miniJava::MainMethod")
miniJava_VarDeclaration = Class(name="miniJava::VarDeclaration")
miniJava_Method = Class(name="miniJava::Method")
miniJava_Statement = Class(name="miniJava::Statement")
miniJava_Type = Class(name="miniJava::Type")
miniJava_Variable = Class(name="miniJava::Variable")
miniJava_Expr = Class(name="miniJava::Expr")
miniJava_NumberValue = Class(name="miniJava::NumberValue")
miniJava_MethodCall = Class(name="miniJava::MethodCall")
miniJava_Expression = Class(name="miniJava::Expression")
Expr = Class(name="Expr")
miniJava_Point = Class(name="miniJava::Point")
miniJava_SquareBrackets = Class(name="miniJava::SquareBrackets")
miniJava_Addition = Class(name="miniJava::Addition")
miniJava_Multiplication = Class(name="miniJava::Multiplication")

# miniJava_Program class attributes and methods

# miniJava_ClassDecl class attributes and methods
miniJava_ClassDecl_name: Property = Property(name="name", type=StringType)
miniJava_ClassDecl.attributes={miniJava_ClassDecl_name}

# miniJava_MainMethod class attributes and methods

# miniJava_VarDeclaration class attributes and methods

# miniJava_Method class attributes and methods
miniJava_Method_name: Property = Property(name="name", type=StringType)
miniJava_Method.attributes={miniJava_Method_name}

# miniJava_Statement class attributes and methods
miniJava_Statement_statementType: Property = Property(name="statementType", type=StringType)
miniJava_Statement_isArrayElementAssignment: Property = Property(name="isArrayElementAssignment", type=BooleanType)
miniJava_Statement.attributes={miniJava_Statement_isArrayElementAssignment, miniJava_Statement_statementType}

# miniJava_Type class attributes and methods
miniJava_Type_typeName: Property = Property(name="typeName", type=StringType)
miniJava_Type.attributes={miniJava_Type_typeName}

# miniJava_Variable class attributes and methods
miniJava_Variable_name: Property = Property(name="name", type=StringType)
miniJava_Variable.attributes={miniJava_Variable_name}

# miniJava_Expr class attributes and methods
miniJava_Expr_expressionType: Property = Property(name="expressionType", type=StringType)
miniJava_Expr.attributes={miniJava_Expr_expressionType}

# miniJava_NumberValue class attributes and methods
miniJava_NumberValue_value: Property = Property(name="value", type=IntegerType)
miniJava_NumberValue.attributes={miniJava_NumberValue_value}

# miniJava_MethodCall class attributes and methods

# miniJava_Expression class attributes and methods

# Expr class attributes and methods

# miniJava_Point class attributes and methods

# miniJava_SquareBrackets class attributes and methods

# miniJava_Addition class attributes and methods

# miniJava_Multiplication class attributes and methods

# Relationships
classDeclarations0: BinaryAssociation = BinaryAssociation(
    name="classDeclarations0",
    ends={
        Property(name="miniJava_ClassDecl", type=miniJava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Program", type=miniJava_ClassDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainMethod1: BinaryAssociation = BinaryAssociation(
    name="mainMethod1",
    ends={
        Property(name="miniJava_MainMethod", type=miniJava_ClassDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClassDecl2", type=miniJava_MainMethod, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedClass4: BinaryAssociation = BinaryAssociation(
    name="extendedClass4",
    ends={
        Property(name="miniJava_ClassDecl5", type=miniJava_ClassDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClassDecl3", type=miniJava_ClassDecl, multiplicity=Multiplicity(0, 1))
    }
)
varDeclarations6: BinaryAssociation = BinaryAssociation(
    name="varDeclarations6",
    ends={
        Property(name="miniJava_VarDeclaration", type=miniJava_ClassDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClassDecl7", type=miniJava_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodDeclarations8: BinaryAssociation = BinaryAssociation(
    name="methodDeclarations8",
    ends={
        Property(name="miniJava_Method", type=miniJava_ClassDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClassDecl9", type=miniJava_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement10: BinaryAssociation = BinaryAssociation(
    name="statement10",
    ends={
        Property(name="miniJava_Statement", type=miniJava_MainMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MainMethod11", type=miniJava_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classDecl12: BinaryAssociation = BinaryAssociation(
    name="classDecl12",
    ends={
        Property(name="miniJava_ClassDecl13", type=miniJava_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Type", type=miniJava_ClassDecl, multiplicity=Multiplicity(0, 1))
    }
)
variable14: BinaryAssociation = BinaryAssociation(
    name="variable14",
    ends={
        Property(name="miniJava_Variable", type=miniJava_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_VarDeclaration15", type=miniJava_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableType16: BinaryAssociation = BinaryAssociation(
    name="variableType16",
    ends={
        Property(name="miniJava_Type18", type=miniJava_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Variable17", type=miniJava_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodType19: BinaryAssociation = BinaryAssociation(
    name="methodType19",
    ends={
        Property(name="miniJava_Type21", type=miniJava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Method20", type=miniJava_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalVarDeclarations22: BinaryAssociation = BinaryAssociation(
    name="formalVarDeclarations22",
    ends={
        Property(name="miniJava_Variable24", type=miniJava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Method23", type=miniJava_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVarDeclarations25: BinaryAssociation = BinaryAssociation(
    name="localVarDeclarations25",
    ends={
        Property(name="miniJava_VarDeclaration27", type=miniJava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Method26", type=miniJava_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements28: BinaryAssociation = BinaryAssociation(
    name="statements28",
    ends={
        Property(name="miniJava_Statement30", type=miniJava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Method29", type=miniJava_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnExpression31: BinaryAssociation = BinaryAssociation(
    name="returnExpression31",
    ends={
        Property(name="miniJava_Expr", type=miniJava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Method32", type=miniJava_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements34: BinaryAssociation = BinaryAssociation(
    name="statements34",
    ends={
        Property(name="miniJava_Statement35", type=miniJava_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Statement33", type=miniJava_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstExpression36: BinaryAssociation = BinaryAssociation(
    name="firstExpression36",
    ends={
        Property(name="miniJava_Expr38", type=miniJava_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Statement37", type=miniJava_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable39: BinaryAssociation = BinaryAssociation(
    name="variable39",
    ends={
        Property(name="miniJava_Variable41", type=miniJava_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Statement40", type=miniJava_Variable, multiplicity=Multiplicity(0, 1))
    }
)
secondExpression42: BinaryAssociation = BinaryAssociation(
    name="secondExpression42",
    ends={
        Property(name="miniJava_Expr44", type=miniJava_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Statement43", type=miniJava_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right46: BinaryAssociation = BinaryAssociation(
    name="right46",
    ends={
        Property(name="miniJava_Expr47", type=miniJava_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Expr45", type=miniJava_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression49: BinaryAssociation = BinaryAssociation(
    name="expression49",
    ends={
        Property(name="miniJava_Expr50", type=miniJava_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Expr48", type=miniJava_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type51: BinaryAssociation = BinaryAssociation(
    name="type51",
    ends={
        Property(name="miniJava_Type53", type=miniJava_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Expr52", type=miniJava_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable54: BinaryAssociation = BinaryAssociation(
    name="variable54",
    ends={
        Property(name="miniJava_Variable56", type=miniJava_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Expr55", type=miniJava_Variable, multiplicity=Multiplicity(0, 1))
    }
)
number57: BinaryAssociation = BinaryAssociation(
    name="number57",
    ends={
        Property(name="miniJava_NumberValue", type=miniJava_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Expr58", type=miniJava_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left62: BinaryAssociation = BinaryAssociation(
    name="left62",
    ends={
        Property(name="miniJava_Expr63", type=miniJava_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Expr61", type=miniJava_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method64: BinaryAssociation = BinaryAssociation(
    name="method64",
    ends={
        Property(name="miniJava_Method66", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall65", type=miniJava_Method, multiplicity=Multiplicity(0, 1))
    }
)
parameters67: BinaryAssociation = BinaryAssociation(
    name="parameters67",
    ends={
        Property(name="miniJava_Expr69", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall68", type=miniJava_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodCall59: BinaryAssociation = BinaryAssociation(
    name="methodCall59",
    ends={
        Property(name="miniJava_MethodCall", type=miniJava_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Expr60", type=miniJava_MethodCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_miniJava_Expression_Expr = Generalization(general=Expr, specific=miniJava_Expression)
gen_miniJava_Point_Expr = Generalization(general=Expr, specific=miniJava_Point)
gen_miniJava_SquareBrackets_Expr = Generalization(general=Expr, specific=miniJava_SquareBrackets)
gen_miniJava_Addition_Expr = Generalization(general=Expr, specific=miniJava_Addition)
gen_miniJava_Multiplication_Expr = Generalization(general=Expr, specific=miniJava_Multiplication)

# Domain Model
domain_model = DomainModel(
    name="miniJava",
    types={miniJava_Program, miniJava_ClassDecl, miniJava_MainMethod, miniJava_VarDeclaration, miniJava_Method, miniJava_Statement, miniJava_Type, miniJava_Variable, miniJava_Expr, miniJava_NumberValue, miniJava_MethodCall, miniJava_Expression, Expr, miniJava_Point, miniJava_SquareBrackets, miniJava_Addition, miniJava_Multiplication},
    associations={classDeclarations0, mainMethod1, extendedClass4, varDeclarations6, methodDeclarations8, statement10, classDecl12, variable14, variableType16, methodType19, formalVarDeclarations22, localVarDeclarations25, statements28, returnExpression31, statements34, firstExpression36, variable39, secondExpression42, right46, expression49, type51, variable54, number57, left62, method64, parameters67, methodCall59},
    generalizations={gen_miniJava_Expression_Expr, gen_miniJava_Point_Expr, gen_miniJava_SquareBrackets_Expr, gen_miniJava_Addition_Expr, gen_miniJava_Multiplication_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)