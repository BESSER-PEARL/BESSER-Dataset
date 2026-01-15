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
model_BreakStatement = Class(name="model::BreakStatement")
model_ReturnStatement = Class(name="model::ReturnStatement")
model_IfStatement = Class(name="model::IfStatement")
model_ProcedureDeclaration = Class(name="model::ProcedureDeclaration")
FunctionDeclaration = Class(name="FunctionDeclaration")
model_Block = Class(name="model::Block")
model_Action = Class(name="model::Action", is_abstract=True)
model_Statement = Class(name="model::Statement", is_abstract=True)
Action = Class(name="Action")
model_EmptyStatement = Class(name="model::EmptyStatement")
Statement = Class(name="Statement")
model_Branch = Class(name="model::Branch")
model_Expression = Class(name="model::Expression")
model_VariableDeclarationStatement = Class(name="model::VariableDeclarationStatement")
model_VariableDeclaration = Class(name="model::VariableDeclaration")
model_ConstantDeclarationStatement = Class(name="model::ConstantDeclarationStatement")
model_ConstantDeclaration = Class(name="model::ConstantDeclaration")
model_ExpressionStatement = Class(name="model::ExpressionStatement")
model_SwitchStatement = Class(name="model::SwitchStatement")
model_ForStatement = Class(name="model::ForStatement")
model_ParameterDeclaration = Class(name="model::ParameterDeclaration")
model_ChoiceStatement = Class(name="model::ChoiceStatement")
model_AssignmentStatement = Class(name="model::AssignmentStatement")
model_ReferenceExpression = Class(name="model::ReferenceExpression")

# model_BreakStatement class attributes and methods

# model_ReturnStatement class attributes and methods

# model_IfStatement class attributes and methods

# model_ProcedureDeclaration class attributes and methods

# FunctionDeclaration class attributes and methods

# model_Block class attributes and methods

# model_Action class attributes and methods

# model_Statement class attributes and methods

# Action class attributes and methods

# model_EmptyStatement class attributes and methods

# Statement class attributes and methods

# model_Branch class attributes and methods

# model_Expression class attributes and methods

# model_VariableDeclarationStatement class attributes and methods

# model_VariableDeclaration class attributes and methods

# model_ConstantDeclarationStatement class attributes and methods

# model_ConstantDeclaration class attributes and methods

# model_ExpressionStatement class attributes and methods

# model_SwitchStatement class attributes and methods

# model_ForStatement class attributes and methods

# model_ParameterDeclaration class attributes and methods

# model_ChoiceStatement class attributes and methods

# model_AssignmentStatement class attributes and methods

# model_ReferenceExpression class attributes and methods

