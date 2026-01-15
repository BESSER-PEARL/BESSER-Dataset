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
ADT = Class(name="ADT")
SOS_PremisseList = Class(name="SOS::PremisseList")
SOS_Conclusion = Class(name="SOS::Conclusion")
Variable = Class(name="Variable")
SOS_Condition = Class(name="SOS::Condition", is_abstract=True)
SOS_Transition = Class(name="SOS::Transition")
Condition = Class(name="Condition")
SOS_Semantics = Class(name="SOS::Semantics")
SOS_Rule = Class(name="SOS::Rule")
SOS_adtmm_ADT = Class(name="SOS::adtmm::ADT")
SortDeclaration = Class(name="SortDeclaration")
Operation = Class(name="Operation")
CondEquation = Class(name="CondEquation")
SOS_adtmm_Sort = Class(name="SOS::adtmm::Sort", is_abstract=True)
SOS_adtmm_Operation = Class(name="SOS::adtmm::Operation")
AbstractOperation = Class(name="AbstractOperation")
Sort = Class(name="Sort")
SOS_adtmm_Variable = Class(name="SOS::adtmm::Variable")
Term = Class(name="Term")
SOS_TypeJudment = Class(name="SOS::TypeJudment")
SOS_AlgebraicCondition = Class(name="SOS::AlgebraicCondition")
AbstractEquation = Class(name="AbstractEquation")
SOS_AlgebraicConditionList = Class(name="SOS::AlgebraicConditionList")
SOS_adtmm_Equation = Class(name="SOS::adtmm::Equation")
SOS_adtmm_Inequation = Class(name="SOS::adtmm::Inequation")
SOS_adtmm_AbstractSort = Class(name="SOS::adtmm::AbstractSort", is_abstract=True)
SOS_adtmm_AtomicSort = Class(name="SOS::adtmm::AtomicSort")
SOS_adtmm_SortDeclaration = Class(name="SOS::adtmm::SortDeclaration")
SOS_adtmm_AbstractOperation = Class(name="SOS::adtmm::AbstractOperation", is_abstract=True)
SOS_adtmm_AbstractGenericOp = Class(name="SOS::adtmm::AbstractGenericOp", is_abstract=True)
SOS_set_ModelSort = Class(name="SOS::set::ModelSort")
SOS_set_SetMembership = Class(name="SOS::set::SetMembership", is_abstract=True)
SetTerm = Class(name="SetTerm")
SOS_adtmm_CondEquation = Class(name="SOS::adtmm::CondEquation")
Equation = Class(name="Equation")
SOS_adtmm_Term = Class(name="SOS::adtmm::Term", is_abstract=True)
SOS_adtmm_VariableRef = Class(name="SOS::adtmm::VariableRef")
SOS_adtmm_CTerm = Class(name="SOS::adtmm::CTerm")
SOS_adtmm_AbstractEquation = Class(name="SOS::adtmm::AbstractEquation", is_abstract=True)
VariableRef = Class(name="VariableRef")
SOS_set_ModelClassAttribute = Class(name="SOS::set::ModelClassAttribute")
SOS_set_Set = Class(name="SOS::set::Set")
SOS_set_ExistsIn = Class(name="SOS::set::ExistsIn")
SetMembership = Class(name="SetMembership")
SOS_set_ForAllIn = Class(name="SOS::set::ForAllIn")
SOS_set_SetTerm = Class(name="SOS::set::SetTerm", is_abstract=True)
SOS_set_ModelSet = Class(name="SOS::set::ModelSet")
SOS_set_SetOperator = Class(name="SOS::set::SetOperator", is_abstract=True)
SOS_set_SetConstructor = Class(name="SOS::set::SetConstructor")
set_SOS_AlgebraicConditionList = Class(name="set::SOS::AlgebraicConditionList")
SOS_set_Union = Class(name="SOS::set::Union")
SetOperator = Class(name="SetOperator")
SOS_set_Excluding = Class(name="SOS::set::Excluding")
SOS_set_Intersection = Class(name="SOS::set::Intersection")
SOS_set_ModelRelation = Class(name="SOS::set::ModelRelation")

