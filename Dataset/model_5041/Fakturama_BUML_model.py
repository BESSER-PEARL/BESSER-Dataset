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
ShippingVatType: Enumeration = Enumeration(
    name="ShippingVatType",
    literals={
            EnumerationLiteral(name="SHIPPINGVATFIX"),
			EnumerationLiteral(name="SHIPPINGVATGROSS"),
			EnumerationLiteral(name="SHIPPINGVATNET")
    }
)

BillingType: Enumeration = Enumeration(
    name="BillingType",
    literals={
            EnumerationLiteral(name="INVOICE"),
			EnumerationLiteral(name="LETTER"),
			EnumerationLiteral(name="OFFER"),
			EnumerationLiteral(name="ORDER"),
			EnumerationLiteral(name="CONFIRMATION"),
			EnumerationLiteral(name="DELIVERY"),
			EnumerationLiteral(name="CREDIT"),
			EnumerationLiteral(name="DUNNING"),
			EnumerationLiteral(name="PROFORMA"),
			EnumerationLiteral(name="NONE")
    }
)

ContactType: Enumeration = Enumeration(
    name="ContactType",
    literals={
            EnumerationLiteral(name="BILLING"),
			EnumerationLiteral(name="DELIVERY")
    }
)

ItemType: Enumeration = Enumeration(
    name="ItemType",
    literals={
            EnumerationLiteral(name="POSITION"),
			EnumerationLiteral(name="FREETEXT"),
			EnumerationLiteral(name="DELIVERY_PART"),
			EnumerationLiteral(name="SUBTOTAL")
    }
)

ReliabilityType: Enumeration = Enumeration(
    name="ReliabilityType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="POOR"),
			EnumerationLiteral(name="MEDIUM"),
			EnumerationLiteral(name="GOOD")
    }
)

VoucherType: Enumeration = Enumeration(
    name="VoucherType",
    literals={
            EnumerationLiteral(name="RECEIPTVOUCHER"),
			EnumerationLiteral(name="EXPENDITURE")
    }
)

# Classes
model_IEntity = Class(name="model::IEntity", is_abstract=True)
model_IDescribableEntity = Class(name="model::IDescribableEntity", is_abstract=True)
IEntity = Class(name="IEntity")
model_AbstractCategory = Class(name="model::AbstractCategory", is_abstract=True)
model_VoucherCategory = Class(name="model::VoucherCategory")
AbstractCategory = Class(name="AbstractCategory")
model_Address = Class(name="model::Address")
model_Contact = Class(name="model::Contact", is_abstract=True)
model_ContactCategory = Class(name="model::ContactCategory")
model_Payment = Class(name="model::Payment")
model_BankAccount = Class(name="model::BankAccount")
model_Creditor = Class(name="model::Creditor")
Contact = Class(name="Contact")
model_Debitor = Class(name="model::Debitor")
model_Document = Class(name="model::Document", is_abstract=True)
model_IndividualDocumentInfo = Class(name="model::IndividualDocumentInfo")
model_Invoice = Class(name="model::Invoice")
model_DocumentItem = Class(name="model::DocumentItem")
model_VAT = Class(name="model::VAT")
model_Shipping = Class(name="model::Shipping")
model_Product = Class(name="model::Product")
model_ItemListTypeCategory = Class(name="model::ItemListTypeCategory")
Document = Class(name="Document")
model_Order = Class(name="model::Order")
model_Letter = Class(name="model::Letter")
model_Offer = Class(name="model::Offer")
model_Dunning = Class(name="model::Dunning")
model_Credit = Class(name="model::Credit")
model_Delivery = Class(name="model::Delivery")
model_Confirmation = Class(name="model::Confirmation")
model_Proforma = Class(name="model::Proforma")
model_Voucher = Class(name="model::Voucher")
model_VoucherItem = Class(name="model::VoucherItem")
model_ItemAccountType = Class(name="model::ItemAccountType")
IDescribableEntity = Class(name="IDescribableEntity")
model_ProductCategory = Class(name="model::ProductCategory")
model_ProductOptions = Class(name="model::ProductOptions")
model_ProductBlockPrice = Class(name="model::ProductBlockPrice")
model_ShippingCategory = Class(name="model::ShippingCategory")
model_Tenant = Class(name="model::Tenant")
model_TextModule = Class(name="model::TextModule")
model_TextCategory = Class(name="model::TextCategory")
model_User = Class(name="model::User")
model_Role = Class(name="model::Role")
model_UserProperty = Class(name="model::UserProperty")
model_VATCategory = Class(name="model::VATCategory")
model_CEFACTCode = Class(name="model::CEFACTCode")
model_WebShop = Class(name="model::WebShop")
model_WebshopStateMapping = Class(name="model::WebshopStateMapping")

