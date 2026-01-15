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
            EnumerationLiteral(name="string"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="boolean")
    }
)

TreeConstraintType: Enumeration = Enumeration(
    name="TreeConstraintType",
    literals={
            EnumerationLiteral(name="Alternative"),
			EnumerationLiteral(name="Or"),
			EnumerationLiteral(name="And")
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

CMConstraintType: Enumeration = Enumeration(
    name="CMConstraintType",
    literals={
            EnumerationLiteral(name="not"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="implies")
    }
)

SelectionStateSCType: Enumeration = Enumeration(
    name="SelectionStateSCType",
    literals={
            EnumerationLiteral(name="mandatory"),
			EnumerationLiteral(name="preferred"),
			EnumerationLiteral(name="forbidden")
    }
)

SCType: Enumeration = Enumeration(
    name="SCType",
    literals={
            EnumerationLiteral(name="hardLimit"),
			EnumerationLiteral(name="optimization"),
			EnumerationLiteral(name="finiteDomain"),
			EnumerationLiteral(name="selectionState")
    }
)

OptimizationSCFunct: Enumeration = Enumeration(
    name="OptimizationSCFunct",
    literals={
            EnumerationLiteral(name="maximize"),
			EnumerationLiteral(name="minimize")
    }
)

HardLimitSCOp: Enumeration = Enumeration(
    name="HardLimitSCOp",
    literals={
            EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="leq"),
			EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="geq")
    }
)

ConfigType: Enumeration = Enumeration(
    name="ConfigType",
    literals={
            EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output")
    }
)

ConfigScenarioType: Enumeration = Enumeration(
    name="ConfigScenarioType",
    literals={
            EnumerationLiteral(name="fmSearch"),
			EnumerationLiteral(name="fmPreferences"),
			EnumerationLiteral(name="fmConflicts"),
			EnumerationLiteral(name="fsgSearch"),
			EnumerationLiteral(name="fsgPreferences"),
			EnumerationLiteral(name="fsgConflicts")
    }
)

# Classes
coCoMM_FeatureModel = Class(name="coCoMM::FeatureModel")
coCoMM_Feature = Class(name="coCoMM::Feature")
coCoMM_FeatureAttribute = Class(name="coCoMM::FeatureAttribute")
coCoMM_CrossTreeConstraint = Class(name="coCoMM::CrossTreeConstraint")
coCoMM_TreeConstraint = Class(name="coCoMM::TreeConstraint")
coCoMM_AttributeType = Class(name="coCoMM::AttributeType")
coCoMM_AttributeTypeElement = Class(name="coCoMM::AttributeTypeElement")
coCoMM_CrossModelConstraint = Class(name="coCoMM::CrossModelConstraint")
coCoMM_SolutionConstraint = Class(name="coCoMM::SolutionConstraint")
coCoMM_Project = Class(name="coCoMM::Project")
coCoMM_FeatureAttributeElement = Class(name="coCoMM::FeatureAttributeElement")
coCoMM_CTConstraintExpression = Class(name="coCoMM::CTConstraintExpression")
coCoMM_CoCo = Class(name="coCoMM::CoCo")
coCoMM_SelectionStateSC = Class(name="coCoMM::SelectionStateSC")
SolutionConstraint = Class(name="SolutionConstraint")
coCoMM_Stakeholder = Class(name="coCoMM::Stakeholder")
coCoMM_CMConstraintExpression = Class(name="coCoMM::CMConstraintExpression")
coCoMM_OptimizationSC = Class(name="coCoMM::OptimizationSC")
coCoMM_HardLimitSC = Class(name="coCoMM::HardLimitSC")
coCoMM_HardLimitDRExpression = Class(name="coCoMM::HardLimitDRExpression")
coCoMM_Config = Class(name="coCoMM::Config")
coCoMM_FiniteDomainSC = Class(name="coCoMM::FiniteDomainSC")
coCoMM_FiniteDomainSCValue = Class(name="coCoMM::FiniteDomainSCValue")

