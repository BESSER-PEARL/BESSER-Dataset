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
ETIOType: Enumeration = Enumeration(
    name="ETIOType",
    literals={
            EnumerationLiteral(name="INPUT"),
			EnumerationLiteral(name="OUTPUT")
    }
)

# Classes
ecdarText_ETFile = Class(name="ecdarText::ETFile")
ecdarText_ETImport = Class(name="ecdarText::ETImport")
ecdarText_ETDeclarations = Class(name="ecdarText::ETDeclarations")
ecdarText_ETSpecification = Class(name="ecdarText::ETSpecification")
ecdarText_ETArrayDeclaration = Class(name="ecdarText::ETArrayDeclaration")
ecdarText_ETExpression = Class(name="ecdarText::ETExpression")
ecdarText_ETDeclaration = Class(name="ecdarText::ETDeclaration")
ecdarText_ETVariableDeclaration = Class(name="ecdarText::ETVariableDeclaration")
ETDeclaration = Class(name="ETDeclaration")
ecdarText_ETVariableID = Class(name="ecdarText::ETVariableID")
ecdarText_ETInitialiser = Class(name="ecdarText::ETInitialiser")
ecdarText_ETSingleInitialiser = Class(name="ecdarText::ETSingleInitialiser")
ETInitialiser = Class(name="ETInitialiser")
ecdarText_ETType = Class(name="ecdarText::ETType")
ecdarText_ETTypeModifiers = Class(name="ecdarText::ETTypeModifiers")
ecdarText_ETTypeIdentifier = Class(name="ecdarText::ETTypeIdentifier")
ecdarText_ETTypeDeclaration = Class(name="ecdarText::ETTypeDeclaration")
ecdarText_ETTypeID = Class(name="ecdarText::ETTypeID")
ecdarText_ETIntegerType = Class(name="ecdarText::ETIntegerType")
ETTypeIdentifier = Class(name="ETTypeIdentifier")
ecdarText_ETClockType = Class(name="ecdarText::ETClockType")
ecdarText_ETActionType = Class(name="ecdarText::ETActionType")
ecdarText_ETInputType = Class(name="ecdarText::ETInputType")
ETActionType = Class(name="ETActionType")
ecdarText_ETOutputType = Class(name="ecdarText::ETOutputType")
ecdarText_ETMultiInitialiser = Class(name="ecdarText::ETMultiInitialiser")
ecdarText_ETStructType = Class(name="ecdarText::ETStructType")
ecdarText_ETFieldDeclaration = Class(name="ecdarText::ETFieldDeclaration")
ecdarText_ETFieldID = Class(name="ecdarText::ETFieldID")
ecdarText_ETSpecificationExpression = Class(name="ecdarText::ETSpecificationExpression")
ecdarText_ETSpecificationBinding = Class(name="ecdarText::ETSpecificationBinding")
ETSpecification = Class(name="ETSpecification")
ecdarText_ETSpecificationDefinition = Class(name="ecdarText::ETSpecificationDefinition")
ecdarText_ETSpecificationBody = Class(name="ecdarText::ETSpecificationBody")
ecdarText_ETSpecificationTemplate = Class(name="ecdarText::ETSpecificationTemplate")
ETSpecificationDefinition = Class(name="ETSpecificationDefinition")
ecdarText_ETBooleanType = Class(name="ecdarText::ETBooleanType")
ecdarText_ETScalarType = Class(name="ecdarText::ETScalarType")
ecdarText_ETEdge = Class(name="ecdarText::ETEdge")
ecdarText_ETSelect = Class(name="ecdarText::ETSelect")
ecdarText_ETIO = Class(name="ecdarText::ETIO")
ecdarText_ETParameter = Class(name="ecdarText::ETParameter")
ecdarText_ETLocation = Class(name="ecdarText::ETLocation")
ecdarText_ETSpecificationDisjunctionExpression = Class(name="ecdarText::ETSpecificationDisjunctionExpression")
ETSpecificationExpression = Class(name="ETSpecificationExpression")
ecdarText_ETSpecificationConjunctionExpression = Class(name="ecdarText::ETSpecificationConjunctionExpression")
ecdarText_ETSpecificationCompositionExpression = Class(name="ecdarText::ETSpecificationCompositionExpression")
ecdarText_ETSpecificationReference = Class(name="ecdarText::ETSpecificationReference")
ecdarText_ETSpecificationInstantiation = Class(name="ecdarText::ETSpecificationInstantiation")
ecdarText_ETTypeReference = Class(name="ecdarText::ETTypeReference")
ecdarText_ETImplyExpression = Class(name="ecdarText::ETImplyExpression")
ecdarText_ETLogicOrExpression = Class(name="ecdarText::ETLogicOrExpression")
ecdarText_ETLogicAndExpression = Class(name="ecdarText::ETLogicAndExpression")
ecdarText_ETAssignmentExpression = Class(name="ecdarText::ETAssignmentExpression")
ecdarText_ETAdditionAssignmentExpression = Class(name="ecdarText::ETAdditionAssignmentExpression")
ecdarText_ETForallExpression = Class(name="ecdarText::ETForallExpression")
ETExpression = Class(name="ETExpression")
ecdarText_ETExistsExpression = Class(name="ecdarText::ETExistsExpression")
ecdarText_ETDivisionAssignmentExpression = Class(name="ecdarText::ETDivisionAssignmentExpression")
ecdarText_ETModuloAssignmentExpression = Class(name="ecdarText::ETModuloAssignmentExpression")
ecdarText_ETBitOrAssignmentExpression = Class(name="ecdarText::ETBitOrAssignmentExpression")
ecdarText_ETBitAndAssignmentExpression = Class(name="ecdarText::ETBitAndAssignmentExpression")
ecdarText_ETBitXORAssignmentExpression = Class(name="ecdarText::ETBitXORAssignmentExpression")
ecdarText_ETBitLeftAssignmentExpression = Class(name="ecdarText::ETBitLeftAssignmentExpression")
ecdarText_ETBitRightAssignmentExpression = Class(name="ecdarText::ETBitRightAssignmentExpression")
ecdarText_ETSubtractionAssignmentExpression = Class(name="ecdarText::ETSubtractionAssignmentExpression")
ecdarText_ETMultiplicationAssignmentExpression = Class(name="ecdarText::ETMultiplicationAssignmentExpression")
ecdarText_ETBitOrExpression = Class(name="ecdarText::ETBitOrExpression")
ecdarText_ETBitXORExpression = Class(name="ecdarText::ETBitXORExpression")
ecdarText_ETBitAndExpression = Class(name="ecdarText::ETBitAndExpression")
ecdarText_ETConditionalExpression = Class(name="ecdarText::ETConditionalExpression")
ecdarText_ETUnequalExpression = Class(name="ecdarText::ETUnequalExpression")
ecdarText_ETLessExpression = Class(name="ecdarText::ETLessExpression")
ecdarText_ETEqualExpression = Class(name="ecdarText::ETEqualExpression")
ecdarText_ETGreaterEqualExpression = Class(name="ecdarText::ETGreaterEqualExpression")
ecdarText_ETGreaterExpression = Class(name="ecdarText::ETGreaterExpression")
ecdarText_ETMinExpression = Class(name="ecdarText::ETMinExpression")
ecdarText_ETLessEqualExpression = Class(name="ecdarText::ETLessEqualExpression")
ecdarText_ETMaxExpression = Class(name="ecdarText::ETMaxExpression")
ecdarText_ETBitLeftExpression = Class(name="ecdarText::ETBitLeftExpression")
ecdarText_ETBitRightExpression = Class(name="ecdarText::ETBitRightExpression")
ecdarText_ETAddExpression = Class(name="ecdarText::ETAddExpression")
ecdarText_ETSubtractExpression = Class(name="ecdarText::ETSubtractExpression")
ecdarText_ETDivideExpression = Class(name="ecdarText::ETDivideExpression")
ecdarText_ETModuloExpression = Class(name="ecdarText::ETModuloExpression")
ecdarText_ETPreIncrementExpression = Class(name="ecdarText::ETPreIncrementExpression")
ecdarText_ETPreDecrementExpression = Class(name="ecdarText::ETPreDecrementExpression")
ecdarText_ETLogicNotExpression = Class(name="ecdarText::ETLogicNotExpression")
ecdarText_ETMinusExpression = Class(name="ecdarText::ETMinusExpression")
ecdarText_ETPostIncrementExpression = Class(name="ecdarText::ETPostIncrementExpression")
ecdarText_ETMultiplyExpression = Class(name="ecdarText::ETMultiplyExpression")
ecdarText_ETStructExpression = Class(name="ecdarText::ETStructExpression")
ecdarText_ETArrayExpression = Class(name="ecdarText::ETArrayExpression")
ecdarText_ETReference = Class(name="ecdarText::ETReference")
ecdarText_EObject = Class(name="ecdarText::EObject")
ecdarText_ETBooleanLiteral = Class(name="ecdarText::ETBooleanLiteral")
ecdarText_ETNumberLiteral = Class(name="ecdarText::ETNumberLiteral")
ecdarText_ETPostDecrementExpression = Class(name="ecdarText::ETPostDecrementExpression")

