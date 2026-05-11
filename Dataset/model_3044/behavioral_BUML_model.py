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
SAMOperatorKindEnum: Enumeration = Enumeration(
    name="SAMOperatorKindEnum",
    literals={
            EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="AND")
    }
)

SAMDerivatorKindEnum: Enumeration = Enumeration(
    name="SAMDerivatorKindEnum",
    literals={
            EnumerationLiteral(name="POPULATION"),
			EnumerationLiteral(name="AGGREGATION"),
			EnumerationLiteral(name="OVERALL")
    }
)

PreconditionKindEnum: Enumeration = Enumeration(
    name="PreconditionKindEnum",
    literals={
            EnumerationLiteral(name="ENABLE"),
			EnumerationLiteral(name="REQUIRED"),
			EnumerationLiteral(name="INHIBIT"),
			EnumerationLiteral(name="NEUTEAL")
    }
)

# Classes
behavioral_bpdm_Dummy = Class(name="behavioral_bpdm_Dummy")
behavioral_actions_Assignment = Class(name="behavioral_actions_Assignment")
StatementWithArgument = Class(name="StatementWithArgument")
Variable = Class(name="Variable")
behavioral_actions_Statement = Class(name="behavioral_actions_Statement", is_abstract=True)
InScope = Class(name="InScope")
behavioral_businesstasks_TaskAgent = Class(name="behavioral_businesstasks_TaskAgent")
behavioral_actions_Block = Class(name="behavioral_actions_Block")
classes_FunctionSignatureImplementation = Class(name="classes_FunctionSignatureImplementation")
classes_InScope = Class(name="classes_InScope")
Statement = Class(name="Statement")
NamedValue = Class(name="NamedValue")
StatementWithNestedBlocks = Class(name="StatementWithNestedBlocks")
behavioral_actions_IfElse = Class(name="behavioral_actions_IfElse")
actions_ConditionalStatement = Class(name="actions_ConditionalStatement")
actions_StatementWithNestedBlocks = Class(name="actions_StatementWithNestedBlocks")
Block = Class(name="Block")
behavioral_actions_WhileLoop = Class(name="behavioral_actions_WhileLoop")
actions_SingleBlockStatement = Class(name="actions_SingleBlockStatement")
behavioral_actions_Foreach = Class(name="behavioral_actions_Foreach")
SingleBlockStatement = Class(name="SingleBlockStatement")
Expression = Class(name="Expression")
Iterator = Class(name="Iterator")
behavioral_actions_Return = Class(name="behavioral_actions_Return")
behavioral_actions_AddLink = Class(name="behavioral_actions_AddLink")
LinkManipulationStatement = Class(name="LinkManipulationStatement")
behavioral_actions_RemoveLink = Class(name="behavioral_actions_RemoveLink")
behavioral_actions_LinkManipulationStatement = Class(name="behavioral_actions_LinkManipulationStatement", is_abstract=True)
behavioral_actions_Sort = Class(name="behavioral_actions_Sort")
behavioral_actions_QueryInvocation = Class(name="behavioral_actions_QueryInvocation")
behavioral_actions_Constant = Class(name="behavioral_actions_Constant")
NamedValueWithOptionalInitExpression = Class(name="NamedValueWithOptionalInitExpression")
collectionexpressions_Iterate = Class(name="collectionexpressions_Iterate")
behavioral_actions_Variable = Class(name="behavioral_actions_Variable")
Assignment = Class(name="Assignment")
behavioral_actions_Iterator = Class(name="behavioral_actions_Iterator")
Foreach = Class(name="Foreach")
Selection = Class(name="Selection")
FromClause = Class(name="FromClause")
GroupBy = Class(name="GroupBy")
Association = Class(name="Association")
behavioral_actions_ExpressionStatement = Class(name="behavioral_actions_ExpressionStatement")
behavioral_actions_StatementWithNestedBlocks = Class(name="behavioral_actions_StatementWithNestedBlocks")
behavioral_actions_SingleBlockStatement = Class(name="behavioral_actions_SingleBlockStatement")
behavioral_actions_StatementWithArgument = Class(name="behavioral_actions_StatementWithArgument", is_abstract=True)
actions_Statement = Class(name="actions_Statement")
expressions_WithArgument = Class(name="expressions_WithArgument")
behavioral_actions_NamedValueWithOptionalInitExpression = Class(name="behavioral_actions_NamedValueWithOptionalInitExpression", is_abstract=True)
NamedValueDeclaration = Class(name="NamedValueDeclaration")
behavioral_actions_ConditionalStatement = Class(name="behavioral_actions_ConditionalStatement", is_abstract=True)
expressions_Conditional = Class(name="expressions_Conditional")
behavioral_rules_Dummy = Class(name="behavioral_rules_Dummy")
behavioral_events_Subscription = Class(name="behavioral_events_Subscription")
NamedElement = Class(name="NamedElement")
DimensionDefinition = Class(name="DimensionDefinition")
behavioral_actions_NamedValueDeclaration = Class(name="behavioral_actions_NamedValueDeclaration")
EventProducer = Class(name="EventProducer")
EventFilter = Class(name="EventFilter")
SapClass = Class(name="SapClass")
behavioral_events_EventProducer = Class(name="behavioral_events_EventProducer", is_abstract=True)
Subscription = Class(name="Subscription")
MethodSignature = Class(name="MethodSignature")
behavioral_events_EventFilter = Class(name="behavioral_events_EventFilter")
behavioral_transactions_Dummy = Class(name="behavioral_transactions_Dummy")
SAMSchemaAction = Class(name="SAMSchemaAction")
behavioral_status_and_action_old_SAMStatusVariable = Class(name="behavioral_status_and_action_old_SAMStatusVariable")
SAMStatusValue = Class(name="SAMStatusValue")
SAMSchemaVariable = Class(name="SAMSchemaVariable")
behavioral_status_and_action_old_SAMDerivator = Class(name="behavioral_status_and_action_old_SAMDerivator")
SAMSchemaDerivator = Class(name="SAMSchemaDerivator")
behavioral_status_and_action_old_SAMStatusValue = Class(name="behavioral_status_and_action_old_SAMStatusValue")
SAMStatusVariable = Class(name="SAMStatusVariable")
behavioral_status_and_action_old_SAMStatusSchema = Class(name="behavioral_status_and_action_old_SAMStatusSchema")
SAMOperator = Class(name="SAMOperator")
behavioral_status_and_action_old_SAMAction = Class(name="behavioral_status_and_action_old_SAMAction")
SAMSchemaValue = Class(name="SAMSchemaValue")
behavioral_status_and_action_old_SAMSchemaVariable = Class(name="behavioral_status_and_action_old_SAMSchemaVariable")
behavioral_status_and_action_old_SAMSchemaValue = Class(name="behavioral_status_and_action_old_SAMSchemaValue")
behavioral_status_and_action_old_SAMOperator = Class(name="behavioral_status_and_action_old_SAMOperator")
SAMStatusSchema = Class(name="SAMStatusSchema")
behavioral_status_and_action_old_SAMSchemaAction = Class(name="behavioral_status_and_action_old_SAMSchemaAction")
SAMAction = Class(name="SAMAction")
behavioral_status_and_action_old_SAMSchemaDerivator = Class(name="behavioral_status_and_action_old_SAMSchemaDerivator")
SAMDerivator = Class(name="SAMDerivator")
behavioral_design_BusinessObjectNode = Class(name="behavioral_design_BusinessObjectNode")
design_StatusVariable = Class(name="design_StatusVariable")
design_Action = Class(name="design_Action")
behavioral_design_StatusVariable = Class(name="behavioral_design_StatusVariable")
AbstractStatusVariable = Class(name="AbstractStatusVariable")
behavioral_design_StatusValue = Class(name="behavioral_design_StatusValue")
AbstractStatusValue = Class(name="AbstractStatusValue")
behavioral_design_Action = Class(name="behavioral_design_Action")
AbstractAction = Class(name="AbstractAction")
behavioral_design_AbstractStatusVariable = Class(name="behavioral_design_AbstractStatusVariable", is_abstract=True)
design_AbstractStatusValue = Class(name="design_AbstractStatusValue")
behavioral_design_AbstractStatusValue = Class(name="behavioral_design_AbstractStatusValue", is_abstract=True)
behavioral_design_AbstractAction = Class(name="behavioral_design_AbstractAction", is_abstract=True)
behavioral_assembly_StatusSchema = Class(name="behavioral_assembly_StatusSchema")
behavioral_design_BusinessObject = Class(name="behavioral_design_BusinessObject")
design_BusinessObjectNode = Class(name="design_BusinessObjectNode")
assembly_SchemaElement = Class(name="assembly_SchemaElement")
behavioral_assembly_Connector = Class(name="behavioral_assembly_Connector", is_abstract=True)
SchemaElement = Class(name="SchemaElement")
assembly_ConnectableElement = Class(name="assembly_ConnectableElement")
behavioral_assembly_Operator = Class(name="behavioral_assembly_Operator")
ConnectableElement = Class(name="ConnectableElement")
behavioral_assembly_ConnectableElement = Class(name="behavioral_assembly_ConnectableElement", is_abstract=True)
behavioral_assembly_ActionProxy = Class(name="behavioral_assembly_ActionProxy")
design_AbstractAction = Class(name="design_AbstractAction")
Signature = Class(name="Signature")
behavioral_assembly_StatusValueProxy = Class(name="behavioral_assembly_StatusValueProxy")
design_StatusValue = Class(name="design_StatusValue")
behavioral_assembly_Transition = Class(name="behavioral_assembly_Transition")
Connector = Class(name="Connector")
behavioral_assembly_Synchroniser = Class(name="behavioral_assembly_Synchroniser")
behavioral_assembly_Precondition = Class(name="behavioral_assembly_Precondition")
behavioral_assembly_StatusVariableProxy = Class(name="behavioral_assembly_StatusVariableProxy")
design_AbstractStatusVariable = Class(name="design_AbstractStatusVariable")
behavioral_assembly_AndOperator = Class(name="behavioral_assembly_AndOperator")
Operator = Class(name="Operator")
behavioral_assembly_OrOperator = Class(name="behavioral_assembly_OrOperator")
behavioral_assembly_RequiredStrategy = Class(name="behavioral_assembly_RequiredStrategy")
Strategy = Class(name="Strategy")
behavioral_assembly_NeutralStrategy = Class(name="behavioral_assembly_NeutralStrategy")
behavioral_assembly_EnablingStrategy = Class(name="behavioral_assembly_EnablingStrategy")
behavioral_assembly_InhibitingStrategy = Class(name="behavioral_assembly_InhibitingStrategy")
behavioral_assembly_Strategy = Class(name="behavioral_assembly_Strategy", is_abstract=True)
behavioral_assembly_SchemaElement = Class(name="behavioral_assembly_SchemaElement", is_abstract=True)
assembly_Strategy = Class(name="assembly_Strategy")

