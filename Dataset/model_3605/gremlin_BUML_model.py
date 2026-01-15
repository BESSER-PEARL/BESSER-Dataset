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
gremlin_GremlinScript = Class(name="gremlin::GremlinScript")
gremlin_Instruction = Class(name="gremlin::Instruction", is_abstract=True)
gremlin_ReturnStatement = Class(name="gremlin::ReturnStatement")
Instruction = Class(name="Instruction")
gremlin_MethodDeclaration = Class(name="gremlin::MethodDeclaration")
gremlin_TypeDeclaration = Class(name="gremlin::TypeDeclaration", is_abstract=True)
gremlin_ListDeclaration = Class(name="gremlin::ListDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
gremlin_SetDeclaration = Class(name="gremlin::SetDeclaration")
gremlin_SortedSetDeclaration = Class(name="gremlin::SortedSetDeclaration")
gremlin_VariableDeclaration = Class(name="gremlin::VariableDeclaration")
gremlin_TraversalElement = Class(name="gremlin::TraversalElement", is_abstract=True)
gremlin_CollectionDefinition = Class(name="gremlin::CollectionDefinition")
TraversalElement = Class(name="TraversalElement")
gremlin_Closure = Class(name="gremlin::Closure")
gremlin_ClosureIt = Class(name="gremlin::ClosureIt")
VariableAccess = Class(name="VariableAccess")
gremlin_VerticesStep = Class(name="gremlin::VerticesStep")
gremlin_VariableAccess = Class(name="gremlin::VariableAccess")
gremlin_Step = Class(name="gremlin::Step", is_abstract=True)
gremlin_IdentityStep = Class(name="gremlin::IdentityStep")
Step = Class(name="Step")
gremlin_FillStep = Class(name="gremlin::FillStep")
gremlin_StartStep = Class(name="gremlin::StartStep")
gremlin_RetainStep = Class(name="gremlin::RetainStep")
gremlin_EdgesStep = Class(name="gremlin::EdgesStep")
gremlin_PropertyStep = Class(name="gremlin::PropertyStep")
gremlin_OutEStep = Class(name="gremlin::OutEStep")
gremlin_InEStep = Class(name="gremlin::InEStep")
gremlin_InVStep = Class(name="gremlin::InVStep")
gremlin_OutVStep = Class(name="gremlin::OutVStep")
gremlin_FilterStep = Class(name="gremlin::FilterStep")
gremlin_ExceptStep = Class(name="gremlin::ExceptStep")
gremlin_TransformStep = Class(name="gremlin::TransformStep")
gremlin_GatherStep = Class(name="gremlin::GatherStep")
gremlin_ScatterStep = Class(name="gremlin::ScatterStep")
gremlin_MethodCall = Class(name="gremlin::MethodCall", is_abstract=True)
gremlin_CustomMethodCall = Class(name="gremlin::CustomMethodCall")
MethodCall = Class(name="MethodCall")
gremlin_ContainsCall = Class(name="gremlin::ContainsCall")
gremlin_EObject = Class(name="gremlin::EObject")
gremlin_NextCall = Class(name="gremlin::NextCall")
gremlin_HasNextCall = Class(name="gremlin::HasNextCall")
gremlin_IndexCall = Class(name="gremlin::IndexCall")
gremlin_CountCall = Class(name="gremlin::CountCall")
gremlin_FirstCall = Class(name="gremlin::FirstCall")
gremlin_ToListCall = Class(name="gremlin::ToListCall")
gremlin_IsEmptyCall = Class(name="gremlin::IsEmptyCall")
gremlin_ContainsAllCall = Class(name="gremlin::ContainsAllCall")
gremlin_AddAllCall = Class(name="gremlin::AddAllCall")
gremlin_RetainAllCall = Class(name="gremlin::RetainAllCall")
gremlin_UnionCall = Class(name="gremlin::UnionCall")
gremlin_EqualityExpression = Class(name="gremlin::EqualityExpression")
BinaryExpression = Class(name="BinaryExpression")
gremlin_IntersectionCall = Class(name="gremlin::IntersectionCall")
gremlin_SizeCall = Class(name="gremlin::SizeCall")
gremlin_Expression = Class(name="gremlin::Expression")
gremlin_UnaryExpression = Class(name="gremlin::UnaryExpression")
Expression = Class(name="Expression")
gremlin_NotExpression = Class(name="gremlin::NotExpression")
UnaryExpression = Class(name="UnaryExpression")
gremlin_BinaryExpression = Class(name="gremlin::BinaryExpression")
gremlin_InExpression = Class(name="gremlin::InExpression")
gremlin_DifferenceExpression = Class(name="gremlin::DifferenceExpression")
gremlin_OrExpression = Class(name="gremlin::OrExpression")
gremlin_AndExpression = Class(name="gremlin::AndExpression")
gremlin_GreaterExpression = Class(name="gremlin::GreaterExpression")
gremlin_GreaterOrEqualExpression = Class(name="gremlin::GreaterOrEqualExpression")
gremlin_LessExpression = Class(name="gremlin::LessExpression")
gremlin_LessOrEqualExpression = Class(name="gremlin::LessOrEqualExpression")
gremlin_AffectationExpression = Class(name="gremlin::AffectationExpression")
gremlin_LeftShiftExpression = Class(name="gremlin::LeftShiftExpression")
gremlin_TernaryOperator = Class(name="gremlin::TernaryOperator")
gremlin_BooleanLiteral = Class(name="gremlin::BooleanLiteral")
gremlin_StringLiteral = Class(name="gremlin::StringLiteral")
gremlin_IntegerLiteral = Class(name="gremlin::IntegerLiteral")
gremlin_DoubleLiteral = Class(name="gremlin::DoubleLiteral")
gremlin_NullLiteral = Class(name="gremlin::NullLiteral")
gremlin_ToIntegerCall = Class(name="gremlin::ToIntegerCall")
gremlin_PlusExpression = Class(name="gremlin::PlusExpression")
gremlin_CustomStep = Class(name="gremlin::CustomStep")

# gremlin_GremlinScript class attributes and methods
gremlin_GremlinScript_name: Property = Property(name="name", type=StringType)
gremlin_GremlinScript_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_GremlinScript.attributes={gremlin_GremlinScript_name}
gremlin_GremlinScript.methods={gremlin_GremlinScript_m_toString}

# gremlin_Instruction class attributes and methods

# gremlin_ReturnStatement class attributes and methods
gremlin_ReturnStatement_value: Property = Property(name="value", type=StringType)
gremlin_ReturnStatement_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_ReturnStatement.attributes={gremlin_ReturnStatement_value}
gremlin_ReturnStatement.methods={gremlin_ReturnStatement_m_toString}

# Instruction class attributes and methods

# gremlin_MethodDeclaration class attributes and methods
gremlin_MethodDeclaration_name: Property = Property(name="name", type=StringType)
gremlin_MethodDeclaration_parameters: Property = Property(name="parameters", type=StringType)
gremlin_MethodDeclaration_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_MethodDeclaration.attributes={gremlin_MethodDeclaration_name, gremlin_MethodDeclaration_parameters}
gremlin_MethodDeclaration.methods={gremlin_MethodDeclaration_m_toString}

# gremlin_TypeDeclaration class attributes and methods

# gremlin_ListDeclaration class attributes and methods
gremlin_ListDeclaration_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_ListDeclaration.methods={gremlin_ListDeclaration_m_toString}

# TypeDeclaration class attributes and methods

# gremlin_SetDeclaration class attributes and methods
gremlin_SetDeclaration_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_SetDeclaration.methods={gremlin_SetDeclaration_m_toString}

# gremlin_SortedSetDeclaration class attributes and methods
gremlin_SortedSetDeclaration_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_SortedSetDeclaration.methods={gremlin_SortedSetDeclaration_m_toString}

# gremlin_VariableDeclaration class attributes and methods
gremlin_VariableDeclaration_name: Property = Property(name="name", type=StringType)
gremlin_VariableDeclaration_final: Property = Property(name="final", type=BooleanType)
gremlin_VariableDeclaration_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_VariableDeclaration.attributes={gremlin_VariableDeclaration_name, gremlin_VariableDeclaration_final}
gremlin_VariableDeclaration.methods={gremlin_VariableDeclaration_m_toString}

# gremlin_TraversalElement class attributes and methods

# gremlin_CollectionDefinition class attributes and methods
gremlin_CollectionDefinition_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_CollectionDefinition.methods={gremlin_CollectionDefinition_m_toString}

# TraversalElement class attributes and methods

# gremlin_Closure class attributes and methods
gremlin_Closure_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_Closure.methods={gremlin_Closure_m_toString}

# gremlin_ClosureIt class attributes and methods
gremlin_ClosureIt_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_ClosureIt_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
gremlin_ClosureIt.methods={gremlin_ClosureIt_m_getName, gremlin_ClosureIt_m_toString}

# VariableAccess class attributes and methods

# gremlin_VerticesStep class attributes and methods
gremlin_VerticesStep_vertexId: Property = Property(name="vertexId", type=StringType)
gremlin_VerticesStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_VerticesStep.attributes={gremlin_VerticesStep_vertexId}
gremlin_VerticesStep.methods={gremlin_VerticesStep_m_toString}

# gremlin_VariableAccess class attributes and methods
gremlin_VariableAccess_name: Property = Property(name="name", type=StringType)
gremlin_VariableAccess_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_VariableAccess.attributes={gremlin_VariableAccess_name}
gremlin_VariableAccess.methods={gremlin_VariableAccess_m_toString}

# gremlin_Step class attributes and methods

# gremlin_IdentityStep class attributes and methods
gremlin_IdentityStep_needed: Property = Property(name="needed", type=BooleanType)
gremlin_IdentityStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_IdentityStep.attributes={gremlin_IdentityStep_needed}
gremlin_IdentityStep.methods={gremlin_IdentityStep_m_toString}

# Step class attributes and methods

# gremlin_FillStep class attributes and methods
gremlin_FillStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_FillStep.methods={gremlin_FillStep_m_toString}

# gremlin_StartStep class attributes and methods
gremlin_StartStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_StartStep.methods={gremlin_StartStep_m_toString}

# gremlin_RetainStep class attributes and methods
gremlin_RetainStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_RetainStep.methods={gremlin_RetainStep_m_toString}

# gremlin_EdgesStep class attributes and methods
gremlin_EdgesStep_relationshipName: Property = Property(name="relationshipName", type=StringType)
gremlin_EdgesStep.attributes={gremlin_EdgesStep_relationshipName}

# gremlin_PropertyStep class attributes and methods
gremlin_PropertyStep_name: Property = Property(name="name", type=StringType)
gremlin_PropertyStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_PropertyStep.attributes={gremlin_PropertyStep_name}
gremlin_PropertyStep.methods={gremlin_PropertyStep_m_toString}

# gremlin_OutEStep class attributes and methods
gremlin_OutEStep_relationshipName: Property = Property(name="relationshipName", type=StringType)
gremlin_OutEStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_OutEStep.attributes={gremlin_OutEStep_relationshipName}
gremlin_OutEStep.methods={gremlin_OutEStep_m_toString}

# gremlin_InEStep class attributes and methods
gremlin_InEStep_relationshipName: Property = Property(name="relationshipName", type=StringType)
gremlin_InEStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_InEStep.attributes={gremlin_InEStep_relationshipName}
gremlin_InEStep.methods={gremlin_InEStep_m_toString}

# gremlin_InVStep class attributes and methods
gremlin_InVStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_InVStep.methods={gremlin_InVStep_m_toString}

# gremlin_OutVStep class attributes and methods
gremlin_OutVStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_OutVStep.methods={gremlin_OutVStep_m_toString}

# gremlin_FilterStep class attributes and methods
gremlin_FilterStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_FilterStep.methods={gremlin_FilterStep_m_toString}

# gremlin_ExceptStep class attributes and methods
gremlin_ExceptStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_ExceptStep.methods={gremlin_ExceptStep_m_toString}

# gremlin_TransformStep class attributes and methods
gremlin_TransformStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_TransformStep.methods={gremlin_TransformStep_m_toString}

# gremlin_GatherStep class attributes and methods
gremlin_GatherStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_GatherStep.methods={gremlin_GatherStep_m_toString}

# gremlin_ScatterStep class attributes and methods
gremlin_ScatterStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_ScatterStep.methods={gremlin_ScatterStep_m_toString}

# gremlin_MethodCall class attributes and methods

# gremlin_CustomMethodCall class attributes and methods
gremlin_CustomMethodCall_name: Property = Property(name="name", type=StringType)
gremlin_CustomMethodCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_CustomMethodCall.attributes={gremlin_CustomMethodCall_name}
gremlin_CustomMethodCall.methods={gremlin_CustomMethodCall_m_toString}

# MethodCall class attributes and methods

# gremlin_ContainsCall class attributes and methods
gremlin_ContainsCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_ContainsCall.methods={gremlin_ContainsCall_m_toString}

# gremlin_EObject class attributes and methods

# gremlin_NextCall class attributes and methods
gremlin_NextCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_NextCall.methods={gremlin_NextCall_m_toString}

# gremlin_HasNextCall class attributes and methods
gremlin_HasNextCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_HasNextCall.methods={gremlin_HasNextCall_m_toString}

# gremlin_IndexCall class attributes and methods
gremlin_IndexCall_indexName: Property = Property(name="indexName", type=StringType)
gremlin_IndexCall_indexProperty: Property = Property(name="indexProperty", type=StringType)
gremlin_IndexCall_indexQuery: Property = Property(name="indexQuery", type=StringType)
gremlin_IndexCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_IndexCall.attributes={gremlin_IndexCall_indexQuery, gremlin_IndexCall_indexName, gremlin_IndexCall_indexProperty}
gremlin_IndexCall.methods={gremlin_IndexCall_m_toString}

# gremlin_CountCall class attributes and methods
gremlin_CountCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_CountCall.methods={gremlin_CountCall_m_toString}

# gremlin_FirstCall class attributes and methods
gremlin_FirstCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_FirstCall.methods={gremlin_FirstCall_m_toString}

# gremlin_ToListCall class attributes and methods
gremlin_ToListCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_ToListCall.methods={gremlin_ToListCall_m_toString}

# gremlin_IsEmptyCall class attributes and methods
gremlin_IsEmptyCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_IsEmptyCall.methods={gremlin_IsEmptyCall_m_toString}

# gremlin_ContainsAllCall class attributes and methods
gremlin_ContainsAllCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_ContainsAllCall.methods={gremlin_ContainsAllCall_m_toString}

# gremlin_AddAllCall class attributes and methods
gremlin_AddAllCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_AddAllCall.methods={gremlin_AddAllCall_m_toString}

# gremlin_RetainAllCall class attributes and methods
gremlin_RetainAllCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_RetainAllCall.methods={gremlin_RetainAllCall_m_toString}

# gremlin_UnionCall class attributes and methods
gremlin_UnionCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_UnionCall.methods={gremlin_UnionCall_m_toString}

# gremlin_EqualityExpression class attributes and methods
gremlin_EqualityExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_EqualityExpression.methods={gremlin_EqualityExpression_m_toString}

# BinaryExpression class attributes and methods

# gremlin_IntersectionCall class attributes and methods
gremlin_IntersectionCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_IntersectionCall.methods={gremlin_IntersectionCall_m_toString}

# gremlin_SizeCall class attributes and methods
gremlin_SizeCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_SizeCall.methods={gremlin_SizeCall_m_toString}

# gremlin_Expression class attributes and methods

# gremlin_UnaryExpression class attributes and methods

# Expression class attributes and methods

# gremlin_NotExpression class attributes and methods
gremlin_NotExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_NotExpression.methods={gremlin_NotExpression_m_toString}

# UnaryExpression class attributes and methods

# gremlin_BinaryExpression class attributes and methods

# gremlin_InExpression class attributes and methods
gremlin_InExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_InExpression.methods={gremlin_InExpression_m_toString}

# gremlin_DifferenceExpression class attributes and methods
gremlin_DifferenceExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_DifferenceExpression.methods={gremlin_DifferenceExpression_m_toString}

# gremlin_OrExpression class attributes and methods
gremlin_OrExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_OrExpression.methods={gremlin_OrExpression_m_toString}

# gremlin_AndExpression class attributes and methods
gremlin_AndExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_AndExpression.methods={gremlin_AndExpression_m_toString}

# gremlin_GreaterExpression class attributes and methods
gremlin_GreaterExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_GreaterExpression.methods={gremlin_GreaterExpression_m_toString}

# gremlin_GreaterOrEqualExpression class attributes and methods
gremlin_GreaterOrEqualExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_GreaterOrEqualExpression.methods={gremlin_GreaterOrEqualExpression_m_toString}

# gremlin_LessExpression class attributes and methods
gremlin_LessExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_LessExpression.methods={gremlin_LessExpression_m_toString}

# gremlin_LessOrEqualExpression class attributes and methods
gremlin_LessOrEqualExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_LessOrEqualExpression.methods={gremlin_LessOrEqualExpression_m_toString}

# gremlin_AffectationExpression class attributes and methods
gremlin_AffectationExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_AffectationExpression.methods={gremlin_AffectationExpression_m_toString}

# gremlin_LeftShiftExpression class attributes and methods
gremlin_LeftShiftExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_LeftShiftExpression.methods={gremlin_LeftShiftExpression_m_toString}

# gremlin_TernaryOperator class attributes and methods
gremlin_TernaryOperator_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_TernaryOperator.methods={gremlin_TernaryOperator_m_toString}

# gremlin_BooleanLiteral class attributes and methods
gremlin_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
gremlin_BooleanLiteral_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_BooleanLiteral.attributes={gremlin_BooleanLiteral_value}
gremlin_BooleanLiteral.methods={gremlin_BooleanLiteral_m_toString}

# gremlin_StringLiteral class attributes and methods
gremlin_StringLiteral_value: Property = Property(name="value", type=StringType)
gremlin_StringLiteral_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_StringLiteral.attributes={gremlin_StringLiteral_value}
gremlin_StringLiteral.methods={gremlin_StringLiteral_m_toString}

# gremlin_IntegerLiteral class attributes and methods
gremlin_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
gremlin_IntegerLiteral_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_IntegerLiteral.attributes={gremlin_IntegerLiteral_value}
gremlin_IntegerLiteral.methods={gremlin_IntegerLiteral_m_toString}

# gremlin_DoubleLiteral class attributes and methods
gremlin_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
gremlin_DoubleLiteral_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_DoubleLiteral.attributes={gremlin_DoubleLiteral_value}
gremlin_DoubleLiteral.methods={gremlin_DoubleLiteral_m_toString}

# gremlin_NullLiteral class attributes and methods
gremlin_NullLiteral_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_NullLiteral.methods={gremlin_NullLiteral_m_toString}

# gremlin_ToIntegerCall class attributes and methods
gremlin_ToIntegerCall_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_ToIntegerCall.methods={gremlin_ToIntegerCall_m_toString}

# gremlin_PlusExpression class attributes and methods
gremlin_PlusExpression_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_PlusExpression.methods={gremlin_PlusExpression_m_toString}

# gremlin_CustomStep class attributes and methods
gremlin_CustomStep_name: Property = Property(name="name", type=StringType)
gremlin_CustomStep_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
gremlin_CustomStep.attributes={gremlin_CustomStep_name}
gremlin_CustomStep.methods={gremlin_CustomStep_m_toString}

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="gremlin_Instruction", type=gremlin_GremlinScript, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_GremlinScript", type=gremlin_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions1: BinaryAssociation = BinaryAssociation(
    name="instructions1",
    ends={
        Property(name="gremlin_Instruction2", type=gremlin_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_MethodDeclaration", type=gremlin_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value3: BinaryAssociation = BinaryAssociation(
    name="value3",
    ends={
        Property(name="gremlin_Instruction4", type=gremlin_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_VariableDeclaration", type=gremlin_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="gremlin_TypeDeclaration", type=gremlin_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_VariableDeclaration6", type=gremlin_TypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nextElement8: BinaryAssociation = BinaryAssociation(
    name="nextElement8",
    ends={
        Property(name="TraversalElement", type=gremlin_TraversalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="previousElement", type=gremlin_TraversalElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
previousElement10: BinaryAssociation = BinaryAssociation(
    name="previousElement10",
    ends={
        Property(name="TraversalElement11", type=gremlin_TraversalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="nextElement", type=gremlin_TraversalElement, multiplicity=Multiplicity(0, 1))
    }
)
values12: BinaryAssociation = BinaryAssociation(
    name="values12",
    ends={
        Property(name="gremlin_Instruction13", type=gremlin_CollectionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_CollectionDefinition", type=gremlin_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="gremlin_TypeDeclaration16", type=gremlin_CollectionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_CollectionDefinition15", type=gremlin_TypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instructions17: BinaryAssociation = BinaryAssociation(
    name="instructions17",
    ends={
        Property(name="gremlin_Instruction18", type=gremlin_Closure, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_Closure", type=gremlin_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cast19: BinaryAssociation = BinaryAssociation(
    name="cast19",
    ends={
        Property(name="gremlin_TypeDeclaration20", type=gremlin_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_VariableAccess", type=gremlin_TypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instruction21: BinaryAssociation = BinaryAssociation(
    name="instruction21",
    ends={
        Property(name="gremlin_Instruction22", type=gremlin_FillStep, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_FillStep", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value23: BinaryAssociation = BinaryAssociation(
    name="value23",
    ends={
        Property(name="gremlin_Instruction24", type=gremlin_PropertyStep, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_PropertyStep", type=gremlin_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
closure25: BinaryAssociation = BinaryAssociation(
    name="closure25",
    ends={
        Property(name="gremlin_Closure26", type=gremlin_FilterStep, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_FilterStep", type=gremlin_Closure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection27: BinaryAssociation = BinaryAssociation(
    name="collection27",
    ends={
        Property(name="gremlin_CollectionDefinition28", type=gremlin_RetainStep, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_RetainStep", type=gremlin_CollectionDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection29: BinaryAssociation = BinaryAssociation(
    name="collection29",
    ends={
        Property(name="gremlin_CollectionDefinition30", type=gremlin_ExceptStep, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_ExceptStep", type=gremlin_CollectionDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
closure31: BinaryAssociation = BinaryAssociation(
    name="closure31",
    ends={
        Property(name="gremlin_Closure32", type=gremlin_TransformStep, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_TransformStep", type=gremlin_Closure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
closure33: BinaryAssociation = BinaryAssociation(
    name="closure33",
    ends={
        Property(name="gremlin_Closure34", type=gremlin_GatherStep, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_GatherStep", type=gremlin_Closure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params35: BinaryAssociation = BinaryAssociation(
    name="params35",
    ends={
        Property(name="gremlin_EObject", type=gremlin_CustomMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_CustomMethodCall", type=gremlin_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftCollection44: BinaryAssociation = BinaryAssociation(
    name="leftCollection44",
    ends={
        Property(name="gremlin_Instruction45", type=gremlin_UnionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_UnionCall", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value36: BinaryAssociation = BinaryAssociation(
    name="value36",
    ends={
        Property(name="gremlin_Instruction37", type=gremlin_ContainsCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_ContainsCall", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value38: BinaryAssociation = BinaryAssociation(
    name="value38",
    ends={
        Property(name="gremlin_Instruction39", type=gremlin_ContainsAllCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_ContainsAllCall", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value40: BinaryAssociation = BinaryAssociation(
    name="value40",
    ends={
        Property(name="gremlin_Instruction41", type=gremlin_AddAllCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_AddAllCall", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value42: BinaryAssociation = BinaryAssociation(
    name="value42",
    ends={
        Property(name="gremlin_Instruction43", type=gremlin_RetainAllCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_RetainAllCall", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightCollection46: BinaryAssociation = BinaryAssociation(
    name="rightCollection46",
    ends={
        Property(name="gremlin_Instruction48", type=gremlin_UnionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_UnionCall47", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cast49: BinaryAssociation = BinaryAssociation(
    name="cast49",
    ends={
        Property(name="gremlin_TypeDeclaration51", type=gremlin_UnionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_UnionCall50", type=gremlin_TypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftCollection52: BinaryAssociation = BinaryAssociation(
    name="leftCollection52",
    ends={
        Property(name="gremlin_Instruction53", type=gremlin_IntersectionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_IntersectionCall", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightCollection54: BinaryAssociation = BinaryAssociation(
    name="rightCollection54",
    ends={
        Property(name="gremlin_Instruction56", type=gremlin_IntersectionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_IntersectionCall55", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cast57: BinaryAssociation = BinaryAssociation(
    name="cast57",
    ends={
        Property(name="gremlin_TypeDeclaration59", type=gremlin_IntersectionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_IntersectionCall58", type=gremlin_TypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp60: BinaryAssociation = BinaryAssociation(
    name="exp60",
    ends={
        Property(name="gremlin_Instruction61", type=gremlin_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_UnaryExpression", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left62: BinaryAssociation = BinaryAssociation(
    name="left62",
    ends={
        Property(name="gremlin_Instruction63", type=gremlin_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_BinaryExpression", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right64: BinaryAssociation = BinaryAssociation(
    name="right64",
    ends={
        Property(name="gremlin_Instruction66", type=gremlin_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_BinaryExpression65", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition67: BinaryAssociation = BinaryAssociation(
    name="condition67",
    ends={
        Property(name="gremlin_Instruction68", type=gremlin_TernaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_TernaryOperator", type=gremlin_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifTrue69: BinaryAssociation = BinaryAssociation(
    name="ifTrue69",
    ends={
        Property(name="gremlin_Instruction71", type=gremlin_TernaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_TernaryOperator70", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifFalse72: BinaryAssociation = BinaryAssociation(
    name="ifFalse72",
    ends={
        Property(name="gremlin_Instruction74", type=gremlin_TernaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_TernaryOperator73", type=gremlin_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
params75: BinaryAssociation = BinaryAssociation(
    name="params75",
    ends={
        Property(name="gremlin_EObject76", type=gremlin_CustomStep, multiplicity=Multiplicity(1, 1)),
        Property(name="gremlin_CustomStep", type=gremlin_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_gremlin_ReturnStatement_Instruction = Generalization(general=Instruction, specific=gremlin_ReturnStatement)
gen_gremlin_MethodDeclaration_Instruction = Generalization(general=Instruction, specific=gremlin_MethodDeclaration)
gen_gremlin_TypeDeclaration_Instruction = Generalization(general=Instruction, specific=gremlin_TypeDeclaration)
gen_gremlin_ListDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=gremlin_ListDeclaration)
gen_gremlin_SetDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=gremlin_SetDeclaration)
gen_gremlin_SortedSetDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=gremlin_SortedSetDeclaration)
gen_gremlin_ClosureIt_VariableAccess = Generalization(general=VariableAccess, specific=gremlin_ClosureIt)
gen_gremlin_VariableDeclaration_Instruction = Generalization(general=Instruction, specific=gremlin_VariableDeclaration)
gen_gremlin_TraversalElement_Instruction = Generalization(general=Instruction, specific=gremlin_TraversalElement)
gen_gremlin_CollectionDefinition_TraversalElement = Generalization(general=TraversalElement, specific=gremlin_CollectionDefinition)
gen_gremlin_Closure_Instruction = Generalization(general=Instruction, specific=gremlin_Closure)
gen_gremlin_VerticesStep_Step = Generalization(general=Step, specific=gremlin_VerticesStep)
gen_gremlin_VariableAccess_TraversalElement = Generalization(general=TraversalElement, specific=gremlin_VariableAccess)
gen_gremlin_Step_TraversalElement = Generalization(general=TraversalElement, specific=gremlin_Step)
gen_gremlin_IdentityStep_Step = Generalization(general=Step, specific=gremlin_IdentityStep)
gen_gremlin_FillStep_Step = Generalization(general=Step, specific=gremlin_FillStep)
gen_gremlin_StartStep_Step = Generalization(general=Step, specific=gremlin_StartStep)
gen_gremlin_RetainStep_Step = Generalization(general=Step, specific=gremlin_RetainStep)
gen_gremlin_EdgesStep_Step = Generalization(general=Step, specific=gremlin_EdgesStep)
gen_gremlin_PropertyStep_Step = Generalization(general=Step, specific=gremlin_PropertyStep)
gen_gremlin_OutEStep_Step = Generalization(general=Step, specific=gremlin_OutEStep)
gen_gremlin_InEStep_Step = Generalization(general=Step, specific=gremlin_InEStep)
gen_gremlin_InVStep_Step = Generalization(general=Step, specific=gremlin_InVStep)
gen_gremlin_OutVStep_Step = Generalization(general=Step, specific=gremlin_OutVStep)
gen_gremlin_FilterStep_Step = Generalization(general=Step, specific=gremlin_FilterStep)
gen_gremlin_ExceptStep_Step = Generalization(general=Step, specific=gremlin_ExceptStep)
gen_gremlin_TransformStep_Step = Generalization(general=Step, specific=gremlin_TransformStep)
gen_gremlin_GatherStep_Step = Generalization(general=Step, specific=gremlin_GatherStep)
gen_gremlin_ScatterStep_Step = Generalization(general=Step, specific=gremlin_ScatterStep)
gen_gremlin_MethodCall_TraversalElement = Generalization(general=TraversalElement, specific=gremlin_MethodCall)
gen_gremlin_CustomMethodCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_CustomMethodCall)
gen_gremlin_ContainsCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_ContainsCall)
gen_gremlin_NextCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_NextCall)
gen_gremlin_HasNextCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_HasNextCall)
gen_gremlin_IndexCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_IndexCall)
gen_gremlin_CountCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_CountCall)
gen_gremlin_FirstCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_FirstCall)
gen_gremlin_ToListCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_ToListCall)
gen_gremlin_IsEmptyCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_IsEmptyCall)
gen_gremlin_ContainsAllCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_ContainsAllCall)
gen_gremlin_AddAllCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_AddAllCall)
gen_gremlin_RetainAllCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_RetainAllCall)
gen_gremlin_UnionCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_UnionCall)
gen_gremlin_EqualityExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_EqualityExpression)
gen_gremlin_IntersectionCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_IntersectionCall)
gen_gremlin_SizeCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_SizeCall)
gen_gremlin_Expression_Instruction = Generalization(general=Instruction, specific=gremlin_Expression)
gen_gremlin_UnaryExpression_Expression = Generalization(general=Expression, specific=gremlin_UnaryExpression)
gen_gremlin_NotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=gremlin_NotExpression)
gen_gremlin_BinaryExpression_Expression = Generalization(general=Expression, specific=gremlin_BinaryExpression)
gen_gremlin_InExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_InExpression)
gen_gremlin_DifferenceExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_DifferenceExpression)
gen_gremlin_OrExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_OrExpression)
gen_gremlin_AndExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_AndExpression)
gen_gremlin_GreaterExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_GreaterExpression)
gen_gremlin_GreaterOrEqualExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_GreaterOrEqualExpression)
gen_gremlin_LessExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_LessExpression)
gen_gremlin_LessOrEqualExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_LessOrEqualExpression)
gen_gremlin_AffectationExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_AffectationExpression)
gen_gremlin_LeftShiftExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_LeftShiftExpression)
gen_gremlin_TernaryOperator_Expression = Generalization(general=Expression, specific=gremlin_TernaryOperator)
gen_gremlin_BooleanLiteral_Expression = Generalization(general=Expression, specific=gremlin_BooleanLiteral)
gen_gremlin_StringLiteral_Expression = Generalization(general=Expression, specific=gremlin_StringLiteral)
gen_gremlin_IntegerLiteral_Expression = Generalization(general=Expression, specific=gremlin_IntegerLiteral)
gen_gremlin_DoubleLiteral_Expression = Generalization(general=Expression, specific=gremlin_DoubleLiteral)
gen_gremlin_NullLiteral_Expression = Generalization(general=Expression, specific=gremlin_NullLiteral)
gen_gremlin_ToIntegerCall_MethodCall = Generalization(general=MethodCall, specific=gremlin_ToIntegerCall)
gen_gremlin_PlusExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=gremlin_PlusExpression)
gen_gremlin_CustomStep_Step = Generalization(general=Step, specific=gremlin_CustomStep)

# Domain Model
domain_model = DomainModel(
    name="gremlin",
    types={gremlin_GremlinScript, gremlin_Instruction, gremlin_ReturnStatement, Instruction, gremlin_MethodDeclaration, gremlin_TypeDeclaration, gremlin_ListDeclaration, TypeDeclaration, gremlin_SetDeclaration, gremlin_SortedSetDeclaration, gremlin_VariableDeclaration, gremlin_TraversalElement, gremlin_CollectionDefinition, TraversalElement, gremlin_Closure, gremlin_ClosureIt, VariableAccess, gremlin_VerticesStep, gremlin_VariableAccess, gremlin_Step, gremlin_IdentityStep, Step, gremlin_FillStep, gremlin_StartStep, gremlin_RetainStep, gremlin_EdgesStep, gremlin_PropertyStep, gremlin_OutEStep, gremlin_InEStep, gremlin_InVStep, gremlin_OutVStep, gremlin_FilterStep, gremlin_ExceptStep, gremlin_TransformStep, gremlin_GatherStep, gremlin_ScatterStep, gremlin_MethodCall, gremlin_CustomMethodCall, MethodCall, gremlin_ContainsCall, gremlin_EObject, gremlin_NextCall, gremlin_HasNextCall, gremlin_IndexCall, gremlin_CountCall, gremlin_FirstCall, gremlin_ToListCall, gremlin_IsEmptyCall, gremlin_ContainsAllCall, gremlin_AddAllCall, gremlin_RetainAllCall, gremlin_UnionCall, gremlin_EqualityExpression, BinaryExpression, gremlin_IntersectionCall, gremlin_SizeCall, gremlin_Expression, gremlin_UnaryExpression, Expression, gremlin_NotExpression, UnaryExpression, gremlin_BinaryExpression, gremlin_InExpression, gremlin_DifferenceExpression, gremlin_OrExpression, gremlin_AndExpression, gremlin_GreaterExpression, gremlin_GreaterOrEqualExpression, gremlin_LessExpression, gremlin_LessOrEqualExpression, gremlin_AffectationExpression, gremlin_LeftShiftExpression, gremlin_TernaryOperator, gremlin_BooleanLiteral, gremlin_StringLiteral, gremlin_IntegerLiteral, gremlin_DoubleLiteral, gremlin_NullLiteral, gremlin_ToIntegerCall, gremlin_PlusExpression, gremlin_CustomStep},
    associations={instructions0, instructions1, value3, type5, nextElement8, previousElement10, values12, type14, instructions17, cast19, instruction21, value23, closure25, collection27, collection29, closure31, closure33, params35, leftCollection44, value36, value38, value40, value42, rightCollection46, cast49, leftCollection52, rightCollection54, cast57, exp60, left62, right64, condition67, ifTrue69, ifFalse72, params75},
    generalizations={gen_gremlin_ReturnStatement_Instruction, gen_gremlin_MethodDeclaration_Instruction, gen_gremlin_TypeDeclaration_Instruction, gen_gremlin_ListDeclaration_TypeDeclaration, gen_gremlin_SetDeclaration_TypeDeclaration, gen_gremlin_SortedSetDeclaration_TypeDeclaration, gen_gremlin_ClosureIt_VariableAccess, gen_gremlin_VariableDeclaration_Instruction, gen_gremlin_TraversalElement_Instruction, gen_gremlin_CollectionDefinition_TraversalElement, gen_gremlin_Closure_Instruction, gen_gremlin_VerticesStep_Step, gen_gremlin_VariableAccess_TraversalElement, gen_gremlin_Step_TraversalElement, gen_gremlin_IdentityStep_Step, gen_gremlin_FillStep_Step, gen_gremlin_StartStep_Step, gen_gremlin_RetainStep_Step, gen_gremlin_EdgesStep_Step, gen_gremlin_PropertyStep_Step, gen_gremlin_OutEStep_Step, gen_gremlin_InEStep_Step, gen_gremlin_InVStep_Step, gen_gremlin_OutVStep_Step, gen_gremlin_FilterStep_Step, gen_gremlin_ExceptStep_Step, gen_gremlin_TransformStep_Step, gen_gremlin_GatherStep_Step, gen_gremlin_ScatterStep_Step, gen_gremlin_MethodCall_TraversalElement, gen_gremlin_CustomMethodCall_MethodCall, gen_gremlin_ContainsCall_MethodCall, gen_gremlin_NextCall_MethodCall, gen_gremlin_HasNextCall_MethodCall, gen_gremlin_IndexCall_MethodCall, gen_gremlin_CountCall_MethodCall, gen_gremlin_FirstCall_MethodCall, gen_gremlin_ToListCall_MethodCall, gen_gremlin_IsEmptyCall_MethodCall, gen_gremlin_ContainsAllCall_MethodCall, gen_gremlin_AddAllCall_MethodCall, gen_gremlin_RetainAllCall_MethodCall, gen_gremlin_UnionCall_MethodCall, gen_gremlin_EqualityExpression_BinaryExpression, gen_gremlin_IntersectionCall_MethodCall, gen_gremlin_SizeCall_MethodCall, gen_gremlin_Expression_Instruction, gen_gremlin_UnaryExpression_Expression, gen_gremlin_NotExpression_UnaryExpression, gen_gremlin_BinaryExpression_Expression, gen_gremlin_InExpression_BinaryExpression, gen_gremlin_DifferenceExpression_BinaryExpression, gen_gremlin_OrExpression_BinaryExpression, gen_gremlin_AndExpression_BinaryExpression, gen_gremlin_GreaterExpression_BinaryExpression, gen_gremlin_GreaterOrEqualExpression_BinaryExpression, gen_gremlin_LessExpression_BinaryExpression, gen_gremlin_LessOrEqualExpression_BinaryExpression, gen_gremlin_AffectationExpression_BinaryExpression, gen_gremlin_LeftShiftExpression_BinaryExpression, gen_gremlin_TernaryOperator_Expression, gen_gremlin_BooleanLiteral_Expression, gen_gremlin_StringLiteral_Expression, gen_gremlin_IntegerLiteral_Expression, gen_gremlin_DoubleLiteral_Expression, gen_gremlin_NullLiteral_Expression, gen_gremlin_ToIntegerCall_MethodCall, gen_gremlin_PlusExpression_BinaryExpression, gen_gremlin_CustomStep_Step},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)