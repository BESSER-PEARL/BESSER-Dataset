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
FunctionDomain: Enumeration = Enumeration(
    name="FunctionDomain",
    literals={
            EnumerationLiteral(name="time"),
			EnumerationLiteral(name="space"),
			EnumerationLiteral(name="form")
    }
)

# Classes
syswbeff106_Function = Class(name="syswbeff106::Function")
SequenceNode = Class(name="SequenceNode")
ProcessNode = Class(name="ProcessNode")
syswbeff106_InputPort = Class(name="syswbeff106::InputPort")
syswbeff106_Description = Class(name="syswbeff106::Description")
syswbeff106_Sequence = Class(name="syswbeff106::Sequence", is_abstract=True)
syswbeff106_Flow = Class(name="syswbeff106::Flow")
syswbeff106_OutputPort = Class(name="syswbeff106::OutputPort")
syswbeff106_Token = Class(name="syswbeff106::Token")
syswbeff106_FunctionProperty = Class(name="syswbeff106::FunctionProperty")
syswbeff106_Component = Class(name="syswbeff106::Component")
syswbeff106_SequenceNode = Class(name="syswbeff106::SequenceNode", is_abstract=True)
syswbeff106_Start = Class(name="syswbeff106::Start")
syswbeff106_And = Class(name="syswbeff106::And")
Sequence = Class(name="Sequence")
syswbeff106_Or = Class(name="syswbeff106::Or")
syswbeff106_Final = Class(name="syswbeff106::Final")
syswbeff106_Loop = Class(name="syswbeff106::Loop")
Port = Class(name="Port")
syswbeff106_Port = Class(name="syswbeff106::Port", is_abstract=True)
syswbeff106_ProcessNode = Class(name="syswbeff106::ProcessNode", is_abstract=True)
syswbeff106_Item = Class(name="syswbeff106::Item")
syswbeff106_LoopExit = Class(name="syswbeff106::LoopExit")
syswbeff106_Iteration = Class(name="syswbeff106::Iteration")
syswbeff106_RelatedTo = Class(name="syswbeff106::RelatedTo")
syswbeff106_Thing = Class(name="syswbeff106::Thing")
syswbeff106_System = Class(name="syswbeff106::System")
syswbeff106_Thoughts = Class(name="syswbeff106::Thoughts")
syswbeff106_PatternCatalog = Class(name="syswbeff106::PatternCatalog")
syswbeff106_Workbench = Class(name="syswbeff106::Workbench")

# syswbeff106_Function class attributes and methods
syswbeff106_Function_domain: Property = Property(name="domain", type=StringType)
syswbeff106_Function.attributes={syswbeff106_Function_domain}

# SequenceNode class attributes and methods

# ProcessNode class attributes and methods

# syswbeff106_InputPort class attributes and methods

# syswbeff106_Description class attributes and methods
syswbeff106_Description_content: Property = Property(name="content", type=StringType)
syswbeff106_Description.attributes={syswbeff106_Description_content}

# syswbeff106_Sequence class attributes and methods

# syswbeff106_Flow class attributes and methods

# syswbeff106_OutputPort class attributes and methods

# syswbeff106_Token class attributes and methods

# syswbeff106_FunctionProperty class attributes and methods
syswbeff106_FunctionProperty_description: Property = Property(name="description", type=StringType)
syswbeff106_FunctionProperty.attributes={syswbeff106_FunctionProperty_description}

# syswbeff106_Component class attributes and methods
syswbeff106_Component_name: Property = Property(name="name", type=StringType)
syswbeff106_Component.attributes={syswbeff106_Component_name}

# syswbeff106_SequenceNode class attributes and methods
syswbeff106_SequenceNode_name: Property = Property(name="name", type=StringType)
syswbeff106_SequenceNode_tMin: Property = Property(name="tMin", type=IntegerType)
syswbeff106_SequenceNode_tMax: Property = Property(name="tMax", type=IntegerType)
syswbeff106_SequenceNode.attributes={syswbeff106_SequenceNode_tMin, syswbeff106_SequenceNode_tMax, syswbeff106_SequenceNode_name}

