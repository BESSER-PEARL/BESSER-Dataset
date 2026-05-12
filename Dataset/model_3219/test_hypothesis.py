import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    oogen_OOCommentOwner,
    oogen_OOComment,
    OOComparatorExpression,
    oogen_OOEqualsExpression,
    oogen_OOLanguageSpecificSnippet,
    OOOneOperandArithmeticExpression,
    oogen_OOPostfixDecrementExpression,
    oogen_OOPrefixIncrementExpression,
    oogen_OOPrefixDecrementExpression,
    oogen_OOPostfixIncrementExpression,
    oogen_OOPlusExpression,
    oogen_OOMinusExpression,
    oogen_OOBracketedExpression,
    oogen_OOBitWiseComplement,
    oogen_OOLessEqualsExpression,
    oogen_OOGreaterEqualsExpression,
    oogen_OONotEqualsExpression,
    oogen_OOLessThanExpression,
    oogen_OOGreaterThanExpression,
    OOCompoundStatement,
    oogen_OODefault,
    oogen_OOCase,
    OOConditionalStatement,
    oogen_OOFor,
    oogen_OOIf,
    OOLogicalExpression,
    oogen_OOTernaryOperator,
    oogen_OOLogicalLiteral,
    oogen_OOOneOperandLogicalExpression,
    oogen_OOComparatorExpression,
    oogen_OOTwoOperandLogicalExpression,
    OOOneOperandLogicalExpression,
    oogen_OONotExpression,
    OOTwoOperandLogicalExpression,
    oogen_OOXorExpression,
    oogen_OOOrExpression,
    oogen_OOAndExpression,
    OOTwoOperandArithmeticExpression,
    oogen_OOTwoOperandAssignableExpression,
    oogen_OORootExpression,
    oogen_OOPowerExpression,
    oogen_OODoWhile,
    oogen_OOWhile,
    OOArithmeticExpression,
    oogen_OOOneOperandArithmeticExpression,
    oogen_OOFloatLiteral,
    oogen_OODoubleLiteral,
    oogen_OOLongLiteral,
    oogen_OOIntegerLiteral,
    oogen_OOTwoOperandArithmeticExpression,
    OOExpression,
    oogen_OONullLiteral,
    oogen_OOFieldReferenceExpression,
    oogen_OOBoolLiteral,
    oogen_OOIndexing,
    oogen_OONewClass,
    oogen_OOLogicalExpression,
    oogen_OOTypeCast,
    oogen_OONewArray,
    oogen_OOEmptyExpression,
    oogen_OOAssignmentExpression,
    oogen_OOVariableReferenceExpression,
    oogen_OOThisLiteral,
    oogen_OOLanguageSpecificExpression,
    oogen_OOFunctionCallExpression,
    oogen_OOStringLiteral,
    oogen_OOInitializerList,
    oogen_OOArithmeticExpression,
    oogen_OOModel,
    OOTwoOperandAssignableExpression,
    oogen_OOBitwiseXorExpression,
    oogen_OOBitwiseOrExpression,
    oogen_OOBitWiseLeftShift,
    oogen_OOBitwiseAndExpression,
    oogen_OOMultiplicationExpression,
    oogen_OOBitWiseRightShift,
    oogen_OOSubtractionExpression,
    oogen_OOIntegerDivisionExpression,
    oogen_OODivisionExpression,
    oogen_OOModuloExpression,
    oogen_OOAdditionExpression,
    oogen_OOType,
    OOStatement,
    oogen_OOEmptyStatement,
    oogen_OOExpression,
    oogen_OOCompoundStatement,
    oogen_OOReturn,
    oogen_OOSwitch,
    oogen_OOVariableDeclarationList,
    oogen_OOContinue,
    oogen_OOBreak,
    oogen_OOForEach,
    oogen_OOConditionalStatement,
    oogen_OOVariable,
    oogen_OOConstructor,
    OOCommentOwner,
    oogen_OOStatement,
    oogen_OOMethod,
    OOVariable,
    oogen_OOMember,
    oogen_OOPackage,
    oogen_OOEnumeration,
    oogen_OOClass,
    OOVisibility,
    OOLanguage,
    OOBaseType,
    OOCollectionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oogen_oocommentowner_is_not_abstract():
    assert not inspect.isabstract(oogen_OOCommentOwner)


def test_oogen_oocommentowner_constructor_exists():
    assert callable(oogen_OOCommentOwner.__init__)


