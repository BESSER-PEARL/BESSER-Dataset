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
atlext_ATL_LocatedElement = Class(name="atlext::ATL::LocatedElement")
ATL_atlext_EObject = Class(name="ATL::atlext::EObject")
StringToStringMap = Class(name="StringToStringMap")
atlext_ATL_StringToStringMap = Class(name="atlext::ATL::StringToStringMap")
atlext_ATL_MatchedRule = Class(name="atlext::ATL::MatchedRule")
atlext_ATL_OutPatternElement = Class(name="atlext::ATL::OutPatternElement")
atlext_ATL_Callable = Class(name="atlext::ATL::Callable")
PropertyCallExp = Class(name="PropertyCallExp")
CallableParameter = Class(name="CallableParameter")
atlext_ATL_CallableParameter = Class(name="atlext::ATL::CallableParameter")
ATL_atlext_Type = Class(name="ATL::atlext::Type")
VariableDeclaration = Class(name="VariableDeclaration")
atlext_ATL_ContextHelper = Class(name="atlext::ATL::ContextHelper")
atlext_ATL_Helper = Class(name="atlext::ATL::Helper")
atlext_ATL_Binding = Class(name="atlext::ATL::Binding")
RuleResolutionInfo = Class(name="RuleResolutionInfo")
atlext_ATL_RuleResolutionInfo = Class(name="atlext::ATL::RuleResolutionInfo")
MatchedRule = Class(name="MatchedRule")
atlext_OCL_TypedElement = Class(name="atlext::OCL::TypedElement", is_abstract=True)
OCL_atlext_Type = Class(name="OCL::atlext::Type")
atlext_OCL_VariableDeclaration = Class(name="atlext::OCL::VariableDeclaration")
TypedElement = Class(name="TypedElement")
atlext_OCL_OclExpression = Class(name="atlext::OCL::OclExpression")
Callable = Class(name="Callable")
ContextHelper = Class(name="ContextHelper")
atlext_OCL_OperationCallExp = Class(name="atlext::OCL::OperationCallExp")
ResolveTempResolution = Class(name="ResolveTempResolution")
atlext_OCL_ResolveTempResolution = Class(name="atlext::OCL::ResolveTempResolution")
OutPatternElement = Class(name="OutPatternElement")
atlext_OCL_JavaBody = Class(name="atlext::OCL::JavaBody")
OclExpression = Class(name="OclExpression")
atlext_OCL_GetAppliedStereotypesBody = Class(name="atlext::OCL::GetAppliedStereotypesBody")
JavaBody = Class(name="JavaBody")
atlext_OCL_PropertyCallExp = Class(name="atlext::OCL::PropertyCallExp")
OCL_atlext_EObject = Class(name="OCL::atlext::EObject")

# atlext_ATL_LocatedElement class attributes and methods
atlext_ATL_LocatedElement_fileLocation: Property = Property(name="fileLocation", type=StringType)
atlext_ATL_LocatedElement_fileObject: Property = Property(name="fileObject", type=StringType)
atlext_ATL_LocatedElement.attributes={atlext_ATL_LocatedElement_fileObject, atlext_ATL_LocatedElement_fileLocation}

# ATL_atlext_EObject class attributes and methods

# StringToStringMap class attributes and methods

# atlext_ATL_StringToStringMap class attributes and methods
atlext_ATL_StringToStringMap_key: Property = Property(name="key", type=StringType)
atlext_ATL_StringToStringMap_value: Property = Property(name="value", type=StringType)
atlext_ATL_StringToStringMap.attributes={atlext_ATL_StringToStringMap_value, atlext_ATL_StringToStringMap_key}

# atlext_ATL_MatchedRule class attributes and methods

# atlext_ATL_OutPatternElement class attributes and methods

# atlext_ATL_Callable class attributes and methods

# PropertyCallExp class attributes and methods

# CallableParameter class attributes and methods

# atlext_ATL_CallableParameter class attributes and methods
atlext_ATL_CallableParameter_name: Property = Property(name="name", type=StringType)
atlext_ATL_CallableParameter.attributes={atlext_ATL_CallableParameter_name}

# ATL_atlext_Type class attributes and methods

# VariableDeclaration class attributes and methods

# atlext_ATL_ContextHelper class attributes and methods

# atlext_ATL_Helper class attributes and methods
atlext_ATL_Helper_hasContext: Property = Property(name="hasContext", type=BooleanType)
atlext_ATL_Helper_isAttribute: Property = Property(name="isAttribute", type=BooleanType)
atlext_ATL_Helper.attributes={atlext_ATL_Helper_hasContext, atlext_ATL_Helper_isAttribute}

# atlext_ATL_Binding class attributes and methods

# RuleResolutionInfo class attributes and methods

# atlext_ATL_RuleResolutionInfo class attributes and methods

# MatchedRule class attributes and methods

# atlext_OCL_TypedElement class attributes and methods