# ecdarText_ETFile class attributes and methods

# ecdarText_ETImport class attributes and methods
ecdarText_ETImport_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
ecdarText_ETImport.attributes={ecdarText_ETImport_importedNamespace}

# ecdarText_ETDeclarations class attributes and methods

# ecdarText_ETSpecification class attributes and methods
ecdarText_ETSpecification_name: Property = Property(name="name", type=StringType)
ecdarText_ETSpecification.attributes={ecdarText_ETSpecification_name}

# ecdarText_ETArrayDeclaration class attributes and methods

# ecdarText_ETExpression class attributes and methods

# ecdarText_ETDeclaration class attributes and methods

# ecdarText_ETVariableDeclaration class attributes and methods

# ETDeclaration class attributes and methods

# ecdarText_ETVariableID class attributes and methods
ecdarText_ETVariableID_name: Property = Property(name="name", type=StringType)
ecdarText_ETVariableID_ioType: Property = Property(name="ioType", type=StringType)
ecdarText_ETVariableID.attributes={ecdarText_ETVariableID_ioType, ecdarText_ETVariableID_name}

# ecdarText_ETInitialiser class attributes and methods

# ecdarText_ETSingleInitialiser class attributes and methods

# ETInitialiser class attributes and methods

# ecdarText_ETType class attributes and methods

# ecdarText_ETTypeModifiers class attributes and methods
ecdarText_ETTypeModifiers_urgent: Property = Property(name="urgent", type=BooleanType)
ecdarText_ETTypeModifiers_meta: Property = Property(name="meta", type=BooleanType)
ecdarText_ETTypeModifiers_const: Property = Property(name="const", type=BooleanType)
ecdarText_ETTypeModifiers.attributes={ecdarText_ETTypeModifiers_urgent, ecdarText_ETTypeModifiers_meta, ecdarText_ETTypeModifiers_const}

# ecdarText_ETTypeIdentifier class attributes and methods

# ecdarText_ETTypeDeclaration class attributes and methods

# ecdarText_ETTypeID class attributes and methods
ecdarText_ETTypeID_name: Property = Property(name="name", type=StringType)
ecdarText_ETTypeID.attributes={ecdarText_ETTypeID_name}

# ecdarText_ETIntegerType class attributes and methods

# ETTypeIdentifier class attributes and methods

# ecdarText_ETClockType class attributes and methods

# ecdarText_ETActionType class attributes and methods

# ecdarText_ETInputType class attributes and methods

# ETActionType class attributes and methods

# ecdarText_ETOutputType class attributes and methods

# ecdarText_ETMultiInitialiser class attributes and methods

# ecdarText_ETStructType class attributes and methods

# ecdarText_ETFieldDeclaration class attributes and methods

# ecdarText_ETFieldID class attributes and methods
ecdarText_ETFieldID_name: Property = Property(name="name", type=StringType)
ecdarText_ETFieldID_ioType: Property = Property(name="ioType", type=StringType)
ecdarText_ETFieldID.attributes={ecdarText_ETFieldID_name, ecdarText_ETFieldID_ioType}

# ecdarText_ETSpecificationExpression class attributes and methods

# ecdarText_ETSpecificationBinding class attributes and methods

# ETSpecification class attributes and methods

# ecdarText_ETSpecificationDefinition class attributes and methods

# ecdarText_ETSpecificationBody class attributes and methods

# ecdarText_ETSpecificationTemplate class attributes and methods

# ETSpecificationDefinition class attributes and methods

# ecdarText_ETBooleanType class attributes and methods

# ecdarText_ETScalarType class attributes and methods

# ecdarText_ETEdge class attributes and methods
ecdarText_ETEdge_controllable: Property = Property(name="controllable", type=BooleanType)
ecdarText_ETEdge.attributes={ecdarText_ETEdge_controllable}

# ecdarText_ETSelect class attributes and methods
ecdarText_ETSelect_name: Property = Property(name="name", type=StringType)
ecdarText_ETSelect.attributes={ecdarText_ETSelect_name}

# ecdarText_ETIO class attributes and methods
ecdarText_ETIO_type: Property = Property(name="type", type=StringType)
ecdarText_ETIO.attributes={ecdarText_ETIO_type}

# ecdarText_ETParameter class attributes and methods
ecdarText_ETParameter_name: Property = Property(name="name", type=StringType)
ecdarText_ETParameter_ioType: Property = Property(name="ioType", type=StringType)
ecdarText_ETParameter.attributes={ecdarText_ETParameter_name, ecdarText_ETParameter_ioType}

# ecdarText_ETLocation class attributes and methods
ecdarText_ETLocation_urgent: Property = Property(name="urgent", type=BooleanType)
ecdarText_ETLocation_universal: Property = Property(name="universal", type=BooleanType)
ecdarText_ETLocation_name: Property = Property(name="name", type=StringType)
ecdarText_ETLocation.attributes={ecdarText_ETLocation_name, ecdarText_ETLocation_universal, ecdarText_ETLocation_urgent}

# ecdarText_ETSpecificationDisjunctionExpression class attributes and methods

# ETSpecificationExpression class attributes and methods

# ecdarText_ETSpecificationConjunctionExpression class attributes and methods

# ecdarText_ETSpecificationCompositionExpression class attributes and methods

# ecdarText_ETSpecificationReference class attributes and methods

# ecdarText_ETSpecificationInstantiation class attributes and methods

# ecdarText_ETTypeReference class attributes and methods

# ecdarText_ETImplyExpression class attributes and methods

# ecdarText_ETLogicOrExpression class attributes and methods

# ecdarText_ETLogicAndExpression class attributes and methods

# ecdarText_ETAssignmentExpression class attributes and methods

# ecdarText_ETAdditionAssignmentExpression class attributes and methods

# ecdarText_ETForallExpression class attributes and methods
ecdarText_ETForallExpression_name: Property = Property(name="name", type=StringType)
ecdarText_ETForallExpression.attributes={ecdarText_ETForallExpression_name}

# ETExpression class attributes and methods

# ecdarText_ETExistsExpression class attributes and methods
ecdarText_ETExistsExpression_name: Property = Property(name="name", type=StringType)
ecdarText_ETExistsExpression.attributes={ecdarText_ETExistsExpression_name}

# ecdarText_ETDivisionAssignmentExpression class attributes and methods

# ecdarText_ETModuloAssignmentExpression class attributes and methods