# coCoMM_FeatureModel class attributes and methods
coCoMM_FeatureModel_name: Property = Property(name="name", type=StringType)
coCoMM_FeatureModel_isDomain: Property = Property(name="isDomain", type=BooleanType)
coCoMM_FeatureModel.attributes={coCoMM_FeatureModel_isDomain, coCoMM_FeatureModel_name}

# coCoMM_Feature class attributes and methods
coCoMM_Feature_mandatory: Property = Property(name="mandatory", type=BooleanType)
coCoMM_Feature_id: Property = Property(name="id", type=StringType)
coCoMM_Feature_name: Property = Property(name="name", type=StringType)
coCoMM_Feature_abstract: Property = Property(name="abstract", type=BooleanType)
coCoMM_Feature.attributes={coCoMM_Feature_abstract, coCoMM_Feature_id, coCoMM_Feature_name, coCoMM_Feature_mandatory}

# coCoMM_FeatureAttribute class attributes and methods
coCoMM_FeatureAttribute_name: Property = Property(name="name", type=StringType)
coCoMM_FeatureAttribute.attributes={coCoMM_FeatureAttribute_name}

# coCoMM_CrossTreeConstraint class attributes and methods

# coCoMM_TreeConstraint class attributes and methods
coCoMM_TreeConstraint_type: Property = Property(name="type", type=StringType)
coCoMM_TreeConstraint.attributes={coCoMM_TreeConstraint_type}

# coCoMM_AttributeType class attributes and methods
coCoMM_AttributeType_id: Property = Property(name="id", type=StringType)
coCoMM_AttributeType_name: Property = Property(name="name", type=StringType)
coCoMM_AttributeType.attributes={coCoMM_AttributeType_name, coCoMM_AttributeType_id}

# coCoMM_AttributeTypeElement class attributes and methods
coCoMM_AttributeTypeElement_name: Property = Property(name="name", type=StringType)
coCoMM_AttributeTypeElement_dataType: Property = Property(name="dataType", type=StringType)
coCoMM_AttributeTypeElement.attributes={coCoMM_AttributeTypeElement_name, coCoMM_AttributeTypeElement_dataType}

# coCoMM_CrossModelConstraint class attributes and methods

# coCoMM_SolutionConstraint class attributes and methods
coCoMM_SolutionConstraint_type: Property = Property(name="type", type=StringType)
coCoMM_SolutionConstraint.attributes={coCoMM_SolutionConstraint_type}

# coCoMM_Project class attributes and methods
coCoMM_Project_name: Property = Property(name="name", type=StringType)
coCoMM_Project_date: Property = Property(name="date", type=DateType)
coCoMM_Project_target: Property = Property(name="target", type=BooleanType)
coCoMM_Project.attributes={coCoMM_Project_name, coCoMM_Project_date, coCoMM_Project_target}

# coCoMM_FeatureAttributeElement class attributes and methods
coCoMM_FeatureAttributeElement_value: Property = Property(name="value", type=StringType)
coCoMM_FeatureAttributeElement.attributes={coCoMM_FeatureAttributeElement_value}

# coCoMM_CTConstraintExpression class attributes and methods
coCoMM_CTConstraintExpression_op: Property = Property(name="op", type=StringType)
coCoMM_CTConstraintExpression.attributes={coCoMM_CTConstraintExpression_op}

# coCoMM_CoCo class attributes and methods
coCoMM_CoCo_configScenario: Property = Property(name="configScenario", type=StringType)
coCoMM_CoCo.attributes={coCoMM_CoCo_configScenario}

# coCoMM_SelectionStateSC class attributes and methods
coCoMM_SelectionStateSC_state: Property = Property(name="state", type=StringType)
coCoMM_SelectionStateSC.attributes={coCoMM_SelectionStateSC_state}

# SolutionConstraint class attributes and methods

# coCoMM_Stakeholder class attributes and methods
coCoMM_Stakeholder_name: Property = Property(name="name", type=StringType)
coCoMM_Stakeholder_job: Property = Property(name="job", type=StringType)
coCoMM_Stakeholder.attributes={coCoMM_Stakeholder_name, coCoMM_Stakeholder_job}

