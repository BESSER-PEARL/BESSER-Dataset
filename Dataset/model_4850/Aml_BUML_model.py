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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="Red"),
			EnumerationLiteral(name="Black"),
			EnumerationLiteral(name="White"),
			EnumerationLiteral(name="Grey"),
			EnumerationLiteral(name="Green")
    }
)

# Classes
aml_Aml = Class(name="aml::Aml")
aml_AbstractElements = Class(name="aml::AbstractElements")
aml_MinMax = Class(name="aml::MinMax")
AbstractElements = Class(name="AbstractElements")
aml_TargetGroupFeature = Class(name="aml::TargetGroupFeature")
aml_ProductPUIDFeature = Class(name="aml::ProductPUIDFeature")
aml_MaxFeature = Class(name="aml::MaxFeature")
aml_Drive = Class(name="aml::Drive")
SuperEntity = Class(name="SuperEntity")
aml_FormFeature = Class(name="aml::FormFeature")
aml_Cable = Class(name="aml::Cable")
aml_ColorFeature = Class(name="aml::ColorFeature")
aml_NetWorkFeature = Class(name="aml::NetWorkFeature")
aml_TypeFeature = Class(name="aml::TypeFeature")
aml_Entity = Class(name="aml::Entity")
aml_SizeFeature = Class(name="aml::SizeFeature")
aml_SuperEntity = Class(name="aml::SuperEntity")
aml_SpeedFeature = Class(name="aml::SpeedFeature")
aml_LengthFeature = Class(name="aml::LengthFeature")
aml_PriceRule = Class(name="aml::PriceRule")
aml_Feature = Class(name="aml::Feature")

# aml_Aml class attributes and methods

# aml_AbstractElements class attributes and methods
aml_AbstractElements_name: Property = Property(name="name", type=StringType)
aml_AbstractElements.attributes={aml_AbstractElements_name}

# aml_MinMax class attributes and methods

# AbstractElements class attributes and methods

# aml_TargetGroupFeature class attributes and methods
aml_TargetGroupFeature_name: Property = Property(name="name", type=StringType)
aml_TargetGroupFeature_value: Property = Property(name="value", type=StringType)
aml_TargetGroupFeature.attributes={aml_TargetGroupFeature_value, aml_TargetGroupFeature_name}

# aml_ProductPUIDFeature class attributes and methods
aml_ProductPUIDFeature_name: Property = Property(name="name", type=StringType)
aml_ProductPUIDFeature_values: Property = Property(name="values", type=IntegerType)
aml_ProductPUIDFeature.attributes={aml_ProductPUIDFeature_name, aml_ProductPUIDFeature_values}

# aml_MaxFeature class attributes and methods
aml_MaxFeature_name: Property = Property(name="name", type=StringType)
aml_MaxFeature_value: Property = Property(name="value", type=IntegerType)
aml_MaxFeature.attributes={aml_MaxFeature_name, aml_MaxFeature_value}

# aml_Drive class attributes and methods

# SuperEntity class attributes and methods

# aml_FormFeature class attributes and methods
aml_FormFeature_name: Property = Property(name="name", type=StringType)
aml_FormFeature_value: Property = Property(name="value", type=IntegerType)
aml_FormFeature.attributes={aml_FormFeature_name, aml_FormFeature_value}

# aml_Cable class attributes and methods

# aml_ColorFeature class attributes and methods
aml_ColorFeature_name: Property = Property(name="name", type=StringType)
aml_ColorFeature_value: Property = Property(name="value", type=StringType)
aml_ColorFeature.attributes={aml_ColorFeature_name, aml_ColorFeature_value}

# aml_NetWorkFeature class attributes and methods
aml_NetWorkFeature_name: Property = Property(name="name", type=StringType)
aml_NetWorkFeature_value: Property = Property(name="value", type=StringType)
aml_NetWorkFeature.attributes={aml_NetWorkFeature_name, aml_NetWorkFeature_value}

# aml_TypeFeature class attributes and methods
aml_TypeFeature_name: Property = Property(name="name", type=StringType)
aml_TypeFeature_value: Property = Property(name="value", type=StringType)
aml_TypeFeature.attributes={aml_TypeFeature_value, aml_TypeFeature_name}

# aml_Entity class attributes and methods

# aml_SizeFeature class attributes and methods
aml_SizeFeature_name: Property = Property(name="name", type=StringType)
aml_SizeFeature_value: Property = Property(name="value", type=IntegerType)
aml_SizeFeature.attributes={aml_SizeFeature_value, aml_SizeFeature_name}

# aml_SuperEntity class attributes and methods

# aml_SpeedFeature class attributes and methods
aml_SpeedFeature_name: Property = Property(name="name", type=StringType)
aml_SpeedFeature_value: Property = Property(name="value", type=FloatType)
aml_SpeedFeature.attributes={aml_SpeedFeature_name, aml_SpeedFeature_value}

# aml_LengthFeature class attributes and methods
aml_LengthFeature_name: Property = Property(name="name", type=StringType)
aml_LengthFeature_value: Property = Property(name="value", type=FloatType)
aml_LengthFeature.attributes={aml_LengthFeature_name, aml_LengthFeature_value}

