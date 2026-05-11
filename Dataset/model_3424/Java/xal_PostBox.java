





import java.util.List;
import java.util.ArrayList;

public class xal_PostBox  {

    private String type;
    private String indicator;
    private String any;
    private String anyAttribute;





    private xal_PostOffice xal_postoffice;




    private xal_Locality xal_locality;




    private xal_DependentLocality xal_dependentlocality;




    private xal_PostBoxNumberExtension xal_postboxnumberextension;




    private xal_PostalCode xal_postalcode;




    private List<xal_AddressLine> xal_addresslines;


    public xal_PostBox(
        String type,        String indicator,        String any,        String anyAttribute    ) {
        this.type = type;
        this.indicator = indicator;
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.xal_addresslines = new ArrayList<>();
    }

    public xal_PostBox(
        String type,        String indicator,        String any,        String anyAttribute        ArrayList<xal_AddressLine> xal_addresslines    ) {
        this.type = type;
        this.indicator = indicator;
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.xal_addresslines = xal_addresslines;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIndicator() {
        return indicator;
    }

    public void setIndicator(String indicator) {
        this.indicator = indicator;
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

    public xal_PostOffice getXal_postoffice() {
        return xal_postoffice;
    }

    public void setXal_postoffice(xal_PostOffice xal_postoffice) {
        this.xal_postoffice = xal_postoffice;
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
    public xal_PostBoxNumberExtension getXal_postboxnumberextension() {
        return xal_postboxnumberextension;
    }

    public void setXal_postboxnumberextension(xal_PostBoxNumberExtension xal_postboxnumberextension) {
        this.xal_postboxnumberextension = xal_postboxnumberextension;
    }
    public xal_PostalCode getXal_postalcode() {
        return xal_postalcode;
    }

    public void setXal_postalcode(xal_PostalCode xal_postalcode) {
        this.xal_postalcode = xal_postalcode;
    }
    public List<xal_AddressLine> getXal_addresslines() {
        return xal_addresslines;
    }

    public void addXal_addressline(Xal_addressline xal_addressline) {
        this.xal_addresslines.add(xal_addressline);
    }

}