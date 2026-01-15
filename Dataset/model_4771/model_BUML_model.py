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
model_MClass = Class(name="model::MClass")
model_Type = Class(name="model::Type")
model_BasicType = Class(name="model::BasicType")
Type = Class(name="Type")
model_IntegerType = Class(name="model::IntegerType")
BasicType = Class(name="BasicType")
model_MAttribute = Class(name="model::MAttribute")
MModelElementEx = Class(name="MModelElementEx")
model_MPrePostCondition = Class(name="model::MPrePostCondition")
model_MModelElement = Class(name="model::MModelElement")
model_MModelElementEx = Class(name="model::MModelElementEx")
MModelElement = Class(name="MModelElement")
model_MOperation = Class(name="model::MOperation")
model_MAssociation = Class(name="model::MAssociation")
model_MMVisitor = Class(name="model::MMVisitor")
model_MModel = Class(name="model::MModel")
model_MClassInvariant = Class(name="model::MClassInvariant")
model_OclAnyType = Class(name="model::OclAnyType")
model_SequenceType = Class(name="model::SequenceType")
model_BooleanType = Class(name="model::BooleanType")
model_VarDecl = Class(name="model::VarDecl")
model_RealType = Class(name="model::RealType")
model_StringType = Class(name="model::StringType")
model_Comparable = Class(name="model::Comparable", is_abstract=True)
model_CollectionType = Class(name="model::CollectionType")
model_SetType = Class(name="model::SetType")
CollectionType = Class(name="CollectionType")
model_ObjectType = Class(name="model::ObjectType")
model_BagType = Class(name="model::BagType")
model_EnumType = Class(name="model::EnumType")
model_MNavigableElement = Class(name="model::MNavigableElement")
model_MAssociationEnd = Class(name="model::MAssociationEnd")
model_MAggregationKind = Class(name="model::MAggregationKind")
model_MMultiplicity = Class(name="model::MMultiplicity")
model_MRange = Class(name="model::MRange")
model_MAssociationClass = Class(name="model::MAssociationClass")
MClass = Class(name="MClass")
MAssociation = Class(name="MAssociation")
model_VarDeclList = Class(name="model::VarDeclList")
model_Expression = Class(name="model::Expression")
model_OrderedSetType = Class(name="model::OrderedSetType")
model_Part = Class(name="model::Part")
model_TupleType = Class(name="model::TupleType")
model_VoidType = Class(name="model::VoidType")

# model_MClass class attributes and methods
model_MClass_m_getAbstract: Method = Method(name="getAbstract", parameters={}, type=BooleanType)
model_MClass_m_setAbstract: Method = Method(name="setAbstract", parameters={Parameter(name='b')})
model_MClass_m_addAttribute: Method = Method(name="addAttribute", parameters={Parameter(name='attr')})
model_MClass_m_addOperation: Method = Method(name="addOperation", parameters={Parameter(name='op')})
model_MClass_m_addAssociation: Method = Method(name="addAssociation", parameters={Parameter(name='a')})
model_MClass_m_addParent: Method = Method(name="addParent", parameters={Parameter(name='c')})
model_MClass_m_addChild: Method = Method(name="addChild", parameters={Parameter(name='c')})
model_MClass_m_processWithVisitor: Method = Method(name="processWithVisitor", parameters={Parameter(name='v')})
model_MClass.methods={model_MClass_m_addAssociation, model_MClass_m_getAbstract, model_MClass_m_addOperation, model_MClass_m_addParent, model_MClass_m_processWithVisitor, model_MClass_m_addAttribute, model_MClass_m_setAbstract, model_MClass_m_addChild}

# model_Type class attributes and methods
model_Type_typeName: Property = Property(name="typeName", type=StringType)
model_Type_typeId: Property = Property(name="typeId", type=IntegerType)
model_Type.attributes={model_Type_typeId, model_Type_typeName}

# model_BasicType class attributes and methods

# Type class attributes and methods

# model_IntegerType class attributes and methods

# BasicType class attributes and methods

# model_MAttribute class attributes and methods
model_MAttribute_m_processWithVisitor: Method = Method(name="processWithVisitor", parameters={Parameter(name='v')})
model_MAttribute.methods={model_MAttribute_m_processWithVisitor}

# MModelElementEx class attributes and methods

