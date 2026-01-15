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
DocType: Enumeration = Enumeration(
    name="DocType",
    literals={
            EnumerationLiteral(name="ScannedPaperCVI"),
			EnumerationLiteral(name="ScannedTestChart"),
			EnumerationLiteral(name="PDFCVI"),
			EnumerationLiteral(name="PDFTestChart"),
			EnumerationLiteral(name="Other")
    }
)

ISO3166Country: Enumeration = Enumeration(
    name="ISO3166Country",
    literals={
            EnumerationLiteral(name="USA")
    }
)

MovementPurpose: Enumeration = Enumeration(
    name="MovementPurpose",
    literals={
            EnumerationLiteral(name="slaughter"),
			EnumerationLiteral(name="medicalTreatment"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="show"),
			EnumerationLiteral(name="race"),
			EnumerationLiteral(name="rodeo"),
			EnumerationLiteral(name="sale"),
			EnumerationLiteral(name="pet"),
			EnumerationLiteral(name="breeding"),
			EnumerationLiteral(name="feeding"),
			EnumerationLiteral(name="grazing"),
			EnumerationLiteral(name="training")
    }
)

PhoneDevice: Enumeration = Enumeration(
    name="PhoneDevice",
    literals={
            EnumerationLiteral(name="Landline"),
			EnumerationLiteral(name="Cellphone"),
			EnumerationLiteral(name="Fax"),
			EnumerationLiteral(name="Unknown")
    }
)

ProgramStatusValue: Enumeration = Enumeration(
    name="ProgramStatusValue",
    literals={
            EnumerationLiteral(name="Free"),
			EnumerationLiteral(name="ModifiedAccredited"),
			EnumerationLiteral(name="ModifiedAdvancedAccredited"),
			EnumerationLiteral(name="Other")
    }
)

ProgramStatusName: Enumeration = Enumeration(
    name="ProgramStatusName",
    literals={
            EnumerationLiteral(name="BovineTuberculosis"),
			EnumerationLiteral(name="BrucellosisState"),
			EnumerationLiteral(name="BrucellosisHerd")
    }
)

ResultName: Enumeration = Enumeration(
    name="ResultName",
    literals={
            EnumerationLiteral(name="RESULT"),
			EnumerationLiteral(name="COMMENT")
    }
)

Sex: Enumeration = Enumeration(
    name="Sex",
    literals={
            EnumerationLiteral(name="Female"),
			EnumerationLiteral(name="Male"),
			EnumerationLiteral(name="GenderUnknown"),
			EnumerationLiteral(name="SpayedFemale"),
			EnumerationLiteral(name="NeuteredMale"),
			EnumerationLiteral(name="TrueHermaphrodite"),
			EnumerationLiteral(name="Other")
    }
)

SpeciesCode: Enumeration = Enumeration(
    name="SpeciesCode",
    literals={
            EnumerationLiteral(name="OVI"),
			EnumerationLiteral(name="POR"),
			EnumerationLiteral(name="UNK"),
			EnumerationLiteral(name="BOV"),
			EnumerationLiteral(name="CAP"),
			EnumerationLiteral(name="CER"),
			EnumerationLiteral(name="EQU")
    }
)

TagType: Enumeration = Enumeration(
    name="TagType",
    literals={
            EnumerationLiteral(name="UN"),
			EnumerationLiteral(name="AIN"),
			EnumerationLiteral(name="AMID"),
			EnumerationLiteral(name="BRAND"),
			EnumerationLiteral(name="BRANDIMAGE"),
			EnumerationLiteral(name="BT"),
			EnumerationLiteral(name="IMP"),
			EnumerationLiteral(name="MGT"),
			EnumerationLiteral(name="N840RFID"),
			EnumerationLiteral(name="NUES8"),
			EnumerationLiteral(name="NUES9"),
			EnumerationLiteral(name="OFORID"),
			EnumerationLiteral(name="OTH"),
			EnumerationLiteral(name="NAME"),
			EnumerationLiteral(name="SGFLID"),
			EnumerationLiteral(name="NPIN"),
			EnumerationLiteral(name="TAT")
    }
)

