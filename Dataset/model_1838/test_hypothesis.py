import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    mMDSL_MultiplicationExpression,
    mMDSL_CompareExpression,
    mMDSL_EqualExpression,
    mMDSL_AdditionExpression,
    mMDSL_AndExpression,
    mMDSL_OrExpression,
    mMDSL_AttributeSet,
    mMDSL_AttributeGet,
    mMDSL_RelationInstanceGetAll,
    mMDSL_RelationInstanceSet,
    mMDSL_RelationInstanceGet,
    mMDSL_RelationInstanceDelete,
    mMDSL_RelationInstanceCreate,
    mMDSL_ClassInstanceGetAll,
    mMDSL_ClassInstanceSet,
    mMDSL_ClassInstanceGet,
    mMDSL_ClassInstanceDelete,
    mMDSL_ClassInstanceCreate,
    mMDSL_RelationInstance,
    mMDSL_ClassInstance,
    mMDSL_ModelIsLoaded,
    mMDSL_ModelLoad,
    mMDSL_ModelSave,
    mMDSL_ModelDiscard,
    mMDSL_ModelDelete,
    mMDSL_ModelCreate,
    mMDSL_RemoveContextItem,
    mMDSL_InsertContextItem,
    mMDSL_RemoveMenuItem,
    mMDSL_InsertMenuItem,
    mMDSL_ContextItem,
    mMDSL_MenuItem,
    mMDSL_ItemOperation,
    mMDSL_ViewBox,
    mMDSL_WarningBox,
    mMDSL_ErrorBox,
    mMDSL_InfoBox,
    mMDSL_EditBox,
    mMDSL_DirList,
    mMDSL_DirDelete,
    mMDSL_DirCreate,
    mMDSL_DirGetWorking,
    mMDSL_DirSetWorking,
    mMDSL_FileWrite,
    mMDSL_FileRead,
    mMDSL_FileCreate,
    mMDSL_FileDelete,
    mMDSL_FileCopy,
    mMDSL_AttributeOperation,
    mMDSL_InstanceOperation,
    mMDSL_ModelOperation,
    mMDSL_SimpleUI,
    mMDSL_DirOperation,
    mMDSL_FileOperation,
    mMDSL_EObject,
    mMDSL_Expression,
    mMDSL_OperatorOr,
    mMDSL_OperatorAnd,
    mMDSL_OperatorEqual,
    mMDSL_OperatorCompare,
    mMDSL_OperatorAdd,
    mMDSL_OperatorMultiply,
    mMDSL_OperatorUnary,
    mMDSL_OperatorMultyAssign,
    mMDSL_VarStatement,
    mMDSL_OperatorAssign,
    mMDSL_BreakContinue,
    mMDSL_ForLoop,
    mMDSL_WhileLoop,
    mMDSL_Expr,
    mMDSL_AlgorithmOperation,
    mMDSL_Variable,
    mMDSL_LoopStatement,
    mMDSL_SelectionStatement,
    mMDSL_Statement,
    mMDSL_StrokeColor,
    mMDSL_PathParametersA,
    mMDSL_PathParametersQ,
    mMDSL_PathParametersS,
    mMDSL_PathParametersC,
    mMDSL_PathParametersHV,
    mMDSL_PathParametersMLT,
    mMDSL_EllipticalArc,
    mMDSL_SmoothQuadraticBezierCurveTo,
    mMDSL_QuadraticBezierCurve,
    mMDSL_SmoothCurveTo,
    mMDSL_CurveTo,
    mMDSL_VerticalLineTo,
    mMDSL_HorizontalLineTo,
    mMDSL_LineTo,
    mMDSL_MoveTo,
    mMDSL_FillColor,
    mMDSL_FontFamily,
    mMDSL_PathData,
    mMDSL_Points,
    mMDSL_Text,
    mMDSL_Path,
    mMDSL_Polygon,
    mMDSL_Polyline,
    mMDSL_Line,
    mMDSL_Ellipse,
    mMDSL_Circle,
    mMDSL_Rectangle,
    mMDSL_SVGCommand,
    mMDSL_Mode,
    mMDSL_EnumType,
    mMDSL_RefName,
    mMDSL_Type,
    mMDSL_Reference,
    mMDSL_ClassAttribute,
    mMDSL_ModelType,
    mMDSL_Attribute,
    mMDSL_Relation,
    mMDSL_Class,
    mMDSL_Event,
    mMDSL_Algorithm,
    mMDSL_Metamodel,
    mMDSL_SymbolRelation,
    mMDSL_SymbolClass,
    mMDSL_SymbolStyle,
    mMDSL_Enumeration,
    mMDSL_InsertEmbedCode,
    mMDSL_Method,
    mMDSL_EmbedCode,
    mMDSL_IncludeLibrary,
    mMDSL_EmbedCodeType,
    mMDSL_EmbedPlatformType,
    mMDSL_IncludeLibraryType,
    mMDSL_MethodName,
    mMDSL_Root,
    SimpleType,
    AttrGetParams,
    ButtonType,
    AttrSetParams,
    Color,
    Font,
    EventName,
    AccessType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_multiplicationexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL_MultiplicationExpression)


def test_mmdsl_multiplicationexpression_constructor_exists():
    assert callable(mMDSL_MultiplicationExpression.__init__)


def test_mmdsl_multiplicationexpression_constructor_args():
    sig = inspect.signature(mMDSL_MultiplicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_compareexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL_CompareExpression)


def test_mmdsl_compareexpression_constructor_exists():
    assert callable(mMDSL_CompareExpression.__init__)


def test_mmdsl_compareexpression_constructor_args():
    sig = inspect.signature(mMDSL_CompareExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_equalexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL_EqualExpression)


def test_mmdsl_equalexpression_constructor_exists():
    assert callable(mMDSL_EqualExpression.__init__)


def test_mmdsl_equalexpression_constructor_args():
    sig = inspect.signature(mMDSL_EqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_additionexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL_AdditionExpression)


def test_mmdsl_additionexpression_constructor_exists():
    assert callable(mMDSL_AdditionExpression.__init__)


def test_mmdsl_additionexpression_constructor_args():
    sig = inspect.signature(mMDSL_AdditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_andexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL_AndExpression)


def test_mmdsl_andexpression_constructor_exists():
    assert callable(mMDSL_AndExpression.__init__)


def test_mmdsl_andexpression_constructor_args():
    sig = inspect.signature(mMDSL_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_orexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL_OrExpression)


def test_mmdsl_orexpression_constructor_exists():
    assert callable(mMDSL_OrExpression.__init__)