# ADT class attributes and methods

# SOS_PremisseList class attributes and methods

# SOS_Conclusion class attributes and methods

# Variable class attributes and methods

# SOS_Condition class attributes and methods

# SOS_Transition class attributes and methods

# Condition class attributes and methods

# SOS_Semantics class attributes and methods

# SOS_Rule class attributes and methods

# SOS_adtmm_ADT class attributes and methods
SOS_adtmm_ADT_name: Property = Property(name="name", type=StringType)
SOS_adtmm_ADT.attributes={SOS_adtmm_ADT_name}

# SortDeclaration class attributes and methods

# Operation class attributes and methods

# CondEquation class attributes and methods

# SOS_adtmm_Sort class attributes and methods

# SOS_adtmm_Operation class attributes and methods

# AbstractOperation class attributes and methods

# Sort class attributes and methods

# SOS_adtmm_Variable class attributes and methods
SOS_adtmm_Variable_name: Property = Property(name="name", type=StringType)
SOS_adtmm_Variable.attributes={SOS_adtmm_Variable_name}

# Term class attributes and methods

# SOS_TypeJudment class attributes and methods

# SOS_AlgebraicCondition class attributes and methods

# AbstractEquation class attributes and methods

# SOS_AlgebraicConditionList class attributes and methods

# SOS_adtmm_Equation class attributes and methods

# SOS_adtmm_Inequation class attributes and methods

# SOS_adtmm_AbstractSort class attributes and methods

# SOS_adtmm_AtomicSort class attributes and methods

# SOS_adtmm_SortDeclaration class attributes and methods
SOS_adtmm_SortDeclaration_name: Property = Property(name="name", type=StringType)
SOS_adtmm_SortDeclaration.attributes={SOS_adtmm_SortDeclaration_name}

# SOS_adtmm_AbstractOperation class attributes and methods
SOS_adtmm_AbstractOperation_name: Property = Property(name="name", type=StringType)
SOS_adtmm_AbstractOperation.attributes={SOS_adtmm_AbstractOperation_name}

# SOS_adtmm_AbstractGenericOp class attributes and methods

# SOS_set_ModelSort class attributes and methods
SOS_set_ModelSort_className: Property = Property(name="className", type=StringType)
SOS_set_ModelSort_packageName: Property = Property(name="packageName", type=StringType)
SOS_set_ModelSort.attributes={SOS_set_ModelSort_packageName, SOS_set_ModelSort_className}

# SOS_set_SetMembership class attributes and methods

# SetTerm class attributes and methods

# SOS_adtmm_CondEquation class attributes and methods

# Equation class attributes and methods

# SOS_adtmm_Term class attributes and methods

# SOS_adtmm_VariableRef class attributes and methods

# SOS_adtmm_CTerm class attributes and methods
SOS_adtmm_CTerm_iter: Property = Property(name="iter", type=IntegerType)
SOS_adtmm_CTerm.attributes={SOS_adtmm_CTerm_iter}

# SOS_adtmm_AbstractEquation class attributes and methods

# VariableRef class attributes and methods

# SOS_set_ModelClassAttribute class attributes and methods
SOS_set_ModelClassAttribute_attributeName: Property = Property(name="attributeName", type=StringType)
SOS_set_ModelClassAttribute.attributes={SOS_set_ModelClassAttribute_attributeName}

# SOS_set_Set class attributes and methods

# SOS_set_ExistsIn class attributes and methods

# SetMembership class attributes and methods

# SOS_set_ForAllIn class attributes and methods

# SOS_set_SetTerm class attributes and methods

# SOS_set_ModelSet class attributes and methods

# SOS_set_SetOperator class attributes and methods

# SOS_set_SetConstructor class attributes and methods

