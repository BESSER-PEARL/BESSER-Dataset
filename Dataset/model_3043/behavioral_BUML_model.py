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
behavioral_bpdm_Dummy = Class(name="behavioral::bpdm::Dummy")
behavioral_businesstasks_TaskAgent = Class(name="behavioral::businesstasks::TaskAgent")
behavioral_actions_Assignment = Class(name="behavioral::actions::Assignment")
StatementWithArgument = Class(name="StatementWithArgument")
Variable = Class(name="Variable")
behavioral_actions_Statement = Class(name="behavioral::actions::Statement", is_abstract=True)
InScope = Class(name="InScope")
Block = Class(name="Block")
behavioral_actions_Block = Class(name="behavioral::actions::Block")
classes_FunctionSignatureImplementation = Class(name="classes::FunctionSignatureImplementation")
classes_InScope = Class(name="classes::InScope")
Statement = Class(name="Statement")
NamedValue = Class(name="NamedValue")
StatementWithNestedBlocks = Class(name="StatementWithNestedBlocks")
behavioral_actions_IfElse = Class(name="behavioral::actions::IfElse")
actions_ConditionalStatement = Class(name="actions::ConditionalStatement")
actions_StatementWithNestedBlocks = Class(name="actions::StatementWithNestedBlocks")
behavioral_actions_Foreach = Class(name="behavioral::actions::Foreach")
SingleBlockStatement = Class(name="SingleBlockStatement")
Expression = Class(name="Expression")
Iterator = Class(name="Iterator")
behavioral_actions_Return = Class(name="behavioral::actions::Return")
behavioral_actions_AddLink = Class(name="behavioral::actions::AddLink")
LinkManipulationStatement = Class(name="LinkManipulationStatement")
behavioral_actions_RemoveLink = Class(name="behavioral::actions::RemoveLink")
behavioral_actions_LinkManipulationStatement = Class(name="behavioral::actions::LinkManipulationStatement", is_abstract=True)
Association = Class(name="Association")
behavioral_actions_ExpressionStatement = Class(name="behavioral::actions::ExpressionStatement")
behavioral_actions_Sort = Class(name="behavioral::actions::Sort")
behavioral_actions_QueryInvocation = Class(name="behavioral::actions::QueryInvocation")
behavioral_actions_WhileLoop = Class(name="behavioral::actions::WhileLoop")
actions_SingleBlockStatement = Class(name="actions::SingleBlockStatement")
collectionexpressions_Iterate = Class(name="collectionexpressions::Iterate")
behavioral_actions_Variable = Class(name="behavioral::actions::Variable")
Assignment = Class(name="Assignment")
behavioral_actions_Iterator = Class(name="behavioral::actions::Iterator")
Foreach = Class(name="Foreach")
Selection = Class(name="Selection")
FromClause = Class(name="FromClause")
GroupBy = Class(name="GroupBy")
DimensionDefinition = Class(name="DimensionDefinition")
behavioral_actions_Constant = Class(name="behavioral::actions::Constant")
NamedValueWithOptionalInitExpression = Class(name="NamedValueWithOptionalInitExpression")
behavioral_actions_NamedValueDeclaration = Class(name="behavioral::actions::NamedValueDeclaration")
behavioral_actions_StatementWithNestedBlocks = Class(name="behavioral::actions::StatementWithNestedBlocks")
behavioral_actions_SingleBlockStatement = Class(name="behavioral::actions::SingleBlockStatement")
behavioral_actions_StatementWithArgument = Class(name="behavioral::actions::StatementWithArgument", is_abstract=True)
actions_Statement = Class(name="actions::Statement")
expressions_WithArgument = Class(name="expressions::WithArgument")
behavioral_actions_NamedValueWithOptionalInitExpression = Class(name="behavioral::actions::NamedValueWithOptionalInitExpression", is_abstract=True)
NamedValueDeclaration = Class(name="NamedValueDeclaration")
behavioral_actions_ConditionalStatement = Class(name="behavioral::actions::ConditionalStatement", is_abstract=True)
expressions_Conditional = Class(name="expressions::Conditional")
behavioral_rules_Dummy = Class(name="behavioral::rules::Dummy")
behavioral_events_Subscription = Class(name="behavioral::events::Subscription")
NamedElement = Class(name="NamedElement")
EventProducer = Class(name="EventProducer")
EventFilter = Class(name="EventFilter")
SapClass = Class(name="SapClass")
behavioral_events_EventProducer = Class(name="behavioral::events::EventProducer", is_abstract=True)
Subscription = Class(name="Subscription")
behavioral_transactions_Dummy = Class(name="behavioral::transactions::Dummy")
behavioral_status_and_action_old_SAMAction = Class(name="behavioral::status::and::action::old::SAMAction")
SAMSchemaAction = Class(name="SAMSchemaAction")
behavioral_status_and_action_old_SAMStatusVariable = Class(name="behavioral::status::and::action::old::SAMStatusVariable")
SAMStatusValue = Class(name="SAMStatusValue")
SAMSchemaVariable = Class(name="SAMSchemaVariable")
behavioral_status_and_action_old_SAMDerivator = Class(name="behavioral::status::and::action::old::SAMDerivator")
SAMSchemaDerivator = Class(name="SAMSchemaDerivator")
behavioral_status_and_action_old_SAMStatusValue = Class(name="behavioral::status::and::action::old::SAMStatusValue")
MethodSignature = Class(name="MethodSignature")
behavioral_events_EventFilter = Class(name="behavioral::events::EventFilter")
behavioral_status_and_action_old_SAMStatusSchema = Class(name="behavioral::status::and::action::old::SAMStatusSchema")
SAMOperator = Class(name="SAMOperator")
behavioral_status_and_action_old_SAMOperator = Class(name="behavioral::status::and::action::old::SAMOperator")
SAMStatusSchema = Class(name="SAMStatusSchema")
SAMSchemaValue = Class(name="SAMSchemaValue")
behavioral_status_and_action_old_SAMSchemaVariable = Class(name="behavioral::status::and::action::old::SAMSchemaVariable")
behavioral_status_and_action_old_SAMSchemaValue = Class(name="behavioral::status::and::action::old::SAMSchemaValue")
SAMStatusVariable = Class(name="SAMStatusVariable")
behavioral_status_and_action_old_SAMSchemaAction = Class(name="behavioral::status::and::action::old::SAMSchemaAction")
SAMAction = Class(name="SAMAction")
behavioral_status_and_action_old_SAMSchemaDerivator = Class(name="behavioral::status::and::action::old::SAMSchemaDerivator")
SAMDerivator = Class(name="SAMDerivator")
behavioral_design_BusinessObject = Class(name="behavioral::design::BusinessObject")
design_BusinessObjectNode = Class(name="design::BusinessObjectNode")
behavioral_design_BusinessObjectNode = Class(name="behavioral::design::BusinessObjectNode")
design_StatusVariable = Class(name="design::StatusVariable")
design_Action = Class(name="design::Action")
behavioral_design_StatusVariable = Class(name="behavioral::design::StatusVariable")
AbstractStatusVariable = Class(name="AbstractStatusVariable")
behavioral_design_StatusValue = Class(name="behavioral::design::StatusValue")
AbstractStatusValue = Class(name="AbstractStatusValue")
behavioral_design_Action = Class(name="behavioral::design::Action")
AbstractAction = Class(name="AbstractAction")
behavioral_design_AbstractStatusVariable = Class(name="behavioral::design::AbstractStatusVariable", is_abstract=True)
design_AbstractStatusValue = Class(name="design::AbstractStatusValue")
behavioral_design_AbstractStatusValue = Class(name="behavioral::design::AbstractStatusValue", is_abstract=True)
behavioral_design_AbstractAction = Class(name="behavioral::design::AbstractAction", is_abstract=True)
behavioral_assembly_StatusSchema = Class(name="behavioral::assembly::StatusSchema")
assembly_SchemaElement = Class(name="assembly::SchemaElement")
behavioral_assembly_Connector = Class(name="behavioral::assembly::Connector", is_abstract=True)
SchemaElement = Class(name="SchemaElement")
assembly_ConnectableElement = Class(name="assembly::ConnectableElement")
behavioral_assembly_Operator = Class(name="behavioral::assembly::Operator")
ConnectableElement = Class(name="ConnectableElement")
behavioral_assembly_ConnectableElement = Class(name="behavioral::assembly::ConnectableElement", is_abstract=True)
behavioral_assembly_ActionProxy = Class(name="behavioral::assembly::ActionProxy")
design_AbstractAction = Class(name="design::AbstractAction")
Signature = Class(name="Signature")
behavioral_assembly_StatusValueProxy = Class(name="behavioral::assembly::StatusValueProxy")
design_StatusValue = Class(name="design::StatusValue")
behavioral_assembly_Transition = Class(name="behavioral::assembly::Transition")
Connector = Class(name="Connector")
behavioral_assembly_Synchroniser = Class(name="behavioral::assembly::Synchroniser")
behavioral_assembly_Precondition = Class(name="behavioral::assembly::Precondition")
assembly_Strategy = Class(name="assembly::Strategy")
behavioral_assembly_StatusVariableProxy = Class(name="behavioral::assembly::StatusVariableProxy")
design_AbstractStatusVariable = Class(name="design::AbstractStatusVariable")
behavioral_assembly_EnablingStrategy = Class(name="behavioral::assembly::EnablingStrategy")
behavioral_assembly_InhibitingStrategy = Class(name="behavioral::assembly::InhibitingStrategy")
behavioral_assembly_Strategy = Class(name="behavioral::assembly::Strategy", is_abstract=True)
behavioral_assembly_SchemaElement = Class(name="behavioral::assembly::SchemaElement", is_abstract=True)
behavioral_assembly_AndOperator = Class(name="behavioral::assembly::AndOperator")
Operator = Class(name="Operator")
behavioral_assembly_OrOperator = Class(name="behavioral::assembly::OrOperator")
behavioral_assembly_RequiredStrategy = Class(name="behavioral::assembly::RequiredStrategy")
Strategy = Class(name="Strategy")
behavioral_assembly_NeutralStrategy = Class(name="behavioral::assembly::NeutralStrategy")

