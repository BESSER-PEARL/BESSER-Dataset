import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    oogen::OOCommentOwner,
    oogen::OOComment,
    OOComparatorExpression,
    oogen::OOEqualsExpression,
    oogen::OOLanguageSpecificSnippet,
    OOOneOperandArithmeticExpression,
    oogen::OOPostfixDecrementExpression,
    oogen::OOPrefixIncrementExpression,
    oogen::OOPlusExpression,
    oogen::OOPrefixDecrementExpression,
    oogen::OOMinusExpression,
    oogen::OOBracketedExpression,
    oogen::OOPostfixIncrementExpression,
    oogen::OOBitWiseComplement,
    oogen::OOLessEqualsExpression,
    oogen::OOGreaterEqualsExpression,
    oogen::OONotEqualsExpression,
    oogen::OOLessThanExpression,
    oogen::OOGreaterThanExpression,
    OOCompoundStatement,
    oogen::OOCase,
    oogen::OODefault,
    OOConditionalStatement,
    oogen::OOFor,
    oogen::OOIf,
    OOLogicalExpression,
    oogen::OOOneOperandLogicalExpression,
    oogen::OOLogicalLiteral,
    oogen::OOComparatorExpression,
    oogen::OOTernaryOperator,
    oogen::OOTwoOperandLogicalExpression,
    OOOneOperandLogicalExpression,
    oogen::OONotExpression,
    OOTwoOperandLogicalExpression,
    oogen::OOXorExpression,
    oogen::OOOrExpression,
    oogen::OOAndExpression,
    OOTwoOperandArithmeticExpression,
    oogen::OOTwoOperandAssignableExpression,
    oogen::OORootExpression,
    oogen::OOPowerExpression,
    oogen::OODoWhile,
    oogen::OOWhile,
    OOArithmeticExpression,
    oogen::OOFloatLiteral,
    oogen::OOIntegerLiteral,
    oogen::OOLongLiteral,
    oogen::OOOneOperandArithmeticExpression,
    oogen::OODoubleLiteral,
    oogen::OOTwoOperandArithmeticExpression,
    OOExpression,
    oogen::OOStringLiteral,
    oogen::OOLogicalExpression,
    oogen::OOEmptyExpression,
    oogen::OOIndexing,
    oogen::OOTypeCast,
    oogen::OOVariableReferenceExpression,
    oogen::OOFieldReferenceExpression,
    oogen::OONewArray,
    oogen::OOThisLiteral,
    oogen::OOLanguageSpecificExpression,
    oogen::OOAssignmentExpression,
    oogen::OOFunctionCallExpression,
    oogen::OONullLiteral,
    oogen::OOInitializerList,
    oogen::OONewClass,
    oogen::OOBoolLiteral,
    oogen::OOArithmeticExpression,
    oogen::OOModel,
    OOTwoOperandAssignableExpression,
    oogen::OOBitwiseAndExpression,
    oogen::OOBitwiseXorExpression,
    oogen::OOBitwiseOrExpression,
    oogen::OOModuloExpression,
    oogen::OOSubtractionExpression,
    oogen::OOMultiplicationExpression,
    oogen::OOIntegerDivisionExpression,
    oogen::OOBitWiseLeftShift,
    oogen::OODivisionExpression,
    oogen::OOBitWiseRightShift,
    oogen::OOAdditionExpression,
    oogen::OOType,
    OOStatement,
    oogen::OOBreak,
    oogen::OOContinue,
    oogen::OOSwitch,
    oogen::OOForEach,
    oogen::OOCompoundStatement,
    oogen::OOConditionalStatement,
    oogen::OOReturn,
    oogen::OOEmptyStatement,
    oogen::OOVariableDeclarationList,
    oogen::OOExpression,
    oogen::OOVariable,
    oogen::OOConstructor,
    OOCommentOwner,
    oogen::OOMethod,
    oogen::OOStatement,
    OOVariable,
    oogen::OOMember,
    oogen::OOPackage,
    oogen::OOEnumeration,
    oogen::OOClass,
    OOLanguage,
    OOBaseType,
    OOCollectionType,
    OOVisibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oogen::oocommentowner_is_not_abstract():
    assert not inspect.isabstract(oogen::OOCommentOwner)


def test_oogen::oocommentowner_constructor_exists():
    assert callable(oogen::OOCommentOwner.__init__)


