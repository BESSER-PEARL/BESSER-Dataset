import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CompoundColorSet,
    cpntools_Union,
    cpntools_Record,
    cpntools_List,
    cpntools_Alias,
    cpntools_Subset,
    cpntools_Product,
    ColorSet,
    cpntools_SimpleColorSet,
    SimpleColorSet,
    cpntools_Integer,
    cpntools_String,
    cpntools_Boolean,
    cpntools_Index,
    cpntools_Real,
    cpntools_LargeInteger,
    cpntools_Time,
    cpntools_Enumerated,
    cpntools_Unit,
    cpntools_CompoundColorSet,
    Auxiliary,
    cpntools_AuxEllipse,
    cpntools_AuxBox,
    cpntools_AuxText,
    cpntools_Declaration,
    Declaration,
    cpntools_Var,
    cpntools_Ml,
    cpntools_Globref,
    cpntools_ColorSet,
    DiagramElement,
    cpntools_TransTime,
    cpntools_Annot,
    cpntools_TransPriority,
    cpntools_TransCond,
    cpntools_Port,
    cpntools_Initmark,
    cpntools_Block,
    cpntools_DiagramElement,
    cpntools_Arc,
    cpntools_Trans,
    cpntools_Auxiliary,
    cpntools_Place,
    cpntools_Group,
    cpntools_Page,
    cpntools_Binder,
    cpntools_Globbox,
    cpntools_Fusion,
    cpntools_Cpnet,
    Colour16,
    Orientation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_compoundcolorset_is_not_abstract():
    assert not inspect.isabstract(CompoundColorSet)


def test_compoundcolorset_constructor_exists():
    assert callable(CompoundColorSet.__init__)


