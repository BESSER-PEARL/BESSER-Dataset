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
Severity: Enumeration = Enumeration(
    name="Severity",
    literals={
            EnumerationLiteral(name="critic"),
			EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning")
    }
)

# Classes
ACG_LocatedElement = Class(name="ACG::LocatedElement", is_abstract=True)
ACG_ACG = Class(name="ACG::ACG")
LocatedElement = Class(name="LocatedElement")
ACGElement = Class(name="ACGElement")
ACG_ACGElement = Class(name="ACG::ACGElement", is_abstract=True)
ACG = Class(name="ACG")
ACG_Function = Class(name="ACG::Function")
ACG_Parameter = Class(name="ACG::Parameter")
VariableDecl = Class(name="VariableDecl")
ACG_Node = Class(name="ACG::Node", is_abstract=True)
StatementBlock = Class(name="StatementBlock")
ACG_ASMNode = Class(name="ACG::ASMNode")
Node = Class(name="Node")
ACG_CodeNode = Class(name="ACG::CodeNode")
ACG_SimpleNode = Class(name="ACG::SimpleNode")
ACG_StatementBlock = Class(name="ACG::StatementBlock", is_abstract=True)
Statement = Class(name="Statement")
ACG_Statement = Class(name="ACG::Statement", is_abstract=True)
ACG_CompoundStat = Class(name="ACG::CompoundStat", is_abstract=True)
ACG_ForEachStat = Class(name="ACG::ForEachStat")
CompoundStat = Class(name="CompoundStat")
Parameter_ = Class(name="Parameter")
Expression = Class(name="Expression")
ACG_Attribute = Class(name="ACG::Attribute")
ACG_OperationStat = Class(name="ACG::OperationStat")
ACG_ConditionalStat = Class(name="ACG::ConditionalStat")
ACG_LetStat = Class(name="ACG::LetStat")
ACG_AnalyzeStat = Class(name="ACG::AnalyzeStat")
ACG_ReportStat = Class(name="ACG::ReportStat")
ACG_OnceStat = Class(name="ACG::OnceStat")
ACG_VariableStat = Class(name="ACG::VariableStat")
ACG_ParamStat = Class(name="ACG::ParamStat")
ACG_EmitStat = Class(name="ACG::EmitStat", is_abstract=True)
ACG_LabelStat = Class(name="ACG::LabelStat")
EmitStat = Class(name="EmitStat")
ACG_NewStat = Class(name="ACG::NewStat")
ACG_NewinStat = Class(name="ACG::NewinStat")
ACG_DeleteStat = Class(name="ACG::DeleteStat")
ACG_DupStat = Class(name="ACG::DupStat")
ACG_DupX1Stat = Class(name="ACG::DupX1Stat")
ACG_PopStat = Class(name="ACG::PopStat")
ACG_SwapStat = Class(name="ACG::SwapStat")
ACG_IterateStat = Class(name="ACG::IterateStat")
ACG_EndIterateStat = Class(name="ACG::EndIterateStat")
ACG_GetAsmStat = Class(name="ACG::GetAsmStat")
ACG_FindMEStat = Class(name="ACG::FindMEStat")
ACG_PushTStat = Class(name="ACG::PushTStat")
ACG_FieldStat = Class(name="ACG::FieldStat")
ACG_PushDStat = Class(name="ACG::PushDStat")
ACG_LoadStat = Class(name="ACG::LoadStat")
ACG_StoreStat = Class(name="ACG::StoreStat")
ACG_CallStat = Class(name="ACG::CallStat")
ACG_PCallStat = Class(name="ACG::PCallStat")
ACG_SuperCallStat = Class(name="ACG::SuperCallStat")
ACG_GetStat = Class(name="ACG::GetStat")
ACG_SetStat = Class(name="ACG::SetStat")
ACG_EmitWithLabelRefStat = Class(name="ACG::EmitWithLabelRefStat", is_abstract=True)
LabelStat = Class(name="LabelStat")
ACG_IfStat = Class(name="ACG::IfStat")
EmitWithLabelRefStat = Class(name="EmitWithLabelRefStat")
ACG_GotoStat = Class(name="ACG::GotoStat")
ACG_VariableDecl = Class(name="ACG::VariableDecl")
ACG_Expression = Class(name="ACG::Expression", is_abstract=True)
ACG_VariableExp = Class(name="ACG::VariableExp")
ACG_SelfExp = Class(name="ACG::SelfExp")
ACG_LastExp = Class(name="ACG::LastExp")
ACG_IfExp = Class(name="ACG::IfExp")
ACG_PushFStat = Class(name="ACG::PushFStat")
ACG_EmitWithOperandStat = Class(name="ACG::EmitWithOperandStat", is_abstract=True)
ACG_PushStat = Class(name="ACG::PushStat")
EmitWithOperandStat = Class(name="EmitWithOperandStat")
ACG_PushIStat = Class(name="ACG::PushIStat")
ACG_IsAExp = Class(name="ACG::IsAExp")
ACG_LetExp = Class(name="ACG::LetExp")
ACG_PropertyCallExp = Class(name="ACG::PropertyCallExp", is_abstract=True)
ACG_NavigationExp = Class(name="ACG::NavigationExp")
PropertyCallExp = Class(name="PropertyCallExp")
ACG_IteratorExp = Class(name="ACG::IteratorExp")
ACG_OperatorCallExp = Class(name="ACG::OperatorCallExp")
OperationCallExp = Class(name="OperationCallExp")
ACG_LiteralExp = Class(name="ACG::LiteralExp", is_abstract=True)
ACG_OclUndefinedExp = Class(name="ACG::OclUndefinedExp")
LiteralExp = Class(name="LiteralExp")
ACG_CollectionExp = Class(name="ACG::CollectionExp", is_abstract=True)
ACG_SequenceExp = Class(name="ACG::SequenceExp")
CollectionExp = Class(name="CollectionExp")
ACG_BooleanExp = Class(name="ACG::BooleanExp")
ACG_IntegerExp = Class(name="ACG::IntegerExp")
ACG_StringExp = Class(name="ACG::StringExp")
ACG_OperationCallExp = Class(name="ACG::OperationCallExp")