def test_oogen::oocommentowner_constructor_args():
    sig = inspect.signature(oogen::OOCommentOwner.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oocomment_is_not_abstract():
    assert not inspect.isabstract(oogen::OOComment)


def test_oogen::oocomment_constructor_exists():
    assert callable(oogen::OOComment.__init__)


def test_oogen::oocomment_constructor_args():
    sig = inspect.signature(oogen::OOComment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "isBlockComment" in params, "Missing parameter 'isBlockComment'"

def test_oogen::oocomment_has_text():
    assert hasattr(oogen::OOComment, "text")
    descriptor = None
    for klass in oogen::OOComment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_oogen::oocomment_has_isBlockComment():
    assert hasattr(oogen::OOComment, "isBlockComment")
    descriptor = None
    for klass in oogen::OOComment.__mro__:
        if "isBlockComment" in klass.__dict__:
            descriptor = klass.__dict__["isBlockComment"]
            break
    assert isinstance(descriptor, property)



def test_oocomparatorexpression_is_not_abstract():
    assert not inspect.isabstract(OOComparatorExpression)


def test_oocomparatorexpression_constructor_exists():
    assert callable(OOComparatorExpression.__init__)


def test_oocomparatorexpression_constructor_args():
    sig = inspect.signature(OOComparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOEqualsExpression)


def test_oogen::ooequalsexpression_constructor_exists():
    assert callable(oogen::OOEqualsExpression.__init__)


def test_oogen::ooequalsexpression_constructor_args():
    sig = inspect.signature(oogen::OOEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oolanguagespecificsnippet_is_not_abstract():
    assert not inspect.isabstract(oogen::OOLanguageSpecificSnippet)


def test_oogen::oolanguagespecificsnippet_constructor_exists():
    assert callable(oogen::OOLanguageSpecificSnippet.__init__)


def test_oogen::oolanguagespecificsnippet_constructor_args():
    sig = inspect.signature(oogen::OOLanguageSpecificSnippet.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "code" in params, "Missing parameter 'code'"

def test_oogen::oolanguagespecificsnippet_has_lang():
    assert hasattr(oogen::OOLanguageSpecificSnippet, "lang")
    descriptor = None
    for klass in oogen::OOLanguageSpecificSnippet.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)

def test_oogen::oolanguagespecificsnippet_has_code():
    assert hasattr(oogen::OOLanguageSpecificSnippet, "code")
    descriptor = None
    for klass in oogen::OOLanguageSpecificSnippet.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_oooneoperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(OOOneOperandArithmeticExpression)


def test_oooneoperandarithmeticexpression_constructor_exists():
    assert callable(OOOneOperandArithmeticExpression.__init__)


def test_oooneoperandarithmeticexpression_constructor_args():
    sig = inspect.signature(OOOneOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oopostfixdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOPostfixDecrementExpression)


def test_oogen::oopostfixdecrementexpression_constructor_exists():
    assert callable(oogen::OOPostfixDecrementExpression.__init__)


def test_oogen::oopostfixdecrementexpression_constructor_args():
    sig = inspect.signature(oogen::OOPostfixDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooprefixincrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOPrefixIncrementExpression)


def test_oogen::ooprefixincrementexpression_constructor_exists():
    assert callable(oogen::OOPrefixIncrementExpression.__init__)


def test_oogen::ooprefixincrementexpression_constructor_args():
    sig = inspect.signature(oogen::OOPrefixIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooplusexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOPlusExpression)


def test_oogen::ooplusexpression_constructor_exists():
    assert callable(oogen::OOPlusExpression.__init__)


def test_oogen::ooplusexpression_constructor_args():
    sig = inspect.signature(oogen::OOPlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooprefixdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOPrefixDecrementExpression)


def test_oogen::ooprefixdecrementexpression_constructor_exists():
    assert callable(oogen::OOPrefixDecrementExpression.__init__)


def test_oogen::ooprefixdecrementexpression_constructor_args():
    sig = inspect.signature(oogen::OOPrefixDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oominusexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOMinusExpression)


def test_oogen::oominusexpression_constructor_exists():
    assert callable(oogen::OOMinusExpression.__init__)


def test_oogen::oominusexpression_constructor_args():
    sig = inspect.signature(oogen::OOMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oobracketedexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOBracketedExpression)


def test_oogen::oobracketedexpression_constructor_exists():
    assert callable(oogen::OOBracketedExpression.__init__)


def test_oogen::oobracketedexpression_constructor_args():
    sig = inspect.signature(oogen::OOBracketedExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oopostfixincrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOPostfixIncrementExpression)


def test_oogen::oopostfixincrementexpression_constructor_exists():
    assert callable(oogen::OOPostfixIncrementExpression.__init__)


def test_oogen::oopostfixincrementexpression_constructor_args():
    sig = inspect.signature(oogen::OOPostfixIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oobitwisecomplement_is_not_abstract():
    assert not inspect.isabstract(oogen::OOBitWiseComplement)


def test_oogen::oobitwisecomplement_constructor_exists():
    assert callable(oogen::OOBitWiseComplement.__init__)


def test_oogen::oobitwisecomplement_constructor_args():
    sig = inspect.signature(oogen::OOBitWiseComplement.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oolessequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOLessEqualsExpression)


def test_oogen::oolessequalsexpression_constructor_exists():
    assert callable(oogen::OOLessEqualsExpression.__init__)


def test_oogen::oolessequalsexpression_constructor_args():
    sig = inspect.signature(oogen::OOLessEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oogreaterequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOGreaterEqualsExpression)


def test_oogen::oogreaterequalsexpression_constructor_exists():
    assert callable(oogen::OOGreaterEqualsExpression.__init__)


def test_oogen::oogreaterequalsexpression_constructor_args():
    sig = inspect.signature(oogen::OOGreaterEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oonotequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OONotEqualsExpression)


def test_oogen::oonotequalsexpression_constructor_exists():
    assert callable(oogen::OONotEqualsExpression.__init__)


def test_oogen::oonotequalsexpression_constructor_args():
    sig = inspect.signature(oogen::OONotEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oolessthanexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOLessThanExpression)


def test_oogen::oolessthanexpression_constructor_exists():
    assert callable(oogen::OOLessThanExpression.__init__)


def test_oogen::oolessthanexpression_constructor_args():
    sig = inspect.signature(oogen::OOLessThanExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oogreaterthanexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOGreaterThanExpression)


def test_oogen::oogreaterthanexpression_constructor_exists():
    assert callable(oogen::OOGreaterThanExpression.__init__)


def test_oogen::oogreaterthanexpression_constructor_args():
    sig = inspect.signature(oogen::OOGreaterThanExpression.__init__)
    params = list(sig.parameters.keys())



def test_oocompoundstatement_is_not_abstract():
    assert not inspect.isabstract(OOCompoundStatement)


def test_oocompoundstatement_constructor_exists():
    assert callable(OOCompoundStatement.__init__)


def test_oocompoundstatement_constructor_args():
    sig = inspect.signature(OOCompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oocase_is_not_abstract():
    assert not inspect.isabstract(oogen::OOCase)


def test_oogen::oocase_constructor_exists():
    assert callable(oogen::OOCase.__init__)


def test_oogen::oocase_constructor_args():
    sig = inspect.signature(oogen::OOCase.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oodefault_is_not_abstract():
    assert not inspect.isabstract(oogen::OODefault)


def test_oogen::oodefault_constructor_exists():
    assert callable(oogen::OODefault.__init__)


def test_oogen::oodefault_constructor_args():
    sig = inspect.signature(oogen::OODefault.__init__)
    params = list(sig.parameters.keys())



def test_ooconditionalstatement_is_not_abstract():
    assert not inspect.isabstract(OOConditionalStatement)


def test_ooconditionalstatement_constructor_exists():
    assert callable(OOConditionalStatement.__init__)


def test_ooconditionalstatement_constructor_args():
    sig = inspect.signature(OOConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oofor_is_not_abstract():
    assert not inspect.isabstract(oogen::OOFor)


def test_oogen::oofor_constructor_exists():
    assert callable(oogen::OOFor.__init__)


def test_oogen::oofor_constructor_args():
    sig = inspect.signature(oogen::OOFor.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooif_is_not_abstract():
    assert not inspect.isabstract(oogen::OOIf)


def test_oogen::ooif_constructor_exists():
    assert callable(oogen::OOIf.__init__)


def test_oogen::ooif_constructor_args():
    sig = inspect.signature(oogen::OOIf.__init__)
    params = list(sig.parameters.keys())



def test_oologicalexpression_is_not_abstract():
    assert not inspect.isabstract(OOLogicalExpression)


def test_oologicalexpression_constructor_exists():
    assert callable(OOLogicalExpression.__init__)


def test_oologicalexpression_constructor_args():
    sig = inspect.signature(OOLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oooneoperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOOneOperandLogicalExpression)


def test_oogen::oooneoperandlogicalexpression_constructor_exists():
    assert callable(oogen::OOOneOperandLogicalExpression.__init__)


def test_oogen::oooneoperandlogicalexpression_constructor_args():
    sig = inspect.signature(oogen::OOOneOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oologicalliteral_is_not_abstract():
    assert not inspect.isabstract(oogen::OOLogicalLiteral)


def test_oogen::oologicalliteral_constructor_exists():
    assert callable(oogen::OOLogicalLiteral.__init__)


def test_oogen::oologicalliteral_constructor_args():
    sig = inspect.signature(oogen::OOLogicalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen::oologicalliteral_has_value():
    assert hasattr(oogen::OOLogicalLiteral, "value")
    descriptor = None
    for klass in oogen::OOLogicalLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen::oocomparatorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOComparatorExpression)


def test_oogen::oocomparatorexpression_constructor_exists():
    assert callable(oogen::OOComparatorExpression.__init__)


def test_oogen::oocomparatorexpression_constructor_args():
    sig = inspect.signature(oogen::OOComparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooternaryoperator_is_not_abstract():
    assert not inspect.isabstract(oogen::OOTernaryOperator)


def test_oogen::ooternaryoperator_constructor_exists():
    assert callable(oogen::OOTernaryOperator.__init__)


def test_oogen::ooternaryoperator_constructor_args():
    sig = inspect.signature(oogen::OOTernaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ootwooperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOTwoOperandLogicalExpression)


def test_oogen::ootwooperandlogicalexpression_constructor_exists():
    assert callable(oogen::OOTwoOperandLogicalExpression.__init__)


def test_oogen::ootwooperandlogicalexpression_constructor_args():
    sig = inspect.signature(oogen::OOTwoOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oooneoperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(OOOneOperandLogicalExpression)


def test_oooneoperandlogicalexpression_constructor_exists():
    assert callable(OOOneOperandLogicalExpression.__init__)


def test_oooneoperandlogicalexpression_constructor_args():
    sig = inspect.signature(OOOneOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oonotexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OONotExpression)


def test_oogen::oonotexpression_constructor_exists():
    assert callable(oogen::OONotExpression.__init__)


def test_oogen::oonotexpression_constructor_args():
    sig = inspect.signature(oogen::OONotExpression.__init__)
    params = list(sig.parameters.keys())



def test_ootwooperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(OOTwoOperandLogicalExpression)


def test_ootwooperandlogicalexpression_constructor_exists():
    assert callable(OOTwoOperandLogicalExpression.__init__)


def test_ootwooperandlogicalexpression_constructor_args():
    sig = inspect.signature(OOTwoOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooxorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOXorExpression)


def test_oogen::ooxorexpression_constructor_exists():
    assert callable(oogen::OOXorExpression.__init__)


def test_oogen::ooxorexpression_constructor_args():
    sig = inspect.signature(oogen::OOXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOOrExpression)


def test_oogen::ooorexpression_constructor_exists():
    assert callable(oogen::OOOrExpression.__init__)


def test_oogen::ooorexpression_constructor_args():
    sig = inspect.signature(oogen::OOOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooandexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOAndExpression)


def test_oogen::ooandexpression_constructor_exists():
    assert callable(oogen::OOAndExpression.__init__)


def test_oogen::ooandexpression_constructor_args():
    sig = inspect.signature(oogen::OOAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ootwooperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(OOTwoOperandArithmeticExpression)


def test_ootwooperandarithmeticexpression_constructor_exists():
    assert callable(OOTwoOperandArithmeticExpression.__init__)


def test_ootwooperandarithmeticexpression_constructor_args():
    sig = inspect.signature(OOTwoOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ootwooperandassignableexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOTwoOperandAssignableExpression)


def test_oogen::ootwooperandassignableexpression_constructor_exists():
    assert callable(oogen::OOTwoOperandAssignableExpression.__init__)


def test_oogen::ootwooperandassignableexpression_constructor_args():
    sig = inspect.signature(oogen::OOTwoOperandAssignableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "assigned" in params, "Missing parameter 'assigned'"

def test_oogen::ootwooperandassignableexpression_has_assigned():
    assert hasattr(oogen::OOTwoOperandAssignableExpression, "assigned")
    descriptor = None
    for klass in oogen::OOTwoOperandAssignableExpression.__mro__:
        if "assigned" in klass.__dict__:
            descriptor = klass.__dict__["assigned"]
            break
    assert isinstance(descriptor, property)



def test_oogen::oorootexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OORootExpression)


def test_oogen::oorootexpression_constructor_exists():
    assert callable(oogen::OORootExpression.__init__)


def test_oogen::oorootexpression_constructor_args():
    sig = inspect.signature(oogen::OORootExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oopowerexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOPowerExpression)


def test_oogen::oopowerexpression_constructor_exists():
    assert callable(oogen::OOPowerExpression.__init__)


def test_oogen::oopowerexpression_constructor_args():
    sig = inspect.signature(oogen::OOPowerExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oodowhile_is_not_abstract():
    assert not inspect.isabstract(oogen::OODoWhile)


def test_oogen::oodowhile_constructor_exists():
    assert callable(oogen::OODoWhile.__init__)


def test_oogen::oodowhile_constructor_args():
    sig = inspect.signature(oogen::OODoWhile.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oowhile_is_not_abstract():
    assert not inspect.isabstract(oogen::OOWhile)


def test_oogen::oowhile_constructor_exists():
    assert callable(oogen::OOWhile.__init__)


def test_oogen::oowhile_constructor_args():
    sig = inspect.signature(oogen::OOWhile.__init__)
    params = list(sig.parameters.keys())



def test_ooarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(OOArithmeticExpression)


def test_ooarithmeticexpression_constructor_exists():
    assert callable(OOArithmeticExpression.__init__)


def test_ooarithmeticexpression_constructor_args():
    sig = inspect.signature(OOArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oofloatliteral_is_not_abstract():
    assert not inspect.isabstract(oogen::OOFloatLiteral)


def test_oogen::oofloatliteral_constructor_exists():
    assert callable(oogen::OOFloatLiteral.__init__)


def test_oogen::oofloatliteral_constructor_args():
    sig = inspect.signature(oogen::OOFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen::oofloatliteral_has_value():
    assert hasattr(oogen::OOFloatLiteral, "value")
    descriptor = None
    for klass in oogen::OOFloatLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen::oointegerliteral_is_not_abstract():
    assert not inspect.isabstract(oogen::OOIntegerLiteral)


def test_oogen::oointegerliteral_constructor_exists():
    assert callable(oogen::OOIntegerLiteral.__init__)


def test_oogen::oointegerliteral_constructor_args():
    sig = inspect.signature(oogen::OOIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen::oointegerliteral_has_value():
    assert hasattr(oogen::OOIntegerLiteral, "value")
    descriptor = None
    for klass in oogen::OOIntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen::oolongliteral_is_not_abstract():
    assert not inspect.isabstract(oogen::OOLongLiteral)


def test_oogen::oolongliteral_constructor_exists():
    assert callable(oogen::OOLongLiteral.__init__)


def test_oogen::oolongliteral_constructor_args():
    sig = inspect.signature(oogen::OOLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen::oolongliteral_has_value():
    assert hasattr(oogen::OOLongLiteral, "value")
    descriptor = None
    for klass in oogen::OOLongLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen::oooneoperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOOneOperandArithmeticExpression)


def test_oogen::oooneoperandarithmeticexpression_constructor_exists():
    assert callable(oogen::OOOneOperandArithmeticExpression.__init__)


def test_oogen::oooneoperandarithmeticexpression_constructor_args():
    sig = inspect.signature(oogen::OOOneOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oodoubleliteral_is_not_abstract():
    assert not inspect.isabstract(oogen::OODoubleLiteral)


def test_oogen::oodoubleliteral_constructor_exists():
    assert callable(oogen::OODoubleLiteral.__init__)


def test_oogen::oodoubleliteral_constructor_args():
    sig = inspect.signature(oogen::OODoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen::oodoubleliteral_has_value():
    assert hasattr(oogen::OODoubleLiteral, "value")
    descriptor = None
    for klass in oogen::OODoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen::ootwooperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOTwoOperandArithmeticExpression)


def test_oogen::ootwooperandarithmeticexpression_constructor_exists():
    assert callable(oogen::OOTwoOperandArithmeticExpression.__init__)


def test_oogen::ootwooperandarithmeticexpression_constructor_args():
    sig = inspect.signature(oogen::OOTwoOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ooexpression_is_not_abstract():
    assert not inspect.isabstract(OOExpression)


def test_ooexpression_constructor_exists():
    assert callable(OOExpression.__init__)


def test_ooexpression_constructor_args():
    sig = inspect.signature(OOExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oostringliteral_is_not_abstract():
    assert not inspect.isabstract(oogen::OOStringLiteral)


def test_oogen::oostringliteral_constructor_exists():
    assert callable(oogen::OOStringLiteral.__init__)


def test_oogen::oostringliteral_constructor_args():
    sig = inspect.signature(oogen::OOStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen::oostringliteral_has_value():
    assert hasattr(oogen::OOStringLiteral, "value")
    descriptor = None
    for klass in oogen::OOStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen::oologicalexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOLogicalExpression)


def test_oogen::oologicalexpression_constructor_exists():
    assert callable(oogen::OOLogicalExpression.__init__)


def test_oogen::oologicalexpression_constructor_args():
    sig = inspect.signature(oogen::OOLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooemptyexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOEmptyExpression)


def test_oogen::ooemptyexpression_constructor_exists():
    assert callable(oogen::OOEmptyExpression.__init__)


def test_oogen::ooemptyexpression_constructor_args():
    sig = inspect.signature(oogen::OOEmptyExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooindexing_is_not_abstract():
    assert not inspect.isabstract(oogen::OOIndexing)


def test_oogen::ooindexing_constructor_exists():
    assert callable(oogen::OOIndexing.__init__)


def test_oogen::ooindexing_constructor_args():
    sig = inspect.signature(oogen::OOIndexing.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ootypecast_is_not_abstract():
    assert not inspect.isabstract(oogen::OOTypeCast)


def test_oogen::ootypecast_constructor_exists():
    assert callable(oogen::OOTypeCast.__init__)


def test_oogen::ootypecast_constructor_args():
    sig = inspect.signature(oogen::OOTypeCast.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oovariablereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOVariableReferenceExpression)


def test_oogen::oovariablereferenceexpression_constructor_exists():
    assert callable(oogen::OOVariableReferenceExpression.__init__)


def test_oogen::oovariablereferenceexpression_constructor_args():
    sig = inspect.signature(oogen::OOVariableReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oofieldreferenceexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOFieldReferenceExpression)


def test_oogen::oofieldreferenceexpression_constructor_exists():
    assert callable(oogen::OOFieldReferenceExpression.__init__)


def test_oogen::oofieldreferenceexpression_constructor_args():
    sig = inspect.signature(oogen::OOFieldReferenceExpression.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_oogen::oofieldreferenceexpression_has_fieldName():
    assert hasattr(oogen::OOFieldReferenceExpression, "fieldName")
    descriptor = None
    for klass in oogen::OOFieldReferenceExpression.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_oogen::oonewarray_is_not_abstract():
    assert not inspect.isabstract(oogen::OONewArray)


def test_oogen::oonewarray_constructor_exists():
    assert callable(oogen::OONewArray.__init__)


def test_oogen::oonewarray_constructor_args():
    sig = inspect.signature(oogen::OONewArray.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oothisliteral_is_not_abstract():
    assert not inspect.isabstract(oogen::OOThisLiteral)


def test_oogen::oothisliteral_constructor_exists():
    assert callable(oogen::OOThisLiteral.__init__)


def test_oogen::oothisliteral_constructor_args():
    sig = inspect.signature(oogen::OOThisLiteral.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oolanguagespecificexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOLanguageSpecificExpression)


def test_oogen::oolanguagespecificexpression_constructor_exists():
    assert callable(oogen::OOLanguageSpecificExpression.__init__)


def test_oogen::oolanguagespecificexpression_constructor_args():
    sig = inspect.signature(oogen::OOLanguageSpecificExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOAssignmentExpression)


def test_oogen::ooassignmentexpression_constructor_exists():
    assert callable(oogen::OOAssignmentExpression.__init__)


def test_oogen::ooassignmentexpression_constructor_args():
    sig = inspect.signature(oogen::OOAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oofunctioncallexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOFunctionCallExpression)


def test_oogen::oofunctioncallexpression_constructor_exists():
    assert callable(oogen::OOFunctionCallExpression.__init__)


def test_oogen::oofunctioncallexpression_constructor_args():
    sig = inspect.signature(oogen::OOFunctionCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_oogen::oofunctioncallexpression_has_functionName():
    assert hasattr(oogen::OOFunctionCallExpression, "functionName")
    descriptor = None
    for klass in oogen::OOFunctionCallExpression.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_oogen::oonullliteral_is_not_abstract():
    assert not inspect.isabstract(oogen::OONullLiteral)


def test_oogen::oonullliteral_constructor_exists():
    assert callable(oogen::OONullLiteral.__init__)


def test_oogen::oonullliteral_constructor_args():
    sig = inspect.signature(oogen::OONullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooinitializerlist_is_not_abstract():
    assert not inspect.isabstract(oogen::OOInitializerList)


def test_oogen::ooinitializerlist_constructor_exists():
    assert callable(oogen::OOInitializerList.__init__)


def test_oogen::ooinitializerlist_constructor_args():
    sig = inspect.signature(oogen::OOInitializerList.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oonewclass_is_not_abstract():
    assert not inspect.isabstract(oogen::OONewClass)


def test_oogen::oonewclass_constructor_exists():
    assert callable(oogen::OONewClass.__init__)


def test_oogen::oonewclass_constructor_args():
    sig = inspect.signature(oogen::OONewClass.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_oogen::oonewclass_has_className():
    assert hasattr(oogen::OONewClass, "className")
    descriptor = None
    for klass in oogen::OONewClass.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_oogen::ooboolliteral_is_not_abstract():
    assert not inspect.isabstract(oogen::OOBoolLiteral)


def test_oogen::ooboolliteral_constructor_exists():
    assert callable(oogen::OOBoolLiteral.__init__)


def test_oogen::ooboolliteral_constructor_args():
    sig = inspect.signature(oogen::OOBoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen::ooboolliteral_has_value():
    assert hasattr(oogen::OOBoolLiteral, "value")
    descriptor = None
    for klass in oogen::OOBoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen::ooarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOArithmeticExpression)


def test_oogen::ooarithmeticexpression_constructor_exists():
    assert callable(oogen::OOArithmeticExpression.__init__)


def test_oogen::ooarithmeticexpression_constructor_args():
    sig = inspect.signature(oogen::OOArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oomodel_is_not_abstract():
    assert not inspect.isabstract(oogen::OOModel)


def test_oogen::oomodel_constructor_exists():
    assert callable(oogen::OOModel.__init__)


def test_oogen::oomodel_constructor_args():
    sig = inspect.signature(oogen::OOModel.__init__)
    params = list(sig.parameters.keys())



def test_ootwooperandassignableexpression_is_not_abstract():
    assert not inspect.isabstract(OOTwoOperandAssignableExpression)


def test_ootwooperandassignableexpression_constructor_exists():
    assert callable(OOTwoOperandAssignableExpression.__init__)


def test_ootwooperandassignableexpression_constructor_args():
    sig = inspect.signature(OOTwoOperandAssignableExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oobitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOBitwiseAndExpression)


def test_oogen::oobitwiseandexpression_constructor_exists():
    assert callable(oogen::OOBitwiseAndExpression.__init__)


def test_oogen::oobitwiseandexpression_constructor_args():
    sig = inspect.signature(oogen::OOBitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oobitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOBitwiseXorExpression)


def test_oogen::oobitwisexorexpression_constructor_exists():
    assert callable(oogen::OOBitwiseXorExpression.__init__)


def test_oogen::oobitwisexorexpression_constructor_args():
    sig = inspect.signature(oogen::OOBitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oobitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOBitwiseOrExpression)


def test_oogen::oobitwiseorexpression_constructor_exists():
    assert callable(oogen::OOBitwiseOrExpression.__init__)


def test_oogen::oobitwiseorexpression_constructor_args():
    sig = inspect.signature(oogen::OOBitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oomoduloexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOModuloExpression)


def test_oogen::oomoduloexpression_constructor_exists():
    assert callable(oogen::OOModuloExpression.__init__)


def test_oogen::oomoduloexpression_constructor_args():
    sig = inspect.signature(oogen::OOModuloExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oosubtractionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOSubtractionExpression)


def test_oogen::oosubtractionexpression_constructor_exists():
    assert callable(oogen::OOSubtractionExpression.__init__)


def test_oogen::oosubtractionexpression_constructor_args():
    sig = inspect.signature(oogen::OOSubtractionExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oomultiplicationexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOMultiplicationExpression)


def test_oogen::oomultiplicationexpression_constructor_exists():
    assert callable(oogen::OOMultiplicationExpression.__init__)


def test_oogen::oomultiplicationexpression_constructor_args():
    sig = inspect.signature(oogen::OOMultiplicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oointegerdivisionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOIntegerDivisionExpression)


def test_oogen::oointegerdivisionexpression_constructor_exists():
    assert callable(oogen::OOIntegerDivisionExpression.__init__)


def test_oogen::oointegerdivisionexpression_constructor_args():
    sig = inspect.signature(oogen::OOIntegerDivisionExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oobitwiseleftshift_is_not_abstract():
    assert not inspect.isabstract(oogen::OOBitWiseLeftShift)


def test_oogen::oobitwiseleftshift_constructor_exists():
    assert callable(oogen::OOBitWiseLeftShift.__init__)


def test_oogen::oobitwiseleftshift_constructor_args():
    sig = inspect.signature(oogen::OOBitWiseLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oodivisionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OODivisionExpression)


def test_oogen::oodivisionexpression_constructor_exists():
    assert callable(oogen::OODivisionExpression.__init__)


def test_oogen::oodivisionexpression_constructor_args():
    sig = inspect.signature(oogen::OODivisionExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oobitwiserightshift_is_not_abstract():
    assert not inspect.isabstract(oogen::OOBitWiseRightShift)


def test_oogen::oobitwiserightshift_constructor_exists():
    assert callable(oogen::OOBitWiseRightShift.__init__)


def test_oogen::oobitwiserightshift_constructor_args():
    sig = inspect.signature(oogen::OOBitWiseRightShift.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooadditionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOAdditionExpression)


def test_oogen::ooadditionexpression_constructor_exists():
    assert callable(oogen::OOAdditionExpression.__init__)


def test_oogen::ooadditionexpression_constructor_args():
    sig = inspect.signature(oogen::OOAdditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ootype_is_not_abstract():
    assert not inspect.isabstract(oogen::OOType)


def test_oogen::ootype_constructor_exists():
    assert callable(oogen::OOType.__init__)


def test_oogen::ootype_constructor_args():
    sig = inspect.signature(oogen::OOType.__init__)
    params = list(sig.parameters.keys())
    assert "collectionType" in params, "Missing parameter 'collectionType'"
    assert "arrayDimensions" in params, "Missing parameter 'arrayDimensions'"
    assert "numberOfIndirections" in params, "Missing parameter 'numberOfIndirections'"
    assert "baseType" in params, "Missing parameter 'baseType'"

def test_oogen::ootype_has_collectionType():
    assert hasattr(oogen::OOType, "collectionType")
    descriptor = None
    for klass in oogen::OOType.__mro__:
        if "collectionType" in klass.__dict__:
            descriptor = klass.__dict__["collectionType"]
            break
    assert isinstance(descriptor, property)

def test_oogen::ootype_has_arrayDimensions():
    assert hasattr(oogen::OOType, "arrayDimensions")
    descriptor = None
    for klass in oogen::OOType.__mro__:
        if "arrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["arrayDimensions"]
            break
    assert isinstance(descriptor, property)

def test_oogen::ootype_has_numberOfIndirections():
    assert hasattr(oogen::OOType, "numberOfIndirections")
    descriptor = None
    for klass in oogen::OOType.__mro__:
        if "numberOfIndirections" in klass.__dict__:
            descriptor = klass.__dict__["numberOfIndirections"]
            break
    assert isinstance(descriptor, property)

def test_oogen::ootype_has_baseType():
    assert hasattr(oogen::OOType, "baseType")
    descriptor = None
    for klass in oogen::OOType.__mro__:
        if "baseType" in klass.__dict__:
            descriptor = klass.__dict__["baseType"]
            break
    assert isinstance(descriptor, property)



def test_oostatement_is_not_abstract():
    assert not inspect.isabstract(OOStatement)


def test_oostatement_constructor_exists():
    assert callable(OOStatement.__init__)


def test_oostatement_constructor_args():
    sig = inspect.signature(OOStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oobreak_is_not_abstract():
    assert not inspect.isabstract(oogen::OOBreak)


def test_oogen::oobreak_constructor_exists():
    assert callable(oogen::OOBreak.__init__)


def test_oogen::oobreak_constructor_args():
    sig = inspect.signature(oogen::OOBreak.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oocontinue_is_not_abstract():
    assert not inspect.isabstract(oogen::OOContinue)


def test_oogen::oocontinue_constructor_exists():
    assert callable(oogen::OOContinue.__init__)


def test_oogen::oocontinue_constructor_args():
    sig = inspect.signature(oogen::OOContinue.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooswitch_is_not_abstract():
    assert not inspect.isabstract(oogen::OOSwitch)


def test_oogen::ooswitch_constructor_exists():
    assert callable(oogen::OOSwitch.__init__)


def test_oogen::ooswitch_constructor_args():
    sig = inspect.signature(oogen::OOSwitch.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooforeach_is_not_abstract():
    assert not inspect.isabstract(oogen::OOForEach)


def test_oogen::ooforeach_constructor_exists():
    assert callable(oogen::OOForEach.__init__)


def test_oogen::ooforeach_constructor_args():
    sig = inspect.signature(oogen::OOForEach.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oocompoundstatement_is_not_abstract():
    assert not inspect.isabstract(oogen::OOCompoundStatement)


def test_oogen::oocompoundstatement_constructor_exists():
    assert callable(oogen::OOCompoundStatement.__init__)


def test_oogen::oocompoundstatement_constructor_args():
    sig = inspect.signature(oogen::OOCompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooconditionalstatement_is_not_abstract():
    assert not inspect.isabstract(oogen::OOConditionalStatement)


def test_oogen::ooconditionalstatement_constructor_exists():
    assert callable(oogen::OOConditionalStatement.__init__)


def test_oogen::ooconditionalstatement_constructor_args():
    sig = inspect.signature(oogen::OOConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooreturn_is_not_abstract():
    assert not inspect.isabstract(oogen::OOReturn)


def test_oogen::ooreturn_constructor_exists():
    assert callable(oogen::OOReturn.__init__)


def test_oogen::ooreturn_constructor_args():
    sig = inspect.signature(oogen::OOReturn.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooemptystatement_is_not_abstract():
    assert not inspect.isabstract(oogen::OOEmptyStatement)


def test_oogen::ooemptystatement_constructor_exists():
    assert callable(oogen::OOEmptyStatement.__init__)


def test_oogen::ooemptystatement_constructor_args():
    sig = inspect.signature(oogen::OOEmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oovariabledeclarationlist_is_not_abstract():
    assert not inspect.isabstract(oogen::OOVariableDeclarationList)


def test_oogen::oovariabledeclarationlist_constructor_exists():
    assert callable(oogen::OOVariableDeclarationList.__init__)


def test_oogen::oovariabledeclarationlist_constructor_args():
    sig = inspect.signature(oogen::OOVariableDeclarationList.__init__)
    params = list(sig.parameters.keys())



def test_oogen::ooexpression_is_not_abstract():
    assert not inspect.isabstract(oogen::OOExpression)


def test_oogen::ooexpression_constructor_exists():
    assert callable(oogen::OOExpression.__init__)


def test_oogen::ooexpression_constructor_args():
    sig = inspect.signature(oogen::OOExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oovariable_is_not_abstract():
    assert not inspect.isabstract(oogen::OOVariable)


def test_oogen::oovariable_constructor_exists():
    assert callable(oogen::OOVariable.__init__)


def test_oogen::oovariable_constructor_args():
    sig = inspect.signature(oogen::OOVariable.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"
    assert "name" in params, "Missing parameter 'name'"

def test_oogen::oovariable_has_transient():
    assert hasattr(oogen::OOVariable, "transient")
    descriptor = None
    for klass in oogen::OOVariable.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_oogen::oovariable_has_name():
    assert hasattr(oogen::OOVariable, "name")
    descriptor = None
    for klass in oogen::OOVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oogen::ooconstructor_is_not_abstract():
    assert not inspect.isabstract(oogen::OOConstructor)


def test_oogen::ooconstructor_constructor_exists():
    assert callable(oogen::OOConstructor.__init__)


def test_oogen::ooconstructor_constructor_args():
    sig = inspect.signature(oogen::OOConstructor.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "className" in params, "Missing parameter 'className'"

def test_oogen::ooconstructor_has_visibility():
    assert hasattr(oogen::OOConstructor, "visibility")
    descriptor = None
    for klass in oogen::OOConstructor.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_oogen::ooconstructor_has_className():
    assert hasattr(oogen::OOConstructor, "className")
    descriptor = None
    for klass in oogen::OOConstructor.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_oocommentowner_is_not_abstract():
    assert not inspect.isabstract(OOCommentOwner)


def test_oocommentowner_constructor_exists():
    assert callable(OOCommentOwner.__init__)


def test_oocommentowner_constructor_args():
    sig = inspect.signature(OOCommentOwner.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oomethod_is_not_abstract():
    assert not inspect.isabstract(oogen::OOMethod)


def test_oogen::oomethod_constructor_exists():
    assert callable(oogen::OOMethod.__init__)


def test_oogen::oomethod_constructor_args():
    sig = inspect.signature(oogen::OOMethod.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "languages" in params, "Missing parameter 'languages'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_oogen::oomethod_has_static():
    assert hasattr(oogen::OOMethod, "static")
    descriptor = None
    for klass in oogen::OOMethod.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_oogen::oomethod_has_languages():
    assert hasattr(oogen::OOMethod, "languages")
    descriptor = None
    for klass in oogen::OOMethod.__mro__:
        if "languages" in klass.__dict__:
            descriptor = klass.__dict__["languages"]
            break
    assert isinstance(descriptor, property)

def test_oogen::oomethod_has_visibility():
    assert hasattr(oogen::OOMethod, "visibility")
    descriptor = None
    for klass in oogen::OOMethod.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_oogen::oomethod_has_name():
    assert hasattr(oogen::OOMethod, "name")
    descriptor = None
    for klass in oogen::OOMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oogen::oostatement_is_not_abstract():
    assert not inspect.isabstract(oogen::OOStatement)


def test_oogen::oostatement_constructor_exists():
    assert callable(oogen::OOStatement.__init__)


def test_oogen::oostatement_constructor_args():
    sig = inspect.signature(oogen::OOStatement.__init__)
    params = list(sig.parameters.keys())



def test_oovariable_is_not_abstract():
    assert not inspect.isabstract(OOVariable)


def test_oovariable_constructor_exists():
    assert callable(OOVariable.__init__)


def test_oovariable_constructor_args():
    sig = inspect.signature(OOVariable.__init__)
    params = list(sig.parameters.keys())



def test_oogen::oomember_is_not_abstract():
    assert not inspect.isabstract(oogen::OOMember)


def test_oogen::oomember_constructor_exists():
    assert callable(oogen::OOMember.__init__)


def test_oogen::oomember_constructor_args():
    sig = inspect.signature(oogen::OOMember.__init__)
    params = list(sig.parameters.keys())
    assert "languages" in params, "Missing parameter 'languages'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "static" in params, "Missing parameter 'static'"

def test_oogen::oomember_has_languages():
    assert hasattr(oogen::OOMember, "languages")
    descriptor = None
    for klass in oogen::OOMember.__mro__:
        if "languages" in klass.__dict__:
            descriptor = klass.__dict__["languages"]
            break
    assert isinstance(descriptor, property)

def test_oogen::oomember_has_visibility():
    assert hasattr(oogen::OOMember, "visibility")
    descriptor = None
    for klass in oogen::OOMember.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_oogen::oomember_has_static():
    assert hasattr(oogen::OOMember, "static")
    descriptor = None
    for klass in oogen::OOMember.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_oogen::oopackage_is_not_abstract():
    assert not inspect.isabstract(oogen::OOPackage)


def test_oogen::oopackage_constructor_exists():
    assert callable(oogen::OOPackage.__init__)


def test_oogen::oopackage_constructor_args():
    sig = inspect.signature(oogen::OOPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oogen::oopackage_has_name():
    assert hasattr(oogen::OOPackage, "name")
    descriptor = None
    for klass in oogen::OOPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oogen::ooenumeration_is_not_abstract():
    assert not inspect.isabstract(oogen::OOEnumeration)


def test_oogen::ooenumeration_constructor_exists():
    assert callable(oogen::OOEnumeration.__init__)


def test_oogen::ooenumeration_constructor_args():
    sig = inspect.signature(oogen::OOEnumeration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "options" in params, "Missing parameter 'options'"

def test_oogen::ooenumeration_has_name():
    assert hasattr(oogen::OOEnumeration, "name")
    descriptor = None
    for klass in oogen::OOEnumeration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oogen::ooenumeration_has_options():
    assert hasattr(oogen::OOEnumeration, "options")
    descriptor = None
    for klass in oogen::OOEnumeration.__mro__:
        if "options" in klass.__dict__:
            descriptor = klass.__dict__["options"]
            break
    assert isinstance(descriptor, property)



def test_oogen::ooclass_is_not_abstract():
    assert not inspect.isabstract(oogen::OOClass)


def test_oogen::ooclass_constructor_exists():
    assert callable(oogen::OOClass.__init__)


def test_oogen::ooclass_constructor_args():
    sig = inspect.signature(oogen::OOClass.__init__)
    params = list(sig.parameters.keys())
    assert "keep" in params, "Missing parameter 'keep'"
    assert "languages" in params, "Missing parameter 'languages'"
    assert "name" in params, "Missing parameter 'name'"

def test_oogen::ooclass_has_keep():
    assert hasattr(oogen::OOClass, "keep")
    descriptor = None
    for klass in oogen::OOClass.__mro__:
        if "keep" in klass.__dict__:
            descriptor = klass.__dict__["keep"]
            break
    assert isinstance(descriptor, property)

def test_oogen::ooclass_has_languages():
    assert hasattr(oogen::OOClass, "languages")
    descriptor = None
    for klass in oogen::OOClass.__mro__:
        if "languages" in klass.__dict__:
            descriptor = klass.__dict__["languages"]
            break
    assert isinstance(descriptor, property)

def test_oogen::ooclass_has_name():
    assert hasattr(oogen::OOClass, "name")
    descriptor = None
    for klass in oogen::OOClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oolanguage_exists():
    # Check that the Enumeration exists
    assert OOLanguage is not None

def test_oolanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OOLanguage]
    expected_literals = [
        "CPP",
        "JAVA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OOLanguage"

def test_oobasetype_exists():
    # Check that the Enumeration exists
    assert OOBaseType is not None

def test_oobasetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OOBaseType]
    expected_literals = [
        "DOUBLE",
        "OBJECT",
        "BYTE",
        "STRING",
        "INT",
        "LONG",
        "BOOLEAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OOBaseType"

def test_oocollectiontype_exists():
    # Check that the Enumeration exists
    assert OOCollectionType is not None

def test_oocollectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OOCollectionType]
    expected_literals = [
        "LIST",
        "NONE",
        "SET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OOCollectionType"

def test_oovisibility_exists():
    # Check that the Enumeration exists
    assert OOVisibility is not None

def test_oovisibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OOVisibility]
    expected_literals = [
        "PACKAGE",
        "PRIVATE",
        "PUBLIC",
        "PROTECTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OOVisibility"


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
oogen::OOCommentOwner_strategy = st.builds(
    oogen::OOCommentOwner,
)
oogen::OOComment_strategy = st.builds(
    oogen::OOComment,
    text=
        safe_text,
    isBlockComment=
        st.booleans()
)
OOComparatorExpression_strategy = st.builds(
    OOComparatorExpression,
)
oogen::OOEqualsExpression_strategy = st.builds(
    oogen::OOEqualsExpression,
)
oogen::OOLanguageSpecificSnippet_strategy = st.builds(
    oogen::OOLanguageSpecificSnippet,
    lang=
        safe_text,
    code=
        safe_text
)
OOOneOperandArithmeticExpression_strategy = st.builds(
    OOOneOperandArithmeticExpression,
)
oogen::OOPostfixDecrementExpression_strategy = st.builds(
    oogen::OOPostfixDecrementExpression,
)
oogen::OOPrefixIncrementExpression_strategy = st.builds(
    oogen::OOPrefixIncrementExpression,
)
oogen::OOPlusExpression_strategy = st.builds(
    oogen::OOPlusExpression,
)
oogen::OOPrefixDecrementExpression_strategy = st.builds(
    oogen::OOPrefixDecrementExpression,
)
oogen::OOMinusExpression_strategy = st.builds(
    oogen::OOMinusExpression,
)
oogen::OOBracketedExpression_strategy = st.builds(
    oogen::OOBracketedExpression,
)
oogen::OOPostfixIncrementExpression_strategy = st.builds(
    oogen::OOPostfixIncrementExpression,
)
oogen::OOBitWiseComplement_strategy = st.builds(
    oogen::OOBitWiseComplement,
)
oogen::OOLessEqualsExpression_strategy = st.builds(
    oogen::OOLessEqualsExpression,
)
oogen::OOGreaterEqualsExpression_strategy = st.builds(
    oogen::OOGreaterEqualsExpression,
)
oogen::OONotEqualsExpression_strategy = st.builds(
    oogen::OONotEqualsExpression,
)
oogen::OOLessThanExpression_strategy = st.builds(
    oogen::OOLessThanExpression,
)
oogen::OOGreaterThanExpression_strategy = st.builds(
    oogen::OOGreaterThanExpression,
)
OOCompoundStatement_strategy = st.builds(
    OOCompoundStatement,
)
oogen::OOCase_strategy = st.builds(
    oogen::OOCase,
)
oogen::OODefault_strategy = st.builds(
    oogen::OODefault,
)
OOConditionalStatement_strategy = st.builds(
    OOConditionalStatement,
)
oogen::OOFor_strategy = st.builds(
    oogen::OOFor,
)
oogen::OOIf_strategy = st.builds(
    oogen::OOIf,
)
OOLogicalExpression_strategy = st.builds(
    OOLogicalExpression,
)
oogen::OOOneOperandLogicalExpression_strategy = st.builds(
    oogen::OOOneOperandLogicalExpression,
)
oogen::OOLogicalLiteral_strategy = st.builds(
    oogen::OOLogicalLiteral,
    value=
        st.booleans()
)
oogen::OOComparatorExpression_strategy = st.builds(
    oogen::OOComparatorExpression,
)
oogen::OOTernaryOperator_strategy = st.builds(
    oogen::OOTernaryOperator,
)
oogen::OOTwoOperandLogicalExpression_strategy = st.builds(
    oogen::OOTwoOperandLogicalExpression,
)
OOOneOperandLogicalExpression_strategy = st.builds(
    OOOneOperandLogicalExpression,
)
oogen::OONotExpression_strategy = st.builds(
    oogen::OONotExpression,
)
OOTwoOperandLogicalExpression_strategy = st.builds(
    OOTwoOperandLogicalExpression,
)
oogen::OOXorExpression_strategy = st.builds(
    oogen::OOXorExpression,
)
oogen::OOOrExpression_strategy = st.builds(
    oogen::OOOrExpression,
)
oogen::OOAndExpression_strategy = st.builds(
    oogen::OOAndExpression,
)
OOTwoOperandArithmeticExpression_strategy = st.builds(
    OOTwoOperandArithmeticExpression,
)
oogen::OOTwoOperandAssignableExpression_strategy = st.builds(
    oogen::OOTwoOperandAssignableExpression,
    assigned=
        st.booleans()
)
oogen::OORootExpression_strategy = st.builds(
    oogen::OORootExpression,
)
oogen::OOPowerExpression_strategy = st.builds(
    oogen::OOPowerExpression,
)
oogen::OODoWhile_strategy = st.builds(
    oogen::OODoWhile,
)
oogen::OOWhile_strategy = st.builds(
    oogen::OOWhile,
)
OOArithmeticExpression_strategy = st.builds(
    OOArithmeticExpression,
)
oogen::OOFloatLiteral_strategy = st.builds(
    oogen::OOFloatLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oogen::OOIntegerLiteral_strategy = st.builds(
    oogen::OOIntegerLiteral,
    value=
        st.integers()
)
oogen::OOLongLiteral_strategy = st.builds(
    oogen::OOLongLiteral,
    value=
        safe_text
)
oogen::OOOneOperandArithmeticExpression_strategy = st.builds(
    oogen::OOOneOperandArithmeticExpression,
)
oogen::OODoubleLiteral_strategy = st.builds(
    oogen::OODoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oogen::OOTwoOperandArithmeticExpression_strategy = st.builds(
    oogen::OOTwoOperandArithmeticExpression,
)
OOExpression_strategy = st.builds(
    OOExpression,
)
oogen::OOStringLiteral_strategy = st.builds(
    oogen::OOStringLiteral,
    value=
        safe_text
)
oogen::OOLogicalExpression_strategy = st.builds(
    oogen::OOLogicalExpression,
)
oogen::OOEmptyExpression_strategy = st.builds(
    oogen::OOEmptyExpression,
)
oogen::OOIndexing_strategy = st.builds(
    oogen::OOIndexing,
)
oogen::OOTypeCast_strategy = st.builds(
    oogen::OOTypeCast,
)
oogen::OOVariableReferenceExpression_strategy = st.builds(
    oogen::OOVariableReferenceExpression,
)
oogen::OOFieldReferenceExpression_strategy = st.builds(
    oogen::OOFieldReferenceExpression,
    fieldName=
        safe_text
)
oogen::OONewArray_strategy = st.builds(
    oogen::OONewArray,
)
oogen::OOThisLiteral_strategy = st.builds(
    oogen::OOThisLiteral,
)
oogen::OOLanguageSpecificExpression_strategy = st.builds(
    oogen::OOLanguageSpecificExpression,
)
oogen::OOAssignmentExpression_strategy = st.builds(
    oogen::OOAssignmentExpression,
)
oogen::OOFunctionCallExpression_strategy = st.builds(
    oogen::OOFunctionCallExpression,
    functionName=
        safe_text
)
oogen::OONullLiteral_strategy = st.builds(
    oogen::OONullLiteral,
)
oogen::OOInitializerList_strategy = st.builds(
    oogen::OOInitializerList,
)
oogen::OONewClass_strategy = st.builds(
    oogen::OONewClass,
    className=
        safe_text
)
oogen::OOBoolLiteral_strategy = st.builds(
    oogen::OOBoolLiteral,
    value=
        st.booleans()
)
oogen::OOArithmeticExpression_strategy = st.builds(
    oogen::OOArithmeticExpression,
)
oogen::OOModel_strategy = st.builds(
    oogen::OOModel,
)
OOTwoOperandAssignableExpression_strategy = st.builds(
    OOTwoOperandAssignableExpression,
)
oogen::OOBitwiseAndExpression_strategy = st.builds(
    oogen::OOBitwiseAndExpression,
)
oogen::OOBitwiseXorExpression_strategy = st.builds(
    oogen::OOBitwiseXorExpression,
)
oogen::OOBitwiseOrExpression_strategy = st.builds(
    oogen::OOBitwiseOrExpression,
)
oogen::OOModuloExpression_strategy = st.builds(
    oogen::OOModuloExpression,
)
oogen::OOSubtractionExpression_strategy = st.builds(
    oogen::OOSubtractionExpression,
)
oogen::OOMultiplicationExpression_strategy = st.builds(
    oogen::OOMultiplicationExpression,
)
oogen::OOIntegerDivisionExpression_strategy = st.builds(
    oogen::OOIntegerDivisionExpression,
)
oogen::OOBitWiseLeftShift_strategy = st.builds(
    oogen::OOBitWiseLeftShift,
)
oogen::OODivisionExpression_strategy = st.builds(
    oogen::OODivisionExpression,
)
oogen::OOBitWiseRightShift_strategy = st.builds(
    oogen::OOBitWiseRightShift,
)
oogen::OOAdditionExpression_strategy = st.builds(
    oogen::OOAdditionExpression,
)
oogen::OOType_strategy = st.builds(
    oogen::OOType,
    collectionType=
        safe_text,
    arrayDimensions=
        st.integers(),
    numberOfIndirections=
        st.integers(),
    baseType=
        safe_text
)
OOStatement_strategy = st.builds(
    OOStatement,
)
oogen::OOBreak_strategy = st.builds(
    oogen::OOBreak,
)
oogen::OOContinue_strategy = st.builds(
    oogen::OOContinue,
)
oogen::OOSwitch_strategy = st.builds(
    oogen::OOSwitch,
)
oogen::OOForEach_strategy = st.builds(
    oogen::OOForEach,
)
oogen::OOCompoundStatement_strategy = st.builds(
    oogen::OOCompoundStatement,
)
oogen::OOConditionalStatement_strategy = st.builds(
    oogen::OOConditionalStatement,
)
oogen::OOReturn_strategy = st.builds(
    oogen::OOReturn,
)
oogen::OOEmptyStatement_strategy = st.builds(
    oogen::OOEmptyStatement,
)
oogen::OOVariableDeclarationList_strategy = st.builds(
    oogen::OOVariableDeclarationList,
)
oogen::OOExpression_strategy = st.builds(
    oogen::OOExpression,
)
oogen::OOVariable_strategy = st.builds(
    oogen::OOVariable,
    transient=
        st.booleans(),
    name=
        safe_text
)
oogen::OOConstructor_strategy = st.builds(
    oogen::OOConstructor,
    visibility=
        safe_text,
    className=
        safe_text
)
OOCommentOwner_strategy = st.builds(
    OOCommentOwner,
)
oogen::OOMethod_strategy = st.builds(
    oogen::OOMethod,
    static=
        st.booleans(),
    languages=
        safe_text,
    visibility=
        safe_text,
    name=
        safe_text
)
oogen::OOStatement_strategy = st.builds(
    oogen::OOStatement,
)
OOVariable_strategy = st.builds(
    OOVariable,
)
oogen::OOMember_strategy = st.builds(
    oogen::OOMember,
    languages=
        safe_text,
    visibility=
        safe_text,
    static=
        st.booleans()
)
oogen::OOPackage_strategy = st.builds(
    oogen::OOPackage,
    name=
        safe_text
)
oogen::OOEnumeration_strategy = st.builds(
    oogen::OOEnumeration,
    name=
        safe_text,
    options=
        safe_text
)
oogen::OOClass_strategy = st.builds(
    oogen::OOClass,
    keep=
        st.booleans(),
    languages=
        safe_text,
    name=
        safe_text
)

@given(instance=oogen::OOCommentOwner_strategy)
@settings(max_examples=50)
def test_oogen::oocommentowner_instantiation(instance):
    assert isinstance(instance, oogen::OOCommentOwner)

@given(instance=oogen::OOComment_strategy)
@settings(max_examples=50)
def test_oogen::oocomment_instantiation(instance):
    assert isinstance(instance, oogen::OOComment)

@given(instance=oogen::OOComment_strategy)
def test_oogen::oocomment_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=oogen::OOComment_strategy)
def test_oogen::oocomment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=oogen::OOComment_strategy)
def test_oogen::oocomment_isBlockComment_type(instance):
    assert isinstance(instance.isBlockComment, bool)


@given(instance=oogen::OOComment_strategy)
def test_oogen::oocomment_isBlockComment_setter(instance):
    original = instance.isBlockComment
    instance.isBlockComment = original
    assert instance.isBlockComment == original

@given(instance=OOComparatorExpression_strategy)
@settings(max_examples=50)
def test_oocomparatorexpression_instantiation(instance):
    assert isinstance(instance, OOComparatorExpression)

@given(instance=oogen::OOEqualsExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooequalsexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOEqualsExpression)

@given(instance=oogen::OOLanguageSpecificSnippet_strategy)
@settings(max_examples=50)
def test_oogen::oolanguagespecificsnippet_instantiation(instance):
    assert isinstance(instance, oogen::OOLanguageSpecificSnippet)

@given(instance=oogen::OOLanguageSpecificSnippet_strategy)
def test_oogen::oolanguagespecificsnippet_lang_type(instance):
    assert isinstance(instance.lang, str)


@given(instance=oogen::OOLanguageSpecificSnippet_strategy)
def test_oogen::oolanguagespecificsnippet_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=oogen::OOLanguageSpecificSnippet_strategy)
def test_oogen::oolanguagespecificsnippet_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=oogen::OOLanguageSpecificSnippet_strategy)
def test_oogen::oolanguagespecificsnippet_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=OOOneOperandArithmeticExpression_strategy)
@settings(max_examples=50)
def test_oooneoperandarithmeticexpression_instantiation(instance):
    assert isinstance(instance, OOOneOperandArithmeticExpression)

@given(instance=oogen::OOPostfixDecrementExpression_strategy)
@settings(max_examples=50)
def test_oogen::oopostfixdecrementexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOPostfixDecrementExpression)

@given(instance=oogen::OOPrefixIncrementExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooprefixincrementexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOPrefixIncrementExpression)

@given(instance=oogen::OOPlusExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooplusexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOPlusExpression)

@given(instance=oogen::OOPrefixDecrementExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooprefixdecrementexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOPrefixDecrementExpression)

@given(instance=oogen::OOMinusExpression_strategy)
@settings(max_examples=50)
def test_oogen::oominusexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOMinusExpression)

@given(instance=oogen::OOBracketedExpression_strategy)
@settings(max_examples=50)
def test_oogen::oobracketedexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOBracketedExpression)

@given(instance=oogen::OOPostfixIncrementExpression_strategy)
@settings(max_examples=50)
def test_oogen::oopostfixincrementexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOPostfixIncrementExpression)

@given(instance=oogen::OOBitWiseComplement_strategy)
@settings(max_examples=50)
def test_oogen::oobitwisecomplement_instantiation(instance):
    assert isinstance(instance, oogen::OOBitWiseComplement)

@given(instance=oogen::OOLessEqualsExpression_strategy)
@settings(max_examples=50)
def test_oogen::oolessequalsexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOLessEqualsExpression)

@given(instance=oogen::OOGreaterEqualsExpression_strategy)
@settings(max_examples=50)
def test_oogen::oogreaterequalsexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOGreaterEqualsExpression)

@given(instance=oogen::OONotEqualsExpression_strategy)
@settings(max_examples=50)
def test_oogen::oonotequalsexpression_instantiation(instance):
    assert isinstance(instance, oogen::OONotEqualsExpression)

@given(instance=oogen::OOLessThanExpression_strategy)
@settings(max_examples=50)
def test_oogen::oolessthanexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOLessThanExpression)

@given(instance=oogen::OOGreaterThanExpression_strategy)
@settings(max_examples=50)
def test_oogen::oogreaterthanexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOGreaterThanExpression)

@given(instance=OOCompoundStatement_strategy)
@settings(max_examples=50)
def test_oocompoundstatement_instantiation(instance):
    assert isinstance(instance, OOCompoundStatement)

@given(instance=oogen::OOCase_strategy)
@settings(max_examples=50)
def test_oogen::oocase_instantiation(instance):
    assert isinstance(instance, oogen::OOCase)

@given(instance=oogen::OODefault_strategy)
@settings(max_examples=50)
def test_oogen::oodefault_instantiation(instance):
    assert isinstance(instance, oogen::OODefault)

@given(instance=OOConditionalStatement_strategy)
@settings(max_examples=50)
def test_ooconditionalstatement_instantiation(instance):
    assert isinstance(instance, OOConditionalStatement)

@given(instance=oogen::OOFor_strategy)
@settings(max_examples=50)
def test_oogen::oofor_instantiation(instance):
    assert isinstance(instance, oogen::OOFor)

@given(instance=oogen::OOIf_strategy)
@settings(max_examples=50)
def test_oogen::ooif_instantiation(instance):
    assert isinstance(instance, oogen::OOIf)

@given(instance=OOLogicalExpression_strategy)
@settings(max_examples=50)
def test_oologicalexpression_instantiation(instance):
    assert isinstance(instance, OOLogicalExpression)

@given(instance=oogen::OOOneOperandLogicalExpression_strategy)
@settings(max_examples=50)
def test_oogen::oooneoperandlogicalexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOOneOperandLogicalExpression)

@given(instance=oogen::OOLogicalLiteral_strategy)
@settings(max_examples=50)
def test_oogen::oologicalliteral_instantiation(instance):
    assert isinstance(instance, oogen::OOLogicalLiteral)

@given(instance=oogen::OOLogicalLiteral_strategy)
def test_oogen::oologicalliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=oogen::OOLogicalLiteral_strategy)
def test_oogen::oologicalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen::OOComparatorExpression_strategy)
@settings(max_examples=50)
def test_oogen::oocomparatorexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOComparatorExpression)

@given(instance=oogen::OOTernaryOperator_strategy)
@settings(max_examples=50)
def test_oogen::ooternaryoperator_instantiation(instance):
    assert isinstance(instance, oogen::OOTernaryOperator)

@given(instance=oogen::OOTwoOperandLogicalExpression_strategy)
@settings(max_examples=50)
def test_oogen::ootwooperandlogicalexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOTwoOperandLogicalExpression)

@given(instance=OOOneOperandLogicalExpression_strategy)
@settings(max_examples=50)
def test_oooneoperandlogicalexpression_instantiation(instance):
    assert isinstance(instance, OOOneOperandLogicalExpression)

@given(instance=oogen::OONotExpression_strategy)
@settings(max_examples=50)
def test_oogen::oonotexpression_instantiation(instance):
    assert isinstance(instance, oogen::OONotExpression)

@given(instance=OOTwoOperandLogicalExpression_strategy)
@settings(max_examples=50)
def test_ootwooperandlogicalexpression_instantiation(instance):
    assert isinstance(instance, OOTwoOperandLogicalExpression)

@given(instance=oogen::OOXorExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooxorexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOXorExpression)

@given(instance=oogen::OOOrExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooorexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOOrExpression)

@given(instance=oogen::OOAndExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooandexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOAndExpression)

@given(instance=OOTwoOperandArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ootwooperandarithmeticexpression_instantiation(instance):
    assert isinstance(instance, OOTwoOperandArithmeticExpression)

@given(instance=oogen::OOTwoOperandAssignableExpression_strategy)
@settings(max_examples=50)
def test_oogen::ootwooperandassignableexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOTwoOperandAssignableExpression)

@given(instance=oogen::OOTwoOperandAssignableExpression_strategy)
def test_oogen::ootwooperandassignableexpression_assigned_type(instance):
    assert isinstance(instance.assigned, bool)


@given(instance=oogen::OOTwoOperandAssignableExpression_strategy)
def test_oogen::ootwooperandassignableexpression_assigned_setter(instance):
    original = instance.assigned
    instance.assigned = original
    assert instance.assigned == original

@given(instance=oogen::OORootExpression_strategy)
@settings(max_examples=50)
def test_oogen::oorootexpression_instantiation(instance):
    assert isinstance(instance, oogen::OORootExpression)

@given(instance=oogen::OOPowerExpression_strategy)
@settings(max_examples=50)
def test_oogen::oopowerexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOPowerExpression)

@given(instance=oogen::OODoWhile_strategy)
@settings(max_examples=50)
def test_oogen::oodowhile_instantiation(instance):
    assert isinstance(instance, oogen::OODoWhile)

@given(instance=oogen::OOWhile_strategy)
@settings(max_examples=50)
def test_oogen::oowhile_instantiation(instance):
    assert isinstance(instance, oogen::OOWhile)

@given(instance=OOArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ooarithmeticexpression_instantiation(instance):
    assert isinstance(instance, OOArithmeticExpression)

@given(instance=oogen::OOFloatLiteral_strategy)
@settings(max_examples=50)
def test_oogen::oofloatliteral_instantiation(instance):
    assert isinstance(instance, oogen::OOFloatLiteral)

@given(instance=oogen::OOFloatLiteral_strategy)
def test_oogen::oofloatliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=oogen::OOFloatLiteral_strategy)
def test_oogen::oofloatliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen::OOIntegerLiteral_strategy)
@settings(max_examples=50)
def test_oogen::oointegerliteral_instantiation(instance):
    assert isinstance(instance, oogen::OOIntegerLiteral)

@given(instance=oogen::OOIntegerLiteral_strategy)
def test_oogen::oointegerliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=oogen::OOIntegerLiteral_strategy)
def test_oogen::oointegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen::OOLongLiteral_strategy)
@settings(max_examples=50)
def test_oogen::oolongliteral_instantiation(instance):
    assert isinstance(instance, oogen::OOLongLiteral)

@given(instance=oogen::OOLongLiteral_strategy)
def test_oogen::oolongliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=oogen::OOLongLiteral_strategy)
def test_oogen::oolongliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen::OOOneOperandArithmeticExpression_strategy)
@settings(max_examples=50)
def test_oogen::oooneoperandarithmeticexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOOneOperandArithmeticExpression)

@given(instance=oogen::OODoubleLiteral_strategy)
@settings(max_examples=50)
def test_oogen::oodoubleliteral_instantiation(instance):
    assert isinstance(instance, oogen::OODoubleLiteral)

@given(instance=oogen::OODoubleLiteral_strategy)
def test_oogen::oodoubleliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=oogen::OODoubleLiteral_strategy)
def test_oogen::oodoubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen::OOTwoOperandArithmeticExpression_strategy)
@settings(max_examples=50)
def test_oogen::ootwooperandarithmeticexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOTwoOperandArithmeticExpression)

@given(instance=OOExpression_strategy)
@settings(max_examples=50)
def test_ooexpression_instantiation(instance):
    assert isinstance(instance, OOExpression)

@given(instance=oogen::OOStringLiteral_strategy)
@settings(max_examples=50)
def test_oogen::oostringliteral_instantiation(instance):
    assert isinstance(instance, oogen::OOStringLiteral)

@given(instance=oogen::OOStringLiteral_strategy)
def test_oogen::oostringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=oogen::OOStringLiteral_strategy)
def test_oogen::oostringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen::OOLogicalExpression_strategy)
@settings(max_examples=50)
def test_oogen::oologicalexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOLogicalExpression)

@given(instance=oogen::OOEmptyExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooemptyexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOEmptyExpression)

@given(instance=oogen::OOIndexing_strategy)
@settings(max_examples=50)
def test_oogen::ooindexing_instantiation(instance):
    assert isinstance(instance, oogen::OOIndexing)

@given(instance=oogen::OOTypeCast_strategy)
@settings(max_examples=50)
def test_oogen::ootypecast_instantiation(instance):
    assert isinstance(instance, oogen::OOTypeCast)

@given(instance=oogen::OOVariableReferenceExpression_strategy)
@settings(max_examples=50)
def test_oogen::oovariablereferenceexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOVariableReferenceExpression)

@given(instance=oogen::OOFieldReferenceExpression_strategy)
@settings(max_examples=50)
def test_oogen::oofieldreferenceexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOFieldReferenceExpression)

@given(instance=oogen::OOFieldReferenceExpression_strategy)
def test_oogen::oofieldreferenceexpression_fieldName_type(instance):
    assert isinstance(instance.fieldName, str)


@given(instance=oogen::OOFieldReferenceExpression_strategy)
def test_oogen::oofieldreferenceexpression_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=oogen::OONewArray_strategy)
@settings(max_examples=50)
def test_oogen::oonewarray_instantiation(instance):
    assert isinstance(instance, oogen::OONewArray)

@given(instance=oogen::OOThisLiteral_strategy)
@settings(max_examples=50)
def test_oogen::oothisliteral_instantiation(instance):
    assert isinstance(instance, oogen::OOThisLiteral)

@given(instance=oogen::OOLanguageSpecificExpression_strategy)
@settings(max_examples=50)
def test_oogen::oolanguagespecificexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOLanguageSpecificExpression)

@given(instance=oogen::OOAssignmentExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooassignmentexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOAssignmentExpression)

@given(instance=oogen::OOFunctionCallExpression_strategy)
@settings(max_examples=50)
def test_oogen::oofunctioncallexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOFunctionCallExpression)

@given(instance=oogen::OOFunctionCallExpression_strategy)
def test_oogen::oofunctioncallexpression_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=oogen::OOFunctionCallExpression_strategy)
def test_oogen::oofunctioncallexpression_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=oogen::OONullLiteral_strategy)
@settings(max_examples=50)
def test_oogen::oonullliteral_instantiation(instance):
    assert isinstance(instance, oogen::OONullLiteral)

@given(instance=oogen::OOInitializerList_strategy)
@settings(max_examples=50)
def test_oogen::ooinitializerlist_instantiation(instance):
    assert isinstance(instance, oogen::OOInitializerList)

@given(instance=oogen::OONewClass_strategy)
@settings(max_examples=50)
def test_oogen::oonewclass_instantiation(instance):
    assert isinstance(instance, oogen::OONewClass)

@given(instance=oogen::OONewClass_strategy)
def test_oogen::oonewclass_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=oogen::OONewClass_strategy)
def test_oogen::oonewclass_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=oogen::OOBoolLiteral_strategy)
@settings(max_examples=50)
def test_oogen::ooboolliteral_instantiation(instance):
    assert isinstance(instance, oogen::OOBoolLiteral)

@given(instance=oogen::OOBoolLiteral_strategy)
def test_oogen::ooboolliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=oogen::OOBoolLiteral_strategy)
def test_oogen::ooboolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen::OOArithmeticExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooarithmeticexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOArithmeticExpression)

@given(instance=oogen::OOModel_strategy)
@settings(max_examples=50)
def test_oogen::oomodel_instantiation(instance):
    assert isinstance(instance, oogen::OOModel)

@given(instance=OOTwoOperandAssignableExpression_strategy)
@settings(max_examples=50)
def test_ootwooperandassignableexpression_instantiation(instance):
    assert isinstance(instance, OOTwoOperandAssignableExpression)

@given(instance=oogen::OOBitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_oogen::oobitwiseandexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOBitwiseAndExpression)

@given(instance=oogen::OOBitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_oogen::oobitwisexorexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOBitwiseXorExpression)

@given(instance=oogen::OOBitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_oogen::oobitwiseorexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOBitwiseOrExpression)

@given(instance=oogen::OOModuloExpression_strategy)
@settings(max_examples=50)
def test_oogen::oomoduloexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOModuloExpression)

@given(instance=oogen::OOSubtractionExpression_strategy)
@settings(max_examples=50)
def test_oogen::oosubtractionexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOSubtractionExpression)

@given(instance=oogen::OOMultiplicationExpression_strategy)
@settings(max_examples=50)
def test_oogen::oomultiplicationexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOMultiplicationExpression)

@given(instance=oogen::OOIntegerDivisionExpression_strategy)
@settings(max_examples=50)
def test_oogen::oointegerdivisionexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOIntegerDivisionExpression)

@given(instance=oogen::OOBitWiseLeftShift_strategy)
@settings(max_examples=50)
def test_oogen::oobitwiseleftshift_instantiation(instance):
    assert isinstance(instance, oogen::OOBitWiseLeftShift)

@given(instance=oogen::OODivisionExpression_strategy)
@settings(max_examples=50)
def test_oogen::oodivisionexpression_instantiation(instance):
    assert isinstance(instance, oogen::OODivisionExpression)

@given(instance=oogen::OOBitWiseRightShift_strategy)
@settings(max_examples=50)
def test_oogen::oobitwiserightshift_instantiation(instance):
    assert isinstance(instance, oogen::OOBitWiseRightShift)

@given(instance=oogen::OOAdditionExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooadditionexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOAdditionExpression)

@given(instance=oogen::OOType_strategy)
@settings(max_examples=50)
def test_oogen::ootype_instantiation(instance):
    assert isinstance(instance, oogen::OOType)

@given(instance=oogen::OOType_strategy)
def test_oogen::ootype_collectionType_type(instance):
    assert isinstance(instance.collectionType, str)


@given(instance=oogen::OOType_strategy)
def test_oogen::ootype_collectionType_setter(instance):
    original = instance.collectionType
    instance.collectionType = original
    assert instance.collectionType == original

@given(instance=oogen::OOType_strategy)
def test_oogen::ootype_arrayDimensions_type(instance):
    assert isinstance(instance.arrayDimensions, int)


@given(instance=oogen::OOType_strategy)
def test_oogen::ootype_arrayDimensions_setter(instance):
    original = instance.arrayDimensions
    instance.arrayDimensions = original
    assert instance.arrayDimensions == original

@given(instance=oogen::OOType_strategy)
def test_oogen::ootype_numberOfIndirections_type(instance):
    assert isinstance(instance.numberOfIndirections, int)


@given(instance=oogen::OOType_strategy)
def test_oogen::ootype_numberOfIndirections_setter(instance):
    original = instance.numberOfIndirections
    instance.numberOfIndirections = original
    assert instance.numberOfIndirections == original

@given(instance=oogen::OOType_strategy)
def test_oogen::ootype_baseType_type(instance):
    assert isinstance(instance.baseType, str)


@given(instance=oogen::OOType_strategy)
def test_oogen::ootype_baseType_setter(instance):
    original = instance.baseType
    instance.baseType = original
    assert instance.baseType == original

@given(instance=OOStatement_strategy)
@settings(max_examples=50)
def test_oostatement_instantiation(instance):
    assert isinstance(instance, OOStatement)

@given(instance=oogen::OOBreak_strategy)
@settings(max_examples=50)
def test_oogen::oobreak_instantiation(instance):
    assert isinstance(instance, oogen::OOBreak)

@given(instance=oogen::OOContinue_strategy)
@settings(max_examples=50)
def test_oogen::oocontinue_instantiation(instance):
    assert isinstance(instance, oogen::OOContinue)

@given(instance=oogen::OOSwitch_strategy)
@settings(max_examples=50)
def test_oogen::ooswitch_instantiation(instance):
    assert isinstance(instance, oogen::OOSwitch)

@given(instance=oogen::OOForEach_strategy)
@settings(max_examples=50)
def test_oogen::ooforeach_instantiation(instance):
    assert isinstance(instance, oogen::OOForEach)

@given(instance=oogen::OOCompoundStatement_strategy)
@settings(max_examples=50)
def test_oogen::oocompoundstatement_instantiation(instance):
    assert isinstance(instance, oogen::OOCompoundStatement)

@given(instance=oogen::OOConditionalStatement_strategy)
@settings(max_examples=50)
def test_oogen::ooconditionalstatement_instantiation(instance):
    assert isinstance(instance, oogen::OOConditionalStatement)

@given(instance=oogen::OOReturn_strategy)
@settings(max_examples=50)
def test_oogen::ooreturn_instantiation(instance):
    assert isinstance(instance, oogen::OOReturn)

@given(instance=oogen::OOEmptyStatement_strategy)
@settings(max_examples=50)
def test_oogen::ooemptystatement_instantiation(instance):
    assert isinstance(instance, oogen::OOEmptyStatement)

@given(instance=oogen::OOVariableDeclarationList_strategy)
@settings(max_examples=50)
def test_oogen::oovariabledeclarationlist_instantiation(instance):
    assert isinstance(instance, oogen::OOVariableDeclarationList)

@given(instance=oogen::OOExpression_strategy)
@settings(max_examples=50)
def test_oogen::ooexpression_instantiation(instance):
    assert isinstance(instance, oogen::OOExpression)

@given(instance=oogen::OOVariable_strategy)
@settings(max_examples=50)
def test_oogen::oovariable_instantiation(instance):
    assert isinstance(instance, oogen::OOVariable)

@given(instance=oogen::OOVariable_strategy)
def test_oogen::oovariable_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=oogen::OOVariable_strategy)
def test_oogen::oovariable_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=oogen::OOVariable_strategy)
def test_oogen::oovariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oogen::OOVariable_strategy)
def test_oogen::oovariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oogen::OOConstructor_strategy)
@settings(max_examples=50)
def test_oogen::ooconstructor_instantiation(instance):
    assert isinstance(instance, oogen::OOConstructor)

