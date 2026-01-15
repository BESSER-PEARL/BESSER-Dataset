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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="boolean")
    }
)

CTConstraintType: Enumeration = Enumeration(
    name="CTConstraintType",
    literals={
            EnumerationLiteral(name="not"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="implies")
    }
)

TreeConstraintType: Enumeration = Enumeration(
    name="TreeConstraintType",
    literals={
            EnumerationLiteral(name="Mandatory"),
			EnumerationLiteral(name="Optional"),
			EnumerationLiteral(name="Alternative"),
			EnumerationLiteral(name="Or")
    }
)

DRType: Enumeration = Enumeration(
    name="DRType",
    literals={
            EnumerationLiteral(name="selectionState"),
			EnumerationLiteral(name="hardLimit")
    }
)

DRSelectionStateType: Enumeration = Enumeration(
    name="DRSelectionStateType",
    literals={
            EnumerationLiteral(name="mandatory"),
			EnumerationLiteral(name="preferred"),
			EnumerationLiteral(name="forbidden")
    }
)

CMConstraintType: Enumeration = Enumeration(
    name="CMConstraintType",
    literals={
            EnumerationLiteral(name="not"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="implies")
    }
)

DROptimizationOp: Enumeration = Enumeration(
    name="DROptimizationOp",
    literals={
            EnumerationLiteral(name="maximize"),
			EnumerationLiteral(name="minimize")
    }
)

DRHardLimitOp: Enumeration = Enumeration(
    name="DRHardLimitOp",
    literals={
            EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="geq"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="leq")
    }
)

ConfigType: Enumeration = Enumeration(
    name="ConfigType",
    literals={
            EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output")
    }
)

# Classes
coCoMM_FeatureModel = Class(name="coCoMM::FeatureModel")
coCoMM_Feature = Class(name="coCoMM::Feature")
coCoMM_CrossTreeConstraint = Class(name="coCoMM::CrossTreeConstraint")
coCoMM_TreeConstraint = Class(name="coCoMM::TreeConstraint")
coCoMM_FeatureAttribute = Class(name="coCoMM::FeatureAttribute")
coCoMM_AttributeType = Class(name="coCoMM::AttributeType")
coCoMM_AttributeTypeElement = Class(name="coCoMM::AttributeTypeElement")
coCoMM_FeatureAttributeElement = Class(name="coCoMM::FeatureAttributeElement")
coCoMM_CTConstraintExpression = Class(name="coCoMM::CTConstraintExpression")
coCoMM_CoCo = Class(name="coCoMM::CoCo")
coCoMM_CrossModelConstraint = Class(name="coCoMM::CrossModelConstraint")
coCoMM_DecisionRule = Class(name="coCoMM::DecisionRule")
coCoMM_Project = Class(name="coCoMM::Project")
coCoMM_Stakeholder = Class(name="coCoMM::Stakeholder")
coCoMM_CMConstraintExpression = Class(name="coCoMM::CMConstraintExpression")
coCoMM_SelectionStateDR = Class(name="coCoMM::SelectionStateDR")
DecisionRule = Class(name="DecisionRule")
coCoMM_HardLimitDR = Class(name="coCoMM::HardLimitDR")
coCoMM_HardLimitDRExpression = Class(name="coCoMM::HardLimitDRExpression")
coCoMM_OptimizationDR = Class(name="coCoMM::OptimizationDR")
coCoMM_Config = Class(name="coCoMM::Config")

# coCoMM_FeatureModel class attributes and methods
coCoMM_FeatureModel_name: Property = Property(name="name", type=StringType)
coCoMM_FeatureModel_isDomain: Property = Property(name="isDomain", type=BooleanType)
coCoMM_FeatureModel.attributes={coCoMM_FeatureModel_isDomain, coCoMM_FeatureModel_name}

# coCoMM_Feature class attributes and methods
coCoMM_Feature_id: Property = Property(name="id", type=StringType)
coCoMM_Feature_name: Property = Property(name="name", type=StringType)
coCoMM_Feature_abstract: Property = Property(name="abstract", type=BooleanType)
coCoMM_Feature.attributes={coCoMM_Feature_name, coCoMM_Feature_abstract, coCoMM_Feature_id}

# coCoMM_CrossTreeConstraint class attributes and methods

# coCoMM_TreeConstraint class attributes and methods
coCoMM_TreeConstraint_type: Property = Property(name="type", type=StringType)
coCoMM_TreeConstraint.attributes={coCoMM_TreeConstraint_type}