def test_oogen_oocommentowner_constructor_args():
    sig = inspect.signature(oogen_OOCommentOwner.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oocomment_is_not_abstract():
    assert not inspect.isabstract(oogen_OOComment)


def test_oogen_oocomment_constructor_exists():
    assert callable(oogen_OOComment.__init__)


def test_oogen_oocomment_constructor_args():
    sig = inspect.signature(oogen_OOComment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "isBlockComment" in params, "Missing parameter 'isBlockComment'"

def test_oogen_oocomment_has_text():
    assert hasattr(oogen_OOComment, "text")
    descriptor = None
    for klass in oogen_OOComment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_oogen_oocomment_has_isBlockComment():
    assert hasattr(oogen_OOComment, "isBlockComment")
    descriptor = None
    for klass in oogen_OOComment.__mro__:
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



def test_oogen_ooequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOEqualsExpression)


def test_oogen_ooequalsexpression_constructor_exists():
    assert callable(oogen_OOEqualsExpression.__init__)


def test_oogen_ooequalsexpression_constructor_args():
    sig = inspect.signature(oogen_OOEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oolanguagespecificsnippet_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLanguageSpecificSnippet)


def test_oogen_oolanguagespecificsnippet_constructor_exists():
    assert callable(oogen_OOLanguageSpecificSnippet.__init__)


def test_oogen_oolanguagespecificsnippet_constructor_args():
    sig = inspect.signature(oogen_OOLanguageSpecificSnippet.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "lang" in params, "Missing parameter 'lang'"

def test_oogen_oolanguagespecificsnippet_has_code():
    assert hasattr(oogen_OOLanguageSpecificSnippet, "code")
    descriptor = None
    for klass in oogen_OOLanguageSpecificSnippet.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_oogen_oolanguagespecificsnippet_has_lang():
    assert hasattr(oogen_OOLanguageSpecificSnippet, "lang")
    descriptor = None
    for klass in oogen_OOLanguageSpecificSnippet.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)



def test_oooneoperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(OOOneOperandArithmeticExpression)


def test_oooneoperandarithmeticexpression_constructor_exists():
    assert callable(OOOneOperandArithmeticExpression.__init__)


def test_oooneoperandarithmeticexpression_constructor_args():
    sig = inspect.signature(OOOneOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oopostfixdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPostfixDecrementExpression)


def test_oogen_oopostfixdecrementexpression_constructor_exists():
    assert callable(oogen_OOPostfixDecrementExpression.__init__)


def test_oogen_oopostfixdecrementexpression_constructor_args():
    sig = inspect.signature(oogen_OOPostfixDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooprefixincrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPrefixIncrementExpression)


def test_oogen_ooprefixincrementexpression_constructor_exists():
    assert callable(oogen_OOPrefixIncrementExpression.__init__)


def test_oogen_ooprefixincrementexpression_constructor_args():
    sig = inspect.signature(oogen_OOPrefixIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooprefixdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPrefixDecrementExpression)


def test_oogen_ooprefixdecrementexpression_constructor_exists():
    assert callable(oogen_OOPrefixDecrementExpression.__init__)


def test_oogen_ooprefixdecrementexpression_constructor_args():
    sig = inspect.signature(oogen_OOPrefixDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oopostfixincrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPostfixIncrementExpression)


def test_oogen_oopostfixincrementexpression_constructor_exists():
    assert callable(oogen_OOPostfixIncrementExpression.__init__)


def test_oogen_oopostfixincrementexpression_constructor_args():
    sig = inspect.signature(oogen_OOPostfixIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooplusexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPlusExpression)


def test_oogen_ooplusexpression_constructor_exists():
    assert callable(oogen_OOPlusExpression.__init__)


def test_oogen_ooplusexpression_constructor_args():
    sig = inspect.signature(oogen_OOPlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oominusexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOMinusExpression)


def test_oogen_oominusexpression_constructor_exists():
    assert callable(oogen_OOMinusExpression.__init__)


def test_oogen_oominusexpression_constructor_args():
    sig = inspect.signature(oogen_OOMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oobracketedexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBracketedExpression)


def test_oogen_oobracketedexpression_constructor_exists():
    assert callable(oogen_OOBracketedExpression.__init__)


def test_oogen_oobracketedexpression_constructor_args():
    sig = inspect.signature(oogen_OOBracketedExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oobitwisecomplement_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitWiseComplement)


def test_oogen_oobitwisecomplement_constructor_exists():
    assert callable(oogen_OOBitWiseComplement.__init__)


def test_oogen_oobitwisecomplement_constructor_args():
    sig = inspect.signature(oogen_OOBitWiseComplement.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oolessequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLessEqualsExpression)


def test_oogen_oolessequalsexpression_constructor_exists():
    assert callable(oogen_OOLessEqualsExpression.__init__)


def test_oogen_oolessequalsexpression_constructor_args():
    sig = inspect.signature(oogen_OOLessEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oogreaterequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOGreaterEqualsExpression)


def test_oogen_oogreaterequalsexpression_constructor_exists():
    assert callable(oogen_OOGreaterEqualsExpression.__init__)


def test_oogen_oogreaterequalsexpression_constructor_args():
    sig = inspect.signature(oogen_OOGreaterEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oonotequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OONotEqualsExpression)


def test_oogen_oonotequalsexpression_constructor_exists():
    assert callable(oogen_OONotEqualsExpression.__init__)


def test_oogen_oonotequalsexpression_constructor_args():
    sig = inspect.signature(oogen_OONotEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oolessthanexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLessThanExpression)


def test_oogen_oolessthanexpression_constructor_exists():
    assert callable(oogen_OOLessThanExpression.__init__)


def test_oogen_oolessthanexpression_constructor_args():
    sig = inspect.signature(oogen_OOLessThanExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oogreaterthanexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOGreaterThanExpression)


def test_oogen_oogreaterthanexpression_constructor_exists():
    assert callable(oogen_OOGreaterThanExpression.__init__)


def test_oogen_oogreaterthanexpression_constructor_args():
    sig = inspect.signature(oogen_OOGreaterThanExpression.__init__)
    params = list(sig.parameters.keys())



def test_oocompoundstatement_is_not_abstract():
    assert not inspect.isabstract(OOCompoundStatement)


def test_oocompoundstatement_constructor_exists():
    assert callable(OOCompoundStatement.__init__)


def test_oocompoundstatement_constructor_args():
    sig = inspect.signature(OOCompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oodefault_is_not_abstract():
    assert not inspect.isabstract(oogen_OODefault)


def test_oogen_oodefault_constructor_exists():
    assert callable(oogen_OODefault.__init__)


def test_oogen_oodefault_constructor_args():
    sig = inspect.signature(oogen_OODefault.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oocase_is_not_abstract():
    assert not inspect.isabstract(oogen_OOCase)


def test_oogen_oocase_constructor_exists():
    assert callable(oogen_OOCase.__init__)


def test_oogen_oocase_constructor_args():
    sig = inspect.signature(oogen_OOCase.__init__)
    params = list(sig.parameters.keys())



def test_ooconditionalstatement_is_not_abstract():
    assert not inspect.isabstract(OOConditionalStatement)


def test_ooconditionalstatement_constructor_exists():
    assert callable(OOConditionalStatement.__init__)


def test_ooconditionalstatement_constructor_args():
    sig = inspect.signature(OOConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oofor_is_not_abstract():
    assert not inspect.isabstract(oogen_OOFor)


def test_oogen_oofor_constructor_exists():
    assert callable(oogen_OOFor.__init__)


def test_oogen_oofor_constructor_args():
    sig = inspect.signature(oogen_OOFor.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooif_is_not_abstract():
    assert not inspect.isabstract(oogen_OOIf)


def test_oogen_ooif_constructor_exists():
    assert callable(oogen_OOIf.__init__)


def test_oogen_ooif_constructor_args():
    sig = inspect.signature(oogen_OOIf.__init__)
    params = list(sig.parameters.keys())



def test_oologicalexpression_is_not_abstract():
    assert not inspect.isabstract(OOLogicalExpression)


def test_oologicalexpression_constructor_exists():
    assert callable(OOLogicalExpression.__init__)


def test_oologicalexpression_constructor_args():
    sig = inspect.signature(OOLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooternaryoperator_is_not_abstract():
    assert not inspect.isabstract(oogen_OOTernaryOperator)


def test_oogen_ooternaryoperator_constructor_exists():
    assert callable(oogen_OOTernaryOperator.__init__)


def test_oogen_ooternaryoperator_constructor_args():
    sig = inspect.signature(oogen_OOTernaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oologicalliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLogicalLiteral)


def test_oogen_oologicalliteral_constructor_exists():
    assert callable(oogen_OOLogicalLiteral.__init__)


def test_oogen_oologicalliteral_constructor_args():
    sig = inspect.signature(oogen_OOLogicalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen_oologicalliteral_has_value():
    assert hasattr(oogen_OOLogicalLiteral, "value")
    descriptor = None
    for klass in oogen_OOLogicalLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen_oooneoperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOOneOperandLogicalExpression)


def test_oogen_oooneoperandlogicalexpression_constructor_exists():
    assert callable(oogen_OOOneOperandLogicalExpression.__init__)


def test_oogen_oooneoperandlogicalexpression_constructor_args():
    sig = inspect.signature(oogen_OOOneOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oocomparatorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOComparatorExpression)


def test_oogen_oocomparatorexpression_constructor_exists():
    assert callable(oogen_OOComparatorExpression.__init__)


def test_oogen_oocomparatorexpression_constructor_args():
    sig = inspect.signature(oogen_OOComparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ootwooperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOTwoOperandLogicalExpression)


def test_oogen_ootwooperandlogicalexpression_constructor_exists():
    assert callable(oogen_OOTwoOperandLogicalExpression.__init__)


def test_oogen_ootwooperandlogicalexpression_constructor_args():
    sig = inspect.signature(oogen_OOTwoOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oooneoperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(OOOneOperandLogicalExpression)


def test_oooneoperandlogicalexpression_constructor_exists():
    assert callable(OOOneOperandLogicalExpression.__init__)


def test_oooneoperandlogicalexpression_constructor_args():
    sig = inspect.signature(OOOneOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oonotexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OONotExpression)


def test_oogen_oonotexpression_constructor_exists():
    assert callable(oogen_OONotExpression.__init__)


def test_oogen_oonotexpression_constructor_args():
    sig = inspect.signature(oogen_OONotExpression.__init__)
    params = list(sig.parameters.keys())



def test_ootwooperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(OOTwoOperandLogicalExpression)


def test_ootwooperandlogicalexpression_constructor_exists():
    assert callable(OOTwoOperandLogicalExpression.__init__)


def test_ootwooperandlogicalexpression_constructor_args():
    sig = inspect.signature(OOTwoOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooxorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOXorExpression)


def test_oogen_ooxorexpression_constructor_exists():
    assert callable(oogen_OOXorExpression.__init__)


def test_oogen_ooxorexpression_constructor_args():
    sig = inspect.signature(oogen_OOXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOOrExpression)


def test_oogen_ooorexpression_constructor_exists():
    assert callable(oogen_OOOrExpression.__init__)


def test_oogen_ooorexpression_constructor_args():
    sig = inspect.signature(oogen_OOOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooandexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOAndExpression)


def test_oogen_ooandexpression_constructor_exists():
    assert callable(oogen_OOAndExpression.__init__)


def test_oogen_ooandexpression_constructor_args():
    sig = inspect.signature(oogen_OOAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ootwooperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(OOTwoOperandArithmeticExpression)


def test_ootwooperandarithmeticexpression_constructor_exists():
    assert callable(OOTwoOperandArithmeticExpression.__init__)


def test_ootwooperandarithmeticexpression_constructor_args():
    sig = inspect.signature(OOTwoOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ootwooperandassignableexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOTwoOperandAssignableExpression)


def test_oogen_ootwooperandassignableexpression_constructor_exists():
    assert callable(oogen_OOTwoOperandAssignableExpression.__init__)


def test_oogen_ootwooperandassignableexpression_constructor_args():
    sig = inspect.signature(oogen_OOTwoOperandAssignableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "assigned" in params, "Missing parameter 'assigned'"

def test_oogen_ootwooperandassignableexpression_has_assigned():
    assert hasattr(oogen_OOTwoOperandAssignableExpression, "assigned")
    descriptor = None
    for klass in oogen_OOTwoOperandAssignableExpression.__mro__:
        if "assigned" in klass.__dict__:
            descriptor = klass.__dict__["assigned"]
            break
    assert isinstance(descriptor, property)



def test_oogen_oorootexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OORootExpression)


def test_oogen_oorootexpression_constructor_exists():
    assert callable(oogen_OORootExpression.__init__)


def test_oogen_oorootexpression_constructor_args():
    sig = inspect.signature(oogen_OORootExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oopowerexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPowerExpression)


def test_oogen_oopowerexpression_constructor_exists():
    assert callable(oogen_OOPowerExpression.__init__)


def test_oogen_oopowerexpression_constructor_args():
    sig = inspect.signature(oogen_OOPowerExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oodowhile_is_not_abstract():
    assert not inspect.isabstract(oogen_OODoWhile)


def test_oogen_oodowhile_constructor_exists():
    assert callable(oogen_OODoWhile.__init__)


def test_oogen_oodowhile_constructor_args():
    sig = inspect.signature(oogen_OODoWhile.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oowhile_is_not_abstract():
    assert not inspect.isabstract(oogen_OOWhile)


def test_oogen_oowhile_constructor_exists():
    assert callable(oogen_OOWhile.__init__)


def test_oogen_oowhile_constructor_args():
    sig = inspect.signature(oogen_OOWhile.__init__)
    params = list(sig.parameters.keys())



def test_ooarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(OOArithmeticExpression)


def test_ooarithmeticexpression_constructor_exists():
    assert callable(OOArithmeticExpression.__init__)


def test_ooarithmeticexpression_constructor_args():
    sig = inspect.signature(OOArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oooneoperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOOneOperandArithmeticExpression)


def test_oogen_oooneoperandarithmeticexpression_constructor_exists():
    assert callable(oogen_OOOneOperandArithmeticExpression.__init__)


def test_oogen_oooneoperandarithmeticexpression_constructor_args():
    sig = inspect.signature(oogen_OOOneOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oofloatliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOFloatLiteral)


def test_oogen_oofloatliteral_constructor_exists():
    assert callable(oogen_OOFloatLiteral.__init__)


def test_oogen_oofloatliteral_constructor_args():
    sig = inspect.signature(oogen_OOFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen_oofloatliteral_has_value():
    assert hasattr(oogen_OOFloatLiteral, "value")
    descriptor = None
    for klass in oogen_OOFloatLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen_oodoubleliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OODoubleLiteral)


def test_oogen_oodoubleliteral_constructor_exists():
    assert callable(oogen_OODoubleLiteral.__init__)


def test_oogen_oodoubleliteral_constructor_args():
    sig = inspect.signature(oogen_OODoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen_oodoubleliteral_has_value():
    assert hasattr(oogen_OODoubleLiteral, "value")
    descriptor = None
    for klass in oogen_OODoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen_oolongliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLongLiteral)


def test_oogen_oolongliteral_constructor_exists():
    assert callable(oogen_OOLongLiteral.__init__)


def test_oogen_oolongliteral_constructor_args():
    sig = inspect.signature(oogen_OOLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen_oolongliteral_has_value():
    assert hasattr(oogen_OOLongLiteral, "value")
    descriptor = None
    for klass in oogen_OOLongLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen_oointegerliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOIntegerLiteral)


def test_oogen_oointegerliteral_constructor_exists():
    assert callable(oogen_OOIntegerLiteral.__init__)


def test_oogen_oointegerliteral_constructor_args():
    sig = inspect.signature(oogen_OOIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen_oointegerliteral_has_value():
    assert hasattr(oogen_OOIntegerLiteral, "value")
    descriptor = None
    for klass in oogen_OOIntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen_ootwooperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOTwoOperandArithmeticExpression)


def test_oogen_ootwooperandarithmeticexpression_constructor_exists():
    assert callable(oogen_OOTwoOperandArithmeticExpression.__init__)


def test_oogen_ootwooperandarithmeticexpression_constructor_args():
    sig = inspect.signature(oogen_OOTwoOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ooexpression_is_not_abstract():
    assert not inspect.isabstract(OOExpression)


def test_ooexpression_constructor_exists():
    assert callable(OOExpression.__init__)


def test_ooexpression_constructor_args():
    sig = inspect.signature(OOExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oonullliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OONullLiteral)


def test_oogen_oonullliteral_constructor_exists():
    assert callable(oogen_OONullLiteral.__init__)


def test_oogen_oonullliteral_constructor_args():
    sig = inspect.signature(oogen_OONullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oofieldreferenceexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOFieldReferenceExpression)


def test_oogen_oofieldreferenceexpression_constructor_exists():
    assert callable(oogen_OOFieldReferenceExpression.__init__)


def test_oogen_oofieldreferenceexpression_constructor_args():
    sig = inspect.signature(oogen_OOFieldReferenceExpression.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_oogen_oofieldreferenceexpression_has_fieldName():
    assert hasattr(oogen_OOFieldReferenceExpression, "fieldName")
    descriptor = None
    for klass in oogen_OOFieldReferenceExpression.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_oogen_ooboolliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBoolLiteral)


def test_oogen_ooboolliteral_constructor_exists():
    assert callable(oogen_OOBoolLiteral.__init__)


def test_oogen_ooboolliteral_constructor_args():
    sig = inspect.signature(oogen_OOBoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen_ooboolliteral_has_value():
    assert hasattr(oogen_OOBoolLiteral, "value")
    descriptor = None
    for klass in oogen_OOBoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen_ooindexing_is_not_abstract():
    assert not inspect.isabstract(oogen_OOIndexing)


def test_oogen_ooindexing_constructor_exists():
    assert callable(oogen_OOIndexing.__init__)


def test_oogen_ooindexing_constructor_args():
    sig = inspect.signature(oogen_OOIndexing.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oonewclass_is_not_abstract():
    assert not inspect.isabstract(oogen_OONewClass)


def test_oogen_oonewclass_constructor_exists():
    assert callable(oogen_OONewClass.__init__)


def test_oogen_oonewclass_constructor_args():
    sig = inspect.signature(oogen_OONewClass.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_oogen_oonewclass_has_className():
    assert hasattr(oogen_OONewClass, "className")
    descriptor = None
    for klass in oogen_OONewClass.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_oogen_oologicalexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLogicalExpression)


def test_oogen_oologicalexpression_constructor_exists():
    assert callable(oogen_OOLogicalExpression.__init__)


def test_oogen_oologicalexpression_constructor_args():
    sig = inspect.signature(oogen_OOLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ootypecast_is_not_abstract():
    assert not inspect.isabstract(oogen_OOTypeCast)


def test_oogen_ootypecast_constructor_exists():
    assert callable(oogen_OOTypeCast.__init__)


def test_oogen_ootypecast_constructor_args():
    sig = inspect.signature(oogen_OOTypeCast.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oonewarray_is_not_abstract():
    assert not inspect.isabstract(oogen_OONewArray)


def test_oogen_oonewarray_constructor_exists():
    assert callable(oogen_OONewArray.__init__)


def test_oogen_oonewarray_constructor_args():
    sig = inspect.signature(oogen_OONewArray.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooemptyexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOEmptyExpression)


def test_oogen_ooemptyexpression_constructor_exists():
    assert callable(oogen_OOEmptyExpression.__init__)


def test_oogen_ooemptyexpression_constructor_args():
    sig = inspect.signature(oogen_OOEmptyExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOAssignmentExpression)


def test_oogen_ooassignmentexpression_constructor_exists():
    assert callable(oogen_OOAssignmentExpression.__init__)


def test_oogen_ooassignmentexpression_constructor_args():
    sig = inspect.signature(oogen_OOAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oovariablereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOVariableReferenceExpression)


def test_oogen_oovariablereferenceexpression_constructor_exists():
    assert callable(oogen_OOVariableReferenceExpression.__init__)


def test_oogen_oovariablereferenceexpression_constructor_args():
    sig = inspect.signature(oogen_OOVariableReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oothisliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOThisLiteral)


def test_oogen_oothisliteral_constructor_exists():
    assert callable(oogen_OOThisLiteral.__init__)


def test_oogen_oothisliteral_constructor_args():
    sig = inspect.signature(oogen_OOThisLiteral.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oolanguagespecificexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLanguageSpecificExpression)


def test_oogen_oolanguagespecificexpression_constructor_exists():
    assert callable(oogen_OOLanguageSpecificExpression.__init__)


def test_oogen_oolanguagespecificexpression_constructor_args():
    sig = inspect.signature(oogen_OOLanguageSpecificExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oofunctioncallexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOFunctionCallExpression)


def test_oogen_oofunctioncallexpression_constructor_exists():
    assert callable(oogen_OOFunctionCallExpression.__init__)


def test_oogen_oofunctioncallexpression_constructor_args():
    sig = inspect.signature(oogen_OOFunctionCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_oogen_oofunctioncallexpression_has_functionName():
    assert hasattr(oogen_OOFunctionCallExpression, "functionName")
    descriptor = None
    for klass in oogen_OOFunctionCallExpression.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_oogen_oostringliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOStringLiteral)


def test_oogen_oostringliteral_constructor_exists():
    assert callable(oogen_OOStringLiteral.__init__)


def test_oogen_oostringliteral_constructor_args():
    sig = inspect.signature(oogen_OOStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oogen_oostringliteral_has_value():
    assert hasattr(oogen_OOStringLiteral, "value")
    descriptor = None
    for klass in oogen_OOStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oogen_ooinitializerlist_is_not_abstract():
    assert not inspect.isabstract(oogen_OOInitializerList)


def test_oogen_ooinitializerlist_constructor_exists():
    assert callable(oogen_OOInitializerList.__init__)


def test_oogen_ooinitializerlist_constructor_args():
    sig = inspect.signature(oogen_OOInitializerList.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOArithmeticExpression)


def test_oogen_ooarithmeticexpression_constructor_exists():
    assert callable(oogen_OOArithmeticExpression.__init__)


def test_oogen_ooarithmeticexpression_constructor_args():
    sig = inspect.signature(oogen_OOArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oomodel_is_not_abstract():
    assert not inspect.isabstract(oogen_OOModel)


def test_oogen_oomodel_constructor_exists():
    assert callable(oogen_OOModel.__init__)


def test_oogen_oomodel_constructor_args():
    sig = inspect.signature(oogen_OOModel.__init__)
    params = list(sig.parameters.keys())



def test_ootwooperandassignableexpression_is_not_abstract():
    assert not inspect.isabstract(OOTwoOperandAssignableExpression)


def test_ootwooperandassignableexpression_constructor_exists():
    assert callable(OOTwoOperandAssignableExpression.__init__)


def test_ootwooperandassignableexpression_constructor_args():
    sig = inspect.signature(OOTwoOperandAssignableExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oobitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitwiseXorExpression)


def test_oogen_oobitwisexorexpression_constructor_exists():
    assert callable(oogen_OOBitwiseXorExpression.__init__)


def test_oogen_oobitwisexorexpression_constructor_args():
    sig = inspect.signature(oogen_OOBitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oobitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitwiseOrExpression)


def test_oogen_oobitwiseorexpression_constructor_exists():
    assert callable(oogen_OOBitwiseOrExpression.__init__)


def test_oogen_oobitwiseorexpression_constructor_args():
    sig = inspect.signature(oogen_OOBitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oobitwiseleftshift_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitWiseLeftShift)


def test_oogen_oobitwiseleftshift_constructor_exists():
    assert callable(oogen_OOBitWiseLeftShift.__init__)


def test_oogen_oobitwiseleftshift_constructor_args():
    sig = inspect.signature(oogen_OOBitWiseLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oobitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitwiseAndExpression)


def test_oogen_oobitwiseandexpression_constructor_exists():
    assert callable(oogen_OOBitwiseAndExpression.__init__)


def test_oogen_oobitwiseandexpression_constructor_args():
    sig = inspect.signature(oogen_OOBitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oomultiplicationexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOMultiplicationExpression)


def test_oogen_oomultiplicationexpression_constructor_exists():
    assert callable(oogen_OOMultiplicationExpression.__init__)


def test_oogen_oomultiplicationexpression_constructor_args():
    sig = inspect.signature(oogen_OOMultiplicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oobitwiserightshift_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitWiseRightShift)


def test_oogen_oobitwiserightshift_constructor_exists():
    assert callable(oogen_OOBitWiseRightShift.__init__)


def test_oogen_oobitwiserightshift_constructor_args():
    sig = inspect.signature(oogen_OOBitWiseRightShift.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oosubtractionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOSubtractionExpression)


def test_oogen_oosubtractionexpression_constructor_exists():
    assert callable(oogen_OOSubtractionExpression.__init__)


def test_oogen_oosubtractionexpression_constructor_args():
    sig = inspect.signature(oogen_OOSubtractionExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oointegerdivisionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOIntegerDivisionExpression)


def test_oogen_oointegerdivisionexpression_constructor_exists():
    assert callable(oogen_OOIntegerDivisionExpression.__init__)


def test_oogen_oointegerdivisionexpression_constructor_args():
    sig = inspect.signature(oogen_OOIntegerDivisionExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oodivisionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OODivisionExpression)


def test_oogen_oodivisionexpression_constructor_exists():
    assert callable(oogen_OODivisionExpression.__init__)


def test_oogen_oodivisionexpression_constructor_args():
    sig = inspect.signature(oogen_OODivisionExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oomoduloexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOModuloExpression)


def test_oogen_oomoduloexpression_constructor_exists():
    assert callable(oogen_OOModuloExpression.__init__)


def test_oogen_oomoduloexpression_constructor_args():
    sig = inspect.signature(oogen_OOModuloExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooadditionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOAdditionExpression)


def test_oogen_ooadditionexpression_constructor_exists():
    assert callable(oogen_OOAdditionExpression.__init__)


def test_oogen_ooadditionexpression_constructor_args():
    sig = inspect.signature(oogen_OOAdditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ootype_is_not_abstract():
    assert not inspect.isabstract(oogen_OOType)


def test_oogen_ootype_constructor_exists():
    assert callable(oogen_OOType.__init__)


def test_oogen_ootype_constructor_args():
    sig = inspect.signature(oogen_OOType.__init__)
    params = list(sig.parameters.keys())
    assert "baseType" in params, "Missing parameter 'baseType'"
    assert "collectionType" in params, "Missing parameter 'collectionType'"
    assert "numberOfIndirections" in params, "Missing parameter 'numberOfIndirections'"
    assert "arrayDimensions" in params, "Missing parameter 'arrayDimensions'"

def test_oogen_ootype_has_baseType():
    assert hasattr(oogen_OOType, "baseType")
    descriptor = None
    for klass in oogen_OOType.__mro__:
        if "baseType" in klass.__dict__:
            descriptor = klass.__dict__["baseType"]
            break
    assert isinstance(descriptor, property)

def test_oogen_ootype_has_collectionType():
    assert hasattr(oogen_OOType, "collectionType")
    descriptor = None
    for klass in oogen_OOType.__mro__:
        if "collectionType" in klass.__dict__:
            descriptor = klass.__dict__["collectionType"]
            break
    assert isinstance(descriptor, property)

def test_oogen_ootype_has_numberOfIndirections():
    assert hasattr(oogen_OOType, "numberOfIndirections")
    descriptor = None
    for klass in oogen_OOType.__mro__:
        if "numberOfIndirections" in klass.__dict__:
            descriptor = klass.__dict__["numberOfIndirections"]
            break
    assert isinstance(descriptor, property)

def test_oogen_ootype_has_arrayDimensions():
    assert hasattr(oogen_OOType, "arrayDimensions")
    descriptor = None
    for klass in oogen_OOType.__mro__:
        if "arrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["arrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_oostatement_is_not_abstract():
    assert not inspect.isabstract(OOStatement)


def test_oostatement_constructor_exists():
    assert callable(OOStatement.__init__)


def test_oostatement_constructor_args():
    sig = inspect.signature(OOStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooemptystatement_is_not_abstract():
    assert not inspect.isabstract(oogen_OOEmptyStatement)


def test_oogen_ooemptystatement_constructor_exists():
    assert callable(oogen_OOEmptyStatement.__init__)


def test_oogen_ooemptystatement_constructor_args():
    sig = inspect.signature(oogen_OOEmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOExpression)


def test_oogen_ooexpression_constructor_exists():
    assert callable(oogen_OOExpression.__init__)


def test_oogen_ooexpression_constructor_args():
    sig = inspect.signature(oogen_OOExpression.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oocompoundstatement_is_not_abstract():
    assert not inspect.isabstract(oogen_OOCompoundStatement)


def test_oogen_oocompoundstatement_constructor_exists():
    assert callable(oogen_OOCompoundStatement.__init__)


def test_oogen_oocompoundstatement_constructor_args():
    sig = inspect.signature(oogen_OOCompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooreturn_is_not_abstract():
    assert not inspect.isabstract(oogen_OOReturn)


def test_oogen_ooreturn_constructor_exists():
    assert callable(oogen_OOReturn.__init__)


def test_oogen_ooreturn_constructor_args():
    sig = inspect.signature(oogen_OOReturn.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooswitch_is_not_abstract():
    assert not inspect.isabstract(oogen_OOSwitch)


def test_oogen_ooswitch_constructor_exists():
    assert callable(oogen_OOSwitch.__init__)


def test_oogen_ooswitch_constructor_args():
    sig = inspect.signature(oogen_OOSwitch.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oovariabledeclarationlist_is_not_abstract():
    assert not inspect.isabstract(oogen_OOVariableDeclarationList)


def test_oogen_oovariabledeclarationlist_constructor_exists():
    assert callable(oogen_OOVariableDeclarationList.__init__)


def test_oogen_oovariabledeclarationlist_constructor_args():
    sig = inspect.signature(oogen_OOVariableDeclarationList.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oocontinue_is_not_abstract():
    assert not inspect.isabstract(oogen_OOContinue)


def test_oogen_oocontinue_constructor_exists():
    assert callable(oogen_OOContinue.__init__)


def test_oogen_oocontinue_constructor_args():
    sig = inspect.signature(oogen_OOContinue.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oobreak_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBreak)


def test_oogen_oobreak_constructor_exists():
    assert callable(oogen_OOBreak.__init__)


def test_oogen_oobreak_constructor_args():
    sig = inspect.signature(oogen_OOBreak.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooforeach_is_not_abstract():
    assert not inspect.isabstract(oogen_OOForEach)


def test_oogen_ooforeach_constructor_exists():
    assert callable(oogen_OOForEach.__init__)


def test_oogen_ooforeach_constructor_args():
    sig = inspect.signature(oogen_OOForEach.__init__)
    params = list(sig.parameters.keys())



def test_oogen_ooconditionalstatement_is_not_abstract():
    assert not inspect.isabstract(oogen_OOConditionalStatement)


def test_oogen_ooconditionalstatement_constructor_exists():
    assert callable(oogen_OOConditionalStatement.__init__)


def test_oogen_ooconditionalstatement_constructor_args():
    sig = inspect.signature(oogen_OOConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oovariable_is_not_abstract():
    assert not inspect.isabstract(oogen_OOVariable)


def test_oogen_oovariable_constructor_exists():
    assert callable(oogen_OOVariable.__init__)


def test_oogen_oovariable_constructor_args():
    sig = inspect.signature(oogen_OOVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "transient" in params, "Missing parameter 'transient'"

def test_oogen_oovariable_has_name():
    assert hasattr(oogen_OOVariable, "name")
    descriptor = None
    for klass in oogen_OOVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oogen_oovariable_has_transient():
    assert hasattr(oogen_OOVariable, "transient")
    descriptor = None
    for klass in oogen_OOVariable.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_oogen_ooconstructor_is_not_abstract():
    assert not inspect.isabstract(oogen_OOConstructor)


def test_oogen_ooconstructor_constructor_exists():
    assert callable(oogen_OOConstructor.__init__)


def test_oogen_ooconstructor_constructor_args():
    sig = inspect.signature(oogen_OOConstructor.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_oogen_ooconstructor_has_className():
    assert hasattr(oogen_OOConstructor, "className")
    descriptor = None
    for klass in oogen_OOConstructor.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_oogen_ooconstructor_has_visibility():
    assert hasattr(oogen_OOConstructor, "visibility")
    descriptor = None
    for klass in oogen_OOConstructor.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_oocommentowner_is_not_abstract():
    assert not inspect.isabstract(OOCommentOwner)


def test_oocommentowner_constructor_exists():
    assert callable(OOCommentOwner.__init__)


def test_oocommentowner_constructor_args():
    sig = inspect.signature(OOCommentOwner.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oostatement_is_not_abstract():
    assert not inspect.isabstract(oogen_OOStatement)


def test_oogen_oostatement_constructor_exists():
    assert callable(oogen_OOStatement.__init__)


def test_oogen_oostatement_constructor_args():
    sig = inspect.signature(oogen_OOStatement.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oomethod_is_not_abstract():
    assert not inspect.isabstract(oogen_OOMethod)


def test_oogen_oomethod_constructor_exists():
    assert callable(oogen_OOMethod.__init__)


def test_oogen_oomethod_constructor_args():
    sig = inspect.signature(oogen_OOMethod.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "languages" in params, "Missing parameter 'languages'"
    assert "name" in params, "Missing parameter 'name'"
    assert "static" in params, "Missing parameter 'static'"

def test_oogen_oomethod_has_visibility():
    assert hasattr(oogen_OOMethod, "visibility")
    descriptor = None
    for klass in oogen_OOMethod.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_oogen_oomethod_has_languages():
    assert hasattr(oogen_OOMethod, "languages")
    descriptor = None
    for klass in oogen_OOMethod.__mro__:
        if "languages" in klass.__dict__:
            descriptor = klass.__dict__["languages"]
            break
    assert isinstance(descriptor, property)

def test_oogen_oomethod_has_name():
    assert hasattr(oogen_OOMethod, "name")
    descriptor = None
    for klass in oogen_OOMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oogen_oomethod_has_static():
    assert hasattr(oogen_OOMethod, "static")
    descriptor = None
    for klass in oogen_OOMethod.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_oovariable_is_not_abstract():
    assert not inspect.isabstract(OOVariable)


def test_oovariable_constructor_exists():
    assert callable(OOVariable.__init__)


def test_oovariable_constructor_args():
    sig = inspect.signature(OOVariable.__init__)
    params = list(sig.parameters.keys())



def test_oogen_oomember_is_not_abstract():
    assert not inspect.isabstract(oogen_OOMember)


def test_oogen_oomember_constructor_exists():
    assert callable(oogen_OOMember.__init__)


def test_oogen_oomember_constructor_args():
    sig = inspect.signature(oogen_OOMember.__init__)
    params = list(sig.parameters.keys())
    assert "languages" in params, "Missing parameter 'languages'"
    assert "static" in params, "Missing parameter 'static'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_oogen_oomember_has_languages():
    assert hasattr(oogen_OOMember, "languages")
    descriptor = None
    for klass in oogen_OOMember.__mro__:
        if "languages" in klass.__dict__:
            descriptor = klass.__dict__["languages"]
            break
    assert isinstance(descriptor, property)

def test_oogen_oomember_has_static():
    assert hasattr(oogen_OOMember, "static")
    descriptor = None
    for klass in oogen_OOMember.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_oogen_oomember_has_visibility():
    assert hasattr(oogen_OOMember, "visibility")
    descriptor = None
    for klass in oogen_OOMember.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_oogen_oopackage_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPackage)


def test_oogen_oopackage_constructor_exists():
    assert callable(oogen_OOPackage.__init__)


def test_oogen_oopackage_constructor_args():
    sig = inspect.signature(oogen_OOPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oogen_oopackage_has_name():
    assert hasattr(oogen_OOPackage, "name")
    descriptor = None
    for klass in oogen_OOPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oogen_ooenumeration_is_not_abstract():
    assert not inspect.isabstract(oogen_OOEnumeration)


def test_oogen_ooenumeration_constructor_exists():
    assert callable(oogen_OOEnumeration.__init__)


def test_oogen_ooenumeration_constructor_args():
    sig = inspect.signature(oogen_OOEnumeration.__init__)
    params = list(sig.parameters.keys())
    assert "options" in params, "Missing parameter 'options'"
    assert "name" in params, "Missing parameter 'name'"

def test_oogen_ooenumeration_has_options():
    assert hasattr(oogen_OOEnumeration, "options")
    descriptor = None
    for klass in oogen_OOEnumeration.__mro__:
        if "options" in klass.__dict__:
            descriptor = klass.__dict__["options"]
            break
    assert isinstance(descriptor, property)

def test_oogen_ooenumeration_has_name():
    assert hasattr(oogen_OOEnumeration, "name")
    descriptor = None
    for klass in oogen_OOEnumeration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oogen_ooclass_is_not_abstract():
    assert not inspect.isabstract(oogen_OOClass)


def test_oogen_ooclass_constructor_exists():
    assert callable(oogen_OOClass.__init__)


def test_oogen_ooclass_constructor_args():
    sig = inspect.signature(oogen_OOClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "keep" in params, "Missing parameter 'keep'"
    assert "languages" in params, "Missing parameter 'languages'"

def test_oogen_ooclass_has_name():
    assert hasattr(oogen_OOClass, "name")
    descriptor = None
    for klass in oogen_OOClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oogen_ooclass_has_keep():
    assert hasattr(oogen_OOClass, "keep")
    descriptor = None
    for klass in oogen_OOClass.__mro__:
        if "keep" in klass.__dict__:
            descriptor = klass.__dict__["keep"]
            break
    assert isinstance(descriptor, property)

def test_oogen_ooclass_has_languages():
    assert hasattr(oogen_OOClass, "languages")
    descriptor = None
    for klass in oogen_OOClass.__mro__:
        if "languages" in klass.__dict__:
            descriptor = klass.__dict__["languages"]
            break
    assert isinstance(descriptor, property)

def test_oovisibility_exists():
    # Check that the Enumeration exists
    assert OOVisibility is not None

def test_oovisibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OOVisibility]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
        "PROTECTED",
        "PACKAGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OOVisibility"

def test_oolanguage_exists():
    # Check that the Enumeration exists
    assert OOLanguage is not None

def test_oolanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OOLanguage]
    expected_literals = [
        "JAVA",
        "CPP",
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
        "INT",
        "BYTE",
        "DOUBLE",
        "OBJECT",
        "LONG",
        "STRING",
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
        "SET",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OOCollectionType"


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
oogen_OOCommentOwner_strategy = st.builds(
    oogen_OOCommentOwner,
)
oogen_OOComment_strategy = st.builds(
    oogen_OOComment,
    text=
        safe_text,
    isBlockComment=
        st.booleans()
)
OOComparatorExpression_strategy = st.builds(
    OOComparatorExpression,
)
oogen_OOEqualsExpression_strategy = st.builds(
    oogen_OOEqualsExpression,
)
oogen_OOLanguageSpecificSnippet_strategy = st.builds(
    oogen_OOLanguageSpecificSnippet,
    code=
        safe_text,
    lang=
        safe_text
)
OOOneOperandArithmeticExpression_strategy = st.builds(
    OOOneOperandArithmeticExpression,
)
oogen_OOPostfixDecrementExpression_strategy = st.builds(
    oogen_OOPostfixDecrementExpression,
)
oogen_OOPrefixIncrementExpression_strategy = st.builds(
    oogen_OOPrefixIncrementExpression,
)
oogen_OOPrefixDecrementExpression_strategy = st.builds(
    oogen_OOPrefixDecrementExpression,
)
oogen_OOPostfixIncrementExpression_strategy = st.builds(
    oogen_OOPostfixIncrementExpression,
)
oogen_OOPlusExpression_strategy = st.builds(
    oogen_OOPlusExpression,
)
oogen_OOMinusExpression_strategy = st.builds(
    oogen_OOMinusExpression,
)
oogen_OOBracketedExpression_strategy = st.builds(
    oogen_OOBracketedExpression,
)
oogen_OOBitWiseComplement_strategy = st.builds(
    oogen_OOBitWiseComplement,
)
oogen_OOLessEqualsExpression_strategy = st.builds(
    oogen_OOLessEqualsExpression,
)
oogen_OOGreaterEqualsExpression_strategy = st.builds(
    oogen_OOGreaterEqualsExpression,
)
oogen_OONotEqualsExpression_strategy = st.builds(
    oogen_OONotEqualsExpression,
)
oogen_OOLessThanExpression_strategy = st.builds(
    oogen_OOLessThanExpression,
)
oogen_OOGreaterThanExpression_strategy = st.builds(
    oogen_OOGreaterThanExpression,
)
OOCompoundStatement_strategy = st.builds(
    OOCompoundStatement,
)
oogen_OODefault_strategy = st.builds(
    oogen_OODefault,
)
oogen_OOCase_strategy = st.builds(
    oogen_OOCase,
)
OOConditionalStatement_strategy = st.builds(
    OOConditionalStatement,
)
oogen_OOFor_strategy = st.builds(
    oogen_OOFor,
)
oogen_OOIf_strategy = st.builds(
    oogen_OOIf,
)
OOLogicalExpression_strategy = st.builds(
    OOLogicalExpression,
)
oogen_OOTernaryOperator_strategy = st.builds(
    oogen_OOTernaryOperator,
)
oogen_OOLogicalLiteral_strategy = st.builds(
    oogen_OOLogicalLiteral,
    value=
        st.booleans()
)
oogen_OOOneOperandLogicalExpression_strategy = st.builds(
    oogen_OOOneOperandLogicalExpression,
)
oogen_OOComparatorExpression_strategy = st.builds(
    oogen_OOComparatorExpression,
)
oogen_OOTwoOperandLogicalExpression_strategy = st.builds(
    oogen_OOTwoOperandLogicalExpression,
)
OOOneOperandLogicalExpression_strategy = st.builds(
    OOOneOperandLogicalExpression,
)
oogen_OONotExpression_strategy = st.builds(
    oogen_OONotExpression,
)
OOTwoOperandLogicalExpression_strategy = st.builds(
    OOTwoOperandLogicalExpression,
)
oogen_OOXorExpression_strategy = st.builds(
    oogen_OOXorExpression,
)
oogen_OOOrExpression_strategy = st.builds(
    oogen_OOOrExpression,
)
oogen_OOAndExpression_strategy = st.builds(
    oogen_OOAndExpression,
)
OOTwoOperandArithmeticExpression_strategy = st.builds(
    OOTwoOperandArithmeticExpression,
)
oogen_OOTwoOperandAssignableExpression_strategy = st.builds(
    oogen_OOTwoOperandAssignableExpression,
    assigned=
        st.booleans()
)
oogen_OORootExpression_strategy = st.builds(
    oogen_OORootExpression,
)
oogen_OOPowerExpression_strategy = st.builds(
    oogen_OOPowerExpression,
)
oogen_OODoWhile_strategy = st.builds(
    oogen_OODoWhile,
)
oogen_OOWhile_strategy = st.builds(
    oogen_OOWhile,
)
OOArithmeticExpression_strategy = st.builds(
    OOArithmeticExpression,
)
oogen_OOOneOperandArithmeticExpression_strategy = st.builds(
    oogen_OOOneOperandArithmeticExpression,
)
oogen_OOFloatLiteral_strategy = st.builds(
    oogen_OOFloatLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oogen_OODoubleLiteral_strategy = st.builds(
    oogen_OODoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oogen_OOLongLiteral_strategy = st.builds(
    oogen_OOLongLiteral,
    value=
        safe_text
)
oogen_OOIntegerLiteral_strategy = st.builds(
    oogen_OOIntegerLiteral,
    value=
        st.integers()
)
oogen_OOTwoOperandArithmeticExpression_strategy = st.builds(
    oogen_OOTwoOperandArithmeticExpression,
)
OOExpression_strategy = st.builds(
    OOExpression,
)
oogen_OONullLiteral_strategy = st.builds(
    oogen_OONullLiteral,
)
oogen_OOFieldReferenceExpression_strategy = st.builds(
    oogen_OOFieldReferenceExpression,
    fieldName=
        safe_text
)
oogen_OOBoolLiteral_strategy = st.builds(
    oogen_OOBoolLiteral,
    value=
        st.booleans()
)
oogen_OOIndexing_strategy = st.builds(
    oogen_OOIndexing,
)
oogen_OONewClass_strategy = st.builds(
    oogen_OONewClass,
    className=
        safe_text
)
oogen_OOLogicalExpression_strategy = st.builds(
    oogen_OOLogicalExpression,
)
oogen_OOTypeCast_strategy = st.builds(
    oogen_OOTypeCast,
)
oogen_OONewArray_strategy = st.builds(
    oogen_OONewArray,
)
oogen_OOEmptyExpression_strategy = st.builds(
    oogen_OOEmptyExpression,
)
oogen_OOAssignmentExpression_strategy = st.builds(
    oogen_OOAssignmentExpression,
)
oogen_OOVariableReferenceExpression_strategy = st.builds(
    oogen_OOVariableReferenceExpression,
)
oogen_OOThisLiteral_strategy = st.builds(
    oogen_OOThisLiteral,
)
oogen_OOLanguageSpecificExpression_strategy = st.builds(
    oogen_OOLanguageSpecificExpression,
)
oogen_OOFunctionCallExpression_strategy = st.builds(
    oogen_OOFunctionCallExpression,
    functionName=
        safe_text
)
oogen_OOStringLiteral_strategy = st.builds(
    oogen_OOStringLiteral,
    value=
        safe_text
)
oogen_OOInitializerList_strategy = st.builds(
    oogen_OOInitializerList,
)
oogen_OOArithmeticExpression_strategy = st.builds(
    oogen_OOArithmeticExpression,
)
oogen_OOModel_strategy = st.builds(
    oogen_OOModel,
)
OOTwoOperandAssignableExpression_strategy = st.builds(
    OOTwoOperandAssignableExpression,
)
oogen_OOBitwiseXorExpression_strategy = st.builds(
    oogen_OOBitwiseXorExpression,
)
oogen_OOBitwiseOrExpression_strategy = st.builds(
    oogen_OOBitwiseOrExpression,
)
oogen_OOBitWiseLeftShift_strategy = st.builds(
    oogen_OOBitWiseLeftShift,
)
oogen_OOBitwiseAndExpression_strategy = st.builds(
    oogen_OOBitwiseAndExpression,
)
oogen_OOMultiplicationExpression_strategy = st.builds(
    oogen_OOMultiplicationExpression,
)
oogen_OOBitWiseRightShift_strategy = st.builds(
    oogen_OOBitWiseRightShift,
)
oogen_OOSubtractionExpression_strategy = st.builds(
    oogen_OOSubtractionExpression,
)
oogen_OOIntegerDivisionExpression_strategy = st.builds(
    oogen_OOIntegerDivisionExpression,
)
oogen_OODivisionExpression_strategy = st.builds(
    oogen_OODivisionExpression,
)
oogen_OOModuloExpression_strategy = st.builds(
    oogen_OOModuloExpression,
)
oogen_OOAdditionExpression_strategy = st.builds(
    oogen_OOAdditionExpression,
)
oogen_OOType_strategy = st.builds(
    oogen_OOType,
    baseType=
        safe_text,
    collectionType=
        safe_text,
    numberOfIndirections=
        st.integers(),
    arrayDimensions=
        st.integers()
)
OOStatement_strategy = st.builds(
    OOStatement,
)
oogen_OOEmptyStatement_strategy = st.builds(
    oogen_OOEmptyStatement,
)
oogen_OOExpression_strategy = st.builds(
    oogen_OOExpression,
)
oogen_OOCompoundStatement_strategy = st.builds(
    oogen_OOCompoundStatement,
)
oogen_OOReturn_strategy = st.builds(
    oogen_OOReturn,
)
oogen_OOSwitch_strategy = st.builds(
    oogen_OOSwitch,
)
oogen_OOVariableDeclarationList_strategy = st.builds(
    oogen_OOVariableDeclarationList,
)
oogen_OOContinue_strategy = st.builds(
    oogen_OOContinue,
)
oogen_OOBreak_strategy = st.builds(
    oogen_OOBreak,
)
oogen_OOForEach_strategy = st.builds(
    oogen_OOForEach,
)
oogen_OOConditionalStatement_strategy = st.builds(
    oogen_OOConditionalStatement,
)
oogen_OOVariable_strategy = st.builds(
    oogen_OOVariable,
    name=
        safe_text,
    transient=
        st.booleans()
)
oogen_OOConstructor_strategy = st.builds(
    oogen_OOConstructor,
    className=
        safe_text,
    visibility=
        safe_text
)
OOCommentOwner_strategy = st.builds(
    OOCommentOwner,
)
oogen_OOStatement_strategy = st.builds(
    oogen_OOStatement,
)
oogen_OOMethod_strategy = st.builds(
    oogen_OOMethod,
    visibility=
        safe_text,
    languages=
        safe_text,
    name=
        safe_text,
    static=
        st.booleans()
)
OOVariable_strategy = st.builds(
    OOVariable,
)
oogen_OOMember_strategy = st.builds(
    oogen_OOMember,
    languages=
        safe_text,
    static=
        st.booleans(),
    visibility=
        safe_text
)
oogen_OOPackage_strategy = st.builds(
    oogen_OOPackage,
    name=
        safe_text
)
oogen_OOEnumeration_strategy = st.builds(
    oogen_OOEnumeration,
    options=
        safe_text,
    name=
        safe_text
)
oogen_OOClass_strategy = st.builds(
    oogen_OOClass,
    name=
        safe_text,
    keep=
        st.booleans(),
    languages=
        safe_text
)

@given(instance=oogen_OOCommentOwner_strategy)
@settings(max_examples=50)
def test_oogen_oocommentowner_instantiation(instance):
    assert isinstance(instance, oogen_OOCommentOwner)

@given(instance=oogen_OOComment_strategy)
@settings(max_examples=50)
def test_oogen_oocomment_instantiation(instance):
    assert isinstance(instance, oogen_OOComment)



@given(instance=oogen_OOComment_strategy)
def test_oogen_oocomment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=oogen_OOComment_strategy)
def test_oogen_oocomment_isBlockComment_setter(instance):
    original = instance.isBlockComment
    instance.isBlockComment = original
    assert instance.isBlockComment == original

@given(instance=OOComparatorExpression_strategy)
@settings(max_examples=50)
def test_oocomparatorexpression_instantiation(instance):
    assert isinstance(instance, OOComparatorExpression)

@given(instance=oogen_OOEqualsExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooequalsexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOEqualsExpression)

@given(instance=oogen_OOLanguageSpecificSnippet_strategy)
@settings(max_examples=50)
def test_oogen_oolanguagespecificsnippet_instantiation(instance):
    assert isinstance(instance, oogen_OOLanguageSpecificSnippet)



@given(instance=oogen_OOLanguageSpecificSnippet_strategy)
def test_oogen_oolanguagespecificsnippet_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=oogen_OOLanguageSpecificSnippet_strategy)
def test_oogen_oolanguagespecificsnippet_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=OOOneOperandArithmeticExpression_strategy)
@settings(max_examples=50)
def test_oooneoperandarithmeticexpression_instantiation(instance):
    assert isinstance(instance, OOOneOperandArithmeticExpression)

@given(instance=oogen_OOPostfixDecrementExpression_strategy)
@settings(max_examples=50)
def test_oogen_oopostfixdecrementexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPostfixDecrementExpression)

@given(instance=oogen_OOPrefixIncrementExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooprefixincrementexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPrefixIncrementExpression)

@given(instance=oogen_OOPrefixDecrementExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooprefixdecrementexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPrefixDecrementExpression)

@given(instance=oogen_OOPostfixIncrementExpression_strategy)
@settings(max_examples=50)
def test_oogen_oopostfixincrementexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPostfixIncrementExpression)

@given(instance=oogen_OOPlusExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooplusexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPlusExpression)

@given(instance=oogen_OOMinusExpression_strategy)
@settings(max_examples=50)
def test_oogen_oominusexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOMinusExpression)

@given(instance=oogen_OOBracketedExpression_strategy)
@settings(max_examples=50)
def test_oogen_oobracketedexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOBracketedExpression)

@given(instance=oogen_OOBitWiseComplement_strategy)
@settings(max_examples=50)
def test_oogen_oobitwisecomplement_instantiation(instance):
    assert isinstance(instance, oogen_OOBitWiseComplement)

@given(instance=oogen_OOLessEqualsExpression_strategy)
@settings(max_examples=50)
def test_oogen_oolessequalsexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOLessEqualsExpression)

@given(instance=oogen_OOGreaterEqualsExpression_strategy)
@settings(max_examples=50)
def test_oogen_oogreaterequalsexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOGreaterEqualsExpression)

@given(instance=oogen_OONotEqualsExpression_strategy)
@settings(max_examples=50)
def test_oogen_oonotequalsexpression_instantiation(instance):
    assert isinstance(instance, oogen_OONotEqualsExpression)

@given(instance=oogen_OOLessThanExpression_strategy)
@settings(max_examples=50)
def test_oogen_oolessthanexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOLessThanExpression)

@given(instance=oogen_OOGreaterThanExpression_strategy)
@settings(max_examples=50)
def test_oogen_oogreaterthanexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOGreaterThanExpression)

@given(instance=OOCompoundStatement_strategy)
@settings(max_examples=50)
def test_oocompoundstatement_instantiation(instance):
    assert isinstance(instance, OOCompoundStatement)

@given(instance=oogen_OODefault_strategy)
@settings(max_examples=50)
def test_oogen_oodefault_instantiation(instance):
    assert isinstance(instance, oogen_OODefault)

@given(instance=oogen_OOCase_strategy)
@settings(max_examples=50)
def test_oogen_oocase_instantiation(instance):
    assert isinstance(instance, oogen_OOCase)

@given(instance=OOConditionalStatement_strategy)
@settings(max_examples=50)
def test_ooconditionalstatement_instantiation(instance):
    assert isinstance(instance, OOConditionalStatement)

@given(instance=oogen_OOFor_strategy)
@settings(max_examples=50)
def test_oogen_oofor_instantiation(instance):
    assert isinstance(instance, oogen_OOFor)

@given(instance=oogen_OOIf_strategy)
@settings(max_examples=50)
def test_oogen_ooif_instantiation(instance):
    assert isinstance(instance, oogen_OOIf)

@given(instance=OOLogicalExpression_strategy)
@settings(max_examples=50)
def test_oologicalexpression_instantiation(instance):
    assert isinstance(instance, OOLogicalExpression)

@given(instance=oogen_OOTernaryOperator_strategy)
@settings(max_examples=50)
def test_oogen_ooternaryoperator_instantiation(instance):
    assert isinstance(instance, oogen_OOTernaryOperator)

@given(instance=oogen_OOLogicalLiteral_strategy)
@settings(max_examples=50)
def test_oogen_oologicalliteral_instantiation(instance):
    assert isinstance(instance, oogen_OOLogicalLiteral)



@given(instance=oogen_OOLogicalLiteral_strategy)
def test_oogen_oologicalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen_OOOneOperandLogicalExpression_strategy)
@settings(max_examples=50)
def test_oogen_oooneoperandlogicalexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOOneOperandLogicalExpression)

@given(instance=oogen_OOComparatorExpression_strategy)
@settings(max_examples=50)
def test_oogen_oocomparatorexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOComparatorExpression)

@given(instance=oogen_OOTwoOperandLogicalExpression_strategy)
@settings(max_examples=50)
def test_oogen_ootwooperandlogicalexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOTwoOperandLogicalExpression)

@given(instance=OOOneOperandLogicalExpression_strategy)
@settings(max_examples=50)
def test_oooneoperandlogicalexpression_instantiation(instance):
    assert isinstance(instance, OOOneOperandLogicalExpression)

@given(instance=oogen_OONotExpression_strategy)
@settings(max_examples=50)
def test_oogen_oonotexpression_instantiation(instance):
    assert isinstance(instance, oogen_OONotExpression)

@given(instance=OOTwoOperandLogicalExpression_strategy)
@settings(max_examples=50)
def test_ootwooperandlogicalexpression_instantiation(instance):
    assert isinstance(instance, OOTwoOperandLogicalExpression)

@given(instance=oogen_OOXorExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooxorexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOXorExpression)

@given(instance=oogen_OOOrExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooorexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOOrExpression)

@given(instance=oogen_OOAndExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooandexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOAndExpression)

@given(instance=OOTwoOperandArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ootwooperandarithmeticexpression_instantiation(instance):
    assert isinstance(instance, OOTwoOperandArithmeticExpression)

@given(instance=oogen_OOTwoOperandAssignableExpression_strategy)
@settings(max_examples=50)
def test_oogen_ootwooperandassignableexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOTwoOperandAssignableExpression)



@given(instance=oogen_OOTwoOperandAssignableExpression_strategy)
def test_oogen_ootwooperandassignableexpression_assigned_setter(instance):
    original = instance.assigned
    instance.assigned = original
    assert instance.assigned == original

@given(instance=oogen_OORootExpression_strategy)
@settings(max_examples=50)
def test_oogen_oorootexpression_instantiation(instance):
    assert isinstance(instance, oogen_OORootExpression)

@given(instance=oogen_OOPowerExpression_strategy)
@settings(max_examples=50)
def test_oogen_oopowerexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPowerExpression)

@given(instance=oogen_OODoWhile_strategy)
@settings(max_examples=50)
def test_oogen_oodowhile_instantiation(instance):
    assert isinstance(instance, oogen_OODoWhile)

@given(instance=oogen_OOWhile_strategy)
@settings(max_examples=50)
def test_oogen_oowhile_instantiation(instance):
    assert isinstance(instance, oogen_OOWhile)

@given(instance=OOArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ooarithmeticexpression_instantiation(instance):
    assert isinstance(instance, OOArithmeticExpression)

@given(instance=oogen_OOOneOperandArithmeticExpression_strategy)
@settings(max_examples=50)
def test_oogen_oooneoperandarithmeticexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOOneOperandArithmeticExpression)

@given(instance=oogen_OOFloatLiteral_strategy)
@settings(max_examples=50)
def test_oogen_oofloatliteral_instantiation(instance):
    assert isinstance(instance, oogen_OOFloatLiteral)



@given(instance=oogen_OOFloatLiteral_strategy)
def test_oogen_oofloatliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen_OODoubleLiteral_strategy)
@settings(max_examples=50)
def test_oogen_oodoubleliteral_instantiation(instance):
    assert isinstance(instance, oogen_OODoubleLiteral)



@given(instance=oogen_OODoubleLiteral_strategy)
def test_oogen_oodoubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen_OOLongLiteral_strategy)
@settings(max_examples=50)
def test_oogen_oolongliteral_instantiation(instance):
    assert isinstance(instance, oogen_OOLongLiteral)



@given(instance=oogen_OOLongLiteral_strategy)
def test_oogen_oolongliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen_OOIntegerLiteral_strategy)
@settings(max_examples=50)
def test_oogen_oointegerliteral_instantiation(instance):
    assert isinstance(instance, oogen_OOIntegerLiteral)



@given(instance=oogen_OOIntegerLiteral_strategy)
def test_oogen_oointegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen_OOTwoOperandArithmeticExpression_strategy)
@settings(max_examples=50)
def test_oogen_ootwooperandarithmeticexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOTwoOperandArithmeticExpression)

@given(instance=OOExpression_strategy)
@settings(max_examples=50)
def test_ooexpression_instantiation(instance):
    assert isinstance(instance, OOExpression)

@given(instance=oogen_OONullLiteral_strategy)
@settings(max_examples=50)
def test_oogen_oonullliteral_instantiation(instance):
    assert isinstance(instance, oogen_OONullLiteral)

@given(instance=oogen_OOFieldReferenceExpression_strategy)
@settings(max_examples=50)
def test_oogen_oofieldreferenceexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOFieldReferenceExpression)



@given(instance=oogen_OOFieldReferenceExpression_strategy)
def test_oogen_oofieldreferenceexpression_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=oogen_OOBoolLiteral_strategy)
@settings(max_examples=50)
def test_oogen_ooboolliteral_instantiation(instance):
    assert isinstance(instance, oogen_OOBoolLiteral)



@given(instance=oogen_OOBoolLiteral_strategy)
def test_oogen_ooboolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen_OOIndexing_strategy)
@settings(max_examples=50)
def test_oogen_ooindexing_instantiation(instance):
    assert isinstance(instance, oogen_OOIndexing)

@given(instance=oogen_OONewClass_strategy)
@settings(max_examples=50)
def test_oogen_oonewclass_instantiation(instance):
    assert isinstance(instance, oogen_OONewClass)



@given(instance=oogen_OONewClass_strategy)
def test_oogen_oonewclass_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=oogen_OOLogicalExpression_strategy)
@settings(max_examples=50)
def test_oogen_oologicalexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOLogicalExpression)

@given(instance=oogen_OOTypeCast_strategy)
@settings(max_examples=50)
def test_oogen_ootypecast_instantiation(instance):
    assert isinstance(instance, oogen_OOTypeCast)

@given(instance=oogen_OONewArray_strategy)
@settings(max_examples=50)
def test_oogen_oonewarray_instantiation(instance):
    assert isinstance(instance, oogen_OONewArray)

@given(instance=oogen_OOEmptyExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooemptyexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOEmptyExpression)

@given(instance=oogen_OOAssignmentExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooassignmentexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOAssignmentExpression)

@given(instance=oogen_OOVariableReferenceExpression_strategy)
@settings(max_examples=50)
def test_oogen_oovariablereferenceexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOVariableReferenceExpression)

@given(instance=oogen_OOThisLiteral_strategy)
@settings(max_examples=50)
def test_oogen_oothisliteral_instantiation(instance):
    assert isinstance(instance, oogen_OOThisLiteral)

@given(instance=oogen_OOLanguageSpecificExpression_strategy)
@settings(max_examples=50)
def test_oogen_oolanguagespecificexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOLanguageSpecificExpression)

@given(instance=oogen_OOFunctionCallExpression_strategy)
@settings(max_examples=50)
def test_oogen_oofunctioncallexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOFunctionCallExpression)



@given(instance=oogen_OOFunctionCallExpression_strategy)
def test_oogen_oofunctioncallexpression_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=oogen_OOStringLiteral_strategy)
@settings(max_examples=50)
def test_oogen_oostringliteral_instantiation(instance):
    assert isinstance(instance, oogen_OOStringLiteral)



@given(instance=oogen_OOStringLiteral_strategy)
def test_oogen_oostringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oogen_OOInitializerList_strategy)
@settings(max_examples=50)
def test_oogen_ooinitializerlist_instantiation(instance):
    assert isinstance(instance, oogen_OOInitializerList)

@given(instance=oogen_OOArithmeticExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooarithmeticexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOArithmeticExpression)

@given(instance=oogen_OOModel_strategy)
@settings(max_examples=50)
def test_oogen_oomodel_instantiation(instance):
    assert isinstance(instance, oogen_OOModel)

@given(instance=OOTwoOperandAssignableExpression_strategy)
@settings(max_examples=50)
def test_ootwooperandassignableexpression_instantiation(instance):
    assert isinstance(instance, OOTwoOperandAssignableExpression)

@given(instance=oogen_OOBitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_oogen_oobitwisexorexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOBitwiseXorExpression)

@given(instance=oogen_OOBitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_oogen_oobitwiseorexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOBitwiseOrExpression)

@given(instance=oogen_OOBitWiseLeftShift_strategy)
@settings(max_examples=50)
def test_oogen_oobitwiseleftshift_instantiation(instance):
    assert isinstance(instance, oogen_OOBitWiseLeftShift)

@given(instance=oogen_OOBitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_oogen_oobitwiseandexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOBitwiseAndExpression)

@given(instance=oogen_OOMultiplicationExpression_strategy)
@settings(max_examples=50)
def test_oogen_oomultiplicationexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOMultiplicationExpression)

@given(instance=oogen_OOBitWiseRightShift_strategy)
@settings(max_examples=50)
def test_oogen_oobitwiserightshift_instantiation(instance):
    assert isinstance(instance, oogen_OOBitWiseRightShift)

@given(instance=oogen_OOSubtractionExpression_strategy)
@settings(max_examples=50)
def test_oogen_oosubtractionexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOSubtractionExpression)

