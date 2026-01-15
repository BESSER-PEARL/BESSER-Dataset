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
emig_MyModel = Class(name="emig::MyModel")
emig_MigrationLibrary = Class(name="emig::MigrationLibrary")
emig_MigrationProgram = Class(name="emig::MigrationProgram")
emig_Rule = Class(name="emig::Rule")
emig_Artifact = Class(name="emig::Artifact")
emig_EPackage = Class(name="emig::EPackage")
emig_OpDef = Class(name="emig::OpDef")
emig_RewritingRule = Class(name="emig::RewritingRule")
emig_setterDef = Class(name="emig::setterDef")
emig_EPackageOpDef = Class(name="emig::EPackageOpDef")
OpDef = Class(name="OpDef")
emig_EClassOpDef = Class(name="emig::EClassOpDef")
emig_EClass = Class(name="emig::EClass")
emig_EAttribute = Class(name="emig::EAttribute")
emig_EReference = Class(name="emig::EReference")
emig_EStructuralFeature = Class(name="emig::EStructuralFeature")
emig_Parameter = Class(name="emig::Parameter")
emig_EAttributeOpDef = Class(name="emig::EAttributeOpDef")
emig_EReferenceOpDef = Class(name="emig::EReferenceOpDef")
emig_Migrator = Class(name="emig::Migrator")
Migrator = Class(name="Migrator")
emig_VariableDeclaration = Class(name="emig::VariableDeclaration")
emig_FilterMigrator = Class(name="emig::FilterMigrator")
emig_MigratorSX = Class(name="emig::MigratorSX")
emig_MigratorDX = Class(name="emig::MigratorDX")
emig_DotNavigationObjDX = Class(name="emig::DotNavigationObjDX")
emig_Package = Class(name="emig::Package")
EPackage = Class(name="EPackage")
emig_OclExpression = Class(name="emig::OclExpression")
emig_DotNavigationObjSX = Class(name="emig::DotNavigationObjSX")
emig_EObject = Class(name="emig::EObject")
emig_VariableExp = Class(name="emig::VariableExp")
VariableExp = Class(name="VariableExp")
emig_SuperExp = Class(name="emig::SuperExp")
SuperExp = Class(name="SuperExp")
emig_BagExp = Class(name="emig::BagExp")
BagExp = Class(name="BagExp")
emig_OrderedSetExp = Class(name="emig::OrderedSetExp")
OrderedSetExp = Class(name="OrderedSetExp")
emig_SequenceExp = Class(name="emig::SequenceExp")
SequenceExp = Class(name="SequenceExp")
emig_SetExp = Class(name="emig::SetExp")
SetExp = Class(name="SetExp")
emig_TupleExp = Class(name="emig::TupleExp")
TupleExp = Class(name="TupleExp")
emig_MapExp = Class(name="emig::MapExp")
MapExp = Class(name="MapExp")
emig_Class = Class(name="emig::Class")
EClass = Class(name="EClass")
emig_Attribute = Class(name="emig::Attribute")
EAttribute = Class(name="EAttribute")
emig_Reference = Class(name="emig::Reference")
EReference = Class(name="EReference")
emig_NavigationOrAttributeCallExp = Class(name="emig::NavigationOrAttributeCallExp")
OclExpression = Class(name="OclExpression")
emig_OclUndefinedExp = Class(name="emig::OclUndefinedExp")
OclUndefinedExp = Class(name="OclUndefinedExp")

# emig_MyModel class attributes and methods

# emig_MigrationLibrary class attributes and methods
emig_MigrationLibrary_title: Property = Property(name="title", type=StringType)
emig_MigrationLibrary.attributes={emig_MigrationLibrary_title}

# emig_MigrationProgram class attributes and methods
emig_MigrationProgram_libs: Property = Property(name="libs", type=StringType)
emig_MigrationProgram_migr: Property = Property(name="migr", type=StringType)
emig_MigrationProgram_name: Property = Property(name="name", type=StringType)
emig_MigrationProgram_delta: Property = Property(name="delta", type=StringType)
emig_MigrationProgram.attributes={emig_MigrationProgram_migr, emig_MigrationProgram_name, emig_MigrationProgram_libs, emig_MigrationProgram_delta}

