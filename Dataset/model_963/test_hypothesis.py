import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    vml::Category,
    ChartElement,
    vml::Point,
    vml::StackBars,
    vml::Bar,
    Chart,
    vml::Scatter,
    vml::StackBarChart,
    vml::LineChart,
    vml::BarChart,
    DiagramElement,
    vml::Edge,
    vml::Node,
    vml::ChartElement,
    vml::Slice,
    Diagram,
    vml::Chart,
    vml::Graph,
    vml::Pie,
    vml::DiagramElement,
    vml::Table,
    vml::Diagram,
    vml::Model,
    vml::Color,
    GraphStyle,
    vml::EdgeStyle,
    vml::NodeStyle,
    Style,
    vml::ChartWithAxisStyle,
    vml::ChartWithoutAxisStyle,
    vml::GraphStyle,
    vml::Style,
    vml::Cell,
    vml::Row,
    vml::Column,
    LineStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vml::category_is_not_abstract():
    assert not inspect.isabstract(vml::Category)


def test_vml::category_constructor_exists():
    assert callable(vml::Category.__init__)


def test_vml::category_constructor_args():
    sig = inspect.signature(vml::Category.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"

def test_vml::category_has_category():
    assert hasattr(vml::Category, "category")
    descriptor = None
    for klass in vml::Category.__mro__:
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



def test_vml::point_is_not_abstract():
    assert not inspect.isabstract(vml::Point)


def test_vml::point_constructor_exists():
    assert callable(vml::Point.__init__)


def test_vml::point_constructor_args():
    sig = inspect.signature(vml::Point.__init__)
    params = list(sig.parameters.keys())



def test_vml::stackbars_is_not_abstract():
    assert not inspect.isabstract(vml::StackBars)


def test_vml::stackbars_constructor_exists():
    assert callable(vml::StackBars.__init__)


def test_vml::stackbars_constructor_args():
    sig = inspect.signature(vml::StackBars.__init__)
    params = list(sig.parameters.keys())



def test_vml::bar_is_not_abstract():
    assert not inspect.isabstract(vml::Bar)


def test_vml::bar_constructor_exists():
    assert callable(vml::Bar.__init__)


def test_vml::bar_constructor_args():
    sig = inspect.signature(vml::Bar.__init__)
    params = list(sig.parameters.keys())



def test_chart_is_not_abstract():
    assert not inspect.isabstract(Chart)


def test_chart_constructor_exists():
    assert callable(Chart.__init__)


def test_chart_constructor_args():
    sig = inspect.signature(Chart.__init__)
    params = list(sig.parameters.keys())



def test_vml::scatter_is_not_abstract():
    assert not inspect.isabstract(vml::Scatter)


def test_vml::scatter_constructor_exists():
    assert callable(vml::Scatter.__init__)


def test_vml::scatter_constructor_args():
    sig = inspect.signature(vml::Scatter.__init__)
    params = list(sig.parameters.keys())



def test_vml::stackbarchart_is_not_abstract():
    assert not inspect.isabstract(vml::StackBarChart)


def test_vml::stackbarchart_constructor_exists():
    assert callable(vml::StackBarChart.__init__)


def test_vml::stackbarchart_constructor_args():
    sig = inspect.signature(vml::StackBarChart.__init__)
    params = list(sig.parameters.keys())



def test_vml::linechart_is_not_abstract():
    assert not inspect.isabstract(vml::LineChart)


def test_vml::linechart_constructor_exists():
    assert callable(vml::LineChart.__init__)


def test_vml::linechart_constructor_args():
    sig = inspect.signature(vml::LineChart.__init__)
    params = list(sig.parameters.keys())



def test_vml::barchart_is_not_abstract():
    assert not inspect.isabstract(vml::BarChart)


def test_vml::barchart_constructor_exists():
    assert callable(vml::BarChart.__init__)


def test_vml::barchart_constructor_args():
    sig = inspect.signature(vml::BarChart.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_vml::edge_is_not_abstract():
    assert not inspect.isabstract(vml::Edge)


def test_vml::edge_constructor_exists():
    assert callable(vml::Edge.__init__)


def test_vml::edge_constructor_args():
    sig = inspect.signature(vml::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "relation" in params, "Missing parameter 'relation'"

def test_vml::edge_has_relation():
    assert hasattr(vml::Edge, "relation")
    descriptor = None
    for klass in vml::Edge.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_vml::node_is_not_abstract():
    assert not inspect.isabstract(vml::Node)


def test_vml::node_constructor_exists():
    assert callable(vml::Node.__init__)


def test_vml::node_constructor_args():
    sig = inspect.signature(vml::Node.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "icone" in params, "Missing parameter 'icone'"

def test_vml::node_has_title():
    assert hasattr(vml::Node, "title")
    descriptor = None
    for klass in vml::Node.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_vml::node_has_icone():
    assert hasattr(vml::Node, "icone")
    descriptor = None
    for klass in vml::Node.__mro__:
        if "icone" in klass.__dict__:
            descriptor = klass.__dict__["icone"]
            break
    assert isinstance(descriptor, property)



def test_vml::chartelement_is_not_abstract():
    assert not inspect.isabstract(vml::ChartElement)


def test_vml::chartelement_constructor_exists():
    assert callable(vml::ChartElement.__init__)


def test_vml::chartelement_constructor_args():
    sig = inspect.signature(vml::ChartElement.__init__)
    params = list(sig.parameters.keys())
    assert "yValue" in params, "Missing parameter 'yValue'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "xValue" in params, "Missing parameter 'xValue'"

def test_vml::chartelement_has_yValue():
    assert hasattr(vml::ChartElement, "yValue")
    descriptor = None
    for klass in vml::ChartElement.__mro__:
        if "yValue" in klass.__dict__:
            descriptor = klass.__dict__["yValue"]
            break
    assert isinstance(descriptor, property)

def test_vml::chartelement_has_ID():
    assert hasattr(vml::ChartElement, "ID")
    descriptor = None
    for klass in vml::ChartElement.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_vml::chartelement_has_xValue():
    assert hasattr(vml::ChartElement, "xValue")
    descriptor = None
    for klass in vml::ChartElement.__mro__:
        if "xValue" in klass.__dict__:
            descriptor = klass.__dict__["xValue"]
            break
    assert isinstance(descriptor, property)



def test_vml::slice_is_not_abstract():
    assert not inspect.isabstract(vml::Slice)


def test_vml::slice_constructor_exists():
    assert callable(vml::Slice.__init__)


def test_vml::slice_constructor_args():
    sig = inspect.signature(vml::Slice.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "title" in params, "Missing parameter 'title'"

def test_vml::slice_has_value():
    assert hasattr(vml::Slice, "value")
    descriptor = None
    for klass in vml::Slice.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vml::slice_has_title():
    assert hasattr(vml::Slice, "title")
    descriptor = None
    for klass in vml::Slice.__mro__:
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



def test_vml::chart_is_not_abstract():
    assert not inspect.isabstract(vml::Chart)


def test_vml::chart_constructor_exists():
    assert callable(vml::Chart.__init__)


def test_vml::chart_constructor_args():
    sig = inspect.signature(vml::Chart.__init__)
    params = list(sig.parameters.keys())
    assert "xTitle" in params, "Missing parameter 'xTitle'"
    assert "yTitle" in params, "Missing parameter 'yTitle'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "title" in params, "Missing parameter 'title'"

def test_vml::chart_has_xTitle():
    assert hasattr(vml::Chart, "xTitle")
    descriptor = None
    for klass in vml::Chart.__mro__:
        if "xTitle" in klass.__dict__:
            descriptor = klass.__dict__["xTitle"]
            break
    assert isinstance(descriptor, property)

def test_vml::chart_has_yTitle():
    assert hasattr(vml::Chart, "yTitle")
    descriptor = None
    for klass in vml::Chart.__mro__:
        if "yTitle" in klass.__dict__:
            descriptor = klass.__dict__["yTitle"]
            break
    assert isinstance(descriptor, property)

def test_vml::chart_has_ID():
    assert hasattr(vml::Chart, "ID")
    descriptor = None
    for klass in vml::Chart.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_vml::chart_has_title():
    assert hasattr(vml::Chart, "title")
    descriptor = None
    for klass in vml::Chart.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_vml::graph_is_not_abstract():
    assert not inspect.isabstract(vml::Graph)


def test_vml::graph_constructor_exists():
    assert callable(vml::Graph.__init__)


def test_vml::graph_constructor_args():
    sig = inspect.signature(vml::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_vml::graph_has_title():
    assert hasattr(vml::Graph, "title")
    descriptor = None
    for klass in vml::Graph.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_vml::graph_has_ID():
    assert hasattr(vml::Graph, "ID")
    descriptor = None
    for klass in vml::Graph.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_vml::pie_is_not_abstract():
    assert not inspect.isabstract(vml::Pie)


def test_vml::pie_constructor_exists():
    assert callable(vml::Pie.__init__)


def test_vml::pie_constructor_args():
    sig = inspect.signature(vml::Pie.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "title" in params, "Missing parameter 'title'"

def test_vml::pie_has_identifier():
    assert hasattr(vml::Pie, "identifier")
    descriptor = None
    for klass in vml::Pie.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_vml::pie_has_title():
    assert hasattr(vml::Pie, "title")
    descriptor = None
    for klass in vml::Pie.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_vml::diagramelement_is_not_abstract():
    assert not inspect.isabstract(vml::DiagramElement)


def test_vml::diagramelement_constructor_exists():
    assert callable(vml::DiagramElement.__init__)


def test_vml::diagramelement_constructor_args():
    sig = inspect.signature(vml::DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_vml::table_is_not_abstract():
    assert not inspect.isabstract(vml::Table)


def test_vml::table_constructor_exists():
    assert callable(vml::Table.__init__)


def test_vml::table_constructor_args():
    sig = inspect.signature(vml::Table.__init__)
    params = list(sig.parameters.keys())
    assert "tableTitle" in params, "Missing parameter 'tableTitle'"

def test_vml::table_has_tableTitle():
    assert hasattr(vml::Table, "tableTitle")
    descriptor = None
    for klass in vml::Table.__mro__:
        if "tableTitle" in klass.__dict__:
            descriptor = klass.__dict__["tableTitle"]
            break
    assert isinstance(descriptor, property)



def test_vml::diagram_is_not_abstract():
    assert not inspect.isabstract(vml::Diagram)


def test_vml::diagram_constructor_exists():
    assert callable(vml::Diagram.__init__)


def test_vml::diagram_constructor_args():
    sig = inspect.signature(vml::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_vml::model_is_not_abstract():
    assert not inspect.isabstract(vml::Model)


def test_vml::model_constructor_exists():
    assert callable(vml::Model.__init__)


def test_vml::model_constructor_args():
    sig = inspect.signature(vml::Model.__init__)
    params = list(sig.parameters.keys())



def test_vml::color_is_not_abstract():
    assert not inspect.isabstract(vml::Color)


def test_vml::color_constructor_exists():
    assert callable(vml::Color.__init__)


def test_vml::color_constructor_args():
    sig = inspect.signature(vml::Color.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"
    assert "name" in params, "Missing parameter 'name'"
    assert "blue" in params, "Missing parameter 'blue'"

def test_vml::color_has_red():
    assert hasattr(vml::Color, "red")
    descriptor = None
    for klass in vml::Color.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_vml::color_has_green():
    assert hasattr(vml::Color, "green")
    descriptor = None
    for klass in vml::Color.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_vml::color_has_name():
    assert hasattr(vml::Color, "name")
    descriptor = None
    for klass in vml::Color.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vml::color_has_blue():
    assert hasattr(vml::Color, "blue")
    descriptor = None
    for klass in vml::Color.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)



def test_graphstyle_is_not_abstract():
    assert not inspect.isabstract(GraphStyle)


def test_graphstyle_constructor_exists():
    assert callable(GraphStyle.__init__)


def test_graphstyle_constructor_args():
    sig = inspect.signature(GraphStyle.__init__)
    params = list(sig.parameters.keys())



def test_vml::edgestyle_is_not_abstract():
    assert not inspect.isabstract(vml::EdgeStyle)


def test_vml::edgestyle_constructor_exists():
    assert callable(vml::EdgeStyle.__init__)


def test_vml::edgestyle_constructor_args():
    sig = inspect.signature(vml::EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "directed" in params, "Missing parameter 'directed'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"

def test_vml::edgestyle_has_directed():
    assert hasattr(vml::EdgeStyle, "directed")
    descriptor = None
    for klass in vml::EdgeStyle.__mro__:
        if "directed" in klass.__dict__:
            descriptor = klass.__dict__["directed"]
            break
    assert isinstance(descriptor, property)

def test_vml::edgestyle_has_lineStyle():
    assert hasattr(vml::EdgeStyle, "lineStyle")
    descriptor = None
    for klass in vml::EdgeStyle.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_vml::edgestyle_has_weight():
    assert hasattr(vml::EdgeStyle, "weight")
    descriptor = None
    for klass in vml::EdgeStyle.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_vml::edgestyle_has_lineWidth():
    assert hasattr(vml::EdgeStyle, "lineWidth")
    descriptor = None
    for klass in vml::EdgeStyle.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)



def test_vml::nodestyle_is_not_abstract():
    assert not inspect.isabstract(vml::NodeStyle)


def test_vml::nodestyle_constructor_exists():
    assert callable(vml::NodeStyle.__init__)


def test_vml::nodestyle_constructor_args():
    sig = inspect.signature(vml::NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "padding" in params, "Missing parameter 'padding'"
    assert "borderWidth" in params, "Missing parameter 'borderWidth'"

def test_vml::nodestyle_has_padding():
    assert hasattr(vml::NodeStyle, "padding")
    descriptor = None
    for klass in vml::NodeStyle.__mro__:
        if "padding" in klass.__dict__:
            descriptor = klass.__dict__["padding"]
            break
    assert isinstance(descriptor, property)

def test_vml::nodestyle_has_borderWidth():
    assert hasattr(vml::NodeStyle, "borderWidth")
    descriptor = None
    for klass in vml::NodeStyle.__mro__:
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



def test_vml::chartwithaxisstyle_is_not_abstract():
    assert not inspect.isabstract(vml::ChartWithAxisStyle)


def test_vml::chartwithaxisstyle_constructor_exists():
    assert callable(vml::ChartWithAxisStyle.__init__)


def test_vml::chartwithaxisstyle_constructor_args():
    sig = inspect.signature(vml::ChartWithAxisStyle.__init__)
    params = list(sig.parameters.keys())



def test_vml::chartwithoutaxisstyle_is_not_abstract():
    assert not inspect.isabstract(vml::ChartWithoutAxisStyle)


def test_vml::chartwithoutaxisstyle_constructor_exists():
    assert callable(vml::ChartWithoutAxisStyle.__init__)


def test_vml::chartwithoutaxisstyle_constructor_args():
    sig = inspect.signature(vml::ChartWithoutAxisStyle.__init__)
    params = list(sig.parameters.keys())



def test_vml::graphstyle_is_not_abstract():
    assert not inspect.isabstract(vml::GraphStyle)


def test_vml::graphstyle_constructor_exists():
    assert callable(vml::GraphStyle.__init__)


def test_vml::graphstyle_constructor_args():
    sig = inspect.signature(vml::GraphStyle.__init__)
    params = list(sig.parameters.keys())



def test_vml::style_is_not_abstract():
    assert not inspect.isabstract(vml::Style)


def test_vml::style_constructor_exists():
    assert callable(vml::Style.__init__)


def test_vml::style_constructor_args():
    sig = inspect.signature(vml::Style.__init__)
    params = list(sig.parameters.keys())



def test_vml::cell_is_not_abstract():
    assert not inspect.isabstract(vml::Cell)


def test_vml::cell_constructor_exists():
    assert callable(vml::Cell.__init__)


def test_vml::cell_constructor_args():
    sig = inspect.signature(vml::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "textValue" in params, "Missing parameter 'textValue'"

def test_vml::cell_has_textValue():
    assert hasattr(vml::Cell, "textValue")
    descriptor = None
    for klass in vml::Cell.__mro__:
        if "textValue" in klass.__dict__:
            descriptor = klass.__dict__["textValue"]
            break
    assert isinstance(descriptor, property)



def test_vml::row_is_not_abstract():
    assert not inspect.isabstract(vml::Row)


def test_vml::row_constructor_exists():
    assert callable(vml::Row.__init__)


def test_vml::row_constructor_args():
    sig = inspect.signature(vml::Row.__init__)
    params = list(sig.parameters.keys())



def test_vml::column_is_not_abstract():
    assert not inspect.isabstract(vml::Column)


def test_vml::column_constructor_exists():
    assert callable(vml::Column.__init__)


def test_vml::column_constructor_args():
    sig = inspect.signature(vml::Column.__init__)
    params = list(sig.parameters.keys())
    assert "columnTitle" in params, "Missing parameter 'columnTitle'"

def test_vml::column_has_columnTitle():
    assert hasattr(vml::Column, "columnTitle")
    descriptor = None
    for klass in vml::Column.__mro__:
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
        "Solid",
        "Dash",
        "Dot",
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
vml::Category_strategy = st.builds(
    vml::Category,
    category=
        safe_text
)
ChartElement_strategy = st.builds(
    ChartElement,
)
vml::Point_strategy = st.builds(
    vml::Point,
)
vml::StackBars_strategy = st.builds(
    vml::StackBars,
)
vml::Bar_strategy = st.builds(
    vml::Bar,
)
Chart_strategy = st.builds(
    Chart,
)
vml::Scatter_strategy = st.builds(
    vml::Scatter,
)
vml::StackBarChart_strategy = st.builds(
    vml::StackBarChart,
)
vml::LineChart_strategy = st.builds(
    vml::LineChart,
)
vml::BarChart_strategy = st.builds(
    vml::BarChart,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
vml::Edge_strategy = st.builds(
    vml::Edge,
    relation=
        safe_text
)
vml::Node_strategy = st.builds(
    vml::Node,
    title=
        safe_text,
    icone=
        safe_text
)
vml::ChartElement_strategy = st.builds(
    vml::ChartElement,
    yValue=
        safe_text,
    ID=
        safe_text,
    xValue=
        safe_text
)
vml::Slice_strategy = st.builds(
    vml::Slice,
    value=
        st.integers(),
    title=
        safe_text
)
Diagram_strategy = st.builds(
    Diagram,
)
vml::Chart_strategy = st.builds(
    vml::Chart,
    xTitle=
        safe_text,
    yTitle=
        safe_text,
    ID=
        safe_text,
    title=
        safe_text
)
vml::Graph_strategy = st.builds(
    vml::Graph,
    title=
        safe_text,
    ID=
        safe_text
)
vml::Pie_strategy = st.builds(
    vml::Pie,
    identifier=
        safe_text,
    title=
        safe_text
)
vml::DiagramElement_strategy = st.builds(
    vml::DiagramElement,
)
vml::Table_strategy = st.builds(
    vml::Table,
    tableTitle=
        safe_text
)
vml::Diagram_strategy = st.builds(
    vml::Diagram,
)
vml::Model_strategy = st.builds(
    vml::Model,
)
vml::Color_strategy = st.builds(
    vml::Color,
    red=
        st.integers(),
    green=
        st.integers(),
    name=
        safe_text,
    blue=
        st.integers()
)
GraphStyle_strategy = st.builds(
    GraphStyle,
)
vml::EdgeStyle_strategy = st.builds(
    vml::EdgeStyle,
    directed=
        st.booleans(),
    lineStyle=
        safe_text,
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineWidth=
        st.integers()
)
vml::NodeStyle_strategy = st.builds(
    vml::NodeStyle,
    padding=
        st.integers(),
    borderWidth=
        st.integers()
)
Style_strategy = st.builds(
    Style,
)
vml::ChartWithAxisStyle_strategy = st.builds(
    vml::ChartWithAxisStyle,
)
vml::ChartWithoutAxisStyle_strategy = st.builds(
    vml::ChartWithoutAxisStyle,
)
vml::GraphStyle_strategy = st.builds(
    vml::GraphStyle,
)
vml::Style_strategy = st.builds(
    vml::Style,
)
vml::Cell_strategy = st.builds(
    vml::Cell,
    textValue=
        safe_text
)
vml::Row_strategy = st.builds(
    vml::Row,
)
vml::Column_strategy = st.builds(
    vml::Column,
    columnTitle=
        safe_text
)

@given(instance=vml::Category_strategy)
@settings(max_examples=50)
def test_vml::category_instantiation(instance):
    assert isinstance(instance, vml::Category)

@given(instance=vml::Category_strategy)
def test_vml::category_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=vml::Category_strategy)
def test_vml::category_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=ChartElement_strategy)
@settings(max_examples=50)
def test_chartelement_instantiation(instance):
    assert isinstance(instance, ChartElement)

@given(instance=vml::Point_strategy)
@settings(max_examples=50)
def test_vml::point_instantiation(instance):
    assert isinstance(instance, vml::Point)

@given(instance=vml::StackBars_strategy)
@settings(max_examples=50)
def test_vml::stackbars_instantiation(instance):
    assert isinstance(instance, vml::StackBars)

@given(instance=vml::Bar_strategy)
@settings(max_examples=50)
def test_vml::bar_instantiation(instance):
    assert isinstance(instance, vml::Bar)

@given(instance=Chart_strategy)
@settings(max_examples=50)
def test_chart_instantiation(instance):
    assert isinstance(instance, Chart)

@given(instance=vml::Scatter_strategy)
@settings(max_examples=50)
def test_vml::scatter_instantiation(instance):
    assert isinstance(instance, vml::Scatter)

@given(instance=vml::StackBarChart_strategy)
@settings(max_examples=50)
def test_vml::stackbarchart_instantiation(instance):
    assert isinstance(instance, vml::StackBarChart)

@given(instance=vml::LineChart_strategy)
@settings(max_examples=50)
def test_vml::linechart_instantiation(instance):
    assert isinstance(instance, vml::LineChart)

@given(instance=vml::BarChart_strategy)
@settings(max_examples=50)
def test_vml::barchart_instantiation(instance):
    assert isinstance(instance, vml::BarChart)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=vml::Edge_strategy)
@settings(max_examples=50)
def test_vml::edge_instantiation(instance):
    assert isinstance(instance, vml::Edge)

@given(instance=vml::Edge_strategy)
def test_vml::edge_relation_type(instance):
    assert isinstance(instance.relation, str)


@given(instance=vml::Edge_strategy)
def test_vml::edge_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=vml::Node_strategy)
@settings(max_examples=50)
def test_vml::node_instantiation(instance):
    assert isinstance(instance, vml::Node)

@given(instance=vml::Node_strategy)
def test_vml::node_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=vml::Node_strategy)
def test_vml::node_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml::Node_strategy)
def test_vml::node_icone_type(instance):
    assert isinstance(instance.icone, str)


@given(instance=vml::Node_strategy)
def test_vml::node_icone_setter(instance):
    original = instance.icone
    instance.icone = original
    assert instance.icone == original

@given(instance=vml::ChartElement_strategy)
@settings(max_examples=50)
def test_vml::chartelement_instantiation(instance):
    assert isinstance(instance, vml::ChartElement)

@given(instance=vml::ChartElement_strategy)
def test_vml::chartelement_yValue_type(instance):
    assert isinstance(instance.yValue, str)


@given(instance=vml::ChartElement_strategy)
def test_vml::chartelement_yValue_setter(instance):
    original = instance.yValue
    instance.yValue = original
    assert instance.yValue == original

@given(instance=vml::ChartElement_strategy)
def test_vml::chartelement_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=vml::ChartElement_strategy)
def test_vml::chartelement_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=vml::ChartElement_strategy)
def test_vml::chartelement_xValue_type(instance):
    assert isinstance(instance.xValue, str)


@given(instance=vml::ChartElement_strategy)
def test_vml::chartelement_xValue_setter(instance):
    original = instance.xValue
    instance.xValue = original
    assert instance.xValue == original

@given(instance=vml::Slice_strategy)
@settings(max_examples=50)
def test_vml::slice_instantiation(instance):
    assert isinstance(instance, vml::Slice)

@given(instance=vml::Slice_strategy)
def test_vml::slice_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=vml::Slice_strategy)
def test_vml::slice_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vml::Slice_strategy)
def test_vml::slice_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=vml::Slice_strategy)
def test_vml::slice_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=vml::Chart_strategy)
@settings(max_examples=50)
def test_vml::chart_instantiation(instance):
    assert isinstance(instance, vml::Chart)