# syswbeff106_Start class attributes and methods

# syswbeff106_And class attributes and methods

# Sequence class attributes and methods

# syswbeff106_Or class attributes and methods

# syswbeff106_Final class attributes and methods

# syswbeff106_Loop class attributes and methods

# Port class attributes and methods

# syswbeff106_Port class attributes and methods
syswbeff106_Port_id: Property = Property(name="id", type=StringType)
syswbeff106_Port.attributes={syswbeff106_Port_id}

# syswbeff106_ProcessNode class attributes and methods
syswbeff106_ProcessNode_label: Property = Property(name="label", type=StringType)
syswbeff106_ProcessNode.attributes={syswbeff106_ProcessNode_label}

# syswbeff106_Item class attributes and methods
syswbeff106_Item_name: Property = Property(name="name", type=StringType)
syswbeff106_Item.attributes={syswbeff106_Item_name}

# syswbeff106_LoopExit class attributes and methods

# syswbeff106_Iteration class attributes and methods

# syswbeff106_RelatedTo class attributes and methods
syswbeff106_RelatedTo_since: Property = Property(name="since", type=StringType)
syswbeff106_RelatedTo.attributes={syswbeff106_RelatedTo_since}

# syswbeff106_Thing class attributes and methods
syswbeff106_Thing_id: Property = Property(name="id", type=IntegerType)
syswbeff106_Thing.attributes={syswbeff106_Thing_id}

# syswbeff106_System class attributes and methods

# syswbeff106_Thoughts class attributes and methods

# syswbeff106_PatternCatalog class attributes and methods
syswbeff106_PatternCatalog_id: Property = Property(name="id", type=StringType)
syswbeff106_PatternCatalog.attributes={syswbeff106_PatternCatalog_id}

# syswbeff106_Workbench class attributes and methods
syswbeff106_Workbench_aprop: Property = Property(name="aprop", type=StringType)
syswbeff106_Workbench.attributes={syswbeff106_Workbench_aprop}

