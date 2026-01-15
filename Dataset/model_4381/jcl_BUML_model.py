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
AdressSpaceEnum: Enumeration = Enumeration(
    name="AdressSpaceEnum",
    literals={
            EnumerationLiteral(name="real"),
			EnumerationLiteral(name="virtual")
    }
)

TypeRunEnum: Enumeration = Enumeration(
    name="TypeRunEnum",
    literals={
            EnumerationLiteral(name="copy"),
			EnumerationLiteral(name="hold"),
			EnumerationLiteral(name="jclhold"),
			EnumerationLiteral(name="scan")
    }
)

# Classes
jcl_commons_NamedElement = Class(name="jcl::commons::NamedElement")
jcl_commons_PhraseableElement = Class(name="jcl::commons::PhraseableElement")
jcl_commons_CommentableElement = Class(name="jcl::commons::CommentableElement", is_abstract=True)
jcl_commons_IncompleteElement = Class(name="jcl::commons::IncompleteElement", is_abstract=True)
Water = Class(name="Water")
jcl_parameters_Parameter = Class(name="jcl::parameters::Parameter", is_abstract=True)
jcl_parameters_Display = Class(name="jcl::parameters::Display")
Parameter_ = Class(name="Parameter")
jcl_parameters_JobClass = Class(name="jcl::parameters::JobClass")
jcl_parameters_MessageClass = Class(name="jcl::parameters::MessageClass")
jcl_parameters_Password = Class(name="jcl::parameters::Password")
jcl_parameters_Priority = Class(name="jcl::parameters::Priority")
jcl_parameters_UserID = Class(name="jcl::parameters::UserID")
jcl_parameters_MessageLevel = Class(name="jcl::parameters::MessageLevel")
jcl_parameters_TypeRun = Class(name="jcl::parameters::TypeRun")
jcl_parameters_AddressSpace = Class(name="jcl::parameters::AddressSpace")
parameters_Parameter = Class(name="parameters::Parameter")
commons_ProcedureStepElement = Class(name="commons::ProcedureStepElement")
jcl_commons_ProcedureStepElement = Class(name="jcl::commons::ProcedureStepElement", is_abstract=True)
jcl_parameters_Bytes = Class(name="jcl::parameters::Bytes")
jcl_parameters_AccountInfo = Class(name="jcl::parameters::AccountInfo")
Literal = Class(name="Literal")
jcl_parameters_Argument = Class(name="jcl::parameters::Argument")
jcl_parameters_Condition = Class(name="jcl::parameters::Condition")
Condition = Class(name="Condition")
jcl_parameters_DatasetName = Class(name="jcl::parameters::DatasetName")
jcl_parameters_Other = Class(name="jcl::parameters::Other")
commons_NamedElement = Class(name="commons::NamedElement")
jcl_statements_Statement = Class(name="jcl::statements::Statement", is_abstract=True)
members_Member = Class(name="members::Member")
jcl_statements_Execute = Class(name="jcl::statements::Execute", is_abstract=True)
Statement = Class(name="Statement")
jcl_statements_StatementContainer = Class(name="jcl::statements::StatementContainer", is_abstract=True)
jcl_statements_Condition = Class(name="jcl::statements::Condition")
statements_StatementContainer = Class(name="statements::StatementContainer")
statements_Statement = Class(name="statements::Statement")
jcl_statements_DataDefinition = Class(name="jcl::statements::DataDefinition")
jcl_statements_Set = Class(name="jcl::statements::Set")
jcl_statements_Input = Class(name="jcl::statements::Input")
jcl_statements_Output = Class(name="jcl::statements::Output")
jcl_statements_JCLLibrary = Class(name="jcl::statements::JCLLibrary")
jcl_statements_Control = Class(name="jcl::statements::Control")
EndControl = Class(name="EndControl")
jcl_statements_Include = Class(name="jcl::statements::Include")
jcl_statements_Command = Class(name="jcl::statements::Command")
jcl_statements_ExecuteProgram = Class(name="jcl::statements::ExecuteProgram")
Execute = Class(name="Execute")
jcl_statements_ExecuteProcedure = Class(name="jcl::statements::ExecuteProcedure")
jcl_statements_EndControl = Class(name="jcl::statements::EndControl")
jcl_containers_JCLRoot = Class(name="jcl::containers::JCLRoot")
Member = Class(name="Member")
jcl_containers_JobUnit = Class(name="jcl::containers::JobUnit")
containers_JCLRoot = Class(name="containers::JCLRoot")
commons_IncompleteElement = Class(name="commons::IncompleteElement")
ExecuteProgram = Class(name="ExecuteProgram")
jcl_expressions_Expression = Class(name="jcl::expressions::Expression", is_abstract=True)
Expression = Class(name="Expression")
jcl_expressions_RelationalExpression = Class(name="jcl::expressions::RelationalExpression")
ConditionalAndExpressionChild = Class(name="ConditionalAndExpressionChild")
RelationalExpressionChild = Class(name="RelationalExpressionChild")
RelationOperator = Class(name="RelationOperator")
jcl_expressions_ConditionalExpression = Class(name="jcl::expressions::ConditionalExpression", is_abstract=True)
jcl_expressions_ConditionalOrExpression = Class(name="jcl::expressions::ConditionalOrExpression")
ConditionalExpression = Class(name="ConditionalExpression")
ConditionalOrExpressionChild = Class(name="ConditionalOrExpressionChild")
Or = Class(name="Or")
jcl_expressions_ConditionalOrExpressionChild = Class(name="jcl::expressions::ConditionalOrExpressionChild", is_abstract=True)
jcl_expressions_ConditionalAndExpression = Class(name="jcl::expressions::ConditionalAndExpression")
And = Class(name="And")
jcl_expressions_ConditionalAndExpressionChild = Class(name="jcl::expressions::ConditionalAndExpressionChild", is_abstract=True)
jcl_expressions_RelationalExpressionChild = Class(name="jcl::expressions::RelationalExpressionChild", is_abstract=True)
jcl_expressions_UnaryExpressionChild = Class(name="jcl::expressions::UnaryExpressionChild", is_abstract=True)
jcl_expressions_UnaryExpression = Class(name="jcl::expressions::UnaryExpression")
UnaryExpressionChild = Class(name="UnaryExpressionChild")
UnaryOperator = Class(name="UnaryOperator")
jcl_expressions_NestedExpression = Class(name="jcl::expressions::NestedExpression")
PrimaryExpression = Class(name="PrimaryExpression")
jcl_expressions_PrimaryExpression = Class(name="jcl::expressions::PrimaryExpression", is_abstract=True)
jcl_expressions_Abend = Class(name="jcl::expressions::Abend")
expressions_PrimaryExpression = Class(name="expressions::PrimaryExpression")
IdentifierReference = Class(name="IdentifierReference")
jcl_expressions_Run = Class(name="jcl::expressions::Run")
jcl_operators_Operator = Class(name="jcl::operators::Operator", is_abstract=True)
PhraseableElement = Class(name="PhraseableElement")
jcl_operators_GreaterThan = Class(name="jcl::operators::GreaterThan")
jcl_operators_GreaterEqual = Class(name="jcl::operators::GreaterEqual")
jcl_operators_Equal = Class(name="jcl::operators::Equal")
jcl_operators_LessThan = Class(name="jcl::operators::LessThan")
jcl_operators_LessEqual = Class(name="jcl::operators::LessEqual")
jcl_operators_NotEqual = Class(name="jcl::operators::NotEqual")
jcl_operators_UnaryOperator = Class(name="jcl::operators::UnaryOperator", is_abstract=True)
Operator = Class(name="Operator")
jcl_operators_RelationOperator = Class(name="jcl::operators::RelationOperator", is_abstract=True)
jcl_operators_Negate = Class(name="jcl::operators::Negate")
jcl_operators_LogicOperator = Class(name="jcl::operators::LogicOperator")
jcl_operators_And = Class(name="jcl::operators::And")
LogicOperator = Class(name="LogicOperator")
jcl_literals_Literal = Class(name="jcl::literals::Literal", is_abstract=True)
jcl_literals_IntegerLiteral = Class(name="jcl::literals::IntegerLiteral")
literals_Literal = Class(name="literals::Literal")
conditions_ReturnCode = Class(name="conditions::ReturnCode")
jcl_literals_StringLiteral = Class(name="jcl::literals::StringLiteral")
jcl_literals_SpecialLiteral = Class(name="jcl::literals::SpecialLiteral")
jcl_references_Reference = Class(name="jcl::references::Reference", is_abstract=True)
Reference = Class(name="Reference")
jcl_references_ElementReference = Class(name="jcl::references::ElementReference", is_abstract=True)
ReferenceableElement = Class(name="ReferenceableElement")
jcl_references_IdentifierReference = Class(name="jcl::references::IdentifierReference")
jcl_operators_Or = Class(name="jcl::operators::Or")
references_ElementReference = Class(name="references::ElementReference")
jcl_references_ReferenceableElement = Class(name="jcl::references::ReferenceableElement", is_abstract=True)
jcl_conditions_Condition = Class(name="jcl::conditions::Condition", is_abstract=True)
jcl_conditions_Even = Class(name="jcl::conditions::Even")
PrimaryCondition = Class(name="PrimaryCondition")
jcl_conditions_Only = Class(name="jcl::conditions::Only")
jcl_conditions_PrimaryCondition = Class(name="jcl::conditions::PrimaryCondition", is_abstract=True)
jcl_conditions_NestedCondition = Class(name="jcl::conditions::NestedCondition")
jcl_conditions_RelationalCondition = Class(name="jcl::conditions::RelationalCondition")
conditions_PrimaryCondition = Class(name="conditions::PrimaryCondition")
ReturnCode = Class(name="ReturnCode")
jcl_conditions_ReturnCode = Class(name="jcl::conditions::ReturnCode", is_abstract=True)
jcl_procedures_Procedure = Class(name="jcl::procedures::Procedure")
jcl_members_Member = Class(name="jcl::members::Member", is_abstract=True)
jcl_waters_Water = Class(name="jcl::waters::Water")

