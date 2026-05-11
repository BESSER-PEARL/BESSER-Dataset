





import java.util.List;
import java.util.ArrayList;

public class xal_Locality  {

    private String any;
    private String type;
    private String anyAttribute;
    private String usageType;
    private String indicator;





    private xal_Country xal_country;




    private xal_AdministrativeArea xal_administrativearea;




    private xal_AddressDetails xal_addressdetails;


    public xal_Locality(
        String any,        String type,        String anyAttribute,        String usageType,        String indicator    ) {
        this.any = any;
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.usageType = usageType;
        this.indicator = indicator;
    }


    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
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
    public String getIndicator() {
        return indicator;
    }

    public void setIndicator(String indicator) {
        this.indicator = indicator;
    }

    public xal_Country getXal_country() {
        return xal_country;
    }

    public void setXal_country(xal_Country xal_country) {
        this.xal_country = xal_country;
    }
    public xal_AdministrativeArea getXal_administrativearea() {
        return xal_administrativearea;
    }

    public void setXal_administrativearea(xal_AdministrativeArea xal_administrativearea) {
        this.xal_administrativearea = xal_administrativearea;
    }
    public xal_AddressDetails getXal_addressdetails() {
        return xal_addressdetails;
    }

    public void setXal_addressdetails(xal_AddressDetails xal_addressdetails) {
        this.xal_addressdetails = xal_addressdetails;
    }

}