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
qvtcore_cst_AreaCS = Class(name="qvtcore::cst::AreaCS", is_abstract=True)
IdentifiedCS = Class(name="IdentifiedCS")
GuardPatternCS = Class(name="GuardPatternCS")
BottomPatternCS = Class(name="BottomPatternCS")
qvtcore_cst_AssignmentCS = Class(name="qvtcore::cst::AssignmentCS")
OCLExpressionCS = Class(name="OCLExpressionCS")
qvtcore_cst_BottomPatternCS = Class(name="qvtcore::cst::BottomPatternCS")
PatternCS = Class(name="PatternCS")
EnforcementOperationCS = Class(name="EnforcementOperationCS")
RealizedVariableCS = Class(name="RealizedVariableCS")
qvtcore_cst_DirectionCS = Class(name="qvtcore::cst::DirectionCS")
PathNameCS = Class(name="PathNameCS")
IdentifierCS = Class(name="IdentifierCS")
qvtcore_cst_DomainCS = Class(name="qvtcore::cst::DomainCS")
AreaCS = Class(name="AreaCS")
qvtcore_cst_EnforcementOperationCS = Class(name="qvtcore::cst::EnforcementOperationCS")
CSTNode = Class(name="CSTNode")
OperationCallExpCS = Class(name="OperationCallExpCS")
qvtcore_cst_GuardPatternCS = Class(name="qvtcore::cst::GuardPatternCS")
qvtcore_cst_MappingCS = Class(name="qvtcore::cst::MappingCS")
MappingCS = Class(name="MappingCS")
DomainCS = Class(name="DomainCS")
qvtcore_cst_ParamDeclarationCS = Class(name="qvtcore::cst::ParamDeclarationCS")
TypeCS = Class(name="TypeCS")
qvtcore_cst_PatternCS = Class(name="qvtcore::cst::PatternCS", is_abstract=True)
UnrealizedVariableCS = Class(name="UnrealizedVariableCS")
ParamDeclarationCS = Class(name="ParamDeclarationCS")
qvtcore_cst_RealizeableVariableCS = Class(name="qvtcore::cst::RealizeableVariableCS", is_abstract=True)
qvtcore_cst_RealizedVariableCS = Class(name="qvtcore::cst::RealizedVariableCS")
RealizeableVariableCS = Class(name="RealizeableVariableCS")
qvtcore_cst_TopLevelCS = Class(name="qvtcore::cst::TopLevelCS")
TransformationCS = Class(name="TransformationCS")
QueryCS = Class(name="QueryCS")
qvtcore_cst_TransformationCS = Class(name="qvtcore::cst::TransformationCS")
DirectionCS = Class(name="DirectionCS")
qvtcore_cst_UnrealizedVariableCS = Class(name="qvtcore::cst::UnrealizedVariableCS")
qvtcore_cst_QueryCS = Class(name="qvtcore::cst::QueryCS")
cst_CSTNode = Class(name="cst::CSTNode")
cst_IHasName = Class(name="cst::IHasName")

# qvtcore_cst_AreaCS class attributes and methods

# IdentifiedCS class attributes and methods

# GuardPatternCS class attributes and methods

# BottomPatternCS class attributes and methods

# qvtcore_cst_AssignmentCS class attributes and methods
qvtcore_cst_AssignmentCS_default: Property = Property(name="default", type=BooleanType)
qvtcore_cst_AssignmentCS.attributes={qvtcore_cst_AssignmentCS_default}

# OCLExpressionCS class attributes and methods

# qvtcore_cst_BottomPatternCS class attributes and methods

# PatternCS class attributes and methods

# EnforcementOperationCS class attributes and methods

# RealizedVariableCS class attributes and methods

# qvtcore_cst_DirectionCS class attributes and methods

# PathNameCS class attributes and methods

# IdentifierCS class attributes and methods

# qvtcore_cst_DomainCS class attributes and methods
qvtcore_cst_DomainCS_check: Property = Property(name="check", type=BooleanType)
qvtcore_cst_DomainCS_enforce: Property = Property(name="enforce", type=BooleanType)
qvtcore_cst_DomainCS.attributes={qvtcore_cst_DomainCS_enforce, qvtcore_cst_DomainCS_check}

# AreaCS class attributes and methods

