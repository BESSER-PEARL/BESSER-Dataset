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
ValueType: Enumeration = Enumeration(
    name="ValueType",
    literals={
            EnumerationLiteral(name="FEATURE"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="STRING")
    }
)

ConfigState: Enumeration = Enumeration(
    name="ConfigState",
    literals={
            EnumerationLiteral(name="UNDECIDED"),
			EnumerationLiteral(name="USER_SELECTED"),
			EnumerationLiteral(name="USER_ELIMINATED")
    }
)

FeatureType: Enumeration = Enumeration(
    name="FeatureType",
    literals={
            EnumerationLiteral(name="OPTIONAL"),
			EnumerationLiteral(name="MANDATORY"),
			EnumerationLiteral(name="SIMPLE")
    }
)

FeatureGroupType: Enumeration = Enumeration(
    name="FeatureGroupType",
    literals={
            EnumerationLiteral(name="XORGROUP"),
			EnumerationLiteral(name="ORGROUP"),
			EnumerationLiteral(name="SIMPLEGROUP")
    }
)

# Classes
specializationModel_Project = Class(name="specializationModel::Project")
specializationModel_Relation = Class(name="specializationModel::Relation")
specializationModel_FeatureGroup = Class(name="specializationModel::FeatureGroup")
specializationModel_Feature = Class(name="specializationModel::Feature")
Node = Class(name="Node")
specializationModel_TypedValue = Class(name="specializationModel::TypedValue")
specializationModel_Node = Class(name="specializationModel::Node")
specializationModel_RelationFG = Class(name="specializationModel::RelationFG")
Relation = Class(name="Relation")
specializationModel_RelationFeature = Class(name="specializationModel::RelationFeature")

# specializationModel_Project class attributes and methods
specializationModel_Project_featureModelURI: Property = Property(name="featureModelURI", type=StringType)
specializationModel_Project_nameConstraintsFile: Property = Property(name="nameConstraintsFile", type=StringType)
specializationModel_Project_nameConfigFile: Property = Property(name="nameConfigFile", type=StringType)
specializationModel_Project_numberOfProducts: Property = Property(name="numberOfProducts", type=IntegerType)
specializationModel_Project_infiniteDomain: Property = Property(name="infiniteDomain", type=BooleanType)
specializationModel_Project_userConstraintsState: Property = Property(name="userConstraintsState", type=BooleanType)
specializationModel_Project.attributes={specializationModel_Project_nameConfigFile, specializationModel_Project_featureModelURI, specializationModel_Project_userConstraintsState, specializationModel_Project_nameConstraintsFile, specializationModel_Project_infiniteDomain, specializationModel_Project_numberOfProducts}

# specializationModel_Relation class attributes and methods

# specializationModel_FeatureGroup class attributes and methods
specializationModel_FeatureGroup_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
specializationModel_FeatureGroup_upperBound: Property = Property(name="upperBound", type=IntegerType)
specializationModel_FeatureGroup_type: Property = Property(name="type", type=StringType)
specializationModel_FeatureGroup.attributes={specializationModel_FeatureGroup_type, specializationModel_FeatureGroup_lowerBound, specializationModel_FeatureGroup_upperBound}

# specializationModel_Feature class attributes and methods
specializationModel_Feature_name: Property = Property(name="name", type=StringType)
specializationModel_Feature_valueType: Property = Property(name="valueType", type=StringType)
specializationModel_Feature_state: Property = Property(name="state", type=StringType)
specializationModel_Feature_realName: Property = Property(name="realName", type=StringType)
specializationModel_Feature.attributes={specializationModel_Feature_valueType, specializationModel_Feature_state, specializationModel_Feature_name, specializationModel_Feature_realName}

# Node class attributes and methods

# specializationModel_TypedValue class attributes and methods
specializationModel_TypedValue_integerValue: Property = Property(name="integerValue", type=StringType)
specializationModel_TypedValue_stringValue: Property = Property(name="stringValue", type=StringType)
specializationModel_TypedValue_floatValue: Property = Property(name="floatValue", type=StringType)
specializationModel_TypedValue.attributes={specializationModel_TypedValue_floatValue, specializationModel_TypedValue_stringValue, specializationModel_TypedValue_integerValue}

# specializationModel_Node class attributes and methods

