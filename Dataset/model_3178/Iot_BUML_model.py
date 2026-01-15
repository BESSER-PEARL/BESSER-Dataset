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
iot_Etiqueta = Class(name="iot::Etiqueta")
iot_Estado = Class(name="iot::Estado")
iot_Evento = Class(name="iot::Evento")
iot_Transicion = Class(name="iot::Transicion")
iot_Model = Class(name="iot::Model")
iot_Dispositivo = Class(name="iot::Dispositivo")
iot_IfBlock = Class(name="iot::IfBlock")
iot_Variable = Class(name="iot::Variable")
iot_Or = Class(name="iot::Or")
Expression = Class(name="Expression")
iot_And = Class(name="iot::And")
iot_AbstractElement = Class(name="iot::AbstractElement")
iot_IfStatement = Class(name="iot::IfStatement")
AbstractElement = Class(name="AbstractElement")
iot_Expression = Class(name="iot::Expression")
iot_Plus = Class(name="iot::Plus")
iot_Minus = Class(name="iot::Minus")
iot_MulOrDiv = Class(name="iot::MulOrDiv")
iot_Equality = Class(name="iot::Equality")
iot_Comparison = Class(name="iot::Comparison")
iot_BoolConstant = Class(name="iot::BoolConstant")
iot_VariableRef = Class(name="iot::VariableRef")
iot_Not = Class(name="iot::Not")
iot_IntConstant = Class(name="iot::IntConstant")
iot_StringConstant = Class(name="iot::StringConstant")

# iot_Etiqueta class attributes and methods
iot_Etiqueta_typeName: Property = Property(name="typeName", type=StringType)
iot_Etiqueta_name: Property = Property(name="name", type=StringType)
iot_Etiqueta_value: Property = Property(name="value", type=StringType)
iot_Etiqueta.attributes={iot_Etiqueta_value, iot_Etiqueta_name, iot_Etiqueta_typeName}

# iot_Estado class attributes and methods
iot_Estado_name: Property = Property(name="name", type=StringType)
iot_Estado.attributes={iot_Estado_name}

# iot_Evento class attributes and methods
iot_Evento_typeName: Property = Property(name="typeName", type=StringType)
iot_Evento_name: Property = Property(name="name", type=StringType)
iot_Evento.attributes={iot_Evento_typeName, iot_Evento_name}

# iot_Transicion class attributes and methods

# iot_Model class attributes and methods

# iot_Dispositivo class attributes and methods
iot_Dispositivo_name: Property = Property(name="name", type=StringType)
iot_Dispositivo.attributes={iot_Dispositivo_name}

# iot_IfBlock class attributes and methods

# iot_Variable class attributes and methods
iot_Variable_name: Property = Property(name="name", type=StringType)
iot_Variable.attributes={iot_Variable_name}

# iot_Or class attributes and methods

# Expression class attributes and methods

# iot_And class attributes and methods

# iot_AbstractElement class attributes and methods

# iot_IfStatement class attributes and methods

# AbstractElement class attributes and methods

# iot_Expression class attributes and methods

# iot_Plus class attributes and methods

# iot_Minus class attributes and methods

# iot_MulOrDiv class attributes and methods
iot_MulOrDiv_op: Property = Property(name="op", type=StringType)
iot_MulOrDiv.attributes={iot_MulOrDiv_op}

# iot_Equality class attributes and methods
iot_Equality_op: Property = Property(name="op", type=StringType)
iot_Equality.attributes={iot_Equality_op}

# iot_Comparison class attributes and methods
iot_Comparison_op: Property = Property(name="op", type=StringType)
iot_Comparison.attributes={iot_Comparison_op}

# iot_BoolConstant class attributes and methods
iot_BoolConstant_value: Property = Property(name="value", type=StringType)
iot_BoolConstant.attributes={iot_BoolConstant_value}

# iot_VariableRef class attributes and methods

# iot_Not class attributes and methods

# iot_IntConstant class attributes and methods
iot_IntConstant_value: Property = Property(name="value", type=IntegerType)
iot_IntConstant.attributes={iot_IntConstant_value}

# iot_StringConstant class attributes and methods
iot_StringConstant_value: Property = Property(name="value", type=StringType)
iot_StringConstant.attributes={iot_StringConstant_value}