@given(instance=vml::Chart_strategy)
def test_vml::chart_xTitle_type(instance):
    assert isinstance(instance.xTitle, str)


@given(instance=vml::Chart_strategy)
def test_vml::chart_xTitle_setter(instance):
    original = instance.xTitle
    instance.xTitle = original
    assert instance.xTitle == original

@given(instance=vml::Chart_strategy)
def test_vml::chart_yTitle_type(instance):
    assert isinstance(instance.yTitle, str)


@given(instance=vml::Chart_strategy)
def test_vml::chart_yTitle_setter(instance):
    original = instance.yTitle
    instance.yTitle = original
    assert instance.yTitle == original

@given(instance=vml::Chart_strategy)
def test_vml::chart_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=vml::Chart_strategy)
def test_vml::chart_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=vml::Chart_strategy)
def test_vml::chart_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=vml::Chart_strategy)
def test_vml::chart_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml::Graph_strategy)
@settings(max_examples=50)
def test_vml::graph_instantiation(instance):
    assert isinstance(instance, vml::Graph)

@given(instance=vml::Graph_strategy)
def test_vml::graph_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=vml::Graph_strategy)
def test_vml::graph_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml::Graph_strategy)
def test_vml::graph_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=vml::Graph_strategy)
def test_vml::graph_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=vml::Pie_strategy)
@settings(max_examples=50)
def test_vml::pie_instantiation(instance):
    assert isinstance(instance, vml::Pie)

