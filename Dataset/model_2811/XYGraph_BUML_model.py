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
ZoomType: Enumeration = Enumeration(
    name="ZoomType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="RUBBERBAND_ZOOM"),
			EnumerationLiteral(name="DYNAMIC_ZOOM"),
			EnumerationLiteral(name="HORIZONTAL_ZOOM"),
			EnumerationLiteral(name="VERTICAL_ZOOM"),
			EnumerationLiteral(name="ZOOM_IN"),
			EnumerationLiteral(name="ZOOM_OUT"),
			EnumerationLiteral(name="ZOOM_IN_HORIZONTALLY"),
			EnumerationLiteral(name="ZOOM_OUT_HORIZONTALLY"),
			EnumerationLiteral(name="ZOOM_IN_VERTICALLY"),
			EnumerationLiteral(name="ZOOM_OUT_VERTICALLY"),
			EnumerationLiteral(name="PANNING")
    }
)

Trace_BaseLine: Enumeration = Enumeration(
    name="Trace_BaseLine",
    literals={
            EnumerationLiteral(name="NEGATIVE_INFINITY"),
			EnumerationLiteral(name="ZERO"),
			EnumerationLiteral(name="POSITIVE_INFINITY")
    }
)

Trace_PointStyle: Enumeration = Enumeration(
    name="Trace_PointStyle",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="POINT"),
			EnumerationLiteral(name="CIRCLE"),
			EnumerationLiteral(name="TRIANGLE"),
			EnumerationLiteral(name="FILLED_TRIANGLE"),
			EnumerationLiteral(name="SQUARE"),
			EnumerationLiteral(name="FILLED_SQUARE"),
			EnumerationLiteral(name="DIAMOND"),
			EnumerationLiteral(name="FILLED_DIAMOND"),
			EnumerationLiteral(name="XCROSS"),
			EnumerationLiteral(name="CROSS"),
			EnumerationLiteral(name="BAR")
    }
)

LinearScale_Orientation: Enumeration = Enumeration(
    name="LinearScale_Orientation",
    literals={
            EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="VERTICAL")
    }
)

Trace_ErrorBarType: Enumeration = Enumeration(
    name="Trace_ErrorBarType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="BOTH")
    }
)

Trace_TraceType: Enumeration = Enumeration(
    name="Trace_TraceType",
    literals={
            EnumerationLiteral(name="DOT_LINE"),
			EnumerationLiteral(name="SOLID_LINE"),
			EnumerationLiteral(name="DASH_LINE"),
			EnumerationLiteral(name="POINT"),
			EnumerationLiteral(name="BAR"),
			EnumerationLiteral(name="AREA"),
			EnumerationLiteral(name="LINE_AREA"),
			EnumerationLiteral(name="STEP_VERTICALLY"),
			EnumerationLiteral(name="STEP_HORIZONTALLY"),
			EnumerationLiteral(name="DASHDOT_LINE"),
			EnumerationLiteral(name="DASHDOTDOT_LINE")
    }
)

# Classes
xygraph_XYGraphDescriptor = Class(name="xygraph::XYGraphDescriptor")
xygraph_ColorDescriptor = Class(name="xygraph::ColorDescriptor")
xygraph_EObject = Class(name="xygraph::EObject")
xygraph_AxisDescriptor = Class(name="xygraph::AxisDescriptor")
xygraph_TraceDescriptor = Class(name="xygraph::TraceDescriptor")
xygraph_FontDescriptor = Class(name="xygraph::FontDescriptor")