# ACG_LocatedElement class attributes and methods
ACG_LocatedElement_location: Property = Property(name="location", type=StringType)
ACG_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
ACG_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
ACG_LocatedElement.attributes={ACG_LocatedElement_commentsBefore, ACG_LocatedElement_commentsAfter, ACG_LocatedElement_location}

# ACG_ACG class attributes and methods
ACG_ACG_metamodel: Property = Property(name="metamodel", type=StringType)
ACG_ACG_startsWith: Property = Property(name="startsWith", type=StringType)
ACG_ACG.attributes={ACG_ACG_startsWith, ACG_ACG_metamodel}

# LocatedElement class attributes and methods

# ACGElement class attributes and methods

# ACG_ACGElement class attributes and methods

# ACG class attributes and methods

# ACG_Function class attributes and methods
ACG_Function_context: Property = Property(name="context", type=StringType)
ACG_Function_name: Property = Property(name="name", type=StringType)
ACG_Function.attributes={ACG_Function_name, ACG_Function_context}

# ACG_Parameter class attributes and methods

# VariableDecl class attributes and methods

# ACG_Node class attributes and methods
ACG_Node_element: Property = Property(name="element", type=StringType)
ACG_Node_mode: Property = Property(name="mode", type=StringType)
ACG_Node.attributes={ACG_Node_element, ACG_Node_mode}

# StatementBlock class attributes and methods

# ACG_ASMNode class attributes and methods

# Node class attributes and methods

# ACG_CodeNode class attributes and methods

# ACG_SimpleNode class attributes and methods

# ACG_StatementBlock class attributes and methods

# Statement class attributes and methods

# ACG_Statement class attributes and methods

# ACG_CompoundStat class attributes and methods

# ACG_ForEachStat class attributes and methods

# CompoundStat class attributes and methods

# Parameter class attributes and methods

# Expression class attributes and methods

# ACG_Attribute class attributes and methods
ACG_Attribute_context: Property = Property(name="context", type=StringType)
ACG_Attribute_name: Property = Property(name="name", type=StringType)
ACG_Attribute.attributes={ACG_Attribute_context, ACG_Attribute_name}

# ACG_OperationStat class attributes and methods

# ACG_ConditionalStat class attributes and methods

# ACG_LetStat class attributes and methods

