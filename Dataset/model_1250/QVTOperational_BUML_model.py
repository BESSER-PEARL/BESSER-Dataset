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
ImportKind: Enumeration = Enumeration(
    name="ImportKind",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="access")
    }
)

DirectionKind: Enumeration = Enumeration(
    name="DirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out")
    }
)

# Classes
QVTOperational_Constructor = Class(name="QVTOperational::Constructor")
ImperativeOperation = Class(name="ImperativeOperation")
QVTOperational_ConstructorBody = Class(name="QVTOperational::ConstructorBody")
OperationBody = Class(name="OperationBody")
QVTOperational_ContextualProperty = Class(name="QVTOperational::ContextualProperty")
Property_ = Class(name="Property")
Class_ = Class(name="Class")
OclExpression = Class(name="OclExpression")
QVTOperational_ImperativeOperation = Class(name="QVTOperational::ImperativeOperation")
Operation = Class(name="Operation")
VarParameter = Class(name="VarParameter")
QVTOperational_Library = Class(name="QVTOperational::Library")
Module = Class(name="Module")
QVTOperational_MappingBody = Class(name="QVTOperational::MappingBody")
QVTOperational_EntryOperation = Class(name="QVTOperational::EntryOperation")
QVTOperational_Helper = Class(name="QVTOperational::Helper")
QVTOperational_ImperativeCallExp = Class(name="QVTOperational::ImperativeCallExp")
OperationCallExp = Class(name="OperationCallExp")
ImperativeExpression = Class(name="ImperativeExpression")
Relation = Class(name="Relation")
QVTOperational_MappingParameter = Class(name="QVTOperational::MappingParameter")
ModelParameter = Class(name="ModelParameter")
RelationDomain = Class(name="RelationDomain")
QVTOperational_ModelParameter = Class(name="QVTOperational::ModelParameter")
OperationalTransformation = Class(name="OperationalTransformation")
QVTOperational_MappingCallExp = Class(name="QVTOperational::MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
QVTOperational_MappingOperation = Class(name="QVTOperational::MappingOperation")
MappingOperation = Class(name="MappingOperation")
ModuleImport = Class(name="ModuleImport")
Tag = Class(name="Tag")
Variable = Class(name="Variable")
ModelType = Class(name="ModelType")
QVTOperational_ModuleImport = Class(name="QVTOperational::ModuleImport")
Element = Class(name="Element")
QVTOperational_ModelType = Class(name="QVTOperational::ModelType")
Package = Class(name="Package")
QVTOperational_Module = Class(name="QVTOperational::Module")
EntryOperation = Class(name="EntryOperation")
QVTOperational_OperationalTransformation = Class(name="QVTOperational::OperationalTransformation")
RelationalTransformation = Class(name="RelationalTransformation")
QVTOperational_ObjectExp = Class(name="QVTOperational::ObjectExp")
InstantiationExp = Class(name="InstantiationExp")
ConstructorBody = Class(name="ConstructorBody")
QVTOperational_OperationBody = Class(name="QVTOperational::OperationBody")
QVTOperational_ResolveInExp = Class(name="QVTOperational::ResolveInExp")
ResolveExp = Class(name="ResolveExp")
QVTOperational_VarParameter = Class(name="QVTOperational::VarParameter")
Parameter_ = Class(name="Parameter")
QVTOperational_ResolveExp = Class(name="QVTOperational::ResolveExp")
CallExp = Class(name="CallExp")

# QVTOperational_Constructor class attributes and methods

# ImperativeOperation class attributes and methods

# QVTOperational_ConstructorBody class attributes and methods

# OperationBody class attributes and methods

# QVTOperational_ContextualProperty class attributes and methods

# Property class attributes and methods

# Class class attributes and methods

# OclExpression class attributes and methods

# QVTOperational_ImperativeOperation class attributes and methods
QVTOperational_ImperativeOperation_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
QVTOperational_ImperativeOperation.attributes={QVTOperational_ImperativeOperation_isBlackbox}

# Operation class attributes and methods

# VarParameter class attributes and methods

# QVTOperational_Library class attributes and methods

# Module class attributes and methods

# QVTOperational_MappingBody class attributes and methods

# QVTOperational_EntryOperation class attributes and methods

# QVTOperational_Helper class attributes and methods
QVTOperational_Helper_isQuery: Property = Property(name="isQuery", type=StringType)
QVTOperational_Helper.attributes={QVTOperational_Helper_isQuery}

# QVTOperational_ImperativeCallExp class attributes and methods
QVTOperational_ImperativeCallExp_isVirtual: Property = Property(name="isVirtual", type=StringType)
QVTOperational_ImperativeCallExp.attributes={QVTOperational_ImperativeCallExp_isVirtual}

# OperationCallExp class attributes and methods

# ImperativeExpression class attributes and methods

# Relation class attributes and methods

# QVTOperational_MappingParameter class attributes and methods

# ModelParameter class attributes and methods

# RelationDomain class attributes and methods

# QVTOperational_ModelParameter class attributes and methods

# OperationalTransformation class attributes and methods

# QVTOperational_MappingCallExp class attributes and methods
QVTOperational_MappingCallExp_isStrict: Property = Property(name="isStrict", type=StringType)
QVTOperational_MappingCallExp.attributes={QVTOperational_MappingCallExp_isStrict}

# ImperativeCallExp class attributes and methods

# QVTOperational_MappingOperation class attributes and methods

# MappingOperation class attributes and methods

# ModuleImport class attributes and methods

# Tag class attributes and methods

# Variable class attributes and methods

# ModelType class attributes and methods

# QVTOperational_ModuleImport class attributes and methods
QVTOperational_ModuleImport_kind: Property = Property(name="kind", type=StringType)
QVTOperational_ModuleImport.attributes={QVTOperational_ModuleImport_kind}

# Element class attributes and methods

# QVTOperational_ModelType class attributes and methods
QVTOperational_ModelType_conformanceKind: Property = Property(name="conformanceKind", type=StringType)
QVTOperational_ModelType.attributes={QVTOperational_ModelType_conformanceKind}

# Package class attributes and methods

# QVTOperational_Module class attributes and methods
QVTOperational_Module_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
QVTOperational_Module.attributes={QVTOperational_Module_isBlackbox}

# EntryOperation class attributes and methods

# QVTOperational_OperationalTransformation class attributes and methods

# RelationalTransformation class attributes and methods

# QVTOperational_ObjectExp class attributes and methods

# InstantiationExp class attributes and methods

# ConstructorBody class attributes and methods

# QVTOperational_OperationBody class attributes and methods

# QVTOperational_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# QVTOperational_VarParameter class attributes and methods
QVTOperational_VarParameter_kind: Property = Property(name="kind", type=StringType)
QVTOperational_VarParameter.attributes={QVTOperational_VarParameter_kind}

# Parameter class attributes and methods

# QVTOperational_ResolveExp class attributes and methods
QVTOperational_ResolveExp_isDeferred: Property = Property(name="isDeferred", type=StringType)
QVTOperational_ResolveExp_isInverse: Property = Property(name="isInverse", type=StringType)
QVTOperational_ResolveExp_one: Property = Property(name="one", type=StringType)
QVTOperational_ResolveExp.attributes={QVTOperational_ResolveExp_isInverse, QVTOperational_ResolveExp_isDeferred, QVTOperational_ResolveExp_one}

# CallExp class attributes and methods

# Relationships
context0: BinaryAssociation = BinaryAssociation(
    name="context0",
    ends={
        Property(name="Class", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
initExpression1: BinaryAssociation = BinaryAssociation(
    name="initExpression1",
    ends={
        Property(name="OclExpression", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty2", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body5: BinaryAssociation = BinaryAssociation(
    name="body5",
    ends={
        Property(name="OperationBody", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation", type=OperationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context6: BinaryAssociation = BinaryAssociation(
    name="context6",
    ends={
        Property(name="VarParameter", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation7", type=VarParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overridden8: BinaryAssociation = BinaryAssociation(
    name="overridden8",
    ends={
        Property(name="ImperativeOperation", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation9", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
result10: BinaryAssociation = BinaryAssociation(
    name="result10",
    ends={
        Property(name="VarParameter12", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation11", type=VarParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endSection13: BinaryAssociation = BinaryAssociation(
    name="endSection13",
    ends={
        Property(name="OclExpression14", type=QVTOperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overridden3: BinaryAssociation = BinaryAssociation(
    name="overridden3",
    ends={
        Property(name="Property", type=QVTOperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ContextualProperty4", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
refinedRelation25: BinaryAssociation = BinaryAssociation(
    name="refinedRelation25",
    ends={
        Property(name="Relation", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation26", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
when27: BinaryAssociation = BinaryAssociation(
    name="when27",
    ends={
        Property(name="OclExpression29", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation28", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where30: BinaryAssociation = BinaryAssociation(
    name="where30",
    ends={
        Property(name="OclExpression32", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation31", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extent33: BinaryAssociation = BinaryAssociation(
    name="extent33",
    ends={
        Property(name="ModelParameter", type=QVTOperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingParameter", type=ModelParameter, multiplicity=Multiplicity(0, 1))
    }
)
referredDomain34: BinaryAssociation = BinaryAssociation(
    name="referredDomain34",
    ends={
        Property(name="RelationDomain", type=QVTOperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingParameter35", type=RelationDomain, multiplicity=Multiplicity(0, 1))
    }
)
module36: BinaryAssociation = BinaryAssociation(
    name="module36",
    ends={
        Property(name="OperationalTransformation", type=QVTOperational_ModelParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModelParameter", type=OperationalTransformation, multiplicity=Multiplicity(1, 1))
    }
)
initSection15: BinaryAssociation = BinaryAssociation(
    name="initSection15",
    ends={
        Property(name="OclExpression17", type=QVTOperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingBody16", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
disjunct18: BinaryAssociation = BinaryAssociation(
    name="disjunct18",
    ends={
        Property(name="MappingOperation", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
inherited19: BinaryAssociation = BinaryAssociation(
    name="inherited19",
    ends={
        Property(name="MappingOperation21", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation20", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
merged22: BinaryAssociation = BinaryAssociation(
    name="merged22",
    ends={
        Property(name="MappingOperation24", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation23", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
moduleImport45: BinaryAssociation = BinaryAssociation(
    name="moduleImport45",
    ends={
        Property(name="ModuleImport", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module46", type=ModuleImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTag47: BinaryAssociation = BinaryAssociation(
    name="ownedTag47",
    ends={
        Property(name="Tag", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module48", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVariable49: BinaryAssociation = BinaryAssociation(
    name="ownedVariable49",
    ends={
        Property(name="Variable", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module50", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedModelType51: BinaryAssociation = BinaryAssociation(
    name="usedModelType51",
    ends={
        Property(name="ModelType", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module52", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
binding53: BinaryAssociation = BinaryAssociation(
    name="binding53",
    ends={
        Property(name="ModelType54", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
importedModule55: BinaryAssociation = BinaryAssociation(
    name="importedModule55",
    ends={
        Property(name="Module", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport56", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
additionalCondition37: BinaryAssociation = BinaryAssociation(
    name="additionalCondition37",
    ends={
        Property(name="OclExpression38", type=QVTOperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModelType", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel39: BinaryAssociation = BinaryAssociation(
    name="metamodel39",
    ends={
        Property(name="Package", type=QVTOperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModelType40", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
configProperty41: BinaryAssociation = BinaryAssociation(
    name="configProperty41",
    ends={
        Property(name="Property42", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
entry43: BinaryAssociation = BinaryAssociation(
    name="entry43",
    ends={
        Property(name="EntryOperation", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module44", type=EntryOperation, multiplicity=Multiplicity(0, 1))
    }
)
content64: BinaryAssociation = BinaryAssociation(
    name="content64",
    ends={
        Property(name="OclExpression65", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation66: BinaryAssociation = BinaryAssociation(
    name="operation66",
    ends={
        Property(name="ImperativeOperation68", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody67", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
variable69: BinaryAssociation = BinaryAssociation(
    name="variable69",
    ends={
        Property(name="Variable71", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody70", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateClass72: BinaryAssociation = BinaryAssociation(
    name="intermediateClass72",
    ends={
        Property(name="Class73", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
intermediateProperty74: BinaryAssociation = BinaryAssociation(
    name="intermediateProperty74",
    ends={
        Property(name="Property76", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation75", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
modelParameter77: BinaryAssociation = BinaryAssociation(
    name="modelParameter77",
    ends={
        Property(name="ModelParameter78", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=ModelParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refined79: BinaryAssociation = BinaryAssociation(
    name="refined79",
    ends={
        Property(name="RelationalTransformation", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation80", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
module57: BinaryAssociation = BinaryAssociation(
    name="module57",
    ends={
        Property(name="Module59", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport58", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
body60: BinaryAssociation = BinaryAssociation(
    name="body60",
    ends={
        Property(name="ConstructorBody", type=QVTOperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ObjectExp", type=ConstructorBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredObject61: BinaryAssociation = BinaryAssociation(
    name="referredObject61",
    ends={
        Property(name="Variable63", type=QVTOperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ObjectExp62", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
inMapping89: BinaryAssociation = BinaryAssociation(
    name="inMapping89",
    ends={
        Property(name="MappingOperation90", type=QVTOperational_ResolveInExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveInExp", type=MappingOperation, multiplicity=Multiplicity(0, 1))
    }
)
ctxOwner91: BinaryAssociation = BinaryAssociation(
    name="ctxOwner91",
    ends={
        Property(name="ImperativeOperation92", type=QVTOperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_VarParameter", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
resOwner93: BinaryAssociation = BinaryAssociation(
    name="resOwner93",
    ends={
        Property(name="ImperativeOperation95", type=QVTOperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_VarParameter94", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
relation81: BinaryAssociation = BinaryAssociation(
    name="relation81",
    ends={
        Property(name="Relation83", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation82", type=Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition84: BinaryAssociation = BinaryAssociation(
    name="condition84",
    ends={
        Property(name="OclExpression85", type=QVTOperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target86: BinaryAssociation = BinaryAssociation(
    name="target86",
    ends={
        Property(name="Variable88", type=QVTOperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveExp87", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_QVTOperational_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Constructor)
gen_QVTOperational_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_ConstructorBody)
gen_QVTOperational_ContextualProperty_Property = Generalization(general=Property_, specific=QVTOperational_ContextualProperty)
gen_QVTOperational_ImperativeOperation_Operation = Generalization(general=Operation, specific=QVTOperational_ImperativeOperation)
gen_QVTOperational_Library_Module = Generalization(general=Module, specific=QVTOperational_Library)
gen_QVTOperational_MappingBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_MappingBody)
gen_QVTOperational_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_EntryOperation)
gen_QVTOperational_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Helper)
gen_QVTOperational_ImperativeCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=QVTOperational_ImperativeCallExp)
gen_QVTOperational_ImperativeCallExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=QVTOperational_ImperativeCallExp)
gen_QVTOperational_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_MappingParameter)
gen_QVTOperational_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_ModelParameter)
gen_QVTOperational_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=QVTOperational_MappingCallExp)
gen_QVTOperational_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_MappingOperation)
gen_QVTOperational_ModuleImport_Element = Generalization(general=Element, specific=QVTOperational_ModuleImport)
gen_QVTOperational_ModelType_Class = Generalization(general=Class_, specific=QVTOperational_ModelType)
gen_QVTOperational_Module_Class = Generalization(general=Class_, specific=QVTOperational_Module)
gen_QVTOperational_Module_Package = Generalization(general=Package, specific=QVTOperational_Module)
gen_QVTOperational_OperationalTransformation_Module = Generalization(general=Module, specific=QVTOperational_OperationalTransformation)
gen_QVTOperational_ObjectExp_InstantiationExp = Generalization(general=InstantiationExp, specific=QVTOperational_ObjectExp)
gen_QVTOperational_OperationBody_Element = Generalization(general=Element, specific=QVTOperational_OperationBody)
gen_QVTOperational_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=QVTOperational_ResolveInExp)
gen_QVTOperational_VarParameter_Variable = Generalization(general=Variable, specific=QVTOperational_VarParameter)
gen_QVTOperational_VarParameter_Parameter = Generalization(general=Parameter_, specific=QVTOperational_VarParameter)
gen_QVTOperational_ResolveExp_CallExp = Generalization(general=CallExp, specific=QVTOperational_ResolveExp)
gen_QVTOperational_ResolveExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=QVTOperational_ResolveExp)

# Domain Model
domain_model = DomainModel(
    name="QVTOperational",
    types={QVTOperational_Constructor, ImperativeOperation, QVTOperational_ConstructorBody, OperationBody, QVTOperational_ContextualProperty, Property_, Class_, OclExpression, QVTOperational_ImperativeOperation, Operation, VarParameter, QVTOperational_Library, Module, QVTOperational_MappingBody, QVTOperational_EntryOperation, QVTOperational_Helper, QVTOperational_ImperativeCallExp, OperationCallExp, ImperativeExpression, Relation, QVTOperational_MappingParameter, ModelParameter, RelationDomain, QVTOperational_ModelParameter, OperationalTransformation, QVTOperational_MappingCallExp, ImperativeCallExp, QVTOperational_MappingOperation, MappingOperation, ModuleImport, Tag, Variable, ModelType, QVTOperational_ModuleImport, Element, QVTOperational_ModelType, Package, QVTOperational_Module, EntryOperation, QVTOperational_OperationalTransformation, RelationalTransformation, QVTOperational_ObjectExp, InstantiationExp, ConstructorBody, QVTOperational_OperationBody, QVTOperational_ResolveInExp, ResolveExp, QVTOperational_VarParameter, Parameter_, QVTOperational_ResolveExp, CallExp, ImportKind, DirectionKind},
    associations={context0, initExpression1, body5, context6, overridden8, result10, endSection13, overridden3, refinedRelation25, when27, where30, extent33, referredDomain34, module36, initSection15, disjunct18, inherited19, merged22, moduleImport45, ownedTag47, ownedVariable49, usedModelType51, binding53, importedModule55, additionalCondition37, metamodel39, configProperty41, entry43, content64, operation66, variable69, intermediateClass72, intermediateProperty74, modelParameter77, refined79, module57, body60, referredObject61, inMapping89, ctxOwner91, resOwner93, relation81, condition84, target86},
    generalizations={gen_QVTOperational_Constructor_ImperativeOperation, gen_QVTOperational_ConstructorBody_OperationBody, gen_QVTOperational_ContextualProperty_Property, gen_QVTOperational_ImperativeOperation_Operation, gen_QVTOperational_Library_Module, gen_QVTOperational_MappingBody_OperationBody, gen_QVTOperational_EntryOperation_ImperativeOperation, gen_QVTOperational_Helper_ImperativeOperation, gen_QVTOperational_ImperativeCallExp_OperationCallExp, gen_QVTOperational_ImperativeCallExp_ImperativeExpression, gen_QVTOperational_MappingParameter_VarParameter, gen_QVTOperational_ModelParameter_VarParameter, gen_QVTOperational_MappingCallExp_ImperativeCallExp, gen_QVTOperational_MappingOperation_ImperativeOperation, gen_QVTOperational_ModuleImport_Element, gen_QVTOperational_ModelType_Class, gen_QVTOperational_Module_Class, gen_QVTOperational_Module_Package, gen_QVTOperational_OperationalTransformation_Module, gen_QVTOperational_ObjectExp_InstantiationExp, gen_QVTOperational_OperationBody_Element, gen_QVTOperational_ResolveInExp_ResolveExp, gen_QVTOperational_VarParameter_Variable, gen_QVTOperational_VarParameter_Parameter, gen_QVTOperational_ResolveExp_CallExp, gen_QVTOperational_ResolveExp_ImperativeExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)