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
trace_ExecutionContext = Class(name="trace::ExecutionContext")
TraceElement = Class(name="TraceElement")
trace_ModuleElement = Class(name="trace::ModuleElement")
trace_Trace = Class(name="trace::Trace")
trace_ModelElement = Class(name="trace::ModelElement")
trace_Property = Class(name="trace::Property")
trace_TraceElement = Class(name="trace::TraceElement", is_abstract=True)

# trace_ExecutionContext class attributes and methods
trace_ExecutionContext_scriptId: Property = Property(name="scriptId", type=StringType)
trace_ExecutionContext_modelsIds: Property = Property(name="modelsIds", type=StringType)
trace_ExecutionContext.attributes={trace_ExecutionContext_scriptId, trace_ExecutionContext_modelsIds}

# TraceElement class attributes and methods

# trace_ModuleElement class attributes and methods
trace_ModuleElement_module_id: Property = Property(name="module_id", type=StringType)
trace_ModuleElement.attributes={trace_ModuleElement_module_id}

# trace_Trace class attributes and methods

# trace_ModelElement class attributes and methods
trace_ModelElement_element_id: Property = Property(name="element_id", type=StringType)
trace_ModelElement.attributes={trace_ModelElement_element_id}

# trace_Property class attributes and methods
trace_Property_name: Property = Property(name="name", type=StringType)
trace_Property.attributes={trace_Property_name}

# trace_TraceElement class attributes and methods
trace_TraceElement_id: Property = Property(name="id", type=StringType)
trace_TraceElement.attributes={trace_TraceElement_id}

# Relationships
for0: BinaryAssociation = BinaryAssociation(
    name="for0",
    ends={
        Property(name="ModuleElement", type=trace_ExecutionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="executionContexts", type=trace_ModuleElement, multiplicity=Multiplicity(0, 9999))
    }
)
contains1: BinaryAssociation = BinaryAssociation(
    name="contains1",
    ends={
        Property(name="Trace", type=trace_ExecutionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="executionContext", type=trace_Trace, multiplicity=Multiplicity(0, 9999))
    }
)
involves2: BinaryAssociation = BinaryAssociation(
    name="involves2",
    ends={
        Property(name="ModelElement", type=trace_ExecutionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="executionContext3", type=trace_ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
accesses15: BinaryAssociation = BinaryAssociation(
    name="accesses15",
    ends={
        Property(name="Property", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces16", type=trace_Property, multiplicity=Multiplicity(0, 9999))
    }
)
executionContext17: BinaryAssociation = BinaryAssociation(
    name="executionContext17",
    ends={
        Property(name="ExecutionContext18", type=trace_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="involves", type=trace_ExecutionContext, multiplicity=Multiplicity(0, 9999))
    }
)
traces19: BinaryAssociation = BinaryAssociation(
    name="traces19",
    ends={
        Property(name="Trace20", type=trace_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="reaches", type=trace_Trace, multiplicity=Multiplicity(0, 9999))
    }
)
owns21: BinaryAssociation = BinaryAssociation(
    name="owns21",
    ends={
        Property(name="Property22", type=trace_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="modelElement", type=trace_Property, multiplicity=Multiplicity(0, 9999))
    }
)
modelElement23: BinaryAssociation = BinaryAssociation(
    name="modelElement23",
    ends={
        Property(name="ModelElement24", type=trace_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="owns", type=trace_ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
traces25: BinaryAssociation = BinaryAssociation(
    name="traces25",
    ends={
        Property(name="Trace26", type=trace_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="accesses", type=trace_Trace, multiplicity=Multiplicity(0, 9999))
    }
)
executionContexts4: BinaryAssociation = BinaryAssociation(
    name="executionContexts4",
    ends={
        Property(name="ExecutionContext", type=trace_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="for", type=trace_ExecutionContext, multiplicity=Multiplicity(0, 9999))
    }
)
traces5: BinaryAssociation = BinaryAssociation(
    name="traces5",
    ends={
        Property(name="Trace6", type=trace_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="traces", type=trace_Trace, multiplicity=Multiplicity(0, 9999))
    }
)
executionContext7: BinaryAssociation = BinaryAssociation(
    name="executionContext7",
    ends={
        Property(name="ExecutionContext8", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="contains", type=trace_ExecutionContext, multiplicity=Multiplicity(0, 1))
    }
)
traces9: BinaryAssociation = BinaryAssociation(
    name="traces9",
    ends={
        Property(name="ModuleElement11", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces10", type=trace_ModuleElement, multiplicity=Multiplicity(1, 1))
    }
)
reaches12: BinaryAssociation = BinaryAssociation(
    name="reaches12",
    ends={
        Property(name="ModelElement14", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces13", type=trace_ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_trace_ExecutionContext_TraceElement = Generalization(general=TraceElement, specific=trace_ExecutionContext)
gen_trace_ModuleElement_TraceElement = Generalization(general=TraceElement, specific=trace_ModuleElement)
gen_trace_ModelElement_TraceElement = Generalization(general=TraceElement, specific=trace_ModelElement)
gen_trace_Property_TraceElement = Generalization(general=TraceElement, specific=trace_Property)
gen_trace_Trace_TraceElement = Generalization(general=TraceElement, specific=trace_Trace)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_ExecutionContext, TraceElement, trace_ModuleElement, trace_Trace, trace_ModelElement, trace_Property, trace_TraceElement},
    associations={for0, contains1, involves2, accesses15, executionContext17, traces19, owns21, modelElement23, traces25, executionContexts4, traces5, executionContext7, traces9, reaches12},
    generalizations={gen_trace_ExecutionContext_TraceElement, gen_trace_ModuleElement_TraceElement, gen_trace_ModelElement_TraceElement, gen_trace_Property_TraceElement, gen_trace_Trace_TraceElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)