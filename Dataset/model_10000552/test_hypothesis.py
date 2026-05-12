import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    APNAdv,
    AppNexus,
    RestClient,
    APNModelFactory,
    Class2,
    APNLineItemModelService,
    ModelService_Interface,
    Model_Interface,
    GenericModel,
    APNRepository_Interface,
    APNCache_Interface,
    APNStore_Interface,
    APNProgrammaticModel,
    ProgrammaticModel_Interface,
    APNModel,
    APNLineItem,
    APNAdvertiser,
    BidAdjuster,
    IOManager,
    autopacing_inputs,
    dbm_li_sfdc_product_li_mapping,
    CreativeApproval,
    SystemLineItemConversionPixel,
    SystemCreative,
    SystemLineItem,
    Tactic,
    CreativeAssetTactic,
    CreativeAsset,
    ProductLineItem,
    CampaignTravelEventType,
    CampaignBlocklistWhitelist,
    SpendAccountBlocklistWhitelist,
    Campaign,
    SpendAccount,
    AgencyExcludedVertical,
    AgencyBlocklistWhitelist,
    AdvertiserExcludedVertical,
    AdvertiserBlocklistWhitelist,
    SystemInsertionOrder,
    PartnerExcludedVertical,
    BrandSafetyBrandSafetyLabel,
    BrandSafetyBrandSafetyCustomSetting,
    Agency,
    Advertiser,
    Pixel,
    Partner,
    Goal,
    BrandSaftey,
    User,
    Targeting,
    SojernBusiness,
    RecordType,
    AppNexusClient,
    APNManager,
    updater_events_dataset_updater_events_daily,
    smp_events_dataset_smp_events_daily,
    GCSManager,
    GCEManager,
    FBManager,
    DSManager,
    CloudSQLManager,
    DCMManager,
    DCSManager,
    DBMManager,
    SalesforceBulkManager,
    Salesforcemanager,
    WHUtils,
    BQTable,
    BQJobError,
    Oauth2client_client_GoogleCredentials,
    GCPManager,
    googleapiclient_discovery,
    BQManager,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_apnadv_is_not_abstract():
    assert not inspect.isabstract(APNAdv)


def test_apnadv_constructor_exists():
    assert callable(APNAdv.__init__)


def test_apnadv_constructor_args():
    sig = inspect.signature(APNAdv.__init__)
    params = list(sig.parameters.keys())



def test_appnexus_is_not_abstract():
    assert not inspect.isabstract(AppNexus)


def test_appnexus_constructor_exists():
    assert callable(AppNexus.__init__)


def test_appnexus_constructor_args():
    sig = inspect.signature(AppNexus.__init__)
    params = list(sig.parameters.keys())



def test_restclient_is_not_abstract():
    assert not inspect.isabstract(RestClient)


def test_restclient_constructor_exists():
    assert callable(RestClient.__init__)


def test_restclient_constructor_args():
    sig = inspect.signature(RestClient.__init__)
    params = list(sig.parameters.keys())



def test_apnmodelfactory_is_not_abstract():
    assert not inspect.isabstract(APNModelFactory)


def test_apnmodelfactory_constructor_exists():
    assert callable(APNModelFactory.__init__)


def test_apnmodelfactory_constructor_args():
    sig = inspect.signature(APNModelFactory.__init__)
    params = list(sig.parameters.keys())



def test_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_apnlineitemmodelservice_is_not_abstract():
    assert not inspect.isabstract(APNLineItemModelService)


def test_apnlineitemmodelservice_constructor_exists():
    assert callable(APNLineItemModelService.__init__)


def test_apnlineitemmodelservice_constructor_args():
    sig = inspect.signature(APNLineItemModelService.__init__)
    params = list(sig.parameters.keys())



def test_modelservice_interface_is_not_abstract():
    assert not inspect.isabstract(ModelService_Interface)


def test_modelservice_interface_constructor_exists():
    assert callable(ModelService_Interface.__init__)


def test_modelservice_interface_constructor_args():
    sig = inspect.signature(ModelService_Interface.__init__)
    params = list(sig.parameters.keys())



def test_model_interface_is_not_abstract():
    assert not inspect.isabstract(Model_Interface)


def test_model_interface_constructor_exists():
    assert callable(Model_Interface.__init__)


def test_model_interface_constructor_args():
    sig = inspect.signature(Model_Interface.__init__)
    params = list(sig.parameters.keys())



def test_genericmodel_is_not_abstract():
    assert not inspect.isabstract(GenericModel)


def test_genericmodel_constructor_exists():
    assert callable(GenericModel.__init__)


def test_genericmodel_constructor_args():
    sig = inspect.signature(GenericModel.__init__)
    params = list(sig.parameters.keys())



def test_apnrepository_interface_is_not_abstract():
    assert not inspect.isabstract(APNRepository_Interface)


def test_apnrepository_interface_constructor_exists():
    assert callable(APNRepository_Interface.__init__)


def test_apnrepository_interface_constructor_args():
    sig = inspect.signature(APNRepository_Interface.__init__)
    params = list(sig.parameters.keys())



def test_apncache_interface_is_not_abstract():
    assert not inspect.isabstract(APNCache_Interface)


def test_apncache_interface_constructor_exists():
    assert callable(APNCache_Interface.__init__)


def test_apncache_interface_constructor_args():
    sig = inspect.signature(APNCache_Interface.__init__)
    params = list(sig.parameters.keys())



def test_apnstore_interface_is_not_abstract():
    assert not inspect.isabstract(APNStore_Interface)


def test_apnstore_interface_constructor_exists():
    assert callable(APNStore_Interface.__init__)


def test_apnstore_interface_constructor_args():
    sig = inspect.signature(APNStore_Interface.__init__)
    params = list(sig.parameters.keys())



def test_apnprogrammaticmodel_is_not_abstract():
    assert not inspect.isabstract(APNProgrammaticModel)


def test_apnprogrammaticmodel_constructor_exists():
    assert callable(APNProgrammaticModel.__init__)


def test_apnprogrammaticmodel_constructor_args():
    sig = inspect.signature(APNProgrammaticModel.__init__)
    params = list(sig.parameters.keys())



def test_programmaticmodel_interface_is_not_abstract():
    assert not inspect.isabstract(ProgrammaticModel_Interface)


def test_programmaticmodel_interface_constructor_exists():
    assert callable(ProgrammaticModel_Interface.__init__)


def test_programmaticmodel_interface_constructor_args():
    sig = inspect.signature(ProgrammaticModel_Interface.__init__)
    params = list(sig.parameters.keys())



def test_apnmodel_is_not_abstract():
    assert not inspect.isabstract(APNModel)


def test_apnmodel_constructor_exists():
    assert callable(APNModel.__init__)


def test_apnmodel_constructor_args():
    sig = inspect.signature(APNModel.__init__)
    params = list(sig.parameters.keys())



def test_apnlineitem_is_not_abstract():
    assert not inspect.isabstract(APNLineItem)


def test_apnlineitem_constructor_exists():
    assert callable(APNLineItem.__init__)