# behavioral_bpdm_Dummy class attributes and methods

# behavioral_actions_Assignment class attributes and methods

# StatementWithArgument class attributes and methods

# Variable class attributes and methods

# behavioral_actions_Statement class attributes and methods
behavioral_actions_Statement_m_getOutermostBlock: Method = Method(name="getOutermostBlock", parameters={}, type=StringType)
behavioral_actions_Statement_m_isSideEffectFree: Method = Method(name="isSideEffectFree", parameters={}, type=BooleanType)
behavioral_actions_Statement_m_isSideEffectFreeForBlock: Method = Method(name="isSideEffectFreeForBlock", parameters={Parameter(name='behavioral_block', type=StringType)}, type=BooleanType)
behavioral_actions_Statement_m_getNamedValuesInScope: Method = Method(name="getNamedValuesInScope", parameters={}, type=StringType)
behavioral_actions_Statement_m_getOwningClass: Method = Method(name="getOwningClass", parameters={}, type=StringType)
behavioral_actions_Statement.methods={behavioral_actions_Statement_m_isSideEffectFree, behavioral_actions_Statement_m_getOutermostBlock, behavioral_actions_Statement_m_getNamedValuesInScope, behavioral_actions_Statement_m_isSideEffectFreeForBlock, behavioral_actions_Statement_m_getOwningClass}

# InScope class attributes and methods

# behavioral_businesstasks_TaskAgent class attributes and methods

# behavioral_actions_Block class attributes and methods
behavioral_actions_Block_m_getOutermostBlock: Method = Method(name="getOutermostBlock", parameters={}, type=StringType)
behavioral_actions_Block_m_localIsSideEffectFree: Method = Method(name="localIsSideEffectFree", parameters={}, type=BooleanType)
behavioral_actions_Block_m_getNamedValuesInScope: Method = Method(name="getNamedValuesInScope", parameters={}, type=StringType)
behavioral_actions_Block_m_getOwningClass: Method = Method(name="getOwningClass", parameters={}, type=StringType)
behavioral_actions_Block.methods={behavioral_actions_Block_m_localIsSideEffectFree, behavioral_actions_Block_m_getOwningClass, behavioral_actions_Block_m_getNamedValuesInScope, behavioral_actions_Block_m_getOutermostBlock}

# classes_FunctionSignatureImplementation class attributes and methods

# classes_InScope class attributes and methods

# Statement class attributes and methods

# NamedValue class attributes and methods

# StatementWithNestedBlocks class attributes and methods

# behavioral_actions_IfElse class attributes and methods
behavioral_actions_IfElse_m_getIfBlock: Method = Method(name="getIfBlock", parameters={}, type=StringType)
behavioral_actions_IfElse_m_getElseBlock: Method = Method(name="getElseBlock", parameters={}, type=StringType)
behavioral_actions_IfElse.methods={behavioral_actions_IfElse_m_getElseBlock, behavioral_actions_IfElse_m_getIfBlock}

# actions_ConditionalStatement class attributes and methods

# actions_StatementWithNestedBlocks class attributes and methods

# Block class attributes and methods

# behavioral_actions_WhileLoop class attributes and methods
behavioral_actions_WhileLoop_m_getLoopBody: Method = Method(name="getLoopBody", parameters={}, type=StringType)
behavioral_actions_WhileLoop.methods={behavioral_actions_WhileLoop_m_getLoopBody}

# actions_SingleBlockStatement class attributes and methods

# behavioral_actions_Foreach class attributes and methods
behavioral_actions_Foreach_parallel: Property = Property(name="parallel", type=BooleanType)
behavioral_actions_Foreach.attributes={behavioral_actions_Foreach_parallel}

# SingleBlockStatement class attributes and methods

# Expression class attributes and methods

# Iterator class attributes and methods

# behavioral_actions_Return class attributes and methods

# behavioral_actions_AddLink class attributes and methods

# LinkManipulationStatement class attributes and methods

# behavioral_actions_RemoveLink class attributes and methods

# behavioral_actions_LinkManipulationStatement class attributes and methods
behavioral_actions_LinkManipulationStatement_at: Property = Property(name="at", type=IntegerType)
behavioral_actions_LinkManipulationStatement.attributes={behavioral_actions_LinkManipulationStatement_at}

# behavioral_actions_Sort class attributes and methods

# behavioral_actions_QueryInvocation class attributes and methods

# behavioral_actions_Constant class attributes and methods

# NamedValueWithOptionalInitExpression class attributes and methods

# collectionexpressions_Iterate class attributes and methods

# behavioral_actions_Variable class attributes and methods
behavioral_actions_Variable_m_getCommonTypeOfAssignments: Method = Method(name="getCommonTypeOfAssignments", parameters={})
behavioral_actions_Variable.methods={behavioral_actions_Variable_m_getCommonTypeOfAssignments}

