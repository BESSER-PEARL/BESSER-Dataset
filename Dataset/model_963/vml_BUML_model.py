####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="Solid"),
			EnumerationLiteral(name="Dash"),
			EnumerationLiteral(name="Dot")
    }
)

# Classes
vml_Model = Class(name="vml::Model")
vml_Diagram = Class(name="vml::Diagram", is_abstract=True)
vml_Table = Class(name="vml::Table")
vml_Column = Class(name="vml::Column")
vml_EdgeStyle = Class(name="vml::EdgeStyle")
vml_Node = Class(name="vml::Node")
vml_Row = Class(name="vml::Row")
vml_Cell = Class(name="vml::Cell")
vml_Style = Class(name="vml::Style")
vml_GraphStyle = Class(name="vml::GraphStyle")
Style = Class(name="Style")
vml_NodeStyle = Class(name="vml::NodeStyle")
GraphStyle = Class(name="GraphStyle")
vml_Color = Class(name="vml::Color")
vml_Edge = Class(name="vml::Edge")
vml_ChartWithAxisStyle = Class(name="vml::ChartWithAxisStyle")
vml_ChartWithoutAxisStyle = Class(name="vml::ChartWithoutAxisStyle")
vml_DiagramElement = Class(name="vml::DiagramElement", is_abstract=True)
vml_Pie = Class(name="vml::Pie")
Diagram = Class(name="Diagram")
vml_Slice = Class(name="vml::Slice")
DiagramElement = Class(name="DiagramElement")
vml_Graph = Class(name="vml::Graph")
vml_StackBars = Class(name="vml::StackBars")
vml_Category = Class(name="vml::Category")
vml_Chart = Class(name="vml::Chart", is_abstract=True)
vml_ChartElement = Class(name="vml::ChartElement")
vml_BarChart = Class(name="vml::BarChart")
Chart = Class(name="Chart")
vml_Bar = Class(name="vml::Bar")
ChartElement = Class(name="ChartElement")
vml_StackBarChart = Class(name="vml::StackBarChart")
vml_LineChart = Class(name="vml::LineChart")
vml_Point = Class(name="vml::Point")
vml_Scatter = Class(name="vml::Scatter")

# vml_Model class attributes and methods

# vml_Diagram class attributes and methods

# vml_Table class attributes and methods
vml_Table_tableTitle: Property = Property(name="tableTitle", type=StringType)
vml_Table.attributes={vml_Table_tableTitle}

# vml_Column class attributes and methods
vml_Column_columnTitle: Property = Property(name="columnTitle", type=StringType)
vml_Column.attributes={vml_Column_columnTitle}

# vml_EdgeStyle class attributes and methods
vml_EdgeStyle_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
vml_EdgeStyle_weight: Property = Property(name="weight", type=FloatType)
vml_EdgeStyle_directed: Property = Property(name="directed", type=BooleanType)
vml_EdgeStyle_lineStyle: Property = Property(name="lineStyle", type=StringType)
vml_EdgeStyle.attributes={vml_EdgeStyle_lineStyle, vml_EdgeStyle_lineWidth, vml_EdgeStyle_weight, vml_EdgeStyle_directed}

# vml_Node class attributes and methods
vml_Node_title: Property = Property(name="title", type=StringType)
vml_Node_icone: Property = Property(name="icone", type=StringType)
vml_Node.attributes={vml_Node_icone, vml_Node_title}

# vml_Row class attributes and methods

# vml_Cell class attributes and methods
vml_Cell_textValue: Property = Property(name="textValue", type=StringType)
vml_Cell.attributes={vml_Cell_textValue}

# vml_Style class attributes and methods

# vml_GraphStyle class attributes and methods

# Style class attributes and methods

# vml_NodeStyle class attributes and methods
vml_NodeStyle_borderWidth: Property = Property(name="borderWidth", type=IntegerType)
vml_NodeStyle_padding: Property = Property(name="padding", type=IntegerType)
vml_NodeStyle.attributes={vml_NodeStyle_borderWidth, vml_NodeStyle_padding}

# GraphStyle class attributes and methods

# vml_Color class attributes and methods
vml_Color_name: Property = Property(name="name", type=StringType)
vml_Color_red: Property = Property(name="red", type=IntegerType)
vml_Color_green: Property = Property(name="green", type=IntegerType)
vml_Color_blue: Property = Property(name="blue", type=IntegerType)
vml_Color.attributes={vml_Color_red, vml_Color_blue, vml_Color_green, vml_Color_name}

