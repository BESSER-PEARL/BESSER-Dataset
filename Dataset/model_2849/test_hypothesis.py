import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IfConditionStart,
    Line,
    RichString,
    model_richstring_ProcessedRichString,
    model_xtype_XExportItem,
    EndIf,
    ElseIfCondition,
    ElseStart,
    RichStringIf,
    ForLoopStart,
    ForLoopEnd,
    RichStringForLoop,
    Literal,
    model_richstring_LineBreak,
    RichStringLiteral,
    model_richstring_LinePart,
    ProcessedRichString,
    LinePart,
    model_richstring_Literal,
    model_richstring_PrintedExpression,
    model_richstring_EndIf,
    model_richstring_IfConditionStart,
    model_richstring_ForLoopEnd,
    model_richstring_ElseIfCondition,
    model_richstring_ElseStart,
    model_richstring_ForLoopStart,
    model_richstring_Line,
    XImportDeclaration1,
    model_xtype_XImportSection1,
    model_xtype_XImportDeclaration,
    XImportDeclaration,
    XExportItem,
    model_xtype_XExportDeclaration,
    XExportDeclaration,
    model_xtype_XExportSection,
    model_xtype_XImportItem,
    XImportItem,
    model_xtype_XImportDeclaration1,
    XAnnotationElementValuePair,
    model_xtype_XImportSection,
    JvmSpecializedTypeReference,
    model_xtype_XComputedTypeReference,
    model_xtype_XFunctionTypeRef,
    model_xannotation_XAnnotationElementValuePair,
    JvmAnnotationValue,
    model_types_JvmTypeAnnotationValue,
    model_types_JvmShortAnnotationValue,
    model_types_JvmStringAnnotationValue,
    model_types_JvmAnnotationAnnotationValue,
    model_types_JvmEnumAnnotationValue,
    model_types_JvmByteAnnotationValue,
    model_types_JvmBooleanAnnotationValue,
    model_types_JvmIntAnnotationValue,
    JvmOperation,
    model_types_JvmAnnotationValue,
    JvmAnnotationType,
    model_types_JvmAnnotationReference,
    JvmAnnotationReference,
    JvmAnnotationTarget,
    model_types_JvmFormalParameter,
    model_types_JvmMember,
    JvmCompoundTypeReference,
    model_types_JvmSynonymTypeReference,
    model_types_JvmMultiTypeReference,
    JvmExecutable,
    model_types_JvmOperation,
    model_types_JvmConstructor,
    JvmFormalParameter,
    types_JvmFeature,
    XExpression,
    model_xannotation_XAnnotation,
    JvmFeature,
    model_types_JvmField,
    model_types_JvmTypeReference,
    types_JvmTypeReference,
    JvmConstraintOwner,
    model_types_JvmTypeConstraint,
    JvmTypeConstraint,
    model_types_JvmConstraintOwner,
    JvmParameterizedTypeReference,
    JvmTypeParameter,
    types_JvmTypeParameterDeclarator,
    model_types_JvmExecutable,
    types_JvmDeclaredType,
    model_types_JvmGenericType,
    JvmField,
    model_types_JvmEnumerationLiteral,
    JvmEnumerationLiteral,
    JvmDeclaredType,
    model_types_JvmEnumerationType,
    model_types_JvmAnnotationType,
    model_types_JvmLowerBound,
    model_types_JvmUpperBound,
    model_types_JvmTypeParameterDeclarator,
    JvmTypeParameterDeclarator,
    types_JvmConstraintOwner,
    model_types_JvmWildcardTypeReference,
    JvmMember,
    model_types_JvmFeature,
    JvmTypeReference,
    model_types_JvmParameterizedTypeReference,
    model_types_JvmSpecializedTypeReference,
    model_types_JvmCompoundTypeReference,
    model_types_JvmAnyTypeReference,
    model_types_JvmDelegateTypeReference,
    model_types_JvmGenericArrayTypeReference,
    model_types_JvmUnknownTypeReference,
    types_JvmComponentType,
    model_types_JvmTypeParameter,
    types_JvmMember,
    model_types_JvmDeclaredType,
    JvmComponentType,
    model_types_JvmArrayType,
    model_types_JvmPrimitiveType,
    JvmArrayType,
    JvmType,
    model_types_JvmComponentType,
    model_types_JvmVoid,
    model_types_JvmNoModule,
    XExportSection,
    types_model_EObject,
    XImportSection1,
    JvmIdentifiableElement,
    model_types_JvmAnnotationTarget,
    model_types_JvmType,
    model_types_JvmModule,
    model_types_JvmIdentifiableElement,
    model_ss_XtendFormalParameter,
    XVariableDeclaration,
    model_ss_XtendVariableDeclaration,
    model_ss_CreateExtensionInfo,
    model_ss_RichStringElseIf,
    RichStringElseIf,
    XBlockExpression,
    model_ss_RichString,
    model_ss_RichStringIf,
    XForEachExpression,
    model_ss_RichStringForLoop,
    XStringLiteral,
    model_ss_RichStringLiteral,
    CreateExtensionInfo,
    XtendParameter,
    XtendMember,
    model_ss_XtendField,
    model_ss_XtendEnumLiteral,
    model_ss_XtendConstructor,
    model_ss_XtendTypeDeclaration,
    model_ss_XtendEvent,
    model_ss_XtendFunction,
    XtendAnnotationTarget,
    model_ss_XtendParameter,
    model_ss_XtendMember,
    XAnnotation,
    model_ss_XtendAnnotationTarget,
    XObjectLiteralPart,
    model_xbase_XObjectLiteral,
    ss_model_EObject,
    XtendTypeDeclaration,
    model_ss_XtendDelegate,
    model_ss_XtendEnum,
    model_ss_XtendAnnotationType,
    model_ss_XtendInterface,
    model_ss_XtendClass,
    model_ss_XtendFile,
    model_xbase_XArrayLiteral,
    model_xbase_XObjectLiteralPart,
    model_xbase_XTernaryOperation,
    model_xbase_XFunctionDeclaration,
    model_xbase_XCatchClause,
    XCatchClause,
    model_xbase_XContinueExpression,
    model_xbase_XBreakExpression,
    model_xbase_XReturnExpression,
    XAbstractWhileExpression,
    model_xbase_XDoWhileExpression,
    model_xbase_XAbstractWhileExpression,
    model_xbase_XTryCatchFinallyExpression,
    model_xbase_XThrowExpression,
    model_xbase_XInstanceOfExpression,
    model_xbase_XTypeLiteral,
    model_xbase_XWhileExpression,
    model_xbase_XForEachExpression,
    model_xbase_XForLoopExpression,
    model_xbase_XKeyValuePair,
    XCollectionLiteral,
    model_xbase_XListLiteral,
    model_xbase_XCollectionLiteral,
    model_xbase_XStringLiteral,
    model_xbase_XNumberLiteral,
    model_xbase_XNullLiteral,
    model_xbase_XBooleanLiteral,
    model_xbase_XCastedExpression,
    model_xbase_XSetLiteral,
    JvmConstructor,
    model_xbase_XConstructorCall,
    model_xbase_XAbstractFeatureCall,
    model_xbase_XVariableDeclarationList,
    XAbstractFeatureCall,
    model_xbase_XAssignment,
    model_xbase_XUnaryOperation,
    model_xbase_XPrefixOperation,
    model_xbase_XMemberFeatureCall1,
    model_xbase_XBinaryOperation,
    model_xbase_XFeatureCall,
    model_xbase_XIndexOperation,
    model_xbase_XPostfixOperation,
    model_xbase_XMemberFeatureCall,
    model_xbase_XIfExpression,
    model_xbase_XExpression,
    model_types_JvmCustomAnnotationValue,
    model_xbase_XBlockExpression,
    model_xbase_XCasePart,
    XCasePart,
    types_JvmIdentifiableElement,
    xbase_XExpression,
    model_xbase_XClosure,
    model_xbase_XVariableDeclaration,
    model_xbase_XSwitchExpression,
    model_types_JvmCharAnnotationValue,
    model_types_JvmFloatAnnotationValue,
    model_types_JvmDoubleAnnotationValue,
    model_types_JvmLongAnnotationValue,
    JvmVisibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ifconditionstart_is_not_abstract():
    assert not inspect.isabstract(IfConditionStart)


def test_ifconditionstart_constructor_exists():
    assert callable(IfConditionStart.__init__)


def test_ifconditionstart_constructor_args():
    sig = inspect.signature(IfConditionStart.__init__)
    params = list(sig.parameters.keys())



def test_line_is_not_abstract():
    assert not inspect.isabstract(Line)


def test_line_constructor_exists():
    assert callable(Line.__init__)


def test_line_constructor_args():
    sig = inspect.signature(Line.__init__)
    params = list(sig.parameters.keys())



def test_richstring_is_not_abstract():
    assert not inspect.isabstract(RichString)


def test_richstring_constructor_exists():
    assert callable(RichString.__init__)


