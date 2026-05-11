





import java.util.List;
import java.util.ArrayList;

public class xal_PostalRoute  {

    private String any;
    private String anyAttribute;
    private String type;





    private List<xal_AddressLine> xal_addresslines;




    private xal_Locality xal_locality;




    private xal_DependentLocality xal_dependentlocality;




    private xal_PostBox xal_postbox;




    private xal_PostOffice xal_postoffice;


    public xal_PostalRoute(
        String any,        String anyAttribute,        String type    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.xal_addresslines = new ArrayList<>();
    }

    public xal_PostalRoute(
        String any,        String anyAttribute,        String type        ArrayList<xal_AddressLine> xal_addresslines    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.xal_addresslines = xal_addresslines;
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

    public List<xal_AddressLine> getXal_addresslines() {
        return xal_addresslines;
    }

    public void addXal_addressline(Xal_addressline xal_addressline) {
        this.xal_addresslines.add(xal_addressline);
    }
    public xal_Locality getXal_locality() {
        return xal_locality;
    }

    public void setXal_locality(xal_Locality xal_locality) {
        this.xal_locality = xal_locality;
    }
    public xal_DependentLocality getXal_dependentlocality() {
        return xal_dependentlocality;
    }

    public void setXal_dependentlocality(xal_DependentLocality xal_dependentlocality) {
        this.xal_dependentlocality = xal_dependentlocality;
    }
    public xal_PostBox getXal_postbox() {
        return xal_postbox;
    }

    public void setXal_postbox(xal_PostBox xal_postbox) {
        this.xal_postbox = xal_postbox;
    }
    public xal_PostOffice getXal_postoffice() {
        return xal_postoffice;
    }

    public void setXal_postoffice(xal_PostOffice xal_postoffice) {
        this.xal_postoffice = xal_postoffice;
    }

}