# Relationships
expression9: BinaryAssociation = BinaryAssociation(
    name="expression9",
    ends={
        Property(name="model_Expression10", type=model_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ExpressionStatement", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression11: BinaryAssociation = BinaryAssociation(
    name="expression11",
    ends={
        Property(name="model_Expression12", type=model_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ReturnStatement", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionals13: BinaryAssociation = BinaryAssociation(
    name="conditionals13",
    ends={
        Property(name="model_Branch14", type=model_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_IfStatement", type=model_Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
body0: BinaryAssociation = BinaryAssociation(
    name="body0",
    ends={
        Property(name="model_Block", type=model_ProcedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ProcedureDeclaration", type=model_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions1: BinaryAssociation = BinaryAssociation(
    name="actions1",
    ends={
        Property(name="model_Action", type=model_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Block2", type=model_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard3: BinaryAssociation = BinaryAssociation(
    name="guard3",
    ends={
        Property(name="model_Expression", type=model_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Branch", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action4: BinaryAssociation = BinaryAssociation(
    name="action4",
    ends={
        Property(name="model_Action6", type=model_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Branch5", type=model_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableDeclaration7: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration7",
    ends={
        Property(name="model_VariableDeclaration", type=model_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_VariableDeclarationStatement", type=model_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constantDeclaration8: BinaryAssociation = BinaryAssociation(
    name="constantDeclaration8",
    ends={
        Property(name="model_ConstantDeclaration", type=model_ConstantDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ConstantDeclarationStatement", type=model_ConstantDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
controlExpression15: BinaryAssociation = BinaryAssociation(
    name="controlExpression15",
    ends={
        Property(name="model_Expression16", type=model_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_SwitchStatement", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases17: BinaryAssociation = BinaryAssociation(
    name="cases17",
    ends={
        Property(name="model_Branch19", type=model_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_SwitchStatement18", type=model_Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameter20: BinaryAssociation = BinaryAssociation(
    name="parameter20",
    ends={
        Property(name="model_ParameterDeclaration", type=model_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ForStatement", type=model_ParameterDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
range21: BinaryAssociation = BinaryAssociation(
    name="range21",
    ends={
        Property(name="model_Expression23", type=model_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ForStatement22", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body24: BinaryAssociation = BinaryAssociation(
    name="body24",
    ends={
        Property(name="model_Action26", type=model_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ForStatement25", type=model_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then27: BinaryAssociation = BinaryAssociation(
    name="then27",
    ends={
        Property(name="model_Action29", type=model_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ForStatement28", type=model_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branches30: BinaryAssociation = BinaryAssociation(
    name="branches30",
    ends={
        Property(name="model_Branch31", type=model_ChoiceStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ChoiceStatement", type=model_Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
lhs32: BinaryAssociation = BinaryAssociation(
    name="lhs32",
    ends={
        Property(name="model_ReferenceExpression", type=model_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AssignmentStatement", type=model_ReferenceExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs33: BinaryAssociation = BinaryAssociation(
    name="rhs33",
    ends={
        Property(name="model_Expression35", type=model_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AssignmentStatement34", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_model_BreakStatement_Statement = Generalization(general=Statement, specific=model_BreakStatement)
gen_model_ReturnStatement_Statement = Generalization(general=Statement, specific=model_ReturnStatement)
gen_model_IfStatement_Statement = Generalization(general=Statement, specific=model_IfStatement)
gen_model_ProcedureDeclaration_FunctionDeclaration = Generalization(general=FunctionDeclaration, specific=model_ProcedureDeclaration)
gen_model_Statement_Action = Generalization(general=Action, specific=model_Statement)
gen_model_EmptyStatement_Statement = Generalization(general=Statement, specific=model_EmptyStatement)
gen_model_Block_Action = Generalization(general=Action, specific=model_Block)
gen_model_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=model_VariableDeclarationStatement)
gen_model_ConstantDeclarationStatement_Statement = Generalization(general=Statement, specific=model_ConstantDeclarationStatement)
gen_model_ExpressionStatement_Statement = Generalization(general=Statement, specific=model_ExpressionStatement)
gen_model_SwitchStatement_Statement = Generalization(general=Statement, specific=model_SwitchStatement)
gen_model_ForStatement_Statement = Generalization(general=Statement, specific=model_ForStatement)
gen_model_ChoiceStatement_Statement = Generalization(general=Statement, specific=model_ChoiceStatement)
gen_model_AssignmentStatement_Statement = Generalization(general=Statement, specific=model_AssignmentStatement)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_BreakStatement, model_ReturnStatement, model_IfStatement, model_ProcedureDeclaration, FunctionDeclaration, model_Block, model_Action, model_Statement, Action, model_EmptyStatement, Statement, model_Branch, model_Expression, model_VariableDeclarationStatement, model_VariableDeclaration, model_ConstantDeclarationStatement, model_ConstantDeclaration, model_ExpressionStatement, model_SwitchStatement, model_ForStatement, model_ParameterDeclaration, model_ChoiceStatement, model_AssignmentStatement, model_ReferenceExpression},
    associations={expression9, expression11, conditionals13, body0, actions1, guard3, action4, variableDeclaration7, constantDeclaration8, controlExpression15, cases17, parameter20, range21, body24, then27, branches30, lhs32, rhs33},
    generalizations={gen_model_BreakStatement_Statement, gen_model_ReturnStatement_Statement, gen_model_IfStatement_Statement, gen_model_ProcedureDeclaration_FunctionDeclaration, gen_model_Statement_Action, gen_model_EmptyStatement_Statement, gen_model_Block_Action, gen_model_VariableDeclarationStatement_Statement, gen_model_ConstantDeclarationStatement_Statement, gen_model_ExpressionStatement_Statement, gen_model_SwitchStatement_Statement, gen_model_ForStatement_Statement, gen_model_ChoiceStatement_Statement, gen_model_AssignmentStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)