def test_mmdsl_orexpression_constructor_args():
    sig = inspect.signature(mMDSL_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_attributeset_is_not_abstract():
    assert not inspect.isabstract(mMDSL_AttributeSet)


def test_mmdsl_attributeset_constructor_exists():
    assert callable(mMDSL_AttributeSet.__init__)


def test_mmdsl_attributeset_constructor_args():
    sig = inspect.signature(mMDSL_AttributeSet.__init__)
    params = list(sig.parameters.keys())
    assert "attrsetparams" in params, "Missing parameter 'attrsetparams'"
    assert "valueRealNumber" in params, "Missing parameter 'valueRealNumber'"
    assert "valueString" in params, "Missing parameter 'valueString'"

def test_mmdsl_attributeset_has_attrsetparams():
    assert hasattr(mMDSL_AttributeSet, "attrsetparams")
    descriptor = None
    for klass in mMDSL_AttributeSet.__mro__:
        if "attrsetparams" in klass.__dict__:
            descriptor = klass.__dict__["attrsetparams"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_attributeset_has_valueRealNumber():
    assert hasattr(mMDSL_AttributeSet, "valueRealNumber")
    descriptor = None
    for klass in mMDSL_AttributeSet.__mro__:
        if "valueRealNumber" in klass.__dict__:
            descriptor = klass.__dict__["valueRealNumber"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_attributeset_has_valueString():
    assert hasattr(mMDSL_AttributeSet, "valueString")
    descriptor = None
    for klass in mMDSL_AttributeSet.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_attributeget_is_not_abstract():
    assert not inspect.isabstract(mMDSL_AttributeGet)


def test_mmdsl_attributeget_constructor_exists():
    assert callable(mMDSL_AttributeGet.__init__)


def test_mmdsl_attributeget_constructor_args():
    sig = inspect.signature(mMDSL_AttributeGet.__init__)
    params = list(sig.parameters.keys())
    assert "attrgetparams" in params, "Missing parameter 'attrgetparams'"

def test_mmdsl_attributeget_has_attrgetparams():
    assert hasattr(mMDSL_AttributeGet, "attrgetparams")
    descriptor = None
    for klass in mMDSL_AttributeGet.__mro__:
        if "attrgetparams" in klass.__dict__:
            descriptor = klass.__dict__["attrgetparams"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_relationinstancegetall_is_not_abstract():
    assert not inspect.isabstract(mMDSL_RelationInstanceGetAll)


def test_mmdsl_relationinstancegetall_constructor_exists():
    assert callable(mMDSL_RelationInstanceGetAll.__init__)


def test_mmdsl_relationinstancegetall_constructor_args():
    sig = inspect.signature(mMDSL_RelationInstanceGetAll.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_relationinstanceset_is_not_abstract():
    assert not inspect.isabstract(mMDSL_RelationInstanceSet)


def test_mmdsl_relationinstanceset_constructor_exists():
    assert callable(mMDSL_RelationInstanceSet.__init__)


def test_mmdsl_relationinstanceset_constructor_args():
    sig = inspect.signature(mMDSL_RelationInstanceSet.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_relationinstanceget_is_not_abstract():
    assert not inspect.isabstract(mMDSL_RelationInstanceGet)


def test_mmdsl_relationinstanceget_constructor_exists():
    assert callable(mMDSL_RelationInstanceGet.__init__)


def test_mmdsl_relationinstanceget_constructor_args():
    sig = inspect.signature(mMDSL_RelationInstanceGet.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_relationinstancedelete_is_not_abstract():
    assert not inspect.isabstract(mMDSL_RelationInstanceDelete)


def test_mmdsl_relationinstancedelete_constructor_exists():
    assert callable(mMDSL_RelationInstanceDelete.__init__)


def test_mmdsl_relationinstancedelete_constructor_args():
    sig = inspect.signature(mMDSL_RelationInstanceDelete.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_relationinstancecreate_is_not_abstract():
    assert not inspect.isabstract(mMDSL_RelationInstanceCreate)


def test_mmdsl_relationinstancecreate_constructor_exists():
    assert callable(mMDSL_RelationInstanceCreate.__init__)


def test_mmdsl_relationinstancecreate_constructor_args():
    sig = inspect.signature(mMDSL_RelationInstanceCreate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_relationinstancecreate_has_name():
    assert hasattr(mMDSL_RelationInstanceCreate, "name")
    descriptor = None
    for klass in mMDSL_RelationInstanceCreate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_classinstancegetall_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ClassInstanceGetAll)


def test_mmdsl_classinstancegetall_constructor_exists():
    assert callable(mMDSL_ClassInstanceGetAll.__init__)


def test_mmdsl_classinstancegetall_constructor_args():
    sig = inspect.signature(mMDSL_ClassInstanceGetAll.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_classinstanceset_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ClassInstanceSet)


def test_mmdsl_classinstanceset_constructor_exists():
    assert callable(mMDSL_ClassInstanceSet.__init__)


def test_mmdsl_classinstanceset_constructor_args():
    sig = inspect.signature(mMDSL_ClassInstanceSet.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_classinstanceget_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ClassInstanceGet)


def test_mmdsl_classinstanceget_constructor_exists():
    assert callable(mMDSL_ClassInstanceGet.__init__)


def test_mmdsl_classinstanceget_constructor_args():
    sig = inspect.signature(mMDSL_ClassInstanceGet.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_classinstancedelete_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ClassInstanceDelete)


def test_mmdsl_classinstancedelete_constructor_exists():
    assert callable(mMDSL_ClassInstanceDelete.__init__)


def test_mmdsl_classinstancedelete_constructor_args():
    sig = inspect.signature(mMDSL_ClassInstanceDelete.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_classinstancecreate_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ClassInstanceCreate)


def test_mmdsl_classinstancecreate_constructor_exists():
    assert callable(mMDSL_ClassInstanceCreate.__init__)


def test_mmdsl_classinstancecreate_constructor_args():
    sig = inspect.signature(mMDSL_ClassInstanceCreate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_classinstancecreate_has_name():
    assert hasattr(mMDSL_ClassInstanceCreate, "name")
    descriptor = None
    for klass in mMDSL_ClassInstanceCreate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_relationinstance_is_not_abstract():
    assert not inspect.isabstract(mMDSL_RelationInstance)


def test_mmdsl_relationinstance_constructor_exists():
    assert callable(mMDSL_RelationInstance.__init__)


def test_mmdsl_relationinstance_constructor_args():
    sig = inspect.signature(mMDSL_RelationInstance.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_classinstance_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ClassInstance)


def test_mmdsl_classinstance_constructor_exists():
    assert callable(mMDSL_ClassInstance.__init__)


def test_mmdsl_classinstance_constructor_args():
    sig = inspect.signature(mMDSL_ClassInstance.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_modelisloaded_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ModelIsLoaded)


def test_mmdsl_modelisloaded_constructor_exists():
    assert callable(mMDSL_ModelIsLoaded.__init__)


def test_mmdsl_modelisloaded_constructor_args():
    sig = inspect.signature(mMDSL_ModelIsLoaded.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_modelload_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ModelLoad)


def test_mmdsl_modelload_constructor_exists():
    assert callable(mMDSL_ModelLoad.__init__)


def test_mmdsl_modelload_constructor_args():
    sig = inspect.signature(mMDSL_ModelLoad.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_modelsave_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ModelSave)


def test_mmdsl_modelsave_constructor_exists():
    assert callable(mMDSL_ModelSave.__init__)


def test_mmdsl_modelsave_constructor_args():
    sig = inspect.signature(mMDSL_ModelSave.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_modeldiscard_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ModelDiscard)


def test_mmdsl_modeldiscard_constructor_exists():
    assert callable(mMDSL_ModelDiscard.__init__)


def test_mmdsl_modeldiscard_constructor_args():
    sig = inspect.signature(mMDSL_ModelDiscard.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_modeldelete_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ModelDelete)


def test_mmdsl_modeldelete_constructor_exists():
    assert callable(mMDSL_ModelDelete.__init__)


def test_mmdsl_modeldelete_constructor_args():
    sig = inspect.signature(mMDSL_ModelDelete.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_modelcreate_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ModelCreate)


def test_mmdsl_modelcreate_constructor_exists():
    assert callable(mMDSL_ModelCreate.__init__)


def test_mmdsl_modelcreate_constructor_args():
    sig = inspect.signature(mMDSL_ModelCreate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_modelcreate_has_name():
    assert hasattr(mMDSL_ModelCreate, "name")
    descriptor = None
    for klass in mMDSL_ModelCreate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_removecontextitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL_RemoveContextItem)


def test_mmdsl_removecontextitem_constructor_exists():
    assert callable(mMDSL_RemoveContextItem.__init__)


def test_mmdsl_removecontextitem_constructor_args():
    sig = inspect.signature(mMDSL_RemoveContextItem.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_insertcontextitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL_InsertContextItem)


def test_mmdsl_insertcontextitem_constructor_exists():
    assert callable(mMDSL_InsertContextItem.__init__)


def test_mmdsl_insertcontextitem_constructor_args():
    sig = inspect.signature(mMDSL_InsertContextItem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "context" in params, "Missing parameter 'context'"

def test_mmdsl_insertcontextitem_has_name():
    assert hasattr(mMDSL_InsertContextItem, "name")
    descriptor = None
    for klass in mMDSL_InsertContextItem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_insertcontextitem_has_context():
    assert hasattr(mMDSL_InsertContextItem, "context")
    descriptor = None
    for klass in mMDSL_InsertContextItem.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_removemenuitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL_RemoveMenuItem)


def test_mmdsl_removemenuitem_constructor_exists():
    assert callable(mMDSL_RemoveMenuItem.__init__)


def test_mmdsl_removemenuitem_constructor_args():
    sig = inspect.signature(mMDSL_RemoveMenuItem.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_insertmenuitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL_InsertMenuItem)


def test_mmdsl_insertmenuitem_constructor_exists():
    assert callable(mMDSL_InsertMenuItem.__init__)


def test_mmdsl_insertmenuitem_constructor_args():
    sig = inspect.signature(mMDSL_InsertMenuItem.__init__)
    params = list(sig.parameters.keys())
    assert "menu" in params, "Missing parameter 'menu'"
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_insertmenuitem_has_menu():
    assert hasattr(mMDSL_InsertMenuItem, "menu")
    descriptor = None
    for klass in mMDSL_InsertMenuItem.__mro__:
        if "menu" in klass.__dict__:
            descriptor = klass.__dict__["menu"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_insertmenuitem_has_name():
    assert hasattr(mMDSL_InsertMenuItem, "name")
    descriptor = None
    for klass in mMDSL_InsertMenuItem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_contextitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ContextItem)


def test_mmdsl_contextitem_constructor_exists():
    assert callable(mMDSL_ContextItem.__init__)


def test_mmdsl_contextitem_constructor_args():
    sig = inspect.signature(mMDSL_ContextItem.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_menuitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL_MenuItem)


def test_mmdsl_menuitem_constructor_exists():
    assert callable(mMDSL_MenuItem.__init__)


def test_mmdsl_menuitem_constructor_args():
    sig = inspect.signature(mMDSL_MenuItem.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_itemoperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ItemOperation)


def test_mmdsl_itemoperation_constructor_exists():
    assert callable(mMDSL_ItemOperation.__init__)


def test_mmdsl_itemoperation_constructor_args():
    sig = inspect.signature(mMDSL_ItemOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_viewbox_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ViewBox)


def test_mmdsl_viewbox_constructor_exists():
    assert callable(mMDSL_ViewBox.__init__)


def test_mmdsl_viewbox_constructor_args():
    sig = inspect.signature(mMDSL_ViewBox.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "text" in params, "Missing parameter 'text'"

def test_mmdsl_viewbox_has_title():
    assert hasattr(mMDSL_ViewBox, "title")
    descriptor = None
    for klass in mMDSL_ViewBox.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_viewbox_has_text():
    assert hasattr(mMDSL_ViewBox, "text")
    descriptor = None
    for klass in mMDSL_ViewBox.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_warningbox_is_not_abstract():
    assert not inspect.isabstract(mMDSL_WarningBox)


def test_mmdsl_warningbox_constructor_exists():
    assert callable(mMDSL_WarningBox.__init__)


def test_mmdsl_warningbox_constructor_args():
    sig = inspect.signature(mMDSL_WarningBox.__init__)
    params = list(sig.parameters.keys())
    assert "buttontype" in params, "Missing parameter 'buttontype'"
    assert "title" in params, "Missing parameter 'title'"
    assert "text" in params, "Missing parameter 'text'"

def test_mmdsl_warningbox_has_buttontype():
    assert hasattr(mMDSL_WarningBox, "buttontype")
    descriptor = None
    for klass in mMDSL_WarningBox.__mro__:
        if "buttontype" in klass.__dict__:
            descriptor = klass.__dict__["buttontype"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_warningbox_has_title():
    assert hasattr(mMDSL_WarningBox, "title")
    descriptor = None
    for klass in mMDSL_WarningBox.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_warningbox_has_text():
    assert hasattr(mMDSL_WarningBox, "text")
    descriptor = None
    for klass in mMDSL_WarningBox.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_errorbox_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ErrorBox)


def test_mmdsl_errorbox_constructor_exists():
    assert callable(mMDSL_ErrorBox.__init__)


def test_mmdsl_errorbox_constructor_args():
    sig = inspect.signature(mMDSL_ErrorBox.__init__)
    params = list(sig.parameters.keys())
    assert "buttontype" in params, "Missing parameter 'buttontype'"
    assert "text" in params, "Missing parameter 'text'"
    assert "title" in params, "Missing parameter 'title'"

def test_mmdsl_errorbox_has_buttontype():
    assert hasattr(mMDSL_ErrorBox, "buttontype")
    descriptor = None
    for klass in mMDSL_ErrorBox.__mro__:
        if "buttontype" in klass.__dict__:
            descriptor = klass.__dict__["buttontype"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_errorbox_has_text():
    assert hasattr(mMDSL_ErrorBox, "text")
    descriptor = None
    for klass in mMDSL_ErrorBox.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_errorbox_has_title():
    assert hasattr(mMDSL_ErrorBox, "title")
    descriptor = None
    for klass in mMDSL_ErrorBox.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_infobox_is_not_abstract():
    assert not inspect.isabstract(mMDSL_InfoBox)


def test_mmdsl_infobox_constructor_exists():
    assert callable(mMDSL_InfoBox.__init__)


def test_mmdsl_infobox_constructor_args():
    sig = inspect.signature(mMDSL_InfoBox.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "title" in params, "Missing parameter 'title'"

def test_mmdsl_infobox_has_text():
    assert hasattr(mMDSL_InfoBox, "text")
    descriptor = None
    for klass in mMDSL_InfoBox.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_infobox_has_title():
    assert hasattr(mMDSL_InfoBox, "title")
    descriptor = None
    for klass in mMDSL_InfoBox.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_editbox_is_not_abstract():
    assert not inspect.isabstract(mMDSL_EditBox)


def test_mmdsl_editbox_constructor_exists():
    assert callable(mMDSL_EditBox.__init__)


def test_mmdsl_editbox_constructor_args():
    sig = inspect.signature(mMDSL_EditBox.__init__)
    params = list(sig.parameters.keys())
    assert "okbuttontext" in params, "Missing parameter 'okbuttontext'"
    assert "title" in params, "Missing parameter 'title'"
    assert "text" in params, "Missing parameter 'text'"

def test_mmdsl_editbox_has_okbuttontext():
    assert hasattr(mMDSL_EditBox, "okbuttontext")
    descriptor = None
    for klass in mMDSL_EditBox.__mro__:
        if "okbuttontext" in klass.__dict__:
            descriptor = klass.__dict__["okbuttontext"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_editbox_has_title():
    assert hasattr(mMDSL_EditBox, "title")
    descriptor = None
    for klass in mMDSL_EditBox.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_editbox_has_text():
    assert hasattr(mMDSL_EditBox, "text")
    descriptor = None
    for klass in mMDSL_EditBox.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_dirlist_is_not_abstract():
    assert not inspect.isabstract(mMDSL_DirList)


def test_mmdsl_dirlist_constructor_exists():
    assert callable(mMDSL_DirList.__init__)


def test_mmdsl_dirlist_constructor_args():
    sig = inspect.signature(mMDSL_DirList.__init__)
    params = list(sig.parameters.keys())
    assert "dirname" in params, "Missing parameter 'dirname'"

def test_mmdsl_dirlist_has_dirname():
    assert hasattr(mMDSL_DirList, "dirname")
    descriptor = None
    for klass in mMDSL_DirList.__mro__:
        if "dirname" in klass.__dict__:
            descriptor = klass.__dict__["dirname"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_dirdelete_is_not_abstract():
    assert not inspect.isabstract(mMDSL_DirDelete)


def test_mmdsl_dirdelete_constructor_exists():
    assert callable(mMDSL_DirDelete.__init__)


def test_mmdsl_dirdelete_constructor_args():
    sig = inspect.signature(mMDSL_DirDelete.__init__)
    params = list(sig.parameters.keys())
    assert "dirname" in params, "Missing parameter 'dirname'"

def test_mmdsl_dirdelete_has_dirname():
    assert hasattr(mMDSL_DirDelete, "dirname")
    descriptor = None
    for klass in mMDSL_DirDelete.__mro__:
        if "dirname" in klass.__dict__:
            descriptor = klass.__dict__["dirname"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_dircreate_is_not_abstract():
    assert not inspect.isabstract(mMDSL_DirCreate)


def test_mmdsl_dircreate_constructor_exists():
    assert callable(mMDSL_DirCreate.__init__)


def test_mmdsl_dircreate_constructor_args():
    sig = inspect.signature(mMDSL_DirCreate.__init__)
    params = list(sig.parameters.keys())
    assert "dirname" in params, "Missing parameter 'dirname'"

def test_mmdsl_dircreate_has_dirname():
    assert hasattr(mMDSL_DirCreate, "dirname")
    descriptor = None
    for klass in mMDSL_DirCreate.__mro__:
        if "dirname" in klass.__dict__:
            descriptor = klass.__dict__["dirname"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_dirgetworking_is_not_abstract():
    assert not inspect.isabstract(mMDSL_DirGetWorking)


def test_mmdsl_dirgetworking_constructor_exists():
    assert callable(mMDSL_DirGetWorking.__init__)


def test_mmdsl_dirgetworking_constructor_args():
    sig = inspect.signature(mMDSL_DirGetWorking.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_dirsetworking_is_not_abstract():
    assert not inspect.isabstract(mMDSL_DirSetWorking)


def test_mmdsl_dirsetworking_constructor_exists():
    assert callable(mMDSL_DirSetWorking.__init__)


def test_mmdsl_dirsetworking_constructor_args():
    sig = inspect.signature(mMDSL_DirSetWorking.__init__)
    params = list(sig.parameters.keys())
    assert "dirname" in params, "Missing parameter 'dirname'"

def test_mmdsl_dirsetworking_has_dirname():
    assert hasattr(mMDSL_DirSetWorking, "dirname")
    descriptor = None
    for klass in mMDSL_DirSetWorking.__mro__:
        if "dirname" in klass.__dict__:
            descriptor = klass.__dict__["dirname"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_filewrite_is_not_abstract():
    assert not inspect.isabstract(mMDSL_FileWrite)


def test_mmdsl_filewrite_constructor_exists():
    assert callable(mMDSL_FileWrite.__init__)


def test_mmdsl_filewrite_constructor_args():
    sig = inspect.signature(mMDSL_FileWrite.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "append" in params, "Missing parameter 'append'"
    assert "text" in params, "Missing parameter 'text'"

def test_mmdsl_filewrite_has_filename():
    assert hasattr(mMDSL_FileWrite, "filename")
    descriptor = None
    for klass in mMDSL_FileWrite.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_filewrite_has_append():
    assert hasattr(mMDSL_FileWrite, "append")
    descriptor = None
    for klass in mMDSL_FileWrite.__mro__:
        if "append" in klass.__dict__:
            descriptor = klass.__dict__["append"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_filewrite_has_text():
    assert hasattr(mMDSL_FileWrite, "text")
    descriptor = None
    for klass in mMDSL_FileWrite.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_fileread_is_not_abstract():
    assert not inspect.isabstract(mMDSL_FileRead)


def test_mmdsl_fileread_constructor_exists():
    assert callable(mMDSL_FileRead.__init__)


def test_mmdsl_fileread_constructor_args():
    sig = inspect.signature(mMDSL_FileRead.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_mmdsl_fileread_has_filename():
    assert hasattr(mMDSL_FileRead, "filename")
    descriptor = None
    for klass in mMDSL_FileRead.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_filecreate_is_not_abstract():
    assert not inspect.isabstract(mMDSL_FileCreate)


def test_mmdsl_filecreate_constructor_exists():
    assert callable(mMDSL_FileCreate.__init__)


def test_mmdsl_filecreate_constructor_args():
    sig = inspect.signature(mMDSL_FileCreate.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_mmdsl_filecreate_has_filename():
    assert hasattr(mMDSL_FileCreate, "filename")
    descriptor = None
    for klass in mMDSL_FileCreate.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_filedelete_is_not_abstract():
    assert not inspect.isabstract(mMDSL_FileDelete)


def test_mmdsl_filedelete_constructor_exists():
    assert callable(mMDSL_FileDelete.__init__)


def test_mmdsl_filedelete_constructor_args():
    sig = inspect.signature(mMDSL_FileDelete.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_mmdsl_filedelete_has_filename():
    assert hasattr(mMDSL_FileDelete, "filename")
    descriptor = None
    for klass in mMDSL_FileDelete.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_filecopy_is_not_abstract():
    assert not inspect.isabstract(mMDSL_FileCopy)


def test_mmdsl_filecopy_constructor_exists():
    assert callable(mMDSL_FileCopy.__init__)


def test_mmdsl_filecopy_constructor_args():
    sig = inspect.signature(mMDSL_FileCopy.__init__)
    params = list(sig.parameters.keys())
    assert "src" in params, "Missing parameter 'src'"
    assert "dest" in params, "Missing parameter 'dest'"

def test_mmdsl_filecopy_has_src():
    assert hasattr(mMDSL_FileCopy, "src")
    descriptor = None
    for klass in mMDSL_FileCopy.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_filecopy_has_dest():
    assert hasattr(mMDSL_FileCopy, "dest")
    descriptor = None
    for klass in mMDSL_FileCopy.__mro__:
        if "dest" in klass.__dict__:
            descriptor = klass.__dict__["dest"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL_AttributeOperation)


def test_mmdsl_attributeoperation_constructor_exists():
    assert callable(mMDSL_AttributeOperation.__init__)


def test_mmdsl_attributeoperation_constructor_args():
    sig = inspect.signature(mMDSL_AttributeOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_instanceoperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL_InstanceOperation)


def test_mmdsl_instanceoperation_constructor_exists():
    assert callable(mMDSL_InstanceOperation.__init__)


def test_mmdsl_instanceoperation_constructor_args():
    sig = inspect.signature(mMDSL_InstanceOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_modeloperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ModelOperation)


def test_mmdsl_modeloperation_constructor_exists():
    assert callable(mMDSL_ModelOperation.__init__)


def test_mmdsl_modeloperation_constructor_args():
    sig = inspect.signature(mMDSL_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_simpleui_is_not_abstract():
    assert not inspect.isabstract(mMDSL_SimpleUI)


def test_mmdsl_simpleui_constructor_exists():
    assert callable(mMDSL_SimpleUI.__init__)


def test_mmdsl_simpleui_constructor_args():
    sig = inspect.signature(mMDSL_SimpleUI.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_diroperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL_DirOperation)


def test_mmdsl_diroperation_constructor_exists():
    assert callable(mMDSL_DirOperation.__init__)


def test_mmdsl_diroperation_constructor_args():
    sig = inspect.signature(mMDSL_DirOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_fileoperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL_FileOperation)


def test_mmdsl_fileoperation_constructor_exists():
    assert callable(mMDSL_FileOperation.__init__)


def test_mmdsl_fileoperation_constructor_args():
    sig = inspect.signature(mMDSL_FileOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_eobject_is_not_abstract():
    assert not inspect.isabstract(mMDSL_EObject)


def test_mmdsl_eobject_constructor_exists():
    assert callable(mMDSL_EObject.__init__)


def test_mmdsl_eobject_constructor_args():
    sig = inspect.signature(mMDSL_EObject.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_expression_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Expression)


def test_mmdsl_expression_constructor_exists():
    assert callable(mMDSL_Expression.__init__)


def test_mmdsl_expression_constructor_args():
    sig = inspect.signature(mMDSL_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "valueRealNumber" in params, "Missing parameter 'valueRealNumber'"
    assert "true" in params, "Missing parameter 'true'"
    assert "valueString" in params, "Missing parameter 'valueString'"
    assert "false" in params, "Missing parameter 'false'"

def test_mmdsl_expression_has_valueRealNumber():
    assert hasattr(mMDSL_Expression, "valueRealNumber")
    descriptor = None
    for klass in mMDSL_Expression.__mro__:
        if "valueRealNumber" in klass.__dict__:
            descriptor = klass.__dict__["valueRealNumber"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_expression_has_true():
    assert hasattr(mMDSL_Expression, "true")
    descriptor = None
    for klass in mMDSL_Expression.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_expression_has_valueString():
    assert hasattr(mMDSL_Expression, "valueString")
    descriptor = None
    for klass in mMDSL_Expression.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_expression_has_false():
    assert hasattr(mMDSL_Expression, "false")
    descriptor = None
    for klass in mMDSL_Expression.__mro__:
        if "false" in klass.__dict__:
            descriptor = klass.__dict__["false"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_operatoror_is_not_abstract():
    assert not inspect.isabstract(mMDSL_OperatorOr)


def test_mmdsl_operatoror_constructor_exists():
    assert callable(mMDSL_OperatorOr.__init__)


def test_mmdsl_operatoror_constructor_args():
    sig = inspect.signature(mMDSL_OperatorOr.__init__)
    params = list(sig.parameters.keys())
    assert "or_" in params, "Missing parameter 'or_'"

def test_mmdsl_operatoror_has_or_():
    assert hasattr(mMDSL_OperatorOr, "or_")
    descriptor = None
    for klass in mMDSL_OperatorOr.__mro__:
        if "or_" in klass.__dict__:
            descriptor = klass.__dict__["or_"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_operatorand_is_not_abstract():
    assert not inspect.isabstract(mMDSL_OperatorAnd)


def test_mmdsl_operatorand_constructor_exists():
    assert callable(mMDSL_OperatorAnd.__init__)


def test_mmdsl_operatorand_constructor_args():
    sig = inspect.signature(mMDSL_OperatorAnd.__init__)
    params = list(sig.parameters.keys())
    assert "and_" in params, "Missing parameter 'and_'"

def test_mmdsl_operatorand_has_and_():
    assert hasattr(mMDSL_OperatorAnd, "and_")
    descriptor = None
    for klass in mMDSL_OperatorAnd.__mro__:
        if "and_" in klass.__dict__:
            descriptor = klass.__dict__["and_"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_operatorequal_is_not_abstract():
    assert not inspect.isabstract(mMDSL_OperatorEqual)


def test_mmdsl_operatorequal_constructor_exists():
    assert callable(mMDSL_OperatorEqual.__init__)


def test_mmdsl_operatorequal_constructor_args():
    sig = inspect.signature(mMDSL_OperatorEqual.__init__)
    params = list(sig.parameters.keys())
    assert "equal" in params, "Missing parameter 'equal'"
    assert "notequal" in params, "Missing parameter 'notequal'"

def test_mmdsl_operatorequal_has_equal():
    assert hasattr(mMDSL_OperatorEqual, "equal")
    descriptor = None
    for klass in mMDSL_OperatorEqual.__mro__:
        if "equal" in klass.__dict__:
            descriptor = klass.__dict__["equal"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_operatorequal_has_notequal():
    assert hasattr(mMDSL_OperatorEqual, "notequal")
    descriptor = None
    for klass in mMDSL_OperatorEqual.__mro__:
        if "notequal" in klass.__dict__:
            descriptor = klass.__dict__["notequal"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_operatorcompare_is_not_abstract():
    assert not inspect.isabstract(mMDSL_OperatorCompare)


def test_mmdsl_operatorcompare_constructor_exists():
    assert callable(mMDSL_OperatorCompare.__init__)


def test_mmdsl_operatorcompare_constructor_args():
    sig = inspect.signature(mMDSL_OperatorCompare.__init__)
    params = list(sig.parameters.keys())
    assert "greater" in params, "Missing parameter 'greater'"
    assert "lesser" in params, "Missing parameter 'lesser'"
    assert "lesserequal" in params, "Missing parameter 'lesserequal'"
    assert "greaterequal" in params, "Missing parameter 'greaterequal'"

def test_mmdsl_operatorcompare_has_greater():
    assert hasattr(mMDSL_OperatorCompare, "greater")
    descriptor = None
    for klass in mMDSL_OperatorCompare.__mro__:
        if "greater" in klass.__dict__:
            descriptor = klass.__dict__["greater"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_operatorcompare_has_lesser():
    assert hasattr(mMDSL_OperatorCompare, "lesser")
    descriptor = None
    for klass in mMDSL_OperatorCompare.__mro__:
        if "lesser" in klass.__dict__:
            descriptor = klass.__dict__["lesser"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_operatorcompare_has_lesserequal():
    assert hasattr(mMDSL_OperatorCompare, "lesserequal")
    descriptor = None
    for klass in mMDSL_OperatorCompare.__mro__:
        if "lesserequal" in klass.__dict__:
            descriptor = klass.__dict__["lesserequal"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_operatorcompare_has_greaterequal():
    assert hasattr(mMDSL_OperatorCompare, "greaterequal")
    descriptor = None
    for klass in mMDSL_OperatorCompare.__mro__:
        if "greaterequal" in klass.__dict__:
            descriptor = klass.__dict__["greaterequal"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_operatoradd_is_not_abstract():
    assert not inspect.isabstract(mMDSL_OperatorAdd)


def test_mmdsl_operatoradd_constructor_exists():
    assert callable(mMDSL_OperatorAdd.__init__)


def test_mmdsl_operatoradd_constructor_args():
    sig = inspect.signature(mMDSL_OperatorAdd.__init__)
    params = list(sig.parameters.keys())
    assert "add" in params, "Missing parameter 'add'"
    assert "subtract" in params, "Missing parameter 'subtract'"

def test_mmdsl_operatoradd_has_add():
    assert hasattr(mMDSL_OperatorAdd, "add")
    descriptor = None
    for klass in mMDSL_OperatorAdd.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_operatoradd_has_subtract():
    assert hasattr(mMDSL_OperatorAdd, "subtract")
    descriptor = None
    for klass in mMDSL_OperatorAdd.__mro__:
        if "subtract" in klass.__dict__:
            descriptor = klass.__dict__["subtract"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_operatormultiply_is_not_abstract():
    assert not inspect.isabstract(mMDSL_OperatorMultiply)


def test_mmdsl_operatormultiply_constructor_exists():
    assert callable(mMDSL_OperatorMultiply.__init__)


def test_mmdsl_operatormultiply_constructor_args():
    sig = inspect.signature(mMDSL_OperatorMultiply.__init__)
    params = list(sig.parameters.keys())
    assert "modulo" in params, "Missing parameter 'modulo'"
    assert "multiply" in params, "Missing parameter 'multiply'"
    assert "divide" in params, "Missing parameter 'divide'"

def test_mmdsl_operatormultiply_has_modulo():
    assert hasattr(mMDSL_OperatorMultiply, "modulo")
    descriptor = None
    for klass in mMDSL_OperatorMultiply.__mro__:
        if "modulo" in klass.__dict__:
            descriptor = klass.__dict__["modulo"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_operatormultiply_has_multiply():
    assert hasattr(mMDSL_OperatorMultiply, "multiply")
    descriptor = None
    for klass in mMDSL_OperatorMultiply.__mro__:
        if "multiply" in klass.__dict__:
            descriptor = klass.__dict__["multiply"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_operatormultiply_has_divide():
    assert hasattr(mMDSL_OperatorMultiply, "divide")
    descriptor = None
    for klass in mMDSL_OperatorMultiply.__mro__:
        if "divide" in klass.__dict__:
            descriptor = klass.__dict__["divide"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_operatorunary_is_not_abstract():
    assert not inspect.isabstract(mMDSL_OperatorUnary)


def test_mmdsl_operatorunary_constructor_exists():
    assert callable(mMDSL_OperatorUnary.__init__)


def test_mmdsl_operatorunary_constructor_args():
    sig = inspect.signature(mMDSL_OperatorUnary.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_mmdsl_operatorunary_has_not_():
    assert hasattr(mMDSL_OperatorUnary, "not_")
    descriptor = None
    for klass in mMDSL_OperatorUnary.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_operatormultyassign_is_not_abstract():
    assert not inspect.isabstract(mMDSL_OperatorMultyAssign)


def test_mmdsl_operatormultyassign_constructor_exists():
    assert callable(mMDSL_OperatorMultyAssign.__init__)


def test_mmdsl_operatormultyassign_constructor_args():
    sig = inspect.signature(mMDSL_OperatorMultyAssign.__init__)
    params = list(sig.parameters.keys())
    assert "divassign" in params, "Missing parameter 'divassign'"
    assert "multiassign" in params, "Missing parameter 'multiassign'"
    assert "subassign" in params, "Missing parameter 'subassign'"
    assert "addassign" in params, "Missing parameter 'addassign'"

def test_mmdsl_operatormultyassign_has_divassign():
    assert hasattr(mMDSL_OperatorMultyAssign, "divassign")
    descriptor = None
    for klass in mMDSL_OperatorMultyAssign.__mro__:
        if "divassign" in klass.__dict__:
            descriptor = klass.__dict__["divassign"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_operatormultyassign_has_multiassign():
    assert hasattr(mMDSL_OperatorMultyAssign, "multiassign")
    descriptor = None
    for klass in mMDSL_OperatorMultyAssign.__mro__:
        if "multiassign" in klass.__dict__:
            descriptor = klass.__dict__["multiassign"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_operatormultyassign_has_subassign():
    assert hasattr(mMDSL_OperatorMultyAssign, "subassign")
    descriptor = None
    for klass in mMDSL_OperatorMultyAssign.__mro__:
        if "subassign" in klass.__dict__:
            descriptor = klass.__dict__["subassign"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_operatormultyassign_has_addassign():
    assert hasattr(mMDSL_OperatorMultyAssign, "addassign")
    descriptor = None
    for klass in mMDSL_OperatorMultyAssign.__mro__:
        if "addassign" in klass.__dict__:
            descriptor = klass.__dict__["addassign"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_varstatement_is_not_abstract():
    assert not inspect.isabstract(mMDSL_VarStatement)


def test_mmdsl_varstatement_constructor_exists():
    assert callable(mMDSL_VarStatement.__init__)


def test_mmdsl_varstatement_constructor_args():
    sig = inspect.signature(mMDSL_VarStatement.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_operatorassign_is_not_abstract():
    assert not inspect.isabstract(mMDSL_OperatorAssign)


def test_mmdsl_operatorassign_constructor_exists():
    assert callable(mMDSL_OperatorAssign.__init__)


def test_mmdsl_operatorassign_constructor_args():
    sig = inspect.signature(mMDSL_OperatorAssign.__init__)
    params = list(sig.parameters.keys())
    assert "assign" in params, "Missing parameter 'assign'"

def test_mmdsl_operatorassign_has_assign():
    assert hasattr(mMDSL_OperatorAssign, "assign")
    descriptor = None
    for klass in mMDSL_OperatorAssign.__mro__:
        if "assign" in klass.__dict__:
            descriptor = klass.__dict__["assign"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_breakcontinue_is_not_abstract():
    assert not inspect.isabstract(mMDSL_BreakContinue)


def test_mmdsl_breakcontinue_constructor_exists():
    assert callable(mMDSL_BreakContinue.__init__)


def test_mmdsl_breakcontinue_constructor_args():
    sig = inspect.signature(mMDSL_BreakContinue.__init__)
    params = list(sig.parameters.keys())
    assert "continue_" in params, "Missing parameter 'continue_'"
    assert "break_" in params, "Missing parameter 'break_'"

def test_mmdsl_breakcontinue_has_continue_():
    assert hasattr(mMDSL_BreakContinue, "continue_")
    descriptor = None
    for klass in mMDSL_BreakContinue.__mro__:
        if "continue_" in klass.__dict__:
            descriptor = klass.__dict__["continue_"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_breakcontinue_has_break_():
    assert hasattr(mMDSL_BreakContinue, "break_")
    descriptor = None
    for klass in mMDSL_BreakContinue.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_forloop_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ForLoop)


def test_mmdsl_forloop_constructor_exists():
    assert callable(mMDSL_ForLoop.__init__)


def test_mmdsl_forloop_constructor_args():
    sig = inspect.signature(mMDSL_ForLoop.__init__)
    params = list(sig.parameters.keys())
    assert "interval" in params, "Missing parameter 'interval'"
    assert "start" in params, "Missing parameter 'start'"
    assert "stop" in params, "Missing parameter 'stop'"

def test_mmdsl_forloop_has_interval():
    assert hasattr(mMDSL_ForLoop, "interval")
    descriptor = None
    for klass in mMDSL_ForLoop.__mro__:
        if "interval" in klass.__dict__:
            descriptor = klass.__dict__["interval"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_forloop_has_start():
    assert hasattr(mMDSL_ForLoop, "start")
    descriptor = None
    for klass in mMDSL_ForLoop.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_forloop_has_stop():
    assert hasattr(mMDSL_ForLoop, "stop")
    descriptor = None
    for klass in mMDSL_ForLoop.__mro__:
        if "stop" in klass.__dict__:
            descriptor = klass.__dict__["stop"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_whileloop_is_not_abstract():
    assert not inspect.isabstract(mMDSL_WhileLoop)


def test_mmdsl_whileloop_constructor_exists():
    assert callable(mMDSL_WhileLoop.__init__)


def test_mmdsl_whileloop_constructor_args():
    sig = inspect.signature(mMDSL_WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_expr_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Expr)


def test_mmdsl_expr_constructor_exists():
    assert callable(mMDSL_Expr.__init__)


def test_mmdsl_expr_constructor_args():
    sig = inspect.signature(mMDSL_Expr.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_algorithmoperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL_AlgorithmOperation)


def test_mmdsl_algorithmoperation_constructor_exists():
    assert callable(mMDSL_AlgorithmOperation.__init__)


def test_mmdsl_algorithmoperation_constructor_args():
    sig = inspect.signature(mMDSL_AlgorithmOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_variable_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Variable)


def test_mmdsl_variable_constructor_exists():
    assert callable(mMDSL_Variable.__init__)


def test_mmdsl_variable_constructor_args():
    sig = inspect.signature(mMDSL_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_variable_has_name():
    assert hasattr(mMDSL_Variable, "name")
    descriptor = None
    for klass in mMDSL_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_loopstatement_is_not_abstract():
    assert not inspect.isabstract(mMDSL_LoopStatement)


def test_mmdsl_loopstatement_constructor_exists():
    assert callable(mMDSL_LoopStatement.__init__)


def test_mmdsl_loopstatement_constructor_args():
    sig = inspect.signature(mMDSL_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_selectionstatement_is_not_abstract():
    assert not inspect.isabstract(mMDSL_SelectionStatement)


def test_mmdsl_selectionstatement_constructor_exists():
    assert callable(mMDSL_SelectionStatement.__init__)


def test_mmdsl_selectionstatement_constructor_args():
    sig = inspect.signature(mMDSL_SelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_statement_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Statement)


def test_mmdsl_statement_constructor_exists():
    assert callable(mMDSL_Statement.__init__)


def test_mmdsl_statement_constructor_args():
    sig = inspect.signature(mMDSL_Statement.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_strokecolor_is_not_abstract():
    assert not inspect.isabstract(mMDSL_StrokeColor)


def test_mmdsl_strokecolor_constructor_exists():
    assert callable(mMDSL_StrokeColor.__init__)


def test_mmdsl_strokecolor_constructor_args():
    sig = inspect.signature(mMDSL_StrokeColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "hexcolor" in params, "Missing parameter 'hexcolor'"

def test_mmdsl_strokecolor_has_color():
    assert hasattr(mMDSL_StrokeColor, "color")
    descriptor = None
    for klass in mMDSL_StrokeColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_strokecolor_has_hexcolor():
    assert hasattr(mMDSL_StrokeColor, "hexcolor")
    descriptor = None
    for klass in mMDSL_StrokeColor.__mro__:
        if "hexcolor" in klass.__dict__:
            descriptor = klass.__dict__["hexcolor"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_pathparametersa_is_not_abstract():
    assert not inspect.isabstract(mMDSL_PathParametersA)


def test_mmdsl_pathparametersa_constructor_exists():
    assert callable(mMDSL_PathParametersA.__init__)


def test_mmdsl_pathparametersa_constructor_args():
    sig = inspect.signature(mMDSL_PathParametersA.__init__)
    params = list(sig.parameters.keys())
    assert "largearcflag" in params, "Missing parameter 'largearcflag'"
    assert "y" in params, "Missing parameter 'y'"
    assert "ry" in params, "Missing parameter 'ry'"
    assert "rx" in params, "Missing parameter 'rx'"
    assert "sweepflag" in params, "Missing parameter 'sweepflag'"
    assert "x" in params, "Missing parameter 'x'"
    assert "xaxisrot" in params, "Missing parameter 'xaxisrot'"

def test_mmdsl_pathparametersa_has_largearcflag():
    assert hasattr(mMDSL_PathParametersA, "largearcflag")
    descriptor = None
    for klass in mMDSL_PathParametersA.__mro__:
        if "largearcflag" in klass.__dict__:
            descriptor = klass.__dict__["largearcflag"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersa_has_y():
    assert hasattr(mMDSL_PathParametersA, "y")
    descriptor = None
    for klass in mMDSL_PathParametersA.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersa_has_ry():
    assert hasattr(mMDSL_PathParametersA, "ry")
    descriptor = None
    for klass in mMDSL_PathParametersA.__mro__:
        if "ry" in klass.__dict__:
            descriptor = klass.__dict__["ry"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersa_has_rx():
    assert hasattr(mMDSL_PathParametersA, "rx")
    descriptor = None
    for klass in mMDSL_PathParametersA.__mro__:
        if "rx" in klass.__dict__:
            descriptor = klass.__dict__["rx"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersa_has_sweepflag():
    assert hasattr(mMDSL_PathParametersA, "sweepflag")
    descriptor = None
    for klass in mMDSL_PathParametersA.__mro__:
        if "sweepflag" in klass.__dict__:
            descriptor = klass.__dict__["sweepflag"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersa_has_x():
    assert hasattr(mMDSL_PathParametersA, "x")
    descriptor = None
    for klass in mMDSL_PathParametersA.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersa_has_xaxisrot():
    assert hasattr(mMDSL_PathParametersA, "xaxisrot")
    descriptor = None
    for klass in mMDSL_PathParametersA.__mro__:
        if "xaxisrot" in klass.__dict__:
            descriptor = klass.__dict__["xaxisrot"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_pathparametersq_is_not_abstract():
    assert not inspect.isabstract(mMDSL_PathParametersQ)


def test_mmdsl_pathparametersq_constructor_exists():
    assert callable(mMDSL_PathParametersQ.__init__)


def test_mmdsl_pathparametersq_constructor_args():
    sig = inspect.signature(mMDSL_PathParametersQ.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x1" in params, "Missing parameter 'x1'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y1" in params, "Missing parameter 'y1'"

def test_mmdsl_pathparametersq_has_y():
    assert hasattr(mMDSL_PathParametersQ, "y")
    descriptor = None
    for klass in mMDSL_PathParametersQ.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersq_has_x1():
    assert hasattr(mMDSL_PathParametersQ, "x1")
    descriptor = None
    for klass in mMDSL_PathParametersQ.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersq_has_x():
    assert hasattr(mMDSL_PathParametersQ, "x")
    descriptor = None
    for klass in mMDSL_PathParametersQ.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersq_has_y1():
    assert hasattr(mMDSL_PathParametersQ, "y1")
    descriptor = None
    for klass in mMDSL_PathParametersQ.__mro__:
        if "y1" in klass.__dict__:
            descriptor = klass.__dict__["y1"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_pathparameterss_is_not_abstract():
    assert not inspect.isabstract(mMDSL_PathParametersS)


def test_mmdsl_pathparameterss_constructor_exists():
    assert callable(mMDSL_PathParametersS.__init__)


def test_mmdsl_pathparameterss_constructor_args():
    sig = inspect.signature(mMDSL_PathParametersS.__init__)
    params = list(sig.parameters.keys())
    assert "y2" in params, "Missing parameter 'y2'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x2" in params, "Missing parameter 'x2'"
    assert "x" in params, "Missing parameter 'x'"

def test_mmdsl_pathparameterss_has_y2():
    assert hasattr(mMDSL_PathParametersS, "y2")
    descriptor = None
    for klass in mMDSL_PathParametersS.__mro__:
        if "y2" in klass.__dict__:
            descriptor = klass.__dict__["y2"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparameterss_has_y():
    assert hasattr(mMDSL_PathParametersS, "y")
    descriptor = None
    for klass in mMDSL_PathParametersS.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparameterss_has_x2():
    assert hasattr(mMDSL_PathParametersS, "x2")
    descriptor = None
    for klass in mMDSL_PathParametersS.__mro__:
        if "x2" in klass.__dict__:
            descriptor = klass.__dict__["x2"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparameterss_has_x():
    assert hasattr(mMDSL_PathParametersS, "x")
    descriptor = None
    for klass in mMDSL_PathParametersS.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_pathparametersc_is_not_abstract():
    assert not inspect.isabstract(mMDSL_PathParametersC)


def test_mmdsl_pathparametersc_constructor_exists():
    assert callable(mMDSL_PathParametersC.__init__)


def test_mmdsl_pathparametersc_constructor_args():
    sig = inspect.signature(mMDSL_PathParametersC.__init__)
    params = list(sig.parameters.keys())
    assert "y1" in params, "Missing parameter 'y1'"
    assert "x2" in params, "Missing parameter 'x2'"
    assert "y2" in params, "Missing parameter 'y2'"
    assert "x" in params, "Missing parameter 'x'"
    assert "x1" in params, "Missing parameter 'x1'"
    assert "y" in params, "Missing parameter 'y'"

def test_mmdsl_pathparametersc_has_y1():
    assert hasattr(mMDSL_PathParametersC, "y1")
    descriptor = None
    for klass in mMDSL_PathParametersC.__mro__:
        if "y1" in klass.__dict__:
            descriptor = klass.__dict__["y1"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersc_has_x2():
    assert hasattr(mMDSL_PathParametersC, "x2")
    descriptor = None
    for klass in mMDSL_PathParametersC.__mro__:
        if "x2" in klass.__dict__:
            descriptor = klass.__dict__["x2"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersc_has_y2():
    assert hasattr(mMDSL_PathParametersC, "y2")
    descriptor = None
    for klass in mMDSL_PathParametersC.__mro__:
        if "y2" in klass.__dict__:
            descriptor = klass.__dict__["y2"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersc_has_x():
    assert hasattr(mMDSL_PathParametersC, "x")
    descriptor = None
    for klass in mMDSL_PathParametersC.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersc_has_x1():
    assert hasattr(mMDSL_PathParametersC, "x1")
    descriptor = None
    for klass in mMDSL_PathParametersC.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersc_has_y():
    assert hasattr(mMDSL_PathParametersC, "y")
    descriptor = None
    for klass in mMDSL_PathParametersC.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_pathparametershv_is_not_abstract():
    assert not inspect.isabstract(mMDSL_PathParametersHV)


def test_mmdsl_pathparametershv_constructor_exists():
    assert callable(mMDSL_PathParametersHV.__init__)


def test_mmdsl_pathparametershv_constructor_args():
    sig = inspect.signature(mMDSL_PathParametersHV.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_mmdsl_pathparametershv_has_x():
    assert hasattr(mMDSL_PathParametersHV, "x")
    descriptor = None
    for klass in mMDSL_PathParametersHV.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_pathparametersmlt_is_not_abstract():
    assert not inspect.isabstract(mMDSL_PathParametersMLT)


def test_mmdsl_pathparametersmlt_constructor_exists():
    assert callable(mMDSL_PathParametersMLT.__init__)


def test_mmdsl_pathparametersmlt_constructor_args():
    sig = inspect.signature(mMDSL_PathParametersMLT.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_mmdsl_pathparametersmlt_has_x():
    assert hasattr(mMDSL_PathParametersMLT, "x")
    descriptor = None
    for klass in mMDSL_PathParametersMLT.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_pathparametersmlt_has_y():
    assert hasattr(mMDSL_PathParametersMLT, "y")
    descriptor = None
    for klass in mMDSL_PathParametersMLT.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_ellipticalarc_is_not_abstract():
    assert not inspect.isabstract(mMDSL_EllipticalArc)


def test_mmdsl_ellipticalarc_constructor_exists():
    assert callable(mMDSL_EllipticalArc.__init__)


def test_mmdsl_ellipticalarc_constructor_args():
    sig = inspect.signature(mMDSL_EllipticalArc.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_smoothquadraticbeziercurveto_is_not_abstract():
    assert not inspect.isabstract(mMDSL_SmoothQuadraticBezierCurveTo)


def test_mmdsl_smoothquadraticbeziercurveto_constructor_exists():
    assert callable(mMDSL_SmoothQuadraticBezierCurveTo.__init__)


def test_mmdsl_smoothquadraticbeziercurveto_constructor_args():
    sig = inspect.signature(mMDSL_SmoothQuadraticBezierCurveTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_quadraticbeziercurve_is_not_abstract():
    assert not inspect.isabstract(mMDSL_QuadraticBezierCurve)


def test_mmdsl_quadraticbeziercurve_constructor_exists():
    assert callable(mMDSL_QuadraticBezierCurve.__init__)


def test_mmdsl_quadraticbeziercurve_constructor_args():
    sig = inspect.signature(mMDSL_QuadraticBezierCurve.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_smoothcurveto_is_not_abstract():
    assert not inspect.isabstract(mMDSL_SmoothCurveTo)


def test_mmdsl_smoothcurveto_constructor_exists():
    assert callable(mMDSL_SmoothCurveTo.__init__)


def test_mmdsl_smoothcurveto_constructor_args():
    sig = inspect.signature(mMDSL_SmoothCurveTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_curveto_is_not_abstract():
    assert not inspect.isabstract(mMDSL_CurveTo)


def test_mmdsl_curveto_constructor_exists():
    assert callable(mMDSL_CurveTo.__init__)


def test_mmdsl_curveto_constructor_args():
    sig = inspect.signature(mMDSL_CurveTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_verticallineto_is_not_abstract():
    assert not inspect.isabstract(mMDSL_VerticalLineTo)


def test_mmdsl_verticallineto_constructor_exists():
    assert callable(mMDSL_VerticalLineTo.__init__)


def test_mmdsl_verticallineto_constructor_args():
    sig = inspect.signature(mMDSL_VerticalLineTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_horizontallineto_is_not_abstract():
    assert not inspect.isabstract(mMDSL_HorizontalLineTo)


def test_mmdsl_horizontallineto_constructor_exists():
    assert callable(mMDSL_HorizontalLineTo.__init__)


def test_mmdsl_horizontallineto_constructor_args():
    sig = inspect.signature(mMDSL_HorizontalLineTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_lineto_is_not_abstract():
    assert not inspect.isabstract(mMDSL_LineTo)


def test_mmdsl_lineto_constructor_exists():
    assert callable(mMDSL_LineTo.__init__)


def test_mmdsl_lineto_constructor_args():
    sig = inspect.signature(mMDSL_LineTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_moveto_is_not_abstract():
    assert not inspect.isabstract(mMDSL_MoveTo)


def test_mmdsl_moveto_constructor_exists():
    assert callable(mMDSL_MoveTo.__init__)


def test_mmdsl_moveto_constructor_args():
    sig = inspect.signature(mMDSL_MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_fillcolor_is_not_abstract():
    assert not inspect.isabstract(mMDSL_FillColor)


def test_mmdsl_fillcolor_constructor_exists():
    assert callable(mMDSL_FillColor.__init__)


def test_mmdsl_fillcolor_constructor_args():
    sig = inspect.signature(mMDSL_FillColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "hexcolor" in params, "Missing parameter 'hexcolor'"

def test_mmdsl_fillcolor_has_color():
    assert hasattr(mMDSL_FillColor, "color")
    descriptor = None
    for klass in mMDSL_FillColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_fillcolor_has_hexcolor():
    assert hasattr(mMDSL_FillColor, "hexcolor")
    descriptor = None
    for klass in mMDSL_FillColor.__mro__:
        if "hexcolor" in klass.__dict__:
            descriptor = klass.__dict__["hexcolor"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_fontfamily_is_not_abstract():
    assert not inspect.isabstract(mMDSL_FontFamily)


def test_mmdsl_fontfamily_constructor_exists():
    assert callable(mMDSL_FontFamily.__init__)


def test_mmdsl_fontfamily_constructor_args():
    sig = inspect.signature(mMDSL_FontFamily.__init__)
    params = list(sig.parameters.keys())
    assert "fontstr" in params, "Missing parameter 'fontstr'"
    assert "font" in params, "Missing parameter 'font'"

def test_mmdsl_fontfamily_has_fontstr():
    assert hasattr(mMDSL_FontFamily, "fontstr")
    descriptor = None
    for klass in mMDSL_FontFamily.__mro__:
        if "fontstr" in klass.__dict__:
            descriptor = klass.__dict__["fontstr"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_fontfamily_has_font():
    assert hasattr(mMDSL_FontFamily, "font")
    descriptor = None
    for klass in mMDSL_FontFamily.__mro__:
        if "font" in klass.__dict__:
            descriptor = klass.__dict__["font"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_pathdata_is_not_abstract():
    assert not inspect.isabstract(mMDSL_PathData)


def test_mmdsl_pathdata_constructor_exists():
    assert callable(mMDSL_PathData.__init__)


def test_mmdsl_pathdata_constructor_args():
    sig = inspect.signature(mMDSL_PathData.__init__)
    params = list(sig.parameters.keys())
    assert "closepath" in params, "Missing parameter 'closepath'"

def test_mmdsl_pathdata_has_closepath():
    assert hasattr(mMDSL_PathData, "closepath")
    descriptor = None
    for klass in mMDSL_PathData.__mro__:
        if "closepath" in klass.__dict__:
            descriptor = klass.__dict__["closepath"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_points_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Points)


def test_mmdsl_points_constructor_exists():
    assert callable(mMDSL_Points.__init__)


def test_mmdsl_points_constructor_args():
    sig = inspect.signature(mMDSL_Points.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_mmdsl_points_has_x():
    assert hasattr(mMDSL_Points, "x")
    descriptor = None
    for klass in mMDSL_Points.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_points_has_y():
    assert hasattr(mMDSL_Points, "y")
    descriptor = None
    for klass in mMDSL_Points.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_text_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Text)


def test_mmdsl_text_constructor_exists():
    assert callable(mMDSL_Text.__init__)


def test_mmdsl_text_constructor_args():
    sig = inspect.signature(mMDSL_Text.__init__)
    params = list(sig.parameters.keys())
    assert "fontsize" in params, "Missing parameter 'fontsize'"
    assert "y" in params, "Missing parameter 'y'"
    assert "value" in params, "Missing parameter 'value'"
    assert "x" in params, "Missing parameter 'x'"

def test_mmdsl_text_has_fontsize():
    assert hasattr(mMDSL_Text, "fontsize")
    descriptor = None
    for klass in mMDSL_Text.__mro__:
        if "fontsize" in klass.__dict__:
            descriptor = klass.__dict__["fontsize"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_text_has_y():
    assert hasattr(mMDSL_Text, "y")
    descriptor = None
    for klass in mMDSL_Text.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_text_has_value():
    assert hasattr(mMDSL_Text, "value")
    descriptor = None
    for klass in mMDSL_Text.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_text_has_x():
    assert hasattr(mMDSL_Text, "x")
    descriptor = None
    for klass in mMDSL_Text.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_path_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Path)


def test_mmdsl_path_constructor_exists():
    assert callable(mMDSL_Path.__init__)


def test_mmdsl_path_constructor_args():
    sig = inspect.signature(mMDSL_Path.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_polygon_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Polygon)


def test_mmdsl_polygon_constructor_exists():
    assert callable(mMDSL_Polygon.__init__)


def test_mmdsl_polygon_constructor_args():
    sig = inspect.signature(mMDSL_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_polyline_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Polyline)


def test_mmdsl_polyline_constructor_exists():
    assert callable(mMDSL_Polyline.__init__)


def test_mmdsl_polyline_constructor_args():
    sig = inspect.signature(mMDSL_Polyline.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_line_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Line)


def test_mmdsl_line_constructor_exists():
    assert callable(mMDSL_Line.__init__)


def test_mmdsl_line_constructor_args():
    sig = inspect.signature(mMDSL_Line.__init__)
    params = list(sig.parameters.keys())
    assert "x1" in params, "Missing parameter 'x1'"
    assert "y1" in params, "Missing parameter 'y1'"
    assert "x2" in params, "Missing parameter 'x2'"
    assert "y2" in params, "Missing parameter 'y2'"

def test_mmdsl_line_has_x1():
    assert hasattr(mMDSL_Line, "x1")
    descriptor = None
    for klass in mMDSL_Line.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_line_has_y1():
    assert hasattr(mMDSL_Line, "y1")
    descriptor = None
    for klass in mMDSL_Line.__mro__:
        if "y1" in klass.__dict__:
            descriptor = klass.__dict__["y1"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_line_has_x2():
    assert hasattr(mMDSL_Line, "x2")
    descriptor = None
    for klass in mMDSL_Line.__mro__:
        if "x2" in klass.__dict__:
            descriptor = klass.__dict__["x2"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_line_has_y2():
    assert hasattr(mMDSL_Line, "y2")
    descriptor = None
    for klass in mMDSL_Line.__mro__:
        if "y2" in klass.__dict__:
            descriptor = klass.__dict__["y2"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_ellipse_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Ellipse)


def test_mmdsl_ellipse_constructor_exists():
    assert callable(mMDSL_Ellipse.__init__)


def test_mmdsl_ellipse_constructor_args():
    sig = inspect.signature(mMDSL_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "cy" in params, "Missing parameter 'cy'"
    assert "rx" in params, "Missing parameter 'rx'"
    assert "ry" in params, "Missing parameter 'ry'"
    assert "cx" in params, "Missing parameter 'cx'"

def test_mmdsl_ellipse_has_cy():
    assert hasattr(mMDSL_Ellipse, "cy")
    descriptor = None
    for klass in mMDSL_Ellipse.__mro__:
        if "cy" in klass.__dict__:
            descriptor = klass.__dict__["cy"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_ellipse_has_rx():
    assert hasattr(mMDSL_Ellipse, "rx")
    descriptor = None
    for klass in mMDSL_Ellipse.__mro__:
        if "rx" in klass.__dict__:
            descriptor = klass.__dict__["rx"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_ellipse_has_ry():
    assert hasattr(mMDSL_Ellipse, "ry")
    descriptor = None
    for klass in mMDSL_Ellipse.__mro__:
        if "ry" in klass.__dict__:
            descriptor = klass.__dict__["ry"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_ellipse_has_cx():
    assert hasattr(mMDSL_Ellipse, "cx")
    descriptor = None
    for klass in mMDSL_Ellipse.__mro__:
        if "cx" in klass.__dict__:
            descriptor = klass.__dict__["cx"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_circle_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Circle)


def test_mmdsl_circle_constructor_exists():
    assert callable(mMDSL_Circle.__init__)


def test_mmdsl_circle_constructor_args():
    sig = inspect.signature(mMDSL_Circle.__init__)
    params = list(sig.parameters.keys())
    assert "cx" in params, "Missing parameter 'cx'"
    assert "cy" in params, "Missing parameter 'cy'"
    assert "r" in params, "Missing parameter 'r'"

def test_mmdsl_circle_has_cx():
    assert hasattr(mMDSL_Circle, "cx")
    descriptor = None
    for klass in mMDSL_Circle.__mro__:
        if "cx" in klass.__dict__:
            descriptor = klass.__dict__["cx"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_circle_has_cy():
    assert hasattr(mMDSL_Circle, "cy")
    descriptor = None
    for klass in mMDSL_Circle.__mro__:
        if "cy" in klass.__dict__:
            descriptor = klass.__dict__["cy"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_circle_has_r():
    assert hasattr(mMDSL_Circle, "r")
    descriptor = None
    for klass in mMDSL_Circle.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_rectangle_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Rectangle)


def test_mmdsl_rectangle_constructor_exists():
    assert callable(mMDSL_Rectangle.__init__)


def test_mmdsl_rectangle_constructor_args():
    sig = inspect.signature(mMDSL_Rectangle.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "height" in params, "Missing parameter 'height'"

def test_mmdsl_rectangle_has_width():
    assert hasattr(mMDSL_Rectangle, "width")
    descriptor = None
    for klass in mMDSL_Rectangle.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_rectangle_has_x():
    assert hasattr(mMDSL_Rectangle, "x")
    descriptor = None
    for klass in mMDSL_Rectangle.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_rectangle_has_y():
    assert hasattr(mMDSL_Rectangle, "y")
    descriptor = None
    for klass in mMDSL_Rectangle.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_rectangle_has_height():
    assert hasattr(mMDSL_Rectangle, "height")
    descriptor = None
    for klass in mMDSL_Rectangle.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_svgcommand_is_not_abstract():
    assert not inspect.isabstract(mMDSL_SVGCommand)


def test_mmdsl_svgcommand_constructor_exists():
    assert callable(mMDSL_SVGCommand.__init__)


def test_mmdsl_svgcommand_constructor_args():
    sig = inspect.signature(mMDSL_SVGCommand.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_mode_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Mode)


def test_mmdsl_mode_constructor_exists():
    assert callable(mMDSL_Mode.__init__)


def test_mmdsl_mode_constructor_args():
    sig = inspect.signature(mMDSL_Mode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_mode_has_name():
    assert hasattr(mMDSL_Mode, "name")
    descriptor = None
    for klass in mMDSL_Mode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_enumtype_is_not_abstract():
    assert not inspect.isabstract(mMDSL_EnumType)


def test_mmdsl_enumtype_constructor_exists():
    assert callable(mMDSL_EnumType.__init__)


def test_mmdsl_enumtype_constructor_args():
    sig = inspect.signature(mMDSL_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_refname_is_not_abstract():
    assert not inspect.isabstract(mMDSL_RefName)


def test_mmdsl_refname_constructor_exists():
    assert callable(mMDSL_RefName.__init__)


def test_mmdsl_refname_constructor_args():
    sig = inspect.signature(mMDSL_RefName.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_type_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Type)


def test_mmdsl_type_constructor_exists():
    assert callable(mMDSL_Type.__init__)


def test_mmdsl_type_constructor_args():
    sig = inspect.signature(mMDSL_Type.__init__)
    params = list(sig.parameters.keys())
    assert "simpletype" in params, "Missing parameter 'simpletype'"

def test_mmdsl_type_has_simpletype():
    assert hasattr(mMDSL_Type, "simpletype")
    descriptor = None
    for klass in mMDSL_Type.__mro__:
        if "simpletype" in klass.__dict__:
            descriptor = klass.__dict__["simpletype"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_reference_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Reference)


def test_mmdsl_reference_constructor_exists():
    assert callable(mMDSL_Reference.__init__)


def test_mmdsl_reference_constructor_args():
    sig = inspect.signature(mMDSL_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_reference_has_name():
    assert hasattr(mMDSL_Reference, "name")
    descriptor = None
    for klass in mMDSL_Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_classattribute_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ClassAttribute)


def test_mmdsl_classattribute_constructor_exists():
    assert callable(mMDSL_ClassAttribute.__init__)


def test_mmdsl_classattribute_constructor_args():
    sig = inspect.signature(mMDSL_ClassAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_classattribute_has_name():
    assert hasattr(mMDSL_ClassAttribute, "name")
    descriptor = None
    for klass in mMDSL_ClassAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_modeltype_is_not_abstract():
    assert not inspect.isabstract(mMDSL_ModelType)


def test_mmdsl_modeltype_constructor_exists():
    assert callable(mMDSL_ModelType.__init__)


def test_mmdsl_modeltype_constructor_args():
    sig = inspect.signature(mMDSL_ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_modeltype_has_name():
    assert hasattr(mMDSL_ModelType, "name")
    descriptor = None
    for klass in mMDSL_ModelType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_attribute_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Attribute)


def test_mmdsl_attribute_constructor_exists():
    assert callable(mMDSL_Attribute.__init__)


def test_mmdsl_attribute_constructor_args():
    sig = inspect.signature(mMDSL_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "access" in params, "Missing parameter 'access'"

def test_mmdsl_attribute_has_name():
    assert hasattr(mMDSL_Attribute, "name")
    descriptor = None
    for klass in mMDSL_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_attribute_has_access():
    assert hasattr(mMDSL_Attribute, "access")
    descriptor = None
    for klass in mMDSL_Attribute.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_relation_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Relation)


def test_mmdsl_relation_constructor_exists():
    assert callable(mMDSL_Relation.__init__)


def test_mmdsl_relation_constructor_args():
    sig = inspect.signature(mMDSL_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_relation_has_name():
    assert hasattr(mMDSL_Relation, "name")
    descriptor = None
    for klass in mMDSL_Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_class_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Class)


def test_mmdsl_class_constructor_exists():
    assert callable(mMDSL_Class.__init__)


def test_mmdsl_class_constructor_args():
    sig = inspect.signature(mMDSL_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_class_has_name():
    assert hasattr(mMDSL_Class, "name")
    descriptor = None
    for klass in mMDSL_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_event_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Event)


def test_mmdsl_event_constructor_exists():
    assert callable(mMDSL_Event.__init__)


def test_mmdsl_event_constructor_args():
    sig = inspect.signature(mMDSL_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_event_has_name():
    assert hasattr(mMDSL_Event, "name")
    descriptor = None
    for klass in mMDSL_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_algorithm_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Algorithm)


def test_mmdsl_algorithm_constructor_exists():
    assert callable(mMDSL_Algorithm.__init__)


def test_mmdsl_algorithm_constructor_args():
    sig = inspect.signature(mMDSL_Algorithm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_algorithm_has_name():
    assert hasattr(mMDSL_Algorithm, "name")
    descriptor = None
    for klass in mMDSL_Algorithm.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_metamodel_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Metamodel)


def test_mmdsl_metamodel_constructor_exists():
    assert callable(mMDSL_Metamodel.__init__)


def test_mmdsl_metamodel_constructor_args():
    sig = inspect.signature(mMDSL_Metamodel.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_symbolrelation_is_not_abstract():
    assert not inspect.isabstract(mMDSL_SymbolRelation)


def test_mmdsl_symbolrelation_constructor_exists():
    assert callable(mMDSL_SymbolRelation.__init__)


def test_mmdsl_symbolrelation_constructor_args():
    sig = inspect.signature(mMDSL_SymbolRelation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_symbolrelation_has_name():
    assert hasattr(mMDSL_SymbolRelation, "name")
    descriptor = None
    for klass in mMDSL_SymbolRelation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_symbolclass_is_not_abstract():
    assert not inspect.isabstract(mMDSL_SymbolClass)


def test_mmdsl_symbolclass_constructor_exists():
    assert callable(mMDSL_SymbolClass.__init__)


def test_mmdsl_symbolclass_constructor_args():
    sig = inspect.signature(mMDSL_SymbolClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_symbolclass_has_name():
    assert hasattr(mMDSL_SymbolClass, "name")
    descriptor = None
    for klass in mMDSL_SymbolClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_symbolstyle_is_not_abstract():
    assert not inspect.isabstract(mMDSL_SymbolStyle)


def test_mmdsl_symbolstyle_constructor_exists():
    assert callable(mMDSL_SymbolStyle.__init__)


def test_mmdsl_symbolstyle_constructor_args():
    sig = inspect.signature(mMDSL_SymbolStyle.__init__)
    params = list(sig.parameters.keys())
    assert "fontsize" in params, "Missing parameter 'fontsize'"
    assert "strokewidth" in params, "Missing parameter 'strokewidth'"
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_symbolstyle_has_fontsize():
    assert hasattr(mMDSL_SymbolStyle, "fontsize")
    descriptor = None
    for klass in mMDSL_SymbolStyle.__mro__:
        if "fontsize" in klass.__dict__:
            descriptor = klass.__dict__["fontsize"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_symbolstyle_has_strokewidth():
    assert hasattr(mMDSL_SymbolStyle, "strokewidth")
    descriptor = None
    for klass in mMDSL_SymbolStyle.__mro__:
        if "strokewidth" in klass.__dict__:
            descriptor = klass.__dict__["strokewidth"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_symbolstyle_has_name():
    assert hasattr(mMDSL_SymbolStyle, "name")
    descriptor = None
    for klass in mMDSL_SymbolStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_enumeration_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Enumeration)


def test_mmdsl_enumeration_constructor_exists():
    assert callable(mMDSL_Enumeration.__init__)


def test_mmdsl_enumeration_constructor_args():
    sig = inspect.signature(mMDSL_Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "enumvalues" in params, "Missing parameter 'enumvalues'"
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_enumeration_has_enumvalues():
    assert hasattr(mMDSL_Enumeration, "enumvalues")
    descriptor = None
    for klass in mMDSL_Enumeration.__mro__:
        if "enumvalues" in klass.__dict__:
            descriptor = klass.__dict__["enumvalues"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_enumeration_has_name():
    assert hasattr(mMDSL_Enumeration, "name")
    descriptor = None
    for klass in mMDSL_Enumeration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_insertembedcode_is_not_abstract():
    assert not inspect.isabstract(mMDSL_InsertEmbedCode)


def test_mmdsl_insertembedcode_constructor_exists():
    assert callable(mMDSL_InsertEmbedCode.__init__)


def test_mmdsl_insertembedcode_constructor_args():
    sig = inspect.signature(mMDSL_InsertEmbedCode.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_method_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Method)


def test_mmdsl_method_constructor_exists():
    assert callable(mMDSL_Method.__init__)


def test_mmdsl_method_constructor_args():
    sig = inspect.signature(mMDSL_Method.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl_embedcode_is_not_abstract():
    assert not inspect.isabstract(mMDSL_EmbedCode)


def test_mmdsl_embedcode_constructor_exists():
    assert callable(mMDSL_EmbedCode.__init__)


def test_mmdsl_embedcode_constructor_args():
    sig = inspect.signature(mMDSL_EmbedCode.__init__)
    params = list(sig.parameters.keys())
    assert "embeddedcode" in params, "Missing parameter 'embeddedcode'"
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_embedcode_has_embeddedcode():
    assert hasattr(mMDSL_EmbedCode, "embeddedcode")
    descriptor = None
    for klass in mMDSL_EmbedCode.__mro__:
        if "embeddedcode" in klass.__dict__:
            descriptor = klass.__dict__["embeddedcode"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl_embedcode_has_name():
    assert hasattr(mMDSL_EmbedCode, "name")
    descriptor = None
    for klass in mMDSL_EmbedCode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_includelibrary_is_not_abstract():
    assert not inspect.isabstract(mMDSL_IncludeLibrary)


def test_mmdsl_includelibrary_constructor_exists():
    assert callable(mMDSL_IncludeLibrary.__init__)


def test_mmdsl_includelibrary_constructor_args():
    sig = inspect.signature(mMDSL_IncludeLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_includelibrary_has_name():
    assert hasattr(mMDSL_IncludeLibrary, "name")
    descriptor = None
    for klass in mMDSL_IncludeLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_embedcodetype_is_not_abstract():
    assert not inspect.isabstract(mMDSL_EmbedCodeType)


def test_mmdsl_embedcodetype_constructor_exists():
    assert callable(mMDSL_EmbedCodeType.__init__)


def test_mmdsl_embedcodetype_constructor_args():
    sig = inspect.signature(mMDSL_EmbedCodeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_embedcodetype_has_name():
    assert hasattr(mMDSL_EmbedCodeType, "name")
    descriptor = None
    for klass in mMDSL_EmbedCodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_embedplatformtype_is_not_abstract():
    assert not inspect.isabstract(mMDSL_EmbedPlatformType)


def test_mmdsl_embedplatformtype_constructor_exists():
    assert callable(mMDSL_EmbedPlatformType.__init__)


def test_mmdsl_embedplatformtype_constructor_args():
    sig = inspect.signature(mMDSL_EmbedPlatformType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_embedplatformtype_has_name():
    assert hasattr(mMDSL_EmbedPlatformType, "name")
    descriptor = None
    for klass in mMDSL_EmbedPlatformType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_includelibrarytype_is_not_abstract():
    assert not inspect.isabstract(mMDSL_IncludeLibraryType)


def test_mmdsl_includelibrarytype_constructor_exists():
    assert callable(mMDSL_IncludeLibraryType.__init__)


def test_mmdsl_includelibrarytype_constructor_args():
    sig = inspect.signature(mMDSL_IncludeLibraryType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_includelibrarytype_has_name():
    assert hasattr(mMDSL_IncludeLibraryType, "name")
    descriptor = None
    for klass in mMDSL_IncludeLibraryType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_methodname_is_not_abstract():
    assert not inspect.isabstract(mMDSL_MethodName)


def test_mmdsl_methodname_constructor_exists():
    assert callable(mMDSL_MethodName.__init__)


def test_mmdsl_methodname_constructor_args():
    sig = inspect.signature(mMDSL_MethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl_methodname_has_name():
    assert hasattr(mMDSL_MethodName, "name")
    descriptor = None
    for klass in mMDSL_MethodName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl_root_is_not_abstract():
    assert not inspect.isabstract(mMDSL_Root)


def test_mmdsl_root_constructor_exists():
    assert callable(mMDSL_Root.__init__)


def test_mmdsl_root_constructor_args():
    sig = inspect.signature(mMDSL_Root.__init__)
    params = list(sig.parameters.keys())

def test_simpletype_exists():
    # Check that the Enumeration exists
    assert SimpleType is not None

def test_simpletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleType]
    expected_literals = [
        "Int",
        "Double",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleType"

def test_attrgetparams_exists():
    # Check that the Enumeration exists
    assert AttrGetParams is not None

def test_attrgetparams_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttrGetParams]
    expected_literals = [
        "type",
        "name",
        "value",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttrGetParams"

def test_buttontype_exists():
    # Check that the Enumeration exists
    assert ButtonType is not None

def test_buttontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ButtonType]
    expected_literals = [
        "okcancel",
        "defyes",
        "defno",
        "defcancel",
        "retrycancel",
        "yesno",
        "defretry",
        "ok",
        "defok",
        "yesnocancel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ButtonType"

def test_attrsetparams_exists():
    # Check that the Enumeration exists
    assert AttrSetParams is not None

def test_attrsetparams_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttrSetParams]
    expected_literals = [
        "value",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttrSetParams"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "cornsilk",
        "mediumblue",
        "turquoise",
        "darkseagreen",
        "olivedrab",
        "indianred",
        "darkred",
        "white",
        "whitesmoke",
        "oldlace",
        "yellowgreen",
        "darkturquoise",
        "gray",
        "darkorchid",
        "navajowhite",
        "honeydew",
        "aqua",
        "linen",
        "goldenrod",
        "palevioletred",
        "aliceblue",
        "moccasin",
        "orangered",
        "khaki",
        "firebrick",
        "navy",
        "lightyellow",
        "blanchedalmond",
        "black",
        "slategray",
        "lightgreen",
        "darkorange",
        "burlywood",
        "plum",
        "cornflowerblue",
        "darkgray",
        "ivory",
        "seashell",
        "orchid",
        "skyblue",
        "darkblue",
        "magenta",
        "mediumturquoise",
        "salmon",
        "pink",
        "lightcyan",
        "springgreen",
        "lavender",
        "dimgray",
        "darkslategray",
        "silver",
        "seagreen",
        "lightblue",
        "deeppink",
        "mediumvioletred",
        "palegoldenrod",
        "sandybrown",
        "darkslateblue",
        "powderblue",
        "purple",
        "brown",
        "darkkhaki",
        "lightseagreen",
        "beige",
        "chartreuse",
        "lightcoral",
        "sienna",
        "lightgray",
        "bisque",
        "fuchsia",
        "lavenderblush",
        "yellow",
        "mediumslateblue",
        "wheat",
        "blue",
        "palegreen",
        "teal",
        "lawngreen",
        "darksalmon",
        "mediumaquamarine",
        "rosybrown",
        "mediumseagreen",
        "darkviolet",
        "dodgerblue",
        "gold",
        "mistyrose",
        "violet",
        "mediumorchid",
        "deepskyblue",
        "green",
        "lemonchiffon",
        "red",
        "lightskyblue",
        "steelblue",
        "darkolivegreen",
        "mintcream",
        "slateblue",
        "thistle",
        "mediumpurple",
        "greenyellow",
        "mediumspringgreen",
        "olive",
        "royalblue",
        "saddlebrown",
        "darkmagenta",
        "maroon",
        "orange",
        "lightgoldenrodyellow",
        "lightslategray",
        "coral",
        "papayawhip",
        "cadetblue",
        "chocolate",
        "indigo",
        "ghostwhite",
        "crimson",
        "floralwhite",
        "limegreen",
        "forestgreen",
        "tomato",
        "lightsteelblue",
        "peachpuff",
        "darkcyan",
        "snow",
        "lightmagenta",
        "hotpink",
        "lightsalmon",
        "midnightblue",
        "antiquewhite",
        "lightpink",
        "darkgoldenrod",
        "aquamarine",
        "lime",
        "peru",
        "paleturquoise",
        "cyan",
        "blueviolet",
        "azure",
        "gainsboro",
        "darkgreen",
        "tan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_font_exists():
    # Check that the Enumeration exists
    assert Font is not None

def test_font_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Font]
    expected_literals = [
        "arial",
        "webdings",
        "georgia",
        "windings",
        "timesnewroman",
        "comicsansms",
        "couriernew",
        "trebuchetms",
        "msserif",
        "tahoma",
        "palatinolinotype",
        "impact",
        "verdana",
        "lucidaconsole",
        "lucidasansunicode",
        "mssansserif",
        "arialblack",
        "symbol",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Font"

def test_eventname_exists():
    # Check that the Enumeration exists
    assert EventName is not None

def test_eventname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventName]
    expected_literals = [
        "deleteinstance",
        "openmodel",
        "beforedeletemodel",
        "aftercreatemodelingconnector",
        "renameinstance",
        "beforecreaterelationinstance",
        "beforedeleteinstance",
        "discardinstance",
        "createmodel",
        "aftereditattributevalue",
        "setattributevalue",
        "savemodel",
        "beforediscardmodel",
        "beforecreatemodel",
        "createrelationinstance",
        "createinstance",
        "aftercreatemodelingnode",
        "deletemodel",
        "discardmodel",
        "beforesavemodel",
        "toolinitialized",
        "deleterelationinstance",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventName"

def test_accesstype_exists():
    # Check that the Enumeration exists
    assert AccessType is not None

def test_accesstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessType]
    expected_literals = [
        "read",
        "internal",
        "write",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessType"


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
Expression_strategy = st.builds(
    Expression,
)
mMDSL_MultiplicationExpression_strategy = st.builds(
    mMDSL_MultiplicationExpression,
)
mMDSL_CompareExpression_strategy = st.builds(
    mMDSL_CompareExpression,
)
mMDSL_EqualExpression_strategy = st.builds(
    mMDSL_EqualExpression,
)
mMDSL_AdditionExpression_strategy = st.builds(
    mMDSL_AdditionExpression,
)
mMDSL_AndExpression_strategy = st.builds(
    mMDSL_AndExpression,
)
mMDSL_OrExpression_strategy = st.builds(
    mMDSL_OrExpression,
)
mMDSL_AttributeSet_strategy = st.builds(
    mMDSL_AttributeSet,
    attrsetparams=
        safe_text,
    valueRealNumber=
        safe_text,
    valueString=
        safe_text
)
mMDSL_AttributeGet_strategy = st.builds(
    mMDSL_AttributeGet,
    attrgetparams=
        safe_text
)
mMDSL_RelationInstanceGetAll_strategy = st.builds(
    mMDSL_RelationInstanceGetAll,
)
mMDSL_RelationInstanceSet_strategy = st.builds(
    mMDSL_RelationInstanceSet,
)
mMDSL_RelationInstanceGet_strategy = st.builds(
    mMDSL_RelationInstanceGet,
)
mMDSL_RelationInstanceDelete_strategy = st.builds(
    mMDSL_RelationInstanceDelete,
)
mMDSL_RelationInstanceCreate_strategy = st.builds(
    mMDSL_RelationInstanceCreate,
    name=
        safe_text
)
mMDSL_ClassInstanceGetAll_strategy = st.builds(
    mMDSL_ClassInstanceGetAll,
)
mMDSL_ClassInstanceSet_strategy = st.builds(
    mMDSL_ClassInstanceSet,
)
mMDSL_ClassInstanceGet_strategy = st.builds(
    mMDSL_ClassInstanceGet,
)
mMDSL_ClassInstanceDelete_strategy = st.builds(
    mMDSL_ClassInstanceDelete,
)
mMDSL_ClassInstanceCreate_strategy = st.builds(
    mMDSL_ClassInstanceCreate,
    name=
        safe_text
)
mMDSL_RelationInstance_strategy = st.builds(
    mMDSL_RelationInstance,
)
mMDSL_ClassInstance_strategy = st.builds(
    mMDSL_ClassInstance,
)
mMDSL_ModelIsLoaded_strategy = st.builds(
    mMDSL_ModelIsLoaded,
)
mMDSL_ModelLoad_strategy = st.builds(
    mMDSL_ModelLoad,
)
mMDSL_ModelSave_strategy = st.builds(
    mMDSL_ModelSave,
)
mMDSL_ModelDiscard_strategy = st.builds(
    mMDSL_ModelDiscard,
)
mMDSL_ModelDelete_strategy = st.builds(
    mMDSL_ModelDelete,
)
mMDSL_ModelCreate_strategy = st.builds(
    mMDSL_ModelCreate,
    name=
        safe_text
)
mMDSL_RemoveContextItem_strategy = st.builds(
    mMDSL_RemoveContextItem,
)
mMDSL_InsertContextItem_strategy = st.builds(
    mMDSL_InsertContextItem,
    name=
        safe_text,
    context=
        safe_text
)
mMDSL_RemoveMenuItem_strategy = st.builds(
    mMDSL_RemoveMenuItem,
)
mMDSL_InsertMenuItem_strategy = st.builds(
    mMDSL_InsertMenuItem,
    menu=
        safe_text,
    name=
        safe_text
)
mMDSL_ContextItem_strategy = st.builds(
    mMDSL_ContextItem,
)
mMDSL_MenuItem_strategy = st.builds(
    mMDSL_MenuItem,
)
mMDSL_ItemOperation_strategy = st.builds(
    mMDSL_ItemOperation,
)
mMDSL_ViewBox_strategy = st.builds(
    mMDSL_ViewBox,
    title=
        safe_text,
    text=
        safe_text
)
mMDSL_WarningBox_strategy = st.builds(
    mMDSL_WarningBox,
    buttontype=
        safe_text,
    title=
        safe_text,
    text=
        safe_text
)
mMDSL_ErrorBox_strategy = st.builds(
    mMDSL_ErrorBox,
    buttontype=
        safe_text,
    text=
        safe_text,
    title=
        safe_text
)
mMDSL_InfoBox_strategy = st.builds(
    mMDSL_InfoBox,
    text=
        safe_text,
    title=
        safe_text
)
mMDSL_EditBox_strategy = st.builds(
    mMDSL_EditBox,
    okbuttontext=
        safe_text,
    title=
        safe_text,
    text=
        safe_text
)
mMDSL_DirList_strategy = st.builds(
    mMDSL_DirList,
    dirname=
        safe_text
)
mMDSL_DirDelete_strategy = st.builds(
    mMDSL_DirDelete,
    dirname=
        safe_text
)
mMDSL_DirCreate_strategy = st.builds(
    mMDSL_DirCreate,
    dirname=
        safe_text
)
mMDSL_DirGetWorking_strategy = st.builds(
    mMDSL_DirGetWorking,
)
mMDSL_DirSetWorking_strategy = st.builds(
    mMDSL_DirSetWorking,
    dirname=
        safe_text
)
mMDSL_FileWrite_strategy = st.builds(
    mMDSL_FileWrite,
    filename=
        safe_text,
    append=
        safe_text,
    text=
        safe_text
)
mMDSL_FileRead_strategy = st.builds(
    mMDSL_FileRead,
    filename=
        safe_text
)
mMDSL_FileCreate_strategy = st.builds(
    mMDSL_FileCreate,
    filename=
        safe_text
)
mMDSL_FileDelete_strategy = st.builds(
    mMDSL_FileDelete,
    filename=
        safe_text
)
mMDSL_FileCopy_strategy = st.builds(
    mMDSL_FileCopy,
    src=
        safe_text,
    dest=
        safe_text
)
mMDSL_AttributeOperation_strategy = st.builds(
    mMDSL_AttributeOperation,
)
mMDSL_InstanceOperation_strategy = st.builds(
    mMDSL_InstanceOperation,
)
mMDSL_ModelOperation_strategy = st.builds(
    mMDSL_ModelOperation,
)
mMDSL_SimpleUI_strategy = st.builds(
    mMDSL_SimpleUI,
)
mMDSL_DirOperation_strategy = st.builds(
    mMDSL_DirOperation,
)
mMDSL_FileOperation_strategy = st.builds(
    mMDSL_FileOperation,
)
mMDSL_EObject_strategy = st.builds(
    mMDSL_EObject,
)
mMDSL_Expression_strategy = st.builds(
    mMDSL_Expression,
    valueRealNumber=
        safe_text,
    true=
        safe_text,
    valueString=
        safe_text,
    false=
        safe_text
)
mMDSL_OperatorOr_strategy = st.builds(
    mMDSL_OperatorOr,
    or_=
        safe_text
)
mMDSL_OperatorAnd_strategy = st.builds(
    mMDSL_OperatorAnd,
    and_=
        safe_text
)
mMDSL_OperatorEqual_strategy = st.builds(
    mMDSL_OperatorEqual,
    equal=
        safe_text,
    notequal=
        safe_text
)
mMDSL_OperatorCompare_strategy = st.builds(
    mMDSL_OperatorCompare,
    greater=
        safe_text,
    lesser=
        safe_text,
    lesserequal=
        safe_text,
    greaterequal=
        safe_text
)
mMDSL_OperatorAdd_strategy = st.builds(
    mMDSL_OperatorAdd,
    add=
        safe_text,
    subtract=
        safe_text
)
mMDSL_OperatorMultiply_strategy = st.builds(
    mMDSL_OperatorMultiply,
    modulo=
        safe_text,
    multiply=
        safe_text,
    divide=
        safe_text
)
mMDSL_OperatorUnary_strategy = st.builds(
    mMDSL_OperatorUnary,
    not_=
        safe_text
)
mMDSL_OperatorMultyAssign_strategy = st.builds(
    mMDSL_OperatorMultyAssign,
    divassign=
        safe_text,
    multiassign=
        safe_text,
    subassign=
        safe_text,
    addassign=
        safe_text
)
mMDSL_VarStatement_strategy = st.builds(
    mMDSL_VarStatement,
)
mMDSL_OperatorAssign_strategy = st.builds(
    mMDSL_OperatorAssign,
    assign=
        safe_text
)
mMDSL_BreakContinue_strategy = st.builds(
    mMDSL_BreakContinue,
    continue_=
        safe_text,
    break_=
        safe_text
)
mMDSL_ForLoop_strategy = st.builds(
    mMDSL_ForLoop,
    interval=
        st.integers(),
    start=
        st.integers(),
    stop=
        st.integers()
)
mMDSL_WhileLoop_strategy = st.builds(
    mMDSL_WhileLoop,
)
mMDSL_Expr_strategy = st.builds(
    mMDSL_Expr,
)
mMDSL_AlgorithmOperation_strategy = st.builds(
    mMDSL_AlgorithmOperation,
)
mMDSL_Variable_strategy = st.builds(
    mMDSL_Variable,
    name=
        safe_text
)
mMDSL_LoopStatement_strategy = st.builds(
    mMDSL_LoopStatement,
)
mMDSL_SelectionStatement_strategy = st.builds(
    mMDSL_SelectionStatement,
)
mMDSL_Statement_strategy = st.builds(
    mMDSL_Statement,
)
mMDSL_StrokeColor_strategy = st.builds(
    mMDSL_StrokeColor,
    color=
        safe_text,
    hexcolor=
        safe_text
)
mMDSL_PathParametersA_strategy = st.builds(
    mMDSL_PathParametersA,
    largearcflag=
        safe_text,
    y=
        safe_text,
    ry=
        safe_text,
    rx=
        safe_text,
    sweepflag=
        safe_text,
    x=
        safe_text,
    xaxisrot=
        safe_text
)
mMDSL_PathParametersQ_strategy = st.builds(
    mMDSL_PathParametersQ,
    y=
        safe_text,
    x1=
        safe_text,
    x=
        safe_text,
    y1=
        safe_text
)
mMDSL_PathParametersS_strategy = st.builds(
    mMDSL_PathParametersS,
    y2=
        safe_text,
    y=
        safe_text,
    x2=
        safe_text,
    x=
        safe_text
)
mMDSL_PathParametersC_strategy = st.builds(
    mMDSL_PathParametersC,
    y1=
        safe_text,
    x2=
        safe_text,
    y2=
        safe_text,
    x=
        safe_text,
    x1=
        safe_text,
    y=
        safe_text
)
mMDSL_PathParametersHV_strategy = st.builds(
    mMDSL_PathParametersHV,
    x=
        safe_text
)
mMDSL_PathParametersMLT_strategy = st.builds(
    mMDSL_PathParametersMLT,
    x=
        safe_text,
    y=
        safe_text
)
mMDSL_EllipticalArc_strategy = st.builds(
    mMDSL_EllipticalArc,
)
mMDSL_SmoothQuadraticBezierCurveTo_strategy = st.builds(
    mMDSL_SmoothQuadraticBezierCurveTo,
)
mMDSL_QuadraticBezierCurve_strategy = st.builds(
    mMDSL_QuadraticBezierCurve,
)
mMDSL_SmoothCurveTo_strategy = st.builds(
    mMDSL_SmoothCurveTo,
)
mMDSL_CurveTo_strategy = st.builds(
    mMDSL_CurveTo,
)
mMDSL_VerticalLineTo_strategy = st.builds(
    mMDSL_VerticalLineTo,
)
mMDSL_HorizontalLineTo_strategy = st.builds(
    mMDSL_HorizontalLineTo,
)
mMDSL_LineTo_strategy = st.builds(
    mMDSL_LineTo,
)
mMDSL_MoveTo_strategy = st.builds(
    mMDSL_MoveTo,
)
mMDSL_FillColor_strategy = st.builds(
    mMDSL_FillColor,
    color=
        safe_text,
    hexcolor=
        safe_text
)
mMDSL_FontFamily_strategy = st.builds(
    mMDSL_FontFamily,
    fontstr=
        safe_text,
    font=
        safe_text
)
mMDSL_PathData_strategy = st.builds(
    mMDSL_PathData,
    closepath=
        safe_text
)
mMDSL_Points_strategy = st.builds(
    mMDSL_Points,
    x=
        safe_text,
    y=
        safe_text
)
mMDSL_Text_strategy = st.builds(
    mMDSL_Text,
    fontsize=
        safe_text,
    y=
        safe_text,
    value=
        safe_text,
    x=
        safe_text
)
mMDSL_Path_strategy = st.builds(
    mMDSL_Path,
)
mMDSL_Polygon_strategy = st.builds(
    mMDSL_Polygon,
)
mMDSL_Polyline_strategy = st.builds(
    mMDSL_Polyline,
)
mMDSL_Line_strategy = st.builds(
    mMDSL_Line,
    x1=
        safe_text,
    y1=
        safe_text,
    x2=
        safe_text,
    y2=
        safe_text
)
mMDSL_Ellipse_strategy = st.builds(
    mMDSL_Ellipse,
    cy=
        safe_text,
    rx=
        safe_text,
    ry=
        safe_text,
    cx=
        safe_text
)
mMDSL_Circle_strategy = st.builds(
    mMDSL_Circle,
    cx=
        safe_text,
    cy=
        safe_text,
    r=
        safe_text
)
mMDSL_Rectangle_strategy = st.builds(
    mMDSL_Rectangle,
    width=
        safe_text,
    x=
        safe_text,
    y=
        safe_text,
    height=
        safe_text
)
mMDSL_SVGCommand_strategy = st.builds(
    mMDSL_SVGCommand,
)
mMDSL_Mode_strategy = st.builds(
    mMDSL_Mode,
    name=
        safe_text
)
mMDSL_EnumType_strategy = st.builds(
    mMDSL_EnumType,
)
mMDSL_RefName_strategy = st.builds(
    mMDSL_RefName,
)
mMDSL_Type_strategy = st.builds(
    mMDSL_Type,
    simpletype=
        safe_text
)
mMDSL_Reference_strategy = st.builds(
    mMDSL_Reference,
    name=
        safe_text
)
mMDSL_ClassAttribute_strategy = st.builds(
    mMDSL_ClassAttribute,
    name=
        safe_text
)
mMDSL_ModelType_strategy = st.builds(
    mMDSL_ModelType,
    name=
        safe_text
)
mMDSL_Attribute_strategy = st.builds(
    mMDSL_Attribute,
    name=
        safe_text,
    access=
        safe_text
)
mMDSL_Relation_strategy = st.builds(
    mMDSL_Relation,
    name=
        safe_text
)
mMDSL_Class_strategy = st.builds(
    mMDSL_Class,
    name=
        safe_text
)
mMDSL_Event_strategy = st.builds(
    mMDSL_Event,
    name=
        safe_text
)
mMDSL_Algorithm_strategy = st.builds(
    mMDSL_Algorithm,
    name=
        safe_text
)
mMDSL_Metamodel_strategy = st.builds(
    mMDSL_Metamodel,
)
mMDSL_SymbolRelation_strategy = st.builds(
    mMDSL_SymbolRelation,
    name=
        safe_text
)
mMDSL_SymbolClass_strategy = st.builds(
    mMDSL_SymbolClass,
    name=
        safe_text
)
mMDSL_SymbolStyle_strategy = st.builds(
    mMDSL_SymbolStyle,
    fontsize=
        safe_text,
    strokewidth=
        safe_text,
    name=
        safe_text
)
mMDSL_Enumeration_strategy = st.builds(
    mMDSL_Enumeration,
    enumvalues=
        safe_text,
    name=
        safe_text
)
mMDSL_InsertEmbedCode_strategy = st.builds(
    mMDSL_InsertEmbedCode,
)
mMDSL_Method_strategy = st.builds(
    mMDSL_Method,
)
mMDSL_EmbedCode_strategy = st.builds(
    mMDSL_EmbedCode,
    embeddedcode=
        safe_text,
    name=
        safe_text
)
mMDSL_IncludeLibrary_strategy = st.builds(
    mMDSL_IncludeLibrary,
    name=
        safe_text
)
mMDSL_EmbedCodeType_strategy = st.builds(
    mMDSL_EmbedCodeType,
    name=
        safe_text
)
mMDSL_EmbedPlatformType_strategy = st.builds(
    mMDSL_EmbedPlatformType,
    name=
        safe_text
)
mMDSL_IncludeLibraryType_strategy = st.builds(
    mMDSL_IncludeLibraryType,
    name=
        safe_text
)
mMDSL_MethodName_strategy = st.builds(
    mMDSL_MethodName,
    name=
        safe_text
)
mMDSL_Root_strategy = st.builds(
    mMDSL_Root,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mMDSL_MultiplicationExpression_strategy)
@settings(max_examples=50)
def test_mmdsl_multiplicationexpression_instantiation(instance):
    assert isinstance(instance, mMDSL_MultiplicationExpression)

@given(instance=mMDSL_CompareExpression_strategy)
@settings(max_examples=50)
def test_mmdsl_compareexpression_instantiation(instance):
    assert isinstance(instance, mMDSL_CompareExpression)

@given(instance=mMDSL_EqualExpression_strategy)
@settings(max_examples=50)
def test_mmdsl_equalexpression_instantiation(instance):
    assert isinstance(instance, mMDSL_EqualExpression)

@given(instance=mMDSL_AdditionExpression_strategy)
@settings(max_examples=50)
def test_mmdsl_additionexpression_instantiation(instance):
    assert isinstance(instance, mMDSL_AdditionExpression)

@given(instance=mMDSL_AndExpression_strategy)
@settings(max_examples=50)
def test_mmdsl_andexpression_instantiation(instance):
    assert isinstance(instance, mMDSL_AndExpression)

@given(instance=mMDSL_OrExpression_strategy)
@settings(max_examples=50)
def test_mmdsl_orexpression_instantiation(instance):
    assert isinstance(instance, mMDSL_OrExpression)

@given(instance=mMDSL_AttributeSet_strategy)
@settings(max_examples=50)
def test_mmdsl_attributeset_instantiation(instance):
    assert isinstance(instance, mMDSL_AttributeSet)



@given(instance=mMDSL_AttributeSet_strategy)
def test_mmdsl_attributeset_attrsetparams_setter(instance):
    original = instance.attrsetparams
    instance.attrsetparams = original
    assert instance.attrsetparams == original



@given(instance=mMDSL_AttributeSet_strategy)
def test_mmdsl_attributeset_valueRealNumber_setter(instance):
    original = instance.valueRealNumber
    instance.valueRealNumber = original
    assert instance.valueRealNumber == original



@given(instance=mMDSL_AttributeSet_strategy)
def test_mmdsl_attributeset_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=mMDSL_AttributeGet_strategy)
@settings(max_examples=50)
def test_mmdsl_attributeget_instantiation(instance):
    assert isinstance(instance, mMDSL_AttributeGet)



@given(instance=mMDSL_AttributeGet_strategy)
def test_mmdsl_attributeget_attrgetparams_setter(instance):
    original = instance.attrgetparams
    instance.attrgetparams = original
    assert instance.attrgetparams == original

@given(instance=mMDSL_RelationInstanceGetAll_strategy)
@settings(max_examples=50)
def test_mmdsl_relationinstancegetall_instantiation(instance):
    assert isinstance(instance, mMDSL_RelationInstanceGetAll)

@given(instance=mMDSL_RelationInstanceSet_strategy)
@settings(max_examples=50)
def test_mmdsl_relationinstanceset_instantiation(instance):
    assert isinstance(instance, mMDSL_RelationInstanceSet)

@given(instance=mMDSL_RelationInstanceGet_strategy)
@settings(max_examples=50)
def test_mmdsl_relationinstanceget_instantiation(instance):
    assert isinstance(instance, mMDSL_RelationInstanceGet)

@given(instance=mMDSL_RelationInstanceDelete_strategy)
@settings(max_examples=50)
def test_mmdsl_relationinstancedelete_instantiation(instance):
    assert isinstance(instance, mMDSL_RelationInstanceDelete)

@given(instance=mMDSL_RelationInstanceCreate_strategy)
@settings(max_examples=50)
def test_mmdsl_relationinstancecreate_instantiation(instance):
    assert isinstance(instance, mMDSL_RelationInstanceCreate)



@given(instance=mMDSL_RelationInstanceCreate_strategy)
def test_mmdsl_relationinstancecreate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_ClassInstanceGetAll_strategy)
@settings(max_examples=50)
def test_mmdsl_classinstancegetall_instantiation(instance):
    assert isinstance(instance, mMDSL_ClassInstanceGetAll)

@given(instance=mMDSL_ClassInstanceSet_strategy)
@settings(max_examples=50)
def test_mmdsl_classinstanceset_instantiation(instance):
    assert isinstance(instance, mMDSL_ClassInstanceSet)

@given(instance=mMDSL_ClassInstanceGet_strategy)
@settings(max_examples=50)
def test_mmdsl_classinstanceget_instantiation(instance):
    assert isinstance(instance, mMDSL_ClassInstanceGet)

@given(instance=mMDSL_ClassInstanceDelete_strategy)
@settings(max_examples=50)
def test_mmdsl_classinstancedelete_instantiation(instance):
    assert isinstance(instance, mMDSL_ClassInstanceDelete)

@given(instance=mMDSL_ClassInstanceCreate_strategy)
@settings(max_examples=50)
def test_mmdsl_classinstancecreate_instantiation(instance):
    assert isinstance(instance, mMDSL_ClassInstanceCreate)



@given(instance=mMDSL_ClassInstanceCreate_strategy)
def test_mmdsl_classinstancecreate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_RelationInstance_strategy)
@settings(max_examples=50)
def test_mmdsl_relationinstance_instantiation(instance):
    assert isinstance(instance, mMDSL_RelationInstance)

@given(instance=mMDSL_ClassInstance_strategy)
@settings(max_examples=50)
def test_mmdsl_classinstance_instantiation(instance):
    assert isinstance(instance, mMDSL_ClassInstance)

@given(instance=mMDSL_ModelIsLoaded_strategy)
@settings(max_examples=50)
def test_mmdsl_modelisloaded_instantiation(instance):
    assert isinstance(instance, mMDSL_ModelIsLoaded)

@given(instance=mMDSL_ModelLoad_strategy)
@settings(max_examples=50)
def test_mmdsl_modelload_instantiation(instance):
    assert isinstance(instance, mMDSL_ModelLoad)

@given(instance=mMDSL_ModelSave_strategy)
@settings(max_examples=50)
def test_mmdsl_modelsave_instantiation(instance):
    assert isinstance(instance, mMDSL_ModelSave)

@given(instance=mMDSL_ModelDiscard_strategy)
@settings(max_examples=50)
def test_mmdsl_modeldiscard_instantiation(instance):
    assert isinstance(instance, mMDSL_ModelDiscard)

@given(instance=mMDSL_ModelDelete_strategy)
@settings(max_examples=50)
def test_mmdsl_modeldelete_instantiation(instance):
    assert isinstance(instance, mMDSL_ModelDelete)

@given(instance=mMDSL_ModelCreate_strategy)
@settings(max_examples=50)
def test_mmdsl_modelcreate_instantiation(instance):
    assert isinstance(instance, mMDSL_ModelCreate)



@given(instance=mMDSL_ModelCreate_strategy)
def test_mmdsl_modelcreate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_RemoveContextItem_strategy)
@settings(max_examples=50)
def test_mmdsl_removecontextitem_instantiation(instance):
    assert isinstance(instance, mMDSL_RemoveContextItem)

@given(instance=mMDSL_InsertContextItem_strategy)
@settings(max_examples=50)
def test_mmdsl_insertcontextitem_instantiation(instance):
    assert isinstance(instance, mMDSL_InsertContextItem)



@given(instance=mMDSL_InsertContextItem_strategy)
def test_mmdsl_insertcontextitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mMDSL_InsertContextItem_strategy)
def test_mmdsl_insertcontextitem_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=mMDSL_RemoveMenuItem_strategy)
@settings(max_examples=50)
def test_mmdsl_removemenuitem_instantiation(instance):
    assert isinstance(instance, mMDSL_RemoveMenuItem)

@given(instance=mMDSL_InsertMenuItem_strategy)
@settings(max_examples=50)
def test_mmdsl_insertmenuitem_instantiation(instance):
    assert isinstance(instance, mMDSL_InsertMenuItem)



@given(instance=mMDSL_InsertMenuItem_strategy)
def test_mmdsl_insertmenuitem_menu_setter(instance):
    original = instance.menu
    instance.menu = original
    assert instance.menu == original



@given(instance=mMDSL_InsertMenuItem_strategy)
def test_mmdsl_insertmenuitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_ContextItem_strategy)
@settings(max_examples=50)
def test_mmdsl_contextitem_instantiation(instance):
    assert isinstance(instance, mMDSL_ContextItem)

@given(instance=mMDSL_MenuItem_strategy)
@settings(max_examples=50)
def test_mmdsl_menuitem_instantiation(instance):
    assert isinstance(instance, mMDSL_MenuItem)

@given(instance=mMDSL_ItemOperation_strategy)
@settings(max_examples=50)
def test_mmdsl_itemoperation_instantiation(instance):
    assert isinstance(instance, mMDSL_ItemOperation)

@given(instance=mMDSL_ViewBox_strategy)
@settings(max_examples=50)
def test_mmdsl_viewbox_instantiation(instance):
    assert isinstance(instance, mMDSL_ViewBox)



@given(instance=mMDSL_ViewBox_strategy)
def test_mmdsl_viewbox_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=mMDSL_ViewBox_strategy)
def test_mmdsl_viewbox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mMDSL_WarningBox_strategy)
@settings(max_examples=50)
def test_mmdsl_warningbox_instantiation(instance):
    assert isinstance(instance, mMDSL_WarningBox)



@given(instance=mMDSL_WarningBox_strategy)
def test_mmdsl_warningbox_buttontype_setter(instance):
    original = instance.buttontype
    instance.buttontype = original
    assert instance.buttontype == original



@given(instance=mMDSL_WarningBox_strategy)
def test_mmdsl_warningbox_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=mMDSL_WarningBox_strategy)
def test_mmdsl_warningbox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mMDSL_ErrorBox_strategy)
@settings(max_examples=50)
def test_mmdsl_errorbox_instantiation(instance):
    assert isinstance(instance, mMDSL_ErrorBox)



@given(instance=mMDSL_ErrorBox_strategy)
def test_mmdsl_errorbox_buttontype_setter(instance):
    original = instance.buttontype
    instance.buttontype = original
    assert instance.buttontype == original



@given(instance=mMDSL_ErrorBox_strategy)
def test_mmdsl_errorbox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=mMDSL_ErrorBox_strategy)
def test_mmdsl_errorbox_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mMDSL_InfoBox_strategy)
@settings(max_examples=50)
def test_mmdsl_infobox_instantiation(instance):
    assert isinstance(instance, mMDSL_InfoBox)



@given(instance=mMDSL_InfoBox_strategy)
def test_mmdsl_infobox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=mMDSL_InfoBox_strategy)
def test_mmdsl_infobox_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mMDSL_EditBox_strategy)
@settings(max_examples=50)
def test_mmdsl_editbox_instantiation(instance):
    assert isinstance(instance, mMDSL_EditBox)



@given(instance=mMDSL_EditBox_strategy)
def test_mmdsl_editbox_okbuttontext_setter(instance):
    original = instance.okbuttontext
    instance.okbuttontext = original
    assert instance.okbuttontext == original



@given(instance=mMDSL_EditBox_strategy)
def test_mmdsl_editbox_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=mMDSL_EditBox_strategy)
def test_mmdsl_editbox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mMDSL_DirList_strategy)
@settings(max_examples=50)
def test_mmdsl_dirlist_instantiation(instance):
    assert isinstance(instance, mMDSL_DirList)



@given(instance=mMDSL_DirList_strategy)
def test_mmdsl_dirlist_dirname_setter(instance):
    original = instance.dirname
    instance.dirname = original
    assert instance.dirname == original

@given(instance=mMDSL_DirDelete_strategy)
@settings(max_examples=50)
def test_mmdsl_dirdelete_instantiation(instance):
    assert isinstance(instance, mMDSL_DirDelete)



@given(instance=mMDSL_DirDelete_strategy)
def test_mmdsl_dirdelete_dirname_setter(instance):
    original = instance.dirname
    instance.dirname = original
    assert instance.dirname == original

@given(instance=mMDSL_DirCreate_strategy)
@settings(max_examples=50)
def test_mmdsl_dircreate_instantiation(instance):
    assert isinstance(instance, mMDSL_DirCreate)



@given(instance=mMDSL_DirCreate_strategy)
def test_mmdsl_dircreate_dirname_setter(instance):
    original = instance.dirname
    instance.dirname = original
    assert instance.dirname == original

@given(instance=mMDSL_DirGetWorking_strategy)
@settings(max_examples=50)
def test_mmdsl_dirgetworking_instantiation(instance):
    assert isinstance(instance, mMDSL_DirGetWorking)

@given(instance=mMDSL_DirSetWorking_strategy)
@settings(max_examples=50)
def test_mmdsl_dirsetworking_instantiation(instance):
    assert isinstance(instance, mMDSL_DirSetWorking)



@given(instance=mMDSL_DirSetWorking_strategy)
def test_mmdsl_dirsetworking_dirname_setter(instance):
    original = instance.dirname
    instance.dirname = original
    assert instance.dirname == original

@given(instance=mMDSL_FileWrite_strategy)
@settings(max_examples=50)
def test_mmdsl_filewrite_instantiation(instance):
    assert isinstance(instance, mMDSL_FileWrite)



@given(instance=mMDSL_FileWrite_strategy)
def test_mmdsl_filewrite_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=mMDSL_FileWrite_strategy)
def test_mmdsl_filewrite_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original



@given(instance=mMDSL_FileWrite_strategy)
def test_mmdsl_filewrite_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mMDSL_FileRead_strategy)
@settings(max_examples=50)
def test_mmdsl_fileread_instantiation(instance):
    assert isinstance(instance, mMDSL_FileRead)



@given(instance=mMDSL_FileRead_strategy)
def test_mmdsl_fileread_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=mMDSL_FileCreate_strategy)
@settings(max_examples=50)
def test_mmdsl_filecreate_instantiation(instance):
    assert isinstance(instance, mMDSL_FileCreate)



@given(instance=mMDSL_FileCreate_strategy)
def test_mmdsl_filecreate_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=mMDSL_FileDelete_strategy)
@settings(max_examples=50)
def test_mmdsl_filedelete_instantiation(instance):
    assert isinstance(instance, mMDSL_FileDelete)



@given(instance=mMDSL_FileDelete_strategy)
def test_mmdsl_filedelete_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=mMDSL_FileCopy_strategy)
@settings(max_examples=50)
def test_mmdsl_filecopy_instantiation(instance):
    assert isinstance(instance, mMDSL_FileCopy)



@given(instance=mMDSL_FileCopy_strategy)
def test_mmdsl_filecopy_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=mMDSL_FileCopy_strategy)
def test_mmdsl_filecopy_dest_setter(instance):
    original = instance.dest
    instance.dest = original
    assert instance.dest == original

@given(instance=mMDSL_AttributeOperation_strategy)
@settings(max_examples=50)
def test_mmdsl_attributeoperation_instantiation(instance):
    assert isinstance(instance, mMDSL_AttributeOperation)

@given(instance=mMDSL_InstanceOperation_strategy)
@settings(max_examples=50)
def test_mmdsl_instanceoperation_instantiation(instance):
    assert isinstance(instance, mMDSL_InstanceOperation)

@given(instance=mMDSL_ModelOperation_strategy)
@settings(max_examples=50)
def test_mmdsl_modeloperation_instantiation(instance):
    assert isinstance(instance, mMDSL_ModelOperation)

@given(instance=mMDSL_SimpleUI_strategy)
@settings(max_examples=50)
def test_mmdsl_simpleui_instantiation(instance):
    assert isinstance(instance, mMDSL_SimpleUI)

@given(instance=mMDSL_DirOperation_strategy)
@settings(max_examples=50)
def test_mmdsl_diroperation_instantiation(instance):
    assert isinstance(instance, mMDSL_DirOperation)

@given(instance=mMDSL_FileOperation_strategy)
@settings(max_examples=50)
def test_mmdsl_fileoperation_instantiation(instance):
    assert isinstance(instance, mMDSL_FileOperation)

@given(instance=mMDSL_EObject_strategy)
@settings(max_examples=50)
def test_mmdsl_eobject_instantiation(instance):
    assert isinstance(instance, mMDSL_EObject)

@given(instance=mMDSL_Expression_strategy)
@settings(max_examples=50)
def test_mmdsl_expression_instantiation(instance):
    assert isinstance(instance, mMDSL_Expression)



@given(instance=mMDSL_Expression_strategy)
def test_mmdsl_expression_valueRealNumber_setter(instance):
    original = instance.valueRealNumber
    instance.valueRealNumber = original
    assert instance.valueRealNumber == original



@given(instance=mMDSL_Expression_strategy)
def test_mmdsl_expression_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original



@given(instance=mMDSL_Expression_strategy)
def test_mmdsl_expression_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original



@given(instance=mMDSL_Expression_strategy)
def test_mmdsl_expression_false_setter(instance):
    original = instance.false
    instance.false = original
    assert instance.false == original

@given(instance=mMDSL_OperatorOr_strategy)
@settings(max_examples=50)
def test_mmdsl_operatoror_instantiation(instance):
    assert isinstance(instance, mMDSL_OperatorOr)



@given(instance=mMDSL_OperatorOr_strategy)
def test_mmdsl_operatoror_or__setter(instance):
    original = instance.or_
    instance.or_ = original
    assert instance.or_ == original

@given(instance=mMDSL_OperatorAnd_strategy)
@settings(max_examples=50)
def test_mmdsl_operatorand_instantiation(instance):
    assert isinstance(instance, mMDSL_OperatorAnd)



@given(instance=mMDSL_OperatorAnd_strategy)
def test_mmdsl_operatorand_and__setter(instance):
    original = instance.and_
    instance.and_ = original
    assert instance.and_ == original

@given(instance=mMDSL_OperatorEqual_strategy)
@settings(max_examples=50)
def test_mmdsl_operatorequal_instantiation(instance):
    assert isinstance(instance, mMDSL_OperatorEqual)



@given(instance=mMDSL_OperatorEqual_strategy)
def test_mmdsl_operatorequal_equal_setter(instance):
    original = instance.equal
    instance.equal = original
    assert instance.equal == original



@given(instance=mMDSL_OperatorEqual_strategy)
def test_mmdsl_operatorequal_notequal_setter(instance):
    original = instance.notequal
    instance.notequal = original
    assert instance.notequal == original

@given(instance=mMDSL_OperatorCompare_strategy)
@settings(max_examples=50)
def test_mmdsl_operatorcompare_instantiation(instance):
    assert isinstance(instance, mMDSL_OperatorCompare)



@given(instance=mMDSL_OperatorCompare_strategy)
def test_mmdsl_operatorcompare_greater_setter(instance):
    original = instance.greater
    instance.greater = original
    assert instance.greater == original



@given(instance=mMDSL_OperatorCompare_strategy)
def test_mmdsl_operatorcompare_lesser_setter(instance):
    original = instance.lesser
    instance.lesser = original
    assert instance.lesser == original



@given(instance=mMDSL_OperatorCompare_strategy)
def test_mmdsl_operatorcompare_lesserequal_setter(instance):
    original = instance.lesserequal
    instance.lesserequal = original
    assert instance.lesserequal == original



@given(instance=mMDSL_OperatorCompare_strategy)
def test_mmdsl_operatorcompare_greaterequal_setter(instance):
    original = instance.greaterequal
    instance.greaterequal = original
    assert instance.greaterequal == original

@given(instance=mMDSL_OperatorAdd_strategy)
@settings(max_examples=50)
def test_mmdsl_operatoradd_instantiation(instance):
    assert isinstance(instance, mMDSL_OperatorAdd)



@given(instance=mMDSL_OperatorAdd_strategy)
def test_mmdsl_operatoradd_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original



@given(instance=mMDSL_OperatorAdd_strategy)
def test_mmdsl_operatoradd_subtract_setter(instance):
    original = instance.subtract
    instance.subtract = original
    assert instance.subtract == original

@given(instance=mMDSL_OperatorMultiply_strategy)
@settings(max_examples=50)
def test_mmdsl_operatormultiply_instantiation(instance):
    assert isinstance(instance, mMDSL_OperatorMultiply)



@given(instance=mMDSL_OperatorMultiply_strategy)
def test_mmdsl_operatormultiply_modulo_setter(instance):
    original = instance.modulo
    instance.modulo = original
    assert instance.modulo == original



@given(instance=mMDSL_OperatorMultiply_strategy)
def test_mmdsl_operatormultiply_multiply_setter(instance):
    original = instance.multiply
    instance.multiply = original
    assert instance.multiply == original



@given(instance=mMDSL_OperatorMultiply_strategy)
def test_mmdsl_operatormultiply_divide_setter(instance):
    original = instance.divide
    instance.divide = original
    assert instance.divide == original

@given(instance=mMDSL_OperatorUnary_strategy)
@settings(max_examples=50)
def test_mmdsl_operatorunary_instantiation(instance):
    assert isinstance(instance, mMDSL_OperatorUnary)



@given(instance=mMDSL_OperatorUnary_strategy)
def test_mmdsl_operatorunary_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=mMDSL_OperatorMultyAssign_strategy)
@settings(max_examples=50)
def test_mmdsl_operatormultyassign_instantiation(instance):
    assert isinstance(instance, mMDSL_OperatorMultyAssign)



@given(instance=mMDSL_OperatorMultyAssign_strategy)
def test_mmdsl_operatormultyassign_divassign_setter(instance):
    original = instance.divassign
    instance.divassign = original
    assert instance.divassign == original



@given(instance=mMDSL_OperatorMultyAssign_strategy)
def test_mmdsl_operatormultyassign_multiassign_setter(instance):
    original = instance.multiassign
    instance.multiassign = original
    assert instance.multiassign == original



@given(instance=mMDSL_OperatorMultyAssign_strategy)
def test_mmdsl_operatormultyassign_subassign_setter(instance):
    original = instance.subassign
    instance.subassign = original
    assert instance.subassign == original



@given(instance=mMDSL_OperatorMultyAssign_strategy)
def test_mmdsl_operatormultyassign_addassign_setter(instance):
    original = instance.addassign
    instance.addassign = original
    assert instance.addassign == original

@given(instance=mMDSL_VarStatement_strategy)
@settings(max_examples=50)
def test_mmdsl_varstatement_instantiation(instance):
    assert isinstance(instance, mMDSL_VarStatement)

@given(instance=mMDSL_OperatorAssign_strategy)
@settings(max_examples=50)
def test_mmdsl_operatorassign_instantiation(instance):
    assert isinstance(instance, mMDSL_OperatorAssign)



@given(instance=mMDSL_OperatorAssign_strategy)
def test_mmdsl_operatorassign_assign_setter(instance):
    original = instance.assign
    instance.assign = original
    assert instance.assign == original

@given(instance=mMDSL_BreakContinue_strategy)
@settings(max_examples=50)
def test_mmdsl_breakcontinue_instantiation(instance):
    assert isinstance(instance, mMDSL_BreakContinue)



@given(instance=mMDSL_BreakContinue_strategy)
def test_mmdsl_breakcontinue_continue__setter(instance):
    original = instance.continue_
    instance.continue_ = original
    assert instance.continue_ == original



@given(instance=mMDSL_BreakContinue_strategy)
def test_mmdsl_breakcontinue_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original

@given(instance=mMDSL_ForLoop_strategy)
@settings(max_examples=50)
def test_mmdsl_forloop_instantiation(instance):
    assert isinstance(instance, mMDSL_ForLoop)



@given(instance=mMDSL_ForLoop_strategy)
def test_mmdsl_forloop_interval_setter(instance):
    original = instance.interval
    instance.interval = original
    assert instance.interval == original



@given(instance=mMDSL_ForLoop_strategy)
def test_mmdsl_forloop_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=mMDSL_ForLoop_strategy)
def test_mmdsl_forloop_stop_setter(instance):
    original = instance.stop
    instance.stop = original
    assert instance.stop == original

@given(instance=mMDSL_WhileLoop_strategy)
@settings(max_examples=50)
def test_mmdsl_whileloop_instantiation(instance):
    assert isinstance(instance, mMDSL_WhileLoop)

@given(instance=mMDSL_Expr_strategy)
@settings(max_examples=50)
def test_mmdsl_expr_instantiation(instance):
    assert isinstance(instance, mMDSL_Expr)

@given(instance=mMDSL_AlgorithmOperation_strategy)
@settings(max_examples=50)
def test_mmdsl_algorithmoperation_instantiation(instance):
    assert isinstance(instance, mMDSL_AlgorithmOperation)

@given(instance=mMDSL_Variable_strategy)
@settings(max_examples=50)
def test_mmdsl_variable_instantiation(instance):
    assert isinstance(instance, mMDSL_Variable)



@given(instance=mMDSL_Variable_strategy)
def test_mmdsl_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_LoopStatement_strategy)
@settings(max_examples=50)
def test_mmdsl_loopstatement_instantiation(instance):
    assert isinstance(instance, mMDSL_LoopStatement)

@given(instance=mMDSL_SelectionStatement_strategy)
@settings(max_examples=50)
def test_mmdsl_selectionstatement_instantiation(instance):
    assert isinstance(instance, mMDSL_SelectionStatement)

@given(instance=mMDSL_Statement_strategy)
@settings(max_examples=50)
def test_mmdsl_statement_instantiation(instance):
    assert isinstance(instance, mMDSL_Statement)

@given(instance=mMDSL_StrokeColor_strategy)
@settings(max_examples=50)
def test_mmdsl_strokecolor_instantiation(instance):
    assert isinstance(instance, mMDSL_StrokeColor)



@given(instance=mMDSL_StrokeColor_strategy)
def test_mmdsl_strokecolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=mMDSL_StrokeColor_strategy)
def test_mmdsl_strokecolor_hexcolor_setter(instance):
    original = instance.hexcolor
    instance.hexcolor = original
    assert instance.hexcolor == original

@given(instance=mMDSL_PathParametersA_strategy)
@settings(max_examples=50)
def test_mmdsl_pathparametersa_instantiation(instance):
    assert isinstance(instance, mMDSL_PathParametersA)



@given(instance=mMDSL_PathParametersA_strategy)
def test_mmdsl_pathparametersa_largearcflag_setter(instance):
    original = instance.largearcflag
    instance.largearcflag = original
    assert instance.largearcflag == original



@given(instance=mMDSL_PathParametersA_strategy)
def test_mmdsl_pathparametersa_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=mMDSL_PathParametersA_strategy)
def test_mmdsl_pathparametersa_ry_setter(instance):
    original = instance.ry
    instance.ry = original
    assert instance.ry == original



@given(instance=mMDSL_PathParametersA_strategy)
def test_mmdsl_pathparametersa_rx_setter(instance):
    original = instance.rx
    instance.rx = original
    assert instance.rx == original



@given(instance=mMDSL_PathParametersA_strategy)
def test_mmdsl_pathparametersa_sweepflag_setter(instance):
    original = instance.sweepflag
    instance.sweepflag = original
    assert instance.sweepflag == original



@given(instance=mMDSL_PathParametersA_strategy)
def test_mmdsl_pathparametersa_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=mMDSL_PathParametersA_strategy)
def test_mmdsl_pathparametersa_xaxisrot_setter(instance):
    original = instance.xaxisrot
    instance.xaxisrot = original
    assert instance.xaxisrot == original

@given(instance=mMDSL_PathParametersQ_strategy)
@settings(max_examples=50)
def test_mmdsl_pathparametersq_instantiation(instance):
    assert isinstance(instance, mMDSL_PathParametersQ)



@given(instance=mMDSL_PathParametersQ_strategy)
def test_mmdsl_pathparametersq_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=mMDSL_PathParametersQ_strategy)
def test_mmdsl_pathparametersq_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original



@given(instance=mMDSL_PathParametersQ_strategy)
def test_mmdsl_pathparametersq_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=mMDSL_PathParametersQ_strategy)
def test_mmdsl_pathparametersq_y1_setter(instance):
    original = instance.y1
    instance.y1 = original
    assert instance.y1 == original

@given(instance=mMDSL_PathParametersS_strategy)
@settings(max_examples=50)
def test_mmdsl_pathparameterss_instantiation(instance):
    assert isinstance(instance, mMDSL_PathParametersS)



@given(instance=mMDSL_PathParametersS_strategy)
def test_mmdsl_pathparameterss_y2_setter(instance):
    original = instance.y2
    instance.y2 = original
    assert instance.y2 == original



@given(instance=mMDSL_PathParametersS_strategy)
def test_mmdsl_pathparameterss_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=mMDSL_PathParametersS_strategy)
def test_mmdsl_pathparameterss_x2_setter(instance):
    original = instance.x2
    instance.x2 = original
    assert instance.x2 == original



@given(instance=mMDSL_PathParametersS_strategy)
def test_mmdsl_pathparameterss_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL_PathParametersC_strategy)
@settings(max_examples=50)
def test_mmdsl_pathparametersc_instantiation(instance):
    assert isinstance(instance, mMDSL_PathParametersC)



@given(instance=mMDSL_PathParametersC_strategy)
def test_mmdsl_pathparametersc_y1_setter(instance):
    original = instance.y1
    instance.y1 = original
    assert instance.y1 == original



@given(instance=mMDSL_PathParametersC_strategy)
def test_mmdsl_pathparametersc_x2_setter(instance):
    original = instance.x2
    instance.x2 = original
    assert instance.x2 == original



@given(instance=mMDSL_PathParametersC_strategy)
def test_mmdsl_pathparametersc_y2_setter(instance):
    original = instance.y2
    instance.y2 = original
    assert instance.y2 == original



@given(instance=mMDSL_PathParametersC_strategy)
def test_mmdsl_pathparametersc_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=mMDSL_PathParametersC_strategy)
def test_mmdsl_pathparametersc_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original



@given(instance=mMDSL_PathParametersC_strategy)
def test_mmdsl_pathparametersc_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL_PathParametersHV_strategy)
@settings(max_examples=50)
def test_mmdsl_pathparametershv_instantiation(instance):
    assert isinstance(instance, mMDSL_PathParametersHV)



@given(instance=mMDSL_PathParametersHV_strategy)
def test_mmdsl_pathparametershv_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL_PathParametersMLT_strategy)
@settings(max_examples=50)
def test_mmdsl_pathparametersmlt_instantiation(instance):
    assert isinstance(instance, mMDSL_PathParametersMLT)



@given(instance=mMDSL_PathParametersMLT_strategy)
def test_mmdsl_pathparametersmlt_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=mMDSL_PathParametersMLT_strategy)
def test_mmdsl_pathparametersmlt_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL_EllipticalArc_strategy)
@settings(max_examples=50)
def test_mmdsl_ellipticalarc_instantiation(instance):
    assert isinstance(instance, mMDSL_EllipticalArc)

@given(instance=mMDSL_SmoothQuadraticBezierCurveTo_strategy)
@settings(max_examples=50)
def test_mmdsl_smoothquadraticbeziercurveto_instantiation(instance):
    assert isinstance(instance, mMDSL_SmoothQuadraticBezierCurveTo)

@given(instance=mMDSL_QuadraticBezierCurve_strategy)
@settings(max_examples=50)
def test_mmdsl_quadraticbeziercurve_instantiation(instance):
    assert isinstance(instance, mMDSL_QuadraticBezierCurve)

@given(instance=mMDSL_SmoothCurveTo_strategy)
@settings(max_examples=50)
def test_mmdsl_smoothcurveto_instantiation(instance):
    assert isinstance(instance, mMDSL_SmoothCurveTo)

@given(instance=mMDSL_CurveTo_strategy)
@settings(max_examples=50)
def test_mmdsl_curveto_instantiation(instance):
    assert isinstance(instance, mMDSL_CurveTo)

@given(instance=mMDSL_VerticalLineTo_strategy)
@settings(max_examples=50)
def test_mmdsl_verticallineto_instantiation(instance):
    assert isinstance(instance, mMDSL_VerticalLineTo)

@given(instance=mMDSL_HorizontalLineTo_strategy)
@settings(max_examples=50)
def test_mmdsl_horizontallineto_instantiation(instance):
    assert isinstance(instance, mMDSL_HorizontalLineTo)

@given(instance=mMDSL_LineTo_strategy)
@settings(max_examples=50)
def test_mmdsl_lineto_instantiation(instance):
    assert isinstance(instance, mMDSL_LineTo)

@given(instance=mMDSL_MoveTo_strategy)
@settings(max_examples=50)
def test_mmdsl_moveto_instantiation(instance):
    assert isinstance(instance, mMDSL_MoveTo)

@given(instance=mMDSL_FillColor_strategy)
@settings(max_examples=50)
def test_mmdsl_fillcolor_instantiation(instance):
    assert isinstance(instance, mMDSL_FillColor)



@given(instance=mMDSL_FillColor_strategy)
def test_mmdsl_fillcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=mMDSL_FillColor_strategy)
def test_mmdsl_fillcolor_hexcolor_setter(instance):
    original = instance.hexcolor
    instance.hexcolor = original
    assert instance.hexcolor == original

@given(instance=mMDSL_FontFamily_strategy)
@settings(max_examples=50)
def test_mmdsl_fontfamily_instantiation(instance):
    assert isinstance(instance, mMDSL_FontFamily)



@given(instance=mMDSL_FontFamily_strategy)
def test_mmdsl_fontfamily_fontstr_setter(instance):
    original = instance.fontstr
    instance.fontstr = original
    assert instance.fontstr == original



@given(instance=mMDSL_FontFamily_strategy)
def test_mmdsl_fontfamily_font_setter(instance):
    original = instance.font
    instance.font = original
    assert instance.font == original

@given(instance=mMDSL_PathData_strategy)
@settings(max_examples=50)
def test_mmdsl_pathdata_instantiation(instance):
    assert isinstance(instance, mMDSL_PathData)



@given(instance=mMDSL_PathData_strategy)
def test_mmdsl_pathdata_closepath_setter(instance):
    original = instance.closepath
    instance.closepath = original
    assert instance.closepath == original

@given(instance=mMDSL_Points_strategy)
@settings(max_examples=50)
def test_mmdsl_points_instantiation(instance):
    assert isinstance(instance, mMDSL_Points)



@given(instance=mMDSL_Points_strategy)
def test_mmdsl_points_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=mMDSL_Points_strategy)
def test_mmdsl_points_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL_Text_strategy)
@settings(max_examples=50)
def test_mmdsl_text_instantiation(instance):
    assert isinstance(instance, mMDSL_Text)



@given(instance=mMDSL_Text_strategy)
def test_mmdsl_text_fontsize_setter(instance):
    original = instance.fontsize
    instance.fontsize = original
    assert instance.fontsize == original



@given(instance=mMDSL_Text_strategy)
def test_mmdsl_text_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=mMDSL_Text_strategy)
def test_mmdsl_text_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=mMDSL_Text_strategy)
def test_mmdsl_text_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL_Path_strategy)
@settings(max_examples=50)
def test_mmdsl_path_instantiation(instance):
    assert isinstance(instance, mMDSL_Path)

@given(instance=mMDSL_Polygon_strategy)
@settings(max_examples=50)
def test_mmdsl_polygon_instantiation(instance):
    assert isinstance(instance, mMDSL_Polygon)

@given(instance=mMDSL_Polyline_strategy)
@settings(max_examples=50)
def test_mmdsl_polyline_instantiation(instance):
    assert isinstance(instance, mMDSL_Polyline)

@given(instance=mMDSL_Line_strategy)
@settings(max_examples=50)
def test_mmdsl_line_instantiation(instance):
    assert isinstance(instance, mMDSL_Line)



@given(instance=mMDSL_Line_strategy)
def test_mmdsl_line_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original



@given(instance=mMDSL_Line_strategy)
def test_mmdsl_line_y1_setter(instance):
    original = instance.y1
    instance.y1 = original
    assert instance.y1 == original



@given(instance=mMDSL_Line_strategy)
def test_mmdsl_line_x2_setter(instance):
    original = instance.x2
    instance.x2 = original
    assert instance.x2 == original



@given(instance=mMDSL_Line_strategy)
def test_mmdsl_line_y2_setter(instance):
    original = instance.y2
    instance.y2 = original
    assert instance.y2 == original

@given(instance=mMDSL_Ellipse_strategy)
@settings(max_examples=50)
def test_mmdsl_ellipse_instantiation(instance):
    assert isinstance(instance, mMDSL_Ellipse)



@given(instance=mMDSL_Ellipse_strategy)
def test_mmdsl_ellipse_cy_setter(instance):
    original = instance.cy
    instance.cy = original
    assert instance.cy == original



@given(instance=mMDSL_Ellipse_strategy)
def test_mmdsl_ellipse_rx_setter(instance):
    original = instance.rx
    instance.rx = original
    assert instance.rx == original



@given(instance=mMDSL_Ellipse_strategy)
def test_mmdsl_ellipse_ry_setter(instance):
    original = instance.ry
    instance.ry = original
    assert instance.ry == original



@given(instance=mMDSL_Ellipse_strategy)
def test_mmdsl_ellipse_cx_setter(instance):
    original = instance.cx
    instance.cx = original
    assert instance.cx == original

@given(instance=mMDSL_Circle_strategy)
@settings(max_examples=50)
def test_mmdsl_circle_instantiation(instance):
    assert isinstance(instance, mMDSL_Circle)



@given(instance=mMDSL_Circle_strategy)
def test_mmdsl_circle_cx_setter(instance):
    original = instance.cx
    instance.cx = original
    assert instance.cx == original



@given(instance=mMDSL_Circle_strategy)
def test_mmdsl_circle_cy_setter(instance):
    original = instance.cy
    instance.cy = original
    assert instance.cy == original



@given(instance=mMDSL_Circle_strategy)
def test_mmdsl_circle_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original

@given(instance=mMDSL_Rectangle_strategy)
@settings(max_examples=50)
def test_mmdsl_rectangle_instantiation(instance):
    assert isinstance(instance, mMDSL_Rectangle)



@given(instance=mMDSL_Rectangle_strategy)
def test_mmdsl_rectangle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=mMDSL_Rectangle_strategy)
def test_mmdsl_rectangle_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=mMDSL_Rectangle_strategy)
def test_mmdsl_rectangle_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=mMDSL_Rectangle_strategy)
def test_mmdsl_rectangle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=mMDSL_SVGCommand_strategy)
@settings(max_examples=50)
def test_mmdsl_svgcommand_instantiation(instance):
    assert isinstance(instance, mMDSL_SVGCommand)

@given(instance=mMDSL_Mode_strategy)
@settings(max_examples=50)
def test_mmdsl_mode_instantiation(instance):
    assert isinstance(instance, mMDSL_Mode)



@given(instance=mMDSL_Mode_strategy)
def test_mmdsl_mode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_EnumType_strategy)
@settings(max_examples=50)
def test_mmdsl_enumtype_instantiation(instance):
    assert isinstance(instance, mMDSL_EnumType)

@given(instance=mMDSL_RefName_strategy)
@settings(max_examples=50)
def test_mmdsl_refname_instantiation(instance):
    assert isinstance(instance, mMDSL_RefName)

@given(instance=mMDSL_Type_strategy)
@settings(max_examples=50)
def test_mmdsl_type_instantiation(instance):
    assert isinstance(instance, mMDSL_Type)



@given(instance=mMDSL_Type_strategy)
def test_mmdsl_type_simpletype_setter(instance):
    original = instance.simpletype
    instance.simpletype = original
    assert instance.simpletype == original

@given(instance=mMDSL_Reference_strategy)
@settings(max_examples=50)
def test_mmdsl_reference_instantiation(instance):
    assert isinstance(instance, mMDSL_Reference)



@given(instance=mMDSL_Reference_strategy)
def test_mmdsl_reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_ClassAttribute_strategy)
@settings(max_examples=50)
def test_mmdsl_classattribute_instantiation(instance):
    assert isinstance(instance, mMDSL_ClassAttribute)



@given(instance=mMDSL_ClassAttribute_strategy)
def test_mmdsl_classattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_ModelType_strategy)
@settings(max_examples=50)
def test_mmdsl_modeltype_instantiation(instance):
    assert isinstance(instance, mMDSL_ModelType)



@given(instance=mMDSL_ModelType_strategy)
def test_mmdsl_modeltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_Attribute_strategy)
@settings(max_examples=50)
def test_mmdsl_attribute_instantiation(instance):
    assert isinstance(instance, mMDSL_Attribute)



@given(instance=mMDSL_Attribute_strategy)
def test_mmdsl_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mMDSL_Attribute_strategy)
def test_mmdsl_attribute_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=mMDSL_Relation_strategy)
@settings(max_examples=50)
def test_mmdsl_relation_instantiation(instance):
    assert isinstance(instance, mMDSL_Relation)



@given(instance=mMDSL_Relation_strategy)
def test_mmdsl_relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_Class_strategy)
@settings(max_examples=50)
def test_mmdsl_class_instantiation(instance):
    assert isinstance(instance, mMDSL_Class)



@given(instance=mMDSL_Class_strategy)
def test_mmdsl_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_Event_strategy)
@settings(max_examples=50)
def test_mmdsl_event_instantiation(instance):
    assert isinstance(instance, mMDSL_Event)



@given(instance=mMDSL_Event_strategy)
def test_mmdsl_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_Algorithm_strategy)
@settings(max_examples=50)
def test_mmdsl_algorithm_instantiation(instance):
    assert isinstance(instance, mMDSL_Algorithm)



@given(instance=mMDSL_Algorithm_strategy)
def test_mmdsl_algorithm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_Metamodel_strategy)
@settings(max_examples=50)
def test_mmdsl_metamodel_instantiation(instance):
    assert isinstance(instance, mMDSL_Metamodel)

@given(instance=mMDSL_SymbolRelation_strategy)
@settings(max_examples=50)
def test_mmdsl_symbolrelation_instantiation(instance):
    assert isinstance(instance, mMDSL_SymbolRelation)



@given(instance=mMDSL_SymbolRelation_strategy)
def test_mmdsl_symbolrelation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_SymbolClass_strategy)
@settings(max_examples=50)
def test_mmdsl_symbolclass_instantiation(instance):
    assert isinstance(instance, mMDSL_SymbolClass)



@given(instance=mMDSL_SymbolClass_strategy)
def test_mmdsl_symbolclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_SymbolStyle_strategy)
@settings(max_examples=50)
def test_mmdsl_symbolstyle_instantiation(instance):
    assert isinstance(instance, mMDSL_SymbolStyle)



@given(instance=mMDSL_SymbolStyle_strategy)
def test_mmdsl_symbolstyle_fontsize_setter(instance):
    original = instance.fontsize
    instance.fontsize = original
    assert instance.fontsize == original



@given(instance=mMDSL_SymbolStyle_strategy)
def test_mmdsl_symbolstyle_strokewidth_setter(instance):
    original = instance.strokewidth
    instance.strokewidth = original
    assert instance.strokewidth == original



@given(instance=mMDSL_SymbolStyle_strategy)
def test_mmdsl_symbolstyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_Enumeration_strategy)
@settings(max_examples=50)
def test_mmdsl_enumeration_instantiation(instance):
    assert isinstance(instance, mMDSL_Enumeration)



@given(instance=mMDSL_Enumeration_strategy)
def test_mmdsl_enumeration_enumvalues_setter(instance):
    original = instance.enumvalues
    instance.enumvalues = original
    assert instance.enumvalues == original



@given(instance=mMDSL_Enumeration_strategy)
def test_mmdsl_enumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_InsertEmbedCode_strategy)
@settings(max_examples=50)
def test_mmdsl_insertembedcode_instantiation(instance):
    assert isinstance(instance, mMDSL_InsertEmbedCode)

@given(instance=mMDSL_Method_strategy)
@settings(max_examples=50)
def test_mmdsl_method_instantiation(instance):
    assert isinstance(instance, mMDSL_Method)

@given(instance=mMDSL_EmbedCode_strategy)
@settings(max_examples=50)
def test_mmdsl_embedcode_instantiation(instance):
    assert isinstance(instance, mMDSL_EmbedCode)



@given(instance=mMDSL_EmbedCode_strategy)
def test_mmdsl_embedcode_embeddedcode_setter(instance):
    original = instance.embeddedcode
    instance.embeddedcode = original
    assert instance.embeddedcode == original



@given(instance=mMDSL_EmbedCode_strategy)
def test_mmdsl_embedcode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_IncludeLibrary_strategy)
@settings(max_examples=50)
def test_mmdsl_includelibrary_instantiation(instance):
    assert isinstance(instance, mMDSL_IncludeLibrary)



@given(instance=mMDSL_IncludeLibrary_strategy)
def test_mmdsl_includelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_EmbedCodeType_strategy)
@settings(max_examples=50)
def test_mmdsl_embedcodetype_instantiation(instance):
    assert isinstance(instance, mMDSL_EmbedCodeType)



@given(instance=mMDSL_EmbedCodeType_strategy)
def test_mmdsl_embedcodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_EmbedPlatformType_strategy)
@settings(max_examples=50)
def test_mmdsl_embedplatformtype_instantiation(instance):
    assert isinstance(instance, mMDSL_EmbedPlatformType)



@given(instance=mMDSL_EmbedPlatformType_strategy)
def test_mmdsl_embedplatformtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_IncludeLibraryType_strategy)
@settings(max_examples=50)
def test_mmdsl_includelibrarytype_instantiation(instance):
    assert isinstance(instance, mMDSL_IncludeLibraryType)



@given(instance=mMDSL_IncludeLibraryType_strategy)
def test_mmdsl_includelibrarytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_MethodName_strategy)
@settings(max_examples=50)
def test_mmdsl_methodname_instantiation(instance):
    assert isinstance(instance, mMDSL_MethodName)



@given(instance=mMDSL_MethodName_strategy)
def test_mmdsl_methodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL_Root_strategy)
@settings(max_examples=50)
def test_mmdsl_root_instantiation(instance):
    assert isinstance(instance, mMDSL_Root)