# jcl_commons_NamedElement class attributes and methods
jcl_commons_NamedElement_name: Property = Property(name="name", type=StringType)
jcl_commons_NamedElement.attributes={jcl_commons_NamedElement_name}

# jcl_commons_PhraseableElement class attributes and methods
jcl_commons_PhraseableElement_isPhrase: Property = Property(name="isPhrase", type=BooleanType)
jcl_commons_PhraseableElement.attributes={jcl_commons_PhraseableElement_isPhrase}

# jcl_commons_CommentableElement class attributes and methods
jcl_commons_CommentableElement_comment: Property = Property(name="comment", type=StringType)
jcl_commons_CommentableElement.attributes={jcl_commons_CommentableElement_comment}

# jcl_commons_IncompleteElement class attributes and methods

# Water class attributes and methods

# jcl_parameters_Parameter class attributes and methods

# jcl_parameters_Display class attributes and methods
jcl_parameters_Display_value: Property = Property(name="value", type=StringType)
jcl_parameters_Display.attributes={jcl_parameters_Display_value}

# Parameter class attributes and methods

# jcl_parameters_JobClass class attributes and methods
jcl_parameters_JobClass_value: Property = Property(name="value", type=IntegerType)
jcl_parameters_JobClass.attributes={jcl_parameters_JobClass_value}

# jcl_parameters_MessageClass class attributes and methods
jcl_parameters_MessageClass_value: Property = Property(name="value", type=StringType)
jcl_parameters_MessageClass.attributes={jcl_parameters_MessageClass_value}

# jcl_parameters_Password class attributes and methods
jcl_parameters_Password_old: Property = Property(name="old", type=StringType)
jcl_parameters_Password_new: Property = Property(name="new", type=StringType)
jcl_parameters_Password.attributes={jcl_parameters_Password_old, jcl_parameters_Password_new}

