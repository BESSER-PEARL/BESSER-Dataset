import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BlankNode,
    sparql::ANON,
    sparql::BLANK::NODE::LABEL,
    AscOrDecs,
    sparql::DescendingLiteral,
    sparql::AscendingLiteral,
    StringLiteral,
    sparql::STRING::LITERAL2,
    sparql::STRING::LITERAL::LONG2,
    sparql::STRING::LITERAL::LONG1,
    sparql::STRING::LITERAL1,
    sparql::VAR2,
    sparql::VAR1,
    BooleanLiteral,
    sparql::FalseBooleanLiteralNE,
    sparql::TrueBooleanLiteralNE,
    PrefixedName,
    sparql::StringLiteral,
    LANGTAGOrIRIrefNE,
    sparql::LANGTAG,
    sparql::UpIRIrefNE,
    AdditionalUnaryExpressionNE,
    sparql::TimesAdditionalUnaryExpressionNE,
    NumericLiteral,
    sparql::NumericLiteralUnsigned,
    sparql::DOUBLE,
    sparql::DECIMAL,
    AdditionalMultiplicativeExpressionNE,
    sparql::NumericLiteralNegative,
    sparql::NumericLiteralPositive,
    sparql::MinusMultiplicativeExpressionNE,
    sparql::PlusMultiplicativeExpressionNE,
    UnaryExpression,
    sparql::PlusPrimaryExpressionNE,
    sparql::PrimaryExpression,
    sparql::MinusPrimaryExpressionNE,
    sparql::NotPrimaryExpressionNE,
    sparql::DividedByAdditionalUnaryExpressionNE,
    AdditionalNumericExpressionNE,
    sparql::BiggerOrEqualNumericExpressionNE,
    sparql::NotEqualNumericExpressionNE,
    sparql::BiggerNumericExpressionNE,
    sparql::SmallerOrEqualNumericExpressionNE,
    sparql::SmallerNumericExpressionNE,
    sparql::EqualsNumericExpressionNE,
    ArgList,
    sparql::ArgListExpressionNE,
    sparql::ArgListNILNE,
    sparql::AscOrDecs,
    OrderCondition,
    sparql::OrderConditionLeftNE,
    Query,
    sparql::DescribeQuery,
    sparql::ConstructQuery,
    sparql::AskQuery,
    sparql::SelectQuery,
    sparql::LocatedElement,
    LocatedElement,
    sparql::UnaryExpression,
    sparql::WS,
    sparql::AdditiveExpression,
    sparql::AdditionalUnaryExpressionNE,
    sparql::Prologue,
    sparql::AdditionalValueLogicalNE,
    sparql::LimitOffsetClauses,
    sparql::MultiplicativeExpression,
    sparql::WhereClause,
    sparql::RelationalExpression,
    sparql::SolutionsDisplayNE,
    sparql::AdditionalNumericExpressionNE,
    sparql::Query,
    sparql::ConstructTemplate,
    sparql::NumericExpression,
    sparql::PN::PREFIX,
    sparql::OrderCondition,
    sparql::SolutionModifier,
    sparql::AdditionalConditionalAndExpressionNE,
    sparql::DatasetClause,
    sparql::BaseDecl,
    sparql::VARNAME,
    sparql::AdditionalMultiplicativeExpressionNE,
    sparql::PN::LOCAL,
    sparql::ValueLogical,
    sparql::LANGTAGOrIRIrefNE,
    sparql::ConditionalAndExpression,
    sparql::PrefixDecl,
    sparql::SparqlQueries,
    sparql::ConditionalOrExpression,
    sparql::ArgList,
    sparql::AdditionalExpressionNE,
    BuiltInCall,
    sparql::IsURIBuiltInCallNE,
    sparql::IsLiteralBuiltInCallNE,
    sparql::RegexExpression,
    sparql::DatatypeBuiltInCallNE,
    sparql::LangmatchesBuiltInCallNE,
    sparql::IsIRIBuiltInCallNE,
    sparql::IsBlankBuiltInCallNE,
    sparql::LangBuiltInCallNE,
    sparql::StrBuiltInCallNE,
    sparql::Expression,
    Constraint,
    sparql::FunctionCall,
    sparql::SameTermBuiltInCallNE,
    sparql::BoundBuiltInCallNE,
    TriplesNode,
    sparql::BlankNodePropertyList,
    sparql::Collection,
    sparql::GraphNode,
    sparql::Object,
    sparql::ObjectList,
    sparql::Verb,
    GraphNode,
    sparql::PropertyListNotEmpty,
    sparql::PatternOrFilterNE,
    sparql::VarOrTerm,
    TriplesSameSubject,
    sparql::TriplesSameSubjectLeftNE,
    sparql::AdditionalGGPElement,
    sparql::TriplesBlock,
    GraphPatternNotTriples,
    sparql::GraphGraphPattern,
    sparql::GroupOrUnionGraphPattern,
    sparql::OptionalGraphPattern,
    PatternOrFilterNE,
    sparql::Filter,
    sparql::GraphPatternNotTriples,
    sparql::TriplesNode,
    sparql::TriplesSameSubjectRightNE,
    IRIreference,
    sparql::PrefixedName,
    SourceSelector,
    GraphTerm,
    sparql::BlankNode,
    sparql::NotInList,
    sparql::GroupGraphPattern,
    sparql::WhereLiteral,
    sparql::SourceSelector,
    GraphClauseNE,
    sparql::NamedGraphClause,
    sparql::DefaultGraphClause,
    sparql::GraphClauseNE,
    OrderConditionRightNE,
    sparql::Constraint,
    VarOrTerm,
    sparql::GraphTerm,
    PrimaryExpression,
    sparql::RDFLiteral,
    sparql::BuiltInCall,
    sparql::BrackettedExpression,
    sparql::NumericLiteral,
    sparql::BooleanLiteral,
    sparql::IRIrefOrFunction,
    VarOrIRIref,
    sparql::PNAME::LN,
    sparql::IRIreference,
    sparql::IRI::REF,
    sparql::Var,
    sparql::PNAME::NS,
    Verb,
    sparql::VerbANE,
    sparql::VarOrIRIref,
    VariablesNE,
    sparql::SomeVariablesNE,
    sparql::AllVariablesNE,
    sparql::VariablesNE,
    SolutionsDisplayNE,
    sparql::ReducedNE,
    sparql::DistinctNE,
    sparql::INTEGER,
    sparql::OrderClause,
    sparql::TriplesSameSubject,
    sparql::OffsetClause,
    sparql::LimitClause,
    LimitOffsetClauses,
    sparql::LimitOffsetClausesRightNE,
    sparql::LimitOffsetClausesLeftNE,
    sparql::OrderConditionRightNE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_blanknode_is_not_abstract():
    assert not inspect.isabstract(BlankNode)


def test_blanknode_constructor_exists():
    assert callable(BlankNode.__init__)