# xygraph_XYGraphDescriptor class attributes and methods
xygraph_XYGraphDescriptor_title: Property = Property(name="title", type=StringType)
xygraph_XYGraphDescriptor_showLegend: Property = Property(name="showLegend", type=BooleanType)
xygraph_XYGraphDescriptor_showTitle: Property = Property(name="showTitle", type=BooleanType)
xygraph_XYGraphDescriptor_transparent: Property = Property(name="transparent", type=BooleanType)
xygraph_XYGraphDescriptor_zoomType: Property = Property(name="zoomType", type=StringType)
xygraph_XYGraphDescriptor_showPlotAreaBorder: Property = Property(name="showPlotAreaBorder", type=BooleanType)
xygraph_XYGraphDescriptor.attributes={xygraph_XYGraphDescriptor_zoomType, xygraph_XYGraphDescriptor_showPlotAreaBorder, xygraph_XYGraphDescriptor_showTitle, xygraph_XYGraphDescriptor_title, xygraph_XYGraphDescriptor_transparent, xygraph_XYGraphDescriptor_showLegend}

# xygraph_ColorDescriptor class attributes and methods
xygraph_ColorDescriptor_r: Property = Property(name="r", type=IntegerType)
xygraph_ColorDescriptor_g: Property = Property(name="g", type=IntegerType)
xygraph_ColorDescriptor_b: Property = Property(name="b", type=IntegerType)
xygraph_ColorDescriptor.attributes={xygraph_ColorDescriptor_b, xygraph_ColorDescriptor_g, xygraph_ColorDescriptor_r}

# xygraph_EObject class attributes and methods

# xygraph_AxisDescriptor class attributes and methods
xygraph_AxisDescriptor_orientation: Property = Property(name="orientation", type=StringType)
xygraph_AxisDescriptor_autoScale: Property = Property(name="autoScale", type=BooleanType)
xygraph_AxisDescriptor_minorTicksVisible: Property = Property(name="minorTicksVisible", type=BooleanType)
xygraph_AxisDescriptor_primarySide: Property = Property(name="primarySide", type=BooleanType)
xygraph_AxisDescriptor_rangeLower: Property = Property(name="rangeLower", type=FloatType)
xygraph_AxisDescriptor_rangeUpper: Property = Property(name="rangeUpper", type=FloatType)
xygraph_AxisDescriptor_showMajorGrid: Property = Property(name="showMajorGrid", type=BooleanType)
xygraph_AxisDescriptor_showMinorGrid: Property = Property(name="showMinorGrid", type=BooleanType)
xygraph_AxisDescriptor_title: Property = Property(name="title", type=StringType)
xygraph_AxisDescriptor_zoomType: Property = Property(name="zoomType", type=StringType)
xygraph_AxisDescriptor_autoScaleThreshold: Property = Property(name="autoScaleThreshold", type=FloatType)
xygraph_AxisDescriptor_dashGridLine: Property = Property(name="dashGridLine", type=BooleanType)
xygraph_AxisDescriptor_logScale: Property = Property(name="logScale", type=BooleanType)
xygraph_AxisDescriptor_autoFormat: Property = Property(name="autoFormat", type=BooleanType)
xygraph_AxisDescriptor_dateEnabled: Property = Property(name="dateEnabled", type=BooleanType)
xygraph_AxisDescriptor_formatPattern: Property = Property(name="formatPattern", type=StringType)
xygraph_AxisDescriptor.attributes={xygraph_AxisDescriptor_formatPattern, xygraph_AxisDescriptor_orientation, xygraph_AxisDescriptor_autoScale, xygraph_AxisDescriptor_autoScaleThreshold, xygraph_AxisDescriptor_rangeLower, xygraph_AxisDescriptor_zoomType, xygraph_AxisDescriptor_logScale, xygraph_AxisDescriptor_showMajorGrid, xygraph_AxisDescriptor_showMinorGrid, xygraph_AxisDescriptor_primarySide, xygraph_AxisDescriptor_rangeUpper, xygraph_AxisDescriptor_dashGridLine, xygraph_AxisDescriptor_dateEnabled, xygraph_AxisDescriptor_minorTicksVisible, xygraph_AxisDescriptor_title, xygraph_AxisDescriptor_autoFormat}

