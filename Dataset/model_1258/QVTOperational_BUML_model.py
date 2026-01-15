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
DirectionKind: Enumeration = Enumeration(
    name="DirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out")
    }
)

ImportKind: Enumeration = Enumeration(
    name="ImportKind",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="access")
    }
)

# Classes
qvtoperational_Constructor = Class(name="qvtoperational::Constructor")
ImperativeOperation = Class(name="ImperativeOperation")
qvtoperational_ConstructorBody = Class(name="qvtoperational::ConstructorBody")
OperationBody = Class(name="OperationBody")
qvtoperational_ContextualProperty = Class(name="qvtoperational::ContextualProperty")
Property_ = Class(name="Property")
qvtoperational_Class = Class(name="qvtoperational::Class")
qvtoperational_OCLExpression = Class(name="qvtoperational::OCLExpression")
qvtoperational_Property = Class(name="qvtoperational::Property")
qvtoperational_DummyRelation = Class(name="qvtoperational::DummyRelation")
Element = Class(name="Element")
VarParameter = Class(name="VarParameter")
qvtoperational_Library = Class(name="qvtoperational::Library")
Module = Class(name="Module")
qvtoperational_MappingBody = Class(name="qvtoperational::MappingBody")
qvtoperational_DummyRelationDomain = Class(name="qvtoperational::DummyRelationDomain")
qvtoperational_DummyRelationalTransformation = Class(name="qvtoperational::DummyRelationalTransformation")
qvtoperational_EntryOperation = Class(name="qvtoperational::EntryOperation")
qvtoperational_Helper = Class(name="qvtoperational::Helper")
qvtoperational_ImperativeCallExp = Class(name="qvtoperational::ImperativeCallExp")
OperationCallExp = Class(name="OperationCallExp")
ImperativeExpression = Class(name="ImperativeExpression")
qvtoperational_ImperativeOperation = Class(name="qvtoperational::ImperativeOperation")
Operation = Class(name="Operation")
DummyRelation = Class(name="DummyRelation")
qvtoperational_MappingParameter = Class(name="qvtoperational::MappingParameter")
ModelParameter = Class(name="ModelParameter")
DummyRelationDomain = Class(name="DummyRelationDomain")
qvtoperational_ModelParameter = Class(name="qvtoperational::ModelParameter")
qvtoperational_ModelType = Class(name="qvtoperational::ModelType")
Class_ = Class(name="Class")
qvtoperational_MappingCallExp = Class(name="qvtoperational::MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
qvtoperational_MappingOperation = Class(name="qvtoperational::MappingOperation")
MappingOperation = Class(name="MappingOperation")
EntryOperation = Class(name="EntryOperation")
ModuleImport = Class(name="ModuleImport")
qvtoperational_TemplateableElement = Class(name="qvtoperational::TemplateableElement")
qvtoperational_Variable = Class(name="qvtoperational::Variable")
ModelType = Class(name="ModelType")
qvtoperational_ModuleImport = Class(name="qvtoperational::ModuleImport")
qvtoperational_ObjectExp = Class(name="qvtoperational::ObjectExp")
qvtoperational_Package = Class(name="qvtoperational::Package")
qvtoperational_Module = Class(name="qvtoperational::Module")
qvtoperational_OperationalTransformation = Class(name="qvtoperational::OperationalTransformation")
Dummy2 = Class(name="Dummy2")
InstantiationExp = Class(name="InstantiationExp")
ConstructorBody = Class(name="ConstructorBody")
qvtoperational_OperationBody = Class(name="qvtoperational::OperationBody")
qvtoperational_ResolveInExp = Class(name="qvtoperational::ResolveInExp")
ResolveExp = Class(name="ResolveExp")
qvtoperational_VarParameter = Class(name="qvtoperational::VarParameter")
Variable = Class(name="Variable")
Parameter_ = Class(name="Parameter")
qvtoperational_Tag = Class(name="qvtoperational::Tag")
qvtoperational_Element = Class(name="qvtoperational::Element")
qvtoperational_ResolveExp = Class(name="qvtoperational::ResolveExp")
CallExp = Class(name="CallExp")

# qvtoperational_Constructor class attributes and methods

# ImperativeOperation class attributes and methods

# qvtoperational_ConstructorBody class attributes and methods

# OperationBody class attributes and methods

# qvtoperational_ContextualProperty class attributes and methods

# Property class attributes and methods

# qvtoperational_Class class attributes and methods

# qvtoperational_OCLExpression class attributes and methods

# qvtoperational_Property class attributes and methods

# qvtoperational_DummyRelation class attributes and methods

# Element class attributes and methods

# VarParameter class attributes and methods

# qvtoperational_Library class attributes and methods

# Module class attributes and methods

# qvtoperational_MappingBody class attributes and methods

# qvtoperational_DummyRelationDomain class attributes and methods

# qvtoperational_DummyRelationalTransformation class attributes and methods

# qvtoperational_EntryOperation class attributes and methods

# qvtoperational_Helper class attributes and methods
qvtoperational_Helper_isQuery: Property = Property(name="isQuery", type=StringType)
qvtoperational_Helper.attributes={qvtoperational_Helper_isQuery}

# qvtoperational_ImperativeCallExp class attributes and methods
qvtoperational_ImperativeCallExp_isVirtual: Property = Property(name="isVirtual", type=StringType)
qvtoperational_ImperativeCallExp.attributes={qvtoperational_ImperativeCallExp_isVirtual}

# OperationCallExp class attributes and methods

# ImperativeExpression class attributes and methods

# qvtoperational_ImperativeOperation class attributes and methods
qvtoperational_ImperativeOperation_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
qvtoperational_ImperativeOperation.attributes={qvtoperational_ImperativeOperation_isBlackbox}

# Operation class attributes and methods

# DummyRelation class attributes and methods

# qvtoperational_MappingParameter class attributes and methods

# ModelParameter class attributes and methods

# DummyRelationDomain class attributes and methods

# qvtoperational_ModelParameter class attributes and methods

# qvtoperational_ModelType class attributes and methods
qvtoperational_ModelType_conformanceKind: Property = Property(name="conformanceKind", type=StringType)
qvtoperational_ModelType.attributes={qvtoperational_ModelType_conformanceKind}

# Class class attributes and methods

# qvtoperational_MappingCallExp class attributes and methods
qvtoperational_MappingCallExp_isStrict: Property = Property(name="isStrict", type=StringType)
qvtoperational_MappingCallExp.attributes={qvtoperational_MappingCallExp_isStrict}

# ImperativeCallExp class attributes and methods

# qvtoperational_MappingOperation class attributes and methods

# MappingOperation class attributes and methods

# EntryOperation class attributes and methods

# ModuleImport class attributes and methods

# qvtoperational_TemplateableElement class attributes and methods

# qvtoperational_Variable class attributes and methods

# ModelType class attributes and methods

# qvtoperational_ModuleImport class attributes and methods
qvtoperational_ModuleImport_kind: Property = Property(name="kind", type=StringType)
qvtoperational_ModuleImport.attributes={qvtoperational_ModuleImport_kind}

# qvtoperational_ObjectExp class attributes and methods

# qvtoperational_Package class attributes and methods

# qvtoperational_Module class attributes and methods
qvtoperational_Module_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
qvtoperational_Module.attributes={qvtoperational_Module_isBlackbox}

# qvtoperational_OperationalTransformation class attributes and methods

# Dummy2 class attributes and methods

# InstantiationExp class attributes and methods

# ConstructorBody class attributes and methods

# qvtoperational_OperationBody class attributes and methods

# qvtoperational_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# qvtoperational_VarParameter class attributes and methods
qvtoperational_VarParameter_kind: Property = Property(name="kind", type=StringType)
qvtoperational_VarParameter.attributes={qvtoperational_VarParameter_kind}

# Variable class attributes and methods

# Parameter class attributes and methods

# qvtoperational_Tag class attributes and methods
qvtoperational_Tag_name: Property = Property(name="name", type=StringType)
qvtoperational_Tag_value: Property = Property(name="value", type=StringType)
qvtoperational_Tag.attributes={qvtoperational_Tag_name, qvtoperational_Tag_value}

# qvtoperational_Element class attributes and methods

# qvtoperational_ResolveExp class attributes and methods
qvtoperational_ResolveExp_isDeferred: Property = Property(name="isDeferred", type=StringType)
qvtoperational_ResolveExp_isInverse: Property = Property(name="isInverse", type=StringType)
qvtoperational_ResolveExp_one: Property = Property(name="one", type=StringType)
qvtoperational_ResolveExp.attributes={qvtoperational_ResolveExp_isDeferred, qvtoperational_ResolveExp_isInverse, qvtoperational_ResolveExp_one}

# CallExp class attributes and methods

# Relationships
context0: BinaryAssociation = BinaryAssociation(
    name="context0",
    ends={
        Property(name="qvtoperational_Class", type=qvtoperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ContextualProperty", type=qvtoperational_Class, multiplicity=Multiplicity(1, 1))
    }
)
initExpression1: BinaryAssociation = BinaryAssociation(
    name="initExpression1",
    ends={
        Property(name="qvtoperational_OCLExpression", type=qvtoperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ContextualProperty2", type=qvtoperational_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overridden3: BinaryAssociation = BinaryAssociation(
    name="overridden3",
    ends={
        Property(name="qvtoperational_Property", type=qvtoperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ContextualProperty4", type=qvtoperational_Property, multiplicity=Multiplicity(0, 1))
    }
)
body5: BinaryAssociation = BinaryAssociation(
    name="body5",
    ends={
        Property(name="OperationBody", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ImperativeOperation", type=OperationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context6: BinaryAssociation = BinaryAssociation(
    name="context6",
    ends={
        Property(name="VarParameter", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ImperativeOperation7", type=VarParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overridden8: BinaryAssociation = BinaryAssociation(
    name="overridden8",
    ends={
        Property(name="ImperativeOperation", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ImperativeOperation9", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
result10: BinaryAssociation = BinaryAssociation(
    name="result10",
    ends={
        Property(name="VarParameter12", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ImperativeOperation11", type=VarParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endSection13: BinaryAssociation = BinaryAssociation(
    name="endSection13",
    ends={
        Property(name="qvtoperational_OCLExpression14", type=qvtoperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingBody", type=qvtoperational_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initSection15: BinaryAssociation = BinaryAssociation(
    name="initSection15",
    ends={
        Property(name="qvtoperational_OCLExpression17", type=qvtoperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingBody16", type=qvtoperational_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
merged22: BinaryAssociation = BinaryAssociation(
    name="merged22",
    ends={
        Property(name="MappingOperation24", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation23", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
refinedRelation25: BinaryAssociation = BinaryAssociation(
    name="refinedRelation25",
    ends={
        Property(name="DummyRelation", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation26", type=DummyRelation, multiplicity=Multiplicity(0, 1))
    }
)
when27: BinaryAssociation = BinaryAssociation(
    name="when27",
    ends={
        Property(name="qvtoperational_OCLExpression29", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation28", type=qvtoperational_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where30: BinaryAssociation = BinaryAssociation(
    name="where30",
    ends={
        Property(name="qvtoperational_OCLExpression32", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation31", type=qvtoperational_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extent33: BinaryAssociation = BinaryAssociation(
    name="extent33",
    ends={
        Property(name="ModelParameter", type=qvtoperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingParameter", type=ModelParameter, multiplicity=Multiplicity(0, 1))
    }
)
referredDomain34: BinaryAssociation = BinaryAssociation(
    name="referredDomain34",
    ends={
        Property(name="DummyRelationDomain", type=qvtoperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingParameter35", type=DummyRelationDomain, multiplicity=Multiplicity(0, 1))
    }
)
disjunct18: BinaryAssociation = BinaryAssociation(
    name="disjunct18",
    ends={
        Property(name="MappingOperation", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
inherited19: BinaryAssociation = BinaryAssociation(
    name="inherited19",
    ends={
        Property(name="MappingOperation21", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation20", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
entry42: BinaryAssociation = BinaryAssociation(
    name="entry42",
    ends={
        Property(name="EntryOperation", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_Module43", type=EntryOperation, multiplicity=Multiplicity(0, 1))
    }
)
moduleImport44: BinaryAssociation = BinaryAssociation(
    name="moduleImport44",
    ends={
        Property(name="ModuleImport", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_Module45", type=ModuleImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTag46: BinaryAssociation = BinaryAssociation(
    name="ownedTag46",
    ends={
        Property(name="qvtoperational_TemplateableElement", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_Module47", type=qvtoperational_TemplateableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVariable48: BinaryAssociation = BinaryAssociation(
    name="ownedVariable48",
    ends={
        Property(name="qvtoperational_Variable", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_Module49", type=qvtoperational_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedModelType50: BinaryAssociation = BinaryAssociation(
    name="usedModelType50",
    ends={
        Property(name="ModelType", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_Module51", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
binding52: BinaryAssociation = BinaryAssociation(
    name="binding52",
    ends={
        Property(name="ModelType53", type=qvtoperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModuleImport", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
importedModule54: BinaryAssociation = BinaryAssociation(
    name="importedModule54",
    ends={
        Property(name="Module", type=qvtoperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModuleImport55", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
module56: BinaryAssociation = BinaryAssociation(
    name="module56",
    ends={
        Property(name="Module58", type=qvtoperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModuleImport57", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
additionalCondition36: BinaryAssociation = BinaryAssociation(
    name="additionalCondition36",
    ends={
        Property(name="qvtoperational_OCLExpression37", type=qvtoperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModelType", type=qvtoperational_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel38: BinaryAssociation = BinaryAssociation(
    name="metamodel38",
    ends={
        Property(name="qvtoperational_Package", type=qvtoperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModelType39", type=qvtoperational_Package, multiplicity=Multiplicity(1, 9999))
    }
)
configProperty40: BinaryAssociation = BinaryAssociation(
    name="configProperty40",
    ends={
        Property(name="qvtoperational_Property41", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_Module", type=qvtoperational_Property, multiplicity=Multiplicity(0, 9999))
    }
)
content63: BinaryAssociation = BinaryAssociation(
    name="content63",
    ends={
        Property(name="qvtoperational_OCLExpression64", type=qvtoperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationBody", type=qvtoperational_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation65: BinaryAssociation = BinaryAssociation(
    name="operation65",
    ends={
        Property(name="ImperativeOperation67", type=qvtoperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationBody66", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
variable68: BinaryAssociation = BinaryAssociation(
    name="variable68",
    ends={
        Property(name="qvtoperational_Variable70", type=qvtoperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationBody69", type=qvtoperational_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateClass71: BinaryAssociation = BinaryAssociation(
    name="intermediateClass71",
    ends={
        Property(name="qvtoperational_Class72", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation", type=qvtoperational_Class, multiplicity=Multiplicity(0, 9999))
    }
)
intermediateProperty73: BinaryAssociation = BinaryAssociation(
    name="intermediateProperty73",
    ends={
        Property(name="qvtoperational_Property75", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation74", type=qvtoperational_Property, multiplicity=Multiplicity(0, 9999))
    }
)
modelParameter76: BinaryAssociation = BinaryAssociation(
    name="modelParameter76",
    ends={
        Property(name="ModelParameter78", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation77", type=ModelParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refined79: BinaryAssociation = BinaryAssociation(
    name="refined79",
    ends={
        Property(name="Dummy2", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation80", type=Dummy2, multiplicity=Multiplicity(0, 1))
    }
)
relation81: BinaryAssociation = BinaryAssociation(
    name="relation81",
    ends={
        Property(name="DummyRelation83", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation82", type=DummyRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body59: BinaryAssociation = BinaryAssociation(
    name="body59",
    ends={
        Property(name="ConstructorBody", type=qvtoperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ObjectExp", type=ConstructorBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredObject60: BinaryAssociation = BinaryAssociation(
    name="referredObject60",
    ends={
        Property(name="qvtoperational_Variable62", type=qvtoperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ObjectExp61", type=qvtoperational_Variable, multiplicity=Multiplicity(1, 1))
    }
)
target86: BinaryAssociation = BinaryAssociation(
    name="target86",
    ends={
        Property(name="qvtoperational_Variable88", type=qvtoperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ResolveExp87", type=qvtoperational_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inMapping89: BinaryAssociation = BinaryAssociation(
    name="inMapping89",
    ends={
        Property(name="MappingOperation90", type=qvtoperational_ResolveInExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ResolveInExp", type=MappingOperation, multiplicity=Multiplicity(0, 1))
    }
)
ctxOwner91: BinaryAssociation = BinaryAssociation(
    name="ctxOwner91",
    ends={
        Property(name="ImperativeOperation92", type=qvtoperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_VarParameter", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
resOwner93: BinaryAssociation = BinaryAssociation(
    name="resOwner93",
    ends={
        Property(name="ImperativeOperation95", type=qvtoperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_VarParameter94", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
elements96: BinaryAssociation = BinaryAssociation(
    name="elements96",
    ends={
        Property(name="qvtoperational_Element", type=qvtoperational_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_Tag", type=qvtoperational_Element, multiplicity=Multiplicity(0, 9999))
    }
)
condition84: BinaryAssociation = BinaryAssociation(
    name="condition84",
    ends={
        Property(name="qvtoperational_OCLExpression85", type=qvtoperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ResolveExp", type=qvtoperational_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_qvtoperational_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_Constructor)
gen_qvtoperational_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=qvtoperational_ConstructorBody)
gen_qvtoperational_ContextualProperty_Property = Generalization(general=Property_, specific=qvtoperational_ContextualProperty)
gen_qvtoperational_DummyRelation_Element = Generalization(general=Element, specific=qvtoperational_DummyRelation)
gen_qvtoperational_Library_Module = Generalization(general=Module, specific=qvtoperational_Library)
gen_qvtoperational_MappingBody_OperationBody = Generalization(general=OperationBody, specific=qvtoperational_MappingBody)
gen_qvtoperational_DummyRelationDomain_Element = Generalization(general=Element, specific=qvtoperational_DummyRelationDomain)
gen_qvtoperational_DummyRelationalTransformation_Element = Generalization(general=Element, specific=qvtoperational_DummyRelationalTransformation)
gen_qvtoperational_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_EntryOperation)
gen_qvtoperational_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_Helper)
gen_qvtoperational_ImperativeCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=qvtoperational_ImperativeCallExp)
gen_qvtoperational_ImperativeCallExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=qvtoperational_ImperativeCallExp)
gen_qvtoperational_ImperativeOperation_Operation = Generalization(general=Operation, specific=qvtoperational_ImperativeOperation)
gen_qvtoperational_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=qvtoperational_MappingParameter)
gen_qvtoperational_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=qvtoperational_ModelParameter)
gen_qvtoperational_ModelType_Class = Generalization(general=Class_, specific=qvtoperational_ModelType)
gen_qvtoperational_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=qvtoperational_MappingCallExp)
gen_qvtoperational_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_MappingOperation)
gen_qvtoperational_ModuleImport_Element = Generalization(general=Element, specific=qvtoperational_ModuleImport)
gen_qvtoperational_Module_Class = Generalization(general=Class_, specific=qvtoperational_Module)
gen_qvtoperational_OperationalTransformation_Module = Generalization(general=Module, specific=qvtoperational_OperationalTransformation)
gen_qvtoperational_ObjectExp_InstantiationExp = Generalization(general=InstantiationExp, specific=qvtoperational_ObjectExp)
gen_qvtoperational_OperationBody_Element = Generalization(general=Element, specific=qvtoperational_OperationBody)
gen_qvtoperational_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=qvtoperational_ResolveInExp)
gen_qvtoperational_VarParameter_Variable = Generalization(general=Variable, specific=qvtoperational_VarParameter)
gen_qvtoperational_VarParameter_Parameter = Generalization(general=Parameter_, specific=qvtoperational_VarParameter)
gen_qvtoperational_Tag_Element = Generalization(general=Element, specific=qvtoperational_Tag)
gen_qvtoperational_ResolveExp_CallExp = Generalization(general=CallExp, specific=qvtoperational_ResolveExp)
gen_qvtoperational_ResolveExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=qvtoperational_ResolveExp)

# Domain Model
domain_model = DomainModel(
    name="qvtoperational",
    types={qvtoperational_Constructor, ImperativeOperation, qvtoperational_ConstructorBody, OperationBody, qvtoperational_ContextualProperty, Property_, qvtoperational_Class, qvtoperational_OCLExpression, qvtoperational_Property, qvtoperational_DummyRelation, Element, VarParameter, qvtoperational_Library, Module, qvtoperational_MappingBody, qvtoperational_DummyRelationDomain, qvtoperational_DummyRelationalTransformation, qvtoperational_EntryOperation, qvtoperational_Helper, qvtoperational_ImperativeCallExp, OperationCallExp, ImperativeExpression, qvtoperational_ImperativeOperation, Operation, DummyRelation, qvtoperational_MappingParameter, ModelParameter, DummyRelationDomain, qvtoperational_ModelParameter, qvtoperational_ModelType, Class_, qvtoperational_MappingCallExp, ImperativeCallExp, qvtoperational_MappingOperation, MappingOperation, EntryOperation, ModuleImport, qvtoperational_TemplateableElement, qvtoperational_Variable, ModelType, qvtoperational_ModuleImport, qvtoperational_ObjectExp, qvtoperational_Package, qvtoperational_Module, qvtoperational_OperationalTransformation, Dummy2, InstantiationExp, ConstructorBody, qvtoperational_OperationBody, qvtoperational_ResolveInExp, ResolveExp, qvtoperational_VarParameter, Variable, Parameter_, qvtoperational_Tag, qvtoperational_Element, qvtoperational_ResolveExp, CallExp, DirectionKind, ImportKind},
    associations={context0, initExpression1, overridden3, body5, context6, overridden8, result10, endSection13, initSection15, merged22, refinedRelation25, when27, where30, extent33, referredDomain34, disjunct18, inherited19, entry42, moduleImport44, ownedTag46, ownedVariable48, usedModelType50, binding52, importedModule54, module56, additionalCondition36, metamodel38, configProperty40, content63, operation65, variable68, intermediateClass71, intermediateProperty73, modelParameter76, refined79, relation81, body59, referredObject60, target86, inMapping89, ctxOwner91, resOwner93, elements96, condition84},
    generalizations={gen_qvtoperational_Constructor_ImperativeOperation, gen_qvtoperational_ConstructorBody_OperationBody, gen_qvtoperational_ContextualProperty_Property, gen_qvtoperational_DummyRelation_Element, gen_qvtoperational_Library_Module, gen_qvtoperational_MappingBody_OperationBody, gen_qvtoperational_DummyRelationDomain_Element, gen_qvtoperational_DummyRelationalTransformation_Element, gen_qvtoperational_EntryOperation_ImperativeOperation, gen_qvtoperational_Helper_ImperativeOperation, gen_qvtoperational_ImperativeCallExp_OperationCallExp, gen_qvtoperational_ImperativeCallExp_ImperativeExpression, gen_qvtoperational_ImperativeOperation_Operation, gen_qvtoperational_MappingParameter_VarParameter, gen_qvtoperational_ModelParameter_VarParameter, gen_qvtoperational_ModelType_Class, gen_qvtoperational_MappingCallExp_ImperativeCallExp, gen_qvtoperational_MappingOperation_ImperativeOperation, gen_qvtoperational_ModuleImport_Element, gen_qvtoperational_Module_Class, gen_qvtoperational_OperationalTransformation_Module, gen_qvtoperational_ObjectExp_InstantiationExp, gen_qvtoperational_OperationBody_Element, gen_qvtoperational_ResolveInExp_ResolveExp, gen_qvtoperational_VarParameter_Variable, gen_qvtoperational_VarParameter_Parameter, gen_qvtoperational_Tag_Element, gen_qvtoperational_ResolveExp_CallExp, gen_qvtoperational_ResolveExp_ImperativeExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)