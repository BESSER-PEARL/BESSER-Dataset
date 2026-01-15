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
FilePath = Class(name="FilePath")
Expression = Class(name="Expression")
mt_core_FilePath = Class(name="mt::core::FilePath")
mt_core_Metamodel = Class(name="mt::core::Metamodel")
mt_ResourceSet = Class(name="mt::ResourceSet")
mt_Resource = Class(name="mt::Resource", is_abstract=True)
mt_core_ASTNode = Class(name="mt::core::ASTNode", is_abstract=True)
mt_core_Template = Class(name="mt::core::Template")
Resource = Class(name="Resource")
core_mt_Resource = Class(name="core::mt::Resource")
Script = Class(name="Script")
mt_core_Script = Class(name="mt::core::Script")
ASTNode = Class(name="ASTNode")
ScriptDescriptor = Class(name="ScriptDescriptor")
Statement = Class(name="Statement")
mt_core_ScriptDescriptor = Class(name="mt::core::ScriptDescriptor")
mt_expressions_Parenthesis = Class(name="mt::expressions::Parenthesis")
mt_expressions_Literal = Class(name="mt::expressions::Literal", is_abstract=True)
mt_expressions_StringLiteral = Class(name="mt::expressions::StringLiteral")
Literal = Class(name="Literal")
mt_core_Service = Class(name="mt::core::Service")
Method_ = Class(name="Method")
mt_core_Method = Class(name="mt::core::Method")
Parameter_ = Class(name="Parameter")
mt_core_Parameter = Class(name="mt::core::Parameter")
mt_expressions_Expression = Class(name="mt::expressions::Expression", is_abstract=True)
mt_expressions_CallSet = Class(name="mt::expressions::CallSet")
Call = Class(name="Call")
mt_expressions_Call = Class(name="mt::expressions::Call")
mt_expressions_Not = Class(name="mt::expressions::Not")
mt_expressions_Operator = Class(name="mt::expressions::Operator")
mt_statements_Feature = Class(name="mt::statements::Feature")
mt_statements_Text = Class(name="mt::statements::Text")
mt_expressions_IntegerLiteral = Class(name="mt::expressions::IntegerLiteral")
mt_expressions_DoubleLiteral = Class(name="mt::expressions::DoubleLiteral")
mt_expressions_BooleanLiteral = Class(name="mt::expressions::BooleanLiteral")
mt_expressions_NullLiteral = Class(name="mt::expressions::NullLiteral")
mt_statements_Statement = Class(name="mt::statements::Statement", is_abstract=True)
mt_statements_Comment = Class(name="mt::statements::Comment")
mt_statements_If = Class(name="mt::statements::If")
If = Class(name="If")
mt_statements_For = Class(name="mt::statements::For")

# FilePath class attributes and methods

# Expression class attributes and methods

# mt_core_FilePath class attributes and methods

# mt_core_Metamodel class attributes and methods
mt_core_Metamodel_packageClass: Property = Property(name="packageClass", type=StringType)
mt_core_Metamodel.attributes={mt_core_Metamodel_packageClass}

# mt_ResourceSet class attributes and methods

# mt_Resource class attributes and methods
mt_Resource_name: Property = Property(name="name", type=StringType)
mt_Resource.attributes={mt_Resource_name}

# mt_core_ASTNode class attributes and methods
mt_core_ASTNode_begin: Property = Property(name="begin", type=IntegerType)
mt_core_ASTNode_end: Property = Property(name="end", type=IntegerType)
mt_core_ASTNode_m_getTemplate: Method = Method(name="getTemplate", parameters={}, type=StringType)
mt_core_ASTNode.attributes={mt_core_ASTNode_end, mt_core_ASTNode_begin}
mt_core_ASTNode.methods={mt_core_ASTNode_m_getTemplate}

# mt_core_Template class attributes and methods
mt_core_Template_beginTag: Property = Property(name="beginTag", type=StringType)
mt_core_Template_endTag: Property = Property(name="endTag", type=StringType)
mt_core_Template.attributes={mt_core_Template_endTag, mt_core_Template_beginTag}

# Resource class attributes and methods

# core_mt_Resource class attributes and methods

# Script class attributes and methods

