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
componentModel_ComponentModel = Class(name="componentModel_ComponentModel")
componentModel_AbstractElement = Class(name="componentModel_AbstractElement")
componentModel_SystemConnDec = Class(name="componentModel_SystemConnDec")
AbstractElement = Class(name="AbstractElement")
componentModel_SystemDec = Class(name="componentModel_SystemDec")
componentModel_SystemPortDec = Class(name="componentModel_SystemPortDec")
componentModel_AbstractFeatures = Class(name="componentModel_AbstractFeatures")
AbstractFeatures = Class(name="AbstractFeatures")
componentModel_SystemPortIn = Class(name="componentModel_SystemPortIn")
SystemPortDec = Class(name="SystemPortDec")
componentModel_ComponentImpl = Class(name="componentModel_ComponentImpl")
componentModel_InPort = Class(name="componentModel_InPort")
componentModel_SystemPortOut = Class(name="componentModel_SystemPortOut")
componentModel_OutPort = Class(name="componentModel_OutPort")
componentModel_CompConnDec = Class(name="componentModel_CompConnDec")
componentModel_ComponentType = Class(name="componentModel_ComponentType")
componentModel_ComponentFeature = Class(name="componentModel_ComponentFeature")
componentModel_Port = Class(name="componentModel_Port")
componentModel_errorModes = Class(name="componentModel_errorModes")
componentModel_PortType = Class(name="componentModel_PortType")
Port = Class(name="Port")

# componentModel_ComponentModel class attributes and methods

# componentModel_AbstractElement class attributes and methods
componentModel_AbstractElement_name: Property = Property(name="name", type=StringType)
componentModel_AbstractElement.attributes={componentModel_AbstractElement_name}

# componentModel_SystemConnDec class attributes and methods

# AbstractElement class attributes and methods

# componentModel_SystemDec class attributes and methods

# componentModel_SystemPortDec class attributes and methods

# componentModel_AbstractFeatures class attributes and methods
componentModel_AbstractFeatures_name: Property = Property(name="name", type=StringType)
componentModel_AbstractFeatures.attributes={componentModel_AbstractFeatures_name}

# AbstractFeatures class attributes and methods

# componentModel_SystemPortIn class attributes and methods

# SystemPortDec class attributes and methods

# componentModel_ComponentImpl class attributes and methods

# componentModel_InPort class attributes and methods

# componentModel_SystemPortOut class attributes and methods

# componentModel_OutPort class attributes and methods

# componentModel_CompConnDec class attributes and methods

# componentModel_ComponentType class attributes and methods

# componentModel_ComponentFeature class attributes and methods

# componentModel_Port class attributes and methods
componentModel_Port_name: Property = Property(name="name", type=StringType)
componentModel_Port.attributes={componentModel_Port_name}

# componentModel_errorModes class attributes and methods
componentModel_errorModes_name: Property = Property(name="name", type=StringType)
componentModel_errorModes.attributes={componentModel_errorModes_name}

# componentModel_PortType class attributes and methods

