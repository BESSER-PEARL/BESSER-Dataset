





import java.util.List;
import java.util.ArrayList;

public class xal_PostTown  {

    private String type;
    private String anyAttribute;





    private List<xal_PostTownName> xal_posttownnames;




    private xal_PostTownSuffix xal_posttownsuffix;




    private List<xal_AddressLine> xal_addresslines;




    private xal_PostalCode xal_postalcode;


    public xal_PostTown(
        String type,        String anyAttribute    ) {
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.xal_posttownnames = new ArrayList<>();
        this.xal_addresslines = new ArrayList<>();
    }

    public xal_PostTown(
        String type,        String anyAttribute        ArrayList<xal_PostTownName> xal_posttownnames,        ArrayList<xal_AddressLine> xal_addresslines    ) {
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.xal_posttownnames = xal_posttownnames;
        this.xal_addresslines = xal_addresslines;
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

    public List<xal_PostTownName> getXal_posttownnames() {
        return xal_posttownnames;
    }

    public void addXal_posttownname(Xal_posttownname xal_posttownname) {
        this.xal_posttownnames.add(xal_posttownname);
    }
    public xal_PostTownSuffix getXal_posttownsuffix() {
        return xal_posttownsuffix;
    }

    public void setXal_posttownsuffix(xal_PostTownSuffix xal_posttownsuffix) {
        this.xal_posttownsuffix = xal_posttownsuffix;
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