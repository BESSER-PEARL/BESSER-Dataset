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
KnownColor: Enumeration = Enumeration(
    name="KnownColor",
    literals={
            EnumerationLiteral(name="green"),
			EnumerationLiteral(name="navy"),
			EnumerationLiteral(name="blue"),
			EnumerationLiteral(name="maroon"),
			EnumerationLiteral(name="red"),
			EnumerationLiteral(name="orange"),
			EnumerationLiteral(name="yellow"),
			EnumerationLiteral(name="olive"),
			EnumerationLiteral(name="purple"),
			EnumerationLiteral(name="fuchsia"),
			EnumerationLiteral(name="white"),
			EnumerationLiteral(name="lime"),
			EnumerationLiteral(name="aqua"),
			EnumerationLiteral(name="teal"),
			EnumerationLiteral(name="black"),
			EnumerationLiteral(name="silver"),
			EnumerationLiteral(name="gray")
    }
)

AlignmentKind: Enumeration = Enumeration(
    name="AlignmentKind",
    literals={
            EnumerationLiteral(name="start"),
			EnumerationLiteral(name="end"),
			EnumerationLiteral(name="center")
    }
)

# Classes
dc_Point = Class(name="dc::Point")
dc_Dimension = Class(name="dc::Dimension")
dc_Bounds = Class(name="dc::Bounds")

# dc_Point class attributes and methods
dc_Point_x: Property = Property(name="x", type=StringType)
dc_Point_y: Property = Property(name="y", type=StringType)
dc_Point.attributes={dc_Point_y, dc_Point_x}

# dc_Dimension class attributes and methods
dc_Dimension_width: Property = Property(name="width", type=StringType)
dc_Dimension_height: Property = Property(name="height", type=StringType)
dc_Dimension_m_nonNegativeDimension: Method = Method(name="nonNegativeDimension", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dc_Dimension.attributes={dc_Dimension_height, dc_Dimension_width}
dc_Dimension.methods={dc_Dimension_m_nonNegativeDimension}

# dc_Bounds class attributes and methods
dc_Bounds_x: Property = Property(name="x", type=StringType)
dc_Bounds_y: Property = Property(name="y", type=StringType)
dc_Bounds_width: Property = Property(name="width", type=StringType)
dc_Bounds_height: Property = Property(name="height", type=StringType)
dc_Bounds_m_nonNegativeSize: Method = Method(name="nonNegativeSize", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dc_Bounds.attributes={dc_Bounds_x, dc_Bounds_width, dc_Bounds_y, dc_Bounds_height}
dc_Bounds.methods={dc_Bounds_m_nonNegativeSize}

# Domain Model
domain_model = DomainModel(
    name="dc",
    types={dc_Point, dc_Dimension, dc_Bounds, KnownColor, AlignmentKind},
    associations={},
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