@given(instance=oogen::OOConstructor_strategy)
def test_oogen::ooconstructor_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=oogen::OOConstructor_strategy)
def test_oogen::ooconstructor_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=oogen::OOConstructor_strategy)
def test_oogen::ooconstructor_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=oogen::OOConstructor_strategy)
def test_oogen::ooconstructor_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=OOCommentOwner_strategy)
@settings(max_examples=50)
def test_oocommentowner_instantiation(instance):
    assert isinstance(instance, OOCommentOwner)

@given(instance=oogen::OOMethod_strategy)
@settings(max_examples=50)
def test_oogen::oomethod_instantiation(instance):
    assert isinstance(instance, oogen::OOMethod)

@given(instance=oogen::OOMethod_strategy)
def test_oogen::oomethod_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=oogen::OOMethod_strategy)
def test_oogen::oomethod_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=oogen::OOMethod_strategy)
def test_oogen::oomethod_languages_type(instance):
    assert isinstance(instance.languages, str)


@given(instance=oogen::OOMethod_strategy)
def test_oogen::oomethod_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original

@given(instance=oogen::OOMethod_strategy)
def test_oogen::oomethod_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=oogen::OOMethod_strategy)
def test_oogen::oomethod_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=oogen::OOMethod_strategy)
def test_oogen::oomethod_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oogen::OOMethod_strategy)
def test_oogen::oomethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oogen::OOStatement_strategy)
@settings(max_examples=50)
def test_oogen::oostatement_instantiation(instance):
    assert isinstance(instance, oogen::OOStatement)

