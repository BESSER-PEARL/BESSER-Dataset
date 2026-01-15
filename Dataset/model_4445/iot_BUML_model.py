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
Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NE"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="GE"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="LE")
    }
)

# Classes
iot_Software = Class(name="iot::Software")
Component = Class(name="Component")
iot_Item = Class(name="iot::Item", is_abstract=True)
iot_Hardware = Class(name="iot::Hardware", is_abstract=True)
iot_CounterLoop = Class(name="iot::CounterLoop")
Iteration = Class(name="Iteration")
iot_IfPort = Class(name="iot::IfPort")
RequiredPort = Class(name="RequiredPort")
iot_Actuator = Class(name="iot::Actuator")
Hardware = Class(name="Hardware")
iot_IterativeLoop = Class(name="iot::IterativeLoop")
iot_ConditionPort = Class(name="iot::ConditionPort")
iot_ProvidedPort = Class(name="iot::ProvidedPort")
iot_Branching = Class(name="iot::Branching")
Controller = Class(name="Controller")
iot_ThenPort = Class(name="iot::ThenPort")
iot_ElsePort = Class(name="iot::ElsePort")
iot_Iteration = Class(name="iot::Iteration", is_abstract=True)
iot_RequiredPort = Class(name="iot::RequiredPort")
iot_Sensor = Class(name="iot::Sensor")
iot_Sequence = Class(name="iot::Sequence")
iot_Component = Class(name="iot::Component", is_abstract=True)
Item = Class(name="Item")
iot_Controller = Class(name="iot::Controller", is_abstract=True)
iot_Snippet = Class(name="iot::Snippet")

# iot_Software class attributes and methods

# Component class attributes and methods

# iot_Item class attributes and methods
iot_Item_name: Property = Property(name="name", type=StringType)
iot_Item_UUID: Property = Property(name="UUID", type=StringType)
iot_Item_newThread: Property = Property(name="newThread", type=BooleanType)
iot_Item_m_invoke: Method = Method(name="invoke", parameters={}, type=StringType)
iot_Item.attributes={iot_Item_UUID, iot_Item_newThread, iot_Item_name}
iot_Item.methods={iot_Item_m_invoke}

# iot_Hardware class attributes and methods
iot_Hardware_type: Property = Property(name="type", type=StringType)
iot_Hardware_pinNumber: Property = Property(name="pinNumber", type=IntegerType)
iot_Hardware_mode: Property = Property(name="mode", type=BooleanType)
iot_Hardware_timeInterval: Property = Property(name="timeInterval", type=IntegerType)
iot_Hardware.attributes={iot_Hardware_timeInterval, iot_Hardware_pinNumber, iot_Hardware_type, iot_Hardware_mode}

# iot_CounterLoop class attributes and methods
iot_CounterLoop_counter: Property = Property(name="counter", type=IntegerType)
iot_CounterLoop.attributes={iot_CounterLoop_counter}

# Iteration class attributes and methods

# iot_IfPort class attributes and methods
iot_IfPort_condition: Property = Property(name="condition", type=BooleanType)
iot_IfPort_var: Property = Property(name="var", type=StringType)
iot_IfPort_operator: Property = Property(name="operator", type=StringType)
iot_IfPort.attributes={iot_IfPort_operator, iot_IfPort_condition, iot_IfPort_var}

# RequiredPort class attributes and methods

# iot_Actuator class attributes and methods
iot_Actuator_toggle: Property = Property(name="toggle", type=BooleanType)
iot_Actuator_m_toggle: Method = Method(name="toggle", parameters={}, type=StringType)
iot_Actuator_m_getStatus: Method = Method(name="getStatus", parameters={}, type=BooleanType)
iot_Actuator_m_switchOnOff: Method = Method(name="switchOnOff", parameters={Parameter(name='onOff')}, type=StringType)
iot_Actuator.attributes={iot_Actuator_toggle}
iot_Actuator.methods={iot_Actuator_m_switchOnOff, iot_Actuator_m_getStatus, iot_Actuator_m_toggle}

