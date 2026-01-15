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
java_Package = Class(name="java::Package")
Container = Class(name="Container")
java_Class = Class(name="java::Class")
Classifier = Class(name="Classifier")
java_System = Class(name="java::System")
Contained = Class(name="Contained")
Annotable = Class(name="Annotable")
java_GenericBinding = Class(name="java::GenericBinding")
java_Field = Class(name="java::Field")
java_Method = Class(name="java::Method")
java_InterfaceImplementation = Class(name="java::InterfaceImplementation")
java_Interface = Class(name="java::Interface")
java_Classifier = Class(name="java::Classifier", is_abstract=True)
java_Generalization = Class(name="java::Generalization")
java_Contained = Class(name="java::Contained", is_abstract=True)
java_Container = Class(name="java::Container", is_abstract=True)
java_Import = Class(name="java::Import")
java_Statement = Class(name="java::Statement", is_abstract=True)
java_AssertStatement = Class(name="java::AssertStatement")
Statement = Class(name="Statement")
java_GETExpression = Class(name="java::GETExpression")
java_Argument = Class(name="java::Argument")
java_Annotable = Class(name="java::Annotable", is_abstract=True)
java_AnnotationInstance = Class(name="java::AnnotationInstance")
java_Annotation = Class(name="java::Annotation")
java_AnnotationInstanceValue = Class(name="java::AnnotationInstanceValue")
java_AnnotationInstanceParameter = Class(name="java::AnnotationInstanceParameter")

# java_Package class attributes and methods
java_Package_name: Property = Property(name="name", type=StringType)
java_Package.attributes={java_Package_name}

# Container class attributes and methods

# java_Class class attributes and methods
java_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
java_Class_isFinal: Property = Property(name="isFinal", type=BooleanType)
java_Class_isStatic: Property = Property(name="isStatic", type=BooleanType)
java_Class.attributes={java_Class_isFinal, java_Class_isAbstract, java_Class_isStatic}

# Classifier class attributes and methods

# java_System class attributes and methods
java_System_name: Property = Property(name="name", type=StringType)
java_System.attributes={java_System_name}

# Contained class attributes and methods

# Annotable class attributes and methods

# java_GenericBinding class attributes and methods
java_GenericBinding_name: Property = Property(name="name", type=StringType)
java_GenericBinding.attributes={java_GenericBinding_name}

# java_Field class attributes and methods
java_Field_default: Property = Property(name="default", type=StringType)
java_Field_isStatic: Property = Property(name="isStatic", type=BooleanType)
java_Field_isFinal: Property = Property(name="isFinal", type=BooleanType)
java_Field_name: Property = Property(name="name", type=StringType)
java_Field.attributes={java_Field_default, java_Field_isStatic, java_Field_name, java_Field_isFinal}

# java_Method class attributes and methods
java_Method_concurrency: Property = Property(name="concurrency", type=StringType)
java_Method_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
java_Method_isDefault: Property = Property(name="isDefault", type=BooleanType)
java_Method_name: Property = Property(name="name", type=StringType)
java_Method_isFinal: Property = Property(name="isFinal", type=BooleanType)
java_Method_isStatic: Property = Property(name="isStatic", type=BooleanType)
java_Method.attributes={java_Method_isDefault, java_Method_isFinal, java_Method_isAbstract, java_Method_name, java_Method_concurrency, java_Method_isStatic}

# java_InterfaceImplementation class attributes and methods
java_InterfaceImplementation_name: Property = Property(name="name", type=StringType)
java_InterfaceImplementation.attributes={java_InterfaceImplementation_name}

# java_Interface class attributes and methods

# java_Classifier class attributes and methods
java_Classifier_name: Property = Property(name="name", type=StringType)
java_Classifier.attributes={java_Classifier_name}

# java_Generalization class attributes and methods
java_Generalization_name: Property = Property(name="name", type=StringType)
java_Generalization.attributes={java_Generalization_name}

# java_Contained class attributes and methods
java_Contained_visibility: Property = Property(name="visibility", type=StringType)
java_Contained.attributes={java_Contained_visibility}

# java_Container class attributes and methods