# Relationships
inputPorts8: BinaryAssociation = BinaryAssociation(
    name="inputPorts8",
    ends={
        Property(name="syswbeff106_InputPort", type=syswbeff106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Function9", type=syswbeff106_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions10: BinaryAssociation = BinaryAssociation(
    name="descriptions10",
    ends={
        Property(name="syswbeff106_Description", type=syswbeff106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Function11", type=syswbeff106_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="syswbeff106_Function", type=syswbeff106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Function0", type=syswbeff106_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="syswbeff106_Sequence", type=syswbeff106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Function3", type=syswbeff106_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flows4: BinaryAssociation = BinaryAssociation(
    name="flows4",
    ends={
        Property(name="syswbeff106_Flow", type=syswbeff106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Function5", type=syswbeff106_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts6: BinaryAssociation = BinaryAssociation(
    name="outputPorts6",
    ends={
        Property(name="syswbeff106_OutputPort", type=syswbeff106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Function7", type=syswbeff106_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens12: BinaryAssociation = BinaryAssociation(
    name="tokens12",
    ends={
        Property(name="syswbeff106_Token", type=syswbeff106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Function13", type=syswbeff106_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property14: BinaryAssociation = BinaryAssociation(
    name="property14",
    ends={
        Property(name="syswbeff106_FunctionProperty", type=syswbeff106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Function15", type=syswbeff106_FunctionProperty, multiplicity=Multiplicity(0, 9999))
    }
)
associations17: BinaryAssociation = BinaryAssociation(
    name="associations17",
    ends={
        Property(name="syswbeff106_Function18", type=syswbeff106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Function16", type=syswbeff106_Function, multiplicity=Multiplicity(0, 1))
    }
)
allocatedTo19: BinaryAssociation = BinaryAssociation(
    name="allocatedTo19",
    ends={
        Property(name="syswbeff106_Component", type=syswbeff106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Function20", type=syswbeff106_Component, multiplicity=Multiplicity(0, 1))
    }
)
controlFlowEdge22: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge22",
    ends={
        Property(name="syswbeff106_SequenceNode", type=syswbeff106_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_SequenceNode21", type=syswbeff106_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)
items26: BinaryAssociation = BinaryAssociation(
    name="items26",
    ends={
        Property(name="syswbeff106_Item", type=syswbeff106_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Flow27", type=syswbeff106_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputflowEdge23: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge23",
    ends={
        Property(name="syswbeff106_InputPort25", type=syswbeff106_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Flow24", type=syswbeff106_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
outputflowEdge28: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge28",
    ends={
        Property(name="syswbeff106_Flow30", type=syswbeff106_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_OutputPort29", type=syswbeff106_Flow, multiplicity=Multiplicity(0, 9999))
    }
)
toThing32: BinaryAssociation = BinaryAssociation(
    name="toThing32",
    ends={
        Property(name="syswbeff106_Thing34", type=syswbeff106_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_RelatedTo33", type=syswbeff106_Thing, multiplicity=Multiplicity(0, 1))
    }
)
fromThing31: BinaryAssociation = BinaryAssociation(
    name="fromThing31",
    ends={
        Property(name="syswbeff106_Thing", type=syswbeff106_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_RelatedTo", type=syswbeff106_Thing, multiplicity=Multiplicity(0, 1))
    }
)
performs49: BinaryAssociation = BinaryAssociation(
    name="performs49",
    ends={
        Property(name="syswbeff106_Function51", type=syswbeff106_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Component50", type=syswbeff106_Function, multiplicity=Multiplicity(0, 9999))
    }
)
relations35: BinaryAssociation = BinaryAssociation(
    name="relations35",
    ends={
        Property(name="syswbeff106_RelatedTo37", type=syswbeff106_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Thing36", type=syswbeff106_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedTo38: BinaryAssociation = BinaryAssociation(
    name="relatedTo38",
    ends={
        Property(name="syswbeff106_Thing39", type=syswbeff106_Thoughts, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Thoughts", type=syswbeff106_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
parent41: BinaryAssociation = BinaryAssociation(
    name="parent41",
    ends={
        Property(name="syswbeff106_FunctionProperty42", type=syswbeff106_FunctionProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_FunctionProperty40", type=syswbeff106_FunctionProperty, multiplicity=Multiplicity(0, 1))
    }
)
decompositions44: BinaryAssociation = BinaryAssociation(
    name="decompositions44",
    ends={
        Property(name="syswbeff106_Component45", type=syswbeff106_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Component43", type=syswbeff106_Component, multiplicity=Multiplicity(0, 9999))
    }
)
associations47: BinaryAssociation = BinaryAssociation(
    name="associations47",
    ends={
        Property(name="syswbeff106_Component48", type=syswbeff106_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Component46", type=syswbeff106_Component, multiplicity=Multiplicity(0, 9999))
    }
)
things59: BinaryAssociation = BinaryAssociation(
    name="things59",
    ends={
        Property(name="syswbeff106_Thing60", type=syswbeff106_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Workbench", type=syswbeff106_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionalArchitecture52: BinaryAssociation = BinaryAssociation(
    name="functionalArchitecture52",
    ends={
        Property(name="syswbeff106_Function53", type=syswbeff106_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_System", type=syswbeff106_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
physicalArchitecture54: BinaryAssociation = BinaryAssociation(
    name="physicalArchitecture54",
    ends={
        Property(name="syswbeff106_Component56", type=syswbeff106_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_System55", type=syswbeff106_Component, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
patterns57: BinaryAssociation = BinaryAssociation(
    name="patterns57",
    ends={
        Property(name="syswbeff106_Function58", type=syswbeff106_PatternCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_PatternCatalog", type=syswbeff106_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoughts61: BinaryAssociation = BinaryAssociation(
    name="thoughts61",
    ends={
        Property(name="syswbeff106_Thoughts63", type=syswbeff106_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Workbench62", type=syswbeff106_Thoughts, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemView64: BinaryAssociation = BinaryAssociation(
    name="systemView64",
    ends={
        Property(name="syswbeff106_System66", type=syswbeff106_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Workbench65", type=syswbeff106_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionProperties67: BinaryAssociation = BinaryAssociation(
    name="functionProperties67",
    ends={
        Property(name="syswbeff106_FunctionProperty69", type=syswbeff106_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Workbench68", type=syswbeff106_FunctionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog70: BinaryAssociation = BinaryAssociation(
    name="catalog70",
    ends={
        Property(name="syswbeff106_PatternCatalog72", type=syswbeff106_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106_Workbench71", type=syswbeff106_PatternCatalog, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_syswbeff106_Function_SequenceNode = Generalization(general=SequenceNode, specific=syswbeff106_Function)
gen_syswbeff106_Function_ProcessNode = Generalization(general=ProcessNode, specific=syswbeff106_Function)
gen_syswbeff106_Start_Sequence = Generalization(general=Sequence, specific=syswbeff106_Start)
gen_syswbeff106_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=syswbeff106_Sequence)
gen_syswbeff106_And_Sequence = Generalization(general=Sequence, specific=syswbeff106_And)
gen_syswbeff106_Or_Sequence = Generalization(general=Sequence, specific=syswbeff106_Or)
gen_syswbeff106_Final_Sequence = Generalization(general=Sequence, specific=syswbeff106_Final)
gen_syswbeff106_Loop_Sequence = Generalization(general=Sequence, specific=syswbeff106_Loop)
gen_syswbeff106_InputPort_Port = Generalization(general=Port, specific=syswbeff106_InputPort)
gen_syswbeff106_Flow_ProcessNode = Generalization(general=ProcessNode, specific=syswbeff106_Flow)
gen_syswbeff106_OutputPort_Port = Generalization(general=Port, specific=syswbeff106_OutputPort)
gen_syswbeff106_LoopExit_Sequence = Generalization(general=Sequence, specific=syswbeff106_LoopExit)
gen_syswbeff106_Iteration_Sequence = Generalization(general=Sequence, specific=syswbeff106_Iteration)

# Domain Model
domain_model = DomainModel(
    name="syswbeff106",
    types={syswbeff106_Function, SequenceNode, ProcessNode, syswbeff106_InputPort, syswbeff106_Description, syswbeff106_Sequence, syswbeff106_Flow, syswbeff106_OutputPort, syswbeff106_Token, syswbeff106_FunctionProperty, syswbeff106_Component, syswbeff106_SequenceNode, syswbeff106_Start, syswbeff106_And, Sequence, syswbeff106_Or, syswbeff106_Final, syswbeff106_Loop, Port, syswbeff106_Port, syswbeff106_ProcessNode, syswbeff106_Item, syswbeff106_LoopExit, syswbeff106_Iteration, syswbeff106_RelatedTo, syswbeff106_Thing, syswbeff106_System, syswbeff106_Thoughts, syswbeff106_PatternCatalog, syswbeff106_Workbench, FunctionDomain},
    associations={inputPorts8, descriptions10, decompositions1, sequenceNodes2, flows4, outputPorts6, tokens12, property14, associations17, allocatedTo19, controlFlowEdge22, items26, inputflowEdge23, outputflowEdge28, toThing32, fromThing31, performs49, relations35, relatedTo38, parent41, decompositions44, associations47, things59, functionalArchitecture52, physicalArchitecture54, patterns57, thoughts61, systemView64, functionProperties67, catalog70},
    generalizations={gen_syswbeff106_Function_SequenceNode, gen_syswbeff106_Function_ProcessNode, gen_syswbeff106_Start_Sequence, gen_syswbeff106_Sequence_SequenceNode, gen_syswbeff106_And_Sequence, gen_syswbeff106_Or_Sequence, gen_syswbeff106_Final_Sequence, gen_syswbeff106_Loop_Sequence, gen_syswbeff106_InputPort_Port, gen_syswbeff106_Flow_ProcessNode, gen_syswbeff106_OutputPort_Port, gen_syswbeff106_LoopExit_Sequence, gen_syswbeff106_Iteration_Sequence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)