# behavioral_bpdm_Dummy class attributes and methods

# behavioral_businesstasks_TaskAgent class attributes and methods

# behavioral_actions_Assignment class attributes and methods

# StatementWithArgument class attributes and methods

# Variable class attributes and methods

# behavioral_actions_Statement class attributes and methods
behavioral_actions_Statement_m_getOutermostBlock: Method = Method(name="getOutermostBlock", parameters={}, type=StringType)
behavioral_actions_Statement_m_isSideEffectFree: Method = Method(name="isSideEffectFree", parameters={}, type=BooleanType)
behavioral_actions_Statement_m_isSideEffectFreeForBlock: Method = Method(name="isSideEffectFreeForBlock", parameters={Parameter(name='block')}, type=BooleanType)
behavioral_actions_Statement_m_getNamedValuesInScope: Method = Method(name="getNamedValuesInScope", parameters={}, type=StringType)
behavioral_actions_Statement_m_getOwningClass: Method = Method(name="getOwningClass", parameters={}, type=StringType)
behavioral_actions_Statement.methods={behavioral_actions_Statement_m_getOwningClass, behavioral_actions_Statement_m_getOutermostBlock, behavioral_actions_Statement_m_getNamedValuesInScope, behavioral_actions_Statement_m_isSideEffectFree, behavioral_actions_Statement_m_isSideEffectFreeForBlock}

# InScope class attributes and methods

# Block class attributes and methods

# behavioral_actions_Block class attributes and methods
behavioral_actions_Block_m_getOutermostBlock: Method = Method(name="getOutermostBlock", parameters={}, type=StringType)
behavioral_actions_Block_m_localIsSideEffectFree: Method = Method(name="localIsSideEffectFree", parameters={}, type=BooleanType)
behavioral_actions_Block_m_getNamedValuesInScope: Method = Method(name="getNamedValuesInScope", parameters={}, type=StringType)
behavioral_actions_Block_m_getOwningClass: Method = Method(name="getOwningClass", parameters={}, type=StringType)
behavioral_actions_Block.methods={behavioral_actions_Block_m_getOutermostBlock, behavioral_actions_Block_m_getNamedValuesInScope, behavioral_actions_Block_m_localIsSideEffectFree, behavioral_actions_Block_m_getOwningClass}

# classes_FunctionSignatureImplementation class attributes and methods

# classes_InScope class attributes and methods

# Statement class attributes and methods

# NamedValue class attributes and methods

# StatementWithNestedBlocks class attributes and methods

# behavioral_actions_IfElse class attributes and methods
behavioral_actions_IfElse_m_getIfBlock: Method = Method(name="getIfBlock", parameters={}, type=StringType)
behavioral_actions_IfElse_m_getElseBlock: Method = Method(name="getElseBlock", parameters={}, type=StringType)
behavioral_actions_IfElse.methods={behavioral_actions_IfElse_m_getIfBlock, behavioral_actions_IfElse_m_getElseBlock}

# actions_ConditionalStatement class attributes and methods

# actions_StatementWithNestedBlocks class attributes and methods

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

# Association class attributes and methods

# behavioral_actions_ExpressionStatement class attributes and methods

# behavioral_actions_Sort class attributes and methods

# behavioral_actions_QueryInvocation class attributes and methods