# Hardware class attributes and methods

# iot_IterativeLoop class attributes and methods
iot_IterativeLoop_var: Property = Property(name="var", type=StringType)
iot_IterativeLoop_operator: Property = Property(name="operator", type=StringType)
iot_IterativeLoop.attributes={iot_IterativeLoop_operator, iot_IterativeLoop_var}

# iot_ConditionPort class attributes and methods

# iot_ProvidedPort class attributes and methods
iot_ProvidedPort_UUID: Property = Property(name="UUID", type=StringType)
iot_ProvidedPort_name: Property = Property(name="name", type=StringType)
iot_ProvidedPort_m_invoke: Method = Method(name="invoke", parameters={Parameter(name='method'), Parameter(name='args')}, type=StringType)
iot_ProvidedPort_m_invoke: Method = Method(name="invoke", parameters={Parameter(name='method')}, type=StringType)
iot_ProvidedPort.attributes={iot_ProvidedPort_name, iot_ProvidedPort_UUID}
iot_ProvidedPort.methods={iot_ProvidedPort_m_invoke, iot_ProvidedPort_m_invoke}

# iot_Branching class attributes and methods

# Controller class attributes and methods

# iot_ThenPort class attributes and methods

# iot_ElsePort class attributes and methods

# iot_Iteration class attributes and methods

# iot_RequiredPort class attributes and methods
iot_RequiredPort_name: Property = Property(name="name", type=StringType)
iot_RequiredPort_UUID: Property = Property(name="UUID", type=StringType)
iot_RequiredPort_method: Property = Property(name="method", type=StringType)
iot_RequiredPort_args: Property = Property(name="args", type=StringType)
iot_RequiredPort_m_invoke: Method = Method(name="invoke", parameters={Parameter(name='method')}, type=StringType)
iot_RequiredPort.attributes={iot_RequiredPort_UUID, iot_RequiredPort_method, iot_RequiredPort_name, iot_RequiredPort_args}
iot_RequiredPort.methods={iot_RequiredPort_m_invoke}

# iot_Sensor class attributes and methods
iot_Sensor_script: Property = Property(name="script", type=StringType)
iot_Sensor_m_getData: Method = Method(name="getData", parameters={}, type=StringType)
iot_Sensor.attributes={iot_Sensor_script}
iot_Sensor.methods={iot_Sensor_m_getData}

# iot_Sequence class attributes and methods

# iot_Component class attributes and methods

# Item class attributes and methods

# iot_Controller class attributes and methods

# iot_Snippet class attributes and methods
iot_Snippet_scriptPath: Property = Property(name="scriptPath", type=StringType)
iot_Snippet.attributes={iot_Snippet_scriptPath}

