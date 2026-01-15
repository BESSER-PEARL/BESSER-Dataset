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
TraceState: Enumeration = Enumeration(
    name="TraceState",
    literals={
            EnumerationLiteral(name="USED"),
			EnumerationLiteral(name="UNUSED")
    }
)

# Classes
viewmodeltrace_JavaObjectMatchArgument = Class(name="viewmodeltrace::JavaObjectMatchArgument")
viewmodeltrace_ViewModelTrace = Class(name="viewmodeltrace::ViewModelTrace")
viewmodeltrace_LogicModel = Class(name="viewmodeltrace::LogicModel")
viewmodeltrace_Trace = Class(name="viewmodeltrace::Trace", is_abstract=True)
viewmodeltrace_MatchArgumentTuple = Class(name="viewmodeltrace::MatchArgumentTuple")
viewmodeltrace_MatchArgument = Class(name="viewmodeltrace::MatchArgument", is_abstract=True)
viewmodeltrace_EObjectMatchArgument = Class(name="viewmodeltrace::EObjectMatchArgument")
MatchArgument = Class(name="MatchArgument")
viewmodeltrace_EObject = Class(name="viewmodeltrace::EObject")
viewmodeltrace_VariableInstantiationTrace = Class(name="viewmodeltrace::VariableInstantiationTrace")
Trace = Class(name="Trace")
viewmodeltrace_StringVariablePair = Class(name="viewmodeltrace::StringVariablePair")
viewmodeltrace_Variable = Class(name="viewmodeltrace::Variable")
viewmodeltrace_ConstraintTrace = Class(name="viewmodeltrace::ConstraintTrace")
viewmodeltrace_Constraint = Class(name="viewmodeltrace::Constraint")

# viewmodeltrace_JavaObjectMatchArgument class attributes and methods
viewmodeltrace_JavaObjectMatchArgument_value: Property = Property(name="value", type=StringType)
viewmodeltrace_JavaObjectMatchArgument.attributes={viewmodeltrace_JavaObjectMatchArgument_value}

# viewmodeltrace_ViewModelTrace class attributes and methods
viewmodeltrace_ViewModelTrace_traceModelId: Property = Property(name="traceModelId", type=StringType)
viewmodeltrace_ViewModelTrace.attributes={viewmodeltrace_ViewModelTrace_traceModelId}

# viewmodeltrace_LogicModel class attributes and methods

# viewmodeltrace_Trace class attributes and methods
viewmodeltrace_Trace_traceName: Property = Property(name="traceName", type=StringType)
viewmodeltrace_Trace_state: Property = Property(name="state", type=StringType)
viewmodeltrace_Trace.attributes={viewmodeltrace_Trace_traceName, viewmodeltrace_Trace_state}

# viewmodeltrace_MatchArgumentTuple class attributes and methods

# viewmodeltrace_MatchArgument class attributes and methods
viewmodeltrace_MatchArgument_parameterName: Property = Property(name="parameterName", type=StringType)
viewmodeltrace_MatchArgument.attributes={viewmodeltrace_MatchArgument_parameterName}

# viewmodeltrace_EObjectMatchArgument class attributes and methods

# MatchArgument class attributes and methods

# viewmodeltrace_EObject class attributes and methods

# viewmodeltrace_VariableInstantiationTrace class attributes and methods

# Trace class attributes and methods

# viewmodeltrace_StringVariablePair class attributes and methods
viewmodeltrace_StringVariablePair_key: Property = Property(name="key", type=StringType)
viewmodeltrace_StringVariablePair.attributes={viewmodeltrace_StringVariablePair_key}

# viewmodeltrace_Variable class attributes and methods

# viewmodeltrace_ConstraintTrace class attributes and methods

# viewmodeltrace_Constraint class attributes and methods