# coCoMM_FeatureAttribute class attributes and methods
coCoMM_FeatureAttribute_name: Property = Property(name="name", type=StringType)
coCoMM_FeatureAttribute.attributes={coCoMM_FeatureAttribute_name}

# coCoMM_AttributeType class attributes and methods
coCoMM_AttributeType_id: Property = Property(name="id", type=StringType)
coCoMM_AttributeType_name: Property = Property(name="name", type=StringType)
coCoMM_AttributeType.attributes={coCoMM_AttributeType_id, coCoMM_AttributeType_name}

# coCoMM_AttributeTypeElement class attributes and methods
coCoMM_AttributeTypeElement_name: Property = Property(name="name", type=StringType)
coCoMM_AttributeTypeElement_dataType: Property = Property(name="dataType", type=StringType)
coCoMM_AttributeTypeElement.attributes={coCoMM_AttributeTypeElement_name, coCoMM_AttributeTypeElement_dataType}

# coCoMM_FeatureAttributeElement class attributes and methods
coCoMM_FeatureAttributeElement_value: Property = Property(name="value", type=StringType)
coCoMM_FeatureAttributeElement.attributes={coCoMM_FeatureAttributeElement_value}

# coCoMM_CTConstraintExpression class attributes and methods
coCoMM_CTConstraintExpression_op: Property = Property(name="op", type=StringType)
coCoMM_CTConstraintExpression.attributes={coCoMM_CTConstraintExpression_op}

# coCoMM_CoCo class attributes and methods

# coCoMM_CrossModelConstraint class attributes and methods

# coCoMM_DecisionRule class attributes and methods
coCoMM_DecisionRule_type: Property = Property(name="type", type=StringType)
coCoMM_DecisionRule.attributes={coCoMM_DecisionRule_type}

# coCoMM_Project class attributes and methods
coCoMM_Project_name: Property = Property(name="name", type=StringType)
coCoMM_Project_date: Property = Property(name="date", type=DateType)
coCoMM_Project_target: Property = Property(name="target", type=BooleanType)
coCoMM_Project.attributes={coCoMM_Project_name, coCoMM_Project_date, coCoMM_Project_target}

# coCoMM_Stakeholder class attributes and methods
coCoMM_Stakeholder_name: Property = Property(name="name", type=StringType)
coCoMM_Stakeholder_job: Property = Property(name="job", type=StringType)
coCoMM_Stakeholder.attributes={coCoMM_Stakeholder_job, coCoMM_Stakeholder_name}

# coCoMM_CMConstraintExpression class attributes and methods
coCoMM_CMConstraintExpression_op: Property = Property(name="op", type=StringType)
coCoMM_CMConstraintExpression.attributes={coCoMM_CMConstraintExpression_op}

# coCoMM_SelectionStateDR class attributes and methods
coCoMM_SelectionStateDR_state: Property = Property(name="state", type=StringType)
coCoMM_SelectionStateDR.attributes={coCoMM_SelectionStateDR_state}

# DecisionRule class attributes and methods

# coCoMM_HardLimitDR class attributes and methods

# coCoMM_HardLimitDRExpression class attributes and methods
coCoMM_HardLimitDRExpression_op: Property = Property(name="op", type=StringType)
coCoMM_HardLimitDRExpression_value: Property = Property(name="value", type=StringType)
coCoMM_HardLimitDRExpression.attributes={coCoMM_HardLimitDRExpression_op, coCoMM_HardLimitDRExpression_value}

# coCoMM_OptimizationDR class attributes and methods
coCoMM_OptimizationDR_funct: Property = Property(name="funct", type=StringType)
coCoMM_OptimizationDR.attributes={coCoMM_OptimizationDR_funct}

