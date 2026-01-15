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
lSGL_Generator = Class(name="lSGL::Generator")
lSGL_Type = Class(name="lSGL::Type")
lSGL_Projection = Class(name="lSGL::Projection")
lSGL_Model = Class(name="lSGL::Model")
lSGL_Config = Class(name="lSGL::Config")
lSGL_ConfigProperty = Class(name="lSGL::ConfigProperty")
lSGL_Enum = Class(name="lSGL::Enum")
Type = Class(name="Type")
lSGL_EnumItem = Class(name="lSGL::EnumItem")
lSGL_Entity = Class(name="lSGL::Entity")
lSGL_AttributeType = Class(name="lSGL::AttributeType")
lSGL_Annotation = Class(name="lSGL::Annotation")
lSGL_GeneratorAnnotation = Class(name="lSGL::GeneratorAnnotation")
lSGL_Attribute = Class(name="lSGL::Attribute")
lSGL_GeneratorConfig = Class(name="lSGL::GeneratorConfig")

# lSGL_Generator class attributes and methods
lSGL_Generator_name: Property = Property(name="name", type=StringType)
lSGL_Generator.attributes={lSGL_Generator_name}

# lSGL_Type class attributes and methods
lSGL_Type_name: Property = Property(name="name", type=StringType)
lSGL_Type.attributes={lSGL_Type_name}

# lSGL_Projection class attributes and methods
lSGL_Projection_excluding: Property = Property(name="excluding", type=BooleanType)
lSGL_Projection_name: Property = Property(name="name", type=StringType)
lSGL_Projection.attributes={lSGL_Projection_excluding, lSGL_Projection_name}

# lSGL_Model class attributes and methods

# lSGL_Config class attributes and methods
lSGL_Config_name: Property = Property(name="name", type=StringType)
lSGL_Config.attributes={lSGL_Config_name}

# lSGL_ConfigProperty class attributes and methods
lSGL_ConfigProperty_name: Property = Property(name="name", type=StringType)
lSGL_ConfigProperty_value: Property = Property(name="value", type=StringType)
lSGL_ConfigProperty.attributes={lSGL_ConfigProperty_value, lSGL_ConfigProperty_name}

# lSGL_Enum class attributes and methods

# Type class attributes and methods

# lSGL_EnumItem class attributes and methods
lSGL_EnumItem_name: Property = Property(name="name", type=StringType)
lSGL_EnumItem_value: Property = Property(name="value", type=StringType)
lSGL_EnumItem.attributes={lSGL_EnumItem_value, lSGL_EnumItem_name}

# lSGL_Entity class attributes and methods

# lSGL_AttributeType class attributes and methods
lSGL_AttributeType_nullable: Property = Property(name="nullable", type=BooleanType)
lSGL_AttributeType_typeName: Property = Property(name="typeName", type=StringType)
lSGL_AttributeType.attributes={lSGL_AttributeType_nullable, lSGL_AttributeType_typeName}

# lSGL_Annotation class attributes and methods
lSGL_Annotation_name: Property = Property(name="name", type=StringType)
lSGL_Annotation_value: Property = Property(name="value", type=StringType)
lSGL_Annotation.attributes={lSGL_Annotation_name, lSGL_Annotation_value}

# lSGL_GeneratorAnnotation class attributes and methods

# lSGL_Attribute class attributes and methods
lSGL_Attribute_isMap: Property = Property(name="isMap", type=BooleanType)
lSGL_Attribute_isList: Property = Property(name="isList", type=BooleanType)
lSGL_Attribute_isArray: Property = Property(name="isArray", type=BooleanType)
lSGL_Attribute_name: Property = Property(name="name", type=StringType)
lSGL_Attribute.attributes={lSGL_Attribute_isArray, lSGL_Attribute_name, lSGL_Attribute_isList, lSGL_Attribute_isMap}

# lSGL_GeneratorConfig class attributes and methods
lSGL_GeneratorConfig_cfgName: Property = Property(name="cfgName", type=StringType)
lSGL_GeneratorConfig_values: Property = Property(name="values", type=StringType)
lSGL_GeneratorConfig.attributes={lSGL_GeneratorConfig_values, lSGL_GeneratorConfig_cfgName}

