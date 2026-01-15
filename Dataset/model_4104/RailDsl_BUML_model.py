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
Side: Enumeration = Enumeration(
    name="Side",
    literals={
            EnumerationLiteral(name="Both"),
			EnumerationLiteral(name="Right"),
			EnumerationLiteral(name="Left")
    }
)

SpeedLimit: Enumeration = Enumeration(
    name="SpeedLimit",
    literals={
            EnumerationLiteral(name="Stop"),
			EnumerationLiteral(name="Speed40"),
			EnumerationLiteral(name="Speed80"),
			EnumerationLiteral(name="Speed120"),
			EnumerationLiteral(name="Max")
    }
)

PointKind: Enumeration = Enumeration(
    name="PointKind",
    literals={
            EnumerationLiteral(name="FixedCrossing"),
			EnumerationLiteral(name="SimplePoint"),
			EnumerationLiteral(name="DoublePoint"),
			EnumerationLiteral(name="SingleSlipPoint"),
			EnumerationLiteral(name="DoubleSlipPoint")
    }
)

VertexKind: Enumeration = Enumeration(
    name="VertexKind",
    literals={
            EnumerationLiteral(name="InnerVertex"),
			EnumerationLiteral(name="TrackEnd"),
			EnumerationLiteral(name="StationBorder")
    }
)

Orientation: Enumeration = Enumeration(
    name="Orientation",
    literals={
            EnumerationLiteral(name="Forwards"),
			EnumerationLiteral(name="Backwards")
    }
)

TrainRouteKind: Enumeration = Enumeration(
    name="TrainRouteKind",
    literals={
            EnumerationLiteral(name="Main"),
			EnumerationLiteral(name="Shunting")
    }
)

# Classes
railDsl_Station = Class(name="railDsl::Station")
NamedElement = Class(name="NamedElement")
railDsl_Declaration = Class(name="railDsl::Declaration", is_abstract=True)
railDsl_LevelCrossing = Class(name="railDsl::LevelCrossing")
railDsl_Signal = Class(name="railDsl::Signal")
railDsl_Platform = Class(name="railDsl::Platform")
railDsl_Point = Class(name="railDsl::Point")
railDsl_TrackObject = Class(name="railDsl::TrackObject", is_abstract=True)
Declaration = Class(name="Declaration")
RouteObject = Class(name="RouteObject")
railDsl_Vertex = Class(name="railDsl::Vertex")
railDsl_Segment = Class(name="railDsl::Segment")
TrackObject = Class(name="TrackObject")
railDsl_SegmentObject = Class(name="railDsl::SegmentObject", is_abstract=True)
railDsl_SegmentPosition = Class(name="railDsl::SegmentPosition")
railDsl_Derailer = Class(name="railDsl::Derailer")
SegmentObject = Class(name="SegmentObject")
railDsl_Train = Class(name="railDsl::Train")
railDsl_TrainSegment = Class(name="railDsl::TrainSegment")
railDsl_RouteObject = Class(name="railDsl::RouteObject", is_abstract=True)
railDsl_TrainRoute = Class(name="railDsl::TrainRoute")
railDsl_TrainRouteObject = Class(name="railDsl::TrainRouteObject")
railDsl_Track = Class(name="railDsl::Track")
railDsl_NamedElement = Class(name="railDsl::NamedElement", is_abstract=True)
railDsl_TrainRoutePoint = Class(name="railDsl::TrainRoutePoint")
TrainRouteObject = Class(name="TrainRouteObject")
railDsl_TrainRouteSegment = Class(name="railDsl::TrainRouteSegment")

# railDsl_Station class attributes and methods

# NamedElement class attributes and methods

# railDsl_Declaration class attributes and methods

# railDsl_LevelCrossing class attributes and methods
railDsl_LevelCrossing_closed: Property = Property(name="closed", type=BooleanType)
railDsl_LevelCrossing_length: Property = Property(name="length", type=FloatType)
railDsl_LevelCrossing.attributes={railDsl_LevelCrossing_length, railDsl_LevelCrossing_closed}

# railDsl_Signal class attributes and methods
railDsl_Signal_main: Property = Property(name="main", type=BooleanType)
railDsl_Signal_shunting: Property = Property(name="shunting", type=BooleanType)
railDsl_Signal.attributes={railDsl_Signal_shunting, railDsl_Signal_main}

# railDsl_Platform class attributes and methods
railDsl_Platform_length: Property = Property(name="length", type=FloatType)
railDsl_Platform.attributes={railDsl_Platform_length}

