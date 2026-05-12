import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    vml_Category,
    ChartElement,
    vml_Point,
    vml_StackBars,
    vml_Bar,
    Chart,
    vml_Scatter,
    vml_StackBarChart,
    vml_LineChart,
    vml_BarChart,
    DiagramElement,
    vml_ChartElement,
    vml_Node,
    vml_Edge,
    vml_Slice,
    Diagram,
    vml_Chart,
    vml_Graph,
    vml_Pie,
    vml_DiagramElement,
    vml_Table,
    vml_Diagram,
    vml_Model,
    vml_Color,
    GraphStyle,
    vml_EdgeStyle,
    vml_NodeStyle,
    Style,
    vml_ChartWithoutAxisStyle,
    vml_ChartWithAxisStyle,
    vml_GraphStyle,
    vml_Style,
    vml_Cell,
    vml_Row,
    vml_Column,
    LineStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vml_category_is_not_abstract():
    assert not inspect.isabstract(vml_Category)


def test_vml_category_constructor_exists():
    assert callable(vml_Category.__init__)


def test_vml_category_constructor_args():
    sig = inspect.signature(vml_Category.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"

def test_vml_category_has_category():
    assert hasattr(vml_Category, "category")
    descriptor = None
    for klass in vml_Category.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_chartelement_is_not_abstract():
    assert not inspect.isabstract(ChartElement)


def test_chartelement_constructor_exists():
    assert callable(ChartElement.__init__)


def test_chartelement_constructor_args():
    sig = inspect.signature(ChartElement.__init__)
    params = list(sig.parameters.keys())



def test_vml_point_is_not_abstract():
    assert not inspect.isabstract(vml_Point)


def test_vml_point_constructor_exists():
    assert callable(vml_Point.__init__)


def test_vml_point_constructor_args():
    sig = inspect.signature(vml_Point.__init__)
    params = list(sig.parameters.keys())



def test_vml_stackbars_is_not_abstract():
    assert not inspect.isabstract(vml_StackBars)


def test_vml_stackbars_constructor_exists():
    assert callable(vml_StackBars.__init__)


def test_vml_stackbars_constructor_args():
    sig = inspect.signature(vml_StackBars.__init__)
    params = list(sig.parameters.keys())



def test_vml_bar_is_not_abstract():
    assert not inspect.isabstract(vml_Bar)


def test_vml_bar_constructor_exists():
    assert callable(vml_Bar.__init__)


def test_vml_bar_constructor_args():
    sig = inspect.signature(vml_Bar.__init__)
    params = list(sig.parameters.keys())



def test_chart_is_not_abstract():
    assert not inspect.isabstract(Chart)


def test_chart_constructor_exists():
    assert callable(Chart.__init__)


def test_chart_constructor_args():
    sig = inspect.signature(Chart.__init__)
    params = list(sig.parameters.keys())



def test_vml_scatter_is_not_abstract():
    assert not inspect.isabstract(vml_Scatter)


def test_vml_scatter_constructor_exists():
    assert callable(vml_Scatter.__init__)


def test_vml_scatter_constructor_args():
    sig = inspect.signature(vml_Scatter.__init__)
    params = list(sig.parameters.keys())



def test_vml_stackbarchart_is_not_abstract():
    assert not inspect.isabstract(vml_StackBarChart)


def test_vml_stackbarchart_constructor_exists():
    assert callable(vml_StackBarChart.__init__)


def test_vml_stackbarchart_constructor_args():
    sig = inspect.signature(vml_StackBarChart.__init__)
    params = list(sig.parameters.keys())



def test_vml_linechart_is_not_abstract():
    assert not inspect.isabstract(vml_LineChart)


def test_vml_linechart_constructor_exists():
    assert callable(vml_LineChart.__init__)


def test_vml_linechart_constructor_args():
    sig = inspect.signature(vml_LineChart.__init__)
    params = list(sig.parameters.keys())



def test_vml_barchart_is_not_abstract():
    assert not inspect.isabstract(vml_BarChart)


def test_vml_barchart_constructor_exists():
    assert callable(vml_BarChart.__init__)


def test_vml_barchart_constructor_args():
    sig = inspect.signature(vml_BarChart.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_vml_chartelement_is_not_abstract():
    assert not inspect.isabstract(vml_ChartElement)


def test_vml_chartelement_constructor_exists():
    assert callable(vml_ChartElement.__init__)


def test_vml_chartelement_constructor_args():
    sig = inspect.signature(vml_ChartElement.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "xValue" in params, "Missing parameter 'xValue'"
    assert "yValue" in params, "Missing parameter 'yValue'"

def test_vml_chartelement_has_ID():
    assert hasattr(vml_ChartElement, "ID")
    descriptor = None
    for klass in vml_ChartElement.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_vml_chartelement_has_xValue():
    assert hasattr(vml_ChartElement, "xValue")
    descriptor = None
    for klass in vml_ChartElement.__mro__:
        if "xValue" in klass.__dict__:
            descriptor = klass.__dict__["xValue"]
            break
    assert isinstance(descriptor, property)

def test_vml_chartelement_has_yValue():
    assert hasattr(vml_ChartElement, "yValue")
    descriptor = None
    for klass in vml_ChartElement.__mro__:
        if "yValue" in klass.__dict__:
            descriptor = klass.__dict__["yValue"]
            break
    assert isinstance(descriptor, property)



def test_vml_node_is_not_abstract():
    assert not inspect.isabstract(vml_Node)


def test_vml_node_constructor_exists():
    assert callable(vml_Node.__init__)


def test_vml_node_constructor_args():
    sig = inspect.signature(vml_Node.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "icone" in params, "Missing parameter 'icone'"

def test_vml_node_has_title():
    assert hasattr(vml_Node, "title")
    descriptor = None
    for klass in vml_Node.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_vml_node_has_icone():
    assert hasattr(vml_Node, "icone")
    descriptor = None
    for klass in vml_Node.__mro__:
        if "icone" in klass.__dict__:
            descriptor = klass.__dict__["icone"]
            break
    assert isinstance(descriptor, property)



def test_vml_edge_is_not_abstract():
    assert not inspect.isabstract(vml_Edge)


def test_vml_edge_constructor_exists():
    assert callable(vml_Edge.__init__)


def test_vml_edge_constructor_args():
    sig = inspect.signature(vml_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "relation" in params, "Missing parameter 'relation'"

def test_vml_edge_has_relation():
    assert hasattr(vml_Edge, "relation")
    descriptor = None
    for klass in vml_Edge.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_vml_slice_is_not_abstract():
    assert not inspect.isabstract(vml_Slice)


def test_vml_slice_constructor_exists():
    assert callable(vml_Slice.__init__)


def test_vml_slice_constructor_args():
    sig = inspect.signature(vml_Slice.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "title" in params, "Missing parameter 'title'"

def test_vml_slice_has_value():
    assert hasattr(vml_Slice, "value")
    descriptor = None
    for klass in vml_Slice.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vml_slice_has_title():
    assert hasattr(vml_Slice, "title")
    descriptor = None
    for klass in vml_Slice.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_vml_chart_is_not_abstract():
    assert not inspect.isabstract(vml_Chart)


def test_vml_chart_constructor_exists():
    assert callable(vml_Chart.__init__)


def test_vml_chart_constructor_args():
    sig = inspect.signature(vml_Chart.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "title" in params, "Missing parameter 'title'"
    assert "xTitle" in params, "Missing parameter 'xTitle'"
    assert "yTitle" in params, "Missing parameter 'yTitle'"

def test_vml_chart_has_ID():
    assert hasattr(vml_Chart, "ID")
    descriptor = None
    for klass in vml_Chart.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_vml_chart_has_title():
    assert hasattr(vml_Chart, "title")
    descriptor = None
    for klass in vml_Chart.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_vml_chart_has_xTitle():
    assert hasattr(vml_Chart, "xTitle")
    descriptor = None
    for klass in vml_Chart.__mro__:
        if "xTitle" in klass.__dict__:
            descriptor = klass.__dict__["xTitle"]
            break
    assert isinstance(descriptor, property)

def test_vml_chart_has_yTitle():
    assert hasattr(vml_Chart, "yTitle")
    descriptor = None
    for klass in vml_Chart.__mro__:
        if "yTitle" in klass.__dict__:
            descriptor = klass.__dict__["yTitle"]
            break
    assert isinstance(descriptor, property)



def test_vml_graph_is_not_abstract():
    assert not inspect.isabstract(vml_Graph)


def test_vml_graph_constructor_exists():
    assert callable(vml_Graph.__init__)


def test_vml_graph_constructor_args():
    sig = inspect.signature(vml_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_vml_graph_has_title():
    assert hasattr(vml_Graph, "title")
    descriptor = None
    for klass in vml_Graph.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_vml_graph_has_ID():
    assert hasattr(vml_Graph, "ID")
    descriptor = None
    for klass in vml_Graph.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_vml_pie_is_not_abstract():
    assert not inspect.isabstract(vml_Pie)


def test_vml_pie_constructor_exists():
    assert callable(vml_Pie.__init__)


def test_vml_pie_constructor_args():
    sig = inspect.signature(vml_Pie.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_vml_pie_has_title():
    assert hasattr(vml_Pie, "title")
    descriptor = None
    for klass in vml_Pie.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_vml_pie_has_identifier():
    assert hasattr(vml_Pie, "identifier")
    descriptor = None
    for klass in vml_Pie.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_vml_diagramelement_is_not_abstract():
    assert not inspect.isabstract(vml_DiagramElement)


def test_vml_diagramelement_constructor_exists():
    assert callable(vml_DiagramElement.__init__)


def test_vml_diagramelement_constructor_args():
    sig = inspect.signature(vml_DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_vml_table_is_not_abstract():
    assert not inspect.isabstract(vml_Table)


def test_vml_table_constructor_exists():
    assert callable(vml_Table.__init__)


def test_vml_table_constructor_args():
    sig = inspect.signature(vml_Table.__init__)
    params = list(sig.parameters.keys())
    assert "tableTitle" in params, "Missing parameter 'tableTitle'"

def test_vml_table_has_tableTitle():
    assert hasattr(vml_Table, "tableTitle")
    descriptor = None
    for klass in vml_Table.__mro__:
        if "tableTitle" in klass.__dict__:
            descriptor = klass.__dict__["tableTitle"]
            break
    assert isinstance(descriptor, property)



def test_vml_diagram_is_not_abstract():
    assert not inspect.isabstract(vml_Diagram)


def test_vml_diagram_constructor_exists():
    assert callable(vml_Diagram.__init__)


def test_vml_diagram_constructor_args():
    sig = inspect.signature(vml_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_vml_model_is_not_abstract():
    assert not inspect.isabstract(vml_Model)


def test_vml_model_constructor_exists():
    assert callable(vml_Model.__init__)


def test_vml_model_constructor_args():
    sig = inspect.signature(vml_Model.__init__)
    params = list(sig.parameters.keys())



def test_vml_color_is_not_abstract():
    assert not inspect.isabstract(vml_Color)


def test_vml_color_constructor_exists():
    assert callable(vml_Color.__init__)


def test_vml_color_constructor_args():
    sig = inspect.signature(vml_Color.__init__)
    params = list(sig.parameters.keys())
    assert "green" in params, "Missing parameter 'green'"
    assert "name" in params, "Missing parameter 'name'"
    assert "blue" in params, "Missing parameter 'blue'"
    assert "red" in params, "Missing parameter 'red'"

def test_vml_color_has_green():
    assert hasattr(vml_Color, "green")
    descriptor = None
    for klass in vml_Color.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_vml_color_has_name():
    assert hasattr(vml_Color, "name")
    descriptor = None
    for klass in vml_Color.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vml_color_has_blue():
    assert hasattr(vml_Color, "blue")
    descriptor = None
    for klass in vml_Color.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_vml_color_has_red():
    assert hasattr(vml_Color, "red")
    descriptor = None
    for klass in vml_Color.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)



def test_graphstyle_is_not_abstract():
    assert not inspect.isabstract(GraphStyle)


def test_graphstyle_constructor_exists():
    assert callable(GraphStyle.__init__)


def test_graphstyle_constructor_args():
    sig = inspect.signature(GraphStyle.__init__)
    params = list(sig.parameters.keys())



def test_vml_edgestyle_is_not_abstract():
    assert not inspect.isabstract(vml_EdgeStyle)


def test_vml_edgestyle_constructor_exists():
    assert callable(vml_EdgeStyle.__init__)


def test_vml_edgestyle_constructor_args():
    sig = inspect.signature(vml_EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "directed" in params, "Missing parameter 'directed'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"

def test_vml_edgestyle_has_directed():
    assert hasattr(vml_EdgeStyle, "directed")
    descriptor = None
    for klass in vml_EdgeStyle.__mro__:
        if "directed" in klass.__dict__:
            descriptor = klass.__dict__["directed"]
            break
    assert isinstance(descriptor, property)

def test_vml_edgestyle_has_weight():
    assert hasattr(vml_EdgeStyle, "weight")
    descriptor = None
    for klass in vml_EdgeStyle.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_vml_edgestyle_has_lineWidth():
    assert hasattr(vml_EdgeStyle, "lineWidth")
    descriptor = None
    for klass in vml_EdgeStyle.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_vml_edgestyle_has_lineStyle():
    assert hasattr(vml_EdgeStyle, "lineStyle")
    descriptor = None
    for klass in vml_EdgeStyle.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)



def test_vml_nodestyle_is_not_abstract():
    assert not inspect.isabstract(vml_NodeStyle)


def test_vml_nodestyle_constructor_exists():
    assert callable(vml_NodeStyle.__init__)


def test_vml_nodestyle_constructor_args():
    sig = inspect.signature(vml_NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "padding" in params, "Missing parameter 'padding'"
    assert "borderWidth" in params, "Missing parameter 'borderWidth'"

def test_vml_nodestyle_has_padding():
    assert hasattr(vml_NodeStyle, "padding")
    descriptor = None
    for klass in vml_NodeStyle.__mro__:
        if "padding" in klass.__dict__:
            descriptor = klass.__dict__["padding"]
            break
    assert isinstance(descriptor, property)

def test_vml_nodestyle_has_borderWidth():
    assert hasattr(vml_NodeStyle, "borderWidth")
    descriptor = None
    for klass in vml_NodeStyle.__mro__:
        if "borderWidth" in klass.__dict__:
            descriptor = klass.__dict__["borderWidth"]
            break
    assert isinstance(descriptor, property)



def test_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_style_constructor_exists():
    assert callable(Style.__init__)


def test_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_vml_chartwithoutaxisstyle_is_not_abstract():
    assert not inspect.isabstract(vml_ChartWithoutAxisStyle)


def test_vml_chartwithoutaxisstyle_constructor_exists():
    assert callable(vml_ChartWithoutAxisStyle.__init__)


def test_vml_chartwithoutaxisstyle_constructor_args():
    sig = inspect.signature(vml_ChartWithoutAxisStyle.__init__)
    params = list(sig.parameters.keys())



def test_vml_chartwithaxisstyle_is_not_abstract():
    assert not inspect.isabstract(vml_ChartWithAxisStyle)


def test_vml_chartwithaxisstyle_constructor_exists():
    assert callable(vml_ChartWithAxisStyle.__init__)


def test_vml_chartwithaxisstyle_constructor_args():
    sig = inspect.signature(vml_ChartWithAxisStyle.__init__)
    params = list(sig.parameters.keys())



def test_vml_graphstyle_is_not_abstract():
    assert not inspect.isabstract(vml_GraphStyle)


def test_vml_graphstyle_constructor_exists():
    assert callable(vml_GraphStyle.__init__)


def test_vml_graphstyle_constructor_args():
    sig = inspect.signature(vml_GraphStyle.__init__)
    params = list(sig.parameters.keys())



def test_vml_style_is_not_abstract():
    assert not inspect.isabstract(vml_Style)


def test_vml_style_constructor_exists():
    assert callable(vml_Style.__init__)


def test_vml_style_constructor_args():
    sig = inspect.signature(vml_Style.__init__)
    params = list(sig.parameters.keys())



def test_vml_cell_is_not_abstract():
    assert not inspect.isabstract(vml_Cell)


def test_vml_cell_constructor_exists():
    assert callable(vml_Cell.__init__)


def test_vml_cell_constructor_args():
    sig = inspect.signature(vml_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "textValue" in params, "Missing parameter 'textValue'"

def test_vml_cell_has_textValue():
    assert hasattr(vml_Cell, "textValue")
    descriptor = None
    for klass in vml_Cell.__mro__:
        if "textValue" in klass.__dict__:
            descriptor = klass.__dict__["textValue"]
            break
    assert isinstance(descriptor, property)



def test_vml_row_is_not_abstract():
    assert not inspect.isabstract(vml_Row)


def test_vml_row_constructor_exists():
    assert callable(vml_Row.__init__)


def test_vml_row_constructor_args():
    sig = inspect.signature(vml_Row.__init__)
    params = list(sig.parameters.keys())



def test_vml_column_is_not_abstract():
    assert not inspect.isabstract(vml_Column)


def test_vml_column_constructor_exists():
    assert callable(vml_Column.__init__)


def test_vml_column_constructor_args():
    sig = inspect.signature(vml_Column.__init__)
    params = list(sig.parameters.keys())
    assert "columnTitle" in params, "Missing parameter 'columnTitle'"

def test_vml_column_has_columnTitle():
    assert hasattr(vml_Column, "columnTitle")
    descriptor = None
    for klass in vml_Column.__mro__:
        if "columnTitle" in klass.__dict__:
            descriptor = klass.__dict__["columnTitle"]
            break
    assert isinstance(descriptor, property)

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "Dot",
        "Dash",
        "Solid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"


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
vml_Category_strategy = st.builds(
    vml_Category,
    category=
        safe_text
)
ChartElement_strategy = st.builds(
    ChartElement,
)
vml_Point_strategy = st.builds(
    vml_Point,
)
vml_StackBars_strategy = st.builds(
    vml_StackBars,
)
vml_Bar_strategy = st.builds(
    vml_Bar,
)
Chart_strategy = st.builds(
    Chart,
)
vml_Scatter_strategy = st.builds(
    vml_Scatter,
)
vml_StackBarChart_strategy = st.builds(
    vml_StackBarChart,
)
vml_LineChart_strategy = st.builds(
    vml_LineChart,
)
vml_BarChart_strategy = st.builds(
    vml_BarChart,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
vml_ChartElement_strategy = st.builds(
    vml_ChartElement,
    ID=
        safe_text,
    xValue=
        safe_text,
    yValue=
        safe_text
)
vml_Node_strategy = st.builds(
    vml_Node,
    title=
        safe_text,
    icone=
        safe_text
)
vml_Edge_strategy = st.builds(
    vml_Edge,
    relation=
        safe_text
)
vml_Slice_strategy = st.builds(
    vml_Slice,
    value=
        st.integers(),
    title=
        safe_text
)
Diagram_strategy = st.builds(
    Diagram,
)
vml_Chart_strategy = st.builds(
    vml_Chart,
    ID=
        safe_text,
    title=
        safe_text,
    xTitle=
        safe_text,
    yTitle=
        safe_text
)
vml_Graph_strategy = st.builds(
    vml_Graph,
    title=
        safe_text,
    ID=
        safe_text
)
vml_Pie_strategy = st.builds(
    vml_Pie,
    title=
        safe_text,
    identifier=
        safe_text
)
vml_DiagramElement_strategy = st.builds(
    vml_DiagramElement,
)
vml_Table_strategy = st.builds(
    vml_Table,
    tableTitle=
        safe_text
)
vml_Diagram_strategy = st.builds(
    vml_Diagram,
)
vml_Model_strategy = st.builds(
    vml_Model,
)
vml_Color_strategy = st.builds(
    vml_Color,
    green=
        st.integers(),
    name=
        safe_text,
    blue=
        st.integers(),
    red=
        st.integers()
)
GraphStyle_strategy = st.builds(
    GraphStyle,
)
vml_EdgeStyle_strategy = st.builds(
    vml_EdgeStyle,
    directed=
        st.booleans(),
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineWidth=
        st.integers(),
    lineStyle=
        safe_text
)
vml_NodeStyle_strategy = st.builds(
    vml_NodeStyle,
    padding=
        st.integers(),
    borderWidth=
        st.integers()
)
Style_strategy = st.builds(
    Style,
)
vml_ChartWithoutAxisStyle_strategy = st.builds(
    vml_ChartWithoutAxisStyle,
)
vml_ChartWithAxisStyle_strategy = st.builds(
    vml_ChartWithAxisStyle,
)
vml_GraphStyle_strategy = st.builds(
    vml_GraphStyle,
)
vml_Style_strategy = st.builds(
    vml_Style,
)
vml_Cell_strategy = st.builds(
    vml_Cell,
    textValue=
        safe_text
)
vml_Row_strategy = st.builds(
    vml_Row,
)
vml_Column_strategy = st.builds(
    vml_Column,
    columnTitle=
        safe_text
)

@given(instance=vml_Category_strategy)
@settings(max_examples=50)
def test_vml_category_instantiation(instance):
    assert isinstance(instance, vml_Category)



@given(instance=vml_Category_strategy)
def test_vml_category_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=ChartElement_strategy)
@settings(max_examples=50)
def test_chartelement_instantiation(instance):
    assert isinstance(instance, ChartElement)

@given(instance=vml_Point_strategy)
@settings(max_examples=50)
def test_vml_point_instantiation(instance):
    assert isinstance(instance, vml_Point)

@given(instance=vml_StackBars_strategy)
@settings(max_examples=50)
def test_vml_stackbars_instantiation(instance):
    assert isinstance(instance, vml_StackBars)

@given(instance=vml_Bar_strategy)
@settings(max_examples=50)
def test_vml_bar_instantiation(instance):
    assert isinstance(instance, vml_Bar)

@given(instance=Chart_strategy)
@settings(max_examples=50)
def test_chart_instantiation(instance):
    assert isinstance(instance, Chart)

@given(instance=vml_Scatter_strategy)
@settings(max_examples=50)
def test_vml_scatter_instantiation(instance):
    assert isinstance(instance, vml_Scatter)

@given(instance=vml_StackBarChart_strategy)
@settings(max_examples=50)
def test_vml_stackbarchart_instantiation(instance):
    assert isinstance(instance, vml_StackBarChart)

@given(instance=vml_LineChart_strategy)
@settings(max_examples=50)
def test_vml_linechart_instantiation(instance):
    assert isinstance(instance, vml_LineChart)

@given(instance=vml_BarChart_strategy)
@settings(max_examples=50)
def test_vml_barchart_instantiation(instance):
    assert isinstance(instance, vml_BarChart)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=vml_ChartElement_strategy)
@settings(max_examples=50)
def test_vml_chartelement_instantiation(instance):
    assert isinstance(instance, vml_ChartElement)



@given(instance=vml_ChartElement_strategy)
def test_vml_chartelement_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=vml_ChartElement_strategy)
def test_vml_chartelement_xValue_setter(instance):
    original = instance.xValue
    instance.xValue = original
    assert instance.xValue == original



@given(instance=vml_ChartElement_strategy)
def test_vml_chartelement_yValue_setter(instance):
    original = instance.yValue
    instance.yValue = original
    assert instance.yValue == original

@given(instance=vml_Node_strategy)
@settings(max_examples=50)
def test_vml_node_instantiation(instance):
    assert isinstance(instance, vml_Node)



@given(instance=vml_Node_strategy)
def test_vml_node_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=vml_Node_strategy)
def test_vml_node_icone_setter(instance):
    original = instance.icone
    instance.icone = original
    assert instance.icone == original

@given(instance=vml_Edge_strategy)
@settings(max_examples=50)
def test_vml_edge_instantiation(instance):
    assert isinstance(instance, vml_Edge)



@given(instance=vml_Edge_strategy)
def test_vml_edge_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=vml_Slice_strategy)
@settings(max_examples=50)
def test_vml_slice_instantiation(instance):
    assert isinstance(instance, vml_Slice)



@given(instance=vml_Slice_strategy)
def test_vml_slice_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=vml_Slice_strategy)
def test_vml_slice_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=vml_Chart_strategy)
@settings(max_examples=50)
def test_vml_chart_instantiation(instance):
    assert isinstance(instance, vml_Chart)



@given(instance=vml_Chart_strategy)
def test_vml_chart_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=vml_Chart_strategy)
def test_vml_chart_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=vml_Chart_strategy)
def test_vml_chart_xTitle_setter(instance):
    original = instance.xTitle
    instance.xTitle = original
    assert instance.xTitle == original



@given(instance=vml_Chart_strategy)
def test_vml_chart_yTitle_setter(instance):
    original = instance.yTitle
    instance.yTitle = original
    assert instance.yTitle == original

@given(instance=vml_Graph_strategy)
@settings(max_examples=50)
def test_vml_graph_instantiation(instance):
    assert isinstance(instance, vml_Graph)



@given(instance=vml_Graph_strategy)
def test_vml_graph_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=vml_Graph_strategy)
def test_vml_graph_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=vml_Pie_strategy)
@settings(max_examples=50)
def test_vml_pie_instantiation(instance):
    assert isinstance(instance, vml_Pie)



@given(instance=vml_Pie_strategy)
def test_vml_pie_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=vml_Pie_strategy)
def test_vml_pie_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=vml_DiagramElement_strategy)
@settings(max_examples=50)
def test_vml_diagramelement_instantiation(instance):
    assert isinstance(instance, vml_DiagramElement)