@given(instance=OOVariable_strategy)
@settings(max_examples=50)
def test_oovariable_instantiation(instance):
    assert isinstance(instance, OOVariable)

@given(instance=oogen::OOMember_strategy)
@settings(max_examples=50)
def test_oogen::oomember_instantiation(instance):
    assert isinstance(instance, oogen::OOMember)

@given(instance=oogen::OOMember_strategy)
def test_oogen::oomember_languages_type(instance):
    assert isinstance(instance.languages, str)


@given(instance=oogen::OOMember_strategy)
def test_oogen::oomember_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original

@given(instance=oogen::OOMember_strategy)
def test_oogen::oomember_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=oogen::OOMember_strategy)
def test_oogen::oomember_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=oogen::OOMember_strategy)
def test_oogen::oomember_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=oogen::OOMember_strategy)
def test_oogen::oomember_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=oogen::OOPackage_strategy)
@settings(max_examples=50)
def test_oogen::oopackage_instantiation(instance):
    assert isinstance(instance, oogen::OOPackage)

@given(instance=oogen::OOPackage_strategy)
def test_oogen::oopackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oogen::OOPackage_strategy)
def test_oogen::oopackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oogen::OOEnumeration_strategy)
@settings(max_examples=50)
def test_oogen::ooenumeration_instantiation(instance):
    assert isinstance(instance, oogen::OOEnumeration)

