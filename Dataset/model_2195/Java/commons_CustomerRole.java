





import java.util.List;
import java.util.ArrayList;

public class commons_CustomerRole extends Timestamped, NameContainer, Describable, SchemaVersionable, Identifiable {

    private boolean salesOrderReportEnabled;
    private boolean quickShopEnabled;
    private boolean dropshipEnabled;
    private String schemaVersion;
    private boolean transactionHistoryEnabled;
    private String status;
    private boolean paymentGatewayEnabled;
    private boolean reviewReminderEnabled;
    private boolean agentSalesReportEnabled;
    private int bookingExpiryTimeInMinutes;
    private String zendeskOrganizationId;
    private boolean readOnly;
    private boolean zendeskIntegration;
    private boolean historySalesOrderEnabled;
    private boolean bookingEnabled;



    public commons_CustomerRole(
        boolean salesOrderReportEnabled,        boolean quickShopEnabled,        boolean dropshipEnabled,        String schemaVersion,        boolean transactionHistoryEnabled,        String status,        boolean paymentGatewayEnabled,        boolean reviewReminderEnabled,        boolean agentSalesReportEnabled,        int bookingExpiryTimeInMinutes,        String zendeskOrganizationId,        boolean readOnly,        boolean zendeskIntegration,        boolean historySalesOrderEnabled,        boolean bookingEnabled    ) {
        super(
        );
        this.salesOrderReportEnabled = salesOrderReportEnabled;
        this.quickShopEnabled = quickShopEnabled;
        this.dropshipEnabled = dropshipEnabled;
        this.schemaVersion = schemaVersion;
        this.transactionHistoryEnabled = transactionHistoryEnabled;
        this.status = status;
        this.paymentGatewayEnabled = paymentGatewayEnabled;
        this.reviewReminderEnabled = reviewReminderEnabled;
        this.agentSalesReportEnabled = agentSalesReportEnabled;
        this.bookingExpiryTimeInMinutes = bookingExpiryTimeInMinutes;
        this.zendeskOrganizationId = zendeskOrganizationId;
        this.readOnly = readOnly;
        this.zendeskIntegration = zendeskIntegration;
        this.historySalesOrderEnabled = historySalesOrderEnabled;
        this.bookingEnabled = bookingEnabled;
    }


    public boolean getSalesorderreportenabled() {
        return salesOrderReportEnabled;
    }

    public void setSalesorderreportenabled(boolean salesOrderReportEnabled) {
        this.salesOrderReportEnabled = salesOrderReportEnabled;
    }
    public boolean getQuickshopenabled() {
        return quickShopEnabled;
    }

    public void setQuickshopenabled(boolean quickShopEnabled) {
        this.quickShopEnabled = quickShopEnabled;
    }
    public boolean getDropshipenabled() {
        return dropshipEnabled;
    }

    public void setDropshipenabled(boolean dropshipEnabled) {
        this.dropshipEnabled = dropshipEnabled;
    }
    public String getSchemaversion() {
        return schemaVersion;
    }

    public void setSchemaversion(String schemaVersion) {
        this.schemaVersion = schemaVersion;
    }
    public boolean getTransactionhistoryenabled() {
        return transactionHistoryEnabled;
    }

    public void setTransactionhistoryenabled(boolean transactionHistoryEnabled) {
        this.transactionHistoryEnabled = transactionHistoryEnabled;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public boolean getPaymentgatewayenabled() {
        return paymentGatewayEnabled;
    }

    public void setPaymentgatewayenabled(boolean paymentGatewayEnabled) {
        this.paymentGatewayEnabled = paymentGatewayEnabled;
    }
    public boolean getReviewreminderenabled() {
        return reviewReminderEnabled;
    }

    public void setReviewreminderenabled(boolean reviewReminderEnabled) {
        this.reviewReminderEnabled = reviewReminderEnabled;
    }
    public boolean getAgentsalesreportenabled() {
        return agentSalesReportEnabled;
    }

    public void setAgentsalesreportenabled(boolean agentSalesReportEnabled) {
        this.agentSalesReportEnabled = agentSalesReportEnabled;
    }
    public int getBookingexpirytimeinminutes() {
        return bookingExpiryTimeInMinutes;
    }

    public void setBookingexpirytimeinminutes(int bookingExpiryTimeInMinutes) {
        this.bookingExpiryTimeInMinutes = bookingExpiryTimeInMinutes;
    }
    public String getZendeskorganizationid() {
        return zendeskOrganizationId;
    }

    public void setZendeskorganizationid(String zendeskOrganizationId) {
        this.zendeskOrganizationId = zendeskOrganizationId;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public boolean getZendeskintegration() {
        return zendeskIntegration;
    }

    public void setZendeskintegration(boolean zendeskIntegration) {
        this.zendeskIntegration = zendeskIntegration;
    }
    public boolean getHistorysalesorderenabled() {
        return historySalesOrderEnabled;
    }

    public void setHistorysalesorderenabled(boolean historySalesOrderEnabled) {
        this.historySalesOrderEnabled = historySalesOrderEnabled;
    }
    public boolean getBookingenabled() {
        return bookingEnabled;
    }

    public void setBookingenabled(boolean bookingEnabled) {
        this.bookingEnabled = bookingEnabled;
    }


}