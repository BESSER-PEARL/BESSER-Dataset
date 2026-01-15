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
eol_statements_Statement = Class(name="eol::statements::Statement", is_abstract=True)
eol_statements_ExpressionStatement = Class(name="eol::statements::ExpressionStatement")
Statement = Class(name="Statement")
eol_statements_Expression = Class(name="eol::statements::Expression", is_abstract=True)
eol_statements_SwitchStatement = Class(name="eol::statements::SwitchStatement")
eol_statements_SwitchCaseStatement = Class(name="eol::statements::SwitchCaseStatement", is_abstract=True)
eol_statements_ExpressionOrStatementBlock = Class(name="eol::statements::ExpressionOrStatementBlock")
SwitchCaseStatement = Class(name="SwitchCaseStatement")
eol_statements_IfStatement = Class(name="eol::statements::IfStatement")
eol_statements_ForStatement = Class(name="eol::statements::ForStatement")
eol_statements_SwitchCaseExpressionStatement = Class(name="eol::statements::SwitchCaseExpressionStatement")
eol_statements_SwitchCaseDefaultStatement = Class(name="eol::statements::SwitchCaseDefaultStatement")
eol_statements_WhileStatement = Class(name="eol::statements::WhileStatement")
eol_statements_ReturnStatement = Class(name="eol::statements::ReturnStatement")
eol_statements_ThrowStatement = Class(name="eol::statements::ThrowStatement")
eol_statements_DeleteStatement = Class(name="eol::statements::DeleteStatement")
eol_statements_AssignmentStatement = Class(name="eol::statements::AssignmentStatement")
eol_statements_FormalParameterExpression = Class(name="eol::statements::FormalParameterExpression")
eol_statements_SpecialAssignmentStatement = Class(name="eol::statements::SpecialAssignmentStatement")
AssignmentStatement = Class(name="AssignmentStatement")
eol_statements_ContinueStatement = Class(name="eol::statements::ContinueStatement")
eol_statements_AbortStatement = Class(name="eol::statements::AbortStatement")
eol_statements_BreakStatement = Class(name="eol::statements::BreakStatement")
eol_statements_BreakAllStatement = Class(name="eol::statements::BreakAllStatement")
eol_statements_AnnotationStatement = Class(name="eol::statements::AnnotationStatement", is_abstract=True)
eol_statements_NameExpression = Class(name="eol::statements::NameExpression")
eol_statements_SimpleAnnotationStatement = Class(name="eol::statements::SimpleAnnotationStatement")
AnnotationStatement = Class(name="AnnotationStatement")
eol_statements_StringExpression = Class(name="eol::statements::StringExpression")
eol_statements_ExecutableAnnotationStatement = Class(name="eol::statements::ExecutableAnnotationStatement")
eol_statements_ModelDeclarationStatement = Class(name="eol::statements::ModelDeclarationStatement")
eol_statements_ModelDeclarationParameter = Class(name="eol::statements::ModelDeclarationParameter")
Expression = Class(name="Expression")
eol_statements_VariableDeclarationExpression = Class(name="eol::statements::VariableDeclarationExpression")

# eol_statements_Statement class attributes and methods

# eol_statements_ExpressionStatement class attributes and methods

# Statement class attributes and methods

# eol_statements_Expression class attributes and methods

# eol_statements_SwitchStatement class attributes and methods

# eol_statements_SwitchCaseStatement class attributes and methods

# eol_statements_ExpressionOrStatementBlock class attributes and methods

# SwitchCaseStatement class attributes and methods

# eol_statements_IfStatement class attributes and methods

# eol_statements_ForStatement class attributes and methods

# eol_statements_SwitchCaseExpressionStatement class attributes and methods

# eol_statements_SwitchCaseDefaultStatement class attributes and methods

# eol_statements_WhileStatement class attributes and methods

# eol_statements_ReturnStatement class attributes and methods

# eol_statements_ThrowStatement class attributes and methods

# eol_statements_DeleteStatement class attributes and methods

# eol_statements_AssignmentStatement class attributes and methods

# eol_statements_FormalParameterExpression class attributes and methods

# eol_statements_SpecialAssignmentStatement class attributes and methods

