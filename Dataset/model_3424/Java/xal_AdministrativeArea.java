





import java.util.List;
import java.util.ArrayList;

public class xal_AdministrativeArea  {

    private String anyAttribute;
    private String usageType;
    private String any;
    private String indicator;
    private String type;





    private xal_Country xal_country;




    private xal_AddressDetails xal_addressdetails;


    public xal_AdministrativeArea(
        String anyAttribute,        String usageType,        String any,        String indicator,        String type    ) {
        this.anyAttribute = anyAttribute;
        this.usageType = usageType;
        this.any = any;
        this.indicator = indicator;
        this.type = type;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getUsagetype() {
        return usageType;
    }

    public void setUsagetype(String usageType) {
        this.usageType = usageType;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getIndicator() {
        return indicator;
    }

    public void setIndicator(String indicator) {
        this.indicator = indicator;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xal_Country getXal_country() {
        return xal_country;
    }

    public void setXal_country(xal_Country xal_country) {
        this.xal_country = xal_country;
    }
    public xal_AddressDetails getXal_addressdetails() {
        return xal_addressdetails;
    }

    public void setXal_addressdetails(xal_AddressDetails xal_addressdetails) {
        this.xal_addressdetails = xal_addressdetails;
    }

}