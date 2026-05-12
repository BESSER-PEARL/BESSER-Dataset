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
operators_CREATE = Class(name="operators_CREATE")
Operator = Class(name="Operator")
operators_TypeVariable = Class(name="operators_TypeVariable")
operators_Operator = Class(name="operators_Operator", is_abstract=True)
operators_Result = Class(name="operators_Result", is_abstract=True)
operators_EAttribute = Class(name="operators_EAttribute")
operators_EObjectReference = Class(name="operators_EObjectReference")
Result = Class(name="Result")
Referrable = Class(name="Referrable")
operators_Referrable = Class(name="operators_Referrable", is_abstract=True)
operators_EReference = Class(name="operators_EReference")
Variable = Class(name="Variable")
operators_EClass = Class(name="operators_EClass")
operators_EObject = Class(name="operators_EObject")
operators_DELETE = Class(name="operators_DELETE")
operators_ASSIGN = Class(name="operators_ASSIGN")
operators_VariableReference = Class(name="operators_VariableReference")
operators_Variable = Class(name="operators_Variable", is_abstract=True)
operators_PrimitiveReference = Class(name="operators_PrimitiveReference")
operators_SET = Class(name="operators_SET")
operators_EStructuralFeature = Class(name="operators_EStructuralFeature")
operators_MERGE = Class(name="operators_MERGE")
operators_MOVE = Class(name="operators_MOVE")
operators_SPLIT = Class(name="operators_SPLIT")
operators_StructuralFeatureSet = Class(name="operators_StructuralFeatureSet")
operators_EOperationQualifier = Class(name="operators_EOperationQualifier")
QueryVariableQualifier = Class(name="QueryVariableQualifier")
operators_EOperation = Class(name="operators_EOperation")
operators_VAR = Class(name="operators_VAR")
operators_QueryVariable = Class(name="operators_QueryVariable")
operators_QueryVariableQualifier = Class(name="operators_QueryVariableQualifier", is_abstract=True)
operators_EReferenceQualifier = Class(name="operators_EReferenceQualifier")

# operators_CREATE class attributes and methods
operators_CREATE_m_execute: Method = Method(name="execute", parameters={})
operators_CREATE.methods={operators_CREATE_m_execute}

# Operator class attributes and methods

# operators_TypeVariable class attributes and methods

# operators_Operator class attributes and methods
operators_Operator_executed: Property = Property(name="executed", type=BooleanType)
operators_Operator_m_execute: Method = Method(name="execute", parameters={})
operators_Operator.attributes={operators_Operator_executed}
operators_Operator.methods={operators_Operator_m_execute}

# operators_Result class attributes and methods

# operators_EAttribute class attributes and methods

# operators_EObjectReference class attributes and methods

# Result class attributes and methods

# Referrable class attributes and methods

# operators_Referrable class attributes and methods

# operators_EReference class attributes and methods

# Variable class attributes and methods

# operators_EClass class attributes and methods

# operators_EObject class attributes and methods

# operators_DELETE class attributes and methods
operators_DELETE_m_execute: Method = Method(name="execute", parameters={})
operators_DELETE.methods={operators_DELETE_m_execute}

# operators_ASSIGN class attributes and methods
operators_ASSIGN_value: Property = Property(name="value", type=StringType)
operators_ASSIGN_m_execute: Method = Method(name="execute", parameters={})
operators_ASSIGN.attributes={operators_ASSIGN_value}
operators_ASSIGN.methods={operators_ASSIGN_m_execute}

# operators_VariableReference class attributes and methods

# operators_Variable class attributes and methods
operators_Variable_name: Property = Property(name="name", type=StringType)
operators_Variable.attributes={operators_Variable_name}

# operators_PrimitiveReference class attributes and methods
operators_PrimitiveReference_value: Property = Property(name="value", type=StringType)
operators_PrimitiveReference.attributes={operators_PrimitiveReference_value}

# operators_SET class attributes and methods
operators_SET_m_execute: Method = Method(name="execute", parameters={})
operators_SET.methods={operators_SET_m_execute}

# operators_EStructuralFeature class attributes and methods

# operators_MERGE class attributes and methods

# operators_MOVE class attributes and methods
operators_MOVE_m_execute: Method = Method(name="execute", parameters={})
operators_MOVE.methods={operators_MOVE_m_execute}

# operators_SPLIT class attributes and methods

# operators_StructuralFeatureSet class attributes and methods

# operators_EOperationQualifier class attributes and methods

# QueryVariableQualifier class attributes and methods

# operators_EOperation class attributes and methods

