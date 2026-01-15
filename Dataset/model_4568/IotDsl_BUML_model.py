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
DefaultType: Enumeration = Enumeration(
    name="DefaultType",
    literals={
            EnumerationLiteral(name="Void"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Real"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Boolean")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="lesser"),
			EnumerationLiteral(name="leq"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="geq"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="neq")
    }
)

Protocol: Enumeration = Enumeration(
    name="Protocol",
    literals={
            EnumerationLiteral(name="ip"),
			EnumerationLiteral(name="zwave"),
			EnumerationLiteral(name="zigbee"),
			EnumerationLiteral(name="mqtt"),
			EnumerationLiteral(name="dds")
    }
)

Unit: Enumeration = Enumeration(
    name="Unit",
    literals={
            EnumerationLiteral(name="hour"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="sec"),
			EnumerationLiteral(name="milli")
    }
)

# Classes
iotdsl_IotModel = Class(name="iotdsl::IotModel")
iotdsl_Import = Class(name="iotdsl::Import")
iotdsl_Content = Class(name="iotdsl::Content", is_abstract=True)
iotdsl_Type = Class(name="iotdsl::Type", is_abstract=True)
Content = Class(name="Content")
iotdsl_PrimitiveType = Class(name="iotdsl::PrimitiveType")
Type = Class(name="Type")
iotdsl_DeclaredType = Class(name="iotdsl::DeclaredType", is_abstract=True)
iotdsl_Enumeration = Class(name="iotdsl::Enumeration")
DeclaredType = Class(name="DeclaredType")
iotdsl_EnumLiteral = Class(name="iotdsl::EnumLiteral")
iotdsl_Node = Class(name="iotdsl::Node", is_abstract=True)
iotdsl_Property = Class(name="iotdsl::Property")
Feature = Class(name="Feature")
iotdsl_Value = Class(name="iotdsl::Value")
iotdsl_Capability = Class(name="iotdsl::Capability", is_abstract=True)
iotdsl_Parameter = Class(name="iotdsl::Parameter")
iotdsl_Actuating = Class(name="iotdsl::Actuating")
Capability = Class(name="Capability")
iotdsl_Sensing = Class(name="iotdsl::Sensing")
iotdsl_Configuration = Class(name="iotdsl::Configuration")
iotdsl_NodeInstance = Class(name="iotdsl::NodeInstance")
iotdsl_CommunicationPath = Class(name="iotdsl::CommunicationPath")
iotdsl_Rule = Class(name="iotdsl::Rule")
iotdsl_Expression = Class(name="iotdsl::Expression", is_abstract=True)
iotdsl_Device = Class(name="iotdsl::Device")
Node = Class(name="Node")
iotdsl_Feature = Class(name="iotdsl::Feature", is_abstract=True)
iotdsl_Gateway = Class(name="iotdsl::Gateway")
Expression = Class(name="Expression")
iotdsl_EventOccurrence = Class(name="iotdsl::EventOccurrence")
iotdsl_Attribute = Class(name="iotdsl::Attribute")
iotdsl_AndExpression = Class(name="iotdsl::AndExpression")
iotdsl_TimingExpression = Class(name="iotdsl::TimingExpression", is_abstract=True)
iotdsl_WithinExpression = Class(name="iotdsl::WithinExpression")
TimingExpression = Class(name="TimingExpression")
iotdsl_Reaction = Class(name="iotdsl::Reaction")
iotdsl_Delay = Class(name="iotdsl::Delay")
iotdsl_NotExpression = Class(name="iotdsl::NotExpression")
iotdsl_BoolConstant = Class(name="iotdsl::BoolConstant")
iotdsl_AfterExpression = Class(name="iotdsl::AfterExpression")
iotdsl_StringConstant = Class(name="iotdsl::StringConstant")
Value = Class(name="Value")
iotdsl_IntConstant = Class(name="iotdsl::IntConstant")

# iotdsl_IotModel class attributes and methods
iotdsl_IotModel_name: Property = Property(name="name", type=StringType)
iotdsl_IotModel.attributes={iotdsl_IotModel_name}

# iotdsl_Import class attributes and methods
iotdsl_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
iotdsl_Import.attributes={iotdsl_Import_importedNamespace}

# iotdsl_Content class attributes and methods

# iotdsl_Type class attributes and methods
iotdsl_Type_name: Property = Property(name="name", type=StringType)
iotdsl_Type.attributes={iotdsl_Type_name}

# Content class attributes and methods

# iotdsl_PrimitiveType class attributes and methods

# Type class attributes and methods

# iotdsl_DeclaredType class attributes and methods

# iotdsl_Enumeration class attributes and methods

# DeclaredType class attributes and methods

