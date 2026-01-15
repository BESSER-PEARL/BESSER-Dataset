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
operandos: Enumeration = Enumeration(
    name="operandos",
    literals={
            EnumerationLiteral(name="menor"),
			EnumerationLiteral(name="mayor"),
			EnumerationLiteral(name="menorigual"),
			EnumerationLiteral(name="mayorigual"),
			EnumerationLiteral(name="igual"),
			EnumerationLiteral(name="diferente")
    }
)

# Classes
arduino_Led = Class(name="arduino::Led")
Actuadores = Class(name="Actuadores")
arduino_LDR = Class(name="arduino::LDR")
Sensores = Class(name="Sensores")
arduino_Apagar = Class(name="arduino::Apagar")
Instrucciones = Class(name="Instrucciones")
arduino_Esperar = Class(name="arduino::Esperar")
arduino_Variar = Class(name="arduino::Variar")
arduino_Sketch = Class(name="arduino::Sketch")
arduino_Sensores = Class(name="arduino::Sensores", is_abstract=True)
arduino_Actuadores = Class(name="arduino::Actuadores", is_abstract=True)
arduino_Instrucciones = Class(name="arduino::Instrucciones", is_abstract=True)
arduino_Bloques = Class(name="arduino::Bloques", is_abstract=True)
arduino_Temperatura = Class(name="arduino::Temperatura")
arduino_Potenciometro = Class(name="arduino::Potenciometro")
arduino_Boton = Class(name="arduino::Boton")
arduino_PIR = Class(name="arduino::PIR")
arduino_Buzzer = Class(name="arduino::Buzzer")
arduino_Servo = Class(name="arduino::Servo")
arduino_Encender = Class(name="arduino::Encender")
arduino_If = Class(name="arduino::If")
Bloques = Class(name="Bloques")
arduino_While = Class(name="arduino::While")

# arduino_Led class attributes and methods

# Actuadores class attributes and methods

# arduino_LDR class attributes and methods

# Sensores class attributes and methods

# arduino_Apagar class attributes and methods

# Instrucciones class attributes and methods

# arduino_Esperar class attributes and methods
arduino_Esperar_miliseg: Property = Property(name="miliseg", type=StringType)
arduino_Esperar.attributes={arduino_Esperar_miliseg}

# arduino_Variar class attributes and methods
arduino_Variar_pwm: Property = Property(name="pwm", type=StringType)
arduino_Variar.attributes={arduino_Variar_pwm}

# arduino_Sketch class attributes and methods
arduino_Sketch_Nombre: Property = Property(name="Nombre", type=StringType)
arduino_Sketch.attributes={arduino_Sketch_Nombre}

# arduino_Sensores class attributes and methods
arduino_Sensores_pin: Property = Property(name="pin", type=StringType)
arduino_Sensores_med: Property = Property(name="med", type=StringType)
arduino_Sensores.attributes={arduino_Sensores_pin, arduino_Sensores_med}

# arduino_Actuadores class attributes and methods
arduino_Actuadores_pin: Property = Property(name="pin", type=StringType)
arduino_Actuadores.attributes={arduino_Actuadores_pin}

# arduino_Instrucciones class attributes and methods

# arduino_Bloques class attributes and methods

# arduino_Temperatura class attributes and methods
arduino_Temperatura_temperatura: Property = Property(name="temperatura", type=StringType)
arduino_Temperatura.attributes={arduino_Temperatura_temperatura}

# arduino_Potenciometro class attributes and methods

# arduino_Boton class attributes and methods

# arduino_PIR class attributes and methods

# arduino_Buzzer class attributes and methods

# arduino_Servo class attributes and methods
arduino_Servo_angulo: Property = Property(name="angulo", type=StringType)
arduino_Servo_libreria: Property = Property(name="libreria", type=StringType)
arduino_Servo.attributes={arduino_Servo_angulo, arduino_Servo_libreria}

# arduino_Encender class attributes and methods

# arduino_If class attributes and methods
arduino_If_operando: Property = Property(name="operando", type=StringType)
arduino_If_referencia: Property = Property(name="referencia", type=StringType)
arduino_If_valor: Property = Property(name="valor", type=StringType)
arduino_If.attributes={arduino_If_operando, arduino_If_referencia, arduino_If_valor}

# Bloques class attributes and methods

# arduino_While class attributes and methods
arduino_While_operando: Property = Property(name="operando", type=StringType)
arduino_While_referencia: Property = Property(name="referencia", type=StringType)
arduino_While_valor: Property = Property(name="valor", type=StringType)
arduino_While.attributes={arduino_While_operando, arduino_While_valor, arduino_While_referencia}

