





import java.util.List;
import java.util.ArrayList;

public class xal_Department  {

    private String any;
    private String anyAttribute;
    private String type;





    private List<xal_AddressLine> xal_addresslines;




    private xal_PostalCode xal_postalcode;


    public xal_Department(
        String any,        String anyAttribute,        String type    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.xal_addresslines = new ArrayList<>();
    }

    public xal_Department(
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
    public xal_PostalCode getXal_postalcode() {
        return xal_postalcode;
    }

    public void setXal_postalcode(xal_PostalCode xal_postalcode) {
        this.xal_postalcode = xal_postalcode;
    }

}