# emig_Rule class attributes and methods
emig_Rule_name: Property = Property(name="name", type=StringType)
emig_Rule.attributes={emig_Rule_name}

# emig_Artifact class attributes and methods
emig_Artifact_type: Property = Property(name="type", type=StringType)
emig_Artifact.attributes={emig_Artifact_type}

# emig_EPackage class attributes and methods

# emig_OpDef class attributes and methods
emig_OpDef_op: Property = Property(name="op", type=StringType)
emig_OpDef.attributes={emig_OpDef_op}

# emig_RewritingRule class attributes and methods

# emig_setterDef class attributes and methods
emig_setterDef_operator: Property = Property(name="operator", type=StringType)
emig_setterDef.attributes={emig_setterDef_operator}

# emig_EPackageOpDef class attributes and methods

# OpDef class attributes and methods

# emig_EClassOpDef class attributes and methods

# emig_EClass class attributes and methods

# emig_EAttribute class attributes and methods

# emig_EReference class attributes and methods

# emig_EStructuralFeature class attributes and methods

# emig_Parameter class attributes and methods
emig_Parameter_name: Property = Property(name="name", type=StringType)
emig_Parameter.attributes={emig_Parameter_name}

# emig_EAttributeOpDef class attributes and methods

# emig_EReferenceOpDef class attributes and methods

# emig_Migrator class attributes and methods

# Migrator class attributes and methods

# emig_VariableDeclaration class attributes and methods

# emig_FilterMigrator class attributes and methods

# emig_MigratorSX class attributes and methods

# emig_MigratorDX class attributes and methods
emig_MigratorDX_name: Property = Property(name="name", type=StringType)
emig_MigratorDX.attributes={emig_MigratorDX_name}

# emig_DotNavigationObjDX class attributes and methods

# emig_Package class attributes and methods

# EPackage class attributes and methods

# emig_OclExpression class attributes and methods

# emig_DotNavigationObjSX class attributes and methods

# emig_EObject class attributes and methods

# emig_VariableExp class attributes and methods

# VariableExp class attributes and methods

# emig_SuperExp class attributes and methods

# SuperExp class attributes and methods

# emig_BagExp class attributes and methods

# BagExp class attributes and methods

# emig_OrderedSetExp class attributes and methods

# OrderedSetExp class attributes and methods

# emig_SequenceExp class attributes and methods

# SequenceExp class attributes and methods

# emig_SetExp class attributes and methods

# SetExp class attributes and methods

# emig_TupleExp class attributes and methods

# TupleExp class attributes and methods

# emig_MapExp class attributes and methods

# MapExp class attributes and methods

# emig_Class class attributes and methods

# EClass class attributes and methods

# emig_Attribute class attributes and methods

# EAttribute class attributes and methods

# emig_Reference class attributes and methods

# EReference class attributes and methods

# emig_NavigationOrAttributeCallExp class attributes and methods

# OclExpression class attributes and methods

# emig_OclUndefinedExp class attributes and methods

# OclUndefinedExp class attributes and methods