# coCoMM_CMConstraintExpression class attributes and methods
coCoMM_CMConstraintExpression_op: Property = Property(name="op", type=StringType)
coCoMM_CMConstraintExpression.attributes={coCoMM_CMConstraintExpression_op}

# coCoMM_OptimizationSC class attributes and methods
coCoMM_OptimizationSC_funct: Property = Property(name="funct", type=StringType)
coCoMM_OptimizationSC.attributes={coCoMM_OptimizationSC_funct}

# coCoMM_HardLimitSC class attributes and methods

# coCoMM_HardLimitDRExpression class attributes and methods
coCoMM_HardLimitDRExpression_op: Property = Property(name="op", type=StringType)
coCoMM_HardLimitDRExpression_value: Property = Property(name="value", type=StringType)
coCoMM_HardLimitDRExpression.attributes={coCoMM_HardLimitDRExpression_value, coCoMM_HardLimitDRExpression_op}

# coCoMM_Config class attributes and methods
coCoMM_Config_selected: Property = Property(name="selected", type=BooleanType)
coCoMM_Config_type: Property = Property(name="type", type=StringType)
coCoMM_Config.attributes={coCoMM_Config_type, coCoMM_Config_selected}

# coCoMM_FiniteDomainSC class attributes and methods

# coCoMM_FiniteDomainSCValue class attributes and methods
coCoMM_FiniteDomainSCValue_value: Property = Property(name="value", type=StringType)
coCoMM_FiniteDomainSCValue.attributes={coCoMM_FiniteDomainSCValue_value}

