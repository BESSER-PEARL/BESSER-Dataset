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
PrimitiveTypeEnum: Enumeration = Enumeration(
    name="PrimitiveTypeEnum",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Real"),
			EnumerationLiteral(name="UnlimitedNatural")
    }
)

# Classes
cvlmodel_VSpec = Class(name="cvlmodel::VSpec", is_abstract=True)
cvlmodel_Variable = Class(name="cvlmodel::Variable")
cvlmodel_VClassifier = Class(name="cvlmodel::VClassifier")
cvlmodel_Multiplicity = Class(name="cvlmodel::Multiplicity")
cvlmodel_Choice = Class(name="cvlmodel::Choice")
VSpec = Class(name="VSpec")
cvlmodel_ChoiceResolution = Class(name="cvlmodel::ChoiceResolution")
VSpecResolution = Class(name="VSpecResolution")
cvlmodel_VariableResolution = Class(name="cvlmodel::VariableResolution")
cvlmodel_VClassifierResolution = Class(name="cvlmodel::VClassifierResolution")
cvlmodel_VariationPoint = Class(name="cvlmodel::VariationPoint", is_abstract=True)
cvlmodel_VSpecResolution = Class(name="cvlmodel::VSpecResolution", is_abstract=True)
cvlmodel_ObjectExistence = Class(name="cvlmodel::ObjectExistence")
VariationPoint = Class(name="VariationPoint")
cvlmodel_VSpecTree = Class(name="cvlmodel::VSpecTree")
cvlmodel_StringToMOFRefMap = Class(name="cvlmodel::StringToMOFRefMap")
cvlmodel_MOFRef = Class(name="cvlmodel::MOFRef")
cvlmodel_ResolutionModel = Class(name="cvlmodel::ResolutionModel")
cvlmodel_CVLModel = Class(name="cvlmodel::CVLModel")

# cvlmodel_VSpec class attributes and methods
cvlmodel_VSpec_name: Property = Property(name="name", type=StringType)
cvlmodel_VSpec_mandatory: Property = Property(name="mandatory", type=StringType)
cvlmodel_VSpec_m_isRoot: Method = Method(name="isRoot", parameters={}, type=StringType)
cvlmodel_VSpec_m_isCloneable: Method = Method(name="isCloneable", parameters={}, type=StringType)
cvlmodel_VSpec_m_isClon: Method = Method(name="isClon", parameters={}, type=StringType)
cvlmodel_VSpec.attributes={cvlmodel_VSpec_mandatory, cvlmodel_VSpec_name}
cvlmodel_VSpec.methods={cvlmodel_VSpec_m_isClon, cvlmodel_VSpec_m_isCloneable, cvlmodel_VSpec_m_isRoot}

# cvlmodel_Variable class attributes and methods
cvlmodel_Variable_type: Property = Property(name="type", type=StringType)
cvlmodel_Variable.attributes={cvlmodel_Variable_type}

# cvlmodel_VClassifier class attributes and methods

# cvlmodel_Multiplicity class attributes and methods
cvlmodel_Multiplicity_min: Property = Property(name="min", type=StringType)
cvlmodel_Multiplicity_max: Property = Property(name="max", type=StringType)
cvlmodel_Multiplicity.attributes={cvlmodel_Multiplicity_min, cvlmodel_Multiplicity_max}

# cvlmodel_Choice class attributes and methods

# VSpec class attributes and methods

# cvlmodel_ChoiceResolution class attributes and methods
cvlmodel_ChoiceResolution_decision: Property = Property(name="decision", type=StringType)
cvlmodel_ChoiceResolution.attributes={cvlmodel_ChoiceResolution_decision}

# VSpecResolution class attributes and methods

# cvlmodel_VariableResolution class attributes and methods
cvlmodel_VariableResolution_value: Property = Property(name="value", type=StringType)
cvlmodel_VariableResolution.attributes={cvlmodel_VariableResolution_value}

# cvlmodel_VClassifierResolution class attributes and methods
cvlmodel_VClassifierResolution_instance: Property = Property(name="instance", type=StringType)
cvlmodel_VClassifierResolution.attributes={cvlmodel_VClassifierResolution_instance}