# mt_core_Script class attributes and methods

# ASTNode class attributes and methods

# ScriptDescriptor class attributes and methods

# Statement class attributes and methods

# mt_core_ScriptDescriptor class attributes and methods
mt_core_ScriptDescriptor_type: Property = Property(name="type", type=StringType)
mt_core_ScriptDescriptor_description: Property = Property(name="description", type=StringType)
mt_core_ScriptDescriptor_name: Property = Property(name="name", type=StringType)
mt_core_ScriptDescriptor.attributes={mt_core_ScriptDescriptor_type, mt_core_ScriptDescriptor_description, mt_core_ScriptDescriptor_name}

# mt_expressions_Parenthesis class attributes and methods

# mt_expressions_Literal class attributes and methods

# mt_expressions_StringLiteral class attributes and methods
mt_expressions_StringLiteral_value: Property = Property(name="value", type=StringType)
mt_expressions_StringLiteral.attributes={mt_expressions_StringLiteral_value}

# Literal class attributes and methods

# mt_core_Service class attributes and methods

# Method class attributes and methods

# mt_core_Method class attributes and methods
mt_core_Method_name: Property = Property(name="name", type=StringType)
mt_core_Method_return: Property = Property(name="return", type=StringType)
mt_core_Method.attributes={mt_core_Method_name, mt_core_Method_return}

# Parameter class attributes and methods

# mt_core_Parameter class attributes and methods
mt_core_Parameter_type: Property = Property(name="type", type=StringType)
mt_core_Parameter.attributes={mt_core_Parameter_type}

# mt_expressions_Expression class attributes and methods

# mt_expressions_CallSet class attributes and methods

# Call class attributes and methods

# mt_expressions_Call class attributes and methods
mt_expressions_Call_name: Property = Property(name="name", type=StringType)
mt_expressions_Call_prefix: Property = Property(name="prefix", type=StringType)
mt_expressions_Call.attributes={mt_expressions_Call_name, mt_expressions_Call_prefix}

# mt_expressions_Not class attributes and methods

# mt_expressions_Operator class attributes and methods
mt_expressions_Operator_operator: Property = Property(name="operator", type=StringType)
mt_expressions_Operator.attributes={mt_expressions_Operator_operator}

# mt_statements_Feature class attributes and methods

# mt_statements_Text class attributes and methods
mt_statements_Text_value: Property = Property(name="value", type=StringType)
mt_statements_Text.attributes={mt_statements_Text_value}

# mt_expressions_IntegerLiteral class attributes and methods
mt_expressions_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
mt_expressions_IntegerLiteral.attributes={mt_expressions_IntegerLiteral_value}

# mt_expressions_DoubleLiteral class attributes and methods
mt_expressions_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
mt_expressions_DoubleLiteral.attributes={mt_expressions_DoubleLiteral_value}

# mt_expressions_BooleanLiteral class attributes and methods
mt_expressions_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
mt_expressions_BooleanLiteral.attributes={mt_expressions_BooleanLiteral_value}

# mt_expressions_NullLiteral class attributes and methods

# mt_statements_Statement class attributes and methods

# mt_statements_Comment class attributes and methods
mt_statements_Comment_value: Property = Property(name="value", type=StringType)
mt_statements_Comment.attributes={mt_statements_Comment_value}

# mt_statements_If class attributes and methods

# If class attributes and methods

# mt_statements_For class attributes and methods

