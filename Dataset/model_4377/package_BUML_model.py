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
KragsteinPackage_Dependency = Class(name="KragsteinPackage::Dependency")
KragsteinPackage_Package = Class(name="KragsteinPackage::Package")
KragsteinPackage_Unit = Class(name="KragsteinPackage::Unit", is_abstract=True)
KragsteinPackage_Relationship = Class(name="KragsteinPackage::Relationship", is_abstract=True)
KragsteinPackage_Class = Class(name="KragsteinPackage::Class")
KragsteinPackage_Generalization = Class(name="KragsteinPackage::Generalization")
Relationship = Class(name="Relationship")
KragsteinPackage_Realization = Class(name="KragsteinPackage::Realization")
KragsteinPackage_Association = Class(name="KragsteinPackage::Association")
KragsteinPackage_Aggregation = Class(name="KragsteinPackage::Aggregation")
KragsteinPackage_Composition = Class(name="KragsteinPackage::Composition")
KragsteinPackage_Note = Class(name="KragsteinPackage::Note")
Unit = Class(name="Unit")
KragsteinPackage_Attribute = Class(name="KragsteinPackage::Attribute")
KragsteinPackage_Method = Class(name="KragsteinPackage::Method")
KragsteinPackage_ImportedClass = Class(name="KragsteinPackage::ImportedClass")
KragsteinPackage_Parameter = Class(name="KragsteinPackage::Parameter")
KragsteinPackage_Link = Class(name="KragsteinPackage::Link")

# KragsteinPackage_Dependency class attributes and methods

# KragsteinPackage_Package class attributes and methods
KragsteinPackage_Package_name: Property = Property(name="name", type=StringType)
KragsteinPackage_Package_path: Property = Property(name="path", type=StringType)
KragsteinPackage_Package.attributes={KragsteinPackage_Package_name, KragsteinPackage_Package_path}

# KragsteinPackage_Unit class attributes and methods

# KragsteinPackage_Relationship class attributes and methods
KragsteinPackage_Relationship_name: Property = Property(name="name", type=StringType)
KragsteinPackage_Relationship_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
KragsteinPackage_Relationship_upperBound: Property = Property(name="upperBound", type=IntegerType)
KragsteinPackage_Relationship.attributes={KragsteinPackage_Relationship_name, KragsteinPackage_Relationship_upperBound, KragsteinPackage_Relationship_lowerBound}

# KragsteinPackage_Class class attributes and methods
KragsteinPackage_Class_name: Property = Property(name="name", type=StringType)
KragsteinPackage_Class_visibility: Property = Property(name="visibility", type=StringType)
KragsteinPackage_Class_isSingletone: Property = Property(name="isSingletone", type=BooleanType)
KragsteinPackage_Class_isInterface: Property = Property(name="isInterface", type=BooleanType)
KragsteinPackage_Class_superClass: Property = Property(name="superClass", type=StringType)
KragsteinPackage_Class_supplierElement: Property = Property(name="supplierElement", type=StringType)
KragsteinPackage_Class.attributes={KragsteinPackage_Class_name, KragsteinPackage_Class_supplierElement, KragsteinPackage_Class_isSingletone, KragsteinPackage_Class_superClass, KragsteinPackage_Class_isInterface, KragsteinPackage_Class_visibility}

# KragsteinPackage_Generalization class attributes and methods
KragsteinPackage_Generalization_type: Property = Property(name="type", type=StringType)
KragsteinPackage_Generalization.attributes={KragsteinPackage_Generalization_type}

# Relationship class attributes and methods

# KragsteinPackage_Realization class attributes and methods

# KragsteinPackage_Association class attributes and methods

# KragsteinPackage_Aggregation class attributes and methods

# KragsteinPackage_Composition class attributes and methods

# KragsteinPackage_Note class attributes and methods
KragsteinPackage_Note_name: Property = Property(name="name", type=StringType)
KragsteinPackage_Note_text: Property = Property(name="text", type=StringType)
KragsteinPackage_Note.attributes={KragsteinPackage_Note_text, KragsteinPackage_Note_name}

# Unit class attributes and methods

# KragsteinPackage_Attribute class attributes and methods
KragsteinPackage_Attribute_name: Property = Property(name="name", type=StringType)
KragsteinPackage_Attribute_type: Property = Property(name="type", type=StringType)
KragsteinPackage_Attribute_visibility: Property = Property(name="visibility", type=StringType)
KragsteinPackage_Attribute_isConst: Property = Property(name="isConst", type=BooleanType)
KragsteinPackage_Attribute_isStatic: Property = Property(name="isStatic", type=BooleanType)
KragsteinPackage_Attribute_value: Property = Property(name="value", type=StringType)
KragsteinPackage_Attribute.attributes={KragsteinPackage_Attribute_visibility, KragsteinPackage_Attribute_type, KragsteinPackage_Attribute_name, KragsteinPackage_Attribute_isStatic, KragsteinPackage_Attribute_value, KragsteinPackage_Attribute_isConst}

# KragsteinPackage_Method class attributes and methods
KragsteinPackage_Method_name: Property = Property(name="name", type=StringType)
KragsteinPackage_Method_type: Property = Property(name="type", type=StringType)
KragsteinPackage_Method_visibility: Property = Property(name="visibility", type=StringType)
KragsteinPackage_Method_isConst: Property = Property(name="isConst", type=BooleanType)
KragsteinPackage_Method_isVirtual: Property = Property(name="isVirtual", type=BooleanType)
KragsteinPackage_Method_isStatic: Property = Property(name="isStatic", type=BooleanType)
KragsteinPackage_Method.attributes={KragsteinPackage_Method_visibility, KragsteinPackage_Method_isConst, KragsteinPackage_Method_isStatic, KragsteinPackage_Method_name, KragsteinPackage_Method_isVirtual, KragsteinPackage_Method_type}

