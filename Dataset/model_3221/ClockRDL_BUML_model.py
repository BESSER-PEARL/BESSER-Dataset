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
UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="UNOT"),
			EnumerationLiteral(name="UMINUS"),
			EnumerationLiteral(name="UPLUS")
    }
)

BinaryOperator: Enumeration = Enumeration(
    name="BinaryOperator",
    literals={
            EnumerationLiteral(name="BGE"),
			EnumerationLiteral(name="BPLUS"),
			EnumerationLiteral(name="BMINUS"),
			EnumerationLiteral(name="BMUL"),
			EnumerationLiteral(name="BDIV"),
			EnumerationLiteral(name="BMOD"),
			EnumerationLiteral(name="BNOR"),
			EnumerationLiteral(name="BNAND"),
			EnumerationLiteral(name="BXOR"),
			EnumerationLiteral(name="BOR"),
			EnumerationLiteral(name="BAND"),
			EnumerationLiteral(name="BEQ"),
			EnumerationLiteral(name="BNE"),
			EnumerationLiteral(name="BLT"),
			EnumerationLiteral(name="BGT"),
			EnumerationLiteral(name="BLE")
    }
)

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="MINUSASSIGN"),
			EnumerationLiteral(name="PLUSASSIGN"),
			EnumerationLiteral(name="MULTASSIGN"),
			EnumerationLiteral(name="MODASSIGN"),
			EnumerationLiteral(name="DIVASSIGN"),
			EnumerationLiteral(name="ORASSIGN"),
			EnumerationLiteral(name="ANDASSIGN")
    }
)

