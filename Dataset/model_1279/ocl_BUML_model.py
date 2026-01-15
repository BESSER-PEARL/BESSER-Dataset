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
EMultiplicity: Enumeration = Enumeration(
    name="EMultiplicity",
    literals={
            EnumerationLiteral(name="one"),
			EnumerationLiteral(name="many")
    }
)

EIteratorKind: Enumeration = Enumeration(
    name="EIteratorKind",
    literals={
            EnumerationLiteral(name="forAll"),
			EnumerationLiteral(name="exists"),
			EnumerationLiteral(name="collect"),
			EnumerationLiteral(name="select")
    }
)

EOperator: Enumeration = Enumeration(
    name="EOperator",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="allInstances"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="less"),
			EnumerationLiteral(name="notEqual"),
			EnumerationLiteral(name="greaterOrEqual"),
			EnumerationLiteral(name="lessOrEqual"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="size"),
			EnumerationLiteral(name="isEmpty"),
			EnumerationLiteral(name="oclIsUndefined"),
			EnumerationLiteral(name="flatten"),
			EnumerationLiteral(name="notEmpty"),
			EnumerationLiteral(name="isUnique")
    }
)

# Classes
EAssociationEnd = Class(name="EAssociationEnd")
EAttribute = Class(name="EAttribute")
ocl_dm_EAssociationEnd = Class(name="ocl::dm::EAssociationEnd")
EEntity = Class(name="EEntity")
ocl_dm_EEntity = Class(name="ocl::dm::EEntity")
EClassifier = Class(name="EClassifier")
ocl_exp_EVariableExp = Class(name="ocl::exp::EVariableExp")
EOclExpression = Class(name="EOclExpression")
EVariable = Class(name="EVariable")
ocl_exp_ETypeExp = Class(name="ocl::exp::ETypeExp")
ocl_exp_ELoopExp = Class(name="ocl::exp::ELoopExp", is_abstract=True)
ECallExp = Class(name="ECallExp")
ocl_dm_EDataModel = Class(name="ocl::dm::EDataModel")
ocl_dm_EAttribute = Class(name="ocl::dm::EAttribute")
EOperationCallExp = Class(name="EOperationCallExp")
ocl_exp_ECallExp = Class(name="ocl::exp::ECallExp", is_abstract=True)
ocl_exp_EFeatureCallExp = Class(name="ocl::exp::EFeatureCallExp", is_abstract=True)
ocl_exp_EAssociationClassCallExp = Class(name="ocl::exp::EAssociationClassCallExp")
ENavigationCallExp = Class(name="ENavigationCallExp")
ocl_exp_ENumericLiteralExp = Class(name="ocl::exp::ENumericLiteralExp", is_abstract=True)
EPrimitiveType = Class(name="EPrimitiveType")
ocl_exp_ELiteralExp = Class(name="ocl::exp::ELiteralExp", is_abstract=True)
ocl_exp_EVariable = Class(name="ocl::exp::EVariable")
ELoopExp = Class(name="ELoopExp")
ocl_exp_EPropertyCallExp = Class(name="ocl::exp::EPropertyCallExp")
ocl_exp_EIteratorExp = Class(name="ocl::exp::EIteratorExp")
ocl_exp_EOclExpression = Class(name="ocl::exp::EOclExpression", is_abstract=True)
ESignal = Class(name="ESignal")
ocl_type_ECollectionType = Class(name="ocl::type::ECollectionType")
EDataType = Class(name="EDataType")
ocl_type_EPrimitiveType = Class(name="ocl::type::EPrimitiveType")
ocl_type_ETupleType = Class(name="ocl::type::ETupleType")
ocl_type_EOrderedSetType = Class(name="ocl::type::EOrderedSetType")
ECollectionType = Class(name="ECollectionType")
ocl_exp_EIntegerLiteralExp = Class(name="ocl::exp::EIntegerLiteralExp")
ENumericLiteralExp = Class(name="ENumericLiteralExp")
ocl_exp_EPrimitiveType = Class(name="ocl::exp::EPrimitiveType", is_abstract=True)
ELiteralExp = Class(name="ELiteralExp")
ocl_exp_ENavigationCallExp = Class(name="ocl::exp::ENavigationCallExp", is_abstract=True)
EFeatureCallExp = Class(name="EFeatureCallExp")
ocl_exp_EOperationCallExp = Class(name="ocl::exp::EOperationCallExp")
ocl_exp_EStringLiteralExp = Class(name="ocl::exp::EStringLiteralExp")
ocl_exp_EBooleanLiteralExp = Class(name="ocl::exp::EBooleanLiteralExp")
ocl_type_EClassifier = Class(name="ocl::type::EClassifier", is_abstract=True)
ocl_type_EDataType = Class(name="ocl::type::EDataType", is_abstract=True)
ocl_type_EInvalidType = Class(name="ocl::type::EInvalidType")
ocl_type_EVoidType = Class(name="ocl::type::EVoidType")
ocl_type_EAnyType = Class(name="ocl::type::EAnyType")
ocl_type_EMessageType = Class(name="ocl::type::EMessageType")
ocl_type_ESequenceType = Class(name="ocl::type::ESequenceType")
ocl_type_EBagType = Class(name="ocl::type::EBagType")
ocl_type_ESetType = Class(name="ocl::type::ESetType")
ocl_type_ESignal = Class(name="ocl::type::ESignal")

