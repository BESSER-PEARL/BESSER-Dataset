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
Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="IN")
    }
)

PortMemoryAnnotation: Enumeration = Enumeration(
    name="PortMemoryAnnotation",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="READ_ONLY"),
			EnumerationLiteral(name="WRITE_ONLY"),
			EnumerationLiteral(name="UNUSED")
    }
)

# Classes
pimm_Parameterizable = Class(name="pimm::Parameterizable", is_abstract=True)
PiMMVisitable = Class(name="PiMMVisitable")
pimm_ConfigInputPort = Class(name="pimm::ConfigInputPort")
pimm_AbstractVertex = Class(name="pimm::AbstractVertex", is_abstract=True)
Parameterizable = Class(name="Parameterizable")
pimm_DataInputPort = Class(name="pimm::DataInputPort")
pimm_AbstractActor = Class(name="pimm::AbstractActor", is_abstract=True)
AbstractVertex = Class(name="AbstractVertex")
pimm_Parameter = Class(name="pimm::Parameter")
pimm_DataOutputPort = Class(name="pimm::DataOutputPort")
pimm_ConfigOutputPort = Class(name="pimm::ConfigOutputPort")
pimm_PiGraph = Class(name="pimm::PiGraph")
AbstractActor = Class(name="AbstractActor")
DataPort = Class(name="DataPort")
pimm_Fifo = Class(name="pimm::Fifo")
pimm_Dependency = Class(name="pimm::Dependency")
pimm_Actor = Class(name="pimm::Actor")
ExecutableActor = Class(name="ExecutableActor")
pimm_Refinement = Class(name="pimm::Refinement")
pimm_Port = Class(name="pimm::Port", is_abstract=True)
Port = Class(name="Port")
DataOutputPort = Class(name="DataOutputPort")
ISetter = Class(name="ISetter")
InterfaceActor = Class(name="InterfaceActor")
pimm_Delay = Class(name="pimm::Delay")
pimm_InterfaceActor = Class(name="pimm::InterfaceActor")
pimm_DataInputInterface = Class(name="pimm::DataInputInterface")
pimm_Expression = Class(name="pimm::Expression")
pimm_DataOutputInterface = Class(name="pimm::DataOutputInterface")
pimm_ConfigInputInterface = Class(name="pimm::ConfigInputInterface")
Parameter_ = Class(name="Parameter")
pimm_ConfigOutputInterface = Class(name="pimm::ConfigOutputInterface")
pimm_ISetter = Class(name="pimm::ISetter", is_abstract=True)
pimm_DataPort = Class(name="pimm::DataPort", is_abstract=True)
pimm_HRefinement = Class(name="pimm::HRefinement")
Refinement = Class(name="Refinement")
pimm_FunctionPrototype = Class(name="pimm::FunctionPrototype")
pimm_FunctionParameter = Class(name="pimm::FunctionParameter")
pimm_visitor_PiMMVisitor = Class(name="pimm::visitor::PiMMVisitor", is_abstract=True)
pimm_BroadcastActor = Class(name="pimm::BroadcastActor")
pimm_JoinActor = Class(name="pimm::JoinActor")
pimm_ForkActor = Class(name="pimm::ForkActor")
pimm_RoundBufferActor = Class(name="pimm::RoundBufferActor")
pimm_ExecutableActor = Class(name="pimm::ExecutableActor", is_abstract=True)
pimm_visitor_PiMMVisitable = Class(name="pimm::visitor::PiMMVisitable", is_abstract=True)

# pimm_Parameterizable class attributes and methods
pimm_Parameterizable_m_getInputParameters: Method = Method(name="getInputParameters", parameters={}, type=StringType)
pimm_Parameterizable.methods={pimm_Parameterizable_m_getInputParameters}

# PiMMVisitable class attributes and methods

# pimm_ConfigInputPort class attributes and methods

# pimm_AbstractVertex class attributes and methods
pimm_AbstractVertex_name: Property = Property(name="name", type=StringType)
pimm_AbstractVertex.attributes={pimm_AbstractVertex_name}