# AssignmentStatement class attributes and methods

# eol_statements_ContinueStatement class attributes and methods

# eol_statements_AbortStatement class attributes and methods

# eol_statements_BreakStatement class attributes and methods

# eol_statements_BreakAllStatement class attributes and methods

# eol_statements_AnnotationStatement class attributes and methods

# eol_statements_NameExpression class attributes and methods

# eol_statements_SimpleAnnotationStatement class attributes and methods

# AnnotationStatement class attributes and methods

# eol_statements_StringExpression class attributes and methods

# eol_statements_ExecutableAnnotationStatement class attributes and methods

# eol_statements_ModelDeclarationStatement class attributes and methods

# eol_statements_ModelDeclarationParameter class attributes and methods

# Expression class attributes and methods

# eol_statements_VariableDeclarationExpression class attributes and methods

# Relationships
expr0: BinaryAssociation = BinaryAssociation(
    name="expr0",
    ends={
        Property(name="eol_statements_Expression", type=eol_statements_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ExpressionStatement", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr1: BinaryAssociation = BinaryAssociation(
    name="expr1",
    ends={
        Property(name="eol_statements_Expression2", type=eol_statements_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_SwitchStatement", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body7: BinaryAssociation = BinaryAssociation(
    name="body7",
    ends={
        Property(name="eol_statements_ExpressionOrStatementBlock", type=eol_statements_SwitchCaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_SwitchCaseStatement", type=eol_statements_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr8: BinaryAssociation = BinaryAssociation(
    name="expr8",
    ends={
        Property(name="eol_statements_Expression10", type=eol_statements_SwitchCaseExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_SwitchCaseExpressionStatement9", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition11: BinaryAssociation = BinaryAssociation(
    name="condition11",
    ends={
        Property(name="eol_statements_Expression12", type=eol_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_IfStatement", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifBody13: BinaryAssociation = BinaryAssociation(
    name="ifBody13",
    ends={
        Property(name="eol_statements_ExpressionOrStatementBlock15", type=eol_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_IfStatement14", type=eol_statements_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseIfBodies16: BinaryAssociation = BinaryAssociation(
    name="elseIfBodies16",
    ends={
        Property(name="eol_statements_ExpressionOrStatementBlock18", type=eol_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_IfStatement17", type=eol_statements_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseBody19: BinaryAssociation = BinaryAssociation(
    name="elseBody19",
    ends={
        Property(name="eol_statements_ExpressionOrStatementBlock21", type=eol_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_IfStatement20", type=eol_statements_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases3: BinaryAssociation = BinaryAssociation(
    name="cases3",
    ends={
        Property(name="eol_statements_SwitchCaseExpressionStatement", type=eol_statements_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_SwitchStatement4", type=eol_statements_SwitchCaseExpressionStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default5: BinaryAssociation = BinaryAssociation(
    name="default5",
    ends={
        Property(name="eol_statements_SwitchCaseDefaultStatement", type=eol_statements_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_SwitchStatement6", type=eol_statements_SwitchCaseDefaultStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body26: BinaryAssociation = BinaryAssociation(
    name="body26",
    ends={
        Property(name="eol_statements_ExpressionOrStatementBlock28", type=eol_statements_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ForStatement27", type=eol_statements_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition29: BinaryAssociation = BinaryAssociation(
    name="condition29",
    ends={
        Property(name="eol_statements_Expression30", type=eol_statements_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_WhileStatement", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body31: BinaryAssociation = BinaryAssociation(
    name="body31",
    ends={
        Property(name="eol_statements_ExpressionOrStatementBlock33", type=eol_statements_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_WhileStatement32", type=eol_statements_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr34: BinaryAssociation = BinaryAssociation(
    name="expr34",
    ends={
        Property(name="eol_statements_Expression35", type=eol_statements_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ReturnStatement", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr36: BinaryAssociation = BinaryAssociation(
    name="expr36",
    ends={
        Property(name="eol_statements_Expression37", type=eol_statements_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ThrowStatement", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr38: BinaryAssociation = BinaryAssociation(
    name="expr38",
    ends={
        Property(name="eol_statements_Expression39", type=eol_statements_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_DeleteStatement", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator22: BinaryAssociation = BinaryAssociation(
    name="iterator22",
    ends={
        Property(name="eol_statements_FormalParameterExpression", type=eol_statements_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ForStatement", type=eol_statements_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition23: BinaryAssociation = BinaryAssociation(
    name="condition23",
    ends={
        Property(name="eol_statements_Expression25", type=eol_statements_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ForStatement24", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name45: BinaryAssociation = BinaryAssociation(
    name="name45",
    ends={
        Property(name="eol_statements_NameExpression", type=eol_statements_AnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_AnnotationStatement", type=eol_statements_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values46: BinaryAssociation = BinaryAssociation(
    name="values46",
    ends={
        Property(name="eol_statements_StringExpression", type=eol_statements_SimpleAnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_SimpleAnnotationStatement", type=eol_statements_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr47: BinaryAssociation = BinaryAssociation(
    name="expr47",
    ends={
        Property(name="eol_statements_Expression48", type=eol_statements_ExecutableAnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ExecutableAnnotationStatement", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs40: BinaryAssociation = BinaryAssociation(
    name="lhs40",
    ends={
        Property(name="eol_statements_Expression41", type=eol_statements_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_AssignmentStatement", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs42: BinaryAssociation = BinaryAssociation(
    name="rhs42",
    ends={
        Property(name="eol_statements_Expression44", type=eol_statements_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_AssignmentStatement43", type=eol_statements_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
driver50: BinaryAssociation = BinaryAssociation(
    name="driver50",
    ends={
        Property(name="eol_statements_NameExpression52", type=eol_statements_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ModelDeclarationStatement51", type=eol_statements_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
aliases53: BinaryAssociation = BinaryAssociation(
    name="aliases53",
    ends={
        Property(name="eol_statements_VariableDeclarationExpression55", type=eol_statements_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ModelDeclarationStatement54", type=eol_statements_VariableDeclarationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters56: BinaryAssociation = BinaryAssociation(
    name="parameters56",
    ends={
        Property(name="eol_statements_ModelDeclarationParameter", type=eol_statements_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ModelDeclarationStatement57", type=eol_statements_ModelDeclarationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name49: BinaryAssociation = BinaryAssociation(
    name="name49",
    ends={
        Property(name="eol_statements_VariableDeclarationExpression", type=eol_statements_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_statements_ModelDeclarationStatement", type=eol_statements_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_eol_statements_ExpressionStatement_Statement = Generalization(general=Statement, specific=eol_statements_ExpressionStatement)
gen_eol_statements_SwitchStatement_Statement = Generalization(general=Statement, specific=eol_statements_SwitchStatement)
gen_eol_statements_SwitchCaseStatement_Statement = Generalization(general=Statement, specific=eol_statements_SwitchCaseStatement)
gen_eol_statements_SwitchCaseDefaultStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_statements_SwitchCaseDefaultStatement)
gen_eol_statements_SwitchCaseExpressionStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_statements_SwitchCaseExpressionStatement)
gen_eol_statements_IfStatement_Statement = Generalization(general=Statement, specific=eol_statements_IfStatement)
gen_eol_statements_ForStatement_Statement = Generalization(general=Statement, specific=eol_statements_ForStatement)
gen_eol_statements_WhileStatement_Statement = Generalization(general=Statement, specific=eol_statements_WhileStatement)
gen_eol_statements_ReturnStatement_Statement = Generalization(general=Statement, specific=eol_statements_ReturnStatement)
gen_eol_statements_ThrowStatement_Statement = Generalization(general=Statement, specific=eol_statements_ThrowStatement)
gen_eol_statements_DeleteStatement_Statement = Generalization(general=Statement, specific=eol_statements_DeleteStatement)
gen_eol_statements_AssignmentStatement_Statement = Generalization(general=Statement, specific=eol_statements_AssignmentStatement)
gen_eol_statements_SpecialAssignmentStatement_AssignmentStatement = Generalization(general=AssignmentStatement, specific=eol_statements_SpecialAssignmentStatement)
gen_eol_statements_ContinueStatement_Statement = Generalization(general=Statement, specific=eol_statements_ContinueStatement)
gen_eol_statements_AbortStatement_Statement = Generalization(general=Statement, specific=eol_statements_AbortStatement)
gen_eol_statements_BreakStatement_Statement = Generalization(general=Statement, specific=eol_statements_BreakStatement)
gen_eol_statements_BreakAllStatement_Statement = Generalization(general=Statement, specific=eol_statements_BreakAllStatement)
gen_eol_statements_AnnotationStatement_Statement = Generalization(general=Statement, specific=eol_statements_AnnotationStatement)
gen_eol_statements_SimpleAnnotationStatement_AnnotationStatement = Generalization(general=AnnotationStatement, specific=eol_statements_SimpleAnnotationStatement)
gen_eol_statements_ExecutableAnnotationStatement_AnnotationStatement = Generalization(general=AnnotationStatement, specific=eol_statements_ExecutableAnnotationStatement)
gen_eol_statements_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=eol_statements_VariableDeclarationExpression)
gen_eol_statements_NameExpression_Expression = Generalization(general=Expression, specific=eol_statements_NameExpression)
gen_eol_statements_ModelDeclarationStatement_Statement = Generalization(general=Statement, specific=eol_statements_ModelDeclarationStatement)

# Domain Model
domain_model = DomainModel(
    name="eol_statements",
    types={eol_statements_Statement, eol_statements_ExpressionStatement, Statement, eol_statements_Expression, eol_statements_SwitchStatement, eol_statements_SwitchCaseStatement, eol_statements_ExpressionOrStatementBlock, SwitchCaseStatement, eol_statements_IfStatement, eol_statements_ForStatement, eol_statements_SwitchCaseExpressionStatement, eol_statements_SwitchCaseDefaultStatement, eol_statements_WhileStatement, eol_statements_ReturnStatement, eol_statements_ThrowStatement, eol_statements_DeleteStatement, eol_statements_AssignmentStatement, eol_statements_FormalParameterExpression, eol_statements_SpecialAssignmentStatement, AssignmentStatement, eol_statements_ContinueStatement, eol_statements_AbortStatement, eol_statements_BreakStatement, eol_statements_BreakAllStatement, eol_statements_AnnotationStatement, eol_statements_NameExpression, eol_statements_SimpleAnnotationStatement, AnnotationStatement, eol_statements_StringExpression, eol_statements_ExecutableAnnotationStatement, eol_statements_ModelDeclarationStatement, eol_statements_ModelDeclarationParameter, Expression, eol_statements_VariableDeclarationExpression},
    associations={expr0, expr1, body7, expr8, condition11, ifBody13, elseIfBodies16, elseBody19, cases3, default5, body26, condition29, body31, expr34, expr36, expr38, iterator22, condition23, name45, values46, expr47, lhs40, rhs42, driver50, aliases53, parameters56, name49},
    generalizations={gen_eol_statements_ExpressionStatement_Statement, gen_eol_statements_SwitchStatement_Statement, gen_eol_statements_SwitchCaseStatement_Statement, gen_eol_statements_SwitchCaseDefaultStatement_SwitchCaseStatement, gen_eol_statements_SwitchCaseExpressionStatement_SwitchCaseStatement, gen_eol_statements_IfStatement_Statement, gen_eol_statements_ForStatement_Statement, gen_eol_statements_WhileStatement_Statement, gen_eol_statements_ReturnStatement_Statement, gen_eol_statements_ThrowStatement_Statement, gen_eol_statements_DeleteStatement_Statement, gen_eol_statements_AssignmentStatement_Statement, gen_eol_statements_SpecialAssignmentStatement_AssignmentStatement, gen_eol_statements_ContinueStatement_Statement, gen_eol_statements_AbortStatement_Statement, gen_eol_statements_BreakStatement_Statement, gen_eol_statements_BreakAllStatement_Statement, gen_eol_statements_AnnotationStatement_Statement, gen_eol_statements_SimpleAnnotationStatement_AnnotationStatement, gen_eol_statements_ExecutableAnnotationStatement_AnnotationStatement, gen_eol_statements_VariableDeclarationExpression_Expression, gen_eol_statements_NameExpression_Expression, gen_eol_statements_ModelDeclarationStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)