# EAssociationEnd class attributes and methods

# EAttribute class attributes and methods

# ocl_dm_EAssociationEnd class attributes and methods
ocl_dm_EAssociationEnd_name: Property = Property(name="name", type=StringType)
ocl_dm_EAssociationEnd_mult: Property = Property(name="mult", type=StringType)
ocl_dm_EAssociationEnd.attributes={ocl_dm_EAssociationEnd_name, ocl_dm_EAssociationEnd_mult}

# EEntity class attributes and methods

# ocl_dm_EEntity class attributes and methods
ocl_dm_EEntity_name: Property = Property(name="name", type=StringType)
ocl_dm_EEntity.attributes={ocl_dm_EEntity_name}

# EClassifier class attributes and methods

# ocl_exp_EVariableExp class attributes and methods

# EOclExpression class attributes and methods

# EVariable class attributes and methods

# ocl_exp_ETypeExp class attributes and methods

# ocl_exp_ELoopExp class attributes and methods

# ECallExp class attributes and methods

# ocl_dm_EDataModel class attributes and methods

# ocl_dm_EAttribute class attributes and methods
ocl_dm_EAttribute_name: Property = Property(name="name", type=StringType)
ocl_dm_EAttribute_type: Property = Property(name="type", type=StringType)
ocl_dm_EAttribute.attributes={ocl_dm_EAttribute_type, ocl_dm_EAttribute_name}

# EOperationCallExp class attributes and methods

# ocl_exp_ECallExp class attributes and methods

# ocl_exp_EFeatureCallExp class attributes and methods

# ocl_exp_EAssociationClassCallExp class attributes and methods

# ENavigationCallExp class attributes and methods

# ocl_exp_ENumericLiteralExp class attributes and methods

# EPrimitiveType class attributes and methods

# ocl_exp_ELiteralExp class attributes and methods

# ocl_exp_EVariable class attributes and methods
ocl_exp_EVariable_name: Property = Property(name="name", type=StringType)
ocl_exp_EVariable.attributes={ocl_exp_EVariable_name}

# ELoopExp class attributes and methods

# ocl_exp_EPropertyCallExp class attributes and methods

# ocl_exp_EIteratorExp class attributes and methods
ocl_exp_EIteratorExp_kind: Property = Property(name="kind", type=StringType)
ocl_exp_EIteratorExp.attributes={ocl_exp_EIteratorExp_kind}