# qvtcore_cst_EnforcementOperationCS class attributes and methods
qvtcore_cst_EnforcementOperationCS_deletion: Property = Property(name="deletion", type=BooleanType)
qvtcore_cst_EnforcementOperationCS.attributes={qvtcore_cst_EnforcementOperationCS_deletion}

# CSTNode class attributes and methods

# OperationCallExpCS class attributes and methods

# qvtcore_cst_GuardPatternCS class attributes and methods

# qvtcore_cst_MappingCS class attributes and methods

# MappingCS class attributes and methods

# DomainCS class attributes and methods

# qvtcore_cst_ParamDeclarationCS class attributes and methods

# TypeCS class attributes and methods

# qvtcore_cst_PatternCS class attributes and methods

# UnrealizedVariableCS class attributes and methods

# ParamDeclarationCS class attributes and methods

# qvtcore_cst_RealizeableVariableCS class attributes and methods

# qvtcore_cst_RealizedVariableCS class attributes and methods

# RealizeableVariableCS class attributes and methods

# qvtcore_cst_TopLevelCS class attributes and methods

# TransformationCS class attributes and methods

# QueryCS class attributes and methods

# qvtcore_cst_TransformationCS class attributes and methods

# DirectionCS class attributes and methods

# qvtcore_cst_UnrealizedVariableCS class attributes and methods

# qvtcore_cst_QueryCS class attributes and methods

# cst_CSTNode class attributes and methods

# cst_IHasName class attributes and methods