@given(instance=vml::Pie_strategy)
def test_vml::pie_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=vml::Pie_strategy)
def test_vml::pie_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=vml::Pie_strategy)
def test_vml::pie_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=vml::Pie_strategy)
def test_vml::pie_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml::DiagramElement_strategy)
@settings(max_examples=50)
def test_vml::diagramelement_instantiation(instance):
    assert isinstance(instance, vml::DiagramElement)

@given(instance=vml::Table_strategy)
@settings(max_examples=50)
def test_vml::table_instantiation(instance):
    assert isinstance(instance, vml::Table)

@given(instance=vml::Table_strategy)
def test_vml::table_tableTitle_type(instance):
    assert isinstance(instance.tableTitle, str)


@given(instance=vml::Table_strategy)
def test_vml::table_tableTitle_setter(instance):
    original = instance.tableTitle
    instance.tableTitle = original
    assert instance.tableTitle == original

@given(instance=vml::Diagram_strategy)
@settings(max_examples=50)
def test_vml::diagram_instantiation(instance):
    assert isinstance(instance, vml::Diagram)

@given(instance=vml::Model_strategy)
@settings(max_examples=50)
def test_vml::model_instantiation(instance):
    assert isinstance(instance, vml::Model)

@given(instance=vml::Color_strategy)
@settings(max_examples=50)
def test_vml::color_instantiation(instance):
    assert isinstance(instance, vml::Color)