# coCoMM_Config class attributes and methods
coCoMM_Config_selected: Property = Property(name="selected", type=BooleanType)
coCoMM_Config_type: Property = Property(name="type", type=StringType)
coCoMM_Config.attributes={coCoMM_Config_type, coCoMM_Config_selected}

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="coCoMM_Feature", type=coCoMM_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_FeatureModel", type=coCoMM_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ctConstraints1: BinaryAssociation = BinaryAssociation(
    name="ctConstraints1",
    ends={
        Property(name="coCoMM_CrossTreeConstraint", type=coCoMM_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_FeatureModel2", type=coCoMM_CrossTreeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
treeConstraints3: BinaryAssociation = BinaryAssociation(
    name="treeConstraints3",
    ends={
        Property(name="coCoMM_TreeConstraint", type=coCoMM_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Feature4", type=coCoMM_TreeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureModel5: BinaryAssociation = BinaryAssociation(
    name="featureModel5",
    ends={
        Property(name="coCoMM_FeatureModel7", type=coCoMM_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Feature6", type=coCoMM_FeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
featureAttributes8: BinaryAssociation = BinaryAssociation(
    name="featureAttributes8",
    ends={
        Property(name="coCoMM_FeatureAttribute", type=coCoMM_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Feature9", type=coCoMM_FeatureAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
children10: BinaryAssociation = BinaryAssociation(
    name="children10",
    ends={
        Property(name="coCoMM_Feature12", type=coCoMM_TreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_TreeConstraint11", type=coCoMM_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
independentAttrType14: BinaryAssociation = BinaryAssociation(
    name="independentAttrType14",
    ends={
        Property(name="coCoMM_AttributeType", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_AttributeType13", type=coCoMM_AttributeType, multiplicity=Multiplicity(0, 1))
    }
)
elements15: BinaryAssociation = BinaryAssociation(
    name="elements15",
    ends={
        Property(name="coCoMM_AttributeTypeElement", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_AttributeType16", type=coCoMM_AttributeTypeElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
featureAttributes17: BinaryAssociation = BinaryAssociation(
    name="featureAttributes17",
    ends={
        Property(name="coCoMM_FeatureAttribute19", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_AttributeType18", type=coCoMM_FeatureAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrType20: BinaryAssociation = BinaryAssociation(
    name="attrType20",
    ends={
        Property(name="coCoMM_AttributeType22", type=coCoMM_FeatureAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_FeatureAttribute21", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
elements23: BinaryAssociation = BinaryAssociation(
    name="elements23",
    ends={
        Property(name="coCoMM_FeatureAttributeElement", type=coCoMM_FeatureAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_FeatureAttribute24", type=coCoMM_FeatureAttributeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions25: BinaryAssociation = BinaryAssociation(
    name="expressions25",
    ends={
        Property(name="coCoMM_CTConstraintExpression", type=coCoMM_CrossTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CrossTreeConstraint26", type=coCoMM_CTConstraintExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
featureModels27: BinaryAssociation = BinaryAssociation(
    name="featureModels27",
    ends={
        Property(name="coCoMM_FeatureModel28", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo", type=coCoMM_FeatureModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmConstraints29: BinaryAssociation = BinaryAssociation(
    name="cmConstraints29",
    ends={
        Property(name="coCoMM_CrossModelConstraint", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo30", type=coCoMM_CrossModelConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decisionRules31: BinaryAssociation = BinaryAssociation(
    name="decisionRules31",
    ends={
        Property(name="coCoMM_DecisionRule", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo32", type=coCoMM_DecisionRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeTypes33: BinaryAssociation = BinaryAssociation(
    name="attributeTypes33",
    ends={
        Property(name="coCoMM_AttributeType35", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo34", type=coCoMM_AttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project36: BinaryAssociation = BinaryAssociation(
    name="project36",
    ends={
        Property(name="coCoMM_Project", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo37", type=coCoMM_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions40: BinaryAssociation = BinaryAssociation(
    name="expressions40",
    ends={
        Property(name="coCoMM_CMConstraintExpression", type=coCoMM_CrossModelConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CrossModelConstraint41", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
featureModel42: BinaryAssociation = BinaryAssociation(
    name="featureModel42",
    ends={
        Property(name="coCoMM_FeatureModel43", type=coCoMM_SelectionStateDR, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_SelectionStateDR", type=coCoMM_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)
feature44: BinaryAssociation = BinaryAssociation(
    name="feature44",
    ends={
        Property(name="coCoMM_Feature46", type=coCoMM_SelectionStateDR, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_SelectionStateDR45", type=coCoMM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
expressions47: BinaryAssociation = BinaryAssociation(
    name="expressions47",
    ends={
        Property(name="coCoMM_HardLimitDRExpression", type=coCoMM_HardLimitDR, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_HardLimitDR", type=coCoMM_HardLimitDRExpression, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
attrType48: BinaryAssociation = BinaryAssociation(
    name="attrType48",
    ends={
        Property(name="coCoMM_AttributeType50", type=coCoMM_HardLimitDR, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_HardLimitDR49", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
attrType51: BinaryAssociation = BinaryAssociation(
    name="attrType51",
    ends={
        Property(name="coCoMM_AttributeType52", type=coCoMM_OptimizationDR, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_OptimizationDR", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
stakeholders38: BinaryAssociation = BinaryAssociation(
    name="stakeholders38",
    ends={
        Property(name="coCoMM_Stakeholder", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo39", type=coCoMM_Stakeholder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decisionRules53: BinaryAssociation = BinaryAssociation(
    name="decisionRules53",
    ends={
        Property(name="coCoMM_DecisionRule55", type=coCoMM_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Project54", type=coCoMM_DecisionRule, multiplicity=Multiplicity(0, 9999))
    }
)
configs56: BinaryAssociation = BinaryAssociation(
    name="configs56",
    ends={
        Property(name="coCoMM_Config", type=coCoMM_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Project57", type=coCoMM_Config, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stakeholder58: BinaryAssociation = BinaryAssociation(
    name="stakeholder58",
    ends={
        Property(name="coCoMM_Stakeholder60", type=coCoMM_Config, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Config59", type=coCoMM_Stakeholder, multiplicity=Multiplicity(0, 1))
    }
)
features61: BinaryAssociation = BinaryAssociation(
    name="features61",
    ends={
        Property(name="coCoMM_Feature63", type=coCoMM_Config, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Config62", type=coCoMM_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
features64: BinaryAssociation = BinaryAssociation(
    name="features64",
    ends={
        Property(name="coCoMM_Feature66", type=coCoMM_CTConstraintExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CTConstraintExpression65", type=coCoMM_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
expressions68: BinaryAssociation = BinaryAssociation(
    name="expressions68",
    ends={
        Property(name="coCoMM_CTConstraintExpression69", type=coCoMM_CTConstraintExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CTConstraintExpression67", type=coCoMM_CTConstraintExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions74: BinaryAssociation = BinaryAssociation(
    name="expressions74",
    ends={
        Property(name="coCoMM_CMConstraintExpression75", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CMConstraintExpression73", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features70: BinaryAssociation = BinaryAssociation(
    name="features70",
    ends={
        Property(name="coCoMM_Feature72", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CMConstraintExpression71", type=coCoMM_Feature, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_coCoMM_SelectionStateDR_DecisionRule = Generalization(general=DecisionRule, specific=coCoMM_SelectionStateDR)
gen_coCoMM_HardLimitDR_DecisionRule = Generalization(general=DecisionRule, specific=coCoMM_HardLimitDR)
gen_coCoMM_OptimizationDR_DecisionRule = Generalization(general=DecisionRule, specific=coCoMM_OptimizationDR)

# Domain Model
domain_model = DomainModel(
    name="coCoMM",
    types={coCoMM_FeatureModel, coCoMM_Feature, coCoMM_CrossTreeConstraint, coCoMM_TreeConstraint, coCoMM_FeatureAttribute, coCoMM_AttributeType, coCoMM_AttributeTypeElement, coCoMM_FeatureAttributeElement, coCoMM_CTConstraintExpression, coCoMM_CoCo, coCoMM_CrossModelConstraint, coCoMM_DecisionRule, coCoMM_Project, coCoMM_Stakeholder, coCoMM_CMConstraintExpression, coCoMM_SelectionStateDR, DecisionRule, coCoMM_HardLimitDR, coCoMM_HardLimitDRExpression, coCoMM_OptimizationDR, coCoMM_Config, DataType, CTConstraintType, TreeConstraintType, DRType, DRSelectionStateType, CMConstraintType, DROptimizationOp, DRHardLimitOp, ConfigType},
    associations={root0, ctConstraints1, treeConstraints3, featureModel5, featureAttributes8, children10, independentAttrType14, elements15, featureAttributes17, attrType20, elements23, expressions25, featureModels27, cmConstraints29, decisionRules31, attributeTypes33, project36, expressions40, featureModel42, feature44, expressions47, attrType48, attrType51, stakeholders38, decisionRules53, configs56, stakeholder58, features61, features64, expressions68, expressions74, features70},
    generalizations={gen_coCoMM_SelectionStateDR_DecisionRule, gen_coCoMM_HardLimitDR_DecisionRule, gen_coCoMM_OptimizationDR_DecisionRule},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)