# Relationships
guardPattern0: BinaryAssociation = BinaryAssociation(
    name="guardPattern0",
    ends={
        Property(name="GuardPatternCS", type=qvtcore_cst_AreaCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_AreaCS", type=GuardPatternCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bottomPattern1: BinaryAssociation = BinaryAssociation(
    name="bottomPattern1",
    ends={
        Property(name="BottomPatternCS", type=qvtcore_cst_AreaCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_AreaCS2", type=BottomPatternCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="OCLExpressionCS", type=qvtcore_cst_AssignmentCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_AssignmentCS", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialiser4: BinaryAssociation = BinaryAssociation(
    name="initialiser4",
    ends={
        Property(name="OCLExpressionCS6", type=qvtcore_cst_AssignmentCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_AssignmentCS5", type=OCLExpressionCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enforcementOperations7: BinaryAssociation = BinaryAssociation(
    name="enforcementOperations7",
    ends={
        Property(name="EnforcementOperationCS", type=qvtcore_cst_BottomPatternCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_BottomPatternCS", type=EnforcementOperationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizedVariables8: BinaryAssociation = BinaryAssociation(
    name="realizedVariables8",
    ends={
        Property(name="RealizedVariableCS", type=qvtcore_cst_BottomPatternCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_BottomPatternCS9", type=RealizedVariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports10: BinaryAssociation = BinaryAssociation(
    name="imports10",
    ends={
        Property(name="PathNameCS", type=qvtcore_cst_DirectionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_DirectionCS", type=PathNameCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uses11: BinaryAssociation = BinaryAssociation(
    name="uses11",
    ends={
        Property(name="IdentifierCS", type=qvtcore_cst_DirectionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_DirectionCS12", type=IdentifierCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operationCall13: BinaryAssociation = BinaryAssociation(
    name="operationCall13",
    ends={
        Property(name="OperationCallExpCS", type=qvtcore_cst_EnforcementOperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_EnforcementOperationCS", type=OperationCallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
composedMappings14: BinaryAssociation = BinaryAssociation(
    name="composedMappings14",
    ends={
        Property(name="MappingCS", type=qvtcore_cst_MappingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_MappingCS", type=MappingCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domains15: BinaryAssociation = BinaryAssociation(
    name="domains15",
    ends={
        Property(name="DomainCS", type=qvtcore_cst_MappingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_MappingCS16", type=DomainCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in17: BinaryAssociation = BinaryAssociation(
    name="in17",
    ends={
        Property(name="PathNameCS19", type=qvtcore_cst_MappingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_MappingCS18", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
middle20: BinaryAssociation = BinaryAssociation(
    name="middle20",
    ends={
        Property(name="DomainCS22", type=qvtcore_cst_MappingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_MappingCS21", type=DomainCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refines23: BinaryAssociation = BinaryAssociation(
    name="refines23",
    ends={
        Property(name="IdentifierCS25", type=qvtcore_cst_MappingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_MappingCS24", type=IdentifierCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier26: BinaryAssociation = BinaryAssociation(
    name="identifier26",
    ends={
        Property(name="IdentifierCS27", type=qvtcore_cst_ParamDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_ParamDeclarationCS", type=IdentifierCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="TypeCS", type=qvtcore_cst_ParamDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_ParamDeclarationCS29", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints30: BinaryAssociation = BinaryAssociation(
    name="constraints30",
    ends={
        Property(name="OCLExpressionCS31", type=qvtcore_cst_PatternCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_PatternCS", type=OCLExpressionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unrealizedVariables32: BinaryAssociation = BinaryAssociation(
    name="unrealizedVariables32",
    ends={
        Property(name="UnrealizedVariableCS", type=qvtcore_cst_PatternCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_PatternCS33", type=UnrealizedVariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParamDeclaration34: BinaryAssociation = BinaryAssociation(
    name="inputParamDeclaration34",
    ends={
        Property(name="ParamDeclarationCS", type=qvtcore_cst_QueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_QueryCS", type=ParamDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oclExpression35: BinaryAssociation = BinaryAssociation(
    name="oclExpression35",
    ends={
        Property(name="OCLExpressionCS37", type=qvtcore_cst_QueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_QueryCS36", type=OCLExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathName38: BinaryAssociation = BinaryAssociation(
    name="pathName38",
    ends={
        Property(name="PathNameCS40", type=qvtcore_cst_QueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_QueryCS39", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type41: BinaryAssociation = BinaryAssociation(
    name="type41",
    ends={
        Property(name="TypeCS43", type=qvtcore_cst_QueryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_QueryCS42", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type44: BinaryAssociation = BinaryAssociation(
    name="type44",
    ends={
        Property(name="TypeCS45", type=qvtcore_cst_RealizeableVariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_RealizeableVariableCS", type=TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transformations46: BinaryAssociation = BinaryAssociation(
    name="transformations46",
    ends={
        Property(name="TransformationCS", type=qvtcore_cst_TopLevelCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_TopLevelCS", type=TransformationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries47: BinaryAssociation = BinaryAssociation(
    name="queries47",
    ends={
        Property(name="QueryCS", type=qvtcore_cst_TopLevelCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_TopLevelCS48", type=QueryCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings49: BinaryAssociation = BinaryAssociation(
    name="mappings49",
    ends={
        Property(name="MappingCS51", type=qvtcore_cst_TopLevelCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_TopLevelCS50", type=MappingCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
directions52: BinaryAssociation = BinaryAssociation(
    name="directions52",
    ends={
        Property(name="DirectionCS", type=qvtcore_cst_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_TransformationCS", type=DirectionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathName53: BinaryAssociation = BinaryAssociation(
    name="pathName53",
    ends={
        Property(name="PathNameCS55", type=qvtcore_cst_TransformationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_cst_TransformationCS54", type=PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_qvtcore_cst_AssignmentCS_OCLExpressionCS = Generalization(general=OCLExpressionCS, specific=qvtcore_cst_AssignmentCS)
gen_qvtcore_cst_BottomPatternCS_PatternCS = Generalization(general=PatternCS, specific=qvtcore_cst_BottomPatternCS)
gen_qvtcore_cst_DirectionCS_IdentifiedCS = Generalization(general=IdentifiedCS, specific=qvtcore_cst_DirectionCS)
gen_qvtcore_cst_DomainCS_AreaCS = Generalization(general=AreaCS, specific=qvtcore_cst_DomainCS)
gen_qvtcore_cst_AreaCS_IdentifiedCS = Generalization(general=IdentifiedCS, specific=qvtcore_cst_AreaCS)
gen_qvtcore_cst_EnforcementOperationCS_CSTNode = Generalization(general=CSTNode, specific=qvtcore_cst_EnforcementOperationCS)
gen_qvtcore_cst_GuardPatternCS_PatternCS = Generalization(general=PatternCS, specific=qvtcore_cst_GuardPatternCS)
gen_qvtcore_cst_MappingCS_IdentifiedCS = Generalization(general=IdentifiedCS, specific=qvtcore_cst_MappingCS)
gen_qvtcore_cst_ParamDeclarationCS_CSTNode = Generalization(general=CSTNode, specific=qvtcore_cst_ParamDeclarationCS)
gen_qvtcore_cst_PatternCS_CSTNode = Generalization(general=CSTNode, specific=qvtcore_cst_PatternCS)
gen_qvtcore_cst_RealizeableVariableCS_IdentifiedCS = Generalization(general=IdentifiedCS, specific=qvtcore_cst_RealizeableVariableCS)
gen_qvtcore_cst_RealizedVariableCS_RealizeableVariableCS = Generalization(general=RealizeableVariableCS, specific=qvtcore_cst_RealizedVariableCS)
gen_qvtcore_cst_TopLevelCS_CSTNode = Generalization(general=CSTNode, specific=qvtcore_cst_TopLevelCS)
gen_qvtcore_cst_TransformationCS_cst_CSTNode = Generalization(general=cst_CSTNode, specific=qvtcore_cst_TransformationCS)
gen_qvtcore_cst_TransformationCS_cst_IHasName = Generalization(general=cst_IHasName, specific=qvtcore_cst_TransformationCS)
gen_qvtcore_cst_UnrealizedVariableCS_RealizeableVariableCS = Generalization(general=RealizeableVariableCS, specific=qvtcore_cst_UnrealizedVariableCS)
gen_qvtcore_cst_QueryCS_cst_CSTNode = Generalization(general=cst_CSTNode, specific=qvtcore_cst_QueryCS)
gen_qvtcore_cst_QueryCS_cst_IHasName = Generalization(general=cst_IHasName, specific=qvtcore_cst_QueryCS)

# Domain Model
domain_model = DomainModel(
    name="qvtcore",
    types={qvtcore_cst_AreaCS, IdentifiedCS, GuardPatternCS, BottomPatternCS, qvtcore_cst_AssignmentCS, OCLExpressionCS, qvtcore_cst_BottomPatternCS, PatternCS, EnforcementOperationCS, RealizedVariableCS, qvtcore_cst_DirectionCS, PathNameCS, IdentifierCS, qvtcore_cst_DomainCS, AreaCS, qvtcore_cst_EnforcementOperationCS, CSTNode, OperationCallExpCS, qvtcore_cst_GuardPatternCS, qvtcore_cst_MappingCS, MappingCS, DomainCS, qvtcore_cst_ParamDeclarationCS, TypeCS, qvtcore_cst_PatternCS, UnrealizedVariableCS, ParamDeclarationCS, qvtcore_cst_RealizeableVariableCS, qvtcore_cst_RealizedVariableCS, RealizeableVariableCS, qvtcore_cst_TopLevelCS, TransformationCS, QueryCS, qvtcore_cst_TransformationCS, DirectionCS, qvtcore_cst_UnrealizedVariableCS, qvtcore_cst_QueryCS, cst_CSTNode, cst_IHasName},
    associations={guardPattern0, bottomPattern1, target3, initialiser4, enforcementOperations7, realizedVariables8, imports10, uses11, operationCall13, composedMappings14, domains15, in17, middle20, refines23, identifier26, type28, constraints30, unrealizedVariables32, inputParamDeclaration34, oclExpression35, pathName38, type41, type44, transformations46, queries47, mappings49, directions52, pathName53},
    generalizations={gen_qvtcore_cst_AssignmentCS_OCLExpressionCS, gen_qvtcore_cst_BottomPatternCS_PatternCS, gen_qvtcore_cst_DirectionCS_IdentifiedCS, gen_qvtcore_cst_DomainCS_AreaCS, gen_qvtcore_cst_AreaCS_IdentifiedCS, gen_qvtcore_cst_EnforcementOperationCS_CSTNode, gen_qvtcore_cst_GuardPatternCS_PatternCS, gen_qvtcore_cst_MappingCS_IdentifiedCS, gen_qvtcore_cst_ParamDeclarationCS_CSTNode, gen_qvtcore_cst_PatternCS_CSTNode, gen_qvtcore_cst_RealizeableVariableCS_IdentifiedCS, gen_qvtcore_cst_RealizedVariableCS_RealizeableVariableCS, gen_qvtcore_cst_TopLevelCS_CSTNode, gen_qvtcore_cst_TransformationCS_cst_CSTNode, gen_qvtcore_cst_TransformationCS_cst_IHasName, gen_qvtcore_cst_UnrealizedVariableCS_RealizeableVariableCS, gen_qvtcore_cst_QueryCS_cst_CSTNode, gen_qvtcore_cst_QueryCS_cst_IHasName},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)