@given(instance=vml::Color_strategy)
def test_vml::color_red_type(instance):
    assert isinstance(instance.red, int)


@given(instance=vml::Color_strategy)
def test_vml::color_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=vml::Color_strategy)
def test_vml::color_green_type(instance):
    assert isinstance(instance.green, int)


@given(instance=vml::Color_strategy)
def test_vml::color_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=vml::Color_strategy)
def test_vml::color_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vml::Color_strategy)
def test_vml::color_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vml::Color_strategy)
def test_vml::color_blue_type(instance):
    assert isinstance(instance.blue, int)


@given(instance=vml::Color_strategy)
def test_vml::color_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=GraphStyle_strategy)
@settings(max_examples=50)
def test_graphstyle_instantiation(instance):
    assert isinstance(instance, GraphStyle)

@given(instance=vml::EdgeStyle_strategy)
@settings(max_examples=50)
def test_vml::edgestyle_instantiation(instance):
    assert isinstance(instance, vml::EdgeStyle)

@given(instance=vml::EdgeStyle_strategy)
def test_vml::edgestyle_directed_type(instance):
    assert isinstance(instance.directed, bool)


@given(instance=vml::EdgeStyle_strategy)
def test_vml::edgestyle_directed_setter(instance):
    original = instance.directed
    instance.directed = original
    assert instance.directed == original