# KragsteinPackage_ImportedClass class attributes and methods
KragsteinPackage_ImportedClass_name: Property = Property(name="name", type=StringType)
KragsteinPackage_ImportedClass_path: Property = Property(name="path", type=StringType)
KragsteinPackage_ImportedClass_isInternal: Property = Property(name="isInternal", type=BooleanType)
KragsteinPackage_ImportedClass.attributes={KragsteinPackage_ImportedClass_isInternal, KragsteinPackage_ImportedClass_name, KragsteinPackage_ImportedClass_path}

# KragsteinPackage_Parameter class attributes and methods
KragsteinPackage_Parameter_name: Property = Property(name="name", type=StringType)
KragsteinPackage_Parameter_type: Property = Property(name="type", type=StringType)
KragsteinPackage_Parameter_value: Property = Property(name="value", type=StringType)
KragsteinPackage_Parameter.attributes={KragsteinPackage_Parameter_value, KragsteinPackage_Parameter_name, KragsteinPackage_Parameter_type}

# KragsteinPackage_Link class attributes and methods

# Relationships
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="KragsteinPackage_Unit", type=KragsteinPackage_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Package", type=KragsteinPackage_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="KragsteinPackage_Class", type=KragsteinPackage_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Relationship", type=KragsteinPackage_Class, multiplicity=Multiplicity(0, 1))
    }
)
source2: BinaryAssociation = BinaryAssociation(
    name="source2",
    ends={
        Property(name="KragsteinPackage_Class4", type=KragsteinPackage_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Relationship3", type=KragsteinPackage_Class, multiplicity=Multiplicity(0, 1))
    }
)
attribute5: BinaryAssociation = BinaryAssociation(
    name="attribute5",
    ends={
        Property(name="KragsteinPackage_Attribute", type=KragsteinPackage_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Class6", type=KragsteinPackage_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method7: BinaryAssociation = BinaryAssociation(
    name="method7",
    ends={
        Property(name="KragsteinPackage_Method", type=KragsteinPackage_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Class8", type=KragsteinPackage_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetRelationship9: BinaryAssociation = BinaryAssociation(
    name="targetRelationship9",
    ends={
        Property(name="KragsteinPackage_Relationship11", type=KragsteinPackage_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Class10", type=KragsteinPackage_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedClass12: BinaryAssociation = BinaryAssociation(
    name="importedClass12",
    ends={
        Property(name="KragsteinPackage_ImportedClass", type=KragsteinPackage_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Class13", type=KragsteinPackage_ImportedClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter14: BinaryAssociation = BinaryAssociation(
    name="parameter14",
    ends={
        Property(name="KragsteinPackage_Parameter", type=KragsteinPackage_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Method15", type=KragsteinPackage_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetLink16: BinaryAssociation = BinaryAssociation(
    name="targetLink16",
    ends={
        Property(name="KragsteinPackage_Link", type=KragsteinPackage_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Unit17", type=KragsteinPackage_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="KragsteinPackage_Unit20", type=KragsteinPackage_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Link19", type=KragsteinPackage_Unit, multiplicity=Multiplicity(0, 1))
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="KragsteinPackage_Unit23", type=KragsteinPackage_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="KragsteinPackage_Link22", type=KragsteinPackage_Unit, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_KragsteinPackage_Dependency_Relationship = Generalization(general=Relationship, specific=KragsteinPackage_Dependency)
gen_KragsteinPackage_Generalization_Relationship = Generalization(general=Relationship, specific=KragsteinPackage_Generalization)
gen_KragsteinPackage_Realization_Relationship = Generalization(general=Relationship, specific=KragsteinPackage_Realization)
gen_KragsteinPackage_Association_Relationship = Generalization(general=Relationship, specific=KragsteinPackage_Association)
gen_KragsteinPackage_Aggregation_Relationship = Generalization(general=Relationship, specific=KragsteinPackage_Aggregation)
gen_KragsteinPackage_Composition_Relationship = Generalization(general=Relationship, specific=KragsteinPackage_Composition)
gen_KragsteinPackage_Note_Unit = Generalization(general=Unit, specific=KragsteinPackage_Note)
gen_KragsteinPackage_Class_Unit = Generalization(general=Unit, specific=KragsteinPackage_Class)

# Domain Model
domain_model = DomainModel(
    name="KragsteinPackage",
    types={KragsteinPackage_Dependency, KragsteinPackage_Package, KragsteinPackage_Unit, KragsteinPackage_Relationship, KragsteinPackage_Class, KragsteinPackage_Generalization, Relationship, KragsteinPackage_Realization, KragsteinPackage_Association, KragsteinPackage_Aggregation, KragsteinPackage_Composition, KragsteinPackage_Note, Unit, KragsteinPackage_Attribute, KragsteinPackage_Method, KragsteinPackage_ImportedClass, KragsteinPackage_Parameter, KragsteinPackage_Link},
    associations={unit0, target1, source2, attribute5, method7, targetRelationship9, importedClass12, parameter14, targetLink16, source18, target21},
    generalizations={gen_KragsteinPackage_Dependency_Relationship, gen_KragsteinPackage_Generalization_Relationship, gen_KragsteinPackage_Realization_Relationship, gen_KragsteinPackage_Association_Relationship, gen_KragsteinPackage_Aggregation_Relationship, gen_KragsteinPackage_Composition_Relationship, gen_KragsteinPackage_Note_Unit, gen_KragsteinPackage_Class_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)