import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BlankNode,
    sparql_ANON,
    sparql_BLANK_NODE_LABEL,
    AscOrDecs,
    sparql_DescendingLiteral,
    sparql_AscendingLiteral,
    StringLiteral,
    sparql_STRING_LITERAL_LONG1,
    sparql_STRING_LITERAL_LONG2,
    sparql_STRING_LITERAL2,
    sparql_STRING_LITERAL1,
    sparql_VAR2,
    sparql_VAR1,
    BooleanLiteral,
    sparql_FalseBooleanLiteralNE,
    sparql_TrueBooleanLiteralNE,
    PrefixedName,
    sparql_StringLiteral,
    LANGTAGOrIRIrefNE,
    sparql_LANGTAG,
    sparql_UpIRIrefNE,
    AdditionalUnaryExpressionNE,
    sparql_TimesAdditionalUnaryExpressionNE,
    NumericLiteral,
    sparql_DOUBLE,
    sparql_DECIMAL,
    sparql_NumericLiteralUnsigned,
    AdditionalMultiplicativeExpressionNE,
    sparql_MinusMultiplicativeExpressionNE,
    sparql_NumericLiteralNegative,
    sparql_NumericLiteralPositive,
    sparql_PlusMultiplicativeExpressionNE,
    UnaryExpression,
    sparql_PrimaryExpression,
    sparql_MinusPrimaryExpressionNE,
    sparql_PlusPrimaryExpressionNE,
    sparql_NotPrimaryExpressionNE,
    sparql_DividedByAdditionalUnaryExpressionNE,
    AdditionalNumericExpressionNE,
    sparql_SmallerOrEqualNumericExpressionNE,
    sparql_BiggerNumericExpressionNE,
    sparql_SmallerNumericExpressionNE,
    sparql_BiggerOrEqualNumericExpressionNE,
    sparql_NotEqualNumericExpressionNE,
    sparql_EqualsNumericExpressionNE,
    ArgList,
    sparql_ArgListExpressionNE,
    sparql_ArgListNILNE,
    BuiltInCall,
    sparql_IsBlankBuiltInCallNE,
    sparql_RegexExpression,
    sparql_LangmatchesBuiltInCallNE,
    sparql_IsURIBuiltInCallNE,
    sparql_LangBuiltInCallNE,
    sparql_DatatypeBuiltInCallNE,
    sparql_IsLiteralBuiltInCallNE,
    sparql_IsIRIBuiltInCallNE,
    sparql_StrBuiltInCallNE,
    Constraint,
    sparql_FunctionCall,
    sparql_SameTermBuiltInCallNE,
    sparql_BoundBuiltInCallNE,
    TriplesNode,
    sparql_BlankNodePropertyList,
    sparql_Collection,
    GraphNode,
    sparql_PatternOrFilterNE,
    sparql_VarOrTerm,
    TriplesSameSubject,
    sparql_TriplesSameSubjectLeftNE,
    sparql_TriplesBlock,
    GraphPatternNotTriples,
    sparql_GraphGraphPattern,
    sparql_GroupOrUnionGraphPattern,
    sparql_OptionalGraphPattern,
    PatternOrFilterNE,
    sparql_Filter,
    sparql_GraphPatternNotTriples,
    sparql_TriplesNode,
    sparql_TriplesSameSubjectRightNE,
    IRIreference,
    sparql_PrefixedName,
    SourceSelector,
    GraphTerm,
    sparql_BlankNode,
    sparql_NotInList,
    sparql_WhereLiteral,
    GraphClauseNE,
    sparql_NamedGraphClause,
    sparql_DefaultGraphClause,
    OrderConditionRightNE,
    sparql_Constraint,
    VarOrTerm,
    sparql_GraphTerm,
    PrimaryExpression,
    sparql_RDFLiteral,
    sparql_BuiltInCall,
    sparql_IRIrefOrFunction,
    sparql_NumericLiteral,
    sparql_BooleanLiteral,
    VarOrIRIref,
    sparql_PNAME_LN,
    sparql_IRIreference,
    Verb,
    sparql_VerbANE,
    VariablesNE,
    sparql_SomeVariablesNE,
    sparql_AllVariablesNE,
    SolutionsDisplayNE,
    sparql_ReducedNE,
    sparql_DistinctNE,
    sparql_INTEGER,
    LimitOffsetClauses,
    sparql_LimitOffsetClausesRightNE,
    sparql_LimitOffsetClausesLeftNE,
    sparql_BrackettedExpression,
    sparql_AscOrDecs,
    OrderCondition,
    sparql_OrderConditionRightNE,
    sparql_OrderConditionLeftNE,
    sparql_VarOrIRIref,
    Query,
    sparql_AskQuery,
    sparql_DescribeQuery,
    sparql_ConstructQuery,
    sparql_SelectQuery,
    sparql_PNAME_NS,
    sparql_Var,
    sparql_LocatedElement,
    sparql_IRI_REF,
    LocatedElement,
    sparql_OffsetClause,
    sparql_TriplesSameSubject,
    sparql_PropertyListNotEmpty,
    sparql_OrderCondition,
    sparql_WS,
    sparql_AdditionalNumericExpressionNE,
    sparql_Object,
    sparql_AdditionalExpressionNE,
    sparql_AdditiveExpression,
    sparql_VariablesNE,
    sparql_Prologue,
    sparql_PrefixDecl,
    sparql_AdditionalConditionalAndExpressionNE,
    sparql_ArgList,
    sparql_Query,
    sparql_LANGTAGOrIRIrefNE,
    sparql_WhereClause,
    sparql_OrderClause,
    sparql_VARNAME,
    sparql_NumericExpression,
    sparql_DatasetClause,
    sparql_PN_LOCAL,
    sparql_AdditionalMultiplicativeExpressionNE,
    sparql_LimitOffsetClauses,
    sparql_PN_PREFIX,
    sparql_AdditionalUnaryExpressionNE,
    sparql_UnaryExpression,
    sparql_SolutionsDisplayNE,
    sparql_LimitClause,
    sparql_BaseDecl,
    sparql_ValueLogical,
    sparql_ObjectList,
    sparql_GraphClauseNE,
    sparql_Expression,
    sparql_SolutionModifier,
    sparql_GraphNode,
    sparql_AdditionalGGPElement,
    sparql_RelationalExpression,
    sparql_ConditionalAndExpression,
    sparql_ConstructTemplate,
    sparql_MultiplicativeExpression,
    sparql_SourceSelector,
    sparql_AdditionalValueLogicalNE,
    sparql_GroupGraphPattern,
    sparql_ConditionalOrExpression,
    sparql_Verb,
    sparql_SparqlQueries,
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



def test_sparql_anon_is_not_abstract():
    assert not inspect.isabstract(sparql_ANON)


def test_sparql_anon_constructor_exists():
    assert callable(sparql_ANON.__init__)


def test_sparql_anon_constructor_args():
    sig = inspect.signature(sparql_ANON.__init__)
    params = list(sig.parameters.keys())



def test_sparql_blank_node_label_is_not_abstract():
    assert not inspect.isabstract(sparql_BLANK_NODE_LABEL)


def test_sparql_blank_node_label_constructor_exists():
    assert callable(sparql_BLANK_NODE_LABEL.__init__)


def test_sparql_blank_node_label_constructor_args():
    sig = inspect.signature(sparql_BLANK_NODE_LABEL.__init__)
    params = list(sig.parameters.keys())
    assert "pn_local" in params, "Missing parameter 'pn_local'"

def test_sparql_blank_node_label_has_pn_local():
    assert hasattr(sparql_BLANK_NODE_LABEL, "pn_local")
    descriptor = None
    for klass in sparql_BLANK_NODE_LABEL.__mro__:
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



def test_sparql_descendingliteral_is_not_abstract():
    assert not inspect.isabstract(sparql_DescendingLiteral)


def test_sparql_descendingliteral_constructor_exists():
    assert callable(sparql_DescendingLiteral.__init__)