# ocl_exp_EOclExpression class attributes and methods

# ESignal class attributes and methods

# ocl_type_ECollectionType class attributes and methods

# EDataType class attributes and methods

# ocl_type_EPrimitiveType class attributes and methods

# ocl_type_ETupleType class attributes and methods

# ocl_type_EOrderedSetType class attributes and methods

# ECollectionType class attributes and methods

# ocl_exp_EIntegerLiteralExp class attributes and methods
ocl_exp_EIntegerLiteralExp_integerValue: Property = Property(name="integerValue", type=StringType)
ocl_exp_EIntegerLiteralExp.attributes={ocl_exp_EIntegerLiteralExp_integerValue}

# ENumericLiteralExp class attributes and methods

# ocl_exp_EPrimitiveType class attributes and methods

# ELiteralExp class attributes and methods

# ocl_exp_ENavigationCallExp class attributes and methods

# EFeatureCallExp class attributes and methods

# ocl_exp_EOperationCallExp class attributes and methods
ocl_exp_EOperationCallExp_referredOperation: Property = Property(name="referredOperation", type=StringType)
ocl_exp_EOperationCallExp.attributes={ocl_exp_EOperationCallExp_referredOperation}

# ocl_exp_EStringLiteralExp class attributes and methods
ocl_exp_EStringLiteralExp_stringValue: Property = Property(name="stringValue", type=StringType)
ocl_exp_EStringLiteralExp.attributes={ocl_exp_EStringLiteralExp_stringValue}

# ocl_exp_EBooleanLiteralExp class attributes and methods
ocl_exp_EBooleanLiteralExp_booleanValue: Property = Property(name="booleanValue", type=StringType)
ocl_exp_EBooleanLiteralExp.attributes={ocl_exp_EBooleanLiteralExp_booleanValue}

# ocl_type_EClassifier class attributes and methods

# ocl_type_EDataType class attributes and methods

# ocl_type_EInvalidType class attributes and methods

# ocl_type_EVoidType class attributes and methods

# ocl_type_EAnyType class attributes and methods

# ocl_type_EMessageType class attributes and methods
ocl_type_EMessageType_referredOperation: Property = Property(name="referredOperation", type=StringType)
ocl_type_EMessageType.attributes={ocl_type_EMessageType_referredOperation}

# ocl_type_ESequenceType class attributes and methods

# ocl_type_EBagType class attributes and methods

# ocl_type_ESetType class attributes and methods

# ocl_type_ESignal class attributes and methods

