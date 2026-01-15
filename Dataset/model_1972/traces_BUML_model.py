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
traces_EObject = Class(name="traces::EObject")
traces_TraceSet = Class(name="traces::TraceSet")
traces_Trace = Class(name="traces::Trace")

# traces_EObject class attributes and methods

# traces_TraceSet class attributes and methods

# traces_Trace class attributes and methods
traces_Trace_rule: Property = Property(name="rule", type=StringType)
traces_Trace.attributes={traces_Trace_rule}

# Relationships
fromDomainElement1: BinaryAssociation = BinaryAssociation(
    name="fromDomainElement1",
    ends={
        Property(name="traces_EObject", type=traces_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_Trace2", type=traces_EObject, multiplicity=Multiplicity(1, 1))
    }
)
toAnalyzableElement3: BinaryAssociation = BinaryAssociation(
    name="toAnalyzableElement3",
    ends={
        Property(name="traces_EObject5", type=traces_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_Trace4", type=traces_EObject, multiplicity=Multiplicity(1, 1))
    }
)
traces0: BinaryAssociation = BinaryAssociation(
    name="traces0",
    ends={
        Property(name="traces_Trace", type=traces_TraceSet, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_TraceSet", type=traces_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="traces",
    types={traces_EObject, traces_TraceSet, traces_Trace},
    associations={fromDomainElement1, toAnalyzableElement3, traces0},
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