# jcl_parameters_Priority class attributes and methods
jcl_parameters_Priority_value: Property = Property(name="value", type=IntegerType)
jcl_parameters_Priority.attributes={jcl_parameters_Priority_value}

# jcl_parameters_UserID class attributes and methods
jcl_parameters_UserID_value: Property = Property(name="value", type=StringType)
jcl_parameters_UserID.attributes={jcl_parameters_UserID_value}

# jcl_parameters_MessageLevel class attributes and methods
jcl_parameters_MessageLevel_statements: Property = Property(name="statements", type=IntegerType)
jcl_parameters_MessageLevel_messages: Property = Property(name="messages", type=IntegerType)
jcl_parameters_MessageLevel.attributes={jcl_parameters_MessageLevel_statements, jcl_parameters_MessageLevel_messages}

# jcl_parameters_TypeRun class attributes and methods
jcl_parameters_TypeRun_value: Property = Property(name="value", type=StringType)
jcl_parameters_TypeRun.attributes={jcl_parameters_TypeRun_value}

# jcl_parameters_AddressSpace class attributes and methods
jcl_parameters_AddressSpace_value: Property = Property(name="value", type=StringType)
jcl_parameters_AddressSpace.attributes={jcl_parameters_AddressSpace_value}

# parameters_Parameter class attributes and methods

# commons_ProcedureStepElement class attributes and methods

# jcl_commons_ProcedureStepElement class attributes and methods
jcl_commons_ProcedureStepElement_procStepName: Property = Property(name="procStepName", type=StringType)
jcl_commons_ProcedureStepElement.attributes={jcl_commons_ProcedureStepElement_procStepName}

# jcl_parameters_Bytes class attributes and methods
jcl_parameters_Bytes_value: Property = Property(name="value", type=IntegerType)
jcl_parameters_Bytes.attributes={jcl_parameters_Bytes_value}

# jcl_parameters_AccountInfo class attributes and methods

# Literal class attributes and methods

# jcl_parameters_Argument class attributes and methods
jcl_parameters_Argument_value: Property = Property(name="value", type=StringType)
jcl_parameters_Argument.attributes={jcl_parameters_Argument_value}

# jcl_parameters_Condition class attributes and methods

# Condition class attributes and methods

# jcl_parameters_DatasetName class attributes and methods
jcl_parameters_DatasetName_value: Property = Property(name="value", type=StringType)
jcl_parameters_DatasetName.attributes={jcl_parameters_DatasetName_value}

# jcl_parameters_Other class attributes and methods
jcl_parameters_Other_value: Property = Property(name="value", type=StringType)
jcl_parameters_Other.attributes={jcl_parameters_Other_value}

# commons_NamedElement class attributes and methods

# jcl_statements_Statement class attributes and methods

# members_Member class attributes and methods

# jcl_statements_Execute class attributes and methods

# Statement class attributes and methods

# jcl_statements_StatementContainer class attributes and methods

# jcl_statements_Condition class attributes and methods
jcl_statements_Condition_elseName: Property = Property(name="elseName", type=StringType)
jcl_statements_Condition_endName: Property = Property(name="endName", type=StringType)
jcl_statements_Condition.attributes={jcl_statements_Condition_elseName, jcl_statements_Condition_endName}

# statements_StatementContainer class attributes and methods

# statements_Statement class attributes and methods

# jcl_statements_DataDefinition class attributes and methods

# jcl_statements_Set class attributes and methods

# jcl_statements_Input class attributes and methods

# jcl_statements_Output class attributes and methods

# jcl_statements_JCLLibrary class attributes and methods

# jcl_statements_Control class attributes and methods
jcl_statements_Control_endName: Property = Property(name="endName", type=StringType)
jcl_statements_Control.attributes={jcl_statements_Control_endName}

# EndControl class attributes and methods

# jcl_statements_Include class attributes and methods

# jcl_statements_Command class attributes and methods
jcl_statements_Command_value: Property = Property(name="value", type=StringType)
jcl_statements_Command.attributes={jcl_statements_Command_value}

# jcl_statements_ExecuteProgram class attributes and methods
jcl_statements_ExecuteProgram_programName: Property = Property(name="programName", type=StringType)
jcl_statements_ExecuteProgram.attributes={jcl_statements_ExecuteProgram_programName}

# Execute class attributes and methods

# jcl_statements_ExecuteProcedure class attributes and methods
jcl_statements_ExecuteProcedure_procedureName: Property = Property(name="procedureName", type=StringType)
jcl_statements_ExecuteProcedure.attributes={jcl_statements_ExecuteProcedure_procedureName}

# jcl_statements_EndControl class attributes and methods

# jcl_containers_JCLRoot class attributes and methods

# Member class attributes and methods

# jcl_containers_JobUnit class attributes and methods

# containers_JCLRoot class attributes and methods

# commons_IncompleteElement class attributes and methods

# ExecuteProgram class attributes and methods

# jcl_expressions_Expression class attributes and methods

# Expression class attributes and methods

# jcl_expressions_RelationalExpression class attributes and methods

# ConditionalAndExpressionChild class attributes and methods

# RelationalExpressionChild class attributes and methods

# RelationOperator class attributes and methods

# jcl_expressions_ConditionalExpression class attributes and methods

# jcl_expressions_ConditionalOrExpression class attributes and methods

# ConditionalExpression class attributes and methods

# ConditionalOrExpressionChild class attributes and methods

# Or class attributes and methods

# jcl_expressions_ConditionalOrExpressionChild class attributes and methods

# jcl_expressions_ConditionalAndExpression class attributes and methods

# And class attributes and methods

# jcl_expressions_ConditionalAndExpressionChild class attributes and methods

# jcl_expressions_RelationalExpressionChild class attributes and methods

# jcl_expressions_UnaryExpressionChild class attributes and methods

# jcl_expressions_UnaryExpression class attributes and methods

# UnaryExpressionChild class attributes and methods

# UnaryOperator class attributes and methods

# jcl_expressions_NestedExpression class attributes and methods

# PrimaryExpression class attributes and methods