@given(instance=vml_Table_strategy)
@settings(max_examples=50)
def test_vml_table_instantiation(instance):
    assert isinstance(instance, vml_Table)



@given(instance=vml_Table_strategy)
def test_vml_table_tableTitle_setter(instance):
    original = instance.tableTitle
    instance.tableTitle = original
    assert instance.tableTitle == original

@given(instance=vml_Diagram_strategy)
@settings(max_examples=50)
def test_vml_diagram_instantiation(instance):
    assert isinstance(instance, vml_Diagram)

@given(instance=vml_Model_strategy)
@settings(max_examples=50)
def test_vml_model_instantiation(instance):
    assert isinstance(instance, vml_Model)

@given(instance=vml_Color_strategy)
@settings(max_examples=50)
def test_vml_color_instantiation(instance):
    assert isinstance(instance, vml_Color)



@given(instance=vml_Color_strategy)
def test_vml_color_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=vml_Color_strategy)
def test_vml_color_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=vml_Color_strategy)
def test_vml_color_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original



@given(instance=vml_Color_strategy)
def test_vml_color_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=GraphStyle_strategy)
@settings(max_examples=50)
def test_graphstyle_instantiation(instance):
    assert isinstance(instance, GraphStyle)

@given(instance=vml_EdgeStyle_strategy)
@settings(max_examples=50)
def test_vml_edgestyle_instantiation(instance):
    assert isinstance(instance, vml_EdgeStyle)