# behavioral_actions_WhileLoop class attributes and methods
behavioral_actions_WhileLoop_m_getLoopBody: Method = Method(name="getLoopBody", parameters={}, type=StringType)
behavioral_actions_WhileLoop.methods={behavioral_actions_WhileLoop_m_getLoopBody}

# actions_SingleBlockStatement class attributes and methods

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

# DimensionDefinition class attributes and methods

# behavioral_actions_Constant class attributes and methods

# NamedValueWithOptionalInitExpression class attributes and methods

# behavioral_actions_NamedValueDeclaration class attributes and methods

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

# EventProducer class attributes and methods

# EventFilter class attributes and methods

# SapClass class attributes and methods

# behavioral_events_EventProducer class attributes and methods

# Subscription class attributes and methods

# behavioral_transactions_Dummy class attributes and methods

# behavioral_status_and_action_old_SAMAction class attributes and methods
behavioral_status_and_action_old_SAMAction_name: Property = Property(name="name", type=StringType)
behavioral_status_and_action_old_SAMAction_isAgentAction: Property = Property(name="isAgentAction", type=BooleanType)
behavioral_status_and_action_old_SAMAction.attributes={behavioral_status_and_action_old_SAMAction_name, behavioral_status_and_action_old_SAMAction_isAgentAction}

# SAMSchemaAction class attributes and methods

# behavioral_status_and_action_old_SAMStatusVariable class attributes and methods
behavioral_status_and_action_old_SAMStatusVariable_name: Property = Property(name="name", type=StringType)
behavioral_status_and_action_old_SAMStatusVariable_isAgentVariable: Property = Property(name="isAgentVariable", type=BooleanType)
behavioral_status_and_action_old_SAMStatusVariable.attributes={behavioral_status_and_action_old_SAMStatusVariable_isAgentVariable, behavioral_status_and_action_old_SAMStatusVariable_name}

# SAMStatusValue class attributes and methods

# SAMSchemaVariable class attributes and methods

# behavioral_status_and_action_old_SAMDerivator class attributes and methods
behavioral_status_and_action_old_SAMDerivator_kind: Property = Property(name="kind", type=StringType)
behavioral_status_and_action_old_SAMDerivator.attributes={behavioral_status_and_action_old_SAMDerivator_kind}

# SAMSchemaDerivator class attributes and methods

# behavioral_status_and_action_old_SAMStatusValue class attributes and methods
behavioral_status_and_action_old_SAMStatusValue_name: Property = Property(name="name", type=StringType)
behavioral_status_and_action_old_SAMStatusValue.attributes={behavioral_status_and_action_old_SAMStatusValue_name}

# MethodSignature class attributes and methods

# behavioral_events_EventFilter class attributes and methods

# behavioral_status_and_action_old_SAMStatusSchema class attributes and methods
behavioral_status_and_action_old_SAMStatusSchema_name: Property = Property(name="name", type=StringType)
behavioral_status_and_action_old_SAMStatusSchema.attributes={behavioral_status_and_action_old_SAMStatusSchema_name}

# SAMOperator class attributes and methods

# behavioral_status_and_action_old_SAMOperator class attributes and methods
behavioral_status_and_action_old_SAMOperator_kind: Property = Property(name="kind", type=StringType)
behavioral_status_and_action_old_SAMOperator.attributes={behavioral_status_and_action_old_SAMOperator_kind}

# SAMStatusSchema class attributes and methods

# SAMSchemaValue class attributes and methods

# behavioral_status_and_action_old_SAMSchemaVariable class attributes and methods
behavioral_status_and_action_old_SAMSchemaVariable_hasStateGuard: Property = Property(name="hasStateGuard", type=BooleanType)
behavioral_status_and_action_old_SAMSchemaVariable.attributes={behavioral_status_and_action_old_SAMSchemaVariable_hasStateGuard}

# behavioral_status_and_action_old_SAMSchemaValue class attributes and methods
behavioral_status_and_action_old_SAMSchemaValue_isInitial: Property = Property(name="isInitial", type=BooleanType)
behavioral_status_and_action_old_SAMSchemaValue_isInhibiting: Property = Property(name="isInhibiting", type=BooleanType)
behavioral_status_and_action_old_SAMSchemaValue.attributes={behavioral_status_and_action_old_SAMSchemaValue_isInhibiting, behavioral_status_and_action_old_SAMSchemaValue_isInitial}

# SAMStatusVariable class attributes and methods

# behavioral_status_and_action_old_SAMSchemaAction class attributes and methods

# SAMAction class attributes and methods

# behavioral_status_and_action_old_SAMSchemaDerivator class attributes and methods

# SAMDerivator class attributes and methods

# behavioral_design_BusinessObject class attributes and methods

# design_BusinessObjectNode class attributes and methods

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

# assembly_Strategy class attributes and methods

# behavioral_assembly_StatusVariableProxy class attributes and methods

# design_AbstractStatusVariable class attributes and methods

# behavioral_assembly_EnablingStrategy class attributes and methods

# behavioral_assembly_InhibitingStrategy class attributes and methods

# behavioral_assembly_Strategy class attributes and methods

# behavioral_assembly_SchemaElement class attributes and methods

# behavioral_assembly_AndOperator class attributes and methods

# Operator class attributes and methods

# behavioral_assembly_OrOperator class attributes and methods

# behavioral_assembly_RequiredStrategy class attributes and methods

# Strategy class attributes and methods

# behavioral_assembly_NeutralStrategy class attributes and methods

