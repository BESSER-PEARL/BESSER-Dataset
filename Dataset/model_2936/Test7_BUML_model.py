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
test7_FeatureAttribute = Class(name="test7::FeatureAttribute")
test7_Feature = Class(name="test7::Feature")
test7_SolutionConstraint = Class(name="test7::SolutionConstraint")
test7_Model = Class(name="test7::Model")
test7_AttributeType = Class(name="test7::AttributeType")
test7_FeatureAttributeElement = Class(name="test7::FeatureAttributeElement")
test7_AttributeTypeElement = Class(name="test7::AttributeTypeElement")
test7_OptimizationSC = Class(name="test7::OptimizationSC")
SolutionConstraint = Class(name="SolutionConstraint")
test7_HardLimitSC = Class(name="test7::HardLimitSC")
test7_FeatureAttributeReference = Class(name="test7::FeatureAttributeReference")
test7_FiniteDomainSCValueReference = Class(name="test7::FiniteDomainSCValueReference")
test7_SelectionStateSC = Class(name="test7::SelectionStateSC")
test7_FiniteDomainSC = Class(name="test7::FiniteDomainSC")

# test7_FeatureAttribute class attributes and methods
test7_FeatureAttribute_name: Property = Property(name="name", type=StringType)
test7_FeatureAttribute.attributes={test7_FeatureAttribute_name}

# test7_Feature class attributes and methods
test7_Feature_name: Property = Property(name="name", type=StringType)
test7_Feature.attributes={test7_Feature_name}

# test7_SolutionConstraint class attributes and methods
test7_SolutionConstraint_type: Property = Property(name="type", type=StringType)
test7_SolutionConstraint_name: Property = Property(name="name", type=StringType)
test7_SolutionConstraint.attributes={test7_SolutionConstraint_type, test7_SolutionConstraint_name}

# test7_Model class attributes and methods

# test7_AttributeType class attributes and methods
test7_AttributeType_name: Property = Property(name="name", type=StringType)
test7_AttributeType.attributes={test7_AttributeType_name}

# test7_FeatureAttributeElement class attributes and methods
test7_FeatureAttributeElement_value: Property = Property(name="value", type=StringType)
test7_FeatureAttributeElement.attributes={test7_FeatureAttributeElement_value}

# test7_AttributeTypeElement class attributes and methods
test7_AttributeTypeElement_name: Property = Property(name="name", type=StringType)
test7_AttributeTypeElement_dataType: Property = Property(name="dataType", type=StringType)
test7_AttributeTypeElement.attributes={test7_AttributeTypeElement_dataType, test7_AttributeTypeElement_name}

# test7_OptimizationSC class attributes and methods
test7_OptimizationSC_funct: Property = Property(name="funct", type=StringType)
test7_OptimizationSC.attributes={test7_OptimizationSC_funct}

# SolutionConstraint class attributes and methods

# test7_HardLimitSC class attributes and methods
test7_HardLimitSC_op1: Property = Property(name="op1", type=StringType)
test7_HardLimitSC_value1: Property = Property(name="value1", type=StringType)
test7_HardLimitSC_op2: Property = Property(name="op2", type=StringType)
test7_HardLimitSC_value2: Property = Property(name="value2", type=StringType)
test7_HardLimitSC.attributes={test7_HardLimitSC_op2, test7_HardLimitSC_value2, test7_HardLimitSC_value1, test7_HardLimitSC_op1}

# test7_FeatureAttributeReference class attributes and methods

# test7_FiniteDomainSCValueReference class attributes and methods
test7_FiniteDomainSCValueReference_value: Property = Property(name="value", type=StringType)
test7_FiniteDomainSCValueReference.attributes={test7_FiniteDomainSCValueReference_value}

# test7_SelectionStateSC class attributes and methods
test7_SelectionStateSC_state: Property = Property(name="state", type=StringType)
test7_SelectionStateSC.attributes={test7_SelectionStateSC_state}

# test7_FiniteDomainSC class attributes and methods

