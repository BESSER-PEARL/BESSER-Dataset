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
IO: Enumeration = Enumeration(
    name="IO",
    literals={
            EnumerationLiteral(name="INPUT"),
			EnumerationLiteral(name="OUTPUT")
    }
)

TYPE: Enumeration = Enumeration(
    name="TYPE",
    literals={
            EnumerationLiteral(name="ANALOG"),
			EnumerationLiteral(name="DIGITAL")
    }
)

# Classes
ardlers_Program = Class(name="ardlers::Program")
ardlers_Library = Class(name="ardlers::Library")
ardlers_SensorImport = Class(name="ardlers::SensorImport")
ardlers_EObject = Class(name="ardlers::EObject")
ardlers_BoardDefinition = Class(name="ardlers::BoardDefinition")
ardlers_Parenthesis = Class(name="ardlers::Parenthesis")
Expression = Class(name="Expression")
ardlers_Value = Class(name="ardlers::Value")
Parenthesis = Class(name="Parenthesis")
ardlers_Attribute = Class(name="ardlers::Attribute")
Value = Class(name="Value")
ardlers_Node = Class(name="ardlers::Node")
ardlers_Component = Class(name="ardlers::Component")
ardlers_Delta = Class(name="ardlers::Delta")
ardlers_NumberLiteral = Class(name="ardlers::NumberLiteral")
ardlers_State = Class(name="ardlers::State")
ardlers_Rule = Class(name="ardlers::Rule")
ardlers_Or = Class(name="ardlers::Or")
ardlers_RuleBody = Class(name="ardlers::RuleBody")
ardlers_Expression = Class(name="ardlers::Expression")
Or = Class(name="Or")
ardlers_Rate = Class(name="ardlers::Rate")
ardlers_Map = Class(name="ardlers::Map")
ardlers_Range = Class(name="ardlers::Range")
ardlers_Assignment = Class(name="ardlers::Assignment")
ardlers_ComponentBody = Class(name="ardlers::ComponentBody")
ardlers_Smoothing = Class(name="ardlers::Smoothing")
ardlers_And = Class(name="ardlers::And")
ardlers_Comparison = Class(name="ardlers::Comparison")
ardlers_Exp = Class(name="ardlers::Exp")
ardlers_Factor = Class(name="ardlers::Factor")

# ardlers_Program class attributes and methods

# ardlers_Library class attributes and methods

# ardlers_SensorImport class attributes and methods
ardlers_SensorImport_name: Property = Property(name="name", type=StringType)
ardlers_SensorImport.attributes={ardlers_SensorImport_name}

# ardlers_EObject class attributes and methods

# ardlers_BoardDefinition class attributes and methods
ardlers_BoardDefinition_name: Property = Property(name="name", type=StringType)
ardlers_BoardDefinition_di: Property = Property(name="di", type=IntegerType)
ardlers_BoardDefinition_do: Property = Property(name="do", type=IntegerType)
ardlers_BoardDefinition_ain: Property = Property(name="ain", type=IntegerType)
ardlers_BoardDefinition_aout: Property = Property(name="aout", type=IntegerType)
ardlers_BoardDefinition.attributes={ardlers_BoardDefinition_aout, ardlers_BoardDefinition_name, ardlers_BoardDefinition_ain, ardlers_BoardDefinition_do, ardlers_BoardDefinition_di}

# ardlers_Parenthesis class attributes and methods

# Expression class attributes and methods

# ardlers_Value class attributes and methods

# Parenthesis class attributes and methods

# ardlers_Attribute class attributes and methods

# Value class attributes and methods

# ardlers_Node class attributes and methods
ardlers_Node_name: Property = Property(name="name", type=StringType)
ardlers_Node.attributes={ardlers_Node_name}

# ardlers_Component class attributes and methods
ardlers_Component_name: Property = Property(name="name", type=StringType)
ardlers_Component.attributes={ardlers_Component_name}

# ardlers_Delta class attributes and methods

# ardlers_NumberLiteral class attributes and methods
ardlers_NumberLiteral_float: Property = Property(name="float", type=StringType)
ardlers_NumberLiteral_int: Property = Property(name="int", type=IntegerType)
ardlers_NumberLiteral.attributes={ardlers_NumberLiteral_int, ardlers_NumberLiteral_float}

# ardlers_State class attributes and methods
ardlers_State_value: Property = Property(name="value", type=StringType)
ardlers_State.attributes={ardlers_State_value}

# ardlers_Rule class attributes and methods
ardlers_Rule_type: Property = Property(name="type", type=StringType)
ardlers_Rule.attributes={ardlers_Rule_type}