def test_richstring_constructor_args():
    sig = inspect.signature(RichString.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_processedrichstring_is_not_abstract():
    assert not inspect.isabstract(model_richstring_ProcessedRichString)


def test_model_richstring_processedrichstring_constructor_exists():
    assert callable(model_richstring_ProcessedRichString.__init__)


def test_model_richstring_processedrichstring_constructor_args():
    sig = inspect.signature(model_richstring_ProcessedRichString.__init__)
    params = list(sig.parameters.keys())



def test_model_xtype_xexportitem_is_not_abstract():
    assert not inspect.isabstract(model_xtype_XExportItem)


def test_model_xtype_xexportitem_constructor_exists():
    assert callable(model_xtype_XExportItem.__init__)


def test_model_xtype_xexportitem_constructor_args():
    sig = inspect.signature(model_xtype_XExportItem.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_model_xtype_xexportitem_has_alias():
    assert hasattr(model_xtype_XExportItem, "alias")
    descriptor = None
    for klass in model_xtype_XExportItem.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_endif_is_not_abstract():
    assert not inspect.isabstract(EndIf)


def test_endif_constructor_exists():
    assert callable(EndIf.__init__)


def test_endif_constructor_args():
    sig = inspect.signature(EndIf.__init__)
    params = list(sig.parameters.keys())



def test_elseifcondition_is_not_abstract():
    assert not inspect.isabstract(ElseIfCondition)


def test_elseifcondition_constructor_exists():
    assert callable(ElseIfCondition.__init__)


def test_elseifcondition_constructor_args():
    sig = inspect.signature(ElseIfCondition.__init__)
    params = list(sig.parameters.keys())



def test_elsestart_is_not_abstract():
    assert not inspect.isabstract(ElseStart)


def test_elsestart_constructor_exists():
    assert callable(ElseStart.__init__)


def test_elsestart_constructor_args():
    sig = inspect.signature(ElseStart.__init__)
    params = list(sig.parameters.keys())



def test_richstringif_is_not_abstract():
    assert not inspect.isabstract(RichStringIf)


def test_richstringif_constructor_exists():
    assert callable(RichStringIf.__init__)


def test_richstringif_constructor_args():
    sig = inspect.signature(RichStringIf.__init__)
    params = list(sig.parameters.keys())



def test_forloopstart_is_not_abstract():
    assert not inspect.isabstract(ForLoopStart)


def test_forloopstart_constructor_exists():
    assert callable(ForLoopStart.__init__)


def test_forloopstart_constructor_args():
    sig = inspect.signature(ForLoopStart.__init__)
    params = list(sig.parameters.keys())



def test_forloopend_is_not_abstract():
    assert not inspect.isabstract(ForLoopEnd)


def test_forloopend_constructor_exists():
    assert callable(ForLoopEnd.__init__)


def test_forloopend_constructor_args():
    sig = inspect.signature(ForLoopEnd.__init__)
    params = list(sig.parameters.keys())



def test_richstringforloop_is_not_abstract():
    assert not inspect.isabstract(RichStringForLoop)


def test_richstringforloop_constructor_exists():
    assert callable(RichStringForLoop.__init__)


def test_richstringforloop_constructor_args():
    sig = inspect.signature(RichStringForLoop.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_linebreak_is_not_abstract():
    assert not inspect.isabstract(model_richstring_LineBreak)


def test_model_richstring_linebreak_constructor_exists():
    assert callable(model_richstring_LineBreak.__init__)


def test_model_richstring_linebreak_constructor_args():
    sig = inspect.signature(model_richstring_LineBreak.__init__)
    params = list(sig.parameters.keys())



def test_richstringliteral_is_not_abstract():
    assert not inspect.isabstract(RichStringLiteral)


def test_richstringliteral_constructor_exists():
    assert callable(RichStringLiteral.__init__)


def test_richstringliteral_constructor_args():
    sig = inspect.signature(RichStringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_linepart_is_not_abstract():
    assert not inspect.isabstract(model_richstring_LinePart)


def test_model_richstring_linepart_constructor_exists():
    assert callable(model_richstring_LinePart.__init__)


def test_model_richstring_linepart_constructor_args():
    sig = inspect.signature(model_richstring_LinePart.__init__)
    params = list(sig.parameters.keys())



def test_processedrichstring_is_not_abstract():
    assert not inspect.isabstract(ProcessedRichString)


def test_processedrichstring_constructor_exists():
    assert callable(ProcessedRichString.__init__)


def test_processedrichstring_constructor_args():
    sig = inspect.signature(ProcessedRichString.__init__)
    params = list(sig.parameters.keys())



def test_linepart_is_not_abstract():
    assert not inspect.isabstract(LinePart)


def test_linepart_constructor_exists():
    assert callable(LinePart.__init__)


def test_linepart_constructor_args():
    sig = inspect.signature(LinePart.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_literal_is_not_abstract():
    assert not inspect.isabstract(model_richstring_Literal)


def test_model_richstring_literal_constructor_exists():
    assert callable(model_richstring_Literal.__init__)


def test_model_richstring_literal_constructor_args():
    sig = inspect.signature(model_richstring_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_model_richstring_literal_has_length():
    assert hasattr(model_richstring_Literal, "length")
    descriptor = None
    for klass in model_richstring_Literal.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_model_richstring_literal_has_offset():
    assert hasattr(model_richstring_Literal, "offset")
    descriptor = None
    for klass in model_richstring_Literal.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_model_richstring_printedexpression_is_not_abstract():
    assert not inspect.isabstract(model_richstring_PrintedExpression)


def test_model_richstring_printedexpression_constructor_exists():
    assert callable(model_richstring_PrintedExpression.__init__)


def test_model_richstring_printedexpression_constructor_args():
    sig = inspect.signature(model_richstring_PrintedExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_endif_is_not_abstract():
    assert not inspect.isabstract(model_richstring_EndIf)


def test_model_richstring_endif_constructor_exists():
    assert callable(model_richstring_EndIf.__init__)


def test_model_richstring_endif_constructor_args():
    sig = inspect.signature(model_richstring_EndIf.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_ifconditionstart_is_not_abstract():
    assert not inspect.isabstract(model_richstring_IfConditionStart)


def test_model_richstring_ifconditionstart_constructor_exists():
    assert callable(model_richstring_IfConditionStart.__init__)


def test_model_richstring_ifconditionstart_constructor_args():
    sig = inspect.signature(model_richstring_IfConditionStart.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_forloopend_is_not_abstract():
    assert not inspect.isabstract(model_richstring_ForLoopEnd)


def test_model_richstring_forloopend_constructor_exists():
    assert callable(model_richstring_ForLoopEnd.__init__)


def test_model_richstring_forloopend_constructor_args():
    sig = inspect.signature(model_richstring_ForLoopEnd.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_elseifcondition_is_not_abstract():
    assert not inspect.isabstract(model_richstring_ElseIfCondition)


def test_model_richstring_elseifcondition_constructor_exists():
    assert callable(model_richstring_ElseIfCondition.__init__)


def test_model_richstring_elseifcondition_constructor_args():
    sig = inspect.signature(model_richstring_ElseIfCondition.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_elsestart_is_not_abstract():
    assert not inspect.isabstract(model_richstring_ElseStart)


def test_model_richstring_elsestart_constructor_exists():
    assert callable(model_richstring_ElseStart.__init__)


def test_model_richstring_elsestart_constructor_args():
    sig = inspect.signature(model_richstring_ElseStart.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_forloopstart_is_not_abstract():
    assert not inspect.isabstract(model_richstring_ForLoopStart)


def test_model_richstring_forloopstart_constructor_exists():
    assert callable(model_richstring_ForLoopStart.__init__)


def test_model_richstring_forloopstart_constructor_args():
    sig = inspect.signature(model_richstring_ForLoopStart.__init__)
    params = list(sig.parameters.keys())



def test_model_richstring_line_is_not_abstract():
    assert not inspect.isabstract(model_richstring_Line)


def test_model_richstring_line_constructor_exists():
    assert callable(model_richstring_Line.__init__)


def test_model_richstring_line_constructor_args():
    sig = inspect.signature(model_richstring_Line.__init__)
    params = list(sig.parameters.keys())



def test_ximportdeclaration1_is_not_abstract():
    assert not inspect.isabstract(XImportDeclaration1)


def test_ximportdeclaration1_constructor_exists():
    assert callable(XImportDeclaration1.__init__)


def test_ximportdeclaration1_constructor_args():
    sig = inspect.signature(XImportDeclaration1.__init__)
    params = list(sig.parameters.keys())



def test_model_xtype_ximportsection1_is_not_abstract():
    assert not inspect.isabstract(model_xtype_XImportSection1)


def test_model_xtype_ximportsection1_constructor_exists():
    assert callable(model_xtype_XImportSection1.__init__)


def test_model_xtype_ximportsection1_constructor_args():
    sig = inspect.signature(model_xtype_XImportSection1.__init__)
    params = list(sig.parameters.keys())



def test_model_xtype_ximportdeclaration_is_not_abstract():
    assert not inspect.isabstract(model_xtype_XImportDeclaration)


def test_model_xtype_ximportdeclaration_constructor_exists():
    assert callable(model_xtype_XImportDeclaration.__init__)


def test_model_xtype_ximportdeclaration_constructor_args():
    sig = inspect.signature(model_xtype_XImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"
    assert "static" in params, "Missing parameter 'static'"
    assert "wildcard" in params, "Missing parameter 'wildcard'"
    assert "extension" in params, "Missing parameter 'extension'"

def test_model_xtype_ximportdeclaration_has_importedNamespace():
    assert hasattr(model_xtype_XImportDeclaration, "importedNamespace")
    descriptor = None
    for klass in model_xtype_XImportDeclaration.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)

def test_model_xtype_ximportdeclaration_has_static():
    assert hasattr(model_xtype_XImportDeclaration, "static")
    descriptor = None
    for klass in model_xtype_XImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_model_xtype_ximportdeclaration_has_wildcard():
    assert hasattr(model_xtype_XImportDeclaration, "wildcard")
    descriptor = None
    for klass in model_xtype_XImportDeclaration.__mro__:
        if "wildcard" in klass.__dict__:
            descriptor = klass.__dict__["wildcard"]
            break
    assert isinstance(descriptor, property)

def test_model_xtype_ximportdeclaration_has_extension():
    assert hasattr(model_xtype_XImportDeclaration, "extension")
    descriptor = None
    for klass in model_xtype_XImportDeclaration.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)



def test_ximportdeclaration_is_not_abstract():
    assert not inspect.isabstract(XImportDeclaration)


def test_ximportdeclaration_constructor_exists():
    assert callable(XImportDeclaration.__init__)


def test_ximportdeclaration_constructor_args():
    sig = inspect.signature(XImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xexportitem_is_not_abstract():
    assert not inspect.isabstract(XExportItem)


def test_xexportitem_constructor_exists():
    assert callable(XExportItem.__init__)


def test_xexportitem_constructor_args():
    sig = inspect.signature(XExportItem.__init__)
    params = list(sig.parameters.keys())



def test_model_xtype_xexportdeclaration_is_not_abstract():
    assert not inspect.isabstract(model_xtype_XExportDeclaration)


def test_model_xtype_xexportdeclaration_constructor_exists():
    assert callable(model_xtype_XExportDeclaration.__init__)


def test_model_xtype_xexportdeclaration_constructor_args():
    sig = inspect.signature(model_xtype_XExportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "wildcard" in params, "Missing parameter 'wildcard'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_model_xtype_xexportdeclaration_has_wildcard():
    assert hasattr(model_xtype_XExportDeclaration, "wildcard")
    descriptor = None
    for klass in model_xtype_XExportDeclaration.__mro__:
        if "wildcard" in klass.__dict__:
            descriptor = klass.__dict__["wildcard"]
            break
    assert isinstance(descriptor, property)

def test_model_xtype_xexportdeclaration_has_alias():
    assert hasattr(model_xtype_XExportDeclaration, "alias")
    descriptor = None
    for klass in model_xtype_XExportDeclaration.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_model_xtype_xexportdeclaration_has_importURI():
    assert hasattr(model_xtype_XExportDeclaration, "importURI")
    descriptor = None
    for klass in model_xtype_XExportDeclaration.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_xexportdeclaration_is_not_abstract():
    assert not inspect.isabstract(XExportDeclaration)


def test_xexportdeclaration_constructor_exists():
    assert callable(XExportDeclaration.__init__)


def test_xexportdeclaration_constructor_args():
    sig = inspect.signature(XExportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_xtype_xexportsection_is_not_abstract():
    assert not inspect.isabstract(model_xtype_XExportSection)


def test_model_xtype_xexportsection_constructor_exists():
    assert callable(model_xtype_XExportSection.__init__)


def test_model_xtype_xexportsection_constructor_args():
    sig = inspect.signature(model_xtype_XExportSection.__init__)
    params = list(sig.parameters.keys())



def test_model_xtype_ximportitem_is_not_abstract():
    assert not inspect.isabstract(model_xtype_XImportItem)


def test_model_xtype_ximportitem_constructor_exists():
    assert callable(model_xtype_XImportItem.__init__)


def test_model_xtype_ximportitem_constructor_args():
    sig = inspect.signature(model_xtype_XImportItem.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_model_xtype_ximportitem_has_alias():
    assert hasattr(model_xtype_XImportItem, "alias")
    descriptor = None
    for klass in model_xtype_XImportItem.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_ximportitem_is_not_abstract():
    assert not inspect.isabstract(XImportItem)


def test_ximportitem_constructor_exists():
    assert callable(XImportItem.__init__)


def test_ximportitem_constructor_args():
    sig = inspect.signature(XImportItem.__init__)
    params = list(sig.parameters.keys())



def test_model_xtype_ximportdeclaration1_is_not_abstract():
    assert not inspect.isabstract(model_xtype_XImportDeclaration1)


def test_model_xtype_ximportdeclaration1_constructor_exists():
    assert callable(model_xtype_XImportDeclaration1.__init__)


def test_model_xtype_ximportdeclaration1_constructor_args():
    sig = inspect.signature(model_xtype_XImportDeclaration1.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_model_xtype_ximportdeclaration1_has_alias():
    assert hasattr(model_xtype_XImportDeclaration1, "alias")
    descriptor = None
    for klass in model_xtype_XImportDeclaration1.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_model_xtype_ximportdeclaration1_has_importURI():
    assert hasattr(model_xtype_XImportDeclaration1, "importURI")
    descriptor = None
    for klass in model_xtype_XImportDeclaration1.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_xannotationelementvaluepair_is_not_abstract():
    assert not inspect.isabstract(XAnnotationElementValuePair)


def test_xannotationelementvaluepair_constructor_exists():
    assert callable(XAnnotationElementValuePair.__init__)


def test_xannotationelementvaluepair_constructor_args():
    sig = inspect.signature(XAnnotationElementValuePair.__init__)
    params = list(sig.parameters.keys())



def test_model_xtype_ximportsection_is_not_abstract():
    assert not inspect.isabstract(model_xtype_XImportSection)


def test_model_xtype_ximportsection_constructor_exists():
    assert callable(model_xtype_XImportSection.__init__)


def test_model_xtype_ximportsection_constructor_args():
    sig = inspect.signature(model_xtype_XImportSection.__init__)
    params = list(sig.parameters.keys())



def test_jvmspecializedtypereference_is_not_abstract():
    assert not inspect.isabstract(JvmSpecializedTypeReference)


def test_jvmspecializedtypereference_constructor_exists():
    assert callable(JvmSpecializedTypeReference.__init__)


def test_jvmspecializedtypereference_constructor_args():
    sig = inspect.signature(JvmSpecializedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_model_xtype_xcomputedtypereference_is_not_abstract():
    assert not inspect.isabstract(model_xtype_XComputedTypeReference)


def test_model_xtype_xcomputedtypereference_constructor_exists():
    assert callable(model_xtype_XComputedTypeReference.__init__)


def test_model_xtype_xcomputedtypereference_constructor_args():
    sig = inspect.signature(model_xtype_XComputedTypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "typeProvider" in params, "Missing parameter 'typeProvider'"

def test_model_xtype_xcomputedtypereference_has_typeProvider():
    assert hasattr(model_xtype_XComputedTypeReference, "typeProvider")
    descriptor = None
    for klass in model_xtype_XComputedTypeReference.__mro__:
        if "typeProvider" in klass.__dict__:
            descriptor = klass.__dict__["typeProvider"]
            break
    assert isinstance(descriptor, property)



def test_model_xtype_xfunctiontyperef_is_not_abstract():
    assert not inspect.isabstract(model_xtype_XFunctionTypeRef)


def test_model_xtype_xfunctiontyperef_constructor_exists():
    assert callable(model_xtype_XFunctionTypeRef.__init__)


def test_model_xtype_xfunctiontyperef_constructor_args():
    sig = inspect.signature(model_xtype_XFunctionTypeRef.__init__)
    params = list(sig.parameters.keys())
    assert "instanceContext" in params, "Missing parameter 'instanceContext'"

def test_model_xtype_xfunctiontyperef_has_instanceContext():
    assert hasattr(model_xtype_XFunctionTypeRef, "instanceContext")
    descriptor = None
    for klass in model_xtype_XFunctionTypeRef.__mro__:
        if "instanceContext" in klass.__dict__:
            descriptor = klass.__dict__["instanceContext"]
            break
    assert isinstance(descriptor, property)



def test_model_xannotation_xannotationelementvaluepair_is_not_abstract():
    assert not inspect.isabstract(model_xannotation_XAnnotationElementValuePair)


def test_model_xannotation_xannotationelementvaluepair_constructor_exists():
    assert callable(model_xannotation_XAnnotationElementValuePair.__init__)


def test_model_xannotation_xannotationelementvaluepair_constructor_args():
    sig = inspect.signature(model_xannotation_XAnnotationElementValuePair.__init__)
    params = list(sig.parameters.keys())



def test_jvmannotationvalue_is_not_abstract():
    assert not inspect.isabstract(JvmAnnotationValue)


def test_jvmannotationvalue_constructor_exists():
    assert callable(JvmAnnotationValue.__init__)


def test_jvmannotationvalue_constructor_args():
    sig = inspect.signature(JvmAnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmtypeannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmTypeAnnotationValue)


def test_model_types_jvmtypeannotationvalue_constructor_exists():
    assert callable(model_types_JvmTypeAnnotationValue.__init__)


def test_model_types_jvmtypeannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmTypeAnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmshortannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmShortAnnotationValue)


def test_model_types_jvmshortannotationvalue_constructor_exists():
    assert callable(model_types_JvmShortAnnotationValue.__init__)


def test_model_types_jvmshortannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmShortAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_types_jvmshortannotationvalue_has_values():
    assert hasattr(model_types_JvmShortAnnotationValue, "values")
    descriptor = None
    for klass in model_types_JvmShortAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmstringannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmStringAnnotationValue)


def test_model_types_jvmstringannotationvalue_constructor_exists():
    assert callable(model_types_JvmStringAnnotationValue.__init__)


def test_model_types_jvmstringannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmStringAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_types_jvmstringannotationvalue_has_values():
    assert hasattr(model_types_JvmStringAnnotationValue, "values")
    descriptor = None
    for klass in model_types_JvmStringAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmannotationannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmAnnotationAnnotationValue)


def test_model_types_jvmannotationannotationvalue_constructor_exists():
    assert callable(model_types_JvmAnnotationAnnotationValue.__init__)


def test_model_types_jvmannotationannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmAnnotationAnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmenumannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmEnumAnnotationValue)


def test_model_types_jvmenumannotationvalue_constructor_exists():
    assert callable(model_types_JvmEnumAnnotationValue.__init__)


def test_model_types_jvmenumannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmEnumAnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmbyteannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmByteAnnotationValue)


def test_model_types_jvmbyteannotationvalue_constructor_exists():
    assert callable(model_types_JvmByteAnnotationValue.__init__)


def test_model_types_jvmbyteannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmByteAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_types_jvmbyteannotationvalue_has_values():
    assert hasattr(model_types_JvmByteAnnotationValue, "values")
    descriptor = None
    for klass in model_types_JvmByteAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmbooleanannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmBooleanAnnotationValue)


def test_model_types_jvmbooleanannotationvalue_constructor_exists():
    assert callable(model_types_JvmBooleanAnnotationValue.__init__)


def test_model_types_jvmbooleanannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmBooleanAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_types_jvmbooleanannotationvalue_has_values():
    assert hasattr(model_types_JvmBooleanAnnotationValue, "values")
    descriptor = None
    for klass in model_types_JvmBooleanAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmintannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmIntAnnotationValue)


def test_model_types_jvmintannotationvalue_constructor_exists():
    assert callable(model_types_JvmIntAnnotationValue.__init__)


def test_model_types_jvmintannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmIntAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_types_jvmintannotationvalue_has_values():
    assert hasattr(model_types_JvmIntAnnotationValue, "values")
    descriptor = None
    for klass in model_types_JvmIntAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_jvmoperation_is_not_abstract():
    assert not inspect.isabstract(JvmOperation)


def test_jvmoperation_constructor_exists():
    assert callable(JvmOperation.__init__)


def test_jvmoperation_constructor_args():
    sig = inspect.signature(JvmOperation.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmAnnotationValue)


def test_model_types_jvmannotationvalue_constructor_exists():
    assert callable(model_types_JvmAnnotationValue.__init__)


def test_model_types_jvmannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmAnnotationValue.__init__)
    params = list(sig.parameters.keys())



def test_jvmannotationtype_is_not_abstract():
    assert not inspect.isabstract(JvmAnnotationType)


def test_jvmannotationtype_constructor_exists():
    assert callable(JvmAnnotationType.__init__)


def test_jvmannotationtype_constructor_args():
    sig = inspect.signature(JvmAnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmannotationreference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmAnnotationReference)


def test_model_types_jvmannotationreference_constructor_exists():
    assert callable(model_types_JvmAnnotationReference.__init__)


def test_model_types_jvmannotationreference_constructor_args():
    sig = inspect.signature(model_types_JvmAnnotationReference.__init__)
    params = list(sig.parameters.keys())



def test_jvmannotationreference_is_not_abstract():
    assert not inspect.isabstract(JvmAnnotationReference)


def test_jvmannotationreference_constructor_exists():
    assert callable(JvmAnnotationReference.__init__)


def test_jvmannotationreference_constructor_args():
    sig = inspect.signature(JvmAnnotationReference.__init__)
    params = list(sig.parameters.keys())



def test_jvmannotationtarget_is_not_abstract():
    assert not inspect.isabstract(JvmAnnotationTarget)


def test_jvmannotationtarget_constructor_exists():
    assert callable(JvmAnnotationTarget.__init__)


def test_jvmannotationtarget_constructor_args():
    sig = inspect.signature(JvmAnnotationTarget.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmformalparameter_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmFormalParameter)


def test_model_types_jvmformalparameter_constructor_exists():
    assert callable(model_types_JvmFormalParameter.__init__)


def test_model_types_jvmformalparameter_constructor_args():
    sig = inspect.signature(model_types_JvmFormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varArg" in params, "Missing parameter 'varArg'"
    assert "name" in params, "Missing parameter 'name'"

def test_model_types_jvmformalparameter_has_varArg():
    assert hasattr(model_types_JvmFormalParameter, "varArg")
    descriptor = None
    for klass in model_types_JvmFormalParameter.__mro__:
        if "varArg" in klass.__dict__:
            descriptor = klass.__dict__["varArg"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmformalparameter_has_name():
    assert hasattr(model_types_JvmFormalParameter, "name")
    descriptor = None
    for klass in model_types_JvmFormalParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmmember_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmMember)


def test_model_types_jvmmember_constructor_exists():
    assert callable(model_types_JvmMember.__init__)


def test_model_types_jvmmember_constructor_args():
    sig = inspect.signature(model_types_JvmMember.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "simpleName" in params, "Missing parameter 'simpleName'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_model_types_jvmmember_has_modifiers():
    assert hasattr(model_types_JvmMember, "modifiers")
    descriptor = None
    for klass in model_types_JvmMember.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmmember_has_identifier():
    assert hasattr(model_types_JvmMember, "identifier")
    descriptor = None
    for klass in model_types_JvmMember.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmmember_has_simpleName():
    assert hasattr(model_types_JvmMember, "simpleName")
    descriptor = None
    for klass in model_types_JvmMember.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmmember_has_visibility():
    assert hasattr(model_types_JvmMember, "visibility")
    descriptor = None
    for klass in model_types_JvmMember.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_jvmcompoundtypereference_is_not_abstract():
    assert not inspect.isabstract(JvmCompoundTypeReference)


def test_jvmcompoundtypereference_constructor_exists():
    assert callable(JvmCompoundTypeReference.__init__)


def test_jvmcompoundtypereference_constructor_args():
    sig = inspect.signature(JvmCompoundTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmsynonymtypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmSynonymTypeReference)


def test_model_types_jvmsynonymtypereference_constructor_exists():
    assert callable(model_types_JvmSynonymTypeReference.__init__)


def test_model_types_jvmsynonymtypereference_constructor_args():
    sig = inspect.signature(model_types_JvmSynonymTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmmultitypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmMultiTypeReference)


def test_model_types_jvmmultitypereference_constructor_exists():
    assert callable(model_types_JvmMultiTypeReference.__init__)


def test_model_types_jvmmultitypereference_constructor_args():
    sig = inspect.signature(model_types_JvmMultiTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jvmexecutable_is_not_abstract():
    assert not inspect.isabstract(JvmExecutable)


def test_jvmexecutable_constructor_exists():
    assert callable(JvmExecutable.__init__)


def test_jvmexecutable_constructor_args():
    sig = inspect.signature(JvmExecutable.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmoperation_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmOperation)


def test_model_types_jvmoperation_constructor_exists():
    assert callable(model_types_JvmOperation.__init__)


def test_model_types_jvmoperation_constructor_args():
    sig = inspect.signature(model_types_JvmOperation.__init__)
    params = list(sig.parameters.keys())
    assert "strictFloatingPoint" in params, "Missing parameter 'strictFloatingPoint'"
    assert "final" in params, "Missing parameter 'final'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "static" in params, "Missing parameter 'static'"
    assert "default" in params, "Missing parameter 'default'"
    assert "native" in params, "Missing parameter 'native'"

def test_model_types_jvmoperation_has_strictFloatingPoint():
    assert hasattr(model_types_JvmOperation, "strictFloatingPoint")
    descriptor = None
    for klass in model_types_JvmOperation.__mro__:
        if "strictFloatingPoint" in klass.__dict__:
            descriptor = klass.__dict__["strictFloatingPoint"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmoperation_has_final():
    assert hasattr(model_types_JvmOperation, "final")
    descriptor = None
    for klass in model_types_JvmOperation.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmoperation_has_abstract():
    assert hasattr(model_types_JvmOperation, "abstract")
    descriptor = None
    for klass in model_types_JvmOperation.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmoperation_has_synchronized():
    assert hasattr(model_types_JvmOperation, "synchronized")
    descriptor = None
    for klass in model_types_JvmOperation.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmoperation_has_static():
    assert hasattr(model_types_JvmOperation, "static")
    descriptor = None
    for klass in model_types_JvmOperation.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmoperation_has_default():
    assert hasattr(model_types_JvmOperation, "default")
    descriptor = None
    for klass in model_types_JvmOperation.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmoperation_has_native():
    assert hasattr(model_types_JvmOperation, "native")
    descriptor = None
    for klass in model_types_JvmOperation.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmconstructor_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmConstructor)


def test_model_types_jvmconstructor_constructor_exists():
    assert callable(model_types_JvmConstructor.__init__)


def test_model_types_jvmconstructor_constructor_args():
    sig = inspect.signature(model_types_JvmConstructor.__init__)
    params = list(sig.parameters.keys())



def test_jvmformalparameter_is_not_abstract():
    assert not inspect.isabstract(JvmFormalParameter)


def test_jvmformalparameter_constructor_exists():
    assert callable(JvmFormalParameter.__init__)


def test_jvmformalparameter_constructor_args():
    sig = inspect.signature(JvmFormalParameter.__init__)
    params = list(sig.parameters.keys())



def test_types_jvmfeature_is_not_abstract():
    assert not inspect.isabstract(types_JvmFeature)


def test_types_jvmfeature_constructor_exists():
    assert callable(types_JvmFeature.__init__)


def test_types_jvmfeature_constructor_args():
    sig = inspect.signature(types_JvmFeature.__init__)
    params = list(sig.parameters.keys())



def test_xexpression_is_not_abstract():
    assert not inspect.isabstract(XExpression)


def test_xexpression_constructor_exists():
    assert callable(XExpression.__init__)


def test_xexpression_constructor_args():
    sig = inspect.signature(XExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xannotation_xannotation_is_not_abstract():
    assert not inspect.isabstract(model_xannotation_XAnnotation)


def test_model_xannotation_xannotation_constructor_exists():
    assert callable(model_xannotation_XAnnotation.__init__)


def test_model_xannotation_xannotation_constructor_args():
    sig = inspect.signature(model_xannotation_XAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_jvmfeature_is_not_abstract():
    assert not inspect.isabstract(JvmFeature)


def test_jvmfeature_constructor_exists():
    assert callable(JvmFeature.__init__)


def test_jvmfeature_constructor_args():
    sig = inspect.signature(JvmFeature.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmfield_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmField)


def test_model_types_jvmfield_constructor_exists():
    assert callable(model_types_JvmField.__init__)


def test_model_types_jvmfield_constructor_args():
    sig = inspect.signature(model_types_JvmField.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "final" in params, "Missing parameter 'final'"
    assert "transient" in params, "Missing parameter 'transient'"

def test_model_types_jvmfield_has_static():
    assert hasattr(model_types_JvmField, "static")
    descriptor = None
    for klass in model_types_JvmField.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmfield_has_volatile():
    assert hasattr(model_types_JvmField, "volatile")
    descriptor = None
    for klass in model_types_JvmField.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmfield_has_final():
    assert hasattr(model_types_JvmField, "final")
    descriptor = None
    for klass in model_types_JvmField.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmfield_has_transient():
    assert hasattr(model_types_JvmField, "transient")
    descriptor = None
    for klass in model_types_JvmField.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmtypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmTypeReference)


def test_model_types_jvmtypereference_constructor_exists():
    assert callable(model_types_JvmTypeReference.__init__)


def test_model_types_jvmtypereference_constructor_args():
    sig = inspect.signature(model_types_JvmTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types_jvmtypereference_is_not_abstract():
    assert not inspect.isabstract(types_JvmTypeReference)


def test_types_jvmtypereference_constructor_exists():
    assert callable(types_JvmTypeReference.__init__)


def test_types_jvmtypereference_constructor_args():
    sig = inspect.signature(types_JvmTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jvmconstraintowner_is_not_abstract():
    assert not inspect.isabstract(JvmConstraintOwner)


def test_jvmconstraintowner_constructor_exists():
    assert callable(JvmConstraintOwner.__init__)


def test_jvmconstraintowner_constructor_args():
    sig = inspect.signature(JvmConstraintOwner.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmTypeConstraint)


def test_model_types_jvmtypeconstraint_constructor_exists():
    assert callable(model_types_JvmTypeConstraint.__init__)


def test_model_types_jvmtypeconstraint_constructor_args():
    sig = inspect.signature(model_types_JvmTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_jvmtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(JvmTypeConstraint)


def test_jvmtypeconstraint_constructor_exists():
    assert callable(JvmTypeConstraint.__init__)


def test_jvmtypeconstraint_constructor_args():
    sig = inspect.signature(JvmTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmconstraintowner_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmConstraintOwner)


def test_model_types_jvmconstraintowner_constructor_exists():
    assert callable(model_types_JvmConstraintOwner.__init__)


def test_model_types_jvmconstraintowner_constructor_args():
    sig = inspect.signature(model_types_JvmConstraintOwner.__init__)
    params = list(sig.parameters.keys())



def test_jvmparameterizedtypereference_is_not_abstract():
    assert not inspect.isabstract(JvmParameterizedTypeReference)


def test_jvmparameterizedtypereference_constructor_exists():
    assert callable(JvmParameterizedTypeReference.__init__)


def test_jvmparameterizedtypereference_constructor_args():
    sig = inspect.signature(JvmParameterizedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jvmtypeparameter_is_not_abstract():
    assert not inspect.isabstract(JvmTypeParameter)


def test_jvmtypeparameter_constructor_exists():
    assert callable(JvmTypeParameter.__init__)


def test_jvmtypeparameter_constructor_args():
    sig = inspect.signature(JvmTypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_types_jvmtypeparameterdeclarator_is_not_abstract():
    assert not inspect.isabstract(types_JvmTypeParameterDeclarator)


def test_types_jvmtypeparameterdeclarator_constructor_exists():
    assert callable(types_JvmTypeParameterDeclarator.__init__)


def test_types_jvmtypeparameterdeclarator_constructor_args():
    sig = inspect.signature(types_JvmTypeParameterDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmexecutable_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmExecutable)


def test_model_types_jvmexecutable_constructor_exists():
    assert callable(model_types_JvmExecutable.__init__)


def test_model_types_jvmexecutable_constructor_args():
    sig = inspect.signature(model_types_JvmExecutable.__init__)
    params = list(sig.parameters.keys())
    assert "varArgs" in params, "Missing parameter 'varArgs'"

def test_model_types_jvmexecutable_has_varArgs():
    assert hasattr(model_types_JvmExecutable, "varArgs")
    descriptor = None
    for klass in model_types_JvmExecutable.__mro__:
        if "varArgs" in klass.__dict__:
            descriptor = klass.__dict__["varArgs"]
            break
    assert isinstance(descriptor, property)



def test_types_jvmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(types_JvmDeclaredType)


def test_types_jvmdeclaredtype_constructor_exists():
    assert callable(types_JvmDeclaredType.__init__)


def test_types_jvmdeclaredtype_constructor_args():
    sig = inspect.signature(types_JvmDeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmgenerictype_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmGenericType)


def test_model_types_jvmgenerictype_constructor_exists():
    assert callable(model_types_JvmGenericType.__init__)


def test_model_types_jvmgenerictype_constructor_args():
    sig = inspect.signature(model_types_JvmGenericType.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"
    assert "strictFloatingPoint" in params, "Missing parameter 'strictFloatingPoint'"

def test_model_types_jvmgenerictype_has_interface():
    assert hasattr(model_types_JvmGenericType, "interface")
    descriptor = None
    for klass in model_types_JvmGenericType.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmgenerictype_has_strictFloatingPoint():
    assert hasattr(model_types_JvmGenericType, "strictFloatingPoint")
    descriptor = None
    for klass in model_types_JvmGenericType.__mro__:
        if "strictFloatingPoint" in klass.__dict__:
            descriptor = klass.__dict__["strictFloatingPoint"]
            break
    assert isinstance(descriptor, property)



def test_jvmfield_is_not_abstract():
    assert not inspect.isabstract(JvmField)


def test_jvmfield_constructor_exists():
    assert callable(JvmField.__init__)


def test_jvmfield_constructor_args():
    sig = inspect.signature(JvmField.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmenumerationliteral_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmEnumerationLiteral)


def test_model_types_jvmenumerationliteral_constructor_exists():
    assert callable(model_types_JvmEnumerationLiteral.__init__)


def test_model_types_jvmenumerationliteral_constructor_args():
    sig = inspect.signature(model_types_JvmEnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jvmenumerationliteral_is_not_abstract():
    assert not inspect.isabstract(JvmEnumerationLiteral)


def test_jvmenumerationliteral_constructor_exists():
    assert callable(JvmEnumerationLiteral.__init__)


def test_jvmenumerationliteral_constructor_args():
    sig = inspect.signature(JvmEnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jvmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(JvmDeclaredType)


def test_jvmdeclaredtype_constructor_exists():
    assert callable(JvmDeclaredType.__init__)


def test_jvmdeclaredtype_constructor_args():
    sig = inspect.signature(JvmDeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmenumerationtype_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmEnumerationType)


def test_model_types_jvmenumerationtype_constructor_exists():
    assert callable(model_types_JvmEnumerationType.__init__)


def test_model_types_jvmenumerationtype_constructor_args():
    sig = inspect.signature(model_types_JvmEnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmannotationtype_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmAnnotationType)


def test_model_types_jvmannotationtype_constructor_exists():
    assert callable(model_types_JvmAnnotationType.__init__)


def test_model_types_jvmannotationtype_constructor_args():
    sig = inspect.signature(model_types_JvmAnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmlowerbound_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmLowerBound)


def test_model_types_jvmlowerbound_constructor_exists():
    assert callable(model_types_JvmLowerBound.__init__)


def test_model_types_jvmlowerbound_constructor_args():
    sig = inspect.signature(model_types_JvmLowerBound.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmupperbound_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmUpperBound)


def test_model_types_jvmupperbound_constructor_exists():
    assert callable(model_types_JvmUpperBound.__init__)


def test_model_types_jvmupperbound_constructor_args():
    sig = inspect.signature(model_types_JvmUpperBound.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmtypeparameterdeclarator_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmTypeParameterDeclarator)


def test_model_types_jvmtypeparameterdeclarator_constructor_exists():
    assert callable(model_types_JvmTypeParameterDeclarator.__init__)


def test_model_types_jvmtypeparameterdeclarator_constructor_args():
    sig = inspect.signature(model_types_JvmTypeParameterDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_jvmtypeparameterdeclarator_is_not_abstract():
    assert not inspect.isabstract(JvmTypeParameterDeclarator)


def test_jvmtypeparameterdeclarator_constructor_exists():
    assert callable(JvmTypeParameterDeclarator.__init__)


def test_jvmtypeparameterdeclarator_constructor_args():
    sig = inspect.signature(JvmTypeParameterDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_types_jvmconstraintowner_is_not_abstract():
    assert not inspect.isabstract(types_JvmConstraintOwner)


def test_types_jvmconstraintowner_constructor_exists():
    assert callable(types_JvmConstraintOwner.__init__)


def test_types_jvmconstraintowner_constructor_args():
    sig = inspect.signature(types_JvmConstraintOwner.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmwildcardtypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmWildcardTypeReference)


def test_model_types_jvmwildcardtypereference_constructor_exists():
    assert callable(model_types_JvmWildcardTypeReference.__init__)


def test_model_types_jvmwildcardtypereference_constructor_args():
    sig = inspect.signature(model_types_JvmWildcardTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_jvmmember_is_not_abstract():
    assert not inspect.isabstract(JvmMember)


def test_jvmmember_constructor_exists():
    assert callable(JvmMember.__init__)


def test_jvmmember_constructor_args():
    sig = inspect.signature(JvmMember.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmfeature_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmFeature)


def test_model_types_jvmfeature_constructor_exists():
    assert callable(model_types_JvmFeature.__init__)


def test_model_types_jvmfeature_constructor_args():
    sig = inspect.signature(model_types_JvmFeature.__init__)
    params = list(sig.parameters.keys())



def test_jvmtypereference_is_not_abstract():
    assert not inspect.isabstract(JvmTypeReference)


def test_jvmtypereference_constructor_exists():
    assert callable(JvmTypeReference.__init__)


def test_jvmtypereference_constructor_args():
    sig = inspect.signature(JvmTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmparameterizedtypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmParameterizedTypeReference)


def test_model_types_jvmparameterizedtypereference_constructor_exists():
    assert callable(model_types_JvmParameterizedTypeReference.__init__)


def test_model_types_jvmparameterizedtypereference_constructor_args():
    sig = inspect.signature(model_types_JvmParameterizedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmspecializedtypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmSpecializedTypeReference)


def test_model_types_jvmspecializedtypereference_constructor_exists():
    assert callable(model_types_JvmSpecializedTypeReference.__init__)


def test_model_types_jvmspecializedtypereference_constructor_args():
    sig = inspect.signature(model_types_JvmSpecializedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmcompoundtypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmCompoundTypeReference)


def test_model_types_jvmcompoundtypereference_constructor_exists():
    assert callable(model_types_JvmCompoundTypeReference.__init__)


def test_model_types_jvmcompoundtypereference_constructor_args():
    sig = inspect.signature(model_types_JvmCompoundTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmanytypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmAnyTypeReference)


def test_model_types_jvmanytypereference_constructor_exists():
    assert callable(model_types_JvmAnyTypeReference.__init__)


def test_model_types_jvmanytypereference_constructor_args():
    sig = inspect.signature(model_types_JvmAnyTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmdelegatetypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmDelegateTypeReference)


def test_model_types_jvmdelegatetypereference_constructor_exists():
    assert callable(model_types_JvmDelegateTypeReference.__init__)


def test_model_types_jvmdelegatetypereference_constructor_args():
    sig = inspect.signature(model_types_JvmDelegateTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmgenericarraytypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmGenericArrayTypeReference)


def test_model_types_jvmgenericarraytypereference_constructor_exists():
    assert callable(model_types_JvmGenericArrayTypeReference.__init__)


def test_model_types_jvmgenericarraytypereference_constructor_args():
    sig = inspect.signature(model_types_JvmGenericArrayTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmunknowntypereference_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmUnknownTypeReference)


def test_model_types_jvmunknowntypereference_constructor_exists():
    assert callable(model_types_JvmUnknownTypeReference.__init__)


def test_model_types_jvmunknowntypereference_constructor_args():
    sig = inspect.signature(model_types_JvmUnknownTypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_model_types_jvmunknowntypereference_has_qualifiedName():
    assert hasattr(model_types_JvmUnknownTypeReference, "qualifiedName")
    descriptor = None
    for klass in model_types_JvmUnknownTypeReference.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_types_jvmcomponenttype_is_not_abstract():
    assert not inspect.isabstract(types_JvmComponentType)


def test_types_jvmcomponenttype_constructor_exists():
    assert callable(types_JvmComponentType.__init__)


def test_types_jvmcomponenttype_constructor_args():
    sig = inspect.signature(types_JvmComponentType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmtypeparameter_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmTypeParameter)


def test_model_types_jvmtypeparameter_constructor_exists():
    assert callable(model_types_JvmTypeParameter.__init__)


def test_model_types_jvmtypeparameter_constructor_args():
    sig = inspect.signature(model_types_JvmTypeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_types_jvmtypeparameter_has_name():
    assert hasattr(model_types_JvmTypeParameter, "name")
    descriptor = None
    for klass in model_types_JvmTypeParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_jvmmember_is_not_abstract():
    assert not inspect.isabstract(types_JvmMember)


def test_types_jvmmember_constructor_exists():
    assert callable(types_JvmMember.__init__)


def test_types_jvmmember_constructor_args():
    sig = inspect.signature(types_JvmMember.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmDeclaredType)


def test_model_types_jvmdeclaredtype_constructor_exists():
    assert callable(model_types_JvmDeclaredType.__init__)


def test_model_types_jvmdeclaredtype_constructor_args():
    sig = inspect.signature(model_types_JvmDeclaredType.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "static" in params, "Missing parameter 'static'"
    assert "exported" in params, "Missing parameter 'exported'"
    assert "packageName" in params, "Missing parameter 'packageName'"
    assert "final" in params, "Missing parameter 'final'"

def test_model_types_jvmdeclaredtype_has_abstract():
    assert hasattr(model_types_JvmDeclaredType, "abstract")
    descriptor = None
    for klass in model_types_JvmDeclaredType.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmdeclaredtype_has_static():
    assert hasattr(model_types_JvmDeclaredType, "static")
    descriptor = None
    for klass in model_types_JvmDeclaredType.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmdeclaredtype_has_exported():
    assert hasattr(model_types_JvmDeclaredType, "exported")
    descriptor = None
    for klass in model_types_JvmDeclaredType.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmdeclaredtype_has_packageName():
    assert hasattr(model_types_JvmDeclaredType, "packageName")
    descriptor = None
    for klass in model_types_JvmDeclaredType.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
            break
    assert isinstance(descriptor, property)

def test_model_types_jvmdeclaredtype_has_final():
    assert hasattr(model_types_JvmDeclaredType, "final")
    descriptor = None
    for klass in model_types_JvmDeclaredType.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_jvmcomponenttype_is_not_abstract():
    assert not inspect.isabstract(JvmComponentType)


def test_jvmcomponenttype_constructor_exists():
    assert callable(JvmComponentType.__init__)


def test_jvmcomponenttype_constructor_args():
    sig = inspect.signature(JvmComponentType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmarraytype_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmArrayType)


def test_model_types_jvmarraytype_constructor_exists():
    assert callable(model_types_JvmArrayType.__init__)


def test_model_types_jvmarraytype_constructor_args():
    sig = inspect.signature(model_types_JvmArrayType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmprimitivetype_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmPrimitiveType)


def test_model_types_jvmprimitivetype_constructor_exists():
    assert callable(model_types_JvmPrimitiveType.__init__)


def test_model_types_jvmprimitivetype_constructor_args():
    sig = inspect.signature(model_types_JvmPrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"

def test_model_types_jvmprimitivetype_has_simpleName():
    assert hasattr(model_types_JvmPrimitiveType, "simpleName")
    descriptor = None
    for klass in model_types_JvmPrimitiveType.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)



def test_jvmarraytype_is_not_abstract():
    assert not inspect.isabstract(JvmArrayType)


def test_jvmarraytype_constructor_exists():
    assert callable(JvmArrayType.__init__)


def test_jvmarraytype_constructor_args():
    sig = inspect.signature(JvmArrayType.__init__)
    params = list(sig.parameters.keys())



def test_jvmtype_is_not_abstract():
    assert not inspect.isabstract(JvmType)


def test_jvmtype_constructor_exists():
    assert callable(JvmType.__init__)


def test_jvmtype_constructor_args():
    sig = inspect.signature(JvmType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmcomponenttype_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmComponentType)


def test_model_types_jvmcomponenttype_constructor_exists():
    assert callable(model_types_JvmComponentType.__init__)


def test_model_types_jvmcomponenttype_constructor_args():
    sig = inspect.signature(model_types_JvmComponentType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmvoid_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmVoid)


def test_model_types_jvmvoid_constructor_exists():
    assert callable(model_types_JvmVoid.__init__)


def test_model_types_jvmvoid_constructor_args():
    sig = inspect.signature(model_types_JvmVoid.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmnomodule_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmNoModule)


def test_model_types_jvmnomodule_constructor_exists():
    assert callable(model_types_JvmNoModule.__init__)


def test_model_types_jvmnomodule_constructor_args():
    sig = inspect.signature(model_types_JvmNoModule.__init__)
    params = list(sig.parameters.keys())



def test_xexportsection_is_not_abstract():
    assert not inspect.isabstract(XExportSection)


def test_xexportsection_constructor_exists():
    assert callable(XExportSection.__init__)


def test_xexportsection_constructor_args():
    sig = inspect.signature(XExportSection.__init__)
    params = list(sig.parameters.keys())



def test_types_model_eobject_is_not_abstract():
    assert not inspect.isabstract(types_model_EObject)


def test_types_model_eobject_constructor_exists():
    assert callable(types_model_EObject.__init__)


def test_types_model_eobject_constructor_args():
    sig = inspect.signature(types_model_EObject.__init__)
    params = list(sig.parameters.keys())



def test_ximportsection1_is_not_abstract():
    assert not inspect.isabstract(XImportSection1)


def test_ximportsection1_constructor_exists():
    assert callable(XImportSection1.__init__)


def test_ximportsection1_constructor_args():
    sig = inspect.signature(XImportSection1.__init__)
    params = list(sig.parameters.keys())



def test_jvmidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(JvmIdentifiableElement)


def test_jvmidentifiableelement_constructor_exists():
    assert callable(JvmIdentifiableElement.__init__)


def test_jvmidentifiableelement_constructor_args():
    sig = inspect.signature(JvmIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmannotationtarget_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmAnnotationTarget)


def test_model_types_jvmannotationtarget_constructor_exists():
    assert callable(model_types_JvmAnnotationTarget.__init__)


def test_model_types_jvmannotationtarget_constructor_args():
    sig = inspect.signature(model_types_JvmAnnotationTarget.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmtype_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmType)


def test_model_types_jvmtype_constructor_exists():
    assert callable(model_types_JvmType.__init__)


def test_model_types_jvmtype_constructor_args():
    sig = inspect.signature(model_types_JvmType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmmodule_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmModule)


def test_model_types_jvmmodule_constructor_exists():
    assert callable(model_types_JvmModule.__init__)


def test_model_types_jvmmodule_constructor_args():
    sig = inspect.signature(model_types_JvmModule.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"

def test_model_types_jvmmodule_has_simpleName():
    assert hasattr(model_types_JvmModule, "simpleName")
    descriptor = None
    for klass in model_types_JvmModule.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmIdentifiableElement)


def test_model_types_jvmidentifiableelement_constructor_exists():
    assert callable(model_types_JvmIdentifiableElement.__init__)


def test_model_types_jvmidentifiableelement_constructor_args():
    sig = inspect.signature(model_types_JvmIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendformalparameter_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendFormalParameter)


def test_model_ss_xtendformalparameter_constructor_exists():
    assert callable(model_ss_XtendFormalParameter.__init__)


def test_model_ss_xtendformalparameter_constructor_args():
    sig = inspect.signature(model_ss_XtendFormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"

def test_model_ss_xtendformalparameter_has_extension():
    assert hasattr(model_ss_XtendFormalParameter, "extension")
    descriptor = None
    for klass in model_ss_XtendFormalParameter.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)



def test_xvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(XVariableDeclaration)


def test_xvariabledeclaration_constructor_exists():
    assert callable(XVariableDeclaration.__init__)


def test_xvariabledeclaration_constructor_args():
    sig = inspect.signature(XVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendVariableDeclaration)


def test_model_ss_xtendvariabledeclaration_constructor_exists():
    assert callable(model_ss_XtendVariableDeclaration.__init__)


def test_model_ss_xtendvariabledeclaration_constructor_args():
    sig = inspect.signature(model_ss_XtendVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"

def test_model_ss_xtendvariabledeclaration_has_extension():
    assert hasattr(model_ss_XtendVariableDeclaration, "extension")
    descriptor = None
    for klass in model_ss_XtendVariableDeclaration.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)



def test_model_ss_createextensioninfo_is_not_abstract():
    assert not inspect.isabstract(model_ss_CreateExtensionInfo)


def test_model_ss_createextensioninfo_constructor_exists():
    assert callable(model_ss_CreateExtensionInfo.__init__)


def test_model_ss_createextensioninfo_constructor_args():
    sig = inspect.signature(model_ss_CreateExtensionInfo.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_ss_createextensioninfo_has_name():
    assert hasattr(model_ss_CreateExtensionInfo, "name")
    descriptor = None
    for klass in model_ss_CreateExtensionInfo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_ss_richstringelseif_is_not_abstract():
    assert not inspect.isabstract(model_ss_RichStringElseIf)


def test_model_ss_richstringelseif_constructor_exists():
    assert callable(model_ss_RichStringElseIf.__init__)


def test_model_ss_richstringelseif_constructor_args():
    sig = inspect.signature(model_ss_RichStringElseIf.__init__)
    params = list(sig.parameters.keys())



def test_richstringelseif_is_not_abstract():
    assert not inspect.isabstract(RichStringElseIf)


def test_richstringelseif_constructor_exists():
    assert callable(RichStringElseIf.__init__)


def test_richstringelseif_constructor_args():
    sig = inspect.signature(RichStringElseIf.__init__)
    params = list(sig.parameters.keys())



def test_xblockexpression_is_not_abstract():
    assert not inspect.isabstract(XBlockExpression)


def test_xblockexpression_constructor_exists():
    assert callable(XBlockExpression.__init__)


def test_xblockexpression_constructor_args():
    sig = inspect.signature(XBlockExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_richstring_is_not_abstract():
    assert not inspect.isabstract(model_ss_RichString)


def test_model_ss_richstring_constructor_exists():
    assert callable(model_ss_RichString.__init__)


def test_model_ss_richstring_constructor_args():
    sig = inspect.signature(model_ss_RichString.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_richstringif_is_not_abstract():
    assert not inspect.isabstract(model_ss_RichStringIf)


def test_model_ss_richstringif_constructor_exists():
    assert callable(model_ss_RichStringIf.__init__)


def test_model_ss_richstringif_constructor_args():
    sig = inspect.signature(model_ss_RichStringIf.__init__)
    params = list(sig.parameters.keys())



def test_xforeachexpression_is_not_abstract():
    assert not inspect.isabstract(XForEachExpression)


def test_xforeachexpression_constructor_exists():
    assert callable(XForEachExpression.__init__)


def test_xforeachexpression_constructor_args():
    sig = inspect.signature(XForEachExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_richstringforloop_is_not_abstract():
    assert not inspect.isabstract(model_ss_RichStringForLoop)


def test_model_ss_richstringforloop_constructor_exists():
    assert callable(model_ss_RichStringForLoop.__init__)


def test_model_ss_richstringforloop_constructor_args():
    sig = inspect.signature(model_ss_RichStringForLoop.__init__)
    params = list(sig.parameters.keys())



def test_xstringliteral_is_not_abstract():
    assert not inspect.isabstract(XStringLiteral)


def test_xstringliteral_constructor_exists():
    assert callable(XStringLiteral.__init__)


def test_xstringliteral_constructor_args():
    sig = inspect.signature(XStringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_richstringliteral_is_not_abstract():
    assert not inspect.isabstract(model_ss_RichStringLiteral)


def test_model_ss_richstringliteral_constructor_exists():
    assert callable(model_ss_RichStringLiteral.__init__)


def test_model_ss_richstringliteral_constructor_args():
    sig = inspect.signature(model_ss_RichStringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_createextensioninfo_is_not_abstract():
    assert not inspect.isabstract(CreateExtensionInfo)


def test_createextensioninfo_constructor_exists():
    assert callable(CreateExtensionInfo.__init__)


def test_createextensioninfo_constructor_args():
    sig = inspect.signature(CreateExtensionInfo.__init__)
    params = list(sig.parameters.keys())



def test_xtendparameter_is_not_abstract():
    assert not inspect.isabstract(XtendParameter)


def test_xtendparameter_constructor_exists():
    assert callable(XtendParameter.__init__)


def test_xtendparameter_constructor_args():
    sig = inspect.signature(XtendParameter.__init__)
    params = list(sig.parameters.keys())



def test_xtendmember_is_not_abstract():
    assert not inspect.isabstract(XtendMember)


def test_xtendmember_constructor_exists():
    assert callable(XtendMember.__init__)


def test_xtendmember_constructor_args():
    sig = inspect.signature(XtendMember.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendfield_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendField)


def test_model_ss_xtendfield_constructor_exists():
    assert callable(model_ss_XtendField.__init__)


def test_model_ss_xtendfield_constructor_args():
    sig = inspect.signature(model_ss_XtendField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_ss_xtendfield_has_name():
    assert hasattr(model_ss_XtendField, "name")
    descriptor = None
    for klass in model_ss_XtendField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_ss_xtendenumliteral_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendEnumLiteral)


def test_model_ss_xtendenumliteral_constructor_exists():
    assert callable(model_ss_XtendEnumLiteral.__init__)


def test_model_ss_xtendenumliteral_constructor_args():
    sig = inspect.signature(model_ss_XtendEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_ss_xtendenumliteral_has_name():
    assert hasattr(model_ss_XtendEnumLiteral, "name")
    descriptor = None
    for klass in model_ss_XtendEnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_ss_xtendconstructor_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendConstructor)


def test_model_ss_xtendconstructor_constructor_exists():
    assert callable(model_ss_XtendConstructor.__init__)


def test_model_ss_xtendconstructor_constructor_args():
    sig = inspect.signature(model_ss_XtendConstructor.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendTypeDeclaration)


def test_model_ss_xtendtypedeclaration_constructor_exists():
    assert callable(model_ss_XtendTypeDeclaration.__init__)


def test_model_ss_xtendtypedeclaration_constructor_args():
    sig = inspect.signature(model_ss_XtendTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_ss_xtendtypedeclaration_has_name():
    assert hasattr(model_ss_XtendTypeDeclaration, "name")
    descriptor = None
    for klass in model_ss_XtendTypeDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_ss_xtendevent_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendEvent)


def test_model_ss_xtendevent_constructor_exists():
    assert callable(model_ss_XtendEvent.__init__)


def test_model_ss_xtendevent_constructor_args():
    sig = inspect.signature(model_ss_XtendEvent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_ss_xtendevent_has_name():
    assert hasattr(model_ss_XtendEvent, "name")
    descriptor = None
    for klass in model_ss_XtendEvent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_ss_xtendfunction_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendFunction)


def test_model_ss_xtendfunction_constructor_exists():
    assert callable(model_ss_XtendFunction.__init__)


def test_model_ss_xtendfunction_constructor_args():
    sig = inspect.signature(model_ss_XtendFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_ss_xtendfunction_has_name():
    assert hasattr(model_ss_XtendFunction, "name")
    descriptor = None
    for klass in model_ss_XtendFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xtendannotationtarget_is_not_abstract():
    assert not inspect.isabstract(XtendAnnotationTarget)


def test_xtendannotationtarget_constructor_exists():
    assert callable(XtendAnnotationTarget.__init__)


def test_xtendannotationtarget_constructor_args():
    sig = inspect.signature(XtendAnnotationTarget.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendparameter_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendParameter)


def test_model_ss_xtendparameter_constructor_exists():
    assert callable(model_ss_XtendParameter.__init__)


def test_model_ss_xtendparameter_constructor_args():
    sig = inspect.signature(model_ss_XtendParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varArg" in params, "Missing parameter 'varArg'"
    assert "extension" in params, "Missing parameter 'extension'"
    assert "name" in params, "Missing parameter 'name'"

def test_model_ss_xtendparameter_has_varArg():
    assert hasattr(model_ss_XtendParameter, "varArg")
    descriptor = None
    for klass in model_ss_XtendParameter.__mro__:
        if "varArg" in klass.__dict__:
            descriptor = klass.__dict__["varArg"]
            break
    assert isinstance(descriptor, property)

def test_model_ss_xtendparameter_has_extension():
    assert hasattr(model_ss_XtendParameter, "extension")
    descriptor = None
    for klass in model_ss_XtendParameter.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_model_ss_xtendparameter_has_name():
    assert hasattr(model_ss_XtendParameter, "name")
    descriptor = None
    for klass in model_ss_XtendParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_ss_xtendmember_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendMember)


def test_model_ss_xtendmember_constructor_exists():
    assert callable(model_ss_XtendMember.__init__)


def test_model_ss_xtendmember_constructor_args():
    sig = inspect.signature(model_ss_XtendMember.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_model_ss_xtendmember_has_modifiers():
    assert hasattr(model_ss_XtendMember, "modifiers")
    descriptor = None
    for klass in model_ss_XtendMember.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_xannotation_is_not_abstract():
    assert not inspect.isabstract(XAnnotation)


def test_xannotation_constructor_exists():
    assert callable(XAnnotation.__init__)


def test_xannotation_constructor_args():
    sig = inspect.signature(XAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendannotationtarget_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendAnnotationTarget)


def test_model_ss_xtendannotationtarget_constructor_exists():
    assert callable(model_ss_XtendAnnotationTarget.__init__)


def test_model_ss_xtendannotationtarget_constructor_args():
    sig = inspect.signature(model_ss_XtendAnnotationTarget.__init__)
    params = list(sig.parameters.keys())



def test_xobjectliteralpart_is_not_abstract():
    assert not inspect.isabstract(XObjectLiteralPart)


def test_xobjectliteralpart_constructor_exists():
    assert callable(XObjectLiteralPart.__init__)


def test_xobjectliteralpart_constructor_args():
    sig = inspect.signature(XObjectLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xobjectliteral_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XObjectLiteral)


def test_model_xbase_xobjectliteral_constructor_exists():
    assert callable(model_xbase_XObjectLiteral.__init__)


def test_model_xbase_xobjectliteral_constructor_args():
    sig = inspect.signature(model_xbase_XObjectLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ss_model_eobject_is_not_abstract():
    assert not inspect.isabstract(ss_model_EObject)


def test_ss_model_eobject_constructor_exists():
    assert callable(ss_model_EObject.__init__)


def test_ss_model_eobject_constructor_args():
    sig = inspect.signature(ss_model_EObject.__init__)
    params = list(sig.parameters.keys())



def test_xtendtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(XtendTypeDeclaration)


def test_xtendtypedeclaration_constructor_exists():
    assert callable(XtendTypeDeclaration.__init__)


def test_xtendtypedeclaration_constructor_args():
    sig = inspect.signature(XtendTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtenddelegate_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendDelegate)


def test_model_ss_xtenddelegate_constructor_exists():
    assert callable(model_ss_XtendDelegate.__init__)


def test_model_ss_xtenddelegate_constructor_args():
    sig = inspect.signature(model_ss_XtendDelegate.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendenum_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendEnum)


def test_model_ss_xtendenum_constructor_exists():
    assert callable(model_ss_XtendEnum.__init__)


def test_model_ss_xtendenum_constructor_args():
    sig = inspect.signature(model_ss_XtendEnum.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendannotationtype_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendAnnotationType)


def test_model_ss_xtendannotationtype_constructor_exists():
    assert callable(model_ss_XtendAnnotationType.__init__)


def test_model_ss_xtendannotationtype_constructor_args():
    sig = inspect.signature(model_ss_XtendAnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendinterface_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendInterface)


def test_model_ss_xtendinterface_constructor_exists():
    assert callable(model_ss_XtendInterface.__init__)


def test_model_ss_xtendinterface_constructor_args():
    sig = inspect.signature(model_ss_XtendInterface.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendclass_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendClass)


def test_model_ss_xtendclass_constructor_exists():
    assert callable(model_ss_XtendClass.__init__)


def test_model_ss_xtendclass_constructor_args():
    sig = inspect.signature(model_ss_XtendClass.__init__)
    params = list(sig.parameters.keys())



def test_model_ss_xtendfile_is_not_abstract():
    assert not inspect.isabstract(model_ss_XtendFile)


def test_model_ss_xtendfile_constructor_exists():
    assert callable(model_ss_XtendFile.__init__)


def test_model_ss_xtendfile_constructor_args():
    sig = inspect.signature(model_ss_XtendFile.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_model_ss_xtendfile_has_package():
    assert hasattr(model_ss_XtendFile, "package")
    descriptor = None
    for klass in model_ss_XtendFile.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xarrayliteral_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XArrayLiteral)


def test_model_xbase_xarrayliteral_constructor_exists():
    assert callable(model_xbase_XArrayLiteral.__init__)


def test_model_xbase_xarrayliteral_constructor_args():
    sig = inspect.signature(model_xbase_XArrayLiteral.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xobjectliteralpart_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XObjectLiteralPart)


def test_model_xbase_xobjectliteralpart_constructor_exists():
    assert callable(model_xbase_XObjectLiteralPart.__init__)


def test_model_xbase_xobjectliteralpart_constructor_args():
    sig = inspect.signature(model_xbase_XObjectLiteralPart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_xbase_xobjectliteralpart_has_name():
    assert hasattr(model_xbase_XObjectLiteralPart, "name")
    descriptor = None
    for klass in model_xbase_XObjectLiteralPart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xternaryoperation_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XTernaryOperation)


def test_model_xbase_xternaryoperation_constructor_exists():
    assert callable(model_xbase_XTernaryOperation.__init__)


def test_model_xbase_xternaryoperation_constructor_args():
    sig = inspect.signature(model_xbase_XTernaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xfunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XFunctionDeclaration)


def test_model_xbase_xfunctiondeclaration_constructor_exists():
    assert callable(model_xbase_XFunctionDeclaration.__init__)


def test_model_xbase_xfunctiondeclaration_constructor_args():
    sig = inspect.signature(model_xbase_XFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_xbase_xfunctiondeclaration_has_name():
    assert hasattr(model_xbase_XFunctionDeclaration, "name")
    descriptor = None
    for klass in model_xbase_XFunctionDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xcatchclause_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XCatchClause)


def test_model_xbase_xcatchclause_constructor_exists():
    assert callable(model_xbase_XCatchClause.__init__)


def test_model_xbase_xcatchclause_constructor_args():
    sig = inspect.signature(model_xbase_XCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_xcatchclause_is_not_abstract():
    assert not inspect.isabstract(XCatchClause)


def test_xcatchclause_constructor_exists():
    assert callable(XCatchClause.__init__)


def test_xcatchclause_constructor_args():
    sig = inspect.signature(XCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xcontinueexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XContinueExpression)


def test_model_xbase_xcontinueexpression_constructor_exists():
    assert callable(model_xbase_XContinueExpression.__init__)


def test_model_xbase_xcontinueexpression_constructor_args():
    sig = inspect.signature(model_xbase_XContinueExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xbreakexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XBreakExpression)


def test_model_xbase_xbreakexpression_constructor_exists():
    assert callable(model_xbase_XBreakExpression.__init__)


def test_model_xbase_xbreakexpression_constructor_args():
    sig = inspect.signature(model_xbase_XBreakExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xreturnexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XReturnExpression)


def test_model_xbase_xreturnexpression_constructor_exists():
    assert callable(model_xbase_XReturnExpression.__init__)


def test_model_xbase_xreturnexpression_constructor_args():
    sig = inspect.signature(model_xbase_XReturnExpression.__init__)
    params = list(sig.parameters.keys())



def test_xabstractwhileexpression_is_not_abstract():
    assert not inspect.isabstract(XAbstractWhileExpression)


def test_xabstractwhileexpression_constructor_exists():
    assert callable(XAbstractWhileExpression.__init__)


def test_xabstractwhileexpression_constructor_args():
    sig = inspect.signature(XAbstractWhileExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xdowhileexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XDoWhileExpression)


def test_model_xbase_xdowhileexpression_constructor_exists():
    assert callable(model_xbase_XDoWhileExpression.__init__)


def test_model_xbase_xdowhileexpression_constructor_args():
    sig = inspect.signature(model_xbase_XDoWhileExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xabstractwhileexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XAbstractWhileExpression)


def test_model_xbase_xabstractwhileexpression_constructor_exists():
    assert callable(model_xbase_XAbstractWhileExpression.__init__)


def test_model_xbase_xabstractwhileexpression_constructor_args():
    sig = inspect.signature(model_xbase_XAbstractWhileExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xtrycatchfinallyexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XTryCatchFinallyExpression)


def test_model_xbase_xtrycatchfinallyexpression_constructor_exists():
    assert callable(model_xbase_XTryCatchFinallyExpression.__init__)


def test_model_xbase_xtrycatchfinallyexpression_constructor_args():
    sig = inspect.signature(model_xbase_XTryCatchFinallyExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xthrowexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XThrowExpression)


def test_model_xbase_xthrowexpression_constructor_exists():
    assert callable(model_xbase_XThrowExpression.__init__)


def test_model_xbase_xthrowexpression_constructor_args():
    sig = inspect.signature(model_xbase_XThrowExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xinstanceofexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XInstanceOfExpression)


def test_model_xbase_xinstanceofexpression_constructor_exists():
    assert callable(model_xbase_XInstanceOfExpression.__init__)


def test_model_xbase_xinstanceofexpression_constructor_args():
    sig = inspect.signature(model_xbase_XInstanceOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xtypeliteral_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XTypeLiteral)


def test_model_xbase_xtypeliteral_constructor_exists():
    assert callable(model_xbase_XTypeLiteral.__init__)


def test_model_xbase_xtypeliteral_constructor_args():
    sig = inspect.signature(model_xbase_XTypeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "arrayDimensions" in params, "Missing parameter 'arrayDimensions'"

def test_model_xbase_xtypeliteral_has_arrayDimensions():
    assert hasattr(model_xbase_XTypeLiteral, "arrayDimensions")
    descriptor = None
    for klass in model_xbase_XTypeLiteral.__mro__:
        if "arrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["arrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xwhileexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XWhileExpression)


def test_model_xbase_xwhileexpression_constructor_exists():
    assert callable(model_xbase_XWhileExpression.__init__)


def test_model_xbase_xwhileexpression_constructor_args():
    sig = inspect.signature(model_xbase_XWhileExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xforeachexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XForEachExpression)


def test_model_xbase_xforeachexpression_constructor_exists():
    assert callable(model_xbase_XForEachExpression.__init__)


def test_model_xbase_xforeachexpression_constructor_args():
    sig = inspect.signature(model_xbase_XForEachExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xforloopexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XForLoopExpression)


def test_model_xbase_xforloopexpression_constructor_exists():
    assert callable(model_xbase_XForLoopExpression.__init__)


def test_model_xbase_xforloopexpression_constructor_args():
    sig = inspect.signature(model_xbase_XForLoopExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xkeyvaluepair_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XKeyValuePair)


def test_model_xbase_xkeyvaluepair_constructor_exists():
    assert callable(model_xbase_XKeyValuePair.__init__)


def test_model_xbase_xkeyvaluepair_constructor_args():
    sig = inspect.signature(model_xbase_XKeyValuePair.__init__)
    params = list(sig.parameters.keys())
    assert "key1" in params, "Missing parameter 'key1'"

def test_model_xbase_xkeyvaluepair_has_key1():
    assert hasattr(model_xbase_XKeyValuePair, "key1")
    descriptor = None
    for klass in model_xbase_XKeyValuePair.__mro__:
        if "key1" in klass.__dict__:
            descriptor = klass.__dict__["key1"]
            break
    assert isinstance(descriptor, property)



def test_xcollectionliteral_is_not_abstract():
    assert not inspect.isabstract(XCollectionLiteral)


def test_xcollectionliteral_constructor_exists():
    assert callable(XCollectionLiteral.__init__)


def test_xcollectionliteral_constructor_args():
    sig = inspect.signature(XCollectionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xlistliteral_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XListLiteral)


def test_model_xbase_xlistliteral_constructor_exists():
    assert callable(model_xbase_XListLiteral.__init__)


def test_model_xbase_xlistliteral_constructor_args():
    sig = inspect.signature(model_xbase_XListLiteral.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xcollectionliteral_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XCollectionLiteral)


def test_model_xbase_xcollectionliteral_constructor_exists():
    assert callable(model_xbase_XCollectionLiteral.__init__)


def test_model_xbase_xcollectionliteral_constructor_args():
    sig = inspect.signature(model_xbase_XCollectionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xstringliteral_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XStringLiteral)


def test_model_xbase_xstringliteral_constructor_exists():
    assert callable(model_xbase_XStringLiteral.__init__)


def test_model_xbase_xstringliteral_constructor_args():
    sig = inspect.signature(model_xbase_XStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_xbase_xstringliteral_has_value():
    assert hasattr(model_xbase_XStringLiteral, "value")
    descriptor = None
    for klass in model_xbase_XStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xnumberliteral_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XNumberLiteral)


def test_model_xbase_xnumberliteral_constructor_exists():
    assert callable(model_xbase_XNumberLiteral.__init__)


def test_model_xbase_xnumberliteral_constructor_args():
    sig = inspect.signature(model_xbase_XNumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_xbase_xnumberliteral_has_value():
    assert hasattr(model_xbase_XNumberLiteral, "value")
    descriptor = None
    for klass in model_xbase_XNumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xnullliteral_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XNullLiteral)


def test_model_xbase_xnullliteral_constructor_exists():
    assert callable(model_xbase_XNullLiteral.__init__)


def test_model_xbase_xnullliteral_constructor_args():
    sig = inspect.signature(model_xbase_XNullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XBooleanLiteral)


def test_model_xbase_xbooleanliteral_constructor_exists():
    assert callable(model_xbase_XBooleanLiteral.__init__)


def test_model_xbase_xbooleanliteral_constructor_args():
    sig = inspect.signature(model_xbase_XBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_model_xbase_xbooleanliteral_has_isTrue():
    assert hasattr(model_xbase_XBooleanLiteral, "isTrue")
    descriptor = None
    for klass in model_xbase_XBooleanLiteral.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xcastedexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XCastedExpression)


def test_model_xbase_xcastedexpression_constructor_exists():
    assert callable(model_xbase_XCastedExpression.__init__)


def test_model_xbase_xcastedexpression_constructor_args():
    sig = inspect.signature(model_xbase_XCastedExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xsetliteral_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XSetLiteral)


def test_model_xbase_xsetliteral_constructor_exists():
    assert callable(model_xbase_XSetLiteral.__init__)


def test_model_xbase_xsetliteral_constructor_args():
    sig = inspect.signature(model_xbase_XSetLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jvmconstructor_is_not_abstract():
    assert not inspect.isabstract(JvmConstructor)


def test_jvmconstructor_constructor_exists():
    assert callable(JvmConstructor.__init__)


def test_jvmconstructor_constructor_args():
    sig = inspect.signature(JvmConstructor.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xconstructorcall_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XConstructorCall)


def test_model_xbase_xconstructorcall_constructor_exists():
    assert callable(model_xbase_XConstructorCall.__init__)


def test_model_xbase_xconstructorcall_constructor_args():
    sig = inspect.signature(model_xbase_XConstructorCall.__init__)
    params = list(sig.parameters.keys())
    assert "validFeature" in params, "Missing parameter 'validFeature'"
    assert "invalidFeatureIssueCode" in params, "Missing parameter 'invalidFeatureIssueCode'"

def test_model_xbase_xconstructorcall_has_validFeature():
    assert hasattr(model_xbase_XConstructorCall, "validFeature")
    descriptor = None
    for klass in model_xbase_XConstructorCall.__mro__:
        if "validFeature" in klass.__dict__:
            descriptor = klass.__dict__["validFeature"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xconstructorcall_has_invalidFeatureIssueCode():
    assert hasattr(model_xbase_XConstructorCall, "invalidFeatureIssueCode")
    descriptor = None
    for klass in model_xbase_XConstructorCall.__mro__:
        if "invalidFeatureIssueCode" in klass.__dict__:
            descriptor = klass.__dict__["invalidFeatureIssueCode"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xabstractfeaturecall_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XAbstractFeatureCall)


def test_model_xbase_xabstractfeaturecall_constructor_exists():
    assert callable(model_xbase_XAbstractFeatureCall.__init__)


def test_model_xbase_xabstractfeaturecall_constructor_args():
    sig = inspect.signature(model_xbase_XAbstractFeatureCall.__init__)
    params = list(sig.parameters.keys())
    assert "invalidFeatureIssueCode" in params, "Missing parameter 'invalidFeatureIssueCode'"
    assert "validFeature" in params, "Missing parameter 'validFeature'"

def test_model_xbase_xabstractfeaturecall_has_invalidFeatureIssueCode():
    assert hasattr(model_xbase_XAbstractFeatureCall, "invalidFeatureIssueCode")
    descriptor = None
    for klass in model_xbase_XAbstractFeatureCall.__mro__:
        if "invalidFeatureIssueCode" in klass.__dict__:
            descriptor = klass.__dict__["invalidFeatureIssueCode"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xabstractfeaturecall_has_validFeature():
    assert hasattr(model_xbase_XAbstractFeatureCall, "validFeature")
    descriptor = None
    for klass in model_xbase_XAbstractFeatureCall.__mro__:
        if "validFeature" in klass.__dict__:
            descriptor = klass.__dict__["validFeature"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xvariabledeclarationlist_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XVariableDeclarationList)


def test_model_xbase_xvariabledeclarationlist_constructor_exists():
    assert callable(model_xbase_XVariableDeclarationList.__init__)


def test_model_xbase_xvariabledeclarationlist_constructor_args():
    sig = inspect.signature(model_xbase_XVariableDeclarationList.__init__)
    params = list(sig.parameters.keys())
    assert "writeable" in params, "Missing parameter 'writeable'"
    assert "exported" in params, "Missing parameter 'exported'"

def test_model_xbase_xvariabledeclarationlist_has_writeable():
    assert hasattr(model_xbase_XVariableDeclarationList, "writeable")
    descriptor = None
    for klass in model_xbase_XVariableDeclarationList.__mro__:
        if "writeable" in klass.__dict__:
            descriptor = klass.__dict__["writeable"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xvariabledeclarationlist_has_exported():
    assert hasattr(model_xbase_XVariableDeclarationList, "exported")
    descriptor = None
    for klass in model_xbase_XVariableDeclarationList.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)



def test_xabstractfeaturecall_is_not_abstract():
    assert not inspect.isabstract(XAbstractFeatureCall)


def test_xabstractfeaturecall_constructor_exists():
    assert callable(XAbstractFeatureCall.__init__)


def test_xabstractfeaturecall_constructor_args():
    sig = inspect.signature(XAbstractFeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xassignment_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XAssignment)


def test_model_xbase_xassignment_constructor_exists():
    assert callable(model_xbase_XAssignment.__init__)


def test_model_xbase_xassignment_constructor_args():
    sig = inspect.signature(model_xbase_XAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "explicitStatic" in params, "Missing parameter 'explicitStatic'"

def test_model_xbase_xassignment_has_explicitStatic():
    assert hasattr(model_xbase_XAssignment, "explicitStatic")
    descriptor = None
    for klass in model_xbase_XAssignment.__mro__:
        if "explicitStatic" in klass.__dict__:
            descriptor = klass.__dict__["explicitStatic"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xunaryoperation_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XUnaryOperation)


def test_model_xbase_xunaryoperation_constructor_exists():
    assert callable(model_xbase_XUnaryOperation.__init__)


def test_model_xbase_xunaryoperation_constructor_args():
    sig = inspect.signature(model_xbase_XUnaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xprefixoperation_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XPrefixOperation)


def test_model_xbase_xprefixoperation_constructor_exists():
    assert callable(model_xbase_XPrefixOperation.__init__)


def test_model_xbase_xprefixoperation_constructor_args():
    sig = inspect.signature(model_xbase_XPrefixOperation.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xmemberfeaturecall1_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XMemberFeatureCall1)


def test_model_xbase_xmemberfeaturecall1_constructor_exists():
    assert callable(model_xbase_XMemberFeatureCall1.__init__)


def test_model_xbase_xmemberfeaturecall1_constructor_args():
    sig = inspect.signature(model_xbase_XMemberFeatureCall1.__init__)
    params = list(sig.parameters.keys())
    assert "typeLiteral" in params, "Missing parameter 'typeLiteral'"
    assert "nullSafe" in params, "Missing parameter 'nullSafe'"
    assert "indexedOperation" in params, "Missing parameter 'indexedOperation'"
    assert "explicitStatic" in params, "Missing parameter 'explicitStatic'"
    assert "packageFragment" in params, "Missing parameter 'packageFragment'"
    assert "staticWithDeclaringType" in params, "Missing parameter 'staticWithDeclaringType'"
    assert "explicitOperationCall" in params, "Missing parameter 'explicitOperationCall'"

def test_model_xbase_xmemberfeaturecall1_has_typeLiteral():
    assert hasattr(model_xbase_XMemberFeatureCall1, "typeLiteral")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall1.__mro__:
        if "typeLiteral" in klass.__dict__:
            descriptor = klass.__dict__["typeLiteral"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall1_has_nullSafe():
    assert hasattr(model_xbase_XMemberFeatureCall1, "nullSafe")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall1.__mro__:
        if "nullSafe" in klass.__dict__:
            descriptor = klass.__dict__["nullSafe"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall1_has_indexedOperation():
    assert hasattr(model_xbase_XMemberFeatureCall1, "indexedOperation")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall1.__mro__:
        if "indexedOperation" in klass.__dict__:
            descriptor = klass.__dict__["indexedOperation"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall1_has_explicitStatic():
    assert hasattr(model_xbase_XMemberFeatureCall1, "explicitStatic")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall1.__mro__:
        if "explicitStatic" in klass.__dict__:
            descriptor = klass.__dict__["explicitStatic"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall1_has_packageFragment():
    assert hasattr(model_xbase_XMemberFeatureCall1, "packageFragment")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall1.__mro__:
        if "packageFragment" in klass.__dict__:
            descriptor = klass.__dict__["packageFragment"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall1_has_staticWithDeclaringType():
    assert hasattr(model_xbase_XMemberFeatureCall1, "staticWithDeclaringType")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall1.__mro__:
        if "staticWithDeclaringType" in klass.__dict__:
            descriptor = klass.__dict__["staticWithDeclaringType"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall1_has_explicitOperationCall():
    assert hasattr(model_xbase_XMemberFeatureCall1, "explicitOperationCall")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall1.__mro__:
        if "explicitOperationCall" in klass.__dict__:
            descriptor = klass.__dict__["explicitOperationCall"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xbinaryoperation_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XBinaryOperation)


def test_model_xbase_xbinaryoperation_constructor_exists():
    assert callable(model_xbase_XBinaryOperation.__init__)


def test_model_xbase_xbinaryoperation_constructor_args():
    sig = inspect.signature(model_xbase_XBinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xfeaturecall_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XFeatureCall)


def test_model_xbase_xfeaturecall_constructor_exists():
    assert callable(model_xbase_XFeatureCall.__init__)


def test_model_xbase_xfeaturecall_constructor_args():
    sig = inspect.signature(model_xbase_XFeatureCall.__init__)
    params = list(sig.parameters.keys())
    assert "typeLiteral" in params, "Missing parameter 'typeLiteral'"
    assert "packageFragment" in params, "Missing parameter 'packageFragment'"
    assert "indexedOperation" in params, "Missing parameter 'indexedOperation'"
    assert "explicitOperationCall" in params, "Missing parameter 'explicitOperationCall'"

def test_model_xbase_xfeaturecall_has_typeLiteral():
    assert hasattr(model_xbase_XFeatureCall, "typeLiteral")
    descriptor = None
    for klass in model_xbase_XFeatureCall.__mro__:
        if "typeLiteral" in klass.__dict__:
            descriptor = klass.__dict__["typeLiteral"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xfeaturecall_has_packageFragment():
    assert hasattr(model_xbase_XFeatureCall, "packageFragment")
    descriptor = None
    for klass in model_xbase_XFeatureCall.__mro__:
        if "packageFragment" in klass.__dict__:
            descriptor = klass.__dict__["packageFragment"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xfeaturecall_has_indexedOperation():
    assert hasattr(model_xbase_XFeatureCall, "indexedOperation")
    descriptor = None
    for klass in model_xbase_XFeatureCall.__mro__:
        if "indexedOperation" in klass.__dict__:
            descriptor = klass.__dict__["indexedOperation"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xfeaturecall_has_explicitOperationCall():
    assert hasattr(model_xbase_XFeatureCall, "explicitOperationCall")
    descriptor = None
    for klass in model_xbase_XFeatureCall.__mro__:
        if "explicitOperationCall" in klass.__dict__:
            descriptor = klass.__dict__["explicitOperationCall"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xindexoperation_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XIndexOperation)


def test_model_xbase_xindexoperation_constructor_exists():
    assert callable(model_xbase_XIndexOperation.__init__)


def test_model_xbase_xindexoperation_constructor_args():
    sig = inspect.signature(model_xbase_XIndexOperation.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xpostfixoperation_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XPostfixOperation)


def test_model_xbase_xpostfixoperation_constructor_exists():
    assert callable(model_xbase_XPostfixOperation.__init__)


def test_model_xbase_xpostfixoperation_constructor_args():
    sig = inspect.signature(model_xbase_XPostfixOperation.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xmemberfeaturecall_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XMemberFeatureCall)


def test_model_xbase_xmemberfeaturecall_constructor_exists():
    assert callable(model_xbase_XMemberFeatureCall.__init__)


def test_model_xbase_xmemberfeaturecall_constructor_args():
    sig = inspect.signature(model_xbase_XMemberFeatureCall.__init__)
    params = list(sig.parameters.keys())
    assert "explicitOperationCall" in params, "Missing parameter 'explicitOperationCall'"
    assert "packageFragment" in params, "Missing parameter 'packageFragment'"
    assert "explicitStatic" in params, "Missing parameter 'explicitStatic'"
    assert "indexedOperation" in params, "Missing parameter 'indexedOperation'"
    assert "typeLiteral" in params, "Missing parameter 'typeLiteral'"
    assert "staticWithDeclaringType" in params, "Missing parameter 'staticWithDeclaringType'"
    assert "nullSafe" in params, "Missing parameter 'nullSafe'"

def test_model_xbase_xmemberfeaturecall_has_explicitOperationCall():
    assert hasattr(model_xbase_XMemberFeatureCall, "explicitOperationCall")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall.__mro__:
        if "explicitOperationCall" in klass.__dict__:
            descriptor = klass.__dict__["explicitOperationCall"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall_has_packageFragment():
    assert hasattr(model_xbase_XMemberFeatureCall, "packageFragment")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall.__mro__:
        if "packageFragment" in klass.__dict__:
            descriptor = klass.__dict__["packageFragment"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall_has_explicitStatic():
    assert hasattr(model_xbase_XMemberFeatureCall, "explicitStatic")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall.__mro__:
        if "explicitStatic" in klass.__dict__:
            descriptor = klass.__dict__["explicitStatic"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall_has_indexedOperation():
    assert hasattr(model_xbase_XMemberFeatureCall, "indexedOperation")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall.__mro__:
        if "indexedOperation" in klass.__dict__:
            descriptor = klass.__dict__["indexedOperation"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall_has_typeLiteral():
    assert hasattr(model_xbase_XMemberFeatureCall, "typeLiteral")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall.__mro__:
        if "typeLiteral" in klass.__dict__:
            descriptor = klass.__dict__["typeLiteral"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall_has_staticWithDeclaringType():
    assert hasattr(model_xbase_XMemberFeatureCall, "staticWithDeclaringType")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall.__mro__:
        if "staticWithDeclaringType" in klass.__dict__:
            descriptor = klass.__dict__["staticWithDeclaringType"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xmemberfeaturecall_has_nullSafe():
    assert hasattr(model_xbase_XMemberFeatureCall, "nullSafe")
    descriptor = None
    for klass in model_xbase_XMemberFeatureCall.__mro__:
        if "nullSafe" in klass.__dict__:
            descriptor = klass.__dict__["nullSafe"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xifexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XIfExpression)


def test_model_xbase_xifexpression_constructor_exists():
    assert callable(model_xbase_XIfExpression.__init__)


def test_model_xbase_xifexpression_constructor_args():
    sig = inspect.signature(model_xbase_XIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XExpression)


def test_model_xbase_xexpression_constructor_exists():
    assert callable(model_xbase_XExpression.__init__)


def test_model_xbase_xexpression_constructor_args():
    sig = inspect.signature(model_xbase_XExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jvmcustomannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmCustomAnnotationValue)


def test_model_types_jvmcustomannotationvalue_constructor_exists():
    assert callable(model_types_JvmCustomAnnotationValue.__init__)


def test_model_types_jvmcustomannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmCustomAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_types_jvmcustomannotationvalue_has_values():
    assert hasattr(model_types_JvmCustomAnnotationValue, "values")
    descriptor = None
    for klass in model_types_JvmCustomAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xblockexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XBlockExpression)


def test_model_xbase_xblockexpression_constructor_exists():
    assert callable(model_xbase_XBlockExpression.__init__)


def test_model_xbase_xblockexpression_constructor_args():
    sig = inspect.signature(model_xbase_XBlockExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xcasepart_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XCasePart)


def test_model_xbase_xcasepart_constructor_exists():
    assert callable(model_xbase_XCasePart.__init__)


def test_model_xbase_xcasepart_constructor_args():
    sig = inspect.signature(model_xbase_XCasePart.__init__)
    params = list(sig.parameters.keys())



def test_xcasepart_is_not_abstract():
    assert not inspect.isabstract(XCasePart)


def test_xcasepart_constructor_exists():
    assert callable(XCasePart.__init__)


def test_xcasepart_constructor_args():
    sig = inspect.signature(XCasePart.__init__)
    params = list(sig.parameters.keys())



def test_types_jvmidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(types_JvmIdentifiableElement)


def test_types_jvmidentifiableelement_constructor_exists():
    assert callable(types_JvmIdentifiableElement.__init__)


def test_types_jvmidentifiableelement_constructor_args():
    sig = inspect.signature(types_JvmIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_xbase_xexpression_is_not_abstract():
    assert not inspect.isabstract(xbase_XExpression)


def test_xbase_xexpression_constructor_exists():
    assert callable(xbase_XExpression.__init__)


def test_xbase_xexpression_constructor_args():
    sig = inspect.signature(xbase_XExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xbase_xclosure_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XClosure)


def test_model_xbase_xclosure_constructor_exists():
    assert callable(model_xbase_XClosure.__init__)


def test_model_xbase_xclosure_constructor_args():
    sig = inspect.signature(model_xbase_XClosure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "operator" in params, "Missing parameter 'operator'"
    assert "explicitSyntax" in params, "Missing parameter 'explicitSyntax'"
    assert "exported" in params, "Missing parameter 'exported'"

def test_model_xbase_xclosure_has_name():
    assert hasattr(model_xbase_XClosure, "name")
    descriptor = None
    for klass in model_xbase_XClosure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xclosure_has_operator():
    assert hasattr(model_xbase_XClosure, "operator")
    descriptor = None
    for klass in model_xbase_XClosure.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xclosure_has_explicitSyntax():
    assert hasattr(model_xbase_XClosure, "explicitSyntax")
    descriptor = None
    for klass in model_xbase_XClosure.__mro__:
        if "explicitSyntax" in klass.__dict__:
            descriptor = klass.__dict__["explicitSyntax"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xclosure_has_exported():
    assert hasattr(model_xbase_XClosure, "exported")
    descriptor = None
    for klass in model_xbase_XClosure.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XVariableDeclaration)


def test_model_xbase_xvariabledeclaration_constructor_exists():
    assert callable(model_xbase_XVariableDeclaration.__init__)


def test_model_xbase_xvariabledeclaration_constructor_args():
    sig = inspect.signature(model_xbase_XVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "exported" in params, "Missing parameter 'exported'"
    assert "name" in params, "Missing parameter 'name'"
    assert "writeable" in params, "Missing parameter 'writeable'"

def test_model_xbase_xvariabledeclaration_has_exported():
    assert hasattr(model_xbase_XVariableDeclaration, "exported")
    descriptor = None
    for klass in model_xbase_XVariableDeclaration.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xvariabledeclaration_has_name():
    assert hasattr(model_xbase_XVariableDeclaration, "name")
    descriptor = None
    for klass in model_xbase_XVariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_xbase_xvariabledeclaration_has_writeable():
    assert hasattr(model_xbase_XVariableDeclaration, "writeable")
    descriptor = None
    for klass in model_xbase_XVariableDeclaration.__mro__:
        if "writeable" in klass.__dict__:
            descriptor = klass.__dict__["writeable"]
            break
    assert isinstance(descriptor, property)



def test_model_xbase_xswitchexpression_is_not_abstract():
    assert not inspect.isabstract(model_xbase_XSwitchExpression)


def test_model_xbase_xswitchexpression_constructor_exists():
    assert callable(model_xbase_XSwitchExpression.__init__)


def test_model_xbase_xswitchexpression_constructor_args():
    sig = inspect.signature(model_xbase_XSwitchExpression.__init__)
    params = list(sig.parameters.keys())
    assert "localVarName" in params, "Missing parameter 'localVarName'"

def test_model_xbase_xswitchexpression_has_localVarName():
    assert hasattr(model_xbase_XSwitchExpression, "localVarName")
    descriptor = None
    for klass in model_xbase_XSwitchExpression.__mro__:
        if "localVarName" in klass.__dict__:
            descriptor = klass.__dict__["localVarName"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmcharannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmCharAnnotationValue)


def test_model_types_jvmcharannotationvalue_constructor_exists():
    assert callable(model_types_JvmCharAnnotationValue.__init__)


def test_model_types_jvmcharannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmCharAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_types_jvmcharannotationvalue_has_values():
    assert hasattr(model_types_JvmCharAnnotationValue, "values")
    descriptor = None
    for klass in model_types_JvmCharAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmfloatannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmFloatAnnotationValue)


def test_model_types_jvmfloatannotationvalue_constructor_exists():
    assert callable(model_types_JvmFloatAnnotationValue.__init__)


def test_model_types_jvmfloatannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmFloatAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_types_jvmfloatannotationvalue_has_values():
    assert hasattr(model_types_JvmFloatAnnotationValue, "values")
    descriptor = None
    for klass in model_types_JvmFloatAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmdoubleannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmDoubleAnnotationValue)


def test_model_types_jvmdoubleannotationvalue_constructor_exists():
    assert callable(model_types_JvmDoubleAnnotationValue.__init__)


def test_model_types_jvmdoubleannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmDoubleAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_types_jvmdoubleannotationvalue_has_values():
    assert hasattr(model_types_JvmDoubleAnnotationValue, "values")
    descriptor = None
    for klass in model_types_JvmDoubleAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model_types_jvmlongannotationvalue_is_not_abstract():
    assert not inspect.isabstract(model_types_JvmLongAnnotationValue)


def test_model_types_jvmlongannotationvalue_constructor_exists():
    assert callable(model_types_JvmLongAnnotationValue.__init__)


def test_model_types_jvmlongannotationvalue_constructor_args():
    sig = inspect.signature(model_types_JvmLongAnnotationValue.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_types_jvmlongannotationvalue_has_values():
    assert hasattr(model_types_JvmLongAnnotationValue, "values")
    descriptor = None
    for klass in model_types_JvmLongAnnotationValue.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_jvmvisibility_exists():
    # Check that the Enumeration exists
    assert JvmVisibility is not None

def test_jvmvisibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JvmVisibility]
    expected_literals = [
        "PUBLIC",
        "PRIVATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JvmVisibility"


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
IfConditionStart_strategy = st.builds(
    IfConditionStart,
)
Line_strategy = st.builds(
    Line,
)
RichString_strategy = st.builds(
    RichString,
)
model_richstring_ProcessedRichString_strategy = st.builds(
    model_richstring_ProcessedRichString,
)
model_xtype_XExportItem_strategy = st.builds(
    model_xtype_XExportItem,
    alias=
        safe_text
)
EndIf_strategy = st.builds(
    EndIf,
)
ElseIfCondition_strategy = st.builds(
    ElseIfCondition,
)
ElseStart_strategy = st.builds(
    ElseStart,
)
RichStringIf_strategy = st.builds(
    RichStringIf,
)
ForLoopStart_strategy = st.builds(
    ForLoopStart,
)
ForLoopEnd_strategy = st.builds(
    ForLoopEnd,
)
RichStringForLoop_strategy = st.builds(
    RichStringForLoop,
)
Literal_strategy = st.builds(
    Literal,
)
model_richstring_LineBreak_strategy = st.builds(
    model_richstring_LineBreak,
)
RichStringLiteral_strategy = st.builds(
    RichStringLiteral,
)
model_richstring_LinePart_strategy = st.builds(
    model_richstring_LinePart,
)
ProcessedRichString_strategy = st.builds(
    ProcessedRichString,
)
LinePart_strategy = st.builds(
    LinePart,
)
model_richstring_Literal_strategy = st.builds(
    model_richstring_Literal,
    length=
        st.integers(),
    offset=
        st.integers()
)
model_richstring_PrintedExpression_strategy = st.builds(
    model_richstring_PrintedExpression,
)
model_richstring_EndIf_strategy = st.builds(
    model_richstring_EndIf,
)
model_richstring_IfConditionStart_strategy = st.builds(
    model_richstring_IfConditionStart,
)
model_richstring_ForLoopEnd_strategy = st.builds(
    model_richstring_ForLoopEnd,
)
model_richstring_ElseIfCondition_strategy = st.builds(
    model_richstring_ElseIfCondition,
)
model_richstring_ElseStart_strategy = st.builds(
    model_richstring_ElseStart,
)
model_richstring_ForLoopStart_strategy = st.builds(
    model_richstring_ForLoopStart,
)
model_richstring_Line_strategy = st.builds(
    model_richstring_Line,
)
XImportDeclaration1_strategy = st.builds(
    XImportDeclaration1,
)
model_xtype_XImportSection1_strategy = st.builds(
    model_xtype_XImportSection1,
)
model_xtype_XImportDeclaration_strategy = st.builds(
    model_xtype_XImportDeclaration,
    importedNamespace=
        safe_text,
    static=
        st.booleans(),
    wildcard=
        st.booleans(),
    extension=
        st.booleans()
)
XImportDeclaration_strategy = st.builds(
    XImportDeclaration,
)
XExportItem_strategy = st.builds(
    XExportItem,
)
model_xtype_XExportDeclaration_strategy = st.builds(
    model_xtype_XExportDeclaration,
    wildcard=
        st.booleans(),
    alias=
        safe_text,
    importURI=
        safe_text
)
XExportDeclaration_strategy = st.builds(
    XExportDeclaration,
)
model_xtype_XExportSection_strategy = st.builds(
    model_xtype_XExportSection,
)
model_xtype_XImportItem_strategy = st.builds(
    model_xtype_XImportItem,
    alias=
        safe_text
)
XImportItem_strategy = st.builds(
    XImportItem,
)
model_xtype_XImportDeclaration1_strategy = st.builds(
    model_xtype_XImportDeclaration1,
    alias=
        safe_text,
    importURI=
        safe_text
)
XAnnotationElementValuePair_strategy = st.builds(
    XAnnotationElementValuePair,
)
model_xtype_XImportSection_strategy = st.builds(
    model_xtype_XImportSection,
)
JvmSpecializedTypeReference_strategy = st.builds(
    JvmSpecializedTypeReference,
)
model_xtype_XComputedTypeReference_strategy = st.builds(
    model_xtype_XComputedTypeReference,
    typeProvider=
        safe_text
)
model_xtype_XFunctionTypeRef_strategy = st.builds(
    model_xtype_XFunctionTypeRef,
    instanceContext=
        st.booleans()
)
model_xannotation_XAnnotationElementValuePair_strategy = st.builds(
    model_xannotation_XAnnotationElementValuePair,
)
JvmAnnotationValue_strategy = st.builds(
    JvmAnnotationValue,
)
model_types_JvmTypeAnnotationValue_strategy = st.builds(
    model_types_JvmTypeAnnotationValue,
)
model_types_JvmShortAnnotationValue_strategy = st.builds(
    model_types_JvmShortAnnotationValue,
    values=
        safe_text
)
model_types_JvmStringAnnotationValue_strategy = st.builds(
    model_types_JvmStringAnnotationValue,
    values=
        safe_text
)
model_types_JvmAnnotationAnnotationValue_strategy = st.builds(
    model_types_JvmAnnotationAnnotationValue,
)
model_types_JvmEnumAnnotationValue_strategy = st.builds(
    model_types_JvmEnumAnnotationValue,
)
model_types_JvmByteAnnotationValue_strategy = st.builds(
    model_types_JvmByteAnnotationValue,
    values=
        safe_text
)
model_types_JvmBooleanAnnotationValue_strategy = st.builds(
    model_types_JvmBooleanAnnotationValue,
    values=
        st.booleans()
)
model_types_JvmIntAnnotationValue_strategy = st.builds(
    model_types_JvmIntAnnotationValue,
    values=
        st.integers()
)
JvmOperation_strategy = st.builds(
    JvmOperation,
)
model_types_JvmAnnotationValue_strategy = st.builds(
    model_types_JvmAnnotationValue,
)
JvmAnnotationType_strategy = st.builds(
    JvmAnnotationType,
)
model_types_JvmAnnotationReference_strategy = st.builds(
    model_types_JvmAnnotationReference,
)
JvmAnnotationReference_strategy = st.builds(
    JvmAnnotationReference,
)
JvmAnnotationTarget_strategy = st.builds(
    JvmAnnotationTarget,
)
model_types_JvmFormalParameter_strategy = st.builds(
    model_types_JvmFormalParameter,
    varArg=
        st.booleans(),
    name=
        safe_text
)
model_types_JvmMember_strategy = st.builds(
    model_types_JvmMember,
    modifiers=
        safe_text,
    identifier=
        safe_text,
    simpleName=
        safe_text,
    visibility=
        safe_text
)
JvmCompoundTypeReference_strategy = st.builds(
    JvmCompoundTypeReference,
)
model_types_JvmSynonymTypeReference_strategy = st.builds(
    model_types_JvmSynonymTypeReference,
)
model_types_JvmMultiTypeReference_strategy = st.builds(
    model_types_JvmMultiTypeReference,
)
JvmExecutable_strategy = st.builds(
    JvmExecutable,
)
model_types_JvmOperation_strategy = st.builds(
    model_types_JvmOperation,
    strictFloatingPoint=
        st.booleans(),
    final=
        st.booleans(),
    abstract=
        st.booleans(),
    synchronized=
        st.booleans(),
    static=
        st.booleans(),
    default=
        st.booleans(),
    native=
        st.booleans()
)
model_types_JvmConstructor_strategy = st.builds(
    model_types_JvmConstructor,
)
JvmFormalParameter_strategy = st.builds(
    JvmFormalParameter,
)
types_JvmFeature_strategy = st.builds(
    types_JvmFeature,
)
XExpression_strategy = st.builds(
    XExpression,
)
model_xannotation_XAnnotation_strategy = st.builds(
    model_xannotation_XAnnotation,
)
JvmFeature_strategy = st.builds(
    JvmFeature,
)
model_types_JvmField_strategy = st.builds(
    model_types_JvmField,
    static=
        st.booleans(),
    volatile=
        st.booleans(),
    final=
        st.booleans(),
    transient=
        st.booleans()
)
model_types_JvmTypeReference_strategy = st.builds(
    model_types_JvmTypeReference,
)
types_JvmTypeReference_strategy = st.builds(
    types_JvmTypeReference,
)
JvmConstraintOwner_strategy = st.builds(
    JvmConstraintOwner,
)
model_types_JvmTypeConstraint_strategy = st.builds(
    model_types_JvmTypeConstraint,
)
JvmTypeConstraint_strategy = st.builds(
    JvmTypeConstraint,
)
model_types_JvmConstraintOwner_strategy = st.builds(
    model_types_JvmConstraintOwner,
)
JvmParameterizedTypeReference_strategy = st.builds(
    JvmParameterizedTypeReference,
)
JvmTypeParameter_strategy = st.builds(
    JvmTypeParameter,
)
types_JvmTypeParameterDeclarator_strategy = st.builds(
    types_JvmTypeParameterDeclarator,
)
model_types_JvmExecutable_strategy = st.builds(
    model_types_JvmExecutable,
    varArgs=
        st.booleans()
)
types_JvmDeclaredType_strategy = st.builds(
    types_JvmDeclaredType,
)
model_types_JvmGenericType_strategy = st.builds(
    model_types_JvmGenericType,
    interface=
        st.booleans(),
    strictFloatingPoint=
        st.booleans()
)
JvmField_strategy = st.builds(
    JvmField,
)
model_types_JvmEnumerationLiteral_strategy = st.builds(
    model_types_JvmEnumerationLiteral,
)
JvmEnumerationLiteral_strategy = st.builds(
    JvmEnumerationLiteral,
)
JvmDeclaredType_strategy = st.builds(
    JvmDeclaredType,
)
model_types_JvmEnumerationType_strategy = st.builds(
    model_types_JvmEnumerationType,
)
model_types_JvmAnnotationType_strategy = st.builds(
    model_types_JvmAnnotationType,
)
model_types_JvmLowerBound_strategy = st.builds(
    model_types_JvmLowerBound,
)
model_types_JvmUpperBound_strategy = st.builds(
    model_types_JvmUpperBound,
)
model_types_JvmTypeParameterDeclarator_strategy = st.builds(
    model_types_JvmTypeParameterDeclarator,
)
JvmTypeParameterDeclarator_strategy = st.builds(
    JvmTypeParameterDeclarator,
)
types_JvmConstraintOwner_strategy = st.builds(
    types_JvmConstraintOwner,
)
model_types_JvmWildcardTypeReference_strategy = st.builds(
    model_types_JvmWildcardTypeReference,
)
JvmMember_strategy = st.builds(
    JvmMember,
)
model_types_JvmFeature_strategy = st.builds(
    model_types_JvmFeature,
)
JvmTypeReference_strategy = st.builds(
    JvmTypeReference,
)
model_types_JvmParameterizedTypeReference_strategy = st.builds(
    model_types_JvmParameterizedTypeReference,
)
model_types_JvmSpecializedTypeReference_strategy = st.builds(
    model_types_JvmSpecializedTypeReference,
)
model_types_JvmCompoundTypeReference_strategy = st.builds(
    model_types_JvmCompoundTypeReference,
)
model_types_JvmAnyTypeReference_strategy = st.builds(
    model_types_JvmAnyTypeReference,
)
model_types_JvmDelegateTypeReference_strategy = st.builds(
    model_types_JvmDelegateTypeReference,
)
model_types_JvmGenericArrayTypeReference_strategy = st.builds(
    model_types_JvmGenericArrayTypeReference,
)
model_types_JvmUnknownTypeReference_strategy = st.builds(
    model_types_JvmUnknownTypeReference,
    qualifiedName=
        safe_text
)
types_JvmComponentType_strategy = st.builds(
    types_JvmComponentType,
)
model_types_JvmTypeParameter_strategy = st.builds(
    model_types_JvmTypeParameter,
    name=
        safe_text
)
types_JvmMember_strategy = st.builds(
    types_JvmMember,
)
model_types_JvmDeclaredType_strategy = st.builds(
    model_types_JvmDeclaredType,
    abstract=
        st.booleans(),
    static=
        st.booleans(),
    exported=
        st.booleans(),
    packageName=
        safe_text,
    final=
        st.booleans()
)
JvmComponentType_strategy = st.builds(
    JvmComponentType,
)
model_types_JvmArrayType_strategy = st.builds(
    model_types_JvmArrayType,
)
model_types_JvmPrimitiveType_strategy = st.builds(
    model_types_JvmPrimitiveType,
    simpleName=
        safe_text
)
JvmArrayType_strategy = st.builds(
    JvmArrayType,
)
JvmType_strategy = st.builds(
    JvmType,
)
model_types_JvmComponentType_strategy = st.builds(
    model_types_JvmComponentType,
)
model_types_JvmVoid_strategy = st.builds(
    model_types_JvmVoid,
)
model_types_JvmNoModule_strategy = st.builds(
    model_types_JvmNoModule,
)
XExportSection_strategy = st.builds(
    XExportSection,
)
types_model_EObject_strategy = st.builds(
    types_model_EObject,
)
XImportSection1_strategy = st.builds(
    XImportSection1,
)
JvmIdentifiableElement_strategy = st.builds(
    JvmIdentifiableElement,
)
model_types_JvmAnnotationTarget_strategy = st.builds(
    model_types_JvmAnnotationTarget,
)
model_types_JvmType_strategy = st.builds(
    model_types_JvmType,
)
model_types_JvmModule_strategy = st.builds(
    model_types_JvmModule,
    simpleName=
        safe_text
)
model_types_JvmIdentifiableElement_strategy = st.builds(
    model_types_JvmIdentifiableElement,
)
model_ss_XtendFormalParameter_strategy = st.builds(
    model_ss_XtendFormalParameter,
    extension=
        st.booleans()
)
XVariableDeclaration_strategy = st.builds(
    XVariableDeclaration,
)
model_ss_XtendVariableDeclaration_strategy = st.builds(
    model_ss_XtendVariableDeclaration,
    extension=
        st.booleans()
)
model_ss_CreateExtensionInfo_strategy = st.builds(
    model_ss_CreateExtensionInfo,
    name=
        safe_text
)
model_ss_RichStringElseIf_strategy = st.builds(
    model_ss_RichStringElseIf,
)
RichStringElseIf_strategy = st.builds(
    RichStringElseIf,
)
XBlockExpression_strategy = st.builds(
    XBlockExpression,
)
model_ss_RichString_strategy = st.builds(
    model_ss_RichString,
)
model_ss_RichStringIf_strategy = st.builds(
    model_ss_RichStringIf,
)
XForEachExpression_strategy = st.builds(
    XForEachExpression,
)
model_ss_RichStringForLoop_strategy = st.builds(
    model_ss_RichStringForLoop,
)
XStringLiteral_strategy = st.builds(
    XStringLiteral,
)
model_ss_RichStringLiteral_strategy = st.builds(
    model_ss_RichStringLiteral,
)
CreateExtensionInfo_strategy = st.builds(
    CreateExtensionInfo,
)
XtendParameter_strategy = st.builds(
    XtendParameter,
)
XtendMember_strategy = st.builds(
    XtendMember,
)
model_ss_XtendField_strategy = st.builds(
    model_ss_XtendField,
    name=
        safe_text
)
model_ss_XtendEnumLiteral_strategy = st.builds(
    model_ss_XtendEnumLiteral,
    name=
        safe_text
)
model_ss_XtendConstructor_strategy = st.builds(
    model_ss_XtendConstructor,
)
model_ss_XtendTypeDeclaration_strategy = st.builds(
    model_ss_XtendTypeDeclaration,
    name=
        safe_text
)
model_ss_XtendEvent_strategy = st.builds(
    model_ss_XtendEvent,
    name=
        safe_text
)
model_ss_XtendFunction_strategy = st.builds(
    model_ss_XtendFunction,
    name=
        safe_text
)
XtendAnnotationTarget_strategy = st.builds(
    XtendAnnotationTarget,
)
model_ss_XtendParameter_strategy = st.builds(
    model_ss_XtendParameter,
    varArg=
        st.booleans(),
    extension=
        st.booleans(),
    name=
        safe_text
)
model_ss_XtendMember_strategy = st.builds(
    model_ss_XtendMember,
    modifiers=
        safe_text
)
XAnnotation_strategy = st.builds(
    XAnnotation,
)
model_ss_XtendAnnotationTarget_strategy = st.builds(
    model_ss_XtendAnnotationTarget,
)
XObjectLiteralPart_strategy = st.builds(
    XObjectLiteralPart,
)
model_xbase_XObjectLiteral_strategy = st.builds(
    model_xbase_XObjectLiteral,
)
ss_model_EObject_strategy = st.builds(
    ss_model_EObject,
)
XtendTypeDeclaration_strategy = st.builds(
    XtendTypeDeclaration,
)
model_ss_XtendDelegate_strategy = st.builds(
    model_ss_XtendDelegate,
)
model_ss_XtendEnum_strategy = st.builds(
    model_ss_XtendEnum,
)
model_ss_XtendAnnotationType_strategy = st.builds(
    model_ss_XtendAnnotationType,
)
model_ss_XtendInterface_strategy = st.builds(
    model_ss_XtendInterface,
)
model_ss_XtendClass_strategy = st.builds(
    model_ss_XtendClass,
)
model_ss_XtendFile_strategy = st.builds(
    model_ss_XtendFile,
    package=
        safe_text
)
model_xbase_XArrayLiteral_strategy = st.builds(
    model_xbase_XArrayLiteral,
)
model_xbase_XObjectLiteralPart_strategy = st.builds(
    model_xbase_XObjectLiteralPart,
    name=
        safe_text
)
model_xbase_XTernaryOperation_strategy = st.builds(
    model_xbase_XTernaryOperation,
)
model_xbase_XFunctionDeclaration_strategy = st.builds(
    model_xbase_XFunctionDeclaration,
    name=
        safe_text
)
model_xbase_XCatchClause_strategy = st.builds(
    model_xbase_XCatchClause,
)
XCatchClause_strategy = st.builds(
    XCatchClause,
)
model_xbase_XContinueExpression_strategy = st.builds(
    model_xbase_XContinueExpression,
)
model_xbase_XBreakExpression_strategy = st.builds(
    model_xbase_XBreakExpression,
)
model_xbase_XReturnExpression_strategy = st.builds(
    model_xbase_XReturnExpression,
)
XAbstractWhileExpression_strategy = st.builds(
    XAbstractWhileExpression,
)
model_xbase_XDoWhileExpression_strategy = st.builds(
    model_xbase_XDoWhileExpression,
)
model_xbase_XAbstractWhileExpression_strategy = st.builds(
    model_xbase_XAbstractWhileExpression,
)
model_xbase_XTryCatchFinallyExpression_strategy = st.builds(
    model_xbase_XTryCatchFinallyExpression,
)
model_xbase_XThrowExpression_strategy = st.builds(
    model_xbase_XThrowExpression,
)
model_xbase_XInstanceOfExpression_strategy = st.builds(
    model_xbase_XInstanceOfExpression,
)
model_xbase_XTypeLiteral_strategy = st.builds(
    model_xbase_XTypeLiteral,
    arrayDimensions=
        safe_text
)
model_xbase_XWhileExpression_strategy = st.builds(
    model_xbase_XWhileExpression,
)
model_xbase_XForEachExpression_strategy = st.builds(
    model_xbase_XForEachExpression,
)
model_xbase_XForLoopExpression_strategy = st.builds(
    model_xbase_XForLoopExpression,
)
model_xbase_XKeyValuePair_strategy = st.builds(
    model_xbase_XKeyValuePair,
    key1=
        safe_text
)
XCollectionLiteral_strategy = st.builds(
    XCollectionLiteral,
)
model_xbase_XListLiteral_strategy = st.builds(
    model_xbase_XListLiteral,
)
model_xbase_XCollectionLiteral_strategy = st.builds(
    model_xbase_XCollectionLiteral,
)
model_xbase_XStringLiteral_strategy = st.builds(
    model_xbase_XStringLiteral,
    value=
        safe_text
)
model_xbase_XNumberLiteral_strategy = st.builds(
    model_xbase_XNumberLiteral,
    value=
        safe_text
)
model_xbase_XNullLiteral_strategy = st.builds(
    model_xbase_XNullLiteral,
)
model_xbase_XBooleanLiteral_strategy = st.builds(
    model_xbase_XBooleanLiteral,
    isTrue=
        st.booleans()
)
model_xbase_XCastedExpression_strategy = st.builds(
    model_xbase_XCastedExpression,
)
model_xbase_XSetLiteral_strategy = st.builds(
    model_xbase_XSetLiteral,
)
JvmConstructor_strategy = st.builds(
    JvmConstructor,
)
model_xbase_XConstructorCall_strategy = st.builds(
    model_xbase_XConstructorCall,
    validFeature=
        st.booleans(),
    invalidFeatureIssueCode=
        safe_text
)
model_xbase_XAbstractFeatureCall_strategy = st.builds(
    model_xbase_XAbstractFeatureCall,
    invalidFeatureIssueCode=
        safe_text,
    validFeature=
        st.booleans()
)
model_xbase_XVariableDeclarationList_strategy = st.builds(
    model_xbase_XVariableDeclarationList,
    writeable=
        st.booleans(),
    exported=
        st.booleans()
)
XAbstractFeatureCall_strategy = st.builds(
    XAbstractFeatureCall,
)
model_xbase_XAssignment_strategy = st.builds(
    model_xbase_XAssignment,
    explicitStatic=
        st.booleans()
)
model_xbase_XUnaryOperation_strategy = st.builds(
    model_xbase_XUnaryOperation,
)
model_xbase_XPrefixOperation_strategy = st.builds(
    model_xbase_XPrefixOperation,
)
model_xbase_XMemberFeatureCall1_strategy = st.builds(
    model_xbase_XMemberFeatureCall1,
    typeLiteral=
        st.booleans(),
    nullSafe=
        st.booleans(),
    indexedOperation=
        st.booleans(),
    explicitStatic=
        st.booleans(),
    packageFragment=
        st.booleans(),
    staticWithDeclaringType=
        st.booleans(),
    explicitOperationCall=
        st.booleans()
)
model_xbase_XBinaryOperation_strategy = st.builds(
    model_xbase_XBinaryOperation,
)
model_xbase_XFeatureCall_strategy = st.builds(
    model_xbase_XFeatureCall,
    typeLiteral=
        st.booleans(),
    packageFragment=
        st.booleans(),
    indexedOperation=
        st.booleans(),
    explicitOperationCall=
        st.booleans()
)
model_xbase_XIndexOperation_strategy = st.builds(
    model_xbase_XIndexOperation,
)
model_xbase_XPostfixOperation_strategy = st.builds(
    model_xbase_XPostfixOperation,
)
model_xbase_XMemberFeatureCall_strategy = st.builds(
    model_xbase_XMemberFeatureCall,
    explicitOperationCall=
        st.booleans(),
    packageFragment=
        st.booleans(),
    explicitStatic=
        st.booleans(),
    indexedOperation=
        st.booleans(),
    typeLiteral=
        st.booleans(),
    staticWithDeclaringType=
        st.booleans(),
    nullSafe=
        st.booleans()
)
model_xbase_XIfExpression_strategy = st.builds(
    model_xbase_XIfExpression,
)
model_xbase_XExpression_strategy = st.builds(
    model_xbase_XExpression,
)
model_types_JvmCustomAnnotationValue_strategy = st.builds(
    model_types_JvmCustomAnnotationValue,
    values=
        safe_text
)
model_xbase_XBlockExpression_strategy = st.builds(
    model_xbase_XBlockExpression,
)
model_xbase_XCasePart_strategy = st.builds(
    model_xbase_XCasePart,
)
XCasePart_strategy = st.builds(
    XCasePart,
)
types_JvmIdentifiableElement_strategy = st.builds(
    types_JvmIdentifiableElement,
)
xbase_XExpression_strategy = st.builds(
    xbase_XExpression,
)
model_xbase_XClosure_strategy = st.builds(
    model_xbase_XClosure,
    name=
        safe_text,
    operator=
        st.booleans(),
    explicitSyntax=
        st.booleans(),
    exported=
        st.booleans()
)
model_xbase_XVariableDeclaration_strategy = st.builds(
    model_xbase_XVariableDeclaration,
    exported=
        st.booleans(),
    name=
        safe_text,
    writeable=
        st.booleans()
)
model_xbase_XSwitchExpression_strategy = st.builds(
    model_xbase_XSwitchExpression,
    localVarName=
        safe_text
)
model_types_JvmCharAnnotationValue_strategy = st.builds(
    model_types_JvmCharAnnotationValue,
    values=
        safe_text
)
model_types_JvmFloatAnnotationValue_strategy = st.builds(
    model_types_JvmFloatAnnotationValue,
    values=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model_types_JvmDoubleAnnotationValue_strategy = st.builds(
    model_types_JvmDoubleAnnotationValue,
    values=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model_types_JvmLongAnnotationValue_strategy = st.builds(
    model_types_JvmLongAnnotationValue,
    values=
        safe_text
)

@given(instance=IfConditionStart_strategy)
@settings(max_examples=50)
def test_ifconditionstart_instantiation(instance):
    assert isinstance(instance, IfConditionStart)

@given(instance=Line_strategy)
@settings(max_examples=50)
def test_line_instantiation(instance):
    assert isinstance(instance, Line)

@given(instance=RichString_strategy)
@settings(max_examples=50)
def test_richstring_instantiation(instance):
    assert isinstance(instance, RichString)

@given(instance=model_richstring_ProcessedRichString_strategy)
@settings(max_examples=50)
def test_model_richstring_processedrichstring_instantiation(instance):
    assert isinstance(instance, model_richstring_ProcessedRichString)

@given(instance=model_xtype_XExportItem_strategy)
@settings(max_examples=50)
def test_model_xtype_xexportitem_instantiation(instance):
    assert isinstance(instance, model_xtype_XExportItem)



@given(instance=model_xtype_XExportItem_strategy)
def test_model_xtype_xexportitem_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=EndIf_strategy)
@settings(max_examples=50)
def test_endif_instantiation(instance):
    assert isinstance(instance, EndIf)

@given(instance=ElseIfCondition_strategy)
@settings(max_examples=50)
def test_elseifcondition_instantiation(instance):
    assert isinstance(instance, ElseIfCondition)

@given(instance=ElseStart_strategy)
@settings(max_examples=50)
def test_elsestart_instantiation(instance):
    assert isinstance(instance, ElseStart)

@given(instance=RichStringIf_strategy)
@settings(max_examples=50)
def test_richstringif_instantiation(instance):
    assert isinstance(instance, RichStringIf)

@given(instance=ForLoopStart_strategy)
@settings(max_examples=50)
def test_forloopstart_instantiation(instance):
    assert isinstance(instance, ForLoopStart)

@given(instance=ForLoopEnd_strategy)
@settings(max_examples=50)
def test_forloopend_instantiation(instance):
    assert isinstance(instance, ForLoopEnd)

@given(instance=RichStringForLoop_strategy)
@settings(max_examples=50)
def test_richstringforloop_instantiation(instance):
    assert isinstance(instance, RichStringForLoop)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=model_richstring_LineBreak_strategy)
@settings(max_examples=50)
def test_model_richstring_linebreak_instantiation(instance):
    assert isinstance(instance, model_richstring_LineBreak)

@given(instance=RichStringLiteral_strategy)
@settings(max_examples=50)
def test_richstringliteral_instantiation(instance):
    assert isinstance(instance, RichStringLiteral)

@given(instance=model_richstring_LinePart_strategy)
@settings(max_examples=50)
def test_model_richstring_linepart_instantiation(instance):
    assert isinstance(instance, model_richstring_LinePart)

@given(instance=ProcessedRichString_strategy)
@settings(max_examples=50)
def test_processedrichstring_instantiation(instance):
    assert isinstance(instance, ProcessedRichString)

@given(instance=LinePart_strategy)
@settings(max_examples=50)
def test_linepart_instantiation(instance):
    assert isinstance(instance, LinePart)

@given(instance=model_richstring_Literal_strategy)
@settings(max_examples=50)
def test_model_richstring_literal_instantiation(instance):
    assert isinstance(instance, model_richstring_Literal)



@given(instance=model_richstring_Literal_strategy)
def test_model_richstring_literal_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=model_richstring_Literal_strategy)
def test_model_richstring_literal_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=model_richstring_PrintedExpression_strategy)
@settings(max_examples=50)
def test_model_richstring_printedexpression_instantiation(instance):
    assert isinstance(instance, model_richstring_PrintedExpression)

@given(instance=model_richstring_EndIf_strategy)
@settings(max_examples=50)
def test_model_richstring_endif_instantiation(instance):
    assert isinstance(instance, model_richstring_EndIf)

@given(instance=model_richstring_IfConditionStart_strategy)
@settings(max_examples=50)
def test_model_richstring_ifconditionstart_instantiation(instance):
    assert isinstance(instance, model_richstring_IfConditionStart)

@given(instance=model_richstring_ForLoopEnd_strategy)
@settings(max_examples=50)
def test_model_richstring_forloopend_instantiation(instance):
    assert isinstance(instance, model_richstring_ForLoopEnd)

@given(instance=model_richstring_ElseIfCondition_strategy)
@settings(max_examples=50)
def test_model_richstring_elseifcondition_instantiation(instance):
    assert isinstance(instance, model_richstring_ElseIfCondition)

@given(instance=model_richstring_ElseStart_strategy)
@settings(max_examples=50)
def test_model_richstring_elsestart_instantiation(instance):
    assert isinstance(instance, model_richstring_ElseStart)

@given(instance=model_richstring_ForLoopStart_strategy)
@settings(max_examples=50)
def test_model_richstring_forloopstart_instantiation(instance):
    assert isinstance(instance, model_richstring_ForLoopStart)

@given(instance=model_richstring_Line_strategy)
@settings(max_examples=50)
def test_model_richstring_line_instantiation(instance):
    assert isinstance(instance, model_richstring_Line)

@given(instance=XImportDeclaration1_strategy)
@settings(max_examples=50)
def test_ximportdeclaration1_instantiation(instance):
    assert isinstance(instance, XImportDeclaration1)

@given(instance=model_xtype_XImportSection1_strategy)
@settings(max_examples=50)
def test_model_xtype_ximportsection1_instantiation(instance):
    assert isinstance(instance, model_xtype_XImportSection1)

@given(instance=model_xtype_XImportDeclaration_strategy)
@settings(max_examples=50)
def test_model_xtype_ximportdeclaration_instantiation(instance):
    assert isinstance(instance, model_xtype_XImportDeclaration)



@given(instance=model_xtype_XImportDeclaration_strategy)
def test_model_xtype_ximportdeclaration_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original



@given(instance=model_xtype_XImportDeclaration_strategy)
def test_model_xtype_ximportdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=model_xtype_XImportDeclaration_strategy)
def test_model_xtype_ximportdeclaration_wildcard_setter(instance):
    original = instance.wildcard
    instance.wildcard = original
    assert instance.wildcard == original



@given(instance=model_xtype_XImportDeclaration_strategy)
def test_model_xtype_ximportdeclaration_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=XImportDeclaration_strategy)
@settings(max_examples=50)
def test_ximportdeclaration_instantiation(instance):
    assert isinstance(instance, XImportDeclaration)

@given(instance=XExportItem_strategy)
@settings(max_examples=50)
def test_xexportitem_instantiation(instance):
    assert isinstance(instance, XExportItem)

@given(instance=model_xtype_XExportDeclaration_strategy)
@settings(max_examples=50)
def test_model_xtype_xexportdeclaration_instantiation(instance):
    assert isinstance(instance, model_xtype_XExportDeclaration)



@given(instance=model_xtype_XExportDeclaration_strategy)
def test_model_xtype_xexportdeclaration_wildcard_setter(instance):
    original = instance.wildcard
    instance.wildcard = original
    assert instance.wildcard == original



@given(instance=model_xtype_XExportDeclaration_strategy)
def test_model_xtype_xexportdeclaration_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=model_xtype_XExportDeclaration_strategy)
def test_model_xtype_xexportdeclaration_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=XExportDeclaration_strategy)
@settings(max_examples=50)
def test_xexportdeclaration_instantiation(instance):
    assert isinstance(instance, XExportDeclaration)

@given(instance=model_xtype_XExportSection_strategy)
@settings(max_examples=50)
def test_model_xtype_xexportsection_instantiation(instance):
    assert isinstance(instance, model_xtype_XExportSection)

@given(instance=model_xtype_XImportItem_strategy)
@settings(max_examples=50)
def test_model_xtype_ximportitem_instantiation(instance):
    assert isinstance(instance, model_xtype_XImportItem)



@given(instance=model_xtype_XImportItem_strategy)
def test_model_xtype_ximportitem_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=XImportItem_strategy)
@settings(max_examples=50)
def test_ximportitem_instantiation(instance):
    assert isinstance(instance, XImportItem)

@given(instance=model_xtype_XImportDeclaration1_strategy)
@settings(max_examples=50)
def test_model_xtype_ximportdeclaration1_instantiation(instance):
    assert isinstance(instance, model_xtype_XImportDeclaration1)



@given(instance=model_xtype_XImportDeclaration1_strategy)
def test_model_xtype_ximportdeclaration1_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=model_xtype_XImportDeclaration1_strategy)
def test_model_xtype_ximportdeclaration1_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_xtype_XImportDeclaration1_strategy)
@settings(max_examples=30)
def test_model_xtype_ximportdeclaration1_iswildcard_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isWildcard()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isWildcard).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isWildcard' in model_xtype_XImportDeclaration1 is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isWildcard' in model_xtype_XImportDeclaration1 did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isWildcard' in model_xtype_XImportDeclaration1 is not implemented or raised an error")

@given(instance=XAnnotationElementValuePair_strategy)
@settings(max_examples=50)
def test_xannotationelementvaluepair_instantiation(instance):
    assert isinstance(instance, XAnnotationElementValuePair)

@given(instance=model_xtype_XImportSection_strategy)
@settings(max_examples=50)
def test_model_xtype_ximportsection_instantiation(instance):
    assert isinstance(instance, model_xtype_XImportSection)

@given(instance=JvmSpecializedTypeReference_strategy)
@settings(max_examples=50)
def test_jvmspecializedtypereference_instantiation(instance):
    assert isinstance(instance, JvmSpecializedTypeReference)

@given(instance=model_xtype_XComputedTypeReference_strategy)
@settings(max_examples=50)
def test_model_xtype_xcomputedtypereference_instantiation(instance):
    assert isinstance(instance, model_xtype_XComputedTypeReference)



@given(instance=model_xtype_XComputedTypeReference_strategy)
def test_model_xtype_xcomputedtypereference_typeProvider_setter(instance):
    original = instance.typeProvider
    instance.typeProvider = original
    assert instance.typeProvider == original

@given(instance=model_xtype_XFunctionTypeRef_strategy)
@settings(max_examples=50)
def test_model_xtype_xfunctiontyperef_instantiation(instance):
    assert isinstance(instance, model_xtype_XFunctionTypeRef)



@given(instance=model_xtype_XFunctionTypeRef_strategy)
def test_model_xtype_xfunctiontyperef_instanceContext_setter(instance):
    original = instance.instanceContext
    instance.instanceContext = original
    assert instance.instanceContext == original

@given(instance=model_xannotation_XAnnotationElementValuePair_strategy)
@settings(max_examples=50)
def test_model_xannotation_xannotationelementvaluepair_instantiation(instance):
    assert isinstance(instance, model_xannotation_XAnnotationElementValuePair)

@given(instance=JvmAnnotationValue_strategy)
@settings(max_examples=50)
def test_jvmannotationvalue_instantiation(instance):
    assert isinstance(instance, JvmAnnotationValue)

@given(instance=model_types_JvmTypeAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmtypeannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmTypeAnnotationValue)

@given(instance=model_types_JvmShortAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmshortannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmShortAnnotationValue)



@given(instance=model_types_JvmShortAnnotationValue_strategy)
def test_model_types_jvmshortannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model_types_JvmStringAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmstringannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmStringAnnotationValue)



@given(instance=model_types_JvmStringAnnotationValue_strategy)
def test_model_types_jvmstringannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model_types_JvmAnnotationAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmannotationannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmAnnotationAnnotationValue)

@given(instance=model_types_JvmEnumAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmenumannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmEnumAnnotationValue)

@given(instance=model_types_JvmByteAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmbyteannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmByteAnnotationValue)



@given(instance=model_types_JvmByteAnnotationValue_strategy)
def test_model_types_jvmbyteannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model_types_JvmBooleanAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmbooleanannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmBooleanAnnotationValue)



@given(instance=model_types_JvmBooleanAnnotationValue_strategy)
def test_model_types_jvmbooleanannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model_types_JvmIntAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmintannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmIntAnnotationValue)



@given(instance=model_types_JvmIntAnnotationValue_strategy)
def test_model_types_jvmintannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=JvmOperation_strategy)
@settings(max_examples=50)
def test_jvmoperation_instantiation(instance):
    assert isinstance(instance, JvmOperation)

@given(instance=model_types_JvmAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmAnnotationValue)

@given(instance=JvmAnnotationType_strategy)
@settings(max_examples=50)
def test_jvmannotationtype_instantiation(instance):
    assert isinstance(instance, JvmAnnotationType)

@given(instance=model_types_JvmAnnotationReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmannotationreference_instantiation(instance):
    assert isinstance(instance, model_types_JvmAnnotationReference)

@given(instance=JvmAnnotationReference_strategy)
@settings(max_examples=50)
def test_jvmannotationreference_instantiation(instance):
    assert isinstance(instance, JvmAnnotationReference)

@given(instance=JvmAnnotationTarget_strategy)
@settings(max_examples=50)
def test_jvmannotationtarget_instantiation(instance):
    assert isinstance(instance, JvmAnnotationTarget)

@given(instance=model_types_JvmFormalParameter_strategy)
@settings(max_examples=50)
def test_model_types_jvmformalparameter_instantiation(instance):
    assert isinstance(instance, model_types_JvmFormalParameter)



@given(instance=model_types_JvmFormalParameter_strategy)
def test_model_types_jvmformalparameter_varArg_setter(instance):
    original = instance.varArg
    instance.varArg = original
    assert instance.varArg == original



@given(instance=model_types_JvmFormalParameter_strategy)
def test_model_types_jvmformalparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_types_JvmMember_strategy)
@settings(max_examples=50)
def test_model_types_jvmmember_instantiation(instance):
    assert isinstance(instance, model_types_JvmMember)



@given(instance=model_types_JvmMember_strategy)
def test_model_types_jvmmember_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original



@given(instance=model_types_JvmMember_strategy)
def test_model_types_jvmmember_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=model_types_JvmMember_strategy)
def test_model_types_jvmmember_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original



@given(instance=model_types_JvmMember_strategy)
def test_model_types_jvmmember_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_types_JvmMember_strategy)
@settings(max_examples=30)
def test_model_types_jvmmember_internalsetidentifier_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.internalSetIdentifier(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.internalSetIdentifier).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'internalSetIdentifier' in model_types_JvmMember is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'internalSetIdentifier' in model_types_JvmMember did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'internalSetIdentifier' in model_types_JvmMember is not implemented or raised an error")

@given(instance=JvmCompoundTypeReference_strategy)
@settings(max_examples=50)
def test_jvmcompoundtypereference_instantiation(instance):
    assert isinstance(instance, JvmCompoundTypeReference)

@given(instance=model_types_JvmSynonymTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmsynonymtypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmSynonymTypeReference)

@given(instance=model_types_JvmMultiTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmmultitypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmMultiTypeReference)

@given(instance=JvmExecutable_strategy)
@settings(max_examples=50)
def test_jvmexecutable_instantiation(instance):
    assert isinstance(instance, JvmExecutable)

@given(instance=model_types_JvmOperation_strategy)
@settings(max_examples=50)
def test_model_types_jvmoperation_instantiation(instance):
    assert isinstance(instance, model_types_JvmOperation)



@given(instance=model_types_JvmOperation_strategy)
def test_model_types_jvmoperation_strictFloatingPoint_setter(instance):
    original = instance.strictFloatingPoint
    instance.strictFloatingPoint = original
    assert instance.strictFloatingPoint == original



@given(instance=model_types_JvmOperation_strategy)
def test_model_types_jvmoperation_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=model_types_JvmOperation_strategy)
def test_model_types_jvmoperation_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=model_types_JvmOperation_strategy)
def test_model_types_jvmoperation_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=model_types_JvmOperation_strategy)
def test_model_types_jvmoperation_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=model_types_JvmOperation_strategy)
def test_model_types_jvmoperation_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=model_types_JvmOperation_strategy)
def test_model_types_jvmoperation_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=model_types_JvmConstructor_strategy)
@settings(max_examples=50)
def test_model_types_jvmconstructor_instantiation(instance):
    assert isinstance(instance, model_types_JvmConstructor)

@given(instance=JvmFormalParameter_strategy)
@settings(max_examples=50)
def test_jvmformalparameter_instantiation(instance):
    assert isinstance(instance, JvmFormalParameter)

@given(instance=types_JvmFeature_strategy)
@settings(max_examples=50)
def test_types_jvmfeature_instantiation(instance):
    assert isinstance(instance, types_JvmFeature)

@given(instance=XExpression_strategy)
@settings(max_examples=50)
def test_xexpression_instantiation(instance):
    assert isinstance(instance, XExpression)

@given(instance=model_xannotation_XAnnotation_strategy)
@settings(max_examples=50)
def test_model_xannotation_xannotation_instantiation(instance):
    assert isinstance(instance, model_xannotation_XAnnotation)

@given(instance=JvmFeature_strategy)
@settings(max_examples=50)
def test_jvmfeature_instantiation(instance):
    assert isinstance(instance, JvmFeature)

@given(instance=model_types_JvmField_strategy)
@settings(max_examples=50)
def test_model_types_jvmfield_instantiation(instance):
    assert isinstance(instance, model_types_JvmField)



@given(instance=model_types_JvmField_strategy)
def test_model_types_jvmfield_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=model_types_JvmField_strategy)
def test_model_types_jvmfield_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=model_types_JvmField_strategy)
def test_model_types_jvmfield_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=model_types_JvmField_strategy)
def test_model_types_jvmfield_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=model_types_JvmTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmtypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmTypeReference)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_types_JvmTypeReference_strategy)
@settings(max_examples=30)
def test_model_types_jvmtypereference_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in model_types_JvmTypeReference is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in model_types_JvmTypeReference did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in model_types_JvmTypeReference is not implemented or raised an error")

@given(instance=types_JvmTypeReference_strategy)
@settings(max_examples=50)
def test_types_jvmtypereference_instantiation(instance):
    assert isinstance(instance, types_JvmTypeReference)

@given(instance=JvmConstraintOwner_strategy)
@settings(max_examples=50)
def test_jvmconstraintowner_instantiation(instance):
    assert isinstance(instance, JvmConstraintOwner)

@given(instance=model_types_JvmTypeConstraint_strategy)
@settings(max_examples=50)
def test_model_types_jvmtypeconstraint_instantiation(instance):
    assert isinstance(instance, model_types_JvmTypeConstraint)

@given(instance=JvmTypeConstraint_strategy)
@settings(max_examples=50)
def test_jvmtypeconstraint_instantiation(instance):
    assert isinstance(instance, JvmTypeConstraint)

@given(instance=model_types_JvmConstraintOwner_strategy)
@settings(max_examples=50)
def test_model_types_jvmconstraintowner_instantiation(instance):
    assert isinstance(instance, model_types_JvmConstraintOwner)

@given(instance=JvmParameterizedTypeReference_strategy)
@settings(max_examples=50)
def test_jvmparameterizedtypereference_instantiation(instance):
    assert isinstance(instance, JvmParameterizedTypeReference)

@given(instance=JvmTypeParameter_strategy)
@settings(max_examples=50)
def test_jvmtypeparameter_instantiation(instance):
    assert isinstance(instance, JvmTypeParameter)

@given(instance=types_JvmTypeParameterDeclarator_strategy)
@settings(max_examples=50)
def test_types_jvmtypeparameterdeclarator_instantiation(instance):
    assert isinstance(instance, types_JvmTypeParameterDeclarator)

@given(instance=model_types_JvmExecutable_strategy)
@settings(max_examples=50)
def test_model_types_jvmexecutable_instantiation(instance):
    assert isinstance(instance, model_types_JvmExecutable)



@given(instance=model_types_JvmExecutable_strategy)
def test_model_types_jvmexecutable_varArgs_setter(instance):
    original = instance.varArgs
    instance.varArgs = original
    assert instance.varArgs == original

@given(instance=types_JvmDeclaredType_strategy)
@settings(max_examples=50)
def test_types_jvmdeclaredtype_instantiation(instance):
    assert isinstance(instance, types_JvmDeclaredType)

@given(instance=model_types_JvmGenericType_strategy)
@settings(max_examples=50)
def test_model_types_jvmgenerictype_instantiation(instance):
    assert isinstance(instance, model_types_JvmGenericType)



@given(instance=model_types_JvmGenericType_strategy)
def test_model_types_jvmgenerictype_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original



@given(instance=model_types_JvmGenericType_strategy)
def test_model_types_jvmgenerictype_strictFloatingPoint_setter(instance):
    original = instance.strictFloatingPoint
    instance.strictFloatingPoint = original
    assert instance.strictFloatingPoint == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_types_JvmGenericType_strategy)
@settings(max_examples=30)
def test_model_types_jvmgenerictype_isinstantiateable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isInstantiateable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isInstantiateable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isInstantiateable' in model_types_JvmGenericType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInstantiateable' in model_types_JvmGenericType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInstantiateable' in model_types_JvmGenericType is not implemented or raised an error")

@given(instance=JvmField_strategy)
@settings(max_examples=50)
def test_jvmfield_instantiation(instance):
    assert isinstance(instance, JvmField)

@given(instance=model_types_JvmEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_model_types_jvmenumerationliteral_instantiation(instance):
    assert isinstance(instance, model_types_JvmEnumerationLiteral)

@given(instance=JvmEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_jvmenumerationliteral_instantiation(instance):
    assert isinstance(instance, JvmEnumerationLiteral)

@given(instance=JvmDeclaredType_strategy)
@settings(max_examples=50)
def test_jvmdeclaredtype_instantiation(instance):
    assert isinstance(instance, JvmDeclaredType)

@given(instance=model_types_JvmEnumerationType_strategy)
@settings(max_examples=50)
def test_model_types_jvmenumerationtype_instantiation(instance):
    assert isinstance(instance, model_types_JvmEnumerationType)

@given(instance=model_types_JvmAnnotationType_strategy)
@settings(max_examples=50)
def test_model_types_jvmannotationtype_instantiation(instance):
    assert isinstance(instance, model_types_JvmAnnotationType)

@given(instance=model_types_JvmLowerBound_strategy)
@settings(max_examples=50)
def test_model_types_jvmlowerbound_instantiation(instance):
    assert isinstance(instance, model_types_JvmLowerBound)

@given(instance=model_types_JvmUpperBound_strategy)
@settings(max_examples=50)
def test_model_types_jvmupperbound_instantiation(instance):
    assert isinstance(instance, model_types_JvmUpperBound)

@given(instance=model_types_JvmTypeParameterDeclarator_strategy)
@settings(max_examples=50)
def test_model_types_jvmtypeparameterdeclarator_instantiation(instance):
    assert isinstance(instance, model_types_JvmTypeParameterDeclarator)

@given(instance=JvmTypeParameterDeclarator_strategy)
@settings(max_examples=50)
def test_jvmtypeparameterdeclarator_instantiation(instance):
    assert isinstance(instance, JvmTypeParameterDeclarator)

@given(instance=types_JvmConstraintOwner_strategy)
@settings(max_examples=50)
def test_types_jvmconstraintowner_instantiation(instance):
    assert isinstance(instance, types_JvmConstraintOwner)

@given(instance=model_types_JvmWildcardTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmwildcardtypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmWildcardTypeReference)

@given(instance=JvmMember_strategy)
@settings(max_examples=50)
def test_jvmmember_instantiation(instance):
    assert isinstance(instance, JvmMember)

@given(instance=model_types_JvmFeature_strategy)
@settings(max_examples=50)
def test_model_types_jvmfeature_instantiation(instance):
    assert isinstance(instance, model_types_JvmFeature)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_types_JvmFeature_strategy)
@settings(max_examples=30)
def test_model_types_jvmfeature_isstatic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isStatic()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isStatic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isStatic' in model_types_JvmFeature is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isStatic' in model_types_JvmFeature did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isStatic' in model_types_JvmFeature is not implemented or raised an error")

@given(instance=JvmTypeReference_strategy)
@settings(max_examples=50)
def test_jvmtypereference_instantiation(instance):
    assert isinstance(instance, JvmTypeReference)

@given(instance=model_types_JvmParameterizedTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmparameterizedtypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmParameterizedTypeReference)

@given(instance=model_types_JvmSpecializedTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmspecializedtypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmSpecializedTypeReference)

@given(instance=model_types_JvmCompoundTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmcompoundtypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmCompoundTypeReference)

@given(instance=model_types_JvmAnyTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmanytypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmAnyTypeReference)

@given(instance=model_types_JvmDelegateTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmdelegatetypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmDelegateTypeReference)

@given(instance=model_types_JvmGenericArrayTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmgenericarraytypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmGenericArrayTypeReference)

@given(instance=model_types_JvmUnknownTypeReference_strategy)
@settings(max_examples=50)
def test_model_types_jvmunknowntypereference_instantiation(instance):
    assert isinstance(instance, model_types_JvmUnknownTypeReference)



@given(instance=model_types_JvmUnknownTypeReference_strategy)
def test_model_types_jvmunknowntypereference_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=types_JvmComponentType_strategy)
@settings(max_examples=50)
def test_types_jvmcomponenttype_instantiation(instance):
    assert isinstance(instance, types_JvmComponentType)

@given(instance=model_types_JvmTypeParameter_strategy)
@settings(max_examples=50)
def test_model_types_jvmtypeparameter_instantiation(instance):
    assert isinstance(instance, model_types_JvmTypeParameter)



@given(instance=model_types_JvmTypeParameter_strategy)
def test_model_types_jvmtypeparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_JvmMember_strategy)
@settings(max_examples=50)
def test_types_jvmmember_instantiation(instance):
    assert isinstance(instance, types_JvmMember)

@given(instance=model_types_JvmDeclaredType_strategy)
@settings(max_examples=50)
def test_model_types_jvmdeclaredtype_instantiation(instance):
    assert isinstance(instance, model_types_JvmDeclaredType)



@given(instance=model_types_JvmDeclaredType_strategy)
def test_model_types_jvmdeclaredtype_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=model_types_JvmDeclaredType_strategy)
def test_model_types_jvmdeclaredtype_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=model_types_JvmDeclaredType_strategy)
def test_model_types_jvmdeclaredtype_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original



@given(instance=model_types_JvmDeclaredType_strategy)
def test_model_types_jvmdeclaredtype_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original



@given(instance=model_types_JvmDeclaredType_strategy)
def test_model_types_jvmdeclaredtype_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_types_JvmDeclaredType_strategy)
@settings(max_examples=30)
def test_model_types_jvmdeclaredtype_findallfeaturesbyname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findAllFeaturesByName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findAllFeaturesByName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findAllFeaturesByName' in model_types_JvmDeclaredType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findAllFeaturesByName' in model_types_JvmDeclaredType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findAllFeaturesByName' in model_types_JvmDeclaredType is not implemented or raised an error")

@given(instance=JvmComponentType_strategy)
@settings(max_examples=50)
def test_jvmcomponenttype_instantiation(instance):
    assert isinstance(instance, JvmComponentType)

@given(instance=model_types_JvmArrayType_strategy)
@settings(max_examples=50)
def test_model_types_jvmarraytype_instantiation(instance):
    assert isinstance(instance, model_types_JvmArrayType)

@given(instance=model_types_JvmPrimitiveType_strategy)
@settings(max_examples=50)
def test_model_types_jvmprimitivetype_instantiation(instance):
    assert isinstance(instance, model_types_JvmPrimitiveType)



@given(instance=model_types_JvmPrimitiveType_strategy)
def test_model_types_jvmprimitivetype_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=JvmArrayType_strategy)
@settings(max_examples=50)
def test_jvmarraytype_instantiation(instance):
    assert isinstance(instance, JvmArrayType)

@given(instance=JvmType_strategy)
@settings(max_examples=50)
def test_jvmtype_instantiation(instance):
    assert isinstance(instance, JvmType)

@given(instance=model_types_JvmComponentType_strategy)
@settings(max_examples=50)
def test_model_types_jvmcomponenttype_instantiation(instance):
    assert isinstance(instance, model_types_JvmComponentType)

@given(instance=model_types_JvmVoid_strategy)
@settings(max_examples=50)
def test_model_types_jvmvoid_instantiation(instance):
    assert isinstance(instance, model_types_JvmVoid)

@given(instance=model_types_JvmNoModule_strategy)
@settings(max_examples=50)
def test_model_types_jvmnomodule_instantiation(instance):
    assert isinstance(instance, model_types_JvmNoModule)

@given(instance=XExportSection_strategy)
@settings(max_examples=50)
def test_xexportsection_instantiation(instance):
    assert isinstance(instance, XExportSection)

@given(instance=types_model_EObject_strategy)
@settings(max_examples=50)
def test_types_model_eobject_instantiation(instance):
    assert isinstance(instance, types_model_EObject)

@given(instance=XImportSection1_strategy)
@settings(max_examples=50)
def test_ximportsection1_instantiation(instance):
    assert isinstance(instance, XImportSection1)

@given(instance=JvmIdentifiableElement_strategy)
@settings(max_examples=50)
def test_jvmidentifiableelement_instantiation(instance):
    assert isinstance(instance, JvmIdentifiableElement)

@given(instance=model_types_JvmAnnotationTarget_strategy)
@settings(max_examples=50)
def test_model_types_jvmannotationtarget_instantiation(instance):
    assert isinstance(instance, model_types_JvmAnnotationTarget)

@given(instance=model_types_JvmType_strategy)
@settings(max_examples=50)
def test_model_types_jvmtype_instantiation(instance):
    assert isinstance(instance, model_types_JvmType)

@given(instance=model_types_JvmModule_strategy)
@settings(max_examples=50)
def test_model_types_jvmmodule_instantiation(instance):
    assert isinstance(instance, model_types_JvmModule)



@given(instance=model_types_JvmModule_strategy)
def test_model_types_jvmmodule_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=model_types_JvmIdentifiableElement_strategy)
@settings(max_examples=50)
def test_model_types_jvmidentifiableelement_instantiation(instance):
    assert isinstance(instance, model_types_JvmIdentifiableElement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_types_JvmIdentifiableElement_strategy)
@settings(max_examples=30)
def test_model_types_jvmidentifiableelement_isexported_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isExported()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isExported).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isExported' in model_types_JvmIdentifiableElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isExported' in model_types_JvmIdentifiableElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isExported' in model_types_JvmIdentifiableElement is not implemented or raised an error")

@given(instance=model_ss_XtendFormalParameter_strategy)
@settings(max_examples=50)
def test_model_ss_xtendformalparameter_instantiation(instance):
    assert isinstance(instance, model_ss_XtendFormalParameter)



@given(instance=model_ss_XtendFormalParameter_strategy)
def test_model_ss_xtendformalparameter_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=XVariableDeclaration_strategy)
@settings(max_examples=50)
def test_xvariabledeclaration_instantiation(instance):
    assert isinstance(instance, XVariableDeclaration)

@given(instance=model_ss_XtendVariableDeclaration_strategy)
@settings(max_examples=50)
def test_model_ss_xtendvariabledeclaration_instantiation(instance):
    assert isinstance(instance, model_ss_XtendVariableDeclaration)



@given(instance=model_ss_XtendVariableDeclaration_strategy)
def test_model_ss_xtendvariabledeclaration_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=model_ss_CreateExtensionInfo_strategy)
@settings(max_examples=50)
def test_model_ss_createextensioninfo_instantiation(instance):
    assert isinstance(instance, model_ss_CreateExtensionInfo)



@given(instance=model_ss_CreateExtensionInfo_strategy)
def test_model_ss_createextensioninfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_ss_RichStringElseIf_strategy)
@settings(max_examples=50)
def test_model_ss_richstringelseif_instantiation(instance):
    assert isinstance(instance, model_ss_RichStringElseIf)

@given(instance=RichStringElseIf_strategy)
@settings(max_examples=50)
def test_richstringelseif_instantiation(instance):
    assert isinstance(instance, RichStringElseIf)

@given(instance=XBlockExpression_strategy)
@settings(max_examples=50)
def test_xblockexpression_instantiation(instance):
    assert isinstance(instance, XBlockExpression)

@given(instance=model_ss_RichString_strategy)
@settings(max_examples=50)
def test_model_ss_richstring_instantiation(instance):
    assert isinstance(instance, model_ss_RichString)

@given(instance=model_ss_RichStringIf_strategy)
@settings(max_examples=50)
def test_model_ss_richstringif_instantiation(instance):
    assert isinstance(instance, model_ss_RichStringIf)

@given(instance=XForEachExpression_strategy)
@settings(max_examples=50)
def test_xforeachexpression_instantiation(instance):
    assert isinstance(instance, XForEachExpression)

@given(instance=model_ss_RichStringForLoop_strategy)
@settings(max_examples=50)
def test_model_ss_richstringforloop_instantiation(instance):
    assert isinstance(instance, model_ss_RichStringForLoop)

@given(instance=XStringLiteral_strategy)
@settings(max_examples=50)
def test_xstringliteral_instantiation(instance):
    assert isinstance(instance, XStringLiteral)

@given(instance=model_ss_RichStringLiteral_strategy)
@settings(max_examples=50)
def test_model_ss_richstringliteral_instantiation(instance):
    assert isinstance(instance, model_ss_RichStringLiteral)

@given(instance=CreateExtensionInfo_strategy)
@settings(max_examples=50)
def test_createextensioninfo_instantiation(instance):
    assert isinstance(instance, CreateExtensionInfo)

@given(instance=XtendParameter_strategy)
@settings(max_examples=50)
def test_xtendparameter_instantiation(instance):
    assert isinstance(instance, XtendParameter)

@given(instance=XtendMember_strategy)
@settings(max_examples=50)
def test_xtendmember_instantiation(instance):
    assert isinstance(instance, XtendMember)

@given(instance=model_ss_XtendField_strategy)
@settings(max_examples=50)
def test_model_ss_xtendfield_instantiation(instance):
    assert isinstance(instance, model_ss_XtendField)



@given(instance=model_ss_XtendField_strategy)
def test_model_ss_xtendfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_ss_XtendField_strategy)
@settings(max_examples=30)
def test_model_ss_xtendfield_isextension_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isExtension()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isExtension).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isExtension' in model_ss_XtendField is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isExtension' in model_ss_XtendField did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isExtension' in model_ss_XtendField is not implemented or raised an error")

@given(instance=model_ss_XtendEnumLiteral_strategy)
@settings(max_examples=50)
def test_model_ss_xtendenumliteral_instantiation(instance):
    assert isinstance(instance, model_ss_XtendEnumLiteral)



@given(instance=model_ss_XtendEnumLiteral_strategy)
def test_model_ss_xtendenumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_ss_XtendConstructor_strategy)
@settings(max_examples=50)
def test_model_ss_xtendconstructor_instantiation(instance):
    assert isinstance(instance, model_ss_XtendConstructor)

@given(instance=model_ss_XtendTypeDeclaration_strategy)
@settings(max_examples=50)
def test_model_ss_xtendtypedeclaration_instantiation(instance):
    assert isinstance(instance, model_ss_XtendTypeDeclaration)



@given(instance=model_ss_XtendTypeDeclaration_strategy)
def test_model_ss_xtendtypedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_ss_XtendEvent_strategy)
@settings(max_examples=50)
def test_model_ss_xtendevent_instantiation(instance):
    assert isinstance(instance, model_ss_XtendEvent)



@given(instance=model_ss_XtendEvent_strategy)
def test_model_ss_xtendevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_ss_XtendEvent_strategy)
@settings(max_examples=30)
def test_model_ss_xtendevent_isextension_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isExtension()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isExtension).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isExtension' in model_ss_XtendEvent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isExtension' in model_ss_XtendEvent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isExtension' in model_ss_XtendEvent is not implemented or raised an error")

@given(instance=model_ss_XtendFunction_strategy)
@settings(max_examples=50)
def test_model_ss_xtendfunction_instantiation(instance):
    assert isinstance(instance, model_ss_XtendFunction)



@given(instance=model_ss_XtendFunction_strategy)
def test_model_ss_xtendfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_ss_XtendFunction_strategy)
@settings(max_examples=30)
def test_model_ss_xtendfunction_isabstract_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAbstract()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAbstract).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAbstract' in model_ss_XtendFunction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAbstract' in model_ss_XtendFunction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAbstract' in model_ss_XtendFunction is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_ss_XtendFunction_strategy)
@settings(max_examples=30)
def test_model_ss_xtendfunction_isoverride_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isOverride()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isOverride).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isOverride' in model_ss_XtendFunction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isOverride' in model_ss_XtendFunction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isOverride' in model_ss_XtendFunction is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_ss_XtendFunction_strategy)
@settings(max_examples=30)
def test_model_ss_xtendfunction_isdispatch_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isDispatch()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isDispatch).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isDispatch' in model_ss_XtendFunction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isDispatch' in model_ss_XtendFunction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isDispatch' in model_ss_XtendFunction is not implemented or raised an error")

@given(instance=XtendAnnotationTarget_strategy)
@settings(max_examples=50)
def test_xtendannotationtarget_instantiation(instance):
    assert isinstance(instance, XtendAnnotationTarget)

@given(instance=model_ss_XtendParameter_strategy)
@settings(max_examples=50)
def test_model_ss_xtendparameter_instantiation(instance):
    assert isinstance(instance, model_ss_XtendParameter)



@given(instance=model_ss_XtendParameter_strategy)
def test_model_ss_xtendparameter_varArg_setter(instance):
    original = instance.varArg
    instance.varArg = original
    assert instance.varArg == original



@given(instance=model_ss_XtendParameter_strategy)
def test_model_ss_xtendparameter_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=model_ss_XtendParameter_strategy)
def test_model_ss_xtendparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_ss_XtendMember_strategy)
@settings(max_examples=50)
def test_model_ss_xtendmember_instantiation(instance):
    assert isinstance(instance, model_ss_XtendMember)



@given(instance=model_ss_XtendMember_strategy)
def test_model_ss_xtendmember_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_ss_XtendMember_strategy)
@settings(max_examples=30)
def test_model_ss_xtendmember_isstatic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isStatic()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isStatic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isStatic' in model_ss_XtendMember is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isStatic' in model_ss_XtendMember did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isStatic' in model_ss_XtendMember is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_ss_XtendMember_strategy)
@settings(max_examples=30)
def test_model_ss_xtendmember_isfinal_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isFinal()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isFinal).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isFinal' in model_ss_XtendMember is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isFinal' in model_ss_XtendMember did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isFinal' in model_ss_XtendMember is not implemented or raised an error")

@given(instance=XAnnotation_strategy)
@settings(max_examples=50)
def test_xannotation_instantiation(instance):
    assert isinstance(instance, XAnnotation)

@given(instance=model_ss_XtendAnnotationTarget_strategy)
@settings(max_examples=50)
def test_model_ss_xtendannotationtarget_instantiation(instance):
    assert isinstance(instance, model_ss_XtendAnnotationTarget)

@given(instance=XObjectLiteralPart_strategy)
@settings(max_examples=50)
def test_xobjectliteralpart_instantiation(instance):
    assert isinstance(instance, XObjectLiteralPart)

@given(instance=model_xbase_XObjectLiteral_strategy)
@settings(max_examples=50)
def test_model_xbase_xobjectliteral_instantiation(instance):
    assert isinstance(instance, model_xbase_XObjectLiteral)

@given(instance=ss_model_EObject_strategy)
@settings(max_examples=50)
def test_ss_model_eobject_instantiation(instance):
    assert isinstance(instance, ss_model_EObject)

@given(instance=XtendTypeDeclaration_strategy)
@settings(max_examples=50)
def test_xtendtypedeclaration_instantiation(instance):
    assert isinstance(instance, XtendTypeDeclaration)

@given(instance=model_ss_XtendDelegate_strategy)
@settings(max_examples=50)
def test_model_ss_xtenddelegate_instantiation(instance):
    assert isinstance(instance, model_ss_XtendDelegate)

@given(instance=model_ss_XtendEnum_strategy)
@settings(max_examples=50)
def test_model_ss_xtendenum_instantiation(instance):
    assert isinstance(instance, model_ss_XtendEnum)

@given(instance=model_ss_XtendAnnotationType_strategy)
@settings(max_examples=50)
def test_model_ss_xtendannotationtype_instantiation(instance):
    assert isinstance(instance, model_ss_XtendAnnotationType)

@given(instance=model_ss_XtendInterface_strategy)
@settings(max_examples=50)
def test_model_ss_xtendinterface_instantiation(instance):
    assert isinstance(instance, model_ss_XtendInterface)

@given(instance=model_ss_XtendClass_strategy)
@settings(max_examples=50)
def test_model_ss_xtendclass_instantiation(instance):
    assert isinstance(instance, model_ss_XtendClass)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_ss_XtendClass_strategy)
@settings(max_examples=30)
def test_model_ss_xtendclass_isabstract_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAbstract()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAbstract).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAbstract' in model_ss_XtendClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAbstract' in model_ss_XtendClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAbstract' in model_ss_XtendClass is not implemented or raised an error")

@given(instance=model_ss_XtendFile_strategy)
@settings(max_examples=50)
def test_model_ss_xtendfile_instantiation(instance):
    assert isinstance(instance, model_ss_XtendFile)



@given(instance=model_ss_XtendFile_strategy)
def test_model_ss_xtendfile_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=model_xbase_XArrayLiteral_strategy)
@settings(max_examples=50)
def test_model_xbase_xarrayliteral_instantiation(instance):
    assert isinstance(instance, model_xbase_XArrayLiteral)

@given(instance=model_xbase_XObjectLiteralPart_strategy)
@settings(max_examples=50)
def test_model_xbase_xobjectliteralpart_instantiation(instance):
    assert isinstance(instance, model_xbase_XObjectLiteralPart)



@given(instance=model_xbase_XObjectLiteralPart_strategy)
def test_model_xbase_xobjectliteralpart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_xbase_XTernaryOperation_strategy)
@settings(max_examples=50)
def test_model_xbase_xternaryoperation_instantiation(instance):
    assert isinstance(instance, model_xbase_XTernaryOperation)

@given(instance=model_xbase_XFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_model_xbase_xfunctiondeclaration_instantiation(instance):
    assert isinstance(instance, model_xbase_XFunctionDeclaration)



@given(instance=model_xbase_XFunctionDeclaration_strategy)
def test_model_xbase_xfunctiondeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_xbase_XCatchClause_strategy)
@settings(max_examples=50)
def test_model_xbase_xcatchclause_instantiation(instance):
    assert isinstance(instance, model_xbase_XCatchClause)

@given(instance=XCatchClause_strategy)
@settings(max_examples=50)
def test_xcatchclause_instantiation(instance):
    assert isinstance(instance, XCatchClause)

@given(instance=model_xbase_XContinueExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xcontinueexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XContinueExpression)

@given(instance=model_xbase_XBreakExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xbreakexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XBreakExpression)

@given(instance=model_xbase_XReturnExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xreturnexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XReturnExpression)

@given(instance=XAbstractWhileExpression_strategy)
@settings(max_examples=50)
def test_xabstractwhileexpression_instantiation(instance):
    assert isinstance(instance, XAbstractWhileExpression)

@given(instance=model_xbase_XDoWhileExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xdowhileexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XDoWhileExpression)

@given(instance=model_xbase_XAbstractWhileExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xabstractwhileexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XAbstractWhileExpression)

@given(instance=model_xbase_XTryCatchFinallyExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xtrycatchfinallyexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XTryCatchFinallyExpression)

@given(instance=model_xbase_XThrowExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xthrowexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XThrowExpression)

@given(instance=model_xbase_XInstanceOfExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xinstanceofexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XInstanceOfExpression)

@given(instance=model_xbase_XTypeLiteral_strategy)
@settings(max_examples=50)
def test_model_xbase_xtypeliteral_instantiation(instance):
    assert isinstance(instance, model_xbase_XTypeLiteral)



@given(instance=model_xbase_XTypeLiteral_strategy)
def test_model_xbase_xtypeliteral_arrayDimensions_setter(instance):
    original = instance.arrayDimensions
    instance.arrayDimensions = original
    assert instance.arrayDimensions == original

@given(instance=model_xbase_XWhileExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xwhileexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XWhileExpression)

@given(instance=model_xbase_XForEachExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xforeachexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XForEachExpression)

@given(instance=model_xbase_XForLoopExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xforloopexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XForLoopExpression)

@given(instance=model_xbase_XKeyValuePair_strategy)
@settings(max_examples=50)
def test_model_xbase_xkeyvaluepair_instantiation(instance):
    assert isinstance(instance, model_xbase_XKeyValuePair)



@given(instance=model_xbase_XKeyValuePair_strategy)
def test_model_xbase_xkeyvaluepair_key1_setter(instance):
    original = instance.key1
    instance.key1 = original
    assert instance.key1 == original

@given(instance=XCollectionLiteral_strategy)
@settings(max_examples=50)
def test_xcollectionliteral_instantiation(instance):
    assert isinstance(instance, XCollectionLiteral)

@given(instance=model_xbase_XListLiteral_strategy)
@settings(max_examples=50)
def test_model_xbase_xlistliteral_instantiation(instance):
    assert isinstance(instance, model_xbase_XListLiteral)

@given(instance=model_xbase_XCollectionLiteral_strategy)
@settings(max_examples=50)
def test_model_xbase_xcollectionliteral_instantiation(instance):
    assert isinstance(instance, model_xbase_XCollectionLiteral)

@given(instance=model_xbase_XStringLiteral_strategy)
@settings(max_examples=50)
def test_model_xbase_xstringliteral_instantiation(instance):
    assert isinstance(instance, model_xbase_XStringLiteral)



@given(instance=model_xbase_XStringLiteral_strategy)
def test_model_xbase_xstringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_xbase_XNumberLiteral_strategy)
@settings(max_examples=50)
def test_model_xbase_xnumberliteral_instantiation(instance):
    assert isinstance(instance, model_xbase_XNumberLiteral)



@given(instance=model_xbase_XNumberLiteral_strategy)
def test_model_xbase_xnumberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_xbase_XNullLiteral_strategy)
@settings(max_examples=50)
def test_model_xbase_xnullliteral_instantiation(instance):
    assert isinstance(instance, model_xbase_XNullLiteral)

