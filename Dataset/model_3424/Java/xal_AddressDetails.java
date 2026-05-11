





import java.util.List;
import java.util.ArrayList;

public class xal_AddressDetails  {

    private String currentStatus;
    private String any;
    private String usage;
    private String addressType;
    private String addressDetailsKey;
    private String code;
    private String validFromDate;
    private String validToDate;
    private String anyAttribute;





    private xal_Address xal_address;


    public xal_AddressDetails(
        String currentStatus,        String any,        String usage,        String addressType,        String addressDetailsKey,        String code,        String validFromDate,        String validToDate,        String anyAttribute    ) {
        this.currentStatus = currentStatus;
        this.any = any;
        this.usage = usage;
        this.addressType = addressType;
        this.addressDetailsKey = addressDetailsKey;
        this.code = code;
        this.validFromDate = validFromDate;
        this.validToDate = validToDate;
        this.anyAttribute = anyAttribute;
    }


    public String getCurrentstatus() {
        return currentStatus;
    }

    public void setCurrentstatus(String currentStatus) {
        this.currentStatus = currentStatus;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getUsage() {
        return usage;
    }

    public void setUsage(String usage) {
        this.usage = usage;
    }
    public String getAddresstype() {
        return addressType;
    }

    public void setAddresstype(String addressType) {
        this.addressType = addressType;
    }
    public String getAddressdetailskey() {
        return addressDetailsKey;
    }

    public void setAddressdetailskey(String addressDetailsKey) {
        this.addressDetailsKey = addressDetailsKey;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getValidfromdate() {
        return validFromDate;
    }

    public void setValidfromdate(String validFromDate) {
        this.validFromDate = validFromDate;
    }
    public String getValidtodate() {
        return validToDate;
    }

    public void setValidtodate(String validToDate) {
        this.validToDate = validToDate;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }

    public xal_Address getXal_address() {
        return xal_address;
    }

    public void setXal_address(xal_Address xal_address) {
        this.xal_address = xal_address;
    }

}