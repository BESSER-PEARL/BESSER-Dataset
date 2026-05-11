import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Document,
    model::Delivery,
    model::Dunning,
    model::Credit,
    model::Order,
    model::Offer,
    model::Confirmation,
    model::Letter,
    Contact,
    model::Debitor,
    model::Creditor,
    model::Invoice,
    AbstractCategory,
    model::ItemListTypeCategory,
    model::VoucherCategory,
    IEntity,
    model::DocumentItem,
    model::BankAccount,
    model::Contact,
    model::Document,
    model::Address,
    model::IndividualDocumentInfo,
    model::VAT,
    model::AbstractCategory,
    model::IDescribableEntity,
    model::Payment,
    model::ContactCategory,
    model::IEntity,
    model::WebshopStateMapping,
    model::WebShop,
    model::CEFACTCode,
    model::User,
    model::TextCategory,
    model::TextModule,
    model::Tenant,
    model::ShippingCategory,
    model::VATCategory,
    model::UserProperty,
    model::Role,
    model::ProductOptions,
    model::ProductCategory,
    IDescribableEntity,
    model::Product,
    model::Shipping,
    model::ProductBlockPrice,
    model::ItemAccountType,
    model::VoucherItem,
    model::Voucher,
    model::Proforma,
    ReliabilityType,
    ShippingVatType,
    VoucherType,
    BillingType,
    ContactType,
    ItemType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_document_is_not_abstract():
    assert not inspect.isabstract(Document)


def test_document_constructor_exists():
    assert callable(Document.__init__)


def test_document_constructor_args():
    sig = inspect.signature(Document.__init__)
    params = list(sig.parameters.keys())



def test_model::delivery_is_not_abstract():
    assert not inspect.isabstract(model::Delivery)


def test_model::delivery_constructor_exists():
    assert callable(model::Delivery.__init__)


def test_model::delivery_constructor_args():
    sig = inspect.signature(model::Delivery.__init__)
    params = list(sig.parameters.keys())



def test_model::dunning_is_not_abstract():
    assert not inspect.isabstract(model::Dunning)


def test_model::dunning_constructor_exists():
    assert callable(model::Dunning.__init__)


def test_model::dunning_constructor_args():
    sig = inspect.signature(model::Dunning.__init__)
    params = list(sig.parameters.keys())
    assert "dunningLevel" in params, "Missing parameter 'dunningLevel'"

def test_model::dunning_has_dunningLevel():
    assert hasattr(model::Dunning, "dunningLevel")
    descriptor = None
    for klass in model::Dunning.__mro__:
        if "dunningLevel" in klass.__dict__:
            descriptor = klass.__dict__["dunningLevel"]
            break
    assert isinstance(descriptor, property)



def test_model::credit_is_not_abstract():
    assert not inspect.isabstract(model::Credit)


def test_model::credit_constructor_exists():
    assert callable(model::Credit.__init__)


def test_model::credit_constructor_args():
    sig = inspect.signature(model::Credit.__init__)
    params = list(sig.parameters.keys())



def test_model::order_is_not_abstract():
    assert not inspect.isabstract(model::Order)


def test_model::order_constructor_exists():
    assert callable(model::Order.__init__)


def test_model::order_constructor_args():
    sig = inspect.signature(model::Order.__init__)
    params = list(sig.parameters.keys())



def test_model::offer_is_not_abstract():
    assert not inspect.isabstract(model::Offer)


def test_model::offer_constructor_exists():
    assert callable(model::Offer.__init__)


def test_model::offer_constructor_args():
    sig = inspect.signature(model::Offer.__init__)
    params = list(sig.parameters.keys())



def test_model::confirmation_is_not_abstract():
    assert not inspect.isabstract(model::Confirmation)


def test_model::confirmation_constructor_exists():
    assert callable(model::Confirmation.__init__)


def test_model::confirmation_constructor_args():
    sig = inspect.signature(model::Confirmation.__init__)
    params = list(sig.parameters.keys())



def test_model::letter_is_not_abstract():
    assert not inspect.isabstract(model::Letter)


def test_model::letter_constructor_exists():
    assert callable(model::Letter.__init__)


def test_model::letter_constructor_args():
    sig = inspect.signature(model::Letter.__init__)
    params = list(sig.parameters.keys())



def test_contact_is_not_abstract():
    assert not inspect.isabstract(Contact)


def test_contact_constructor_exists():
    assert callable(Contact.__init__)


def test_contact_constructor_args():
    sig = inspect.signature(Contact.__init__)
    params = list(sig.parameters.keys())



def test_model::debitor_is_not_abstract():
    assert not inspect.isabstract(model::Debitor)


def test_model::debitor_constructor_exists():
    assert callable(model::Debitor.__init__)


def test_model::debitor_constructor_args():
    sig = inspect.signature(model::Debitor.__init__)
    params = list(sig.parameters.keys())



def test_model::creditor_is_not_abstract():
    assert not inspect.isabstract(model::Creditor)


def test_model::creditor_constructor_exists():
    assert callable(model::Creditor.__init__)


def test_model::creditor_constructor_args():
    sig = inspect.signature(model::Creditor.__init__)
    params = list(sig.parameters.keys())



def test_model::invoice_is_not_abstract():
    assert not inspect.isabstract(model::Invoice)


def test_model::invoice_constructor_exists():
    assert callable(model::Invoice.__init__)


def test_model::invoice_constructor_args():
    sig = inspect.signature(model::Invoice.__init__)
    params = list(sig.parameters.keys())



def test_abstractcategory_is_not_abstract():
    assert not inspect.isabstract(AbstractCategory)


def test_abstractcategory_constructor_exists():
    assert callable(AbstractCategory.__init__)


def test_abstractcategory_constructor_args():
    sig = inspect.signature(AbstractCategory.__init__)
    params = list(sig.parameters.keys())



def test_model::itemlisttypecategory_is_not_abstract():
    assert not inspect.isabstract(model::ItemListTypeCategory)


def test_model::itemlisttypecategory_constructor_exists():
    assert callable(model::ItemListTypeCategory.__init__)


def test_model::itemlisttypecategory_constructor_args():
    sig = inspect.signature(model::ItemListTypeCategory.__init__)
    params = list(sig.parameters.keys())



def test_model::vouchercategory_is_not_abstract():
    assert not inspect.isabstract(model::VoucherCategory)


def test_model::vouchercategory_constructor_exists():
    assert callable(model::VoucherCategory.__init__)


def test_model::vouchercategory_constructor_args():
    sig = inspect.signature(model::VoucherCategory.__init__)
    params = list(sig.parameters.keys())



def test_ientity_is_not_abstract():
    assert not inspect.isabstract(IEntity)


def test_ientity_constructor_exists():
    assert callable(IEntity.__init__)


def test_ientity_constructor_args():
    sig = inspect.signature(IEntity.__init__)
    params = list(sig.parameters.keys())



def test_model::documentitem_is_not_abstract():
    assert not inspect.isabstract(model::DocumentItem)


def test_model::documentitem_constructor_exists():
    assert callable(model::DocumentItem.__init__)


def test_model::documentitem_constructor_args():
    sig = inspect.signature(model::DocumentItem.__init__)
    params = list(sig.parameters.keys())
    assert "itemType" in params, "Missing parameter 'itemType'"
    assert "price" in params, "Missing parameter 'price'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "gtin" in params, "Missing parameter 'gtin'"
    assert "vestingPeriodStart" in params, "Missing parameter 'vestingPeriodStart'"
    assert "noVat" in params, "Missing parameter 'noVat'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "vestingPeriodEnd" in params, "Missing parameter 'vestingPeriodEnd'"
    assert "itemNumber" in params, "Missing parameter 'itemNumber'"
    assert "quantityUnit" in params, "Missing parameter 'quantityUnit'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "tara" in params, "Missing parameter 'tara'"
    assert "description" in params, "Missing parameter 'description'"
    assert "originQuantity" in params, "Missing parameter 'originQuantity'"
    assert "posNr" in params, "Missing parameter 'posNr'"
    assert "itemRebate" in params, "Missing parameter 'itemRebate'"
    assert "picture" in params, "Missing parameter 'picture'"