# operators_VAR class attributes and methods
operators_VAR_m_execute: Method = Method(name="execute", parameters={})
operators_VAR.methods={operators_VAR_m_execute}

# operators_QueryVariable class attributes and methods

# operators_QueryVariableQualifier class attributes and methods

# operators_EReferenceQualifier class attributes and methods

# Relationships
result0: BinaryAssociation = BinaryAssociation(
    name="result0",
    ends={
        Property(name="operators_Result", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator", type=operators_Result, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute12: BinaryAssociation = BinaryAssociation(
    name="attribute12",
    ends={
        Property(name="operators_EAttribute", type=operators_ASSIGN, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ASSIGN", type=operators_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
attributeOwner13: BinaryAssociation = BinaryAssociation(
    name="attributeOwner13",
    ends={
        Property(name="operators_Referrable15", type=operators_ASSIGN, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ASSIGN14", type=operators_Referrable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newInstanceVariable1: BinaryAssociation = BinaryAssociation(
    name="newInstanceVariable1",
    ends={
        Property(name="operators_TypeVariable", type=operators_CREATE, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_CREATE", type=operators_TypeVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="operators_Referrable", type=operators_CREATE, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_CREATE3", type=operators_Referrable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentCompositeReference4: BinaryAssociation = BinaryAssociation(
    name="parentCompositeReference4",
    ends={
        Property(name="operators_EReference", type=operators_CREATE, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_CREATE5", type=operators_EReference, multiplicity=Multiplicity(1, 1))
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="operators_EClass", type=operators_TypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_TypeVariable7", type=operators_EClass, multiplicity=Multiplicity(1, 1))
    }
)
instance8: BinaryAssociation = BinaryAssociation(
    name="instance8",
    ends={
        Property(name="operators_EObject", type=operators_TypeVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_TypeVariable9", type=operators_EObject, multiplicity=Multiplicity(1, 1))
    }
)
deletion10: BinaryAssociation = BinaryAssociation(
    name="deletion10",
    ends={
        Property(name="operators_Referrable11", type=operators_DELETE, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_DELETE", type=operators_Referrable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencedVariable26: BinaryAssociation = BinaryAssociation(
    name="referencedVariable26",
    ends={
        Property(name="operators_Variable", type=operators_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_VariableReference", type=operators_Variable, multiplicity=Multiplicity(1, 1))
    }
)
elements16: BinaryAssociation = BinaryAssociation(
    name="elements16",
    ends={
        Property(name="operators_EObject17", type=operators_EObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_EObjectReference", type=operators_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
reference18: BinaryAssociation = BinaryAssociation(
    name="reference18",
    ends={
        Property(name="operators_EReference19", type=operators_SET, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_SET", type=operators_EReference, multiplicity=Multiplicity(1, 1))
    }
)
value20: BinaryAssociation = BinaryAssociation(
    name="value20",
    ends={
        Property(name="operators_Referrable22", type=operators_SET, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_SET21", type=operators_Referrable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referenceOwner23: BinaryAssociation = BinaryAssociation(
    name="referenceOwner23",
    ends={
        Property(name="operators_Referrable25", type=operators_SET, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_SET24", type=operators_Referrable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structuralFeatures39: BinaryAssociation = BinaryAssociation(
    name="structuralFeatures39",
    ends={
        Property(name="operators_EStructuralFeature", type=operators_StructuralFeatureSet, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_StructuralFeatureSet40", type=operators_EStructuralFeature, multiplicity=Multiplicity(1, 9999))
    }
)
mergeObjects41: BinaryAssociation = BinaryAssociation(
    name="mergeObjects41",
    ends={
        Property(name="operators_Referrable42", type=operators_MERGE, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_MERGE", type=operators_Referrable, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
newParent27: BinaryAssociation = BinaryAssociation(
    name="newParent27",
    ends={
        Property(name="operators_Referrable28", type=operators_MOVE, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_MOVE", type=operators_Referrable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentReference29: BinaryAssociation = BinaryAssociation(
    name="parentReference29",
    ends={
        Property(name="operators_EReference31", type=operators_MOVE, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_MOVE30", type=operators_EReference, multiplicity=Multiplicity(1, 1))
    }
)
movee32: BinaryAssociation = BinaryAssociation(
    name="movee32",
    ends={
        Property(name="operators_Referrable34", type=operators_MOVE, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_MOVE33", type=operators_Referrable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
splitSets35: BinaryAssociation = BinaryAssociation(
    name="splitSets35",
    ends={
        Property(name="operators_StructuralFeatureSet", type=operators_SPLIT, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_SPLIT", type=operators_StructuralFeatureSet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
splitObject36: BinaryAssociation = BinaryAssociation(
    name="splitObject36",
    ends={
        Property(name="operators_Referrable38", type=operators_SPLIT, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_SPLIT37", type=operators_Referrable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable51: BinaryAssociation = BinaryAssociation(
    name="variable51",
    ends={
        Property(name="QueryVariable", type=operators_QueryVariableQualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=operators_QueryVariable, multiplicity=Multiplicity(1, 1))
    }
)
operation52: BinaryAssociation = BinaryAssociation(
    name="operation52",
    ends={
        Property(name="operators_EOperation", type=operators_EOperationQualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_EOperationQualifier", type=operators_EOperation, multiplicity=Multiplicity(1, 1))
    }
)
variable43: BinaryAssociation = BinaryAssociation(
    name="variable43",
    ends={
        Property(name="operators_QueryVariable", type=operators_VAR, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_VAR", type=operators_QueryVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queryObject44: BinaryAssociation = BinaryAssociation(
    name="queryObject44",
    ends={
        Property(name="operators_Referrable46", type=operators_QueryVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_QueryVariable45", type=operators_Referrable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queryResult47: BinaryAssociation = BinaryAssociation(
    name="queryResult47",
    ends={
        Property(name="operators_Result49", type=operators_QueryVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_QueryVariable48", type=operators_Result, multiplicity=Multiplicity(1, 1))
    }
)
qualifier50: BinaryAssociation = BinaryAssociation(
    name="qualifier50",
    ends={
        Property(name="QueryVariableQualifier", type=operators_QueryVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=operators_QueryVariableQualifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference53: BinaryAssociation = BinaryAssociation(
    name="reference53",
    ends={
        Property(name="operators_EReference54", type=operators_EReferenceQualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_EReferenceQualifier", type=operators_EReference, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_operators_CREATE_Operator = Generalization(general=Operator, specific=operators_CREATE)
gen_operators_EObjectReference_Result = Generalization(general=Result, specific=operators_EObjectReference)
gen_operators_EObjectReference_Referrable = Generalization(general=Referrable, specific=operators_EObjectReference)
gen_operators_TypeVariable_Variable = Generalization(general=Variable, specific=operators_TypeVariable)
gen_operators_DELETE_Operator = Generalization(general=Operator, specific=operators_DELETE)
gen_operators_ASSIGN_Operator = Generalization(general=Operator, specific=operators_ASSIGN)
gen_operators_VariableReference_Referrable = Generalization(general=Referrable, specific=operators_VariableReference)
gen_operators_PrimitiveReference_Result = Generalization(general=Result, specific=operators_PrimitiveReference)
gen_operators_SET_Operator = Generalization(general=Operator, specific=operators_SET)
gen_operators_MERGE_Operator = Generalization(general=Operator, specific=operators_MERGE)
gen_operators_MOVE_Operator = Generalization(general=Operator, specific=operators_MOVE)
gen_operators_SPLIT_Operator = Generalization(general=Operator, specific=operators_SPLIT)
gen_operators_EOperationQualifier_QueryVariableQualifier = Generalization(general=QueryVariableQualifier, specific=operators_EOperationQualifier)
gen_operators_VAR_Operator = Generalization(general=Operator, specific=operators_VAR)
gen_operators_QueryVariable_Variable = Generalization(general=Variable, specific=operators_QueryVariable)
gen_operators_EReferenceQualifier_QueryVariableQualifier = Generalization(general=QueryVariableQualifier, specific=operators_EReferenceQualifier)


# OCL Constraints
nameNotNull: Constraint = Constraint(
    name="nameNotNull",
    context=operators_VariableReference,
    expression="context Variable inv: not(self.name = null)",
    language="OCL"
)
parameterLessOperation: Constraint = Constraint(
    name="parameterLessOperation",
    context=operators_EOperationQualifier,
    expression="context EOperationQualifier inv: self.operation.eParameters->size() = 0",
    language="OCL"
)
typeMustBeConcrete: Constraint = Constraint(
    name="typeMustBeConcrete",
    context=operators_TypeVariable,
    expression="context TypeVariable inv: not(self.type.abstract = true)",
    language="OCL"
)
containmentReference: Constraint = Constraint(
    name="containmentReference",
    context=operators_CREATE,
    expression="context CREATE inv: self.parentCompositeReference.containment = true",
    language="OCL"
)
uniqueParent: Constraint = Constraint(
    name="uniqueParent",
    context=operators_CREATE,
    expression="context CREATE inv: letvariableReference : VariableReference = self.parent.oclAsType(VariableReference),queryResult : EObjectReference = variableReference.referencedVariable.oclAsType(QueryVariable).queryResult.oclAsType(EObjectReference)inif self.parent.oclIsKindOf(EObjectReference) thenself.parent.oclAsType(EObjectReference).elements->size() = 1elseif self.parent.oclIsKindOf(VariableReference) thenif variableReference.referencedVariable.oclIsKindOf(QueryVariable) thenif variableReference.referencedVariable.oclAsType(QueryVariable).queryResult.oclIsKindOf(EObjectReference) thenqueryResult.elements->size() = 1else falseendifelse trueendifelse trueendifendif",
    language="OCL"
)
uniqueParent1: Constraint = Constraint(
    name="uniqueParent1",
    context=operators_SET,
    expression="context SET inv: letvariableReference : VariableReference = self.referenceOwner.oclAsType(VariableReference),queryResult : EObjectReference = variableReference.referencedVariable.oclAsType(QueryVariable).queryResult.oclAsType(EObjectReference)inif self.referenceOwner.oclIsKindOf(EObjectReference) thenself.referenceOwner.oclAsType(EObjectReference).elements->size() = 1elseif self.referenceOwner.oclIsKindOf(VariableReference) thenif variableReference.referencedVariable.oclIsKindOf(QueryVariable) thenif variableReference.referencedVariable.oclAsType(QueryVariable).queryResult.oclIsKindOf(EObjectReference) thenqueryResult.elements->size() = 1else falseendifelse trueendifelse trueendifendif",
    language="OCL"
)
uniqueParent2: Constraint = Constraint(
    name="uniqueParent2",
    context=operators_MOVE,
    expression="context MOVE inv: letvariableReference : VariableReference = self.newParent.oclAsType(VariableReference),queryResult : EObjectReference = variableReference.referencedVariable.oclAsType(QueryVariable).queryResult.oclAsType(EObjectReference)inif self.newParent.oclIsKindOf(EObjectReference) thenself.newParent.oclAsType(EObjectReference).elements->size() = 1elseif self.newParent.oclIsKindOf(VariableReference) thenif variableReference.referencedVariable.oclIsKindOf(QueryVariable) thenif variableReference.referencedVariable.oclAsType(QueryVariable).queryResult.oclIsKindOf(EObjectReference) thenqueryResult.elements->size() = 1else falseendifelse trueendifelse trueendifendif",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="operators",
    types={operators_CREATE, Operator, operators_TypeVariable, operators_Operator, operators_Result, operators_EAttribute, operators_EObjectReference, Result, Referrable, operators_Referrable, operators_EReference, Variable, operators_EClass, operators_EObject, operators_DELETE, operators_ASSIGN, operators_VariableReference, operators_Variable, operators_PrimitiveReference, operators_SET, operators_EStructuralFeature, operators_MERGE, operators_MOVE, operators_SPLIT, operators_StructuralFeatureSet, operators_EOperationQualifier, QueryVariableQualifier, operators_EOperation, operators_VAR, operators_QueryVariable, operators_QueryVariableQualifier, operators_EReferenceQualifier},
    associations={result0, attribute12, attributeOwner13, newInstanceVariable1, parent2, parentCompositeReference4, type6, instance8, deletion10, referencedVariable26, elements16, reference18, value20, referenceOwner23, structuralFeatures39, mergeObjects41, newParent27, parentReference29, movee32, splitSets35, splitObject36, variable51, operation52, variable43, queryObject44, queryResult47, qualifier50, reference53},
    constraints={nameNotNull, parameterLessOperation, typeMustBeConcrete, containmentReference, uniqueParent, uniqueParent1, uniqueParent2},
    generalizations={gen_operators_CREATE_Operator, gen_operators_EObjectReference_Result, gen_operators_EObjectReference_Referrable, gen_operators_TypeVariable_Variable, gen_operators_DELETE_Operator, gen_operators_ASSIGN_Operator, gen_operators_VariableReference_Referrable, gen_operators_PrimitiveReference_Result, gen_operators_SET_Operator, gen_operators_MERGE_Operator, gen_operators_MOVE_Operator, gen_operators_SPLIT_Operator, gen_operators_EOperationQualifier_QueryVariableQualifier, gen_operators_VAR_Operator, gen_operators_QueryVariable_Variable, gen_operators_EReferenceQualifier_QueryVariableQualifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)