@given(instance=oogen_OOIntegerDivisionExpression_strategy)
@settings(max_examples=50)
def test_oogen_oointegerdivisionexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOIntegerDivisionExpression)

@given(instance=oogen_OODivisionExpression_strategy)
@settings(max_examples=50)
def test_oogen_oodivisionexpression_instantiation(instance):
    assert isinstance(instance, oogen_OODivisionExpression)

@given(instance=oogen_OOModuloExpression_strategy)
@settings(max_examples=50)
def test_oogen_oomoduloexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOModuloExpression)

@given(instance=oogen_OOAdditionExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooadditionexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOAdditionExpression)

@given(instance=oogen_OOType_strategy)
@settings(max_examples=50)
def test_oogen_ootype_instantiation(instance):
    assert isinstance(instance, oogen_OOType)



@given(instance=oogen_OOType_strategy)
def test_oogen_ootype_baseType_setter(instance):
    original = instance.baseType
    instance.baseType = original
    assert instance.baseType == original



@given(instance=oogen_OOType_strategy)
def test_oogen_ootype_collectionType_setter(instance):
    original = instance.collectionType
    instance.collectionType = original
    assert instance.collectionType == original



@given(instance=oogen_OOType_strategy)
def test_oogen_ootype_numberOfIndirections_setter(instance):
    original = instance.numberOfIndirections
    instance.numberOfIndirections = original
    assert instance.numberOfIndirections == original