UsState: Enumeration = Enumeration(
    name="UsState",
    literals={
            EnumerationLiteral(name="CA"),
			EnumerationLiteral(name="CO"),
			EnumerationLiteral(name="CT"),
			EnumerationLiteral(name="DC"),
			EnumerationLiteral(name="DE"),
			EnumerationLiteral(name="FL"),
			EnumerationLiteral(name="AA"),
			EnumerationLiteral(name="AE"),
			EnumerationLiteral(name="AK"),
			EnumerationLiteral(name="AL"),
			EnumerationLiteral(name="AP"),
			EnumerationLiteral(name="AR"),
			EnumerationLiteral(name="AS"),
			EnumerationLiteral(name="AZ"),
			EnumerationLiteral(name="NM"),
			EnumerationLiteral(name="NV"),
			EnumerationLiteral(name="NY"),
			EnumerationLiteral(name="OH"),
			EnumerationLiteral(name="OK"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="FM"),
			EnumerationLiteral(name="GA"),
			EnumerationLiteral(name="GU"),
			EnumerationLiteral(name="HI"),
			EnumerationLiteral(name="IA"),
			EnumerationLiteral(name="ID"),
			EnumerationLiteral(name="IL"),
			EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="KS"),
			EnumerationLiteral(name="KY"),
			EnumerationLiteral(name="LA"),
			EnumerationLiteral(name="MA"),
			EnumerationLiteral(name="MD"),
			EnumerationLiteral(name="ME"),
			EnumerationLiteral(name="MH"),
			EnumerationLiteral(name="MI"),
			EnumerationLiteral(name="MN"),
			EnumerationLiteral(name="MO"),
			EnumerationLiteral(name="MP"),
			EnumerationLiteral(name="MS"),
			EnumerationLiteral(name="MT"),
			EnumerationLiteral(name="NC"),
			EnumerationLiteral(name="ND"),
			EnumerationLiteral(name="NE"),
			EnumerationLiteral(name="NH"),
			EnumerationLiteral(name="NJ"),
			EnumerationLiteral(name="PA"),
			EnumerationLiteral(name="PR"),
			EnumerationLiteral(name="PW"),
			EnumerationLiteral(name="RI"),
			EnumerationLiteral(name="SC"),
			EnumerationLiteral(name="SD"),
			EnumerationLiteral(name="TN"),
			EnumerationLiteral(name="TX"),
			EnumerationLiteral(name="UT"),
			EnumerationLiteral(name="VA"),
			EnumerationLiteral(name="VI"),
			EnumerationLiteral(name="VT"),
			EnumerationLiteral(name="WA"),
			EnumerationLiteral(name="WI"),
			EnumerationLiteral(name="WV"),
			EnumerationLiteral(name="WY")
    }
)

# Classes
ecvi_Accessions = Class(name="ecvi::Accessions")
ecvi_Accession = Class(name="ecvi::Accession")
ecvi_Laboratory = Class(name="ecvi::Laboratory")
ecvi_Address = Class(name="ecvi::Address")
ecvi_GeoPoint = Class(name="ecvi::GeoPoint")
ecvi_Test = Class(name="ecvi::Test")
ecvi_Animal = Class(name="ecvi::Animal")
ecvi_AnimalTag = Class(name="ecvi::AnimalTag")
ecvi_Attachement = Class(name="ecvi::Attachement")
ecvi_Contact = Class(name="ecvi::Contact")
ecvi_Person = Class(name="ecvi::Person")
ecvi_EStringToStringMapEntry = Class(name="ecvi::EStringToStringMapEntry")
ecvi_Ecvi = Class(name="ecvi::Ecvi")
ecvi_DocumentRoot = Class(name="ecvi::DocumentRoot")
ecvi_MovementPurposes = Class(name="ecvi::MovementPurposes")
ecvi_Premises = Class(name="ecvi::Premises")
ecvi_Veterinarian = Class(name="ecvi::Veterinarian")
ecvi_GroupLot = Class(name="ecvi::GroupLot")
ecvi_PhoneNum = Class(name="ecvi::PhoneNum")
ecvi_ProgramStatus = Class(name="ecvi::ProgramStatus")
ecvi_ResultValue = Class(name="ecvi::ResultValue")

# ecvi_Accessions class attributes and methods