# iotdsl_EnumLiteral class attributes and methods
iotdsl_EnumLiteral_name: Property = Property(name="name", type=StringType)
iotdsl_EnumLiteral.attributes={iotdsl_EnumLiteral_name}

# iotdsl_Node class attributes and methods

# iotdsl_Property class attributes and methods

# Feature class attributes and methods

# iotdsl_Value class attributes and methods

# iotdsl_Capability class attributes and methods

# iotdsl_Parameter class attributes and methods
iotdsl_Parameter_name: Property = Property(name="name", type=StringType)
iotdsl_Parameter.attributes={iotdsl_Parameter_name}

# iotdsl_Actuating class attributes and methods

# Capability class attributes and methods

# iotdsl_Sensing class attributes and methods

# iotdsl_Configuration class attributes and methods
iotdsl_Configuration_confname: Property = Property(name="confname", type=StringType)
iotdsl_Configuration.attributes={iotdsl_Configuration_confname}

# iotdsl_NodeInstance class attributes and methods
iotdsl_NodeInstance_name: Property = Property(name="name", type=StringType)
iotdsl_NodeInstance.attributes={iotdsl_NodeInstance_name}

# iotdsl_CommunicationPath class attributes and methods
iotdsl_CommunicationPath_protocol: Property = Property(name="protocol", type=StringType)
iotdsl_CommunicationPath.attributes={iotdsl_CommunicationPath_protocol}

# iotdsl_Rule class attributes and methods
iotdsl_Rule_name: Property = Property(name="name", type=StringType)
iotdsl_Rule.attributes={iotdsl_Rule_name}

# iotdsl_Expression class attributes and methods

# iotdsl_Device class attributes and methods

# Node class attributes and methods

# iotdsl_Feature class attributes and methods
iotdsl_Feature_name: Property = Property(name="name", type=StringType)
iotdsl_Feature.attributes={iotdsl_Feature_name}

# iotdsl_Gateway class attributes and methods

# Expression class attributes and methods

# iotdsl_EventOccurrence class attributes and methods
iotdsl_EventOccurrence_operator: Property = Property(name="operator", type=StringType)
iotdsl_EventOccurrence.attributes={iotdsl_EventOccurrence_operator}

# iotdsl_Attribute class attributes and methods
iotdsl_Attribute_name: Property = Property(name="name", type=StringType)
iotdsl_Attribute.attributes={iotdsl_Attribute_name}

# iotdsl_AndExpression class attributes and methods

# iotdsl_TimingExpression class attributes and methods

# iotdsl_WithinExpression class attributes and methods

# TimingExpression class attributes and methods

# iotdsl_Reaction class attributes and methods

# iotdsl_Delay class attributes and methods
iotdsl_Delay_time: Property = Property(name="time", type=IntegerType)
iotdsl_Delay_unit: Property = Property(name="unit", type=StringType)
iotdsl_Delay.attributes={iotdsl_Delay_unit, iotdsl_Delay_time}

# iotdsl_NotExpression class attributes and methods

# iotdsl_BoolConstant class attributes and methods
iotdsl_BoolConstant_value: Property = Property(name="value", type=StringType)
iotdsl_BoolConstant.attributes={iotdsl_BoolConstant_value}

# iotdsl_AfterExpression class attributes and methods

# iotdsl_StringConstant class attributes and methods
iotdsl_StringConstant_value: Property = Property(name="value", type=StringType)
iotdsl_StringConstant.attributes={iotdsl_StringConstant_value}

# Value class attributes and methods