# ardlers_Or class attributes and methods
ardlers_Or_operator: Property = Property(name="operator", type=StringType)
ardlers_Or.attributes={ardlers_Or_operator}

# ardlers_RuleBody class attributes and methods

# ardlers_Expression class attributes and methods

# Or class attributes and methods

# ardlers_Rate class attributes and methods
ardlers_Rate_value: Property = Property(name="value", type=IntegerType)
ardlers_Rate.attributes={ardlers_Rate_value}

# ardlers_Map class attributes and methods

# ardlers_Range class attributes and methods
ardlers_Range_low: Property = Property(name="low", type=FloatType)
ardlers_Range_high: Property = Property(name="high", type=FloatType)
ardlers_Range.attributes={ardlers_Range_high, ardlers_Range_low}

# ardlers_Assignment class attributes and methods

# ardlers_ComponentBody class attributes and methods
ardlers_ComponentBody_io: Property = Property(name="io", type=StringType)
ardlers_ComponentBody_type: Property = Property(name="type", type=StringType)
ardlers_ComponentBody_pinned: Property = Property(name="pinned", type=StringType)
ardlers_ComponentBody_pin: Property = Property(name="pin", type=IntegerType)
ardlers_ComponentBody.attributes={ardlers_ComponentBody_pinned, ardlers_ComponentBody_pin, ardlers_ComponentBody_io, ardlers_ComponentBody_type}

# ardlers_Smoothing class attributes and methods
ardlers_Smoothing_value: Property = Property(name="value", type=FloatType)
ardlers_Smoothing.attributes={ardlers_Smoothing_value}

# ardlers_And class attributes and methods

# ardlers_Comparison class attributes and methods

# ardlers_Exp class attributes and methods

# ardlers_Factor class attributes and methods