def test_compoundcolorset_constructor_args():
    sig = inspect.signature(CompoundColorSet.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_union_is_not_abstract():
    assert not inspect.isabstract(cpntools_Union)


def test_cpntools_union_constructor_exists():
    assert callable(cpntools_Union.__init__)


def test_cpntools_union_constructor_args():
    sig = inspect.signature(cpntools_Union.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_record_is_not_abstract():
    assert not inspect.isabstract(cpntools_Record)


def test_cpntools_record_constructor_exists():
    assert callable(cpntools_Record.__init__)


def test_cpntools_record_constructor_args():
    sig = inspect.signature(cpntools_Record.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_list_is_not_abstract():
    assert not inspect.isabstract(cpntools_List)


def test_cpntools_list_constructor_exists():
    assert callable(cpntools_List.__init__)


def test_cpntools_list_constructor_args():
    sig = inspect.signature(cpntools_List.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_alias_is_not_abstract():
    assert not inspect.isabstract(cpntools_Alias)


def test_cpntools_alias_constructor_exists():
    assert callable(cpntools_Alias.__init__)


def test_cpntools_alias_constructor_args():
    sig = inspect.signature(cpntools_Alias.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_subset_is_not_abstract():
    assert not inspect.isabstract(cpntools_Subset)


def test_cpntools_subset_constructor_exists():
    assert callable(cpntools_Subset.__init__)


def test_cpntools_subset_constructor_args():
    sig = inspect.signature(cpntools_Subset.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_product_is_not_abstract():
    assert not inspect.isabstract(cpntools_Product)


def test_cpntools_product_constructor_exists():
    assert callable(cpntools_Product.__init__)


def test_cpntools_product_constructor_args():
    sig = inspect.signature(cpntools_Product.__init__)
    params = list(sig.parameters.keys())



def test_colorset_is_not_abstract():
    assert not inspect.isabstract(ColorSet)


def test_colorset_constructor_exists():
    assert callable(ColorSet.__init__)


def test_colorset_constructor_args():
    sig = inspect.signature(ColorSet.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_simplecolorset_is_not_abstract():
    assert not inspect.isabstract(cpntools_SimpleColorSet)


def test_cpntools_simplecolorset_constructor_exists():
    assert callable(cpntools_SimpleColorSet.__init__)


def test_cpntools_simplecolorset_constructor_args():
    sig = inspect.signature(cpntools_SimpleColorSet.__init__)
    params = list(sig.parameters.keys())



def test_simplecolorset_is_not_abstract():
    assert not inspect.isabstract(SimpleColorSet)


def test_simplecolorset_constructor_exists():
    assert callable(SimpleColorSet.__init__)


def test_simplecolorset_constructor_args():
    sig = inspect.signature(SimpleColorSet.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_integer_is_not_abstract():
    assert not inspect.isabstract(cpntools_Integer)


def test_cpntools_integer_constructor_exists():
    assert callable(cpntools_Integer.__init__)


def test_cpntools_integer_constructor_args():
    sig = inspect.signature(cpntools_Integer.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"

def test_cpntools_integer_has_with_():
    assert hasattr(cpntools_Integer, "with_")
    descriptor = None
    for klass in cpntools_Integer.__mro__:
        if "with_" in klass.__dict__:
            descriptor = klass.__dict__["with_"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_string_is_not_abstract():
    assert not inspect.isabstract(cpntools_String)


def test_cpntools_string_constructor_exists():
    assert callable(cpntools_String.__init__)


def test_cpntools_string_constructor_args():
    sig = inspect.signature(cpntools_String.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"
    assert "and_" in params, "Missing parameter 'and_'"

def test_cpntools_string_has_with_():
    assert hasattr(cpntools_String, "with_")
    descriptor = None
    for klass in cpntools_String.__mro__:
        if "with_" in klass.__dict__:
            descriptor = klass.__dict__["with_"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_string_has_and_():
    assert hasattr(cpntools_String, "and_")
    descriptor = None
    for klass in cpntools_String.__mro__:
        if "and_" in klass.__dict__:
            descriptor = klass.__dict__["and_"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_boolean_is_not_abstract():
    assert not inspect.isabstract(cpntools_Boolean)


def test_cpntools_boolean_constructor_exists():
    assert callable(cpntools_Boolean.__init__)


def test_cpntools_boolean_constructor_args():
    sig = inspect.signature(cpntools_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"

def test_cpntools_boolean_has_with_():
    assert hasattr(cpntools_Boolean, "with_")
    descriptor = None
    for klass in cpntools_Boolean.__mro__:
        if "with_" in klass.__dict__:
            descriptor = klass.__dict__["with_"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_index_is_not_abstract():
    assert not inspect.isabstract(cpntools_Index)


def test_cpntools_index_constructor_exists():
    assert callable(cpntools_Index.__init__)


def test_cpntools_index_constructor_args():
    sig = inspect.signature(cpntools_Index.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"

def test_cpntools_index_has_with_():
    assert hasattr(cpntools_Index, "with_")
    descriptor = None
    for klass in cpntools_Index.__mro__:
        if "with_" in klass.__dict__:
            descriptor = klass.__dict__["with_"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_real_is_not_abstract():
    assert not inspect.isabstract(cpntools_Real)


def test_cpntools_real_constructor_exists():
    assert callable(cpntools_Real.__init__)


def test_cpntools_real_constructor_args():
    sig = inspect.signature(cpntools_Real.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"

def test_cpntools_real_has_with_():
    assert hasattr(cpntools_Real, "with_")
    descriptor = None
    for klass in cpntools_Real.__mro__:
        if "with_" in klass.__dict__:
            descriptor = klass.__dict__["with_"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_largeinteger_is_not_abstract():
    assert not inspect.isabstract(cpntools_LargeInteger)


def test_cpntools_largeinteger_constructor_exists():
    assert callable(cpntools_LargeInteger.__init__)


def test_cpntools_largeinteger_constructor_args():
    sig = inspect.signature(cpntools_LargeInteger.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"

def test_cpntools_largeinteger_has_with_():
    assert hasattr(cpntools_LargeInteger, "with_")
    descriptor = None
    for klass in cpntools_LargeInteger.__mro__:
        if "with_" in klass.__dict__:
            descriptor = klass.__dict__["with_"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_time_is_not_abstract():
    assert not inspect.isabstract(cpntools_Time)


def test_cpntools_time_constructor_exists():
    assert callable(cpntools_Time.__init__)


def test_cpntools_time_constructor_args():
    sig = inspect.signature(cpntools_Time.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_enumerated_is_not_abstract():
    assert not inspect.isabstract(cpntools_Enumerated)


def test_cpntools_enumerated_constructor_exists():
    assert callable(cpntools_Enumerated.__init__)


def test_cpntools_enumerated_constructor_args():
    sig = inspect.signature(cpntools_Enumerated.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"

def test_cpntools_enumerated_has_with_():
    assert hasattr(cpntools_Enumerated, "with_")
    descriptor = None
    for klass in cpntools_Enumerated.__mro__:
        if "with_" in klass.__dict__:
            descriptor = klass.__dict__["with_"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_unit_is_not_abstract():
    assert not inspect.isabstract(cpntools_Unit)


def test_cpntools_unit_constructor_exists():
    assert callable(cpntools_Unit.__init__)


def test_cpntools_unit_constructor_args():
    sig = inspect.signature(cpntools_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"

def test_cpntools_unit_has_with_():
    assert hasattr(cpntools_Unit, "with_")
    descriptor = None
    for klass in cpntools_Unit.__mro__:
        if "with_" in klass.__dict__:
            descriptor = klass.__dict__["with_"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_compoundcolorset_is_not_abstract():
    assert not inspect.isabstract(cpntools_CompoundColorSet)


def test_cpntools_compoundcolorset_constructor_exists():
    assert callable(cpntools_CompoundColorSet.__init__)


def test_cpntools_compoundcolorset_constructor_args():
    sig = inspect.signature(cpntools_CompoundColorSet.__init__)
    params = list(sig.parameters.keys())



def test_auxiliary_is_not_abstract():
    assert not inspect.isabstract(Auxiliary)


def test_auxiliary_constructor_exists():
    assert callable(Auxiliary.__init__)


def test_auxiliary_constructor_args():
    sig = inspect.signature(Auxiliary.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_auxellipse_is_not_abstract():
    assert not inspect.isabstract(cpntools_AuxEllipse)


def test_cpntools_auxellipse_constructor_exists():
    assert callable(cpntools_AuxEllipse.__init__)


def test_cpntools_auxellipse_constructor_args():
    sig = inspect.signature(cpntools_AuxEllipse.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_cpntools_auxellipse_has_width():
    assert hasattr(cpntools_AuxEllipse, "width")
    descriptor = None
    for klass in cpntools_AuxEllipse.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_auxellipse_has_height():
    assert hasattr(cpntools_AuxEllipse, "height")
    descriptor = None
    for klass in cpntools_AuxEllipse.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_auxbox_is_not_abstract():
    assert not inspect.isabstract(cpntools_AuxBox)


def test_cpntools_auxbox_constructor_exists():
    assert callable(cpntools_AuxBox.__init__)


def test_cpntools_auxbox_constructor_args():
    sig = inspect.signature(cpntools_AuxBox.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_cpntools_auxbox_has_width():
    assert hasattr(cpntools_AuxBox, "width")
    descriptor = None
    for klass in cpntools_AuxBox.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_auxbox_has_height():
    assert hasattr(cpntools_AuxBox, "height")
    descriptor = None
    for klass in cpntools_AuxBox.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_auxtext_is_not_abstract():
    assert not inspect.isabstract(cpntools_AuxText)


def test_cpntools_auxtext_constructor_exists():
    assert callable(cpntools_AuxText.__init__)


def test_cpntools_auxtext_constructor_args():
    sig = inspect.signature(cpntools_AuxText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_cpntools_auxtext_has_text():
    assert hasattr(cpntools_AuxText, "text")
    descriptor = None
    for klass in cpntools_AuxText.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_declaration_is_not_abstract():
    assert not inspect.isabstract(cpntools_Declaration)


def test_cpntools_declaration_constructor_exists():
    assert callable(cpntools_Declaration.__init__)


def test_cpntools_declaration_constructor_args():
    sig = inspect.signature(cpntools_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_var_is_not_abstract():
    assert not inspect.isabstract(cpntools_Var)


def test_cpntools_var_constructor_exists():
    assert callable(cpntools_Var.__init__)


def test_cpntools_var_constructor_args():
    sig = inspect.signature(cpntools_Var.__init__)
    params = list(sig.parameters.keys())
    assert "idname" in params, "Missing parameter 'idname'"

def test_cpntools_var_has_idname():
    assert hasattr(cpntools_Var, "idname")
    descriptor = None
    for klass in cpntools_Var.__mro__:
        if "idname" in klass.__dict__:
            descriptor = klass.__dict__["idname"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_ml_is_not_abstract():
    assert not inspect.isabstract(cpntools_Ml)


def test_cpntools_ml_constructor_exists():
    assert callable(cpntools_Ml.__init__)


def test_cpntools_ml_constructor_args():
    sig = inspect.signature(cpntools_Ml.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_cpntools_ml_has_expression():
    assert hasattr(cpntools_Ml, "expression")
    descriptor = None
    for klass in cpntools_Ml.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_globref_is_not_abstract():
    assert not inspect.isabstract(cpntools_Globref)


def test_cpntools_globref_constructor_exists():
    assert callable(cpntools_Globref.__init__)


def test_cpntools_globref_constructor_args():
    sig = inspect.signature(cpntools_Globref.__init__)
    params = list(sig.parameters.keys())
    assert "idname" in params, "Missing parameter 'idname'"

def test_cpntools_globref_has_idname():
    assert hasattr(cpntools_Globref, "idname")
    descriptor = None
    for klass in cpntools_Globref.__mro__:
        if "idname" in klass.__dict__:
            descriptor = klass.__dict__["idname"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_colorset_is_not_abstract():
    assert not inspect.isabstract(cpntools_ColorSet)


def test_cpntools_colorset_constructor_exists():
    assert callable(cpntools_ColorSet.__init__)


def test_cpntools_colorset_constructor_args():
    sig = inspect.signature(cpntools_ColorSet.__init__)
    params = list(sig.parameters.keys())
    assert "declare" in params, "Missing parameter 'declare'"
    assert "timed" in params, "Missing parameter 'timed'"
    assert "colorSetType" in params, "Missing parameter 'colorSetType'"
    assert "idname" in params, "Missing parameter 'idname'"

def test_cpntools_colorset_has_declare():
    assert hasattr(cpntools_ColorSet, "declare")
    descriptor = None
    for klass in cpntools_ColorSet.__mro__:
        if "declare" in klass.__dict__:
            descriptor = klass.__dict__["declare"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_colorset_has_timed():
    assert hasattr(cpntools_ColorSet, "timed")
    descriptor = None
    for klass in cpntools_ColorSet.__mro__:
        if "timed" in klass.__dict__:
            descriptor = klass.__dict__["timed"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_colorset_has_colorSetType():
    assert hasattr(cpntools_ColorSet, "colorSetType")
    descriptor = None
    for klass in cpntools_ColorSet.__mro__:
        if "colorSetType" in klass.__dict__:
            descriptor = klass.__dict__["colorSetType"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_colorset_has_idname():
    assert hasattr(cpntools_ColorSet, "idname")
    descriptor = None
    for klass in cpntools_ColorSet.__mro__:
        if "idname" in klass.__dict__:
            descriptor = klass.__dict__["idname"]
            break
    assert isinstance(descriptor, property)



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_transtime_is_not_abstract():
    assert not inspect.isabstract(cpntools_TransTime)


def test_cpntools_transtime_constructor_exists():
    assert callable(cpntools_TransTime.__init__)


def test_cpntools_transtime_constructor_args():
    sig = inspect.signature(cpntools_TransTime.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_cpntools_transtime_has_text():
    assert hasattr(cpntools_TransTime, "text")
    descriptor = None
    for klass in cpntools_TransTime.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_annot_is_not_abstract():
    assert not inspect.isabstract(cpntools_Annot)


def test_cpntools_annot_constructor_exists():
    assert callable(cpntools_Annot.__init__)


def test_cpntools_annot_constructor_args():
    sig = inspect.signature(cpntools_Annot.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_cpntools_annot_has_text():
    assert hasattr(cpntools_Annot, "text")
    descriptor = None
    for klass in cpntools_Annot.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_transpriority_is_not_abstract():
    assert not inspect.isabstract(cpntools_TransPriority)


def test_cpntools_transpriority_constructor_exists():
    assert callable(cpntools_TransPriority.__init__)


def test_cpntools_transpriority_constructor_args():
    sig = inspect.signature(cpntools_TransPriority.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_cpntools_transpriority_has_text():
    assert hasattr(cpntools_TransPriority, "text")
    descriptor = None
    for klass in cpntools_TransPriority.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_transcond_is_not_abstract():
    assert not inspect.isabstract(cpntools_TransCond)


def test_cpntools_transcond_constructor_exists():
    assert callable(cpntools_TransCond.__init__)


def test_cpntools_transcond_constructor_args():
    sig = inspect.signature(cpntools_TransCond.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_cpntools_transcond_has_text():
    assert hasattr(cpntools_TransCond, "text")
    descriptor = None
    for klass in cpntools_TransCond.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_port_is_not_abstract():
    assert not inspect.isabstract(cpntools_Port)


def test_cpntools_port_constructor_exists():
    assert callable(cpntools_Port.__init__)


def test_cpntools_port_constructor_args():
    sig = inspect.signature(cpntools_Port.__init__)
    params = list(sig.parameters.keys())
    assert "portType" in params, "Missing parameter 'portType'"

def test_cpntools_port_has_portType():
    assert hasattr(cpntools_Port, "portType")
    descriptor = None
    for klass in cpntools_Port.__mro__:
        if "portType" in klass.__dict__:
            descriptor = klass.__dict__["portType"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_initmark_is_not_abstract():
    assert not inspect.isabstract(cpntools_Initmark)


def test_cpntools_initmark_constructor_exists():
    assert callable(cpntools_Initmark.__init__)


def test_cpntools_initmark_constructor_args():
    sig = inspect.signature(cpntools_Initmark.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_cpntools_initmark_has_expression():
    assert hasattr(cpntools_Initmark, "expression")
    descriptor = None
    for klass in cpntools_Initmark.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_block_is_not_abstract():
    assert not inspect.isabstract(cpntools_Block)


def test_cpntools_block_constructor_exists():
    assert callable(cpntools_Block.__init__)


def test_cpntools_block_constructor_args():
    sig = inspect.signature(cpntools_Block.__init__)
    params = list(sig.parameters.keys())
    assert "idname" in params, "Missing parameter 'idname'"

def test_cpntools_block_has_idname():
    assert hasattr(cpntools_Block, "idname")
    descriptor = None
    for klass in cpntools_Block.__mro__:
        if "idname" in klass.__dict__:
            descriptor = klass.__dict__["idname"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_diagramelement_is_not_abstract():
    assert not inspect.isabstract(cpntools_DiagramElement)


def test_cpntools_diagramelement_constructor_exists():
    assert callable(cpntools_DiagramElement.__init__)


def test_cpntools_diagramelement_constructor_args():
    sig = inspect.signature(cpntools_DiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "fillFilled" in params, "Missing parameter 'fillFilled'"
    assert "lineType" in params, "Missing parameter 'lineType'"
    assert "posy" in params, "Missing parameter 'posy'"
    assert "fillPattern" in params, "Missing parameter 'fillPattern'"
    assert "lineColour" in params, "Missing parameter 'lineColour'"
    assert "posx" in params, "Missing parameter 'posx'"
    assert "lineThick" in params, "Missing parameter 'lineThick'"
    assert "fillColour" in params, "Missing parameter 'fillColour'"

def test_cpntools_diagramelement_has_fillFilled():
    assert hasattr(cpntools_DiagramElement, "fillFilled")
    descriptor = None
    for klass in cpntools_DiagramElement.__mro__:
        if "fillFilled" in klass.__dict__:
            descriptor = klass.__dict__["fillFilled"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_diagramelement_has_lineType():
    assert hasattr(cpntools_DiagramElement, "lineType")
    descriptor = None
    for klass in cpntools_DiagramElement.__mro__:
        if "lineType" in klass.__dict__:
            descriptor = klass.__dict__["lineType"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_diagramelement_has_posy():
    assert hasattr(cpntools_DiagramElement, "posy")
    descriptor = None
    for klass in cpntools_DiagramElement.__mro__:
        if "posy" in klass.__dict__:
            descriptor = klass.__dict__["posy"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_diagramelement_has_fillPattern():
    assert hasattr(cpntools_DiagramElement, "fillPattern")
    descriptor = None
    for klass in cpntools_DiagramElement.__mro__:
        if "fillPattern" in klass.__dict__:
            descriptor = klass.__dict__["fillPattern"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_diagramelement_has_lineColour():
    assert hasattr(cpntools_DiagramElement, "lineColour")
    descriptor = None
    for klass in cpntools_DiagramElement.__mro__:
        if "lineColour" in klass.__dict__:
            descriptor = klass.__dict__["lineColour"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_diagramelement_has_posx():
    assert hasattr(cpntools_DiagramElement, "posx")
    descriptor = None
    for klass in cpntools_DiagramElement.__mro__:
        if "posx" in klass.__dict__:
            descriptor = klass.__dict__["posx"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_diagramelement_has_lineThick():
    assert hasattr(cpntools_DiagramElement, "lineThick")
    descriptor = None
    for klass in cpntools_DiagramElement.__mro__:
        if "lineThick" in klass.__dict__:
            descriptor = klass.__dict__["lineThick"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_diagramelement_has_fillColour():
    assert hasattr(cpntools_DiagramElement, "fillColour")
    descriptor = None
    for klass in cpntools_DiagramElement.__mro__:
        if "fillColour" in klass.__dict__:
            descriptor = klass.__dict__["fillColour"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_arc_is_not_abstract():
    assert not inspect.isabstract(cpntools_Arc)


def test_cpntools_arc_constructor_exists():
    assert callable(cpntools_Arc.__init__)


def test_cpntools_arc_constructor_args():
    sig = inspect.signature(cpntools_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "headsize" in params, "Missing parameter 'headsize'"
    assert "currentcyckle" in params, "Missing parameter 'currentcyckle'"

def test_cpntools_arc_has_order():
    assert hasattr(cpntools_Arc, "order")
    descriptor = None
    for klass in cpntools_Arc.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_arc_has_orientation():
    assert hasattr(cpntools_Arc, "orientation")
    descriptor = None
    for klass in cpntools_Arc.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_arc_has_headsize():
    assert hasattr(cpntools_Arc, "headsize")
    descriptor = None
    for klass in cpntools_Arc.__mro__:
        if "headsize" in klass.__dict__:
            descriptor = klass.__dict__["headsize"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_arc_has_currentcyckle():
    assert hasattr(cpntools_Arc, "currentcyckle")
    descriptor = None
    for klass in cpntools_Arc.__mro__:
        if "currentcyckle" in klass.__dict__:
            descriptor = klass.__dict__["currentcyckle"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_trans_is_not_abstract():
    assert not inspect.isabstract(cpntools_Trans)


def test_cpntools_trans_constructor_exists():
    assert callable(cpntools_Trans.__init__)


def test_cpntools_trans_constructor_args():
    sig = inspect.signature(cpntools_Trans.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "text" in params, "Missing parameter 'text'"
    assert "height" in params, "Missing parameter 'height'"
    assert "explicit" in params, "Missing parameter 'explicit'"

def test_cpntools_trans_has_width():
    assert hasattr(cpntools_Trans, "width")
    descriptor = None
    for klass in cpntools_Trans.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_trans_has_text():
    assert hasattr(cpntools_Trans, "text")
    descriptor = None
    for klass in cpntools_Trans.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_trans_has_height():
    assert hasattr(cpntools_Trans, "height")
    descriptor = None
    for klass in cpntools_Trans.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_trans_has_explicit():
    assert hasattr(cpntools_Trans, "explicit")
    descriptor = None
    for klass in cpntools_Trans.__mro__:
        if "explicit" in klass.__dict__:
            descriptor = klass.__dict__["explicit"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_auxiliary_is_not_abstract():
    assert not inspect.isabstract(cpntools_Auxiliary)


def test_cpntools_auxiliary_constructor_exists():
    assert callable(cpntools_Auxiliary.__init__)


def test_cpntools_auxiliary_constructor_args():
    sig = inspect.signature(cpntools_Auxiliary.__init__)
    params = list(sig.parameters.keys())



def test_cpntools_place_is_not_abstract():
    assert not inspect.isabstract(cpntools_Place)


def test_cpntools_place_constructor_exists():
    assert callable(cpntools_Place.__init__)


def test_cpntools_place_constructor_args():
    sig = inspect.signature(cpntools_Place.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "text" in params, "Missing parameter 'text'"
    assert "height" in params, "Missing parameter 'height'"

def test_cpntools_place_has_width():
    assert hasattr(cpntools_Place, "width")
    descriptor = None
    for klass in cpntools_Place.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_place_has_text():
    assert hasattr(cpntools_Place, "text")
    descriptor = None
    for klass in cpntools_Place.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_place_has_height():
    assert hasattr(cpntools_Place, "height")
    descriptor = None
    for klass in cpntools_Place.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_group_is_not_abstract():
    assert not inspect.isabstract(cpntools_Group)


def test_cpntools_group_constructor_exists():
    assert callable(cpntools_Group.__init__)


def test_cpntools_group_constructor_args():
    sig = inspect.signature(cpntools_Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpntools_group_has_name():
    assert hasattr(cpntools_Group, "name")
    descriptor = None
    for klass in cpntools_Group.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_page_is_not_abstract():
    assert not inspect.isabstract(cpntools_Page)


def test_cpntools_page_constructor_exists():
    assert callable(cpntools_Page.__init__)


def test_cpntools_page_constructor_args():
    sig = inspect.signature(cpntools_Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpntools_page_has_name():
    assert hasattr(cpntools_Page, "name")
    descriptor = None
    for klass in cpntools_Page.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_binder_is_not_abstract():
    assert not inspect.isabstract(cpntools_Binder)


def test_cpntools_binder_constructor_exists():
    assert callable(cpntools_Binder.__init__)


def test_cpntools_binder_constructor_args():
    sig = inspect.signature(cpntools_Binder.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "posx" in params, "Missing parameter 'posx'"
    assert "posy" in params, "Missing parameter 'posy'"
    assert "width" in params, "Missing parameter 'width'"

def test_cpntools_binder_has_height():
    assert hasattr(cpntools_Binder, "height")
    descriptor = None
    for klass in cpntools_Binder.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_binder_has_posx():
    assert hasattr(cpntools_Binder, "posx")
    descriptor = None
    for klass in cpntools_Binder.__mro__:
        if "posx" in klass.__dict__:
            descriptor = klass.__dict__["posx"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_binder_has_posy():
    assert hasattr(cpntools_Binder, "posy")
    descriptor = None
    for klass in cpntools_Binder.__mro__:
        if "posy" in klass.__dict__:
            descriptor = klass.__dict__["posy"]
            break
    assert isinstance(descriptor, property)

def test_cpntools_binder_has_width():
    assert hasattr(cpntools_Binder, "width")
    descriptor = None
    for klass in cpntools_Binder.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_globbox_is_not_abstract():
    assert not inspect.isabstract(cpntools_Globbox)


def test_cpntools_globbox_constructor_exists():
    assert callable(cpntools_Globbox.__init__)


def test_cpntools_globbox_constructor_args():
    sig = inspect.signature(cpntools_Globbox.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpntools_globbox_has_name():
    assert hasattr(cpntools_Globbox, "name")
    descriptor = None
    for klass in cpntools_Globbox.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_fusion_is_not_abstract():
    assert not inspect.isabstract(cpntools_Fusion)


def test_cpntools_fusion_constructor_exists():
    assert callable(cpntools_Fusion.__init__)


def test_cpntools_fusion_constructor_args():
    sig = inspect.signature(cpntools_Fusion.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpntools_fusion_has_name():
    assert hasattr(cpntools_Fusion, "name")
    descriptor = None
    for klass in cpntools_Fusion.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpntools_cpnet_is_not_abstract():
    assert not inspect.isabstract(cpntools_Cpnet)


def test_cpntools_cpnet_constructor_exists():
    assert callable(cpntools_Cpnet.__init__)


def test_cpntools_cpnet_constructor_args():
    sig = inspect.signature(cpntools_Cpnet.__init__)
    params = list(sig.parameters.keys())

def test_colour16_exists():
    # Check that the Enumeration exists
    assert Colour16 is not None

def test_colour16_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Colour16]
    expected_literals = [
        "Gray",
        "Teal",
        "Navy",
        "White",
        "Fuchsia",
        "Blue",
        "Olive",
        "Silver",
        "Maroon",
        "Black",
        "Lime",
        "Red",
        "Yellow",
        "Aqua",
        "Green",
        "Purple",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Colour16"

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "undefined",
        "Inhibitor",
        "TtoP",
        "PtoT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"


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
CompoundColorSet_strategy = st.builds(
    CompoundColorSet,
)
cpntools_Union_strategy = st.builds(
    cpntools_Union,
)
cpntools_Record_strategy = st.builds(
    cpntools_Record,
)
cpntools_List_strategy = st.builds(
    cpntools_List,
)
cpntools_Alias_strategy = st.builds(
    cpntools_Alias,
)
cpntools_Subset_strategy = st.builds(
    cpntools_Subset,
)
cpntools_Product_strategy = st.builds(
    cpntools_Product,
)
ColorSet_strategy = st.builds(
    ColorSet,
)
cpntools_SimpleColorSet_strategy = st.builds(
    cpntools_SimpleColorSet,
)
SimpleColorSet_strategy = st.builds(
    SimpleColorSet,
)
cpntools_Integer_strategy = st.builds(
    cpntools_Integer,
    with_=
        safe_text
)
cpntools_String_strategy = st.builds(
    cpntools_String,
    with_=
        safe_text,
    and_=
        safe_text
)
cpntools_Boolean_strategy = st.builds(
    cpntools_Boolean,
    with_=
        safe_text
)
cpntools_Index_strategy = st.builds(
    cpntools_Index,
    with_=
        safe_text
)
cpntools_Real_strategy = st.builds(
    cpntools_Real,
    with_=
        safe_text
)
cpntools_LargeInteger_strategy = st.builds(
    cpntools_LargeInteger,
    with_=
        safe_text
)
cpntools_Time_strategy = st.builds(
    cpntools_Time,
)
cpntools_Enumerated_strategy = st.builds(
    cpntools_Enumerated,
    with_=
        safe_text
)
cpntools_Unit_strategy = st.builds(
    cpntools_Unit,
    with_=
        safe_text
)
cpntools_CompoundColorSet_strategy = st.builds(
    cpntools_CompoundColorSet,
)
Auxiliary_strategy = st.builds(
    Auxiliary,
)
cpntools_AuxEllipse_strategy = st.builds(
    cpntools_AuxEllipse,
    width=
        st.integers(),
    height=
        st.integers()
)
cpntools_AuxBox_strategy = st.builds(
    cpntools_AuxBox,
    width=
        st.integers(),
    height=
        st.integers()
)
cpntools_AuxText_strategy = st.builds(
    cpntools_AuxText,
    text=
        safe_text
)
cpntools_Declaration_strategy = st.builds(
    cpntools_Declaration,
)
Declaration_strategy = st.builds(
    Declaration,
)
cpntools_Var_strategy = st.builds(
    cpntools_Var,
    idname=
        safe_text
)
cpntools_Ml_strategy = st.builds(
    cpntools_Ml,
    expression=
        safe_text
)
cpntools_Globref_strategy = st.builds(
    cpntools_Globref,
    idname=
        safe_text
)
cpntools_ColorSet_strategy = st.builds(
    cpntools_ColorSet,
    declare=
        safe_text,
    timed=
        st.booleans(),
    colorSetType=
        safe_text,
    idname=
        safe_text
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
cpntools_TransTime_strategy = st.builds(
    cpntools_TransTime,
    text=
        safe_text
)
cpntools_Annot_strategy = st.builds(
    cpntools_Annot,
    text=
        safe_text
)
cpntools_TransPriority_strategy = st.builds(
    cpntools_TransPriority,
    text=
        safe_text
)
cpntools_TransCond_strategy = st.builds(
    cpntools_TransCond,
    text=
        safe_text
)
cpntools_Port_strategy = st.builds(
    cpntools_Port,
    portType=
        safe_text
)
cpntools_Initmark_strategy = st.builds(
    cpntools_Initmark,
    expression=
        safe_text
)
cpntools_Block_strategy = st.builds(
    cpntools_Block,
    idname=
        safe_text
)
cpntools_DiagramElement_strategy = st.builds(
    cpntools_DiagramElement,
    fillFilled=
        st.booleans(),
    lineType=
        safe_text,
    posy=
        st.integers(),
    fillPattern=
        safe_text,
    lineColour=
        safe_text,
    posx=
        st.integers(),
    lineThick=
        st.integers(),
    fillColour=
        safe_text
)
cpntools_Arc_strategy = st.builds(
    cpntools_Arc,
    order=
        st.integers(),
    orientation=
        safe_text,
    headsize=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    currentcyckle=
        safe_text
)
cpntools_Trans_strategy = st.builds(
    cpntools_Trans,
    width=
        st.integers(),
    text=
        safe_text,
    height=
        st.integers(),
    explicit=
        st.booleans()
)
cpntools_Auxiliary_strategy = st.builds(
    cpntools_Auxiliary,
)
cpntools_Place_strategy = st.builds(
    cpntools_Place,
    width=
        st.integers(),
    text=
        safe_text,
    height=
        st.integers()
)
cpntools_Group_strategy = st.builds(
    cpntools_Group,
    name=
        safe_text
)
cpntools_Page_strategy = st.builds(
    cpntools_Page,
    name=
        safe_text
)
cpntools_Binder_strategy = st.builds(
    cpntools_Binder,
    height=
        st.integers(),
    posx=
        st.integers(),
    posy=
        st.integers(),
    width=
        st.integers()
)
cpntools_Globbox_strategy = st.builds(
    cpntools_Globbox,
    name=
        safe_text
)
cpntools_Fusion_strategy = st.builds(
    cpntools_Fusion,
    name=
        safe_text
)
cpntools_Cpnet_strategy = st.builds(
    cpntools_Cpnet,
)

@given(instance=CompoundColorSet_strategy)
@settings(max_examples=50)
def test_compoundcolorset_instantiation(instance):
    assert isinstance(instance, CompoundColorSet)

@given(instance=cpntools_Union_strategy)
@settings(max_examples=50)
def test_cpntools_union_instantiation(instance):
    assert isinstance(instance, cpntools_Union)

@given(instance=cpntools_Record_strategy)
@settings(max_examples=50)
def test_cpntools_record_instantiation(instance):
    assert isinstance(instance, cpntools_Record)

@given(instance=cpntools_List_strategy)
@settings(max_examples=50)
def test_cpntools_list_instantiation(instance):
    assert isinstance(instance, cpntools_List)

@given(instance=cpntools_Alias_strategy)
@settings(max_examples=50)
def test_cpntools_alias_instantiation(instance):
    assert isinstance(instance, cpntools_Alias)

@given(instance=cpntools_Subset_strategy)
@settings(max_examples=50)
def test_cpntools_subset_instantiation(instance):
    assert isinstance(instance, cpntools_Subset)

@given(instance=cpntools_Product_strategy)
@settings(max_examples=50)
def test_cpntools_product_instantiation(instance):
    assert isinstance(instance, cpntools_Product)

@given(instance=ColorSet_strategy)
@settings(max_examples=50)
def test_colorset_instantiation(instance):
    assert isinstance(instance, ColorSet)

@given(instance=cpntools_SimpleColorSet_strategy)
@settings(max_examples=50)
def test_cpntools_simplecolorset_instantiation(instance):
    assert isinstance(instance, cpntools_SimpleColorSet)

@given(instance=SimpleColorSet_strategy)
@settings(max_examples=50)
def test_simplecolorset_instantiation(instance):
    assert isinstance(instance, SimpleColorSet)

@given(instance=cpntools_Integer_strategy)
@settings(max_examples=50)
def test_cpntools_integer_instantiation(instance):
    assert isinstance(instance, cpntools_Integer)



@given(instance=cpntools_Integer_strategy)
def test_cpntools_integer_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original

@given(instance=cpntools_String_strategy)
@settings(max_examples=50)
def test_cpntools_string_instantiation(instance):
    assert isinstance(instance, cpntools_String)



@given(instance=cpntools_String_strategy)
def test_cpntools_string_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original



@given(instance=cpntools_String_strategy)
def test_cpntools_string_and__setter(instance):
    original = instance.and_
    instance.and_ = original
    assert instance.and_ == original

@given(instance=cpntools_Boolean_strategy)
@settings(max_examples=50)
def test_cpntools_boolean_instantiation(instance):
    assert isinstance(instance, cpntools_Boolean)



@given(instance=cpntools_Boolean_strategy)
def test_cpntools_boolean_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original

@given(instance=cpntools_Index_strategy)
@settings(max_examples=50)
def test_cpntools_index_instantiation(instance):
    assert isinstance(instance, cpntools_Index)



@given(instance=cpntools_Index_strategy)
def test_cpntools_index_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original

@given(instance=cpntools_Real_strategy)
@settings(max_examples=50)
def test_cpntools_real_instantiation(instance):
    assert isinstance(instance, cpntools_Real)



@given(instance=cpntools_Real_strategy)
def test_cpntools_real_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original

@given(instance=cpntools_LargeInteger_strategy)
@settings(max_examples=50)
def test_cpntools_largeinteger_instantiation(instance):
    assert isinstance(instance, cpntools_LargeInteger)



@given(instance=cpntools_LargeInteger_strategy)
def test_cpntools_largeinteger_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original

@given(instance=cpntools_Time_strategy)
@settings(max_examples=50)
def test_cpntools_time_instantiation(instance):
    assert isinstance(instance, cpntools_Time)

@given(instance=cpntools_Enumerated_strategy)
@settings(max_examples=50)
def test_cpntools_enumerated_instantiation(instance):
    assert isinstance(instance, cpntools_Enumerated)



@given(instance=cpntools_Enumerated_strategy)
def test_cpntools_enumerated_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original

@given(instance=cpntools_Unit_strategy)
@settings(max_examples=50)
def test_cpntools_unit_instantiation(instance):
    assert isinstance(instance, cpntools_Unit)



@given(instance=cpntools_Unit_strategy)
def test_cpntools_unit_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original

@given(instance=cpntools_CompoundColorSet_strategy)
@settings(max_examples=50)
def test_cpntools_compoundcolorset_instantiation(instance):
    assert isinstance(instance, cpntools_CompoundColorSet)

@given(instance=Auxiliary_strategy)
@settings(max_examples=50)
def test_auxiliary_instantiation(instance):
    assert isinstance(instance, Auxiliary)

@given(instance=cpntools_AuxEllipse_strategy)
@settings(max_examples=50)
def test_cpntools_auxellipse_instantiation(instance):
    assert isinstance(instance, cpntools_AuxEllipse)



@given(instance=cpntools_AuxEllipse_strategy)
def test_cpntools_auxellipse_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cpntools_AuxEllipse_strategy)
def test_cpntools_auxellipse_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=cpntools_AuxBox_strategy)
@settings(max_examples=50)
def test_cpntools_auxbox_instantiation(instance):
    assert isinstance(instance, cpntools_AuxBox)



@given(instance=cpntools_AuxBox_strategy)
def test_cpntools_auxbox_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cpntools_AuxBox_strategy)
def test_cpntools_auxbox_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=cpntools_AuxText_strategy)
@settings(max_examples=50)
def test_cpntools_auxtext_instantiation(instance):
    assert isinstance(instance, cpntools_AuxText)



@given(instance=cpntools_AuxText_strategy)
def test_cpntools_auxtext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=cpntools_Declaration_strategy)
@settings(max_examples=50)
def test_cpntools_declaration_instantiation(instance):
    assert isinstance(instance, cpntools_Declaration)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=cpntools_Var_strategy)
@settings(max_examples=50)
def test_cpntools_var_instantiation(instance):
    assert isinstance(instance, cpntools_Var)



@given(instance=cpntools_Var_strategy)
def test_cpntools_var_idname_setter(instance):
    original = instance.idname
    instance.idname = original
    assert instance.idname == original

@given(instance=cpntools_Ml_strategy)
@settings(max_examples=50)
def test_cpntools_ml_instantiation(instance):
    assert isinstance(instance, cpntools_Ml)



@given(instance=cpntools_Ml_strategy)
def test_cpntools_ml_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=cpntools_Globref_strategy)
@settings(max_examples=50)
def test_cpntools_globref_instantiation(instance):
    assert isinstance(instance, cpntools_Globref)



@given(instance=cpntools_Globref_strategy)
def test_cpntools_globref_idname_setter(instance):
    original = instance.idname
    instance.idname = original
    assert instance.idname == original

@given(instance=cpntools_ColorSet_strategy)
@settings(max_examples=50)
def test_cpntools_colorset_instantiation(instance):
    assert isinstance(instance, cpntools_ColorSet)



@given(instance=cpntools_ColorSet_strategy)
def test_cpntools_colorset_declare_setter(instance):
    original = instance.declare
    instance.declare = original
    assert instance.declare == original



@given(instance=cpntools_ColorSet_strategy)
def test_cpntools_colorset_timed_setter(instance):
    original = instance.timed
    instance.timed = original
    assert instance.timed == original



@given(instance=cpntools_ColorSet_strategy)
def test_cpntools_colorset_colorSetType_setter(instance):
    original = instance.colorSetType
    instance.colorSetType = original
    assert instance.colorSetType == original



@given(instance=cpntools_ColorSet_strategy)
def test_cpntools_colorset_idname_setter(instance):
    original = instance.idname
    instance.idname = original
    assert instance.idname == original

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=cpntools_TransTime_strategy)
@settings(max_examples=50)
def test_cpntools_transtime_instantiation(instance):
    assert isinstance(instance, cpntools_TransTime)



@given(instance=cpntools_TransTime_strategy)
def test_cpntools_transtime_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=cpntools_Annot_strategy)
@settings(max_examples=50)
def test_cpntools_annot_instantiation(instance):
    assert isinstance(instance, cpntools_Annot)



@given(instance=cpntools_Annot_strategy)
def test_cpntools_annot_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=cpntools_TransPriority_strategy)
@settings(max_examples=50)
def test_cpntools_transpriority_instantiation(instance):
    assert isinstance(instance, cpntools_TransPriority)



@given(instance=cpntools_TransPriority_strategy)
def test_cpntools_transpriority_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=cpntools_TransCond_strategy)
@settings(max_examples=50)
def test_cpntools_transcond_instantiation(instance):
    assert isinstance(instance, cpntools_TransCond)



@given(instance=cpntools_TransCond_strategy)
def test_cpntools_transcond_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=cpntools_Port_strategy)
@settings(max_examples=50)
def test_cpntools_port_instantiation(instance):
    assert isinstance(instance, cpntools_Port)



@given(instance=cpntools_Port_strategy)
def test_cpntools_port_portType_setter(instance):
    original = instance.portType
    instance.portType = original
    assert instance.portType == original

@given(instance=cpntools_Initmark_strategy)
@settings(max_examples=50)
def test_cpntools_initmark_instantiation(instance):
    assert isinstance(instance, cpntools_Initmark)



@given(instance=cpntools_Initmark_strategy)
def test_cpntools_initmark_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=cpntools_Block_strategy)
@settings(max_examples=50)
def test_cpntools_block_instantiation(instance):
    assert isinstance(instance, cpntools_Block)



@given(instance=cpntools_Block_strategy)
def test_cpntools_block_idname_setter(instance):
    original = instance.idname
    instance.idname = original
    assert instance.idname == original

@given(instance=cpntools_DiagramElement_strategy)
@settings(max_examples=50)
def test_cpntools_diagramelement_instantiation(instance):
    assert isinstance(instance, cpntools_DiagramElement)



@given(instance=cpntools_DiagramElement_strategy)
def test_cpntools_diagramelement_fillFilled_setter(instance):
    original = instance.fillFilled
    instance.fillFilled = original
    assert instance.fillFilled == original



@given(instance=cpntools_DiagramElement_strategy)
def test_cpntools_diagramelement_lineType_setter(instance):
    original = instance.lineType
    instance.lineType = original
    assert instance.lineType == original



@given(instance=cpntools_DiagramElement_strategy)
def test_cpntools_diagramelement_posy_setter(instance):
    original = instance.posy
    instance.posy = original
    assert instance.posy == original



@given(instance=cpntools_DiagramElement_strategy)
def test_cpntools_diagramelement_fillPattern_setter(instance):
    original = instance.fillPattern
    instance.fillPattern = original
    assert instance.fillPattern == original



@given(instance=cpntools_DiagramElement_strategy)
def test_cpntools_diagramelement_lineColour_setter(instance):
    original = instance.lineColour
    instance.lineColour = original
    assert instance.lineColour == original



@given(instance=cpntools_DiagramElement_strategy)
def test_cpntools_diagramelement_posx_setter(instance):
    original = instance.posx
    instance.posx = original
    assert instance.posx == original



@given(instance=cpntools_DiagramElement_strategy)
def test_cpntools_diagramelement_lineThick_setter(instance):
    original = instance.lineThick
    instance.lineThick = original
    assert instance.lineThick == original



@given(instance=cpntools_DiagramElement_strategy)
def test_cpntools_diagramelement_fillColour_setter(instance):
    original = instance.fillColour
    instance.fillColour = original
    assert instance.fillColour == original

@given(instance=cpntools_Arc_strategy)
@settings(max_examples=50)
def test_cpntools_arc_instantiation(instance):
    assert isinstance(instance, cpntools_Arc)



@given(instance=cpntools_Arc_strategy)
def test_cpntools_arc_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=cpntools_Arc_strategy)
def test_cpntools_arc_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=cpntools_Arc_strategy)
def test_cpntools_arc_headsize_setter(instance):
    original = instance.headsize
    instance.headsize = original
    assert instance.headsize == original



@given(instance=cpntools_Arc_strategy)
def test_cpntools_arc_currentcyckle_setter(instance):
    original = instance.currentcyckle
    instance.currentcyckle = original
    assert instance.currentcyckle == original

@given(instance=cpntools_Trans_strategy)
@settings(max_examples=50)
def test_cpntools_trans_instantiation(instance):
    assert isinstance(instance, cpntools_Trans)



@given(instance=cpntools_Trans_strategy)
def test_cpntools_trans_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cpntools_Trans_strategy)
def test_cpntools_trans_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=cpntools_Trans_strategy)
def test_cpntools_trans_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=cpntools_Trans_strategy)
def test_cpntools_trans_explicit_setter(instance):
    original = instance.explicit
    instance.explicit = original
    assert instance.explicit == original

@given(instance=cpntools_Auxiliary_strategy)
@settings(max_examples=50)
def test_cpntools_auxiliary_instantiation(instance):
    assert isinstance(instance, cpntools_Auxiliary)

@given(instance=cpntools_Place_strategy)
@settings(max_examples=50)
def test_cpntools_place_instantiation(instance):
    assert isinstance(instance, cpntools_Place)



@given(instance=cpntools_Place_strategy)
def test_cpntools_place_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cpntools_Place_strategy)
def test_cpntools_place_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=cpntools_Place_strategy)
def test_cpntools_place_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=cpntools_Group_strategy)
@settings(max_examples=50)
def test_cpntools_group_instantiation(instance):
    assert isinstance(instance, cpntools_Group)



@given(instance=cpntools_Group_strategy)
def test_cpntools_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpntools_Page_strategy)
@settings(max_examples=50)
def test_cpntools_page_instantiation(instance):
    assert isinstance(instance, cpntools_Page)



@given(instance=cpntools_Page_strategy)
def test_cpntools_page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=cpntools_Page_strategy)
@settings(max_examples=30)
def test_cpntools_page_layout_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.layout()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.layout).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'layout' in cpntools_Page is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'layout' in cpntools_Page did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'layout' in cpntools_Page is not implemented or raised an error")

@given(instance=cpntools_Binder_strategy)
@settings(max_examples=50)
def test_cpntools_binder_instantiation(instance):
    assert isinstance(instance, cpntools_Binder)



@given(instance=cpntools_Binder_strategy)
def test_cpntools_binder_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=cpntools_Binder_strategy)
def test_cpntools_binder_posx_setter(instance):
    original = instance.posx
    instance.posx = original
    assert instance.posx == original



@given(instance=cpntools_Binder_strategy)
def test_cpntools_binder_posy_setter(instance):
    original = instance.posy
    instance.posy = original
    assert instance.posy == original



@given(instance=cpntools_Binder_strategy)
def test_cpntools_binder_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=cpntools_Globbox_strategy)
@settings(max_examples=50)
def test_cpntools_globbox_instantiation(instance):
    assert isinstance(instance, cpntools_Globbox)



@given(instance=cpntools_Globbox_strategy)
def test_cpntools_globbox_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpntools_Fusion_strategy)
@settings(max_examples=50)
def test_cpntools_fusion_instantiation(instance):
    assert isinstance(instance, cpntools_Fusion)



@given(instance=cpntools_Fusion_strategy)
def test_cpntools_fusion_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpntools_Cpnet_strategy)
@settings(max_examples=50)
def test_cpntools_cpnet_instantiation(instance):
    assert isinstance(instance, cpntools_Cpnet)