# Relationships
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
elements15: BinaryAssociation = BinaryAssociation(
    name="elements15",
    ends={
        Property(name="coCoMM_AttributeType16", type=coCoMM_AttributeTypeElement, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="coCoMM_AttributeTypeElement", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1))
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
independentAttrType14: BinaryAssociation = BinaryAssociation(
    name="independentAttrType14",
    ends={
        Property(name="coCoMM_AttributeType", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_AttributeType13", type=coCoMM_AttributeType, multiplicity=Multiplicity(0, 1))
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
solutionConstraints31: BinaryAssociation = BinaryAssociation(
    name="solutionConstraints31",
    ends={
        Property(name="coCoMM_SolutionConstraint", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo32", type=coCoMM_SolutionConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeTypes33: BinaryAssociation = BinaryAssociation(
    name="attributeTypes33",
    ends={
        Property(name="coCoMM_AttributeType35", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo34", type=coCoMM_AttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="coCoMM_FeatureModel43", type=coCoMM_SelectionStateSC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_SelectionStateSC", type=coCoMM_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)
project36: BinaryAssociation = BinaryAssociation(
    name="project36",
    ends={
        Property(name="coCoMM_Project", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo37", type=coCoMM_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stakeholders38: BinaryAssociation = BinaryAssociation(
    name="stakeholders38",
    ends={
        Property(name="coCoMM_Stakeholder", type=coCoMM_CoCo, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CoCo39", type=coCoMM_Stakeholder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature44: BinaryAssociation = BinaryAssociation(
    name="feature44",
    ends={
        Property(name="coCoMM_Feature46", type=coCoMM_SelectionStateSC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_SelectionStateSC45", type=coCoMM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
expressions47: BinaryAssociation = BinaryAssociation(
    name="expressions47",
    ends={
        Property(name="coCoMM_HardLimitDRExpression", type=coCoMM_HardLimitSC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_HardLimitSC", type=coCoMM_HardLimitDRExpression, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
attrType48: BinaryAssociation = BinaryAssociation(
    name="attrType48",
    ends={
        Property(name="coCoMM_AttributeType50", type=coCoMM_HardLimitSC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_HardLimitSC49", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
solutionConstraints53: BinaryAssociation = BinaryAssociation(
    name="solutionConstraints53",
    ends={
        Property(name="coCoMM_SolutionConstraint55", type=coCoMM_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Project54", type=coCoMM_SolutionConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
configs56: BinaryAssociation = BinaryAssociation(
    name="configs56",
    ends={
        Property(name="coCoMM_Config", type=coCoMM_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_Project57", type=coCoMM_Config, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrType51: BinaryAssociation = BinaryAssociation(
    name="attrType51",
    ends={
        Property(name="coCoMM_AttributeType52", type=coCoMM_OptimizationSC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_OptimizationSC", type=coCoMM_AttributeType, multiplicity=Multiplicity(1, 1))
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
expressions74: BinaryAssociation = BinaryAssociation(
    name="expressions74",
    ends={
        Property(name="coCoMM_CMConstraintExpression75", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CMConstraintExpression73", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
features70: BinaryAssociation = BinaryAssociation(
    name="features70",
    ends={
        Property(name="coCoMM_Feature72", type=coCoMM_CMConstraintExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_CMConstraintExpression71", type=coCoMM_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
featureAttributes76: BinaryAssociation = BinaryAssociation(
    name="featureAttributes76",
    ends={
        Property(name="coCoMM_FeatureAttribute77", type=coCoMM_FiniteDomainSC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_FiniteDomainSC", type=coCoMM_FeatureAttribute, multiplicity=Multiplicity(1, 1))
    }
)
feature78: BinaryAssociation = BinaryAssociation(
    name="feature78",
    ends={
        Property(name="coCoMM_Feature80", type=coCoMM_FiniteDomainSC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_FiniteDomainSC79", type=coCoMM_Feature, multiplicity=Multiplicity(1, 1))
    }
)
values81: BinaryAssociation = BinaryAssociation(
    name="values81",
    ends={
        Property(name="coCoMM_FiniteDomainSCValue", type=coCoMM_FiniteDomainSC, multiplicity=Multiplicity(1, 1)),
        Property(name="coCoMM_FiniteDomainSC82", type=coCoMM_FiniteDomainSCValue, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_coCoMM_SelectionStateSC_SolutionConstraint = Generalization(general=SolutionConstraint, specific=coCoMM_SelectionStateSC)
gen_coCoMM_OptimizationSC_SolutionConstraint = Generalization(general=SolutionConstraint, specific=coCoMM_OptimizationSC)
gen_coCoMM_HardLimitSC_SolutionConstraint = Generalization(general=SolutionConstraint, specific=coCoMM_HardLimitSC)
gen_coCoMM_FiniteDomainSC_SolutionConstraint = Generalization(general=SolutionConstraint, specific=coCoMM_FiniteDomainSC)

# Domain Model
domain_model = DomainModel(
    name="coCoMM",
    types={coCoMM_FeatureModel, coCoMM_Feature, coCoMM_FeatureAttribute, coCoMM_CrossTreeConstraint, coCoMM_TreeConstraint, coCoMM_AttributeType, coCoMM_AttributeTypeElement, coCoMM_CrossModelConstraint, coCoMM_SolutionConstraint, coCoMM_Project, coCoMM_FeatureAttributeElement, coCoMM_CTConstraintExpression, coCoMM_CoCo, coCoMM_SelectionStateSC, SolutionConstraint, coCoMM_Stakeholder, coCoMM_CMConstraintExpression, coCoMM_OptimizationSC, coCoMM_HardLimitSC, coCoMM_HardLimitDRExpression, coCoMM_Config, coCoMM_FiniteDomainSC, coCoMM_FiniteDomainSCValue, DataType, TreeConstraintType, CTConstraintType, CMConstraintType, SelectionStateSCType, SCType, OptimizationSCFunct, HardLimitSCOp, ConfigType, ConfigScenarioType},
    associations={treeConstraints3, featureModel5, featureAttributes8, children10, root0, ctConstraints1, elements15, featureAttributes17, attrType20, independentAttrType14, featureModels27, cmConstraints29, solutionConstraints31, attributeTypes33, elements23, expressions25, expressions40, featureModel42, project36, stakeholders38, feature44, expressions47, attrType48, solutionConstraints53, configs56, attrType51, stakeholder58, features61, expressions74, features64, expressions68, features70, featureAttributes76, feature78, values81},
    generalizations={gen_coCoMM_SelectionStateSC_SolutionConstraint, gen_coCoMM_OptimizationSC_SolutionConstraint, gen_coCoMM_HardLimitSC_SolutionConstraint, gen_coCoMM_FiniteDomainSC_SolutionConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)