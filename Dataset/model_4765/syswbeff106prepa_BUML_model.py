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
syswbeff106prepa_InputPort = Class(name="syswbeff106prepa::InputPort")
syswbeff106prepa_OutputPort = Class(name="syswbeff106prepa::OutputPort")
syswbeff106prepa_Flow = Class(name="syswbeff106prepa::Flow")
syswbeff106prepa_System = Class(name="syswbeff106prepa::System")
syswbeff106prepa_Function = Class(name="syswbeff106prepa::Function")
syswbeff106prepa_PatternCatalog = Class(name="syswbeff106prepa::PatternCatalog")
syswbeff106prepa_AbstractFunction = Class(name="syswbeff106prepa::AbstractFunction", is_abstract=True)
Port = Class(name="Port")
syswbeff106prepa_Port = Class(name="syswbeff106prepa::Port", is_abstract=True)
syswbeff106prepa_Pattern = Class(name="syswbeff106prepa::Pattern")
syswbeff106prepa_Workbench = Class(name="syswbeff106prepa::Workbench")
AbstractFunction = Class(name="AbstractFunction")

# syswbeff106prepa_InputPort class attributes and methods

# syswbeff106prepa_OutputPort class attributes and methods

# syswbeff106prepa_Flow class attributes and methods

# syswbeff106prepa_System class attributes and methods
syswbeff106prepa_System_id: Property = Property(name="id", type=StringType)
syswbeff106prepa_System.attributes={syswbeff106prepa_System_id}

# syswbeff106prepa_Function class attributes and methods

# syswbeff106prepa_PatternCatalog class attributes and methods
syswbeff106prepa_PatternCatalog_id: Property = Property(name="id", type=StringType)
syswbeff106prepa_PatternCatalog.attributes={syswbeff106prepa_PatternCatalog_id}

# syswbeff106prepa_AbstractFunction class attributes and methods
syswbeff106prepa_AbstractFunction_name: Property = Property(name="name", type=StringType)
syswbeff106prepa_AbstractFunction.attributes={syswbeff106prepa_AbstractFunction_name}

# Port class attributes and methods

# syswbeff106prepa_Port class attributes and methods
syswbeff106prepa_Port_name: Property = Property(name="name", type=StringType)
syswbeff106prepa_Port.attributes={syswbeff106prepa_Port_name}

# syswbeff106prepa_Pattern class attributes and methods

# syswbeff106prepa_Workbench class attributes and methods

# AbstractFunction class attributes and methods

# Relationships
associations1: BinaryAssociation = BinaryAssociation(
    name="associations1",
    ends={
        Property(name="syswbeff106prepa_AbstractFunction", type=syswbeff106prepa_AbstractFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_AbstractFunction0", type=syswbeff106prepa_AbstractFunction, multiplicity=Multiplicity(0, 1))
    }
)
inputports2: BinaryAssociation = BinaryAssociation(
    name="inputports2",
    ends={
        Property(name="syswbeff106prepa_InputPort", type=syswbeff106prepa_AbstractFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_AbstractFunction3", type=syswbeff106prepa_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputports4: BinaryAssociation = BinaryAssociation(
    name="outputports4",
    ends={
        Property(name="syswbeff106prepa_OutputPort", type=syswbeff106prepa_AbstractFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_AbstractFunction5", type=syswbeff106prepa_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flows6: BinaryAssociation = BinaryAssociation(
    name="flows6",
    ends={
        Property(name="syswbeff106prepa_Flow", type=syswbeff106prepa_AbstractFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_AbstractFunction7", type=syswbeff106prepa_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionalArchitecture8: BinaryAssociation = BinaryAssociation(
    name="functionalArchitecture8",
    ends={
        Property(name="syswbeff106prepa_Function", type=syswbeff106prepa_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_System", type=syswbeff106prepa_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equivalent16: BinaryAssociation = BinaryAssociation(
    name="equivalent16",
    ends={
        Property(name="syswbeff106prepa_Pattern17", type=syswbeff106prepa_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_Pattern15", type=syswbeff106prepa_Pattern, multiplicity=Multiplicity(0, 1))
    }
)
pdecompositions19: BinaryAssociation = BinaryAssociation(
    name="pdecompositions19",
    ends={
        Property(name="syswbeff106prepa_Pattern20", type=syswbeff106prepa_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_Pattern18", type=syswbeff106prepa_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fdecompositions22: BinaryAssociation = BinaryAssociation(
    name="fdecompositions22",
    ends={
        Property(name="syswbeff106prepa_Function23", type=syswbeff106prepa_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_Function21", type=syswbeff106prepa_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
patterns9: BinaryAssociation = BinaryAssociation(
    name="patterns9",
    ends={
        Property(name="syswbeff106prepa_Pattern", type=syswbeff106prepa_PatternCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_PatternCatalog", type=syswbeff106prepa_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemView10: BinaryAssociation = BinaryAssociation(
    name="systemView10",
    ends={
        Property(name="syswbeff106prepa_System11", type=syswbeff106prepa_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_Workbench", type=syswbeff106prepa_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catalog12: BinaryAssociation = BinaryAssociation(
    name="catalog12",
    ends={
        Property(name="syswbeff106prepa_PatternCatalog14", type=syswbeff106prepa_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_Workbench13", type=syswbeff106prepa_PatternCatalog, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from24: BinaryAssociation = BinaryAssociation(
    name="from24",
    ends={
        Property(name="syswbeff106prepa_OutputPort26", type=syswbeff106prepa_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_Flow25", type=syswbeff106prepa_OutputPort, multiplicity=Multiplicity(0, 1))
    }
)
to27: BinaryAssociation = BinaryAssociation(
    name="to27",
    ends={
        Property(name="syswbeff106prepa_InputPort29", type=syswbeff106prepa_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="syswbeff106prepa_Flow28", type=syswbeff106prepa_InputPort, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_syswbeff106prepa_Function_AbstractFunction = Generalization(general=AbstractFunction, specific=syswbeff106prepa_Function)
gen_syswbeff106prepa_InputPort_Port = Generalization(general=Port, specific=syswbeff106prepa_InputPort)
gen_syswbeff106prepa_OutputPort_Port = Generalization(general=Port, specific=syswbeff106prepa_OutputPort)
gen_syswbeff106prepa_Pattern_AbstractFunction = Generalization(general=AbstractFunction, specific=syswbeff106prepa_Pattern)

# Domain Model
domain_model = DomainModel(
    name="syswbeff106prepa",
    types={syswbeff106prepa_InputPort, syswbeff106prepa_OutputPort, syswbeff106prepa_Flow, syswbeff106prepa_System, syswbeff106prepa_Function, syswbeff106prepa_PatternCatalog, syswbeff106prepa_AbstractFunction, Port, syswbeff106prepa_Port, syswbeff106prepa_Pattern, syswbeff106prepa_Workbench, AbstractFunction},
    associations={associations1, inputports2, outputports4, flows6, functionalArchitecture8, equivalent16, pdecompositions19, fdecompositions22, patterns9, systemView10, catalog12, from24, to27},
    generalizations={gen_syswbeff106prepa_Function_AbstractFunction, gen_syswbeff106prepa_InputPort_Port, gen_syswbeff106prepa_OutputPort_Port, gen_syswbeff106prepa_Pattern_AbstractFunction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)