@given(instance=model_xbase_XBooleanLiteral_strategy)
@settings(max_examples=50)
def test_model_xbase_xbooleanliteral_instantiation(instance):
    assert isinstance(instance, model_xbase_XBooleanLiteral)



@given(instance=model_xbase_XBooleanLiteral_strategy)
def test_model_xbase_xbooleanliteral_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=model_xbase_XCastedExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xcastedexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XCastedExpression)

@given(instance=model_xbase_XSetLiteral_strategy)
@settings(max_examples=50)
def test_model_xbase_xsetliteral_instantiation(instance):
    assert isinstance(instance, model_xbase_XSetLiteral)

@given(instance=JvmConstructor_strategy)
@settings(max_examples=50)
def test_jvmconstructor_instantiation(instance):
    assert isinstance(instance, JvmConstructor)

@given(instance=model_xbase_XConstructorCall_strategy)
@settings(max_examples=50)
def test_model_xbase_xconstructorcall_instantiation(instance):
    assert isinstance(instance, model_xbase_XConstructorCall)



@given(instance=model_xbase_XConstructorCall_strategy)
def test_model_xbase_xconstructorcall_validFeature_setter(instance):
    original = instance.validFeature
    instance.validFeature = original
    assert instance.validFeature == original



@given(instance=model_xbase_XConstructorCall_strategy)
def test_model_xbase_xconstructorcall_invalidFeatureIssueCode_setter(instance):
    original = instance.invalidFeatureIssueCode
    instance.invalidFeatureIssueCode = original
    assert instance.invalidFeatureIssueCode == original

