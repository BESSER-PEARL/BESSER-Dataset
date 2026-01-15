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
TreeConstraintType: Enumeration = Enumeration(
    name="TreeConstraintType",
    literals={
            EnumerationLiteral(name="And"),
			EnumerationLiteral(name="Alternative"),
			EnumerationLiteral(name="Or")
    }
)

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

CCType: Enumeration = Enumeration(
    name="CCType",
    literals={
            EnumerationLiteral(name="selectionState"),
			EnumerationLiteral(name="hardLimit"),
			EnumerationLiteral(name="optimization")
    }
)

CCSelectionStateType: Enumeration = Enumeration(
    name="CCSelectionStateType",
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

CCOptimizationOp: Enumeration = Enumeration(
    name="CCOptimizationOp",
    literals={
            EnumerationLiteral(name="maximize"),
			EnumerationLiteral(name="minimize")
    }
)

CCHardLimitOp: Enumeration = Enumeration(
    name="CCHardLimitOp",
    literals={
            EnumerationLiteral(name="leq"),
			EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="geq"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="eq")
    }
)

ConfigType: Enumeration = Enumeration(
    name="ConfigType",
    literals={
            EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output")
    }
)

AggregationOp: Enumeration = Enumeration(
    name="AggregationOp",
    literals={
            EnumerationLiteral(name="add"),
			EnumerationLiteral(name="multiply"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="max")
    }
)

SCType: Enumeration = Enumeration(
    name="SCType",
    literals={
            EnumerationLiteral(name="selectionState"),
			EnumerationLiteral(name="hardLimit"),
			EnumerationLiteral(name="optimization"),
			EnumerationLiteral(name="finiteDomain")
    }
)

OptimizationSCFunct: Enumeration = Enumeration(
    name="OptimizationSCFunct",
    literals={
            EnumerationLiteral(name="maximize"),
			EnumerationLiteral(name="minimize")
    }
)

# Classes
coCoMM_FeatureModel = Class(name="coCoMM::FeatureModel")
coCoMM_FeatureAttribute = Class(name="coCoMM::FeatureAttribute")
coCoMM_AttributeType = Class(name="coCoMM::AttributeType")
coCoMM_Feature = Class(name="coCoMM::Feature")
coCoMM_CrossTreeConstraint = Class(name="coCoMM::CrossTreeConstraint")
coCoMM_TreeConstraint = Class(name="coCoMM::TreeConstraint")
coCoMM_CoCo = Class(name="coCoMM::CoCo")
coCoMM_CrossModelConstraint = Class(name="coCoMM::CrossModelConstraint")
coCoMM_SolutionConstraint = Class(name="coCoMM::SolutionConstraint")
coCoMM_ConfigurationConstraint = Class(name="coCoMM::ConfigurationConstraint")
coCoMM_Project = Class(name="coCoMM::Project")
coCoMM_Stakeholder = Class(name="coCoMM::Stakeholder")
coCoMM_CTConstraintExpression = Class(name="coCoMM::CTConstraintExpression")
coCoMM_HardLimitCC = Class(name="coCoMM::HardLimitCC")
coCoMM_HardLimitCCExpression = Class(name="coCoMM::HardLimitCCExpression")
coCoMM_AggregationFunction = Class(name="coCoMM::AggregationFunction")
coCoMM_CMConstraintExpression = Class(name="coCoMM::CMConstraintExpression")
coCoMM_SelectionStateCC = Class(name="coCoMM::SelectionStateCC")
ConfigurationConstraint = Class(name="ConfigurationConstraint")
coCoMM_OptimizationCC = Class(name="coCoMM::OptimizationCC")
coCoMM_Config = Class(name="coCoMM::Config")
coCoMM_OptimizationSC = Class(name="coCoMM::OptimizationSC")
SolutionConstraint = Class(name="SolutionConstraint")

# coCoMM_FeatureModel class attributes and methods
coCoMM_FeatureModel_name: Property = Property(name="name", type=StringType)
coCoMM_FeatureModel_isDomain: Property = Property(name="isDomain", type=BooleanType)
coCoMM_FeatureModel_id: Property = Property(name="id", type=StringType)
coCoMM_FeatureModel.attributes={coCoMM_FeatureModel_name, coCoMM_FeatureModel_id, coCoMM_FeatureModel_isDomain}

# coCoMM_FeatureAttribute class attributes and methods
coCoMM_FeatureAttribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
coCoMM_FeatureAttribute_minValue: Property = Property(name="minValue", type=StringType)
coCoMM_FeatureAttribute_maxValue: Property = Property(name="maxValue", type=StringType)
coCoMM_FeatureAttribute.attributes={coCoMM_FeatureAttribute_defaultValue, coCoMM_FeatureAttribute_maxValue, coCoMM_FeatureAttribute_minValue}