# Relationships
item0: BinaryAssociation = BinaryAssociation(
    name="item0",
    ends={
        Property(name="iot_Item", type=iot_Software, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Software", type=iot_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition1: BinaryAssociation = BinaryAssociation(
    name="condition1",
    ends={
        Property(name="iot_ConditionPort", type=iot_IterativeLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_IterativeLoop", type=iot_ConditionPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referto2: BinaryAssociation = BinaryAssociation(
    name="referto2",
    ends={
        Property(name="iot_Item3", type=iot_ProvidedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_ProvidedPort", type=iot_Item, multiplicity=Multiplicity(1, 1))
    }
)
ifport4: BinaryAssociation = BinaryAssociation(
    name="ifport4",
    ends={
        Property(name="iot_IfPort", type=iot_Branching, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Branching", type=iot_IfPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenport5: BinaryAssociation = BinaryAssociation(
    name="thenport5",
    ends={
        Property(name="iot_ThenPort", type=iot_Branching, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Branching6", type=iot_ThenPort, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseport7: BinaryAssociation = BinaryAssociation(
    name="elseport7",
    ends={
        Property(name="iot_ElsePort", type=iot_Branching, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Branching8", type=iot_ElsePort, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredport9: BinaryAssociation = BinaryAssociation(
    name="requiredport9",
    ends={
        Property(name="iot_RequiredPort", type=iot_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Iteration", type=iot_RequiredPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
requiredport10: BinaryAssociation = BinaryAssociation(
    name="requiredport10",
    ends={
        Property(name="iot_RequiredPort11", type=iot_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Sequence", type=iot_RequiredPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
requiredport12: BinaryAssociation = BinaryAssociation(
    name="requiredport12",
    ends={
        Property(name="iot_RequiredPort13", type=iot_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Component", type=iot_RequiredPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedport14: BinaryAssociation = BinaryAssociation(
    name="providedport14",
    ends={
        Property(name="iot_ProvidedPort16", type=iot_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Component15", type=iot_ProvidedPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedport17: BinaryAssociation = BinaryAssociation(
    name="providedport17",
    ends={
        Property(name="iot_ProvidedPort18", type=iot_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Controller", type=iot_ProvidedPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
use19: BinaryAssociation = BinaryAssociation(
    name="use19",
    ends={
        Property(name="iot_ProvidedPort21", type=iot_RequiredPort, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_RequiredPort20", type=iot_ProvidedPort, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_iot_Software_Component = Generalization(general=Component, specific=iot_Software)
gen_iot_Hardware_Component = Generalization(general=Component, specific=iot_Hardware)
gen_iot_CounterLoop_Iteration = Generalization(general=Iteration, specific=iot_CounterLoop)
gen_iot_IfPort_RequiredPort = Generalization(general=RequiredPort, specific=iot_IfPort)
gen_iot_Actuator_Hardware = Generalization(general=Hardware, specific=iot_Actuator)
gen_iot_IterativeLoop_Iteration = Generalization(general=Iteration, specific=iot_IterativeLoop)
gen_iot_Branching_Controller = Generalization(general=Controller, specific=iot_Branching)
gen_iot_Iteration_Controller = Generalization(general=Controller, specific=iot_Iteration)
gen_iot_Sensor_Hardware = Generalization(general=Hardware, specific=iot_Sensor)
gen_iot_Sequence_Controller = Generalization(general=Controller, specific=iot_Sequence)
gen_iot_Component_Item = Generalization(general=Item, specific=iot_Component)
gen_iot_Controller_Item = Generalization(general=Item, specific=iot_Controller)
gen_iot_Snippet_Component = Generalization(general=Component, specific=iot_Snippet)
gen_iot_ConditionPort_RequiredPort = Generalization(general=RequiredPort, specific=iot_ConditionPort)
gen_iot_ThenPort_RequiredPort = Generalization(general=RequiredPort, specific=iot_ThenPort)
gen_iot_ElsePort_RequiredPort = Generalization(general=RequiredPort, specific=iot_ElsePort)

# Domain Model
domain_model = DomainModel(
    name="iot",
    types={iot_Software, Component, iot_Item, iot_Hardware, iot_CounterLoop, Iteration, iot_IfPort, RequiredPort, iot_Actuator, Hardware, iot_IterativeLoop, iot_ConditionPort, iot_ProvidedPort, iot_Branching, Controller, iot_ThenPort, iot_ElsePort, iot_Iteration, iot_RequiredPort, iot_Sensor, iot_Sequence, iot_Component, Item, iot_Controller, iot_Snippet, Operator},
    associations={item0, condition1, referto2, ifport4, thenport5, elseport7, requiredport9, requiredport10, requiredport12, providedport14, providedport17, use19},
    generalizations={gen_iot_Software_Component, gen_iot_Hardware_Component, gen_iot_CounterLoop_Iteration, gen_iot_IfPort_RequiredPort, gen_iot_Actuator_Hardware, gen_iot_IterativeLoop_Iteration, gen_iot_Branching_Controller, gen_iot_Iteration_Controller, gen_iot_Sensor_Hardware, gen_iot_Sequence_Controller, gen_iot_Component_Item, gen_iot_Controller_Item, gen_iot_Snippet_Component, gen_iot_ConditionPort_RequiredPort, gen_iot_ThenPort_RequiredPort, gen_iot_ElsePort_RequiredPort},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)