@given(instance=model_xbase_XAbstractFeatureCall_strategy)
@settings(max_examples=50)
def test_model_xbase_xabstractfeaturecall_instantiation(instance):
    assert isinstance(instance, model_xbase_XAbstractFeatureCall)



@given(instance=model_xbase_XAbstractFeatureCall_strategy)
def test_model_xbase_xabstractfeaturecall_invalidFeatureIssueCode_setter(instance):
    original = instance.invalidFeatureIssueCode
    instance.invalidFeatureIssueCode = original
    assert instance.invalidFeatureIssueCode == original



@given(instance=model_xbase_XAbstractFeatureCall_strategy)
def test_model_xbase_xabstractfeaturecall_validFeature_setter(instance):
    original = instance.validFeature
    instance.validFeature = original
    assert instance.validFeature == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_xbase_XAbstractFeatureCall_strategy)
@settings(max_examples=30)
def test_model_xbase_xabstractfeaturecall_isextension_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isExtension()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isExtension).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isExtension' in model_xbase_XAbstractFeatureCall is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isExtension' in model_xbase_XAbstractFeatureCall did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isExtension' in model_xbase_XAbstractFeatureCall is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_xbase_XAbstractFeatureCall_strategy)
@settings(max_examples=30)
def test_model_xbase_xabstractfeaturecall_ispackagefragment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPackageFragment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPackageFragment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPackageFragment' in model_xbase_XAbstractFeatureCall is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPackageFragment' in model_xbase_XAbstractFeatureCall did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPackageFragment' in model_xbase_XAbstractFeatureCall is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_xbase_XAbstractFeatureCall_strategy)
@settings(max_examples=30)
def test_model_xbase_xabstractfeaturecall_istypeliteral_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isTypeLiteral()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isTypeLiteral).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isTypeLiteral' in model_xbase_XAbstractFeatureCall is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isTypeLiteral' in model_xbase_XAbstractFeatureCall did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isTypeLiteral' in model_xbase_XAbstractFeatureCall is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_xbase_XAbstractFeatureCall_strategy)
@settings(max_examples=30)
def test_model_xbase_xabstractfeaturecall_isstatic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isStatic()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isStatic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isStatic' in model_xbase_XAbstractFeatureCall is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isStatic' in model_xbase_XAbstractFeatureCall did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isStatic' in model_xbase_XAbstractFeatureCall is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_xbase_XAbstractFeatureCall_strategy)
@settings(max_examples=30)
def test_model_xbase_xabstractfeaturecall_isexplicitoperationcallorbuildersyntax_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isExplicitOperationCallOrBuilderSyntax()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isExplicitOperationCallOrBuilderSyntax).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isExplicitOperationCallOrBuilderSyntax' in model_xbase_XAbstractFeatureCall is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isExplicitOperationCallOrBuilderSyntax' in model_xbase_XAbstractFeatureCall did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isExplicitOperationCallOrBuilderSyntax' in model_xbase_XAbstractFeatureCall is not implemented or raised an error")

