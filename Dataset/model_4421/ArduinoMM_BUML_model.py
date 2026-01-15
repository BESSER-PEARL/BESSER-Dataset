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
AnalogID: Enumeration = Enumeration(
    name="AnalogID",
    literals={
            EnumerationLiteral(name="A0"),
			EnumerationLiteral(name="A1"),
			EnumerationLiteral(name="A2"),
			EnumerationLiteral(name="A3"),
			EnumerationLiteral(name="A4"),
			EnumerationLiteral(name="A5"),
			EnumerationLiteral(name="A6")
    }
)

DigitalID: Enumeration = Enumeration(
    name="DigitalID",
    literals={
            EnumerationLiteral(name="D2"),
			EnumerationLiteral(name="D4"),
			EnumerationLiteral(name="D7"),
			EnumerationLiteral(name="D8"),
			EnumerationLiteral(name="D12"),
			EnumerationLiteral(name="D13")
    }
)

PinMode: Enumeration = Enumeration(
    name="PinMode",
    literals={
            EnumerationLiteral(name="INPUT"),
			EnumerationLiteral(name="OUTPUT"),
			EnumerationLiteral(name="INPUT_PULLUP")
    }
)

# Classes
ArduinoMetamodel_FiniteStateMachine = Class(name="ArduinoMetamodel::FiniteStateMachine")
ArduinoMetamodel_Digital = Class(name="ArduinoMetamodel::Digital")
ArduinoMetamodel_Analog = Class(name="ArduinoMetamodel::Analog")
ArduinoMetamodel_Pin = Class(name="ArduinoMetamodel::Pin", is_abstract=True)
Pin = Class(name="Pin")
ArduinoMetamodel_Project = Class(name="ArduinoMetamodel::Project")
ArduinoMetamodel_ArduinoBoardUNO = Class(name="ArduinoMetamodel::ArduinoBoardUNO")
ArduinoMetamodel_Metodo = Class(name="ArduinoMetamodel::Metodo")
ArduinoMetamodel_Action = Class(name="ArduinoMetamodel::Action")
ArduinoMetamodel_PWM = Class(name="ArduinoMetamodel::PWM")
Analog = Class(name="Analog")
ArduinoMetamodel_Instruccion = Class(name="ArduinoMetamodel::Instruccion")
ArduinoMetamodel_delay = Class(name="ArduinoMetamodel::delay")
Instruccion = Class(name="Instruccion")
ArduinoMetamodel_State = Class(name="ArduinoMetamodel::State")
ArduinoMetamodel_Transition = Class(name="ArduinoMetamodel::Transition")

# ArduinoMetamodel_FiniteStateMachine class attributes and methods

# ArduinoMetamodel_Digital class attributes and methods
ArduinoMetamodel_Digital_ID: Property = Property(name="ID", type=StringType)
ArduinoMetamodel_Digital.attributes={ArduinoMetamodel_Digital_ID}

# ArduinoMetamodel_Analog class attributes and methods
ArduinoMetamodel_Analog_ID: Property = Property(name="ID", type=StringType)
ArduinoMetamodel_Analog.attributes={ArduinoMetamodel_Analog_ID}

# ArduinoMetamodel_Pin class attributes and methods
ArduinoMetamodel_Pin_label: Property = Property(name="label", type=StringType)
ArduinoMetamodel_Pin_pinMode: Property = Property(name="pinMode", type=StringType)
ArduinoMetamodel_Pin.attributes={ArduinoMetamodel_Pin_pinMode, ArduinoMetamodel_Pin_label}

# Pin class attributes and methods

# ArduinoMetamodel_Project class attributes and methods

# ArduinoMetamodel_ArduinoBoardUNO class attributes and methods

# ArduinoMetamodel_Metodo class attributes and methods
ArduinoMetamodel_Metodo_nombre: Property = Property(name="nombre", type=StringType)
ArduinoMetamodel_Metodo.attributes={ArduinoMetamodel_Metodo_nombre}

# ArduinoMetamodel_Action class attributes and methods

# ArduinoMetamodel_PWM class attributes and methods

# Analog class attributes and methods

# ArduinoMetamodel_Instruccion class attributes and methods
ArduinoMetamodel_Instruccion_codigo: Property = Property(name="codigo", type=StringType)
ArduinoMetamodel_Instruccion.attributes={ArduinoMetamodel_Instruccion_codigo}

# ArduinoMetamodel_delay class attributes and methods

# Instruccion class attributes and methods

# ArduinoMetamodel_State class attributes and methods
ArduinoMetamodel_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
ArduinoMetamodel_State_name: Property = Property(name="name", type=StringType)
ArduinoMetamodel_State.attributes={ArduinoMetamodel_State_isInitial, ArduinoMetamodel_State_name}

