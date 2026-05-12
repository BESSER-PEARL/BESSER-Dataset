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
BQManager = Class(name="BQManager")
googleapiclient_discovery = Class(name="googleapiclient_discovery")
GCPManager = Class(name="GCPManager")
Oauth2client_client_GoogleCredentials = Class(name="Oauth2client_client_GoogleCredentials")
BQJobError = Class(name="BQJobError")
BQTable = Class(name="BQTable")
WHUtils = Class(name="WHUtils")
Salesforcemanager = Class(name="Salesforcemanager")
SalesforceBulkManager = Class(name="SalesforceBulkManager")
DBMManager = Class(name="DBMManager")
DCSManager = Class(name="DCSManager")
DCMManager = Class(name="DCMManager")
CloudSQLManager = Class(name="CloudSQLManager")
DSManager = Class(name="DSManager")
FBManager = Class(name="FBManager")
GCEManager = Class(name="GCEManager")
GCSManager = Class(name="GCSManager")
smp_events_dataset_smp_events_daily = Class(name="smp_events_dataset_smp_events_daily")
updater_events_dataset_updater_events_daily = Class(name="updater_events_dataset_updater_events_daily")
APNManager = Class(name="APNManager")
AppNexusClient = Class(name="AppNexusClient")
RecordType = Class(name="RecordType")
SojernBusiness = Class(name="SojernBusiness")
Targeting = Class(name="Targeting")
User = Class(name="User")
BrandSaftey = Class(name="BrandSaftey")
Goal = Class(name="Goal")
Partner = Class(name="Partner")
Pixel = Class(name="Pixel")
Advertiser = Class(name="Advertiser")
Agency = Class(name="Agency")
BrandSafetyBrandSafetyCustomSetting = Class(name="BrandSafetyBrandSafetyCustomSetting")
BrandSafetyBrandSafetyLabel = Class(name="BrandSafetyBrandSafetyLabel")
PartnerExcludedVertical = Class(name="PartnerExcludedVertical")
SystemInsertionOrder = Class(name="SystemInsertionOrder")
AdvertiserBlocklistWhitelist = Class(name="AdvertiserBlocklistWhitelist")
AdvertiserExcludedVertical = Class(name="AdvertiserExcludedVertical")
AgencyBlocklistWhitelist = Class(name="AgencyBlocklistWhitelist")
AgencyExcludedVertical = Class(name="AgencyExcludedVertical")
SpendAccount = Class(name="SpendAccount")
Campaign = Class(name="Campaign")
SpendAccountBlocklistWhitelist = Class(name="SpendAccountBlocklistWhitelist")
CampaignBlocklistWhitelist = Class(name="CampaignBlocklistWhitelist")
CampaignTravelEventType = Class(name="CampaignTravelEventType")
ProductLineItem = Class(name="ProductLineItem")
CreativeAsset = Class(name="CreativeAsset")
CreativeAssetTactic = Class(name="CreativeAssetTactic")
Tactic = Class(name="Tactic")
SystemLineItem = Class(name="SystemLineItem")
SystemCreative = Class(name="SystemCreative")
SystemLineItemConversionPixel = Class(name="SystemLineItemConversionPixel")
CreativeApproval = Class(name="CreativeApproval")
dbm_li_sfdc_product_li_mapping = Class(name="dbm_li_sfdc_product_li_mapping")
autopacing_inputs = Class(name="autopacing_inputs")
IOManager = Class(name="IOManager")
BidAdjuster = Class(name="BidAdjuster")
APNAdvertiser = Class(name="APNAdvertiser")
APNLineItem = Class(name="APNLineItem")
APNModel = Class(name="APNModel")
ProgrammaticModel_Interface = Class(name="ProgrammaticModel_Interface")
APNProgrammaticModel = Class(name="APNProgrammaticModel")
APNStore_Interface = Class(name="APNStore_Interface")
APNCache_Interface = Class(name="APNCache_Interface")
APNRepository_Interface = Class(name="APNRepository_Interface")
GenericModel = Class(name="GenericModel")
Model_Interface = Class(name="Model_Interface")
ModelService_Interface = Class(name="ModelService_Interface")
APNLineItemModelService = Class(name="APNLineItemModelService")
Class2 = Class(name="Class2")
APNModelFactory = Class(name="APNModelFactory")
RestClient = Class(name="RestClient")
AppNexus = Class(name="AppNexus")
APNAdv = Class(name="APNAdv")

# BQManager class attributes and methods

# googleapiclient_discovery class attributes and methods

# GCPManager class attributes and methods