@given(instance=oogen_OOType_strategy)
def test_oogen_ootype_arrayDimensions_setter(instance):
    original = instance.arrayDimensions
    instance.arrayDimensions = original
    assert instance.arrayDimensions == original

@given(instance=OOStatement_strategy)
@settings(max_examples=50)
def test_oostatement_instantiation(instance):
    assert isinstance(instance, OOStatement)

@given(instance=oogen_OOEmptyStatement_strategy)
@settings(max_examples=50)
def test_oogen_ooemptystatement_instantiation(instance):
    assert isinstance(instance, oogen_OOEmptyStatement)

@given(instance=oogen_OOExpression_strategy)
@settings(max_examples=50)
def test_oogen_ooexpression_instantiation(instance):
    assert isinstance(instance, oogen_OOExpression)

@given(instance=oogen_OOCompoundStatement_strategy)
@settings(max_examples=50)
def test_oogen_oocompoundstatement_instantiation(instance):
    assert isinstance(instance, oogen_OOCompoundStatement)

@given(instance=oogen_OOReturn_strategy)
@settings(max_examples=50)
def test_oogen_ooreturn_instantiation(instance):
    assert isinstance(instance, oogen_OOReturn)

@given(instance=oogen_OOSwitch_strategy)
@settings(max_examples=50)
def test_oogen_ooswitch_instantiation(instance):
    assert isinstance(instance, oogen_OOSwitch)

