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
componentmodel_Component = Class(name="componentmodel::Component", is_abstract=True)
componentmodel_Port = Class(name="componentmodel::Port", is_abstract=True)
componentmodel_PrimitiveComponent = Class(name="componentmodel::PrimitiveComponent")
Component = Class(name="Component")
componentmodel_Property = Class(name="componentmodel::Property", is_abstract=True)
componentmodel_CompositeComponent = Class(name="componentmodel::CompositeComponent")
componentmodel_NumericProperty = Class(name="componentmodel::NumericProperty")
Property_ = Class(name="Property")
componentmodel_EnumProperty = Class(name="componentmodel::EnumProperty")
componentmodel_InPort = Class(name="componentmodel::InPort")
Port = Class(name="Port")
componentmodel_OutPort = Class(name="componentmodel::OutPort")

# componentmodel_Component class attributes and methods
componentmodel_Component_name: Property = Property(name="name", type=StringType)
componentmodel_Component_description: Property = Property(name="description", type=StringType)
componentmodel_Component.attributes={componentmodel_Component_name, componentmodel_Component_description}

# componentmodel_Port class attributes and methods
componentmodel_Port_type: Property = Property(name="type", type=StringType)
componentmodel_Port_typePackage: Property = Property(name="typePackage", type=StringType)
componentmodel_Port_name: Property = Property(name="name", type=StringType)
componentmodel_Port_description: Property = Property(name="description", type=StringType)
componentmodel_Port.attributes={componentmodel_Port_type, componentmodel_Port_name, componentmodel_Port_typePackage, componentmodel_Port_description}

# componentmodel_PrimitiveComponent class attributes and methods

# Component class attributes and methods

# componentmodel_Property class attributes and methods
componentmodel_Property_description: Property = Property(name="description", type=StringType)
componentmodel_Property_name: Property = Property(name="name", type=StringType)
componentmodel_Property.attributes={componentmodel_Property_description, componentmodel_Property_name}

# componentmodel_CompositeComponent class attributes and methods

# componentmodel_NumericProperty class attributes and methods
componentmodel_NumericProperty_minValue: Property = Property(name="minValue", type=FloatType)
componentmodel_NumericProperty_maxValue: Property = Property(name="maxValue", type=FloatType)
componentmodel_NumericProperty_defaultValue: Property = Property(name="defaultValue", type=FloatType)
componentmodel_NumericProperty.attributes={componentmodel_NumericProperty_maxValue, componentmodel_NumericProperty_minValue, componentmodel_NumericProperty_defaultValue}

# Property class attributes and methods

# componentmodel_EnumProperty class attributes and methods
componentmodel_EnumProperty_literalValue: Property = Property(name="literalValue", type=StringType)
componentmodel_EnumProperty.attributes={componentmodel_EnumProperty_literalValue}

# componentmodel_InPort class attributes and methods

# Port class attributes and methods

# componentmodel_OutPort class attributes and methods

# Relationships
ports0: BinaryAssociation = BinaryAssociation(
    name="ports0",
    ends={
        Property(name="componentmodel_Port", type=componentmodel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="componentmodel_Component", type=componentmodel_Port, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
properties1: BinaryAssociation = BinaryAssociation(
    name="properties1",
    ends={
        Property(name="componentmodel_Property", type=componentmodel_PrimitiveComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentmodel_PrimitiveComponent", type=componentmodel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components2: BinaryAssociation = BinaryAssociation(
    name="components2",
    ends={
        Property(name="componentmodel_Component3", type=componentmodel_CompositeComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentmodel_CompositeComponent", type=componentmodel_Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
delegatesTo5: BinaryAssociation = BinaryAssociation(
    name="delegatesTo5",
    ends={
        Property(name="InPort", type=componentmodel_InPort, multiplicity=Multiplicity(1, 1)),
        Property(name="delegatesFrom", type=componentmodel_InPort, multiplicity=Multiplicity(0, 9999))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="OutPort", type=componentmodel_InPort, multiplicity=Multiplicity(1, 1)),
        Property(name="sink", type=componentmodel_OutPort, multiplicity=Multiplicity(0, 1))
    }
)
delegatesFrom8: BinaryAssociation = BinaryAssociation(
    name="delegatesFrom8",
    ends={
        Property(name="InPort9", type=componentmodel_InPort, multiplicity=Multiplicity(1, 1)),
        Property(name="delegatesTo", type=componentmodel_InPort, multiplicity=Multiplicity(0, 1))
    }
)
propagatesFrom11: BinaryAssociation = BinaryAssociation(
    name="propagatesFrom11",
    ends={
        Property(name="OutPort12", type=componentmodel_OutPort, multiplicity=Multiplicity(1, 1)),
        Property(name="propagatesTo", type=componentmodel_OutPort, multiplicity=Multiplicity(0, 1))
    }
)
sink13: BinaryAssociation = BinaryAssociation(
    name="sink13",
    ends={
        Property(name="InPort14", type=componentmodel_OutPort, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=componentmodel_InPort, multiplicity=Multiplicity(0, 9999))
    }
)
propagatesTo16: BinaryAssociation = BinaryAssociation(
    name="propagatesTo16",
    ends={
        Property(name="OutPort17", type=componentmodel_OutPort, multiplicity=Multiplicity(1, 1)),
        Property(name="propagatesFrom", type=componentmodel_OutPort, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_componentmodel_PrimitiveComponent_Component = Generalization(general=Component, specific=componentmodel_PrimitiveComponent)
gen_componentmodel_CompositeComponent_Component = Generalization(general=Component, specific=componentmodel_CompositeComponent)
gen_componentmodel_NumericProperty_Property = Generalization(general=Property_, specific=componentmodel_NumericProperty)
gen_componentmodel_EnumProperty_Property = Generalization(general=Property_, specific=componentmodel_EnumProperty)
gen_componentmodel_InPort_Port = Generalization(general=Port, specific=componentmodel_InPort)
gen_componentmodel_OutPort_Port = Generalization(general=Port, specific=componentmodel_OutPort)

# Domain Model
domain_model = DomainModel(
    name="componentmodel",
    types={componentmodel_Component, componentmodel_Port, componentmodel_PrimitiveComponent, Component, componentmodel_Property, componentmodel_CompositeComponent, componentmodel_NumericProperty, Property_, componentmodel_EnumProperty, componentmodel_InPort, Port, componentmodel_OutPort},
    associations={ports0, properties1, components2, delegatesTo5, source6, delegatesFrom8, propagatesFrom11, sink13, propagatesTo16},
    generalizations={gen_componentmodel_PrimitiveComponent_Component, gen_componentmodel_CompositeComponent_Component, gen_componentmodel_NumericProperty_Property, gen_componentmodel_EnumProperty_Property, gen_componentmodel_InPort_Port, gen_componentmodel_OutPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)