@given(instance=oogen::OOEnumeration_strategy)
def test_oogen::ooenumeration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oogen::OOEnumeration_strategy)
def test_oogen::ooenumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oogen::OOEnumeration_strategy)
def test_oogen::ooenumeration_options_type(instance):
    assert isinstance(instance.options, str)


@given(instance=oogen::OOEnumeration_strategy)
def test_oogen::ooenumeration_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original

@given(instance=oogen::OOClass_strategy)
@settings(max_examples=50)
def test_oogen::ooclass_instantiation(instance):
    assert isinstance(instance, oogen::OOClass)

@given(instance=oogen::OOClass_strategy)
def test_oogen::ooclass_keep_type(instance):
    assert isinstance(instance.keep, bool)


@given(instance=oogen::OOClass_strategy)
def test_oogen::ooclass_keep_setter(instance):
    original = instance.keep
    instance.keep = original
    assert instance.keep == original

@given(instance=oogen::OOClass_strategy)
def test_oogen::ooclass_languages_type(instance):
    assert isinstance(instance.languages, str)


@given(instance=oogen::OOClass_strategy)
def test_oogen::ooclass_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original

@given(instance=oogen::OOClass_strategy)
def test_oogen::ooclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oogen::OOClass_strategy)
def test_oogen::ooclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