# model_IEntity class attributes and methods
model_IEntity_name: Property = Property(name="name", type=StringType)
model_IEntity_dateAdded: Property = Property(name="dateAdded", type=DateType)
model_IEntity_modifiedBy: Property = Property(name="modifiedBy", type=StringType)
model_IEntity_modified: Property = Property(name="modified", type=DateType)
model_IEntity_id: Property = Property(name="id", type=StringType)
model_IEntity_deleted: Property = Property(name="deleted", type=StringType)
model_IEntity_validFrom: Property = Property(name="validFrom", type=DateType)
model_IEntity_validTo: Property = Property(name="validTo", type=DateType)
model_IEntity_m_isSameAs: Method = Method(name="isSameAs", parameters={}, type=StringType)
model_IEntity.attributes={model_IEntity_validTo, model_IEntity_name, model_IEntity_deleted, model_IEntity_validFrom, model_IEntity_modified, model_IEntity_dateAdded, model_IEntity_modifiedBy, model_IEntity_id}
model_IEntity.methods={model_IEntity_m_isSameAs}

# model_IDescribableEntity class attributes and methods
model_IDescribableEntity_description: Property = Property(name="description", type=StringType)
model_IDescribableEntity.attributes={model_IDescribableEntity_description}

# IEntity class attributes and methods

# model_AbstractCategory class attributes and methods

# model_VoucherCategory class attributes and methods

# AbstractCategory class attributes and methods

# model_Address class attributes and methods
model_Address_street: Property = Property(name="street", type=StringType)
model_Address_cityAddon: Property = Property(name="cityAddon", type=StringType)
model_Address_city: Property = Property(name="city", type=StringType)
model_Address_zip: Property = Property(name="zip", type=StringType)
model_Address_countryCode: Property = Property(name="countryCode", type=StringType)
model_Address_manualAddress: Property = Property(name="manualAddress", type=StringType)
model_Address.attributes={model_Address_zip, model_Address_street, model_Address_city, model_Address_manualAddress, model_Address_cityAddon, model_Address_countryCode}

# model_Contact class attributes and methods
model_Contact_mandateReference: Property = Property(name="mandateReference", type=StringType)
model_Contact_customerNumber: Property = Property(name="customerNumber", type=StringType)
model_Contact_title: Property = Property(name="title", type=StringType)
model_Contact_firstName: Property = Property(name="firstName", type=StringType)
model_Contact_gender: Property = Property(name="gender", type=StringType)
model_Contact_company: Property = Property(name="company", type=StringType)
model_Contact_birthday: Property = Property(name="birthday", type=DateType)
model_Contact_email: Property = Property(name="email", type=StringType)
model_Contact_mobile: Property = Property(name="mobile", type=StringType)
model_Contact_phone: Property = Property(name="phone", type=StringType)
model_Contact_fax: Property = Property(name="fax", type=StringType)
model_Contact_discount: Property = Property(name="discount", type=StringType)
model_Contact_note: Property = Property(name="note", type=StringType)
model_Contact_reliability: Property = Property(name="reliability", type=StringType)
model_Contact_useNetGross: Property = Property(name="useNetGross", type=StringType)
model_Contact_vatNumber: Property = Property(name="vatNumber", type=StringType)
model_Contact_vatNumberValid: Property = Property(name="vatNumberValid", type=StringType)
model_Contact_website: Property = Property(name="website", type=StringType)
model_Contact_webshopName: Property = Property(name="webshopName", type=StringType)
model_Contact_supplierNumber: Property = Property(name="supplierNumber", type=StringType)
model_Contact_gln: Property = Property(name="gln", type=StringType)
model_Contact_contactType: Property = Property(name="contactType", type=StringType)
model_Contact_useSalesEqualizationTax: Property = Property(name="useSalesEqualizationTax", type=StringType)
model_Contact.attributes={model_Contact_contactType, model_Contact_supplierNumber, model_Contact_reliability, model_Contact_firstName, model_Contact_discount, model_Contact_webshopName, model_Contact_useNetGross, model_Contact_mandateReference, model_Contact_gln, model_Contact_birthday, model_Contact_gender, model_Contact_note, model_Contact_vatNumber, model_Contact_customerNumber, model_Contact_mobile, model_Contact_useSalesEqualizationTax, model_Contact_company, model_Contact_email, model_Contact_vatNumberValid, model_Contact_fax, model_Contact_title, model_Contact_website, model_Contact_phone}

# model_ContactCategory class attributes and methods

# model_Payment class attributes and methods
model_Payment_description: Property = Property(name="description", type=StringType)
model_Payment_discountDays: Property = Property(name="discountDays", type=StringType)
model_Payment_discountValue: Property = Property(name="discountValue", type=StringType)
model_Payment_netDays: Property = Property(name="netDays", type=StringType)
model_Payment_paidText: Property = Property(name="paidText", type=StringType)
model_Payment_unpaidText: Property = Property(name="unpaidText", type=StringType)
model_Payment_depositText: Property = Property(name="depositText", type=StringType)
model_Payment_code: Property = Property(name="code", type=StringType)
model_Payment.attributes={model_Payment_unpaidText, model_Payment_depositText, model_Payment_paidText, model_Payment_description, model_Payment_netDays, model_Payment_code, model_Payment_discountDays, model_Payment_discountValue}