# ecvi_Accession class attributes and methods
ecvi_Accession_id: Property = Property(name="id", type=StringType)
ecvi_Accession_infieldTest: Property = Property(name="infieldTest", type=StringType)
ecvi_Accession.attributes={ecvi_Accession_infieldTest, ecvi_Accession_id}

# ecvi_Laboratory class attributes and methods
ecvi_Laboratory_labName: Property = Property(name="labName", type=StringType)
ecvi_Laboratory_premId: Property = Property(name="premId", type=StringType)
ecvi_Laboratory_accessionDate: Property = Property(name="accessionDate", type=StringType)
ecvi_Laboratory_accessionNumber: Property = Property(name="accessionNumber", type=StringType)
ecvi_Laboratory.attributes={ecvi_Laboratory_labName, ecvi_Laboratory_premId, ecvi_Laboratory_accessionNumber, ecvi_Laboratory_accessionDate}

# ecvi_Address class attributes and methods
ecvi_Address_line2: Property = Property(name="line2", type=StringType)
ecvi_Address_town: Property = Property(name="town", type=StringType)
ecvi_Address_county: Property = Property(name="county", type=StringType)
ecvi_Address_line1: Property = Property(name="line1", type=StringType)
ecvi_Address_state: Property = Property(name="state", type=StringType)
ecvi_Address_zIP: Property = Property(name="zIP", type=StringType)
ecvi_Address_country: Property = Property(name="country", type=StringType)
ecvi_Address.attributes={ecvi_Address_line1, ecvi_Address_line2, ecvi_Address_state, ecvi_Address_country, ecvi_Address_zIP, ecvi_Address_county, ecvi_Address_town}

# ecvi_GeoPoint class attributes and methods
ecvi_GeoPoint_lat: Property = Property(name="lat", type=StringType)
ecvi_GeoPoint_lng: Property = Property(name="lng", type=StringType)
ecvi_GeoPoint.attributes={ecvi_GeoPoint_lng, ecvi_GeoPoint_lat}

# ecvi_Test class attributes and methods
ecvi_Test_idref: Property = Property(name="idref", type=StringType)
ecvi_Test_testCode: Property = Property(name="testCode", type=StringType)
ecvi_Test.attributes={ecvi_Test_idref, ecvi_Test_testCode}

# ecvi_Animal class attributes and methods
ecvi_Animal_age: Property = Property(name="age", type=StringType)
ecvi_Animal_breed: Property = Property(name="breed", type=StringType)
ecvi_Animal_inspectionDate: Property = Property(name="inspectionDate", type=StringType)
ecvi_Animal_sex: Property = Property(name="sex", type=StringType)
ecvi_Animal_sexDetail: Property = Property(name="sexDetail", type=StringType)
ecvi_Animal.attributes={ecvi_Animal_breed, ecvi_Animal_sexDetail, ecvi_Animal_age, ecvi_Animal_sex, ecvi_Animal_inspectionDate}

# ecvi_AnimalTag class attributes and methods
ecvi_AnimalTag_brandImage: Property = Property(name="brandImage", type=StringType)
ecvi_AnimalTag_number: Property = Property(name="number", type=StringType)
ecvi_AnimalTag_type: Property = Property(name="type", type=StringType)
ecvi_AnimalTag.attributes={ecvi_AnimalTag_type, ecvi_AnimalTag_number, ecvi_AnimalTag_brandImage}

# ecvi_Attachement class attributes and methods
ecvi_Attachement_filename: Property = Property(name="filename", type=StringType)
ecvi_Attachement_mimeType: Property = Property(name="mimeType", type=StringType)
ecvi_Attachement_payload: Property = Property(name="payload", type=StringType)
ecvi_Attachement_comment: Property = Property(name="comment", type=StringType)
ecvi_Attachement_docType: Property = Property(name="docType", type=StringType)
ecvi_Attachement.attributes={ecvi_Attachement_comment, ecvi_Attachement_filename, ecvi_Attachement_mimeType, ecvi_Attachement_payload, ecvi_Attachement_docType}

