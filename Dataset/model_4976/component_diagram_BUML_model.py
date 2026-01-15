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
component_diagram_ComponentType = Class(name="component::diagram::ComponentType", is_abstract=True)
IDBase = Class(name="IDBase")
component_diagram_PortType = Class(name="component::diagram::PortType")
component_diagram_ComponentInstance = Class(name="component::diagram::ComponentInstance")
component_diagram_Connector = Class(name="component::diagram::Connector")
component_diagram_PortInstance = Class(name="component::diagram::PortInstance")
component_diagram_HardwareComponent = Class(name="component::diagram::HardwareComponent")
ComponentType = Class(name="ComponentType")
component_diagram_SoftwareComponent = Class(name="component::diagram::SoftwareComponent")
component_diagram_ElectronicDevice = Class(name="component::diagram::ElectronicDevice")
HardwareComponent = Class(name="HardwareComponent")
component_diagram_MechanicalDevice = Class(name="component::diagram::MechanicalDevice")
component_diagram_Actuator = Class(name="component::diagram::Actuator")
MechanicalDevice = Class(name="MechanicalDevice")
component_diagram_Sensor = Class(name="component::diagram::Sensor")
ElectronicDevice = Class(name="ElectronicDevice")
component_diagram_Architecture = Class(name="component::diagram::Architecture")

# component_diagram_ComponentType class attributes and methods
component_diagram_ComponentType_name: Property = Property(name="name", type=StringType)
component_diagram_ComponentType.attributes={component_diagram_ComponentType_name}

# IDBase class attributes and methods

# component_diagram_PortType class attributes and methods
component_diagram_PortType_name: Property = Property(name="name", type=StringType)
component_diagram_PortType.attributes={component_diagram_PortType_name}

# component_diagram_ComponentInstance class attributes and methods
component_diagram_ComponentInstance_version: Property = Property(name="version", type=IntegerType)
component_diagram_ComponentInstance_name: Property = Property(name="name", type=StringType)
component_diagram_ComponentInstance.attributes={component_diagram_ComponentInstance_name, component_diagram_ComponentInstance_version}

# component_diagram_Connector class attributes and methods
component_diagram_Connector_name: Property = Property(name="name", type=StringType)
component_diagram_Connector.attributes={component_diagram_Connector_name}

# component_diagram_PortInstance class attributes and methods
component_diagram_PortInstance_name: Property = Property(name="name", type=StringType)
component_diagram_PortInstance.attributes={component_diagram_PortInstance_name}

# component_diagram_HardwareComponent class attributes and methods
component_diagram_HardwareComponent_powerSupply: Property = Property(name="powerSupply", type=StringType)
component_diagram_HardwareComponent.attributes={component_diagram_HardwareComponent_powerSupply}

# ComponentType class attributes and methods

# component_diagram_SoftwareComponent class attributes and methods

# component_diagram_ElectronicDevice class attributes and methods

# HardwareComponent class attributes and methods

# component_diagram_MechanicalDevice class attributes and methods

# component_diagram_Actuator class attributes and methods

# MechanicalDevice class attributes and methods

# component_diagram_Sensor class attributes and methods
component_diagram_Sensor_type: Property = Property(name="type", type=StringType)
component_diagram_Sensor.attributes={component_diagram_Sensor_type}

# ElectronicDevice class attributes and methods

# component_diagram_Architecture class attributes and methods

