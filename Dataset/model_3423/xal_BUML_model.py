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
DependentThoroughfaresType: Enumeration = Enumeration(
    name="DependentThoroughfaresType",
    literals={
            EnumerationLiteral(name="Yes"),
			EnumerationLiteral(name="No")
    }
)

IndicatorOccurence: Enumeration = Enumeration(
    name="IndicatorOccurence",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

IndicatorOccurrence3: Enumeration = Enumeration(
    name="IndicatorOccurrence3",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

IndicatorOccurrence4: Enumeration = Enumeration(
    name="IndicatorOccurrence4",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

IndicatorOccurrence: Enumeration = Enumeration(
    name="IndicatorOccurrence",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

IndicatorOccurrence1: Enumeration = Enumeration(
    name="IndicatorOccurrence1",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

IndicatorOccurrence2: Enumeration = Enumeration(
    name="IndicatorOccurrence2",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

NameNumberOccurrence: Enumeration = Enumeration(
    name="NameNumberOccurrence",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

NumberOccurrence: Enumeration = Enumeration(
    name="NumberOccurrence",
    literals={
            EnumerationLiteral(name="BeforeName"),
			EnumerationLiteral(name="AfterName"),
			EnumerationLiteral(name="BeforeType"),
			EnumerationLiteral(name="AfterType")
    }
)

NumberRangeOccurence: Enumeration = Enumeration(
    name="NumberRangeOccurence",
    literals={
            EnumerationLiteral(name="BeforeName"),
			EnumerationLiteral(name="AfterName"),
			EnumerationLiteral(name="BeforeType"),
			EnumerationLiteral(name="AfterType")
    }
)

NumberRangeOccurrence: Enumeration = Enumeration(
    name="NumberRangeOccurrence",
    literals={
            EnumerationLiteral(name="BeforeName"),
			EnumerationLiteral(name="AfterName"),
			EnumerationLiteral(name="BeforeType"),
			EnumerationLiteral(name="AfterType")
    }
)

NumberTypeOccurrence: Enumeration = Enumeration(
    name="NumberTypeOccurrence",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

NumberTypeOccurrence1: Enumeration = Enumeration(
    name="NumberTypeOccurrence1",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

NumberTypeType: Enumeration = Enumeration(
    name="NumberTypeType",
    literals={
            EnumerationLiteral(name="Single"),
			EnumerationLiteral(name="Range")
    }
)

NumberTypeType1: Enumeration = Enumeration(
    name="NumberTypeType1",
    literals={
            EnumerationLiteral(name="Single"),
			EnumerationLiteral(name="Range")
    }
)

RangeTypeType: Enumeration = Enumeration(
    name="RangeTypeType",
    literals={
            EnumerationLiteral(name="Odd"),
			EnumerationLiteral(name="Even")
    }
)

TypeOccurrence: Enumeration = Enumeration(
    name="TypeOccurrence",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

TypeOccurrence1: Enumeration = Enumeration(
    name="TypeOccurrence1",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

TypeOccurrence2: Enumeration = Enumeration(
    name="TypeOccurrence2",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
    }
)

# Classes
xal_Address = Class(name="xal::Address")
xal_AddressDetails = Class(name="xal::AddressDetails")
xal_PostalServiceElements = Class(name="xal::PostalServiceElements")
xal_AddressLines = Class(name="xal::AddressLines")
xal_Country = Class(name="xal::Country")
xal_AdministrativeArea = Class(name="xal::AdministrativeArea")
xal_Locality = Class(name="xal::Locality")
xal_Thoroughfare = Class(name="xal::Thoroughfare")
xal_AddressIdentifier = Class(name="xal::AddressIdentifier")
xal_AddressLatitude = Class(name="xal::AddressLatitude")
xal_AddressLatitudeDirection = Class(name="xal::AddressLatitudeDirection")
xal_AddressLine = Class(name="xal::AddressLine")
xal_AddressLongitude = Class(name="xal::AddressLongitude")
xal_AddressLongitudeDirection = Class(name="xal::AddressLongitudeDirection")
xal_SubAdministrativeArea = Class(name="xal::SubAdministrativeArea")
xal_PostOffice = Class(name="xal::PostOffice")
xal_AdministrativeAreaName = Class(name="xal::AdministrativeAreaName")
xal_PostalCode = Class(name="xal::PostalCode")
xal_BuildingName = Class(name="xal::BuildingName")
xal_CountryNameCode = Class(name="xal::CountryNameCode")
xal_Barcode = Class(name="xal::Barcode")
xal_CountryName = Class(name="xal::CountryName")
xal_DepartmentName = Class(name="xal::DepartmentName")
xal_MailStop = Class(name="xal::MailStop")
xal_Department = Class(name="xal::Department")
xal_DependentLocality = Class(name="xal::DependentLocality")
xal_DependentLocalityName = Class(name="xal::DependentLocalityName")
xal_DependentLocalityNumber = Class(name="xal::DependentLocalityNumber")
xal_PostBox = Class(name="xal::PostBox")
xal_Premise = Class(name="xal::Premise")
xal_LargeMailUser = Class(name="xal::LargeMailUser")
xal_PostalRoute = Class(name="xal::PostalRoute")
xal_ThoroughfareName = Class(name="xal::ThoroughfareName")
xal_ThoroughfareTrailingType = Class(name="xal::ThoroughfareTrailingType")
xal_ThoroughfarePostDirection = Class(name="xal::ThoroughfarePostDirection")
xal_DependentThoroughfare = Class(name="xal::DependentThoroughfare")
xal_ThoroughfarePreDirection = Class(name="xal::ThoroughfarePreDirection")
xal_ThoroughfareLeadingType = Class(name="xal::ThoroughfareLeadingType")
xal_EStringToStringMapEntry = Class(name="xal::EStringToStringMapEntry")
xal_DocumentRoot = Class(name="xal::DocumentRoot")
xal_ThoroughfareNumber = Class(name="xal::ThoroughfareNumber")
xal_ThoroughfareNumberPrefix = Class(name="xal::ThoroughfareNumberPrefix")
xal_ThoroughfareNumberSuffix = Class(name="xal::ThoroughfareNumberSuffix")
xal_PremiseNumber = Class(name="xal::PremiseNumber")
xal_PremiseNumberPrefix = Class(name="xal::PremiseNumberPrefix")
xal_PremiseNumberSuffix = Class(name="xal::PremiseNumberSuffix")
xal_Firm = Class(name="xal::Firm")
xal_FirmName = Class(name="xal::FirmName")
xal_Xal = Class(name="xal::Xal")
xal_EndorsementLineCode = Class(name="xal::EndorsementLineCode")
xal_KeyLineCode = Class(name="xal::KeyLineCode")
xal_LargeMailUserName = Class(name="xal::LargeMailUserName")
xal_LargeMailUserIdentifier = Class(name="xal::LargeMailUserIdentifier")
xal_LocalityName = Class(name="xal::LocalityName")
xal_MailStopName = Class(name="xal::MailStopName")
xal_MailStopNumber = Class(name="xal::MailStopNumber")
xal_PostalCodeNumber = Class(name="xal::PostalCodeNumber")
xal_PostalCodeNumberExtension = Class(name="xal::PostalCodeNumberExtension")
xal_PostTown = Class(name="xal::PostTown")
xal_PostalRouteNumber = Class(name="xal::PostalRouteNumber")
xal_PostalRouteName = Class(name="xal::PostalRouteName")
xal_SortingCode = Class(name="xal::SortingCode")
xal_SupplementaryPostalServiceData = Class(name="xal::SupplementaryPostalServiceData")
xal_PostBoxNumber = Class(name="xal::PostBoxNumber")
xal_PostBoxNumberPrefix = Class(name="xal::PostBoxNumberPrefix")
xal_PostBoxNumberSuffix = Class(name="xal::PostBoxNumberSuffix")
xal_PostBoxNumberExtension = Class(name="xal::PostBoxNumberExtension")
xal_PostOfficeName = Class(name="xal::PostOfficeName")
xal_PostOfficeNumber = Class(name="xal::PostOfficeNumber")
xal_PostTownName = Class(name="xal::PostTownName")
xal_PostTownSuffix = Class(name="xal::PostTownSuffix")
xal_PremiseName = Class(name="xal::PremiseName")
xal_PremiseLocation = Class(name="xal::PremiseLocation")
xal_PremiseNumberRange = Class(name="xal::PremiseNumberRange")
xal_SubPremise = Class(name="xal::SubPremise")
xal_PremiseNumberRangeFrom = Class(name="xal::PremiseNumberRangeFrom")
xal_PremiseNumberRangeTo = Class(name="xal::PremiseNumberRangeTo")
xal_SubAdministrativeAreaName = Class(name="xal::SubAdministrativeAreaName")
xal_SubPremiseNumber = Class(name="xal::SubPremiseNumber")
xal_SubPremiseNumberPrefix = Class(name="xal::SubPremiseNumberPrefix")
xal_SubPremiseNumberSuffix = Class(name="xal::SubPremiseNumberSuffix")
xal_SubPremiseName = Class(name="xal::SubPremiseName")
xal_SubPremiseLocation = Class(name="xal::SubPremiseLocation")
xal_ThoroughfareNumberRange = Class(name="xal::ThoroughfareNumberRange")
xal_ThoroughfareNumberFrom = Class(name="xal::ThoroughfareNumberFrom")
xal_ThoroughfareNumberTo = Class(name="xal::ThoroughfareNumberTo")

# xal_Address class attributes and methods
xal_Address_mixed: Property = Property(name="mixed", type=StringType)
xal_Address_code: Property = Property(name="code", type=StringType)
xal_Address_type: Property = Property(name="type", type=StringType)
xal_Address_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_Address.attributes={xal_Address_code, xal_Address_anyAttribute, xal_Address_type, xal_Address_mixed}

# xal_AddressDetails class attributes and methods
xal_AddressDetails_code: Property = Property(name="code", type=StringType)
xal_AddressDetails_any: Property = Property(name="any", type=StringType)
xal_AddressDetails_addressDetailsKey: Property = Property(name="addressDetailsKey", type=StringType)
xal_AddressDetails_addressType: Property = Property(name="addressType", type=StringType)
xal_AddressDetails_currentStatus: Property = Property(name="currentStatus", type=StringType)
xal_AddressDetails_usage: Property = Property(name="usage", type=StringType)
xal_AddressDetails_validFromDate: Property = Property(name="validFromDate", type=StringType)
xal_AddressDetails_validToDate: Property = Property(name="validToDate", type=StringType)
xal_AddressDetails_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_AddressDetails.attributes={xal_AddressDetails_anyAttribute, xal_AddressDetails_currentStatus, xal_AddressDetails_addressType, xal_AddressDetails_validToDate, xal_AddressDetails_code, xal_AddressDetails_addressDetailsKey, xal_AddressDetails_any, xal_AddressDetails_usage, xal_AddressDetails_validFromDate}

# xal_PostalServiceElements class attributes and methods
xal_PostalServiceElements_any: Property = Property(name="any", type=StringType)
xal_PostalServiceElements_type: Property = Property(name="type", type=StringType)
xal_PostalServiceElements_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostalServiceElements.attributes={xal_PostalServiceElements_type, xal_PostalServiceElements_any, xal_PostalServiceElements_anyAttribute}

# xal_AddressLines class attributes and methods
xal_AddressLines_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_AddressLines_any: Property = Property(name="any", type=StringType)
xal_AddressLines.attributes={xal_AddressLines_any, xal_AddressLines_anyAttribute}

# xal_Country class attributes and methods
xal_Country_any: Property = Property(name="any", type=StringType)
xal_Country_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_Country.attributes={xal_Country_anyAttribute, xal_Country_any}

# xal_AdministrativeArea class attributes and methods
xal_AdministrativeArea_type: Property = Property(name="type", type=StringType)
xal_AdministrativeArea_usageType: Property = Property(name="usageType", type=StringType)
xal_AdministrativeArea_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_AdministrativeArea_any: Property = Property(name="any", type=StringType)
xal_AdministrativeArea_indicator: Property = Property(name="indicator", type=StringType)
xal_AdministrativeArea.attributes={xal_AdministrativeArea_anyAttribute, xal_AdministrativeArea_indicator, xal_AdministrativeArea_any, xal_AdministrativeArea_type, xal_AdministrativeArea_usageType}

# xal_Locality class attributes and methods
xal_Locality_indicator: Property = Property(name="indicator", type=StringType)
xal_Locality_type: Property = Property(name="type", type=StringType)
xal_Locality_usageType: Property = Property(name="usageType", type=StringType)
xal_Locality_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_Locality_any: Property = Property(name="any", type=StringType)
xal_Locality.attributes={xal_Locality_indicator, xal_Locality_anyAttribute, xal_Locality_usageType, xal_Locality_any, xal_Locality_type}

# xal_Thoroughfare class attributes and methods
xal_Thoroughfare_group: Property = Property(name="group", type=StringType)
xal_Thoroughfare_any: Property = Property(name="any", type=StringType)
xal_Thoroughfare_dependentThoroughfaresIndicator: Property = Property(name="dependentThoroughfaresIndicator", type=StringType)
xal_Thoroughfare_dependentThoroughfaresType: Property = Property(name="dependentThoroughfaresType", type=StringType)
xal_Thoroughfare_type: Property = Property(name="type", type=StringType)
xal_Thoroughfare_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_Thoroughfare_dependentThoroughfares: Property = Property(name="dependentThoroughfares", type=StringType)
xal_Thoroughfare_dependentThoroughfaresConnector: Property = Property(name="dependentThoroughfaresConnector", type=StringType)
xal_Thoroughfare.attributes={xal_Thoroughfare_group, xal_Thoroughfare_type, xal_Thoroughfare_anyAttribute, xal_Thoroughfare_dependentThoroughfaresType, xal_Thoroughfare_any, xal_Thoroughfare_dependentThoroughfaresConnector, xal_Thoroughfare_dependentThoroughfares, xal_Thoroughfare_dependentThoroughfaresIndicator}

# xal_AddressIdentifier class attributes and methods
xal_AddressIdentifier_code: Property = Property(name="code", type=StringType)
xal_AddressIdentifier_mixed: Property = Property(name="mixed", type=StringType)
xal_AddressIdentifier_identifierType: Property = Property(name="identifierType", type=StringType)
xal_AddressIdentifier_type: Property = Property(name="type", type=StringType)
xal_AddressIdentifier_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_AddressIdentifier.attributes={xal_AddressIdentifier_code, xal_AddressIdentifier_type, xal_AddressIdentifier_mixed, xal_AddressIdentifier_identifierType, xal_AddressIdentifier_anyAttribute}

# xal_AddressLatitude class attributes and methods
xal_AddressLatitude_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_AddressLatitude_mixed: Property = Property(name="mixed", type=StringType)
xal_AddressLatitude_code: Property = Property(name="code", type=StringType)
xal_AddressLatitude_type: Property = Property(name="type", type=StringType)
xal_AddressLatitude.attributes={xal_AddressLatitude_anyAttribute, xal_AddressLatitude_type, xal_AddressLatitude_mixed, xal_AddressLatitude_code}

# xal_AddressLatitudeDirection class attributes and methods
xal_AddressLatitudeDirection_mixed: Property = Property(name="mixed", type=StringType)
xal_AddressLatitudeDirection_code: Property = Property(name="code", type=StringType)
xal_AddressLatitudeDirection_type: Property = Property(name="type", type=StringType)
xal_AddressLatitudeDirection_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_AddressLatitudeDirection.attributes={xal_AddressLatitudeDirection_code, xal_AddressLatitudeDirection_type, xal_AddressLatitudeDirection_anyAttribute, xal_AddressLatitudeDirection_mixed}

# xal_AddressLine class attributes and methods
xal_AddressLine_code: Property = Property(name="code", type=StringType)
xal_AddressLine_mixed: Property = Property(name="mixed", type=StringType)
xal_AddressLine_type: Property = Property(name="type", type=StringType)
xal_AddressLine_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_AddressLine.attributes={xal_AddressLine_type, xal_AddressLine_anyAttribute, xal_AddressLine_mixed, xal_AddressLine_code}

# xal_AddressLongitude class attributes and methods
xal_AddressLongitude_mixed: Property = Property(name="mixed", type=StringType)
xal_AddressLongitude_code: Property = Property(name="code", type=StringType)
xal_AddressLongitude_type: Property = Property(name="type", type=StringType)
xal_AddressLongitude_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_AddressLongitude.attributes={xal_AddressLongitude_anyAttribute, xal_AddressLongitude_mixed, xal_AddressLongitude_code, xal_AddressLongitude_type}

# xal_AddressLongitudeDirection class attributes and methods
xal_AddressLongitudeDirection_code: Property = Property(name="code", type=StringType)
xal_AddressLongitudeDirection_type: Property = Property(name="type", type=StringType)
xal_AddressLongitudeDirection_mixed: Property = Property(name="mixed", type=StringType)
xal_AddressLongitudeDirection_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_AddressLongitudeDirection.attributes={xal_AddressLongitudeDirection_code, xal_AddressLongitudeDirection_mixed, xal_AddressLongitudeDirection_anyAttribute, xal_AddressLongitudeDirection_type}

# xal_SubAdministrativeArea class attributes and methods
xal_SubAdministrativeArea_usageType: Property = Property(name="usageType", type=StringType)
xal_SubAdministrativeArea_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_SubAdministrativeArea_any: Property = Property(name="any", type=StringType)
xal_SubAdministrativeArea_indicator: Property = Property(name="indicator", type=StringType)
xal_SubAdministrativeArea_type: Property = Property(name="type", type=StringType)
xal_SubAdministrativeArea.attributes={xal_SubAdministrativeArea_any, xal_SubAdministrativeArea_indicator, xal_SubAdministrativeArea_usageType, xal_SubAdministrativeArea_type, xal_SubAdministrativeArea_anyAttribute}

# xal_PostOffice class attributes and methods
xal_PostOffice_any: Property = Property(name="any", type=StringType)
xal_PostOffice_indicator: Property = Property(name="indicator", type=StringType)
xal_PostOffice_type: Property = Property(name="type", type=StringType)
xal_PostOffice_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostOffice.attributes={xal_PostOffice_anyAttribute, xal_PostOffice_any, xal_PostOffice_type, xal_PostOffice_indicator}

# xal_AdministrativeAreaName class attributes and methods
xal_AdministrativeAreaName_mixed: Property = Property(name="mixed", type=StringType)
xal_AdministrativeAreaName_code: Property = Property(name="code", type=StringType)
xal_AdministrativeAreaName_type: Property = Property(name="type", type=StringType)
xal_AdministrativeAreaName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_AdministrativeAreaName.attributes={xal_AdministrativeAreaName_type, xal_AdministrativeAreaName_mixed, xal_AdministrativeAreaName_anyAttribute, xal_AdministrativeAreaName_code}

# xal_PostalCode class attributes and methods
xal_PostalCode_any: Property = Property(name="any", type=StringType)
xal_PostalCode_type: Property = Property(name="type", type=StringType)
xal_PostalCode_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostalCode.attributes={xal_PostalCode_any, xal_PostalCode_anyAttribute, xal_PostalCode_type}

# xal_BuildingName class attributes and methods
xal_BuildingName_mixed: Property = Property(name="mixed", type=StringType)
xal_BuildingName_code: Property = Property(name="code", type=StringType)
xal_BuildingName_type: Property = Property(name="type", type=StringType)
xal_BuildingName_typeOccurrence: Property = Property(name="typeOccurrence", type=StringType)
xal_BuildingName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_BuildingName.attributes={xal_BuildingName_type, xal_BuildingName_anyAttribute, xal_BuildingName_mixed, xal_BuildingName_code, xal_BuildingName_typeOccurrence}

# xal_CountryNameCode class attributes and methods
xal_CountryNameCode_mixed: Property = Property(name="mixed", type=StringType)
xal_CountryNameCode_code: Property = Property(name="code", type=StringType)
xal_CountryNameCode_scheme: Property = Property(name="scheme", type=StringType)
xal_CountryNameCode_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_CountryNameCode.attributes={xal_CountryNameCode_mixed, xal_CountryNameCode_anyAttribute, xal_CountryNameCode_scheme, xal_CountryNameCode_code}

# xal_Barcode class attributes and methods
xal_Barcode_mixed: Property = Property(name="mixed", type=StringType)
xal_Barcode_code: Property = Property(name="code", type=StringType)
xal_Barcode_type: Property = Property(name="type", type=StringType)
xal_Barcode_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_Barcode.attributes={xal_Barcode_code, xal_Barcode_mixed, xal_Barcode_type, xal_Barcode_anyAttribute}

# xal_CountryName class attributes and methods
xal_CountryName_mixed: Property = Property(name="mixed", type=StringType)
xal_CountryName_code: Property = Property(name="code", type=StringType)
xal_CountryName_type: Property = Property(name="type", type=StringType)
xal_CountryName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_CountryName.attributes={xal_CountryName_code, xal_CountryName_anyAttribute, xal_CountryName_mixed, xal_CountryName_type}

# xal_DepartmentName class attributes and methods
xal_DepartmentName_mixed: Property = Property(name="mixed", type=StringType)
xal_DepartmentName_code: Property = Property(name="code", type=StringType)
xal_DepartmentName_type: Property = Property(name="type", type=StringType)
xal_DepartmentName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_DepartmentName.attributes={xal_DepartmentName_code, xal_DepartmentName_type, xal_DepartmentName_anyAttribute, xal_DepartmentName_mixed}

# xal_MailStop class attributes and methods
xal_MailStop_any: Property = Property(name="any", type=StringType)
xal_MailStop_type: Property = Property(name="type", type=StringType)
xal_MailStop_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_MailStop.attributes={xal_MailStop_any, xal_MailStop_type, xal_MailStop_anyAttribute}

# xal_Department class attributes and methods
xal_Department_any: Property = Property(name="any", type=StringType)
xal_Department_type: Property = Property(name="type", type=StringType)
xal_Department_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_Department.attributes={xal_Department_any, xal_Department_anyAttribute, xal_Department_type}

# xal_DependentLocality class attributes and methods
xal_DependentLocality_any: Property = Property(name="any", type=StringType)
xal_DependentLocality_connector: Property = Property(name="connector", type=StringType)
xal_DependentLocality_indicator: Property = Property(name="indicator", type=StringType)
xal_DependentLocality_type: Property = Property(name="type", type=StringType)
xal_DependentLocality_usageType: Property = Property(name="usageType", type=StringType)
xal_DependentLocality_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_DependentLocality.attributes={xal_DependentLocality_anyAttribute, xal_DependentLocality_any, xal_DependentLocality_indicator, xal_DependentLocality_connector, xal_DependentLocality_type, xal_DependentLocality_usageType}

# xal_DependentLocalityName class attributes and methods
xal_DependentLocalityName_code: Property = Property(name="code", type=StringType)
xal_DependentLocalityName_type: Property = Property(name="type", type=StringType)
xal_DependentLocalityName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_DependentLocalityName_mixed: Property = Property(name="mixed", type=StringType)
xal_DependentLocalityName.attributes={xal_DependentLocalityName_type, xal_DependentLocalityName_mixed, xal_DependentLocalityName_anyAttribute, xal_DependentLocalityName_code}

# xal_DependentLocalityNumber class attributes and methods
xal_DependentLocalityNumber_mixed: Property = Property(name="mixed", type=StringType)
xal_DependentLocalityNumber_code: Property = Property(name="code", type=StringType)
xal_DependentLocalityNumber_nameNumberOccurrence: Property = Property(name="nameNumberOccurrence", type=StringType)
xal_DependentLocalityNumber_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_DependentLocalityNumber.attributes={xal_DependentLocalityNumber_anyAttribute, xal_DependentLocalityNumber_code, xal_DependentLocalityNumber_nameNumberOccurrence, xal_DependentLocalityNumber_mixed}

# xal_PostBox class attributes and methods
xal_PostBox_any: Property = Property(name="any", type=StringType)
xal_PostBox_indicator: Property = Property(name="indicator", type=StringType)
xal_PostBox_type: Property = Property(name="type", type=StringType)
xal_PostBox_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostBox.attributes={xal_PostBox_anyAttribute, xal_PostBox_indicator, xal_PostBox_any, xal_PostBox_type}

# xal_Premise class attributes and methods
xal_Premise_any: Property = Property(name="any", type=StringType)
xal_Premise_premiseDependency: Property = Property(name="premiseDependency", type=StringType)
xal_Premise_premiseDependencyType: Property = Property(name="premiseDependencyType", type=StringType)
xal_Premise_premiseThoroughfareConnector: Property = Property(name="premiseThoroughfareConnector", type=StringType)
xal_Premise_type: Property = Property(name="type", type=StringType)
xal_Premise_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_Premise.attributes={xal_Premise_type, xal_Premise_premiseDependencyType, xal_Premise_anyAttribute, xal_Premise_premiseThoroughfareConnector, xal_Premise_premiseDependency, xal_Premise_any}

# xal_LargeMailUser class attributes and methods
xal_LargeMailUser_any: Property = Property(name="any", type=StringType)
xal_LargeMailUser_type: Property = Property(name="type", type=StringType)
xal_LargeMailUser_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_LargeMailUser.attributes={xal_LargeMailUser_type, xal_LargeMailUser_any, xal_LargeMailUser_anyAttribute}

# xal_PostalRoute class attributes and methods
xal_PostalRoute_any: Property = Property(name="any", type=StringType)
xal_PostalRoute_type: Property = Property(name="type", type=StringType)
xal_PostalRoute_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostalRoute.attributes={xal_PostalRoute_type, xal_PostalRoute_anyAttribute, xal_PostalRoute_any}

# xal_ThoroughfareName class attributes and methods
xal_ThoroughfareName_mixed: Property = Property(name="mixed", type=StringType)
xal_ThoroughfareName_code: Property = Property(name="code", type=StringType)
xal_ThoroughfareName_type: Property = Property(name="type", type=StringType)
xal_ThoroughfareName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfareName.attributes={xal_ThoroughfareName_anyAttribute, xal_ThoroughfareName_code, xal_ThoroughfareName_mixed, xal_ThoroughfareName_type}

# xal_ThoroughfareTrailingType class attributes and methods
xal_ThoroughfareTrailingType_mixed: Property = Property(name="mixed", type=StringType)
xal_ThoroughfareTrailingType_code: Property = Property(name="code", type=StringType)
xal_ThoroughfareTrailingType_type: Property = Property(name="type", type=StringType)
xal_ThoroughfareTrailingType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfareTrailingType.attributes={xal_ThoroughfareTrailingType_anyAttribute, xal_ThoroughfareTrailingType_mixed, xal_ThoroughfareTrailingType_type, xal_ThoroughfareTrailingType_code}

# xal_ThoroughfarePostDirection class attributes and methods
xal_ThoroughfarePostDirection_mixed: Property = Property(name="mixed", type=StringType)
xal_ThoroughfarePostDirection_code: Property = Property(name="code", type=StringType)
xal_ThoroughfarePostDirection_type: Property = Property(name="type", type=StringType)
xal_ThoroughfarePostDirection_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfarePostDirection.attributes={xal_ThoroughfarePostDirection_anyAttribute, xal_ThoroughfarePostDirection_type, xal_ThoroughfarePostDirection_code, xal_ThoroughfarePostDirection_mixed}

# xal_DependentThoroughfare class attributes and methods
xal_DependentThoroughfare_any: Property = Property(name="any", type=StringType)
xal_DependentThoroughfare_type: Property = Property(name="type", type=StringType)
xal_DependentThoroughfare_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_DependentThoroughfare.attributes={xal_DependentThoroughfare_type, xal_DependentThoroughfare_anyAttribute, xal_DependentThoroughfare_any}

# xal_ThoroughfarePreDirection class attributes and methods
xal_ThoroughfarePreDirection_mixed: Property = Property(name="mixed", type=StringType)
xal_ThoroughfarePreDirection_code: Property = Property(name="code", type=StringType)
xal_ThoroughfarePreDirection_type: Property = Property(name="type", type=StringType)
xal_ThoroughfarePreDirection_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfarePreDirection.attributes={xal_ThoroughfarePreDirection_code, xal_ThoroughfarePreDirection_anyAttribute, xal_ThoroughfarePreDirection_mixed, xal_ThoroughfarePreDirection_type}

# xal_ThoroughfareLeadingType class attributes and methods
xal_ThoroughfareLeadingType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfareLeadingType_mixed: Property = Property(name="mixed", type=StringType)
xal_ThoroughfareLeadingType_code: Property = Property(name="code", type=StringType)
xal_ThoroughfareLeadingType_type: Property = Property(name="type", type=StringType)
xal_ThoroughfareLeadingType.attributes={xal_ThoroughfareLeadingType_anyAttribute, xal_ThoroughfareLeadingType_code, xal_ThoroughfareLeadingType_mixed, xal_ThoroughfareLeadingType_type}

# xal_EStringToStringMapEntry class attributes and methods

# xal_DocumentRoot class attributes and methods
xal_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
xal_DocumentRoot.attributes={xal_DocumentRoot_mixed}

# xal_ThoroughfareNumber class attributes and methods
xal_ThoroughfareNumber_code: Property = Property(name="code", type=StringType)
xal_ThoroughfareNumber_indicator: Property = Property(name="indicator", type=StringType)
xal_ThoroughfareNumber_indicatorOccurrence: Property = Property(name="indicatorOccurrence", type=StringType)
xal_ThoroughfareNumber_numberOccurrence: Property = Property(name="numberOccurrence", type=StringType)
xal_ThoroughfareNumber_numberType: Property = Property(name="numberType", type=StringType)
xal_ThoroughfareNumber_mixed: Property = Property(name="mixed", type=StringType)
xal_ThoroughfareNumber_type: Property = Property(name="type", type=StringType)
xal_ThoroughfareNumber_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfareNumber.attributes={xal_ThoroughfareNumber_anyAttribute, xal_ThoroughfareNumber_indicatorOccurrence, xal_ThoroughfareNumber_code, xal_ThoroughfareNumber_indicator, xal_ThoroughfareNumber_type, xal_ThoroughfareNumber_numberType, xal_ThoroughfareNumber_numberOccurrence, xal_ThoroughfareNumber_mixed}

# xal_ThoroughfareNumberPrefix class attributes and methods
xal_ThoroughfareNumberPrefix_mixed: Property = Property(name="mixed", type=StringType)
xal_ThoroughfareNumberPrefix_numberPrefixSeparator: Property = Property(name="numberPrefixSeparator", type=StringType)
xal_ThoroughfareNumberPrefix_type: Property = Property(name="type", type=StringType)
xal_ThoroughfareNumberPrefix_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfareNumberPrefix_code: Property = Property(name="code", type=StringType)
xal_ThoroughfareNumberPrefix.attributes={xal_ThoroughfareNumberPrefix_type, xal_ThoroughfareNumberPrefix_code, xal_ThoroughfareNumberPrefix_mixed, xal_ThoroughfareNumberPrefix_anyAttribute, xal_ThoroughfareNumberPrefix_numberPrefixSeparator}

# xal_ThoroughfareNumberSuffix class attributes and methods
xal_ThoroughfareNumberSuffix_mixed: Property = Property(name="mixed", type=StringType)
xal_ThoroughfareNumberSuffix_code: Property = Property(name="code", type=StringType)
xal_ThoroughfareNumberSuffix_numberSuffixSeparator: Property = Property(name="numberSuffixSeparator", type=StringType)
xal_ThoroughfareNumberSuffix_type: Property = Property(name="type", type=StringType)
xal_ThoroughfareNumberSuffix_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfareNumberSuffix.attributes={xal_ThoroughfareNumberSuffix_numberSuffixSeparator, xal_ThoroughfareNumberSuffix_type, xal_ThoroughfareNumberSuffix_mixed, xal_ThoroughfareNumberSuffix_code, xal_ThoroughfareNumberSuffix_anyAttribute}

# xal_PremiseNumber class attributes and methods
xal_PremiseNumber_mixed: Property = Property(name="mixed", type=StringType)
xal_PremiseNumber_code: Property = Property(name="code", type=StringType)
xal_PremiseNumber_indicator: Property = Property(name="indicator", type=StringType)
xal_PremiseNumber_indicatorOccurrence: Property = Property(name="indicatorOccurrence", type=StringType)
xal_PremiseNumber_numberType: Property = Property(name="numberType", type=StringType)
xal_PremiseNumber_numberTypeOccurrence: Property = Property(name="numberTypeOccurrence", type=StringType)
xal_PremiseNumber_type: Property = Property(name="type", type=StringType)
xal_PremiseNumber_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PremiseNumber.attributes={xal_PremiseNumber_type, xal_PremiseNumber_indicator, xal_PremiseNumber_anyAttribute, xal_PremiseNumber_mixed, xal_PremiseNumber_numberType, xal_PremiseNumber_code, xal_PremiseNumber_numberTypeOccurrence, xal_PremiseNumber_indicatorOccurrence}

# xal_PremiseNumberPrefix class attributes and methods
xal_PremiseNumberPrefix_value: Property = Property(name="value", type=StringType)
xal_PremiseNumberPrefix_code: Property = Property(name="code", type=StringType)
xal_PremiseNumberPrefix_numberPrefixSeparator: Property = Property(name="numberPrefixSeparator", type=StringType)
xal_PremiseNumberPrefix_type: Property = Property(name="type", type=StringType)
xal_PremiseNumberPrefix_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PremiseNumberPrefix.attributes={xal_PremiseNumberPrefix_value, xal_PremiseNumberPrefix_anyAttribute, xal_PremiseNumberPrefix_code, xal_PremiseNumberPrefix_type, xal_PremiseNumberPrefix_numberPrefixSeparator}

# xal_PremiseNumberSuffix class attributes and methods
xal_PremiseNumberSuffix_mixed: Property = Property(name="mixed", type=StringType)
xal_PremiseNumberSuffix_code: Property = Property(name="code", type=StringType)
xal_PremiseNumberSuffix_numberSuffixSeparator: Property = Property(name="numberSuffixSeparator", type=StringType)
xal_PremiseNumberSuffix_type: Property = Property(name="type", type=StringType)
xal_PremiseNumberSuffix_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PremiseNumberSuffix.attributes={xal_PremiseNumberSuffix_mixed, xal_PremiseNumberSuffix_code, xal_PremiseNumberSuffix_numberSuffixSeparator, xal_PremiseNumberSuffix_anyAttribute, xal_PremiseNumberSuffix_type}

# xal_Firm class attributes and methods
xal_Firm_any: Property = Property(name="any", type=StringType)
xal_Firm_type: Property = Property(name="type", type=StringType)
xal_Firm_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_Firm.attributes={xal_Firm_anyAttribute, xal_Firm_type, xal_Firm_any}

# xal_FirmName class attributes and methods
xal_FirmName_mixed: Property = Property(name="mixed", type=StringType)
xal_FirmName_code: Property = Property(name="code", type=StringType)
xal_FirmName_type: Property = Property(name="type", type=StringType)
xal_FirmName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_FirmName.attributes={xal_FirmName_anyAttribute, xal_FirmName_code, xal_FirmName_mixed, xal_FirmName_type}

# xal_Xal class attributes and methods
xal_Xal_version: Property = Property(name="version", type=StringType)
xal_Xal_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_Xal_any: Property = Property(name="any", type=StringType)
xal_Xal.attributes={xal_Xal_version, xal_Xal_anyAttribute, xal_Xal_any}

# xal_EndorsementLineCode class attributes and methods
xal_EndorsementLineCode_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_EndorsementLineCode_mixed: Property = Property(name="mixed", type=StringType)
xal_EndorsementLineCode_code: Property = Property(name="code", type=StringType)
xal_EndorsementLineCode_type: Property = Property(name="type", type=StringType)
xal_EndorsementLineCode.attributes={xal_EndorsementLineCode_anyAttribute, xal_EndorsementLineCode_code, xal_EndorsementLineCode_type, xal_EndorsementLineCode_mixed}

# xal_KeyLineCode class attributes and methods
xal_KeyLineCode_mixed: Property = Property(name="mixed", type=StringType)
xal_KeyLineCode_code: Property = Property(name="code", type=StringType)
xal_KeyLineCode_type: Property = Property(name="type", type=StringType)
xal_KeyLineCode_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_KeyLineCode.attributes={xal_KeyLineCode_code, xal_KeyLineCode_mixed, xal_KeyLineCode_type, xal_KeyLineCode_anyAttribute}

# xal_LargeMailUserName class attributes and methods
xal_LargeMailUserName_mixed: Property = Property(name="mixed", type=StringType)
xal_LargeMailUserName_code: Property = Property(name="code", type=StringType)
xal_LargeMailUserName_type: Property = Property(name="type", type=StringType)
xal_LargeMailUserName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_LargeMailUserName.attributes={xal_LargeMailUserName_type, xal_LargeMailUserName_anyAttribute, xal_LargeMailUserName_code, xal_LargeMailUserName_mixed}

# xal_LargeMailUserIdentifier class attributes and methods
xal_LargeMailUserIdentifier_mixed: Property = Property(name="mixed", type=StringType)
xal_LargeMailUserIdentifier_code: Property = Property(name="code", type=StringType)
xal_LargeMailUserIdentifier_indicator: Property = Property(name="indicator", type=StringType)
xal_LargeMailUserIdentifier_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_LargeMailUserIdentifier_type: Property = Property(name="type", type=StringType)
xal_LargeMailUserIdentifier.attributes={xal_LargeMailUserIdentifier_mixed, xal_LargeMailUserIdentifier_code, xal_LargeMailUserIdentifier_anyAttribute, xal_LargeMailUserIdentifier_indicator, xal_LargeMailUserIdentifier_type}

# xal_LocalityName class attributes and methods
xal_LocalityName_mixed: Property = Property(name="mixed", type=StringType)
xal_LocalityName_code: Property = Property(name="code", type=StringType)
xal_LocalityName_type: Property = Property(name="type", type=StringType)
xal_LocalityName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_LocalityName.attributes={xal_LocalityName_anyAttribute, xal_LocalityName_type, xal_LocalityName_mixed, xal_LocalityName_code}

# xal_MailStopName class attributes and methods
xal_MailStopName_mixed: Property = Property(name="mixed", type=StringType)
xal_MailStopName_code: Property = Property(name="code", type=StringType)
xal_MailStopName_type: Property = Property(name="type", type=StringType)
xal_MailStopName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_MailStopName.attributes={xal_MailStopName_mixed, xal_MailStopName_anyAttribute, xal_MailStopName_type, xal_MailStopName_code}

# xal_MailStopNumber class attributes and methods
xal_MailStopNumber_mixed: Property = Property(name="mixed", type=StringType)
xal_MailStopNumber_code: Property = Property(name="code", type=StringType)
xal_MailStopNumber_nameNumberSeparator: Property = Property(name="nameNumberSeparator", type=StringType)
xal_MailStopNumber_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_MailStopNumber.attributes={xal_MailStopNumber_anyAttribute, xal_MailStopNumber_nameNumberSeparator, xal_MailStopNumber_code, xal_MailStopNumber_mixed}

# xal_PostalCodeNumber class attributes and methods
xal_PostalCodeNumber_code: Property = Property(name="code", type=StringType)
xal_PostalCodeNumber_type: Property = Property(name="type", type=StringType)
xal_PostalCodeNumber_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostalCodeNumber_mixed: Property = Property(name="mixed", type=StringType)
xal_PostalCodeNumber.attributes={xal_PostalCodeNumber_code, xal_PostalCodeNumber_type, xal_PostalCodeNumber_anyAttribute, xal_PostalCodeNumber_mixed}

# xal_PostalCodeNumberExtension class attributes and methods
xal_PostalCodeNumberExtension_mixed: Property = Property(name="mixed", type=StringType)
xal_PostalCodeNumberExtension_code: Property = Property(name="code", type=StringType)
xal_PostalCodeNumberExtension_numberExtensionSeparator: Property = Property(name="numberExtensionSeparator", type=StringType)
xal_PostalCodeNumberExtension_type: Property = Property(name="type", type=StringType)
xal_PostalCodeNumberExtension_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostalCodeNumberExtension.attributes={xal_PostalCodeNumberExtension_code, xal_PostalCodeNumberExtension_anyAttribute, xal_PostalCodeNumberExtension_mixed, xal_PostalCodeNumberExtension_type, xal_PostalCodeNumberExtension_numberExtensionSeparator}

# xal_PostTown class attributes and methods
xal_PostTown_type: Property = Property(name="type", type=StringType)
xal_PostTown_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostTown.attributes={xal_PostTown_anyAttribute, xal_PostTown_type}

# xal_PostalRouteNumber class attributes and methods
xal_PostalRouteNumber_code: Property = Property(name="code", type=StringType)
xal_PostalRouteNumber_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostalRouteNumber_mixed: Property = Property(name="mixed", type=StringType)
xal_PostalRouteNumber.attributes={xal_PostalRouteNumber_code, xal_PostalRouteNumber_anyAttribute, xal_PostalRouteNumber_mixed}

# xal_PostalRouteName class attributes and methods
xal_PostalRouteName_mixed: Property = Property(name="mixed", type=StringType)
xal_PostalRouteName_code: Property = Property(name="code", type=StringType)
xal_PostalRouteName_type: Property = Property(name="type", type=StringType)
xal_PostalRouteName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostalRouteName.attributes={xal_PostalRouteName_code, xal_PostalRouteName_anyAttribute, xal_PostalRouteName_type, xal_PostalRouteName_mixed}

# xal_SortingCode class attributes and methods
xal_SortingCode_code: Property = Property(name="code", type=StringType)
xal_SortingCode_type: Property = Property(name="type", type=StringType)
xal_SortingCode.attributes={xal_SortingCode_type, xal_SortingCode_code}

# xal_SupplementaryPostalServiceData class attributes and methods
xal_SupplementaryPostalServiceData_mixed: Property = Property(name="mixed", type=StringType)
xal_SupplementaryPostalServiceData_code: Property = Property(name="code", type=StringType)
xal_SupplementaryPostalServiceData_type: Property = Property(name="type", type=StringType)
xal_SupplementaryPostalServiceData_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_SupplementaryPostalServiceData.attributes={xal_SupplementaryPostalServiceData_mixed, xal_SupplementaryPostalServiceData_anyAttribute, xal_SupplementaryPostalServiceData_type, xal_SupplementaryPostalServiceData_code}

# xal_PostBoxNumber class attributes and methods
xal_PostBoxNumber_mixed: Property = Property(name="mixed", type=StringType)
xal_PostBoxNumber_code: Property = Property(name="code", type=StringType)
xal_PostBoxNumber_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostBoxNumber.attributes={xal_PostBoxNumber_anyAttribute, xal_PostBoxNumber_mixed, xal_PostBoxNumber_code}

# xal_PostBoxNumberPrefix class attributes and methods
xal_PostBoxNumberPrefix_mixed: Property = Property(name="mixed", type=StringType)
xal_PostBoxNumberPrefix_code: Property = Property(name="code", type=StringType)
xal_PostBoxNumberPrefix_numberPrefixSeparator: Property = Property(name="numberPrefixSeparator", type=StringType)
xal_PostBoxNumberPrefix_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostBoxNumberPrefix.attributes={xal_PostBoxNumberPrefix_code, xal_PostBoxNumberPrefix_numberPrefixSeparator, xal_PostBoxNumberPrefix_mixed, xal_PostBoxNumberPrefix_anyAttribute}

# xal_PostBoxNumberSuffix class attributes and methods
xal_PostBoxNumberSuffix_mixed: Property = Property(name="mixed", type=StringType)
xal_PostBoxNumberSuffix_code: Property = Property(name="code", type=StringType)
xal_PostBoxNumberSuffix_numberSuffixSeparator: Property = Property(name="numberSuffixSeparator", type=StringType)
xal_PostBoxNumberSuffix_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostBoxNumberSuffix.attributes={xal_PostBoxNumberSuffix_mixed, xal_PostBoxNumberSuffix_code, xal_PostBoxNumberSuffix_numberSuffixSeparator, xal_PostBoxNumberSuffix_anyAttribute}

# xal_PostBoxNumberExtension class attributes and methods
xal_PostBoxNumberExtension_mixed: Property = Property(name="mixed", type=StringType)
xal_PostBoxNumberExtension_numberExtensionSeparator: Property = Property(name="numberExtensionSeparator", type=StringType)
xal_PostBoxNumberExtension_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostBoxNumberExtension.attributes={xal_PostBoxNumberExtension_numberExtensionSeparator, xal_PostBoxNumberExtension_anyAttribute, xal_PostBoxNumberExtension_mixed}

# xal_PostOfficeName class attributes and methods
xal_PostOfficeName_mixed: Property = Property(name="mixed", type=StringType)
xal_PostOfficeName_code: Property = Property(name="code", type=StringType)
xal_PostOfficeName_type: Property = Property(name="type", type=StringType)
xal_PostOfficeName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostOfficeName.attributes={xal_PostOfficeName_type, xal_PostOfficeName_mixed, xal_PostOfficeName_code, xal_PostOfficeName_anyAttribute}

# xal_PostOfficeNumber class attributes and methods
xal_PostOfficeNumber_mixed: Property = Property(name="mixed", type=StringType)
xal_PostOfficeNumber_code: Property = Property(name="code", type=StringType)
xal_PostOfficeNumber_indicator: Property = Property(name="indicator", type=StringType)
xal_PostOfficeNumber_indicatorOccurrence: Property = Property(name="indicatorOccurrence", type=StringType)
xal_PostOfficeNumber_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostOfficeNumber.attributes={xal_PostOfficeNumber_mixed, xal_PostOfficeNumber_indicator, xal_PostOfficeNumber_indicatorOccurrence, xal_PostOfficeNumber_code, xal_PostOfficeNumber_anyAttribute}

# xal_PostTownName class attributes and methods
xal_PostTownName_mixed: Property = Property(name="mixed", type=StringType)
xal_PostTownName_code: Property = Property(name="code", type=StringType)
xal_PostTownName_type: Property = Property(name="type", type=StringType)
xal_PostTownName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostTownName.attributes={xal_PostTownName_type, xal_PostTownName_anyAttribute, xal_PostTownName_mixed, xal_PostTownName_code}

# xal_PostTownSuffix class attributes and methods
xal_PostTownSuffix_mixed: Property = Property(name="mixed", type=StringType)
xal_PostTownSuffix_code: Property = Property(name="code", type=StringType)
xal_PostTownSuffix_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PostTownSuffix.attributes={xal_PostTownSuffix_code, xal_PostTownSuffix_mixed, xal_PostTownSuffix_anyAttribute}

# xal_PremiseName class attributes and methods
xal_PremiseName_mixed: Property = Property(name="mixed", type=StringType)
xal_PremiseName_type: Property = Property(name="type", type=StringType)
xal_PremiseName_typeOccurrence: Property = Property(name="typeOccurrence", type=StringType)
xal_PremiseName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PremiseName_code: Property = Property(name="code", type=StringType)
xal_PremiseName.attributes={xal_PremiseName_code, xal_PremiseName_typeOccurrence, xal_PremiseName_type, xal_PremiseName_mixed, xal_PremiseName_anyAttribute}

# xal_PremiseLocation class attributes and methods
xal_PremiseLocation_mixed: Property = Property(name="mixed", type=StringType)
xal_PremiseLocation_code: Property = Property(name="code", type=StringType)
xal_PremiseLocation_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_PremiseLocation.attributes={xal_PremiseLocation_mixed, xal_PremiseLocation_code, xal_PremiseLocation_anyAttribute}

# xal_PremiseNumberRange class attributes and methods
xal_PremiseNumberRange_separator: Property = Property(name="separator", type=StringType)
xal_PremiseNumberRange_indicator: Property = Property(name="indicator", type=StringType)
xal_PremiseNumberRange_indicatorOccurence: Property = Property(name="indicatorOccurence", type=StringType)
xal_PremiseNumberRange_numberRangeOccurence: Property = Property(name="numberRangeOccurence", type=StringType)
xal_PremiseNumberRange_rangeType: Property = Property(name="rangeType", type=StringType)
xal_PremiseNumberRange_type: Property = Property(name="type", type=StringType)
xal_PremiseNumberRange.attributes={xal_PremiseNumberRange_indicatorOccurence, xal_PremiseNumberRange_numberRangeOccurence, xal_PremiseNumberRange_type, xal_PremiseNumberRange_indicator, xal_PremiseNumberRange_rangeType, xal_PremiseNumberRange_separator}

# xal_SubPremise class attributes and methods
xal_SubPremise_any: Property = Property(name="any", type=StringType)
xal_SubPremise_type: Property = Property(name="type", type=StringType)
xal_SubPremise_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_SubPremise.attributes={xal_SubPremise_type, xal_SubPremise_any, xal_SubPremise_anyAttribute}

# xal_PremiseNumberRangeFrom class attributes and methods

# xal_PremiseNumberRangeTo class attributes and methods

# xal_SubAdministrativeAreaName class attributes and methods
xal_SubAdministrativeAreaName_mixed: Property = Property(name="mixed", type=StringType)
xal_SubAdministrativeAreaName_code: Property = Property(name="code", type=StringType)
xal_SubAdministrativeAreaName_type: Property = Property(name="type", type=StringType)
xal_SubAdministrativeAreaName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_SubAdministrativeAreaName.attributes={xal_SubAdministrativeAreaName_type, xal_SubAdministrativeAreaName_mixed, xal_SubAdministrativeAreaName_code, xal_SubAdministrativeAreaName_anyAttribute}

# xal_SubPremiseNumber class attributes and methods
xal_SubPremiseNumber_mixed: Property = Property(name="mixed", type=StringType)
xal_SubPremiseNumber_code: Property = Property(name="code", type=StringType)
xal_SubPremiseNumber_indicator: Property = Property(name="indicator", type=StringType)
xal_SubPremiseNumber_indicatorOccurrence: Property = Property(name="indicatorOccurrence", type=StringType)
xal_SubPremiseNumber_type: Property = Property(name="type", type=StringType)
xal_SubPremiseNumber_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_SubPremiseNumber_numberTypeOccurrence: Property = Property(name="numberTypeOccurrence", type=StringType)
xal_SubPremiseNumber_premiseNumberSeparator: Property = Property(name="premiseNumberSeparator", type=StringType)
xal_SubPremiseNumber.attributes={xal_SubPremiseNumber_indicatorOccurrence, xal_SubPremiseNumber_premiseNumberSeparator, xal_SubPremiseNumber_mixed, xal_SubPremiseNumber_anyAttribute, xal_SubPremiseNumber_type, xal_SubPremiseNumber_code, xal_SubPremiseNumber_numberTypeOccurrence, xal_SubPremiseNumber_indicator}

# xal_SubPremiseNumberPrefix class attributes and methods
xal_SubPremiseNumberPrefix_mixed: Property = Property(name="mixed", type=StringType)
xal_SubPremiseNumberPrefix_code: Property = Property(name="code", type=StringType)
xal_SubPremiseNumberPrefix_numberPrefixSeparator: Property = Property(name="numberPrefixSeparator", type=StringType)
xal_SubPremiseNumberPrefix_type: Property = Property(name="type", type=StringType)
xal_SubPremiseNumberPrefix_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_SubPremiseNumberPrefix.attributes={xal_SubPremiseNumberPrefix_code, xal_SubPremiseNumberPrefix_mixed, xal_SubPremiseNumberPrefix_type, xal_SubPremiseNumberPrefix_numberPrefixSeparator, xal_SubPremiseNumberPrefix_anyAttribute}

# xal_SubPremiseNumberSuffix class attributes and methods
xal_SubPremiseNumberSuffix_mixed: Property = Property(name="mixed", type=StringType)
xal_SubPremiseNumberSuffix_code: Property = Property(name="code", type=StringType)
xal_SubPremiseNumberSuffix_numberSuffixSeparator: Property = Property(name="numberSuffixSeparator", type=StringType)
xal_SubPremiseNumberSuffix_type: Property = Property(name="type", type=StringType)
xal_SubPremiseNumberSuffix_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_SubPremiseNumberSuffix.attributes={xal_SubPremiseNumberSuffix_mixed, xal_SubPremiseNumberSuffix_type, xal_SubPremiseNumberSuffix_anyAttribute, xal_SubPremiseNumberSuffix_code, xal_SubPremiseNumberSuffix_numberSuffixSeparator}

# xal_SubPremiseName class attributes and methods
xal_SubPremiseName_mixed: Property = Property(name="mixed", type=StringType)
xal_SubPremiseName_type: Property = Property(name="type", type=StringType)
xal_SubPremiseName_typeOccurrence: Property = Property(name="typeOccurrence", type=StringType)
xal_SubPremiseName_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_SubPremiseName_code: Property = Property(name="code", type=StringType)
xal_SubPremiseName.attributes={xal_SubPremiseName_code, xal_SubPremiseName_mixed, xal_SubPremiseName_typeOccurrence, xal_SubPremiseName_type, xal_SubPremiseName_anyAttribute}

# xal_SubPremiseLocation class attributes and methods
xal_SubPremiseLocation_code: Property = Property(name="code", type=StringType)
xal_SubPremiseLocation_mixed: Property = Property(name="mixed", type=StringType)
xal_SubPremiseLocation.attributes={xal_SubPremiseLocation_mixed, xal_SubPremiseLocation_code}

# xal_ThoroughfareNumberRange class attributes and methods
xal_ThoroughfareNumberRange_code: Property = Property(name="code", type=StringType)
xal_ThoroughfareNumberRange_indicator: Property = Property(name="indicator", type=StringType)
xal_ThoroughfareNumberRange_indicatorOccurrence: Property = Property(name="indicatorOccurrence", type=StringType)
xal_ThoroughfareNumberRange_numberRangeOccurrence: Property = Property(name="numberRangeOccurrence", type=StringType)
xal_ThoroughfareNumberRange_rangeType: Property = Property(name="rangeType", type=StringType)
xal_ThoroughfareNumberRange_separator: Property = Property(name="separator", type=StringType)
xal_ThoroughfareNumberRange_type: Property = Property(name="type", type=StringType)
xal_ThoroughfareNumberRange_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfareNumberRange.attributes={xal_ThoroughfareNumberRange_numberRangeOccurrence, xal_ThoroughfareNumberRange_code, xal_ThoroughfareNumberRange_rangeType, xal_ThoroughfareNumberRange_indicatorOccurrence, xal_ThoroughfareNumberRange_indicator, xal_ThoroughfareNumberRange_separator, xal_ThoroughfareNumberRange_anyAttribute, xal_ThoroughfareNumberRange_type}

# xal_ThoroughfareNumberFrom class attributes and methods
xal_ThoroughfareNumberFrom_mixed: Property = Property(name="mixed", type=StringType)
xal_ThoroughfareNumberFrom_code: Property = Property(name="code", type=StringType)
xal_ThoroughfareNumberFrom_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfareNumberFrom.attributes={xal_ThoroughfareNumberFrom_anyAttribute, xal_ThoroughfareNumberFrom_code, xal_ThoroughfareNumberFrom_mixed}

# xal_ThoroughfareNumberTo class attributes and methods
xal_ThoroughfareNumberTo_mixed: Property = Property(name="mixed", type=StringType)
xal_ThoroughfareNumberTo_code: Property = Property(name="code", type=StringType)
xal_ThoroughfareNumberTo_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
xal_ThoroughfareNumberTo.attributes={xal_ThoroughfareNumberTo_code, xal_ThoroughfareNumberTo_mixed, xal_ThoroughfareNumberTo_anyAttribute}

# Relationships
postalServiceElements0: BinaryAssociation = BinaryAssociation(
    name="postalServiceElements0",
    ends={
        Property(name="xal_PostalServiceElements", type=xal_AddressDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AddressDetails", type=xal_PostalServiceElements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address1: BinaryAssociation = BinaryAssociation(
    name="address1",
    ends={
        Property(name="xal_Address", type=xal_AddressDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AddressDetails2", type=xal_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLines3: BinaryAssociation = BinaryAssociation(
    name="addressLines3",
    ends={
        Property(name="xal_AddressLines", type=xal_AddressDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AddressDetails4", type=xal_AddressLines, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
country5: BinaryAssociation = BinaryAssociation(
    name="country5",
    ends={
        Property(name="xal_Country", type=xal_AddressDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AddressDetails6", type=xal_Country, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
administrativeArea7: BinaryAssociation = BinaryAssociation(
    name="administrativeArea7",
    ends={
        Property(name="xal_AdministrativeArea", type=xal_AddressDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AddressDetails8", type=xal_AdministrativeArea, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
locality9: BinaryAssociation = BinaryAssociation(
    name="locality9",
    ends={
        Property(name="xal_Locality", type=xal_AddressDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AddressDetails10", type=xal_Locality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfare11: BinaryAssociation = BinaryAssociation(
    name="thoroughfare11",
    ends={
        Property(name="xal_Thoroughfare", type=xal_AddressDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AddressDetails12", type=xal_Thoroughfare, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine13: BinaryAssociation = BinaryAssociation(
    name="addressLine13",
    ends={
        Property(name="xal_AddressLine", type=xal_AddressLines, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AddressLines14", type=xal_AddressLine, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subAdministrativeArea20: BinaryAssociation = BinaryAssociation(
    name="subAdministrativeArea20",
    ends={
        Property(name="xal_SubAdministrativeArea", type=xal_AdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AdministrativeArea21", type=xal_SubAdministrativeArea, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
locality22: BinaryAssociation = BinaryAssociation(
    name="locality22",
    ends={
        Property(name="xal_Locality24", type=xal_AdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AdministrativeArea23", type=xal_Locality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postOffice25: BinaryAssociation = BinaryAssociation(
    name="postOffice25",
    ends={
        Property(name="xal_PostOffice", type=xal_AdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AdministrativeArea26", type=xal_PostOffice, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine15: BinaryAssociation = BinaryAssociation(
    name="addressLine15",
    ends={
        Property(name="xal_AddressLine17", type=xal_AdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AdministrativeArea16", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
administrativeAreaName18: BinaryAssociation = BinaryAssociation(
    name="administrativeAreaName18",
    ends={
        Property(name="xal_AdministrativeAreaName", type=xal_AdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AdministrativeArea19", type=xal_AdministrativeAreaName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postalCode27: BinaryAssociation = BinaryAssociation(
    name="postalCode27",
    ends={
        Property(name="xal_PostalCode", type=xal_AdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_AdministrativeArea28", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine29: BinaryAssociation = BinaryAssociation(
    name="addressLine29",
    ends={
        Property(name="xal_AddressLine31", type=xal_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Country30", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
countryNameCode32: BinaryAssociation = BinaryAssociation(
    name="countryNameCode32",
    ends={
        Property(name="xal_CountryNameCode", type=xal_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Country33", type=xal_CountryNameCode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
countryName34: BinaryAssociation = BinaryAssociation(
    name="countryName34",
    ends={
        Property(name="xal_CountryName", type=xal_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Country35", type=xal_CountryName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
administrativeArea36: BinaryAssociation = BinaryAssociation(
    name="administrativeArea36",
    ends={
        Property(name="xal_AdministrativeArea38", type=xal_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Country37", type=xal_AdministrativeArea, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
locality39: BinaryAssociation = BinaryAssociation(
    name="locality39",
    ends={
        Property(name="xal_Locality41", type=xal_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Country40", type=xal_Locality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfare42: BinaryAssociation = BinaryAssociation(
    name="thoroughfare42",
    ends={
        Property(name="xal_Thoroughfare44", type=xal_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Country43", type=xal_Thoroughfare, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
departmentName47: BinaryAssociation = BinaryAssociation(
    name="departmentName47",
    ends={
        Property(name="xal_DepartmentName", type=xal_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Department48", type=xal_DepartmentName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mailStop49: BinaryAssociation = BinaryAssociation(
    name="mailStop49",
    ends={
        Property(name="xal_MailStop", type=xal_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Department50", type=xal_MailStop, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode51: BinaryAssociation = BinaryAssociation(
    name="postalCode51",
    ends={
        Property(name="xal_PostalCode53", type=xal_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Department52", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine45: BinaryAssociation = BinaryAssociation(
    name="addressLine45",
    ends={
        Property(name="xal_AddressLine46", type=xal_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Department", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressLine54: BinaryAssociation = BinaryAssociation(
    name="addressLine54",
    ends={
        Property(name="xal_AddressLine55", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependentLocalityName56: BinaryAssociation = BinaryAssociation(
    name="dependentLocalityName56",
    ends={
        Property(name="xal_DependentLocalityName", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality57", type=xal_DependentLocalityName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependentLocalityNumber58: BinaryAssociation = BinaryAssociation(
    name="dependentLocalityNumber58",
    ends={
        Property(name="xal_DependentLocalityNumber", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality59", type=xal_DependentLocalityNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postBox60: BinaryAssociation = BinaryAssociation(
    name="postBox60",
    ends={
        Property(name="xal_PostBox", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality61", type=xal_PostBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
premise72: BinaryAssociation = BinaryAssociation(
    name="premise72",
    ends={
        Property(name="xal_Premise", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality73", type=xal_Premise, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependentLocality75: BinaryAssociation = BinaryAssociation(
    name="dependentLocality75",
    ends={
        Property(name="xal_DependentLocality76", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality74", type=xal_DependentLocality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode77: BinaryAssociation = BinaryAssociation(
    name="postalCode77",
    ends={
        Property(name="xal_PostalCode79", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality78", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
largeMailUser62: BinaryAssociation = BinaryAssociation(
    name="largeMailUser62",
    ends={
        Property(name="xal_LargeMailUser", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality63", type=xal_LargeMailUser, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postOffice64: BinaryAssociation = BinaryAssociation(
    name="postOffice64",
    ends={
        Property(name="xal_PostOffice66", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality65", type=xal_PostOffice, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalRoute67: BinaryAssociation = BinaryAssociation(
    name="postalRoute67",
    ends={
        Property(name="xal_PostalRoute", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality68", type=xal_PostalRoute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfare69: BinaryAssociation = BinaryAssociation(
    name="thoroughfare69",
    ends={
        Property(name="xal_Thoroughfare71", type=xal_DependentLocality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentLocality70", type=xal_Thoroughfare, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfareName86: BinaryAssociation = BinaryAssociation(
    name="thoroughfareName86",
    ends={
        Property(name="xal_ThoroughfareName", type=xal_DependentThoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentThoroughfare87", type=xal_ThoroughfareName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareTrailingType88: BinaryAssociation = BinaryAssociation(
    name="thoroughfareTrailingType88",
    ends={
        Property(name="xal_ThoroughfareTrailingType", type=xal_DependentThoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentThoroughfare89", type=xal_ThoroughfareTrailingType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfarePostDirection90: BinaryAssociation = BinaryAssociation(
    name="thoroughfarePostDirection90",
    ends={
        Property(name="xal_ThoroughfarePostDirection", type=xal_DependentThoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentThoroughfare91", type=xal_ThoroughfarePostDirection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine80: BinaryAssociation = BinaryAssociation(
    name="addressLine80",
    ends={
        Property(name="xal_AddressLine81", type=xal_DependentThoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentThoroughfare", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfarePreDirection82: BinaryAssociation = BinaryAssociation(
    name="thoroughfarePreDirection82",
    ends={
        Property(name="xal_ThoroughfarePreDirection", type=xal_DependentThoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentThoroughfare83", type=xal_ThoroughfarePreDirection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfareLeadingType84: BinaryAssociation = BinaryAssociation(
    name="thoroughfareLeadingType84",
    ends={
        Property(name="xal_ThoroughfareLeadingType", type=xal_DependentThoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DependentThoroughfare85", type=xal_ThoroughfareLeadingType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xMLNSPrefixMap92: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap92",
    ends={
        Property(name="xal_EStringToStringMapEntry", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot", type=xal_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation93: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation93",
    ends={
        Property(name="xal_EStringToStringMapEntry95", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot94", type=xal_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressDetails96: BinaryAssociation = BinaryAssociation(
    name="addressDetails96",
    ends={
        Property(name="xal_AddressDetails98", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot97", type=xal_AddressDetails, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressLine99: BinaryAssociation = BinaryAssociation(
    name="addressLine99",
    ends={
        Property(name="xal_AddressLine101", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot100", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
administrativeArea102: BinaryAssociation = BinaryAssociation(
    name="administrativeArea102",
    ends={
        Property(name="xal_AdministrativeArea104", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot103", type=xal_AdministrativeArea, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postalCode114: BinaryAssociation = BinaryAssociation(
    name="postalCode114",
    ends={
        Property(name="xal_PostalCode116", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot115", type=xal_PostalCode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postBox117: BinaryAssociation = BinaryAssociation(
    name="postBox117",
    ends={
        Property(name="xal_PostBox119", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot118", type=xal_PostBox, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postOffice120: BinaryAssociation = BinaryAssociation(
    name="postOffice120",
    ends={
        Property(name="xal_PostOffice122", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot121", type=xal_PostOffice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premise123: BinaryAssociation = BinaryAssociation(
    name="premise123",
    ends={
        Property(name="xal_Premise125", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot124", type=xal_Premise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
countryName105: BinaryAssociation = BinaryAssociation(
    name="countryName105",
    ends={
        Property(name="xal_CountryName107", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot106", type=xal_CountryName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department108: BinaryAssociation = BinaryAssociation(
    name="department108",
    ends={
        Property(name="xal_Department110", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot109", type=xal_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locality111: BinaryAssociation = BinaryAssociation(
    name="locality111",
    ends={
        Property(name="xal_Locality113", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot112", type=xal_Locality, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfare132: BinaryAssociation = BinaryAssociation(
    name="thoroughfare132",
    ends={
        Property(name="xal_Thoroughfare134", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot133", type=xal_Thoroughfare, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareNumber135: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumber135",
    ends={
        Property(name="xal_ThoroughfareNumber", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot136", type=xal_ThoroughfareNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareNumberPrefix137: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberPrefix137",
    ends={
        Property(name="xal_ThoroughfareNumberPrefix", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot138", type=xal_ThoroughfareNumberPrefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareNumberSuffix139: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberSuffix139",
    ends={
        Property(name="xal_ThoroughfareNumberSuffix", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot140", type=xal_ThoroughfareNumberSuffix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseNumber126: BinaryAssociation = BinaryAssociation(
    name="premiseNumber126",
    ends={
        Property(name="xal_PremiseNumber", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot127", type=xal_PremiseNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseNumberPrefix128: BinaryAssociation = BinaryAssociation(
    name="premiseNumberPrefix128",
    ends={
        Property(name="xal_PremiseNumberPrefix", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot129", type=xal_PremiseNumberPrefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseNumberSuffix130: BinaryAssociation = BinaryAssociation(
    name="premiseNumberSuffix130",
    ends={
        Property(name="xal_PremiseNumberSuffix", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot131", type=xal_PremiseNumberSuffix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressLine143: BinaryAssociation = BinaryAssociation(
    name="addressLine143",
    ends={
        Property(name="xal_AddressLine144", type=xal_Firm, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Firm", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firmName145: BinaryAssociation = BinaryAssociation(
    name="firmName145",
    ends={
        Property(name="xal_FirmName", type=xal_Firm, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Firm146", type=xal_FirmName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department147: BinaryAssociation = BinaryAssociation(
    name="department147",
    ends={
        Property(name="xal_Department149", type=xal_Firm, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Firm148", type=xal_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xAL141: BinaryAssociation = BinaryAssociation(
    name="xAL141",
    ends={
        Property(name="xal_Xal", type=xal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_DocumentRoot142", type=xal_Xal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mailStop150: BinaryAssociation = BinaryAssociation(
    name="mailStop150",
    ends={
        Property(name="xal_MailStop152", type=xal_Firm, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Firm151", type=xal_MailStop, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode153: BinaryAssociation = BinaryAssociation(
    name="postalCode153",
    ends={
        Property(name="xal_PostalCode155", type=xal_Firm, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Firm154", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine156: BinaryAssociation = BinaryAssociation(
    name="addressLine156",
    ends={
        Property(name="xal_AddressLine158", type=xal_LargeMailUser, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_LargeMailUser157", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
largeMailUserName159: BinaryAssociation = BinaryAssociation(
    name="largeMailUserName159",
    ends={
        Property(name="xal_LargeMailUserName", type=xal_LargeMailUser, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_LargeMailUser160", type=xal_LargeMailUserName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buildingName163: BinaryAssociation = BinaryAssociation(
    name="buildingName163",
    ends={
        Property(name="xal_BuildingName", type=xal_LargeMailUser, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_LargeMailUser164", type=xal_BuildingName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department165: BinaryAssociation = BinaryAssociation(
    name="department165",
    ends={
        Property(name="xal_Department167", type=xal_LargeMailUser, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_LargeMailUser166", type=xal_Department, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postBox168: BinaryAssociation = BinaryAssociation(
    name="postBox168",
    ends={
        Property(name="xal_PostBox170", type=xal_LargeMailUser, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_LargeMailUser169", type=xal_PostBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfare171: BinaryAssociation = BinaryAssociation(
    name="thoroughfare171",
    ends={
        Property(name="xal_Thoroughfare173", type=xal_LargeMailUser, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_LargeMailUser172", type=xal_Thoroughfare, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode174: BinaryAssociation = BinaryAssociation(
    name="postalCode174",
    ends={
        Property(name="xal_PostalCode176", type=xal_LargeMailUser, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_LargeMailUser175", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
largeMailUserIdentifier161: BinaryAssociation = BinaryAssociation(
    name="largeMailUserIdentifier161",
    ends={
        Property(name="xal_LargeMailUserIdentifier", type=xal_LargeMailUser, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_LargeMailUser162", type=xal_LargeMailUserIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine177: BinaryAssociation = BinaryAssociation(
    name="addressLine177",
    ends={
        Property(name="xal_AddressLine179", type=xal_Locality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Locality178", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localityName180: BinaryAssociation = BinaryAssociation(
    name="localityName180",
    ends={
        Property(name="xal_LocalityName", type=xal_Locality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Locality181", type=xal_LocalityName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
largeMailUser185: BinaryAssociation = BinaryAssociation(
    name="largeMailUser185",
    ends={
        Property(name="xal_LargeMailUser187", type=xal_Locality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Locality186", type=xal_LargeMailUser, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postOffice188: BinaryAssociation = BinaryAssociation(
    name="postOffice188",
    ends={
        Property(name="xal_PostOffice190", type=xal_Locality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Locality189", type=xal_PostOffice, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalRoute191: BinaryAssociation = BinaryAssociation(
    name="postalRoute191",
    ends={
        Property(name="xal_PostalRoute193", type=xal_Locality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Locality192", type=xal_PostalRoute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfare194: BinaryAssociation = BinaryAssociation(
    name="thoroughfare194",
    ends={
        Property(name="xal_Thoroughfare196", type=xal_Locality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Locality195", type=xal_Thoroughfare, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
premise197: BinaryAssociation = BinaryAssociation(
    name="premise197",
    ends={
        Property(name="xal_Premise199", type=xal_Locality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Locality198", type=xal_Premise, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependentLocality200: BinaryAssociation = BinaryAssociation(
    name="dependentLocality200",
    ends={
        Property(name="xal_DependentLocality202", type=xal_Locality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Locality201", type=xal_DependentLocality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode203: BinaryAssociation = BinaryAssociation(
    name="postalCode203",
    ends={
        Property(name="xal_PostalCode205", type=xal_Locality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Locality204", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postBox182: BinaryAssociation = BinaryAssociation(
    name="postBox182",
    ends={
        Property(name="xal_PostBox184", type=xal_Locality, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Locality183", type=xal_PostBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine206: BinaryAssociation = BinaryAssociation(
    name="addressLine206",
    ends={
        Property(name="xal_AddressLine208", type=xal_MailStop, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_MailStop207", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mailStopName209: BinaryAssociation = BinaryAssociation(
    name="mailStopName209",
    ends={
        Property(name="xal_MailStopName", type=xal_MailStop, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_MailStop210", type=xal_MailStopName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mailStopNumber211: BinaryAssociation = BinaryAssociation(
    name="mailStopNumber211",
    ends={
        Property(name="xal_MailStopNumber", type=xal_MailStop, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_MailStop212", type=xal_MailStopNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine213: BinaryAssociation = BinaryAssociation(
    name="addressLine213",
    ends={
        Property(name="xal_AddressLine215", type=xal_PostalCode, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalCode214", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postalCodeNumber216: BinaryAssociation = BinaryAssociation(
    name="postalCodeNumber216",
    ends={
        Property(name="xal_PostalCodeNumber", type=xal_PostalCode, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalCode217", type=xal_PostalCodeNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postalCodeNumberExtension218: BinaryAssociation = BinaryAssociation(
    name="postalCodeNumberExtension218",
    ends={
        Property(name="xal_PostalCodeNumberExtension", type=xal_PostalCode, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalCode219", type=xal_PostalCodeNumberExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postTown220: BinaryAssociation = BinaryAssociation(
    name="postTown220",
    ends={
        Property(name="xal_PostTown", type=xal_PostalCode, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalCode221", type=xal_PostTown, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine222: BinaryAssociation = BinaryAssociation(
    name="addressLine222",
    ends={
        Property(name="xal_AddressLine224", type=xal_PostalRoute, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalRoute223", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postalRouteNumber227: BinaryAssociation = BinaryAssociation(
    name="postalRouteNumber227",
    ends={
        Property(name="xal_PostalRouteNumber", type=xal_PostalRoute, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalRoute228", type=xal_PostalRouteNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postBox229: BinaryAssociation = BinaryAssociation(
    name="postBox229",
    ends={
        Property(name="xal_PostBox231", type=xal_PostalRoute, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalRoute230", type=xal_PostBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalRouteName225: BinaryAssociation = BinaryAssociation(
    name="postalRouteName225",
    ends={
        Property(name="xal_PostalRouteName", type=xal_PostalRoute, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalRoute226", type=xal_PostalRouteName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressLongitude246: BinaryAssociation = BinaryAssociation(
    name="addressLongitude246",
    ends={
        Property(name="xal_AddressLongitude", type=xal_PostalServiceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalServiceElements247", type=xal_AddressLongitude, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressIdentifier232: BinaryAssociation = BinaryAssociation(
    name="addressIdentifier232",
    ends={
        Property(name="xal_AddressIdentifier", type=xal_PostalServiceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalServiceElements233", type=xal_AddressIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endorsementLineCode234: BinaryAssociation = BinaryAssociation(
    name="endorsementLineCode234",
    ends={
        Property(name="xal_EndorsementLineCode", type=xal_PostalServiceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalServiceElements235", type=xal_EndorsementLineCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyLineCode236: BinaryAssociation = BinaryAssociation(
    name="keyLineCode236",
    ends={
        Property(name="xal_KeyLineCode", type=xal_PostalServiceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalServiceElements237", type=xal_KeyLineCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
barcode238: BinaryAssociation = BinaryAssociation(
    name="barcode238",
    ends={
        Property(name="xal_Barcode", type=xal_PostalServiceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalServiceElements239", type=xal_Barcode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sortingCode240: BinaryAssociation = BinaryAssociation(
    name="sortingCode240",
    ends={
        Property(name="xal_SortingCode", type=xal_PostalServiceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalServiceElements241", type=xal_SortingCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLatitude242: BinaryAssociation = BinaryAssociation(
    name="addressLatitude242",
    ends={
        Property(name="xal_AddressLatitude", type=xal_PostalServiceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalServiceElements243", type=xal_AddressLatitude, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLatitudeDirection244: BinaryAssociation = BinaryAssociation(
    name="addressLatitudeDirection244",
    ends={
        Property(name="xal_AddressLatitudeDirection", type=xal_PostalServiceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalServiceElements245", type=xal_AddressLatitudeDirection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLongitudeDirection248: BinaryAssociation = BinaryAssociation(
    name="addressLongitudeDirection248",
    ends={
        Property(name="xal_AddressLongitudeDirection", type=xal_PostalServiceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalServiceElements249", type=xal_AddressLongitudeDirection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
supplementaryPostalServiceData250: BinaryAssociation = BinaryAssociation(
    name="supplementaryPostalServiceData250",
    ends={
        Property(name="xal_SupplementaryPostalServiceData", type=xal_PostalServiceElements, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostalServiceElements251", type=xal_SupplementaryPostalServiceData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressLine252: BinaryAssociation = BinaryAssociation(
    name="addressLine252",
    ends={
        Property(name="xal_AddressLine254", type=xal_PostBox, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostBox253", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postBoxNumber255: BinaryAssociation = BinaryAssociation(
    name="postBoxNumber255",
    ends={
        Property(name="xal_PostBoxNumber", type=xal_PostBox, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostBox256", type=xal_PostBoxNumber, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
postBoxNumberPrefix257: BinaryAssociation = BinaryAssociation(
    name="postBoxNumberPrefix257",
    ends={
        Property(name="xal_PostBoxNumberPrefix", type=xal_PostBox, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostBox258", type=xal_PostBoxNumberPrefix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postBoxNumberSuffix259: BinaryAssociation = BinaryAssociation(
    name="postBoxNumberSuffix259",
    ends={
        Property(name="xal_PostBoxNumberSuffix", type=xal_PostBox, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostBox260", type=xal_PostBoxNumberSuffix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postBoxNumberExtension261: BinaryAssociation = BinaryAssociation(
    name="postBoxNumberExtension261",
    ends={
        Property(name="xal_PostBoxNumberExtension", type=xal_PostBox, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostBox262", type=xal_PostBoxNumberExtension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firm263: BinaryAssociation = BinaryAssociation(
    name="firm263",
    ends={
        Property(name="xal_Firm265", type=xal_PostBox, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostBox264", type=xal_Firm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode266: BinaryAssociation = BinaryAssociation(
    name="postalCode266",
    ends={
        Property(name="xal_PostalCode268", type=xal_PostBox, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostBox267", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine269: BinaryAssociation = BinaryAssociation(
    name="addressLine269",
    ends={
        Property(name="xal_AddressLine271", type=xal_PostOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostOffice270", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postOfficeName272: BinaryAssociation = BinaryAssociation(
    name="postOfficeName272",
    ends={
        Property(name="xal_PostOfficeName", type=xal_PostOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostOffice273", type=xal_PostOfficeName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postOfficeNumber274: BinaryAssociation = BinaryAssociation(
    name="postOfficeNumber274",
    ends={
        Property(name="xal_PostOfficeNumber", type=xal_PostOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostOffice275", type=xal_PostOfficeNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalRoute276: BinaryAssociation = BinaryAssociation(
    name="postalRoute276",
    ends={
        Property(name="xal_PostalRoute278", type=xal_PostOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostOffice277", type=xal_PostalRoute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postBox279: BinaryAssociation = BinaryAssociation(
    name="postBox279",
    ends={
        Property(name="xal_PostBox281", type=xal_PostOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostOffice280", type=xal_PostBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode282: BinaryAssociation = BinaryAssociation(
    name="postalCode282",
    ends={
        Property(name="xal_PostalCode284", type=xal_PostOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostOffice283", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine285: BinaryAssociation = BinaryAssociation(
    name="addressLine285",
    ends={
        Property(name="xal_AddressLine287", type=xal_PostTown, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostTown286", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postTownName288: BinaryAssociation = BinaryAssociation(
    name="postTownName288",
    ends={
        Property(name="xal_PostTownName", type=xal_PostTown, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostTown289", type=xal_PostTownName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postTownSuffix290: BinaryAssociation = BinaryAssociation(
    name="postTownSuffix290",
    ends={
        Property(name="xal_PostTownSuffix", type=xal_PostTown, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PostTown291", type=xal_PostTownSuffix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine292: BinaryAssociation = BinaryAssociation(
    name="addressLine292",
    ends={
        Property(name="xal_AddressLine294", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise293", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseName295: BinaryAssociation = BinaryAssociation(
    name="premiseName295",
    ends={
        Property(name="xal_PremiseName", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise296", type=xal_PremiseName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseLocation297: BinaryAssociation = BinaryAssociation(
    name="premiseLocation297",
    ends={
        Property(name="xal_PremiseLocation", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise298", type=xal_PremiseLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
premiseNumber299: BinaryAssociation = BinaryAssociation(
    name="premiseNumber299",
    ends={
        Property(name="xal_PremiseNumber301", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise300", type=xal_PremiseNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseNumberRange302: BinaryAssociation = BinaryAssociation(
    name="premiseNumberRange302",
    ends={
        Property(name="xal_PremiseNumberRange", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise303", type=xal_PremiseNumberRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
premiseNumberPrefix304: BinaryAssociation = BinaryAssociation(
    name="premiseNumberPrefix304",
    ends={
        Property(name="xal_PremiseNumberPrefix306", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise305", type=xal_PremiseNumberPrefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseNumberSuffix307: BinaryAssociation = BinaryAssociation(
    name="premiseNumberSuffix307",
    ends={
        Property(name="xal_PremiseNumberSuffix309", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise308", type=xal_PremiseNumberSuffix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buildingName310: BinaryAssociation = BinaryAssociation(
    name="buildingName310",
    ends={
        Property(name="xal_BuildingName312", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise311", type=xal_BuildingName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPremise313: BinaryAssociation = BinaryAssociation(
    name="subPremise313",
    ends={
        Property(name="xal_SubPremise", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise314", type=xal_SubPremise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firm315: BinaryAssociation = BinaryAssociation(
    name="firm315",
    ends={
        Property(name="xal_Firm317", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise316", type=xal_Firm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mailStop318: BinaryAssociation = BinaryAssociation(
    name="mailStop318",
    ends={
        Property(name="xal_MailStop320", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise319", type=xal_MailStop, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode321: BinaryAssociation = BinaryAssociation(
    name="postalCode321",
    ends={
        Property(name="xal_PostalCode323", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise322", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
premise325: BinaryAssociation = BinaryAssociation(
    name="premise325",
    ends={
        Property(name="xal_Premise326", type=xal_Premise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Premise324", type=xal_Premise, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
premiseNumberRangeFrom327: BinaryAssociation = BinaryAssociation(
    name="premiseNumberRangeFrom327",
    ends={
        Property(name="xal_PremiseNumberRangeFrom", type=xal_PremiseNumberRange, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PremiseNumberRange328", type=xal_PremiseNumberRangeFrom, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
premiseNumberRangeTo329: BinaryAssociation = BinaryAssociation(
    name="premiseNumberRangeTo329",
    ends={
        Property(name="xal_PremiseNumberRangeTo", type=xal_PremiseNumberRange, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PremiseNumberRange330", type=xal_PremiseNumberRangeTo, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
premiseNumber349: BinaryAssociation = BinaryAssociation(
    name="premiseNumber349",
    ends={
        Property(name="xal_PremiseNumber351", type=xal_PremiseNumberRangeTo, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PremiseNumberRangeTo350", type=xal_PremiseNumber, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
addressLine331: BinaryAssociation = BinaryAssociation(
    name="addressLine331",
    ends={
        Property(name="xal_AddressLine333", type=xal_PremiseNumberRangeFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PremiseNumberRangeFrom332", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseNumberPrefix334: BinaryAssociation = BinaryAssociation(
    name="premiseNumberPrefix334",
    ends={
        Property(name="xal_PremiseNumberPrefix336", type=xal_PremiseNumberRangeFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PremiseNumberRangeFrom335", type=xal_PremiseNumberPrefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseNumber337: BinaryAssociation = BinaryAssociation(
    name="premiseNumber337",
    ends={
        Property(name="xal_PremiseNumber339", type=xal_PremiseNumberRangeFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PremiseNumberRangeFrom338", type=xal_PremiseNumber, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
premiseNumberSuffix340: BinaryAssociation = BinaryAssociation(
    name="premiseNumberSuffix340",
    ends={
        Property(name="xal_PremiseNumberSuffix342", type=xal_PremiseNumberRangeFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PremiseNumberRangeFrom341", type=xal_PremiseNumberSuffix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressLine343: BinaryAssociation = BinaryAssociation(
    name="addressLine343",
    ends={
        Property(name="xal_AddressLine345", type=xal_PremiseNumberRangeTo, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PremiseNumberRangeTo344", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseNumberPrefix346: BinaryAssociation = BinaryAssociation(
    name="premiseNumberPrefix346",
    ends={
        Property(name="xal_PremiseNumberPrefix348", type=xal_PremiseNumberRangeTo, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PremiseNumberRangeTo347", type=xal_PremiseNumberPrefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
premiseNumberSuffix352: BinaryAssociation = BinaryAssociation(
    name="premiseNumberSuffix352",
    ends={
        Property(name="xal_PremiseNumberSuffix354", type=xal_PremiseNumberRangeTo, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_PremiseNumberRangeTo353", type=xal_PremiseNumberSuffix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressLine355: BinaryAssociation = BinaryAssociation(
    name="addressLine355",
    ends={
        Property(name="xal_AddressLine357", type=xal_SubAdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubAdministrativeArea356", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subAdministrativeAreaName358: BinaryAssociation = BinaryAssociation(
    name="subAdministrativeAreaName358",
    ends={
        Property(name="xal_SubAdministrativeAreaName", type=xal_SubAdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubAdministrativeArea359", type=xal_SubAdministrativeAreaName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locality360: BinaryAssociation = BinaryAssociation(
    name="locality360",
    ends={
        Property(name="xal_Locality362", type=xal_SubAdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubAdministrativeArea361", type=xal_Locality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postOffice363: BinaryAssociation = BinaryAssociation(
    name="postOffice363",
    ends={
        Property(name="xal_PostOffice365", type=xal_SubAdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubAdministrativeArea364", type=xal_PostOffice, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode366: BinaryAssociation = BinaryAssociation(
    name="postalCode366",
    ends={
        Property(name="xal_PostalCode368", type=xal_SubAdministrativeArea, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubAdministrativeArea367", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine369: BinaryAssociation = BinaryAssociation(
    name="addressLine369",
    ends={
        Property(name="xal_AddressLine371", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise370", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPremiseNumber376: BinaryAssociation = BinaryAssociation(
    name="subPremiseNumber376",
    ends={
        Property(name="xal_SubPremiseNumber", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise377", type=xal_SubPremiseNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPremiseNumberPrefix378: BinaryAssociation = BinaryAssociation(
    name="subPremiseNumberPrefix378",
    ends={
        Property(name="xal_SubPremiseNumberPrefix", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise379", type=xal_SubPremiseNumberPrefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPremiseNumberSuffix380: BinaryAssociation = BinaryAssociation(
    name="subPremiseNumberSuffix380",
    ends={
        Property(name="xal_SubPremiseNumberSuffix", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise381", type=xal_SubPremiseNumberSuffix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buildingName382: BinaryAssociation = BinaryAssociation(
    name="buildingName382",
    ends={
        Property(name="xal_BuildingName384", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise383", type=xal_BuildingName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPremiseName372: BinaryAssociation = BinaryAssociation(
    name="subPremiseName372",
    ends={
        Property(name="xal_SubPremiseName", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise373", type=xal_SubPremiseName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPremiseLocation374: BinaryAssociation = BinaryAssociation(
    name="subPremiseLocation374",
    ends={
        Property(name="xal_SubPremiseLocation", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise375", type=xal_SubPremiseLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode391: BinaryAssociation = BinaryAssociation(
    name="postalCode391",
    ends={
        Property(name="xal_PostalCode393", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise392", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subPremise395: BinaryAssociation = BinaryAssociation(
    name="subPremise395",
    ends={
        Property(name="xal_SubPremise396", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise394", type=xal_SubPremise, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firm385: BinaryAssociation = BinaryAssociation(
    name="firm385",
    ends={
        Property(name="xal_Firm387", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise386", type=xal_Firm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mailStop388: BinaryAssociation = BinaryAssociation(
    name="mailStop388",
    ends={
        Property(name="xal_MailStop390", type=xal_SubPremise, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_SubPremise389", type=xal_MailStop, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfareNumber400: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumber400",
    ends={
        Property(name="xal_ThoroughfareNumber402", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare401", type=xal_ThoroughfareNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareNumberRange403: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberRange403",
    ends={
        Property(name="xal_ThoroughfareNumberRange", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare404", type=xal_ThoroughfareNumberRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressLine397: BinaryAssociation = BinaryAssociation(
    name="addressLine397",
    ends={
        Property(name="xal_AddressLine399", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare398", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareNumberSuffix408: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberSuffix408",
    ends={
        Property(name="xal_ThoroughfareNumberSuffix410", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare409", type=xal_ThoroughfareNumberSuffix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfarePreDirection411: BinaryAssociation = BinaryAssociation(
    name="thoroughfarePreDirection411",
    ends={
        Property(name="xal_ThoroughfarePreDirection413", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare412", type=xal_ThoroughfarePreDirection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfareLeadingType414: BinaryAssociation = BinaryAssociation(
    name="thoroughfareLeadingType414",
    ends={
        Property(name="xal_ThoroughfareLeadingType416", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare415", type=xal_ThoroughfareLeadingType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfareNumberPrefix405: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberPrefix405",
    ends={
        Property(name="xal_ThoroughfareNumberPrefix407", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare406", type=xal_ThoroughfareNumberPrefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareTrailingType420: BinaryAssociation = BinaryAssociation(
    name="thoroughfareTrailingType420",
    ends={
        Property(name="xal_ThoroughfareTrailingType422", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare421", type=xal_ThoroughfareTrailingType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfarePostDirection423: BinaryAssociation = BinaryAssociation(
    name="thoroughfarePostDirection423",
    ends={
        Property(name="xal_ThoroughfarePostDirection425", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare424", type=xal_ThoroughfarePostDirection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependentThoroughfare426: BinaryAssociation = BinaryAssociation(
    name="dependentThoroughfare426",
    ends={
        Property(name="xal_DependentThoroughfare428", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare427", type=xal_DependentThoroughfare, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependentLocality429: BinaryAssociation = BinaryAssociation(
    name="dependentLocality429",
    ends={
        Property(name="xal_DependentLocality431", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare430", type=xal_DependentLocality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thoroughfareName417: BinaryAssociation = BinaryAssociation(
    name="thoroughfareName417",
    ends={
        Property(name="xal_ThoroughfareName419", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare418", type=xal_ThoroughfareName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firm435: BinaryAssociation = BinaryAssociation(
    name="firm435",
    ends={
        Property(name="xal_Firm437", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare436", type=xal_Firm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postalCode438: BinaryAssociation = BinaryAssociation(
    name="postalCode438",
    ends={
        Property(name="xal_PostalCode440", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare439", type=xal_PostalCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
premise432: BinaryAssociation = BinaryAssociation(
    name="premise432",
    ends={
        Property(name="xal_Premise434", type=xal_Thoroughfare, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Thoroughfare433", type=xal_Premise, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressLine441: BinaryAssociation = BinaryAssociation(
    name="addressLine441",
    ends={
        Property(name="xal_AddressLine442", type=xal_ThoroughfareNumberFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_ThoroughfareNumberFrom", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareNumberPrefix443: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberPrefix443",
    ends={
        Property(name="xal_ThoroughfareNumberPrefix445", type=xal_ThoroughfareNumberFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_ThoroughfareNumberFrom444", type=xal_ThoroughfareNumberPrefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareNumberSuffix449: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberSuffix449",
    ends={
        Property(name="xal_ThoroughfareNumberFrom450", type=xal_ThoroughfareNumberSuffix, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="xal_ThoroughfareNumberSuffix451", type=xal_ThoroughfareNumberFrom, multiplicity=Multiplicity(1, 1))
    }
)
thoroughfareNumber446: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumber446",
    ends={
        Property(name="xal_ThoroughfareNumber448", type=xal_ThoroughfareNumberFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_ThoroughfareNumberFrom447", type=xal_ThoroughfareNumber, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
thoroughfareNumberTo458: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberTo458",
    ends={
        Property(name="xal_ThoroughfareNumberTo", type=xal_ThoroughfareNumberRange, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_ThoroughfareNumberRange459", type=xal_ThoroughfareNumberTo, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addressLine452: BinaryAssociation = BinaryAssociation(
    name="addressLine452",
    ends={
        Property(name="xal_AddressLine454", type=xal_ThoroughfareNumberRange, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_ThoroughfareNumberRange453", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareNumberFrom455: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberFrom455",
    ends={
        Property(name="xal_ThoroughfareNumberFrom457", type=xal_ThoroughfareNumberRange, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_ThoroughfareNumberRange456", type=xal_ThoroughfareNumberFrom, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addressLine460: BinaryAssociation = BinaryAssociation(
    name="addressLine460",
    ends={
        Property(name="xal_AddressLine462", type=xal_ThoroughfareNumberTo, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_ThoroughfareNumberTo461", type=xal_AddressLine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareNumberPrefix463: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberPrefix463",
    ends={
        Property(name="xal_ThoroughfareNumberPrefix465", type=xal_ThoroughfareNumberTo, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_ThoroughfareNumberTo464", type=xal_ThoroughfareNumberPrefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoroughfareNumber466: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumber466",
    ends={
        Property(name="xal_ThoroughfareNumber468", type=xal_ThoroughfareNumberTo, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_ThoroughfareNumberTo467", type=xal_ThoroughfareNumber, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
thoroughfareNumberSuffix469: BinaryAssociation = BinaryAssociation(
    name="thoroughfareNumberSuffix469",
    ends={
        Property(name="xal_ThoroughfareNumberSuffix471", type=xal_ThoroughfareNumberTo, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_ThoroughfareNumberTo470", type=xal_ThoroughfareNumberSuffix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressDetails472: BinaryAssociation = BinaryAssociation(
    name="addressDetails472",
    ends={
        Property(name="xal_AddressDetails474", type=xal_Xal, multiplicity=Multiplicity(1, 1)),
        Property(name="xal_Xal473", type=xal_AddressDetails, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="xal",
    types={xal_Address, xal_AddressDetails, xal_PostalServiceElements, xal_AddressLines, xal_Country, xal_AdministrativeArea, xal_Locality, xal_Thoroughfare, xal_AddressIdentifier, xal_AddressLatitude, xal_AddressLatitudeDirection, xal_AddressLine, xal_AddressLongitude, xal_AddressLongitudeDirection, xal_SubAdministrativeArea, xal_PostOffice, xal_AdministrativeAreaName, xal_PostalCode, xal_BuildingName, xal_CountryNameCode, xal_Barcode, xal_CountryName, xal_DepartmentName, xal_MailStop, xal_Department, xal_DependentLocality, xal_DependentLocalityName, xal_DependentLocalityNumber, xal_PostBox, xal_Premise, xal_LargeMailUser, xal_PostalRoute, xal_ThoroughfareName, xal_ThoroughfareTrailingType, xal_ThoroughfarePostDirection, xal_DependentThoroughfare, xal_ThoroughfarePreDirection, xal_ThoroughfareLeadingType, xal_EStringToStringMapEntry, xal_DocumentRoot, xal_ThoroughfareNumber, xal_ThoroughfareNumberPrefix, xal_ThoroughfareNumberSuffix, xal_PremiseNumber, xal_PremiseNumberPrefix, xal_PremiseNumberSuffix, xal_Firm, xal_FirmName, xal_Xal, xal_EndorsementLineCode, xal_KeyLineCode, xal_LargeMailUserName, xal_LargeMailUserIdentifier, xal_LocalityName, xal_MailStopName, xal_MailStopNumber, xal_PostalCodeNumber, xal_PostalCodeNumberExtension, xal_PostTown, xal_PostalRouteNumber, xal_PostalRouteName, xal_SortingCode, xal_SupplementaryPostalServiceData, xal_PostBoxNumber, xal_PostBoxNumberPrefix, xal_PostBoxNumberSuffix, xal_PostBoxNumberExtension, xal_PostOfficeName, xal_PostOfficeNumber, xal_PostTownName, xal_PostTownSuffix, xal_PremiseName, xal_PremiseLocation, xal_PremiseNumberRange, xal_SubPremise, xal_PremiseNumberRangeFrom, xal_PremiseNumberRangeTo, xal_SubAdministrativeAreaName, xal_SubPremiseNumber, xal_SubPremiseNumberPrefix, xal_SubPremiseNumberSuffix, xal_SubPremiseName, xal_SubPremiseLocation, xal_ThoroughfareNumberRange, xal_ThoroughfareNumberFrom, xal_ThoroughfareNumberTo, DependentThoroughfaresType, IndicatorOccurence, IndicatorOccurrence3, IndicatorOccurrence4, IndicatorOccurrence, IndicatorOccurrence1, IndicatorOccurrence2, NameNumberOccurrence, NumberOccurrence, NumberRangeOccurence, NumberRangeOccurrence, NumberTypeOccurrence, NumberTypeOccurrence1, NumberTypeType, NumberTypeType1, RangeTypeType, TypeOccurrence, TypeOccurrence1, TypeOccurrence2},
    associations={postalServiceElements0, address1, addressLines3, country5, administrativeArea7, locality9, thoroughfare11, addressLine13, subAdministrativeArea20, locality22, postOffice25, addressLine15, administrativeAreaName18, postalCode27, addressLine29, countryNameCode32, countryName34, administrativeArea36, locality39, thoroughfare42, departmentName47, mailStop49, postalCode51, addressLine45, addressLine54, dependentLocalityName56, dependentLocalityNumber58, postBox60, premise72, dependentLocality75, postalCode77, largeMailUser62, postOffice64, postalRoute67, thoroughfare69, thoroughfareName86, thoroughfareTrailingType88, thoroughfarePostDirection90, addressLine80, thoroughfarePreDirection82, thoroughfareLeadingType84, xMLNSPrefixMap92, xSISchemaLocation93, addressDetails96, addressLine99, administrativeArea102, postalCode114, postBox117, postOffice120, premise123, countryName105, department108, locality111, thoroughfare132, thoroughfareNumber135, thoroughfareNumberPrefix137, thoroughfareNumberSuffix139, premiseNumber126, premiseNumberPrefix128, premiseNumberSuffix130, addressLine143, firmName145, department147, xAL141, mailStop150, postalCode153, addressLine156, largeMailUserName159, buildingName163, department165, postBox168, thoroughfare171, postalCode174, largeMailUserIdentifier161, addressLine177, localityName180, largeMailUser185, postOffice188, postalRoute191, thoroughfare194, premise197, dependentLocality200, postalCode203, postBox182, addressLine206, mailStopName209, mailStopNumber211, addressLine213, postalCodeNumber216, postalCodeNumberExtension218, postTown220, addressLine222, postalRouteNumber227, postBox229, postalRouteName225, addressLongitude246, addressIdentifier232, endorsementLineCode234, keyLineCode236, barcode238, sortingCode240, addressLatitude242, addressLatitudeDirection244, addressLongitudeDirection248, supplementaryPostalServiceData250, addressLine252, postBoxNumber255, postBoxNumberPrefix257, postBoxNumberSuffix259, postBoxNumberExtension261, firm263, postalCode266, addressLine269, postOfficeName272, postOfficeNumber274, postalRoute276, postBox279, postalCode282, addressLine285, postTownName288, postTownSuffix290, addressLine292, premiseName295, premiseLocation297, premiseNumber299, premiseNumberRange302, premiseNumberPrefix304, premiseNumberSuffix307, buildingName310, subPremise313, firm315, mailStop318, postalCode321, premise325, premiseNumberRangeFrom327, premiseNumberRangeTo329, premiseNumber349, addressLine331, premiseNumberPrefix334, premiseNumber337, premiseNumberSuffix340, addressLine343, premiseNumberPrefix346, premiseNumberSuffix352, addressLine355, subAdministrativeAreaName358, locality360, postOffice363, postalCode366, addressLine369, subPremiseNumber376, subPremiseNumberPrefix378, subPremiseNumberSuffix380, buildingName382, subPremiseName372, subPremiseLocation374, postalCode391, subPremise395, firm385, mailStop388, thoroughfareNumber400, thoroughfareNumberRange403, addressLine397, thoroughfareNumberSuffix408, thoroughfarePreDirection411, thoroughfareLeadingType414, thoroughfareNumberPrefix405, thoroughfareTrailingType420, thoroughfarePostDirection423, dependentThoroughfare426, dependentLocality429, thoroughfareName417, firm435, postalCode438, premise432, addressLine441, thoroughfareNumberPrefix443, thoroughfareNumberSuffix449, thoroughfareNumber446, thoroughfareNumberTo458, addressLine452, thoroughfareNumberFrom455, addressLine460, thoroughfareNumberPrefix463, thoroughfareNumber466, thoroughfareNumberSuffix469, addressDetails472},
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