# jcl_expressions_PrimaryExpression class attributes and methods

# jcl_expressions_Abend class attributes and methods

# expressions_PrimaryExpression class attributes and methods

# IdentifierReference class attributes and methods

# jcl_expressions_Run class attributes and methods

# jcl_operators_Operator class attributes and methods

# PhraseableElement class attributes and methods

# jcl_operators_GreaterThan class attributes and methods

# jcl_operators_GreaterEqual class attributes and methods

# jcl_operators_Equal class attributes and methods

# jcl_operators_LessThan class attributes and methods

# jcl_operators_LessEqual class attributes and methods

# jcl_operators_NotEqual class attributes and methods

# jcl_operators_UnaryOperator class attributes and methods

# Operator class attributes and methods

# jcl_operators_RelationOperator class attributes and methods

# jcl_operators_Negate class attributes and methods

# jcl_operators_LogicOperator class attributes and methods

# jcl_operators_And class attributes and methods

# LogicOperator class attributes and methods

# jcl_literals_Literal class attributes and methods

# jcl_literals_IntegerLiteral class attributes and methods
jcl_literals_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
jcl_literals_IntegerLiteral.attributes={jcl_literals_IntegerLiteral_value}

# literals_Literal class attributes and methods

# conditions_ReturnCode class attributes and methods

# jcl_literals_StringLiteral class attributes and methods
jcl_literals_StringLiteral_value: Property = Property(name="value", type=StringType)
jcl_literals_StringLiteral.attributes={jcl_literals_StringLiteral_value}

# jcl_literals_SpecialLiteral class attributes and methods
jcl_literals_SpecialLiteral_value: Property = Property(name="value", type=StringType)
jcl_literals_SpecialLiteral.attributes={jcl_literals_SpecialLiteral_value}

# jcl_references_Reference class attributes and methods

# Reference class attributes and methods

# jcl_references_ElementReference class attributes and methods

# ReferenceableElement class attributes and methods

# jcl_references_IdentifierReference class attributes and methods

# jcl_operators_Or class attributes and methods

# references_ElementReference class attributes and methods

# jcl_references_ReferenceableElement class attributes and methods

# jcl_conditions_Condition class attributes and methods

# jcl_conditions_Even class attributes and methods

# PrimaryCondition class attributes and methods

# jcl_conditions_Only class attributes and methods

# jcl_conditions_PrimaryCondition class attributes and methods

# jcl_conditions_NestedCondition class attributes and methods

# jcl_conditions_RelationalCondition class attributes and methods

# conditions_PrimaryCondition class attributes and methods

# ReturnCode class attributes and methods

# jcl_conditions_ReturnCode class attributes and methods

# jcl_procedures_Procedure class attributes and methods
jcl_procedures_Procedure_endName: Property = Property(name="endName", type=StringType)
jcl_procedures_Procedure.attributes={jcl_procedures_Procedure_endName}

# jcl_members_Member class attributes and methods

# jcl_waters_Water class attributes and methods
jcl_waters_Water_value: Property = Property(name="value", type=StringType)
jcl_waters_Water.attributes={jcl_waters_Water_value}