# model_MPrePostCondition class attributes and methods
model_MPrePostCondition_positionInModel: Property = Property(name="positionInModel", type=IntegerType)
model_MPrePostCondition_m_getIsPre: Method = Method(name="getIsPre", parameters={}, type=BooleanType)
model_MPrePostCondition_m_setPre: Method = Method(name="setPre", parameters={Parameter(name='b')})
model_MPrePostCondition.attributes={model_MPrePostCondition_positionInModel}
model_MPrePostCondition.methods={model_MPrePostCondition_m_setPre, model_MPrePostCondition_m_getIsPre}

# model_MModelElement class attributes and methods
model_MModelElement_m_name: Method = Method(name="name", parameters={}, type=StringType)
model_MModelElement_m_processWithVisitor: Method = Method(name="processWithVisitor", parameters={Parameter(name='v')})
model_MModelElement.methods={model_MModelElement_m_name, model_MModelElement_m_processWithVisitor}

# model_MModelElementEx class attributes and methods
model_MModelElementEx_name: Property = Property(name="name", type=StringType)
model_MModelElementEx_m_processWithVisitor: Method = Method(name="processWithVisitor", parameters={Parameter(name='v')})
model_MModelElementEx.attributes={model_MModelElementEx_name}
model_MModelElementEx.methods={model_MModelElementEx_m_processWithVisitor}

# MModelElement class attributes and methods

# model_MOperation class attributes and methods
model_MOperation_m_addVarDecl: Method = Method(name="addVarDecl", parameters={Parameter(name='vd')})
model_MOperation.methods={model_MOperation_m_addVarDecl}

# model_MAssociation class attributes and methods
model_MAssociation_m_addAssociationEnd: Method = Method(name="addAssociationEnd", parameters={Parameter(name='ae')})
model_MAssociation_m_processWithVisitor: Method = Method(name="processWithVisitor", parameters={Parameter(name='v')})
model_MAssociation.methods={model_MAssociation_m_processWithVisitor, model_MAssociation_m_addAssociationEnd}

# model_MMVisitor class attributes and methods

# model_MModel class attributes and methods
model_MModel_m_addClass: Method = Method(name="addClass", parameters={Parameter(name='cls')})
model_MModel_m_addClassInvariant: Method = Method(name="addClassInvariant", parameters={Parameter(name='inv')})
model_MModel_m_addPrePostCondition: Method = Method(name="addPrePostCondition", parameters={Parameter(name='ppc')})
model_MModel_m_processWithVisitor: Method = Method(name="processWithVisitor", parameters={Parameter(name='v')})
model_MModel.methods={model_MModel_m_addPrePostCondition, model_MModel_m_addClass, model_MModel_m_processWithVisitor, model_MModel_m_addClassInvariant}

# model_MClassInvariant class attributes and methods
model_MClassInvariant_positionInModel: Property = Property(name="positionInModel", type=IntegerType)
model_MClassInvariant_name: Property = Property(name="name", type=StringType)
model_MClassInvariant_m_getHasVars: Method = Method(name="getHasVars", parameters={}, type=BooleanType)
model_MClassInvariant_m_getIsExistential: Method = Method(name="getIsExistential", parameters={}, type=BooleanType)
model_MClassInvariant.attributes={model_MClassInvariant_name, model_MClassInvariant_positionInModel}
model_MClassInvariant.methods={model_MClassInvariant_m_getIsExistential, model_MClassInvariant_m_getHasVars}

# model_OclAnyType class attributes and methods

# model_SequenceType class attributes and methods

# model_BooleanType class attributes and methods

# model_VarDecl class attributes and methods
model_VarDecl_var: Property = Property(name="var", type=StringType)
model_VarDecl.attributes={model_VarDecl_var}

# model_RealType class attributes and methods

# model_StringType class attributes and methods

# model_Comparable class attributes and methods

# model_CollectionType class attributes and methods

# model_SetType class attributes and methods

# CollectionType class attributes and methods

# model_ObjectType class attributes and methods

# model_BagType class attributes and methods

# model_EnumType class attributes and methods
model_EnumType_name: Property = Property(name="name", type=StringType)
model_EnumType_literals: Property = Property(name="literals", type=StringType)
model_EnumType_m_addLiteral: Method = Method(name="addLiteral", parameters={Parameter(name='literal')})
model_EnumType.attributes={model_EnumType_literals, model_EnumType_name}
model_EnumType.methods={model_EnumType_m_addLiteral}

# model_MNavigableElement class attributes and methods
model_MNavigableElement_nameAsRolename: Property = Property(name="nameAsRolename", type=StringType)
model_MNavigableElement_m_getType: Method = Method(name="getType", parameters={Parameter(name='src')}, type=Type)
model_MNavigableElement.attributes={model_MNavigableElement_nameAsRolename}
model_MNavigableElement.methods={model_MNavigableElement_m_getType}