def test_apnlineitem_constructor_args():
    sig = inspect.signature(APNLineItem.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_apnlineitem_has_attribute2():
    assert hasattr(APNLineItem, "attribute2")
    descriptor = None
    for klass in APNLineItem.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_apnlineitem_has_attribute():
    assert hasattr(APNLineItem, "attribute")
    descriptor = None
    for klass in APNLineItem.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_apnadvertiser_is_not_abstract():
    assert not inspect.isabstract(APNAdvertiser)


def test_apnadvertiser_constructor_exists():
    assert callable(APNAdvertiser.__init__)


def test_apnadvertiser_constructor_args():
    sig = inspect.signature(APNAdvertiser.__init__)
    params = list(sig.parameters.keys())



def test_bidadjuster_is_not_abstract():
    assert not inspect.isabstract(BidAdjuster)


def test_bidadjuster_constructor_exists():
    assert callable(BidAdjuster.__init__)


def test_bidadjuster_constructor_args():
    sig = inspect.signature(BidAdjuster.__init__)
    params = list(sig.parameters.keys())



def test_iomanager_is_not_abstract():
    assert not inspect.isabstract(IOManager)


def test_iomanager_constructor_exists():
    assert callable(IOManager.__init__)


def test_iomanager_constructor_args():
    sig = inspect.signature(IOManager.__init__)
    params = list(sig.parameters.keys())



def test_autopacing_inputs_is_not_abstract():
    assert not inspect.isabstract(autopacing_inputs)


def test_autopacing_inputs_constructor_exists():
    assert callable(autopacing_inputs.__init__)


def test_autopacing_inputs_constructor_args():
    sig = inspect.signature(autopacing_inputs.__init__)
    params = list(sig.parameters.keys())
    assert "cvr" in params, "Missing parameter 'cvr'"
    assert "impressions" in params, "Missing parameter 'impressions'"
    assert "sojern_goal_rae" in params, "Missing parameter 'sojern_goal_rae'"
    assert "sfdc_opportunity_id" in params, "Missing parameter 'sfdc_opportunity_id'"
    assert "region1" in params, "Missing parameter 'region1'"
    assert "percentage_impression_credit" in params, "Missing parameter 'percentage_impression_credit'"
    assert "minimum_margin" in params, "Missing parameter 'minimum_margin'"
    assert "product_type" in params, "Missing parameter 'product_type'"
    assert "minimum_partner_data_delivery_percent" in params, "Missing parameter 'minimum_partner_data_delivery_percent'"
    assert "avg_price_usd" in params, "Missing parameter 'avg_price_usd'"
    assert "adjust_bids" in params, "Missing parameter 'adjust_bids'"
    assert "end_date" in params, "Missing parameter 'end_date'"
    assert "expected_click_credit" in params, "Missing parameter 'expected_click_credit'"
    assert "account_manager" in params, "Missing parameter 'account_manager'"
    assert "sfdc_product_id" in params, "Missing parameter 'sfdc_product_id'"
    assert "min_daily_volume" in params, "Missing parameter 'min_daily_volume'"
    assert "billing_currency" in params, "Missing parameter 'billing_currency'"
    assert "start_date" in params, "Missing parameter 'start_date'"
    assert "cpx" in params, "Missing parameter 'cpx'"
    assert "on_off" in params, "Missing parameter 'on_off'"
    assert "percentage_conversion_credit" in params, "Missing parameter 'percentage_conversion_credit'"
    assert "hours_early_to_complete" in params, "Missing parameter 'hours_early_to_complete'"
    assert "goal_type" in params, "Missing parameter 'goal_type'"
    assert "days_early_to_complete" in params, "Missing parameter 'days_early_to_complete'"
    assert "estimated_booking_value" in params, "Missing parameter 'estimated_booking_value'"
    assert "dbm_io_id" in params, "Missing parameter 'dbm_io_id'"
    assert "product_start_date" in params, "Missing parameter 'product_start_date'"
    assert "conversions" in params, "Missing parameter 'conversions'"
    assert "kpi_goal" in params, "Missing parameter 'kpi_goal'"
    assert "min_daily_volume_percent" in params, "Missing parameter 'min_daily_volume_percent'"
    assert "pacing" in params, "Missing parameter 'pacing'"
    assert "product_end_date" in params, "Missing parameter 'product_end_date'"
    assert "effective_impressions" in params, "Missing parameter 'effective_impressions'"
    assert "cpm" in params, "Missing parameter 'cpm'"
    assert "region" in params, "Missing parameter 'region'"
    assert "exchange_rate" in params, "Missing parameter 'exchange_rate'"

def test_autopacing_inputs_has_cvr():
    assert hasattr(autopacing_inputs, "cvr")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "cvr" in klass.__dict__:
            descriptor = klass.__dict__["cvr"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_impressions():
    assert hasattr(autopacing_inputs, "impressions")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "impressions" in klass.__dict__:
            descriptor = klass.__dict__["impressions"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_sojern_goal_rae():
    assert hasattr(autopacing_inputs, "sojern_goal_rae")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "sojern_goal_rae" in klass.__dict__:
            descriptor = klass.__dict__["sojern_goal_rae"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_sfdc_opportunity_id():
    assert hasattr(autopacing_inputs, "sfdc_opportunity_id")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "sfdc_opportunity_id" in klass.__dict__:
            descriptor = klass.__dict__["sfdc_opportunity_id"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_region1():
    assert hasattr(autopacing_inputs, "region1")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "region1" in klass.__dict__:
            descriptor = klass.__dict__["region1"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_percentage_impression_credit():
    assert hasattr(autopacing_inputs, "percentage_impression_credit")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "percentage_impression_credit" in klass.__dict__:
            descriptor = klass.__dict__["percentage_impression_credit"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_minimum_margin():
    assert hasattr(autopacing_inputs, "minimum_margin")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "minimum_margin" in klass.__dict__:
            descriptor = klass.__dict__["minimum_margin"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_product_type():
    assert hasattr(autopacing_inputs, "product_type")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "product_type" in klass.__dict__:
            descriptor = klass.__dict__["product_type"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_minimum_partner_data_delivery_percent():
    assert hasattr(autopacing_inputs, "minimum_partner_data_delivery_percent")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "minimum_partner_data_delivery_percent" in klass.__dict__:
            descriptor = klass.__dict__["minimum_partner_data_delivery_percent"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_avg_price_usd():
    assert hasattr(autopacing_inputs, "avg_price_usd")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "avg_price_usd" in klass.__dict__:
            descriptor = klass.__dict__["avg_price_usd"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_adjust_bids():
    assert hasattr(autopacing_inputs, "adjust_bids")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "adjust_bids" in klass.__dict__:
            descriptor = klass.__dict__["adjust_bids"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_end_date():
    assert hasattr(autopacing_inputs, "end_date")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "end_date" in klass.__dict__:
            descriptor = klass.__dict__["end_date"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_expected_click_credit():
    assert hasattr(autopacing_inputs, "expected_click_credit")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "expected_click_credit" in klass.__dict__:
            descriptor = klass.__dict__["expected_click_credit"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_account_manager():
    assert hasattr(autopacing_inputs, "account_manager")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "account_manager" in klass.__dict__:
            descriptor = klass.__dict__["account_manager"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_sfdc_product_id():
    assert hasattr(autopacing_inputs, "sfdc_product_id")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "sfdc_product_id" in klass.__dict__:
            descriptor = klass.__dict__["sfdc_product_id"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_min_daily_volume():
    assert hasattr(autopacing_inputs, "min_daily_volume")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "min_daily_volume" in klass.__dict__:
            descriptor = klass.__dict__["min_daily_volume"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_billing_currency():
    assert hasattr(autopacing_inputs, "billing_currency")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "billing_currency" in klass.__dict__:
            descriptor = klass.__dict__["billing_currency"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_start_date():
    assert hasattr(autopacing_inputs, "start_date")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "start_date" in klass.__dict__:
            descriptor = klass.__dict__["start_date"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_cpx():
    assert hasattr(autopacing_inputs, "cpx")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "cpx" in klass.__dict__:
            descriptor = klass.__dict__["cpx"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_on_off():
    assert hasattr(autopacing_inputs, "on_off")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "on_off" in klass.__dict__:
            descriptor = klass.__dict__["on_off"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_percentage_conversion_credit():
    assert hasattr(autopacing_inputs, "percentage_conversion_credit")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "percentage_conversion_credit" in klass.__dict__:
            descriptor = klass.__dict__["percentage_conversion_credit"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_hours_early_to_complete():
    assert hasattr(autopacing_inputs, "hours_early_to_complete")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "hours_early_to_complete" in klass.__dict__:
            descriptor = klass.__dict__["hours_early_to_complete"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_goal_type():
    assert hasattr(autopacing_inputs, "goal_type")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "goal_type" in klass.__dict__:
            descriptor = klass.__dict__["goal_type"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_days_early_to_complete():
    assert hasattr(autopacing_inputs, "days_early_to_complete")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "days_early_to_complete" in klass.__dict__:
            descriptor = klass.__dict__["days_early_to_complete"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_estimated_booking_value():
    assert hasattr(autopacing_inputs, "estimated_booking_value")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "estimated_booking_value" in klass.__dict__:
            descriptor = klass.__dict__["estimated_booking_value"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_dbm_io_id():
    assert hasattr(autopacing_inputs, "dbm_io_id")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "dbm_io_id" in klass.__dict__:
            descriptor = klass.__dict__["dbm_io_id"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_product_start_date():
    assert hasattr(autopacing_inputs, "product_start_date")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "product_start_date" in klass.__dict__:
            descriptor = klass.__dict__["product_start_date"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_conversions():
    assert hasattr(autopacing_inputs, "conversions")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "conversions" in klass.__dict__:
            descriptor = klass.__dict__["conversions"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_kpi_goal():
    assert hasattr(autopacing_inputs, "kpi_goal")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "kpi_goal" in klass.__dict__:
            descriptor = klass.__dict__["kpi_goal"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_min_daily_volume_percent():
    assert hasattr(autopacing_inputs, "min_daily_volume_percent")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "min_daily_volume_percent" in klass.__dict__:
            descriptor = klass.__dict__["min_daily_volume_percent"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_pacing():
    assert hasattr(autopacing_inputs, "pacing")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "pacing" in klass.__dict__:
            descriptor = klass.__dict__["pacing"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_product_end_date():
    assert hasattr(autopacing_inputs, "product_end_date")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "product_end_date" in klass.__dict__:
            descriptor = klass.__dict__["product_end_date"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_effective_impressions():
    assert hasattr(autopacing_inputs, "effective_impressions")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "effective_impressions" in klass.__dict__:
            descriptor = klass.__dict__["effective_impressions"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_cpm():
    assert hasattr(autopacing_inputs, "cpm")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "cpm" in klass.__dict__:
            descriptor = klass.__dict__["cpm"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_region():
    assert hasattr(autopacing_inputs, "region")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "region" in klass.__dict__:
            descriptor = klass.__dict__["region"]
            break
    assert isinstance(descriptor, property)

def test_autopacing_inputs_has_exchange_rate():
    assert hasattr(autopacing_inputs, "exchange_rate")
    descriptor = None
    for klass in autopacing_inputs.__mro__:
        if "exchange_rate" in klass.__dict__:
            descriptor = klass.__dict__["exchange_rate"]
            break
    assert isinstance(descriptor, property)



def test_dbm_li_sfdc_product_li_mapping_is_not_abstract():
    assert not inspect.isabstract(dbm_li_sfdc_product_li_mapping)


def test_dbm_li_sfdc_product_li_mapping_constructor_exists():
    assert callable(dbm_li_sfdc_product_li_mapping.__init__)


def test_dbm_li_sfdc_product_li_mapping_constructor_args():
    sig = inspect.signature(dbm_li_sfdc_product_li_mapping.__init__)
    params = list(sig.parameters.keys())
    assert "sfdc_product_id" in params, "Missing parameter 'sfdc_product_id'"
    assert "dub_allocation_label" in params, "Missing parameter 'dub_allocation_label'"
    assert "dbm_creative_ids" in params, "Missing parameter 'dbm_creative_ids'"
    assert "dbm_line_item_id" in params, "Missing parameter 'dbm_line_item_id'"
    assert "dbm_io_id" in params, "Missing parameter 'dbm_io_id'"

def test_dbm_li_sfdc_product_li_mapping_has_sfdc_product_id():
    assert hasattr(dbm_li_sfdc_product_li_mapping, "sfdc_product_id")
    descriptor = None
    for klass in dbm_li_sfdc_product_li_mapping.__mro__:
        if "sfdc_product_id" in klass.__dict__:
            descriptor = klass.__dict__["sfdc_product_id"]
            break
    assert isinstance(descriptor, property)

def test_dbm_li_sfdc_product_li_mapping_has_dub_allocation_label():
    assert hasattr(dbm_li_sfdc_product_li_mapping, "dub_allocation_label")
    descriptor = None
    for klass in dbm_li_sfdc_product_li_mapping.__mro__:
        if "dub_allocation_label" in klass.__dict__:
            descriptor = klass.__dict__["dub_allocation_label"]
            break
    assert isinstance(descriptor, property)

def test_dbm_li_sfdc_product_li_mapping_has_dbm_creative_ids():
    assert hasattr(dbm_li_sfdc_product_li_mapping, "dbm_creative_ids")
    descriptor = None
    for klass in dbm_li_sfdc_product_li_mapping.__mro__:
        if "dbm_creative_ids" in klass.__dict__:
            descriptor = klass.__dict__["dbm_creative_ids"]
            break
    assert isinstance(descriptor, property)

def test_dbm_li_sfdc_product_li_mapping_has_dbm_line_item_id():
    assert hasattr(dbm_li_sfdc_product_li_mapping, "dbm_line_item_id")
    descriptor = None
    for klass in dbm_li_sfdc_product_li_mapping.__mro__:
        if "dbm_line_item_id" in klass.__dict__:
            descriptor = klass.__dict__["dbm_line_item_id"]
            break
    assert isinstance(descriptor, property)

def test_dbm_li_sfdc_product_li_mapping_has_dbm_io_id():
    assert hasattr(dbm_li_sfdc_product_li_mapping, "dbm_io_id")
    descriptor = None
    for klass in dbm_li_sfdc_product_li_mapping.__mro__:
        if "dbm_io_id" in klass.__dict__:
            descriptor = klass.__dict__["dbm_io_id"]
            break
    assert isinstance(descriptor, property)



def test_creativeapproval_is_not_abstract():
    assert not inspect.isabstract(CreativeApproval)


def test_creativeapproval_constructor_exists():
    assert callable(CreativeApproval.__init__)


def test_creativeapproval_constructor_args():
    sig = inspect.signature(CreativeApproval.__init__)
    params = list(sig.parameters.keys())



def test_systemlineitemconversionpixel_is_not_abstract():
    assert not inspect.isabstract(SystemLineItemConversionPixel)


def test_systemlineitemconversionpixel_constructor_exists():
    assert callable(SystemLineItemConversionPixel.__init__)


def test_systemlineitemconversionpixel_constructor_args():
    sig = inspect.signature(SystemLineItemConversionPixel.__init__)
    params = list(sig.parameters.keys())



def test_systemcreative_is_not_abstract():
    assert not inspect.isabstract(SystemCreative)


def test_systemcreative_constructor_exists():
    assert callable(SystemCreative.__init__)


def test_systemcreative_constructor_args():
    sig = inspect.signature(SystemCreative.__init__)
    params = list(sig.parameters.keys())



def test_systemlineitem_is_not_abstract():
    assert not inspect.isabstract(SystemLineItem)


def test_systemlineitem_constructor_exists():
    assert callable(SystemLineItem.__init__)


def test_systemlineitem_constructor_args():
    sig = inspect.signature(SystemLineItem.__init__)
    params = list(sig.parameters.keys())



def test_tactic_is_not_abstract():
    assert not inspect.isabstract(Tactic)


def test_tactic_constructor_exists():
    assert callable(Tactic.__init__)


def test_tactic_constructor_args():
    sig = inspect.signature(Tactic.__init__)
    params = list(sig.parameters.keys())



def test_creativeassettactic_is_not_abstract():
    assert not inspect.isabstract(CreativeAssetTactic)


def test_creativeassettactic_constructor_exists():
    assert callable(CreativeAssetTactic.__init__)


def test_creativeassettactic_constructor_args():
    sig = inspect.signature(CreativeAssetTactic.__init__)
    params = list(sig.parameters.keys())



def test_creativeasset_is_not_abstract():
    assert not inspect.isabstract(CreativeAsset)


def test_creativeasset_constructor_exists():
    assert callable(CreativeAsset.__init__)


def test_creativeasset_constructor_args():
    sig = inspect.signature(CreativeAsset.__init__)
    params = list(sig.parameters.keys())



def test_productlineitem_is_not_abstract():
    assert not inspect.isabstract(ProductLineItem)


def test_productlineitem_constructor_exists():
    assert callable(ProductLineItem.__init__)


def test_productlineitem_constructor_args():
    sig = inspect.signature(ProductLineItem.__init__)
    params = list(sig.parameters.keys())



def test_campaigntraveleventtype_is_not_abstract():
    assert not inspect.isabstract(CampaignTravelEventType)


def test_campaigntraveleventtype_constructor_exists():
    assert callable(CampaignTravelEventType.__init__)


def test_campaigntraveleventtype_constructor_args():
    sig = inspect.signature(CampaignTravelEventType.__init__)
    params = list(sig.parameters.keys())



def test_campaignblocklistwhitelist_is_not_abstract():
    assert not inspect.isabstract(CampaignBlocklistWhitelist)


def test_campaignblocklistwhitelist_constructor_exists():
    assert callable(CampaignBlocklistWhitelist.__init__)


def test_campaignblocklistwhitelist_constructor_args():
    sig = inspect.signature(CampaignBlocklistWhitelist.__init__)
    params = list(sig.parameters.keys())



def test_spendaccountblocklistwhitelist_is_not_abstract():
    assert not inspect.isabstract(SpendAccountBlocklistWhitelist)


def test_spendaccountblocklistwhitelist_constructor_exists():
    assert callable(SpendAccountBlocklistWhitelist.__init__)


def test_spendaccountblocklistwhitelist_constructor_args():
    sig = inspect.signature(SpendAccountBlocklistWhitelist.__init__)
    params = list(sig.parameters.keys())



def test_campaign_is_not_abstract():
    assert not inspect.isabstract(Campaign)


def test_campaign_constructor_exists():
    assert callable(Campaign.__init__)


def test_campaign_constructor_args():
    sig = inspect.signature(Campaign.__init__)
    params = list(sig.parameters.keys())



def test_spendaccount_is_not_abstract():
    assert not inspect.isabstract(SpendAccount)


def test_spendaccount_constructor_exists():
    assert callable(SpendAccount.__init__)


def test_spendaccount_constructor_args():
    sig = inspect.signature(SpendAccount.__init__)
    params = list(sig.parameters.keys())



def test_agencyexcludedvertical_is_not_abstract():
    assert not inspect.isabstract(AgencyExcludedVertical)


def test_agencyexcludedvertical_constructor_exists():
    assert callable(AgencyExcludedVertical.__init__)


def test_agencyexcludedvertical_constructor_args():
    sig = inspect.signature(AgencyExcludedVertical.__init__)
    params = list(sig.parameters.keys())



def test_agencyblocklistwhitelist_is_not_abstract():
    assert not inspect.isabstract(AgencyBlocklistWhitelist)


def test_agencyblocklistwhitelist_constructor_exists():
    assert callable(AgencyBlocklistWhitelist.__init__)


def test_agencyblocklistwhitelist_constructor_args():
    sig = inspect.signature(AgencyBlocklistWhitelist.__init__)
    params = list(sig.parameters.keys())



def test_advertiserexcludedvertical_is_not_abstract():
    assert not inspect.isabstract(AdvertiserExcludedVertical)


def test_advertiserexcludedvertical_constructor_exists():
    assert callable(AdvertiserExcludedVertical.__init__)


def test_advertiserexcludedvertical_constructor_args():
    sig = inspect.signature(AdvertiserExcludedVertical.__init__)
    params = list(sig.parameters.keys())



def test_advertiserblocklistwhitelist_is_not_abstract():
    assert not inspect.isabstract(AdvertiserBlocklistWhitelist)


def test_advertiserblocklistwhitelist_constructor_exists():
    assert callable(AdvertiserBlocklistWhitelist.__init__)


def test_advertiserblocklistwhitelist_constructor_args():
    sig = inspect.signature(AdvertiserBlocklistWhitelist.__init__)
    params = list(sig.parameters.keys())



def test_systeminsertionorder_is_not_abstract():
    assert not inspect.isabstract(SystemInsertionOrder)


def test_systeminsertionorder_constructor_exists():
    assert callable(SystemInsertionOrder.__init__)


def test_systeminsertionorder_constructor_args():
    sig = inspect.signature(SystemInsertionOrder.__init__)
    params = list(sig.parameters.keys())



def test_partnerexcludedvertical_is_not_abstract():
    assert not inspect.isabstract(PartnerExcludedVertical)


def test_partnerexcludedvertical_constructor_exists():
    assert callable(PartnerExcludedVertical.__init__)


def test_partnerexcludedvertical_constructor_args():
    sig = inspect.signature(PartnerExcludedVertical.__init__)
    params = list(sig.parameters.keys())



def test_brandsafetybrandsafetylabel_is_not_abstract():
    assert not inspect.isabstract(BrandSafetyBrandSafetyLabel)


def test_brandsafetybrandsafetylabel_constructor_exists():
    assert callable(BrandSafetyBrandSafetyLabel.__init__)


def test_brandsafetybrandsafetylabel_constructor_args():
    sig = inspect.signature(BrandSafetyBrandSafetyLabel.__init__)
    params = list(sig.parameters.keys())



def test_brandsafetybrandsafetycustomsetting_is_not_abstract():
    assert not inspect.isabstract(BrandSafetyBrandSafetyCustomSetting)


def test_brandsafetybrandsafetycustomsetting_constructor_exists():
    assert callable(BrandSafetyBrandSafetyCustomSetting.__init__)


def test_brandsafetybrandsafetycustomsetting_constructor_args():
    sig = inspect.signature(BrandSafetyBrandSafetyCustomSetting.__init__)
    params = list(sig.parameters.keys())



def test_agency_is_not_abstract():
    assert not inspect.isabstract(Agency)


def test_agency_constructor_exists():
    assert callable(Agency.__init__)


def test_agency_constructor_args():
    sig = inspect.signature(Agency.__init__)
    params = list(sig.parameters.keys())
    assert "crm_id" in params, "Missing parameter 'crm_id'"

def test_agency_has_crm_id():
    assert hasattr(Agency, "crm_id")
    descriptor = None
    for klass in Agency.__mro__:
        if "crm_id" in klass.__dict__:
            descriptor = klass.__dict__["crm_id"]
            break
    assert isinstance(descriptor, property)



def test_advertiser_is_not_abstract():
    assert not inspect.isabstract(Advertiser)


def test_advertiser_constructor_exists():
    assert callable(Advertiser.__init__)


def test_advertiser_constructor_args():
    sig = inspect.signature(Advertiser.__init__)
    params = list(sig.parameters.keys())
    assert "crm_id" in params, "Missing parameter 'crm_id'"

def test_advertiser_has_crm_id():
    assert hasattr(Advertiser, "crm_id")
    descriptor = None
    for klass in Advertiser.__mro__:
        if "crm_id" in klass.__dict__:
            descriptor = klass.__dict__["crm_id"]
            break
    assert isinstance(descriptor, property)



def test_pixel_is_not_abstract():
    assert not inspect.isabstract(Pixel)


def test_pixel_constructor_exists():
    assert callable(Pixel.__init__)


def test_pixel_constructor_args():
    sig = inspect.signature(Pixel.__init__)
    params = list(sig.parameters.keys())



def test_partner_is_not_abstract():
    assert not inspect.isabstract(Partner)


def test_partner_constructor_exists():
    assert callable(Partner.__init__)


def test_partner_constructor_args():
    sig = inspect.signature(Partner.__init__)
    params = list(sig.parameters.keys())



def test_goal_is_not_abstract():
    assert not inspect.isabstract(Goal)


def test_goal_constructor_exists():
    assert callable(Goal.__init__)


def test_goal_constructor_args():
    sig = inspect.signature(Goal.__init__)
    params = list(sig.parameters.keys())



def test_brandsaftey_is_not_abstract():
    assert not inspect.isabstract(BrandSaftey)


def test_brandsaftey_constructor_exists():
    assert callable(BrandSaftey.__init__)


def test_brandsaftey_constructor_args():
    sig = inspect.signature(BrandSaftey.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_targeting_is_not_abstract():
    assert not inspect.isabstract(Targeting)


def test_targeting_constructor_exists():
    assert callable(Targeting.__init__)


def test_targeting_constructor_args():
    sig = inspect.signature(Targeting.__init__)
    params = list(sig.parameters.keys())



def test_sojernbusiness_is_not_abstract():
    assert not inspect.isabstract(SojernBusiness)


def test_sojernbusiness_constructor_exists():
    assert callable(SojernBusiness.__init__)


def test_sojernbusiness_constructor_args():
    sig = inspect.signature(SojernBusiness.__init__)
    params = list(sig.parameters.keys())



def test_recordtype_is_not_abstract():
    assert not inspect.isabstract(RecordType)


def test_recordtype_constructor_exists():
    assert callable(RecordType.__init__)


def test_recordtype_constructor_args():
    sig = inspect.signature(RecordType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "deleted" in params, "Missing parameter 'deleted'"
    assert "description" in params, "Missing parameter 'description'"
    assert "updated_by" in params, "Missing parameter 'updated_by'"
    assert "crm_id" in params, "Missing parameter 'crm_id'"

def test_recordtype_has_name():
    assert hasattr(RecordType, "name")
    descriptor = None
    for klass in RecordType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_recordtype_has_id():
    assert hasattr(RecordType, "id")
    descriptor = None
    for klass in RecordType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_recordtype_has_deleted():
    assert hasattr(RecordType, "deleted")
    descriptor = None
    for klass in RecordType.__mro__:
        if "deleted" in klass.__dict__:
            descriptor = klass.__dict__["deleted"]
            break
    assert isinstance(descriptor, property)

def test_recordtype_has_description():
    assert hasattr(RecordType, "description")
    descriptor = None
    for klass in RecordType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_recordtype_has_updated_by():
    assert hasattr(RecordType, "updated_by")
    descriptor = None
    for klass in RecordType.__mro__:
        if "updated_by" in klass.__dict__:
            descriptor = klass.__dict__["updated_by"]
            break
    assert isinstance(descriptor, property)

def test_recordtype_has_crm_id():
    assert hasattr(RecordType, "crm_id")
    descriptor = None
    for klass in RecordType.__mro__:
        if "crm_id" in klass.__dict__:
            descriptor = klass.__dict__["crm_id"]
            break
    assert isinstance(descriptor, property)



def test_appnexusclient_is_not_abstract():
    assert not inspect.isabstract(AppNexusClient)


def test_appnexusclient_constructor_exists():
    assert callable(AppNexusClient.__init__)


def test_appnexusclient_constructor_args():
    sig = inspect.signature(AppNexusClient.__init__)
    params = list(sig.parameters.keys())



def test_apnmanager_is_not_abstract():
    assert not inspect.isabstract(APNManager)


def test_apnmanager_constructor_exists():
    assert callable(APNManager.__init__)


def test_apnmanager_constructor_args():
    sig = inspect.signature(APNManager.__init__)
    params = list(sig.parameters.keys())



def test_updater_events_dataset_updater_events_daily_is_not_abstract():
    assert not inspect.isabstract(updater_events_dataset_updater_events_daily)


def test_updater_events_dataset_updater_events_daily_constructor_exists():
    assert callable(updater_events_dataset_updater_events_daily.__init__)


def test_updater_events_dataset_updater_events_daily_constructor_args():
    sig = inspect.signature(updater_events_dataset_updater_events_daily.__init__)
    params = list(sig.parameters.keys())
    assert "advertisername" in params, "Missing parameter 'advertisername'"
    assert "segments_id" in params, "Missing parameter 'segments_id'"
    assert "sojernId" in params, "Missing parameter 'sojernId'"

def test_updater_events_dataset_updater_events_daily_has_advertisername():
    assert hasattr(updater_events_dataset_updater_events_daily, "advertisername")
    descriptor = None
    for klass in updater_events_dataset_updater_events_daily.__mro__:
        if "advertisername" in klass.__dict__:
            descriptor = klass.__dict__["advertisername"]
            break
    assert isinstance(descriptor, property)

def test_updater_events_dataset_updater_events_daily_has_segments_id():
    assert hasattr(updater_events_dataset_updater_events_daily, "segments_id")
    descriptor = None
    for klass in updater_events_dataset_updater_events_daily.__mro__:
        if "segments_id" in klass.__dict__:
            descriptor = klass.__dict__["segments_id"]
            break
    assert isinstance(descriptor, property)

def test_updater_events_dataset_updater_events_daily_has_sojernId():
    assert hasattr(updater_events_dataset_updater_events_daily, "sojernId")
    descriptor = None
    for klass in updater_events_dataset_updater_events_daily.__mro__:
        if "sojernId" in klass.__dict__:
            descriptor = klass.__dict__["sojernId"]
            break
    assert isinstance(descriptor, property)



def test_smp_events_dataset_smp_events_daily_is_not_abstract():
    assert not inspect.isabstract(smp_events_dataset_smp_events_daily)


def test_smp_events_dataset_smp_events_daily_constructor_exists():
    assert callable(smp_events_dataset_smp_events_daily.__init__)


def test_smp_events_dataset_smp_events_daily_constructor_args():
    sig = inspect.signature(smp_events_dataset_smp_events_daily.__init__)
    params = list(sig.parameters.keys())
    assert "profileid" in params, "Missing parameter 'profileid'"
    assert "eventsourcename" in params, "Missing parameter 'eventsourcename'"
    assert "externalIds_id__used_as_apnid_" in params, "Missing parameter 'externalIds_id__used_as_apnid_'"
    assert "ExternalIds_Type" in params, "Missing parameter 'ExternalIds_Type'"

def test_smp_events_dataset_smp_events_daily_has_profileid():
    assert hasattr(smp_events_dataset_smp_events_daily, "profileid")
    descriptor = None
    for klass in smp_events_dataset_smp_events_daily.__mro__:
        if "profileid" in klass.__dict__:
            descriptor = klass.__dict__["profileid"]
            break
    assert isinstance(descriptor, property)

def test_smp_events_dataset_smp_events_daily_has_eventsourcename():
    assert hasattr(smp_events_dataset_smp_events_daily, "eventsourcename")
    descriptor = None
    for klass in smp_events_dataset_smp_events_daily.__mro__:
        if "eventsourcename" in klass.__dict__:
            descriptor = klass.__dict__["eventsourcename"]
            break
    assert isinstance(descriptor, property)

def test_smp_events_dataset_smp_events_daily_has_externalIds_id__used_as_apnid_():
    assert hasattr(smp_events_dataset_smp_events_daily, "externalIds_id__used_as_apnid_")
    descriptor = None
    for klass in smp_events_dataset_smp_events_daily.__mro__:
        if "externalIds_id__used_as_apnid_" in klass.__dict__:
            descriptor = klass.__dict__["externalIds_id__used_as_apnid_"]
            break
    assert isinstance(descriptor, property)

def test_smp_events_dataset_smp_events_daily_has_ExternalIds_Type():
    assert hasattr(smp_events_dataset_smp_events_daily, "ExternalIds_Type")
    descriptor = None
    for klass in smp_events_dataset_smp_events_daily.__mro__:
        if "ExternalIds_Type" in klass.__dict__:
            descriptor = klass.__dict__["ExternalIds_Type"]
            break
    assert isinstance(descriptor, property)



def test_gcsmanager_is_not_abstract():
    assert not inspect.isabstract(GCSManager)


def test_gcsmanager_constructor_exists():
    assert callable(GCSManager.__init__)


def test_gcsmanager_constructor_args():
    sig = inspect.signature(GCSManager.__init__)
    params = list(sig.parameters.keys())



def test_gcemanager_is_not_abstract():
    assert not inspect.isabstract(GCEManager)


def test_gcemanager_constructor_exists():
    assert callable(GCEManager.__init__)


def test_gcemanager_constructor_args():
    sig = inspect.signature(GCEManager.__init__)
    params = list(sig.parameters.keys())



def test_fbmanager_is_not_abstract():
    assert not inspect.isabstract(FBManager)


def test_fbmanager_constructor_exists():
    assert callable(FBManager.__init__)


def test_fbmanager_constructor_args():
    sig = inspect.signature(FBManager.__init__)
    params = list(sig.parameters.keys())



def test_dsmanager_is_not_abstract():
    assert not inspect.isabstract(DSManager)


def test_dsmanager_constructor_exists():
    assert callable(DSManager.__init__)


def test_dsmanager_constructor_args():
    sig = inspect.signature(DSManager.__init__)
    params = list(sig.parameters.keys())



def test_cloudsqlmanager_is_not_abstract():
    assert not inspect.isabstract(CloudSQLManager)


def test_cloudsqlmanager_constructor_exists():
    assert callable(CloudSQLManager.__init__)


def test_cloudsqlmanager_constructor_args():
    sig = inspect.signature(CloudSQLManager.__init__)
    params = list(sig.parameters.keys())



def test_dcmmanager_is_not_abstract():
    assert not inspect.isabstract(DCMManager)


def test_dcmmanager_constructor_exists():
    assert callable(DCMManager.__init__)


def test_dcmmanager_constructor_args():
    sig = inspect.signature(DCMManager.__init__)
    params = list(sig.parameters.keys())



def test_dcsmanager_is_not_abstract():
    assert not inspect.isabstract(DCSManager)


def test_dcsmanager_constructor_exists():
    assert callable(DCSManager.__init__)


def test_dcsmanager_constructor_args():
    sig = inspect.signature(DCSManager.__init__)
    params = list(sig.parameters.keys())



def test_dbmmanager_is_not_abstract():
    assert not inspect.isabstract(DBMManager)


def test_dbmmanager_constructor_exists():
    assert callable(DBMManager.__init__)


def test_dbmmanager_constructor_args():
    sig = inspect.signature(DBMManager.__init__)
    params = list(sig.parameters.keys())



def test_salesforcebulkmanager_is_not_abstract():
    assert not inspect.isabstract(SalesforceBulkManager)


def test_salesforcebulkmanager_constructor_exists():
    assert callable(SalesforceBulkManager.__init__)


def test_salesforcebulkmanager_constructor_args():
    sig = inspect.signature(SalesforceBulkManager.__init__)
    params = list(sig.parameters.keys())



def test_salesforcemanager_is_not_abstract():
    assert not inspect.isabstract(Salesforcemanager)


def test_salesforcemanager_constructor_exists():
    assert callable(Salesforcemanager.__init__)


def test_salesforcemanager_constructor_args():
    sig = inspect.signature(Salesforcemanager.__init__)
    params = list(sig.parameters.keys())



def test_whutils_is_not_abstract():
    assert not inspect.isabstract(WHUtils)


def test_whutils_constructor_exists():
    assert callable(WHUtils.__init__)


def test_whutils_constructor_args():
    sig = inspect.signature(WHUtils.__init__)
    params = list(sig.parameters.keys())



def test_bqtable_is_not_abstract():
    assert not inspect.isabstract(BQTable)


def test_bqtable_constructor_exists():
    assert callable(BQTable.__init__)


def test_bqtable_constructor_args():
    sig = inspect.signature(BQTable.__init__)
    params = list(sig.parameters.keys())



def test_bqjoberror_is_not_abstract():
    assert not inspect.isabstract(BQJobError)


def test_bqjoberror_constructor_exists():
    assert callable(BQJobError.__init__)


def test_bqjoberror_constructor_args():
    sig = inspect.signature(BQJobError.__init__)
    params = list(sig.parameters.keys())



def test_oauth2client_client_googlecredentials_is_not_abstract():
    assert not inspect.isabstract(Oauth2client_client_GoogleCredentials)


def test_oauth2client_client_googlecredentials_constructor_exists():
    assert callable(Oauth2client_client_GoogleCredentials.__init__)


def test_oauth2client_client_googlecredentials_constructor_args():
    sig = inspect.signature(Oauth2client_client_GoogleCredentials.__init__)
    params = list(sig.parameters.keys())



def test_gcpmanager_is_not_abstract():
    assert not inspect.isabstract(GCPManager)


def test_gcpmanager_constructor_exists():
    assert callable(GCPManager.__init__)


def test_gcpmanager_constructor_args():
    sig = inspect.signature(GCPManager.__init__)
    params = list(sig.parameters.keys())



def test_googleapiclient_discovery_is_not_abstract():
    assert not inspect.isabstract(googleapiclient_discovery)


def test_googleapiclient_discovery_constructor_exists():
    assert callable(googleapiclient_discovery.__init__)


def test_googleapiclient_discovery_constructor_args():
    sig = inspect.signature(googleapiclient_discovery.__init__)
    params = list(sig.parameters.keys())



def test_bqmanager_is_not_abstract():
    assert not inspect.isabstract(BQManager)


def test_bqmanager_constructor_exists():
    assert callable(BQManager.__init__)


def test_bqmanager_constructor_args():
    sig = inspect.signature(BQManager.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
APNAdv_strategy = st.builds(
    APNAdv,
)
AppNexus_strategy = st.builds(
    AppNexus,
)
RestClient_strategy = st.builds(
    RestClient,
)
APNModelFactory_strategy = st.builds(
    APNModelFactory,
)
Class2_strategy = st.builds(
    Class2,
)
APNLineItemModelService_strategy = st.builds(
    APNLineItemModelService,
)
ModelService_Interface_strategy = st.builds(
    ModelService_Interface,
)
Model_Interface_strategy = st.builds(
    Model_Interface,
)
GenericModel_strategy = st.builds(
    GenericModel,
)
APNRepository_Interface_strategy = st.builds(
    APNRepository_Interface,
)
APNCache_Interface_strategy = st.builds(
    APNCache_Interface,
)
APNStore_Interface_strategy = st.builds(
    APNStore_Interface,
)
APNProgrammaticModel_strategy = st.builds(
    APNProgrammaticModel,
)
ProgrammaticModel_Interface_strategy = st.builds(
    ProgrammaticModel_Interface,
)
APNModel_strategy = st.builds(
    APNModel,
)
APNLineItem_strategy = st.builds(
    APNLineItem,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
APNAdvertiser_strategy = st.builds(
    APNAdvertiser,
)
BidAdjuster_strategy = st.builds(
    BidAdjuster,
)
IOManager_strategy = st.builds(
    IOManager,
)
autopacing_inputs_strategy = st.builds(
    autopacing_inputs,
    cvr=
        safe_text,
    impressions=
        safe_text,
    sojern_goal_rae=
        safe_text,
    sfdc_opportunity_id=
        safe_text,
    region1=
        safe_text,
    percentage_impression_credit=
        safe_text,
    minimum_margin=
        safe_text,
    product_type=
        safe_text,
    minimum_partner_data_delivery_percent=
        safe_text,
    avg_price_usd=
        safe_text,
    adjust_bids=
        safe_text,
    end_date=
        safe_text,
    expected_click_credit=
        safe_text,
    account_manager=
        safe_text,
    sfdc_product_id=
        safe_text,
    min_daily_volume=
        safe_text,
    billing_currency=
        safe_text,
    start_date=
        safe_text,
    cpx=
        safe_text,
    on_off=
        safe_text,
    percentage_conversion_credit=
        safe_text,
    hours_early_to_complete=
        safe_text,
    goal_type=
        safe_text,
    days_early_to_complete=
        safe_text,
    estimated_booking_value=
        safe_text,
    dbm_io_id=
        safe_text,
    product_start_date=
        safe_text,
    conversions=
        safe_text,
    kpi_goal=
        safe_text,
    min_daily_volume_percent=
        safe_text,
    pacing=
        safe_text,
    product_end_date=
        safe_text,
    effective_impressions=
        safe_text,
    cpm=
        safe_text,
    region=
        safe_text,
    exchange_rate=
        safe_text
)
dbm_li_sfdc_product_li_mapping_strategy = st.builds(
    dbm_li_sfdc_product_li_mapping,
    sfdc_product_id=
        safe_text,
    dub_allocation_label=
        safe_text,
    dbm_creative_ids=
        safe_text,
    dbm_line_item_id=
        safe_text,
    dbm_io_id=
        safe_text
)
CreativeApproval_strategy = st.builds(
    CreativeApproval,
)
SystemLineItemConversionPixel_strategy = st.builds(
    SystemLineItemConversionPixel,
)
SystemCreative_strategy = st.builds(
    SystemCreative,
)
SystemLineItem_strategy = st.builds(
    SystemLineItem,
)
Tactic_strategy = st.builds(
    Tactic,
)
CreativeAssetTactic_strategy = st.builds(
    CreativeAssetTactic,
)
CreativeAsset_strategy = st.builds(
    CreativeAsset,
)
ProductLineItem_strategy = st.builds(
    ProductLineItem,
)
CampaignTravelEventType_strategy = st.builds(
    CampaignTravelEventType,
)
CampaignBlocklistWhitelist_strategy = st.builds(
    CampaignBlocklistWhitelist,
)
SpendAccountBlocklistWhitelist_strategy = st.builds(
    SpendAccountBlocklistWhitelist,
)
Campaign_strategy = st.builds(
    Campaign,
)
SpendAccount_strategy = st.builds(
    SpendAccount,
)
AgencyExcludedVertical_strategy = st.builds(
    AgencyExcludedVertical,
)
AgencyBlocklistWhitelist_strategy = st.builds(
    AgencyBlocklistWhitelist,
)
AdvertiserExcludedVertical_strategy = st.builds(
    AdvertiserExcludedVertical,
)
AdvertiserBlocklistWhitelist_strategy = st.builds(
    AdvertiserBlocklistWhitelist,
)
SystemInsertionOrder_strategy = st.builds(
    SystemInsertionOrder,
)
PartnerExcludedVertical_strategy = st.builds(
    PartnerExcludedVertical,
)
BrandSafetyBrandSafetyLabel_strategy = st.builds(
    BrandSafetyBrandSafetyLabel,
)
BrandSafetyBrandSafetyCustomSetting_strategy = st.builds(
    BrandSafetyBrandSafetyCustomSetting,
)
Agency_strategy = st.builds(
    Agency,
    crm_id=
        safe_text
)
Advertiser_strategy = st.builds(
    Advertiser,
    crm_id=
        safe_text
)
Pixel_strategy = st.builds(
    Pixel,
)
Partner_strategy = st.builds(
    Partner,
)
Goal_strategy = st.builds(
    Goal,
)
BrandSaftey_strategy = st.builds(
    BrandSaftey,
)
User_strategy = st.builds(
    User,
)
Targeting_strategy = st.builds(
    Targeting,
)
SojernBusiness_strategy = st.builds(
    SojernBusiness,
)
RecordType_strategy = st.builds(
    RecordType,
    name=
        safe_text,
    id=
        safe_text,
    deleted=
        safe_text,
    description=
        safe_text,
    updated_by=
        safe_text,
    crm_id=
        safe_text
)
AppNexusClient_strategy = st.builds(
    AppNexusClient,
)
APNManager_strategy = st.builds(
    APNManager,
)
updater_events_dataset_updater_events_daily_strategy = st.builds(
    updater_events_dataset_updater_events_daily,
    advertisername=
        safe_text,
    segments_id=
        safe_text,
    sojernId=
        safe_text
)
smp_events_dataset_smp_events_daily_strategy = st.builds(
    smp_events_dataset_smp_events_daily,
    profileid=
        safe_text,
    eventsourcename=
        safe_text,
    externalIds_id__used_as_apnid_=
        safe_text,
    ExternalIds_Type=
        safe_text
)
GCSManager_strategy = st.builds(
    GCSManager,
)
GCEManager_strategy = st.builds(
    GCEManager,
)
FBManager_strategy = st.builds(
    FBManager,
)
DSManager_strategy = st.builds(
    DSManager,
)
CloudSQLManager_strategy = st.builds(
    CloudSQLManager,
)
DCMManager_strategy = st.builds(
    DCMManager,
)
DCSManager_strategy = st.builds(
    DCSManager,
)
DBMManager_strategy = st.builds(
    DBMManager,
)
SalesforceBulkManager_strategy = st.builds(
    SalesforceBulkManager,
)
Salesforcemanager_strategy = st.builds(
    Salesforcemanager,
)
WHUtils_strategy = st.builds(
    WHUtils,
)
BQTable_strategy = st.builds(
    BQTable,
)
BQJobError_strategy = st.builds(
    BQJobError,
)
Oauth2client_client_GoogleCredentials_strategy = st.builds(
    Oauth2client_client_GoogleCredentials,
)
GCPManager_strategy = st.builds(
    GCPManager,
)
googleapiclient_discovery_strategy = st.builds(
    googleapiclient_discovery,
)
BQManager_strategy = st.builds(
    BQManager,
)

@given(instance=APNAdv_strategy)
@settings(max_examples=50)
def test_apnadv_instantiation(instance):
    assert isinstance(instance, APNAdv)

@given(instance=AppNexus_strategy)
@settings(max_examples=50)
def test_appnexus_instantiation(instance):
    assert isinstance(instance, AppNexus)

@given(instance=RestClient_strategy)
@settings(max_examples=50)
def test_restclient_instantiation(instance):
    assert isinstance(instance, RestClient)

@given(instance=APNModelFactory_strategy)
@settings(max_examples=50)
def test_apnmodelfactory_instantiation(instance):
    assert isinstance(instance, APNModelFactory)

@given(instance=Class2_strategy)
@settings(max_examples=50)
def test_class2_instantiation(instance):
    assert isinstance(instance, Class2)

@given(instance=APNLineItemModelService_strategy)
@settings(max_examples=50)
def test_apnlineitemmodelservice_instantiation(instance):
    assert isinstance(instance, APNLineItemModelService)

@given(instance=ModelService_Interface_strategy)
@settings(max_examples=50)
def test_modelservice_interface_instantiation(instance):
    assert isinstance(instance, ModelService_Interface)

@given(instance=Model_Interface_strategy)
@settings(max_examples=50)
def test_model_interface_instantiation(instance):
    assert isinstance(instance, Model_Interface)

@given(instance=GenericModel_strategy)
@settings(max_examples=50)
def test_genericmodel_instantiation(instance):
    assert isinstance(instance, GenericModel)

@given(instance=APNRepository_Interface_strategy)
@settings(max_examples=50)
def test_apnrepository_interface_instantiation(instance):
    assert isinstance(instance, APNRepository_Interface)

@given(instance=APNCache_Interface_strategy)
@settings(max_examples=50)
def test_apncache_interface_instantiation(instance):
    assert isinstance(instance, APNCache_Interface)

@given(instance=APNStore_Interface_strategy)
@settings(max_examples=50)
def test_apnstore_interface_instantiation(instance):
    assert isinstance(instance, APNStore_Interface)

@given(instance=APNProgrammaticModel_strategy)
@settings(max_examples=50)
def test_apnprogrammaticmodel_instantiation(instance):
    assert isinstance(instance, APNProgrammaticModel)

@given(instance=ProgrammaticModel_Interface_strategy)
@settings(max_examples=50)
def test_programmaticmodel_interface_instantiation(instance):
    assert isinstance(instance, ProgrammaticModel_Interface)

@given(instance=APNModel_strategy)
@settings(max_examples=50)
def test_apnmodel_instantiation(instance):
    assert isinstance(instance, APNModel)

@given(instance=APNLineItem_strategy)
@settings(max_examples=50)
def test_apnlineitem_instantiation(instance):
    assert isinstance(instance, APNLineItem)



@given(instance=APNLineItem_strategy)
def test_apnlineitem_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=APNLineItem_strategy)
def test_apnlineitem_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=APNAdvertiser_strategy)
@settings(max_examples=50)
def test_apnadvertiser_instantiation(instance):
    assert isinstance(instance, APNAdvertiser)

@given(instance=BidAdjuster_strategy)
@settings(max_examples=50)
def test_bidadjuster_instantiation(instance):
    assert isinstance(instance, BidAdjuster)

@given(instance=IOManager_strategy)
@settings(max_examples=50)
def test_iomanager_instantiation(instance):
    assert isinstance(instance, IOManager)

@given(instance=autopacing_inputs_strategy)
@settings(max_examples=50)
def test_autopacing_inputs_instantiation(instance):
    assert isinstance(instance, autopacing_inputs)



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_cvr_setter(instance):
    original = instance.cvr
    instance.cvr = original
    assert instance.cvr == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_impressions_setter(instance):
    original = instance.impressions
    instance.impressions = original
    assert instance.impressions == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_sojern_goal_rae_setter(instance):
    original = instance.sojern_goal_rae
    instance.sojern_goal_rae = original
    assert instance.sojern_goal_rae == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_sfdc_opportunity_id_setter(instance):
    original = instance.sfdc_opportunity_id
    instance.sfdc_opportunity_id = original
    assert instance.sfdc_opportunity_id == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_region1_setter(instance):
    original = instance.region1
    instance.region1 = original
    assert instance.region1 == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_percentage_impression_credit_setter(instance):
    original = instance.percentage_impression_credit
    instance.percentage_impression_credit = original
    assert instance.percentage_impression_credit == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_minimum_margin_setter(instance):
    original = instance.minimum_margin
    instance.minimum_margin = original
    assert instance.minimum_margin == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_product_type_setter(instance):
    original = instance.product_type
    instance.product_type = original
    assert instance.product_type == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_minimum_partner_data_delivery_percent_setter(instance):
    original = instance.minimum_partner_data_delivery_percent
    instance.minimum_partner_data_delivery_percent = original
    assert instance.minimum_partner_data_delivery_percent == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_avg_price_usd_setter(instance):
    original = instance.avg_price_usd
    instance.avg_price_usd = original
    assert instance.avg_price_usd == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_adjust_bids_setter(instance):
    original = instance.adjust_bids
    instance.adjust_bids = original
    assert instance.adjust_bids == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_end_date_setter(instance):
    original = instance.end_date
    instance.end_date = original
    assert instance.end_date == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_expected_click_credit_setter(instance):
    original = instance.expected_click_credit
    instance.expected_click_credit = original
    assert instance.expected_click_credit == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_account_manager_setter(instance):
    original = instance.account_manager
    instance.account_manager = original
    assert instance.account_manager == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_sfdc_product_id_setter(instance):
    original = instance.sfdc_product_id
    instance.sfdc_product_id = original
    assert instance.sfdc_product_id == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_min_daily_volume_setter(instance):
    original = instance.min_daily_volume
    instance.min_daily_volume = original
    assert instance.min_daily_volume == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_billing_currency_setter(instance):
    original = instance.billing_currency
    instance.billing_currency = original
    assert instance.billing_currency == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_start_date_setter(instance):
    original = instance.start_date
    instance.start_date = original
    assert instance.start_date == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_cpx_setter(instance):
    original = instance.cpx
    instance.cpx = original
    assert instance.cpx == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_on_off_setter(instance):
    original = instance.on_off
    instance.on_off = original
    assert instance.on_off == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_percentage_conversion_credit_setter(instance):
    original = instance.percentage_conversion_credit
    instance.percentage_conversion_credit = original
    assert instance.percentage_conversion_credit == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_hours_early_to_complete_setter(instance):
    original = instance.hours_early_to_complete
    instance.hours_early_to_complete = original
    assert instance.hours_early_to_complete == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_goal_type_setter(instance):
    original = instance.goal_type
    instance.goal_type = original
    assert instance.goal_type == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_days_early_to_complete_setter(instance):
    original = instance.days_early_to_complete
    instance.days_early_to_complete = original
    assert instance.days_early_to_complete == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_estimated_booking_value_setter(instance):
    original = instance.estimated_booking_value
    instance.estimated_booking_value = original
    assert instance.estimated_booking_value == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_dbm_io_id_setter(instance):
    original = instance.dbm_io_id
    instance.dbm_io_id = original
    assert instance.dbm_io_id == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_product_start_date_setter(instance):
    original = instance.product_start_date
    instance.product_start_date = original
    assert instance.product_start_date == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_conversions_setter(instance):
    original = instance.conversions
    instance.conversions = original
    assert instance.conversions == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_kpi_goal_setter(instance):
    original = instance.kpi_goal
    instance.kpi_goal = original
    assert instance.kpi_goal == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_min_daily_volume_percent_setter(instance):
    original = instance.min_daily_volume_percent
    instance.min_daily_volume_percent = original
    assert instance.min_daily_volume_percent == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_pacing_setter(instance):
    original = instance.pacing
    instance.pacing = original
    assert instance.pacing == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_product_end_date_setter(instance):
    original = instance.product_end_date
    instance.product_end_date = original
    assert instance.product_end_date == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_effective_impressions_setter(instance):
    original = instance.effective_impressions
    instance.effective_impressions = original
    assert instance.effective_impressions == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_cpm_setter(instance):
    original = instance.cpm
    instance.cpm = original
    assert instance.cpm == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_region_setter(instance):
    original = instance.region
    instance.region = original
    assert instance.region == original



@given(instance=autopacing_inputs_strategy)
def test_autopacing_inputs_exchange_rate_setter(instance):
    original = instance.exchange_rate
    instance.exchange_rate = original
    assert instance.exchange_rate == original

@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
@settings(max_examples=50)
def test_dbm_li_sfdc_product_li_mapping_instantiation(instance):
    assert isinstance(instance, dbm_li_sfdc_product_li_mapping)



@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
def test_dbm_li_sfdc_product_li_mapping_sfdc_product_id_setter(instance):
    original = instance.sfdc_product_id
    instance.sfdc_product_id = original
    assert instance.sfdc_product_id == original



@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
def test_dbm_li_sfdc_product_li_mapping_dub_allocation_label_setter(instance):
    original = instance.dub_allocation_label
    instance.dub_allocation_label = original
    assert instance.dub_allocation_label == original



@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
def test_dbm_li_sfdc_product_li_mapping_dbm_creative_ids_setter(instance):
    original = instance.dbm_creative_ids
    instance.dbm_creative_ids = original
    assert instance.dbm_creative_ids == original



@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
def test_dbm_li_sfdc_product_li_mapping_dbm_line_item_id_setter(instance):
    original = instance.dbm_line_item_id
    instance.dbm_line_item_id = original
    assert instance.dbm_line_item_id == original



@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
def test_dbm_li_sfdc_product_li_mapping_dbm_io_id_setter(instance):
    original = instance.dbm_io_id
    instance.dbm_io_id = original
    assert instance.dbm_io_id == original

@given(instance=CreativeApproval_strategy)
@settings(max_examples=50)
def test_creativeapproval_instantiation(instance):
    assert isinstance(instance, CreativeApproval)

@given(instance=SystemLineItemConversionPixel_strategy)
@settings(max_examples=50)
def test_systemlineitemconversionpixel_instantiation(instance):
    assert isinstance(instance, SystemLineItemConversionPixel)

@given(instance=SystemCreative_strategy)
@settings(max_examples=50)
def test_systemcreative_instantiation(instance):
    assert isinstance(instance, SystemCreative)

@given(instance=SystemLineItem_strategy)
@settings(max_examples=50)
def test_systemlineitem_instantiation(instance):
    assert isinstance(instance, SystemLineItem)

@given(instance=Tactic_strategy)
@settings(max_examples=50)
def test_tactic_instantiation(instance):
    assert isinstance(instance, Tactic)

@given(instance=CreativeAssetTactic_strategy)
@settings(max_examples=50)
def test_creativeassettactic_instantiation(instance):
    assert isinstance(instance, CreativeAssetTactic)

@given(instance=CreativeAsset_strategy)
@settings(max_examples=50)
def test_creativeasset_instantiation(instance):
    assert isinstance(instance, CreativeAsset)

@given(instance=ProductLineItem_strategy)
@settings(max_examples=50)
def test_productlineitem_instantiation(instance):
    assert isinstance(instance, ProductLineItem)

@given(instance=CampaignTravelEventType_strategy)
@settings(max_examples=50)
def test_campaigntraveleventtype_instantiation(instance):
    assert isinstance(instance, CampaignTravelEventType)

@given(instance=CampaignBlocklistWhitelist_strategy)
@settings(max_examples=50)
def test_campaignblocklistwhitelist_instantiation(instance):
    assert isinstance(instance, CampaignBlocklistWhitelist)

@given(instance=SpendAccountBlocklistWhitelist_strategy)
@settings(max_examples=50)
def test_spendaccountblocklistwhitelist_instantiation(instance):
    assert isinstance(instance, SpendAccountBlocklistWhitelist)

@given(instance=Campaign_strategy)
@settings(max_examples=50)
def test_campaign_instantiation(instance):
    assert isinstance(instance, Campaign)

@given(instance=SpendAccount_strategy)
@settings(max_examples=50)
def test_spendaccount_instantiation(instance):
    assert isinstance(instance, SpendAccount)

@given(instance=AgencyExcludedVertical_strategy)
@settings(max_examples=50)
def test_agencyexcludedvertical_instantiation(instance):
    assert isinstance(instance, AgencyExcludedVertical)

@given(instance=AgencyBlocklistWhitelist_strategy)
@settings(max_examples=50)
def test_agencyblocklistwhitelist_instantiation(instance):
    assert isinstance(instance, AgencyBlocklistWhitelist)

@given(instance=AdvertiserExcludedVertical_strategy)
@settings(max_examples=50)
def test_advertiserexcludedvertical_instantiation(instance):
    assert isinstance(instance, AdvertiserExcludedVertical)

@given(instance=AdvertiserBlocklistWhitelist_strategy)
@settings(max_examples=50)
def test_advertiserblocklistwhitelist_instantiation(instance):
    assert isinstance(instance, AdvertiserBlocklistWhitelist)

@given(instance=SystemInsertionOrder_strategy)
@settings(max_examples=50)
def test_systeminsertionorder_instantiation(instance):
    assert isinstance(instance, SystemInsertionOrder)

@given(instance=PartnerExcludedVertical_strategy)
@settings(max_examples=50)
def test_partnerexcludedvertical_instantiation(instance):
    assert isinstance(instance, PartnerExcludedVertical)

@given(instance=BrandSafetyBrandSafetyLabel_strategy)
@settings(max_examples=50)
def test_brandsafetybrandsafetylabel_instantiation(instance):
    assert isinstance(instance, BrandSafetyBrandSafetyLabel)

@given(instance=BrandSafetyBrandSafetyCustomSetting_strategy)
@settings(max_examples=50)
def test_brandsafetybrandsafetycustomsetting_instantiation(instance):
    assert isinstance(instance, BrandSafetyBrandSafetyCustomSetting)

@given(instance=Agency_strategy)
@settings(max_examples=50)
def test_agency_instantiation(instance):
    assert isinstance(instance, Agency)



@given(instance=Agency_strategy)
def test_agency_crm_id_setter(instance):
    original = instance.crm_id
    instance.crm_id = original
    assert instance.crm_id == original

@given(instance=Advertiser_strategy)
@settings(max_examples=50)
def test_advertiser_instantiation(instance):
    assert isinstance(instance, Advertiser)



@given(instance=Advertiser_strategy)
def test_advertiser_crm_id_setter(instance):
    original = instance.crm_id
    instance.crm_id = original
    assert instance.crm_id == original

@given(instance=Pixel_strategy)
@settings(max_examples=50)
def test_pixel_instantiation(instance):
    assert isinstance(instance, Pixel)

@given(instance=Partner_strategy)
@settings(max_examples=50)
def test_partner_instantiation(instance):
    assert isinstance(instance, Partner)

@given(instance=Goal_strategy)
@settings(max_examples=50)
def test_goal_instantiation(instance):
    assert isinstance(instance, Goal)

@given(instance=BrandSaftey_strategy)
@settings(max_examples=50)
def test_brandsaftey_instantiation(instance):
    assert isinstance(instance, BrandSaftey)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=Targeting_strategy)
@settings(max_examples=50)
def test_targeting_instantiation(instance):
    assert isinstance(instance, Targeting)

@given(instance=SojernBusiness_strategy)
@settings(max_examples=50)
def test_sojernbusiness_instantiation(instance):
    assert isinstance(instance, SojernBusiness)

@given(instance=RecordType_strategy)
@settings(max_examples=50)
def test_recordtype_instantiation(instance):
    assert isinstance(instance, RecordType)



@given(instance=RecordType_strategy)
def test_recordtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=RecordType_strategy)
def test_recordtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=RecordType_strategy)
def test_recordtype_deleted_setter(instance):
    original = instance.deleted
    instance.deleted = original
    assert instance.deleted == original



@given(instance=RecordType_strategy)
def test_recordtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=RecordType_strategy)
def test_recordtype_updated_by_setter(instance):
    original = instance.updated_by
    instance.updated_by = original
    assert instance.updated_by == original



@given(instance=RecordType_strategy)
def test_recordtype_crm_id_setter(instance):
    original = instance.crm_id
    instance.crm_id = original
    assert instance.crm_id == original

@given(instance=AppNexusClient_strategy)
@settings(max_examples=50)
def test_appnexusclient_instantiation(instance):
    assert isinstance(instance, AppNexusClient)

@given(instance=APNManager_strategy)
@settings(max_examples=50)
def test_apnmanager_instantiation(instance):
    assert isinstance(instance, APNManager)

@given(instance=updater_events_dataset_updater_events_daily_strategy)
@settings(max_examples=50)
def test_updater_events_dataset_updater_events_daily_instantiation(instance):
    assert isinstance(instance, updater_events_dataset_updater_events_daily)



@given(instance=updater_events_dataset_updater_events_daily_strategy)
def test_updater_events_dataset_updater_events_daily_advertisername_setter(instance):
    original = instance.advertisername
    instance.advertisername = original
    assert instance.advertisername == original



@given(instance=updater_events_dataset_updater_events_daily_strategy)
def test_updater_events_dataset_updater_events_daily_segments_id_setter(instance):
    original = instance.segments_id
    instance.segments_id = original
    assert instance.segments_id == original



@given(instance=updater_events_dataset_updater_events_daily_strategy)
def test_updater_events_dataset_updater_events_daily_sojernId_setter(instance):
    original = instance.sojernId
    instance.sojernId = original
    assert instance.sojernId == original

@given(instance=smp_events_dataset_smp_events_daily_strategy)
@settings(max_examples=50)
def test_smp_events_dataset_smp_events_daily_instantiation(instance):
    assert isinstance(instance, smp_events_dataset_smp_events_daily)



@given(instance=smp_events_dataset_smp_events_daily_strategy)
def test_smp_events_dataset_smp_events_daily_profileid_setter(instance):
    original = instance.profileid
    instance.profileid = original
    assert instance.profileid == original



@given(instance=smp_events_dataset_smp_events_daily_strategy)
def test_smp_events_dataset_smp_events_daily_eventsourcename_setter(instance):
    original = instance.eventsourcename
    instance.eventsourcename = original
    assert instance.eventsourcename == original



@given(instance=smp_events_dataset_smp_events_daily_strategy)
def test_smp_events_dataset_smp_events_daily_externalIds_id__used_as_apnid__setter(instance):
    original = instance.externalIds_id__used_as_apnid_
    instance.externalIds_id__used_as_apnid_ = original
    assert instance.externalIds_id__used_as_apnid_ == original



@given(instance=smp_events_dataset_smp_events_daily_strategy)
def test_smp_events_dataset_smp_events_daily_ExternalIds_Type_setter(instance):
    original = instance.ExternalIds_Type
    instance.ExternalIds_Type = original
    assert instance.ExternalIds_Type == original

@given(instance=GCSManager_strategy)
@settings(max_examples=50)
def test_gcsmanager_instantiation(instance):
    assert isinstance(instance, GCSManager)

@given(instance=GCEManager_strategy)
@settings(max_examples=50)
def test_gcemanager_instantiation(instance):
    assert isinstance(instance, GCEManager)

@given(instance=FBManager_strategy)
@settings(max_examples=50)
def test_fbmanager_instantiation(instance):
    assert isinstance(instance, FBManager)

@given(instance=DSManager_strategy)
@settings(max_examples=50)
def test_dsmanager_instantiation(instance):
    assert isinstance(instance, DSManager)

@given(instance=CloudSQLManager_strategy)
@settings(max_examples=50)
def test_cloudsqlmanager_instantiation(instance):
    assert isinstance(instance, CloudSQLManager)

@given(instance=DCMManager_strategy)
@settings(max_examples=50)
def test_dcmmanager_instantiation(instance):
    assert isinstance(instance, DCMManager)

@given(instance=DCSManager_strategy)
@settings(max_examples=50)
def test_dcsmanager_instantiation(instance):
    assert isinstance(instance, DCSManager)

@given(instance=DBMManager_strategy)
@settings(max_examples=50)
def test_dbmmanager_instantiation(instance):
    assert isinstance(instance, DBMManager)

@given(instance=SalesforceBulkManager_strategy)
@settings(max_examples=50)
def test_salesforcebulkmanager_instantiation(instance):
    assert isinstance(instance, SalesforceBulkManager)

@given(instance=Salesforcemanager_strategy)
@settings(max_examples=50)
def test_salesforcemanager_instantiation(instance):
    assert isinstance(instance, Salesforcemanager)

@given(instance=WHUtils_strategy)
@settings(max_examples=50)
def test_whutils_instantiation(instance):
    assert isinstance(instance, WHUtils)

@given(instance=BQTable_strategy)
@settings(max_examples=50)
def test_bqtable_instantiation(instance):
    assert isinstance(instance, BQTable)

@given(instance=BQJobError_strategy)
@settings(max_examples=50)
def test_bqjoberror_instantiation(instance):
    assert isinstance(instance, BQJobError)

@given(instance=Oauth2client_client_GoogleCredentials_strategy)
@settings(max_examples=50)
def test_oauth2client_client_googlecredentials_instantiation(instance):
    assert isinstance(instance, Oauth2client_client_GoogleCredentials)

@given(instance=GCPManager_strategy)
@settings(max_examples=50)
def test_gcpmanager_instantiation(instance):
    assert isinstance(instance, GCPManager)

@given(instance=googleapiclient_discovery_strategy)
@settings(max_examples=50)
def test_googleapiclient_discovery_instantiation(instance):
    assert isinstance(instance, googleapiclient_discovery)

@given(instance=BQManager_strategy)
@settings(max_examples=50)
def test_bqmanager_instantiation(instance):
    assert isinstance(instance, BQManager)