# Relationships
attributeTypes0: BinaryAssociation = BinaryAssociation(
    name="attributeTypes0",
    ends={
        Property(name="test7_AttributeType", type=test7_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_Model", type=test7_AttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureAttributes1: BinaryAssociation = BinaryAssociation(
    name="featureAttributes1",
    ends={
        Property(name="test7_FeatureAttribute", type=test7_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_Model2", type=test7_FeatureAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="test7_Feature", type=test7_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_Model4", type=test7_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
solutionConstraints5: BinaryAssociation = BinaryAssociation(
    name="solutionConstraints5",
    ends={
        Property(name="test7_SolutionConstraint", type=test7_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_Model6", type=test7_SolutionConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrType12: BinaryAssociation = BinaryAssociation(
    name="attrType12",
    ends={
        Property(name="test7_AttributeType14", type=test7_FeatureAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_FeatureAttribute13", type=test7_AttributeType, multiplicity=Multiplicity(0, 1))
    }
)
values15: BinaryAssociation = BinaryAssociation(
    name="values15",
    ends={
        Property(name="test7_FeatureAttributeElement", type=test7_FeatureAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_FeatureAttribute16", type=test7_FeatureAttributeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements7: BinaryAssociation = BinaryAssociation(
    name="elements7",
    ends={
        Property(name="test7_AttributeTypeElement", type=test7_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_AttributeType8", type=test7_AttributeTypeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
independentAttrType10: BinaryAssociation = BinaryAssociation(
    name="independentAttrType10",
    ends={
        Property(name="test7_AttributeType11", type=test7_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_AttributeType9", type=test7_AttributeType, multiplicity=Multiplicity(0, 1))
    }
)
attrType22: BinaryAssociation = BinaryAssociation(
    name="attrType22",
    ends={
        Property(name="test7_AttributeType23", type=test7_OptimizationSC, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_OptimizationSC", type=test7_AttributeType, multiplicity=Multiplicity(0, 1))
    }
)
attrType24: BinaryAssociation = BinaryAssociation(
    name="attrType24",
    ends={
        Property(name="test7_AttributeType25", type=test7_HardLimitSC, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_HardLimitSC", type=test7_AttributeType, multiplicity=Multiplicity(0, 1))
    }
)
name17: BinaryAssociation = BinaryAssociation(
    name="name17",
    ends={
        Property(name="test7_FeatureAttribute18", type=test7_FeatureAttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_FeatureAttributeReference", type=test7_FeatureAttribute, multiplicity=Multiplicity(0, 1))
    }
)
attributes19: BinaryAssociation = BinaryAssociation(
    name="attributes19",
    ends={
        Property(name="test7_FeatureAttributeReference21", type=test7_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_Feature20", type=test7_FeatureAttributeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values33: BinaryAssociation = BinaryAssociation(
    name="values33",
    ends={
        Property(name="test7_FiniteDomainSCValueReference", type=test7_FiniteDomainSC, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_FiniteDomainSC34", type=test7_FiniteDomainSCValueReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature26: BinaryAssociation = BinaryAssociation(
    name="feature26",
    ends={
        Property(name="test7_Feature27", type=test7_SelectionStateSC, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_SelectionStateSC", type=test7_Feature, multiplicity=Multiplicity(0, 1))
    }
)
feature28: BinaryAssociation = BinaryAssociation(
    name="feature28",
    ends={
        Property(name="test7_Feature29", type=test7_FiniteDomainSC, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_FiniteDomainSC", type=test7_Feature, multiplicity=Multiplicity(0, 1))
    }
)
featureAttr30: BinaryAssociation = BinaryAssociation(
    name="featureAttr30",
    ends={
        Property(name="test7_FeatureAttribute32", type=test7_FiniteDomainSC, multiplicity=Multiplicity(1, 1)),
        Property(name="test7_FiniteDomainSC31", type=test7_FeatureAttribute, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_test7_OptimizationSC_SolutionConstraint = Generalization(general=SolutionConstraint, specific=test7_OptimizationSC)
gen_test7_HardLimitSC_SolutionConstraint = Generalization(general=SolutionConstraint, specific=test7_HardLimitSC)
gen_test7_SelectionStateSC_SolutionConstraint = Generalization(general=SolutionConstraint, specific=test7_SelectionStateSC)
gen_test7_FiniteDomainSC_SolutionConstraint = Generalization(general=SolutionConstraint, specific=test7_FiniteDomainSC)

# Domain Model
domain_model = DomainModel(
    name="test7",
    types={test7_FeatureAttribute, test7_Feature, test7_SolutionConstraint, test7_Model, test7_AttributeType, test7_FeatureAttributeElement, test7_AttributeTypeElement, test7_OptimizationSC, SolutionConstraint, test7_HardLimitSC, test7_FeatureAttributeReference, test7_FiniteDomainSCValueReference, test7_SelectionStateSC, test7_FiniteDomainSC},
    associations={attributeTypes0, featureAttributes1, features3, solutionConstraints5, attrType12, values15, elements7, independentAttrType10, attrType22, attrType24, name17, attributes19, values33, feature26, feature28, featureAttr30},
    generalizations={gen_test7_OptimizationSC_SolutionConstraint, gen_test7_HardLimitSC_SolutionConstraint, gen_test7_SelectionStateSC_SolutionConstraint, gen_test7_FiniteDomainSC_SolutionConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)