# model_MAssociationEnd class attributes and methods
model_MAssociationEnd_mClassName: Property = Property(name="mClassName", type=StringType)
model_MAssociationEnd_m_getOrdered: Method = Method(name="getOrdered", parameters={}, type=BooleanType)
model_MAssociationEnd_m_getNavigation: Method = Method(name="getNavigation", parameters={}, type=BooleanType)
model_MAssociationEnd_m_getExplicitNavigation: Method = Method(name="getExplicitNavigation", parameters={}, type=BooleanType)
model_MAssociationEnd.attributes={model_MAssociationEnd_mClassName}
model_MAssociationEnd.methods={model_MAssociationEnd_m_getOrdered, model_MAssociationEnd_m_getNavigation, model_MAssociationEnd_m_getExplicitNavigation}

# model_MAggregationKind class attributes and methods
model_MAggregationKind_name: Property = Property(name="name", type=StringType)
model_MAggregationKind_kind: Property = Property(name="kind", type=IntegerType)
model_MAggregationKind.attributes={model_MAggregationKind_kind, model_MAggregationKind_name}

# model_MMultiplicity class attributes and methods
model_MMultiplicity_m_addRange: Method = Method(name="addRange", parameters={Parameter(name='r')})
model_MMultiplicity.methods={model_MMultiplicity_m_addRange}

# model_MRange class attributes and methods
model_MRange_lower: Property = Property(name="lower", type=IntegerType)
model_MRange_upper: Property = Property(name="upper", type=IntegerType)
model_MRange.attributes={model_MRange_upper, model_MRange_lower}

# model_MAssociationClass class attributes and methods
model_MAssociationClass_m_processWithVisitor: Method = Method(name="processWithVisitor", parameters={Parameter(name='v')})
model_MAssociationClass.methods={model_MAssociationClass_m_processWithVisitor}

# MClass class attributes and methods

# MAssociation class attributes and methods

# model_VarDeclList class attributes and methods

# model_Expression class attributes and methods

# model_OrderedSetType class attributes and methods

# model_Part class attributes and methods
model_Part_name: Property = Property(name="name", type=StringType)
model_Part.attributes={model_Part_name}

# model_TupleType class attributes and methods
model_TupleType_parts: Property = Property(name="parts", type=StringType)
model_TupleType.attributes={model_TupleType_parts}

# model_VoidType class attributes and methods