# Relationships
waters0: BinaryAssociation = BinaryAssociation(
    name="waters0",
    ends={
        Property(name="Water", type=jcl_commons_IncompleteElement, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_commons_IncompleteElement", type=Water, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values1: BinaryAssociation = BinaryAssociation(
    name="values1",
    ends={
        Property(name="Literal", type=jcl_parameters_AccountInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_parameters_AccountInfo", type=Literal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition2: BinaryAssociation = BinaryAssociation(
    name="condition2",
    ends={
        Property(name="Condition", type=jcl_parameters_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_parameters_Condition", type=Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters3: BinaryAssociation = BinaryAssociation(
    name="parameters3",
    ends={
        Property(name="Parameter", type=jcl_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_statements_Statement", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements4: BinaryAssociation = BinaryAssociation(
    name="statements4",
    ends={
        Property(name="Statement", type=jcl_statements_StatementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_statements_StatementContainer", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition7: BinaryAssociation = BinaryAssociation(
    name="condition7",
    ends={
        Property(name="Expression", type=jcl_statements_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_statements_Condition8", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endControl9: BinaryAssociation = BinaryAssociation(
    name="endControl9",
    ends={
        Property(name="EndControl", type=jcl_statements_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_statements_Control", type=EndControl, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
members10: BinaryAssociation = BinaryAssociation(
    name="members10",
    ends={
        Property(name="Member", type=jcl_containers_JCLRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_containers_JCLRoot", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters11: BinaryAssociation = BinaryAssociation(
    name="parameters11",
    ends={
        Property(name="Parameter12", type=jcl_containers_JobUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_containers_JobUnit", type=Parameter_, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
accountInfos13: BinaryAssociation = BinaryAssociation(
    name="accountInfos13",
    ends={
        Property(name="Literal15", type=jcl_containers_JobUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_containers_JobUnit14", type=Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatements5: BinaryAssociation = BinaryAssociation(
    name="elseStatements5",
    ends={
        Property(name="Statement6", type=jcl_statements_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_statements_Condition", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
executes16: BinaryAssociation = BinaryAssociation(
    name="executes16",
    ends={
        Property(name="ExecuteProgram", type=jcl_containers_JobUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_containers_JobUnit17", type=ExecuteProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children18: BinaryAssociation = BinaryAssociation(
    name="children18",
    ends={
        Property(name="RelationalExpressionChild", type=jcl_expressions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_RelationalExpression", type=RelationalExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relationOperators19: BinaryAssociation = BinaryAssociation(
    name="relationOperators19",
    ends={
        Property(name="RelationOperator", type=jcl_expressions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_RelationalExpression20", type=RelationOperator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children21: BinaryAssociation = BinaryAssociation(
    name="children21",
    ends={
        Property(name="ConditionalOrExpressionChild", type=jcl_expressions_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_ConditionalOrExpression", type=ConditionalOrExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
orOperators22: BinaryAssociation = BinaryAssociation(
    name="orOperators22",
    ends={
        Property(name="Or", type=jcl_expressions_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_ConditionalOrExpression23", type=Or, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children24: BinaryAssociation = BinaryAssociation(
    name="children24",
    ends={
        Property(name="ConditionalAndExpressionChild", type=jcl_expressions_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_ConditionalAndExpression", type=ConditionalAndExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
andOperators25: BinaryAssociation = BinaryAssociation(
    name="andOperators25",
    ends={
        Property(name="And", type=jcl_expressions_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_ConditionalAndExpression26", type=And, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child27: BinaryAssociation = BinaryAssociation(
    name="child27",
    ends={
        Property(name="UnaryExpressionChild", type=jcl_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_UnaryExpression", type=UnaryExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator28: BinaryAssociation = BinaryAssociation(
    name="operator28",
    ends={
        Property(name="UnaryOperator", type=jcl_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_UnaryExpression29", type=UnaryOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression30: BinaryAssociation = BinaryAssociation(
    name="expression30",
    ends={
        Property(name="Expression31", type=jcl_expressions_NestedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_NestedExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
step32: BinaryAssociation = BinaryAssociation(
    name="step32",
    ends={
        Property(name="IdentifierReference", type=jcl_expressions_Abend, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_Abend", type=IdentifierReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
step33: BinaryAssociation = BinaryAssociation(
    name="step33",
    ends={
        Property(name="IdentifierReference34", type=jcl_expressions_Run, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_expressions_Run", type=IdentifierReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
next35: BinaryAssociation = BinaryAssociation(
    name="next35",
    ends={
        Property(name="Reference", type=jcl_references_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_references_Reference", type=Reference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target36: BinaryAssociation = BinaryAssociation(
    name="target36",
    ends={
        Property(name="ReferenceableElement", type=jcl_references_ElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_references_ElementReference", type=ReferenceableElement, multiplicity=Multiplicity(1, 1))
    }
)
conditions37: BinaryAssociation = BinaryAssociation(
    name="conditions37",
    ends={
        Property(name="Condition38", type=jcl_conditions_NestedCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_conditions_NestedCondition", type=Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
returnCode41: BinaryAssociation = BinaryAssociation(
    name="returnCode41",
    ends={
        Property(name="ReturnCode", type=jcl_conditions_RelationalCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_conditions_RelationalCondition42", type=ReturnCode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
relationOperator39: BinaryAssociation = BinaryAssociation(
    name="relationOperator39",
    ends={
        Property(name="RelationOperator40", type=jcl_conditions_RelationalCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="jcl_conditions_RelationalCondition", type=RelationOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_jcl_parameters_Display_Parameter = Generalization(general=Parameter_, specific=jcl_parameters_Display)
gen_jcl_parameters_JobClass_Parameter = Generalization(general=Parameter_, specific=jcl_parameters_JobClass)
gen_jcl_parameters_MessageClass_Parameter = Generalization(general=Parameter_, specific=jcl_parameters_MessageClass)
gen_jcl_parameters_Password_Parameter = Generalization(general=Parameter_, specific=jcl_parameters_Password)
gen_jcl_parameters_Priority_Parameter = Generalization(general=Parameter_, specific=jcl_parameters_Priority)
gen_jcl_parameters_UserID_Parameter = Generalization(general=Parameter_, specific=jcl_parameters_UserID)
gen_jcl_parameters_MessageLevel_Parameter = Generalization(general=Parameter_, specific=jcl_parameters_MessageLevel)
gen_jcl_parameters_TypeRun_Parameter = Generalization(general=Parameter_, specific=jcl_parameters_TypeRun)
gen_jcl_parameters_AddressSpace_parameters_Parameter = Generalization(general=parameters_Parameter, specific=jcl_parameters_AddressSpace)
gen_jcl_parameters_AddressSpace_commons_ProcedureStepElement = Generalization(general=commons_ProcedureStepElement, specific=jcl_parameters_AddressSpace)
gen_jcl_parameters_Bytes_Parameter = Generalization(general=Parameter_, specific=jcl_parameters_Bytes)
gen_jcl_parameters_AccountInfo_parameters_Parameter = Generalization(general=parameters_Parameter, specific=jcl_parameters_AccountInfo)
gen_jcl_parameters_AccountInfo_commons_ProcedureStepElement = Generalization(general=commons_ProcedureStepElement, specific=jcl_parameters_AccountInfo)
gen_jcl_parameters_Argument_parameters_Parameter = Generalization(general=parameters_Parameter, specific=jcl_parameters_Argument)
gen_jcl_parameters_Argument_commons_ProcedureStepElement = Generalization(general=commons_ProcedureStepElement, specific=jcl_parameters_Argument)
gen_jcl_parameters_Condition_parameters_Parameter = Generalization(general=parameters_Parameter, specific=jcl_parameters_Condition)
gen_jcl_parameters_Condition_commons_ProcedureStepElement = Generalization(general=commons_ProcedureStepElement, specific=jcl_parameters_Condition)
gen_jcl_parameters_DatasetName_Parameter = Generalization(general=Parameter_, specific=jcl_parameters_DatasetName)
gen_jcl_parameters_Other_parameters_Parameter = Generalization(general=parameters_Parameter, specific=jcl_parameters_Other)
gen_jcl_parameters_Other_commons_NamedElement = Generalization(general=commons_NamedElement, specific=jcl_parameters_Other)
gen_jcl_parameters_Other_commons_ProcedureStepElement = Generalization(general=commons_ProcedureStepElement, specific=jcl_parameters_Other)
gen_jcl_statements_Statement_commons_NamedElement = Generalization(general=commons_NamedElement, specific=jcl_statements_Statement)
gen_jcl_statements_Statement_members_Member = Generalization(general=members_Member, specific=jcl_statements_Statement)
gen_jcl_statements_Execute_Statement = Generalization(general=Statement, specific=jcl_statements_Execute)
gen_jcl_statements_Condition_statements_StatementContainer = Generalization(general=statements_StatementContainer, specific=jcl_statements_Condition)
gen_jcl_statements_Condition_statements_Statement = Generalization(general=statements_Statement, specific=jcl_statements_Condition)
gen_jcl_statements_DataDefinition_statements_Statement = Generalization(general=statements_Statement, specific=jcl_statements_DataDefinition)
gen_jcl_statements_DataDefinition_commons_ProcedureStepElement = Generalization(general=commons_ProcedureStepElement, specific=jcl_statements_DataDefinition)
gen_jcl_statements_Set_Statement = Generalization(general=Statement, specific=jcl_statements_Set)
gen_jcl_statements_Input_Statement = Generalization(general=Statement, specific=jcl_statements_Input)
gen_jcl_statements_Output_Statement = Generalization(general=Statement, specific=jcl_statements_Output)
gen_jcl_statements_JCLLibrary_Statement = Generalization(general=Statement, specific=jcl_statements_JCLLibrary)
gen_jcl_statements_Control_Statement = Generalization(general=Statement, specific=jcl_statements_Control)
gen_jcl_statements_Include_Statement = Generalization(general=Statement, specific=jcl_statements_Include)
gen_jcl_statements_Command_Statement = Generalization(general=Statement, specific=jcl_statements_Command)
gen_jcl_statements_ExecuteProgram_Execute = Generalization(general=Execute, specific=jcl_statements_ExecuteProgram)
gen_jcl_statements_ExecuteProcedure_Execute = Generalization(general=Execute, specific=jcl_statements_ExecuteProcedure)
gen_jcl_statements_EndControl_Statement = Generalization(general=Statement, specific=jcl_statements_EndControl)
gen_jcl_containers_JobUnit_commons_NamedElement = Generalization(general=commons_NamedElement, specific=jcl_containers_JobUnit)
gen_jcl_containers_JobUnit_containers_JCLRoot = Generalization(general=containers_JCLRoot, specific=jcl_containers_JobUnit)
gen_jcl_containers_JobUnit_commons_IncompleteElement = Generalization(general=commons_IncompleteElement, specific=jcl_containers_JobUnit)
gen_jcl_expressions_RelationalExpression_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=jcl_expressions_RelationalExpression)
gen_jcl_expressions_ConditionalExpression_Expression = Generalization(general=Expression, specific=jcl_expressions_ConditionalExpression)
gen_jcl_expressions_ConditionalOrExpression_ConditionalExpression = Generalization(general=ConditionalExpression, specific=jcl_expressions_ConditionalOrExpression)
gen_jcl_expressions_ConditionalOrExpressionChild_ConditionalExpression = Generalization(general=ConditionalExpression, specific=jcl_expressions_ConditionalOrExpressionChild)
gen_jcl_expressions_ConditionalAndExpression_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=jcl_expressions_ConditionalAndExpression)
gen_jcl_expressions_ConditionalAndExpressionChild_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=jcl_expressions_ConditionalAndExpressionChild)
gen_jcl_expressions_RelationalExpressionChild_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=jcl_expressions_RelationalExpressionChild)
gen_jcl_expressions_UnaryExpressionChild_RelationalExpressionChild = Generalization(general=RelationalExpressionChild, specific=jcl_expressions_UnaryExpressionChild)
gen_jcl_expressions_UnaryExpression_RelationalExpressionChild = Generalization(general=RelationalExpressionChild, specific=jcl_expressions_UnaryExpression)
gen_jcl_expressions_NestedExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=jcl_expressions_NestedExpression)
gen_jcl_expressions_PrimaryExpression_UnaryExpressionChild = Generalization(general=UnaryExpressionChild, specific=jcl_expressions_PrimaryExpression)
gen_jcl_expressions_Abend_expressions_PrimaryExpression = Generalization(general=expressions_PrimaryExpression, specific=jcl_expressions_Abend)
gen_jcl_expressions_Abend_commons_ProcedureStepElement = Generalization(general=commons_ProcedureStepElement, specific=jcl_expressions_Abend)
gen_jcl_expressions_Run_expressions_PrimaryExpression = Generalization(general=expressions_PrimaryExpression, specific=jcl_expressions_Run)
gen_jcl_expressions_Run_commons_ProcedureStepElement = Generalization(general=commons_ProcedureStepElement, specific=jcl_expressions_Run)
gen_jcl_operators_Operator_PhraseableElement = Generalization(general=PhraseableElement, specific=jcl_operators_Operator)
gen_jcl_operators_GreaterThan_RelationOperator = Generalization(general=RelationOperator, specific=jcl_operators_GreaterThan)
gen_jcl_operators_GreaterEqual_RelationOperator = Generalization(general=RelationOperator, specific=jcl_operators_GreaterEqual)
gen_jcl_operators_Equal_RelationOperator = Generalization(general=RelationOperator, specific=jcl_operators_Equal)
gen_jcl_operators_LessThan_RelationOperator = Generalization(general=RelationOperator, specific=jcl_operators_LessThan)
gen_jcl_operators_LessEqual_RelationOperator = Generalization(general=RelationOperator, specific=jcl_operators_LessEqual)
gen_jcl_operators_NotEqual_RelationOperator = Generalization(general=RelationOperator, specific=jcl_operators_NotEqual)
gen_jcl_operators_UnaryOperator_Operator = Generalization(general=Operator, specific=jcl_operators_UnaryOperator)
gen_jcl_operators_RelationOperator_Operator = Generalization(general=Operator, specific=jcl_operators_RelationOperator)
gen_jcl_operators_Negate_UnaryOperator = Generalization(general=UnaryOperator, specific=jcl_operators_Negate)
gen_jcl_operators_LogicOperator_Operator = Generalization(general=Operator, specific=jcl_operators_LogicOperator)
gen_jcl_operators_And_LogicOperator = Generalization(general=LogicOperator, specific=jcl_operators_And)
gen_jcl_literals_IntegerLiteral_literals_Literal = Generalization(general=literals_Literal, specific=jcl_literals_IntegerLiteral)
gen_jcl_literals_IntegerLiteral_expressions_PrimaryExpression = Generalization(general=expressions_PrimaryExpression, specific=jcl_literals_IntegerLiteral)
gen_jcl_literals_IntegerLiteral_conditions_ReturnCode = Generalization(general=conditions_ReturnCode, specific=jcl_literals_IntegerLiteral)
gen_jcl_literals_StringLiteral_Literal = Generalization(general=Literal, specific=jcl_literals_StringLiteral)
gen_jcl_literals_SpecialLiteral_Literal = Generalization(general=Literal, specific=jcl_literals_SpecialLiteral)
gen_jcl_references_ElementReference_Reference = Generalization(general=Reference, specific=jcl_references_ElementReference)
gen_jcl_operators_Or_LogicOperator = Generalization(general=LogicOperator, specific=jcl_operators_Or)
gen_jcl_references_IdentifierReference_references_ElementReference = Generalization(general=references_ElementReference, specific=jcl_references_IdentifierReference)
gen_jcl_references_IdentifierReference_expressions_PrimaryExpression = Generalization(general=expressions_PrimaryExpression, specific=jcl_references_IdentifierReference)
gen_jcl_conditions_Even_PrimaryCondition = Generalization(general=PrimaryCondition, specific=jcl_conditions_Even)
gen_jcl_conditions_Only_PrimaryCondition = Generalization(general=PrimaryCondition, specific=jcl_conditions_Only)
gen_jcl_conditions_PrimaryCondition_Condition = Generalization(general=Condition, specific=jcl_conditions_PrimaryCondition)
gen_jcl_conditions_NestedCondition_PrimaryCondition = Generalization(general=PrimaryCondition, specific=jcl_conditions_NestedCondition)
gen_jcl_conditions_RelationalCondition_conditions_PrimaryCondition = Generalization(general=conditions_PrimaryCondition, specific=jcl_conditions_RelationalCondition)
gen_jcl_conditions_RelationalCondition_references_ElementReference = Generalization(general=references_ElementReference, specific=jcl_conditions_RelationalCondition)
gen_jcl_references_IdentifierReference_conditions_ReturnCode = Generalization(general=conditions_ReturnCode, specific=jcl_references_IdentifierReference)
gen_jcl_procedures_Procedure_containers_JCLRoot = Generalization(general=containers_JCLRoot, specific=jcl_procedures_Procedure)
gen_jcl_procedures_Procedure_commons_NamedElement = Generalization(general=commons_NamedElement, specific=jcl_procedures_Procedure)
gen_jcl_procedures_Procedure_members_Member = Generalization(general=members_Member, specific=jcl_procedures_Procedure)

# Domain Model
domain_model = DomainModel(
    name="jcl",
    types={jcl_commons_NamedElement, jcl_commons_PhraseableElement, jcl_commons_CommentableElement, jcl_commons_IncompleteElement, Water, jcl_parameters_Parameter, jcl_parameters_Display, Parameter_, jcl_parameters_JobClass, jcl_parameters_MessageClass, jcl_parameters_Password, jcl_parameters_Priority, jcl_parameters_UserID, jcl_parameters_MessageLevel, jcl_parameters_TypeRun, jcl_parameters_AddressSpace, parameters_Parameter, commons_ProcedureStepElement, jcl_commons_ProcedureStepElement, jcl_parameters_Bytes, jcl_parameters_AccountInfo, Literal, jcl_parameters_Argument, jcl_parameters_Condition, Condition, jcl_parameters_DatasetName, jcl_parameters_Other, commons_NamedElement, jcl_statements_Statement, members_Member, jcl_statements_Execute, Statement, jcl_statements_StatementContainer, jcl_statements_Condition, statements_StatementContainer, statements_Statement, jcl_statements_DataDefinition, jcl_statements_Set, jcl_statements_Input, jcl_statements_Output, jcl_statements_JCLLibrary, jcl_statements_Control, EndControl, jcl_statements_Include, jcl_statements_Command, jcl_statements_ExecuteProgram, Execute, jcl_statements_ExecuteProcedure, jcl_statements_EndControl, jcl_containers_JCLRoot, Member, jcl_containers_JobUnit, containers_JCLRoot, commons_IncompleteElement, ExecuteProgram, jcl_expressions_Expression, Expression, jcl_expressions_RelationalExpression, ConditionalAndExpressionChild, RelationalExpressionChild, RelationOperator, jcl_expressions_ConditionalExpression, jcl_expressions_ConditionalOrExpression, ConditionalExpression, ConditionalOrExpressionChild, Or, jcl_expressions_ConditionalOrExpressionChild, jcl_expressions_ConditionalAndExpression, And, jcl_expressions_ConditionalAndExpressionChild, jcl_expressions_RelationalExpressionChild, jcl_expressions_UnaryExpressionChild, jcl_expressions_UnaryExpression, UnaryExpressionChild, UnaryOperator, jcl_expressions_NestedExpression, PrimaryExpression, jcl_expressions_PrimaryExpression, jcl_expressions_Abend, expressions_PrimaryExpression, IdentifierReference, jcl_expressions_Run, jcl_operators_Operator, PhraseableElement, jcl_operators_GreaterThan, jcl_operators_GreaterEqual, jcl_operators_Equal, jcl_operators_LessThan, jcl_operators_LessEqual, jcl_operators_NotEqual, jcl_operators_UnaryOperator, Operator, jcl_operators_RelationOperator, jcl_operators_Negate, jcl_operators_LogicOperator, jcl_operators_And, LogicOperator, jcl_literals_Literal, jcl_literals_IntegerLiteral, literals_Literal, conditions_ReturnCode, jcl_literals_StringLiteral, jcl_literals_SpecialLiteral, jcl_references_Reference, Reference, jcl_references_ElementReference, ReferenceableElement, jcl_references_IdentifierReference, jcl_operators_Or, references_ElementReference, jcl_references_ReferenceableElement, jcl_conditions_Condition, jcl_conditions_Even, PrimaryCondition, jcl_conditions_Only, jcl_conditions_PrimaryCondition, jcl_conditions_NestedCondition, jcl_conditions_RelationalCondition, conditions_PrimaryCondition, ReturnCode, jcl_conditions_ReturnCode, jcl_procedures_Procedure, jcl_members_Member, jcl_waters_Water, AdressSpaceEnum, TypeRunEnum},
    associations={waters0, values1, condition2, parameters3, statements4, condition7, endControl9, members10, parameters11, accountInfos13, elseStatements5, executes16, children18, relationOperators19, children21, orOperators22, children24, andOperators25, child27, operator28, expression30, step32, step33, next35, target36, conditions37, returnCode41, relationOperator39},
    generalizations={gen_jcl_parameters_Display_Parameter, gen_jcl_parameters_JobClass_Parameter, gen_jcl_parameters_MessageClass_Parameter, gen_jcl_parameters_Password_Parameter, gen_jcl_parameters_Priority_Parameter, gen_jcl_parameters_UserID_Parameter, gen_jcl_parameters_MessageLevel_Parameter, gen_jcl_parameters_TypeRun_Parameter, gen_jcl_parameters_AddressSpace_parameters_Parameter, gen_jcl_parameters_AddressSpace_commons_ProcedureStepElement, gen_jcl_parameters_Bytes_Parameter, gen_jcl_parameters_AccountInfo_parameters_Parameter, gen_jcl_parameters_AccountInfo_commons_ProcedureStepElement, gen_jcl_parameters_Argument_parameters_Parameter, gen_jcl_parameters_Argument_commons_ProcedureStepElement, gen_jcl_parameters_Condition_parameters_Parameter, gen_jcl_parameters_Condition_commons_ProcedureStepElement, gen_jcl_parameters_DatasetName_Parameter, gen_jcl_parameters_Other_parameters_Parameter, gen_jcl_parameters_Other_commons_NamedElement, gen_jcl_parameters_Other_commons_ProcedureStepElement, gen_jcl_statements_Statement_commons_NamedElement, gen_jcl_statements_Statement_members_Member, gen_jcl_statements_Execute_Statement, gen_jcl_statements_Condition_statements_StatementContainer, gen_jcl_statements_Condition_statements_Statement, gen_jcl_statements_DataDefinition_statements_Statement, gen_jcl_statements_DataDefinition_commons_ProcedureStepElement, gen_jcl_statements_Set_Statement, gen_jcl_statements_Input_Statement, gen_jcl_statements_Output_Statement, gen_jcl_statements_JCLLibrary_Statement, gen_jcl_statements_Control_Statement, gen_jcl_statements_Include_Statement, gen_jcl_statements_Command_Statement, gen_jcl_statements_ExecuteProgram_Execute, gen_jcl_statements_ExecuteProcedure_Execute, gen_jcl_statements_EndControl_Statement, gen_jcl_containers_JobUnit_commons_NamedElement, gen_jcl_containers_JobUnit_containers_JCLRoot, gen_jcl_containers_JobUnit_commons_IncompleteElement, gen_jcl_expressions_RelationalExpression_ConditionalAndExpressionChild, gen_jcl_expressions_ConditionalExpression_Expression, gen_jcl_expressions_ConditionalOrExpression_ConditionalExpression, gen_jcl_expressions_ConditionalOrExpressionChild_ConditionalExpression, gen_jcl_expressions_ConditionalAndExpression_ConditionalOrExpressionChild, gen_jcl_expressions_ConditionalAndExpressionChild_ConditionalOrExpressionChild, gen_jcl_expressions_RelationalExpressionChild_ConditionalAndExpressionChild, gen_jcl_expressions_UnaryExpressionChild_RelationalExpressionChild, gen_jcl_expressions_UnaryExpression_RelationalExpressionChild, gen_jcl_expressions_NestedExpression_PrimaryExpression, gen_jcl_expressions_PrimaryExpression_UnaryExpressionChild, gen_jcl_expressions_Abend_expressions_PrimaryExpression, gen_jcl_expressions_Abend_commons_ProcedureStepElement, gen_jcl_expressions_Run_expressions_PrimaryExpression, gen_jcl_expressions_Run_commons_ProcedureStepElement, gen_jcl_operators_Operator_PhraseableElement, gen_jcl_operators_GreaterThan_RelationOperator, gen_jcl_operators_GreaterEqual_RelationOperator, gen_jcl_operators_Equal_RelationOperator, gen_jcl_operators_LessThan_RelationOperator, gen_jcl_operators_LessEqual_RelationOperator, gen_jcl_operators_NotEqual_RelationOperator, gen_jcl_operators_UnaryOperator_Operator, gen_jcl_operators_RelationOperator_Operator, gen_jcl_operators_Negate_UnaryOperator, gen_jcl_operators_LogicOperator_Operator, gen_jcl_operators_And_LogicOperator, gen_jcl_literals_IntegerLiteral_literals_Literal, gen_jcl_literals_IntegerLiteral_expressions_PrimaryExpression, gen_jcl_literals_IntegerLiteral_conditions_ReturnCode, gen_jcl_literals_StringLiteral_Literal, gen_jcl_literals_SpecialLiteral_Literal, gen_jcl_references_ElementReference_Reference, gen_jcl_operators_Or_LogicOperator, gen_jcl_references_IdentifierReference_references_ElementReference, gen_jcl_references_IdentifierReference_expressions_PrimaryExpression, gen_jcl_conditions_Even_PrimaryCondition, gen_jcl_conditions_Only_PrimaryCondition, gen_jcl_conditions_PrimaryCondition_Condition, gen_jcl_conditions_NestedCondition_PrimaryCondition, gen_jcl_conditions_RelationalCondition_conditions_PrimaryCondition, gen_jcl_conditions_RelationalCondition_references_ElementReference, gen_jcl_references_IdentifierReference_conditions_ReturnCode, gen_jcl_procedures_Procedure_containers_JCLRoot, gen_jcl_procedures_Procedure_commons_NamedElement, gen_jcl_procedures_Procedure_members_Member},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)