@given(instance=oogen_OOVariableDeclarationList_strategy)
@settings(max_examples=50)
def test_oogen_oovariabledeclarationlist_instantiation(instance):
    assert isinstance(instance, oogen_OOVariableDeclarationList)

@given(instance=oogen_OOContinue_strategy)
@settings(max_examples=50)
def test_oogen_oocontinue_instantiation(instance):
    assert isinstance(instance, oogen_OOContinue)

@given(instance=oogen_OOBreak_strategy)
@settings(max_examples=50)
def test_oogen_oobreak_instantiation(instance):
    assert isinstance(instance, oogen_OOBreak)

@given(instance=oogen_OOForEach_strategy)
@settings(max_examples=50)
def test_oogen_ooforeach_instantiation(instance):
    assert isinstance(instance, oogen_OOForEach)

@given(instance=oogen_OOConditionalStatement_strategy)
@settings(max_examples=50)
def test_oogen_ooconditionalstatement_instantiation(instance):
    assert isinstance(instance, oogen_OOConditionalStatement)

@given(instance=oogen_OOVariable_strategy)
@settings(max_examples=50)
def test_oogen_oovariable_instantiation(instance):
    assert isinstance(instance, oogen_OOVariable)



@given(instance=oogen_OOVariable_strategy)
def test_oogen_oovariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oogen_OOVariable_strategy)
def test_oogen_oovariable_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=oogen_OOConstructor_strategy)
@settings(max_examples=50)
def test_oogen_ooconstructor_instantiation(instance):
    assert isinstance(instance, oogen_OOConstructor)