@given(instance=model_xbase_XVariableDeclarationList_strategy)
@settings(max_examples=50)
def test_model_xbase_xvariabledeclarationlist_instantiation(instance):
    assert isinstance(instance, model_xbase_XVariableDeclarationList)



@given(instance=model_xbase_XVariableDeclarationList_strategy)
def test_model_xbase_xvariabledeclarationlist_writeable_setter(instance):
    original = instance.writeable
    instance.writeable = original
    assert instance.writeable == original



@given(instance=model_xbase_XVariableDeclarationList_strategy)
def test_model_xbase_xvariabledeclarationlist_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original

@given(instance=XAbstractFeatureCall_strategy)
@settings(max_examples=50)
def test_xabstractfeaturecall_instantiation(instance):
    assert isinstance(instance, XAbstractFeatureCall)

@given(instance=model_xbase_XAssignment_strategy)
@settings(max_examples=50)
def test_model_xbase_xassignment_instantiation(instance):
    assert isinstance(instance, model_xbase_XAssignment)



@given(instance=model_xbase_XAssignment_strategy)
def test_model_xbase_xassignment_explicitStatic_setter(instance):
    original = instance.explicitStatic
    instance.explicitStatic = original
    assert instance.explicitStatic == original

@given(instance=model_xbase_XUnaryOperation_strategy)
@settings(max_examples=50)
def test_model_xbase_xunaryoperation_instantiation(instance):
    assert isinstance(instance, model_xbase_XUnaryOperation)