# ACG_AnalyzeStat class attributes and methods
ACG_AnalyzeStat_mode: Property = Property(name="mode", type=StringType)
ACG_AnalyzeStat.attributes={ACG_AnalyzeStat_mode}

# ACG_ReportStat class attributes and methods
ACG_ReportStat_severity: Property = Property(name="severity", type=StringType)
ACG_ReportStat.attributes={ACG_ReportStat_severity}

# ACG_OnceStat class attributes and methods

# ACG_VariableStat class attributes and methods

# ACG_ParamStat class attributes and methods

# ACG_EmitStat class attributes and methods

# ACG_LabelStat class attributes and methods
ACG_LabelStat_name: Property = Property(name="name", type=StringType)
ACG_LabelStat.attributes={ACG_LabelStat_name}

# EmitStat class attributes and methods

# ACG_NewStat class attributes and methods

# ACG_NewinStat class attributes and methods

# ACG_DeleteStat class attributes and methods

# ACG_DupStat class attributes and methods

# ACG_DupX1Stat class attributes and methods

# ACG_PopStat class attributes and methods

# ACG_SwapStat class attributes and methods

# ACG_IterateStat class attributes and methods

# ACG_EndIterateStat class attributes and methods

# ACG_GetAsmStat class attributes and methods

# ACG_FindMEStat class attributes and methods

# ACG_PushTStat class attributes and methods

# ACG_FieldStat class attributes and methods

# ACG_PushDStat class attributes and methods

# ACG_LoadStat class attributes and methods

# ACG_StoreStat class attributes and methods

# ACG_CallStat class attributes and methods

# ACG_PCallStat class attributes and methods

# ACG_SuperCallStat class attributes and methods

# ACG_GetStat class attributes and methods

# ACG_SetStat class attributes and methods

# ACG_EmitWithLabelRefStat class attributes and methods

# LabelStat class attributes and methods

# ACG_IfStat class attributes and methods

# EmitWithLabelRefStat class attributes and methods

# ACG_GotoStat class attributes and methods

# ACG_VariableDecl class attributes and methods
ACG_VariableDecl_name: Property = Property(name="name", type=StringType)
ACG_VariableDecl.attributes={ACG_VariableDecl_name}

# ACG_Expression class attributes and methods

# ACG_VariableExp class attributes and methods

# ACG_SelfExp class attributes and methods

# ACG_LastExp class attributes and methods

# ACG_IfExp class attributes and methods

# ACG_PushFStat class attributes and methods

# ACG_EmitWithOperandStat class attributes and methods

# ACG_PushStat class attributes and methods

# EmitWithOperandStat class attributes and methods

# ACG_PushIStat class attributes and methods

# ACG_IsAExp class attributes and methods
ACG_IsAExp_type: Property = Property(name="type", type=StringType)
ACG_IsAExp.attributes={ACG_IsAExp_type}

# ACG_LetExp class attributes and methods

# ACG_PropertyCallExp class attributes and methods
ACG_PropertyCallExp_name: Property = Property(name="name", type=StringType)
ACG_PropertyCallExp.attributes={ACG_PropertyCallExp_name}

# ACG_NavigationExp class attributes and methods

# PropertyCallExp class attributes and methods

# ACG_IteratorExp class attributes and methods

# ACG_OperatorCallExp class attributes and methods

# OperationCallExp class attributes and methods

# ACG_LiteralExp class attributes and methods

# ACG_OclUndefinedExp class attributes and methods

# LiteralExp class attributes and methods

# ACG_CollectionExp class attributes and methods

# ACG_SequenceExp class attributes and methods

# CollectionExp class attributes and methods

# ACG_BooleanExp class attributes and methods
ACG_BooleanExp_value: Property = Property(name="value", type=StringType)
ACG_BooleanExp.attributes={ACG_BooleanExp_value}

# ACG_IntegerExp class attributes and methods
ACG_IntegerExp_value: Property = Property(name="value", type=StringType)
ACG_IntegerExp.attributes={ACG_IntegerExp_value}

# ACG_StringExp class attributes and methods
ACG_StringExp_value: Property = Property(name="value", type=StringType)
ACG_StringExp.attributes={ACG_StringExp_value}

