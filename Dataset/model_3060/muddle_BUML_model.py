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
muddle_Muddle = Class(name="muddle::Muddle")
muddle_Type = Class(name="muddle::Type", is_abstract=True)
muddle_MuddleElement = Class(name="muddle::MuddleElement")
muddle_Slot = Class(name="muddle::Slot")
muddle_MuddleElementType = Class(name="muddle::MuddleElementType")
muddle_MuddleElementStyle = Class(name="muddle::MuddleElementStyle")
muddle_Feature = Class(name="muddle::Feature")
muddle_LinkElementType = Class(name="muddle::LinkElementType")
MuddleElementType = Class(name="MuddleElementType")
Type = Class(name="Type")
muddle_PrimitiveType = Class(name="muddle::PrimitiveType", is_abstract=True)
muddle_IntegerType = Class(name="muddle::IntegerType")
PrimitiveType = Class(name="PrimitiveType")
muddle_StringType = Class(name="muddle::StringType")
muddle_BooleanType = Class(name="muddle::BooleanType")
muddle_RealType = Class(name="muddle::RealType")

# muddle_Muddle class attributes and methods

# muddle_Type class attributes and methods
muddle_Type_name: Property = Property(name="name", type=StringType)
muddle_Type.attributes={muddle_Type_name}

# muddle_MuddleElement class attributes and methods
muddle_MuddleElement_id: Property = Property(name="id", type=StringType)
muddle_MuddleElement.attributes={muddle_MuddleElement_id}

# muddle_Slot class attributes and methods
muddle_Slot_values: Property = Property(name="values", type=StringType)
muddle_Slot.attributes={muddle_Slot_values}

# muddle_MuddleElementType class attributes and methods

# muddle_MuddleElementStyle class attributes and methods
muddle_MuddleElementStyle_color: Property = Property(name="color", type=StringType)
muddle_MuddleElementStyle_shape: Property = Property(name="shape", type=StringType)
muddle_MuddleElementStyle_width: Property = Property(name="width", type=FloatType)
muddle_MuddleElementStyle_height: Property = Property(name="height", type=FloatType)
muddle_MuddleElementStyle_borderWidth: Property = Property(name="borderWidth", type=FloatType)
muddle_MuddleElementStyle_labelFontSize: Property = Property(name="labelFontSize", type=IntegerType)
muddle_MuddleElementStyle_x: Property = Property(name="x", type=FloatType)
muddle_MuddleElementStyle_y: Property = Property(name="y", type=FloatType)
muddle_MuddleElementStyle.attributes={muddle_MuddleElementStyle_color, muddle_MuddleElementStyle_height, muddle_MuddleElementStyle_borderWidth, muddle_MuddleElementStyle_shape, muddle_MuddleElementStyle_x, muddle_MuddleElementStyle_labelFontSize, muddle_MuddleElementStyle_width, muddle_MuddleElementStyle_y}

# muddle_Feature class attributes and methods
muddle_Feature_many: Property = Property(name="many", type=BooleanType)
muddle_Feature_primary: Property = Property(name="primary", type=BooleanType)
muddle_Feature_runtime: Property = Property(name="runtime", type=BooleanType)
muddle_Feature_name: Property = Property(name="name", type=StringType)
muddle_Feature.attributes={muddle_Feature_runtime, muddle_Feature_many, muddle_Feature_primary, muddle_Feature_name}

# muddle_LinkElementType class attributes and methods

# MuddleElementType class attributes and methods

# Type class attributes and methods

# muddle_PrimitiveType class attributes and methods

# muddle_IntegerType class attributes and methods

# PrimitiveType class attributes and methods

# muddle_StringType class attributes and methods

# muddle_BooleanType class attributes and methods