# Relationships
port_types0: BinaryAssociation = BinaryAssociation(
    name="port_types0",
    ends={
        Property(name="PortType", type=component_diagram_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="component_type", type=component_diagram_PortType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance1: BinaryAssociation = BinaryAssociation(
    name="instance1",
    ends={
        Property(name="ComponentInstance", type=component_diagram_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
port2: BinaryAssociation = BinaryAssociation(
    name="port2",
    ends={
        Property(name="PortInstance", type=component_diagram_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connect", type=component_diagram_PortInstance, multiplicity=Multiplicity(2, 2))
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="PortType9", type=component_diagram_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="port_instance", type=component_diagram_PortType, multiplicity=Multiplicity(1, 1))
    }
)
component10: BinaryAssociation = BinaryAssociation(
    name="component10",
    ends={
        Property(name="component_diagram_ComponentType", type=component_diagram_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="component_diagram_Architecture", type=component_diagram_ComponentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors11: BinaryAssociation = BinaryAssociation(
    name="connectors11",
    ends={
        Property(name="component_diagram_Connector", type=component_diagram_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="component_diagram_Architecture12", type=component_diagram_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports13: BinaryAssociation = BinaryAssociation(
    name="ports13",
    ends={
        Property(name="component_diagram_PortInstance", type=component_diagram_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="component_diagram_Architecture14", type=component_diagram_PortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connect3: BinaryAssociation = BinaryAssociation(
    name="connect3",
    ends={
        Property(name="Connector", type=component_diagram_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="port", type=component_diagram_Connector, multiplicity=Multiplicity(0, 1))
    }
)
outComponent4: BinaryAssociation = BinaryAssociation(
    name="outComponent4",
    ends={
        Property(name="ComponentInstance5", type=component_diagram_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="outPorts", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(0, 1))
    }
)
inComponent6: BinaryAssociation = BinaryAssociation(
    name="inComponent6",
    ends={
        Property(name="ComponentInstance7", type=component_diagram_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="inPorts", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(0, 1))
    }
)
inPorts25: BinaryAssociation = BinaryAssociation(
    name="inPorts25",
    ends={
        Property(name="inComponent", type=component_diagram_PortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="PortInstance26", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
outPorts27: BinaryAssociation = BinaryAssociation(
    name="outPorts27",
    ends={
        Property(name="PortInstance28", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="outComponent", type=component_diagram_PortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="ComponentType", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance", type=component_diagram_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
component_type30: BinaryAssociation = BinaryAssociation(
    name="component_type30",
    ends={
        Property(name="ComponentType31", type=component_diagram_PortType, multiplicity=Multiplicity(1, 1)),
        Property(name="port_types", type=component_diagram_ComponentType, multiplicity=Multiplicity(0, 1))
    }
)
port_instance32: BinaryAssociation = BinaryAssociation(
    name="port_instance32",
    ends={
        Property(name="PortInstance34", type=component_diagram_PortType, multiplicity=Multiplicity(1, 1)),
        Property(name="type33", type=component_diagram_PortInstance, multiplicity=Multiplicity(0, 9999))
    }
)
instances15: BinaryAssociation = BinaryAssociation(
    name="instances15",
    ends={
        Property(name="component_diagram_ComponentInstance", type=component_diagram_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="component_diagram_Architecture16", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port_type17: BinaryAssociation = BinaryAssociation(
    name="port_type17",
    ends={
        Property(name="component_diagram_PortType", type=component_diagram_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="component_diagram_Architecture18", type=component_diagram_PortType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subcomponent20: BinaryAssociation = BinaryAssociation(
    name="subcomponent20",
    ends={
        Property(name="ComponentInstance21", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="parentcomponent", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentcomponent23: BinaryAssociation = BinaryAssociation(
    name="parentcomponent23",
    ends={
        Property(name="ComponentInstance24", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="subcomponent", type=component_diagram_ComponentInstance, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_component_diagram_ComponentType_IDBase = Generalization(general=IDBase, specific=component_diagram_ComponentType)
gen_component_diagram_Connector_IDBase = Generalization(general=IDBase, specific=component_diagram_Connector)
gen_component_diagram_HardwareComponent_ComponentType = Generalization(general=ComponentType, specific=component_diagram_HardwareComponent)
gen_component_diagram_SoftwareComponent_ComponentType = Generalization(general=ComponentType, specific=component_diagram_SoftwareComponent)
gen_component_diagram_ElectronicDevice_HardwareComponent = Generalization(general=HardwareComponent, specific=component_diagram_ElectronicDevice)
gen_component_diagram_MechanicalDevice_HardwareComponent = Generalization(general=HardwareComponent, specific=component_diagram_MechanicalDevice)
gen_component_diagram_Actuator_MechanicalDevice = Generalization(general=MechanicalDevice, specific=component_diagram_Actuator)
gen_component_diagram_Sensor_ElectronicDevice = Generalization(general=ElectronicDevice, specific=component_diagram_Sensor)
gen_component_diagram_Architecture_IDBase = Generalization(general=IDBase, specific=component_diagram_Architecture)
gen_component_diagram_PortInstance_IDBase = Generalization(general=IDBase, specific=component_diagram_PortInstance)
gen_component_diagram_PortType_IDBase = Generalization(general=IDBase, specific=component_diagram_PortType)
gen_component_diagram_ComponentInstance_IDBase = Generalization(general=IDBase, specific=component_diagram_ComponentInstance)

# Domain Model
domain_model = DomainModel(
    name="component_diagram",
    types={component_diagram_ComponentType, IDBase, component_diagram_PortType, component_diagram_ComponentInstance, component_diagram_Connector, component_diagram_PortInstance, component_diagram_HardwareComponent, ComponentType, component_diagram_SoftwareComponent, component_diagram_ElectronicDevice, HardwareComponent, component_diagram_MechanicalDevice, component_diagram_Actuator, MechanicalDevice, component_diagram_Sensor, ElectronicDevice, component_diagram_Architecture},
    associations={port_types0, instance1, port2, type8, component10, connectors11, ports13, connect3, outComponent4, inComponent6, inPorts25, outPorts27, type29, component_type30, port_instance32, instances15, port_type17, subcomponent20, parentcomponent23},
    generalizations={gen_component_diagram_ComponentType_IDBase, gen_component_diagram_Connector_IDBase, gen_component_diagram_HardwareComponent_ComponentType, gen_component_diagram_SoftwareComponent_ComponentType, gen_component_diagram_ElectronicDevice_HardwareComponent, gen_component_diagram_MechanicalDevice_HardwareComponent, gen_component_diagram_Actuator_MechanicalDevice, gen_component_diagram_Sensor_ElectronicDevice, gen_component_diagram_Architecture_IDBase, gen_component_diagram_PortInstance_IDBase, gen_component_diagram_PortType_IDBase, gen_component_diagram_ComponentInstance_IDBase},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)