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
muddle_MuddleElement = Class(name="muddle::MuddleElement")
muddle_Muddle = Class(name="muddle::Muddle")
muddle_Type = Class(name="muddle::Type", is_abstract=True)
muddle_Slot = Class(name="muddle::Slot")
muddle_MuddleElementType = Class(name="muddle::MuddleElementType")
muddle_Feature = Class(name="muddle::Feature")
Type = Class(name="Type")
muddle_PrimitiveType = Class(name="muddle::PrimitiveType", is_abstract=True)
muddle_IntegerType = Class(name="muddle::IntegerType")
PrimitiveType = Class(name="PrimitiveType")
muddle_StringType = Class(name="muddle::StringType")
muddle_LinkElementType = Class(name="muddle::LinkElementType")
MuddleElementType = Class(name="MuddleElementType")
muddle_BooleanType = Class(name="muddle::BooleanType")
muddle_RealType = Class(name="muddle::RealType")

# muddle_MuddleElement class attributes and methods
muddle_MuddleElement_id: Property = Property(name="id", type=StringType)
muddle_MuddleElement.attributes={muddle_MuddleElement_id}

# muddle_Muddle class attributes and methods

# muddle_Type class attributes and methods
muddle_Type_name: Property = Property(name="name", type=StringType)
muddle_Type.attributes={muddle_Type_name}

# muddle_Slot class attributes and methods
muddle_Slot_values: Property = Property(name="values", type=StringType)
muddle_Slot.attributes={muddle_Slot_values}

# muddle_MuddleElementType class attributes and methods

# muddle_Feature class attributes and methods
muddle_Feature_name: Property = Property(name="name", type=StringType)
muddle_Feature_many: Property = Property(name="many", type=BooleanType)
muddle_Feature_primary: Property = Property(name="primary", type=BooleanType)
muddle_Feature_runtime: Property = Property(name="runtime", type=BooleanType)
muddle_Feature.attributes={muddle_Feature_runtime, muddle_Feature_many, muddle_Feature_primary, muddle_Feature_name}

# Type class attributes and methods

# muddle_PrimitiveType class attributes and methods

# muddle_IntegerType class attributes and methods

# PrimitiveType class attributes and methods

# muddle_StringType class attributes and methods

# muddle_LinkElementType class attributes and methods

# MuddleElementType class attributes and methods

# muddle_BooleanType class attributes and methods

# muddle_RealType class attributes and methods

# Relationships
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="MuddleElement", type=muddle_Muddle, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle", type=muddle_MuddleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="muddle_Type", type=muddle_Muddle, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_Muddle", type=muddle_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
muddle4: BinaryAssociation = BinaryAssociation(
    name="muddle4",
    ends={
        Property(name="elements", type=muddle_Muddle, multiplicity=Multiplicity(0, 1)),
        Property(name="Muddle", type=muddle_MuddleElement, multiplicity=Multiplicity(1, 1))
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
instances15: BinaryAssociation = BinaryAssociation(
    name="instances15",
    ends={
        Property(name="MuddleElement16", type=muddle_MuddleElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=muddle_MuddleElement, multiplicity=Multiplicity(0, 9999))
    }
)
feature5: BinaryAssociation = BinaryAssociation(
    name="feature5",
    ends={
        Property(name="Feature", type=muddle_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slots", type=muddle_Feature, multiplicity=Multiplicity(0, 1))
    }
)
owningElement6: BinaryAssociation = BinaryAssociation(
    name="owningElement6",
    ends={
        Property(name="MuddleElement8", type=muddle_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slots7", type=muddle_MuddleElement, multiplicity=Multiplicity(0, 1))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="muddle_Type10", type=muddle_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_Feature", type=muddle_Type, multiplicity=Multiplicity(0, 1))
    }
)
owningType11: BinaryAssociation = BinaryAssociation(
    name="owningType11",
    ends={
        Property(name="MuddleElementType12", type=muddle_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=muddle_MuddleElementType, multiplicity=Multiplicity(0, 1))
    }
)
slots13: BinaryAssociation = BinaryAssociation(
    name="slots13",
    ends={
        Property(name="Slot14", type=muddle_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=muddle_Slot, multiplicity=Multiplicity(0, 9999))
    }
)
features17: BinaryAssociation = BinaryAssociation(
    name="features17",
    ends={
        Property(name="Feature18", type=muddle_MuddleElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="owningType", type=muddle_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTypes20: BinaryAssociation = BinaryAssociation(
    name="superTypes20",
    ends={
        Property(name="MuddleElementType21", type=muddle_MuddleElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="subTypes", type=muddle_MuddleElementType, multiplicity=Multiplicity(0, 9999))
    }
)
subTypes23: BinaryAssociation = BinaryAssociation(
    name="subTypes23",
    ends={
        Property(name="MuddleElementType24", type=muddle_MuddleElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="superTypes", type=muddle_MuddleElementType, multiplicity=Multiplicity(0, 9999))
    }
)
sourceFeature25: BinaryAssociation = BinaryAssociation(
    name="sourceFeature25",
    ends={
        Property(name="muddle_Feature26", type=muddle_LinkElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_LinkElementType", type=muddle_Feature, multiplicity=Multiplicity(0, 1))
    }
)
targetFeature27: BinaryAssociation = BinaryAssociation(
    name="targetFeature27",
    ends={
        Property(name="muddle_Feature29", type=muddle_LinkElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_LinkElementType28", type=muddle_Feature, multiplicity=Multiplicity(0, 1))
    }
)
roleInSourceFeature30: BinaryAssociation = BinaryAssociation(
    name="roleInSourceFeature30",
    ends={
        Property(name="muddle_Feature32", type=muddle_LinkElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_LinkElementType31", type=muddle_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roleInTargetFeature33: BinaryAssociation = BinaryAssociation(
    name="roleInTargetFeature33",
    ends={
        Property(name="muddle_Feature35", type=muddle_LinkElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="muddle_LinkElementType34", type=muddle_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_muddle_MuddleElementType_Type = Generalization(general=Type, specific=muddle_MuddleElementType)
gen_muddle_PrimitiveType_Type = Generalization(general=Type, specific=muddle_PrimitiveType)
gen_muddle_IntegerType_PrimitiveType = Generalization(general=PrimitiveType, specific=muddle_IntegerType)
gen_muddle_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=muddle_StringType)
gen_muddle_LinkElementType_MuddleElementType = Generalization(general=MuddleElementType, specific=muddle_LinkElementType)
gen_muddle_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=muddle_BooleanType)
gen_muddle_RealType_PrimitiveType = Generalization(general=PrimitiveType, specific=muddle_RealType)

# Domain Model
domain_model = DomainModel(
    name="muddle",
    types={muddle_MuddleElement, muddle_Muddle, muddle_Type, muddle_Slot, muddle_MuddleElementType, muddle_Feature, Type, muddle_PrimitiveType, muddle_IntegerType, PrimitiveType, muddle_StringType, muddle_LinkElementType, MuddleElementType, muddle_BooleanType, muddle_RealType},
    associations={elements1, types0, muddle4, slots2, type3, instances15, feature5, owningElement6, type9, owningType11, slots13, features17, superTypes20, subTypes23, sourceFeature25, targetFeature27, roleInSourceFeature30, roleInTargetFeature33},
    generalizations={gen_muddle_MuddleElementType_Type, gen_muddle_PrimitiveType_Type, gen_muddle_IntegerType_PrimitiveType, gen_muddle_StringType_PrimitiveType, gen_muddle_LinkElementType_MuddleElementType, gen_muddle_BooleanType_PrimitiveType, gen_muddle_RealType_PrimitiveType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)