# Relationships
ends0: BinaryAssociation = BinaryAssociation(
    name="ends0",
    ends={
        Property(name="EAssociationEnd", type=ocl_dm_EEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_dm_EEntity", type=EAssociationEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="EAttribute", type=ocl_dm_EEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_dm_EEntity2", type=EAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="EEntity", type=ocl_dm_EAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_dm_EAssociationEnd", type=EEntity, multiplicity=Multiplicity(1, 1))
    }
)
referredVariable9: BinaryAssociation = BinaryAssociation(
    name="referredVariable9",
    ends={
        Property(name="EVariable", type=ocl_exp_EVariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_exp_EVariableExp", type=EVariable, multiplicity=Multiplicity(0, 1))
    }
)
referredType10: BinaryAssociation = BinaryAssociation(
    name="referredType10",
    ends={
        Property(name="EClassifier", type=ocl_exp_ETypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_exp_ETypeExp", type=EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
body11: BinaryAssociation = BinaryAssociation(
    name="body11",
    ends={
        Property(name="exp", type=ocl_exp_ELoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EOclExpression", type=EOclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
opp4: BinaryAssociation = BinaryAssociation(
    name="opp4",
    ends={
        Property(name="EAssociationEnd6", type=ocl_dm_EAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_dm_EAssociationEnd5", type=EAssociationEnd, multiplicity=Multiplicity(1, 1))
    }
)
classes7: BinaryAssociation = BinaryAssociation(
    name="classes7",
    ends={
        Property(name="EEntity8", type=ocl_dm_EDataModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_dm_EDataModel", type=EEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializedElement29: BinaryAssociation = BinaryAssociation(
    name="initializedElement29",
    ends={
        Property(name="exp31", type=ocl_exp_EOclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="EVariable30", type=EVariable, multiplicity=Multiplicity(0, 1))
    }
)
parentCall32: BinaryAssociation = BinaryAssociation(
    name="parentCall32",
    ends={
        Property(name="exp33", type=ocl_exp_EOclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="EOperationCallExp", type=EOperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
parentNav34: BinaryAssociation = BinaryAssociation(
    name="parentNav34",
    ends={
        Property(name="exp35", type=ocl_exp_EOclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ENavigationCallExp", type=ENavigationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
source36: BinaryAssociation = BinaryAssociation(
    name="source36",
    ends={
        Property(name="exp38", type=ocl_exp_ECallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EOclExpression37", type=EOclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterator12: BinaryAssociation = BinaryAssociation(
    name="iterator12",
    ends={
        Property(name="exp14", type=ocl_exp_ELoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EVariable13", type=EVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredAssociationEnds15: BinaryAssociation = BinaryAssociation(
    name="referredAssociationEnds15",
    ends={
        Property(name="EAssociationEnd16", type=ocl_exp_EAssociationClassCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_exp_EAssociationClassCallExp", type=EAssociationEnd, multiplicity=Multiplicity(1, 1))
    }
)
loopExp17: BinaryAssociation = BinaryAssociation(
    name="loopExp17",
    ends={
        Property(name="exp18", type=ocl_exp_EVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ELoopExp", type=ELoopExp, multiplicity=Multiplicity(0, 1))
    }
)
initExpression19: BinaryAssociation = BinaryAssociation(
    name="initExpression19",
    ends={
        Property(name="exp21", type=ocl_exp_EVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="EOclExpression20", type=EOclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredProperty22: BinaryAssociation = BinaryAssociation(
    name="referredProperty22",
    ends={
        Property(name="EAttribute23", type=ocl_exp_EPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_exp_EPropertyCallExp", type=EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
loopBodyOwner24: BinaryAssociation = BinaryAssociation(
    name="loopBodyOwner24",
    ends={
        Property(name="exp26", type=ocl_exp_EOclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ELoopExp25", type=ELoopExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedElement27: BinaryAssociation = BinaryAssociation(
    name="appliedElement27",
    ends={
        Property(name="exp28", type=ocl_exp_EOclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ECallExp", type=ECallExp, multiplicity=Multiplicity(0, 1))
    }
)
referredSignal45: BinaryAssociation = BinaryAssociation(
    name="referredSignal45",
    ends={
        Property(name="ESignal", type=ocl_type_EMessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_type_EMessageType", type=ESignal, multiplicity=Multiplicity(0, 1))
    }
)
elementType46: BinaryAssociation = BinaryAssociation(
    name="elementType46",
    ends={
        Property(name="EClassifier47", type=ocl_type_ECollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_type_ECollectionType", type=EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
qualifier39: BinaryAssociation = BinaryAssociation(
    name="qualifier39",
    ends={
        Property(name="exp41", type=ocl_exp_ENavigationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EOclExpression40", type=EOclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument42: BinaryAssociation = BinaryAssociation(
    name="argument42",
    ends={
        Property(name="exp44", type=ocl_exp_EOperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EOclExpression43", type=EOclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ocl_dm_EEntity_EClassifier = Generalization(general=EClassifier, specific=ocl_dm_EEntity)
gen_ocl_exp_EVariableExp_EOclExpression = Generalization(general=EOclExpression, specific=ocl_exp_EVariableExp)
gen_ocl_exp_ETypeExp_EOclExpression = Generalization(general=EOclExpression, specific=ocl_exp_ETypeExp)
gen_ocl_exp_ELoopExp_ECallExp = Generalization(general=ECallExp, specific=ocl_exp_ELoopExp)
gen_ocl_exp_ECallExp_EOclExpression = Generalization(general=EOclExpression, specific=ocl_exp_ECallExp)
gen_ocl_exp_EFeatureCallExp_ECallExp = Generalization(general=ECallExp, specific=ocl_exp_EFeatureCallExp)
gen_ocl_exp_EAssociationClassCallExp_ENavigationCallExp = Generalization(general=ENavigationCallExp, specific=ocl_exp_EAssociationClassCallExp)
gen_ocl_exp_ENumericLiteralExp_EPrimitiveType = Generalization(general=EPrimitiveType, specific=ocl_exp_ENumericLiteralExp)
gen_ocl_exp_ELiteralExp_EOclExpression = Generalization(general=EOclExpression, specific=ocl_exp_ELiteralExp)
gen_ocl_exp_EPropertyCallExp_ENavigationCallExp = Generalization(general=ENavigationCallExp, specific=ocl_exp_EPropertyCallExp)
gen_ocl_exp_EIteratorExp_ELoopExp = Generalization(general=ELoopExp, specific=ocl_exp_EIteratorExp)
gen_ocl_type_ECollectionType_EDataType = Generalization(general=EDataType, specific=ocl_type_ECollectionType)
gen_ocl_type_EPrimitiveType_EDataType = Generalization(general=EDataType, specific=ocl_type_EPrimitiveType)
gen_ocl_type_ETupleType_EDataType = Generalization(general=EDataType, specific=ocl_type_ETupleType)
gen_ocl_type_EOrderedSetType_ECollectionType = Generalization(general=ECollectionType, specific=ocl_type_EOrderedSetType)
gen_ocl_exp_EIntegerLiteralExp_ENumericLiteralExp = Generalization(general=ENumericLiteralExp, specific=ocl_exp_EIntegerLiteralExp)
gen_ocl_exp_EPrimitiveType_ELiteralExp = Generalization(general=ELiteralExp, specific=ocl_exp_EPrimitiveType)
gen_ocl_exp_ENavigationCallExp_EFeatureCallExp = Generalization(general=EFeatureCallExp, specific=ocl_exp_ENavigationCallExp)
gen_ocl_exp_EOperationCallExp_EFeatureCallExp = Generalization(general=EFeatureCallExp, specific=ocl_exp_EOperationCallExp)
gen_ocl_exp_EStringLiteralExp_EPrimitiveType = Generalization(general=EPrimitiveType, specific=ocl_exp_EStringLiteralExp)
gen_ocl_exp_EBooleanLiteralExp_EPrimitiveType = Generalization(general=EPrimitiveType, specific=ocl_exp_EBooleanLiteralExp)
gen_ocl_type_EDataType_EClassifier = Generalization(general=EClassifier, specific=ocl_type_EDataType)
gen_ocl_type_EInvalidType_EClassifier = Generalization(general=EClassifier, specific=ocl_type_EInvalidType)
gen_ocl_type_EVoidType_EClassifier = Generalization(general=EClassifier, specific=ocl_type_EVoidType)
gen_ocl_type_EAnyType_EClassifier = Generalization(general=EClassifier, specific=ocl_type_EAnyType)
gen_ocl_type_EMessageType_EClassifier = Generalization(general=EClassifier, specific=ocl_type_EMessageType)
gen_ocl_type_ESequenceType_ECollectionType = Generalization(general=ECollectionType, specific=ocl_type_ESequenceType)
gen_ocl_type_EBagType_ECollectionType = Generalization(general=ECollectionType, specific=ocl_type_EBagType)
gen_ocl_type_ESetType_ECollectionType = Generalization(general=ECollectionType, specific=ocl_type_ESetType)

# Domain Model
domain_model = DomainModel(
    name="ocl",
    types={EAssociationEnd, EAttribute, ocl_dm_EAssociationEnd, EEntity, ocl_dm_EEntity, EClassifier, ocl_exp_EVariableExp, EOclExpression, EVariable, ocl_exp_ETypeExp, ocl_exp_ELoopExp, ECallExp, ocl_dm_EDataModel, ocl_dm_EAttribute, EOperationCallExp, ocl_exp_ECallExp, ocl_exp_EFeatureCallExp, ocl_exp_EAssociationClassCallExp, ENavigationCallExp, ocl_exp_ENumericLiteralExp, EPrimitiveType, ocl_exp_ELiteralExp, ocl_exp_EVariable, ELoopExp, ocl_exp_EPropertyCallExp, ocl_exp_EIteratorExp, ocl_exp_EOclExpression, ESignal, ocl_type_ECollectionType, EDataType, ocl_type_EPrimitiveType, ocl_type_ETupleType, ocl_type_EOrderedSetType, ECollectionType, ocl_exp_EIntegerLiteralExp, ENumericLiteralExp, ocl_exp_EPrimitiveType, ELiteralExp, ocl_exp_ENavigationCallExp, EFeatureCallExp, ocl_exp_EOperationCallExp, ocl_exp_EStringLiteralExp, ocl_exp_EBooleanLiteralExp, ocl_type_EClassifier, ocl_type_EDataType, ocl_type_EInvalidType, ocl_type_EVoidType, ocl_type_EAnyType, ocl_type_EMessageType, ocl_type_ESequenceType, ocl_type_EBagType, ocl_type_ESetType, ocl_type_ESignal, EMultiplicity, EIteratorKind, EOperator},
    associations={ends0, attributes1, target3, referredVariable9, referredType10, body11, opp4, classes7, initializedElement29, parentCall32, parentNav34, source36, iterator12, referredAssociationEnds15, loopExp17, initExpression19, referredProperty22, loopBodyOwner24, appliedElement27, referredSignal45, elementType46, qualifier39, argument42},
    generalizations={gen_ocl_dm_EEntity_EClassifier, gen_ocl_exp_EVariableExp_EOclExpression, gen_ocl_exp_ETypeExp_EOclExpression, gen_ocl_exp_ELoopExp_ECallExp, gen_ocl_exp_ECallExp_EOclExpression, gen_ocl_exp_EFeatureCallExp_ECallExp, gen_ocl_exp_EAssociationClassCallExp_ENavigationCallExp, gen_ocl_exp_ENumericLiteralExp_EPrimitiveType, gen_ocl_exp_ELiteralExp_EOclExpression, gen_ocl_exp_EPropertyCallExp_ENavigationCallExp, gen_ocl_exp_EIteratorExp_ELoopExp, gen_ocl_type_ECollectionType_EDataType, gen_ocl_type_EPrimitiveType_EDataType, gen_ocl_type_ETupleType_EDataType, gen_ocl_type_EOrderedSetType_ECollectionType, gen_ocl_exp_EIntegerLiteralExp_ENumericLiteralExp, gen_ocl_exp_EPrimitiveType_ELiteralExp, gen_ocl_exp_ENavigationCallExp_EFeatureCallExp, gen_ocl_exp_EOperationCallExp_EFeatureCallExp, gen_ocl_exp_EStringLiteralExp_EPrimitiveType, gen_ocl_exp_EBooleanLiteralExp_EPrimitiveType, gen_ocl_type_EDataType_EClassifier, gen_ocl_type_EInvalidType_EClassifier, gen_ocl_type_EVoidType_EClassifier, gen_ocl_type_EAnyType_EClassifier, gen_ocl_type_EMessageType_EClassifier, gen_ocl_type_ESequenceType_ECollectionType, gen_ocl_type_EBagType_ECollectionType, gen_ocl_type_ESetType_ECollectionType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)