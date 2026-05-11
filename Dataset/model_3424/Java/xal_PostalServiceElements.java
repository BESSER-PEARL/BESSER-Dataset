





import java.util.List;
import java.util.ArrayList;

public class xal_PostalServiceElements  {

    private String any;
    private String anyAttribute;
    private String type;





    private xal_AddressDetails xal_addressdetails;


    public xal_PostalServiceElements(
        String any,        String anyAttribute,        String type    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.type = type;
    }


    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xal_AddressDetails getXal_addressdetails() {
        return xal_addressdetails;
    }

    public void setXal_addressdetails(xal_AddressDetails xal_addressdetails) {
        this.xal_addressdetails = xal_addressdetails;
    }

}