# java_Import class attributes and methods
java_Import_name: Property = Property(name="name", type=StringType)
java_Import.attributes={java_Import_name}

# java_Statement class attributes and methods
java_Statement_name: Property = Property(name="name", type=StringType)
java_Statement.attributes={java_Statement_name}

# java_AssertStatement class attributes and methods

# Statement class attributes and methods

# java_GETExpression class attributes and methods
java_GETExpression_rightSide: Property = Property(name="rightSide", type=StringType)
java_GETExpression_leftSide: Property = Property(name="leftSide", type=StringType)
java_GETExpression.attributes={java_GETExpression_rightSide, java_GETExpression_leftSide}

# java_Argument class attributes and methods
java_Argument_name: Property = Property(name="name", type=StringType)
java_Argument_order: Property = Property(name="order", type=IntegerType)
java_Argument.attributes={java_Argument_order, java_Argument_name}

# java_Annotable class attributes and methods

# java_AnnotationInstance class attributes and methods
java_AnnotationInstance_name: Property = Property(name="name", type=StringType)
java_AnnotationInstance.attributes={java_AnnotationInstance_name}

# java_Annotation class attributes and methods

# java_AnnotationInstanceValue class attributes and methods
java_AnnotationInstanceValue_value: Property = Property(name="value", type=StringType)
java_AnnotationInstanceValue_id: Property = Property(name="id", type=IntegerType)
java_AnnotationInstanceValue_name: Property = Property(name="name", type=StringType)
java_AnnotationInstanceValue.attributes={java_AnnotationInstanceValue_value, java_AnnotationInstanceValue_name, java_AnnotationInstanceValue_id}