# Classes
ClockRDL_kernel_Declaration = Class(name="ClockRDL::kernel::Declaration", is_abstract=True)
ClockRDL_kernel_NamedDeclaration = Class(name="ClockRDL::kernel::NamedDeclaration", is_abstract=True)
kernel_Declaration = Class(name="kernel::Declaration")
kernel_NamedElement = Class(name="kernel::NamedElement")
ClockRDL_kernel_Statement = Class(name="ClockRDL::kernel::Statement", is_abstract=True)
ClockRDL_kernel_Expression = Class(name="ClockRDL::kernel::Expression", is_abstract=True)
kernel_Element = Class(name="kernel::Element")
kernel_Statement = Class(name="kernel::Statement")
ClockRDL_kernel_Element = Class(name="ClockRDL::kernel::Element", is_abstract=True)
ClockRDL_kernel_NamedElement = Class(name="ClockRDL::kernel::NamedElement", is_abstract=True)
Element = Class(name="Element")
ClockRDL_expressions_SelectedExp = Class(name="ClockRDL::expressions::SelectedExp")
ClockRDL_expressions_FunctionCallExp = Class(name="ClockRDL::expressions::FunctionCallExp")
expressions_PrefixedExp = Class(name="expressions::PrefixedExp")
ClockRDL_expressions_ReferenceExp = Class(name="ClockRDL::expressions::ReferenceExp")
ClockRDL_expressions_Literal = Class(name="ClockRDL::expressions::Literal", is_abstract=True)
Expression = Class(name="Expression")
ClockRDL_expressions_ParenExp = Class(name="ClockRDL::expressions::ParenExp")
kernel_Expression = Class(name="kernel::Expression")
ClockRDL_expressions_PrefixedExp = Class(name="ClockRDL::expressions::PrefixedExp", is_abstract=True)
ClockRDL_expressions_IndexedExp = Class(name="ClockRDL::expressions::IndexedExp")
PrefixedExp = Class(name="PrefixedExp")
ClockRDL_expressions_UnaryExp = Class(name="ClockRDL::expressions::UnaryExp")
kernel_NamedDeclaration = Class(name="kernel::NamedDeclaration")
ClockRDL_expressions_ClockReference = Class(name="ClockRDL::expressions::ClockReference")
ReferenceExp = Class(name="ReferenceExp")
ClockRDL_literals_IntegerLiteral = Class(name="ClockRDL::literals::IntegerLiteral")
Literal = Class(name="Literal")
ClockRDL_literals_BooleanLiteral = Class(name="ClockRDL::literals::BooleanLiteral")
ClockRDL_expressions_BinaryExp = Class(name="ClockRDL::expressions::BinaryExp")
ClockRDL_expressions_ConditionalExp = Class(name="ClockRDL::expressions::ConditionalExp")
ClockRDL_literals_QueueLiteral = Class(name="ClockRDL::literals::QueueLiteral")
ClockRDL_literals_ClockLiteral = Class(name="ClockRDL::literals::ClockLiteral")
ClockRDL_literals_ArrayLiteral = Class(name="ClockRDL::literals::ArrayLiteral")
ClockRDL_literals_FieldLiteral = Class(name="ClockRDL::literals::FieldLiteral")
expressions_Literal = Class(name="expressions::Literal")
ClockRDL_literals_RecordLiteral = Class(name="ClockRDL::literals::RecordLiteral")
literals_FieldLiteral = Class(name="literals::FieldLiteral")
ClockRDL_statements_ConditionalStmt = Class(name="ClockRDL::statements::ConditionalStmt")
statements_BlockStmt = Class(name="statements::BlockStmt")
ClockRDL_statements_LoopStmt = Class(name="ClockRDL::statements::LoopStmt")
ClockRDL_statements_AssignmentStmt = Class(name="ClockRDL::statements::AssignmentStmt")
Statement = Class(name="Statement")
ClockRDL_declarations_ClockDecl = Class(name="ClockRDL::declarations::ClockDecl")
NamedDeclaration = Class(name="NamedDeclaration")
literals_ClockLiteral = Class(name="literals::ClockLiteral")
ClockRDL_declarations_VariableDecl = Class(name="ClockRDL::declarations::VariableDecl")
ClockRDL_declarations_ConstantDecl = Class(name="ClockRDL::declarations::ConstantDecl")
ClockRDL_statements_ReturnStmt = Class(name="ClockRDL::statements::ReturnStmt")
ClockRDL_statements_BlockStmt = Class(name="ClockRDL::statements::BlockStmt")
expressions_ClockReference = Class(name="expressions::ClockReference")
ClockRDL_declarations_AbstractRelationDecl = Class(name="ClockRDL::declarations::AbstractRelationDecl")
declarations_LibraryItemDecl = Class(name="declarations::LibraryItemDecl")
VariableDecl = Class(name="VariableDecl")
ClockRDL_declarations_ArgumentDecl = Class(name="ClockRDL::declarations::ArgumentDecl")
ClockRDL_declarations_AbstractFunctionDecl = Class(name="ClockRDL::declarations::AbstractFunctionDecl", is_abstract=True)
declarations_ArgumentDecl = Class(name="declarations::ArgumentDecl")
ClockRDL_declarations_PrimitiveFunctionDecl = Class(name="ClockRDL::declarations::PrimitiveFunctionDecl")
AbstractFunctionDecl = Class(name="AbstractFunctionDecl")
ClockRDL_declarations_FunctionDecl = Class(name="ClockRDL::declarations::FunctionDecl")
ClockRDL_declarations_TransitionDecl = Class(name="ClockRDL::declarations::TransitionDecl")
Declaration = Class(name="Declaration")
ClockRDL_declarations_RelationInstanceDecl = Class(name="ClockRDL::declarations::RelationInstanceDecl")
declarations_AbstractRelationDecl = Class(name="declarations::AbstractRelationDecl")
declarations_FormalToActualMapEntry = Class(name="declarations::FormalToActualMapEntry")
ClockRDL_declarations_FormalToActualMapEntry = Class(name="ClockRDL::declarations::FormalToActualMapEntry")
ClockRDL_declarations_PrimitiveRelationDecl = Class(name="ClockRDL::declarations::PrimitiveRelationDecl")
AbstractRelationDecl = Class(name="AbstractRelationDecl")
declarations_TransitionDecl = Class(name="declarations::TransitionDecl")
ClockRDL_declarations_CompositeRelationDecl = Class(name="ClockRDL::declarations::CompositeRelationDecl")
declarations_ClockDecl = Class(name="declarations::ClockDecl")
declarations_RelationInstanceDecl = Class(name="declarations::RelationInstanceDecl")
ClockRDL_declarations_SystemDecl = Class(name="ClockRDL::declarations::SystemDecl")
RepositoryDecl = Class(name="RepositoryDecl")
ClockRDL_declarations_LibraryItemDecl = Class(name="ClockRDL::declarations::LibraryItemDecl", is_abstract=True)
declarations_RepositoryDecl = Class(name="declarations::RepositoryDecl")
ClockRDL_declarations_RepositoryDecl = Class(name="ClockRDL::declarations::RepositoryDecl")
ClockRDL_declarations_LibraryDecl = Class(name="ClockRDL::declarations::LibraryDecl")

# ClockRDL_kernel_Declaration class attributes and methods

# ClockRDL_kernel_NamedDeclaration class attributes and methods

# kernel_Declaration class attributes and methods

# kernel_NamedElement class attributes and methods

# ClockRDL_kernel_Statement class attributes and methods

# ClockRDL_kernel_Expression class attributes and methods

# kernel_Element class attributes and methods

# kernel_Statement class attributes and methods

# ClockRDL_kernel_Element class attributes and methods

# ClockRDL_kernel_NamedElement class attributes and methods
ClockRDL_kernel_NamedElement_name: Property = Property(name="name", type=StringType)
ClockRDL_kernel_NamedElement.attributes={ClockRDL_kernel_NamedElement_name}

# Element class attributes and methods

# ClockRDL_expressions_SelectedExp class attributes and methods
ClockRDL_expressions_SelectedExp_selector: Property = Property(name="selector", type=StringType)
ClockRDL_expressions_SelectedExp.attributes={ClockRDL_expressions_SelectedExp_selector}

# ClockRDL_expressions_FunctionCallExp class attributes and methods

# expressions_PrefixedExp class attributes and methods

# ClockRDL_expressions_ReferenceExp class attributes and methods

# ClockRDL_expressions_Literal class attributes and methods

# Expression class attributes and methods

# ClockRDL_expressions_ParenExp class attributes and methods

# kernel_Expression class attributes and methods

# ClockRDL_expressions_PrefixedExp class attributes and methods