# vml_Edge class attributes and methods
vml_Edge_relation: Property = Property(name="relation", type=StringType)
vml_Edge.attributes={vml_Edge_relation}

# vml_ChartWithAxisStyle class attributes and methods

# vml_ChartWithoutAxisStyle class attributes and methods

# vml_DiagramElement class attributes and methods

# vml_Pie class attributes and methods
vml_Pie_title: Property = Property(name="title", type=StringType)
vml_Pie_identifier: Property = Property(name="identifier", type=StringType)
vml_Pie.attributes={vml_Pie_identifier, vml_Pie_title}

# Diagram class attributes and methods

# vml_Slice class attributes and methods
vml_Slice_title: Property = Property(name="title", type=StringType)
vml_Slice_value: Property = Property(name="value", type=IntegerType)
vml_Slice.attributes={vml_Slice_value, vml_Slice_title}

# DiagramElement class attributes and methods

# vml_Graph class attributes and methods
vml_Graph_title: Property = Property(name="title", type=StringType)
vml_Graph_ID: Property = Property(name="ID", type=StringType)
vml_Graph.attributes={vml_Graph_ID, vml_Graph_title}

# vml_StackBars class attributes and methods

# vml_Category class attributes and methods
vml_Category_category: Property = Property(name="category", type=StringType)
vml_Category.attributes={vml_Category_category}

# vml_Chart class attributes and methods
vml_Chart_ID: Property = Property(name="ID", type=StringType)
vml_Chart_title: Property = Property(name="title", type=StringType)
vml_Chart_xTitle: Property = Property(name="xTitle", type=StringType)
vml_Chart_yTitle: Property = Property(name="yTitle", type=StringType)
vml_Chart.attributes={vml_Chart_ID, vml_Chart_xTitle, vml_Chart_yTitle, vml_Chart_title}

# vml_ChartElement class attributes and methods
vml_ChartElement_ID: Property = Property(name="ID", type=StringType)
vml_ChartElement_xValue: Property = Property(name="xValue", type=StringType)
vml_ChartElement_yValue: Property = Property(name="yValue", type=StringType)
vml_ChartElement.attributes={vml_ChartElement_xValue, vml_ChartElement_ID, vml_ChartElement_yValue}

# vml_BarChart class attributes and methods

# Chart class attributes and methods

# vml_Bar class attributes and methods

# ChartElement class attributes and methods

# vml_StackBarChart class attributes and methods

# vml_LineChart class attributes and methods

# vml_Point class attributes and methods

# vml_Scatter class attributes and methods