# Relationships
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="model_MClass", type=model_MAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MAttribute", type=model_MClass, multiplicity=Multiplicity(0, 1))
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="model_Type", type=model_MAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MAttribute2", type=model_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prePostCondition20: BinaryAssociation = BinaryAssociation(
    name="prePostCondition20",
    ends={
        Property(name="model_MPrePostCondition", type=model_MModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MModel21", type=model_MPrePostCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="model_MAttribute5", type=model_MClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MClass4", type=model_MAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations6: BinaryAssociation = BinaryAssociation(
    name="operations6",
    ends={
        Property(name="model_MOperation", type=model_MClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MClass7", type=model_MOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations8: BinaryAssociation = BinaryAssociation(
    name="associations8",
    ends={
        Property(name="model_MAssociation", type=model_MClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MClass9", type=model_MAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parents11: BinaryAssociation = BinaryAssociation(
    name="parents11",
    ends={
        Property(name="model_MClass12", type=model_MClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MClass10", type=model_MClass, multiplicity=Multiplicity(0, 9999))
    }
)
children14: BinaryAssociation = BinaryAssociation(
    name="children14",
    ends={
        Property(name="model_MClass15", type=model_MClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MClass13", type=model_MClass, multiplicity=Multiplicity(0, 9999))
    }
)
classes16: BinaryAssociation = BinaryAssociation(
    name="classes16",
    ends={
        Property(name="model_MClass17", type=model_MModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MModel", type=model_MClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classInvariant18: BinaryAssociation = BinaryAssociation(
    name="classInvariant18",
    ends={
        Property(name="model_MClassInvariant", type=model_MModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MModel19", type=model_MClassInvariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner22: BinaryAssociation = BinaryAssociation(
    name="owner22",
    ends={
        Property(name="model_MClass24", type=model_MOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MOperation23", type=model_MClass, multiplicity=Multiplicity(0, 1))
    }
)
resultType25: BinaryAssociation = BinaryAssociation(
    name="resultType25",
    ends={
        Property(name="model_Type27", type=model_MOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MOperation26", type=model_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varDecls28: BinaryAssociation = BinaryAssociation(
    name="varDecls28",
    ends={
        Property(name="model_VarDecl", type=model_MOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MOperation29", type=model_VarDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type30: BinaryAssociation = BinaryAssociation(
    name="type30",
    ends={
        Property(name="model_Type32", type=model_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="model_VarDecl31", type=model_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elemType33: BinaryAssociation = BinaryAssociation(
    name="elemType33",
    ends={
        Property(name="model_Type34", type=model_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CollectionType", type=model_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mClass35: BinaryAssociation = BinaryAssociation(
    name="mClass35",
    ends={
        Property(name="model_MClass36", type=model_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ObjectType", type=model_MClass, multiplicity=Multiplicity(0, 1))
    }
)
cls54: BinaryAssociation = BinaryAssociation(
    name="cls54",
    ends={
        Property(name="model_MClass55", type=model_MNavigableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MNavigableElement", type=model_MClass, multiplicity=Multiplicity(0, 1))
    }
)
association56: BinaryAssociation = BinaryAssociation(
    name="association56",
    ends={
        Property(name="model_MAssociation58", type=model_MNavigableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MNavigableElement57", type=model_MAssociation, multiplicity=Multiplicity(0, 1))
    }
)
associationEnds37: BinaryAssociation = BinaryAssociation(
    name="associationEnds37",
    ends={
        Property(name="model_MAssociationEnd", type=model_MAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MAssociation38", type=model_MAssociationEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregationKind39: BinaryAssociation = BinaryAssociation(
    name="aggregationKind39",
    ends={
        Property(name="model_MAggregationKind", type=model_MAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MAssociation40", type=model_MAggregationKind, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
association41: BinaryAssociation = BinaryAssociation(
    name="association41",
    ends={
        Property(name="model_MAssociation43", type=model_MAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MAssociationEnd42", type=model_MAssociation, multiplicity=Multiplicity(0, 1))
    }
)
mClass44: BinaryAssociation = BinaryAssociation(
    name="mClass44",
    ends={
        Property(name="model_MClass46", type=model_MAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MAssociationEnd45", type=model_MClass, multiplicity=Multiplicity(0, 1))
    }
)
mMultiplicity47: BinaryAssociation = BinaryAssociation(
    name="mMultiplicity47",
    ends={
        Property(name="model_MMultiplicity", type=model_MAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MAssociationEnd48", type=model_MMultiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
kind49: BinaryAssociation = BinaryAssociation(
    name="kind49",
    ends={
        Property(name="model_MAggregationKind51", type=model_MAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MAssociationEnd50", type=model_MAggregationKind, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ranges52: BinaryAssociation = BinaryAssociation(
    name="ranges52",
    ends={
        Property(name="model_MRange", type=model_MMultiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MMultiplicity53", type=model_MRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vars59: BinaryAssociation = BinaryAssociation(
    name="vars59",
    ends={
        Property(name="model_VarDeclList", type=model_MClassInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MClassInvariant60", type=model_VarDeclList, multiplicity=Multiplicity(0, 1))
    }
)
cls61: BinaryAssociation = BinaryAssociation(
    name="cls61",
    ends={
        Property(name="model_MClass63", type=model_MClassInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MClassInvariant62", type=model_MClass, multiplicity=Multiplicity(0, 1))
    }
)
body64: BinaryAssociation = BinaryAssociation(
    name="body64",
    ends={
        Property(name="model_Expression", type=model_MClassInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MClassInvariant65", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expanded66: BinaryAssociation = BinaryAssociation(
    name="expanded66",
    ends={
        Property(name="model_Expression68", type=model_MClassInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MClassInvariant67", type=model_Expression, multiplicity=Multiplicity(0, 1))
    }
)
operation69: BinaryAssociation = BinaryAssociation(
    name="operation69",
    ends={
        Property(name="model_MOperation71", type=model_MPrePostCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MPrePostCondition70", type=model_MOperation, multiplicity=Multiplicity(0, 1))
    }
)
expression72: BinaryAssociation = BinaryAssociation(
    name="expression72",
    ends={
        Property(name="model_Expression74", type=model_MPrePostCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MPrePostCondition73", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type75: BinaryAssociation = BinaryAssociation(
    name="type75",
    ends={
        Property(name="model_Type76", type=model_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Part", type=model_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model_MClass_MModelElementEx = Generalization(general=MModelElementEx, specific=model_MClass)
gen_model_BasicType_Type = Generalization(general=Type, specific=model_BasicType)
gen_model_IntegerType_BasicType = Generalization(general=BasicType, specific=model_IntegerType)
gen_model_MAttribute_MModelElementEx = Generalization(general=MModelElementEx, specific=model_MAttribute)
gen_model_MModelElementEx_MModelElement = Generalization(general=MModelElement, specific=model_MModelElementEx)
gen_model_MOperation_MModelElementEx = Generalization(general=MModelElementEx, specific=model_MOperation)
gen_model_MModel_MModelElementEx = Generalization(general=MModelElementEx, specific=model_MModel)
gen_model_OclAnyType_Type = Generalization(general=Type, specific=model_OclAnyType)
gen_model_SequenceType_CollectionType = Generalization(general=CollectionType, specific=model_SequenceType)
gen_model_BooleanType_BasicType = Generalization(general=BasicType, specific=model_BooleanType)
gen_model_MAssociation_MModelElementEx = Generalization(general=MModelElementEx, specific=model_MAssociation)
gen_model_RealType_BasicType = Generalization(general=BasicType, specific=model_RealType)
gen_model_StringType_BasicType = Generalization(general=BasicType, specific=model_StringType)
gen_model_CollectionType_Type = Generalization(general=Type, specific=model_CollectionType)
gen_model_SetType_CollectionType = Generalization(general=CollectionType, specific=model_SetType)
gen_model_ObjectType_Type = Generalization(general=Type, specific=model_ObjectType)
gen_model_BagType_CollectionType = Generalization(general=CollectionType, specific=model_BagType)
gen_model_EnumType_Type = Generalization(general=Type, specific=model_EnumType)
gen_model_MClassInvariant_MModelElement = Generalization(general=MModelElement, specific=model_MClassInvariant)
gen_model_MAssociationEnd_MModelElementEx = Generalization(general=MModelElementEx, specific=model_MAssociationEnd)
gen_model_MAssociationClass_MClass = Generalization(general=MClass, specific=model_MAssociationClass)
gen_model_MAssociationClass_MAssociation = Generalization(general=MAssociation, specific=model_MAssociationClass)
gen_model_MPrePostCondition_MModelElement = Generalization(general=MModelElement, specific=model_MPrePostCondition)
gen_model_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=model_OrderedSetType)
gen_model_TupleType_Type = Generalization(general=Type, specific=model_TupleType)
gen_model_VoidType_Type = Generalization(general=Type, specific=model_VoidType)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_MClass, model_Type, model_BasicType, Type, model_IntegerType, BasicType, model_MAttribute, MModelElementEx, model_MPrePostCondition, model_MModelElement, model_MModelElementEx, MModelElement, model_MOperation, model_MAssociation, model_MMVisitor, model_MModel, model_MClassInvariant, model_OclAnyType, model_SequenceType, model_BooleanType, model_VarDecl, model_RealType, model_StringType, model_Comparable, model_CollectionType, model_SetType, CollectionType, model_ObjectType, model_BagType, model_EnumType, model_MNavigableElement, model_MAssociationEnd, model_MAggregationKind, model_MMultiplicity, model_MRange, model_MAssociationClass, MClass, MAssociation, model_VarDeclList, model_Expression, model_OrderedSetType, model_Part, model_TupleType, model_VoidType},
    associations={owner0, type1, prePostCondition20, attributes3, operations6, associations8, parents11, children14, classes16, classInvariant18, owner22, resultType25, varDecls28, type30, elemType33, mClass35, cls54, association56, associationEnds37, aggregationKind39, association41, mClass44, mMultiplicity47, kind49, ranges52, vars59, cls61, body64, expanded66, operation69, expression72, type75},
    generalizations={gen_model_MClass_MModelElementEx, gen_model_BasicType_Type, gen_model_IntegerType_BasicType, gen_model_MAttribute_MModelElementEx, gen_model_MModelElementEx_MModelElement, gen_model_MOperation_MModelElementEx, gen_model_MModel_MModelElementEx, gen_model_OclAnyType_Type, gen_model_SequenceType_CollectionType, gen_model_BooleanType_BasicType, gen_model_MAssociation_MModelElementEx, gen_model_RealType_BasicType, gen_model_StringType_BasicType, gen_model_CollectionType_Type, gen_model_SetType_CollectionType, gen_model_ObjectType_Type, gen_model_BagType_CollectionType, gen_model_EnumType_Type, gen_model_MClassInvariant_MModelElement, gen_model_MAssociationEnd_MModelElementEx, gen_model_MAssociationClass_MClass, gen_model_MAssociationClass_MAssociation, gen_model_MPrePostCondition_MModelElement, gen_model_OrderedSetType_CollectionType, gen_model_TupleType_Type, gen_model_VoidType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)