# ArduinoMetamodel_Transition class attributes and methods

# Relationships
metodos1: BinaryAssociation = BinaryAssociation(
    name="metodos1",
    ends={
        Property(name="ArduinoMetamodel_Metodo", type=ArduinoMetamodel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoMetamodel_Project2", type=ArduinoMetamodel_Metodo, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fsm3: BinaryAssociation = BinaryAssociation(
    name="fsm3",
    ends={
        Property(name="ArduinoMetamodel_FiniteStateMachine", type=ArduinoMetamodel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoMetamodel_Project4", type=ArduinoMetamodel_FiniteStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
digitalpins5: BinaryAssociation = BinaryAssociation(
    name="digitalpins5",
    ends={
        Property(name="ArduinoMetamodel_Digital", type=ArduinoMetamodel_ArduinoBoardUNO, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoMetamodel_ArduinoBoardUNO6", type=ArduinoMetamodel_Digital, multiplicity=Multiplicity(0, 6), is_composite=True)
    }
)
analogpins7: BinaryAssociation = BinaryAssociation(
    name="analogpins7",
    ends={
        Property(name="ArduinoMetamodel_Analog", type=ArduinoMetamodel_ArduinoBoardUNO, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoMetamodel_ArduinoBoardUNO8", type=ArduinoMetamodel_Analog, multiplicity=Multiplicity(0, 6), is_composite=True)
    }
)
boards0: BinaryAssociation = BinaryAssociation(
    name="boards0",
    ends={
        Property(name="ArduinoMetamodel_ArduinoBoardUNO", type=ArduinoMetamodel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoMetamodel_Project", type=ArduinoMetamodel_ArduinoBoardUNO, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actions14: BinaryAssociation = BinaryAssociation(
    name="actions14",
    ends={
        Property(name="ArduinoMetamodel_Action", type=ArduinoMetamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoMetamodel_Transition", type=ArduinoMetamodel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="State", type=ArduinoMetamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=ArduinoMetamodel_State, multiplicity=Multiplicity(1, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="State17", type=ArduinoMetamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=ArduinoMetamodel_State, multiplicity=Multiplicity(1, 1))
    }
)
states18: BinaryAssociation = BinaryAssociation(
    name="states18",
    ends={
        Property(name="ArduinoMetamodel_State", type=ArduinoMetamodel_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoMetamodel_FiniteStateMachine19", type=ArduinoMetamodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instrucciones9: BinaryAssociation = BinaryAssociation(
    name="instrucciones9",
    ends={
        Property(name="ArduinoMetamodel_Instruccion", type=ArduinoMetamodel_Metodo, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoMetamodel_Metodo10", type=ArduinoMetamodel_Instruccion, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
incoming11: BinaryAssociation = BinaryAssociation(
    name="incoming11",
    ends={
        Property(name="Transition", type=ArduinoMetamodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=ArduinoMetamodel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing12: BinaryAssociation = BinaryAssociation(
    name="outgoing12",
    ends={
        Property(name="Transition13", type=ArduinoMetamodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ArduinoMetamodel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ArduinoMetamodel_Digital_Pin = Generalization(general=Pin, specific=ArduinoMetamodel_Digital)
gen_ArduinoMetamodel_Analog_Pin = Generalization(general=Pin, specific=ArduinoMetamodel_Analog)
gen_ArduinoMetamodel_PWM_Analog = Generalization(general=Analog, specific=ArduinoMetamodel_PWM)
gen_ArduinoMetamodel_delay_Instruccion = Generalization(general=Instruccion, specific=ArduinoMetamodel_delay)

# Domain Model
domain_model = DomainModel(
    name="ArduinoMetamodel",
    types={ArduinoMetamodel_FiniteStateMachine, ArduinoMetamodel_Digital, ArduinoMetamodel_Analog, ArduinoMetamodel_Pin, Pin, ArduinoMetamodel_Project, ArduinoMetamodel_ArduinoBoardUNO, ArduinoMetamodel_Metodo, ArduinoMetamodel_Action, ArduinoMetamodel_PWM, Analog, ArduinoMetamodel_Instruccion, ArduinoMetamodel_delay, Instruccion, ArduinoMetamodel_State, ArduinoMetamodel_Transition, AnalogID, DigitalID, PinMode},
    associations={metodos1, fsm3, digitalpins5, analogpins7, boards0, actions14, source15, target16, states18, instrucciones9, incoming11, outgoing12},
    generalizations={gen_ArduinoMetamodel_Digital_Pin, gen_ArduinoMetamodel_Analog_Pin, gen_ArduinoMetamodel_PWM_Analog, gen_ArduinoMetamodel_delay_Instruccion},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)