@given(instance=vml_EdgeStyle_strategy)
def test_vml_edgestyle_directed_setter(instance):
    original = instance.directed
    instance.directed = original
    assert instance.directed == original



@given(instance=vml_EdgeStyle_strategy)
def test_vml_edgestyle_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=vml_EdgeStyle_strategy)
def test_vml_edgestyle_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original



@given(instance=vml_EdgeStyle_strategy)
def test_vml_edgestyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=vml_NodeStyle_strategy)
@settings(max_examples=50)
def test_vml_nodestyle_instantiation(instance):
    assert isinstance(instance, vml_NodeStyle)



@given(instance=vml_NodeStyle_strategy)
def test_vml_nodestyle_padding_setter(instance):
    original = instance.padding
    instance.padding = original
    assert instance.padding == original



@given(instance=vml_NodeStyle_strategy)
def test_vml_nodestyle_borderWidth_setter(instance):
    original = instance.borderWidth
    instance.borderWidth = original
    assert instance.borderWidth == original

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=vml_ChartWithoutAxisStyle_strategy)
@settings(max_examples=50)
def test_vml_chartwithoutaxisstyle_instantiation(instance):
    assert isinstance(instance, vml_ChartWithoutAxisStyle)

@given(instance=vml_ChartWithAxisStyle_strategy)
@settings(max_examples=50)
def test_vml_chartwithaxisstyle_instantiation(instance):
    assert isinstance(instance, vml_ChartWithAxisStyle)

@given(instance=vml_GraphStyle_strategy)
@settings(max_examples=50)
def test_vml_graphstyle_instantiation(instance):
    assert isinstance(instance, vml_GraphStyle)

@given(instance=vml_Style_strategy)
@settings(max_examples=50)
def test_vml_style_instantiation(instance):
    assert isinstance(instance, vml_Style)

@given(instance=vml_Cell_strategy)
@settings(max_examples=50)
def test_vml_cell_instantiation(instance):
    assert isinstance(instance, vml_Cell)



@given(instance=vml_Cell_strategy)
def test_vml_cell_textValue_setter(instance):
    original = instance.textValue
    instance.textValue = original
    assert instance.textValue == original

@given(instance=vml_Row_strategy)
@settings(max_examples=50)
def test_vml_row_instantiation(instance):
    assert isinstance(instance, vml_Row)

@given(instance=vml_Column_strategy)
@settings(max_examples=50)
def test_vml_column_instantiation(instance):
    assert isinstance(instance, vml_Column)



@given(instance=vml_Column_strategy)
def test_vml_column_columnTitle_setter(instance):
    original = instance.columnTitle
    instance.columnTitle = original
    assert instance.columnTitle == original
