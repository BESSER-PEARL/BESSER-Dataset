





import java.util.List;
import java.util.ArrayList;

public class xal_LargeMailUser  {

    private String any;
    private String type;
    private String anyAttribute;





    private List<xal_BuildingName> xal_buildingnames;




    private xal_Thoroughfare xal_thoroughfare;




    private xal_PostBox xal_postbox;




    private xal_Department xal_department;




    private xal_DependentLocality xal_dependentlocality;




    private xal_PostalCode xal_postalcode;




    private List<xal_AddressLine> xal_addresslines;




    private xal_Locality xal_locality;


    public xal_LargeMailUser(
        String any,        String type,        String anyAttribute    ) {
        this.any = any;
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.xal_buildingnames = new ArrayList<>();
        this.xal_addresslines = new ArrayList<>();
    }

    public xal_LargeMailUser(
        String any,        String type,        String anyAttribute        ArrayList<xal_BuildingName> xal_buildingnames,        ArrayList<xal_AddressLine> xal_addresslines    ) {
        this.any = any;
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.xal_buildingnames = xal_buildingnames;
        this.xal_addresslines = xal_addresslines;
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

    public List<xal_BuildingName> getXal_buildingnames() {
        return xal_buildingnames;
    }

    public void addXal_buildingname(Xal_buildingname xal_buildingname) {
        this.xal_buildingnames.add(xal_buildingname);
    }
    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
    }
    public xal_PostBox getXal_postbox() {
        return xal_postbox;
    }

    public void setXal_postbox(xal_PostBox xal_postbox) {
        this.xal_postbox = xal_postbox;
    }
    public xal_Department getXal_department() {
        return xal_department;
    }

    public void setXal_department(xal_Department xal_department) {
        this.xal_department = xal_department;
    }
    public xal_DependentLocality getXal_dependentlocality() {
        return xal_dependentlocality;
    }

    public void setXal_dependentlocality(xal_DependentLocality xal_dependentlocality) {
        this.xal_dependentlocality = xal_dependentlocality;
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
    public xal_Locality getXal_locality() {
        return xal_locality;
    }

    public void setXal_locality(xal_Locality xal_locality) {
        this.xal_locality = xal_locality;
    }

}