# muddle_RealType class attributes and methods

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="muddle_Type", type=muddle_Muddle, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_Muddle", type=muddle_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="MuddleElement", type=muddle_Muddle, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle", type=muddle_MuddleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="muddle_Type11", type=muddle_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_Feature", type=muddle_Type, multiplicity=Multiplicity(0, 1))
    }
)
owningType12: BinaryAssociation = BinaryAssociation(
    name="owningType12",
    ends={
        Property(name="MuddleElementType13", type=muddle_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=muddle_MuddleElementType, multiplicity=Multiplicity(0, 1))
    }
)
slots2: BinaryAssociation = BinaryAssociation(
    name="slots2",
    ends={
        Property(name="Slot", type=muddle_MuddleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningElement", type=muddle_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="MuddleElementType", type=muddle_MuddleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="instances", type=muddle_MuddleElementType, multiplicity=Multiplicity(0, 1))
    }
)
muddle4: BinaryAssociation = BinaryAssociation(
    name="muddle4",
    ends={
        Property(name="Muddle", type=muddle_MuddleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=muddle_Muddle, multiplicity=Multiplicity(0, 1))
    }
)
style5: BinaryAssociation = BinaryAssociation(
    name="style5",
    ends={
        Property(name="muddle_MuddleElementStyle", type=muddle_MuddleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_MuddleElement", type=muddle_MuddleElementStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature6: BinaryAssociation = BinaryAssociation(
    name="feature6",
    ends={
        Property(name="Feature", type=muddle_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slots", type=muddle_Feature, multiplicity=Multiplicity(0, 1))
    }
)
owningElement7: BinaryAssociation = BinaryAssociation(
    name="owningElement7",
    ends={
        Property(name="MuddleElement9", type=muddle_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slots8", type=muddle_MuddleElement, multiplicity=Multiplicity(0, 1))
    }
)
sourceFeature26: BinaryAssociation = BinaryAssociation(
    name="sourceFeature26",
    ends={
        Property(name="muddle_Feature27", type=muddle_LinkElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_LinkElementType", type=muddle_Feature, multiplicity=Multiplicity(0, 1))
    }
)
targetFeature28: BinaryAssociation = BinaryAssociation(
    name="targetFeature28",
    ends={
        Property(name="muddle_Feature30", type=muddle_LinkElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_LinkElementType29", type=muddle_Feature, multiplicity=Multiplicity(0, 1))
    }
)
slots14: BinaryAssociation = BinaryAssociation(
    name="slots14",
    ends={
        Property(name="Slot15", type=muddle_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=muddle_Slot, multiplicity=Multiplicity(0, 9999))
    }
)
instances16: BinaryAssociation = BinaryAssociation(
    name="instances16",
    ends={
        Property(name="MuddleElement17", type=muddle_MuddleElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=muddle_MuddleElement, multiplicity=Multiplicity(0, 9999))
    }
)
features18: BinaryAssociation = BinaryAssociation(
    name="features18",
    ends={
        Property(name="Feature19", type=muddle_MuddleElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="owningType", type=muddle_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTypes21: BinaryAssociation = BinaryAssociation(
    name="superTypes21",
    ends={
        Property(name="MuddleElementType22", type=muddle_MuddleElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="subTypes", type=muddle_MuddleElementType, multiplicity=Multiplicity(0, 9999))
    }
)
subTypes24: BinaryAssociation = BinaryAssociation(
    name="subTypes24",
    ends={
        Property(name="MuddleElementType25", type=muddle_MuddleElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="superTypes", type=muddle_MuddleElementType, multiplicity=Multiplicity(0, 9999))
    }
)
roleInSourceFeature31: BinaryAssociation = BinaryAssociation(
    name="roleInSourceFeature31",
    ends={
        Property(name="muddle_Feature33", type=muddle_LinkElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_LinkElementType32", type=muddle_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roleInTargetFeature34: BinaryAssociation = BinaryAssociation(
    name="roleInTargetFeature34",
    ends={
        Property(name="muddle_Feature36", type=muddle_LinkElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_LinkElementType35", type=muddle_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_muddle_LinkElementType_MuddleElementType = Generalization(general=MuddleElementType, specific=muddle_LinkElementType)
gen_muddle_MuddleElementType_Type = Generalization(general=Type, specific=muddle_MuddleElementType)
gen_muddle_PrimitiveType_Type = Generalization(general=Type, specific=muddle_PrimitiveType)
gen_muddle_IntegerType_PrimitiveType = Generalization(general=PrimitiveType, specific=muddle_IntegerType)
gen_muddle_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=muddle_StringType)
gen_muddle_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=muddle_BooleanType)
gen_muddle_RealType_PrimitiveType = Generalization(general=PrimitiveType, specific=muddle_RealType)

# Domain Model
domain_model = DomainModel(
    name="muddle",
    types={muddle_Muddle, muddle_Type, muddle_MuddleElement, muddle_Slot, muddle_MuddleElementType, muddle_MuddleElementStyle, muddle_Feature, muddle_LinkElementType, MuddleElementType, Type, muddle_PrimitiveType, muddle_IntegerType, PrimitiveType, muddle_StringType, muddle_BooleanType, muddle_RealType},
    associations={types0, elements1, type10, owningType12, slots2, type3, muddle4, style5, feature6, owningElement7, sourceFeature26, targetFeature28, slots14, instances16, features18, superTypes21, subTypes24, roleInSourceFeature31, roleInTargetFeature34},
    generalizations={gen_muddle_LinkElementType_MuddleElementType, gen_muddle_MuddleElementType_Type, gen_muddle_PrimitiveType_Type, gen_muddle_IntegerType_PrimitiveType, gen_muddle_StringType_PrimitiveType, gen_muddle_BooleanType_PrimitiveType, gen_muddle_RealType_PrimitiveType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)