def test_blanknode_constructor_args():
    sig = inspect.signature(BlankNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql::anon_is_not_abstract():
    assert not inspect.isabstract(sparql::ANON)


def test_sparql::anon_constructor_exists():
    assert callable(sparql::ANON.__init__)


def test_sparql::anon_constructor_args():
    sig = inspect.signature(sparql::ANON.__init__)
    params = list(sig.parameters.keys())



def test_sparql::blank::node::label_is_not_abstract():
    assert not inspect.isabstract(sparql::BLANK::NODE::LABEL)


def test_sparql::blank::node::label_constructor_exists():
    assert callable(sparql::BLANK::NODE::LABEL.__init__)


def test_sparql::blank::node::label_constructor_args():
    sig = inspect.signature(sparql::BLANK::NODE::LABEL.__init__)
    params = list(sig.parameters.keys())
    assert "pn_local" in params, "Missing parameter 'pn_local'"

def test_sparql::blank::node::label_has_pn_local():
    assert hasattr(sparql::BLANK::NODE::LABEL, "pn_local")
    descriptor = None
    for klass in sparql::BLANK::NODE::LABEL.__mro__:
        if "pn_local" in klass.__dict__:
            descriptor = klass.__dict__["pn_local"]
            break
    assert isinstance(descriptor, property)



def test_ascordecs_is_not_abstract():
    assert not inspect.isabstract(AscOrDecs)


def test_ascordecs_constructor_exists():
    assert callable(AscOrDecs.__init__)


def test_ascordecs_constructor_args():
    sig = inspect.signature(AscOrDecs.__init__)
    params = list(sig.parameters.keys())



def test_sparql::descendingliteral_is_not_abstract():
    assert not inspect.isabstract(sparql::DescendingLiteral)


def test_sparql::descendingliteral_constructor_exists():
    assert callable(sparql::DescendingLiteral.__init__)


def test_sparql::descendingliteral_constructor_args():
    sig = inspect.signature(sparql::DescendingLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql::ascendingliteral_is_not_abstract():
    assert not inspect.isabstract(sparql::AscendingLiteral)


def test_sparql::ascendingliteral_constructor_exists():
    assert callable(sparql::AscendingLiteral.__init__)


def test_sparql::ascendingliteral_constructor_args():
    sig = inspect.signature(sparql::AscendingLiteral.__init__)
    params = list(sig.parameters.keys())



def test_stringliteral_is_not_abstract():
    assert not inspect.isabstract(StringLiteral)


def test_stringliteral_constructor_exists():
    assert callable(StringLiteral.__init__)


def test_stringliteral_constructor_args():
    sig = inspect.signature(StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql::string::literal2_is_not_abstract():
    assert not inspect.isabstract(sparql::STRING::LITERAL2)


def test_sparql::string::literal2_constructor_exists():
    assert callable(sparql::STRING::LITERAL2.__init__)


def test_sparql::string::literal2_constructor_args():
    sig = inspect.signature(sparql::STRING::LITERAL2.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_sparql::string::literal2_has_string():
    assert hasattr(sparql::STRING::LITERAL2, "string")
    descriptor = None
    for klass in sparql::STRING::LITERAL2.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_sparql::string::literal::long2_is_not_abstract():
    assert not inspect.isabstract(sparql::STRING::LITERAL::LONG2)


def test_sparql::string::literal::long2_constructor_exists():
    assert callable(sparql::STRING::LITERAL::LONG2.__init__)


def test_sparql::string::literal::long2_constructor_args():
    sig = inspect.signature(sparql::STRING::LITERAL::LONG2.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_sparql::string::literal::long2_has_string():
    assert hasattr(sparql::STRING::LITERAL::LONG2, "string")
    descriptor = None
    for klass in sparql::STRING::LITERAL::LONG2.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_sparql::string::literal::long1_is_not_abstract():
    assert not inspect.isabstract(sparql::STRING::LITERAL::LONG1)


def test_sparql::string::literal::long1_constructor_exists():
    assert callable(sparql::STRING::LITERAL::LONG1.__init__)


def test_sparql::string::literal::long1_constructor_args():
    sig = inspect.signature(sparql::STRING::LITERAL::LONG1.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_sparql::string::literal::long1_has_string():
    assert hasattr(sparql::STRING::LITERAL::LONG1, "string")
    descriptor = None
    for klass in sparql::STRING::LITERAL::LONG1.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_sparql::string::literal1_is_not_abstract():
    assert not inspect.isabstract(sparql::STRING::LITERAL1)


def test_sparql::string::literal1_constructor_exists():
    assert callable(sparql::STRING::LITERAL1.__init__)


def test_sparql::string::literal1_constructor_args():
    sig = inspect.signature(sparql::STRING::LITERAL1.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_sparql::string::literal1_has_string():
    assert hasattr(sparql::STRING::LITERAL1, "string")
    descriptor = None
    for klass in sparql::STRING::LITERAL1.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_sparql::var2_is_not_abstract():
    assert not inspect.isabstract(sparql::VAR2)


def test_sparql::var2_constructor_exists():
    assert callable(sparql::VAR2.__init__)


def test_sparql::var2_constructor_args():
    sig = inspect.signature(sparql::VAR2.__init__)
    params = list(sig.parameters.keys())



def test_sparql::var1_is_not_abstract():
    assert not inspect.isabstract(sparql::VAR1)


def test_sparql::var1_constructor_exists():
    assert callable(sparql::VAR1.__init__)


def test_sparql::var1_constructor_args():
    sig = inspect.signature(sparql::VAR1.__init__)
    params = list(sig.parameters.keys())



def test_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteral)


def test_booleanliteral_constructor_exists():
    assert callable(BooleanLiteral.__init__)


def test_booleanliteral_constructor_args():
    sig = inspect.signature(BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql::falsebooleanliteralne_is_not_abstract():
    assert not inspect.isabstract(sparql::FalseBooleanLiteralNE)


def test_sparql::falsebooleanliteralne_constructor_exists():
    assert callable(sparql::FalseBooleanLiteralNE.__init__)


def test_sparql::falsebooleanliteralne_constructor_args():
    sig = inspect.signature(sparql::FalseBooleanLiteralNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::truebooleanliteralne_is_not_abstract():
    assert not inspect.isabstract(sparql::TrueBooleanLiteralNE)


def test_sparql::truebooleanliteralne_constructor_exists():
    assert callable(sparql::TrueBooleanLiteralNE.__init__)


def test_sparql::truebooleanliteralne_constructor_args():
    sig = inspect.signature(sparql::TrueBooleanLiteralNE.__init__)
    params = list(sig.parameters.keys())



def test_prefixedname_is_not_abstract():
    assert not inspect.isabstract(PrefixedName)


def test_prefixedname_constructor_exists():
    assert callable(PrefixedName.__init__)


def test_prefixedname_constructor_args():
    sig = inspect.signature(PrefixedName.__init__)
    params = list(sig.parameters.keys())



def test_sparql::stringliteral_is_not_abstract():
    assert not inspect.isabstract(sparql::StringLiteral)


def test_sparql::stringliteral_constructor_exists():
    assert callable(sparql::StringLiteral.__init__)


def test_sparql::stringliteral_constructor_args():
    sig = inspect.signature(sparql::StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_langtagoririrefne_is_not_abstract():
    assert not inspect.isabstract(LANGTAGOrIRIrefNE)


def test_langtagoririrefne_constructor_exists():
    assert callable(LANGTAGOrIRIrefNE.__init__)


def test_langtagoririrefne_constructor_args():
    sig = inspect.signature(LANGTAGOrIRIrefNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::langtag_is_not_abstract():
    assert not inspect.isabstract(sparql::LANGTAG)


def test_sparql::langtag_constructor_exists():
    assert callable(sparql::LANGTAG.__init__)


def test_sparql::langtag_constructor_args():
    sig = inspect.signature(sparql::LANGTAG.__init__)
    params = list(sig.parameters.keys())
    assert "langtag" in params, "Missing parameter 'langtag'"

def test_sparql::langtag_has_langtag():
    assert hasattr(sparql::LANGTAG, "langtag")
    descriptor = None
    for klass in sparql::LANGTAG.__mro__:
        if "langtag" in klass.__dict__:
            descriptor = klass.__dict__["langtag"]
            break
    assert isinstance(descriptor, property)



def test_sparql::upirirefne_is_not_abstract():
    assert not inspect.isabstract(sparql::UpIRIrefNE)


def test_sparql::upirirefne_constructor_exists():
    assert callable(sparql::UpIRIrefNE.__init__)


def test_sparql::upirirefne_constructor_args():
    sig = inspect.signature(sparql::UpIRIrefNE.__init__)
    params = list(sig.parameters.keys())



def test_additionalunaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(AdditionalUnaryExpressionNE)


def test_additionalunaryexpressionne_constructor_exists():
    assert callable(AdditionalUnaryExpressionNE.__init__)


def test_additionalunaryexpressionne_constructor_args():
    sig = inspect.signature(AdditionalUnaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::timesadditionalunaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::TimesAdditionalUnaryExpressionNE)


def test_sparql::timesadditionalunaryexpressionne_constructor_exists():
    assert callable(sparql::TimesAdditionalUnaryExpressionNE.__init__)


def test_sparql::timesadditionalunaryexpressionne_constructor_args():
    sig = inspect.signature(sparql::TimesAdditionalUnaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_numericliteral_is_not_abstract():
    assert not inspect.isabstract(NumericLiteral)


def test_numericliteral_constructor_exists():
    assert callable(NumericLiteral.__init__)


def test_numericliteral_constructor_args():
    sig = inspect.signature(NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql::numericliteralunsigned_is_not_abstract():
    assert not inspect.isabstract(sparql::NumericLiteralUnsigned)


def test_sparql::numericliteralunsigned_constructor_exists():
    assert callable(sparql::NumericLiteralUnsigned.__init__)


def test_sparql::numericliteralunsigned_constructor_args():
    sig = inspect.signature(sparql::NumericLiteralUnsigned.__init__)
    params = list(sig.parameters.keys())



def test_sparql::double_is_not_abstract():
    assert not inspect.isabstract(sparql::DOUBLE)


def test_sparql::double_constructor_exists():
    assert callable(sparql::DOUBLE.__init__)


def test_sparql::double_constructor_args():
    sig = inspect.signature(sparql::DOUBLE.__init__)
    params = list(sig.parameters.keys())
    assert "double" in params, "Missing parameter 'double'"

def test_sparql::double_has_double():
    assert hasattr(sparql::DOUBLE, "double")
    descriptor = None
    for klass in sparql::DOUBLE.__mro__:
        if "double" in klass.__dict__:
            descriptor = klass.__dict__["double"]
            break
    assert isinstance(descriptor, property)



def test_sparql::decimal_is_not_abstract():
    assert not inspect.isabstract(sparql::DECIMAL)


def test_sparql::decimal_constructor_exists():
    assert callable(sparql::DECIMAL.__init__)


def test_sparql::decimal_constructor_args():
    sig = inspect.signature(sparql::DECIMAL.__init__)
    params = list(sig.parameters.keys())
    assert "decimal" in params, "Missing parameter 'decimal'"

def test_sparql::decimal_has_decimal():
    assert hasattr(sparql::DECIMAL, "decimal")
    descriptor = None
    for klass in sparql::DECIMAL.__mro__:
        if "decimal" in klass.__dict__:
            descriptor = klass.__dict__["decimal"]
            break
    assert isinstance(descriptor, property)



def test_additionalmultiplicativeexpressionne_is_not_abstract():
    assert not inspect.isabstract(AdditionalMultiplicativeExpressionNE)


def test_additionalmultiplicativeexpressionne_constructor_exists():
    assert callable(AdditionalMultiplicativeExpressionNE.__init__)


def test_additionalmultiplicativeexpressionne_constructor_args():
    sig = inspect.signature(AdditionalMultiplicativeExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::numericliteralnegative_is_not_abstract():
    assert not inspect.isabstract(sparql::NumericLiteralNegative)


def test_sparql::numericliteralnegative_constructor_exists():
    assert callable(sparql::NumericLiteralNegative.__init__)


def test_sparql::numericliteralnegative_constructor_args():
    sig = inspect.signature(sparql::NumericLiteralNegative.__init__)
    params = list(sig.parameters.keys())



def test_sparql::numericliteralpositive_is_not_abstract():
    assert not inspect.isabstract(sparql::NumericLiteralPositive)


def test_sparql::numericliteralpositive_constructor_exists():
    assert callable(sparql::NumericLiteralPositive.__init__)


def test_sparql::numericliteralpositive_constructor_args():
    sig = inspect.signature(sparql::NumericLiteralPositive.__init__)
    params = list(sig.parameters.keys())



def test_sparql::minusmultiplicativeexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::MinusMultiplicativeExpressionNE)


def test_sparql::minusmultiplicativeexpressionne_constructor_exists():
    assert callable(sparql::MinusMultiplicativeExpressionNE.__init__)


def test_sparql::minusmultiplicativeexpressionne_constructor_args():
    sig = inspect.signature(sparql::MinusMultiplicativeExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::plusmultiplicativeexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::PlusMultiplicativeExpressionNE)


def test_sparql::plusmultiplicativeexpressionne_constructor_exists():
    assert callable(sparql::PlusMultiplicativeExpressionNE.__init__)


def test_sparql::plusmultiplicativeexpressionne_constructor_args():
    sig = inspect.signature(sparql::PlusMultiplicativeExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::plusprimaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::PlusPrimaryExpressionNE)


def test_sparql::plusprimaryexpressionne_constructor_exists():
    assert callable(sparql::PlusPrimaryExpressionNE.__init__)


def test_sparql::plusprimaryexpressionne_constructor_args():
    sig = inspect.signature(sparql::PlusPrimaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(sparql::PrimaryExpression)


def test_sparql::primaryexpression_constructor_exists():
    assert callable(sparql::PrimaryExpression.__init__)


def test_sparql::primaryexpression_constructor_args():
    sig = inspect.signature(sparql::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::minusprimaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::MinusPrimaryExpressionNE)


def test_sparql::minusprimaryexpressionne_constructor_exists():
    assert callable(sparql::MinusPrimaryExpressionNE.__init__)


def test_sparql::minusprimaryexpressionne_constructor_args():
    sig = inspect.signature(sparql::MinusPrimaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::notprimaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::NotPrimaryExpressionNE)


def test_sparql::notprimaryexpressionne_constructor_exists():
    assert callable(sparql::NotPrimaryExpressionNE.__init__)


def test_sparql::notprimaryexpressionne_constructor_args():
    sig = inspect.signature(sparql::NotPrimaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::dividedbyadditionalunaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::DividedByAdditionalUnaryExpressionNE)


def test_sparql::dividedbyadditionalunaryexpressionne_constructor_exists():
    assert callable(sparql::DividedByAdditionalUnaryExpressionNE.__init__)


def test_sparql::dividedbyadditionalunaryexpressionne_constructor_args():
    sig = inspect.signature(sparql::DividedByAdditionalUnaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_additionalnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(AdditionalNumericExpressionNE)


def test_additionalnumericexpressionne_constructor_exists():
    assert callable(AdditionalNumericExpressionNE.__init__)


def test_additionalnumericexpressionne_constructor_args():
    sig = inspect.signature(AdditionalNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::biggerorequalnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::BiggerOrEqualNumericExpressionNE)


def test_sparql::biggerorequalnumericexpressionne_constructor_exists():
    assert callable(sparql::BiggerOrEqualNumericExpressionNE.__init__)


def test_sparql::biggerorequalnumericexpressionne_constructor_args():
    sig = inspect.signature(sparql::BiggerOrEqualNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::notequalnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::NotEqualNumericExpressionNE)


def test_sparql::notequalnumericexpressionne_constructor_exists():
    assert callable(sparql::NotEqualNumericExpressionNE.__init__)


def test_sparql::notequalnumericexpressionne_constructor_args():
    sig = inspect.signature(sparql::NotEqualNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::biggernumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::BiggerNumericExpressionNE)


def test_sparql::biggernumericexpressionne_constructor_exists():
    assert callable(sparql::BiggerNumericExpressionNE.__init__)


def test_sparql::biggernumericexpressionne_constructor_args():
    sig = inspect.signature(sparql::BiggerNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::smallerorequalnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::SmallerOrEqualNumericExpressionNE)


def test_sparql::smallerorequalnumericexpressionne_constructor_exists():
    assert callable(sparql::SmallerOrEqualNumericExpressionNE.__init__)


def test_sparql::smallerorequalnumericexpressionne_constructor_args():
    sig = inspect.signature(sparql::SmallerOrEqualNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::smallernumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::SmallerNumericExpressionNE)


def test_sparql::smallernumericexpressionne_constructor_exists():
    assert callable(sparql::SmallerNumericExpressionNE.__init__)


def test_sparql::smallernumericexpressionne_constructor_args():
    sig = inspect.signature(sparql::SmallerNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::equalsnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::EqualsNumericExpressionNE)


def test_sparql::equalsnumericexpressionne_constructor_exists():
    assert callable(sparql::EqualsNumericExpressionNE.__init__)


def test_sparql::equalsnumericexpressionne_constructor_args():
    sig = inspect.signature(sparql::EqualsNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_arglist_is_not_abstract():
    assert not inspect.isabstract(ArgList)


def test_arglist_constructor_exists():
    assert callable(ArgList.__init__)


def test_arglist_constructor_args():
    sig = inspect.signature(ArgList.__init__)
    params = list(sig.parameters.keys())



def test_sparql::arglistexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::ArgListExpressionNE)


def test_sparql::arglistexpressionne_constructor_exists():
    assert callable(sparql::ArgListExpressionNE.__init__)


def test_sparql::arglistexpressionne_constructor_args():
    sig = inspect.signature(sparql::ArgListExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::arglistnilne_is_not_abstract():
    assert not inspect.isabstract(sparql::ArgListNILNE)


def test_sparql::arglistnilne_constructor_exists():
    assert callable(sparql::ArgListNILNE.__init__)


def test_sparql::arglistnilne_constructor_args():
    sig = inspect.signature(sparql::ArgListNILNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::ascordecs_is_not_abstract():
    assert not inspect.isabstract(sparql::AscOrDecs)


def test_sparql::ascordecs_constructor_exists():
    assert callable(sparql::AscOrDecs.__init__)


def test_sparql::ascordecs_constructor_args():
    sig = inspect.signature(sparql::AscOrDecs.__init__)
    params = list(sig.parameters.keys())



def test_ordercondition_is_not_abstract():
    assert not inspect.isabstract(OrderCondition)


def test_ordercondition_constructor_exists():
    assert callable(OrderCondition.__init__)


def test_ordercondition_constructor_args():
    sig = inspect.signature(OrderCondition.__init__)
    params = list(sig.parameters.keys())



def test_sparql::orderconditionleftne_is_not_abstract():
    assert not inspect.isabstract(sparql::OrderConditionLeftNE)


def test_sparql::orderconditionleftne_constructor_exists():
    assert callable(sparql::OrderConditionLeftNE.__init__)


def test_sparql::orderconditionleftne_constructor_args():
    sig = inspect.signature(sparql::OrderConditionLeftNE.__init__)
    params = list(sig.parameters.keys())



def test_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_query_constructor_exists():
    assert callable(Query.__init__)


def test_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())



def test_sparql::describequery_is_not_abstract():
    assert not inspect.isabstract(sparql::DescribeQuery)


def test_sparql::describequery_constructor_exists():
    assert callable(sparql::DescribeQuery.__init__)


def test_sparql::describequery_constructor_args():
    sig = inspect.signature(sparql::DescribeQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql::constructquery_is_not_abstract():
    assert not inspect.isabstract(sparql::ConstructQuery)


def test_sparql::constructquery_constructor_exists():
    assert callable(sparql::ConstructQuery.__init__)


def test_sparql::constructquery_constructor_args():
    sig = inspect.signature(sparql::ConstructQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql::askquery_is_not_abstract():
    assert not inspect.isabstract(sparql::AskQuery)


def test_sparql::askquery_constructor_exists():
    assert callable(sparql::AskQuery.__init__)


def test_sparql::askquery_constructor_args():
    sig = inspect.signature(sparql::AskQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql::selectquery_is_not_abstract():
    assert not inspect.isabstract(sparql::SelectQuery)


def test_sparql::selectquery_constructor_exists():
    assert callable(sparql::SelectQuery.__init__)


def test_sparql::selectquery_constructor_args():
    sig = inspect.signature(sparql::SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql::locatedelement_is_not_abstract():
    assert not inspect.isabstract(sparql::LocatedElement)


def test_sparql::locatedelement_constructor_exists():
    assert callable(sparql::LocatedElement.__init__)


def test_sparql::locatedelement_constructor_args():
    sig = inspect.signature(sparql::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_sparql::locatedelement_has_commentsAfter():
    assert hasattr(sparql::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in sparql::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_sparql::locatedelement_has_location():
    assert hasattr(sparql::LocatedElement, "location")
    descriptor = None
    for klass in sparql::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_sparql::locatedelement_has_commentsBefore():
    assert hasattr(sparql::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in sparql::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_sparql::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(sparql::UnaryExpression)


def test_sparql::unaryexpression_constructor_exists():
    assert callable(sparql::UnaryExpression.__init__)


def test_sparql::unaryexpression_constructor_args():
    sig = inspect.signature(sparql::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::ws_is_not_abstract():
    assert not inspect.isabstract(sparql::WS)


def test_sparql::ws_constructor_exists():
    assert callable(sparql::WS.__init__)


def test_sparql::ws_constructor_args():
    sig = inspect.signature(sparql::WS.__init__)
    params = list(sig.parameters.keys())
    assert "ws" in params, "Missing parameter 'ws'"

def test_sparql::ws_has_ws():
    assert hasattr(sparql::WS, "ws")
    descriptor = None
    for klass in sparql::WS.__mro__:
        if "ws" in klass.__dict__:
            descriptor = klass.__dict__["ws"]
            break
    assert isinstance(descriptor, property)



def test_sparql::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(sparql::AdditiveExpression)


def test_sparql::additiveexpression_constructor_exists():
    assert callable(sparql::AdditiveExpression.__init__)


def test_sparql::additiveexpression_constructor_args():
    sig = inspect.signature(sparql::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::additionalunaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::AdditionalUnaryExpressionNE)


def test_sparql::additionalunaryexpressionne_constructor_exists():
    assert callable(sparql::AdditionalUnaryExpressionNE.__init__)


def test_sparql::additionalunaryexpressionne_constructor_args():
    sig = inspect.signature(sparql::AdditionalUnaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::prologue_is_not_abstract():
    assert not inspect.isabstract(sparql::Prologue)


def test_sparql::prologue_constructor_exists():
    assert callable(sparql::Prologue.__init__)


def test_sparql::prologue_constructor_args():
    sig = inspect.signature(sparql::Prologue.__init__)
    params = list(sig.parameters.keys())



def test_sparql::additionalvaluelogicalne_is_not_abstract():
    assert not inspect.isabstract(sparql::AdditionalValueLogicalNE)


def test_sparql::additionalvaluelogicalne_constructor_exists():
    assert callable(sparql::AdditionalValueLogicalNE.__init__)


def test_sparql::additionalvaluelogicalne_constructor_args():
    sig = inspect.signature(sparql::AdditionalValueLogicalNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::limitoffsetclauses_is_not_abstract():
    assert not inspect.isabstract(sparql::LimitOffsetClauses)


def test_sparql::limitoffsetclauses_constructor_exists():
    assert callable(sparql::LimitOffsetClauses.__init__)


def test_sparql::limitoffsetclauses_constructor_args():
    sig = inspect.signature(sparql::LimitOffsetClauses.__init__)
    params = list(sig.parameters.keys())



def test_sparql::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(sparql::MultiplicativeExpression)


def test_sparql::multiplicativeexpression_constructor_exists():
    assert callable(sparql::MultiplicativeExpression.__init__)


def test_sparql::multiplicativeexpression_constructor_args():
    sig = inspect.signature(sparql::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::whereclause_is_not_abstract():
    assert not inspect.isabstract(sparql::WhereClause)


def test_sparql::whereclause_constructor_exists():
    assert callable(sparql::WhereClause.__init__)


def test_sparql::whereclause_constructor_args():
    sig = inspect.signature(sparql::WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(sparql::RelationalExpression)


def test_sparql::relationalexpression_constructor_exists():
    assert callable(sparql::RelationalExpression.__init__)


def test_sparql::relationalexpression_constructor_args():
    sig = inspect.signature(sparql::RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::solutionsdisplayne_is_not_abstract():
    assert not inspect.isabstract(sparql::SolutionsDisplayNE)


def test_sparql::solutionsdisplayne_constructor_exists():
    assert callable(sparql::SolutionsDisplayNE.__init__)


def test_sparql::solutionsdisplayne_constructor_args():
    sig = inspect.signature(sparql::SolutionsDisplayNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::additionalnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::AdditionalNumericExpressionNE)


def test_sparql::additionalnumericexpressionne_constructor_exists():
    assert callable(sparql::AdditionalNumericExpressionNE.__init__)


def test_sparql::additionalnumericexpressionne_constructor_args():
    sig = inspect.signature(sparql::AdditionalNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::query_is_not_abstract():
    assert not inspect.isabstract(sparql::Query)


def test_sparql::query_constructor_exists():
    assert callable(sparql::Query.__init__)


def test_sparql::query_constructor_args():
    sig = inspect.signature(sparql::Query.__init__)
    params = list(sig.parameters.keys())



def test_sparql::constructtemplate_is_not_abstract():
    assert not inspect.isabstract(sparql::ConstructTemplate)


def test_sparql::constructtemplate_constructor_exists():
    assert callable(sparql::ConstructTemplate.__init__)


def test_sparql::constructtemplate_constructor_args():
    sig = inspect.signature(sparql::ConstructTemplate.__init__)
    params = list(sig.parameters.keys())



def test_sparql::numericexpression_is_not_abstract():
    assert not inspect.isabstract(sparql::NumericExpression)


def test_sparql::numericexpression_constructor_exists():
    assert callable(sparql::NumericExpression.__init__)


def test_sparql::numericexpression_constructor_args():
    sig = inspect.signature(sparql::NumericExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::pn::prefix_is_not_abstract():
    assert not inspect.isabstract(sparql::PN::PREFIX)


def test_sparql::pn::prefix_constructor_exists():
    assert callable(sparql::PN::PREFIX.__init__)


def test_sparql::pn::prefix_constructor_args():
    sig = inspect.signature(sparql::PN::PREFIX.__init__)
    params = list(sig.parameters.keys())
    assert "pn_prefix" in params, "Missing parameter 'pn_prefix'"

def test_sparql::pn::prefix_has_pn_prefix():
    assert hasattr(sparql::PN::PREFIX, "pn_prefix")
    descriptor = None
    for klass in sparql::PN::PREFIX.__mro__:
        if "pn_prefix" in klass.__dict__:
            descriptor = klass.__dict__["pn_prefix"]
            break
    assert isinstance(descriptor, property)



def test_sparql::ordercondition_is_not_abstract():
    assert not inspect.isabstract(sparql::OrderCondition)


def test_sparql::ordercondition_constructor_exists():
    assert callable(sparql::OrderCondition.__init__)


def test_sparql::ordercondition_constructor_args():
    sig = inspect.signature(sparql::OrderCondition.__init__)
    params = list(sig.parameters.keys())



def test_sparql::solutionmodifier_is_not_abstract():
    assert not inspect.isabstract(sparql::SolutionModifier)


def test_sparql::solutionmodifier_constructor_exists():
    assert callable(sparql::SolutionModifier.__init__)


def test_sparql::solutionmodifier_constructor_args():
    sig = inspect.signature(sparql::SolutionModifier.__init__)
    params = list(sig.parameters.keys())



def test_sparql::additionalconditionalandexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::AdditionalConditionalAndExpressionNE)


def test_sparql::additionalconditionalandexpressionne_constructor_exists():
    assert callable(sparql::AdditionalConditionalAndExpressionNE.__init__)


def test_sparql::additionalconditionalandexpressionne_constructor_args():
    sig = inspect.signature(sparql::AdditionalConditionalAndExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::datasetclause_is_not_abstract():
    assert not inspect.isabstract(sparql::DatasetClause)


def test_sparql::datasetclause_constructor_exists():
    assert callable(sparql::DatasetClause.__init__)


def test_sparql::datasetclause_constructor_args():
    sig = inspect.signature(sparql::DatasetClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql::basedecl_is_not_abstract():
    assert not inspect.isabstract(sparql::BaseDecl)


def test_sparql::basedecl_constructor_exists():
    assert callable(sparql::BaseDecl.__init__)


def test_sparql::basedecl_constructor_args():
    sig = inspect.signature(sparql::BaseDecl.__init__)
    params = list(sig.parameters.keys())



def test_sparql::varname_is_not_abstract():
    assert not inspect.isabstract(sparql::VARNAME)


def test_sparql::varname_constructor_exists():
    assert callable(sparql::VARNAME.__init__)


def test_sparql::varname_constructor_args():
    sig = inspect.signature(sparql::VARNAME.__init__)
    params = list(sig.parameters.keys())
    assert "varname" in params, "Missing parameter 'varname'"

def test_sparql::varname_has_varname():
    assert hasattr(sparql::VARNAME, "varname")
    descriptor = None
    for klass in sparql::VARNAME.__mro__:
        if "varname" in klass.__dict__:
            descriptor = klass.__dict__["varname"]
            break
    assert isinstance(descriptor, property)



def test_sparql::additionalmultiplicativeexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::AdditionalMultiplicativeExpressionNE)


def test_sparql::additionalmultiplicativeexpressionne_constructor_exists():
    assert callable(sparql::AdditionalMultiplicativeExpressionNE.__init__)


def test_sparql::additionalmultiplicativeexpressionne_constructor_args():
    sig = inspect.signature(sparql::AdditionalMultiplicativeExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::pn::local_is_not_abstract():
    assert not inspect.isabstract(sparql::PN::LOCAL)


def test_sparql::pn::local_constructor_exists():
    assert callable(sparql::PN::LOCAL.__init__)


def test_sparql::pn::local_constructor_args():
    sig = inspect.signature(sparql::PN::LOCAL.__init__)
    params = list(sig.parameters.keys())
    assert "pn_local" in params, "Missing parameter 'pn_local'"

def test_sparql::pn::local_has_pn_local():
    assert hasattr(sparql::PN::LOCAL, "pn_local")
    descriptor = None
    for klass in sparql::PN::LOCAL.__mro__:
        if "pn_local" in klass.__dict__:
            descriptor = klass.__dict__["pn_local"]
            break
    assert isinstance(descriptor, property)



def test_sparql::valuelogical_is_not_abstract():
    assert not inspect.isabstract(sparql::ValueLogical)


def test_sparql::valuelogical_constructor_exists():
    assert callable(sparql::ValueLogical.__init__)


def test_sparql::valuelogical_constructor_args():
    sig = inspect.signature(sparql::ValueLogical.__init__)
    params = list(sig.parameters.keys())



def test_sparql::langtagoririrefne_is_not_abstract():
    assert not inspect.isabstract(sparql::LANGTAGOrIRIrefNE)


def test_sparql::langtagoririrefne_constructor_exists():
    assert callable(sparql::LANGTAGOrIRIrefNE.__init__)


def test_sparql::langtagoririrefne_constructor_args():
    sig = inspect.signature(sparql::LANGTAGOrIRIrefNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(sparql::ConditionalAndExpression)


def test_sparql::conditionalandexpression_constructor_exists():
    assert callable(sparql::ConditionalAndExpression.__init__)


def test_sparql::conditionalandexpression_constructor_args():
    sig = inspect.signature(sparql::ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::prefixdecl_is_not_abstract():
    assert not inspect.isabstract(sparql::PrefixDecl)


def test_sparql::prefixdecl_constructor_exists():
    assert callable(sparql::PrefixDecl.__init__)


def test_sparql::prefixdecl_constructor_args():
    sig = inspect.signature(sparql::PrefixDecl.__init__)
    params = list(sig.parameters.keys())



def test_sparql::sparqlqueries_is_not_abstract():
    assert not inspect.isabstract(sparql::SparqlQueries)


def test_sparql::sparqlqueries_constructor_exists():
    assert callable(sparql::SparqlQueries.__init__)


def test_sparql::sparqlqueries_constructor_args():
    sig = inspect.signature(sparql::SparqlQueries.__init__)
    params = list(sig.parameters.keys())



def test_sparql::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(sparql::ConditionalOrExpression)


def test_sparql::conditionalorexpression_constructor_exists():
    assert callable(sparql::ConditionalOrExpression.__init__)


def test_sparql::conditionalorexpression_constructor_args():
    sig = inspect.signature(sparql::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::arglist_is_not_abstract():
    assert not inspect.isabstract(sparql::ArgList)


def test_sparql::arglist_constructor_exists():
    assert callable(sparql::ArgList.__init__)


def test_sparql::arglist_constructor_args():
    sig = inspect.signature(sparql::ArgList.__init__)
    params = list(sig.parameters.keys())



def test_sparql::additionalexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql::AdditionalExpressionNE)


def test_sparql::additionalexpressionne_constructor_exists():
    assert callable(sparql::AdditionalExpressionNE.__init__)


def test_sparql::additionalexpressionne_constructor_args():
    sig = inspect.signature(sparql::AdditionalExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_builtincall_is_not_abstract():
    assert not inspect.isabstract(BuiltInCall)


def test_builtincall_constructor_exists():
    assert callable(BuiltInCall.__init__)


def test_builtincall_constructor_args():
    sig = inspect.signature(BuiltInCall.__init__)
    params = list(sig.parameters.keys())



def test_sparql::isuribuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql::IsURIBuiltInCallNE)


def test_sparql::isuribuiltincallne_constructor_exists():
    assert callable(sparql::IsURIBuiltInCallNE.__init__)


def test_sparql::isuribuiltincallne_constructor_args():
    sig = inspect.signature(sparql::IsURIBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::isliteralbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql::IsLiteralBuiltInCallNE)


def test_sparql::isliteralbuiltincallne_constructor_exists():
    assert callable(sparql::IsLiteralBuiltInCallNE.__init__)


def test_sparql::isliteralbuiltincallne_constructor_args():
    sig = inspect.signature(sparql::IsLiteralBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::regexexpression_is_not_abstract():
    assert not inspect.isabstract(sparql::RegexExpression)


def test_sparql::regexexpression_constructor_exists():
    assert callable(sparql::RegexExpression.__init__)


def test_sparql::regexexpression_constructor_args():
    sig = inspect.signature(sparql::RegexExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::datatypebuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql::DatatypeBuiltInCallNE)


def test_sparql::datatypebuiltincallne_constructor_exists():
    assert callable(sparql::DatatypeBuiltInCallNE.__init__)


def test_sparql::datatypebuiltincallne_constructor_args():
    sig = inspect.signature(sparql::DatatypeBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::langmatchesbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql::LangmatchesBuiltInCallNE)


def test_sparql::langmatchesbuiltincallne_constructor_exists():
    assert callable(sparql::LangmatchesBuiltInCallNE.__init__)


def test_sparql::langmatchesbuiltincallne_constructor_args():
    sig = inspect.signature(sparql::LangmatchesBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::isiribuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql::IsIRIBuiltInCallNE)


def test_sparql::isiribuiltincallne_constructor_exists():
    assert callable(sparql::IsIRIBuiltInCallNE.__init__)


def test_sparql::isiribuiltincallne_constructor_args():
    sig = inspect.signature(sparql::IsIRIBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::isblankbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql::IsBlankBuiltInCallNE)


def test_sparql::isblankbuiltincallne_constructor_exists():
    assert callable(sparql::IsBlankBuiltInCallNE.__init__)


def test_sparql::isblankbuiltincallne_constructor_args():
    sig = inspect.signature(sparql::IsBlankBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::langbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql::LangBuiltInCallNE)


def test_sparql::langbuiltincallne_constructor_exists():
    assert callable(sparql::LangBuiltInCallNE.__init__)


def test_sparql::langbuiltincallne_constructor_args():
    sig = inspect.signature(sparql::LangBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::strbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql::StrBuiltInCallNE)


def test_sparql::strbuiltincallne_constructor_exists():
    assert callable(sparql::StrBuiltInCallNE.__init__)


def test_sparql::strbuiltincallne_constructor_args():
    sig = inspect.signature(sparql::StrBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::expression_is_not_abstract():
    assert not inspect.isabstract(sparql::Expression)


def test_sparql::expression_constructor_exists():
    assert callable(sparql::Expression.__init__)


def test_sparql::expression_constructor_args():
    sig = inspect.signature(sparql::Expression.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_sparql::functioncall_is_not_abstract():
    assert not inspect.isabstract(sparql::FunctionCall)


def test_sparql::functioncall_constructor_exists():
    assert callable(sparql::FunctionCall.__init__)


def test_sparql::functioncall_constructor_args():
    sig = inspect.signature(sparql::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_sparql::sametermbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql::SameTermBuiltInCallNE)


def test_sparql::sametermbuiltincallne_constructor_exists():
    assert callable(sparql::SameTermBuiltInCallNE.__init__)


def test_sparql::sametermbuiltincallne_constructor_args():
    sig = inspect.signature(sparql::SameTermBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::boundbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql::BoundBuiltInCallNE)


def test_sparql::boundbuiltincallne_constructor_exists():
    assert callable(sparql::BoundBuiltInCallNE.__init__)


def test_sparql::boundbuiltincallne_constructor_args():
    sig = inspect.signature(sparql::BoundBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_triplesnode_is_not_abstract():
    assert not inspect.isabstract(TriplesNode)


def test_triplesnode_constructor_exists():
    assert callable(TriplesNode.__init__)


def test_triplesnode_constructor_args():
    sig = inspect.signature(TriplesNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql::blanknodepropertylist_is_not_abstract():
    assert not inspect.isabstract(sparql::BlankNodePropertyList)


def test_sparql::blanknodepropertylist_constructor_exists():
    assert callable(sparql::BlankNodePropertyList.__init__)


def test_sparql::blanknodepropertylist_constructor_args():
    sig = inspect.signature(sparql::BlankNodePropertyList.__init__)
    params = list(sig.parameters.keys())



def test_sparql::collection_is_not_abstract():
    assert not inspect.isabstract(sparql::Collection)


def test_sparql::collection_constructor_exists():
    assert callable(sparql::Collection.__init__)


def test_sparql::collection_constructor_args():
    sig = inspect.signature(sparql::Collection.__init__)
    params = list(sig.parameters.keys())



def test_sparql::graphnode_is_not_abstract():
    assert not inspect.isabstract(sparql::GraphNode)


def test_sparql::graphnode_constructor_exists():
    assert callable(sparql::GraphNode.__init__)


def test_sparql::graphnode_constructor_args():
    sig = inspect.signature(sparql::GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql::object_is_not_abstract():
    assert not inspect.isabstract(sparql::Object)


def test_sparql::object_constructor_exists():
    assert callable(sparql::Object.__init__)


def test_sparql::object_constructor_args():
    sig = inspect.signature(sparql::Object.__init__)
    params = list(sig.parameters.keys())



def test_sparql::objectlist_is_not_abstract():
    assert not inspect.isabstract(sparql::ObjectList)


def test_sparql::objectlist_constructor_exists():
    assert callable(sparql::ObjectList.__init__)


def test_sparql::objectlist_constructor_args():
    sig = inspect.signature(sparql::ObjectList.__init__)
    params = list(sig.parameters.keys())



def test_sparql::verb_is_not_abstract():
    assert not inspect.isabstract(sparql::Verb)


def test_sparql::verb_constructor_exists():
    assert callable(sparql::Verb.__init__)


def test_sparql::verb_constructor_args():
    sig = inspect.signature(sparql::Verb.__init__)
    params = list(sig.parameters.keys())



def test_graphnode_is_not_abstract():
    assert not inspect.isabstract(GraphNode)


def test_graphnode_constructor_exists():
    assert callable(GraphNode.__init__)


def test_graphnode_constructor_args():
    sig = inspect.signature(GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql::propertylistnotempty_is_not_abstract():
    assert not inspect.isabstract(sparql::PropertyListNotEmpty)


def test_sparql::propertylistnotempty_constructor_exists():
    assert callable(sparql::PropertyListNotEmpty.__init__)


def test_sparql::propertylistnotempty_constructor_args():
    sig = inspect.signature(sparql::PropertyListNotEmpty.__init__)
    params = list(sig.parameters.keys())



def test_sparql::patternorfilterne_is_not_abstract():
    assert not inspect.isabstract(sparql::PatternOrFilterNE)


def test_sparql::patternorfilterne_constructor_exists():
    assert callable(sparql::PatternOrFilterNE.__init__)


def test_sparql::patternorfilterne_constructor_args():
    sig = inspect.signature(sparql::PatternOrFilterNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::varorterm_is_not_abstract():
    assert not inspect.isabstract(sparql::VarOrTerm)


def test_sparql::varorterm_constructor_exists():
    assert callable(sparql::VarOrTerm.__init__)


def test_sparql::varorterm_constructor_args():
    sig = inspect.signature(sparql::VarOrTerm.__init__)
    params = list(sig.parameters.keys())



def test_triplessamesubject_is_not_abstract():
    assert not inspect.isabstract(TriplesSameSubject)


def test_triplessamesubject_constructor_exists():
    assert callable(TriplesSameSubject.__init__)


def test_triplessamesubject_constructor_args():
    sig = inspect.signature(TriplesSameSubject.__init__)
    params = list(sig.parameters.keys())



def test_sparql::triplessamesubjectleftne_is_not_abstract():
    assert not inspect.isabstract(sparql::TriplesSameSubjectLeftNE)


def test_sparql::triplessamesubjectleftne_constructor_exists():
    assert callable(sparql::TriplesSameSubjectLeftNE.__init__)


def test_sparql::triplessamesubjectleftne_constructor_args():
    sig = inspect.signature(sparql::TriplesSameSubjectLeftNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::additionalggpelement_is_not_abstract():
    assert not inspect.isabstract(sparql::AdditionalGGPElement)


def test_sparql::additionalggpelement_constructor_exists():
    assert callable(sparql::AdditionalGGPElement.__init__)


def test_sparql::additionalggpelement_constructor_args():
    sig = inspect.signature(sparql::AdditionalGGPElement.__init__)
    params = list(sig.parameters.keys())



def test_sparql::triplesblock_is_not_abstract():
    assert not inspect.isabstract(sparql::TriplesBlock)


def test_sparql::triplesblock_constructor_exists():
    assert callable(sparql::TriplesBlock.__init__)


def test_sparql::triplesblock_constructor_args():
    sig = inspect.signature(sparql::TriplesBlock.__init__)
    params = list(sig.parameters.keys())



def test_graphpatternnottriples_is_not_abstract():
    assert not inspect.isabstract(GraphPatternNotTriples)


def test_graphpatternnottriples_constructor_exists():
    assert callable(GraphPatternNotTriples.__init__)


def test_graphpatternnottriples_constructor_args():
    sig = inspect.signature(GraphPatternNotTriples.__init__)
    params = list(sig.parameters.keys())



def test_sparql::graphgraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql::GraphGraphPattern)


def test_sparql::graphgraphpattern_constructor_exists():
    assert callable(sparql::GraphGraphPattern.__init__)


def test_sparql::graphgraphpattern_constructor_args():
    sig = inspect.signature(sparql::GraphGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql::grouporuniongraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql::GroupOrUnionGraphPattern)


def test_sparql::grouporuniongraphpattern_constructor_exists():
    assert callable(sparql::GroupOrUnionGraphPattern.__init__)


def test_sparql::grouporuniongraphpattern_constructor_args():
    sig = inspect.signature(sparql::GroupOrUnionGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql::optionalgraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql::OptionalGraphPattern)


def test_sparql::optionalgraphpattern_constructor_exists():
    assert callable(sparql::OptionalGraphPattern.__init__)


def test_sparql::optionalgraphpattern_constructor_args():
    sig = inspect.signature(sparql::OptionalGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_patternorfilterne_is_not_abstract():
    assert not inspect.isabstract(PatternOrFilterNE)


def test_patternorfilterne_constructor_exists():
    assert callable(PatternOrFilterNE.__init__)


def test_patternorfilterne_constructor_args():
    sig = inspect.signature(PatternOrFilterNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::filter_is_not_abstract():
    assert not inspect.isabstract(sparql::Filter)


def test_sparql::filter_constructor_exists():
    assert callable(sparql::Filter.__init__)


def test_sparql::filter_constructor_args():
    sig = inspect.signature(sparql::Filter.__init__)
    params = list(sig.parameters.keys())



def test_sparql::graphpatternnottriples_is_not_abstract():
    assert not inspect.isabstract(sparql::GraphPatternNotTriples)


def test_sparql::graphpatternnottriples_constructor_exists():
    assert callable(sparql::GraphPatternNotTriples.__init__)


def test_sparql::graphpatternnottriples_constructor_args():
    sig = inspect.signature(sparql::GraphPatternNotTriples.__init__)
    params = list(sig.parameters.keys())



def test_sparql::triplesnode_is_not_abstract():
    assert not inspect.isabstract(sparql::TriplesNode)


def test_sparql::triplesnode_constructor_exists():
    assert callable(sparql::TriplesNode.__init__)


def test_sparql::triplesnode_constructor_args():
    sig = inspect.signature(sparql::TriplesNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql::triplessamesubjectrightne_is_not_abstract():
    assert not inspect.isabstract(sparql::TriplesSameSubjectRightNE)


def test_sparql::triplessamesubjectrightne_constructor_exists():
    assert callable(sparql::TriplesSameSubjectRightNE.__init__)


def test_sparql::triplessamesubjectrightne_constructor_args():
    sig = inspect.signature(sparql::TriplesSameSubjectRightNE.__init__)
    params = list(sig.parameters.keys())



def test_irireference_is_not_abstract():
    assert not inspect.isabstract(IRIreference)


def test_irireference_constructor_exists():
    assert callable(IRIreference.__init__)


def test_irireference_constructor_args():
    sig = inspect.signature(IRIreference.__init__)
    params = list(sig.parameters.keys())



def test_sparql::prefixedname_is_not_abstract():
    assert not inspect.isabstract(sparql::PrefixedName)


def test_sparql::prefixedname_constructor_exists():
    assert callable(sparql::PrefixedName.__init__)


def test_sparql::prefixedname_constructor_args():
    sig = inspect.signature(sparql::PrefixedName.__init__)
    params = list(sig.parameters.keys())



def test_sourceselector_is_not_abstract():
    assert not inspect.isabstract(SourceSelector)


def test_sourceselector_constructor_exists():
    assert callable(SourceSelector.__init__)


def test_sourceselector_constructor_args():
    sig = inspect.signature(SourceSelector.__init__)
    params = list(sig.parameters.keys())



def test_graphterm_is_not_abstract():
    assert not inspect.isabstract(GraphTerm)


def test_graphterm_constructor_exists():
    assert callable(GraphTerm.__init__)


def test_graphterm_constructor_args():
    sig = inspect.signature(GraphTerm.__init__)
    params = list(sig.parameters.keys())



def test_sparql::blanknode_is_not_abstract():
    assert not inspect.isabstract(sparql::BlankNode)


def test_sparql::blanknode_constructor_exists():
    assert callable(sparql::BlankNode.__init__)


def test_sparql::blanknode_constructor_args():
    sig = inspect.signature(sparql::BlankNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql::notinlist_is_not_abstract():
    assert not inspect.isabstract(sparql::NotInList)


def test_sparql::notinlist_constructor_exists():
    assert callable(sparql::NotInList.__init__)


def test_sparql::notinlist_constructor_args():
    sig = inspect.signature(sparql::NotInList.__init__)
    params = list(sig.parameters.keys())



def test_sparql::groupgraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql::GroupGraphPattern)


def test_sparql::groupgraphpattern_constructor_exists():
    assert callable(sparql::GroupGraphPattern.__init__)


def test_sparql::groupgraphpattern_constructor_args():
    sig = inspect.signature(sparql::GroupGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql::whereliteral_is_not_abstract():
    assert not inspect.isabstract(sparql::WhereLiteral)


def test_sparql::whereliteral_constructor_exists():
    assert callable(sparql::WhereLiteral.__init__)


def test_sparql::whereliteral_constructor_args():
    sig = inspect.signature(sparql::WhereLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql::sourceselector_is_not_abstract():
    assert not inspect.isabstract(sparql::SourceSelector)


def test_sparql::sourceselector_constructor_exists():
    assert callable(sparql::SourceSelector.__init__)


def test_sparql::sourceselector_constructor_args():
    sig = inspect.signature(sparql::SourceSelector.__init__)
    params = list(sig.parameters.keys())



def test_graphclausene_is_not_abstract():
    assert not inspect.isabstract(GraphClauseNE)


def test_graphclausene_constructor_exists():
    assert callable(GraphClauseNE.__init__)


def test_graphclausene_constructor_args():
    sig = inspect.signature(GraphClauseNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::namedgraphclause_is_not_abstract():
    assert not inspect.isabstract(sparql::NamedGraphClause)


def test_sparql::namedgraphclause_constructor_exists():
    assert callable(sparql::NamedGraphClause.__init__)


def test_sparql::namedgraphclause_constructor_args():
    sig = inspect.signature(sparql::NamedGraphClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql::defaultgraphclause_is_not_abstract():
    assert not inspect.isabstract(sparql::DefaultGraphClause)


def test_sparql::defaultgraphclause_constructor_exists():
    assert callable(sparql::DefaultGraphClause.__init__)


def test_sparql::defaultgraphclause_constructor_args():
    sig = inspect.signature(sparql::DefaultGraphClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql::graphclausene_is_not_abstract():
    assert not inspect.isabstract(sparql::GraphClauseNE)


def test_sparql::graphclausene_constructor_exists():
    assert callable(sparql::GraphClauseNE.__init__)


def test_sparql::graphclausene_constructor_args():
    sig = inspect.signature(sparql::GraphClauseNE.__init__)
    params = list(sig.parameters.keys())



def test_orderconditionrightne_is_not_abstract():
    assert not inspect.isabstract(OrderConditionRightNE)


def test_orderconditionrightne_constructor_exists():
    assert callable(OrderConditionRightNE.__init__)


def test_orderconditionrightne_constructor_args():
    sig = inspect.signature(OrderConditionRightNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::constraint_is_not_abstract():
    assert not inspect.isabstract(sparql::Constraint)


def test_sparql::constraint_constructor_exists():
    assert callable(sparql::Constraint.__init__)


def test_sparql::constraint_constructor_args():
    sig = inspect.signature(sparql::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_varorterm_is_not_abstract():
    assert not inspect.isabstract(VarOrTerm)


def test_varorterm_constructor_exists():
    assert callable(VarOrTerm.__init__)


def test_varorterm_constructor_args():
    sig = inspect.signature(VarOrTerm.__init__)
    params = list(sig.parameters.keys())



def test_sparql::graphterm_is_not_abstract():
    assert not inspect.isabstract(sparql::GraphTerm)


def test_sparql::graphterm_constructor_exists():
    assert callable(sparql::GraphTerm.__init__)


def test_sparql::graphterm_constructor_args():
    sig = inspect.signature(sparql::GraphTerm.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::rdfliteral_is_not_abstract():
    assert not inspect.isabstract(sparql::RDFLiteral)


def test_sparql::rdfliteral_constructor_exists():
    assert callable(sparql::RDFLiteral.__init__)


def test_sparql::rdfliteral_constructor_args():
    sig = inspect.signature(sparql::RDFLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql::builtincall_is_not_abstract():
    assert not inspect.isabstract(sparql::BuiltInCall)


def test_sparql::builtincall_constructor_exists():
    assert callable(sparql::BuiltInCall.__init__)


def test_sparql::builtincall_constructor_args():
    sig = inspect.signature(sparql::BuiltInCall.__init__)
    params = list(sig.parameters.keys())



def test_sparql::brackettedexpression_is_not_abstract():
    assert not inspect.isabstract(sparql::BrackettedExpression)


def test_sparql::brackettedexpression_constructor_exists():
    assert callable(sparql::BrackettedExpression.__init__)


def test_sparql::brackettedexpression_constructor_args():
    sig = inspect.signature(sparql::BrackettedExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql::numericliteral_is_not_abstract():
    assert not inspect.isabstract(sparql::NumericLiteral)


def test_sparql::numericliteral_constructor_exists():
    assert callable(sparql::NumericLiteral.__init__)


def test_sparql::numericliteral_constructor_args():
    sig = inspect.signature(sparql::NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(sparql::BooleanLiteral)


def test_sparql::booleanliteral_constructor_exists():
    assert callable(sparql::BooleanLiteral.__init__)


def test_sparql::booleanliteral_constructor_args():
    sig = inspect.signature(sparql::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql::irireforfunction_is_not_abstract():
    assert not inspect.isabstract(sparql::IRIrefOrFunction)


def test_sparql::irireforfunction_constructor_exists():
    assert callable(sparql::IRIrefOrFunction.__init__)


def test_sparql::irireforfunction_constructor_args():
    sig = inspect.signature(sparql::IRIrefOrFunction.__init__)
    params = list(sig.parameters.keys())



def test_varoririref_is_not_abstract():
    assert not inspect.isabstract(VarOrIRIref)


def test_varoririref_constructor_exists():
    assert callable(VarOrIRIref.__init__)


def test_varoririref_constructor_args():
    sig = inspect.signature(VarOrIRIref.__init__)
    params = list(sig.parameters.keys())



def test_sparql::pname::ln_is_not_abstract():
    assert not inspect.isabstract(sparql::PNAME::LN)


def test_sparql::pname::ln_constructor_exists():
    assert callable(sparql::PNAME::LN.__init__)


def test_sparql::pname::ln_constructor_args():
    sig = inspect.signature(sparql::PNAME::LN.__init__)
    params = list(sig.parameters.keys())



def test_sparql::irireference_is_not_abstract():
    assert not inspect.isabstract(sparql::IRIreference)


def test_sparql::irireference_constructor_exists():
    assert callable(sparql::IRIreference.__init__)


def test_sparql::irireference_constructor_args():
    sig = inspect.signature(sparql::IRIreference.__init__)
    params = list(sig.parameters.keys())



def test_sparql::iri::ref_is_not_abstract():
    assert not inspect.isabstract(sparql::IRI::REF)


def test_sparql::iri::ref_constructor_exists():
    assert callable(sparql::IRI::REF.__init__)


def test_sparql::iri::ref_constructor_args():
    sig = inspect.signature(sparql::IRI::REF.__init__)
    params = list(sig.parameters.keys())
    assert "iri_ref" in params, "Missing parameter 'iri_ref'"

def test_sparql::iri::ref_has_iri_ref():
    assert hasattr(sparql::IRI::REF, "iri_ref")
    descriptor = None
    for klass in sparql::IRI::REF.__mro__:
        if "iri_ref" in klass.__dict__:
            descriptor = klass.__dict__["iri_ref"]
            break
    assert isinstance(descriptor, property)



def test_sparql::var_is_not_abstract():
    assert not inspect.isabstract(sparql::Var)


def test_sparql::var_constructor_exists():
    assert callable(sparql::Var.__init__)


def test_sparql::var_constructor_args():
    sig = inspect.signature(sparql::Var.__init__)
    params = list(sig.parameters.keys())
    assert "varname" in params, "Missing parameter 'varname'"

def test_sparql::var_has_varname():
    assert hasattr(sparql::Var, "varname")
    descriptor = None
    for klass in sparql::Var.__mro__:
        if "varname" in klass.__dict__:
            descriptor = klass.__dict__["varname"]
            break
    assert isinstance(descriptor, property)



def test_sparql::pname::ns_is_not_abstract():
    assert not inspect.isabstract(sparql::PNAME::NS)


def test_sparql::pname::ns_constructor_exists():
    assert callable(sparql::PNAME::NS.__init__)


def test_sparql::pname::ns_constructor_args():
    sig = inspect.signature(sparql::PNAME::NS.__init__)
    params = list(sig.parameters.keys())
    assert "pn_prefix" in params, "Missing parameter 'pn_prefix'"

def test_sparql::pname::ns_has_pn_prefix():
    assert hasattr(sparql::PNAME::NS, "pn_prefix")
    descriptor = None
    for klass in sparql::PNAME::NS.__mro__:
        if "pn_prefix" in klass.__dict__:
            descriptor = klass.__dict__["pn_prefix"]
            break
    assert isinstance(descriptor, property)



def test_verb_is_not_abstract():
    assert not inspect.isabstract(Verb)


def test_verb_constructor_exists():
    assert callable(Verb.__init__)


def test_verb_constructor_args():
    sig = inspect.signature(Verb.__init__)
    params = list(sig.parameters.keys())



def test_sparql::verbane_is_not_abstract():
    assert not inspect.isabstract(sparql::VerbANE)


def test_sparql::verbane_constructor_exists():
    assert callable(sparql::VerbANE.__init__)


def test_sparql::verbane_constructor_args():
    sig = inspect.signature(sparql::VerbANE.__init__)
    params = list(sig.parameters.keys())
    assert "theA" in params, "Missing parameter 'theA'"

def test_sparql::verbane_has_theA():
    assert hasattr(sparql::VerbANE, "theA")
    descriptor = None
    for klass in sparql::VerbANE.__mro__:
        if "theA" in klass.__dict__:
            descriptor = klass.__dict__["theA"]
            break
    assert isinstance(descriptor, property)



def test_sparql::varoririref_is_not_abstract():
    assert not inspect.isabstract(sparql::VarOrIRIref)


def test_sparql::varoririref_constructor_exists():
    assert callable(sparql::VarOrIRIref.__init__)


def test_sparql::varoririref_constructor_args():
    sig = inspect.signature(sparql::VarOrIRIref.__init__)
    params = list(sig.parameters.keys())



def test_variablesne_is_not_abstract():
    assert not inspect.isabstract(VariablesNE)


def test_variablesne_constructor_exists():
    assert callable(VariablesNE.__init__)


def test_variablesne_constructor_args():
    sig = inspect.signature(VariablesNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::somevariablesne_is_not_abstract():
    assert not inspect.isabstract(sparql::SomeVariablesNE)


def test_sparql::somevariablesne_constructor_exists():
    assert callable(sparql::SomeVariablesNE.__init__)


def test_sparql::somevariablesne_constructor_args():
    sig = inspect.signature(sparql::SomeVariablesNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::allvariablesne_is_not_abstract():
    assert not inspect.isabstract(sparql::AllVariablesNE)


def test_sparql::allvariablesne_constructor_exists():
    assert callable(sparql::AllVariablesNE.__init__)


def test_sparql::allvariablesne_constructor_args():
    sig = inspect.signature(sparql::AllVariablesNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::variablesne_is_not_abstract():
    assert not inspect.isabstract(sparql::VariablesNE)


def test_sparql::variablesne_constructor_exists():
    assert callable(sparql::VariablesNE.__init__)


def test_sparql::variablesne_constructor_args():
    sig = inspect.signature(sparql::VariablesNE.__init__)
    params = list(sig.parameters.keys())



def test_solutionsdisplayne_is_not_abstract():
    assert not inspect.isabstract(SolutionsDisplayNE)


def test_solutionsdisplayne_constructor_exists():
    assert callable(SolutionsDisplayNE.__init__)


def test_solutionsdisplayne_constructor_args():
    sig = inspect.signature(SolutionsDisplayNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::reducedne_is_not_abstract():
    assert not inspect.isabstract(sparql::ReducedNE)


def test_sparql::reducedne_constructor_exists():
    assert callable(sparql::ReducedNE.__init__)


def test_sparql::reducedne_constructor_args():
    sig = inspect.signature(sparql::ReducedNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::distinctne_is_not_abstract():
    assert not inspect.isabstract(sparql::DistinctNE)


def test_sparql::distinctne_constructor_exists():
    assert callable(sparql::DistinctNE.__init__)


def test_sparql::distinctne_constructor_args():
    sig = inspect.signature(sparql::DistinctNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::integer_is_not_abstract():
    assert not inspect.isabstract(sparql::INTEGER)


def test_sparql::integer_constructor_exists():
    assert callable(sparql::INTEGER.__init__)


def test_sparql::integer_constructor_args():
    sig = inspect.signature(sparql::INTEGER.__init__)
    params = list(sig.parameters.keys())
    assert "integer" in params, "Missing parameter 'integer'"

def test_sparql::integer_has_integer():
    assert hasattr(sparql::INTEGER, "integer")
    descriptor = None
    for klass in sparql::INTEGER.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)



def test_sparql::orderclause_is_not_abstract():
    assert not inspect.isabstract(sparql::OrderClause)


def test_sparql::orderclause_constructor_exists():
    assert callable(sparql::OrderClause.__init__)


def test_sparql::orderclause_constructor_args():
    sig = inspect.signature(sparql::OrderClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql::triplessamesubject_is_not_abstract():
    assert not inspect.isabstract(sparql::TriplesSameSubject)


def test_sparql::triplessamesubject_constructor_exists():
    assert callable(sparql::TriplesSameSubject.__init__)


def test_sparql::triplessamesubject_constructor_args():
    sig = inspect.signature(sparql::TriplesSameSubject.__init__)
    params = list(sig.parameters.keys())



def test_sparql::offsetclause_is_not_abstract():
    assert not inspect.isabstract(sparql::OffsetClause)


def test_sparql::offsetclause_constructor_exists():
    assert callable(sparql::OffsetClause.__init__)


def test_sparql::offsetclause_constructor_args():
    sig = inspect.signature(sparql::OffsetClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql::limitclause_is_not_abstract():
    assert not inspect.isabstract(sparql::LimitClause)


def test_sparql::limitclause_constructor_exists():
    assert callable(sparql::LimitClause.__init__)


def test_sparql::limitclause_constructor_args():
    sig = inspect.signature(sparql::LimitClause.__init__)
    params = list(sig.parameters.keys())



def test_limitoffsetclauses_is_not_abstract():
    assert not inspect.isabstract(LimitOffsetClauses)


def test_limitoffsetclauses_constructor_exists():
    assert callable(LimitOffsetClauses.__init__)


def test_limitoffsetclauses_constructor_args():
    sig = inspect.signature(LimitOffsetClauses.__init__)
    params = list(sig.parameters.keys())



def test_sparql::limitoffsetclausesrightne_is_not_abstract():
    assert not inspect.isabstract(sparql::LimitOffsetClausesRightNE)


def test_sparql::limitoffsetclausesrightne_constructor_exists():
    assert callable(sparql::LimitOffsetClausesRightNE.__init__)


def test_sparql::limitoffsetclausesrightne_constructor_args():
    sig = inspect.signature(sparql::LimitOffsetClausesRightNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::limitoffsetclausesleftne_is_not_abstract():
    assert not inspect.isabstract(sparql::LimitOffsetClausesLeftNE)


def test_sparql::limitoffsetclausesleftne_constructor_exists():
    assert callable(sparql::LimitOffsetClausesLeftNE.__init__)


def test_sparql::limitoffsetclausesleftne_constructor_args():
    sig = inspect.signature(sparql::LimitOffsetClausesLeftNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql::orderconditionrightne_is_not_abstract():
    assert not inspect.isabstract(sparql::OrderConditionRightNE)


def test_sparql::orderconditionrightne_constructor_exists():
    assert callable(sparql::OrderConditionRightNE.__init__)


def test_sparql::orderconditionrightne_constructor_args():
    sig = inspect.signature(sparql::OrderConditionRightNE.__init__)
    params = list(sig.parameters.keys())


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
BlankNode_strategy = st.builds(
    BlankNode,
)
sparql::ANON_strategy = st.builds(
    sparql::ANON,
)
sparql::BLANK::NODE::LABEL_strategy = st.builds(
    sparql::BLANK::NODE::LABEL,
    pn_local=
        safe_text
)
AscOrDecs_strategy = st.builds(
    AscOrDecs,
)
sparql::DescendingLiteral_strategy = st.builds(
    sparql::DescendingLiteral,
)
sparql::AscendingLiteral_strategy = st.builds(
    sparql::AscendingLiteral,
)
StringLiteral_strategy = st.builds(
    StringLiteral,
)
sparql::STRING::LITERAL2_strategy = st.builds(
    sparql::STRING::LITERAL2,
    string=
        safe_text
)
sparql::STRING::LITERAL::LONG2_strategy = st.builds(
    sparql::STRING::LITERAL::LONG2,
    string=
        safe_text
)
sparql::STRING::LITERAL::LONG1_strategy = st.builds(
    sparql::STRING::LITERAL::LONG1,
    string=
        safe_text
)
sparql::STRING::LITERAL1_strategy = st.builds(
    sparql::STRING::LITERAL1,
    string=
        safe_text
)
sparql::VAR2_strategy = st.builds(
    sparql::VAR2,
)
sparql::VAR1_strategy = st.builds(
    sparql::VAR1,
)
BooleanLiteral_strategy = st.builds(
    BooleanLiteral,
)
sparql::FalseBooleanLiteralNE_strategy = st.builds(
    sparql::FalseBooleanLiteralNE,
)
sparql::TrueBooleanLiteralNE_strategy = st.builds(
    sparql::TrueBooleanLiteralNE,
)
PrefixedName_strategy = st.builds(
    PrefixedName,
)
sparql::StringLiteral_strategy = st.builds(
    sparql::StringLiteral,
)
LANGTAGOrIRIrefNE_strategy = st.builds(
    LANGTAGOrIRIrefNE,
)
sparql::LANGTAG_strategy = st.builds(
    sparql::LANGTAG,
    langtag=
        safe_text
)
sparql::UpIRIrefNE_strategy = st.builds(
    sparql::UpIRIrefNE,
)
AdditionalUnaryExpressionNE_strategy = st.builds(
    AdditionalUnaryExpressionNE,
)
sparql::TimesAdditionalUnaryExpressionNE_strategy = st.builds(
    sparql::TimesAdditionalUnaryExpressionNE,
)
NumericLiteral_strategy = st.builds(
    NumericLiteral,
)
sparql::NumericLiteralUnsigned_strategy = st.builds(
    sparql::NumericLiteralUnsigned,
)
sparql::DOUBLE_strategy = st.builds(
    sparql::DOUBLE,
    double=
        safe_text
)
sparql::DECIMAL_strategy = st.builds(
    sparql::DECIMAL,
    decimal=
        safe_text
)
AdditionalMultiplicativeExpressionNE_strategy = st.builds(
    AdditionalMultiplicativeExpressionNE,
)
sparql::NumericLiteralNegative_strategy = st.builds(
    sparql::NumericLiteralNegative,
)
sparql::NumericLiteralPositive_strategy = st.builds(
    sparql::NumericLiteralPositive,
)
sparql::MinusMultiplicativeExpressionNE_strategy = st.builds(
    sparql::MinusMultiplicativeExpressionNE,
)
sparql::PlusMultiplicativeExpressionNE_strategy = st.builds(
    sparql::PlusMultiplicativeExpressionNE,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
sparql::PlusPrimaryExpressionNE_strategy = st.builds(
    sparql::PlusPrimaryExpressionNE,
)
sparql::PrimaryExpression_strategy = st.builds(
    sparql::PrimaryExpression,
)
sparql::MinusPrimaryExpressionNE_strategy = st.builds(
    sparql::MinusPrimaryExpressionNE,
)
sparql::NotPrimaryExpressionNE_strategy = st.builds(
    sparql::NotPrimaryExpressionNE,
)
sparql::DividedByAdditionalUnaryExpressionNE_strategy = st.builds(
    sparql::DividedByAdditionalUnaryExpressionNE,
)
AdditionalNumericExpressionNE_strategy = st.builds(
    AdditionalNumericExpressionNE,
)
sparql::BiggerOrEqualNumericExpressionNE_strategy = st.builds(
    sparql::BiggerOrEqualNumericExpressionNE,
)
sparql::NotEqualNumericExpressionNE_strategy = st.builds(
    sparql::NotEqualNumericExpressionNE,
)
sparql::BiggerNumericExpressionNE_strategy = st.builds(
    sparql::BiggerNumericExpressionNE,
)
sparql::SmallerOrEqualNumericExpressionNE_strategy = st.builds(
    sparql::SmallerOrEqualNumericExpressionNE,
)
sparql::SmallerNumericExpressionNE_strategy = st.builds(
    sparql::SmallerNumericExpressionNE,
)
sparql::EqualsNumericExpressionNE_strategy = st.builds(
    sparql::EqualsNumericExpressionNE,
)
ArgList_strategy = st.builds(
    ArgList,
)
sparql::ArgListExpressionNE_strategy = st.builds(
    sparql::ArgListExpressionNE,
)
sparql::ArgListNILNE_strategy = st.builds(
    sparql::ArgListNILNE,
)
sparql::AscOrDecs_strategy = st.builds(
    sparql::AscOrDecs,
)
OrderCondition_strategy = st.builds(
    OrderCondition,
)
sparql::OrderConditionLeftNE_strategy = st.builds(
    sparql::OrderConditionLeftNE,
)
Query_strategy = st.builds(
    Query,
)
sparql::DescribeQuery_strategy = st.builds(
    sparql::DescribeQuery,
)
sparql::ConstructQuery_strategy = st.builds(
    sparql::ConstructQuery,
)
sparql::AskQuery_strategy = st.builds(
    sparql::AskQuery,
)
sparql::SelectQuery_strategy = st.builds(
    sparql::SelectQuery,
)
sparql::LocatedElement_strategy = st.builds(
    sparql::LocatedElement,
    commentsAfter=
        safe_text,
    location=
        safe_text,
    commentsBefore=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
sparql::UnaryExpression_strategy = st.builds(
    sparql::UnaryExpression,
)
sparql::WS_strategy = st.builds(
    sparql::WS,
    ws=
        safe_text
)
sparql::AdditiveExpression_strategy = st.builds(
    sparql::AdditiveExpression,
)
sparql::AdditionalUnaryExpressionNE_strategy = st.builds(
    sparql::AdditionalUnaryExpressionNE,
)
sparql::Prologue_strategy = st.builds(
    sparql::Prologue,
)
sparql::AdditionalValueLogicalNE_strategy = st.builds(
    sparql::AdditionalValueLogicalNE,
)
sparql::LimitOffsetClauses_strategy = st.builds(
    sparql::LimitOffsetClauses,
)
sparql::MultiplicativeExpression_strategy = st.builds(
    sparql::MultiplicativeExpression,
)
sparql::WhereClause_strategy = st.builds(
    sparql::WhereClause,
)
sparql::RelationalExpression_strategy = st.builds(
    sparql::RelationalExpression,
)
sparql::SolutionsDisplayNE_strategy = st.builds(
    sparql::SolutionsDisplayNE,
)
sparql::AdditionalNumericExpressionNE_strategy = st.builds(
    sparql::AdditionalNumericExpressionNE,
)
sparql::Query_strategy = st.builds(
    sparql::Query,
)
sparql::ConstructTemplate_strategy = st.builds(
    sparql::ConstructTemplate,
)
sparql::NumericExpression_strategy = st.builds(
    sparql::NumericExpression,
)
sparql::PN::PREFIX_strategy = st.builds(
    sparql::PN::PREFIX,
    pn_prefix=
        safe_text
)
sparql::OrderCondition_strategy = st.builds(
    sparql::OrderCondition,
)
sparql::SolutionModifier_strategy = st.builds(
    sparql::SolutionModifier,
)
sparql::AdditionalConditionalAndExpressionNE_strategy = st.builds(
    sparql::AdditionalConditionalAndExpressionNE,
)
sparql::DatasetClause_strategy = st.builds(
    sparql::DatasetClause,
)
sparql::BaseDecl_strategy = st.builds(
    sparql::BaseDecl,
)
sparql::VARNAME_strategy = st.builds(
    sparql::VARNAME,
    varname=
        safe_text
)
sparql::AdditionalMultiplicativeExpressionNE_strategy = st.builds(
    sparql::AdditionalMultiplicativeExpressionNE,
)
sparql::PN::LOCAL_strategy = st.builds(
    sparql::PN::LOCAL,
    pn_local=
        safe_text
)
sparql::ValueLogical_strategy = st.builds(
    sparql::ValueLogical,
)
sparql::LANGTAGOrIRIrefNE_strategy = st.builds(
    sparql::LANGTAGOrIRIrefNE,
)
sparql::ConditionalAndExpression_strategy = st.builds(
    sparql::ConditionalAndExpression,
)
sparql::PrefixDecl_strategy = st.builds(
    sparql::PrefixDecl,
)
sparql::SparqlQueries_strategy = st.builds(
    sparql::SparqlQueries,
)
sparql::ConditionalOrExpression_strategy = st.builds(
    sparql::ConditionalOrExpression,
)
sparql::ArgList_strategy = st.builds(
    sparql::ArgList,
)
sparql::AdditionalExpressionNE_strategy = st.builds(
    sparql::AdditionalExpressionNE,
)
BuiltInCall_strategy = st.builds(
    BuiltInCall,
)
sparql::IsURIBuiltInCallNE_strategy = st.builds(
    sparql::IsURIBuiltInCallNE,
)
sparql::IsLiteralBuiltInCallNE_strategy = st.builds(
    sparql::IsLiteralBuiltInCallNE,
)
sparql::RegexExpression_strategy = st.builds(
    sparql::RegexExpression,
)
sparql::DatatypeBuiltInCallNE_strategy = st.builds(
    sparql::DatatypeBuiltInCallNE,
)
sparql::LangmatchesBuiltInCallNE_strategy = st.builds(
    sparql::LangmatchesBuiltInCallNE,
)
sparql::IsIRIBuiltInCallNE_strategy = st.builds(
    sparql::IsIRIBuiltInCallNE,
)
sparql::IsBlankBuiltInCallNE_strategy = st.builds(
    sparql::IsBlankBuiltInCallNE,
)
sparql::LangBuiltInCallNE_strategy = st.builds(
    sparql::LangBuiltInCallNE,
)
sparql::StrBuiltInCallNE_strategy = st.builds(
    sparql::StrBuiltInCallNE,
)
sparql::Expression_strategy = st.builds(
    sparql::Expression,
)
Constraint_strategy = st.builds(
    Constraint,
)
sparql::FunctionCall_strategy = st.builds(
    sparql::FunctionCall,
)
sparql::SameTermBuiltInCallNE_strategy = st.builds(
    sparql::SameTermBuiltInCallNE,
)
sparql::BoundBuiltInCallNE_strategy = st.builds(
    sparql::BoundBuiltInCallNE,
)
TriplesNode_strategy = st.builds(
    TriplesNode,
)
sparql::BlankNodePropertyList_strategy = st.builds(
    sparql::BlankNodePropertyList,
)
sparql::Collection_strategy = st.builds(
    sparql::Collection,
)
sparql::GraphNode_strategy = st.builds(
    sparql::GraphNode,
)
sparql::Object_strategy = st.builds(
    sparql::Object,
)
sparql::ObjectList_strategy = st.builds(
    sparql::ObjectList,
)
sparql::Verb_strategy = st.builds(
    sparql::Verb,
)
GraphNode_strategy = st.builds(
    GraphNode,
)
sparql::PropertyListNotEmpty_strategy = st.builds(
    sparql::PropertyListNotEmpty,
)
sparql::PatternOrFilterNE_strategy = st.builds(
    sparql::PatternOrFilterNE,
)
sparql::VarOrTerm_strategy = st.builds(
    sparql::VarOrTerm,
)
TriplesSameSubject_strategy = st.builds(
    TriplesSameSubject,
)
sparql::TriplesSameSubjectLeftNE_strategy = st.builds(
    sparql::TriplesSameSubjectLeftNE,
)
sparql::AdditionalGGPElement_strategy = st.builds(
    sparql::AdditionalGGPElement,
)
sparql::TriplesBlock_strategy = st.builds(
    sparql::TriplesBlock,
)
GraphPatternNotTriples_strategy = st.builds(
    GraphPatternNotTriples,
)
sparql::GraphGraphPattern_strategy = st.builds(
    sparql::GraphGraphPattern,
)
sparql::GroupOrUnionGraphPattern_strategy = st.builds(
    sparql::GroupOrUnionGraphPattern,
)
sparql::OptionalGraphPattern_strategy = st.builds(
    sparql::OptionalGraphPattern,
)
PatternOrFilterNE_strategy = st.builds(
    PatternOrFilterNE,
)
sparql::Filter_strategy = st.builds(
    sparql::Filter,
)
sparql::GraphPatternNotTriples_strategy = st.builds(
    sparql::GraphPatternNotTriples,
)
sparql::TriplesNode_strategy = st.builds(
    sparql::TriplesNode,
)
sparql::TriplesSameSubjectRightNE_strategy = st.builds(
    sparql::TriplesSameSubjectRightNE,
)
IRIreference_strategy = st.builds(
    IRIreference,
)
sparql::PrefixedName_strategy = st.builds(
    sparql::PrefixedName,
)
SourceSelector_strategy = st.builds(
    SourceSelector,
)
GraphTerm_strategy = st.builds(
    GraphTerm,
)
sparql::BlankNode_strategy = st.builds(
    sparql::BlankNode,
)
sparql::NotInList_strategy = st.builds(
    sparql::NotInList,
)
sparql::GroupGraphPattern_strategy = st.builds(
    sparql::GroupGraphPattern,
)
sparql::WhereLiteral_strategy = st.builds(
    sparql::WhereLiteral,
)
sparql::SourceSelector_strategy = st.builds(
    sparql::SourceSelector,
)
GraphClauseNE_strategy = st.builds(
    GraphClauseNE,
)
sparql::NamedGraphClause_strategy = st.builds(
    sparql::NamedGraphClause,
)
sparql::DefaultGraphClause_strategy = st.builds(
    sparql::DefaultGraphClause,
)
sparql::GraphClauseNE_strategy = st.builds(
    sparql::GraphClauseNE,
)
OrderConditionRightNE_strategy = st.builds(
    OrderConditionRightNE,
)
sparql::Constraint_strategy = st.builds(
    sparql::Constraint,
)
VarOrTerm_strategy = st.builds(
    VarOrTerm,
)
sparql::GraphTerm_strategy = st.builds(
    sparql::GraphTerm,
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
sparql::RDFLiteral_strategy = st.builds(
    sparql::RDFLiteral,
)
sparql::BuiltInCall_strategy = st.builds(
    sparql::BuiltInCall,
)
sparql::BrackettedExpression_strategy = st.builds(
    sparql::BrackettedExpression,
)
sparql::NumericLiteral_strategy = st.builds(
    sparql::NumericLiteral,
)
sparql::BooleanLiteral_strategy = st.builds(
    sparql::BooleanLiteral,
)
sparql::IRIrefOrFunction_strategy = st.builds(
    sparql::IRIrefOrFunction,
)
VarOrIRIref_strategy = st.builds(
    VarOrIRIref,
)
sparql::PNAME::LN_strategy = st.builds(
    sparql::PNAME::LN,
)
sparql::IRIreference_strategy = st.builds(
    sparql::IRIreference,
)
sparql::IRI::REF_strategy = st.builds(
    sparql::IRI::REF,
    iri_ref=
        safe_text
)
sparql::Var_strategy = st.builds(
    sparql::Var,
    varname=
        safe_text
)
sparql::PNAME::NS_strategy = st.builds(
    sparql::PNAME::NS,
    pn_prefix=
        safe_text
)
Verb_strategy = st.builds(
    Verb,
)
sparql::VerbANE_strategy = st.builds(
    sparql::VerbANE,
    theA=
        safe_text
)
sparql::VarOrIRIref_strategy = st.builds(
    sparql::VarOrIRIref,
)
VariablesNE_strategy = st.builds(
    VariablesNE,
)
sparql::SomeVariablesNE_strategy = st.builds(
    sparql::SomeVariablesNE,
)
sparql::AllVariablesNE_strategy = st.builds(
    sparql::AllVariablesNE,
)
sparql::VariablesNE_strategy = st.builds(
    sparql::VariablesNE,
)
SolutionsDisplayNE_strategy = st.builds(
    SolutionsDisplayNE,
)
sparql::ReducedNE_strategy = st.builds(
    sparql::ReducedNE,
)
sparql::DistinctNE_strategy = st.builds(
    sparql::DistinctNE,
)
sparql::INTEGER_strategy = st.builds(
    sparql::INTEGER,
    integer=
        safe_text
)
sparql::OrderClause_strategy = st.builds(
    sparql::OrderClause,
)
sparql::TriplesSameSubject_strategy = st.builds(
    sparql::TriplesSameSubject,
)
sparql::OffsetClause_strategy = st.builds(
    sparql::OffsetClause,
)
sparql::LimitClause_strategy = st.builds(
    sparql::LimitClause,
)
LimitOffsetClauses_strategy = st.builds(
    LimitOffsetClauses,
)
sparql::LimitOffsetClausesRightNE_strategy = st.builds(
    sparql::LimitOffsetClausesRightNE,
)
sparql::LimitOffsetClausesLeftNE_strategy = st.builds(
    sparql::LimitOffsetClausesLeftNE,
)
sparql::OrderConditionRightNE_strategy = st.builds(
    sparql::OrderConditionRightNE,
)

@given(instance=BlankNode_strategy)
@settings(max_examples=50)
def test_blanknode_instantiation(instance):
    assert isinstance(instance, BlankNode)

@given(instance=sparql::ANON_strategy)
@settings(max_examples=50)
def test_sparql::anon_instantiation(instance):
    assert isinstance(instance, sparql::ANON)

@given(instance=sparql::BLANK::NODE::LABEL_strategy)
@settings(max_examples=50)
def test_sparql::blank::node::label_instantiation(instance):
    assert isinstance(instance, sparql::BLANK::NODE::LABEL)

@given(instance=sparql::BLANK::NODE::LABEL_strategy)
def test_sparql::blank::node::label_pn_local_type(instance):
    assert isinstance(instance.pn_local, str)


@given(instance=sparql::BLANK::NODE::LABEL_strategy)
def test_sparql::blank::node::label_pn_local_setter(instance):
    original = instance.pn_local
    instance.pn_local = original
    assert instance.pn_local == original

@given(instance=AscOrDecs_strategy)
@settings(max_examples=50)
def test_ascordecs_instantiation(instance):
    assert isinstance(instance, AscOrDecs)

@given(instance=sparql::DescendingLiteral_strategy)
@settings(max_examples=50)
def test_sparql::descendingliteral_instantiation(instance):
    assert isinstance(instance, sparql::DescendingLiteral)

@given(instance=sparql::AscendingLiteral_strategy)
@settings(max_examples=50)
def test_sparql::ascendingliteral_instantiation(instance):
    assert isinstance(instance, sparql::AscendingLiteral)

@given(instance=StringLiteral_strategy)
@settings(max_examples=50)
def test_stringliteral_instantiation(instance):
    assert isinstance(instance, StringLiteral)

@given(instance=sparql::STRING::LITERAL2_strategy)
@settings(max_examples=50)
def test_sparql::string::literal2_instantiation(instance):
    assert isinstance(instance, sparql::STRING::LITERAL2)

@given(instance=sparql::STRING::LITERAL2_strategy)
def test_sparql::string::literal2_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=sparql::STRING::LITERAL2_strategy)
def test_sparql::string::literal2_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=sparql::STRING::LITERAL::LONG2_strategy)
@settings(max_examples=50)
def test_sparql::string::literal::long2_instantiation(instance):
    assert isinstance(instance, sparql::STRING::LITERAL::LONG2)

@given(instance=sparql::STRING::LITERAL::LONG2_strategy)
def test_sparql::string::literal::long2_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=sparql::STRING::LITERAL::LONG2_strategy)
def test_sparql::string::literal::long2_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=sparql::STRING::LITERAL::LONG1_strategy)
@settings(max_examples=50)
def test_sparql::string::literal::long1_instantiation(instance):
    assert isinstance(instance, sparql::STRING::LITERAL::LONG1)

@given(instance=sparql::STRING::LITERAL::LONG1_strategy)
def test_sparql::string::literal::long1_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=sparql::STRING::LITERAL::LONG1_strategy)
def test_sparql::string::literal::long1_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=sparql::STRING::LITERAL1_strategy)
@settings(max_examples=50)
def test_sparql::string::literal1_instantiation(instance):
    assert isinstance(instance, sparql::STRING::LITERAL1)

@given(instance=sparql::STRING::LITERAL1_strategy)
def test_sparql::string::literal1_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=sparql::STRING::LITERAL1_strategy)
def test_sparql::string::literal1_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=sparql::VAR2_strategy)
@settings(max_examples=50)
def test_sparql::var2_instantiation(instance):
    assert isinstance(instance, sparql::VAR2)

@given(instance=sparql::VAR1_strategy)
@settings(max_examples=50)
def test_sparql::var1_instantiation(instance):
    assert isinstance(instance, sparql::VAR1)

@given(instance=BooleanLiteral_strategy)
@settings(max_examples=50)
def test_booleanliteral_instantiation(instance):
    assert isinstance(instance, BooleanLiteral)

@given(instance=sparql::FalseBooleanLiteralNE_strategy)
@settings(max_examples=50)
def test_sparql::falsebooleanliteralne_instantiation(instance):
    assert isinstance(instance, sparql::FalseBooleanLiteralNE)

@given(instance=sparql::TrueBooleanLiteralNE_strategy)
@settings(max_examples=50)
def test_sparql::truebooleanliteralne_instantiation(instance):
    assert isinstance(instance, sparql::TrueBooleanLiteralNE)

@given(instance=PrefixedName_strategy)
@settings(max_examples=50)
def test_prefixedname_instantiation(instance):
    assert isinstance(instance, PrefixedName)

@given(instance=sparql::StringLiteral_strategy)
@settings(max_examples=50)
def test_sparql::stringliteral_instantiation(instance):
    assert isinstance(instance, sparql::StringLiteral)

@given(instance=LANGTAGOrIRIrefNE_strategy)
@settings(max_examples=50)
def test_langtagoririrefne_instantiation(instance):
    assert isinstance(instance, LANGTAGOrIRIrefNE)

@given(instance=sparql::LANGTAG_strategy)
@settings(max_examples=50)
def test_sparql::langtag_instantiation(instance):
    assert isinstance(instance, sparql::LANGTAG)

@given(instance=sparql::LANGTAG_strategy)
def test_sparql::langtag_langtag_type(instance):
    assert isinstance(instance.langtag, str)


@given(instance=sparql::LANGTAG_strategy)
def test_sparql::langtag_langtag_setter(instance):
    original = instance.langtag
    instance.langtag = original
    assert instance.langtag == original

@given(instance=sparql::UpIRIrefNE_strategy)
@settings(max_examples=50)
def test_sparql::upirirefne_instantiation(instance):
    assert isinstance(instance, sparql::UpIRIrefNE)

@given(instance=AdditionalUnaryExpressionNE_strategy)
@settings(max_examples=50)
def test_additionalunaryexpressionne_instantiation(instance):
    assert isinstance(instance, AdditionalUnaryExpressionNE)

@given(instance=sparql::TimesAdditionalUnaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::timesadditionalunaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::TimesAdditionalUnaryExpressionNE)

@given(instance=NumericLiteral_strategy)
@settings(max_examples=50)
def test_numericliteral_instantiation(instance):
    assert isinstance(instance, NumericLiteral)

@given(instance=sparql::NumericLiteralUnsigned_strategy)
@settings(max_examples=50)
def test_sparql::numericliteralunsigned_instantiation(instance):
    assert isinstance(instance, sparql::NumericLiteralUnsigned)

@given(instance=sparql::DOUBLE_strategy)
@settings(max_examples=50)
def test_sparql::double_instantiation(instance):
    assert isinstance(instance, sparql::DOUBLE)

@given(instance=sparql::DOUBLE_strategy)
def test_sparql::double_double_type(instance):
    assert isinstance(instance.double, str)


@given(instance=sparql::DOUBLE_strategy)
def test_sparql::double_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original

@given(instance=sparql::DECIMAL_strategy)
@settings(max_examples=50)
def test_sparql::decimal_instantiation(instance):
    assert isinstance(instance, sparql::DECIMAL)

@given(instance=sparql::DECIMAL_strategy)
def test_sparql::decimal_decimal_type(instance):
    assert isinstance(instance.decimal, str)


@given(instance=sparql::DECIMAL_strategy)
def test_sparql::decimal_decimal_setter(instance):
    original = instance.decimal
    instance.decimal = original
    assert instance.decimal == original

@given(instance=AdditionalMultiplicativeExpressionNE_strategy)
@settings(max_examples=50)
def test_additionalmultiplicativeexpressionne_instantiation(instance):
    assert isinstance(instance, AdditionalMultiplicativeExpressionNE)

@given(instance=sparql::NumericLiteralNegative_strategy)
@settings(max_examples=50)
def test_sparql::numericliteralnegative_instantiation(instance):
    assert isinstance(instance, sparql::NumericLiteralNegative)

@given(instance=sparql::NumericLiteralPositive_strategy)
@settings(max_examples=50)
def test_sparql::numericliteralpositive_instantiation(instance):
    assert isinstance(instance, sparql::NumericLiteralPositive)

@given(instance=sparql::MinusMultiplicativeExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::minusmultiplicativeexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::MinusMultiplicativeExpressionNE)

@given(instance=sparql::PlusMultiplicativeExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::plusmultiplicativeexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::PlusMultiplicativeExpressionNE)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=sparql::PlusPrimaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::plusprimaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::PlusPrimaryExpressionNE)

@given(instance=sparql::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_sparql::primaryexpression_instantiation(instance):
    assert isinstance(instance, sparql::PrimaryExpression)

@given(instance=sparql::MinusPrimaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::minusprimaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::MinusPrimaryExpressionNE)

@given(instance=sparql::NotPrimaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::notprimaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::NotPrimaryExpressionNE)

@given(instance=sparql::DividedByAdditionalUnaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::dividedbyadditionalunaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::DividedByAdditionalUnaryExpressionNE)

@given(instance=AdditionalNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_additionalnumericexpressionne_instantiation(instance):
    assert isinstance(instance, AdditionalNumericExpressionNE)

@given(instance=sparql::BiggerOrEqualNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::biggerorequalnumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::BiggerOrEqualNumericExpressionNE)

@given(instance=sparql::NotEqualNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::notequalnumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::NotEqualNumericExpressionNE)

@given(instance=sparql::BiggerNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::biggernumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::BiggerNumericExpressionNE)

@given(instance=sparql::SmallerOrEqualNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::smallerorequalnumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::SmallerOrEqualNumericExpressionNE)

@given(instance=sparql::SmallerNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::smallernumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::SmallerNumericExpressionNE)

@given(instance=sparql::EqualsNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::equalsnumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::EqualsNumericExpressionNE)

@given(instance=ArgList_strategy)
@settings(max_examples=50)
def test_arglist_instantiation(instance):
    assert isinstance(instance, ArgList)

@given(instance=sparql::ArgListExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::arglistexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::ArgListExpressionNE)

@given(instance=sparql::ArgListNILNE_strategy)
@settings(max_examples=50)
def test_sparql::arglistnilne_instantiation(instance):
    assert isinstance(instance, sparql::ArgListNILNE)

@given(instance=sparql::AscOrDecs_strategy)
@settings(max_examples=50)
def test_sparql::ascordecs_instantiation(instance):
    assert isinstance(instance, sparql::AscOrDecs)

@given(instance=OrderCondition_strategy)
@settings(max_examples=50)
def test_ordercondition_instantiation(instance):
    assert isinstance(instance, OrderCondition)

@given(instance=sparql::OrderConditionLeftNE_strategy)
@settings(max_examples=50)
def test_sparql::orderconditionleftne_instantiation(instance):
    assert isinstance(instance, sparql::OrderConditionLeftNE)

@given(instance=Query_strategy)
@settings(max_examples=50)
def test_query_instantiation(instance):
    assert isinstance(instance, Query)

@given(instance=sparql::DescribeQuery_strategy)
@settings(max_examples=50)
def test_sparql::describequery_instantiation(instance):
    assert isinstance(instance, sparql::DescribeQuery)

@given(instance=sparql::ConstructQuery_strategy)
@settings(max_examples=50)
def test_sparql::constructquery_instantiation(instance):
    assert isinstance(instance, sparql::ConstructQuery)

@given(instance=sparql::AskQuery_strategy)
@settings(max_examples=50)
def test_sparql::askquery_instantiation(instance):
    assert isinstance(instance, sparql::AskQuery)

@given(instance=sparql::SelectQuery_strategy)
@settings(max_examples=50)
def test_sparql::selectquery_instantiation(instance):
    assert isinstance(instance, sparql::SelectQuery)

@given(instance=sparql::LocatedElement_strategy)
@settings(max_examples=50)
def test_sparql::locatedelement_instantiation(instance):
    assert isinstance(instance, sparql::LocatedElement)

@given(instance=sparql::LocatedElement_strategy)
def test_sparql::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=sparql::LocatedElement_strategy)
def test_sparql::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=sparql::LocatedElement_strategy)
def test_sparql::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=sparql::LocatedElement_strategy)
def test_sparql::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=sparql::LocatedElement_strategy)
def test_sparql::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=sparql::LocatedElement_strategy)
def test_sparql::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=sparql::UnaryExpression_strategy)
@settings(max_examples=50)
def test_sparql::unaryexpression_instantiation(instance):
    assert isinstance(instance, sparql::UnaryExpression)

@given(instance=sparql::WS_strategy)
@settings(max_examples=50)
def test_sparql::ws_instantiation(instance):
    assert isinstance(instance, sparql::WS)

@given(instance=sparql::WS_strategy)
def test_sparql::ws_ws_type(instance):
    assert isinstance(instance.ws, str)


@given(instance=sparql::WS_strategy)
def test_sparql::ws_ws_setter(instance):
    original = instance.ws
    instance.ws = original
    assert instance.ws == original

@given(instance=sparql::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_sparql::additiveexpression_instantiation(instance):
    assert isinstance(instance, sparql::AdditiveExpression)

@given(instance=sparql::AdditionalUnaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::additionalunaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::AdditionalUnaryExpressionNE)

@given(instance=sparql::Prologue_strategy)
@settings(max_examples=50)
def test_sparql::prologue_instantiation(instance):
    assert isinstance(instance, sparql::Prologue)

@given(instance=sparql::AdditionalValueLogicalNE_strategy)
@settings(max_examples=50)
def test_sparql::additionalvaluelogicalne_instantiation(instance):
    assert isinstance(instance, sparql::AdditionalValueLogicalNE)

@given(instance=sparql::LimitOffsetClauses_strategy)
@settings(max_examples=50)
def test_sparql::limitoffsetclauses_instantiation(instance):
    assert isinstance(instance, sparql::LimitOffsetClauses)

@given(instance=sparql::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_sparql::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, sparql::MultiplicativeExpression)

@given(instance=sparql::WhereClause_strategy)
@settings(max_examples=50)
def test_sparql::whereclause_instantiation(instance):
    assert isinstance(instance, sparql::WhereClause)

@given(instance=sparql::RelationalExpression_strategy)
@settings(max_examples=50)
def test_sparql::relationalexpression_instantiation(instance):
    assert isinstance(instance, sparql::RelationalExpression)

@given(instance=sparql::SolutionsDisplayNE_strategy)
@settings(max_examples=50)
def test_sparql::solutionsdisplayne_instantiation(instance):
    assert isinstance(instance, sparql::SolutionsDisplayNE)

@given(instance=sparql::AdditionalNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::additionalnumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::AdditionalNumericExpressionNE)

@given(instance=sparql::Query_strategy)
@settings(max_examples=50)
def test_sparql::query_instantiation(instance):
    assert isinstance(instance, sparql::Query)

@given(instance=sparql::ConstructTemplate_strategy)
@settings(max_examples=50)
def test_sparql::constructtemplate_instantiation(instance):
    assert isinstance(instance, sparql::ConstructTemplate)

@given(instance=sparql::NumericExpression_strategy)
@settings(max_examples=50)
def test_sparql::numericexpression_instantiation(instance):
    assert isinstance(instance, sparql::NumericExpression)

@given(instance=sparql::PN::PREFIX_strategy)
@settings(max_examples=50)
def test_sparql::pn::prefix_instantiation(instance):
    assert isinstance(instance, sparql::PN::PREFIX)

@given(instance=sparql::PN::PREFIX_strategy)
def test_sparql::pn::prefix_pn_prefix_type(instance):
    assert isinstance(instance.pn_prefix, str)


@given(instance=sparql::PN::PREFIX_strategy)
def test_sparql::pn::prefix_pn_prefix_setter(instance):
    original = instance.pn_prefix
    instance.pn_prefix = original
    assert instance.pn_prefix == original

@given(instance=sparql::OrderCondition_strategy)
@settings(max_examples=50)
def test_sparql::ordercondition_instantiation(instance):
    assert isinstance(instance, sparql::OrderCondition)

@given(instance=sparql::SolutionModifier_strategy)
@settings(max_examples=50)
def test_sparql::solutionmodifier_instantiation(instance):
    assert isinstance(instance, sparql::SolutionModifier)

@given(instance=sparql::AdditionalConditionalAndExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::additionalconditionalandexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::AdditionalConditionalAndExpressionNE)

@given(instance=sparql::DatasetClause_strategy)
@settings(max_examples=50)
def test_sparql::datasetclause_instantiation(instance):
    assert isinstance(instance, sparql::DatasetClause)

@given(instance=sparql::BaseDecl_strategy)
@settings(max_examples=50)
def test_sparql::basedecl_instantiation(instance):
    assert isinstance(instance, sparql::BaseDecl)

@given(instance=sparql::VARNAME_strategy)
@settings(max_examples=50)
def test_sparql::varname_instantiation(instance):
    assert isinstance(instance, sparql::VARNAME)

@given(instance=sparql::VARNAME_strategy)
def test_sparql::varname_varname_type(instance):
    assert isinstance(instance.varname, str)


@given(instance=sparql::VARNAME_strategy)
def test_sparql::varname_varname_setter(instance):
    original = instance.varname
    instance.varname = original
    assert instance.varname == original

@given(instance=sparql::AdditionalMultiplicativeExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::additionalmultiplicativeexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::AdditionalMultiplicativeExpressionNE)

@given(instance=sparql::PN::LOCAL_strategy)
@settings(max_examples=50)
def test_sparql::pn::local_instantiation(instance):
    assert isinstance(instance, sparql::PN::LOCAL)

@given(instance=sparql::PN::LOCAL_strategy)
def test_sparql::pn::local_pn_local_type(instance):
    assert isinstance(instance.pn_local, str)


@given(instance=sparql::PN::LOCAL_strategy)
def test_sparql::pn::local_pn_local_setter(instance):
    original = instance.pn_local
    instance.pn_local = original
    assert instance.pn_local == original

@given(instance=sparql::ValueLogical_strategy)
@settings(max_examples=50)
def test_sparql::valuelogical_instantiation(instance):
    assert isinstance(instance, sparql::ValueLogical)

@given(instance=sparql::LANGTAGOrIRIrefNE_strategy)
@settings(max_examples=50)
def test_sparql::langtagoririrefne_instantiation(instance):
    assert isinstance(instance, sparql::LANGTAGOrIRIrefNE)

@given(instance=sparql::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_sparql::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, sparql::ConditionalAndExpression)

@given(instance=sparql::PrefixDecl_strategy)
@settings(max_examples=50)
def test_sparql::prefixdecl_instantiation(instance):
    assert isinstance(instance, sparql::PrefixDecl)

@given(instance=sparql::SparqlQueries_strategy)
@settings(max_examples=50)
def test_sparql::sparqlqueries_instantiation(instance):
    assert isinstance(instance, sparql::SparqlQueries)

@given(instance=sparql::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_sparql::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, sparql::ConditionalOrExpression)

@given(instance=sparql::ArgList_strategy)
@settings(max_examples=50)
def test_sparql::arglist_instantiation(instance):
    assert isinstance(instance, sparql::ArgList)

@given(instance=sparql::AdditionalExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql::additionalexpressionne_instantiation(instance):
    assert isinstance(instance, sparql::AdditionalExpressionNE)

@given(instance=BuiltInCall_strategy)
@settings(max_examples=50)
def test_builtincall_instantiation(instance):
    assert isinstance(instance, BuiltInCall)

@given(instance=sparql::IsURIBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql::isuribuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql::IsURIBuiltInCallNE)

@given(instance=sparql::IsLiteralBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql::isliteralbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql::IsLiteralBuiltInCallNE)

@given(instance=sparql::RegexExpression_strategy)
@settings(max_examples=50)
def test_sparql::regexexpression_instantiation(instance):
    assert isinstance(instance, sparql::RegexExpression)

@given(instance=sparql::DatatypeBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql::datatypebuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql::DatatypeBuiltInCallNE)

@given(instance=sparql::LangmatchesBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql::langmatchesbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql::LangmatchesBuiltInCallNE)

@given(instance=sparql::IsIRIBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql::isiribuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql::IsIRIBuiltInCallNE)

@given(instance=sparql::IsBlankBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql::isblankbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql::IsBlankBuiltInCallNE)

@given(instance=sparql::LangBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql::langbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql::LangBuiltInCallNE)

@given(instance=sparql::StrBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql::strbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql::StrBuiltInCallNE)

@given(instance=sparql::Expression_strategy)
@settings(max_examples=50)
def test_sparql::expression_instantiation(instance):
    assert isinstance(instance, sparql::Expression)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=sparql::FunctionCall_strategy)
@settings(max_examples=50)
def test_sparql::functioncall_instantiation(instance):
    assert isinstance(instance, sparql::FunctionCall)

@given(instance=sparql::SameTermBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql::sametermbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql::SameTermBuiltInCallNE)

@given(instance=sparql::BoundBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql::boundbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql::BoundBuiltInCallNE)

@given(instance=TriplesNode_strategy)
@settings(max_examples=50)
def test_triplesnode_instantiation(instance):
    assert isinstance(instance, TriplesNode)

@given(instance=sparql::BlankNodePropertyList_strategy)
@settings(max_examples=50)
def test_sparql::blanknodepropertylist_instantiation(instance):
    assert isinstance(instance, sparql::BlankNodePropertyList)

@given(instance=sparql::Collection_strategy)
@settings(max_examples=50)
def test_sparql::collection_instantiation(instance):
    assert isinstance(instance, sparql::Collection)

@given(instance=sparql::GraphNode_strategy)
@settings(max_examples=50)
def test_sparql::graphnode_instantiation(instance):
    assert isinstance(instance, sparql::GraphNode)

@given(instance=sparql::Object_strategy)
@settings(max_examples=50)
def test_sparql::object_instantiation(instance):
    assert isinstance(instance, sparql::Object)

@given(instance=sparql::ObjectList_strategy)
@settings(max_examples=50)
def test_sparql::objectlist_instantiation(instance):
    assert isinstance(instance, sparql::ObjectList)

@given(instance=sparql::Verb_strategy)
@settings(max_examples=50)
def test_sparql::verb_instantiation(instance):
    assert isinstance(instance, sparql::Verb)

@given(instance=GraphNode_strategy)
@settings(max_examples=50)
def test_graphnode_instantiation(instance):
    assert isinstance(instance, GraphNode)

@given(instance=sparql::PropertyListNotEmpty_strategy)
@settings(max_examples=50)
def test_sparql::propertylistnotempty_instantiation(instance):
    assert isinstance(instance, sparql::PropertyListNotEmpty)

@given(instance=sparql::PatternOrFilterNE_strategy)
@settings(max_examples=50)
def test_sparql::patternorfilterne_instantiation(instance):
    assert isinstance(instance, sparql::PatternOrFilterNE)

@given(instance=sparql::VarOrTerm_strategy)
@settings(max_examples=50)
def test_sparql::varorterm_instantiation(instance):
    assert isinstance(instance, sparql::VarOrTerm)

@given(instance=TriplesSameSubject_strategy)
@settings(max_examples=50)
def test_triplessamesubject_instantiation(instance):
    assert isinstance(instance, TriplesSameSubject)

@given(instance=sparql::TriplesSameSubjectLeftNE_strategy)
@settings(max_examples=50)
def test_sparql::triplessamesubjectleftne_instantiation(instance):
    assert isinstance(instance, sparql::TriplesSameSubjectLeftNE)

@given(instance=sparql::AdditionalGGPElement_strategy)
@settings(max_examples=50)
def test_sparql::additionalggpelement_instantiation(instance):
    assert isinstance(instance, sparql::AdditionalGGPElement)

@given(instance=sparql::TriplesBlock_strategy)
@settings(max_examples=50)
def test_sparql::triplesblock_instantiation(instance):
    assert isinstance(instance, sparql::TriplesBlock)

@given(instance=GraphPatternNotTriples_strategy)
@settings(max_examples=50)
def test_graphpatternnottriples_instantiation(instance):
    assert isinstance(instance, GraphPatternNotTriples)

@given(instance=sparql::GraphGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql::graphgraphpattern_instantiation(instance):
    assert isinstance(instance, sparql::GraphGraphPattern)

@given(instance=sparql::GroupOrUnionGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql::grouporuniongraphpattern_instantiation(instance):
    assert isinstance(instance, sparql::GroupOrUnionGraphPattern)

@given(instance=sparql::OptionalGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql::optionalgraphpattern_instantiation(instance):
    assert isinstance(instance, sparql::OptionalGraphPattern)

@given(instance=PatternOrFilterNE_strategy)
@settings(max_examples=50)
def test_patternorfilterne_instantiation(instance):
    assert isinstance(instance, PatternOrFilterNE)

@given(instance=sparql::Filter_strategy)
@settings(max_examples=50)
def test_sparql::filter_instantiation(instance):
    assert isinstance(instance, sparql::Filter)

@given(instance=sparql::GraphPatternNotTriples_strategy)
@settings(max_examples=50)
def test_sparql::graphpatternnottriples_instantiation(instance):
    assert isinstance(instance, sparql::GraphPatternNotTriples)

@given(instance=sparql::TriplesNode_strategy)
@settings(max_examples=50)
def test_sparql::triplesnode_instantiation(instance):
    assert isinstance(instance, sparql::TriplesNode)

@given(instance=sparql::TriplesSameSubjectRightNE_strategy)
@settings(max_examples=50)
def test_sparql::triplessamesubjectrightne_instantiation(instance):
    assert isinstance(instance, sparql::TriplesSameSubjectRightNE)

@given(instance=IRIreference_strategy)
@settings(max_examples=50)
def test_irireference_instantiation(instance):
    assert isinstance(instance, IRIreference)

@given(instance=sparql::PrefixedName_strategy)
@settings(max_examples=50)
def test_sparql::prefixedname_instantiation(instance):
    assert isinstance(instance, sparql::PrefixedName)

@given(instance=SourceSelector_strategy)
@settings(max_examples=50)
def test_sourceselector_instantiation(instance):
    assert isinstance(instance, SourceSelector)

@given(instance=GraphTerm_strategy)
@settings(max_examples=50)
def test_graphterm_instantiation(instance):
    assert isinstance(instance, GraphTerm)

@given(instance=sparql::BlankNode_strategy)
@settings(max_examples=50)
def test_sparql::blanknode_instantiation(instance):
    assert isinstance(instance, sparql::BlankNode)

@given(instance=sparql::NotInList_strategy)
@settings(max_examples=50)
def test_sparql::notinlist_instantiation(instance):
    assert isinstance(instance, sparql::NotInList)

@given(instance=sparql::GroupGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql::groupgraphpattern_instantiation(instance):
    assert isinstance(instance, sparql::GroupGraphPattern)

@given(instance=sparql::WhereLiteral_strategy)
@settings(max_examples=50)
def test_sparql::whereliteral_instantiation(instance):
    assert isinstance(instance, sparql::WhereLiteral)

@given(instance=sparql::SourceSelector_strategy)
@settings(max_examples=50)
def test_sparql::sourceselector_instantiation(instance):
    assert isinstance(instance, sparql::SourceSelector)

@given(instance=GraphClauseNE_strategy)
@settings(max_examples=50)
def test_graphclausene_instantiation(instance):
    assert isinstance(instance, GraphClauseNE)

@given(instance=sparql::NamedGraphClause_strategy)
@settings(max_examples=50)
def test_sparql::namedgraphclause_instantiation(instance):
    assert isinstance(instance, sparql::NamedGraphClause)

@given(instance=sparql::DefaultGraphClause_strategy)
@settings(max_examples=50)
def test_sparql::defaultgraphclause_instantiation(instance):
    assert isinstance(instance, sparql::DefaultGraphClause)

@given(instance=sparql::GraphClauseNE_strategy)
@settings(max_examples=50)
def test_sparql::graphclausene_instantiation(instance):
    assert isinstance(instance, sparql::GraphClauseNE)

@given(instance=OrderConditionRightNE_strategy)
@settings(max_examples=50)
def test_orderconditionrightne_instantiation(instance):
    assert isinstance(instance, OrderConditionRightNE)

@given(instance=sparql::Constraint_strategy)
@settings(max_examples=50)
def test_sparql::constraint_instantiation(instance):
    assert isinstance(instance, sparql::Constraint)

@given(instance=VarOrTerm_strategy)
@settings(max_examples=50)
def test_varorterm_instantiation(instance):
    assert isinstance(instance, VarOrTerm)

@given(instance=sparql::GraphTerm_strategy)
@settings(max_examples=50)
def test_sparql::graphterm_instantiation(instance):
    assert isinstance(instance, sparql::GraphTerm)

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=sparql::RDFLiteral_strategy)
@settings(max_examples=50)
def test_sparql::rdfliteral_instantiation(instance):
    assert isinstance(instance, sparql::RDFLiteral)

@given(instance=sparql::BuiltInCall_strategy)
@settings(max_examples=50)
def test_sparql::builtincall_instantiation(instance):
    assert isinstance(instance, sparql::BuiltInCall)

@given(instance=sparql::BrackettedExpression_strategy)
@settings(max_examples=50)
def test_sparql::brackettedexpression_instantiation(instance):
    assert isinstance(instance, sparql::BrackettedExpression)

@given(instance=sparql::NumericLiteral_strategy)
@settings(max_examples=50)
def test_sparql::numericliteral_instantiation(instance):
    assert isinstance(instance, sparql::NumericLiteral)

@given(instance=sparql::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_sparql::booleanliteral_instantiation(instance):
    assert isinstance(instance, sparql::BooleanLiteral)

@given(instance=sparql::IRIrefOrFunction_strategy)
@settings(max_examples=50)
def test_sparql::irireforfunction_instantiation(instance):
    assert isinstance(instance, sparql::IRIrefOrFunction)

@given(instance=VarOrIRIref_strategy)
@settings(max_examples=50)
def test_varoririref_instantiation(instance):
    assert isinstance(instance, VarOrIRIref)

@given(instance=sparql::PNAME::LN_strategy)
@settings(max_examples=50)
def test_sparql::pname::ln_instantiation(instance):
    assert isinstance(instance, sparql::PNAME::LN)

@given(instance=sparql::IRIreference_strategy)
@settings(max_examples=50)
def test_sparql::irireference_instantiation(instance):
    assert isinstance(instance, sparql::IRIreference)

@given(instance=sparql::IRI::REF_strategy)
@settings(max_examples=50)
def test_sparql::iri::ref_instantiation(instance):
    assert isinstance(instance, sparql::IRI::REF)

@given(instance=sparql::IRI::REF_strategy)
def test_sparql::iri::ref_iri_ref_type(instance):
    assert isinstance(instance.iri_ref, str)


@given(instance=sparql::IRI::REF_strategy)
def test_sparql::iri::ref_iri_ref_setter(instance):
    original = instance.iri_ref
    instance.iri_ref = original
    assert instance.iri_ref == original

@given(instance=sparql::Var_strategy)
@settings(max_examples=50)
def test_sparql::var_instantiation(instance):
    assert isinstance(instance, sparql::Var)

@given(instance=sparql::Var_strategy)
def test_sparql::var_varname_type(instance):
    assert isinstance(instance.varname, str)


@given(instance=sparql::Var_strategy)
def test_sparql::var_varname_setter(instance):
    original = instance.varname
    instance.varname = original
    assert instance.varname == original

@given(instance=sparql::PNAME::NS_strategy)
@settings(max_examples=50)
def test_sparql::pname::ns_instantiation(instance):
    assert isinstance(instance, sparql::PNAME::NS)

@given(instance=sparql::PNAME::NS_strategy)
def test_sparql::pname::ns_pn_prefix_type(instance):
    assert isinstance(instance.pn_prefix, str)


@given(instance=sparql::PNAME::NS_strategy)
def test_sparql::pname::ns_pn_prefix_setter(instance):
    original = instance.pn_prefix
    instance.pn_prefix = original
    assert instance.pn_prefix == original

@given(instance=Verb_strategy)
@settings(max_examples=50)
def test_verb_instantiation(instance):
    assert isinstance(instance, Verb)

@given(instance=sparql::VerbANE_strategy)
@settings(max_examples=50)
def test_sparql::verbane_instantiation(instance):
    assert isinstance(instance, sparql::VerbANE)

@given(instance=sparql::VerbANE_strategy)
def test_sparql::verbane_theA_type(instance):
    assert isinstance(instance.theA, str)


@given(instance=sparql::VerbANE_strategy)
def test_sparql::verbane_theA_setter(instance):
    original = instance.theA
    instance.theA = original
    assert instance.theA == original

@given(instance=sparql::VarOrIRIref_strategy)
@settings(max_examples=50)
def test_sparql::varoririref_instantiation(instance):
    assert isinstance(instance, sparql::VarOrIRIref)

@given(instance=VariablesNE_strategy)
@settings(max_examples=50)
def test_variablesne_instantiation(instance):
    assert isinstance(instance, VariablesNE)

@given(instance=sparql::SomeVariablesNE_strategy)
@settings(max_examples=50)
def test_sparql::somevariablesne_instantiation(instance):
    assert isinstance(instance, sparql::SomeVariablesNE)

@given(instance=sparql::AllVariablesNE_strategy)
@settings(max_examples=50)
def test_sparql::allvariablesne_instantiation(instance):
    assert isinstance(instance, sparql::AllVariablesNE)

@given(instance=sparql::VariablesNE_strategy)
@settings(max_examples=50)
def test_sparql::variablesne_instantiation(instance):
    assert isinstance(instance, sparql::VariablesNE)

@given(instance=SolutionsDisplayNE_strategy)
@settings(max_examples=50)
def test_solutionsdisplayne_instantiation(instance):
    assert isinstance(instance, SolutionsDisplayNE)

@given(instance=sparql::ReducedNE_strategy)
@settings(max_examples=50)
def test_sparql::reducedne_instantiation(instance):
    assert isinstance(instance, sparql::ReducedNE)

@given(instance=sparql::DistinctNE_strategy)
@settings(max_examples=50)
def test_sparql::distinctne_instantiation(instance):
    assert isinstance(instance, sparql::DistinctNE)

@given(instance=sparql::INTEGER_strategy)
@settings(max_examples=50)
def test_sparql::integer_instantiation(instance):
    assert isinstance(instance, sparql::INTEGER)

@given(instance=sparql::INTEGER_strategy)
def test_sparql::integer_integer_type(instance):
    assert isinstance(instance.integer, str)


@given(instance=sparql::INTEGER_strategy)
def test_sparql::integer_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original

@given(instance=sparql::OrderClause_strategy)
@settings(max_examples=50)
def test_sparql::orderclause_instantiation(instance):
    assert isinstance(instance, sparql::OrderClause)

@given(instance=sparql::TriplesSameSubject_strategy)
@settings(max_examples=50)
def test_sparql::triplessamesubject_instantiation(instance):
    assert isinstance(instance, sparql::TriplesSameSubject)

@given(instance=sparql::OffsetClause_strategy)
@settings(max_examples=50)
def test_sparql::offsetclause_instantiation(instance):
    assert isinstance(instance, sparql::OffsetClause)

@given(instance=sparql::LimitClause_strategy)
@settings(max_examples=50)
def test_sparql::limitclause_instantiation(instance):
    assert isinstance(instance, sparql::LimitClause)

@given(instance=LimitOffsetClauses_strategy)
@settings(max_examples=50)
def test_limitoffsetclauses_instantiation(instance):
    assert isinstance(instance, LimitOffsetClauses)

@given(instance=sparql::LimitOffsetClausesRightNE_strategy)
@settings(max_examples=50)
def test_sparql::limitoffsetclausesrightne_instantiation(instance):
    assert isinstance(instance, sparql::LimitOffsetClausesRightNE)

@given(instance=sparql::LimitOffsetClausesLeftNE_strategy)
@settings(max_examples=50)
def test_sparql::limitoffsetclausesleftne_instantiation(instance):
    assert isinstance(instance, sparql::LimitOffsetClausesLeftNE)

@given(instance=sparql::OrderConditionRightNE_strategy)
@settings(max_examples=50)
def test_sparql::orderconditionrightne_instantiation(instance):
    assert isinstance(instance, sparql::OrderConditionRightNE)