# set_SOS_AlgebraicConditionList class attributes and methods

# SOS_set_Union class attributes and methods

# SetOperator class attributes and methods

# SOS_set_Excluding class attributes and methods

# SOS_set_Intersection class attributes and methods

# SOS_set_ModelRelation class attributes and methods
SOS_set_ModelRelation_referenceName: Property = Property(name="referenceName", type=StringType)
SOS_set_ModelRelation.attributes={SOS_set_ModelRelation_referenceName}

# Relationships
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="SOS_Rule", type=SOS_Semantics, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_Semantics", type=SOS_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature1: BinaryAssociation = BinaryAssociation(
    name="signature1",
    ends={
        Property(name="ADT", type=SOS_Semantics, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_Semantics2", type=ADT, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assumes3: BinaryAssociation = BinaryAssociation(
    name="assumes3",
    ends={
        Property(name="SOS_PremisseList", type=SOS_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_Rule4", type=SOS_PremisseList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concludes5: BinaryAssociation = BinaryAssociation(
    name="concludes5",
    ends={
        Property(name="SOS_Conclusion", type=SOS_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_Rule6", type=SOS_Conclusion, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedVariables7: BinaryAssociation = BinaryAssociation(
    name="ownedVariables7",
    ends={
        Property(name="Variable", type=SOS_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_Rule8", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
has9: BinaryAssociation = BinaryAssociation(
    name="has9",
    ends={
        Property(name="SOS_Condition", type=SOS_PremisseList, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_PremisseList10", type=SOS_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
next12: BinaryAssociation = BinaryAssociation(
    name="next12",
    ends={
        Property(name="SOS_PremisseList13", type=SOS_PremisseList, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_PremisseList11", type=SOS_PremisseList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
has14: BinaryAssociation = BinaryAssociation(
    name="has14",
    ends={
        Property(name="SOS_Transition", type=SOS_Conclusion, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_Conclusion15", type=SOS_Transition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
next39: BinaryAssociation = BinaryAssociation(
    name="next39",
    ends={
        Property(name="SOS_AlgebraicConditionList40", type=SOS_AlgebraicConditionList, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_AlgebraicConditionList38", type=SOS_AlgebraicConditionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedSorts41: BinaryAssociation = BinaryAssociation(
    name="ownedSorts41",
    ends={
        Property(name="SortDeclaration", type=SOS_adtmm_ADT, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_ADT", type=SortDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperations42: BinaryAssociation = BinaryAssociation(
    name="ownedOperations42",
    ends={
        Property(name="Operation", type=SOS_adtmm_ADT, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_ADT43", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedGenerators44: BinaryAssociation = BinaryAssociation(
    name="ownedGenerators44",
    ends={
        Property(name="Operation46", type=SOS_adtmm_ADT, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_ADT45", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVariables47: BinaryAssociation = BinaryAssociation(
    name="ownedVariables47",
    ends={
        Property(name="Variable49", type=SOS_adtmm_ADT, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_ADT48", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAxioms50: BinaryAssociation = BinaryAssociation(
    name="ownedAxioms50",
    ends={
        Property(name="CondEquation", type=SOS_adtmm_ADT, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_ADT51", type=CondEquation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operationSorts52: BinaryAssociation = BinaryAssociation(
    name="operationSorts52",
    ends={
        Property(name="Sort", type=SOS_adtmm_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_Operation", type=Sort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result53: BinaryAssociation = BinaryAssociation(
    name="result53",
    ends={
        Property(name="Sort55", type=SOS_adtmm_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_Operation54", type=Sort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label16: BinaryAssociation = BinaryAssociation(
    name="label16",
    ends={
        Property(name="Term", type=SOS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_Transition17", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
preState18: BinaryAssociation = BinaryAssociation(
    name="preState18",
    ends={
        Property(name="Term20", type=SOS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_Transition19", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
posState21: BinaryAssociation = BinaryAssociation(
    name="posState21",
    ends={
        Property(name="Term23", type=SOS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_Transition22", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
environment24: BinaryAssociation = BinaryAssociation(
    name="environment24",
    ends={
        Property(name="Term26", type=SOS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_Transition25", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
environment27: BinaryAssociation = BinaryAssociation(
    name="environment27",
    ends={
        Property(name="Term28", type=SOS_TypeJudment, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_TypeJudment", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftHandSide29: BinaryAssociation = BinaryAssociation(
    name="leftHandSide29",
    ends={
        Property(name="Term31", type=SOS_TypeJudment, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_TypeJudment30", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide32: BinaryAssociation = BinaryAssociation(
    name="rightHandSide32",
    ends={
        Property(name="Term34", type=SOS_TypeJudment, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_TypeJudment33", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedConditions35: BinaryAssociation = BinaryAssociation(
    name="ownedConditions35",
    ends={
        Property(name="AbstractEquation", type=SOS_AlgebraicCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_AlgebraicCondition", type=AbstractEquation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
has36: BinaryAssociation = BinaryAssociation(
    name="has36",
    ends={
        Property(name="SOS_AlgebraicCondition37", type=SOS_AlgebraicConditionList, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_AlgebraicConditionList", type=SOS_AlgebraicCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedLeftTerm74: BinaryAssociation = BinaryAssociation(
    name="ownedLeftTerm74",
    ends={
        Property(name="Term76", type=SOS_adtmm_AbstractEquation, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_AbstractEquation75", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration77: BinaryAssociation = BinaryAssociation(
    name="declaration77",
    ends={
        Property(name="SortDeclaration78", type=SOS_adtmm_AtomicSort, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_AtomicSort", type=SortDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
variableSort56: BinaryAssociation = BinaryAssociation(
    name="variableSort56",
    ends={
        Property(name="Sort57", type=SOS_adtmm_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_Variable", type=Sort, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedConditions58: BinaryAssociation = BinaryAssociation(
    name="ownedConditions58",
    ends={
        Property(name="AbstractEquation59", type=SOS_adtmm_CondEquation, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_CondEquation", type=AbstractEquation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEquation60: BinaryAssociation = BinaryAssociation(
    name="ownedEquation60",
    ends={
        Property(name="Equation", type=SOS_adtmm_CondEquation, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_CondEquation61", type=Equation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable62: BinaryAssociation = BinaryAssociation(
    name="variable62",
    ends={
        Property(name="Variable63", type=SOS_adtmm_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_VariableRef", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
ownedTerms64: BinaryAssociation = BinaryAssociation(
    name="ownedTerms64",
    ends={
        Property(name="Term65", type=SOS_adtmm_CTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_CTerm", type=Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op66: BinaryAssociation = BinaryAssociation(
    name="op66",
    ends={
        Property(name="Operation68", type=SOS_adtmm_CTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_CTerm67", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
iterTerm69: BinaryAssociation = BinaryAssociation(
    name="iterTerm69",
    ends={
        Property(name="Term71", type=SOS_adtmm_CTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_CTerm70", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRightTerm72: BinaryAssociation = BinaryAssociation(
    name="ownedRightTerm72",
    ends={
        Property(name="Term73", type=SOS_adtmm_AbstractEquation, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_adtmm_AbstractEquation", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source93: BinaryAssociation = BinaryAssociation(
    name="source93",
    ends={
        Property(name="VariableRef", type=SOS_set_ModelRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_set_ModelRelation", type=VariableRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target94: BinaryAssociation = BinaryAssociation(
    name="target94",
    ends={
        Property(name="VariableRef96", type=SOS_set_ModelRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_set_ModelRelation95", type=VariableRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selector97: BinaryAssociation = BinaryAssociation(
    name="selector97",
    ends={
        Property(name="VariableRef98", type=SOS_set_ModelClassAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_set_ModelClassAttribute", type=VariableRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sort99: BinaryAssociation = BinaryAssociation(
    name="sort99",
    ends={
        Property(name="Sort100", type=SOS_set_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_set_Set", type=Sort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide79: BinaryAssociation = BinaryAssociation(
    name="leftHandSide79",
    ends={
        Property(name="Term80", type=SOS_set_SetMembership, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_set_SetMembership", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide81: BinaryAssociation = BinaryAssociation(
    name="rightHandSide81",
    ends={
        Property(name="Term83", type=SOS_set_SetMembership, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_set_SetMembership82", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide84: BinaryAssociation = BinaryAssociation(
    name="leftHandSide84",
    ends={
        Property(name="Term85", type=SOS_set_SetOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_set_SetOperator", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide86: BinaryAssociation = BinaryAssociation(
    name="rightHandSide86",
    ends={
        Property(name="Term88", type=SOS_set_SetOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_set_SetOperator87", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
suchThat89: BinaryAssociation = BinaryAssociation(
    name="suchThat89",
    ends={
        Property(name="set_SOS_AlgebraicConditionList", type=SOS_set_SetConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_set_SetConstructor", type=set_SOS_AlgebraicConditionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member90: BinaryAssociation = BinaryAssociation(
    name="member90",
    ends={
        Property(name="Term92", type=SOS_set_SetConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="SOS_set_SetConstructor91", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_SOS_Transition_Condition = Generalization(general=Condition, specific=SOS_Transition)
gen_SOS_adtmm_Operation_AbstractOperation = Generalization(general=AbstractOperation, specific=SOS_adtmm_Operation)
gen_SOS_TypeJudment_Condition = Generalization(general=Condition, specific=SOS_TypeJudment)
gen_SOS_AlgebraicCondition_Condition = Generalization(general=Condition, specific=SOS_AlgebraicCondition)
gen_SOS_adtmm_Equation_AbstractEquation = Generalization(general=AbstractEquation, specific=SOS_adtmm_Equation)
gen_SOS_adtmm_Inequation_AbstractEquation = Generalization(general=AbstractEquation, specific=SOS_adtmm_Inequation)
gen_SOS_adtmm_AtomicSort_Sort = Generalization(general=Sort, specific=SOS_adtmm_AtomicSort)
gen_SOS_adtmm_AbstractGenericOp_AbstractOperation = Generalization(general=AbstractOperation, specific=SOS_adtmm_AbstractGenericOp)
gen_SOS_set_ModelSort_Sort = Generalization(general=Sort, specific=SOS_set_ModelSort)
gen_SOS_set_SetMembership_SetTerm = Generalization(general=SetTerm, specific=SOS_set_SetMembership)
gen_SOS_adtmm_VariableRef_Term = Generalization(general=Term, specific=SOS_adtmm_VariableRef)
gen_SOS_adtmm_CTerm_Term = Generalization(general=Term, specific=SOS_adtmm_CTerm)
gen_SOS_set_ModelRelation_Term = Generalization(general=Term, specific=SOS_set_ModelRelation)
gen_SOS_set_ModelClassAttribute_Term = Generalization(general=Term, specific=SOS_set_ModelClassAttribute)
gen_SOS_set_Set_Sort = Generalization(general=Sort, specific=SOS_set_Set)
gen_SOS_set_ExistsIn_SetMembership = Generalization(general=SetMembership, specific=SOS_set_ExistsIn)
gen_SOS_set_ForAllIn_SetMembership = Generalization(general=SetMembership, specific=SOS_set_ForAllIn)
gen_SOS_set_SetTerm_Term = Generalization(general=Term, specific=SOS_set_SetTerm)
gen_SOS_set_ModelSet_SetTerm = Generalization(general=SetTerm, specific=SOS_set_ModelSet)
gen_SOS_set_SetOperator_SetTerm = Generalization(general=SetTerm, specific=SOS_set_SetOperator)
gen_SOS_set_SetConstructor_SetTerm = Generalization(general=SetTerm, specific=SOS_set_SetConstructor)
gen_SOS_set_Union_SetOperator = Generalization(general=SetOperator, specific=SOS_set_Union)
gen_SOS_set_Excluding_SetOperator = Generalization(general=SetOperator, specific=SOS_set_Excluding)
gen_SOS_set_Intersection_SetOperator = Generalization(general=SetOperator, specific=SOS_set_Intersection)

# Domain Model
domain_model = DomainModel(
    name="SOS",
    types={ADT, SOS_PremisseList, SOS_Conclusion, Variable, SOS_Condition, SOS_Transition, Condition, SOS_Semantics, SOS_Rule, SOS_adtmm_ADT, SortDeclaration, Operation, CondEquation, SOS_adtmm_Sort, SOS_adtmm_Operation, AbstractOperation, Sort, SOS_adtmm_Variable, Term, SOS_TypeJudment, SOS_AlgebraicCondition, AbstractEquation, SOS_AlgebraicConditionList, SOS_adtmm_Equation, SOS_adtmm_Inequation, SOS_adtmm_AbstractSort, SOS_adtmm_AtomicSort, SOS_adtmm_SortDeclaration, SOS_adtmm_AbstractOperation, SOS_adtmm_AbstractGenericOp, SOS_set_ModelSort, SOS_set_SetMembership, SetTerm, SOS_adtmm_CondEquation, Equation, SOS_adtmm_Term, SOS_adtmm_VariableRef, SOS_adtmm_CTerm, SOS_adtmm_AbstractEquation, VariableRef, SOS_set_ModelClassAttribute, SOS_set_Set, SOS_set_ExistsIn, SetMembership, SOS_set_ForAllIn, SOS_set_SetTerm, SOS_set_ModelSet, SOS_set_SetOperator, SOS_set_SetConstructor, set_SOS_AlgebraicConditionList, SOS_set_Union, SetOperator, SOS_set_Excluding, SOS_set_Intersection, SOS_set_ModelRelation},
    associations={rules0, signature1, assumes3, concludes5, ownedVariables7, has9, next12, has14, next39, ownedSorts41, ownedOperations42, ownedGenerators44, ownedVariables47, ownedAxioms50, operationSorts52, result53, label16, preState18, posState21, environment24, environment27, leftHandSide29, rightHandSide32, ownedConditions35, has36, ownedLeftTerm74, declaration77, variableSort56, ownedConditions58, ownedEquation60, variable62, ownedTerms64, op66, iterTerm69, ownedRightTerm72, source93, target94, selector97, sort99, leftHandSide79, rightHandSide81, leftHandSide84, rightHandSide86, suchThat89, member90},
    generalizations={gen_SOS_Transition_Condition, gen_SOS_adtmm_Operation_AbstractOperation, gen_SOS_TypeJudment_Condition, gen_SOS_AlgebraicCondition_Condition, gen_SOS_adtmm_Equation_AbstractEquation, gen_SOS_adtmm_Inequation_AbstractEquation, gen_SOS_adtmm_AtomicSort_Sort, gen_SOS_adtmm_AbstractGenericOp_AbstractOperation, gen_SOS_set_ModelSort_Sort, gen_SOS_set_SetMembership_SetTerm, gen_SOS_adtmm_VariableRef_Term, gen_SOS_adtmm_CTerm_Term, gen_SOS_set_ModelRelation_Term, gen_SOS_set_ModelClassAttribute_Term, gen_SOS_set_Set_Sort, gen_SOS_set_ExistsIn_SetMembership, gen_SOS_set_ForAllIn_SetMembership, gen_SOS_set_SetTerm_Term, gen_SOS_set_ModelSet_SetTerm, gen_SOS_set_SetOperator_SetTerm, gen_SOS_set_SetConstructor_SetTerm, gen_SOS_set_Union_SetOperator, gen_SOS_set_Excluding_SetOperator, gen_SOS_set_Intersection_SetOperator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)