@given(instance=oogen_OOConstructor_strategy)
def test_oogen_ooconstructor_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=oogen_OOConstructor_strategy)
def test_oogen_ooconstructor_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=OOCommentOwner_strategy)
@settings(max_examples=50)
def test_oocommentowner_instantiation(instance):
    assert isinstance(instance, OOCommentOwner)

@given(instance=oogen_OOStatement_strategy)
@settings(max_examples=50)
def test_oogen_oostatement_instantiation(instance):
    assert isinstance(instance, oogen_OOStatement)

@given(instance=oogen_OOMethod_strategy)
@settings(max_examples=50)
def test_oogen_oomethod_instantiation(instance):
    assert isinstance(instance, oogen_OOMethod)



@given(instance=oogen_OOMethod_strategy)
def test_oogen_oomethod_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=oogen_OOMethod_strategy)
def test_oogen_oomethod_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original



@given(instance=oogen_OOMethod_strategy)
def test_oogen_oomethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oogen_OOMethod_strategy)
def test_oogen_oomethod_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=OOVariable_strategy)
@settings(max_examples=50)
def test_oovariable_instantiation(instance):
    assert isinstance(instance, OOVariable)

@given(instance=oogen_OOMember_strategy)
@settings(max_examples=50)
def test_oogen_oomember_instantiation(instance):
    assert isinstance(instance, oogen_OOMember)