# Assignment class attributes and methods

# behavioral_actions_Iterator class attributes and methods

# Foreach class attributes and methods

# Selection class attributes and methods

# FromClause class attributes and methods

# GroupBy class attributes and methods

# Association class attributes and methods

# behavioral_actions_ExpressionStatement class attributes and methods

# behavioral_actions_StatementWithNestedBlocks class attributes and methods

# behavioral_actions_SingleBlockStatement class attributes and methods

# behavioral_actions_StatementWithArgument class attributes and methods

# actions_Statement class attributes and methods

# expressions_WithArgument class attributes and methods

# behavioral_actions_NamedValueWithOptionalInitExpression class attributes and methods

# NamedValueDeclaration class attributes and methods

# behavioral_actions_ConditionalStatement class attributes and methods

# expressions_Conditional class attributes and methods

# behavioral_rules_Dummy class attributes and methods

# behavioral_events_Subscription class attributes and methods

# NamedElement class attributes and methods

# DimensionDefinition class attributes and methods

# behavioral_actions_NamedValueDeclaration class attributes and methods

# EventProducer class attributes and methods

# EventFilter class attributes and methods

# SapClass class attributes and methods

# behavioral_events_EventProducer class attributes and methods

# Subscription class attributes and methods

# MethodSignature class attributes and methods

# behavioral_events_EventFilter class attributes and methods

# behavioral_transactions_Dummy class attributes and methods

# SAMSchemaAction class attributes and methods

# behavioral_status_and_action_old_SAMStatusVariable class attributes and methods
behavioral_status_and_action_old_SAMStatusVariable_name: Property = Property(name="name", type=StringType)
behavioral_status_and_action_old_SAMStatusVariable_isAgentVariable: Property = Property(name="isAgentVariable", type=BooleanType)
behavioral_status_and_action_old_SAMStatusVariable.attributes={behavioral_status_and_action_old_SAMStatusVariable_name, behavioral_status_and_action_old_SAMStatusVariable_isAgentVariable}

# SAMStatusValue class attributes and methods

# SAMSchemaVariable class attributes and methods

# behavioral_status_and_action_old_SAMDerivator class attributes and methods
behavioral_status_and_action_old_SAMDerivator_kind: Property = Property(name="kind", type=StringType)
behavioral_status_and_action_old_SAMDerivator.attributes={behavioral_status_and_action_old_SAMDerivator_kind}

# SAMSchemaDerivator class attributes and methods

# behavioral_status_and_action_old_SAMStatusValue class attributes and methods
behavioral_status_and_action_old_SAMStatusValue_name: Property = Property(name="name", type=StringType)
behavioral_status_and_action_old_SAMStatusValue.attributes={behavioral_status_and_action_old_SAMStatusValue_name}

# SAMStatusVariable class attributes and methods

# behavioral_status_and_action_old_SAMStatusSchema class attributes and methods
behavioral_status_and_action_old_SAMStatusSchema_name: Property = Property(name="name", type=StringType)
behavioral_status_and_action_old_SAMStatusSchema.attributes={behavioral_status_and_action_old_SAMStatusSchema_name}

# SAMOperator class attributes and methods

# behavioral_status_and_action_old_SAMAction class attributes and methods
behavioral_status_and_action_old_SAMAction_name: Property = Property(name="name", type=StringType)
behavioral_status_and_action_old_SAMAction_isAgentAction: Property = Property(name="isAgentAction", type=BooleanType)
behavioral_status_and_action_old_SAMAction.attributes={behavioral_status_and_action_old_SAMAction_name, behavioral_status_and_action_old_SAMAction_isAgentAction}

# SAMSchemaValue class attributes and methods

# behavioral_status_and_action_old_SAMSchemaVariable class attributes and methods
behavioral_status_and_action_old_SAMSchemaVariable_hasStateGuard: Property = Property(name="hasStateGuard", type=BooleanType)
behavioral_status_and_action_old_SAMSchemaVariable.attributes={behavioral_status_and_action_old_SAMSchemaVariable_hasStateGuard}

# behavioral_status_and_action_old_SAMSchemaValue class attributes and methods
behavioral_status_and_action_old_SAMSchemaValue_isInitial: Property = Property(name="isInitial", type=BooleanType)
behavioral_status_and_action_old_SAMSchemaValue_isInhibiting: Property = Property(name="isInhibiting", type=BooleanType)
behavioral_status_and_action_old_SAMSchemaValue.attributes={behavioral_status_and_action_old_SAMSchemaValue_isInhibiting, behavioral_status_and_action_old_SAMSchemaValue_isInitial}

# behavioral_status_and_action_old_SAMOperator class attributes and methods
behavioral_status_and_action_old_SAMOperator_kind: Property = Property(name="kind", type=StringType)
behavioral_status_and_action_old_SAMOperator.attributes={behavioral_status_and_action_old_SAMOperator_kind}

# SAMStatusSchema class attributes and methods

# behavioral_status_and_action_old_SAMSchemaAction class attributes and methods

# SAMAction class attributes and methods

# behavioral_status_and_action_old_SAMSchemaDerivator class attributes and methods

# SAMDerivator class attributes and methods

# behavioral_design_BusinessObjectNode class attributes and methods

# design_StatusVariable class attributes and methods

# design_Action class attributes and methods

# behavioral_design_StatusVariable class attributes and methods

# AbstractStatusVariable class attributes and methods

# behavioral_design_StatusValue class attributes and methods

# AbstractStatusValue class attributes and methods

# behavioral_design_Action class attributes and methods

# AbstractAction class attributes and methods

# behavioral_design_AbstractStatusVariable class attributes and methods
behavioral_design_AbstractStatusVariable_isAgent: Property = Property(name="isAgent", type=BooleanType)
behavioral_design_AbstractStatusVariable_isStateGuarded: Property = Property(name="isStateGuarded", type=BooleanType)
behavioral_design_AbstractStatusVariable.attributes={behavioral_design_AbstractStatusVariable_isAgent, behavioral_design_AbstractStatusVariable_isStateGuarded}

# design_AbstractStatusValue class attributes and methods

# behavioral_design_AbstractStatusValue class attributes and methods
behavioral_design_AbstractStatusValue_isInitial: Property = Property(name="isInitial", type=BooleanType)
behavioral_design_AbstractStatusValue_isInhibiting: Property = Property(name="isInhibiting", type=BooleanType)
behavioral_design_AbstractStatusValue_isStateGuarded: Property = Property(name="isStateGuarded", type=BooleanType)
behavioral_design_AbstractStatusValue.attributes={behavioral_design_AbstractStatusValue_isInhibiting, behavioral_design_AbstractStatusValue_isInitial, behavioral_design_AbstractStatusValue_isStateGuarded}

# behavioral_design_AbstractAction class attributes and methods
behavioral_design_AbstractAction_isAgent: Property = Property(name="isAgent", type=BooleanType)
behavioral_design_AbstractAction_isPreconditionFixed: Property = Property(name="isPreconditionFixed", type=BooleanType)
behavioral_design_AbstractAction.attributes={behavioral_design_AbstractAction_isAgent, behavioral_design_AbstractAction_isPreconditionFixed}

# behavioral_assembly_StatusSchema class attributes and methods

# behavioral_design_BusinessObject class attributes and methods

# design_BusinessObjectNode class attributes and methods

# assembly_SchemaElement class attributes and methods

# behavioral_assembly_Connector class attributes and methods

# SchemaElement class attributes and methods

# assembly_ConnectableElement class attributes and methods

# behavioral_assembly_Operator class attributes and methods

# ConnectableElement class attributes and methods

# behavioral_assembly_ConnectableElement class attributes and methods

# behavioral_assembly_ActionProxy class attributes and methods

# design_AbstractAction class attributes and methods

# Signature class attributes and methods

# behavioral_assembly_StatusValueProxy class attributes and methods

# design_StatusValue class attributes and methods