@given(instance=vml::EdgeStyle_strategy)
def test_vml::edgestyle_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=vml::EdgeStyle_strategy)
def test_vml::edgestyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=vml::EdgeStyle_strategy)
def test_vml::edgestyle_weight_type(instance):
    assert isinstance(instance.weight, float)


@given(instance=vml::EdgeStyle_strategy)
def test_vml::edgestyle_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=vml::EdgeStyle_strategy)
def test_vml::edgestyle_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, int)


@given(instance=vml::EdgeStyle_strategy)
def test_vml::edgestyle_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=vml::NodeStyle_strategy)
@settings(max_examples=50)
def test_vml::nodestyle_instantiation(instance):
    assert isinstance(instance, vml::NodeStyle)

@given(instance=vml::NodeStyle_strategy)
def test_vml::nodestyle_padding_type(instance):
    assert isinstance(instance.padding, int)


@given(instance=vml::NodeStyle_strategy)
def test_vml::nodestyle_padding_setter(instance):
    original = instance.padding
    instance.padding = original
    assert instance.padding == original

@given(instance=vml::NodeStyle_strategy)
def test_vml::nodestyle_borderWidth_type(instance):
    assert isinstance(instance.borderWidth, int)


@given(instance=vml::NodeStyle_strategy)
def test_vml::nodestyle_borderWidth_setter(instance):
    original = instance.borderWidth
    instance.borderWidth = original
    assert instance.borderWidth == original

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=vml::ChartWithAxisStyle_strategy)
@settings(max_examples=50)
def test_vml::chartwithaxisstyle_instantiation(instance):
    assert isinstance(instance, vml::ChartWithAxisStyle)

