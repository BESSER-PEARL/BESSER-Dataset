import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    strings::Occurrence,
    strings::Tallying,
    cobol::strings::TallyingOccurrence,
    cobol::strings::Occurrence,
    cobol::strings::Location,
    ManipulatedStrings,
    cobol::strings::SplittedString,
    cobol::strings::ConcatenatingStrings,
    cobol::strings::String,
    Location,
    String,
    cobol::strings::ManipulatedStrings,
    cobol::strings::StringManipulation,
    StringManipulation,
    cobol::strings::Replacement,
    cobol::strings::Tallying,
    strings::Replacement,
    cobol::strings::ReplacementOccurrence,
    NotErrorHandler,
    cobol::handlers::NotOnOverflow,
    cobol::handlers::NotAtEnd,
    cobol::handlers::NotInvalidKey,
    cobol::handlers::NotOnException,
    cobol::handlers::NotOnSizeError,
    cobol::functions::Argumentable,
    Argument,
    cobol::functions::OmittedArgument,
    cobol::functions::ByContentArgument,
    cobol::functions::ByValueArgument,
    cobol::functions::ByReferenceArgument,
    cobol::functions::Argument,
    cobol::labels::Label,
    cobol::labels::Procedure,
    Procedure,
    cobol::handlers::NotAtEndOfPage,
    ProcedureRangeChild,
    cobol::verbs::Verb,
    Verb,
    cobol::verbs::Is,
    DeclarativeSection,
    cobol::declaratives::Declaratives,
    cobol::labels::ProcedureLabel,
    cobol::files::FileStatus,
    FileStatus,
    cobol::tables::TableDimension,
    AdditionalIndexName,
    Parameter,
    cobol::parameters::ByReferenceParameter,
    cobol::parameters::ByValueParameter,
    cobol::parameters::Parametrizable,
    IndexName,
    TableDimension,
    dataitems::DataItem,
    cobol::specialnames::SpecialNameStatement,
    AlphabetNameReference,
    SymbolicCharacter,
    SpecialName,
    cobol::specialnames::SymbolicCharacter,
    cobol::specialnames::MnemonicName,
    cobol::tables::KeyName,
    KeyName,
    cobol::specialnames::AlphabetType,
    specialnames::MnemonicName,
    AlphabetType,
    cobol::specialnames::CodeNameAlphabetType,
    cobol::specialnames::PredefinedAlphabetType,
    specialnames::SpecialNameStatement,
    cobol::specialnames::UPSISwitchIs,
    cobol::specialnames::SystemDeviceIs,
    ConditionName,
    cobol::specialnames::OffStatus,
    cobol::specialnames::OnStatus,
    specialnames::SpecialName,
    cobol::specialnames::CurrencySign,
    cobol::specialnames::ClassName,
    cobol::specialnames::AlphabetName,
    cobol::specialnames::ExplicitAlphabetType,
    references::ReferenceableElement,
    cobol::dataitems::DataItemAttribute,
    RangeExpression,
    DataName,
    cobol::dataitems::RenamingDataName,
    DataItemAttribute,
    cobol::dataitems::Redefines,
    cobol::dataitems::Usage,
    cobol::dataitems::Value,
    cobol::dataitems::External,
    cobol::dataitems::GroupUsage,
    cobol::dataitems::Global,
    cobol::dataitems::PictureString,
    SystemDevice,
    cobol::environments::AdvancedFunctionPrinting,
    cobol::environments::Pocket,
    cobol::environments::SuppressSpacing,
    cobol::environments::SystemLogicalOutput,
    cobol::environments::SystemPunchDevice,
    cobol::environments::Console,
    cobol::environments::Channel,
    cobol::environments::SystemLogicalInput,
    Register,
    cobol::registers::AddressOf,
    cobol::registers::WhenCompiled,
    cobol::registers::ShiftOut,
    cobol::registers::ReturnCode,
    cobol::registers::LengthOf,
    cobol::registers::ShiftIn,
    SortPhraseWater,
    cobol::water::SortPhraseToken,
    OpenStatementWater,
    cobol::water::OpenStatementToken,
    InvokeStatementWater,
    cobol::water::InvokeStatementToken,
    CloseStatementWater,
    cobol::water::CloseStatementToken,
    UseStatementWater,
    cobol::water::UseStatementToken,
    AcceptStatementWater,
    cobol::environments::Environment,
    cobol::water::AcceptStatementToken,
    CICSStatementWater,
    cobol::water::CICSStatementToken,
    SQLStatementWater,
    cobol::water::SQLStatementToken,
    RepositoryParagraphWater,
    cobol::water::RepositoryDescription,
    IOControlParagraphWater,
    cobol::water::IOControlDescription,
    DataDescriptorWater,
    cobol::water::DataDescription,
    FileDescriptorWater,
    cobol::water::FileDescription,
    SelectStatementWater,
    cobol::water::SelectStatementClause,
    ObjectComputerParagraphWater,
    cobol::water::PriorityNumber,
    cobol::water::ObjectComputerDescription,
    cobol::water::Water,
    Water,
    cobol::water::SpecialNamesParagraphWater,
    cobol::water::SelectStatementWater,
    cobol::water::FileDescriptorWater,
    cobol::water::CICSStatementWater,
    cobol::water::RepositoryParagraphWater,
    cobol::water::InvokeStatementWater,
    cobol::water::ObjectComputerParagraphWater,
    cobol::water::DataDescriptorWater,
    cobol::water::CloseStatementWater,
    cobol::water::OpenStatementWater,
    cobol::water::AcceptStatementWater,
    cobol::water::SQLStatementWater,
    cobol::water::IdentificationDivisionWater,
    cobol::water::SortPhraseWater,
    cobol::water::UseStatementWater,
    cobol::water::IOControlParagraphWater,
    cobol::water::IncompleteElement,
    Label,
    cobol::labels::ProcedureRangeLabel,
    cobol::labels::StopLabel,
    cobol::ios::IODirectives,
    ios::OutputDirective,
    ios::FileDirective,
    cobol::ios::OutputFile,
    IODirectives,
    cobol::ios::ProcedureDirective,
    cobol::ios::FileDirective,
    cobol::ios::OutputDirective,
    cobol::ios::InputDirective,
    ios::ProcedureDirective,
    cobol::ios::OutputProcedure,
    ios::InputDirective,
    cobol::ios::InputFile,
    cobol::ios::InputProcedure,
    cobol::identifiers::ReferenceModifier,
    DirectSubscript,
    cobol::identifiers::All,
    IdentificationDivisionWater,
    cobol::water::ProgramDescription,
    Subscript,
    cobol::identifiers::DirectSubscript,
    cobol::identifiers::RelativeSubscript,
    identifiers::Identifier,
    ReferenceModifier,
    water::SortPhraseWater,
    water::DataDescriptorWater,
    water::UseStatementWater,
    water::SQLStatementWater,
    water::IdentificationDivisionWater,
    cobol::water::Dot,
    water::RepositoryParagraphWater,
    water::AcceptStatementWater,
    cobol::identifiers::Subscript,
    VaryingUntilCondition,
    cobol::statements::AfterUntilCondition,
    Qualifier,
    Conditional,
    cobol::statements::VaryingUntilCondition,
    Tallying,
    cobol::strings::AnyCharacter,
    cobol::strings::SpecificCharacter,
    cobol::statements::TallyingIn,
    cobol::statements::Statement,
    cobol::operands::Operand,
    ReplacementOperand,
    cobol::operands::Encoding,
    Operand,
    cobol::operands::ArithmeticOperand,
    cobol::operands::ReplacementOperand,
    Identifier,
    statements::NestedStatement,
    statements::Perform,
    cobol::statements::PerformNestedStatement,
    ArithmeticStatement,
    cobol::statements::Multiply,
    cobol::statements::Subtract,
    cobol::statements::Divide,
    cobol::statements::Add,
    statements::ErrorHandled,
    statements::Statement,
    cobol::statements::Delete,
    cobol::statements::Start,
    cobol::statements::ArithmeticStatement,
    DataItem,
    cobol::dataitems::ConditionName,
    cobol::dataitems::DataName,
    cobol::dataitems::RecordName,
    Statement,
    cobol::statements::Perform,
    cobol::statements::Exit,
    EnvironmentDivisionSection,
    cobol::sections::ConfigurationSection,
    cobol::sections::IOSection,
    ArithmeticOperand,
    cobol::operands::RoundedIdentifier,
    DataDivisionSection,
    cobol::sections::LinkageStorageSection,
    cobol::sections::FileSection,
    cobol::sections::LocalStorageSection,
    cobol::sections::WorkingStorageSection,
    operands::ArithmeticOperand,
    arithmetics::PrimaryExpression,
    operands::Operand,
    operands::ReplacementOperand,
    cobol::operands::PrimaryOperand,
    sentences::StatementContainer,
    Sentence,
    cobol::sentences::ExitProcedure,
    cobol::sentences::AlteredGoTo,
    cobol::sentences::EntrySentence,
    cobol::sentences::EmptySentence,
    cobol::sentences::StatementContainer,
    FileName,
    Reference,
    cobol::references::ElementReference,
    ReferenceableElement,
    cobol::specialnames::SpecialName,
    cobol::parameters::Parameter,
    cobol::tables::AdditionalIndexName,
    cobol::references::Reference,
    cobol::paragraphs::DebuggingMode,
    SpecialNamesParagraphWater,
    cobol::water::SpecialNamesClause,
    SpecialNameStatement,
    IncompleteElement,
    cobol::files::SelectStatement,
    cobol::statements::IOFile,
    IOFile,
    cobol::statements::IOFileDescriptor,
    IOFileDescriptor,
    cobol::statements::IOStatement,
    cobol::statements::KeyDescriptor,
    statements::VaryingUntilCondition,
    cobol::statements::PerformUntilCondition,
    cobol::statements::Release,
    statements::PerformFixedTimes,
    statements::FileIOStatement,
    KeyDescriptor,
    OutputDirective,
    InputDirective,
    statements::PerformProcedure,
    cobol::statements::PerformProcedureFixedTimes,
    cobol::statements::FileIOStatement,
    statements::PerformNestedStatement,
    cobol::statements::PerformNestedStatementFixedTimes,
    AfterUntilCondition,
    statements::PerformUntilCondition,
    cobol::statements::PerformNestedStatementUntilCondition,
    cobol::statements::PerformProcedureUntilCondition,
    cobol::statements::Read,
    TallyingIn,
    cobol::statements::SwitchStatus,
    Write,
    cobol::statements::Rewrite,
    MnemonicNameReference,
    IntegerLiteral,
    cobol::statements::Write,
    cobol::statements::Unstring,
    SearchStatement,
    cobol::statements::BinarySearch,
    cobol::statements::SerialSearch,
    NormalEvaluateCase,
    cobol::statements::SearchStatement,
    Replacement,
    cobol::strings::SpecificCharacterBySpecificCharacter,
    cobol::strings::AnyCharacterBySpecificCharacter,
    cobol::statements::Initialize,
    cobol::statements::Inspect,
    cobol::statements::Replace,
    NestedStatement,
    cobol::handlers::Handler,
    cobol::statements::EvaluateCase,
    ExpressionList,
    EvaluateCase,
    cobol::statements::NormalEvaluateCase,
    cobol::statements::OtherEvaluateCase,
    cobol::statements::Evaluate,
    SplittedString,
    SetStatement,
    cobol::statements::Set,
    cobol::statements::SetSwitches,
    cobol::statements::SetStatement,
    FileNameReference,
    cobol::statements::Return,
    Handler,
    cobol::handlers::OnException,
    cobol::handlers::AtEndOfPage,
    cobol::handlers::NotErrorHandler,
    cobol::handlers::InvalidKey,
    cobol::handlers::OnOverflow,
    cobol::handlers::AtEnd,
    cobol::handlers::OnSizeError,
    cobol::statements::ErrorHandled,
    cobol::statements::Execute,
    functions::Argumentable,
    cobol::statements::Call,
    cobol::statements::Cancel,
    statements::IOStatement,
    ConcatenatingStrings,
    cobol::statements::String,
    IndexNameReference,
    cobol::statements::SetIndexName,
    SwitchStatus,
    PrimaryOperand,
    cobol::registers::Register,
    cobol::statements::Move,
    cobol::statements::NestedStatement,
    Jump,
    cobol::statements::Continue,
    cobol::statements::GoBack,
    cobol::statements::GoTo,
    cobol::statements::NextSentence,
    cobol::statements::Jump,
    ProcedureRangeLabel,
    cobol::labels::ProcedureRange,
    cobol::labels::ProcedureRangeChild,
    Perform,
    cobol::statements::PerformFixedTimes,
    cobol::statements::PerformProcedure,
    AssignmentExpression,
    cobol::statements::Compute,
    Environment,
    cobol::environments::SystemDevice,
    cobol::environments::UPSI,
    cobol::statements::Display,
    StopLabel,
    cobol::labels::Run,
    cobol::statements::Stop,
    cobol::statements::Conditional,
    statements::Conditional,
    cobol::statements::Condition,
    NegatedConditionalExpressionChild,
    ConditionalAndExpressionChild,
    cobol::conditions::NegatedConditionalExpression,
    LogicalOperator,
    ConditionalOrExpressionChild,
    Condition,
    cobol::conditions::ConditionalOrExpressionChild,
    cobol::conditions::ConditionalOrExpression,
    cobol::conditions::Condition,
    Is,
    RelationalOperator,
    SimpleConditionChild,
    cobol::conditions::RelationalExpression,
    cobol::conditions::SimpleConditionChild,
    cobol::conditions::NegatedConditionalExpressionChild,
    Negate,
    cobol::commons::Commentable,
    Commentable,
    cobol::commons::URIableElement,
    cobol::commons::LabellableElement,
    cobol::commons::NamedElement,
    identifiers::IdentifierReference,
    cobol::references::Qualifiable,
    cobol::references::ConditionName,
    ElementReference,
    cobol::identifiers::Qualifier,
    cobol::references::AlphabetNameReference,
    IdentifierReference,
    cobol::references::IndexNameReference,
    references::IdentifierReferenceQualifier,
    cobol::references::DataNameReference,
    references::ConditionName,
    cobol::references::ConditionNameReference,
    references::Qualifiable,
    cobol::identifiers::LinageCounter,
    references::ElementReference,
    cobol::identifiers::IdentifierReference,
    cobol::references::FileNameReference,
    cobol::references::MnemonicNameReference,
    cobol::references::IdentifierReferenceQualifier,
    cobol::specialnames::SymbolicCharacterStatement,
    cobol::references::SpecialNamesConditionNameReference,
    GreaterThan,
    cobol::operators::GTPhrase,
    LessThanOrEqual,
    cobol::operators::LTEQSign,
    cobol::operators::LTEQPhrase,
    LessThan,
    cobol::operators::LTSign,
    cobol::operators::LTPhrase,
    paragraphs::IOSectionParagraph,
    SelectStatement,
    IOSectionParagraph,
    cobol::paragraphs::FileControlParagraph,
    paragraphs::ConfigurationSectionParagraph,
    DebuggingMode,
    ConfigurationSectionParagraph,
    cobol::paragraphs::SpecialNamesParagraph,
    cobol::paragraphs::SourceComputerParagraph,
    labels::Procedure,
    GreaterThanOrEqual,
    cobol::operators::GTEQSign,
    cobol::operators::GTEQPhrase,
    cobol::operators::GTSign,
    operators::UnaryOperator,
    operators::AdditiveOperator,
    cobol::operators::Subtraction,
    cobol::operators::Addition,
    cobol::operators::ConditionAnd,
    cobol::operators::ConditionOr,
    Operator,
    cobol::operators::RelationalOperator,
    cobol::operators::UnaryOperator,
    cobol::operators::LogicalOperator,
    cobol::operators::MultiplicativeOperator,
    cobol::operators::SignOperator,
    cobol::operators::AdditiveOperator,
    cobol::operators::Operator,
    AlphanumericLiteral,
    cobol::literals::AlphanumericHexaDecimalLiteral,
    cobol::operators::ClassOperator,
    cobol::operators::Through,
    cobol::operators::Negate,
    cobol::operators::Power,
    cobol::operators::Equal,
    cobol::operators::LessThanOrEqual,
    cobol::operators::LessThan,
    cobol::operators::GreaterThan,
    cobol::operators::GreaterThanOrEqual,
    DBCSLiteral,
    cobol::literals::NationalHexLiteral,
    cobol::literals::NationalLiteral,
    labels::StopLabel,
    ConstantLiteral,
    cobol::literals::HighValue,
    cobol::literals::LowValue,
    cobol::literals::Quote,
    cobol::literals::Null,
    cobol::literals::Zero,
    cobol::literals::Space,
    FigurativeConstantLiteral,
    cobol::literals::ConstantLiteral,
    cobol::literals::AllLiteral,
    DecimalLiteral,
    cobol::literals::FixedDecimalLiteral,
    cobol::literals::FloatingDecimalLiteral,
    NumericLiteral,
    cobol::literals::DecimalLiteral,
    water::IOControlParagraphWater,
    water::FileDescriptorWater,
    water::ObjectComputerParagraphWater,
    literals::NumericLiteral,
    cobol::literals::IntegerLiteral,
    Literal,
    cobol::literals::NumericLiteral,
    cobol::literals::Any,
    cobol::literals::FigurativeConstantLiteral,
    cobol::literals::DBCSLiteral,
    cobol::literals::PseudoLiteral,
    cobol::literals::BooleanLiteral,
    cobol::literals::Characters,
    cobol::literals::AlphanumericLiteral,
    Division,
    cobol::divisions::EnvironmentDivision,
    cobol::divisions::DataDivision,
    StatementContainer,
    cobol::sentences::Sentence,
    cobol::sentences::ExecuteSentence,
    Paragraph,
    cobol::paragraphs::IOSectionParagraph,
    cobol::paragraphs::ConfigurationSectionParagraph,
    Section,
    cobol::sections::DeclarativeSection,
    cobol::sections::DataDivisionSection,
    cobol::sections::EnvironmentDivisionSection,
    CobolRoot,
    cobol::containers::EmptyModel,
    cobol::containers::CobolRoot,
    ProcedureDivision,
    DataDivision,
    EnvironmentDivision,
    water::InvokeStatementWater,
    operands::PrimaryOperand,
    water::CICSStatementWater,
    water::SpecialNamesParagraphWater,
    water::SelectStatementWater,
    cobol::identifiers::Identifier,
    cobol::literals::Literal,
    Declaratives,
    parameters::Parametrizable,
    cobol::statements::Entry,
    water::IncompleteElement,
    cobol::files::FileName,
    cobol::statements::Merge,
    cobol::statements::Accept,
    cobol::dataitems::DataItem,
    cobol::paragraphs::RepositoryParagraph,
    cobol::statements::Sort,
    cobol::statements::Open,
    cobol::paragraphs::IOControlParagraph,
    cobol::paragraphs::ObjectComputerParagraph,
    cobol::sentences::UseSentence,
    cobol::tables::Table,
    cobol::statements::Close,
    divisions::Division,
    cobol::divisions::ProcedureDivision,
    cobol::divisions::IdentificationDivision,
    ArithmeticExpression,
    cobol::arithmetics::RangeExpression,
    Equal,
    cobol::operators::EqualPhrase,
    cobol::operators::EqualSign,
    cobol::arithmetics::AssignmentExpression,
    UnaryOperator,
    UnaryArithmeticExpressionChild,
    cobol::arithmetics::PrimaryExpression,
    PowerArithmeticExpressionChild,
    cobol::arithmetics::UnaryArithmeticExpression,
    cobol::arithmetics::UnaryArithmeticExpressionChild,
    IdentificationDivision,
    NamedElement,
    cobol::divisions::Division,
    cobol::references::ReferenceableElement,
    cobol::containers::CompilationUnit,
    CompilationUnit,
    commons::NamedElement,
    cobol::functions::FunctionCall,
    cobol::sections::Section,
    cobol::tables::IndexName,
    cobol::specialnames::ConditionName,
    cobol::paragraphs::Paragraph,
    containers::CobolRoot,
    cobol::containers::CompilationGroup,
    conditions::SimpleConditionChild,
    conditions::AbbreviatedRelationalExpressionChild,
    cobol::arithmetics::ArithmeticExpression,
    PrimaryExpression,
    cobol::arithmetics::NestedArithmeticExpression,
    cobol::arithmetics::RangeExpressionChild,
    Through,
    ClassOperator,
    cobol::operators::ClassName,
    cobol::operators::DBCS,
    cobol::operators::Kanji,
    cobol::operators::AlphabeticLower,
    cobol::operators::AlphabeticUpper,
    cobol::operators::Numeric,
    cobol::operators::Alphabetic,
    cobol::conditions::ClassCondition,
    SignOperator,
    cobol::operators::Negative,
    cobol::operators::Zero,
    cobol::operators::Positive,
    MultiplicativeOperator,
    cobol::operators::Multiplication,
    cobol::operators::Division,
    MultiplicativeArithmeticExpressionChild,
    cobol::arithmetics::PowerArithmeticExpressionChild,
    cobol::arithmetics::PowerArithmeticExpression,
    AdditiveOperator,
    AdditiveArithmeticExpressionChild,
    cobol::arithmetics::MultiplicativeArithmeticExpressionChild,
    cobol::arithmetics::MultiplicativeArithmeticExpression,
    RangeExpressionChild,
    cobol::arithmetics::AdditiveArithmeticExpressionChild,
    cobol::arithmetics::AdditiveArithmeticExpression,
    cobol::conditions::NestedCondition,
    NegatedAbbreviatedConditionalExpressionChild,
    cobol::conditions::AbbreviatedRelationalExpressionChild,
    cobol::conditions::AbbreviatedRelationalExpression,
    cobol::conditions::AbbreviatedConditionalExpressionChild,
    AbbreviatedConditionalExpressionChild,
    cobol::conditions::NegatedAbbreviatedConditionalExpressionChild,
    cobol::conditions::NegatedAbbreviatedConditionalExpression,
    cobol::conditions::AbbreviatedConditionalExpression,
    cobol::conditions::ConditionalAndExpression,
    cobol::conditions::ConditionalAndExpressionChild,
    cobol::conditions::ExpressionList,
    cobol::conditions::SignCondition,
    AbbreviatedRelationalExpressionChild,
    cobol::conditions::NestedAbbreviatedConditionalExpression,
    RepositoryDescriptionInfo,
    SystemPunchDevices,
    Quotes,
    Spaces,
    FileDescriptors,
    InvokeStatementTokens,
    EncodingTypes,
    SelectStatementClauses,
    UseStatementTokens,
    SpecialNamesClauses,
    Adjustings,
    PredefinedAlphabetTypes,
    ObjectComputerDescriptionInfo,
    Selects,
    IOControlDescriptionInfo,
    Channels,
    FileDescriptionInfo,
    SystemOutputs,
    ThroughPhrase,
    UPSISwitches,
    DataDescriptionInfo,
    ProgramDescriptionInfo,
    PictureStringCharacters,
    Occurrences,
    Zeroes,
    OpenStatementTokens,
    LowValues,
    HighValues,
    ExitLabels,
    Positions,
    Status,
    SystemInputs,
    Properties,
    SQLStatementTokens,
    Usages,
    IOTypes,
    Corresponding,
    AcceptStatementTokens,
    EOP,
    CICSStatementTokens,
    SortPhraseTokens,
    Orders,
    SortingOrder,
    Nulls,
    CloseStatementTokens,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_strings::occurrence_is_not_abstract():
    assert not inspect.isabstract(strings::Occurrence)


def test_strings::occurrence_constructor_exists():
    assert callable(strings::Occurrence.__init__)


def test_strings::occurrence_constructor_args():
    sig = inspect.signature(strings::Occurrence.__init__)
    params = list(sig.parameters.keys())



def test_strings::tallying_is_not_abstract():
    assert not inspect.isabstract(strings::Tallying)


def test_strings::tallying_constructor_exists():
    assert callable(strings::Tallying.__init__)


def test_strings::tallying_constructor_args():
    sig = inspect.signature(strings::Tallying.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::tallyingoccurrence_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::TallyingOccurrence)


def test_cobol::strings::tallyingoccurrence_constructor_exists():
    assert callable(cobol::strings::TallyingOccurrence.__init__)


def test_cobol::strings::tallyingoccurrence_constructor_args():
    sig = inspect.signature(cobol::strings::TallyingOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::occurrence_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::Occurrence)


def test_cobol::strings::occurrence_constructor_exists():
    assert callable(cobol::strings::Occurrence.__init__)


def test_cobol::strings::occurrence_constructor_args():
    sig = inspect.signature(cobol::strings::Occurrence.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cobol::strings::occurrence_has_type():
    assert hasattr(cobol::strings::Occurrence, "type")
    descriptor = None
    for klass in cobol::strings::Occurrence.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cobol::strings::location_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::Location)


def test_cobol::strings::location_constructor_exists():
    assert callable(cobol::strings::Location.__init__)


def test_cobol::strings::location_constructor_args():
    sig = inspect.signature(cobol::strings::Location.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "position" in params, "Missing parameter 'position'"

def test_cobol::strings::location_has_initial():
    assert hasattr(cobol::strings::Location, "initial")
    descriptor = None
    for klass in cobol::strings::Location.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_cobol::strings::location_has_position():
    assert hasattr(cobol::strings::Location, "position")
    descriptor = None
    for klass in cobol::strings::Location.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_manipulatedstrings_is_not_abstract():
    assert not inspect.isabstract(ManipulatedStrings)


def test_manipulatedstrings_constructor_exists():
    assert callable(ManipulatedStrings.__init__)


def test_manipulatedstrings_constructor_args():
    sig = inspect.signature(ManipulatedStrings.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::splittedstring_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::SplittedString)


def test_cobol::strings::splittedstring_constructor_exists():
    assert callable(cobol::strings::SplittedString.__init__)


def test_cobol::strings::splittedstring_constructor_args():
    sig = inspect.signature(cobol::strings::SplittedString.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::concatenatingstrings_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::ConcatenatingStrings)


def test_cobol::strings::concatenatingstrings_constructor_exists():
    assert callable(cobol::strings::ConcatenatingStrings.__init__)


def test_cobol::strings::concatenatingstrings_constructor_args():
    sig = inspect.signature(cobol::strings::ConcatenatingStrings.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::string_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::String)


def test_cobol::strings::string_constructor_exists():
    assert callable(cobol::strings::String.__init__)


def test_cobol::strings::string_constructor_args():
    sig = inspect.signature(cobol::strings::String.__init__)
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



def test_cobol::strings::manipulatedstrings_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::ManipulatedStrings)


def test_cobol::strings::manipulatedstrings_constructor_exists():
    assert callable(cobol::strings::ManipulatedStrings.__init__)


def test_cobol::strings::manipulatedstrings_constructor_args():
    sig = inspect.signature(cobol::strings::ManipulatedStrings.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::stringmanipulation_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::StringManipulation)


def test_cobol::strings::stringmanipulation_constructor_exists():
    assert callable(cobol::strings::StringManipulation.__init__)


def test_cobol::strings::stringmanipulation_constructor_args():
    sig = inspect.signature(cobol::strings::StringManipulation.__init__)
    params = list(sig.parameters.keys())



def test_stringmanipulation_is_not_abstract():
    assert not inspect.isabstract(StringManipulation)


def test_stringmanipulation_constructor_exists():
    assert callable(StringManipulation.__init__)


def test_stringmanipulation_constructor_args():
    sig = inspect.signature(StringManipulation.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::replacement_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::Replacement)


def test_cobol::strings::replacement_constructor_exists():
    assert callable(cobol::strings::Replacement.__init__)


def test_cobol::strings::replacement_constructor_args():
    sig = inspect.signature(cobol::strings::Replacement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::tallying_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::Tallying)


def test_cobol::strings::tallying_constructor_exists():
    assert callable(cobol::strings::Tallying.__init__)


def test_cobol::strings::tallying_constructor_args():
    sig = inspect.signature(cobol::strings::Tallying.__init__)
    params = list(sig.parameters.keys())



def test_strings::replacement_is_not_abstract():
    assert not inspect.isabstract(strings::Replacement)


def test_strings::replacement_constructor_exists():
    assert callable(strings::Replacement.__init__)


def test_strings::replacement_constructor_args():
    sig = inspect.signature(strings::Replacement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::replacementoccurrence_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::ReplacementOccurrence)


def test_cobol::strings::replacementoccurrence_constructor_exists():
    assert callable(cobol::strings::ReplacementOccurrence.__init__)


def test_cobol::strings::replacementoccurrence_constructor_args():
    sig = inspect.signature(cobol::strings::ReplacementOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_noterrorhandler_is_not_abstract():
    assert not inspect.isabstract(NotErrorHandler)


def test_noterrorhandler_constructor_exists():
    assert callable(NotErrorHandler.__init__)


def test_noterrorhandler_constructor_args():
    sig = inspect.signature(NotErrorHandler.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::notonoverflow_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::NotOnOverflow)


def test_cobol::handlers::notonoverflow_constructor_exists():
    assert callable(cobol::handlers::NotOnOverflow.__init__)


def test_cobol::handlers::notonoverflow_constructor_args():
    sig = inspect.signature(cobol::handlers::NotOnOverflow.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::notatend_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::NotAtEnd)


def test_cobol::handlers::notatend_constructor_exists():
    assert callable(cobol::handlers::NotAtEnd.__init__)


def test_cobol::handlers::notatend_constructor_args():
    sig = inspect.signature(cobol::handlers::NotAtEnd.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::notinvalidkey_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::NotInvalidKey)


def test_cobol::handlers::notinvalidkey_constructor_exists():
    assert callable(cobol::handlers::NotInvalidKey.__init__)


def test_cobol::handlers::notinvalidkey_constructor_args():
    sig = inspect.signature(cobol::handlers::NotInvalidKey.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::notonexception_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::NotOnException)


def test_cobol::handlers::notonexception_constructor_exists():
    assert callable(cobol::handlers::NotOnException.__init__)


def test_cobol::handlers::notonexception_constructor_args():
    sig = inspect.signature(cobol::handlers::NotOnException.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::notonsizeerror_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::NotOnSizeError)


def test_cobol::handlers::notonsizeerror_constructor_exists():
    assert callable(cobol::handlers::NotOnSizeError.__init__)


def test_cobol::handlers::notonsizeerror_constructor_args():
    sig = inspect.signature(cobol::handlers::NotOnSizeError.__init__)
    params = list(sig.parameters.keys())



def test_cobol::functions::argumentable_is_not_abstract():
    assert not inspect.isabstract(cobol::functions::Argumentable)


def test_cobol::functions::argumentable_constructor_exists():
    assert callable(cobol::functions::Argumentable.__init__)


def test_cobol::functions::argumentable_constructor_args():
    sig = inspect.signature(cobol::functions::Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_cobol::functions::omittedargument_is_not_abstract():
    assert not inspect.isabstract(cobol::functions::OmittedArgument)


def test_cobol::functions::omittedargument_constructor_exists():
    assert callable(cobol::functions::OmittedArgument.__init__)


def test_cobol::functions::omittedargument_constructor_args():
    sig = inspect.signature(cobol::functions::OmittedArgument.__init__)
    params = list(sig.parameters.keys())



def test_cobol::functions::bycontentargument_is_not_abstract():
    assert not inspect.isabstract(cobol::functions::ByContentArgument)


def test_cobol::functions::bycontentargument_constructor_exists():
    assert callable(cobol::functions::ByContentArgument.__init__)


def test_cobol::functions::bycontentargument_constructor_args():
    sig = inspect.signature(cobol::functions::ByContentArgument.__init__)
    params = list(sig.parameters.keys())



def test_cobol::functions::byvalueargument_is_not_abstract():
    assert not inspect.isabstract(cobol::functions::ByValueArgument)


def test_cobol::functions::byvalueargument_constructor_exists():
    assert callable(cobol::functions::ByValueArgument.__init__)


def test_cobol::functions::byvalueargument_constructor_args():
    sig = inspect.signature(cobol::functions::ByValueArgument.__init__)
    params = list(sig.parameters.keys())



def test_cobol::functions::byreferenceargument_is_not_abstract():
    assert not inspect.isabstract(cobol::functions::ByReferenceArgument)


def test_cobol::functions::byreferenceargument_constructor_exists():
    assert callable(cobol::functions::ByReferenceArgument.__init__)


def test_cobol::functions::byreferenceargument_constructor_args():
    sig = inspect.signature(cobol::functions::ByReferenceArgument.__init__)
    params = list(sig.parameters.keys())



def test_cobol::functions::argument_is_not_abstract():
    assert not inspect.isabstract(cobol::functions::Argument)


def test_cobol::functions::argument_constructor_exists():
    assert callable(cobol::functions::Argument.__init__)


def test_cobol::functions::argument_constructor_args():
    sig = inspect.signature(cobol::functions::Argument.__init__)
    params = list(sig.parameters.keys())



def test_cobol::labels::label_is_not_abstract():
    assert not inspect.isabstract(cobol::labels::Label)


def test_cobol::labels::label_constructor_exists():
    assert callable(cobol::labels::Label.__init__)


def test_cobol::labels::label_constructor_args():
    sig = inspect.signature(cobol::labels::Label.__init__)
    params = list(sig.parameters.keys())



def test_cobol::labels::procedure_is_not_abstract():
    assert not inspect.isabstract(cobol::labels::Procedure)


def test_cobol::labels::procedure_constructor_exists():
    assert callable(cobol::labels::Procedure.__init__)


def test_cobol::labels::procedure_constructor_args():
    sig = inspect.signature(cobol::labels::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_procedure_is_not_abstract():
    assert not inspect.isabstract(Procedure)


def test_procedure_constructor_exists():
    assert callable(Procedure.__init__)


def test_procedure_constructor_args():
    sig = inspect.signature(Procedure.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::notatendofpage_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::NotAtEndOfPage)


def test_cobol::handlers::notatendofpage_constructor_exists():
    assert callable(cobol::handlers::NotAtEndOfPage.__init__)


def test_cobol::handlers::notatendofpage_constructor_args():
    sig = inspect.signature(cobol::handlers::NotAtEndOfPage.__init__)
    params = list(sig.parameters.keys())



def test_procedurerangechild_is_not_abstract():
    assert not inspect.isabstract(ProcedureRangeChild)


def test_procedurerangechild_constructor_exists():
    assert callable(ProcedureRangeChild.__init__)


def test_procedurerangechild_constructor_args():
    sig = inspect.signature(ProcedureRangeChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::verbs::verb_is_not_abstract():
    assert not inspect.isabstract(cobol::verbs::Verb)


def test_cobol::verbs::verb_constructor_exists():
    assert callable(cobol::verbs::Verb.__init__)


def test_cobol::verbs::verb_constructor_args():
    sig = inspect.signature(cobol::verbs::Verb.__init__)
    params = list(sig.parameters.keys())



def test_verb_is_not_abstract():
    assert not inspect.isabstract(Verb)


def test_verb_constructor_exists():
    assert callable(Verb.__init__)


def test_verb_constructor_args():
    sig = inspect.signature(Verb.__init__)
    params = list(sig.parameters.keys())



def test_cobol::verbs::is_is_not_abstract():
    assert not inspect.isabstract(cobol::verbs::Is)


def test_cobol::verbs::is_constructor_exists():
    assert callable(cobol::verbs::Is.__init__)


def test_cobol::verbs::is_constructor_args():
    sig = inspect.signature(cobol::verbs::Is.__init__)
    params = list(sig.parameters.keys())



def test_declarativesection_is_not_abstract():
    assert not inspect.isabstract(DeclarativeSection)


def test_declarativesection_constructor_exists():
    assert callable(DeclarativeSection.__init__)


def test_declarativesection_constructor_args():
    sig = inspect.signature(DeclarativeSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol::declaratives::declaratives_is_not_abstract():
    assert not inspect.isabstract(cobol::declaratives::Declaratives)


def test_cobol::declaratives::declaratives_constructor_exists():
    assert callable(cobol::declaratives::Declaratives.__init__)


def test_cobol::declaratives::declaratives_constructor_args():
    sig = inspect.signature(cobol::declaratives::Declaratives.__init__)
    params = list(sig.parameters.keys())



def test_cobol::labels::procedurelabel_is_not_abstract():
    assert not inspect.isabstract(cobol::labels::ProcedureLabel)


def test_cobol::labels::procedurelabel_constructor_exists():
    assert callable(cobol::labels::ProcedureLabel.__init__)


def test_cobol::labels::procedurelabel_constructor_args():
    sig = inspect.signature(cobol::labels::ProcedureLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol::files::filestatus_is_not_abstract():
    assert not inspect.isabstract(cobol::files::FileStatus)


def test_cobol::files::filestatus_constructor_exists():
    assert callable(cobol::files::FileStatus.__init__)


def test_cobol::files::filestatus_constructor_args():
    sig = inspect.signature(cobol::files::FileStatus.__init__)
    params = list(sig.parameters.keys())



def test_filestatus_is_not_abstract():
    assert not inspect.isabstract(FileStatus)


def test_filestatus_constructor_exists():
    assert callable(FileStatus.__init__)


def test_filestatus_constructor_args():
    sig = inspect.signature(FileStatus.__init__)
    params = list(sig.parameters.keys())



def test_cobol::tables::tabledimension_is_not_abstract():
    assert not inspect.isabstract(cobol::tables::TableDimension)


def test_cobol::tables::tabledimension_constructor_exists():
    assert callable(cobol::tables::TableDimension.__init__)


def test_cobol::tables::tabledimension_constructor_args():
    sig = inspect.signature(cobol::tables::TableDimension.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::tables::tabledimension_has_value():
    assert hasattr(cobol::tables::TableDimension, "value")
    descriptor = None
    for klass in cobol::tables::TableDimension.__mro__:
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



def test_cobol::parameters::byreferenceparameter_is_not_abstract():
    assert not inspect.isabstract(cobol::parameters::ByReferenceParameter)


def test_cobol::parameters::byreferenceparameter_constructor_exists():
    assert callable(cobol::parameters::ByReferenceParameter.__init__)


def test_cobol::parameters::byreferenceparameter_constructor_args():
    sig = inspect.signature(cobol::parameters::ByReferenceParameter.__init__)
    params = list(sig.parameters.keys())



def test_cobol::parameters::byvalueparameter_is_not_abstract():
    assert not inspect.isabstract(cobol::parameters::ByValueParameter)


def test_cobol::parameters::byvalueparameter_constructor_exists():
    assert callable(cobol::parameters::ByValueParameter.__init__)


def test_cobol::parameters::byvalueparameter_constructor_args():
    sig = inspect.signature(cobol::parameters::ByValueParameter.__init__)
    params = list(sig.parameters.keys())



def test_cobol::parameters::parametrizable_is_not_abstract():
    assert not inspect.isabstract(cobol::parameters::Parametrizable)


def test_cobol::parameters::parametrizable_constructor_exists():
    assert callable(cobol::parameters::Parametrizable.__init__)


def test_cobol::parameters::parametrizable_constructor_args():
    sig = inspect.signature(cobol::parameters::Parametrizable.__init__)
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



def test_dataitems::dataitem_is_not_abstract():
    assert not inspect.isabstract(dataitems::DataItem)


def test_dataitems::dataitem_constructor_exists():
    assert callable(dataitems::DataItem.__init__)


def test_dataitems::dataitem_constructor_args():
    sig = inspect.signature(dataitems::DataItem.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::specialnamestatement_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::SpecialNameStatement)


def test_cobol::specialnames::specialnamestatement_constructor_exists():
    assert callable(cobol::specialnames::SpecialNameStatement.__init__)


def test_cobol::specialnames::specialnamestatement_constructor_args():
    sig = inspect.signature(cobol::specialnames::SpecialNameStatement.__init__)
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



def test_cobol::specialnames::symboliccharacter_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::SymbolicCharacter)


def test_cobol::specialnames::symboliccharacter_constructor_exists():
    assert callable(cobol::specialnames::SymbolicCharacter.__init__)


def test_cobol::specialnames::symboliccharacter_constructor_args():
    sig = inspect.signature(cobol::specialnames::SymbolicCharacter.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::mnemonicname_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::MnemonicName)


def test_cobol::specialnames::mnemonicname_constructor_exists():
    assert callable(cobol::specialnames::MnemonicName.__init__)


def test_cobol::specialnames::mnemonicname_constructor_args():
    sig = inspect.signature(cobol::specialnames::MnemonicName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::tables::keyname_is_not_abstract():
    assert not inspect.isabstract(cobol::tables::KeyName)


def test_cobol::tables::keyname_constructor_exists():
    assert callable(cobol::tables::KeyName.__init__)


def test_cobol::tables::keyname_constructor_args():
    sig = inspect.signature(cobol::tables::KeyName.__init__)
    params = list(sig.parameters.keys())
    assert "keyOrder" in params, "Missing parameter 'keyOrder'"

def test_cobol::tables::keyname_has_keyOrder():
    assert hasattr(cobol::tables::KeyName, "keyOrder")
    descriptor = None
    for klass in cobol::tables::KeyName.__mro__:
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



def test_cobol::specialnames::alphabettype_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::AlphabetType)


def test_cobol::specialnames::alphabettype_constructor_exists():
    assert callable(cobol::specialnames::AlphabetType.__init__)


def test_cobol::specialnames::alphabettype_constructor_args():
    sig = inspect.signature(cobol::specialnames::AlphabetType.__init__)
    params = list(sig.parameters.keys())



def test_specialnames::mnemonicname_is_not_abstract():
    assert not inspect.isabstract(specialnames::MnemonicName)


def test_specialnames::mnemonicname_constructor_exists():
    assert callable(specialnames::MnemonicName.__init__)


def test_specialnames::mnemonicname_constructor_args():
    sig = inspect.signature(specialnames::MnemonicName.__init__)
    params = list(sig.parameters.keys())



def test_alphabettype_is_not_abstract():
    assert not inspect.isabstract(AlphabetType)


def test_alphabettype_constructor_exists():
    assert callable(AlphabetType.__init__)


def test_alphabettype_constructor_args():
    sig = inspect.signature(AlphabetType.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::codenamealphabettype_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::CodeNameAlphabetType)


def test_cobol::specialnames::codenamealphabettype_constructor_exists():
    assert callable(cobol::specialnames::CodeNameAlphabetType.__init__)


def test_cobol::specialnames::codenamealphabettype_constructor_args():
    sig = inspect.signature(cobol::specialnames::CodeNameAlphabetType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::specialnames::codenamealphabettype_has_value():
    assert hasattr(cobol::specialnames::CodeNameAlphabetType, "value")
    descriptor = None
    for klass in cobol::specialnames::CodeNameAlphabetType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::specialnames::predefinedalphabettype_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::PredefinedAlphabetType)


def test_cobol::specialnames::predefinedalphabettype_constructor_exists():
    assert callable(cobol::specialnames::PredefinedAlphabetType.__init__)


def test_cobol::specialnames::predefinedalphabettype_constructor_args():
    sig = inspect.signature(cobol::specialnames::PredefinedAlphabetType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::specialnames::predefinedalphabettype_has_value():
    assert hasattr(cobol::specialnames::PredefinedAlphabetType, "value")
    descriptor = None
    for klass in cobol::specialnames::PredefinedAlphabetType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_specialnames::specialnamestatement_is_not_abstract():
    assert not inspect.isabstract(specialnames::SpecialNameStatement)


def test_specialnames::specialnamestatement_constructor_exists():
    assert callable(specialnames::SpecialNameStatement.__init__)


def test_specialnames::specialnamestatement_constructor_args():
    sig = inspect.signature(specialnames::SpecialNameStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::upsiswitchis_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::UPSISwitchIs)


def test_cobol::specialnames::upsiswitchis_constructor_exists():
    assert callable(cobol::specialnames::UPSISwitchIs.__init__)


def test_cobol::specialnames::upsiswitchis_constructor_args():
    sig = inspect.signature(cobol::specialnames::UPSISwitchIs.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::systemdeviceis_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::SystemDeviceIs)


def test_cobol::specialnames::systemdeviceis_constructor_exists():
    assert callable(cobol::specialnames::SystemDeviceIs.__init__)


def test_cobol::specialnames::systemdeviceis_constructor_args():
    sig = inspect.signature(cobol::specialnames::SystemDeviceIs.__init__)
    params = list(sig.parameters.keys())



def test_conditionname_is_not_abstract():
    assert not inspect.isabstract(ConditionName)


def test_conditionname_constructor_exists():
    assert callable(ConditionName.__init__)


def test_conditionname_constructor_args():
    sig = inspect.signature(ConditionName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::offstatus_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::OffStatus)


def test_cobol::specialnames::offstatus_constructor_exists():
    assert callable(cobol::specialnames::OffStatus.__init__)


def test_cobol::specialnames::offstatus_constructor_args():
    sig = inspect.signature(cobol::specialnames::OffStatus.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::onstatus_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::OnStatus)


def test_cobol::specialnames::onstatus_constructor_exists():
    assert callable(cobol::specialnames::OnStatus.__init__)


def test_cobol::specialnames::onstatus_constructor_args():
    sig = inspect.signature(cobol::specialnames::OnStatus.__init__)
    params = list(sig.parameters.keys())



def test_specialnames::specialname_is_not_abstract():
    assert not inspect.isabstract(specialnames::SpecialName)


def test_specialnames::specialname_constructor_exists():
    assert callable(specialnames::SpecialName.__init__)


def test_specialnames::specialname_constructor_args():
    sig = inspect.signature(specialnames::SpecialName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::currencysign_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::CurrencySign)


def test_cobol::specialnames::currencysign_constructor_exists():
    assert callable(cobol::specialnames::CurrencySign.__init__)


def test_cobol::specialnames::currencysign_constructor_args():
    sig = inspect.signature(cobol::specialnames::CurrencySign.__init__)
    params = list(sig.parameters.keys())
    assert "pictureSymbol" in params, "Missing parameter 'pictureSymbol'"

def test_cobol::specialnames::currencysign_has_pictureSymbol():
    assert hasattr(cobol::specialnames::CurrencySign, "pictureSymbol")
    descriptor = None
    for klass in cobol::specialnames::CurrencySign.__mro__:
        if "pictureSymbol" in klass.__dict__:
            descriptor = klass.__dict__["pictureSymbol"]
            break
    assert isinstance(descriptor, property)



def test_cobol::specialnames::classname_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::ClassName)


def test_cobol::specialnames::classname_constructor_exists():
    assert callable(cobol::specialnames::ClassName.__init__)


def test_cobol::specialnames::classname_constructor_args():
    sig = inspect.signature(cobol::specialnames::ClassName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::alphabetname_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::AlphabetName)


def test_cobol::specialnames::alphabetname_constructor_exists():
    assert callable(cobol::specialnames::AlphabetName.__init__)


def test_cobol::specialnames::alphabetname_constructor_args():
    sig = inspect.signature(cobol::specialnames::AlphabetName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::explicitalphabettype_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::ExplicitAlphabetType)


def test_cobol::specialnames::explicitalphabettype_constructor_exists():
    assert callable(cobol::specialnames::ExplicitAlphabetType.__init__)


def test_cobol::specialnames::explicitalphabettype_constructor_args():
    sig = inspect.signature(cobol::specialnames::ExplicitAlphabetType.__init__)
    params = list(sig.parameters.keys())



def test_references::referenceableelement_is_not_abstract():
    assert not inspect.isabstract(references::ReferenceableElement)


def test_references::referenceableelement_constructor_exists():
    assert callable(references::ReferenceableElement.__init__)


def test_references::referenceableelement_constructor_args():
    sig = inspect.signature(references::ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::dataitemattribute_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::DataItemAttribute)


def test_cobol::dataitems::dataitemattribute_constructor_exists():
    assert callable(cobol::dataitems::DataItemAttribute.__init__)


def test_cobol::dataitems::dataitemattribute_constructor_args():
    sig = inspect.signature(cobol::dataitems::DataItemAttribute.__init__)
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



def test_cobol::dataitems::renamingdataname_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::RenamingDataName)


def test_cobol::dataitems::renamingdataname_constructor_exists():
    assert callable(cobol::dataitems::RenamingDataName.__init__)


def test_cobol::dataitems::renamingdataname_constructor_args():
    sig = inspect.signature(cobol::dataitems::RenamingDataName.__init__)
    params = list(sig.parameters.keys())



def test_dataitemattribute_is_not_abstract():
    assert not inspect.isabstract(DataItemAttribute)


def test_dataitemattribute_constructor_exists():
    assert callable(DataItemAttribute.__init__)


def test_dataitemattribute_constructor_args():
    sig = inspect.signature(DataItemAttribute.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::redefines_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::Redefines)


def test_cobol::dataitems::redefines_constructor_exists():
    assert callable(cobol::dataitems::Redefines.__init__)


def test_cobol::dataitems::redefines_constructor_args():
    sig = inspect.signature(cobol::dataitems::Redefines.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::usage_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::Usage)


def test_cobol::dataitems::usage_constructor_exists():
    assert callable(cobol::dataitems::Usage.__init__)


def test_cobol::dataitems::usage_constructor_args():
    sig = inspect.signature(cobol::dataitems::Usage.__init__)
    params = list(sig.parameters.keys())
    assert "usage" in params, "Missing parameter 'usage'"
    assert "isNative" in params, "Missing parameter 'isNative'"

def test_cobol::dataitems::usage_has_usage():
    assert hasattr(cobol::dataitems::Usage, "usage")
    descriptor = None
    for klass in cobol::dataitems::Usage.__mro__:
        if "usage" in klass.__dict__:
            descriptor = klass.__dict__["usage"]
            break
    assert isinstance(descriptor, property)

def test_cobol::dataitems::usage_has_isNative():
    assert hasattr(cobol::dataitems::Usage, "isNative")
    descriptor = None
    for klass in cobol::dataitems::Usage.__mro__:
        if "isNative" in klass.__dict__:
            descriptor = klass.__dict__["isNative"]
            break
    assert isinstance(descriptor, property)



def test_cobol::dataitems::value_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::Value)


def test_cobol::dataitems::value_constructor_exists():
    assert callable(cobol::dataitems::Value.__init__)


def test_cobol::dataitems::value_constructor_args():
    sig = inspect.signature(cobol::dataitems::Value.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::external_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::External)


def test_cobol::dataitems::external_constructor_exists():
    assert callable(cobol::dataitems::External.__init__)


def test_cobol::dataitems::external_constructor_args():
    sig = inspect.signature(cobol::dataitems::External.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::groupusage_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::GroupUsage)


def test_cobol::dataitems::groupusage_constructor_exists():
    assert callable(cobol::dataitems::GroupUsage.__init__)


def test_cobol::dataitems::groupusage_constructor_args():
    sig = inspect.signature(cobol::dataitems::GroupUsage.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::global_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::Global)


def test_cobol::dataitems::global_constructor_exists():
    assert callable(cobol::dataitems::Global.__init__)


def test_cobol::dataitems::global_constructor_args():
    sig = inspect.signature(cobol::dataitems::Global.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::picturestring_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::PictureString)


def test_cobol::dataitems::picturestring_constructor_exists():
    assert callable(cobol::dataitems::PictureString.__init__)


def test_cobol::dataitems::picturestring_constructor_args():
    sig = inspect.signature(cobol::dataitems::PictureString.__init__)
    params = list(sig.parameters.keys())
    assert "picture" in params, "Missing parameter 'picture'"

def test_cobol::dataitems::picturestring_has_picture():
    assert hasattr(cobol::dataitems::PictureString, "picture")
    descriptor = None
    for klass in cobol::dataitems::PictureString.__mro__:
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



def test_cobol::environments::advancedfunctionprinting_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::AdvancedFunctionPrinting)


def test_cobol::environments::advancedfunctionprinting_constructor_exists():
    assert callable(cobol::environments::AdvancedFunctionPrinting.__init__)


def test_cobol::environments::advancedfunctionprinting_constructor_args():
    sig = inspect.signature(cobol::environments::AdvancedFunctionPrinting.__init__)
    params = list(sig.parameters.keys())



def test_cobol::environments::pocket_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::Pocket)


def test_cobol::environments::pocket_constructor_exists():
    assert callable(cobol::environments::Pocket.__init__)


def test_cobol::environments::pocket_constructor_args():
    sig = inspect.signature(cobol::environments::Pocket.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::environments::pocket_has_value():
    assert hasattr(cobol::environments::Pocket, "value")
    descriptor = None
    for klass in cobol::environments::Pocket.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::environments::suppressspacing_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::SuppressSpacing)


def test_cobol::environments::suppressspacing_constructor_exists():
    assert callable(cobol::environments::SuppressSpacing.__init__)


def test_cobol::environments::suppressspacing_constructor_args():
    sig = inspect.signature(cobol::environments::SuppressSpacing.__init__)
    params = list(sig.parameters.keys())



def test_cobol::environments::systemlogicaloutput_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::SystemLogicalOutput)


def test_cobol::environments::systemlogicaloutput_constructor_exists():
    assert callable(cobol::environments::SystemLogicalOutput.__init__)


def test_cobol::environments::systemlogicaloutput_constructor_args():
    sig = inspect.signature(cobol::environments::SystemLogicalOutput.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::environments::systemlogicaloutput_has_value():
    assert hasattr(cobol::environments::SystemLogicalOutput, "value")
    descriptor = None
    for klass in cobol::environments::SystemLogicalOutput.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::environments::systempunchdevice_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::SystemPunchDevice)


def test_cobol::environments::systempunchdevice_constructor_exists():
    assert callable(cobol::environments::SystemPunchDevice.__init__)


def test_cobol::environments::systempunchdevice_constructor_args():
    sig = inspect.signature(cobol::environments::SystemPunchDevice.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::environments::systempunchdevice_has_value():
    assert hasattr(cobol::environments::SystemPunchDevice, "value")
    descriptor = None
    for klass in cobol::environments::SystemPunchDevice.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::environments::console_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::Console)


def test_cobol::environments::console_constructor_exists():
    assert callable(cobol::environments::Console.__init__)


def test_cobol::environments::console_constructor_args():
    sig = inspect.signature(cobol::environments::Console.__init__)
    params = list(sig.parameters.keys())



def test_cobol::environments::channel_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::Channel)


def test_cobol::environments::channel_constructor_exists():
    assert callable(cobol::environments::Channel.__init__)


def test_cobol::environments::channel_constructor_args():
    sig = inspect.signature(cobol::environments::Channel.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::environments::channel_has_value():
    assert hasattr(cobol::environments::Channel, "value")
    descriptor = None
    for klass in cobol::environments::Channel.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::environments::systemlogicalinput_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::SystemLogicalInput)


def test_cobol::environments::systemlogicalinput_constructor_exists():
    assert callable(cobol::environments::SystemLogicalInput.__init__)


def test_cobol::environments::systemlogicalinput_constructor_args():
    sig = inspect.signature(cobol::environments::SystemLogicalInput.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::environments::systemlogicalinput_has_value():
    assert hasattr(cobol::environments::SystemLogicalInput, "value")
    descriptor = None
    for klass in cobol::environments::SystemLogicalInput.__mro__:
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



def test_cobol::registers::addressof_is_not_abstract():
    assert not inspect.isabstract(cobol::registers::AddressOf)


def test_cobol::registers::addressof_constructor_exists():
    assert callable(cobol::registers::AddressOf.__init__)


def test_cobol::registers::addressof_constructor_args():
    sig = inspect.signature(cobol::registers::AddressOf.__init__)
    params = list(sig.parameters.keys())



def test_cobol::registers::whencompiled_is_not_abstract():
    assert not inspect.isabstract(cobol::registers::WhenCompiled)


def test_cobol::registers::whencompiled_constructor_exists():
    assert callable(cobol::registers::WhenCompiled.__init__)


def test_cobol::registers::whencompiled_constructor_args():
    sig = inspect.signature(cobol::registers::WhenCompiled.__init__)
    params = list(sig.parameters.keys())



def test_cobol::registers::shiftout_is_not_abstract():
    assert not inspect.isabstract(cobol::registers::ShiftOut)


def test_cobol::registers::shiftout_constructor_exists():
    assert callable(cobol::registers::ShiftOut.__init__)


def test_cobol::registers::shiftout_constructor_args():
    sig = inspect.signature(cobol::registers::ShiftOut.__init__)
    params = list(sig.parameters.keys())



def test_cobol::registers::returncode_is_not_abstract():
    assert not inspect.isabstract(cobol::registers::ReturnCode)


def test_cobol::registers::returncode_constructor_exists():
    assert callable(cobol::registers::ReturnCode.__init__)


def test_cobol::registers::returncode_constructor_args():
    sig = inspect.signature(cobol::registers::ReturnCode.__init__)
    params = list(sig.parameters.keys())



def test_cobol::registers::lengthof_is_not_abstract():
    assert not inspect.isabstract(cobol::registers::LengthOf)


def test_cobol::registers::lengthof_constructor_exists():
    assert callable(cobol::registers::LengthOf.__init__)


def test_cobol::registers::lengthof_constructor_args():
    sig = inspect.signature(cobol::registers::LengthOf.__init__)
    params = list(sig.parameters.keys())



def test_cobol::registers::shiftin_is_not_abstract():
    assert not inspect.isabstract(cobol::registers::ShiftIn)


def test_cobol::registers::shiftin_constructor_exists():
    assert callable(cobol::registers::ShiftIn.__init__)


def test_cobol::registers::shiftin_constructor_args():
    sig = inspect.signature(cobol::registers::ShiftIn.__init__)
    params = list(sig.parameters.keys())



def test_sortphrasewater_is_not_abstract():
    assert not inspect.isabstract(SortPhraseWater)


def test_sortphrasewater_constructor_exists():
    assert callable(SortPhraseWater.__init__)


def test_sortphrasewater_constructor_args():
    sig = inspect.signature(SortPhraseWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::sortphrasetoken_is_not_abstract():
    assert not inspect.isabstract(cobol::water::SortPhraseToken)


def test_cobol::water::sortphrasetoken_constructor_exists():
    assert callable(cobol::water::SortPhraseToken.__init__)


def test_cobol::water::sortphrasetoken_constructor_args():
    sig = inspect.signature(cobol::water::SortPhraseToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::sortphrasetoken_has_value():
    assert hasattr(cobol::water::SortPhraseToken, "value")
    descriptor = None
    for klass in cobol::water::SortPhraseToken.__mro__:
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



def test_cobol::water::openstatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol::water::OpenStatementToken)


def test_cobol::water::openstatementtoken_constructor_exists():
    assert callable(cobol::water::OpenStatementToken.__init__)


def test_cobol::water::openstatementtoken_constructor_args():
    sig = inspect.signature(cobol::water::OpenStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::openstatementtoken_has_value():
    assert hasattr(cobol::water::OpenStatementToken, "value")
    descriptor = None
    for klass in cobol::water::OpenStatementToken.__mro__:
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



def test_cobol::water::invokestatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol::water::InvokeStatementToken)


def test_cobol::water::invokestatementtoken_constructor_exists():
    assert callable(cobol::water::InvokeStatementToken.__init__)


def test_cobol::water::invokestatementtoken_constructor_args():
    sig = inspect.signature(cobol::water::InvokeStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::invokestatementtoken_has_value():
    assert hasattr(cobol::water::InvokeStatementToken, "value")
    descriptor = None
    for klass in cobol::water::InvokeStatementToken.__mro__:
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



def test_cobol::water::closestatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol::water::CloseStatementToken)


def test_cobol::water::closestatementtoken_constructor_exists():
    assert callable(cobol::water::CloseStatementToken.__init__)


def test_cobol::water::closestatementtoken_constructor_args():
    sig = inspect.signature(cobol::water::CloseStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::closestatementtoken_has_value():
    assert hasattr(cobol::water::CloseStatementToken, "value")
    descriptor = None
    for klass in cobol::water::CloseStatementToken.__mro__:
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



def test_cobol::water::usestatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol::water::UseStatementToken)


def test_cobol::water::usestatementtoken_constructor_exists():
    assert callable(cobol::water::UseStatementToken.__init__)


def test_cobol::water::usestatementtoken_constructor_args():
    sig = inspect.signature(cobol::water::UseStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::usestatementtoken_has_value():
    assert hasattr(cobol::water::UseStatementToken, "value")
    descriptor = None
    for klass in cobol::water::UseStatementToken.__mro__:
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



def test_cobol::environments::environment_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::Environment)


def test_cobol::environments::environment_constructor_exists():
    assert callable(cobol::environments::Environment.__init__)


def test_cobol::environments::environment_constructor_args():
    sig = inspect.signature(cobol::environments::Environment.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::acceptstatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol::water::AcceptStatementToken)


def test_cobol::water::acceptstatementtoken_constructor_exists():
    assert callable(cobol::water::AcceptStatementToken.__init__)


def test_cobol::water::acceptstatementtoken_constructor_args():
    sig = inspect.signature(cobol::water::AcceptStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::acceptstatementtoken_has_value():
    assert hasattr(cobol::water::AcceptStatementToken, "value")
    descriptor = None
    for klass in cobol::water::AcceptStatementToken.__mro__:
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



def test_cobol::water::cicsstatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol::water::CICSStatementToken)


def test_cobol::water::cicsstatementtoken_constructor_exists():
    assert callable(cobol::water::CICSStatementToken.__init__)


def test_cobol::water::cicsstatementtoken_constructor_args():
    sig = inspect.signature(cobol::water::CICSStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::cicsstatementtoken_has_value():
    assert hasattr(cobol::water::CICSStatementToken, "value")
    descriptor = None
    for klass in cobol::water::CICSStatementToken.__mro__:
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



def test_cobol::water::sqlstatementtoken_is_not_abstract():
    assert not inspect.isabstract(cobol::water::SQLStatementToken)


def test_cobol::water::sqlstatementtoken_constructor_exists():
    assert callable(cobol::water::SQLStatementToken.__init__)


def test_cobol::water::sqlstatementtoken_constructor_args():
    sig = inspect.signature(cobol::water::SQLStatementToken.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::sqlstatementtoken_has_value():
    assert hasattr(cobol::water::SQLStatementToken, "value")
    descriptor = None
    for klass in cobol::water::SQLStatementToken.__mro__:
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



def test_cobol::water::repositorydescription_is_not_abstract():
    assert not inspect.isabstract(cobol::water::RepositoryDescription)


def test_cobol::water::repositorydescription_constructor_exists():
    assert callable(cobol::water::RepositoryDescription.__init__)


def test_cobol::water::repositorydescription_constructor_args():
    sig = inspect.signature(cobol::water::RepositoryDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::repositorydescription_has_value():
    assert hasattr(cobol::water::RepositoryDescription, "value")
    descriptor = None
    for klass in cobol::water::RepositoryDescription.__mro__:
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



def test_cobol::water::iocontroldescription_is_not_abstract():
    assert not inspect.isabstract(cobol::water::IOControlDescription)


def test_cobol::water::iocontroldescription_constructor_exists():
    assert callable(cobol::water::IOControlDescription.__init__)


def test_cobol::water::iocontroldescription_constructor_args():
    sig = inspect.signature(cobol::water::IOControlDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::iocontroldescription_has_value():
    assert hasattr(cobol::water::IOControlDescription, "value")
    descriptor = None
    for klass in cobol::water::IOControlDescription.__mro__:
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



def test_cobol::water::datadescription_is_not_abstract():
    assert not inspect.isabstract(cobol::water::DataDescription)


def test_cobol::water::datadescription_constructor_exists():
    assert callable(cobol::water::DataDescription.__init__)


def test_cobol::water::datadescription_constructor_args():
    sig = inspect.signature(cobol::water::DataDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::datadescription_has_value():
    assert hasattr(cobol::water::DataDescription, "value")
    descriptor = None
    for klass in cobol::water::DataDescription.__mro__:
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



def test_cobol::water::filedescription_is_not_abstract():
    assert not inspect.isabstract(cobol::water::FileDescription)


def test_cobol::water::filedescription_constructor_exists():
    assert callable(cobol::water::FileDescription.__init__)


def test_cobol::water::filedescription_constructor_args():
    sig = inspect.signature(cobol::water::FileDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::filedescription_has_value():
    assert hasattr(cobol::water::FileDescription, "value")
    descriptor = None
    for klass in cobol::water::FileDescription.__mro__:
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



def test_cobol::water::selectstatementclause_is_not_abstract():
    assert not inspect.isabstract(cobol::water::SelectStatementClause)


def test_cobol::water::selectstatementclause_constructor_exists():
    assert callable(cobol::water::SelectStatementClause.__init__)


def test_cobol::water::selectstatementclause_constructor_args():
    sig = inspect.signature(cobol::water::SelectStatementClause.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::selectstatementclause_has_value():
    assert hasattr(cobol::water::SelectStatementClause, "value")
    descriptor = None
    for klass in cobol::water::SelectStatementClause.__mro__:
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



def test_cobol::water::prioritynumber_is_not_abstract():
    assert not inspect.isabstract(cobol::water::PriorityNumber)


def test_cobol::water::prioritynumber_constructor_exists():
    assert callable(cobol::water::PriorityNumber.__init__)


def test_cobol::water::prioritynumber_constructor_args():
    sig = inspect.signature(cobol::water::PriorityNumber.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::prioritynumber_has_value():
    assert hasattr(cobol::water::PriorityNumber, "value")
    descriptor = None
    for klass in cobol::water::PriorityNumber.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::water::objectcomputerdescription_is_not_abstract():
    assert not inspect.isabstract(cobol::water::ObjectComputerDescription)


def test_cobol::water::objectcomputerdescription_constructor_exists():
    assert callable(cobol::water::ObjectComputerDescription.__init__)


def test_cobol::water::objectcomputerdescription_constructor_args():
    sig = inspect.signature(cobol::water::ObjectComputerDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::objectcomputerdescription_has_value():
    assert hasattr(cobol::water::ObjectComputerDescription, "value")
    descriptor = None
    for klass in cobol::water::ObjectComputerDescription.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::water::water_is_not_abstract():
    assert not inspect.isabstract(cobol::water::Water)


def test_cobol::water::water_constructor_exists():
    assert callable(cobol::water::Water.__init__)


def test_cobol::water::water_constructor_args():
    sig = inspect.signature(cobol::water::Water.__init__)
    params = list(sig.parameters.keys())



def test_water_is_not_abstract():
    assert not inspect.isabstract(Water)


def test_water_constructor_exists():
    assert callable(Water.__init__)


def test_water_constructor_args():
    sig = inspect.signature(Water.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::specialnamesparagraphwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::SpecialNamesParagraphWater)


def test_cobol::water::specialnamesparagraphwater_constructor_exists():
    assert callable(cobol::water::SpecialNamesParagraphWater.__init__)


def test_cobol::water::specialnamesparagraphwater_constructor_args():
    sig = inspect.signature(cobol::water::SpecialNamesParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::selectstatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::SelectStatementWater)


def test_cobol::water::selectstatementwater_constructor_exists():
    assert callable(cobol::water::SelectStatementWater.__init__)


def test_cobol::water::selectstatementwater_constructor_args():
    sig = inspect.signature(cobol::water::SelectStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::filedescriptorwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::FileDescriptorWater)


def test_cobol::water::filedescriptorwater_constructor_exists():
    assert callable(cobol::water::FileDescriptorWater.__init__)


def test_cobol::water::filedescriptorwater_constructor_args():
    sig = inspect.signature(cobol::water::FileDescriptorWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::cicsstatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::CICSStatementWater)


def test_cobol::water::cicsstatementwater_constructor_exists():
    assert callable(cobol::water::CICSStatementWater.__init__)


def test_cobol::water::cicsstatementwater_constructor_args():
    sig = inspect.signature(cobol::water::CICSStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::repositoryparagraphwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::RepositoryParagraphWater)


def test_cobol::water::repositoryparagraphwater_constructor_exists():
    assert callable(cobol::water::RepositoryParagraphWater.__init__)


def test_cobol::water::repositoryparagraphwater_constructor_args():
    sig = inspect.signature(cobol::water::RepositoryParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::invokestatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::InvokeStatementWater)


def test_cobol::water::invokestatementwater_constructor_exists():
    assert callable(cobol::water::InvokeStatementWater.__init__)


def test_cobol::water::invokestatementwater_constructor_args():
    sig = inspect.signature(cobol::water::InvokeStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::objectcomputerparagraphwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::ObjectComputerParagraphWater)


def test_cobol::water::objectcomputerparagraphwater_constructor_exists():
    assert callable(cobol::water::ObjectComputerParagraphWater.__init__)


def test_cobol::water::objectcomputerparagraphwater_constructor_args():
    sig = inspect.signature(cobol::water::ObjectComputerParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::datadescriptorwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::DataDescriptorWater)


def test_cobol::water::datadescriptorwater_constructor_exists():
    assert callable(cobol::water::DataDescriptorWater.__init__)


def test_cobol::water::datadescriptorwater_constructor_args():
    sig = inspect.signature(cobol::water::DataDescriptorWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::closestatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::CloseStatementWater)


def test_cobol::water::closestatementwater_constructor_exists():
    assert callable(cobol::water::CloseStatementWater.__init__)


def test_cobol::water::closestatementwater_constructor_args():
    sig = inspect.signature(cobol::water::CloseStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::openstatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::OpenStatementWater)


def test_cobol::water::openstatementwater_constructor_exists():
    assert callable(cobol::water::OpenStatementWater.__init__)


def test_cobol::water::openstatementwater_constructor_args():
    sig = inspect.signature(cobol::water::OpenStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::acceptstatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::AcceptStatementWater)


def test_cobol::water::acceptstatementwater_constructor_exists():
    assert callable(cobol::water::AcceptStatementWater.__init__)


def test_cobol::water::acceptstatementwater_constructor_args():
    sig = inspect.signature(cobol::water::AcceptStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::sqlstatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::SQLStatementWater)


def test_cobol::water::sqlstatementwater_constructor_exists():
    assert callable(cobol::water::SQLStatementWater.__init__)


def test_cobol::water::sqlstatementwater_constructor_args():
    sig = inspect.signature(cobol::water::SQLStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::identificationdivisionwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::IdentificationDivisionWater)


def test_cobol::water::identificationdivisionwater_constructor_exists():
    assert callable(cobol::water::IdentificationDivisionWater.__init__)


def test_cobol::water::identificationdivisionwater_constructor_args():
    sig = inspect.signature(cobol::water::IdentificationDivisionWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::sortphrasewater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::SortPhraseWater)


def test_cobol::water::sortphrasewater_constructor_exists():
    assert callable(cobol::water::SortPhraseWater.__init__)


def test_cobol::water::sortphrasewater_constructor_args():
    sig = inspect.signature(cobol::water::SortPhraseWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::usestatementwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::UseStatementWater)


def test_cobol::water::usestatementwater_constructor_exists():
    assert callable(cobol::water::UseStatementWater.__init__)


def test_cobol::water::usestatementwater_constructor_args():
    sig = inspect.signature(cobol::water::UseStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::iocontrolparagraphwater_is_not_abstract():
    assert not inspect.isabstract(cobol::water::IOControlParagraphWater)


def test_cobol::water::iocontrolparagraphwater_constructor_exists():
    assert callable(cobol::water::IOControlParagraphWater.__init__)


def test_cobol::water::iocontrolparagraphwater_constructor_args():
    sig = inspect.signature(cobol::water::IOControlParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::incompleteelement_is_not_abstract():
    assert not inspect.isabstract(cobol::water::IncompleteElement)


def test_cobol::water::incompleteelement_constructor_exists():
    assert callable(cobol::water::IncompleteElement.__init__)


def test_cobol::water::incompleteelement_constructor_args():
    sig = inspect.signature(cobol::water::IncompleteElement.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_cobol::labels::procedurerangelabel_is_not_abstract():
    assert not inspect.isabstract(cobol::labels::ProcedureRangeLabel)


def test_cobol::labels::procedurerangelabel_constructor_exists():
    assert callable(cobol::labels::ProcedureRangeLabel.__init__)


def test_cobol::labels::procedurerangelabel_constructor_args():
    sig = inspect.signature(cobol::labels::ProcedureRangeLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol::labels::stoplabel_is_not_abstract():
    assert not inspect.isabstract(cobol::labels::StopLabel)


def test_cobol::labels::stoplabel_constructor_exists():
    assert callable(cobol::labels::StopLabel.__init__)


def test_cobol::labels::stoplabel_constructor_args():
    sig = inspect.signature(cobol::labels::StopLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol::ios::iodirectives_is_not_abstract():
    assert not inspect.isabstract(cobol::ios::IODirectives)


def test_cobol::ios::iodirectives_constructor_exists():
    assert callable(cobol::ios::IODirectives.__init__)


def test_cobol::ios::iodirectives_constructor_args():
    sig = inspect.signature(cobol::ios::IODirectives.__init__)
    params = list(sig.parameters.keys())



def test_ios::outputdirective_is_not_abstract():
    assert not inspect.isabstract(ios::OutputDirective)


def test_ios::outputdirective_constructor_exists():
    assert callable(ios::OutputDirective.__init__)


def test_ios::outputdirective_constructor_args():
    sig = inspect.signature(ios::OutputDirective.__init__)
    params = list(sig.parameters.keys())



def test_ios::filedirective_is_not_abstract():
    assert not inspect.isabstract(ios::FileDirective)


def test_ios::filedirective_constructor_exists():
    assert callable(ios::FileDirective.__init__)


def test_ios::filedirective_constructor_args():
    sig = inspect.signature(ios::FileDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol::ios::outputfile_is_not_abstract():
    assert not inspect.isabstract(cobol::ios::OutputFile)


def test_cobol::ios::outputfile_constructor_exists():
    assert callable(cobol::ios::OutputFile.__init__)


def test_cobol::ios::outputfile_constructor_args():
    sig = inspect.signature(cobol::ios::OutputFile.__init__)
    params = list(sig.parameters.keys())



def test_iodirectives_is_not_abstract():
    assert not inspect.isabstract(IODirectives)


def test_iodirectives_constructor_exists():
    assert callable(IODirectives.__init__)


def test_iodirectives_constructor_args():
    sig = inspect.signature(IODirectives.__init__)
    params = list(sig.parameters.keys())



def test_cobol::ios::proceduredirective_is_not_abstract():
    assert not inspect.isabstract(cobol::ios::ProcedureDirective)


def test_cobol::ios::proceduredirective_constructor_exists():
    assert callable(cobol::ios::ProcedureDirective.__init__)


def test_cobol::ios::proceduredirective_constructor_args():
    sig = inspect.signature(cobol::ios::ProcedureDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol::ios::filedirective_is_not_abstract():
    assert not inspect.isabstract(cobol::ios::FileDirective)


def test_cobol::ios::filedirective_constructor_exists():
    assert callable(cobol::ios::FileDirective.__init__)


def test_cobol::ios::filedirective_constructor_args():
    sig = inspect.signature(cobol::ios::FileDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol::ios::outputdirective_is_not_abstract():
    assert not inspect.isabstract(cobol::ios::OutputDirective)


def test_cobol::ios::outputdirective_constructor_exists():
    assert callable(cobol::ios::OutputDirective.__init__)


def test_cobol::ios::outputdirective_constructor_args():
    sig = inspect.signature(cobol::ios::OutputDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol::ios::inputdirective_is_not_abstract():
    assert not inspect.isabstract(cobol::ios::InputDirective)


def test_cobol::ios::inputdirective_constructor_exists():
    assert callable(cobol::ios::InputDirective.__init__)


def test_cobol::ios::inputdirective_constructor_args():
    sig = inspect.signature(cobol::ios::InputDirective.__init__)
    params = list(sig.parameters.keys())



def test_ios::proceduredirective_is_not_abstract():
    assert not inspect.isabstract(ios::ProcedureDirective)


def test_ios::proceduredirective_constructor_exists():
    assert callable(ios::ProcedureDirective.__init__)


def test_ios::proceduredirective_constructor_args():
    sig = inspect.signature(ios::ProcedureDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol::ios::outputprocedure_is_not_abstract():
    assert not inspect.isabstract(cobol::ios::OutputProcedure)


def test_cobol::ios::outputprocedure_constructor_exists():
    assert callable(cobol::ios::OutputProcedure.__init__)


def test_cobol::ios::outputprocedure_constructor_args():
    sig = inspect.signature(cobol::ios::OutputProcedure.__init__)
    params = list(sig.parameters.keys())



def test_ios::inputdirective_is_not_abstract():
    assert not inspect.isabstract(ios::InputDirective)


def test_ios::inputdirective_constructor_exists():
    assert callable(ios::InputDirective.__init__)


def test_ios::inputdirective_constructor_args():
    sig = inspect.signature(ios::InputDirective.__init__)
    params = list(sig.parameters.keys())



def test_cobol::ios::inputfile_is_not_abstract():
    assert not inspect.isabstract(cobol::ios::InputFile)


def test_cobol::ios::inputfile_constructor_exists():
    assert callable(cobol::ios::InputFile.__init__)


def test_cobol::ios::inputfile_constructor_args():
    sig = inspect.signature(cobol::ios::InputFile.__init__)
    params = list(sig.parameters.keys())



def test_cobol::ios::inputprocedure_is_not_abstract():
    assert not inspect.isabstract(cobol::ios::InputProcedure)


def test_cobol::ios::inputprocedure_constructor_exists():
    assert callable(cobol::ios::InputProcedure.__init__)


def test_cobol::ios::inputprocedure_constructor_args():
    sig = inspect.signature(cobol::ios::InputProcedure.__init__)
    params = list(sig.parameters.keys())



def test_cobol::identifiers::referencemodifier_is_not_abstract():
    assert not inspect.isabstract(cobol::identifiers::ReferenceModifier)


def test_cobol::identifiers::referencemodifier_constructor_exists():
    assert callable(cobol::identifiers::ReferenceModifier.__init__)


def test_cobol::identifiers::referencemodifier_constructor_args():
    sig = inspect.signature(cobol::identifiers::ReferenceModifier.__init__)
    params = list(sig.parameters.keys())



def test_directsubscript_is_not_abstract():
    assert not inspect.isabstract(DirectSubscript)


def test_directsubscript_constructor_exists():
    assert callable(DirectSubscript.__init__)


def test_directsubscript_constructor_args():
    sig = inspect.signature(DirectSubscript.__init__)
    params = list(sig.parameters.keys())



def test_cobol::identifiers::all_is_not_abstract():
    assert not inspect.isabstract(cobol::identifiers::All)


def test_cobol::identifiers::all_constructor_exists():
    assert callable(cobol::identifiers::All.__init__)


def test_cobol::identifiers::all_constructor_args():
    sig = inspect.signature(cobol::identifiers::All.__init__)
    params = list(sig.parameters.keys())



def test_identificationdivisionwater_is_not_abstract():
    assert not inspect.isabstract(IdentificationDivisionWater)


def test_identificationdivisionwater_constructor_exists():
    assert callable(IdentificationDivisionWater.__init__)


def test_identificationdivisionwater_constructor_args():
    sig = inspect.signature(IdentificationDivisionWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::programdescription_is_not_abstract():
    assert not inspect.isabstract(cobol::water::ProgramDescription)


def test_cobol::water::programdescription_constructor_exists():
    assert callable(cobol::water::ProgramDescription.__init__)


def test_cobol::water::programdescription_constructor_args():
    sig = inspect.signature(cobol::water::ProgramDescription.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::programdescription_has_value():
    assert hasattr(cobol::water::ProgramDescription, "value")
    descriptor = None
    for klass in cobol::water::ProgramDescription.__mro__:
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



def test_cobol::identifiers::directsubscript_is_not_abstract():
    assert not inspect.isabstract(cobol::identifiers::DirectSubscript)


def test_cobol::identifiers::directsubscript_constructor_exists():
    assert callable(cobol::identifiers::DirectSubscript.__init__)


def test_cobol::identifiers::directsubscript_constructor_args():
    sig = inspect.signature(cobol::identifiers::DirectSubscript.__init__)
    params = list(sig.parameters.keys())



def test_cobol::identifiers::relativesubscript_is_not_abstract():
    assert not inspect.isabstract(cobol::identifiers::RelativeSubscript)


def test_cobol::identifiers::relativesubscript_constructor_exists():
    assert callable(cobol::identifiers::RelativeSubscript.__init__)


def test_cobol::identifiers::relativesubscript_constructor_args():
    sig = inspect.signature(cobol::identifiers::RelativeSubscript.__init__)
    params = list(sig.parameters.keys())



def test_identifiers::identifier_is_not_abstract():
    assert not inspect.isabstract(identifiers::Identifier)


def test_identifiers::identifier_constructor_exists():
    assert callable(identifiers::Identifier.__init__)


def test_identifiers::identifier_constructor_args():
    sig = inspect.signature(identifiers::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_referencemodifier_is_not_abstract():
    assert not inspect.isabstract(ReferenceModifier)


def test_referencemodifier_constructor_exists():
    assert callable(ReferenceModifier.__init__)


def test_referencemodifier_constructor_args():
    sig = inspect.signature(ReferenceModifier.__init__)
    params = list(sig.parameters.keys())



def test_water::sortphrasewater_is_not_abstract():
    assert not inspect.isabstract(water::SortPhraseWater)


def test_water::sortphrasewater_constructor_exists():
    assert callable(water::SortPhraseWater.__init__)


def test_water::sortphrasewater_constructor_args():
    sig = inspect.signature(water::SortPhraseWater.__init__)
    params = list(sig.parameters.keys())



def test_water::datadescriptorwater_is_not_abstract():
    assert not inspect.isabstract(water::DataDescriptorWater)


def test_water::datadescriptorwater_constructor_exists():
    assert callable(water::DataDescriptorWater.__init__)


def test_water::datadescriptorwater_constructor_args():
    sig = inspect.signature(water::DataDescriptorWater.__init__)
    params = list(sig.parameters.keys())



def test_water::usestatementwater_is_not_abstract():
    assert not inspect.isabstract(water::UseStatementWater)


def test_water::usestatementwater_constructor_exists():
    assert callable(water::UseStatementWater.__init__)


def test_water::usestatementwater_constructor_args():
    sig = inspect.signature(water::UseStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_water::sqlstatementwater_is_not_abstract():
    assert not inspect.isabstract(water::SQLStatementWater)


def test_water::sqlstatementwater_constructor_exists():
    assert callable(water::SQLStatementWater.__init__)


def test_water::sqlstatementwater_constructor_args():
    sig = inspect.signature(water::SQLStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_water::identificationdivisionwater_is_not_abstract():
    assert not inspect.isabstract(water::IdentificationDivisionWater)


def test_water::identificationdivisionwater_constructor_exists():
    assert callable(water::IdentificationDivisionWater.__init__)


def test_water::identificationdivisionwater_constructor_args():
    sig = inspect.signature(water::IdentificationDivisionWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::dot_is_not_abstract():
    assert not inspect.isabstract(cobol::water::Dot)


def test_cobol::water::dot_constructor_exists():
    assert callable(cobol::water::Dot.__init__)


def test_cobol::water::dot_constructor_args():
    sig = inspect.signature(cobol::water::Dot.__init__)
    params = list(sig.parameters.keys())



def test_water::repositoryparagraphwater_is_not_abstract():
    assert not inspect.isabstract(water::RepositoryParagraphWater)


def test_water::repositoryparagraphwater_constructor_exists():
    assert callable(water::RepositoryParagraphWater.__init__)


def test_water::repositoryparagraphwater_constructor_args():
    sig = inspect.signature(water::RepositoryParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_water::acceptstatementwater_is_not_abstract():
    assert not inspect.isabstract(water::AcceptStatementWater)


def test_water::acceptstatementwater_constructor_exists():
    assert callable(water::AcceptStatementWater.__init__)


def test_water::acceptstatementwater_constructor_args():
    sig = inspect.signature(water::AcceptStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::identifiers::subscript_is_not_abstract():
    assert not inspect.isabstract(cobol::identifiers::Subscript)


def test_cobol::identifiers::subscript_constructor_exists():
    assert callable(cobol::identifiers::Subscript.__init__)


def test_cobol::identifiers::subscript_constructor_args():
    sig = inspect.signature(cobol::identifiers::Subscript.__init__)
    params = list(sig.parameters.keys())



def test_varyinguntilcondition_is_not_abstract():
    assert not inspect.isabstract(VaryingUntilCondition)


def test_varyinguntilcondition_constructor_exists():
    assert callable(VaryingUntilCondition.__init__)


def test_varyinguntilcondition_constructor_args():
    sig = inspect.signature(VaryingUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::afteruntilcondition_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::AfterUntilCondition)


def test_cobol::statements::afteruntilcondition_constructor_exists():
    assert callable(cobol::statements::AfterUntilCondition.__init__)


def test_cobol::statements::afteruntilcondition_constructor_args():
    sig = inspect.signature(cobol::statements::AfterUntilCondition.__init__)
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



def test_cobol::statements::varyinguntilcondition_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::VaryingUntilCondition)


def test_cobol::statements::varyinguntilcondition_constructor_exists():
    assert callable(cobol::statements::VaryingUntilCondition.__init__)


def test_cobol::statements::varyinguntilcondition_constructor_args():
    sig = inspect.signature(cobol::statements::VaryingUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_tallying_is_not_abstract():
    assert not inspect.isabstract(Tallying)


def test_tallying_constructor_exists():
    assert callable(Tallying.__init__)


def test_tallying_constructor_args():
    sig = inspect.signature(Tallying.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::anycharacter_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::AnyCharacter)


def test_cobol::strings::anycharacter_constructor_exists():
    assert callable(cobol::strings::AnyCharacter.__init__)


def test_cobol::strings::anycharacter_constructor_args():
    sig = inspect.signature(cobol::strings::AnyCharacter.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::specificcharacter_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::SpecificCharacter)


def test_cobol::strings::specificcharacter_constructor_exists():
    assert callable(cobol::strings::SpecificCharacter.__init__)


def test_cobol::strings::specificcharacter_constructor_args():
    sig = inspect.signature(cobol::strings::SpecificCharacter.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::tallyingin_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::TallyingIn)


def test_cobol::statements::tallyingin_constructor_exists():
    assert callable(cobol::statements::TallyingIn.__init__)


def test_cobol::statements::tallyingin_constructor_args():
    sig = inspect.signature(cobol::statements::TallyingIn.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::statement_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Statement)


def test_cobol::statements::statement_constructor_exists():
    assert callable(cobol::statements::Statement.__init__)


def test_cobol::statements::statement_constructor_args():
    sig = inspect.signature(cobol::statements::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "endVerb" in params, "Missing parameter 'endVerb'"

def test_cobol::statements::statement_has_endVerb():
    assert hasattr(cobol::statements::Statement, "endVerb")
    descriptor = None
    for klass in cobol::statements::Statement.__mro__:
        if "endVerb" in klass.__dict__:
            descriptor = klass.__dict__["endVerb"]
            break
    assert isinstance(descriptor, property)



def test_cobol::operands::operand_is_not_abstract():
    assert not inspect.isabstract(cobol::operands::Operand)


def test_cobol::operands::operand_constructor_exists():
    assert callable(cobol::operands::Operand.__init__)


def test_cobol::operands::operand_constructor_args():
    sig = inspect.signature(cobol::operands::Operand.__init__)
    params = list(sig.parameters.keys())



def test_replacementoperand_is_not_abstract():
    assert not inspect.isabstract(ReplacementOperand)


def test_replacementoperand_constructor_exists():
    assert callable(ReplacementOperand.__init__)


def test_replacementoperand_constructor_args():
    sig = inspect.signature(ReplacementOperand.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operands::encoding_is_not_abstract():
    assert not inspect.isabstract(cobol::operands::Encoding)


def test_cobol::operands::encoding_constructor_exists():
    assert callable(cobol::operands::Encoding.__init__)


def test_cobol::operands::encoding_constructor_args():
    sig = inspect.signature(cobol::operands::Encoding.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cobol::operands::encoding_has_type():
    assert hasattr(cobol::operands::Encoding, "type")
    descriptor = None
    for klass in cobol::operands::Encoding.__mro__:
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



def test_cobol::operands::arithmeticoperand_is_not_abstract():
    assert not inspect.isabstract(cobol::operands::ArithmeticOperand)


def test_cobol::operands::arithmeticoperand_constructor_exists():
    assert callable(cobol::operands::ArithmeticOperand.__init__)


def test_cobol::operands::arithmeticoperand_constructor_args():
    sig = inspect.signature(cobol::operands::ArithmeticOperand.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operands::replacementoperand_is_not_abstract():
    assert not inspect.isabstract(cobol::operands::ReplacementOperand)


def test_cobol::operands::replacementoperand_constructor_exists():
    assert callable(cobol::operands::ReplacementOperand.__init__)


def test_cobol::operands::replacementoperand_constructor_args():
    sig = inspect.signature(cobol::operands::ReplacementOperand.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_statements::nestedstatement_is_not_abstract():
    assert not inspect.isabstract(statements::NestedStatement)


def test_statements::nestedstatement_constructor_exists():
    assert callable(statements::NestedStatement.__init__)


def test_statements::nestedstatement_constructor_args():
    sig = inspect.signature(statements::NestedStatement.__init__)
    params = list(sig.parameters.keys())



def test_statements::perform_is_not_abstract():
    assert not inspect.isabstract(statements::Perform)


def test_statements::perform_constructor_exists():
    assert callable(statements::Perform.__init__)


def test_statements::perform_constructor_args():
    sig = inspect.signature(statements::Perform.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::performnestedstatement_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::PerformNestedStatement)


def test_cobol::statements::performnestedstatement_constructor_exists():
    assert callable(cobol::statements::PerformNestedStatement.__init__)


def test_cobol::statements::performnestedstatement_constructor_args():
    sig = inspect.signature(cobol::statements::PerformNestedStatement.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticstatement_is_not_abstract():
    assert not inspect.isabstract(ArithmeticStatement)


def test_arithmeticstatement_constructor_exists():
    assert callable(ArithmeticStatement.__init__)


def test_arithmeticstatement_constructor_args():
    sig = inspect.signature(ArithmeticStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::multiply_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Multiply)


def test_cobol::statements::multiply_constructor_exists():
    assert callable(cobol::statements::Multiply.__init__)


def test_cobol::statements::multiply_constructor_args():
    sig = inspect.signature(cobol::statements::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::subtract_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Subtract)


def test_cobol::statements::subtract_constructor_exists():
    assert callable(cobol::statements::Subtract.__init__)


def test_cobol::statements::subtract_constructor_args():
    sig = inspect.signature(cobol::statements::Subtract.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::divide_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Divide)


def test_cobol::statements::divide_constructor_exists():
    assert callable(cobol::statements::Divide.__init__)


def test_cobol::statements::divide_constructor_args():
    sig = inspect.signature(cobol::statements::Divide.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::add_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Add)


def test_cobol::statements::add_constructor_exists():
    assert callable(cobol::statements::Add.__init__)


def test_cobol::statements::add_constructor_args():
    sig = inspect.signature(cobol::statements::Add.__init__)
    params = list(sig.parameters.keys())



def test_statements::errorhandled_is_not_abstract():
    assert not inspect.isabstract(statements::ErrorHandled)


def test_statements::errorhandled_constructor_exists():
    assert callable(statements::ErrorHandled.__init__)


def test_statements::errorhandled_constructor_args():
    sig = inspect.signature(statements::ErrorHandled.__init__)
    params = list(sig.parameters.keys())



def test_statements::statement_is_not_abstract():
    assert not inspect.isabstract(statements::Statement)


def test_statements::statement_constructor_exists():
    assert callable(statements::Statement.__init__)


def test_statements::statement_constructor_args():
    sig = inspect.signature(statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::delete_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Delete)


def test_cobol::statements::delete_constructor_exists():
    assert callable(cobol::statements::Delete.__init__)


def test_cobol::statements::delete_constructor_args():
    sig = inspect.signature(cobol::statements::Delete.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::start_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Start)


def test_cobol::statements::start_constructor_exists():
    assert callable(cobol::statements::Start.__init__)


def test_cobol::statements::start_constructor_args():
    sig = inspect.signature(cobol::statements::Start.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::arithmeticstatement_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::ArithmeticStatement)


def test_cobol::statements::arithmeticstatement_constructor_exists():
    assert callable(cobol::statements::ArithmeticStatement.__init__)


def test_cobol::statements::arithmeticstatement_constructor_args():
    sig = inspect.signature(cobol::statements::ArithmeticStatement.__init__)
    params = list(sig.parameters.keys())
    assert "corresponding" in params, "Missing parameter 'corresponding'"

def test_cobol::statements::arithmeticstatement_has_corresponding():
    assert hasattr(cobol::statements::ArithmeticStatement, "corresponding")
    descriptor = None
    for klass in cobol::statements::ArithmeticStatement.__mro__:
        if "corresponding" in klass.__dict__:
            descriptor = klass.__dict__["corresponding"]
            break
    assert isinstance(descriptor, property)



def test_dataitem_is_not_abstract():
    assert not inspect.isabstract(DataItem)


def test_dataitem_constructor_exists():
    assert callable(DataItem.__init__)


def test_dataitem_constructor_args():
    sig = inspect.signature(DataItem.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::conditionname_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::ConditionName)


def test_cobol::dataitems::conditionname_constructor_exists():
    assert callable(cobol::dataitems::ConditionName.__init__)


def test_cobol::dataitems::conditionname_constructor_args():
    sig = inspect.signature(cobol::dataitems::ConditionName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::dataname_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::DataName)


def test_cobol::dataitems::dataname_constructor_exists():
    assert callable(cobol::dataitems::DataName.__init__)


def test_cobol::dataitems::dataname_constructor_args():
    sig = inspect.signature(cobol::dataitems::DataName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::recordname_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::RecordName)


def test_cobol::dataitems::recordname_constructor_exists():
    assert callable(cobol::dataitems::RecordName.__init__)


def test_cobol::dataitems::recordname_constructor_args():
    sig = inspect.signature(cobol::dataitems::RecordName.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::perform_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Perform)


def test_cobol::statements::perform_constructor_exists():
    assert callable(cobol::statements::Perform.__init__)


def test_cobol::statements::perform_constructor_args():
    sig = inspect.signature(cobol::statements::Perform.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::exit_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Exit)


def test_cobol::statements::exit_constructor_exists():
    assert callable(cobol::statements::Exit.__init__)


def test_cobol::statements::exit_constructor_args():
    sig = inspect.signature(cobol::statements::Exit.__init__)
    params = list(sig.parameters.keys())
    assert "exitLabel" in params, "Missing parameter 'exitLabel'"

def test_cobol::statements::exit_has_exitLabel():
    assert hasattr(cobol::statements::Exit, "exitLabel")
    descriptor = None
    for klass in cobol::statements::Exit.__mro__:
        if "exitLabel" in klass.__dict__:
            descriptor = klass.__dict__["exitLabel"]
            break
    assert isinstance(descriptor, property)



def test_environmentdivisionsection_is_not_abstract():
    assert not inspect.isabstract(EnvironmentDivisionSection)


def test_environmentdivisionsection_constructor_exists():
    assert callable(EnvironmentDivisionSection.__init__)


def test_environmentdivisionsection_constructor_args():
    sig = inspect.signature(EnvironmentDivisionSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sections::configurationsection_is_not_abstract():
    assert not inspect.isabstract(cobol::sections::ConfigurationSection)


def test_cobol::sections::configurationsection_constructor_exists():
    assert callable(cobol::sections::ConfigurationSection.__init__)


def test_cobol::sections::configurationsection_constructor_args():
    sig = inspect.signature(cobol::sections::ConfigurationSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sections::iosection_is_not_abstract():
    assert not inspect.isabstract(cobol::sections::IOSection)


def test_cobol::sections::iosection_constructor_exists():
    assert callable(cobol::sections::IOSection.__init__)


def test_cobol::sections::iosection_constructor_args():
    sig = inspect.signature(cobol::sections::IOSection.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticoperand_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperand)


def test_arithmeticoperand_constructor_exists():
    assert callable(ArithmeticOperand.__init__)


def test_arithmeticoperand_constructor_args():
    sig = inspect.signature(ArithmeticOperand.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operands::roundedidentifier_is_not_abstract():
    assert not inspect.isabstract(cobol::operands::RoundedIdentifier)


def test_cobol::operands::roundedidentifier_constructor_exists():
    assert callable(cobol::operands::RoundedIdentifier.__init__)


def test_cobol::operands::roundedidentifier_constructor_args():
    sig = inspect.signature(cobol::operands::RoundedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_datadivisionsection_is_not_abstract():
    assert not inspect.isabstract(DataDivisionSection)


def test_datadivisionsection_constructor_exists():
    assert callable(DataDivisionSection.__init__)


def test_datadivisionsection_constructor_args():
    sig = inspect.signature(DataDivisionSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sections::linkagestoragesection_is_not_abstract():
    assert not inspect.isabstract(cobol::sections::LinkageStorageSection)


def test_cobol::sections::linkagestoragesection_constructor_exists():
    assert callable(cobol::sections::LinkageStorageSection.__init__)


def test_cobol::sections::linkagestoragesection_constructor_args():
    sig = inspect.signature(cobol::sections::LinkageStorageSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sections::filesection_is_not_abstract():
    assert not inspect.isabstract(cobol::sections::FileSection)


def test_cobol::sections::filesection_constructor_exists():
    assert callable(cobol::sections::FileSection.__init__)


def test_cobol::sections::filesection_constructor_args():
    sig = inspect.signature(cobol::sections::FileSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sections::localstoragesection_is_not_abstract():
    assert not inspect.isabstract(cobol::sections::LocalStorageSection)


def test_cobol::sections::localstoragesection_constructor_exists():
    assert callable(cobol::sections::LocalStorageSection.__init__)


def test_cobol::sections::localstoragesection_constructor_args():
    sig = inspect.signature(cobol::sections::LocalStorageSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sections::workingstoragesection_is_not_abstract():
    assert not inspect.isabstract(cobol::sections::WorkingStorageSection)


def test_cobol::sections::workingstoragesection_constructor_exists():
    assert callable(cobol::sections::WorkingStorageSection.__init__)


def test_cobol::sections::workingstoragesection_constructor_args():
    sig = inspect.signature(cobol::sections::WorkingStorageSection.__init__)
    params = list(sig.parameters.keys())



def test_operands::arithmeticoperand_is_not_abstract():
    assert not inspect.isabstract(operands::ArithmeticOperand)


def test_operands::arithmeticoperand_constructor_exists():
    assert callable(operands::ArithmeticOperand.__init__)


def test_operands::arithmeticoperand_constructor_args():
    sig = inspect.signature(operands::ArithmeticOperand.__init__)
    params = list(sig.parameters.keys())



def test_arithmetics::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(arithmetics::PrimaryExpression)


def test_arithmetics::primaryexpression_constructor_exists():
    assert callable(arithmetics::PrimaryExpression.__init__)


def test_arithmetics::primaryexpression_constructor_args():
    sig = inspect.signature(arithmetics::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_operands::operand_is_not_abstract():
    assert not inspect.isabstract(operands::Operand)


def test_operands::operand_constructor_exists():
    assert callable(operands::Operand.__init__)


def test_operands::operand_constructor_args():
    sig = inspect.signature(operands::Operand.__init__)
    params = list(sig.parameters.keys())



def test_operands::replacementoperand_is_not_abstract():
    assert not inspect.isabstract(operands::ReplacementOperand)


def test_operands::replacementoperand_constructor_exists():
    assert callable(operands::ReplacementOperand.__init__)


def test_operands::replacementoperand_constructor_args():
    sig = inspect.signature(operands::ReplacementOperand.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operands::primaryoperand_is_not_abstract():
    assert not inspect.isabstract(cobol::operands::PrimaryOperand)


def test_cobol::operands::primaryoperand_constructor_exists():
    assert callable(cobol::operands::PrimaryOperand.__init__)


def test_cobol::operands::primaryoperand_constructor_args():
    sig = inspect.signature(cobol::operands::PrimaryOperand.__init__)
    params = list(sig.parameters.keys())



def test_sentences::statementcontainer_is_not_abstract():
    assert not inspect.isabstract(sentences::StatementContainer)


def test_sentences::statementcontainer_constructor_exists():
    assert callable(sentences::StatementContainer.__init__)


def test_sentences::statementcontainer_constructor_args():
    sig = inspect.signature(sentences::StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_sentence_is_not_abstract():
    assert not inspect.isabstract(Sentence)


def test_sentence_constructor_exists():
    assert callable(Sentence.__init__)


def test_sentence_constructor_args():
    sig = inspect.signature(Sentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sentences::exitprocedure_is_not_abstract():
    assert not inspect.isabstract(cobol::sentences::ExitProcedure)


def test_cobol::sentences::exitprocedure_constructor_exists():
    assert callable(cobol::sentences::ExitProcedure.__init__)


def test_cobol::sentences::exitprocedure_constructor_args():
    sig = inspect.signature(cobol::sentences::ExitProcedure.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sentences::alteredgoto_is_not_abstract():
    assert not inspect.isabstract(cobol::sentences::AlteredGoTo)


def test_cobol::sentences::alteredgoto_constructor_exists():
    assert callable(cobol::sentences::AlteredGoTo.__init__)


def test_cobol::sentences::alteredgoto_constructor_args():
    sig = inspect.signature(cobol::sentences::AlteredGoTo.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sentences::entrysentence_is_not_abstract():
    assert not inspect.isabstract(cobol::sentences::EntrySentence)


def test_cobol::sentences::entrysentence_constructor_exists():
    assert callable(cobol::sentences::EntrySentence.__init__)


def test_cobol::sentences::entrysentence_constructor_args():
    sig = inspect.signature(cobol::sentences::EntrySentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sentences::emptysentence_is_not_abstract():
    assert not inspect.isabstract(cobol::sentences::EmptySentence)


def test_cobol::sentences::emptysentence_constructor_exists():
    assert callable(cobol::sentences::EmptySentence.__init__)


def test_cobol::sentences::emptysentence_constructor_args():
    sig = inspect.signature(cobol::sentences::EmptySentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sentences::statementcontainer_is_not_abstract():
    assert not inspect.isabstract(cobol::sentences::StatementContainer)


def test_cobol::sentences::statementcontainer_constructor_exists():
    assert callable(cobol::sentences::StatementContainer.__init__)


def test_cobol::sentences::statementcontainer_constructor_args():
    sig = inspect.signature(cobol::sentences::StatementContainer.__init__)
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



def test_cobol::references::elementreference_is_not_abstract():
    assert not inspect.isabstract(cobol::references::ElementReference)


def test_cobol::references::elementreference_constructor_exists():
    assert callable(cobol::references::ElementReference.__init__)


def test_cobol::references::elementreference_constructor_args():
    sig = inspect.signature(cobol::references::ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(ReferenceableElement)


def test_referenceableelement_constructor_exists():
    assert callable(ReferenceableElement.__init__)


def test_referenceableelement_constructor_args():
    sig = inspect.signature(ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::specialname_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::SpecialName)


def test_cobol::specialnames::specialname_constructor_exists():
    assert callable(cobol::specialnames::SpecialName.__init__)


def test_cobol::specialnames::specialname_constructor_args():
    sig = inspect.signature(cobol::specialnames::SpecialName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::parameters::parameter_is_not_abstract():
    assert not inspect.isabstract(cobol::parameters::Parameter)


def test_cobol::parameters::parameter_constructor_exists():
    assert callable(cobol::parameters::Parameter.__init__)


def test_cobol::parameters::parameter_constructor_args():
    sig = inspect.signature(cobol::parameters::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_cobol::tables::additionalindexname_is_not_abstract():
    assert not inspect.isabstract(cobol::tables::AdditionalIndexName)


def test_cobol::tables::additionalindexname_constructor_exists():
    assert callable(cobol::tables::AdditionalIndexName.__init__)


def test_cobol::tables::additionalindexname_constructor_args():
    sig = inspect.signature(cobol::tables::AdditionalIndexName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::reference_is_not_abstract():
    assert not inspect.isabstract(cobol::references::Reference)


def test_cobol::references::reference_constructor_exists():
    assert callable(cobol::references::Reference.__init__)


def test_cobol::references::reference_constructor_args():
    sig = inspect.signature(cobol::references::Reference.__init__)
    params = list(sig.parameters.keys())



def test_cobol::paragraphs::debuggingmode_is_not_abstract():
    assert not inspect.isabstract(cobol::paragraphs::DebuggingMode)


def test_cobol::paragraphs::debuggingmode_constructor_exists():
    assert callable(cobol::paragraphs::DebuggingMode.__init__)


def test_cobol::paragraphs::debuggingmode_constructor_args():
    sig = inspect.signature(cobol::paragraphs::DebuggingMode.__init__)
    params = list(sig.parameters.keys())



def test_specialnamesparagraphwater_is_not_abstract():
    assert not inspect.isabstract(SpecialNamesParagraphWater)


def test_specialnamesparagraphwater_constructor_exists():
    assert callable(SpecialNamesParagraphWater.__init__)


def test_specialnamesparagraphwater_constructor_args():
    sig = inspect.signature(SpecialNamesParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::water::specialnamesclause_is_not_abstract():
    assert not inspect.isabstract(cobol::water::SpecialNamesClause)


def test_cobol::water::specialnamesclause_constructor_exists():
    assert callable(cobol::water::SpecialNamesClause.__init__)


def test_cobol::water::specialnamesclause_constructor_args():
    sig = inspect.signature(cobol::water::SpecialNamesClause.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::water::specialnamesclause_has_value():
    assert hasattr(cobol::water::SpecialNamesClause, "value")
    descriptor = None
    for klass in cobol::water::SpecialNamesClause.__mro__:
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



def test_incompleteelement_is_not_abstract():
    assert not inspect.isabstract(IncompleteElement)


def test_incompleteelement_constructor_exists():
    assert callable(IncompleteElement.__init__)


def test_incompleteelement_constructor_args():
    sig = inspect.signature(IncompleteElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::files::selectstatement_is_not_abstract():
    assert not inspect.isabstract(cobol::files::SelectStatement)


def test_cobol::files::selectstatement_constructor_exists():
    assert callable(cobol::files::SelectStatement.__init__)


def test_cobol::files::selectstatement_constructor_args():
    sig = inspect.signature(cobol::files::SelectStatement.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"
    assert "externalFileNames" in params, "Missing parameter 'externalFileNames'"

def test_cobol::files::selectstatement_has_isOptional():
    assert hasattr(cobol::files::SelectStatement, "isOptional")
    descriptor = None
    for klass in cobol::files::SelectStatement.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)

def test_cobol::files::selectstatement_has_externalFileNames():
    assert hasattr(cobol::files::SelectStatement, "externalFileNames")
    descriptor = None
    for klass in cobol::files::SelectStatement.__mro__:
        if "externalFileNames" in klass.__dict__:
            descriptor = klass.__dict__["externalFileNames"]
            break
    assert isinstance(descriptor, property)



def test_cobol::statements::iofile_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::IOFile)


def test_cobol::statements::iofile_constructor_exists():
    assert callable(cobol::statements::IOFile.__init__)


def test_cobol::statements::iofile_constructor_args():
    sig = inspect.signature(cobol::statements::IOFile.__init__)
    params = list(sig.parameters.keys())



def test_iofile_is_not_abstract():
    assert not inspect.isabstract(IOFile)


def test_iofile_constructor_exists():
    assert callable(IOFile.__init__)


def test_iofile_constructor_args():
    sig = inspect.signature(IOFile.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::iofiledescriptor_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::IOFileDescriptor)


def test_cobol::statements::iofiledescriptor_constructor_exists():
    assert callable(cobol::statements::IOFileDescriptor.__init__)


def test_cobol::statements::iofiledescriptor_constructor_args():
    sig = inspect.signature(cobol::statements::IOFileDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cobol::statements::iofiledescriptor_has_type():
    assert hasattr(cobol::statements::IOFileDescriptor, "type")
    descriptor = None
    for klass in cobol::statements::IOFileDescriptor.__mro__:
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



def test_cobol::statements::iostatement_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::IOStatement)


def test_cobol::statements::iostatement_constructor_exists():
    assert callable(cobol::statements::IOStatement.__init__)


def test_cobol::statements::iostatement_constructor_args():
    sig = inspect.signature(cobol::statements::IOStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::keydescriptor_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::KeyDescriptor)


def test_cobol::statements::keydescriptor_constructor_exists():
    assert callable(cobol::statements::KeyDescriptor.__init__)


def test_cobol::statements::keydescriptor_constructor_args():
    sig = inspect.signature(cobol::statements::KeyDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_cobol::statements::keydescriptor_has_order():
    assert hasattr(cobol::statements::KeyDescriptor, "order")
    descriptor = None
    for klass in cobol::statements::KeyDescriptor.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_statements::varyinguntilcondition_is_not_abstract():
    assert not inspect.isabstract(statements::VaryingUntilCondition)


def test_statements::varyinguntilcondition_constructor_exists():
    assert callable(statements::VaryingUntilCondition.__init__)


def test_statements::varyinguntilcondition_constructor_args():
    sig = inspect.signature(statements::VaryingUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::performuntilcondition_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::PerformUntilCondition)


def test_cobol::statements::performuntilcondition_constructor_exists():
    assert callable(cobol::statements::PerformUntilCondition.__init__)


def test_cobol::statements::performuntilcondition_constructor_args():
    sig = inspect.signature(cobol::statements::PerformUntilCondition.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_cobol::statements::performuntilcondition_has_position():
    assert hasattr(cobol::statements::PerformUntilCondition, "position")
    descriptor = None
    for klass in cobol::statements::PerformUntilCondition.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_cobol::statements::release_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Release)


def test_cobol::statements::release_constructor_exists():
    assert callable(cobol::statements::Release.__init__)


def test_cobol::statements::release_constructor_args():
    sig = inspect.signature(cobol::statements::Release.__init__)
    params = list(sig.parameters.keys())



def test_statements::performfixedtimes_is_not_abstract():
    assert not inspect.isabstract(statements::PerformFixedTimes)


def test_statements::performfixedtimes_constructor_exists():
    assert callable(statements::PerformFixedTimes.__init__)


def test_statements::performfixedtimes_constructor_args():
    sig = inspect.signature(statements::PerformFixedTimes.__init__)
    params = list(sig.parameters.keys())



def test_statements::fileiostatement_is_not_abstract():
    assert not inspect.isabstract(statements::FileIOStatement)


def test_statements::fileiostatement_constructor_exists():
    assert callable(statements::FileIOStatement.__init__)


def test_statements::fileiostatement_constructor_args():
    sig = inspect.signature(statements::FileIOStatement.__init__)
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



def test_statements::performprocedure_is_not_abstract():
    assert not inspect.isabstract(statements::PerformProcedure)


def test_statements::performprocedure_constructor_exists():
    assert callable(statements::PerformProcedure.__init__)


def test_statements::performprocedure_constructor_args():
    sig = inspect.signature(statements::PerformProcedure.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::performprocedurefixedtimes_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::PerformProcedureFixedTimes)


def test_cobol::statements::performprocedurefixedtimes_constructor_exists():
    assert callable(cobol::statements::PerformProcedureFixedTimes.__init__)


def test_cobol::statements::performprocedurefixedtimes_constructor_args():
    sig = inspect.signature(cobol::statements::PerformProcedureFixedTimes.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::fileiostatement_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::FileIOStatement)


def test_cobol::statements::fileiostatement_constructor_exists():
    assert callable(cobol::statements::FileIOStatement.__init__)


def test_cobol::statements::fileiostatement_constructor_args():
    sig = inspect.signature(cobol::statements::FileIOStatement.__init__)
    params = list(sig.parameters.keys())



def test_statements::performnestedstatement_is_not_abstract():
    assert not inspect.isabstract(statements::PerformNestedStatement)


def test_statements::performnestedstatement_constructor_exists():
    assert callable(statements::PerformNestedStatement.__init__)


def test_statements::performnestedstatement_constructor_args():
    sig = inspect.signature(statements::PerformNestedStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::performnestedstatementfixedtimes_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::PerformNestedStatementFixedTimes)


def test_cobol::statements::performnestedstatementfixedtimes_constructor_exists():
    assert callable(cobol::statements::PerformNestedStatementFixedTimes.__init__)


def test_cobol::statements::performnestedstatementfixedtimes_constructor_args():
    sig = inspect.signature(cobol::statements::PerformNestedStatementFixedTimes.__init__)
    params = list(sig.parameters.keys())



def test_afteruntilcondition_is_not_abstract():
    assert not inspect.isabstract(AfterUntilCondition)


def test_afteruntilcondition_constructor_exists():
    assert callable(AfterUntilCondition.__init__)


def test_afteruntilcondition_constructor_args():
    sig = inspect.signature(AfterUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_statements::performuntilcondition_is_not_abstract():
    assert not inspect.isabstract(statements::PerformUntilCondition)


def test_statements::performuntilcondition_constructor_exists():
    assert callable(statements::PerformUntilCondition.__init__)


def test_statements::performuntilcondition_constructor_args():
    sig = inspect.signature(statements::PerformUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::performnestedstatementuntilcondition_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::PerformNestedStatementUntilCondition)


def test_cobol::statements::performnestedstatementuntilcondition_constructor_exists():
    assert callable(cobol::statements::PerformNestedStatementUntilCondition.__init__)


def test_cobol::statements::performnestedstatementuntilcondition_constructor_args():
    sig = inspect.signature(cobol::statements::PerformNestedStatementUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::performprocedureuntilcondition_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::PerformProcedureUntilCondition)


def test_cobol::statements::performprocedureuntilcondition_constructor_exists():
    assert callable(cobol::statements::PerformProcedureUntilCondition.__init__)


def test_cobol::statements::performprocedureuntilcondition_constructor_args():
    sig = inspect.signature(cobol::statements::PerformProcedureUntilCondition.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::read_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Read)


def test_cobol::statements::read_constructor_exists():
    assert callable(cobol::statements::Read.__init__)


def test_cobol::statements::read_constructor_args():
    sig = inspect.signature(cobol::statements::Read.__init__)
    params = list(sig.parameters.keys())



def test_tallyingin_is_not_abstract():
    assert not inspect.isabstract(TallyingIn)


def test_tallyingin_constructor_exists():
    assert callable(TallyingIn.__init__)


def test_tallyingin_constructor_args():
    sig = inspect.signature(TallyingIn.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::switchstatus_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::SwitchStatus)


def test_cobol::statements::switchstatus_constructor_exists():
    assert callable(cobol::statements::SwitchStatus.__init__)


def test_cobol::statements::switchstatus_constructor_args():
    sig = inspect.signature(cobol::statements::SwitchStatus.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_cobol::statements::switchstatus_has_status():
    assert hasattr(cobol::statements::SwitchStatus, "status")
    descriptor = None
    for klass in cobol::statements::SwitchStatus.__mro__:
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



def test_cobol::statements::rewrite_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Rewrite)


def test_cobol::statements::rewrite_constructor_exists():
    assert callable(cobol::statements::Rewrite.__init__)


def test_cobol::statements::rewrite_constructor_args():
    sig = inspect.signature(cobol::statements::Rewrite.__init__)
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



def test_cobol::statements::write_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Write)


def test_cobol::statements::write_constructor_exists():
    assert callable(cobol::statements::Write.__init__)


def test_cobol::statements::write_constructor_args():
    sig = inspect.signature(cobol::statements::Write.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::unstring_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Unstring)


def test_cobol::statements::unstring_constructor_exists():
    assert callable(cobol::statements::Unstring.__init__)


def test_cobol::statements::unstring_constructor_args():
    sig = inspect.signature(cobol::statements::Unstring.__init__)
    params = list(sig.parameters.keys())



def test_searchstatement_is_not_abstract():
    assert not inspect.isabstract(SearchStatement)


def test_searchstatement_constructor_exists():
    assert callable(SearchStatement.__init__)


def test_searchstatement_constructor_args():
    sig = inspect.signature(SearchStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::binarysearch_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::BinarySearch)


def test_cobol::statements::binarysearch_constructor_exists():
    assert callable(cobol::statements::BinarySearch.__init__)


def test_cobol::statements::binarysearch_constructor_args():
    sig = inspect.signature(cobol::statements::BinarySearch.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::serialsearch_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::SerialSearch)


def test_cobol::statements::serialsearch_constructor_exists():
    assert callable(cobol::statements::SerialSearch.__init__)


def test_cobol::statements::serialsearch_constructor_args():
    sig = inspect.signature(cobol::statements::SerialSearch.__init__)
    params = list(sig.parameters.keys())



def test_normalevaluatecase_is_not_abstract():
    assert not inspect.isabstract(NormalEvaluateCase)


def test_normalevaluatecase_constructor_exists():
    assert callable(NormalEvaluateCase.__init__)


def test_normalevaluatecase_constructor_args():
    sig = inspect.signature(NormalEvaluateCase.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::searchstatement_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::SearchStatement)


def test_cobol::statements::searchstatement_constructor_exists():
    assert callable(cobol::statements::SearchStatement.__init__)


def test_cobol::statements::searchstatement_constructor_args():
    sig = inspect.signature(cobol::statements::SearchStatement.__init__)
    params = list(sig.parameters.keys())



def test_replacement_is_not_abstract():
    assert not inspect.isabstract(Replacement)


def test_replacement_constructor_exists():
    assert callable(Replacement.__init__)


def test_replacement_constructor_args():
    sig = inspect.signature(Replacement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::specificcharacterbyspecificcharacter_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::SpecificCharacterBySpecificCharacter)


def test_cobol::strings::specificcharacterbyspecificcharacter_constructor_exists():
    assert callable(cobol::strings::SpecificCharacterBySpecificCharacter.__init__)


def test_cobol::strings::specificcharacterbyspecificcharacter_constructor_args():
    sig = inspect.signature(cobol::strings::SpecificCharacterBySpecificCharacter.__init__)
    params = list(sig.parameters.keys())



def test_cobol::strings::anycharacterbyspecificcharacter_is_not_abstract():
    assert not inspect.isabstract(cobol::strings::AnyCharacterBySpecificCharacter)


def test_cobol::strings::anycharacterbyspecificcharacter_constructor_exists():
    assert callable(cobol::strings::AnyCharacterBySpecificCharacter.__init__)


def test_cobol::strings::anycharacterbyspecificcharacter_constructor_args():
    sig = inspect.signature(cobol::strings::AnyCharacterBySpecificCharacter.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::initialize_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Initialize)


def test_cobol::statements::initialize_constructor_exists():
    assert callable(cobol::statements::Initialize.__init__)


def test_cobol::statements::initialize_constructor_args():
    sig = inspect.signature(cobol::statements::Initialize.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::inspect_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Inspect)


def test_cobol::statements::inspect_constructor_exists():
    assert callable(cobol::statements::Inspect.__init__)


def test_cobol::statements::inspect_constructor_args():
    sig = inspect.signature(cobol::statements::Inspect.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::replace_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Replace)


def test_cobol::statements::replace_constructor_exists():
    assert callable(cobol::statements::Replace.__init__)


def test_cobol::statements::replace_constructor_args():
    sig = inspect.signature(cobol::statements::Replace.__init__)
    params = list(sig.parameters.keys())
    assert "replaceSwitch" in params, "Missing parameter 'replaceSwitch'"

def test_cobol::statements::replace_has_replaceSwitch():
    assert hasattr(cobol::statements::Replace, "replaceSwitch")
    descriptor = None
    for klass in cobol::statements::Replace.__mro__:
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



def test_cobol::handlers::handler_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::Handler)


def test_cobol::handlers::handler_constructor_exists():
    assert callable(cobol::handlers::Handler.__init__)


def test_cobol::handlers::handler_constructor_args():
    sig = inspect.signature(cobol::handlers::Handler.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::evaluatecase_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::EvaluateCase)


def test_cobol::statements::evaluatecase_constructor_exists():
    assert callable(cobol::statements::EvaluateCase.__init__)


def test_cobol::statements::evaluatecase_constructor_args():
    sig = inspect.signature(cobol::statements::EvaluateCase.__init__)
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



def test_cobol::statements::normalevaluatecase_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::NormalEvaluateCase)


def test_cobol::statements::normalevaluatecase_constructor_exists():
    assert callable(cobol::statements::NormalEvaluateCase.__init__)


def test_cobol::statements::normalevaluatecase_constructor_args():
    sig = inspect.signature(cobol::statements::NormalEvaluateCase.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::otherevaluatecase_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::OtherEvaluateCase)


def test_cobol::statements::otherevaluatecase_constructor_exists():
    assert callable(cobol::statements::OtherEvaluateCase.__init__)


def test_cobol::statements::otherevaluatecase_constructor_args():
    sig = inspect.signature(cobol::statements::OtherEvaluateCase.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::evaluate_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Evaluate)


def test_cobol::statements::evaluate_constructor_exists():
    assert callable(cobol::statements::Evaluate.__init__)


def test_cobol::statements::evaluate_constructor_args():
    sig = inspect.signature(cobol::statements::Evaluate.__init__)
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



def test_cobol::statements::set_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Set)


def test_cobol::statements::set_constructor_exists():
    assert callable(cobol::statements::Set.__init__)


def test_cobol::statements::set_constructor_args():
    sig = inspect.signature(cobol::statements::Set.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::setswitches_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::SetSwitches)


def test_cobol::statements::setswitches_constructor_exists():
    assert callable(cobol::statements::SetSwitches.__init__)


def test_cobol::statements::setswitches_constructor_args():
    sig = inspect.signature(cobol::statements::SetSwitches.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::setstatement_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::SetStatement)


def test_cobol::statements::setstatement_constructor_exists():
    assert callable(cobol::statements::SetStatement.__init__)


def test_cobol::statements::setstatement_constructor_args():
    sig = inspect.signature(cobol::statements::SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_filenamereference_is_not_abstract():
    assert not inspect.isabstract(FileNameReference)


def test_filenamereference_constructor_exists():
    assert callable(FileNameReference.__init__)


def test_filenamereference_constructor_args():
    sig = inspect.signature(FileNameReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::return_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Return)


def test_cobol::statements::return_constructor_exists():
    assert callable(cobol::statements::Return.__init__)


def test_cobol::statements::return_constructor_args():
    sig = inspect.signature(cobol::statements::Return.__init__)
    params = list(sig.parameters.keys())



def test_handler_is_not_abstract():
    assert not inspect.isabstract(Handler)


def test_handler_constructor_exists():
    assert callable(Handler.__init__)


def test_handler_constructor_args():
    sig = inspect.signature(Handler.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::onexception_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::OnException)


def test_cobol::handlers::onexception_constructor_exists():
    assert callable(cobol::handlers::OnException.__init__)


def test_cobol::handlers::onexception_constructor_args():
    sig = inspect.signature(cobol::handlers::OnException.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::atendofpage_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::AtEndOfPage)


def test_cobol::handlers::atendofpage_constructor_exists():
    assert callable(cobol::handlers::AtEndOfPage.__init__)


def test_cobol::handlers::atendofpage_constructor_args():
    sig = inspect.signature(cobol::handlers::AtEndOfPage.__init__)
    params = list(sig.parameters.keys())
    assert "eop" in params, "Missing parameter 'eop'"

def test_cobol::handlers::atendofpage_has_eop():
    assert hasattr(cobol::handlers::AtEndOfPage, "eop")
    descriptor = None
    for klass in cobol::handlers::AtEndOfPage.__mro__:
        if "eop" in klass.__dict__:
            descriptor = klass.__dict__["eop"]
            break
    assert isinstance(descriptor, property)



def test_cobol::handlers::noterrorhandler_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::NotErrorHandler)


def test_cobol::handlers::noterrorhandler_constructor_exists():
    assert callable(cobol::handlers::NotErrorHandler.__init__)


def test_cobol::handlers::noterrorhandler_constructor_args():
    sig = inspect.signature(cobol::handlers::NotErrorHandler.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::invalidkey_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::InvalidKey)


def test_cobol::handlers::invalidkey_constructor_exists():
    assert callable(cobol::handlers::InvalidKey.__init__)


def test_cobol::handlers::invalidkey_constructor_args():
    sig = inspect.signature(cobol::handlers::InvalidKey.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::onoverflow_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::OnOverflow)


def test_cobol::handlers::onoverflow_constructor_exists():
    assert callable(cobol::handlers::OnOverflow.__init__)


def test_cobol::handlers::onoverflow_constructor_args():
    sig = inspect.signature(cobol::handlers::OnOverflow.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::atend_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::AtEnd)


def test_cobol::handlers::atend_constructor_exists():
    assert callable(cobol::handlers::AtEnd.__init__)


def test_cobol::handlers::atend_constructor_args():
    sig = inspect.signature(cobol::handlers::AtEnd.__init__)
    params = list(sig.parameters.keys())



def test_cobol::handlers::onsizeerror_is_not_abstract():
    assert not inspect.isabstract(cobol::handlers::OnSizeError)


def test_cobol::handlers::onsizeerror_constructor_exists():
    assert callable(cobol::handlers::OnSizeError.__init__)


def test_cobol::handlers::onsizeerror_constructor_args():
    sig = inspect.signature(cobol::handlers::OnSizeError.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::errorhandled_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::ErrorHandled)


def test_cobol::statements::errorhandled_constructor_exists():
    assert callable(cobol::statements::ErrorHandled.__init__)


def test_cobol::statements::errorhandled_constructor_args():
    sig = inspect.signature(cobol::statements::ErrorHandled.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::execute_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Execute)


def test_cobol::statements::execute_constructor_exists():
    assert callable(cobol::statements::Execute.__init__)


def test_cobol::statements::execute_constructor_args():
    sig = inspect.signature(cobol::statements::Execute.__init__)
    params = list(sig.parameters.keys())
    assert "water" in params, "Missing parameter 'water'"

def test_cobol::statements::execute_has_water():
    assert hasattr(cobol::statements::Execute, "water")
    descriptor = None
    for klass in cobol::statements::Execute.__mro__:
        if "water" in klass.__dict__:
            descriptor = klass.__dict__["water"]
            break
    assert isinstance(descriptor, property)



def test_functions::argumentable_is_not_abstract():
    assert not inspect.isabstract(functions::Argumentable)


def test_functions::argumentable_constructor_exists():
    assert callable(functions::Argumentable.__init__)


def test_functions::argumentable_constructor_args():
    sig = inspect.signature(functions::Argumentable.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::call_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Call)


def test_cobol::statements::call_constructor_exists():
    assert callable(cobol::statements::Call.__init__)


def test_cobol::statements::call_constructor_args():
    sig = inspect.signature(cobol::statements::Call.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::cancel_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Cancel)


def test_cobol::statements::cancel_constructor_exists():
    assert callable(cobol::statements::Cancel.__init__)


def test_cobol::statements::cancel_constructor_args():
    sig = inspect.signature(cobol::statements::Cancel.__init__)
    params = list(sig.parameters.keys())



def test_statements::iostatement_is_not_abstract():
    assert not inspect.isabstract(statements::IOStatement)


def test_statements::iostatement_constructor_exists():
    assert callable(statements::IOStatement.__init__)


def test_statements::iostatement_constructor_args():
    sig = inspect.signature(statements::IOStatement.__init__)
    params = list(sig.parameters.keys())



def test_concatenatingstrings_is_not_abstract():
    assert not inspect.isabstract(ConcatenatingStrings)


def test_concatenatingstrings_constructor_exists():
    assert callable(ConcatenatingStrings.__init__)


def test_concatenatingstrings_constructor_args():
    sig = inspect.signature(ConcatenatingStrings.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::string_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::String)


def test_cobol::statements::string_constructor_exists():
    assert callable(cobol::statements::String.__init__)


def test_cobol::statements::string_constructor_args():
    sig = inspect.signature(cobol::statements::String.__init__)
    params = list(sig.parameters.keys())



def test_indexnamereference_is_not_abstract():
    assert not inspect.isabstract(IndexNameReference)


def test_indexnamereference_constructor_exists():
    assert callable(IndexNameReference.__init__)


def test_indexnamereference_constructor_args():
    sig = inspect.signature(IndexNameReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::setindexname_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::SetIndexName)


def test_cobol::statements::setindexname_constructor_exists():
    assert callable(cobol::statements::SetIndexName.__init__)


def test_cobol::statements::setindexname_constructor_args():
    sig = inspect.signature(cobol::statements::SetIndexName.__init__)
    params = list(sig.parameters.keys())
    assert "adjust" in params, "Missing parameter 'adjust'"

def test_cobol::statements::setindexname_has_adjust():
    assert hasattr(cobol::statements::SetIndexName, "adjust")
    descriptor = None
    for klass in cobol::statements::SetIndexName.__mro__:
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



def test_cobol::registers::register_is_not_abstract():
    assert not inspect.isabstract(cobol::registers::Register)


def test_cobol::registers::register_constructor_exists():
    assert callable(cobol::registers::Register.__init__)


def test_cobol::registers::register_constructor_args():
    sig = inspect.signature(cobol::registers::Register.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::move_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Move)


def test_cobol::statements::move_constructor_exists():
    assert callable(cobol::statements::Move.__init__)


def test_cobol::statements::move_constructor_args():
    sig = inspect.signature(cobol::statements::Move.__init__)
    params = list(sig.parameters.keys())
    assert "corresponding" in params, "Missing parameter 'corresponding'"

def test_cobol::statements::move_has_corresponding():
    assert hasattr(cobol::statements::Move, "corresponding")
    descriptor = None
    for klass in cobol::statements::Move.__mro__:
        if "corresponding" in klass.__dict__:
            descriptor = klass.__dict__["corresponding"]
            break
    assert isinstance(descriptor, property)



def test_cobol::statements::nestedstatement_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::NestedStatement)


def test_cobol::statements::nestedstatement_constructor_exists():
    assert callable(cobol::statements::NestedStatement.__init__)


def test_cobol::statements::nestedstatement_constructor_args():
    sig = inspect.signature(cobol::statements::NestedStatement.__init__)
    params = list(sig.parameters.keys())



def test_jump_is_not_abstract():
    assert not inspect.isabstract(Jump)


def test_jump_constructor_exists():
    assert callable(Jump.__init__)


def test_jump_constructor_args():
    sig = inspect.signature(Jump.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::continue_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Continue)


def test_cobol::statements::continue_constructor_exists():
    assert callable(cobol::statements::Continue.__init__)


def test_cobol::statements::continue_constructor_args():
    sig = inspect.signature(cobol::statements::Continue.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::goback_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::GoBack)


def test_cobol::statements::goback_constructor_exists():
    assert callable(cobol::statements::GoBack.__init__)


def test_cobol::statements::goback_constructor_args():
    sig = inspect.signature(cobol::statements::GoBack.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::goto_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::GoTo)


def test_cobol::statements::goto_constructor_exists():
    assert callable(cobol::statements::GoTo.__init__)


def test_cobol::statements::goto_constructor_args():
    sig = inspect.signature(cobol::statements::GoTo.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::nextsentence_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::NextSentence)


def test_cobol::statements::nextsentence_constructor_exists():
    assert callable(cobol::statements::NextSentence.__init__)


def test_cobol::statements::nextsentence_constructor_args():
    sig = inspect.signature(cobol::statements::NextSentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::jump_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Jump)


def test_cobol::statements::jump_constructor_exists():
    assert callable(cobol::statements::Jump.__init__)


def test_cobol::statements::jump_constructor_args():
    sig = inspect.signature(cobol::statements::Jump.__init__)
    params = list(sig.parameters.keys())



def test_procedurerangelabel_is_not_abstract():
    assert not inspect.isabstract(ProcedureRangeLabel)


def test_procedurerangelabel_constructor_exists():
    assert callable(ProcedureRangeLabel.__init__)


def test_procedurerangelabel_constructor_args():
    sig = inspect.signature(ProcedureRangeLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol::labels::procedurerange_is_not_abstract():
    assert not inspect.isabstract(cobol::labels::ProcedureRange)


def test_cobol::labels::procedurerange_constructor_exists():
    assert callable(cobol::labels::ProcedureRange.__init__)


def test_cobol::labels::procedurerange_constructor_args():
    sig = inspect.signature(cobol::labels::ProcedureRange.__init__)
    params = list(sig.parameters.keys())



def test_cobol::labels::procedurerangechild_is_not_abstract():
    assert not inspect.isabstract(cobol::labels::ProcedureRangeChild)


def test_cobol::labels::procedurerangechild_constructor_exists():
    assert callable(cobol::labels::ProcedureRangeChild.__init__)


def test_cobol::labels::procedurerangechild_constructor_args():
    sig = inspect.signature(cobol::labels::ProcedureRangeChild.__init__)
    params = list(sig.parameters.keys())



def test_perform_is_not_abstract():
    assert not inspect.isabstract(Perform)


def test_perform_constructor_exists():
    assert callable(Perform.__init__)


def test_perform_constructor_args():
    sig = inspect.signature(Perform.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::performfixedtimes_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::PerformFixedTimes)


def test_cobol::statements::performfixedtimes_constructor_exists():
    assert callable(cobol::statements::PerformFixedTimes.__init__)


def test_cobol::statements::performfixedtimes_constructor_args():
    sig = inspect.signature(cobol::statements::PerformFixedTimes.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::performprocedure_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::PerformProcedure)


def test_cobol::statements::performprocedure_constructor_exists():
    assert callable(cobol::statements::PerformProcedure.__init__)


def test_cobol::statements::performprocedure_constructor_args():
    sig = inspect.signature(cobol::statements::PerformProcedure.__init__)
    params = list(sig.parameters.keys())



def test_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(AssignmentExpression)


def test_assignmentexpression_constructor_exists():
    assert callable(AssignmentExpression.__init__)


def test_assignmentexpression_constructor_args():
    sig = inspect.signature(AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::compute_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Compute)


def test_cobol::statements::compute_constructor_exists():
    assert callable(cobol::statements::Compute.__init__)


def test_cobol::statements::compute_constructor_args():
    sig = inspect.signature(cobol::statements::Compute.__init__)
    params = list(sig.parameters.keys())



def test_environment_is_not_abstract():
    assert not inspect.isabstract(Environment)


def test_environment_constructor_exists():
    assert callable(Environment.__init__)


def test_environment_constructor_args():
    sig = inspect.signature(Environment.__init__)
    params = list(sig.parameters.keys())



def test_cobol::environments::systemdevice_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::SystemDevice)


def test_cobol::environments::systemdevice_constructor_exists():
    assert callable(cobol::environments::SystemDevice.__init__)


def test_cobol::environments::systemdevice_constructor_args():
    sig = inspect.signature(cobol::environments::SystemDevice.__init__)
    params = list(sig.parameters.keys())



def test_cobol::environments::upsi_is_not_abstract():
    assert not inspect.isabstract(cobol::environments::UPSI)


def test_cobol::environments::upsi_constructor_exists():
    assert callable(cobol::environments::UPSI.__init__)


def test_cobol::environments::upsi_constructor_args():
    sig = inspect.signature(cobol::environments::UPSI.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::environments::upsi_has_value():
    assert hasattr(cobol::environments::UPSI, "value")
    descriptor = None
    for klass in cobol::environments::UPSI.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::statements::display_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Display)


def test_cobol::statements::display_constructor_exists():
    assert callable(cobol::statements::Display.__init__)


def test_cobol::statements::display_constructor_args():
    sig = inspect.signature(cobol::statements::Display.__init__)
    params = list(sig.parameters.keys())



def test_stoplabel_is_not_abstract():
    assert not inspect.isabstract(StopLabel)


def test_stoplabel_constructor_exists():
    assert callable(StopLabel.__init__)


def test_stoplabel_constructor_args():
    sig = inspect.signature(StopLabel.__init__)
    params = list(sig.parameters.keys())



def test_cobol::labels::run_is_not_abstract():
    assert not inspect.isabstract(cobol::labels::Run)


def test_cobol::labels::run_constructor_exists():
    assert callable(cobol::labels::Run.__init__)


def test_cobol::labels::run_constructor_args():
    sig = inspect.signature(cobol::labels::Run.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::stop_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Stop)


def test_cobol::statements::stop_constructor_exists():
    assert callable(cobol::statements::Stop.__init__)


def test_cobol::statements::stop_constructor_args():
    sig = inspect.signature(cobol::statements::Stop.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::conditional_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Conditional)


def test_cobol::statements::conditional_constructor_exists():
    assert callable(cobol::statements::Conditional.__init__)


def test_cobol::statements::conditional_constructor_args():
    sig = inspect.signature(cobol::statements::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_statements::conditional_is_not_abstract():
    assert not inspect.isabstract(statements::Conditional)


def test_statements::conditional_constructor_exists():
    assert callable(statements::Conditional.__init__)


def test_statements::conditional_constructor_args():
    sig = inspect.signature(statements::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::condition_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Condition)


def test_cobol::statements::condition_constructor_exists():
    assert callable(cobol::statements::Condition.__init__)


def test_cobol::statements::condition_constructor_args():
    sig = inspect.signature(cobol::statements::Condition.__init__)
    params = list(sig.parameters.keys())



def test_negatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(NegatedConditionalExpressionChild)


def test_negatedconditionalexpressionchild_constructor_exists():
    assert callable(NegatedConditionalExpressionChild.__init__)


def test_negatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(NegatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(ConditionalAndExpressionChild)


def test_conditionalandexpressionchild_constructor_exists():
    assert callable(ConditionalAndExpressionChild.__init__)


def test_conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::negatedconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::NegatedConditionalExpression)


def test_cobol::conditions::negatedconditionalexpression_constructor_exists():
    assert callable(cobol::conditions::NegatedConditionalExpression.__init__)


def test_cobol::conditions::negatedconditionalexpression_constructor_args():
    sig = inspect.signature(cobol::conditions::NegatedConditionalExpression.__init__)
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



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::conditionalorexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::ConditionalOrExpressionChild)


def test_cobol::conditions::conditionalorexpressionchild_constructor_exists():
    assert callable(cobol::conditions::ConditionalOrExpressionChild.__init__)


def test_cobol::conditions::conditionalorexpressionchild_constructor_args():
    sig = inspect.signature(cobol::conditions::ConditionalOrExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::ConditionalOrExpression)


def test_cobol::conditions::conditionalorexpression_constructor_exists():
    assert callable(cobol::conditions::ConditionalOrExpression.__init__)


def test_cobol::conditions::conditionalorexpression_constructor_args():
    sig = inspect.signature(cobol::conditions::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::condition_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::Condition)


def test_cobol::conditions::condition_constructor_exists():
    assert callable(cobol::conditions::Condition.__init__)


def test_cobol::conditions::condition_constructor_args():
    sig = inspect.signature(cobol::conditions::Condition.__init__)
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



def test_cobol::conditions::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::RelationalExpression)


def test_cobol::conditions::relationalexpression_constructor_exists():
    assert callable(cobol::conditions::RelationalExpression.__init__)


def test_cobol::conditions::relationalexpression_constructor_args():
    sig = inspect.signature(cobol::conditions::RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::simpleconditionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::SimpleConditionChild)


def test_cobol::conditions::simpleconditionchild_constructor_exists():
    assert callable(cobol::conditions::SimpleConditionChild.__init__)


def test_cobol::conditions::simpleconditionchild_constructor_args():
    sig = inspect.signature(cobol::conditions::SimpleConditionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::negatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::NegatedConditionalExpressionChild)


def test_cobol::conditions::negatedconditionalexpressionchild_constructor_exists():
    assert callable(cobol::conditions::NegatedConditionalExpressionChild.__init__)


def test_cobol::conditions::negatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(cobol::conditions::NegatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_negate_is_not_abstract():
    assert not inspect.isabstract(Negate)


def test_negate_constructor_exists():
    assert callable(Negate.__init__)


def test_negate_constructor_args():
    sig = inspect.signature(Negate.__init__)
    params = list(sig.parameters.keys())



def test_cobol::commons::commentable_is_not_abstract():
    assert not inspect.isabstract(cobol::commons::Commentable)


def test_cobol::commons::commentable_constructor_exists():
    assert callable(cobol::commons::Commentable.__init__)


def test_cobol::commons::commentable_constructor_args():
    sig = inspect.signature(cobol::commons::Commentable.__init__)
    params = list(sig.parameters.keys())



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_cobol::commons::uriableelement_is_not_abstract():
    assert not inspect.isabstract(cobol::commons::URIableElement)


def test_cobol::commons::uriableelement_constructor_exists():
    assert callable(cobol::commons::URIableElement.__init__)


def test_cobol::commons::uriableelement_constructor_args():
    sig = inspect.signature(cobol::commons::URIableElement.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_cobol::commons::uriableelement_has_uri():
    assert hasattr(cobol::commons::URIableElement, "uri")
    descriptor = None
    for klass in cobol::commons::URIableElement.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_cobol::commons::labellableelement_is_not_abstract():
    assert not inspect.isabstract(cobol::commons::LabellableElement)


def test_cobol::commons::labellableelement_constructor_exists():
    assert callable(cobol::commons::LabellableElement.__init__)


def test_cobol::commons::labellableelement_constructor_args():
    sig = inspect.signature(cobol::commons::LabellableElement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_cobol::commons::labellableelement_has_label():
    assert hasattr(cobol::commons::LabellableElement, "label")
    descriptor = None
    for klass in cobol::commons::LabellableElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_cobol::commons::namedelement_is_not_abstract():
    assert not inspect.isabstract(cobol::commons::NamedElement)


def test_cobol::commons::namedelement_constructor_exists():
    assert callable(cobol::commons::NamedElement.__init__)


def test_cobol::commons::namedelement_constructor_args():
    sig = inspect.signature(cobol::commons::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cobol::commons::namedelement_has_name():
    assert hasattr(cobol::commons::NamedElement, "name")
    descriptor = None
    for klass in cobol::commons::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_identifiers::identifierreference_is_not_abstract():
    assert not inspect.isabstract(identifiers::IdentifierReference)


def test_identifiers::identifierreference_constructor_exists():
    assert callable(identifiers::IdentifierReference.__init__)


def test_identifiers::identifierreference_constructor_args():
    sig = inspect.signature(identifiers::IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::qualifiable_is_not_abstract():
    assert not inspect.isabstract(cobol::references::Qualifiable)


def test_cobol::references::qualifiable_constructor_exists():
    assert callable(cobol::references::Qualifiable.__init__)


def test_cobol::references::qualifiable_constructor_args():
    sig = inspect.signature(cobol::references::Qualifiable.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::conditionname_is_not_abstract():
    assert not inspect.isabstract(cobol::references::ConditionName)


def test_cobol::references::conditionname_constructor_exists():
    assert callable(cobol::references::ConditionName.__init__)


def test_cobol::references::conditionname_constructor_args():
    sig = inspect.signature(cobol::references::ConditionName.__init__)
    params = list(sig.parameters.keys())



def test_elementreference_is_not_abstract():
    assert not inspect.isabstract(ElementReference)


def test_elementreference_constructor_exists():
    assert callable(ElementReference.__init__)


def test_elementreference_constructor_args():
    sig = inspect.signature(ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol::identifiers::qualifier_is_not_abstract():
    assert not inspect.isabstract(cobol::identifiers::Qualifier)


def test_cobol::identifiers::qualifier_constructor_exists():
    assert callable(cobol::identifiers::Qualifier.__init__)


def test_cobol::identifiers::qualifier_constructor_args():
    sig = inspect.signature(cobol::identifiers::Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::alphabetnamereference_is_not_abstract():
    assert not inspect.isabstract(cobol::references::AlphabetNameReference)


def test_cobol::references::alphabetnamereference_constructor_exists():
    assert callable(cobol::references::AlphabetNameReference.__init__)


def test_cobol::references::alphabetnamereference_constructor_args():
    sig = inspect.signature(cobol::references::AlphabetNameReference.__init__)
    params = list(sig.parameters.keys())



def test_identifierreference_is_not_abstract():
    assert not inspect.isabstract(IdentifierReference)


def test_identifierreference_constructor_exists():
    assert callable(IdentifierReference.__init__)


def test_identifierreference_constructor_args():
    sig = inspect.signature(IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::indexnamereference_is_not_abstract():
    assert not inspect.isabstract(cobol::references::IndexNameReference)


def test_cobol::references::indexnamereference_constructor_exists():
    assert callable(cobol::references::IndexNameReference.__init__)


def test_cobol::references::indexnamereference_constructor_args():
    sig = inspect.signature(cobol::references::IndexNameReference.__init__)
    params = list(sig.parameters.keys())



def test_references::identifierreferencequalifier_is_not_abstract():
    assert not inspect.isabstract(references::IdentifierReferenceQualifier)


def test_references::identifierreferencequalifier_constructor_exists():
    assert callable(references::IdentifierReferenceQualifier.__init__)


def test_references::identifierreferencequalifier_constructor_args():
    sig = inspect.signature(references::IdentifierReferenceQualifier.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::datanamereference_is_not_abstract():
    assert not inspect.isabstract(cobol::references::DataNameReference)


def test_cobol::references::datanamereference_constructor_exists():
    assert callable(cobol::references::DataNameReference.__init__)


def test_cobol::references::datanamereference_constructor_args():
    sig = inspect.signature(cobol::references::DataNameReference.__init__)
    params = list(sig.parameters.keys())



def test_references::conditionname_is_not_abstract():
    assert not inspect.isabstract(references::ConditionName)


def test_references::conditionname_constructor_exists():
    assert callable(references::ConditionName.__init__)


def test_references::conditionname_constructor_args():
    sig = inspect.signature(references::ConditionName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::conditionnamereference_is_not_abstract():
    assert not inspect.isabstract(cobol::references::ConditionNameReference)


def test_cobol::references::conditionnamereference_constructor_exists():
    assert callable(cobol::references::ConditionNameReference.__init__)


def test_cobol::references::conditionnamereference_constructor_args():
    sig = inspect.signature(cobol::references::ConditionNameReference.__init__)
    params = list(sig.parameters.keys())



def test_references::qualifiable_is_not_abstract():
    assert not inspect.isabstract(references::Qualifiable)


def test_references::qualifiable_constructor_exists():
    assert callable(references::Qualifiable.__init__)


def test_references::qualifiable_constructor_args():
    sig = inspect.signature(references::Qualifiable.__init__)
    params = list(sig.parameters.keys())



def test_cobol::identifiers::linagecounter_is_not_abstract():
    assert not inspect.isabstract(cobol::identifiers::LinageCounter)


def test_cobol::identifiers::linagecounter_constructor_exists():
    assert callable(cobol::identifiers::LinageCounter.__init__)


def test_cobol::identifiers::linagecounter_constructor_args():
    sig = inspect.signature(cobol::identifiers::LinageCounter.__init__)
    params = list(sig.parameters.keys())



def test_references::elementreference_is_not_abstract():
    assert not inspect.isabstract(references::ElementReference)


def test_references::elementreference_constructor_exists():
    assert callable(references::ElementReference.__init__)


def test_references::elementreference_constructor_args():
    sig = inspect.signature(references::ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol::identifiers::identifierreference_is_not_abstract():
    assert not inspect.isabstract(cobol::identifiers::IdentifierReference)


def test_cobol::identifiers::identifierreference_constructor_exists():
    assert callable(cobol::identifiers::IdentifierReference.__init__)


def test_cobol::identifiers::identifierreference_constructor_args():
    sig = inspect.signature(cobol::identifiers::IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::filenamereference_is_not_abstract():
    assert not inspect.isabstract(cobol::references::FileNameReference)


def test_cobol::references::filenamereference_constructor_exists():
    assert callable(cobol::references::FileNameReference.__init__)


def test_cobol::references::filenamereference_constructor_args():
    sig = inspect.signature(cobol::references::FileNameReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::mnemonicnamereference_is_not_abstract():
    assert not inspect.isabstract(cobol::references::MnemonicNameReference)


def test_cobol::references::mnemonicnamereference_constructor_exists():
    assert callable(cobol::references::MnemonicNameReference.__init__)


def test_cobol::references::mnemonicnamereference_constructor_args():
    sig = inspect.signature(cobol::references::MnemonicNameReference.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::identifierreferencequalifier_is_not_abstract():
    assert not inspect.isabstract(cobol::references::IdentifierReferenceQualifier)


def test_cobol::references::identifierreferencequalifier_constructor_exists():
    assert callable(cobol::references::IdentifierReferenceQualifier.__init__)


def test_cobol::references::identifierreferencequalifier_constructor_args():
    sig = inspect.signature(cobol::references::IdentifierReferenceQualifier.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::symboliccharacterstatement_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::SymbolicCharacterStatement)


def test_cobol::specialnames::symboliccharacterstatement_constructor_exists():
    assert callable(cobol::specialnames::SymbolicCharacterStatement.__init__)


def test_cobol::specialnames::symboliccharacterstatement_constructor_args():
    sig = inspect.signature(cobol::specialnames::SymbolicCharacterStatement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::specialnamesconditionnamereference_is_not_abstract():
    assert not inspect.isabstract(cobol::references::SpecialNamesConditionNameReference)


def test_cobol::references::specialnamesconditionnamereference_constructor_exists():
    assert callable(cobol::references::SpecialNamesConditionNameReference.__init__)


def test_cobol::references::specialnamesconditionnamereference_constructor_args():
    sig = inspect.signature(cobol::references::SpecialNamesConditionNameReference.__init__)
    params = list(sig.parameters.keys())



def test_greaterthan_is_not_abstract():
    assert not inspect.isabstract(GreaterThan)


def test_greaterthan_constructor_exists():
    assert callable(GreaterThan.__init__)


def test_greaterthan_constructor_args():
    sig = inspect.signature(GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::gtphrase_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::GTPhrase)


def test_cobol::operators::gtphrase_constructor_exists():
    assert callable(cobol::operators::GTPhrase.__init__)


def test_cobol::operators::gtphrase_constructor_args():
    sig = inspect.signature(cobol::operators::GTPhrase.__init__)
    params = list(sig.parameters.keys())



def test_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(LessThanOrEqual)


def test_lessthanorequal_constructor_exists():
    assert callable(LessThanOrEqual.__init__)


def test_lessthanorequal_constructor_args():
    sig = inspect.signature(LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::lteqsign_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::LTEQSign)


def test_cobol::operators::lteqsign_constructor_exists():
    assert callable(cobol::operators::LTEQSign.__init__)


def test_cobol::operators::lteqsign_constructor_args():
    sig = inspect.signature(cobol::operators::LTEQSign.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::lteqphrase_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::LTEQPhrase)


def test_cobol::operators::lteqphrase_constructor_exists():
    assert callable(cobol::operators::LTEQPhrase.__init__)


def test_cobol::operators::lteqphrase_constructor_args():
    sig = inspect.signature(cobol::operators::LTEQPhrase.__init__)
    params = list(sig.parameters.keys())



def test_lessthan_is_not_abstract():
    assert not inspect.isabstract(LessThan)


def test_lessthan_constructor_exists():
    assert callable(LessThan.__init__)


def test_lessthan_constructor_args():
    sig = inspect.signature(LessThan.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::ltsign_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::LTSign)


def test_cobol::operators::ltsign_constructor_exists():
    assert callable(cobol::operators::LTSign.__init__)


def test_cobol::operators::ltsign_constructor_args():
    sig = inspect.signature(cobol::operators::LTSign.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::ltphrase_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::LTPhrase)


def test_cobol::operators::ltphrase_constructor_exists():
    assert callable(cobol::operators::LTPhrase.__init__)


def test_cobol::operators::ltphrase_constructor_args():
    sig = inspect.signature(cobol::operators::LTPhrase.__init__)
    params = list(sig.parameters.keys())



def test_paragraphs::iosectionparagraph_is_not_abstract():
    assert not inspect.isabstract(paragraphs::IOSectionParagraph)


def test_paragraphs::iosectionparagraph_constructor_exists():
    assert callable(paragraphs::IOSectionParagraph.__init__)


def test_paragraphs::iosectionparagraph_constructor_args():
    sig = inspect.signature(paragraphs::IOSectionParagraph.__init__)
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



def test_cobol::paragraphs::filecontrolparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol::paragraphs::FileControlParagraph)


def test_cobol::paragraphs::filecontrolparagraph_constructor_exists():
    assert callable(cobol::paragraphs::FileControlParagraph.__init__)


def test_cobol::paragraphs::filecontrolparagraph_constructor_args():
    sig = inspect.signature(cobol::paragraphs::FileControlParagraph.__init__)
    params = list(sig.parameters.keys())



def test_paragraphs::configurationsectionparagraph_is_not_abstract():
    assert not inspect.isabstract(paragraphs::ConfigurationSectionParagraph)


def test_paragraphs::configurationsectionparagraph_constructor_exists():
    assert callable(paragraphs::ConfigurationSectionParagraph.__init__)


def test_paragraphs::configurationsectionparagraph_constructor_args():
    sig = inspect.signature(paragraphs::ConfigurationSectionParagraph.__init__)
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



def test_cobol::paragraphs::specialnamesparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol::paragraphs::SpecialNamesParagraph)


def test_cobol::paragraphs::specialnamesparagraph_constructor_exists():
    assert callable(cobol::paragraphs::SpecialNamesParagraph.__init__)


def test_cobol::paragraphs::specialnamesparagraph_constructor_args():
    sig = inspect.signature(cobol::paragraphs::SpecialNamesParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol::paragraphs::sourcecomputerparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol::paragraphs::SourceComputerParagraph)


def test_cobol::paragraphs::sourcecomputerparagraph_constructor_exists():
    assert callable(cobol::paragraphs::SourceComputerParagraph.__init__)


def test_cobol::paragraphs::sourcecomputerparagraph_constructor_args():
    sig = inspect.signature(cobol::paragraphs::SourceComputerParagraph.__init__)
    params = list(sig.parameters.keys())



def test_labels::procedure_is_not_abstract():
    assert not inspect.isabstract(labels::Procedure)


def test_labels::procedure_constructor_exists():
    assert callable(labels::Procedure.__init__)


def test_labels::procedure_constructor_args():
    sig = inspect.signature(labels::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(GreaterThanOrEqual)


def test_greaterthanorequal_constructor_exists():
    assert callable(GreaterThanOrEqual.__init__)


def test_greaterthanorequal_constructor_args():
    sig = inspect.signature(GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::gteqsign_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::GTEQSign)


def test_cobol::operators::gteqsign_constructor_exists():
    assert callable(cobol::operators::GTEQSign.__init__)


def test_cobol::operators::gteqsign_constructor_args():
    sig = inspect.signature(cobol::operators::GTEQSign.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::gteqphrase_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::GTEQPhrase)


def test_cobol::operators::gteqphrase_constructor_exists():
    assert callable(cobol::operators::GTEQPhrase.__init__)


def test_cobol::operators::gteqphrase_constructor_args():
    sig = inspect.signature(cobol::operators::GTEQPhrase.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::gtsign_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::GTSign)


def test_cobol::operators::gtsign_constructor_exists():
    assert callable(cobol::operators::GTSign.__init__)


def test_cobol::operators::gtsign_constructor_args():
    sig = inspect.signature(cobol::operators::GTSign.__init__)
    params = list(sig.parameters.keys())



def test_operators::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(operators::UnaryOperator)


def test_operators::unaryoperator_constructor_exists():
    assert callable(operators::UnaryOperator.__init__)


def test_operators::unaryoperator_constructor_args():
    sig = inspect.signature(operators::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_operators::additiveoperator_is_not_abstract():
    assert not inspect.isabstract(operators::AdditiveOperator)


def test_operators::additiveoperator_constructor_exists():
    assert callable(operators::AdditiveOperator.__init__)


def test_operators::additiveoperator_constructor_args():
    sig = inspect.signature(operators::AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::subtraction_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Subtraction)


def test_cobol::operators::subtraction_constructor_exists():
    assert callable(cobol::operators::Subtraction.__init__)


def test_cobol::operators::subtraction_constructor_args():
    sig = inspect.signature(cobol::operators::Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::addition_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Addition)


def test_cobol::operators::addition_constructor_exists():
    assert callable(cobol::operators::Addition.__init__)


def test_cobol::operators::addition_constructor_args():
    sig = inspect.signature(cobol::operators::Addition.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::conditionand_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::ConditionAnd)


def test_cobol::operators::conditionand_constructor_exists():
    assert callable(cobol::operators::ConditionAnd.__init__)


def test_cobol::operators::conditionand_constructor_args():
    sig = inspect.signature(cobol::operators::ConditionAnd.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::conditionor_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::ConditionOr)


def test_cobol::operators::conditionor_constructor_exists():
    assert callable(cobol::operators::ConditionOr.__init__)


def test_cobol::operators::conditionor_constructor_args():
    sig = inspect.signature(cobol::operators::ConditionOr.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::relationaloperator_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::RelationalOperator)


def test_cobol::operators::relationaloperator_constructor_exists():
    assert callable(cobol::operators::RelationalOperator.__init__)


def test_cobol::operators::relationaloperator_constructor_args():
    sig = inspect.signature(cobol::operators::RelationalOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::UnaryOperator)


def test_cobol::operators::unaryoperator_constructor_exists():
    assert callable(cobol::operators::UnaryOperator.__init__)


def test_cobol::operators::unaryoperator_constructor_args():
    sig = inspect.signature(cobol::operators::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::logicaloperator_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::LogicalOperator)


def test_cobol::operators::logicaloperator_constructor_exists():
    assert callable(cobol::operators::LogicalOperator.__init__)


def test_cobol::operators::logicaloperator_constructor_args():
    sig = inspect.signature(cobol::operators::LogicalOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::MultiplicativeOperator)


def test_cobol::operators::multiplicativeoperator_constructor_exists():
    assert callable(cobol::operators::MultiplicativeOperator.__init__)


def test_cobol::operators::multiplicativeoperator_constructor_args():
    sig = inspect.signature(cobol::operators::MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::signoperator_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::SignOperator)


def test_cobol::operators::signoperator_constructor_exists():
    assert callable(cobol::operators::SignOperator.__init__)


def test_cobol::operators::signoperator_constructor_args():
    sig = inspect.signature(cobol::operators::SignOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::additiveoperator_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::AdditiveOperator)


def test_cobol::operators::additiveoperator_constructor_exists():
    assert callable(cobol::operators::AdditiveOperator.__init__)


def test_cobol::operators::additiveoperator_constructor_args():
    sig = inspect.signature(cobol::operators::AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::operator_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Operator)


def test_cobol::operators::operator_constructor_exists():
    assert callable(cobol::operators::Operator.__init__)


def test_cobol::operators::operator_constructor_args():
    sig = inspect.signature(cobol::operators::Operator.__init__)
    params = list(sig.parameters.keys())



def test_alphanumericliteral_is_not_abstract():
    assert not inspect.isabstract(AlphanumericLiteral)


def test_alphanumericliteral_constructor_exists():
    assert callable(AlphanumericLiteral.__init__)


def test_alphanumericliteral_constructor_args():
    sig = inspect.signature(AlphanumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::alphanumerichexadecimalliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::AlphanumericHexaDecimalLiteral)


def test_cobol::literals::alphanumerichexadecimalliteral_constructor_exists():
    assert callable(cobol::literals::AlphanumericHexaDecimalLiteral.__init__)


def test_cobol::literals::alphanumerichexadecimalliteral_constructor_args():
    sig = inspect.signature(cobol::literals::AlphanumericHexaDecimalLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::classoperator_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::ClassOperator)


def test_cobol::operators::classoperator_constructor_exists():
    assert callable(cobol::operators::ClassOperator.__init__)


def test_cobol::operators::classoperator_constructor_args():
    sig = inspect.signature(cobol::operators::ClassOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::through_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Through)


def test_cobol::operators::through_constructor_exists():
    assert callable(cobol::operators::Through.__init__)


def test_cobol::operators::through_constructor_args():
    sig = inspect.signature(cobol::operators::Through.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::operators::through_has_value():
    assert hasattr(cobol::operators::Through, "value")
    descriptor = None
    for klass in cobol::operators::Through.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::operators::negate_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Negate)


def test_cobol::operators::negate_constructor_exists():
    assert callable(cobol::operators::Negate.__init__)


def test_cobol::operators::negate_constructor_args():
    sig = inspect.signature(cobol::operators::Negate.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::power_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Power)


def test_cobol::operators::power_constructor_exists():
    assert callable(cobol::operators::Power.__init__)


def test_cobol::operators::power_constructor_args():
    sig = inspect.signature(cobol::operators::Power.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::equal_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Equal)


def test_cobol::operators::equal_constructor_exists():
    assert callable(cobol::operators::Equal.__init__)


def test_cobol::operators::equal_constructor_args():
    sig = inspect.signature(cobol::operators::Equal.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_cobol::operators::equal_has_to():
    assert hasattr(cobol::operators::Equal, "to")
    descriptor = None
    for klass in cobol::operators::Equal.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_cobol::operators::lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::LessThanOrEqual)


def test_cobol::operators::lessthanorequal_constructor_exists():
    assert callable(cobol::operators::LessThanOrEqual.__init__)


def test_cobol::operators::lessthanorequal_constructor_args():
    sig = inspect.signature(cobol::operators::LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())
    assert "than" in params, "Missing parameter 'than'"
    assert "to" in params, "Missing parameter 'to'"

def test_cobol::operators::lessthanorequal_has_than():
    assert hasattr(cobol::operators::LessThanOrEqual, "than")
    descriptor = None
    for klass in cobol::operators::LessThanOrEqual.__mro__:
        if "than" in klass.__dict__:
            descriptor = klass.__dict__["than"]
            break
    assert isinstance(descriptor, property)

def test_cobol::operators::lessthanorequal_has_to():
    assert hasattr(cobol::operators::LessThanOrEqual, "to")
    descriptor = None
    for klass in cobol::operators::LessThanOrEqual.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_cobol::operators::lessthan_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::LessThan)


def test_cobol::operators::lessthan_constructor_exists():
    assert callable(cobol::operators::LessThan.__init__)


def test_cobol::operators::lessthan_constructor_args():
    sig = inspect.signature(cobol::operators::LessThan.__init__)
    params = list(sig.parameters.keys())
    assert "than" in params, "Missing parameter 'than'"

def test_cobol::operators::lessthan_has_than():
    assert hasattr(cobol::operators::LessThan, "than")
    descriptor = None
    for klass in cobol::operators::LessThan.__mro__:
        if "than" in klass.__dict__:
            descriptor = klass.__dict__["than"]
            break
    assert isinstance(descriptor, property)



def test_cobol::operators::greaterthan_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::GreaterThan)


def test_cobol::operators::greaterthan_constructor_exists():
    assert callable(cobol::operators::GreaterThan.__init__)


def test_cobol::operators::greaterthan_constructor_args():
    sig = inspect.signature(cobol::operators::GreaterThan.__init__)
    params = list(sig.parameters.keys())
    assert "than" in params, "Missing parameter 'than'"

def test_cobol::operators::greaterthan_has_than():
    assert hasattr(cobol::operators::GreaterThan, "than")
    descriptor = None
    for klass in cobol::operators::GreaterThan.__mro__:
        if "than" in klass.__dict__:
            descriptor = klass.__dict__["than"]
            break
    assert isinstance(descriptor, property)



def test_cobol::operators::greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::GreaterThanOrEqual)


def test_cobol::operators::greaterthanorequal_constructor_exists():
    assert callable(cobol::operators::GreaterThanOrEqual.__init__)


def test_cobol::operators::greaterthanorequal_constructor_args():
    sig = inspect.signature(cobol::operators::GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "than" in params, "Missing parameter 'than'"

def test_cobol::operators::greaterthanorequal_has_to():
    assert hasattr(cobol::operators::GreaterThanOrEqual, "to")
    descriptor = None
    for klass in cobol::operators::GreaterThanOrEqual.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_cobol::operators::greaterthanorequal_has_than():
    assert hasattr(cobol::operators::GreaterThanOrEqual, "than")
    descriptor = None
    for klass in cobol::operators::GreaterThanOrEqual.__mro__:
        if "than" in klass.__dict__:
            descriptor = klass.__dict__["than"]
            break
    assert isinstance(descriptor, property)



def test_dbcsliteral_is_not_abstract():
    assert not inspect.isabstract(DBCSLiteral)


def test_dbcsliteral_constructor_exists():
    assert callable(DBCSLiteral.__init__)


def test_dbcsliteral_constructor_args():
    sig = inspect.signature(DBCSLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::nationalhexliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::NationalHexLiteral)


def test_cobol::literals::nationalhexliteral_constructor_exists():
    assert callable(cobol::literals::NationalHexLiteral.__init__)


def test_cobol::literals::nationalhexliteral_constructor_args():
    sig = inspect.signature(cobol::literals::NationalHexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::nationalhexliteral_has_value():
    assert hasattr(cobol::literals::NationalHexLiteral, "value")
    descriptor = None
    for klass in cobol::literals::NationalHexLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::literals::nationalliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::NationalLiteral)


def test_cobol::literals::nationalliteral_constructor_exists():
    assert callable(cobol::literals::NationalLiteral.__init__)


def test_cobol::literals::nationalliteral_constructor_args():
    sig = inspect.signature(cobol::literals::NationalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::nationalliteral_has_value():
    assert hasattr(cobol::literals::NationalLiteral, "value")
    descriptor = None
    for klass in cobol::literals::NationalLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_labels::stoplabel_is_not_abstract():
    assert not inspect.isabstract(labels::StopLabel)


def test_labels::stoplabel_constructor_exists():
    assert callable(labels::StopLabel.__init__)


def test_labels::stoplabel_constructor_args():
    sig = inspect.signature(labels::StopLabel.__init__)
    params = list(sig.parameters.keys())



def test_constantliteral_is_not_abstract():
    assert not inspect.isabstract(ConstantLiteral)


def test_constantliteral_constructor_exists():
    assert callable(ConstantLiteral.__init__)


def test_constantliteral_constructor_args():
    sig = inspect.signature(ConstantLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::highvalue_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::HighValue)


def test_cobol::literals::highvalue_constructor_exists():
    assert callable(cobol::literals::HighValue.__init__)


def test_cobol::literals::highvalue_constructor_args():
    sig = inspect.signature(cobol::literals::HighValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::highvalue_has_value():
    assert hasattr(cobol::literals::HighValue, "value")
    descriptor = None
    for klass in cobol::literals::HighValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::literals::lowvalue_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::LowValue)


def test_cobol::literals::lowvalue_constructor_exists():
    assert callable(cobol::literals::LowValue.__init__)


def test_cobol::literals::lowvalue_constructor_args():
    sig = inspect.signature(cobol::literals::LowValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::lowvalue_has_value():
    assert hasattr(cobol::literals::LowValue, "value")
    descriptor = None
    for klass in cobol::literals::LowValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::literals::quote_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::Quote)


def test_cobol::literals::quote_constructor_exists():
    assert callable(cobol::literals::Quote.__init__)


def test_cobol::literals::quote_constructor_args():
    sig = inspect.signature(cobol::literals::Quote.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::quote_has_value():
    assert hasattr(cobol::literals::Quote, "value")
    descriptor = None
    for klass in cobol::literals::Quote.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::literals::null_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::Null)


def test_cobol::literals::null_constructor_exists():
    assert callable(cobol::literals::Null.__init__)


def test_cobol::literals::null_constructor_args():
    sig = inspect.signature(cobol::literals::Null.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::null_has_value():
    assert hasattr(cobol::literals::Null, "value")
    descriptor = None
    for klass in cobol::literals::Null.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::literals::zero_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::Zero)


def test_cobol::literals::zero_constructor_exists():
    assert callable(cobol::literals::Zero.__init__)


def test_cobol::literals::zero_constructor_args():
    sig = inspect.signature(cobol::literals::Zero.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::zero_has_value():
    assert hasattr(cobol::literals::Zero, "value")
    descriptor = None
    for klass in cobol::literals::Zero.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::literals::space_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::Space)


def test_cobol::literals::space_constructor_exists():
    assert callable(cobol::literals::Space.__init__)


def test_cobol::literals::space_constructor_args():
    sig = inspect.signature(cobol::literals::Space.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::space_has_value():
    assert hasattr(cobol::literals::Space, "value")
    descriptor = None
    for klass in cobol::literals::Space.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_figurativeconstantliteral_is_not_abstract():
    assert not inspect.isabstract(FigurativeConstantLiteral)


def test_figurativeconstantliteral_constructor_exists():
    assert callable(FigurativeConstantLiteral.__init__)


def test_figurativeconstantliteral_constructor_args():
    sig = inspect.signature(FigurativeConstantLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::constantliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::ConstantLiteral)


def test_cobol::literals::constantliteral_constructor_exists():
    assert callable(cobol::literals::ConstantLiteral.__init__)


def test_cobol::literals::constantliteral_constructor_args():
    sig = inspect.signature(cobol::literals::ConstantLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::allliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::AllLiteral)


def test_cobol::literals::allliteral_constructor_exists():
    assert callable(cobol::literals::AllLiteral.__init__)


def test_cobol::literals::allliteral_constructor_args():
    sig = inspect.signature(cobol::literals::AllLiteral.__init__)
    params = list(sig.parameters.keys())



def test_decimalliteral_is_not_abstract():
    assert not inspect.isabstract(DecimalLiteral)


def test_decimalliteral_constructor_exists():
    assert callable(DecimalLiteral.__init__)


def test_decimalliteral_constructor_args():
    sig = inspect.signature(DecimalLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::fixeddecimalliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::FixedDecimalLiteral)


def test_cobol::literals::fixeddecimalliteral_constructor_exists():
    assert callable(cobol::literals::FixedDecimalLiteral.__init__)


def test_cobol::literals::fixeddecimalliteral_constructor_args():
    sig = inspect.signature(cobol::literals::FixedDecimalLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::floatingdecimalliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::FloatingDecimalLiteral)


def test_cobol::literals::floatingdecimalliteral_constructor_exists():
    assert callable(cobol::literals::FloatingDecimalLiteral.__init__)


def test_cobol::literals::floatingdecimalliteral_constructor_args():
    sig = inspect.signature(cobol::literals::FloatingDecimalLiteral.__init__)
    params = list(sig.parameters.keys())



def test_numericliteral_is_not_abstract():
    assert not inspect.isabstract(NumericLiteral)


def test_numericliteral_constructor_exists():
    assert callable(NumericLiteral.__init__)


def test_numericliteral_constructor_args():
    sig = inspect.signature(NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::decimalliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::DecimalLiteral)


def test_cobol::literals::decimalliteral_constructor_exists():
    assert callable(cobol::literals::DecimalLiteral.__init__)


def test_cobol::literals::decimalliteral_constructor_args():
    sig = inspect.signature(cobol::literals::DecimalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::decimalliteral_has_value():
    assert hasattr(cobol::literals::DecimalLiteral, "value")
    descriptor = None
    for klass in cobol::literals::DecimalLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_water::iocontrolparagraphwater_is_not_abstract():
    assert not inspect.isabstract(water::IOControlParagraphWater)


def test_water::iocontrolparagraphwater_constructor_exists():
    assert callable(water::IOControlParagraphWater.__init__)


def test_water::iocontrolparagraphwater_constructor_args():
    sig = inspect.signature(water::IOControlParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_water::filedescriptorwater_is_not_abstract():
    assert not inspect.isabstract(water::FileDescriptorWater)


def test_water::filedescriptorwater_constructor_exists():
    assert callable(water::FileDescriptorWater.__init__)


def test_water::filedescriptorwater_constructor_args():
    sig = inspect.signature(water::FileDescriptorWater.__init__)
    params = list(sig.parameters.keys())



def test_water::objectcomputerparagraphwater_is_not_abstract():
    assert not inspect.isabstract(water::ObjectComputerParagraphWater)


def test_water::objectcomputerparagraphwater_constructor_exists():
    assert callable(water::ObjectComputerParagraphWater.__init__)


def test_water::objectcomputerparagraphwater_constructor_args():
    sig = inspect.signature(water::ObjectComputerParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_literals::numericliteral_is_not_abstract():
    assert not inspect.isabstract(literals::NumericLiteral)


def test_literals::numericliteral_constructor_exists():
    assert callable(literals::NumericLiteral.__init__)


def test_literals::numericliteral_constructor_args():
    sig = inspect.signature(literals::NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::integerliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::IntegerLiteral)


def test_cobol::literals::integerliteral_constructor_exists():
    assert callable(cobol::literals::IntegerLiteral.__init__)


def test_cobol::literals::integerliteral_constructor_args():
    sig = inspect.signature(cobol::literals::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::integerliteral_has_value():
    assert hasattr(cobol::literals::IntegerLiteral, "value")
    descriptor = None
    for klass in cobol::literals::IntegerLiteral.__mro__:
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



def test_cobol::literals::numericliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::NumericLiteral)


def test_cobol::literals::numericliteral_constructor_exists():
    assert callable(cobol::literals::NumericLiteral.__init__)


def test_cobol::literals::numericliteral_constructor_args():
    sig = inspect.signature(cobol::literals::NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::any_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::Any)


def test_cobol::literals::any_constructor_exists():
    assert callable(cobol::literals::Any.__init__)


def test_cobol::literals::any_constructor_args():
    sig = inspect.signature(cobol::literals::Any.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::figurativeconstantliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::FigurativeConstantLiteral)


def test_cobol::literals::figurativeconstantliteral_constructor_exists():
    assert callable(cobol::literals::FigurativeConstantLiteral.__init__)


def test_cobol::literals::figurativeconstantliteral_constructor_args():
    sig = inspect.signature(cobol::literals::FigurativeConstantLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::dbcsliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::DBCSLiteral)


def test_cobol::literals::dbcsliteral_constructor_exists():
    assert callable(cobol::literals::DBCSLiteral.__init__)


def test_cobol::literals::dbcsliteral_constructor_args():
    sig = inspect.signature(cobol::literals::DBCSLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::pseudoliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::PseudoLiteral)


def test_cobol::literals::pseudoliteral_constructor_exists():
    assert callable(cobol::literals::PseudoLiteral.__init__)


def test_cobol::literals::pseudoliteral_constructor_args():
    sig = inspect.signature(cobol::literals::PseudoLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::pseudoliteral_has_value():
    assert hasattr(cobol::literals::PseudoLiteral, "value")
    descriptor = None
    for klass in cobol::literals::PseudoLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::literals::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::BooleanLiteral)


def test_cobol::literals::booleanliteral_constructor_exists():
    assert callable(cobol::literals::BooleanLiteral.__init__)


def test_cobol::literals::booleanliteral_constructor_args():
    sig = inspect.signature(cobol::literals::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::booleanliteral_has_value():
    assert hasattr(cobol::literals::BooleanLiteral, "value")
    descriptor = None
    for klass in cobol::literals::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cobol::literals::characters_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::Characters)


def test_cobol::literals::characters_constructor_exists():
    assert callable(cobol::literals::Characters.__init__)


def test_cobol::literals::characters_constructor_args():
    sig = inspect.signature(cobol::literals::Characters.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::alphanumericliteral_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::AlphanumericLiteral)


def test_cobol::literals::alphanumericliteral_constructor_exists():
    assert callable(cobol::literals::AlphanumericLiteral.__init__)


def test_cobol::literals::alphanumericliteral_constructor_args():
    sig = inspect.signature(cobol::literals::AlphanumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cobol::literals::alphanumericliteral_has_value():
    assert hasattr(cobol::literals::AlphanumericLiteral, "value")
    descriptor = None
    for klass in cobol::literals::AlphanumericLiteral.__mro__:
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



def test_cobol::divisions::environmentdivision_is_not_abstract():
    assert not inspect.isabstract(cobol::divisions::EnvironmentDivision)


def test_cobol::divisions::environmentdivision_constructor_exists():
    assert callable(cobol::divisions::EnvironmentDivision.__init__)


def test_cobol::divisions::environmentdivision_constructor_args():
    sig = inspect.signature(cobol::divisions::EnvironmentDivision.__init__)
    params = list(sig.parameters.keys())



def test_cobol::divisions::datadivision_is_not_abstract():
    assert not inspect.isabstract(cobol::divisions::DataDivision)


def test_cobol::divisions::datadivision_constructor_exists():
    assert callable(cobol::divisions::DataDivision.__init__)


def test_cobol::divisions::datadivision_constructor_args():
    sig = inspect.signature(cobol::divisions::DataDivision.__init__)
    params = list(sig.parameters.keys())



def test_statementcontainer_is_not_abstract():
    assert not inspect.isabstract(StatementContainer)


def test_statementcontainer_constructor_exists():
    assert callable(StatementContainer.__init__)


def test_statementcontainer_constructor_args():
    sig = inspect.signature(StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sentences::sentence_is_not_abstract():
    assert not inspect.isabstract(cobol::sentences::Sentence)


def test_cobol::sentences::sentence_constructor_exists():
    assert callable(cobol::sentences::Sentence.__init__)


def test_cobol::sentences::sentence_constructor_args():
    sig = inspect.signature(cobol::sentences::Sentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sentences::executesentence_is_not_abstract():
    assert not inspect.isabstract(cobol::sentences::ExecuteSentence)


def test_cobol::sentences::executesentence_constructor_exists():
    assert callable(cobol::sentences::ExecuteSentence.__init__)


def test_cobol::sentences::executesentence_constructor_args():
    sig = inspect.signature(cobol::sentences::ExecuteSentence.__init__)
    params = list(sig.parameters.keys())



def test_paragraph_is_not_abstract():
    assert not inspect.isabstract(Paragraph)


def test_paragraph_constructor_exists():
    assert callable(Paragraph.__init__)


def test_paragraph_constructor_args():
    sig = inspect.signature(Paragraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol::paragraphs::iosectionparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol::paragraphs::IOSectionParagraph)


def test_cobol::paragraphs::iosectionparagraph_constructor_exists():
    assert callable(cobol::paragraphs::IOSectionParagraph.__init__)


def test_cobol::paragraphs::iosectionparagraph_constructor_args():
    sig = inspect.signature(cobol::paragraphs::IOSectionParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol::paragraphs::configurationsectionparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol::paragraphs::ConfigurationSectionParagraph)


def test_cobol::paragraphs::configurationsectionparagraph_constructor_exists():
    assert callable(cobol::paragraphs::ConfigurationSectionParagraph.__init__)


def test_cobol::paragraphs::configurationsectionparagraph_constructor_args():
    sig = inspect.signature(cobol::paragraphs::ConfigurationSectionParagraph.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sections::declarativesection_is_not_abstract():
    assert not inspect.isabstract(cobol::sections::DeclarativeSection)


def test_cobol::sections::declarativesection_constructor_exists():
    assert callable(cobol::sections::DeclarativeSection.__init__)


def test_cobol::sections::declarativesection_constructor_args():
    sig = inspect.signature(cobol::sections::DeclarativeSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sections::datadivisionsection_is_not_abstract():
    assert not inspect.isabstract(cobol::sections::DataDivisionSection)


def test_cobol::sections::datadivisionsection_constructor_exists():
    assert callable(cobol::sections::DataDivisionSection.__init__)


def test_cobol::sections::datadivisionsection_constructor_args():
    sig = inspect.signature(cobol::sections::DataDivisionSection.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sections::environmentdivisionsection_is_not_abstract():
    assert not inspect.isabstract(cobol::sections::EnvironmentDivisionSection)


def test_cobol::sections::environmentdivisionsection_constructor_exists():
    assert callable(cobol::sections::EnvironmentDivisionSection.__init__)


def test_cobol::sections::environmentdivisionsection_constructor_args():
    sig = inspect.signature(cobol::sections::EnvironmentDivisionSection.__init__)
    params = list(sig.parameters.keys())



def test_cobolroot_is_not_abstract():
    assert not inspect.isabstract(CobolRoot)


def test_cobolroot_constructor_exists():
    assert callable(CobolRoot.__init__)


def test_cobolroot_constructor_args():
    sig = inspect.signature(CobolRoot.__init__)
    params = list(sig.parameters.keys())



def test_cobol::containers::emptymodel_is_not_abstract():
    assert not inspect.isabstract(cobol::containers::EmptyModel)


def test_cobol::containers::emptymodel_constructor_exists():
    assert callable(cobol::containers::EmptyModel.__init__)


def test_cobol::containers::emptymodel_constructor_args():
    sig = inspect.signature(cobol::containers::EmptyModel.__init__)
    params = list(sig.parameters.keys())



def test_cobol::containers::cobolroot_is_not_abstract():
    assert not inspect.isabstract(cobol::containers::CobolRoot)


def test_cobol::containers::cobolroot_constructor_exists():
    assert callable(cobol::containers::CobolRoot.__init__)


def test_cobol::containers::cobolroot_constructor_args():
    sig = inspect.signature(cobol::containers::CobolRoot.__init__)
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



def test_water::invokestatementwater_is_not_abstract():
    assert not inspect.isabstract(water::InvokeStatementWater)


def test_water::invokestatementwater_constructor_exists():
    assert callable(water::InvokeStatementWater.__init__)


def test_water::invokestatementwater_constructor_args():
    sig = inspect.signature(water::InvokeStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_operands::primaryoperand_is_not_abstract():
    assert not inspect.isabstract(operands::PrimaryOperand)


def test_operands::primaryoperand_constructor_exists():
    assert callable(operands::PrimaryOperand.__init__)


def test_operands::primaryoperand_constructor_args():
    sig = inspect.signature(operands::PrimaryOperand.__init__)
    params = list(sig.parameters.keys())



def test_water::cicsstatementwater_is_not_abstract():
    assert not inspect.isabstract(water::CICSStatementWater)


def test_water::cicsstatementwater_constructor_exists():
    assert callable(water::CICSStatementWater.__init__)


def test_water::cicsstatementwater_constructor_args():
    sig = inspect.signature(water::CICSStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_water::specialnamesparagraphwater_is_not_abstract():
    assert not inspect.isabstract(water::SpecialNamesParagraphWater)


def test_water::specialnamesparagraphwater_constructor_exists():
    assert callable(water::SpecialNamesParagraphWater.__init__)


def test_water::specialnamesparagraphwater_constructor_args():
    sig = inspect.signature(water::SpecialNamesParagraphWater.__init__)
    params = list(sig.parameters.keys())



def test_water::selectstatementwater_is_not_abstract():
    assert not inspect.isabstract(water::SelectStatementWater)


def test_water::selectstatementwater_constructor_exists():
    assert callable(water::SelectStatementWater.__init__)


def test_water::selectstatementwater_constructor_args():
    sig = inspect.signature(water::SelectStatementWater.__init__)
    params = list(sig.parameters.keys())



def test_cobol::identifiers::identifier_is_not_abstract():
    assert not inspect.isabstract(cobol::identifiers::Identifier)


def test_cobol::identifiers::identifier_constructor_exists():
    assert callable(cobol::identifiers::Identifier.__init__)


def test_cobol::identifiers::identifier_constructor_args():
    sig = inspect.signature(cobol::identifiers::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_cobol::literals::literal_is_not_abstract():
    assert not inspect.isabstract(cobol::literals::Literal)


def test_cobol::literals::literal_constructor_exists():
    assert callable(cobol::literals::Literal.__init__)


def test_cobol::literals::literal_constructor_args():
    sig = inspect.signature(cobol::literals::Literal.__init__)
    params = list(sig.parameters.keys())



def test_declaratives_is_not_abstract():
    assert not inspect.isabstract(Declaratives)


def test_declaratives_constructor_exists():
    assert callable(Declaratives.__init__)


def test_declaratives_constructor_args():
    sig = inspect.signature(Declaratives.__init__)
    params = list(sig.parameters.keys())



def test_parameters::parametrizable_is_not_abstract():
    assert not inspect.isabstract(parameters::Parametrizable)


def test_parameters::parametrizable_constructor_exists():
    assert callable(parameters::Parametrizable.__init__)


def test_parameters::parametrizable_constructor_args():
    sig = inspect.signature(parameters::Parametrizable.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::entry_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Entry)


def test_cobol::statements::entry_constructor_exists():
    assert callable(cobol::statements::Entry.__init__)


def test_cobol::statements::entry_constructor_args():
    sig = inspect.signature(cobol::statements::Entry.__init__)
    params = list(sig.parameters.keys())



def test_water::incompleteelement_is_not_abstract():
    assert not inspect.isabstract(water::IncompleteElement)


def test_water::incompleteelement_constructor_exists():
    assert callable(water::IncompleteElement.__init__)


def test_water::incompleteelement_constructor_args():
    sig = inspect.signature(water::IncompleteElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::files::filename_is_not_abstract():
    assert not inspect.isabstract(cobol::files::FileName)


def test_cobol::files::filename_constructor_exists():
    assert callable(cobol::files::FileName.__init__)


def test_cobol::files::filename_constructor_args():
    sig = inspect.signature(cobol::files::FileName.__init__)
    params = list(sig.parameters.keys())
    assert "fileDescriptor" in params, "Missing parameter 'fileDescriptor'"

def test_cobol::files::filename_has_fileDescriptor():
    assert hasattr(cobol::files::FileName, "fileDescriptor")
    descriptor = None
    for klass in cobol::files::FileName.__mro__:
        if "fileDescriptor" in klass.__dict__:
            descriptor = klass.__dict__["fileDescriptor"]
            break
    assert isinstance(descriptor, property)



def test_cobol::statements::merge_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Merge)


def test_cobol::statements::merge_constructor_exists():
    assert callable(cobol::statements::Merge.__init__)


def test_cobol::statements::merge_constructor_args():
    sig = inspect.signature(cobol::statements::Merge.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::accept_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Accept)


def test_cobol::statements::accept_constructor_exists():
    assert callable(cobol::statements::Accept.__init__)


def test_cobol::statements::accept_constructor_args():
    sig = inspect.signature(cobol::statements::Accept.__init__)
    params = list(sig.parameters.keys())



def test_cobol::dataitems::dataitem_is_not_abstract():
    assert not inspect.isabstract(cobol::dataitems::DataItem)


def test_cobol::dataitems::dataitem_constructor_exists():
    assert callable(cobol::dataitems::DataItem.__init__)


def test_cobol::dataitems::dataitem_constructor_args():
    sig = inspect.signature(cobol::dataitems::DataItem.__init__)
    params = list(sig.parameters.keys())
    assert "levelNumber" in params, "Missing parameter 'levelNumber'"

def test_cobol::dataitems::dataitem_has_levelNumber():
    assert hasattr(cobol::dataitems::DataItem, "levelNumber")
    descriptor = None
    for klass in cobol::dataitems::DataItem.__mro__:
        if "levelNumber" in klass.__dict__:
            descriptor = klass.__dict__["levelNumber"]
            break
    assert isinstance(descriptor, property)



def test_cobol::paragraphs::repositoryparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol::paragraphs::RepositoryParagraph)


def test_cobol::paragraphs::repositoryparagraph_constructor_exists():
    assert callable(cobol::paragraphs::RepositoryParagraph.__init__)


def test_cobol::paragraphs::repositoryparagraph_constructor_args():
    sig = inspect.signature(cobol::paragraphs::RepositoryParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::sort_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Sort)


def test_cobol::statements::sort_constructor_exists():
    assert callable(cobol::statements::Sort.__init__)


def test_cobol::statements::sort_constructor_args():
    sig = inspect.signature(cobol::statements::Sort.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::open_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Open)


def test_cobol::statements::open_constructor_exists():
    assert callable(cobol::statements::Open.__init__)


def test_cobol::statements::open_constructor_args():
    sig = inspect.signature(cobol::statements::Open.__init__)
    params = list(sig.parameters.keys())



def test_cobol::paragraphs::iocontrolparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol::paragraphs::IOControlParagraph)


def test_cobol::paragraphs::iocontrolparagraph_constructor_exists():
    assert callable(cobol::paragraphs::IOControlParagraph.__init__)


def test_cobol::paragraphs::iocontrolparagraph_constructor_args():
    sig = inspect.signature(cobol::paragraphs::IOControlParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol::paragraphs::objectcomputerparagraph_is_not_abstract():
    assert not inspect.isabstract(cobol::paragraphs::ObjectComputerParagraph)


def test_cobol::paragraphs::objectcomputerparagraph_constructor_exists():
    assert callable(cobol::paragraphs::ObjectComputerParagraph.__init__)


def test_cobol::paragraphs::objectcomputerparagraph_constructor_args():
    sig = inspect.signature(cobol::paragraphs::ObjectComputerParagraph.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sentences::usesentence_is_not_abstract():
    assert not inspect.isabstract(cobol::sentences::UseSentence)


def test_cobol::sentences::usesentence_constructor_exists():
    assert callable(cobol::sentences::UseSentence.__init__)


def test_cobol::sentences::usesentence_constructor_args():
    sig = inspect.signature(cobol::sentences::UseSentence.__init__)
    params = list(sig.parameters.keys())



def test_cobol::tables::table_is_not_abstract():
    assert not inspect.isabstract(cobol::tables::Table)


def test_cobol::tables::table_constructor_exists():
    assert callable(cobol::tables::Table.__init__)


def test_cobol::tables::table_constructor_args():
    sig = inspect.signature(cobol::tables::Table.__init__)
    params = list(sig.parameters.keys())



def test_cobol::statements::close_is_not_abstract():
    assert not inspect.isabstract(cobol::statements::Close)


def test_cobol::statements::close_constructor_exists():
    assert callable(cobol::statements::Close.__init__)


def test_cobol::statements::close_constructor_args():
    sig = inspect.signature(cobol::statements::Close.__init__)
    params = list(sig.parameters.keys())



def test_divisions::division_is_not_abstract():
    assert not inspect.isabstract(divisions::Division)


def test_divisions::division_constructor_exists():
    assert callable(divisions::Division.__init__)


def test_divisions::division_constructor_args():
    sig = inspect.signature(divisions::Division.__init__)
    params = list(sig.parameters.keys())



def test_cobol::divisions::proceduredivision_is_not_abstract():
    assert not inspect.isabstract(cobol::divisions::ProcedureDivision)


def test_cobol::divisions::proceduredivision_constructor_exists():
    assert callable(cobol::divisions::ProcedureDivision.__init__)


def test_cobol::divisions::proceduredivision_constructor_args():
    sig = inspect.signature(cobol::divisions::ProcedureDivision.__init__)
    params = list(sig.parameters.keys())



def test_cobol::divisions::identificationdivision_is_not_abstract():
    assert not inspect.isabstract(cobol::divisions::IdentificationDivision)


def test_cobol::divisions::identificationdivision_constructor_exists():
    assert callable(cobol::divisions::IdentificationDivision.__init__)


def test_cobol::divisions::identificationdivision_constructor_args():
    sig = inspect.signature(cobol::divisions::IdentificationDivision.__init__)
    params = list(sig.parameters.keys())
    assert "properties" in params, "Missing parameter 'properties'"

def test_cobol::divisions::identificationdivision_has_properties():
    assert hasattr(cobol::divisions::IdentificationDivision, "properties")
    descriptor = None
    for klass in cobol::divisions::IdentificationDivision.__mro__:
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



def test_cobol::arithmetics::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::RangeExpression)


def test_cobol::arithmetics::rangeexpression_constructor_exists():
    assert callable(cobol::arithmetics::RangeExpression.__init__)


def test_cobol::arithmetics::rangeexpression_constructor_args():
    sig = inspect.signature(cobol::arithmetics::RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_equal_is_not_abstract():
    assert not inspect.isabstract(Equal)


def test_equal_constructor_exists():
    assert callable(Equal.__init__)


def test_equal_constructor_args():
    sig = inspect.signature(Equal.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::equalphrase_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::EqualPhrase)


def test_cobol::operators::equalphrase_constructor_exists():
    assert callable(cobol::operators::EqualPhrase.__init__)


def test_cobol::operators::equalphrase_constructor_args():
    sig = inspect.signature(cobol::operators::EqualPhrase.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::equalsign_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::EqualSign)


def test_cobol::operators::equalsign_constructor_exists():
    assert callable(cobol::operators::EqualSign.__init__)


def test_cobol::operators::equalsign_constructor_args():
    sig = inspect.signature(cobol::operators::EqualSign.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::AssignmentExpression)


def test_cobol::arithmetics::assignmentexpression_constructor_exists():
    assert callable(cobol::arithmetics::AssignmentExpression.__init__)


def test_cobol::arithmetics::assignmentexpression_constructor_args():
    sig = inspect.signature(cobol::arithmetics::AssignmentExpression.__init__)
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



def test_cobol::arithmetics::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::PrimaryExpression)


def test_cobol::arithmetics::primaryexpression_constructor_exists():
    assert callable(cobol::arithmetics::PrimaryExpression.__init__)


def test_cobol::arithmetics::primaryexpression_constructor_args():
    sig = inspect.signature(cobol::arithmetics::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_powerarithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(PowerArithmeticExpressionChild)


def test_powerarithmeticexpressionchild_constructor_exists():
    assert callable(PowerArithmeticExpressionChild.__init__)


def test_powerarithmeticexpressionchild_constructor_args():
    sig = inspect.signature(PowerArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::unaryarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::UnaryArithmeticExpression)


def test_cobol::arithmetics::unaryarithmeticexpression_constructor_exists():
    assert callable(cobol::arithmetics::UnaryArithmeticExpression.__init__)


def test_cobol::arithmetics::unaryarithmeticexpression_constructor_args():
    sig = inspect.signature(cobol::arithmetics::UnaryArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::unaryarithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::UnaryArithmeticExpressionChild)


def test_cobol::arithmetics::unaryarithmeticexpressionchild_constructor_exists():
    assert callable(cobol::arithmetics::UnaryArithmeticExpressionChild.__init__)


def test_cobol::arithmetics::unaryarithmeticexpressionchild_constructor_args():
    sig = inspect.signature(cobol::arithmetics::UnaryArithmeticExpressionChild.__init__)
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



def test_cobol::divisions::division_is_not_abstract():
    assert not inspect.isabstract(cobol::divisions::Division)


def test_cobol::divisions::division_constructor_exists():
    assert callable(cobol::divisions::Division.__init__)


def test_cobol::divisions::division_constructor_args():
    sig = inspect.signature(cobol::divisions::Division.__init__)
    params = list(sig.parameters.keys())



def test_cobol::references::referenceableelement_is_not_abstract():
    assert not inspect.isabstract(cobol::references::ReferenceableElement)


def test_cobol::references::referenceableelement_constructor_exists():
    assert callable(cobol::references::ReferenceableElement.__init__)


def test_cobol::references::referenceableelement_constructor_args():
    sig = inspect.signature(cobol::references::ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::containers::compilationunit_is_not_abstract():
    assert not inspect.isabstract(cobol::containers::CompilationUnit)


def test_cobol::containers::compilationunit_constructor_exists():
    assert callable(cobol::containers::CompilationUnit.__init__)


def test_cobol::containers::compilationunit_constructor_args():
    sig = inspect.signature(cobol::containers::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_commons::namedelement_is_not_abstract():
    assert not inspect.isabstract(commons::NamedElement)


def test_commons::namedelement_constructor_exists():
    assert callable(commons::NamedElement.__init__)


def test_commons::namedelement_constructor_args():
    sig = inspect.signature(commons::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_cobol::functions::functioncall_is_not_abstract():
    assert not inspect.isabstract(cobol::functions::FunctionCall)


def test_cobol::functions::functioncall_constructor_exists():
    assert callable(cobol::functions::FunctionCall.__init__)


def test_cobol::functions::functioncall_constructor_args():
    sig = inspect.signature(cobol::functions::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_cobol::sections::section_is_not_abstract():
    assert not inspect.isabstract(cobol::sections::Section)


def test_cobol::sections::section_constructor_exists():
    assert callable(cobol::sections::Section.__init__)


def test_cobol::sections::section_constructor_args():
    sig = inspect.signature(cobol::sections::Section.__init__)
    params = list(sig.parameters.keys())
    assert "segmentNumber" in params, "Missing parameter 'segmentNumber'"

def test_cobol::sections::section_has_segmentNumber():
    assert hasattr(cobol::sections::Section, "segmentNumber")
    descriptor = None
    for klass in cobol::sections::Section.__mro__:
        if "segmentNumber" in klass.__dict__:
            descriptor = klass.__dict__["segmentNumber"]
            break
    assert isinstance(descriptor, property)



def test_cobol::tables::indexname_is_not_abstract():
    assert not inspect.isabstract(cobol::tables::IndexName)


def test_cobol::tables::indexname_constructor_exists():
    assert callable(cobol::tables::IndexName.__init__)


def test_cobol::tables::indexname_constructor_args():
    sig = inspect.signature(cobol::tables::IndexName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::specialnames::conditionname_is_not_abstract():
    assert not inspect.isabstract(cobol::specialnames::ConditionName)


def test_cobol::specialnames::conditionname_constructor_exists():
    assert callable(cobol::specialnames::ConditionName.__init__)


def test_cobol::specialnames::conditionname_constructor_args():
    sig = inspect.signature(cobol::specialnames::ConditionName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::paragraphs::paragraph_is_not_abstract():
    assert not inspect.isabstract(cobol::paragraphs::Paragraph)


def test_cobol::paragraphs::paragraph_constructor_exists():
    assert callable(cobol::paragraphs::Paragraph.__init__)


def test_cobol::paragraphs::paragraph_constructor_args():
    sig = inspect.signature(cobol::paragraphs::Paragraph.__init__)
    params = list(sig.parameters.keys())



def test_containers::cobolroot_is_not_abstract():
    assert not inspect.isabstract(containers::CobolRoot)


def test_containers::cobolroot_constructor_exists():
    assert callable(containers::CobolRoot.__init__)


def test_containers::cobolroot_constructor_args():
    sig = inspect.signature(containers::CobolRoot.__init__)
    params = list(sig.parameters.keys())



def test_cobol::containers::compilationgroup_is_not_abstract():
    assert not inspect.isabstract(cobol::containers::CompilationGroup)


def test_cobol::containers::compilationgroup_constructor_exists():
    assert callable(cobol::containers::CompilationGroup.__init__)


def test_cobol::containers::compilationgroup_constructor_args():
    sig = inspect.signature(cobol::containers::CompilationGroup.__init__)
    params = list(sig.parameters.keys())



def test_conditions::simpleconditionchild_is_not_abstract():
    assert not inspect.isabstract(conditions::SimpleConditionChild)


def test_conditions::simpleconditionchild_constructor_exists():
    assert callable(conditions::SimpleConditionChild.__init__)


def test_conditions::simpleconditionchild_constructor_args():
    sig = inspect.signature(conditions::SimpleConditionChild.__init__)
    params = list(sig.parameters.keys())



def test_conditions::abbreviatedrelationalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(conditions::AbbreviatedRelationalExpressionChild)


def test_conditions::abbreviatedrelationalexpressionchild_constructor_exists():
    assert callable(conditions::AbbreviatedRelationalExpressionChild.__init__)


def test_conditions::abbreviatedrelationalexpressionchild_constructor_args():
    sig = inspect.signature(conditions::AbbreviatedRelationalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::ArithmeticExpression)


def test_cobol::arithmetics::arithmeticexpression_constructor_exists():
    assert callable(cobol::arithmetics::ArithmeticExpression.__init__)


def test_cobol::arithmetics::arithmeticexpression_constructor_args():
    sig = inspect.signature(cobol::arithmetics::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::nestedarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::NestedArithmeticExpression)


def test_cobol::arithmetics::nestedarithmeticexpression_constructor_exists():
    assert callable(cobol::arithmetics::NestedArithmeticExpression.__init__)


def test_cobol::arithmetics::nestedarithmeticexpression_constructor_args():
    sig = inspect.signature(cobol::arithmetics::NestedArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::rangeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::RangeExpressionChild)


def test_cobol::arithmetics::rangeexpressionchild_constructor_exists():
    assert callable(cobol::arithmetics::RangeExpressionChild.__init__)


def test_cobol::arithmetics::rangeexpressionchild_constructor_args():
    sig = inspect.signature(cobol::arithmetics::RangeExpressionChild.__init__)
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



def test_cobol::operators::classname_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::ClassName)


def test_cobol::operators::classname_constructor_exists():
    assert callable(cobol::operators::ClassName.__init__)


def test_cobol::operators::classname_constructor_args():
    sig = inspect.signature(cobol::operators::ClassName.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::dbcs_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::DBCS)


def test_cobol::operators::dbcs_constructor_exists():
    assert callable(cobol::operators::DBCS.__init__)


def test_cobol::operators::dbcs_constructor_args():
    sig = inspect.signature(cobol::operators::DBCS.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::kanji_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Kanji)


def test_cobol::operators::kanji_constructor_exists():
    assert callable(cobol::operators::Kanji.__init__)


def test_cobol::operators::kanji_constructor_args():
    sig = inspect.signature(cobol::operators::Kanji.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::alphabeticlower_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::AlphabeticLower)


def test_cobol::operators::alphabeticlower_constructor_exists():
    assert callable(cobol::operators::AlphabeticLower.__init__)


def test_cobol::operators::alphabeticlower_constructor_args():
    sig = inspect.signature(cobol::operators::AlphabeticLower.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::alphabeticupper_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::AlphabeticUpper)


def test_cobol::operators::alphabeticupper_constructor_exists():
    assert callable(cobol::operators::AlphabeticUpper.__init__)


def test_cobol::operators::alphabeticupper_constructor_args():
    sig = inspect.signature(cobol::operators::AlphabeticUpper.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::numeric_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Numeric)


def test_cobol::operators::numeric_constructor_exists():
    assert callable(cobol::operators::Numeric.__init__)


def test_cobol::operators::numeric_constructor_args():
    sig = inspect.signature(cobol::operators::Numeric.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::alphabetic_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Alphabetic)


def test_cobol::operators::alphabetic_constructor_exists():
    assert callable(cobol::operators::Alphabetic.__init__)


def test_cobol::operators::alphabetic_constructor_args():
    sig = inspect.signature(cobol::operators::Alphabetic.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::classcondition_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::ClassCondition)


def test_cobol::conditions::classcondition_constructor_exists():
    assert callable(cobol::conditions::ClassCondition.__init__)


def test_cobol::conditions::classcondition_constructor_args():
    sig = inspect.signature(cobol::conditions::ClassCondition.__init__)
    params = list(sig.parameters.keys())



def test_signoperator_is_not_abstract():
    assert not inspect.isabstract(SignOperator)


def test_signoperator_constructor_exists():
    assert callable(SignOperator.__init__)


def test_signoperator_constructor_args():
    sig = inspect.signature(SignOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::negative_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Negative)


def test_cobol::operators::negative_constructor_exists():
    assert callable(cobol::operators::Negative.__init__)


def test_cobol::operators::negative_constructor_args():
    sig = inspect.signature(cobol::operators::Negative.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::zero_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Zero)


def test_cobol::operators::zero_constructor_exists():
    assert callable(cobol::operators::Zero.__init__)


def test_cobol::operators::zero_constructor_args():
    sig = inspect.signature(cobol::operators::Zero.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::positive_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Positive)


def test_cobol::operators::positive_constructor_exists():
    assert callable(cobol::operators::Positive.__init__)


def test_cobol::operators::positive_constructor_args():
    sig = inspect.signature(cobol::operators::Positive.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeOperator)


def test_multiplicativeoperator_constructor_exists():
    assert callable(MultiplicativeOperator.__init__)


def test_multiplicativeoperator_constructor_args():
    sig = inspect.signature(MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::multiplication_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Multiplication)


def test_cobol::operators::multiplication_constructor_exists():
    assert callable(cobol::operators::Multiplication.__init__)


def test_cobol::operators::multiplication_constructor_args():
    sig = inspect.signature(cobol::operators::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_cobol::operators::division_is_not_abstract():
    assert not inspect.isabstract(cobol::operators::Division)


def test_cobol::operators::division_constructor_exists():
    assert callable(cobol::operators::Division.__init__)


def test_cobol::operators::division_constructor_args():
    sig = inspect.signature(cobol::operators::Division.__init__)
    params = list(sig.parameters.keys())



def test_multiplicativearithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeArithmeticExpressionChild)


def test_multiplicativearithmeticexpressionchild_constructor_exists():
    assert callable(MultiplicativeArithmeticExpressionChild.__init__)


def test_multiplicativearithmeticexpressionchild_constructor_args():
    sig = inspect.signature(MultiplicativeArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::powerarithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::PowerArithmeticExpressionChild)


def test_cobol::arithmetics::powerarithmeticexpressionchild_constructor_exists():
    assert callable(cobol::arithmetics::PowerArithmeticExpressionChild.__init__)


def test_cobol::arithmetics::powerarithmeticexpressionchild_constructor_args():
    sig = inspect.signature(cobol::arithmetics::PowerArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::powerarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::PowerArithmeticExpression)


def test_cobol::arithmetics::powerarithmeticexpression_constructor_exists():
    assert callable(cobol::arithmetics::PowerArithmeticExpression.__init__)


def test_cobol::arithmetics::powerarithmeticexpression_constructor_args():
    sig = inspect.signature(cobol::arithmetics::PowerArithmeticExpression.__init__)
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



def test_cobol::arithmetics::multiplicativearithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::MultiplicativeArithmeticExpressionChild)


def test_cobol::arithmetics::multiplicativearithmeticexpressionchild_constructor_exists():
    assert callable(cobol::arithmetics::MultiplicativeArithmeticExpressionChild.__init__)


def test_cobol::arithmetics::multiplicativearithmeticexpressionchild_constructor_args():
    sig = inspect.signature(cobol::arithmetics::MultiplicativeArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::multiplicativearithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::MultiplicativeArithmeticExpression)


def test_cobol::arithmetics::multiplicativearithmeticexpression_constructor_exists():
    assert callable(cobol::arithmetics::MultiplicativeArithmeticExpression.__init__)


def test_cobol::arithmetics::multiplicativearithmeticexpression_constructor_args():
    sig = inspect.signature(cobol::arithmetics::MultiplicativeArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_rangeexpressionchild_is_not_abstract():
    assert not inspect.isabstract(RangeExpressionChild)


def test_rangeexpressionchild_constructor_exists():
    assert callable(RangeExpressionChild.__init__)


def test_rangeexpressionchild_constructor_args():
    sig = inspect.signature(RangeExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::additivearithmeticexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::AdditiveArithmeticExpressionChild)


def test_cobol::arithmetics::additivearithmeticexpressionchild_constructor_exists():
    assert callable(cobol::arithmetics::AdditiveArithmeticExpressionChild.__init__)


def test_cobol::arithmetics::additivearithmeticexpressionchild_constructor_args():
    sig = inspect.signature(cobol::arithmetics::AdditiveArithmeticExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::arithmetics::additivearithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::arithmetics::AdditiveArithmeticExpression)


def test_cobol::arithmetics::additivearithmeticexpression_constructor_exists():
    assert callable(cobol::arithmetics::AdditiveArithmeticExpression.__init__)


def test_cobol::arithmetics::additivearithmeticexpression_constructor_args():
    sig = inspect.signature(cobol::arithmetics::AdditiveArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::nestedcondition_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::NestedCondition)


def test_cobol::conditions::nestedcondition_constructor_exists():
    assert callable(cobol::conditions::NestedCondition.__init__)


def test_cobol::conditions::nestedcondition_constructor_args():
    sig = inspect.signature(cobol::conditions::NestedCondition.__init__)
    params = list(sig.parameters.keys())



def test_negatedabbreviatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(NegatedAbbreviatedConditionalExpressionChild)


def test_negatedabbreviatedconditionalexpressionchild_constructor_exists():
    assert callable(NegatedAbbreviatedConditionalExpressionChild.__init__)


def test_negatedabbreviatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(NegatedAbbreviatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::abbreviatedrelationalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::AbbreviatedRelationalExpressionChild)


def test_cobol::conditions::abbreviatedrelationalexpressionchild_constructor_exists():
    assert callable(cobol::conditions::AbbreviatedRelationalExpressionChild.__init__)


def test_cobol::conditions::abbreviatedrelationalexpressionchild_constructor_args():
    sig = inspect.signature(cobol::conditions::AbbreviatedRelationalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::abbreviatedrelationalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::AbbreviatedRelationalExpression)


def test_cobol::conditions::abbreviatedrelationalexpression_constructor_exists():
    assert callable(cobol::conditions::AbbreviatedRelationalExpression.__init__)


def test_cobol::conditions::abbreviatedrelationalexpression_constructor_args():
    sig = inspect.signature(cobol::conditions::AbbreviatedRelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::abbreviatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::AbbreviatedConditionalExpressionChild)


def test_cobol::conditions::abbreviatedconditionalexpressionchild_constructor_exists():
    assert callable(cobol::conditions::AbbreviatedConditionalExpressionChild.__init__)


def test_cobol::conditions::abbreviatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(cobol::conditions::AbbreviatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_abbreviatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AbbreviatedConditionalExpressionChild)


def test_abbreviatedconditionalexpressionchild_constructor_exists():
    assert callable(AbbreviatedConditionalExpressionChild.__init__)


def test_abbreviatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(AbbreviatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::negatedabbreviatedconditionalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::NegatedAbbreviatedConditionalExpressionChild)


def test_cobol::conditions::negatedabbreviatedconditionalexpressionchild_constructor_exists():
    assert callable(cobol::conditions::NegatedAbbreviatedConditionalExpressionChild.__init__)


def test_cobol::conditions::negatedabbreviatedconditionalexpressionchild_constructor_args():
    sig = inspect.signature(cobol::conditions::NegatedAbbreviatedConditionalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::negatedabbreviatedconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::NegatedAbbreviatedConditionalExpression)


def test_cobol::conditions::negatedabbreviatedconditionalexpression_constructor_exists():
    assert callable(cobol::conditions::NegatedAbbreviatedConditionalExpression.__init__)


def test_cobol::conditions::negatedabbreviatedconditionalexpression_constructor_args():
    sig = inspect.signature(cobol::conditions::NegatedAbbreviatedConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::abbreviatedconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::AbbreviatedConditionalExpression)


def test_cobol::conditions::abbreviatedconditionalexpression_constructor_exists():
    assert callable(cobol::conditions::AbbreviatedConditionalExpression.__init__)


def test_cobol::conditions::abbreviatedconditionalexpression_constructor_args():
    sig = inspect.signature(cobol::conditions::AbbreviatedConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::ConditionalAndExpression)


def test_cobol::conditions::conditionalandexpression_constructor_exists():
    assert callable(cobol::conditions::ConditionalAndExpression.__init__)


def test_cobol::conditions::conditionalandexpression_constructor_args():
    sig = inspect.signature(cobol::conditions::ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::conditionalandexpressionchild_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::ConditionalAndExpressionChild)


def test_cobol::conditions::conditionalandexpressionchild_constructor_exists():
    assert callable(cobol::conditions::ConditionalAndExpressionChild.__init__)


def test_cobol::conditions::conditionalandexpressionchild_constructor_args():
    sig = inspect.signature(cobol::conditions::ConditionalAndExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::expressionlist_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::ExpressionList)


def test_cobol::conditions::expressionlist_constructor_exists():
    assert callable(cobol::conditions::ExpressionList.__init__)


def test_cobol::conditions::expressionlist_constructor_args():
    sig = inspect.signature(cobol::conditions::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::signcondition_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::SignCondition)


def test_cobol::conditions::signcondition_constructor_exists():
    assert callable(cobol::conditions::SignCondition.__init__)


def test_cobol::conditions::signcondition_constructor_args():
    sig = inspect.signature(cobol::conditions::SignCondition.__init__)
    params = list(sig.parameters.keys())



def test_abbreviatedrelationalexpressionchild_is_not_abstract():
    assert not inspect.isabstract(AbbreviatedRelationalExpressionChild)


def test_abbreviatedrelationalexpressionchild_constructor_exists():
    assert callable(AbbreviatedRelationalExpressionChild.__init__)


def test_abbreviatedrelationalexpressionchild_constructor_args():
    sig = inspect.signature(AbbreviatedRelationalExpressionChild.__init__)
    params = list(sig.parameters.keys())



def test_cobol::conditions::nestedabbreviatedconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(cobol::conditions::NestedAbbreviatedConditionalExpression)


def test_cobol::conditions::nestedabbreviatedconditionalexpression_constructor_exists():
    assert callable(cobol::conditions::NestedAbbreviatedConditionalExpression.__init__)


def test_cobol::conditions::nestedabbreviatedconditionalexpression_constructor_args():
    sig = inspect.signature(cobol::conditions::NestedAbbreviatedConditionalExpression.__init__)
    params = list(sig.parameters.keys())

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

def test_systempunchdevices_exists():
    # Check that the Enumeration exists
    assert SystemPunchDevices is not None

def test_systempunchdevices_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemPunchDevices]
    expected_literals = [
        "syspch",
        "syspunch",
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
        "quotes",
        "quote",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Quotes"

def test_spaces_exists():
    # Check that the Enumeration exists
    assert Spaces is not None

def test_spaces_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Spaces]
    expected_literals = [
        "space",
        "spaces",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Spaces"

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

def test_invokestatementtokens_exists():
    # Check that the Enumeration exists
    assert InvokeStatementTokens is not None

def test_invokestatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InvokeStatementTokens]
    expected_literals = [
        "using",
        "super",
        "new",
        "by",
        "returning",
        "self",
        "value",
        "length",
        "of",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InvokeStatementTokens"

def test_encodingtypes_exists():
    # Check that the Enumeration exists
    assert EncodingTypes is not None

def test_encodingtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EncodingTypes]
    expected_literals = [
        "nationalEdited",
        "egcs",
        "alphabetic",
        "alphanumericEdited",
        "alphanumeric",
        "dbcs",
        "national",
        "numeric",
        "numericEdited",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EncodingTypes"

def test_selectstatementclauses_exists():
    # Check that the Enumeration exists
    assert SelectStatementClauses is not None

def test_selectstatementclauses_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectStatementClauses]
    expected_literals = [
        "indexed",
        "sequential",
        "random",
        "mode",
        "with_",
        "areas",
        "relative",
        "area",
        "padding",
        "organization",
        "record",
        "delimiter",
        "alternate",
        "reserve",
        "key",
        "standard1",
        "duplicates",
        "access",
        "is_",
        "character",
        "dynamic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectStatementClauses"

def test_usestatementtokens_exists():
    # Check that the Enumeration exists
    assert UseStatementTokens is not None

def test_usestatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UseStatementTokens]
    expected_literals = [
        "all",
        "after",
        "reel",
        "error",
        "standard",
        "ending",
        "io",
        "extend",
        "for_",
        "debugging",
        "beginning",
        "input",
        "on",
        "unit",
        "label",
        "output",
        "global_",
        "file",
        "procedure",
        "procedures",
        "exception",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UseStatementTokens"

def test_specialnamesclauses_exists():
    # Check that the Enumeration exists
    assert SpecialNamesClauses is not None

def test_specialnamesclauses_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpecialNamesClauses]
    expected_literals = [
        "comma",
        "is_",
        "xmlSchema",
        "decimalPoint",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpecialNamesClauses"

def test_adjustings_exists():
    # Check that the Enumeration exists
    assert Adjustings is not None

def test_adjustings_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Adjustings]
    expected_literals = [
        "down",
        "up",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Adjustings"

def test_predefinedalphabettypes_exists():
    # Check that the Enumeration exists
    assert PredefinedAlphabetTypes is not None

def test_predefinedalphabettypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PredefinedAlphabetTypes]
    expected_literals = [
        "native",
        "ebcdic",
        "standard2",
        "standard1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PredefinedAlphabetTypes"

def test_objectcomputerdescriptioninfo_exists():
    # Check that the Enumeration exists
    assert ObjectComputerDescriptionInfo is not None

def test_objectcomputerdescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectComputerDescriptionInfo]
    expected_literals = [
        "modules",
        "program",
        "segmentLimit",
        "memory",
        "words",
        "collating",
        "characters",
        "size",
        "segment",
        "sequence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectComputerDescriptionInfo"

def test_selects_exists():
    # Check that the Enumeration exists
    assert Selects is not None

def test_selects_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Selects]
    expected_literals = [
        "s3",
        "s4",
        "s1",
        "s2",
        "s5",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Selects"

def test_iocontroldescriptioninfo_exists():
    # Check that the Enumeration exists
    assert IOControlDescriptionInfo is not None

def test_iocontroldescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IOControlDescriptionInfo]
    expected_literals = [
        "unit",
        "area",
        "contains",
        "file",
        "for_",
        "apply",
        "record",
        "tape",
        "rerun",
        "of",
        "sortMerge",
        "position",
        "every",
        "on",
        "records",
        "multiple",
        "same",
        "writeOnly",
        "sort",
        "reel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IOControlDescriptionInfo"

def test_channels_exists():
    # Check that the Enumeration exists
    assert Channels is not None

def test_channels_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Channels]
    expected_literals = [
        "c9",
        "c1",
        "c5",
        "c3",
        "c7",
        "c11",
        "c8",
        "c2",
        "c12",
        "c10",
        "c4",
        "c6",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Channels"

def test_filedescriptioninfo_exists():
    # Check that the Enumeration exists
    assert FileDescriptionInfo is not None

def test_filedescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FileDescriptionInfo]
    expected_literals = [
        "to",
        "records",
        "label",
        "report",
        "from_",
        "standard",
        "block",
        "recording",
        "omitted",
        "on",
        "u",
        "value",
        "mode",
        "reports",
        "with_",
        "contains",
        "top",
        "v",
        "data",
        "linage",
        "identification",
        "varying",
        "in_",
        "depending",
        "record",
        "codeSet",
        "is_",
        "bottom",
        "at",
        "characters",
        "footing",
        "id",
        "are",
        "s",
        "lines",
        "size",
        "of",
        "f",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FileDescriptionInfo"

def test_systemoutputs_exists():
    # Check that the Enumeration exists
    assert SystemOutputs is not None

def test_systemoutputs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemOutputs]
    expected_literals = [
        "syslst",
        "syslist",
        "sysout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemOutputs"

def test_throughphrase_exists():
    # Check that the Enumeration exists
    assert ThroughPhrase is not None

def test_throughphrase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ThroughPhrase]
    expected_literals = [
        "thru",
        "through",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ThroughPhrase"

def test_upsiswitches_exists():
    # Check that the Enumeration exists
    assert UPSISwitches is not None

def test_upsiswitches_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UPSISwitches]
    expected_literals = [
        "upsi5",
        "upsi1",
        "upsi0",
        "upsi7",
        "upsi4",
        "upsi2",
        "upsi6",
        "upsi3",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UPSISwitches"

def test_datadescriptioninfo_exists():
    # Check that the Enumeration exists
    assert DataDescriptionInfo is not None

def test_datadescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataDescriptionInfo]
    expected_literals = [
        "leading",
        "just",
        "justified",
        "zeros",
        "synchronized",
        "sign",
        "right",
        "sync",
        "zero",
        "when",
        "is_",
        "character",
        "blank",
        "zeroes",
        "trailing",
        "left",
        "separate",
        "date",
        "format",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataDescriptionInfo"

def test_programdescriptioninfo_exists():
    # Check that the Enumeration exists
    assert ProgramDescriptionInfo is not None

def test_programdescriptioninfo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgramDescriptionInfo]
    expected_literals = [
        "author",
        "dateCompleted",
        "dateWritten",
        "security",
        "installation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgramDescriptionInfo"

def test_picturestringcharacters_exists():
    # Check that the Enumeration exists
    assert PictureStringCharacters is not None

def test_picturestringcharacters_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PictureStringCharacters]
    expected_literals = [
        "exponent",
        "decimalPoint",
        "comma",
        "slash",
        "leadingZero",
        "blank",
        "alphabetic",
        "assumedDecimalPoint",
        "asterik",
        "escape",
        "negative",
        "debit",
        "sign",
        "numeric",
        "zero",
        "period",
        "dollar",
        "any",
        "national",
        "plus",
        "credit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PictureStringCharacters"

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

def test_zeroes_exists():
    # Check that the Enumeration exists
    assert Zeroes is not None

def test_zeroes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Zeroes]
    expected_literals = [
        "zeros",
        "zeroes",
        "zero",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Zeroes"

def test_openstatementtokens_exists():
    # Check that the Enumeration exists
    assert OpenStatementTokens is not None

def test_openstatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OpenStatementTokens]
    expected_literals = [
        "no",
        "rewind",
        "with_",
        "reversed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OpenStatementTokens"

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

def test_highvalues_exists():
    # Check that the Enumeration exists
    assert HighValues is not None

def test_highvalues_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HighValues]
    expected_literals = [
        "highValues",
        "highValue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HighValues"

def test_exitlabels_exists():
    # Check that the Enumeration exists
    assert ExitLabels is not None

def test_exitlabels_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExitLabels]
    expected_literals = [
        "program",
        "paragraph",
        "method",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExitLabels"

def test_positions_exists():
    # Check that the Enumeration exists
    assert Positions is not None

def test_positions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Positions]
    expected_literals = [
        "before",
        "after",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Positions"

def test_status_exists():
    # Check that the Enumeration exists
    assert Status is not None

def test_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Status]
    expected_literals = [
        "on",
        "off",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Status"

def test_systeminputs_exists():
    # Check that the Enumeration exists
    assert SystemInputs is not None

def test_systeminputs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemInputs]
    expected_literals = [
        "sysin",
        "sysipt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemInputs"

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

def test_sqlstatementtokens_exists():
    # Check that the Enumeration exists
    assert SQLStatementTokens is not None

def test_sqlstatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SQLStatementTokens]
    expected_literals = [
        "declare",
        "from_",
        "select",
        "delete",
        "include",
        "insert",
        "into",
        "update",
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
        "computational3",
        "display1",
        "index",
        "display",
        "comp",
        "procedurePointer",
        "national",
        "computational1",
        "packedDecimal",
        "comp2",
        "comp5",
        "functionPointer",
        "pointer",
        "binary",
        "comp1",
        "comp4",
        "comp3",
        "computational",
        "computational5",
        "computational2",
        "computational4",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Usages"

def test_iotypes_exists():
    # Check that the Enumeration exists
    assert IOTypes is not None

def test_iotypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IOTypes]
    expected_literals = [
        "input",
        "output",
        "extend",
        "io",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IOTypes"

def test_corresponding_exists():
    # Check that the Enumeration exists
    assert Corresponding is not None

def test_corresponding_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Corresponding]
    expected_literals = [
        "corresponding",
        "corr",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Corresponding"

def test_acceptstatementtokens_exists():
    # Check that the Enumeration exists
    assert AcceptStatementTokens is not None

def test_acceptstatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AcceptStatementTokens]
    expected_literals = [
        "time",
        "day",
        "dateformat1",
        "dateformat2",
        "dow",
        "from_",
        "date",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AcceptStatementTokens"

def test_eop_exists():
    # Check that the Enumeration exists
    assert EOP is not None

def test_eop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EOP]
    expected_literals = [
        "eop",
        "endOfPage",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EOP"

def test_cicsstatementtokens_exists():
    # Check that the Enumeration exists
    assert CICSStatementTokens is not None

def test_cicsstatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CICSStatementTokens]
    expected_literals = [
        "load",
        "qname",
        "closepar",
        "into",
        "massinsert",
        "rba",
        "dataset",
        "synconreturn",
        "keylength",
        "rewrite",
        "queue",
        "xrba",
        "update",
        "ridfld",
        "equal",
        "xctl",
        "commarea",
        "write",
        "from_",
        "item",
        "sysid",
        "start",
        "length",
        "main",
        "gteq",
        "ts",
        "datalength",
        "channel",
        "td",
        "file",
        "next",
        "sys",
        "set",
        "transid",
        "rrn",
        "inputmsglen",
        "uncommitted",
        "repeatable",
        "read",
        "writeq",
        "deleteq",
        "generic",
        "consistent",
        "openpar",
        "numitems",
        "program",
        "inputmsg",
        "tr",
        "nosuspend",
        "auxiliary",
        "token",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CICSStatementTokens"

def test_sortphrasetokens_exists():
    # Check that the Enumeration exists
    assert SortPhraseTokens is not None

def test_sortphrasetokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortPhraseTokens]
    expected_literals = [
        "sequence",
        "in_",
        "is_",
        "collating",
        "with_",
        "duplicates",
        "order",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SortPhraseTokens"

def test_orders_exists():
    # Check that the Enumeration exists
    assert Orders is not None

def test_orders_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orders]
    expected_literals = [
        "dsc",
        "asc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orders"

def test_sortingorder_exists():
    # Check that the Enumeration exists
    assert SortingOrder is not None

def test_sortingorder_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortingOrder]
    expected_literals = [
        "dsc",
        "asc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SortingOrder"

def test_nulls_exists():
    # Check that the Enumeration exists
    assert Nulls is not None

def test_nulls_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Nulls]
    expected_literals = [
        "nulls",
        "null",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Nulls"

def test_closestatementtokens_exists():
    # Check that the Enumeration exists
    assert CloseStatementTokens is not None

def test_closestatementtokens_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CloseStatementTokens]
    expected_literals = [
        "rewind",
        "reel",
        "removal",
        "no",
        "lock",
        "unit",
        "for_",
        "with_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CloseStatementTokens"


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
strings::Occurrence_strategy = st.builds(
    strings::Occurrence,
)
strings::Tallying_strategy = st.builds(
    strings::Tallying,
)
cobol::strings::TallyingOccurrence_strategy = st.builds(
    cobol::strings::TallyingOccurrence,
)
cobol::strings::Occurrence_strategy = st.builds(
    cobol::strings::Occurrence,
    type=
        safe_text
)
cobol::strings::Location_strategy = st.builds(
    cobol::strings::Location,
    initial=
        st.booleans(),
    position=
        safe_text
)
ManipulatedStrings_strategy = st.builds(
    ManipulatedStrings,
)
cobol::strings::SplittedString_strategy = st.builds(
    cobol::strings::SplittedString,
)
cobol::strings::ConcatenatingStrings_strategy = st.builds(
    cobol::strings::ConcatenatingStrings,
)
cobol::strings::String_strategy = st.builds(
    cobol::strings::String,
)
Location_strategy = st.builds(
    Location,
)
String_strategy = st.builds(
    String,
)
cobol::strings::ManipulatedStrings_strategy = st.builds(
    cobol::strings::ManipulatedStrings,
)
cobol::strings::StringManipulation_strategy = st.builds(
    cobol::strings::StringManipulation,
)
StringManipulation_strategy = st.builds(
    StringManipulation,
)
cobol::strings::Replacement_strategy = st.builds(
    cobol::strings::Replacement,
)
cobol::strings::Tallying_strategy = st.builds(
    cobol::strings::Tallying,
)
strings::Replacement_strategy = st.builds(
    strings::Replacement,
)
cobol::strings::ReplacementOccurrence_strategy = st.builds(
    cobol::strings::ReplacementOccurrence,
)
NotErrorHandler_strategy = st.builds(
    NotErrorHandler,
)
cobol::handlers::NotOnOverflow_strategy = st.builds(
    cobol::handlers::NotOnOverflow,
)
cobol::handlers::NotAtEnd_strategy = st.builds(
    cobol::handlers::NotAtEnd,
)
cobol::handlers::NotInvalidKey_strategy = st.builds(
    cobol::handlers::NotInvalidKey,
)
cobol::handlers::NotOnException_strategy = st.builds(
    cobol::handlers::NotOnException,
)
cobol::handlers::NotOnSizeError_strategy = st.builds(
    cobol::handlers::NotOnSizeError,
)
cobol::functions::Argumentable_strategy = st.builds(
    cobol::functions::Argumentable,
)
Argument_strategy = st.builds(
    Argument,
)
cobol::functions::OmittedArgument_strategy = st.builds(
    cobol::functions::OmittedArgument,
)
cobol::functions::ByContentArgument_strategy = st.builds(
    cobol::functions::ByContentArgument,
)
cobol::functions::ByValueArgument_strategy = st.builds(
    cobol::functions::ByValueArgument,
)
cobol::functions::ByReferenceArgument_strategy = st.builds(
    cobol::functions::ByReferenceArgument,
)
cobol::functions::Argument_strategy = st.builds(
    cobol::functions::Argument,
)
cobol::labels::Label_strategy = st.builds(
    cobol::labels::Label,
)
cobol::labels::Procedure_strategy = st.builds(
    cobol::labels::Procedure,
)
Procedure_strategy = st.builds(
    Procedure,
)
cobol::handlers::NotAtEndOfPage_strategy = st.builds(
    cobol::handlers::NotAtEndOfPage,
)
ProcedureRangeChild_strategy = st.builds(
    ProcedureRangeChild,
)
cobol::verbs::Verb_strategy = st.builds(
    cobol::verbs::Verb,
)
Verb_strategy = st.builds(
    Verb,
)
cobol::verbs::Is_strategy = st.builds(
    cobol::verbs::Is,
)
DeclarativeSection_strategy = st.builds(
    DeclarativeSection,
)
cobol::declaratives::Declaratives_strategy = st.builds(
    cobol::declaratives::Declaratives,
)
cobol::labels::ProcedureLabel_strategy = st.builds(
    cobol::labels::ProcedureLabel,
)
cobol::files::FileStatus_strategy = st.builds(
    cobol::files::FileStatus,
)
FileStatus_strategy = st.builds(
    FileStatus,
)
cobol::tables::TableDimension_strategy = st.builds(
    cobol::tables::TableDimension,
    value=
        st.integers()
)
AdditionalIndexName_strategy = st.builds(
    AdditionalIndexName,
)
Parameter_strategy = st.builds(
    Parameter,
)
cobol::parameters::ByReferenceParameter_strategy = st.builds(
    cobol::parameters::ByReferenceParameter,
)
cobol::parameters::ByValueParameter_strategy = st.builds(
    cobol::parameters::ByValueParameter,
)
cobol::parameters::Parametrizable_strategy = st.builds(
    cobol::parameters::Parametrizable,
)
IndexName_strategy = st.builds(
    IndexName,
)
TableDimension_strategy = st.builds(
    TableDimension,
)
dataitems::DataItem_strategy = st.builds(
    dataitems::DataItem,
)
cobol::specialnames::SpecialNameStatement_strategy = st.builds(
    cobol::specialnames::SpecialNameStatement,
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
cobol::specialnames::SymbolicCharacter_strategy = st.builds(
    cobol::specialnames::SymbolicCharacter,
)
cobol::specialnames::MnemonicName_strategy = st.builds(
    cobol::specialnames::MnemonicName,
)
cobol::tables::KeyName_strategy = st.builds(
    cobol::tables::KeyName,
    keyOrder=
        safe_text
)
KeyName_strategy = st.builds(
    KeyName,
)
cobol::specialnames::AlphabetType_strategy = st.builds(
    cobol::specialnames::AlphabetType,
)
specialnames::MnemonicName_strategy = st.builds(
    specialnames::MnemonicName,
)
AlphabetType_strategy = st.builds(
    AlphabetType,
)
cobol::specialnames::CodeNameAlphabetType_strategy = st.builds(
    cobol::specialnames::CodeNameAlphabetType,
    value=
        safe_text
)
cobol::specialnames::PredefinedAlphabetType_strategy = st.builds(
    cobol::specialnames::PredefinedAlphabetType,
    value=
        safe_text
)
specialnames::SpecialNameStatement_strategy = st.builds(
    specialnames::SpecialNameStatement,
)
cobol::specialnames::UPSISwitchIs_strategy = st.builds(
    cobol::specialnames::UPSISwitchIs,
)
cobol::specialnames::SystemDeviceIs_strategy = st.builds(
    cobol::specialnames::SystemDeviceIs,
)
ConditionName_strategy = st.builds(
    ConditionName,
)
cobol::specialnames::OffStatus_strategy = st.builds(
    cobol::specialnames::OffStatus,
)
cobol::specialnames::OnStatus_strategy = st.builds(
    cobol::specialnames::OnStatus,
)
specialnames::SpecialName_strategy = st.builds(
    specialnames::SpecialName,
)
cobol::specialnames::CurrencySign_strategy = st.builds(
    cobol::specialnames::CurrencySign,
    pictureSymbol=
        safe_text
)
cobol::specialnames::ClassName_strategy = st.builds(
    cobol::specialnames::ClassName,
)
cobol::specialnames::AlphabetName_strategy = st.builds(
    cobol::specialnames::AlphabetName,
)
cobol::specialnames::ExplicitAlphabetType_strategy = st.builds(
    cobol::specialnames::ExplicitAlphabetType,
)
references::ReferenceableElement_strategy = st.builds(
    references::ReferenceableElement,
)
cobol::dataitems::DataItemAttribute_strategy = st.builds(
    cobol::dataitems::DataItemAttribute,
)
RangeExpression_strategy = st.builds(
    RangeExpression,
)
DataName_strategy = st.builds(
    DataName,
)
cobol::dataitems::RenamingDataName_strategy = st.builds(
    cobol::dataitems::RenamingDataName,
)
DataItemAttribute_strategy = st.builds(
    DataItemAttribute,
)
cobol::dataitems::Redefines_strategy = st.builds(
    cobol::dataitems::Redefines,
)
cobol::dataitems::Usage_strategy = st.builds(
    cobol::dataitems::Usage,
    usage=
        safe_text,
    isNative=
        st.booleans()
)
cobol::dataitems::Value_strategy = st.builds(
    cobol::dataitems::Value,
)
cobol::dataitems::External_strategy = st.builds(
    cobol::dataitems::External,
)
cobol::dataitems::GroupUsage_strategy = st.builds(
    cobol::dataitems::GroupUsage,
)
cobol::dataitems::Global_strategy = st.builds(
    cobol::dataitems::Global,
)
cobol::dataitems::PictureString_strategy = st.builds(
    cobol::dataitems::PictureString,
    picture=
        safe_text
)
SystemDevice_strategy = st.builds(
    SystemDevice,
)
cobol::environments::AdvancedFunctionPrinting_strategy = st.builds(
    cobol::environments::AdvancedFunctionPrinting,
)
cobol::environments::Pocket_strategy = st.builds(
    cobol::environments::Pocket,
    value=
        safe_text
)
cobol::environments::SuppressSpacing_strategy = st.builds(
    cobol::environments::SuppressSpacing,
)
cobol::environments::SystemLogicalOutput_strategy = st.builds(
    cobol::environments::SystemLogicalOutput,
    value=
        safe_text
)
cobol::environments::SystemPunchDevice_strategy = st.builds(
    cobol::environments::SystemPunchDevice,
    value=
        safe_text
)
cobol::environments::Console_strategy = st.builds(
    cobol::environments::Console,
)
cobol::environments::Channel_strategy = st.builds(
    cobol::environments::Channel,
    value=
        safe_text
)
cobol::environments::SystemLogicalInput_strategy = st.builds(
    cobol::environments::SystemLogicalInput,
    value=
        safe_text
)
Register_strategy = st.builds(
    Register,
)
cobol::registers::AddressOf_strategy = st.builds(
    cobol::registers::AddressOf,
)
cobol::registers::WhenCompiled_strategy = st.builds(
    cobol::registers::WhenCompiled,
)
cobol::registers::ShiftOut_strategy = st.builds(
    cobol::registers::ShiftOut,
)
cobol::registers::ReturnCode_strategy = st.builds(
    cobol::registers::ReturnCode,
)
cobol::registers::LengthOf_strategy = st.builds(
    cobol::registers::LengthOf,
)
cobol::registers::ShiftIn_strategy = st.builds(
    cobol::registers::ShiftIn,
)
SortPhraseWater_strategy = st.builds(
    SortPhraseWater,
)
cobol::water::SortPhraseToken_strategy = st.builds(
    cobol::water::SortPhraseToken,
    value=
        safe_text
)
OpenStatementWater_strategy = st.builds(
    OpenStatementWater,
)
cobol::water::OpenStatementToken_strategy = st.builds(
    cobol::water::OpenStatementToken,
    value=
        safe_text
)
InvokeStatementWater_strategy = st.builds(
    InvokeStatementWater,
)
cobol::water::InvokeStatementToken_strategy = st.builds(
    cobol::water::InvokeStatementToken,
    value=
        safe_text
)
CloseStatementWater_strategy = st.builds(
    CloseStatementWater,
)
cobol::water::CloseStatementToken_strategy = st.builds(
    cobol::water::CloseStatementToken,
    value=
        safe_text
)
UseStatementWater_strategy = st.builds(
    UseStatementWater,
)
cobol::water::UseStatementToken_strategy = st.builds(
    cobol::water::UseStatementToken,
    value=
        safe_text
)
AcceptStatementWater_strategy = st.builds(
    AcceptStatementWater,
)
cobol::environments::Environment_strategy = st.builds(
    cobol::environments::Environment,
)
cobol::water::AcceptStatementToken_strategy = st.builds(
    cobol::water::AcceptStatementToken,
    value=
        safe_text
)
CICSStatementWater_strategy = st.builds(
    CICSStatementWater,
)
cobol::water::CICSStatementToken_strategy = st.builds(
    cobol::water::CICSStatementToken,
    value=
        safe_text
)
SQLStatementWater_strategy = st.builds(
    SQLStatementWater,
)
cobol::water::SQLStatementToken_strategy = st.builds(
    cobol::water::SQLStatementToken,
    value=
        safe_text
)
RepositoryParagraphWater_strategy = st.builds(
    RepositoryParagraphWater,
)
cobol::water::RepositoryDescription_strategy = st.builds(
    cobol::water::RepositoryDescription,
    value=
        safe_text
)
IOControlParagraphWater_strategy = st.builds(
    IOControlParagraphWater,
)
cobol::water::IOControlDescription_strategy = st.builds(
    cobol::water::IOControlDescription,
    value=
        safe_text
)
DataDescriptorWater_strategy = st.builds(
    DataDescriptorWater,
)
cobol::water::DataDescription_strategy = st.builds(
    cobol::water::DataDescription,
    value=
        safe_text
)
FileDescriptorWater_strategy = st.builds(
    FileDescriptorWater,
)
cobol::water::FileDescription_strategy = st.builds(
    cobol::water::FileDescription,
    value=
        safe_text
)
SelectStatementWater_strategy = st.builds(
    SelectStatementWater,
)
cobol::water::SelectStatementClause_strategy = st.builds(
    cobol::water::SelectStatementClause,
    value=
        safe_text
)
ObjectComputerParagraphWater_strategy = st.builds(
    ObjectComputerParagraphWater,
)
cobol::water::PriorityNumber_strategy = st.builds(
    cobol::water::PriorityNumber,
    value=
        safe_text
)
cobol::water::ObjectComputerDescription_strategy = st.builds(
    cobol::water::ObjectComputerDescription,
    value=
        safe_text
)
cobol::water::Water_strategy = st.builds(
    cobol::water::Water,
)
Water_strategy = st.builds(
    Water,
)
cobol::water::SpecialNamesParagraphWater_strategy = st.builds(
    cobol::water::SpecialNamesParagraphWater,
)
cobol::water::SelectStatementWater_strategy = st.builds(
    cobol::water::SelectStatementWater,
)
cobol::water::FileDescriptorWater_strategy = st.builds(
    cobol::water::FileDescriptorWater,
)
cobol::water::CICSStatementWater_strategy = st.builds(
    cobol::water::CICSStatementWater,
)
cobol::water::RepositoryParagraphWater_strategy = st.builds(
    cobol::water::RepositoryParagraphWater,
)
cobol::water::InvokeStatementWater_strategy = st.builds(
    cobol::water::InvokeStatementWater,
)
cobol::water::ObjectComputerParagraphWater_strategy = st.builds(
    cobol::water::ObjectComputerParagraphWater,
)
cobol::water::DataDescriptorWater_strategy = st.builds(
    cobol::water::DataDescriptorWater,
)
cobol::water::CloseStatementWater_strategy = st.builds(
    cobol::water::CloseStatementWater,
)
cobol::water::OpenStatementWater_strategy = st.builds(
    cobol::water::OpenStatementWater,
)
cobol::water::AcceptStatementWater_strategy = st.builds(
    cobol::water::AcceptStatementWater,
)
cobol::water::SQLStatementWater_strategy = st.builds(
    cobol::water::SQLStatementWater,
)
cobol::water::IdentificationDivisionWater_strategy = st.builds(
    cobol::water::IdentificationDivisionWater,
)
cobol::water::SortPhraseWater_strategy = st.builds(
    cobol::water::SortPhraseWater,
)
cobol::water::UseStatementWater_strategy = st.builds(
    cobol::water::UseStatementWater,
)
cobol::water::IOControlParagraphWater_strategy = st.builds(
    cobol::water::IOControlParagraphWater,
)
cobol::water::IncompleteElement_strategy = st.builds(
    cobol::water::IncompleteElement,
)
Label_strategy = st.builds(
    Label,
)
cobol::labels::ProcedureRangeLabel_strategy = st.builds(
    cobol::labels::ProcedureRangeLabel,
)
cobol::labels::StopLabel_strategy = st.builds(
    cobol::labels::StopLabel,
)
cobol::ios::IODirectives_strategy = st.builds(
    cobol::ios::IODirectives,
)
ios::OutputDirective_strategy = st.builds(
    ios::OutputDirective,
)
ios::FileDirective_strategy = st.builds(
    ios::FileDirective,
)
cobol::ios::OutputFile_strategy = st.builds(
    cobol::ios::OutputFile,
)
IODirectives_strategy = st.builds(
    IODirectives,
)
cobol::ios::ProcedureDirective_strategy = st.builds(
    cobol::ios::ProcedureDirective,
)
cobol::ios::FileDirective_strategy = st.builds(
    cobol::ios::FileDirective,
)
cobol::ios::OutputDirective_strategy = st.builds(
    cobol::ios::OutputDirective,
)
cobol::ios::InputDirective_strategy = st.builds(
    cobol::ios::InputDirective,
)
ios::ProcedureDirective_strategy = st.builds(
    ios::ProcedureDirective,
)
cobol::ios::OutputProcedure_strategy = st.builds(
    cobol::ios::OutputProcedure,
)
ios::InputDirective_strategy = st.builds(
    ios::InputDirective,
)
cobol::ios::InputFile_strategy = st.builds(
    cobol::ios::InputFile,
)
cobol::ios::InputProcedure_strategy = st.builds(
    cobol::ios::InputProcedure,
)
cobol::identifiers::ReferenceModifier_strategy = st.builds(
    cobol::identifiers::ReferenceModifier,
)
DirectSubscript_strategy = st.builds(
    DirectSubscript,
)
cobol::identifiers::All_strategy = st.builds(
    cobol::identifiers::All,
)
IdentificationDivisionWater_strategy = st.builds(
    IdentificationDivisionWater,
)
cobol::water::ProgramDescription_strategy = st.builds(
    cobol::water::ProgramDescription,
    value=
        safe_text
)
Subscript_strategy = st.builds(
    Subscript,
)
cobol::identifiers::DirectSubscript_strategy = st.builds(
    cobol::identifiers::DirectSubscript,
)
cobol::identifiers::RelativeSubscript_strategy = st.builds(
    cobol::identifiers::RelativeSubscript,
)
identifiers::Identifier_strategy = st.builds(
    identifiers::Identifier,
)
ReferenceModifier_strategy = st.builds(
    ReferenceModifier,
)
water::SortPhraseWater_strategy = st.builds(
    water::SortPhraseWater,
)
water::DataDescriptorWater_strategy = st.builds(
    water::DataDescriptorWater,
)
water::UseStatementWater_strategy = st.builds(
    water::UseStatementWater,
)
water::SQLStatementWater_strategy = st.builds(
    water::SQLStatementWater,
)
water::IdentificationDivisionWater_strategy = st.builds(
    water::IdentificationDivisionWater,
)
cobol::water::Dot_strategy = st.builds(
    cobol::water::Dot,
)
water::RepositoryParagraphWater_strategy = st.builds(
    water::RepositoryParagraphWater,
)
water::AcceptStatementWater_strategy = st.builds(
    water::AcceptStatementWater,
)
cobol::identifiers::Subscript_strategy = st.builds(
    cobol::identifiers::Subscript,
)
VaryingUntilCondition_strategy = st.builds(
    VaryingUntilCondition,
)
cobol::statements::AfterUntilCondition_strategy = st.builds(
    cobol::statements::AfterUntilCondition,
)
Qualifier_strategy = st.builds(
    Qualifier,
)
Conditional_strategy = st.builds(
    Conditional,
)
cobol::statements::VaryingUntilCondition_strategy = st.builds(
    cobol::statements::VaryingUntilCondition,
)
Tallying_strategy = st.builds(
    Tallying,
)
cobol::strings::AnyCharacter_strategy = st.builds(
    cobol::strings::AnyCharacter,
)
cobol::strings::SpecificCharacter_strategy = st.builds(
    cobol::strings::SpecificCharacter,
)
cobol::statements::TallyingIn_strategy = st.builds(
    cobol::statements::TallyingIn,
)
cobol::statements::Statement_strategy = st.builds(
    cobol::statements::Statement,
    endVerb=
        st.booleans()
)
cobol::operands::Operand_strategy = st.builds(
    cobol::operands::Operand,
)
ReplacementOperand_strategy = st.builds(
    ReplacementOperand,
)
cobol::operands::Encoding_strategy = st.builds(
    cobol::operands::Encoding,
    type=
        safe_text
)
Operand_strategy = st.builds(
    Operand,
)
cobol::operands::ArithmeticOperand_strategy = st.builds(
    cobol::operands::ArithmeticOperand,
)
cobol::operands::ReplacementOperand_strategy = st.builds(
    cobol::operands::ReplacementOperand,
)
Identifier_strategy = st.builds(
    Identifier,
)
statements::NestedStatement_strategy = st.builds(
    statements::NestedStatement,
)
statements::Perform_strategy = st.builds(
    statements::Perform,
)
cobol::statements::PerformNestedStatement_strategy = st.builds(
    cobol::statements::PerformNestedStatement,
)
ArithmeticStatement_strategy = st.builds(
    ArithmeticStatement,
)
cobol::statements::Multiply_strategy = st.builds(
    cobol::statements::Multiply,
)
cobol::statements::Subtract_strategy = st.builds(
    cobol::statements::Subtract,
)
cobol::statements::Divide_strategy = st.builds(
    cobol::statements::Divide,
)
cobol::statements::Add_strategy = st.builds(
    cobol::statements::Add,
)
statements::ErrorHandled_strategy = st.builds(
    statements::ErrorHandled,
)
statements::Statement_strategy = st.builds(
    statements::Statement,
)
cobol::statements::Delete_strategy = st.builds(
    cobol::statements::Delete,
)
cobol::statements::Start_strategy = st.builds(
    cobol::statements::Start,
)
cobol::statements::ArithmeticStatement_strategy = st.builds(
    cobol::statements::ArithmeticStatement,
    corresponding=
        safe_text
)
DataItem_strategy = st.builds(
    DataItem,
)
cobol::dataitems::ConditionName_strategy = st.builds(
    cobol::dataitems::ConditionName,
)
cobol::dataitems::DataName_strategy = st.builds(
    cobol::dataitems::DataName,
)
cobol::dataitems::RecordName_strategy = st.builds(
    cobol::dataitems::RecordName,
)
Statement_strategy = st.builds(
    Statement,
)
cobol::statements::Perform_strategy = st.builds(
    cobol::statements::Perform,
)
cobol::statements::Exit_strategy = st.builds(
    cobol::statements::Exit,
    exitLabel=
        safe_text
)
EnvironmentDivisionSection_strategy = st.builds(
    EnvironmentDivisionSection,
)
cobol::sections::ConfigurationSection_strategy = st.builds(
    cobol::sections::ConfigurationSection,
)
cobol::sections::IOSection_strategy = st.builds(
    cobol::sections::IOSection,
)
ArithmeticOperand_strategy = st.builds(
    ArithmeticOperand,
)
cobol::operands::RoundedIdentifier_strategy = st.builds(
    cobol::operands::RoundedIdentifier,
)
DataDivisionSection_strategy = st.builds(
    DataDivisionSection,
)
cobol::sections::LinkageStorageSection_strategy = st.builds(
    cobol::sections::LinkageStorageSection,
)
cobol::sections::FileSection_strategy = st.builds(
    cobol::sections::FileSection,
)
cobol::sections::LocalStorageSection_strategy = st.builds(
    cobol::sections::LocalStorageSection,
)
cobol::sections::WorkingStorageSection_strategy = st.builds(
    cobol::sections::WorkingStorageSection,
)
operands::ArithmeticOperand_strategy = st.builds(
    operands::ArithmeticOperand,
)
arithmetics::PrimaryExpression_strategy = st.builds(
    arithmetics::PrimaryExpression,
)
operands::Operand_strategy = st.builds(
    operands::Operand,
)
operands::ReplacementOperand_strategy = st.builds(
    operands::ReplacementOperand,
)
cobol::operands::PrimaryOperand_strategy = st.builds(
    cobol::operands::PrimaryOperand,
)
sentences::StatementContainer_strategy = st.builds(
    sentences::StatementContainer,
)
Sentence_strategy = st.builds(
    Sentence,
)
cobol::sentences::ExitProcedure_strategy = st.builds(
    cobol::sentences::ExitProcedure,
)
cobol::sentences::AlteredGoTo_strategy = st.builds(
    cobol::sentences::AlteredGoTo,
)
cobol::sentences::EntrySentence_strategy = st.builds(
    cobol::sentences::EntrySentence,
)
cobol::sentences::EmptySentence_strategy = st.builds(
    cobol::sentences::EmptySentence,
)
cobol::sentences::StatementContainer_strategy = st.builds(
    cobol::sentences::StatementContainer,
)
FileName_strategy = st.builds(
    FileName,
)
Reference_strategy = st.builds(
    Reference,
)
cobol::references::ElementReference_strategy = st.builds(
    cobol::references::ElementReference,
)
ReferenceableElement_strategy = st.builds(
    ReferenceableElement,
)
cobol::specialnames::SpecialName_strategy = st.builds(
    cobol::specialnames::SpecialName,
)
cobol::parameters::Parameter_strategy = st.builds(
    cobol::parameters::Parameter,
)
cobol::tables::AdditionalIndexName_strategy = st.builds(
    cobol::tables::AdditionalIndexName,
)
cobol::references::Reference_strategy = st.builds(
    cobol::references::Reference,
)
cobol::paragraphs::DebuggingMode_strategy = st.builds(
    cobol::paragraphs::DebuggingMode,
)
SpecialNamesParagraphWater_strategy = st.builds(
    SpecialNamesParagraphWater,
)
cobol::water::SpecialNamesClause_strategy = st.builds(
    cobol::water::SpecialNamesClause,
    value=
        safe_text
)
SpecialNameStatement_strategy = st.builds(
    SpecialNameStatement,
)
IncompleteElement_strategy = st.builds(
    IncompleteElement,
)
cobol::files::SelectStatement_strategy = st.builds(
    cobol::files::SelectStatement,
    isOptional=
        st.booleans(),
    externalFileNames=
        safe_text
)
cobol::statements::IOFile_strategy = st.builds(
    cobol::statements::IOFile,
)
IOFile_strategy = st.builds(
    IOFile,
)
cobol::statements::IOFileDescriptor_strategy = st.builds(
    cobol::statements::IOFileDescriptor,
    type=
        safe_text
)
IOFileDescriptor_strategy = st.builds(
    IOFileDescriptor,
)
cobol::statements::IOStatement_strategy = st.builds(
    cobol::statements::IOStatement,
)
cobol::statements::KeyDescriptor_strategy = st.builds(
    cobol::statements::KeyDescriptor,
    order=
        safe_text
)
statements::VaryingUntilCondition_strategy = st.builds(
    statements::VaryingUntilCondition,
)
cobol::statements::PerformUntilCondition_strategy = st.builds(
    cobol::statements::PerformUntilCondition,
    position=
        safe_text
)
cobol::statements::Release_strategy = st.builds(
    cobol::statements::Release,
)
statements::PerformFixedTimes_strategy = st.builds(
    statements::PerformFixedTimes,
)
statements::FileIOStatement_strategy = st.builds(
    statements::FileIOStatement,
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
statements::PerformProcedure_strategy = st.builds(
    statements::PerformProcedure,
)
cobol::statements::PerformProcedureFixedTimes_strategy = st.builds(
    cobol::statements::PerformProcedureFixedTimes,
)
cobol::statements::FileIOStatement_strategy = st.builds(
    cobol::statements::FileIOStatement,
)
statements::PerformNestedStatement_strategy = st.builds(
    statements::PerformNestedStatement,
)
cobol::statements::PerformNestedStatementFixedTimes_strategy = st.builds(
    cobol::statements::PerformNestedStatementFixedTimes,
)
AfterUntilCondition_strategy = st.builds(
    AfterUntilCondition,
)
statements::PerformUntilCondition_strategy = st.builds(
    statements::PerformUntilCondition,
)
cobol::statements::PerformNestedStatementUntilCondition_strategy = st.builds(
    cobol::statements::PerformNestedStatementUntilCondition,
)
cobol::statements::PerformProcedureUntilCondition_strategy = st.builds(
    cobol::statements::PerformProcedureUntilCondition,
)
cobol::statements::Read_strategy = st.builds(
    cobol::statements::Read,
)
TallyingIn_strategy = st.builds(
    TallyingIn,
)
cobol::statements::SwitchStatus_strategy = st.builds(
    cobol::statements::SwitchStatus,
    status=
        safe_text
)
Write_strategy = st.builds(
    Write,
)
cobol::statements::Rewrite_strategy = st.builds(
    cobol::statements::Rewrite,
)
MnemonicNameReference_strategy = st.builds(
    MnemonicNameReference,
)
IntegerLiteral_strategy = st.builds(
    IntegerLiteral,
)
cobol::statements::Write_strategy = st.builds(
    cobol::statements::Write,
)
cobol::statements::Unstring_strategy = st.builds(
    cobol::statements::Unstring,
)
SearchStatement_strategy = st.builds(
    SearchStatement,
)
cobol::statements::BinarySearch_strategy = st.builds(
    cobol::statements::BinarySearch,
)
cobol::statements::SerialSearch_strategy = st.builds(
    cobol::statements::SerialSearch,
)
NormalEvaluateCase_strategy = st.builds(
    NormalEvaluateCase,
)
cobol::statements::SearchStatement_strategy = st.builds(
    cobol::statements::SearchStatement,
)
Replacement_strategy = st.builds(
    Replacement,
)
cobol::strings::SpecificCharacterBySpecificCharacter_strategy = st.builds(
    cobol::strings::SpecificCharacterBySpecificCharacter,
)
cobol::strings::AnyCharacterBySpecificCharacter_strategy = st.builds(
    cobol::strings::AnyCharacterBySpecificCharacter,
)
cobol::statements::Initialize_strategy = st.builds(
    cobol::statements::Initialize,
)
cobol::statements::Inspect_strategy = st.builds(
    cobol::statements::Inspect,
)
cobol::statements::Replace_strategy = st.builds(
    cobol::statements::Replace,
    replaceSwitch=
        st.booleans()
)
NestedStatement_strategy = st.builds(
    NestedStatement,
)
cobol::handlers::Handler_strategy = st.builds(
    cobol::handlers::Handler,
)
cobol::statements::EvaluateCase_strategy = st.builds(
    cobol::statements::EvaluateCase,
)
ExpressionList_strategy = st.builds(
    ExpressionList,
)
EvaluateCase_strategy = st.builds(
    EvaluateCase,
)
cobol::statements::NormalEvaluateCase_strategy = st.builds(
    cobol::statements::NormalEvaluateCase,
)
cobol::statements::OtherEvaluateCase_strategy = st.builds(
    cobol::statements::OtherEvaluateCase,
)
cobol::statements::Evaluate_strategy = st.builds(
    cobol::statements::Evaluate,
)
SplittedString_strategy = st.builds(
    SplittedString,
)
SetStatement_strategy = st.builds(
    SetStatement,
)
cobol::statements::Set_strategy = st.builds(
    cobol::statements::Set,
)
cobol::statements::SetSwitches_strategy = st.builds(
    cobol::statements::SetSwitches,
)
cobol::statements::SetStatement_strategy = st.builds(
    cobol::statements::SetStatement,
)
FileNameReference_strategy = st.builds(
    FileNameReference,
)
cobol::statements::Return_strategy = st.builds(
    cobol::statements::Return,
)
Handler_strategy = st.builds(
    Handler,
)
cobol::handlers::OnException_strategy = st.builds(
    cobol::handlers::OnException,
)
cobol::handlers::AtEndOfPage_strategy = st.builds(
    cobol::handlers::AtEndOfPage,
    eop=
        safe_text
)
cobol::handlers::NotErrorHandler_strategy = st.builds(
    cobol::handlers::NotErrorHandler,
)
cobol::handlers::InvalidKey_strategy = st.builds(
    cobol::handlers::InvalidKey,
)
cobol::handlers::OnOverflow_strategy = st.builds(
    cobol::handlers::OnOverflow,
)
cobol::handlers::AtEnd_strategy = st.builds(
    cobol::handlers::AtEnd,
)
cobol::handlers::OnSizeError_strategy = st.builds(
    cobol::handlers::OnSizeError,
)
cobol::statements::ErrorHandled_strategy = st.builds(
    cobol::statements::ErrorHandled,
)
cobol::statements::Execute_strategy = st.builds(
    cobol::statements::Execute,
    water=
        safe_text
)
functions::Argumentable_strategy = st.builds(
    functions::Argumentable,
)
cobol::statements::Call_strategy = st.builds(
    cobol::statements::Call,
)
cobol::statements::Cancel_strategy = st.builds(
    cobol::statements::Cancel,
)
statements::IOStatement_strategy = st.builds(
    statements::IOStatement,
)
ConcatenatingStrings_strategy = st.builds(
    ConcatenatingStrings,
)
cobol::statements::String_strategy = st.builds(
    cobol::statements::String,
)
IndexNameReference_strategy = st.builds(
    IndexNameReference,
)
cobol::statements::SetIndexName_strategy = st.builds(
    cobol::statements::SetIndexName,
    adjust=
        safe_text
)
SwitchStatus_strategy = st.builds(
    SwitchStatus,
)
PrimaryOperand_strategy = st.builds(
    PrimaryOperand,
)
cobol::registers::Register_strategy = st.builds(
    cobol::registers::Register,
)
cobol::statements::Move_strategy = st.builds(
    cobol::statements::Move,
    corresponding=
        safe_text
)
cobol::statements::NestedStatement_strategy = st.builds(
    cobol::statements::NestedStatement,
)
Jump_strategy = st.builds(
    Jump,
)
cobol::statements::Continue_strategy = st.builds(
    cobol::statements::Continue,
)
cobol::statements::GoBack_strategy = st.builds(
    cobol::statements::GoBack,
)
cobol::statements::GoTo_strategy = st.builds(
    cobol::statements::GoTo,
)
cobol::statements::NextSentence_strategy = st.builds(
    cobol::statements::NextSentence,
)
cobol::statements::Jump_strategy = st.builds(
    cobol::statements::Jump,
)
ProcedureRangeLabel_strategy = st.builds(
    ProcedureRangeLabel,
)
cobol::labels::ProcedureRange_strategy = st.builds(
    cobol::labels::ProcedureRange,
)
cobol::labels::ProcedureRangeChild_strategy = st.builds(
    cobol::labels::ProcedureRangeChild,
)
Perform_strategy = st.builds(
    Perform,
)
cobol::statements::PerformFixedTimes_strategy = st.builds(
    cobol::statements::PerformFixedTimes,
)
cobol::statements::PerformProcedure_strategy = st.builds(
    cobol::statements::PerformProcedure,
)
AssignmentExpression_strategy = st.builds(
    AssignmentExpression,
)
cobol::statements::Compute_strategy = st.builds(
    cobol::statements::Compute,
)
Environment_strategy = st.builds(
    Environment,
)
cobol::environments::SystemDevice_strategy = st.builds(
    cobol::environments::SystemDevice,
)
cobol::environments::UPSI_strategy = st.builds(
    cobol::environments::UPSI,
    value=
        safe_text
)
cobol::statements::Display_strategy = st.builds(
    cobol::statements::Display,
)
StopLabel_strategy = st.builds(
    StopLabel,
)
cobol::labels::Run_strategy = st.builds(
    cobol::labels::Run,
)
cobol::statements::Stop_strategy = st.builds(
    cobol::statements::Stop,
)
cobol::statements::Conditional_strategy = st.builds(
    cobol::statements::Conditional,
)
statements::Conditional_strategy = st.builds(
    statements::Conditional,
)
cobol::statements::Condition_strategy = st.builds(
    cobol::statements::Condition,
)
NegatedConditionalExpressionChild_strategy = st.builds(
    NegatedConditionalExpressionChild,
)
ConditionalAndExpressionChild_strategy = st.builds(
    ConditionalAndExpressionChild,
)
cobol::conditions::NegatedConditionalExpression_strategy = st.builds(
    cobol::conditions::NegatedConditionalExpression,
)
LogicalOperator_strategy = st.builds(
    LogicalOperator,
)
ConditionalOrExpressionChild_strategy = st.builds(
    ConditionalOrExpressionChild,
)
Condition_strategy = st.builds(
    Condition,
)
cobol::conditions::ConditionalOrExpressionChild_strategy = st.builds(
    cobol::conditions::ConditionalOrExpressionChild,
)
cobol::conditions::ConditionalOrExpression_strategy = st.builds(
    cobol::conditions::ConditionalOrExpression,
)
cobol::conditions::Condition_strategy = st.builds(
    cobol::conditions::Condition,
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
cobol::conditions::RelationalExpression_strategy = st.builds(
    cobol::conditions::RelationalExpression,
)
cobol::conditions::SimpleConditionChild_strategy = st.builds(
    cobol::conditions::SimpleConditionChild,
)
cobol::conditions::NegatedConditionalExpressionChild_strategy = st.builds(
    cobol::conditions::NegatedConditionalExpressionChild,
)
Negate_strategy = st.builds(
    Negate,
)
cobol::commons::Commentable_strategy = st.builds(
    cobol::commons::Commentable,
)
Commentable_strategy = st.builds(
    Commentable,
)
cobol::commons::URIableElement_strategy = st.builds(
    cobol::commons::URIableElement,
    uri=
        safe_text
)
cobol::commons::LabellableElement_strategy = st.builds(
    cobol::commons::LabellableElement,
    label=
        safe_text
)
cobol::commons::NamedElement_strategy = st.builds(
    cobol::commons::NamedElement,
    name=
        safe_text
)
identifiers::IdentifierReference_strategy = st.builds(
    identifiers::IdentifierReference,
)
cobol::references::Qualifiable_strategy = st.builds(
    cobol::references::Qualifiable,
)
cobol::references::ConditionName_strategy = st.builds(
    cobol::references::ConditionName,
)
ElementReference_strategy = st.builds(
    ElementReference,
)
cobol::identifiers::Qualifier_strategy = st.builds(
    cobol::identifiers::Qualifier,
)
cobol::references::AlphabetNameReference_strategy = st.builds(
    cobol::references::AlphabetNameReference,
)
IdentifierReference_strategy = st.builds(
    IdentifierReference,
)
cobol::references::IndexNameReference_strategy = st.builds(
    cobol::references::IndexNameReference,
)
references::IdentifierReferenceQualifier_strategy = st.builds(
    references::IdentifierReferenceQualifier,
)
cobol::references::DataNameReference_strategy = st.builds(
    cobol::references::DataNameReference,
)
references::ConditionName_strategy = st.builds(
    references::ConditionName,
)
cobol::references::ConditionNameReference_strategy = st.builds(
    cobol::references::ConditionNameReference,
)
references::Qualifiable_strategy = st.builds(
    references::Qualifiable,
)
cobol::identifiers::LinageCounter_strategy = st.builds(
    cobol::identifiers::LinageCounter,
)
references::ElementReference_strategy = st.builds(
    references::ElementReference,
)
cobol::identifiers::IdentifierReference_strategy = st.builds(
    cobol::identifiers::IdentifierReference,
)
cobol::references::FileNameReference_strategy = st.builds(
    cobol::references::FileNameReference,
)
cobol::references::MnemonicNameReference_strategy = st.builds(
    cobol::references::MnemonicNameReference,
)
cobol::references::IdentifierReferenceQualifier_strategy = st.builds(
    cobol::references::IdentifierReferenceQualifier,
)
cobol::specialnames::SymbolicCharacterStatement_strategy = st.builds(
    cobol::specialnames::SymbolicCharacterStatement,
)
cobol::references::SpecialNamesConditionNameReference_strategy = st.builds(
    cobol::references::SpecialNamesConditionNameReference,
)
GreaterThan_strategy = st.builds(
    GreaterThan,
)
cobol::operators::GTPhrase_strategy = st.builds(
    cobol::operators::GTPhrase,
)
LessThanOrEqual_strategy = st.builds(
    LessThanOrEqual,
)
cobol::operators::LTEQSign_strategy = st.builds(
    cobol::operators::LTEQSign,
)
cobol::operators::LTEQPhrase_strategy = st.builds(
    cobol::operators::LTEQPhrase,
)
LessThan_strategy = st.builds(
    LessThan,
)
cobol::operators::LTSign_strategy = st.builds(
    cobol::operators::LTSign,
)
cobol::operators::LTPhrase_strategy = st.builds(
    cobol::operators::LTPhrase,
)
paragraphs::IOSectionParagraph_strategy = st.builds(
    paragraphs::IOSectionParagraph,
)
SelectStatement_strategy = st.builds(
    SelectStatement,
)
IOSectionParagraph_strategy = st.builds(
    IOSectionParagraph,
)
cobol::paragraphs::FileControlParagraph_strategy = st.builds(
    cobol::paragraphs::FileControlParagraph,
)
paragraphs::ConfigurationSectionParagraph_strategy = st.builds(
    paragraphs::ConfigurationSectionParagraph,
)
DebuggingMode_strategy = st.builds(
    DebuggingMode,
)
ConfigurationSectionParagraph_strategy = st.builds(
    ConfigurationSectionParagraph,
)
cobol::paragraphs::SpecialNamesParagraph_strategy = st.builds(
    cobol::paragraphs::SpecialNamesParagraph,
)
cobol::paragraphs::SourceComputerParagraph_strategy = st.builds(
    cobol::paragraphs::SourceComputerParagraph,
)
labels::Procedure_strategy = st.builds(
    labels::Procedure,
)
GreaterThanOrEqual_strategy = st.builds(
    GreaterThanOrEqual,
)
cobol::operators::GTEQSign_strategy = st.builds(
    cobol::operators::GTEQSign,
)
cobol::operators::GTEQPhrase_strategy = st.builds(
    cobol::operators::GTEQPhrase,
)
cobol::operators::GTSign_strategy = st.builds(
    cobol::operators::GTSign,
)
operators::UnaryOperator_strategy = st.builds(
    operators::UnaryOperator,
)
operators::AdditiveOperator_strategy = st.builds(
    operators::AdditiveOperator,
)
cobol::operators::Subtraction_strategy = st.builds(
    cobol::operators::Subtraction,
)
cobol::operators::Addition_strategy = st.builds(
    cobol::operators::Addition,
)
cobol::operators::ConditionAnd_strategy = st.builds(
    cobol::operators::ConditionAnd,
)
cobol::operators::ConditionOr_strategy = st.builds(
    cobol::operators::ConditionOr,
)
Operator_strategy = st.builds(
    Operator,
)
cobol::operators::RelationalOperator_strategy = st.builds(
    cobol::operators::RelationalOperator,
)
cobol::operators::UnaryOperator_strategy = st.builds(
    cobol::operators::UnaryOperator,
)
cobol::operators::LogicalOperator_strategy = st.builds(
    cobol::operators::LogicalOperator,
)
cobol::operators::MultiplicativeOperator_strategy = st.builds(
    cobol::operators::MultiplicativeOperator,
)
cobol::operators::SignOperator_strategy = st.builds(
    cobol::operators::SignOperator,
)
cobol::operators::AdditiveOperator_strategy = st.builds(
    cobol::operators::AdditiveOperator,
)
cobol::operators::Operator_strategy = st.builds(
    cobol::operators::Operator,
)
AlphanumericLiteral_strategy = st.builds(
    AlphanumericLiteral,
)
cobol::literals::AlphanumericHexaDecimalLiteral_strategy = st.builds(
    cobol::literals::AlphanumericHexaDecimalLiteral,
)
cobol::operators::ClassOperator_strategy = st.builds(
    cobol::operators::ClassOperator,
)
cobol::operators::Through_strategy = st.builds(
    cobol::operators::Through,
    value=
        safe_text
)
cobol::operators::Negate_strategy = st.builds(
    cobol::operators::Negate,
)
cobol::operators::Power_strategy = st.builds(
    cobol::operators::Power,
)
cobol::operators::Equal_strategy = st.builds(
    cobol::operators::Equal,
    to=
        st.booleans()
)
cobol::operators::LessThanOrEqual_strategy = st.builds(
    cobol::operators::LessThanOrEqual,
    than=
        st.booleans(),
    to=
        st.booleans()
)
cobol::operators::LessThan_strategy = st.builds(
    cobol::operators::LessThan,
    than=
        st.booleans()
)
cobol::operators::GreaterThan_strategy = st.builds(
    cobol::operators::GreaterThan,
    than=
        st.booleans()
)
cobol::operators::GreaterThanOrEqual_strategy = st.builds(
    cobol::operators::GreaterThanOrEqual,
    to=
        st.booleans(),
    than=
        st.booleans()
)
DBCSLiteral_strategy = st.builds(
    DBCSLiteral,
)
cobol::literals::NationalHexLiteral_strategy = st.builds(
    cobol::literals::NationalHexLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cobol::literals::NationalLiteral_strategy = st.builds(
    cobol::literals::NationalLiteral,
    value=
        safe_text
)
labels::StopLabel_strategy = st.builds(
    labels::StopLabel,
)
ConstantLiteral_strategy = st.builds(
    ConstantLiteral,
)
cobol::literals::HighValue_strategy = st.builds(
    cobol::literals::HighValue,
    value=
        safe_text
)
cobol::literals::LowValue_strategy = st.builds(
    cobol::literals::LowValue,
    value=
        safe_text
)
cobol::literals::Quote_strategy = st.builds(
    cobol::literals::Quote,
    value=
        safe_text
)
cobol::literals::Null_strategy = st.builds(
    cobol::literals::Null,
    value=
        safe_text
)
cobol::literals::Zero_strategy = st.builds(
    cobol::literals::Zero,
    value=
        safe_text
)
cobol::literals::Space_strategy = st.builds(
    cobol::literals::Space,
    value=
        safe_text
)
FigurativeConstantLiteral_strategy = st.builds(
    FigurativeConstantLiteral,
)
cobol::literals::ConstantLiteral_strategy = st.builds(
    cobol::literals::ConstantLiteral,
)
cobol::literals::AllLiteral_strategy = st.builds(
    cobol::literals::AllLiteral,
)
DecimalLiteral_strategy = st.builds(
    DecimalLiteral,
)
cobol::literals::FixedDecimalLiteral_strategy = st.builds(
    cobol::literals::FixedDecimalLiteral,
)
cobol::literals::FloatingDecimalLiteral_strategy = st.builds(
    cobol::literals::FloatingDecimalLiteral,
)
NumericLiteral_strategy = st.builds(
    NumericLiteral,
)
cobol::literals::DecimalLiteral_strategy = st.builds(
    cobol::literals::DecimalLiteral,
    value=
        safe_text
)
water::IOControlParagraphWater_strategy = st.builds(
    water::IOControlParagraphWater,
)
water::FileDescriptorWater_strategy = st.builds(
    water::FileDescriptorWater,
)
water::ObjectComputerParagraphWater_strategy = st.builds(
    water::ObjectComputerParagraphWater,
)
literals::NumericLiteral_strategy = st.builds(
    literals::NumericLiteral,
)
cobol::literals::IntegerLiteral_strategy = st.builds(
    cobol::literals::IntegerLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Literal_strategy = st.builds(
    Literal,
)
cobol::literals::NumericLiteral_strategy = st.builds(
    cobol::literals::NumericLiteral,
)
cobol::literals::Any_strategy = st.builds(
    cobol::literals::Any,
)
cobol::literals::FigurativeConstantLiteral_strategy = st.builds(
    cobol::literals::FigurativeConstantLiteral,
)
cobol::literals::DBCSLiteral_strategy = st.builds(
    cobol::literals::DBCSLiteral,
)
cobol::literals::PseudoLiteral_strategy = st.builds(
    cobol::literals::PseudoLiteral,
    value=
        safe_text
)
cobol::literals::BooleanLiteral_strategy = st.builds(
    cobol::literals::BooleanLiteral,
    value=
        st.booleans()
)
cobol::literals::Characters_strategy = st.builds(
    cobol::literals::Characters,
)
cobol::literals::AlphanumericLiteral_strategy = st.builds(
    cobol::literals::AlphanumericLiteral,
    value=
        safe_text
)
Division_strategy = st.builds(
    Division,
)
cobol::divisions::EnvironmentDivision_strategy = st.builds(
    cobol::divisions::EnvironmentDivision,
)
cobol::divisions::DataDivision_strategy = st.builds(
    cobol::divisions::DataDivision,
)
StatementContainer_strategy = st.builds(
    StatementContainer,
)
cobol::sentences::Sentence_strategy = st.builds(
    cobol::sentences::Sentence,
)
cobol::sentences::ExecuteSentence_strategy = st.builds(
    cobol::sentences::ExecuteSentence,
)
Paragraph_strategy = st.builds(
    Paragraph,
)
cobol::paragraphs::IOSectionParagraph_strategy = st.builds(
    cobol::paragraphs::IOSectionParagraph,
)
cobol::paragraphs::ConfigurationSectionParagraph_strategy = st.builds(
    cobol::paragraphs::ConfigurationSectionParagraph,
)
Section_strategy = st.builds(
    Section,
)
cobol::sections::DeclarativeSection_strategy = st.builds(
    cobol::sections::DeclarativeSection,
)
cobol::sections::DataDivisionSection_strategy = st.builds(
    cobol::sections::DataDivisionSection,
)
cobol::sections::EnvironmentDivisionSection_strategy = st.builds(
    cobol::sections::EnvironmentDivisionSection,
)
CobolRoot_strategy = st.builds(
    CobolRoot,
)
cobol::containers::EmptyModel_strategy = st.builds(
    cobol::containers::EmptyModel,
)
cobol::containers::CobolRoot_strategy = st.builds(
    cobol::containers::CobolRoot,
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
water::InvokeStatementWater_strategy = st.builds(
    water::InvokeStatementWater,
)
operands::PrimaryOperand_strategy = st.builds(
    operands::PrimaryOperand,
)
water::CICSStatementWater_strategy = st.builds(
    water::CICSStatementWater,
)
water::SpecialNamesParagraphWater_strategy = st.builds(
    water::SpecialNamesParagraphWater,
)
water::SelectStatementWater_strategy = st.builds(
    water::SelectStatementWater,
)
cobol::identifiers::Identifier_strategy = st.builds(
    cobol::identifiers::Identifier,
)
cobol::literals::Literal_strategy = st.builds(
    cobol::literals::Literal,
)
Declaratives_strategy = st.builds(
    Declaratives,
)
parameters::Parametrizable_strategy = st.builds(
    parameters::Parametrizable,
)
cobol::statements::Entry_strategy = st.builds(
    cobol::statements::Entry,
)
water::IncompleteElement_strategy = st.builds(
    water::IncompleteElement,
)
cobol::files::FileName_strategy = st.builds(
    cobol::files::FileName,
    fileDescriptor=
        safe_text
)
cobol::statements::Merge_strategy = st.builds(
    cobol::statements::Merge,
)
cobol::statements::Accept_strategy = st.builds(
    cobol::statements::Accept,
)
cobol::dataitems::DataItem_strategy = st.builds(
    cobol::dataitems::DataItem,
    levelNumber=
        safe_text
)
cobol::paragraphs::RepositoryParagraph_strategy = st.builds(
    cobol::paragraphs::RepositoryParagraph,
)
cobol::statements::Sort_strategy = st.builds(
    cobol::statements::Sort,
)
cobol::statements::Open_strategy = st.builds(
    cobol::statements::Open,
)
cobol::paragraphs::IOControlParagraph_strategy = st.builds(
    cobol::paragraphs::IOControlParagraph,
)
cobol::paragraphs::ObjectComputerParagraph_strategy = st.builds(
    cobol::paragraphs::ObjectComputerParagraph,
)
cobol::sentences::UseSentence_strategy = st.builds(
    cobol::sentences::UseSentence,
)
cobol::tables::Table_strategy = st.builds(
    cobol::tables::Table,
)
cobol::statements::Close_strategy = st.builds(
    cobol::statements::Close,
)
divisions::Division_strategy = st.builds(
    divisions::Division,
)
cobol::divisions::ProcedureDivision_strategy = st.builds(
    cobol::divisions::ProcedureDivision,
)
cobol::divisions::IdentificationDivision_strategy = st.builds(
    cobol::divisions::IdentificationDivision,
    properties=
        safe_text
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
cobol::arithmetics::RangeExpression_strategy = st.builds(
    cobol::arithmetics::RangeExpression,
)
Equal_strategy = st.builds(
    Equal,
)
cobol::operators::EqualPhrase_strategy = st.builds(
    cobol::operators::EqualPhrase,
)
cobol::operators::EqualSign_strategy = st.builds(
    cobol::operators::EqualSign,
)
cobol::arithmetics::AssignmentExpression_strategy = st.builds(
    cobol::arithmetics::AssignmentExpression,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
UnaryArithmeticExpressionChild_strategy = st.builds(
    UnaryArithmeticExpressionChild,
)
cobol::arithmetics::PrimaryExpression_strategy = st.builds(
    cobol::arithmetics::PrimaryExpression,
)
PowerArithmeticExpressionChild_strategy = st.builds(
    PowerArithmeticExpressionChild,
)
cobol::arithmetics::UnaryArithmeticExpression_strategy = st.builds(
    cobol::arithmetics::UnaryArithmeticExpression,
)
cobol::arithmetics::UnaryArithmeticExpressionChild_strategy = st.builds(
    cobol::arithmetics::UnaryArithmeticExpressionChild,
)
IdentificationDivision_strategy = st.builds(
    IdentificationDivision,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
cobol::divisions::Division_strategy = st.builds(
    cobol::divisions::Division,
)
cobol::references::ReferenceableElement_strategy = st.builds(
    cobol::references::ReferenceableElement,
)
cobol::containers::CompilationUnit_strategy = st.builds(
    cobol::containers::CompilationUnit,
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
commons::NamedElement_strategy = st.builds(
    commons::NamedElement,
)
cobol::functions::FunctionCall_strategy = st.builds(
    cobol::functions::FunctionCall,
)
cobol::sections::Section_strategy = st.builds(
    cobol::sections::Section,
    segmentNumber=
        safe_text
)
cobol::tables::IndexName_strategy = st.builds(
    cobol::tables::IndexName,
)
cobol::specialnames::ConditionName_strategy = st.builds(
    cobol::specialnames::ConditionName,
)
cobol::paragraphs::Paragraph_strategy = st.builds(
    cobol::paragraphs::Paragraph,
)
containers::CobolRoot_strategy = st.builds(
    containers::CobolRoot,
)
cobol::containers::CompilationGroup_strategy = st.builds(
    cobol::containers::CompilationGroup,
)
conditions::SimpleConditionChild_strategy = st.builds(
    conditions::SimpleConditionChild,
)
conditions::AbbreviatedRelationalExpressionChild_strategy = st.builds(
    conditions::AbbreviatedRelationalExpressionChild,
)
cobol::arithmetics::ArithmeticExpression_strategy = st.builds(
    cobol::arithmetics::ArithmeticExpression,
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
cobol::arithmetics::NestedArithmeticExpression_strategy = st.builds(
    cobol::arithmetics::NestedArithmeticExpression,
)
cobol::arithmetics::RangeExpressionChild_strategy = st.builds(
    cobol::arithmetics::RangeExpressionChild,
)
Through_strategy = st.builds(
    Through,
)
ClassOperator_strategy = st.builds(
    ClassOperator,
)
cobol::operators::ClassName_strategy = st.builds(
    cobol::operators::ClassName,
)
cobol::operators::DBCS_strategy = st.builds(
    cobol::operators::DBCS,
)
cobol::operators::Kanji_strategy = st.builds(
    cobol::operators::Kanji,
)
cobol::operators::AlphabeticLower_strategy = st.builds(
    cobol::operators::AlphabeticLower,
)
cobol::operators::AlphabeticUpper_strategy = st.builds(
    cobol::operators::AlphabeticUpper,
)
cobol::operators::Numeric_strategy = st.builds(
    cobol::operators::Numeric,
)
cobol::operators::Alphabetic_strategy = st.builds(
    cobol::operators::Alphabetic,
)
cobol::conditions::ClassCondition_strategy = st.builds(
    cobol::conditions::ClassCondition,
)
SignOperator_strategy = st.builds(
    SignOperator,
)
cobol::operators::Negative_strategy = st.builds(
    cobol::operators::Negative,
)
cobol::operators::Zero_strategy = st.builds(
    cobol::operators::Zero,
)
cobol::operators::Positive_strategy = st.builds(
    cobol::operators::Positive,
)
MultiplicativeOperator_strategy = st.builds(
    MultiplicativeOperator,
)
cobol::operators::Multiplication_strategy = st.builds(
    cobol::operators::Multiplication,
)
cobol::operators::Division_strategy = st.builds(
    cobol::operators::Division,
)
MultiplicativeArithmeticExpressionChild_strategy = st.builds(
    MultiplicativeArithmeticExpressionChild,
)
cobol::arithmetics::PowerArithmeticExpressionChild_strategy = st.builds(
    cobol::arithmetics::PowerArithmeticExpressionChild,
)
cobol::arithmetics::PowerArithmeticExpression_strategy = st.builds(
    cobol::arithmetics::PowerArithmeticExpression,
)
AdditiveOperator_strategy = st.builds(
    AdditiveOperator,
)
AdditiveArithmeticExpressionChild_strategy = st.builds(
    AdditiveArithmeticExpressionChild,
)
cobol::arithmetics::MultiplicativeArithmeticExpressionChild_strategy = st.builds(
    cobol::arithmetics::MultiplicativeArithmeticExpressionChild,
)
cobol::arithmetics::MultiplicativeArithmeticExpression_strategy = st.builds(
    cobol::arithmetics::MultiplicativeArithmeticExpression,
)
RangeExpressionChild_strategy = st.builds(
    RangeExpressionChild,
)
cobol::arithmetics::AdditiveArithmeticExpressionChild_strategy = st.builds(
    cobol::arithmetics::AdditiveArithmeticExpressionChild,
)
cobol::arithmetics::AdditiveArithmeticExpression_strategy = st.builds(
    cobol::arithmetics::AdditiveArithmeticExpression,
)
cobol::conditions::NestedCondition_strategy = st.builds(
    cobol::conditions::NestedCondition,
)
NegatedAbbreviatedConditionalExpressionChild_strategy = st.builds(
    NegatedAbbreviatedConditionalExpressionChild,
)
cobol::conditions::AbbreviatedRelationalExpressionChild_strategy = st.builds(
    cobol::conditions::AbbreviatedRelationalExpressionChild,
)
cobol::conditions::AbbreviatedRelationalExpression_strategy = st.builds(
    cobol::conditions::AbbreviatedRelationalExpression,
)
cobol::conditions::AbbreviatedConditionalExpressionChild_strategy = st.builds(
    cobol::conditions::AbbreviatedConditionalExpressionChild,
)
AbbreviatedConditionalExpressionChild_strategy = st.builds(
    AbbreviatedConditionalExpressionChild,
)
cobol::conditions::NegatedAbbreviatedConditionalExpressionChild_strategy = st.builds(
    cobol::conditions::NegatedAbbreviatedConditionalExpressionChild,
)
cobol::conditions::NegatedAbbreviatedConditionalExpression_strategy = st.builds(
    cobol::conditions::NegatedAbbreviatedConditionalExpression,
)
cobol::conditions::AbbreviatedConditionalExpression_strategy = st.builds(
    cobol::conditions::AbbreviatedConditionalExpression,
)
cobol::conditions::ConditionalAndExpression_strategy = st.builds(
    cobol::conditions::ConditionalAndExpression,
)
cobol::conditions::ConditionalAndExpressionChild_strategy = st.builds(
    cobol::conditions::ConditionalAndExpressionChild,
)
cobol::conditions::ExpressionList_strategy = st.builds(
    cobol::conditions::ExpressionList,
)
cobol::conditions::SignCondition_strategy = st.builds(
    cobol::conditions::SignCondition,
)
AbbreviatedRelationalExpressionChild_strategy = st.builds(
    AbbreviatedRelationalExpressionChild,
)
cobol::conditions::NestedAbbreviatedConditionalExpression_strategy = st.builds(
    cobol::conditions::NestedAbbreviatedConditionalExpression,
)

@given(instance=strings::Occurrence_strategy)
@settings(max_examples=50)
def test_strings::occurrence_instantiation(instance):
    assert isinstance(instance, strings::Occurrence)

@given(instance=strings::Tallying_strategy)
@settings(max_examples=50)
def test_strings::tallying_instantiation(instance):
    assert isinstance(instance, strings::Tallying)

@given(instance=cobol::strings::TallyingOccurrence_strategy)
@settings(max_examples=50)
def test_cobol::strings::tallyingoccurrence_instantiation(instance):
    assert isinstance(instance, cobol::strings::TallyingOccurrence)

@given(instance=cobol::strings::Occurrence_strategy)
@settings(max_examples=50)
def test_cobol::strings::occurrence_instantiation(instance):
    assert isinstance(instance, cobol::strings::Occurrence)

@given(instance=cobol::strings::Occurrence_strategy)
def test_cobol::strings::occurrence_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cobol::strings::Occurrence_strategy)
def test_cobol::strings::occurrence_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cobol::strings::Location_strategy)
@settings(max_examples=50)
def test_cobol::strings::location_instantiation(instance):
    assert isinstance(instance, cobol::strings::Location)

@given(instance=cobol::strings::Location_strategy)
def test_cobol::strings::location_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=cobol::strings::Location_strategy)
def test_cobol::strings::location_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=cobol::strings::Location_strategy)
def test_cobol::strings::location_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=cobol::strings::Location_strategy)
def test_cobol::strings::location_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=ManipulatedStrings_strategy)
@settings(max_examples=50)
def test_manipulatedstrings_instantiation(instance):
    assert isinstance(instance, ManipulatedStrings)

@given(instance=cobol::strings::SplittedString_strategy)
@settings(max_examples=50)
def test_cobol::strings::splittedstring_instantiation(instance):
    assert isinstance(instance, cobol::strings::SplittedString)

@given(instance=cobol::strings::ConcatenatingStrings_strategy)
@settings(max_examples=50)
def test_cobol::strings::concatenatingstrings_instantiation(instance):
    assert isinstance(instance, cobol::strings::ConcatenatingStrings)

@given(instance=cobol::strings::String_strategy)
@settings(max_examples=50)
def test_cobol::strings::string_instantiation(instance):
    assert isinstance(instance, cobol::strings::String)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=String_strategy)
@settings(max_examples=50)
def test_string_instantiation(instance):
    assert isinstance(instance, String)

@given(instance=cobol::strings::ManipulatedStrings_strategy)
@settings(max_examples=50)
def test_cobol::strings::manipulatedstrings_instantiation(instance):
    assert isinstance(instance, cobol::strings::ManipulatedStrings)

@given(instance=cobol::strings::StringManipulation_strategy)
@settings(max_examples=50)
def test_cobol::strings::stringmanipulation_instantiation(instance):
    assert isinstance(instance, cobol::strings::StringManipulation)

@given(instance=StringManipulation_strategy)
@settings(max_examples=50)
def test_stringmanipulation_instantiation(instance):
    assert isinstance(instance, StringManipulation)

@given(instance=cobol::strings::Replacement_strategy)
@settings(max_examples=50)
def test_cobol::strings::replacement_instantiation(instance):
    assert isinstance(instance, cobol::strings::Replacement)

@given(instance=cobol::strings::Tallying_strategy)
@settings(max_examples=50)
def test_cobol::strings::tallying_instantiation(instance):
    assert isinstance(instance, cobol::strings::Tallying)

@given(instance=strings::Replacement_strategy)
@settings(max_examples=50)
def test_strings::replacement_instantiation(instance):
    assert isinstance(instance, strings::Replacement)

@given(instance=cobol::strings::ReplacementOccurrence_strategy)
@settings(max_examples=50)
def test_cobol::strings::replacementoccurrence_instantiation(instance):
    assert isinstance(instance, cobol::strings::ReplacementOccurrence)

@given(instance=NotErrorHandler_strategy)
@settings(max_examples=50)
def test_noterrorhandler_instantiation(instance):
    assert isinstance(instance, NotErrorHandler)

@given(instance=cobol::handlers::NotOnOverflow_strategy)
@settings(max_examples=50)
def test_cobol::handlers::notonoverflow_instantiation(instance):
    assert isinstance(instance, cobol::handlers::NotOnOverflow)

@given(instance=cobol::handlers::NotAtEnd_strategy)
@settings(max_examples=50)
def test_cobol::handlers::notatend_instantiation(instance):
    assert isinstance(instance, cobol::handlers::NotAtEnd)

@given(instance=cobol::handlers::NotInvalidKey_strategy)
@settings(max_examples=50)
def test_cobol::handlers::notinvalidkey_instantiation(instance):
    assert isinstance(instance, cobol::handlers::NotInvalidKey)

@given(instance=cobol::handlers::NotOnException_strategy)
@settings(max_examples=50)
def test_cobol::handlers::notonexception_instantiation(instance):
    assert isinstance(instance, cobol::handlers::NotOnException)

@given(instance=cobol::handlers::NotOnSizeError_strategy)
@settings(max_examples=50)
def test_cobol::handlers::notonsizeerror_instantiation(instance):
    assert isinstance(instance, cobol::handlers::NotOnSizeError)

@given(instance=cobol::functions::Argumentable_strategy)
@settings(max_examples=50)
def test_cobol::functions::argumentable_instantiation(instance):
    assert isinstance(instance, cobol::functions::Argumentable)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=cobol::functions::OmittedArgument_strategy)
@settings(max_examples=50)
def test_cobol::functions::omittedargument_instantiation(instance):
    assert isinstance(instance, cobol::functions::OmittedArgument)

@given(instance=cobol::functions::ByContentArgument_strategy)
@settings(max_examples=50)
def test_cobol::functions::bycontentargument_instantiation(instance):
    assert isinstance(instance, cobol::functions::ByContentArgument)

@given(instance=cobol::functions::ByValueArgument_strategy)
@settings(max_examples=50)
def test_cobol::functions::byvalueargument_instantiation(instance):
    assert isinstance(instance, cobol::functions::ByValueArgument)

@given(instance=cobol::functions::ByReferenceArgument_strategy)
@settings(max_examples=50)
def test_cobol::functions::byreferenceargument_instantiation(instance):
    assert isinstance(instance, cobol::functions::ByReferenceArgument)

@given(instance=cobol::functions::Argument_strategy)
@settings(max_examples=50)
def test_cobol::functions::argument_instantiation(instance):
    assert isinstance(instance, cobol::functions::Argument)

@given(instance=cobol::labels::Label_strategy)
@settings(max_examples=50)
def test_cobol::labels::label_instantiation(instance):
    assert isinstance(instance, cobol::labels::Label)

@given(instance=cobol::labels::Procedure_strategy)
@settings(max_examples=50)
def test_cobol::labels::procedure_instantiation(instance):
    assert isinstance(instance, cobol::labels::Procedure)

@given(instance=Procedure_strategy)
@settings(max_examples=50)
def test_procedure_instantiation(instance):
    assert isinstance(instance, Procedure)

@given(instance=cobol::handlers::NotAtEndOfPage_strategy)
@settings(max_examples=50)
def test_cobol::handlers::notatendofpage_instantiation(instance):
    assert isinstance(instance, cobol::handlers::NotAtEndOfPage)

@given(instance=ProcedureRangeChild_strategy)
@settings(max_examples=50)
def test_procedurerangechild_instantiation(instance):
    assert isinstance(instance, ProcedureRangeChild)

@given(instance=cobol::verbs::Verb_strategy)
@settings(max_examples=50)
def test_cobol::verbs::verb_instantiation(instance):
    assert isinstance(instance, cobol::verbs::Verb)

@given(instance=Verb_strategy)
@settings(max_examples=50)
def test_verb_instantiation(instance):
    assert isinstance(instance, Verb)

@given(instance=cobol::verbs::Is_strategy)
@settings(max_examples=50)
def test_cobol::verbs::is_instantiation(instance):
    assert isinstance(instance, cobol::verbs::Is)

@given(instance=DeclarativeSection_strategy)
@settings(max_examples=50)
def test_declarativesection_instantiation(instance):
    assert isinstance(instance, DeclarativeSection)

@given(instance=cobol::declaratives::Declaratives_strategy)
@settings(max_examples=50)
def test_cobol::declaratives::declaratives_instantiation(instance):
    assert isinstance(instance, cobol::declaratives::Declaratives)

@given(instance=cobol::labels::ProcedureLabel_strategy)
@settings(max_examples=50)
def test_cobol::labels::procedurelabel_instantiation(instance):
    assert isinstance(instance, cobol::labels::ProcedureLabel)

@given(instance=cobol::files::FileStatus_strategy)
@settings(max_examples=50)
def test_cobol::files::filestatus_instantiation(instance):
    assert isinstance(instance, cobol::files::FileStatus)

@given(instance=FileStatus_strategy)
@settings(max_examples=50)
def test_filestatus_instantiation(instance):
    assert isinstance(instance, FileStatus)

@given(instance=cobol::tables::TableDimension_strategy)
@settings(max_examples=50)
def test_cobol::tables::tabledimension_instantiation(instance):
    assert isinstance(instance, cobol::tables::TableDimension)

@given(instance=cobol::tables::TableDimension_strategy)
def test_cobol::tables::tabledimension_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=cobol::tables::TableDimension_strategy)
def test_cobol::tables::tabledimension_value_setter(instance):
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

@given(instance=cobol::parameters::ByReferenceParameter_strategy)
@settings(max_examples=50)
def test_cobol::parameters::byreferenceparameter_instantiation(instance):
    assert isinstance(instance, cobol::parameters::ByReferenceParameter)

@given(instance=cobol::parameters::ByValueParameter_strategy)
@settings(max_examples=50)
def test_cobol::parameters::byvalueparameter_instantiation(instance):
    assert isinstance(instance, cobol::parameters::ByValueParameter)

@given(instance=cobol::parameters::Parametrizable_strategy)
@settings(max_examples=50)
def test_cobol::parameters::parametrizable_instantiation(instance):
    assert isinstance(instance, cobol::parameters::Parametrizable)

@given(instance=IndexName_strategy)
@settings(max_examples=50)
def test_indexname_instantiation(instance):
    assert isinstance(instance, IndexName)

@given(instance=TableDimension_strategy)
@settings(max_examples=50)
def test_tabledimension_instantiation(instance):
    assert isinstance(instance, TableDimension)

@given(instance=dataitems::DataItem_strategy)
@settings(max_examples=50)
def test_dataitems::dataitem_instantiation(instance):
    assert isinstance(instance, dataitems::DataItem)

@given(instance=cobol::specialnames::SpecialNameStatement_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::specialnamestatement_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::SpecialNameStatement)

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

@given(instance=cobol::specialnames::SymbolicCharacter_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::symboliccharacter_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::SymbolicCharacter)

@given(instance=cobol::specialnames::MnemonicName_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::mnemonicname_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::MnemonicName)

@given(instance=cobol::tables::KeyName_strategy)
@settings(max_examples=50)
def test_cobol::tables::keyname_instantiation(instance):
    assert isinstance(instance, cobol::tables::KeyName)

@given(instance=cobol::tables::KeyName_strategy)
def test_cobol::tables::keyname_keyOrder_type(instance):
    assert isinstance(instance.keyOrder, str)


@given(instance=cobol::tables::KeyName_strategy)
def test_cobol::tables::keyname_keyOrder_setter(instance):
    original = instance.keyOrder
    instance.keyOrder = original
    assert instance.keyOrder == original

@given(instance=KeyName_strategy)
@settings(max_examples=50)
def test_keyname_instantiation(instance):
    assert isinstance(instance, KeyName)

@given(instance=cobol::specialnames::AlphabetType_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::alphabettype_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::AlphabetType)

@given(instance=specialnames::MnemonicName_strategy)
@settings(max_examples=50)
def test_specialnames::mnemonicname_instantiation(instance):
    assert isinstance(instance, specialnames::MnemonicName)

@given(instance=AlphabetType_strategy)
@settings(max_examples=50)
def test_alphabettype_instantiation(instance):
    assert isinstance(instance, AlphabetType)

@given(instance=cobol::specialnames::CodeNameAlphabetType_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::codenamealphabettype_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::CodeNameAlphabetType)

@given(instance=cobol::specialnames::CodeNameAlphabetType_strategy)
def test_cobol::specialnames::codenamealphabettype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::specialnames::CodeNameAlphabetType_strategy)
def test_cobol::specialnames::codenamealphabettype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::specialnames::PredefinedAlphabetType_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::predefinedalphabettype_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::PredefinedAlphabetType)

@given(instance=cobol::specialnames::PredefinedAlphabetType_strategy)
def test_cobol::specialnames::predefinedalphabettype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::specialnames::PredefinedAlphabetType_strategy)
def test_cobol::specialnames::predefinedalphabettype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=specialnames::SpecialNameStatement_strategy)
@settings(max_examples=50)
def test_specialnames::specialnamestatement_instantiation(instance):
    assert isinstance(instance, specialnames::SpecialNameStatement)

@given(instance=cobol::specialnames::UPSISwitchIs_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::upsiswitchis_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::UPSISwitchIs)

@given(instance=cobol::specialnames::SystemDeviceIs_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::systemdeviceis_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::SystemDeviceIs)

@given(instance=ConditionName_strategy)
@settings(max_examples=50)
def test_conditionname_instantiation(instance):
    assert isinstance(instance, ConditionName)

@given(instance=cobol::specialnames::OffStatus_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::offstatus_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::OffStatus)

@given(instance=cobol::specialnames::OnStatus_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::onstatus_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::OnStatus)

@given(instance=specialnames::SpecialName_strategy)
@settings(max_examples=50)
def test_specialnames::specialname_instantiation(instance):
    assert isinstance(instance, specialnames::SpecialName)

@given(instance=cobol::specialnames::CurrencySign_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::currencysign_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::CurrencySign)

@given(instance=cobol::specialnames::CurrencySign_strategy)
def test_cobol::specialnames::currencysign_pictureSymbol_type(instance):
    assert isinstance(instance.pictureSymbol, str)


@given(instance=cobol::specialnames::CurrencySign_strategy)
def test_cobol::specialnames::currencysign_pictureSymbol_setter(instance):
    original = instance.pictureSymbol
    instance.pictureSymbol = original
    assert instance.pictureSymbol == original

@given(instance=cobol::specialnames::ClassName_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::classname_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::ClassName)

@given(instance=cobol::specialnames::AlphabetName_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::alphabetname_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::AlphabetName)

@given(instance=cobol::specialnames::ExplicitAlphabetType_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::explicitalphabettype_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::ExplicitAlphabetType)

@given(instance=references::ReferenceableElement_strategy)
@settings(max_examples=50)
def test_references::referenceableelement_instantiation(instance):
    assert isinstance(instance, references::ReferenceableElement)

@given(instance=cobol::dataitems::DataItemAttribute_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::dataitemattribute_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::DataItemAttribute)

@given(instance=RangeExpression_strategy)
@settings(max_examples=50)
def test_rangeexpression_instantiation(instance):
    assert isinstance(instance, RangeExpression)

@given(instance=DataName_strategy)
@settings(max_examples=50)
def test_dataname_instantiation(instance):
    assert isinstance(instance, DataName)

@given(instance=cobol::dataitems::RenamingDataName_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::renamingdataname_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::RenamingDataName)

@given(instance=DataItemAttribute_strategy)
@settings(max_examples=50)
def test_dataitemattribute_instantiation(instance):
    assert isinstance(instance, DataItemAttribute)

@given(instance=cobol::dataitems::Redefines_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::redefines_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::Redefines)

@given(instance=cobol::dataitems::Usage_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::usage_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::Usage)

@given(instance=cobol::dataitems::Usage_strategy)
def test_cobol::dataitems::usage_usage_type(instance):
    assert isinstance(instance.usage, str)


@given(instance=cobol::dataitems::Usage_strategy)
def test_cobol::dataitems::usage_usage_setter(instance):
    original = instance.usage
    instance.usage = original
    assert instance.usage == original

@given(instance=cobol::dataitems::Usage_strategy)
def test_cobol::dataitems::usage_isNative_type(instance):
    assert isinstance(instance.isNative, bool)


@given(instance=cobol::dataitems::Usage_strategy)
def test_cobol::dataitems::usage_isNative_setter(instance):
    original = instance.isNative
    instance.isNative = original
    assert instance.isNative == original

@given(instance=cobol::dataitems::Value_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::value_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::Value)

@given(instance=cobol::dataitems::External_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::external_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::External)

@given(instance=cobol::dataitems::GroupUsage_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::groupusage_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::GroupUsage)

@given(instance=cobol::dataitems::Global_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::global_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::Global)

@given(instance=cobol::dataitems::PictureString_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::picturestring_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::PictureString)

@given(instance=cobol::dataitems::PictureString_strategy)
def test_cobol::dataitems::picturestring_picture_type(instance):
    assert isinstance(instance.picture, str)


@given(instance=cobol::dataitems::PictureString_strategy)
def test_cobol::dataitems::picturestring_picture_setter(instance):
    original = instance.picture
    instance.picture = original
    assert instance.picture == original

@given(instance=SystemDevice_strategy)
@settings(max_examples=50)
def test_systemdevice_instantiation(instance):
    assert isinstance(instance, SystemDevice)

@given(instance=cobol::environments::AdvancedFunctionPrinting_strategy)
@settings(max_examples=50)
def test_cobol::environments::advancedfunctionprinting_instantiation(instance):
    assert isinstance(instance, cobol::environments::AdvancedFunctionPrinting)

@given(instance=cobol::environments::Pocket_strategy)
@settings(max_examples=50)
def test_cobol::environments::pocket_instantiation(instance):
    assert isinstance(instance, cobol::environments::Pocket)

@given(instance=cobol::environments::Pocket_strategy)
def test_cobol::environments::pocket_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::environments::Pocket_strategy)
def test_cobol::environments::pocket_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::environments::SuppressSpacing_strategy)
@settings(max_examples=50)
def test_cobol::environments::suppressspacing_instantiation(instance):
    assert isinstance(instance, cobol::environments::SuppressSpacing)

@given(instance=cobol::environments::SystemLogicalOutput_strategy)
@settings(max_examples=50)
def test_cobol::environments::systemlogicaloutput_instantiation(instance):
    assert isinstance(instance, cobol::environments::SystemLogicalOutput)

@given(instance=cobol::environments::SystemLogicalOutput_strategy)
def test_cobol::environments::systemlogicaloutput_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::environments::SystemLogicalOutput_strategy)
def test_cobol::environments::systemlogicaloutput_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::environments::SystemPunchDevice_strategy)
@settings(max_examples=50)
def test_cobol::environments::systempunchdevice_instantiation(instance):
    assert isinstance(instance, cobol::environments::SystemPunchDevice)

@given(instance=cobol::environments::SystemPunchDevice_strategy)
def test_cobol::environments::systempunchdevice_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::environments::SystemPunchDevice_strategy)
def test_cobol::environments::systempunchdevice_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::environments::Console_strategy)
@settings(max_examples=50)
def test_cobol::environments::console_instantiation(instance):
    assert isinstance(instance, cobol::environments::Console)

@given(instance=cobol::environments::Channel_strategy)
@settings(max_examples=50)
def test_cobol::environments::channel_instantiation(instance):
    assert isinstance(instance, cobol::environments::Channel)

@given(instance=cobol::environments::Channel_strategy)
def test_cobol::environments::channel_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::environments::Channel_strategy)
def test_cobol::environments::channel_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::environments::SystemLogicalInput_strategy)
@settings(max_examples=50)
def test_cobol::environments::systemlogicalinput_instantiation(instance):
    assert isinstance(instance, cobol::environments::SystemLogicalInput)

@given(instance=cobol::environments::SystemLogicalInput_strategy)
def test_cobol::environments::systemlogicalinput_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::environments::SystemLogicalInput_strategy)
def test_cobol::environments::systemlogicalinput_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Register_strategy)
@settings(max_examples=50)
def test_register_instantiation(instance):
    assert isinstance(instance, Register)

@given(instance=cobol::registers::AddressOf_strategy)
@settings(max_examples=50)
def test_cobol::registers::addressof_instantiation(instance):
    assert isinstance(instance, cobol::registers::AddressOf)

@given(instance=cobol::registers::WhenCompiled_strategy)
@settings(max_examples=50)
def test_cobol::registers::whencompiled_instantiation(instance):
    assert isinstance(instance, cobol::registers::WhenCompiled)

@given(instance=cobol::registers::ShiftOut_strategy)
@settings(max_examples=50)
def test_cobol::registers::shiftout_instantiation(instance):
    assert isinstance(instance, cobol::registers::ShiftOut)

@given(instance=cobol::registers::ReturnCode_strategy)
@settings(max_examples=50)
def test_cobol::registers::returncode_instantiation(instance):
    assert isinstance(instance, cobol::registers::ReturnCode)

@given(instance=cobol::registers::LengthOf_strategy)
@settings(max_examples=50)
def test_cobol::registers::lengthof_instantiation(instance):
    assert isinstance(instance, cobol::registers::LengthOf)

@given(instance=cobol::registers::ShiftIn_strategy)
@settings(max_examples=50)
def test_cobol::registers::shiftin_instantiation(instance):
    assert isinstance(instance, cobol::registers::ShiftIn)

@given(instance=SortPhraseWater_strategy)
@settings(max_examples=50)
def test_sortphrasewater_instantiation(instance):
    assert isinstance(instance, SortPhraseWater)

@given(instance=cobol::water::SortPhraseToken_strategy)
@settings(max_examples=50)
def test_cobol::water::sortphrasetoken_instantiation(instance):
    assert isinstance(instance, cobol::water::SortPhraseToken)

@given(instance=cobol::water::SortPhraseToken_strategy)
def test_cobol::water::sortphrasetoken_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::SortPhraseToken_strategy)
def test_cobol::water::sortphrasetoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OpenStatementWater_strategy)
@settings(max_examples=50)
def test_openstatementwater_instantiation(instance):
    assert isinstance(instance, OpenStatementWater)

@given(instance=cobol::water::OpenStatementToken_strategy)
@settings(max_examples=50)
def test_cobol::water::openstatementtoken_instantiation(instance):
    assert isinstance(instance, cobol::water::OpenStatementToken)

@given(instance=cobol::water::OpenStatementToken_strategy)
def test_cobol::water::openstatementtoken_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::OpenStatementToken_strategy)
def test_cobol::water::openstatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=InvokeStatementWater_strategy)
@settings(max_examples=50)
def test_invokestatementwater_instantiation(instance):
    assert isinstance(instance, InvokeStatementWater)

@given(instance=cobol::water::InvokeStatementToken_strategy)
@settings(max_examples=50)
def test_cobol::water::invokestatementtoken_instantiation(instance):
    assert isinstance(instance, cobol::water::InvokeStatementToken)

@given(instance=cobol::water::InvokeStatementToken_strategy)
def test_cobol::water::invokestatementtoken_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::InvokeStatementToken_strategy)
def test_cobol::water::invokestatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CloseStatementWater_strategy)
@settings(max_examples=50)
def test_closestatementwater_instantiation(instance):
    assert isinstance(instance, CloseStatementWater)

@given(instance=cobol::water::CloseStatementToken_strategy)
@settings(max_examples=50)
def test_cobol::water::closestatementtoken_instantiation(instance):
    assert isinstance(instance, cobol::water::CloseStatementToken)

@given(instance=cobol::water::CloseStatementToken_strategy)
def test_cobol::water::closestatementtoken_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::CloseStatementToken_strategy)
def test_cobol::water::closestatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UseStatementWater_strategy)
@settings(max_examples=50)
def test_usestatementwater_instantiation(instance):
    assert isinstance(instance, UseStatementWater)

@given(instance=cobol::water::UseStatementToken_strategy)
@settings(max_examples=50)
def test_cobol::water::usestatementtoken_instantiation(instance):
    assert isinstance(instance, cobol::water::UseStatementToken)

@given(instance=cobol::water::UseStatementToken_strategy)
def test_cobol::water::usestatementtoken_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::UseStatementToken_strategy)
def test_cobol::water::usestatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AcceptStatementWater_strategy)
@settings(max_examples=50)
def test_acceptstatementwater_instantiation(instance):
    assert isinstance(instance, AcceptStatementWater)

@given(instance=cobol::environments::Environment_strategy)
@settings(max_examples=50)
def test_cobol::environments::environment_instantiation(instance):
    assert isinstance(instance, cobol::environments::Environment)

@given(instance=cobol::water::AcceptStatementToken_strategy)
@settings(max_examples=50)
def test_cobol::water::acceptstatementtoken_instantiation(instance):
    assert isinstance(instance, cobol::water::AcceptStatementToken)

@given(instance=cobol::water::AcceptStatementToken_strategy)
def test_cobol::water::acceptstatementtoken_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::AcceptStatementToken_strategy)
def test_cobol::water::acceptstatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CICSStatementWater_strategy)
@settings(max_examples=50)
def test_cicsstatementwater_instantiation(instance):
    assert isinstance(instance, CICSStatementWater)

@given(instance=cobol::water::CICSStatementToken_strategy)
@settings(max_examples=50)
def test_cobol::water::cicsstatementtoken_instantiation(instance):
    assert isinstance(instance, cobol::water::CICSStatementToken)

@given(instance=cobol::water::CICSStatementToken_strategy)
def test_cobol::water::cicsstatementtoken_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::CICSStatementToken_strategy)
def test_cobol::water::cicsstatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQLStatementWater_strategy)
@settings(max_examples=50)
def test_sqlstatementwater_instantiation(instance):
    assert isinstance(instance, SQLStatementWater)

@given(instance=cobol::water::SQLStatementToken_strategy)
@settings(max_examples=50)
def test_cobol::water::sqlstatementtoken_instantiation(instance):
    assert isinstance(instance, cobol::water::SQLStatementToken)

@given(instance=cobol::water::SQLStatementToken_strategy)
def test_cobol::water::sqlstatementtoken_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::SQLStatementToken_strategy)
def test_cobol::water::sqlstatementtoken_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=RepositoryParagraphWater_strategy)
@settings(max_examples=50)
def test_repositoryparagraphwater_instantiation(instance):
    assert isinstance(instance, RepositoryParagraphWater)

@given(instance=cobol::water::RepositoryDescription_strategy)
@settings(max_examples=50)
def test_cobol::water::repositorydescription_instantiation(instance):
    assert isinstance(instance, cobol::water::RepositoryDescription)

@given(instance=cobol::water::RepositoryDescription_strategy)
def test_cobol::water::repositorydescription_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::RepositoryDescription_strategy)
def test_cobol::water::repositorydescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=IOControlParagraphWater_strategy)
@settings(max_examples=50)
def test_iocontrolparagraphwater_instantiation(instance):
    assert isinstance(instance, IOControlParagraphWater)

@given(instance=cobol::water::IOControlDescription_strategy)
@settings(max_examples=50)
def test_cobol::water::iocontroldescription_instantiation(instance):
    assert isinstance(instance, cobol::water::IOControlDescription)

@given(instance=cobol::water::IOControlDescription_strategy)
def test_cobol::water::iocontroldescription_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::IOControlDescription_strategy)
def test_cobol::water::iocontroldescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DataDescriptorWater_strategy)
@settings(max_examples=50)
def test_datadescriptorwater_instantiation(instance):
    assert isinstance(instance, DataDescriptorWater)

@given(instance=cobol::water::DataDescription_strategy)
@settings(max_examples=50)
def test_cobol::water::datadescription_instantiation(instance):
    assert isinstance(instance, cobol::water::DataDescription)

@given(instance=cobol::water::DataDescription_strategy)
def test_cobol::water::datadescription_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::DataDescription_strategy)
def test_cobol::water::datadescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FileDescriptorWater_strategy)
@settings(max_examples=50)
def test_filedescriptorwater_instantiation(instance):
    assert isinstance(instance, FileDescriptorWater)

@given(instance=cobol::water::FileDescription_strategy)
@settings(max_examples=50)
def test_cobol::water::filedescription_instantiation(instance):
    assert isinstance(instance, cobol::water::FileDescription)

@given(instance=cobol::water::FileDescription_strategy)
def test_cobol::water::filedescription_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::FileDescription_strategy)
def test_cobol::water::filedescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SelectStatementWater_strategy)
@settings(max_examples=50)
def test_selectstatementwater_instantiation(instance):
    assert isinstance(instance, SelectStatementWater)

@given(instance=cobol::water::SelectStatementClause_strategy)
@settings(max_examples=50)
def test_cobol::water::selectstatementclause_instantiation(instance):
    assert isinstance(instance, cobol::water::SelectStatementClause)

@given(instance=cobol::water::SelectStatementClause_strategy)
def test_cobol::water::selectstatementclause_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::SelectStatementClause_strategy)
def test_cobol::water::selectstatementclause_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ObjectComputerParagraphWater_strategy)
@settings(max_examples=50)
def test_objectcomputerparagraphwater_instantiation(instance):
    assert isinstance(instance, ObjectComputerParagraphWater)

@given(instance=cobol::water::PriorityNumber_strategy)
@settings(max_examples=50)
def test_cobol::water::prioritynumber_instantiation(instance):
    assert isinstance(instance, cobol::water::PriorityNumber)

@given(instance=cobol::water::PriorityNumber_strategy)
def test_cobol::water::prioritynumber_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::PriorityNumber_strategy)
def test_cobol::water::prioritynumber_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::water::ObjectComputerDescription_strategy)
@settings(max_examples=50)
def test_cobol::water::objectcomputerdescription_instantiation(instance):
    assert isinstance(instance, cobol::water::ObjectComputerDescription)

@given(instance=cobol::water::ObjectComputerDescription_strategy)
def test_cobol::water::objectcomputerdescription_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::ObjectComputerDescription_strategy)
def test_cobol::water::objectcomputerdescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::water::Water_strategy)
@settings(max_examples=50)
def test_cobol::water::water_instantiation(instance):
    assert isinstance(instance, cobol::water::Water)

@given(instance=Water_strategy)
@settings(max_examples=50)
def test_water_instantiation(instance):
    assert isinstance(instance, Water)

@given(instance=cobol::water::SpecialNamesParagraphWater_strategy)
@settings(max_examples=50)
def test_cobol::water::specialnamesparagraphwater_instantiation(instance):
    assert isinstance(instance, cobol::water::SpecialNamesParagraphWater)

@given(instance=cobol::water::SelectStatementWater_strategy)
@settings(max_examples=50)
def test_cobol::water::selectstatementwater_instantiation(instance):
    assert isinstance(instance, cobol::water::SelectStatementWater)

@given(instance=cobol::water::FileDescriptorWater_strategy)
@settings(max_examples=50)
def test_cobol::water::filedescriptorwater_instantiation(instance):
    assert isinstance(instance, cobol::water::FileDescriptorWater)

@given(instance=cobol::water::CICSStatementWater_strategy)
@settings(max_examples=50)
def test_cobol::water::cicsstatementwater_instantiation(instance):
    assert isinstance(instance, cobol::water::CICSStatementWater)

@given(instance=cobol::water::RepositoryParagraphWater_strategy)
@settings(max_examples=50)
def test_cobol::water::repositoryparagraphwater_instantiation(instance):
    assert isinstance(instance, cobol::water::RepositoryParagraphWater)

@given(instance=cobol::water::InvokeStatementWater_strategy)
@settings(max_examples=50)
def test_cobol::water::invokestatementwater_instantiation(instance):
    assert isinstance(instance, cobol::water::InvokeStatementWater)

@given(instance=cobol::water::ObjectComputerParagraphWater_strategy)
@settings(max_examples=50)
def test_cobol::water::objectcomputerparagraphwater_instantiation(instance):
    assert isinstance(instance, cobol::water::ObjectComputerParagraphWater)

@given(instance=cobol::water::DataDescriptorWater_strategy)
@settings(max_examples=50)
def test_cobol::water::datadescriptorwater_instantiation(instance):
    assert isinstance(instance, cobol::water::DataDescriptorWater)

@given(instance=cobol::water::CloseStatementWater_strategy)
@settings(max_examples=50)
def test_cobol::water::closestatementwater_instantiation(instance):
    assert isinstance(instance, cobol::water::CloseStatementWater)

@given(instance=cobol::water::OpenStatementWater_strategy)
@settings(max_examples=50)
def test_cobol::water::openstatementwater_instantiation(instance):
    assert isinstance(instance, cobol::water::OpenStatementWater)

@given(instance=cobol::water::AcceptStatementWater_strategy)
@settings(max_examples=50)
def test_cobol::water::acceptstatementwater_instantiation(instance):
    assert isinstance(instance, cobol::water::AcceptStatementWater)

@given(instance=cobol::water::SQLStatementWater_strategy)
@settings(max_examples=50)
def test_cobol::water::sqlstatementwater_instantiation(instance):
    assert isinstance(instance, cobol::water::SQLStatementWater)

@given(instance=cobol::water::IdentificationDivisionWater_strategy)
@settings(max_examples=50)
def test_cobol::water::identificationdivisionwater_instantiation(instance):
    assert isinstance(instance, cobol::water::IdentificationDivisionWater)

@given(instance=cobol::water::SortPhraseWater_strategy)
@settings(max_examples=50)
def test_cobol::water::sortphrasewater_instantiation(instance):
    assert isinstance(instance, cobol::water::SortPhraseWater)

@given(instance=cobol::water::UseStatementWater_strategy)
@settings(max_examples=50)
def test_cobol::water::usestatementwater_instantiation(instance):
    assert isinstance(instance, cobol::water::UseStatementWater)

@given(instance=cobol::water::IOControlParagraphWater_strategy)
@settings(max_examples=50)
def test_cobol::water::iocontrolparagraphwater_instantiation(instance):
    assert isinstance(instance, cobol::water::IOControlParagraphWater)

@given(instance=cobol::water::IncompleteElement_strategy)
@settings(max_examples=50)
def test_cobol::water::incompleteelement_instantiation(instance):
    assert isinstance(instance, cobol::water::IncompleteElement)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=cobol::labels::ProcedureRangeLabel_strategy)
@settings(max_examples=50)
def test_cobol::labels::procedurerangelabel_instantiation(instance):
    assert isinstance(instance, cobol::labels::ProcedureRangeLabel)

@given(instance=cobol::labels::StopLabel_strategy)
@settings(max_examples=50)
def test_cobol::labels::stoplabel_instantiation(instance):
    assert isinstance(instance, cobol::labels::StopLabel)

@given(instance=cobol::ios::IODirectives_strategy)
@settings(max_examples=50)
def test_cobol::ios::iodirectives_instantiation(instance):
    assert isinstance(instance, cobol::ios::IODirectives)

@given(instance=ios::OutputDirective_strategy)
@settings(max_examples=50)
def test_ios::outputdirective_instantiation(instance):
    assert isinstance(instance, ios::OutputDirective)

@given(instance=ios::FileDirective_strategy)
@settings(max_examples=50)
def test_ios::filedirective_instantiation(instance):
    assert isinstance(instance, ios::FileDirective)

@given(instance=cobol::ios::OutputFile_strategy)
@settings(max_examples=50)
def test_cobol::ios::outputfile_instantiation(instance):
    assert isinstance(instance, cobol::ios::OutputFile)

@given(instance=IODirectives_strategy)
@settings(max_examples=50)
def test_iodirectives_instantiation(instance):
    assert isinstance(instance, IODirectives)

@given(instance=cobol::ios::ProcedureDirective_strategy)
@settings(max_examples=50)
def test_cobol::ios::proceduredirective_instantiation(instance):
    assert isinstance(instance, cobol::ios::ProcedureDirective)

@given(instance=cobol::ios::FileDirective_strategy)
@settings(max_examples=50)
def test_cobol::ios::filedirective_instantiation(instance):
    assert isinstance(instance, cobol::ios::FileDirective)

@given(instance=cobol::ios::OutputDirective_strategy)
@settings(max_examples=50)
def test_cobol::ios::outputdirective_instantiation(instance):
    assert isinstance(instance, cobol::ios::OutputDirective)

@given(instance=cobol::ios::InputDirective_strategy)
@settings(max_examples=50)
def test_cobol::ios::inputdirective_instantiation(instance):
    assert isinstance(instance, cobol::ios::InputDirective)

@given(instance=ios::ProcedureDirective_strategy)
@settings(max_examples=50)
def test_ios::proceduredirective_instantiation(instance):
    assert isinstance(instance, ios::ProcedureDirective)

@given(instance=cobol::ios::OutputProcedure_strategy)
@settings(max_examples=50)
def test_cobol::ios::outputprocedure_instantiation(instance):
    assert isinstance(instance, cobol::ios::OutputProcedure)

@given(instance=ios::InputDirective_strategy)
@settings(max_examples=50)
def test_ios::inputdirective_instantiation(instance):
    assert isinstance(instance, ios::InputDirective)

@given(instance=cobol::ios::InputFile_strategy)
@settings(max_examples=50)
def test_cobol::ios::inputfile_instantiation(instance):
    assert isinstance(instance, cobol::ios::InputFile)

@given(instance=cobol::ios::InputProcedure_strategy)
@settings(max_examples=50)
def test_cobol::ios::inputprocedure_instantiation(instance):
    assert isinstance(instance, cobol::ios::InputProcedure)

@given(instance=cobol::identifiers::ReferenceModifier_strategy)
@settings(max_examples=50)
def test_cobol::identifiers::referencemodifier_instantiation(instance):
    assert isinstance(instance, cobol::identifiers::ReferenceModifier)

@given(instance=DirectSubscript_strategy)
@settings(max_examples=50)
def test_directsubscript_instantiation(instance):
    assert isinstance(instance, DirectSubscript)

@given(instance=cobol::identifiers::All_strategy)
@settings(max_examples=50)
def test_cobol::identifiers::all_instantiation(instance):
    assert isinstance(instance, cobol::identifiers::All)

@given(instance=IdentificationDivisionWater_strategy)
@settings(max_examples=50)
def test_identificationdivisionwater_instantiation(instance):
    assert isinstance(instance, IdentificationDivisionWater)

@given(instance=cobol::water::ProgramDescription_strategy)
@settings(max_examples=50)
def test_cobol::water::programdescription_instantiation(instance):
    assert isinstance(instance, cobol::water::ProgramDescription)

@given(instance=cobol::water::ProgramDescription_strategy)
def test_cobol::water::programdescription_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::ProgramDescription_strategy)
def test_cobol::water::programdescription_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Subscript_strategy)
@settings(max_examples=50)
def test_subscript_instantiation(instance):
    assert isinstance(instance, Subscript)

@given(instance=cobol::identifiers::DirectSubscript_strategy)
@settings(max_examples=50)
def test_cobol::identifiers::directsubscript_instantiation(instance):
    assert isinstance(instance, cobol::identifiers::DirectSubscript)

@given(instance=cobol::identifiers::RelativeSubscript_strategy)
@settings(max_examples=50)
def test_cobol::identifiers::relativesubscript_instantiation(instance):
    assert isinstance(instance, cobol::identifiers::RelativeSubscript)

@given(instance=identifiers::Identifier_strategy)
@settings(max_examples=50)
def test_identifiers::identifier_instantiation(instance):
    assert isinstance(instance, identifiers::Identifier)

@given(instance=ReferenceModifier_strategy)
@settings(max_examples=50)
def test_referencemodifier_instantiation(instance):
    assert isinstance(instance, ReferenceModifier)

@given(instance=water::SortPhraseWater_strategy)
@settings(max_examples=50)
def test_water::sortphrasewater_instantiation(instance):
    assert isinstance(instance, water::SortPhraseWater)

@given(instance=water::DataDescriptorWater_strategy)
@settings(max_examples=50)
def test_water::datadescriptorwater_instantiation(instance):
    assert isinstance(instance, water::DataDescriptorWater)

@given(instance=water::UseStatementWater_strategy)
@settings(max_examples=50)
def test_water::usestatementwater_instantiation(instance):
    assert isinstance(instance, water::UseStatementWater)

@given(instance=water::SQLStatementWater_strategy)
@settings(max_examples=50)
def test_water::sqlstatementwater_instantiation(instance):
    assert isinstance(instance, water::SQLStatementWater)

@given(instance=water::IdentificationDivisionWater_strategy)
@settings(max_examples=50)
def test_water::identificationdivisionwater_instantiation(instance):
    assert isinstance(instance, water::IdentificationDivisionWater)

@given(instance=cobol::water::Dot_strategy)
@settings(max_examples=50)
def test_cobol::water::dot_instantiation(instance):
    assert isinstance(instance, cobol::water::Dot)

@given(instance=water::RepositoryParagraphWater_strategy)
@settings(max_examples=50)
def test_water::repositoryparagraphwater_instantiation(instance):
    assert isinstance(instance, water::RepositoryParagraphWater)

@given(instance=water::AcceptStatementWater_strategy)
@settings(max_examples=50)
def test_water::acceptstatementwater_instantiation(instance):
    assert isinstance(instance, water::AcceptStatementWater)

@given(instance=cobol::identifiers::Subscript_strategy)
@settings(max_examples=50)
def test_cobol::identifiers::subscript_instantiation(instance):
    assert isinstance(instance, cobol::identifiers::Subscript)

@given(instance=VaryingUntilCondition_strategy)
@settings(max_examples=50)
def test_varyinguntilcondition_instantiation(instance):
    assert isinstance(instance, VaryingUntilCondition)

@given(instance=cobol::statements::AfterUntilCondition_strategy)
@settings(max_examples=50)
def test_cobol::statements::afteruntilcondition_instantiation(instance):
    assert isinstance(instance, cobol::statements::AfterUntilCondition)

@given(instance=Qualifier_strategy)
@settings(max_examples=50)
def test_qualifier_instantiation(instance):
    assert isinstance(instance, Qualifier)

@given(instance=Conditional_strategy)
@settings(max_examples=50)
def test_conditional_instantiation(instance):
    assert isinstance(instance, Conditional)

@given(instance=cobol::statements::VaryingUntilCondition_strategy)
@settings(max_examples=50)
def test_cobol::statements::varyinguntilcondition_instantiation(instance):
    assert isinstance(instance, cobol::statements::VaryingUntilCondition)

@given(instance=Tallying_strategy)
@settings(max_examples=50)
def test_tallying_instantiation(instance):
    assert isinstance(instance, Tallying)

@given(instance=cobol::strings::AnyCharacter_strategy)
@settings(max_examples=50)
def test_cobol::strings::anycharacter_instantiation(instance):
    assert isinstance(instance, cobol::strings::AnyCharacter)

@given(instance=cobol::strings::SpecificCharacter_strategy)
@settings(max_examples=50)
def test_cobol::strings::specificcharacter_instantiation(instance):
    assert isinstance(instance, cobol::strings::SpecificCharacter)

@given(instance=cobol::statements::TallyingIn_strategy)
@settings(max_examples=50)
def test_cobol::statements::tallyingin_instantiation(instance):
    assert isinstance(instance, cobol::statements::TallyingIn)

@given(instance=cobol::statements::Statement_strategy)
@settings(max_examples=50)
def test_cobol::statements::statement_instantiation(instance):
    assert isinstance(instance, cobol::statements::Statement)

@given(instance=cobol::statements::Statement_strategy)
def test_cobol::statements::statement_endVerb_type(instance):
    assert isinstance(instance.endVerb, bool)


@given(instance=cobol::statements::Statement_strategy)
def test_cobol::statements::statement_endVerb_setter(instance):
    original = instance.endVerb
    instance.endVerb = original
    assert instance.endVerb == original

@given(instance=cobol::operands::Operand_strategy)
@settings(max_examples=50)
def test_cobol::operands::operand_instantiation(instance):
    assert isinstance(instance, cobol::operands::Operand)

@given(instance=ReplacementOperand_strategy)
@settings(max_examples=50)
def test_replacementoperand_instantiation(instance):
    assert isinstance(instance, ReplacementOperand)

@given(instance=cobol::operands::Encoding_strategy)
@settings(max_examples=50)
def test_cobol::operands::encoding_instantiation(instance):
    assert isinstance(instance, cobol::operands::Encoding)

@given(instance=cobol::operands::Encoding_strategy)
def test_cobol::operands::encoding_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cobol::operands::Encoding_strategy)
def test_cobol::operands::encoding_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Operand_strategy)
@settings(max_examples=50)
def test_operand_instantiation(instance):
    assert isinstance(instance, Operand)

@given(instance=cobol::operands::ArithmeticOperand_strategy)
@settings(max_examples=50)
def test_cobol::operands::arithmeticoperand_instantiation(instance):
    assert isinstance(instance, cobol::operands::ArithmeticOperand)

@given(instance=cobol::operands::ReplacementOperand_strategy)
@settings(max_examples=50)
def test_cobol::operands::replacementoperand_instantiation(instance):
    assert isinstance(instance, cobol::operands::ReplacementOperand)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=statements::NestedStatement_strategy)
@settings(max_examples=50)
def test_statements::nestedstatement_instantiation(instance):
    assert isinstance(instance, statements::NestedStatement)

@given(instance=statements::Perform_strategy)
@settings(max_examples=50)
def test_statements::perform_instantiation(instance):
    assert isinstance(instance, statements::Perform)

@given(instance=cobol::statements::PerformNestedStatement_strategy)
@settings(max_examples=50)
def test_cobol::statements::performnestedstatement_instantiation(instance):
    assert isinstance(instance, cobol::statements::PerformNestedStatement)

@given(instance=ArithmeticStatement_strategy)
@settings(max_examples=50)
def test_arithmeticstatement_instantiation(instance):
    assert isinstance(instance, ArithmeticStatement)

@given(instance=cobol::statements::Multiply_strategy)
@settings(max_examples=50)
def test_cobol::statements::multiply_instantiation(instance):
    assert isinstance(instance, cobol::statements::Multiply)

@given(instance=cobol::statements::Subtract_strategy)
@settings(max_examples=50)
def test_cobol::statements::subtract_instantiation(instance):
    assert isinstance(instance, cobol::statements::Subtract)

@given(instance=cobol::statements::Divide_strategy)
@settings(max_examples=50)
def test_cobol::statements::divide_instantiation(instance):
    assert isinstance(instance, cobol::statements::Divide)

@given(instance=cobol::statements::Add_strategy)
@settings(max_examples=50)
def test_cobol::statements::add_instantiation(instance):
    assert isinstance(instance, cobol::statements::Add)

@given(instance=statements::ErrorHandled_strategy)
@settings(max_examples=50)
def test_statements::errorhandled_instantiation(instance):
    assert isinstance(instance, statements::ErrorHandled)

@given(instance=statements::Statement_strategy)
@settings(max_examples=50)
def test_statements::statement_instantiation(instance):
    assert isinstance(instance, statements::Statement)

@given(instance=cobol::statements::Delete_strategy)
@settings(max_examples=50)
def test_cobol::statements::delete_instantiation(instance):
    assert isinstance(instance, cobol::statements::Delete)

@given(instance=cobol::statements::Start_strategy)
@settings(max_examples=50)
def test_cobol::statements::start_instantiation(instance):
    assert isinstance(instance, cobol::statements::Start)

@given(instance=cobol::statements::ArithmeticStatement_strategy)
@settings(max_examples=50)
def test_cobol::statements::arithmeticstatement_instantiation(instance):
    assert isinstance(instance, cobol::statements::ArithmeticStatement)

@given(instance=cobol::statements::ArithmeticStatement_strategy)
def test_cobol::statements::arithmeticstatement_corresponding_type(instance):
    assert isinstance(instance.corresponding, str)


@given(instance=cobol::statements::ArithmeticStatement_strategy)
def test_cobol::statements::arithmeticstatement_corresponding_setter(instance):
    original = instance.corresponding
    instance.corresponding = original
    assert instance.corresponding == original

@given(instance=DataItem_strategy)
@settings(max_examples=50)
def test_dataitem_instantiation(instance):
    assert isinstance(instance, DataItem)

@given(instance=cobol::dataitems::ConditionName_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::conditionname_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::ConditionName)

@given(instance=cobol::dataitems::DataName_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::dataname_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::DataName)

@given(instance=cobol::dataitems::RecordName_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::recordname_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::RecordName)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=cobol::statements::Perform_strategy)
@settings(max_examples=50)
def test_cobol::statements::perform_instantiation(instance):
    assert isinstance(instance, cobol::statements::Perform)

@given(instance=cobol::statements::Exit_strategy)
@settings(max_examples=50)
def test_cobol::statements::exit_instantiation(instance):
    assert isinstance(instance, cobol::statements::Exit)

@given(instance=cobol::statements::Exit_strategy)
def test_cobol::statements::exit_exitLabel_type(instance):
    assert isinstance(instance.exitLabel, str)


@given(instance=cobol::statements::Exit_strategy)
def test_cobol::statements::exit_exitLabel_setter(instance):
    original = instance.exitLabel
    instance.exitLabel = original
    assert instance.exitLabel == original

@given(instance=EnvironmentDivisionSection_strategy)
@settings(max_examples=50)
def test_environmentdivisionsection_instantiation(instance):
    assert isinstance(instance, EnvironmentDivisionSection)

@given(instance=cobol::sections::ConfigurationSection_strategy)
@settings(max_examples=50)
def test_cobol::sections::configurationsection_instantiation(instance):
    assert isinstance(instance, cobol::sections::ConfigurationSection)

@given(instance=cobol::sections::IOSection_strategy)
@settings(max_examples=50)
def test_cobol::sections::iosection_instantiation(instance):
    assert isinstance(instance, cobol::sections::IOSection)

@given(instance=ArithmeticOperand_strategy)
@settings(max_examples=50)
def test_arithmeticoperand_instantiation(instance):
    assert isinstance(instance, ArithmeticOperand)

@given(instance=cobol::operands::RoundedIdentifier_strategy)
@settings(max_examples=50)
def test_cobol::operands::roundedidentifier_instantiation(instance):
    assert isinstance(instance, cobol::operands::RoundedIdentifier)

@given(instance=DataDivisionSection_strategy)
@settings(max_examples=50)
def test_datadivisionsection_instantiation(instance):
    assert isinstance(instance, DataDivisionSection)

@given(instance=cobol::sections::LinkageStorageSection_strategy)
@settings(max_examples=50)
def test_cobol::sections::linkagestoragesection_instantiation(instance):
    assert isinstance(instance, cobol::sections::LinkageStorageSection)

@given(instance=cobol::sections::FileSection_strategy)
@settings(max_examples=50)
def test_cobol::sections::filesection_instantiation(instance):
    assert isinstance(instance, cobol::sections::FileSection)

@given(instance=cobol::sections::LocalStorageSection_strategy)
@settings(max_examples=50)
def test_cobol::sections::localstoragesection_instantiation(instance):
    assert isinstance(instance, cobol::sections::LocalStorageSection)

@given(instance=cobol::sections::WorkingStorageSection_strategy)
@settings(max_examples=50)
def test_cobol::sections::workingstoragesection_instantiation(instance):
    assert isinstance(instance, cobol::sections::WorkingStorageSection)

@given(instance=operands::ArithmeticOperand_strategy)
@settings(max_examples=50)
def test_operands::arithmeticoperand_instantiation(instance):
    assert isinstance(instance, operands::ArithmeticOperand)

@given(instance=arithmetics::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_arithmetics::primaryexpression_instantiation(instance):
    assert isinstance(instance, arithmetics::PrimaryExpression)

@given(instance=operands::Operand_strategy)
@settings(max_examples=50)
def test_operands::operand_instantiation(instance):
    assert isinstance(instance, operands::Operand)

@given(instance=operands::ReplacementOperand_strategy)
@settings(max_examples=50)
def test_operands::replacementoperand_instantiation(instance):
    assert isinstance(instance, operands::ReplacementOperand)

@given(instance=cobol::operands::PrimaryOperand_strategy)
@settings(max_examples=50)
def test_cobol::operands::primaryoperand_instantiation(instance):
    assert isinstance(instance, cobol::operands::PrimaryOperand)

@given(instance=sentences::StatementContainer_strategy)
@settings(max_examples=50)
def test_sentences::statementcontainer_instantiation(instance):
    assert isinstance(instance, sentences::StatementContainer)

@given(instance=Sentence_strategy)
@settings(max_examples=50)
def test_sentence_instantiation(instance):
    assert isinstance(instance, Sentence)

@given(instance=cobol::sentences::ExitProcedure_strategy)
@settings(max_examples=50)
def test_cobol::sentences::exitprocedure_instantiation(instance):
    assert isinstance(instance, cobol::sentences::ExitProcedure)

@given(instance=cobol::sentences::AlteredGoTo_strategy)
@settings(max_examples=50)
def test_cobol::sentences::alteredgoto_instantiation(instance):
    assert isinstance(instance, cobol::sentences::AlteredGoTo)

@given(instance=cobol::sentences::EntrySentence_strategy)
@settings(max_examples=50)
def test_cobol::sentences::entrysentence_instantiation(instance):
    assert isinstance(instance, cobol::sentences::EntrySentence)

@given(instance=cobol::sentences::EmptySentence_strategy)
@settings(max_examples=50)
def test_cobol::sentences::emptysentence_instantiation(instance):
    assert isinstance(instance, cobol::sentences::EmptySentence)

@given(instance=cobol::sentences::StatementContainer_strategy)
@settings(max_examples=50)
def test_cobol::sentences::statementcontainer_instantiation(instance):
    assert isinstance(instance, cobol::sentences::StatementContainer)

@given(instance=FileName_strategy)
@settings(max_examples=50)
def test_filename_instantiation(instance):
    assert isinstance(instance, FileName)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=cobol::references::ElementReference_strategy)
@settings(max_examples=50)
def test_cobol::references::elementreference_instantiation(instance):
    assert isinstance(instance, cobol::references::ElementReference)

@given(instance=ReferenceableElement_strategy)
@settings(max_examples=50)
def test_referenceableelement_instantiation(instance):
    assert isinstance(instance, ReferenceableElement)

@given(instance=cobol::specialnames::SpecialName_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::specialname_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::SpecialName)

@given(instance=cobol::parameters::Parameter_strategy)
@settings(max_examples=50)
def test_cobol::parameters::parameter_instantiation(instance):
    assert isinstance(instance, cobol::parameters::Parameter)

@given(instance=cobol::tables::AdditionalIndexName_strategy)
@settings(max_examples=50)
def test_cobol::tables::additionalindexname_instantiation(instance):
    assert isinstance(instance, cobol::tables::AdditionalIndexName)

@given(instance=cobol::references::Reference_strategy)
@settings(max_examples=50)
def test_cobol::references::reference_instantiation(instance):
    assert isinstance(instance, cobol::references::Reference)

@given(instance=cobol::paragraphs::DebuggingMode_strategy)
@settings(max_examples=50)
def test_cobol::paragraphs::debuggingmode_instantiation(instance):
    assert isinstance(instance, cobol::paragraphs::DebuggingMode)

@given(instance=SpecialNamesParagraphWater_strategy)
@settings(max_examples=50)
def test_specialnamesparagraphwater_instantiation(instance):
    assert isinstance(instance, SpecialNamesParagraphWater)

@given(instance=cobol::water::SpecialNamesClause_strategy)
@settings(max_examples=50)
def test_cobol::water::specialnamesclause_instantiation(instance):
    assert isinstance(instance, cobol::water::SpecialNamesClause)

@given(instance=cobol::water::SpecialNamesClause_strategy)
def test_cobol::water::specialnamesclause_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::water::SpecialNamesClause_strategy)
def test_cobol::water::specialnamesclause_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpecialNameStatement_strategy)
@settings(max_examples=50)
def test_specialnamestatement_instantiation(instance):
    assert isinstance(instance, SpecialNameStatement)

@given(instance=IncompleteElement_strategy)
@settings(max_examples=50)
def test_incompleteelement_instantiation(instance):
    assert isinstance(instance, IncompleteElement)

@given(instance=cobol::files::SelectStatement_strategy)
@settings(max_examples=50)
def test_cobol::files::selectstatement_instantiation(instance):
    assert isinstance(instance, cobol::files::SelectStatement)

@given(instance=cobol::files::SelectStatement_strategy)
def test_cobol::files::selectstatement_isOptional_type(instance):
    assert isinstance(instance.isOptional, bool)


@given(instance=cobol::files::SelectStatement_strategy)
def test_cobol::files::selectstatement_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=cobol::files::SelectStatement_strategy)
def test_cobol::files::selectstatement_externalFileNames_type(instance):
    assert isinstance(instance.externalFileNames, str)


@given(instance=cobol::files::SelectStatement_strategy)
def test_cobol::files::selectstatement_externalFileNames_setter(instance):
    original = instance.externalFileNames
    instance.externalFileNames = original
    assert instance.externalFileNames == original

@given(instance=cobol::statements::IOFile_strategy)
@settings(max_examples=50)
def test_cobol::statements::iofile_instantiation(instance):
    assert isinstance(instance, cobol::statements::IOFile)

@given(instance=IOFile_strategy)
@settings(max_examples=50)
def test_iofile_instantiation(instance):
    assert isinstance(instance, IOFile)

@given(instance=cobol::statements::IOFileDescriptor_strategy)
@settings(max_examples=50)
def test_cobol::statements::iofiledescriptor_instantiation(instance):
    assert isinstance(instance, cobol::statements::IOFileDescriptor)

@given(instance=cobol::statements::IOFileDescriptor_strategy)
def test_cobol::statements::iofiledescriptor_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cobol::statements::IOFileDescriptor_strategy)
def test_cobol::statements::iofiledescriptor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=IOFileDescriptor_strategy)
@settings(max_examples=50)
def test_iofiledescriptor_instantiation(instance):
    assert isinstance(instance, IOFileDescriptor)

@given(instance=cobol::statements::IOStatement_strategy)
@settings(max_examples=50)
def test_cobol::statements::iostatement_instantiation(instance):
    assert isinstance(instance, cobol::statements::IOStatement)

@given(instance=cobol::statements::KeyDescriptor_strategy)
@settings(max_examples=50)
def test_cobol::statements::keydescriptor_instantiation(instance):
    assert isinstance(instance, cobol::statements::KeyDescriptor)

@given(instance=cobol::statements::KeyDescriptor_strategy)
def test_cobol::statements::keydescriptor_order_type(instance):
    assert isinstance(instance.order, str)


@given(instance=cobol::statements::KeyDescriptor_strategy)
def test_cobol::statements::keydescriptor_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=statements::VaryingUntilCondition_strategy)
@settings(max_examples=50)
def test_statements::varyinguntilcondition_instantiation(instance):
    assert isinstance(instance, statements::VaryingUntilCondition)

@given(instance=cobol::statements::PerformUntilCondition_strategy)
@settings(max_examples=50)
def test_cobol::statements::performuntilcondition_instantiation(instance):
    assert isinstance(instance, cobol::statements::PerformUntilCondition)

@given(instance=cobol::statements::PerformUntilCondition_strategy)
def test_cobol::statements::performuntilcondition_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=cobol::statements::PerformUntilCondition_strategy)
def test_cobol::statements::performuntilcondition_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=cobol::statements::Release_strategy)
@settings(max_examples=50)
def test_cobol::statements::release_instantiation(instance):
    assert isinstance(instance, cobol::statements::Release)

@given(instance=statements::PerformFixedTimes_strategy)
@settings(max_examples=50)
def test_statements::performfixedtimes_instantiation(instance):
    assert isinstance(instance, statements::PerformFixedTimes)

@given(instance=statements::FileIOStatement_strategy)
@settings(max_examples=50)
def test_statements::fileiostatement_instantiation(instance):
    assert isinstance(instance, statements::FileIOStatement)

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

@given(instance=statements::PerformProcedure_strategy)
@settings(max_examples=50)
def test_statements::performprocedure_instantiation(instance):
    assert isinstance(instance, statements::PerformProcedure)

@given(instance=cobol::statements::PerformProcedureFixedTimes_strategy)
@settings(max_examples=50)
def test_cobol::statements::performprocedurefixedtimes_instantiation(instance):
    assert isinstance(instance, cobol::statements::PerformProcedureFixedTimes)

@given(instance=cobol::statements::FileIOStatement_strategy)
@settings(max_examples=50)
def test_cobol::statements::fileiostatement_instantiation(instance):
    assert isinstance(instance, cobol::statements::FileIOStatement)

@given(instance=statements::PerformNestedStatement_strategy)
@settings(max_examples=50)
def test_statements::performnestedstatement_instantiation(instance):
    assert isinstance(instance, statements::PerformNestedStatement)

@given(instance=cobol::statements::PerformNestedStatementFixedTimes_strategy)
@settings(max_examples=50)
def test_cobol::statements::performnestedstatementfixedtimes_instantiation(instance):
    assert isinstance(instance, cobol::statements::PerformNestedStatementFixedTimes)

@given(instance=AfterUntilCondition_strategy)
@settings(max_examples=50)
def test_afteruntilcondition_instantiation(instance):
    assert isinstance(instance, AfterUntilCondition)

@given(instance=statements::PerformUntilCondition_strategy)
@settings(max_examples=50)
def test_statements::performuntilcondition_instantiation(instance):
    assert isinstance(instance, statements::PerformUntilCondition)

@given(instance=cobol::statements::PerformNestedStatementUntilCondition_strategy)
@settings(max_examples=50)
def test_cobol::statements::performnestedstatementuntilcondition_instantiation(instance):
    assert isinstance(instance, cobol::statements::PerformNestedStatementUntilCondition)

@given(instance=cobol::statements::PerformProcedureUntilCondition_strategy)
@settings(max_examples=50)
def test_cobol::statements::performprocedureuntilcondition_instantiation(instance):
    assert isinstance(instance, cobol::statements::PerformProcedureUntilCondition)

@given(instance=cobol::statements::Read_strategy)
@settings(max_examples=50)
def test_cobol::statements::read_instantiation(instance):
    assert isinstance(instance, cobol::statements::Read)

@given(instance=TallyingIn_strategy)
@settings(max_examples=50)
def test_tallyingin_instantiation(instance):
    assert isinstance(instance, TallyingIn)

@given(instance=cobol::statements::SwitchStatus_strategy)
@settings(max_examples=50)
def test_cobol::statements::switchstatus_instantiation(instance):
    assert isinstance(instance, cobol::statements::SwitchStatus)

@given(instance=cobol::statements::SwitchStatus_strategy)
def test_cobol::statements::switchstatus_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=cobol::statements::SwitchStatus_strategy)
def test_cobol::statements::switchstatus_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Write_strategy)
@settings(max_examples=50)
def test_write_instantiation(instance):
    assert isinstance(instance, Write)

@given(instance=cobol::statements::Rewrite_strategy)
@settings(max_examples=50)
def test_cobol::statements::rewrite_instantiation(instance):
    assert isinstance(instance, cobol::statements::Rewrite)

@given(instance=MnemonicNameReference_strategy)
@settings(max_examples=50)
def test_mnemonicnamereference_instantiation(instance):
    assert isinstance(instance, MnemonicNameReference)

@given(instance=IntegerLiteral_strategy)
@settings(max_examples=50)
def test_integerliteral_instantiation(instance):
    assert isinstance(instance, IntegerLiteral)

@given(instance=cobol::statements::Write_strategy)
@settings(max_examples=50)
def test_cobol::statements::write_instantiation(instance):
    assert isinstance(instance, cobol::statements::Write)

@given(instance=cobol::statements::Unstring_strategy)
@settings(max_examples=50)
def test_cobol::statements::unstring_instantiation(instance):
    assert isinstance(instance, cobol::statements::Unstring)

@given(instance=SearchStatement_strategy)
@settings(max_examples=50)
def test_searchstatement_instantiation(instance):
    assert isinstance(instance, SearchStatement)

@given(instance=cobol::statements::BinarySearch_strategy)
@settings(max_examples=50)
def test_cobol::statements::binarysearch_instantiation(instance):
    assert isinstance(instance, cobol::statements::BinarySearch)

@given(instance=cobol::statements::SerialSearch_strategy)
@settings(max_examples=50)
def test_cobol::statements::serialsearch_instantiation(instance):
    assert isinstance(instance, cobol::statements::SerialSearch)

@given(instance=NormalEvaluateCase_strategy)
@settings(max_examples=50)
def test_normalevaluatecase_instantiation(instance):
    assert isinstance(instance, NormalEvaluateCase)

@given(instance=cobol::statements::SearchStatement_strategy)
@settings(max_examples=50)
def test_cobol::statements::searchstatement_instantiation(instance):
    assert isinstance(instance, cobol::statements::SearchStatement)

@given(instance=Replacement_strategy)
@settings(max_examples=50)
def test_replacement_instantiation(instance):
    assert isinstance(instance, Replacement)

@given(instance=cobol::strings::SpecificCharacterBySpecificCharacter_strategy)
@settings(max_examples=50)
def test_cobol::strings::specificcharacterbyspecificcharacter_instantiation(instance):
    assert isinstance(instance, cobol::strings::SpecificCharacterBySpecificCharacter)

@given(instance=cobol::strings::AnyCharacterBySpecificCharacter_strategy)
@settings(max_examples=50)
def test_cobol::strings::anycharacterbyspecificcharacter_instantiation(instance):
    assert isinstance(instance, cobol::strings::AnyCharacterBySpecificCharacter)

@given(instance=cobol::statements::Initialize_strategy)
@settings(max_examples=50)
def test_cobol::statements::initialize_instantiation(instance):
    assert isinstance(instance, cobol::statements::Initialize)

@given(instance=cobol::statements::Inspect_strategy)
@settings(max_examples=50)
def test_cobol::statements::inspect_instantiation(instance):
    assert isinstance(instance, cobol::statements::Inspect)

@given(instance=cobol::statements::Replace_strategy)
@settings(max_examples=50)
def test_cobol::statements::replace_instantiation(instance):
    assert isinstance(instance, cobol::statements::Replace)

@given(instance=cobol::statements::Replace_strategy)
def test_cobol::statements::replace_replaceSwitch_type(instance):
    assert isinstance(instance.replaceSwitch, bool)


@given(instance=cobol::statements::Replace_strategy)
def test_cobol::statements::replace_replaceSwitch_setter(instance):
    original = instance.replaceSwitch
    instance.replaceSwitch = original
    assert instance.replaceSwitch == original

@given(instance=NestedStatement_strategy)
@settings(max_examples=50)
def test_nestedstatement_instantiation(instance):
    assert isinstance(instance, NestedStatement)

@given(instance=cobol::handlers::Handler_strategy)
@settings(max_examples=50)
def test_cobol::handlers::handler_instantiation(instance):
    assert isinstance(instance, cobol::handlers::Handler)

@given(instance=cobol::statements::EvaluateCase_strategy)
@settings(max_examples=50)
def test_cobol::statements::evaluatecase_instantiation(instance):
    assert isinstance(instance, cobol::statements::EvaluateCase)

@given(instance=ExpressionList_strategy)
@settings(max_examples=50)
def test_expressionlist_instantiation(instance):
    assert isinstance(instance, ExpressionList)

@given(instance=EvaluateCase_strategy)
@settings(max_examples=50)
def test_evaluatecase_instantiation(instance):
    assert isinstance(instance, EvaluateCase)

@given(instance=cobol::statements::NormalEvaluateCase_strategy)
@settings(max_examples=50)
def test_cobol::statements::normalevaluatecase_instantiation(instance):
    assert isinstance(instance, cobol::statements::NormalEvaluateCase)

@given(instance=cobol::statements::OtherEvaluateCase_strategy)
@settings(max_examples=50)
def test_cobol::statements::otherevaluatecase_instantiation(instance):
    assert isinstance(instance, cobol::statements::OtherEvaluateCase)

@given(instance=cobol::statements::Evaluate_strategy)
@settings(max_examples=50)
def test_cobol::statements::evaluate_instantiation(instance):
    assert isinstance(instance, cobol::statements::Evaluate)

@given(instance=SplittedString_strategy)
@settings(max_examples=50)
def test_splittedstring_instantiation(instance):
    assert isinstance(instance, SplittedString)

@given(instance=SetStatement_strategy)
@settings(max_examples=50)
def test_setstatement_instantiation(instance):
    assert isinstance(instance, SetStatement)

@given(instance=cobol::statements::Set_strategy)
@settings(max_examples=50)
def test_cobol::statements::set_instantiation(instance):
    assert isinstance(instance, cobol::statements::Set)

@given(instance=cobol::statements::SetSwitches_strategy)
@settings(max_examples=50)
def test_cobol::statements::setswitches_instantiation(instance):
    assert isinstance(instance, cobol::statements::SetSwitches)

@given(instance=cobol::statements::SetStatement_strategy)
@settings(max_examples=50)
def test_cobol::statements::setstatement_instantiation(instance):
    assert isinstance(instance, cobol::statements::SetStatement)

@given(instance=FileNameReference_strategy)
@settings(max_examples=50)
def test_filenamereference_instantiation(instance):
    assert isinstance(instance, FileNameReference)

@given(instance=cobol::statements::Return_strategy)
@settings(max_examples=50)
def test_cobol::statements::return_instantiation(instance):
    assert isinstance(instance, cobol::statements::Return)

@given(instance=Handler_strategy)
@settings(max_examples=50)
def test_handler_instantiation(instance):
    assert isinstance(instance, Handler)

@given(instance=cobol::handlers::OnException_strategy)
@settings(max_examples=50)
def test_cobol::handlers::onexception_instantiation(instance):
    assert isinstance(instance, cobol::handlers::OnException)

@given(instance=cobol::handlers::AtEndOfPage_strategy)
@settings(max_examples=50)
def test_cobol::handlers::atendofpage_instantiation(instance):
    assert isinstance(instance, cobol::handlers::AtEndOfPage)

@given(instance=cobol::handlers::AtEndOfPage_strategy)
def test_cobol::handlers::atendofpage_eop_type(instance):
    assert isinstance(instance.eop, str)


@given(instance=cobol::handlers::AtEndOfPage_strategy)
def test_cobol::handlers::atendofpage_eop_setter(instance):
    original = instance.eop
    instance.eop = original
    assert instance.eop == original

@given(instance=cobol::handlers::NotErrorHandler_strategy)
@settings(max_examples=50)
def test_cobol::handlers::noterrorhandler_instantiation(instance):
    assert isinstance(instance, cobol::handlers::NotErrorHandler)

@given(instance=cobol::handlers::InvalidKey_strategy)
@settings(max_examples=50)
def test_cobol::handlers::invalidkey_instantiation(instance):
    assert isinstance(instance, cobol::handlers::InvalidKey)

@given(instance=cobol::handlers::OnOverflow_strategy)
@settings(max_examples=50)
def test_cobol::handlers::onoverflow_instantiation(instance):
    assert isinstance(instance, cobol::handlers::OnOverflow)

@given(instance=cobol::handlers::AtEnd_strategy)
@settings(max_examples=50)
def test_cobol::handlers::atend_instantiation(instance):
    assert isinstance(instance, cobol::handlers::AtEnd)

@given(instance=cobol::handlers::OnSizeError_strategy)
@settings(max_examples=50)
def test_cobol::handlers::onsizeerror_instantiation(instance):
    assert isinstance(instance, cobol::handlers::OnSizeError)

@given(instance=cobol::statements::ErrorHandled_strategy)
@settings(max_examples=50)
def test_cobol::statements::errorhandled_instantiation(instance):
    assert isinstance(instance, cobol::statements::ErrorHandled)

@given(instance=cobol::statements::Execute_strategy)
@settings(max_examples=50)
def test_cobol::statements::execute_instantiation(instance):
    assert isinstance(instance, cobol::statements::Execute)

@given(instance=cobol::statements::Execute_strategy)
def test_cobol::statements::execute_water_type(instance):
    assert isinstance(instance.water, str)


@given(instance=cobol::statements::Execute_strategy)
def test_cobol::statements::execute_water_setter(instance):
    original = instance.water
    instance.water = original
    assert instance.water == original

@given(instance=functions::Argumentable_strategy)
@settings(max_examples=50)
def test_functions::argumentable_instantiation(instance):
    assert isinstance(instance, functions::Argumentable)

@given(instance=cobol::statements::Call_strategy)
@settings(max_examples=50)
def test_cobol::statements::call_instantiation(instance):
    assert isinstance(instance, cobol::statements::Call)

@given(instance=cobol::statements::Cancel_strategy)
@settings(max_examples=50)
def test_cobol::statements::cancel_instantiation(instance):
    assert isinstance(instance, cobol::statements::Cancel)

@given(instance=statements::IOStatement_strategy)
@settings(max_examples=50)
def test_statements::iostatement_instantiation(instance):
    assert isinstance(instance, statements::IOStatement)

@given(instance=ConcatenatingStrings_strategy)
@settings(max_examples=50)
def test_concatenatingstrings_instantiation(instance):
    assert isinstance(instance, ConcatenatingStrings)

@given(instance=cobol::statements::String_strategy)
@settings(max_examples=50)
def test_cobol::statements::string_instantiation(instance):
    assert isinstance(instance, cobol::statements::String)

@given(instance=IndexNameReference_strategy)
@settings(max_examples=50)
def test_indexnamereference_instantiation(instance):
    assert isinstance(instance, IndexNameReference)

@given(instance=cobol::statements::SetIndexName_strategy)
@settings(max_examples=50)
def test_cobol::statements::setindexname_instantiation(instance):
    assert isinstance(instance, cobol::statements::SetIndexName)

@given(instance=cobol::statements::SetIndexName_strategy)
def test_cobol::statements::setindexname_adjust_type(instance):
    assert isinstance(instance.adjust, str)


@given(instance=cobol::statements::SetIndexName_strategy)
def test_cobol::statements::setindexname_adjust_setter(instance):
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

@given(instance=cobol::registers::Register_strategy)
@settings(max_examples=50)
def test_cobol::registers::register_instantiation(instance):
    assert isinstance(instance, cobol::registers::Register)

@given(instance=cobol::statements::Move_strategy)
@settings(max_examples=50)
def test_cobol::statements::move_instantiation(instance):
    assert isinstance(instance, cobol::statements::Move)

@given(instance=cobol::statements::Move_strategy)
def test_cobol::statements::move_corresponding_type(instance):
    assert isinstance(instance.corresponding, str)


@given(instance=cobol::statements::Move_strategy)
def test_cobol::statements::move_corresponding_setter(instance):
    original = instance.corresponding
    instance.corresponding = original
    assert instance.corresponding == original

@given(instance=cobol::statements::NestedStatement_strategy)
@settings(max_examples=50)
def test_cobol::statements::nestedstatement_instantiation(instance):
    assert isinstance(instance, cobol::statements::NestedStatement)

@given(instance=Jump_strategy)
@settings(max_examples=50)
def test_jump_instantiation(instance):
    assert isinstance(instance, Jump)

@given(instance=cobol::statements::Continue_strategy)
@settings(max_examples=50)
def test_cobol::statements::continue_instantiation(instance):
    assert isinstance(instance, cobol::statements::Continue)

@given(instance=cobol::statements::GoBack_strategy)
@settings(max_examples=50)
def test_cobol::statements::goback_instantiation(instance):
    assert isinstance(instance, cobol::statements::GoBack)

@given(instance=cobol::statements::GoTo_strategy)
@settings(max_examples=50)
def test_cobol::statements::goto_instantiation(instance):
    assert isinstance(instance, cobol::statements::GoTo)

@given(instance=cobol::statements::NextSentence_strategy)
@settings(max_examples=50)
def test_cobol::statements::nextsentence_instantiation(instance):
    assert isinstance(instance, cobol::statements::NextSentence)

@given(instance=cobol::statements::Jump_strategy)
@settings(max_examples=50)
def test_cobol::statements::jump_instantiation(instance):
    assert isinstance(instance, cobol::statements::Jump)

@given(instance=ProcedureRangeLabel_strategy)
@settings(max_examples=50)
def test_procedurerangelabel_instantiation(instance):
    assert isinstance(instance, ProcedureRangeLabel)

@given(instance=cobol::labels::ProcedureRange_strategy)
@settings(max_examples=50)
def test_cobol::labels::procedurerange_instantiation(instance):
    assert isinstance(instance, cobol::labels::ProcedureRange)

@given(instance=cobol::labels::ProcedureRangeChild_strategy)
@settings(max_examples=50)
def test_cobol::labels::procedurerangechild_instantiation(instance):
    assert isinstance(instance, cobol::labels::ProcedureRangeChild)

@given(instance=Perform_strategy)
@settings(max_examples=50)
def test_perform_instantiation(instance):
    assert isinstance(instance, Perform)

@given(instance=cobol::statements::PerformFixedTimes_strategy)
@settings(max_examples=50)
def test_cobol::statements::performfixedtimes_instantiation(instance):
    assert isinstance(instance, cobol::statements::PerformFixedTimes)

@given(instance=cobol::statements::PerformProcedure_strategy)
@settings(max_examples=50)
def test_cobol::statements::performprocedure_instantiation(instance):
    assert isinstance(instance, cobol::statements::PerformProcedure)

@given(instance=AssignmentExpression_strategy)
@settings(max_examples=50)
def test_assignmentexpression_instantiation(instance):
    assert isinstance(instance, AssignmentExpression)

@given(instance=cobol::statements::Compute_strategy)
@settings(max_examples=50)
def test_cobol::statements::compute_instantiation(instance):
    assert isinstance(instance, cobol::statements::Compute)

@given(instance=Environment_strategy)
@settings(max_examples=50)
def test_environment_instantiation(instance):
    assert isinstance(instance, Environment)

@given(instance=cobol::environments::SystemDevice_strategy)
@settings(max_examples=50)
def test_cobol::environments::systemdevice_instantiation(instance):
    assert isinstance(instance, cobol::environments::SystemDevice)

@given(instance=cobol::environments::UPSI_strategy)
@settings(max_examples=50)
def test_cobol::environments::upsi_instantiation(instance):
    assert isinstance(instance, cobol::environments::UPSI)

@given(instance=cobol::environments::UPSI_strategy)
def test_cobol::environments::upsi_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::environments::UPSI_strategy)
def test_cobol::environments::upsi_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::statements::Display_strategy)
@settings(max_examples=50)
def test_cobol::statements::display_instantiation(instance):
    assert isinstance(instance, cobol::statements::Display)

@given(instance=StopLabel_strategy)
@settings(max_examples=50)
def test_stoplabel_instantiation(instance):
    assert isinstance(instance, StopLabel)

@given(instance=cobol::labels::Run_strategy)
@settings(max_examples=50)
def test_cobol::labels::run_instantiation(instance):
    assert isinstance(instance, cobol::labels::Run)

@given(instance=cobol::statements::Stop_strategy)
@settings(max_examples=50)
def test_cobol::statements::stop_instantiation(instance):
    assert isinstance(instance, cobol::statements::Stop)

@given(instance=cobol::statements::Conditional_strategy)
@settings(max_examples=50)
def test_cobol::statements::conditional_instantiation(instance):
    assert isinstance(instance, cobol::statements::Conditional)

@given(instance=statements::Conditional_strategy)
@settings(max_examples=50)
def test_statements::conditional_instantiation(instance):
    assert isinstance(instance, statements::Conditional)

@given(instance=cobol::statements::Condition_strategy)
@settings(max_examples=50)
def test_cobol::statements::condition_instantiation(instance):
    assert isinstance(instance, cobol::statements::Condition)

@given(instance=NegatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_negatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, NegatedConditionalExpressionChild)

@given(instance=ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpressionChild)

@given(instance=cobol::conditions::NegatedConditionalExpression_strategy)
@settings(max_examples=50)
def test_cobol::conditions::negatedconditionalexpression_instantiation(instance):
    assert isinstance(instance, cobol::conditions::NegatedConditionalExpression)

@given(instance=LogicalOperator_strategy)
@settings(max_examples=50)
def test_logicaloperator_instantiation(instance):
    assert isinstance(instance, LogicalOperator)

@given(instance=ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpressionChild)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=cobol::conditions::ConditionalOrExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::conditions::conditionalorexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::conditions::ConditionalOrExpressionChild)

@given(instance=cobol::conditions::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_cobol::conditions::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, cobol::conditions::ConditionalOrExpression)

@given(instance=cobol::conditions::Condition_strategy)
@settings(max_examples=50)
def test_cobol::conditions::condition_instantiation(instance):
    assert isinstance(instance, cobol::conditions::Condition)

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

@given(instance=cobol::conditions::RelationalExpression_strategy)
@settings(max_examples=50)
def test_cobol::conditions::relationalexpression_instantiation(instance):
    assert isinstance(instance, cobol::conditions::RelationalExpression)

@given(instance=cobol::conditions::SimpleConditionChild_strategy)
@settings(max_examples=50)
def test_cobol::conditions::simpleconditionchild_instantiation(instance):
    assert isinstance(instance, cobol::conditions::SimpleConditionChild)

@given(instance=cobol::conditions::NegatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::conditions::negatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::conditions::NegatedConditionalExpressionChild)

@given(instance=Negate_strategy)
@settings(max_examples=50)
def test_negate_instantiation(instance):
    assert isinstance(instance, Negate)

@given(instance=cobol::commons::Commentable_strategy)
@settings(max_examples=50)
def test_cobol::commons::commentable_instantiation(instance):
    assert isinstance(instance, cobol::commons::Commentable)

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=cobol::commons::URIableElement_strategy)
@settings(max_examples=50)
def test_cobol::commons::uriableelement_instantiation(instance):
    assert isinstance(instance, cobol::commons::URIableElement)

@given(instance=cobol::commons::URIableElement_strategy)
def test_cobol::commons::uriableelement_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=cobol::commons::URIableElement_strategy)
def test_cobol::commons::uriableelement_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=cobol::commons::LabellableElement_strategy)
@settings(max_examples=50)
def test_cobol::commons::labellableelement_instantiation(instance):
    assert isinstance(instance, cobol::commons::LabellableElement)

@given(instance=cobol::commons::LabellableElement_strategy)
def test_cobol::commons::labellableelement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=cobol::commons::LabellableElement_strategy)
def test_cobol::commons::labellableelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=cobol::commons::NamedElement_strategy)
@settings(max_examples=50)
def test_cobol::commons::namedelement_instantiation(instance):
    assert isinstance(instance, cobol::commons::NamedElement)

@given(instance=cobol::commons::NamedElement_strategy)
def test_cobol::commons::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cobol::commons::NamedElement_strategy)
def test_cobol::commons::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=identifiers::IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifiers::identifierreference_instantiation(instance):
    assert isinstance(instance, identifiers::IdentifierReference)

@given(instance=cobol::references::Qualifiable_strategy)
@settings(max_examples=50)
def test_cobol::references::qualifiable_instantiation(instance):
    assert isinstance(instance, cobol::references::Qualifiable)

@given(instance=cobol::references::ConditionName_strategy)
@settings(max_examples=50)
def test_cobol::references::conditionname_instantiation(instance):
    assert isinstance(instance, cobol::references::ConditionName)

@given(instance=ElementReference_strategy)
@settings(max_examples=50)
def test_elementreference_instantiation(instance):
    assert isinstance(instance, ElementReference)

@given(instance=cobol::identifiers::Qualifier_strategy)
@settings(max_examples=50)
def test_cobol::identifiers::qualifier_instantiation(instance):
    assert isinstance(instance, cobol::identifiers::Qualifier)

@given(instance=cobol::references::AlphabetNameReference_strategy)
@settings(max_examples=50)
def test_cobol::references::alphabetnamereference_instantiation(instance):
    assert isinstance(instance, cobol::references::AlphabetNameReference)

@given(instance=IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifierreference_instantiation(instance):
    assert isinstance(instance, IdentifierReference)

@given(instance=cobol::references::IndexNameReference_strategy)
@settings(max_examples=50)
def test_cobol::references::indexnamereference_instantiation(instance):
    assert isinstance(instance, cobol::references::IndexNameReference)

@given(instance=references::IdentifierReferenceQualifier_strategy)
@settings(max_examples=50)
def test_references::identifierreferencequalifier_instantiation(instance):
    assert isinstance(instance, references::IdentifierReferenceQualifier)

@given(instance=cobol::references::DataNameReference_strategy)
@settings(max_examples=50)
def test_cobol::references::datanamereference_instantiation(instance):
    assert isinstance(instance, cobol::references::DataNameReference)

@given(instance=references::ConditionName_strategy)
@settings(max_examples=50)
def test_references::conditionname_instantiation(instance):
    assert isinstance(instance, references::ConditionName)

@given(instance=cobol::references::ConditionNameReference_strategy)
@settings(max_examples=50)
def test_cobol::references::conditionnamereference_instantiation(instance):
    assert isinstance(instance, cobol::references::ConditionNameReference)

@given(instance=references::Qualifiable_strategy)
@settings(max_examples=50)
def test_references::qualifiable_instantiation(instance):
    assert isinstance(instance, references::Qualifiable)

@given(instance=cobol::identifiers::LinageCounter_strategy)
@settings(max_examples=50)
def test_cobol::identifiers::linagecounter_instantiation(instance):
    assert isinstance(instance, cobol::identifiers::LinageCounter)

@given(instance=references::ElementReference_strategy)
@settings(max_examples=50)
def test_references::elementreference_instantiation(instance):
    assert isinstance(instance, references::ElementReference)

@given(instance=cobol::identifiers::IdentifierReference_strategy)
@settings(max_examples=50)
def test_cobol::identifiers::identifierreference_instantiation(instance):
    assert isinstance(instance, cobol::identifiers::IdentifierReference)

@given(instance=cobol::references::FileNameReference_strategy)
@settings(max_examples=50)
def test_cobol::references::filenamereference_instantiation(instance):
    assert isinstance(instance, cobol::references::FileNameReference)

@given(instance=cobol::references::MnemonicNameReference_strategy)
@settings(max_examples=50)
def test_cobol::references::mnemonicnamereference_instantiation(instance):
    assert isinstance(instance, cobol::references::MnemonicNameReference)

@given(instance=cobol::references::IdentifierReferenceQualifier_strategy)
@settings(max_examples=50)
def test_cobol::references::identifierreferencequalifier_instantiation(instance):
    assert isinstance(instance, cobol::references::IdentifierReferenceQualifier)

@given(instance=cobol::specialnames::SymbolicCharacterStatement_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::symboliccharacterstatement_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::SymbolicCharacterStatement)

@given(instance=cobol::references::SpecialNamesConditionNameReference_strategy)
@settings(max_examples=50)
def test_cobol::references::specialnamesconditionnamereference_instantiation(instance):
    assert isinstance(instance, cobol::references::SpecialNamesConditionNameReference)

@given(instance=GreaterThan_strategy)
@settings(max_examples=50)
def test_greaterthan_instantiation(instance):
    assert isinstance(instance, GreaterThan)

@given(instance=cobol::operators::GTPhrase_strategy)
@settings(max_examples=50)
def test_cobol::operators::gtphrase_instantiation(instance):
    assert isinstance(instance, cobol::operators::GTPhrase)

@given(instance=LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_lessthanorequal_instantiation(instance):
    assert isinstance(instance, LessThanOrEqual)

@given(instance=cobol::operators::LTEQSign_strategy)
@settings(max_examples=50)
def test_cobol::operators::lteqsign_instantiation(instance):
    assert isinstance(instance, cobol::operators::LTEQSign)

@given(instance=cobol::operators::LTEQPhrase_strategy)
@settings(max_examples=50)
def test_cobol::operators::lteqphrase_instantiation(instance):
    assert isinstance(instance, cobol::operators::LTEQPhrase)

@given(instance=LessThan_strategy)
@settings(max_examples=50)
def test_lessthan_instantiation(instance):
    assert isinstance(instance, LessThan)

@given(instance=cobol::operators::LTSign_strategy)
@settings(max_examples=50)
def test_cobol::operators::ltsign_instantiation(instance):
    assert isinstance(instance, cobol::operators::LTSign)

@given(instance=cobol::operators::LTPhrase_strategy)
@settings(max_examples=50)
def test_cobol::operators::ltphrase_instantiation(instance):
    assert isinstance(instance, cobol::operators::LTPhrase)

@given(instance=paragraphs::IOSectionParagraph_strategy)
@settings(max_examples=50)
def test_paragraphs::iosectionparagraph_instantiation(instance):
    assert isinstance(instance, paragraphs::IOSectionParagraph)

@given(instance=SelectStatement_strategy)
@settings(max_examples=50)
def test_selectstatement_instantiation(instance):
    assert isinstance(instance, SelectStatement)

@given(instance=IOSectionParagraph_strategy)
@settings(max_examples=50)
def test_iosectionparagraph_instantiation(instance):
    assert isinstance(instance, IOSectionParagraph)

@given(instance=cobol::paragraphs::FileControlParagraph_strategy)
@settings(max_examples=50)
def test_cobol::paragraphs::filecontrolparagraph_instantiation(instance):
    assert isinstance(instance, cobol::paragraphs::FileControlParagraph)

@given(instance=paragraphs::ConfigurationSectionParagraph_strategy)
@settings(max_examples=50)
def test_paragraphs::configurationsectionparagraph_instantiation(instance):
    assert isinstance(instance, paragraphs::ConfigurationSectionParagraph)

@given(instance=DebuggingMode_strategy)
@settings(max_examples=50)
def test_debuggingmode_instantiation(instance):
    assert isinstance(instance, DebuggingMode)

@given(instance=ConfigurationSectionParagraph_strategy)
@settings(max_examples=50)
def test_configurationsectionparagraph_instantiation(instance):
    assert isinstance(instance, ConfigurationSectionParagraph)

@given(instance=cobol::paragraphs::SpecialNamesParagraph_strategy)
@settings(max_examples=50)
def test_cobol::paragraphs::specialnamesparagraph_instantiation(instance):
    assert isinstance(instance, cobol::paragraphs::SpecialNamesParagraph)

@given(instance=cobol::paragraphs::SourceComputerParagraph_strategy)
@settings(max_examples=50)
def test_cobol::paragraphs::sourcecomputerparagraph_instantiation(instance):
    assert isinstance(instance, cobol::paragraphs::SourceComputerParagraph)

@given(instance=labels::Procedure_strategy)
@settings(max_examples=50)
def test_labels::procedure_instantiation(instance):
    assert isinstance(instance, labels::Procedure)

@given(instance=GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_greaterthanorequal_instantiation(instance):
    assert isinstance(instance, GreaterThanOrEqual)

@given(instance=cobol::operators::GTEQSign_strategy)
@settings(max_examples=50)
def test_cobol::operators::gteqsign_instantiation(instance):
    assert isinstance(instance, cobol::operators::GTEQSign)

@given(instance=cobol::operators::GTEQPhrase_strategy)
@settings(max_examples=50)
def test_cobol::operators::gteqphrase_instantiation(instance):
    assert isinstance(instance, cobol::operators::GTEQPhrase)

@given(instance=cobol::operators::GTSign_strategy)
@settings(max_examples=50)
def test_cobol::operators::gtsign_instantiation(instance):
    assert isinstance(instance, cobol::operators::GTSign)

@given(instance=operators::UnaryOperator_strategy)
@settings(max_examples=50)
def test_operators::unaryoperator_instantiation(instance):
    assert isinstance(instance, operators::UnaryOperator)

@given(instance=operators::AdditiveOperator_strategy)
@settings(max_examples=50)
def test_operators::additiveoperator_instantiation(instance):
    assert isinstance(instance, operators::AdditiveOperator)

@given(instance=cobol::operators::Subtraction_strategy)
@settings(max_examples=50)
def test_cobol::operators::subtraction_instantiation(instance):
    assert isinstance(instance, cobol::operators::Subtraction)

@given(instance=cobol::operators::Addition_strategy)
@settings(max_examples=50)
def test_cobol::operators::addition_instantiation(instance):
    assert isinstance(instance, cobol::operators::Addition)

@given(instance=cobol::operators::ConditionAnd_strategy)
@settings(max_examples=50)
def test_cobol::operators::conditionand_instantiation(instance):
    assert isinstance(instance, cobol::operators::ConditionAnd)

@given(instance=cobol::operators::ConditionOr_strategy)
@settings(max_examples=50)
def test_cobol::operators::conditionor_instantiation(instance):
    assert isinstance(instance, cobol::operators::ConditionOr)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=cobol::operators::RelationalOperator_strategy)
@settings(max_examples=50)
def test_cobol::operators::relationaloperator_instantiation(instance):
    assert isinstance(instance, cobol::operators::RelationalOperator)

@given(instance=cobol::operators::UnaryOperator_strategy)
@settings(max_examples=50)
def test_cobol::operators::unaryoperator_instantiation(instance):
    assert isinstance(instance, cobol::operators::UnaryOperator)

@given(instance=cobol::operators::LogicalOperator_strategy)
@settings(max_examples=50)
def test_cobol::operators::logicaloperator_instantiation(instance):
    assert isinstance(instance, cobol::operators::LogicalOperator)

@given(instance=cobol::operators::MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_cobol::operators::multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, cobol::operators::MultiplicativeOperator)

@given(instance=cobol::operators::SignOperator_strategy)
@settings(max_examples=50)
def test_cobol::operators::signoperator_instantiation(instance):
    assert isinstance(instance, cobol::operators::SignOperator)

@given(instance=cobol::operators::AdditiveOperator_strategy)
@settings(max_examples=50)
def test_cobol::operators::additiveoperator_instantiation(instance):
    assert isinstance(instance, cobol::operators::AdditiveOperator)

@given(instance=cobol::operators::Operator_strategy)
@settings(max_examples=50)
def test_cobol::operators::operator_instantiation(instance):
    assert isinstance(instance, cobol::operators::Operator)

@given(instance=AlphanumericLiteral_strategy)
@settings(max_examples=50)
def test_alphanumericliteral_instantiation(instance):
    assert isinstance(instance, AlphanumericLiteral)

@given(instance=cobol::literals::AlphanumericHexaDecimalLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::alphanumerichexadecimalliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::AlphanumericHexaDecimalLiteral)

@given(instance=cobol::operators::ClassOperator_strategy)
@settings(max_examples=50)
def test_cobol::operators::classoperator_instantiation(instance):
    assert isinstance(instance, cobol::operators::ClassOperator)

@given(instance=cobol::operators::Through_strategy)
@settings(max_examples=50)
def test_cobol::operators::through_instantiation(instance):
    assert isinstance(instance, cobol::operators::Through)

@given(instance=cobol::operators::Through_strategy)
def test_cobol::operators::through_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::operators::Through_strategy)
def test_cobol::operators::through_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::operators::Negate_strategy)
@settings(max_examples=50)
def test_cobol::operators::negate_instantiation(instance):
    assert isinstance(instance, cobol::operators::Negate)

@given(instance=cobol::operators::Power_strategy)
@settings(max_examples=50)
def test_cobol::operators::power_instantiation(instance):
    assert isinstance(instance, cobol::operators::Power)

@given(instance=cobol::operators::Equal_strategy)
@settings(max_examples=50)
def test_cobol::operators::equal_instantiation(instance):
    assert isinstance(instance, cobol::operators::Equal)

@given(instance=cobol::operators::Equal_strategy)
def test_cobol::operators::equal_to_type(instance):
    assert isinstance(instance.to, bool)


@given(instance=cobol::operators::Equal_strategy)
def test_cobol::operators::equal_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=cobol::operators::LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_cobol::operators::lessthanorequal_instantiation(instance):
    assert isinstance(instance, cobol::operators::LessThanOrEqual)

@given(instance=cobol::operators::LessThanOrEqual_strategy)
def test_cobol::operators::lessthanorequal_than_type(instance):
    assert isinstance(instance.than, bool)


@given(instance=cobol::operators::LessThanOrEqual_strategy)
def test_cobol::operators::lessthanorequal_than_setter(instance):
    original = instance.than
    instance.than = original
    assert instance.than == original

@given(instance=cobol::operators::LessThanOrEqual_strategy)
def test_cobol::operators::lessthanorequal_to_type(instance):
    assert isinstance(instance.to, bool)


@given(instance=cobol::operators::LessThanOrEqual_strategy)
def test_cobol::operators::lessthanorequal_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=cobol::operators::LessThan_strategy)
@settings(max_examples=50)
def test_cobol::operators::lessthan_instantiation(instance):
    assert isinstance(instance, cobol::operators::LessThan)

@given(instance=cobol::operators::LessThan_strategy)
def test_cobol::operators::lessthan_than_type(instance):
    assert isinstance(instance.than, bool)


@given(instance=cobol::operators::LessThan_strategy)
def test_cobol::operators::lessthan_than_setter(instance):
    original = instance.than
    instance.than = original
    assert instance.than == original

@given(instance=cobol::operators::GreaterThan_strategy)
@settings(max_examples=50)
def test_cobol::operators::greaterthan_instantiation(instance):
    assert isinstance(instance, cobol::operators::GreaterThan)

@given(instance=cobol::operators::GreaterThan_strategy)
def test_cobol::operators::greaterthan_than_type(instance):
    assert isinstance(instance.than, bool)


@given(instance=cobol::operators::GreaterThan_strategy)
def test_cobol::operators::greaterthan_than_setter(instance):
    original = instance.than
    instance.than = original
    assert instance.than == original

@given(instance=cobol::operators::GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_cobol::operators::greaterthanorequal_instantiation(instance):
    assert isinstance(instance, cobol::operators::GreaterThanOrEqual)

@given(instance=cobol::operators::GreaterThanOrEqual_strategy)
def test_cobol::operators::greaterthanorequal_to_type(instance):
    assert isinstance(instance.to, bool)


@given(instance=cobol::operators::GreaterThanOrEqual_strategy)
def test_cobol::operators::greaterthanorequal_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=cobol::operators::GreaterThanOrEqual_strategy)
def test_cobol::operators::greaterthanorequal_than_type(instance):
    assert isinstance(instance.than, bool)


@given(instance=cobol::operators::GreaterThanOrEqual_strategy)
def test_cobol::operators::greaterthanorequal_than_setter(instance):
    original = instance.than
    instance.than = original
    assert instance.than == original

@given(instance=DBCSLiteral_strategy)
@settings(max_examples=50)
def test_dbcsliteral_instantiation(instance):
    assert isinstance(instance, DBCSLiteral)

@given(instance=cobol::literals::NationalHexLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::nationalhexliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::NationalHexLiteral)

@given(instance=cobol::literals::NationalHexLiteral_strategy)
def test_cobol::literals::nationalhexliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=cobol::literals::NationalHexLiteral_strategy)
def test_cobol::literals::nationalhexliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::literals::NationalLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::nationalliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::NationalLiteral)

@given(instance=cobol::literals::NationalLiteral_strategy)
def test_cobol::literals::nationalliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::literals::NationalLiteral_strategy)
def test_cobol::literals::nationalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=labels::StopLabel_strategy)
@settings(max_examples=50)
def test_labels::stoplabel_instantiation(instance):
    assert isinstance(instance, labels::StopLabel)

@given(instance=ConstantLiteral_strategy)
@settings(max_examples=50)
def test_constantliteral_instantiation(instance):
    assert isinstance(instance, ConstantLiteral)

@given(instance=cobol::literals::HighValue_strategy)
@settings(max_examples=50)
def test_cobol::literals::highvalue_instantiation(instance):
    assert isinstance(instance, cobol::literals::HighValue)

@given(instance=cobol::literals::HighValue_strategy)
def test_cobol::literals::highvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::literals::HighValue_strategy)
def test_cobol::literals::highvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::literals::LowValue_strategy)
@settings(max_examples=50)
def test_cobol::literals::lowvalue_instantiation(instance):
    assert isinstance(instance, cobol::literals::LowValue)

@given(instance=cobol::literals::LowValue_strategy)
def test_cobol::literals::lowvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::literals::LowValue_strategy)
def test_cobol::literals::lowvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::literals::Quote_strategy)
@settings(max_examples=50)
def test_cobol::literals::quote_instantiation(instance):
    assert isinstance(instance, cobol::literals::Quote)

@given(instance=cobol::literals::Quote_strategy)
def test_cobol::literals::quote_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::literals::Quote_strategy)
def test_cobol::literals::quote_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::literals::Null_strategy)
@settings(max_examples=50)
def test_cobol::literals::null_instantiation(instance):
    assert isinstance(instance, cobol::literals::Null)

@given(instance=cobol::literals::Null_strategy)
def test_cobol::literals::null_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::literals::Null_strategy)
def test_cobol::literals::null_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::literals::Zero_strategy)
@settings(max_examples=50)
def test_cobol::literals::zero_instantiation(instance):
    assert isinstance(instance, cobol::literals::Zero)

@given(instance=cobol::literals::Zero_strategy)
def test_cobol::literals::zero_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::literals::Zero_strategy)
def test_cobol::literals::zero_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::literals::Space_strategy)
@settings(max_examples=50)
def test_cobol::literals::space_instantiation(instance):
    assert isinstance(instance, cobol::literals::Space)

@given(instance=cobol::literals::Space_strategy)
def test_cobol::literals::space_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::literals::Space_strategy)
def test_cobol::literals::space_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FigurativeConstantLiteral_strategy)
@settings(max_examples=50)
def test_figurativeconstantliteral_instantiation(instance):
    assert isinstance(instance, FigurativeConstantLiteral)

@given(instance=cobol::literals::ConstantLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::constantliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::ConstantLiteral)

@given(instance=cobol::literals::AllLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::allliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::AllLiteral)

@given(instance=DecimalLiteral_strategy)
@settings(max_examples=50)
def test_decimalliteral_instantiation(instance):
    assert isinstance(instance, DecimalLiteral)

@given(instance=cobol::literals::FixedDecimalLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::fixeddecimalliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::FixedDecimalLiteral)

@given(instance=cobol::literals::FloatingDecimalLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::floatingdecimalliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::FloatingDecimalLiteral)

@given(instance=NumericLiteral_strategy)
@settings(max_examples=50)
def test_numericliteral_instantiation(instance):
    assert isinstance(instance, NumericLiteral)

@given(instance=cobol::literals::DecimalLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::decimalliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::DecimalLiteral)

@given(instance=cobol::literals::DecimalLiteral_strategy)
def test_cobol::literals::decimalliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::literals::DecimalLiteral_strategy)
def test_cobol::literals::decimalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=water::IOControlParagraphWater_strategy)
@settings(max_examples=50)
def test_water::iocontrolparagraphwater_instantiation(instance):
    assert isinstance(instance, water::IOControlParagraphWater)

@given(instance=water::FileDescriptorWater_strategy)
@settings(max_examples=50)
def test_water::filedescriptorwater_instantiation(instance):
    assert isinstance(instance, water::FileDescriptorWater)

@given(instance=water::ObjectComputerParagraphWater_strategy)
@settings(max_examples=50)
def test_water::objectcomputerparagraphwater_instantiation(instance):
    assert isinstance(instance, water::ObjectComputerParagraphWater)

@given(instance=literals::NumericLiteral_strategy)
@settings(max_examples=50)
def test_literals::numericliteral_instantiation(instance):
    assert isinstance(instance, literals::NumericLiteral)

@given(instance=cobol::literals::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::integerliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::IntegerLiteral)

@given(instance=cobol::literals::IntegerLiteral_strategy)
def test_cobol::literals::integerliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=cobol::literals::IntegerLiteral_strategy)
def test_cobol::literals::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=cobol::literals::NumericLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::numericliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::NumericLiteral)

@given(instance=cobol::literals::Any_strategy)
@settings(max_examples=50)
def test_cobol::literals::any_instantiation(instance):
    assert isinstance(instance, cobol::literals::Any)

@given(instance=cobol::literals::FigurativeConstantLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::figurativeconstantliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::FigurativeConstantLiteral)

@given(instance=cobol::literals::DBCSLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::dbcsliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::DBCSLiteral)

@given(instance=cobol::literals::PseudoLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::pseudoliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::PseudoLiteral)

@given(instance=cobol::literals::PseudoLiteral_strategy)
def test_cobol::literals::pseudoliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::literals::PseudoLiteral_strategy)
def test_cobol::literals::pseudoliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::literals::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::booleanliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::BooleanLiteral)

@given(instance=cobol::literals::BooleanLiteral_strategy)
def test_cobol::literals::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=cobol::literals::BooleanLiteral_strategy)
def test_cobol::literals::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cobol::literals::Characters_strategy)
@settings(max_examples=50)
def test_cobol::literals::characters_instantiation(instance):
    assert isinstance(instance, cobol::literals::Characters)

@given(instance=cobol::literals::AlphanumericLiteral_strategy)
@settings(max_examples=50)
def test_cobol::literals::alphanumericliteral_instantiation(instance):
    assert isinstance(instance, cobol::literals::AlphanumericLiteral)

@given(instance=cobol::literals::AlphanumericLiteral_strategy)
def test_cobol::literals::alphanumericliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cobol::literals::AlphanumericLiteral_strategy)
def test_cobol::literals::alphanumericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Division_strategy)
@settings(max_examples=50)
def test_division_instantiation(instance):
    assert isinstance(instance, Division)

@given(instance=cobol::divisions::EnvironmentDivision_strategy)
@settings(max_examples=50)
def test_cobol::divisions::environmentdivision_instantiation(instance):
    assert isinstance(instance, cobol::divisions::EnvironmentDivision)

@given(instance=cobol::divisions::DataDivision_strategy)
@settings(max_examples=50)
def test_cobol::divisions::datadivision_instantiation(instance):
    assert isinstance(instance, cobol::divisions::DataDivision)

@given(instance=StatementContainer_strategy)
@settings(max_examples=50)
def test_statementcontainer_instantiation(instance):
    assert isinstance(instance, StatementContainer)

@given(instance=cobol::sentences::Sentence_strategy)
@settings(max_examples=50)
def test_cobol::sentences::sentence_instantiation(instance):
    assert isinstance(instance, cobol::sentences::Sentence)

@given(instance=cobol::sentences::ExecuteSentence_strategy)
@settings(max_examples=50)
def test_cobol::sentences::executesentence_instantiation(instance):
    assert isinstance(instance, cobol::sentences::ExecuteSentence)

@given(instance=Paragraph_strategy)
@settings(max_examples=50)
def test_paragraph_instantiation(instance):
    assert isinstance(instance, Paragraph)

@given(instance=cobol::paragraphs::IOSectionParagraph_strategy)
@settings(max_examples=50)
def test_cobol::paragraphs::iosectionparagraph_instantiation(instance):
    assert isinstance(instance, cobol::paragraphs::IOSectionParagraph)

@given(instance=cobol::paragraphs::ConfigurationSectionParagraph_strategy)
@settings(max_examples=50)
def test_cobol::paragraphs::configurationsectionparagraph_instantiation(instance):
    assert isinstance(instance, cobol::paragraphs::ConfigurationSectionParagraph)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=cobol::sections::DeclarativeSection_strategy)
@settings(max_examples=50)
def test_cobol::sections::declarativesection_instantiation(instance):
    assert isinstance(instance, cobol::sections::DeclarativeSection)

@given(instance=cobol::sections::DataDivisionSection_strategy)
@settings(max_examples=50)
def test_cobol::sections::datadivisionsection_instantiation(instance):
    assert isinstance(instance, cobol::sections::DataDivisionSection)

@given(instance=cobol::sections::EnvironmentDivisionSection_strategy)
@settings(max_examples=50)
def test_cobol::sections::environmentdivisionsection_instantiation(instance):
    assert isinstance(instance, cobol::sections::EnvironmentDivisionSection)

@given(instance=CobolRoot_strategy)
@settings(max_examples=50)
def test_cobolroot_instantiation(instance):
    assert isinstance(instance, CobolRoot)

@given(instance=cobol::containers::EmptyModel_strategy)
@settings(max_examples=50)
def test_cobol::containers::emptymodel_instantiation(instance):
    assert isinstance(instance, cobol::containers::EmptyModel)

@given(instance=cobol::containers::CobolRoot_strategy)
@settings(max_examples=50)
def test_cobol::containers::cobolroot_instantiation(instance):
    assert isinstance(instance, cobol::containers::CobolRoot)

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

@given(instance=water::InvokeStatementWater_strategy)
@settings(max_examples=50)
def test_water::invokestatementwater_instantiation(instance):
    assert isinstance(instance, water::InvokeStatementWater)

@given(instance=operands::PrimaryOperand_strategy)
@settings(max_examples=50)
def test_operands::primaryoperand_instantiation(instance):
    assert isinstance(instance, operands::PrimaryOperand)

@given(instance=water::CICSStatementWater_strategy)
@settings(max_examples=50)
def test_water::cicsstatementwater_instantiation(instance):
    assert isinstance(instance, water::CICSStatementWater)

@given(instance=water::SpecialNamesParagraphWater_strategy)
@settings(max_examples=50)
def test_water::specialnamesparagraphwater_instantiation(instance):
    assert isinstance(instance, water::SpecialNamesParagraphWater)

@given(instance=water::SelectStatementWater_strategy)
@settings(max_examples=50)
def test_water::selectstatementwater_instantiation(instance):
    assert isinstance(instance, water::SelectStatementWater)

@given(instance=cobol::identifiers::Identifier_strategy)
@settings(max_examples=50)
def test_cobol::identifiers::identifier_instantiation(instance):
    assert isinstance(instance, cobol::identifiers::Identifier)

@given(instance=cobol::literals::Literal_strategy)
@settings(max_examples=50)
def test_cobol::literals::literal_instantiation(instance):
    assert isinstance(instance, cobol::literals::Literal)

@given(instance=Declaratives_strategy)
@settings(max_examples=50)
def test_declaratives_instantiation(instance):
    assert isinstance(instance, Declaratives)

@given(instance=parameters::Parametrizable_strategy)
@settings(max_examples=50)
def test_parameters::parametrizable_instantiation(instance):
    assert isinstance(instance, parameters::Parametrizable)

@given(instance=cobol::statements::Entry_strategy)
@settings(max_examples=50)
def test_cobol::statements::entry_instantiation(instance):
    assert isinstance(instance, cobol::statements::Entry)

@given(instance=water::IncompleteElement_strategy)
@settings(max_examples=50)
def test_water::incompleteelement_instantiation(instance):
    assert isinstance(instance, water::IncompleteElement)

@given(instance=cobol::files::FileName_strategy)
@settings(max_examples=50)
def test_cobol::files::filename_instantiation(instance):
    assert isinstance(instance, cobol::files::FileName)

@given(instance=cobol::files::FileName_strategy)
def test_cobol::files::filename_fileDescriptor_type(instance):
    assert isinstance(instance.fileDescriptor, str)


@given(instance=cobol::files::FileName_strategy)
def test_cobol::files::filename_fileDescriptor_setter(instance):
    original = instance.fileDescriptor
    instance.fileDescriptor = original
    assert instance.fileDescriptor == original

@given(instance=cobol::statements::Merge_strategy)
@settings(max_examples=50)
def test_cobol::statements::merge_instantiation(instance):
    assert isinstance(instance, cobol::statements::Merge)

@given(instance=cobol::statements::Accept_strategy)
@settings(max_examples=50)
def test_cobol::statements::accept_instantiation(instance):
    assert isinstance(instance, cobol::statements::Accept)

@given(instance=cobol::dataitems::DataItem_strategy)
@settings(max_examples=50)
def test_cobol::dataitems::dataitem_instantiation(instance):
    assert isinstance(instance, cobol::dataitems::DataItem)

@given(instance=cobol::dataitems::DataItem_strategy)
def test_cobol::dataitems::dataitem_levelNumber_type(instance):
    assert isinstance(instance.levelNumber, str)


@given(instance=cobol::dataitems::DataItem_strategy)
def test_cobol::dataitems::dataitem_levelNumber_setter(instance):
    original = instance.levelNumber
    instance.levelNumber = original
    assert instance.levelNumber == original

@given(instance=cobol::paragraphs::RepositoryParagraph_strategy)
@settings(max_examples=50)
def test_cobol::paragraphs::repositoryparagraph_instantiation(instance):
    assert isinstance(instance, cobol::paragraphs::RepositoryParagraph)

@given(instance=cobol::statements::Sort_strategy)
@settings(max_examples=50)
def test_cobol::statements::sort_instantiation(instance):
    assert isinstance(instance, cobol::statements::Sort)

@given(instance=cobol::statements::Open_strategy)
@settings(max_examples=50)
def test_cobol::statements::open_instantiation(instance):
    assert isinstance(instance, cobol::statements::Open)

@given(instance=cobol::paragraphs::IOControlParagraph_strategy)
@settings(max_examples=50)
def test_cobol::paragraphs::iocontrolparagraph_instantiation(instance):
    assert isinstance(instance, cobol::paragraphs::IOControlParagraph)

@given(instance=cobol::paragraphs::ObjectComputerParagraph_strategy)
@settings(max_examples=50)
def test_cobol::paragraphs::objectcomputerparagraph_instantiation(instance):
    assert isinstance(instance, cobol::paragraphs::ObjectComputerParagraph)

@given(instance=cobol::sentences::UseSentence_strategy)
@settings(max_examples=50)
def test_cobol::sentences::usesentence_instantiation(instance):
    assert isinstance(instance, cobol::sentences::UseSentence)

@given(instance=cobol::tables::Table_strategy)
@settings(max_examples=50)
def test_cobol::tables::table_instantiation(instance):
    assert isinstance(instance, cobol::tables::Table)

@given(instance=cobol::statements::Close_strategy)
@settings(max_examples=50)
def test_cobol::statements::close_instantiation(instance):
    assert isinstance(instance, cobol::statements::Close)

@given(instance=divisions::Division_strategy)
@settings(max_examples=50)
def test_divisions::division_instantiation(instance):
    assert isinstance(instance, divisions::Division)

@given(instance=cobol::divisions::ProcedureDivision_strategy)
@settings(max_examples=50)
def test_cobol::divisions::proceduredivision_instantiation(instance):
    assert isinstance(instance, cobol::divisions::ProcedureDivision)

@given(instance=cobol::divisions::IdentificationDivision_strategy)
@settings(max_examples=50)
def test_cobol::divisions::identificationdivision_instantiation(instance):
    assert isinstance(instance, cobol::divisions::IdentificationDivision)

@given(instance=cobol::divisions::IdentificationDivision_strategy)
def test_cobol::divisions::identificationdivision_properties_type(instance):
    assert isinstance(instance.properties, str)


@given(instance=cobol::divisions::IdentificationDivision_strategy)
def test_cobol::divisions::identificationdivision_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=cobol::arithmetics::RangeExpression_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::rangeexpression_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::RangeExpression)

@given(instance=Equal_strategy)
@settings(max_examples=50)
def test_equal_instantiation(instance):
    assert isinstance(instance, Equal)

@given(instance=cobol::operators::EqualPhrase_strategy)
@settings(max_examples=50)
def test_cobol::operators::equalphrase_instantiation(instance):
    assert isinstance(instance, cobol::operators::EqualPhrase)

@given(instance=cobol::operators::EqualSign_strategy)
@settings(max_examples=50)
def test_cobol::operators::equalsign_instantiation(instance):
    assert isinstance(instance, cobol::operators::EqualSign)

@given(instance=cobol::arithmetics::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::assignmentexpression_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::AssignmentExpression)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=UnaryArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_unaryarithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, UnaryArithmeticExpressionChild)

@given(instance=cobol::arithmetics::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::primaryexpression_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::PrimaryExpression)

@given(instance=PowerArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_powerarithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, PowerArithmeticExpressionChild)

@given(instance=cobol::arithmetics::UnaryArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::unaryarithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::UnaryArithmeticExpression)

@given(instance=cobol::arithmetics::UnaryArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::unaryarithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::UnaryArithmeticExpressionChild)

@given(instance=IdentificationDivision_strategy)
@settings(max_examples=50)
def test_identificationdivision_instantiation(instance):
    assert isinstance(instance, IdentificationDivision)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=cobol::divisions::Division_strategy)
@settings(max_examples=50)
def test_cobol::divisions::division_instantiation(instance):
    assert isinstance(instance, cobol::divisions::Division)

@given(instance=cobol::references::ReferenceableElement_strategy)
@settings(max_examples=50)
def test_cobol::references::referenceableelement_instantiation(instance):
    assert isinstance(instance, cobol::references::ReferenceableElement)

@given(instance=cobol::containers::CompilationUnit_strategy)
@settings(max_examples=50)
def test_cobol::containers::compilationunit_instantiation(instance):
    assert isinstance(instance, cobol::containers::CompilationUnit)

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=commons::NamedElement_strategy)
@settings(max_examples=50)
def test_commons::namedelement_instantiation(instance):
    assert isinstance(instance, commons::NamedElement)

@given(instance=cobol::functions::FunctionCall_strategy)
@settings(max_examples=50)
def test_cobol::functions::functioncall_instantiation(instance):
    assert isinstance(instance, cobol::functions::FunctionCall)

@given(instance=cobol::sections::Section_strategy)
@settings(max_examples=50)
def test_cobol::sections::section_instantiation(instance):
    assert isinstance(instance, cobol::sections::Section)

@given(instance=cobol::sections::Section_strategy)
def test_cobol::sections::section_segmentNumber_type(instance):
    assert isinstance(instance.segmentNumber, str)


@given(instance=cobol::sections::Section_strategy)
def test_cobol::sections::section_segmentNumber_setter(instance):
    original = instance.segmentNumber
    instance.segmentNumber = original
    assert instance.segmentNumber == original

@given(instance=cobol::tables::IndexName_strategy)
@settings(max_examples=50)
def test_cobol::tables::indexname_instantiation(instance):
    assert isinstance(instance, cobol::tables::IndexName)

@given(instance=cobol::specialnames::ConditionName_strategy)
@settings(max_examples=50)
def test_cobol::specialnames::conditionname_instantiation(instance):
    assert isinstance(instance, cobol::specialnames::ConditionName)

@given(instance=cobol::paragraphs::Paragraph_strategy)
@settings(max_examples=50)
def test_cobol::paragraphs::paragraph_instantiation(instance):
    assert isinstance(instance, cobol::paragraphs::Paragraph)

@given(instance=containers::CobolRoot_strategy)
@settings(max_examples=50)
def test_containers::cobolroot_instantiation(instance):
    assert isinstance(instance, containers::CobolRoot)

@given(instance=cobol::containers::CompilationGroup_strategy)
@settings(max_examples=50)
def test_cobol::containers::compilationgroup_instantiation(instance):
    assert isinstance(instance, cobol::containers::CompilationGroup)

@given(instance=conditions::SimpleConditionChild_strategy)
@settings(max_examples=50)
def test_conditions::simpleconditionchild_instantiation(instance):
    assert isinstance(instance, conditions::SimpleConditionChild)

@given(instance=conditions::AbbreviatedRelationalExpressionChild_strategy)
@settings(max_examples=50)
def test_conditions::abbreviatedrelationalexpressionchild_instantiation(instance):
    assert isinstance(instance, conditions::AbbreviatedRelationalExpressionChild)

@given(instance=cobol::arithmetics::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::ArithmeticExpression)

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=cobol::arithmetics::NestedArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::nestedarithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::NestedArithmeticExpression)

@given(instance=cobol::arithmetics::RangeExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::rangeexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::RangeExpressionChild)

@given(instance=Through_strategy)
@settings(max_examples=50)
def test_through_instantiation(instance):
    assert isinstance(instance, Through)

@given(instance=ClassOperator_strategy)
@settings(max_examples=50)
def test_classoperator_instantiation(instance):
    assert isinstance(instance, ClassOperator)

@given(instance=cobol::operators::ClassName_strategy)
@settings(max_examples=50)
def test_cobol::operators::classname_instantiation(instance):
    assert isinstance(instance, cobol::operators::ClassName)

@given(instance=cobol::operators::DBCS_strategy)
@settings(max_examples=50)
def test_cobol::operators::dbcs_instantiation(instance):
    assert isinstance(instance, cobol::operators::DBCS)

@given(instance=cobol::operators::Kanji_strategy)
@settings(max_examples=50)
def test_cobol::operators::kanji_instantiation(instance):
    assert isinstance(instance, cobol::operators::Kanji)

@given(instance=cobol::operators::AlphabeticLower_strategy)
@settings(max_examples=50)
def test_cobol::operators::alphabeticlower_instantiation(instance):
    assert isinstance(instance, cobol::operators::AlphabeticLower)

@given(instance=cobol::operators::AlphabeticUpper_strategy)
@settings(max_examples=50)
def test_cobol::operators::alphabeticupper_instantiation(instance):
    assert isinstance(instance, cobol::operators::AlphabeticUpper)

@given(instance=cobol::operators::Numeric_strategy)
@settings(max_examples=50)
def test_cobol::operators::numeric_instantiation(instance):
    assert isinstance(instance, cobol::operators::Numeric)

@given(instance=cobol::operators::Alphabetic_strategy)
@settings(max_examples=50)
def test_cobol::operators::alphabetic_instantiation(instance):
    assert isinstance(instance, cobol::operators::Alphabetic)

@given(instance=cobol::conditions::ClassCondition_strategy)
@settings(max_examples=50)
def test_cobol::conditions::classcondition_instantiation(instance):
    assert isinstance(instance, cobol::conditions::ClassCondition)

@given(instance=SignOperator_strategy)
@settings(max_examples=50)
def test_signoperator_instantiation(instance):
    assert isinstance(instance, SignOperator)

@given(instance=cobol::operators::Negative_strategy)
@settings(max_examples=50)
def test_cobol::operators::negative_instantiation(instance):
    assert isinstance(instance, cobol::operators::Negative)

@given(instance=cobol::operators::Zero_strategy)
@settings(max_examples=50)
def test_cobol::operators::zero_instantiation(instance):
    assert isinstance(instance, cobol::operators::Zero)

@given(instance=cobol::operators::Positive_strategy)
@settings(max_examples=50)
def test_cobol::operators::positive_instantiation(instance):
    assert isinstance(instance, cobol::operators::Positive)

@given(instance=MultiplicativeOperator_strategy)
@settings(max_examples=50)
def test_multiplicativeoperator_instantiation(instance):
    assert isinstance(instance, MultiplicativeOperator)

@given(instance=cobol::operators::Multiplication_strategy)
@settings(max_examples=50)
def test_cobol::operators::multiplication_instantiation(instance):
    assert isinstance(instance, cobol::operators::Multiplication)

@given(instance=cobol::operators::Division_strategy)
@settings(max_examples=50)
def test_cobol::operators::division_instantiation(instance):
    assert isinstance(instance, cobol::operators::Division)

@given(instance=MultiplicativeArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_multiplicativearithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, MultiplicativeArithmeticExpressionChild)

@given(instance=cobol::arithmetics::PowerArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::powerarithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::PowerArithmeticExpressionChild)

@given(instance=cobol::arithmetics::PowerArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::powerarithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::PowerArithmeticExpression)

@given(instance=AdditiveOperator_strategy)
@settings(max_examples=50)
def test_additiveoperator_instantiation(instance):
    assert isinstance(instance, AdditiveOperator)

@given(instance=AdditiveArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_additivearithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, AdditiveArithmeticExpressionChild)

@given(instance=cobol::arithmetics::MultiplicativeArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::multiplicativearithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::MultiplicativeArithmeticExpressionChild)

@given(instance=cobol::arithmetics::MultiplicativeArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::multiplicativearithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::MultiplicativeArithmeticExpression)

@given(instance=RangeExpressionChild_strategy)
@settings(max_examples=50)
def test_rangeexpressionchild_instantiation(instance):
    assert isinstance(instance, RangeExpressionChild)

@given(instance=cobol::arithmetics::AdditiveArithmeticExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::additivearithmeticexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::AdditiveArithmeticExpressionChild)

@given(instance=cobol::arithmetics::AdditiveArithmeticExpression_strategy)
@settings(max_examples=50)
def test_cobol::arithmetics::additivearithmeticexpression_instantiation(instance):
    assert isinstance(instance, cobol::arithmetics::AdditiveArithmeticExpression)

@given(instance=cobol::conditions::NestedCondition_strategy)
@settings(max_examples=50)
def test_cobol::conditions::nestedcondition_instantiation(instance):
    assert isinstance(instance, cobol::conditions::NestedCondition)

@given(instance=NegatedAbbreviatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_negatedabbreviatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, NegatedAbbreviatedConditionalExpressionChild)

@given(instance=cobol::conditions::AbbreviatedRelationalExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::conditions::abbreviatedrelationalexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::conditions::AbbreviatedRelationalExpressionChild)

@given(instance=cobol::conditions::AbbreviatedRelationalExpression_strategy)
@settings(max_examples=50)
def test_cobol::conditions::abbreviatedrelationalexpression_instantiation(instance):
    assert isinstance(instance, cobol::conditions::AbbreviatedRelationalExpression)

@given(instance=cobol::conditions::AbbreviatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::conditions::abbreviatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::conditions::AbbreviatedConditionalExpressionChild)

@given(instance=AbbreviatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_abbreviatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, AbbreviatedConditionalExpressionChild)

@given(instance=cobol::conditions::NegatedAbbreviatedConditionalExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::conditions::negatedabbreviatedconditionalexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::conditions::NegatedAbbreviatedConditionalExpressionChild)

@given(instance=cobol::conditions::NegatedAbbreviatedConditionalExpression_strategy)
@settings(max_examples=50)
def test_cobol::conditions::negatedabbreviatedconditionalexpression_instantiation(instance):
    assert isinstance(instance, cobol::conditions::NegatedAbbreviatedConditionalExpression)

@given(instance=cobol::conditions::AbbreviatedConditionalExpression_strategy)
@settings(max_examples=50)
def test_cobol::conditions::abbreviatedconditionalexpression_instantiation(instance):
    assert isinstance(instance, cobol::conditions::AbbreviatedConditionalExpression)

@given(instance=cobol::conditions::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_cobol::conditions::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, cobol::conditions::ConditionalAndExpression)

@given(instance=cobol::conditions::ConditionalAndExpressionChild_strategy)
@settings(max_examples=50)
def test_cobol::conditions::conditionalandexpressionchild_instantiation(instance):
    assert isinstance(instance, cobol::conditions::ConditionalAndExpressionChild)

@given(instance=cobol::conditions::ExpressionList_strategy)
@settings(max_examples=50)
def test_cobol::conditions::expressionlist_instantiation(instance):
    assert isinstance(instance, cobol::conditions::ExpressionList)

@given(instance=cobol::conditions::SignCondition_strategy)
@settings(max_examples=50)
def test_cobol::conditions::signcondition_instantiation(instance):
    assert isinstance(instance, cobol::conditions::SignCondition)

@given(instance=AbbreviatedRelationalExpressionChild_strategy)
@settings(max_examples=50)
def test_abbreviatedrelationalexpressionchild_instantiation(instance):
    assert isinstance(instance, AbbreviatedRelationalExpressionChild)

@given(instance=cobol::conditions::NestedAbbreviatedConditionalExpression_strategy)
@settings(max_examples=50)
def test_cobol::conditions::nestedabbreviatedconditionalexpression_instantiation(instance):
    assert isinstance(instance, cobol::conditions::NestedAbbreviatedConditionalExpression)