# model_BankAccount class attributes and methods
model_BankAccount_accountHolder: Property = Property(name="accountHolder", type=StringType)
model_BankAccount_bankCode: Property = Property(name="bankCode", type=StringType)
model_BankAccount_bankName: Property = Property(name="bankName", type=StringType)
model_BankAccount_bic: Property = Property(name="bic", type=StringType)
model_BankAccount_iban: Property = Property(name="iban", type=StringType)
model_BankAccount.attributes={model_BankAccount_iban, model_BankAccount_accountHolder, model_BankAccount_bankName, model_BankAccount_bankCode, model_BankAccount_bic}

# model_Creditor class attributes and methods

# Contact class attributes and methods

# model_Debitor class attributes and methods

# model_Document class attributes and methods
model_Document_odtPath: Property = Property(name="odtPath", type=StringType)
model_Document_addressFirstLine: Property = Property(name="addressFirstLine", type=StringType)
model_Document_billingType: Property = Property(name="billingType", type=StringType)
model_Document_consultant: Property = Property(name="consultant", type=StringType)
model_Document_customerRef: Property = Property(name="customerRef", type=StringType)
model_Document_deposit: Property = Property(name="deposit", type=StringType)
model_Document_documentDate: Property = Property(name="documentDate", type=DateType)
model_Document_dueDays: Property = Property(name="dueDays", type=StringType)
model_Document_itemsRebate: Property = Property(name="itemsRebate", type=StringType)
model_Document_message: Property = Property(name="message", type=StringType)
model_Document_message2: Property = Property(name="message2", type=StringType)
model_Document_message3: Property = Property(name="message3", type=StringType)
model_Document_netGross: Property = Property(name="netGross", type=StringType)
model_Document_orderDate: Property = Property(name="orderDate", type=DateType)
model_Document_paidValue: Property = Property(name="paidValue", type=StringType)
model_Document_paid: Property = Property(name="paid", type=StringType)
model_Document_payDate: Property = Property(name="payDate", type=DateType)
model_Document_pdfPath: Property = Property(name="pdfPath", type=StringType)
model_Document_printed: Property = Property(name="printed", type=StringType)
model_Document_printTemplate: Property = Property(name="printTemplate", type=StringType)
model_Document_progress: Property = Property(name="progress", type=StringType)
model_Document_serviceDate: Property = Property(name="serviceDate", type=DateType)
model_Document_shippingAutoVat: Property = Property(name="shippingAutoVat", type=StringType)
model_Document_shippingValue: Property = Property(name="shippingValue", type=StringType)
model_Document_totalValue: Property = Property(name="totalValue", type=StringType)
model_Document_transactionId: Property = Property(name="transactionId", type=StringType)
model_Document_webshopDate: Property = Property(name="webshopDate", type=DateType)
model_Document_webshopId: Property = Property(name="webshopId", type=StringType)
model_Document_vestingPeriodStart: Property = Property(name="vestingPeriodStart", type=DateType)
model_Document_vestingPeriodEnd: Property = Property(name="vestingPeriodEnd", type=DateType)
model_Document.attributes={model_Document_addressFirstLine, model_Document_message2, model_Document_dueDays, model_Document_totalValue, model_Document_deposit, model_Document_printed, model_Document_serviceDate, model_Document_paid, model_Document_message, model_Document_printTemplate, model_Document_documentDate, model_Document_shippingAutoVat, model_Document_customerRef, model_Document_pdfPath, model_Document_orderDate, model_Document_odtPath, model_Document_billingType, model_Document_transactionId, model_Document_payDate, model_Document_itemsRebate, model_Document_paidValue, model_Document_netGross, model_Document_vestingPeriodEnd, model_Document_message3, model_Document_vestingPeriodStart, model_Document_progress, model_Document_webshopId, model_Document_shippingValue, model_Document_webshopDate, model_Document_consultant}

# model_IndividualDocumentInfo class attributes and methods
model_IndividualDocumentInfo_shippingValue: Property = Property(name="shippingValue", type=StringType)
model_IndividualDocumentInfo_paymentName: Property = Property(name="paymentName", type=StringType)
model_IndividualDocumentInfo_paymentText: Property = Property(name="paymentText", type=StringType)
model_IndividualDocumentInfo_paymentDescription: Property = Property(name="paymentDescription", type=StringType)
model_IndividualDocumentInfo_shippingName: Property = Property(name="shippingName", type=StringType)
model_IndividualDocumentInfo_shippingAutoVat: Property = Property(name="shippingAutoVat", type=StringType)
model_IndividualDocumentInfo_shippingDescription: Property = Property(name="shippingDescription", type=StringType)
model_IndividualDocumentInfo_shippingVatDescription: Property = Property(name="shippingVatDescription", type=StringType)
model_IndividualDocumentInfo_shippingVatValue: Property = Property(name="shippingVatValue", type=StringType)
model_IndividualDocumentInfo_noVatName: Property = Property(name="noVatName", type=StringType)
model_IndividualDocumentInfo_noVatDescription: Property = Property(name="noVatDescription", type=StringType)
model_IndividualDocumentInfo.attributes={model_IndividualDocumentInfo_shippingAutoVat, model_IndividualDocumentInfo_paymentText, model_IndividualDocumentInfo_noVatName, model_IndividualDocumentInfo_shippingValue, model_IndividualDocumentInfo_paymentDescription, model_IndividualDocumentInfo_shippingVatValue, model_IndividualDocumentInfo_shippingName, model_IndividualDocumentInfo_shippingDescription, model_IndividualDocumentInfo_noVatDescription, model_IndividualDocumentInfo_paymentName, model_IndividualDocumentInfo_shippingVatDescription}