# ClockRDL_expressions_IndexedExp class attributes and methods

# PrefixedExp class attributes and methods

# ClockRDL_expressions_UnaryExp class attributes and methods
ClockRDL_expressions_UnaryExp_operator: Property = Property(name="operator", type=StringType)
ClockRDL_expressions_UnaryExp.attributes={ClockRDL_expressions_UnaryExp_operator}

# kernel_NamedDeclaration class attributes and methods

# ClockRDL_expressions_ClockReference class attributes and methods

# ReferenceExp class attributes and methods

# ClockRDL_literals_IntegerLiteral class attributes and methods
ClockRDL_literals_IntegerLiteral_value: Property = Property(name="value", type=StringType)
ClockRDL_literals_IntegerLiteral.attributes={ClockRDL_literals_IntegerLiteral_value}

# Literal class attributes and methods

# ClockRDL_literals_BooleanLiteral class attributes and methods
ClockRDL_literals_BooleanLiteral_value: Property = Property(name="value", type=StringType)
ClockRDL_literals_BooleanLiteral.attributes={ClockRDL_literals_BooleanLiteral_value}

# ClockRDL_expressions_BinaryExp class attributes and methods
ClockRDL_expressions_BinaryExp_operator: Property = Property(name="operator", type=StringType)
ClockRDL_expressions_BinaryExp.attributes={ClockRDL_expressions_BinaryExp_operator}

# ClockRDL_expressions_ConditionalExp class attributes and methods

# ClockRDL_literals_QueueLiteral class attributes and methods

# ClockRDL_literals_ClockLiteral class attributes and methods
ClockRDL_literals_ClockLiteral_name: Property = Property(name="name", type=StringType)
ClockRDL_literals_ClockLiteral_isInternal: Property = Property(name="isInternal", type=StringType)
ClockRDL_literals_ClockLiteral.attributes={ClockRDL_literals_ClockLiteral_isInternal, ClockRDL_literals_ClockLiteral_name}

# ClockRDL_literals_ArrayLiteral class attributes and methods

# ClockRDL_literals_FieldLiteral class attributes and methods

# expressions_Literal class attributes and methods

# ClockRDL_literals_RecordLiteral class attributes and methods

# literals_FieldLiteral class attributes and methods

# ClockRDL_statements_ConditionalStmt class attributes and methods

# statements_BlockStmt class attributes and methods

# ClockRDL_statements_LoopStmt class attributes and methods

# ClockRDL_statements_AssignmentStmt class attributes and methods
ClockRDL_statements_AssignmentStmt_operator: Property = Property(name="operator", type=StringType)
ClockRDL_statements_AssignmentStmt.attributes={ClockRDL_statements_AssignmentStmt_operator}

# Statement class attributes and methods

# ClockRDL_declarations_ClockDecl class attributes and methods

# NamedDeclaration class attributes and methods

# literals_ClockLiteral class attributes and methods

# ClockRDL_declarations_VariableDecl class attributes and methods

# ClockRDL_declarations_ConstantDecl class attributes and methods

# ClockRDL_statements_ReturnStmt class attributes and methods

# ClockRDL_statements_BlockStmt class attributes and methods

# expressions_ClockReference class attributes and methods

# ClockRDL_declarations_AbstractRelationDecl class attributes and methods

# declarations_LibraryItemDecl class attributes and methods

# VariableDecl class attributes and methods

# ClockRDL_declarations_ArgumentDecl class attributes and methods

# ClockRDL_declarations_AbstractFunctionDecl class attributes and methods

# declarations_ArgumentDecl class attributes and methods

# ClockRDL_declarations_PrimitiveFunctionDecl class attributes and methods

# AbstractFunctionDecl class attributes and methods

# ClockRDL_declarations_FunctionDecl class attributes and methods

# ClockRDL_declarations_TransitionDecl class attributes and methods

# Declaration class attributes and methods

# ClockRDL_declarations_RelationInstanceDecl class attributes and methods
ClockRDL_declarations_RelationInstanceDecl_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
ClockRDL_declarations_RelationInstanceDecl.attributes={ClockRDL_declarations_RelationInstanceDecl_qualifiedName}

# declarations_AbstractRelationDecl class attributes and methods

# declarations_FormalToActualMapEntry class attributes and methods

# ClockRDL_declarations_FormalToActualMapEntry class attributes and methods
ClockRDL_declarations_FormalToActualMapEntry_key: Property = Property(name="key", type=StringType)
ClockRDL_declarations_FormalToActualMapEntry.attributes={ClockRDL_declarations_FormalToActualMapEntry_key}

# ClockRDL_declarations_PrimitiveRelationDecl class attributes and methods

# AbstractRelationDecl class attributes and methods

# declarations_TransitionDecl class attributes and methods

# ClockRDL_declarations_CompositeRelationDecl class attributes and methods

# declarations_ClockDecl class attributes and methods

# declarations_RelationInstanceDecl class attributes and methods

# ClockRDL_declarations_SystemDecl class attributes and methods

# RepositoryDecl class attributes and methods

# ClockRDL_declarations_LibraryItemDecl class attributes and methods

# declarations_RepositoryDecl class attributes and methods