# Relationships
migrationLib0: BinaryAssociation = BinaryAssociation(
    name="migrationLib0",
    ends={
        Property(name="emig_MigrationLibrary", type=emig_MyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MyModel", type=emig_MigrationLibrary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MigrationProgr1: BinaryAssociation = BinaryAssociation(
    name="MigrationProgr1",
    ends={
        Property(name="emig_MigrationProgram", type=emig_MyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MyModel2", type=emig_MigrationProgram, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rules3: BinaryAssociation = BinaryAssociation(
    name="rules3",
    ends={
        Property(name="emig_Rule", type=emig_MigrationLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigrationLibrary4", type=emig_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArt5: BinaryAssociation = BinaryAssociation(
    name="typeArt5",
    ends={
        Property(name="emig_Artifact", type=emig_MigrationProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigrationProgram6", type=emig_Artifact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transformationPackage7: BinaryAssociation = BinaryAssociation(
    name="transformationPackage7",
    ends={
        Property(name="emig_EPackage", type=emig_MigrationProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigrationProgram8", type=emig_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
rules9: BinaryAssociation = BinaryAssociation(
    name="rules9",
    ends={
        Property(name="emig_Rule11", type=emig_MigrationProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigrationProgram10", type=emig_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filter12: BinaryAssociation = BinaryAssociation(
    name="filter12",
    ends={
        Property(name="emig_OpDef", type=emig_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_Rule13", type=emig_OpDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rewritingRules14: BinaryAssociation = BinaryAssociation(
    name="rewritingRules14",
    ends={
        Property(name="emig_RewritingRule", type=emig_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_Rule15", type=emig_RewritingRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setters16: BinaryAssociation = BinaryAssociation(
    name="setters16",
    ends={
        Property(name="emig_setterDef", type=emig_OpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_OpDef17", type=emig_setterDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var18: BinaryAssociation = BinaryAssociation(
    name="var18",
    ends={
        Property(name="emig_EPackage19", type=emig_EPackageOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EPackageOpDef", type=emig_EPackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref20: BinaryAssociation = BinaryAssociation(
    name="ref20",
    ends={
        Property(name="emig_EPackage22", type=emig_EPackageOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EPackageOpDef21", type=emig_EPackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classes23: BinaryAssociation = BinaryAssociation(
    name="classes23",
    ends={
        Property(name="emig_EClassOpDef", type=emig_EPackageOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EPackageOpDef24", type=emig_EClassOpDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var34: BinaryAssociation = BinaryAssociation(
    name="var34",
    ends={
        Property(name="emig_EAttribute", type=emig_EAttributeOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EAttributeOpDef35", type=emig_EAttribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref36: BinaryAssociation = BinaryAssociation(
    name="ref36",
    ends={
        Property(name="emig_EAttribute38", type=emig_EAttributeOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EAttributeOpDef37", type=emig_EAttribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var39: BinaryAssociation = BinaryAssociation(
    name="var39",
    ends={
        Property(name="emig_EReference", type=emig_EReferenceOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EReferenceOpDef40", type=emig_EReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref41: BinaryAssociation = BinaryAssociation(
    name="ref41",
    ends={
        Property(name="emig_EReference43", type=emig_EReferenceOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EReferenceOpDef42", type=emig_EReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metafeature44: BinaryAssociation = BinaryAssociation(
    name="metafeature44",
    ends={
        Property(name="emig_EStructuralFeature", type=emig_setterDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_setterDef45", type=emig_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
var25: BinaryAssociation = BinaryAssociation(
    name="var25",
    ends={
        Property(name="emig_EClass", type=emig_EClassOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EClassOpDef26", type=emig_EClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
par46: BinaryAssociation = BinaryAssociation(
    name="par46",
    ends={
        Property(name="emig_Parameter", type=emig_setterDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_setterDef47", type=emig_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref27: BinaryAssociation = BinaryAssociation(
    name="ref27",
    ends={
        Property(name="emig_EClass29", type=emig_EClassOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EClassOpDef28", type=emig_EClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes30: BinaryAssociation = BinaryAssociation(
    name="attributes30",
    ends={
        Property(name="emig_EAttributeOpDef", type=emig_EClassOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EClassOpDef31", type=emig_EAttributeOpDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references32: BinaryAssociation = BinaryAssociation(
    name="references32",
    ends={
        Property(name="emig_EReferenceOpDef", type=emig_EClassOpDef, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_EClassOpDef33", type=emig_EReferenceOpDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
migratorSX52: BinaryAssociation = BinaryAssociation(
    name="migratorSX52",
    ends={
        Property(name="emig_RewritingRule53", type=emig_MigratorSX, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="emig_MigratorSX54", type=emig_RewritingRule, multiplicity=Multiplicity(1, 1))
    }
)
name55: BinaryAssociation = BinaryAssociation(
    name="name55",
    ends={
        Property(name="emig_VariableDeclaration", type=emig_MigratorSX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigratorSX56", type=emig_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementSX57: BinaryAssociation = BinaryAssociation(
    name="elementSX57",
    ends={
        Property(name="emig_EClass59", type=emig_MigratorSX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigratorSX58", type=emig_EClass, multiplicity=Multiplicity(0, 1))
    }
)
filterSX60: BinaryAssociation = BinaryAssociation(
    name="filterSX60",
    ends={
        Property(name="emig_FilterMigrator", type=emig_MigratorSX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigratorSX61", type=emig_FilterMigrator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementDX62: BinaryAssociation = BinaryAssociation(
    name="elementDX62",
    ends={
        Property(name="emig_EClass64", type=emig_MigratorDX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigratorDX63", type=emig_EClass, multiplicity=Multiplicity(0, 1))
    }
)
filterDX65: BinaryAssociation = BinaryAssociation(
    name="filterDX65",
    ends={
        Property(name="emig_FilterMigrator67", type=emig_MigratorDX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_MigratorDX66", type=emig_FilterMigrator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
migratorsSX48: BinaryAssociation = BinaryAssociation(
    name="migratorsSX48",
    ends={
        Property(name="emig_MigratorSX", type=emig_RewritingRule, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_RewritingRule49", type=emig_MigratorSX, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
migratorDX50: BinaryAssociation = BinaryAssociation(
    name="migratorDX50",
    ends={
        Property(name="emig_MigratorDX", type=emig_RewritingRule, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_RewritingRule51", type=emig_MigratorDX, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref71: BinaryAssociation = BinaryAssociation(
    name="ref71",
    ends={
        Property(name="emig_EStructuralFeature73", type=emig_DotNavigationObjSX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_DotNavigationObjSX72", type=emig_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
obj74: BinaryAssociation = BinaryAssociation(
    name="obj74",
    ends={
        Property(name="emig_EObject75", type=emig_DotNavigationObjDX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_DotNavigationObjDX", type=emig_EObject, multiplicity=Multiplicity(0, 1))
    }
)
ref76: BinaryAssociation = BinaryAssociation(
    name="ref76",
    ends={
        Property(name="emig_EStructuralFeature78", type=emig_DotNavigationObjDX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_DotNavigationObjDX77", type=emig_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
specification68: BinaryAssociation = BinaryAssociation(
    name="specification68",
    ends={
        Property(name="emig_OclExpression", type=emig_FilterMigrator, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_FilterMigrator69", type=emig_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
src79: BinaryAssociation = BinaryAssociation(
    name="src79",
    ends={
        Property(name="emig_OclExpression80", type=emig_NavigationOrAttributeCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_NavigationOrAttributeCallExp", type=emig_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
obj70: BinaryAssociation = BinaryAssociation(
    name="obj70",
    ends={
        Property(name="emig_EObject", type=emig_DotNavigationObjSX, multiplicity=Multiplicity(1, 1)),
        Property(name="emig_DotNavigationObjSX", type=emig_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_emig_EPackageOpDef_OpDef = Generalization(general=OpDef, specific=emig_EPackageOpDef)
gen_emig_EClassOpDef_OpDef = Generalization(general=OpDef, specific=emig_EClassOpDef)
gen_emig_EAttributeOpDef_OpDef = Generalization(general=OpDef, specific=emig_EAttributeOpDef)
gen_emig_EReferenceOpDef_OpDef = Generalization(general=OpDef, specific=emig_EReferenceOpDef)
gen_emig_MigratorSX_Migrator = Generalization(general=Migrator, specific=emig_MigratorSX)
gen_emig_MigratorDX_Migrator = Generalization(general=Migrator, specific=emig_MigratorDX)
gen_emig_Package_EPackage = Generalization(general=EPackage, specific=emig_Package)
gen_emig_VariableExp_VariableExp = Generalization(general=VariableExp, specific=emig_VariableExp)
gen_emig_SuperExp_SuperExp = Generalization(general=SuperExp, specific=emig_SuperExp)
gen_emig_BagExp_BagExp = Generalization(general=BagExp, specific=emig_BagExp)
gen_emig_OrderedSetExp_OrderedSetExp = Generalization(general=OrderedSetExp, specific=emig_OrderedSetExp)
gen_emig_SequenceExp_SequenceExp = Generalization(general=SequenceExp, specific=emig_SequenceExp)
gen_emig_SetExp_SetExp = Generalization(general=SetExp, specific=emig_SetExp)
gen_emig_TupleExp_TupleExp = Generalization(general=TupleExp, specific=emig_TupleExp)
gen_emig_MapExp_MapExp = Generalization(general=MapExp, specific=emig_MapExp)
gen_emig_Class_EClass = Generalization(general=EClass, specific=emig_Class)
gen_emig_Attribute_EAttribute = Generalization(general=EAttribute, specific=emig_Attribute)
gen_emig_Reference_EReference = Generalization(general=EReference, specific=emig_Reference)
gen_emig_NavigationOrAttributeCallExp_OclExpression = Generalization(general=OclExpression, specific=emig_NavigationOrAttributeCallExp)
gen_emig_OclUndefinedExp_OclUndefinedExp = Generalization(general=OclUndefinedExp, specific=emig_OclUndefinedExp)

# Domain Model
domain_model = DomainModel(
    name="emig",
    types={emig_MyModel, emig_MigrationLibrary, emig_MigrationProgram, emig_Rule, emig_Artifact, emig_EPackage, emig_OpDef, emig_RewritingRule, emig_setterDef, emig_EPackageOpDef, OpDef, emig_EClassOpDef, emig_EClass, emig_EAttribute, emig_EReference, emig_EStructuralFeature, emig_Parameter, emig_EAttributeOpDef, emig_EReferenceOpDef, emig_Migrator, Migrator, emig_VariableDeclaration, emig_FilterMigrator, emig_MigratorSX, emig_MigratorDX, emig_DotNavigationObjDX, emig_Package, EPackage, emig_OclExpression, emig_DotNavigationObjSX, emig_EObject, emig_VariableExp, VariableExp, emig_SuperExp, SuperExp, emig_BagExp, BagExp, emig_OrderedSetExp, OrderedSetExp, emig_SequenceExp, SequenceExp, emig_SetExp, SetExp, emig_TupleExp, TupleExp, emig_MapExp, MapExp, emig_Class, EClass, emig_Attribute, EAttribute, emig_Reference, EReference, emig_NavigationOrAttributeCallExp, OclExpression, emig_OclUndefinedExp, OclUndefinedExp},
    associations={migrationLib0, MigrationProgr1, rules3, typeArt5, transformationPackage7, rules9, filter12, rewritingRules14, setters16, var18, ref20, classes23, var34, ref36, var39, ref41, metafeature44, var25, par46, ref27, attributes30, references32, migratorSX52, name55, elementSX57, filterSX60, elementDX62, filterDX65, migratorsSX48, migratorDX50, ref71, obj74, ref76, specification68, src79, obj70},
    generalizations={gen_emig_EPackageOpDef_OpDef, gen_emig_EClassOpDef_OpDef, gen_emig_EAttributeOpDef_OpDef, gen_emig_EReferenceOpDef_OpDef, gen_emig_MigratorSX_Migrator, gen_emig_MigratorDX_Migrator, gen_emig_Package_EPackage, gen_emig_VariableExp_VariableExp, gen_emig_SuperExp_SuperExp, gen_emig_BagExp_BagExp, gen_emig_OrderedSetExp_OrderedSetExp, gen_emig_SequenceExp_SequenceExp, gen_emig_SetExp_SetExp, gen_emig_TupleExp_TupleExp, gen_emig_MapExp_MapExp, gen_emig_Class_EClass, gen_emig_Attribute_EAttribute, gen_emig_Reference_EReference, gen_emig_NavigationOrAttributeCallExp_OclExpression, gen_emig_OclUndefinedExp_OclUndefinedExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)