# Relationships
assignTo0: BinaryAssociation = BinaryAssociation(
    name="assignTo0",
    ends={
        Property(name="actions", type=behavioral_actions_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
block1: BinaryAssociation = BinaryAssociation(
    name="block1",
    ends={
        Property(name="actions2", type=behavioral_actions_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="Block", type=Block, multiplicity=Multiplicity(1, 1))
    }
)
statements3: BinaryAssociation = BinaryAssociation(
    name="statements3",
    ends={
        Property(name="actions4", type=behavioral_actions_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="data.ecoreclasses", type=behavioral_actions_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedValue", type=NamedValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningStatement6: BinaryAssociation = BinaryAssociation(
    name="owningStatement6",
    ends={
        Property(name="actions7", type=behavioral_actions_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="StatementWithNestedBlocks", type=StatementWithNestedBlocks, multiplicity=Multiplicity(0, 1))
    }
)
collection8: BinaryAssociation = BinaryAssociation(
    name="collection8",
    ends={
        Property(name="Expression", type=behavioral_actions_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_actions_Foreach", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
forVariable9: BinaryAssociation = BinaryAssociation(
    name="forVariable9",
    ends={
        Property(name="actions10", type=behavioral_actions_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="Iterator", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
association11: BinaryAssociation = BinaryAssociation(
    name="association11",
    ends={
        Property(name="Association", type=behavioral_actions_LinkManipulationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_actions_LinkManipulationStatement", type=Association, multiplicity=Multiplicity(1, 1))
    }
)
objects12: BinaryAssociation = BinaryAssociation(
    name="objects12",
    ends={
        Property(name="Expression14", type=behavioral_actions_LinkManipulationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_actions_LinkManipulationStatement13", type=Expression, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
expression15: BinaryAssociation = BinaryAssociation(
    name="expression15",
    ends={
        Property(name="dataaccess.ecoreexpressions", type=behavioral_actions_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Expression16", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterate17: BinaryAssociation = BinaryAssociation(
    name="iterate17",
    ends={
        Property(name="dataaccess.ecoreexpressions18", type=behavioral_actions_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionexpressions", type=collectionexpressions_Iterate, multiplicity=Multiplicity(0, 1))
    }
)
assignments19: BinaryAssociation = BinaryAssociation(
    name="assignments19",
    ends={
        Property(name="actions20", type=behavioral_actions_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="Assignment", type=Assignment, multiplicity=Multiplicity(0, 9999))
    }
)
boundToFor21: BinaryAssociation = BinaryAssociation(
    name="boundToFor21",
    ends={
        Property(name="actions22", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="Foreach", type=Foreach, multiplicity=Multiplicity(0, 1))
    }
)
iterate23: BinaryAssociation = BinaryAssociation(
    name="iterate23",
    ends={
        Property(name="dataaccess.ecoreexpressions25", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionexpressions24", type=collectionexpressions_Iterate, multiplicity=Multiplicity(0, 1))
    }
)
selection26: BinaryAssociation = BinaryAssociation(
    name="selection26",
    ends={
        Property(name="dataaccess.ecorequery", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="Selection", type=Selection, multiplicity=Multiplicity(0, 1))
    }
)
fromClause27: BinaryAssociation = BinaryAssociation(
    name="fromClause27",
    ends={
        Property(name="dataaccess.ecorequery28", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="FromClause", type=FromClause, multiplicity=Multiplicity(0, 1))
    }
)
factOfGroupBy29: BinaryAssociation = BinaryAssociation(
    name="factOfGroupBy29",
    ends={
        Property(name="dataaccess.ecoreanalytics", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="GroupBy", type=GroupBy, multiplicity=Multiplicity(0, 1))
    }
)
dimension30: BinaryAssociation = BinaryAssociation(
    name="dimension30",
    ends={
        Property(name="dataaccess.ecoreanalytics31", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="DimensionDefinition", type=DimensionDefinition, multiplicity=Multiplicity(0, 1))
    }
)
groupedFactsOfGroupBy32: BinaryAssociation = BinaryAssociation(
    name="groupedFactsOfGroupBy32",
    ends={
        Property(name="dataaccess.ecoreanalytics34", type=behavioral_actions_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="GroupBy33", type=GroupBy, multiplicity=Multiplicity(0, 1))
    }
)
nestedBlocks37: BinaryAssociation = BinaryAssociation(
    name="nestedBlocks37",
    ends={
        Property(name="actions39", type=behavioral_actions_StatementWithNestedBlocks, multiplicity=Multiplicity(1, 1)),
        Property(name="Block38", type=Block, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
initExpression40: BinaryAssociation = BinaryAssociation(
    name="initExpression40",
    ends={
        Property(name="dataaccess.ecoreexpressions42", type=behavioral_actions_NamedValueWithOptionalInitExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Expression41", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedValueDeclaration43: BinaryAssociation = BinaryAssociation(
    name="namedValueDeclaration43",
    ends={
        Property(name="actions44", type=behavioral_actions_NamedValueWithOptionalInitExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedValueDeclaration", type=NamedValueDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
producer45: BinaryAssociation = BinaryAssociation(
    name="producer45",
    ends={
        Property(name="events", type=behavioral_events_Subscription, multiplicity=Multiplicity(1, 1)),
        Property(name="EventProducer", type=EventProducer, multiplicity=Multiplicity(1, 1))
    }
)
filters46: BinaryAssociation = BinaryAssociation(
    name="filters46",
    ends={
        Property(name="events47", type=behavioral_events_Subscription, multiplicity=Multiplicity(1, 1)),
        Property(name="EventFilter", type=EventFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subscribingClass48: BinaryAssociation = BinaryAssociation(
    name="subscribingClass48",
    ends={
        Property(name="data.ecoreclasses49", type=behavioral_events_Subscription, multiplicity=Multiplicity(1, 1)),
        Property(name="SapClass", type=SapClass, multiplicity=Multiplicity(1, 1))
    }
)
subscriptions50: BinaryAssociation = BinaryAssociation(
    name="subscriptions50",
    ends={
        Property(name="events51", type=behavioral_events_EventProducer, multiplicity=Multiplicity(1, 1)),
        Property(name="Subscription", type=Subscription, multiplicity=Multiplicity(0, 9999))
    }
)
namedValue35: BinaryAssociation = BinaryAssociation(
    name="namedValue35",
    ends={
        Property(name="actions36", type=behavioral_actions_NamedValueDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedValueWithOptionalInitExpression", type=NamedValueWithOptionalInitExpression, multiplicity=Multiplicity(1, 1))
    }
)
subscription54: BinaryAssociation = BinaryAssociation(
    name="subscription54",
    ends={
        Property(name="events56", type=behavioral_events_EventFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="Subscription55", type=Subscription, multiplicity=Multiplicity(1, 1))
    }
)
test57: BinaryAssociation = BinaryAssociation(
    name="test57",
    ends={
        Property(name="Block58", type=behavioral_events_EventFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_events_EventFilter", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
businessObjectNode59: BinaryAssociation = BinaryAssociation(
    name="businessObjectNode59",
    ends={
        Property(name="data.ecoreclasses61", type=behavioral_status_and_action_old_SAMAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SapClass60", type=SapClass, multiplicity=Multiplicity(1, 1))
    }
)
samSchemaActions62: BinaryAssociation = BinaryAssociation(
    name="samSchemaActions62",
    ends={
        Property(name="status_and_action_old", type=behavioral_status_and_action_old_SAMAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaAction", type=SAMSchemaAction, multiplicity=Multiplicity(0, 9999))
    }
)
businessObjectNode63: BinaryAssociation = BinaryAssociation(
    name="businessObjectNode63",
    ends={
        Property(name="data.ecoreclasses65", type=behavioral_status_and_action_old_SAMStatusVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="SapClass64", type=SapClass, multiplicity=Multiplicity(1, 1))
    }
)
samStatusValues66: BinaryAssociation = BinaryAssociation(
    name="samStatusValues66",
    ends={
        Property(name="status_and_action_old67", type=behavioral_status_and_action_old_SAMStatusVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMStatusValue", type=SAMStatusValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samSchemaVariables68: BinaryAssociation = BinaryAssociation(
    name="samSchemaVariables68",
    ends={
        Property(name="status_and_action_old69", type=behavioral_status_and_action_old_SAMStatusVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaVariable", type=SAMSchemaVariable, multiplicity=Multiplicity(0, 9999))
    }
)
businessObject70: BinaryAssociation = BinaryAssociation(
    name="businessObject70",
    ends={
        Property(name="data.ecoreclasses72", type=behavioral_status_and_action_old_SAMDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="SapClass71", type=SapClass, multiplicity=Multiplicity(1, 1))
    }
)
samSchemaDerivators73: BinaryAssociation = BinaryAssociation(
    name="samSchemaDerivators73",
    ends={
        Property(name="status_and_action_old74", type=behavioral_status_and_action_old_SAMDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaDerivator", type=SAMSchemaDerivator, multiplicity=Multiplicity(0, 9999))
    }
)
notificationSignatures52: BinaryAssociation = BinaryAssociation(
    name="notificationSignatures52",
    ends={
        Property(name="data.ecoreclasses53", type=behavioral_events_EventProducer, multiplicity=Multiplicity(1, 1)),
        Property(name="MethodSignature", type=MethodSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessObjectNode77: BinaryAssociation = BinaryAssociation(
    name="businessObjectNode77",
    ends={
        Property(name="data.ecoreclasses79", type=behavioral_status_and_action_old_SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="SapClass78", type=SapClass, multiplicity=Multiplicity(1, 1))
    }
)
samOperators80: BinaryAssociation = BinaryAssociation(
    name="samOperators80",
    ends={
        Property(name="status_and_action_old81", type=behavioral_status_and_action_old_SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMOperator", type=SAMOperator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samSchemaVariables82: BinaryAssociation = BinaryAssociation(
    name="samSchemaVariables82",
    ends={
        Property(name="status_and_action_old84", type=behavioral_status_and_action_old_SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaVariable83", type=SAMSchemaVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samSchemaActions85: BinaryAssociation = BinaryAssociation(
    name="samSchemaActions85",
    ends={
        Property(name="status_and_action_old87", type=behavioral_status_and_action_old_SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaAction86", type=SAMSchemaAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samSchemaDerivators88: BinaryAssociation = BinaryAssociation(
    name="samSchemaDerivators88",
    ends={
        Property(name="status_and_action_old90", type=behavioral_status_and_action_old_SAMStatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaDerivator89", type=SAMSchemaDerivator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samStatusSchema91: BinaryAssociation = BinaryAssociation(
    name="samStatusSchema91",
    ends={
        Property(name="status_and_action_old92", type=behavioral_status_and_action_old_SAMOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMStatusSchema", type=SAMStatusSchema, multiplicity=Multiplicity(1, 1))
    }
)
samSchemaValues93: BinaryAssociation = BinaryAssociation(
    name="samSchemaValues93",
    ends={
        Property(name="status_and_action_old94", type=behavioral_status_and_action_old_SAMOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaValue", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999))
    }
)
samSourceOperators95: BinaryAssociation = BinaryAssociation(
    name="samSourceOperators95",
    ends={
        Property(name="status_and_action_old97", type=behavioral_status_and_action_old_SAMOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMOperator96", type=SAMOperator, multiplicity=Multiplicity(0, 9999))
    }
)
samTargetOperators98: BinaryAssociation = BinaryAssociation(
    name="samTargetOperators98",
    ends={
        Property(name="status_and_action_old100", type=behavioral_status_and_action_old_SAMOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMOperator99", type=SAMOperator, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaActions101: BinaryAssociation = BinaryAssociation(
    name="samSchemaActions101",
    ends={
        Property(name="status_and_action_old103", type=behavioral_status_and_action_old_SAMOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaAction102", type=SAMSchemaAction, multiplicity=Multiplicity(0, 9999))
    }
)
samStatusSchema104: BinaryAssociation = BinaryAssociation(
    name="samStatusSchema104",
    ends={
        Property(name="status_and_action_old106", type=behavioral_status_and_action_old_SAMSchemaVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMStatusSchema105", type=SAMStatusSchema, multiplicity=Multiplicity(1, 1))
    }
)
samSchemaValues107: BinaryAssociation = BinaryAssociation(
    name="samSchemaValues107",
    ends={
        Property(name="status_and_action_old109", type=behavioral_status_and_action_old_SAMSchemaVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaValue108", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samSchemaValue110: BinaryAssociation = BinaryAssociation(
    name="samSchemaValue110",
    ends={
        Property(name="status_and_action_old112", type=behavioral_status_and_action_old_SAMSchemaVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMStatusVariable111", type=SAMStatusVariable, multiplicity=Multiplicity(1, 1))
    }
)
samTargetSchemaDerivators113: BinaryAssociation = BinaryAssociation(
    name="samTargetSchemaDerivators113",
    ends={
        Property(name="status_and_action_old115", type=behavioral_status_and_action_old_SAMSchemaVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaDerivator114", type=SAMSchemaDerivator, multiplicity=Multiplicity(0, 9999))
    }
)
samSourceSchemaDerivators116: BinaryAssociation = BinaryAssociation(
    name="samSourceSchemaDerivators116",
    ends={
        Property(name="status_and_action_old118", type=behavioral_status_and_action_old_SAMSchemaVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaDerivator117", type=SAMSchemaDerivator, multiplicity=Multiplicity(0, 9999))
    }
)
samStatusVariable75: BinaryAssociation = BinaryAssociation(
    name="samStatusVariable75",
    ends={
        Property(name="status_and_action_old76", type=behavioral_status_and_action_old_SAMStatusValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMStatusVariable", type=SAMStatusVariable, multiplicity=Multiplicity(1, 1))
    }
)
samSourceSchemaActions122: BinaryAssociation = BinaryAssociation(
    name="samSourceSchemaActions122",
    ends={
        Property(name="status_and_action_old124", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaAction123", type=SAMSchemaAction, multiplicity=Multiplicity(0, 9999))
    }
)
samSourceSchemaValues125: BinaryAssociation = BinaryAssociation(
    name="samSourceSchemaValues125",
    ends={
        Property(name="status_and_action_old127", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaValue126", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999))
    }
)
samTargetSchemaValues128: BinaryAssociation = BinaryAssociation(
    name="samTargetSchemaValues128",
    ends={
        Property(name="status_and_action_old130", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaValue129", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999))
    }
)
samOperators131: BinaryAssociation = BinaryAssociation(
    name="samOperators131",
    ends={
        Property(name="status_and_action_old133", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMOperator132", type=SAMOperator, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaActions134: BinaryAssociation = BinaryAssociation(
    name="samSchemaActions134",
    ends={
        Property(name="status_and_action_old136", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaAction135", type=SAMSchemaAction, multiplicity=Multiplicity(0, 9999))
    }
)
samStatusSchema137: BinaryAssociation = BinaryAssociation(
    name="samStatusSchema137",
    ends={
        Property(name="status_and_action_old139", type=behavioral_status_and_action_old_SAMSchemaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMStatusSchema138", type=SAMStatusSchema, multiplicity=Multiplicity(1, 1))
    }
)
samAction140: BinaryAssociation = BinaryAssociation(
    name="samAction140",
    ends={
        Property(name="status_and_action_old141", type=behavioral_status_and_action_old_SAMSchemaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMAction", type=SAMAction, multiplicity=Multiplicity(1, 1))
    }
)
samTargetSchemaValues142: BinaryAssociation = BinaryAssociation(
    name="samTargetSchemaValues142",
    ends={
        Property(name="status_and_action_old144", type=behavioral_status_and_action_old_SAMSchemaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaValue143", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaValues145: BinaryAssociation = BinaryAssociation(
    name="samSchemaValues145",
    ends={
        Property(name="status_and_action_old147", type=behavioral_status_and_action_old_SAMSchemaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaValue146", type=SAMSchemaValue, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaOperators148: BinaryAssociation = BinaryAssociation(
    name="samSchemaOperators148",
    ends={
        Property(name="status_and_action_old150", type=behavioral_status_and_action_old_SAMSchemaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMOperator149", type=SAMOperator, multiplicity=Multiplicity(0, 9999))
    }
)
samDerivator151: BinaryAssociation = BinaryAssociation(
    name="samDerivator151",
    ends={
        Property(name="status_and_action_old152", type=behavioral_status_and_action_old_SAMSchemaDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMDerivator", type=SAMDerivator, multiplicity=Multiplicity(1, 1))
    }
)
samStatusSchema153: BinaryAssociation = BinaryAssociation(
    name="samStatusSchema153",
    ends={
        Property(name="status_and_action_old155", type=behavioral_status_and_action_old_SAMSchemaDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMStatusSchema154", type=SAMStatusSchema, multiplicity=Multiplicity(1, 1))
    }
)
samSourceSchemaVariables156: BinaryAssociation = BinaryAssociation(
    name="samSourceSchemaVariables156",
    ends={
        Property(name="status_and_action_old158", type=behavioral_status_and_action_old_SAMSchemaDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaVariable157", type=SAMSchemaVariable, multiplicity=Multiplicity(0, 9999))
    }
)
samTargetSchemaVariable159: BinaryAssociation = BinaryAssociation(
    name="samTargetSchemaVariable159",
    ends={
        Property(name="status_and_action_old161", type=behavioral_status_and_action_old_SAMSchemaDerivator, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaVariable160", type=SAMSchemaVariable, multiplicity=Multiplicity(0, 9999))
    }
)
samSchemaVariable119: BinaryAssociation = BinaryAssociation(
    name="samSchemaVariable119",
    ends={
        Property(name="status_and_action_old121", type=behavioral_status_and_action_old_SAMSchemaValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SAMSchemaVariable120", type=SAMSchemaVariable, multiplicity=Multiplicity(1, 1))
    }
)
nodes162: BinaryAssociation = BinaryAssociation(
    name="nodes162",
    ends={
        Property(name="design_BusinessObjectNode", type=behavioral_design_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_design_BusinessObject", type=design_BusinessObjectNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables163: BinaryAssociation = BinaryAssociation(
    name="variables163",
    ends={
        Property(name="design_StatusVariable", type=behavioral_design_BusinessObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_design_BusinessObjectNode", type=design_StatusVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions164: BinaryAssociation = BinaryAssociation(
    name="actions164",
    ends={
        Property(name="design_Action", type=behavioral_design_BusinessObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_design_BusinessObjectNode165", type=design_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values166: BinaryAssociation = BinaryAssociation(
    name="values166",
    ends={
        Property(name="design_AbstractStatusValue", type=behavioral_design_AbstractStatusVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_design_AbstractStatusVariable", type=design_AbstractStatusValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node167: BinaryAssociation = BinaryAssociation(
    name="node167",
    ends={
        Property(name="data.ecoreclasses169", type=behavioral_assembly_StatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="SapClass168", type=SapClass, multiplicity=Multiplicity(0, 1))
    }
)
elements170: BinaryAssociation = BinaryAssociation(
    name="elements170",
    ends={
        Property(name="assembly_SchemaElement", type=behavioral_assembly_StatusSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_StatusSchema", type=assembly_SchemaElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source171: BinaryAssociation = BinaryAssociation(
    name="source171",
    ends={
        Property(name="assembly_ConnectableElement", type=behavioral_assembly_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_Connector", type=assembly_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
target172: BinaryAssociation = BinaryAssociation(
    name="target172",
    ends={
        Property(name="assembly_ConnectableElement174", type=behavioral_assembly_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_Connector173", type=assembly_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
action175: BinaryAssociation = BinaryAssociation(
    name="action175",
    ends={
        Property(name="Signature", type=behavioral_assembly_ActionProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_ActionProxy", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
value176: BinaryAssociation = BinaryAssociation(
    name="value176",
    ends={
        Property(name="design_StatusValue", type=behavioral_assembly_StatusValueProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_StatusValueProxy", type=design_StatusValue, multiplicity=Multiplicity(0, 1))
    }
)
strategy177: BinaryAssociation = BinaryAssociation(
    name="strategy177",
    ends={
        Property(name="assembly_Strategy", type=behavioral_assembly_Precondition, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_Precondition", type=assembly_Strategy, multiplicity=Multiplicity(1, 1))
    }
)
variable178: BinaryAssociation = BinaryAssociation(
    name="variable178",
    ends={
        Property(name="design_StatusVariable179", type=behavioral_assembly_StatusVariableProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioral_assembly_StatusVariableProxy", type=design_StatusVariable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_behavioral_actions_Assignment_StatementWithArgument = Generalization(general=StatementWithArgument, specific=behavioral_actions_Assignment)
gen_behavioral_actions_Statement_InScope = Generalization(general=InScope, specific=behavioral_actions_Statement)
gen_behavioral_actions_Block_classes_FunctionSignatureImplementation = Generalization(general=classes_FunctionSignatureImplementation, specific=behavioral_actions_Block)
gen_behavioral_actions_Block_classes_InScope = Generalization(general=classes_InScope, specific=behavioral_actions_Block)
gen_behavioral_actions_IfElse_actions_ConditionalStatement = Generalization(general=actions_ConditionalStatement, specific=behavioral_actions_IfElse)
gen_behavioral_actions_IfElse_actions_StatementWithNestedBlocks = Generalization(general=actions_StatementWithNestedBlocks, specific=behavioral_actions_IfElse)
gen_behavioral_actions_Foreach_SingleBlockStatement = Generalization(general=SingleBlockStatement, specific=behavioral_actions_Foreach)
gen_behavioral_actions_Return_StatementWithArgument = Generalization(general=StatementWithArgument, specific=behavioral_actions_Return)
gen_behavioral_actions_AddLink_LinkManipulationStatement = Generalization(general=LinkManipulationStatement, specific=behavioral_actions_AddLink)
gen_behavioral_actions_RemoveLink_LinkManipulationStatement = Generalization(general=LinkManipulationStatement, specific=behavioral_actions_RemoveLink)
gen_behavioral_actions_LinkManipulationStatement_Statement = Generalization(general=Statement, specific=behavioral_actions_LinkManipulationStatement)
gen_behavioral_actions_ExpressionStatement_Statement = Generalization(general=Statement, specific=behavioral_actions_ExpressionStatement)
gen_behavioral_actions_WhileLoop_actions_ConditionalStatement = Generalization(general=actions_ConditionalStatement, specific=behavioral_actions_WhileLoop)
gen_behavioral_actions_WhileLoop_actions_SingleBlockStatement = Generalization(general=actions_SingleBlockStatement, specific=behavioral_actions_WhileLoop)
gen_behavioral_actions_Variable_NamedValueWithOptionalInitExpression = Generalization(general=NamedValueWithOptionalInitExpression, specific=behavioral_actions_Variable)
gen_behavioral_actions_Iterator_NamedValue = Generalization(general=NamedValue, specific=behavioral_actions_Iterator)
gen_behavioral_actions_Constant_NamedValueWithOptionalInitExpression = Generalization(general=NamedValueWithOptionalInitExpression, specific=behavioral_actions_Constant)
gen_behavioral_actions_NamedValueDeclaration_Statement = Generalization(general=Statement, specific=behavioral_actions_NamedValueDeclaration)
gen_behavioral_actions_StatementWithNestedBlocks_Statement = Generalization(general=Statement, specific=behavioral_actions_StatementWithNestedBlocks)
gen_behavioral_actions_SingleBlockStatement_StatementWithNestedBlocks = Generalization(general=StatementWithNestedBlocks, specific=behavioral_actions_SingleBlockStatement)
gen_behavioral_actions_StatementWithArgument_actions_Statement = Generalization(general=actions_Statement, specific=behavioral_actions_StatementWithArgument)
gen_behavioral_actions_StatementWithArgument_expressions_WithArgument = Generalization(general=expressions_WithArgument, specific=behavioral_actions_StatementWithArgument)
gen_behavioral_actions_NamedValueWithOptionalInitExpression_NamedValue = Generalization(general=NamedValue, specific=behavioral_actions_NamedValueWithOptionalInitExpression)
gen_behavioral_actions_ConditionalStatement_expressions_Conditional = Generalization(general=expressions_Conditional, specific=behavioral_actions_ConditionalStatement)
gen_behavioral_actions_ConditionalStatement_actions_Statement = Generalization(general=actions_Statement, specific=behavioral_actions_ConditionalStatement)
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
gen_behavioral_assembly_EnablingStrategy_Strategy = Generalization(general=Strategy, specific=behavioral_assembly_EnablingStrategy)
gen_behavioral_assembly_InhibitingStrategy_Strategy = Generalization(general=Strategy, specific=behavioral_assembly_InhibitingStrategy)
gen_behavioral_assembly_SchemaElement_NamedElement = Generalization(general=NamedElement, specific=behavioral_assembly_SchemaElement)
gen_behavioral_assembly_AndOperator_Operator = Generalization(general=Operator, specific=behavioral_assembly_AndOperator)
gen_behavioral_assembly_OrOperator_Operator = Generalization(general=Operator, specific=behavioral_assembly_OrOperator)
gen_behavioral_assembly_RequiredStrategy_Strategy = Generalization(general=Strategy, specific=behavioral_assembly_RequiredStrategy)
gen_behavioral_assembly_NeutralStrategy_Strategy = Generalization(general=Strategy, specific=behavioral_assembly_NeutralStrategy)

# Domain Model
domain_model = DomainModel(
    name="behavioral",
    types={behavioral_bpdm_Dummy, behavioral_businesstasks_TaskAgent, behavioral_actions_Assignment, StatementWithArgument, Variable, behavioral_actions_Statement, InScope, Block, behavioral_actions_Block, classes_FunctionSignatureImplementation, classes_InScope, Statement, NamedValue, StatementWithNestedBlocks, behavioral_actions_IfElse, actions_ConditionalStatement, actions_StatementWithNestedBlocks, behavioral_actions_Foreach, SingleBlockStatement, Expression, Iterator, behavioral_actions_Return, behavioral_actions_AddLink, LinkManipulationStatement, behavioral_actions_RemoveLink, behavioral_actions_LinkManipulationStatement, Association, behavioral_actions_ExpressionStatement, behavioral_actions_Sort, behavioral_actions_QueryInvocation, behavioral_actions_WhileLoop, actions_SingleBlockStatement, collectionexpressions_Iterate, behavioral_actions_Variable, Assignment, behavioral_actions_Iterator, Foreach, Selection, FromClause, GroupBy, DimensionDefinition, behavioral_actions_Constant, NamedValueWithOptionalInitExpression, behavioral_actions_NamedValueDeclaration, behavioral_actions_StatementWithNestedBlocks, behavioral_actions_SingleBlockStatement, behavioral_actions_StatementWithArgument, actions_Statement, expressions_WithArgument, behavioral_actions_NamedValueWithOptionalInitExpression, NamedValueDeclaration, behavioral_actions_ConditionalStatement, expressions_Conditional, behavioral_rules_Dummy, behavioral_events_Subscription, NamedElement, EventProducer, EventFilter, SapClass, behavioral_events_EventProducer, Subscription, behavioral_transactions_Dummy, behavioral_status_and_action_old_SAMAction, SAMSchemaAction, behavioral_status_and_action_old_SAMStatusVariable, SAMStatusValue, SAMSchemaVariable, behavioral_status_and_action_old_SAMDerivator, SAMSchemaDerivator, behavioral_status_and_action_old_SAMStatusValue, MethodSignature, behavioral_events_EventFilter, behavioral_status_and_action_old_SAMStatusSchema, SAMOperator, behavioral_status_and_action_old_SAMOperator, SAMStatusSchema, SAMSchemaValue, behavioral_status_and_action_old_SAMSchemaVariable, behavioral_status_and_action_old_SAMSchemaValue, SAMStatusVariable, behavioral_status_and_action_old_SAMSchemaAction, SAMAction, behavioral_status_and_action_old_SAMSchemaDerivator, SAMDerivator, behavioral_design_BusinessObject, design_BusinessObjectNode, behavioral_design_BusinessObjectNode, design_StatusVariable, design_Action, behavioral_design_StatusVariable, AbstractStatusVariable, behavioral_design_StatusValue, AbstractStatusValue, behavioral_design_Action, AbstractAction, behavioral_design_AbstractStatusVariable, design_AbstractStatusValue, behavioral_design_AbstractStatusValue, behavioral_design_AbstractAction, behavioral_assembly_StatusSchema, assembly_SchemaElement, behavioral_assembly_Connector, SchemaElement, assembly_ConnectableElement, behavioral_assembly_Operator, ConnectableElement, behavioral_assembly_ConnectableElement, behavioral_assembly_ActionProxy, design_AbstractAction, Signature, behavioral_assembly_StatusValueProxy, design_StatusValue, behavioral_assembly_Transition, Connector, behavioral_assembly_Synchroniser, behavioral_assembly_Precondition, assembly_Strategy, behavioral_assembly_StatusVariableProxy, design_AbstractStatusVariable, behavioral_assembly_EnablingStrategy, behavioral_assembly_InhibitingStrategy, behavioral_assembly_Strategy, behavioral_assembly_SchemaElement, behavioral_assembly_AndOperator, Operator, behavioral_assembly_OrOperator, behavioral_assembly_RequiredStrategy, Strategy, behavioral_assembly_NeutralStrategy, SAMOperatorKindEnum, SAMDerivatorKindEnum, PreconditionKindEnum},
    associations={assignTo0, block1, statements3, variables5, owningStatement6, collection8, forVariable9, association11, objects12, expression15, iterate17, assignments19, boundToFor21, iterate23, selection26, fromClause27, factOfGroupBy29, dimension30, groupedFactsOfGroupBy32, nestedBlocks37, initExpression40, namedValueDeclaration43, producer45, filters46, subscribingClass48, subscriptions50, namedValue35, subscription54, test57, businessObjectNode59, samSchemaActions62, businessObjectNode63, samStatusValues66, samSchemaVariables68, businessObject70, samSchemaDerivators73, notificationSignatures52, businessObjectNode77, samOperators80, samSchemaVariables82, samSchemaActions85, samSchemaDerivators88, samStatusSchema91, samSchemaValues93, samSourceOperators95, samTargetOperators98, samSchemaActions101, samStatusSchema104, samSchemaValues107, samSchemaValue110, samTargetSchemaDerivators113, samSourceSchemaDerivators116, samStatusVariable75, samSourceSchemaActions122, samSourceSchemaValues125, samTargetSchemaValues128, samOperators131, samSchemaActions134, samStatusSchema137, samAction140, samTargetSchemaValues142, samSchemaValues145, samSchemaOperators148, samDerivator151, samStatusSchema153, samSourceSchemaVariables156, samTargetSchemaVariable159, samSchemaVariable119, nodes162, variables163, actions164, values166, node167, elements170, source171, target172, action175, value176, strategy177, variable178},
    generalizations={gen_behavioral_actions_Assignment_StatementWithArgument, gen_behavioral_actions_Statement_InScope, gen_behavioral_actions_Block_classes_FunctionSignatureImplementation, gen_behavioral_actions_Block_classes_InScope, gen_behavioral_actions_IfElse_actions_ConditionalStatement, gen_behavioral_actions_IfElse_actions_StatementWithNestedBlocks, gen_behavioral_actions_Foreach_SingleBlockStatement, gen_behavioral_actions_Return_StatementWithArgument, gen_behavioral_actions_AddLink_LinkManipulationStatement, gen_behavioral_actions_RemoveLink_LinkManipulationStatement, gen_behavioral_actions_LinkManipulationStatement_Statement, gen_behavioral_actions_ExpressionStatement_Statement, gen_behavioral_actions_WhileLoop_actions_ConditionalStatement, gen_behavioral_actions_WhileLoop_actions_SingleBlockStatement, gen_behavioral_actions_Variable_NamedValueWithOptionalInitExpression, gen_behavioral_actions_Iterator_NamedValue, gen_behavioral_actions_Constant_NamedValueWithOptionalInitExpression, gen_behavioral_actions_NamedValueDeclaration_Statement, gen_behavioral_actions_StatementWithNestedBlocks_Statement, gen_behavioral_actions_SingleBlockStatement_StatementWithNestedBlocks, gen_behavioral_actions_StatementWithArgument_actions_Statement, gen_behavioral_actions_StatementWithArgument_expressions_WithArgument, gen_behavioral_actions_NamedValueWithOptionalInitExpression_NamedValue, gen_behavioral_actions_ConditionalStatement_expressions_Conditional, gen_behavioral_actions_ConditionalStatement_actions_Statement, gen_behavioral_events_Subscription_NamedElement, gen_behavioral_design_BusinessObjectNode_NamedElement, gen_behavioral_design_StatusVariable_AbstractStatusVariable, gen_behavioral_design_StatusValue_AbstractStatusValue, gen_behavioral_design_Action_AbstractAction, gen_behavioral_design_AbstractStatusVariable_NamedElement, gen_behavioral_design_AbstractStatusValue_NamedElement, gen_behavioral_design_AbstractAction_NamedElement, gen_behavioral_assembly_StatusSchema_NamedElement, gen_behavioral_assembly_Connector_SchemaElement, gen_behavioral_assembly_Operator_ConnectableElement, gen_behavioral_assembly_ConnectableElement_SchemaElement, gen_behavioral_assembly_ActionProxy_design_AbstractAction, gen_behavioral_assembly_ActionProxy_design_Action, gen_behavioral_assembly_ActionProxy_assembly_ConnectableElement, gen_behavioral_assembly_StatusValueProxy_design_AbstractStatusValue, gen_behavioral_assembly_StatusValueProxy_design_StatusValue, gen_behavioral_assembly_StatusValueProxy_assembly_ConnectableElement, gen_behavioral_assembly_Transition_Connector, gen_behavioral_assembly_Synchroniser_Connector, gen_behavioral_assembly_Precondition_Connector, gen_behavioral_assembly_StatusVariableProxy_design_AbstractStatusVariable, gen_behavioral_assembly_StatusVariableProxy_design_StatusVariable, gen_behavioral_assembly_StatusVariableProxy_assembly_ConnectableElement, gen_behavioral_assembly_EnablingStrategy_Strategy, gen_behavioral_assembly_InhibitingStrategy_Strategy, gen_behavioral_assembly_SchemaElement_NamedElement, gen_behavioral_assembly_AndOperator_Operator, gen_behavioral_assembly_OrOperator_Operator, gen_behavioral_assembly_RequiredStrategy_Strategy, gen_behavioral_assembly_NeutralStrategy_Strategy},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)