# Relationships
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="iot_Dispositivo3", type=iot_Dispositivo, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Dispositivo1", type=iot_Dispositivo, multiplicity=Multiplicity(0, 1))
    }
)
etiquetas4: BinaryAssociation = BinaryAssociation(
    name="etiquetas4",
    ends={
        Property(name="iot_Etiqueta", type=iot_Dispositivo, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Dispositivo5", type=iot_Etiqueta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
estados6: BinaryAssociation = BinaryAssociation(
    name="estados6",
    ends={
        Property(name="iot_Estado", type=iot_Dispositivo, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Dispositivo7", type=iot_Estado, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventos8: BinaryAssociation = BinaryAssociation(
    name="eventos8",
    ends={
        Property(name="iot_Evento", type=iot_Dispositivo, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Dispositivo9", type=iot_Evento, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transiciones10: BinaryAssociation = BinaryAssociation(
    name="transiciones10",
    ends={
        Property(name="iot_Transicion", type=iot_Dispositivo, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Dispositivo11", type=iot_Transicion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dispositivos0: BinaryAssociation = BinaryAssociation(
    name="dispositivos0",
    ends={
        Property(name="iot_Dispositivo", type=iot_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Model", type=iot_Dispositivo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression20: BinaryAssociation = BinaryAssociation(
    name="expression20",
    ends={
        Property(name="iot_Expression", type=iot_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_IfStatement", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBlock21: BinaryAssociation = BinaryAssociation(
    name="thenBlock21",
    ends={
        Property(name="iot_IfBlock", type=iot_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_IfStatement22", type=iot_IfBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock23: BinaryAssociation = BinaryAssociation(
    name="elseBlock23",
    ends={
        Property(name="iot_IfBlock25", type=iot_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_IfStatement24", type=iot_IfBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementos26: BinaryAssociation = BinaryAssociation(
    name="elementos26",
    ends={
        Property(name="iot_AbstractElement28", type=iot_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_IfBlock27", type=iot_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression29: BinaryAssociation = BinaryAssociation(
    name="expression29",
    ends={
        Property(name="iot_Expression30", type=iot_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Variable", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left31: BinaryAssociation = BinaryAssociation(
    name="left31",
    ends={
        Property(name="iot_Expression32", type=iot_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Or", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right33: BinaryAssociation = BinaryAssociation(
    name="right33",
    ends={
        Property(name="iot_Expression35", type=iot_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Or34", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementos12: BinaryAssociation = BinaryAssociation(
    name="elementos12",
    ends={
        Property(name="iot_AbstractElement", type=iot_Estado, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Estado13", type=iot_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
evento14: BinaryAssociation = BinaryAssociation(
    name="evento14",
    ends={
        Property(name="iot_Evento16", type=iot_Transicion, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Transicion15", type=iot_Evento, multiplicity=Multiplicity(0, 1))
    }
)
estado17: BinaryAssociation = BinaryAssociation(
    name="estado17",
    ends={
        Property(name="iot_Estado19", type=iot_Transicion, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Transicion18", type=iot_Estado, multiplicity=Multiplicity(0, 1))
    }
)
left46: BinaryAssociation = BinaryAssociation(
    name="left46",
    ends={
        Property(name="iot_Expression47", type=iot_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Comparison", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right48: BinaryAssociation = BinaryAssociation(
    name="right48",
    ends={
        Property(name="iot_Expression50", type=iot_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Comparison49", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left51: BinaryAssociation = BinaryAssociation(
    name="left51",
    ends={
        Property(name="iot_Expression52", type=iot_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Plus", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right53: BinaryAssociation = BinaryAssociation(
    name="right53",
    ends={
        Property(name="iot_Expression55", type=iot_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Plus54", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left56: BinaryAssociation = BinaryAssociation(
    name="left56",
    ends={
        Property(name="iot_Expression57", type=iot_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Minus", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right58: BinaryAssociation = BinaryAssociation(
    name="right58",
    ends={
        Property(name="iot_Expression60", type=iot_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Minus59", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left61: BinaryAssociation = BinaryAssociation(
    name="left61",
    ends={
        Property(name="iot_Expression62", type=iot_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_MulOrDiv", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left36: BinaryAssociation = BinaryAssociation(
    name="left36",
    ends={
        Property(name="iot_Expression37", type=iot_And, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_And", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right38: BinaryAssociation = BinaryAssociation(
    name="right38",
    ends={
        Property(name="iot_Expression40", type=iot_And, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_And39", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left41: BinaryAssociation = BinaryAssociation(
    name="left41",
    ends={
        Property(name="iot_Expression42", type=iot_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Equality", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right43: BinaryAssociation = BinaryAssociation(
    name="right43",
    ends={
        Property(name="iot_Expression45", type=iot_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Equality44", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable68: BinaryAssociation = BinaryAssociation(
    name="variable68",
    ends={
        Property(name="iot_Variable69", type=iot_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_VariableRef", type=iot_Variable, multiplicity=Multiplicity(0, 1))
    }
)
right63: BinaryAssociation = BinaryAssociation(
    name="right63",
    ends={
        Property(name="iot_Expression65", type=iot_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_MulOrDiv64", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression66: BinaryAssociation = BinaryAssociation(
    name="expression66",
    ends={
        Property(name="iot_Expression67", type=iot_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_Not", type=iot_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_iot_Variable_AbstractElement = Generalization(general=AbstractElement, specific=iot_Variable)
gen_iot_Expression_AbstractElement = Generalization(general=AbstractElement, specific=iot_Expression)
gen_iot_Or_Expression = Generalization(general=Expression, specific=iot_Or)
gen_iot_And_Expression = Generalization(general=Expression, specific=iot_And)
gen_iot_IfStatement_AbstractElement = Generalization(general=AbstractElement, specific=iot_IfStatement)
gen_iot_Plus_Expression = Generalization(general=Expression, specific=iot_Plus)
gen_iot_Minus_Expression = Generalization(general=Expression, specific=iot_Minus)
gen_iot_MulOrDiv_Expression = Generalization(general=Expression, specific=iot_MulOrDiv)
gen_iot_Equality_Expression = Generalization(general=Expression, specific=iot_Equality)
gen_iot_Comparison_Expression = Generalization(general=Expression, specific=iot_Comparison)
gen_iot_BoolConstant_Expression = Generalization(general=Expression, specific=iot_BoolConstant)
gen_iot_VariableRef_Expression = Generalization(general=Expression, specific=iot_VariableRef)
gen_iot_Not_Expression = Generalization(general=Expression, specific=iot_Not)
gen_iot_IntConstant_Expression = Generalization(general=Expression, specific=iot_IntConstant)
gen_iot_StringConstant_Expression = Generalization(general=Expression, specific=iot_StringConstant)

# Domain Model
domain_model = DomainModel(
    name="iot",
    types={iot_Etiqueta, iot_Estado, iot_Evento, iot_Transicion, iot_Model, iot_Dispositivo, iot_IfBlock, iot_Variable, iot_Or, Expression, iot_And, iot_AbstractElement, iot_IfStatement, AbstractElement, iot_Expression, iot_Plus, iot_Minus, iot_MulOrDiv, iot_Equality, iot_Comparison, iot_BoolConstant, iot_VariableRef, iot_Not, iot_IntConstant, iot_StringConstant},
    associations={superType2, etiquetas4, estados6, eventos8, transiciones10, dispositivos0, expression20, thenBlock21, elseBlock23, elementos26, expression29, left31, right33, elementos12, evento14, estado17, left46, right48, left51, right53, left56, right58, left61, left36, right38, left41, right43, variable68, right63, expression66},
    generalizations={gen_iot_Variable_AbstractElement, gen_iot_Expression_AbstractElement, gen_iot_Or_Expression, gen_iot_And_Expression, gen_iot_IfStatement_AbstractElement, gen_iot_Plus_Expression, gen_iot_Minus_Expression, gen_iot_MulOrDiv_Expression, gen_iot_Equality_Expression, gen_iot_Comparison_Expression, gen_iot_BoolConstant_Expression, gen_iot_VariableRef_Expression, gen_iot_Not_Expression, gen_iot_IntConstant_Expression, gen_iot_StringConstant_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)