# Parameterizable class attributes and methods

# pimm_DataInputPort class attributes and methods

# pimm_AbstractActor class attributes and methods
pimm_AbstractActor_m_getAllPorts: Method = Method(name="getAllPorts", parameters={}, type=StringType)
pimm_AbstractActor.methods={pimm_AbstractActor_m_getAllPorts}

# AbstractVertex class attributes and methods

# pimm_Parameter class attributes and methods
pimm_Parameter_configurationInterface: Property = Property(name="configurationInterface", type=BooleanType)
pimm_Parameter_m_isLocallyStatic: Method = Method(name="isLocallyStatic", parameters={}, type=BooleanType)
pimm_Parameter_m_isDependent: Method = Method(name="isDependent", parameters={}, type=BooleanType)
pimm_Parameter.attributes={pimm_Parameter_configurationInterface}
pimm_Parameter.methods={pimm_Parameter_m_isDependent, pimm_Parameter_m_isLocallyStatic}

# pimm_DataOutputPort class attributes and methods

# pimm_ConfigOutputPort class attributes and methods

# pimm_PiGraph class attributes and methods
pimm_PiGraph_m_getVerticesNames: Method = Method(name="getVerticesNames", parameters={}, type=StringType)
pimm_PiGraph_m_getParametersNames: Method = Method(name="getParametersNames", parameters={}, type=StringType)
pimm_PiGraph_m_getActors: Method = Method(name="getActors", parameters={}, type=StringType)
pimm_PiGraph_m_getAllParameters: Method = Method(name="getAllParameters", parameters={}, type=StringType)
pimm_PiGraph.methods={pimm_PiGraph_m_getAllParameters, pimm_PiGraph_m_getActors, pimm_PiGraph_m_getParametersNames, pimm_PiGraph_m_getVerticesNames}

# AbstractActor class attributes and methods

# DataPort class attributes and methods

# pimm_Fifo class attributes and methods
pimm_Fifo_id: Property = Property(name="id", type=StringType)
pimm_Fifo_type: Property = Property(name="type", type=StringType)
pimm_Fifo.attributes={pimm_Fifo_id, pimm_Fifo_type}

# pimm_Dependency class attributes and methods

# pimm_Actor class attributes and methods
pimm_Actor_configurationActor: Property = Property(name="configurationActor", type=BooleanType)
pimm_Actor_memoryScriptPath: Property = Property(name="memoryScriptPath", type=StringType)
pimm_Actor.attributes={pimm_Actor_configurationActor, pimm_Actor_memoryScriptPath}

# ExecutableActor class attributes and methods

# pimm_Refinement class attributes and methods
pimm_Refinement_fileName: Property = Property(name="fileName", type=StringType)
pimm_Refinement_filePath: Property = Property(name="filePath", type=StringType)
pimm_Refinement_m_getAbstractActor: Method = Method(name="getAbstractActor", parameters={}, type=AbstractActor)
pimm_Refinement.attributes={pimm_Refinement_fileName, pimm_Refinement_filePath}
pimm_Refinement.methods={pimm_Refinement_m_getAbstractActor}

# pimm_Port class attributes and methods
pimm_Port_name: Property = Property(name="name", type=StringType)
pimm_Port_kind: Property = Property(name="kind", type=StringType)
pimm_Port.attributes={pimm_Port_kind, pimm_Port_name}

# Port class attributes and methods

# DataOutputPort class attributes and methods

# ISetter class attributes and methods

# InterfaceActor class attributes and methods

# pimm_Delay class attributes and methods

# pimm_InterfaceActor class attributes and methods
pimm_InterfaceActor_kind: Property = Property(name="kind", type=StringType)
pimm_InterfaceActor.attributes={pimm_InterfaceActor_kind}

# pimm_DataInputInterface class attributes and methods

# pimm_Expression class attributes and methods
pimm_Expression_string: Property = Property(name="string", type=StringType)
pimm_Expression_m_evaluate: Method = Method(name="evaluate", parameters={}, type=StringType)
pimm_Expression.attributes={pimm_Expression_string}
pimm_Expression.methods={pimm_Expression_m_evaluate}