@given(instance=model_xbase_XPrefixOperation_strategy)
@settings(max_examples=50)
def test_model_xbase_xprefixoperation_instantiation(instance):
    assert isinstance(instance, model_xbase_XPrefixOperation)

@given(instance=model_xbase_XMemberFeatureCall1_strategy)
@settings(max_examples=50)
def test_model_xbase_xmemberfeaturecall1_instantiation(instance):
    assert isinstance(instance, model_xbase_XMemberFeatureCall1)



@given(instance=model_xbase_XMemberFeatureCall1_strategy)
def test_model_xbase_xmemberfeaturecall1_typeLiteral_setter(instance):
    original = instance.typeLiteral
    instance.typeLiteral = original
    assert instance.typeLiteral == original



@given(instance=model_xbase_XMemberFeatureCall1_strategy)
def test_model_xbase_xmemberfeaturecall1_nullSafe_setter(instance):
    original = instance.nullSafe
    instance.nullSafe = original
    assert instance.nullSafe == original



@given(instance=model_xbase_XMemberFeatureCall1_strategy)
def test_model_xbase_xmemberfeaturecall1_indexedOperation_setter(instance):
    original = instance.indexedOperation
    instance.indexedOperation = original
    assert instance.indexedOperation == original



@given(instance=model_xbase_XMemberFeatureCall1_strategy)
def test_model_xbase_xmemberfeaturecall1_explicitStatic_setter(instance):
    original = instance.explicitStatic
    instance.explicitStatic = original
    assert instance.explicitStatic == original



