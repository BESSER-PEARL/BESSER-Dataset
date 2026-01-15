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
library_OCLRoot = Class(name="library::OCLRoot")
library_OCLBoundType = Class(name="library::OCLBoundType")
OCLTypeValue = Class(name="OCLTypeValue")
library_OCLTypeDefinition = Class(name="library::OCLTypeDefinition")
library_OCLTypeBinding = Class(name="library::OCLTypeBinding")
library_OCLElement = Class(name="library::OCLElement")
library_OCLLibraryIteration = Class(name="library::OCLLibraryIteration")
OCLTypedElement = Class(name="OCLTypedElement")
OCLElement = Class(name="OCLElement")
library_OCLLibraryOperation = Class(name="library::OCLLibraryOperation")
library_OCLTypeParameter = Class(name="library::OCLTypeParameter")
library_OCLParameter = Class(name="library::OCLParameter")
library_OCLPackage = Class(name="library::OCLPackage")
library_OCLPackageParent = Class(name="library::OCLPackageParent")
OCLNamedElement = Class(name="OCLNamedElement")
library_OCLLibrary = Class(name="library::OCLLibrary")
OCLRoot = Class(name="OCLRoot")
OCLPackageParent = Class(name="OCLPackageParent")
library_OCLNamedElement = Class(name="library::OCLNamedElement")
library_OCLTypeValue = Class(name="library::OCLTypeValue")
OCLType = Class(name="OCLType")
library_OCLLibraryProperty = Class(name="library::OCLLibraryProperty")
library_OCLType = Class(name="library::OCLType")
library_OCLTypedElement = Class(name="library::OCLTypedElement")
library_OCLTypeReference = Class(name="library::OCLTypeReference")

# library_OCLRoot class attributes and methods

# library_OCLBoundType class attributes and methods

# OCLTypeValue class attributes and methods

# library_OCLTypeDefinition class attributes and methods

# library_OCLTypeBinding class attributes and methods

# library_OCLElement class attributes and methods

# library_OCLLibraryIteration class attributes and methods
library_OCLLibraryIteration_iterator: Property = Property(name="iterator", type=StringType)
library_OCLLibraryIteration_iterators: Property = Property(name="iterators", type=BooleanType)
library_OCLLibraryIteration_class: Property = Property(name="class", type=StringType)
library_OCLLibraryIteration.attributes={library_OCLLibraryIteration_iterator, library_OCLLibraryIteration_class, library_OCLLibraryIteration_iterators}

# OCLTypedElement class attributes and methods

# OCLElement class attributes and methods

# library_OCLLibraryOperation class attributes and methods
library_OCLLibraryOperation_isStatic: Property = Property(name="isStatic", type=BooleanType)
library_OCLLibraryOperation_class: Property = Property(name="class", type=StringType)
library_OCLLibraryOperation.attributes={library_OCLLibraryOperation_class, library_OCLLibraryOperation_isStatic}

# library_OCLTypeParameter class attributes and methods

# library_OCLParameter class attributes and methods

# library_OCLPackage class attributes and methods

# library_OCLPackageParent class attributes and methods

# OCLNamedElement class attributes and methods

# library_OCLLibrary class attributes and methods

# OCLRoot class attributes and methods

# OCLPackageParent class attributes and methods

# library_OCLNamedElement class attributes and methods
library_OCLNamedElement_name: Property = Property(name="name", type=StringType)
library_OCLNamedElement.attributes={library_OCLNamedElement_name}

# library_OCLTypeValue class attributes and methods

# OCLType class attributes and methods

# library_OCLLibraryProperty class attributes and methods
library_OCLLibraryProperty_isStatic: Property = Property(name="isStatic", type=BooleanType)
library_OCLLibraryProperty_class: Property = Property(name="class", type=StringType)
library_OCLLibraryProperty.attributes={library_OCLLibraryProperty_isStatic, library_OCLLibraryProperty_class}

# library_OCLType class attributes and methods

# library_OCLTypedElement class attributes and methods