# Relationships
diagrams0: BinaryAssociation = BinaryAssociation(
    name="diagrams0",
    ends={
        Property(name="vml_Diagram", type=vml_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Model", type=vml_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables1: BinaryAssociation = BinaryAssociation(
    name="tables1",
    ends={
        Property(name="vml_Table", type=vml_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Model2", type=vml_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="vml_Column", type=vml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Table4", type=vml_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borderHighlightColor25: BinaryAssociation = BinaryAssociation(
    name="borderHighlightColor25",
    ends={
        Property(name="vml_Color27", type=vml_NodeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_NodeStyle26", type=vml_Color, multiplicity=Multiplicity(0, 1))
    }
)
source28: BinaryAssociation = BinaryAssociation(
    name="source28",
    ends={
        Property(name="vml_Node", type=vml_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_EdgeStyle", type=vml_Node, multiplicity=Multiplicity(0, 1))
    }
)
target29: BinaryAssociation = BinaryAssociation(
    name="target29",
    ends={
        Property(name="vml_Node31", type=vml_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_EdgeStyle30", type=vml_Node, multiplicity=Multiplicity(0, 1))
    }
)
lineColor32: BinaryAssociation = BinaryAssociation(
    name="lineColor32",
    ends={
        Property(name="vml_Color34", type=vml_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_EdgeStyle33", type=vml_Color, multiplicity=Multiplicity(0, 1))
    }
)
rows5: BinaryAssociation = BinaryAssociation(
    name="rows5",
    ends={
        Property(name="vml_Row", type=vml_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Table6", type=vml_Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cells7: BinaryAssociation = BinaryAssociation(
    name="cells7",
    ends={
        Property(name="vml_Cell", type=vml_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Row8", type=vml_Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col9: BinaryAssociation = BinaryAssociation(
    name="col9",
    ends={
        Property(name="vml_Column11", type=vml_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Cell10", type=vml_Column, multiplicity=Multiplicity(0, 1))
    }
)
digrams13: BinaryAssociation = BinaryAssociation(
    name="digrams13",
    ends={
        Property(name="vml_Diagram14", type=vml_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Diagram12", type=vml_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
backgroundColor15: BinaryAssociation = BinaryAssociation(
    name="backgroundColor15",
    ends={
        Property(name="vml_Color", type=vml_NodeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_NodeStyle", type=vml_Color, multiplicity=Multiplicity(0, 1))
    }
)
foregroundColor16: BinaryAssociation = BinaryAssociation(
    name="foregroundColor16",
    ends={
        Property(name="vml_Color18", type=vml_NodeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_NodeStyle17", type=vml_Color, multiplicity=Multiplicity(0, 1))
    }
)
highlightColor19: BinaryAssociation = BinaryAssociation(
    name="highlightColor19",
    ends={
        Property(name="vml_Color21", type=vml_NodeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_NodeStyle20", type=vml_Color, multiplicity=Multiplicity(0, 1))
    }
)
borderColor22: BinaryAssociation = BinaryAssociation(
    name="borderColor22",
    ends={
        Property(name="vml_Color24", type=vml_NodeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_NodeStyle23", type=vml_Color, multiplicity=Multiplicity(0, 1))
    }
)
nodes46: BinaryAssociation = BinaryAssociation(
    name="nodes46",
    ends={
        Property(name="vml_Node47", type=vml_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Graph", type=vml_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges48: BinaryAssociation = BinaryAssociation(
    name="edges48",
    ends={
        Property(name="vml_Edge", type=vml_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Graph49", type=vml_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style50: BinaryAssociation = BinaryAssociation(
    name="style50",
    ends={
        Property(name="vml_GraphStyle", type=vml_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Graph51", type=vml_GraphStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoing52: BinaryAssociation = BinaryAssociation(
    name="outgoing52",
    ends={
        Property(name="Edge", type=vml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=vml_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
highlightColor35: BinaryAssociation = BinaryAssociation(
    name="highlightColor35",
    ends={
        Property(name="vml_Color37", type=vml_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_EdgeStyle36", type=vml_Color, multiplicity=Multiplicity(0, 1))
    }
)
diagrams38: BinaryAssociation = BinaryAssociation(
    name="diagrams38",
    ends={
        Property(name="vml_Diagram39", type=vml_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_DiagramElement", type=vml_Diagram, multiplicity=Multiplicity(0, 1))
    }
)
table40: BinaryAssociation = BinaryAssociation(
    name="table40",
    ends={
        Property(name="vml_Table42", type=vml_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_DiagramElement41", type=vml_Table, multiplicity=Multiplicity(0, 1))
    }
)
slices43: BinaryAssociation = BinaryAssociation(
    name="slices43",
    ends={
        Property(name="vml_Slice", type=vml_Pie, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Pie", type=vml_Slice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style44: BinaryAssociation = BinaryAssociation(
    name="style44",
    ends={
        Property(name="vml_ChartWithoutAxisStyle", type=vml_Pie, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Pie45", type=vml_ChartWithoutAxisStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stackBar60: BinaryAssociation = BinaryAssociation(
    name="stackBar60",
    ends={
        Property(name="vml_StackBars", type=vml_StackBarChart, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_StackBarChart", type=vml_StackBars, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categories61: BinaryAssociation = BinaryAssociation(
    name="categories61",
    ends={
        Property(name="vml_Category", type=vml_StackBarChart, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_StackBarChart62", type=vml_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
category63: BinaryAssociation = BinaryAssociation(
    name="category63",
    ends={
        Property(name="vml_Category65", type=vml_StackBars, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_StackBars64", type=vml_Category, multiplicity=Multiplicity(0, 1))
    }
)
bars66: BinaryAssociation = BinaryAssociation(
    name="bars66",
    ends={
        Property(name="vml_Bar68", type=vml_StackBars, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_StackBars67", type=vml_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming53: BinaryAssociation = BinaryAssociation(
    name="incoming53",
    ends={
        Property(name="Edge54", type=vml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=vml_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source55: BinaryAssociation = BinaryAssociation(
    name="source55",
    ends={
        Property(name="Node", type=vml_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=vml_Node, multiplicity=Multiplicity(0, 1))
    }
)
target56: BinaryAssociation = BinaryAssociation(
    name="target56",
    ends={
        Property(name="Node57", type=vml_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=vml_Node, multiplicity=Multiplicity(0, 1))
    }
)
style58: BinaryAssociation = BinaryAssociation(
    name="style58",
    ends={
        Property(name="vml_ChartWithAxisStyle", type=vml_Chart, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Chart", type=vml_ChartWithAxisStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bars59: BinaryAssociation = BinaryAssociation(
    name="bars59",
    ends={
        Property(name="vml_Bar", type=vml_BarChart, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_BarChart", type=vml_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
points69: BinaryAssociation = BinaryAssociation(
    name="points69",
    ends={
        Property(name="vml_Point", type=vml_LineChart, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_LineChart", type=vml_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
points70: BinaryAssociation = BinaryAssociation(
    name="points70",
    ends={
        Property(name="vml_Point71", type=vml_Scatter, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Scatter", type=vml_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_vml_EdgeStyle_GraphStyle = Generalization(general=GraphStyle, specific=vml_EdgeStyle)
gen_vml_GraphStyle_Style = Generalization(general=Style, specific=vml_GraphStyle)
gen_vml_NodeStyle_GraphStyle = Generalization(general=GraphStyle, specific=vml_NodeStyle)
gen_vml_Node_DiagramElement = Generalization(general=DiagramElement, specific=vml_Node)
gen_vml_ChartWithAxisStyle_Style = Generalization(general=Style, specific=vml_ChartWithAxisStyle)
gen_vml_ChartWithoutAxisStyle_Style = Generalization(general=Style, specific=vml_ChartWithoutAxisStyle)
gen_vml_Pie_Diagram = Generalization(general=Diagram, specific=vml_Pie)
gen_vml_Slice_DiagramElement = Generalization(general=DiagramElement, specific=vml_Slice)
gen_vml_Graph_Diagram = Generalization(general=Diagram, specific=vml_Graph)
gen_vml_StackBars_ChartElement = Generalization(general=ChartElement, specific=vml_StackBars)
gen_vml_Edge_DiagramElement = Generalization(general=DiagramElement, specific=vml_Edge)
gen_vml_Chart_Diagram = Generalization(general=Diagram, specific=vml_Chart)
gen_vml_ChartElement_DiagramElement = Generalization(general=DiagramElement, specific=vml_ChartElement)
gen_vml_BarChart_Chart = Generalization(general=Chart, specific=vml_BarChart)
gen_vml_Bar_ChartElement = Generalization(general=ChartElement, specific=vml_Bar)
gen_vml_StackBarChart_Chart = Generalization(general=Chart, specific=vml_StackBarChart)
gen_vml_LineChart_Chart = Generalization(general=Chart, specific=vml_LineChart)
gen_vml_Point_ChartElement = Generalization(general=ChartElement, specific=vml_Point)
gen_vml_Scatter_Chart = Generalization(general=Chart, specific=vml_Scatter)

# Domain Model
domain_model = DomainModel(
    name="vml",
    types={vml_Model, vml_Diagram, vml_Table, vml_Column, vml_EdgeStyle, vml_Node, vml_Row, vml_Cell, vml_Style, vml_GraphStyle, Style, vml_NodeStyle, GraphStyle, vml_Color, vml_Edge, vml_ChartWithAxisStyle, vml_ChartWithoutAxisStyle, vml_DiagramElement, vml_Pie, Diagram, vml_Slice, DiagramElement, vml_Graph, vml_StackBars, vml_Category, vml_Chart, vml_ChartElement, vml_BarChart, Chart, vml_Bar, ChartElement, vml_StackBarChart, vml_LineChart, vml_Point, vml_Scatter, LineStyle},
    associations={diagrams0, tables1, columns3, borderHighlightColor25, source28, target29, lineColor32, rows5, cells7, col9, digrams13, backgroundColor15, foregroundColor16, highlightColor19, borderColor22, nodes46, edges48, style50, outgoing52, highlightColor35, diagrams38, table40, slices43, style44, stackBar60, categories61, category63, bars66, incoming53, source55, target56, style58, bars59, points69, points70},
    generalizations={gen_vml_EdgeStyle_GraphStyle, gen_vml_GraphStyle_Style, gen_vml_NodeStyle_GraphStyle, gen_vml_Node_DiagramElement, gen_vml_ChartWithAxisStyle_Style, gen_vml_ChartWithoutAxisStyle_Style, gen_vml_Pie_Diagram, gen_vml_Slice_DiagramElement, gen_vml_Graph_Diagram, gen_vml_StackBars_ChartElement, gen_vml_Edge_DiagramElement, gen_vml_Chart_Diagram, gen_vml_ChartElement_DiagramElement, gen_vml_BarChart_Chart, gen_vml_Bar_ChartElement, gen_vml_StackBarChart_Chart, gen_vml_LineChart_Chart, gen_vml_Point_ChartElement, gen_vml_Scatter_Chart},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)