# Oauth2client_client_GoogleCredentials class attributes and methods

# BQJobError class attributes and methods

# BQTable class attributes and methods

# WHUtils class attributes and methods

# Salesforcemanager class attributes and methods

# SalesforceBulkManager class attributes and methods

# DBMManager class attributes and methods

# DCSManager class attributes and methods

# DCMManager class attributes and methods

# CloudSQLManager class attributes and methods

# DSManager class attributes and methods

# FBManager class attributes and methods

# GCEManager class attributes and methods

# GCSManager class attributes and methods

# smp_events_dataset_smp_events_daily class attributes and methods
smp_events_dataset_smp_events_daily_externalIds_id__used_as_apnid_: Property = Property(name="externalIds_id__used_as_apnid_", type=StringType)
smp_events_dataset_smp_events_daily_eventsourcename: Property = Property(name="eventsourcename", type=StringType)
smp_events_dataset_smp_events_daily_profileid: Property = Property(name="profileid", type=StringType)
smp_events_dataset_smp_events_daily_ExternalIds_Type: Property = Property(name="ExternalIds_Type", type=StringType)
smp_events_dataset_smp_events_daily.attributes={smp_events_dataset_smp_events_daily_eventsourcename, smp_events_dataset_smp_events_daily_ExternalIds_Type, smp_events_dataset_smp_events_daily_profileid, smp_events_dataset_smp_events_daily_externalIds_id__used_as_apnid_}

# updater_events_dataset_updater_events_daily class attributes and methods
updater_events_dataset_updater_events_daily_sojernId: Property = Property(name="sojernId", type=StringType)
updater_events_dataset_updater_events_daily_advertisername: Property = Property(name="advertisername", type=StringType)
updater_events_dataset_updater_events_daily_segments_id: Property = Property(name="segments_id", type=StringType)
updater_events_dataset_updater_events_daily.attributes={updater_events_dataset_updater_events_daily_advertisername, updater_events_dataset_updater_events_daily_segments_id, updater_events_dataset_updater_events_daily_sojernId}

# APNManager class attributes and methods

# AppNexusClient class attributes and methods

# RecordType class attributes and methods
RecordType_id: Property = Property(name="id", type=StringType)
RecordType_name: Property = Property(name="name", type=StringType)
RecordType_description: Property = Property(name="description", type=StringType)
RecordType_crm_id: Property = Property(name="crm_id", type=StringType)
RecordType_updated_by: Property = Property(name="updated_by", type=StringType)
RecordType_deleted: Property = Property(name="deleted", type=StringType)
RecordType.attributes={RecordType_description, RecordType_updated_by, RecordType_name, RecordType_id, RecordType_crm_id, RecordType_deleted}

# SojernBusiness class attributes and methods

# Targeting class attributes and methods

# User class attributes and methods

# BrandSaftey class attributes and methods

# Goal class attributes and methods

# Partner class attributes and methods

# Pixel class attributes and methods

# Advertiser class attributes and methods
Advertiser_crm_id: Property = Property(name="crm_id", type=StringType)
Advertiser.attributes={Advertiser_crm_id}

# Agency class attributes and methods
Agency_crm_id: Property = Property(name="crm_id", type=StringType)
Agency.attributes={Agency_crm_id}

# BrandSafetyBrandSafetyCustomSetting class attributes and methods

# BrandSafetyBrandSafetyLabel class attributes and methods

# PartnerExcludedVertical class attributes and methods

# SystemInsertionOrder class attributes and methods

# AdvertiserBlocklistWhitelist class attributes and methods

# AdvertiserExcludedVertical class attributes and methods

# AgencyBlocklistWhitelist class attributes and methods

# AgencyExcludedVertical class attributes and methods

# SpendAccount class attributes and methods

# Campaign class attributes and methods

# SpendAccountBlocklistWhitelist class attributes and methods

# CampaignBlocklistWhitelist class attributes and methods

# CampaignTravelEventType class attributes and methods

# ProductLineItem class attributes and methods

# CreativeAsset class attributes and methods

# CreativeAssetTactic class attributes and methods

# Tactic class attributes and methods

# SystemLineItem class attributes and methods

# SystemCreative class attributes and methods

# SystemLineItemConversionPixel class attributes and methods

# CreativeApproval class attributes and methods