# Port class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="componentModel_AbstractElement", type=componentModel_ComponentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_ComponentModel", type=componentModel_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceSystem1: BinaryAssociation = BinaryAssociation(
    name="sourceSystem1",
    ends={
        Property(name="componentModel_SystemDec", type=componentModel_SystemConnDec, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_SystemConnDec", type=componentModel_SystemDec, multiplicity=Multiplicity(0, 1))
    }
)
sourcePort2: BinaryAssociation = BinaryAssociation(
    name="sourcePort2",
    ends={
        Property(name="componentModel_SystemPortDec", type=componentModel_SystemConnDec, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_SystemConnDec3", type=componentModel_SystemPortDec, multiplicity=Multiplicity(0, 1))
    }
)
targetSystem4: BinaryAssociation = BinaryAssociation(
    name="targetSystem4",
    ends={
        Property(name="componentModel_SystemDec6", type=componentModel_SystemConnDec, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_SystemConnDec5", type=componentModel_SystemDec, multiplicity=Multiplicity(0, 1))
    }
)
targetPort7: BinaryAssociation = BinaryAssociation(
    name="targetPort7",
    ends={
        Property(name="componentModel_SystemPortDec9", type=componentModel_SystemConnDec, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_SystemConnDec8", type=componentModel_SystemPortDec, multiplicity=Multiplicity(0, 1))
    }
)
sysFeatures10: BinaryAssociation = BinaryAssociation(
    name="sysFeatures10",
    ends={
        Property(name="componentModel_AbstractFeatures", type=componentModel_SystemDec, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_SystemDec11", type=componentModel_AbstractFeatures, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inComp12: BinaryAssociation = BinaryAssociation(
    name="inComp12",
    ends={
        Property(name="componentModel_ComponentImpl", type=componentModel_SystemPortIn, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_SystemPortIn", type=componentModel_ComponentImpl, multiplicity=Multiplicity(0, 1))
    }
)
inPort13: BinaryAssociation = BinaryAssociation(
    name="inPort13",
    ends={
        Property(name="componentModel_InPort", type=componentModel_SystemPortIn, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_SystemPortIn14", type=componentModel_InPort, multiplicity=Multiplicity(0, 1))
    }
)
outComp15: BinaryAssociation = BinaryAssociation(
    name="outComp15",
    ends={
        Property(name="componentModel_ComponentImpl16", type=componentModel_SystemPortOut, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_SystemPortOut", type=componentModel_ComponentImpl, multiplicity=Multiplicity(0, 1))
    }
)
outPort17: BinaryAssociation = BinaryAssociation(
    name="outPort17",
    ends={
        Property(name="componentModel_OutPort", type=componentModel_SystemPortOut, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_SystemPortOut18", type=componentModel_OutPort, multiplicity=Multiplicity(0, 1))
    }
)
sourceComp19: BinaryAssociation = BinaryAssociation(
    name="sourceComp19",
    ends={
        Property(name="componentModel_ComponentImpl20", type=componentModel_CompConnDec, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_CompConnDec", type=componentModel_ComponentImpl, multiplicity=Multiplicity(0, 1))
    }
)
sourcePort21: BinaryAssociation = BinaryAssociation(
    name="sourcePort21",
    ends={
        Property(name="componentModel_OutPort23", type=componentModel_CompConnDec, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_CompConnDec22", type=componentModel_OutPort, multiplicity=Multiplicity(0, 1))
    }
)
targetComp24: BinaryAssociation = BinaryAssociation(
    name="targetComp24",
    ends={
        Property(name="componentModel_ComponentImpl26", type=componentModel_CompConnDec, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_CompConnDec25", type=componentModel_ComponentImpl, multiplicity=Multiplicity(0, 1))
    }
)
targetPort27: BinaryAssociation = BinaryAssociation(
    name="targetPort27",
    ends={
        Property(name="componentModel_InPort29", type=componentModel_CompConnDec, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_CompConnDec28", type=componentModel_InPort, multiplicity=Multiplicity(0, 1))
    }
)
superType30: BinaryAssociation = BinaryAssociation(
    name="superType30",
    ends={
        Property(name="componentModel_ComponentType", type=componentModel_ComponentImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_ComponentImpl31", type=componentModel_ComponentType, multiplicity=Multiplicity(0, 1))
    }
)
compFeatures32: BinaryAssociation = BinaryAssociation(
    name="compFeatures32",
    ends={
        Property(name="componentModel_ComponentFeature", type=componentModel_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_ComponentType33", type=componentModel_ComponentFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports34: BinaryAssociation = BinaryAssociation(
    name="ports34",
    ends={
        Property(name="componentModel_Port", type=componentModel_ComponentFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_ComponentFeature35", type=componentModel_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eModes38: BinaryAssociation = BinaryAssociation(
    name="eModes38",
    ends={
        Property(name="componentModel_errorModes", type=componentModel_PortType, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_PortType39", type=componentModel_errorModes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType36: BinaryAssociation = BinaryAssociation(
    name="superType36",
    ends={
        Property(name="componentModel_PortType", type=componentModel_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Port37", type=componentModel_PortType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_componentModel_SystemConnDec_AbstractElement = Generalization(general=AbstractElement, specific=componentModel_SystemConnDec)
gen_componentModel_SystemPortDec_AbstractFeatures = Generalization(general=AbstractFeatures, specific=componentModel_SystemPortDec)
gen_componentModel_SystemPortIn_SystemPortDec = Generalization(general=SystemPortDec, specific=componentModel_SystemPortIn)
gen_componentModel_SystemPortOut_SystemPortDec = Generalization(general=SystemPortDec, specific=componentModel_SystemPortOut)
gen_componentModel_CompConnDec_AbstractFeatures = Generalization(general=AbstractFeatures, specific=componentModel_CompConnDec)
gen_componentModel_ComponentImpl_AbstractFeatures = Generalization(general=AbstractFeatures, specific=componentModel_ComponentImpl)
gen_componentModel_ComponentType_AbstractFeatures = Generalization(general=AbstractFeatures, specific=componentModel_ComponentType)
gen_componentModel_SystemDec_AbstractElement = Generalization(general=AbstractElement, specific=componentModel_SystemDec)
gen_componentModel_OutPort_Port = Generalization(general=Port, specific=componentModel_OutPort)
gen_componentModel_PortType_AbstractElement = Generalization(general=AbstractElement, specific=componentModel_PortType)
gen_componentModel_InPort_Port = Generalization(general=Port, specific=componentModel_InPort)

# Domain Model
domain_model = DomainModel(
    name="componentModel",
    types={componentModel_ComponentModel, componentModel_AbstractElement, componentModel_SystemConnDec, AbstractElement, componentModel_SystemDec, componentModel_SystemPortDec, componentModel_AbstractFeatures, AbstractFeatures, componentModel_SystemPortIn, SystemPortDec, componentModel_ComponentImpl, componentModel_InPort, componentModel_SystemPortOut, componentModel_OutPort, componentModel_CompConnDec, componentModel_ComponentType, componentModel_ComponentFeature, componentModel_Port, componentModel_errorModes, componentModel_PortType, Port},
    associations={elements0, sourceSystem1, sourcePort2, targetSystem4, targetPort7, sysFeatures10, inComp12, inPort13, outComp15, outPort17, sourceComp19, sourcePort21, targetComp24, targetPort27, superType30, compFeatures32, ports34, eModes38, superType36},
    generalizations={gen_componentModel_SystemConnDec_AbstractElement, gen_componentModel_SystemPortDec_AbstractFeatures, gen_componentModel_SystemPortIn_SystemPortDec, gen_componentModel_SystemPortOut_SystemPortDec, gen_componentModel_CompConnDec_AbstractFeatures, gen_componentModel_ComponentImpl_AbstractFeatures, gen_componentModel_ComponentType_AbstractFeatures, gen_componentModel_SystemDec_AbstractElement, gen_componentModel_OutPort_Port, gen_componentModel_PortType_AbstractElement, gen_componentModel_InPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)