# pimm_DataOutputInterface class attributes and methods

# pimm_ConfigInputInterface class attributes and methods

# Parameter class attributes and methods

# pimm_ConfigOutputInterface class attributes and methods

# pimm_ISetter class attributes and methods
pimm_ISetter_m_getValue: Method = Method(name="getValue", parameters={}, type=IntegerType)
pimm_ISetter.methods={pimm_ISetter_m_getValue}

# pimm_DataPort class attributes and methods
pimm_DataPort_annotation: Property = Property(name="annotation", type=StringType)
pimm_DataPort.attributes={pimm_DataPort_annotation}

# pimm_HRefinement class attributes and methods

# Refinement class attributes and methods

# pimm_FunctionPrototype class attributes and methods
pimm_FunctionPrototype_name: Property = Property(name="name", type=StringType)
pimm_FunctionPrototype.attributes={pimm_FunctionPrototype_name}

# pimm_FunctionParameter class attributes and methods
pimm_FunctionParameter_name: Property = Property(name="name", type=StringType)
pimm_FunctionParameter_direction: Property = Property(name="direction", type=StringType)
pimm_FunctionParameter_type: Property = Property(name="type", type=StringType)
pimm_FunctionParameter_isConfigurationParameter: Property = Property(name="isConfigurationParameter", type=BooleanType)
pimm_FunctionParameter.attributes={pimm_FunctionParameter_isConfigurationParameter, pimm_FunctionParameter_type, pimm_FunctionParameter_name, pimm_FunctionParameter_direction}