# Relationships
esperar113: BinaryAssociation = BinaryAssociation(
    name="esperar113",
    ends={
        Property(name="arduino_Esperar", type=arduino_Apagar, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Apagar", type=arduino_Esperar, multiplicity=Multiplicity(0, 1))
    }
)
sensores0: BinaryAssociation = BinaryAssociation(
    name="sensores0",
    ends={
        Property(name="arduino_Sensores", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch", type=arduino_Sensores, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actuadores1: BinaryAssociation = BinaryAssociation(
    name="actuadores1",
    ends={
        Property(name="arduino_Actuadores", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch2", type=arduino_Actuadores, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instrucciones3: BinaryAssociation = BinaryAssociation(
    name="instrucciones3",
    ends={
        Property(name="arduino_Instrucciones", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch4", type=arduino_Instrucciones, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bloques5: BinaryAssociation = BinaryAssociation(
    name="bloques5",
    ends={
        Property(name="arduino_Bloques", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch6", type=arduino_Bloques, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actuadorinstruccion7: BinaryAssociation = BinaryAssociation(
    name="actuadorinstruccion7",
    ends={
        Property(name="arduino_Instrucciones9", type=arduino_Actuadores, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Actuadores8", type=arduino_Instrucciones, multiplicity=Multiplicity(0, 1))
    }
)
act10: BinaryAssociation = BinaryAssociation(
    name="act10",
    ends={
        Property(name="arduino_Actuadores12", type=arduino_Sensores, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sensores11", type=arduino_Actuadores, multiplicity=Multiplicity(0, 9999))
    }
)
datos14: BinaryAssociation = BinaryAssociation(
    name="datos14",
    ends={
        Property(name="arduino_Sensores15", type=arduino_Variar, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Variar", type=arduino_Sensores, multiplicity=Multiplicity(0, 1))
    }
)
apagar16: BinaryAssociation = BinaryAssociation(
    name="apagar16",
    ends={
        Property(name="arduino_Apagar18", type=arduino_Esperar, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Esperar17", type=arduino_Apagar, multiplicity=Multiplicity(0, 1))
    }
)
encender19: BinaryAssociation = BinaryAssociation(
    name="encender19",
    ends={
        Property(name="arduino_Encender", type=arduino_Esperar, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Esperar20", type=arduino_Encender, multiplicity=Multiplicity(0, 1))
    }
)
esperar21: BinaryAssociation = BinaryAssociation(
    name="esperar21",
    ends={
        Property(name="arduino_Esperar23", type=arduino_Encender, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Encender22", type=arduino_Esperar, multiplicity=Multiplicity(0, 1))
    }
)
bloq25: BinaryAssociation = BinaryAssociation(
    name="bloq25",
    ends={
        Property(name="arduino_Bloques26", type=arduino_Bloques, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Bloques24", type=arduino_Bloques, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bactuadores27: BinaryAssociation = BinaryAssociation(
    name="bactuadores27",
    ends={
        Property(name="arduino_Actuadores29", type=arduino_Bloques, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Bloques28", type=arduino_Actuadores, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
binstrucciones30: BinaryAssociation = BinaryAssociation(
    name="binstrucciones30",
    ends={
        Property(name="arduino_Instrucciones32", type=arduino_Bloques, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Bloques31", type=arduino_Instrucciones, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bsensores33: BinaryAssociation = BinaryAssociation(
    name="bsensores33",
    ends={
        Property(name="arduino_Sensores35", type=arduino_Bloques, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Bloques34", type=arduino_Sensores, multiplicity=Multiplicity(0, 1))
    }
)
bloacts36: BinaryAssociation = BinaryAssociation(
    name="bloacts36",
    ends={
        Property(name="arduino_Actuadores38", type=arduino_Bloques, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Bloques37", type=arduino_Actuadores, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_arduino_Led_Actuadores = Generalization(general=Actuadores, specific=arduino_Led)
gen_arduino_LDR_Sensores = Generalization(general=Sensores, specific=arduino_LDR)
gen_arduino_Apagar_Instrucciones = Generalization(general=Instrucciones, specific=arduino_Apagar)
gen_arduino_Variar_Instrucciones = Generalization(general=Instrucciones, specific=arduino_Variar)
gen_arduino_Temperatura_Sensores = Generalization(general=Sensores, specific=arduino_Temperatura)
gen_arduino_Potenciometro_Sensores = Generalization(general=Sensores, specific=arduino_Potenciometro)
gen_arduino_Boton_Sensores = Generalization(general=Sensores, specific=arduino_Boton)
gen_arduino_PIR_Sensores = Generalization(general=Sensores, specific=arduino_PIR)
gen_arduino_Buzzer_Actuadores = Generalization(general=Actuadores, specific=arduino_Buzzer)
gen_arduino_Servo_Actuadores = Generalization(general=Actuadores, specific=arduino_Servo)
gen_arduino_Esperar_Instrucciones = Generalization(general=Instrucciones, specific=arduino_Esperar)
gen_arduino_Encender_Instrucciones = Generalization(general=Instrucciones, specific=arduino_Encender)
gen_arduino_If_Bloques = Generalization(general=Bloques, specific=arduino_If)
gen_arduino_While_Bloques = Generalization(general=Bloques, specific=arduino_While)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_Led, Actuadores, arduino_LDR, Sensores, arduino_Apagar, Instrucciones, arduino_Esperar, arduino_Variar, arduino_Sketch, arduino_Sensores, arduino_Actuadores, arduino_Instrucciones, arduino_Bloques, arduino_Temperatura, arduino_Potenciometro, arduino_Boton, arduino_PIR, arduino_Buzzer, arduino_Servo, arduino_Encender, arduino_If, Bloques, arduino_While, operandos},
    associations={esperar113, sensores0, actuadores1, instrucciones3, bloques5, actuadorinstruccion7, act10, datos14, apagar16, encender19, esperar21, bloq25, bactuadores27, binstrucciones30, bsensores33, bloacts36},
    generalizations={gen_arduino_Led_Actuadores, gen_arduino_LDR_Sensores, gen_arduino_Apagar_Instrucciones, gen_arduino_Variar_Instrucciones, gen_arduino_Temperatura_Sensores, gen_arduino_Potenciometro_Sensores, gen_arduino_Boton_Sensores, gen_arduino_PIR_Sensores, gen_arduino_Buzzer_Actuadores, gen_arduino_Servo_Actuadores, gen_arduino_Esperar_Instrucciones, gen_arduino_Encender_Instrucciones, gen_arduino_If_Bloques, gen_arduino_While_Bloques},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)