# java_AnnotationInstanceParameter class attributes and methods
java_AnnotationInstanceParameter_name: Property = Property(name="name", type=StringType)
java_AnnotationInstanceParameter.attributes={java_AnnotationInstanceParameter_name}

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="Package", type=java_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system", type=java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system1: BinaryAssociation = BinaryAssociation(
    name="system1",
    ends={
        Property(name="System", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=java_System, multiplicity=Multiplicity(0, 1))
    }
)
extendedClass3: BinaryAssociation = BinaryAssociation(
    name="extendedClass3",
    ends={
        Property(name="Class", type=java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="extendingClasses", type=java_Class, multiplicity=Multiplicity(0, 1))
    }
)
extendingClasses5: BinaryAssociation = BinaryAssociation(
    name="extendingClasses5",
    ends={
        Property(name="Class6", type=java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedClass", type=java_Class, multiplicity=Multiplicity(0, 1))
    }
)
genericBindings12: BinaryAssociation = BinaryAssociation(
    name="genericBindings12",
    ends={
        Property(name="GenericBinding", type=java_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="usingClassifier", type=java_GenericBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields13: BinaryAssociation = BinaryAssociation(
    name="fields13",
    ends={
        Property(name="Field", type=java_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="containingClassifier", type=java_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods14: BinaryAssociation = BinaryAssociation(
    name="methods14",
    ends={
        Property(name="Method", type=java_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="containingClassifier15", type=java_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceImplementations16: BinaryAssociation = BinaryAssociation(
    name="interfaceImplementations16",
    ends={
        Property(name="InterfaceImplementation", type=java_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="implementer", type=java_InterfaceImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface7: BinaryAssociation = BinaryAssociation(
    name="interface7",
    ends={
        Property(name="java_Interface", type=java_InterfaceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InterfaceImplementation", type=java_Interface, multiplicity=Multiplicity(0, 1))
    }
)
implementer8: BinaryAssociation = BinaryAssociation(
    name="implementer8",
    ends={
        Property(name="Classifier", type=java_InterfaceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaceImplementations", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
general9: BinaryAssociation = BinaryAssociation(
    name="general9",
    ends={
        Property(name="java_Classifier", type=java_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Generalization", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalizator10: BinaryAssociation = BinaryAssociation(
    name="generalizator10",
    ends={
        Property(name="Classifier11", type=java_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
containingClassifier21: BinaryAssociation = BinaryAssociation(
    name="containingClassifier21",
    ends={
        Property(name="Classifier22", type=java_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
imported23: BinaryAssociation = BinaryAssociation(
    name="imported23",
    ends={
        Property(name="java_Classifier24", type=java_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Import", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
importing25: BinaryAssociation = BinaryAssociation(
    name="importing25",
    ends={
        Property(name="Classifier26", type=java_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="imports", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
container27: BinaryAssociation = BinaryAssociation(
    name="container27",
    ends={
        Property(name="Container", type=java_Contained, multiplicity=Multiplicity(1, 1)),
        Property(name="containedElements", type=java_Container, multiplicity=Multiplicity(0, 1))
    }
)
importingClasses28: BinaryAssociation = BinaryAssociation(
    name="importingClasses28",
    ends={
        Property(name="java_Class", type=java_Contained, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Contained", type=java_Class, multiplicity=Multiplicity(0, 9999))
    }
)
generalization17: BinaryAssociation = BinaryAssociation(
    name="generalization17",
    ends={
        Property(name="Generalization", type=java_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="generalizator", type=java_Generalization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports18: BinaryAssociation = BinaryAssociation(
    name="imports18",
    ends={
        Property(name="Import", type=java_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="importing", type=java_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="java_Classifier20", type=java_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Field", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
raisedExceptions34: BinaryAssociation = BinaryAssociation(
    name="raisedExceptions34",
    ends={
        Property(name="java_Classifier36", type=java_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Method35", type=java_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
body37: BinaryAssociation = BinaryAssociation(
    name="body37",
    ends={
        Property(name="Statement", type=java_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method38: BinaryAssociation = BinaryAssociation(
    name="method38",
    ends={
        Property(name="Method39", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=java_Method, multiplicity=Multiplicity(0, 1))
    }
)
assertion40: BinaryAssociation = BinaryAssociation(
    name="assertion40",
    ends={
        Property(name="GETExpression", type=java_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="containerStatement", type=java_GETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType29: BinaryAssociation = BinaryAssociation(
    name="returnType29",
    ends={
        Property(name="java_Classifier30", type=java_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Method", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
arguments31: BinaryAssociation = BinaryAssociation(
    name="arguments31",
    ends={
        Property(name="Argument", type=java_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="usingMethod", type=java_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containingClassifier32: BinaryAssociation = BinaryAssociation(
    name="containingClassifier32",
    ends={
        Property(name="Classifier33", type=java_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
containedElements46: BinaryAssociation = BinaryAssociation(
    name="containedElements46",
    ends={
        Property(name="Contained", type=java_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=java_Contained, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upperBoundings47: BinaryAssociation = BinaryAssociation(
    name="upperBoundings47",
    ends={
        Property(name="java_Classifier48", type=java_GenericBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="java_GenericBinding", type=java_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
lowerBounding49: BinaryAssociation = BinaryAssociation(
    name="lowerBounding49",
    ends={
        Property(name="java_Classifier51", type=java_GenericBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="java_GenericBinding50", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
usingClassifier52: BinaryAssociation = BinaryAssociation(
    name="usingClassifier52",
    ends={
        Property(name="Classifier53", type=java_GenericBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericBindings", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
annotationInstances54: BinaryAssociation = BinaryAssociation(
    name="annotationInstances54",
    ends={
        Property(name="AnnotationInstance", type=java_Annotable, multiplicity=Multiplicity(1, 1)),
        Property(name="annotable", type=java_AnnotationInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerStatement41: BinaryAssociation = BinaryAssociation(
    name="containerStatement41",
    ends={
        Property(name="AssertStatement", type=java_GETExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="assertion", type=java_AssertStatement, multiplicity=Multiplicity(0, 1))
    }
)
type42: BinaryAssociation = BinaryAssociation(
    name="type42",
    ends={
        Property(name="java_Classifier43", type=java_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Argument", type=java_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
usingMethod44: BinaryAssociation = BinaryAssociation(
    name="usingMethod44",
    ends={
        Property(name="Method45", type=java_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=java_Method, multiplicity=Multiplicity(0, 1))
    }
)
values58: BinaryAssociation = BinaryAssociation(
    name="values58",
    ends={
        Property(name="AnnotationInstanceValue", type=java_AnnotationInstanceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=java_AnnotationInstanceValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance59: BinaryAssociation = BinaryAssociation(
    name="instance59",
    ends={
        Property(name="AnnotationInstance60", type=java_AnnotationInstanceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=java_AnnotationInstance, multiplicity=Multiplicity(0, 1))
    }
)
parameter61: BinaryAssociation = BinaryAssociation(
    name="parameter61",
    ends={
        Property(name="AnnotationInstanceParameter62", type=java_AnnotationInstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="values", type=java_AnnotationInstanceParameter, multiplicity=Multiplicity(0, 1))
    }
)
annotation55: BinaryAssociation = BinaryAssociation(
    name="annotation55",
    ends={
        Property(name="java_Annotation", type=java_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationInstance", type=java_Annotation, multiplicity=Multiplicity(0, 1))
    }
)
parameters56: BinaryAssociation = BinaryAssociation(
    name="parameters56",
    ends={
        Property(name="AnnotationInstanceParameter", type=java_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance", type=java_AnnotationInstanceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotable57: BinaryAssociation = BinaryAssociation(
    name="annotable57",
    ends={
        Property(name="Annotable", type=java_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationInstances", type=java_Annotable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_java_Package_Container = Generalization(general=Container, specific=java_Package)
gen_java_Class_Classifier = Generalization(general=Classifier, specific=java_Class)
gen_java_Classifier_Contained = Generalization(general=Contained, specific=java_Classifier)
gen_java_Classifier_Container = Generalization(general=Container, specific=java_Classifier)
gen_java_Classifier_Annotable = Generalization(general=Annotable, specific=java_Classifier)
gen_java_Method_Contained = Generalization(general=Contained, specific=java_Method)
gen_java_Field_Contained = Generalization(general=Contained, specific=java_Field)
gen_java_Field_Annotable = Generalization(general=Annotable, specific=java_Field)
gen_java_AssertStatement_Statement = Generalization(general=Statement, specific=java_AssertStatement)
gen_java_Method_Annotable = Generalization(general=Annotable, specific=java_Method)
gen_java_Interface_Classifier = Generalization(general=Classifier, specific=java_Interface)
gen_java_Interface_Contained = Generalization(general=Contained, specific=java_Interface)
gen_java_Interface_Container = Generalization(general=Container, specific=java_Interface)
gen_java_Annotation_Classifier = Generalization(general=Classifier, specific=java_Annotation)

# Domain Model
domain_model = DomainModel(
    name="java",
    types={java_Package, Container, java_Class, Classifier, java_System, Contained, Annotable, java_GenericBinding, java_Field, java_Method, java_InterfaceImplementation, java_Interface, java_Classifier, java_Generalization, java_Contained, java_Container, java_Import, java_Statement, java_AssertStatement, Statement, java_GETExpression, java_Argument, java_Annotable, java_AnnotationInstance, java_Annotation, java_AnnotationInstanceValue, java_AnnotationInstanceParameter},
    associations={packages0, system1, extendedClass3, extendingClasses5, genericBindings12, fields13, methods14, interfaceImplementations16, interface7, implementer8, general9, generalizator10, containingClassifier21, imported23, importing25, container27, importingClasses28, generalization17, imports18, type19, raisedExceptions34, body37, method38, assertion40, returnType29, arguments31, containingClassifier32, containedElements46, upperBoundings47, lowerBounding49, usingClassifier52, annotationInstances54, containerStatement41, type42, usingMethod44, values58, instance59, parameter61, annotation55, parameters56, annotable57},
    generalizations={gen_java_Package_Container, gen_java_Class_Classifier, gen_java_Classifier_Contained, gen_java_Classifier_Container, gen_java_Classifier_Annotable, gen_java_Method_Contained, gen_java_Field_Contained, gen_java_Field_Annotable, gen_java_AssertStatement_Statement, gen_java_Method_Annotable, gen_java_Interface_Classifier, gen_java_Interface_Contained, gen_java_Interface_Container, gen_java_Annotation_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)