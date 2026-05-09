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
ocl_ecore_AnyType = Class(name="ocl_ecore_AnyType")
ocl_ecore_BagType = Class(name="ocl_ecore_BagType")
ocl_ecore_CollectionType = Class(name="ocl_ecore_CollectionType")
ocl_ecore_ElementType = Class(name="ocl_ecore_ElementType")
EClass = Class(name="EClass")
types_ElementType = Class(name="types_ElementType")
ocl_ecore_InvalidType = Class(name="ocl_ecore_InvalidType")
ocl_ecore_MessageType = Class(name="ocl_ecore_MessageType")
ocl_ecore_TemplateParameterType = Class(name="ocl_ecore_TemplateParameterType")
ocl_ecore_TupleType = Class(name="ocl_ecore_TupleType")
ocl_ecore_TypeType = Class(name="ocl_ecore_TypeType")
ocl_ecore_VoidType = Class(name="ocl_ecore_VoidType")
ocl_ecore_CallOperationAction = Class(name="ocl_ecore_CallOperationAction")
ecore_ocl_EOperation = Class(name="ecore_ocl_EOperation")
ocl_ecore_Constraint = Class(name="ocl_ecore_Constraint")
ENamedElement = Class(name="ENamedElement")
ecore_ocl_EModelElement = Class(name="ecore_ocl_EModelElement")
ocl_ecore_SendSignalAction = Class(name="ocl_ecore_SendSignalAction")
ecore_ocl_EClass = Class(name="ecore_ocl_EClass")
ocl_ecore_ExpressionInOCL = Class(name="ocl_ecore_ExpressionInOCL")
ocl_ecore_AssociationClassCallExp = Class(name="ocl_ecore_AssociationClassCallExp")
ocl_ecore_BooleanLiteralExp = Class(name="ocl_ecore_BooleanLiteralExp")
ocl_ecore_CallExp = Class(name="ocl_ecore_CallExp", is_abstract=True)
ocl_ecore_CollectionItem = Class(name="ocl_ecore_CollectionItem")
ocl_ecore_OrderedSetType = Class(name="ocl_ecore_OrderedSetType")
ocl_ecore_PrimitiveType = Class(name="ocl_ecore_PrimitiveType")
ocl_ecore_SequenceType = Class(name="ocl_ecore_SequenceType")
ocl_ecore_SetType = Class(name="ocl_ecore_SetType")
ocl_ecore_FeatureCallExp = Class(name="ocl_ecore_FeatureCallExp", is_abstract=True)
ocl_ecore_IfExp = Class(name="ocl_ecore_IfExp")
ocl_ecore_IntegerLiteralExp = Class(name="ocl_ecore_IntegerLiteralExp")
ocl_ecore_UnlimitedNaturalLiteralExp = Class(name="ocl_ecore_UnlimitedNaturalLiteralExp")
ocl_ecore_InvalidLiteralExp = Class(name="ocl_ecore_InvalidLiteralExp")
ocl_ecore_IterateExp = Class(name="ocl_ecore_IterateExp")
ocl_ecore_IteratorExp = Class(name="ocl_ecore_IteratorExp")
ocl_ecore_LetExp = Class(name="ocl_ecore_LetExp")
ocl_ecore_LiteralExp = Class(name="ocl_ecore_LiteralExp", is_abstract=True)
ocl_ecore_LoopExp = Class(name="ocl_ecore_LoopExp", is_abstract=True)
ocl_ecore_MessageExp = Class(name="ocl_ecore_MessageExp")
ocl_ecore_NavigationCallExp = Class(name="ocl_ecore_NavigationCallExp", is_abstract=True)
ocl_ecore_NullLiteralExp = Class(name="ocl_ecore_NullLiteralExp")
ocl_ecore_NumericLiteralExp = Class(name="ocl_ecore_NumericLiteralExp", is_abstract=True)
ocl_ecore_OCLExpression = Class(name="ocl_ecore_OCLExpression", is_abstract=True)
ocl_ecore_OperationCallExp = Class(name="ocl_ecore_OperationCallExp")
ocl_ecore_CollectionLiteralExp = Class(name="ocl_ecore_CollectionLiteralExp")
ocl_ecore_CollectionLiteralPart = Class(name="ocl_ecore_CollectionLiteralPart", is_abstract=True)
ocl_ecore_CollectionRange = Class(name="ocl_ecore_CollectionRange")
ocl_ecore_EnumLiteralExp = Class(name="ocl_ecore_EnumLiteralExp")
ocl_ecore_TupleLiteralExp = Class(name="ocl_ecore_TupleLiteralExp")
ocl_ecore_TupleLiteralPart = Class(name="ocl_ecore_TupleLiteralPart")
ocl_ecore_TypeExp = Class(name="ocl_ecore_TypeExp")
ocl_ecore_UnspecifiedValueExp = Class(name="ocl_ecore_UnspecifiedValueExp")
ocl_ecore_Variable = Class(name="ocl_ecore_Variable")
ocl_ecore_VariableExp = Class(name="ocl_ecore_VariableExp")
ocl_ecore_OppositePropertyCallExp = Class(name="ocl_ecore_OppositePropertyCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
ecore_ocl_EReference = Class(name="ecore_ocl_EReference")
ocl_ecore_PrimitiveLiteralExp = Class(name="ocl_ecore_PrimitiveLiteralExp", is_abstract=True)
ocl_ecore_PropertyCallExp = Class(name="ocl_ecore_PropertyCallExp")
ocl_ecore_RealLiteralExp = Class(name="ocl_ecore_RealLiteralExp")
ocl_ecore_StateExp = Class(name="ocl_ecore_StateExp")
ocl_ecore_StringLiteralExp = Class(name="ocl_ecore_StringLiteralExp")

# ocl_ecore_AnyType class attributes and methods

# ocl_ecore_BagType class attributes and methods

# ocl_ecore_CollectionType class attributes and methods

# ocl_ecore_ElementType class attributes and methods

# EClass class attributes and methods

# types_ElementType class attributes and methods

# ocl_ecore_InvalidType class attributes and methods

# ocl_ecore_MessageType class attributes and methods

# ocl_ecore_TemplateParameterType class attributes and methods

# ocl_ecore_TupleType class attributes and methods

# ocl_ecore_TypeType class attributes and methods

# ocl_ecore_VoidType class attributes and methods

# ocl_ecore_CallOperationAction class attributes and methods

# ecore_ocl_EOperation class attributes and methods

# ocl_ecore_Constraint class attributes and methods
ocl_ecore_Constraint_stereotype: Property = Property(name="stereotype", type=StringType)
ocl_ecore_Constraint.attributes={ocl_ecore_Constraint_stereotype}

# ENamedElement class attributes and methods

# ecore_ocl_EModelElement class attributes and methods

# ocl_ecore_SendSignalAction class attributes and methods

# ecore_ocl_EClass class attributes and methods

# ocl_ecore_ExpressionInOCL class attributes and methods

# ocl_ecore_AssociationClassCallExp class attributes and methods

# ocl_ecore_BooleanLiteralExp class attributes and methods

# ocl_ecore_CallExp class attributes and methods

# ocl_ecore_CollectionItem class attributes and methods

# ocl_ecore_OrderedSetType class attributes and methods

# ocl_ecore_PrimitiveType class attributes and methods

# ocl_ecore_SequenceType class attributes and methods

# ocl_ecore_SetType class attributes and methods

# ocl_ecore_FeatureCallExp class attributes and methods

# ocl_ecore_IfExp class attributes and methods

# ocl_ecore_IntegerLiteralExp class attributes and methods

# ocl_ecore_UnlimitedNaturalLiteralExp class attributes and methods

# ocl_ecore_InvalidLiteralExp class attributes and methods

# ocl_ecore_IterateExp class attributes and methods

# ocl_ecore_IteratorExp class attributes and methods

# ocl_ecore_LetExp class attributes and methods

# ocl_ecore_LiteralExp class attributes and methods

# ocl_ecore_LoopExp class attributes and methods

# ocl_ecore_MessageExp class attributes and methods

# ocl_ecore_NavigationCallExp class attributes and methods

# ocl_ecore_NullLiteralExp class attributes and methods

# ocl_ecore_NumericLiteralExp class attributes and methods

# ocl_ecore_OCLExpression class attributes and methods

# ocl_ecore_OperationCallExp class attributes and methods

# ocl_ecore_CollectionLiteralExp class attributes and methods

# ocl_ecore_CollectionLiteralPart class attributes and methods

# ocl_ecore_CollectionRange class attributes and methods

# ocl_ecore_EnumLiteralExp class attributes and methods

# ocl_ecore_TupleLiteralExp class attributes and methods

# ocl_ecore_TupleLiteralPart class attributes and methods

# ocl_ecore_TypeExp class attributes and methods

# ocl_ecore_UnspecifiedValueExp class attributes and methods

# ocl_ecore_Variable class attributes and methods

# ocl_ecore_VariableExp class attributes and methods

# ocl_ecore_OppositePropertyCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# ecore_ocl_EReference class attributes and methods

# ocl_ecore_PrimitiveLiteralExp class attributes and methods

# ocl_ecore_PropertyCallExp class attributes and methods

# ocl_ecore_RealLiteralExp class attributes and methods

# ocl_ecore_StateExp class attributes and methods

# ocl_ecore_StringLiteralExp class attributes and methods

# Relationships
operation0: BinaryAssociation = BinaryAssociation(
    name="operation0",
    ends={
        Property(name="ecore_ocl_EOperation", type=ocl_ecore_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_ecore_CallOperationAction", type=ecore_ocl_EOperation, multiplicity=Multiplicity(1, 1))
    }
)
constrainedElements1: BinaryAssociation = BinaryAssociation(
    name="constrainedElements1",
    ends={
        Property(name="ecore_ocl_EModelElement", type=ocl_ecore_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_ecore_Constraint", type=ecore_ocl_EModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
signal2: BinaryAssociation = BinaryAssociation(
    name="signal2",
    ends={
        Property(name="ecore_ocl_EClass", type=ocl_ecore_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_ecore_SendSignalAction", type=ecore_ocl_EClass, multiplicity=Multiplicity(1, 1))
    }
)
referredOppositeProperty3: BinaryAssociation = BinaryAssociation(
    name="referredOppositeProperty3",
    ends={
        Property(name="ecore_ocl_EReference", type=ocl_ecore_OppositePropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_ecore_OppositePropertyCallExp", type=ecore_ocl_EReference, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ocl_ecore_ElementType_EClass = Generalization(general=EClass, specific=ocl_ecore_ElementType)
gen_ocl_ecore_ElementType_types_ElementType = Generalization(general=types_ElementType, specific=ocl_ecore_ElementType)
gen_ocl_ecore_Constraint_ENamedElement = Generalization(general=ENamedElement, specific=ocl_ecore_Constraint)
gen_ocl_ecore_OppositePropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=ocl_ecore_OppositePropertyCallExp)

# Domain Model
domain_model = DomainModel(
    name="ocl",
    types={ocl_ecore_AnyType, ocl_ecore_BagType, ocl_ecore_CollectionType, ocl_ecore_ElementType, EClass, types_ElementType, ocl_ecore_InvalidType, ocl_ecore_MessageType, ocl_ecore_TemplateParameterType, ocl_ecore_TupleType, ocl_ecore_TypeType, ocl_ecore_VoidType, ocl_ecore_CallOperationAction, ecore_ocl_EOperation, ocl_ecore_Constraint, ENamedElement, ecore_ocl_EModelElement, ocl_ecore_SendSignalAction, ecore_ocl_EClass, ocl_ecore_ExpressionInOCL, ocl_ecore_AssociationClassCallExp, ocl_ecore_BooleanLiteralExp, ocl_ecore_CallExp, ocl_ecore_CollectionItem, ocl_ecore_OrderedSetType, ocl_ecore_PrimitiveType, ocl_ecore_SequenceType, ocl_ecore_SetType, ocl_ecore_FeatureCallExp, ocl_ecore_IfExp, ocl_ecore_IntegerLiteralExp, ocl_ecore_UnlimitedNaturalLiteralExp, ocl_ecore_InvalidLiteralExp, ocl_ecore_IterateExp, ocl_ecore_IteratorExp, ocl_ecore_LetExp, ocl_ecore_LiteralExp, ocl_ecore_LoopExp, ocl_ecore_MessageExp, ocl_ecore_NavigationCallExp, ocl_ecore_NullLiteralExp, ocl_ecore_NumericLiteralExp, ocl_ecore_OCLExpression, ocl_ecore_OperationCallExp, ocl_ecore_CollectionLiteralExp, ocl_ecore_CollectionLiteralPart, ocl_ecore_CollectionRange, ocl_ecore_EnumLiteralExp, ocl_ecore_TupleLiteralExp, ocl_ecore_TupleLiteralPart, ocl_ecore_TypeExp, ocl_ecore_UnspecifiedValueExp, ocl_ecore_Variable, ocl_ecore_VariableExp, ocl_ecore_OppositePropertyCallExp, NavigationCallExp, ecore_ocl_EReference, ocl_ecore_PrimitiveLiteralExp, ocl_ecore_PropertyCallExp, ocl_ecore_RealLiteralExp, ocl_ecore_StateExp, ocl_ecore_StringLiteralExp},
    associations={operation0, constrainedElements1, signal2, referredOppositeProperty3},
    generalizations={gen_ocl_ecore_ElementType_EClass, gen_ocl_ecore_ElementType_types_ElementType, gen_ocl_ecore_Constraint_ENamedElement, gen_ocl_ecore_OppositePropertyCallExp_NavigationCallExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)