# ClockRDL_declarations_RepositoryDecl class attributes and methods

# ClockRDL_declarations_LibraryDecl class attributes and methods

# Relationships
index3: BinaryAssociation = BinaryAssociation(
    name="index3",
    ends={
        Property(name="kernel_Expression4", type=ClockRDL_expressions_IndexedExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_IndexedExp", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments5: BinaryAssociation = BinaryAssociation(
    name="arguments5",
    ends={
        Property(name="kernel_Expression6", type=ClockRDL_expressions_FunctionCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_FunctionCallExp", type=kernel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp0: BinaryAssociation = BinaryAssociation(
    name="exp0",
    ends={
        Property(name="kernel_Expression", type=ClockRDL_expressions_ParenExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_ParenExp", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
prefix1: BinaryAssociation = BinaryAssociation(
    name="prefix1",
    ends={
        Property(name="kernel_Expression2", type=ClockRDL_expressions_PrefixedExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_PrefixedExp", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref7: BinaryAssociation = BinaryAssociation(
    name="ref7",
    ends={
        Property(name="kernel_NamedDeclaration", type=ClockRDL_expressions_ReferenceExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_ReferenceExp", type=kernel_NamedDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
trueBranch17: BinaryAssociation = BinaryAssociation(
    name="trueBranch17",
    ends={
        Property(name="kernel_Expression19", type=ClockRDL_expressions_ConditionalExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_ConditionalExp18", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseBranch20: BinaryAssociation = BinaryAssociation(
    name="falseBranch20",
    ends={
        Property(name="kernel_Expression22", type=ClockRDL_expressions_ConditionalExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_ConditionalExp21", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand8: BinaryAssociation = BinaryAssociation(
    name="operand8",
    ends={
        Property(name="kernel_Expression9", type=ClockRDL_expressions_UnaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_UnaryExp", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs10: BinaryAssociation = BinaryAssociation(
    name="lhs10",
    ends={
        Property(name="kernel_Expression11", type=ClockRDL_expressions_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_BinaryExp", type=kernel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs12: BinaryAssociation = BinaryAssociation(
    name="rhs12",
    ends={
        Property(name="kernel_Expression14", type=ClockRDL_expressions_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_BinaryExp13", type=kernel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="kernel_Expression16", type=ClockRDL_expressions_ConditionalExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_expressions_ConditionalExp", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value28: BinaryAssociation = BinaryAssociation(
    name="value28",
    ends={
        Property(name="kernel_Expression29", type=ClockRDL_literals_QueueLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_literals_QueueLiteral", type=kernel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value23: BinaryAssociation = BinaryAssociation(
    name="value23",
    ends={
        Property(name="kernel_Expression24", type=ClockRDL_literals_ArrayLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_literals_ArrayLiteral", type=kernel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value25: BinaryAssociation = BinaryAssociation(
    name="value25",
    ends={
        Property(name="kernel_Expression26", type=ClockRDL_literals_FieldLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_literals_FieldLiteral", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value27: BinaryAssociation = BinaryAssociation(
    name="value27",
    ends={
        Property(name="literals_FieldLiteral", type=ClockRDL_literals_RecordLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_literals_RecordLiteral", type=literals_FieldLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition35: BinaryAssociation = BinaryAssociation(
    name="condition35",
    ends={
        Property(name="kernel_Expression36", type=ClockRDL_statements_ConditionalStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_statements_ConditionalStmt", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trueBranch37: BinaryAssociation = BinaryAssociation(
    name="trueBranch37",
    ends={
        Property(name="statements_BlockStmt", type=ClockRDL_statements_ConditionalStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_statements_ConditionalStmt38", type=statements_BlockStmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseBranch39: BinaryAssociation = BinaryAssociation(
    name="falseBranch39",
    ends={
        Property(name="statements_BlockStmt41", type=ClockRDL_statements_ConditionalStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_statements_ConditionalStmt40", type=statements_BlockStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs30: BinaryAssociation = BinaryAssociation(
    name="lhs30",
    ends={
        Property(name="kernel_Expression31", type=ClockRDL_statements_AssignmentStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_statements_AssignmentStmt", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs32: BinaryAssociation = BinaryAssociation(
    name="rhs32",
    ends={
        Property(name="kernel_Expression34", type=ClockRDL_statements_AssignmentStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_statements_AssignmentStmt33", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements51: BinaryAssociation = BinaryAssociation(
    name="statements51",
    ends={
        Property(name="ClockRDL_statements_BlockStmt52", type=kernel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="kernel_Statement", type=ClockRDL_statements_BlockStmt, multiplicity=Multiplicity(1, 1))
    }
)
initial53: BinaryAssociation = BinaryAssociation(
    name="initial53",
    ends={
        Property(name="literals_ClockLiteral", type=ClockRDL_declarations_ClockDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_ClockDecl", type=literals_ClockLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial54: BinaryAssociation = BinaryAssociation(
    name="initial54",
    ends={
        Property(name="kernel_Expression55", type=ClockRDL_declarations_VariableDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_VariableDecl", type=kernel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition42: BinaryAssociation = BinaryAssociation(
    name="condition42",
    ends={
        Property(name="kernel_Expression43", type=ClockRDL_statements_LoopStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_statements_LoopStmt", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body44: BinaryAssociation = BinaryAssociation(
    name="body44",
    ends={
        Property(name="statements_BlockStmt46", type=ClockRDL_statements_LoopStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_statements_LoopStmt45", type=statements_BlockStmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp47: BinaryAssociation = BinaryAssociation(
    name="exp47",
    ends={
        Property(name="kernel_Expression48", type=ClockRDL_statements_ReturnStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_statements_ReturnStmt", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarations49: BinaryAssociation = BinaryAssociation(
    name="declarations49",
    ends={
        Property(name="kernel_NamedDeclaration50", type=ClockRDL_statements_BlockStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_statements_BlockStmt", type=kernel_NamedDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard59: BinaryAssociation = BinaryAssociation(
    name="guard59",
    ends={
        Property(name="ClockRDL_declarations_TransitionDecl", type=kernel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="kernel_Expression60", type=ClockRDL_declarations_TransitionDecl, multiplicity=Multiplicity(1, 1))
    }
)
vector61: BinaryAssociation = BinaryAssociation(
    name="vector61",
    ends={
        Property(name="expressions_ClockReference", type=ClockRDL_declarations_TransitionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_TransitionDecl62", type=expressions_ClockReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action63: BinaryAssociation = BinaryAssociation(
    name="action63",
    ends={
        Property(name="kernel_Statement65", type=ClockRDL_declarations_TransitionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_TransitionDecl64", type=kernel_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments66: BinaryAssociation = BinaryAssociation(
    name="arguments66",
    ends={
        Property(name="declarations_ArgumentDecl67", type=ClockRDL_declarations_AbstractRelationDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_AbstractRelationDecl", type=declarations_ArgumentDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments56: BinaryAssociation = BinaryAssociation(
    name="arguments56",
    ends={
        Property(name="declarations_ArgumentDecl", type=ClockRDL_declarations_AbstractFunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_AbstractFunctionDecl", type=declarations_ArgumentDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body57: BinaryAssociation = BinaryAssociation(
    name="body57",
    ends={
        Property(name="statements_BlockStmt58", type=ClockRDL_declarations_FunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_FunctionDecl", type=statements_BlockStmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
relation75: BinaryAssociation = BinaryAssociation(
    name="relation75",
    ends={
        Property(name="declarations_AbstractRelationDecl", type=ClockRDL_declarations_RelationInstanceDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_RelationInstanceDecl", type=declarations_AbstractRelationDecl, multiplicity=Multiplicity(0, 1))
    }
)
argumentMap76: BinaryAssociation = BinaryAssociation(
    name="argumentMap76",
    ends={
        Property(name="declarations_FormalToActualMapEntry", type=ClockRDL_declarations_RelationInstanceDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_RelationInstanceDecl77", type=declarations_FormalToActualMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value78: BinaryAssociation = BinaryAssociation(
    name="value78",
    ends={
        Property(name="kernel_Expression79", type=ClockRDL_declarations_FormalToActualMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_FormalToActualMapEntry", type=kernel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarations68: BinaryAssociation = BinaryAssociation(
    name="declarations68",
    ends={
        Property(name="kernel_NamedDeclaration70", type=ClockRDL_declarations_AbstractRelationDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_AbstractRelationDecl69", type=kernel_NamedDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions71: BinaryAssociation = BinaryAssociation(
    name="transitions71",
    ends={
        Property(name="declarations_TransitionDecl", type=ClockRDL_declarations_PrimitiveRelationDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_PrimitiveRelationDecl", type=declarations_TransitionDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalClocks72: BinaryAssociation = BinaryAssociation(
    name="internalClocks72",
    ends={
        Property(name="declarations_ClockDecl", type=ClockRDL_declarations_CompositeRelationDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_CompositeRelationDecl", type=declarations_ClockDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instances73: BinaryAssociation = BinaryAssociation(
    name="instances73",
    ends={
        Property(name="declarations_RelationInstanceDecl", type=ClockRDL_declarations_CompositeRelationDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_CompositeRelationDecl74", type=declarations_RelationInstanceDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root86: BinaryAssociation = BinaryAssociation(
    name="root86",
    ends={
        Property(name="declarations_RelationInstanceDecl87", type=ClockRDL_declarations_SystemDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_SystemDecl", type=declarations_RelationInstanceDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalDecl80: BinaryAssociation = BinaryAssociation(
    name="formalDecl80",
    ends={
        Property(name="kernel_Declaration", type=ClockRDL_declarations_FormalToActualMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="ClockRDL_declarations_FormalToActualMapEntry81", type=kernel_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
library82: BinaryAssociation = BinaryAssociation(
    name="library82",
    ends={
        Property(name="#", type=ClockRDL_declarations_LibraryItemDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=declarations_RepositoryDecl, multiplicity=Multiplicity(1, 1))
    }
)
libraries83: BinaryAssociation = BinaryAssociation(
    name="libraries83",
    ends={
        Property(name="#85", type=ClockRDL_declarations_RepositoryDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="084", type=declarations_LibraryItemDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ClockRDL_kernel_Declaration_Element = Generalization(general=Element, specific=ClockRDL_kernel_Declaration)
gen_ClockRDL_kernel_NamedDeclaration_kernel_Declaration = Generalization(general=kernel_Declaration, specific=ClockRDL_kernel_NamedDeclaration)
gen_ClockRDL_kernel_NamedDeclaration_kernel_NamedElement = Generalization(general=kernel_NamedElement, specific=ClockRDL_kernel_NamedDeclaration)
gen_ClockRDL_kernel_Statement_Element = Generalization(general=Element, specific=ClockRDL_kernel_Statement)
gen_ClockRDL_kernel_Expression_kernel_Element = Generalization(general=kernel_Element, specific=ClockRDL_kernel_Expression)
gen_ClockRDL_kernel_Expression_kernel_Statement = Generalization(general=kernel_Statement, specific=ClockRDL_kernel_Expression)
gen_ClockRDL_kernel_NamedElement_Element = Generalization(general=Element, specific=ClockRDL_kernel_NamedElement)
gen_ClockRDL_expressions_SelectedExp_PrefixedExp = Generalization(general=PrefixedExp, specific=ClockRDL_expressions_SelectedExp)
gen_ClockRDL_expressions_FunctionCallExp_expressions_PrefixedExp = Generalization(general=expressions_PrefixedExp, specific=ClockRDL_expressions_FunctionCallExp)
gen_ClockRDL_expressions_FunctionCallExp_kernel_Statement = Generalization(general=kernel_Statement, specific=ClockRDL_expressions_FunctionCallExp)
gen_ClockRDL_expressions_ReferenceExp_Expression = Generalization(general=Expression, specific=ClockRDL_expressions_ReferenceExp)
gen_ClockRDL_expressions_Literal_Expression = Generalization(general=Expression, specific=ClockRDL_expressions_Literal)
gen_ClockRDL_expressions_ParenExp_Expression = Generalization(general=Expression, specific=ClockRDL_expressions_ParenExp)
gen_ClockRDL_expressions_PrefixedExp_Expression = Generalization(general=Expression, specific=ClockRDL_expressions_PrefixedExp)
gen_ClockRDL_expressions_IndexedExp_PrefixedExp = Generalization(general=PrefixedExp, specific=ClockRDL_expressions_IndexedExp)
gen_ClockRDL_expressions_UnaryExp_Expression = Generalization(general=Expression, specific=ClockRDL_expressions_UnaryExp)
gen_ClockRDL_expressions_ClockReference_ReferenceExp = Generalization(general=ReferenceExp, specific=ClockRDL_expressions_ClockReference)
gen_ClockRDL_literals_IntegerLiteral_Literal = Generalization(general=Literal, specific=ClockRDL_literals_IntegerLiteral)
gen_ClockRDL_literals_BooleanLiteral_Literal = Generalization(general=Literal, specific=ClockRDL_literals_BooleanLiteral)
gen_ClockRDL_expressions_BinaryExp_Expression = Generalization(general=Expression, specific=ClockRDL_expressions_BinaryExp)
gen_ClockRDL_expressions_ConditionalExp_Expression = Generalization(general=Expression, specific=ClockRDL_expressions_ConditionalExp)
gen_ClockRDL_literals_QueueLiteral_Literal = Generalization(general=Literal, specific=ClockRDL_literals_QueueLiteral)
gen_ClockRDL_literals_ClockLiteral_Literal = Generalization(general=Literal, specific=ClockRDL_literals_ClockLiteral)
gen_ClockRDL_literals_ArrayLiteral_Literal = Generalization(general=Literal, specific=ClockRDL_literals_ArrayLiteral)
gen_ClockRDL_literals_FieldLiteral_kernel_NamedElement = Generalization(general=kernel_NamedElement, specific=ClockRDL_literals_FieldLiteral)
gen_ClockRDL_literals_FieldLiteral_expressions_Literal = Generalization(general=expressions_Literal, specific=ClockRDL_literals_FieldLiteral)
gen_ClockRDL_literals_RecordLiteral_Literal = Generalization(general=Literal, specific=ClockRDL_literals_RecordLiteral)
gen_ClockRDL_statements_ConditionalStmt_Statement = Generalization(general=Statement, specific=ClockRDL_statements_ConditionalStmt)
gen_ClockRDL_statements_LoopStmt_Statement = Generalization(general=Statement, specific=ClockRDL_statements_LoopStmt)
gen_ClockRDL_statements_AssignmentStmt_Statement = Generalization(general=Statement, specific=ClockRDL_statements_AssignmentStmt)
gen_ClockRDL_declarations_ClockDecl_NamedDeclaration = Generalization(general=NamedDeclaration, specific=ClockRDL_declarations_ClockDecl)
gen_ClockRDL_declarations_VariableDecl_NamedDeclaration = Generalization(general=NamedDeclaration, specific=ClockRDL_declarations_VariableDecl)
gen_ClockRDL_statements_ReturnStmt_Statement = Generalization(general=Statement, specific=ClockRDL_statements_ReturnStmt)
gen_ClockRDL_statements_BlockStmt_Statement = Generalization(general=Statement, specific=ClockRDL_statements_BlockStmt)
gen_ClockRDL_declarations_AbstractRelationDecl_kernel_NamedDeclaration = Generalization(general=kernel_NamedDeclaration, specific=ClockRDL_declarations_AbstractRelationDecl)
gen_ClockRDL_declarations_AbstractRelationDecl_declarations_LibraryItemDecl = Generalization(general=declarations_LibraryItemDecl, specific=ClockRDL_declarations_AbstractRelationDecl)
gen_ClockRDL_declarations_ConstantDecl_VariableDecl = Generalization(general=VariableDecl, specific=ClockRDL_declarations_ConstantDecl)
gen_ClockRDL_declarations_ArgumentDecl_NamedDeclaration = Generalization(general=NamedDeclaration, specific=ClockRDL_declarations_ArgumentDecl)
gen_ClockRDL_declarations_AbstractFunctionDecl_NamedDeclaration = Generalization(general=NamedDeclaration, specific=ClockRDL_declarations_AbstractFunctionDecl)
gen_ClockRDL_declarations_PrimitiveFunctionDecl_AbstractFunctionDecl = Generalization(general=AbstractFunctionDecl, specific=ClockRDL_declarations_PrimitiveFunctionDecl)
gen_ClockRDL_declarations_FunctionDecl_AbstractFunctionDecl = Generalization(general=AbstractFunctionDecl, specific=ClockRDL_declarations_FunctionDecl)
gen_ClockRDL_declarations_TransitionDecl_Declaration = Generalization(general=Declaration, specific=ClockRDL_declarations_TransitionDecl)
gen_ClockRDL_declarations_RelationInstanceDecl_NamedDeclaration = Generalization(general=NamedDeclaration, specific=ClockRDL_declarations_RelationInstanceDecl)
gen_ClockRDL_declarations_PrimitiveRelationDecl_AbstractRelationDecl = Generalization(general=AbstractRelationDecl, specific=ClockRDL_declarations_PrimitiveRelationDecl)
gen_ClockRDL_declarations_CompositeRelationDecl_AbstractRelationDecl = Generalization(general=AbstractRelationDecl, specific=ClockRDL_declarations_CompositeRelationDecl)
gen_ClockRDL_declarations_SystemDecl_RepositoryDecl = Generalization(general=RepositoryDecl, specific=ClockRDL_declarations_SystemDecl)
gen_ClockRDL_declarations_LibraryItemDecl_Declaration = Generalization(general=Declaration, specific=ClockRDL_declarations_LibraryItemDecl)
gen_ClockRDL_declarations_RepositoryDecl_NamedDeclaration = Generalization(general=NamedDeclaration, specific=ClockRDL_declarations_RepositoryDecl)
gen_ClockRDL_declarations_LibraryDecl_declarations_RepositoryDecl = Generalization(general=declarations_RepositoryDecl, specific=ClockRDL_declarations_LibraryDecl)
gen_ClockRDL_declarations_LibraryDecl_declarations_LibraryItemDecl = Generalization(general=declarations_LibraryItemDecl, specific=ClockRDL_declarations_LibraryDecl)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={ClockRDL_kernel_Declaration, ClockRDL_kernel_NamedDeclaration, kernel_Declaration, kernel_NamedElement, ClockRDL_kernel_Statement, ClockRDL_kernel_Expression, kernel_Element, kernel_Statement, ClockRDL_kernel_Element, ClockRDL_kernel_NamedElement, Element, ClockRDL_expressions_SelectedExp, ClockRDL_expressions_FunctionCallExp, expressions_PrefixedExp, ClockRDL_expressions_ReferenceExp, ClockRDL_expressions_Literal, Expression, ClockRDL_expressions_ParenExp, kernel_Expression, ClockRDL_expressions_PrefixedExp, ClockRDL_expressions_IndexedExp, PrefixedExp, ClockRDL_expressions_UnaryExp, kernel_NamedDeclaration, ClockRDL_expressions_ClockReference, ReferenceExp, ClockRDL_literals_IntegerLiteral, Literal, ClockRDL_literals_BooleanLiteral, ClockRDL_expressions_BinaryExp, ClockRDL_expressions_ConditionalExp, ClockRDL_literals_QueueLiteral, ClockRDL_literals_ClockLiteral, ClockRDL_literals_ArrayLiteral, ClockRDL_literals_FieldLiteral, expressions_Literal, ClockRDL_literals_RecordLiteral, literals_FieldLiteral, ClockRDL_statements_ConditionalStmt, statements_BlockStmt, ClockRDL_statements_LoopStmt, ClockRDL_statements_AssignmentStmt, Statement, ClockRDL_declarations_ClockDecl, NamedDeclaration, literals_ClockLiteral, ClockRDL_declarations_VariableDecl, ClockRDL_declarations_ConstantDecl, ClockRDL_statements_ReturnStmt, ClockRDL_statements_BlockStmt, expressions_ClockReference, ClockRDL_declarations_AbstractRelationDecl, declarations_LibraryItemDecl, VariableDecl, ClockRDL_declarations_ArgumentDecl, ClockRDL_declarations_AbstractFunctionDecl, declarations_ArgumentDecl, ClockRDL_declarations_PrimitiveFunctionDecl, AbstractFunctionDecl, ClockRDL_declarations_FunctionDecl, ClockRDL_declarations_TransitionDecl, Declaration, ClockRDL_declarations_RelationInstanceDecl, declarations_AbstractRelationDecl, declarations_FormalToActualMapEntry, ClockRDL_declarations_FormalToActualMapEntry, ClockRDL_declarations_PrimitiveRelationDecl, AbstractRelationDecl, declarations_TransitionDecl, ClockRDL_declarations_CompositeRelationDecl, declarations_ClockDecl, declarations_RelationInstanceDecl, ClockRDL_declarations_SystemDecl, RepositoryDecl, ClockRDL_declarations_LibraryItemDecl, declarations_RepositoryDecl, ClockRDL_declarations_RepositoryDecl, ClockRDL_declarations_LibraryDecl, UnaryOperator, BinaryOperator, AssignmentOperator},
    associations={index3, arguments5, exp0, prefix1, ref7, trueBranch17, falseBranch20, operand8, lhs10, rhs12, condition15, value28, value23, value25, value27, condition35, trueBranch37, falseBranch39, lhs30, rhs32, statements51, initial53, initial54, condition42, body44, exp47, declarations49, guard59, vector61, action63, arguments66, arguments56, body57, relation75, argumentMap76, value78, declarations68, transitions71, internalClocks72, instances73, root86, formalDecl80, library82, libraries83},
    generalizations={gen_ClockRDL_kernel_Declaration_Element, gen_ClockRDL_kernel_NamedDeclaration_kernel_Declaration, gen_ClockRDL_kernel_NamedDeclaration_kernel_NamedElement, gen_ClockRDL_kernel_Statement_Element, gen_ClockRDL_kernel_Expression_kernel_Element, gen_ClockRDL_kernel_Expression_kernel_Statement, gen_ClockRDL_kernel_NamedElement_Element, gen_ClockRDL_expressions_SelectedExp_PrefixedExp, gen_ClockRDL_expressions_FunctionCallExp_expressions_PrefixedExp, gen_ClockRDL_expressions_FunctionCallExp_kernel_Statement, gen_ClockRDL_expressions_ReferenceExp_Expression, gen_ClockRDL_expressions_Literal_Expression, gen_ClockRDL_expressions_ParenExp_Expression, gen_ClockRDL_expressions_PrefixedExp_Expression, gen_ClockRDL_expressions_IndexedExp_PrefixedExp, gen_ClockRDL_expressions_UnaryExp_Expression, gen_ClockRDL_expressions_ClockReference_ReferenceExp, gen_ClockRDL_literals_IntegerLiteral_Literal, gen_ClockRDL_literals_BooleanLiteral_Literal, gen_ClockRDL_expressions_BinaryExp_Expression, gen_ClockRDL_expressions_ConditionalExp_Expression, gen_ClockRDL_literals_QueueLiteral_Literal, gen_ClockRDL_literals_ClockLiteral_Literal, gen_ClockRDL_literals_ArrayLiteral_Literal, gen_ClockRDL_literals_FieldLiteral_kernel_NamedElement, gen_ClockRDL_literals_FieldLiteral_expressions_Literal, gen_ClockRDL_literals_RecordLiteral_Literal, gen_ClockRDL_statements_ConditionalStmt_Statement, gen_ClockRDL_statements_LoopStmt_Statement, gen_ClockRDL_statements_AssignmentStmt_Statement, gen_ClockRDL_declarations_ClockDecl_NamedDeclaration, gen_ClockRDL_declarations_VariableDecl_NamedDeclaration, gen_ClockRDL_statements_ReturnStmt_Statement, gen_ClockRDL_statements_BlockStmt_Statement, gen_ClockRDL_declarations_AbstractRelationDecl_kernel_NamedDeclaration, gen_ClockRDL_declarations_AbstractRelationDecl_declarations_LibraryItemDecl, gen_ClockRDL_declarations_ConstantDecl_VariableDecl, gen_ClockRDL_declarations_ArgumentDecl_NamedDeclaration, gen_ClockRDL_declarations_AbstractFunctionDecl_NamedDeclaration, gen_ClockRDL_declarations_PrimitiveFunctionDecl_AbstractFunctionDecl, gen_ClockRDL_declarations_FunctionDecl_AbstractFunctionDecl, gen_ClockRDL_declarations_TransitionDecl_Declaration, gen_ClockRDL_declarations_RelationInstanceDecl_NamedDeclaration, gen_ClockRDL_declarations_PrimitiveRelationDecl_AbstractRelationDecl, gen_ClockRDL_declarations_CompositeRelationDecl_AbstractRelationDecl, gen_ClockRDL_declarations_SystemDecl_RepositoryDecl, gen_ClockRDL_declarations_LibraryItemDecl_Declaration, gen_ClockRDL_declarations_RepositoryDecl_NamedDeclaration, gen_ClockRDL_declarations_LibraryDecl_declarations_RepositoryDecl, gen_ClockRDL_declarations_LibraryDecl_declarations_LibraryItemDecl},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)