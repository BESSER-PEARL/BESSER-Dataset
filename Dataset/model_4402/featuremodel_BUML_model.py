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
            EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="FEATURE")
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
featureModel_Feature = Class(name="featureModel::Feature")
Node = Class(name="Node")
featureModel_TypedValue = Class(name="featureModel::TypedValue")
featureModel_Node = Class(name="featureModel::Node")
featureModel_Project = Class(name="featureModel::Project")
featureModel_Relation = Class(name="featureModel::Relation")
featureModel_FeatureGroup = Class(name="featureModel::FeatureGroup")
featureModel_RelationFG = Class(name="featureModel::RelationFG")
Relation = Class(name="Relation")
featureModel_RelationFeature = Class(name="featureModel::RelationFeature")

# featureModel_Feature class attributes and methods
featureModel_Feature_name: Property = Property(name="name", type=StringType)
featureModel_Feature_valueType: Property = Property(name="valueType", type=StringType)
featureModel_Feature.attributes={featureModel_Feature_valueType, featureModel_Feature_name}

# Node class attributes and methods

# featureModel_TypedValue class attributes and methods
featureModel_TypedValue_integerValue: Property = Property(name="integerValue", type=StringType)
featureModel_TypedValue_stringValue: Property = Property(name="stringValue", type=StringType)
featureModel_TypedValue_floatValue: Property = Property(name="floatValue", type=StringType)
featureModel_TypedValue.attributes={featureModel_TypedValue_stringValue, featureModel_TypedValue_integerValue, featureModel_TypedValue_floatValue}

# featureModel_Node class attributes and methods

# featureModel_Project class attributes and methods
featureModel_Project_nameConfigFile: Property = Property(name="nameConfigFile", type=StringType)
featureModel_Project_nameConstraintsFile: Property = Property(name="nameConstraintsFile", type=StringType)
featureModel_Project_numberOfProducts: Property = Property(name="numberOfProducts", type=IntegerType)
featureModel_Project_validatedOCL: Property = Property(name="validatedOCL", type=BooleanType)
featureModel_Project_validatedTEF: Property = Property(name="validatedTEF", type=BooleanType)
featureModel_Project.attributes={featureModel_Project_validatedOCL, featureModel_Project_validatedTEF, featureModel_Project_numberOfProducts, featureModel_Project_nameConfigFile, featureModel_Project_nameConstraintsFile}

# featureModel_Relation class attributes and methods

# featureModel_FeatureGroup class attributes and methods
featureModel_FeatureGroup_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
featureModel_FeatureGroup_upperBound: Property = Property(name="upperBound", type=IntegerType)
featureModel_FeatureGroup_type: Property = Property(name="type", type=StringType)
featureModel_FeatureGroup.attributes={featureModel_FeatureGroup_upperBound, featureModel_FeatureGroup_lowerBound, featureModel_FeatureGroup_type}

# featureModel_RelationFG class attributes and methods

# Relation class attributes and methods

# featureModel_RelationFeature class attributes and methods
featureModel_RelationFeature_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
featureModel_RelationFeature_upperBound: Property = Property(name="upperBound", type=IntegerType)
featureModel_RelationFeature_type: Property = Property(name="type", type=StringType)
featureModel_RelationFeature.attributes={featureModel_RelationFeature_type, featureModel_RelationFeature_upperBound, featureModel_RelationFeature_lowerBound}

# Relationships
featureValue9: BinaryAssociation = BinaryAssociation(
    name="featureValue9",
    ends={
        Property(name="featureModel_Feature11", type=featureModel_TypedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_TypedValue10", type=featureModel_Feature, multiplicity=Multiplicity(0, 1))
    }
)
typedValue0: BinaryAssociation = BinaryAssociation(
    name="typedValue0",
    ends={
        Property(name="featureModel_TypedValue", type=featureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Feature", type=featureModel_TypedValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="featureModel_Node", type=featureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Feature2", type=featureModel_Node, multiplicity=Multiplicity(0, 9999))
    }
)
references4: BinaryAssociation = BinaryAssociation(
    name="references4",
    ends={
        Property(name="featureModel_Feature5", type=featureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Feature3", type=featureModel_Feature, multiplicity=Multiplicity(0, 1))
    }
)
referenciated7: BinaryAssociation = BinaryAssociation(
    name="referenciated7",
    ends={
        Property(name="featureModel_Feature8", type=featureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Feature6", type=featureModel_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
source26: BinaryAssociation = BinaryAssociation(
    name="source26",
    ends={
        Property(name="featureModel_Feature27", type=featureModel_RelationFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_RelationFeature", type=featureModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="featureModel_Feature30", type=featureModel_RelationFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_RelationFeature29", type=featureModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
features12: BinaryAssociation = BinaryAssociation(
    name="features12",
    ends={
        Property(name="featureModel_Node13", type=featureModel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Project", type=featureModel_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations14: BinaryAssociation = BinaryAssociation(
    name="relations14",
    ends={
        Property(name="featureModel_Relation", type=featureModel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Project15", type=featureModel_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children16: BinaryAssociation = BinaryAssociation(
    name="children16",
    ends={
        Property(name="featureModel_Feature17", type=featureModel_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_FeatureGroup", type=featureModel_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
father19: BinaryAssociation = BinaryAssociation(
    name="father19",
    ends={
        Property(name="featureModel_Node20", type=featureModel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Node18", type=featureModel_Node, multiplicity=Multiplicity(0, 1))
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="featureModel_Node22", type=featureModel_RelationFG, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_RelationFG", type=featureModel_Node, multiplicity=Multiplicity(1, 1))
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="featureModel_Node25", type=featureModel_RelationFG, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_RelationFG24", type=featureModel_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_featureModel_Feature_Node = Generalization(general=Node, specific=featureModel_Feature)
gen_featureModel_FeatureGroup_Node = Generalization(general=Node, specific=featureModel_FeatureGroup)
gen_featureModel_RelationFG_Relation = Generalization(general=Relation, specific=featureModel_RelationFG)
gen_featureModel_RelationFeature_Relation = Generalization(general=Relation, specific=featureModel_RelationFeature)

# Domain Model
domain_model = DomainModel(
    name="featureModel",
    types={featureModel_Feature, Node, featureModel_TypedValue, featureModel_Node, featureModel_Project, featureModel_Relation, featureModel_FeatureGroup, featureModel_RelationFG, Relation, featureModel_RelationFeature, ValueType, FeatureType, FeatureGroupType},
    associations={featureValue9, typedValue0, children1, references4, referenciated7, source26, target28, features12, relations14, children16, father19, source21, target23},
    generalizations={gen_featureModel_Feature_Node, gen_featureModel_FeatureGroup_Node, gen_featureModel_RelationFG_Relation, gen_featureModel_RelationFeature_Relation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)