# coCoMM_AttributeType class attributes and methods
coCoMM_AttributeType_id: Property = Property(name="id", type=StringType)
coCoMM_AttributeType_name: Property = Property(name="name", type=StringType)
coCoMM_AttributeType_dataType: Property = Property(name="dataType", type=StringType)
coCoMM_AttributeType.attributes={coCoMM_AttributeType_id, coCoMM_AttributeType_name, coCoMM_AttributeType_dataType}

# coCoMM_Feature class attributes and methods
coCoMM_Feature_mandatory: Property = Property(name="mandatory", type=BooleanType)
coCoMM_Feature_id: Property = Property(name="id", type=StringType)
coCoMM_Feature_name: Property = Property(name="name", type=StringType)
coCoMM_Feature_abstract: Property = Property(name="abstract", type=BooleanType)
coCoMM_Feature.attributes={coCoMM_Feature_id, coCoMM_Feature_name, coCoMM_Feature_abstract, coCoMM_Feature_mandatory}

# coCoMM_CrossTreeConstraint class attributes and methods

# coCoMM_TreeConstraint class attributes and methods
coCoMM_TreeConstraint_type: Property = Property(name="type", type=StringType)
coCoMM_TreeConstraint.attributes={coCoMM_TreeConstraint_type}

# coCoMM_CoCo class attributes and methods
coCoMM_CoCo_id: Property = Property(name="id", type=StringType)
coCoMM_CoCo_name: Property = Property(name="name", type=StringType)
coCoMM_CoCo_configScenario: Property = Property(name="configScenario", type=StringType)
coCoMM_CoCo.attributes={coCoMM_CoCo_name, coCoMM_CoCo_configScenario, coCoMM_CoCo_id}

# coCoMM_CrossModelConstraint class attributes and methods

# coCoMM_SolutionConstraint class attributes and methods
coCoMM_SolutionConstraint_type: Property = Property(name="type", type=StringType)
coCoMM_SolutionConstraint.attributes={coCoMM_SolutionConstraint_type}

# coCoMM_ConfigurationConstraint class attributes and methods
coCoMM_ConfigurationConstraint_type: Property = Property(name="type", type=StringType)
coCoMM_ConfigurationConstraint_id: Property = Property(name="id", type=StringType)
coCoMM_ConfigurationConstraint_name: Property = Property(name="name", type=StringType)
coCoMM_ConfigurationConstraint.attributes={coCoMM_ConfigurationConstraint_id, coCoMM_ConfigurationConstraint_name, coCoMM_ConfigurationConstraint_type}

# coCoMM_Project class attributes and methods
coCoMM_Project_name: Property = Property(name="name", type=StringType)
coCoMM_Project_date: Property = Property(name="date", type=DateType)
coCoMM_Project_target: Property = Property(name="target", type=BooleanType)
coCoMM_Project.attributes={coCoMM_Project_name, coCoMM_Project_target, coCoMM_Project_date}

# coCoMM_Stakeholder class attributes and methods
coCoMM_Stakeholder_name: Property = Property(name="name", type=StringType)
coCoMM_Stakeholder_job: Property = Property(name="job", type=StringType)
coCoMM_Stakeholder.attributes={coCoMM_Stakeholder_job, coCoMM_Stakeholder_name}

# coCoMM_CTConstraintExpression class attributes and methods
coCoMM_CTConstraintExpression_op: Property = Property(name="op", type=StringType)
coCoMM_CTConstraintExpression.attributes={coCoMM_CTConstraintExpression_op}

# coCoMM_HardLimitCC class attributes and methods

# coCoMM_HardLimitCCExpression class attributes and methods
coCoMM_HardLimitCCExpression_op: Property = Property(name="op", type=StringType)
coCoMM_HardLimitCCExpression_value: Property = Property(name="value", type=StringType)
coCoMM_HardLimitCCExpression.attributes={coCoMM_HardLimitCCExpression_value, coCoMM_HardLimitCCExpression_op}

# coCoMM_AggregationFunction class attributes and methods
coCoMM_AggregationFunction_operation: Property = Property(name="operation", type=StringType)
coCoMM_AggregationFunction.attributes={coCoMM_AggregationFunction_operation}

# coCoMM_CMConstraintExpression class attributes and methods
coCoMM_CMConstraintExpression_op: Property = Property(name="op", type=StringType)
coCoMM_CMConstraintExpression.attributes={coCoMM_CMConstraintExpression_op}

# coCoMM_SelectionStateCC class attributes and methods
coCoMM_SelectionStateCC_state: Property = Property(name="state", type=StringType)
coCoMM_SelectionStateCC.attributes={coCoMM_SelectionStateCC_state}