# Relationships
generators0: BinaryAssociation = BinaryAssociation(
    name="generators0",
    ends={
        Property(name="lSGL_Generator", type=lSGL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Model", type=lSGL_Generator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="lSGL_Type", type=lSGL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Model2", type=lSGL_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projections3: BinaryAssociation = BinaryAssociation(
    name="projections3",
    ends={
        Property(name="lSGL_Projection", type=lSGL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Model4", type=lSGL_Projection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configs7: BinaryAssociation = BinaryAssociation(
    name="configs7",
    ends={
        Property(name="lSGL_Config", type=lSGL_Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Generator8", type=lSGL_Config, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="lSGL_ConfigProperty11", type=lSGL_Config, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Config10", type=lSGL_ConfigProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties5: BinaryAssociation = BinaryAssociation(
    name="properties5",
    ends={
        Property(name="lSGL_ConfigProperty", type=lSGL_Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Generator6", type=lSGL_ConfigProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items12: BinaryAssociation = BinaryAssociation(
    name="items12",
    ends={
        Property(name="lSGL_EnumItem", type=lSGL_Enum, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Enum", type=lSGL_EnumItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="lSGL_Type20", type=lSGL_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_AttributeType", type=lSGL_Type, multiplicity=Multiplicity(0, 1))
    }
)
annotations21: BinaryAssociation = BinaryAssociation(
    name="annotations21",
    ends={
        Property(name="lSGL_Annotation", type=lSGL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Attribute22", type=lSGL_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key23: BinaryAssociation = BinaryAssociation(
    name="key23",
    ends={
        Property(name="lSGL_AttributeType25", type=lSGL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Attribute24", type=lSGL_AttributeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="lSGL_AttributeType28", type=lSGL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Attribute27", type=lSGL_AttributeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generatorAnnotations13: BinaryAssociation = BinaryAssociation(
    name="generatorAnnotations13",
    ends={
        Property(name="lSGL_GeneratorAnnotation", type=lSGL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Entity", type=lSGL_GeneratorAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass15: BinaryAssociation = BinaryAssociation(
    name="superClass15",
    ends={
        Property(name="lSGL_Entity16", type=lSGL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Entity14", type=lSGL_Entity, multiplicity=Multiplicity(0, 1))
    }
)
attributes17: BinaryAssociation = BinaryAssociation(
    name="attributes17",
    ends={
        Property(name="lSGL_Attribute", type=lSGL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Entity18", type=lSGL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configItem32: BinaryAssociation = BinaryAssociation(
    name="configItem32",
    ends={
        Property(name="lSGL_Config34", type=lSGL_GeneratorAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_GeneratorAnnotation33", type=lSGL_Config, multiplicity=Multiplicity(0, 1))
    }
)
customConfig35: BinaryAssociation = BinaryAssociation(
    name="customConfig35",
    ends={
        Property(name="lSGL_GeneratorConfig", type=lSGL_GeneratorAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_GeneratorAnnotation36", type=lSGL_GeneratorConfig, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generatorAnnotations37: BinaryAssociation = BinaryAssociation(
    name="generatorAnnotations37",
    ends={
        Property(name="lSGL_GeneratorAnnotation39", type=lSGL_Projection, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Projection38", type=lSGL_GeneratorAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity40: BinaryAssociation = BinaryAssociation(
    name="entity40",
    ends={
        Property(name="lSGL_Entity42", type=lSGL_Projection, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Projection41", type=lSGL_Entity, multiplicity=Multiplicity(0, 1))
    }
)
attributes43: BinaryAssociation = BinaryAssociation(
    name="attributes43",
    ends={
        Property(name="lSGL_Attribute45", type=lSGL_Projection, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_Projection44", type=lSGL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generator29: BinaryAssociation = BinaryAssociation(
    name="generator29",
    ends={
        Property(name="lSGL_Generator31", type=lSGL_GeneratorAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="lSGL_GeneratorAnnotation30", type=lSGL_Generator, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_lSGL_Enum_Type = Generalization(general=Type, specific=lSGL_Enum)
gen_lSGL_Entity_Type = Generalization(general=Type, specific=lSGL_Entity)

# Domain Model
domain_model = DomainModel(
    name="lSGL",
    types={lSGL_Generator, lSGL_Type, lSGL_Projection, lSGL_Model, lSGL_Config, lSGL_ConfigProperty, lSGL_Enum, Type, lSGL_EnumItem, lSGL_Entity, lSGL_AttributeType, lSGL_Annotation, lSGL_GeneratorAnnotation, lSGL_Attribute, lSGL_GeneratorConfig},
    associations={generators0, types1, projections3, configs7, properties9, properties5, items12, type19, annotations21, key23, type26, generatorAnnotations13, superClass15, attributes17, configItem32, customConfig35, generatorAnnotations37, entity40, attributes43, generator29},
    generalizations={gen_lSGL_Enum_Type, gen_lSGL_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)