# Relationships
file7: BinaryAssociation = BinaryAssociation(
    name="file7",
    ends={
        Property(name="FilePath", type=mt_core_ScriptDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_core_ScriptDescriptor", type=FilePath, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
post8: BinaryAssociation = BinaryAssociation(
    name="post8",
    ends={
        Property(name="Expression", type=mt_core_ScriptDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_core_ScriptDescriptor9", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements10: BinaryAssociation = BinaryAssociation(
    name="statements10",
    ends={
        Property(name="Statement11", type=mt_core_FilePath, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_core_FilePath", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources0: BinaryAssociation = BinaryAssociation(
    name="resources0",
    ends={
        Property(name="mt_Resource", type=mt_ResourceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_ResourceSet", type=mt_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="core_mt_Resource", type=mt_core_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_core_Template", type=core_mt_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
scripts2: BinaryAssociation = BinaryAssociation(
    name="scripts2",
    ends={
        Property(name="Script", type=mt_core_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_core_Template3", type=Script, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptor4: BinaryAssociation = BinaryAssociation(
    name="descriptor4",
    ends={
        Property(name="ScriptDescriptor", type=mt_core_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_core_Script", type=ScriptDescriptor, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements5: BinaryAssociation = BinaryAssociation(
    name="statements5",
    ends={
        Property(name="Statement", type=mt_core_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_core_Script6", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands22: BinaryAssociation = BinaryAssociation(
    name="operands22",
    ends={
        Property(name="Expression23", type=mt_expressions_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_expressions_Operator", type=Expression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
expression24: BinaryAssociation = BinaryAssociation(
    name="expression24",
    ends={
        Property(name="Expression25", type=mt_expressions_Parenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_expressions_Parenthesis", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methods12: BinaryAssociation = BinaryAssociation(
    name="methods12",
    ends={
        Property(name="Method", type=mt_core_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_core_Service", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters13: BinaryAssociation = BinaryAssociation(
    name="parameters13",
    ends={
        Property(name="Parameter", type=mt_core_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_core_Method", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calls14: BinaryAssociation = BinaryAssociation(
    name="calls14",
    ends={
        Property(name="Call", type=mt_expressions_CallSet, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_expressions_CallSet", type=Call, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments15: BinaryAssociation = BinaryAssociation(
    name="arguments15",
    ends={
        Property(name="Expression16", type=mt_expressions_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_expressions_Call", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filter17: BinaryAssociation = BinaryAssociation(
    name="filter17",
    ends={
        Property(name="Expression19", type=mt_expressions_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_expressions_Call18", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression20: BinaryAssociation = BinaryAssociation(
    name="expression20",
    ends={
        Property(name="Expression21", type=mt_expressions_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_expressions_Not", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression41: BinaryAssociation = BinaryAssociation(
    name="expression41",
    ends={
        Property(name="Expression42", type=mt_statements_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_statements_Feature", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition26: BinaryAssociation = BinaryAssociation(
    name="condition26",
    ends={
        Property(name="Expression27", type=mt_statements_If, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_statements_If", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements28: BinaryAssociation = BinaryAssociation(
    name="thenStatements28",
    ends={
        Property(name="Statement30", type=mt_statements_If, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_statements_If29", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements31: BinaryAssociation = BinaryAssociation(
    name="elseStatements31",
    ends={
        Property(name="Statement33", type=mt_statements_If, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_statements_If32", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseIf34: BinaryAssociation = BinaryAssociation(
    name="elseIf34",
    ends={
        Property(name="If", type=mt_statements_If, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_statements_If35", type=If, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator36: BinaryAssociation = BinaryAssociation(
    name="iterator36",
    ends={
        Property(name="Expression37", type=mt_statements_For, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_statements_For", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements38: BinaryAssociation = BinaryAssociation(
    name="statements38",
    ends={
        Property(name="Statement40", type=mt_statements_For, multiplicity=Multiplicity(1, 1)),
        Property(name="mt_statements_For39", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mt_core_FilePath_ASTNode = Generalization(general=ASTNode, specific=mt_core_FilePath)
gen_mt_core_Metamodel_Resource = Generalization(general=Resource, specific=mt_core_Metamodel)
gen_mt_core_Template_Resource = Generalization(general=Resource, specific=mt_core_Template)
gen_mt_core_Script_ASTNode = Generalization(general=ASTNode, specific=mt_core_Script)
gen_mt_core_ScriptDescriptor_ASTNode = Generalization(general=ASTNode, specific=mt_core_ScriptDescriptor)
gen_mt_expressions_Parenthesis_Expression = Generalization(general=Expression, specific=mt_expressions_Parenthesis)
gen_mt_expressions_Literal_Expression = Generalization(general=Expression, specific=mt_expressions_Literal)
gen_mt_expressions_StringLiteral_Literal = Generalization(general=Literal, specific=mt_expressions_StringLiteral)
gen_mt_core_Service_Resource = Generalization(general=Resource, specific=mt_core_Service)
gen_mt_expressions_Expression_ASTNode = Generalization(general=ASTNode, specific=mt_expressions_Expression)
gen_mt_expressions_CallSet_Expression = Generalization(general=Expression, specific=mt_expressions_CallSet)
gen_mt_expressions_Call_ASTNode = Generalization(general=ASTNode, specific=mt_expressions_Call)
gen_mt_expressions_Not_Expression = Generalization(general=Expression, specific=mt_expressions_Not)
gen_mt_expressions_Operator_Expression = Generalization(general=Expression, specific=mt_expressions_Operator)
gen_mt_statements_Feature_Statement = Generalization(general=Statement, specific=mt_statements_Feature)
gen_mt_statements_Text_Statement = Generalization(general=Statement, specific=mt_statements_Text)
gen_mt_expressions_IntegerLiteral_Literal = Generalization(general=Literal, specific=mt_expressions_IntegerLiteral)
gen_mt_expressions_DoubleLiteral_Literal = Generalization(general=Literal, specific=mt_expressions_DoubleLiteral)
gen_mt_expressions_BooleanLiteral_Literal = Generalization(general=Literal, specific=mt_expressions_BooleanLiteral)
gen_mt_expressions_NullLiteral_Literal = Generalization(general=Literal, specific=mt_expressions_NullLiteral)
gen_mt_statements_Statement_ASTNode = Generalization(general=ASTNode, specific=mt_statements_Statement)
gen_mt_statements_Comment_Statement = Generalization(general=Statement, specific=mt_statements_Comment)
gen_mt_statements_If_Statement = Generalization(general=Statement, specific=mt_statements_If)
gen_mt_statements_For_Statement = Generalization(general=Statement, specific=mt_statements_For)

# Domain Model
domain_model = DomainModel(
    name="mt",
    types={FilePath, Expression, mt_core_FilePath, mt_core_Metamodel, mt_ResourceSet, mt_Resource, mt_core_ASTNode, mt_core_Template, Resource, core_mt_Resource, Script, mt_core_Script, ASTNode, ScriptDescriptor, Statement, mt_core_ScriptDescriptor, mt_expressions_Parenthesis, mt_expressions_Literal, mt_expressions_StringLiteral, Literal, mt_core_Service, Method_, mt_core_Method, Parameter_, mt_core_Parameter, mt_expressions_Expression, mt_expressions_CallSet, Call, mt_expressions_Call, mt_expressions_Not, mt_expressions_Operator, mt_statements_Feature, mt_statements_Text, mt_expressions_IntegerLiteral, mt_expressions_DoubleLiteral, mt_expressions_BooleanLiteral, mt_expressions_NullLiteral, mt_statements_Statement, mt_statements_Comment, mt_statements_If, If, mt_statements_For},
    associations={file7, post8, statements10, resources0, imports1, scripts2, descriptor4, statements5, operands22, expression24, methods12, parameters13, calls14, arguments15, filter17, expression20, expression41, condition26, thenStatements28, elseStatements31, elseIf34, iterator36, statements38},
    generalizations={gen_mt_core_FilePath_ASTNode, gen_mt_core_Metamodel_Resource, gen_mt_core_Template_Resource, gen_mt_core_Script_ASTNode, gen_mt_core_ScriptDescriptor_ASTNode, gen_mt_expressions_Parenthesis_Expression, gen_mt_expressions_Literal_Expression, gen_mt_expressions_StringLiteral_Literal, gen_mt_core_Service_Resource, gen_mt_expressions_Expression_ASTNode, gen_mt_expressions_CallSet_Expression, gen_mt_expressions_Call_ASTNode, gen_mt_expressions_Not_Expression, gen_mt_expressions_Operator_Expression, gen_mt_statements_Feature_Statement, gen_mt_statements_Text_Statement, gen_mt_expressions_IntegerLiteral_Literal, gen_mt_expressions_DoubleLiteral_Literal, gen_mt_expressions_BooleanLiteral_Literal, gen_mt_expressions_NullLiteral_Literal, gen_mt_statements_Statement_ASTNode, gen_mt_statements_Comment_Statement, gen_mt_statements_If_Statement, gen_mt_statements_For_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)