# ecdarText_ETBitOrAssignmentExpression class attributes and methods

# ecdarText_ETBitAndAssignmentExpression class attributes and methods

# ecdarText_ETBitXORAssignmentExpression class attributes and methods

# ecdarText_ETBitLeftAssignmentExpression class attributes and methods

# ecdarText_ETBitRightAssignmentExpression class attributes and methods

# ecdarText_ETSubtractionAssignmentExpression class attributes and methods

# ecdarText_ETMultiplicationAssignmentExpression class attributes and methods

# ecdarText_ETBitOrExpression class attributes and methods

# ecdarText_ETBitXORExpression class attributes and methods

# ecdarText_ETBitAndExpression class attributes and methods

# ecdarText_ETConditionalExpression class attributes and methods

# ecdarText_ETUnequalExpression class attributes and methods

# ecdarText_ETLessExpression class attributes and methods

# ecdarText_ETEqualExpression class attributes and methods

# ecdarText_ETGreaterEqualExpression class attributes and methods

# ecdarText_ETGreaterExpression class attributes and methods

# ecdarText_ETMinExpression class attributes and methods

# ecdarText_ETLessEqualExpression class attributes and methods

# ecdarText_ETMaxExpression class attributes and methods

# ecdarText_ETBitLeftExpression class attributes and methods

# ecdarText_ETBitRightExpression class attributes and methods

# ecdarText_ETAddExpression class attributes and methods

# ecdarText_ETSubtractExpression class attributes and methods

# ecdarText_ETDivideExpression class attributes and methods

# ecdarText_ETModuloExpression class attributes and methods

# ecdarText_ETPreIncrementExpression class attributes and methods

# ecdarText_ETPreDecrementExpression class attributes and methods

# ecdarText_ETLogicNotExpression class attributes and methods

# ecdarText_ETMinusExpression class attributes and methods

# ecdarText_ETPostIncrementExpression class attributes and methods

# ecdarText_ETMultiplyExpression class attributes and methods

# ecdarText_ETStructExpression class attributes and methods
ecdarText_ETStructExpression_right: Property = Property(name="right", type=StringType)
ecdarText_ETStructExpression.attributes={ecdarText_ETStructExpression_right}

# ecdarText_ETArrayExpression class attributes and methods

# ecdarText_ETReference class attributes and methods

# ecdarText_EObject class attributes and methods

# ecdarText_ETBooleanLiteral class attributes and methods
ecdarText_ETBooleanLiteral_value: Property = Property(name="value", type=StringType)
ecdarText_ETBooleanLiteral.attributes={ecdarText_ETBooleanLiteral_value}

# ecdarText_ETNumberLiteral class attributes and methods
ecdarText_ETNumberLiteral_value: Property = Property(name="value", type=IntegerType)
ecdarText_ETNumberLiteral.attributes={ecdarText_ETNumberLiteral_value}