# aml_PriceRule class attributes and methods

# aml_Feature class attributes and methods
aml_Feature_name: Property = Property(name="name", type=StringType)
aml_Feature_value: Property = Property(name="value", type=StringType)
aml_Feature.attributes={aml_Feature_name, aml_Feature_value}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="aml_AbstractElements", type=aml_Aml, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Aml", type=aml_AbstractElements, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetGroupFeature1: BinaryAssociation = BinaryAssociation(
    name="targetGroupFeature1",
    ends={
        Property(name="aml_TargetGroupFeature", type=aml_MinMax, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MinMax", type=aml_TargetGroupFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
productPuidsFeature2: BinaryAssociation = BinaryAssociation(
    name="productPuidsFeature2",
    ends={
        Property(name="aml_ProductPUIDFeature", type=aml_MinMax, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MinMax3", type=aml_ProductPUIDFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxFeature4: BinaryAssociation = BinaryAssociation(
    name="maxFeature4",
    ends={
        Property(name="aml_MaxFeature", type=aml_MinMax, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MinMax5", type=aml_MaxFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
speedFeature9: BinaryAssociation = BinaryAssociation(
    name="speedFeature9",
    ends={
        Property(name="aml_SpeedFeature", type=aml_Drive, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Drive10", type=aml_SpeedFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formFeature11: BinaryAssociation = BinaryAssociation(
    name="formFeature11",
    ends={
        Property(name="aml_FormFeature", type=aml_Drive, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Drive12", type=aml_FormFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colorFeature13: BinaryAssociation = BinaryAssociation(
    name="colorFeature13",
    ends={
        Property(name="aml_ColorFeature", type=aml_Cable, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Cable", type=aml_ColorFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
networkFeature14: BinaryAssociation = BinaryAssociation(
    name="networkFeature14",
    ends={
        Property(name="aml_NetWorkFeature", type=aml_Cable, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Cable15", type=aml_NetWorkFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeFeature6: BinaryAssociation = BinaryAssociation(
    name="typeFeature6",
    ends={
        Property(name="aml_TypeFeature", type=aml_Drive, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Drive", type=aml_TypeFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sizeFeature7: BinaryAssociation = BinaryAssociation(
    name="sizeFeature7",
    ends={
        Property(name="aml_SizeFeature", type=aml_Drive, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Drive8", type=aml_SizeFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType22: BinaryAssociation = BinaryAssociation(
    name="superType22",
    ends={
        Property(name="aml_SuperEntity", type=aml_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Entity", type=aml_SuperEntity, multiplicity=Multiplicity(0, 1))
    }
)
features23: BinaryAssociation = BinaryAssociation(
    name="features23",
    ends={
        Property(name="aml_Feature25", type=aml_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Entity24", type=aml_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lengthFeature16: BinaryAssociation = BinaryAssociation(
    name="lengthFeature16",
    ends={
        Property(name="aml_LengthFeature", type=aml_Cable, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Cable17", type=aml_LengthFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType18: BinaryAssociation = BinaryAssociation(
    name="superType18",
    ends={
        Property(name="aml_MinMax19", type=aml_PriceRule, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_PriceRule", type=aml_MinMax, multiplicity=Multiplicity(0, 1))
    }
)
features20: BinaryAssociation = BinaryAssociation(
    name="features20",
    ends={
        Property(name="aml_Feature", type=aml_PriceRule, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_PriceRule21", type=aml_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_aml_MinMax_AbstractElements = Generalization(general=AbstractElements, specific=aml_MinMax)
gen_aml_Drive_SuperEntity = Generalization(general=SuperEntity, specific=aml_Drive)
gen_aml_Cable_SuperEntity = Generalization(general=SuperEntity, specific=aml_Cable)
gen_aml_Entity_AbstractElements = Generalization(general=AbstractElements, specific=aml_Entity)
gen_aml_SuperEntity_AbstractElements = Generalization(general=AbstractElements, specific=aml_SuperEntity)
gen_aml_PriceRule_AbstractElements = Generalization(general=AbstractElements, specific=aml_PriceRule)

# Domain Model
domain_model = DomainModel(
    name="aml",
    types={aml_Aml, aml_AbstractElements, aml_MinMax, AbstractElements, aml_TargetGroupFeature, aml_ProductPUIDFeature, aml_MaxFeature, aml_Drive, SuperEntity, aml_FormFeature, aml_Cable, aml_ColorFeature, aml_NetWorkFeature, aml_TypeFeature, aml_Entity, aml_SizeFeature, aml_SuperEntity, aml_SpeedFeature, aml_LengthFeature, aml_PriceRule, aml_Feature, Color},
    associations={elements0, targetGroupFeature1, productPuidsFeature2, maxFeature4, speedFeature9, formFeature11, colorFeature13, networkFeature14, typeFeature6, sizeFeature7, superType22, features23, lengthFeature16, superType18, features20},
    generalizations={gen_aml_MinMax_AbstractElements, gen_aml_Drive_SuperEntity, gen_aml_Cable_SuperEntity, gen_aml_Entity_AbstractElements, gen_aml_SuperEntity_AbstractElements, gen_aml_PriceRule_AbstractElements},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)