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
syswbeff1065ok_Function = Class(name="syswbeff1065ok::Function")
SequenceNode = Class(name="SequenceNode")
ProcessNode = Class(name="ProcessNode")
syswbeff1065ok_Flow = Class(name="syswbeff1065ok::Flow")
syswbeff1065ok_OutputPort = Class(name="syswbeff1065ok::OutputPort")
syswbeff1065ok_InputPort = Class(name="syswbeff1065ok::InputPort")
syswbeff1065ok_Description = Class(name="syswbeff1065ok::Description")
syswbeff1065ok_Token = Class(name="syswbeff1065ok::Token")
syswbeff1065ok_FunctionProperty = Class(name="syswbeff1065ok::FunctionProperty")
syswbeff1065ok_Component = Class(name="syswbeff1065ok::Component")
syswbeff1065ok_SequenceNode = Class(name="syswbeff1065ok::SequenceNode", is_abstract=True)
syswbeff1065ok_Sequence = Class(name="syswbeff1065ok::Sequence", is_abstract=True)
syswbeff1065ok_And = Class(name="syswbeff1065ok::And")
Sequence = Class(name="Sequence")
syswbeff1065ok_Or = Class(name="syswbeff1065ok::Or")
syswbeff1065ok_Final = Class(name="syswbeff1065ok::Final")
syswbeff1065ok_Loop = Class(name="syswbeff1065ok::Loop")
syswbeff1065ok_Start = Class(name="syswbeff1065ok::Start")
syswbeff1065ok_Item = Class(name="syswbeff1065ok::Item")
Port = Class(name="Port")
syswbeff1065ok_Port = Class(name="syswbeff1065ok::Port", is_abstract=True)
syswbeff1065ok_ProcessNode = Class(name="syswbeff1065ok::ProcessNode", is_abstract=True)
syswbeff1065ok_Iteration = Class(name="syswbeff1065ok::Iteration")
syswbeff1065ok_AssociatedTo = Class(name="syswbeff1065ok::AssociatedTo")
syswbeff1065ok_Thing = Class(name="syswbeff1065ok::Thing")
syswbeff1065ok_LoopExit = Class(name="syswbeff1065ok::LoopExit")
syswbeff1065ok_Thoughts = Class(name="syswbeff1065ok::Thoughts")
syswbeff1065ok_PatternCatalog = Class(name="syswbeff1065ok::PatternCatalog")
syswbeff1065ok_Workbench = Class(name="syswbeff1065ok::Workbench")
syswbeff1065ok_System = Class(name="syswbeff1065ok::System")

# syswbeff1065ok_Function class attributes and methods
syswbeff1065ok_Function_domain: Property = Property(name="domain", type=StringType)
syswbeff1065ok_Function.attributes={syswbeff1065ok_Function_domain}

# SequenceNode class attributes and methods

# ProcessNode class attributes and methods

# syswbeff1065ok_Flow class attributes and methods

# syswbeff1065ok_OutputPort class attributes and methods

# syswbeff1065ok_InputPort class attributes and methods

# syswbeff1065ok_Description class attributes and methods
syswbeff1065ok_Description_content: Property = Property(name="content", type=StringType)
syswbeff1065ok_Description.attributes={syswbeff1065ok_Description_content}

# syswbeff1065ok_Token class attributes and methods

# syswbeff1065ok_FunctionProperty class attributes and methods
syswbeff1065ok_FunctionProperty_description: Property = Property(name="description", type=StringType)
syswbeff1065ok_FunctionProperty.attributes={syswbeff1065ok_FunctionProperty_description}

# syswbeff1065ok_Component class attributes and methods
syswbeff1065ok_Component_name: Property = Property(name="name", type=StringType)
syswbeff1065ok_Component.attributes={syswbeff1065ok_Component_name}

# syswbeff1065ok_SequenceNode class attributes and methods
syswbeff1065ok_SequenceNode_name: Property = Property(name="name", type=StringType)
syswbeff1065ok_SequenceNode_tMin: Property = Property(name="tMin", type=IntegerType)
syswbeff1065ok_SequenceNode_tMax: Property = Property(name="tMax", type=IntegerType)
syswbeff1065ok_SequenceNode.attributes={syswbeff1065ok_SequenceNode_name, syswbeff1065ok_SequenceNode_tMax, syswbeff1065ok_SequenceNode_tMin}

# syswbeff1065ok_Sequence class attributes and methods

# syswbeff1065ok_And class attributes and methods

# Sequence class attributes and methods

# syswbeff1065ok_Or class attributes and methods

# syswbeff1065ok_Final class attributes and methods