# Relationships
logicModel0: BinaryAssociation = BinaryAssociation(
    name="logicModel0",
    ends={
        Property(name="viewmodeltrace_LogicModel", type=viewmodeltrace_ViewModelTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="viewmodeltrace_ViewModelTrace", type=viewmodeltrace_LogicModel, multiplicity=Multiplicity(0, 1))
    }
)
traces1: BinaryAssociation = BinaryAssociation(
    name="traces1",
    ends={
        Property(name="viewmodeltrace_Trace", type=viewmodeltrace_ViewModelTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="viewmodeltrace_ViewModelTrace2", type=viewmodeltrace_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="viewmodeltrace_MatchArgument", type=viewmodeltrace_MatchArgumentTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="viewmodeltrace_MatchArgumentTuple", type=viewmodeltrace_MatchArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value4: BinaryAssociation = BinaryAssociation(
    name="value4",
    ends={
        Property(name="viewmodeltrace_EObject", type=viewmodeltrace_EObjectMatchArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="viewmodeltrace_EObjectMatchArgument", type=viewmodeltrace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
argumentTuple5: BinaryAssociation = BinaryAssociation(
    name="argumentTuple5",
    ends={
        Property(name="viewmodeltrace_MatchArgumentTuple7", type=viewmodeltrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="viewmodeltrace_Trace6", type=viewmodeltrace_MatchArgumentTuple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables8: BinaryAssociation = BinaryAssociation(
    name="variables8",
    ends={
        Property(name="viewmodeltrace_StringVariablePair", type=viewmodeltrace_VariableInstantiationTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="viewmodeltrace_VariableInstantiationTrace", type=viewmodeltrace_StringVariablePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value9: BinaryAssociation = BinaryAssociation(
    name="value9",
    ends={
        Property(name="viewmodeltrace_Variable", type=viewmodeltrace_StringVariablePair, multiplicity=Multiplicity(1, 1)),
        Property(name="viewmodeltrace_StringVariablePair10", type=viewmodeltrace_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariables11: BinaryAssociation = BinaryAssociation(
    name="localVariables11",
    ends={
        Property(name="viewmodeltrace_Variable12", type=viewmodeltrace_ConstraintTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="viewmodeltrace_ConstraintTrace", type=viewmodeltrace_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints13: BinaryAssociation = BinaryAssociation(
    name="constraints13",
    ends={
        Property(name="viewmodeltrace_Constraint", type=viewmodeltrace_ConstraintTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="viewmodeltrace_ConstraintTrace14", type=viewmodeltrace_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_viewmodeltrace_JavaObjectMatchArgument_MatchArgument = Generalization(general=MatchArgument, specific=viewmodeltrace_JavaObjectMatchArgument)
gen_viewmodeltrace_EObjectMatchArgument_MatchArgument = Generalization(general=MatchArgument, specific=viewmodeltrace_EObjectMatchArgument)
gen_viewmodeltrace_VariableInstantiationTrace_Trace = Generalization(general=Trace, specific=viewmodeltrace_VariableInstantiationTrace)
gen_viewmodeltrace_ConstraintTrace_Trace = Generalization(general=Trace, specific=viewmodeltrace_ConstraintTrace)

# Domain Model
domain_model = DomainModel(
    name="viewmodeltrace",
    types={viewmodeltrace_JavaObjectMatchArgument, viewmodeltrace_ViewModelTrace, viewmodeltrace_LogicModel, viewmodeltrace_Trace, viewmodeltrace_MatchArgumentTuple, viewmodeltrace_MatchArgument, viewmodeltrace_EObjectMatchArgument, MatchArgument, viewmodeltrace_EObject, viewmodeltrace_VariableInstantiationTrace, Trace, viewmodeltrace_StringVariablePair, viewmodeltrace_Variable, viewmodeltrace_ConstraintTrace, viewmodeltrace_Constraint, TraceState},
    associations={logicModel0, traces1, elements3, value4, argumentTuple5, variables8, value9, localVariables11, constraints13},
    generalizations={gen_viewmodeltrace_JavaObjectMatchArgument_MatchArgument, gen_viewmodeltrace_EObjectMatchArgument_MatchArgument, gen_viewmodeltrace_VariableInstantiationTrace_Trace, gen_viewmodeltrace_ConstraintTrace_Trace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)