# dbm_li_sfdc_product_li_mapping class attributes and methods
dbm_li_sfdc_product_li_mapping_dbm_line_item_id: Property = Property(name="dbm_line_item_id", type=StringType)
dbm_li_sfdc_product_li_mapping_dbm_io_id: Property = Property(name="dbm_io_id", type=StringType)
dbm_li_sfdc_product_li_mapping_dbm_creative_ids: Property = Property(name="dbm_creative_ids", type=StringType)
dbm_li_sfdc_product_li_mapping_sfdc_product_id: Property = Property(name="sfdc_product_id", type=StringType)
dbm_li_sfdc_product_li_mapping_dub_allocation_label: Property = Property(name="dub_allocation_label", type=StringType)
dbm_li_sfdc_product_li_mapping.attributes={dbm_li_sfdc_product_li_mapping_dbm_io_id, dbm_li_sfdc_product_li_mapping_sfdc_product_id, dbm_li_sfdc_product_li_mapping_dub_allocation_label, dbm_li_sfdc_product_li_mapping_dbm_line_item_id, dbm_li_sfdc_product_li_mapping_dbm_creative_ids}

# autopacing_inputs class attributes and methods
autopacing_inputs_on_off: Property = Property(name="on_off", type=StringType)
autopacing_inputs_adjust_bids: Property = Property(name="adjust_bids", type=StringType)
autopacing_inputs_sfdc_opportunity_id: Property = Property(name="sfdc_opportunity_id", type=StringType)
autopacing_inputs_dbm_io_id: Property = Property(name="dbm_io_id", type=StringType)
autopacing_inputs_sfdc_product_id: Property = Property(name="sfdc_product_id", type=StringType)
autopacing_inputs_product_start_date: Property = Property(name="product_start_date", type=StringType)
autopacing_inputs_start_date: Property = Property(name="start_date", type=StringType)
autopacing_inputs_product_end_date: Property = Property(name="product_end_date", type=StringType)
autopacing_inputs_end_date: Property = Property(name="end_date", type=StringType)
autopacing_inputs_product_type: Property = Property(name="product_type", type=StringType)
autopacing_inputs_goal_type: Property = Property(name="goal_type", type=StringType)
autopacing_inputs_kpi_goal: Property = Property(name="kpi_goal", type=StringType)
autopacing_inputs_billing_currency: Property = Property(name="billing_currency", type=StringType)
autopacing_inputs_exchange_rate: Property = Property(name="exchange_rate", type=StringType)
autopacing_inputs_avg_price_usd: Property = Property(name="avg_price_usd", type=StringType)
autopacing_inputs_cvr: Property = Property(name="cvr", type=StringType)
autopacing_inputs_cpm: Property = Property(name="cpm", type=StringType)
autopacing_inputs_impressions: Property = Property(name="impressions", type=StringType)
autopacing_inputs_region: Property = Property(name="region", type=StringType)
autopacing_inputs_region1: Property = Property(name="region1", type=StringType)
autopacing_inputs_percentage_impression_credit: Property = Property(name="percentage_impression_credit", type=StringType)
autopacing_inputs_percentage_conversion_credit: Property = Property(name="percentage_conversion_credit", type=StringType)
autopacing_inputs_hours_early_to_complete: Property = Property(name="hours_early_to_complete", type=StringType)
autopacing_inputs_minimum_partner_data_delivery_percent: Property = Property(name="minimum_partner_data_delivery_percent", type=StringType)
autopacing_inputs_sojern_goal_rae: Property = Property(name="sojern_goal_rae", type=StringType)
autopacing_inputs_pacing: Property = Property(name="pacing", type=StringType)
autopacing_inputs_days_early_to_complete: Property = Property(name="days_early_to_complete", type=StringType)
autopacing_inputs_min_daily_volume_percent: Property = Property(name="min_daily_volume_percent", type=StringType)
autopacing_inputs_min_daily_volume: Property = Property(name="min_daily_volume", type=StringType)
autopacing_inputs_minimum_margin: Property = Property(name="minimum_margin", type=StringType)
autopacing_inputs_estimated_booking_value: Property = Property(name="estimated_booking_value", type=StringType)
autopacing_inputs_account_manager: Property = Property(name="account_manager", type=StringType)
autopacing_inputs_expected_click_credit: Property = Property(name="expected_click_credit", type=StringType)
autopacing_inputs_cpx: Property = Property(name="cpx", type=StringType)
autopacing_inputs_effective_impressions: Property = Property(name="effective_impressions", type=StringType)
autopacing_inputs_conversions: Property = Property(name="conversions", type=StringType)
autopacing_inputs.attributes={autopacing_inputs_conversions, autopacing_inputs_region, autopacing_inputs_sfdc_product_id, autopacing_inputs_expected_click_credit, autopacing_inputs_pacing, autopacing_inputs_product_start_date, autopacing_inputs_exchange_rate, autopacing_inputs_min_daily_volume, autopacing_inputs_product_type, autopacing_inputs_on_off, autopacing_inputs_cpm, autopacing_inputs_cpx, autopacing_inputs_billing_currency, autopacing_inputs_impressions, autopacing_inputs_account_manager, autopacing_inputs_effective_impressions, autopacing_inputs_kpi_goal, autopacing_inputs_minimum_partner_data_delivery_percent, autopacing_inputs_start_date, autopacing_inputs_adjust_bids, autopacing_inputs_estimated_booking_value, autopacing_inputs_minimum_margin, autopacing_inputs_sojern_goal_rae, autopacing_inputs_end_date, autopacing_inputs_avg_price_usd, autopacing_inputs_dbm_io_id, autopacing_inputs_days_early_to_complete, autopacing_inputs_percentage_conversion_credit, autopacing_inputs_min_daily_volume_percent, autopacing_inputs_sfdc_opportunity_id, autopacing_inputs_cvr, autopacing_inputs_region1, autopacing_inputs_goal_type, autopacing_inputs_hours_early_to_complete, autopacing_inputs_percentage_impression_credit, autopacing_inputs_product_end_date}