# syswbeff1065ok_Loop class attributes and methods

# syswbeff1065ok_Start class attributes and methods

# syswbeff1065ok_Item class attributes and methods
syswbeff1065ok_Item_name: Property = Property(name="name", type=StringType)
syswbeff1065ok_Item.attributes={syswbeff1065ok_Item_name}

# Port class attributes and methods

# syswbeff1065ok_Port class attributes and methods
syswbeff1065ok_Port_id: Property = Property(name="id", type=StringType)
syswbeff1065ok_Port.attributes={syswbeff1065ok_Port_id}

# syswbeff1065ok_ProcessNode class attributes and methods
syswbeff1065ok_ProcessNode_label: Property = Property(name="label", type=StringType)
syswbeff1065ok_ProcessNode.attributes={syswbeff1065ok_ProcessNode_label}

# syswbeff1065ok_Iteration class attributes and methods

# syswbeff1065ok_AssociatedTo class attributes and methods
syswbeff1065ok_AssociatedTo_since: Property = Property(name="since", type=StringType)
syswbeff1065ok_AssociatedTo.attributes={syswbeff1065ok_AssociatedTo_since}

# syswbeff1065ok_Thing class attributes and methods
syswbeff1065ok_Thing_id: Property = Property(name="id", type=IntegerType)
syswbeff1065ok_Thing.attributes={syswbeff1065ok_Thing_id}

# syswbeff1065ok_LoopExit class attributes and methods

# syswbeff1065ok_Thoughts class attributes and methods
syswbeff1065ok_Thoughts_id: Property = Property(name="id", type=StringType)
syswbeff1065ok_Thoughts.attributes={syswbeff1065ok_Thoughts_id}

# syswbeff1065ok_PatternCatalog class attributes and methods
syswbeff1065ok_PatternCatalog_id: Property = Property(name="id", type=StringType)
syswbeff1065ok_PatternCatalog.attributes={syswbeff1065ok_PatternCatalog_id}

# syswbeff1065ok_Workbench class attributes and methods

# syswbeff1065ok_System class attributes and methods
syswbeff1065ok_System_id: Property = Property(name="id", type=StringType)
syswbeff1065ok_System.attributes={syswbeff1065ok_System_id}