# xygraph_TraceDescriptor class attributes and methods
xygraph_TraceDescriptor_baseLine: Property = Property(name="baseLine", type=StringType)
xygraph_TraceDescriptor_drawYErrorInArea: Property = Property(name="drawYErrorInArea", type=BooleanType)
xygraph_TraceDescriptor_errorBarCapWidth: Property = Property(name="errorBarCapWidth", type=IntegerType)
xygraph_TraceDescriptor_errorBarEnabled: Property = Property(name="errorBarEnabled", type=BooleanType)
xygraph_TraceDescriptor_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
xygraph_TraceDescriptor_name: Property = Property(name="name", type=StringType)
xygraph_TraceDescriptor_pointSize: Property = Property(name="pointSize", type=IntegerType)
xygraph_TraceDescriptor_pointStyle: Property = Property(name="pointStyle", type=StringType)
xygraph_TraceDescriptor_antiAliasing: Property = Property(name="antiAliasing", type=BooleanType)
xygraph_TraceDescriptor_areaAlpha: Property = Property(name="areaAlpha", type=IntegerType)
xygraph_TraceDescriptor_traceType: Property = Property(name="traceType", type=StringType)
xygraph_TraceDescriptor_xErrorBarType: Property = Property(name="xErrorBarType", type=StringType)
xygraph_TraceDescriptor_yErrorBarType: Property = Property(name="yErrorBarType", type=StringType)
xygraph_TraceDescriptor.attributes={xygraph_TraceDescriptor_lineWidth, xygraph_TraceDescriptor_traceType, xygraph_TraceDescriptor_drawYErrorInArea, xygraph_TraceDescriptor_antiAliasing, xygraph_TraceDescriptor_errorBarEnabled, xygraph_TraceDescriptor_baseLine, xygraph_TraceDescriptor_errorBarCapWidth, xygraph_TraceDescriptor_name, xygraph_TraceDescriptor_yErrorBarType, xygraph_TraceDescriptor_areaAlpha, xygraph_TraceDescriptor_xErrorBarType, xygraph_TraceDescriptor_pointStyle, xygraph_TraceDescriptor_pointSize}

# xygraph_FontDescriptor class attributes and methods
xygraph_FontDescriptor_name: Property = Property(name="name", type=StringType)
xygraph_FontDescriptor_size: Property = Property(name="size", type=IntegerType)
xygraph_FontDescriptor_style: Property = Property(name="style", type=IntegerType)
xygraph_FontDescriptor.attributes={xygraph_FontDescriptor_style, xygraph_FontDescriptor_size, xygraph_FontDescriptor_name}