# railDsl_Point class attributes and methods
railDsl_Point_kind: Property = Property(name="kind", type=StringType)
railDsl_Point_selectedInput: Property = Property(name="selectedInput", type=IntegerType)
railDsl_Point_selectedOutput: Property = Property(name="selectedOutput", type=IntegerType)
railDsl_Point_locked: Property = Property(name="locked", type=BooleanType)
railDsl_Point.attributes={railDsl_Point_selectedOutput, railDsl_Point_locked, railDsl_Point_selectedInput, railDsl_Point_kind}

# railDsl_TrackObject class attributes and methods
railDsl_TrackObject_length: Property = Property(name="length", type=FloatType)
railDsl_TrackObject.attributes={railDsl_TrackObject_length}

# Declaration class attributes and methods

# RouteObject class attributes and methods

# railDsl_Vertex class attributes and methods
railDsl_Vertex_kind: Property = Property(name="kind", type=StringType)
railDsl_Vertex.attributes={railDsl_Vertex_kind}

# railDsl_Segment class attributes and methods

# TrackObject class attributes and methods

# railDsl_SegmentObject class attributes and methods

# railDsl_SegmentPosition class attributes and methods
railDsl_SegmentPosition_atStart: Property = Property(name="atStart", type=BooleanType)
railDsl_SegmentPosition_atEnd: Property = Property(name="atEnd", type=BooleanType)
railDsl_SegmentPosition_position: Property = Property(name="position", type=FloatType)
railDsl_SegmentPosition_side: Property = Property(name="side", type=StringType)
railDsl_SegmentPosition_orientation: Property = Property(name="orientation", type=StringType)
railDsl_SegmentPosition.attributes={railDsl_SegmentPosition_position, railDsl_SegmentPosition_atEnd, railDsl_SegmentPosition_side, railDsl_SegmentPosition_atStart, railDsl_SegmentPosition_orientation}

# railDsl_Derailer class attributes and methods
railDsl_Derailer_active: Property = Property(name="active", type=BooleanType)
railDsl_Derailer.attributes={railDsl_Derailer_active}

# SegmentObject class attributes and methods

# railDsl_Train class attributes and methods
railDsl_Train_length: Property = Property(name="length", type=FloatType)
railDsl_Train_speed: Property = Property(name="speed", type=FloatType)
railDsl_Train_acceleration: Property = Property(name="acceleration", type=FloatType)
railDsl_Train.attributes={railDsl_Train_speed, railDsl_Train_acceleration, railDsl_Train_length}

# railDsl_TrainSegment class attributes and methods
railDsl_TrainSegment_length: Property = Property(name="length", type=FloatType)
railDsl_TrainSegment.attributes={railDsl_TrainSegment_length}

# railDsl_RouteObject class attributes and methods
railDsl_RouteObject_speedLimit: Property = Property(name="speedLimit", type=StringType)
railDsl_RouteObject_error: Property = Property(name="error", type=BooleanType)
railDsl_RouteObject.attributes={railDsl_RouteObject_error, railDsl_RouteObject_speedLimit}

# railDsl_TrainRoute class attributes and methods
railDsl_TrainRoute_kind: Property = Property(name="kind", type=StringType)
railDsl_TrainRoute_locked: Property = Property(name="locked", type=BooleanType)
railDsl_TrainRoute.attributes={railDsl_TrainRoute_locked, railDsl_TrainRoute_kind}

# railDsl_TrainRouteObject class attributes and methods
railDsl_TrainRouteObject_speedLimit: Property = Property(name="speedLimit", type=StringType)
railDsl_TrainRouteObject.attributes={railDsl_TrainRouteObject_speedLimit}

# railDsl_Track class attributes and methods

# railDsl_NamedElement class attributes and methods
railDsl_NamedElement_name: Property = Property(name="name", type=StringType)
railDsl_NamedElement.attributes={railDsl_NamedElement_name}

# railDsl_TrainRoutePoint class attributes and methods
railDsl_TrainRoutePoint_selectedInput: Property = Property(name="selectedInput", type=IntegerType)
railDsl_TrainRoutePoint_selectedOutput: Property = Property(name="selectedOutput", type=IntegerType)
railDsl_TrainRoutePoint.attributes={railDsl_TrainRoutePoint_selectedInput, railDsl_TrainRoutePoint_selectedOutput}

# TrainRouteObject class attributes and methods

# railDsl_TrainRouteSegment class attributes and methods