# OCL_atlext_Type class attributes and methods

# atlext_OCL_VariableDeclaration class attributes and methods

# TypedElement class attributes and methods

# atlext_OCL_OclExpression class attributes and methods
atlext_OCL_OclExpression_implicitlyCasted: Property = Property(name="implicitlyCasted", type=BooleanType)
atlext_OCL_OclExpression.attributes={atlext_OCL_OclExpression_implicitlyCasted}

# Callable class attributes and methods

# ContextHelper class attributes and methods

# atlext_OCL_OperationCallExp class attributes and methods

# ResolveTempResolution class attributes and methods

# atlext_OCL_ResolveTempResolution class attributes and methods

# OutPatternElement class attributes and methods

# atlext_OCL_JavaBody class attributes and methods

# OclExpression class attributes and methods

# atlext_OCL_GetAppliedStereotypesBody class attributes and methods

# JavaBody class attributes and methods

# atlext_OCL_PropertyCallExp class attributes and methods
atlext_OCL_PropertyCallExp_isStaticCall: Property = Property(name="isStaticCall", type=BooleanType)
atlext_OCL_PropertyCallExp.attributes={atlext_OCL_PropertyCallExp_isStaticCall}

# OCL_atlext_EObject class attributes and methods

# Relationships
problems0: BinaryAssociation = BinaryAssociation(
    name="problems0",
    ends={
        Property(name="ATL_atlext_EObject", type=atlext_ATL_LocatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_LocatedElement", type=ATL_atlext_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
annotations1: BinaryAssociation = BinaryAssociation(
    name="annotations1",
    ends={
        Property(name="StringToStringMap", type=atlext_ATL_LocatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_LocatedElement2", type=StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledBy3: BinaryAssociation = BinaryAssociation(
    name="calledBy3",
    ends={
        Property(name="PropertyCallExp", type=atlext_ATL_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Callable", type=PropertyCallExp, multiplicity=Multiplicity(0, 9999))
    }
)
callableParameters4: BinaryAssociation = BinaryAssociation(
    name="callableParameters4",
    ends={
        Property(name="CallableParameter", type=atlext_ATL_Callable, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Callable5", type=CallableParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticType6: BinaryAssociation = BinaryAssociation(
    name="staticType6",
    ends={
        Property(name="ATL_atlext_Type", type=atlext_ATL_CallableParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CallableParameter", type=ATL_atlext_Type, multiplicity=Multiplicity(1, 1))
    }
)
paramDeclaration7: BinaryAssociation = BinaryAssociation(
    name="paramDeclaration7",
    ends={
        Property(name="VariableDeclaration", type=atlext_ATL_CallableParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_CallableParameter8", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
polymorphicCalledBy11: BinaryAssociation = BinaryAssociation(
    name="polymorphicCalledBy11",
    ends={
        Property(name="PropertyCallExp12", type=PropertyCallExp, multiplicity=Multiplicity(0, 9999)),
        Property(name="OCL", type=atlext_ATL_ContextHelper, multiplicity=Multiplicity(1, 1))
    }
)
inferredReturnType13: BinaryAssociation = BinaryAssociation(
    name="inferredReturnType13",
    ends={
        Property(name="ATL_atlext_Type14", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Helper", type=ATL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
staticReturnType15: BinaryAssociation = BinaryAssociation(
    name="staticReturnType15",
    ends={
        Property(name="ATL_atlext_Type17", type=atlext_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Helper16", type=ATL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
writtenFeature18: BinaryAssociation = BinaryAssociation(
    name="writtenFeature18",
    ends={
        Property(name="ATL_atlext_EObject19", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding", type=ATL_atlext_EObject, multiplicity=Multiplicity(1, 1))
    }
)
leftType20: BinaryAssociation = BinaryAssociation(
    name="leftType20",
    ends={
        Property(name="ATL_atlext_Type22", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding21", type=ATL_atlext_Type, multiplicity=Multiplicity(1, 1))
    }
)
resolvedBy23: BinaryAssociation = BinaryAssociation(
    name="resolvedBy23",
    ends={
        Property(name="RuleResolutionInfo", type=atlext_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_Binding24", type=RuleResolutionInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule25: BinaryAssociation = BinaryAssociation(
    name="rule25",
    ends={
        Property(name="MatchedRule", type=atlext_ATL_RuleResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleResolutionInfo", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
allInvolvedRules26: BinaryAssociation = BinaryAssociation(
    name="allInvolvedRules26",
    ends={
        Property(name="MatchedRule28", type=atlext_ATL_RuleResolutionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_RuleResolutionInfo27", type=MatchedRule, multiplicity=Multiplicity(1, 9999))
    }
)
inferredType29: BinaryAssociation = BinaryAssociation(
    name="inferredType29",
    ends={
        Property(name="OCL_atlext_Type", type=atlext_OCL_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_TypedElement", type=OCL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
staticType30: BinaryAssociation = BinaryAssociation(
    name="staticType30",
    ends={
        Property(name="OCL_atlext_Type31", type=atlext_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_VariableDeclaration", type=OCL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
noCastedType32: BinaryAssociation = BinaryAssociation(
    name="noCastedType32",
    ends={
        Property(name="OCL_atlext_Type33", type=atlext_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_OclExpression", type=OCL_atlext_Type, multiplicity=Multiplicity(0, 1))
    }
)
contextType9: BinaryAssociation = BinaryAssociation(
    name="contextType9",
    ends={
        Property(name="ATL_atlext_Type10", type=atlext_ATL_ContextHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_ATL_ContextHelper", type=ATL_atlext_Type, multiplicity=Multiplicity(1, 1))
    }
)
receptorType35: BinaryAssociation = BinaryAssociation(
    name="receptorType35",
    ends={
        Property(name="OCL_atlext_EObject37", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp36", type=OCL_atlext_EObject, multiplicity=Multiplicity(0, 1))
    }
)
staticResolver38: BinaryAssociation = BinaryAssociation(
    name="staticResolver38",
    ends={
        Property(name="Callable", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp39", type=Callable, multiplicity=Multiplicity(1, 1))
    }
)
dynamicResolvers40: BinaryAssociation = BinaryAssociation(
    name="dynamicResolvers40",
    ends={
        Property(name="ATL", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ContextHelper", type=ContextHelper, multiplicity=Multiplicity(0, 9999))
    }
)
resolveTempResolvedBy41: BinaryAssociation = BinaryAssociation(
    name="resolveTempResolvedBy41",
    ends={
        Property(name="ResolveTempResolution", type=atlext_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_OperationCallExp", type=ResolveTempResolution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element42: BinaryAssociation = BinaryAssociation(
    name="element42",
    ends={
        Property(name="OutPatternElement", type=atlext_OCL_ResolveTempResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_ResolveTempResolution", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
usedFeature34: BinaryAssociation = BinaryAssociation(
    name="usedFeature34",
    ends={
        Property(name="OCL_atlext_EObject", type=atlext_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atlext_OCL_PropertyCallExp", type=OCL_atlext_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_atlext_OCL_VariableDeclaration_TypedElement = Generalization(general=TypedElement, specific=atlext_OCL_VariableDeclaration)
gen_atlext_OCL_OclExpression_TypedElement = Generalization(general=TypedElement, specific=atlext_OCL_OclExpression)
gen_atlext_OCL_ResolveTempResolution_RuleResolutionInfo = Generalization(general=RuleResolutionInfo, specific=atlext_OCL_ResolveTempResolution)
gen_atlext_OCL_JavaBody_OclExpression = Generalization(general=OclExpression, specific=atlext_OCL_JavaBody)
gen_atlext_OCL_GetAppliedStereotypesBody_JavaBody = Generalization(general=JavaBody, specific=atlext_OCL_GetAppliedStereotypesBody)

# Domain Model
domain_model = DomainModel(
    name="atlext",
    types={atlext_ATL_LocatedElement, ATL_atlext_EObject, StringToStringMap, atlext_ATL_StringToStringMap, atlext_ATL_MatchedRule, atlext_ATL_OutPatternElement, atlext_ATL_Callable, PropertyCallExp, CallableParameter, atlext_ATL_CallableParameter, ATL_atlext_Type, VariableDeclaration, atlext_ATL_ContextHelper, atlext_ATL_Helper, atlext_ATL_Binding, RuleResolutionInfo, atlext_ATL_RuleResolutionInfo, MatchedRule, atlext_OCL_TypedElement, OCL_atlext_Type, atlext_OCL_VariableDeclaration, TypedElement, atlext_OCL_OclExpression, Callable, ContextHelper, atlext_OCL_OperationCallExp, ResolveTempResolution, atlext_OCL_ResolveTempResolution, OutPatternElement, atlext_OCL_JavaBody, OclExpression, atlext_OCL_GetAppliedStereotypesBody, JavaBody, atlext_OCL_PropertyCallExp, OCL_atlext_EObject},
    associations={problems0, annotations1, calledBy3, callableParameters4, staticType6, paramDeclaration7, polymorphicCalledBy11, inferredReturnType13, staticReturnType15, writtenFeature18, leftType20, resolvedBy23, rule25, allInvolvedRules26, inferredType29, staticType30, noCastedType32, contextType9, receptorType35, staticResolver38, dynamicResolvers40, resolveTempResolvedBy41, element42, usedFeature34},
    generalizations={gen_atlext_OCL_VariableDeclaration_TypedElement, gen_atlext_OCL_OclExpression_TypedElement, gen_atlext_OCL_ResolveTempResolution_RuleResolutionInfo, gen_atlext_OCL_JavaBody_OclExpression, gen_atlext_OCL_GetAppliedStereotypesBody_JavaBody},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)