# ecvi_Contact class attributes and methods
ecvi_Contact_premId: Property = Property(name="premId", type=StringType)
ecvi_Contact_premName: Property = Property(name="premName", type=StringType)
ecvi_Contact.attributes={ecvi_Contact_premId, ecvi_Contact_premName}

# ecvi_Person class attributes and methods
ecvi_Person_name: Property = Property(name="name", type=StringType)
ecvi_Person.attributes={ecvi_Person_name}

# ecvi_EStringToStringMapEntry class attributes and methods

# ecvi_Ecvi class attributes and methods
ecvi_Ecvi_group: Property = Property(name="group", type=StringType)
ecvi_Ecvi_group1: Property = Property(name="group1", type=StringType)
ecvi_Ecvi_cviNumber: Property = Property(name="cviNumber", type=StringType)
ecvi_Ecvi_entryPermitNumber: Property = Property(name="entryPermitNumber", type=StringType)
ecvi_Ecvi_expirationDate: Property = Property(name="expirationDate", type=StringType)
ecvi_Ecvi_issueDate: Property = Property(name="issueDate", type=StringType)
ecvi_Ecvi_shipmentDate: Property = Property(name="shipmentDate", type=StringType)
ecvi_Ecvi_speciesCode: Property = Property(name="speciesCode", type=StringType)
ecvi_Ecvi.attributes={ecvi_Ecvi_group, ecvi_Ecvi_group1, ecvi_Ecvi_shipmentDate, ecvi_Ecvi_cviNumber, ecvi_Ecvi_speciesCode, ecvi_Ecvi_expirationDate, ecvi_Ecvi_issueDate, ecvi_Ecvi_entryPermitNumber}

# ecvi_DocumentRoot class attributes and methods
ecvi_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
ecvi_DocumentRoot.attributes={ecvi_DocumentRoot_mixed}

# ecvi_MovementPurposes class attributes and methods
ecvi_MovementPurposes_movementPurpose: Property = Property(name="movementPurpose", type=StringType)
ecvi_MovementPurposes.attributes={ecvi_MovementPurposes_movementPurpose}

# ecvi_Premises class attributes and methods
ecvi_Premises_premId: Property = Property(name="premId", type=StringType)
ecvi_Premises_premName: Property = Property(name="premName", type=StringType)
ecvi_Premises.attributes={ecvi_Premises_premName, ecvi_Premises_premId}

# ecvi_Veterinarian class attributes and methods
ecvi_Veterinarian_licenseIssueState: Property = Property(name="licenseIssueState", type=StringType)
ecvi_Veterinarian_licenseNumber: Property = Property(name="licenseNumber", type=StringType)
ecvi_Veterinarian_nationalAccreditationNumber: Property = Property(name="nationalAccreditationNumber", type=StringType)
ecvi_Veterinarian.attributes={ecvi_Veterinarian_licenseNumber, ecvi_Veterinarian_nationalAccreditationNumber, ecvi_Veterinarian_licenseIssueState}

# ecvi_GroupLot class attributes and methods
ecvi_GroupLot_sex: Property = Property(name="sex", type=StringType)
ecvi_GroupLot_age: Property = Property(name="age", type=StringType)
ecvi_GroupLot_breed: Property = Property(name="breed", type=StringType)
ecvi_GroupLot_description: Property = Property(name="description", type=StringType)
ecvi_GroupLot_quantity: Property = Property(name="quantity", type=StringType)
ecvi_GroupLot_sexDetail: Property = Property(name="sexDetail", type=StringType)
ecvi_GroupLot_species: Property = Property(name="species", type=StringType)
ecvi_GroupLot_unit: Property = Property(name="unit", type=StringType)
ecvi_GroupLot.attributes={ecvi_GroupLot_quantity, ecvi_GroupLot_species, ecvi_GroupLot_unit, ecvi_GroupLot_age, ecvi_GroupLot_sexDetail, ecvi_GroupLot_sex, ecvi_GroupLot_breed, ecvi_GroupLot_description}

# ecvi_PhoneNum class attributes and methods
ecvi_PhoneNum_comment: Property = Property(name="comment", type=StringType)
ecvi_PhoneNum_number: Property = Property(name="number", type=StringType)
ecvi_PhoneNum_type: Property = Property(name="type", type=StringType)
ecvi_PhoneNum.attributes={ecvi_PhoneNum_type, ecvi_PhoneNum_number, ecvi_PhoneNum_comment}