# iotdsl_IntConstant class attributes and methods
iotdsl_IntConstant_value: Property = Property(name="value", type=IntegerType)
iotdsl_IntConstant.attributes={iotdsl_IntConstant_value}

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="iotdsl_Import", type=iotdsl_IotModel, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_IotModel", type=iotdsl_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content1: BinaryAssociation = BinaryAssociation(
    name="content1",
    ends={
        Property(name="iotdsl_Content", type=iotdsl_IotModel, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_IotModel2", type=iotdsl_Content, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literals3: BinaryAssociation = BinaryAssociation(
    name="literals3",
    ends={
        Property(name="iotdsl_EnumLiteral", type=iotdsl_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Enumeration", type=iotdsl_EnumLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value5: BinaryAssociation = BinaryAssociation(
    name="value5",
    ends={
        Property(name="iotdsl_Value", type=iotdsl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Property", type=iotdsl_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters6: BinaryAssociation = BinaryAssociation(
    name="parameters6",
    ends={
        Property(name="iotdsl_Parameter", type=iotdsl_Capability, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Capability", type=iotdsl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="iotdsl_Type", type=iotdsl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Parameter8", type=iotdsl_Type, multiplicity=Multiplicity(1, 1))
    }
)
nodes9: BinaryAssociation = BinaryAssociation(
    name="nodes9",
    ends={
        Property(name="iotdsl_NodeInstance", type=iotdsl_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Configuration", type=iotdsl_NodeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paths10: BinaryAssociation = BinaryAssociation(
    name="paths10",
    ends={
        Property(name="iotdsl_CommunicationPath", type=iotdsl_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Configuration11", type=iotdsl_CommunicationPath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="iotdsl_Type14", type=iotdsl_NodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_NodeInstance13", type=iotdsl_Type, multiplicity=Multiplicity(1, 1))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="iotdsl_NodeInstance17", type=iotdsl_CommunicationPath, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_CommunicationPath16", type=iotdsl_NodeInstance, multiplicity=Multiplicity(1, 1))
    }
)
taget18: BinaryAssociation = BinaryAssociation(
    name="taget18",
    ends={
        Property(name="iotdsl_NodeInstance20", type=iotdsl_CommunicationPath, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_CommunicationPath19", type=iotdsl_NodeInstance, multiplicity=Multiplicity(1, 1))
    }
)
triggers21: BinaryAssociation = BinaryAssociation(
    name="triggers21",
    ends={
        Property(name="iotdsl_Expression", type=iotdsl_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Rule", type=iotdsl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
features4: BinaryAssociation = BinaryAssociation(
    name="features4",
    ends={
        Property(name="iotdsl_Feature", type=iotdsl_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Device", type=iotdsl_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event24: BinaryAssociation = BinaryAssociation(
    name="event24",
    ends={
        Property(name="iotdsl_EventOccurrence", type=iotdsl_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_NotExpression", type=iotdsl_EventOccurrence, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instance25: BinaryAssociation = BinaryAssociation(
    name="instance25",
    ends={
        Property(name="iotdsl_NodeInstance27", type=iotdsl_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_EventOccurrence26", type=iotdsl_NodeInstance, multiplicity=Multiplicity(1, 1))
    }
)
capability28: BinaryAssociation = BinaryAssociation(
    name="capability28",
    ends={
        Property(name="iotdsl_Sensing", type=iotdsl_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_EventOccurrence29", type=iotdsl_Sensing, multiplicity=Multiplicity(1, 1))
    }
)
attributes30: BinaryAssociation = BinaryAssociation(
    name="attributes30",
    ends={
        Property(name="iotdsl_Attribute", type=iotdsl_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_EventOccurrence31", type=iotdsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value32: BinaryAssociation = BinaryAssociation(
    name="value32",
    ends={
        Property(name="iotdsl_Value34", type=iotdsl_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_EventOccurrence33", type=iotdsl_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instance35: BinaryAssociation = BinaryAssociation(
    name="instance35",
    ends={
        Property(name="iotdsl_NodeInstance37", type=iotdsl_Reaction, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Reaction36", type=iotdsl_NodeInstance, multiplicity=Multiplicity(1, 1))
    }
)
capability38: BinaryAssociation = BinaryAssociation(
    name="capability38",
    ends={
        Property(name="iotdsl_Actuating", type=iotdsl_Reaction, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Reaction39", type=iotdsl_Actuating, multiplicity=Multiplicity(1, 1))
    }
)
attributes40: BinaryAssociation = BinaryAssociation(
    name="attributes40",
    ends={
        Property(name="iotdsl_Attribute42", type=iotdsl_Reaction, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Reaction41", type=iotdsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left43: BinaryAssociation = BinaryAssociation(
    name="left43",
    ends={
        Property(name="iotdsl_Expression44", type=iotdsl_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_AndExpression", type=iotdsl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right45: BinaryAssociation = BinaryAssociation(
    name="right45",
    ends={
        Property(name="iotdsl_Expression47", type=iotdsl_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_AndExpression46", type=iotdsl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
following48: BinaryAssociation = BinaryAssociation(
    name="following48",
    ends={
        Property(name="iotdsl_Expression49", type=iotdsl_TimingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_TimingExpression", type=iotdsl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
preceding50: BinaryAssociation = BinaryAssociation(
    name="preceding50",
    ends={
        Property(name="iotdsl_Expression52", type=iotdsl_TimingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_TimingExpression51", type=iotdsl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
delay53: BinaryAssociation = BinaryAssociation(
    name="delay53",
    ends={
        Property(name="iotdsl_Delay", type=iotdsl_WithinExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_WithinExpression", type=iotdsl_Delay, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reactions22: BinaryAssociation = BinaryAssociation(
    name="reactions22",
    ends={
        Property(name="iotdsl_Reaction", type=iotdsl_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Rule23", type=iotdsl_Reaction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_iotdsl_Type_Content = Generalization(general=Content, specific=iotdsl_Type)
gen_iotdsl_PrimitiveType_Type = Generalization(general=Type, specific=iotdsl_PrimitiveType)
gen_iotdsl_DeclaredType_Type = Generalization(general=Type, specific=iotdsl_DeclaredType)
gen_iotdsl_Enumeration_DeclaredType = Generalization(general=DeclaredType, specific=iotdsl_Enumeration)
gen_iotdsl_Node_DeclaredType = Generalization(general=DeclaredType, specific=iotdsl_Node)
gen_iotdsl_Property_Feature = Generalization(general=Feature, specific=iotdsl_Property)
gen_iotdsl_Capability_Feature = Generalization(general=Feature, specific=iotdsl_Capability)
gen_iotdsl_Actuating_Capability = Generalization(general=Capability, specific=iotdsl_Actuating)
gen_iotdsl_Sensing_Capability = Generalization(general=Capability, specific=iotdsl_Sensing)
gen_iotdsl_Configuration_Content = Generalization(general=Content, specific=iotdsl_Configuration)
gen_iotdsl_Rule_Content = Generalization(general=Content, specific=iotdsl_Rule)
gen_iotdsl_Device_Node = Generalization(general=Node, specific=iotdsl_Device)
gen_iotdsl_Gateway_Node = Generalization(general=Node, specific=iotdsl_Gateway)
gen_iotdsl_NotExpression_Expression = Generalization(general=Expression, specific=iotdsl_NotExpression)
gen_iotdsl_EventOccurrence_Expression = Generalization(general=Expression, specific=iotdsl_EventOccurrence)
gen_iotdsl_AndExpression_Expression = Generalization(general=Expression, specific=iotdsl_AndExpression)
gen_iotdsl_TimingExpression_Expression = Generalization(general=Expression, specific=iotdsl_TimingExpression)
gen_iotdsl_WithinExpression_TimingExpression = Generalization(general=TimingExpression, specific=iotdsl_WithinExpression)
gen_iotdsl_BoolConstant_Value = Generalization(general=Value, specific=iotdsl_BoolConstant)
gen_iotdsl_AfterExpression_TimingExpression = Generalization(general=TimingExpression, specific=iotdsl_AfterExpression)
gen_iotdsl_StringConstant_Value = Generalization(general=Value, specific=iotdsl_StringConstant)
gen_iotdsl_IntConstant_Value = Generalization(general=Value, specific=iotdsl_IntConstant)

# Domain Model
domain_model = DomainModel(
    name="iotdsl",
    types={iotdsl_IotModel, iotdsl_Import, iotdsl_Content, iotdsl_Type, Content, iotdsl_PrimitiveType, Type, iotdsl_DeclaredType, iotdsl_Enumeration, DeclaredType, iotdsl_EnumLiteral, iotdsl_Node, iotdsl_Property, Feature, iotdsl_Value, iotdsl_Capability, iotdsl_Parameter, iotdsl_Actuating, Capability, iotdsl_Sensing, iotdsl_Configuration, iotdsl_NodeInstance, iotdsl_CommunicationPath, iotdsl_Rule, iotdsl_Expression, iotdsl_Device, Node, iotdsl_Feature, iotdsl_Gateway, Expression, iotdsl_EventOccurrence, iotdsl_Attribute, iotdsl_AndExpression, iotdsl_TimingExpression, iotdsl_WithinExpression, TimingExpression, iotdsl_Reaction, iotdsl_Delay, iotdsl_NotExpression, iotdsl_BoolConstant, iotdsl_AfterExpression, iotdsl_StringConstant, Value, iotdsl_IntConstant, DefaultType, Operator, Protocol, Unit},
    associations={imports0, content1, literals3, value5, parameters6, type7, nodes9, paths10, type12, source15, taget18, triggers21, features4, event24, instance25, capability28, attributes30, value32, instance35, capability38, attributes40, left43, right45, following48, preceding50, delay53, reactions22},
    generalizations={gen_iotdsl_Type_Content, gen_iotdsl_PrimitiveType_Type, gen_iotdsl_DeclaredType_Type, gen_iotdsl_Enumeration_DeclaredType, gen_iotdsl_Node_DeclaredType, gen_iotdsl_Property_Feature, gen_iotdsl_Capability_Feature, gen_iotdsl_Actuating_Capability, gen_iotdsl_Sensing_Capability, gen_iotdsl_Configuration_Content, gen_iotdsl_Rule_Content, gen_iotdsl_Device_Node, gen_iotdsl_Gateway_Node, gen_iotdsl_NotExpression_Expression, gen_iotdsl_EventOccurrence_Expression, gen_iotdsl_AndExpression_Expression, gen_iotdsl_TimingExpression_Expression, gen_iotdsl_WithinExpression_TimingExpression, gen_iotdsl_BoolConstant_Value, gen_iotdsl_AfterExpression_TimingExpression, gen_iotdsl_StringConstant_Value, gen_iotdsl_IntConstant_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)