# cvlmodel_VariationPoint class attributes and methods
cvlmodel_VariationPoint_modelTransformationURL: Property = Property(name="modelTransformationURL", type=StringType)
cvlmodel_VariationPoint_modelTransformationSourceURL: Property = Property(name="modelTransformationSourceURL", type=StringType)
cvlmodel_VariationPoint_name: Property = Property(name="name", type=StringType)
cvlmodel_VariationPoint_negativeVariability: Property = Property(name="negativeVariability", type=StringType)
cvlmodel_VariationPoint.attributes={cvlmodel_VariationPoint_modelTransformationURL, cvlmodel_VariationPoint_modelTransformationSourceURL, cvlmodel_VariationPoint_name, cvlmodel_VariationPoint_negativeVariability}

# cvlmodel_VSpecResolution class attributes and methods
cvlmodel_VSpecResolution_name: Property = Property(name="name", type=StringType)
cvlmodel_VSpecResolution_m_isPossitivelyResolved: Method = Method(name="isPossitivelyResolved", parameters={}, type=StringType)
cvlmodel_VSpecResolution.attributes={cvlmodel_VSpecResolution_name}
cvlmodel_VSpecResolution.methods={cvlmodel_VSpecResolution_m_isPossitivelyResolved}

# cvlmodel_ObjectExistence class attributes and methods
cvlmodel_ObjectExistence_target: Property = Property(name="target", type=StringType)
cvlmodel_ObjectExistence.attributes={cvlmodel_ObjectExistence_target}

# VariationPoint class attributes and methods

# cvlmodel_VSpecTree class attributes and methods

# cvlmodel_StringToMOFRefMap class attributes and methods
cvlmodel_StringToMOFRefMap_key: Property = Property(name="key", type=StringType)
cvlmodel_StringToMOFRefMap.attributes={cvlmodel_StringToMOFRefMap_key}

# cvlmodel_MOFRef class attributes and methods
cvlmodel_MOFRef_id: Property = Property(name="id", type=StringType)
cvlmodel_MOFRef.attributes={cvlmodel_MOFRef_id}

# cvlmodel_ResolutionModel class attributes and methods
cvlmodel_ResolutionModel_name: Property = Property(name="name", type=StringType)
cvlmodel_ResolutionModel_m_getVSpecResolutionsForVSpec: Method = Method(name="getVSpecResolutionsForVSpec", parameters={Parameter(name='vspec')}, type=StringType)
cvlmodel_ResolutionModel.attributes={cvlmodel_ResolutionModel_name}
cvlmodel_ResolutionModel.methods={cvlmodel_ResolutionModel_m_getVSpecResolutionsForVSpec}

# cvlmodel_CVLModel class attributes and methods
cvlmodel_CVLModel_name: Property = Property(name="name", type=StringType)
cvlmodel_CVLModel.attributes={cvlmodel_CVLModel_name}