# Relationships
titleColor0: BinaryAssociation = BinaryAssociation(
    name="titleColor0",
    ends={
        Property(name="xygraph_ColorDescriptor", type=xygraph_XYGraphDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_XYGraphDescriptor", type=xygraph_ColorDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
titleFont8: BinaryAssociation = BinaryAssociation(
    name="titleFont8",
    ends={
        Property(name="xygraph_XYGraphDescriptor9", type=xygraph_FontDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="xygraph_FontDescriptor", type=xygraph_XYGraphDescriptor, multiplicity=Multiplicity(1, 1))
    }
)
context10: BinaryAssociation = BinaryAssociation(
    name="context10",
    ends={
        Property(name="xygraph_EObject", type=xygraph_XYGraphDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_XYGraphDescriptor11", type=xygraph_EObject, multiplicity=Multiplicity(1, 1))
    }
)
dataSource12: BinaryAssociation = BinaryAssociation(
    name="dataSource12",
    ends={
        Property(name="xygraph_EObject14", type=xygraph_XYGraphDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_XYGraphDescriptor13", type=xygraph_EObject, multiplicity=Multiplicity(0, 1))
    }
)
visibleTraces15: BinaryAssociation = BinaryAssociation(
    name="visibleTraces15",
    ends={
        Property(name="xygraph_TraceDescriptor17", type=xygraph_XYGraphDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_XYGraphDescriptor16", type=xygraph_TraceDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
axisDescriptors1: BinaryAssociation = BinaryAssociation(
    name="axisDescriptors1",
    ends={
        Property(name="xygraph_AxisDescriptor", type=xygraph_XYGraphDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_XYGraphDescriptor2", type=xygraph_AxisDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traceDescriptors3: BinaryAssociation = BinaryAssociation(
    name="traceDescriptors3",
    ends={
        Property(name="xygraph_TraceDescriptor", type=xygraph_XYGraphDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_XYGraphDescriptor4", type=xygraph_TraceDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plotAreaBackgroundColor5: BinaryAssociation = BinaryAssociation(
    name="plotAreaBackgroundColor5",
    ends={
        Property(name="xygraph_ColorDescriptor7", type=xygraph_XYGraphDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_XYGraphDescriptor6", type=xygraph_ColorDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minorGridColor27: BinaryAssociation = BinaryAssociation(
    name="minorGridColor27",
    ends={
        Property(name="xygraph_ColorDescriptor29", type=xygraph_AxisDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_AxisDescriptor28", type=xygraph_ColorDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor18: BinaryAssociation = BinaryAssociation(
    name="backgroundColor18",
    ends={
        Property(name="xygraph_ColorDescriptor20", type=xygraph_AxisDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_AxisDescriptor19", type=xygraph_ColorDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColor21: BinaryAssociation = BinaryAssociation(
    name="foregroundColor21",
    ends={
        Property(name="xygraph_ColorDescriptor23", type=xygraph_AxisDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_AxisDescriptor22", type=xygraph_ColorDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
majorGridColor24: BinaryAssociation = BinaryAssociation(
    name="majorGridColor24",
    ends={
        Property(name="xygraph_ColorDescriptor26", type=xygraph_AxisDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_AxisDescriptor25", type=xygraph_ColorDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
errorBarColor36: BinaryAssociation = BinaryAssociation(
    name="errorBarColor36",
    ends={
        Property(name="xygraph_ColorDescriptor38", type=xygraph_TraceDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_TraceDescriptor37", type=xygraph_ColorDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
titleFont30: BinaryAssociation = BinaryAssociation(
    name="titleFont30",
    ends={
        Property(name="xygraph_FontDescriptor32", type=xygraph_AxisDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_AxisDescriptor31", type=xygraph_FontDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font33: BinaryAssociation = BinaryAssociation(
    name="font33",
    ends={
        Property(name="xygraph_FontDescriptor35", type=xygraph_AxisDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_AxisDescriptor34", type=xygraph_FontDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
traceColor39: BinaryAssociation = BinaryAssociation(
    name="traceColor39",
    ends={
        Property(name="xygraph_ColorDescriptor41", type=xygraph_TraceDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_TraceDescriptor40", type=xygraph_ColorDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xAxis42: BinaryAssociation = BinaryAssociation(
    name="xAxis42",
    ends={
        Property(name="xygraph_AxisDescriptor44", type=xygraph_TraceDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_TraceDescriptor43", type=xygraph_AxisDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
yAxis45: BinaryAssociation = BinaryAssociation(
    name="yAxis45",
    ends={
        Property(name="xygraph_AxisDescriptor47", type=xygraph_TraceDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_TraceDescriptor46", type=xygraph_AxisDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
dataSource48: BinaryAssociation = BinaryAssociation(
    name="dataSource48",
    ends={
        Property(name="xygraph_EObject50", type=xygraph_TraceDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="xygraph_TraceDescriptor49", type=xygraph_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="xygraph",
    types={xygraph_XYGraphDescriptor, xygraph_ColorDescriptor, xygraph_EObject, xygraph_AxisDescriptor, xygraph_TraceDescriptor, xygraph_FontDescriptor, ZoomType, Trace_BaseLine, Trace_PointStyle, LinearScale_Orientation, Trace_ErrorBarType, Trace_TraceType},
    associations={titleColor0, titleFont8, context10, dataSource12, visibleTraces15, axisDescriptors1, traceDescriptors3, plotAreaBackgroundColor5, minorGridColor27, backgroundColor18, foregroundColor21, majorGridColor24, errorBarColor36, titleFont30, font33, traceColor39, xAxis42, yAxis45, dataSource48},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)