# Relationships
board0: BinaryAssociation = BinaryAssociation(
    name="board0",
    ends={
        Property(name="ardlers_Library", type=ardlers_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Program", type=ardlers_Library, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensorsImports1: BinaryAssociation = BinaryAssociation(
    name="sensorsImports1",
    ends={
        Property(name="ardlers_SensorImport", type=ardlers_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Program2", type=ardlers_SensorImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program3: BinaryAssociation = BinaryAssociation(
    name="program3",
    ends={
        Property(name="ardlers_EObject", type=ardlers_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Program4", type=ardlers_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitions5: BinaryAssociation = BinaryAssociation(
    name="definitions5",
    ends={
        Property(name="ardlers_BoardDefinition", type=ardlers_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Program6", type=ardlers_BoardDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boardtype7: BinaryAssociation = BinaryAssociation(
    name="boardtype7",
    ends={
        Property(name="ardlers_BoardDefinition9", type=ardlers_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Library8", type=ardlers_BoardDefinition, multiplicity=Multiplicity(0, 1))
    }
)
sub18: BinaryAssociation = BinaryAssociation(
    name="sub18",
    ends={
        Property(name="ardlers_Or19", type=ardlers_Parenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Parenthesis", type=ardlers_Or, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name20: BinaryAssociation = BinaryAssociation(
    name="name20",
    ends={
        Property(name="ardlers_Node", type=ardlers_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Attribute", type=ardlers_Node, multiplicity=Multiplicity(0, 1))
    }
)
component21: BinaryAssociation = BinaryAssociation(
    name="component21",
    ends={
        Property(name="ardlers_Component", type=ardlers_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Attribute22", type=ardlers_Component, multiplicity=Multiplicity(0, 1))
    }
)
attr23: BinaryAssociation = BinaryAssociation(
    name="attr23",
    ends={
        Property(name="ardlers_Attribute24", type=ardlers_Delta, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Delta", type=ardlers_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition10: BinaryAssociation = BinaryAssociation(
    name="condition10",
    ends={
        Property(name="ardlers_Or", type=ardlers_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Rule", type=ardlers_Or, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body11: BinaryAssociation = BinaryAssociation(
    name="body11",
    ends={
        Property(name="ardlers_RuleBody", type=ardlers_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Rule12", type=ardlers_RuleBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left14: BinaryAssociation = BinaryAssociation(
    name="left14",
    ends={
        Property(name="ardlers_Or15", type=ardlers_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Or13", type=ardlers_Or, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right16: BinaryAssociation = BinaryAssociation(
    name="right16",
    ends={
        Property(name="ardlers_Expression", type=ardlers_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Or17", type=ardlers_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rate44: BinaryAssociation = BinaryAssociation(
    name="rate44",
    ends={
        Property(name="ardlers_Rate", type=ardlers_ComponentBody, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_ComponentBody45", type=ardlers_Rate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
map46: BinaryAssociation = BinaryAssociation(
    name="map46",
    ends={
        Property(name="ardlers_Map", type=ardlers_ComponentBody, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_ComponentBody47", type=ardlers_Map, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in48: BinaryAssociation = BinaryAssociation(
    name="in48",
    ends={
        Property(name="ardlers_Range", type=ardlers_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Map49", type=ardlers_Range, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
out50: BinaryAssociation = BinaryAssociation(
    name="out50",
    ends={
        Property(name="ardlers_Range52", type=ardlers_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Map51", type=ardlers_Range, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment25: BinaryAssociation = BinaryAssociation(
    name="assignment25",
    ends={
        Property(name="ardlers_Assignment", type=ardlers_RuleBody, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_RuleBody26", type=ardlers_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute27: BinaryAssociation = BinaryAssociation(
    name="attribute27",
    ends={
        Property(name="ardlers_Attribute29", type=ardlers_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Assignment28", type=ardlers_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value30: BinaryAssociation = BinaryAssociation(
    name="value30",
    ends={
        Property(name="ardlers_EObject32", type=ardlers_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Assignment31", type=ardlers_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boardType33: BinaryAssociation = BinaryAssociation(
    name="boardType33",
    ends={
        Property(name="ardlers_BoardDefinition35", type=ardlers_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Node34", type=ardlers_BoardDefinition, multiplicity=Multiplicity(0, 1))
    }
)
components36: BinaryAssociation = BinaryAssociation(
    name="components36",
    ends={
        Property(name="ardlers_Component38", type=ardlers_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Node37", type=ardlers_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensor39: BinaryAssociation = BinaryAssociation(
    name="sensor39",
    ends={
        Property(name="ardlers_SensorImport41", type=ardlers_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Component40", type=ardlers_SensorImport, multiplicity=Multiplicity(0, 1))
    }
)
properties42: BinaryAssociation = BinaryAssociation(
    name="properties42",
    ends={
        Property(name="ardlers_ComponentBody", type=ardlers_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ardlers_Component43", type=ardlers_ComponentBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_ardlers_Expression_Or = Generalization(general=Or, specific=ardlers_Expression)
gen_ardlers_Parenthesis_Expression = Generalization(general=Expression, specific=ardlers_Parenthesis)
gen_ardlers_Value_Parenthesis = Generalization(general=Parenthesis, specific=ardlers_Value)
gen_ardlers_Attribute_Value = Generalization(general=Value, specific=ardlers_Attribute)
gen_ardlers_Delta_Value = Generalization(general=Value, specific=ardlers_Delta)
gen_ardlers_NumberLiteral_Value = Generalization(general=Value, specific=ardlers_NumberLiteral)
gen_ardlers_And_Expression = Generalization(general=Expression, specific=ardlers_And)
gen_ardlers_Comparison_Expression = Generalization(general=Expression, specific=ardlers_Comparison)
gen_ardlers_Exp_Expression = Generalization(general=Expression, specific=ardlers_Exp)
gen_ardlers_Factor_Expression = Generalization(general=Expression, specific=ardlers_Factor)

# Domain Model
domain_model = DomainModel(
    name="ardlers",
    types={ardlers_Program, ardlers_Library, ardlers_SensorImport, ardlers_EObject, ardlers_BoardDefinition, ardlers_Parenthesis, Expression, ardlers_Value, Parenthesis, ardlers_Attribute, Value, ardlers_Node, ardlers_Component, ardlers_Delta, ardlers_NumberLiteral, ardlers_State, ardlers_Rule, ardlers_Or, ardlers_RuleBody, ardlers_Expression, Or, ardlers_Rate, ardlers_Map, ardlers_Range, ardlers_Assignment, ardlers_ComponentBody, ardlers_Smoothing, ardlers_And, ardlers_Comparison, ardlers_Exp, ardlers_Factor, IO, TYPE},
    associations={board0, sensorsImports1, program3, definitions5, boardtype7, sub18, name20, component21, attr23, condition10, body11, left14, right16, rate44, map46, in48, out50, assignment25, attribute27, value30, boardType33, components36, sensor39, properties42},
    generalizations={gen_ardlers_Expression_Or, gen_ardlers_Parenthesis_Expression, gen_ardlers_Value_Parenthesis, gen_ardlers_Attribute_Value, gen_ardlers_Delta_Value, gen_ardlers_NumberLiteral_Value, gen_ardlers_And_Expression, gen_ardlers_Comparison_Expression, gen_ardlers_Exp_Expression, gen_ardlers_Factor_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)