# Relationships
children7: BinaryAssociation = BinaryAssociation(
    name="children7",
    ends={
        Property(name="cvlmodel_VSpec9", type=cvlmodel_Multiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_Multiplicity8", type=cvlmodel_VSpec, multiplicity=Multiplicity(0, 9999))
    }
)
groupMultiplicity0: BinaryAssociation = BinaryAssociation(
    name="groupMultiplicity0",
    ends={
        Property(name="cvlmodel_Multiplicity", type=cvlmodel_VSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_VSpec", type=cvlmodel_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="cvlmodel_VSpec3", type=cvlmodel_VSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_VSpec1", type=cvlmodel_VSpec, multiplicity=Multiplicity(0, 1))
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="cvlmodel_VSpec6", type=cvlmodel_VSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_VSpec4", type=cvlmodel_VSpec, multiplicity=Multiplicity(0, 9999))
    }
)
instanceMultiplicity10: BinaryAssociation = BinaryAssociation(
    name="instanceMultiplicity10",
    ends={
        Property(name="cvlmodel_Multiplicity11", type=cvlmodel_VClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_VClassifier", type=cvlmodel_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resolvedVSpec12: BinaryAssociation = BinaryAssociation(
    name="resolvedVSpec12",
    ends={
        Property(name="cvlmodel_VSpec13", type=cvlmodel_VSpecResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_VSpecResolution", type=cvlmodel_VSpec, multiplicity=Multiplicity(1, 1))
    }
)
value18: BinaryAssociation = BinaryAssociation(
    name="value18",
    ends={
        Property(name="cvlmodel_MOFRef", type=cvlmodel_StringToMOFRefMap, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_StringToMOFRefMap19", type=cvlmodel_MOFRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vspecs20: BinaryAssociation = BinaryAssociation(
    name="vspecs20",
    ends={
        Property(name="cvlmodel_VSpec21", type=cvlmodel_VSpecTree, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_VSpecTree", type=cvlmodel_VSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root22: BinaryAssociation = BinaryAssociation(
    name="root22",
    ends={
        Property(name="cvlmodel_VSpec24", type=cvlmodel_VSpecTree, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_VSpecTree23", type=cvlmodel_VSpec, multiplicity=Multiplicity(0, 1))
    }
)
binding14: BinaryAssociation = BinaryAssociation(
    name="binding14",
    ends={
        Property(name="cvlmodel_VSpec15", type=cvlmodel_VariationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_VariationPoint", type=cvlmodel_VSpec, multiplicity=Multiplicity(1, 1))
    }
)
references16: BinaryAssociation = BinaryAssociation(
    name="references16",
    ends={
        Property(name="cvlmodel_StringToMOFRefMap", type=cvlmodel_VariationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_VariationPoint17", type=cvlmodel_StringToMOFRefMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolutions25: BinaryAssociation = BinaryAssociation(
    name="resolutions25",
    ends={
        Property(name="cvlmodel_VSpecResolution26", type=cvlmodel_ResolutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_ResolutionModel", type=cvlmodel_VSpecResolution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolvedVSpec27: BinaryAssociation = BinaryAssociation(
    name="resolvedVSpec27",
    ends={
        Property(name="cvlmodel_VSpecTree29", type=cvlmodel_ResolutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_ResolutionModel28", type=cvlmodel_VSpecTree, multiplicity=Multiplicity(1, 1))
    }
)
vspecTree30: BinaryAssociation = BinaryAssociation(
    name="vspecTree30",
    ends={
        Property(name="cvlmodel_VSpecTree31", type=cvlmodel_CVLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_CVLModel", type=cvlmodel_VSpecTree, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variationPoints32: BinaryAssociation = BinaryAssociation(
    name="variationPoints32",
    ends={
        Property(name="cvlmodel_VariationPoint34", type=cvlmodel_CVLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cvlmodel_CVLModel33", type=cvlmodel_VariationPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cvlmodel_Variable_VSpec = Generalization(general=VSpec, specific=cvlmodel_Variable)
gen_cvlmodel_VClassifier_VSpec = Generalization(general=VSpec, specific=cvlmodel_VClassifier)
gen_cvlmodel_Choice_VSpec = Generalization(general=VSpec, specific=cvlmodel_Choice)
gen_cvlmodel_ChoiceResolution_VSpecResolution = Generalization(general=VSpecResolution, specific=cvlmodel_ChoiceResolution)
gen_cvlmodel_VariableResolution_VSpecResolution = Generalization(general=VSpecResolution, specific=cvlmodel_VariableResolution)
gen_cvlmodel_VClassifierResolution_VSpecResolution = Generalization(general=VSpecResolution, specific=cvlmodel_VClassifierResolution)
gen_cvlmodel_ObjectExistence_VariationPoint = Generalization(general=VariationPoint, specific=cvlmodel_ObjectExistence)

# Domain Model
domain_model = DomainModel(
    name="cvlmodel",
    types={cvlmodel_VSpec, cvlmodel_Variable, cvlmodel_VClassifier, cvlmodel_Multiplicity, cvlmodel_Choice, VSpec, cvlmodel_ChoiceResolution, VSpecResolution, cvlmodel_VariableResolution, cvlmodel_VClassifierResolution, cvlmodel_VariationPoint, cvlmodel_VSpecResolution, cvlmodel_ObjectExistence, VariationPoint, cvlmodel_VSpecTree, cvlmodel_StringToMOFRefMap, cvlmodel_MOFRef, cvlmodel_ResolutionModel, cvlmodel_CVLModel, PrimitiveTypeEnum},
    associations={children7, groupMultiplicity0, parent2, children5, instanceMultiplicity10, resolvedVSpec12, value18, vspecs20, root22, binding14, references16, resolutions25, resolvedVSpec27, vspecTree30, variationPoints32},
    generalizations={gen_cvlmodel_Variable_VSpec, gen_cvlmodel_VClassifier_VSpec, gen_cvlmodel_Choice_VSpec, gen_cvlmodel_ChoiceResolution_VSpecResolution, gen_cvlmodel_VariableResolution_VSpecResolution, gen_cvlmodel_VClassifierResolution_VSpecResolution, gen_cvlmodel_ObjectExistence_VariationPoint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)