# library_OCLTypeReference class attributes and methods

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="library_OCLTypeDefinition", type=library_OCLBoundType, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLBoundType", type=library_OCLTypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
typeBinding1: BinaryAssociation = BinaryAssociation(
    name="typeBinding1",
    ends={
        Property(name="library_OCLTypeBinding", type=library_OCLBoundType, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLBoundType2", type=library_OCLTypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameter5: BinaryAssociation = BinaryAssociation(
    name="typeParameter5",
    ends={
        Property(name="library_OCLTypeParameter", type=library_OCLLibraryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLLibraryOperation", type=library_OCLTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter6: BinaryAssociation = BinaryAssociation(
    name="parameter6",
    ends={
        Property(name="library_OCLParameter", type=library_OCLLibraryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLLibraryOperation7", type=library_OCLParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="library_OCLTypeDefinition9", type=library_OCLPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLPackage", type=library_OCLTypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports4: BinaryAssociation = BinaryAssociation(
    name="imports4",
    ends={
        Property(name="library_OCLLibrary", type=library_OCLLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLLibrary3", type=library_OCLLibrary, multiplicity=Multiplicity(0, 9999))
    }
)
typeParameter12: BinaryAssociation = BinaryAssociation(
    name="typeParameter12",
    ends={
        Property(name="library_OCLTypeValue", type=library_OCLTypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLTypeBinding13", type=library_OCLTypeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameter14: BinaryAssociation = BinaryAssociation(
    name="typeParameter14",
    ends={
        Property(name="library_OCLTypeParameter16", type=library_OCLTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLTypeDefinition15", type=library_OCLTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conformsTo17: BinaryAssociation = BinaryAssociation(
    name="conformsTo17",
    ends={
        Property(name="library_OCLTypeValue19", type=library_OCLTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLTypeDefinition18", type=library_OCLTypeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iteration20: BinaryAssociation = BinaryAssociation(
    name="iteration20",
    ends={
        Property(name="library_OCLLibraryIteration", type=library_OCLTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLTypeDefinition21", type=library_OCLLibraryIteration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation22: BinaryAssociation = BinaryAssociation(
    name="operation22",
    ends={
        Property(name="library_OCLLibraryOperation24", type=library_OCLTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLTypeDefinition23", type=library_OCLLibraryOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package10: BinaryAssociation = BinaryAssociation(
    name="package10",
    ends={
        Property(name="library_OCLPackage11", type=library_OCLPackageParent, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLPackageParent", type=library_OCLPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="library_OCLType", type=library_OCLTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLTypeReference", type=library_OCLType, multiplicity=Multiplicity(0, 1))
    }
)
property25: BinaryAssociation = BinaryAssociation(
    name="property25",
    ends={
        Property(name="library_OCLLibraryProperty", type=library_OCLTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLTypeDefinition26", type=library_OCLLibraryProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="library_OCLTypeValue28", type=library_OCLTypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OCLTypedElement", type=library_OCLTypeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_library_OCLBoundType_OCLTypeValue = Generalization(general=OCLTypeValue, specific=library_OCLBoundType)
gen_library_OCLLibraryIteration_OCLTypedElement = Generalization(general=OCLTypedElement, specific=library_OCLLibraryIteration)
gen_library_OCLNamedElement_OCLElement = Generalization(general=OCLElement, specific=library_OCLNamedElement)
gen_library_OCLLibraryOperation_OCLTypedElement = Generalization(general=OCLTypedElement, specific=library_OCLLibraryOperation)
gen_library_OCLPackage_OCLPackageParent = Generalization(general=OCLPackageParent, specific=library_OCLPackage)
gen_library_OCLPackageParent_OCLNamedElement = Generalization(general=OCLNamedElement, specific=library_OCLPackageParent)
gen_library_OCLLibrary_OCLRoot = Generalization(general=OCLRoot, specific=library_OCLLibrary)
gen_library_OCLLibrary_OCLPackageParent = Generalization(general=OCLPackageParent, specific=library_OCLLibrary)
gen_library_OCLTypeBinding_OCLElement = Generalization(general=OCLElement, specific=library_OCLTypeBinding)
gen_library_OCLTypeDefinition_OCLType = Generalization(general=OCLType, specific=library_OCLTypeDefinition)
gen_library_OCLParameter_OCLTypedElement = Generalization(general=OCLTypedElement, specific=library_OCLParameter)
gen_library_OCLLibraryProperty_OCLTypedElement = Generalization(general=OCLTypedElement, specific=library_OCLLibraryProperty)
gen_library_OCLType_OCLNamedElement = Generalization(general=OCLNamedElement, specific=library_OCLType)
gen_library_OCLTypeValue_OCLElement = Generalization(general=OCLElement, specific=library_OCLTypeValue)
gen_library_OCLTypedElement_OCLNamedElement = Generalization(general=OCLNamedElement, specific=library_OCLTypedElement)
gen_library_OCLTypeParameter_OCLType = Generalization(general=OCLType, specific=library_OCLTypeParameter)
gen_library_OCLTypeReference_OCLTypeValue = Generalization(general=OCLTypeValue, specific=library_OCLTypeReference)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_OCLRoot, library_OCLBoundType, OCLTypeValue, library_OCLTypeDefinition, library_OCLTypeBinding, library_OCLElement, library_OCLLibraryIteration, OCLTypedElement, OCLElement, library_OCLLibraryOperation, library_OCLTypeParameter, library_OCLParameter, library_OCLPackage, library_OCLPackageParent, OCLNamedElement, library_OCLLibrary, OCLRoot, OCLPackageParent, library_OCLNamedElement, library_OCLTypeValue, OCLType, library_OCLLibraryProperty, library_OCLType, library_OCLTypedElement, library_OCLTypeReference},
    associations={type0, typeBinding1, typeParameter5, parameter6, type8, imports4, typeParameter12, typeParameter14, conformsTo17, iteration20, operation22, package10, type29, property25, type27},
    generalizations={gen_library_OCLBoundType_OCLTypeValue, gen_library_OCLLibraryIteration_OCLTypedElement, gen_library_OCLNamedElement_OCLElement, gen_library_OCLLibraryOperation_OCLTypedElement, gen_library_OCLPackage_OCLPackageParent, gen_library_OCLPackageParent_OCLNamedElement, gen_library_OCLLibrary_OCLRoot, gen_library_OCLLibrary_OCLPackageParent, gen_library_OCLTypeBinding_OCLElement, gen_library_OCLTypeDefinition_OCLType, gen_library_OCLParameter_OCLTypedElement, gen_library_OCLLibraryProperty_OCLTypedElement, gen_library_OCLType_OCLNamedElement, gen_library_OCLTypeValue_OCLElement, gen_library_OCLTypedElement_OCLNamedElement, gen_library_OCLTypeParameter_OCLType, gen_library_OCLTypeReference_OCLTypeValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)