# ACG_OperationCallExp class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="", type=ACG_ACG, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=ACGElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acg1: BinaryAssociation = BinaryAssociation(
    name="acg1",
    ends={
        Property(name="3", type=ACG_ACGElement, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=ACG, multiplicity=Multiplicity(1, 1))
    }
)
body7: BinaryAssociation = BinaryAssociation(
    name="body7",
    ends={
        Property(name="Expression8", type=ACG_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_Attribute", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard9: BinaryAssociation = BinaryAssociation(
    name="guard9",
    ends={
        Property(name="Expression10", type=ACG_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_Node", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name11: BinaryAssociation = BinaryAssociation(
    name="name11",
    ends={
        Property(name="Expression12", type=ACG_ASMNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_ASMNode", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements13: BinaryAssociation = BinaryAssociation(
    name="statements13",
    ends={
        Property(name="Statement", type=ACG_StatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_StatementBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator14: BinaryAssociation = BinaryAssociation(
    name="iterator14",
    ends={
        Property(name="VariableDecl", type=ACG_ForEachStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_ForEachStat", type=VariableDecl, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters4: BinaryAssociation = BinaryAssociation(
    name="parameters4",
    ends={
        Property(name="Parameter", type=ACG_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_Function", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body5: BinaryAssociation = BinaryAssociation(
    name="body5",
    ends={
        Property(name="Expression", type=ACG_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_Function6", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name20: BinaryAssociation = BinaryAssociation(
    name="name20",
    ends={
        Property(name="ACG_VariableStat21", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Expression22", type=ACG_VariableStat, multiplicity=Multiplicity(1, 1))
    }
)
context23: BinaryAssociation = BinaryAssociation(
    name="context23",
    ends={
        Property(name="Expression24", type=ACG_OperationStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_OperationStat", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name25: BinaryAssociation = BinaryAssociation(
    name="name25",
    ends={
        Property(name="Expression27", type=ACG_OperationStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_OperationStat26", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition28: BinaryAssociation = BinaryAssociation(
    name="condition28",
    ends={
        Property(name="Expression29", type=ACG_ConditionalStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_ConditionalStat", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatements30: BinaryAssociation = BinaryAssociation(
    name="elseStatements30",
    ends={
        Property(name="Statement32", type=ACG_ConditionalStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_ConditionalStat31", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable33: BinaryAssociation = BinaryAssociation(
    name="variable33",
    ends={
        Property(name="VariableDecl34", type=ACG_LetStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_LetStat", type=VariableDecl, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value35: BinaryAssociation = BinaryAssociation(
    name="value35",
    ends={
        Property(name="Expression37", type=ACG_LetStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_LetStat36", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target38: BinaryAssociation = BinaryAssociation(
    name="target38",
    ends={
        Property(name="Expression39", type=ACG_AnalyzeStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_AnalyzeStat", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection15: BinaryAssociation = BinaryAssociation(
    name="collection15",
    ends={
        Property(name="Expression17", type=ACG_ForEachStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_ForEachStat16", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition18: BinaryAssociation = BinaryAssociation(
    name="definition18",
    ends={
        Property(name="Expression19", type=ACG_VariableStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_VariableStat", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name42: BinaryAssociation = BinaryAssociation(
    name="name42",
    ends={
        Property(name="Expression43", type=ACG_FieldStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_FieldStat", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type44: BinaryAssociation = BinaryAssociation(
    name="type44",
    ends={
        Property(name="Expression46", type=ACG_FieldStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_FieldStat45", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name47: BinaryAssociation = BinaryAssociation(
    name="name47",
    ends={
        Property(name="Expression48", type=ACG_ParamStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_ParamStat", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="Expression51", type=ACG_ParamStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_ParamStat50", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
id52: BinaryAssociation = BinaryAssociation(
    name="id52",
    ends={
        Property(name="Expression53", type=ACG_LabelStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_LabelStat", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message40: BinaryAssociation = BinaryAssociation(
    name="message40",
    ends={
        Property(name="Expression41", type=ACG_ReportStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_ReportStat", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label56: BinaryAssociation = BinaryAssociation(
    name="label56",
    ends={
        Property(name="LabelStat", type=ACG_EmitWithLabelRefStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_EmitWithLabelRefStat", type=LabelStat, multiplicity=Multiplicity(1, 1))
    }
)
variable57: BinaryAssociation = BinaryAssociation(
    name="variable57",
    ends={
        Property(name="VariableDecl58", type=ACG_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_VariableExp", type=VariableDecl, multiplicity=Multiplicity(1, 1))
    }
)
operand54: BinaryAssociation = BinaryAssociation(
    name="operand54",
    ends={
        Property(name="Expression55", type=ACG_EmitWithOperandStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_EmitWithOperandStat", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source67: BinaryAssociation = BinaryAssociation(
    name="source67",
    ends={
        Property(name="Expression68", type=ACG_IsAExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_IsAExp", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable69: BinaryAssociation = BinaryAssociation(
    name="variable69",
    ends={
        Property(name="VariableDecl70", type=ACG_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_LetExp", type=VariableDecl, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value71: BinaryAssociation = BinaryAssociation(
    name="value71",
    ends={
        Property(name="Expression73", type=ACG_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_LetExp72", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in74: BinaryAssociation = BinaryAssociation(
    name="in74",
    ends={
        Property(name="Expression76", type=ACG_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_LetExp75", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source77: BinaryAssociation = BinaryAssociation(
    name="source77",
    ends={
        Property(name="Expression78", type=ACG_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_PropertyCallExp", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition59: BinaryAssociation = BinaryAssociation(
    name="condition59",
    ends={
        Property(name="Expression60", type=ACG_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_IfExp", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator79: BinaryAssociation = BinaryAssociation(
    name="iterator79",
    ends={
        Property(name="VariableDecl80", type=ACG_IteratorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_IteratorExp", type=VariableDecl, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExp61: BinaryAssociation = BinaryAssociation(
    name="thenExp61",
    ends={
        Property(name="Expression63", type=ACG_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_IfExp62", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExp64: BinaryAssociation = BinaryAssociation(
    name="elseExp64",
    ends={
        Property(name="Expression66", type=ACG_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_IfExp65", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments84: BinaryAssociation = BinaryAssociation(
    name="arguments84",
    ends={
        Property(name="Expression85", type=ACG_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_OperationCallExp", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements86: BinaryAssociation = BinaryAssociation(
    name="elements86",
    ends={
        Property(name="Expression87", type=ACG_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_CollectionExp", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body81: BinaryAssociation = BinaryAssociation(
    name="body81",
    ends={
        Property(name="Expression83", type=ACG_IteratorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ACG_IteratorExp82", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_ACG_ACG_LocatedElement = Generalization(general=LocatedElement, specific=ACG_ACG)
gen_ACG_ACGElement_LocatedElement = Generalization(general=LocatedElement, specific=ACG_ACGElement)
gen_ACG_Function_ACGElement = Generalization(general=ACGElement, specific=ACG_Function)
gen_ACG_Parameter_VariableDecl = Generalization(general=VariableDecl, specific=ACG_Parameter)
gen_ACG_Node_ACGElement = Generalization(general=ACGElement, specific=ACG_Node)
gen_ACG_Node_StatementBlock = Generalization(general=StatementBlock, specific=ACG_Node)
gen_ACG_ASMNode_Node = Generalization(general=Node, specific=ACG_ASMNode)
gen_ACG_CodeNode_Node = Generalization(general=Node, specific=ACG_CodeNode)
gen_ACG_SimpleNode_Node = Generalization(general=Node, specific=ACG_SimpleNode)
gen_ACG_StatementBlock_LocatedElement = Generalization(general=LocatedElement, specific=ACG_StatementBlock)
gen_ACG_Statement_LocatedElement = Generalization(general=LocatedElement, specific=ACG_Statement)
gen_ACG_CompoundStat_Statement = Generalization(general=Statement, specific=ACG_CompoundStat)
gen_ACG_CompoundStat_StatementBlock = Generalization(general=StatementBlock, specific=ACG_CompoundStat)
gen_ACG_ForEachStat_CompoundStat = Generalization(general=CompoundStat, specific=ACG_ForEachStat)
gen_ACG_Attribute_ACGElement = Generalization(general=ACGElement, specific=ACG_Attribute)
gen_ACG_OperationStat_CompoundStat = Generalization(general=CompoundStat, specific=ACG_OperationStat)
gen_ACG_ConditionalStat_CompoundStat = Generalization(general=CompoundStat, specific=ACG_ConditionalStat)
gen_ACG_LetStat_CompoundStat = Generalization(general=CompoundStat, specific=ACG_LetStat)
gen_ACG_AnalyzeStat_CompoundStat = Generalization(general=CompoundStat, specific=ACG_AnalyzeStat)
gen_ACG_ReportStat_Statement = Generalization(general=Statement, specific=ACG_ReportStat)
gen_ACG_OnceStat_CompoundStat = Generalization(general=CompoundStat, specific=ACG_OnceStat)
gen_ACG_VariableStat_CompoundStat = Generalization(general=CompoundStat, specific=ACG_VariableStat)
gen_ACG_ParamStat_Statement = Generalization(general=Statement, specific=ACG_ParamStat)
gen_ACG_EmitStat_Statement = Generalization(general=Statement, specific=ACG_EmitStat)
gen_ACG_LabelStat_EmitStat = Generalization(general=EmitStat, specific=ACG_LabelStat)
gen_ACG_NewStat_EmitStat = Generalization(general=EmitStat, specific=ACG_NewStat)
gen_ACG_NewinStat_EmitStat = Generalization(general=EmitStat, specific=ACG_NewinStat)
gen_ACG_DeleteStat_EmitStat = Generalization(general=EmitStat, specific=ACG_DeleteStat)
gen_ACG_DupStat_EmitStat = Generalization(general=EmitStat, specific=ACG_DupStat)
gen_ACG_DupX1Stat_EmitStat = Generalization(general=EmitStat, specific=ACG_DupX1Stat)
gen_ACG_PopStat_EmitStat = Generalization(general=EmitStat, specific=ACG_PopStat)
gen_ACG_SwapStat_EmitStat = Generalization(general=EmitStat, specific=ACG_SwapStat)
gen_ACG_IterateStat_EmitStat = Generalization(general=EmitStat, specific=ACG_IterateStat)
gen_ACG_EndIterateStat_EmitStat = Generalization(general=EmitStat, specific=ACG_EndIterateStat)
gen_ACG_GetAsmStat_EmitStat = Generalization(general=EmitStat, specific=ACG_GetAsmStat)
gen_ACG_FindMEStat_EmitStat = Generalization(general=EmitStat, specific=ACG_FindMEStat)
gen_ACG_PushTStat_EmitStat = Generalization(general=EmitStat, specific=ACG_PushTStat)
gen_ACG_FieldStat_Statement = Generalization(general=Statement, specific=ACG_FieldStat)
gen_ACG_PushDStat_EmitWithOperandStat = Generalization(general=EmitWithOperandStat, specific=ACG_PushDStat)
gen_ACG_LoadStat_EmitWithOperandStat = Generalization(general=EmitWithOperandStat, specific=ACG_LoadStat)
gen_ACG_StoreStat_EmitWithOperandStat = Generalization(general=EmitWithOperandStat, specific=ACG_StoreStat)
gen_ACG_CallStat_EmitWithOperandStat = Generalization(general=EmitWithOperandStat, specific=ACG_CallStat)
gen_ACG_PCallStat_EmitWithOperandStat = Generalization(general=EmitWithOperandStat, specific=ACG_PCallStat)
gen_ACG_SuperCallStat_EmitWithOperandStat = Generalization(general=EmitWithOperandStat, specific=ACG_SuperCallStat)
gen_ACG_GetStat_EmitWithOperandStat = Generalization(general=EmitWithOperandStat, specific=ACG_GetStat)
gen_ACG_SetStat_EmitWithOperandStat = Generalization(general=EmitWithOperandStat, specific=ACG_SetStat)
gen_ACG_EmitWithLabelRefStat_EmitStat = Generalization(general=EmitStat, specific=ACG_EmitWithLabelRefStat)
gen_ACG_IfStat_EmitWithLabelRefStat = Generalization(general=EmitWithLabelRefStat, specific=ACG_IfStat)
gen_ACG_GotoStat_EmitWithLabelRefStat = Generalization(general=EmitWithLabelRefStat, specific=ACG_GotoStat)
gen_ACG_VariableDecl_LocatedElement = Generalization(general=LocatedElement, specific=ACG_VariableDecl)
gen_ACG_Expression_LocatedElement = Generalization(general=LocatedElement, specific=ACG_Expression)
gen_ACG_VariableExp_Expression = Generalization(general=Expression, specific=ACG_VariableExp)
gen_ACG_SelfExp_Expression = Generalization(general=Expression, specific=ACG_SelfExp)
gen_ACG_LastExp_Expression = Generalization(general=Expression, specific=ACG_LastExp)
gen_ACG_IfExp_Expression = Generalization(general=Expression, specific=ACG_IfExp)
gen_ACG_PushFStat_EmitStat = Generalization(general=EmitStat, specific=ACG_PushFStat)
gen_ACG_EmitWithOperandStat_EmitStat = Generalization(general=EmitStat, specific=ACG_EmitWithOperandStat)
gen_ACG_PushStat_EmitWithOperandStat = Generalization(general=EmitWithOperandStat, specific=ACG_PushStat)
gen_ACG_PushIStat_EmitWithOperandStat = Generalization(general=EmitWithOperandStat, specific=ACG_PushIStat)
gen_ACG_IsAExp_Expression = Generalization(general=Expression, specific=ACG_IsAExp)
gen_ACG_LetExp_Expression = Generalization(general=Expression, specific=ACG_LetExp)
gen_ACG_PropertyCallExp_Expression = Generalization(general=Expression, specific=ACG_PropertyCallExp)
gen_ACG_NavigationExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=ACG_NavigationExp)
gen_ACG_IteratorExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=ACG_IteratorExp)
gen_ACG_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=ACG_OperatorCallExp)
gen_ACG_LiteralExp_Expression = Generalization(general=Expression, specific=ACG_LiteralExp)
gen_ACG_OclUndefinedExp_LiteralExp = Generalization(general=LiteralExp, specific=ACG_OclUndefinedExp)
gen_ACG_CollectionExp_LiteralExp = Generalization(general=LiteralExp, specific=ACG_CollectionExp)
gen_ACG_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=ACG_SequenceExp)
gen_ACG_BooleanExp_LiteralExp = Generalization(general=LiteralExp, specific=ACG_BooleanExp)
gen_ACG_IntegerExp_LiteralExp = Generalization(general=LiteralExp, specific=ACG_IntegerExp)
gen_ACG_StringExp_LiteralExp = Generalization(general=LiteralExp, specific=ACG_StringExp)
gen_ACG_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=ACG_OperationCallExp)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={ACG_LocatedElement, ACG_ACG, LocatedElement, ACGElement, ACG_ACGElement, ACG, ACG_Function, ACG_Parameter, VariableDecl, ACG_Node, StatementBlock, ACG_ASMNode, Node, ACG_CodeNode, ACG_SimpleNode, ACG_StatementBlock, Statement, ACG_Statement, ACG_CompoundStat, ACG_ForEachStat, CompoundStat, Parameter_, Expression, ACG_Attribute, ACG_OperationStat, ACG_ConditionalStat, ACG_LetStat, ACG_AnalyzeStat, ACG_ReportStat, ACG_OnceStat, ACG_VariableStat, ACG_ParamStat, ACG_EmitStat, ACG_LabelStat, EmitStat, ACG_NewStat, ACG_NewinStat, ACG_DeleteStat, ACG_DupStat, ACG_DupX1Stat, ACG_PopStat, ACG_SwapStat, ACG_IterateStat, ACG_EndIterateStat, ACG_GetAsmStat, ACG_FindMEStat, ACG_PushTStat, ACG_FieldStat, ACG_PushDStat, ACG_LoadStat, ACG_StoreStat, ACG_CallStat, ACG_PCallStat, ACG_SuperCallStat, ACG_GetStat, ACG_SetStat, ACG_EmitWithLabelRefStat, LabelStat, ACG_IfStat, EmitWithLabelRefStat, ACG_GotoStat, ACG_VariableDecl, ACG_Expression, ACG_VariableExp, ACG_SelfExp, ACG_LastExp, ACG_IfExp, ACG_PushFStat, ACG_EmitWithOperandStat, ACG_PushStat, EmitWithOperandStat, ACG_PushIStat, ACG_IsAExp, ACG_LetExp, ACG_PropertyCallExp, ACG_NavigationExp, PropertyCallExp, ACG_IteratorExp, ACG_OperatorCallExp, OperationCallExp, ACG_LiteralExp, ACG_OclUndefinedExp, LiteralExp, ACG_CollectionExp, ACG_SequenceExp, CollectionExp, ACG_BooleanExp, ACG_IntegerExp, ACG_StringExp, ACG_OperationCallExp, Severity},
    associations={elements0, acg1, body7, guard9, name11, statements13, iterator14, parameters4, body5, name20, context23, name25, condition28, elseStatements30, variable33, value35, target38, collection15, definition18, name42, type44, name47, type49, id52, message40, label56, variable57, operand54, source67, variable69, value71, in74, source77, condition59, iterator79, thenExp61, elseExp64, arguments84, elements86, body81},
    generalizations={gen_ACG_ACG_LocatedElement, gen_ACG_ACGElement_LocatedElement, gen_ACG_Function_ACGElement, gen_ACG_Parameter_VariableDecl, gen_ACG_Node_ACGElement, gen_ACG_Node_StatementBlock, gen_ACG_ASMNode_Node, gen_ACG_CodeNode_Node, gen_ACG_SimpleNode_Node, gen_ACG_StatementBlock_LocatedElement, gen_ACG_Statement_LocatedElement, gen_ACG_CompoundStat_Statement, gen_ACG_CompoundStat_StatementBlock, gen_ACG_ForEachStat_CompoundStat, gen_ACG_Attribute_ACGElement, gen_ACG_OperationStat_CompoundStat, gen_ACG_ConditionalStat_CompoundStat, gen_ACG_LetStat_CompoundStat, gen_ACG_AnalyzeStat_CompoundStat, gen_ACG_ReportStat_Statement, gen_ACG_OnceStat_CompoundStat, gen_ACG_VariableStat_CompoundStat, gen_ACG_ParamStat_Statement, gen_ACG_EmitStat_Statement, gen_ACG_LabelStat_EmitStat, gen_ACG_NewStat_EmitStat, gen_ACG_NewinStat_EmitStat, gen_ACG_DeleteStat_EmitStat, gen_ACG_DupStat_EmitStat, gen_ACG_DupX1Stat_EmitStat, gen_ACG_PopStat_EmitStat, gen_ACG_SwapStat_EmitStat, gen_ACG_IterateStat_EmitStat, gen_ACG_EndIterateStat_EmitStat, gen_ACG_GetAsmStat_EmitStat, gen_ACG_FindMEStat_EmitStat, gen_ACG_PushTStat_EmitStat, gen_ACG_FieldStat_Statement, gen_ACG_PushDStat_EmitWithOperandStat, gen_ACG_LoadStat_EmitWithOperandStat, gen_ACG_StoreStat_EmitWithOperandStat, gen_ACG_CallStat_EmitWithOperandStat, gen_ACG_PCallStat_EmitWithOperandStat, gen_ACG_SuperCallStat_EmitWithOperandStat, gen_ACG_GetStat_EmitWithOperandStat, gen_ACG_SetStat_EmitWithOperandStat, gen_ACG_EmitWithLabelRefStat_EmitStat, gen_ACG_IfStat_EmitWithLabelRefStat, gen_ACG_GotoStat_EmitWithLabelRefStat, gen_ACG_VariableDecl_LocatedElement, gen_ACG_Expression_LocatedElement, gen_ACG_VariableExp_Expression, gen_ACG_SelfExp_Expression, gen_ACG_LastExp_Expression, gen_ACG_IfExp_Expression, gen_ACG_PushFStat_EmitStat, gen_ACG_EmitWithOperandStat_EmitStat, gen_ACG_PushStat_EmitWithOperandStat, gen_ACG_PushIStat_EmitWithOperandStat, gen_ACG_IsAExp_Expression, gen_ACG_LetExp_Expression, gen_ACG_PropertyCallExp_Expression, gen_ACG_NavigationExp_PropertyCallExp, gen_ACG_IteratorExp_PropertyCallExp, gen_ACG_OperatorCallExp_OperationCallExp, gen_ACG_LiteralExp_Expression, gen_ACG_OclUndefinedExp_LiteralExp, gen_ACG_CollectionExp_LiteralExp, gen_ACG_SequenceExp_CollectionExp, gen_ACG_BooleanExp_LiteralExp, gen_ACG_IntegerExp_LiteralExp, gen_ACG_StringExp_LiteralExp, gen_ACG_OperationCallExp_PropertyCallExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)