# IOManager class attributes and methods

# BidAdjuster class attributes and methods

# APNAdvertiser class attributes and methods

# APNLineItem class attributes and methods
APNLineItem_attribute: Property = Property(name="attribute", type=StringType)
APNLineItem_attribute2: Property = Property(name="attribute2", type=StringType)
APNLineItem.attributes={APNLineItem_attribute2, APNLineItem_attribute}

# APNModel class attributes and methods

# ProgrammaticModel_Interface class attributes and methods

# APNProgrammaticModel class attributes and methods

# APNStore_Interface class attributes and methods

# APNCache_Interface class attributes and methods

# APNRepository_Interface class attributes and methods

# GenericModel class attributes and methods

# Model_Interface class attributes and methods

# ModelService_Interface class attributes and methods

# APNLineItemModelService class attributes and methods

# Class2 class attributes and methods

# APNModelFactory class attributes and methods

# RestClient class attributes and methods

# AppNexus class attributes and methods

# APNAdv class attributes and methods

# Relationships
APNModel_APNLineItem: BinaryAssociation = BinaryAssociation(
    name="APNModel_APNLineItem",
    ends={
        Property(name="APNModel_APNLineItem_15", type=APNModel, multiplicity=Multiplicity(0, 9999)),
        Property(name="APNModel_APNLineItem_04", type=APNLineItem, multiplicity=Multiplicity(1, 1))
    }
)
APNProgrammaticModel_APNRepository: BinaryAssociation = BinaryAssociation(
    name="APNProgrammaticModel_APNRepository",
    ends={
        Property(name="aPNRepository6", type=APNRepository_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="aPNProgrammaticModel7", type=APNProgrammaticModel, multiplicity=Multiplicity(0, 1))
    }
)
APNRepository_APNStore: BinaryAssociation = BinaryAssociation(
    name="APNRepository_APNStore",
    ends={
        Property(name="aPNStore8", type=APNStore_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="aPNRepository9", type=APNRepository_Interface, multiplicity=Multiplicity(0, 1))
    }
)
APNRepository_APNCache: BinaryAssociation = BinaryAssociation(
    name="APNRepository_APNCache",
    ends={
        Property(name="aPNCache10", type=APNCache_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="aPNRepository11", type=APNRepository_Interface, multiplicity=Multiplicity(0, 1))
    }
)
APNProgrammaticModel_APNModel: BinaryAssociation = BinaryAssociation(
    name="APNProgrammaticModel_APNModel",
    ends={
        Property(name="aPNModel12", type=APNModel, multiplicity=Multiplicity(0, 1)),
        Property(name="aPNProgrammaticModel13", type=APNProgrammaticModel, multiplicity=Multiplicity(0, 1))
    }
)
APNProgrammaticModel_APNModelFactory: BinaryAssociation = BinaryAssociation(
    name="APNProgrammaticModel_APNModelFactory",
    ends={
        Property(name="APNProgrammaticModel_APNModelFactory_014", type=APNModelFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="aPNProgrammaticModel15", type=APNProgrammaticModel, multiplicity=Multiplicity(1, 1))
    }
)
APNModelFactory_APNModel: BinaryAssociation = BinaryAssociation(
    name="APNModelFactory_APNModel",
    ends={
        Property(name="APNModelFactory_APNModel_016", type=APNModel, multiplicity=Multiplicity(0, 9999)),
        Property(name="APNModelFactory_APNModel_117", type=APNModelFactory, multiplicity=Multiplicity(1, 1))
    }
)
APNLineItem_APNModel: BinaryAssociation = BinaryAssociation(
    name="APNLineItem_APNModel",
    ends={
        Property(name="APNLineItem_APNModel_018", type=APNModel, multiplicity=Multiplicity(0, 9999)),
        Property(name="APNLineItem_APNModel_119", type=APNLineItem, multiplicity=Multiplicity(0, 9999))
    }
)
APNLineItemModelService_APNLineItem: BinaryAssociation = BinaryAssociation(
    name="APNLineItemModelService_APNLineItem",
    ends={
        Property(name="APNLineItemModelService_APNLineItem_020", type=APNLineItem, multiplicity=Multiplicity(0, 1)),
        Property(name="APNLineItemModelService_APNLineItem_121", type=APNLineItemModelService, multiplicity=Multiplicity(0, 1))
    }
)
APNStore_RestClient: BinaryAssociation = BinaryAssociation(
    name="APNStore_RestClient",
    ends={
        Property(name="restClient22", type=RestClient, multiplicity=Multiplicity(0, 1)),
        Property(name="aPNStore23", type=APNStore_Interface, multiplicity=Multiplicity(0, 1))
    }
)
APNModel_APNAdv: BinaryAssociation = BinaryAssociation(
    name="APNModel_APNAdv",
    ends={
        Property(name="aPNAdv24", type=APNAdv, multiplicity=Multiplicity(0, 9999)),
        Property(name="aPNModel25", type=APNModel, multiplicity=Multiplicity(0, 9999))
    }
)
BQManager_BQJobError: BinaryAssociation = BinaryAssociation(
    name="BQManager_BQJobError",
    ends={
        Property(name="bQJobError0", type=BQJobError, multiplicity=Multiplicity(0, 1)),
        Property(name="bQManager1", type=BQManager, multiplicity=Multiplicity(0, 1))
    }
)
APNModel_APNAdvertiser: BinaryAssociation = BinaryAssociation(
    name="APNModel_APNAdvertiser",
    ends={
        Property(name="APNModel_APNAdvertiser_02", type=APNAdvertiser, multiplicity=Multiplicity(0, 9999)),
        Property(name="APNModel_APNAdvertiser_13", type=APNModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_437ab337_a90b_4f71_b624_4453324e5fa9",
    types={BQManager, googleapiclient_discovery, GCPManager, Oauth2client_client_GoogleCredentials, BQJobError, BQTable, WHUtils, Salesforcemanager, SalesforceBulkManager, DBMManager, DCSManager, DCMManager, CloudSQLManager, DSManager, FBManager, GCEManager, GCSManager, smp_events_dataset_smp_events_daily, updater_events_dataset_updater_events_daily, APNManager, AppNexusClient, RecordType, SojernBusiness, Targeting, User, BrandSaftey, Goal, Partner, Pixel, Advertiser, Agency, BrandSafetyBrandSafetyCustomSetting, BrandSafetyBrandSafetyLabel, PartnerExcludedVertical, SystemInsertionOrder, AdvertiserBlocklistWhitelist, AdvertiserExcludedVertical, AgencyBlocklistWhitelist, AgencyExcludedVertical, SpendAccount, Campaign, SpendAccountBlocklistWhitelist, CampaignBlocklistWhitelist, CampaignTravelEventType, ProductLineItem, CreativeAsset, CreativeAssetTactic, Tactic, SystemLineItem, SystemCreative, SystemLineItemConversionPixel, CreativeApproval, dbm_li_sfdc_product_li_mapping, autopacing_inputs, IOManager, BidAdjuster, APNAdvertiser, APNLineItem, APNModel, ProgrammaticModel_Interface, APNProgrammaticModel, APNStore_Interface, APNCache_Interface, APNRepository_Interface, GenericModel, Model_Interface, ModelService_Interface, APNLineItemModelService, Class2, APNModelFactory, RestClient, AppNexus, APNAdv},
    associations={APNModel_APNLineItem, APNProgrammaticModel_APNRepository, APNRepository_APNStore, APNRepository_APNCache, APNProgrammaticModel_APNModel, APNProgrammaticModel_APNModelFactory, APNModelFactory_APNModel, APNLineItem_APNModel, APNLineItemModelService_APNLineItem, APNStore_RestClient, APNModel_APNAdv, BQManager_BQJobError, APNModel_APNAdvertiser},
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