# model_Invoice class attributes and methods

# model_DocumentItem class attributes and methods
model_DocumentItem_gtin: Property = Property(name="gtin", type=StringType)
model_DocumentItem_noVat: Property = Property(name="noVat", type=StringType)
model_DocumentItem_itemRebate: Property = Property(name="itemRebate", type=StringType)
model_DocumentItem_itemNumber: Property = Property(name="itemNumber", type=StringType)
model_DocumentItem_quantity: Property = Property(name="quantity", type=StringType)
model_DocumentItem_originQuantity: Property = Property(name="originQuantity", type=StringType)
model_DocumentItem_weight: Property = Property(name="weight", type=StringType)
model_DocumentItem_tara: Property = Property(name="tara", type=StringType)
model_DocumentItem_description: Property = Property(name="description", type=StringType)
model_DocumentItem_optional: Property = Property(name="optional", type=StringType)
model_DocumentItem_picture: Property = Property(name="picture", type=StringType)
model_DocumentItem_price: Property = Property(name="price", type=StringType)
model_DocumentItem_quantityUnit: Property = Property(name="quantityUnit", type=StringType)
model_DocumentItem_posNr: Property = Property(name="posNr", type=StringType)
model_DocumentItem_itemType: Property = Property(name="itemType", type=StringType)
model_DocumentItem_vestingPeriodStart: Property = Property(name="vestingPeriodStart", type=DateType)
model_DocumentItem_vestingPeriodEnd: Property = Property(name="vestingPeriodEnd", type=DateType)
model_DocumentItem.attributes={model_DocumentItem_description, model_DocumentItem_optional, model_DocumentItem_vestingPeriodStart, model_DocumentItem_itemRebate, model_DocumentItem_originQuantity, model_DocumentItem_quantity, model_DocumentItem_tara, model_DocumentItem_itemType, model_DocumentItem_noVat, model_DocumentItem_quantityUnit, model_DocumentItem_price, model_DocumentItem_picture, model_DocumentItem_itemNumber, model_DocumentItem_gtin, model_DocumentItem_vestingPeriodEnd, model_DocumentItem_weight, model_DocumentItem_posNr}

# model_VAT class attributes and methods
model_VAT_description: Property = Property(name="description", type=StringType)
model_VAT_taxValue: Property = Property(name="taxValue", type=StringType)
model_VAT_salesEqualizationTax: Property = Property(name="salesEqualizationTax", type=StringType)
model_VAT.attributes={model_VAT_salesEqualizationTax, model_VAT_taxValue, model_VAT_description}

# model_Shipping class attributes and methods
model_Shipping_autoVat: Property = Property(name="autoVat", type=StringType)
model_Shipping_shippingValue: Property = Property(name="shippingValue", type=StringType)
model_Shipping_code: Property = Property(name="code", type=StringType)
model_Shipping.attributes={model_Shipping_shippingValue, model_Shipping_autoVat, model_Shipping_code}

# model_Product class attributes and methods
model_Product_webshopId: Property = Property(name="webshopId", type=StringType)
model_Product_weight: Property = Property(name="weight", type=StringType)
model_Product_block1: Property = Property(name="block1", type=StringType)
model_Product_block2: Property = Property(name="block2", type=StringType)
model_Product_block3: Property = Property(name="block3", type=StringType)
model_Product_block4: Property = Property(name="block4", type=StringType)
model_Product_block5: Property = Property(name="block5", type=StringType)
model_Product_picture: Property = Property(name="picture", type=StringType)
model_Product_itemNumber: Property = Property(name="itemNumber", type=StringType)
model_Product_price1: Property = Property(name="price1", type=StringType)
model_Product_price2: Property = Property(name="price2", type=StringType)
model_Product_price3: Property = Property(name="price3", type=StringType)
model_Product_price4: Property = Property(name="price4", type=StringType)
model_Product_price5: Property = Property(name="price5", type=StringType)
model_Product_quantity: Property = Property(name="quantity", type=StringType)
model_Product_quantityUnit: Property = Property(name="quantityUnit", type=StringType)
model_Product_sellingUnit: Property = Property(name="sellingUnit", type=StringType)
model_Product_gtin: Property = Property(name="gtin", type=StringType)
model_Product_costPrice: Property = Property(name="costPrice", type=StringType)
model_Product_cdf01: Property = Property(name="cdf01", type=StringType)
model_Product_cdf02: Property = Property(name="cdf02", type=StringType)
model_Product_cdf03: Property = Property(name="cdf03", type=StringType)
model_Product.attributes={model_Product_cdf03, model_Product_itemNumber, model_Product_price2, model_Product_block2, model_Product_block1, model_Product_quantityUnit, model_Product_weight, model_Product_costPrice, model_Product_block3, model_Product_webshopId, model_Product_price3, model_Product_price5, model_Product_quantity, model_Product_picture, model_Product_gtin, model_Product_cdf02, model_Product_block5, model_Product_cdf01, model_Product_sellingUnit, model_Product_price1, model_Product_block4, model_Product_price4}