@given(instance=oogen_OOMember_strategy)
def test_oogen_oomember_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original



@given(instance=oogen_OOMember_strategy)
def test_oogen_oomember_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=oogen_OOMember_strategy)
def test_oogen_oomember_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=oogen_OOPackage_strategy)
@settings(max_examples=50)
def test_oogen_oopackage_instantiation(instance):
    assert isinstance(instance, oogen_OOPackage)



@given(instance=oogen_OOPackage_strategy)
def test_oogen_oopackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oogen_OOEnumeration_strategy)
@settings(max_examples=50)
def test_oogen_ooenumeration_instantiation(instance):
    assert isinstance(instance, oogen_OOEnumeration)



@given(instance=oogen_OOEnumeration_strategy)
def test_oogen_ooenumeration_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original



@given(instance=oogen_OOEnumeration_strategy)
def test_oogen_ooenumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oogen_OOClass_strategy)
@settings(max_examples=50)
def test_oogen_ooclass_instantiation(instance):
    assert isinstance(instance, oogen_OOClass)



@given(instance=oogen_OOClass_strategy)
def test_oogen_ooclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oogen_OOClass_strategy)
def test_oogen_ooclass_keep_setter(instance):
    original = instance.keep
    instance.keep = original
    assert instance.keep == original



@given(instance=oogen_OOClass_strategy)
def test_oogen_ooclass_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original
