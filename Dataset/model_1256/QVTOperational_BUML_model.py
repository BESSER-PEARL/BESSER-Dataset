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
QVTOperational_ContextualProperty = Class(name="QVTOperational::ContextualProperty")
QVTOperational_Constructor = Class(name="QVTOperational::Constructor")
ImperativeOperation = Class(name="ImperativeOperation")
QVTOperational_ConstructorBody = Class(name="QVTOperational::ConstructorBody")
OperationBody = Class(name="OperationBody")
QVTOperational_EntryOperation = Class(name="QVTOperational::EntryOperation")
QVTOperational_Helper = Class(name="QVTOperational::Helper")
QVTOperational_ImperativeCallExp = Class(name="QVTOperational::ImperativeCallExp")
QVTOperational_ImperativeOperation = Class(name="QVTOperational::ImperativeOperation")
VarParameter = Class(name="VarParameter")
QVTOperational_MappingParameter = Class(name="QVTOperational::MappingParameter")
QVTOperational_Library = Class(name="QVTOperational::Library")
Module = Class(name="Module")
QVTOperational_MappingBody = Class(name="QVTOperational::MappingBody")
QVTOperational_MappingCallExp = Class(name="QVTOperational::MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
QVTOperational_MappingOperation = Class(name="QVTOperational::MappingOperation")
MappingOperation = Class(name="MappingOperation")
ModelType = Class(name="ModelType")
QVTOperational_ModuleImport = Class(name="QVTOperational::ModuleImport")
ModelParameter = Class(name="ModelParameter")
QVTOperational_ModelParameter = Class(name="QVTOperational::ModelParameter")
QVTOperational_ModelType = Class(name="QVTOperational::ModelType")
QVTOperational_Module = Class(name="QVTOperational::Module")
EntryOperation = Class(name="EntryOperation")
ModuleImport = Class(name="ModuleImport")
QVTOperational_ObjectExp = Class(name="QVTOperational::ObjectExp")
ConstructorBody = Class(name="ConstructorBody")
QVTOperational_OperationBody = Class(name="QVTOperational::OperationBody")
QVTOperational_VarParameter = Class(name="QVTOperational::VarParameter")
QVTOperational_OperationalTransformation = Class(name="QVTOperational::OperationalTransformation")
QVTOperational_ResolveExp = Class(name="QVTOperational::ResolveExp")
QVTOperational_ResolveInExp = Class(name="QVTOperational::ResolveInExp")
ResolveExp = Class(name="ResolveExp")

# QVTOperational_ContextualProperty class attributes and methods

# QVTOperational_Constructor class attributes and methods

# ImperativeOperation class attributes and methods

# QVTOperational_ConstructorBody class attributes and methods

# OperationBody class attributes and methods

# QVTOperational_EntryOperation class attributes and methods

# QVTOperational_Helper class attributes and methods
QVTOperational_Helper_isQuery: Property = Property(name="isQuery", type=StringType)
QVTOperational_Helper.attributes={QVTOperational_Helper_isQuery}

# QVTOperational_ImperativeCallExp class attributes and methods
QVTOperational_ImperativeCallExp_isVirtual: Property = Property(name="isVirtual", type=StringType)
QVTOperational_ImperativeCallExp.attributes={QVTOperational_ImperativeCallExp_isVirtual}

# QVTOperational_ImperativeOperation class attributes and methods
QVTOperational_ImperativeOperation_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
QVTOperational_ImperativeOperation.attributes={QVTOperational_ImperativeOperation_isBlackbox}

# VarParameter class attributes and methods

# QVTOperational_MappingParameter class attributes and methods

# QVTOperational_Library class attributes and methods

# Module class attributes and methods

# QVTOperational_MappingBody class attributes and methods

# QVTOperational_MappingCallExp class attributes and methods
QVTOperational_MappingCallExp_isStrict: Property = Property(name="isStrict", type=StringType)
QVTOperational_MappingCallExp.attributes={QVTOperational_MappingCallExp_isStrict}

# ImperativeCallExp class attributes and methods

# QVTOperational_MappingOperation class attributes and methods

# MappingOperation class attributes and methods

# ModelType class attributes and methods

# QVTOperational_ModuleImport class attributes and methods
QVTOperational_ModuleImport_kind: Property = Property(name="kind", type=StringType)
QVTOperational_ModuleImport.attributes={QVTOperational_ModuleImport_kind}

# ModelParameter class attributes and methods

# QVTOperational_ModelParameter class attributes and methods

# QVTOperational_ModelType class attributes and methods
QVTOperational_ModelType_conformanceKind: Property = Property(name="conformanceKind", type=StringType)
QVTOperational_ModelType.attributes={QVTOperational_ModelType_conformanceKind}

# QVTOperational_Module class attributes and methods
QVTOperational_Module_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
QVTOperational_Module.attributes={QVTOperational_Module_isBlackbox}

# EntryOperation class attributes and methods

# ModuleImport class attributes and methods

# QVTOperational_ObjectExp class attributes and methods

# ConstructorBody class attributes and methods

# QVTOperational_OperationBody class attributes and methods

# QVTOperational_VarParameter class attributes and methods
QVTOperational_VarParameter_kind: Property = Property(name="kind", type=StringType)
QVTOperational_VarParameter.attributes={QVTOperational_VarParameter_kind}

# QVTOperational_OperationalTransformation class attributes and methods

# QVTOperational_ResolveExp class attributes and methods
QVTOperational_ResolveExp_isDeferred: Property = Property(name="isDeferred", type=StringType)
QVTOperational_ResolveExp_isInverse: Property = Property(name="isInverse", type=StringType)
QVTOperational_ResolveExp_one: Property = Property(name="one", type=StringType)
QVTOperational_ResolveExp.attributes={QVTOperational_ResolveExp_isInverse, QVTOperational_ResolveExp_one, QVTOperational_ResolveExp_isDeferred}

# QVTOperational_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# Relationships
result5: BinaryAssociation = BinaryAssociation(
    name="result5",
    ends={
        Property(name="QVTOperational_ImperativeOperation6", type=VarParameter, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="VarParameter7", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1))
    }
)
body0: BinaryAssociation = BinaryAssociation(
    name="body0",
    ends={
        Property(name="OperationBody", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation", type=OperationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context1: BinaryAssociation = BinaryAssociation(
    name="context1",
    ends={
        Property(name="VarParameter", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation2", type=VarParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overridden3: BinaryAssociation = BinaryAssociation(
    name="overridden3",
    ends={
        Property(name="ImperativeOperation", type=QVTOperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ImperativeOperation4", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
disjunct8: BinaryAssociation = BinaryAssociation(
    name="disjunct8",
    ends={
        Property(name="MappingOperation", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
inherited9: BinaryAssociation = BinaryAssociation(
    name="inherited9",
    ends={
        Property(name="MappingOperation11", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation10", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
merged12: BinaryAssociation = BinaryAssociation(
    name="merged12",
    ends={
        Property(name="MappingOperation14", type=QVTOperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingOperation13", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
usedModelType19: BinaryAssociation = BinaryAssociation(
    name="usedModelType19",
    ends={
        Property(name="ModelType", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module20", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
extent15: BinaryAssociation = BinaryAssociation(
    name="extent15",
    ends={
        Property(name="ModelParameter", type=QVTOperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_MappingParameter", type=ModelParameter, multiplicity=Multiplicity(0, 1))
    }
)
entry16: BinaryAssociation = BinaryAssociation(
    name="entry16",
    ends={
        Property(name="EntryOperation", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module", type=EntryOperation, multiplicity=Multiplicity(0, 1))
    }
)
moduleImport17: BinaryAssociation = BinaryAssociation(
    name="moduleImport17",
    ends={
        Property(name="ModuleImport", type=QVTOperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_Module18", type=ModuleImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
binding21: BinaryAssociation = BinaryAssociation(
    name="binding21",
    ends={
        Property(name="ModelType22", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
importedModule23: BinaryAssociation = BinaryAssociation(
    name="importedModule23",
    ends={
        Property(name="Module", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport24", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
module25: BinaryAssociation = BinaryAssociation(
    name="module25",
    ends={
        Property(name="Module27", type=QVTOperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ModuleImport26", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
body28: BinaryAssociation = BinaryAssociation(
    name="body28",
    ends={
        Property(name="ConstructorBody", type=QVTOperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ObjectExp", type=ConstructorBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation29: BinaryAssociation = BinaryAssociation(
    name="operation29",
    ends={
        Property(name="ImperativeOperation30", type=QVTOperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationBody", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
modelParameter31: BinaryAssociation = BinaryAssociation(
    name="modelParameter31",
    ends={
        Property(name="ModelParameter32", type=QVTOperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_OperationalTransformation", type=ModelParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inMapping33: BinaryAssociation = BinaryAssociation(
    name="inMapping33",
    ends={
        Property(name="MappingOperation34", type=QVTOperational_ResolveInExp, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_ResolveInExp", type=MappingOperation, multiplicity=Multiplicity(0, 1))
    }
)
ctxOwner35: BinaryAssociation = BinaryAssociation(
    name="ctxOwner35",
    ends={
        Property(name="ImperativeOperation36", type=QVTOperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_VarParameter", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
resOwner37: BinaryAssociation = BinaryAssociation(
    name="resOwner37",
    ends={
        Property(name="ImperativeOperation39", type=QVTOperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="QVTOperational_VarParameter38", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_QVTOperational_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Constructor)
gen_QVTOperational_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_ConstructorBody)
gen_QVTOperational_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_EntryOperation)
gen_QVTOperational_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_Helper)
gen_QVTOperational_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_MappingParameter)
gen_QVTOperational_Library_Module = Generalization(general=Module, specific=QVTOperational_Library)
gen_QVTOperational_MappingBody_OperationBody = Generalization(general=OperationBody, specific=QVTOperational_MappingBody)
gen_QVTOperational_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=QVTOperational_MappingCallExp)
gen_QVTOperational_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=QVTOperational_MappingOperation)
gen_QVTOperational_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=QVTOperational_ModelParameter)
gen_QVTOperational_OperationalTransformation_Module = Generalization(general=Module, specific=QVTOperational_OperationalTransformation)
gen_QVTOperational_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=QVTOperational_ResolveInExp)

# Domain Model
domain_model = DomainModel(
    name="QVTOperational",
    types={QVTOperational_ContextualProperty, QVTOperational_Constructor, ImperativeOperation, QVTOperational_ConstructorBody, OperationBody, QVTOperational_EntryOperation, QVTOperational_Helper, QVTOperational_ImperativeCallExp, QVTOperational_ImperativeOperation, VarParameter, QVTOperational_MappingParameter, QVTOperational_Library, Module, QVTOperational_MappingBody, QVTOperational_MappingCallExp, ImperativeCallExp, QVTOperational_MappingOperation, MappingOperation, ModelType, QVTOperational_ModuleImport, ModelParameter, QVTOperational_ModelParameter, QVTOperational_ModelType, QVTOperational_Module, EntryOperation, ModuleImport, QVTOperational_ObjectExp, ConstructorBody, QVTOperational_OperationBody, QVTOperational_VarParameter, QVTOperational_OperationalTransformation, QVTOperational_ResolveExp, QVTOperational_ResolveInExp, ResolveExp, ImportKind, DirectionKind},
    associations={result5, body0, context1, overridden3, disjunct8, inherited9, merged12, usedModelType19, extent15, entry16, moduleImport17, binding21, importedModule23, module25, body28, operation29, modelParameter31, inMapping33, ctxOwner35, resOwner37},
    generalizations={gen_QVTOperational_Constructor_ImperativeOperation, gen_QVTOperational_ConstructorBody_OperationBody, gen_QVTOperational_EntryOperation_ImperativeOperation, gen_QVTOperational_Helper_ImperativeOperation, gen_QVTOperational_MappingParameter_VarParameter, gen_QVTOperational_Library_Module, gen_QVTOperational_MappingBody_OperationBody, gen_QVTOperational_MappingCallExp_ImperativeCallExp, gen_QVTOperational_MappingOperation_ImperativeOperation, gen_QVTOperational_ModelParameter_VarParameter, gen_QVTOperational_OperationalTransformation_Module, gen_QVTOperational_ResolveInExp_ResolveExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)