# Relationships
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="railDsl_Declaration", type=railDsl_Station, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_Station", type=railDsl_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
distantFor10: BinaryAssociation = BinaryAssociation(
    name="distantFor10",
    ends={
        Property(name="railDsl_Signal", type=railDsl_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_Signal9", type=railDsl_Signal, multiplicity=Multiplicity(0, 1))
    }
)
segment11: BinaryAssociation = BinaryAssociation(
    name="segment11",
    ends={
        Property(name="railDsl_Segment13", type=railDsl_SegmentPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_SegmentPosition12", type=railDsl_Segment, multiplicity=Multiplicity(0, 1))
    }
)
inputs14: BinaryAssociation = BinaryAssociation(
    name="inputs14",
    ends={
        Property(name="railDsl_Vertex15", type=railDsl_Point, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_Point", type=railDsl_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
outputs16: BinaryAssociation = BinaryAssociation(
    name="outputs16",
    ends={
        Property(name="railDsl_Vertex18", type=railDsl_Point, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_Point17", type=railDsl_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
start1: BinaryAssociation = BinaryAssociation(
    name="start1",
    ends={
        Property(name="railDsl_Vertex", type=railDsl_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_Segment", type=railDsl_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
end2: BinaryAssociation = BinaryAssociation(
    name="end2",
    ends={
        Property(name="railDsl_Vertex4", type=railDsl_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_Segment3", type=railDsl_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
objects5: BinaryAssociation = BinaryAssociation(
    name="objects5",
    ends={
        Property(name="railDsl_SegmentObject", type=railDsl_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_Segment6", type=railDsl_SegmentObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position7: BinaryAssociation = BinaryAssociation(
    name="position7",
    ends={
        Property(name="railDsl_SegmentPosition", type=railDsl_SegmentObject, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_SegmentObject8", type=railDsl_SegmentPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
segments20: BinaryAssociation = BinaryAssociation(
    name="segments20",
    ends={
        Property(name="railDsl_TrainSegment", type=railDsl_Train, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_Train", type=railDsl_TrainSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position21: BinaryAssociation = BinaryAssociation(
    name="position21",
    ends={
        Property(name="railDsl_SegmentPosition23", type=railDsl_Train, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_Train22", type=railDsl_SegmentPosition, multiplicity=Multiplicity(0, 1))
    }
)
position24: BinaryAssociation = BinaryAssociation(
    name="position24",
    ends={
        Property(name="railDsl_SegmentPosition26", type=railDsl_TrainSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_TrainSegment25", type=railDsl_SegmentPosition, multiplicity=Multiplicity(0, 1))
    }
)
path27: BinaryAssociation = BinaryAssociation(
    name="path27",
    ends={
        Property(name="railDsl_TrainRouteObject", type=railDsl_TrainRoute, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_TrainRoute", type=railDsl_TrainRouteObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements19: BinaryAssociation = BinaryAssociation(
    name="elements19",
    ends={
        Property(name="railDsl_TrackObject", type=railDsl_Track, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_Track", type=railDsl_TrackObject, multiplicity=Multiplicity(0, 9999))
    }
)
startSignal28: BinaryAssociation = BinaryAssociation(
    name="startSignal28",
    ends={
        Property(name="railDsl_Signal30", type=railDsl_TrainRoute, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_TrainRoute29", type=railDsl_Signal, multiplicity=Multiplicity(0, 1))
    }
)
endSignal31: BinaryAssociation = BinaryAssociation(
    name="endSignal31",
    ends={
        Property(name="railDsl_Signal33", type=railDsl_TrainRoute, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_TrainRoute32", type=railDsl_Signal, multiplicity=Multiplicity(0, 1))
    }
)
protectionObjects34: BinaryAssociation = BinaryAssociation(
    name="protectionObjects34",
    ends={
        Property(name="railDsl_TrainRouteObject36", type=railDsl_TrainRoute, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_TrainRoute35", type=railDsl_TrainRouteObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conflictingRoutes38: BinaryAssociation = BinaryAssociation(
    name="conflictingRoutes38",
    ends={
        Property(name="railDsl_TrainRoute39", type=railDsl_TrainRoute, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_TrainRoute37", type=railDsl_TrainRoute, multiplicity=Multiplicity(0, 9999))
    }
)
originalPoint40: BinaryAssociation = BinaryAssociation(
    name="originalPoint40",
    ends={
        Property(name="railDsl_Point41", type=railDsl_TrainRoutePoint, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_TrainRoutePoint", type=railDsl_Point, multiplicity=Multiplicity(0, 1))
    }
)
originalSegment42: BinaryAssociation = BinaryAssociation(
    name="originalSegment42",
    ends={
        Property(name="railDsl_Segment43", type=railDsl_TrainRouteSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="railDsl_TrainRouteSegment", type=railDsl_Segment, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_railDsl_Station_NamedElement = Generalization(general=NamedElement, specific=railDsl_Station)
gen_railDsl_Declaration_NamedElement = Generalization(general=NamedElement, specific=railDsl_Declaration)
gen_railDsl_LevelCrossing_SegmentObject = Generalization(general=SegmentObject, specific=railDsl_LevelCrossing)
gen_railDsl_Signal_SegmentObject = Generalization(general=SegmentObject, specific=railDsl_Signal)
gen_railDsl_Platform_SegmentObject = Generalization(general=SegmentObject, specific=railDsl_Platform)
gen_railDsl_Point_TrackObject = Generalization(general=TrackObject, specific=railDsl_Point)
gen_railDsl_TrackObject_Declaration = Generalization(general=Declaration, specific=railDsl_TrackObject)
gen_railDsl_TrackObject_RouteObject = Generalization(general=RouteObject, specific=railDsl_TrackObject)
gen_railDsl_Vertex_Declaration = Generalization(general=Declaration, specific=railDsl_Vertex)
gen_railDsl_Segment_TrackObject = Generalization(general=TrackObject, specific=railDsl_Segment)
gen_railDsl_SegmentObject_NamedElement = Generalization(general=NamedElement, specific=railDsl_SegmentObject)
gen_railDsl_SegmentObject_RouteObject = Generalization(general=RouteObject, specific=railDsl_SegmentObject)
gen_railDsl_Derailer_SegmentObject = Generalization(general=SegmentObject, specific=railDsl_Derailer)
gen_railDsl_Train_Declaration = Generalization(general=Declaration, specific=railDsl_Train)
gen_railDsl_TrainRoute_Declaration = Generalization(general=Declaration, specific=railDsl_TrainRoute)
gen_railDsl_Track_Declaration = Generalization(general=Declaration, specific=railDsl_Track)
gen_railDsl_TrainRoutePoint_TrainRouteObject = Generalization(general=TrainRouteObject, specific=railDsl_TrainRoutePoint)
gen_railDsl_TrainRouteSegment_TrainRouteObject = Generalization(general=TrainRouteObject, specific=railDsl_TrainRouteSegment)

# Domain Model
domain_model = DomainModel(
    name="railDsl",
    types={railDsl_Station, NamedElement, railDsl_Declaration, railDsl_LevelCrossing, railDsl_Signal, railDsl_Platform, railDsl_Point, railDsl_TrackObject, Declaration, RouteObject, railDsl_Vertex, railDsl_Segment, TrackObject, railDsl_SegmentObject, railDsl_SegmentPosition, railDsl_Derailer, SegmentObject, railDsl_Train, railDsl_TrainSegment, railDsl_RouteObject, railDsl_TrainRoute, railDsl_TrainRouteObject, railDsl_Track, railDsl_NamedElement, railDsl_TrainRoutePoint, TrainRouteObject, railDsl_TrainRouteSegment, Side, SpeedLimit, PointKind, VertexKind, Orientation, TrainRouteKind},
    associations={declarations0, distantFor10, segment11, inputs14, outputs16, start1, end2, objects5, position7, segments20, position21, position24, path27, elements19, startSignal28, endSignal31, protectionObjects34, conflictingRoutes38, originalPoint40, originalSegment42},
    generalizations={gen_railDsl_Station_NamedElement, gen_railDsl_Declaration_NamedElement, gen_railDsl_LevelCrossing_SegmentObject, gen_railDsl_Signal_SegmentObject, gen_railDsl_Platform_SegmentObject, gen_railDsl_Point_TrackObject, gen_railDsl_TrackObject_Declaration, gen_railDsl_TrackObject_RouteObject, gen_railDsl_Vertex_Declaration, gen_railDsl_Segment_TrackObject, gen_railDsl_SegmentObject_NamedElement, gen_railDsl_SegmentObject_RouteObject, gen_railDsl_Derailer_SegmentObject, gen_railDsl_Train_Declaration, gen_railDsl_TrainRoute_Declaration, gen_railDsl_Track_Declaration, gen_railDsl_TrainRoutePoint_TrainRouteObject, gen_railDsl_TrainRouteSegment_TrainRouteObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)