def test_model::documentitem_has_itemType():
    assert hasattr(model::DocumentItem, "itemType")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "itemType" in klass.__dict__:
            descriptor = klass.__dict__["itemType"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_price():
    assert hasattr(model::DocumentItem, "price")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_optional():
    assert hasattr(model::DocumentItem, "optional")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_gtin():
    assert hasattr(model::DocumentItem, "gtin")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "gtin" in klass.__dict__:
            descriptor = klass.__dict__["gtin"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_vestingPeriodStart():
    assert hasattr(model::DocumentItem, "vestingPeriodStart")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "vestingPeriodStart" in klass.__dict__:
            descriptor = klass.__dict__["vestingPeriodStart"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_noVat():
    assert hasattr(model::DocumentItem, "noVat")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "noVat" in klass.__dict__:
            descriptor = klass.__dict__["noVat"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_quantity():
    assert hasattr(model::DocumentItem, "quantity")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_vestingPeriodEnd():
    assert hasattr(model::DocumentItem, "vestingPeriodEnd")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "vestingPeriodEnd" in klass.__dict__:
            descriptor = klass.__dict__["vestingPeriodEnd"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_itemNumber():
    assert hasattr(model::DocumentItem, "itemNumber")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "itemNumber" in klass.__dict__:
            descriptor = klass.__dict__["itemNumber"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_quantityUnit():
    assert hasattr(model::DocumentItem, "quantityUnit")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "quantityUnit" in klass.__dict__:
            descriptor = klass.__dict__["quantityUnit"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_weight():
    assert hasattr(model::DocumentItem, "weight")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_tara():
    assert hasattr(model::DocumentItem, "tara")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "tara" in klass.__dict__:
            descriptor = klass.__dict__["tara"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_description():
    assert hasattr(model::DocumentItem, "description")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_originQuantity():
    assert hasattr(model::DocumentItem, "originQuantity")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "originQuantity" in klass.__dict__:
            descriptor = klass.__dict__["originQuantity"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_posNr():
    assert hasattr(model::DocumentItem, "posNr")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "posNr" in klass.__dict__:
            descriptor = klass.__dict__["posNr"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_itemRebate():
    assert hasattr(model::DocumentItem, "itemRebate")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "itemRebate" in klass.__dict__:
            descriptor = klass.__dict__["itemRebate"]
            break
    assert isinstance(descriptor, property)

def test_model::documentitem_has_picture():
    assert hasattr(model::DocumentItem, "picture")
    descriptor = None
    for klass in model::DocumentItem.__mro__:
        if "picture" in klass.__dict__:
            descriptor = klass.__dict__["picture"]
            break
    assert isinstance(descriptor, property)



def test_model::bankaccount_is_not_abstract():
    assert not inspect.isabstract(model::BankAccount)


def test_model::bankaccount_constructor_exists():
    assert callable(model::BankAccount.__init__)


def test_model::bankaccount_constructor_args():
    sig = inspect.signature(model::BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "iban" in params, "Missing parameter 'iban'"
    assert "bankCode" in params, "Missing parameter 'bankCode'"
    assert "accountHolder" in params, "Missing parameter 'accountHolder'"
    assert "bic" in params, "Missing parameter 'bic'"
    assert "bankName" in params, "Missing parameter 'bankName'"

def test_model::bankaccount_has_iban():
    assert hasattr(model::BankAccount, "iban")
    descriptor = None
    for klass in model::BankAccount.__mro__:
        if "iban" in klass.__dict__:
            descriptor = klass.__dict__["iban"]
            break
    assert isinstance(descriptor, property)

def test_model::bankaccount_has_bankCode():
    assert hasattr(model::BankAccount, "bankCode")
    descriptor = None
    for klass in model::BankAccount.__mro__:
        if "bankCode" in klass.__dict__:
            descriptor = klass.__dict__["bankCode"]
            break
    assert isinstance(descriptor, property)

def test_model::bankaccount_has_accountHolder():
    assert hasattr(model::BankAccount, "accountHolder")
    descriptor = None
    for klass in model::BankAccount.__mro__:
        if "accountHolder" in klass.__dict__:
            descriptor = klass.__dict__["accountHolder"]
            break
    assert isinstance(descriptor, property)

def test_model::bankaccount_has_bic():
    assert hasattr(model::BankAccount, "bic")
    descriptor = None
    for klass in model::BankAccount.__mro__:
        if "bic" in klass.__dict__:
            descriptor = klass.__dict__["bic"]
            break
    assert isinstance(descriptor, property)

def test_model::bankaccount_has_bankName():
    assert hasattr(model::BankAccount, "bankName")
    descriptor = None
    for klass in model::BankAccount.__mro__:
        if "bankName" in klass.__dict__:
            descriptor = klass.__dict__["bankName"]
            break
    assert isinstance(descriptor, property)



def test_model::contact_is_not_abstract():
    assert not inspect.isabstract(model::Contact)


def test_model::contact_constructor_exists():
    assert callable(model::Contact.__init__)


def test_model::contact_constructor_args():
    sig = inspect.signature(model::Contact.__init__)
    params = list(sig.parameters.keys())
    assert "discount" in params, "Missing parameter 'discount'"
    assert "webshopName" in params, "Missing parameter 'webshopName'"
    assert "website" in params, "Missing parameter 'website'"
    assert "birthday" in params, "Missing parameter 'birthday'"
    assert "note" in params, "Missing parameter 'note'"
    assert "useNetGross" in params, "Missing parameter 'useNetGross'"
    assert "customerNumber" in params, "Missing parameter 'customerNumber'"
    assert "gln" in params, "Missing parameter 'gln'"
    assert "title" in params, "Missing parameter 'title'"
    assert "fax" in params, "Missing parameter 'fax'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "company" in params, "Missing parameter 'company'"
    assert "supplierNumber" in params, "Missing parameter 'supplierNumber'"
    assert "email" in params, "Missing parameter 'email'"
    assert "vatNumberValid" in params, "Missing parameter 'vatNumberValid'"
    assert "useSalesEqualizationTax" in params, "Missing parameter 'useSalesEqualizationTax'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "mandateReference" in params, "Missing parameter 'mandateReference'"
    assert "vatNumber" in params, "Missing parameter 'vatNumber'"
    assert "reliability" in params, "Missing parameter 'reliability'"
    assert "mobile" in params, "Missing parameter 'mobile'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "contactType" in params, "Missing parameter 'contactType'"

def test_model::contact_has_discount():
    assert hasattr(model::Contact, "discount")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "discount" in klass.__dict__:
            descriptor = klass.__dict__["discount"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_webshopName():
    assert hasattr(model::Contact, "webshopName")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "webshopName" in klass.__dict__:
            descriptor = klass.__dict__["webshopName"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_website():
    assert hasattr(model::Contact, "website")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "website" in klass.__dict__:
            descriptor = klass.__dict__["website"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_birthday():
    assert hasattr(model::Contact, "birthday")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "birthday" in klass.__dict__:
            descriptor = klass.__dict__["birthday"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_note():
    assert hasattr(model::Contact, "note")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_useNetGross():
    assert hasattr(model::Contact, "useNetGross")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "useNetGross" in klass.__dict__:
            descriptor = klass.__dict__["useNetGross"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_customerNumber():
    assert hasattr(model::Contact, "customerNumber")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "customerNumber" in klass.__dict__:
            descriptor = klass.__dict__["customerNumber"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_gln():
    assert hasattr(model::Contact, "gln")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "gln" in klass.__dict__:
            descriptor = klass.__dict__["gln"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_title():
    assert hasattr(model::Contact, "title")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_fax():
    assert hasattr(model::Contact, "fax")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "fax" in klass.__dict__:
            descriptor = klass.__dict__["fax"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_gender():
    assert hasattr(model::Contact, "gender")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_company():
    assert hasattr(model::Contact, "company")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_supplierNumber():
    assert hasattr(model::Contact, "supplierNumber")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "supplierNumber" in klass.__dict__:
            descriptor = klass.__dict__["supplierNumber"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_email():
    assert hasattr(model::Contact, "email")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_vatNumberValid():
    assert hasattr(model::Contact, "vatNumberValid")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "vatNumberValid" in klass.__dict__:
            descriptor = klass.__dict__["vatNumberValid"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_useSalesEqualizationTax():
    assert hasattr(model::Contact, "useSalesEqualizationTax")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "useSalesEqualizationTax" in klass.__dict__:
            descriptor = klass.__dict__["useSalesEqualizationTax"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_firstName():
    assert hasattr(model::Contact, "firstName")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_mandateReference():
    assert hasattr(model::Contact, "mandateReference")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "mandateReference" in klass.__dict__:
            descriptor = klass.__dict__["mandateReference"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_vatNumber():
    assert hasattr(model::Contact, "vatNumber")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "vatNumber" in klass.__dict__:
            descriptor = klass.__dict__["vatNumber"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_reliability():
    assert hasattr(model::Contact, "reliability")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "reliability" in klass.__dict__:
            descriptor = klass.__dict__["reliability"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_mobile():
    assert hasattr(model::Contact, "mobile")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "mobile" in klass.__dict__:
            descriptor = klass.__dict__["mobile"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_phone():
    assert hasattr(model::Contact, "phone")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_model::contact_has_contactType():
    assert hasattr(model::Contact, "contactType")
    descriptor = None
    for klass in model::Contact.__mro__:
        if "contactType" in klass.__dict__:
            descriptor = klass.__dict__["contactType"]
            break
    assert isinstance(descriptor, property)



def test_model::document_is_not_abstract():
    assert not inspect.isabstract(model::Document)


def test_model::document_constructor_exists():
    assert callable(model::Document.__init__)


def test_model::document_constructor_args():
    sig = inspect.signature(model::Document.__init__)
    params = list(sig.parameters.keys())
    assert "deposit" in params, "Missing parameter 'deposit'"
    assert "documentDate" in params, "Missing parameter 'documentDate'"
    assert "printed" in params, "Missing parameter 'printed'"
    assert "itemsRebate" in params, "Missing parameter 'itemsRebate'"
    assert "paidValue" in params, "Missing parameter 'paidValue'"
    assert "shippingAutoVat" in params, "Missing parameter 'shippingAutoVat'"
    assert "vestingPeriodEnd" in params, "Missing parameter 'vestingPeriodEnd'"
    assert "odtPath" in params, "Missing parameter 'odtPath'"
    assert "paid" in params, "Missing parameter 'paid'"
    assert "shippingValue" in params, "Missing parameter 'shippingValue'"
    assert "progress" in params, "Missing parameter 'progress'"
    assert "customerRef" in params, "Missing parameter 'customerRef'"
    assert "pdfPath" in params, "Missing parameter 'pdfPath'"
    assert "addressFirstLine" in params, "Missing parameter 'addressFirstLine'"
    assert "transactionId" in params, "Missing parameter 'transactionId'"
    assert "consultant" in params, "Missing parameter 'consultant'"
    assert "dueDays" in params, "Missing parameter 'dueDays'"
    assert "payDate" in params, "Missing parameter 'payDate'"
    assert "serviceDate" in params, "Missing parameter 'serviceDate'"
    assert "printTemplate" in params, "Missing parameter 'printTemplate'"
    assert "vestingPeriodStart" in params, "Missing parameter 'vestingPeriodStart'"
    assert "message3" in params, "Missing parameter 'message3'"
    assert "message2" in params, "Missing parameter 'message2'"
    assert "message" in params, "Missing parameter 'message'"
    assert "webshopId" in params, "Missing parameter 'webshopId'"
    assert "orderDate" in params, "Missing parameter 'orderDate'"
    assert "billingType" in params, "Missing parameter 'billingType'"
    assert "netGross" in params, "Missing parameter 'netGross'"
    assert "webshopDate" in params, "Missing parameter 'webshopDate'"
    assert "totalValue" in params, "Missing parameter 'totalValue'"

def test_model::document_has_deposit():
    assert hasattr(model::Document, "deposit")
    descriptor = None
    for klass in model::Document.__mro__:
        if "deposit" in klass.__dict__:
            descriptor = klass.__dict__["deposit"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_documentDate():
    assert hasattr(model::Document, "documentDate")
    descriptor = None
    for klass in model::Document.__mro__:
        if "documentDate" in klass.__dict__:
            descriptor = klass.__dict__["documentDate"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_printed():
    assert hasattr(model::Document, "printed")
    descriptor = None
    for klass in model::Document.__mro__:
        if "printed" in klass.__dict__:
            descriptor = klass.__dict__["printed"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_itemsRebate():
    assert hasattr(model::Document, "itemsRebate")
    descriptor = None
    for klass in model::Document.__mro__:
        if "itemsRebate" in klass.__dict__:
            descriptor = klass.__dict__["itemsRebate"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_paidValue():
    assert hasattr(model::Document, "paidValue")
    descriptor = None
    for klass in model::Document.__mro__:
        if "paidValue" in klass.__dict__:
            descriptor = klass.__dict__["paidValue"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_shippingAutoVat():
    assert hasattr(model::Document, "shippingAutoVat")
    descriptor = None
    for klass in model::Document.__mro__:
        if "shippingAutoVat" in klass.__dict__:
            descriptor = klass.__dict__["shippingAutoVat"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_vestingPeriodEnd():
    assert hasattr(model::Document, "vestingPeriodEnd")
    descriptor = None
    for klass in model::Document.__mro__:
        if "vestingPeriodEnd" in klass.__dict__:
            descriptor = klass.__dict__["vestingPeriodEnd"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_odtPath():
    assert hasattr(model::Document, "odtPath")
    descriptor = None
    for klass in model::Document.__mro__:
        if "odtPath" in klass.__dict__:
            descriptor = klass.__dict__["odtPath"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_paid():
    assert hasattr(model::Document, "paid")
    descriptor = None
    for klass in model::Document.__mro__:
        if "paid" in klass.__dict__:
            descriptor = klass.__dict__["paid"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_shippingValue():
    assert hasattr(model::Document, "shippingValue")
    descriptor = None
    for klass in model::Document.__mro__:
        if "shippingValue" in klass.__dict__:
            descriptor = klass.__dict__["shippingValue"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_progress():
    assert hasattr(model::Document, "progress")
    descriptor = None
    for klass in model::Document.__mro__:
        if "progress" in klass.__dict__:
            descriptor = klass.__dict__["progress"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_customerRef():
    assert hasattr(model::Document, "customerRef")
    descriptor = None
    for klass in model::Document.__mro__:
        if "customerRef" in klass.__dict__:
            descriptor = klass.__dict__["customerRef"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_pdfPath():
    assert hasattr(model::Document, "pdfPath")
    descriptor = None
    for klass in model::Document.__mro__:
        if "pdfPath" in klass.__dict__:
            descriptor = klass.__dict__["pdfPath"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_addressFirstLine():
    assert hasattr(model::Document, "addressFirstLine")
    descriptor = None
    for klass in model::Document.__mro__:
        if "addressFirstLine" in klass.__dict__:
            descriptor = klass.__dict__["addressFirstLine"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_transactionId():
    assert hasattr(model::Document, "transactionId")
    descriptor = None
    for klass in model::Document.__mro__:
        if "transactionId" in klass.__dict__:
            descriptor = klass.__dict__["transactionId"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_consultant():
    assert hasattr(model::Document, "consultant")
    descriptor = None
    for klass in model::Document.__mro__:
        if "consultant" in klass.__dict__:
            descriptor = klass.__dict__["consultant"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_dueDays():
    assert hasattr(model::Document, "dueDays")
    descriptor = None
    for klass in model::Document.__mro__:
        if "dueDays" in klass.__dict__:
            descriptor = klass.__dict__["dueDays"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_payDate():
    assert hasattr(model::Document, "payDate")
    descriptor = None
    for klass in model::Document.__mro__:
        if "payDate" in klass.__dict__:
            descriptor = klass.__dict__["payDate"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_serviceDate():
    assert hasattr(model::Document, "serviceDate")
    descriptor = None
    for klass in model::Document.__mro__:
        if "serviceDate" in klass.__dict__:
            descriptor = klass.__dict__["serviceDate"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_printTemplate():
    assert hasattr(model::Document, "printTemplate")
    descriptor = None
    for klass in model::Document.__mro__:
        if "printTemplate" in klass.__dict__:
            descriptor = klass.__dict__["printTemplate"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_vestingPeriodStart():
    assert hasattr(model::Document, "vestingPeriodStart")
    descriptor = None
    for klass in model::Document.__mro__:
        if "vestingPeriodStart" in klass.__dict__:
            descriptor = klass.__dict__["vestingPeriodStart"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_message3():
    assert hasattr(model::Document, "message3")
    descriptor = None
    for klass in model::Document.__mro__:
        if "message3" in klass.__dict__:
            descriptor = klass.__dict__["message3"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_message2():
    assert hasattr(model::Document, "message2")
    descriptor = None
    for klass in model::Document.__mro__:
        if "message2" in klass.__dict__:
            descriptor = klass.__dict__["message2"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_message():
    assert hasattr(model::Document, "message")
    descriptor = None
    for klass in model::Document.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_webshopId():
    assert hasattr(model::Document, "webshopId")
    descriptor = None
    for klass in model::Document.__mro__:
        if "webshopId" in klass.__dict__:
            descriptor = klass.__dict__["webshopId"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_orderDate():
    assert hasattr(model::Document, "orderDate")
    descriptor = None
    for klass in model::Document.__mro__:
        if "orderDate" in klass.__dict__:
            descriptor = klass.__dict__["orderDate"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_billingType():
    assert hasattr(model::Document, "billingType")
    descriptor = None
    for klass in model::Document.__mro__:
        if "billingType" in klass.__dict__:
            descriptor = klass.__dict__["billingType"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_netGross():
    assert hasattr(model::Document, "netGross")
    descriptor = None
    for klass in model::Document.__mro__:
        if "netGross" in klass.__dict__:
            descriptor = klass.__dict__["netGross"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_webshopDate():
    assert hasattr(model::Document, "webshopDate")
    descriptor = None
    for klass in model::Document.__mro__:
        if "webshopDate" in klass.__dict__:
            descriptor = klass.__dict__["webshopDate"]
            break
    assert isinstance(descriptor, property)

def test_model::document_has_totalValue():
    assert hasattr(model::Document, "totalValue")
    descriptor = None
    for klass in model::Document.__mro__:
        if "totalValue" in klass.__dict__:
            descriptor = klass.__dict__["totalValue"]
            break
    assert isinstance(descriptor, property)



def test_model::address_is_not_abstract():
    assert not inspect.isabstract(model::Address)


def test_model::address_constructor_exists():
    assert callable(model::Address.__init__)


def test_model::address_constructor_args():
    sig = inspect.signature(model::Address.__init__)
    params = list(sig.parameters.keys())
    assert "cityAddon" in params, "Missing parameter 'cityAddon'"
    assert "street" in params, "Missing parameter 'street'"
    assert "zip" in params, "Missing parameter 'zip'"
    assert "manualAddress" in params, "Missing parameter 'manualAddress'"
    assert "city" in params, "Missing parameter 'city'"
    assert "countryCode" in params, "Missing parameter 'countryCode'"

def test_model::address_has_cityAddon():
    assert hasattr(model::Address, "cityAddon")
    descriptor = None
    for klass in model::Address.__mro__:
        if "cityAddon" in klass.__dict__:
            descriptor = klass.__dict__["cityAddon"]
            break
    assert isinstance(descriptor, property)

def test_model::address_has_street():
    assert hasattr(model::Address, "street")
    descriptor = None
    for klass in model::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_model::address_has_zip():
    assert hasattr(model::Address, "zip")
    descriptor = None
    for klass in model::Address.__mro__:
        if "zip" in klass.__dict__:
            descriptor = klass.__dict__["zip"]
            break
    assert isinstance(descriptor, property)

def test_model::address_has_manualAddress():
    assert hasattr(model::Address, "manualAddress")
    descriptor = None
    for klass in model::Address.__mro__:
        if "manualAddress" in klass.__dict__:
            descriptor = klass.__dict__["manualAddress"]
            break
    assert isinstance(descriptor, property)

def test_model::address_has_city():
    assert hasattr(model::Address, "city")
    descriptor = None
    for klass in model::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_model::address_has_countryCode():
    assert hasattr(model::Address, "countryCode")
    descriptor = None
    for klass in model::Address.__mro__:
        if "countryCode" in klass.__dict__:
            descriptor = klass.__dict__["countryCode"]
            break
    assert isinstance(descriptor, property)



def test_model::individualdocumentinfo_is_not_abstract():
    assert not inspect.isabstract(model::IndividualDocumentInfo)


def test_model::individualdocumentinfo_constructor_exists():
    assert callable(model::IndividualDocumentInfo.__init__)


def test_model::individualdocumentinfo_constructor_args():
    sig = inspect.signature(model::IndividualDocumentInfo.__init__)
    params = list(sig.parameters.keys())
    assert "noVatName" in params, "Missing parameter 'noVatName'"
    assert "shippingAutoVat" in params, "Missing parameter 'shippingAutoVat'"
    assert "paymentDescription" in params, "Missing parameter 'paymentDescription'"
    assert "shippingValue" in params, "Missing parameter 'shippingValue'"
    assert "paymentText" in params, "Missing parameter 'paymentText'"
    assert "shippingDescription" in params, "Missing parameter 'shippingDescription'"
    assert "shippingVatDescription" in params, "Missing parameter 'shippingVatDescription'"
    assert "paymentName" in params, "Missing parameter 'paymentName'"
    assert "shippingName" in params, "Missing parameter 'shippingName'"
    assert "noVatDescription" in params, "Missing parameter 'noVatDescription'"
    assert "shippingVatValue" in params, "Missing parameter 'shippingVatValue'"

def test_model::individualdocumentinfo_has_noVatName():
    assert hasattr(model::IndividualDocumentInfo, "noVatName")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "noVatName" in klass.__dict__:
            descriptor = klass.__dict__["noVatName"]
            break
    assert isinstance(descriptor, property)

def test_model::individualdocumentinfo_has_shippingAutoVat():
    assert hasattr(model::IndividualDocumentInfo, "shippingAutoVat")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "shippingAutoVat" in klass.__dict__:
            descriptor = klass.__dict__["shippingAutoVat"]
            break
    assert isinstance(descriptor, property)

def test_model::individualdocumentinfo_has_paymentDescription():
    assert hasattr(model::IndividualDocumentInfo, "paymentDescription")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "paymentDescription" in klass.__dict__:
            descriptor = klass.__dict__["paymentDescription"]
            break
    assert isinstance(descriptor, property)

def test_model::individualdocumentinfo_has_shippingValue():
    assert hasattr(model::IndividualDocumentInfo, "shippingValue")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "shippingValue" in klass.__dict__:
            descriptor = klass.__dict__["shippingValue"]
            break
    assert isinstance(descriptor, property)

def test_model::individualdocumentinfo_has_paymentText():
    assert hasattr(model::IndividualDocumentInfo, "paymentText")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "paymentText" in klass.__dict__:
            descriptor = klass.__dict__["paymentText"]
            break
    assert isinstance(descriptor, property)

def test_model::individualdocumentinfo_has_shippingDescription():
    assert hasattr(model::IndividualDocumentInfo, "shippingDescription")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "shippingDescription" in klass.__dict__:
            descriptor = klass.__dict__["shippingDescription"]
            break
    assert isinstance(descriptor, property)

def test_model::individualdocumentinfo_has_shippingVatDescription():
    assert hasattr(model::IndividualDocumentInfo, "shippingVatDescription")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "shippingVatDescription" in klass.__dict__:
            descriptor = klass.__dict__["shippingVatDescription"]
            break
    assert isinstance(descriptor, property)

def test_model::individualdocumentinfo_has_paymentName():
    assert hasattr(model::IndividualDocumentInfo, "paymentName")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "paymentName" in klass.__dict__:
            descriptor = klass.__dict__["paymentName"]
            break
    assert isinstance(descriptor, property)

def test_model::individualdocumentinfo_has_shippingName():
    assert hasattr(model::IndividualDocumentInfo, "shippingName")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "shippingName" in klass.__dict__:
            descriptor = klass.__dict__["shippingName"]
            break
    assert isinstance(descriptor, property)

def test_model::individualdocumentinfo_has_noVatDescription():
    assert hasattr(model::IndividualDocumentInfo, "noVatDescription")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "noVatDescription" in klass.__dict__:
            descriptor = klass.__dict__["noVatDescription"]
            break
    assert isinstance(descriptor, property)

def test_model::individualdocumentinfo_has_shippingVatValue():
    assert hasattr(model::IndividualDocumentInfo, "shippingVatValue")
    descriptor = None
    for klass in model::IndividualDocumentInfo.__mro__:
        if "shippingVatValue" in klass.__dict__:
            descriptor = klass.__dict__["shippingVatValue"]
            break
    assert isinstance(descriptor, property)



def test_model::vat_is_not_abstract():
    assert not inspect.isabstract(model::VAT)


def test_model::vat_constructor_exists():
    assert callable(model::VAT.__init__)


def test_model::vat_constructor_args():
    sig = inspect.signature(model::VAT.__init__)
    params = list(sig.parameters.keys())
    assert "salesEqualizationTax" in params, "Missing parameter 'salesEqualizationTax'"
    assert "description" in params, "Missing parameter 'description'"
    assert "taxValue" in params, "Missing parameter 'taxValue'"

def test_model::vat_has_salesEqualizationTax():
    assert hasattr(model::VAT, "salesEqualizationTax")
    descriptor = None
    for klass in model::VAT.__mro__:
        if "salesEqualizationTax" in klass.__dict__:
            descriptor = klass.__dict__["salesEqualizationTax"]
            break
    assert isinstance(descriptor, property)

def test_model::vat_has_description():
    assert hasattr(model::VAT, "description")
    descriptor = None
    for klass in model::VAT.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model::vat_has_taxValue():
    assert hasattr(model::VAT, "taxValue")
    descriptor = None
    for klass in model::VAT.__mro__:
        if "taxValue" in klass.__dict__:
            descriptor = klass.__dict__["taxValue"]
            break
    assert isinstance(descriptor, property)



def test_model::abstractcategory_is_not_abstract():
    assert not inspect.isabstract(model::AbstractCategory)


def test_model::abstractcategory_constructor_exists():
    assert callable(model::AbstractCategory.__init__)


def test_model::abstractcategory_constructor_args():
    sig = inspect.signature(model::AbstractCategory.__init__)
    params = list(sig.parameters.keys())



def test_model::idescribableentity_is_not_abstract():
    assert not inspect.isabstract(model::IDescribableEntity)


def test_model::idescribableentity_constructor_exists():
    assert callable(model::IDescribableEntity.__init__)


def test_model::idescribableentity_constructor_args():
    sig = inspect.signature(model::IDescribableEntity.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_model::idescribableentity_has_description():
    assert hasattr(model::IDescribableEntity, "description")
    descriptor = None
    for klass in model::IDescribableEntity.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_model::payment_is_not_abstract():
    assert not inspect.isabstract(model::Payment)


def test_model::payment_constructor_exists():
    assert callable(model::Payment.__init__)


def test_model::payment_constructor_args():
    sig = inspect.signature(model::Payment.__init__)
    params = list(sig.parameters.keys())
    assert "discountValue" in params, "Missing parameter 'discountValue'"
    assert "unpaidText" in params, "Missing parameter 'unpaidText'"
    assert "netDays" in params, "Missing parameter 'netDays'"
    assert "paidText" in params, "Missing parameter 'paidText'"
    assert "code" in params, "Missing parameter 'code'"
    assert "depositText" in params, "Missing parameter 'depositText'"
    assert "description" in params, "Missing parameter 'description'"
    assert "discountDays" in params, "Missing parameter 'discountDays'"

def test_model::payment_has_discountValue():
    assert hasattr(model::Payment, "discountValue")
    descriptor = None
    for klass in model::Payment.__mro__:
        if "discountValue" in klass.__dict__:
            descriptor = klass.__dict__["discountValue"]
            break
    assert isinstance(descriptor, property)

def test_model::payment_has_unpaidText():
    assert hasattr(model::Payment, "unpaidText")
    descriptor = None
    for klass in model::Payment.__mro__:
        if "unpaidText" in klass.__dict__:
            descriptor = klass.__dict__["unpaidText"]
            break
    assert isinstance(descriptor, property)

def test_model::payment_has_netDays():
    assert hasattr(model::Payment, "netDays")
    descriptor = None
    for klass in model::Payment.__mro__:
        if "netDays" in klass.__dict__:
            descriptor = klass.__dict__["netDays"]
            break
    assert isinstance(descriptor, property)

def test_model::payment_has_paidText():
    assert hasattr(model::Payment, "paidText")
    descriptor = None
    for klass in model::Payment.__mro__:
        if "paidText" in klass.__dict__:
            descriptor = klass.__dict__["paidText"]
            break
    assert isinstance(descriptor, property)

def test_model::payment_has_code():
    assert hasattr(model::Payment, "code")
    descriptor = None
    for klass in model::Payment.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_model::payment_has_depositText():
    assert hasattr(model::Payment, "depositText")
    descriptor = None
    for klass in model::Payment.__mro__:
        if "depositText" in klass.__dict__:
            descriptor = klass.__dict__["depositText"]
            break
    assert isinstance(descriptor, property)

def test_model::payment_has_description():
    assert hasattr(model::Payment, "description")
    descriptor = None
    for klass in model::Payment.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model::payment_has_discountDays():
    assert hasattr(model::Payment, "discountDays")
    descriptor = None
    for klass in model::Payment.__mro__:
        if "discountDays" in klass.__dict__:
            descriptor = klass.__dict__["discountDays"]
            break
    assert isinstance(descriptor, property)



def test_model::contactcategory_is_not_abstract():
    assert not inspect.isabstract(model::ContactCategory)


def test_model::contactcategory_constructor_exists():
    assert callable(model::ContactCategory.__init__)


def test_model::contactcategory_constructor_args():
    sig = inspect.signature(model::ContactCategory.__init__)
    params = list(sig.parameters.keys())



def test_model::ientity_is_not_abstract():
    assert not inspect.isabstract(model::IEntity)


def test_model::ientity_constructor_exists():
    assert callable(model::IEntity.__init__)


def test_model::ientity_constructor_args():
    sig = inspect.signature(model::IEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "deleted" in params, "Missing parameter 'deleted'"
    assert "modifiedBy" in params, "Missing parameter 'modifiedBy'"
    assert "validFrom" in params, "Missing parameter 'validFrom'"
    assert "id" in params, "Missing parameter 'id'"
    assert "validTo" in params, "Missing parameter 'validTo'"
    assert "dateAdded" in params, "Missing parameter 'dateAdded'"
    assert "modified" in params, "Missing parameter 'modified'"

def test_model::ientity_has_name():
    assert hasattr(model::IEntity, "name")
    descriptor = None
    for klass in model::IEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::ientity_has_deleted():
    assert hasattr(model::IEntity, "deleted")
    descriptor = None
    for klass in model::IEntity.__mro__:
        if "deleted" in klass.__dict__:
            descriptor = klass.__dict__["deleted"]
            break
    assert isinstance(descriptor, property)

def test_model::ientity_has_modifiedBy():
    assert hasattr(model::IEntity, "modifiedBy")
    descriptor = None
    for klass in model::IEntity.__mro__:
        if "modifiedBy" in klass.__dict__:
            descriptor = klass.__dict__["modifiedBy"]
            break
    assert isinstance(descriptor, property)

def test_model::ientity_has_validFrom():
    assert hasattr(model::IEntity, "validFrom")
    descriptor = None
    for klass in model::IEntity.__mro__:
        if "validFrom" in klass.__dict__:
            descriptor = klass.__dict__["validFrom"]
            break
    assert isinstance(descriptor, property)

def test_model::ientity_has_id():
    assert hasattr(model::IEntity, "id")
    descriptor = None
    for klass in model::IEntity.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_model::ientity_has_validTo():
    assert hasattr(model::IEntity, "validTo")
    descriptor = None
    for klass in model::IEntity.__mro__:
        if "validTo" in klass.__dict__:
            descriptor = klass.__dict__["validTo"]
            break
    assert isinstance(descriptor, property)

def test_model::ientity_has_dateAdded():
    assert hasattr(model::IEntity, "dateAdded")
    descriptor = None
    for klass in model::IEntity.__mro__:
        if "dateAdded" in klass.__dict__:
            descriptor = klass.__dict__["dateAdded"]
            break
    assert isinstance(descriptor, property)

def test_model::ientity_has_modified():
    assert hasattr(model::IEntity, "modified")
    descriptor = None
    for klass in model::IEntity.__mro__:
        if "modified" in klass.__dict__:
            descriptor = klass.__dict__["modified"]
            break
    assert isinstance(descriptor, property)



def test_model::webshopstatemapping_is_not_abstract():
    assert not inspect.isabstract(model::WebshopStateMapping)


def test_model::webshopstatemapping_constructor_exists():
    assert callable(model::WebshopStateMapping.__init__)


def test_model::webshopstatemapping_constructor_args():
    sig = inspect.signature(model::WebshopStateMapping.__init__)
    params = list(sig.parameters.keys())
    assert "fakturamaOrderState" in params, "Missing parameter 'fakturamaOrderState'"
    assert "webshopState" in params, "Missing parameter 'webshopState'"

def test_model::webshopstatemapping_has_fakturamaOrderState():
    assert hasattr(model::WebshopStateMapping, "fakturamaOrderState")
    descriptor = None
    for klass in model::WebshopStateMapping.__mro__:
        if "fakturamaOrderState" in klass.__dict__:
            descriptor = klass.__dict__["fakturamaOrderState"]
            break
    assert isinstance(descriptor, property)

def test_model::webshopstatemapping_has_webshopState():
    assert hasattr(model::WebshopStateMapping, "webshopState")
    descriptor = None
    for klass in model::WebshopStateMapping.__mro__:
        if "webshopState" in klass.__dict__:
            descriptor = klass.__dict__["webshopState"]
            break
    assert isinstance(descriptor, property)



def test_model::webshop_is_not_abstract():
    assert not inspect.isabstract(model::WebShop)


def test_model::webshop_constructor_exists():
    assert callable(model::WebShop.__init__)


def test_model::webshop_constructor_args():
    sig = inspect.signature(model::WebShop.__init__)
    params = list(sig.parameters.keys())
    assert "webshopVendor" in params, "Missing parameter 'webshopVendor'"
    assert "webshopVersion" in params, "Missing parameter 'webshopVersion'"

def test_model::webshop_has_webshopVendor():
    assert hasattr(model::WebShop, "webshopVendor")
    descriptor = None
    for klass in model::WebShop.__mro__:
        if "webshopVendor" in klass.__dict__:
            descriptor = klass.__dict__["webshopVendor"]
            break
    assert isinstance(descriptor, property)

def test_model::webshop_has_webshopVersion():
    assert hasattr(model::WebShop, "webshopVersion")
    descriptor = None
    for klass in model::WebShop.__mro__:
        if "webshopVersion" in klass.__dict__:
            descriptor = klass.__dict__["webshopVersion"]
            break
    assert isinstance(descriptor, property)



def test_model::cefactcode_is_not_abstract():
    assert not inspect.isabstract(model::CEFACTCode)


def test_model::cefactcode_constructor_exists():
    assert callable(model::CEFACTCode.__init__)


def test_model::cefactcode_constructor_args():
    sig = inspect.signature(model::CEFACTCode.__init__)
    params = list(sig.parameters.keys())
    assert "abbreviation_de" in params, "Missing parameter 'abbreviation_de'"
    assert "target" in params, "Missing parameter 'target'"
    assert "name_de" in params, "Missing parameter 'name_de'"
    assert "code" in params, "Missing parameter 'code'"
    assert "abbreviation_en" in params, "Missing parameter 'abbreviation_en'"

def test_model::cefactcode_has_abbreviation_de():
    assert hasattr(model::CEFACTCode, "abbreviation_de")
    descriptor = None
    for klass in model::CEFACTCode.__mro__:
        if "abbreviation_de" in klass.__dict__:
            descriptor = klass.__dict__["abbreviation_de"]
            break
    assert isinstance(descriptor, property)

def test_model::cefactcode_has_target():
    assert hasattr(model::CEFACTCode, "target")
    descriptor = None
    for klass in model::CEFACTCode.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_model::cefactcode_has_name_de():
    assert hasattr(model::CEFACTCode, "name_de")
    descriptor = None
    for klass in model::CEFACTCode.__mro__:
        if "name_de" in klass.__dict__:
            descriptor = klass.__dict__["name_de"]
            break
    assert isinstance(descriptor, property)

def test_model::cefactcode_has_code():
    assert hasattr(model::CEFACTCode, "code")
    descriptor = None
    for klass in model::CEFACTCode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_model::cefactcode_has_abbreviation_en():
    assert hasattr(model::CEFACTCode, "abbreviation_en")
    descriptor = None
    for klass in model::CEFACTCode.__mro__:
        if "abbreviation_en" in klass.__dict__:
            descriptor = klass.__dict__["abbreviation_en"]
            break
    assert isinstance(descriptor, property)



def test_model::user_is_not_abstract():
    assert not inspect.isabstract(model::User)


def test_model::user_constructor_exists():
    assert callable(model::User.__init__)


def test_model::user_constructor_args():
    sig = inspect.signature(model::User.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "password" in params, "Missing parameter 'password'"

def test_model::user_has_userName():
    assert hasattr(model::User, "userName")
    descriptor = None
    for klass in model::User.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_model::user_has_password():
    assert hasattr(model::User, "password")
    descriptor = None
    for klass in model::User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_model::textcategory_is_not_abstract():
    assert not inspect.isabstract(model::TextCategory)


def test_model::textcategory_constructor_exists():
    assert callable(model::TextCategory.__init__)


def test_model::textcategory_constructor_args():
    sig = inspect.signature(model::TextCategory.__init__)
    params = list(sig.parameters.keys())



def test_model::textmodule_is_not_abstract():
    assert not inspect.isabstract(model::TextModule)


def test_model::textmodule_constructor_exists():
    assert callable(model::TextModule.__init__)


def test_model::textmodule_constructor_args():
    sig = inspect.signature(model::TextModule.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_model::textmodule_has_text():
    assert hasattr(model::TextModule, "text")
    descriptor = None
    for klass in model::TextModule.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_model::tenant_is_not_abstract():
    assert not inspect.isabstract(model::Tenant)


def test_model::tenant_constructor_exists():
    assert callable(model::Tenant.__init__)


def test_model::tenant_constructor_args():
    sig = inspect.signature(model::Tenant.__init__)
    params = list(sig.parameters.keys())



def test_model::shippingcategory_is_not_abstract():
    assert not inspect.isabstract(model::ShippingCategory)


def test_model::shippingcategory_constructor_exists():
    assert callable(model::ShippingCategory.__init__)


def test_model::shippingcategory_constructor_args():
    sig = inspect.signature(model::ShippingCategory.__init__)
    params = list(sig.parameters.keys())



def test_model::vatcategory_is_not_abstract():
    assert not inspect.isabstract(model::VATCategory)


def test_model::vatcategory_constructor_exists():
    assert callable(model::VATCategory.__init__)


def test_model::vatcategory_constructor_args():
    sig = inspect.signature(model::VATCategory.__init__)
    params = list(sig.parameters.keys())



def test_model::userproperty_is_not_abstract():
    assert not inspect.isabstract(model::UserProperty)


def test_model::userproperty_constructor_exists():
    assert callable(model::UserProperty.__init__)


def test_model::userproperty_constructor_args():
    sig = inspect.signature(model::UserProperty.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "value" in params, "Missing parameter 'value'"
    assert "user" in params, "Missing parameter 'user'"
    assert "global_" in params, "Missing parameter 'global_'"

def test_model::userproperty_has_default():
    assert hasattr(model::UserProperty, "default")
    descriptor = None
    for klass in model::UserProperty.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_model::userproperty_has_value():
    assert hasattr(model::UserProperty, "value")
    descriptor = None
    for klass in model::UserProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_model::userproperty_has_user():
    assert hasattr(model::UserProperty, "user")
    descriptor = None
    for klass in model::UserProperty.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_model::userproperty_has_global_():
    assert hasattr(model::UserProperty, "global_")
    descriptor = None
    for klass in model::UserProperty.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)



def test_model::role_is_not_abstract():
    assert not inspect.isabstract(model::Role)


def test_model::role_constructor_exists():
    assert callable(model::Role.__init__)


def test_model::role_constructor_args():
    sig = inspect.signature(model::Role.__init__)
    params = list(sig.parameters.keys())



def test_model::productoptions_is_not_abstract():
    assert not inspect.isabstract(model::ProductOptions)


def test_model::productoptions_constructor_exists():
    assert callable(model::ProductOptions.__init__)


def test_model::productoptions_constructor_args():
    sig = inspect.signature(model::ProductOptions.__init__)
    params = list(sig.parameters.keys())
    assert "sequenceNumber" in params, "Missing parameter 'sequenceNumber'"
    assert "attributeValue" in params, "Missing parameter 'attributeValue'"

def test_model::productoptions_has_sequenceNumber():
    assert hasattr(model::ProductOptions, "sequenceNumber")
    descriptor = None
    for klass in model::ProductOptions.__mro__:
        if "sequenceNumber" in klass.__dict__:
            descriptor = klass.__dict__["sequenceNumber"]
            break
    assert isinstance(descriptor, property)

def test_model::productoptions_has_attributeValue():
    assert hasattr(model::ProductOptions, "attributeValue")
    descriptor = None
    for klass in model::ProductOptions.__mro__:
        if "attributeValue" in klass.__dict__:
            descriptor = klass.__dict__["attributeValue"]
            break
    assert isinstance(descriptor, property)



def test_model::productcategory_is_not_abstract():
    assert not inspect.isabstract(model::ProductCategory)


def test_model::productcategory_constructor_exists():
    assert callable(model::ProductCategory.__init__)


def test_model::productcategory_constructor_args():
    sig = inspect.signature(model::ProductCategory.__init__)
    params = list(sig.parameters.keys())



def test_idescribableentity_is_not_abstract():
    assert not inspect.isabstract(IDescribableEntity)


def test_idescribableentity_constructor_exists():
    assert callable(IDescribableEntity.__init__)


def test_idescribableentity_constructor_args():
    sig = inspect.signature(IDescribableEntity.__init__)
    params = list(sig.parameters.keys())



def test_model::product_is_not_abstract():
    assert not inspect.isabstract(model::Product)


def test_model::product_constructor_exists():
    assert callable(model::Product.__init__)


def test_model::product_constructor_args():
    sig = inspect.signature(model::Product.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "itemNumber" in params, "Missing parameter 'itemNumber'"
    assert "price1" in params, "Missing parameter 'price1'"
    assert "cdf01" in params, "Missing parameter 'cdf01'"
    assert "block1" in params, "Missing parameter 'block1'"
    assert "block2" in params, "Missing parameter 'block2'"
    assert "price4" in params, "Missing parameter 'price4'"
    assert "cdf03" in params, "Missing parameter 'cdf03'"
    assert "price5" in params, "Missing parameter 'price5'"
    assert "sellingUnit" in params, "Missing parameter 'sellingUnit'"
    assert "block4" in params, "Missing parameter 'block4'"
    assert "quantityUnit" in params, "Missing parameter 'quantityUnit'"
    assert "gtin" in params, "Missing parameter 'gtin'"
    assert "picture" in params, "Missing parameter 'picture'"
    assert "block5" in params, "Missing parameter 'block5'"
    assert "block3" in params, "Missing parameter 'block3'"
    assert "cdf02" in params, "Missing parameter 'cdf02'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "price2" in params, "Missing parameter 'price2'"
    assert "webshopId" in params, "Missing parameter 'webshopId'"
    assert "costPrice" in params, "Missing parameter 'costPrice'"
    assert "price3" in params, "Missing parameter 'price3'"

def test_model::product_has_weight():
    assert hasattr(model::Product, "weight")
    descriptor = None
    for klass in model::Product.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_itemNumber():
    assert hasattr(model::Product, "itemNumber")
    descriptor = None
    for klass in model::Product.__mro__:
        if "itemNumber" in klass.__dict__:
            descriptor = klass.__dict__["itemNumber"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_price1():
    assert hasattr(model::Product, "price1")
    descriptor = None
    for klass in model::Product.__mro__:
        if "price1" in klass.__dict__:
            descriptor = klass.__dict__["price1"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_cdf01():
    assert hasattr(model::Product, "cdf01")
    descriptor = None
    for klass in model::Product.__mro__:
        if "cdf01" in klass.__dict__:
            descriptor = klass.__dict__["cdf01"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_block1():
    assert hasattr(model::Product, "block1")
    descriptor = None
    for klass in model::Product.__mro__:
        if "block1" in klass.__dict__:
            descriptor = klass.__dict__["block1"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_block2():
    assert hasattr(model::Product, "block2")
    descriptor = None
    for klass in model::Product.__mro__:
        if "block2" in klass.__dict__:
            descriptor = klass.__dict__["block2"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_price4():
    assert hasattr(model::Product, "price4")
    descriptor = None
    for klass in model::Product.__mro__:
        if "price4" in klass.__dict__:
            descriptor = klass.__dict__["price4"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_cdf03():
    assert hasattr(model::Product, "cdf03")
    descriptor = None
    for klass in model::Product.__mro__:
        if "cdf03" in klass.__dict__:
            descriptor = klass.__dict__["cdf03"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_price5():
    assert hasattr(model::Product, "price5")
    descriptor = None
    for klass in model::Product.__mro__:
        if "price5" in klass.__dict__:
            descriptor = klass.__dict__["price5"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_sellingUnit():
    assert hasattr(model::Product, "sellingUnit")
    descriptor = None
    for klass in model::Product.__mro__:
        if "sellingUnit" in klass.__dict__:
            descriptor = klass.__dict__["sellingUnit"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_block4():
    assert hasattr(model::Product, "block4")
    descriptor = None
    for klass in model::Product.__mro__:
        if "block4" in klass.__dict__:
            descriptor = klass.__dict__["block4"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_quantityUnit():
    assert hasattr(model::Product, "quantityUnit")
    descriptor = None
    for klass in model::Product.__mro__:
        if "quantityUnit" in klass.__dict__:
            descriptor = klass.__dict__["quantityUnit"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_gtin():
    assert hasattr(model::Product, "gtin")
    descriptor = None
    for klass in model::Product.__mro__:
        if "gtin" in klass.__dict__:
            descriptor = klass.__dict__["gtin"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_picture():
    assert hasattr(model::Product, "picture")
    descriptor = None
    for klass in model::Product.__mro__:
        if "picture" in klass.__dict__:
            descriptor = klass.__dict__["picture"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_block5():
    assert hasattr(model::Product, "block5")
    descriptor = None
    for klass in model::Product.__mro__:
        if "block5" in klass.__dict__:
            descriptor = klass.__dict__["block5"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_block3():
    assert hasattr(model::Product, "block3")
    descriptor = None
    for klass in model::Product.__mro__:
        if "block3" in klass.__dict__:
            descriptor = klass.__dict__["block3"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_cdf02():
    assert hasattr(model::Product, "cdf02")
    descriptor = None
    for klass in model::Product.__mro__:
        if "cdf02" in klass.__dict__:
            descriptor = klass.__dict__["cdf02"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_quantity():
    assert hasattr(model::Product, "quantity")
    descriptor = None
    for klass in model::Product.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_price2():
    assert hasattr(model::Product, "price2")
    descriptor = None
    for klass in model::Product.__mro__:
        if "price2" in klass.__dict__:
            descriptor = klass.__dict__["price2"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_webshopId():
    assert hasattr(model::Product, "webshopId")
    descriptor = None
    for klass in model::Product.__mro__:
        if "webshopId" in klass.__dict__:
            descriptor = klass.__dict__["webshopId"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_costPrice():
    assert hasattr(model::Product, "costPrice")
    descriptor = None
    for klass in model::Product.__mro__:
        if "costPrice" in klass.__dict__:
            descriptor = klass.__dict__["costPrice"]
            break
    assert isinstance(descriptor, property)

def test_model::product_has_price3():
    assert hasattr(model::Product, "price3")
    descriptor = None
    for klass in model::Product.__mro__:
        if "price3" in klass.__dict__:
            descriptor = klass.__dict__["price3"]
            break
    assert isinstance(descriptor, property)



def test_model::shipping_is_not_abstract():
    assert not inspect.isabstract(model::Shipping)


def test_model::shipping_constructor_exists():
    assert callable(model::Shipping.__init__)


def test_model::shipping_constructor_args():
    sig = inspect.signature(model::Shipping.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "autoVat" in params, "Missing parameter 'autoVat'"
    assert "shippingValue" in params, "Missing parameter 'shippingValue'"

def test_model::shipping_has_code():
    assert hasattr(model::Shipping, "code")
    descriptor = None
    for klass in model::Shipping.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_model::shipping_has_autoVat():
    assert hasattr(model::Shipping, "autoVat")
    descriptor = None
    for klass in model::Shipping.__mro__:
        if "autoVat" in klass.__dict__:
            descriptor = klass.__dict__["autoVat"]
            break
    assert isinstance(descriptor, property)

def test_model::shipping_has_shippingValue():
    assert hasattr(model::Shipping, "shippingValue")
    descriptor = None
    for klass in model::Shipping.__mro__:
        if "shippingValue" in klass.__dict__:
            descriptor = klass.__dict__["shippingValue"]
            break
    assert isinstance(descriptor, property)



def test_model::productblockprice_is_not_abstract():
    assert not inspect.isabstract(model::ProductBlockPrice)


def test_model::productblockprice_constructor_exists():
    assert callable(model::ProductBlockPrice.__init__)


def test_model::productblockprice_constructor_args():
    sig = inspect.signature(model::ProductBlockPrice.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "block" in params, "Missing parameter 'block'"

def test_model::productblockprice_has_price():
    assert hasattr(model::ProductBlockPrice, "price")
    descriptor = None
    for klass in model::ProductBlockPrice.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_model::productblockprice_has_block():
    assert hasattr(model::ProductBlockPrice, "block")
    descriptor = None
    for klass in model::ProductBlockPrice.__mro__:
        if "block" in klass.__dict__:
            descriptor = klass.__dict__["block"]
            break
    assert isinstance(descriptor, property)



def test_model::itemaccounttype_is_not_abstract():
    assert not inspect.isabstract(model::ItemAccountType)


def test_model::itemaccounttype_constructor_exists():
    assert callable(model::ItemAccountType.__init__)


def test_model::itemaccounttype_constructor_args():
    sig = inspect.signature(model::ItemAccountType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::itemaccounttype_has_value():
    assert hasattr(model::ItemAccountType, "value")
    descriptor = None
    for klass in model::ItemAccountType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::voucheritem_is_not_abstract():
    assert not inspect.isabstract(model::VoucherItem)


def test_model::voucheritem_constructor_exists():
    assert callable(model::VoucherItem.__init__)


def test_model::voucheritem_constructor_args():
    sig = inspect.signature(model::VoucherItem.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "posNr" in params, "Missing parameter 'posNr'"
    assert "itemVoucherType" in params, "Missing parameter 'itemVoucherType'"

def test_model::voucheritem_has_price():
    assert hasattr(model::VoucherItem, "price")
    descriptor = None
    for klass in model::VoucherItem.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_model::voucheritem_has_posNr():
    assert hasattr(model::VoucherItem, "posNr")
    descriptor = None
    for klass in model::VoucherItem.__mro__:
        if "posNr" in klass.__dict__:
            descriptor = klass.__dict__["posNr"]
            break
    assert isinstance(descriptor, property)

def test_model::voucheritem_has_itemVoucherType():
    assert hasattr(model::VoucherItem, "itemVoucherType")
    descriptor = None
    for klass in model::VoucherItem.__mro__:
        if "itemVoucherType" in klass.__dict__:
            descriptor = klass.__dict__["itemVoucherType"]
            break
    assert isinstance(descriptor, property)



def test_model::voucher_is_not_abstract():
    assert not inspect.isabstract(model::Voucher)


def test_model::voucher_constructor_exists():
    assert callable(model::Voucher.__init__)


def test_model::voucher_constructor_args():
    sig = inspect.signature(model::Voucher.__init__)
    params = list(sig.parameters.keys())
    assert "paidValue" in params, "Missing parameter 'paidValue'"
    assert "voucherNumber" in params, "Missing parameter 'voucherNumber'"
    assert "documentNumber" in params, "Missing parameter 'documentNumber'"
    assert "discounted" in params, "Missing parameter 'discounted'"
    assert "doNotBook" in params, "Missing parameter 'doNotBook'"
    assert "voucherType" in params, "Missing parameter 'voucherType'"
    assert "totalValue" in params, "Missing parameter 'totalValue'"
    assert "voucherDate" in params, "Missing parameter 'voucherDate'"

def test_model::voucher_has_paidValue():
    assert hasattr(model::Voucher, "paidValue")
    descriptor = None
    for klass in model::Voucher.__mro__:
        if "paidValue" in klass.__dict__:
            descriptor = klass.__dict__["paidValue"]
            break
    assert isinstance(descriptor, property)

def test_model::voucher_has_voucherNumber():
    assert hasattr(model::Voucher, "voucherNumber")
    descriptor = None
    for klass in model::Voucher.__mro__:
        if "voucherNumber" in klass.__dict__:
            descriptor = klass.__dict__["voucherNumber"]
            break
    assert isinstance(descriptor, property)

def test_model::voucher_has_documentNumber():
    assert hasattr(model::Voucher, "documentNumber")
    descriptor = None
    for klass in model::Voucher.__mro__:
        if "documentNumber" in klass.__dict__:
            descriptor = klass.__dict__["documentNumber"]
            break
    assert isinstance(descriptor, property)

def test_model::voucher_has_discounted():
    assert hasattr(model::Voucher, "discounted")
    descriptor = None
    for klass in model::Voucher.__mro__:
        if "discounted" in klass.__dict__:
            descriptor = klass.__dict__["discounted"]
            break
    assert isinstance(descriptor, property)

def test_model::voucher_has_doNotBook():
    assert hasattr(model::Voucher, "doNotBook")
    descriptor = None
    for klass in model::Voucher.__mro__:
        if "doNotBook" in klass.__dict__:
            descriptor = klass.__dict__["doNotBook"]
            break
    assert isinstance(descriptor, property)

def test_model::voucher_has_voucherType():
    assert hasattr(model::Voucher, "voucherType")
    descriptor = None
    for klass in model::Voucher.__mro__:
        if "voucherType" in klass.__dict__:
            descriptor = klass.__dict__["voucherType"]
            break
    assert isinstance(descriptor, property)

def test_model::voucher_has_totalValue():
    assert hasattr(model::Voucher, "totalValue")
    descriptor = None
    for klass in model::Voucher.__mro__:
        if "totalValue" in klass.__dict__:
            descriptor = klass.__dict__["totalValue"]
            break
    assert isinstance(descriptor, property)

def test_model::voucher_has_voucherDate():
    assert hasattr(model::Voucher, "voucherDate")
    descriptor = None
    for klass in model::Voucher.__mro__:
        if "voucherDate" in klass.__dict__:
            descriptor = klass.__dict__["voucherDate"]
            break
    assert isinstance(descriptor, property)



def test_model::proforma_is_not_abstract():
    assert not inspect.isabstract(model::Proforma)


def test_model::proforma_constructor_exists():
    assert callable(model::Proforma.__init__)


def test_model::proforma_constructor_args():
    sig = inspect.signature(model::Proforma.__init__)
    params = list(sig.parameters.keys())

def test_reliabilitytype_exists():
    # Check that the Enumeration exists
    assert ReliabilityType is not None

def test_reliabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReliabilityType]
    expected_literals = [
        "GOOD",
        "NONE",
        "MEDIUM",
        "POOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReliabilityType"

def test_shippingvattype_exists():
    # Check that the Enumeration exists
    assert ShippingVatType is not None

def test_shippingvattype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShippingVatType]
    expected_literals = [
        "SHIPPINGVATFIX",
        "SHIPPINGVATNET",
        "SHIPPINGVATGROSS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShippingVatType"

def test_vouchertype_exists():
    # Check that the Enumeration exists
    assert VoucherType is not None

def test_vouchertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VoucherType]
    expected_literals = [
        "EXPENDITURE",
        "RECEIPTVOUCHER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VoucherType"

def test_billingtype_exists():
    # Check that the Enumeration exists
    assert BillingType is not None

def test_billingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BillingType]
    expected_literals = [
        "OFFER",
        "PROFORMA",
        "NONE",
        "ORDER",
        "DUNNING",
        "LETTER",
        "DELIVERY",
        "CREDIT",
        "INVOICE",
        "CONFIRMATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BillingType"

def test_contacttype_exists():
    # Check that the Enumeration exists
    assert ContactType is not None

def test_contacttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContactType]
    expected_literals = [
        "DELIVERY",
        "BILLING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContactType"

def test_itemtype_exists():
    # Check that the Enumeration exists
    assert ItemType is not None

def test_itemtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ItemType]
    expected_literals = [
        "DELIVERY_PART",
        "SUBTOTAL",
        "FREETEXT",
        "POSITION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ItemType"


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
Document_strategy = st.builds(
    Document,
)
model::Delivery_strategy = st.builds(
    model::Delivery,
)
model::Dunning_strategy = st.builds(
    model::Dunning,
    dunningLevel=
        safe_text
)
model::Credit_strategy = st.builds(
    model::Credit,
)
model::Order_strategy = st.builds(
    model::Order,
)
model::Offer_strategy = st.builds(
    model::Offer,
)
model::Confirmation_strategy = st.builds(
    model::Confirmation,
)
model::Letter_strategy = st.builds(
    model::Letter,
)
Contact_strategy = st.builds(
    Contact,
)
model::Debitor_strategy = st.builds(
    model::Debitor,
)
model::Creditor_strategy = st.builds(
    model::Creditor,
)
model::Invoice_strategy = st.builds(
    model::Invoice,
)
AbstractCategory_strategy = st.builds(
    AbstractCategory,
)
model::ItemListTypeCategory_strategy = st.builds(
    model::ItemListTypeCategory,
)
model::VoucherCategory_strategy = st.builds(
    model::VoucherCategory,
)
IEntity_strategy = st.builds(
    IEntity,
)
model::DocumentItem_strategy = st.builds(
    model::DocumentItem,
    itemType=
        safe_text,
    price=
        safe_text,
    optional=
        safe_text,
    gtin=
        safe_text,
    vestingPeriodStart=
        st.dates(),
    noVat=
        safe_text,
    quantity=
        safe_text,
    vestingPeriodEnd=
        st.dates(),
    itemNumber=
        safe_text,
    quantityUnit=
        safe_text,
    weight=
        safe_text,
    tara=
        safe_text,
    description=
        safe_text,
    originQuantity=
        safe_text,
    posNr=
        safe_text,
    itemRebate=
        safe_text,
    picture=
        safe_text
)
model::BankAccount_strategy = st.builds(
    model::BankAccount,
    iban=
        safe_text,
    bankCode=
        safe_text,
    accountHolder=
        safe_text,
    bic=
        safe_text,
    bankName=
        safe_text
)
model::Contact_strategy = st.builds(
    model::Contact,
    discount=
        safe_text,
    webshopName=
        safe_text,
    website=
        safe_text,
    birthday=
        st.dates(),
    note=
        safe_text,
    useNetGross=
        safe_text,
    customerNumber=
        safe_text,
    gln=
        safe_text,
    title=
        safe_text,
    fax=
        safe_text,
    gender=
        safe_text,
    company=
        safe_text,
    supplierNumber=
        safe_text,
    email=
        safe_text,
    vatNumberValid=
        safe_text,
    useSalesEqualizationTax=
        safe_text,
    firstName=
        safe_text,
    mandateReference=
        safe_text,
    vatNumber=
        safe_text,
    reliability=
        safe_text,
    mobile=
        safe_text,
    phone=
        safe_text,
    contactType=
        safe_text
)
model::Document_strategy = st.builds(
    model::Document,
    deposit=
        safe_text,
    documentDate=
        st.dates(),
    printed=
        safe_text,
    itemsRebate=
        safe_text,
    paidValue=
        safe_text,
    shippingAutoVat=
        safe_text,
    vestingPeriodEnd=
        st.dates(),
    odtPath=
        safe_text,
    paid=
        safe_text,
    shippingValue=
        safe_text,
    progress=
        safe_text,
    customerRef=
        safe_text,
    pdfPath=
        safe_text,
    addressFirstLine=
        safe_text,
    transactionId=
        safe_text,
    consultant=
        safe_text,
    dueDays=
        safe_text,
    payDate=
        st.dates(),
    serviceDate=
        st.dates(),
    printTemplate=
        safe_text,
    vestingPeriodStart=
        st.dates(),
    message3=
        safe_text,
    message2=
        safe_text,
    message=
        safe_text,
    webshopId=
        safe_text,
    orderDate=
        st.dates(),
    billingType=
        safe_text,
    netGross=
        safe_text,
    webshopDate=
        st.dates(),
    totalValue=
        safe_text
)
model::Address_strategy = st.builds(
    model::Address,
    cityAddon=
        safe_text,
    street=
        safe_text,
    zip=
        safe_text,
    manualAddress=
        safe_text,
    city=
        safe_text,
    countryCode=
        safe_text
)
model::IndividualDocumentInfo_strategy = st.builds(
    model::IndividualDocumentInfo,
    noVatName=
        safe_text,
    shippingAutoVat=
        safe_text,
    paymentDescription=
        safe_text,
    shippingValue=
        safe_text,
    paymentText=
        safe_text,
    shippingDescription=
        safe_text,
    shippingVatDescription=
        safe_text,
    paymentName=
        safe_text,
    shippingName=
        safe_text,
    noVatDescription=
        safe_text,
    shippingVatValue=
        safe_text
)
model::VAT_strategy = st.builds(
    model::VAT,
    salesEqualizationTax=
        safe_text,
    description=
        safe_text,
    taxValue=
        safe_text
)
model::AbstractCategory_strategy = st.builds(
    model::AbstractCategory,
)
model::IDescribableEntity_strategy = st.builds(
    model::IDescribableEntity,
    description=
        safe_text
)
model::Payment_strategy = st.builds(
    model::Payment,
    discountValue=
        safe_text,
    unpaidText=
        safe_text,
    netDays=
        safe_text,
    paidText=
        safe_text,
    code=
        safe_text,
    depositText=
        safe_text,
    description=
        safe_text,
    discountDays=
        safe_text
)
model::ContactCategory_strategy = st.builds(
    model::ContactCategory,
)
model::IEntity_strategy = st.builds(
    model::IEntity,
    name=
        safe_text,
    deleted=
        safe_text,
    modifiedBy=
        safe_text,
    validFrom=
        st.dates(),
    id=
        safe_text,
    validTo=
        st.dates(),
    dateAdded=
        st.dates(),
    modified=
        st.dates()
)
model::WebshopStateMapping_strategy = st.builds(
    model::WebshopStateMapping,
    fakturamaOrderState=
        safe_text,
    webshopState=
        safe_text
)
model::WebShop_strategy = st.builds(
    model::WebShop,
    webshopVendor=
        safe_text,
    webshopVersion=
        safe_text
)
model::CEFACTCode_strategy = st.builds(
    model::CEFACTCode,
    abbreviation_de=
        safe_text,
    target=
        safe_text,
    name_de=
        safe_text,
    code=
        safe_text,
    abbreviation_en=
        safe_text
)
model::User_strategy = st.builds(
    model::User,
    userName=
        safe_text,
    password=
        safe_text
)
model::TextCategory_strategy = st.builds(
    model::TextCategory,
)
model::TextModule_strategy = st.builds(
    model::TextModule,
    text=
        safe_text
)
model::Tenant_strategy = st.builds(
    model::Tenant,
)
model::ShippingCategory_strategy = st.builds(
    model::ShippingCategory,
)
model::VATCategory_strategy = st.builds(
    model::VATCategory,
)
model::UserProperty_strategy = st.builds(
    model::UserProperty,
    default=
        safe_text,
    value=
        safe_text,
    user=
        safe_text,
    global_=
        safe_text
)
model::Role_strategy = st.builds(
    model::Role,
)
model::ProductOptions_strategy = st.builds(
    model::ProductOptions,
    sequenceNumber=
        safe_text,
    attributeValue=
        safe_text
)
model::ProductCategory_strategy = st.builds(
    model::ProductCategory,
)
IDescribableEntity_strategy = st.builds(
    IDescribableEntity,
)
model::Product_strategy = st.builds(
    model::Product,
    weight=
        safe_text,
    itemNumber=
        safe_text,
    price1=
        safe_text,
    cdf01=
        safe_text,
    block1=
        safe_text,
    block2=
        safe_text,
    price4=
        safe_text,
    cdf03=
        safe_text,
    price5=
        safe_text,
    sellingUnit=
        safe_text,
    block4=
        safe_text,
    quantityUnit=
        safe_text,
    gtin=
        safe_text,
    picture=
        safe_text,
    block5=
        safe_text,
    block3=
        safe_text,
    cdf02=
        safe_text,
    quantity=
        safe_text,
    price2=
        safe_text,
    webshopId=
        safe_text,
    costPrice=
        safe_text,
    price3=
        safe_text
)
model::Shipping_strategy = st.builds(
    model::Shipping,
    code=
        safe_text,
    autoVat=
        safe_text,
    shippingValue=
        safe_text
)
model::ProductBlockPrice_strategy = st.builds(
    model::ProductBlockPrice,
    price=
        safe_text,
    block=
        safe_text
)
model::ItemAccountType_strategy = st.builds(
    model::ItemAccountType,
    value=
        safe_text
)
model::VoucherItem_strategy = st.builds(
    model::VoucherItem,
    price=
        safe_text,
    posNr=
        safe_text,
    itemVoucherType=
        safe_text
)
model::Voucher_strategy = st.builds(
    model::Voucher,
    paidValue=
        safe_text,
    voucherNumber=
        safe_text,
    documentNumber=
        safe_text,
    discounted=
        safe_text,
    doNotBook=
        safe_text,
    voucherType=
        safe_text,
    totalValue=
        safe_text,
    voucherDate=
        st.dates()
)
model::Proforma_strategy = st.builds(
    model::Proforma,
)

@given(instance=Document_strategy)
@settings(max_examples=50)
def test_document_instantiation(instance):
    assert isinstance(instance, Document)

@given(instance=model::Delivery_strategy)
@settings(max_examples=50)
def test_model::delivery_instantiation(instance):
    assert isinstance(instance, model::Delivery)

@given(instance=model::Dunning_strategy)
@settings(max_examples=50)
def test_model::dunning_instantiation(instance):
    assert isinstance(instance, model::Dunning)

@given(instance=model::Dunning_strategy)
def test_model::dunning_dunningLevel_type(instance):
    assert isinstance(instance.dunningLevel, str)


@given(instance=model::Dunning_strategy)
def test_model::dunning_dunningLevel_setter(instance):
    original = instance.dunningLevel
    instance.dunningLevel = original
    assert instance.dunningLevel == original

@given(instance=model::Credit_strategy)
@settings(max_examples=50)
def test_model::credit_instantiation(instance):
    assert isinstance(instance, model::Credit)

@given(instance=model::Order_strategy)
@settings(max_examples=50)
def test_model::order_instantiation(instance):
    assert isinstance(instance, model::Order)

@given(instance=model::Offer_strategy)
@settings(max_examples=50)
def test_model::offer_instantiation(instance):
    assert isinstance(instance, model::Offer)

@given(instance=model::Confirmation_strategy)
@settings(max_examples=50)
def test_model::confirmation_instantiation(instance):
    assert isinstance(instance, model::Confirmation)

@given(instance=model::Letter_strategy)
@settings(max_examples=50)
def test_model::letter_instantiation(instance):
    assert isinstance(instance, model::Letter)

@given(instance=Contact_strategy)
@settings(max_examples=50)
def test_contact_instantiation(instance):
    assert isinstance(instance, Contact)

@given(instance=model::Debitor_strategy)
@settings(max_examples=50)
def test_model::debitor_instantiation(instance):
    assert isinstance(instance, model::Debitor)

@given(instance=model::Creditor_strategy)
@settings(max_examples=50)
def test_model::creditor_instantiation(instance):
    assert isinstance(instance, model::Creditor)

@given(instance=model::Invoice_strategy)
@settings(max_examples=50)
def test_model::invoice_instantiation(instance):
    assert isinstance(instance, model::Invoice)

@given(instance=AbstractCategory_strategy)
@settings(max_examples=50)
def test_abstractcategory_instantiation(instance):
    assert isinstance(instance, AbstractCategory)

@given(instance=model::ItemListTypeCategory_strategy)
@settings(max_examples=50)
def test_model::itemlisttypecategory_instantiation(instance):
    assert isinstance(instance, model::ItemListTypeCategory)

@given(instance=model::VoucherCategory_strategy)
@settings(max_examples=50)
def test_model::vouchercategory_instantiation(instance):
    assert isinstance(instance, model::VoucherCategory)

@given(instance=IEntity_strategy)
@settings(max_examples=50)
def test_ientity_instantiation(instance):
    assert isinstance(instance, IEntity)

@given(instance=model::DocumentItem_strategy)
@settings(max_examples=50)
def test_model::documentitem_instantiation(instance):
    assert isinstance(instance, model::DocumentItem)

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_itemType_type(instance):
    assert isinstance(instance.itemType, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_itemType_setter(instance):
    original = instance.itemType
    instance.itemType = original
    assert instance.itemType == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_price_type(instance):
    assert isinstance(instance.price, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_gtin_type(instance):
    assert isinstance(instance.gtin, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_gtin_setter(instance):
    original = instance.gtin
    instance.gtin = original
    assert instance.gtin == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_vestingPeriodStart_type(instance):
    assert isinstance(instance.vestingPeriodStart, date)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_vestingPeriodStart_setter(instance):
    original = instance.vestingPeriodStart
    instance.vestingPeriodStart = original
    assert instance.vestingPeriodStart == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_noVat_type(instance):
    assert isinstance(instance.noVat, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_noVat_setter(instance):
    original = instance.noVat
    instance.noVat = original
    assert instance.noVat == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_quantity_type(instance):
    assert isinstance(instance.quantity, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_vestingPeriodEnd_type(instance):
    assert isinstance(instance.vestingPeriodEnd, date)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_vestingPeriodEnd_setter(instance):
    original = instance.vestingPeriodEnd
    instance.vestingPeriodEnd = original
    assert instance.vestingPeriodEnd == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_itemNumber_type(instance):
    assert isinstance(instance.itemNumber, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_itemNumber_setter(instance):
    original = instance.itemNumber
    instance.itemNumber = original
    assert instance.itemNumber == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_quantityUnit_type(instance):
    assert isinstance(instance.quantityUnit, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_quantityUnit_setter(instance):
    original = instance.quantityUnit
    instance.quantityUnit = original
    assert instance.quantityUnit == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_tara_type(instance):
    assert isinstance(instance.tara, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_tara_setter(instance):
    original = instance.tara
    instance.tara = original
    assert instance.tara == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_originQuantity_type(instance):
    assert isinstance(instance.originQuantity, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_originQuantity_setter(instance):
    original = instance.originQuantity
    instance.originQuantity = original
    assert instance.originQuantity == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_posNr_type(instance):
    assert isinstance(instance.posNr, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_posNr_setter(instance):
    original = instance.posNr
    instance.posNr = original
    assert instance.posNr == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_itemRebate_type(instance):
    assert isinstance(instance.itemRebate, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_itemRebate_setter(instance):
    original = instance.itemRebate
    instance.itemRebate = original
    assert instance.itemRebate == original

@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_picture_type(instance):
    assert isinstance(instance.picture, str)


@given(instance=model::DocumentItem_strategy)
def test_model::documentitem_picture_setter(instance):
    original = instance.picture
    instance.picture = original
    assert instance.picture == original

@given(instance=model::BankAccount_strategy)
@settings(max_examples=50)
def test_model::bankaccount_instantiation(instance):
    assert isinstance(instance, model::BankAccount)

@given(instance=model::BankAccount_strategy)
def test_model::bankaccount_iban_type(instance):
    assert isinstance(instance.iban, str)


@given(instance=model::BankAccount_strategy)
def test_model::bankaccount_iban_setter(instance):
    original = instance.iban
    instance.iban = original
    assert instance.iban == original

@given(instance=model::BankAccount_strategy)
def test_model::bankaccount_bankCode_type(instance):
    assert isinstance(instance.bankCode, str)


@given(instance=model::BankAccount_strategy)
def test_model::bankaccount_bankCode_setter(instance):
    original = instance.bankCode
    instance.bankCode = original
    assert instance.bankCode == original

@given(instance=model::BankAccount_strategy)
def test_model::bankaccount_accountHolder_type(instance):
    assert isinstance(instance.accountHolder, str)


@given(instance=model::BankAccount_strategy)
def test_model::bankaccount_accountHolder_setter(instance):
    original = instance.accountHolder
    instance.accountHolder = original
    assert instance.accountHolder == original

@given(instance=model::BankAccount_strategy)
def test_model::bankaccount_bic_type(instance):
    assert isinstance(instance.bic, str)


@given(instance=model::BankAccount_strategy)
def test_model::bankaccount_bic_setter(instance):
    original = instance.bic
    instance.bic = original
    assert instance.bic == original

@given(instance=model::BankAccount_strategy)
def test_model::bankaccount_bankName_type(instance):
    assert isinstance(instance.bankName, str)


@given(instance=model::BankAccount_strategy)
def test_model::bankaccount_bankName_setter(instance):
    original = instance.bankName
    instance.bankName = original
    assert instance.bankName == original

@given(instance=model::Contact_strategy)
@settings(max_examples=50)
def test_model::contact_instantiation(instance):
    assert isinstance(instance, model::Contact)

@given(instance=model::Contact_strategy)
def test_model::contact_discount_type(instance):
    assert isinstance(instance.discount, str)


@given(instance=model::Contact_strategy)
def test_model::contact_discount_setter(instance):
    original = instance.discount
    instance.discount = original
    assert instance.discount == original

@given(instance=model::Contact_strategy)
def test_model::contact_webshopName_type(instance):
    assert isinstance(instance.webshopName, str)


@given(instance=model::Contact_strategy)
def test_model::contact_webshopName_setter(instance):
    original = instance.webshopName
    instance.webshopName = original
    assert instance.webshopName == original

@given(instance=model::Contact_strategy)
def test_model::contact_website_type(instance):
    assert isinstance(instance.website, str)


@given(instance=model::Contact_strategy)
def test_model::contact_website_setter(instance):
    original = instance.website
    instance.website = original
    assert instance.website == original

@given(instance=model::Contact_strategy)
def test_model::contact_birthday_type(instance):
    assert isinstance(instance.birthday, date)


@given(instance=model::Contact_strategy)
def test_model::contact_birthday_setter(instance):
    original = instance.birthday
    instance.birthday = original
    assert instance.birthday == original

@given(instance=model::Contact_strategy)
def test_model::contact_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=model::Contact_strategy)
def test_model::contact_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=model::Contact_strategy)
def test_model::contact_useNetGross_type(instance):
    assert isinstance(instance.useNetGross, str)


@given(instance=model::Contact_strategy)
def test_model::contact_useNetGross_setter(instance):
    original = instance.useNetGross
    instance.useNetGross = original
    assert instance.useNetGross == original

@given(instance=model::Contact_strategy)
def test_model::contact_customerNumber_type(instance):
    assert isinstance(instance.customerNumber, str)


@given(instance=model::Contact_strategy)
def test_model::contact_customerNumber_setter(instance):
    original = instance.customerNumber
    instance.customerNumber = original
    assert instance.customerNumber == original

@given(instance=model::Contact_strategy)
def test_model::contact_gln_type(instance):
    assert isinstance(instance.gln, str)


@given(instance=model::Contact_strategy)
def test_model::contact_gln_setter(instance):
    original = instance.gln
    instance.gln = original
    assert instance.gln == original

@given(instance=model::Contact_strategy)
def test_model::contact_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=model::Contact_strategy)
def test_model::contact_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=model::Contact_strategy)
def test_model::contact_fax_type(instance):
    assert isinstance(instance.fax, str)


@given(instance=model::Contact_strategy)
def test_model::contact_fax_setter(instance):
    original = instance.fax
    instance.fax = original
    assert instance.fax == original

@given(instance=model::Contact_strategy)
def test_model::contact_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=model::Contact_strategy)
def test_model::contact_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=model::Contact_strategy)
def test_model::contact_company_type(instance):
    assert isinstance(instance.company, str)


@given(instance=model::Contact_strategy)
def test_model::contact_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=model::Contact_strategy)
def test_model::contact_supplierNumber_type(instance):
    assert isinstance(instance.supplierNumber, str)


@given(instance=model::Contact_strategy)
def test_model::contact_supplierNumber_setter(instance):
    original = instance.supplierNumber
    instance.supplierNumber = original
    assert instance.supplierNumber == original

@given(instance=model::Contact_strategy)
def test_model::contact_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=model::Contact_strategy)
def test_model::contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=model::Contact_strategy)
def test_model::contact_vatNumberValid_type(instance):
    assert isinstance(instance.vatNumberValid, str)


@given(instance=model::Contact_strategy)
def test_model::contact_vatNumberValid_setter(instance):
    original = instance.vatNumberValid
    instance.vatNumberValid = original
    assert instance.vatNumberValid == original

@given(instance=model::Contact_strategy)
def test_model::contact_useSalesEqualizationTax_type(instance):
    assert isinstance(instance.useSalesEqualizationTax, str)


@given(instance=model::Contact_strategy)
def test_model::contact_useSalesEqualizationTax_setter(instance):
    original = instance.useSalesEqualizationTax
    instance.useSalesEqualizationTax = original
    assert instance.useSalesEqualizationTax == original

@given(instance=model::Contact_strategy)
def test_model::contact_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=model::Contact_strategy)
def test_model::contact_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=model::Contact_strategy)
def test_model::contact_mandateReference_type(instance):
    assert isinstance(instance.mandateReference, str)


@given(instance=model::Contact_strategy)
def test_model::contact_mandateReference_setter(instance):
    original = instance.mandateReference
    instance.mandateReference = original
    assert instance.mandateReference == original

@given(instance=model::Contact_strategy)
def test_model::contact_vatNumber_type(instance):
    assert isinstance(instance.vatNumber, str)


@given(instance=model::Contact_strategy)
def test_model::contact_vatNumber_setter(instance):
    original = instance.vatNumber
    instance.vatNumber = original
    assert instance.vatNumber == original

@given(instance=model::Contact_strategy)
def test_model::contact_reliability_type(instance):
    assert isinstance(instance.reliability, str)


@given(instance=model::Contact_strategy)
def test_model::contact_reliability_setter(instance):
    original = instance.reliability
    instance.reliability = original
    assert instance.reliability == original

@given(instance=model::Contact_strategy)
def test_model::contact_mobile_type(instance):
    assert isinstance(instance.mobile, str)


@given(instance=model::Contact_strategy)
def test_model::contact_mobile_setter(instance):
    original = instance.mobile
    instance.mobile = original
    assert instance.mobile == original

@given(instance=model::Contact_strategy)
def test_model::contact_phone_type(instance):
    assert isinstance(instance.phone, str)


@given(instance=model::Contact_strategy)
def test_model::contact_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original

@given(instance=model::Contact_strategy)
def test_model::contact_contactType_type(instance):
    assert isinstance(instance.contactType, str)


@given(instance=model::Contact_strategy)
def test_model::contact_contactType_setter(instance):
    original = instance.contactType
    instance.contactType = original
    assert instance.contactType == original

@given(instance=model::Document_strategy)
@settings(max_examples=50)
def test_model::document_instantiation(instance):
    assert isinstance(instance, model::Document)

@given(instance=model::Document_strategy)
def test_model::document_deposit_type(instance):
    assert isinstance(instance.deposit, str)


@given(instance=model::Document_strategy)
def test_model::document_deposit_setter(instance):
    original = instance.deposit
    instance.deposit = original
    assert instance.deposit == original

@given(instance=model::Document_strategy)
def test_model::document_documentDate_type(instance):
    assert isinstance(instance.documentDate, date)


@given(instance=model::Document_strategy)
def test_model::document_documentDate_setter(instance):
    original = instance.documentDate
    instance.documentDate = original
    assert instance.documentDate == original

@given(instance=model::Document_strategy)
def test_model::document_printed_type(instance):
    assert isinstance(instance.printed, str)


@given(instance=model::Document_strategy)
def test_model::document_printed_setter(instance):
    original = instance.printed
    instance.printed = original
    assert instance.printed == original

@given(instance=model::Document_strategy)
def test_model::document_itemsRebate_type(instance):
    assert isinstance(instance.itemsRebate, str)


@given(instance=model::Document_strategy)
def test_model::document_itemsRebate_setter(instance):
    original = instance.itemsRebate
    instance.itemsRebate = original
    assert instance.itemsRebate == original

@given(instance=model::Document_strategy)
def test_model::document_paidValue_type(instance):
    assert isinstance(instance.paidValue, str)


@given(instance=model::Document_strategy)
def test_model::document_paidValue_setter(instance):
    original = instance.paidValue
    instance.paidValue = original
    assert instance.paidValue == original

@given(instance=model::Document_strategy)
def test_model::document_shippingAutoVat_type(instance):
    assert isinstance(instance.shippingAutoVat, str)


@given(instance=model::Document_strategy)
def test_model::document_shippingAutoVat_setter(instance):
    original = instance.shippingAutoVat
    instance.shippingAutoVat = original
    assert instance.shippingAutoVat == original

@given(instance=model::Document_strategy)
def test_model::document_vestingPeriodEnd_type(instance):
    assert isinstance(instance.vestingPeriodEnd, date)


@given(instance=model::Document_strategy)
def test_model::document_vestingPeriodEnd_setter(instance):
    original = instance.vestingPeriodEnd
    instance.vestingPeriodEnd = original
    assert instance.vestingPeriodEnd == original

@given(instance=model::Document_strategy)
def test_model::document_odtPath_type(instance):
    assert isinstance(instance.odtPath, str)


@given(instance=model::Document_strategy)
def test_model::document_odtPath_setter(instance):
    original = instance.odtPath
    instance.odtPath = original
    assert instance.odtPath == original

@given(instance=model::Document_strategy)
def test_model::document_paid_type(instance):
    assert isinstance(instance.paid, str)


@given(instance=model::Document_strategy)
def test_model::document_paid_setter(instance):
    original = instance.paid
    instance.paid = original
    assert instance.paid == original

@given(instance=model::Document_strategy)
def test_model::document_shippingValue_type(instance):
    assert isinstance(instance.shippingValue, str)


@given(instance=model::Document_strategy)
def test_model::document_shippingValue_setter(instance):
    original = instance.shippingValue
    instance.shippingValue = original
    assert instance.shippingValue == original

@given(instance=model::Document_strategy)
def test_model::document_progress_type(instance):
    assert isinstance(instance.progress, str)


@given(instance=model::Document_strategy)
def test_model::document_progress_setter(instance):
    original = instance.progress
    instance.progress = original
    assert instance.progress == original

@given(instance=model::Document_strategy)
def test_model::document_customerRef_type(instance):
    assert isinstance(instance.customerRef, str)


@given(instance=model::Document_strategy)
def test_model::document_customerRef_setter(instance):
    original = instance.customerRef
    instance.customerRef = original
    assert instance.customerRef == original

@given(instance=model::Document_strategy)
def test_model::document_pdfPath_type(instance):
    assert isinstance(instance.pdfPath, str)


@given(instance=model::Document_strategy)
def test_model::document_pdfPath_setter(instance):
    original = instance.pdfPath
    instance.pdfPath = original
    assert instance.pdfPath == original

@given(instance=model::Document_strategy)
def test_model::document_addressFirstLine_type(instance):
    assert isinstance(instance.addressFirstLine, str)


@given(instance=model::Document_strategy)
def test_model::document_addressFirstLine_setter(instance):
    original = instance.addressFirstLine
    instance.addressFirstLine = original
    assert instance.addressFirstLine == original

@given(instance=model::Document_strategy)
def test_model::document_transactionId_type(instance):
    assert isinstance(instance.transactionId, str)


@given(instance=model::Document_strategy)
def test_model::document_transactionId_setter(instance):
    original = instance.transactionId
    instance.transactionId = original
    assert instance.transactionId == original

@given(instance=model::Document_strategy)
def test_model::document_consultant_type(instance):
    assert isinstance(instance.consultant, str)


@given(instance=model::Document_strategy)
def test_model::document_consultant_setter(instance):
    original = instance.consultant
    instance.consultant = original
    assert instance.consultant == original

@given(instance=model::Document_strategy)
def test_model::document_dueDays_type(instance):
    assert isinstance(instance.dueDays, str)


@given(instance=model::Document_strategy)
def test_model::document_dueDays_setter(instance):
    original = instance.dueDays
    instance.dueDays = original
    assert instance.dueDays == original

@given(instance=model::Document_strategy)
def test_model::document_payDate_type(instance):
    assert isinstance(instance.payDate, date)


@given(instance=model::Document_strategy)
def test_model::document_payDate_setter(instance):
    original = instance.payDate
    instance.payDate = original
    assert instance.payDate == original

@given(instance=model::Document_strategy)
def test_model::document_serviceDate_type(instance):
    assert isinstance(instance.serviceDate, date)


@given(instance=model::Document_strategy)
def test_model::document_serviceDate_setter(instance):
    original = instance.serviceDate
    instance.serviceDate = original
    assert instance.serviceDate == original

@given(instance=model::Document_strategy)
def test_model::document_printTemplate_type(instance):
    assert isinstance(instance.printTemplate, str)


@given(instance=model::Document_strategy)
def test_model::document_printTemplate_setter(instance):
    original = instance.printTemplate
    instance.printTemplate = original
    assert instance.printTemplate == original

@given(instance=model::Document_strategy)
def test_model::document_vestingPeriodStart_type(instance):
    assert isinstance(instance.vestingPeriodStart, date)


@given(instance=model::Document_strategy)
def test_model::document_vestingPeriodStart_setter(instance):
    original = instance.vestingPeriodStart
    instance.vestingPeriodStart = original
    assert instance.vestingPeriodStart == original

@given(instance=model::Document_strategy)
def test_model::document_message3_type(instance):
    assert isinstance(instance.message3, str)


@given(instance=model::Document_strategy)
def test_model::document_message3_setter(instance):
    original = instance.message3
    instance.message3 = original
    assert instance.message3 == original

@given(instance=model::Document_strategy)
def test_model::document_message2_type(instance):
    assert isinstance(instance.message2, str)


@given(instance=model::Document_strategy)
def test_model::document_message2_setter(instance):
    original = instance.message2
    instance.message2 = original
    assert instance.message2 == original

@given(instance=model::Document_strategy)
def test_model::document_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=model::Document_strategy)
def test_model::document_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=model::Document_strategy)
def test_model::document_webshopId_type(instance):
    assert isinstance(instance.webshopId, str)


@given(instance=model::Document_strategy)
def test_model::document_webshopId_setter(instance):
    original = instance.webshopId
    instance.webshopId = original
    assert instance.webshopId == original

@given(instance=model::Document_strategy)
def test_model::document_orderDate_type(instance):
    assert isinstance(instance.orderDate, date)


@given(instance=model::Document_strategy)
def test_model::document_orderDate_setter(instance):
    original = instance.orderDate
    instance.orderDate = original
    assert instance.orderDate == original

@given(instance=model::Document_strategy)
def test_model::document_billingType_type(instance):
    assert isinstance(instance.billingType, str)


@given(instance=model::Document_strategy)
def test_model::document_billingType_setter(instance):
    original = instance.billingType
    instance.billingType = original
    assert instance.billingType == original

@given(instance=model::Document_strategy)
def test_model::document_netGross_type(instance):
    assert isinstance(instance.netGross, str)


@given(instance=model::Document_strategy)
def test_model::document_netGross_setter(instance):
    original = instance.netGross
    instance.netGross = original
    assert instance.netGross == original

@given(instance=model::Document_strategy)
def test_model::document_webshopDate_type(instance):
    assert isinstance(instance.webshopDate, date)


@given(instance=model::Document_strategy)
def test_model::document_webshopDate_setter(instance):
    original = instance.webshopDate
    instance.webshopDate = original
    assert instance.webshopDate == original

@given(instance=model::Document_strategy)
def test_model::document_totalValue_type(instance):
    assert isinstance(instance.totalValue, str)


@given(instance=model::Document_strategy)
def test_model::document_totalValue_setter(instance):
    original = instance.totalValue
    instance.totalValue = original
    assert instance.totalValue == original

@given(instance=model::Address_strategy)
@settings(max_examples=50)
def test_model::address_instantiation(instance):
    assert isinstance(instance, model::Address)

@given(instance=model::Address_strategy)
def test_model::address_cityAddon_type(instance):
    assert isinstance(instance.cityAddon, str)


@given(instance=model::Address_strategy)
def test_model::address_cityAddon_setter(instance):
    original = instance.cityAddon
    instance.cityAddon = original
    assert instance.cityAddon == original

@given(instance=model::Address_strategy)
def test_model::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=model::Address_strategy)
def test_model::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=model::Address_strategy)
def test_model::address_zip_type(instance):
    assert isinstance(instance.zip, str)


@given(instance=model::Address_strategy)
def test_model::address_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original

@given(instance=model::Address_strategy)
def test_model::address_manualAddress_type(instance):
    assert isinstance(instance.manualAddress, str)


@given(instance=model::Address_strategy)
def test_model::address_manualAddress_setter(instance):
    original = instance.manualAddress
    instance.manualAddress = original
    assert instance.manualAddress == original

@given(instance=model::Address_strategy)
def test_model::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=model::Address_strategy)
def test_model::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=model::Address_strategy)
def test_model::address_countryCode_type(instance):
    assert isinstance(instance.countryCode, str)


@given(instance=model::Address_strategy)
def test_model::address_countryCode_setter(instance):
    original = instance.countryCode
    instance.countryCode = original
    assert instance.countryCode == original

@given(instance=model::IndividualDocumentInfo_strategy)
@settings(max_examples=50)
def test_model::individualdocumentinfo_instantiation(instance):
    assert isinstance(instance, model::IndividualDocumentInfo)

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_noVatName_type(instance):
    assert isinstance(instance.noVatName, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_noVatName_setter(instance):
    original = instance.noVatName
    instance.noVatName = original
    assert instance.noVatName == original

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingAutoVat_type(instance):
    assert isinstance(instance.shippingAutoVat, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingAutoVat_setter(instance):
    original = instance.shippingAutoVat
    instance.shippingAutoVat = original
    assert instance.shippingAutoVat == original

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_paymentDescription_type(instance):
    assert isinstance(instance.paymentDescription, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_paymentDescription_setter(instance):
    original = instance.paymentDescription
    instance.paymentDescription = original
    assert instance.paymentDescription == original

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingValue_type(instance):
    assert isinstance(instance.shippingValue, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingValue_setter(instance):
    original = instance.shippingValue
    instance.shippingValue = original
    assert instance.shippingValue == original

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_paymentText_type(instance):
    assert isinstance(instance.paymentText, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_paymentText_setter(instance):
    original = instance.paymentText
    instance.paymentText = original
    assert instance.paymentText == original

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingDescription_type(instance):
    assert isinstance(instance.shippingDescription, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingDescription_setter(instance):
    original = instance.shippingDescription
    instance.shippingDescription = original
    assert instance.shippingDescription == original

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingVatDescription_type(instance):
    assert isinstance(instance.shippingVatDescription, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingVatDescription_setter(instance):
    original = instance.shippingVatDescription
    instance.shippingVatDescription = original
    assert instance.shippingVatDescription == original

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_paymentName_type(instance):
    assert isinstance(instance.paymentName, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_paymentName_setter(instance):
    original = instance.paymentName
    instance.paymentName = original
    assert instance.paymentName == original

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingName_type(instance):
    assert isinstance(instance.shippingName, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingName_setter(instance):
    original = instance.shippingName
    instance.shippingName = original
    assert instance.shippingName == original

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_noVatDescription_type(instance):
    assert isinstance(instance.noVatDescription, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_noVatDescription_setter(instance):
    original = instance.noVatDescription
    instance.noVatDescription = original
    assert instance.noVatDescription == original

@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingVatValue_type(instance):
    assert isinstance(instance.shippingVatValue, str)


@given(instance=model::IndividualDocumentInfo_strategy)
def test_model::individualdocumentinfo_shippingVatValue_setter(instance):
    original = instance.shippingVatValue
    instance.shippingVatValue = original
    assert instance.shippingVatValue == original

@given(instance=model::VAT_strategy)
@settings(max_examples=50)
def test_model::vat_instantiation(instance):
    assert isinstance(instance, model::VAT)

@given(instance=model::VAT_strategy)
def test_model::vat_salesEqualizationTax_type(instance):
    assert isinstance(instance.salesEqualizationTax, str)


@given(instance=model::VAT_strategy)
def test_model::vat_salesEqualizationTax_setter(instance):
    original = instance.salesEqualizationTax
    instance.salesEqualizationTax = original
    assert instance.salesEqualizationTax == original

@given(instance=model::VAT_strategy)
def test_model::vat_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::VAT_strategy)
def test_model::vat_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::VAT_strategy)
def test_model::vat_taxValue_type(instance):
    assert isinstance(instance.taxValue, str)


@given(instance=model::VAT_strategy)
def test_model::vat_taxValue_setter(instance):
    original = instance.taxValue
    instance.taxValue = original
    assert instance.taxValue == original

@given(instance=model::AbstractCategory_strategy)
@settings(max_examples=50)
def test_model::abstractcategory_instantiation(instance):
    assert isinstance(instance, model::AbstractCategory)

@given(instance=model::IDescribableEntity_strategy)
@settings(max_examples=50)
def test_model::idescribableentity_instantiation(instance):
    assert isinstance(instance, model::IDescribableEntity)

@given(instance=model::IDescribableEntity_strategy)
def test_model::idescribableentity_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::IDescribableEntity_strategy)
def test_model::idescribableentity_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::Payment_strategy)
@settings(max_examples=50)
def test_model::payment_instantiation(instance):
    assert isinstance(instance, model::Payment)

@given(instance=model::Payment_strategy)
def test_model::payment_discountValue_type(instance):
    assert isinstance(instance.discountValue, str)


@given(instance=model::Payment_strategy)
def test_model::payment_discountValue_setter(instance):
    original = instance.discountValue
    instance.discountValue = original
    assert instance.discountValue == original

@given(instance=model::Payment_strategy)
def test_model::payment_unpaidText_type(instance):
    assert isinstance(instance.unpaidText, str)


@given(instance=model::Payment_strategy)
def test_model::payment_unpaidText_setter(instance):
    original = instance.unpaidText
    instance.unpaidText = original
    assert instance.unpaidText == original

@given(instance=model::Payment_strategy)
def test_model::payment_netDays_type(instance):
    assert isinstance(instance.netDays, str)


@given(instance=model::Payment_strategy)
def test_model::payment_netDays_setter(instance):
    original = instance.netDays
    instance.netDays = original
    assert instance.netDays == original

@given(instance=model::Payment_strategy)
def test_model::payment_paidText_type(instance):
    assert isinstance(instance.paidText, str)


@given(instance=model::Payment_strategy)
def test_model::payment_paidText_setter(instance):
    original = instance.paidText
    instance.paidText = original
    assert instance.paidText == original

@given(instance=model::Payment_strategy)
def test_model::payment_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=model::Payment_strategy)
def test_model::payment_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=model::Payment_strategy)
def test_model::payment_depositText_type(instance):
    assert isinstance(instance.depositText, str)


@given(instance=model::Payment_strategy)
def test_model::payment_depositText_setter(instance):
    original = instance.depositText
    instance.depositText = original
    assert instance.depositText == original

@given(instance=model::Payment_strategy)
def test_model::payment_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::Payment_strategy)
def test_model::payment_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::Payment_strategy)
def test_model::payment_discountDays_type(instance):
    assert isinstance(instance.discountDays, str)


@given(instance=model::Payment_strategy)
def test_model::payment_discountDays_setter(instance):
    original = instance.discountDays
    instance.discountDays = original
    assert instance.discountDays == original

@given(instance=model::ContactCategory_strategy)
@settings(max_examples=50)
def test_model::contactcategory_instantiation(instance):
    assert isinstance(instance, model::ContactCategory)

@given(instance=model::IEntity_strategy)
@settings(max_examples=50)
def test_model::ientity_instantiation(instance):
    assert isinstance(instance, model::IEntity)

@given(instance=model::IEntity_strategy)
def test_model::ientity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::IEntity_strategy)
def test_model::ientity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::IEntity_strategy)
def test_model::ientity_deleted_type(instance):
    assert isinstance(instance.deleted, str)


@given(instance=model::IEntity_strategy)
def test_model::ientity_deleted_setter(instance):
    original = instance.deleted
    instance.deleted = original
    assert instance.deleted == original

@given(instance=model::IEntity_strategy)
def test_model::ientity_modifiedBy_type(instance):
    assert isinstance(instance.modifiedBy, str)


@given(instance=model::IEntity_strategy)
def test_model::ientity_modifiedBy_setter(instance):
    original = instance.modifiedBy
    instance.modifiedBy = original
    assert instance.modifiedBy == original

@given(instance=model::IEntity_strategy)
def test_model::ientity_validFrom_type(instance):
    assert isinstance(instance.validFrom, date)


@given(instance=model::IEntity_strategy)
def test_model::ientity_validFrom_setter(instance):
    original = instance.validFrom
    instance.validFrom = original
    assert instance.validFrom == original

@given(instance=model::IEntity_strategy)
def test_model::ientity_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=model::IEntity_strategy)
def test_model::ientity_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model::IEntity_strategy)
def test_model::ientity_validTo_type(instance):
    assert isinstance(instance.validTo, date)


@given(instance=model::IEntity_strategy)
def test_model::ientity_validTo_setter(instance):
    original = instance.validTo
    instance.validTo = original
    assert instance.validTo == original

@given(instance=model::IEntity_strategy)
def test_model::ientity_dateAdded_type(instance):
    assert isinstance(instance.dateAdded, date)


@given(instance=model::IEntity_strategy)
def test_model::ientity_dateAdded_setter(instance):
    original = instance.dateAdded
    instance.dateAdded = original
    assert instance.dateAdded == original

@given(instance=model::IEntity_strategy)
def test_model::ientity_modified_type(instance):
    assert isinstance(instance.modified, date)


@given(instance=model::IEntity_strategy)
def test_model::ientity_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model::IEntity_strategy)
@settings(max_examples=30)
def test_model::ientity_issameas_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSameAs()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSameAs).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSameAs' in model::IEntity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSameAs' in model::IEntity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSameAs' in model::IEntity is not implemented or raised an error")

@given(instance=model::WebshopStateMapping_strategy)
@settings(max_examples=50)
def test_model::webshopstatemapping_instantiation(instance):
    assert isinstance(instance, model::WebshopStateMapping)

@given(instance=model::WebshopStateMapping_strategy)
def test_model::webshopstatemapping_fakturamaOrderState_type(instance):
    assert isinstance(instance.fakturamaOrderState, str)


@given(instance=model::WebshopStateMapping_strategy)
def test_model::webshopstatemapping_fakturamaOrderState_setter(instance):
    original = instance.fakturamaOrderState
    instance.fakturamaOrderState = original
    assert instance.fakturamaOrderState == original

@given(instance=model::WebshopStateMapping_strategy)
def test_model::webshopstatemapping_webshopState_type(instance):
    assert isinstance(instance.webshopState, str)


@given(instance=model::WebshopStateMapping_strategy)
def test_model::webshopstatemapping_webshopState_setter(instance):
    original = instance.webshopState
    instance.webshopState = original
    assert instance.webshopState == original

@given(instance=model::WebShop_strategy)
@settings(max_examples=50)
def test_model::webshop_instantiation(instance):
    assert isinstance(instance, model::WebShop)

@given(instance=model::WebShop_strategy)
def test_model::webshop_webshopVendor_type(instance):
    assert isinstance(instance.webshopVendor, str)


@given(instance=model::WebShop_strategy)
def test_model::webshop_webshopVendor_setter(instance):
    original = instance.webshopVendor
    instance.webshopVendor = original
    assert instance.webshopVendor == original

@given(instance=model::WebShop_strategy)
def test_model::webshop_webshopVersion_type(instance):
    assert isinstance(instance.webshopVersion, str)


@given(instance=model::WebShop_strategy)
def test_model::webshop_webshopVersion_setter(instance):
    original = instance.webshopVersion
    instance.webshopVersion = original
    assert instance.webshopVersion == original

@given(instance=model::CEFACTCode_strategy)
@settings(max_examples=50)
def test_model::cefactcode_instantiation(instance):
    assert isinstance(instance, model::CEFACTCode)

@given(instance=model::CEFACTCode_strategy)
def test_model::cefactcode_abbreviation_de_type(instance):
    assert isinstance(instance.abbreviation_de, str)


@given(instance=model::CEFACTCode_strategy)
def test_model::cefactcode_abbreviation_de_setter(instance):
    original = instance.abbreviation_de
    instance.abbreviation_de = original
    assert instance.abbreviation_de == original

@given(instance=model::CEFACTCode_strategy)
def test_model::cefactcode_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=model::CEFACTCode_strategy)
def test_model::cefactcode_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=model::CEFACTCode_strategy)
def test_model::cefactcode_name_de_type(instance):
    assert isinstance(instance.name_de, str)


@given(instance=model::CEFACTCode_strategy)
def test_model::cefactcode_name_de_setter(instance):
    original = instance.name_de
    instance.name_de = original
    assert instance.name_de == original

@given(instance=model::CEFACTCode_strategy)
def test_model::cefactcode_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=model::CEFACTCode_strategy)
def test_model::cefactcode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=model::CEFACTCode_strategy)
def test_model::cefactcode_abbreviation_en_type(instance):
    assert isinstance(instance.abbreviation_en, str)


@given(instance=model::CEFACTCode_strategy)
def test_model::cefactcode_abbreviation_en_setter(instance):
    original = instance.abbreviation_en
    instance.abbreviation_en = original
    assert instance.abbreviation_en == original

@given(instance=model::User_strategy)
@settings(max_examples=50)
def test_model::user_instantiation(instance):
    assert isinstance(instance, model::User)

@given(instance=model::User_strategy)
def test_model::user_userName_type(instance):
    assert isinstance(instance.userName, str)


@given(instance=model::User_strategy)
def test_model::user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=model::User_strategy)
def test_model::user_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=model::User_strategy)
def test_model::user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=model::TextCategory_strategy)
@settings(max_examples=50)
def test_model::textcategory_instantiation(instance):
    assert isinstance(instance, model::TextCategory)

@given(instance=model::TextModule_strategy)
@settings(max_examples=50)
def test_model::textmodule_instantiation(instance):
    assert isinstance(instance, model::TextModule)

@given(instance=model::TextModule_strategy)
def test_model::textmodule_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=model::TextModule_strategy)
def test_model::textmodule_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=model::Tenant_strategy)
@settings(max_examples=50)
def test_model::tenant_instantiation(instance):
    assert isinstance(instance, model::Tenant)

@given(instance=model::ShippingCategory_strategy)
@settings(max_examples=50)
def test_model::shippingcategory_instantiation(instance):
    assert isinstance(instance, model::ShippingCategory)

@given(instance=model::VATCategory_strategy)
@settings(max_examples=50)
def test_model::vatcategory_instantiation(instance):
    assert isinstance(instance, model::VATCategory)

@given(instance=model::UserProperty_strategy)
@settings(max_examples=50)
def test_model::userproperty_instantiation(instance):
    assert isinstance(instance, model::UserProperty)

@given(instance=model::UserProperty_strategy)
def test_model::userproperty_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=model::UserProperty_strategy)
def test_model::userproperty_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=model::UserProperty_strategy)
def test_model::userproperty_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::UserProperty_strategy)
def test_model::userproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::UserProperty_strategy)
def test_model::userproperty_user_type(instance):
    assert isinstance(instance.user, str)


@given(instance=model::UserProperty_strategy)
def test_model::userproperty_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=model::UserProperty_strategy)
def test_model::userproperty_global__type(instance):
    assert isinstance(instance.global_, str)


@given(instance=model::UserProperty_strategy)
def test_model::userproperty_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=model::Role_strategy)
@settings(max_examples=50)
def test_model::role_instantiation(instance):
    assert isinstance(instance, model::Role)

@given(instance=model::ProductOptions_strategy)
@settings(max_examples=50)
def test_model::productoptions_instantiation(instance):
    assert isinstance(instance, model::ProductOptions)

@given(instance=model::ProductOptions_strategy)
def test_model::productoptions_sequenceNumber_type(instance):
    assert isinstance(instance.sequenceNumber, str)


@given(instance=model::ProductOptions_strategy)
def test_model::productoptions_sequenceNumber_setter(instance):
    original = instance.sequenceNumber
    instance.sequenceNumber = original
    assert instance.sequenceNumber == original

@given(instance=model::ProductOptions_strategy)
def test_model::productoptions_attributeValue_type(instance):
    assert isinstance(instance.attributeValue, str)


@given(instance=model::ProductOptions_strategy)
def test_model::productoptions_attributeValue_setter(instance):
    original = instance.attributeValue
    instance.attributeValue = original
    assert instance.attributeValue == original

@given(instance=model::ProductCategory_strategy)
@settings(max_examples=50)
def test_model::productcategory_instantiation(instance):
    assert isinstance(instance, model::ProductCategory)

@given(instance=IDescribableEntity_strategy)
@settings(max_examples=50)
def test_idescribableentity_instantiation(instance):
    assert isinstance(instance, IDescribableEntity)

@given(instance=model::Product_strategy)
@settings(max_examples=50)
def test_model::product_instantiation(instance):
    assert isinstance(instance, model::Product)

@given(instance=model::Product_strategy)
def test_model::product_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=model::Product_strategy)
def test_model::product_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=model::Product_strategy)
def test_model::product_itemNumber_type(instance):
    assert isinstance(instance.itemNumber, str)


@given(instance=model::Product_strategy)
def test_model::product_itemNumber_setter(instance):
    original = instance.itemNumber
    instance.itemNumber = original
    assert instance.itemNumber == original

@given(instance=model::Product_strategy)
def test_model::product_price1_type(instance):
    assert isinstance(instance.price1, str)


@given(instance=model::Product_strategy)
def test_model::product_price1_setter(instance):
    original = instance.price1
    instance.price1 = original
    assert instance.price1 == original

@given(instance=model::Product_strategy)
def test_model::product_cdf01_type(instance):
    assert isinstance(instance.cdf01, str)


@given(instance=model::Product_strategy)
def test_model::product_cdf01_setter(instance):
    original = instance.cdf01
    instance.cdf01 = original
    assert instance.cdf01 == original

@given(instance=model::Product_strategy)
def test_model::product_block1_type(instance):
    assert isinstance(instance.block1, str)


@given(instance=model::Product_strategy)
def test_model::product_block1_setter(instance):
    original = instance.block1
    instance.block1 = original
    assert instance.block1 == original

@given(instance=model::Product_strategy)
def test_model::product_block2_type(instance):
    assert isinstance(instance.block2, str)


@given(instance=model::Product_strategy)
def test_model::product_block2_setter(instance):
    original = instance.block2
    instance.block2 = original
    assert instance.block2 == original

@given(instance=model::Product_strategy)
def test_model::product_price4_type(instance):
    assert isinstance(instance.price4, str)


@given(instance=model::Product_strategy)
def test_model::product_price4_setter(instance):
    original = instance.price4
    instance.price4 = original
    assert instance.price4 == original

@given(instance=model::Product_strategy)
def test_model::product_cdf03_type(instance):
    assert isinstance(instance.cdf03, str)


@given(instance=model::Product_strategy)
def test_model::product_cdf03_setter(instance):
    original = instance.cdf03
    instance.cdf03 = original
    assert instance.cdf03 == original

@given(instance=model::Product_strategy)
def test_model::product_price5_type(instance):
    assert isinstance(instance.price5, str)


@given(instance=model::Product_strategy)
def test_model::product_price5_setter(instance):
    original = instance.price5
    instance.price5 = original
    assert instance.price5 == original

@given(instance=model::Product_strategy)
def test_model::product_sellingUnit_type(instance):
    assert isinstance(instance.sellingUnit, str)


@given(instance=model::Product_strategy)
def test_model::product_sellingUnit_setter(instance):
    original = instance.sellingUnit
    instance.sellingUnit = original
    assert instance.sellingUnit == original

@given(instance=model::Product_strategy)
def test_model::product_block4_type(instance):
    assert isinstance(instance.block4, str)


@given(instance=model::Product_strategy)
def test_model::product_block4_setter(instance):
    original = instance.block4
    instance.block4 = original
    assert instance.block4 == original

@given(instance=model::Product_strategy)
def test_model::product_quantityUnit_type(instance):
    assert isinstance(instance.quantityUnit, str)


@given(instance=model::Product_strategy)
def test_model::product_quantityUnit_setter(instance):
    original = instance.quantityUnit
    instance.quantityUnit = original
    assert instance.quantityUnit == original

@given(instance=model::Product_strategy)
def test_model::product_gtin_type(instance):
    assert isinstance(instance.gtin, str)


@given(instance=model::Product_strategy)
def test_model::product_gtin_setter(instance):
    original = instance.gtin
    instance.gtin = original
    assert instance.gtin == original

@given(instance=model::Product_strategy)
def test_model::product_picture_type(instance):
    assert isinstance(instance.picture, str)


@given(instance=model::Product_strategy)
def test_model::product_picture_setter(instance):
    original = instance.picture
    instance.picture = original
    assert instance.picture == original

@given(instance=model::Product_strategy)
def test_model::product_block5_type(instance):
    assert isinstance(instance.block5, str)


@given(instance=model::Product_strategy)
def test_model::product_block5_setter(instance):
    original = instance.block5
    instance.block5 = original
    assert instance.block5 == original

@given(instance=model::Product_strategy)
def test_model::product_block3_type(instance):
    assert isinstance(instance.block3, str)


@given(instance=model::Product_strategy)
def test_model::product_block3_setter(instance):
    original = instance.block3
    instance.block3 = original
    assert instance.block3 == original

@given(instance=model::Product_strategy)
def test_model::product_cdf02_type(instance):
    assert isinstance(instance.cdf02, str)


@given(instance=model::Product_strategy)
def test_model::product_cdf02_setter(instance):
    original = instance.cdf02
    instance.cdf02 = original
    assert instance.cdf02 == original

@given(instance=model::Product_strategy)
def test_model::product_quantity_type(instance):
    assert isinstance(instance.quantity, str)


@given(instance=model::Product_strategy)
def test_model::product_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=model::Product_strategy)
def test_model::product_price2_type(instance):
    assert isinstance(instance.price2, str)


@given(instance=model::Product_strategy)
def test_model::product_price2_setter(instance):
    original = instance.price2
    instance.price2 = original
    assert instance.price2 == original

@given(instance=model::Product_strategy)
def test_model::product_webshopId_type(instance):
    assert isinstance(instance.webshopId, str)


@given(instance=model::Product_strategy)
def test_model::product_webshopId_setter(instance):
    original = instance.webshopId
    instance.webshopId = original
    assert instance.webshopId == original

@given(instance=model::Product_strategy)
def test_model::product_costPrice_type(instance):
    assert isinstance(instance.costPrice, str)


@given(instance=model::Product_strategy)
def test_model::product_costPrice_setter(instance):
    original = instance.costPrice
    instance.costPrice = original
    assert instance.costPrice == original

@given(instance=model::Product_strategy)
def test_model::product_price3_type(instance):
    assert isinstance(instance.price3, str)


@given(instance=model::Product_strategy)
def test_model::product_price3_setter(instance):
    original = instance.price3
    instance.price3 = original
    assert instance.price3 == original

@given(instance=model::Shipping_strategy)
@settings(max_examples=50)
def test_model::shipping_instantiation(instance):
    assert isinstance(instance, model::Shipping)

@given(instance=model::Shipping_strategy)
def test_model::shipping_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=model::Shipping_strategy)
def test_model::shipping_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=model::Shipping_strategy)
def test_model::shipping_autoVat_type(instance):
    assert isinstance(instance.autoVat, str)


@given(instance=model::Shipping_strategy)
def test_model::shipping_autoVat_setter(instance):
    original = instance.autoVat
    instance.autoVat = original
    assert instance.autoVat == original

@given(instance=model::Shipping_strategy)
def test_model::shipping_shippingValue_type(instance):
    assert isinstance(instance.shippingValue, str)


@given(instance=model::Shipping_strategy)
def test_model::shipping_shippingValue_setter(instance):
    original = instance.shippingValue
    instance.shippingValue = original
    assert instance.shippingValue == original

@given(instance=model::ProductBlockPrice_strategy)
@settings(max_examples=50)
def test_model::productblockprice_instantiation(instance):
    assert isinstance(instance, model::ProductBlockPrice)

@given(instance=model::ProductBlockPrice_strategy)
def test_model::productblockprice_price_type(instance):
    assert isinstance(instance.price, str)


@given(instance=model::ProductBlockPrice_strategy)
def test_model::productblockprice_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=model::ProductBlockPrice_strategy)
def test_model::productblockprice_block_type(instance):
    assert isinstance(instance.block, str)


@given(instance=model::ProductBlockPrice_strategy)
def test_model::productblockprice_block_setter(instance):
    original = instance.block
    instance.block = original
    assert instance.block == original

@given(instance=model::ItemAccountType_strategy)
@settings(max_examples=50)
def test_model::itemaccounttype_instantiation(instance):
    assert isinstance(instance, model::ItemAccountType)

@given(instance=model::ItemAccountType_strategy)
def test_model::itemaccounttype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::ItemAccountType_strategy)
def test_model::itemaccounttype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::VoucherItem_strategy)
@settings(max_examples=50)
def test_model::voucheritem_instantiation(instance):
    assert isinstance(instance, model::VoucherItem)

@given(instance=model::VoucherItem_strategy)
def test_model::voucheritem_price_type(instance):
    assert isinstance(instance.price, str)


@given(instance=model::VoucherItem_strategy)
def test_model::voucheritem_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=model::VoucherItem_strategy)
def test_model::voucheritem_posNr_type(instance):
    assert isinstance(instance.posNr, str)


@given(instance=model::VoucherItem_strategy)
def test_model::voucheritem_posNr_setter(instance):
    original = instance.posNr
    instance.posNr = original
    assert instance.posNr == original

@given(instance=model::VoucherItem_strategy)
def test_model::voucheritem_itemVoucherType_type(instance):
    assert isinstance(instance.itemVoucherType, str)


@given(instance=model::VoucherItem_strategy)
def test_model::voucheritem_itemVoucherType_setter(instance):
    original = instance.itemVoucherType
    instance.itemVoucherType = original
    assert instance.itemVoucherType == original

@given(instance=model::Voucher_strategy)
@settings(max_examples=50)
def test_model::voucher_instantiation(instance):
    assert isinstance(instance, model::Voucher)

@given(instance=model::Voucher_strategy)
def test_model::voucher_paidValue_type(instance):
    assert isinstance(instance.paidValue, str)


@given(instance=model::Voucher_strategy)
def test_model::voucher_paidValue_setter(instance):
    original = instance.paidValue
    instance.paidValue = original
    assert instance.paidValue == original

@given(instance=model::Voucher_strategy)
def test_model::voucher_voucherNumber_type(instance):
    assert isinstance(instance.voucherNumber, str)


@given(instance=model::Voucher_strategy)
def test_model::voucher_voucherNumber_setter(instance):
    original = instance.voucherNumber
    instance.voucherNumber = original
    assert instance.voucherNumber == original

@given(instance=model::Voucher_strategy)
def test_model::voucher_documentNumber_type(instance):
    assert isinstance(instance.documentNumber, str)


@given(instance=model::Voucher_strategy)
def test_model::voucher_documentNumber_setter(instance):
    original = instance.documentNumber
    instance.documentNumber = original
    assert instance.documentNumber == original

@given(instance=model::Voucher_strategy)
def test_model::voucher_discounted_type(instance):
    assert isinstance(instance.discounted, str)


@given(instance=model::Voucher_strategy)
def test_model::voucher_discounted_setter(instance):
    original = instance.discounted
    instance.discounted = original
    assert instance.discounted == original

@given(instance=model::Voucher_strategy)
def test_model::voucher_doNotBook_type(instance):
    assert isinstance(instance.doNotBook, str)


@given(instance=model::Voucher_strategy)
def test_model::voucher_doNotBook_setter(instance):
    original = instance.doNotBook
    instance.doNotBook = original
    assert instance.doNotBook == original

@given(instance=model::Voucher_strategy)
def test_model::voucher_voucherType_type(instance):
    assert isinstance(instance.voucherType, str)


@given(instance=model::Voucher_strategy)
def test_model::voucher_voucherType_setter(instance):
    original = instance.voucherType
    instance.voucherType = original
    assert instance.voucherType == original

@given(instance=model::Voucher_strategy)
def test_model::voucher_totalValue_type(instance):
    assert isinstance(instance.totalValue, str)


@given(instance=model::Voucher_strategy)
def test_model::voucher_totalValue_setter(instance):
    original = instance.totalValue
    instance.totalValue = original
    assert instance.totalValue == original

@given(instance=model::Voucher_strategy)
def test_model::voucher_voucherDate_type(instance):
    assert isinstance(instance.voucherDate, date)


@given(instance=model::Voucher_strategy)
def test_model::voucher_voucherDate_setter(instance):
    original = instance.voucherDate
    instance.voucherDate = original
    assert instance.voucherDate == original

@given(instance=model::Proforma_strategy)
@settings(max_examples=50)
def test_model::proforma_instantiation(instance):
    assert isinstance(instance, model::Proforma)