# Relationships
flows4: BinaryAssociation = BinaryAssociation(
    name="flows4",
    ends={
        Property(name="syswbeff1065ok_Flow", type=syswbeff1065ok_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Function5", type=syswbeff1065ok_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts6: BinaryAssociation = BinaryAssociation(
    name="outputPorts6",
    ends={
        Property(name="syswbeff1065ok_OutputPort", type=syswbeff1065ok_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Function7", type=syswbeff1065ok_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts8: BinaryAssociation = BinaryAssociation(
    name="inputPorts8",
    ends={
        Property(name="syswbeff1065ok_InputPort", type=syswbeff1065ok_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Function9", type=syswbeff1065ok_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions10: BinaryAssociation = BinaryAssociation(
    name="descriptions10",
    ends={
        Property(name="syswbeff1065ok_Description", type=syswbeff1065ok_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Function11", type=syswbeff1065ok_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens12: BinaryAssociation = BinaryAssociation(
    name="tokens12",
    ends={
        Property(name="syswbeff1065ok_Token", type=syswbeff1065ok_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Function13", type=syswbeff1065ok_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property14: BinaryAssociation = BinaryAssociation(
    name="property14",
    ends={
        Property(name="syswbeff1065ok_FunctionProperty", type=syswbeff1065ok_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Function15", type=syswbeff1065ok_FunctionProperty, multiplicity=Multiplicity(0, 9999))
    }
)
associations17: BinaryAssociation = BinaryAssociation(
    name="associations17",
    ends={
        Property(name="syswbeff1065ok_Function18", type=syswbeff1065ok_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Function16", type=syswbeff1065ok_Function, multiplicity=Multiplicity(0, 1))
    }
)
allocatedTo19: BinaryAssociation = BinaryAssociation(
    name="allocatedTo19",
    ends={
        Property(name="syswbeff1065ok_Component", type=syswbeff1065ok_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Function20", type=syswbeff1065ok_Component, multiplicity=Multiplicity(0, 1))
    }
)
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="syswbeff1065ok_Function", type=syswbeff1065ok_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Function0", type=syswbeff1065ok_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="syswbeff1065ok_Sequence", type=syswbeff1065ok_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Function3", type=syswbeff1065ok_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlFlowEdge22: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge22",
    ends={
        Property(name="syswbeff1065ok_SequenceNode21", type=syswbeff1065ok_SequenceNode, multiplicity=Multiplicity(0, 9999)),
        Property(name="syswbeff1065ok_SequenceNode", type=syswbeff1065ok_SequenceNode, multiplicity=Multiplicity(1, 1))
    }
)
inputflowEdge23: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge23",
    ends={
        Property(name="syswbeff1065ok_InputPort25", type=syswbeff1065ok_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Flow24", type=syswbeff1065ok_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
outputflowEdge28: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge28",
    ends={
        Property(name="syswbeff1065ok_Flow30", type=syswbeff1065ok_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_OutputPort29", type=syswbeff1065ok_Flow, multiplicity=Multiplicity(0, 9999))
    }
)
items26: BinaryAssociation = BinaryAssociation(
    name="items26",
    ends={
        Property(name="syswbeff1065ok_Item", type=syswbeff1065ok_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Flow27", type=syswbeff1065ok_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing31: BinaryAssociation = BinaryAssociation(
    name="fromThing31",
    ends={
        Property(name="syswbeff1065ok_Thing", type=syswbeff1065ok_AssociatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_AssociatedTo", type=syswbeff1065ok_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing32: BinaryAssociation = BinaryAssociation(
    name="toThing32",
    ends={
        Property(name="syswbeff1065ok_Thing34", type=syswbeff1065ok_AssociatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_AssociatedTo33", type=syswbeff1065ok_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relatedTo38: BinaryAssociation = BinaryAssociation(
    name="relatedTo38",
    ends={
        Property(name="syswbeff1065ok_Thing39", type=syswbeff1065ok_Thoughts, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Thoughts", type=syswbeff1065ok_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
parent41: BinaryAssociation = BinaryAssociation(
    name="parent41",
    ends={
        Property(name="syswbeff1065ok_FunctionProperty42", type=syswbeff1065ok_FunctionProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_FunctionProperty40", type=syswbeff1065ok_FunctionProperty, multiplicity=Multiplicity(0, 1))
    }
)
decompositions44: BinaryAssociation = BinaryAssociation(
    name="decompositions44",
    ends={
        Property(name="syswbeff1065ok_Component45", type=syswbeff1065ok_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Component43", type=syswbeff1065ok_Component, multiplicity=Multiplicity(0, 9999))
    }
)
associations47: BinaryAssociation = BinaryAssociation(
    name="associations47",
    ends={
        Property(name="syswbeff1065ok_Component48", type=syswbeff1065ok_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Component46", type=syswbeff1065ok_Component, multiplicity=Multiplicity(0, 9999))
    }
)
relations35: BinaryAssociation = BinaryAssociation(
    name="relations35",
    ends={
        Property(name="syswbeff1065ok_AssociatedTo37", type=syswbeff1065ok_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Thing36", type=syswbeff1065ok_AssociatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionalArchitecture52: BinaryAssociation = BinaryAssociation(
    name="functionalArchitecture52",
    ends={
        Property(name="syswbeff1065ok_Function53", type=syswbeff1065ok_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_System", type=syswbeff1065ok_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
physicalArchitecture54: BinaryAssociation = BinaryAssociation(
    name="physicalArchitecture54",
    ends={
        Property(name="syswbeff1065ok_Component56", type=syswbeff1065ok_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_System55", type=syswbeff1065ok_Component, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
patterns57: BinaryAssociation = BinaryAssociation(
    name="patterns57",
    ends={
        Property(name="syswbeff1065ok_Function58", type=syswbeff1065ok_PatternCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_PatternCatalog", type=syswbeff1065ok_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
performs49: BinaryAssociation = BinaryAssociation(
    name="performs49",
    ends={
        Property(name="syswbeff1065ok_Function51", type=syswbeff1065ok_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Component50", type=syswbeff1065ok_Function, multiplicity=Multiplicity(0, 9999))
    }
)
systemView64: BinaryAssociation = BinaryAssociation(
    name="systemView64",
    ends={
        Property(name="syswbeff1065ok_Workbench65", type=syswbeff1065ok_System, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="syswbeff1065ok_System66", type=syswbeff1065ok_Workbench, multiplicity=Multiplicity(1, 1))
    }
)
functionProperties67: BinaryAssociation = BinaryAssociation(
    name="functionProperties67",
    ends={
        Property(name="syswbeff1065ok_FunctionProperty69", type=syswbeff1065ok_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Workbench68", type=syswbeff1065ok_FunctionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog70: BinaryAssociation = BinaryAssociation(
    name="catalog70",
    ends={
        Property(name="syswbeff1065ok_PatternCatalog72", type=syswbeff1065ok_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Workbench71", type=syswbeff1065ok_PatternCatalog, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things59: BinaryAssociation = BinaryAssociation(
    name="things59",
    ends={
        Property(name="syswbeff1065ok_Thing60", type=syswbeff1065ok_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Workbench", type=syswbeff1065ok_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoughts61: BinaryAssociation = BinaryAssociation(
    name="thoughts61",
    ends={
        Property(name="syswbeff1065ok_Thoughts63", type=syswbeff1065ok_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff1065ok_Workbench62", type=syswbeff1065ok_Thoughts, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_syswbeff1065ok_Function_SequenceNode = Generalization(general=SequenceNode, specific=syswbeff1065ok_Function)
gen_syswbeff1065ok_Function_ProcessNode = Generalization(general=ProcessNode, specific=syswbeff1065ok_Function)
gen_syswbeff1065ok_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=syswbeff1065ok_Sequence)
gen_syswbeff1065ok_And_Sequence = Generalization(general=Sequence, specific=syswbeff1065ok_And)
gen_syswbeff1065ok_Or_Sequence = Generalization(general=Sequence, specific=syswbeff1065ok_Or)
gen_syswbeff1065ok_Final_Sequence = Generalization(general=Sequence, specific=syswbeff1065ok_Final)
gen_syswbeff1065ok_Loop_Sequence = Generalization(general=Sequence, specific=syswbeff1065ok_Loop)
gen_syswbeff1065ok_Start_Sequence = Generalization(general=Sequence, specific=syswbeff1065ok_Start)
gen_syswbeff1065ok_Flow_ProcessNode = Generalization(general=ProcessNode, specific=syswbeff1065ok_Flow)
gen_syswbeff1065ok_InputPort_Port = Generalization(general=Port, specific=syswbeff1065ok_InputPort)
gen_syswbeff1065ok_OutputPort_Port = Generalization(general=Port, specific=syswbeff1065ok_OutputPort)
gen_syswbeff1065ok_Iteration_Sequence = Generalization(general=Sequence, specific=syswbeff1065ok_Iteration)
gen_syswbeff1065ok_LoopExit_Sequence = Generalization(general=Sequence, specific=syswbeff1065ok_LoopExit)

# Domain Model
domain_model = DomainModel(
    name="syswbeff1065ok",
    types={syswbeff1065ok_Function, SequenceNode, ProcessNode, syswbeff1065ok_Flow, syswbeff1065ok_OutputPort, syswbeff1065ok_InputPort, syswbeff1065ok_Description, syswbeff1065ok_Token, syswbeff1065ok_FunctionProperty, syswbeff1065ok_Component, syswbeff1065ok_SequenceNode, syswbeff1065ok_Sequence, syswbeff1065ok_And, Sequence, syswbeff1065ok_Or, syswbeff1065ok_Final, syswbeff1065ok_Loop, syswbeff1065ok_Start, syswbeff1065ok_Item, Port, syswbeff1065ok_Port, syswbeff1065ok_ProcessNode, syswbeff1065ok_Iteration, syswbeff1065ok_AssociatedTo, syswbeff1065ok_Thing, syswbeff1065ok_LoopExit, syswbeff1065ok_Thoughts, syswbeff1065ok_PatternCatalog, syswbeff1065ok_Workbench, syswbeff1065ok_System, FunctionDomain},
    associations={flows4, outputPorts6, inputPorts8, descriptions10, tokens12, property14, associations17, allocatedTo19, decompositions1, sequenceNodes2, controlFlowEdge22, inputflowEdge23, outputflowEdge28, items26, fromThing31, toThing32, relatedTo38, parent41, decompositions44, associations47, relations35, functionalArchitecture52, physicalArchitecture54, patterns57, performs49, systemView64, functionProperties67, catalog70, things59, thoughts61},
    generalizations={gen_syswbeff1065ok_Function_SequenceNode, gen_syswbeff1065ok_Function_ProcessNode, gen_syswbeff1065ok_Sequence_SequenceNode, gen_syswbeff1065ok_And_Sequence, gen_syswbeff1065ok_Or_Sequence, gen_syswbeff1065ok_Final_Sequence, gen_syswbeff1065ok_Loop_Sequence, gen_syswbeff1065ok_Start_Sequence, gen_syswbeff1065ok_Flow_ProcessNode, gen_syswbeff1065ok_InputPort_Port, gen_syswbeff1065ok_OutputPort_Port, gen_syswbeff1065ok_Iteration_Sequence, gen_syswbeff1065ok_LoopExit_Sequence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)