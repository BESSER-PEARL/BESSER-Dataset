





import java.util.List;
import java.util.ArrayList;

public class xal_Country  {

    private String any;
    private String anyAttribute;





    private xal_AddressDetails xal_addressdetails;


    public xal_Country(
        String any,        String anyAttribute    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
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

    public xal_AddressDetails getXal_addressdetails() {
        return xal_addressdetails;
    }

    public void setXal_addressdetails(xal_AddressDetails xal_addressdetails) {
        this.xal_addressdetails = xal_addressdetails;
    }

}