




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Document extends IEntity {

    private String paidValue;
    private String netGross;
    private String shippingValue;
    private String printTemplate;
    private String itemsRebate;
    private LocalDate payDate;
    private String message;
    private String billingType;
    private String customerRef;
    private String odtPath;
    private String pdfPath;
    private LocalDate serviceDate;
    private LocalDate vestingPeriodStart;
    private LocalDate orderDate;
    private String webshopId;
    private LocalDate vestingPeriodEnd;
    private String progress;
    private LocalDate webshopDate;
    private String transactionId;
    private String shippingAutoVat;
    private String consultant;
    private String printed;
    private String deposit;
    private String totalValue;
    private String dueDays;
    private String message3;
    private LocalDate documentDate;
    private String paid;
    private String addressFirstLine;
    private String message2;





    private model_Payment model_payment;




    private model_IndividualDocumentInfo model_individualdocumentinfo;




    private model_Document model_document;




    private model_VAT model_vat;


    public model_Document(
        String paidValue,        String netGross,        String shippingValue,        String printTemplate,        String itemsRebate,        LocalDate payDate,        String message,        String billingType,        String customerRef,        String odtPath,        String pdfPath,        LocalDate serviceDate,        LocalDate vestingPeriodStart,        LocalDate orderDate,        String webshopId,        LocalDate vestingPeriodEnd,        String progress,        LocalDate webshopDate,        String transactionId,        String shippingAutoVat,        String consultant,        String printed,        String deposit,        String totalValue,        String dueDays,        String message3,        LocalDate documentDate,        String paid,        String addressFirstLine,        String message2    ) {
        super(
        );
        this.paidValue = paidValue;
        this.netGross = netGross;
        this.shippingValue = shippingValue;
        this.printTemplate = printTemplate;
        this.itemsRebate = itemsRebate;
        this.payDate = payDate;
        this.message = message;
        this.billingType = billingType;
        this.customerRef = customerRef;
        this.odtPath = odtPath;
        this.pdfPath = pdfPath;
        this.serviceDate = serviceDate;
        this.vestingPeriodStart = vestingPeriodStart;
        this.orderDate = orderDate;
        this.webshopId = webshopId;
        this.vestingPeriodEnd = vestingPeriodEnd;
        this.progress = progress;
        this.webshopDate = webshopDate;
        this.transactionId = transactionId;
        this.shippingAutoVat = shippingAutoVat;
        this.consultant = consultant;
        this.printed = printed;
        this.deposit = deposit;
        this.totalValue = totalValue;
        this.dueDays = dueDays;
        this.message3 = message3;
        this.documentDate = documentDate;
        this.paid = paid;
        this.addressFirstLine = addressFirstLine;
        this.message2 = message2;
    }


    public String getPaidvalue() {
        return paidValue;
    }

    public void setPaidvalue(String paidValue) {
        this.paidValue = paidValue;
    }
    public String getNetgross() {
        return netGross;
    }

    public void setNetgross(String netGross) {
        this.netGross = netGross;
    }
    public String getShippingvalue() {
        return shippingValue;
    }

    public void setShippingvalue(String shippingValue) {
        this.shippingValue = shippingValue;
    }
    public String getPrinttemplate() {
        return printTemplate;
    }

    public void setPrinttemplate(String printTemplate) {
        this.printTemplate = printTemplate;
    }
    public String getItemsrebate() {
        return itemsRebate;
    }

    public void setItemsrebate(String itemsRebate) {
        this.itemsRebate = itemsRebate;
    }
    public LocalDate getPaydate() {
        return payDate;
    }

    public void setPaydate(LocalDate payDate) {
        this.payDate = payDate;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getBillingtype() {
        return billingType;
    }

    public void setBillingtype(String billingType) {
        this.billingType = billingType;
    }
    public String getCustomerref() {
        return customerRef;
    }

    public void setCustomerref(String customerRef) {
        this.customerRef = customerRef;
    }
    public String getOdtpath() {
        return odtPath;
    }

    public void setOdtpath(String odtPath) {
        this.odtPath = odtPath;
    }
    public String getPdfpath() {
        return pdfPath;
    }

    public void setPdfpath(String pdfPath) {
        this.pdfPath = pdfPath;
    }
    public LocalDate getServicedate() {
        return serviceDate;
    }

    public void setServicedate(LocalDate serviceDate) {
        this.serviceDate = serviceDate;
    }
    public LocalDate getVestingperiodstart() {
        return vestingPeriodStart;
    }

    public void setVestingperiodstart(LocalDate vestingPeriodStart) {
        this.vestingPeriodStart = vestingPeriodStart;
    }
    public LocalDate getOrderdate() {
        return orderDate;
    }

    public void setOrderdate(LocalDate orderDate) {
        this.orderDate = orderDate;
    }
    public String getWebshopid() {
        return webshopId;
    }

    public void setWebshopid(String webshopId) {
        this.webshopId = webshopId;
    }
    public LocalDate getVestingperiodend() {
        return vestingPeriodEnd;
    }

    public void setVestingperiodend(LocalDate vestingPeriodEnd) {
        this.vestingPeriodEnd = vestingPeriodEnd;
    }
    public String getProgress() {
        return progress;
    }

    public void setProgress(String progress) {
        this.progress = progress;
    }
    public LocalDate getWebshopdate() {
        return webshopDate;
    }

    public void setWebshopdate(LocalDate webshopDate) {
        this.webshopDate = webshopDate;
    }
    public String getTransactionid() {
        return transactionId;
    }

    public void setTransactionid(String transactionId) {
        this.transactionId = transactionId;
    }
    public String getShippingautovat() {
        return shippingAutoVat;
    }

    public void setShippingautovat(String shippingAutoVat) {
        this.shippingAutoVat = shippingAutoVat;
    }
    public String getConsultant() {
        return consultant;
    }

    public void setConsultant(String consultant) {
        this.consultant = consultant;
    }
    public String getPrinted() {
        return printed;
    }

    public void setPrinted(String printed) {
        this.printed = printed;
    }
    public String getDeposit() {
        return deposit;
    }

    public void setDeposit(String deposit) {
        this.deposit = deposit;
    }
    public String getTotalvalue() {
        return totalValue;
    }

    public void setTotalvalue(String totalValue) {
        this.totalValue = totalValue;
    }
    public String getDuedays() {
        return dueDays;
    }

    public void setDuedays(String dueDays) {
        this.dueDays = dueDays;
    }
    public String getMessage3() {
        return message3;
    }

    public void setMessage3(String message3) {
        this.message3 = message3;
    }
    public LocalDate getDocumentdate() {
        return documentDate;
    }

    public void setDocumentdate(LocalDate documentDate) {
        this.documentDate = documentDate;
    }
    public String getPaid() {
        return paid;
    }

    public void setPaid(String paid) {
        this.paid = paid;
    }
    public String getAddressfirstline() {
        return addressFirstLine;
    }

    public void setAddressfirstline(String addressFirstLine) {
        this.addressFirstLine = addressFirstLine;
    }
    public String getMessage2() {
        return message2;
    }

    public void setMessage2(String message2) {
        this.message2 = message2;
    }

    public model_Payment getModel_payment() {
        return model_payment;
    }

    public void setModel_payment(model_Payment model_payment) {
        this.model_payment = model_payment;
    }
    public model_IndividualDocumentInfo getModel_individualdocumentinfo() {
        return model_individualdocumentinfo;
    }

    public void setModel_individualdocumentinfo(model_IndividualDocumentInfo model_individualdocumentinfo) {
        this.model_individualdocumentinfo = model_individualdocumentinfo;
    }
    public model_Document getModel_document() {
        return model_document;
    }

    public void setModel_document(model_Document model_document) {
        this.model_document = model_document;
    }
    public model_VAT getModel_vat() {
        return model_vat;
    }

    public void setModel_vat(model_VAT model_vat) {
        this.model_vat = model_vat;
    }

}