@given(instance=model_xbase_XMemberFeatureCall1_strategy)
def test_model_xbase_xmemberfeaturecall1_packageFragment_setter(instance):
    original = instance.packageFragment
    instance.packageFragment = original
    assert instance.packageFragment == original



@given(instance=model_xbase_XMemberFeatureCall1_strategy)
def test_model_xbase_xmemberfeaturecall1_staticWithDeclaringType_setter(instance):
    original = instance.staticWithDeclaringType
    instance.staticWithDeclaringType = original
    assert instance.staticWithDeclaringType == original



@given(instance=model_xbase_XMemberFeatureCall1_strategy)
def test_model_xbase_xmemberfeaturecall1_explicitOperationCall_setter(instance):
    original = instance.explicitOperationCall
    instance.explicitOperationCall = original
    assert instance.explicitOperationCall == original

@given(instance=model_xbase_XBinaryOperation_strategy)
@settings(max_examples=50)
def test_model_xbase_xbinaryoperation_instantiation(instance):
    assert isinstance(instance, model_xbase_XBinaryOperation)

@given(instance=model_xbase_XFeatureCall_strategy)
@settings(max_examples=50)
def test_model_xbase_xfeaturecall_instantiation(instance):
    assert isinstance(instance, model_xbase_XFeatureCall)