# ConfigurationConstraint class attributes and methods

# coCoMM_OptimizationCC class attributes and methods
coCoMM_OptimizationCC_funct: Property = Property(name="funct", type=StringType)
coCoMM_OptimizationCC.attributes={coCoMM_OptimizationCC_funct}

# coCoMM_Config class attributes and methods
coCoMM_Config_selected: Property = Property(name="selected", type=BooleanType)
coCoMM_Config_type: Property = Property(name="type", type=StringType)
coCoMM_Config.attributes={coCoMM_Config_type, coCoMM_Config_selected}

# coCoMM_OptimizationSC class attributes and methods
coCoMM_OptimizationSC_funct: Property = Property(name="funct", type=StringType)
coCoMM_OptimizationSC.attributes={coCoMM_OptimizationSC_funct}

# SolutionConstraint class attributes and methods

# Relationships
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
        Property(name="coCoMM_Feature9", type=coCoMM_FeatureAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children10: BinaryAssociation = BinaryAssociation(
    name="children10",
    ends={
        Property(name="coCoMM_Feature12", type=coCoMM_TreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_TreeConstraint11", type=coCoMM_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
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
featureModels17: BinaryAssociation = BinaryAssociation(
    name="featureModels17",
    ends={
        Property(name="coCoMM_FeatureModel18", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo", type=coCoMM_FeatureModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmConstraints19: BinaryAssociation = BinaryAssociation(
    name="cmConstraints19",
    ends={
        Property(name="coCoMM_CrossModelConstraint", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo20", type=coCoMM_CrossModelConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
solutionConstraints21: BinaryAssociation = BinaryAssociation(
    name="solutionConstraints21",
    ends={
        Property(name="coCoMM_SolutionConstraint", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo22", type=coCoMM_SolutionConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configConstraints23: BinaryAssociation = BinaryAssociation(
    name="configConstraints23",
    ends={
        Property(name="coCoMM_ConfigurationConstraint", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo24", type=coCoMM_ConfigurationConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeTypes25: BinaryAssociation = BinaryAssociation(
    name="attributeTypes25",
    ends={
        Property(name="coCoMM_AttributeType27", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo26", type=coCoMM_AttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project28: BinaryAssociation = BinaryAssociation(
    name="project28",
    ends={
        Property(name="coCoMM_Project", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo29", type=coCoMM_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stakeholders30: BinaryAssociation = BinaryAssociation(
    name="stakeholders30",
    ends={
        Property(name="coCoMM_Stakeholder", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo31", type=coCoMM_Stakeholder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrType13: BinaryAssociation = BinaryAssociation(
    name="attrType13",
    ends={
        Property(name="coCoMM_AttributeType", type=coCoMM_FeatureAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_FeatureAttribute14", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
expressions15: BinaryAssociation = BinaryAssociation(
    name="expressions15",
    ends={
        Property(name="coCoMM_CTConstraintExpression", type=coCoMM_CrossTreeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CrossTreeConstraint16", type=coCoMM_CTConstraintExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
featureModel34: BinaryAssociation = BinaryAssociation(
    name="featureModel34",
    ends={
        Property(name="coCoMM_FeatureModel35", type=coCoMM_SelectionStateCC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_SelectionStateCC", type=coCoMM_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)
feature36: BinaryAssociation = BinaryAssociation(
    name="feature36",
    ends={
        Property(name="coCoMM_Feature38", type=coCoMM_SelectionStateCC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_SelectionStateCC37", type=coCoMM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
expressions39: BinaryAssociation = BinaryAssociation(
    name="expressions39",
    ends={
        Property(name="coCoMM_HardLimitCCExpression", type=coCoMM_HardLimitCC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_HardLimitCC", type=coCoMM_HardLimitCCExpression, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
function40: BinaryAssociation = BinaryAssociation(
    name="function40",
    ends={
        Property(name="coCoMM_AggregationFunction", type=coCoMM_HardLimitCC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_HardLimitCC41", type=coCoMM_AggregationFunction, multiplicity=Multiplicity(1, 1))
    }
)
expressions32: BinaryAssociation = BinaryAssociation(
    name="expressions32",
    ends={
        Property(name="coCoMM_CMConstraintExpression", type=coCoMM_CrossModelConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CrossModelConstraint33", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
funtion42: BinaryAssociation = BinaryAssociation(
    name="funtion42",
    ends={
        Property(name="coCoMM_AggregationFunction43", type=coCoMM_OptimizationCC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_OptimizationCC", type=coCoMM_AggregationFunction, multiplicity=Multiplicity(1, 1))
    }
)
configConstraints44: BinaryAssociation = BinaryAssociation(
    name="configConstraints44",
    ends={
        Property(name="coCoMM_ConfigurationConstraint46", type=coCoMM_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Project45", type=coCoMM_ConfigurationConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
stakeholder52: BinaryAssociation = BinaryAssociation(
    name="stakeholder52",
    ends={
        Property(name="coCoMM_Stakeholder54", type=coCoMM_Config, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Config53", type=coCoMM_Stakeholder, multiplicity=Multiplicity(0, 1))
    }
)
features55: BinaryAssociation = BinaryAssociation(
    name="features55",
    ends={
        Property(name="coCoMM_Feature57", type=coCoMM_Config, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Config56", type=coCoMM_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
solutionConstraints47: BinaryAssociation = BinaryAssociation(
    name="solutionConstraints47",
    ends={
        Property(name="coCoMM_SolutionConstraint49", type=coCoMM_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Project48", type=coCoMM_SolutionConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
configs50: BinaryAssociation = BinaryAssociation(
    name="configs50",
    ends={
        Property(name="coCoMM_Config", type=coCoMM_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Project51", type=coCoMM_Config, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrType70: BinaryAssociation = BinaryAssociation(
    name="attrType70",
    ends={
        Property(name="coCoMM_AttributeType72", type=coCoMM_AggregationFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_AggregationFunction71", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
features58: BinaryAssociation = BinaryAssociation(
    name="features58",
    ends={
        Property(name="coCoMM_Feature60", type=coCoMM_CTConstraintExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CTConstraintExpression59", type=coCoMM_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
expressions62: BinaryAssociation = BinaryAssociation(
    name="expressions62",
    ends={
        Property(name="coCoMM_CTConstraintExpression63", type=coCoMM_CTConstraintExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CTConstraintExpression61", type=coCoMM_CTConstraintExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features64: BinaryAssociation = BinaryAssociation(
    name="features64",
    ends={
        Property(name="coCoMM_Feature66", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CMConstraintExpression65", type=coCoMM_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
expressions68: BinaryAssociation = BinaryAssociation(
    name="expressions68",
    ends={
        Property(name="coCoMM_CMConstraintExpression69", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CMConstraintExpression67", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrType73: BinaryAssociation = BinaryAssociation(
    name="attrType73",
    ends={
        Property(name="coCoMM_AttributeType74", type=coCoMM_OptimizationSC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_OptimizationSC", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_coCoMM_HardLimitCC_ConfigurationConstraint = Generalization(general=ConfigurationConstraint, specific=coCoMM_HardLimitCC)
gen_coCoMM_SelectionStateCC_ConfigurationConstraint = Generalization(general=ConfigurationConstraint, specific=coCoMM_SelectionStateCC)
gen_coCoMM_OptimizationCC_ConfigurationConstraint = Generalization(general=ConfigurationConstraint, specific=coCoMM_OptimizationCC)
gen_coCoMM_OptimizationSC_SolutionConstraint = Generalization(general=SolutionConstraint, specific=coCoMM_OptimizationSC)

# Domain Model
domain_model = DomainModel(
    name="coCoMM",
    types={coCoMM_FeatureModel, coCoMM_FeatureAttribute, coCoMM_AttributeType, coCoMM_Feature, coCoMM_CrossTreeConstraint, coCoMM_TreeConstraint, coCoMM_CoCo, coCoMM_CrossModelConstraint, coCoMM_SolutionConstraint, coCoMM_ConfigurationConstraint, coCoMM_Project, coCoMM_Stakeholder, coCoMM_CTConstraintExpression, coCoMM_HardLimitCC, coCoMM_HardLimitCCExpression, coCoMM_AggregationFunction, coCoMM_CMConstraintExpression, coCoMM_SelectionStateCC, ConfigurationConstraint, coCoMM_OptimizationCC, coCoMM_Config, coCoMM_OptimizationSC, SolutionConstraint, TreeConstraintType, DataType, CTConstraintType, CCType, CCSelectionStateType, CMConstraintType, CCOptimizationOp, CCHardLimitOp, ConfigType, AggregationOp, SCType, OptimizationSCFunct},
    associations={featureModel5, featureAttributes8, children10, root0, ctConstraints1, treeConstraints3, featureModels17, cmConstraints19, solutionConstraints21, configConstraints23, attributeTypes25, project28, stakeholders30, attrType13, expressions15, featureModel34, feature36, expressions39, function40, expressions32, funtion42, configConstraints44, stakeholder52, features55, solutionConstraints47, configs50, attrType70, features58, expressions62, features64, expressions68, attrType73},
    generalizations={gen_coCoMM_HardLimitCC_ConfigurationConstraint, gen_coCoMM_SelectionStateCC_ConfigurationConstraint, gen_coCoMM_OptimizationCC_ConfigurationConstraint, gen_coCoMM_OptimizationSC_SolutionConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)