# model_ItemListTypeCategory class attributes and methods

# Document class attributes and methods

# model_Order class attributes and methods

# model_Letter class attributes and methods

# model_Offer class attributes and methods

# model_Dunning class attributes and methods
model_Dunning_dunningLevel: Property = Property(name="dunningLevel", type=StringType)
model_Dunning.attributes={model_Dunning_dunningLevel}

# model_Credit class attributes and methods

# model_Delivery class attributes and methods

# model_Confirmation class attributes and methods

# model_Proforma class attributes and methods

# model_Voucher class attributes and methods
model_Voucher_voucherDate: Property = Property(name="voucherDate", type=DateType)
model_Voucher_discounted: Property = Property(name="discounted", type=StringType)
model_Voucher_doNotBook: Property = Property(name="doNotBook", type=StringType)
model_Voucher_documentNumber: Property = Property(name="documentNumber", type=StringType)
model_Voucher_voucherNumber: Property = Property(name="voucherNumber", type=StringType)
model_Voucher_paidValue: Property = Property(name="paidValue", type=StringType)
model_Voucher_totalValue: Property = Property(name="totalValue", type=StringType)
model_Voucher_voucherType: Property = Property(name="voucherType", type=StringType)
model_Voucher.attributes={model_Voucher_totalValue, model_Voucher_discounted, model_Voucher_voucherDate, model_Voucher_voucherNumber, model_Voucher_paidValue, model_Voucher_documentNumber, model_Voucher_doNotBook, model_Voucher_voucherType}

# model_VoucherItem class attributes and methods
model_VoucherItem_price: Property = Property(name="price", type=StringType)
model_VoucherItem_posNr: Property = Property(name="posNr", type=StringType)
model_VoucherItem_itemVoucherType: Property = Property(name="itemVoucherType", type=StringType)
model_VoucherItem.attributes={model_VoucherItem_price, model_VoucherItem_posNr, model_VoucherItem_itemVoucherType}

# model_ItemAccountType class attributes and methods
model_ItemAccountType_value: Property = Property(name="value", type=StringType)
model_ItemAccountType.attributes={model_ItemAccountType_value}

# IDescribableEntity class attributes and methods

# model_ProductCategory class attributes and methods

# model_ProductOptions class attributes and methods
model_ProductOptions_attributeValue: Property = Property(name="attributeValue", type=StringType)
model_ProductOptions_sequenceNumber: Property = Property(name="sequenceNumber", type=StringType)
model_ProductOptions.attributes={model_ProductOptions_attributeValue, model_ProductOptions_sequenceNumber}

# model_ProductBlockPrice class attributes and methods
model_ProductBlockPrice_block: Property = Property(name="block", type=StringType)
model_ProductBlockPrice_price: Property = Property(name="price", type=StringType)
model_ProductBlockPrice.attributes={model_ProductBlockPrice_block, model_ProductBlockPrice_price}

# model_ShippingCategory class attributes and methods

# model_Tenant class attributes and methods

# model_TextModule class attributes and methods
model_TextModule_text: Property = Property(name="text", type=StringType)
model_TextModule.attributes={model_TextModule_text}

# model_TextCategory class attributes and methods

# model_User class attributes and methods
model_User_password: Property = Property(name="password", type=StringType)
model_User_userName: Property = Property(name="userName", type=StringType)
model_User.attributes={model_User_password, model_User_userName}

# model_Role class attributes and methods

# model_UserProperty class attributes and methods
model_UserProperty_value: Property = Property(name="value", type=StringType)
model_UserProperty_user: Property = Property(name="user", type=StringType)
model_UserProperty_default: Property = Property(name="default", type=StringType)
model_UserProperty_global: Property = Property(name="global", type=StringType)
model_UserProperty.attributes={model_UserProperty_value, model_UserProperty_global, model_UserProperty_user, model_UserProperty_default}

# model_VATCategory class attributes and methods

# model_CEFACTCode class attributes and methods
model_CEFACTCode_abbreviation_de: Property = Property(name="abbreviation_de", type=StringType)
model_CEFACTCode_abbreviation_en: Property = Property(name="abbreviation_en", type=StringType)
model_CEFACTCode_code: Property = Property(name="code", type=StringType)
model_CEFACTCode_target: Property = Property(name="target", type=StringType)
model_CEFACTCode_name_de: Property = Property(name="name_de", type=StringType)
model_CEFACTCode.attributes={model_CEFACTCode_abbreviation_en, model_CEFACTCode_target, model_CEFACTCode_abbreviation_de, model_CEFACTCode_code, model_CEFACTCode_name_de}

# model_WebShop class attributes and methods
model_WebShop_webshopVendor: Property = Property(name="webshopVendor", type=StringType)
model_WebShop_webshopVersion: Property = Property(name="webshopVersion", type=StringType)
model_WebShop.attributes={model_WebShop_webshopVersion, model_WebShop_webshopVendor}