@given(instance=vml::ChartWithoutAxisStyle_strategy)
@settings(max_examples=50)
def test_vml::chartwithoutaxisstyle_instantiation(instance):
    assert isinstance(instance, vml::ChartWithoutAxisStyle)

@given(instance=vml::GraphStyle_strategy)
@settings(max_examples=50)
def test_vml::graphstyle_instantiation(instance):
    assert isinstance(instance, vml::GraphStyle)

@given(instance=vml::Style_strategy)
@settings(max_examples=50)
def test_vml::style_instantiation(instance):
    assert isinstance(instance, vml::Style)

@given(instance=vml::Cell_strategy)
@settings(max_examples=50)
def test_vml::cell_instantiation(instance):
    assert isinstance(instance, vml::Cell)

@given(instance=vml::Cell_strategy)
def test_vml::cell_textValue_type(instance):
    assert isinstance(instance.textValue, str)


@given(instance=vml::Cell_strategy)
def test_vml::cell_textValue_setter(instance):
    original = instance.textValue
    instance.textValue = original
    assert instance.textValue == original

@given(instance=vml::Row_strategy)
@settings(max_examples=50)
def test_vml::row_instantiation(instance):
    assert isinstance(instance, vml::Row)

@given(instance=vml::Column_strategy)
@settings(max_examples=50)
def test_vml::column_instantiation(instance):
    assert isinstance(instance, vml::Column)

@given(instance=vml::Column_strategy)
def test_vml::column_columnTitle_type(instance):
    assert isinstance(instance.columnTitle, str)


@given(instance=vml::Column_strategy)
def test_vml::column_columnTitle_setter(instance):
    original = instance.columnTitle
    instance.columnTitle = original
    assert instance.columnTitle == original
