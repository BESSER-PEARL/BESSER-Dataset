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

# Classes
trace_Any = Class(name="trace::Any", is_abstract=True)
trace_EObject = Class(name="trace::EObject")
trace_BoolAny = Class(name="trace::BoolAny")
Any = Class(name="Any")
trace_IntAny = Class(name="trace::IntAny")
trace_DecimalAny = Class(name="trace::DecimalAny")
trace_Trace = Class(name="trace::Trace")
trace_StringAny = Class(name="trace::StringAny")
trace_ObjectAny = Class(name="trace::ObjectAny")

# trace_Any class attributes and methods

# trace_EObject class attributes and methods

# trace_BoolAny class attributes and methods
trace_BoolAny_value: Property = Property(name="value", type=BooleanType)
trace_BoolAny.attributes={trace_BoolAny_value}

# Any class attributes and methods

# trace_IntAny class attributes and methods
trace_IntAny_value: Property = Property(name="value", type=StringType)
trace_IntAny.attributes={trace_IntAny_value}

# trace_DecimalAny class attributes and methods
trace_DecimalAny_value: Property = Property(name="value", type=StringType)
trace_DecimalAny.attributes={trace_DecimalAny_value}

# trace_Trace class attributes and methods
trace_Trace_name: Property = Property(name="name", type=StringType)
trace_Trace.attributes={trace_Trace_name}

# trace_StringAny class attributes and methods
trace_StringAny_value: Property = Property(name="value", type=StringType)
trace_StringAny.attributes={trace_StringAny_value}

# trace_ObjectAny class attributes and methods

# Relationships
sources0: BinaryAssociation = BinaryAssociation(
    name="sources0",
    ends={
        Property(name="trace_Any", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_Any, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="trace_EObject", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace2", type=trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
rules3: BinaryAssociation = BinaryAssociation(
    name="rules3",
    ends={
        Property(name="trace_EObject5", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace4", type=trace_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
value6: BinaryAssociation = BinaryAssociation(
    name="value6",
    ends={
        Property(name="trace_EObject7", type=trace_ObjectAny, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ObjectAny", type=trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_trace_BoolAny_Any = Generalization(general=Any, specific=trace_BoolAny)
gen_trace_IntAny_Any = Generalization(general=Any, specific=trace_IntAny)
gen_trace_DecimalAny_Any = Generalization(general=Any, specific=trace_DecimalAny)
gen_trace_StringAny_Any = Generalization(general=Any, specific=trace_StringAny)
gen_trace_ObjectAny_Any = Generalization(general=Any, specific=trace_ObjectAny)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Any, trace_EObject, trace_BoolAny, Any, trace_IntAny, trace_DecimalAny, trace_Trace, trace_StringAny, trace_ObjectAny},
    associations={sources0, target1, rules3, value6},
    generalizations={gen_trace_BoolAny_Any, gen_trace_IntAny_Any, gen_trace_DecimalAny_Any, gen_trace_StringAny_Any, gen_trace_ObjectAny_Any},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)