# ecdarText_ETPostDecrementExpression class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="ecdarText_ETImport", type=ecdarText_ETFile, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETFile", type=ecdarText_ETImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations1: BinaryAssociation = BinaryAssociation(
    name="declarations1",
    ends={
        Property(name="ecdarText_ETDeclarations", type=ecdarText_ETFile, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETFile2", type=ecdarText_ETDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifications3: BinaryAssociation = BinaryAssociation(
    name="specifications3",
    ends={
        Property(name="ecdarText_ETSpecification", type=ecdarText_ETFile, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETFile4", type=ecdarText_ETSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
size5: BinaryAssociation = BinaryAssociation(
    name="size5",
    ends={
        Property(name="ecdarText_ETExpression", type=ecdarText_ETArrayDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETArrayDeclaration", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations6: BinaryAssociation = BinaryAssociation(
    name="declarations6",
    ends={
        Property(name="ecdarText_ETDeclaration", type=ecdarText_ETDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETDeclarations7", type=ecdarText_ETDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="ecdarText_ETType12", type=ecdarText_ETVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETVariableDeclaration", type=ecdarText_ETType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables13: BinaryAssociation = BinaryAssociation(
    name="variables13",
    ends={
        Property(name="ecdarText_ETVariableID", type=ecdarText_ETVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETVariableDeclaration14", type=ecdarText_ETVariableID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimensions15: BinaryAssociation = BinaryAssociation(
    name="dimensions15",
    ends={
        Property(name="ecdarText_ETArrayDeclaration17", type=ecdarText_ETVariableID, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETVariableID16", type=ecdarText_ETArrayDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialiser18: BinaryAssociation = BinaryAssociation(
    name="initialiser18",
    ends={
        Property(name="ecdarText_ETInitialiser", type=ecdarText_ETVariableID, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETVariableID19", type=ecdarText_ETInitialiser, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers8: BinaryAssociation = BinaryAssociation(
    name="modifiers8",
    ends={
        Property(name="ecdarText_ETTypeModifiers", type=ecdarText_ETType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETType", type=ecdarText_ETTypeModifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier9: BinaryAssociation = BinaryAssociation(
    name="identifier9",
    ends={
        Property(name="ecdarText_ETTypeIdentifier", type=ecdarText_ETType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETType10", type=ecdarText_ETTypeIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseType24: BinaryAssociation = BinaryAssociation(
    name="baseType24",
    ends={
        Property(name="ecdarText_ETType25", type=ecdarText_ETTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETTypeDeclaration", type=ecdarText_ETType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types26: BinaryAssociation = BinaryAssociation(
    name="types26",
    ends={
        Property(name="ecdarText_ETTypeID", type=ecdarText_ETTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETTypeDeclaration27", type=ecdarText_ETTypeID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimensions28: BinaryAssociation = BinaryAssociation(
    name="dimensions28",
    ends={
        Property(name="ecdarText_ETArrayDeclaration30", type=ecdarText_ETTypeID, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETTypeID29", type=ecdarText_ETArrayDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
min31: BinaryAssociation = BinaryAssociation(
    name="min31",
    ends={
        Property(name="ecdarText_ETExpression32", type=ecdarText_ETIntegerType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETIntegerType", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
max33: BinaryAssociation = BinaryAssociation(
    name="max33",
    ends={
        Property(name="ecdarText_ETExpression35", type=ecdarText_ETIntegerType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETIntegerType34", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression20: BinaryAssociation = BinaryAssociation(
    name="expression20",
    ends={
        Property(name="ecdarText_ETExpression21", type=ecdarText_ETSingleInitialiser, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSingleInitialiser", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialisers22: BinaryAssociation = BinaryAssociation(
    name="initialisers22",
    ends={
        Property(name="ecdarText_ETInitialiser23", type=ecdarText_ETMultiInitialiser, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETMultiInitialiser", type=ecdarText_ETInitialiser, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations38: BinaryAssociation = BinaryAssociation(
    name="declarations38",
    ends={
        Property(name="ecdarText_ETFieldDeclaration", type=ecdarText_ETStructType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETStructType", type=ecdarText_ETFieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type39: BinaryAssociation = BinaryAssociation(
    name="type39",
    ends={
        Property(name="ecdarText_ETType41", type=ecdarText_ETFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETFieldDeclaration40", type=ecdarText_ETType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields42: BinaryAssociation = BinaryAssociation(
    name="fields42",
    ends={
        Property(name="ecdarText_ETFieldID", type=ecdarText_ETFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETFieldDeclaration43", type=ecdarText_ETFieldID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimensions44: BinaryAssociation = BinaryAssociation(
    name="dimensions44",
    ends={
        Property(name="ecdarText_ETArrayDeclaration46", type=ecdarText_ETFieldID, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETFieldID45", type=ecdarText_ETArrayDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression47: BinaryAssociation = BinaryAssociation(
    name="expression47",
    ends={
        Property(name="ecdarText_ETSpecificationExpression", type=ecdarText_ETSpecificationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationBinding", type=ecdarText_ETSpecificationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body48: BinaryAssociation = BinaryAssociation(
    name="body48",
    ends={
        Property(name="ecdarText_ETSpecificationBody", type=ecdarText_ETSpecificationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationDefinition", type=ecdarText_ETSpecificationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size36: BinaryAssociation = BinaryAssociation(
    name="size36",
    ends={
        Property(name="ecdarText_ETExpression37", type=ecdarText_ETScalarType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETScalarType", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type58: BinaryAssociation = BinaryAssociation(
    name="type58",
    ends={
        Property(name="ecdarText_ETParameter59", type=ecdarText_ETType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ecdarText_ETType60", type=ecdarText_ETParameter, multiplicity=Multiplicity(1, 1))
    }
)
dimensions61: BinaryAssociation = BinaryAssociation(
    name="dimensions61",
    ends={
        Property(name="ecdarText_ETArrayDeclaration63", type=ecdarText_ETParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETParameter62", type=ecdarText_ETArrayDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invariants64: BinaryAssociation = BinaryAssociation(
    name="invariants64",
    ends={
        Property(name="ecdarText_ETExpression66", type=ecdarText_ETLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLocation65", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges67: BinaryAssociation = BinaryAssociation(
    name="edges67",
    ends={
        Property(name="ecdarText_ETEdge", type=ecdarText_ETLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLocation68", type=ecdarText_ETEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selects69: BinaryAssociation = BinaryAssociation(
    name="selects69",
    ends={
        Property(name="ecdarText_ETSelect", type=ecdarText_ETEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETEdge70", type=ecdarText_ETSelect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
io71: BinaryAssociation = BinaryAssociation(
    name="io71",
    ends={
        Property(name="ecdarText_ETIO", type=ecdarText_ETEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETEdge72", type=ecdarText_ETIO, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard73: BinaryAssociation = BinaryAssociation(
    name="guard73",
    ends={
        Property(name="ecdarText_ETExpression75", type=ecdarText_ETEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETEdge74", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target76: BinaryAssociation = BinaryAssociation(
    name="target76",
    ends={
        Property(name="ecdarText_ETLocation78", type=ecdarText_ETEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETEdge77", type=ecdarText_ETLocation, multiplicity=Multiplicity(0, 1))
    }
)
updates79: BinaryAssociation = BinaryAssociation(
    name="updates79",
    ends={
        Property(name="ecdarText_ETExpression81", type=ecdarText_ETEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETEdge80", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression82: BinaryAssociation = BinaryAssociation(
    name="expression82",
    ends={
        Property(name="ecdarText_ETExpression84", type=ecdarText_ETIO, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETIO83", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters49: BinaryAssociation = BinaryAssociation(
    name="parameters49",
    ends={
        Property(name="ecdarText_ETParameter", type=ecdarText_ETSpecificationTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationTemplate", type=ecdarText_ETParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations50: BinaryAssociation = BinaryAssociation(
    name="declarations50",
    ends={
        Property(name="ecdarText_ETDeclarations52", type=ecdarText_ETSpecificationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationBody51", type=ecdarText_ETDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialLocation53: BinaryAssociation = BinaryAssociation(
    name="initialLocation53",
    ends={
        Property(name="ecdarText_ETLocation", type=ecdarText_ETSpecificationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationBody54", type=ecdarText_ETLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
locations55: BinaryAssociation = BinaryAssociation(
    name="locations55",
    ends={
        Property(name="ecdarText_ETLocation57", type=ecdarText_ETSpecificationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationBody56", type=ecdarText_ETLocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left90: BinaryAssociation = BinaryAssociation(
    name="left90",
    ends={
        Property(name="ecdarText_ETSpecificationExpression91", type=ecdarText_ETSpecificationDisjunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationDisjunctionExpression", type=ecdarText_ETSpecificationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right92: BinaryAssociation = BinaryAssociation(
    name="right92",
    ends={
        Property(name="ecdarText_ETSpecificationExpression94", type=ecdarText_ETSpecificationDisjunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationDisjunctionExpression93", type=ecdarText_ETSpecificationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left95: BinaryAssociation = BinaryAssociation(
    name="left95",
    ends={
        Property(name="ecdarText_ETSpecificationExpression96", type=ecdarText_ETSpecificationConjunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationConjunctionExpression", type=ecdarText_ETSpecificationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right97: BinaryAssociation = BinaryAssociation(
    name="right97",
    ends={
        Property(name="ecdarText_ETSpecificationExpression99", type=ecdarText_ETSpecificationConjunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationConjunctionExpression98", type=ecdarText_ETSpecificationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left100: BinaryAssociation = BinaryAssociation(
    name="left100",
    ends={
        Property(name="ecdarText_ETSpecificationExpression101", type=ecdarText_ETSpecificationCompositionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationCompositionExpression", type=ecdarText_ETSpecificationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right102: BinaryAssociation = BinaryAssociation(
    name="right102",
    ends={
        Property(name="ecdarText_ETSpecificationExpression104", type=ecdarText_ETSpecificationCompositionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationCompositionExpression103", type=ecdarText_ETSpecificationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification105: BinaryAssociation = BinaryAssociation(
    name="specification105",
    ends={
        Property(name="ecdarText_ETSpecification106", type=ecdarText_ETSpecificationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationReference", type=ecdarText_ETSpecification, multiplicity=Multiplicity(0, 1))
    }
)
template107: BinaryAssociation = BinaryAssociation(
    name="template107",
    ends={
        Property(name="ecdarText_ETSpecificationTemplate108", type=ecdarText_ETSpecificationInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationInstantiation", type=ecdarText_ETSpecificationTemplate, multiplicity=Multiplicity(0, 1))
    }
)
type85: BinaryAssociation = BinaryAssociation(
    name="type85",
    ends={
        Property(name="ecdarText_ETType87", type=ecdarText_ETSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSelect86", type=ecdarText_ETType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type117: BinaryAssociation = BinaryAssociation(
    name="type117",
    ends={
        Property(name="ecdarText_ETExistsExpression", type=ecdarText_ETType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ecdarText_ETType118", type=ecdarText_ETExistsExpression, multiplicity=Multiplicity(1, 1))
    }
)
target88: BinaryAssociation = BinaryAssociation(
    name="target88",
    ends={
        Property(name="ecdarText_ETTypeID89", type=ecdarText_ETTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETTypeReference", type=ecdarText_ETTypeID, multiplicity=Multiplicity(0, 1))
    }
)
expression119: BinaryAssociation = BinaryAssociation(
    name="expression119",
    ends={
        Property(name="ecdarText_ETExpression121", type=ecdarText_ETExistsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETExistsExpression120", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left122: BinaryAssociation = BinaryAssociation(
    name="left122",
    ends={
        Property(name="ecdarText_ETExpression123", type=ecdarText_ETImplyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETImplyExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right124: BinaryAssociation = BinaryAssociation(
    name="right124",
    ends={
        Property(name="ecdarText_ETExpression126", type=ecdarText_ETImplyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETImplyExpression125", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left127: BinaryAssociation = BinaryAssociation(
    name="left127",
    ends={
        Property(name="ecdarText_ETExpression128", type=ecdarText_ETLogicOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLogicOrExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right129: BinaryAssociation = BinaryAssociation(
    name="right129",
    ends={
        Property(name="ecdarText_ETExpression131", type=ecdarText_ETLogicOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLogicOrExpression130", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left132: BinaryAssociation = BinaryAssociation(
    name="left132",
    ends={
        Property(name="ecdarText_ETExpression133", type=ecdarText_ETLogicAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLogicAndExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right134: BinaryAssociation = BinaryAssociation(
    name="right134",
    ends={
        Property(name="ecdarText_ETExpression136", type=ecdarText_ETLogicAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLogicAndExpression135", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left137: BinaryAssociation = BinaryAssociation(
    name="left137",
    ends={
        Property(name="ecdarText_ETExpression138", type=ecdarText_ETAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right139: BinaryAssociation = BinaryAssociation(
    name="right139",
    ends={
        Property(name="ecdarText_ETExpression141", type=ecdarText_ETAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETAssignmentExpression140", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left142: BinaryAssociation = BinaryAssociation(
    name="left142",
    ends={
        Property(name="ecdarText_ETExpression143", type=ecdarText_ETAdditionAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETAdditionAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right144: BinaryAssociation = BinaryAssociation(
    name="right144",
    ends={
        Property(name="ecdarText_ETExpression146", type=ecdarText_ETAdditionAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETAdditionAssignmentExpression145", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments109: BinaryAssociation = BinaryAssociation(
    name="arguments109",
    ends={
        Property(name="ecdarText_ETExpression111", type=ecdarText_ETSpecificationInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSpecificationInstantiation110", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type112: BinaryAssociation = BinaryAssociation(
    name="type112",
    ends={
        Property(name="ecdarText_ETType113", type=ecdarText_ETForallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETForallExpression", type=ecdarText_ETType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression114: BinaryAssociation = BinaryAssociation(
    name="expression114",
    ends={
        Property(name="ecdarText_ETExpression116", type=ecdarText_ETForallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETForallExpression115", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right154: BinaryAssociation = BinaryAssociation(
    name="right154",
    ends={
        Property(name="ecdarText_ETExpression156", type=ecdarText_ETMultiplicationAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETMultiplicationAssignmentExpression155", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left157: BinaryAssociation = BinaryAssociation(
    name="left157",
    ends={
        Property(name="ecdarText_ETExpression158", type=ecdarText_ETDivisionAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETDivisionAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right159: BinaryAssociation = BinaryAssociation(
    name="right159",
    ends={
        Property(name="ecdarText_ETExpression161", type=ecdarText_ETDivisionAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETDivisionAssignmentExpression160", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left162: BinaryAssociation = BinaryAssociation(
    name="left162",
    ends={
        Property(name="ecdarText_ETExpression163", type=ecdarText_ETModuloAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETModuloAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right164: BinaryAssociation = BinaryAssociation(
    name="right164",
    ends={
        Property(name="ecdarText_ETExpression166", type=ecdarText_ETModuloAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETModuloAssignmentExpression165", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left167: BinaryAssociation = BinaryAssociation(
    name="left167",
    ends={
        Property(name="ecdarText_ETExpression168", type=ecdarText_ETBitOrAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitOrAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right169: BinaryAssociation = BinaryAssociation(
    name="right169",
    ends={
        Property(name="ecdarText_ETExpression171", type=ecdarText_ETBitOrAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitOrAssignmentExpression170", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left172: BinaryAssociation = BinaryAssociation(
    name="left172",
    ends={
        Property(name="ecdarText_ETExpression173", type=ecdarText_ETBitAndAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitAndAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right174: BinaryAssociation = BinaryAssociation(
    name="right174",
    ends={
        Property(name="ecdarText_ETExpression176", type=ecdarText_ETBitAndAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitAndAssignmentExpression175", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left177: BinaryAssociation = BinaryAssociation(
    name="left177",
    ends={
        Property(name="ecdarText_ETExpression178", type=ecdarText_ETBitXORAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitXORAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right179: BinaryAssociation = BinaryAssociation(
    name="right179",
    ends={
        Property(name="ecdarText_ETExpression181", type=ecdarText_ETBitXORAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitXORAssignmentExpression180", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left182: BinaryAssociation = BinaryAssociation(
    name="left182",
    ends={
        Property(name="ecdarText_ETExpression183", type=ecdarText_ETBitLeftAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitLeftAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right184: BinaryAssociation = BinaryAssociation(
    name="right184",
    ends={
        Property(name="ecdarText_ETExpression186", type=ecdarText_ETBitLeftAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitLeftAssignmentExpression185", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left147: BinaryAssociation = BinaryAssociation(
    name="left147",
    ends={
        Property(name="ecdarText_ETExpression148", type=ecdarText_ETSubtractionAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSubtractionAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right149: BinaryAssociation = BinaryAssociation(
    name="right149",
    ends={
        Property(name="ecdarText_ETExpression151", type=ecdarText_ETSubtractionAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSubtractionAssignmentExpression150", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left152: BinaryAssociation = BinaryAssociation(
    name="left152",
    ends={
        Property(name="ecdarText_ETExpression153", type=ecdarText_ETMultiplicationAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETMultiplicationAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else197: BinaryAssociation = BinaryAssociation(
    name="else197",
    ends={
        Property(name="ecdarText_ETExpression199", type=ecdarText_ETConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETConditionalExpression198", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left200: BinaryAssociation = BinaryAssociation(
    name="left200",
    ends={
        Property(name="ecdarText_ETExpression201", type=ecdarText_ETBitOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitOrExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right202: BinaryAssociation = BinaryAssociation(
    name="right202",
    ends={
        Property(name="ecdarText_ETExpression204", type=ecdarText_ETBitOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitOrExpression203", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left205: BinaryAssociation = BinaryAssociation(
    name="left205",
    ends={
        Property(name="ecdarText_ETExpression206", type=ecdarText_ETBitXORExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitXORExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right207: BinaryAssociation = BinaryAssociation(
    name="right207",
    ends={
        Property(name="ecdarText_ETExpression209", type=ecdarText_ETBitXORExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitXORExpression208", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left210: BinaryAssociation = BinaryAssociation(
    name="left210",
    ends={
        Property(name="ecdarText_ETExpression211", type=ecdarText_ETBitAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitAndExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left187: BinaryAssociation = BinaryAssociation(
    name="left187",
    ends={
        Property(name="ecdarText_ETExpression188", type=ecdarText_ETBitRightAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitRightAssignmentExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right189: BinaryAssociation = BinaryAssociation(
    name="right189",
    ends={
        Property(name="ecdarText_ETExpression191", type=ecdarText_ETBitRightAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitRightAssignmentExpression190", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition192: BinaryAssociation = BinaryAssociation(
    name="condition192",
    ends={
        Property(name="ecdarText_ETExpression193", type=ecdarText_ETConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETConditionalExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then194: BinaryAssociation = BinaryAssociation(
    name="then194",
    ends={
        Property(name="ecdarText_ETExpression196", type=ecdarText_ETConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETConditionalExpression195", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right217: BinaryAssociation = BinaryAssociation(
    name="right217",
    ends={
        Property(name="ecdarText_ETExpression219", type=ecdarText_ETEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETEqualExpression218", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left220: BinaryAssociation = BinaryAssociation(
    name="left220",
    ends={
        Property(name="ecdarText_ETExpression221", type=ecdarText_ETUnequalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETUnequalExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right222: BinaryAssociation = BinaryAssociation(
    name="right222",
    ends={
        Property(name="ecdarText_ETExpression224", type=ecdarText_ETUnequalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETUnequalExpression223", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left225: BinaryAssociation = BinaryAssociation(
    name="left225",
    ends={
        Property(name="ecdarText_ETExpression226", type=ecdarText_ETLessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLessExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right227: BinaryAssociation = BinaryAssociation(
    name="right227",
    ends={
        Property(name="ecdarText_ETExpression229", type=ecdarText_ETLessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLessExpression228", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right212: BinaryAssociation = BinaryAssociation(
    name="right212",
    ends={
        Property(name="ecdarText_ETExpression214", type=ecdarText_ETBitAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitAndExpression213", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left215: BinaryAssociation = BinaryAssociation(
    name="left215",
    ends={
        Property(name="ecdarText_ETExpression216", type=ecdarText_ETEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETEqualExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right232: BinaryAssociation = BinaryAssociation(
    name="right232",
    ends={
        Property(name="ecdarText_ETExpression234", type=ecdarText_ETLessEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLessEqualExpression233", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left235: BinaryAssociation = BinaryAssociation(
    name="left235",
    ends={
        Property(name="ecdarText_ETExpression236", type=ecdarText_ETGreaterEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETGreaterEqualExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right237: BinaryAssociation = BinaryAssociation(
    name="right237",
    ends={
        Property(name="ecdarText_ETExpression239", type=ecdarText_ETGreaterEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETGreaterEqualExpression238", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left240: BinaryAssociation = BinaryAssociation(
    name="left240",
    ends={
        Property(name="ecdarText_ETExpression241", type=ecdarText_ETGreaterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETGreaterExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right242: BinaryAssociation = BinaryAssociation(
    name="right242",
    ends={
        Property(name="ecdarText_ETExpression244", type=ecdarText_ETGreaterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETGreaterExpression243", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left230: BinaryAssociation = BinaryAssociation(
    name="left230",
    ends={
        Property(name="ecdarText_ETExpression231", type=ecdarText_ETLessEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLessEqualExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left250: BinaryAssociation = BinaryAssociation(
    name="left250",
    ends={
        Property(name="ecdarText_ETExpression251", type=ecdarText_ETMaxExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETMaxExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right252: BinaryAssociation = BinaryAssociation(
    name="right252",
    ends={
        Property(name="ecdarText_ETExpression254", type=ecdarText_ETMaxExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETMaxExpression253", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left255: BinaryAssociation = BinaryAssociation(
    name="left255",
    ends={
        Property(name="ecdarText_ETExpression256", type=ecdarText_ETBitLeftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitLeftExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right257: BinaryAssociation = BinaryAssociation(
    name="right257",
    ends={
        Property(name="ecdarText_ETExpression259", type=ecdarText_ETBitLeftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitLeftExpression258", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left245: BinaryAssociation = BinaryAssociation(
    name="left245",
    ends={
        Property(name="ecdarText_ETExpression246", type=ecdarText_ETMinExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETMinExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right247: BinaryAssociation = BinaryAssociation(
    name="right247",
    ends={
        Property(name="ecdarText_ETExpression249", type=ecdarText_ETMinExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETMinExpression248", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left260: BinaryAssociation = BinaryAssociation(
    name="left260",
    ends={
        Property(name="ecdarText_ETExpression261", type=ecdarText_ETBitRightExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitRightExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right262: BinaryAssociation = BinaryAssociation(
    name="right262",
    ends={
        Property(name="ecdarText_ETExpression264", type=ecdarText_ETBitRightExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETBitRightExpression263", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left265: BinaryAssociation = BinaryAssociation(
    name="left265",
    ends={
        Property(name="ecdarText_ETExpression266", type=ecdarText_ETAddExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETAddExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right267: BinaryAssociation = BinaryAssociation(
    name="right267",
    ends={
        Property(name="ecdarText_ETExpression269", type=ecdarText_ETAddExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETAddExpression268", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left270: BinaryAssociation = BinaryAssociation(
    name="left270",
    ends={
        Property(name="ecdarText_ETExpression271", type=ecdarText_ETSubtractExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSubtractExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right277: BinaryAssociation = BinaryAssociation(
    name="right277",
    ends={
        Property(name="ecdarText_ETExpression279", type=ecdarText_ETMultiplyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETMultiplyExpression278", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left280: BinaryAssociation = BinaryAssociation(
    name="left280",
    ends={
        Property(name="ecdarText_ETExpression281", type=ecdarText_ETDivideExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETDivideExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right282: BinaryAssociation = BinaryAssociation(
    name="right282",
    ends={
        Property(name="ecdarText_ETExpression284", type=ecdarText_ETDivideExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETDivideExpression283", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left285: BinaryAssociation = BinaryAssociation(
    name="left285",
    ends={
        Property(name="ecdarText_ETExpression286", type=ecdarText_ETModuloExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETModuloExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right287: BinaryAssociation = BinaryAssociation(
    name="right287",
    ends={
        Property(name="ecdarText_ETExpression289", type=ecdarText_ETModuloExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETModuloExpression288", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression290: BinaryAssociation = BinaryAssociation(
    name="expression290",
    ends={
        Property(name="ecdarText_ETExpression291", type=ecdarText_ETPreIncrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETPreIncrementExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression292: BinaryAssociation = BinaryAssociation(
    name="expression292",
    ends={
        Property(name="ecdarText_ETExpression293", type=ecdarText_ETPreDecrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETPreDecrementExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression294: BinaryAssociation = BinaryAssociation(
    name="expression294",
    ends={
        Property(name="ecdarText_ETExpression295", type=ecdarText_ETLogicNotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETLogicNotExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression296: BinaryAssociation = BinaryAssociation(
    name="expression296",
    ends={
        Property(name="ecdarText_ETExpression297", type=ecdarText_ETMinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETMinusExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression298: BinaryAssociation = BinaryAssociation(
    name="expression298",
    ends={
        Property(name="ecdarText_ETExpression299", type=ecdarText_ETPostIncrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETPostIncrementExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right272: BinaryAssociation = BinaryAssociation(
    name="right272",
    ends={
        Property(name="ecdarText_ETExpression274", type=ecdarText_ETSubtractExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETSubtractExpression273", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left275: BinaryAssociation = BinaryAssociation(
    name="left275",
    ends={
        Property(name="ecdarText_ETExpression276", type=ecdarText_ETMultiplyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETMultiplyExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left302: BinaryAssociation = BinaryAssociation(
    name="left302",
    ends={
        Property(name="ecdarText_ETExpression303", type=ecdarText_ETStructExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETStructExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left304: BinaryAssociation = BinaryAssociation(
    name="left304",
    ends={
        Property(name="ecdarText_ETExpression305", type=ecdarText_ETArrayExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETArrayExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right306: BinaryAssociation = BinaryAssociation(
    name="right306",
    ends={
        Property(name="ecdarText_ETExpression308", type=ecdarText_ETArrayExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETArrayExpression307", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target309: BinaryAssociation = BinaryAssociation(
    name="target309",
    ends={
        Property(name="ecdarText_EObject", type=ecdarText_ETReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETReference", type=ecdarText_EObject, multiplicity=Multiplicity(0, 1))
    }
)
expression300: BinaryAssociation = BinaryAssociation(
    name="expression300",
    ends={
        Property(name="ecdarText_ETExpression301", type=ecdarText_ETPostDecrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ecdarText_ETPostDecrementExpression", type=ecdarText_ETExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_ecdarText_ETVariableDeclaration_ETDeclaration = Generalization(general=ETDeclaration, specific=ecdarText_ETVariableDeclaration)
gen_ecdarText_ETSingleInitialiser_ETInitialiser = Generalization(general=ETInitialiser, specific=ecdarText_ETSingleInitialiser)
gen_ecdarText_ETTypeDeclaration_ETDeclaration = Generalization(general=ETDeclaration, specific=ecdarText_ETTypeDeclaration)
gen_ecdarText_ETIntegerType_ETTypeIdentifier = Generalization(general=ETTypeIdentifier, specific=ecdarText_ETIntegerType)
gen_ecdarText_ETClockType_ETTypeIdentifier = Generalization(general=ETTypeIdentifier, specific=ecdarText_ETClockType)
gen_ecdarText_ETActionType_ETTypeIdentifier = Generalization(general=ETTypeIdentifier, specific=ecdarText_ETActionType)
gen_ecdarText_ETInputType_ETActionType = Generalization(general=ETActionType, specific=ecdarText_ETInputType)
gen_ecdarText_ETOutputType_ETActionType = Generalization(general=ETActionType, specific=ecdarText_ETOutputType)
gen_ecdarText_ETMultiInitialiser_ETInitialiser = Generalization(general=ETInitialiser, specific=ecdarText_ETMultiInitialiser)
gen_ecdarText_ETStructType_ETTypeIdentifier = Generalization(general=ETTypeIdentifier, specific=ecdarText_ETStructType)
gen_ecdarText_ETSpecificationBinding_ETSpecification = Generalization(general=ETSpecification, specific=ecdarText_ETSpecificationBinding)
gen_ecdarText_ETSpecificationDefinition_ETSpecification = Generalization(general=ETSpecification, specific=ecdarText_ETSpecificationDefinition)
gen_ecdarText_ETSpecificationTemplate_ETSpecificationDefinition = Generalization(general=ETSpecificationDefinition, specific=ecdarText_ETSpecificationTemplate)
gen_ecdarText_ETBooleanType_ETTypeIdentifier = Generalization(general=ETTypeIdentifier, specific=ecdarText_ETBooleanType)
gen_ecdarText_ETScalarType_ETTypeIdentifier = Generalization(general=ETTypeIdentifier, specific=ecdarText_ETScalarType)
gen_ecdarText_ETSpecificationDisjunctionExpression_ETSpecificationExpression = Generalization(general=ETSpecificationExpression, specific=ecdarText_ETSpecificationDisjunctionExpression)
gen_ecdarText_ETSpecificationConjunctionExpression_ETSpecificationExpression = Generalization(general=ETSpecificationExpression, specific=ecdarText_ETSpecificationConjunctionExpression)
gen_ecdarText_ETSpecificationCompositionExpression_ETSpecificationExpression = Generalization(general=ETSpecificationExpression, specific=ecdarText_ETSpecificationCompositionExpression)
gen_ecdarText_ETSpecificationReference_ETSpecificationExpression = Generalization(general=ETSpecificationExpression, specific=ecdarText_ETSpecificationReference)
gen_ecdarText_ETSpecificationInstantiation_ETSpecificationExpression = Generalization(general=ETSpecificationExpression, specific=ecdarText_ETSpecificationInstantiation)
gen_ecdarText_ETTypeReference_ETTypeIdentifier = Generalization(general=ETTypeIdentifier, specific=ecdarText_ETTypeReference)
gen_ecdarText_ETImplyExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETImplyExpression)
gen_ecdarText_ETLogicOrExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETLogicOrExpression)
gen_ecdarText_ETLogicAndExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETLogicAndExpression)
gen_ecdarText_ETAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETAssignmentExpression)
gen_ecdarText_ETAdditionAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETAdditionAssignmentExpression)
gen_ecdarText_ETForallExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETForallExpression)
gen_ecdarText_ETExistsExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETExistsExpression)
gen_ecdarText_ETDivisionAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETDivisionAssignmentExpression)
gen_ecdarText_ETModuloAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETModuloAssignmentExpression)
gen_ecdarText_ETBitOrAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBitOrAssignmentExpression)
gen_ecdarText_ETBitAndAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBitAndAssignmentExpression)
gen_ecdarText_ETBitXORAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBitXORAssignmentExpression)
gen_ecdarText_ETBitLeftAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBitLeftAssignmentExpression)
gen_ecdarText_ETBitRightAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBitRightAssignmentExpression)
gen_ecdarText_ETSubtractionAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETSubtractionAssignmentExpression)
gen_ecdarText_ETMultiplicationAssignmentExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETMultiplicationAssignmentExpression)
gen_ecdarText_ETBitOrExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBitOrExpression)
gen_ecdarText_ETBitXORExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBitXORExpression)
gen_ecdarText_ETBitAndExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBitAndExpression)
gen_ecdarText_ETConditionalExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETConditionalExpression)
gen_ecdarText_ETUnequalExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETUnequalExpression)
gen_ecdarText_ETLessExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETLessExpression)
gen_ecdarText_ETEqualExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETEqualExpression)
gen_ecdarText_ETGreaterEqualExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETGreaterEqualExpression)
gen_ecdarText_ETGreaterExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETGreaterExpression)
gen_ecdarText_ETMinExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETMinExpression)
gen_ecdarText_ETLessEqualExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETLessEqualExpression)
gen_ecdarText_ETMaxExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETMaxExpression)
gen_ecdarText_ETBitLeftExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBitLeftExpression)
gen_ecdarText_ETAddExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETAddExpression)
gen_ecdarText_ETSubtractExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETSubtractExpression)
gen_ecdarText_ETBitRightExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBitRightExpression)
gen_ecdarText_ETDivideExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETDivideExpression)
gen_ecdarText_ETModuloExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETModuloExpression)
gen_ecdarText_ETPreIncrementExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETPreIncrementExpression)
gen_ecdarText_ETPreDecrementExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETPreDecrementExpression)
gen_ecdarText_ETLogicNotExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETLogicNotExpression)
gen_ecdarText_ETMinusExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETMinusExpression)
gen_ecdarText_ETPostIncrementExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETPostIncrementExpression)
gen_ecdarText_ETMultiplyExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETMultiplyExpression)
gen_ecdarText_ETStructExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETStructExpression)
gen_ecdarText_ETArrayExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETArrayExpression)
gen_ecdarText_ETReference_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETReference)
gen_ecdarText_ETBooleanLiteral_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETBooleanLiteral)
gen_ecdarText_ETNumberLiteral_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETNumberLiteral)
gen_ecdarText_ETPostDecrementExpression_ETExpression = Generalization(general=ETExpression, specific=ecdarText_ETPostDecrementExpression)

# Domain Model
domain_model = DomainModel(
    name="ecdarText",
    types={ecdarText_ETFile, ecdarText_ETImport, ecdarText_ETDeclarations, ecdarText_ETSpecification, ecdarText_ETArrayDeclaration, ecdarText_ETExpression, ecdarText_ETDeclaration, ecdarText_ETVariableDeclaration, ETDeclaration, ecdarText_ETVariableID, ecdarText_ETInitialiser, ecdarText_ETSingleInitialiser, ETInitialiser, ecdarText_ETType, ecdarText_ETTypeModifiers, ecdarText_ETTypeIdentifier, ecdarText_ETTypeDeclaration, ecdarText_ETTypeID, ecdarText_ETIntegerType, ETTypeIdentifier, ecdarText_ETClockType, ecdarText_ETActionType, ecdarText_ETInputType, ETActionType, ecdarText_ETOutputType, ecdarText_ETMultiInitialiser, ecdarText_ETStructType, ecdarText_ETFieldDeclaration, ecdarText_ETFieldID, ecdarText_ETSpecificationExpression, ecdarText_ETSpecificationBinding, ETSpecification, ecdarText_ETSpecificationDefinition, ecdarText_ETSpecificationBody, ecdarText_ETSpecificationTemplate, ETSpecificationDefinition, ecdarText_ETBooleanType, ecdarText_ETScalarType, ecdarText_ETEdge, ecdarText_ETSelect, ecdarText_ETIO, ecdarText_ETParameter, ecdarText_ETLocation, ecdarText_ETSpecificationDisjunctionExpression, ETSpecificationExpression, ecdarText_ETSpecificationConjunctionExpression, ecdarText_ETSpecificationCompositionExpression, ecdarText_ETSpecificationReference, ecdarText_ETSpecificationInstantiation, ecdarText_ETTypeReference, ecdarText_ETImplyExpression, ecdarText_ETLogicOrExpression, ecdarText_ETLogicAndExpression, ecdarText_ETAssignmentExpression, ecdarText_ETAdditionAssignmentExpression, ecdarText_ETForallExpression, ETExpression, ecdarText_ETExistsExpression, ecdarText_ETDivisionAssignmentExpression, ecdarText_ETModuloAssignmentExpression, ecdarText_ETBitOrAssignmentExpression, ecdarText_ETBitAndAssignmentExpression, ecdarText_ETBitXORAssignmentExpression, ecdarText_ETBitLeftAssignmentExpression, ecdarText_ETBitRightAssignmentExpression, ecdarText_ETSubtractionAssignmentExpression, ecdarText_ETMultiplicationAssignmentExpression, ecdarText_ETBitOrExpression, ecdarText_ETBitXORExpression, ecdarText_ETBitAndExpression, ecdarText_ETConditionalExpression, ecdarText_ETUnequalExpression, ecdarText_ETLessExpression, ecdarText_ETEqualExpression, ecdarText_ETGreaterEqualExpression, ecdarText_ETGreaterExpression, ecdarText_ETMinExpression, ecdarText_ETLessEqualExpression, ecdarText_ETMaxExpression, ecdarText_ETBitLeftExpression, ecdarText_ETBitRightExpression, ecdarText_ETAddExpression, ecdarText_ETSubtractExpression, ecdarText_ETDivideExpression, ecdarText_ETModuloExpression, ecdarText_ETPreIncrementExpression, ecdarText_ETPreDecrementExpression, ecdarText_ETLogicNotExpression, ecdarText_ETMinusExpression, ecdarText_ETPostIncrementExpression, ecdarText_ETMultiplyExpression, ecdarText_ETStructExpression, ecdarText_ETArrayExpression, ecdarText_ETReference, ecdarText_EObject, ecdarText_ETBooleanLiteral, ecdarText_ETNumberLiteral, ecdarText_ETPostDecrementExpression, ETIOType},
    associations={imports0, declarations1, specifications3, size5, declarations6, type11, variables13, dimensions15, initialiser18, modifiers8, identifier9, baseType24, types26, dimensions28, min31, max33, expression20, initialisers22, declarations38, type39, fields42, dimensions44, expression47, body48, size36, type58, dimensions61, invariants64, edges67, selects69, io71, guard73, target76, updates79, expression82, parameters49, declarations50, initialLocation53, locations55, left90, right92, left95, right97, left100, right102, specification105, template107, type85, type117, target88, expression119, left122, right124, left127, right129, left132, right134, left137, right139, left142, right144, arguments109, type112, expression114, right154, left157, right159, left162, right164, left167, right169, left172, right174, left177, right179, left182, right184, left147, right149, left152, else197, left200, right202, left205, right207, left210, left187, right189, condition192, then194, right217, left220, right222, left225, right227, right212, left215, right232, left235, right237, left240, right242, left230, left250, right252, left255, right257, left245, right247, left260, right262, left265, right267, left270, right277, left280, right282, left285, right287, expression290, expression292, expression294, expression296, expression298, right272, left275, left302, left304, right306, target309, expression300},
    generalizations={gen_ecdarText_ETVariableDeclaration_ETDeclaration, gen_ecdarText_ETSingleInitialiser_ETInitialiser, gen_ecdarText_ETTypeDeclaration_ETDeclaration, gen_ecdarText_ETIntegerType_ETTypeIdentifier, gen_ecdarText_ETClockType_ETTypeIdentifier, gen_ecdarText_ETActionType_ETTypeIdentifier, gen_ecdarText_ETInputType_ETActionType, gen_ecdarText_ETOutputType_ETActionType, gen_ecdarText_ETMultiInitialiser_ETInitialiser, gen_ecdarText_ETStructType_ETTypeIdentifier, gen_ecdarText_ETSpecificationBinding_ETSpecification, gen_ecdarText_ETSpecificationDefinition_ETSpecification, gen_ecdarText_ETSpecificationTemplate_ETSpecificationDefinition, gen_ecdarText_ETBooleanType_ETTypeIdentifier, gen_ecdarText_ETScalarType_ETTypeIdentifier, gen_ecdarText_ETSpecificationDisjunctionExpression_ETSpecificationExpression, gen_ecdarText_ETSpecificationConjunctionExpression_ETSpecificationExpression, gen_ecdarText_ETSpecificationCompositionExpression_ETSpecificationExpression, gen_ecdarText_ETSpecificationReference_ETSpecificationExpression, gen_ecdarText_ETSpecificationInstantiation_ETSpecificationExpression, gen_ecdarText_ETTypeReference_ETTypeIdentifier, gen_ecdarText_ETImplyExpression_ETExpression, gen_ecdarText_ETLogicOrExpression_ETExpression, gen_ecdarText_ETLogicAndExpression_ETExpression, gen_ecdarText_ETAssignmentExpression_ETExpression, gen_ecdarText_ETAdditionAssignmentExpression_ETExpression, gen_ecdarText_ETForallExpression_ETExpression, gen_ecdarText_ETExistsExpression_ETExpression, gen_ecdarText_ETDivisionAssignmentExpression_ETExpression, gen_ecdarText_ETModuloAssignmentExpression_ETExpression, gen_ecdarText_ETBitOrAssignmentExpression_ETExpression, gen_ecdarText_ETBitAndAssignmentExpression_ETExpression, gen_ecdarText_ETBitXORAssignmentExpression_ETExpression, gen_ecdarText_ETBitLeftAssignmentExpression_ETExpression, gen_ecdarText_ETBitRightAssignmentExpression_ETExpression, gen_ecdarText_ETSubtractionAssignmentExpression_ETExpression, gen_ecdarText_ETMultiplicationAssignmentExpression_ETExpression, gen_ecdarText_ETBitOrExpression_ETExpression, gen_ecdarText_ETBitXORExpression_ETExpression, gen_ecdarText_ETBitAndExpression_ETExpression, gen_ecdarText_ETConditionalExpression_ETExpression, gen_ecdarText_ETUnequalExpression_ETExpression, gen_ecdarText_ETLessExpression_ETExpression, gen_ecdarText_ETEqualExpression_ETExpression, gen_ecdarText_ETGreaterEqualExpression_ETExpression, gen_ecdarText_ETGreaterExpression_ETExpression, gen_ecdarText_ETMinExpression_ETExpression, gen_ecdarText_ETLessEqualExpression_ETExpression, gen_ecdarText_ETMaxExpression_ETExpression, gen_ecdarText_ETBitLeftExpression_ETExpression, gen_ecdarText_ETAddExpression_ETExpression, gen_ecdarText_ETSubtractExpression_ETExpression, gen_ecdarText_ETBitRightExpression_ETExpression, gen_ecdarText_ETDivideExpression_ETExpression, gen_ecdarText_ETModuloExpression_ETExpression, gen_ecdarText_ETPreIncrementExpression_ETExpression, gen_ecdarText_ETPreDecrementExpression_ETExpression, gen_ecdarText_ETLogicNotExpression_ETExpression, gen_ecdarText_ETMinusExpression_ETExpression, gen_ecdarText_ETPostIncrementExpression_ETExpression, gen_ecdarText_ETMultiplyExpression_ETExpression, gen_ecdarText_ETStructExpression_ETExpression, gen_ecdarText_ETArrayExpression_ETExpression, gen_ecdarText_ETReference_ETExpression, gen_ecdarText_ETBooleanLiteral_ETExpression, gen_ecdarText_ETNumberLiteral_ETExpression, gen_ecdarText_ETPostDecrementExpression_ETExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)