# behavioral_assembly_Transition class attributes and methods

# Connector class attributes and methods

# behavioral_assembly_Synchroniser class attributes and methods

# behavioral_assembly_Precondition class attributes and methods

# behavioral_assembly_StatusVariableProxy class attributes and methods

# design_AbstractStatusVariable class attributes and methods

# behavioral_assembly_AndOperator class attributes and methods

# Operator class attributes and methods

# behavioral_assembly_OrOperator class attributes and methods

# behavioral_assembly_RequiredStrategy class attributes and methods

# Strategy class attributes and methods

# behavioral_assembly_NeutralStrategy class attributes and methods

# behavioral_assembly_EnablingStrategy class attributes and methods

# behavioral_assembly_InhibitingStrategy class attributes and methods

# behavioral_assembly_Strategy class attributes and methods

# behavioral_assembly_SchemaElement class attributes and methods

# assembly_Strategy class attributes and methods

# Relationships
assignTo0: BinaryAssociation = BinaryAssociation(
    name="assignTo0",
    ends={
        Property(name="Variable", type=behavioral_actions_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="assignments", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
statements2: BinaryAssociation = BinaryAssociation(
    name="statements2",
    ends={
        Property(name="Statement", type=behavioral_actions_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="block", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables3: BinaryAssociation = BinaryAssociation(
    name="variables3",
    ends={
        Property(name="NamedValue", type=behavioral_actions_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=NamedValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningStatement4: BinaryAssociation = BinaryAssociation(
    name="owningStatement4",
    ends={
        Property(name="StatementWithNestedBlocks", type=behavioral_actions_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedBlocks", type=StatementWithNestedBlocks, multiplicity=Multiplicity(0, 1))
    }
)
block1: BinaryAssociation = BinaryAssociation(
    name="block1",
    ends={
        Property(name="Block", type=behavioral_actions_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="statements", type=Block, multiplicity=Multiplicity(1, 1))
    }
)
collection5: BinaryAssociation = BinaryAssociation(
    name="collection5",
    ends={
        Property(name="Expression", type=behavioral_actions_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_actions_Foreach", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
forVariable6: BinaryAssociation = BinaryAssociation(
    name="forVariable6",
    ends={
        Property(name="Iterator", type=behavioral_actions_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="boundToFor", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression11: BinaryAssociation = BinaryAssociation(
    name="expression11",
    ends={
        Property(name="Expression12", type=behavioral_actions_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterate13: BinaryAssociation = BinaryAssociation(
    name="iterate13",
    ends={
        Property(name="Iterate", type=behavioral_actions_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="accumulator", type=collectionexpressions_Iterate, multiplicity=Multiplicity(0, 1))
    }
)
assignments14: BinaryAssociation = BinaryAssociation(
    name="assignments14",
    ends={
        Property(name="Assignment", type=behavioral_actions_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="assignTo", type=Assignment, multiplicity=Multiplicity(0, 9999))
    }
)
boundToFor15: BinaryAssociation = BinaryAssociation(
    name="boundToFor15",
    ends={
        Property(name="Foreach", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="forVariable", type=Foreach, multiplicity=Multiplicity(0, 1))
    }
)
iterate16: BinaryAssociation = BinaryAssociation(
    name="iterate16",
    ends={
        Property(name="Iterate17", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=collectionexpressions_Iterate, multiplicity=Multiplicity(0, 1))
    }
)
selection18: BinaryAssociation = BinaryAssociation(
    name="selection18",
    ends={
        Property(name="Selection", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterator", type=Selection, multiplicity=Multiplicity(0, 1))
    }
)
fromClause19: BinaryAssociation = BinaryAssociation(
    name="fromClause19",
    ends={
        Property(name="FromClause", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="alias", type=FromClause, multiplicity=Multiplicity(0, 1))
    }
)
factOfGroupBy20: BinaryAssociation = BinaryAssociation(
    name="factOfGroupBy20",
    ends={
        Property(name="GroupBy", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="fact", type=GroupBy, multiplicity=Multiplicity(0, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="Association", type=behavioral_actions_LinkManipulationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_actions_LinkManipulationStatement", type=Association, multiplicity=Multiplicity(1, 1))
    }
)
objects8: BinaryAssociation = BinaryAssociation(
    name="objects8",
    ends={
        Property(name="Expression10", type=behavioral_actions_LinkManipulationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_actions_LinkManipulationStatement9", type=Expression, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
nestedBlocks26: BinaryAssociation = BinaryAssociation(
    name="nestedBlocks26",
    ends={
        Property(name="Block27", type=behavioral_actions_StatementWithNestedBlocks, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStatement", type=Block, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
initExpression28: BinaryAssociation = BinaryAssociation(
    name="initExpression28",
    ends={
        Property(name="Expression29", type=behavioral_actions_NamedValueWithOptionalInitExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpressionFor", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedValueDeclaration30: BinaryAssociation = BinaryAssociation(
    name="namedValueDeclaration30",
    ends={
        Property(name="NamedValueDeclaration", type=behavioral_actions_NamedValueWithOptionalInitExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="namedValue", type=NamedValueDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
dimension21: BinaryAssociation = BinaryAssociation(
    name="dimension21",
    ends={
        Property(name="DimensionDefinition", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterator22", type=DimensionDefinition, multiplicity=Multiplicity(0, 1))
    }
)
groupedFactsOfGroupBy23: BinaryAssociation = BinaryAssociation(
    name="groupedFactsOfGroupBy23",
    ends={
        Property(name="GroupBy24", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="groupedFacts", type=GroupBy, multiplicity=Multiplicity(0, 1))
    }
)
namedValue25: BinaryAssociation = BinaryAssociation(
    name="namedValue25",
    ends={
        Property(name="NamedValueWithOptionalInitExpression", type=behavioral_actions_NamedValueDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="namedValueDeclaration", type=NamedValueWithOptionalInitExpression, multiplicity=Multiplicity(1, 1))
    }
)
producer31: BinaryAssociation = BinaryAssociation(
    name="producer31",
    ends={
        Property(name="EventProducer", type=behavioral_events_Subscription, multiplicity=Multiplicity(1, 1)),
        Property(name="subscriptions", type=EventProducer, multiplicity=Multiplicity(1, 1))
    }
)
filters32: BinaryAssociation = BinaryAssociation(
    name="filters32",
    ends={
        Property(name="EventFilter", type=behavioral_events_Subscription, multiplicity=Multiplicity(1, 1)),
        Property(name="subscription", type=EventFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subscribingClass33: BinaryAssociation = BinaryAssociation(
    name="subscribingClass33",
    ends={
        Property(name="SapClass", type=behavioral_events_Subscription, multiplicity=Multiplicity(1, 1)),
        Property(name="subscription34", type=SapClass, multiplicity=Multiplicity(1, 1))
    }
)
subscriptions35: BinaryAssociation = BinaryAssociation(
    name="subscriptions35",
    ends={
        Property(name="Subscription", type=behavioral_events_EventProducer, multiplicity=Multiplicity(1, 1)),
        Property(name="producer", type=Subscription, multiplicity=Multiplicity(0, 9999))
    }
)
notificationSignatures36: BinaryAssociation = BinaryAssociation(
    name="notificationSignatures36",
    ends={
        Property(name="MethodSignature", type=behavioral_events_EventProducer, multiplicity=Multiplicity(1, 1)),
        Property(name="producer37", type=MethodSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subscription38: BinaryAssociation = BinaryAssociation(
    name="subscription38",
    ends={
        Property(name="Subscription39", type=behavioral_events_EventFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="filters", type=Subscription, multiplicity=Multiplicity(1, 1))
    }
)
test40: BinaryAssociation = BinaryAssociation(
    name="test40",
    ends={
        Property(name="Block41", type=behavioral_events_EventFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_events_EventFilter", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
samSchemaActions44: BinaryAssociation = BinaryAssociation(
    name="samSchemaActions44",
    ends={
        Property(name="SAMSchemaAction", type=behavioral_status_and_action_old_SAMAction, multiplicity=Multiplicity(1, 1)),
        Property(name="samAction", type=SAMSchemaAction, multiplicity=Multiplicity(0, 9999))
    }
)
businessObjectNode45: BinaryAssociation = BinaryAssociation(
    name="businessObjectNode45",
    ends={
        Property(name="SapClass46", type=behavioral_status_and_action_old_SAMStatusVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="samStatusVariables", type=SapClass, multiplicity=Multiplicity(1, 1))
    }
)
samStatusValues47: BinaryAssociation = BinaryAssociation(
    name="samStatusValues47",
    ends={
        Property(name="SAMStatusValue", type=behavioral_status_and_action_old_SAMStatusVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="samStatusVariable", type=SAMStatusValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samSchemaVariables48: BinaryAssociation = BinaryAssociation(
    name="samSchemaVariables48",
    ends={
        Property(name="SAMSchemaVariable", type=behavioral_status_and_action_old_SAMStatusVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaValue", type=SAMSchemaVariable, multiplicity=Multiplicity(0, 9999))
    }
)
businessObject49: BinaryAssociation = BinaryAssociation(
    name="businessObject49",
    ends={
        Property(name="SapClass50", type=behavioral_status_and_action_old_SAMDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="samDerivators", type=SapClass, multiplicity=Multiplicity(1, 1))
    }
)
samSchemaDerivators51: BinaryAssociation = BinaryAssociation(
    name="samSchemaDerivators51",
    ends={
        Property(name="SAMSchemaDerivator", type=behavioral_status_and_action_old_SAMDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="samDerivator", type=SAMSchemaDerivator, multiplicity=Multiplicity(0, 9999))
    }
)
samStatusVariable52: BinaryAssociation = BinaryAssociation(
    name="samStatusVariable52",
    ends={
        Property(name="SAMStatusVariable", type=behavioral_status_and_action_old_SAMStatusValue, multiplicity=Multiplicity(1, 1)),
        Property(name="samStatusValues", type=SAMStatusVariable, multiplicity=Multiplicity(1, 1))
    }
)
businessObjectNode53: BinaryAssociation = BinaryAssociation(
    name="businessObjectNode53",
    ends={
        Property(name="SapClass54", type=behavioral_status_and_action_old_SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="samStatusSchema", type=SapClass, multiplicity=Multiplicity(1, 1))
    }
)
samOperators55: BinaryAssociation = BinaryAssociation(
    name="samOperators55",
    ends={
        Property(name="SAMOperator", type=behavioral_status_and_action_old_SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="samStatusSchema56", type=SAMOperator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samSchemaVariables57: BinaryAssociation = BinaryAssociation(
    name="samSchemaVariables57",
    ends={
        Property(name="SAMSchemaVariable59", type=behavioral_status_and_action_old_SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="samStatusSchema58", type=SAMSchemaVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessObjectNode42: BinaryAssociation = BinaryAssociation(
    name="businessObjectNode42",
    ends={
        Property(name="SapClass43", type=behavioral_status_and_action_old_SAMAction, multiplicity=Multiplicity(1, 1)),
        Property(name="samActions", type=SapClass, multiplicity=Multiplicity(1, 1))
    }
)
samStatusSchema66: BinaryAssociation = BinaryAssociation(
    name="samStatusSchema66",
    ends={
        Property(name="samOperators", type=SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMStatusSchema", type=behavioral_status_and_action_old_SAMOperator, multiplicity=Multiplicity(1, 1))
    }
)
samSchemaValues67: BinaryAssociation = BinaryAssociation(
    name="samSchemaValues67",
    ends={
        Property(name="SAMSchemaValue", type=behavioral_status_and_action_old_SAMOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="samOperators68", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999))
    }
)
samSourceOperators69: BinaryAssociation = BinaryAssociation(
    name="samSourceOperators69",
    ends={
        Property(name="SAMOperator70", type=behavioral_status_and_action_old_SAMOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="samTargetOperators", type=SAMOperator, multiplicity=Multiplicity(0, 9999))
    }
)
samTargetOperators71: BinaryAssociation = BinaryAssociation(
    name="samTargetOperators71",
    ends={
        Property(name="SAMOperator72", type=behavioral_status_and_action_old_SAMOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="samSourceOperators", type=SAMOperator, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaActions73: BinaryAssociation = BinaryAssociation(
    name="samSchemaActions73",
    ends={
        Property(name="SAMSchemaAction74", type=behavioral_status_and_action_old_SAMOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaOperators", type=SAMSchemaAction, multiplicity=Multiplicity(0, 9999))
    }
)
samStatusSchema75: BinaryAssociation = BinaryAssociation(
    name="samStatusSchema75",
    ends={
        Property(name="SAMStatusSchema76", type=behavioral_status_and_action_old_SAMSchemaVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaVariables", type=SAMStatusSchema, multiplicity=Multiplicity(1, 1))
    }
)
samSchemaValues77: BinaryAssociation = BinaryAssociation(
    name="samSchemaValues77",
    ends={
        Property(name="SAMSchemaValue78", type=behavioral_status_and_action_old_SAMSchemaVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaVariable", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samSchemaValue79: BinaryAssociation = BinaryAssociation(
    name="samSchemaValue79",
    ends={
        Property(name="SAMStatusVariable81", type=behavioral_status_and_action_old_SAMSchemaVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaVariables80", type=SAMStatusVariable, multiplicity=Multiplicity(1, 1))
    }
)
samTargetSchemaDerivators82: BinaryAssociation = BinaryAssociation(
    name="samTargetSchemaDerivators82",
    ends={
        Property(name="SAMSchemaDerivator83", type=behavioral_status_and_action_old_SAMSchemaVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="samSourceSchemaVariables", type=SAMSchemaDerivator, multiplicity=Multiplicity(0, 9999))
    }
)
samSourceSchemaDerivators84: BinaryAssociation = BinaryAssociation(
    name="samSourceSchemaDerivators84",
    ends={
        Property(name="SAMSchemaDerivator85", type=behavioral_status_and_action_old_SAMSchemaVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="samTargetSchemaVariable", type=SAMSchemaDerivator, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaVariable86: BinaryAssociation = BinaryAssociation(
    name="samSchemaVariable86",
    ends={
        Property(name="SAMSchemaVariable87", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaValues", type=SAMSchemaVariable, multiplicity=Multiplicity(1, 1))
    }
)
samSourceSchemaActions88: BinaryAssociation = BinaryAssociation(
    name="samSourceSchemaActions88",
    ends={
        Property(name="SAMSchemaAction89", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="samTargetSchemaValues", type=SAMSchemaAction, multiplicity=Multiplicity(0, 9999))
    }
)
samSourceSchemaValues90: BinaryAssociation = BinaryAssociation(
    name="samSourceSchemaValues90",
    ends={
        Property(name="SAMSchemaValue92", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="samTargetSchemaValues91", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaActions60: BinaryAssociation = BinaryAssociation(
    name="samSchemaActions60",
    ends={
        Property(name="SAMSchemaAction62", type=behavioral_status_and_action_old_SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="samStatusSchema61", type=SAMSchemaAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samTargetSchemaValues93: BinaryAssociation = BinaryAssociation(
    name="samTargetSchemaValues93",
    ends={
        Property(name="SAMSchemaValue94", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="samSourceSchemaValues", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaDerivators63: BinaryAssociation = BinaryAssociation(
    name="samSchemaDerivators63",
    ends={
        Property(name="SAMSchemaDerivator65", type=behavioral_status_and_action_old_SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="samStatusSchema64", type=SAMSchemaDerivator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samOperators95: BinaryAssociation = BinaryAssociation(
    name="samOperators95",
    ends={
        Property(name="SAMOperator97", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaValues96", type=SAMOperator, multiplicity=Multiplicity(0, 9999))
    }
)
samStatusSchema101: BinaryAssociation = BinaryAssociation(
    name="samStatusSchema101",
    ends={
        Property(name="SAMStatusSchema102", type=behavioral_status_and_action_old_SAMSchemaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaActions", type=SAMStatusSchema, multiplicity=Multiplicity(1, 1))
    }
)
samAction103: BinaryAssociation = BinaryAssociation(
    name="samAction103",
    ends={
        Property(name="SAMAction", type=behavioral_status_and_action_old_SAMSchemaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaActions104", type=SAMAction, multiplicity=Multiplicity(1, 1))
    }
)
samTargetSchemaValues105: BinaryAssociation = BinaryAssociation(
    name="samTargetSchemaValues105",
    ends={
        Property(name="SAMSchemaValue106", type=behavioral_status_and_action_old_SAMSchemaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="samSourceSchemaActions", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaValues107: BinaryAssociation = BinaryAssociation(
    name="samSchemaValues107",
    ends={
        Property(name="SAMSchemaValue109", type=behavioral_status_and_action_old_SAMSchemaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaActions108", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaOperators110: BinaryAssociation = BinaryAssociation(
    name="samSchemaOperators110",
    ends={
        Property(name="SAMOperator112", type=behavioral_status_and_action_old_SAMSchemaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaActions111", type=SAMOperator, multiplicity=Multiplicity(0, 9999))
    }
)
samDerivator113: BinaryAssociation = BinaryAssociation(
    name="samDerivator113",
    ends={
        Property(name="SAMDerivator", type=behavioral_status_and_action_old_SAMSchemaDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaDerivators", type=SAMDerivator, multiplicity=Multiplicity(1, 1))
    }
)
samStatusSchema114: BinaryAssociation = BinaryAssociation(
    name="samStatusSchema114",
    ends={
        Property(name="SAMStatusSchema116", type=behavioral_status_and_action_old_SAMSchemaDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaDerivators115", type=SAMStatusSchema, multiplicity=Multiplicity(1, 1))
    }
)
samSourceSchemaVariables117: BinaryAssociation = BinaryAssociation(
    name="samSourceSchemaVariables117",
    ends={
        Property(name="SAMSchemaVariable118", type=behavioral_status_and_action_old_SAMSchemaDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="samTargetSchemaDerivators", type=SAMSchemaVariable, multiplicity=Multiplicity(0, 9999))
    }
)
samTargetSchemaVariable119: BinaryAssociation = BinaryAssociation(
    name="samTargetSchemaVariable119",
    ends={
        Property(name="SAMSchemaVariable120", type=behavioral_status_and_action_old_SAMSchemaDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="samSourceSchemaDerivators", type=SAMSchemaVariable, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaActions98: BinaryAssociation = BinaryAssociation(
    name="samSchemaActions98",
    ends={
        Property(name="SAMSchemaAction100", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="samSchemaValues99", type=SAMSchemaAction, multiplicity=Multiplicity(0, 9999))
    }
)
variables122: BinaryAssociation = BinaryAssociation(
    name="variables122",
    ends={
        Property(name="design_StatusVariable", type=behavioral_design_BusinessObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_design_BusinessObjectNode", type=design_StatusVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions123: BinaryAssociation = BinaryAssociation(
    name="actions123",
    ends={
        Property(name="design_Action", type=behavioral_design_BusinessObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_design_BusinessObjectNode124", type=design_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values125: BinaryAssociation = BinaryAssociation(
    name="values125",
    ends={
        Property(name="design_AbstractStatusValue", type=behavioral_design_AbstractStatusVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_design_AbstractStatusVariable", type=design_AbstractStatusValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes121: BinaryAssociation = BinaryAssociation(
    name="nodes121",
    ends={
        Property(name="design_BusinessObjectNode", type=behavioral_design_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_design_BusinessObject", type=design_BusinessObjectNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements128: BinaryAssociation = BinaryAssociation(
    name="elements128",
    ends={
        Property(name="assembly_SchemaElement", type=behavioral_assembly_StatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_StatusSchema", type=assembly_SchemaElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source129: BinaryAssociation = BinaryAssociation(
    name="source129",
    ends={
        Property(name="assembly_ConnectableElement", type=behavioral_assembly_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_Connector", type=assembly_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
target130: BinaryAssociation = BinaryAssociation(
    name="target130",
    ends={
        Property(name="assembly_ConnectableElement132", type=behavioral_assembly_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_Connector131", type=assembly_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
action133: BinaryAssociation = BinaryAssociation(
    name="action133",
    ends={
        Property(name="Signature", type=behavioral_assembly_ActionProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_ActionProxy", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
value134: BinaryAssociation = BinaryAssociation(
    name="value134",
    ends={
        Property(name="design_StatusValue", type=behavioral_assembly_StatusValueProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_StatusValueProxy", type=design_StatusValue, multiplicity=Multiplicity(0, 1))
    }
)
node126: BinaryAssociation = BinaryAssociation(
    name="node126",
    ends={
        Property(name="SapClass127", type=behavioral_assembly_StatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralModel", type=SapClass, multiplicity=Multiplicity(0, 1))
    }
)
variable136: BinaryAssociation = BinaryAssociation(
    name="variable136",
    ends={
        Property(name="design_StatusVariable137", type=behavioral_assembly_StatusVariableProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_StatusVariableProxy", type=design_StatusVariable, multiplicity=Multiplicity(0, 1))
    }
)
strategy135: BinaryAssociation = BinaryAssociation(
    name="strategy135",
    ends={
        Property(name="assembly_Strategy", type=behavioral_assembly_Precondition, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_Precondition", type=assembly_Strategy, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_behavioral_actions_Assignment_StatementWithArgument = Generalization(general=StatementWithArgument, specific=behavioral_actions_Assignment)
gen_behavioral_actions_Statement_InScope = Generalization(general=InScope, specific=behavioral_actions_Statement)
gen_behavioral_actions_Block_classes_FunctionSignatureImplementation = Generalization(general=classes_FunctionSignatureImplementation, specific=behavioral_actions_Block)
gen_behavioral_actions_Block_classes_InScope = Generalization(general=classes_InScope, specific=behavioral_actions_Block)
gen_behavioral_actions_IfElse_actions_ConditionalStatement = Generalization(general=actions_ConditionalStatement, specific=behavioral_actions_IfElse)
gen_behavioral_actions_IfElse_actions_StatementWithNestedBlocks = Generalization(general=actions_StatementWithNestedBlocks, specific=behavioral_actions_IfElse)
gen_behavioral_actions_WhileLoop_actions_ConditionalStatement = Generalization(general=actions_ConditionalStatement, specific=behavioral_actions_WhileLoop)
gen_behavioral_actions_WhileLoop_actions_SingleBlockStatement = Generalization(general=actions_SingleBlockStatement, specific=behavioral_actions_WhileLoop)
gen_behavioral_actions_Foreach_SingleBlockStatement = Generalization(general=SingleBlockStatement, specific=behavioral_actions_Foreach)
gen_behavioral_actions_Return_StatementWithArgument = Generalization(general=StatementWithArgument, specific=behavioral_actions_Return)
gen_behavioral_actions_AddLink_LinkManipulationStatement = Generalization(general=LinkManipulationStatement, specific=behavioral_actions_AddLink)
gen_behavioral_actions_RemoveLink_LinkManipulationStatement = Generalization(general=LinkManipulationStatement, specific=behavioral_actions_RemoveLink)
gen_behavioral_actions_LinkManipulationStatement_Statement = Generalization(general=Statement, specific=behavioral_actions_LinkManipulationStatement)
gen_behavioral_actions_Constant_NamedValueWithOptionalInitExpression = Generalization(general=NamedValueWithOptionalInitExpression, specific=behavioral_actions_Constant)
gen_behavioral_actions_Variable_NamedValueWithOptionalInitExpression = Generalization(general=NamedValueWithOptionalInitExpression, specific=behavioral_actions_Variable)
gen_behavioral_actions_Iterator_NamedValue = Generalization(general=NamedValue, specific=behavioral_actions_Iterator)
gen_behavioral_actions_ExpressionStatement_Statement = Generalization(general=Statement, specific=behavioral_actions_ExpressionStatement)
gen_behavioral_actions_StatementWithNestedBlocks_Statement = Generalization(general=Statement, specific=behavioral_actions_StatementWithNestedBlocks)
gen_behavioral_actions_SingleBlockStatement_StatementWithNestedBlocks = Generalization(general=StatementWithNestedBlocks, specific=behavioral_actions_SingleBlockStatement)
gen_behavioral_actions_StatementWithArgument_actions_Statement = Generalization(general=actions_Statement, specific=behavioral_actions_StatementWithArgument)
gen_behavioral_actions_StatementWithArgument_expressions_WithArgument = Generalization(general=expressions_WithArgument, specific=behavioral_actions_StatementWithArgument)
gen_behavioral_actions_NamedValueWithOptionalInitExpression_NamedValue = Generalization(general=NamedValue, specific=behavioral_actions_NamedValueWithOptionalInitExpression)
gen_behavioral_actions_ConditionalStatement_expressions_Conditional = Generalization(general=expressions_Conditional, specific=behavioral_actions_ConditionalStatement)
gen_behavioral_actions_ConditionalStatement_actions_Statement = Generalization(general=actions_Statement, specific=behavioral_actions_ConditionalStatement)
gen_behavioral_actions_NamedValueDeclaration_Statement = Generalization(general=Statement, specific=behavioral_actions_NamedValueDeclaration)
gen_behavioral_events_Subscription_NamedElement = Generalization(general=NamedElement, specific=behavioral_events_Subscription)
gen_behavioral_design_BusinessObjectNode_NamedElement = Generalization(general=NamedElement, specific=behavioral_design_BusinessObjectNode)
gen_behavioral_design_StatusVariable_AbstractStatusVariable = Generalization(general=AbstractStatusVariable, specific=behavioral_design_StatusVariable)
gen_behavioral_design_StatusValue_AbstractStatusValue = Generalization(general=AbstractStatusValue, specific=behavioral_design_StatusValue)
gen_behavioral_design_Action_AbstractAction = Generalization(general=AbstractAction, specific=behavioral_design_Action)
gen_behavioral_design_AbstractStatusVariable_NamedElement = Generalization(general=NamedElement, specific=behavioral_design_AbstractStatusVariable)
gen_behavioral_design_AbstractStatusValue_NamedElement = Generalization(general=NamedElement, specific=behavioral_design_AbstractStatusValue)
gen_behavioral_design_AbstractAction_NamedElement = Generalization(general=NamedElement, specific=behavioral_design_AbstractAction)
gen_behavioral_assembly_StatusSchema_NamedElement = Generalization(general=NamedElement, specific=behavioral_assembly_StatusSchema)
gen_behavioral_assembly_Connector_SchemaElement = Generalization(general=SchemaElement, specific=behavioral_assembly_Connector)
gen_behavioral_assembly_Operator_ConnectableElement = Generalization(general=ConnectableElement, specific=behavioral_assembly_Operator)
gen_behavioral_assembly_ConnectableElement_SchemaElement = Generalization(general=SchemaElement, specific=behavioral_assembly_ConnectableElement)
gen_behavioral_assembly_ActionProxy_design_AbstractAction = Generalization(general=design_AbstractAction, specific=behavioral_assembly_ActionProxy)
gen_behavioral_assembly_ActionProxy_design_Action = Generalization(general=design_Action, specific=behavioral_assembly_ActionProxy)
gen_behavioral_assembly_ActionProxy_assembly_ConnectableElement = Generalization(general=assembly_ConnectableElement, specific=behavioral_assembly_ActionProxy)
gen_behavioral_assembly_StatusValueProxy_design_AbstractStatusValue = Generalization(general=design_AbstractStatusValue, specific=behavioral_assembly_StatusValueProxy)
gen_behavioral_assembly_StatusValueProxy_design_StatusValue = Generalization(general=design_StatusValue, specific=behavioral_assembly_StatusValueProxy)
gen_behavioral_assembly_StatusValueProxy_assembly_ConnectableElement = Generalization(general=assembly_ConnectableElement, specific=behavioral_assembly_StatusValueProxy)
gen_behavioral_assembly_Transition_Connector = Generalization(general=Connector, specific=behavioral_assembly_Transition)
gen_behavioral_assembly_Synchroniser_Connector = Generalization(general=Connector, specific=behavioral_assembly_Synchroniser)
gen_behavioral_assembly_Precondition_Connector = Generalization(general=Connector, specific=behavioral_assembly_Precondition)
gen_behavioral_assembly_StatusVariableProxy_design_AbstractStatusVariable = Generalization(general=design_AbstractStatusVariable, specific=behavioral_assembly_StatusVariableProxy)
gen_behavioral_assembly_StatusVariableProxy_design_StatusVariable = Generalization(general=design_StatusVariable, specific=behavioral_assembly_StatusVariableProxy)
gen_behavioral_assembly_StatusVariableProxy_assembly_ConnectableElement = Generalization(general=assembly_ConnectableElement, specific=behavioral_assembly_StatusVariableProxy)
gen_behavioral_assembly_AndOperator_Operator = Generalization(general=Operator, specific=behavioral_assembly_AndOperator)
gen_behavioral_assembly_OrOperator_Operator = Generalization(general=Operator, specific=behavioral_assembly_OrOperator)
gen_behavioral_assembly_RequiredStrategy_Strategy = Generalization(general=Strategy, specific=behavioral_assembly_RequiredStrategy)
gen_behavioral_assembly_NeutralStrategy_Strategy = Generalization(general=Strategy, specific=behavioral_assembly_NeutralStrategy)
gen_behavioral_assembly_EnablingStrategy_Strategy = Generalization(general=Strategy, specific=behavioral_assembly_EnablingStrategy)
gen_behavioral_assembly_InhibitingStrategy_Strategy = Generalization(general=Strategy, specific=behavioral_assembly_InhibitingStrategy)
gen_behavioral_assembly_SchemaElement_NamedElement = Generalization(general=NamedElement, specific=behavioral_assembly_SchemaElement)

# Domain Model
domain_model = DomainModel(
    name="behavioral",
    types={behavioral_bpdm_Dummy, behavioral_actions_Assignment, StatementWithArgument, Variable, behavioral_actions_Statement, InScope, behavioral_businesstasks_TaskAgent, behavioral_actions_Block, classes_FunctionSignatureImplementation, classes_InScope, Statement, NamedValue, StatementWithNestedBlocks, behavioral_actions_IfElse, actions_ConditionalStatement, actions_StatementWithNestedBlocks, Block, behavioral_actions_WhileLoop, actions_SingleBlockStatement, behavioral_actions_Foreach, SingleBlockStatement, Expression, Iterator, behavioral_actions_Return, behavioral_actions_AddLink, LinkManipulationStatement, behavioral_actions_RemoveLink, behavioral_actions_LinkManipulationStatement, behavioral_actions_Sort, behavioral_actions_QueryInvocation, behavioral_actions_Constant, NamedValueWithOptionalInitExpression, collectionexpressions_Iterate, behavioral_actions_Variable, Assignment, behavioral_actions_Iterator, Foreach, Selection, FromClause, GroupBy, Association, behavioral_actions_ExpressionStatement, behavioral_actions_StatementWithNestedBlocks, behavioral_actions_SingleBlockStatement, behavioral_actions_StatementWithArgument, actions_Statement, expressions_WithArgument, behavioral_actions_NamedValueWithOptionalInitExpression, NamedValueDeclaration, behavioral_actions_ConditionalStatement, expressions_Conditional, behavioral_rules_Dummy, behavioral_events_Subscription, NamedElement, DimensionDefinition, behavioral_actions_NamedValueDeclaration, EventProducer, EventFilter, SapClass, behavioral_events_EventProducer, Subscription, MethodSignature, behavioral_events_EventFilter, behavioral_transactions_Dummy, SAMSchemaAction, behavioral_status_and_action_old_SAMStatusVariable, SAMStatusValue, SAMSchemaVariable, behavioral_status_and_action_old_SAMDerivator, SAMSchemaDerivator, behavioral_status_and_action_old_SAMStatusValue, SAMStatusVariable, behavioral_status_and_action_old_SAMStatusSchema, SAMOperator, behavioral_status_and_action_old_SAMAction, SAMSchemaValue, behavioral_status_and_action_old_SAMSchemaVariable, behavioral_status_and_action_old_SAMSchemaValue, behavioral_status_and_action_old_SAMOperator, SAMStatusSchema, behavioral_status_and_action_old_SAMSchemaAction, SAMAction, behavioral_status_and_action_old_SAMSchemaDerivator, SAMDerivator, behavioral_design_BusinessObjectNode, design_StatusVariable, design_Action, behavioral_design_StatusVariable, AbstractStatusVariable, behavioral_design_StatusValue, AbstractStatusValue, behavioral_design_Action, AbstractAction, behavioral_design_AbstractStatusVariable, design_AbstractStatusValue, behavioral_design_AbstractStatusValue, behavioral_design_AbstractAction, behavioral_assembly_StatusSchema, behavioral_design_BusinessObject, design_BusinessObjectNode, assembly_SchemaElement, behavioral_assembly_Connector, SchemaElement, assembly_ConnectableElement, behavioral_assembly_Operator, ConnectableElement, behavioral_assembly_ConnectableElement, behavioral_assembly_ActionProxy, design_AbstractAction, Signature, behavioral_assembly_StatusValueProxy, design_StatusValue, behavioral_assembly_Transition, Connector, behavioral_assembly_Synchroniser, behavioral_assembly_Precondition, behavioral_assembly_StatusVariableProxy, design_AbstractStatusVariable, behavioral_assembly_AndOperator, Operator, behavioral_assembly_OrOperator, behavioral_assembly_RequiredStrategy, Strategy, behavioral_assembly_NeutralStrategy, behavioral_assembly_EnablingStrategy, behavioral_assembly_InhibitingStrategy, behavioral_assembly_Strategy, behavioral_assembly_SchemaElement, assembly_Strategy, SAMOperatorKindEnum, SAMDerivatorKindEnum, PreconditionKindEnum},
    associations={assignTo0, statements2, variables3, owningStatement4, block1, collection5, forVariable6, expression11, iterate13, assignments14, boundToFor15, iterate16, selection18, fromClause19, factOfGroupBy20, association7, objects8, nestedBlocks26, initExpression28, namedValueDeclaration30, dimension21, groupedFactsOfGroupBy23, namedValue25, producer31, filters32, subscribingClass33, subscriptions35, notificationSignatures36, subscription38, test40, samSchemaActions44, businessObjectNode45, samStatusValues47, samSchemaVariables48, businessObject49, samSchemaDerivators51, samStatusVariable52, businessObjectNode53, samOperators55, samSchemaVariables57, businessObjectNode42, samStatusSchema66, samSchemaValues67, samSourceOperators69, samTargetOperators71, samSchemaActions73, samStatusSchema75, samSchemaValues77, samSchemaValue79, samTargetSchemaDerivators82, samSourceSchemaDerivators84, samSchemaVariable86, samSourceSchemaActions88, samSourceSchemaValues90, samSchemaActions60, samTargetSchemaValues93, samSchemaDerivators63, samOperators95, samStatusSchema101, samAction103, samTargetSchemaValues105, samSchemaValues107, samSchemaOperators110, samDerivator113, samStatusSchema114, samSourceSchemaVariables117, samTargetSchemaVariable119, samSchemaActions98, variables122, actions123, values125, nodes121, elements128, source129, target130, action133, value134, node126, variable136, strategy135},
    generalizations={gen_behavioral_actions_Assignment_StatementWithArgument, gen_behavioral_actions_Statement_InScope, gen_behavioral_actions_Block_classes_FunctionSignatureImplementation, gen_behavioral_actions_Block_classes_InScope, gen_behavioral_actions_IfElse_actions_ConditionalStatement, gen_behavioral_actions_IfElse_actions_StatementWithNestedBlocks, gen_behavioral_actions_WhileLoop_actions_ConditionalStatement, gen_behavioral_actions_WhileLoop_actions_SingleBlockStatement, gen_behavioral_actions_Foreach_SingleBlockStatement, gen_behavioral_actions_Return_StatementWithArgument, gen_behavioral_actions_AddLink_LinkManipulationStatement, gen_behavioral_actions_RemoveLink_LinkManipulationStatement, gen_behavioral_actions_LinkManipulationStatement_Statement, gen_behavioral_actions_Constant_NamedValueWithOptionalInitExpression, gen_behavioral_actions_Variable_NamedValueWithOptionalInitExpression, gen_behavioral_actions_Iterator_NamedValue, gen_behavioral_actions_ExpressionStatement_Statement, gen_behavioral_actions_StatementWithNestedBlocks_Statement, gen_behavioral_actions_SingleBlockStatement_StatementWithNestedBlocks, gen_behavioral_actions_StatementWithArgument_actions_Statement, gen_behavioral_actions_StatementWithArgument_expressions_WithArgument, gen_behavioral_actions_NamedValueWithOptionalInitExpression_NamedValue, gen_behavioral_actions_ConditionalStatement_expressions_Conditional, gen_behavioral_actions_ConditionalStatement_actions_Statement, gen_behavioral_actions_NamedValueDeclaration_Statement, gen_behavioral_events_Subscription_NamedElement, gen_behavioral_design_BusinessObjectNode_NamedElement, gen_behavioral_design_StatusVariable_AbstractStatusVariable, gen_behavioral_design_StatusValue_AbstractStatusValue, gen_behavioral_design_Action_AbstractAction, gen_behavioral_design_AbstractStatusVariable_NamedElement, gen_behavioral_design_AbstractStatusValue_NamedElement, gen_behavioral_design_AbstractAction_NamedElement, gen_behavioral_assembly_StatusSchema_NamedElement, gen_behavioral_assembly_Connector_SchemaElement, gen_behavioral_assembly_Operator_ConnectableElement, gen_behavioral_assembly_ConnectableElement_SchemaElement, gen_behavioral_assembly_ActionProxy_design_AbstractAction, gen_behavioral_assembly_ActionProxy_design_Action, gen_behavioral_assembly_ActionProxy_assembly_ConnectableElement, gen_behavioral_assembly_StatusValueProxy_design_AbstractStatusValue, gen_behavioral_assembly_StatusValueProxy_design_StatusValue, gen_behavioral_assembly_StatusValueProxy_assembly_ConnectableElement, gen_behavioral_assembly_Transition_Connector, gen_behavioral_assembly_Synchroniser_Connector, gen_behavioral_assembly_Precondition_Connector, gen_behavioral_assembly_StatusVariableProxy_design_AbstractStatusVariable, gen_behavioral_assembly_StatusVariableProxy_design_StatusVariable, gen_behavioral_assembly_StatusVariableProxy_assembly_ConnectableElement, gen_behavioral_assembly_AndOperator_Operator, gen_behavioral_assembly_OrOperator_Operator, gen_behavioral_assembly_RequiredStrategy_Strategy, gen_behavioral_assembly_NeutralStrategy_Strategy, gen_behavioral_assembly_EnablingStrategy_Strategy, gen_behavioral_assembly_InhibitingStrategy_Strategy, gen_behavioral_assembly_SchemaElement_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)