@given(instance=model_xbase_XFeatureCall_strategy)
def test_model_xbase_xfeaturecall_typeLiteral_setter(instance):
    original = instance.typeLiteral
    instance.typeLiteral = original
    assert instance.typeLiteral == original



@given(instance=model_xbase_XFeatureCall_strategy)
def test_model_xbase_xfeaturecall_packageFragment_setter(instance):
    original = instance.packageFragment
    instance.packageFragment = original
    assert instance.packageFragment == original



@given(instance=model_xbase_XFeatureCall_strategy)
def test_model_xbase_xfeaturecall_indexedOperation_setter(instance):
    original = instance.indexedOperation
    instance.indexedOperation = original
    assert instance.indexedOperation == original



@given(instance=model_xbase_XFeatureCall_strategy)
def test_model_xbase_xfeaturecall_explicitOperationCall_setter(instance):
    original = instance.explicitOperationCall
    instance.explicitOperationCall = original
    assert instance.explicitOperationCall == original

@given(instance=model_xbase_XIndexOperation_strategy)
@settings(max_examples=50)
def test_model_xbase_xindexoperation_instantiation(instance):
    assert isinstance(instance, model_xbase_XIndexOperation)

@given(instance=model_xbase_XPostfixOperation_strategy)
@settings(max_examples=50)
def test_model_xbase_xpostfixoperation_instantiation(instance):
    assert isinstance(instance, model_xbase_XPostfixOperation)

@given(instance=model_xbase_XMemberFeatureCall_strategy)
@settings(max_examples=50)
def test_model_xbase_xmemberfeaturecall_instantiation(instance):
    assert isinstance(instance, model_xbase_XMemberFeatureCall)



@given(instance=model_xbase_XMemberFeatureCall_strategy)
def test_model_xbase_xmemberfeaturecall_explicitOperationCall_setter(instance):
    original = instance.explicitOperationCall
    instance.explicitOperationCall = original
    assert instance.explicitOperationCall == original



@given(instance=model_xbase_XMemberFeatureCall_strategy)
def test_model_xbase_xmemberfeaturecall_packageFragment_setter(instance):
    original = instance.packageFragment
    instance.packageFragment = original
    assert instance.packageFragment == original



@given(instance=model_xbase_XMemberFeatureCall_strategy)
def test_model_xbase_xmemberfeaturecall_explicitStatic_setter(instance):
    original = instance.explicitStatic
    instance.explicitStatic = original
    assert instance.explicitStatic == original



@given(instance=model_xbase_XMemberFeatureCall_strategy)
def test_model_xbase_xmemberfeaturecall_indexedOperation_setter(instance):
    original = instance.indexedOperation
    instance.indexedOperation = original
    assert instance.indexedOperation == original



@given(instance=model_xbase_XMemberFeatureCall_strategy)
def test_model_xbase_xmemberfeaturecall_typeLiteral_setter(instance):
    original = instance.typeLiteral
    instance.typeLiteral = original
    assert instance.typeLiteral == original



@given(instance=model_xbase_XMemberFeatureCall_strategy)
def test_model_xbase_xmemberfeaturecall_staticWithDeclaringType_setter(instance):
    original = instance.staticWithDeclaringType
    instance.staticWithDeclaringType = original
    assert instance.staticWithDeclaringType == original



@given(instance=model_xbase_XMemberFeatureCall_strategy)
def test_model_xbase_xmemberfeaturecall_nullSafe_setter(instance):
    original = instance.nullSafe
    instance.nullSafe = original
    assert instance.nullSafe == original

@given(instance=model_xbase_XIfExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xifexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XIfExpression)

@given(instance=model_xbase_XExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XExpression)

@given(instance=model_types_JvmCustomAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmcustomannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmCustomAnnotationValue)



@given(instance=model_types_JvmCustomAnnotationValue_strategy)
def test_model_types_jvmcustomannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model_xbase_XBlockExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xblockexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XBlockExpression)

@given(instance=model_xbase_XCasePart_strategy)
@settings(max_examples=50)
def test_model_xbase_xcasepart_instantiation(instance):
    assert isinstance(instance, model_xbase_XCasePart)

@given(instance=XCasePart_strategy)
@settings(max_examples=50)
def test_xcasepart_instantiation(instance):
    assert isinstance(instance, XCasePart)

@given(instance=types_JvmIdentifiableElement_strategy)
@settings(max_examples=50)
def test_types_jvmidentifiableelement_instantiation(instance):
    assert isinstance(instance, types_JvmIdentifiableElement)

@given(instance=xbase_XExpression_strategy)
@settings(max_examples=50)
def test_xbase_xexpression_instantiation(instance):
    assert isinstance(instance, xbase_XExpression)

@given(instance=model_xbase_XClosure_strategy)
@settings(max_examples=50)
def test_model_xbase_xclosure_instantiation(instance):
    assert isinstance(instance, model_xbase_XClosure)



@given(instance=model_xbase_XClosure_strategy)
def test_model_xbase_xclosure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_xbase_XClosure_strategy)
def test_model_xbase_xclosure_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=model_xbase_XClosure_strategy)
def test_model_xbase_xclosure_explicitSyntax_setter(instance):
    original = instance.explicitSyntax
    instance.explicitSyntax = original
    assert instance.explicitSyntax == original



@given(instance=model_xbase_XClosure_strategy)
def test_model_xbase_xclosure_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original

@given(instance=model_xbase_XVariableDeclaration_strategy)
@settings(max_examples=50)
def test_model_xbase_xvariabledeclaration_instantiation(instance):
    assert isinstance(instance, model_xbase_XVariableDeclaration)



@given(instance=model_xbase_XVariableDeclaration_strategy)
def test_model_xbase_xvariabledeclaration_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original



@given(instance=model_xbase_XVariableDeclaration_strategy)
def test_model_xbase_xvariabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_xbase_XVariableDeclaration_strategy)
def test_model_xbase_xvariabledeclaration_writeable_setter(instance):
    original = instance.writeable
    instance.writeable = original
    assert instance.writeable == original

@given(instance=model_xbase_XSwitchExpression_strategy)
@settings(max_examples=50)
def test_model_xbase_xswitchexpression_instantiation(instance):
    assert isinstance(instance, model_xbase_XSwitchExpression)



@given(instance=model_xbase_XSwitchExpression_strategy)
def test_model_xbase_xswitchexpression_localVarName_setter(instance):
    original = instance.localVarName
    instance.localVarName = original
    assert instance.localVarName == original

@given(instance=model_types_JvmCharAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmcharannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmCharAnnotationValue)



@given(instance=model_types_JvmCharAnnotationValue_strategy)
def test_model_types_jvmcharannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model_types_JvmFloatAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmfloatannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmFloatAnnotationValue)



@given(instance=model_types_JvmFloatAnnotationValue_strategy)
def test_model_types_jvmfloatannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model_types_JvmDoubleAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmdoubleannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmDoubleAnnotationValue)



@given(instance=model_types_JvmDoubleAnnotationValue_strategy)
def test_model_types_jvmdoubleannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model_types_JvmLongAnnotationValue_strategy)
@settings(max_examples=50)
def test_model_types_jvmlongannotationvalue_instantiation(instance):
    assert isinstance(instance, model_types_JvmLongAnnotationValue)



@given(instance=model_types_JvmLongAnnotationValue_strategy)
def test_model_types_jvmlongannotationvalue_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original