# specializationModel_RelationFG class attributes and methods

# Relation class attributes and methods

# specializationModel_RelationFeature class attributes and methods
specializationModel_RelationFeature_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
specializationModel_RelationFeature_upperBound: Property = Property(name="upperBound", type=IntegerType)
specializationModel_RelationFeature_type: Property = Property(name="type", type=StringType)
specializationModel_RelationFeature.attributes={specializationModel_RelationFeature_type, specializationModel_RelationFeature_lowerBound, specializationModel_RelationFeature_upperBound}

# Relationships
features12: BinaryAssociation = BinaryAssociation(
    name="features12",
    ends={
        Property(name="specializationModel_Node13", type=specializationModel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_Project", type=specializationModel_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations14: BinaryAssociation = BinaryAssociation(
    name="relations14",
    ends={
        Property(name="specializationModel_Relation", type=specializationModel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_Project15", type=specializationModel_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typedValue0: BinaryAssociation = BinaryAssociation(
    name="typedValue0",
    ends={
        Property(name="specializationModel_TypedValue", type=specializationModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_Feature", type=specializationModel_TypedValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
references2: BinaryAssociation = BinaryAssociation(
    name="references2",
    ends={
        Property(name="specializationModel_Feature3", type=specializationModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_Feature1", type=specializationModel_Feature, multiplicity=Multiplicity(0, 1))
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="specializationModel_Node", type=specializationModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_Feature5", type=specializationModel_Node, multiplicity=Multiplicity(0, 9999))
    }
)
referenciated7: BinaryAssociation = BinaryAssociation(
    name="referenciated7",
    ends={
        Property(name="specializationModel_Feature8", type=specializationModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_Feature6", type=specializationModel_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
featureValue9: BinaryAssociation = BinaryAssociation(
    name="featureValue9",
    ends={
        Property(name="specializationModel_Feature11", type=specializationModel_TypedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_TypedValue10", type=specializationModel_Feature, multiplicity=Multiplicity(0, 1))
    }
)
children16: BinaryAssociation = BinaryAssociation(
    name="children16",
    ends={
        Property(name="specializationModel_Feature17", type=specializationModel_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_FeatureGroup", type=specializationModel_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
father19: BinaryAssociation = BinaryAssociation(
    name="father19",
    ends={
        Property(name="specializationModel_Node20", type=specializationModel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_Node18", type=specializationModel_Node, multiplicity=Multiplicity(0, 1))
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="specializationModel_Node22", type=specializationModel_RelationFG, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_RelationFG", type=specializationModel_Node, multiplicity=Multiplicity(1, 1))
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="specializationModel_Node25", type=specializationModel_RelationFG, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_RelationFG24", type=specializationModel_Node, multiplicity=Multiplicity(1, 1))
    }
)
source26: BinaryAssociation = BinaryAssociation(
    name="source26",
    ends={
        Property(name="specializationModel_Feature27", type=specializationModel_RelationFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_RelationFeature", type=specializationModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="specializationModel_Feature30", type=specializationModel_RelationFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specializationModel_RelationFeature29", type=specializationModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_specializationModel_FeatureGroup_Node = Generalization(general=Node, specific=specializationModel_FeatureGroup)
gen_specializationModel_Feature_Node = Generalization(general=Node, specific=specializationModel_Feature)
gen_specializationModel_RelationFG_Relation = Generalization(general=Relation, specific=specializationModel_RelationFG)
gen_specializationModel_RelationFeature_Relation = Generalization(general=Relation, specific=specializationModel_RelationFeature)

# Domain Model
domain_model = DomainModel(
    name="specializationModel",
    types={specializationModel_Project, specializationModel_Relation, specializationModel_FeatureGroup, specializationModel_Feature, Node, specializationModel_TypedValue, specializationModel_Node, specializationModel_RelationFG, Relation, specializationModel_RelationFeature, ValueType, ConfigState, FeatureType, FeatureGroupType},
    associations={features12, relations14, typedValue0, references2, children4, referenciated7, featureValue9, children16, father19, source21, target23, source26, target28},
    generalizations={gen_specializationModel_FeatureGroup_Node, gen_specializationModel_Feature_Node, gen_specializationModel_RelationFG_Relation, gen_specializationModel_RelationFeature_Relation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)