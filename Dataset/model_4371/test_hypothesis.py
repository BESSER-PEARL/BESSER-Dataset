import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    strings_Occurrence,
    strings_Tallying,
    cobol_strings_TallyingOccurrence,
    cobol_strings_Occurrence,
    cobol_strings_Location,
    ManipulatedStrings,
    cobol_strings_SplittedString,
    cobol_strings_ConcatenatingStrings,
    cobol_strings_String,
    Location,
    String,
    cobol_strings_ManipulatedStrings,
    cobol_strings_StringManipulation,
    StringManipulation,
    cobol_strings_Replacement,
    cobol_strings_Tallying,
    strings_Replacement,
    cobol_strings_ReplacementOccurrence,
    NotErrorHandler,
    cobol_handlers_NotOnOverflow,
    cobol_handlers_NotAtEnd,
    cobol_handlers_NotInvalidKey,
    cobol_handlers_NotOnException,
    cobol_handlers_NotOnSizeError,
    cobol_functions_Argumentable,
    Argument,
    cobol_functions_ByContentArgument,
    cobol_functions_ByValueArgument,
    cobol_functions_OmittedArgument,
    cobol_functions_ByReferenceArgument,
    cobol_functions_Argument,
    cobol_labels_Label,
    cobol_labels_Procedure,
    Procedure,
    cobol_handlers_NotAtEndOfPage,
    ProcedureRangeChild,
    cobol_verbs_Verb,
    Verb,
    cobol_verbs_Is,
    DeclarativeSection,
    cobol_declaratives_Declaratives,
    cobol_labels_ProcedureLabel,
    cobol_files_FileStatus,
    FileStatus,
    cobol_tables_TableDimension,
    AdditionalIndexName,
    Parameter,
    cobol_parameters_ByReferenceParameter,
    cobol_parameters_ByValueParameter,
    cobol_parameters_Parametrizable,
    IndexName,
    TableDimension,
    dataitems_DataItem,
    cobol_specialnames_SpecialNameStatement,
    AlphabetNameReference,
    SymbolicCharacter,
    SpecialName,
    cobol_specialnames_SymbolicCharacter,
    cobol_specialnames_MnemonicName,
    cobol_tables_KeyName,
    KeyName,
    cobol_specialnames_AlphabetType,
    specialnames_MnemonicName,
    AlphabetType,
    cobol_specialnames_PredefinedAlphabetType,
    cobol_specialnames_CodeNameAlphabetType,
    specialnames_SpecialNameStatement,
    cobol_specialnames_SystemDeviceIs,
    cobol_specialnames_UPSISwitchIs,
    ConditionName,
    cobol_specialnames_OffStatus,
    cobol_specialnames_OnStatus,
    specialnames_SpecialName,
    cobol_specialnames_CurrencySign,
    cobol_specialnames_AlphabetName,
    cobol_specialnames_ClassName,
    cobol_specialnames_ExplicitAlphabetType,
    references_ReferenceableElement,
    cobol_dataitems_DataItemAttribute,
    RangeExpression,
    DataName,
    cobol_dataitems_RenamingDataName,
    DataItemAttribute,
    cobol_dataitems_GroupUsage,
    cobol_dataitems_Redefines,
    cobol_dataitems_Value,
    cobol_dataitems_Global,
    cobol_dataitems_External,
    cobol_dataitems_Usage,
    cobol_dataitems_PictureString,
    SystemDevice,
    cobol_environments_SystemPunchDevice,
    cobol_environments_AdvancedFunctionPrinting,
    cobol_environments_SuppressSpacing,
    cobol_environments_Console,
    cobol_environments_SystemLogicalOutput,
    cobol_environments_Pocket,
    cobol_environments_Channel,
    cobol_environments_SystemLogicalInput,
    Register,
    cobol_registers_ShiftOut,
    cobol_registers_AddressOf,
    cobol_registers_LengthOf,
    cobol_registers_WhenCompiled,
    cobol_registers_ReturnCode,
    cobol_registers_ShiftIn,
    SortPhraseWater,
    cobol_water_SortPhraseToken,
    OpenStatementWater,
    cobol_water_OpenStatementToken,
    InvokeStatementWater,
    cobol_water_InvokeStatementToken,
    CloseStatementWater,
    cobol_water_CloseStatementToken,
    UseStatementWater,
    cobol_water_UseStatementToken,
    AcceptStatementWater,
    cobol_environments_Environment,
    cobol_water_AcceptStatementToken,
    CICSStatementWater,
    cobol_water_CICSStatementToken,
    SQLStatementWater,
    cobol_water_SQLStatementToken,
    RepositoryParagraphWater,
    cobol_water_RepositoryDescription,
    IOControlParagraphWater,
    cobol_water_IOControlDescription,
    DataDescriptorWater,
    cobol_water_DataDescription,
    FileDescriptorWater,
    cobol_water_FileDescription,
    SelectStatementWater,
    cobol_water_SelectStatementClause,
    ObjectComputerParagraphWater,
    cobol_water_PriorityNumber,
    cobol_water_ObjectComputerDescription,
    cobol_water_Water,
    Water,
    cobol_water_CloseStatementWater,
    cobol_water_FileDescriptorWater,
    cobol_water_InvokeStatementWater,
    cobol_water_DataDescriptorWater,
    cobol_water_SelectStatementWater,
    cobol_water_SQLStatementWater,
    cobol_water_AcceptStatementWater,
    cobol_water_IdentificationDivisionWater,
    cobol_water_UseStatementWater,
    cobol_water_IOControlParagraphWater,
    cobol_water_SpecialNamesParagraphWater,
    cobol_water_ObjectComputerParagraphWater,
    cobol_water_OpenStatementWater,
    cobol_water_CICSStatementWater,
    cobol_water_SortPhraseWater,
    cobol_water_RepositoryParagraphWater,
    cobol_water_IncompleteElement,
    Label,
    cobol_labels_ProcedureRangeLabel,
    cobol_labels_StopLabel,
    cobol_ios_IODirectives,
    ios_OutputDirective,
    ios_FileDirective,
    cobol_ios_OutputFile,
    IODirectives,
    cobol_ios_OutputDirective,
    cobol_ios_FileDirective,
    cobol_ios_ProcedureDirective,
    cobol_ios_InputDirective,
    ios_ProcedureDirective,
    cobol_ios_OutputProcedure,
    ios_InputDirective,
    cobol_ios_InputFile,
    cobol_ios_InputProcedure,
    cobol_identifiers_ReferenceModifier,
    DirectSubscript,
    cobol_identifiers_All,
    IdentificationDivisionWater,
    cobol_water_ProgramDescription,
    Subscript,
    cobol_identifiers_RelativeSubscript,
    cobol_identifiers_DirectSubscript,
    identifiers_Identifier,
    ReferenceModifier,
    water_SortPhraseWater,
    water_DataDescriptorWater,
    statements_Statement,
    water_UseStatementWater,
    DataItem,
    cobol_dataitems_ConditionName,
    cobol_dataitems_RecordName,
    cobol_dataitems_DataName,
    Statement,
    EnvironmentDivisionSection,
    cobol_sections_ConfigurationSection,
    cobol_sections_IOSection,
    ArithmeticOperand,
    cobol_operands_RoundedIdentifier,
    water_SQLStatementWater,
    water_IdentificationDivisionWater,
    cobol_water_Dot,
    water_RepositoryParagraphWater,
    water_AcceptStatementWater,
    cobol_identifiers_Subscript,
    VaryingUntilCondition,
    cobol_statements_AfterUntilCondition,
    Qualifier,
    Conditional,
    cobol_statements_VaryingUntilCondition,
    Tallying,
    cobol_strings_AnyCharacter,
    cobol_strings_SpecificCharacter,
    cobol_statements_TallyingIn,
    IncompleteElement,
    cobol_files_SelectStatement,
    cobol_statements_IOFile,
    IOFile,
    cobol_statements_IOFileDescriptor,
    IOFileDescriptor,
    cobol_statements_IOStatement,
    cobol_statements_KeyDescriptor,
    statements_VaryingUntilCondition,
    cobol_statements_Release,
    statements_PerformFixedTimes,
    statements_FileIOStatement,
    KeyDescriptor,
    OutputDirective,
    InputDirective,
    statements_PerformProcedure,
    cobol_statements_PerformProcedureFixedTimes,
    cobol_statements_FileIOStatement,
    statements_PerformNestedStatement,
    cobol_statements_PerformNestedStatementFixedTimes,
    AfterUntilCondition,
    statements_PerformUntilCondition,
    cobol_statements_PerformNestedStatementUntilCondition,
    cobol_statements_PerformProcedureUntilCondition,
    TallyingIn,
    cobol_statements_SwitchStatus,
    Write,
    cobol_statements_Rewrite,
    MnemonicNameReference,
    IntegerLiteral,
    SearchStatement,
    cobol_statements_BinarySearch,
    cobol_statements_SerialSearch,
    NormalEvaluateCase,
    Replacement,
    cobol_strings_AnyCharacterBySpecificCharacter,
    cobol_strings_SpecificCharacterBySpecificCharacter,
    cobol_statements_Initialize,
    cobol_statements_Inspect,
    cobol_statements_Replace,
    NestedStatement,
    cobol_handlers_Handler,
    cobol_statements_EvaluateCase,
    ExpressionList,
    EvaluateCase,
    cobol_statements_OtherEvaluateCase,
    cobol_statements_NormalEvaluateCase,
    cobol_statements_Evaluate,
    SplittedString,
    SetStatement,
    cobol_statements_Set,
    cobol_statements_SetSwitches,
    cobol_statements_SetStatement,
    FileNameReference,
    Handler,
    cobol_handlers_OnException,
    cobol_handlers_AtEndOfPage,
    cobol_handlers_OnSizeError,
    cobol_handlers_AtEnd,
    cobol_handlers_NotErrorHandler,
    cobol_handlers_InvalidKey,
    cobol_handlers_OnOverflow,
    cobol_statements_ErrorHandled,
    cobol_statements_Execute,
    functions_Argumentable,
    cobol_statements_Cancel,
    statements_IOStatement,
    ConcatenatingStrings,
    IndexNameReference,
    cobol_statements_SetIndexName,
    SwitchStatus,
    PrimaryOperand,
    cobol_registers_Register,
    cobol_statements_Move,
    cobol_statements_NestedStatement,
    Jump,
    cobol_statements_GoTo,
    cobol_statements_GoBack,
    cobol_statements_Continue,
    cobol_statements_NextSentence,
    cobol_statements_Jump,
    ProcedureRangeLabel,
    cobol_labels_ProcedureRange,
    cobol_labels_ProcedureRangeChild,
    Perform,
    cobol_statements_PerformFixedTimes,
    cobol_statements_PerformProcedure,
    AssignmentExpression,
    Environment,
    cobol_environments_UPSI,
    cobol_environments_SystemDevice,
    cobol_statements_Display,
    StopLabel,
    cobol_labels_Run,
    cobol_statements_Stop,
    cobol_statements_Conditional,
    statements_Conditional,
    cobol_statements_Exit,
    cobol_statements_Statement,
    cobol_operands_Operand,
    ReplacementOperand,
    cobol_operands_Encoding,
    Operand,
    cobol_operands_ArithmeticOperand,
    cobol_operands_ReplacementOperand,
    Identifier,
    statements_NestedStatement,
    cobol_statements_Condition,
    statements_Perform,
    cobol_statements_PerformUntilCondition,
    cobol_statements_PerformNestedStatement,
    cobol_statements_Perform,
    ArithmeticStatement,
    cobol_statements_Divide,
    cobol_statements_Multiply,
    cobol_statements_Subtract,
    cobol_statements_Add,
    statements_ErrorHandled,
    cobol_statements_Return,
    cobol_statements_ArithmeticStatement,
    cobol_statements_Start,
    cobol_statements_SearchStatement,
    cobol_statements_Delete,
    cobol_statements_Read,
    cobol_statements_Unstring,
    cobol_statements_Write,
    cobol_statements_Call,
    cobol_statements_String,
    cobol_statements_Compute,
    ConstantLiteral,
    FigurativeConstantLiteral,
    cobol_literals_AllLiteral,
    DecimalLiteral,
    cobol_literals_FloatingDecimalLiteral,
    NumericLiteral,
    cobol_literals_DecimalLiteral,
    water_IOControlParagraphWater,
    water_FileDescriptorWater,
    water_ObjectComputerParagraphWater,
    literals_NumericLiteral,
    cobol_literals_IntegerLiteral,
    Literal,
    cobol_literals_FigurativeConstantLiteral,
    cobol_literals_BooleanLiteral,
    cobol_literals_AlphanumericLiteral,
    Division,
    cobol_divisions_EnvironmentDivision,
    cobol_divisions_DataDivision,
    StatementContainer,
    Paragraph,
    Section,
    cobol_sections_DataDivisionSection,
    cobol_sections_EnvironmentDivisionSection,
    CobolRoot,
    cobol_containers_EmptyModel,
    cobol_containers_CobolRoot,
    ProcedureDivision,
    DataDivision,
    EnvironmentDivision,
    water_InvokeStatementWater,
    operands_PrimaryOperand,
    water_CICSStatementWater,
    water_SpecialNamesParagraphWater,
    water_SelectStatementWater,
    cobol_identifiers_Identifier,
    Declaratives,
    parameters_Parametrizable,
    cobol_statements_Entry,
    water_IncompleteElement,
    cobol_files_FileName,
    cobol_statements_Merge,
    cobol_statements_Accept,
    cobol_tables_Table,
    cobol_statements_Sort,
    cobol_statements_Close,
    cobol_statements_Open,
    cobol_dataitems_DataItem,
    divisions_Division,
    cobol_divisions_ProcedureDivision,
    cobol_divisions_IdentificationDivision,
    ArithmeticExpression,
    cobol_arithmetics_RangeExpression,
    Equal,
    cobol_arithmetics_AssignmentExpression,
    UnaryOperator,
    UnaryArithmeticExpressionChild,
    cobol_arithmetics_PrimaryExpression,
    PowerArithmeticExpressionChild,
    cobol_arithmetics_UnaryArithmeticExpression,
    cobol_arithmetics_UnaryArithmeticExpressionChild,
    IdentificationDivision,
    NamedElement,
    cobol_divisions_Division,
    cobol_containers_CompilationUnit,
    CompilationUnit,
    commons_NamedElement,
    cobol_specialnames_ConditionName,
    cobol_functions_FunctionCall,
    cobol_tables_IndexName,
    containers_CobolRoot,
    cobol_containers_CompilationGroup,
    conditions_SimpleConditionChild,
    conditions_AbbreviatedRelationalExpressionChild,
    cobol_arithmetics_ArithmeticExpression,
    PrimaryExpression,
    cobol_arithmetics_NestedArithmeticExpression,
    cobol_arithmetics_RangeExpressionChild,
    Through,
    ClassOperator,
    SignOperator,
    MultiplicativeOperator,
    MultiplicativeArithmeticExpressionChild,
    cobol_arithmetics_PowerArithmeticExpression,
    cobol_arithmetics_PowerArithmeticExpressionChild,
    AdditiveOperator,
    AdditiveArithmeticExpressionChild,
    cobol_arithmetics_MultiplicativeArithmeticExpression,
    cobol_arithmetics_MultiplicativeArithmeticExpressionChild,
    RangeExpressionChild,
    cobol_arithmetics_AdditiveArithmeticExpressionChild,
    cobol_arithmetics_AdditiveArithmeticExpression,
    NegatedAbbreviatedConditionalExpressionChild,
    cobol_conditions_AbbreviatedRelationalExpressionChild,
    AbbreviatedConditionalExpressionChild,
    cobol_conditions_NegatedAbbreviatedConditionalExpression,
    cobol_conditions_ExpressionList,
    AbbreviatedRelationalExpressionChild,
    cobol_conditions_NestedAbbreviatedConditionalExpression,
    cobol_conditions_AbbreviatedRelationalExpression,
    cobol_conditions_NegatedAbbreviatedConditionalExpressionChild,
    NegatedConditionalExpressionChild,
    cobol_conditions_ClassCondition,
    cobol_conditions_SignCondition,
    ConditionalAndExpressionChild,
    cobol_conditions_AbbreviatedConditionalExpressionChild,
    cobol_conditions_AbbreviatedConditionalExpression,
    cobol_conditions_NegatedConditionalExpression,
    LogicalOperator,
    ConditionalOrExpressionChild,
    cobol_conditions_ConditionalAndExpression,
    cobol_conditions_ConditionalAndExpressionChild,
    Condition,
    cobol_conditions_ConditionalOrExpressionChild,
    cobol_conditions_ConditionalOrExpression,
    cobol_conditions_Condition,
    Is,
    RelationalOperator,
    SimpleConditionChild,
    cobol_conditions_NestedCondition,
    cobol_conditions_RelationalExpression,
    cobol_conditions_SimpleConditionChild,
    cobol_conditions_NegatedConditionalExpressionChild,
    Negate,
    cobol_commons_Commentable,
    Commentable,
    cobol_commons_URIableElement,
    cobol_commons_LabellableElement,
    cobol_commons_NamedElement,
    DataDivisionSection,
    cobol_sections_LinkageStorageSection,
    cobol_sections_LocalStorageSection,
    cobol_sections_FileSection,
    cobol_sections_WorkingStorageSection,
    operands_ArithmeticOperand,
    arithmetics_PrimaryExpression,
    operands_Operand,
    operands_ReplacementOperand,
    cobol_operands_PrimaryOperand,
    cobol_sentences_Sentence,
    cobol_sentences_ExecuteSentence,
    sentences_StatementContainer,
    cobol_sentences_UseSentence,
    Sentence,
    cobol_sentences_ExitProcedure,
    cobol_sentences_EntrySentence,
    cobol_sentences_AlteredGoTo,
    cobol_sentences_EmptySentence,
    cobol_sentences_StatementContainer,
    cobol_sections_DeclarativeSection,
    FileName,
    Reference,
    cobol_references_ElementReference,
    ReferenceableElement,
    cobol_specialnames_SpecialName,
    cobol_parameters_Parameter,
    cobol_tables_AdditionalIndexName,
    cobol_references_ReferenceableElement,
    cobol_references_Reference,
    cobol_paragraphs_DebuggingMode,
    SpecialNamesParagraphWater,
    cobol_water_SpecialNamesClause,
    SpecialNameStatement,
    cobol_paragraphs_IOSectionParagraph,
    cobol_paragraphs_ConfigurationSectionParagraph,
    identifiers_IdentifierReference,
    cobol_references_Qualifiable,
    cobol_references_ConditionName,
    ElementReference,
    cobol_identifiers_Qualifier,
    cobol_references_AlphabetNameReference,
    IdentifierReference,
    cobol_references_IndexNameReference,
    references_IdentifierReferenceQualifier,
    cobol_references_DataNameReference,
    references_ConditionName,
    cobol_references_ConditionNameReference,
    references_Qualifiable,
    cobol_identifiers_LinageCounter,
    references_ElementReference,
    cobol_references_FileNameReference,
    cobol_specialnames_SymbolicCharacterStatement,
    cobol_identifiers_IdentifierReference,
    cobol_references_IdentifierReferenceQualifier,
    cobol_references_MnemonicNameReference,
    cobol_references_SpecialNamesConditionNameReference,
    GreaterThan,
    cobol_operators_GTPhrase,
    LessThanOrEqual,
    cobol_operators_LTEQSign,
    cobol_operators_LTEQPhrase,
    LessThan,
    cobol_operators_LTSign,
    cobol_operators_LTPhrase,
    cobol_operators_EqualSign,
    cobol_operators_EqualPhrase,
    cobol_operators_Kanji,
    cobol_operators_AlphabeticLower,
    cobol_operators_AlphabeticUpper,
    cobol_operators_Numeric,
    cobol_operators_DBCS,
    cobol_operators_Alphabetic,
    cobol_operators_ClassName,
    cobol_operators_Zero,
    paragraphs_IOSectionParagraph,
    cobol_paragraphs_IOControlParagraph,
    SelectStatement,
    IOSectionParagraph,
    cobol_paragraphs_FileControlParagraph,
    paragraphs_ConfigurationSectionParagraph,
    cobol_paragraphs_RepositoryParagraph,
    cobol_paragraphs_ObjectComputerParagraph,
    DebuggingMode,
    ConfigurationSectionParagraph,
    cobol_paragraphs_SpecialNamesParagraph,
    cobol_paragraphs_SourceComputerParagraph,
    labels_Procedure,
    cobol_sections_Section,
    cobol_paragraphs_Paragraph,
    GreaterThanOrEqual,
    cobol_operators_GTEQSign,
    cobol_operators_GTEQPhrase,
    cobol_operators_GTSign,
    operators_UnaryOperator,
    operators_AdditiveOperator,
    cobol_operators_Subtraction,
    cobol_operators_Addition,
    cobol_operators_Division,
    cobol_operators_Negative,
    cobol_operators_Positive,
    cobol_operators_Multiplication,
    cobol_operators_ConditionAnd,
    cobol_operators_ConditionOr,
    Operator,
    cobol_operators_LogicalOperator,
    cobol_operators_MultiplicativeOperator,
    cobol_operators_RelationalOperator,
    cobol_operators_UnaryOperator,
    cobol_operators_SignOperator,
    cobol_operators_AdditiveOperator,
    cobol_operators_Operator,
    AlphanumericLiteral,
    cobol_literals_AlphanumericHexaDecimalLiteral,
    cobol_operators_ClassOperator,
    cobol_operators_Through,
    cobol_operators_Negate,
    cobol_operators_Power,
    cobol_operators_Equal,
    cobol_operators_LessThanOrEqual,
    cobol_operators_LessThan,
    cobol_operators_GreaterThan,
    cobol_operators_GreaterThanOrEqual,
    cobol_literals_HighValue,
    cobol_literals_LowValue,
    cobol_literals_Quote,
    cobol_literals_Zero,
    cobol_literals_Null,
    cobol_literals_FixedDecimalLiteral,
    DBCSLiteral,
    cobol_literals_NationalHexLiteral,
    cobol_literals_NationalLiteral,
    cobol_literals_DBCSLiteral,
    cobol_literals_PseudoLiteral,
    cobol_literals_Characters,
    cobol_literals_Any,
    cobol_literals_Space,
    labels_StopLabel,
    cobol_literals_Literal,
    cobol_literals_ConstantLiteral,
    cobol_literals_NumericLiteral,
    DataDescriptionInfo,
    Channels,
    Zeroes,
    HighValues,
    Orders,
    EOP,
    RepositoryDescriptionInfo,
    ObjectComputerDescriptionInfo,
    SelectStatementClauses,
    Corresponding,
    SortingOrder,
    SystemOutputs,
    SpecialNamesClauses,
    LowValues,
    EncodingTypes,
    CloseStatementTokens,
    PredefinedAlphabetTypes,
    Nulls,
    Positions,
    FileDescriptionInfo,
    IOControlDescriptionInfo,
    PictureStringCharacters,
    Spaces,
    Status,
    Properties,
    InvokeStatementTokens,
    Selects,
    SystemPunchDevices,
    Quotes,
    Adjustings,
    SQLStatementTokens,
    Usages,
    ThroughPhrase,
    OpenStatementTokens,
    ExitLabels,
    UPSISwitches,
    Occurrences,
    SortPhraseTokens,
    ProgramDescriptionInfo,
    AcceptStatementTokens,
    FileDescriptors,
    SystemInputs,
    CICSStatementTokens,
    IOTypes,
    UseStatementTokens,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_strings_occurrence_is_not_abstract():
    assert not inspect.isabstract(strings_Occurrence)


def test_strings_occurrence_constructor_exists():
    assert callable(strings_Occurrence.__init__)


def test_strings_occurrence_constructor_args():
    sig = inspect.signature(strings_Occurrence.__init__)
    params = list(sig.parameters.keys())



def test_strings_tallying_is_not_abstract():
    assert not inspect.isabstract(strings_Tallying)


def test_strings_tallying_constructor_exists():
    assert callable(strings_Tallying.__init__)


def test_strings_tallying_constructor_args():
    sig = inspect.signature(strings_Tallying.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_tallyingoccurrence_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_TallyingOccurrence)


def test_cobol_strings_tallyingoccurrence_constructor_exists():
    assert callable(cobol_strings_TallyingOccurrence.__init__)


def test_cobol_strings_tallyingoccurrence_constructor_args():
    sig = inspect.signature(cobol_strings_TallyingOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_occurrence_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_Occurrence)


def test_cobol_strings_occurrence_constructor_exists():
    assert callable(cobol_strings_Occurrence.__init__)


def test_cobol_strings_occurrence_constructor_args():
    sig = inspect.signature(cobol_strings_Occurrence.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cobol_strings_occurrence_has_type():
    assert hasattr(cobol_strings_Occurrence, "type")
    descriptor = None
    for klass in cobol_strings_Occurrence.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cobol_strings_location_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_Location)


def test_cobol_strings_location_constructor_exists():
    assert callable(cobol_strings_Location.__init__)


def test_cobol_strings_location_constructor_args():
    sig = inspect.signature(cobol_strings_Location.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_cobol_strings_location_has_position():
    assert hasattr(cobol_strings_Location, "position")
    descriptor = None
    for klass in cobol_strings_Location.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_cobol_strings_location_has_initial():
    assert hasattr(cobol_strings_Location, "initial")
    descriptor = None
    for klass in cobol_strings_Location.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_manipulatedstrings_is_not_abstract():
    assert not inspect.isabstract(ManipulatedStrings)


def test_manipulatedstrings_constructor_exists():
    assert callable(ManipulatedStrings.__init__)


def test_manipulatedstrings_constructor_args():
    sig = inspect.signature(ManipulatedStrings.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_splittedstring_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_SplittedString)


def test_cobol_strings_splittedstring_constructor_exists():
    assert callable(cobol_strings_SplittedString.__init__)


def test_cobol_strings_splittedstring_constructor_args():
    sig = inspect.signature(cobol_strings_SplittedString.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_concatenatingstrings_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_ConcatenatingStrings)


def test_cobol_strings_concatenatingstrings_constructor_exists():
    assert callable(cobol_strings_ConcatenatingStrings.__init__)


def test_cobol_strings_concatenatingstrings_constructor_args():
    sig = inspect.signature(cobol_strings_ConcatenatingStrings.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_string_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_String)


def test_cobol_strings_string_constructor_exists():
    assert callable(cobol_strings_String.__init__)


def test_cobol_strings_string_constructor_args():
    sig = inspect.signature(cobol_strings_String.__init__)
    params = list(sig.parameters.keys())



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_string_is_not_abstract():
    assert not inspect.isabstract(String)


def test_string_constructor_exists():
    assert callable(String.__init__)


def test_string_constructor_args():
    sig = inspect.signature(String.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_manipulatedstrings_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_ManipulatedStrings)


def test_cobol_strings_manipulatedstrings_constructor_exists():
    assert callable(cobol_strings_ManipulatedStrings.__init__)


def test_cobol_strings_manipulatedstrings_constructor_args():
    sig = inspect.signature(cobol_strings_ManipulatedStrings.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_stringmanipulation_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_StringManipulation)


def test_cobol_strings_stringmanipulation_constructor_exists():
    assert callable(cobol_strings_StringManipulation.__init__)


def test_cobol_strings_stringmanipulation_constructor_args():
    sig = inspect.signature(cobol_strings_StringManipulation.__init__)
    params = list(sig.parameters.keys())



def test_stringmanipulation_is_not_abstract():
    assert not inspect.isabstract(StringManipulation)


def test_stringmanipulation_constructor_exists():
    assert callable(StringManipulation.__init__)


def test_stringmanipulation_constructor_args():
    sig = inspect.signature(StringManipulation.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_replacement_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_Replacement)


def test_cobol_strings_replacement_constructor_exists():
    assert callable(cobol_strings_Replacement.__init__)


def test_cobol_strings_replacement_constructor_args():
    sig = inspect.signature(cobol_strings_Replacement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_tallying_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_Tallying)


def test_cobol_strings_tallying_constructor_exists():
    assert callable(cobol_strings_Tallying.__init__)


def test_cobol_strings_tallying_constructor_args():
    sig = inspect.signature(cobol_strings_Tallying.__init__)
    params = list(sig.parameters.keys())



def test_strings_replacement_is_not_abstract():
    assert not inspect.isabstract(strings_Replacement)


def test_strings_replacement_constructor_exists():
    assert callable(strings_Replacement.__init__)


def test_strings_replacement_constructor_args():
    sig = inspect.signature(strings_Replacement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_replacementoccurrence_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_ReplacementOccurrence)


def test_cobol_strings_replacementoccurrence_constructor_exists():
    assert callable(cobol_strings_ReplacementOccurrence.__init__)


def test_cobol_strings_replacementoccurrence_constructor_args():
    sig = inspect.signature(cobol_strings_ReplacementOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_noterrorhandler_is_not_abstract():
    assert not inspect.isabstract(NotErrorHandler)


def test_noterrorhandler_constructor_exists():
    assert callable(NotErrorHandler.__init__)


def test_noterrorhandler_constructor_args():
    sig = inspect.signature(NotErrorHandler.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_notonoverflow_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_NotOnOverflow)


def test_cobol_handlers_notonoverflow_constructor_exists():
    assert callable(cobol_handlers_NotOnOverflow.__init__)


def test_cobol_handlers_notonoverflow_constructor_args():
    sig = inspect.signature(cobol_handlers_NotOnOverflow.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_notatend_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_NotAtEnd)


def test_cobol_handlers_notatend_constructor_exists():
    assert callable(cobol_handlers_NotAtEnd.__init__)


def test_cobol_handlers_notatend_constructor_args():
    sig = inspect.signature(cobol_handlers_NotAtEnd.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_notinvalidkey_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_NotInvalidKey)


def test_cobol_handlers_notinvalidkey_constructor_exists():
    assert callable(cobol_handlers_NotInvalidKey.__init__)


def test_cobol_handlers_notinvalidkey_constructor_args():
    sig = inspect.signature(cobol_handlers_NotInvalidKey.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_notonexception_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_NotOnException)


def test_cobol_handlers_notonexception_constructor_exists():
    assert callable(cobol_handlers_NotOnException.__init__)


def test_cobol_handlers_notonexception_constructor_args():
    sig = inspect.signature(cobol_handlers_NotOnException.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_notonsizeerror_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_NotOnSizeError)


def test_cobol_handlers_notonsizeerror_constructor_exists():
    assert callable(cobol_handlers_NotOnSizeError.__init__)


def test_cobol_handlers_notonsizeerror_constructor_args():
    sig = inspect.signature(cobol_handlers_NotOnSizeError.__init__)
    params = list(sig.parameters.keys())



def test_cobol_functions_argumentable_is_not_abstract():
    assert not inspect.isabstract(cobol_functions_Argumentable)


def test_cobol_functions_argumentable_constructor_exists():
    assert callable(cobol_functions_Argumentable.__init__)


def test_cobol_functions_argumentable_constructor_args():
    sig = inspect.signature(cobol_functions_Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_cobol_functions_bycontentargument_is_not_abstract():
    assert not inspect.isabstract(cobol_functions_ByContentArgument)


def test_cobol_functions_bycontentargument_constructor_exists():
    assert callable(cobol_functions_ByContentArgument.__init__)


def test_cobol_functions_bycontentargument_constructor_args():
    sig = inspect.signature(cobol_functions_ByContentArgument.__init__)
    params = list(sig.parameters.keys())



def test_cobol_functions_byvalueargument_is_not_abstract():
    assert not inspect.isabstract(cobol_functions_ByValueArgument)


def test_cobol_functions_byvalueargument_constructor_exists():
    assert callable(cobol_functions_ByValueArgument.__init__)


def test_cobol_functions_byvalueargument_constructor_args():
    sig = inspect.signature(cobol_functions_ByValueArgument.__init__)
    params = list(sig.parameters.keys())



def test_cobol_functions_omittedargument_is_not_abstract():
    assert not inspect.isabstract(cobol_functions_OmittedArgument)


def test_cobol_functions_omittedargument_constructor_exists():
    assert callable(cobol_functions_OmittedArgument.__init__)


def test_cobol_functions_omittedargument_constructor_args():
    sig = inspect.signature(cobol_functions_OmittedArgument.__init__)
    params = list(sig.parameters.keys())



def test_cobol_functions_byreferenceargument_is_not_abstract():
    assert not inspect.isabstract(cobol_functions_ByReferenceArgument)


def test_cobol_functions_byreferenceargument_constructor_exists():
    assert callable(cobol_functions_ByReferenceArgument.__init__)


def test_cobol_functions_byreferenceargument_constructor_args():
    sig = inspect.signature(cobol_functions_ByReferenceArgument.__init__)
    params = list(sig.parameters.keys())



def test_cobol_functions_argument_is_not_abstract():
    assert not inspect.isabstract(cobol_functions_Argument)


def test_cobol_functions_argument_constructor_exists():
    assert callable(cobol_functions_Argument.__init__)


def test_cobol_functions_argument_constructor_args():
    sig = inspect.signature(cobol_functions_Argument.__init__)
    params = list(sig.parameters.keys())



def test_cobol_labels_label_is_not_abstract():
    assert not inspect.isabstract(cobol_labels_Label)


def test_cobol_labels_label_constructor_exists():
    assert callable(cobol_labels_Label.__init__)


def test_cobol_labels_label_constructor_args():
    sig = inspect.signature(cobol_labels_Label.__init__)
    params = list(sig.parameters.keys())



def test_cobol_labels_procedure_is_not_abstract():
    assert not inspect.isabstract(cobol_labels_Procedure)


def test_cobol_labels_procedure_constructor_exists():
    assert callable(cobol_labels_Procedure.__init__)


def test_cobol_labels_procedure_constructor_args():
    sig = inspect.signature(cobol_labels_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_procedure_is_not_abstract():
    assert not inspect.isabstract(Procedure)


def test_procedure_constructor_exists():
    assert callable(Procedure.__init__)


def test_procedure_constructor_args():
    sig = inspect.signature(Procedure.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_notatendofpage_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_NotAtEndOfPage)


def test_cobol_handlers_notatendofpage_constructor_exists():
    assert callable(cobol_handlers_NotAtEndOfPage.__init__)


def test_cobol_handlers_notatendofpage_constructor_args():
    sig = inspect.signature(cobol_handlers_NotAtEndOfPage.__init__)
    params = list(sig.parameters.keys())



def test_procedurerangechild_is_not_abstract():
    assert not inspect.isabstract(ProcedureRangeChild)


def test_procedurerangechild_constructor_exists():
    assert callable(ProcedureRangeChild.__init__)


def test_procedurerangechild_constructor_args():
    sig = inspect.signature(ProcedureRangeChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_verbs_verb_is_not_abstract():
    assert not inspect.isabstract(cobol_verbs_Verb)


def test_cobol_verbs_verb_constructor_exists():
    assert callable(cobol_verbs_Verb.__init__)


def test_cobol_verbs_verb_constructor_args():
    sig = inspect.signature(cobol_verbs_Verb.__init__)
    params = list(sig.parameters.keys())



def test_verb_is_not_abstract():
    assert not inspect.isabstract(Verb)


def test_verb_constructor_exists():
    assert callable(Verb.__init__)


def test_verb_constructor_args():
    sig = inspect.signature(Verb.__init__)
    params = list(sig.parameters.keys())



def test_cobol_verbs_is_is_not_abstract():
    assert not inspect.isabstract(cobol_verbs_Is)


def test_cobol_verbs_is_constructor_exists():
    assert callable(cobol_verbs_Is.__init__)


def test_cobol_verbs_is_constructor_args():
    sig = inspect.signature(cobol_verbs_Is.__init__)
    params = list(sig.parameters.keys())



def test_declarativesection_is_not_abstract():
    assert not inspect.isabstract(DeclarativeSection)


def test_declarativesection_constructor_exists():
    assert callable(DeclarativeSection.__init__)


def test_declarativesection_constructor_args():
    sig = inspect.signature(DeclarativeSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol_declaratives_declaratives_is_not_abstract():
    assert not inspect.isabstract(cobol_declaratives_Declaratives)


def test_cobol_declaratives_declaratives_constructor_exists():
    assert callable(cobol_declaratives_Declaratives.__init__)


def test_cobol_declaratives_declaratives_constructor_args():
    sig = inspect.signature(cobol_declaratives_Declaratives.__init__)
    params = list(sig.parameters.keys())



def test_cobol_labels_procedurelabel_is_not_abstract():
    assert not inspect.isabstract(cobol_labels_ProcedureLabel)


def test_cobol_labels_procedurelabel_constructor_exists():
    assert callable(cobol_labels_ProcedureLabel.__init__)


def test_cobol_labels_procedurelabel_constructor_args():
    sig = inspect.signature(cobol_labels_ProcedureLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol_files_filestatus_is_not_abstract():
    assert not inspect.isabstract(cobol_files_FileStatus)


def test_cobol_files_filestatus_constructor_exists():
    assert callable(cobol_files_FileStatus.__init__)


def test_cobol_files_filestatus_constructor_args():
    sig = inspect.signature(cobol_files_FileStatus.__init__)
    params = list(sig.parameters.keys())



def test_filestatus_is_not_abstract():
    assert not inspect.isabstract(FileStatus)


def test_filestatus_constructor_exists():
    assert callable(FileStatus.__init__)


def test_filestatus_constructor_args():
    sig = inspect.signature(FileStatus.__init__)
    params = list(sig.parameters.keys())



def test_cobol_tables_tabledimension_is_not_abstract():
    assert not inspect.isabstract(cobol_tables_TableDimension)


def test_cobol_tables_tabledimension_constructor_exists():
    assert callable(cobol_tables_TableDimension.__init__)


def test_cobol_tables_tabledimension_constructor_args():
    sig = inspect.signature(cobol_tables_TableDimension.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_tables_tabledimension_has_value():
    assert hasattr(cobol_tables_TableDimension, "value")
    descriptor = None
    for klass in cobol_tables_TableDimension.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_additionalindexname_is_not_abstract():
    assert not inspect.isabstract(AdditionalIndexName)


def test_additionalindexname_constructor_exists():
    assert callable(AdditionalIndexName.__init__)


def test_additionalindexname_constructor_args():
    sig = inspect.signature(AdditionalIndexName.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_cobol_parameters_byreferenceparameter_is_not_abstract():
    assert not inspect.isabstract(cobol_parameters_ByReferenceParameter)


def test_cobol_parameters_byreferenceparameter_constructor_exists():
    assert callable(cobol_parameters_ByReferenceParameter.__init__)


def test_cobol_parameters_byreferenceparameter_constructor_args():
    sig = inspect.signature(cobol_parameters_ByReferenceParameter.__init__)
    params = list(sig.parameters.keys())



def test_cobol_parameters_byvalueparameter_is_not_abstract():
    assert not inspect.isabstract(cobol_parameters_ByValueParameter)


def test_cobol_parameters_byvalueparameter_constructor_exists():
    assert callable(cobol_parameters_ByValueParameter.__init__)


def test_cobol_parameters_byvalueparameter_constructor_args():
    sig = inspect.signature(cobol_parameters_ByValueParameter.__init__)
    params = list(sig.parameters.keys())



def test_cobol_parameters_parametrizable_is_not_abstract():
    assert not inspect.isabstract(cobol_parameters_Parametrizable)


def test_cobol_parameters_parametrizable_constructor_exists():
    assert callable(cobol_parameters_Parametrizable.__init__)


def test_cobol_parameters_parametrizable_constructor_args():
    sig = inspect.signature(cobol_parameters_Parametrizable.__init__)
    params = list(sig.parameters.keys())



def test_indexname_is_not_abstract():
    assert not inspect.isabstract(IndexName)


def test_indexname_constructor_exists():
    assert callable(IndexName.__init__)


def test_indexname_constructor_args():
    sig = inspect.signature(IndexName.__init__)
    params = list(sig.parameters.keys())



def test_tabledimension_is_not_abstract():
    assert not inspect.isabstract(TableDimension)


def test_tabledimension_constructor_exists():
    assert callable(TableDimension.__init__)


def test_tabledimension_constructor_args():
    sig = inspect.signature(TableDimension.__init__)
    params = list(sig.parameters.keys())



def test_dataitems_dataitem_is_not_abstract():
    assert not inspect.isabstract(dataitems_DataItem)


def test_dataitems_dataitem_constructor_exists():
    assert callable(dataitems_DataItem.__init__)


def test_dataitems_dataitem_constructor_args():
    sig = inspect.signature(dataitems_DataItem.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_specialnamestatement_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_SpecialNameStatement)


def test_cobol_specialnames_specialnamestatement_constructor_exists():
    assert callable(cobol_specialnames_SpecialNameStatement.__init__)


def test_cobol_specialnames_specialnamestatement_constructor_args():
    sig = inspect.signature(cobol_specialnames_SpecialNameStatement.__init__)
    params = list(sig.parameters.keys())



def test_alphabetnamereference_is_not_abstract():
    assert not inspect.isabstract(AlphabetNameReference)


def test_alphabetnamereference_constructor_exists():
    assert callable(AlphabetNameReference.__init__)


def test_alphabetnamereference_constructor_args():
    sig = inspect.signature(AlphabetNameReference.__init__)
    params = list(sig.parameters.keys())



def test_symboliccharacter_is_not_abstract():
    assert not inspect.isabstract(SymbolicCharacter)


def test_symboliccharacter_constructor_exists():
    assert callable(SymbolicCharacter.__init__)


def test_symboliccharacter_constructor_args():
    sig = inspect.signature(SymbolicCharacter.__init__)
    params = list(sig.parameters.keys())



def test_specialname_is_not_abstract():
    assert not inspect.isabstract(SpecialName)


def test_specialname_constructor_exists():
    assert callable(SpecialName.__init__)


def test_specialname_constructor_args():
    sig = inspect.signature(SpecialName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_symboliccharacter_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_SymbolicCharacter)


def test_cobol_specialnames_symboliccharacter_constructor_exists():
    assert callable(cobol_specialnames_SymbolicCharacter.__init__)


def test_cobol_specialnames_symboliccharacter_constructor_args():
    sig = inspect.signature(cobol_specialnames_SymbolicCharacter.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_mnemonicname_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_MnemonicName)


def test_cobol_specialnames_mnemonicname_constructor_exists():
    assert callable(cobol_specialnames_MnemonicName.__init__)


def test_cobol_specialnames_mnemonicname_constructor_args():
    sig = inspect.signature(cobol_specialnames_MnemonicName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_tables_keyname_is_not_abstract():
    assert not inspect.isabstract(cobol_tables_KeyName)


def test_cobol_tables_keyname_constructor_exists():
    assert callable(cobol_tables_KeyName.__init__)


def test_cobol_tables_keyname_constructor_args():
    sig = inspect.signature(cobol_tables_KeyName.__init__)
    params = list(sig.parameters.keys())
    assert "keyOrder" in params, "Missing parameter 'keyOrder'"

def test_cobol_tables_keyname_has_keyOrder():
    assert hasattr(cobol_tables_KeyName, "keyOrder")
    descriptor = None
    for klass in cobol_tables_KeyName.__mro__:
        if "keyOrder" in klass.__dict__:
            descriptor = klass.__dict__["keyOrder"]
            break
    assert isinstance(descriptor, property)



def test_keyname_is_not_abstract():
    assert not inspect.isabstract(KeyName)


def test_keyname_constructor_exists():
    assert callable(KeyName.__init__)


def test_keyname_constructor_args():
    sig = inspect.signature(KeyName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_alphabettype_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_AlphabetType)


def test_cobol_specialnames_alphabettype_constructor_exists():
    assert callable(cobol_specialnames_AlphabetType.__init__)


def test_cobol_specialnames_alphabettype_constructor_args():
    sig = inspect.signature(cobol_specialnames_AlphabetType.__init__)
    params = list(sig.parameters.keys())



def test_specialnames_mnemonicname_is_not_abstract():
    assert not inspect.isabstract(specialnames_MnemonicName)


def test_specialnames_mnemonicname_constructor_exists():
    assert callable(specialnames_MnemonicName.__init__)


def test_specialnames_mnemonicname_constructor_args():
    sig = inspect.signature(specialnames_MnemonicName.__init__)
    params = list(sig.parameters.keys())



def test_alphabettype_is_not_abstract():
    assert not inspect.isabstract(AlphabetType)


def test_alphabettype_constructor_exists():
    assert callable(AlphabetType.__init__)


def test_alphabettype_constructor_args():
    sig = inspect.signature(AlphabetType.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_predefinedalphabettype_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_PredefinedAlphabetType)


def test_cobol_specialnames_predefinedalphabettype_constructor_exists():
    assert callable(cobol_specialnames_PredefinedAlphabetType.__init__)


def test_cobol_specialnames_predefinedalphabettype_constructor_args():
    sig = inspect.signature(cobol_specialnames_PredefinedAlphabetType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_specialnames_predefinedalphabettype_has_value():
    assert hasattr(cobol_specialnames_PredefinedAlphabetType, "value")
    descriptor = None
    for klass in cobol_specialnames_PredefinedAlphabetType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_specialnames_codenamealphabettype_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_CodeNameAlphabetType)


def test_cobol_specialnames_codenamealphabettype_constructor_exists():
    assert callable(cobol_specialnames_CodeNameAlphabetType.__init__)


def test_cobol_specialnames_codenamealphabettype_constructor_args():
    sig = inspect.signature(cobol_specialnames_CodeNameAlphabetType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_specialnames_codenamealphabettype_has_value():
    assert hasattr(cobol_specialnames_CodeNameAlphabetType, "value")
    descriptor = None
    for klass in cobol_specialnames_CodeNameAlphabetType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_specialnames_specialnamestatement_is_not_abstract():
    assert not inspect.isabstract(specialnames_SpecialNameStatement)


def test_specialnames_specialnamestatement_constructor_exists():
    assert callable(specialnames_SpecialNameStatement.__init__)


def test_specialnames_specialnamestatement_constructor_args():
    sig = inspect.signature(specialnames_SpecialNameStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_systemdeviceis_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_SystemDeviceIs)


def test_cobol_specialnames_systemdeviceis_constructor_exists():
    assert callable(cobol_specialnames_SystemDeviceIs.__init__)


def test_cobol_specialnames_systemdeviceis_constructor_args():
    sig = inspect.signature(cobol_specialnames_SystemDeviceIs.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_upsiswitchis_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_UPSISwitchIs)


def test_cobol_specialnames_upsiswitchis_constructor_exists():
    assert callable(cobol_specialnames_UPSISwitchIs.__init__)


def test_cobol_specialnames_upsiswitchis_constructor_args():
    sig = inspect.signature(cobol_specialnames_UPSISwitchIs.__init__)
    params = list(sig.parameters.keys())



def test_conditionname_is_not_abstract():
    assert not inspect.isabstract(ConditionName)


def test_conditionname_constructor_exists():
    assert callable(ConditionName.__init__)


def test_conditionname_constructor_args():
    sig = inspect.signature(ConditionName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_offstatus_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_OffStatus)


def test_cobol_specialnames_offstatus_constructor_exists():
    assert callable(cobol_specialnames_OffStatus.__init__)


def test_cobol_specialnames_offstatus_constructor_args():
    sig = inspect.signature(cobol_specialnames_OffStatus.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_onstatus_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_OnStatus)


def test_cobol_specialnames_onstatus_constructor_exists():
    assert callable(cobol_specialnames_OnStatus.__init__)


def test_cobol_specialnames_onstatus_constructor_args():
    sig = inspect.signature(cobol_specialnames_OnStatus.__init__)
    params = list(sig.parameters.keys())



def test_specialnames_specialname_is_not_abstract():
    assert not inspect.isabstract(specialnames_SpecialName)


def test_specialnames_specialname_constructor_exists():
    assert callable(specialnames_SpecialName.__init__)


def test_specialnames_specialname_constructor_args():
    sig = inspect.signature(specialnames_SpecialName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_currencysign_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_CurrencySign)


def test_cobol_specialnames_currencysign_constructor_exists():
    assert callable(cobol_specialnames_CurrencySign.__init__)


def test_cobol_specialnames_currencysign_constructor_args():
    sig = inspect.signature(cobol_specialnames_CurrencySign.__init__)
    params = list(sig.parameters.keys())
    assert "pictureSymbol" in params, "Missing parameter 'pictureSymbol'"

def test_cobol_specialnames_currencysign_has_pictureSymbol():
    assert hasattr(cobol_specialnames_CurrencySign, "pictureSymbol")
    descriptor = None
    for klass in cobol_specialnames_CurrencySign.__mro__:
        if "pictureSymbol" in klass.__dict__:
            descriptor = klass.__dict__["pictureSymbol"]
            break
    assert isinstance(descriptor, property)



def test_cobol_specialnames_alphabetname_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_AlphabetName)


def test_cobol_specialnames_alphabetname_constructor_exists():
    assert callable(cobol_specialnames_AlphabetName.__init__)


def test_cobol_specialnames_alphabetname_constructor_args():
    sig = inspect.signature(cobol_specialnames_AlphabetName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_classname_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_ClassName)


def test_cobol_specialnames_classname_constructor_exists():
    assert callable(cobol_specialnames_ClassName.__init__)


def test_cobol_specialnames_classname_constructor_args():
    sig = inspect.signature(cobol_specialnames_ClassName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_explicitalphabettype_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_ExplicitAlphabetType)


def test_cobol_specialnames_explicitalphabettype_constructor_exists():
    assert callable(cobol_specialnames_ExplicitAlphabetType.__init__)


def test_cobol_specialnames_explicitalphabettype_constructor_args():
    sig = inspect.signature(cobol_specialnames_ExplicitAlphabetType.__init__)
    params = list(sig.parameters.keys())



def test_references_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(references_ReferenceableElement)


def test_references_referenceableelement_constructor_exists():
    assert callable(references_ReferenceableElement.__init__)


def test_references_referenceableelement_constructor_args():
    sig = inspect.signature(references_ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_dataitemattribute_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_DataItemAttribute)


def test_cobol_dataitems_dataitemattribute_constructor_exists():
    assert callable(cobol_dataitems_DataItemAttribute.__init__)


def test_cobol_dataitems_dataitemattribute_constructor_args():
    sig = inspect.signature(cobol_dataitems_DataItemAttribute.__init__)
    params = list(sig.parameters.keys())



def test_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(RangeExpression)


def test_rangeexpression_constructor_exists():
    assert callable(RangeExpression.__init__)


def test_rangeexpression_constructor_args():
    sig = inspect.signature(RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_dataname_is_not_abstract():
    assert not inspect.isabstract(DataName)


def test_dataname_constructor_exists():
    assert callable(DataName.__init__)


def test_dataname_constructor_args():
    sig = inspect.signature(DataName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_renamingdataname_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_RenamingDataName)


def test_cobol_dataitems_renamingdataname_constructor_exists():
    assert callable(cobol_dataitems_RenamingDataName.__init__)


def test_cobol_dataitems_renamingdataname_constructor_args():
    sig = inspect.signature(cobol_dataitems_RenamingDataName.__init__)
    params = list(sig.parameters.keys())



def test_dataitemattribute_is_not_abstract():
    assert not inspect.isabstract(DataItemAttribute)


def test_dataitemattribute_constructor_exists():
    assert callable(DataItemAttribute.__init__)


def test_dataitemattribute_constructor_args():
    sig = inspect.signature(DataItemAttribute.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_groupusage_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_GroupUsage)


def test_cobol_dataitems_groupusage_constructor_exists():
    assert callable(cobol_dataitems_GroupUsage.__init__)


def test_cobol_dataitems_groupusage_constructor_args():
    sig = inspect.signature(cobol_dataitems_GroupUsage.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_redefines_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_Redefines)


def test_cobol_dataitems_redefines_constructor_exists():
    assert callable(cobol_dataitems_Redefines.__init__)


def test_cobol_dataitems_redefines_constructor_args():
    sig = inspect.signature(cobol_dataitems_Redefines.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_value_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_Value)


def test_cobol_dataitems_value_constructor_exists():
    assert callable(cobol_dataitems_Value.__init__)


def test_cobol_dataitems_value_constructor_args():
    sig = inspect.signature(cobol_dataitems_Value.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_global_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_Global)


def test_cobol_dataitems_global_constructor_exists():
    assert callable(cobol_dataitems_Global.__init__)


def test_cobol_dataitems_global_constructor_args():
    sig = inspect.signature(cobol_dataitems_Global.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_external_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_External)


def test_cobol_dataitems_external_constructor_exists():
    assert callable(cobol_dataitems_External.__init__)


def test_cobol_dataitems_external_constructor_args():
    sig = inspect.signature(cobol_dataitems_External.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_usage_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_Usage)


def test_cobol_dataitems_usage_constructor_exists():
    assert callable(cobol_dataitems_Usage.__init__)


def test_cobol_dataitems_usage_constructor_args():
    sig = inspect.signature(cobol_dataitems_Usage.__init__)
    params = list(sig.parameters.keys())
    assert "usage" in params, "Missing parameter 'usage'"
    assert "isNative" in params, "Missing parameter 'isNative'"

def test_cobol_dataitems_usage_has_usage():
    assert hasattr(cobol_dataitems_Usage, "usage")
    descriptor = None
    for klass in cobol_dataitems_Usage.__mro__:
        if "usage" in klass.__dict__:
            descriptor = klass.__dict__["usage"]
            break
    assert isinstance(descriptor, property)

def test_cobol_dataitems_usage_has_isNative():
    assert hasattr(cobol_dataitems_Usage, "isNative")
    descriptor = None
    for klass in cobol_dataitems_Usage.__mro__:
        if "isNative" in klass.__dict__:
            descriptor = klass.__dict__["isNative"]
            break
    assert isinstance(descriptor, property)



def test_cobol_dataitems_picturestring_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_PictureString)


def test_cobol_dataitems_picturestring_constructor_exists():
    assert callable(cobol_dataitems_PictureString.__init__)


def test_cobol_dataitems_picturestring_constructor_args():
    sig = inspect.signature(cobol_dataitems_PictureString.__init__)
    params = list(sig.parameters.keys())
    assert "picture" in params, "Missing parameter 'picture'"

def test_cobol_dataitems_picturestring_has_picture():
    assert hasattr(cobol_dataitems_PictureString, "picture")
    descriptor = None
    for klass in cobol_dataitems_PictureString.__mro__:
        if "picture" in klass.__dict__:
            descriptor = klass.__dict__["picture"]
            break
    assert isinstance(descriptor, property)



def test_systemdevice_is_not_abstract():
    assert not inspect.isabstract(SystemDevice)


def test_systemdevice_constructor_exists():
    assert callable(SystemDevice.__init__)


def test_systemdevice_constructor_args():
    sig = inspect.signature(SystemDevice.__init__)
    params = list(sig.parameters.keys())



def test_cobol_environments_systempunchdevice_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_SystemPunchDevice)


def test_cobol_environments_systempunchdevice_constructor_exists():
    assert callable(cobol_environments_SystemPunchDevice.__init__)


def test_cobol_environments_systempunchdevice_constructor_args():
    sig = inspect.signature(cobol_environments_SystemPunchDevice.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_environments_systempunchdevice_has_value():
    assert hasattr(cobol_environments_SystemPunchDevice, "value")
    descriptor = None
    for klass in cobol_environments_SystemPunchDevice.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_environments_advancedfunctionprinting_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_AdvancedFunctionPrinting)


def test_cobol_environments_advancedfunctionprinting_constructor_exists():
    assert callable(cobol_environments_AdvancedFunctionPrinting.__init__)


def test_cobol_environments_advancedfunctionprinting_constructor_args():
    sig = inspect.signature(cobol_environments_AdvancedFunctionPrinting.__init__)
    params = list(sig.parameters.keys())



def test_cobol_environments_suppressspacing_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_SuppressSpacing)


def test_cobol_environments_suppressspacing_constructor_exists():
    assert callable(cobol_environments_SuppressSpacing.__init__)


def test_cobol_environments_suppressspacing_constructor_args():
    sig = inspect.signature(cobol_environments_SuppressSpacing.__init__)
    params = list(sig.parameters.keys())



def test_cobol_environments_console_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_Console)


def test_cobol_environments_console_constructor_exists():
    assert callable(cobol_environments_Console.__init__)


def test_cobol_environments_console_constructor_args():
    sig = inspect.signature(cobol_environments_Console.__init__)
    params = list(sig.parameters.keys())



def test_cobol_environments_systemlogicaloutput_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_SystemLogicalOutput)


def test_cobol_environments_systemlogicaloutput_constructor_exists():
    assert callable(cobol_environments_SystemLogicalOutput.__init__)


def test_cobol_environments_systemlogicaloutput_constructor_args():
    sig = inspect.signature(cobol_environments_SystemLogicalOutput.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_environments_systemlogicaloutput_has_value():
    assert hasattr(cobol_environments_SystemLogicalOutput, "value")
    descriptor = None
    for klass in cobol_environments_SystemLogicalOutput.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_environments_pocket_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_Pocket)


def test_cobol_environments_pocket_constructor_exists():
    assert callable(cobol_environments_Pocket.__init__)


def test_cobol_environments_pocket_constructor_args():
    sig = inspect.signature(cobol_environments_Pocket.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_environments_pocket_has_value():
    assert hasattr(cobol_environments_Pocket, "value")
    descriptor = None
    for klass in cobol_environments_Pocket.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_environments_channel_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_Channel)


def test_cobol_environments_channel_constructor_exists():
    assert callable(cobol_environments_Channel.__init__)


def test_cobol_environments_channel_constructor_args():
    sig = inspect.signature(cobol_environments_Channel.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_environments_channel_has_value():
    assert hasattr(cobol_environments_Channel, "value")
    descriptor = None
    for klass in cobol_environments_Channel.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_environments_systemlogicalinput_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_SystemLogicalInput)


def test_cobol_environments_systemlogicalinput_constructor_exists():
    assert callable(cobol_environments_SystemLogicalInput.__init__)


def test_cobol_environments_systemlogicalinput_constructor_args():
    sig = inspect.signature(cobol_environments_SystemLogicalInput.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_environments_systemlogicalinput_has_value():
    assert hasattr(cobol_environments_SystemLogicalInput, "value")
    descriptor = None
    for klass in cobol_environments_SystemLogicalInput.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_register_is_not_abstract():
    assert not inspect.isabstract(Register)


def test_register_constructor_exists():
    assert callable(Register.__init__)


def test_register_constructor_args():
    sig = inspect.signature(Register.__init__)
    params = list(sig.parameters.keys())



def test_cobol_registers_shiftout_is_not_abstract():
    assert not inspect.isabstract(cobol_registers_ShiftOut)


def test_cobol_registers_shiftout_constructor_exists():
    assert callable(cobol_registers_ShiftOut.__init__)


def test_cobol_registers_shiftout_constructor_args():
    sig = inspect.signature(cobol_registers_ShiftOut.__init__)
    params = list(sig.parameters.keys())



def test_cobol_registers_addressof_is_not_abstract():
    assert not inspect.isabstract(cobol_registers_AddressOf)


def test_cobol_registers_addressof_constructor_exists():
    assert callable(cobol_registers_AddressOf.__init__)


def test_cobol_registers_addressof_constructor_args():
    sig = inspect.signature(cobol_registers_AddressOf.__init__)
    params = list(sig.parameters.keys())



def test_cobol_registers_lengthof_is_not_abstract():
    assert not inspect.isabstract(cobol_registers_LengthOf)


def test_cobol_registers_lengthof_constructor_exists():
    assert callable(cobol_registers_LengthOf.__init__)


def test_cobol_registers_lengthof_constructor_args():
    sig = inspect.signature(cobol_registers_LengthOf.__init__)
    params = list(sig.parameters.keys())



def test_cobol_registers_whencompiled_is_not_abstract():
    assert not inspect.isabstract(cobol_registers_WhenCompiled)


def test_cobol_registers_whencompiled_constructor_exists():
    assert callable(cobol_registers_WhenCompiled.__init__)


def test_cobol_registers_whencompiled_constructor_args():
    sig = inspect.signature(cobol_registers_WhenCompiled.__init__)
    params = list(sig.parameters.keys())



def test_cobol_registers_returncode_is_not_abstract():
    assert not inspect.isabstract(cobol_registers_ReturnCode)


def test_cobol_registers_returncode_constructor_exists():
    assert callable(cobol_registers_ReturnCode.__init__)


def test_cobol_registers_returncode_constructor_args():
    sig = inspect.signature(cobol_registers_ReturnCode.__init__)
    params = list(sig.parameters.keys())



def test_cobol_registers_shiftin_is_not_abstract():
    assert not inspect.isabstract(cobol_registers_ShiftIn)


def test_cobol_registers_shiftin_constructor_exists():
    assert callable(cobol_registers_ShiftIn.__init__)


def test_cobol_registers_shiftin_constructor_args():
    sig = inspect.signature(cobol_registers_ShiftIn.__init__)
    params = list(sig.parameters.keys())



def test_sortphrasewater_is_not_abstract():
    assert not inspect.isabstract(SortPhraseWater)


def test_sortphrasewater_constructor_exists():
    assert callable(SortPhraseWater.__init__)


def test_sortphrasewater_constructor_args():
    sig = inspect.signature(SortPhraseWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_sortphrasetoken_is_not_abstract():
    assert not inspect.isabstract(cobol_water_SortPhraseToken)


def test_cobol_water_sortphrasetoken_constructor_exists():
    assert callable(cobol_water_SortPhraseToken.__init__)


def test_cobol_water_sortphrasetoken_constructor_args():
    sig = inspect.signature(cobol_water_SortPhraseToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_sortphrasetoken_has_value():
    assert hasattr(cobol_water_SortPhraseToken, "value")
    descriptor = None
    for klass in cobol_water_SortPhraseToken.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_openstatementwater_is_not_abstract():
    assert not inspect.isabstract(OpenStatementWater)


def test_openstatementwater_constructor_exists():
    assert callable(OpenStatementWater.__init__)


def test_openstatementwater_constructor_args():
    sig = inspect.signature(OpenStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_openstatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol_water_OpenStatementToken)


def test_cobol_water_openstatementtoken_constructor_exists():
    assert callable(cobol_water_OpenStatementToken.__init__)


def test_cobol_water_openstatementtoken_constructor_args():
    sig = inspect.signature(cobol_water_OpenStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_openstatementtoken_has_value():
    assert hasattr(cobol_water_OpenStatementToken, "value")
    descriptor = None
    for klass in cobol_water_OpenStatementToken.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_invokestatementwater_is_not_abstract():
    assert not inspect.isabstract(InvokeStatementWater)


def test_invokestatementwater_constructor_exists():
    assert callable(InvokeStatementWater.__init__)


def test_invokestatementwater_constructor_args():
    sig = inspect.signature(InvokeStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_invokestatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol_water_InvokeStatementToken)


def test_cobol_water_invokestatementtoken_constructor_exists():
    assert callable(cobol_water_InvokeStatementToken.__init__)


def test_cobol_water_invokestatementtoken_constructor_args():
    sig = inspect.signature(cobol_water_InvokeStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_invokestatementtoken_has_value():
    assert hasattr(cobol_water_InvokeStatementToken, "value")
    descriptor = None
    for klass in cobol_water_InvokeStatementToken.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_closestatementwater_is_not_abstract():
    assert not inspect.isabstract(CloseStatementWater)


def test_closestatementwater_constructor_exists():
    assert callable(CloseStatementWater.__init__)


def test_closestatementwater_constructor_args():
    sig = inspect.signature(CloseStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_closestatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol_water_CloseStatementToken)


def test_cobol_water_closestatementtoken_constructor_exists():
    assert callable(cobol_water_CloseStatementToken.__init__)


def test_cobol_water_closestatementtoken_constructor_args():
    sig = inspect.signature(cobol_water_CloseStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_closestatementtoken_has_value():
    assert hasattr(cobol_water_CloseStatementToken, "value")
    descriptor = None
    for klass in cobol_water_CloseStatementToken.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_usestatementwater_is_not_abstract():
    assert not inspect.isabstract(UseStatementWater)


def test_usestatementwater_constructor_exists():
    assert callable(UseStatementWater.__init__)


def test_usestatementwater_constructor_args():
    sig = inspect.signature(UseStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_usestatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol_water_UseStatementToken)


def test_cobol_water_usestatementtoken_constructor_exists():
    assert callable(cobol_water_UseStatementToken.__init__)


def test_cobol_water_usestatementtoken_constructor_args():
    sig = inspect.signature(cobol_water_UseStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_usestatementtoken_has_value():
    assert hasattr(cobol_water_UseStatementToken, "value")
    descriptor = None
    for klass in cobol_water_UseStatementToken.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_acceptstatementwater_is_not_abstract():
    assert not inspect.isabstract(AcceptStatementWater)


def test_acceptstatementwater_constructor_exists():
    assert callable(AcceptStatementWater.__init__)


def test_acceptstatementwater_constructor_args():
    sig = inspect.signature(AcceptStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_environments_environment_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_Environment)


def test_cobol_environments_environment_constructor_exists():
    assert callable(cobol_environments_Environment.__init__)


def test_cobol_environments_environment_constructor_args():
    sig = inspect.signature(cobol_environments_Environment.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_acceptstatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol_water_AcceptStatementToken)


def test_cobol_water_acceptstatementtoken_constructor_exists():
    assert callable(cobol_water_AcceptStatementToken.__init__)


def test_cobol_water_acceptstatementtoken_constructor_args():
    sig = inspect.signature(cobol_water_AcceptStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_acceptstatementtoken_has_value():
    assert hasattr(cobol_water_AcceptStatementToken, "value")
    descriptor = None
    for klass in cobol_water_AcceptStatementToken.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cicsstatementwater_is_not_abstract():
    assert not inspect.isabstract(CICSStatementWater)


def test_cicsstatementwater_constructor_exists():
    assert callable(CICSStatementWater.__init__)


def test_cicsstatementwater_constructor_args():
    sig = inspect.signature(CICSStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_cicsstatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol_water_CICSStatementToken)


def test_cobol_water_cicsstatementtoken_constructor_exists():
    assert callable(cobol_water_CICSStatementToken.__init__)


def test_cobol_water_cicsstatementtoken_constructor_args():
    sig = inspect.signature(cobol_water_CICSStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_cicsstatementtoken_has_value():
    assert hasattr(cobol_water_CICSStatementToken, "value")
    descriptor = None
    for klass in cobol_water_CICSStatementToken.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sqlstatementwater_is_not_abstract():
    assert not inspect.isabstract(SQLStatementWater)


def test_sqlstatementwater_constructor_exists():
    assert callable(SQLStatementWater.__init__)


def test_sqlstatementwater_constructor_args():
    sig = inspect.signature(SQLStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_sqlstatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol_water_SQLStatementToken)


def test_cobol_water_sqlstatementtoken_constructor_exists():
    assert callable(cobol_water_SQLStatementToken.__init__)


def test_cobol_water_sqlstatementtoken_constructor_args():
    sig = inspect.signature(cobol_water_SQLStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_sqlstatementtoken_has_value():
    assert hasattr(cobol_water_SQLStatementToken, "value")
    descriptor = None
    for klass in cobol_water_SQLStatementToken.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_repositoryparagraphwater_is_not_abstract():
    assert not inspect.isabstract(RepositoryParagraphWater)


def test_repositoryparagraphwater_constructor_exists():
    assert callable(RepositoryParagraphWater.__init__)


def test_repositoryparagraphwater_constructor_args():
    sig = inspect.signature(RepositoryParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_repositorydescription_is_not_abstract():
    assert not inspect.isabstract(cobol_water_RepositoryDescription)


def test_cobol_water_repositorydescription_constructor_exists():
    assert callable(cobol_water_RepositoryDescription.__init__)


def test_cobol_water_repositorydescription_constructor_args():
    sig = inspect.signature(cobol_water_RepositoryDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_repositorydescription_has_value():
    assert hasattr(cobol_water_RepositoryDescription, "value")
    descriptor = None
    for klass in cobol_water_RepositoryDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iocontrolparagraphwater_is_not_abstract():
    assert not inspect.isabstract(IOControlParagraphWater)


def test_iocontrolparagraphwater_constructor_exists():
    assert callable(IOControlParagraphWater.__init__)


def test_iocontrolparagraphwater_constructor_args():
    sig = inspect.signature(IOControlParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_iocontroldescription_is_not_abstract():
    assert not inspect.isabstract(cobol_water_IOControlDescription)


def test_cobol_water_iocontroldescription_constructor_exists():
    assert callable(cobol_water_IOControlDescription.__init__)


def test_cobol_water_iocontroldescription_constructor_args():
    sig = inspect.signature(cobol_water_IOControlDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_iocontroldescription_has_value():
    assert hasattr(cobol_water_IOControlDescription, "value")
    descriptor = None
    for klass in cobol_water_IOControlDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_datadescriptorwater_is_not_abstract():
    assert not inspect.isabstract(DataDescriptorWater)


def test_datadescriptorwater_constructor_exists():
    assert callable(DataDescriptorWater.__init__)


def test_datadescriptorwater_constructor_args():
    sig = inspect.signature(DataDescriptorWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_datadescription_is_not_abstract():
    assert not inspect.isabstract(cobol_water_DataDescription)


def test_cobol_water_datadescription_constructor_exists():
    assert callable(cobol_water_DataDescription.__init__)


def test_cobol_water_datadescription_constructor_args():
    sig = inspect.signature(cobol_water_DataDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_datadescription_has_value():
    assert hasattr(cobol_water_DataDescription, "value")
    descriptor = None
    for klass in cobol_water_DataDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_filedescriptorwater_is_not_abstract():
    assert not inspect.isabstract(FileDescriptorWater)


def test_filedescriptorwater_constructor_exists():
    assert callable(FileDescriptorWater.__init__)


def test_filedescriptorwater_constructor_args():
    sig = inspect.signature(FileDescriptorWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_filedescription_is_not_abstract():
    assert not inspect.isabstract(cobol_water_FileDescription)


def test_cobol_water_filedescription_constructor_exists():
    assert callable(cobol_water_FileDescription.__init__)


def test_cobol_water_filedescription_constructor_args():
    sig = inspect.signature(cobol_water_FileDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_filedescription_has_value():
    assert hasattr(cobol_water_FileDescription, "value")
    descriptor = None
    for klass in cobol_water_FileDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_selectstatementwater_is_not_abstract():
    assert not inspect.isabstract(SelectStatementWater)


def test_selectstatementwater_constructor_exists():
    assert callable(SelectStatementWater.__init__)


def test_selectstatementwater_constructor_args():
    sig = inspect.signature(SelectStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_selectstatementclause_is_not_abstract():
    assert not inspect.isabstract(cobol_water_SelectStatementClause)


def test_cobol_water_selectstatementclause_constructor_exists():
    assert callable(cobol_water_SelectStatementClause.__init__)


def test_cobol_water_selectstatementclause_constructor_args():
    sig = inspect.signature(cobol_water_SelectStatementClause.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_selectstatementclause_has_value():
    assert hasattr(cobol_water_SelectStatementClause, "value")
    descriptor = None
    for klass in cobol_water_SelectStatementClause.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_objectcomputerparagraphwater_is_not_abstract():
    assert not inspect.isabstract(ObjectComputerParagraphWater)


def test_objectcomputerparagraphwater_constructor_exists():
    assert callable(ObjectComputerParagraphWater.__init__)


def test_objectcomputerparagraphwater_constructor_args():
    sig = inspect.signature(ObjectComputerParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_prioritynumber_is_not_abstract():
    assert not inspect.isabstract(cobol_water_PriorityNumber)


def test_cobol_water_prioritynumber_constructor_exists():
    assert callable(cobol_water_PriorityNumber.__init__)


def test_cobol_water_prioritynumber_constructor_args():
    sig = inspect.signature(cobol_water_PriorityNumber.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_prioritynumber_has_value():
    assert hasattr(cobol_water_PriorityNumber, "value")
    descriptor = None
    for klass in cobol_water_PriorityNumber.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_water_objectcomputerdescription_is_not_abstract():
    assert not inspect.isabstract(cobol_water_ObjectComputerDescription)


def test_cobol_water_objectcomputerdescription_constructor_exists():
    assert callable(cobol_water_ObjectComputerDescription.__init__)


def test_cobol_water_objectcomputerdescription_constructor_args():
    sig = inspect.signature(cobol_water_ObjectComputerDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_objectcomputerdescription_has_value():
    assert hasattr(cobol_water_ObjectComputerDescription, "value")
    descriptor = None
    for klass in cobol_water_ObjectComputerDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_water_water_is_not_abstract():
    assert not inspect.isabstract(cobol_water_Water)


def test_cobol_water_water_constructor_exists():
    assert callable(cobol_water_Water.__init__)


def test_cobol_water_water_constructor_args():
    sig = inspect.signature(cobol_water_Water.__init__)
    params = list(sig.parameters.keys())



def test_water_is_not_abstract():
    assert not inspect.isabstract(Water)


def test_water_constructor_exists():
    assert callable(Water.__init__)


def test_water_constructor_args():
    sig = inspect.signature(Water.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_closestatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_CloseStatementWater)


def test_cobol_water_closestatementwater_constructor_exists():
    assert callable(cobol_water_CloseStatementWater.__init__)


def test_cobol_water_closestatementwater_constructor_args():
    sig = inspect.signature(cobol_water_CloseStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_filedescriptorwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_FileDescriptorWater)


def test_cobol_water_filedescriptorwater_constructor_exists():
    assert callable(cobol_water_FileDescriptorWater.__init__)


def test_cobol_water_filedescriptorwater_constructor_args():
    sig = inspect.signature(cobol_water_FileDescriptorWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_invokestatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_InvokeStatementWater)


def test_cobol_water_invokestatementwater_constructor_exists():
    assert callable(cobol_water_InvokeStatementWater.__init__)


def test_cobol_water_invokestatementwater_constructor_args():
    sig = inspect.signature(cobol_water_InvokeStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_datadescriptorwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_DataDescriptorWater)


def test_cobol_water_datadescriptorwater_constructor_exists():
    assert callable(cobol_water_DataDescriptorWater.__init__)


def test_cobol_water_datadescriptorwater_constructor_args():
    sig = inspect.signature(cobol_water_DataDescriptorWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_selectstatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_SelectStatementWater)


def test_cobol_water_selectstatementwater_constructor_exists():
    assert callable(cobol_water_SelectStatementWater.__init__)


def test_cobol_water_selectstatementwater_constructor_args():
    sig = inspect.signature(cobol_water_SelectStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_sqlstatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_SQLStatementWater)


def test_cobol_water_sqlstatementwater_constructor_exists():
    assert callable(cobol_water_SQLStatementWater.__init__)


def test_cobol_water_sqlstatementwater_constructor_args():
    sig = inspect.signature(cobol_water_SQLStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_acceptstatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_AcceptStatementWater)


def test_cobol_water_acceptstatementwater_constructor_exists():
    assert callable(cobol_water_AcceptStatementWater.__init__)


def test_cobol_water_acceptstatementwater_constructor_args():
    sig = inspect.signature(cobol_water_AcceptStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_identificationdivisionwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_IdentificationDivisionWater)


def test_cobol_water_identificationdivisionwater_constructor_exists():
    assert callable(cobol_water_IdentificationDivisionWater.__init__)


def test_cobol_water_identificationdivisionwater_constructor_args():
    sig = inspect.signature(cobol_water_IdentificationDivisionWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_usestatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_UseStatementWater)


def test_cobol_water_usestatementwater_constructor_exists():
    assert callable(cobol_water_UseStatementWater.__init__)


def test_cobol_water_usestatementwater_constructor_args():
    sig = inspect.signature(cobol_water_UseStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_iocontrolparagraphwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_IOControlParagraphWater)


def test_cobol_water_iocontrolparagraphwater_constructor_exists():
    assert callable(cobol_water_IOControlParagraphWater.__init__)


def test_cobol_water_iocontrolparagraphwater_constructor_args():
    sig = inspect.signature(cobol_water_IOControlParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_specialnamesparagraphwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_SpecialNamesParagraphWater)


def test_cobol_water_specialnamesparagraphwater_constructor_exists():
    assert callable(cobol_water_SpecialNamesParagraphWater.__init__)


def test_cobol_water_specialnamesparagraphwater_constructor_args():
    sig = inspect.signature(cobol_water_SpecialNamesParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_objectcomputerparagraphwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_ObjectComputerParagraphWater)


def test_cobol_water_objectcomputerparagraphwater_constructor_exists():
    assert callable(cobol_water_ObjectComputerParagraphWater.__init__)


def test_cobol_water_objectcomputerparagraphwater_constructor_args():
    sig = inspect.signature(cobol_water_ObjectComputerParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_openstatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_OpenStatementWater)


def test_cobol_water_openstatementwater_constructor_exists():
    assert callable(cobol_water_OpenStatementWater.__init__)


def test_cobol_water_openstatementwater_constructor_args():
    sig = inspect.signature(cobol_water_OpenStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_cicsstatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_CICSStatementWater)


def test_cobol_water_cicsstatementwater_constructor_exists():
    assert callable(cobol_water_CICSStatementWater.__init__)


def test_cobol_water_cicsstatementwater_constructor_args():
    sig = inspect.signature(cobol_water_CICSStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_sortphrasewater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_SortPhraseWater)


def test_cobol_water_sortphrasewater_constructor_exists():
    assert callable(cobol_water_SortPhraseWater.__init__)


def test_cobol_water_sortphrasewater_constructor_args():
    sig = inspect.signature(cobol_water_SortPhraseWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_repositoryparagraphwater_is_not_abstract():
    assert not inspect.isabstract(cobol_water_RepositoryParagraphWater)


def test_cobol_water_repositoryparagraphwater_constructor_exists():
    assert callable(cobol_water_RepositoryParagraphWater.__init__)


def test_cobol_water_repositoryparagraphwater_constructor_args():
    sig = inspect.signature(cobol_water_RepositoryParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_incompleteelement_is_not_abstract():
    assert not inspect.isabstract(cobol_water_IncompleteElement)


def test_cobol_water_incompleteelement_constructor_exists():
    assert callable(cobol_water_IncompleteElement.__init__)


def test_cobol_water_incompleteelement_constructor_args():
    sig = inspect.signature(cobol_water_IncompleteElement.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_cobol_labels_procedurerangelabel_is_not_abstract():
    assert not inspect.isabstract(cobol_labels_ProcedureRangeLabel)


def test_cobol_labels_procedurerangelabel_constructor_exists():
    assert callable(cobol_labels_ProcedureRangeLabel.__init__)


def test_cobol_labels_procedurerangelabel_constructor_args():
    sig = inspect.signature(cobol_labels_ProcedureRangeLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol_labels_stoplabel_is_not_abstract():
    assert not inspect.isabstract(cobol_labels_StopLabel)


def test_cobol_labels_stoplabel_constructor_exists():
    assert callable(cobol_labels_StopLabel.__init__)


def test_cobol_labels_stoplabel_constructor_args():
    sig = inspect.signature(cobol_labels_StopLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol_ios_iodirectives_is_not_abstract():
    assert not inspect.isabstract(cobol_ios_IODirectives)


def test_cobol_ios_iodirectives_constructor_exists():
    assert callable(cobol_ios_IODirectives.__init__)


def test_cobol_ios_iodirectives_constructor_args():
    sig = inspect.signature(cobol_ios_IODirectives.__init__)
    params = list(sig.parameters.keys())



def test_ios_outputdirective_is_not_abstract():
    assert not inspect.isabstract(ios_OutputDirective)


def test_ios_outputdirective_constructor_exists():
    assert callable(ios_OutputDirective.__init__)


def test_ios_outputdirective_constructor_args():
    sig = inspect.signature(ios_OutputDirective.__init__)
    params = list(sig.parameters.keys())



def test_ios_filedirective_is_not_abstract():
    assert not inspect.isabstract(ios_FileDirective)


def test_ios_filedirective_constructor_exists():
    assert callable(ios_FileDirective.__init__)


def test_ios_filedirective_constructor_args():
    sig = inspect.signature(ios_FileDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol_ios_outputfile_is_not_abstract():
    assert not inspect.isabstract(cobol_ios_OutputFile)


def test_cobol_ios_outputfile_constructor_exists():
    assert callable(cobol_ios_OutputFile.__init__)


def test_cobol_ios_outputfile_constructor_args():
    sig = inspect.signature(cobol_ios_OutputFile.__init__)
    params = list(sig.parameters.keys())



def test_iodirectives_is_not_abstract():
    assert not inspect.isabstract(IODirectives)


def test_iodirectives_constructor_exists():
    assert callable(IODirectives.__init__)


def test_iodirectives_constructor_args():
    sig = inspect.signature(IODirectives.__init__)
    params = list(sig.parameters.keys())



def test_cobol_ios_outputdirective_is_not_abstract():
    assert not inspect.isabstract(cobol_ios_OutputDirective)


def test_cobol_ios_outputdirective_constructor_exists():
    assert callable(cobol_ios_OutputDirective.__init__)


def test_cobol_ios_outputdirective_constructor_args():
    sig = inspect.signature(cobol_ios_OutputDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol_ios_filedirective_is_not_abstract():
    assert not inspect.isabstract(cobol_ios_FileDirective)


def test_cobol_ios_filedirective_constructor_exists():
    assert callable(cobol_ios_FileDirective.__init__)


def test_cobol_ios_filedirective_constructor_args():
    sig = inspect.signature(cobol_ios_FileDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol_ios_proceduredirective_is_not_abstract():
    assert not inspect.isabstract(cobol_ios_ProcedureDirective)


def test_cobol_ios_proceduredirective_constructor_exists():
    assert callable(cobol_ios_ProcedureDirective.__init__)


def test_cobol_ios_proceduredirective_constructor_args():
    sig = inspect.signature(cobol_ios_ProcedureDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol_ios_inputdirective_is_not_abstract():
    assert not inspect.isabstract(cobol_ios_InputDirective)


def test_cobol_ios_inputdirective_constructor_exists():
    assert callable(cobol_ios_InputDirective.__init__)


def test_cobol_ios_inputdirective_constructor_args():
    sig = inspect.signature(cobol_ios_InputDirective.__init__)
    params = list(sig.parameters.keys())



def test_ios_proceduredirective_is_not_abstract():
    assert not inspect.isabstract(ios_ProcedureDirective)


def test_ios_proceduredirective_constructor_exists():
    assert callable(ios_ProcedureDirective.__init__)


def test_ios_proceduredirective_constructor_args():
    sig = inspect.signature(ios_ProcedureDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol_ios_outputprocedure_is_not_abstract():
    assert not inspect.isabstract(cobol_ios_OutputProcedure)


def test_cobol_ios_outputprocedure_constructor_exists():
    assert callable(cobol_ios_OutputProcedure.__init__)


def test_cobol_ios_outputprocedure_constructor_args():
    sig = inspect.signature(cobol_ios_OutputProcedure.__init__)
    params = list(sig.parameters.keys())



def test_ios_inputdirective_is_not_abstract():
    assert not inspect.isabstract(ios_InputDirective)


def test_ios_inputdirective_constructor_exists():
    assert callable(ios_InputDirective.__init__)


def test_ios_inputdirective_constructor_args():
    sig = inspect.signature(ios_InputDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol_ios_inputfile_is_not_abstract():
    assert not inspect.isabstract(cobol_ios_InputFile)


def test_cobol_ios_inputfile_constructor_exists():
    assert callable(cobol_ios_InputFile.__init__)


def test_cobol_ios_inputfile_constructor_args():
    sig = inspect.signature(cobol_ios_InputFile.__init__)
    params = list(sig.parameters.keys())



def test_cobol_ios_inputprocedure_is_not_abstract():
    assert not inspect.isabstract(cobol_ios_InputProcedure)


def test_cobol_ios_inputprocedure_constructor_exists():
    assert callable(cobol_ios_InputProcedure.__init__)


def test_cobol_ios_inputprocedure_constructor_args():
    sig = inspect.signature(cobol_ios_InputProcedure.__init__)
    params = list(sig.parameters.keys())



def test_cobol_identifiers_referencemodifier_is_not_abstract():
    assert not inspect.isabstract(cobol_identifiers_ReferenceModifier)


def test_cobol_identifiers_referencemodifier_constructor_exists():
    assert callable(cobol_identifiers_ReferenceModifier.__init__)


def test_cobol_identifiers_referencemodifier_constructor_args():
    sig = inspect.signature(cobol_identifiers_ReferenceModifier.__init__)
    params = list(sig.parameters.keys())



def test_directsubscript_is_not_abstract():
    assert not inspect.isabstract(DirectSubscript)


def test_directsubscript_constructor_exists():
    assert callable(DirectSubscript.__init__)


def test_directsubscript_constructor_args():
    sig = inspect.signature(DirectSubscript.__init__)
    params = list(sig.parameters.keys())



def test_cobol_identifiers_all_is_not_abstract():
    assert not inspect.isabstract(cobol_identifiers_All)


def test_cobol_identifiers_all_constructor_exists():
    assert callable(cobol_identifiers_All.__init__)


def test_cobol_identifiers_all_constructor_args():
    sig = inspect.signature(cobol_identifiers_All.__init__)
    params = list(sig.parameters.keys())



def test_identificationdivisionwater_is_not_abstract():
    assert not inspect.isabstract(IdentificationDivisionWater)


def test_identificationdivisionwater_constructor_exists():
    assert callable(IdentificationDivisionWater.__init__)


def test_identificationdivisionwater_constructor_args():
    sig = inspect.signature(IdentificationDivisionWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_programdescription_is_not_abstract():
    assert not inspect.isabstract(cobol_water_ProgramDescription)


def test_cobol_water_programdescription_constructor_exists():
    assert callable(cobol_water_ProgramDescription.__init__)


def test_cobol_water_programdescription_constructor_args():
    sig = inspect.signature(cobol_water_ProgramDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_programdescription_has_value():
    assert hasattr(cobol_water_ProgramDescription, "value")
    descriptor = None
    for klass in cobol_water_ProgramDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_subscript_is_not_abstract():
    assert not inspect.isabstract(Subscript)


def test_subscript_constructor_exists():
    assert callable(Subscript.__init__)


def test_subscript_constructor_args():
    sig = inspect.signature(Subscript.__init__)
    params = list(sig.parameters.keys())



def test_cobol_identifiers_relativesubscript_is_not_abstract():
    assert not inspect.isabstract(cobol_identifiers_RelativeSubscript)


def test_cobol_identifiers_relativesubscript_constructor_exists():
    assert callable(cobol_identifiers_RelativeSubscript.__init__)


def test_cobol_identifiers_relativesubscript_constructor_args():
    sig = inspect.signature(cobol_identifiers_RelativeSubscript.__init__)
    params = list(sig.parameters.keys())



def test_cobol_identifiers_directsubscript_is_not_abstract():
    assert not inspect.isabstract(cobol_identifiers_DirectSubscript)


def test_cobol_identifiers_directsubscript_constructor_exists():
    assert callable(cobol_identifiers_DirectSubscript.__init__)


def test_cobol_identifiers_directsubscript_constructor_args():
    sig = inspect.signature(cobol_identifiers_DirectSubscript.__init__)
    params = list(sig.parameters.keys())



def test_identifiers_identifier_is_not_abstract():
    assert not inspect.isabstract(identifiers_Identifier)


def test_identifiers_identifier_constructor_exists():
    assert callable(identifiers_Identifier.__init__)


def test_identifiers_identifier_constructor_args():
    sig = inspect.signature(identifiers_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_referencemodifier_is_not_abstract():
    assert not inspect.isabstract(ReferenceModifier)


def test_referencemodifier_constructor_exists():
    assert callable(ReferenceModifier.__init__)


def test_referencemodifier_constructor_args():
    sig = inspect.signature(ReferenceModifier.__init__)
    params = list(sig.parameters.keys())



def test_water_sortphrasewater_is_not_abstract():
    assert not inspect.isabstract(water_SortPhraseWater)


def test_water_sortphrasewater_constructor_exists():
    assert callable(water_SortPhraseWater.__init__)


def test_water_sortphrasewater_constructor_args():
    sig = inspect.signature(water_SortPhraseWater.__init__)
    params = list(sig.parameters.keys())



def test_water_datadescriptorwater_is_not_abstract():
    assert not inspect.isabstract(water_DataDescriptorWater)


def test_water_datadescriptorwater_constructor_exists():
    assert callable(water_DataDescriptorWater.__init__)


def test_water_datadescriptorwater_constructor_args():
    sig = inspect.signature(water_DataDescriptorWater.__init__)
    params = list(sig.parameters.keys())



def test_statements_statement_is_not_abstract():
    assert not inspect.isabstract(statements_Statement)


def test_statements_statement_constructor_exists():
    assert callable(statements_Statement.__init__)


def test_statements_statement_constructor_args():
    sig = inspect.signature(statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_water_usestatementwater_is_not_abstract():
    assert not inspect.isabstract(water_UseStatementWater)


def test_water_usestatementwater_constructor_exists():
    assert callable(water_UseStatementWater.__init__)


def test_water_usestatementwater_constructor_args():
    sig = inspect.signature(water_UseStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_dataitem_is_not_abstract():
    assert not inspect.isabstract(DataItem)


def test_dataitem_constructor_exists():
    assert callable(DataItem.__init__)


def test_dataitem_constructor_args():
    sig = inspect.signature(DataItem.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_conditionname_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_ConditionName)


def test_cobol_dataitems_conditionname_constructor_exists():
    assert callable(cobol_dataitems_ConditionName.__init__)


def test_cobol_dataitems_conditionname_constructor_args():
    sig = inspect.signature(cobol_dataitems_ConditionName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_recordname_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_RecordName)


def test_cobol_dataitems_recordname_constructor_exists():
    assert callable(cobol_dataitems_RecordName.__init__)


def test_cobol_dataitems_recordname_constructor_args():
    sig = inspect.signature(cobol_dataitems_RecordName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_dataname_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_DataName)


def test_cobol_dataitems_dataname_constructor_exists():
    assert callable(cobol_dataitems_DataName.__init__)


def test_cobol_dataitems_dataname_constructor_args():
    sig = inspect.signature(cobol_dataitems_DataName.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_environmentdivisionsection_is_not_abstract():
    assert not inspect.isabstract(EnvironmentDivisionSection)


def test_environmentdivisionsection_constructor_exists():
    assert callable(EnvironmentDivisionSection.__init__)


def test_environmentdivisionsection_constructor_args():
    sig = inspect.signature(EnvironmentDivisionSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sections_configurationsection_is_not_abstract():
    assert not inspect.isabstract(cobol_sections_ConfigurationSection)


def test_cobol_sections_configurationsection_constructor_exists():
    assert callable(cobol_sections_ConfigurationSection.__init__)


def test_cobol_sections_configurationsection_constructor_args():
    sig = inspect.signature(cobol_sections_ConfigurationSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sections_iosection_is_not_abstract():
    assert not inspect.isabstract(cobol_sections_IOSection)


def test_cobol_sections_iosection_constructor_exists():
    assert callable(cobol_sections_IOSection.__init__)


def test_cobol_sections_iosection_constructor_args():
    sig = inspect.signature(cobol_sections_IOSection.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticoperand_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperand)


def test_arithmeticoperand_constructor_exists():
    assert callable(ArithmeticOperand.__init__)


def test_arithmeticoperand_constructor_args():
    sig = inspect.signature(ArithmeticOperand.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operands_roundedidentifier_is_not_abstract():
    assert not inspect.isabstract(cobol_operands_RoundedIdentifier)


def test_cobol_operands_roundedidentifier_constructor_exists():
    assert callable(cobol_operands_RoundedIdentifier.__init__)


def test_cobol_operands_roundedidentifier_constructor_args():
    sig = inspect.signature(cobol_operands_RoundedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_water_sqlstatementwater_is_not_abstract():
    assert not inspect.isabstract(water_SQLStatementWater)


def test_water_sqlstatementwater_constructor_exists():
    assert callable(water_SQLStatementWater.__init__)


def test_water_sqlstatementwater_constructor_args():
    sig = inspect.signature(water_SQLStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_water_identificationdivisionwater_is_not_abstract():
    assert not inspect.isabstract(water_IdentificationDivisionWater)


def test_water_identificationdivisionwater_constructor_exists():
    assert callable(water_IdentificationDivisionWater.__init__)


def test_water_identificationdivisionwater_constructor_args():
    sig = inspect.signature(water_IdentificationDivisionWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_dot_is_not_abstract():
    assert not inspect.isabstract(cobol_water_Dot)


def test_cobol_water_dot_constructor_exists():
    assert callable(cobol_water_Dot.__init__)


def test_cobol_water_dot_constructor_args():
    sig = inspect.signature(cobol_water_Dot.__init__)
    params = list(sig.parameters.keys())



def test_water_repositoryparagraphwater_is_not_abstract():
    assert not inspect.isabstract(water_RepositoryParagraphWater)


def test_water_repositoryparagraphwater_constructor_exists():
    assert callable(water_RepositoryParagraphWater.__init__)


def test_water_repositoryparagraphwater_constructor_args():
    sig = inspect.signature(water_RepositoryParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_water_acceptstatementwater_is_not_abstract():
    assert not inspect.isabstract(water_AcceptStatementWater)


def test_water_acceptstatementwater_constructor_exists():
    assert callable(water_AcceptStatementWater.__init__)


def test_water_acceptstatementwater_constructor_args():
    sig = inspect.signature(water_AcceptStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_identifiers_subscript_is_not_abstract():
    assert not inspect.isabstract(cobol_identifiers_Subscript)


def test_cobol_identifiers_subscript_constructor_exists():
    assert callable(cobol_identifiers_Subscript.__init__)


def test_cobol_identifiers_subscript_constructor_args():
    sig = inspect.signature(cobol_identifiers_Subscript.__init__)
    params = list(sig.parameters.keys())



def test_varyinguntilcondition_is_not_abstract():
    assert not inspect.isabstract(VaryingUntilCondition)


def test_varyinguntilcondition_constructor_exists():
    assert callable(VaryingUntilCondition.__init__)


def test_varyinguntilcondition_constructor_args():
    sig = inspect.signature(VaryingUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_afteruntilcondition_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_AfterUntilCondition)


def test_cobol_statements_afteruntilcondition_constructor_exists():
    assert callable(cobol_statements_AfterUntilCondition.__init__)


def test_cobol_statements_afteruntilcondition_constructor_args():
    sig = inspect.signature(cobol_statements_AfterUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_qualifier_is_not_abstract():
    assert not inspect.isabstract(Qualifier)


def test_qualifier_constructor_exists():
    assert callable(Qualifier.__init__)


def test_qualifier_constructor_args():
    sig = inspect.signature(Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_conditional_is_not_abstract():
    assert not inspect.isabstract(Conditional)


def test_conditional_constructor_exists():
    assert callable(Conditional.__init__)


def test_conditional_constructor_args():
    sig = inspect.signature(Conditional.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_varyinguntilcondition_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_VaryingUntilCondition)


def test_cobol_statements_varyinguntilcondition_constructor_exists():
    assert callable(cobol_statements_VaryingUntilCondition.__init__)


def test_cobol_statements_varyinguntilcondition_constructor_args():
    sig = inspect.signature(cobol_statements_VaryingUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_tallying_is_not_abstract():
    assert not inspect.isabstract(Tallying)


def test_tallying_constructor_exists():
    assert callable(Tallying.__init__)


def test_tallying_constructor_args():
    sig = inspect.signature(Tallying.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_anycharacter_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_AnyCharacter)


def test_cobol_strings_anycharacter_constructor_exists():
    assert callable(cobol_strings_AnyCharacter.__init__)


def test_cobol_strings_anycharacter_constructor_args():
    sig = inspect.signature(cobol_strings_AnyCharacter.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_specificcharacter_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_SpecificCharacter)


def test_cobol_strings_specificcharacter_constructor_exists():
    assert callable(cobol_strings_SpecificCharacter.__init__)


def test_cobol_strings_specificcharacter_constructor_args():
    sig = inspect.signature(cobol_strings_SpecificCharacter.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_tallyingin_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_TallyingIn)


def test_cobol_statements_tallyingin_constructor_exists():
    assert callable(cobol_statements_TallyingIn.__init__)


def test_cobol_statements_tallyingin_constructor_args():
    sig = inspect.signature(cobol_statements_TallyingIn.__init__)
    params = list(sig.parameters.keys())



def test_incompleteelement_is_not_abstract():
    assert not inspect.isabstract(IncompleteElement)


def test_incompleteelement_constructor_exists():
    assert callable(IncompleteElement.__init__)


def test_incompleteelement_constructor_args():
    sig = inspect.signature(IncompleteElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_files_selectstatement_is_not_abstract():
    assert not inspect.isabstract(cobol_files_SelectStatement)


def test_cobol_files_selectstatement_constructor_exists():
    assert callable(cobol_files_SelectStatement.__init__)


def test_cobol_files_selectstatement_constructor_args():
    sig = inspect.signature(cobol_files_SelectStatement.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"
    assert "externalFileNames" in params, "Missing parameter 'externalFileNames'"

def test_cobol_files_selectstatement_has_isOptional():
    assert hasattr(cobol_files_SelectStatement, "isOptional")
    descriptor = None
    for klass in cobol_files_SelectStatement.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)

def test_cobol_files_selectstatement_has_externalFileNames():
    assert hasattr(cobol_files_SelectStatement, "externalFileNames")
    descriptor = None
    for klass in cobol_files_SelectStatement.__mro__:
        if "externalFileNames" in klass.__dict__:
            descriptor = klass.__dict__["externalFileNames"]
            break
    assert isinstance(descriptor, property)



def test_cobol_statements_iofile_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_IOFile)


def test_cobol_statements_iofile_constructor_exists():
    assert callable(cobol_statements_IOFile.__init__)


def test_cobol_statements_iofile_constructor_args():
    sig = inspect.signature(cobol_statements_IOFile.__init__)
    params = list(sig.parameters.keys())



def test_iofile_is_not_abstract():
    assert not inspect.isabstract(IOFile)


def test_iofile_constructor_exists():
    assert callable(IOFile.__init__)


def test_iofile_constructor_args():
    sig = inspect.signature(IOFile.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_iofiledescriptor_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_IOFileDescriptor)


def test_cobol_statements_iofiledescriptor_constructor_exists():
    assert callable(cobol_statements_IOFileDescriptor.__init__)


def test_cobol_statements_iofiledescriptor_constructor_args():
    sig = inspect.signature(cobol_statements_IOFileDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cobol_statements_iofiledescriptor_has_type():
    assert hasattr(cobol_statements_IOFileDescriptor, "type")
    descriptor = None
    for klass in cobol_statements_IOFileDescriptor.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_iofiledescriptor_is_not_abstract():
    assert not inspect.isabstract(IOFileDescriptor)


def test_iofiledescriptor_constructor_exists():
    assert callable(IOFileDescriptor.__init__)


def test_iofiledescriptor_constructor_args():
    sig = inspect.signature(IOFileDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_iostatement_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_IOStatement)


def test_cobol_statements_iostatement_constructor_exists():
    assert callable(cobol_statements_IOStatement.__init__)


def test_cobol_statements_iostatement_constructor_args():
    sig = inspect.signature(cobol_statements_IOStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_keydescriptor_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_KeyDescriptor)


def test_cobol_statements_keydescriptor_constructor_exists():
    assert callable(cobol_statements_KeyDescriptor.__init__)


def test_cobol_statements_keydescriptor_constructor_args():
    sig = inspect.signature(cobol_statements_KeyDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_cobol_statements_keydescriptor_has_order():
    assert hasattr(cobol_statements_KeyDescriptor, "order")
    descriptor = None
    for klass in cobol_statements_KeyDescriptor.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_statements_varyinguntilcondition_is_not_abstract():
    assert not inspect.isabstract(statements_VaryingUntilCondition)


def test_statements_varyinguntilcondition_constructor_exists():
    assert callable(statements_VaryingUntilCondition.__init__)


def test_statements_varyinguntilcondition_constructor_args():
    sig = inspect.signature(statements_VaryingUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_release_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Release)


def test_cobol_statements_release_constructor_exists():
    assert callable(cobol_statements_Release.__init__)


def test_cobol_statements_release_constructor_args():
    sig = inspect.signature(cobol_statements_Release.__init__)
    params = list(sig.parameters.keys())



def test_statements_performfixedtimes_is_not_abstract():
    assert not inspect.isabstract(statements_PerformFixedTimes)


def test_statements_performfixedtimes_constructor_exists():
    assert callable(statements_PerformFixedTimes.__init__)


def test_statements_performfixedtimes_constructor_args():
    sig = inspect.signature(statements_PerformFixedTimes.__init__)
    params = list(sig.parameters.keys())



def test_statements_fileiostatement_is_not_abstract():
    assert not inspect.isabstract(statements_FileIOStatement)


def test_statements_fileiostatement_constructor_exists():
    assert callable(statements_FileIOStatement.__init__)


def test_statements_fileiostatement_constructor_args():
    sig = inspect.signature(statements_FileIOStatement.__init__)
    params = list(sig.parameters.keys())



def test_keydescriptor_is_not_abstract():
    assert not inspect.isabstract(KeyDescriptor)


def test_keydescriptor_constructor_exists():
    assert callable(KeyDescriptor.__init__)


def test_keydescriptor_constructor_args():
    sig = inspect.signature(KeyDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_outputdirective_is_not_abstract():
    assert not inspect.isabstract(OutputDirective)


def test_outputdirective_constructor_exists():
    assert callable(OutputDirective.__init__)


def test_outputdirective_constructor_args():
    sig = inspect.signature(OutputDirective.__init__)
    params = list(sig.parameters.keys())



def test_inputdirective_is_not_abstract():
    assert not inspect.isabstract(InputDirective)


def test_inputdirective_constructor_exists():
    assert callable(InputDirective.__init__)


def test_inputdirective_constructor_args():
    sig = inspect.signature(InputDirective.__init__)
    params = list(sig.parameters.keys())



def test_statements_performprocedure_is_not_abstract():
    assert not inspect.isabstract(statements_PerformProcedure)


def test_statements_performprocedure_constructor_exists():
    assert callable(statements_PerformProcedure.__init__)


def test_statements_performprocedure_constructor_args():
    sig = inspect.signature(statements_PerformProcedure.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_performprocedurefixedtimes_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_PerformProcedureFixedTimes)


def test_cobol_statements_performprocedurefixedtimes_constructor_exists():
    assert callable(cobol_statements_PerformProcedureFixedTimes.__init__)


def test_cobol_statements_performprocedurefixedtimes_constructor_args():
    sig = inspect.signature(cobol_statements_PerformProcedureFixedTimes.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_fileiostatement_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_FileIOStatement)


def test_cobol_statements_fileiostatement_constructor_exists():
    assert callable(cobol_statements_FileIOStatement.__init__)


def test_cobol_statements_fileiostatement_constructor_args():
    sig = inspect.signature(cobol_statements_FileIOStatement.__init__)
    params = list(sig.parameters.keys())



def test_statements_performnestedstatement_is_not_abstract():
    assert not inspect.isabstract(statements_PerformNestedStatement)


def test_statements_performnestedstatement_constructor_exists():
    assert callable(statements_PerformNestedStatement.__init__)


def test_statements_performnestedstatement_constructor_args():
    sig = inspect.signature(statements_PerformNestedStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_performnestedstatementfixedtimes_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_PerformNestedStatementFixedTimes)


def test_cobol_statements_performnestedstatementfixedtimes_constructor_exists():
    assert callable(cobol_statements_PerformNestedStatementFixedTimes.__init__)


def test_cobol_statements_performnestedstatementfixedtimes_constructor_args():
    sig = inspect.signature(cobol_statements_PerformNestedStatementFixedTimes.__init__)
    params = list(sig.parameters.keys())



def test_afteruntilcondition_is_not_abstract():
    assert not inspect.isabstract(AfterUntilCondition)


def test_afteruntilcondition_constructor_exists():
    assert callable(AfterUntilCondition.__init__)


def test_afteruntilcondition_constructor_args():
    sig = inspect.signature(AfterUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_statements_performuntilcondition_is_not_abstract():
    assert not inspect.isabstract(statements_PerformUntilCondition)


def test_statements_performuntilcondition_constructor_exists():
    assert callable(statements_PerformUntilCondition.__init__)


def test_statements_performuntilcondition_constructor_args():
    sig = inspect.signature(statements_PerformUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_performnestedstatementuntilcondition_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_PerformNestedStatementUntilCondition)


def test_cobol_statements_performnestedstatementuntilcondition_constructor_exists():
    assert callable(cobol_statements_PerformNestedStatementUntilCondition.__init__)


def test_cobol_statements_performnestedstatementuntilcondition_constructor_args():
    sig = inspect.signature(cobol_statements_PerformNestedStatementUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_performprocedureuntilcondition_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_PerformProcedureUntilCondition)


def test_cobol_statements_performprocedureuntilcondition_constructor_exists():
    assert callable(cobol_statements_PerformProcedureUntilCondition.__init__)


def test_cobol_statements_performprocedureuntilcondition_constructor_args():
    sig = inspect.signature(cobol_statements_PerformProcedureUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_tallyingin_is_not_abstract():
    assert not inspect.isabstract(TallyingIn)


def test_tallyingin_constructor_exists():
    assert callable(TallyingIn.__init__)


def test_tallyingin_constructor_args():
    sig = inspect.signature(TallyingIn.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_switchstatus_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_SwitchStatus)


def test_cobol_statements_switchstatus_constructor_exists():
    assert callable(cobol_statements_SwitchStatus.__init__)


def test_cobol_statements_switchstatus_constructor_args():
    sig = inspect.signature(cobol_statements_SwitchStatus.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_cobol_statements_switchstatus_has_status():
    assert hasattr(cobol_statements_SwitchStatus, "status")
    descriptor = None
    for klass in cobol_statements_SwitchStatus.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_write_is_not_abstract():
    assert not inspect.isabstract(Write)


def test_write_constructor_exists():
    assert callable(Write.__init__)


def test_write_constructor_args():
    sig = inspect.signature(Write.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_rewrite_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Rewrite)


def test_cobol_statements_rewrite_constructor_exists():
    assert callable(cobol_statements_Rewrite.__init__)


def test_cobol_statements_rewrite_constructor_args():
    sig = inspect.signature(cobol_statements_Rewrite.__init__)
    params = list(sig.parameters.keys())



def test_mnemonicnamereference_is_not_abstract():
    assert not inspect.isabstract(MnemonicNameReference)


def test_mnemonicnamereference_constructor_exists():
    assert callable(MnemonicNameReference.__init__)


def test_mnemonicnamereference_constructor_args():
    sig = inspect.signature(MnemonicNameReference.__init__)
    params = list(sig.parameters.keys())



def test_integerliteral_is_not_abstract():
    assert not inspect.isabstract(IntegerLiteral)


def test_integerliteral_constructor_exists():
    assert callable(IntegerLiteral.__init__)


def test_integerliteral_constructor_args():
    sig = inspect.signature(IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_searchstatement_is_not_abstract():
    assert not inspect.isabstract(SearchStatement)


def test_searchstatement_constructor_exists():
    assert callable(SearchStatement.__init__)


def test_searchstatement_constructor_args():
    sig = inspect.signature(SearchStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_binarysearch_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_BinarySearch)


def test_cobol_statements_binarysearch_constructor_exists():
    assert callable(cobol_statements_BinarySearch.__init__)


def test_cobol_statements_binarysearch_constructor_args():
    sig = inspect.signature(cobol_statements_BinarySearch.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_serialsearch_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_SerialSearch)


def test_cobol_statements_serialsearch_constructor_exists():
    assert callable(cobol_statements_SerialSearch.__init__)


def test_cobol_statements_serialsearch_constructor_args():
    sig = inspect.signature(cobol_statements_SerialSearch.__init__)
    params = list(sig.parameters.keys())



def test_normalevaluatecase_is_not_abstract():
    assert not inspect.isabstract(NormalEvaluateCase)


def test_normalevaluatecase_constructor_exists():
    assert callable(NormalEvaluateCase.__init__)


def test_normalevaluatecase_constructor_args():
    sig = inspect.signature(NormalEvaluateCase.__init__)
    params = list(sig.parameters.keys())



def test_replacement_is_not_abstract():
    assert not inspect.isabstract(Replacement)


def test_replacement_constructor_exists():
    assert callable(Replacement.__init__)


def test_replacement_constructor_args():
    sig = inspect.signature(Replacement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_anycharacterbyspecificcharacter_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_AnyCharacterBySpecificCharacter)


def test_cobol_strings_anycharacterbyspecificcharacter_constructor_exists():
    assert callable(cobol_strings_AnyCharacterBySpecificCharacter.__init__)


def test_cobol_strings_anycharacterbyspecificcharacter_constructor_args():
    sig = inspect.signature(cobol_strings_AnyCharacterBySpecificCharacter.__init__)
    params = list(sig.parameters.keys())



def test_cobol_strings_specificcharacterbyspecificcharacter_is_not_abstract():
    assert not inspect.isabstract(cobol_strings_SpecificCharacterBySpecificCharacter)


def test_cobol_strings_specificcharacterbyspecificcharacter_constructor_exists():
    assert callable(cobol_strings_SpecificCharacterBySpecificCharacter.__init__)


def test_cobol_strings_specificcharacterbyspecificcharacter_constructor_args():
    sig = inspect.signature(cobol_strings_SpecificCharacterBySpecificCharacter.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_initialize_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Initialize)


def test_cobol_statements_initialize_constructor_exists():
    assert callable(cobol_statements_Initialize.__init__)


def test_cobol_statements_initialize_constructor_args():
    sig = inspect.signature(cobol_statements_Initialize.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_inspect_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Inspect)


def test_cobol_statements_inspect_constructor_exists():
    assert callable(cobol_statements_Inspect.__init__)


def test_cobol_statements_inspect_constructor_args():
    sig = inspect.signature(cobol_statements_Inspect.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_replace_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Replace)


def test_cobol_statements_replace_constructor_exists():
    assert callable(cobol_statements_Replace.__init__)


def test_cobol_statements_replace_constructor_args():
    sig = inspect.signature(cobol_statements_Replace.__init__)
    params = list(sig.parameters.keys())
    assert "replaceSwitch" in params, "Missing parameter 'replaceSwitch'"

def test_cobol_statements_replace_has_replaceSwitch():
    assert hasattr(cobol_statements_Replace, "replaceSwitch")
    descriptor = None
    for klass in cobol_statements_Replace.__mro__:
        if "replaceSwitch" in klass.__dict__:
            descriptor = klass.__dict__["replaceSwitch"]
            break
    assert isinstance(descriptor, property)



def test_nestedstatement_is_not_abstract():
    assert not inspect.isabstract(NestedStatement)


def test_nestedstatement_constructor_exists():
    assert callable(NestedStatement.__init__)


def test_nestedstatement_constructor_args():
    sig = inspect.signature(NestedStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_handler_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_Handler)


def test_cobol_handlers_handler_constructor_exists():
    assert callable(cobol_handlers_Handler.__init__)


def test_cobol_handlers_handler_constructor_args():
    sig = inspect.signature(cobol_handlers_Handler.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_evaluatecase_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_EvaluateCase)


def test_cobol_statements_evaluatecase_constructor_exists():
    assert callable(cobol_statements_EvaluateCase.__init__)


def test_cobol_statements_evaluatecase_constructor_args():
    sig = inspect.signature(cobol_statements_EvaluateCase.__init__)
    params = list(sig.parameters.keys())



def test_expressionlist_is_not_abstract():
    assert not inspect.isabstract(ExpressionList)


def test_expressionlist_constructor_exists():
    assert callable(ExpressionList.__init__)


def test_expressionlist_constructor_args():
    sig = inspect.signature(ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_evaluatecase_is_not_abstract():
    assert not inspect.isabstract(EvaluateCase)


def test_evaluatecase_constructor_exists():
    assert callable(EvaluateCase.__init__)


def test_evaluatecase_constructor_args():
    sig = inspect.signature(EvaluateCase.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_otherevaluatecase_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_OtherEvaluateCase)


def test_cobol_statements_otherevaluatecase_constructor_exists():
    assert callable(cobol_statements_OtherEvaluateCase.__init__)


def test_cobol_statements_otherevaluatecase_constructor_args():
    sig = inspect.signature(cobol_statements_OtherEvaluateCase.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_normalevaluatecase_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_NormalEvaluateCase)


def test_cobol_statements_normalevaluatecase_constructor_exists():
    assert callable(cobol_statements_NormalEvaluateCase.__init__)


def test_cobol_statements_normalevaluatecase_constructor_args():
    sig = inspect.signature(cobol_statements_NormalEvaluateCase.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_evaluate_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Evaluate)


def test_cobol_statements_evaluate_constructor_exists():
    assert callable(cobol_statements_Evaluate.__init__)


def test_cobol_statements_evaluate_constructor_args():
    sig = inspect.signature(cobol_statements_Evaluate.__init__)
    params = list(sig.parameters.keys())



def test_splittedstring_is_not_abstract():
    assert not inspect.isabstract(SplittedString)


def test_splittedstring_constructor_exists():
    assert callable(SplittedString.__init__)


def test_splittedstring_constructor_args():
    sig = inspect.signature(SplittedString.__init__)
    params = list(sig.parameters.keys())



def test_setstatement_is_not_abstract():
    assert not inspect.isabstract(SetStatement)


def test_setstatement_constructor_exists():
    assert callable(SetStatement.__init__)


def test_setstatement_constructor_args():
    sig = inspect.signature(SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_set_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Set)


def test_cobol_statements_set_constructor_exists():
    assert callable(cobol_statements_Set.__init__)


def test_cobol_statements_set_constructor_args():
    sig = inspect.signature(cobol_statements_Set.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_setswitches_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_SetSwitches)


def test_cobol_statements_setswitches_constructor_exists():
    assert callable(cobol_statements_SetSwitches.__init__)


def test_cobol_statements_setswitches_constructor_args():
    sig = inspect.signature(cobol_statements_SetSwitches.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_setstatement_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_SetStatement)


def test_cobol_statements_setstatement_constructor_exists():
    assert callable(cobol_statements_SetStatement.__init__)


def test_cobol_statements_setstatement_constructor_args():
    sig = inspect.signature(cobol_statements_SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_filenamereference_is_not_abstract():
    assert not inspect.isabstract(FileNameReference)


def test_filenamereference_constructor_exists():
    assert callable(FileNameReference.__init__)


def test_filenamereference_constructor_args():
    sig = inspect.signature(FileNameReference.__init__)
    params = list(sig.parameters.keys())



def test_handler_is_not_abstract():
    assert not inspect.isabstract(Handler)


def test_handler_constructor_exists():
    assert callable(Handler.__init__)


def test_handler_constructor_args():
    sig = inspect.signature(Handler.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_onexception_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_OnException)


def test_cobol_handlers_onexception_constructor_exists():
    assert callable(cobol_handlers_OnException.__init__)


def test_cobol_handlers_onexception_constructor_args():
    sig = inspect.signature(cobol_handlers_OnException.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_atendofpage_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_AtEndOfPage)


def test_cobol_handlers_atendofpage_constructor_exists():
    assert callable(cobol_handlers_AtEndOfPage.__init__)


def test_cobol_handlers_atendofpage_constructor_args():
    sig = inspect.signature(cobol_handlers_AtEndOfPage.__init__)
    params = list(sig.parameters.keys())
    assert "eop" in params, "Missing parameter 'eop'"

def test_cobol_handlers_atendofpage_has_eop():
    assert hasattr(cobol_handlers_AtEndOfPage, "eop")
    descriptor = None
    for klass in cobol_handlers_AtEndOfPage.__mro__:
        if "eop" in klass.__dict__:
            descriptor = klass.__dict__["eop"]
            break
    assert isinstance(descriptor, property)



def test_cobol_handlers_onsizeerror_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_OnSizeError)


def test_cobol_handlers_onsizeerror_constructor_exists():
    assert callable(cobol_handlers_OnSizeError.__init__)


def test_cobol_handlers_onsizeerror_constructor_args():
    sig = inspect.signature(cobol_handlers_OnSizeError.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_atend_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_AtEnd)


def test_cobol_handlers_atend_constructor_exists():
    assert callable(cobol_handlers_AtEnd.__init__)


def test_cobol_handlers_atend_constructor_args():
    sig = inspect.signature(cobol_handlers_AtEnd.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_noterrorhandler_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_NotErrorHandler)


def test_cobol_handlers_noterrorhandler_constructor_exists():
    assert callable(cobol_handlers_NotErrorHandler.__init__)


def test_cobol_handlers_noterrorhandler_constructor_args():
    sig = inspect.signature(cobol_handlers_NotErrorHandler.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_invalidkey_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_InvalidKey)


def test_cobol_handlers_invalidkey_constructor_exists():
    assert callable(cobol_handlers_InvalidKey.__init__)


def test_cobol_handlers_invalidkey_constructor_args():
    sig = inspect.signature(cobol_handlers_InvalidKey.__init__)
    params = list(sig.parameters.keys())



def test_cobol_handlers_onoverflow_is_not_abstract():
    assert not inspect.isabstract(cobol_handlers_OnOverflow)


def test_cobol_handlers_onoverflow_constructor_exists():
    assert callable(cobol_handlers_OnOverflow.__init__)


def test_cobol_handlers_onoverflow_constructor_args():
    sig = inspect.signature(cobol_handlers_OnOverflow.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_errorhandled_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_ErrorHandled)


def test_cobol_statements_errorhandled_constructor_exists():
    assert callable(cobol_statements_ErrorHandled.__init__)


def test_cobol_statements_errorhandled_constructor_args():
    sig = inspect.signature(cobol_statements_ErrorHandled.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_execute_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Execute)


def test_cobol_statements_execute_constructor_exists():
    assert callable(cobol_statements_Execute.__init__)


def test_cobol_statements_execute_constructor_args():
    sig = inspect.signature(cobol_statements_Execute.__init__)
    params = list(sig.parameters.keys())
    assert "water" in params, "Missing parameter 'water'"

def test_cobol_statements_execute_has_water():
    assert hasattr(cobol_statements_Execute, "water")
    descriptor = None
    for klass in cobol_statements_Execute.__mro__:
        if "water" in klass.__dict__:
            descriptor = klass.__dict__["water"]
            break
    assert isinstance(descriptor, property)



def test_functions_argumentable_is_not_abstract():
    assert not inspect.isabstract(functions_Argumentable)


def test_functions_argumentable_constructor_exists():
    assert callable(functions_Argumentable.__init__)


def test_functions_argumentable_constructor_args():
    sig = inspect.signature(functions_Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_cancel_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Cancel)


def test_cobol_statements_cancel_constructor_exists():
    assert callable(cobol_statements_Cancel.__init__)


def test_cobol_statements_cancel_constructor_args():
    sig = inspect.signature(cobol_statements_Cancel.__init__)
    params = list(sig.parameters.keys())



def test_statements_iostatement_is_not_abstract():
    assert not inspect.isabstract(statements_IOStatement)


def test_statements_iostatement_constructor_exists():
    assert callable(statements_IOStatement.__init__)


def test_statements_iostatement_constructor_args():
    sig = inspect.signature(statements_IOStatement.__init__)
    params = list(sig.parameters.keys())



def test_concatenatingstrings_is_not_abstract():
    assert not inspect.isabstract(ConcatenatingStrings)


def test_concatenatingstrings_constructor_exists():
    assert callable(ConcatenatingStrings.__init__)


def test_concatenatingstrings_constructor_args():
    sig = inspect.signature(ConcatenatingStrings.__init__)
    params = list(sig.parameters.keys())



def test_indexnamereference_is_not_abstract():
    assert not inspect.isabstract(IndexNameReference)


def test_indexnamereference_constructor_exists():
    assert callable(IndexNameReference.__init__)


def test_indexnamereference_constructor_args():
    sig = inspect.signature(IndexNameReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_setindexname_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_SetIndexName)


def test_cobol_statements_setindexname_constructor_exists():
    assert callable(cobol_statements_SetIndexName.__init__)


def test_cobol_statements_setindexname_constructor_args():
    sig = inspect.signature(cobol_statements_SetIndexName.__init__)
    params = list(sig.parameters.keys())
    assert "adjust" in params, "Missing parameter 'adjust'"

def test_cobol_statements_setindexname_has_adjust():
    assert hasattr(cobol_statements_SetIndexName, "adjust")
    descriptor = None
    for klass in cobol_statements_SetIndexName.__mro__:
        if "adjust" in klass.__dict__:
            descriptor = klass.__dict__["adjust"]
            break
    assert isinstance(descriptor, property)



def test_switchstatus_is_not_abstract():
    assert not inspect.isabstract(SwitchStatus)


def test_switchstatus_constructor_exists():
    assert callable(SwitchStatus.__init__)


def test_switchstatus_constructor_args():
    sig = inspect.signature(SwitchStatus.__init__)
    params = list(sig.parameters.keys())



def test_primaryoperand_is_not_abstract():
    assert not inspect.isabstract(PrimaryOperand)


def test_primaryoperand_constructor_exists():
    assert callable(PrimaryOperand.__init__)


def test_primaryoperand_constructor_args():
    sig = inspect.signature(PrimaryOperand.__init__)
    params = list(sig.parameters.keys())



def test_cobol_registers_register_is_not_abstract():
    assert not inspect.isabstract(cobol_registers_Register)


def test_cobol_registers_register_constructor_exists():
    assert callable(cobol_registers_Register.__init__)


def test_cobol_registers_register_constructor_args():
    sig = inspect.signature(cobol_registers_Register.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_move_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Move)


def test_cobol_statements_move_constructor_exists():
    assert callable(cobol_statements_Move.__init__)


def test_cobol_statements_move_constructor_args():
    sig = inspect.signature(cobol_statements_Move.__init__)
    params = list(sig.parameters.keys())
    assert "corresponding" in params, "Missing parameter 'corresponding'"

def test_cobol_statements_move_has_corresponding():
    assert hasattr(cobol_statements_Move, "corresponding")
    descriptor = None
    for klass in cobol_statements_Move.__mro__:
        if "corresponding" in klass.__dict__:
            descriptor = klass.__dict__["corresponding"]
            break
    assert isinstance(descriptor, property)



def test_cobol_statements_nestedstatement_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_NestedStatement)


def test_cobol_statements_nestedstatement_constructor_exists():
    assert callable(cobol_statements_NestedStatement.__init__)


def test_cobol_statements_nestedstatement_constructor_args():
    sig = inspect.signature(cobol_statements_NestedStatement.__init__)
    params = list(sig.parameters.keys())



def test_jump_is_not_abstract():
    assert not inspect.isabstract(Jump)


def test_jump_constructor_exists():
    assert callable(Jump.__init__)


def test_jump_constructor_args():
    sig = inspect.signature(Jump.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_goto_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_GoTo)


def test_cobol_statements_goto_constructor_exists():
    assert callable(cobol_statements_GoTo.__init__)


def test_cobol_statements_goto_constructor_args():
    sig = inspect.signature(cobol_statements_GoTo.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_goback_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_GoBack)


def test_cobol_statements_goback_constructor_exists():
    assert callable(cobol_statements_GoBack.__init__)


def test_cobol_statements_goback_constructor_args():
    sig = inspect.signature(cobol_statements_GoBack.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_continue_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Continue)


def test_cobol_statements_continue_constructor_exists():
    assert callable(cobol_statements_Continue.__init__)


def test_cobol_statements_continue_constructor_args():
    sig = inspect.signature(cobol_statements_Continue.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_nextsentence_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_NextSentence)


def test_cobol_statements_nextsentence_constructor_exists():
    assert callable(cobol_statements_NextSentence.__init__)


def test_cobol_statements_nextsentence_constructor_args():
    sig = inspect.signature(cobol_statements_NextSentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_jump_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Jump)


def test_cobol_statements_jump_constructor_exists():
    assert callable(cobol_statements_Jump.__init__)


def test_cobol_statements_jump_constructor_args():
    sig = inspect.signature(cobol_statements_Jump.__init__)
    params = list(sig.parameters.keys())



def test_procedurerangelabel_is_not_abstract():
    assert not inspect.isabstract(ProcedureRangeLabel)


def test_procedurerangelabel_constructor_exists():
    assert callable(ProcedureRangeLabel.__init__)


def test_procedurerangelabel_constructor_args():
    sig = inspect.signature(ProcedureRangeLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol_labels_procedurerange_is_not_abstract():
    assert not inspect.isabstract(cobol_labels_ProcedureRange)


def test_cobol_labels_procedurerange_constructor_exists():
    assert callable(cobol_labels_ProcedureRange.__init__)


def test_cobol_labels_procedurerange_constructor_args():
    sig = inspect.signature(cobol_labels_ProcedureRange.__init__)
    params = list(sig.parameters.keys())



def test_cobol_labels_procedurerangechild_is_not_abstract():
    assert not inspect.isabstract(cobol_labels_ProcedureRangeChild)


def test_cobol_labels_procedurerangechild_constructor_exists():
    assert callable(cobol_labels_ProcedureRangeChild.__init__)


def test_cobol_labels_procedurerangechild_constructor_args():
    sig = inspect.signature(cobol_labels_ProcedureRangeChild.__init__)
    params = list(sig.parameters.keys())



def test_perform_is_not_abstract():
    assert not inspect.isabstract(Perform)


def test_perform_constructor_exists():
    assert callable(Perform.__init__)


def test_perform_constructor_args():
    sig = inspect.signature(Perform.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_performfixedtimes_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_PerformFixedTimes)


def test_cobol_statements_performfixedtimes_constructor_exists():
    assert callable(cobol_statements_PerformFixedTimes.__init__)


def test_cobol_statements_performfixedtimes_constructor_args():
    sig = inspect.signature(cobol_statements_PerformFixedTimes.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_performprocedure_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_PerformProcedure)


def test_cobol_statements_performprocedure_constructor_exists():
    assert callable(cobol_statements_PerformProcedure.__init__)


def test_cobol_statements_performprocedure_constructor_args():
    sig = inspect.signature(cobol_statements_PerformProcedure.__init__)
    params = list(sig.parameters.keys())



def test_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(AssignmentExpression)


def test_assignmentexpression_constructor_exists():
    assert callable(AssignmentExpression.__init__)


def test_assignmentexpression_constructor_args():
    sig = inspect.signature(AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_environment_is_not_abstract():
    assert not inspect.isabstract(Environment)


def test_environment_constructor_exists():
    assert callable(Environment.__init__)


def test_environment_constructor_args():
    sig = inspect.signature(Environment.__init__)
    params = list(sig.parameters.keys())



def test_cobol_environments_upsi_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_UPSI)


def test_cobol_environments_upsi_constructor_exists():
    assert callable(cobol_environments_UPSI.__init__)


def test_cobol_environments_upsi_constructor_args():
    sig = inspect.signature(cobol_environments_UPSI.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_environments_upsi_has_value():
    assert hasattr(cobol_environments_UPSI, "value")
    descriptor = None
    for klass in cobol_environments_UPSI.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_environments_systemdevice_is_not_abstract():
    assert not inspect.isabstract(cobol_environments_SystemDevice)


def test_cobol_environments_systemdevice_constructor_exists():
    assert callable(cobol_environments_SystemDevice.__init__)


def test_cobol_environments_systemdevice_constructor_args():
    sig = inspect.signature(cobol_environments_SystemDevice.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_display_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Display)


def test_cobol_statements_display_constructor_exists():
    assert callable(cobol_statements_Display.__init__)


def test_cobol_statements_display_constructor_args():
    sig = inspect.signature(cobol_statements_Display.__init__)
    params = list(sig.parameters.keys())



def test_stoplabel_is_not_abstract():
    assert not inspect.isabstract(StopLabel)


def test_stoplabel_constructor_exists():
    assert callable(StopLabel.__init__)


def test_stoplabel_constructor_args():
    sig = inspect.signature(StopLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol_labels_run_is_not_abstract():
    assert not inspect.isabstract(cobol_labels_Run)


def test_cobol_labels_run_constructor_exists():
    assert callable(cobol_labels_Run.__init__)


def test_cobol_labels_run_constructor_args():
    sig = inspect.signature(cobol_labels_Run.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_stop_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Stop)


def test_cobol_statements_stop_constructor_exists():
    assert callable(cobol_statements_Stop.__init__)


def test_cobol_statements_stop_constructor_args():
    sig = inspect.signature(cobol_statements_Stop.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_conditional_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Conditional)


def test_cobol_statements_conditional_constructor_exists():
    assert callable(cobol_statements_Conditional.__init__)


def test_cobol_statements_conditional_constructor_args():
    sig = inspect.signature(cobol_statements_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_statements_conditional_is_not_abstract():
    assert not inspect.isabstract(statements_Conditional)


def test_statements_conditional_constructor_exists():
    assert callable(statements_Conditional.__init__)


def test_statements_conditional_constructor_args():
    sig = inspect.signature(statements_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_exit_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Exit)


def test_cobol_statements_exit_constructor_exists():
    assert callable(cobol_statements_Exit.__init__)


def test_cobol_statements_exit_constructor_args():
    sig = inspect.signature(cobol_statements_Exit.__init__)
    params = list(sig.parameters.keys())
    assert "exitLabel" in params, "Missing parameter 'exitLabel'"

def test_cobol_statements_exit_has_exitLabel():
    assert hasattr(cobol_statements_Exit, "exitLabel")
    descriptor = None
    for klass in cobol_statements_Exit.__mro__:
        if "exitLabel" in klass.__dict__:
            descriptor = klass.__dict__["exitLabel"]
            break
    assert isinstance(descriptor, property)



def test_cobol_statements_statement_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Statement)


def test_cobol_statements_statement_constructor_exists():
    assert callable(cobol_statements_Statement.__init__)


def test_cobol_statements_statement_constructor_args():
    sig = inspect.signature(cobol_statements_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "endVerb" in params, "Missing parameter 'endVerb'"

def test_cobol_statements_statement_has_endVerb():
    assert hasattr(cobol_statements_Statement, "endVerb")
    descriptor = None
    for klass in cobol_statements_Statement.__mro__:
        if "endVerb" in klass.__dict__:
            descriptor = klass.__dict__["endVerb"]
            break
    assert isinstance(descriptor, property)



def test_cobol_operands_operand_is_not_abstract():
    assert not inspect.isabstract(cobol_operands_Operand)


def test_cobol_operands_operand_constructor_exists():
    assert callable(cobol_operands_Operand.__init__)


def test_cobol_operands_operand_constructor_args():
    sig = inspect.signature(cobol_operands_Operand.__init__)
    params = list(sig.parameters.keys())



def test_replacementoperand_is_not_abstract():
    assert not inspect.isabstract(ReplacementOperand)


def test_replacementoperand_constructor_exists():
    assert callable(ReplacementOperand.__init__)


def test_replacementoperand_constructor_args():
    sig = inspect.signature(ReplacementOperand.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operands_encoding_is_not_abstract():
    assert not inspect.isabstract(cobol_operands_Encoding)


def test_cobol_operands_encoding_constructor_exists():
    assert callable(cobol_operands_Encoding.__init__)


def test_cobol_operands_encoding_constructor_args():
    sig = inspect.signature(cobol_operands_Encoding.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cobol_operands_encoding_has_type():
    assert hasattr(cobol_operands_Encoding, "type")
    descriptor = None
    for klass in cobol_operands_Encoding.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_operand_is_not_abstract():
    assert not inspect.isabstract(Operand)


def test_operand_constructor_exists():
    assert callable(Operand.__init__)


def test_operand_constructor_args():
    sig = inspect.signature(Operand.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operands_arithmeticoperand_is_not_abstract():
    assert not inspect.isabstract(cobol_operands_ArithmeticOperand)


def test_cobol_operands_arithmeticoperand_constructor_exists():
    assert callable(cobol_operands_ArithmeticOperand.__init__)


def test_cobol_operands_arithmeticoperand_constructor_args():
    sig = inspect.signature(cobol_operands_ArithmeticOperand.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operands_replacementoperand_is_not_abstract():
    assert not inspect.isabstract(cobol_operands_ReplacementOperand)


def test_cobol_operands_replacementoperand_constructor_exists():
    assert callable(cobol_operands_ReplacementOperand.__init__)


def test_cobol_operands_replacementoperand_constructor_args():
    sig = inspect.signature(cobol_operands_ReplacementOperand.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_statements_nestedstatement_is_not_abstract():
    assert not inspect.isabstract(statements_NestedStatement)


def test_statements_nestedstatement_constructor_exists():
    assert callable(statements_NestedStatement.__init__)


def test_statements_nestedstatement_constructor_args():
    sig = inspect.signature(statements_NestedStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_condition_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Condition)


def test_cobol_statements_condition_constructor_exists():
    assert callable(cobol_statements_Condition.__init__)


def test_cobol_statements_condition_constructor_args():
    sig = inspect.signature(cobol_statements_Condition.__init__)
    params = list(sig.parameters.keys())



def test_statements_perform_is_not_abstract():
    assert not inspect.isabstract(statements_Perform)


def test_statements_perform_constructor_exists():
    assert callable(statements_Perform.__init__)


def test_statements_perform_constructor_args():
    sig = inspect.signature(statements_Perform.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_performuntilcondition_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_PerformUntilCondition)


def test_cobol_statements_performuntilcondition_constructor_exists():
    assert callable(cobol_statements_PerformUntilCondition.__init__)


def test_cobol_statements_performuntilcondition_constructor_args():
    sig = inspect.signature(cobol_statements_PerformUntilCondition.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_cobol_statements_performuntilcondition_has_position():
    assert hasattr(cobol_statements_PerformUntilCondition, "position")
    descriptor = None
    for klass in cobol_statements_PerformUntilCondition.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_cobol_statements_performnestedstatement_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_PerformNestedStatement)


def test_cobol_statements_performnestedstatement_constructor_exists():
    assert callable(cobol_statements_PerformNestedStatement.__init__)


def test_cobol_statements_performnestedstatement_constructor_args():
    sig = inspect.signature(cobol_statements_PerformNestedStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_perform_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Perform)


def test_cobol_statements_perform_constructor_exists():
    assert callable(cobol_statements_Perform.__init__)


def test_cobol_statements_perform_constructor_args():
    sig = inspect.signature(cobol_statements_Perform.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticstatement_is_not_abstract():
    assert not inspect.isabstract(ArithmeticStatement)


def test_arithmeticstatement_constructor_exists():
    assert callable(ArithmeticStatement.__init__)


def test_arithmeticstatement_constructor_args():
    sig = inspect.signature(ArithmeticStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_divide_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Divide)


def test_cobol_statements_divide_constructor_exists():
    assert callable(cobol_statements_Divide.__init__)


def test_cobol_statements_divide_constructor_args():
    sig = inspect.signature(cobol_statements_Divide.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_multiply_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Multiply)


def test_cobol_statements_multiply_constructor_exists():
    assert callable(cobol_statements_Multiply.__init__)


def test_cobol_statements_multiply_constructor_args():
    sig = inspect.signature(cobol_statements_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_subtract_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Subtract)


def test_cobol_statements_subtract_constructor_exists():
    assert callable(cobol_statements_Subtract.__init__)


def test_cobol_statements_subtract_constructor_args():
    sig = inspect.signature(cobol_statements_Subtract.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_add_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Add)


def test_cobol_statements_add_constructor_exists():
    assert callable(cobol_statements_Add.__init__)


def test_cobol_statements_add_constructor_args():
    sig = inspect.signature(cobol_statements_Add.__init__)
    params = list(sig.parameters.keys())



def test_statements_errorhandled_is_not_abstract():
    assert not inspect.isabstract(statements_ErrorHandled)


def test_statements_errorhandled_constructor_exists():
    assert callable(statements_ErrorHandled.__init__)


def test_statements_errorhandled_constructor_args():
    sig = inspect.signature(statements_ErrorHandled.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_return_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Return)


def test_cobol_statements_return_constructor_exists():
    assert callable(cobol_statements_Return.__init__)


def test_cobol_statements_return_constructor_args():
    sig = inspect.signature(cobol_statements_Return.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_arithmeticstatement_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_ArithmeticStatement)


def test_cobol_statements_arithmeticstatement_constructor_exists():
    assert callable(cobol_statements_ArithmeticStatement.__init__)


def test_cobol_statements_arithmeticstatement_constructor_args():
    sig = inspect.signature(cobol_statements_ArithmeticStatement.__init__)
    params = list(sig.parameters.keys())
    assert "corresponding" in params, "Missing parameter 'corresponding'"

def test_cobol_statements_arithmeticstatement_has_corresponding():
    assert hasattr(cobol_statements_ArithmeticStatement, "corresponding")
    descriptor = None
    for klass in cobol_statements_ArithmeticStatement.__mro__:
        if "corresponding" in klass.__dict__:
            descriptor = klass.__dict__["corresponding"]
            break
    assert isinstance(descriptor, property)



def test_cobol_statements_start_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Start)


def test_cobol_statements_start_constructor_exists():
    assert callable(cobol_statements_Start.__init__)


def test_cobol_statements_start_constructor_args():
    sig = inspect.signature(cobol_statements_Start.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_searchstatement_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_SearchStatement)


def test_cobol_statements_searchstatement_constructor_exists():
    assert callable(cobol_statements_SearchStatement.__init__)


def test_cobol_statements_searchstatement_constructor_args():
    sig = inspect.signature(cobol_statements_SearchStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_delete_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Delete)


def test_cobol_statements_delete_constructor_exists():
    assert callable(cobol_statements_Delete.__init__)


def test_cobol_statements_delete_constructor_args():
    sig = inspect.signature(cobol_statements_Delete.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_read_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Read)


def test_cobol_statements_read_constructor_exists():
    assert callable(cobol_statements_Read.__init__)


def test_cobol_statements_read_constructor_args():
    sig = inspect.signature(cobol_statements_Read.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_unstring_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Unstring)


def test_cobol_statements_unstring_constructor_exists():
    assert callable(cobol_statements_Unstring.__init__)


def test_cobol_statements_unstring_constructor_args():
    sig = inspect.signature(cobol_statements_Unstring.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_write_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Write)


def test_cobol_statements_write_constructor_exists():
    assert callable(cobol_statements_Write.__init__)


def test_cobol_statements_write_constructor_args():
    sig = inspect.signature(cobol_statements_Write.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_call_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Call)


def test_cobol_statements_call_constructor_exists():
    assert callable(cobol_statements_Call.__init__)


def test_cobol_statements_call_constructor_args():
    sig = inspect.signature(cobol_statements_Call.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_string_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_String)


def test_cobol_statements_string_constructor_exists():
    assert callable(cobol_statements_String.__init__)


def test_cobol_statements_string_constructor_args():
    sig = inspect.signature(cobol_statements_String.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_compute_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Compute)


def test_cobol_statements_compute_constructor_exists():
    assert callable(cobol_statements_Compute.__init__)


def test_cobol_statements_compute_constructor_args():
    sig = inspect.signature(cobol_statements_Compute.__init__)
    params = list(sig.parameters.keys())



def test_constantliteral_is_not_abstract():
    assert not inspect.isabstract(ConstantLiteral)


def test_constantliteral_constructor_exists():
    assert callable(ConstantLiteral.__init__)


def test_constantliteral_constructor_args():
    sig = inspect.signature(ConstantLiteral.__init__)
    params = list(sig.parameters.keys())



def test_figurativeconstantliteral_is_not_abstract():
    assert not inspect.isabstract(FigurativeConstantLiteral)


def test_figurativeconstantliteral_constructor_exists():
    assert callable(FigurativeConstantLiteral.__init__)


def test_figurativeconstantliteral_constructor_args():
    sig = inspect.signature(FigurativeConstantLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_allliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_AllLiteral)


def test_cobol_literals_allliteral_constructor_exists():
    assert callable(cobol_literals_AllLiteral.__init__)


def test_cobol_literals_allliteral_constructor_args():
    sig = inspect.signature(cobol_literals_AllLiteral.__init__)
    params = list(sig.parameters.keys())



def test_decimalliteral_is_not_abstract():
    assert not inspect.isabstract(DecimalLiteral)


def test_decimalliteral_constructor_exists():
    assert callable(DecimalLiteral.__init__)


def test_decimalliteral_constructor_args():
    sig = inspect.signature(DecimalLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_floatingdecimalliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_FloatingDecimalLiteral)


def test_cobol_literals_floatingdecimalliteral_constructor_exists():
    assert callable(cobol_literals_FloatingDecimalLiteral.__init__)


def test_cobol_literals_floatingdecimalliteral_constructor_args():
    sig = inspect.signature(cobol_literals_FloatingDecimalLiteral.__init__)
    params = list(sig.parameters.keys())



def test_numericliteral_is_not_abstract():
    assert not inspect.isabstract(NumericLiteral)


def test_numericliteral_constructor_exists():
    assert callable(NumericLiteral.__init__)


def test_numericliteral_constructor_args():
    sig = inspect.signature(NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_decimalliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_DecimalLiteral)


def test_cobol_literals_decimalliteral_constructor_exists():
    assert callable(cobol_literals_DecimalLiteral.__init__)


def test_cobol_literals_decimalliteral_constructor_args():
    sig = inspect.signature(cobol_literals_DecimalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_decimalliteral_has_value():
    assert hasattr(cobol_literals_DecimalLiteral, "value")
    descriptor = None
    for klass in cobol_literals_DecimalLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_water_iocontrolparagraphwater_is_not_abstract():
    assert not inspect.isabstract(water_IOControlParagraphWater)


def test_water_iocontrolparagraphwater_constructor_exists():
    assert callable(water_IOControlParagraphWater.__init__)


def test_water_iocontrolparagraphwater_constructor_args():
    sig = inspect.signature(water_IOControlParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_water_filedescriptorwater_is_not_abstract():
    assert not inspect.isabstract(water_FileDescriptorWater)


def test_water_filedescriptorwater_constructor_exists():
    assert callable(water_FileDescriptorWater.__init__)


def test_water_filedescriptorwater_constructor_args():
    sig = inspect.signature(water_FileDescriptorWater.__init__)
    params = list(sig.parameters.keys())



def test_water_objectcomputerparagraphwater_is_not_abstract():
    assert not inspect.isabstract(water_ObjectComputerParagraphWater)


def test_water_objectcomputerparagraphwater_constructor_exists():
    assert callable(water_ObjectComputerParagraphWater.__init__)


def test_water_objectcomputerparagraphwater_constructor_args():
    sig = inspect.signature(water_ObjectComputerParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_literals_numericliteral_is_not_abstract():
    assert not inspect.isabstract(literals_NumericLiteral)


def test_literals_numericliteral_constructor_exists():
    assert callable(literals_NumericLiteral.__init__)


def test_literals_numericliteral_constructor_args():
    sig = inspect.signature(literals_NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_integerliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_IntegerLiteral)


def test_cobol_literals_integerliteral_constructor_exists():
    assert callable(cobol_literals_IntegerLiteral.__init__)


def test_cobol_literals_integerliteral_constructor_args():
    sig = inspect.signature(cobol_literals_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_integerliteral_has_value():
    assert hasattr(cobol_literals_IntegerLiteral, "value")
    descriptor = None
    for klass in cobol_literals_IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_figurativeconstantliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_FigurativeConstantLiteral)


def test_cobol_literals_figurativeconstantliteral_constructor_exists():
    assert callable(cobol_literals_FigurativeConstantLiteral.__init__)


def test_cobol_literals_figurativeconstantliteral_constructor_args():
    sig = inspect.signature(cobol_literals_FigurativeConstantLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_BooleanLiteral)


def test_cobol_literals_booleanliteral_constructor_exists():
    assert callable(cobol_literals_BooleanLiteral.__init__)


def test_cobol_literals_booleanliteral_constructor_args():
    sig = inspect.signature(cobol_literals_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_booleanliteral_has_value():
    assert hasattr(cobol_literals_BooleanLiteral, "value")
    descriptor = None
    for klass in cobol_literals_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_literals_alphanumericliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_AlphanumericLiteral)


def test_cobol_literals_alphanumericliteral_constructor_exists():
    assert callable(cobol_literals_AlphanumericLiteral.__init__)


def test_cobol_literals_alphanumericliteral_constructor_args():
    sig = inspect.signature(cobol_literals_AlphanumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_alphanumericliteral_has_value():
    assert hasattr(cobol_literals_AlphanumericLiteral, "value")
    descriptor = None
    for klass in cobol_literals_AlphanumericLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_division_is_not_abstract():
    assert not inspect.isabstract(Division)


def test_division_constructor_exists():
    assert callable(Division.__init__)


def test_division_constructor_args():
    sig = inspect.signature(Division.__init__)
    params = list(sig.parameters.keys())



def test_cobol_divisions_environmentdivision_is_not_abstract():
    assert not inspect.isabstract(cobol_divisions_EnvironmentDivision)


def test_cobol_divisions_environmentdivision_constructor_exists():
    assert callable(cobol_divisions_EnvironmentDivision.__init__)


def test_cobol_divisions_environmentdivision_constructor_args():
    sig = inspect.signature(cobol_divisions_EnvironmentDivision.__init__)
    params = list(sig.parameters.keys())



def test_cobol_divisions_datadivision_is_not_abstract():
    assert not inspect.isabstract(cobol_divisions_DataDivision)


def test_cobol_divisions_datadivision_constructor_exists():
    assert callable(cobol_divisions_DataDivision.__init__)


def test_cobol_divisions_datadivision_constructor_args():
    sig = inspect.signature(cobol_divisions_DataDivision.__init__)
    params = list(sig.parameters.keys())



def test_statementcontainer_is_not_abstract():
    assert not inspect.isabstract(StatementContainer)


def test_statementcontainer_constructor_exists():
    assert callable(StatementContainer.__init__)


def test_statementcontainer_constructor_args():
    sig = inspect.signature(StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_paragraph_is_not_abstract():
    assert not inspect.isabstract(Paragraph)


def test_paragraph_constructor_exists():
    assert callable(Paragraph.__init__)


def test_paragraph_constructor_args():
    sig = inspect.signature(Paragraph.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sections_datadivisionsection_is_not_abstract():
    assert not inspect.isabstract(cobol_sections_DataDivisionSection)


def test_cobol_sections_datadivisionsection_constructor_exists():
    assert callable(cobol_sections_DataDivisionSection.__init__)


def test_cobol_sections_datadivisionsection_constructor_args():
    sig = inspect.signature(cobol_sections_DataDivisionSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sections_environmentdivisionsection_is_not_abstract():
    assert not inspect.isabstract(cobol_sections_EnvironmentDivisionSection)


def test_cobol_sections_environmentdivisionsection_constructor_exists():
    assert callable(cobol_sections_EnvironmentDivisionSection.__init__)


def test_cobol_sections_environmentdivisionsection_constructor_args():
    sig = inspect.signature(cobol_sections_EnvironmentDivisionSection.__init__)
    params = list(sig.parameters.keys())



def test_cobolroot_is_not_abstract():
    assert not inspect.isabstract(CobolRoot)


def test_cobolroot_constructor_exists():
    assert callable(CobolRoot.__init__)


def test_cobolroot_constructor_args():
    sig = inspect.signature(CobolRoot.__init__)
    params = list(sig.parameters.keys())



def test_cobol_containers_emptymodel_is_not_abstract():
    assert not inspect.isabstract(cobol_containers_EmptyModel)


def test_cobol_containers_emptymodel_constructor_exists():
    assert callable(cobol_containers_EmptyModel.__init__)


def test_cobol_containers_emptymodel_constructor_args():
    sig = inspect.signature(cobol_containers_EmptyModel.__init__)
    params = list(sig.parameters.keys())



def test_cobol_containers_cobolroot_is_not_abstract():
    assert not inspect.isabstract(cobol_containers_CobolRoot)


def test_cobol_containers_cobolroot_constructor_exists():
    assert callable(cobol_containers_CobolRoot.__init__)


def test_cobol_containers_cobolroot_constructor_args():
    sig = inspect.signature(cobol_containers_CobolRoot.__init__)
    params = list(sig.parameters.keys())



def test_proceduredivision_is_not_abstract():
    assert not inspect.isabstract(ProcedureDivision)


def test_proceduredivision_constructor_exists():
    assert callable(ProcedureDivision.__init__)


def test_proceduredivision_constructor_args():
    sig = inspect.signature(ProcedureDivision.__init__)
    params = list(sig.parameters.keys())



def test_datadivision_is_not_abstract():
    assert not inspect.isabstract(DataDivision)


def test_datadivision_constructor_exists():
    assert callable(DataDivision.__init__)


def test_datadivision_constructor_args():
    sig = inspect.signature(DataDivision.__init__)
    params = list(sig.parameters.keys())



def test_environmentdivision_is_not_abstract():
    assert not inspect.isabstract(EnvironmentDivision)


def test_environmentdivision_constructor_exists():
    assert callable(EnvironmentDivision.__init__)


def test_environmentdivision_constructor_args():
    sig = inspect.signature(EnvironmentDivision.__init__)
    params = list(sig.parameters.keys())



def test_water_invokestatementwater_is_not_abstract():
    assert not inspect.isabstract(water_InvokeStatementWater)


def test_water_invokestatementwater_constructor_exists():
    assert callable(water_InvokeStatementWater.__init__)


def test_water_invokestatementwater_constructor_args():
    sig = inspect.signature(water_InvokeStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_operands_primaryoperand_is_not_abstract():
    assert not inspect.isabstract(operands_PrimaryOperand)


def test_operands_primaryoperand_constructor_exists():
    assert callable(operands_PrimaryOperand.__init__)


def test_operands_primaryoperand_constructor_args():
    sig = inspect.signature(operands_PrimaryOperand.__init__)
    params = list(sig.parameters.keys())



def test_water_cicsstatementwater_is_not_abstract():
    assert not inspect.isabstract(water_CICSStatementWater)


def test_water_cicsstatementwater_constructor_exists():
    assert callable(water_CICSStatementWater.__init__)


def test_water_cicsstatementwater_constructor_args():
    sig = inspect.signature(water_CICSStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_water_specialnamesparagraphwater_is_not_abstract():
    assert not inspect.isabstract(water_SpecialNamesParagraphWater)


def test_water_specialnamesparagraphwater_constructor_exists():
    assert callable(water_SpecialNamesParagraphWater.__init__)


def test_water_specialnamesparagraphwater_constructor_args():
    sig = inspect.signature(water_SpecialNamesParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_water_selectstatementwater_is_not_abstract():
    assert not inspect.isabstract(water_SelectStatementWater)


def test_water_selectstatementwater_constructor_exists():
    assert callable(water_SelectStatementWater.__init__)


def test_water_selectstatementwater_constructor_args():
    sig = inspect.signature(water_SelectStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_identifiers_identifier_is_not_abstract():
    assert not inspect.isabstract(cobol_identifiers_Identifier)


def test_cobol_identifiers_identifier_constructor_exists():
    assert callable(cobol_identifiers_Identifier.__init__)


def test_cobol_identifiers_identifier_constructor_args():
    sig = inspect.signature(cobol_identifiers_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_declaratives_is_not_abstract():
    assert not inspect.isabstract(Declaratives)


def test_declaratives_constructor_exists():
    assert callable(Declaratives.__init__)


def test_declaratives_constructor_args():
    sig = inspect.signature(Declaratives.__init__)
    params = list(sig.parameters.keys())



def test_parameters_parametrizable_is_not_abstract():
    assert not inspect.isabstract(parameters_Parametrizable)


def test_parameters_parametrizable_constructor_exists():
    assert callable(parameters_Parametrizable.__init__)


def test_parameters_parametrizable_constructor_args():
    sig = inspect.signature(parameters_Parametrizable.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_entry_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Entry)


def test_cobol_statements_entry_constructor_exists():
    assert callable(cobol_statements_Entry.__init__)


def test_cobol_statements_entry_constructor_args():
    sig = inspect.signature(cobol_statements_Entry.__init__)
    params = list(sig.parameters.keys())



def test_water_incompleteelement_is_not_abstract():
    assert not inspect.isabstract(water_IncompleteElement)


def test_water_incompleteelement_constructor_exists():
    assert callable(water_IncompleteElement.__init__)


def test_water_incompleteelement_constructor_args():
    sig = inspect.signature(water_IncompleteElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_files_filename_is_not_abstract():
    assert not inspect.isabstract(cobol_files_FileName)


def test_cobol_files_filename_constructor_exists():
    assert callable(cobol_files_FileName.__init__)


def test_cobol_files_filename_constructor_args():
    sig = inspect.signature(cobol_files_FileName.__init__)
    params = list(sig.parameters.keys())
    assert "fileDescriptor" in params, "Missing parameter 'fileDescriptor'"

def test_cobol_files_filename_has_fileDescriptor():
    assert hasattr(cobol_files_FileName, "fileDescriptor")
    descriptor = None
    for klass in cobol_files_FileName.__mro__:
        if "fileDescriptor" in klass.__dict__:
            descriptor = klass.__dict__["fileDescriptor"]
            break
    assert isinstance(descriptor, property)



def test_cobol_statements_merge_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Merge)


def test_cobol_statements_merge_constructor_exists():
    assert callable(cobol_statements_Merge.__init__)


def test_cobol_statements_merge_constructor_args():
    sig = inspect.signature(cobol_statements_Merge.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_accept_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Accept)


def test_cobol_statements_accept_constructor_exists():
    assert callable(cobol_statements_Accept.__init__)


def test_cobol_statements_accept_constructor_args():
    sig = inspect.signature(cobol_statements_Accept.__init__)
    params = list(sig.parameters.keys())



def test_cobol_tables_table_is_not_abstract():
    assert not inspect.isabstract(cobol_tables_Table)


def test_cobol_tables_table_constructor_exists():
    assert callable(cobol_tables_Table.__init__)


def test_cobol_tables_table_constructor_args():
    sig = inspect.signature(cobol_tables_Table.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_sort_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Sort)


def test_cobol_statements_sort_constructor_exists():
    assert callable(cobol_statements_Sort.__init__)


def test_cobol_statements_sort_constructor_args():
    sig = inspect.signature(cobol_statements_Sort.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_close_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Close)


def test_cobol_statements_close_constructor_exists():
    assert callable(cobol_statements_Close.__init__)


def test_cobol_statements_close_constructor_args():
    sig = inspect.signature(cobol_statements_Close.__init__)
    params = list(sig.parameters.keys())



def test_cobol_statements_open_is_not_abstract():
    assert not inspect.isabstract(cobol_statements_Open)


def test_cobol_statements_open_constructor_exists():
    assert callable(cobol_statements_Open.__init__)


def test_cobol_statements_open_constructor_args():
    sig = inspect.signature(cobol_statements_Open.__init__)
    params = list(sig.parameters.keys())



def test_cobol_dataitems_dataitem_is_not_abstract():
    assert not inspect.isabstract(cobol_dataitems_DataItem)


def test_cobol_dataitems_dataitem_constructor_exists():
    assert callable(cobol_dataitems_DataItem.__init__)


def test_cobol_dataitems_dataitem_constructor_args():
    sig = inspect.signature(cobol_dataitems_DataItem.__init__)
    params = list(sig.parameters.keys())
    assert "levelNumber" in params, "Missing parameter 'levelNumber'"

def test_cobol_dataitems_dataitem_has_levelNumber():
    assert hasattr(cobol_dataitems_DataItem, "levelNumber")
    descriptor = None
    for klass in cobol_dataitems_DataItem.__mro__:
        if "levelNumber" in klass.__dict__:
            descriptor = klass.__dict__["levelNumber"]
            break
    assert isinstance(descriptor, property)



def test_divisions_division_is_not_abstract():
    assert not inspect.isabstract(divisions_Division)


def test_divisions_division_constructor_exists():
    assert callable(divisions_Division.__init__)


def test_divisions_division_constructor_args():
    sig = inspect.signature(divisions_Division.__init__)
    params = list(sig.parameters.keys())



def test_cobol_divisions_proceduredivision_is_not_abstract():
    assert not inspect.isabstract(cobol_divisions_ProcedureDivision)


def test_cobol_divisions_proceduredivision_constructor_exists():
    assert callable(cobol_divisions_ProcedureDivision.__init__)


def test_cobol_divisions_proceduredivision_constructor_args():
    sig = inspect.signature(cobol_divisions_ProcedureDivision.__init__)
    params = list(sig.parameters.keys())



def test_cobol_divisions_identificationdivision_is_not_abstract():
    assert not inspect.isabstract(cobol_divisions_IdentificationDivision)


def test_cobol_divisions_identificationdivision_constructor_exists():
    assert callable(cobol_divisions_IdentificationDivision.__init__)


def test_cobol_divisions_identificationdivision_constructor_args():
    sig = inspect.signature(cobol_divisions_IdentificationDivision.__init__)
    params = list(sig.parameters.keys())
    assert "properties" in params, "Missing parameter 'properties'"

def test_cobol_divisions_identificationdivision_has_properties():
    assert hasattr(cobol_divisions_IdentificationDivision, "properties")
    descriptor = None
    for klass in cobol_divisions_IdentificationDivision.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_RangeExpression)


def test_cobol_arithmetics_rangeexpression_constructor_exists():
    assert callable(cobol_arithmetics_RangeExpression.__init__)


def test_cobol_arithmetics_rangeexpression_constructor_args():
    sig = inspect.signature(cobol_arithmetics_RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_equal_is_not_abstract():
    assert not inspect.isabstract(Equal)


def test_equal_constructor_exists():
    assert callable(Equal.__init__)


def test_equal_constructor_args():
    sig = inspect.signature(Equal.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_AssignmentExpression)


def test_cobol_arithmetics_assignmentexpression_constructor_exists():
    assert callable(cobol_arithmetics_AssignmentExpression.__init__)


def test_cobol_arithmetics_assignmentexpression_constructor_args():
    sig = inspect.signature(cobol_arithmetics_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_unaryarithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(UnaryArithmeticExpressionChild)


def test_unaryarithmeticexpressionchild_constructor_exists():
    assert callable(UnaryArithmeticExpressionChild.__init__)


def test_unaryarithmeticexpressionchild_constructor_args():
    sig = inspect.signature(UnaryArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_PrimaryExpression)


def test_cobol_arithmetics_primaryexpression_constructor_exists():
    assert callable(cobol_arithmetics_PrimaryExpression.__init__)


def test_cobol_arithmetics_primaryexpression_constructor_args():
    sig = inspect.signature(cobol_arithmetics_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_powerarithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(PowerArithmeticExpressionChild)


def test_powerarithmeticexpressionchild_constructor_exists():
    assert callable(PowerArithmeticExpressionChild.__init__)


def test_powerarithmeticexpressionchild_constructor_args():
    sig = inspect.signature(PowerArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_unaryarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_UnaryArithmeticExpression)


def test_cobol_arithmetics_unaryarithmeticexpression_constructor_exists():
    assert callable(cobol_arithmetics_UnaryArithmeticExpression.__init__)


def test_cobol_arithmetics_unaryarithmeticexpression_constructor_args():
    sig = inspect.signature(cobol_arithmetics_UnaryArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_unaryarithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_UnaryArithmeticExpressionChild)


def test_cobol_arithmetics_unaryarithmeticexpressionchild_constructor_exists():
    assert callable(cobol_arithmetics_UnaryArithmeticExpressionChild.__init__)


def test_cobol_arithmetics_unaryarithmeticexpressionchild_constructor_args():
    sig = inspect.signature(cobol_arithmetics_UnaryArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_identificationdivision_is_not_abstract():
    assert not inspect.isabstract(IdentificationDivision)


def test_identificationdivision_constructor_exists():
    assert callable(IdentificationDivision.__init__)


def test_identificationdivision_constructor_args():
    sig = inspect.signature(IdentificationDivision.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_divisions_division_is_not_abstract():
    assert not inspect.isabstract(cobol_divisions_Division)


def test_cobol_divisions_division_constructor_exists():
    assert callable(cobol_divisions_Division.__init__)


def test_cobol_divisions_division_constructor_args():
    sig = inspect.signature(cobol_divisions_Division.__init__)
    params = list(sig.parameters.keys())



def test_cobol_containers_compilationunit_is_not_abstract():
    assert not inspect.isabstract(cobol_containers_CompilationUnit)


def test_cobol_containers_compilationunit_constructor_exists():
    assert callable(cobol_containers_CompilationUnit.__init__)


def test_cobol_containers_compilationunit_constructor_args():
    sig = inspect.signature(cobol_containers_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_commons_namedelement_is_not_abstract():
    assert not inspect.isabstract(commons_NamedElement)


def test_commons_namedelement_constructor_exists():
    assert callable(commons_NamedElement.__init__)


def test_commons_namedelement_constructor_args():
    sig = inspect.signature(commons_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_conditionname_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_ConditionName)


def test_cobol_specialnames_conditionname_constructor_exists():
    assert callable(cobol_specialnames_ConditionName.__init__)


def test_cobol_specialnames_conditionname_constructor_args():
    sig = inspect.signature(cobol_specialnames_ConditionName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_functions_functioncall_is_not_abstract():
    assert not inspect.isabstract(cobol_functions_FunctionCall)


def test_cobol_functions_functioncall_constructor_exists():
    assert callable(cobol_functions_FunctionCall.__init__)


def test_cobol_functions_functioncall_constructor_args():
    sig = inspect.signature(cobol_functions_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_cobol_tables_indexname_is_not_abstract():
    assert not inspect.isabstract(cobol_tables_IndexName)


def test_cobol_tables_indexname_constructor_exists():
    assert callable(cobol_tables_IndexName.__init__)


def test_cobol_tables_indexname_constructor_args():
    sig = inspect.signature(cobol_tables_IndexName.__init__)
    params = list(sig.parameters.keys())



def test_containers_cobolroot_is_not_abstract():
    assert not inspect.isabstract(containers_CobolRoot)


def test_containers_cobolroot_constructor_exists():
    assert callable(containers_CobolRoot.__init__)


def test_containers_cobolroot_constructor_args():
    sig = inspect.signature(containers_CobolRoot.__init__)
    params = list(sig.parameters.keys())



def test_cobol_containers_compilationgroup_is_not_abstract():
    assert not inspect.isabstract(cobol_containers_CompilationGroup)


def test_cobol_containers_compilationgroup_constructor_exists():
    assert callable(cobol_containers_CompilationGroup.__init__)


def test_cobol_containers_compilationgroup_constructor_args():
    sig = inspect.signature(cobol_containers_CompilationGroup.__init__)
    params = list(sig.parameters.keys())



def test_conditions_simpleconditionchild_is_not_abstract():
    assert not inspect.isabstract(conditions_SimpleConditionChild)


def test_conditions_simpleconditionchild_constructor_exists():
    assert callable(conditions_SimpleConditionChild.__init__)


def test_conditions_simpleconditionchild_constructor_args():
    sig = inspect.signature(conditions_SimpleConditionChild.__init__)
    params = list(sig.parameters.keys())



def test_conditions_abbreviatedrelationalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(conditions_AbbreviatedRelationalExpressionChild)


def test_conditions_abbreviatedrelationalexpressionchild_constructor_exists():
    assert callable(conditions_AbbreviatedRelationalExpressionChild.__init__)


def test_conditions_abbreviatedrelationalexpressionchild_constructor_args():
    sig = inspect.signature(conditions_AbbreviatedRelationalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_ArithmeticExpression)


def test_cobol_arithmetics_arithmeticexpression_constructor_exists():
    assert callable(cobol_arithmetics_ArithmeticExpression.__init__)


def test_cobol_arithmetics_arithmeticexpression_constructor_args():
    sig = inspect.signature(cobol_arithmetics_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_nestedarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_NestedArithmeticExpression)


def test_cobol_arithmetics_nestedarithmeticexpression_constructor_exists():
    assert callable(cobol_arithmetics_NestedArithmeticExpression.__init__)


def test_cobol_arithmetics_nestedarithmeticexpression_constructor_args():
    sig = inspect.signature(cobol_arithmetics_NestedArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_rangeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_RangeExpressionChild)


def test_cobol_arithmetics_rangeexpressionchild_constructor_exists():
    assert callable(cobol_arithmetics_RangeExpressionChild.__init__)


def test_cobol_arithmetics_rangeexpressionchild_constructor_args():
    sig = inspect.signature(cobol_arithmetics_RangeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_through_is_not_abstract():
    assert not inspect.isabstract(Through)


def test_through_constructor_exists():
    assert callable(Through.__init__)


def test_through_constructor_args():
    sig = inspect.signature(Through.__init__)
    params = list(sig.parameters.keys())



def test_classoperator_is_not_abstract():
    assert not inspect.isabstract(ClassOperator)


def test_classoperator_constructor_exists():
    assert callable(ClassOperator.__init__)


def test_classoperator_constructor_args():
    sig = inspect.signature(ClassOperator.__init__)
    params = list(sig.parameters.keys())



def test_signoperator_is_not_abstract():
    assert not inspect.isabstract(SignOperator)


def test_signoperator_constructor_exists():
    assert callable(SignOperator.__init__)


def test_signoperator_constructor_args():
    sig = inspect.signature(SignOperator.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeOperator)


def test_multiplicativeoperator_constructor_exists():
    assert callable(MultiplicativeOperator.__init__)


def test_multiplicativeoperator_constructor_args():
    sig = inspect.signature(MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativearithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeArithmeticExpressionChild)


def test_multiplicativearithmeticexpressionchild_constructor_exists():
    assert callable(MultiplicativeArithmeticExpressionChild.__init__)


def test_multiplicativearithmeticexpressionchild_constructor_args():
    sig = inspect.signature(MultiplicativeArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_powerarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_PowerArithmeticExpression)


def test_cobol_arithmetics_powerarithmeticexpression_constructor_exists():
    assert callable(cobol_arithmetics_PowerArithmeticExpression.__init__)


def test_cobol_arithmetics_powerarithmeticexpression_constructor_args():
    sig = inspect.signature(cobol_arithmetics_PowerArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_powerarithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_PowerArithmeticExpressionChild)


def test_cobol_arithmetics_powerarithmeticexpressionchild_constructor_exists():
    assert callable(cobol_arithmetics_PowerArithmeticExpressionChild.__init__)


def test_cobol_arithmetics_powerarithmeticexpressionchild_constructor_args():
    sig = inspect.signature(cobol_arithmetics_PowerArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(AdditiveOperator)


def test_additiveoperator_constructor_exists():
    assert callable(AdditiveOperator.__init__)


def test_additiveoperator_constructor_args():
    sig = inspect.signature(AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_additivearithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AdditiveArithmeticExpressionChild)


def test_additivearithmeticexpressionchild_constructor_exists():
    assert callable(AdditiveArithmeticExpressionChild.__init__)


def test_additivearithmeticexpressionchild_constructor_args():
    sig = inspect.signature(AdditiveArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_multiplicativearithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_MultiplicativeArithmeticExpression)


def test_cobol_arithmetics_multiplicativearithmeticexpression_constructor_exists():
    assert callable(cobol_arithmetics_MultiplicativeArithmeticExpression.__init__)


def test_cobol_arithmetics_multiplicativearithmeticexpression_constructor_args():
    sig = inspect.signature(cobol_arithmetics_MultiplicativeArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_multiplicativearithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_MultiplicativeArithmeticExpressionChild)


def test_cobol_arithmetics_multiplicativearithmeticexpressionchild_constructor_exists():
    assert callable(cobol_arithmetics_MultiplicativeArithmeticExpressionChild.__init__)


def test_cobol_arithmetics_multiplicativearithmeticexpressionchild_constructor_args():
    sig = inspect.signature(cobol_arithmetics_MultiplicativeArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_rangeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(RangeExpressionChild)


def test_rangeexpressionchild_constructor_exists():
    assert callable(RangeExpressionChild.__init__)


def test_rangeexpressionchild_constructor_args():
    sig = inspect.signature(RangeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_additivearithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_AdditiveArithmeticExpressionChild)


def test_cobol_arithmetics_additivearithmeticexpressionchild_constructor_exists():
    assert callable(cobol_arithmetics_AdditiveArithmeticExpressionChild.__init__)


def test_cobol_arithmetics_additivearithmeticexpressionchild_constructor_args():
    sig = inspect.signature(cobol_arithmetics_AdditiveArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_arithmetics_additivearithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_arithmetics_AdditiveArithmeticExpression)


def test_cobol_arithmetics_additivearithmeticexpression_constructor_exists():
    assert callable(cobol_arithmetics_AdditiveArithmeticExpression.__init__)


def test_cobol_arithmetics_additivearithmeticexpression_constructor_args():
    sig = inspect.signature(cobol_arithmetics_AdditiveArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_negatedabbreviatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(NegatedAbbreviatedConditionalExpressionChild)


def test_negatedabbreviatedconditionalexpressionchild_constructor_exists():
    assert callable(NegatedAbbreviatedConditionalExpressionChild.__init__)


def test_negatedabbreviatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(NegatedAbbreviatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_abbreviatedrelationalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_AbbreviatedRelationalExpressionChild)


def test_cobol_conditions_abbreviatedrelationalexpressionchild_constructor_exists():
    assert callable(cobol_conditions_AbbreviatedRelationalExpressionChild.__init__)


def test_cobol_conditions_abbreviatedrelationalexpressionchild_constructor_args():
    sig = inspect.signature(cobol_conditions_AbbreviatedRelationalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_abbreviatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AbbreviatedConditionalExpressionChild)


def test_abbreviatedconditionalexpressionchild_constructor_exists():
    assert callable(AbbreviatedConditionalExpressionChild.__init__)


def test_abbreviatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(AbbreviatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_negatedabbreviatedconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_NegatedAbbreviatedConditionalExpression)


def test_cobol_conditions_negatedabbreviatedconditionalexpression_constructor_exists():
    assert callable(cobol_conditions_NegatedAbbreviatedConditionalExpression.__init__)


def test_cobol_conditions_negatedabbreviatedconditionalexpression_constructor_args():
    sig = inspect.signature(cobol_conditions_NegatedAbbreviatedConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_expressionlist_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_ExpressionList)


def test_cobol_conditions_expressionlist_constructor_exists():
    assert callable(cobol_conditions_ExpressionList.__init__)


def test_cobol_conditions_expressionlist_constructor_args():
    sig = inspect.signature(cobol_conditions_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_abbreviatedrelationalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AbbreviatedRelationalExpressionChild)


def test_abbreviatedrelationalexpressionchild_constructor_exists():
    assert callable(AbbreviatedRelationalExpressionChild.__init__)


def test_abbreviatedrelationalexpressionchild_constructor_args():
    sig = inspect.signature(AbbreviatedRelationalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_nestedabbreviatedconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_NestedAbbreviatedConditionalExpression)


def test_cobol_conditions_nestedabbreviatedconditionalexpression_constructor_exists():
    assert callable(cobol_conditions_NestedAbbreviatedConditionalExpression.__init__)


def test_cobol_conditions_nestedabbreviatedconditionalexpression_constructor_args():
    sig = inspect.signature(cobol_conditions_NestedAbbreviatedConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_abbreviatedrelationalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_AbbreviatedRelationalExpression)


def test_cobol_conditions_abbreviatedrelationalexpression_constructor_exists():
    assert callable(cobol_conditions_AbbreviatedRelationalExpression.__init__)


def test_cobol_conditions_abbreviatedrelationalexpression_constructor_args():
    sig = inspect.signature(cobol_conditions_AbbreviatedRelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_negatedabbreviatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_NegatedAbbreviatedConditionalExpressionChild)


def test_cobol_conditions_negatedabbreviatedconditionalexpressionchild_constructor_exists():
    assert callable(cobol_conditions_NegatedAbbreviatedConditionalExpressionChild.__init__)


def test_cobol_conditions_negatedabbreviatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(cobol_conditions_NegatedAbbreviatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_negatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(NegatedConditionalExpressionChild)


def test_negatedconditionalexpressionchild_constructor_exists():
    assert callable(NegatedConditionalExpressionChild.__init__)


def test_negatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(NegatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_classcondition_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_ClassCondition)


def test_cobol_conditions_classcondition_constructor_exists():
    assert callable(cobol_conditions_ClassCondition.__init__)


def test_cobol_conditions_classcondition_constructor_args():
    sig = inspect.signature(cobol_conditions_ClassCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_signcondition_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_SignCondition)


def test_cobol_conditions_signcondition_constructor_exists():
    assert callable(cobol_conditions_SignCondition.__init__)


def test_cobol_conditions_signcondition_constructor_args():
    sig = inspect.signature(cobol_conditions_SignCondition.__init__)
    params = list(sig.parameters.keys())



def test_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalAndExpressionChild)


def test_conditionalandexpressionchild_constructor_exists():
    assert callable(ConditionalAndExpressionChild.__init__)


def test_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_abbreviatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_AbbreviatedConditionalExpressionChild)


def test_cobol_conditions_abbreviatedconditionalexpressionchild_constructor_exists():
    assert callable(cobol_conditions_AbbreviatedConditionalExpressionChild.__init__)


def test_cobol_conditions_abbreviatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(cobol_conditions_AbbreviatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_abbreviatedconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_AbbreviatedConditionalExpression)


def test_cobol_conditions_abbreviatedconditionalexpression_constructor_exists():
    assert callable(cobol_conditions_AbbreviatedConditionalExpression.__init__)


def test_cobol_conditions_abbreviatedconditionalexpression_constructor_args():
    sig = inspect.signature(cobol_conditions_AbbreviatedConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_negatedconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_NegatedConditionalExpression)


def test_cobol_conditions_negatedconditionalexpression_constructor_exists():
    assert callable(cobol_conditions_NegatedConditionalExpression.__init__)


def test_cobol_conditions_negatedconditionalexpression_constructor_args():
    sig = inspect.signature(cobol_conditions_NegatedConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_logicaloperator_is_not_abstract():
    assert not inspect.isabstract(LogicalOperator)


def test_logicaloperator_constructor_exists():
    assert callable(LogicalOperator.__init__)


def test_logicaloperator_constructor_args():
    sig = inspect.signature(LogicalOperator.__init__)
    params = list(sig.parameters.keys())



def test_conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalOrExpressionChild)


def test_conditionalorexpressionchild_constructor_exists():
    assert callable(ConditionalOrExpressionChild.__init__)


def test_conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_ConditionalAndExpression)


def test_cobol_conditions_conditionalandexpression_constructor_exists():
    assert callable(cobol_conditions_ConditionalAndExpression.__init__)


def test_cobol_conditions_conditionalandexpression_constructor_args():
    sig = inspect.signature(cobol_conditions_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_ConditionalAndExpressionChild)


def test_cobol_conditions_conditionalandexpressionchild_constructor_exists():
    assert callable(cobol_conditions_ConditionalAndExpressionChild.__init__)


def test_cobol_conditions_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(cobol_conditions_ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_ConditionalOrExpressionChild)


def test_cobol_conditions_conditionalorexpressionchild_constructor_exists():
    assert callable(cobol_conditions_ConditionalOrExpressionChild.__init__)


def test_cobol_conditions_conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(cobol_conditions_ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_ConditionalOrExpression)


def test_cobol_conditions_conditionalorexpression_constructor_exists():
    assert callable(cobol_conditions_ConditionalOrExpression.__init__)


def test_cobol_conditions_conditionalorexpression_constructor_args():
    sig = inspect.signature(cobol_conditions_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_condition_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_Condition)


def test_cobol_conditions_condition_constructor_exists():
    assert callable(cobol_conditions_Condition.__init__)


def test_cobol_conditions_condition_constructor_args():
    sig = inspect.signature(cobol_conditions_Condition.__init__)
    params = list(sig.parameters.keys())



def test_is_is_not_abstract():
    assert not inspect.isabstract(Is)


def test_is_constructor_exists():
    assert callable(Is.__init__)


def test_is_constructor_args():
    sig = inspect.signature(Is.__init__)
    params = list(sig.parameters.keys())



def test_relationaloperator_is_not_abstract():
    assert not inspect.isabstract(RelationalOperator)


def test_relationaloperator_constructor_exists():
    assert callable(RelationalOperator.__init__)


def test_relationaloperator_constructor_args():
    sig = inspect.signature(RelationalOperator.__init__)
    params = list(sig.parameters.keys())



def test_simpleconditionchild_is_not_abstract():
    assert not inspect.isabstract(SimpleConditionChild)


def test_simpleconditionchild_constructor_exists():
    assert callable(SimpleConditionChild.__init__)


def test_simpleconditionchild_constructor_args():
    sig = inspect.signature(SimpleConditionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_nestedcondition_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_NestedCondition)


def test_cobol_conditions_nestedcondition_constructor_exists():
    assert callable(cobol_conditions_NestedCondition.__init__)


def test_cobol_conditions_nestedcondition_constructor_args():
    sig = inspect.signature(cobol_conditions_NestedCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_RelationalExpression)


def test_cobol_conditions_relationalexpression_constructor_exists():
    assert callable(cobol_conditions_RelationalExpression.__init__)


def test_cobol_conditions_relationalexpression_constructor_args():
    sig = inspect.signature(cobol_conditions_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_simpleconditionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_SimpleConditionChild)


def test_cobol_conditions_simpleconditionchild_constructor_exists():
    assert callable(cobol_conditions_SimpleConditionChild.__init__)


def test_cobol_conditions_simpleconditionchild_constructor_args():
    sig = inspect.signature(cobol_conditions_SimpleConditionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol_conditions_negatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol_conditions_NegatedConditionalExpressionChild)


def test_cobol_conditions_negatedconditionalexpressionchild_constructor_exists():
    assert callable(cobol_conditions_NegatedConditionalExpressionChild.__init__)


def test_cobol_conditions_negatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(cobol_conditions_NegatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_negate_is_not_abstract():
    assert not inspect.isabstract(Negate)


def test_negate_constructor_exists():
    assert callable(Negate.__init__)


def test_negate_constructor_args():
    sig = inspect.signature(Negate.__init__)
    params = list(sig.parameters.keys())



def test_cobol_commons_commentable_is_not_abstract():
    assert not inspect.isabstract(cobol_commons_Commentable)


def test_cobol_commons_commentable_constructor_exists():
    assert callable(cobol_commons_Commentable.__init__)


def test_cobol_commons_commentable_constructor_args():
    sig = inspect.signature(cobol_commons_Commentable.__init__)
    params = list(sig.parameters.keys())



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_cobol_commons_uriableelement_is_not_abstract():
    assert not inspect.isabstract(cobol_commons_URIableElement)


def test_cobol_commons_uriableelement_constructor_exists():
    assert callable(cobol_commons_URIableElement.__init__)


def test_cobol_commons_uriableelement_constructor_args():
    sig = inspect.signature(cobol_commons_URIableElement.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_cobol_commons_uriableelement_has_uri():
    assert hasattr(cobol_commons_URIableElement, "uri")
    descriptor = None
    for klass in cobol_commons_URIableElement.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_cobol_commons_labellableelement_is_not_abstract():
    assert not inspect.isabstract(cobol_commons_LabellableElement)


def test_cobol_commons_labellableelement_constructor_exists():
    assert callable(cobol_commons_LabellableElement.__init__)


def test_cobol_commons_labellableelement_constructor_args():
    sig = inspect.signature(cobol_commons_LabellableElement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_cobol_commons_labellableelement_has_label():
    assert hasattr(cobol_commons_LabellableElement, "label")
    descriptor = None
    for klass in cobol_commons_LabellableElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_cobol_commons_namedelement_is_not_abstract():
    assert not inspect.isabstract(cobol_commons_NamedElement)


def test_cobol_commons_namedelement_constructor_exists():
    assert callable(cobol_commons_NamedElement.__init__)


def test_cobol_commons_namedelement_constructor_args():
    sig = inspect.signature(cobol_commons_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cobol_commons_namedelement_has_name():
    assert hasattr(cobol_commons_NamedElement, "name")
    descriptor = None
    for klass in cobol_commons_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datadivisionsection_is_not_abstract():
    assert not inspect.isabstract(DataDivisionSection)


def test_datadivisionsection_constructor_exists():
    assert callable(DataDivisionSection.__init__)


def test_datadivisionsection_constructor_args():
    sig = inspect.signature(DataDivisionSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sections_linkagestoragesection_is_not_abstract():
    assert not inspect.isabstract(cobol_sections_LinkageStorageSection)


def test_cobol_sections_linkagestoragesection_constructor_exists():
    assert callable(cobol_sections_LinkageStorageSection.__init__)


def test_cobol_sections_linkagestoragesection_constructor_args():
    sig = inspect.signature(cobol_sections_LinkageStorageSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sections_localstoragesection_is_not_abstract():
    assert not inspect.isabstract(cobol_sections_LocalStorageSection)


def test_cobol_sections_localstoragesection_constructor_exists():
    assert callable(cobol_sections_LocalStorageSection.__init__)


def test_cobol_sections_localstoragesection_constructor_args():
    sig = inspect.signature(cobol_sections_LocalStorageSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sections_filesection_is_not_abstract():
    assert not inspect.isabstract(cobol_sections_FileSection)


def test_cobol_sections_filesection_constructor_exists():
    assert callable(cobol_sections_FileSection.__init__)


def test_cobol_sections_filesection_constructor_args():
    sig = inspect.signature(cobol_sections_FileSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sections_workingstoragesection_is_not_abstract():
    assert not inspect.isabstract(cobol_sections_WorkingStorageSection)


def test_cobol_sections_workingstoragesection_constructor_exists():
    assert callable(cobol_sections_WorkingStorageSection.__init__)


def test_cobol_sections_workingstoragesection_constructor_args():
    sig = inspect.signature(cobol_sections_WorkingStorageSection.__init__)
    params = list(sig.parameters.keys())



def test_operands_arithmeticoperand_is_not_abstract():
    assert not inspect.isabstract(operands_ArithmeticOperand)


def test_operands_arithmeticoperand_constructor_exists():
    assert callable(operands_ArithmeticOperand.__init__)


def test_operands_arithmeticoperand_constructor_args():
    sig = inspect.signature(operands_ArithmeticOperand.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(arithmetics_PrimaryExpression)


def test_arithmetics_primaryexpression_constructor_exists():
    assert callable(arithmetics_PrimaryExpression.__init__)


def test_arithmetics_primaryexpression_constructor_args():
    sig = inspect.signature(arithmetics_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_operands_operand_is_not_abstract():
    assert not inspect.isabstract(operands_Operand)


def test_operands_operand_constructor_exists():
    assert callable(operands_Operand.__init__)


def test_operands_operand_constructor_args():
    sig = inspect.signature(operands_Operand.__init__)
    params = list(sig.parameters.keys())



def test_operands_replacementoperand_is_not_abstract():
    assert not inspect.isabstract(operands_ReplacementOperand)


def test_operands_replacementoperand_constructor_exists():
    assert callable(operands_ReplacementOperand.__init__)


def test_operands_replacementoperand_constructor_args():
    sig = inspect.signature(operands_ReplacementOperand.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operands_primaryoperand_is_not_abstract():
    assert not inspect.isabstract(cobol_operands_PrimaryOperand)


def test_cobol_operands_primaryoperand_constructor_exists():
    assert callable(cobol_operands_PrimaryOperand.__init__)


def test_cobol_operands_primaryoperand_constructor_args():
    sig = inspect.signature(cobol_operands_PrimaryOperand.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sentences_sentence_is_not_abstract():
    assert not inspect.isabstract(cobol_sentences_Sentence)


def test_cobol_sentences_sentence_constructor_exists():
    assert callable(cobol_sentences_Sentence.__init__)


def test_cobol_sentences_sentence_constructor_args():
    sig = inspect.signature(cobol_sentences_Sentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sentences_executesentence_is_not_abstract():
    assert not inspect.isabstract(cobol_sentences_ExecuteSentence)


def test_cobol_sentences_executesentence_constructor_exists():
    assert callable(cobol_sentences_ExecuteSentence.__init__)


def test_cobol_sentences_executesentence_constructor_args():
    sig = inspect.signature(cobol_sentences_ExecuteSentence.__init__)
    params = list(sig.parameters.keys())



def test_sentences_statementcontainer_is_not_abstract():
    assert not inspect.isabstract(sentences_StatementContainer)


def test_sentences_statementcontainer_constructor_exists():
    assert callable(sentences_StatementContainer.__init__)


def test_sentences_statementcontainer_constructor_args():
    sig = inspect.signature(sentences_StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sentences_usesentence_is_not_abstract():
    assert not inspect.isabstract(cobol_sentences_UseSentence)


def test_cobol_sentences_usesentence_constructor_exists():
    assert callable(cobol_sentences_UseSentence.__init__)


def test_cobol_sentences_usesentence_constructor_args():
    sig = inspect.signature(cobol_sentences_UseSentence.__init__)
    params = list(sig.parameters.keys())



def test_sentence_is_not_abstract():
    assert not inspect.isabstract(Sentence)


def test_sentence_constructor_exists():
    assert callable(Sentence.__init__)


def test_sentence_constructor_args():
    sig = inspect.signature(Sentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sentences_exitprocedure_is_not_abstract():
    assert not inspect.isabstract(cobol_sentences_ExitProcedure)


def test_cobol_sentences_exitprocedure_constructor_exists():
    assert callable(cobol_sentences_ExitProcedure.__init__)


def test_cobol_sentences_exitprocedure_constructor_args():
    sig = inspect.signature(cobol_sentences_ExitProcedure.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sentences_entrysentence_is_not_abstract():
    assert not inspect.isabstract(cobol_sentences_EntrySentence)


def test_cobol_sentences_entrysentence_constructor_exists():
    assert callable(cobol_sentences_EntrySentence.__init__)


def test_cobol_sentences_entrysentence_constructor_args():
    sig = inspect.signature(cobol_sentences_EntrySentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sentences_alteredgoto_is_not_abstract():
    assert not inspect.isabstract(cobol_sentences_AlteredGoTo)


def test_cobol_sentences_alteredgoto_constructor_exists():
    assert callable(cobol_sentences_AlteredGoTo.__init__)


def test_cobol_sentences_alteredgoto_constructor_args():
    sig = inspect.signature(cobol_sentences_AlteredGoTo.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sentences_emptysentence_is_not_abstract():
    assert not inspect.isabstract(cobol_sentences_EmptySentence)


def test_cobol_sentences_emptysentence_constructor_exists():
    assert callable(cobol_sentences_EmptySentence.__init__)


def test_cobol_sentences_emptysentence_constructor_args():
    sig = inspect.signature(cobol_sentences_EmptySentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sentences_statementcontainer_is_not_abstract():
    assert not inspect.isabstract(cobol_sentences_StatementContainer)


def test_cobol_sentences_statementcontainer_constructor_exists():
    assert callable(cobol_sentences_StatementContainer.__init__)


def test_cobol_sentences_statementcontainer_constructor_args():
    sig = inspect.signature(cobol_sentences_StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sections_declarativesection_is_not_abstract():
    assert not inspect.isabstract(cobol_sections_DeclarativeSection)


def test_cobol_sections_declarativesection_constructor_exists():
    assert callable(cobol_sections_DeclarativeSection.__init__)


def test_cobol_sections_declarativesection_constructor_args():
    sig = inspect.signature(cobol_sections_DeclarativeSection.__init__)
    params = list(sig.parameters.keys())



def test_filename_is_not_abstract():
    assert not inspect.isabstract(FileName)


def test_filename_constructor_exists():
    assert callable(FileName.__init__)


def test_filename_constructor_args():
    sig = inspect.signature(FileName.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_elementreference_is_not_abstract():
    assert not inspect.isabstract(cobol_references_ElementReference)


def test_cobol_references_elementreference_constructor_exists():
    assert callable(cobol_references_ElementReference.__init__)


def test_cobol_references_elementreference_constructor_args():
    sig = inspect.signature(cobol_references_ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(ReferenceableElement)


def test_referenceableelement_constructor_exists():
    assert callable(ReferenceableElement.__init__)


def test_referenceableelement_constructor_args():
    sig = inspect.signature(ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_specialname_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_SpecialName)


def test_cobol_specialnames_specialname_constructor_exists():
    assert callable(cobol_specialnames_SpecialName.__init__)


def test_cobol_specialnames_specialname_constructor_args():
    sig = inspect.signature(cobol_specialnames_SpecialName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_parameters_parameter_is_not_abstract():
    assert not inspect.isabstract(cobol_parameters_Parameter)


def test_cobol_parameters_parameter_constructor_exists():
    assert callable(cobol_parameters_Parameter.__init__)


def test_cobol_parameters_parameter_constructor_args():
    sig = inspect.signature(cobol_parameters_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_cobol_tables_additionalindexname_is_not_abstract():
    assert not inspect.isabstract(cobol_tables_AdditionalIndexName)


def test_cobol_tables_additionalindexname_constructor_exists():
    assert callable(cobol_tables_AdditionalIndexName.__init__)


def test_cobol_tables_additionalindexname_constructor_args():
    sig = inspect.signature(cobol_tables_AdditionalIndexName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(cobol_references_ReferenceableElement)


def test_cobol_references_referenceableelement_constructor_exists():
    assert callable(cobol_references_ReferenceableElement.__init__)


def test_cobol_references_referenceableelement_constructor_args():
    sig = inspect.signature(cobol_references_ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_reference_is_not_abstract():
    assert not inspect.isabstract(cobol_references_Reference)


def test_cobol_references_reference_constructor_exists():
    assert callable(cobol_references_Reference.__init__)


def test_cobol_references_reference_constructor_args():
    sig = inspect.signature(cobol_references_Reference.__init__)
    params = list(sig.parameters.keys())



def test_cobol_paragraphs_debuggingmode_is_not_abstract():
    assert not inspect.isabstract(cobol_paragraphs_DebuggingMode)


def test_cobol_paragraphs_debuggingmode_constructor_exists():
    assert callable(cobol_paragraphs_DebuggingMode.__init__)


def test_cobol_paragraphs_debuggingmode_constructor_args():
    sig = inspect.signature(cobol_paragraphs_DebuggingMode.__init__)
    params = list(sig.parameters.keys())



def test_specialnamesparagraphwater_is_not_abstract():
    assert not inspect.isabstract(SpecialNamesParagraphWater)


def test_specialnamesparagraphwater_constructor_exists():
    assert callable(SpecialNamesParagraphWater.__init__)


def test_specialnamesparagraphwater_constructor_args():
    sig = inspect.signature(SpecialNamesParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol_water_specialnamesclause_is_not_abstract():
    assert not inspect.isabstract(cobol_water_SpecialNamesClause)


def test_cobol_water_specialnamesclause_constructor_exists():
    assert callable(cobol_water_SpecialNamesClause.__init__)


def test_cobol_water_specialnamesclause_constructor_args():
    sig = inspect.signature(cobol_water_SpecialNamesClause.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_water_specialnamesclause_has_value():
    assert hasattr(cobol_water_SpecialNamesClause, "value")
    descriptor = None
    for klass in cobol_water_SpecialNamesClause.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_specialnamestatement_is_not_abstract():
    assert not inspect.isabstract(SpecialNameStatement)


def test_specialnamestatement_constructor_exists():
    assert callable(SpecialNameStatement.__init__)


def test_specialnamestatement_constructor_args():
    sig = inspect.signature(SpecialNameStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_paragraphs_iosectionparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol_paragraphs_IOSectionParagraph)


def test_cobol_paragraphs_iosectionparagraph_constructor_exists():
    assert callable(cobol_paragraphs_IOSectionParagraph.__init__)


def test_cobol_paragraphs_iosectionparagraph_constructor_args():
    sig = inspect.signature(cobol_paragraphs_IOSectionParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol_paragraphs_configurationsectionparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol_paragraphs_ConfigurationSectionParagraph)


def test_cobol_paragraphs_configurationsectionparagraph_constructor_exists():
    assert callable(cobol_paragraphs_ConfigurationSectionParagraph.__init__)


def test_cobol_paragraphs_configurationsectionparagraph_constructor_args():
    sig = inspect.signature(cobol_paragraphs_ConfigurationSectionParagraph.__init__)
    params = list(sig.parameters.keys())



def test_identifiers_identifierreference_is_not_abstract():
    assert not inspect.isabstract(identifiers_IdentifierReference)


def test_identifiers_identifierreference_constructor_exists():
    assert callable(identifiers_IdentifierReference.__init__)


def test_identifiers_identifierreference_constructor_args():
    sig = inspect.signature(identifiers_IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_qualifiable_is_not_abstract():
    assert not inspect.isabstract(cobol_references_Qualifiable)


def test_cobol_references_qualifiable_constructor_exists():
    assert callable(cobol_references_Qualifiable.__init__)


def test_cobol_references_qualifiable_constructor_args():
    sig = inspect.signature(cobol_references_Qualifiable.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_conditionname_is_not_abstract():
    assert not inspect.isabstract(cobol_references_ConditionName)


def test_cobol_references_conditionname_constructor_exists():
    assert callable(cobol_references_ConditionName.__init__)


def test_cobol_references_conditionname_constructor_args():
    sig = inspect.signature(cobol_references_ConditionName.__init__)
    params = list(sig.parameters.keys())



def test_elementreference_is_not_abstract():
    assert not inspect.isabstract(ElementReference)


def test_elementreference_constructor_exists():
    assert callable(ElementReference.__init__)


def test_elementreference_constructor_args():
    sig = inspect.signature(ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol_identifiers_qualifier_is_not_abstract():
    assert not inspect.isabstract(cobol_identifiers_Qualifier)


def test_cobol_identifiers_qualifier_constructor_exists():
    assert callable(cobol_identifiers_Qualifier.__init__)


def test_cobol_identifiers_qualifier_constructor_args():
    sig = inspect.signature(cobol_identifiers_Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_alphabetnamereference_is_not_abstract():
    assert not inspect.isabstract(cobol_references_AlphabetNameReference)


def test_cobol_references_alphabetnamereference_constructor_exists():
    assert callable(cobol_references_AlphabetNameReference.__init__)


def test_cobol_references_alphabetnamereference_constructor_args():
    sig = inspect.signature(cobol_references_AlphabetNameReference.__init__)
    params = list(sig.parameters.keys())



def test_identifierreference_is_not_abstract():
    assert not inspect.isabstract(IdentifierReference)


def test_identifierreference_constructor_exists():
    assert callable(IdentifierReference.__init__)


def test_identifierreference_constructor_args():
    sig = inspect.signature(IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_indexnamereference_is_not_abstract():
    assert not inspect.isabstract(cobol_references_IndexNameReference)


def test_cobol_references_indexnamereference_constructor_exists():
    assert callable(cobol_references_IndexNameReference.__init__)


def test_cobol_references_indexnamereference_constructor_args():
    sig = inspect.signature(cobol_references_IndexNameReference.__init__)
    params = list(sig.parameters.keys())



def test_references_identifierreferencequalifier_is_not_abstract():
    assert not inspect.isabstract(references_IdentifierReferenceQualifier)


def test_references_identifierreferencequalifier_constructor_exists():
    assert callable(references_IdentifierReferenceQualifier.__init__)


def test_references_identifierreferencequalifier_constructor_args():
    sig = inspect.signature(references_IdentifierReferenceQualifier.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_datanamereference_is_not_abstract():
    assert not inspect.isabstract(cobol_references_DataNameReference)


def test_cobol_references_datanamereference_constructor_exists():
    assert callable(cobol_references_DataNameReference.__init__)


def test_cobol_references_datanamereference_constructor_args():
    sig = inspect.signature(cobol_references_DataNameReference.__init__)
    params = list(sig.parameters.keys())



def test_references_conditionname_is_not_abstract():
    assert not inspect.isabstract(references_ConditionName)


def test_references_conditionname_constructor_exists():
    assert callable(references_ConditionName.__init__)


def test_references_conditionname_constructor_args():
    sig = inspect.signature(references_ConditionName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_conditionnamereference_is_not_abstract():
    assert not inspect.isabstract(cobol_references_ConditionNameReference)


def test_cobol_references_conditionnamereference_constructor_exists():
    assert callable(cobol_references_ConditionNameReference.__init__)


def test_cobol_references_conditionnamereference_constructor_args():
    sig = inspect.signature(cobol_references_ConditionNameReference.__init__)
    params = list(sig.parameters.keys())



def test_references_qualifiable_is_not_abstract():
    assert not inspect.isabstract(references_Qualifiable)


def test_references_qualifiable_constructor_exists():
    assert callable(references_Qualifiable.__init__)


def test_references_qualifiable_constructor_args():
    sig = inspect.signature(references_Qualifiable.__init__)
    params = list(sig.parameters.keys())



def test_cobol_identifiers_linagecounter_is_not_abstract():
    assert not inspect.isabstract(cobol_identifiers_LinageCounter)


def test_cobol_identifiers_linagecounter_constructor_exists():
    assert callable(cobol_identifiers_LinageCounter.__init__)


def test_cobol_identifiers_linagecounter_constructor_args():
    sig = inspect.signature(cobol_identifiers_LinageCounter.__init__)
    params = list(sig.parameters.keys())



def test_references_elementreference_is_not_abstract():
    assert not inspect.isabstract(references_ElementReference)


def test_references_elementreference_constructor_exists():
    assert callable(references_ElementReference.__init__)


def test_references_elementreference_constructor_args():
    sig = inspect.signature(references_ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_filenamereference_is_not_abstract():
    assert not inspect.isabstract(cobol_references_FileNameReference)


def test_cobol_references_filenamereference_constructor_exists():
    assert callable(cobol_references_FileNameReference.__init__)


def test_cobol_references_filenamereference_constructor_args():
    sig = inspect.signature(cobol_references_FileNameReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol_specialnames_symboliccharacterstatement_is_not_abstract():
    assert not inspect.isabstract(cobol_specialnames_SymbolicCharacterStatement)


def test_cobol_specialnames_symboliccharacterstatement_constructor_exists():
    assert callable(cobol_specialnames_SymbolicCharacterStatement.__init__)


def test_cobol_specialnames_symboliccharacterstatement_constructor_args():
    sig = inspect.signature(cobol_specialnames_SymbolicCharacterStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol_identifiers_identifierreference_is_not_abstract():
    assert not inspect.isabstract(cobol_identifiers_IdentifierReference)


def test_cobol_identifiers_identifierreference_constructor_exists():
    assert callable(cobol_identifiers_IdentifierReference.__init__)


def test_cobol_identifiers_identifierreference_constructor_args():
    sig = inspect.signature(cobol_identifiers_IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_identifierreferencequalifier_is_not_abstract():
    assert not inspect.isabstract(cobol_references_IdentifierReferenceQualifier)


def test_cobol_references_identifierreferencequalifier_constructor_exists():
    assert callable(cobol_references_IdentifierReferenceQualifier.__init__)


def test_cobol_references_identifierreferencequalifier_constructor_args():
    sig = inspect.signature(cobol_references_IdentifierReferenceQualifier.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_mnemonicnamereference_is_not_abstract():
    assert not inspect.isabstract(cobol_references_MnemonicNameReference)


def test_cobol_references_mnemonicnamereference_constructor_exists():
    assert callable(cobol_references_MnemonicNameReference.__init__)


def test_cobol_references_mnemonicnamereference_constructor_args():
    sig = inspect.signature(cobol_references_MnemonicNameReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol_references_specialnamesconditionnamereference_is_not_abstract():
    assert not inspect.isabstract(cobol_references_SpecialNamesConditionNameReference)


def test_cobol_references_specialnamesconditionnamereference_constructor_exists():
    assert callable(cobol_references_SpecialNamesConditionNameReference.__init__)


def test_cobol_references_specialnamesconditionnamereference_constructor_args():
    sig = inspect.signature(cobol_references_SpecialNamesConditionNameReference.__init__)
    params = list(sig.parameters.keys())



def test_greaterthan_is_not_abstract():
    assert not inspect.isabstract(GreaterThan)


def test_greaterthan_constructor_exists():
    assert callable(GreaterThan.__init__)


def test_greaterthan_constructor_args():
    sig = inspect.signature(GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_gtphrase_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_GTPhrase)


def test_cobol_operators_gtphrase_constructor_exists():
    assert callable(cobol_operators_GTPhrase.__init__)


def test_cobol_operators_gtphrase_constructor_args():
    sig = inspect.signature(cobol_operators_GTPhrase.__init__)
    params = list(sig.parameters.keys())



def test_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(LessThanOrEqual)


def test_lessthanorequal_constructor_exists():
    assert callable(LessThanOrEqual.__init__)


def test_lessthanorequal_constructor_args():
    sig = inspect.signature(LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_lteqsign_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_LTEQSign)


def test_cobol_operators_lteqsign_constructor_exists():
    assert callable(cobol_operators_LTEQSign.__init__)


def test_cobol_operators_lteqsign_constructor_args():
    sig = inspect.signature(cobol_operators_LTEQSign.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_lteqphrase_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_LTEQPhrase)


def test_cobol_operators_lteqphrase_constructor_exists():
    assert callable(cobol_operators_LTEQPhrase.__init__)


def test_cobol_operators_lteqphrase_constructor_args():
    sig = inspect.signature(cobol_operators_LTEQPhrase.__init__)
    params = list(sig.parameters.keys())



def test_lessthan_is_not_abstract():
    assert not inspect.isabstract(LessThan)


def test_lessthan_constructor_exists():
    assert callable(LessThan.__init__)


def test_lessthan_constructor_args():
    sig = inspect.signature(LessThan.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_ltsign_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_LTSign)


def test_cobol_operators_ltsign_constructor_exists():
    assert callable(cobol_operators_LTSign.__init__)


def test_cobol_operators_ltsign_constructor_args():
    sig = inspect.signature(cobol_operators_LTSign.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_ltphrase_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_LTPhrase)


def test_cobol_operators_ltphrase_constructor_exists():
    assert callable(cobol_operators_LTPhrase.__init__)


def test_cobol_operators_ltphrase_constructor_args():
    sig = inspect.signature(cobol_operators_LTPhrase.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_equalsign_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_EqualSign)


def test_cobol_operators_equalsign_constructor_exists():
    assert callable(cobol_operators_EqualSign.__init__)


def test_cobol_operators_equalsign_constructor_args():
    sig = inspect.signature(cobol_operators_EqualSign.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_equalphrase_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_EqualPhrase)


def test_cobol_operators_equalphrase_constructor_exists():
    assert callable(cobol_operators_EqualPhrase.__init__)


def test_cobol_operators_equalphrase_constructor_args():
    sig = inspect.signature(cobol_operators_EqualPhrase.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_kanji_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Kanji)


def test_cobol_operators_kanji_constructor_exists():
    assert callable(cobol_operators_Kanji.__init__)


def test_cobol_operators_kanji_constructor_args():
    sig = inspect.signature(cobol_operators_Kanji.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_alphabeticlower_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_AlphabeticLower)


def test_cobol_operators_alphabeticlower_constructor_exists():
    assert callable(cobol_operators_AlphabeticLower.__init__)


def test_cobol_operators_alphabeticlower_constructor_args():
    sig = inspect.signature(cobol_operators_AlphabeticLower.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_alphabeticupper_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_AlphabeticUpper)


def test_cobol_operators_alphabeticupper_constructor_exists():
    assert callable(cobol_operators_AlphabeticUpper.__init__)


def test_cobol_operators_alphabeticupper_constructor_args():
    sig = inspect.signature(cobol_operators_AlphabeticUpper.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_numeric_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Numeric)


def test_cobol_operators_numeric_constructor_exists():
    assert callable(cobol_operators_Numeric.__init__)


def test_cobol_operators_numeric_constructor_args():
    sig = inspect.signature(cobol_operators_Numeric.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_dbcs_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_DBCS)


def test_cobol_operators_dbcs_constructor_exists():
    assert callable(cobol_operators_DBCS.__init__)


def test_cobol_operators_dbcs_constructor_args():
    sig = inspect.signature(cobol_operators_DBCS.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_alphabetic_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Alphabetic)


def test_cobol_operators_alphabetic_constructor_exists():
    assert callable(cobol_operators_Alphabetic.__init__)


def test_cobol_operators_alphabetic_constructor_args():
    sig = inspect.signature(cobol_operators_Alphabetic.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_classname_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_ClassName)


def test_cobol_operators_classname_constructor_exists():
    assert callable(cobol_operators_ClassName.__init__)


def test_cobol_operators_classname_constructor_args():
    sig = inspect.signature(cobol_operators_ClassName.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_zero_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Zero)


def test_cobol_operators_zero_constructor_exists():
    assert callable(cobol_operators_Zero.__init__)


def test_cobol_operators_zero_constructor_args():
    sig = inspect.signature(cobol_operators_Zero.__init__)
    params = list(sig.parameters.keys())



def test_paragraphs_iosectionparagraph_is_not_abstract():
    assert not inspect.isabstract(paragraphs_IOSectionParagraph)


def test_paragraphs_iosectionparagraph_constructor_exists():
    assert callable(paragraphs_IOSectionParagraph.__init__)


def test_paragraphs_iosectionparagraph_constructor_args():
    sig = inspect.signature(paragraphs_IOSectionParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol_paragraphs_iocontrolparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol_paragraphs_IOControlParagraph)


def test_cobol_paragraphs_iocontrolparagraph_constructor_exists():
    assert callable(cobol_paragraphs_IOControlParagraph.__init__)


def test_cobol_paragraphs_iocontrolparagraph_constructor_args():
    sig = inspect.signature(cobol_paragraphs_IOControlParagraph.__init__)
    params = list(sig.parameters.keys())



def test_selectstatement_is_not_abstract():
    assert not inspect.isabstract(SelectStatement)


def test_selectstatement_constructor_exists():
    assert callable(SelectStatement.__init__)


def test_selectstatement_constructor_args():
    sig = inspect.signature(SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_iosectionparagraph_is_not_abstract():
    assert not inspect.isabstract(IOSectionParagraph)


def test_iosectionparagraph_constructor_exists():
    assert callable(IOSectionParagraph.__init__)


def test_iosectionparagraph_constructor_args():
    sig = inspect.signature(IOSectionParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol_paragraphs_filecontrolparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol_paragraphs_FileControlParagraph)


def test_cobol_paragraphs_filecontrolparagraph_constructor_exists():
    assert callable(cobol_paragraphs_FileControlParagraph.__init__)


def test_cobol_paragraphs_filecontrolparagraph_constructor_args():
    sig = inspect.signature(cobol_paragraphs_FileControlParagraph.__init__)
    params = list(sig.parameters.keys())



def test_paragraphs_configurationsectionparagraph_is_not_abstract():
    assert not inspect.isabstract(paragraphs_ConfigurationSectionParagraph)


def test_paragraphs_configurationsectionparagraph_constructor_exists():
    assert callable(paragraphs_ConfigurationSectionParagraph.__init__)


def test_paragraphs_configurationsectionparagraph_constructor_args():
    sig = inspect.signature(paragraphs_ConfigurationSectionParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol_paragraphs_repositoryparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol_paragraphs_RepositoryParagraph)


def test_cobol_paragraphs_repositoryparagraph_constructor_exists():
    assert callable(cobol_paragraphs_RepositoryParagraph.__init__)


def test_cobol_paragraphs_repositoryparagraph_constructor_args():
    sig = inspect.signature(cobol_paragraphs_RepositoryParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol_paragraphs_objectcomputerparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol_paragraphs_ObjectComputerParagraph)


def test_cobol_paragraphs_objectcomputerparagraph_constructor_exists():
    assert callable(cobol_paragraphs_ObjectComputerParagraph.__init__)


def test_cobol_paragraphs_objectcomputerparagraph_constructor_args():
    sig = inspect.signature(cobol_paragraphs_ObjectComputerParagraph.__init__)
    params = list(sig.parameters.keys())



def test_debuggingmode_is_not_abstract():
    assert not inspect.isabstract(DebuggingMode)


def test_debuggingmode_constructor_exists():
    assert callable(DebuggingMode.__init__)


def test_debuggingmode_constructor_args():
    sig = inspect.signature(DebuggingMode.__init__)
    params = list(sig.parameters.keys())



def test_configurationsectionparagraph_is_not_abstract():
    assert not inspect.isabstract(ConfigurationSectionParagraph)


def test_configurationsectionparagraph_constructor_exists():
    assert callable(ConfigurationSectionParagraph.__init__)


def test_configurationsectionparagraph_constructor_args():
    sig = inspect.signature(ConfigurationSectionParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol_paragraphs_specialnamesparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol_paragraphs_SpecialNamesParagraph)


def test_cobol_paragraphs_specialnamesparagraph_constructor_exists():
    assert callable(cobol_paragraphs_SpecialNamesParagraph.__init__)


def test_cobol_paragraphs_specialnamesparagraph_constructor_args():
    sig = inspect.signature(cobol_paragraphs_SpecialNamesParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol_paragraphs_sourcecomputerparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol_paragraphs_SourceComputerParagraph)


def test_cobol_paragraphs_sourcecomputerparagraph_constructor_exists():
    assert callable(cobol_paragraphs_SourceComputerParagraph.__init__)


def test_cobol_paragraphs_sourcecomputerparagraph_constructor_args():
    sig = inspect.signature(cobol_paragraphs_SourceComputerParagraph.__init__)
    params = list(sig.parameters.keys())



def test_labels_procedure_is_not_abstract():
    assert not inspect.isabstract(labels_Procedure)


def test_labels_procedure_constructor_exists():
    assert callable(labels_Procedure.__init__)


def test_labels_procedure_constructor_args():
    sig = inspect.signature(labels_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_cobol_sections_section_is_not_abstract():
    assert not inspect.isabstract(cobol_sections_Section)


def test_cobol_sections_section_constructor_exists():
    assert callable(cobol_sections_Section.__init__)


def test_cobol_sections_section_constructor_args():
    sig = inspect.signature(cobol_sections_Section.__init__)
    params = list(sig.parameters.keys())
    assert "segmentNumber" in params, "Missing parameter 'segmentNumber'"

def test_cobol_sections_section_has_segmentNumber():
    assert hasattr(cobol_sections_Section, "segmentNumber")
    descriptor = None
    for klass in cobol_sections_Section.__mro__:
        if "segmentNumber" in klass.__dict__:
            descriptor = klass.__dict__["segmentNumber"]
            break
    assert isinstance(descriptor, property)



def test_cobol_paragraphs_paragraph_is_not_abstract():
    assert not inspect.isabstract(cobol_paragraphs_Paragraph)


def test_cobol_paragraphs_paragraph_constructor_exists():
    assert callable(cobol_paragraphs_Paragraph.__init__)


def test_cobol_paragraphs_paragraph_constructor_args():
    sig = inspect.signature(cobol_paragraphs_Paragraph.__init__)
    params = list(sig.parameters.keys())



def test_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(GreaterThanOrEqual)


def test_greaterthanorequal_constructor_exists():
    assert callable(GreaterThanOrEqual.__init__)


def test_greaterthanorequal_constructor_args():
    sig = inspect.signature(GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_gteqsign_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_GTEQSign)


def test_cobol_operators_gteqsign_constructor_exists():
    assert callable(cobol_operators_GTEQSign.__init__)


def test_cobol_operators_gteqsign_constructor_args():
    sig = inspect.signature(cobol_operators_GTEQSign.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_gteqphrase_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_GTEQPhrase)


def test_cobol_operators_gteqphrase_constructor_exists():
    assert callable(cobol_operators_GTEQPhrase.__init__)


def test_cobol_operators_gteqphrase_constructor_args():
    sig = inspect.signature(cobol_operators_GTEQPhrase.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_gtsign_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_GTSign)


def test_cobol_operators_gtsign_constructor_exists():
    assert callable(cobol_operators_GTSign.__init__)


def test_cobol_operators_gtsign_constructor_args():
    sig = inspect.signature(cobol_operators_GTSign.__init__)
    params = list(sig.parameters.keys())



def test_operators_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(operators_UnaryOperator)


def test_operators_unaryoperator_constructor_exists():
    assert callable(operators_UnaryOperator.__init__)


def test_operators_unaryoperator_constructor_args():
    sig = inspect.signature(operators_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(operators_AdditiveOperator)


def test_operators_additiveoperator_constructor_exists():
    assert callable(operators_AdditiveOperator.__init__)


def test_operators_additiveoperator_constructor_args():
    sig = inspect.signature(operators_AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_subtraction_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Subtraction)


def test_cobol_operators_subtraction_constructor_exists():
    assert callable(cobol_operators_Subtraction.__init__)


def test_cobol_operators_subtraction_constructor_args():
    sig = inspect.signature(cobol_operators_Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_addition_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Addition)


def test_cobol_operators_addition_constructor_exists():
    assert callable(cobol_operators_Addition.__init__)


def test_cobol_operators_addition_constructor_args():
    sig = inspect.signature(cobol_operators_Addition.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_division_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Division)


def test_cobol_operators_division_constructor_exists():
    assert callable(cobol_operators_Division.__init__)


def test_cobol_operators_division_constructor_args():
    sig = inspect.signature(cobol_operators_Division.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_negative_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Negative)


def test_cobol_operators_negative_constructor_exists():
    assert callable(cobol_operators_Negative.__init__)


def test_cobol_operators_negative_constructor_args():
    sig = inspect.signature(cobol_operators_Negative.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_positive_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Positive)


def test_cobol_operators_positive_constructor_exists():
    assert callable(cobol_operators_Positive.__init__)


def test_cobol_operators_positive_constructor_args():
    sig = inspect.signature(cobol_operators_Positive.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_multiplication_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Multiplication)


def test_cobol_operators_multiplication_constructor_exists():
    assert callable(cobol_operators_Multiplication.__init__)


def test_cobol_operators_multiplication_constructor_args():
    sig = inspect.signature(cobol_operators_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_conditionand_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_ConditionAnd)


def test_cobol_operators_conditionand_constructor_exists():
    assert callable(cobol_operators_ConditionAnd.__init__)


def test_cobol_operators_conditionand_constructor_args():
    sig = inspect.signature(cobol_operators_ConditionAnd.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_conditionor_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_ConditionOr)


def test_cobol_operators_conditionor_constructor_exists():
    assert callable(cobol_operators_ConditionOr.__init__)


def test_cobol_operators_conditionor_constructor_args():
    sig = inspect.signature(cobol_operators_ConditionOr.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_logicaloperator_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_LogicalOperator)


def test_cobol_operators_logicaloperator_constructor_exists():
    assert callable(cobol_operators_LogicalOperator.__init__)


def test_cobol_operators_logicaloperator_constructor_args():
    sig = inspect.signature(cobol_operators_LogicalOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_MultiplicativeOperator)


def test_cobol_operators_multiplicativeoperator_constructor_exists():
    assert callable(cobol_operators_MultiplicativeOperator.__init__)


def test_cobol_operators_multiplicativeoperator_constructor_args():
    sig = inspect.signature(cobol_operators_MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_relationaloperator_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_RelationalOperator)


def test_cobol_operators_relationaloperator_constructor_exists():
    assert callable(cobol_operators_RelationalOperator.__init__)


def test_cobol_operators_relationaloperator_constructor_args():
    sig = inspect.signature(cobol_operators_RelationalOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_UnaryOperator)


def test_cobol_operators_unaryoperator_constructor_exists():
    assert callable(cobol_operators_UnaryOperator.__init__)


def test_cobol_operators_unaryoperator_constructor_args():
    sig = inspect.signature(cobol_operators_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_signoperator_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_SignOperator)


def test_cobol_operators_signoperator_constructor_exists():
    assert callable(cobol_operators_SignOperator.__init__)


def test_cobol_operators_signoperator_constructor_args():
    sig = inspect.signature(cobol_operators_SignOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_AdditiveOperator)


def test_cobol_operators_additiveoperator_constructor_exists():
    assert callable(cobol_operators_AdditiveOperator.__init__)


def test_cobol_operators_additiveoperator_constructor_args():
    sig = inspect.signature(cobol_operators_AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_operator_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Operator)


def test_cobol_operators_operator_constructor_exists():
    assert callable(cobol_operators_Operator.__init__)


def test_cobol_operators_operator_constructor_args():
    sig = inspect.signature(cobol_operators_Operator.__init__)
    params = list(sig.parameters.keys())



def test_alphanumericliteral_is_not_abstract():
    assert not inspect.isabstract(AlphanumericLiteral)


def test_alphanumericliteral_constructor_exists():
    assert callable(AlphanumericLiteral.__init__)


def test_alphanumericliteral_constructor_args():
    sig = inspect.signature(AlphanumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_alphanumerichexadecimalliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_AlphanumericHexaDecimalLiteral)


def test_cobol_literals_alphanumerichexadecimalliteral_constructor_exists():
    assert callable(cobol_literals_AlphanumericHexaDecimalLiteral.__init__)


def test_cobol_literals_alphanumerichexadecimalliteral_constructor_args():
    sig = inspect.signature(cobol_literals_AlphanumericHexaDecimalLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_classoperator_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_ClassOperator)


def test_cobol_operators_classoperator_constructor_exists():
    assert callable(cobol_operators_ClassOperator.__init__)


def test_cobol_operators_classoperator_constructor_args():
    sig = inspect.signature(cobol_operators_ClassOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_through_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Through)


def test_cobol_operators_through_constructor_exists():
    assert callable(cobol_operators_Through.__init__)


def test_cobol_operators_through_constructor_args():
    sig = inspect.signature(cobol_operators_Through.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_operators_through_has_value():
    assert hasattr(cobol_operators_Through, "value")
    descriptor = None
    for klass in cobol_operators_Through.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_operators_negate_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Negate)


def test_cobol_operators_negate_constructor_exists():
    assert callable(cobol_operators_Negate.__init__)


def test_cobol_operators_negate_constructor_args():
    sig = inspect.signature(cobol_operators_Negate.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_power_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Power)


def test_cobol_operators_power_constructor_exists():
    assert callable(cobol_operators_Power.__init__)


def test_cobol_operators_power_constructor_args():
    sig = inspect.signature(cobol_operators_Power.__init__)
    params = list(sig.parameters.keys())



def test_cobol_operators_equal_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_Equal)


def test_cobol_operators_equal_constructor_exists():
    assert callable(cobol_operators_Equal.__init__)


def test_cobol_operators_equal_constructor_args():
    sig = inspect.signature(cobol_operators_Equal.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_cobol_operators_equal_has_to():
    assert hasattr(cobol_operators_Equal, "to")
    descriptor = None
    for klass in cobol_operators_Equal.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_cobol_operators_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_LessThanOrEqual)


def test_cobol_operators_lessthanorequal_constructor_exists():
    assert callable(cobol_operators_LessThanOrEqual.__init__)


def test_cobol_operators_lessthanorequal_constructor_args():
    sig = inspect.signature(cobol_operators_LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())
    assert "than" in params, "Missing parameter 'than'"
    assert "to" in params, "Missing parameter 'to'"

def test_cobol_operators_lessthanorequal_has_than():
    assert hasattr(cobol_operators_LessThanOrEqual, "than")
    descriptor = None
    for klass in cobol_operators_LessThanOrEqual.__mro__:
        if "than" in klass.__dict__:
            descriptor = klass.__dict__["than"]
            break
    assert isinstance(descriptor, property)

def test_cobol_operators_lessthanorequal_has_to():
    assert hasattr(cobol_operators_LessThanOrEqual, "to")
    descriptor = None
    for klass in cobol_operators_LessThanOrEqual.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_cobol_operators_lessthan_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_LessThan)


def test_cobol_operators_lessthan_constructor_exists():
    assert callable(cobol_operators_LessThan.__init__)


def test_cobol_operators_lessthan_constructor_args():
    sig = inspect.signature(cobol_operators_LessThan.__init__)
    params = list(sig.parameters.keys())
    assert "than" in params, "Missing parameter 'than'"

def test_cobol_operators_lessthan_has_than():
    assert hasattr(cobol_operators_LessThan, "than")
    descriptor = None
    for klass in cobol_operators_LessThan.__mro__:
        if "than" in klass.__dict__:
            descriptor = klass.__dict__["than"]
            break
    assert isinstance(descriptor, property)



def test_cobol_operators_greaterthan_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_GreaterThan)


def test_cobol_operators_greaterthan_constructor_exists():
    assert callable(cobol_operators_GreaterThan.__init__)


def test_cobol_operators_greaterthan_constructor_args():
    sig = inspect.signature(cobol_operators_GreaterThan.__init__)
    params = list(sig.parameters.keys())
    assert "than" in params, "Missing parameter 'than'"

def test_cobol_operators_greaterthan_has_than():
    assert hasattr(cobol_operators_GreaterThan, "than")
    descriptor = None
    for klass in cobol_operators_GreaterThan.__mro__:
        if "than" in klass.__dict__:
            descriptor = klass.__dict__["than"]
            break
    assert isinstance(descriptor, property)



def test_cobol_operators_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(cobol_operators_GreaterThanOrEqual)


def test_cobol_operators_greaterthanorequal_constructor_exists():
    assert callable(cobol_operators_GreaterThanOrEqual.__init__)


def test_cobol_operators_greaterthanorequal_constructor_args():
    sig = inspect.signature(cobol_operators_GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "than" in params, "Missing parameter 'than'"

def test_cobol_operators_greaterthanorequal_has_to():
    assert hasattr(cobol_operators_GreaterThanOrEqual, "to")
    descriptor = None
    for klass in cobol_operators_GreaterThanOrEqual.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_cobol_operators_greaterthanorequal_has_than():
    assert hasattr(cobol_operators_GreaterThanOrEqual, "than")
    descriptor = None
    for klass in cobol_operators_GreaterThanOrEqual.__mro__:
        if "than" in klass.__dict__:
            descriptor = klass.__dict__["than"]
            break
    assert isinstance(descriptor, property)



def test_cobol_literals_highvalue_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_HighValue)


def test_cobol_literals_highvalue_constructor_exists():
    assert callable(cobol_literals_HighValue.__init__)


def test_cobol_literals_highvalue_constructor_args():
    sig = inspect.signature(cobol_literals_HighValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_highvalue_has_value():
    assert hasattr(cobol_literals_HighValue, "value")
    descriptor = None
    for klass in cobol_literals_HighValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_literals_lowvalue_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_LowValue)


def test_cobol_literals_lowvalue_constructor_exists():
    assert callable(cobol_literals_LowValue.__init__)


def test_cobol_literals_lowvalue_constructor_args():
    sig = inspect.signature(cobol_literals_LowValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_lowvalue_has_value():
    assert hasattr(cobol_literals_LowValue, "value")
    descriptor = None
    for klass in cobol_literals_LowValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_literals_quote_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_Quote)


def test_cobol_literals_quote_constructor_exists():
    assert callable(cobol_literals_Quote.__init__)


def test_cobol_literals_quote_constructor_args():
    sig = inspect.signature(cobol_literals_Quote.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_quote_has_value():
    assert hasattr(cobol_literals_Quote, "value")
    descriptor = None
    for klass in cobol_literals_Quote.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_literals_zero_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_Zero)


def test_cobol_literals_zero_constructor_exists():
    assert callable(cobol_literals_Zero.__init__)


def test_cobol_literals_zero_constructor_args():
    sig = inspect.signature(cobol_literals_Zero.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_zero_has_value():
    assert hasattr(cobol_literals_Zero, "value")
    descriptor = None
    for klass in cobol_literals_Zero.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_literals_null_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_Null)


def test_cobol_literals_null_constructor_exists():
    assert callable(cobol_literals_Null.__init__)


def test_cobol_literals_null_constructor_args():
    sig = inspect.signature(cobol_literals_Null.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_null_has_value():
    assert hasattr(cobol_literals_Null, "value")
    descriptor = None
    for klass in cobol_literals_Null.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_literals_fixeddecimalliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_FixedDecimalLiteral)


def test_cobol_literals_fixeddecimalliteral_constructor_exists():
    assert callable(cobol_literals_FixedDecimalLiteral.__init__)


def test_cobol_literals_fixeddecimalliteral_constructor_args():
    sig = inspect.signature(cobol_literals_FixedDecimalLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbcsliteral_is_not_abstract():
    assert not inspect.isabstract(DBCSLiteral)


def test_dbcsliteral_constructor_exists():
    assert callable(DBCSLiteral.__init__)


def test_dbcsliteral_constructor_args():
    sig = inspect.signature(DBCSLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_nationalhexliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_NationalHexLiteral)


def test_cobol_literals_nationalhexliteral_constructor_exists():
    assert callable(cobol_literals_NationalHexLiteral.__init__)


def test_cobol_literals_nationalhexliteral_constructor_args():
    sig = inspect.signature(cobol_literals_NationalHexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_nationalhexliteral_has_value():
    assert hasattr(cobol_literals_NationalHexLiteral, "value")
    descriptor = None
    for klass in cobol_literals_NationalHexLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_literals_nationalliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_NationalLiteral)


def test_cobol_literals_nationalliteral_constructor_exists():
    assert callable(cobol_literals_NationalLiteral.__init__)


def test_cobol_literals_nationalliteral_constructor_args():
    sig = inspect.signature(cobol_literals_NationalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_nationalliteral_has_value():
    assert hasattr(cobol_literals_NationalLiteral, "value")
    descriptor = None
    for klass in cobol_literals_NationalLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_literals_dbcsliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_DBCSLiteral)


def test_cobol_literals_dbcsliteral_constructor_exists():
    assert callable(cobol_literals_DBCSLiteral.__init__)


def test_cobol_literals_dbcsliteral_constructor_args():
    sig = inspect.signature(cobol_literals_DBCSLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_pseudoliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_PseudoLiteral)


def test_cobol_literals_pseudoliteral_constructor_exists():
    assert callable(cobol_literals_PseudoLiteral.__init__)


def test_cobol_literals_pseudoliteral_constructor_args():
    sig = inspect.signature(cobol_literals_PseudoLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_pseudoliteral_has_value():
    assert hasattr(cobol_literals_PseudoLiteral, "value")
    descriptor = None
    for klass in cobol_literals_PseudoLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol_literals_characters_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_Characters)


def test_cobol_literals_characters_constructor_exists():
    assert callable(cobol_literals_Characters.__init__)


def test_cobol_literals_characters_constructor_args():
    sig = inspect.signature(cobol_literals_Characters.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_any_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_Any)


def test_cobol_literals_any_constructor_exists():
    assert callable(cobol_literals_Any.__init__)


def test_cobol_literals_any_constructor_args():
    sig = inspect.signature(cobol_literals_Any.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_space_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_Space)


def test_cobol_literals_space_constructor_exists():
    assert callable(cobol_literals_Space.__init__)


def test_cobol_literals_space_constructor_args():
    sig = inspect.signature(cobol_literals_Space.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol_literals_space_has_value():
    assert hasattr(cobol_literals_Space, "value")
    descriptor = None
    for klass in cobol_literals_Space.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_labels_stoplabel_is_not_abstract():
    assert not inspect.isabstract(labels_StopLabel)


def test_labels_stoplabel_constructor_exists():
    assert callable(labels_StopLabel.__init__)


def test_labels_stoplabel_constructor_args():
    sig = inspect.signature(labels_StopLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_literal_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_Literal)


def test_cobol_literals_literal_constructor_exists():
    assert callable(cobol_literals_Literal.__init__)


def test_cobol_literals_literal_constructor_args():
    sig = inspect.signature(cobol_literals_Literal.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_constantliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_ConstantLiteral)


def test_cobol_literals_constantliteral_constructor_exists():
    assert callable(cobol_literals_ConstantLiteral.__init__)


def test_cobol_literals_constantliteral_constructor_args():
    sig = inspect.signature(cobol_literals_ConstantLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol_literals_numericliteral_is_not_abstract():
    assert not inspect.isabstract(cobol_literals_NumericLiteral)


def test_cobol_literals_numericliteral_constructor_exists():
    assert callable(cobol_literals_NumericLiteral.__init__)


def test_cobol_literals_numericliteral_constructor_args():
    sig = inspect.signature(cobol_literals_NumericLiteral.__init__)
    params = list(sig.parameters.keys())

def test_datadescriptioninfo_exists():
    # Check that the Enumeration exists
    assert DataDescriptionInfo is not None

def test_datadescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataDescriptionInfo]
    expected_literals = [
        "left",
        "sync",
        "character",
        "separate",
        "when",
        "is_",
        "date",
        "zeros",
        "sign",
        "leading",
        "trailing",
        "zeroes",
        "right",
        "synchronized",
        "format",
        "zero",
        "just",
        "justified",
        "blank",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataDescriptionInfo"

def test_channels_exists():
    # Check that the Enumeration exists
    assert Channels is not None

def test_channels_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Channels]
    expected_literals = [
        "c3",
        "c6",
        "c4",
        "c12",
        "c2",
        "c10",
        "c9",
        "c8",
        "c11",
        "c5",
        "c7",
        "c1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Channels"

def test_zeroes_exists():
    # Check that the Enumeration exists
    assert Zeroes is not None

def test_zeroes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Zeroes]
    expected_literals = [
        "zero",
        "zeroes",
        "zeros",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Zeroes"

def test_highvalues_exists():
    # Check that the Enumeration exists
    assert HighValues is not None

def test_highvalues_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HighValues]
    expected_literals = [
        "highValue",
        "highValues",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HighValues"

def test_orders_exists():
    # Check that the Enumeration exists
    assert Orders is not None

def test_orders_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orders]
    expected_literals = [
        "asc",
        "dsc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orders"

def test_eop_exists():
    # Check that the Enumeration exists
    assert EOP is not None

def test_eop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EOP]
    expected_literals = [
        "endOfPage",
        "eop",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EOP"

def test_repositorydescriptioninfo_exists():
    # Check that the Enumeration exists
    assert RepositoryDescriptionInfo is not None

def test_repositorydescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RepositoryDescriptionInfo]
    expected_literals = [
        "is_",
        "class_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RepositoryDescriptionInfo"

def test_objectcomputerdescriptioninfo_exists():
    # Check that the Enumeration exists
    assert ObjectComputerDescriptionInfo is not None

def test_objectcomputerdescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectComputerDescriptionInfo]
    expected_literals = [
        "memory",
        "modules",
        "sequence",
        "program",
        "collating",
        "words",
        "size",
        "segmentLimit",
        "segment",
        "characters",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectComputerDescriptionInfo"

def test_selectstatementclauses_exists():
    # Check that the Enumeration exists
    assert SelectStatementClauses is not None

def test_selectstatementclauses_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectStatementClauses]
    expected_literals = [
        "sequential",
        "padding",
        "reserve",
        "access",
        "indexed",
        "relative",
        "standard1",
        "character",
        "areas",
        "record",
        "alternate",
        "is_",
        "random",
        "with_",
        "mode",
        "dynamic",
        "delimiter",
        "organization",
        "key",
        "area",
        "duplicates",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectStatementClauses"

def test_corresponding_exists():
    # Check that the Enumeration exists
    assert Corresponding is not None

def test_corresponding_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Corresponding]
    expected_literals = [
        "corr",
        "corresponding",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Corresponding"

def test_sortingorder_exists():
    # Check that the Enumeration exists
    assert SortingOrder is not None

def test_sortingorder_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortingOrder]
    expected_literals = [
        "asc",
        "dsc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SortingOrder"

def test_systemoutputs_exists():
    # Check that the Enumeration exists
    assert SystemOutputs is not None

def test_systemoutputs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemOutputs]
    expected_literals = [
        "syslist",
        "syslst",
        "sysout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemOutputs"

def test_specialnamesclauses_exists():
    # Check that the Enumeration exists
    assert SpecialNamesClauses is not None

def test_specialnamesclauses_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpecialNamesClauses]
    expected_literals = [
        "comma",
        "is_",
        "decimalPoint",
        "xmlSchema",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpecialNamesClauses"

def test_lowvalues_exists():
    # Check that the Enumeration exists
    assert LowValues is not None

def test_lowvalues_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LowValues]
    expected_literals = [
        "lowValues",
        "lowValue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LowValues"

def test_encodingtypes_exists():
    # Check that the Enumeration exists
    assert EncodingTypes is not None

def test_encodingtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EncodingTypes]
    expected_literals = [
        "national",
        "alphanumeric",
        "alphanumericEdited",
        "alphabetic",
        "egcs",
        "numeric",
        "dbcs",
        "nationalEdited",
        "numericEdited",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EncodingTypes"

def test_closestatementtokens_exists():
    # Check that the Enumeration exists
    assert CloseStatementTokens is not None

def test_closestatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CloseStatementTokens]
    expected_literals = [
        "with_",
        "removal",
        "no",
        "rewind",
        "unit",
        "lock",
        "for_",
        "reel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CloseStatementTokens"

def test_predefinedalphabettypes_exists():
    # Check that the Enumeration exists
    assert PredefinedAlphabetTypes is not None

def test_predefinedalphabettypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PredefinedAlphabetTypes]
    expected_literals = [
        "standard2",
        "native",
        "ebcdic",
        "standard1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PredefinedAlphabetTypes"

def test_nulls_exists():
    # Check that the Enumeration exists
    assert Nulls is not None

def test_nulls_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Nulls]
    expected_literals = [
        "null",
        "nulls",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Nulls"

def test_positions_exists():
    # Check that the Enumeration exists
    assert Positions is not None

def test_positions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Positions]
    expected_literals = [
        "after",
        "before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Positions"

def test_filedescriptioninfo_exists():
    # Check that the Enumeration exists
    assert FileDescriptionInfo is not None

def test_filedescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FileDescriptionInfo]
    expected_literals = [
        "value",
        "u",
        "codeSet",
        "s",
        "to",
        "id",
        "size",
        "mode",
        "depending",
        "records",
        "linage",
        "top",
        "in_",
        "contains",
        "from_",
        "of",
        "recording",
        "record",
        "on",
        "report",
        "bottom",
        "with_",
        "standard",
        "is_",
        "varying",
        "lines",
        "f",
        "block",
        "footing",
        "characters",
        "data",
        "reports",
        "omitted",
        "label",
        "v",
        "identification",
        "are",
        "at",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FileDescriptionInfo"

def test_iocontroldescriptioninfo_exists():
    # Check that the Enumeration exists
    assert IOControlDescriptionInfo is not None

def test_iocontroldescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IOControlDescriptionInfo]
    expected_literals = [
        "same",
        "apply",
        "unit",
        "for_",
        "writeOnly",
        "sort",
        "file",
        "on",
        "position",
        "reel",
        "records",
        "area",
        "contains",
        "every",
        "tape",
        "of",
        "rerun",
        "multiple",
        "sortMerge",
        "record",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IOControlDescriptionInfo"

def test_picturestringcharacters_exists():
    # Check that the Enumeration exists
    assert PictureStringCharacters is not None

def test_picturestringcharacters_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PictureStringCharacters]
    expected_literals = [
        "credit",
        "national",
        "numeric",
        "negative",
        "asterik",
        "sign",
        "dollar",
        "plus",
        "decimalPoint",
        "zero",
        "slash",
        "blank",
        "alphabetic",
        "assumedDecimalPoint",
        "debit",
        "any",
        "period",
        "exponent",
        "escape",
        "leadingZero",
        "comma",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PictureStringCharacters"

def test_spaces_exists():
    # Check that the Enumeration exists
    assert Spaces is not None

def test_spaces_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Spaces]
    expected_literals = [
        "spaces",
        "space",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Spaces"

def test_status_exists():
    # Check that the Enumeration exists
    assert Status is not None

def test_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Status]
    expected_literals = [
        "off",
        "on",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Status"

def test_properties_exists():
    # Check that the Enumeration exists
    assert Properties is not None

def test_properties_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Properties]
    expected_literals = [
        "initial",
        "recursive",
        "common",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Properties"

def test_invokestatementtokens_exists():
    # Check that the Enumeration exists
    assert InvokeStatementTokens is not None

def test_invokestatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InvokeStatementTokens]
    expected_literals = [
        "of",
        "self",
        "by",
        "new",
        "value",
        "length",
        "returning",
        "super",
        "using",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InvokeStatementTokens"

def test_selects_exists():
    # Check that the Enumeration exists
    assert Selects is not None

def test_selects_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Selects]
    expected_literals = [
        "s2",
        "s4",
        "s3",
        "s1",
        "s5",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Selects"

def test_systempunchdevices_exists():
    # Check that the Enumeration exists
    assert SystemPunchDevices is not None

def test_systempunchdevices_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemPunchDevices]
    expected_literals = [
        "syspunch",
        "syspch",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemPunchDevices"

def test_quotes_exists():
    # Check that the Enumeration exists
    assert Quotes is not None

def test_quotes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Quotes]
    expected_literals = [
        "quote",
        "quotes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Quotes"

def test_adjustings_exists():
    # Check that the Enumeration exists
    assert Adjustings is not None

def test_adjustings_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Adjustings]
    expected_literals = [
        "up",
        "down",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Adjustings"

def test_sqlstatementtokens_exists():
    # Check that the Enumeration exists
    assert SQLStatementTokens is not None

def test_sqlstatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SQLStatementTokens]
    expected_literals = [
        "include",
        "update",
        "select",
        "into",
        "insert",
        "delete",
        "declare",
        "from_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SQLStatementTokens"

def test_usages_exists():
    # Check that the Enumeration exists
    assert Usages is not None

def test_usages_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Usages]
    expected_literals = [
        "pointer",
        "comp4",
        "comp5",
        "comp2",
        "procedurePointer",
        "computational1",
        "computational3",
        "functionPointer",
        "binary",
        "national",
        "packedDecimal",
        "computational4",
        "computational5",
        "display1",
        "index",
        "computational",
        "computational2",
        "comp1",
        "display",
        "comp3",
        "comp",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Usages"

def test_throughphrase_exists():
    # Check that the Enumeration exists
    assert ThroughPhrase is not None

def test_throughphrase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ThroughPhrase]
    expected_literals = [
        "through",
        "thru",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ThroughPhrase"

def test_openstatementtokens_exists():
    # Check that the Enumeration exists
    assert OpenStatementTokens is not None

def test_openstatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OpenStatementTokens]
    expected_literals = [
        "rewind",
        "with_",
        "no",
        "reversed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OpenStatementTokens"

def test_exitlabels_exists():
    # Check that the Enumeration exists
    assert ExitLabels is not None

def test_exitlabels_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExitLabels]
    expected_literals = [
        "paragraph",
        "method",
        "program",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExitLabels"

def test_upsiswitches_exists():
    # Check that the Enumeration exists
    assert UPSISwitches is not None

def test_upsiswitches_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UPSISwitches]
    expected_literals = [
        "upsi0",
        "upsi7",
        "upsi1",
        "upsi5",
        "upsi3",
        "upsi4",
        "upsi6",
        "upsi2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UPSISwitches"

def test_occurrences_exists():
    # Check that the Enumeration exists
    assert Occurrences is not None

def test_occurrences_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Occurrences]
    expected_literals = [
        "leading",
        "all",
        "first",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Occurrences"

def test_sortphrasetokens_exists():
    # Check that the Enumeration exists
    assert SortPhraseTokens is not None

def test_sortphrasetokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortPhraseTokens]
    expected_literals = [
        "in_",
        "is_",
        "sequence",
        "order",
        "with_",
        "duplicates",
        "collating",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SortPhraseTokens"

def test_programdescriptioninfo_exists():
    # Check that the Enumeration exists
    assert ProgramDescriptionInfo is not None

def test_programdescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgramDescriptionInfo]
    expected_literals = [
        "installation",
        "author",
        "dateWritten",
        "security",
        "dateCompleted",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgramDescriptionInfo"

def test_acceptstatementtokens_exists():
    # Check that the Enumeration exists
    assert AcceptStatementTokens is not None

def test_acceptstatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AcceptStatementTokens]
    expected_literals = [
        "dateformat1",
        "day",
        "dow",
        "from_",
        "date",
        "dateformat2",
        "time",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AcceptStatementTokens"

def test_filedescriptors_exists():
    # Check that the Enumeration exists
    assert FileDescriptors is not None

def test_filedescriptors_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FileDescriptors]
    expected_literals = [
        "fd",
        "sd",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FileDescriptors"

def test_systeminputs_exists():
    # Check that the Enumeration exists
    assert SystemInputs is not None

def test_systeminputs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemInputs]
    expected_literals = [
        "sysipt",
        "sysin",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemInputs"

def test_cicsstatementtokens_exists():
    # Check that the Enumeration exists
    assert CICSStatementTokens is not None

def test_cicsstatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CICSStatementTokens]
    expected_literals = [
        "keylength",
        "next",
        "inputmsg",
        "closepar",
        "synconreturn",
        "rba",
        "write",
        "commarea",
        "from_",
        "tr",
        "token",
        "channel",
        "openpar",
        "transid",
        "gteq",
        "start",
        "qname",
        "xctl",
        "read",
        "update",
        "auxiliary",
        "uncommitted",
        "rewrite",
        "xrba",
        "file",
        "length",
        "datalength",
        "ts",
        "massinsert",
        "numitems",
        "inputmsglen",
        "consistent",
        "main",
        "program",
        "set",
        "repeatable",
        "sys",
        "queue",
        "nosuspend",
        "dataset",
        "deleteq",
        "load",
        "rrn",
        "sysid",
        "into",
        "writeq",
        "item",
        "equal",
        "td",
        "ridfld",
        "generic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CICSStatementTokens"

def test_iotypes_exists():
    # Check that the Enumeration exists
    assert IOTypes is not None

def test_iotypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IOTypes]
    expected_literals = [
        "extend",
        "output",
        "io",
        "input",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IOTypes"

def test_usestatementtokens_exists():
    # Check that the Enumeration exists
    assert UseStatementTokens is not None

def test_usestatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UseStatementTokens]
    expected_literals = [
        "exception",
        "procedures",
        "input",
        "all",
        "reel",
        "for_",
        "global_",
        "io",
        "on",
        "beginning",
        "ending",
        "procedure",
        "output",
        "debugging",
        "unit",
        "label",
        "standard",
        "error",
        "extend",
        "file",
        "after",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UseStatementTokens"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
strings_Occurrence_strategy = st.builds(
    strings_Occurrence,
)
strings_Tallying_strategy = st.builds(
    strings_Tallying,
)
cobol_strings_TallyingOccurrence_strategy = st.builds(
    cobol_strings_TallyingOccurrence,
)
cobol_strings_Occurrence_strategy = st.builds(
    cobol_strings_Occurrence,
    type=
        safe_text
)
cobol_strings_Location_strategy = st.builds(
    cobol_strings_Location,
    position=
        safe_text,
    initial=
        st.booleans()
)
ManipulatedStrings_strategy = st.builds(
    ManipulatedStrings,
)
cobol_strings_SplittedString_strategy = st.builds(
    cobol_strings_SplittedString,
)
cobol_strings_ConcatenatingStrings_strategy = st.builds(
    cobol_strings_ConcatenatingStrings,
)
cobol_strings_String_strategy = st.builds(
    cobol_strings_String,
)
Location_strategy = st.builds(
    Location,
)
String_strategy = st.builds(
    String,
)
cobol_strings_ManipulatedStrings_strategy = st.builds(
    cobol_strings_ManipulatedStrings,
)
cobol_strings_StringManipulation_strategy = st.builds(
    cobol_strings_StringManipulation,
)
StringManipulation_strategy = st.builds(
    StringManipulation,
)
cobol_strings_Replacement_strategy = st.builds(
    cobol_strings_Replacement,
)
cobol_strings_Tallying_strategy = st.builds(
    cobol_strings_Tallying,
)
strings_Replacement_strategy = st.builds(
    strings_Replacement,
)
cobol_strings_ReplacementOccurrence_strategy = st.builds(
    cobol_strings_ReplacementOccurrence,
)
NotErrorHandler_strategy = st.builds(
    NotErrorHandler,
)
cobol_handlers_NotOnOverflow_strategy = st.builds(
    cobol_handlers_NotOnOverflow,
)
cobol_handlers_NotAtEnd_strategy = st.builds(
    cobol_handlers_NotAtEnd,
)
cobol_handlers_NotInvalidKey_strategy = st.builds(
    cobol_handlers_NotInvalidKey,
)
cobol_handlers_NotOnException_strategy = st.builds(
    cobol_handlers_NotOnException,
)
cobol_handlers_NotOnSizeError_strategy = st.builds(
    cobol_handlers_NotOnSizeError,
)
cobol_functions_Argumentable_strategy = st.builds(
    cobol_functions_Argumentable,
)
Argument_strategy = st.builds(
    Argument,
)
cobol_functions_ByContentArgument_strategy = st.builds(
    cobol_functions_ByContentArgument,
)
cobol_functions_ByValueArgument_strategy = st.builds(
    cobol_functions_ByValueArgument,
)
cobol_functions_OmittedArgument_strategy = st.builds(
    cobol_functions_OmittedArgument,
)
cobol_functions_ByReferenceArgument_strategy = st.builds(
    cobol_functions_ByReferenceArgument,
)
cobol_functions_Argument_strategy = st.builds(
    cobol_functions_Argument,
)
cobol_labels_Label_strategy = st.builds(
    cobol_labels_Label,
)
cobol_labels_Procedure_strategy = st.builds(
    cobol_labels_Procedure,
)
Procedure_strategy = st.builds(
    Procedure,
)
cobol_handlers_NotAtEndOfPage_strategy = st.builds(
    cobol_handlers_NotAtEndOfPage,
)
ProcedureRangeChild_strategy = st.builds(
    ProcedureRangeChild,
)
cobol_verbs_Verb_strategy = st.builds(
    cobol_verbs_Verb,
)
Verb_strategy = st.builds(
    Verb,
)
cobol_verbs_Is_strategy = st.builds(
    cobol_verbs_Is,
)
DeclarativeSection_strategy = st.builds(
    DeclarativeSection,
)
cobol_declaratives_Declaratives_strategy = st.builds(
    cobol_declaratives_Declaratives,
)
cobol_labels_ProcedureLabel_strategy = st.builds(
    cobol_labels_ProcedureLabel,
)
cobol_files_FileStatus_strategy = st.builds(
    cobol_files_FileStatus,
)
FileStatus_strategy = st.builds(
    FileStatus,
)
cobol_tables_TableDimension_strategy = st.builds(
    cobol_tables_TableDimension,
    value=
        st.integers()
)
AdditionalIndexName_strategy = st.builds(
    AdditionalIndexName,
)
Parameter_strategy = st.builds(
    Parameter,
)
cobol_parameters_ByReferenceParameter_strategy = st.builds(
    cobol_parameters_ByReferenceParameter,
)
cobol_parameters_ByValueParameter_strategy = st.builds(
    cobol_parameters_ByValueParameter,
)
cobol_parameters_Parametrizable_strategy = st.builds(
    cobol_parameters_Parametrizable,
)
IndexName_strategy = st.builds(
    IndexName,
)
TableDimension_strategy = st.builds(
    TableDimension,
)
dataitems_DataItem_strategy = st.builds(
    dataitems_DataItem,
)
cobol_specialnames_SpecialNameStatement_strategy = st.builds(
    cobol_specialnames_SpecialNameStatement,
)
AlphabetNameReference_strategy = st.builds(
    AlphabetNameReference,
)
SymbolicCharacter_strategy = st.builds(
    SymbolicCharacter,
)
SpecialName_strategy = st.builds(
    SpecialName,
)
cobol_specialnames_SymbolicCharacter_strategy = st.builds(
    cobol_specialnames_SymbolicCharacter,
)
cobol_specialnames_MnemonicName_strategy = st.builds(
    cobol_specialnames_MnemonicName,
)
cobol_tables_KeyName_strategy = st.builds(
    cobol_tables_KeyName,
    keyOrder=
        safe_text
)
KeyName_strategy = st.builds(
    KeyName,
)
cobol_specialnames_AlphabetType_strategy = st.builds(
    cobol_specialnames_AlphabetType,
)
specialnames_MnemonicName_strategy = st.builds(
    specialnames_MnemonicName,
)
AlphabetType_strategy = st.builds(
    AlphabetType,
)
cobol_specialnames_PredefinedAlphabetType_strategy = st.builds(
    cobol_specialnames_PredefinedAlphabetType,
    value=
        safe_text
)
cobol_specialnames_CodeNameAlphabetType_strategy = st.builds(
    cobol_specialnames_CodeNameAlphabetType,
    value=
        safe_text
)
specialnames_SpecialNameStatement_strategy = st.builds(
    specialnames_SpecialNameStatement,
)
cobol_specialnames_SystemDeviceIs_strategy = st.builds(
    cobol_specialnames_SystemDeviceIs,
)
cobol_specialnames_UPSISwitchIs_strategy = st.builds(
    cobol_specialnames_UPSISwitchIs,
)
ConditionName_strategy = st.builds(
    ConditionName,
)
cobol_specialnames_OffStatus_strategy = st.builds(
    cobol_specialnames_OffStatus,
)
cobol_specialnames_OnStatus_strategy = st.builds(
    cobol_specialnames_OnStatus,
)
specialnames_SpecialName_strategy = st.builds(
    specialnames_SpecialName,
)
cobol_specialnames_CurrencySign_strategy = st.builds(
    cobol_specialnames_CurrencySign,
    pictureSymbol=
        safe_text
)
cobol_specialnames_AlphabetName_strategy = st.builds(
    cobol_specialnames_AlphabetName,
)
cobol_specialnames_ClassName_strategy = st.builds(
    cobol_specialnames_ClassName,
)
cobol_specialnames_ExplicitAlphabetType_strategy = st.builds(
    cobol_specialnames_ExplicitAlphabetType,
)
references_ReferenceableElement_strategy = st.builds(
    references_ReferenceableElement,
)
cobol_dataitems_DataItemAttribute_strategy = st.builds(
    cobol_dataitems_DataItemAttribute,
)
RangeExpression_strategy = st.builds(
    RangeExpression,
)
DataName_strategy = st.builds(
    DataName,
)
cobol_dataitems_RenamingDataName_strategy = st.builds(
    cobol_dataitems_RenamingDataName,
)
DataItemAttribute_strategy = st.builds(
    DataItemAttribute,
)
cobol_dataitems_GroupUsage_strategy = st.builds(
    cobol_dataitems_GroupUsage,
)
cobol_dataitems_Redefines_strategy = st.builds(
    cobol_dataitems_Redefines,
)
cobol_dataitems_Value_strategy = st.builds(
    cobol_dataitems_Value,
)
cobol_dataitems_Global_strategy = st.builds(
    cobol_dataitems_Global,
)
cobol_dataitems_External_strategy = st.builds(
    cobol_dataitems_External,
)
cobol_dataitems_Usage_strategy = st.builds(
    cobol_dataitems_Usage,
    usage=
        safe_text,
    isNative=
        st.booleans()
)
cobol_dataitems_PictureString_strategy = st.builds(
    cobol_dataitems_PictureString,
    picture=
        safe_text
)
SystemDevice_strategy = st.builds(
    SystemDevice,
)
cobol_environments_SystemPunchDevice_strategy = st.builds(
    cobol_environments_SystemPunchDevice,
    value=
        safe_text
)
cobol_environments_AdvancedFunctionPrinting_strategy = st.builds(
    cobol_environments_AdvancedFunctionPrinting,
)
cobol_environments_SuppressSpacing_strategy = st.builds(
    cobol_environments_SuppressSpacing,
)
cobol_environments_Console_strategy = st.builds(
    cobol_environments_Console,
)
cobol_environments_SystemLogicalOutput_strategy = st.builds(
    cobol_environments_SystemLogicalOutput,
    value=
        safe_text
)
cobol_environments_Pocket_strategy = st.builds(
    cobol_environments_Pocket,
    value=
        safe_text
)
cobol_environments_Channel_strategy = st.builds(
    cobol_environments_Channel,
    value=
        safe_text
)
cobol_environments_SystemLogicalInput_strategy = st.builds(
    cobol_environments_SystemLogicalInput,
    value=
        safe_text
)
Register_strategy = st.builds(
    Register,
)
cobol_registers_ShiftOut_strategy = st.builds(
    cobol_registers_ShiftOut,
)
cobol_registers_AddressOf_strategy = st.builds(
    cobol_registers_AddressOf,
)
cobol_registers_LengthOf_strategy = st.builds(
    cobol_registers_LengthOf,
)
cobol_registers_WhenCompiled_strategy = st.builds(
    cobol_registers_WhenCompiled,
)
cobol_registers_ReturnCode_strategy = st.builds(
    cobol_registers_ReturnCode,
)
cobol_registers_ShiftIn_strategy = st.builds(
    cobol_registers_ShiftIn,
)
SortPhraseWater_strategy = st.builds(
    SortPhraseWater,
)
cobol_water_SortPhraseToken_strategy = st.builds(
    cobol_water_SortPhraseToken,
    value=
        safe_text
)
OpenStatementWater_strategy = st.builds(
    OpenStatementWater,
)
cobol_water_OpenStatementToken_strategy = st.builds(
    cobol_water_OpenStatementToken,
    value=
        safe_text
)
InvokeStatementWater_strategy = st.builds(
    InvokeStatementWater,
)
cobol_water_InvokeStatementToken_strategy = st.builds(
    cobol_water_InvokeStatementToken,
    value=
        safe_text
)
CloseStatementWater_strategy = st.builds(
    CloseStatementWater,
)
cobol_water_CloseStatementToken_strategy = st.builds(
    cobol_water_CloseStatementToken,
    value=
        safe_text
)
UseStatementWater_strategy = st.builds(
    UseStatementWater,
)
cobol_water_UseStatementToken_strategy = st.builds(
    cobol_water_UseStatementToken,
    value=
        safe_text
)
AcceptStatementWater_strategy = st.builds(
    AcceptStatementWater,
)
cobol_environments_Environment_strategy = st.builds(
    cobol_environments_Environment,
)
cobol_water_AcceptStatementToken_strategy = st.builds(
    cobol_water_AcceptStatementToken,
    value=
        safe_text
)
CICSStatementWater_strategy = st.builds(
    CICSStatementWater,
)
cobol_water_CICSStatementToken_strategy = st.builds(
    cobol_water_CICSStatementToken,
    value=
        safe_text
)
SQLStatementWater_strategy = st.builds(
    SQLStatementWater,
)
cobol_water_SQLStatementToken_strategy = st.builds(
    cobol_water_SQLStatementToken,
    value=
        safe_text
)
RepositoryParagraphWater_strategy = st.builds(
    RepositoryParagraphWater,
)
cobol_water_RepositoryDescription_strategy = st.builds(
    cobol_water_RepositoryDescription,
    value=
        safe_text
)
IOControlParagraphWater_strategy = st.builds(
    IOControlParagraphWater,
)
cobol_water_IOControlDescription_strategy = st.builds(
    cobol_water_IOControlDescription,
    value=
        safe_text
)
DataDescriptorWater_strategy = st.builds(
    DataDescriptorWater,
)
cobol_water_DataDescription_strategy = st.builds(
    cobol_water_DataDescription,
    value=
        safe_text
)
FileDescriptorWater_strategy = st.builds(
    FileDescriptorWater,
)
cobol_water_FileDescription_strategy = st.builds(
    cobol_water_FileDescription,
    value=
        safe_text
)
SelectStatementWater_strategy = st.builds(
    SelectStatementWater,
)
cobol_water_SelectStatementClause_strategy = st.builds(
    cobol_water_SelectStatementClause,
    value=
        safe_text
)
ObjectComputerParagraphWater_strategy = st.builds(
    ObjectComputerParagraphWater,
)
cobol_water_PriorityNumber_strategy = st.builds(
    cobol_water_PriorityNumber,
    value=
        safe_text
)
cobol_water_ObjectComputerDescription_strategy = st.builds(
    cobol_water_ObjectComputerDescription,
    value=
        safe_text
)
cobol_water_Water_strategy = st.builds(
    cobol_water_Water,
)
Water_strategy = st.builds(
    Water,
)
cobol_water_CloseStatementWater_strategy = st.builds(
    cobol_water_CloseStatementWater,
)
cobol_water_FileDescriptorWater_strategy = st.builds(
    cobol_water_FileDescriptorWater,
)
cobol_water_InvokeStatementWater_strategy = st.builds(
    cobol_water_InvokeStatementWater,
)
cobol_water_DataDescriptorWater_strategy = st.builds(
    cobol_water_DataDescriptorWater,
)
cobol_water_SelectStatementWater_strategy = st.builds(
    cobol_water_SelectStatementWater,
)
cobol_water_SQLStatementWater_strategy = st.builds(
    cobol_water_SQLStatementWater,
)
cobol_water_AcceptStatementWater_strategy = st.builds(
    cobol_water_AcceptStatementWater,
)
cobol_water_IdentificationDivisionWater_strategy = st.builds(
    cobol_water_IdentificationDivisionWater,
)
cobol_water_UseStatementWater_strategy = st.builds(
    cobol_water_UseStatementWater,
)
cobol_water_IOControlParagraphWater_strategy = st.builds(
    cobol_water_IOControlParagraphWater,
)
cobol_water_SpecialNamesParagraphWater_strategy = st.builds(
    cobol_water_SpecialNamesParagraphWater,
)
cobol_water_ObjectComputerParagraphWater_strategy = st.builds(
    cobol_water_ObjectComputerParagraphWater,
)
cobol_water_OpenStatementWater_strategy = st.builds(
    cobol_water_OpenStatementWater,
)
cobol_water_CICSStatementWater_strategy = st.builds(
    cobol_water_CICSStatementWater,
)
cobol_water_SortPhraseWater_strategy = st.builds(
    cobol_water_SortPhraseWater,
)
cobol_water_RepositoryParagraphWater_strategy = st.builds(
    cobol_water_RepositoryParagraphWater,
)
cobol_water_IncompleteElement_strategy = st.builds(
    cobol_water_IncompleteElement,
)
Label_strategy = st.builds(
    Label,
)
cobol_labels_ProcedureRangeLabel_strategy = st.builds(
    cobol_labels_ProcedureRangeLabel,
)
cobol_labels_StopLabel_strategy = st.builds(
    cobol_labels_StopLabel,
)
cobol_ios_IODirectives_strategy = st.builds(
    cobol_ios_IODirectives,
)
ios_OutputDirective_strategy = st.builds(
    ios_OutputDirective,
)
ios_FileDirective_strategy = st.builds(
    ios_FileDirective,
)
cobol_ios_OutputFile_strategy = st.builds(
    cobol_ios_OutputFile,
)
IODirectives_strategy = st.builds(
    IODirectives,
)
cobol_ios_OutputDirective_strategy = st.builds(
    cobol_ios_OutputDirective,
)
cobol_ios_FileDirective_strategy = st.builds(
    cobol_ios_FileDirective,
)
cobol_ios_ProcedureDirective_strategy = st.builds(
    cobol_ios_ProcedureDirective,
)
cobol_ios_InputDirective_strategy = st.builds(
    cobol_ios_InputDirective,
)
ios_ProcedureDirective_strategy = st.builds(
    ios_ProcedureDirective,
)
cobol_ios_OutputProcedure_strategy = st.builds(
    cobol_ios_OutputProcedure,
)
ios_InputDirective_strategy = st.builds(
    ios_InputDirective,
)
cobol_ios_InputFile_strategy = st.builds(
    cobol_ios_InputFile,
)
cobol_ios_InputProcedure_strategy = st.builds(
    cobol_ios_InputProcedure,
)
cobol_identifiers_ReferenceModifier_strategy = st.builds(
    cobol_identifiers_ReferenceModifier,
)
DirectSubscript_strategy = st.builds(
    DirectSubscript,
)
cobol_identifiers_All_strategy = st.builds(
    cobol_identifiers_All,
)
IdentificationDivisionWater_strategy = st.builds(
    IdentificationDivisionWater,
)
cobol_water_ProgramDescription_strategy = st.builds(
    cobol_water_ProgramDescription,
    value=
        safe_text
)
Subscript_strategy = st.builds(
    Subscript,
)
cobol_identifiers_RelativeSubscript_strategy = st.builds(
    cobol_identifiers_RelativeSubscript,
)
cobol_identifiers_DirectSubscript_strategy = st.builds(
    cobol_identifiers_DirectSubscript,
)
identifiers_Identifier_strategy = st.builds(
    identifiers_Identifier,
)
ReferenceModifier_strategy = st.builds(
    ReferenceModifier,
)
water_SortPhraseWater_strategy = st.builds(
    water_SortPhraseWater,
)
water_DataDescriptorWater_strategy = st.builds(
    water_DataDescriptorWater,
)
statements_Statement_strategy = st.builds(
    statements_Statement,
)
water_UseStatementWater_strategy = st.builds(
    water_UseStatementWater,
)
DataItem_strategy = st.builds(
    DataItem,
)
cobol_dataitems_ConditionName_strategy = st.builds(
    cobol_dataitems_ConditionName,
)
cobol_dataitems_RecordName_strategy = st.builds(
    cobol_dataitems_RecordName,
)
cobol_dataitems_DataName_strategy = st.builds(
    cobol_dataitems_DataName,
)
Statement_strategy = st.builds(
    Statement,
)
EnvironmentDivisionSection_strategy = st.builds(
    EnvironmentDivisionSection,
)
cobol_sections_ConfigurationSection_strategy = st.builds(
    cobol_sections_ConfigurationSection,
)
cobol_sections_IOSection_strategy = st.builds(
    cobol_sections_IOSection,
)
ArithmeticOperand_strategy = st.builds(
    ArithmeticOperand,
)
cobol_operands_RoundedIdentifier_strategy = st.builds(
    cobol_operands_RoundedIdentifier,
)
water_SQLStatementWater_strategy = st.builds(
    water_SQLStatementWater,
)
water_IdentificationDivisionWater_strategy = st.builds(
    water_IdentificationDivisionWater,
)
cobol_water_Dot_strategy = st.builds(
    cobol_water_Dot,
)
water_RepositoryParagraphWater_strategy = st.builds(
    water_RepositoryParagraphWater,
)
water_AcceptStatementWater_strategy = st.builds(
    water_AcceptStatementWater,
)
cobol_identifiers_Subscript_strategy = st.builds(
    cobol_identifiers_Subscript,
)
VaryingUntilCondition_strategy = st.builds(
    VaryingUntilCondition,
)
cobol_statements_AfterUntilCondition_strategy = st.builds(
    cobol_statements_AfterUntilCondition,
)
Qualifier_strategy = st.builds(
    Qualifier,
)
Conditional_strategy = st.builds(
    Conditional,
)
cobol_statements_VaryingUntilCondition_strategy = st.builds(
    cobol_statements_VaryingUntilCondition,
)
Tallying_strategy = st.builds(
    Tallying,
)
cobol_strings_AnyCharacter_strategy = st.builds(
    cobol_strings_AnyCharacter,
)
cobol_strings_SpecificCharacter_strategy = st.builds(
    cobol_strings_SpecificCharacter,
)
cobol_statements_TallyingIn_strategy = st.builds(
    cobol_statements_TallyingIn,
)
IncompleteElement_strategy = st.builds(
    IncompleteElement,
)
cobol_files_SelectStatement_strategy = st.builds(
    cobol_files_SelectStatement,
    isOptional=
        st.booleans(),
    externalFileNames=
        safe_text
)
cobol_statements_IOFile_strategy = st.builds(
    cobol_statements_IOFile,
)
IOFile_strategy = st.builds(
    IOFile,
)
cobol_statements_IOFileDescriptor_strategy = st.builds(
    cobol_statements_IOFileDescriptor,
    type=
        safe_text
)
IOFileDescriptor_strategy = st.builds(
    IOFileDescriptor,
)
cobol_statements_IOStatement_strategy = st.builds(
    cobol_statements_IOStatement,
)
cobol_statements_KeyDescriptor_strategy = st.builds(
    cobol_statements_KeyDescriptor,
    order=
        safe_text
)
statements_VaryingUntilCondition_strategy = st.builds(
    statements_VaryingUntilCondition,
)
cobol_statements_Release_strategy = st.builds(
    cobol_statements_Release,
)
statements_PerformFixedTimes_strategy = st.builds(
    statements_PerformFixedTimes,
)
statements_FileIOStatement_strategy = st.builds(
    statements_FileIOStatement,
)
KeyDescriptor_strategy = st.builds(
    KeyDescriptor,
)
OutputDirective_strategy = st.builds(
    OutputDirective,
)
InputDirective_strategy = st.builds(
    InputDirective,
)
statements_PerformProcedure_strategy = st.builds(
    statements_PerformProcedure,
)
cobol_statements_PerformProcedureFixedTimes_strategy = st.builds(
    cobol_statements_PerformProcedureFixedTimes,
)
cobol_statements_FileIOStatement_strategy = st.builds(
    cobol_statements_FileIOStatement,
)
statements_PerformNestedStatement_strategy = st.builds(
    statements_PerformNestedStatement,
)
cobol_statements_PerformNestedStatementFixedTimes_strategy = st.builds(
    cobol_statements_PerformNestedStatementFixedTimes,
)
AfterUntilCondition_strategy = st.builds(
    AfterUntilCondition,
)
statements_PerformUntilCondition_strategy = st.builds(
    statements_PerformUntilCondition,
)
cobol_statements_PerformNestedStatementUntilCondition_strategy = st.builds(
    cobol_statements_PerformNestedStatementUntilCondition,
)
cobol_statements_PerformProcedureUntilCondition_strategy = st.builds(
    cobol_statements_PerformProcedureUntilCondition,
)
TallyingIn_strategy = st.builds(
    TallyingIn,
)
cobol_statements_SwitchStatus_strategy = st.builds(
    cobol_statements_SwitchStatus,
    status=
        safe_text
)
Write_strategy = st.builds(
    Write,
)
cobol_statements_Rewrite_strategy = st.builds(
    cobol_statements_Rewrite,
)
MnemonicNameReference_strategy = st.builds(
    MnemonicNameReference,
)
IntegerLiteral_strategy = st.builds(
    IntegerLiteral,
)
SearchStatement_strategy = st.builds(
    SearchStatement,
)
cobol_statements_BinarySearch_strategy = st.builds(
    cobol_statements_BinarySearch,
)
cobol_statements_SerialSearch_strategy = st.builds(
    cobol_statements_SerialSearch,
)
NormalEvaluateCase_strategy = st.builds(
    NormalEvaluateCase,
)
Replacement_strategy = st.builds(
    Replacement,
)
cobol_strings_AnyCharacterBySpecificCharacter_strategy = st.builds(
    cobol_strings_AnyCharacterBySpecificCharacter,
)
cobol_strings_SpecificCharacterBySpecificCharacter_strategy = st.builds(
    cobol_strings_SpecificCharacterBySpecificCharacter,
)
cobol_statements_Initialize_strategy = st.builds(
    cobol_statements_Initialize,
)
cobol_statements_Inspect_strategy = st.builds(
    cobol_statements_Inspect,
)
cobol_statements_Replace_strategy = st.builds(
    cobol_statements_Replace,
    replaceSwitch=
        st.booleans()
)
NestedStatement_strategy = st.builds(
    NestedStatement,
)
cobol_handlers_Handler_strategy = st.builds(
    cobol_handlers_Handler,
)
cobol_statements_EvaluateCase_strategy = st.builds(
    cobol_statements_EvaluateCase,
)
ExpressionList_strategy = st.builds(
    ExpressionList,
)
EvaluateCase_strategy = st.builds(
    EvaluateCase,
)
cobol_statements_OtherEvaluateCase_strategy = st.builds(
    cobol_statements_OtherEvaluateCase,
)
cobol_statements_NormalEvaluateCase_strategy = st.builds(
    cobol_statements_NormalEvaluateCase,
)
cobol_statements_Evaluate_strategy = st.builds(
    cobol_statements_Evaluate,
)
SplittedString_strategy = st.builds(
    SplittedString,
)
SetStatement_strategy = st.builds(
    SetStatement,
)
cobol_statements_Set_strategy = st.builds(
    cobol_statements_Set,
)
cobol_statements_SetSwitches_strategy = st.builds(
    cobol_statements_SetSwitches,
)
cobol_statements_SetStatement_strategy = st.builds(
    cobol_statements_SetStatement,
)
FileNameReference_strategy = st.builds(
    FileNameReference,
)
Handler_strategy = st.builds(
    Handler,
)
cobol_handlers_OnException_strategy = st.builds(
    cobol_handlers_OnException,
)
cobol_handlers_AtEndOfPage_strategy = st.builds(
    cobol_handlers_AtEndOfPage,
    eop=
        safe_text
)
cobol_handlers_OnSizeError_strategy = st.builds(
    cobol_handlers_OnSizeError,
)
cobol_handlers_AtEnd_strategy = st.builds(
    cobol_handlers_AtEnd,
)
cobol_handlers_NotErrorHandler_strategy = st.builds(
    cobol_handlers_NotErrorHandler,
)
cobol_handlers_InvalidKey_strategy = st.builds(
    cobol_handlers_InvalidKey,
)
cobol_handlers_OnOverflow_strategy = st.builds(
    cobol_handlers_OnOverflow,
)
cobol_statements_ErrorHandled_strategy = st.builds(
    cobol_statements_ErrorHandled,
)
cobol_statements_Execute_strategy = st.builds(
    cobol_statements_Execute,
    water=
        safe_text
)
functions_Argumentable_strategy = st.builds(
    functions_Argumentable,
)
cobol_statements_Cancel_strategy = st.builds(
    cobol_statements_Cancel,
)
statements_IOStatement_strategy = st.builds(
    statements_IOStatement,
)
ConcatenatingStrings_strategy = st.builds(
    ConcatenatingStrings,
)
IndexNameReference_strategy = st.builds(
    IndexNameReference,
)
cobol_statements_SetIndexName_strategy = st.builds(
    cobol_statements_SetIndexName,
    adjust=
        safe_text
)
SwitchStatus_strategy = st.builds(
    SwitchStatus,
)
PrimaryOperand_strategy = st.builds(
    PrimaryOperand,
)
cobol_registers_Register_strategy = st.builds(
    cobol_registers_Register,
)
cobol_statements_Move_strategy = st.builds(
    cobol_statements_Move,
    corresponding=
        safe_text
)
cobol_statements_NestedStatement_strategy = st.builds(
    cobol_statements_NestedStatement,
)
Jump_strategy = st.builds(
    Jump,
)
cobol_statements_GoTo_strategy = st.builds(
    cobol_statements_GoTo,
)
cobol_statements_GoBack_strategy = st.builds(
    cobol_statements_GoBack,
)
cobol_statements_Continue_strategy = st.builds(
    cobol_statements_Continue,
)
cobol_statements_NextSentence_strategy = st.builds(
    cobol_statements_NextSentence,
)
cobol_statements_Jump_strategy = st.builds(
    cobol_statements_Jump,
)
ProcedureRangeLabel_strategy = st.builds(
    ProcedureRangeLabel,
)
cobol_labels_ProcedureRange_strategy = st.builds(
    cobol_labels_ProcedureRange,
)
cobol_labels_ProcedureRangeChild_strategy = st.builds(
    cobol_labels_ProcedureRangeChild,
)
Perform_strategy = st.builds(
    Perform,
)
cobol_statements_PerformFixedTimes_strategy = st.builds(
    cobol_statements_PerformFixedTimes,
)
cobol_statements_PerformProcedure_strategy = st.builds(
    cobol_statements_PerformProcedure,
)
AssignmentExpression_strategy = st.builds(
    AssignmentExpression,
)
Environment_strategy = st.builds(
    Environment,
)
cobol_environments_UPSI_strategy = st.builds(
    cobol_environments_UPSI,
    value=
        safe_text
)
cobol_environments_SystemDevice_strategy = st.builds(
    cobol_environments_SystemDevice,
)
cobol_statements_Display_strategy = st.builds(
    cobol_statements_Display,
)
StopLabel_strategy = st.builds(
    StopLabel,
)
cobol_labels_Run_strategy = st.builds(
    cobol_labels_Run,
)
cobol_statements_Stop_strategy = st.builds(
    cobol_statements_Stop,
)
cobol_statements_Conditional_strategy = st.builds(
    cobol_statements_Conditional,
)
statements_Conditional_strategy = st.builds(
    statements_Conditional,
)
cobol_statements_Exit_strategy = st.builds(
    cobol_statements_Exit,
    exitLabel=
        safe_text
)
cobol_statements_Statement_strategy = st.builds(
    cobol_statements_Statement,
    endVerb=
        st.booleans()
)
cobol_operands_Operand_strategy = st.builds(
    cobol_operands_Operand,
)
ReplacementOperand_strategy = st.builds(
    ReplacementOperand,
)
cobol_operands_Encoding_strategy = st.builds(
    cobol_operands_Encoding,
    type=
        safe_text
)
Operand_strategy = st.builds(
    Operand,
)
cobol_operands_ArithmeticOperand_strategy = st.builds(
    cobol_operands_ArithmeticOperand,
)
cobol_operands_ReplacementOperand_strategy = st.builds(
    cobol_operands_ReplacementOperand,
)
Identifier_strategy = st.builds(
    Identifier,
)
statements_NestedStatement_strategy = st.builds(
    statements_NestedStatement,
)
cobol_statements_Condition_strategy = st.builds(
    cobol_statements_Condition,
)
statements_Perform_strategy = st.builds(
    statements_Perform,
)
cobol_statements_PerformUntilCondition_strategy = st.builds(
    cobol_statements_PerformUntilCondition,
    position=
        safe_text
)
cobol_statements_PerformNestedStatement_strategy = st.builds(
    cobol_statements_PerformNestedStatement,
)
cobol_statements_Perform_strategy = st.builds(
    cobol_statements_Perform,
)
ArithmeticStatement_strategy = st.builds(
    ArithmeticStatement,
)
cobol_statements_Divide_strategy = st.builds(
    cobol_statements_Divide,
)
cobol_statements_Multiply_strategy = st.builds(
    cobol_statements_Multiply,
)
cobol_statements_Subtract_strategy = st.builds(
    cobol_statements_Subtract,
)
cobol_statements_Add_strategy = st.builds(
    cobol_statements_Add,
)
statements_ErrorHandled_strategy = st.builds(
    statements_ErrorHandled,
)
cobol_statements_Return_strategy = st.builds(
    cobol_statements_Return,
)
cobol_statements_ArithmeticStatement_strategy = st.builds(
    cobol_statements_ArithmeticStatement,
    corresponding=
        safe_text
)
cobol_statements_Start_strategy = st.builds(
    cobol_statements_Start,
)
cobol_statements_SearchStatement_strategy = st.builds(
    cobol_statements_SearchStatement,
)
cobol_statements_Delete_strategy = st.builds(
    cobol_statements_Delete,
)
cobol_statements_Read_strategy = st.builds(
    cobol_statements_Read,
)
cobol_statements_Unstring_strategy = st.builds(
    cobol_statements_Unstring,
)
cobol_statements_Write_strategy = st.builds(
    cobol_statements_Write,
)
cobol_statements_Call_strategy = st.builds(
    cobol_statements_Call,
)
cobol_statements_String_strategy = st.builds(
    cobol_statements_String,
)
cobol_statements_Compute_strategy = st.builds(
    cobol_statements_Compute,
)
ConstantLiteral_strategy = st.builds(
    ConstantLiteral,
)
FigurativeConstantLiteral_strategy = st.builds(
    FigurativeConstantLiteral,
)
cobol_literals_AllLiteral_strategy = st.builds(
    cobol_literals_AllLiteral,
)
DecimalLiteral_strategy = st.builds(
    DecimalLiteral,
)
cobol_literals_FloatingDecimalLiteral_strategy = st.builds(
    cobol_literals_FloatingDecimalLiteral,
)
NumericLiteral_strategy = st.builds(
    NumericLiteral,
)
cobol_literals_DecimalLiteral_strategy = st.builds(
    cobol_literals_DecimalLiteral,
    value=
        safe_text
)
water_IOControlParagraphWater_strategy = st.builds(
    water_IOControlParagraphWater,
)
water_FileDescriptorWater_strategy = st.builds(
    water_FileDescriptorWater,
)
water_ObjectComputerParagraphWater_strategy = st.builds(
    water_ObjectComputerParagraphWater,
)
literals_NumericLiteral_strategy = st.builds(
    literals_NumericLiteral,
)
cobol_literals_IntegerLiteral_strategy = st.builds(
    cobol_literals_IntegerLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Literal_strategy = st.builds(
    Literal,
)
cobol_literals_FigurativeConstantLiteral_strategy = st.builds(
    cobol_literals_FigurativeConstantLiteral,
)
cobol_literals_BooleanLiteral_strategy = st.builds(
    cobol_literals_BooleanLiteral,
    value=
        st.booleans()
)
cobol_literals_AlphanumericLiteral_strategy = st.builds(
    cobol_literals_AlphanumericLiteral,
    value=
        safe_text
)
Division_strategy = st.builds(
    Division,
)
cobol_divisions_EnvironmentDivision_strategy = st.builds(
    cobol_divisions_EnvironmentDivision,
)
cobol_divisions_DataDivision_strategy = st.builds(
    cobol_divisions_DataDivision,
)
StatementContainer_strategy = st.builds(
    StatementContainer,
)
Paragraph_strategy = st.builds(
    Paragraph,
)
Section_strategy = st.builds(
    Section,
)
cobol_sections_DataDivisionSection_strategy = st.builds(
    cobol_sections_DataDivisionSection,
)
cobol_sections_EnvironmentDivisionSection_strategy = st.builds(
    cobol_sections_EnvironmentDivisionSection,
)
CobolRoot_strategy = st.builds(
    CobolRoot,
)
cobol_containers_EmptyModel_strategy = st.builds(
    cobol_containers_EmptyModel,
)
cobol_containers_CobolRoot_strategy = st.builds(
    cobol_containers_CobolRoot,
)
ProcedureDivision_strategy = st.builds(
    ProcedureDivision,
)
DataDivision_strategy = st.builds(
    DataDivision,
)
EnvironmentDivision_strategy = st.builds(
    EnvironmentDivision,
)
water_InvokeStatementWater_strategy = st.builds(
    water_InvokeStatementWater,
)
operands_PrimaryOperand_strategy = st.builds(
    operands_PrimaryOperand,
)
water_CICSStatementWater_strategy = st.builds(
    water_CICSStatementWater,
)
water_SpecialNamesParagraphWater_strategy = st.builds(
    water_SpecialNamesParagraphWater,
)
water_SelectStatementWater_strategy = st.builds(
    water_SelectStatementWater,
)
cobol_identifiers_Identifier_strategy = st.builds(
    cobol_identifiers_Identifier,
)
Declaratives_strategy = st.builds(
    Declaratives,
)
parameters_Parametrizable_strategy = st.builds(
    parameters_Parametrizable,
)
cobol_statements_Entry_strategy = st.builds(
    cobol_statements_Entry,
)
water_IncompleteElement_strategy = st.builds(
    water_IncompleteElement,
)
cobol_files_FileName_strategy = st.builds(
    cobol_files_FileName,
    fileDescriptor=
        safe_text
)
cobol_statements_Merge_strategy = st.builds(
    cobol_statements_Merge,
)
cobol_statements_Accept_strategy = st.builds(
    cobol_statements_Accept,
)
cobol_tables_Table_strategy = st.builds(
    cobol_tables_Table,
)
cobol_statements_Sort_strategy = st.builds(
    cobol_statements_Sort,
)
cobol_statements_Close_strategy = st.builds(
    cobol_statements_Close,
)
cobol_statements_Open_strategy = st.builds(
    cobol_statements_Open,
)
cobol_dataitems_DataItem_strategy = st.builds(
    cobol_dataitems_DataItem,
    levelNumber=
        safe_text
)
divisions_Division_strategy = st.builds(
    divisions_Division,
)
cobol_divisions_ProcedureDivision_strategy = st.builds(
    cobol_divisions_ProcedureDivision,
)
cobol_divisions_IdentificationDivision_strategy = st.builds(
    cobol_divisions_IdentificationDivision,
    properties=
        safe_text
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
cobol_arithmetics_RangeExpression_strategy = st.builds(
    cobol_arithmetics_RangeExpression,
)
Equal_strategy = st.builds(
    Equal,
)
cobol_arithmetics_AssignmentExpression_strategy = st.builds(
    cobol_arithmetics_AssignmentExpression,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
UnaryArithmeticExpressionChild_strategy = st.builds(
    UnaryArithmeticExpressionChild,
)
cobol_arithmetics_PrimaryExpression_strategy = st.builds(
    cobol_arithmetics_PrimaryExpression,
)
PowerArithmeticExpressionChild_strategy = st.builds(
    PowerArithmeticExpressionChild,
)
cobol_arithmetics_UnaryArithmeticExpression_strategy = st.builds(
    cobol_arithmetics_UnaryArithmeticExpression,
)
cobol_arithmetics_UnaryArithmeticExpressionChild_strategy = st.builds(
    cobol_arithmetics_UnaryArithmeticExpressionChild,
)
IdentificationDivision_strategy = st.builds(
    IdentificationDivision,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
cobol_divisions_Division_strategy = st.builds(
    cobol_divisions_Division,
)
cobol_containers_CompilationUnit_strategy = st.builds(
    cobol_containers_CompilationUnit,
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
commons_NamedElement_strategy = st.builds(
    commons_NamedElement,
)
cobol_specialnames_ConditionName_strategy = st.builds(
    cobol_specialnames_ConditionName,
)
cobol_functions_FunctionCall_strategy = st.builds(
    cobol_functions_FunctionCall,
)
cobol_tables_IndexName_strategy = st.builds(
    cobol_tables_IndexName,
)
containers_CobolRoot_strategy = st.builds(
    containers_CobolRoot,
)
cobol_containers_CompilationGroup_strategy = st.builds(
    cobol_containers_CompilationGroup,
)
conditions_SimpleConditionChild_strategy = st.builds(
    conditions_SimpleConditionChild,
)
conditions_AbbreviatedRelationalExpressionChild_strategy = st.builds(
    conditions_AbbreviatedRelationalExpressionChild,
)
cobol_arithmetics_ArithmeticExpression_strategy = st.builds(
    cobol_arithmetics_ArithmeticExpression,
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
cobol_arithmetics_NestedArithmeticExpression_strategy = st.builds(
    cobol_arithmetics_NestedArithmeticExpression,
)
cobol_arithmetics_RangeExpressionChild_strategy = st.builds(
    cobol_arithmetics_RangeExpressionChild,
)
Through_strategy = st.builds(
    Through,
)
ClassOperator_strategy = st.builds(
    ClassOperator,
)
SignOperator_strategy = st.builds(
    SignOperator,
)
MultiplicativeOperator_strategy = st.builds(
    MultiplicativeOperator,
)
MultiplicativeArithmeticExpressionChild_strategy = st.builds(
    MultiplicativeArithmeticExpressionChild,
)
cobol_arithmetics_PowerArithmeticExpression_strategy = st.builds(
    cobol_arithmetics_PowerArithmeticExpression,
)
cobol_arithmetics_PowerArithmeticExpressionChild_strategy = st.builds(
    cobol_arithmetics_PowerArithmeticExpressionChild,
)
AdditiveOperator_strategy = st.builds(
    AdditiveOperator,
)
AdditiveArithmeticExpressionChild_strategy = st.builds(
    AdditiveArithmeticExpressionChild,
)
cobol_arithmetics_MultiplicativeArithmeticExpression_strategy = st.builds(
    cobol_arithmetics_MultiplicativeArithmeticExpression,
)
cobol_arithmetics_MultiplicativeArithmeticExpressionChild_strategy = st.builds(
    cobol_arithmetics_MultiplicativeArithmeticExpressionChild,
)
RangeExpressionChild_strategy = st.builds(
    RangeExpressionChild,
)
cobol_arithmetics_AdditiveArithmeticExpressionChild_strategy = st.builds(
    cobol_arithmetics_AdditiveArithmeticExpressionChild,
)
cobol_arithmetics_AdditiveArithmeticExpression_strategy = st.builds(
    cobol_arithmetics_AdditiveArithmeticExpression,
)
NegatedAbbreviatedConditionalExpressionChild_strategy = st.builds(
    NegatedAbbreviatedConditionalExpressionChild,
)
cobol_conditions_AbbreviatedRelationalExpressionChild_strategy = st.builds(
    cobol_conditions_AbbreviatedRelationalExpressionChild,
)
AbbreviatedConditionalExpressionChild_strategy = st.builds(
    AbbreviatedConditionalExpressionChild,
)
cobol_conditions_NegatedAbbreviatedConditionalExpression_strategy = st.builds(
    cobol_conditions_NegatedAbbreviatedConditionalExpression,
)
cobol_conditions_ExpressionList_strategy = st.builds(
    cobol_conditions_ExpressionList,
)
AbbreviatedRelationalExpressionChild_strategy = st.builds(
    AbbreviatedRelationalExpressionChild,
)
cobol_conditions_NestedAbbreviatedConditionalExpression_strategy = st.builds(
    cobol_conditions_NestedAbbreviatedConditionalExpression,
)
cobol_conditions_AbbreviatedRelationalExpression_strategy = st.builds(
    cobol_conditions_AbbreviatedRelationalExpression,
)
cobol_conditions_NegatedAbbreviatedConditionalExpressionChild_strategy = st.builds(
    cobol_conditions_NegatedAbbreviatedConditionalExpressionChild,
)
NegatedConditionalExpressionChild_strategy = st.builds(
    NegatedConditionalExpressionChild,
)
cobol_conditions_ClassCondition_strategy = st.builds(
    cobol_conditions_ClassCondition,
)
cobol_conditions_SignCondition_strategy = st.builds(
    cobol_conditions_SignCondition,
)
ConditionalAndExpressionChild_strategy = st.builds(
    ConditionalAndExpressionChild,
)
cobol_conditions_AbbreviatedConditionalExpressionChild_strategy = st.builds(
    cobol_conditions_AbbreviatedConditionalExpressionChild,
)
cobol_conditions_AbbreviatedConditionalExpression_strategy = st.builds(
    cobol_conditions_AbbreviatedConditionalExpression,
)
cobol_conditions_NegatedConditionalExpression_strategy = st.builds(
    cobol_conditions_NegatedConditionalExpression,
)
LogicalOperator_strategy = st.builds(
    LogicalOperator,
)
ConditionalOrExpressionChild_strategy = st.builds(
    ConditionalOrExpressionChild,
)
cobol_conditions_ConditionalAndExpression_strategy = st.builds(
    cobol_conditions_ConditionalAndExpression,
)
cobol_conditions_ConditionalAndExpressionChild_strategy = st.builds(
    cobol_conditions_ConditionalAndExpressionChild,
)
Condition_strategy = st.builds(
    Condition,
)
cobol_conditions_ConditionalOrExpressionChild_strategy = st.builds(
    cobol_conditions_ConditionalOrExpressionChild,
)
cobol_conditions_ConditionalOrExpression_strategy = st.builds(
    cobol_conditions_ConditionalOrExpression,
)
cobol_conditions_Condition_strategy = st.builds(
    cobol_conditions_Condition,
)
Is_strategy = st.builds(
    Is,
)
RelationalOperator_strategy = st.builds(
    RelationalOperator,
)
SimpleConditionChild_strategy = st.builds(
    SimpleConditionChild,
)
cobol_conditions_NestedCondition_strategy = st.builds(
    cobol_conditions_NestedCondition,
)
cobol_conditions_RelationalExpression_strategy = st.builds(
    cobol_conditions_RelationalExpression,
)
cobol_conditions_SimpleConditionChild_strategy = st.builds(
    cobol_conditions_SimpleConditionChild,
)
cobol_conditions_NegatedConditionalExpressionChild_strategy = st.builds(
    cobol_conditions_NegatedConditionalExpressionChild,
)
Negate_strategy = st.builds(
    Negate,
)
cobol_commons_Commentable_strategy = st.builds(
    cobol_commons_Commentable,
)
Commentable_strategy = st.builds(
    Commentable,
)
cobol_commons_URIableElement_strategy = st.builds(
    cobol_commons_URIableElement,
    uri=
        safe_text
)
cobol_commons_LabellableElement_strategy = st.builds(
    cobol_commons_LabellableElement,
    label=
        safe_text
)
cobol_commons_NamedElement_strategy = st.builds(
    cobol_commons_NamedElement,
    name=
        safe_text
)
DataDivisionSection_strategy = st.builds(
    DataDivisionSection,
)
cobol_sections_LinkageStorageSection_strategy = st.builds(
    cobol_sections_LinkageStorageSection,
)
cobol_sections_LocalStorageSection_strategy = st.builds(
    cobol_sections_LocalStorageSection,
)
cobol_sections_FileSection_strategy = st.builds(
    cobol_sections_FileSection,
)
cobol_sections_WorkingStorageSection_strategy = st.builds(
    cobol_sections_WorkingStorageSection,
)
operands_ArithmeticOperand_strategy = st.builds(
    operands_ArithmeticOperand,
)
arithmetics_PrimaryExpression_strategy = st.builds(
    arithmetics_PrimaryExpression,
)
operands_Operand_strategy = st.builds(
    operands_Operand,
)
operands_ReplacementOperand_strategy = st.builds(
    operands_ReplacementOperand,
)
cobol_operands_PrimaryOperand_strategy = st.builds(
    cobol_operands_PrimaryOperand,
)
cobol_sentences_Sentence_strategy = st.builds(
    cobol_sentences_Sentence,
)
cobol_sentences_ExecuteSentence_strategy = st.builds(
    cobol_sentences_ExecuteSentence,
)
sentences_StatementContainer_strategy = st.builds(
    sentences_StatementContainer,
)
cobol_sentences_UseSentence_strategy = st.builds(
    cobol_sentences_UseSentence,
)
Sentence_strategy = st.builds(
    Sentence,
)
cobol_sentences_ExitProcedure_strategy = st.builds(
    cobol_sentences_ExitProcedure,
)
cobol_sentences_EntrySentence_strategy = st.builds(
    cobol_sentences_EntrySentence,
)
cobol_sentences_AlteredGoTo_strategy = st.builds(
    cobol_sentences_AlteredGoTo,
)
cobol_sentences_EmptySentence_strategy = st.builds(
    cobol_sentences_EmptySentence,
)
cobol_sentences_StatementContainer_strategy = st.builds(
    cobol_sentences_StatementContainer,
)
cobol_sections_DeclarativeSection_strategy = st.builds(
    cobol_sections_DeclarativeSection,
)
FileName_strategy = st.builds(
    FileName,
)
Reference_strategy = st.builds(
    Reference,
)
cobol_references_ElementReference_strategy = st.builds(
    cobol_references_ElementReference,
)
ReferenceableElement_strategy = st.builds(
    ReferenceableElement,
)
cobol_specialnames_SpecialName_strategy = st.builds(
    cobol_specialnames_SpecialName,
)
cobol_parameters_Parameter_strategy = st.builds(
    cobol_parameters_Parameter,
)
cobol_tables_AdditionalIndexName_strategy = st.builds(
    cobol_tables_AdditionalIndexName,
)
cobol_references_ReferenceableElement_strategy = st.builds(
    cobol_references_ReferenceableElement,
)
cobol_references_Reference_strategy = st.builds(
    cobol_references_Reference,
)
cobol_paragraphs_DebuggingMode_strategy = st.builds(
    cobol_paragraphs_DebuggingMode,
)
SpecialNamesParagraphWater_strategy = st.builds(
    SpecialNamesParagraphWater,
)
cobol_water_SpecialNamesClause_strategy = st.builds(
    cobol_water_SpecialNamesClause,
    value=
        safe_text
)
SpecialNameStatement_strategy = st.builds(
    SpecialNameStatement,
)
cobol_paragraphs_IOSectionParagraph_strategy = st.builds(
    cobol_paragraphs_IOSectionParagraph,
)
cobol_paragraphs_ConfigurationSectionParagraph_strategy = st.builds(
    cobol_paragraphs_ConfigurationSectionParagraph,
)
identifiers_IdentifierReference_strategy = st.builds(
    identifiers_IdentifierReference,
)
cobol_references_Qualifiable_strategy = st.builds(
    cobol_references_Qualifiable,
)
cobol_references_ConditionName_strategy = st.builds(
    cobol_references_ConditionName,
)
ElementReference_strategy = st.builds(
    ElementReference,
)
cobol_identifiers_Qualifier_strategy = st.builds(
    cobol_identifiers_Qualifier,
)
cobol_references_AlphabetNameReference_strategy = st.builds(
    cobol_references_AlphabetNameReference,
)
IdentifierReference_strategy = st.builds(
    IdentifierReference,
)
cobol_references_IndexNameReference_strategy = st.builds(
    cobol_references_IndexNameReference,
)
references_IdentifierReferenceQualifier_strategy = st.builds(
    references_IdentifierReferenceQualifier,
)
cobol_references_DataNameReference_strategy = st.builds(
    cobol_references_DataNameReference,
)
references_ConditionName_strategy = st.builds(
    references_ConditionName,
)
cobol_references_ConditionNameReference_strategy = st.builds(
    cobol_references_ConditionNameReference,
)
references_Qualifiable_strategy = st.builds(
    references_Qualifiable,
)
cobol_identifiers_LinageCounter_strategy = st.builds(
    cobol_identifiers_LinageCounter,
)
references_ElementReference_strategy = st.builds(
    references_ElementReference,
)
cobol_references_FileNameReference_strategy = st.builds(
    cobol_references_FileNameReference,
)
cobol_specialnames_SymbolicCharacterStatement_strategy = st.builds(
    cobol_specialnames_SymbolicCharacterStatement,
)
cobol_identifiers_IdentifierReference_strategy = st.builds(
    cobol_identifiers_IdentifierReference,
)
cobol_references_IdentifierReferenceQualifier_strategy = st.builds(
    cobol_references_IdentifierReferenceQualifier,
)
cobol_references_MnemonicNameReference_strategy = st.builds(
    cobol_references_MnemonicNameReference,
)
cobol_references_SpecialNamesConditionNameReference_strategy = st.builds(
    cobol_references_SpecialNamesConditionNameReference,
)
GreaterThan_strategy = st.builds(
    GreaterThan,
)
cobol_operators_GTPhrase_strategy = st.builds(
    cobol_operators_GTPhrase,
)
LessThanOrEqual_strategy = st.builds(
    LessThanOrEqual,
)
cobol_operators_LTEQSign_strategy = st.builds(
    cobol_operators_LTEQSign,
)
cobol_operators_LTEQPhrase_strategy = st.builds(
    cobol_operators_LTEQPhrase,
)
LessThan_strategy = st.builds(
    LessThan,
)
cobol_operators_LTSign_strategy = st.builds(
    cobol_operators_LTSign,
)
cobol_operators_LTPhrase_strategy = st.builds(
    cobol_operators_LTPhrase,
)
cobol_operators_EqualSign_strategy = st.builds(
    cobol_operators_EqualSign,
)
cobol_operators_EqualPhrase_strategy = st.builds(
    cobol_operators_EqualPhrase,
)
cobol_operators_Kanji_strategy = st.builds(
    cobol_operators_Kanji,
)
cobol_operators_AlphabeticLower_strategy = st.builds(
    cobol_operators_AlphabeticLower,
)
cobol_operators_AlphabeticUpper_strategy = st.builds(
    cobol_operators_AlphabeticUpper,
)
cobol_operators_Numeric_strategy = st.builds(
    cobol_operators_Numeric,
)
cobol_operators_DBCS_strategy = st.builds(
    cobol_operators_DBCS,
)
cobol_operators_Alphabetic_strategy = st.builds(
    cobol_operators_Alphabetic,
)
cobol_operators_ClassName_strategy = st.builds(
    cobol_operators_ClassName,
)
cobol_operators_Zero_strategy = st.builds(
    cobol_operators_Zero,
)
paragraphs_IOSectionParagraph_strategy = st.builds(
    paragraphs_IOSectionParagraph,
)
cobol_paragraphs_IOControlParagraph_strategy = st.builds(
    cobol_paragraphs_IOControlParagraph,
)
SelectStatement_strategy = st.builds(
    SelectStatement,
)
IOSectionParagraph_strategy = st.builds(
    IOSectionParagraph,
)
cobol_paragraphs_FileControlParagraph_strategy = st.builds(
    cobol_paragraphs_FileControlParagraph,
)
paragraphs_ConfigurationSectionParagraph_strategy = st.builds(
    paragraphs_ConfigurationSectionParagraph,
)
cobol_paragraphs_RepositoryParagraph_strategy = st.builds(
    cobol_paragraphs_RepositoryParagraph,
)
cobol_paragraphs_ObjectComputerParagraph_strategy = st.builds(
    cobol_paragraphs_ObjectComputerParagraph,
)
DebuggingMode_strategy = st.builds(
    DebuggingMode,
)
ConfigurationSectionParagraph_strategy = st.builds(
    ConfigurationSectionParagraph,
)
cobol_paragraphs_SpecialNamesParagraph_strategy = st.builds(
    cobol_paragraphs_SpecialNamesParagraph,
)
cobol_paragraphs_SourceComputerParagraph_strategy = st.builds(
    cobol_paragraphs_SourceComputerParagraph,
)
labels_Procedure_strategy = st.builds(
    labels_Procedure,
)
cobol_sections_Section_strategy = st.builds(
    cobol_sections_Section,
    segmentNumber=
        safe_text
)
cobol_paragraphs_Paragraph_strategy = st.builds(
    cobol_paragraphs_Paragraph,
)
GreaterThanOrEqual_strategy = st.builds(
    GreaterThanOrEqual,
)
cobol_operators_GTEQSign_strategy = st.builds(
    cobol_operators_GTEQSign,
)
cobol_operators_GTEQPhrase_strategy = st.builds(
    cobol_operators_GTEQPhrase,
)
cobol_operators_GTSign_strategy = st.builds(
    cobol_operators_GTSign,
)
operators_UnaryOperator_strategy = st.builds(
    operators_UnaryOperator,
)
operators_AdditiveOperator_strategy = st.builds(
    operators_AdditiveOperator,
)
cobol_operators_Subtraction_strategy = st.builds(
    cobol_operators_Subtraction,
)
cobol_operators_Addition_strategy = st.builds(
    cobol_operators_Addition,
)
cobol_operators_Division_strategy = st.builds(
    cobol_operators_Division,
)
cobol_operators_Negative_strategy = st.builds(
    cobol_operators_Negative,
)
cobol_operators_Positive_strategy = st.builds(
    cobol_operators_Positive,
)
cobol_operators_Multiplication_strategy = st.builds(
    cobol_operators_Multiplication,
)
cobol_operators_ConditionAnd_strategy = st.builds(
    cobol_operators_ConditionAnd,
)
cobol_operators_ConditionOr_strategy = st.builds(
    cobol_operators_ConditionOr,
)
Operator_strategy = st.builds(
    Operator,
)
cobol_operators_LogicalOperator_strategy = st.builds(
    cobol_operators_LogicalOperator,
)
cobol_operators_MultiplicativeOperator_strategy = st.builds(
    cobol_operators_MultiplicativeOperator,
)
cobol_operators_RelationalOperator_strategy = st.builds(
    cobol_operators_RelationalOperator,
)
cobol_operators_UnaryOperator_strategy = st.builds(
    cobol_operators_UnaryOperator,
)
cobol_operators_SignOperator_strategy = st.builds(
    cobol_operators_SignOperator,
)
cobol_operators_AdditiveOperator_strategy = st.builds(
    cobol_operators_AdditiveOperator,
)
cobol_operators_Operator_strategy = st.builds(
    cobol_operators_Operator,
)
AlphanumericLiteral_strategy = st.builds(
    AlphanumericLiteral,
)
cobol_literals_AlphanumericHexaDecimalLiteral_strategy = st.builds(
    cobol_literals_AlphanumericHexaDecimalLiteral,
)
cobol_operators_ClassOperator_strategy = st.builds(
    cobol_operators_ClassOperator,
)
cobol_operators_Through_strategy = st.builds(
    cobol_operators_Through,
    value=
        safe_text
)
cobol_operators_Negate_strategy = st.builds(
    cobol_operators_Negate,
)
cobol_operators_Power_strategy = st.builds(
    cobol_operators_Power,
)
cobol_operators_Equal_strategy = st.builds(
    cobol_operators_Equal,
    to=
        st.booleans()
)
cobol_operators_LessThanOrEqual_strategy = st.builds(
    cobol_operators_LessThanOrEqual,
    than=
        st.booleans(),
    to=
        st.booleans()
)
cobol_operators_LessThan_strategy = st.builds(
    cobol_operators_LessThan,
    than=
        st.booleans()
)
cobol_operators_GreaterThan_strategy = st.builds(
    cobol_operators_GreaterThan,
    than=
        st.booleans()
)
cobol_operators_GreaterThanOrEqual_strategy = st.builds(
    cobol_operators_GreaterThanOrEqual,
    to=
        st.booleans(),
    than=
        st.booleans()
)
cobol_literals_HighValue_strategy = st.builds(
    cobol_literals_HighValue,
    value=
        safe_text
)
cobol_literals_LowValue_strategy = st.builds(
    cobol_literals_LowValue,
    value=
        safe_text
)
cobol_literals_Quote_strategy = st.builds(
    cobol_literals_Quote,
    value=
        safe_text
)
cobol_literals_Zero_strategy = st.builds(
    cobol_literals_Zero,
    value=
        safe_text
)
cobol_literals_Null_strategy = st.builds(
    cobol_literals_Null,
    value=
        safe_text
)
cobol_literals_FixedDecimalLiteral_strategy = st.builds(
    cobol_literals_FixedDecimalLiteral,
)
DBCSLiteral_strategy = st.builds(
    DBCSLiteral,
)
cobol_literals_NationalHexLiteral_strategy = st.builds(
    cobol_literals_NationalHexLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cobol_literals_NationalLiteral_strategy = st.builds(
    cobol_literals_NationalLiteral,
    value=
        safe_text
)
cobol_literals_DBCSLiteral_strategy = st.builds(
    cobol_literals_DBCSLiteral,
)
cobol_literals_PseudoLiteral_strategy = st.builds(
    cobol_literals_PseudoLiteral,
    value=
        safe_text
)
cobol_literals_Characters_strategy = st.builds(
    cobol_literals_Characters,
)
cobol_literals_Any_strategy = st.builds(
    cobol_literals_Any,
)
cobol_literals_Space_strategy = st.builds(
    cobol_literals_Space,
    value=
        safe_text
)
labels_StopLabel_strategy = st.builds(
    labels_StopLabel,
)
cobol_literals_Literal_strategy = st.builds(
    cobol_literals_Literal,
)
cobol_literals_ConstantLiteral_strategy = st.builds(
    cobol_literals_ConstantLiteral,
)
cobol_literals_NumericLiteral_strategy = st.builds(
    cobol_literals_NumericLiteral,
)

@given(instance=strings_Occurrence_strategy)
@settings(max_examples=50)
def test_strings_occurrence_instantiation(instance):
    assert isinstance(instance, strings_Occurrence)

@given(instance=strings_Tallying_strategy)
@settings(max_examples=50)
def test_strings_tallying_instantiation(instance):
    assert isinstance(instance, strings_Tallying)

@given(instance=cobol_strings_TallyingOccurrence_strategy)
@settings(max_examples=50)
def test_cobol_strings_tallyingoccurrence_instantiation(instance):
    assert isinstance(instance, cobol_strings_TallyingOccurrence)

@given(instance=cobol_strings_Occurrence_strategy)
@settings(max_examples=50)
def test_cobol_strings_occurrence_instantiation(instance):
    assert isinstance(instance, cobol_strings_Occurrence)



@given(instance=cobol_strings_Occurrence_strategy)
def test_cobol_strings_occurrence_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cobol_strings_Location_strategy)
@settings(max_examples=50)
def test_cobol_strings_location_instantiation(instance):
    assert isinstance(instance, cobol_strings_Location)



@given(instance=cobol_strings_Location_strategy)
def test_cobol_strings_location_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=cobol_strings_Location_strategy)
def test_cobol_strings_location_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=ManipulatedStrings_strategy)
@settings(max_examples=50)
def test_manipulatedstrings_instantiation(instance):
    assert isinstance(instance, ManipulatedStrings)

@given(instance=cobol_strings_SplittedString_strategy)
@settings(max_examples=50)
def test_cobol_strings_splittedstring_instantiation(instance):
    assert isinstance(instance, cobol_strings_SplittedString)

@given(instance=cobol_strings_ConcatenatingStrings_strategy)
@settings(max_examples=50)
def test_cobol_strings_concatenatingstrings_instantiation(instance):
    assert isinstance(instance, cobol_strings_ConcatenatingStrings)

@given(instance=cobol_strings_String_strategy)
@settings(max_examples=50)
def test_cobol_strings_string_instantiation(instance):
    assert isinstance(instance, cobol_strings_String)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=String_strategy)
@settings(max_examples=50)
def test_string_instantiation(instance):
    assert isinstance(instance, String)

@given(instance=cobol_strings_ManipulatedStrings_strategy)
@settings(max_examples=50)
def test_cobol_strings_manipulatedstrings_instantiation(instance):
    assert isinstance(instance, cobol_strings_ManipulatedStrings)

@given(instance=cobol_strings_StringManipulation_strategy)
@settings(max_examples=50)
def test_cobol_strings_stringmanipulation_instantiation(instance):
    assert isinstance(instance, cobol_strings_StringManipulation)

@given(instance=StringManipulation_strategy)
@settings(max_examples=50)
def test_stringmanipulation_instantiation(instance):
    assert isinstance(instance, StringManipulation)

@given(instance=cobol_strings_Replacement_strategy)
@settings(max_examples=50)
def test_cobol_strings_replacement_instantiation(instance):
    assert isinstance(instance, cobol_strings_Replacement)

@given(instance=cobol_strings_Tallying_strategy)
@settings(max_examples=50)
def test_cobol_strings_tallying_instantiation(instance):
    assert isinstance(instance, cobol_strings_Tallying)

@given(instance=strings_Replacement_strategy)
@settings(max_examples=50)
def test_strings_replacement_instantiation(instance):
    assert isinstance(instance, strings_Replacement)

@given(instance=cobol_strings_ReplacementOccurrence_strategy)
@settings(max_examples=50)
def test_cobol_strings_replacementoccurrence_instantiation(instance):
    assert isinstance(instance, cobol_strings_ReplacementOccurrence)

@given(instance=NotErrorHandler_strategy)
@settings(max_examples=50)
def test_noterrorhandler_instantiation(instance):
    assert isinstance(instance, NotErrorHandler)

@given(instance=cobol_handlers_NotOnOverflow_strategy)
@settings(max_examples=50)
def test_cobol_handlers_notonoverflow_instantiation(instance):
    assert isinstance(instance, cobol_handlers_NotOnOverflow)

@given(instance=cobol_handlers_NotAtEnd_strategy)
@settings(max_examples=50)
def test_cobol_handlers_notatend_instantiation(instance):
    assert isinstance(instance, cobol_handlers_NotAtEnd)

@given(instance=cobol_handlers_NotInvalidKey_strategy)
@settings(max_examples=50)
def test_cobol_handlers_notinvalidkey_instantiation(instance):
    assert isinstance(instance, cobol_handlers_NotInvalidKey)

@given(instance=cobol_handlers_NotOnException_strategy)
@settings(max_examples=50)
def test_cobol_handlers_notonexception_instantiation(instance):
    assert isinstance(instance, cobol_handlers_NotOnException)

@given(instance=cobol_handlers_NotOnSizeError_strategy)
@settings(max_examples=50)
def test_cobol_handlers_notonsizeerror_instantiation(instance):
    assert isinstance(instance, cobol_handlers_NotOnSizeError)

@given(instance=cobol_functions_Argumentable_strategy)
@settings(max_examples=50)
def test_cobol_functions_argumentable_instantiation(instance):
    assert isinstance(instance, cobol_functions_Argumentable)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=cobol_functions_ByContentArgument_strategy)
@settings(max_examples=50)
def test_cobol_functions_bycontentargument_instantiation(instance):
    assert isinstance(instance, cobol_functions_ByContentArgument)

@given(instance=cobol_functions_ByValueArgument_strategy)
@settings(max_examples=50)
def test_cobol_functions_byvalueargument_instantiation(instance):
    assert isinstance(instance, cobol_functions_ByValueArgument)

@given(instance=cobol_functions_OmittedArgument_strategy)
@settings(max_examples=50)
def test_cobol_functions_omittedargument_instantiation(instance):
    assert isinstance(instance, cobol_functions_OmittedArgument)

@given(instance=cobol_functions_ByReferenceArgument_strategy)
@settings(max_examples=50)
def test_cobol_functions_byreferenceargument_instantiation(instance):
    assert isinstance(instance, cobol_functions_ByReferenceArgument)

@given(instance=cobol_functions_Argument_strategy)
@settings(max_examples=50)
def test_cobol_functions_argument_instantiation(instance):
    assert isinstance(instance, cobol_functions_Argument)

@given(instance=cobol_labels_Label_strategy)
@settings(max_examples=50)
def test_cobol_labels_label_instantiation(instance):
    assert isinstance(instance, cobol_labels_Label)

@given(instance=cobol_labels_Procedure_strategy)
@settings(max_examples=50)
def test_cobol_labels_procedure_instantiation(instance):
    assert isinstance(instance, cobol_labels_Procedure)

@given(instance=Procedure_strategy)
@settings(max_examples=50)
def test_procedure_instantiation(instance):
    assert isinstance(instance, Procedure)

@given(instance=cobol_handlers_NotAtEndOfPage_strategy)
@settings(max_examples=50)
def test_cobol_handlers_notatendofpage_instantiation(instance):
    assert isinstance(instance, cobol_handlers_NotAtEndOfPage)

@given(instance=ProcedureRangeChild_strategy)
@settings(max_examples=50)
def test_procedurerangechild_instantiation(instance):
    assert isinstance(instance, ProcedureRangeChild)

@given(instance=cobol_verbs_Verb_strategy)
@settings(max_examples=50)
def test_cobol_verbs_verb_instantiation(instance):
    assert isinstance(instance, cobol_verbs_Verb)

@given(instance=Verb_strategy)
@settings(max_examples=50)
def test_verb_instantiation(instance):
    assert isinstance(instance, Verb)

@given(instance=cobol_verbs_Is_strategy)
@settings(max_examples=50)
def test_cobol_verbs_is_instantiation(instance):
    assert isinstance(instance, cobol_verbs_Is)

@given(instance=DeclarativeSection_strategy)
@settings(max_examples=50)
def test_declarativesection_instantiation(instance):
    assert isinstance(instance, DeclarativeSection)

@given(instance=cobol_declaratives_Declaratives_strategy)
@settings(max_examples=50)
def test_cobol_declaratives_declaratives_instantiation(instance):
    assert isinstance(instance, cobol_declaratives_Declaratives)

@given(instance=cobol_labels_ProcedureLabel_strategy)
@settings(max_examples=50)
def test_cobol_labels_procedurelabel_instantiation(instance):
    assert isinstance(instance, cobol_labels_ProcedureLabel)

@given(instance=cobol_files_FileStatus_strategy)
@settings(max_examples=50)
def test_cobol_files_filestatus_instantiation(instance):
    assert isinstance(instance, cobol_files_FileStatus)

@given(instance=FileStatus_strategy)
@settings(max_examples=50)
def test_filestatus_instantiation(instance):
    assert isinstance(instance, FileStatus)

@given(instance=cobol_tables_TableDimension_strategy)
@settings(max_examples=50)
def test_cobol_tables_tabledimension_instantiation(instance):
    assert isinstance(instance, cobol_tables_TableDimension)



@given(instance=cobol_tables_TableDimension_strategy)
def test_cobol_tables_tabledimension_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AdditionalIndexName_strategy)
@settings(max_examples=50)
def test_additionalindexname_instantiation(instance):
    assert isinstance(instance, AdditionalIndexName)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=cobol_parameters_ByReferenceParameter_strategy)
@settings(max_examples=50)
def test_cobol_parameters_byreferenceparameter_instantiation(instance):
    assert isinstance(instance, cobol_parameters_ByReferenceParameter)

@given(instance=cobol_parameters_ByValueParameter_strategy)
@settings(max_examples=50)
def test_cobol_parameters_byvalueparameter_instantiation(instance):
    assert isinstance(instance, cobol_parameters_ByValueParameter)

@given(instance=cobol_parameters_Parametrizable_strategy)
@settings(max_examples=50)
def test_cobol_parameters_parametrizable_instantiation(instance):
    assert isinstance(instance, cobol_parameters_Parametrizable)

@given(instance=IndexName_strategy)
@settings(max_examples=50)
def test_indexname_instantiation(instance):
    assert isinstance(instance, IndexName)

@given(instance=TableDimension_strategy)
@settings(max_examples=50)
def test_tabledimension_instantiation(instance):
    assert isinstance(instance, TableDimension)

@given(instance=dataitems_DataItem_strategy)
@settings(max_examples=50)
def test_dataitems_dataitem_instantiation(instance):
    assert isinstance(instance, dataitems_DataItem)

@given(instance=cobol_specialnames_SpecialNameStatement_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_specialnamestatement_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_SpecialNameStatement)

@given(instance=AlphabetNameReference_strategy)
@settings(max_examples=50)
def test_alphabetnamereference_instantiation(instance):
    assert isinstance(instance, AlphabetNameReference)

@given(instance=SymbolicCharacter_strategy)
@settings(max_examples=50)
def test_symboliccharacter_instantiation(instance):
    assert isinstance(instance, SymbolicCharacter)

@given(instance=SpecialName_strategy)
@settings(max_examples=50)
def test_specialname_instantiation(instance):
    assert isinstance(instance, SpecialName)

@given(instance=cobol_specialnames_SymbolicCharacter_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_symboliccharacter_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_SymbolicCharacter)

@given(instance=cobol_specialnames_MnemonicName_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_mnemonicname_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_MnemonicName)

@given(instance=cobol_tables_KeyName_strategy)
@settings(max_examples=50)
def test_cobol_tables_keyname_instantiation(instance):
    assert isinstance(instance, cobol_tables_KeyName)



@given(instance=cobol_tables_KeyName_strategy)
def test_cobol_tables_keyname_keyOrder_setter(instance):
    original = instance.keyOrder
    instance.keyOrder = original
    assert instance.keyOrder == original

@given(instance=KeyName_strategy)
@settings(max_examples=50)
def test_keyname_instantiation(instance):
    assert isinstance(instance, KeyName)

@given(instance=cobol_specialnames_AlphabetType_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_alphabettype_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_AlphabetType)

@given(instance=specialnames_MnemonicName_strategy)
@settings(max_examples=50)
def test_specialnames_mnemonicname_instantiation(instance):
    assert isinstance(instance, specialnames_MnemonicName)

@given(instance=AlphabetType_strategy)
@settings(max_examples=50)
def test_alphabettype_instantiation(instance):
    assert isinstance(instance, AlphabetType)

@given(instance=cobol_specialnames_PredefinedAlphabetType_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_predefinedalphabettype_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_PredefinedAlphabetType)



@given(instance=cobol_specialnames_PredefinedAlphabetType_strategy)
def test_cobol_specialnames_predefinedalphabettype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_specialnames_CodeNameAlphabetType_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_codenamealphabettype_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_CodeNameAlphabetType)



@given(instance=cobol_specialnames_CodeNameAlphabetType_strategy)
def test_cobol_specialnames_codenamealphabettype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=specialnames_SpecialNameStatement_strategy)
@settings(max_examples=50)
def test_specialnames_specialnamestatement_instantiation(instance):
    assert isinstance(instance, specialnames_SpecialNameStatement)

@given(instance=cobol_specialnames_SystemDeviceIs_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_systemdeviceis_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_SystemDeviceIs)

@given(instance=cobol_specialnames_UPSISwitchIs_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_upsiswitchis_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_UPSISwitchIs)

@given(instance=ConditionName_strategy)
@settings(max_examples=50)
def test_conditionname_instantiation(instance):
    assert isinstance(instance, ConditionName)

@given(instance=cobol_specialnames_OffStatus_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_offstatus_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_OffStatus)

@given(instance=cobol_specialnames_OnStatus_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_onstatus_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_OnStatus)

@given(instance=specialnames_SpecialName_strategy)
@settings(max_examples=50)
def test_specialnames_specialname_instantiation(instance):
    assert isinstance(instance, specialnames_SpecialName)

@given(instance=cobol_specialnames_CurrencySign_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_currencysign_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_CurrencySign)



@given(instance=cobol_specialnames_CurrencySign_strategy)
def test_cobol_specialnames_currencysign_pictureSymbol_setter(instance):
    original = instance.pictureSymbol
    instance.pictureSymbol = original
    assert instance.pictureSymbol == original

@given(instance=cobol_specialnames_AlphabetName_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_alphabetname_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_AlphabetName)

@given(instance=cobol_specialnames_ClassName_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_classname_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_ClassName)

@given(instance=cobol_specialnames_ExplicitAlphabetType_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_explicitalphabettype_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_ExplicitAlphabetType)

@given(instance=references_ReferenceableElement_strategy)
@settings(max_examples=50)
def test_references_referenceableelement_instantiation(instance):
    assert isinstance(instance, references_ReferenceableElement)

@given(instance=cobol_dataitems_DataItemAttribute_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_dataitemattribute_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_DataItemAttribute)

@given(instance=RangeExpression_strategy)
@settings(max_examples=50)
def test_rangeexpression_instantiation(instance):
    assert isinstance(instance, RangeExpression)

@given(instance=DataName_strategy)
@settings(max_examples=50)
def test_dataname_instantiation(instance):
    assert isinstance(instance, DataName)

@given(instance=cobol_dataitems_RenamingDataName_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_renamingdataname_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_RenamingDataName)

@given(instance=DataItemAttribute_strategy)
@settings(max_examples=50)
def test_dataitemattribute_instantiation(instance):
    assert isinstance(instance, DataItemAttribute)

@given(instance=cobol_dataitems_GroupUsage_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_groupusage_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_GroupUsage)

@given(instance=cobol_dataitems_Redefines_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_redefines_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_Redefines)

@given(instance=cobol_dataitems_Value_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_value_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_Value)

@given(instance=cobol_dataitems_Global_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_global_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_Global)

@given(instance=cobol_dataitems_External_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_external_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_External)

@given(instance=cobol_dataitems_Usage_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_usage_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_Usage)



@given(instance=cobol_dataitems_Usage_strategy)
def test_cobol_dataitems_usage_usage_setter(instance):
    original = instance.usage
    instance.usage = original
    assert instance.usage == original



@given(instance=cobol_dataitems_Usage_strategy)
def test_cobol_dataitems_usage_isNative_setter(instance):
    original = instance.isNative
    instance.isNative = original
    assert instance.isNative == original

@given(instance=cobol_dataitems_PictureString_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_picturestring_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_PictureString)



@given(instance=cobol_dataitems_PictureString_strategy)
def test_cobol_dataitems_picturestring_picture_setter(instance):
    original = instance.picture
    instance.picture = original
    assert instance.picture == original

@given(instance=SystemDevice_strategy)
@settings(max_examples=50)
def test_systemdevice_instantiation(instance):
    assert isinstance(instance, SystemDevice)

@given(instance=cobol_environments_SystemPunchDevice_strategy)
@settings(max_examples=50)
def test_cobol_environments_systempunchdevice_instantiation(instance):
    assert isinstance(instance, cobol_environments_SystemPunchDevice)



@given(instance=cobol_environments_SystemPunchDevice_strategy)
def test_cobol_environments_systempunchdevice_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_environments_AdvancedFunctionPrinting_strategy)
@settings(max_examples=50)
def test_cobol_environments_advancedfunctionprinting_instantiation(instance):
    assert isinstance(instance, cobol_environments_AdvancedFunctionPrinting)

@given(instance=cobol_environments_SuppressSpacing_strategy)
@settings(max_examples=50)
def test_cobol_environments_suppressspacing_instantiation(instance):
    assert isinstance(instance, cobol_environments_SuppressSpacing)

@given(instance=cobol_environments_Console_strategy)
@settings(max_examples=50)
def test_cobol_environments_console_instantiation(instance):
    assert isinstance(instance, cobol_environments_Console)

@given(instance=cobol_environments_SystemLogicalOutput_strategy)
@settings(max_examples=50)
def test_cobol_environments_systemlogicaloutput_instantiation(instance):
    assert isinstance(instance, cobol_environments_SystemLogicalOutput)



@given(instance=cobol_environments_SystemLogicalOutput_strategy)
def test_cobol_environments_systemlogicaloutput_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_environments_Pocket_strategy)
@settings(max_examples=50)
def test_cobol_environments_pocket_instantiation(instance):
    assert isinstance(instance, cobol_environments_Pocket)



@given(instance=cobol_environments_Pocket_strategy)
def test_cobol_environments_pocket_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_environments_Channel_strategy)
@settings(max_examples=50)
def test_cobol_environments_channel_instantiation(instance):
    assert isinstance(instance, cobol_environments_Channel)



@given(instance=cobol_environments_Channel_strategy)
def test_cobol_environments_channel_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_environments_SystemLogicalInput_strategy)
@settings(max_examples=50)
def test_cobol_environments_systemlogicalinput_instantiation(instance):
    assert isinstance(instance, cobol_environments_SystemLogicalInput)



@given(instance=cobol_environments_SystemLogicalInput_strategy)
def test_cobol_environments_systemlogicalinput_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Register_strategy)
@settings(max_examples=50)
def test_register_instantiation(instance):
    assert isinstance(instance, Register)

@given(instance=cobol_registers_ShiftOut_strategy)
@settings(max_examples=50)
def test_cobol_registers_shiftout_instantiation(instance):
    assert isinstance(instance, cobol_registers_ShiftOut)

@given(instance=cobol_registers_AddressOf_strategy)
@settings(max_examples=50)
def test_cobol_registers_addressof_instantiation(instance):
    assert isinstance(instance, cobol_registers_AddressOf)

@given(instance=cobol_registers_LengthOf_strategy)
@settings(max_examples=50)
def test_cobol_registers_lengthof_instantiation(instance):
    assert isinstance(instance, cobol_registers_LengthOf)

@given(instance=cobol_registers_WhenCompiled_strategy)
@settings(max_examples=50)
def test_cobol_registers_whencompiled_instantiation(instance):
    assert isinstance(instance, cobol_registers_WhenCompiled)

@given(instance=cobol_registers_ReturnCode_strategy)
@settings(max_examples=50)
def test_cobol_registers_returncode_instantiation(instance):
    assert isinstance(instance, cobol_registers_ReturnCode)

@given(instance=cobol_registers_ShiftIn_strategy)
@settings(max_examples=50)
def test_cobol_registers_shiftin_instantiation(instance):
    assert isinstance(instance, cobol_registers_ShiftIn)

@given(instance=SortPhraseWater_strategy)
@settings(max_examples=50)
def test_sortphrasewater_instantiation(instance):
    assert isinstance(instance, SortPhraseWater)

@given(instance=cobol_water_SortPhraseToken_strategy)
@settings(max_examples=50)
def test_cobol_water_sortphrasetoken_instantiation(instance):
    assert isinstance(instance, cobol_water_SortPhraseToken)



@given(instance=cobol_water_SortPhraseToken_strategy)
def test_cobol_water_sortphrasetoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OpenStatementWater_strategy)
@settings(max_examples=50)
def test_openstatementwater_instantiation(instance):
    assert isinstance(instance, OpenStatementWater)

@given(instance=cobol_water_OpenStatementToken_strategy)
@settings(max_examples=50)
def test_cobol_water_openstatementtoken_instantiation(instance):
    assert isinstance(instance, cobol_water_OpenStatementToken)



@given(instance=cobol_water_OpenStatementToken_strategy)
def test_cobol_water_openstatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=InvokeStatementWater_strategy)
@settings(max_examples=50)
def test_invokestatementwater_instantiation(instance):
    assert isinstance(instance, InvokeStatementWater)

@given(instance=cobol_water_InvokeStatementToken_strategy)
@settings(max_examples=50)
def test_cobol_water_invokestatementtoken_instantiation(instance):
    assert isinstance(instance, cobol_water_InvokeStatementToken)



@given(instance=cobol_water_InvokeStatementToken_strategy)
def test_cobol_water_invokestatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CloseStatementWater_strategy)
@settings(max_examples=50)
def test_closestatementwater_instantiation(instance):
    assert isinstance(instance, CloseStatementWater)

@given(instance=cobol_water_CloseStatementToken_strategy)
@settings(max_examples=50)
def test_cobol_water_closestatementtoken_instantiation(instance):
    assert isinstance(instance, cobol_water_CloseStatementToken)



@given(instance=cobol_water_CloseStatementToken_strategy)
def test_cobol_water_closestatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UseStatementWater_strategy)
@settings(max_examples=50)
def test_usestatementwater_instantiation(instance):
    assert isinstance(instance, UseStatementWater)

@given(instance=cobol_water_UseStatementToken_strategy)
@settings(max_examples=50)
def test_cobol_water_usestatementtoken_instantiation(instance):
    assert isinstance(instance, cobol_water_UseStatementToken)



@given(instance=cobol_water_UseStatementToken_strategy)
def test_cobol_water_usestatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AcceptStatementWater_strategy)
@settings(max_examples=50)
def test_acceptstatementwater_instantiation(instance):
    assert isinstance(instance, AcceptStatementWater)

@given(instance=cobol_environments_Environment_strategy)
@settings(max_examples=50)
def test_cobol_environments_environment_instantiation(instance):
    assert isinstance(instance, cobol_environments_Environment)

@given(instance=cobol_water_AcceptStatementToken_strategy)
@settings(max_examples=50)
def test_cobol_water_acceptstatementtoken_instantiation(instance):
    assert isinstance(instance, cobol_water_AcceptStatementToken)



@given(instance=cobol_water_AcceptStatementToken_strategy)
def test_cobol_water_acceptstatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CICSStatementWater_strategy)
@settings(max_examples=50)
def test_cicsstatementwater_instantiation(instance):
    assert isinstance(instance, CICSStatementWater)

@given(instance=cobol_water_CICSStatementToken_strategy)
@settings(max_examples=50)
def test_cobol_water_cicsstatementtoken_instantiation(instance):
    assert isinstance(instance, cobol_water_CICSStatementToken)



@given(instance=cobol_water_CICSStatementToken_strategy)
def test_cobol_water_cicsstatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQLStatementWater_strategy)
@settings(max_examples=50)
def test_sqlstatementwater_instantiation(instance):
    assert isinstance(instance, SQLStatementWater)

@given(instance=cobol_water_SQLStatementToken_strategy)
@settings(max_examples=50)
def test_cobol_water_sqlstatementtoken_instantiation(instance):
    assert isinstance(instance, cobol_water_SQLStatementToken)



@given(instance=cobol_water_SQLStatementToken_strategy)
def test_cobol_water_sqlstatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=RepositoryParagraphWater_strategy)
@settings(max_examples=50)
def test_repositoryparagraphwater_instantiation(instance):
    assert isinstance(instance, RepositoryParagraphWater)

@given(instance=cobol_water_RepositoryDescription_strategy)
@settings(max_examples=50)
def test_cobol_water_repositorydescription_instantiation(instance):
    assert isinstance(instance, cobol_water_RepositoryDescription)



@given(instance=cobol_water_RepositoryDescription_strategy)
def test_cobol_water_repositorydescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=IOControlParagraphWater_strategy)
@settings(max_examples=50)
def test_iocontrolparagraphwater_instantiation(instance):
    assert isinstance(instance, IOControlParagraphWater)

@given(instance=cobol_water_IOControlDescription_strategy)
@settings(max_examples=50)
def test_cobol_water_iocontroldescription_instantiation(instance):
    assert isinstance(instance, cobol_water_IOControlDescription)



@given(instance=cobol_water_IOControlDescription_strategy)
def test_cobol_water_iocontroldescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DataDescriptorWater_strategy)
@settings(max_examples=50)
def test_datadescriptorwater_instantiation(instance):
    assert isinstance(instance, DataDescriptorWater)

@given(instance=cobol_water_DataDescription_strategy)
@settings(max_examples=50)
def test_cobol_water_datadescription_instantiation(instance):
    assert isinstance(instance, cobol_water_DataDescription)



@given(instance=cobol_water_DataDescription_strategy)
def test_cobol_water_datadescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FileDescriptorWater_strategy)
@settings(max_examples=50)
def test_filedescriptorwater_instantiation(instance):
    assert isinstance(instance, FileDescriptorWater)

@given(instance=cobol_water_FileDescription_strategy)
@settings(max_examples=50)
def test_cobol_water_filedescription_instantiation(instance):
    assert isinstance(instance, cobol_water_FileDescription)



@given(instance=cobol_water_FileDescription_strategy)
def test_cobol_water_filedescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SelectStatementWater_strategy)
@settings(max_examples=50)
def test_selectstatementwater_instantiation(instance):
    assert isinstance(instance, SelectStatementWater)

@given(instance=cobol_water_SelectStatementClause_strategy)
@settings(max_examples=50)
def test_cobol_water_selectstatementclause_instantiation(instance):
    assert isinstance(instance, cobol_water_SelectStatementClause)



@given(instance=cobol_water_SelectStatementClause_strategy)
def test_cobol_water_selectstatementclause_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ObjectComputerParagraphWater_strategy)
@settings(max_examples=50)
def test_objectcomputerparagraphwater_instantiation(instance):
    assert isinstance(instance, ObjectComputerParagraphWater)

@given(instance=cobol_water_PriorityNumber_strategy)
@settings(max_examples=50)
def test_cobol_water_prioritynumber_instantiation(instance):
    assert isinstance(instance, cobol_water_PriorityNumber)



@given(instance=cobol_water_PriorityNumber_strategy)
def test_cobol_water_prioritynumber_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_water_ObjectComputerDescription_strategy)
@settings(max_examples=50)
def test_cobol_water_objectcomputerdescription_instantiation(instance):
    assert isinstance(instance, cobol_water_ObjectComputerDescription)



@given(instance=cobol_water_ObjectComputerDescription_strategy)
def test_cobol_water_objectcomputerdescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_water_Water_strategy)
@settings(max_examples=50)
def test_cobol_water_water_instantiation(instance):
    assert isinstance(instance, cobol_water_Water)

@given(instance=Water_strategy)
@settings(max_examples=50)
def test_water_instantiation(instance):
    assert isinstance(instance, Water)

@given(instance=cobol_water_CloseStatementWater_strategy)
@settings(max_examples=50)
def test_cobol_water_closestatementwater_instantiation(instance):
    assert isinstance(instance, cobol_water_CloseStatementWater)

@given(instance=cobol_water_FileDescriptorWater_strategy)
@settings(max_examples=50)
def test_cobol_water_filedescriptorwater_instantiation(instance):
    assert isinstance(instance, cobol_water_FileDescriptorWater)

@given(instance=cobol_water_InvokeStatementWater_strategy)
@settings(max_examples=50)
def test_cobol_water_invokestatementwater_instantiation(instance):
    assert isinstance(instance, cobol_water_InvokeStatementWater)

@given(instance=cobol_water_DataDescriptorWater_strategy)
@settings(max_examples=50)
def test_cobol_water_datadescriptorwater_instantiation(instance):
    assert isinstance(instance, cobol_water_DataDescriptorWater)

@given(instance=cobol_water_SelectStatementWater_strategy)
@settings(max_examples=50)
def test_cobol_water_selectstatementwater_instantiation(instance):
    assert isinstance(instance, cobol_water_SelectStatementWater)

@given(instance=cobol_water_SQLStatementWater_strategy)
@settings(max_examples=50)
def test_cobol_water_sqlstatementwater_instantiation(instance):
    assert isinstance(instance, cobol_water_SQLStatementWater)

@given(instance=cobol_water_AcceptStatementWater_strategy)
@settings(max_examples=50)
def test_cobol_water_acceptstatementwater_instantiation(instance):
    assert isinstance(instance, cobol_water_AcceptStatementWater)

@given(instance=cobol_water_IdentificationDivisionWater_strategy)
@settings(max_examples=50)
def test_cobol_water_identificationdivisionwater_instantiation(instance):
    assert isinstance(instance, cobol_water_IdentificationDivisionWater)

@given(instance=cobol_water_UseStatementWater_strategy)
@settings(max_examples=50)
def test_cobol_water_usestatementwater_instantiation(instance):
    assert isinstance(instance, cobol_water_UseStatementWater)

@given(instance=cobol_water_IOControlParagraphWater_strategy)
@settings(max_examples=50)
def test_cobol_water_iocontrolparagraphwater_instantiation(instance):
    assert isinstance(instance, cobol_water_IOControlParagraphWater)

@given(instance=cobol_water_SpecialNamesParagraphWater_strategy)
@settings(max_examples=50)
def test_cobol_water_specialnamesparagraphwater_instantiation(instance):
    assert isinstance(instance, cobol_water_SpecialNamesParagraphWater)

@given(instance=cobol_water_ObjectComputerParagraphWater_strategy)
@settings(max_examples=50)
def test_cobol_water_objectcomputerparagraphwater_instantiation(instance):
    assert isinstance(instance, cobol_water_ObjectComputerParagraphWater)

@given(instance=cobol_water_OpenStatementWater_strategy)
@settings(max_examples=50)
def test_cobol_water_openstatementwater_instantiation(instance):
    assert isinstance(instance, cobol_water_OpenStatementWater)

@given(instance=cobol_water_CICSStatementWater_strategy)
@settings(max_examples=50)
def test_cobol_water_cicsstatementwater_instantiation(instance):
    assert isinstance(instance, cobol_water_CICSStatementWater)

@given(instance=cobol_water_SortPhraseWater_strategy)
@settings(max_examples=50)
def test_cobol_water_sortphrasewater_instantiation(instance):
    assert isinstance(instance, cobol_water_SortPhraseWater)

@given(instance=cobol_water_RepositoryParagraphWater_strategy)
@settings(max_examples=50)
def test_cobol_water_repositoryparagraphwater_instantiation(instance):
    assert isinstance(instance, cobol_water_RepositoryParagraphWater)

@given(instance=cobol_water_IncompleteElement_strategy)
@settings(max_examples=50)
def test_cobol_water_incompleteelement_instantiation(instance):
    assert isinstance(instance, cobol_water_IncompleteElement)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=cobol_labels_ProcedureRangeLabel_strategy)
@settings(max_examples=50)
def test_cobol_labels_procedurerangelabel_instantiation(instance):
    assert isinstance(instance, cobol_labels_ProcedureRangeLabel)

@given(instance=cobol_labels_StopLabel_strategy)
@settings(max_examples=50)
def test_cobol_labels_stoplabel_instantiation(instance):
    assert isinstance(instance, cobol_labels_StopLabel)

@given(instance=cobol_ios_IODirectives_strategy)
@settings(max_examples=50)
def test_cobol_ios_iodirectives_instantiation(instance):
    assert isinstance(instance, cobol_ios_IODirectives)

@given(instance=ios_OutputDirective_strategy)
@settings(max_examples=50)
def test_ios_outputdirective_instantiation(instance):
    assert isinstance(instance, ios_OutputDirective)

@given(instance=ios_FileDirective_strategy)
@settings(max_examples=50)
def test_ios_filedirective_instantiation(instance):
    assert isinstance(instance, ios_FileDirective)

@given(instance=cobol_ios_OutputFile_strategy)
@settings(max_examples=50)
def test_cobol_ios_outputfile_instantiation(instance):
    assert isinstance(instance, cobol_ios_OutputFile)

@given(instance=IODirectives_strategy)
@settings(max_examples=50)
def test_iodirectives_instantiation(instance):
    assert isinstance(instance, IODirectives)

@given(instance=cobol_ios_OutputDirective_strategy)
@settings(max_examples=50)
def test_cobol_ios_outputdirective_instantiation(instance):
    assert isinstance(instance, cobol_ios_OutputDirective)

@given(instance=cobol_ios_FileDirective_strategy)
@settings(max_examples=50)
def test_cobol_ios_filedirective_instantiation(instance):
    assert isinstance(instance, cobol_ios_FileDirective)

@given(instance=cobol_ios_ProcedureDirective_strategy)
@settings(max_examples=50)
def test_cobol_ios_proceduredirective_instantiation(instance):
    assert isinstance(instance, cobol_ios_ProcedureDirective)

@given(instance=cobol_ios_InputDirective_strategy)
@settings(max_examples=50)
def test_cobol_ios_inputdirective_instantiation(instance):
    assert isinstance(instance, cobol_ios_InputDirective)

@given(instance=ios_ProcedureDirective_strategy)
@settings(max_examples=50)
def test_ios_proceduredirective_instantiation(instance):
    assert isinstance(instance, ios_ProcedureDirective)

@given(instance=cobol_ios_OutputProcedure_strategy)
@settings(max_examples=50)
def test_cobol_ios_outputprocedure_instantiation(instance):
    assert isinstance(instance, cobol_ios_OutputProcedure)

@given(instance=ios_InputDirective_strategy)
@settings(max_examples=50)
def test_ios_inputdirective_instantiation(instance):
    assert isinstance(instance, ios_InputDirective)

@given(instance=cobol_ios_InputFile_strategy)
@settings(max_examples=50)
def test_cobol_ios_inputfile_instantiation(instance):
    assert isinstance(instance, cobol_ios_InputFile)

@given(instance=cobol_ios_InputProcedure_strategy)
@settings(max_examples=50)
def test_cobol_ios_inputprocedure_instantiation(instance):
    assert isinstance(instance, cobol_ios_InputProcedure)

@given(instance=cobol_identifiers_ReferenceModifier_strategy)
@settings(max_examples=50)
def test_cobol_identifiers_referencemodifier_instantiation(instance):
    assert isinstance(instance, cobol_identifiers_ReferenceModifier)

@given(instance=DirectSubscript_strategy)
@settings(max_examples=50)
def test_directsubscript_instantiation(instance):
    assert isinstance(instance, DirectSubscript)

@given(instance=cobol_identifiers_All_strategy)
@settings(max_examples=50)
def test_cobol_identifiers_all_instantiation(instance):
    assert isinstance(instance, cobol_identifiers_All)

@given(instance=IdentificationDivisionWater_strategy)
@settings(max_examples=50)
def test_identificationdivisionwater_instantiation(instance):
    assert isinstance(instance, IdentificationDivisionWater)

@given(instance=cobol_water_ProgramDescription_strategy)
@settings(max_examples=50)
def test_cobol_water_programdescription_instantiation(instance):
    assert isinstance(instance, cobol_water_ProgramDescription)



@given(instance=cobol_water_ProgramDescription_strategy)
def test_cobol_water_programdescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Subscript_strategy)
@settings(max_examples=50)
def test_subscript_instantiation(instance):
    assert isinstance(instance, Subscript)

@given(instance=cobol_identifiers_RelativeSubscript_strategy)
@settings(max_examples=50)
def test_cobol_identifiers_relativesubscript_instantiation(instance):
    assert isinstance(instance, cobol_identifiers_RelativeSubscript)

@given(instance=cobol_identifiers_DirectSubscript_strategy)
@settings(max_examples=50)
def test_cobol_identifiers_directsubscript_instantiation(instance):
    assert isinstance(instance, cobol_identifiers_DirectSubscript)

@given(instance=identifiers_Identifier_strategy)
@settings(max_examples=50)
def test_identifiers_identifier_instantiation(instance):
    assert isinstance(instance, identifiers_Identifier)

@given(instance=ReferenceModifier_strategy)
@settings(max_examples=50)
def test_referencemodifier_instantiation(instance):
    assert isinstance(instance, ReferenceModifier)

@given(instance=water_SortPhraseWater_strategy)
@settings(max_examples=50)
def test_water_sortphrasewater_instantiation(instance):
    assert isinstance(instance, water_SortPhraseWater)

@given(instance=water_DataDescriptorWater_strategy)
@settings(max_examples=50)
def test_water_datadescriptorwater_instantiation(instance):
    assert isinstance(instance, water_DataDescriptorWater)

@given(instance=statements_Statement_strategy)
@settings(max_examples=50)
def test_statements_statement_instantiation(instance):
    assert isinstance(instance, statements_Statement)

@given(instance=water_UseStatementWater_strategy)
@settings(max_examples=50)
def test_water_usestatementwater_instantiation(instance):
    assert isinstance(instance, water_UseStatementWater)

@given(instance=DataItem_strategy)
@settings(max_examples=50)
def test_dataitem_instantiation(instance):
    assert isinstance(instance, DataItem)

@given(instance=cobol_dataitems_ConditionName_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_conditionname_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_ConditionName)

@given(instance=cobol_dataitems_RecordName_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_recordname_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_RecordName)

@given(instance=cobol_dataitems_DataName_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_dataname_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_DataName)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=EnvironmentDivisionSection_strategy)
@settings(max_examples=50)
def test_environmentdivisionsection_instantiation(instance):
    assert isinstance(instance, EnvironmentDivisionSection)

@given(instance=cobol_sections_ConfigurationSection_strategy)
@settings(max_examples=50)
def test_cobol_sections_configurationsection_instantiation(instance):
    assert isinstance(instance, cobol_sections_ConfigurationSection)

@given(instance=cobol_sections_IOSection_strategy)
@settings(max_examples=50)
def test_cobol_sections_iosection_instantiation(instance):
    assert isinstance(instance, cobol_sections_IOSection)

@given(instance=ArithmeticOperand_strategy)
@settings(max_examples=50)
def test_arithmeticoperand_instantiation(instance):
    assert isinstance(instance, ArithmeticOperand)

@given(instance=cobol_operands_RoundedIdentifier_strategy)
@settings(max_examples=50)
def test_cobol_operands_roundedidentifier_instantiation(instance):
    assert isinstance(instance, cobol_operands_RoundedIdentifier)

@given(instance=water_SQLStatementWater_strategy)
@settings(max_examples=50)
def test_water_sqlstatementwater_instantiation(instance):
    assert isinstance(instance, water_SQLStatementWater)

@given(instance=water_IdentificationDivisionWater_strategy)
@settings(max_examples=50)
def test_water_identificationdivisionwater_instantiation(instance):
    assert isinstance(instance, water_IdentificationDivisionWater)

@given(instance=cobol_water_Dot_strategy)
@settings(max_examples=50)
def test_cobol_water_dot_instantiation(instance):
    assert isinstance(instance, cobol_water_Dot)

@given(instance=water_RepositoryParagraphWater_strategy)
@settings(max_examples=50)
def test_water_repositoryparagraphwater_instantiation(instance):
    assert isinstance(instance, water_RepositoryParagraphWater)

@given(instance=water_AcceptStatementWater_strategy)
@settings(max_examples=50)
def test_water_acceptstatementwater_instantiation(instance):
    assert isinstance(instance, water_AcceptStatementWater)

@given(instance=cobol_identifiers_Subscript_strategy)
@settings(max_examples=50)
def test_cobol_identifiers_subscript_instantiation(instance):
    assert isinstance(instance, cobol_identifiers_Subscript)

@given(instance=VaryingUntilCondition_strategy)
@settings(max_examples=50)
def test_varyinguntilcondition_instantiation(instance):
    assert isinstance(instance, VaryingUntilCondition)

@given(instance=cobol_statements_AfterUntilCondition_strategy)
@settings(max_examples=50)
def test_cobol_statements_afteruntilcondition_instantiation(instance):
    assert isinstance(instance, cobol_statements_AfterUntilCondition)

@given(instance=Qualifier_strategy)
@settings(max_examples=50)
def test_qualifier_instantiation(instance):
    assert isinstance(instance, Qualifier)

@given(instance=Conditional_strategy)
@settings(max_examples=50)
def test_conditional_instantiation(instance):
    assert isinstance(instance, Conditional)

@given(instance=cobol_statements_VaryingUntilCondition_strategy)
@settings(max_examples=50)
def test_cobol_statements_varyinguntilcondition_instantiation(instance):
    assert isinstance(instance, cobol_statements_VaryingUntilCondition)

@given(instance=Tallying_strategy)
@settings(max_examples=50)
def test_tallying_instantiation(instance):
    assert isinstance(instance, Tallying)

@given(instance=cobol_strings_AnyCharacter_strategy)
@settings(max_examples=50)
def test_cobol_strings_anycharacter_instantiation(instance):
    assert isinstance(instance, cobol_strings_AnyCharacter)

@given(instance=cobol_strings_SpecificCharacter_strategy)
@settings(max_examples=50)
def test_cobol_strings_specificcharacter_instantiation(instance):
    assert isinstance(instance, cobol_strings_SpecificCharacter)

@given(instance=cobol_statements_TallyingIn_strategy)
@settings(max_examples=50)
def test_cobol_statements_tallyingin_instantiation(instance):
    assert isinstance(instance, cobol_statements_TallyingIn)

@given(instance=IncompleteElement_strategy)
@settings(max_examples=50)
def test_incompleteelement_instantiation(instance):
    assert isinstance(instance, IncompleteElement)

@given(instance=cobol_files_SelectStatement_strategy)
@settings(max_examples=50)
def test_cobol_files_selectstatement_instantiation(instance):
    assert isinstance(instance, cobol_files_SelectStatement)



@given(instance=cobol_files_SelectStatement_strategy)
def test_cobol_files_selectstatement_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original



@given(instance=cobol_files_SelectStatement_strategy)
def test_cobol_files_selectstatement_externalFileNames_setter(instance):
    original = instance.externalFileNames
    instance.externalFileNames = original
    assert instance.externalFileNames == original

@given(instance=cobol_statements_IOFile_strategy)
@settings(max_examples=50)
def test_cobol_statements_iofile_instantiation(instance):
    assert isinstance(instance, cobol_statements_IOFile)

@given(instance=IOFile_strategy)
@settings(max_examples=50)
def test_iofile_instantiation(instance):
    assert isinstance(instance, IOFile)

@given(instance=cobol_statements_IOFileDescriptor_strategy)
@settings(max_examples=50)
def test_cobol_statements_iofiledescriptor_instantiation(instance):
    assert isinstance(instance, cobol_statements_IOFileDescriptor)



@given(instance=cobol_statements_IOFileDescriptor_strategy)
def test_cobol_statements_iofiledescriptor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=IOFileDescriptor_strategy)
@settings(max_examples=50)
def test_iofiledescriptor_instantiation(instance):
    assert isinstance(instance, IOFileDescriptor)

@given(instance=cobol_statements_IOStatement_strategy)
@settings(max_examples=50)
def test_cobol_statements_iostatement_instantiation(instance):
    assert isinstance(instance, cobol_statements_IOStatement)

@given(instance=cobol_statements_KeyDescriptor_strategy)
@settings(max_examples=50)
def test_cobol_statements_keydescriptor_instantiation(instance):
    assert isinstance(instance, cobol_statements_KeyDescriptor)



@given(instance=cobol_statements_KeyDescriptor_strategy)
def test_cobol_statements_keydescriptor_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=statements_VaryingUntilCondition_strategy)
@settings(max_examples=50)
def test_statements_varyinguntilcondition_instantiation(instance):
    assert isinstance(instance, statements_VaryingUntilCondition)

@given(instance=cobol_statements_Release_strategy)
@settings(max_examples=50)
def test_cobol_statements_release_instantiation(instance):
    assert isinstance(instance, cobol_statements_Release)

@given(instance=statements_PerformFixedTimes_strategy)
@settings(max_examples=50)
def test_statements_performfixedtimes_instantiation(instance):
    assert isinstance(instance, statements_PerformFixedTimes)

@given(instance=statements_FileIOStatement_strategy)
@settings(max_examples=50)
def test_statements_fileiostatement_instantiation(instance):
    assert isinstance(instance, statements_FileIOStatement)

@given(instance=KeyDescriptor_strategy)
@settings(max_examples=50)
def test_keydescriptor_instantiation(instance):
    assert isinstance(instance, KeyDescriptor)

@given(instance=OutputDirective_strategy)
@settings(max_examples=50)
def test_outputdirective_instantiation(instance):
    assert isinstance(instance, OutputDirective)

@given(instance=InputDirective_strategy)
@settings(max_examples=50)
def test_inputdirective_instantiation(instance):
    assert isinstance(instance, InputDirective)

@given(instance=statements_PerformProcedure_strategy)
@settings(max_examples=50)
def test_statements_performprocedure_instantiation(instance):
    assert isinstance(instance, statements_PerformProcedure)

@given(instance=cobol_statements_PerformProcedureFixedTimes_strategy)
@settings(max_examples=50)
def test_cobol_statements_performprocedurefixedtimes_instantiation(instance):
    assert isinstance(instance, cobol_statements_PerformProcedureFixedTimes)

@given(instance=cobol_statements_FileIOStatement_strategy)
@settings(max_examples=50)
def test_cobol_statements_fileiostatement_instantiation(instance):
    assert isinstance(instance, cobol_statements_FileIOStatement)

@given(instance=statements_PerformNestedStatement_strategy)
@settings(max_examples=50)
def test_statements_performnestedstatement_instantiation(instance):
    assert isinstance(instance, statements_PerformNestedStatement)

@given(instance=cobol_statements_PerformNestedStatementFixedTimes_strategy)
@settings(max_examples=50)
def test_cobol_statements_performnestedstatementfixedtimes_instantiation(instance):
    assert isinstance(instance, cobol_statements_PerformNestedStatementFixedTimes)

@given(instance=AfterUntilCondition_strategy)
@settings(max_examples=50)
def test_afteruntilcondition_instantiation(instance):
    assert isinstance(instance, AfterUntilCondition)

@given(instance=statements_PerformUntilCondition_strategy)
@settings(max_examples=50)
def test_statements_performuntilcondition_instantiation(instance):
    assert isinstance(instance, statements_PerformUntilCondition)

@given(instance=cobol_statements_PerformNestedStatementUntilCondition_strategy)
@settings(max_examples=50)
def test_cobol_statements_performnestedstatementuntilcondition_instantiation(instance):
    assert isinstance(instance, cobol_statements_PerformNestedStatementUntilCondition)

@given(instance=cobol_statements_PerformProcedureUntilCondition_strategy)
@settings(max_examples=50)
def test_cobol_statements_performprocedureuntilcondition_instantiation(instance):
    assert isinstance(instance, cobol_statements_PerformProcedureUntilCondition)

@given(instance=TallyingIn_strategy)
@settings(max_examples=50)
def test_tallyingin_instantiation(instance):
    assert isinstance(instance, TallyingIn)

@given(instance=cobol_statements_SwitchStatus_strategy)
@settings(max_examples=50)
def test_cobol_statements_switchstatus_instantiation(instance):
    assert isinstance(instance, cobol_statements_SwitchStatus)



@given(instance=cobol_statements_SwitchStatus_strategy)
def test_cobol_statements_switchstatus_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Write_strategy)
@settings(max_examples=50)
def test_write_instantiation(instance):
    assert isinstance(instance, Write)

@given(instance=cobol_statements_Rewrite_strategy)
@settings(max_examples=50)
def test_cobol_statements_rewrite_instantiation(instance):
    assert isinstance(instance, cobol_statements_Rewrite)

@given(instance=MnemonicNameReference_strategy)
@settings(max_examples=50)
def test_mnemonicnamereference_instantiation(instance):
    assert isinstance(instance, MnemonicNameReference)

@given(instance=IntegerLiteral_strategy)
@settings(max_examples=50)
def test_integerliteral_instantiation(instance):
    assert isinstance(instance, IntegerLiteral)

@given(instance=SearchStatement_strategy)
@settings(max_examples=50)
def test_searchstatement_instantiation(instance):
    assert isinstance(instance, SearchStatement)

@given(instance=cobol_statements_BinarySearch_strategy)
@settings(max_examples=50)
def test_cobol_statements_binarysearch_instantiation(instance):
    assert isinstance(instance, cobol_statements_BinarySearch)

@given(instance=cobol_statements_SerialSearch_strategy)
@settings(max_examples=50)
def test_cobol_statements_serialsearch_instantiation(instance):
    assert isinstance(instance, cobol_statements_SerialSearch)

@given(instance=NormalEvaluateCase_strategy)
@settings(max_examples=50)
def test_normalevaluatecase_instantiation(instance):
    assert isinstance(instance, NormalEvaluateCase)

@given(instance=Replacement_strategy)
@settings(max_examples=50)
def test_replacement_instantiation(instance):
    assert isinstance(instance, Replacement)

@given(instance=cobol_strings_AnyCharacterBySpecificCharacter_strategy)
@settings(max_examples=50)
def test_cobol_strings_anycharacterbyspecificcharacter_instantiation(instance):
    assert isinstance(instance, cobol_strings_AnyCharacterBySpecificCharacter)

@given(instance=cobol_strings_SpecificCharacterBySpecificCharacter_strategy)
@settings(max_examples=50)
def test_cobol_strings_specificcharacterbyspecificcharacter_instantiation(instance):
    assert isinstance(instance, cobol_strings_SpecificCharacterBySpecificCharacter)

@given(instance=cobol_statements_Initialize_strategy)
@settings(max_examples=50)
def test_cobol_statements_initialize_instantiation(instance):
    assert isinstance(instance, cobol_statements_Initialize)

@given(instance=cobol_statements_Inspect_strategy)
@settings(max_examples=50)
def test_cobol_statements_inspect_instantiation(instance):
    assert isinstance(instance, cobol_statements_Inspect)

@given(instance=cobol_statements_Replace_strategy)
@settings(max_examples=50)
def test_cobol_statements_replace_instantiation(instance):
    assert isinstance(instance, cobol_statements_Replace)



@given(instance=cobol_statements_Replace_strategy)
def test_cobol_statements_replace_replaceSwitch_setter(instance):
    original = instance.replaceSwitch
    instance.replaceSwitch = original
    assert instance.replaceSwitch == original

@given(instance=NestedStatement_strategy)
@settings(max_examples=50)
def test_nestedstatement_instantiation(instance):
    assert isinstance(instance, NestedStatement)

@given(instance=cobol_handlers_Handler_strategy)
@settings(max_examples=50)
def test_cobol_handlers_handler_instantiation(instance):
    assert isinstance(instance, cobol_handlers_Handler)

@given(instance=cobol_statements_EvaluateCase_strategy)
@settings(max_examples=50)
def test_cobol_statements_evaluatecase_instantiation(instance):
    assert isinstance(instance, cobol_statements_EvaluateCase)

@given(instance=ExpressionList_strategy)
@settings(max_examples=50)
def test_expressionlist_instantiation(instance):
    assert isinstance(instance, ExpressionList)

@given(instance=EvaluateCase_strategy)
@settings(max_examples=50)
def test_evaluatecase_instantiation(instance):
    assert isinstance(instance, EvaluateCase)

@given(instance=cobol_statements_OtherEvaluateCase_strategy)
@settings(max_examples=50)
def test_cobol_statements_otherevaluatecase_instantiation(instance):
    assert isinstance(instance, cobol_statements_OtherEvaluateCase)

@given(instance=cobol_statements_NormalEvaluateCase_strategy)
@settings(max_examples=50)
def test_cobol_statements_normalevaluatecase_instantiation(instance):
    assert isinstance(instance, cobol_statements_NormalEvaluateCase)

@given(instance=cobol_statements_Evaluate_strategy)
@settings(max_examples=50)
def test_cobol_statements_evaluate_instantiation(instance):
    assert isinstance(instance, cobol_statements_Evaluate)

@given(instance=SplittedString_strategy)
@settings(max_examples=50)
def test_splittedstring_instantiation(instance):
    assert isinstance(instance, SplittedString)

@given(instance=SetStatement_strategy)
@settings(max_examples=50)
def test_setstatement_instantiation(instance):
    assert isinstance(instance, SetStatement)

@given(instance=cobol_statements_Set_strategy)
@settings(max_examples=50)
def test_cobol_statements_set_instantiation(instance):
    assert isinstance(instance, cobol_statements_Set)

@given(instance=cobol_statements_SetSwitches_strategy)
@settings(max_examples=50)
def test_cobol_statements_setswitches_instantiation(instance):
    assert isinstance(instance, cobol_statements_SetSwitches)

@given(instance=cobol_statements_SetStatement_strategy)
@settings(max_examples=50)
def test_cobol_statements_setstatement_instantiation(instance):
    assert isinstance(instance, cobol_statements_SetStatement)

@given(instance=FileNameReference_strategy)
@settings(max_examples=50)
def test_filenamereference_instantiation(instance):
    assert isinstance(instance, FileNameReference)

@given(instance=Handler_strategy)
@settings(max_examples=50)
def test_handler_instantiation(instance):
    assert isinstance(instance, Handler)

@given(instance=cobol_handlers_OnException_strategy)
@settings(max_examples=50)
def test_cobol_handlers_onexception_instantiation(instance):
    assert isinstance(instance, cobol_handlers_OnException)

@given(instance=cobol_handlers_AtEndOfPage_strategy)
@settings(max_examples=50)
def test_cobol_handlers_atendofpage_instantiation(instance):
    assert isinstance(instance, cobol_handlers_AtEndOfPage)



@given(instance=cobol_handlers_AtEndOfPage_strategy)
def test_cobol_handlers_atendofpage_eop_setter(instance):
    original = instance.eop
    instance.eop = original
    assert instance.eop == original

@given(instance=cobol_handlers_OnSizeError_strategy)
@settings(max_examples=50)
def test_cobol_handlers_onsizeerror_instantiation(instance):
    assert isinstance(instance, cobol_handlers_OnSizeError)

@given(instance=cobol_handlers_AtEnd_strategy)
@settings(max_examples=50)
def test_cobol_handlers_atend_instantiation(instance):
    assert isinstance(instance, cobol_handlers_AtEnd)

@given(instance=cobol_handlers_NotErrorHandler_strategy)
@settings(max_examples=50)
def test_cobol_handlers_noterrorhandler_instantiation(instance):
    assert isinstance(instance, cobol_handlers_NotErrorHandler)

@given(instance=cobol_handlers_InvalidKey_strategy)
@settings(max_examples=50)
def test_cobol_handlers_invalidkey_instantiation(instance):
    assert isinstance(instance, cobol_handlers_InvalidKey)

@given(instance=cobol_handlers_OnOverflow_strategy)
@settings(max_examples=50)
def test_cobol_handlers_onoverflow_instantiation(instance):
    assert isinstance(instance, cobol_handlers_OnOverflow)

@given(instance=cobol_statements_ErrorHandled_strategy)
@settings(max_examples=50)
def test_cobol_statements_errorhandled_instantiation(instance):
    assert isinstance(instance, cobol_statements_ErrorHandled)

@given(instance=cobol_statements_Execute_strategy)
@settings(max_examples=50)
def test_cobol_statements_execute_instantiation(instance):
    assert isinstance(instance, cobol_statements_Execute)



@given(instance=cobol_statements_Execute_strategy)
def test_cobol_statements_execute_water_setter(instance):
    original = instance.water
    instance.water = original
    assert instance.water == original

@given(instance=functions_Argumentable_strategy)
@settings(max_examples=50)
def test_functions_argumentable_instantiation(instance):
    assert isinstance(instance, functions_Argumentable)

@given(instance=cobol_statements_Cancel_strategy)
@settings(max_examples=50)
def test_cobol_statements_cancel_instantiation(instance):
    assert isinstance(instance, cobol_statements_Cancel)

@given(instance=statements_IOStatement_strategy)
@settings(max_examples=50)
def test_statements_iostatement_instantiation(instance):
    assert isinstance(instance, statements_IOStatement)

@given(instance=ConcatenatingStrings_strategy)
@settings(max_examples=50)
def test_concatenatingstrings_instantiation(instance):
    assert isinstance(instance, ConcatenatingStrings)

@given(instance=IndexNameReference_strategy)
@settings(max_examples=50)
def test_indexnamereference_instantiation(instance):
    assert isinstance(instance, IndexNameReference)

@given(instance=cobol_statements_SetIndexName_strategy)
@settings(max_examples=50)
def test_cobol_statements_setindexname_instantiation(instance):
    assert isinstance(instance, cobol_statements_SetIndexName)



@given(instance=cobol_statements_SetIndexName_strategy)
def test_cobol_statements_setindexname_adjust_setter(instance):
    original = instance.adjust
    instance.adjust = original
    assert instance.adjust == original

@given(instance=SwitchStatus_strategy)
@settings(max_examples=50)
def test_switchstatus_instantiation(instance):
    assert isinstance(instance, SwitchStatus)

@given(instance=PrimaryOperand_strategy)
@settings(max_examples=50)
def test_primaryoperand_instantiation(instance):
    assert isinstance(instance, PrimaryOperand)

@given(instance=cobol_registers_Register_strategy)
@settings(max_examples=50)
def test_cobol_registers_register_instantiation(instance):
    assert isinstance(instance, cobol_registers_Register)

@given(instance=cobol_statements_Move_strategy)
@settings(max_examples=50)
def test_cobol_statements_move_instantiation(instance):
    assert isinstance(instance, cobol_statements_Move)



@given(instance=cobol_statements_Move_strategy)
def test_cobol_statements_move_corresponding_setter(instance):
    original = instance.corresponding
    instance.corresponding = original
    assert instance.corresponding == original

@given(instance=cobol_statements_NestedStatement_strategy)
@settings(max_examples=50)
def test_cobol_statements_nestedstatement_instantiation(instance):
    assert isinstance(instance, cobol_statements_NestedStatement)

@given(instance=Jump_strategy)
@settings(max_examples=50)
def test_jump_instantiation(instance):
    assert isinstance(instance, Jump)

@given(instance=cobol_statements_GoTo_strategy)
@settings(max_examples=50)
def test_cobol_statements_goto_instantiation(instance):
    assert isinstance(instance, cobol_statements_GoTo)

@given(instance=cobol_statements_GoBack_strategy)
@settings(max_examples=50)
def test_cobol_statements_goback_instantiation(instance):
    assert isinstance(instance, cobol_statements_GoBack)

@given(instance=cobol_statements_Continue_strategy)
@settings(max_examples=50)
def test_cobol_statements_continue_instantiation(instance):
    assert isinstance(instance, cobol_statements_Continue)

@given(instance=cobol_statements_NextSentence_strategy)
@settings(max_examples=50)
def test_cobol_statements_nextsentence_instantiation(instance):
    assert isinstance(instance, cobol_statements_NextSentence)

@given(instance=cobol_statements_Jump_strategy)
@settings(max_examples=50)
def test_cobol_statements_jump_instantiation(instance):
    assert isinstance(instance, cobol_statements_Jump)

@given(instance=ProcedureRangeLabel_strategy)
@settings(max_examples=50)
def test_procedurerangelabel_instantiation(instance):
    assert isinstance(instance, ProcedureRangeLabel)

@given(instance=cobol_labels_ProcedureRange_strategy)
@settings(max_examples=50)
def test_cobol_labels_procedurerange_instantiation(instance):
    assert isinstance(instance, cobol_labels_ProcedureRange)

@given(instance=cobol_labels_ProcedureRangeChild_strategy)
@settings(max_examples=50)
def test_cobol_labels_procedurerangechild_instantiation(instance):
    assert isinstance(instance, cobol_labels_ProcedureRangeChild)

@given(instance=Perform_strategy)
@settings(max_examples=50)
def test_perform_instantiation(instance):
    assert isinstance(instance, Perform)

@given(instance=cobol_statements_PerformFixedTimes_strategy)
@settings(max_examples=50)
def test_cobol_statements_performfixedtimes_instantiation(instance):
    assert isinstance(instance, cobol_statements_PerformFixedTimes)

@given(instance=cobol_statements_PerformProcedure_strategy)
@settings(max_examples=50)
def test_cobol_statements_performprocedure_instantiation(instance):
    assert isinstance(instance, cobol_statements_PerformProcedure)

@given(instance=AssignmentExpression_strategy)
@settings(max_examples=50)
def test_assignmentexpression_instantiation(instance):
    assert isinstance(instance, AssignmentExpression)

@given(instance=Environment_strategy)
@settings(max_examples=50)
def test_environment_instantiation(instance):
    assert isinstance(instance, Environment)

@given(instance=cobol_environments_UPSI_strategy)
@settings(max_examples=50)
def test_cobol_environments_upsi_instantiation(instance):
    assert isinstance(instance, cobol_environments_UPSI)



@given(instance=cobol_environments_UPSI_strategy)
def test_cobol_environments_upsi_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_environments_SystemDevice_strategy)
@settings(max_examples=50)
def test_cobol_environments_systemdevice_instantiation(instance):
    assert isinstance(instance, cobol_environments_SystemDevice)

@given(instance=cobol_statements_Display_strategy)
@settings(max_examples=50)
def test_cobol_statements_display_instantiation(instance):
    assert isinstance(instance, cobol_statements_Display)

@given(instance=StopLabel_strategy)
@settings(max_examples=50)
def test_stoplabel_instantiation(instance):
    assert isinstance(instance, StopLabel)

@given(instance=cobol_labels_Run_strategy)
@settings(max_examples=50)
def test_cobol_labels_run_instantiation(instance):
    assert isinstance(instance, cobol_labels_Run)

@given(instance=cobol_statements_Stop_strategy)
@settings(max_examples=50)
def test_cobol_statements_stop_instantiation(instance):
    assert isinstance(instance, cobol_statements_Stop)

@given(instance=cobol_statements_Conditional_strategy)
@settings(max_examples=50)
def test_cobol_statements_conditional_instantiation(instance):
    assert isinstance(instance, cobol_statements_Conditional)

@given(instance=statements_Conditional_strategy)
@settings(max_examples=50)
def test_statements_conditional_instantiation(instance):
    assert isinstance(instance, statements_Conditional)

@given(instance=cobol_statements_Exit_strategy)
@settings(max_examples=50)
def test_cobol_statements_exit_instantiation(instance):
    assert isinstance(instance, cobol_statements_Exit)



@given(instance=cobol_statements_Exit_strategy)
def test_cobol_statements_exit_exitLabel_setter(instance):
    original = instance.exitLabel
    instance.exitLabel = original
    assert instance.exitLabel == original

@given(instance=cobol_statements_Statement_strategy)
@settings(max_examples=50)
def test_cobol_statements_statement_instantiation(instance):
    assert isinstance(instance, cobol_statements_Statement)



@given(instance=cobol_statements_Statement_strategy)
def test_cobol_statements_statement_endVerb_setter(instance):
    original = instance.endVerb
    instance.endVerb = original
    assert instance.endVerb == original

@given(instance=cobol_operands_Operand_strategy)
@settings(max_examples=50)
def test_cobol_operands_operand_instantiation(instance):
    assert isinstance(instance, cobol_operands_Operand)

@given(instance=ReplacementOperand_strategy)
@settings(max_examples=50)
def test_replacementoperand_instantiation(instance):
    assert isinstance(instance, ReplacementOperand)

@given(instance=cobol_operands_Encoding_strategy)
@settings(max_examples=50)
def test_cobol_operands_encoding_instantiation(instance):
    assert isinstance(instance, cobol_operands_Encoding)



@given(instance=cobol_operands_Encoding_strategy)
def test_cobol_operands_encoding_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Operand_strategy)
@settings(max_examples=50)
def test_operand_instantiation(instance):
    assert isinstance(instance, Operand)

@given(instance=cobol_operands_ArithmeticOperand_strategy)
@settings(max_examples=50)
def test_cobol_operands_arithmeticoperand_instantiation(instance):
    assert isinstance(instance, cobol_operands_ArithmeticOperand)

@given(instance=cobol_operands_ReplacementOperand_strategy)
@settings(max_examples=50)
def test_cobol_operands_replacementoperand_instantiation(instance):
    assert isinstance(instance, cobol_operands_ReplacementOperand)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=statements_NestedStatement_strategy)
@settings(max_examples=50)
def test_statements_nestedstatement_instantiation(instance):
    assert isinstance(instance, statements_NestedStatement)

@given(instance=cobol_statements_Condition_strategy)
@settings(max_examples=50)
def test_cobol_statements_condition_instantiation(instance):
    assert isinstance(instance, cobol_statements_Condition)

@given(instance=statements_Perform_strategy)
@settings(max_examples=50)
def test_statements_perform_instantiation(instance):
    assert isinstance(instance, statements_Perform)

@given(instance=cobol_statements_PerformUntilCondition_strategy)
@settings(max_examples=50)
def test_cobol_statements_performuntilcondition_instantiation(instance):
    assert isinstance(instance, cobol_statements_PerformUntilCondition)



@given(instance=cobol_statements_PerformUntilCondition_strategy)
def test_cobol_statements_performuntilcondition_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=cobol_statements_PerformNestedStatement_strategy)
@settings(max_examples=50)
def test_cobol_statements_performnestedstatement_instantiation(instance):
    assert isinstance(instance, cobol_statements_PerformNestedStatement)

@given(instance=cobol_statements_Perform_strategy)
@settings(max_examples=50)
def test_cobol_statements_perform_instantiation(instance):
    assert isinstance(instance, cobol_statements_Perform)

@given(instance=ArithmeticStatement_strategy)
@settings(max_examples=50)
def test_arithmeticstatement_instantiation(instance):
    assert isinstance(instance, ArithmeticStatement)

@given(instance=cobol_statements_Divide_strategy)
@settings(max_examples=50)
def test_cobol_statements_divide_instantiation(instance):
    assert isinstance(instance, cobol_statements_Divide)

@given(instance=cobol_statements_Multiply_strategy)
@settings(max_examples=50)
def test_cobol_statements_multiply_instantiation(instance):
    assert isinstance(instance, cobol_statements_Multiply)

@given(instance=cobol_statements_Subtract_strategy)
@settings(max_examples=50)
def test_cobol_statements_subtract_instantiation(instance):
    assert isinstance(instance, cobol_statements_Subtract)

@given(instance=cobol_statements_Add_strategy)
@settings(max_examples=50)
def test_cobol_statements_add_instantiation(instance):
    assert isinstance(instance, cobol_statements_Add)

@given(instance=statements_ErrorHandled_strategy)
@settings(max_examples=50)
def test_statements_errorhandled_instantiation(instance):
    assert isinstance(instance, statements_ErrorHandled)

@given(instance=cobol_statements_Return_strategy)
@settings(max_examples=50)
def test_cobol_statements_return_instantiation(instance):
    assert isinstance(instance, cobol_statements_Return)

@given(instance=cobol_statements_ArithmeticStatement_strategy)
@settings(max_examples=50)
def test_cobol_statements_arithmeticstatement_instantiation(instance):
    assert isinstance(instance, cobol_statements_ArithmeticStatement)



@given(instance=cobol_statements_ArithmeticStatement_strategy)
def test_cobol_statements_arithmeticstatement_corresponding_setter(instance):
    original = instance.corresponding
    instance.corresponding = original
    assert instance.corresponding == original

@given(instance=cobol_statements_Start_strategy)
@settings(max_examples=50)
def test_cobol_statements_start_instantiation(instance):
    assert isinstance(instance, cobol_statements_Start)

@given(instance=cobol_statements_SearchStatement_strategy)
@settings(max_examples=50)
def test_cobol_statements_searchstatement_instantiation(instance):
    assert isinstance(instance, cobol_statements_SearchStatement)

@given(instance=cobol_statements_Delete_strategy)
@settings(max_examples=50)
def test_cobol_statements_delete_instantiation(instance):
    assert isinstance(instance, cobol_statements_Delete)

@given(instance=cobol_statements_Read_strategy)
@settings(max_examples=50)
def test_cobol_statements_read_instantiation(instance):
    assert isinstance(instance, cobol_statements_Read)

@given(instance=cobol_statements_Unstring_strategy)
@settings(max_examples=50)
def test_cobol_statements_unstring_instantiation(instance):
    assert isinstance(instance, cobol_statements_Unstring)

@given(instance=cobol_statements_Write_strategy)
@settings(max_examples=50)
def test_cobol_statements_write_instantiation(instance):
    assert isinstance(instance, cobol_statements_Write)

@given(instance=cobol_statements_Call_strategy)
@settings(max_examples=50)
def test_cobol_statements_call_instantiation(instance):
    assert isinstance(instance, cobol_statements_Call)

@given(instance=cobol_statements_String_strategy)
@settings(max_examples=50)
def test_cobol_statements_string_instantiation(instance):
    assert isinstance(instance, cobol_statements_String)

@given(instance=cobol_statements_Compute_strategy)
@settings(max_examples=50)
def test_cobol_statements_compute_instantiation(instance):
    assert isinstance(instance, cobol_statements_Compute)

@given(instance=ConstantLiteral_strategy)
@settings(max_examples=50)
def test_constantliteral_instantiation(instance):
    assert isinstance(instance, ConstantLiteral)

@given(instance=FigurativeConstantLiteral_strategy)
@settings(max_examples=50)
def test_figurativeconstantliteral_instantiation(instance):
    assert isinstance(instance, FigurativeConstantLiteral)

@given(instance=cobol_literals_AllLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_allliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_AllLiteral)

@given(instance=DecimalLiteral_strategy)
@settings(max_examples=50)
def test_decimalliteral_instantiation(instance):
    assert isinstance(instance, DecimalLiteral)

@given(instance=cobol_literals_FloatingDecimalLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_floatingdecimalliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_FloatingDecimalLiteral)

@given(instance=NumericLiteral_strategy)
@settings(max_examples=50)
def test_numericliteral_instantiation(instance):
    assert isinstance(instance, NumericLiteral)

@given(instance=cobol_literals_DecimalLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_decimalliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_DecimalLiteral)



@given(instance=cobol_literals_DecimalLiteral_strategy)
def test_cobol_literals_decimalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=water_IOControlParagraphWater_strategy)
@settings(max_examples=50)
def test_water_iocontrolparagraphwater_instantiation(instance):
    assert isinstance(instance, water_IOControlParagraphWater)

@given(instance=water_FileDescriptorWater_strategy)
@settings(max_examples=50)
def test_water_filedescriptorwater_instantiation(instance):
    assert isinstance(instance, water_FileDescriptorWater)

@given(instance=water_ObjectComputerParagraphWater_strategy)
@settings(max_examples=50)
def test_water_objectcomputerparagraphwater_instantiation(instance):
    assert isinstance(instance, water_ObjectComputerParagraphWater)

@given(instance=literals_NumericLiteral_strategy)
@settings(max_examples=50)
def test_literals_numericliteral_instantiation(instance):
    assert isinstance(instance, literals_NumericLiteral)

@given(instance=cobol_literals_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_integerliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_IntegerLiteral)



@given(instance=cobol_literals_IntegerLiteral_strategy)
def test_cobol_literals_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=cobol_literals_FigurativeConstantLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_figurativeconstantliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_FigurativeConstantLiteral)

@given(instance=cobol_literals_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_booleanliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_BooleanLiteral)



@given(instance=cobol_literals_BooleanLiteral_strategy)
def test_cobol_literals_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_literals_AlphanumericLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_alphanumericliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_AlphanumericLiteral)



@given(instance=cobol_literals_AlphanumericLiteral_strategy)
def test_cobol_literals_alphanumericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Division_strategy)
@settings(max_examples=50)
def test_division_instantiation(instance):
    assert isinstance(instance, Division)

@given(instance=cobol_divisions_EnvironmentDivision_strategy)
@settings(max_examples=50)
def test_cobol_divisions_environmentdivision_instantiation(instance):
    assert isinstance(instance, cobol_divisions_EnvironmentDivision)

@given(instance=cobol_divisions_DataDivision_strategy)
@settings(max_examples=50)
def test_cobol_divisions_datadivision_instantiation(instance):
    assert isinstance(instance, cobol_divisions_DataDivision)

@given(instance=StatementContainer_strategy)
@settings(max_examples=50)
def test_statementcontainer_instantiation(instance):
    assert isinstance(instance, StatementContainer)

@given(instance=Paragraph_strategy)
@settings(max_examples=50)
def test_paragraph_instantiation(instance):
    assert isinstance(instance, Paragraph)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=cobol_sections_DataDivisionSection_strategy)
@settings(max_examples=50)
def test_cobol_sections_datadivisionsection_instantiation(instance):
    assert isinstance(instance, cobol_sections_DataDivisionSection)

@given(instance=cobol_sections_EnvironmentDivisionSection_strategy)
@settings(max_examples=50)
def test_cobol_sections_environmentdivisionsection_instantiation(instance):
    assert isinstance(instance, cobol_sections_EnvironmentDivisionSection)

@given(instance=CobolRoot_strategy)
@settings(max_examples=50)
def test_cobolroot_instantiation(instance):
    assert isinstance(instance, CobolRoot)

@given(instance=cobol_containers_EmptyModel_strategy)
@settings(max_examples=50)
def test_cobol_containers_emptymodel_instantiation(instance):
    assert isinstance(instance, cobol_containers_EmptyModel)

@given(instance=cobol_containers_CobolRoot_strategy)
@settings(max_examples=50)
def test_cobol_containers_cobolroot_instantiation(instance):
    assert isinstance(instance, cobol_containers_CobolRoot)

@given(instance=ProcedureDivision_strategy)
@settings(max_examples=50)
def test_proceduredivision_instantiation(instance):
    assert isinstance(instance, ProcedureDivision)

@given(instance=DataDivision_strategy)
@settings(max_examples=50)
def test_datadivision_instantiation(instance):
    assert isinstance(instance, DataDivision)

@given(instance=EnvironmentDivision_strategy)
@settings(max_examples=50)
def test_environmentdivision_instantiation(instance):
    assert isinstance(instance, EnvironmentDivision)

@given(instance=water_InvokeStatementWater_strategy)
@settings(max_examples=50)
def test_water_invokestatementwater_instantiation(instance):
    assert isinstance(instance, water_InvokeStatementWater)

@given(instance=operands_PrimaryOperand_strategy)
@settings(max_examples=50)
def test_operands_primaryoperand_instantiation(instance):
    assert isinstance(instance, operands_PrimaryOperand)

@given(instance=water_CICSStatementWater_strategy)
@settings(max_examples=50)
def test_water_cicsstatementwater_instantiation(instance):
    assert isinstance(instance, water_CICSStatementWater)

@given(instance=water_SpecialNamesParagraphWater_strategy)
@settings(max_examples=50)
def test_water_specialnamesparagraphwater_instantiation(instance):
    assert isinstance(instance, water_SpecialNamesParagraphWater)

@given(instance=water_SelectStatementWater_strategy)
@settings(max_examples=50)
def test_water_selectstatementwater_instantiation(instance):
    assert isinstance(instance, water_SelectStatementWater)

@given(instance=cobol_identifiers_Identifier_strategy)
@settings(max_examples=50)
def test_cobol_identifiers_identifier_instantiation(instance):
    assert isinstance(instance, cobol_identifiers_Identifier)

@given(instance=Declaratives_strategy)
@settings(max_examples=50)
def test_declaratives_instantiation(instance):
    assert isinstance(instance, Declaratives)

@given(instance=parameters_Parametrizable_strategy)
@settings(max_examples=50)
def test_parameters_parametrizable_instantiation(instance):
    assert isinstance(instance, parameters_Parametrizable)

@given(instance=cobol_statements_Entry_strategy)
@settings(max_examples=50)
def test_cobol_statements_entry_instantiation(instance):
    assert isinstance(instance, cobol_statements_Entry)

@given(instance=water_IncompleteElement_strategy)
@settings(max_examples=50)
def test_water_incompleteelement_instantiation(instance):
    assert isinstance(instance, water_IncompleteElement)

@given(instance=cobol_files_FileName_strategy)
@settings(max_examples=50)
def test_cobol_files_filename_instantiation(instance):
    assert isinstance(instance, cobol_files_FileName)



@given(instance=cobol_files_FileName_strategy)
def test_cobol_files_filename_fileDescriptor_setter(instance):
    original = instance.fileDescriptor
    instance.fileDescriptor = original
    assert instance.fileDescriptor == original

@given(instance=cobol_statements_Merge_strategy)
@settings(max_examples=50)
def test_cobol_statements_merge_instantiation(instance):
    assert isinstance(instance, cobol_statements_Merge)

@given(instance=cobol_statements_Accept_strategy)
@settings(max_examples=50)
def test_cobol_statements_accept_instantiation(instance):
    assert isinstance(instance, cobol_statements_Accept)

@given(instance=cobol_tables_Table_strategy)
@settings(max_examples=50)
def test_cobol_tables_table_instantiation(instance):
    assert isinstance(instance, cobol_tables_Table)

@given(instance=cobol_statements_Sort_strategy)
@settings(max_examples=50)
def test_cobol_statements_sort_instantiation(instance):
    assert isinstance(instance, cobol_statements_Sort)

@given(instance=cobol_statements_Close_strategy)
@settings(max_examples=50)
def test_cobol_statements_close_instantiation(instance):
    assert isinstance(instance, cobol_statements_Close)

@given(instance=cobol_statements_Open_strategy)
@settings(max_examples=50)
def test_cobol_statements_open_instantiation(instance):
    assert isinstance(instance, cobol_statements_Open)

@given(instance=cobol_dataitems_DataItem_strategy)
@settings(max_examples=50)
def test_cobol_dataitems_dataitem_instantiation(instance):
    assert isinstance(instance, cobol_dataitems_DataItem)



@given(instance=cobol_dataitems_DataItem_strategy)
def test_cobol_dataitems_dataitem_levelNumber_setter(instance):
    original = instance.levelNumber
    instance.levelNumber = original
    assert instance.levelNumber == original

@given(instance=divisions_Division_strategy)
@settings(max_examples=50)
def test_divisions_division_instantiation(instance):
    assert isinstance(instance, divisions_Division)

@given(instance=cobol_divisions_ProcedureDivision_strategy)
@settings(max_examples=50)
def test_cobol_divisions_proceduredivision_instantiation(instance):
    assert isinstance(instance, cobol_divisions_ProcedureDivision)

@given(instance=cobol_divisions_IdentificationDivision_strategy)
@settings(max_examples=50)
def test_cobol_divisions_identificationdivision_instantiation(instance):
    assert isinstance(instance, cobol_divisions_IdentificationDivision)



@given(instance=cobol_divisions_IdentificationDivision_strategy)
def test_cobol_divisions_identificationdivision_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=cobol_arithmetics_RangeExpression_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_rangeexpression_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_RangeExpression)

@given(instance=Equal_strategy)
@settings(max_examples=50)
def test_equal_instantiation(instance):
    assert isinstance(instance, Equal)

@given(instance=cobol_arithmetics_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_assignmentexpression_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_AssignmentExpression)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=UnaryArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_unaryarithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryArithmeticExpressionChild)

@given(instance=cobol_arithmetics_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_primaryexpression_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_PrimaryExpression)

@given(instance=PowerArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_powerarithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, PowerArithmeticExpressionChild)

@given(instance=cobol_arithmetics_UnaryArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_unaryarithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_UnaryArithmeticExpression)

@given(instance=cobol_arithmetics_UnaryArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_unaryarithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_UnaryArithmeticExpressionChild)

@given(instance=IdentificationDivision_strategy)
@settings(max_examples=50)
def test_identificationdivision_instantiation(instance):
    assert isinstance(instance, IdentificationDivision)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=cobol_divisions_Division_strategy)
@settings(max_examples=50)
def test_cobol_divisions_division_instantiation(instance):
    assert isinstance(instance, cobol_divisions_Division)

@given(instance=cobol_containers_CompilationUnit_strategy)
@settings(max_examples=50)
def test_cobol_containers_compilationunit_instantiation(instance):
    assert isinstance(instance, cobol_containers_CompilationUnit)

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=commons_NamedElement_strategy)
@settings(max_examples=50)
def test_commons_namedelement_instantiation(instance):
    assert isinstance(instance, commons_NamedElement)

@given(instance=cobol_specialnames_ConditionName_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_conditionname_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_ConditionName)

@given(instance=cobol_functions_FunctionCall_strategy)
@settings(max_examples=50)
def test_cobol_functions_functioncall_instantiation(instance):
    assert isinstance(instance, cobol_functions_FunctionCall)

@given(instance=cobol_tables_IndexName_strategy)
@settings(max_examples=50)
def test_cobol_tables_indexname_instantiation(instance):
    assert isinstance(instance, cobol_tables_IndexName)

@given(instance=containers_CobolRoot_strategy)
@settings(max_examples=50)
def test_containers_cobolroot_instantiation(instance):
    assert isinstance(instance, containers_CobolRoot)

@given(instance=cobol_containers_CompilationGroup_strategy)
@settings(max_examples=50)
def test_cobol_containers_compilationgroup_instantiation(instance):
    assert isinstance(instance, cobol_containers_CompilationGroup)

@given(instance=conditions_SimpleConditionChild_strategy)
@settings(max_examples=50)
def test_conditions_simpleconditionchild_instantiation(instance):
    assert isinstance(instance, conditions_SimpleConditionChild)

@given(instance=conditions_AbbreviatedRelationalExpressionChild_strategy)
@settings(max_examples=50)
def test_conditions_abbreviatedrelationalexpressionchild_instantiation(instance):
    assert isinstance(instance, conditions_AbbreviatedRelationalExpressionChild)

@given(instance=cobol_arithmetics_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_ArithmeticExpression)

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=cobol_arithmetics_NestedArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_nestedarithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_NestedArithmeticExpression)

@given(instance=cobol_arithmetics_RangeExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_rangeexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_RangeExpressionChild)

@given(instance=Through_strategy)
@settings(max_examples=50)
def test_through_instantiation(instance):
    assert isinstance(instance, Through)

@given(instance=ClassOperator_strategy)
@settings(max_examples=50)
def test_classoperator_instantiation(instance):
    assert isinstance(instance, ClassOperator)

@given(instance=SignOperator_strategy)
@settings(max_examples=50)
def test_signoperator_instantiation(instance):
    assert isinstance(instance, SignOperator)

@given(instance=MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, MultiplicativeOperator)

@given(instance=MultiplicativeArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_multiplicativearithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, MultiplicativeArithmeticExpressionChild)

@given(instance=cobol_arithmetics_PowerArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_powerarithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_PowerArithmeticExpression)

@given(instance=cobol_arithmetics_PowerArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_powerarithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_PowerArithmeticExpressionChild)

@given(instance=AdditiveOperator_strategy)
@settings(max_examples=50)
def test_additiveoperator_instantiation(instance):
    assert isinstance(instance, AdditiveOperator)

@given(instance=AdditiveArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_additivearithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, AdditiveArithmeticExpressionChild)

@given(instance=cobol_arithmetics_MultiplicativeArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_multiplicativearithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_MultiplicativeArithmeticExpression)

@given(instance=cobol_arithmetics_MultiplicativeArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_multiplicativearithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_MultiplicativeArithmeticExpressionChild)

@given(instance=RangeExpressionChild_strategy)
@settings(max_examples=50)
def test_rangeexpressionchild_instantiation(instance):
    assert isinstance(instance, RangeExpressionChild)

@given(instance=cobol_arithmetics_AdditiveArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_additivearithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_AdditiveArithmeticExpressionChild)

@given(instance=cobol_arithmetics_AdditiveArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol_arithmetics_additivearithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol_arithmetics_AdditiveArithmeticExpression)

@given(instance=NegatedAbbreviatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_negatedabbreviatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, NegatedAbbreviatedConditionalExpressionChild)

@given(instance=cobol_conditions_AbbreviatedRelationalExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_conditions_abbreviatedrelationalexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_conditions_AbbreviatedRelationalExpressionChild)

@given(instance=AbbreviatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_abbreviatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, AbbreviatedConditionalExpressionChild)

@given(instance=cobol_conditions_NegatedAbbreviatedConditionalExpression_strategy)
@settings(max_examples=50)
def test_cobol_conditions_negatedabbreviatedconditionalexpression_instantiation(instance):
    assert isinstance(instance, cobol_conditions_NegatedAbbreviatedConditionalExpression)

@given(instance=cobol_conditions_ExpressionList_strategy)
@settings(max_examples=50)
def test_cobol_conditions_expressionlist_instantiation(instance):
    assert isinstance(instance, cobol_conditions_ExpressionList)

@given(instance=AbbreviatedRelationalExpressionChild_strategy)
@settings(max_examples=50)
def test_abbreviatedrelationalexpressionchild_instantiation(instance):
    assert isinstance(instance, AbbreviatedRelationalExpressionChild)

@given(instance=cobol_conditions_NestedAbbreviatedConditionalExpression_strategy)
@settings(max_examples=50)
def test_cobol_conditions_nestedabbreviatedconditionalexpression_instantiation(instance):
    assert isinstance(instance, cobol_conditions_NestedAbbreviatedConditionalExpression)

@given(instance=cobol_conditions_AbbreviatedRelationalExpression_strategy)
@settings(max_examples=50)
def test_cobol_conditions_abbreviatedrelationalexpression_instantiation(instance):
    assert isinstance(instance, cobol_conditions_AbbreviatedRelationalExpression)

@given(instance=cobol_conditions_NegatedAbbreviatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_conditions_negatedabbreviatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_conditions_NegatedAbbreviatedConditionalExpressionChild)

@given(instance=NegatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_negatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, NegatedConditionalExpressionChild)

@given(instance=cobol_conditions_ClassCondition_strategy)
@settings(max_examples=50)
def test_cobol_conditions_classcondition_instantiation(instance):
    assert isinstance(instance, cobol_conditions_ClassCondition)

@given(instance=cobol_conditions_SignCondition_strategy)
@settings(max_examples=50)
def test_cobol_conditions_signcondition_instantiation(instance):
    assert isinstance(instance, cobol_conditions_SignCondition)

@given(instance=ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpressionChild)

@given(instance=cobol_conditions_AbbreviatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_conditions_abbreviatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_conditions_AbbreviatedConditionalExpressionChild)

@given(instance=cobol_conditions_AbbreviatedConditionalExpression_strategy)
@settings(max_examples=50)
def test_cobol_conditions_abbreviatedconditionalexpression_instantiation(instance):
    assert isinstance(instance, cobol_conditions_AbbreviatedConditionalExpression)

@given(instance=cobol_conditions_NegatedConditionalExpression_strategy)
@settings(max_examples=50)
def test_cobol_conditions_negatedconditionalexpression_instantiation(instance):
    assert isinstance(instance, cobol_conditions_NegatedConditionalExpression)

@given(instance=LogicalOperator_strategy)
@settings(max_examples=50)
def test_logicaloperator_instantiation(instance):
    assert isinstance(instance, LogicalOperator)

@given(instance=ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpressionChild)

@given(instance=cobol_conditions_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_cobol_conditions_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, cobol_conditions_ConditionalAndExpression)

@given(instance=cobol_conditions_ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_conditions_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_conditions_ConditionalAndExpressionChild)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=cobol_conditions_ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_conditions_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_conditions_ConditionalOrExpressionChild)

@given(instance=cobol_conditions_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_cobol_conditions_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, cobol_conditions_ConditionalOrExpression)

@given(instance=cobol_conditions_Condition_strategy)
@settings(max_examples=50)
def test_cobol_conditions_condition_instantiation(instance):
    assert isinstance(instance, cobol_conditions_Condition)

@given(instance=Is_strategy)
@settings(max_examples=50)
def test_is_instantiation(instance):
    assert isinstance(instance, Is)

@given(instance=RelationalOperator_strategy)
@settings(max_examples=50)
def test_relationaloperator_instantiation(instance):
    assert isinstance(instance, RelationalOperator)

@given(instance=SimpleConditionChild_strategy)
@settings(max_examples=50)
def test_simpleconditionchild_instantiation(instance):
    assert isinstance(instance, SimpleConditionChild)

@given(instance=cobol_conditions_NestedCondition_strategy)
@settings(max_examples=50)
def test_cobol_conditions_nestedcondition_instantiation(instance):
    assert isinstance(instance, cobol_conditions_NestedCondition)

@given(instance=cobol_conditions_RelationalExpression_strategy)
@settings(max_examples=50)
def test_cobol_conditions_relationalexpression_instantiation(instance):
    assert isinstance(instance, cobol_conditions_RelationalExpression)

@given(instance=cobol_conditions_SimpleConditionChild_strategy)
@settings(max_examples=50)
def test_cobol_conditions_simpleconditionchild_instantiation(instance):
    assert isinstance(instance, cobol_conditions_SimpleConditionChild)

@given(instance=cobol_conditions_NegatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol_conditions_negatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol_conditions_NegatedConditionalExpressionChild)

@given(instance=Negate_strategy)
@settings(max_examples=50)
def test_negate_instantiation(instance):
    assert isinstance(instance, Negate)

@given(instance=cobol_commons_Commentable_strategy)
@settings(max_examples=50)
def test_cobol_commons_commentable_instantiation(instance):
    assert isinstance(instance, cobol_commons_Commentable)

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=cobol_commons_URIableElement_strategy)
@settings(max_examples=50)
def test_cobol_commons_uriableelement_instantiation(instance):
    assert isinstance(instance, cobol_commons_URIableElement)



@given(instance=cobol_commons_URIableElement_strategy)
def test_cobol_commons_uriableelement_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=cobol_commons_LabellableElement_strategy)
@settings(max_examples=50)
def test_cobol_commons_labellableelement_instantiation(instance):
    assert isinstance(instance, cobol_commons_LabellableElement)



@given(instance=cobol_commons_LabellableElement_strategy)
def test_cobol_commons_labellableelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=cobol_commons_NamedElement_strategy)
@settings(max_examples=50)
def test_cobol_commons_namedelement_instantiation(instance):
    assert isinstance(instance, cobol_commons_NamedElement)



@given(instance=cobol_commons_NamedElement_strategy)
def test_cobol_commons_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataDivisionSection_strategy)
@settings(max_examples=50)
def test_datadivisionsection_instantiation(instance):
    assert isinstance(instance, DataDivisionSection)

@given(instance=cobol_sections_LinkageStorageSection_strategy)
@settings(max_examples=50)
def test_cobol_sections_linkagestoragesection_instantiation(instance):
    assert isinstance(instance, cobol_sections_LinkageStorageSection)

@given(instance=cobol_sections_LocalStorageSection_strategy)
@settings(max_examples=50)
def test_cobol_sections_localstoragesection_instantiation(instance):
    assert isinstance(instance, cobol_sections_LocalStorageSection)

@given(instance=cobol_sections_FileSection_strategy)
@settings(max_examples=50)
def test_cobol_sections_filesection_instantiation(instance):
    assert isinstance(instance, cobol_sections_FileSection)

@given(instance=cobol_sections_WorkingStorageSection_strategy)
@settings(max_examples=50)
def test_cobol_sections_workingstoragesection_instantiation(instance):
    assert isinstance(instance, cobol_sections_WorkingStorageSection)

@given(instance=operands_ArithmeticOperand_strategy)
@settings(max_examples=50)
def test_operands_arithmeticoperand_instantiation(instance):
    assert isinstance(instance, operands_ArithmeticOperand)

@given(instance=arithmetics_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_arithmetics_primaryexpression_instantiation(instance):
    assert isinstance(instance, arithmetics_PrimaryExpression)

@given(instance=operands_Operand_strategy)
@settings(max_examples=50)
def test_operands_operand_instantiation(instance):
    assert isinstance(instance, operands_Operand)

@given(instance=operands_ReplacementOperand_strategy)
@settings(max_examples=50)
def test_operands_replacementoperand_instantiation(instance):
    assert isinstance(instance, operands_ReplacementOperand)

@given(instance=cobol_operands_PrimaryOperand_strategy)
@settings(max_examples=50)
def test_cobol_operands_primaryoperand_instantiation(instance):
    assert isinstance(instance, cobol_operands_PrimaryOperand)

@given(instance=cobol_sentences_Sentence_strategy)
@settings(max_examples=50)
def test_cobol_sentences_sentence_instantiation(instance):
    assert isinstance(instance, cobol_sentences_Sentence)

@given(instance=cobol_sentences_ExecuteSentence_strategy)
@settings(max_examples=50)
def test_cobol_sentences_executesentence_instantiation(instance):
    assert isinstance(instance, cobol_sentences_ExecuteSentence)

@given(instance=sentences_StatementContainer_strategy)
@settings(max_examples=50)
def test_sentences_statementcontainer_instantiation(instance):
    assert isinstance(instance, sentences_StatementContainer)

@given(instance=cobol_sentences_UseSentence_strategy)
@settings(max_examples=50)
def test_cobol_sentences_usesentence_instantiation(instance):
    assert isinstance(instance, cobol_sentences_UseSentence)

@given(instance=Sentence_strategy)
@settings(max_examples=50)
def test_sentence_instantiation(instance):
    assert isinstance(instance, Sentence)

@given(instance=cobol_sentences_ExitProcedure_strategy)
@settings(max_examples=50)
def test_cobol_sentences_exitprocedure_instantiation(instance):
    assert isinstance(instance, cobol_sentences_ExitProcedure)

@given(instance=cobol_sentences_EntrySentence_strategy)
@settings(max_examples=50)
def test_cobol_sentences_entrysentence_instantiation(instance):
    assert isinstance(instance, cobol_sentences_EntrySentence)

@given(instance=cobol_sentences_AlteredGoTo_strategy)
@settings(max_examples=50)
def test_cobol_sentences_alteredgoto_instantiation(instance):
    assert isinstance(instance, cobol_sentences_AlteredGoTo)

@given(instance=cobol_sentences_EmptySentence_strategy)
@settings(max_examples=50)
def test_cobol_sentences_emptysentence_instantiation(instance):
    assert isinstance(instance, cobol_sentences_EmptySentence)

@given(instance=cobol_sentences_StatementContainer_strategy)
@settings(max_examples=50)
def test_cobol_sentences_statementcontainer_instantiation(instance):
    assert isinstance(instance, cobol_sentences_StatementContainer)

@given(instance=cobol_sections_DeclarativeSection_strategy)
@settings(max_examples=50)
def test_cobol_sections_declarativesection_instantiation(instance):
    assert isinstance(instance, cobol_sections_DeclarativeSection)

@given(instance=FileName_strategy)
@settings(max_examples=50)
def test_filename_instantiation(instance):
    assert isinstance(instance, FileName)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=cobol_references_ElementReference_strategy)
@settings(max_examples=50)
def test_cobol_references_elementreference_instantiation(instance):
    assert isinstance(instance, cobol_references_ElementReference)

@given(instance=ReferenceableElement_strategy)
@settings(max_examples=50)
def test_referenceableelement_instantiation(instance):
    assert isinstance(instance, ReferenceableElement)

@given(instance=cobol_specialnames_SpecialName_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_specialname_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_SpecialName)

@given(instance=cobol_parameters_Parameter_strategy)
@settings(max_examples=50)
def test_cobol_parameters_parameter_instantiation(instance):
    assert isinstance(instance, cobol_parameters_Parameter)

@given(instance=cobol_tables_AdditionalIndexName_strategy)
@settings(max_examples=50)
def test_cobol_tables_additionalindexname_instantiation(instance):
    assert isinstance(instance, cobol_tables_AdditionalIndexName)

@given(instance=cobol_references_ReferenceableElement_strategy)
@settings(max_examples=50)
def test_cobol_references_referenceableelement_instantiation(instance):
    assert isinstance(instance, cobol_references_ReferenceableElement)

@given(instance=cobol_references_Reference_strategy)
@settings(max_examples=50)
def test_cobol_references_reference_instantiation(instance):
    assert isinstance(instance, cobol_references_Reference)

@given(instance=cobol_paragraphs_DebuggingMode_strategy)
@settings(max_examples=50)
def test_cobol_paragraphs_debuggingmode_instantiation(instance):
    assert isinstance(instance, cobol_paragraphs_DebuggingMode)

@given(instance=SpecialNamesParagraphWater_strategy)
@settings(max_examples=50)
def test_specialnamesparagraphwater_instantiation(instance):
    assert isinstance(instance, SpecialNamesParagraphWater)

@given(instance=cobol_water_SpecialNamesClause_strategy)
@settings(max_examples=50)
def test_cobol_water_specialnamesclause_instantiation(instance):
    assert isinstance(instance, cobol_water_SpecialNamesClause)



@given(instance=cobol_water_SpecialNamesClause_strategy)
def test_cobol_water_specialnamesclause_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpecialNameStatement_strategy)
@settings(max_examples=50)
def test_specialnamestatement_instantiation(instance):
    assert isinstance(instance, SpecialNameStatement)

@given(instance=cobol_paragraphs_IOSectionParagraph_strategy)
@settings(max_examples=50)
def test_cobol_paragraphs_iosectionparagraph_instantiation(instance):
    assert isinstance(instance, cobol_paragraphs_IOSectionParagraph)

@given(instance=cobol_paragraphs_ConfigurationSectionParagraph_strategy)
@settings(max_examples=50)
def test_cobol_paragraphs_configurationsectionparagraph_instantiation(instance):
    assert isinstance(instance, cobol_paragraphs_ConfigurationSectionParagraph)

@given(instance=identifiers_IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifiers_identifierreference_instantiation(instance):
    assert isinstance(instance, identifiers_IdentifierReference)

@given(instance=cobol_references_Qualifiable_strategy)
@settings(max_examples=50)
def test_cobol_references_qualifiable_instantiation(instance):
    assert isinstance(instance, cobol_references_Qualifiable)

@given(instance=cobol_references_ConditionName_strategy)
@settings(max_examples=50)
def test_cobol_references_conditionname_instantiation(instance):
    assert isinstance(instance, cobol_references_ConditionName)

@given(instance=ElementReference_strategy)
@settings(max_examples=50)
def test_elementreference_instantiation(instance):
    assert isinstance(instance, ElementReference)

@given(instance=cobol_identifiers_Qualifier_strategy)
@settings(max_examples=50)
def test_cobol_identifiers_qualifier_instantiation(instance):
    assert isinstance(instance, cobol_identifiers_Qualifier)

@given(instance=cobol_references_AlphabetNameReference_strategy)
@settings(max_examples=50)
def test_cobol_references_alphabetnamereference_instantiation(instance):
    assert isinstance(instance, cobol_references_AlphabetNameReference)

@given(instance=IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifierreference_instantiation(instance):
    assert isinstance(instance, IdentifierReference)

@given(instance=cobol_references_IndexNameReference_strategy)
@settings(max_examples=50)
def test_cobol_references_indexnamereference_instantiation(instance):
    assert isinstance(instance, cobol_references_IndexNameReference)

@given(instance=references_IdentifierReferenceQualifier_strategy)
@settings(max_examples=50)
def test_references_identifierreferencequalifier_instantiation(instance):
    assert isinstance(instance, references_IdentifierReferenceQualifier)

@given(instance=cobol_references_DataNameReference_strategy)
@settings(max_examples=50)
def test_cobol_references_datanamereference_instantiation(instance):
    assert isinstance(instance, cobol_references_DataNameReference)

@given(instance=references_ConditionName_strategy)
@settings(max_examples=50)
def test_references_conditionname_instantiation(instance):
    assert isinstance(instance, references_ConditionName)

@given(instance=cobol_references_ConditionNameReference_strategy)
@settings(max_examples=50)
def test_cobol_references_conditionnamereference_instantiation(instance):
    assert isinstance(instance, cobol_references_ConditionNameReference)

@given(instance=references_Qualifiable_strategy)
@settings(max_examples=50)
def test_references_qualifiable_instantiation(instance):
    assert isinstance(instance, references_Qualifiable)

@given(instance=cobol_identifiers_LinageCounter_strategy)
@settings(max_examples=50)
def test_cobol_identifiers_linagecounter_instantiation(instance):
    assert isinstance(instance, cobol_identifiers_LinageCounter)

@given(instance=references_ElementReference_strategy)
@settings(max_examples=50)
def test_references_elementreference_instantiation(instance):
    assert isinstance(instance, references_ElementReference)

@given(instance=cobol_references_FileNameReference_strategy)
@settings(max_examples=50)
def test_cobol_references_filenamereference_instantiation(instance):
    assert isinstance(instance, cobol_references_FileNameReference)

@given(instance=cobol_specialnames_SymbolicCharacterStatement_strategy)
@settings(max_examples=50)
def test_cobol_specialnames_symboliccharacterstatement_instantiation(instance):
    assert isinstance(instance, cobol_specialnames_SymbolicCharacterStatement)

@given(instance=cobol_identifiers_IdentifierReference_strategy)
@settings(max_examples=50)
def test_cobol_identifiers_identifierreference_instantiation(instance):
    assert isinstance(instance, cobol_identifiers_IdentifierReference)

@given(instance=cobol_references_IdentifierReferenceQualifier_strategy)
@settings(max_examples=50)
def test_cobol_references_identifierreferencequalifier_instantiation(instance):
    assert isinstance(instance, cobol_references_IdentifierReferenceQualifier)

@given(instance=cobol_references_MnemonicNameReference_strategy)
@settings(max_examples=50)
def test_cobol_references_mnemonicnamereference_instantiation(instance):
    assert isinstance(instance, cobol_references_MnemonicNameReference)

@given(instance=cobol_references_SpecialNamesConditionNameReference_strategy)
@settings(max_examples=50)
def test_cobol_references_specialnamesconditionnamereference_instantiation(instance):
    assert isinstance(instance, cobol_references_SpecialNamesConditionNameReference)

@given(instance=GreaterThan_strategy)
@settings(max_examples=50)
def test_greaterthan_instantiation(instance):
    assert isinstance(instance, GreaterThan)

@given(instance=cobol_operators_GTPhrase_strategy)
@settings(max_examples=50)
def test_cobol_operators_gtphrase_instantiation(instance):
    assert isinstance(instance, cobol_operators_GTPhrase)

@given(instance=LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_lessthanorequal_instantiation(instance):
    assert isinstance(instance, LessThanOrEqual)

@given(instance=cobol_operators_LTEQSign_strategy)
@settings(max_examples=50)
def test_cobol_operators_lteqsign_instantiation(instance):
    assert isinstance(instance, cobol_operators_LTEQSign)

@given(instance=cobol_operators_LTEQPhrase_strategy)
@settings(max_examples=50)
def test_cobol_operators_lteqphrase_instantiation(instance):
    assert isinstance(instance, cobol_operators_LTEQPhrase)

@given(instance=LessThan_strategy)
@settings(max_examples=50)
def test_lessthan_instantiation(instance):
    assert isinstance(instance, LessThan)

@given(instance=cobol_operators_LTSign_strategy)
@settings(max_examples=50)
def test_cobol_operators_ltsign_instantiation(instance):
    assert isinstance(instance, cobol_operators_LTSign)

@given(instance=cobol_operators_LTPhrase_strategy)
@settings(max_examples=50)
def test_cobol_operators_ltphrase_instantiation(instance):
    assert isinstance(instance, cobol_operators_LTPhrase)

@given(instance=cobol_operators_EqualSign_strategy)
@settings(max_examples=50)
def test_cobol_operators_equalsign_instantiation(instance):
    assert isinstance(instance, cobol_operators_EqualSign)

@given(instance=cobol_operators_EqualPhrase_strategy)
@settings(max_examples=50)
def test_cobol_operators_equalphrase_instantiation(instance):
    assert isinstance(instance, cobol_operators_EqualPhrase)

@given(instance=cobol_operators_Kanji_strategy)
@settings(max_examples=50)
def test_cobol_operators_kanji_instantiation(instance):
    assert isinstance(instance, cobol_operators_Kanji)

@given(instance=cobol_operators_AlphabeticLower_strategy)
@settings(max_examples=50)
def test_cobol_operators_alphabeticlower_instantiation(instance):
    assert isinstance(instance, cobol_operators_AlphabeticLower)

@given(instance=cobol_operators_AlphabeticUpper_strategy)
@settings(max_examples=50)
def test_cobol_operators_alphabeticupper_instantiation(instance):
    assert isinstance(instance, cobol_operators_AlphabeticUpper)

@given(instance=cobol_operators_Numeric_strategy)
@settings(max_examples=50)
def test_cobol_operators_numeric_instantiation(instance):
    assert isinstance(instance, cobol_operators_Numeric)

@given(instance=cobol_operators_DBCS_strategy)
@settings(max_examples=50)
def test_cobol_operators_dbcs_instantiation(instance):
    assert isinstance(instance, cobol_operators_DBCS)

@given(instance=cobol_operators_Alphabetic_strategy)
@settings(max_examples=50)
def test_cobol_operators_alphabetic_instantiation(instance):
    assert isinstance(instance, cobol_operators_Alphabetic)

@given(instance=cobol_operators_ClassName_strategy)
@settings(max_examples=50)
def test_cobol_operators_classname_instantiation(instance):
    assert isinstance(instance, cobol_operators_ClassName)

@given(instance=cobol_operators_Zero_strategy)
@settings(max_examples=50)
def test_cobol_operators_zero_instantiation(instance):
    assert isinstance(instance, cobol_operators_Zero)

@given(instance=paragraphs_IOSectionParagraph_strategy)
@settings(max_examples=50)
def test_paragraphs_iosectionparagraph_instantiation(instance):
    assert isinstance(instance, paragraphs_IOSectionParagraph)

@given(instance=cobol_paragraphs_IOControlParagraph_strategy)
@settings(max_examples=50)
def test_cobol_paragraphs_iocontrolparagraph_instantiation(instance):
    assert isinstance(instance, cobol_paragraphs_IOControlParagraph)

@given(instance=SelectStatement_strategy)
@settings(max_examples=50)
def test_selectstatement_instantiation(instance):
    assert isinstance(instance, SelectStatement)

@given(instance=IOSectionParagraph_strategy)
@settings(max_examples=50)
def test_iosectionparagraph_instantiation(instance):
    assert isinstance(instance, IOSectionParagraph)

@given(instance=cobol_paragraphs_FileControlParagraph_strategy)
@settings(max_examples=50)
def test_cobol_paragraphs_filecontrolparagraph_instantiation(instance):
    assert isinstance(instance, cobol_paragraphs_FileControlParagraph)

@given(instance=paragraphs_ConfigurationSectionParagraph_strategy)
@settings(max_examples=50)
def test_paragraphs_configurationsectionparagraph_instantiation(instance):
    assert isinstance(instance, paragraphs_ConfigurationSectionParagraph)

@given(instance=cobol_paragraphs_RepositoryParagraph_strategy)
@settings(max_examples=50)
def test_cobol_paragraphs_repositoryparagraph_instantiation(instance):
    assert isinstance(instance, cobol_paragraphs_RepositoryParagraph)

@given(instance=cobol_paragraphs_ObjectComputerParagraph_strategy)
@settings(max_examples=50)
def test_cobol_paragraphs_objectcomputerparagraph_instantiation(instance):
    assert isinstance(instance, cobol_paragraphs_ObjectComputerParagraph)

@given(instance=DebuggingMode_strategy)
@settings(max_examples=50)
def test_debuggingmode_instantiation(instance):
    assert isinstance(instance, DebuggingMode)

@given(instance=ConfigurationSectionParagraph_strategy)
@settings(max_examples=50)
def test_configurationsectionparagraph_instantiation(instance):
    assert isinstance(instance, ConfigurationSectionParagraph)

@given(instance=cobol_paragraphs_SpecialNamesParagraph_strategy)
@settings(max_examples=50)
def test_cobol_paragraphs_specialnamesparagraph_instantiation(instance):
    assert isinstance(instance, cobol_paragraphs_SpecialNamesParagraph)

@given(instance=cobol_paragraphs_SourceComputerParagraph_strategy)
@settings(max_examples=50)
def test_cobol_paragraphs_sourcecomputerparagraph_instantiation(instance):
    assert isinstance(instance, cobol_paragraphs_SourceComputerParagraph)

@given(instance=labels_Procedure_strategy)
@settings(max_examples=50)
def test_labels_procedure_instantiation(instance):
    assert isinstance(instance, labels_Procedure)

@given(instance=cobol_sections_Section_strategy)
@settings(max_examples=50)
def test_cobol_sections_section_instantiation(instance):
    assert isinstance(instance, cobol_sections_Section)



@given(instance=cobol_sections_Section_strategy)
def test_cobol_sections_section_segmentNumber_setter(instance):
    original = instance.segmentNumber
    instance.segmentNumber = original
    assert instance.segmentNumber == original

@given(instance=cobol_paragraphs_Paragraph_strategy)
@settings(max_examples=50)
def test_cobol_paragraphs_paragraph_instantiation(instance):
    assert isinstance(instance, cobol_paragraphs_Paragraph)

@given(instance=GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_greaterthanorequal_instantiation(instance):
    assert isinstance(instance, GreaterThanOrEqual)

@given(instance=cobol_operators_GTEQSign_strategy)
@settings(max_examples=50)
def test_cobol_operators_gteqsign_instantiation(instance):
    assert isinstance(instance, cobol_operators_GTEQSign)

@given(instance=cobol_operators_GTEQPhrase_strategy)
@settings(max_examples=50)
def test_cobol_operators_gteqphrase_instantiation(instance):
    assert isinstance(instance, cobol_operators_GTEQPhrase)

@given(instance=cobol_operators_GTSign_strategy)
@settings(max_examples=50)
def test_cobol_operators_gtsign_instantiation(instance):
    assert isinstance(instance, cobol_operators_GTSign)

@given(instance=operators_UnaryOperator_strategy)
@settings(max_examples=50)
def test_operators_unaryoperator_instantiation(instance):
    assert isinstance(instance, operators_UnaryOperator)

@given(instance=operators_AdditiveOperator_strategy)
@settings(max_examples=50)
def test_operators_additiveoperator_instantiation(instance):
    assert isinstance(instance, operators_AdditiveOperator)

@given(instance=cobol_operators_Subtraction_strategy)
@settings(max_examples=50)
def test_cobol_operators_subtraction_instantiation(instance):
    assert isinstance(instance, cobol_operators_Subtraction)

@given(instance=cobol_operators_Addition_strategy)
@settings(max_examples=50)
def test_cobol_operators_addition_instantiation(instance):
    assert isinstance(instance, cobol_operators_Addition)

@given(instance=cobol_operators_Division_strategy)
@settings(max_examples=50)
def test_cobol_operators_division_instantiation(instance):
    assert isinstance(instance, cobol_operators_Division)

@given(instance=cobol_operators_Negative_strategy)
@settings(max_examples=50)
def test_cobol_operators_negative_instantiation(instance):
    assert isinstance(instance, cobol_operators_Negative)

@given(instance=cobol_operators_Positive_strategy)
@settings(max_examples=50)
def test_cobol_operators_positive_instantiation(instance):
    assert isinstance(instance, cobol_operators_Positive)

@given(instance=cobol_operators_Multiplication_strategy)
@settings(max_examples=50)
def test_cobol_operators_multiplication_instantiation(instance):
    assert isinstance(instance, cobol_operators_Multiplication)

@given(instance=cobol_operators_ConditionAnd_strategy)
@settings(max_examples=50)
def test_cobol_operators_conditionand_instantiation(instance):
    assert isinstance(instance, cobol_operators_ConditionAnd)

@given(instance=cobol_operators_ConditionOr_strategy)
@settings(max_examples=50)
def test_cobol_operators_conditionor_instantiation(instance):
    assert isinstance(instance, cobol_operators_ConditionOr)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=cobol_operators_LogicalOperator_strategy)
@settings(max_examples=50)
def test_cobol_operators_logicaloperator_instantiation(instance):
    assert isinstance(instance, cobol_operators_LogicalOperator)

@given(instance=cobol_operators_MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_cobol_operators_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, cobol_operators_MultiplicativeOperator)

@given(instance=cobol_operators_RelationalOperator_strategy)
@settings(max_examples=50)
def test_cobol_operators_relationaloperator_instantiation(instance):
    assert isinstance(instance, cobol_operators_RelationalOperator)

@given(instance=cobol_operators_UnaryOperator_strategy)
@settings(max_examples=50)
def test_cobol_operators_unaryoperator_instantiation(instance):
    assert isinstance(instance, cobol_operators_UnaryOperator)

@given(instance=cobol_operators_SignOperator_strategy)
@settings(max_examples=50)
def test_cobol_operators_signoperator_instantiation(instance):
    assert isinstance(instance, cobol_operators_SignOperator)

@given(instance=cobol_operators_AdditiveOperator_strategy)
@settings(max_examples=50)
def test_cobol_operators_additiveoperator_instantiation(instance):
    assert isinstance(instance, cobol_operators_AdditiveOperator)

@given(instance=cobol_operators_Operator_strategy)
@settings(max_examples=50)
def test_cobol_operators_operator_instantiation(instance):
    assert isinstance(instance, cobol_operators_Operator)

@given(instance=AlphanumericLiteral_strategy)
@settings(max_examples=50)
def test_alphanumericliteral_instantiation(instance):
    assert isinstance(instance, AlphanumericLiteral)

@given(instance=cobol_literals_AlphanumericHexaDecimalLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_alphanumerichexadecimalliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_AlphanumericHexaDecimalLiteral)

@given(instance=cobol_operators_ClassOperator_strategy)
@settings(max_examples=50)
def test_cobol_operators_classoperator_instantiation(instance):
    assert isinstance(instance, cobol_operators_ClassOperator)

@given(instance=cobol_operators_Through_strategy)
@settings(max_examples=50)
def test_cobol_operators_through_instantiation(instance):
    assert isinstance(instance, cobol_operators_Through)



@given(instance=cobol_operators_Through_strategy)
def test_cobol_operators_through_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_operators_Negate_strategy)
@settings(max_examples=50)
def test_cobol_operators_negate_instantiation(instance):
    assert isinstance(instance, cobol_operators_Negate)

@given(instance=cobol_operators_Power_strategy)
@settings(max_examples=50)
def test_cobol_operators_power_instantiation(instance):
    assert isinstance(instance, cobol_operators_Power)

@given(instance=cobol_operators_Equal_strategy)
@settings(max_examples=50)
def test_cobol_operators_equal_instantiation(instance):
    assert isinstance(instance, cobol_operators_Equal)



@given(instance=cobol_operators_Equal_strategy)
def test_cobol_operators_equal_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=cobol_operators_LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_cobol_operators_lessthanorequal_instantiation(instance):
    assert isinstance(instance, cobol_operators_LessThanOrEqual)



@given(instance=cobol_operators_LessThanOrEqual_strategy)
def test_cobol_operators_lessthanorequal_than_setter(instance):
    original = instance.than
    instance.than = original
    assert instance.than == original



@given(instance=cobol_operators_LessThanOrEqual_strategy)
def test_cobol_operators_lessthanorequal_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=cobol_operators_LessThan_strategy)
@settings(max_examples=50)
def test_cobol_operators_lessthan_instantiation(instance):
    assert isinstance(instance, cobol_operators_LessThan)



@given(instance=cobol_operators_LessThan_strategy)
def test_cobol_operators_lessthan_than_setter(instance):
    original = instance.than
    instance.than = original
    assert instance.than == original

@given(instance=cobol_operators_GreaterThan_strategy)
@settings(max_examples=50)
def test_cobol_operators_greaterthan_instantiation(instance):
    assert isinstance(instance, cobol_operators_GreaterThan)



@given(instance=cobol_operators_GreaterThan_strategy)
def test_cobol_operators_greaterthan_than_setter(instance):
    original = instance.than
    instance.than = original
    assert instance.than == original

@given(instance=cobol_operators_GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_cobol_operators_greaterthanorequal_instantiation(instance):
    assert isinstance(instance, cobol_operators_GreaterThanOrEqual)



@given(instance=cobol_operators_GreaterThanOrEqual_strategy)
def test_cobol_operators_greaterthanorequal_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=cobol_operators_GreaterThanOrEqual_strategy)
def test_cobol_operators_greaterthanorequal_than_setter(instance):
    original = instance.than
    instance.than = original
    assert instance.than == original

@given(instance=cobol_literals_HighValue_strategy)
@settings(max_examples=50)
def test_cobol_literals_highvalue_instantiation(instance):
    assert isinstance(instance, cobol_literals_HighValue)



@given(instance=cobol_literals_HighValue_strategy)
def test_cobol_literals_highvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_literals_LowValue_strategy)
@settings(max_examples=50)
def test_cobol_literals_lowvalue_instantiation(instance):
    assert isinstance(instance, cobol_literals_LowValue)



@given(instance=cobol_literals_LowValue_strategy)
def test_cobol_literals_lowvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_literals_Quote_strategy)
@settings(max_examples=50)
def test_cobol_literals_quote_instantiation(instance):
    assert isinstance(instance, cobol_literals_Quote)



@given(instance=cobol_literals_Quote_strategy)
def test_cobol_literals_quote_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_literals_Zero_strategy)
@settings(max_examples=50)
def test_cobol_literals_zero_instantiation(instance):
    assert isinstance(instance, cobol_literals_Zero)



@given(instance=cobol_literals_Zero_strategy)
def test_cobol_literals_zero_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_literals_Null_strategy)
@settings(max_examples=50)
def test_cobol_literals_null_instantiation(instance):
    assert isinstance(instance, cobol_literals_Null)



@given(instance=cobol_literals_Null_strategy)
def test_cobol_literals_null_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_literals_FixedDecimalLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_fixeddecimalliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_FixedDecimalLiteral)

@given(instance=DBCSLiteral_strategy)
@settings(max_examples=50)
def test_dbcsliteral_instantiation(instance):
    assert isinstance(instance, DBCSLiteral)

@given(instance=cobol_literals_NationalHexLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_nationalhexliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_NationalHexLiteral)



@given(instance=cobol_literals_NationalHexLiteral_strategy)
def test_cobol_literals_nationalhexliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_literals_NationalLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_nationalliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_NationalLiteral)



@given(instance=cobol_literals_NationalLiteral_strategy)
def test_cobol_literals_nationalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_literals_DBCSLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_dbcsliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_DBCSLiteral)

@given(instance=cobol_literals_PseudoLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_pseudoliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_PseudoLiteral)



@given(instance=cobol_literals_PseudoLiteral_strategy)
def test_cobol_literals_pseudoliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol_literals_Characters_strategy)
@settings(max_examples=50)
def test_cobol_literals_characters_instantiation(instance):
    assert isinstance(instance, cobol_literals_Characters)

@given(instance=cobol_literals_Any_strategy)
@settings(max_examples=50)
def test_cobol_literals_any_instantiation(instance):
    assert isinstance(instance, cobol_literals_Any)

@given(instance=cobol_literals_Space_strategy)
@settings(max_examples=50)
def test_cobol_literals_space_instantiation(instance):
    assert isinstance(instance, cobol_literals_Space)



@given(instance=cobol_literals_Space_strategy)
def test_cobol_literals_space_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=labels_StopLabel_strategy)
@settings(max_examples=50)
def test_labels_stoplabel_instantiation(instance):
    assert isinstance(instance, labels_StopLabel)

@given(instance=cobol_literals_Literal_strategy)
@settings(max_examples=50)
def test_cobol_literals_literal_instantiation(instance):
    assert isinstance(instance, cobol_literals_Literal)

@given(instance=cobol_literals_ConstantLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_constantliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_ConstantLiteral)

@given(instance=cobol_literals_NumericLiteral_strategy)
@settings(max_examples=50)
def test_cobol_literals_numericliteral_instantiation(instance):
    assert isinstance(instance, cobol_literals_NumericLiteral)