# model_WebshopStateMapping class attributes and methods
model_WebshopStateMapping_webshopState: Property = Property(name="webshopState", type=StringType)
model_WebshopStateMapping_fakturamaOrderState: Property = Property(name="fakturamaOrderState", type=StringType)
model_WebshopStateMapping.attributes={model_WebshopStateMapping_webshopState, model_WebshopStateMapping_fakturamaOrderState}

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="model_AbstractCategory", type=model_AbstractCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractCategory0", type=model_AbstractCategory, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address2: BinaryAssociation = BinaryAssociation(
    name="address2",
    ends={
        Property(name="model_Address", type=model_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Contact", type=model_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alternateContacts4: BinaryAssociation = BinaryAssociation(
    name="alternateContacts4",
    ends={
        Property(name="model_Contact5", type=model_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Contact3", type=model_Contact, multiplicity=Multiplicity(0, 1))
    }
)
categories6: BinaryAssociation = BinaryAssociation(
    name="categories6",
    ends={
        Property(name="model_ContactCategory", type=model_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Contact7", type=model_ContactCategory, multiplicity=Multiplicity(0, 1))
    }
)
payment8: BinaryAssociation = BinaryAssociation(
    name="payment8",
    ends={
        Property(name="model_Payment", type=model_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Contact9", type=model_Payment, multiplicity=Multiplicity(0, 1))
    }
)
bankAccount10: BinaryAssociation = BinaryAssociation(
    name="bankAccount10",
    ends={
        Property(name="model_BankAccount", type=model_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Contact11", type=model_BankAccount, multiplicity=Multiplicity(0, 1))
    }
)
additionalInfo12: BinaryAssociation = BinaryAssociation(
    name="additionalInfo12",
    ends={
        Property(name="model_IndividualDocumentInfo", type=model_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Document", type=model_IndividualDocumentInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
billingContact13: BinaryAssociation = BinaryAssociation(
    name="billingContact13",
    ends={
        Property(name="model_Contact15", type=model_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Document14", type=model_Contact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deliveryContact16: BinaryAssociation = BinaryAssociation(
    name="deliveryContact16",
    ends={
        Property(name="model_Contact18", type=model_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Document17", type=model_Contact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invoiceReference19: BinaryAssociation = BinaryAssociation(
    name="invoiceReference19",
    ends={
        Property(name="model_Invoice", type=model_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Document20", type=model_Invoice, multiplicity=Multiplicity(0, 1))
    }
)
items21: BinaryAssociation = BinaryAssociation(
    name="items21",
    ends={
        Property(name="model_DocumentItem", type=model_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Document22", type=model_DocumentItem, multiplicity=Multiplicity(0, 9999))
    }
)
noVatReference23: BinaryAssociation = BinaryAssociation(
    name="noVatReference23",
    ends={
        Property(name="model_VAT", type=model_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Document24", type=model_VAT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
payment25: BinaryAssociation = BinaryAssociation(
    name="payment25",
    ends={
        Property(name="model_Payment27", type=model_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Document26", type=model_Payment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shipping28: BinaryAssociation = BinaryAssociation(
    name="shipping28",
    ends={
        Property(name="model_Shipping", type=model_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Document29", type=model_Shipping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceDocument31: BinaryAssociation = BinaryAssociation(
    name="sourceDocument31",
    ends={
        Property(name="model_Document32", type=model_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Document30", type=model_Document, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
product33: BinaryAssociation = BinaryAssociation(
    name="product33",
    ends={
        Property(name="model_Product", type=model_DocumentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DocumentItem34", type=model_Product, multiplicity=Multiplicity(0, 1))
    }
)
itemVat35: BinaryAssociation = BinaryAssociation(
    name="itemVat35",
    ends={
        Property(name="model_VAT37", type=model_DocumentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DocumentItem36", type=model_VAT, multiplicity=Multiplicity(0, 1))
    }
)
category46: BinaryAssociation = BinaryAssociation(
    name="category46",
    ends={
        Property(name="model_ItemListTypeCategory", type=model_ItemAccountType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ItemAccountType47", type=model_ItemListTypeCategory, multiplicity=Multiplicity(0, 1))
    }
)
account38: BinaryAssociation = BinaryAssociation(
    name="account38",
    ends={
        Property(name="model_VoucherCategory", type=model_Voucher, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Voucher", type=model_VoucherCategory, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items39: BinaryAssociation = BinaryAssociation(
    name="items39",
    ends={
        Property(name="model_VoucherItem", type=model_Voucher, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Voucher40", type=model_VoucherItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accountType41: BinaryAssociation = BinaryAssociation(
    name="accountType41",
    ends={
        Property(name="model_ItemAccountType", type=model_VoucherItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_VoucherItem42", type=model_ItemAccountType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vat43: BinaryAssociation = BinaryAssociation(
    name="vat43",
    ends={
        Property(name="model_VAT45", type=model_VoucherItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_VoucherItem44", type=model_VAT, multiplicity=Multiplicity(0, 1))
    }
)
category48: BinaryAssociation = BinaryAssociation(
    name="category48",
    ends={
        Property(name="model_VoucherCategory50", type=model_Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Payment49", type=model_VoucherCategory, multiplicity=Multiplicity(0, 1))
    }
)
categories51: BinaryAssociation = BinaryAssociation(
    name="categories51",
    ends={
        Property(name="model_ProductCategory", type=model_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Product52", type=model_ProductCategory, multiplicity=Multiplicity(0, 1))
    }
)
attributes53: BinaryAssociation = BinaryAssociation(
    name="attributes53",
    ends={
        Property(name="model_ProductOptions", type=model_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Product54", type=model_ProductOptions, multiplicity=Multiplicity(0, 9999))
    }
)
vat55: BinaryAssociation = BinaryAssociation(
    name="vat55",
    ends={
        Property(name="model_VAT57", type=model_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Product56", type=model_VAT, multiplicity=Multiplicity(0, 1))
    }
)
blockPrices58: BinaryAssociation = BinaryAssociation(
    name="blockPrices58",
    ends={
        Property(name="model_ProductBlockPrice", type=model_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Product59", type=model_ProductBlockPrice, multiplicity=Multiplicity(1, 9999))
    }
)
shippingVat60: BinaryAssociation = BinaryAssociation(
    name="shippingVat60",
    ends={
        Property(name="model_VAT62", type=model_Shipping, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Shipping61", type=model_VAT, multiplicity=Multiplicity(1, 1))
    }
)
categories63: BinaryAssociation = BinaryAssociation(
    name="categories63",
    ends={
        Property(name="model_ShippingCategory", type=model_Shipping, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Shipping64", type=model_ShippingCategory, multiplicity=Multiplicity(0, 1))
    }
)
categories65: BinaryAssociation = BinaryAssociation(
    name="categories65",
    ends={
        Property(name="model_TextCategory", type=model_TextModule, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TextModule", type=model_TextCategory, multiplicity=Multiplicity(0, 1))
    }
)
tenant66: BinaryAssociation = BinaryAssociation(
    name="tenant66",
    ends={
        Property(name="model_Tenant", type=model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="model_User", type=model_Tenant, multiplicity=Multiplicity(0, 1))
    }
)
roles67: BinaryAssociation = BinaryAssociation(
    name="roles67",
    ends={
        Property(name="model_Role", type=model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="model_User68", type=model_Role, multiplicity=Multiplicity(0, 9999))
    }
)
category69: BinaryAssociation = BinaryAssociation(
    name="category69",
    ends={
        Property(name="model_VATCategory", type=model_VAT, multiplicity=Multiplicity(1, 1)),
        Property(name="model_VAT70", type=model_VATCategory, multiplicity=Multiplicity(0, 1))
    }
)
stateMapping71: BinaryAssociation = BinaryAssociation(
    name="stateMapping71",
    ends={
        Property(name="model_WebshopStateMapping", type=model_WebShop, multiplicity=Multiplicity(1, 1)),
        Property(name="model_WebShop", type=model_WebshopStateMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_IDescribableEntity_IEntity = Generalization(general=IEntity, specific=model_IDescribableEntity)
gen_model_AbstractCategory_IEntity = Generalization(general=IEntity, specific=model_AbstractCategory)
gen_model_VoucherCategory_AbstractCategory = Generalization(general=AbstractCategory, specific=model_VoucherCategory)
gen_model_Address_IEntity = Generalization(general=IEntity, specific=model_Address)
gen_model_Contact_IEntity = Generalization(general=IEntity, specific=model_Contact)
gen_model_ContactCategory_AbstractCategory = Generalization(general=AbstractCategory, specific=model_ContactCategory)
gen_model_Creditor_Contact = Generalization(general=Contact, specific=model_Creditor)
gen_model_Debitor_Contact = Generalization(general=Contact, specific=model_Debitor)
gen_model_BankAccount_IEntity = Generalization(general=IEntity, specific=model_BankAccount)
gen_model_Document_IEntity = Generalization(general=IEntity, specific=model_Document)
gen_model_DocumentItem_IEntity = Generalization(general=IEntity, specific=model_DocumentItem)
gen_model_Invoice_Document = Generalization(general=Document, specific=model_Invoice)
gen_model_Order_Document = Generalization(general=Document, specific=model_Order)
gen_model_Letter_Document = Generalization(general=Document, specific=model_Letter)
gen_model_Offer_Document = Generalization(general=Document, specific=model_Offer)
gen_model_Dunning_Document = Generalization(general=Document, specific=model_Dunning)
gen_model_Credit_Document = Generalization(general=Document, specific=model_Credit)
gen_model_Delivery_Document = Generalization(general=Document, specific=model_Delivery)
gen_model_Confirmation_Document = Generalization(general=Document, specific=model_Confirmation)
gen_model_Proforma_Document = Generalization(general=Document, specific=model_Proforma)
gen_model_Voucher_IEntity = Generalization(general=IEntity, specific=model_Voucher)
gen_model_VoucherItem_IEntity = Generalization(general=IEntity, specific=model_VoucherItem)
gen_model_ItemAccountType_IEntity = Generalization(general=IEntity, specific=model_ItemAccountType)
gen_model_Payment_IEntity = Generalization(general=IEntity, specific=model_Payment)
gen_model_Product_IDescribableEntity = Generalization(general=IDescribableEntity, specific=model_Product)
gen_model_ProductOptions_IEntity = Generalization(general=IEntity, specific=model_ProductOptions)
gen_model_ProductBlockPrice_IEntity = Generalization(general=IEntity, specific=model_ProductBlockPrice)
gen_model_ProductCategory_AbstractCategory = Generalization(general=AbstractCategory, specific=model_ProductCategory)
gen_model_Shipping_IDescribableEntity = Generalization(general=IDescribableEntity, specific=model_Shipping)
gen_model_ShippingCategory_AbstractCategory = Generalization(general=AbstractCategory, specific=model_ShippingCategory)
gen_model_Tenant_IEntity = Generalization(general=IEntity, specific=model_Tenant)
gen_model_TextModule_IEntity = Generalization(general=IEntity, specific=model_TextModule)
gen_model_TextCategory_AbstractCategory = Generalization(general=AbstractCategory, specific=model_TextCategory)
gen_model_IndividualDocumentInfo_IEntity = Generalization(general=IEntity, specific=model_IndividualDocumentInfo)
gen_model_CEFACTCode_IEntity = Generalization(general=IEntity, specific=model_CEFACTCode)
gen_model_User_IEntity = Generalization(general=IEntity, specific=model_User)
gen_model_Role_IEntity = Generalization(general=IEntity, specific=model_Role)
gen_model_UserProperty_IEntity = Generalization(general=IEntity, specific=model_UserProperty)
gen_model_VAT_IEntity = Generalization(general=IEntity, specific=model_VAT)
gen_model_VATCategory_AbstractCategory = Generalization(general=AbstractCategory, specific=model_VATCategory)
gen_model_ItemListTypeCategory_AbstractCategory = Generalization(general=AbstractCategory, specific=model_ItemListTypeCategory)
gen_model_WebShop_IEntity = Generalization(general=IEntity, specific=model_WebShop)
gen_model_WebshopStateMapping_IEntity = Generalization(general=IEntity, specific=model_WebshopStateMapping)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_IEntity, model_IDescribableEntity, IEntity, model_AbstractCategory, model_VoucherCategory, AbstractCategory, model_Address, model_Contact, model_ContactCategory, model_Payment, model_BankAccount, model_Creditor, Contact, model_Debitor, model_Document, model_IndividualDocumentInfo, model_Invoice, model_DocumentItem, model_VAT, model_Shipping, model_Product, model_ItemListTypeCategory, Document, model_Order, model_Letter, model_Offer, model_Dunning, model_Credit, model_Delivery, model_Confirmation, model_Proforma, model_Voucher, model_VoucherItem, model_ItemAccountType, IDescribableEntity, model_ProductCategory, model_ProductOptions, model_ProductBlockPrice, model_ShippingCategory, model_Tenant, model_TextModule, model_TextCategory, model_User, model_Role, model_UserProperty, model_VATCategory, model_CEFACTCode, model_WebShop, model_WebshopStateMapping, ShippingVatType, BillingType, ContactType, ItemType, ReliabilityType, VoucherType},
    associations={parent1, address2, alternateContacts4, categories6, payment8, bankAccount10, additionalInfo12, billingContact13, deliveryContact16, invoiceReference19, items21, noVatReference23, payment25, shipping28, sourceDocument31, product33, itemVat35, category46, account38, items39, accountType41, vat43, category48, categories51, attributes53, vat55, blockPrices58, shippingVat60, categories63, categories65, tenant66, roles67, category69, stateMapping71},
    generalizations={gen_model_IDescribableEntity_IEntity, gen_model_AbstractCategory_IEntity, gen_model_VoucherCategory_AbstractCategory, gen_model_Address_IEntity, gen_model_Contact_IEntity, gen_model_ContactCategory_AbstractCategory, gen_model_Creditor_Contact, gen_model_Debitor_Contact, gen_model_BankAccount_IEntity, gen_model_Document_IEntity, gen_model_DocumentItem_IEntity, gen_model_Invoice_Document, gen_model_Order_Document, gen_model_Letter_Document, gen_model_Offer_Document, gen_model_Dunning_Document, gen_model_Credit_Document, gen_model_Delivery_Document, gen_model_Confirmation_Document, gen_model_Proforma_Document, gen_model_Voucher_IEntity, gen_model_VoucherItem_IEntity, gen_model_ItemAccountType_IEntity, gen_model_Payment_IEntity, gen_model_Product_IDescribableEntity, gen_model_ProductOptions_IEntity, gen_model_ProductBlockPrice_IEntity, gen_model_ProductCategory_AbstractCategory, gen_model_Shipping_IDescribableEntity, gen_model_ShippingCategory_AbstractCategory, gen_model_Tenant_IEntity, gen_model_TextModule_IEntity, gen_model_TextCategory_AbstractCategory, gen_model_IndividualDocumentInfo_IEntity, gen_model_CEFACTCode_IEntity, gen_model_User_IEntity, gen_model_Role_IEntity, gen_model_UserProperty_IEntity, gen_model_VAT_IEntity, gen_model_VATCategory_AbstractCategory, gen_model_ItemListTypeCategory_AbstractCategory, gen_model_WebShop_IEntity, gen_model_WebshopStateMapping_IEntity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)