# ecvi_ProgramStatus class attributes and methods
ecvi_ProgramStatus_name: Property = Property(name="name", type=StringType)
ecvi_ProgramStatus_value: Property = Property(name="value", type=StringType)
ecvi_ProgramStatus_valueOther: Property = Property(name="valueOther", type=StringType)
ecvi_ProgramStatus.attributes={ecvi_ProgramStatus_valueOther, ecvi_ProgramStatus_value, ecvi_ProgramStatus_name}

# ecvi_ResultValue class attributes and methods
ecvi_ResultValue_resultFloat: Property = Property(name="resultFloat", type=StringType)
ecvi_ResultValue_resultInteger: Property = Property(name="resultInteger", type=StringType)
ecvi_ResultValue_resultString: Property = Property(name="resultString", type=StringType)
ecvi_ResultValue_resultName: Property = Property(name="resultName", type=StringType)
ecvi_ResultValue.attributes={ecvi_ResultValue_resultFloat, ecvi_ResultValue_resultInteger, ecvi_ResultValue_resultString, ecvi_ResultValue_resultName}

# Relationships
laboratory0: BinaryAssociation = BinaryAssociation(
    name="laboratory0",
    ends={
        Property(name="ecvi_Laboratory", type=ecvi_Accession, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Accession", type=ecvi_Laboratory, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accession1: BinaryAssociation = BinaryAssociation(
    name="accession1",
    ends={
        Property(name="ecvi_Accession2", type=ecvi_Accessions, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Accessions", type=ecvi_Accession, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
geoPoint3: BinaryAssociation = BinaryAssociation(
    name="geoPoint3",
    ends={
        Property(name="ecvi_GeoPoint", type=ecvi_Address, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Address", type=ecvi_GeoPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
test5: BinaryAssociation = BinaryAssociation(
    name="test5",
    ends={
        Property(name="ecvi_Test", type=ecvi_Animal, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Animal6", type=ecvi_Test, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
animalTag4: BinaryAssociation = BinaryAssociation(
    name="animalTag4",
    ends={
        Property(name="ecvi_AnimalTag", type=ecvi_Animal, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Animal", type=ecvi_AnimalTag, multiplicity=Multiplicity(1, 6), is_composite=True)
    }
)
person9: BinaryAssociation = BinaryAssociation(
    name="person9",
    ends={
        Property(name="ecvi_Person", type=ecvi_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Contact10", type=ecvi_Person, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
address7: BinaryAssociation = BinaryAssociation(
    name="address7",
    ends={
        Property(name="ecvi_Address8", type=ecvi_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Contact", type=ecvi_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xMLNSPrefixMap11: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap11",
    ends={
        Property(name="ecvi_EStringToStringMapEntry", type=ecvi_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_DocumentRoot", type=ecvi_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation12: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation12",
    ends={
        Property(name="ecvi_EStringToStringMapEntry14", type=ecvi_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_DocumentRoot13", type=ecvi_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eCVI15: BinaryAssociation = BinaryAssociation(
    name="eCVI15",
    ends={
        Property(name="ecvi_Ecvi", type=ecvi_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_DocumentRoot16", type=ecvi_Ecvi, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
movementPurposes19: BinaryAssociation = BinaryAssociation(
    name="movementPurposes19",
    ends={
        Property(name="ecvi_MovementPurposes", type=ecvi_Ecvi, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Ecvi20", type=ecvi_MovementPurposes, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
origin21: BinaryAssociation = BinaryAssociation(
    name="origin21",
    ends={
        Property(name="ecvi_Premises", type=ecvi_Ecvi, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Ecvi22", type=ecvi_Premises, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
destination23: BinaryAssociation = BinaryAssociation(
    name="destination23",
    ends={
        Property(name="ecvi_Premises25", type=ecvi_Ecvi, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Ecvi24", type=ecvi_Premises, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
veterinarian17: BinaryAssociation = BinaryAssociation(
    name="veterinarian17",
    ends={
        Property(name="ecvi_Veterinarian", type=ecvi_Ecvi, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Ecvi18", type=ecvi_Veterinarian, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accessions32: BinaryAssociation = BinaryAssociation(
    name="accessions32",
    ends={
        Property(name="ecvi_Accessions34", type=ecvi_Ecvi, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Ecvi33", type=ecvi_Accessions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
animal35: BinaryAssociation = BinaryAssociation(
    name="animal35",
    ends={
        Property(name="ecvi_Animal37", type=ecvi_Ecvi, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Ecvi36", type=ecvi_Animal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consignor26: BinaryAssociation = BinaryAssociation(
    name="consignor26",
    ends={
        Property(name="ecvi_Contact28", type=ecvi_Ecvi, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Ecvi27", type=ecvi_Contact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
consignee29: BinaryAssociation = BinaryAssociation(
    name="consignee29",
    ends={
        Property(name="ecvi_Contact31", type=ecvi_Ecvi, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Ecvi30", type=ecvi_Contact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupLot38: BinaryAssociation = BinaryAssociation(
    name="groupLot38",
    ends={
        Property(name="ecvi_GroupLot", type=ecvi_Ecvi, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Ecvi39", type=ecvi_GroupLot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attachment40: BinaryAssociation = BinaryAssociation(
    name="attachment40",
    ends={
        Property(name="ecvi_Attachement", type=ecvi_Ecvi, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Ecvi41", type=ecvi_Attachement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address42: BinaryAssociation = BinaryAssociation(
    name="address42",
    ends={
        Property(name="ecvi_Address44", type=ecvi_Laboratory, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Laboratory43", type=ecvi_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phone45: BinaryAssociation = BinaryAssociation(
    name="phone45",
    ends={
        Property(name="ecvi_PhoneNum", type=ecvi_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Person46", type=ecvi_PhoneNum, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person52: BinaryAssociation = BinaryAssociation(
    name="person52",
    ends={
        Property(name="ecvi_Person54", type=ecvi_Premises, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Premises53", type=ecvi_Person, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
address47: BinaryAssociation = BinaryAssociation(
    name="address47",
    ends={
        Property(name="ecvi_Address49", type=ecvi_Premises, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Premises48", type=ecvi_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
programStatus50: BinaryAssociation = BinaryAssociation(
    name="programStatus50",
    ends={
        Property(name="ecvi_ProgramStatus", type=ecvi_Premises, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Premises51", type=ecvi_ProgramStatus, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result55: BinaryAssociation = BinaryAssociation(
    name="result55",
    ends={
        Property(name="ecvi_ResultValue", type=ecvi_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Test56", type=ecvi_ResultValue, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
address60: BinaryAssociation = BinaryAssociation(
    name="address60",
    ends={
        Property(name="ecvi_Address62", type=ecvi_Veterinarian, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Veterinarian61", type=ecvi_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
person57: BinaryAssociation = BinaryAssociation(
    name="person57",
    ends={
        Property(name="ecvi_Person59", type=ecvi_Veterinarian, multiplicity=Multiplicity(1, 1)),
        Property(name="ecvi_Veterinarian58", type=ecvi_Person, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ecvi",
    types={ecvi_Accessions, ecvi_Accession, ecvi_Laboratory, ecvi_Address, ecvi_GeoPoint, ecvi_Test, ecvi_Animal, ecvi_AnimalTag, ecvi_Attachement, ecvi_Contact, ecvi_Person, ecvi_EStringToStringMapEntry, ecvi_Ecvi, ecvi_DocumentRoot, ecvi_MovementPurposes, ecvi_Premises, ecvi_Veterinarian, ecvi_GroupLot, ecvi_PhoneNum, ecvi_ProgramStatus, ecvi_ResultValue, DocType, ISO3166Country, MovementPurpose, PhoneDevice, ProgramStatusValue, ProgramStatusName, ResultName, Sex, SpeciesCode, TagType, UsState},
    associations={laboratory0, accession1, geoPoint3, test5, animalTag4, person9, address7, xMLNSPrefixMap11, xSISchemaLocation12, eCVI15, movementPurposes19, origin21, destination23, veterinarian17, accessions32, animal35, consignor26, consignee29, groupLot38, attachment40, address42, phone45, person52, address47, programStatus50, result55, address60, person57},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)