# pimm_visitor_PiMMVisitor class attributes and methods
pimm_visitor_PiMMVisitor_m_visit: Method = Method(name="visit", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitDelay: Method = Method(name="visitDelay", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitDependency: Method = Method(name="visitDependency", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitAbstractActor: Method = Method(name="visitAbstractActor", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitAbstractVertex: Method = Method(name="visitAbstractVertex", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitActor: Method = Method(name="visitActor", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitConfigInputInterface: Method = Method(name="visitConfigInputInterface", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitConfigInputPort: Method = Method(name="visitConfigInputPort", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitConfigOutputInterface: Method = Method(name="visitConfigOutputInterface", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitConfigOutputPort: Method = Method(name="visitConfigOutputPort", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitDataInputInterface: Method = Method(name="visitDataInputInterface", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitDataInputPort: Method = Method(name="visitDataInputPort", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitDataOutputInterface: Method = Method(name="visitDataOutputInterface", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitDataOutputPort: Method = Method(name="visitDataOutputPort", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitDataPort: Method = Method(name="visitDataPort", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitExpression: Method = Method(name="visitExpression", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitFifo: Method = Method(name="visitFifo", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitInterfaceActor: Method = Method(name="visitInterfaceActor", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitISetter: Method = Method(name="visitISetter", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitParameter: Method = Method(name="visitParameter", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitParameterizable: Method = Method(name="visitParameterizable", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitPiGraph: Method = Method(name="visitPiGraph", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitPort: Method = Method(name="visitPort", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitRefinement: Method = Method(name="visitRefinement", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitFunctionParameter: Method = Method(name="visitFunctionParameter", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitFunctionPrototype: Method = Method(name="visitFunctionPrototype", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitHRefinement: Method = Method(name="visitHRefinement", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitBroadcastActor: Method = Method(name="visitBroadcastActor", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitJoinActor: Method = Method(name="visitJoinActor", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitForkActor: Method = Method(name="visitForkActor", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitRoundBufferActor: Method = Method(name="visitRoundBufferActor", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor_m_visitExecutableActor: Method = Method(name="visitExecutableActor", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitor.methods={pimm_visitor_PiMMVisitor_m_visitForkActor, pimm_visitor_PiMMVisitor_m_visitConfigInputInterface, pimm_visitor_PiMMVisitor_m_visitInterfaceActor, pimm_visitor_PiMMVisitor_m_visitRoundBufferActor, pimm_visitor_PiMMVisitor_m_visitAbstractActor, pimm_visitor_PiMMVisitor_m_visitFunctionParameter, pimm_visitor_PiMMVisitor_m_visitBroadcastActor, pimm_visitor_PiMMVisitor_m_visitExecutableActor, pimm_visitor_PiMMVisitor_m_visitISetter, pimm_visitor_PiMMVisitor_m_visitExpression, pimm_visitor_PiMMVisitor_m_visitActor, pimm_visitor_PiMMVisitor_m_visitDataInputPort, pimm_visitor_PiMMVisitor_m_visitConfigInputPort, pimm_visitor_PiMMVisitor_m_visitDependency, pimm_visitor_PiMMVisitor_m_visitFunctionPrototype, pimm_visitor_PiMMVisitor_m_visitConfigOutputInterface, pimm_visitor_PiMMVisitor_m_visitHRefinement, pimm_visitor_PiMMVisitor_m_visit, pimm_visitor_PiMMVisitor_m_visitDataPort, pimm_visitor_PiMMVisitor_m_visitJoinActor, pimm_visitor_PiMMVisitor_m_visitFifo, pimm_visitor_PiMMVisitor_m_visitDataOutputInterface, pimm_visitor_PiMMVisitor_m_visitParameterizable, pimm_visitor_PiMMVisitor_m_visitDataOutputPort, pimm_visitor_PiMMVisitor_m_visitConfigOutputPort, pimm_visitor_PiMMVisitor_m_visitDataInputInterface, pimm_visitor_PiMMVisitor_m_visitPort, pimm_visitor_PiMMVisitor_m_visitRefinement, pimm_visitor_PiMMVisitor_m_visitDelay, pimm_visitor_PiMMVisitor_m_visitAbstractVertex, pimm_visitor_PiMMVisitor_m_visitParameter, pimm_visitor_PiMMVisitor_m_visitPiGraph}

# pimm_BroadcastActor class attributes and methods

# pimm_JoinActor class attributes and methods

# pimm_ForkActor class attributes and methods

# pimm_RoundBufferActor class attributes and methods

# pimm_ExecutableActor class attributes and methods

# pimm_visitor_PiMMVisitable class attributes and methods
pimm_visitor_PiMMVisitable_m_accept: Method = Method(name="accept", parameters={Parameter(name='subject')})
pimm_visitor_PiMMVisitable.methods={pimm_visitor_PiMMVisitable_m_accept}

# Relationships
configInputPorts0: BinaryAssociation = BinaryAssociation(
    name="configInputPorts0",
    ends={
        Property(name="pimm_ConfigInputPort", type=pimm_Parameterizable, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_Parameterizable", type=pimm_ConfigInputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataInputPorts1: BinaryAssociation = BinaryAssociation(
    name="dataInputPorts1",
    ends={
        Property(name="pimm_DataInputPort", type=pimm_AbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_AbstractActor", type=pimm_DataInputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fifos8: BinaryAssociation = BinaryAssociation(
    name="fifos8",
    ends={
        Property(name="pimm_Fifo", type=pimm_PiGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_PiGraph9", type=pimm_Fifo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataOutputPorts2: BinaryAssociation = BinaryAssociation(
    name="dataOutputPorts2",
    ends={
        Property(name="pimm_DataOutputPort", type=pimm_AbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_AbstractActor3", type=pimm_DataOutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configOutputPorts4: BinaryAssociation = BinaryAssociation(
    name="configOutputPorts4",
    ends={
        Property(name="pimm_ConfigOutputPort", type=pimm_AbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_AbstractActor5", type=pimm_ConfigOutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertices6: BinaryAssociation = BinaryAssociation(
    name="vertices6",
    ends={
        Property(name="pimm_AbstractActor7", type=pimm_PiGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_PiGraph", type=pimm_AbstractActor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters10: BinaryAssociation = BinaryAssociation(
    name="parameters10",
    ends={
        Property(name="pimm_Parameter", type=pimm_PiGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_PiGraph11", type=pimm_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies12: BinaryAssociation = BinaryAssociation(
    name="dependencies12",
    ends={
        Property(name="pimm_Dependency", type=pimm_PiGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_PiGraph13", type=pimm_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinement14: BinaryAssociation = BinaryAssociation(
    name="refinement14",
    ends={
        Property(name="pimm_Refinement", type=pimm_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_Actor", type=pimm_Refinement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
incomingFifo15: BinaryAssociation = BinaryAssociation(
    name="incomingFifo15",
    ends={
        Property(name="Fifo", type=pimm_DataInputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="targetPort", type=pimm_Fifo, multiplicity=Multiplicity(0, 1))
    }
)
outgoingFifo16: BinaryAssociation = BinaryAssociation(
    name="outgoingFifo16",
    ends={
        Property(name="Fifo17", type=pimm_DataOutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcePort", type=pimm_Fifo, multiplicity=Multiplicity(0, 1))
    }
)
incomingDependency18: BinaryAssociation = BinaryAssociation(
    name="incomingDependency18",
    ends={
        Property(name="Dependency", type=pimm_ConfigInputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="getter", type=pimm_Dependency, multiplicity=Multiplicity(0, 1))
    }
)
sourcePort19: BinaryAssociation = BinaryAssociation(
    name="sourcePort19",
    ends={
        Property(name="DataOutputPort", type=pimm_Fifo, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingFifo", type=pimm_DataOutputPort, multiplicity=Multiplicity(1, 1))
    }
)
targetPort20: BinaryAssociation = BinaryAssociation(
    name="targetPort20",
    ends={
        Property(name="DataInputPort", type=pimm_Fifo, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingFifo", type=pimm_DataInputPort, multiplicity=Multiplicity(1, 1))
    }
)
delay21: BinaryAssociation = BinaryAssociation(
    name="delay21",
    ends={
        Property(name="pimm_Delay", type=pimm_Fifo, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_Fifo22", type=pimm_Delay, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphPort23: BinaryAssociation = BinaryAssociation(
    name="graphPort23",
    ends={
        Property(name="pimm_Port", type=pimm_InterfaceActor, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_InterfaceActor", type=pimm_Port, multiplicity=Multiplicity(1, 1))
    }
)
expression27: BinaryAssociation = BinaryAssociation(
    name="expression27",
    ends={
        Property(name="pimm_Expression", type=pimm_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_Parameter28", type=pimm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
graphPort24: BinaryAssociation = BinaryAssociation(
    name="graphPort24",
    ends={
        Property(name="pimm_ConfigInputPort26", type=pimm_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_Parameter25", type=pimm_ConfigInputPort, multiplicity=Multiplicity(1, 1))
    }
)
setter29: BinaryAssociation = BinaryAssociation(
    name="setter29",
    ends={
        Property(name="ISetter", type=pimm_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingDependencies", type=pimm_ISetter, multiplicity=Multiplicity(1, 1))
    }
)
getter30: BinaryAssociation = BinaryAssociation(
    name="getter30",
    ends={
        Property(name="ConfigInputPort", type=pimm_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingDependency", type=pimm_ConfigInputPort, multiplicity=Multiplicity(1, 1))
    }
)
outgoingDependencies31: BinaryAssociation = BinaryAssociation(
    name="outgoingDependencies31",
    ends={
        Property(name="Dependency32", type=pimm_ISetter, multiplicity=Multiplicity(1, 1)),
        Property(name="setter", type=pimm_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
expression33: BinaryAssociation = BinaryAssociation(
    name="expression33",
    ends={
        Property(name="pimm_Expression35", type=pimm_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_Delay34", type=pimm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loopPrototype36: BinaryAssociation = BinaryAssociation(
    name="loopPrototype36",
    ends={
        Property(name="pimm_FunctionPrototype", type=pimm_HRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_HRefinement", type=pimm_FunctionPrototype, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initPrototype37: BinaryAssociation = BinaryAssociation(
    name="initPrototype37",
    ends={
        Property(name="pimm_FunctionPrototype39", type=pimm_HRefinement, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_HRefinement38", type=pimm_FunctionPrototype, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters40: BinaryAssociation = BinaryAssociation(
    name="parameters40",
    ends={
        Property(name="pimm_FunctionParameter", type=pimm_FunctionPrototype, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_FunctionPrototype41", type=pimm_FunctionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression42: BinaryAssociation = BinaryAssociation(
    name="expression42",
    ends={
        Property(name="pimm_Expression43", type=pimm_DataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="pimm_DataPort", type=pimm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_pimm_Parameterizable_PiMMVisitable = Generalization(general=PiMMVisitable, specific=pimm_Parameterizable)
gen_pimm_AbstractVertex_Parameterizable = Generalization(general=Parameterizable, specific=pimm_AbstractVertex)
gen_pimm_AbstractActor_AbstractVertex = Generalization(general=AbstractVertex, specific=pimm_AbstractActor)
gen_pimm_PiGraph_AbstractActor = Generalization(general=AbstractActor, specific=pimm_PiGraph)
gen_pimm_DataInputPort_DataPort = Generalization(general=DataPort, specific=pimm_DataInputPort)
gen_pimm_Actor_ExecutableActor = Generalization(general=ExecutableActor, specific=pimm_Actor)
gen_pimm_Port_PiMMVisitable = Generalization(general=PiMMVisitable, specific=pimm_Port)
gen_pimm_DataOutputPort_DataPort = Generalization(general=DataPort, specific=pimm_DataOutputPort)
gen_pimm_ConfigInputPort_Port = Generalization(general=Port, specific=pimm_ConfigInputPort)
gen_pimm_ConfigOutputPort_DataOutputPort = Generalization(general=DataOutputPort, specific=pimm_ConfigOutputPort)
gen_pimm_ConfigOutputPort_ISetter = Generalization(general=ISetter, specific=pimm_ConfigOutputPort)
gen_pimm_Fifo_PiMMVisitable = Generalization(general=PiMMVisitable, specific=pimm_Fifo)
gen_pimm_DataInputInterface_InterfaceActor = Generalization(general=InterfaceActor, specific=pimm_DataInputInterface)
gen_pimm_InterfaceActor_AbstractActor = Generalization(general=AbstractActor, specific=pimm_InterfaceActor)
gen_pimm_DataOutputInterface_InterfaceActor = Generalization(general=InterfaceActor, specific=pimm_DataOutputInterface)
gen_pimm_ConfigInputInterface_Parameter = Generalization(general=Parameter_, specific=pimm_ConfigInputInterface)
gen_pimm_ConfigOutputInterface_InterfaceActor = Generalization(general=InterfaceActor, specific=pimm_ConfigOutputInterface)
gen_pimm_Refinement_PiMMVisitable = Generalization(general=PiMMVisitable, specific=pimm_Refinement)
gen_pimm_Parameter_AbstractVertex = Generalization(general=AbstractVertex, specific=pimm_Parameter)
gen_pimm_Parameter_ISetter = Generalization(general=ISetter, specific=pimm_Parameter)
gen_pimm_Dependency_PiMMVisitable = Generalization(general=PiMMVisitable, specific=pimm_Dependency)
gen_pimm_Delay_Parameterizable = Generalization(general=Parameterizable, specific=pimm_Delay)
gen_pimm_Expression_PiMMVisitable = Generalization(general=PiMMVisitable, specific=pimm_Expression)
gen_pimm_HRefinement_Refinement = Generalization(general=Refinement, specific=pimm_HRefinement)
gen_pimm_FunctionPrototype_PiMMVisitable = Generalization(general=PiMMVisitable, specific=pimm_FunctionPrototype)
gen_pimm_FunctionParameter_PiMMVisitable = Generalization(general=PiMMVisitable, specific=pimm_FunctionParameter)
gen_pimm_DataPort_Port = Generalization(general=Port, specific=pimm_DataPort)
gen_pimm_BroadcastActor_ExecutableActor = Generalization(general=ExecutableActor, specific=pimm_BroadcastActor)
gen_pimm_JoinActor_ExecutableActor = Generalization(general=ExecutableActor, specific=pimm_JoinActor)
gen_pimm_ForkActor_ExecutableActor = Generalization(general=ExecutableActor, specific=pimm_ForkActor)
gen_pimm_RoundBufferActor_ExecutableActor = Generalization(general=ExecutableActor, specific=pimm_RoundBufferActor)
gen_pimm_ExecutableActor_AbstractActor = Generalization(general=AbstractActor, specific=pimm_ExecutableActor)

# Domain Model
domain_model = DomainModel(
    name="pimm",
    types={pimm_Parameterizable, PiMMVisitable, pimm_ConfigInputPort, pimm_AbstractVertex, Parameterizable, pimm_DataInputPort, pimm_AbstractActor, AbstractVertex, pimm_Parameter, pimm_DataOutputPort, pimm_ConfigOutputPort, pimm_PiGraph, AbstractActor, DataPort, pimm_Fifo, pimm_Dependency, pimm_Actor, ExecutableActor, pimm_Refinement, pimm_Port, Port, DataOutputPort, ISetter, InterfaceActor, pimm_Delay, pimm_InterfaceActor, pimm_DataInputInterface, pimm_Expression, pimm_DataOutputInterface, pimm_ConfigInputInterface, Parameter_, pimm_ConfigOutputInterface, pimm_ISetter, pimm_DataPort, pimm_HRefinement, Refinement, pimm_FunctionPrototype, pimm_FunctionParameter, pimm_visitor_PiMMVisitor, pimm_BroadcastActor, pimm_JoinActor, pimm_ForkActor, pimm_RoundBufferActor, pimm_ExecutableActor, pimm_visitor_PiMMVisitable, Direction, PortMemoryAnnotation},
    associations={configInputPorts0, dataInputPorts1, fifos8, dataOutputPorts2, configOutputPorts4, vertices6, parameters10, dependencies12, refinement14, incomingFifo15, outgoingFifo16, incomingDependency18, sourcePort19, targetPort20, delay21, graphPort23, expression27, graphPort24, setter29, getter30, outgoingDependencies31, expression33, loopPrototype36, initPrototype37, parameters40, expression42},
    generalizations={gen_pimm_Parameterizable_PiMMVisitable, gen_pimm_AbstractVertex_Parameterizable, gen_pimm_AbstractActor_AbstractVertex, gen_pimm_PiGraph_AbstractActor, gen_pimm_DataInputPort_DataPort, gen_pimm_Actor_ExecutableActor, gen_pimm_Port_PiMMVisitable, gen_pimm_DataOutputPort_DataPort, gen_pimm_ConfigInputPort_Port, gen_pimm_ConfigOutputPort_DataOutputPort, gen_pimm_ConfigOutputPort_ISetter, gen_pimm_Fifo_PiMMVisitable, gen_pimm_DataInputInterface_InterfaceActor, gen_pimm_InterfaceActor_AbstractActor, gen_pimm_DataOutputInterface_InterfaceActor, gen_pimm_ConfigInputInterface_Parameter, gen_pimm_ConfigOutputInterface_InterfaceActor, gen_pimm_Refinement_PiMMVisitable, gen_pimm_Parameter_AbstractVertex, gen_pimm_Parameter_ISetter, gen_pimm_Dependency_PiMMVisitable, gen_pimm_Delay_Parameterizable, gen_pimm_Expression_PiMMVisitable, gen_pimm_HRefinement_Refinement, gen_pimm_FunctionPrototype_PiMMVisitable, gen_pimm_FunctionParameter_PiMMVisitable, gen_pimm_DataPort_Port, gen_pimm_BroadcastActor_ExecutableActor, gen_pimm_JoinActor_ExecutableActor, gen_pimm_ForkActor_ExecutableActor, gen_pimm_RoundBufferActor_ExecutableActor, gen_pimm_ExecutableActor_AbstractActor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)