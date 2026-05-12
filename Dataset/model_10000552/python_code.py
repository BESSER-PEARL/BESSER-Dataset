from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class AppNexus:

    pass


class APNAdv:

    pass


class RestClient:

    pass


class APNModelFactory:

    pass


class Class2:

    pass


class APNLineItemModelService:

    pass


class ModelService_Interface:

    pass


class Model_Interface:

    pass


class GenericModel:

    pass


class APNRepository_Interface:

    pass


class APNCache_Interface:

    pass


class APNStore_Interface:

    pass


class APNProgrammaticModel:

    pass


class ProgrammaticModel_Interface:

    pass


class APNModel:

    pass


class APNLineItem:

    def __init__(self, attribute: str, attribute2: str, APNModel_APNLineItem_15: set["APNModel"] = None, APNLineItem_APNModel_018: set["APNModel"] = None, APNLineItemModelService_APNLineItem_121: "APNLineItemModelService" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.APNModel_APNLineItem_15 = APNModel_APNLineItem_15 if APNModel_APNLineItem_15 is not None else set()
        self.APNLineItem_APNModel_018 = APNLineItem_APNModel_018 if APNLineItem_APNModel_018 is not None else set()
        self.APNLineItemModelService_APNLineItem_121 = APNLineItemModelService_APNLineItem_121
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def APNLineItemModelService_APNLineItem_121(self):
        return self.__APNLineItemModelService_APNLineItem_121
    @APNLineItemModelService_APNLineItem_121.setter
    def APNLineItemModelService_APNLineItem_121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_APNLineItem__APNLineItemModelService_APNLineItem_121", None)
        self.__APNLineItemModelService_APNLineItem_121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "APNLineItemModelService_APNLineItem_020"):
                opp_val = getattr(old_value, "APNLineItemModelService_APNLineItem_020", None)
                if opp_val == self:
                    setattr(old_value, "APNLineItemModelService_APNLineItem_020", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "APNLineItemModelService_APNLineItem_020"):
                opp_val = getattr(value, "APNLineItemModelService_APNLineItem_020", None)
                setattr(value, "APNLineItemModelService_APNLineItem_020", self)

    @property
    def APNLineItem_APNModel_018(self):
        return self.__APNLineItem_APNModel_018
    @APNLineItem_APNModel_018.setter
    def APNLineItem_APNModel_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_APNLineItem__APNLineItem_APNModel_018", None)
        self.__APNLineItem_APNModel_018 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "APNLineItem_APNModel_119"):
                    opp_val = getattr(item, "APNLineItem_APNModel_119", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "APNLineItem_APNModel_119"):
                    opp_val = getattr(item, "APNLineItem_APNModel_119", None)
                    
                    if opp_val is None:
                        setattr(item, "APNLineItem_APNModel_119", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def APNModel_APNLineItem_15(self):
        return self.__APNModel_APNLineItem_15
    @APNModel_APNLineItem_15.setter
    def APNModel_APNLineItem_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_APNLineItem__APNModel_APNLineItem_15", None)
        self.__APNModel_APNLineItem_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "APNModel_APNLineItem_04"):
                    opp_val = getattr(item, "APNModel_APNLineItem_04", None)
                    
                    if opp_val == self:
                        setattr(item, "APNModel_APNLineItem_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "APNModel_APNLineItem_04"):
                    opp_val = getattr(item, "APNModel_APNLineItem_04", None)
                    
                    setattr(item, "APNModel_APNLineItem_04", self)
                    



class APNAdvertiser:

    pass


class BidAdjuster:

    pass


class IOManager:

    pass


class autopacing_inputs:

    def __init__(self, on_off: str, adjust_bids: str, sfdc_opportunity_id: str, dbm_io_id: str, sfdc_product_id: str, product_start_date: str, start_date: str, product_end_date: str, end_date: str, product_type: str, goal_type: str, kpi_goal: str, billing_currency: str, exchange_rate: str, avg_price_usd: str, cvr: str, cpm: str, impressions: str, region: str, region1: str, percentage_impression_credit: str, percentage_conversion_credit: str, hours_early_to_complete: str, minimum_partner_data_delivery_percent: str, sojern_goal_rae: str, pacing: str, days_early_to_complete: str, min_daily_volume_percent: str, min_daily_volume: str, minimum_margin: str, estimated_booking_value: str, account_manager: str, expected_click_credit: str, cpx: str, effective_impressions: str, conversions: str):
        self.on_off = on_off
        self.adjust_bids = adjust_bids
        self.sfdc_opportunity_id = sfdc_opportunity_id
        self.dbm_io_id = dbm_io_id
        self.sfdc_product_id = sfdc_product_id
        self.product_start_date = product_start_date
        self.start_date = start_date
        self.product_end_date = product_end_date
        self.end_date = end_date
        self.product_type = product_type
        self.goal_type = goal_type
        self.kpi_goal = kpi_goal
        self.billing_currency = billing_currency
        self.exchange_rate = exchange_rate
        self.avg_price_usd = avg_price_usd
        self.cvr = cvr
        self.cpm = cpm
        self.impressions = impressions
        self.region = region
        self.region1 = region1
        self.percentage_impression_credit = percentage_impression_credit
        self.percentage_conversion_credit = percentage_conversion_credit
        self.hours_early_to_complete = hours_early_to_complete
        self.minimum_partner_data_delivery_percent = minimum_partner_data_delivery_percent
        self.sojern_goal_rae = sojern_goal_rae
        self.pacing = pacing
        self.days_early_to_complete = days_early_to_complete
        self.min_daily_volume_percent = min_daily_volume_percent
        self.min_daily_volume = min_daily_volume
        self.minimum_margin = minimum_margin
        self.estimated_booking_value = estimated_booking_value
        self.account_manager = account_manager
        self.expected_click_credit = expected_click_credit
        self.cpx = cpx
        self.effective_impressions = effective_impressions
        self.conversions = conversions
        
        pass
    @property
    def avg_price_usd(self):
        return self.__avg_price_usd
    @avg_price_usd.setter
    def avg_price_usd(self, avg_price_usd: str):
        self.__avg_price_usd = avg_price_usd

    @property
    def kpi_goal(self):
        return self.__kpi_goal
    @kpi_goal.setter
    def kpi_goal(self, kpi_goal: str):
        self.__kpi_goal = kpi_goal

    @property
    def region(self):
        return self.__region
    @region.setter
    def region(self, region: str):
        self.__region = region

    @property
    def sfdc_opportunity_id(self):
        return self.__sfdc_opportunity_id
    @sfdc_opportunity_id.setter
    def sfdc_opportunity_id(self, sfdc_opportunity_id: str):
        self.__sfdc_opportunity_id = sfdc_opportunity_id

    @property
    def percentage_conversion_credit(self):
        return self.__percentage_conversion_credit
    @percentage_conversion_credit.setter
    def percentage_conversion_credit(self, percentage_conversion_credit: str):
        self.__percentage_conversion_credit = percentage_conversion_credit

    @property
    def adjust_bids(self):
        return self.__adjust_bids
    @adjust_bids.setter
    def adjust_bids(self, adjust_bids: str):
        self.__adjust_bids = adjust_bids

    @property
    def min_daily_volume(self):
        return self.__min_daily_volume
    @min_daily_volume.setter
    def min_daily_volume(self, min_daily_volume: str):
        self.__min_daily_volume = min_daily_volume

    @property
    def account_manager(self):
        return self.__account_manager
    @account_manager.setter
    def account_manager(self, account_manager: str):
        self.__account_manager = account_manager

    @property
    def days_early_to_complete(self):
        return self.__days_early_to_complete
    @days_early_to_complete.setter
    def days_early_to_complete(self, days_early_to_complete: str):
        self.__days_early_to_complete = days_early_to_complete

    @property
    def cpx(self):
        return self.__cpx
    @cpx.setter
    def cpx(self, cpx: str):
        self.__cpx = cpx

    @property
    def product_end_date(self):
        return self.__product_end_date
    @product_end_date.setter
    def product_end_date(self, product_end_date: str):
        self.__product_end_date = product_end_date

    @property
    def effective_impressions(self):
        return self.__effective_impressions
    @effective_impressions.setter
    def effective_impressions(self, effective_impressions: str):
        self.__effective_impressions = effective_impressions

    @property
    def minimum_partner_data_delivery_percent(self):
        return self.__minimum_partner_data_delivery_percent
    @minimum_partner_data_delivery_percent.setter
    def minimum_partner_data_delivery_percent(self, minimum_partner_data_delivery_percent: str):
        self.__minimum_partner_data_delivery_percent = minimum_partner_data_delivery_percent

    @property
    def sojern_goal_rae(self):
        return self.__sojern_goal_rae
    @sojern_goal_rae.setter
    def sojern_goal_rae(self, sojern_goal_rae: str):
        self.__sojern_goal_rae = sojern_goal_rae

    @property
    def impressions(self):
        return self.__impressions
    @impressions.setter
    def impressions(self, impressions: str):
        self.__impressions = impressions

    @property
    def exchange_rate(self):
        return self.__exchange_rate
    @exchange_rate.setter
    def exchange_rate(self, exchange_rate: str):
        self.__exchange_rate = exchange_rate

    @property
    def sfdc_product_id(self):
        return self.__sfdc_product_id
    @sfdc_product_id.setter
    def sfdc_product_id(self, sfdc_product_id: str):
        self.__sfdc_product_id = sfdc_product_id

    @property
    def conversions(self):
        return self.__conversions
    @conversions.setter
    def conversions(self, conversions: str):
        self.__conversions = conversions

    @property
    def region1(self):
        return self.__region1
    @region1.setter
    def region1(self, region1: str):
        self.__region1 = region1

    @property
    def end_date(self):
        return self.__end_date
    @end_date.setter
    def end_date(self, end_date: str):
        self.__end_date = end_date

    @property
    def min_daily_volume_percent(self):
        return self.__min_daily_volume_percent
    @min_daily_volume_percent.setter
    def min_daily_volume_percent(self, min_daily_volume_percent: str):
        self.__min_daily_volume_percent = min_daily_volume_percent

    @property
    def cvr(self):
        return self.__cvr
    @cvr.setter
    def cvr(self, cvr: str):
        self.__cvr = cvr

    @property
    def pacing(self):
        return self.__pacing
    @pacing.setter
    def pacing(self, pacing: str):
        self.__pacing = pacing

    @property
    def product_start_date(self):
        return self.__product_start_date
    @product_start_date.setter
    def product_start_date(self, product_start_date: str):
        self.__product_start_date = product_start_date

    @property
    def percentage_impression_credit(self):
        return self.__percentage_impression_credit
    @percentage_impression_credit.setter
    def percentage_impression_credit(self, percentage_impression_credit: str):
        self.__percentage_impression_credit = percentage_impression_credit

    @property
    def billing_currency(self):
        return self.__billing_currency
    @billing_currency.setter
    def billing_currency(self, billing_currency: str):
        self.__billing_currency = billing_currency

    @property
    def hours_early_to_complete(self):
        return self.__hours_early_to_complete
    @hours_early_to_complete.setter
    def hours_early_to_complete(self, hours_early_to_complete: str):
        self.__hours_early_to_complete = hours_early_to_complete

    @property
    def on_off(self):
        return self.__on_off
    @on_off.setter
    def on_off(self, on_off: str):
        self.__on_off = on_off

    @property
    def start_date(self):
        return self.__start_date
    @start_date.setter
    def start_date(self, start_date: str):
        self.__start_date = start_date

    @property
    def minimum_margin(self):
        return self.__minimum_margin
    @minimum_margin.setter
    def minimum_margin(self, minimum_margin: str):
        self.__minimum_margin = minimum_margin

    @property
    def expected_click_credit(self):
        return self.__expected_click_credit
    @expected_click_credit.setter
    def expected_click_credit(self, expected_click_credit: str):
        self.__expected_click_credit = expected_click_credit

    @property
    def cpm(self):
        return self.__cpm
    @cpm.setter
    def cpm(self, cpm: str):
        self.__cpm = cpm

    @property
    def goal_type(self):
        return self.__goal_type
    @goal_type.setter
    def goal_type(self, goal_type: str):
        self.__goal_type = goal_type

    @property
    def product_type(self):
        return self.__product_type
    @product_type.setter
    def product_type(self, product_type: str):
        self.__product_type = product_type

    @property
    def estimated_booking_value(self):
        return self.__estimated_booking_value
    @estimated_booking_value.setter
    def estimated_booking_value(self, estimated_booking_value: str):
        self.__estimated_booking_value = estimated_booking_value

    @property
    def dbm_io_id(self):
        return self.__dbm_io_id
    @dbm_io_id.setter
    def dbm_io_id(self, dbm_io_id: str):
        self.__dbm_io_id = dbm_io_id



class dbm_li_sfdc_product_li_mapping:

    def __init__(self, dbm_line_item_id: str, dbm_io_id: str, dbm_creative_ids: str, sfdc_product_id: str, dub_allocation_label: str):
        self.dbm_line_item_id = dbm_line_item_id
        self.dbm_io_id = dbm_io_id
        self.dbm_creative_ids = dbm_creative_ids
        self.sfdc_product_id = sfdc_product_id
        self.dub_allocation_label = dub_allocation_label
        
        pass
    @property
    def dbm_creative_ids(self):
        return self.__dbm_creative_ids
    @dbm_creative_ids.setter
    def dbm_creative_ids(self, dbm_creative_ids: str):
        self.__dbm_creative_ids = dbm_creative_ids

    @property
    def sfdc_product_id(self):
        return self.__sfdc_product_id
    @sfdc_product_id.setter
    def sfdc_product_id(self, sfdc_product_id: str):
        self.__sfdc_product_id = sfdc_product_id

    @property
    def dub_allocation_label(self):
        return self.__dub_allocation_label
    @dub_allocation_label.setter
    def dub_allocation_label(self, dub_allocation_label: str):
        self.__dub_allocation_label = dub_allocation_label

    @property
    def dbm_line_item_id(self):
        return self.__dbm_line_item_id
    @dbm_line_item_id.setter
    def dbm_line_item_id(self, dbm_line_item_id: str):
        self.__dbm_line_item_id = dbm_line_item_id

    @property
    def dbm_io_id(self):
        return self.__dbm_io_id
    @dbm_io_id.setter
    def dbm_io_id(self, dbm_io_id: str):
        self.__dbm_io_id = dbm_io_id



class CreativeApproval:

    pass


class SystemLineItemConversionPixel:

    pass


class SystemCreative:

    pass


class SystemLineItem:

    pass


class Tactic:

    pass


class CreativeAssetTactic:

    pass


class CreativeAsset:

    pass


class ProductLineItem:

    pass


class CampaignTravelEventType:

    pass


class CampaignBlocklistWhitelist:

    pass


class SpendAccountBlocklistWhitelist:

    pass


class Campaign:

    pass


class SpendAccount:

    pass


class AgencyExcludedVertical:

    pass


class AgencyBlocklistWhitelist:

    pass


class AdvertiserExcludedVertical:

    pass


class AdvertiserBlocklistWhitelist:

    pass


class SystemInsertionOrder:

    pass


class PartnerExcludedVertical:

    pass


class BrandSafetyBrandSafetyLabel:

    pass


class BrandSafetyBrandSafetyCustomSetting:

    pass


class Agency:

    def __init__(self, crm_id: str):
        self.crm_id = crm_id
        
        pass
    @property
    def crm_id(self):
        return self.__crm_id
    @crm_id.setter
    def crm_id(self, crm_id: str):
        self.__crm_id = crm_id



class Advertiser:

    def __init__(self, crm_id: str):
        self.crm_id = crm_id
        
        pass
    @property
    def crm_id(self):
        return self.__crm_id
    @crm_id.setter
    def crm_id(self, crm_id: str):
        self.__crm_id = crm_id



class Pixel:

    pass


class Partner:

    pass


class Goal:

    pass


class BrandSaftey:

    pass


class User:

    pass


class Targeting:

    pass


class SojernBusiness:

    pass


class RecordType:

    def __init__(self, id: str, name: str, description: str, crm_id: str, updated_by: str, deleted: str):
        self.id = id
        self.name = name
        self.description = description
        self.crm_id = crm_id
        self.updated_by = updated_by
        self.deleted = deleted
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def crm_id(self):
        return self.__crm_id
    @crm_id.setter
    def crm_id(self, crm_id: str):
        self.__crm_id = crm_id

    @property
    def updated_by(self):
        return self.__updated_by
    @updated_by.setter
    def updated_by(self, updated_by: str):
        self.__updated_by = updated_by

    @property
    def deleted(self):
        return self.__deleted
    @deleted.setter
    def deleted(self, deleted: str):
        self.__deleted = deleted

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id



class AppNexusClient:

    pass


class APNManager:

    pass


class updater_events_dataset_updater_events_daily:

    def __init__(self, sojernId: str, advertisername: str, segments_id: str):
        self.sojernId = sojernId
        self.advertisername = advertisername
        self.segments_id = segments_id
        
        pass
    @property
    def sojernId(self):
        return self.__sojernId
    @sojernId.setter
    def sojernId(self, sojernId: str):
        self.__sojernId = sojernId

    @property
    def segments_id(self):
        return self.__segments_id
    @segments_id.setter
    def segments_id(self, segments_id: str):
        self.__segments_id = segments_id

    @property
    def advertisername(self):
        return self.__advertisername
    @advertisername.setter
    def advertisername(self, advertisername: str):
        self.__advertisername = advertisername



class smp_events_dataset_smp_events_daily:

    def __init__(self, externalIds_id__used_as_apnid_: str, eventsourcename: str, profileid: str, ExternalIds_Type: str):
        self.externalIds_id__used_as_apnid_ = externalIds_id__used_as_apnid_
        self.eventsourcename = eventsourcename
        self.profileid = profileid
        self.ExternalIds_Type = ExternalIds_Type
        
        pass
    @property
    def ExternalIds_Type(self):
        return self.__ExternalIds_Type
    @ExternalIds_Type.setter
    def ExternalIds_Type(self, ExternalIds_Type: str):
        self.__ExternalIds_Type = ExternalIds_Type

    @property
    def externalIds_id__used_as_apnid_(self):
        return self.__externalIds_id__used_as_apnid_
    @externalIds_id__used_as_apnid_.setter
    def externalIds_id__used_as_apnid_(self, externalIds_id__used_as_apnid_: str):
        self.__externalIds_id__used_as_apnid_ = externalIds_id__used_as_apnid_

    @property
    def profileid(self):
        return self.__profileid
    @profileid.setter
    def profileid(self, profileid: str):
        self.__profileid = profileid

    @property
    def eventsourcename(self):
        return self.__eventsourcename
    @eventsourcename.setter
    def eventsourcename(self, eventsourcename: str):
        self.__eventsourcename = eventsourcename



class GCSManager:

    pass


class GCEManager:

    pass


class FBManager:

    pass


class DSManager:

    pass


class CloudSQLManager:

    pass


class DCMManager:

    pass


class DCSManager:

    pass


class DBMManager:

    pass


class SalesforceBulkManager:

    pass


class Salesforcemanager:

    pass


class WHUtils:

    pass


class BQTable:

    pass


class BQJobError:

    pass


class Oauth2client_client_GoogleCredentials:

    pass


class GCPManager:

    pass


class googleapiclient_discovery:

    pass


class BQManager:

    pass