def test_sparql_descendingliteral_constructor_args():
    sig = inspect.signature(sparql_DescendingLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql_ascendingliteral_is_not_abstract():
    assert not inspect.isabstract(sparql_AscendingLiteral)


def test_sparql_ascendingliteral_constructor_exists():
    assert callable(sparql_AscendingLiteral.__init__)


def test_sparql_ascendingliteral_constructor_args():
    sig = inspect.signature(sparql_AscendingLiteral.__init__)
    params = list(sig.parameters.keys())



def test_stringliteral_is_not_abstract():
    assert not inspect.isabstract(StringLiteral)


def test_stringliteral_constructor_exists():
    assert callable(StringLiteral.__init__)


def test_stringliteral_constructor_args():
    sig = inspect.signature(StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql_string_literal_long1_is_not_abstract():
    assert not inspect.isabstract(sparql_STRING_LITERAL_LONG1)


def test_sparql_string_literal_long1_constructor_exists():
    assert callable(sparql_STRING_LITERAL_LONG1.__init__)


def test_sparql_string_literal_long1_constructor_args():
    sig = inspect.signature(sparql_STRING_LITERAL_LONG1.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_sparql_string_literal_long1_has_string():
    assert hasattr(sparql_STRING_LITERAL_LONG1, "string")
    descriptor = None
    for klass in sparql_STRING_LITERAL_LONG1.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_sparql_string_literal_long2_is_not_abstract():
    assert not inspect.isabstract(sparql_STRING_LITERAL_LONG2)


def test_sparql_string_literal_long2_constructor_exists():
    assert callable(sparql_STRING_LITERAL_LONG2.__init__)


def test_sparql_string_literal_long2_constructor_args():
    sig = inspect.signature(sparql_STRING_LITERAL_LONG2.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_sparql_string_literal_long2_has_string():
    assert hasattr(sparql_STRING_LITERAL_LONG2, "string")
    descriptor = None
    for klass in sparql_STRING_LITERAL_LONG2.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_sparql_string_literal2_is_not_abstract():
    assert not inspect.isabstract(sparql_STRING_LITERAL2)


def test_sparql_string_literal2_constructor_exists():
    assert callable(sparql_STRING_LITERAL2.__init__)


def test_sparql_string_literal2_constructor_args():
    sig = inspect.signature(sparql_STRING_LITERAL2.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_sparql_string_literal2_has_string():
    assert hasattr(sparql_STRING_LITERAL2, "string")
    descriptor = None
    for klass in sparql_STRING_LITERAL2.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_sparql_string_literal1_is_not_abstract():
    assert not inspect.isabstract(sparql_STRING_LITERAL1)


def test_sparql_string_literal1_constructor_exists():
    assert callable(sparql_STRING_LITERAL1.__init__)


def test_sparql_string_literal1_constructor_args():
    sig = inspect.signature(sparql_STRING_LITERAL1.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_sparql_string_literal1_has_string():
    assert hasattr(sparql_STRING_LITERAL1, "string")
    descriptor = None
    for klass in sparql_STRING_LITERAL1.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_sparql_var2_is_not_abstract():
    assert not inspect.isabstract(sparql_VAR2)


def test_sparql_var2_constructor_exists():
    assert callable(sparql_VAR2.__init__)


def test_sparql_var2_constructor_args():
    sig = inspect.signature(sparql_VAR2.__init__)
    params = list(sig.parameters.keys())



def test_sparql_var1_is_not_abstract():
    assert not inspect.isabstract(sparql_VAR1)


def test_sparql_var1_constructor_exists():
    assert callable(sparql_VAR1.__init__)


def test_sparql_var1_constructor_args():
    sig = inspect.signature(sparql_VAR1.__init__)
    params = list(sig.parameters.keys())



def test_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteral)


def test_booleanliteral_constructor_exists():
    assert callable(BooleanLiteral.__init__)


def test_booleanliteral_constructor_args():
    sig = inspect.signature(BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql_falsebooleanliteralne_is_not_abstract():
    assert not inspect.isabstract(sparql_FalseBooleanLiteralNE)


def test_sparql_falsebooleanliteralne_constructor_exists():
    assert callable(sparql_FalseBooleanLiteralNE.__init__)


def test_sparql_falsebooleanliteralne_constructor_args():
    sig = inspect.signature(sparql_FalseBooleanLiteralNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_truebooleanliteralne_is_not_abstract():
    assert not inspect.isabstract(sparql_TrueBooleanLiteralNE)


def test_sparql_truebooleanliteralne_constructor_exists():
    assert callable(sparql_TrueBooleanLiteralNE.__init__)


def test_sparql_truebooleanliteralne_constructor_args():
    sig = inspect.signature(sparql_TrueBooleanLiteralNE.__init__)
    params = list(sig.parameters.keys())



def test_prefixedname_is_not_abstract():
    assert not inspect.isabstract(PrefixedName)


def test_prefixedname_constructor_exists():
    assert callable(PrefixedName.__init__)


def test_prefixedname_constructor_args():
    sig = inspect.signature(PrefixedName.__init__)
    params = list(sig.parameters.keys())



def test_sparql_stringliteral_is_not_abstract():
    assert not inspect.isabstract(sparql_StringLiteral)


def test_sparql_stringliteral_constructor_exists():
    assert callable(sparql_StringLiteral.__init__)


def test_sparql_stringliteral_constructor_args():
    sig = inspect.signature(sparql_StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_langtagoririrefne_is_not_abstract():
    assert not inspect.isabstract(LANGTAGOrIRIrefNE)


def test_langtagoririrefne_constructor_exists():
    assert callable(LANGTAGOrIRIrefNE.__init__)


def test_langtagoririrefne_constructor_args():
    sig = inspect.signature(LANGTAGOrIRIrefNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_langtag_is_not_abstract():
    assert not inspect.isabstract(sparql_LANGTAG)


def test_sparql_langtag_constructor_exists():
    assert callable(sparql_LANGTAG.__init__)


def test_sparql_langtag_constructor_args():
    sig = inspect.signature(sparql_LANGTAG.__init__)
    params = list(sig.parameters.keys())
    assert "langtag" in params, "Missing parameter 'langtag'"

def test_sparql_langtag_has_langtag():
    assert hasattr(sparql_LANGTAG, "langtag")
    descriptor = None
    for klass in sparql_LANGTAG.__mro__:
        if "langtag" in klass.__dict__:
            descriptor = klass.__dict__["langtag"]
            break
    assert isinstance(descriptor, property)



def test_sparql_upirirefne_is_not_abstract():
    assert not inspect.isabstract(sparql_UpIRIrefNE)


def test_sparql_upirirefne_constructor_exists():
    assert callable(sparql_UpIRIrefNE.__init__)


def test_sparql_upirirefne_constructor_args():
    sig = inspect.signature(sparql_UpIRIrefNE.__init__)
    params = list(sig.parameters.keys())



def test_additionalunaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(AdditionalUnaryExpressionNE)


def test_additionalunaryexpressionne_constructor_exists():
    assert callable(AdditionalUnaryExpressionNE.__init__)


def test_additionalunaryexpressionne_constructor_args():
    sig = inspect.signature(AdditionalUnaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_timesadditionalunaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_TimesAdditionalUnaryExpressionNE)


def test_sparql_timesadditionalunaryexpressionne_constructor_exists():
    assert callable(sparql_TimesAdditionalUnaryExpressionNE.__init__)


def test_sparql_timesadditionalunaryexpressionne_constructor_args():
    sig = inspect.signature(sparql_TimesAdditionalUnaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_numericliteral_is_not_abstract():
    assert not inspect.isabstract(NumericLiteral)


def test_numericliteral_constructor_exists():
    assert callable(NumericLiteral.__init__)


def test_numericliteral_constructor_args():
    sig = inspect.signature(NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql_double_is_not_abstract():
    assert not inspect.isabstract(sparql_DOUBLE)


def test_sparql_double_constructor_exists():
    assert callable(sparql_DOUBLE.__init__)


def test_sparql_double_constructor_args():
    sig = inspect.signature(sparql_DOUBLE.__init__)
    params = list(sig.parameters.keys())
    assert "double" in params, "Missing parameter 'double'"

def test_sparql_double_has_double():
    assert hasattr(sparql_DOUBLE, "double")
    descriptor = None
    for klass in sparql_DOUBLE.__mro__:
        if "double" in klass.__dict__:
            descriptor = klass.__dict__["double"]
            break
    assert isinstance(descriptor, property)



def test_sparql_decimal_is_not_abstract():
    assert not inspect.isabstract(sparql_DECIMAL)


def test_sparql_decimal_constructor_exists():
    assert callable(sparql_DECIMAL.__init__)


def test_sparql_decimal_constructor_args():
    sig = inspect.signature(sparql_DECIMAL.__init__)
    params = list(sig.parameters.keys())
    assert "decimal" in params, "Missing parameter 'decimal'"

def test_sparql_decimal_has_decimal():
    assert hasattr(sparql_DECIMAL, "decimal")
    descriptor = None
    for klass in sparql_DECIMAL.__mro__:
        if "decimal" in klass.__dict__:
            descriptor = klass.__dict__["decimal"]
            break
    assert isinstance(descriptor, property)



def test_sparql_numericliteralunsigned_is_not_abstract():
    assert not inspect.isabstract(sparql_NumericLiteralUnsigned)


def test_sparql_numericliteralunsigned_constructor_exists():
    assert callable(sparql_NumericLiteralUnsigned.__init__)


def test_sparql_numericliteralunsigned_constructor_args():
    sig = inspect.signature(sparql_NumericLiteralUnsigned.__init__)
    params = list(sig.parameters.keys())



def test_additionalmultiplicativeexpressionne_is_not_abstract():
    assert not inspect.isabstract(AdditionalMultiplicativeExpressionNE)


def test_additionalmultiplicativeexpressionne_constructor_exists():
    assert callable(AdditionalMultiplicativeExpressionNE.__init__)


def test_additionalmultiplicativeexpressionne_constructor_args():
    sig = inspect.signature(AdditionalMultiplicativeExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_minusmultiplicativeexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_MinusMultiplicativeExpressionNE)


def test_sparql_minusmultiplicativeexpressionne_constructor_exists():
    assert callable(sparql_MinusMultiplicativeExpressionNE.__init__)


def test_sparql_minusmultiplicativeexpressionne_constructor_args():
    sig = inspect.signature(sparql_MinusMultiplicativeExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_numericliteralnegative_is_not_abstract():
    assert not inspect.isabstract(sparql_NumericLiteralNegative)


def test_sparql_numericliteralnegative_constructor_exists():
    assert callable(sparql_NumericLiteralNegative.__init__)


def test_sparql_numericliteralnegative_constructor_args():
    sig = inspect.signature(sparql_NumericLiteralNegative.__init__)
    params = list(sig.parameters.keys())



def test_sparql_numericliteralpositive_is_not_abstract():
    assert not inspect.isabstract(sparql_NumericLiteralPositive)


def test_sparql_numericliteralpositive_constructor_exists():
    assert callable(sparql_NumericLiteralPositive.__init__)


def test_sparql_numericliteralpositive_constructor_args():
    sig = inspect.signature(sparql_NumericLiteralPositive.__init__)
    params = list(sig.parameters.keys())



def test_sparql_plusmultiplicativeexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_PlusMultiplicativeExpressionNE)


def test_sparql_plusmultiplicativeexpressionne_constructor_exists():
    assert callable(sparql_PlusMultiplicativeExpressionNE.__init__)


def test_sparql_plusmultiplicativeexpressionne_constructor_args():
    sig = inspect.signature(sparql_PlusMultiplicativeExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_PrimaryExpression)


def test_sparql_primaryexpression_constructor_exists():
    assert callable(sparql_PrimaryExpression.__init__)


def test_sparql_primaryexpression_constructor_args():
    sig = inspect.signature(sparql_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_minusprimaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_MinusPrimaryExpressionNE)


def test_sparql_minusprimaryexpressionne_constructor_exists():
    assert callable(sparql_MinusPrimaryExpressionNE.__init__)


def test_sparql_minusprimaryexpressionne_constructor_args():
    sig = inspect.signature(sparql_MinusPrimaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_plusprimaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_PlusPrimaryExpressionNE)


def test_sparql_plusprimaryexpressionne_constructor_exists():
    assert callable(sparql_PlusPrimaryExpressionNE.__init__)


def test_sparql_plusprimaryexpressionne_constructor_args():
    sig = inspect.signature(sparql_PlusPrimaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_notprimaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_NotPrimaryExpressionNE)


def test_sparql_notprimaryexpressionne_constructor_exists():
    assert callable(sparql_NotPrimaryExpressionNE.__init__)


def test_sparql_notprimaryexpressionne_constructor_args():
    sig = inspect.signature(sparql_NotPrimaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_dividedbyadditionalunaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_DividedByAdditionalUnaryExpressionNE)


def test_sparql_dividedbyadditionalunaryexpressionne_constructor_exists():
    assert callable(sparql_DividedByAdditionalUnaryExpressionNE.__init__)


def test_sparql_dividedbyadditionalunaryexpressionne_constructor_args():
    sig = inspect.signature(sparql_DividedByAdditionalUnaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_additionalnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(AdditionalNumericExpressionNE)


def test_additionalnumericexpressionne_constructor_exists():
    assert callable(AdditionalNumericExpressionNE.__init__)


def test_additionalnumericexpressionne_constructor_args():
    sig = inspect.signature(AdditionalNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_smallerorequalnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_SmallerOrEqualNumericExpressionNE)


def test_sparql_smallerorequalnumericexpressionne_constructor_exists():
    assert callable(sparql_SmallerOrEqualNumericExpressionNE.__init__)


def test_sparql_smallerorequalnumericexpressionne_constructor_args():
    sig = inspect.signature(sparql_SmallerOrEqualNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_biggernumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_BiggerNumericExpressionNE)


def test_sparql_biggernumericexpressionne_constructor_exists():
    assert callable(sparql_BiggerNumericExpressionNE.__init__)


def test_sparql_biggernumericexpressionne_constructor_args():
    sig = inspect.signature(sparql_BiggerNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_smallernumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_SmallerNumericExpressionNE)


def test_sparql_smallernumericexpressionne_constructor_exists():
    assert callable(sparql_SmallerNumericExpressionNE.__init__)


def test_sparql_smallernumericexpressionne_constructor_args():
    sig = inspect.signature(sparql_SmallerNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_biggerorequalnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_BiggerOrEqualNumericExpressionNE)


def test_sparql_biggerorequalnumericexpressionne_constructor_exists():
    assert callable(sparql_BiggerOrEqualNumericExpressionNE.__init__)


def test_sparql_biggerorequalnumericexpressionne_constructor_args():
    sig = inspect.signature(sparql_BiggerOrEqualNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_notequalnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_NotEqualNumericExpressionNE)


def test_sparql_notequalnumericexpressionne_constructor_exists():
    assert callable(sparql_NotEqualNumericExpressionNE.__init__)


def test_sparql_notequalnumericexpressionne_constructor_args():
    sig = inspect.signature(sparql_NotEqualNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_equalsnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_EqualsNumericExpressionNE)


def test_sparql_equalsnumericexpressionne_constructor_exists():
    assert callable(sparql_EqualsNumericExpressionNE.__init__)


def test_sparql_equalsnumericexpressionne_constructor_args():
    sig = inspect.signature(sparql_EqualsNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_arglist_is_not_abstract():
    assert not inspect.isabstract(ArgList)


def test_arglist_constructor_exists():
    assert callable(ArgList.__init__)


def test_arglist_constructor_args():
    sig = inspect.signature(ArgList.__init__)
    params = list(sig.parameters.keys())



def test_sparql_arglistexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_ArgListExpressionNE)


def test_sparql_arglistexpressionne_constructor_exists():
    assert callable(sparql_ArgListExpressionNE.__init__)


def test_sparql_arglistexpressionne_constructor_args():
    sig = inspect.signature(sparql_ArgListExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_arglistnilne_is_not_abstract():
    assert not inspect.isabstract(sparql_ArgListNILNE)


def test_sparql_arglistnilne_constructor_exists():
    assert callable(sparql_ArgListNILNE.__init__)


def test_sparql_arglistnilne_constructor_args():
    sig = inspect.signature(sparql_ArgListNILNE.__init__)
    params = list(sig.parameters.keys())



def test_builtincall_is_not_abstract():
    assert not inspect.isabstract(BuiltInCall)


def test_builtincall_constructor_exists():
    assert callable(BuiltInCall.__init__)


def test_builtincall_constructor_args():
    sig = inspect.signature(BuiltInCall.__init__)
    params = list(sig.parameters.keys())



def test_sparql_isblankbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql_IsBlankBuiltInCallNE)


def test_sparql_isblankbuiltincallne_constructor_exists():
    assert callable(sparql_IsBlankBuiltInCallNE.__init__)


def test_sparql_isblankbuiltincallne_constructor_args():
    sig = inspect.signature(sparql_IsBlankBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_regexexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_RegexExpression)


def test_sparql_regexexpression_constructor_exists():
    assert callable(sparql_RegexExpression.__init__)


def test_sparql_regexexpression_constructor_args():
    sig = inspect.signature(sparql_RegexExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_langmatchesbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql_LangmatchesBuiltInCallNE)


def test_sparql_langmatchesbuiltincallne_constructor_exists():
    assert callable(sparql_LangmatchesBuiltInCallNE.__init__)


def test_sparql_langmatchesbuiltincallne_constructor_args():
    sig = inspect.signature(sparql_LangmatchesBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_isuribuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql_IsURIBuiltInCallNE)


def test_sparql_isuribuiltincallne_constructor_exists():
    assert callable(sparql_IsURIBuiltInCallNE.__init__)


def test_sparql_isuribuiltincallne_constructor_args():
    sig = inspect.signature(sparql_IsURIBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_langbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql_LangBuiltInCallNE)


def test_sparql_langbuiltincallne_constructor_exists():
    assert callable(sparql_LangBuiltInCallNE.__init__)


def test_sparql_langbuiltincallne_constructor_args():
    sig = inspect.signature(sparql_LangBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_datatypebuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql_DatatypeBuiltInCallNE)


def test_sparql_datatypebuiltincallne_constructor_exists():
    assert callable(sparql_DatatypeBuiltInCallNE.__init__)


def test_sparql_datatypebuiltincallne_constructor_args():
    sig = inspect.signature(sparql_DatatypeBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_isliteralbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql_IsLiteralBuiltInCallNE)


def test_sparql_isliteralbuiltincallne_constructor_exists():
    assert callable(sparql_IsLiteralBuiltInCallNE.__init__)


def test_sparql_isliteralbuiltincallne_constructor_args():
    sig = inspect.signature(sparql_IsLiteralBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_isiribuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql_IsIRIBuiltInCallNE)


def test_sparql_isiribuiltincallne_constructor_exists():
    assert callable(sparql_IsIRIBuiltInCallNE.__init__)


def test_sparql_isiribuiltincallne_constructor_args():
    sig = inspect.signature(sparql_IsIRIBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_strbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql_StrBuiltInCallNE)


def test_sparql_strbuiltincallne_constructor_exists():
    assert callable(sparql_StrBuiltInCallNE.__init__)


def test_sparql_strbuiltincallne_constructor_args():
    sig = inspect.signature(sparql_StrBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_sparql_functioncall_is_not_abstract():
    assert not inspect.isabstract(sparql_FunctionCall)


def test_sparql_functioncall_constructor_exists():
    assert callable(sparql_FunctionCall.__init__)


def test_sparql_functioncall_constructor_args():
    sig = inspect.signature(sparql_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_sparql_sametermbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql_SameTermBuiltInCallNE)


def test_sparql_sametermbuiltincallne_constructor_exists():
    assert callable(sparql_SameTermBuiltInCallNE.__init__)


def test_sparql_sametermbuiltincallne_constructor_args():
    sig = inspect.signature(sparql_SameTermBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_boundbuiltincallne_is_not_abstract():
    assert not inspect.isabstract(sparql_BoundBuiltInCallNE)


def test_sparql_boundbuiltincallne_constructor_exists():
    assert callable(sparql_BoundBuiltInCallNE.__init__)


def test_sparql_boundbuiltincallne_constructor_args():
    sig = inspect.signature(sparql_BoundBuiltInCallNE.__init__)
    params = list(sig.parameters.keys())



def test_triplesnode_is_not_abstract():
    assert not inspect.isabstract(TriplesNode)


def test_triplesnode_constructor_exists():
    assert callable(TriplesNode.__init__)


def test_triplesnode_constructor_args():
    sig = inspect.signature(TriplesNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql_blanknodepropertylist_is_not_abstract():
    assert not inspect.isabstract(sparql_BlankNodePropertyList)


def test_sparql_blanknodepropertylist_constructor_exists():
    assert callable(sparql_BlankNodePropertyList.__init__)


def test_sparql_blanknodepropertylist_constructor_args():
    sig = inspect.signature(sparql_BlankNodePropertyList.__init__)
    params = list(sig.parameters.keys())



def test_sparql_collection_is_not_abstract():
    assert not inspect.isabstract(sparql_Collection)


def test_sparql_collection_constructor_exists():
    assert callable(sparql_Collection.__init__)


def test_sparql_collection_constructor_args():
    sig = inspect.signature(sparql_Collection.__init__)
    params = list(sig.parameters.keys())



def test_graphnode_is_not_abstract():
    assert not inspect.isabstract(GraphNode)


def test_graphnode_constructor_exists():
    assert callable(GraphNode.__init__)


def test_graphnode_constructor_args():
    sig = inspect.signature(GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql_patternorfilterne_is_not_abstract():
    assert not inspect.isabstract(sparql_PatternOrFilterNE)


def test_sparql_patternorfilterne_constructor_exists():
    assert callable(sparql_PatternOrFilterNE.__init__)


def test_sparql_patternorfilterne_constructor_args():
    sig = inspect.signature(sparql_PatternOrFilterNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_varorterm_is_not_abstract():
    assert not inspect.isabstract(sparql_VarOrTerm)


def test_sparql_varorterm_constructor_exists():
    assert callable(sparql_VarOrTerm.__init__)


def test_sparql_varorterm_constructor_args():
    sig = inspect.signature(sparql_VarOrTerm.__init__)
    params = list(sig.parameters.keys())



def test_triplessamesubject_is_not_abstract():
    assert not inspect.isabstract(TriplesSameSubject)


def test_triplessamesubject_constructor_exists():
    assert callable(TriplesSameSubject.__init__)


def test_triplessamesubject_constructor_args():
    sig = inspect.signature(TriplesSameSubject.__init__)
    params = list(sig.parameters.keys())



def test_sparql_triplessamesubjectleftne_is_not_abstract():
    assert not inspect.isabstract(sparql_TriplesSameSubjectLeftNE)


def test_sparql_triplessamesubjectleftne_constructor_exists():
    assert callable(sparql_TriplesSameSubjectLeftNE.__init__)


def test_sparql_triplessamesubjectleftne_constructor_args():
    sig = inspect.signature(sparql_TriplesSameSubjectLeftNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_triplesblock_is_not_abstract():
    assert not inspect.isabstract(sparql_TriplesBlock)


def test_sparql_triplesblock_constructor_exists():
    assert callable(sparql_TriplesBlock.__init__)


def test_sparql_triplesblock_constructor_args():
    sig = inspect.signature(sparql_TriplesBlock.__init__)
    params = list(sig.parameters.keys())



def test_graphpatternnottriples_is_not_abstract():
    assert not inspect.isabstract(GraphPatternNotTriples)


def test_graphpatternnottriples_constructor_exists():
    assert callable(GraphPatternNotTriples.__init__)


def test_graphpatternnottriples_constructor_args():
    sig = inspect.signature(GraphPatternNotTriples.__init__)
    params = list(sig.parameters.keys())



def test_sparql_graphgraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_GraphGraphPattern)


def test_sparql_graphgraphpattern_constructor_exists():
    assert callable(sparql_GraphGraphPattern.__init__)


def test_sparql_graphgraphpattern_constructor_args():
    sig = inspect.signature(sparql_GraphGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_grouporuniongraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_GroupOrUnionGraphPattern)


def test_sparql_grouporuniongraphpattern_constructor_exists():
    assert callable(sparql_GroupOrUnionGraphPattern.__init__)


def test_sparql_grouporuniongraphpattern_constructor_args():
    sig = inspect.signature(sparql_GroupOrUnionGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_optionalgraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_OptionalGraphPattern)


def test_sparql_optionalgraphpattern_constructor_exists():
    assert callable(sparql_OptionalGraphPattern.__init__)


def test_sparql_optionalgraphpattern_constructor_args():
    sig = inspect.signature(sparql_OptionalGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_patternorfilterne_is_not_abstract():
    assert not inspect.isabstract(PatternOrFilterNE)


def test_patternorfilterne_constructor_exists():
    assert callable(PatternOrFilterNE.__init__)


def test_patternorfilterne_constructor_args():
    sig = inspect.signature(PatternOrFilterNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_filter_is_not_abstract():
    assert not inspect.isabstract(sparql_Filter)


def test_sparql_filter_constructor_exists():
    assert callable(sparql_Filter.__init__)


def test_sparql_filter_constructor_args():
    sig = inspect.signature(sparql_Filter.__init__)
    params = list(sig.parameters.keys())



def test_sparql_graphpatternnottriples_is_not_abstract():
    assert not inspect.isabstract(sparql_GraphPatternNotTriples)


def test_sparql_graphpatternnottriples_constructor_exists():
    assert callable(sparql_GraphPatternNotTriples.__init__)


def test_sparql_graphpatternnottriples_constructor_args():
    sig = inspect.signature(sparql_GraphPatternNotTriples.__init__)
    params = list(sig.parameters.keys())



def test_sparql_triplesnode_is_not_abstract():
    assert not inspect.isabstract(sparql_TriplesNode)


def test_sparql_triplesnode_constructor_exists():
    assert callable(sparql_TriplesNode.__init__)


def test_sparql_triplesnode_constructor_args():
    sig = inspect.signature(sparql_TriplesNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql_triplessamesubjectrightne_is_not_abstract():
    assert not inspect.isabstract(sparql_TriplesSameSubjectRightNE)


def test_sparql_triplessamesubjectrightne_constructor_exists():
    assert callable(sparql_TriplesSameSubjectRightNE.__init__)


def test_sparql_triplessamesubjectrightne_constructor_args():
    sig = inspect.signature(sparql_TriplesSameSubjectRightNE.__init__)
    params = list(sig.parameters.keys())



def test_irireference_is_not_abstract():
    assert not inspect.isabstract(IRIreference)


def test_irireference_constructor_exists():
    assert callable(IRIreference.__init__)


def test_irireference_constructor_args():
    sig = inspect.signature(IRIreference.__init__)
    params = list(sig.parameters.keys())



def test_sparql_prefixedname_is_not_abstract():
    assert not inspect.isabstract(sparql_PrefixedName)


def test_sparql_prefixedname_constructor_exists():
    assert callable(sparql_PrefixedName.__init__)


def test_sparql_prefixedname_constructor_args():
    sig = inspect.signature(sparql_PrefixedName.__init__)
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



def test_sparql_blanknode_is_not_abstract():
    assert not inspect.isabstract(sparql_BlankNode)


def test_sparql_blanknode_constructor_exists():
    assert callable(sparql_BlankNode.__init__)


def test_sparql_blanknode_constructor_args():
    sig = inspect.signature(sparql_BlankNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql_notinlist_is_not_abstract():
    assert not inspect.isabstract(sparql_NotInList)


def test_sparql_notinlist_constructor_exists():
    assert callable(sparql_NotInList.__init__)


def test_sparql_notinlist_constructor_args():
    sig = inspect.signature(sparql_NotInList.__init__)
    params = list(sig.parameters.keys())



def test_sparql_whereliteral_is_not_abstract():
    assert not inspect.isabstract(sparql_WhereLiteral)


def test_sparql_whereliteral_constructor_exists():
    assert callable(sparql_WhereLiteral.__init__)


def test_sparql_whereliteral_constructor_args():
    sig = inspect.signature(sparql_WhereLiteral.__init__)
    params = list(sig.parameters.keys())



def test_graphclausene_is_not_abstract():
    assert not inspect.isabstract(GraphClauseNE)


def test_graphclausene_constructor_exists():
    assert callable(GraphClauseNE.__init__)


def test_graphclausene_constructor_args():
    sig = inspect.signature(GraphClauseNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_namedgraphclause_is_not_abstract():
    assert not inspect.isabstract(sparql_NamedGraphClause)


def test_sparql_namedgraphclause_constructor_exists():
    assert callable(sparql_NamedGraphClause.__init__)


def test_sparql_namedgraphclause_constructor_args():
    sig = inspect.signature(sparql_NamedGraphClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql_defaultgraphclause_is_not_abstract():
    assert not inspect.isabstract(sparql_DefaultGraphClause)


def test_sparql_defaultgraphclause_constructor_exists():
    assert callable(sparql_DefaultGraphClause.__init__)


def test_sparql_defaultgraphclause_constructor_args():
    sig = inspect.signature(sparql_DefaultGraphClause.__init__)
    params = list(sig.parameters.keys())



def test_orderconditionrightne_is_not_abstract():
    assert not inspect.isabstract(OrderConditionRightNE)


def test_orderconditionrightne_constructor_exists():
    assert callable(OrderConditionRightNE.__init__)


def test_orderconditionrightne_constructor_args():
    sig = inspect.signature(OrderConditionRightNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_constraint_is_not_abstract():
    assert not inspect.isabstract(sparql_Constraint)


def test_sparql_constraint_constructor_exists():
    assert callable(sparql_Constraint.__init__)


def test_sparql_constraint_constructor_args():
    sig = inspect.signature(sparql_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_varorterm_is_not_abstract():
    assert not inspect.isabstract(VarOrTerm)


def test_varorterm_constructor_exists():
    assert callable(VarOrTerm.__init__)


def test_varorterm_constructor_args():
    sig = inspect.signature(VarOrTerm.__init__)
    params = list(sig.parameters.keys())



def test_sparql_graphterm_is_not_abstract():
    assert not inspect.isabstract(sparql_GraphTerm)


def test_sparql_graphterm_constructor_exists():
    assert callable(sparql_GraphTerm.__init__)


def test_sparql_graphterm_constructor_args():
    sig = inspect.signature(sparql_GraphTerm.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_rdfliteral_is_not_abstract():
    assert not inspect.isabstract(sparql_RDFLiteral)


def test_sparql_rdfliteral_constructor_exists():
    assert callable(sparql_RDFLiteral.__init__)


def test_sparql_rdfliteral_constructor_args():
    sig = inspect.signature(sparql_RDFLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql_builtincall_is_not_abstract():
    assert not inspect.isabstract(sparql_BuiltInCall)


def test_sparql_builtincall_constructor_exists():
    assert callable(sparql_BuiltInCall.__init__)


def test_sparql_builtincall_constructor_args():
    sig = inspect.signature(sparql_BuiltInCall.__init__)
    params = list(sig.parameters.keys())



def test_sparql_irireforfunction_is_not_abstract():
    assert not inspect.isabstract(sparql_IRIrefOrFunction)


def test_sparql_irireforfunction_constructor_exists():
    assert callable(sparql_IRIrefOrFunction.__init__)


def test_sparql_irireforfunction_constructor_args():
    sig = inspect.signature(sparql_IRIrefOrFunction.__init__)
    params = list(sig.parameters.keys())



def test_sparql_numericliteral_is_not_abstract():
    assert not inspect.isabstract(sparql_NumericLiteral)


def test_sparql_numericliteral_constructor_exists():
    assert callable(sparql_NumericLiteral.__init__)


def test_sparql_numericliteral_constructor_args():
    sig = inspect.signature(sparql_NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparql_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(sparql_BooleanLiteral)


def test_sparql_booleanliteral_constructor_exists():
    assert callable(sparql_BooleanLiteral.__init__)


def test_sparql_booleanliteral_constructor_args():
    sig = inspect.signature(sparql_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_varoririref_is_not_abstract():
    assert not inspect.isabstract(VarOrIRIref)


def test_varoririref_constructor_exists():
    assert callable(VarOrIRIref.__init__)


def test_varoririref_constructor_args():
    sig = inspect.signature(VarOrIRIref.__init__)
    params = list(sig.parameters.keys())



def test_sparql_pname_ln_is_not_abstract():
    assert not inspect.isabstract(sparql_PNAME_LN)


def test_sparql_pname_ln_constructor_exists():
    assert callable(sparql_PNAME_LN.__init__)


def test_sparql_pname_ln_constructor_args():
    sig = inspect.signature(sparql_PNAME_LN.__init__)
    params = list(sig.parameters.keys())



def test_sparql_irireference_is_not_abstract():
    assert not inspect.isabstract(sparql_IRIreference)


def test_sparql_irireference_constructor_exists():
    assert callable(sparql_IRIreference.__init__)


def test_sparql_irireference_constructor_args():
    sig = inspect.signature(sparql_IRIreference.__init__)
    params = list(sig.parameters.keys())



def test_verb_is_not_abstract():
    assert not inspect.isabstract(Verb)


def test_verb_constructor_exists():
    assert callable(Verb.__init__)


def test_verb_constructor_args():
    sig = inspect.signature(Verb.__init__)
    params = list(sig.parameters.keys())



def test_sparql_verbane_is_not_abstract():
    assert not inspect.isabstract(sparql_VerbANE)


def test_sparql_verbane_constructor_exists():
    assert callable(sparql_VerbANE.__init__)


def test_sparql_verbane_constructor_args():
    sig = inspect.signature(sparql_VerbANE.__init__)
    params = list(sig.parameters.keys())
    assert "theA" in params, "Missing parameter 'theA'"

def test_sparql_verbane_has_theA():
    assert hasattr(sparql_VerbANE, "theA")
    descriptor = None
    for klass in sparql_VerbANE.__mro__:
        if "theA" in klass.__dict__:
            descriptor = klass.__dict__["theA"]
            break
    assert isinstance(descriptor, property)



def test_variablesne_is_not_abstract():
    assert not inspect.isabstract(VariablesNE)


def test_variablesne_constructor_exists():
    assert callable(VariablesNE.__init__)


def test_variablesne_constructor_args():
    sig = inspect.signature(VariablesNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_somevariablesne_is_not_abstract():
    assert not inspect.isabstract(sparql_SomeVariablesNE)


def test_sparql_somevariablesne_constructor_exists():
    assert callable(sparql_SomeVariablesNE.__init__)


def test_sparql_somevariablesne_constructor_args():
    sig = inspect.signature(sparql_SomeVariablesNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_allvariablesne_is_not_abstract():
    assert not inspect.isabstract(sparql_AllVariablesNE)


def test_sparql_allvariablesne_constructor_exists():
    assert callable(sparql_AllVariablesNE.__init__)


def test_sparql_allvariablesne_constructor_args():
    sig = inspect.signature(sparql_AllVariablesNE.__init__)
    params = list(sig.parameters.keys())



def test_solutionsdisplayne_is_not_abstract():
    assert not inspect.isabstract(SolutionsDisplayNE)


def test_solutionsdisplayne_constructor_exists():
    assert callable(SolutionsDisplayNE.__init__)


def test_solutionsdisplayne_constructor_args():
    sig = inspect.signature(SolutionsDisplayNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_reducedne_is_not_abstract():
    assert not inspect.isabstract(sparql_ReducedNE)


def test_sparql_reducedne_constructor_exists():
    assert callable(sparql_ReducedNE.__init__)


def test_sparql_reducedne_constructor_args():
    sig = inspect.signature(sparql_ReducedNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_distinctne_is_not_abstract():
    assert not inspect.isabstract(sparql_DistinctNE)


def test_sparql_distinctne_constructor_exists():
    assert callable(sparql_DistinctNE.__init__)


def test_sparql_distinctne_constructor_args():
    sig = inspect.signature(sparql_DistinctNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_integer_is_not_abstract():
    assert not inspect.isabstract(sparql_INTEGER)


def test_sparql_integer_constructor_exists():
    assert callable(sparql_INTEGER.__init__)


def test_sparql_integer_constructor_args():
    sig = inspect.signature(sparql_INTEGER.__init__)
    params = list(sig.parameters.keys())
    assert "integer" in params, "Missing parameter 'integer'"

def test_sparql_integer_has_integer():
    assert hasattr(sparql_INTEGER, "integer")
    descriptor = None
    for klass in sparql_INTEGER.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)



def test_limitoffsetclauses_is_not_abstract():
    assert not inspect.isabstract(LimitOffsetClauses)


def test_limitoffsetclauses_constructor_exists():
    assert callable(LimitOffsetClauses.__init__)


def test_limitoffsetclauses_constructor_args():
    sig = inspect.signature(LimitOffsetClauses.__init__)
    params = list(sig.parameters.keys())



def test_sparql_limitoffsetclausesrightne_is_not_abstract():
    assert not inspect.isabstract(sparql_LimitOffsetClausesRightNE)


def test_sparql_limitoffsetclausesrightne_constructor_exists():
    assert callable(sparql_LimitOffsetClausesRightNE.__init__)


def test_sparql_limitoffsetclausesrightne_constructor_args():
    sig = inspect.signature(sparql_LimitOffsetClausesRightNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_limitoffsetclausesleftne_is_not_abstract():
    assert not inspect.isabstract(sparql_LimitOffsetClausesLeftNE)


def test_sparql_limitoffsetclausesleftne_constructor_exists():
    assert callable(sparql_LimitOffsetClausesLeftNE.__init__)


def test_sparql_limitoffsetclausesleftne_constructor_args():
    sig = inspect.signature(sparql_LimitOffsetClausesLeftNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_brackettedexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_BrackettedExpression)


def test_sparql_brackettedexpression_constructor_exists():
    assert callable(sparql_BrackettedExpression.__init__)


def test_sparql_brackettedexpression_constructor_args():
    sig = inspect.signature(sparql_BrackettedExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_ascordecs_is_not_abstract():
    assert not inspect.isabstract(sparql_AscOrDecs)


def test_sparql_ascordecs_constructor_exists():
    assert callable(sparql_AscOrDecs.__init__)


def test_sparql_ascordecs_constructor_args():
    sig = inspect.signature(sparql_AscOrDecs.__init__)
    params = list(sig.parameters.keys())



def test_ordercondition_is_not_abstract():
    assert not inspect.isabstract(OrderCondition)


def test_ordercondition_constructor_exists():
    assert callable(OrderCondition.__init__)


def test_ordercondition_constructor_args():
    sig = inspect.signature(OrderCondition.__init__)
    params = list(sig.parameters.keys())



def test_sparql_orderconditionrightne_is_not_abstract():
    assert not inspect.isabstract(sparql_OrderConditionRightNE)


def test_sparql_orderconditionrightne_constructor_exists():
    assert callable(sparql_OrderConditionRightNE.__init__)


def test_sparql_orderconditionrightne_constructor_args():
    sig = inspect.signature(sparql_OrderConditionRightNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_orderconditionleftne_is_not_abstract():
    assert not inspect.isabstract(sparql_OrderConditionLeftNE)


def test_sparql_orderconditionleftne_constructor_exists():
    assert callable(sparql_OrderConditionLeftNE.__init__)


def test_sparql_orderconditionleftne_constructor_args():
    sig = inspect.signature(sparql_OrderConditionLeftNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_varoririref_is_not_abstract():
    assert not inspect.isabstract(sparql_VarOrIRIref)


def test_sparql_varoririref_constructor_exists():
    assert callable(sparql_VarOrIRIref.__init__)


def test_sparql_varoririref_constructor_args():
    sig = inspect.signature(sparql_VarOrIRIref.__init__)
    params = list(sig.parameters.keys())



def test_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_query_constructor_exists():
    assert callable(Query.__init__)


def test_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())



def test_sparql_askquery_is_not_abstract():
    assert not inspect.isabstract(sparql_AskQuery)


def test_sparql_askquery_constructor_exists():
    assert callable(sparql_AskQuery.__init__)


def test_sparql_askquery_constructor_args():
    sig = inspect.signature(sparql_AskQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_describequery_is_not_abstract():
    assert not inspect.isabstract(sparql_DescribeQuery)


def test_sparql_describequery_constructor_exists():
    assert callable(sparql_DescribeQuery.__init__)


def test_sparql_describequery_constructor_args():
    sig = inspect.signature(sparql_DescribeQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_constructquery_is_not_abstract():
    assert not inspect.isabstract(sparql_ConstructQuery)


def test_sparql_constructquery_constructor_exists():
    assert callable(sparql_ConstructQuery.__init__)


def test_sparql_constructquery_constructor_args():
    sig = inspect.signature(sparql_ConstructQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_selectquery_is_not_abstract():
    assert not inspect.isabstract(sparql_SelectQuery)


def test_sparql_selectquery_constructor_exists():
    assert callable(sparql_SelectQuery.__init__)


def test_sparql_selectquery_constructor_args():
    sig = inspect.signature(sparql_SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_pname_ns_is_not_abstract():
    assert not inspect.isabstract(sparql_PNAME_NS)


def test_sparql_pname_ns_constructor_exists():
    assert callable(sparql_PNAME_NS.__init__)


def test_sparql_pname_ns_constructor_args():
    sig = inspect.signature(sparql_PNAME_NS.__init__)
    params = list(sig.parameters.keys())
    assert "pn_prefix" in params, "Missing parameter 'pn_prefix'"

def test_sparql_pname_ns_has_pn_prefix():
    assert hasattr(sparql_PNAME_NS, "pn_prefix")
    descriptor = None
    for klass in sparql_PNAME_NS.__mro__:
        if "pn_prefix" in klass.__dict__:
            descriptor = klass.__dict__["pn_prefix"]
            break
    assert isinstance(descriptor, property)



def test_sparql_var_is_not_abstract():
    assert not inspect.isabstract(sparql_Var)


def test_sparql_var_constructor_exists():
    assert callable(sparql_Var.__init__)


def test_sparql_var_constructor_args():
    sig = inspect.signature(sparql_Var.__init__)
    params = list(sig.parameters.keys())
    assert "varname" in params, "Missing parameter 'varname'"

def test_sparql_var_has_varname():
    assert hasattr(sparql_Var, "varname")
    descriptor = None
    for klass in sparql_Var.__mro__:
        if "varname" in klass.__dict__:
            descriptor = klass.__dict__["varname"]
            break
    assert isinstance(descriptor, property)



def test_sparql_locatedelement_is_not_abstract():
    assert not inspect.isabstract(sparql_LocatedElement)


def test_sparql_locatedelement_constructor_exists():
    assert callable(sparql_LocatedElement.__init__)


def test_sparql_locatedelement_constructor_args():
    sig = inspect.signature(sparql_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_sparql_locatedelement_has_location():
    assert hasattr(sparql_LocatedElement, "location")
    descriptor = None
    for klass in sparql_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_sparql_locatedelement_has_commentsAfter():
    assert hasattr(sparql_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in sparql_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_sparql_locatedelement_has_commentsBefore():
    assert hasattr(sparql_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in sparql_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)



def test_sparql_iri_ref_is_not_abstract():
    assert not inspect.isabstract(sparql_IRI_REF)


def test_sparql_iri_ref_constructor_exists():
    assert callable(sparql_IRI_REF.__init__)


def test_sparql_iri_ref_constructor_args():
    sig = inspect.signature(sparql_IRI_REF.__init__)
    params = list(sig.parameters.keys())
    assert "iri_ref" in params, "Missing parameter 'iri_ref'"

def test_sparql_iri_ref_has_iri_ref():
    assert hasattr(sparql_IRI_REF, "iri_ref")
    descriptor = None
    for klass in sparql_IRI_REF.__mro__:
        if "iri_ref" in klass.__dict__:
            descriptor = klass.__dict__["iri_ref"]
            break
    assert isinstance(descriptor, property)



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_sparql_offsetclause_is_not_abstract():
    assert not inspect.isabstract(sparql_OffsetClause)


def test_sparql_offsetclause_constructor_exists():
    assert callable(sparql_OffsetClause.__init__)


def test_sparql_offsetclause_constructor_args():
    sig = inspect.signature(sparql_OffsetClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql_triplessamesubject_is_not_abstract():
    assert not inspect.isabstract(sparql_TriplesSameSubject)


def test_sparql_triplessamesubject_constructor_exists():
    assert callable(sparql_TriplesSameSubject.__init__)


def test_sparql_triplessamesubject_constructor_args():
    sig = inspect.signature(sparql_TriplesSameSubject.__init__)
    params = list(sig.parameters.keys())



def test_sparql_propertylistnotempty_is_not_abstract():
    assert not inspect.isabstract(sparql_PropertyListNotEmpty)


def test_sparql_propertylistnotempty_constructor_exists():
    assert callable(sparql_PropertyListNotEmpty.__init__)


def test_sparql_propertylistnotempty_constructor_args():
    sig = inspect.signature(sparql_PropertyListNotEmpty.__init__)
    params = list(sig.parameters.keys())



def test_sparql_ordercondition_is_not_abstract():
    assert not inspect.isabstract(sparql_OrderCondition)


def test_sparql_ordercondition_constructor_exists():
    assert callable(sparql_OrderCondition.__init__)


def test_sparql_ordercondition_constructor_args():
    sig = inspect.signature(sparql_OrderCondition.__init__)
    params = list(sig.parameters.keys())



def test_sparql_ws_is_not_abstract():
    assert not inspect.isabstract(sparql_WS)


def test_sparql_ws_constructor_exists():
    assert callable(sparql_WS.__init__)


def test_sparql_ws_constructor_args():
    sig = inspect.signature(sparql_WS.__init__)
    params = list(sig.parameters.keys())
    assert "ws" in params, "Missing parameter 'ws'"

def test_sparql_ws_has_ws():
    assert hasattr(sparql_WS, "ws")
    descriptor = None
    for klass in sparql_WS.__mro__:
        if "ws" in klass.__dict__:
            descriptor = klass.__dict__["ws"]
            break
    assert isinstance(descriptor, property)



def test_sparql_additionalnumericexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_AdditionalNumericExpressionNE)


def test_sparql_additionalnumericexpressionne_constructor_exists():
    assert callable(sparql_AdditionalNumericExpressionNE.__init__)


def test_sparql_additionalnumericexpressionne_constructor_args():
    sig = inspect.signature(sparql_AdditionalNumericExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_object_is_not_abstract():
    assert not inspect.isabstract(sparql_Object)


def test_sparql_object_constructor_exists():
    assert callable(sparql_Object.__init__)


def test_sparql_object_constructor_args():
    sig = inspect.signature(sparql_Object.__init__)
    params = list(sig.parameters.keys())



def test_sparql_additionalexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_AdditionalExpressionNE)


def test_sparql_additionalexpressionne_constructor_exists():
    assert callable(sparql_AdditionalExpressionNE.__init__)


def test_sparql_additionalexpressionne_constructor_args():
    sig = inspect.signature(sparql_AdditionalExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_AdditiveExpression)


def test_sparql_additiveexpression_constructor_exists():
    assert callable(sparql_AdditiveExpression.__init__)


def test_sparql_additiveexpression_constructor_args():
    sig = inspect.signature(sparql_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_variablesne_is_not_abstract():
    assert not inspect.isabstract(sparql_VariablesNE)


def test_sparql_variablesne_constructor_exists():
    assert callable(sparql_VariablesNE.__init__)


def test_sparql_variablesne_constructor_args():
    sig = inspect.signature(sparql_VariablesNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_prologue_is_not_abstract():
    assert not inspect.isabstract(sparql_Prologue)


def test_sparql_prologue_constructor_exists():
    assert callable(sparql_Prologue.__init__)


def test_sparql_prologue_constructor_args():
    sig = inspect.signature(sparql_Prologue.__init__)
    params = list(sig.parameters.keys())



def test_sparql_prefixdecl_is_not_abstract():
    assert not inspect.isabstract(sparql_PrefixDecl)


def test_sparql_prefixdecl_constructor_exists():
    assert callable(sparql_PrefixDecl.__init__)


def test_sparql_prefixdecl_constructor_args():
    sig = inspect.signature(sparql_PrefixDecl.__init__)
    params = list(sig.parameters.keys())



def test_sparql_additionalconditionalandexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_AdditionalConditionalAndExpressionNE)


def test_sparql_additionalconditionalandexpressionne_constructor_exists():
    assert callable(sparql_AdditionalConditionalAndExpressionNE.__init__)


def test_sparql_additionalconditionalandexpressionne_constructor_args():
    sig = inspect.signature(sparql_AdditionalConditionalAndExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_arglist_is_not_abstract():
    assert not inspect.isabstract(sparql_ArgList)


def test_sparql_arglist_constructor_exists():
    assert callable(sparql_ArgList.__init__)


def test_sparql_arglist_constructor_args():
    sig = inspect.signature(sparql_ArgList.__init__)
    params = list(sig.parameters.keys())



def test_sparql_query_is_not_abstract():
    assert not inspect.isabstract(sparql_Query)


def test_sparql_query_constructor_exists():
    assert callable(sparql_Query.__init__)


def test_sparql_query_constructor_args():
    sig = inspect.signature(sparql_Query.__init__)
    params = list(sig.parameters.keys())



def test_sparql_langtagoririrefne_is_not_abstract():
    assert not inspect.isabstract(sparql_LANGTAGOrIRIrefNE)


def test_sparql_langtagoririrefne_constructor_exists():
    assert callable(sparql_LANGTAGOrIRIrefNE.__init__)


def test_sparql_langtagoririrefne_constructor_args():
    sig = inspect.signature(sparql_LANGTAGOrIRIrefNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_whereclause_is_not_abstract():
    assert not inspect.isabstract(sparql_WhereClause)


def test_sparql_whereclause_constructor_exists():
    assert callable(sparql_WhereClause.__init__)


def test_sparql_whereclause_constructor_args():
    sig = inspect.signature(sparql_WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql_orderclause_is_not_abstract():
    assert not inspect.isabstract(sparql_OrderClause)


def test_sparql_orderclause_constructor_exists():
    assert callable(sparql_OrderClause.__init__)


def test_sparql_orderclause_constructor_args():
    sig = inspect.signature(sparql_OrderClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql_varname_is_not_abstract():
    assert not inspect.isabstract(sparql_VARNAME)


def test_sparql_varname_constructor_exists():
    assert callable(sparql_VARNAME.__init__)


def test_sparql_varname_constructor_args():
    sig = inspect.signature(sparql_VARNAME.__init__)
    params = list(sig.parameters.keys())
    assert "varname" in params, "Missing parameter 'varname'"

def test_sparql_varname_has_varname():
    assert hasattr(sparql_VARNAME, "varname")
    descriptor = None
    for klass in sparql_VARNAME.__mro__:
        if "varname" in klass.__dict__:
            descriptor = klass.__dict__["varname"]
            break
    assert isinstance(descriptor, property)



def test_sparql_numericexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_NumericExpression)


def test_sparql_numericexpression_constructor_exists():
    assert callable(sparql_NumericExpression.__init__)


def test_sparql_numericexpression_constructor_args():
    sig = inspect.signature(sparql_NumericExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_datasetclause_is_not_abstract():
    assert not inspect.isabstract(sparql_DatasetClause)


def test_sparql_datasetclause_constructor_exists():
    assert callable(sparql_DatasetClause.__init__)


def test_sparql_datasetclause_constructor_args():
    sig = inspect.signature(sparql_DatasetClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql_pn_local_is_not_abstract():
    assert not inspect.isabstract(sparql_PN_LOCAL)


def test_sparql_pn_local_constructor_exists():
    assert callable(sparql_PN_LOCAL.__init__)


def test_sparql_pn_local_constructor_args():
    sig = inspect.signature(sparql_PN_LOCAL.__init__)
    params = list(sig.parameters.keys())
    assert "pn_local" in params, "Missing parameter 'pn_local'"

def test_sparql_pn_local_has_pn_local():
    assert hasattr(sparql_PN_LOCAL, "pn_local")
    descriptor = None
    for klass in sparql_PN_LOCAL.__mro__:
        if "pn_local" in klass.__dict__:
            descriptor = klass.__dict__["pn_local"]
            break
    assert isinstance(descriptor, property)



def test_sparql_additionalmultiplicativeexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_AdditionalMultiplicativeExpressionNE)


def test_sparql_additionalmultiplicativeexpressionne_constructor_exists():
    assert callable(sparql_AdditionalMultiplicativeExpressionNE.__init__)


def test_sparql_additionalmultiplicativeexpressionne_constructor_args():
    sig = inspect.signature(sparql_AdditionalMultiplicativeExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_limitoffsetclauses_is_not_abstract():
    assert not inspect.isabstract(sparql_LimitOffsetClauses)


def test_sparql_limitoffsetclauses_constructor_exists():
    assert callable(sparql_LimitOffsetClauses.__init__)


def test_sparql_limitoffsetclauses_constructor_args():
    sig = inspect.signature(sparql_LimitOffsetClauses.__init__)
    params = list(sig.parameters.keys())



def test_sparql_pn_prefix_is_not_abstract():
    assert not inspect.isabstract(sparql_PN_PREFIX)


def test_sparql_pn_prefix_constructor_exists():
    assert callable(sparql_PN_PREFIX.__init__)


def test_sparql_pn_prefix_constructor_args():
    sig = inspect.signature(sparql_PN_PREFIX.__init__)
    params = list(sig.parameters.keys())
    assert "pn_prefix" in params, "Missing parameter 'pn_prefix'"

def test_sparql_pn_prefix_has_pn_prefix():
    assert hasattr(sparql_PN_PREFIX, "pn_prefix")
    descriptor = None
    for klass in sparql_PN_PREFIX.__mro__:
        if "pn_prefix" in klass.__dict__:
            descriptor = klass.__dict__["pn_prefix"]
            break
    assert isinstance(descriptor, property)



def test_sparql_additionalunaryexpressionne_is_not_abstract():
    assert not inspect.isabstract(sparql_AdditionalUnaryExpressionNE)


def test_sparql_additionalunaryexpressionne_constructor_exists():
    assert callable(sparql_AdditionalUnaryExpressionNE.__init__)


def test_sparql_additionalunaryexpressionne_constructor_args():
    sig = inspect.signature(sparql_AdditionalUnaryExpressionNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_UnaryExpression)


def test_sparql_unaryexpression_constructor_exists():
    assert callable(sparql_UnaryExpression.__init__)


def test_sparql_unaryexpression_constructor_args():
    sig = inspect.signature(sparql_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_solutionsdisplayne_is_not_abstract():
    assert not inspect.isabstract(sparql_SolutionsDisplayNE)


def test_sparql_solutionsdisplayne_constructor_exists():
    assert callable(sparql_SolutionsDisplayNE.__init__)


def test_sparql_solutionsdisplayne_constructor_args():
    sig = inspect.signature(sparql_SolutionsDisplayNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_limitclause_is_not_abstract():
    assert not inspect.isabstract(sparql_LimitClause)


def test_sparql_limitclause_constructor_exists():
    assert callable(sparql_LimitClause.__init__)


def test_sparql_limitclause_constructor_args():
    sig = inspect.signature(sparql_LimitClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql_basedecl_is_not_abstract():
    assert not inspect.isabstract(sparql_BaseDecl)


def test_sparql_basedecl_constructor_exists():
    assert callable(sparql_BaseDecl.__init__)


def test_sparql_basedecl_constructor_args():
    sig = inspect.signature(sparql_BaseDecl.__init__)
    params = list(sig.parameters.keys())



def test_sparql_valuelogical_is_not_abstract():
    assert not inspect.isabstract(sparql_ValueLogical)


def test_sparql_valuelogical_constructor_exists():
    assert callable(sparql_ValueLogical.__init__)


def test_sparql_valuelogical_constructor_args():
    sig = inspect.signature(sparql_ValueLogical.__init__)
    params = list(sig.parameters.keys())



def test_sparql_objectlist_is_not_abstract():
    assert not inspect.isabstract(sparql_ObjectList)


def test_sparql_objectlist_constructor_exists():
    assert callable(sparql_ObjectList.__init__)


def test_sparql_objectlist_constructor_args():
    sig = inspect.signature(sparql_ObjectList.__init__)
    params = list(sig.parameters.keys())



def test_sparql_graphclausene_is_not_abstract():
    assert not inspect.isabstract(sparql_GraphClauseNE)


def test_sparql_graphclausene_constructor_exists():
    assert callable(sparql_GraphClauseNE.__init__)


def test_sparql_graphclausene_constructor_args():
    sig = inspect.signature(sparql_GraphClauseNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_expression_is_not_abstract():
    assert not inspect.isabstract(sparql_Expression)


def test_sparql_expression_constructor_exists():
    assert callable(sparql_Expression.__init__)


def test_sparql_expression_constructor_args():
    sig = inspect.signature(sparql_Expression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_solutionmodifier_is_not_abstract():
    assert not inspect.isabstract(sparql_SolutionModifier)


def test_sparql_solutionmodifier_constructor_exists():
    assert callable(sparql_SolutionModifier.__init__)


def test_sparql_solutionmodifier_constructor_args():
    sig = inspect.signature(sparql_SolutionModifier.__init__)
    params = list(sig.parameters.keys())



def test_sparql_graphnode_is_not_abstract():
    assert not inspect.isabstract(sparql_GraphNode)


def test_sparql_graphnode_constructor_exists():
    assert callable(sparql_GraphNode.__init__)


def test_sparql_graphnode_constructor_args():
    sig = inspect.signature(sparql_GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql_additionalggpelement_is_not_abstract():
    assert not inspect.isabstract(sparql_AdditionalGGPElement)


def test_sparql_additionalggpelement_constructor_exists():
    assert callable(sparql_AdditionalGGPElement.__init__)


def test_sparql_additionalggpelement_constructor_args():
    sig = inspect.signature(sparql_AdditionalGGPElement.__init__)
    params = list(sig.parameters.keys())



def test_sparql_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_RelationalExpression)


def test_sparql_relationalexpression_constructor_exists():
    assert callable(sparql_RelationalExpression.__init__)


def test_sparql_relationalexpression_constructor_args():
    sig = inspect.signature(sparql_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_ConditionalAndExpression)


def test_sparql_conditionalandexpression_constructor_exists():
    assert callable(sparql_ConditionalAndExpression.__init__)


def test_sparql_conditionalandexpression_constructor_args():
    sig = inspect.signature(sparql_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_constructtemplate_is_not_abstract():
    assert not inspect.isabstract(sparql_ConstructTemplate)


def test_sparql_constructtemplate_constructor_exists():
    assert callable(sparql_ConstructTemplate.__init__)


def test_sparql_constructtemplate_constructor_args():
    sig = inspect.signature(sparql_ConstructTemplate.__init__)
    params = list(sig.parameters.keys())



def test_sparql_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_MultiplicativeExpression)


def test_sparql_multiplicativeexpression_constructor_exists():
    assert callable(sparql_MultiplicativeExpression.__init__)


def test_sparql_multiplicativeexpression_constructor_args():
    sig = inspect.signature(sparql_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_sourceselector_is_not_abstract():
    assert not inspect.isabstract(sparql_SourceSelector)


def test_sparql_sourceselector_constructor_exists():
    assert callable(sparql_SourceSelector.__init__)


def test_sparql_sourceselector_constructor_args():
    sig = inspect.signature(sparql_SourceSelector.__init__)
    params = list(sig.parameters.keys())



def test_sparql_additionalvaluelogicalne_is_not_abstract():
    assert not inspect.isabstract(sparql_AdditionalValueLogicalNE)


def test_sparql_additionalvaluelogicalne_constructor_exists():
    assert callable(sparql_AdditionalValueLogicalNE.__init__)


def test_sparql_additionalvaluelogicalne_constructor_args():
    sig = inspect.signature(sparql_AdditionalValueLogicalNE.__init__)
    params = list(sig.parameters.keys())



def test_sparql_groupgraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_GroupGraphPattern)


def test_sparql_groupgraphpattern_constructor_exists():
    assert callable(sparql_GroupGraphPattern.__init__)


def test_sparql_groupgraphpattern_constructor_args():
    sig = inspect.signature(sparql_GroupGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_ConditionalOrExpression)


def test_sparql_conditionalorexpression_constructor_exists():
    assert callable(sparql_ConditionalOrExpression.__init__)


def test_sparql_conditionalorexpression_constructor_args():
    sig = inspect.signature(sparql_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_verb_is_not_abstract():
    assert not inspect.isabstract(sparql_Verb)


def test_sparql_verb_constructor_exists():
    assert callable(sparql_Verb.__init__)


def test_sparql_verb_constructor_args():
    sig = inspect.signature(sparql_Verb.__init__)
    params = list(sig.parameters.keys())



def test_sparql_sparqlqueries_is_not_abstract():
    assert not inspect.isabstract(sparql_SparqlQueries)


def test_sparql_sparqlqueries_constructor_exists():
    assert callable(sparql_SparqlQueries.__init__)


def test_sparql_sparqlqueries_constructor_args():
    sig = inspect.signature(sparql_SparqlQueries.__init__)
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
sparql_ANON_strategy = st.builds(
    sparql_ANON,
)
sparql_BLANK_NODE_LABEL_strategy = st.builds(
    sparql_BLANK_NODE_LABEL,
    pn_local=
        safe_text
)
AscOrDecs_strategy = st.builds(
    AscOrDecs,
)
sparql_DescendingLiteral_strategy = st.builds(
    sparql_DescendingLiteral,
)
sparql_AscendingLiteral_strategy = st.builds(
    sparql_AscendingLiteral,
)
StringLiteral_strategy = st.builds(
    StringLiteral,
)
sparql_STRING_LITERAL_LONG1_strategy = st.builds(
    sparql_STRING_LITERAL_LONG1,
    string=
        safe_text
)
sparql_STRING_LITERAL_LONG2_strategy = st.builds(
    sparql_STRING_LITERAL_LONG2,
    string=
        safe_text
)
sparql_STRING_LITERAL2_strategy = st.builds(
    sparql_STRING_LITERAL2,
    string=
        safe_text
)
sparql_STRING_LITERAL1_strategy = st.builds(
    sparql_STRING_LITERAL1,
    string=
        safe_text
)
sparql_VAR2_strategy = st.builds(
    sparql_VAR2,
)
sparql_VAR1_strategy = st.builds(
    sparql_VAR1,
)
BooleanLiteral_strategy = st.builds(
    BooleanLiteral,
)
sparql_FalseBooleanLiteralNE_strategy = st.builds(
    sparql_FalseBooleanLiteralNE,
)
sparql_TrueBooleanLiteralNE_strategy = st.builds(
    sparql_TrueBooleanLiteralNE,
)
PrefixedName_strategy = st.builds(
    PrefixedName,
)
sparql_StringLiteral_strategy = st.builds(
    sparql_StringLiteral,
)
LANGTAGOrIRIrefNE_strategy = st.builds(
    LANGTAGOrIRIrefNE,
)
sparql_LANGTAG_strategy = st.builds(
    sparql_LANGTAG,
    langtag=
        safe_text
)
sparql_UpIRIrefNE_strategy = st.builds(
    sparql_UpIRIrefNE,
)
AdditionalUnaryExpressionNE_strategy = st.builds(
    AdditionalUnaryExpressionNE,
)
sparql_TimesAdditionalUnaryExpressionNE_strategy = st.builds(
    sparql_TimesAdditionalUnaryExpressionNE,
)
NumericLiteral_strategy = st.builds(
    NumericLiteral,
)
sparql_DOUBLE_strategy = st.builds(
    sparql_DOUBLE,
    double=
        safe_text
)
sparql_DECIMAL_strategy = st.builds(
    sparql_DECIMAL,
    decimal=
        safe_text
)
sparql_NumericLiteralUnsigned_strategy = st.builds(
    sparql_NumericLiteralUnsigned,
)
AdditionalMultiplicativeExpressionNE_strategy = st.builds(
    AdditionalMultiplicativeExpressionNE,
)
sparql_MinusMultiplicativeExpressionNE_strategy = st.builds(
    sparql_MinusMultiplicativeExpressionNE,
)
sparql_NumericLiteralNegative_strategy = st.builds(
    sparql_NumericLiteralNegative,
)
sparql_NumericLiteralPositive_strategy = st.builds(
    sparql_NumericLiteralPositive,
)
sparql_PlusMultiplicativeExpressionNE_strategy = st.builds(
    sparql_PlusMultiplicativeExpressionNE,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
sparql_PrimaryExpression_strategy = st.builds(
    sparql_PrimaryExpression,
)
sparql_MinusPrimaryExpressionNE_strategy = st.builds(
    sparql_MinusPrimaryExpressionNE,
)
sparql_PlusPrimaryExpressionNE_strategy = st.builds(
    sparql_PlusPrimaryExpressionNE,
)
sparql_NotPrimaryExpressionNE_strategy = st.builds(
    sparql_NotPrimaryExpressionNE,
)
sparql_DividedByAdditionalUnaryExpressionNE_strategy = st.builds(
    sparql_DividedByAdditionalUnaryExpressionNE,
)
AdditionalNumericExpressionNE_strategy = st.builds(
    AdditionalNumericExpressionNE,
)
sparql_SmallerOrEqualNumericExpressionNE_strategy = st.builds(
    sparql_SmallerOrEqualNumericExpressionNE,
)
sparql_BiggerNumericExpressionNE_strategy = st.builds(
    sparql_BiggerNumericExpressionNE,
)
sparql_SmallerNumericExpressionNE_strategy = st.builds(
    sparql_SmallerNumericExpressionNE,
)
sparql_BiggerOrEqualNumericExpressionNE_strategy = st.builds(
    sparql_BiggerOrEqualNumericExpressionNE,
)
sparql_NotEqualNumericExpressionNE_strategy = st.builds(
    sparql_NotEqualNumericExpressionNE,
)
sparql_EqualsNumericExpressionNE_strategy = st.builds(
    sparql_EqualsNumericExpressionNE,
)
ArgList_strategy = st.builds(
    ArgList,
)
sparql_ArgListExpressionNE_strategy = st.builds(
    sparql_ArgListExpressionNE,
)
sparql_ArgListNILNE_strategy = st.builds(
    sparql_ArgListNILNE,
)
BuiltInCall_strategy = st.builds(
    BuiltInCall,
)
sparql_IsBlankBuiltInCallNE_strategy = st.builds(
    sparql_IsBlankBuiltInCallNE,
)
sparql_RegexExpression_strategy = st.builds(
    sparql_RegexExpression,
)
sparql_LangmatchesBuiltInCallNE_strategy = st.builds(
    sparql_LangmatchesBuiltInCallNE,
)
sparql_IsURIBuiltInCallNE_strategy = st.builds(
    sparql_IsURIBuiltInCallNE,
)
sparql_LangBuiltInCallNE_strategy = st.builds(
    sparql_LangBuiltInCallNE,
)
sparql_DatatypeBuiltInCallNE_strategy = st.builds(
    sparql_DatatypeBuiltInCallNE,
)
sparql_IsLiteralBuiltInCallNE_strategy = st.builds(
    sparql_IsLiteralBuiltInCallNE,
)
sparql_IsIRIBuiltInCallNE_strategy = st.builds(
    sparql_IsIRIBuiltInCallNE,
)
sparql_StrBuiltInCallNE_strategy = st.builds(
    sparql_StrBuiltInCallNE,
)
Constraint_strategy = st.builds(
    Constraint,
)
sparql_FunctionCall_strategy = st.builds(
    sparql_FunctionCall,
)
sparql_SameTermBuiltInCallNE_strategy = st.builds(
    sparql_SameTermBuiltInCallNE,
)
sparql_BoundBuiltInCallNE_strategy = st.builds(
    sparql_BoundBuiltInCallNE,
)
TriplesNode_strategy = st.builds(
    TriplesNode,
)
sparql_BlankNodePropertyList_strategy = st.builds(
    sparql_BlankNodePropertyList,
)
sparql_Collection_strategy = st.builds(
    sparql_Collection,
)
GraphNode_strategy = st.builds(
    GraphNode,
)
sparql_PatternOrFilterNE_strategy = st.builds(
    sparql_PatternOrFilterNE,
)
sparql_VarOrTerm_strategy = st.builds(
    sparql_VarOrTerm,
)
TriplesSameSubject_strategy = st.builds(
    TriplesSameSubject,
)
sparql_TriplesSameSubjectLeftNE_strategy = st.builds(
    sparql_TriplesSameSubjectLeftNE,
)
sparql_TriplesBlock_strategy = st.builds(
    sparql_TriplesBlock,
)
GraphPatternNotTriples_strategy = st.builds(
    GraphPatternNotTriples,
)
sparql_GraphGraphPattern_strategy = st.builds(
    sparql_GraphGraphPattern,
)
sparql_GroupOrUnionGraphPattern_strategy = st.builds(
    sparql_GroupOrUnionGraphPattern,
)
sparql_OptionalGraphPattern_strategy = st.builds(
    sparql_OptionalGraphPattern,
)
PatternOrFilterNE_strategy = st.builds(
    PatternOrFilterNE,
)
sparql_Filter_strategy = st.builds(
    sparql_Filter,
)
sparql_GraphPatternNotTriples_strategy = st.builds(
    sparql_GraphPatternNotTriples,
)
sparql_TriplesNode_strategy = st.builds(
    sparql_TriplesNode,
)
sparql_TriplesSameSubjectRightNE_strategy = st.builds(
    sparql_TriplesSameSubjectRightNE,
)
IRIreference_strategy = st.builds(
    IRIreference,
)
sparql_PrefixedName_strategy = st.builds(
    sparql_PrefixedName,
)
SourceSelector_strategy = st.builds(
    SourceSelector,
)
GraphTerm_strategy = st.builds(
    GraphTerm,
)
sparql_BlankNode_strategy = st.builds(
    sparql_BlankNode,
)
sparql_NotInList_strategy = st.builds(
    sparql_NotInList,
)
sparql_WhereLiteral_strategy = st.builds(
    sparql_WhereLiteral,
)
GraphClauseNE_strategy = st.builds(
    GraphClauseNE,
)
sparql_NamedGraphClause_strategy = st.builds(
    sparql_NamedGraphClause,
)
sparql_DefaultGraphClause_strategy = st.builds(
    sparql_DefaultGraphClause,
)
OrderConditionRightNE_strategy = st.builds(
    OrderConditionRightNE,
)
sparql_Constraint_strategy = st.builds(
    sparql_Constraint,
)
VarOrTerm_strategy = st.builds(
    VarOrTerm,
)
sparql_GraphTerm_strategy = st.builds(
    sparql_GraphTerm,
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
sparql_RDFLiteral_strategy = st.builds(
    sparql_RDFLiteral,
)
sparql_BuiltInCall_strategy = st.builds(
    sparql_BuiltInCall,
)
sparql_IRIrefOrFunction_strategy = st.builds(
    sparql_IRIrefOrFunction,
)
sparql_NumericLiteral_strategy = st.builds(
    sparql_NumericLiteral,
)
sparql_BooleanLiteral_strategy = st.builds(
    sparql_BooleanLiteral,
)
VarOrIRIref_strategy = st.builds(
    VarOrIRIref,
)
sparql_PNAME_LN_strategy = st.builds(
    sparql_PNAME_LN,
)
sparql_IRIreference_strategy = st.builds(
    sparql_IRIreference,
)
Verb_strategy = st.builds(
    Verb,
)
sparql_VerbANE_strategy = st.builds(
    sparql_VerbANE,
    theA=
        safe_text
)
VariablesNE_strategy = st.builds(
    VariablesNE,
)
sparql_SomeVariablesNE_strategy = st.builds(
    sparql_SomeVariablesNE,
)
sparql_AllVariablesNE_strategy = st.builds(
    sparql_AllVariablesNE,
)
SolutionsDisplayNE_strategy = st.builds(
    SolutionsDisplayNE,
)
sparql_ReducedNE_strategy = st.builds(
    sparql_ReducedNE,
)
sparql_DistinctNE_strategy = st.builds(
    sparql_DistinctNE,
)
sparql_INTEGER_strategy = st.builds(
    sparql_INTEGER,
    integer=
        safe_text
)
LimitOffsetClauses_strategy = st.builds(
    LimitOffsetClauses,
)
sparql_LimitOffsetClausesRightNE_strategy = st.builds(
    sparql_LimitOffsetClausesRightNE,
)
sparql_LimitOffsetClausesLeftNE_strategy = st.builds(
    sparql_LimitOffsetClausesLeftNE,
)
sparql_BrackettedExpression_strategy = st.builds(
    sparql_BrackettedExpression,
)
sparql_AscOrDecs_strategy = st.builds(
    sparql_AscOrDecs,
)
OrderCondition_strategy = st.builds(
    OrderCondition,
)
sparql_OrderConditionRightNE_strategy = st.builds(
    sparql_OrderConditionRightNE,
)
sparql_OrderConditionLeftNE_strategy = st.builds(
    sparql_OrderConditionLeftNE,
)
sparql_VarOrIRIref_strategy = st.builds(
    sparql_VarOrIRIref,
)
Query_strategy = st.builds(
    Query,
)
sparql_AskQuery_strategy = st.builds(
    sparql_AskQuery,
)
sparql_DescribeQuery_strategy = st.builds(
    sparql_DescribeQuery,
)
sparql_ConstructQuery_strategy = st.builds(
    sparql_ConstructQuery,
)
sparql_SelectQuery_strategy = st.builds(
    sparql_SelectQuery,
)
sparql_PNAME_NS_strategy = st.builds(
    sparql_PNAME_NS,
    pn_prefix=
        safe_text
)
sparql_Var_strategy = st.builds(
    sparql_Var,
    varname=
        safe_text
)
sparql_LocatedElement_strategy = st.builds(
    sparql_LocatedElement,
    location=
        safe_text,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text
)
sparql_IRI_REF_strategy = st.builds(
    sparql_IRI_REF,
    iri_ref=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
sparql_OffsetClause_strategy = st.builds(
    sparql_OffsetClause,
)
sparql_TriplesSameSubject_strategy = st.builds(
    sparql_TriplesSameSubject,
)
sparql_PropertyListNotEmpty_strategy = st.builds(
    sparql_PropertyListNotEmpty,
)
sparql_OrderCondition_strategy = st.builds(
    sparql_OrderCondition,
)
sparql_WS_strategy = st.builds(
    sparql_WS,
    ws=
        safe_text
)
sparql_AdditionalNumericExpressionNE_strategy = st.builds(
    sparql_AdditionalNumericExpressionNE,
)
sparql_Object_strategy = st.builds(
    sparql_Object,
)
sparql_AdditionalExpressionNE_strategy = st.builds(
    sparql_AdditionalExpressionNE,
)
sparql_AdditiveExpression_strategy = st.builds(
    sparql_AdditiveExpression,
)
sparql_VariablesNE_strategy = st.builds(
    sparql_VariablesNE,
)
sparql_Prologue_strategy = st.builds(
    sparql_Prologue,
)
sparql_PrefixDecl_strategy = st.builds(
    sparql_PrefixDecl,
)
sparql_AdditionalConditionalAndExpressionNE_strategy = st.builds(
    sparql_AdditionalConditionalAndExpressionNE,
)
sparql_ArgList_strategy = st.builds(
    sparql_ArgList,
)
sparql_Query_strategy = st.builds(
    sparql_Query,
)
sparql_LANGTAGOrIRIrefNE_strategy = st.builds(
    sparql_LANGTAGOrIRIrefNE,
)
sparql_WhereClause_strategy = st.builds(
    sparql_WhereClause,
)
sparql_OrderClause_strategy = st.builds(
    sparql_OrderClause,
)
sparql_VARNAME_strategy = st.builds(
    sparql_VARNAME,
    varname=
        safe_text
)
sparql_NumericExpression_strategy = st.builds(
    sparql_NumericExpression,
)
sparql_DatasetClause_strategy = st.builds(
    sparql_DatasetClause,
)
sparql_PN_LOCAL_strategy = st.builds(
    sparql_PN_LOCAL,
    pn_local=
        safe_text
)
sparql_AdditionalMultiplicativeExpressionNE_strategy = st.builds(
    sparql_AdditionalMultiplicativeExpressionNE,
)
sparql_LimitOffsetClauses_strategy = st.builds(
    sparql_LimitOffsetClauses,
)
sparql_PN_PREFIX_strategy = st.builds(
    sparql_PN_PREFIX,
    pn_prefix=
        safe_text
)
sparql_AdditionalUnaryExpressionNE_strategy = st.builds(
    sparql_AdditionalUnaryExpressionNE,
)
sparql_UnaryExpression_strategy = st.builds(
    sparql_UnaryExpression,
)
sparql_SolutionsDisplayNE_strategy = st.builds(
    sparql_SolutionsDisplayNE,
)
sparql_LimitClause_strategy = st.builds(
    sparql_LimitClause,
)
sparql_BaseDecl_strategy = st.builds(
    sparql_BaseDecl,
)
sparql_ValueLogical_strategy = st.builds(
    sparql_ValueLogical,
)
sparql_ObjectList_strategy = st.builds(
    sparql_ObjectList,
)
sparql_GraphClauseNE_strategy = st.builds(
    sparql_GraphClauseNE,
)
sparql_Expression_strategy = st.builds(
    sparql_Expression,
)
sparql_SolutionModifier_strategy = st.builds(
    sparql_SolutionModifier,
)
sparql_GraphNode_strategy = st.builds(
    sparql_GraphNode,
)
sparql_AdditionalGGPElement_strategy = st.builds(
    sparql_AdditionalGGPElement,
)
sparql_RelationalExpression_strategy = st.builds(
    sparql_RelationalExpression,
)
sparql_ConditionalAndExpression_strategy = st.builds(
    sparql_ConditionalAndExpression,
)
sparql_ConstructTemplate_strategy = st.builds(
    sparql_ConstructTemplate,
)
sparql_MultiplicativeExpression_strategy = st.builds(
    sparql_MultiplicativeExpression,
)
sparql_SourceSelector_strategy = st.builds(
    sparql_SourceSelector,
)
sparql_AdditionalValueLogicalNE_strategy = st.builds(
    sparql_AdditionalValueLogicalNE,
)
sparql_GroupGraphPattern_strategy = st.builds(
    sparql_GroupGraphPattern,
)
sparql_ConditionalOrExpression_strategy = st.builds(
    sparql_ConditionalOrExpression,
)
sparql_Verb_strategy = st.builds(
    sparql_Verb,
)
sparql_SparqlQueries_strategy = st.builds(
    sparql_SparqlQueries,
)

@given(instance=BlankNode_strategy)
@settings(max_examples=50)
def test_blanknode_instantiation(instance):
    assert isinstance(instance, BlankNode)

@given(instance=sparql_ANON_strategy)
@settings(max_examples=50)
def test_sparql_anon_instantiation(instance):
    assert isinstance(instance, sparql_ANON)

@given(instance=sparql_BLANK_NODE_LABEL_strategy)
@settings(max_examples=50)
def test_sparql_blank_node_label_instantiation(instance):
    assert isinstance(instance, sparql_BLANK_NODE_LABEL)



@given(instance=sparql_BLANK_NODE_LABEL_strategy)
def test_sparql_blank_node_label_pn_local_setter(instance):
    original = instance.pn_local
    instance.pn_local = original
    assert instance.pn_local == original

@given(instance=AscOrDecs_strategy)
@settings(max_examples=50)
def test_ascordecs_instantiation(instance):
    assert isinstance(instance, AscOrDecs)

@given(instance=sparql_DescendingLiteral_strategy)
@settings(max_examples=50)
def test_sparql_descendingliteral_instantiation(instance):
    assert isinstance(instance, sparql_DescendingLiteral)

@given(instance=sparql_AscendingLiteral_strategy)
@settings(max_examples=50)
def test_sparql_ascendingliteral_instantiation(instance):
    assert isinstance(instance, sparql_AscendingLiteral)

@given(instance=StringLiteral_strategy)
@settings(max_examples=50)
def test_stringliteral_instantiation(instance):
    assert isinstance(instance, StringLiteral)

@given(instance=sparql_STRING_LITERAL_LONG1_strategy)
@settings(max_examples=50)
def test_sparql_string_literal_long1_instantiation(instance):
    assert isinstance(instance, sparql_STRING_LITERAL_LONG1)



@given(instance=sparql_STRING_LITERAL_LONG1_strategy)
def test_sparql_string_literal_long1_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=sparql_STRING_LITERAL_LONG2_strategy)
@settings(max_examples=50)
def test_sparql_string_literal_long2_instantiation(instance):
    assert isinstance(instance, sparql_STRING_LITERAL_LONG2)



@given(instance=sparql_STRING_LITERAL_LONG2_strategy)
def test_sparql_string_literal_long2_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=sparql_STRING_LITERAL2_strategy)
@settings(max_examples=50)
def test_sparql_string_literal2_instantiation(instance):
    assert isinstance(instance, sparql_STRING_LITERAL2)



@given(instance=sparql_STRING_LITERAL2_strategy)
def test_sparql_string_literal2_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=sparql_STRING_LITERAL1_strategy)
@settings(max_examples=50)
def test_sparql_string_literal1_instantiation(instance):
    assert isinstance(instance, sparql_STRING_LITERAL1)



@given(instance=sparql_STRING_LITERAL1_strategy)
def test_sparql_string_literal1_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=sparql_VAR2_strategy)
@settings(max_examples=50)
def test_sparql_var2_instantiation(instance):
    assert isinstance(instance, sparql_VAR2)

@given(instance=sparql_VAR1_strategy)
@settings(max_examples=50)
def test_sparql_var1_instantiation(instance):
    assert isinstance(instance, sparql_VAR1)

@given(instance=BooleanLiteral_strategy)
@settings(max_examples=50)
def test_booleanliteral_instantiation(instance):
    assert isinstance(instance, BooleanLiteral)

@given(instance=sparql_FalseBooleanLiteralNE_strategy)
@settings(max_examples=50)
def test_sparql_falsebooleanliteralne_instantiation(instance):
    assert isinstance(instance, sparql_FalseBooleanLiteralNE)

@given(instance=sparql_TrueBooleanLiteralNE_strategy)
@settings(max_examples=50)
def test_sparql_truebooleanliteralne_instantiation(instance):
    assert isinstance(instance, sparql_TrueBooleanLiteralNE)

@given(instance=PrefixedName_strategy)
@settings(max_examples=50)
def test_prefixedname_instantiation(instance):
    assert isinstance(instance, PrefixedName)

@given(instance=sparql_StringLiteral_strategy)
@settings(max_examples=50)
def test_sparql_stringliteral_instantiation(instance):
    assert isinstance(instance, sparql_StringLiteral)

@given(instance=LANGTAGOrIRIrefNE_strategy)
@settings(max_examples=50)
def test_langtagoririrefne_instantiation(instance):
    assert isinstance(instance, LANGTAGOrIRIrefNE)

@given(instance=sparql_LANGTAG_strategy)
@settings(max_examples=50)
def test_sparql_langtag_instantiation(instance):
    assert isinstance(instance, sparql_LANGTAG)



@given(instance=sparql_LANGTAG_strategy)
def test_sparql_langtag_langtag_setter(instance):
    original = instance.langtag
    instance.langtag = original
    assert instance.langtag == original

@given(instance=sparql_UpIRIrefNE_strategy)
@settings(max_examples=50)
def test_sparql_upirirefne_instantiation(instance):
    assert isinstance(instance, sparql_UpIRIrefNE)

@given(instance=AdditionalUnaryExpressionNE_strategy)
@settings(max_examples=50)
def test_additionalunaryexpressionne_instantiation(instance):
    assert isinstance(instance, AdditionalUnaryExpressionNE)

@given(instance=sparql_TimesAdditionalUnaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_timesadditionalunaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_TimesAdditionalUnaryExpressionNE)

@given(instance=NumericLiteral_strategy)
@settings(max_examples=50)
def test_numericliteral_instantiation(instance):
    assert isinstance(instance, NumericLiteral)

@given(instance=sparql_DOUBLE_strategy)
@settings(max_examples=50)
def test_sparql_double_instantiation(instance):
    assert isinstance(instance, sparql_DOUBLE)



@given(instance=sparql_DOUBLE_strategy)
def test_sparql_double_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original

@given(instance=sparql_DECIMAL_strategy)
@settings(max_examples=50)
def test_sparql_decimal_instantiation(instance):
    assert isinstance(instance, sparql_DECIMAL)



@given(instance=sparql_DECIMAL_strategy)
def test_sparql_decimal_decimal_setter(instance):
    original = instance.decimal
    instance.decimal = original
    assert instance.decimal == original

@given(instance=sparql_NumericLiteralUnsigned_strategy)
@settings(max_examples=50)
def test_sparql_numericliteralunsigned_instantiation(instance):
    assert isinstance(instance, sparql_NumericLiteralUnsigned)

@given(instance=AdditionalMultiplicativeExpressionNE_strategy)
@settings(max_examples=50)
def test_additionalmultiplicativeexpressionne_instantiation(instance):
    assert isinstance(instance, AdditionalMultiplicativeExpressionNE)

@given(instance=sparql_MinusMultiplicativeExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_minusmultiplicativeexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_MinusMultiplicativeExpressionNE)

@given(instance=sparql_NumericLiteralNegative_strategy)
@settings(max_examples=50)
def test_sparql_numericliteralnegative_instantiation(instance):
    assert isinstance(instance, sparql_NumericLiteralNegative)

@given(instance=sparql_NumericLiteralPositive_strategy)
@settings(max_examples=50)
def test_sparql_numericliteralpositive_instantiation(instance):
    assert isinstance(instance, sparql_NumericLiteralPositive)

@given(instance=sparql_PlusMultiplicativeExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_plusmultiplicativeexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_PlusMultiplicativeExpressionNE)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=sparql_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_sparql_primaryexpression_instantiation(instance):
    assert isinstance(instance, sparql_PrimaryExpression)

@given(instance=sparql_MinusPrimaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_minusprimaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_MinusPrimaryExpressionNE)

@given(instance=sparql_PlusPrimaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_plusprimaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_PlusPrimaryExpressionNE)

@given(instance=sparql_NotPrimaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_notprimaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_NotPrimaryExpressionNE)

@given(instance=sparql_DividedByAdditionalUnaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_dividedbyadditionalunaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_DividedByAdditionalUnaryExpressionNE)

@given(instance=AdditionalNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_additionalnumericexpressionne_instantiation(instance):
    assert isinstance(instance, AdditionalNumericExpressionNE)

@given(instance=sparql_SmallerOrEqualNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_smallerorequalnumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_SmallerOrEqualNumericExpressionNE)

@given(instance=sparql_BiggerNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_biggernumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_BiggerNumericExpressionNE)

@given(instance=sparql_SmallerNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_smallernumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_SmallerNumericExpressionNE)

@given(instance=sparql_BiggerOrEqualNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_biggerorequalnumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_BiggerOrEqualNumericExpressionNE)

@given(instance=sparql_NotEqualNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_notequalnumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_NotEqualNumericExpressionNE)

@given(instance=sparql_EqualsNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_equalsnumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_EqualsNumericExpressionNE)

@given(instance=ArgList_strategy)
@settings(max_examples=50)
def test_arglist_instantiation(instance):
    assert isinstance(instance, ArgList)

@given(instance=sparql_ArgListExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_arglistexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_ArgListExpressionNE)

@given(instance=sparql_ArgListNILNE_strategy)
@settings(max_examples=50)
def test_sparql_arglistnilne_instantiation(instance):
    assert isinstance(instance, sparql_ArgListNILNE)

@given(instance=BuiltInCall_strategy)
@settings(max_examples=50)
def test_builtincall_instantiation(instance):
    assert isinstance(instance, BuiltInCall)

@given(instance=sparql_IsBlankBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql_isblankbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql_IsBlankBuiltInCallNE)

@given(instance=sparql_RegexExpression_strategy)
@settings(max_examples=50)
def test_sparql_regexexpression_instantiation(instance):
    assert isinstance(instance, sparql_RegexExpression)

@given(instance=sparql_LangmatchesBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql_langmatchesbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql_LangmatchesBuiltInCallNE)

@given(instance=sparql_IsURIBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql_isuribuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql_IsURIBuiltInCallNE)

@given(instance=sparql_LangBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql_langbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql_LangBuiltInCallNE)

@given(instance=sparql_DatatypeBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql_datatypebuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql_DatatypeBuiltInCallNE)

@given(instance=sparql_IsLiteralBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql_isliteralbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql_IsLiteralBuiltInCallNE)

@given(instance=sparql_IsIRIBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql_isiribuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql_IsIRIBuiltInCallNE)

@given(instance=sparql_StrBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql_strbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql_StrBuiltInCallNE)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=sparql_FunctionCall_strategy)
@settings(max_examples=50)
def test_sparql_functioncall_instantiation(instance):
    assert isinstance(instance, sparql_FunctionCall)

@given(instance=sparql_SameTermBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql_sametermbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql_SameTermBuiltInCallNE)

@given(instance=sparql_BoundBuiltInCallNE_strategy)
@settings(max_examples=50)
def test_sparql_boundbuiltincallne_instantiation(instance):
    assert isinstance(instance, sparql_BoundBuiltInCallNE)

@given(instance=TriplesNode_strategy)
@settings(max_examples=50)
def test_triplesnode_instantiation(instance):
    assert isinstance(instance, TriplesNode)

@given(instance=sparql_BlankNodePropertyList_strategy)
@settings(max_examples=50)
def test_sparql_blanknodepropertylist_instantiation(instance):
    assert isinstance(instance, sparql_BlankNodePropertyList)

@given(instance=sparql_Collection_strategy)
@settings(max_examples=50)
def test_sparql_collection_instantiation(instance):
    assert isinstance(instance, sparql_Collection)

@given(instance=GraphNode_strategy)
@settings(max_examples=50)
def test_graphnode_instantiation(instance):
    assert isinstance(instance, GraphNode)

@given(instance=sparql_PatternOrFilterNE_strategy)
@settings(max_examples=50)
def test_sparql_patternorfilterne_instantiation(instance):
    assert isinstance(instance, sparql_PatternOrFilterNE)

@given(instance=sparql_VarOrTerm_strategy)
@settings(max_examples=50)
def test_sparql_varorterm_instantiation(instance):
    assert isinstance(instance, sparql_VarOrTerm)

@given(instance=TriplesSameSubject_strategy)
@settings(max_examples=50)
def test_triplessamesubject_instantiation(instance):
    assert isinstance(instance, TriplesSameSubject)

@given(instance=sparql_TriplesSameSubjectLeftNE_strategy)
@settings(max_examples=50)
def test_sparql_triplessamesubjectleftne_instantiation(instance):
    assert isinstance(instance, sparql_TriplesSameSubjectLeftNE)

@given(instance=sparql_TriplesBlock_strategy)
@settings(max_examples=50)
def test_sparql_triplesblock_instantiation(instance):
    assert isinstance(instance, sparql_TriplesBlock)

@given(instance=GraphPatternNotTriples_strategy)
@settings(max_examples=50)
def test_graphpatternnottriples_instantiation(instance):
    assert isinstance(instance, GraphPatternNotTriples)

@given(instance=sparql_GraphGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql_graphgraphpattern_instantiation(instance):
    assert isinstance(instance, sparql_GraphGraphPattern)

@given(instance=sparql_GroupOrUnionGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql_grouporuniongraphpattern_instantiation(instance):
    assert isinstance(instance, sparql_GroupOrUnionGraphPattern)

@given(instance=sparql_OptionalGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql_optionalgraphpattern_instantiation(instance):
    assert isinstance(instance, sparql_OptionalGraphPattern)

@given(instance=PatternOrFilterNE_strategy)
@settings(max_examples=50)
def test_patternorfilterne_instantiation(instance):
    assert isinstance(instance, PatternOrFilterNE)

@given(instance=sparql_Filter_strategy)
@settings(max_examples=50)
def test_sparql_filter_instantiation(instance):
    assert isinstance(instance, sparql_Filter)

@given(instance=sparql_GraphPatternNotTriples_strategy)
@settings(max_examples=50)
def test_sparql_graphpatternnottriples_instantiation(instance):
    assert isinstance(instance, sparql_GraphPatternNotTriples)

@given(instance=sparql_TriplesNode_strategy)
@settings(max_examples=50)
def test_sparql_triplesnode_instantiation(instance):
    assert isinstance(instance, sparql_TriplesNode)

@given(instance=sparql_TriplesSameSubjectRightNE_strategy)
@settings(max_examples=50)
def test_sparql_triplessamesubjectrightne_instantiation(instance):
    assert isinstance(instance, sparql_TriplesSameSubjectRightNE)

@given(instance=IRIreference_strategy)
@settings(max_examples=50)
def test_irireference_instantiation(instance):
    assert isinstance(instance, IRIreference)

@given(instance=sparql_PrefixedName_strategy)
@settings(max_examples=50)
def test_sparql_prefixedname_instantiation(instance):
    assert isinstance(instance, sparql_PrefixedName)

@given(instance=SourceSelector_strategy)
@settings(max_examples=50)
def test_sourceselector_instantiation(instance):
    assert isinstance(instance, SourceSelector)

@given(instance=GraphTerm_strategy)
@settings(max_examples=50)
def test_graphterm_instantiation(instance):
    assert isinstance(instance, GraphTerm)

@given(instance=sparql_BlankNode_strategy)
@settings(max_examples=50)
def test_sparql_blanknode_instantiation(instance):
    assert isinstance(instance, sparql_BlankNode)

@given(instance=sparql_NotInList_strategy)
@settings(max_examples=50)
def test_sparql_notinlist_instantiation(instance):
    assert isinstance(instance, sparql_NotInList)

@given(instance=sparql_WhereLiteral_strategy)
@settings(max_examples=50)
def test_sparql_whereliteral_instantiation(instance):
    assert isinstance(instance, sparql_WhereLiteral)

@given(instance=GraphClauseNE_strategy)
@settings(max_examples=50)
def test_graphclausene_instantiation(instance):
    assert isinstance(instance, GraphClauseNE)

@given(instance=sparql_NamedGraphClause_strategy)
@settings(max_examples=50)
def test_sparql_namedgraphclause_instantiation(instance):
    assert isinstance(instance, sparql_NamedGraphClause)

@given(instance=sparql_DefaultGraphClause_strategy)
@settings(max_examples=50)
def test_sparql_defaultgraphclause_instantiation(instance):
    assert isinstance(instance, sparql_DefaultGraphClause)

@given(instance=OrderConditionRightNE_strategy)
@settings(max_examples=50)
def test_orderconditionrightne_instantiation(instance):
    assert isinstance(instance, OrderConditionRightNE)

@given(instance=sparql_Constraint_strategy)
@settings(max_examples=50)
def test_sparql_constraint_instantiation(instance):
    assert isinstance(instance, sparql_Constraint)

@given(instance=VarOrTerm_strategy)
@settings(max_examples=50)
def test_varorterm_instantiation(instance):
    assert isinstance(instance, VarOrTerm)

@given(instance=sparql_GraphTerm_strategy)
@settings(max_examples=50)
def test_sparql_graphterm_instantiation(instance):
    assert isinstance(instance, sparql_GraphTerm)

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=sparql_RDFLiteral_strategy)
@settings(max_examples=50)
def test_sparql_rdfliteral_instantiation(instance):
    assert isinstance(instance, sparql_RDFLiteral)

@given(instance=sparql_BuiltInCall_strategy)
@settings(max_examples=50)
def test_sparql_builtincall_instantiation(instance):
    assert isinstance(instance, sparql_BuiltInCall)

@given(instance=sparql_IRIrefOrFunction_strategy)
@settings(max_examples=50)
def test_sparql_irireforfunction_instantiation(instance):
    assert isinstance(instance, sparql_IRIrefOrFunction)

@given(instance=sparql_NumericLiteral_strategy)
@settings(max_examples=50)
def test_sparql_numericliteral_instantiation(instance):
    assert isinstance(instance, sparql_NumericLiteral)

@given(instance=sparql_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_sparql_booleanliteral_instantiation(instance):
    assert isinstance(instance, sparql_BooleanLiteral)

@given(instance=VarOrIRIref_strategy)
@settings(max_examples=50)
def test_varoririref_instantiation(instance):
    assert isinstance(instance, VarOrIRIref)

@given(instance=sparql_PNAME_LN_strategy)
@settings(max_examples=50)
def test_sparql_pname_ln_instantiation(instance):
    assert isinstance(instance, sparql_PNAME_LN)

@given(instance=sparql_IRIreference_strategy)
@settings(max_examples=50)
def test_sparql_irireference_instantiation(instance):
    assert isinstance(instance, sparql_IRIreference)

@given(instance=Verb_strategy)
@settings(max_examples=50)
def test_verb_instantiation(instance):
    assert isinstance(instance, Verb)

@given(instance=sparql_VerbANE_strategy)
@settings(max_examples=50)
def test_sparql_verbane_instantiation(instance):
    assert isinstance(instance, sparql_VerbANE)



@given(instance=sparql_VerbANE_strategy)
def test_sparql_verbane_theA_setter(instance):
    original = instance.theA
    instance.theA = original
    assert instance.theA == original

@given(instance=VariablesNE_strategy)
@settings(max_examples=50)
def test_variablesne_instantiation(instance):
    assert isinstance(instance, VariablesNE)

@given(instance=sparql_SomeVariablesNE_strategy)
@settings(max_examples=50)
def test_sparql_somevariablesne_instantiation(instance):
    assert isinstance(instance, sparql_SomeVariablesNE)

@given(instance=sparql_AllVariablesNE_strategy)
@settings(max_examples=50)
def test_sparql_allvariablesne_instantiation(instance):
    assert isinstance(instance, sparql_AllVariablesNE)

@given(instance=SolutionsDisplayNE_strategy)
@settings(max_examples=50)
def test_solutionsdisplayne_instantiation(instance):
    assert isinstance(instance, SolutionsDisplayNE)

@given(instance=sparql_ReducedNE_strategy)
@settings(max_examples=50)
def test_sparql_reducedne_instantiation(instance):
    assert isinstance(instance, sparql_ReducedNE)

@given(instance=sparql_DistinctNE_strategy)
@settings(max_examples=50)
def test_sparql_distinctne_instantiation(instance):
    assert isinstance(instance, sparql_DistinctNE)

@given(instance=sparql_INTEGER_strategy)
@settings(max_examples=50)
def test_sparql_integer_instantiation(instance):
    assert isinstance(instance, sparql_INTEGER)



@given(instance=sparql_INTEGER_strategy)
def test_sparql_integer_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original

@given(instance=LimitOffsetClauses_strategy)
@settings(max_examples=50)
def test_limitoffsetclauses_instantiation(instance):
    assert isinstance(instance, LimitOffsetClauses)

@given(instance=sparql_LimitOffsetClausesRightNE_strategy)
@settings(max_examples=50)
def test_sparql_limitoffsetclausesrightne_instantiation(instance):
    assert isinstance(instance, sparql_LimitOffsetClausesRightNE)

@given(instance=sparql_LimitOffsetClausesLeftNE_strategy)
@settings(max_examples=50)
def test_sparql_limitoffsetclausesleftne_instantiation(instance):
    assert isinstance(instance, sparql_LimitOffsetClausesLeftNE)

@given(instance=sparql_BrackettedExpression_strategy)
@settings(max_examples=50)
def test_sparql_brackettedexpression_instantiation(instance):
    assert isinstance(instance, sparql_BrackettedExpression)

@given(instance=sparql_AscOrDecs_strategy)
@settings(max_examples=50)
def test_sparql_ascordecs_instantiation(instance):
    assert isinstance(instance, sparql_AscOrDecs)

@given(instance=OrderCondition_strategy)
@settings(max_examples=50)
def test_ordercondition_instantiation(instance):
    assert isinstance(instance, OrderCondition)

@given(instance=sparql_OrderConditionRightNE_strategy)
@settings(max_examples=50)
def test_sparql_orderconditionrightne_instantiation(instance):
    assert isinstance(instance, sparql_OrderConditionRightNE)

@given(instance=sparql_OrderConditionLeftNE_strategy)
@settings(max_examples=50)
def test_sparql_orderconditionleftne_instantiation(instance):
    assert isinstance(instance, sparql_OrderConditionLeftNE)

@given(instance=sparql_VarOrIRIref_strategy)
@settings(max_examples=50)
def test_sparql_varoririref_instantiation(instance):
    assert isinstance(instance, sparql_VarOrIRIref)

@given(instance=Query_strategy)
@settings(max_examples=50)
def test_query_instantiation(instance):
    assert isinstance(instance, Query)

@given(instance=sparql_AskQuery_strategy)
@settings(max_examples=50)
def test_sparql_askquery_instantiation(instance):
    assert isinstance(instance, sparql_AskQuery)

@given(instance=sparql_DescribeQuery_strategy)
@settings(max_examples=50)
def test_sparql_describequery_instantiation(instance):
    assert isinstance(instance, sparql_DescribeQuery)

@given(instance=sparql_ConstructQuery_strategy)
@settings(max_examples=50)
def test_sparql_constructquery_instantiation(instance):
    assert isinstance(instance, sparql_ConstructQuery)

@given(instance=sparql_SelectQuery_strategy)
@settings(max_examples=50)
def test_sparql_selectquery_instantiation(instance):
    assert isinstance(instance, sparql_SelectQuery)

@given(instance=sparql_PNAME_NS_strategy)
@settings(max_examples=50)
def test_sparql_pname_ns_instantiation(instance):
    assert isinstance(instance, sparql_PNAME_NS)



@given(instance=sparql_PNAME_NS_strategy)
def test_sparql_pname_ns_pn_prefix_setter(instance):
    original = instance.pn_prefix
    instance.pn_prefix = original
    assert instance.pn_prefix == original

@given(instance=sparql_Var_strategy)
@settings(max_examples=50)
def test_sparql_var_instantiation(instance):
    assert isinstance(instance, sparql_Var)



@given(instance=sparql_Var_strategy)
def test_sparql_var_varname_setter(instance):
    original = instance.varname
    instance.varname = original
    assert instance.varname == original

@given(instance=sparql_LocatedElement_strategy)
@settings(max_examples=50)
def test_sparql_locatedelement_instantiation(instance):
    assert isinstance(instance, sparql_LocatedElement)



@given(instance=sparql_LocatedElement_strategy)
def test_sparql_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=sparql_LocatedElement_strategy)
def test_sparql_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original



@given(instance=sparql_LocatedElement_strategy)
def test_sparql_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=sparql_IRI_REF_strategy)
@settings(max_examples=50)
def test_sparql_iri_ref_instantiation(instance):
    assert isinstance(instance, sparql_IRI_REF)



@given(instance=sparql_IRI_REF_strategy)
def test_sparql_iri_ref_iri_ref_setter(instance):
    original = instance.iri_ref
    instance.iri_ref = original
    assert instance.iri_ref == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=sparql_OffsetClause_strategy)
@settings(max_examples=50)
def test_sparql_offsetclause_instantiation(instance):
    assert isinstance(instance, sparql_OffsetClause)

@given(instance=sparql_TriplesSameSubject_strategy)
@settings(max_examples=50)
def test_sparql_triplessamesubject_instantiation(instance):
    assert isinstance(instance, sparql_TriplesSameSubject)

@given(instance=sparql_PropertyListNotEmpty_strategy)
@settings(max_examples=50)
def test_sparql_propertylistnotempty_instantiation(instance):
    assert isinstance(instance, sparql_PropertyListNotEmpty)

@given(instance=sparql_OrderCondition_strategy)
@settings(max_examples=50)
def test_sparql_ordercondition_instantiation(instance):
    assert isinstance(instance, sparql_OrderCondition)

@given(instance=sparql_WS_strategy)
@settings(max_examples=50)
def test_sparql_ws_instantiation(instance):
    assert isinstance(instance, sparql_WS)



@given(instance=sparql_WS_strategy)
def test_sparql_ws_ws_setter(instance):
    original = instance.ws
    instance.ws = original
    assert instance.ws == original

@given(instance=sparql_AdditionalNumericExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_additionalnumericexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_AdditionalNumericExpressionNE)

@given(instance=sparql_Object_strategy)
@settings(max_examples=50)
def test_sparql_object_instantiation(instance):
    assert isinstance(instance, sparql_Object)

@given(instance=sparql_AdditionalExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_additionalexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_AdditionalExpressionNE)

@given(instance=sparql_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_sparql_additiveexpression_instantiation(instance):
    assert isinstance(instance, sparql_AdditiveExpression)

@given(instance=sparql_VariablesNE_strategy)
@settings(max_examples=50)
def test_sparql_variablesne_instantiation(instance):
    assert isinstance(instance, sparql_VariablesNE)

@given(instance=sparql_Prologue_strategy)
@settings(max_examples=50)
def test_sparql_prologue_instantiation(instance):
    assert isinstance(instance, sparql_Prologue)

@given(instance=sparql_PrefixDecl_strategy)
@settings(max_examples=50)
def test_sparql_prefixdecl_instantiation(instance):
    assert isinstance(instance, sparql_PrefixDecl)

@given(instance=sparql_AdditionalConditionalAndExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_additionalconditionalandexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_AdditionalConditionalAndExpressionNE)

@given(instance=sparql_ArgList_strategy)
@settings(max_examples=50)
def test_sparql_arglist_instantiation(instance):
    assert isinstance(instance, sparql_ArgList)

@given(instance=sparql_Query_strategy)
@settings(max_examples=50)
def test_sparql_query_instantiation(instance):
    assert isinstance(instance, sparql_Query)

@given(instance=sparql_LANGTAGOrIRIrefNE_strategy)
@settings(max_examples=50)
def test_sparql_langtagoririrefne_instantiation(instance):
    assert isinstance(instance, sparql_LANGTAGOrIRIrefNE)

@given(instance=sparql_WhereClause_strategy)
@settings(max_examples=50)
def test_sparql_whereclause_instantiation(instance):
    assert isinstance(instance, sparql_WhereClause)

@given(instance=sparql_OrderClause_strategy)
@settings(max_examples=50)
def test_sparql_orderclause_instantiation(instance):
    assert isinstance(instance, sparql_OrderClause)

@given(instance=sparql_VARNAME_strategy)
@settings(max_examples=50)
def test_sparql_varname_instantiation(instance):
    assert isinstance(instance, sparql_VARNAME)



@given(instance=sparql_VARNAME_strategy)
def test_sparql_varname_varname_setter(instance):
    original = instance.varname
    instance.varname = original
    assert instance.varname == original

@given(instance=sparql_NumericExpression_strategy)
@settings(max_examples=50)
def test_sparql_numericexpression_instantiation(instance):
    assert isinstance(instance, sparql_NumericExpression)

@given(instance=sparql_DatasetClause_strategy)
@settings(max_examples=50)
def test_sparql_datasetclause_instantiation(instance):
    assert isinstance(instance, sparql_DatasetClause)

@given(instance=sparql_PN_LOCAL_strategy)
@settings(max_examples=50)
def test_sparql_pn_local_instantiation(instance):
    assert isinstance(instance, sparql_PN_LOCAL)



@given(instance=sparql_PN_LOCAL_strategy)
def test_sparql_pn_local_pn_local_setter(instance):
    original = instance.pn_local
    instance.pn_local = original
    assert instance.pn_local == original

@given(instance=sparql_AdditionalMultiplicativeExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_additionalmultiplicativeexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_AdditionalMultiplicativeExpressionNE)

@given(instance=sparql_LimitOffsetClauses_strategy)
@settings(max_examples=50)
def test_sparql_limitoffsetclauses_instantiation(instance):
    assert isinstance(instance, sparql_LimitOffsetClauses)

@given(instance=sparql_PN_PREFIX_strategy)
@settings(max_examples=50)
def test_sparql_pn_prefix_instantiation(instance):
    assert isinstance(instance, sparql_PN_PREFIX)



@given(instance=sparql_PN_PREFIX_strategy)
def test_sparql_pn_prefix_pn_prefix_setter(instance):
    original = instance.pn_prefix
    instance.pn_prefix = original
    assert instance.pn_prefix == original

@given(instance=sparql_AdditionalUnaryExpressionNE_strategy)
@settings(max_examples=50)
def test_sparql_additionalunaryexpressionne_instantiation(instance):
    assert isinstance(instance, sparql_AdditionalUnaryExpressionNE)

@given(instance=sparql_UnaryExpression_strategy)
@settings(max_examples=50)
def test_sparql_unaryexpression_instantiation(instance):
    assert isinstance(instance, sparql_UnaryExpression)

@given(instance=sparql_SolutionsDisplayNE_strategy)
@settings(max_examples=50)
def test_sparql_solutionsdisplayne_instantiation(instance):
    assert isinstance(instance, sparql_SolutionsDisplayNE)

@given(instance=sparql_LimitClause_strategy)
@settings(max_examples=50)
def test_sparql_limitclause_instantiation(instance):
    assert isinstance(instance, sparql_LimitClause)

@given(instance=sparql_BaseDecl_strategy)
@settings(max_examples=50)
def test_sparql_basedecl_instantiation(instance):
    assert isinstance(instance, sparql_BaseDecl)

@given(instance=sparql_ValueLogical_strategy)
@settings(max_examples=50)
def test_sparql_valuelogical_instantiation(instance):
    assert isinstance(instance, sparql_ValueLogical)

@given(instance=sparql_ObjectList_strategy)
@settings(max_examples=50)
def test_sparql_objectlist_instantiation(instance):
    assert isinstance(instance, sparql_ObjectList)

@given(instance=sparql_GraphClauseNE_strategy)
@settings(max_examples=50)
def test_sparql_graphclausene_instantiation(instance):
    assert isinstance(instance, sparql_GraphClauseNE)

@given(instance=sparql_Expression_strategy)
@settings(max_examples=50)
def test_sparql_expression_instantiation(instance):
    assert isinstance(instance, sparql_Expression)

@given(instance=sparql_SolutionModifier_strategy)
@settings(max_examples=50)
def test_sparql_solutionmodifier_instantiation(instance):
    assert isinstance(instance, sparql_SolutionModifier)

@given(instance=sparql_GraphNode_strategy)
@settings(max_examples=50)
def test_sparql_graphnode_instantiation(instance):
    assert isinstance(instance, sparql_GraphNode)

@given(instance=sparql_AdditionalGGPElement_strategy)
@settings(max_examples=50)
def test_sparql_additionalggpelement_instantiation(instance):
    assert isinstance(instance, sparql_AdditionalGGPElement)

@given(instance=sparql_RelationalExpression_strategy)
@settings(max_examples=50)
def test_sparql_relationalexpression_instantiation(instance):
    assert isinstance(instance, sparql_RelationalExpression)

@given(instance=sparql_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_sparql_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, sparql_ConditionalAndExpression)

@given(instance=sparql_ConstructTemplate_strategy)
@settings(max_examples=50)
def test_sparql_constructtemplate_instantiation(instance):
    assert isinstance(instance, sparql_ConstructTemplate)

@given(instance=sparql_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_sparql_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, sparql_MultiplicativeExpression)

@given(instance=sparql_SourceSelector_strategy)
@settings(max_examples=50)
def test_sparql_sourceselector_instantiation(instance):
    assert isinstance(instance, sparql_SourceSelector)

@given(instance=sparql_AdditionalValueLogicalNE_strategy)
@settings(max_examples=50)
def test_sparql_additionalvaluelogicalne_instantiation(instance):
    assert isinstance(instance, sparql_AdditionalValueLogicalNE)

@given(instance=sparql_GroupGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql_groupgraphpattern_instantiation(instance):
    assert isinstance(instance, sparql_GroupGraphPattern)

@given(instance=sparql_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_sparql_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, sparql_ConditionalOrExpression)

@given(instance=sparql_Verb_strategy)
@settings(max_examples=50)
def test_sparql_verb_instantiation(instance):
    assert isinstance(instance, sparql_Verb)

@given(instance=sparql_SparqlQueries_strategy)
@settings(max_examples=50)
def test_sparql_sparqlqueries_instantiation(instance):
    assert isinstance(instance, sparql_SparqlQueries)
